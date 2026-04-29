# 08. Gateway Selection (GSLB)

**Escalation Bug Count**: 9 | **Regression**: 4 (44%) | **Day-1**: 4 (44%) | **Test Gap**: 5 (56%)

📋 **[Test Cases — Google Sheet](https://docs.google.com/spreadsheets/d/1ackCZ-EcepXw1BkSGoi5Go9Ex1I72-fXqcqLGMGiuio/edit?gid=1966867652#gid=1966867652)**

> This chapter covers how NSClient selects the optimal Netskope gateway (POP) using Global Server Load Balancing. The GSLB subsystem is the critical path between config download and tunnel establishment -- a wrong POP selection directly impacts user-perceived latency, while a stale POP list can cause connection failures. Nine escalation bugs span POP selection, proxy integration, DTLS fallback, GSLB refresh, and on-prem detection via egress IP.

---

## Overview

NSClient must connect to a Netskope Point of Presence (POP) to steer traffic. With 70+ POPs worldwide, selecting the *right* one matters: a user in Tokyo connecting to a US-East POP adds 150+ ms of unnecessary latency to every request. GSLB solves this by combining server-side geo-intelligence with client-side RTT measurements to produce an ordered POP list ranked by actual network proximity.

The highest-risk area in gateway selection is the **POP selection logic under adverse conditions** (S2): when egress IP mismatches, proxy settings are lost during upgrades, or GSLB state is not refreshed after reboot, users connect to suboptimal or wrong POPs. Four of nine bugs are regressions (44%), and the regression chain from ENG-445563 (wrong POP fix) to ENG-503501 (DTLS fallback broken) demonstrates how GSLB changes can cascade into tunnel protocol failures.

**Design Decision: Two-Phase Selection with Server Authority**

The client does NOT autonomously pick a POP. Instead, it follows a two-phase protocol:
1. **Phase 1 (Fetch)**: Client asks the GSLB service for candidate POPs. The server uses the client's egress IP to pre-sort by geographic distance.
2. **Phase 2 (Measure + Post)**: Client measures RTT to each candidate, posts measurements back, and the server returns the *final* ordered list factoring in both RTT and server-side load/health data.

This design gives the server ultimate control over POP assignment (for capacity planning, maintenance windows, geo-fencing) while still optimizing for client-perceived latency.

**Design Decision: Separate GSLB Paths for SWG and NPA**

SWG (Secure Web Gateway) tunnels and NPA (Private Access) tunnels use different GSLB endpoints and selection logic. NPA adds a broker selection layer with cloud brokers, local brokers (LBR), and on-prem/off-prem awareness. This separation exists because NPA has fundamentally different topology requirements -- a private app may only be reachable through a specific local broker.

---

## SWG Gateway Selection Flow (All Platforms)

The SWG GSLB flow is the primary gateway selection path used by all platforms. It runs on tunnel manager initialization and refreshes every 14 minutes. This flow contains the majority of confirmed escalation bugs: wrong POP selection due to egress IP mismatch (ENG-398819), stale GSLB state after reboot (ENG-659009), and proxy settings lost during upgrade (ENG-463329). The flow below shows where each bug strikes.

```mermaid
flowchart TD
    START[TunnelMgr triggers<br/>updateGSLB] --> CONFIG_CHECK{GSLB enabled?<br/>gslb.host + tenantId}

    CONFIG_CHECK -->|No| DNS_ONLY[Use DNS-resolved<br/>gateway only]
    CONFIG_CHECK -->|Yes| PROXY_SETUP["Set proxy list<br/>+ proxy params"]

    PROXY_SETUP --> BUG_PROXY["🔴 BUG ENG-463329<br/>Proxy settings lost<br/>after R115 upgrade"]

    PROXY_SETUP --> FETCH["Phase 1: Fetch candidates<br/>GET /api/v0.2/footprint/{tenantKey}<br/>?limit=25&device_id=...&traffic_mode=..."]

    FETCH -->|HTTP 200| PARSE["parseGSLBResponse()<br/>Extract POP list + egress_ip<br/>+ client_country"]
    FETCH -->|HTTP 304| REUSE[Reuse cached POP list]
    FETCH -->|HTTP 250| DECOMMISSION[Clear POP list<br/>Tenant decommissioned]
    FETCH -->|Connect failed| BACKOFF["Exponential backoff<br/>2 -> 4 -> 8 -> 14 min"]

    PARSE --> EGRESS_CHECK["Record egress_ip<br/>from GSLB response"]
    EGRESS_CHECK --> BUG_EGRESS["🔴 BUG ENG-398819<br/>Egress IP from corporate proxy<br/>causes wrong POP region"]

    EGRESS_CHECK --> RTT["Phase 2: calculateRTT()<br/>Thread per POP<br/>TCP or HTTP probe"]
    REUSE --> RTT

    RTT --> ANOMALY{Any POP RTT<br/>> 250ms?}
    ANOMALY -->|Yes| USE_DIFF["Use connect duration<br/>for ALL POPs"]
    ANOMALY -->|No| USE_RTT[Use kernel RTT]

    USE_DIFF --> POST["Phase 3: POST RTT data<br/>to GSLB service"]
    USE_RTT --> POST

    POST --> SERVER_ORDER["Server returns final<br/>ordered POP list"]
    SERVER_ORDER --> BUG_POP["🔴 BUG ENG-445563<br/>Connected to non-optimal POP<br/>despite better options"]

    SERVER_ORDER --> COMPARE{Top POP changed<br/>vs current?}
    COMPARE -->|Same| DONE[Keep current POP]
    COMPARE -->|Different| REEVAL["Phase 4: Re-evaluation<br/>Repeat RTT + POST once"]

    REEVAL --> CONNECT["gslbConnect()<br/>Iterate ordered POP list"]

    BACKOFF --> PROXY_TOGGLE{Toggle proxy<br/>and retry?}
    PROXY_TOGGLE -->|Yes| BUG_PROXY_RETAIN["🔴 BUG ENG-406879<br/>Stale proxy details<br/>retained after removal"]
    PROXY_TOGGLE -->|No| DNS_ONLY

    DNS_ONLY --> CONNECT

    CONNECT -->|Success| TUNNEL_UP[Tunnel connected]
    CONNECT -->|All POPs failed| FALLBACK["DNS fallback:<br/>primary + backup host"]
    FALLBACK -->|Success| TUNNEL_UP
    FALLBACK -->|Failed| DISCONNECTED[Tunnel disconnected]
```

### Node Risk Assessment

| Node | Risk | Assessment |
|---|---|---|
| TunnelMgr triggers updateGSLB | 🟡 Medium | **ENG-659009**: After reboot, `m_lastUpdateTime` not reset -- GSLB update skipped |
| GSLB enabled check | 🟢 Low | Simple config key check |
| Set proxy list + params | 🔴 High | **ENG-463329**: Proxy settings lost after R115 upgrade; **ENG-406879**: Stale proxy retained after removal |
| Phase 1: Fetch candidates | 🟡 Medium | Network-dependent; backoff logic handles transient failures |
| parseGSLBResponse + egress_ip | 🔴 High | **ENG-398819**: Corporate proxy egress IP causes wrong geo-region POP list |
| Phase 2: calculateRTT() | 🟡 Medium | Anomaly threshold at 250ms can force less accurate measurements for all POPs |
| Phase 3: POST RTT data | 🟢 Low | Server-side processing; client just posts data |
| Server-ordered POP list | 🔴 High | **ENG-445563**: Server returns non-optimal ordering; stickiness evaluation may prevent switch |
| Phase 4: Re-evaluation | 🟡 Medium | Single re-evaluation iteration; could be insufficient if conditions change rapidly |
| gslbConnect() iteration | 🟡 Medium | POP list exhaustion falls back to DNS -- China geo-fence blocks DNS fallback |
| DNS fallback | 🟡 Medium | Predicted risk: geo-fence + DNS failure = no connectivity path |

---

## Tunnel Connection with GSLB POPs (All Platforms)

When the tunnel is ready to connect, `NSTunnel::gslbConnect()` builds a gateway list from the GSLB-ordered POPs and falls back to DNS-resolved gateways. The DTLS-to-TLS fallback path is where ENG-503501 struck -- a fix for ENG-445563 inadvertently broke the fallback logic.

```mermaid
flowchart TD
    START[gslbConnect called] --> GSLB_CHECK{GSLB enabled?}

    GSLB_CHECK -->|Yes| GET_POPS[Get ordered POPs from config]
    GSLB_CHECK -->|No| DNS_ONLY[Use DNS-resolved gateway only]

    GET_POPS --> BUILD_LIST["Build gateway list from ordered POPs:<br/>gw.FQDN, gw.IP, pop_name, viaProxy"]

    BUILD_LIST --> GEO_CHECK{China DC<br/>Geo-fence?}
    GEO_CHECK -->|No| ADD_DNS["Append DNS-resolved gateways<br/>(primary + backup host)"]
    GEO_CHECK -->|Yes| SKIP_DNS[Skip DNS fallback]

    DNS_ONLY --> ADD_DNS
    ADD_DNS --> ITERATE
    SKIP_DNS --> ITERATE

    ITERATE[Iterate gateway list] --> SET_RESOLVER{Is GSLB gateway?}
    SET_RESOLVER -->|Yes| GSLB_RESOLVER["Set DNS resolver: useGSLBDNS<br/>Pre-set resolved IP from GSLB"]
    SET_RESOLVER -->|No| DEFAULT_RESOLVER["Set DNS resolver: useDefault<br/>Normal EDNS/LDNS resolution"]

    GSLB_RESOLVER --> DTLS_TRY{DTLS enabled?}
    DEFAULT_RESOLVER --> DTLS_TRY

    DTLS_TRY -->|Yes| DTLS[Attempt DTLS connection]
    DTLS_TRY -->|No| TLS[Attempt TLS connection]

    DTLS -->|Success| DONE[Tunnel connected to POP]
    DTLS -->|Failed| DTLS_FALLBACK{dtlsFallback<br/>enabled?}
    DTLS_FALLBACK -->|Yes| TLS
    DTLS_FALLBACK -->|No| BUG_DTLS["🔴 BUG ENG-503501<br/>DTLS no fallback to TLS<br/>(regression from ENG-445563 fix)"]

    TLS -->|Success| DONE
    TLS -->|Failed| REACHABLE{Network reachable?}

    REACHABLE -->|No| ABORT[Stop -- network down]
    REACHABLE -->|Yes| NEXT[Try next gateway in list]

    NEXT -->|More gateways| ITERATE
    NEXT -->|No more| DISCONNECTED[Tunnel disconnected]

    BUG_DTLS --> NEXT
```

### Node Risk Assessment

| Node | Risk | Assessment |
|---|---|---|
| Get ordered POPs from config | 🟡 Medium | Returns empty list if GSLB fetch failed |
| Build gateway list | 🟢 Low | Deterministic list construction |
| China DC Geo-fence check | 🟡 Medium | Blocks DNS fallback entirely for China tenants |
| Iterate gateway list | 🟢 Low | Simple loop |
| GSLB resolver (useGSLBDNS) | 🟢 Low | Bypasses DNS resolution entirely -- uses IP from GSLB |
| Attempt DTLS connection | 🟡 Medium | DTLS handshake can fail silently in restrictive networks |
| DTLS fallback to TLS | 🔴 High | **ENG-503501**: Regression from POP selection fix broke TLS fallback path |
| Network reachable check | 🟡 Medium | `isNetworkReachable()` probes nearest successful endpoint; false negative possible |
| DNS fallback | 🟡 Medium | Last resort; blocked by China geo-fence |

---

## Periodic RTT Re-evaluation and POP Switching (All Platforms)

Once a tunnel is connected, the tunnel manager periodically checks whether the client should switch to a better POP. The GSLB refresh after reboot is where ENG-659009 manifested -- the `m_lastUpdateTime` was not reset on service restart, causing the interval check to skip the update even when the network environment had changed.

```mermaid
flowchart TD
    CONNECTED[Tunnel connected to POP X] --> TIMER["Periodic check in workerThread<br/>(every ~15 minutes)"]

    TIMER --> REBOOT_CHECK{"Service just<br/>restarted?"}
    REBOOT_CHECK -->|Yes| FORCE_UPDATE["Force GSLB update<br/>(resetGatewaySelection)"]
    REBOOT_CHECK -->|No| PINNED{POP pinned<br/>by user?}

    FORCE_UPDATE --> BUG_REBOOT["🔴 BUG ENG-659009<br/>m_lastUpdateTime not reset<br/>on service restart"]
    FORCE_UPDATE --> GSLB_PATH

    PINNED -->|Yes| STAY[Stay on current POP]
    PINNED -->|No| PROXY_CHECK{Connected<br/>via proxy?}

    PROXY_CHECK -->|Yes| STAY
    PROXY_CHECK -->|No| GSLB_CHECK{GSLB enabled?}

    GSLB_CHECK -->|Yes| GSLB_PATH[GSLB-based re-evaluation]
    GSLB_CHECK -->|No| LEGACY_PATH[Legacy DNS-based re-evaluation]

    GSLB_PATH --> UPDATE_GW["updateGateway(currentPop)<br/>Full GSLB cycle: fetch + RTT + post"]
    UPDATE_GW --> COMPARE{New top POP IP<br/>!= current IP?}
    COMPARE -->|Same| NO_SWITCH[No switch needed]
    COMPARE -->|Different| TEST_CONNECT["gslbConnect() probe to new POP<br/>TCP connect port 443, timeout 3s"]
    TEST_CONNECT -->|Reachable| SWITCH["Disconnect current tunnel<br/>Reconnect to new POP"]
    TEST_CONNECT -->|Unreachable| SKIP["Skip reconnect<br/>(log: gslb skip reconnect)"]

    LEGACY_PATH --> DNS_RESOLVE["Resolve nsgwHost via DNS"]
    DNS_RESOLVE --> IP_CHANGED{Resolved IP<br/>!= connected IP?}
    IP_CHANGED -->|Same| NO_SWITCH_L[No switch needed]
    IP_CHANGED -->|Different| RTT_COMPARE["Compare 3 RTT measurements<br/>New must be < current by 50%+"]
    RTT_COMPARE -->|Better by 50%+| SWITCH_L["Disconnect and reconnect"]
    RTT_COMPARE -->|Not enough improvement| NO_SWITCH_L

    SWITCH --> RISK_RACE["🟡 Warning: Race condition<br/>between reset() and updateGateway()<br/>during network change"]
```

---

## Windows

**Bug Count**: 7 direct | **Key Gaps**: GSLB refresh after reboot, proxy integration, POP selection accuracy, DTLS fallback

Windows accounts for the majority of GSLB escalation bugs. The most dangerous failure pattern is the regression chain where fixing POP selection (ENG-445563) broke DTLS-to-TLS fallback (ENG-503501). Windows is also the only platform where proxy integration issues have been reported (ENG-463329, ENG-406879).

### Windows GSLB + Tunnel Connection Flow

This flow shows the complete Windows-specific path from GSLB initialization through tunnel establishment, annotated with all confirmed bugs on Windows.

```mermaid
flowchart TD
    START[Windows TunnelMgr<br/>workerThread start] --> REBOOT{Service<br/>restarted?}

    REBOOT -->|Yes| RESET["resetGatewaySelection()<br/>Clear m_lastUpdateTime"]
    REBOOT -->|No| INTERVAL{Update interval<br/>elapsed?}

    RESET --> BUG_RESET["🔴 BUG ENG-659009<br/>GSLB not refreshed after reboot<br/>stale POP list used"]
    RESET --> GSLB_UPDATE

    INTERVAL -->|Yes| GSLB_UPDATE[updateGSLB]
    INTERVAL -->|No| SKIP[Skip GSLB update]

    GSLB_UPDATE --> PROXY_DETECT["Detect system proxy<br/>(WinHTTP + System Proxy)"]
    PROXY_DETECT --> BUG_PROXY_LOST["🔴 BUG ENG-463329<br/>Local proxy not used after<br/>R115 upgrade (regression)"]
    PROXY_DETECT --> BUG_PROXY_STALE["🔴 BUG ENG-406879<br/>Stale proxy retained<br/>after proxy removed"]

    PROXY_DETECT --> FETCH[GSLB Phase 1: Fetch POPs]

    FETCH --> EGRESS["Parse egress_ip<br/>from response"]
    EGRESS --> BUG_WRONG_POP["🔴 BUG ENG-398819<br/>Corporate proxy egress IP<br/>causes wrong POP region"]

    EGRESS --> RTT_MEASURE[Phase 2: RTT measurement<br/>TCP or HTTP per POP]

    RTT_MEASURE --> POST_RTT[Phase 3: POST measurements]
    POST_RTT --> ORDERED[Server-ordered POP list]

    ORDERED --> BUG_NON_OPTIMAL["🔴 BUG ENG-445563<br/>Connected to non-optimal POP<br/>BUE1 instead of nearest"]

    ORDERED --> CONNECT[gslbConnect: iterate POPs]

    CONNECT --> DTLS_ATTEMPT{DTLS enabled?}
    DTLS_ATTEMPT -->|Yes| DTLS[Attempt DTLS]
    DTLS_ATTEMPT -->|No| TLS[Attempt TLS]

    DTLS -->|Success| CONNECTED[Tunnel connected]
    DTLS -->|Failed| FALLBACK{DTLS fallback?}
    FALLBACK -->|No| BUG_NO_FALLBACK["🔴 BUG ENG-503501<br/>DTLS no fallback to TLS<br/>(regression from ENG-445563 fix)"]
    FALLBACK -->|Yes| TLS

    TLS -->|Success| CONNECTED
    TLS -->|Failed| NEXT_POP{More POPs?}
    NEXT_POP -->|Yes| CONNECT
    NEXT_POP -->|No| DNS_FALLBACK[DNS-resolved gateway]
    DNS_FALLBACK -->|Failed| DISCONNECTED[Tunnel disconnected]
    DNS_FALLBACK -->|Success| CONNECTED

    CONNECTED --> BUG_OUT_COUNTRY["🔴 BUG ENG-614375<br/>Connected to out-of-country POP<br/>after primary POP unreachable"]
```

## macOS

**Bug Count**: 0 direct (shared code path with Windows for GSLB core) | **Key Gaps**: Same GSLB logic as Windows but no macOS-specific escalation bugs yet

macOS shares the same `GatewaySelection` C++ code as Windows for GSLB core logic. The captive portal grace period issue (ENG-548975, categorized under FailClose) has a GSLB timing dependency on macOS -- the original code reset captive portal status after tunnel worker thread start, but GSLB checking introduces a 20-second delay.

## Linux

*No GSLB-specific escalation bugs on Linux.* Linux uses the same `GatewaySelection` code path. The egress IP on-prem detection issue (ENG-851222) noted that Linux also had an Egress IP feature issue tracked by a separate ticket.

## Android

**Bug Count**: 1 direct (ENG-846458) | **Key Gaps**: UI gateway display, socket protection for GSLB

Android has a unique requirement: `setsockprotect()` must be called on GSLB sockets to prevent routing loops through the VPN tunnel. Additionally, Android monitors `isEgressIPUpdated()` in the tunnel worker thread and triggers `handleOnPremStatusChange()` on egress IP change. The on-prem detection regression (ENG-918451) was an Android fix that broke Windows behavior.

### Android-Specific Behavior

- **Socket protection**: `setsockprotect()` required on GSLB sockets
- **Egress IP monitoring**: Explicit `isEgressIPUpdated()` check triggers on-prem re-evaluation
- **API version fallback**: May use v0.1 API with orgKey when tenant ID is unavailable
- **UI gateway display**: ENG-846458 -- shows tenant hostname instead of POP name

## iOS

*No GSLB-specific escalation bugs on iOS.* iOS may use API v0.1 with orgKey fallback for older clients.

## ChromeOS

*No GSLB-specific escalation bugs on ChromeOS.* ChromeOS uses the Android GSLB code path.

---

## Backend

*No backend-specific GSLB escalation bugs.* However, the GSLB service is the authoritative component for POP ordering, and server-side issues (load balancing overrides, geo-database mismatches) can cause wrong POP selection even when the client logic is correct.

---

## NPA Gateway Selection (All Platforms)

NPA uses a more complex selection system with three types of brokers: cloud, local public, and local private. The NPA broker selection path adds on-prem/off-prem awareness that interacts with the egress IP detection bugs (ENG-851222, ENG-918451).

```mermaid
flowchart TD
    START[NPA Tunnel needs gateway] --> CHECK_FF{GSLB Broker Selection<br/>Feature Flag enabled?}

    CHECK_FF -->|Yes| BROKER_PATH[New Broker Selection Path]
    CHECK_FF -->|No| LEGACY_PATH[Legacy Path]

    subgraph New Broker Selection
        BROKER_PATH --> INIT_FB["Initialize fallback settings<br/>based on on-prem/off-prem"]
        INIT_FB --> FETCH_BROKERS["FetchBrokerListFromTenant()<br/>GET npa-gateway/footprint/{tenantKey}<br/>Returns cloud + local brokers"]
        FETCH_BROKERS --> RTT_BROKERS["calculateRTTForNpaBrokers()<br/>Thread per broker, same RTT logic"]
        RTT_BROKERS --> POST_RTT["PostRttAndGetBrokerInOrder()<br/>POST measured RTTs"]
        POST_RTT --> STORE["Store sorted brokers"]
    end

    subgraph Legacy Path
        LEGACY_PATH --> LBR_CHECK{Local Broker<br/>configured?}
        LBR_CHECK -->|Yes| LBR_RESOLVE["Resolve LBR via DNS<br/>Random selection from IPs"]
        LBR_CHECK -->|No| GSLB_CHECK{GSLB enabled?}
        LBR_RESOLVE -->|Failed| GSLB_CHECK

        GSLB_CHECK -->|Yes| NPA_GSLB["NPA-specific GSLB endpoint<br/>/api/v0.2/npa/footprint/{tenantKey}"]
        GSLB_CHECK -->|No| EDNS_LDNS["Resolve via EDNS then LDNS"]
        NPA_GSLB -->|Failed + fallback enabled| EDNS_LDNS
        NPA_GSLB -->|Failed + fallback disabled| FAIL["🟡 Warning: No gateway path<br/>when npa_gslb_client_no_fallback=true"]
    end

    INIT_FB --> ONPREM_RISK["🟡 Warning: On-prem/off-prem<br/>detection via egress IP<br/>See ENG-851222, ENG-918451"]
```

### NPA Broker Types

| Type | Key | Description |
|------|-----|-------------|
| Cloud Broker | `"cloud"` | Standard Netskope POP acting as NPA gateway |
| Local Broker (Public) | `"local_public"` | On-premises broker reachable via public network |
| Local Broker (Private) | `"local_private"` | On-premises broker reachable only via private network |

## Automation Coverage Summary

| Test Area | Coverage | Notes |
|-----------|----------|-------|
| Basic GSLB POP selection | ❌ Not covered | No automated verification that nearest POP is selected |
| GSLB refresh after reboot | ❌ Not covered | ENG-659009: Deepthi added cases to TestRail but automation status unclear |
| GSLB with proxy | ⚠️ Partial | Existing GSLB+proxy test case exists per Deepthi; ENG-463329 gap unclear |
| DTLS-to-TLS fallback | ❌ Not covered | ENG-503501 regression chain not automated |
| POP pinning lifecycle | ✅ Covered | GRS `nplan-5878-pop_pinning/test_pop_pinning.py` covers pin/unpin lifecycle |
| Wrong POP (egress IP) | ❌ Not covered | ENG-398819: Deepthi notes negative cases exist in TestRail |
| Out-of-country POP fallback | ❌ Not covered | ENG-614375: Block POP + verify next closest |
| GSLB backoff timer | ❌ Not covered | |
| China DC geo-fence | ❌ Not covered | |
| NPA broker selection | ❌ Not covered | |
| On-prem egress IP detection | ⚠️ Partial | `nplan_5628_onpremises_profiles` tests transitions but not tunnel reconnect |

---

## Cross-Flow Interactions

### GSLB + Tunnel Establishment + FailClose

The most dangerous cross-flow interaction in gateway selection is the cascade from GSLB failure through tunnel establishment to FailClose activation. When GSLB fails and the client cannot connect to any POP or DNS gateway, FailClose may activate and block all traffic. The GSLB timing also affects captive portal detection (ENG-548975).

```mermaid
sequenceDiagram
    participant OS as OS Network Event
    participant TM as TunnelMgr
    participant GSLB as GatewaySelection
    participant TUN as NSTunnel
    participant FC as FailCloseMgr

    Note over OS: Network change detected

    OS->>TM: Network change callback
    TM->>GSLB: resetGatewaySelection()
    Note over GSLB: 🔴 ENG-659009: Reset may not<br/>clear m_lastUpdateTime

    TM->>GSLB: updateGSLB(force=true)
    GSLB->>GSLB: fetchTenantInfo()
    Note over GSLB: 🔴 ENG-398819: Egress IP<br/>from wrong region
    GSLB->>GSLB: calculateRTT()
    GSLB->>GSLB: PostClientRTTMeasurements()
    GSLB-->>TM: Ordered POP list

    TM->>TUN: gslbConnect()
    TUN->>TUN: Try DTLS to POP #1
    Note over TUN: 🔴 ENG-503501: DTLS failure<br/>may not fall back to TLS
    TUN->>TUN: Try TLS to POP #1
    TUN->>TUN: Try POP #2...N
    TUN-->>TM: All POPs failed

    TM->>TUN: DNS fallback
    TUN-->>TM: DNS also failed

    TM->>FC: Tunnel disconnected
    Note over FC: 🟡 Risk: FailClose activated<br/>All traffic blocked<br/>See Chapter 11
```

### Regression Chain: POP Selection Fix Breaks DTLS Fallback

This is a documented regression chain from the escalation bug analysis. The fix for ENG-445563 (wrong POP) introduced ENG-503501 (DTLS no fallback to TLS). This chain demonstrates why GSLB changes must include DTLS fallback regression tests.

```mermaid
flowchart LR
    A["🔴 ENG-445563<br/>POP selection incorrect"] -->|Fix introduced| B["🔴 ENG-503501<br/>DTLS no fallback to TLS"]
    B -->|Reverted fix| C["POP selection fix<br/>re-implemented safely"]
```

### Cross-Flow Risk Matrix (Chapter-Relevant)

| Cross-Flow | Risk Level | Confirmed Bugs | Chapters |
|---|---|---|---|
| GSLB failure + FailClose | High | ENG-659009 (GSLB stale) + FailClose activation | [07](07_tunnel_management.md), [11](11_failclose.md) |
| POP selection fix + DTLS fallback | High | ENG-445563 -> ENG-503501 regression chain | [07](07_tunnel_management.md) |
| GSLB + Proxy detection | Medium | ENG-463329, ENG-406879 | [14](14_proxy_management.md) |
| Egress IP + On-prem detection | Medium | ENG-851222, ENG-918451 | [12](12_device_classification.md) |
| GSLB timing + Captive portal | Medium | ENG-548975 (GSLB 20s delay) | [11](11_failclose.md) |
| NPA broker + On-prem status | Low | No confirmed bugs yet | [15](15_npa_integration.md) |

## Appendix A: Bug Quick Reference

| Bug ID | Summary | Platform | Root Cause | Severity |
|--------|---------|----------|------------|----------|
| ENG-398819 | GSLB selects wrong POP (DEI wrongly used for ATL2) | Windows | Corporate proxy egress IP causes wrong geo-region | S2 |
| ENG-406879 | NSClient retains proxy details after proxy removed | Windows | Day-1: proxy settings not synced after clearing | S3 |
| ENG-445563 | Connected to non-optimal POP (BUE1) causing poor performance | Windows | GSLB POP selection logic does not handle all cases | S2 |
| ENG-463329 | Client not using local proxy after R115 upgrade | Windows | Regression: proxy settings lost during upgrade | S2 |
| ENG-503501 | DTLS tunnel not failing over to TLS | Windows | Regression from ENG-445563 fix broke TLS fallback | S1 |
| ENG-614375 | Client connecting to out-of-country POP | Windows | When primary POP unreachable, fallback selects random POP instead of next closest | S2 |
| ENG-659009 | GSLB not refreshed after reboot | Windows | Day-1: m_lastUpdateTime not reset on service restart | S2 |
| ENG-846458 | Android Client UI Gateway field not matching other OSes | Android | Day-1: displays tenant hostname instead of POP name | S3 |
| ENG-548975 | Captive portal grace period not working (GSLB timing) | Win/Mac | Day-1: captive portal status reset before GSLB completes (20s delay) | S2 |

**Related bugs from other categories that affect GSLB flows:**

| Bug ID | Summary | Platform | Primary Category | GSLB Impact |
|--------|---------|----------|-----------------|-------------|
| ENG-851222 | On-prem detection using Egress IP does not work | Windows | On-prem Detection | Egress IP from GSLB used for on-prem detection |
| ENG-918451 | Internet Steering not honoring on-prem detection (egressIP) | Windows | On-prem Detection | Android fix caused Windows regression in tunnel reconnect after on-prem switch |

---

## Appendix B: Methodology

### Severity Ratings

| Rating | Definition |
|--------|------------|
| S1 | Complete connectivity loss or security bypass affecting all users |
| S2 | Significant degradation (wrong POP = high latency) or partial functionality loss |
| S3 | Minor inconvenience or cosmetic issue; workaround available |

### Automation Priority

| Priority | Definition |
|----------|------------|
| P1 | Must automate immediately -- regression risk is high and bug has recurred |
| P2 | Should automate in next sprint -- important coverage gap |
| P3 | Nice to have -- low regression probability or hard to automate |

### Gap Type Taxonomy

| Type | Definition |
|------|------------|
| Regression | Bug introduced by a code change that broke previously working functionality |
| Day-1 | Bug present since feature was first implemented |
| Test Gap | Scenario that was never tested (no test case existed) |
| Corner Case | Unusual environment or configuration that is hard to reproduce |

### Code References

| Component | File |
|-----------|------|
| GatewaySelection core | `lib/nsConfig/GatewaySelection.h/.cpp` |
| NPA cloud POP selection | `lib/npa_core/npaGslbGatewaySelection.h/.cpp` |
| NPA broker selection | `lib/npa_core/npaGslbGatewaySelection.h/.cpp` |
| NPA gateway resolution | `lib/npa_core/npaGWSelection.h/.cpp` |
| Config GSLB wrapper | `lib/nsConfig/config.cpp::updateGSLB()` |
| Tunnel GSLB connect | `lib/nsTunnel/tunnel.cpp::gslbConnect()` |
| Tunnel manager GSLB trigger | `stAgent/stAgentSvc/tunnelMgr.cpp::workerThread()` |
| DNS resolver | `lib/nsUtils/nsDnsResolver.h` |

---

**Related Chapters**: [07. Tunnel Management](07_tunnel_management.md) | [04. Config Download](04_config_download.md) | [05. Steering Config](05_steering_config.md) | [11. FailClose](11_failclose.md) | [14. Proxy Management](14_proxy_management.md) | [15. NPA Integration](15_npa_integration.md) | [12. Device Classification](12_device_classification.md)
