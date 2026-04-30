# Tunneling / Gateway / Connectivity Bugs

Bugs related to tunnel establishment, tunnel disconnect, SPDY/DTLS protocols, gateway selection (GSLB), reconnection, heartbeat, and NPA tunneling.

> Source: Escalation Bug Review spreadsheet, filtered by keywords: tunnel, SPDY, DTLS, gateway, GSLB, reconnect, heartbeat, crash+tunnel.

**Total: 64 bugs**

---

## 1. AI:
- Steering and Bypass  & Flexible dynamic steering -> revist the test plan and Plan for KT
- Come up with extensive coverage on Network/tunnel stability use cases and infrastructure for Mobile
- Share the issues which needs to be taken care by NPA team.
-

**Description**: AI:
- Steering and Bypass  & Flexible dynamic steering -> revist the test plan and Plan for KT
- Come up with extensive coverage on Network/tunnel stability use cases and infrastructure for Mobile
- Share the issues which needs to be taken care by NPA team.
-

| Field | Value |
|-------|-------|
| OS Platform | N/A |
| Feature | N/A |
| Regression | N/A |
| Bug Type | N/A |
| Automatable | N/A |
| Interop | N/A |
| QE Owner | N/A |
| Source Sheet | Escalation Bug-Review Q226 (Feb) |

**Test Case Needed**: N/A

---

## 2. ENG-393015

**Jira**: [ENG-393015](https://netskope.atlassian.net/browse/ENG-393015)

**Description**: ENG-393015 [Win] NSclient with co-existence of NPA tunnel crashes when switching the network.
Duplicate of https://netskope.atlassian.net/browse/ENG-424271

| Field | Value |
|-------|-------|
| OS Platform | Windows |
| Feature | NPA Integration |
| Regression | Yes |
| Bug Type | Internal found |
| Automatable | No |
| Interop | No |
| QE Owner | N/A |
| Source Sheet | Customer Escalations - Overall |

**Test Case Needed**: No

**Comments**:
-  Internal found defect but this issue was there even in the previous release.
- Need  more stress test with NPA integration on Network switch. 
- Integration:NPA

---

## 3. ENG-398819

**Jira**: [ENG-398819](https://netskope.atlassian.net/browse/ENG-398819)

**Description**: ENG-398819 CLONE - [FloridaBlue] - DEI wrongly used for ATL2 POP all though not configured

| Field | Value |
|-------|-------|
| OS Platform | Windows |
| Feature | GSLB |
| Regression | No |
| Bug Type | Test Gap |
| Automatable | Yes |
| Interop | No |
| QE Owner | Deepthi K S |
| Source Sheet | Customer Escalations - Overall |

**Test Case Needed**: yes- https://netskope.testrail.com/index.php?/cases/view/1541879

**Comments**:
- Test case needs detailed steps.
- Need to automate
- Test Gap scope: Negative testing

Deepthi - All the Negative cases related to GSLB and LDNS/EDNS fallback are already part of the Test Rail. I am not sure what is missign here.

---

## 4. ENG-406879

**Jira**: [ENG-406879](https://netskope.atlassian.net/browse/ENG-406879)

**Description**: ENG-406879 NSClient still holds proxy details even after removing the proxy settings

| Field | Value |
|-------|-------|
| OS Platform | Windows |
| Feature | GSLB |
| Regression | Day-1 |
| Bug Type | Enhancement |
| Automatable | Yes |
| Interop | Yes |
| QE Owner | Deepthi K S |
| Source Sheet | Customer Escalations - Overall |

**Test Case Needed**: Yes

**Comments**:
- Design Improvement(ENG-317961)
- Internal reported.
- Can be automatable.
- Test Gap scope: Interop test
- Interop scope: Proxy

Deepthi - This cannot have atest case, as this was just an observation from logs. Tester testign with proxy should monitor this in logs.

---

## 5. ENG-429034

**Jira**: [ENG-429034](https://netskope.atlassian.net/browse/ENG-429034)

**Description**: ENG-429034 CLONE - Android: Tunnel disconnects 1m30s after establishing with TLS SSL_read failed, err: 0, ret: -1, sys_err: 104

| Field | Value |
|-------|-------|
| OS Platform | Android |
| Feature | Data path |
| Regression | Yes |
| Bug Type | Corner case |
| Automatable | No |
| Interop | No |
| QE Owner | Anand Kumar S |
| Source Sheet | Customer Escalations - Overall |

**Test Case Needed**: Yes

**Comments**:
- We have existin g test case and it's a corner case scenario. 
- Issue only happens for the customer environment(Samsung A53,A51)
- Need to add test case with Data to 4G/5G.
- Test Gap scope: platform coverage

---

## 6. ENG-438566

**Jira**: [ENG-438566](https://netskope.atlassian.net/browse/ENG-438566)

**Description**: ENG-438566 CLONE - [D & F Man Capital] [ DNS over TCP - Windows ] R110 | DNS resolution not learnt when DNS is over TCP and tunneled to app-fw

| Field | Value |
|-------|-------|
| OS Platform | Windows |
| Feature | DNS Security |
| Regression | No |
| Bug Type | Enhancement |
| Automatable | Yes |
| Interop | No |
| QE Owner | Abhishek Sharma |
| Source Sheet | Customer Escalations - Overall |

**Test Case Needed**: Yes

**Comments**:
- Need to Add Test case.
- Need to include Automation
- Test Gap scope: Need-Additional Coverage - DNS Security,
Steering&Exception,DNS over TCP.

Test cases added to DNS security, For blockDNSTcp feature and learn TCP dns ip/domain

---

## 7. ENG-445563

**Jira**: [ENG-445563](https://netskope.atlassian.net/browse/ENG-445563)

**Description**: ENG-445563 CLONE - Users connects to POP other than BUE1 causes performance issues

| Field | Value |
|-------|-------|
| OS Platform | Windows |
| Feature | GSLB |
| Regression | Day-1 |
| Bug Type | Test Gap |
| Automatable | Yes |
| Interop | No |
| QE Owner | Deepthi K S |
| Source Sheet | Customer Escalations - Overall |

**Test Case Needed**: Yes

**Comments**:
- ( Same issue ENG-398819 whch was fixed got resurfaced.)
- Need to add test case in testrail.
 - https://netskope.atlassian.net/browse/ENG-445563

Deepthi - ENG-398819 and ENG-445563 are completely different issues. Also this is a duplicate entry rom Row 37

---

## 8. ENG-446763

**Jira**: [ENG-446763](https://netskope.atlassian.net/browse/ENG-446763)

**Description**: ENG-446763 CLONE - {ION Group} Tunnel consistently getting disconnected on iOS

| Field | Value |
|-------|-------|
| OS Platform | iOS |
| Feature | Logging |
| Regression | No |
| Bug Type | Corner case |
| Automatable | No |
| Interop | No |
| QE Owner | N/A |
| Source Sheet | Customer Escalations - Overall |

**Test Case Needed**: No

**Comments**:
-No action
- QE and Dev couldn't replicate this issue.
- Fix is to add Improvement in the logging

---

## 9. ENG-463329

**Jira**: [ENG-463329](https://netskope.atlassian.net/browse/ENG-463329)

**Description**: ENG-463329 CLONE - [NSclient] - Client not using local proxy for tunnel after upgrade to R115

| Field | Value |
|-------|-------|
| OS Platform | Windows |
| Feature | GSLB |
| Regression | Yes |
| Bug Type | Missing in Regression |
| Automatable | Yes |
| Interop | Yes |
| QE Owner | Deepthi K S |
| Source Sheet | Customer Escalations - Overall |

**Test Case Needed**: Yes

**Comments**:
- As per the Support, customer confirms R113 and R114 versions work fine and not with R115. Sounds to be a regression.
- Need to add a test case in GSLB or Proxy.
-Test Gap scope: Interop-Proxy test
- Interop scope: Proxy - squid

Deepthi - GSLB was introduced in R97 and GSLB has a testcase already to test with Proxy. Snehalkumar Donga can confirm if this is automated.

---

## 10. ENG-490822

**Jira**: [ENG-490822](https://netskope.atlassian.net/browse/ENG-490822)

**Description**: ENG-490822 CLONE - [tricare]: One way audio issue for WFC app on Zebra Android phone

| Field | Value |
|-------|-------|
| OS Platform | Android |
| Feature | Steering&Exception |
| Regression | No |
| Bug Type | Test Gap |
| Automatable | Yes |
| Interop | No |
| QE Owner | N/A |
| Source Sheet | Customer Escalations - Overall |

**Test Case Needed**: No

**Comments**:
- review the Bypass by tunnel and Bypass by client cases W/Wo Flexible dynamic steering 
- Test Gap scope: Platform coverage

---

## 11. ENG-503501

**Jira**: [ENG-503501](https://netskope.atlassian.net/browse/ENG-503501)

**Description**: ENG-503501 CLONE - [Macquarie Bank Limited ] DTLS tunnel not failing over to TLS

| Field | Value |
|-------|-------|
| OS Platform | Windows |
| Feature | GSLB |
| Regression | Yes |
| Bug Type | Missing in Regression |
| Automatable | Yes |
| Interop | No |
| QE Owner | Deepthi K S |
| Source Sheet | Customer Escalations - Overall |

**Test Case Needed**: No

**Comments**:
- This regression was caused by ENG-445563
- Fix is to revert back

---

## 12. ENG-528750

**Jira**: [ENG-528750](https://netskope.atlassian.net/browse/ENG-528750)

**Description**: ENG-528750 CLONE - [Analytix] Client Status Tunnel Down Events Not Generated

| Field | Value |
|-------|-------|
| OS Platform | Windows |
| Feature | Client Status |
| Regression | Day-1 |
| Bug Type | Test Gap |
| Automatable | Yes |
| Interop | No |
| QE Owner | Devendra Shirsath |
| Source Sheet | Customer Escalations - Overall |

**Test Case Needed**: Yes

**Comments**:
- Need to add test case.
- Day-1 Issue,  Client status doesn't updates the tunnel status for a particular case.
- Test Gap Scope: Day-1 Issue

---

## 13. ENG-533981

**Jira**: [ENG-533981](https://netskope.atlassian.net/browse/ENG-533981)

**Description**: ENG-533981 CLONE - [Android Client ] Tunnel Flaps in android NS client

| Field | Value |
|-------|-------|
| OS Platform | Android |
| Feature | Steering&Exception |
| Regression | No |
| Bug Type | Test Gap.(Need to add DNS Tunnel health check up case for 1 hr duration) |
| Automatable | No |
| Interop | No |
| QE Owner | Anand Kumar S |
| Source Sheet | Customer Escalations - Overall |

**Test Case Needed**: Yes

**Comments**:
- Need to add a seperate test case for Network Switch with DNS health check.
- Test Gap scope: Negative testing

---

## 14. ENG-538734

**Jira**: [ENG-538734](https://netskope.atlassian.net/browse/ENG-538734)

**Description**: ENG-538734 CLONE - [idfcfirst] Airplay mirroring doesn't work with Crestron Airmedia

| Field | Value |
|-------|-------|
| OS Platform | Mac |
| Feature | DNS Security |
| Regression | Yes |
| Bug Type | Corner case |
| Automatable | Yes |
| Interop | No |
| QE Owner | Kim Shaw |
| Source Sheet | Customer Escalations - Overall |

**Test Case Needed**: Yes

**Comments**:
- need to add detailed test case -https://netskope.testrail.io/index.php?/cases/view/2202460
5353 should be get tunnel as per dns security
https://netskope.atlassian.net/wiki/spaces/CDTBA/pages/3297345704/Netskope+Client+Design+for+DNS+Security
- External software issue (for ex. with Mac OS here)

---

## 15. ENG-548975

**Jira**: [ENG-548975](https://netskope.atlassian.net/browse/ENG-548975)

**Description**: ENG-548975 CLONE - Captive portal detection timeout - Grace Period not working as expected

| Field | Value |
|-------|-------|
| OS Platform | Windows & Mac |
| Feature | Captive portal |
| Regression | Day-1 |
| Bug Type | Test Gap |
| Automatable | No |
| Interop | No |
| QE Owner | N/A |
| Source Sheet | Customer Escalations - Overall |

**Test Case Needed**: No

**Comments**:
- Seems to be a day-1 issue (The original code would reset fail close captive portal status after the tunnel worker thread start,fix would reset fail close captive portal status after GSLB checking(which may have 20 sec delay), and before tunnel worker thread start.
- Need to consolidate all Captive portal Customer and Intercases under Fail-close
- Test Gap scope: Need-Additional Coverage

---

## 16. ENG-561500

**Jira**: [ENG-561500](https://netskope.atlassian.net/browse/ENG-561500)

**Description**: ENG-561500 CLONE - [Rolex - POC] DNS traffic is not steered after recovering from Fail Close

| Field | Value |
|-------|-------|
| OS Platform | Windows |
| Feature | Fail-close,DNS security |
| Regression | Day-1 |
| Bug Type | Test Gap |
| Automatable | Yes |
| Interop | No |
| QE Owner | N/A |
| Source Sheet | Customer Escalations - Overall |

**Test Case Needed**: No

**Comments**:
- This issue is a Day-1 and happens with the combination of Web Mode + DNS steering when fail-close is enabled..
- Fail close reference
- Test Gap Scope: Day-1 Issue
- Negative testing - When client tunnel disconencts for various reasons with Fail-close mode.

---

## 17. ENG-570306

**Jira**: [ENG-570306](https://netskope.atlassian.net/browse/ENG-570306)

**Description**: ENG-570306 CLONE - (SENTRY) Looking for possible update in tenant or client configuration

| Field | Value |
|-------|-------|
| OS Platform | Windows |
| Feature | Fail-close |
| Regression | No |
| Bug Type | Test Gap |
| Automatable | No |
| Interop | Yes |
| QE Owner | Karthic Mariappan |
| Source Sheet | Customer Escalations - Overall |

**Test Case Needed**: Yes

**Comments**:
- Need to add fail-close test case when multiple user logout and login flow and when GW is not reachable, test with tunnel disconnect and resume flow.
- Test Gap scope: interop test
- Interop: Citrix/AVD VDI

---

## 18. ENG-577918

**Jira**: [ENG-577918](https://netskope.atlassian.net/browse/ENG-577918)

**Description**: ENG-577918 CLONE - [NPA] [Chromebook] Client not restarting NPA service automatically

| Field | Value |
|-------|-------|
| OS Platform | Android |
| Feature | Steering&Exception |
| Regression | No |
| Bug Type | Test Gap (NPA Integration) |
| Automatable | No |
| Interop | No |
| QE Owner | Anand Kumar S |
| Source Sheet | Customer Escalations - Overall |

**Test Case Needed**: No

**Comments**:
- The issue occurs when the client simulates the user Disable/Enable action to reset the tun device. In this process, the client disables NPA but fails to re-enable it.
- In the last 6 months, there were several bug fixes done on Tunnel unstability issues, but still we are facing new issues. Thjis needs more testing on Android and Chrome OS
- Already added in testrail. Include for tracking
- Test Gap scope: Need-Additional Coverage
- Integration: NPA

---

## 19. ENG-587497

**Jira**: [ENG-587497](https://netskope.atlassian.net/browse/ENG-587497)

**Description**: ENG-587497 CLONE - [Dubai World Trade Centre] Client service Crashes frequently

| Field | Value |
|-------|-------|
| OS Platform | Windows |
| Feature | NSC |
| Regression | Yes |
| Bug Type | Corner case (needs to have scenarios which exposes the Crash issues) |
| Automatable | No |
| Interop | No |
| QE Owner | Abhishek Sharma |
| Source Sheet | Escalation Bug-Review Q226 (Feb) |
| Steering & Exception | No |
| Client Endpoint Bug | Yes |
| Backend Issue | No |

**Test Case Needed**: Yes

**Comments**:
- There were many instance of crash issues during tunnel disconenct case.
- Dev has refactored the code to avoid the crash occurances.
- Many bugs around crash was reported by QE( The issue was addressed one of the Internal QE ticket(ENG-538602)

---

## 20. ENG-591725

**Jira**: [ENG-591725](https://netskope.atlassian.net/browse/ENG-591725)

**Description**: ENG-591725 CLONE - [ Viasat ] Client's SWG tunnel does not get connected when client is moved from a Steering configuration with "None" steering to a Steering Configuration with "All Traffic

| Field | Value |
|-------|-------|
| OS Platform | Windows, Mac, Linux |
| Feature | Flexible Dynamic Steering |
| Regression | Yes |
| Bug Type | Internal found |
| Automatable | Yes |
| Interop | No |
| QE Owner | Deepthi K S |
| Source Sheet | Customer Escalations - Overall |
| Steering & Exception | Yes |

**Test Case Needed**: Yes

**Comments**:
- Issue happens when Steering Mode changes from None to Web/All traffic- Tunnel does not kick-in.
- This one happens after Auto-config update flow.
- Have to include this in Automation.
- This issue was Internally found and fixed before it was reported by customer

Deepthi --> DSE has this case covered and also automated. This runs every release

---

## 21. ENG-592681

**Jira**: [ENG-592681](https://netskope.atlassian.net/browse/ENG-592681)

**Description**: ENG-592681 CLONE - [UWV] [Android] Tunnel gets dropped often

| Field | Value |
|-------|-------|
| OS Platform | Android |
| Feature | Steering&Exception |
| Regression | Yes |
| Bug Type | Enhancement |
| Automatable | No |
| Interop | No |
| QE Owner | Anand Kumar S |
| Source Sheet | Customer Escalations - Overall |
| Steering & Exception | Yes |

**Test Case Needed**: No

**Comments**:
- Client team to include NPA + NSclient Integration testing.
- The original implementation of this mechanism has bug, which will cause the both tunnel in disconnected state if the recovery mechanism is not fully executed under certain cases. The recovery mechanism is re-implemented to ensure to cover all cases
- Have more coverage for Tunnel Disconnect/Connect scenarios.

**Action Items**:
Negative scenario with Tunnel Disconnect using Wifii/5G data switch. hence it cannot be automated.

---

## 22. ENG-593503

**Jira**: [ENG-593503](https://netskope.atlassian.net/browse/ENG-593503)

**Description**: ENG-593503 NSC crash investigation - DEM thread stack overrun

| Field | Value |
|-------|-------|
| OS Platform | Windows |
| Feature | DEM |
| Regression | Yes |
| Bug Type | Corner case (needs to have scenarios which exposes the Crash issues) |
| Automatable | No |
| Interop | No |
| QE Owner | Abhishek Sharma |
| Source Sheet | Escalation Bug-Review Q226 (Feb) |
| Steering & Exception | No |
| Client Endpoint Bug | Yes |
| Backend Issue | No |

**Test Case Needed**: Yes

**Comments**:
-  crash was observed on the DEM thread, and during tunnel disconnection, and was difficult to reproduce.

---

## 23. ENG-593814

**Jira**: [ENG-593814](https://netskope.atlassian.net/browse/ENG-593814)

**Description**: ENG-593814 CLONE - [Bayer] Client Proxy Settings After Reboot - Continuation of ENG-491848

| Field | Value |
|-------|-------|
| OS Platform | Windows |
| Feature | Explicit Proxy |
| Regression | No |
| Bug Type | Test Gap |
| Automatable | Yes |
| Interop | Yes |
| QE Owner | Anand Kumar S |
| Source Sheet | Escalation Bug-Review Q226 (Feb) |
| Steering & Exception | No |
| Client Endpoint Bug | Yes |
| Backend Issue | No |

**Test Case Needed**: Yes

**Comments**:
- This ticket addresses a critical proxy detection issue causing delays in tunnel startup after device reboot.
-The fix ensures proxy re-detection if the `addonhost` has not been populated.
- Need to add the test case to cover tbius scenario in EP test plan and see to automate.

---

## 24. ENG-595031

**Jira**: [ENG-595031](https://netskope.atlassian.net/browse/ENG-595031)

**Description**: ENG-595031 CLONE - [Nintendo] Incorrect Cert-pinned app definition applied causing Exception app to be tunnelled

| Field | Value |
|-------|-------|
| OS Platform | Windows |
| Feature | Secure Config, Flexible Dynamic Steering |
| Regression | Yes |
| Bug Type | Missing in Regression ( If. this is automated, It should've been caught by automation.) |
| Automatable | Yes |
| Interop | No |
| QE Owner | Deepthi K S |
| Source Sheet | Customer Escalations - Overall |
| Steering & Exception | Yes |

**Test Case Needed**: Yes

**Comments**:
- Issue caused by client calling wrong API endpoint (steering/pinnedapps instead of steering/dynamicpinnedapps) with Secure Config Validation and Dynamic Steering enabled.
- This should've been caught with Secure Config feature validation

Deepthi - Karthic Mariappan Please re-assign this one to the person who validated the Secure config to add tests around this in their NPLAN

---

## 25. ENG-611565

**Jira**: [ENG-611565](https://netskope.atlassian.net/browse/ENG-611565)

**Description**: ENG-611565 On VDI DaaS Environment we must not terminate existing connections when NSClient establishes the tunnel

| Field | Value |
|-------|-------|
| OS Platform | N/A |
| Feature | N/A |
| Regression | N/A |
| Bug Type | N/A |
| Automatable | N/A |
| Interop | N/A |
| QE Owner | N/A |
| Source Sheet | Internal Bugs |
| Client Endpoint Bug | Yes |
| Backend Issue | No |

**Test Case Needed**: N/A

**Comments**:
Dev work in progress

---

## 26. ENG-614375

**Jira**: [ENG-614375](https://netskope.atlassian.net/browse/ENG-614375)

**Description**: ENG-614375 CLONE - [HR Block] Client connecting to out of country pop

| Field | Value |
|-------|-------|
| OS Platform | Windows |
| Feature | GSLB |
| Regression | Yes |
| Bug Type | Missing in Regression(Negative Scenario) |
| Automatable | Yes |
| Interop | No |
| QE Owner | Deepthi K S |
| Source Sheet | Escalation Bug-Review Q226 (Feb) |
| Steering & Exception | No |
| Client Endpoint Bug | Yes |
| Backend Issue | No |

**Test Case Needed**: Yes

**Comments**:
- Negativce scenario.
- When a particular POP is not reachable, client connects to the random POP instead of swtich to the next closest POP.
- Add the test case to block the POP and verify the client connects to the next closest POP.

---

## 27. ENG-624953

**Jira**: [ENG-624953](https://netskope.atlassian.net/browse/ENG-624953)

**Description**: ENG-624953 CLONE - On VDI DaaS Environment we must not terminate existing connections when NSClient establishes the tunnel

| Field | Value |
|-------|-------|
| OS Platform | Windows |
| Feature | multi-user |
| Regression | Day-1 |
| Bug Type | Corner case |
| Automatable | No |
| Interop | Yes |
| QE Owner | Karthic Mariappan |
| Source Sheet | Customer Escalations - Overall |
| Steering & Exception | Yes |

**Test Case Needed**: Yes

**Comments**:
- Day-1 issue
- Client distruptes the existing connections which is in bypass list and and this broke the VDI communication for multi-users.
- Need to add test case.
- Test Gap Scope: Day-1 Issue
- Interop Scope: VDI-Citrix VDI/AVD

---

## 28. ENG-625957

**Jira**: [ENG-625957](https://netskope.atlassian.net/browse/ENG-625957)

**Description**: ENG-625957 [Akin Gump Strauss Hauer & Feld LLP] NPA not tunneling traffic

| Field | Value |
|-------|-------|
| OS Platform | Windows |
| Feature | BWAN |
| Regression | No |
| Bug Type | Corner case |
| Automatable | No |
| Interop | Yes |
| QE Owner | Poovarasan Chitravel |
| Source Sheet | Customer Escalations - Overall |
| Steering & Exception | Yes |

**Test Case Needed**: Yes

**Comments**:
- INtegration issue(NSC + NPA + BWAN)
- This happens with Interop and Integration.
- NSclient driver doesn'rt captured the Outbound/Egress pkts, if injected by third party driver in the presence of windivert driver.
- Fix is to divert all egress pkats to bwan in case BWAN is configured Internet bypass AppX rule.
- Interop: AV- windows defender, VPN - Chekcpoint

---

## 29. ENG-637794

**Jira**: [ENG-637794](https://netskope.atlassian.net/browse/ENG-637794)

**Description**: ENG-637794 CLONE - [Jio] NPA Traffic not tunneling - Chromebook

| Field | Value |
|-------|-------|
| OS Platform | ChromeOS |
| Feature | Steering&Exception |
| Regression | Yes |
| Bug Type | Missing in Regression(bypassIpExceptionAtAndroidOs) |
| Automatable | Yes |
| Interop | No |
| QE Owner | Anand Kumar S |
| Source Sheet | Customer Escalations - Overall |
| Steering & Exception | Yes |

**Test Case Needed**: No

**Comments**:
- Wiht the new FF(bypassIPExceptionAtAndroidOs) additin, will cause all exception IPs/IP Ranges/Subnets to be bypassed by OS directly instead of NS Client app. This affects NPA overlap app list.
- Fix is to check all NPA subnet lists  wiht the Exclude route and make sure to add the overlap bypass list.
- NSclient + NPA Android Integration.
- Add test case for NSclient 
- Regression

**Action Items**:
Automation Task - https://netskope.atlassian.net/browse/ENG-782342

---

## 30. ENG-649593

**Jira**: [ENG-649593](https://netskope.atlassian.net/browse/ENG-649593)

**Description**: ENG-649593 CLONE - Ack numbers mangled in response to syn/ack for Outlook->MS365 connections

| Field | Value |
|-------|-------|
| OS Platform | Windows |
| Feature | Proxy-Steering&Exception |
| Regression | Day-1 |
| Bug Type | Test Gap |
| Automatable | Yes |
| Interop | No |
| QE Owner | Anand Kumar S |
| Source Sheet | Customer Escalations - Overall |

**Test Case Needed**: No

**Comments**:
- Issue seems to be reproduced  and this issue seems to be exists from Day-1
- intermittent impact on one app and on-prem users only
- It happens with local proxy with cert pin applications with bypass by tunnelling (Steering&Exception)
- Test case can be automatable.
- Test Gap scope: Day-1 issue

---

## 31. ENG-652754

**Jira**: [ENG-652754](https://netskope.atlassian.net/browse/ENG-652754)

**Description**: ENG-652754 CLONE - [Banco de Sabadell] Android Clients stuck in connecting state

| Field | Value |
|-------|-------|
| OS Platform | Android |
| Feature | Steering&Exception |
| Regression | Yes |
| Bug Type | Corner case |
| Automatable | No |
| Interop | No |
| QE Owner | Anand Kumar S |
| Source Sheet | Customer Escalations - Overall |

**Test Case Needed**: Yes

**Comments**:
- Issue happens when network is unreliable.Few users had rported it.
- Unable to replicate the same case by both dev and QE.
- Need to add more test on Tunnel Disconnect/Connect case with Android.
- Test case needs to be added(Testrail link in JIRA is broken)
- Negative testing.

---

## 32. ENG-655009

**Jira**: [ENG-655009](https://netskope.atlassian.net/browse/ENG-655009)

**Description**: ENG-655009 CLONE - [NBC] CFW application tunnelling issue on Windows

| Field | Value |
|-------|-------|
| OS Platform | Windows |
| Feature | Cloud Firewall-Steering&Exception |
| Regression | Yes |
| Bug Type | Test Gap |
| Automatable | Yes |
| Interop | No |
| QE Owner | Deepthi K S |
| Source Sheet | Customer Escalations - Overall |

**Test Case Needed**: No

**Comments**:
- Issue is with F/W exception addition and deletion flow.
- Limitation: Exceptions involving port and IP/URL or only IP/URL still do not work consistently on Windows; timing issues observed.
- This can be automable.
- Test Gap scope: Need-Additional Coverage

Deepthi - DSE cases tests this and also has Automation covered.

---

## 33. ENG-659009

**Jira**: [ENG-659009](https://netskope.atlassian.net/browse/ENG-659009)

**Description**: ENG-659009 CLONE - GSLB is not working as expected

| Field | Value |
|-------|-------|
| OS Platform | Windows |
| Feature | GSLB |
| Regression | Day-1 |
| Bug Type | Test Gap |
| Automatable | Yes |
| Interop | No |
| QE Owner | Deepthi K S |
| Source Sheet | Customer Escalations - Overall |

**Test Case Needed**: Yes

**Comments**:
- When tunnel disconencts, tunnel manager should kick in or force download the GSLB Pop list..
- Need to cover the Client Tunnel disconnect case(Device Reboot)
- Test Gap scope: Day-1 issue

Deepthi - Added new cases in GSLB to support reboot of device / service

---

## 34. ENG-679420

**Jira**: [ENG-679420](https://netskope.atlassian.net/browse/ENG-679420)

**Description**: ENG-679420 CLONE - [Tier 1/EXL] Seeing the Netskope Icon in Network Path Latency - Underlay Dashboard

| Field | Value |
|-------|-------|
| OS Platform | Windows, Mac |
| Feature | DEM |
| Regression | No |
| Bug Type | Corner case |
| Automatable | Yes |
| Interop | No |
| QE Owner | Kim Shaw |
| Source Sheet | Customer Escalations - Overall |

**Test Case Needed**: No

**Comments**:
-customer's tenant has feature flag duplicateRccDataToGEF enabled. This flag will cause Polaris route control data to be sent to PDEM also. However, PDEM webUI will check if the target IP(s) is the same to the tunnel dest IP. If not matching, it will show Netskope Icon on the PDEM webUI.
- this feature flag is no longer needed.  To fix this issue, we removed all the code related to this feature flag to prevent Polaris route control data being sent to PDEM."
- Since duplicateRccDataToGEF is depricated, QE don't test this feature and customer has somehow enabled it and hit with this problem.
- Corner case.

---

## 35. ENG-707515

**Jira**: [ENG-707515](https://netskope.atlassian.net/browse/ENG-707515)

**Description**: ENG-707515 CLONE - [Satair A S] Google workspace access is forced via Reverseproxy even when NS client is active.

| Field | Value |
|-------|-------|
| OS Platform | Android |
| Feature | Steering&Exception |
| Regression | Yes |
| Bug Type | Corner case |
| Automatable | Yes |
| Interop | No |
| QE Owner | Anand Kumar S |
| Source Sheet | Customer Escalations - Overall |

**Test Case Needed**: No

**Comments**:
- This bug was regressed due to https://netskope.atlassian.net/browse/ENG-600647
- Some google services such as Google Workspace apps (ex., Gmail) uses com.google.android.gms process / package name 
- From R128 we have added com.google.android.gms package name to the default bypass list as it was causing the OS update to fail when the tunnel is established
- One of the customer [Satair] wants to have com.google.android.gms package tarffic to be tunneled. We have to revert the fix on R130
- Test case has been added in the testrail to cover this flow in the future regressions
- For the OS update to work we need to ask the customer to have a cert pinned exception for com.google.android.gms, this needed to be documented

**Action Items**:
Automation task - https://netskope.atlassian.net/browse/ENG-781866

---

## 36. ENG-710784

**Jira**: [ENG-710784](https://netskope.atlassian.net/browse/ENG-710784)

**Description**: ENG-710784 CLONE - R127.2 - Citrix VDI DaaS and Netskope Client Terminating the Existing Connections

| Field | Value |
|-------|-------|
| OS Platform | Windows |
| Feature | Steering&Exception |
| Regression | Day-1 |
| Bug Type | Enhancement |
| Automatable | No |
| Interop | Yes |
| QE Owner | Karthic Mariappan |
| Source Sheet | Customer Escalations - Overall |

**Test Case Needed**: No

**Comments**:
- The previous feature flag avoidDisruptingBypass which was introduced only to bypass existing connections from certpinned applications with "*"domain rule is not working in Citrix Daas environment because svchost.exe also is generating some traffic to bring up Citrix connections.
- Fix is to Bypass all the existing connections once the tunnel is established if the feature flag bypassAllExistingConnections is set
- Not able to hit this issue internally.

---

## 37. ENG-742949

**Jira**: [ENG-742949](https://netskope.atlassian.net/browse/ENG-742949)

**Description**: ENG-742949 CLONE - Cert pinned bypass not working

| Field | Value |
|-------|-------|
| OS Platform | Windows |
| Feature | Steering&Exception |
| Regression | Yes |
| Bug Type | Missing in Regression |
| Automatable | Yes |
| Interop | Yes |
| Reported Version | 127.0.0 |
| QE Owner | Anand Kumar S |
| Source Sheet | Customer Escalations - Overall |

**Test Case Needed**: No

**Comments**:
- This issue was caused due to the fix ENG-649593.
- We have this test case in the existing automation(Cert Pinned apps). Need to improve the validation steps the current automation.
- Due to the above fix, Defined the cert pinned app to bypass by tunnel flow to avoid proxy inspection, but traffic is still decrypted intermittently.

**Action Items**:
Automation task: https://netskope.atlassian.net/browse/ENG-782343

---

## 38. ENG-746099

**Jira**: [ENG-746099](https://netskope.atlassian.net/browse/ENG-746099)

**Description**: ENG-746099 CLONE - [Makemytrip]NS Client disconnects frequently for multiple users causing severe disruption

| Field | Value |
|-------|-------|
| OS Platform | Windows & Mac |
| Feature | AOAC |
| Regression | Day-1 |
| Bug Type | Enhancement |
| Automatable | Yes |
| Interop | No |
| Reported Version | 129.0.0 |
| QE Owner | Anand Kumar S |
| Source Sheet | Customer Escalations - Overall |

**Test Case Needed**: No

**Comments**:
- Day-1 issue. We have implemented a feature flag -enableMacOsAOACSupport to keep the tunnel running during  the onSystemWakeup callback.

---

## 39. ENG-751720

**Jira**: [ENG-751720](https://netskope.atlassian.net/browse/ENG-751720)

**Description**: ENG-751720 CLONE - [Religare Broking Limited] Multiple System in Fail Closed error

| Field | Value |
|-------|-------|
| OS Platform | Windows |
| Feature | Fail-Close |
| Regression | Day-1 |
| Bug Type | Corner Case |
| Automatable | No |
| Interop | No |
| Reported Version | 129.0.0 |
| QE Owner | Ganesa Pandian S |
| Source Sheet | Customer Escalations - Overall |

**Test Case Needed**: No

**Comments**:
After customer upgrade from Windows 10 to Windows 11, there are machines have corrupt system files, please check the comment history and attached system event logs.   

One machine has corrupt system files which related to "DNS client event 8020", trigger this bug.

Day-1 code. The tunnel manager thread would become stuck when flushing DNS using ipconfig.exe /flushdns. This occurred because the legacy code was using the CreateProcess function with an INFINITE timeout, causing the thread to hang if the system has "DNS client event 8020" and flush dns did not return.
- This scenario is not a stright forward case

---

## 40. ENG-752117

**Jira**: [ENG-752117](https://netskope.atlassian.net/browse/ENG-752117)

**Description**: ENG-752117 CLONE - [IDFC First Bank] Citrix VDI machines NSC enabled but not tunneling traffic

| Field | Value |
|-------|-------|
| OS Platform | Windows |
| Feature | Fail-Close |
| Regression | No |
| Bug Type | Corner Case |
| Automatable | No |
| Interop | Yes |
| Reported Version | 126.0.0 |
| QE Owner | Karthic Mariappan |
| Source Sheet | Customer Escalations - Overall |

**Test Case Needed**: No

**Comments**:
- Customer has deployed the Citrix VDI master image with fail-close enabled and later on the tenant Fail-close was disabled in the client config. With this mismatch, whenever the cloned VM sync with the Master image template did enable the fail-close in the driver and later updading config sync have forced gthe clientto the race condition and fails the on-prem detection.
- This scenario is not a stright forward case and usually not a recommedned on on the customer deployment.

**Action Items**:
Corner case Not automatable. Not recommended configuration

---

## 41. ENG-756104

**Jira**: [ENG-756104](https://netskope.atlassian.net/browse/ENG-756104)

**Description**: ENG-756104 CLONE - SkopeIT Application logs shows source IP as the Gateway's assigned DHCP ip instead of Machine's public IP

| Field | Value |
|-------|-------|
| OS Platform | Mac |
| Feature | Data path |
| Regression | Day-1 |
| Bug Type | Corner Case |
| Automatable | Yes |
| Interop | No |
| Reported Version | 126.0.0 |
| QE Owner | Abhishek Sharma |
| Source Sheet | Customer Escalations - Overall |

**Test Case Needed**: N/A

**Comments**:
client code was updating the machine IP in the info log print statement. This issue will appear only when customer selects the log level to warn, error, critical, because client will not print the info log so client machine IP will also not get updated.
Now as part of this fix, printing og and updating the machine IP splitted into two statements.

---

## 42. ENG-762672

**Jira**: [ENG-762672](https://netskope.atlassian.net/browse/ENG-762672)

**Description**: ENG-762672 CLONE - [BHEL] Android Client gets enabled auto enabled during NW change though it's disabled by User

| Field | Value |
|-------|-------|
| OS Platform | Android |
| Feature | Data path |
| Regression | Yes |
| Bug Type | Corner Case |
| Automatable | Yes |
| Interop | No |
| Reported Version | 129.0.0 |
| QE Owner | Anand Kumar S |
| Source Sheet | Customer Escalations - Overall |

**Test Case Needed**: No

**Comments**:
Some custom OS devices still allow the user to disconnect the tunnel from the notification bar, when the user disconnects via the tunnel notiifcaion the Client enables automatiocally. We may need additional custom OS devices to cover this scenario.

---

## 43. ENG-765691

**Jira**: [ENG-765691](https://netskope.atlassian.net/browse/ENG-765691)

**Description**: ENG-765691 CLONE - [Morgan Stanley] Alternate Steering Check not performed occasionally

| Field | Value |
|-------|-------|
| OS Platform | Windows |
| Feature | Data path |
| Regression | Day-1 |
| Bug Type | Enhancement |
| Automatable | No |
| Interop | No |
| Reported Version | 126.0.0 |
| QE Owner | Anand Kumar S |
| Source Sheet | Customer Escalations - Overall |

**Test Case Needed**: No

**Comments**:
-Proxy detection depends on Impersonating as Active user.
-In multi user scenario (VDI), It is possible that users might be in disconnected state rather than active state.
-Disconnected state means Users are still logged in but not actively connected.
-Proxy detection should consider disconnected users as well as the Tunnels for those users are still active.

---

## 44. ENG-766017

**Jira**: [ENG-766017](https://netskope.atlassian.net/browse/ENG-766017)

**Description**: ENG-766017 CLONE - [ Deltics ] NPA inner pcaps is coming corrupted

| Field | Value |
|-------|-------|
| OS Platform | Windows and Mac |
| Feature | NPA Integration |
| Regression | Yes |
| Bug Type | Test Gap |
| Automatable | Yes |
| Interop | No |
| Reported Version | 130.1.0 |
| QE Owner | Poovarasan Chitravel |
| Source Sheet | Customer Escalations - Overall |

**Test Case Needed**: Yes

**Comments**:
NPA Specific issue. There is a defect in the NSClient PCAP rotation function. When rotation occurred, the client mistakenly wrote the PCAP header to the SWG PCAP file instead of the NPA PCAP file. As a result, all NPA internal PCAP files except the first one were in an invalid format.

---

## 45. ENG-773191

**Jira**: [ENG-773191](https://netskope.atlassian.net/browse/ENG-773191)

**Description**: ENG-773191 CLONE - NPA traffic isn't getting tunneled with R131.

| Field | Value |
|-------|-------|
| OS Platform | Mac |
| Feature | NPA Integration |
| Regression | Yes |
| Bug Type | Corner Case |
| Automatable | Yes |
| Interop | No |
| Reported Version | 131.0.0 |
| QE Owner | Poovarasan Chitravel |
| Source Sheet | Customer Escalations - Overall |

**Test Case Needed**: Yes

**Comments**:
specific to macOS 15.x. The issue was reproduced after several time device reboot. The issue was linked to a regression(Partner Access) during the upgrade from R130 to R131, which caused the transparent proxy to stop when NPA was in a DISABLED state, preventing traffic processing. The issue is hard to reproduce.

---

## 46. ENG-846458

**Jira**: [ENG-846458](https://netskope.atlassian.net/browse/ENG-846458)

**Description**: ENG-846458 CLONE - [UWV] Android Client UI Gateway Field Not Aligning with Other OSes

| Field | Value |
|-------|-------|
| OS Platform | Android |
| Feature | NSC-FT-ClientConfiguration |
| Regression | Day-1 |
| Bug Type | Enhancement |
| Automatable | Yes |
| Interop | No |
| Reported Version | 133.0.0 |
| QE Owner | Anand Kumar S |
| Source Sheet | Customer Escalations - Overall |

**Test Case Needed**: No

**Comments**:
Customer has noted that the Configuration page on the Android Client's UI displays the SWG gateway hostname as “gateway-<tenantname>.goskope.com”, revealing their actual tenant URL. In contrast, all other platforms show the gateway as “gateway-<POP>.goskope.com”.
The customer expects this to be standardised across all Clients and operating systems.

---

## 47. ENG-855335

**Jira**: [ENG-855335](https://netskope.atlassian.net/browse/ENG-855335)

**Description**: ENG-855335 CLONE - [Axians] All SWG traffic bypassed on MAC due to wildcard exception

| Field | Value |
|-------|-------|
| OS Platform | Mac |
| Feature | Steering&Exception |
| Regression | Yes |
| Bug Type | Corner Case |
| Automatable | Yes |
| Interop | N/A |
| Reported Version | 132.0.0 |
| QE Owner | Abhishek Sharma |
| Source Sheet | Customer Escalations - Overall |

**Test Case Needed**: N/A

**Comments**:
Netskope client was throwing an error while adding include and exclude rules (::/128 or ::/0 or 0.0.0.0/0) in the client code, causing all traffic to be bypassed.
This is a corner case and generally customers doesn't configure these exception because it will bypass all the IPV4 or IPV6.

However, Customers can also add 0.0.0.0/0 from Network Locations as a destination exception and Netskope client will not treat 0.0.0.0/0 (all IPv4 traffic) as an exception and will continue tunneling all IPv4 traffic.

---

## 48. ENG-885394

**Jira**: [ENG-885394](https://netskope.atlassian.net/browse/ENG-885394)

**Description**: ENG-885394 CLONE - [Optiv] NPA re-auth window refreshes unexpectedly

| Field | Value |
|-------|-------|
| OS Platform | Mac |
| Feature | NPA Integration |
| Regression | Day-1 |
| Bug Type | Corner Case |
| Automatable | No |
| Interop | N/A |
| Reported Version | 132.0.0 |
| QE Owner | Poovarasan Chitravel |
| Source Sheet | Customer Escalations - Overall |

**Test Case Needed**: N/A

**Comments**:
During macOS Dark Wake (short wakeups while lid closed / machine “sleeping”):That XPC call may fail or stall.
The issue was caused by repeated firing of the NPA_REAUTH_SESSION_REFRESH event, which triggered frequent re-auth window refreshes and cancellations before user input.

---

## 49. ENG-906435

**Jira**: [ENG-906435](https://netskope.atlassian.net/browse/ENG-906435)

**Description**: CLONE - [Reel SAS] Android Client steers own client initiated traffic

| Field | Value |
|-------|-------|
| OS Platform | Android |
| Feature | Steering&Exception |
| Regression | Day-1 |
| Bug Type | Internal found |
| Automatable | Yes |
| Interop | No |
| Reported Version | 133.0.0 |
| QE Owner | Anand Kumar S |
| Source Sheet | Customer Escalations - Overall |

**Test Case Needed**: No

**Comments**:
This is a Day 1 issue. Traffic to the management plane is tunneled.
Although we have an internal ticket filed, it was closed stating it is a design.
With this fix, we will bypass all the traffic originating from NS Client; achecker and aproxy are two exceptions.

---

## 50. ENG-917549

**Jira**: [ENG-917549](https://netskope.atlassian.net/browse/ENG-917549)

**Description**: CLONE - [Sabistech] Android Client stuck in Connecting state

| Field | Value |
|-------|-------|
| OS Platform | Android |
| Feature | Steering&Exception |
| Regression | Day-1 |
| Bug Type | Corner case |
| Automatable | Yes |
| Interop | No |
| Reported Version | 133.0.0 |
| QE Owner | Anand Kumar S |
| Source Sheet | Customer Escalations - Overall |

**Test Case Needed**: Yes

**Comments**:
When Wifi connection was being switched to Mobile Data,  NS Client received the no network event. This event triggered tunnel disconnect and tunnel manager stop.  After tunnel manager is stopped, the latest tunnel state is not updated to UI (NS Agent UI) and UI still keeps the previous received tunnel CONNECTING state.

---

## 51. ENG-918131

**Jira**: [ENG-918131](https://netskope.atlassian.net/browse/ENG-918131)

**Description**: CLONE - [Citizen Bank] Multi-Session VDI - SWG traffic tunnelling broken intermittently

| Field | Value |
|-------|-------|
| OS Platform | Windows |
| Feature | Steering&Exception |
| Regression | Day-1 |
| Bug Type | Corner Case |
| Automatable | No |
| Interop | Yes |
| Reported Version | 129.0.0 |
| QE Owner | Austin Cheng |
| Source Sheet | Customer Escalations - Overall |

**Test Case Needed**: N/A

**Comments**:
This issue happen when multiple users logon at same time and tunnel building is late for about 20 seconds. Not easy to replicate the issue. It is good if we can have automation on VDI evironment. Setup mltiple user logon togather with the nsclient building the tunnel as a stability test.

---

## 52. ENG-918295

**Jira**: [ENG-918295](https://netskope.atlassian.net/browse/ENG-918295)

**Description**: CLONE - [ Moffitt ] NPA not able to intercept DNS query for a private app when endpoint SDWAN is also enabled ..

| Field | Value |
|-------|-------|
| OS Platform | Mac |
| Feature | NPA Integration |
| Regression | Day-1 |
| Bug Type | Corner Case |
| Automatable | N/A |
| Interop | No |
| Reported Version | 132.0.0 |
| QE Owner | Poovarasan Chitravel |
| Source Sheet | Customer Escalations - Overall |

**Test Case Needed**: N/A

**Comments**:
The issue in presence of BWAN the dns queries were directly going to BWAN service instead of coming to NPA. Initially only the global dns servers were read by the NSC, now service dns server will also be monitored. When bwan is not configured in full tunnel mode then it add the dns server at service level only and hence NSC misses that dns server pushed by BWAN

---

## 53. ENG-918451

**Jira**: [ENG-918451](https://netskope.atlassian.net/browse/ENG-918451)

**Description**: CLONE - Internet Steering not honoring on-prem detection(using egressIP)

| Field | Value |
|-------|-------|
| OS Platform | Windows |
| Feature | On-prem Detection |
| Regression | Yes |
| Bug Type | Missing in Regression |
| Automatable | Yes |
| Interop | No |
| Reported Version | 132.0.0 |
| QE Owner | Anand Kumar S |
| Source Sheet | Customer Escalations - Overall |

**Test Case Needed**: N/A

**Comments**:
The client did not attempt to reconnect to the tunnel after switching from Off-Prem to On-Prem. This issue was introduced on Windows because of the following fix implemented for Android. 
https://netskope.atlassian.net/browse/ENG-707767

---

## 54. GSLB

**Description**: GSLB

| Field | Value |
|-------|-------|
| OS Platform | 5.0 |
| Feature | Deepthi K S |
| Regression | N/A |
| Bug Type | N/A |
| Automatable | N/A |
| Interop | N/A |
| QE Owner | N/A |
| Source Sheet | Customer Escalations - Overall |
| Steering & Exception | Internal Found |

**Test Case Needed**: N/A

---

## 55. Interoperability Product Issues -Summary

Total Issues Identified: 18 across 7 product categories (Last 1.5 yrs)

1. VDI Solutions (8 issues) 
    - Citrix VDI: 6 issues
        - Secure enrollment failures (2)
        - Self-protection/upgrade conflicts (1)
        - DNS Security integration (1)
        - Fail-close mechanism failures (2)
    - Amazon WorkSpaces VDI: 1 issue 
        - Cloud Firewall (CFW) compatibility

2. Proxy Integration (4 issues)
     - GSLB, Proxy Diable and Loopback proxy

3. Antivirus Conflicts (4 issues)
    - CrowdStrike: Device Classification(DC) and AOAC conflicts
    - Windows Defender: Steering mechanism issues
    - CyberArk - DNS Security

4. VPN ( 2 issues)
    - Citrix and Cisco VPN (Packet handling)

5. MDM Platform Issues (2 issues)
    - Android(IDP) and Mac(Jamf Script)

6. IDP (1 Issue)
     - Microsoft Azure Entra IDP

Next steps:
 - Include Citrix VDI regression for monthly release.
 - Use the GRS suite to cover the Interop products
 - Combine Various products as One solution deployed on endpoints(VPN, AV, IDP,Proxy) and cover GRS sanity.
 - Map the GRS suite scenarios with Top/large customers and identify the Interop products they use in their deployment.

**Description**: Interoperability Product Issues -Summary

Total Issues Identified: 18 across 7 product categories (Last 1.5 yrs)

1. VDI Solutions (8 issues) 
    - Citrix VDI: 6 issues
        - Secure enrollment failures (2)
        - Self-protection/upgrade conflicts (1)
        - DNS Security integration (1)
        - Fail-close mechanism failures (2)
    - Amazon WorkSpaces VDI: 1 issue 
        - Cloud Firewall (CFW) compatibility

2. Proxy Integration (4 issues)
     - GSLB, Proxy Diable and Loopback proxy

3. Antivirus Conflicts (4 issues)
    - CrowdStrike: Device Classification(DC) and AOAC conflicts
    - Windows Defender: Steering mechanism issues
    - CyberArk - DNS Security

4. VPN ( 2 issues)
    - Citrix and Cisco VPN (Packet handling)

5. MDM Platform Issues (2 issues)
    - Android(IDP) and Mac(Jamf Script)

6. IDP (1 Issue)
     - Microsoft Azure Entra IDP

Next steps:
 - Include Citrix VDI regression for monthly release.
 - Use the GRS suite to cover the Interop products
 - Combine Various products as One solution deployed on endpoints(VPN, AV, IDP,Proxy) and cover GRS sanity.
 - Map the GRS suite scenarios with Top/large customers and identify the Interop products they use in their deployment.

| Field | Value |
|-------|-------|
| OS Platform | N/A |
| Feature | N/A |
| Regression | N/A |
| Bug Type | N/A |
| Automatable | N/A |
| Interop | N/A |
| QE Owner | N/A |
| Source Sheet | Customer Escalations - Overall |

**Test Case Needed**: N/A

---

## 56. NSGateway-Datapath(Android)

**Description**: NSGateway-Datapath(Android)

| Field | Value |
|-------|-------|
| OS Platform | 2.0 |
| Feature | Anand Kumar S |
| Regression | N/A |
| Bug Type | N/A |
| Automatable | N/A |
| Interop | N/A |
| QE Owner | N/A |
| Source Sheet | Customer Escalations - Overall |

**Test Case Needed**: N/A

---

## 57. Review  summary notes  for Feb to May 2024 - Tickets
- ~50% of the customer bugs needs to be added in Test rail.  From the history, QE had used the Bug link in the JIRA -QE test plan field to close the bugs and those issues need to created/converted as test case in test rail.

- Customer issues added in test rail was not covered or automated for the release regression testing. 

- Need to group the customer issues in seperate folder. Currently the customer issue reported test cases were added in different folders.

- Based on the report, Need to focus regression on Steering & Bypass, Devices status(Client and Backend), DEM, DNS security, Fail-close, GSLB, Secure enrollment, AOAC. (Needs to conisdered for Golden regression suite)

- Steering and Exception( Lot of changes and enhancements were made in last one year and still new changes are inprogress (e.g., Flexible Dynamic Steering, Location Detection, Steering enhancement(NPLAN-125),Egress IP, Express connect  etc.,). Entire QE needs to familer and get hands on with the new changes, this might help avoid customer issues and more possibility on finding bugs internally. Same for the Device status feature as well.

- Steering & Exception - Need to keep an eye on feature parity with all platforms.
      - Steering & exception with various steering modes(Cloud, Web, All traffic, None)
      - Steering & Exception with Flexible Dynamic steering
      - Steering & Exception wtih Onprem/Offprem
      - Steering & Exception with DNS security
      - Steering and Exception with UDP traffic
      - Steering and Exception with Fail-close
      - Steering & Exception with Proxy(Local/Fiddler etc.,)
      - Steering & Exception with Cloud Firewall
      - Steering & Exception with Custom Port
      - 

- Compared to DP, more  customer issues found on the client to MP(client services) components

- Android regression needs to be improved for 2 areas - 1) steering and Bypass feature , 2) Keep more cases for Network switch/Tunnel disconnect/Connect( e.g., stress test, Longivity)"

**Description**: Review  summary notes  for Feb to May 2024 - Tickets
- ~50% of the customer bugs needs to be added in Test rail.  From the history, QE had used the Bug link in the JIRA -QE test plan field to close the bugs and those issues need to created/converted as test case in test rail.

- Customer issues added in test rail was not covered or automated for the release regression testing. 

- Need to group the customer issues in seperate folder. Currently the customer issue reported test cases were added in different folders.

- Based on the report, Need to focus regression on Steering & Bypass, Devices status(Client and Backend), DEM, DNS security, Fail-close, GSLB, Secure enrollment, AOAC. (Needs to conisdered for Golden regression suite)

- Steering and Exception( Lot of changes and enhancements were made in last one year and still new changes are inprogress (e.g., Flexible Dynamic Steering, Location Detection, Steering enhancement(NPLAN-125),Egress IP, Express connect  etc.,). Entire QE needs to familer and get hands on with the new changes, this might help avoid customer issues and more possibility on finding bugs internally. Same for the Device status feature as well.

- Steering & Exception - Need to keep an eye on feature parity with all platforms.
      - Steering & exception with various steering modes(Cloud, Web, All traffic, None)
      - Steering & Exception with Flexible Dynamic steering
      - Steering & Exception wtih Onprem/Offprem
      - Steering & Exception with DNS security
      - Steering and Exception with UDP traffic
      - Steering and Exception with Fail-close
      - Steering & Exception with Proxy(Local/Fiddler etc.,)
      - Steering & Exception with Cloud Firewall
      - Steering & Exception with Custom Port
      - 

- Compared to DP, more  customer issues found on the client to MP(client services) components

- Android regression needs to be improved for 2 areas - 1) steering and Bypass feature , 2) Keep more cases for Network switch/Tunnel disconnect/Connect( e.g., stress test, Longivity)"

| Field | Value |
|-------|-------|
| OS Platform | N/A |
| Feature | N/A |
| Regression | N/A |
| Bug Type | N/A |
| Automatable | N/A |
| Interop | N/A |
| QE Owner | N/A |
| Source Sheet | Customer Escalations - Overall |

**Test Case Needed**: N/A

---

## 58. Review  summary notes for reference:
- ~50% of the customer bugs needs to be added in Test rail.  From the history, QE had used the Bug link in the JIRA -QE test plan field to close the bugs and those issues need to created/converted as test case in test rail.

- Customer issues added in test rail was not covered or automated for the release regression testing. 

- Need to group the customer issues in seperate folder. Currently the customer issue reported test cases were added in different folders.

- Based on the report, Need to focus regression on Steering & Bypass, Devices status(Client and Backend), DEM, DNS security, Fail-close, GSLB, Secure enrollment, AOAC. (Needs to conisdered for Golden regression suite)

- Steering and Exception( Lot of changes and enhancements were made in last one year and still new changes are inprogress (e.g., Flexible Dynamic Steering, Location Detection, Steering enhancement(NPLAN-125),Egress IP, Express connect  etc.,). Entire QE needs to familer and get hands on with the new changes, this might help avoid customer issues and more possibility on finding bugs internally. Same for the Device status feature as well.

- Steering & Exception - Need to keep an eye on feature parity with all platforms.
      - Steering & exception with various steering modes(Cloud, Web, All traffic, None)
      - Steering & Exception with Flexible Dynamic steering
      - Steering & Exception wtih Onprem/Offprem
      - Steering & Exception with DNS security
      - Steering and Exception with UDP traffic
      - Steering and Exception with Fail-close
      - Steering & Exception with Proxy(Local/Fiddler etc.,)
      - Steering & Exception with Cloud Firewall
      - Steering & Exception with Custom Port
      - 

- Compared to DP, more  customer issues found on the client to MP(client services) components

- Android regression needs to be improved for 2 areas - 1) steering and Bypass feature , 2) Keep more cases for Network switch/Tunnel disconnect/Connect( e.g., stress test, Longivity)

**Description**: Review  summary notes for reference:
- ~50% of the customer bugs needs to be added in Test rail.  From the history, QE had used the Bug link in the JIRA -QE test plan field to close the bugs and those issues need to created/converted as test case in test rail.

- Customer issues added in test rail was not covered or automated for the release regression testing. 

- Need to group the customer issues in seperate folder. Currently the customer issue reported test cases were added in different folders.

- Based on the report, Need to focus regression on Steering & Bypass, Devices status(Client and Backend), DEM, DNS security, Fail-close, GSLB, Secure enrollment, AOAC. (Needs to conisdered for Golden regression suite)

- Steering and Exception( Lot of changes and enhancements were made in last one year and still new changes are inprogress (e.g., Flexible Dynamic Steering, Location Detection, Steering enhancement(NPLAN-125),Egress IP, Express connect  etc.,). Entire QE needs to familer and get hands on with the new changes, this might help avoid customer issues and more possibility on finding bugs internally. Same for the Device status feature as well.

- Steering & Exception - Need to keep an eye on feature parity with all platforms.
      - Steering & exception with various steering modes(Cloud, Web, All traffic, None)
      - Steering & Exception with Flexible Dynamic steering
      - Steering & Exception wtih Onprem/Offprem
      - Steering & Exception with DNS security
      - Steering and Exception with UDP traffic
      - Steering and Exception with Fail-close
      - Steering & Exception with Proxy(Local/Fiddler etc.,)
      - Steering & Exception with Cloud Firewall
      - Steering & Exception with Custom Port
      - 

- Compared to DP, more  customer issues found on the client to MP(client services) components

- Android regression needs to be improved for 2 areas - 1) steering and Bypass feature , 2) Keep more cases for Network switch/Tunnel disconnect/Connect( e.g., stress test, Longivity)

| Field | Value |
|-------|-------|
| OS Platform | N/A |
| Feature | N/A |
| Regression | N/A |
| Bug Type | N/A |
| Automatable | N/A |
| Interop | N/A |
| QE Owner | N/A |
| Source Sheet | Customer Escalations - Overall |

**Test Case Needed**: N/A

---

## 59. Review Notes:
- Steering and Exception:
     - Android and ChromeOS has 4 Issues under this catagotry and mostly with tunnel stability
 - Backend : Clearning cache, Secure Config, Device classification
- Flexible Dynamic steering: Steering mode change, Bypass logic & Secure config API.
- Cloud Firewall: Network switch, Bypass logic, IPV4/IPv6 traffic exception handling w/wo handling exceptionbydriver
- Install/Upgrade: Client rollback and UI issue.
- GSLB - Tunnel disconnect, Device offline/online - check GSLB flow
- Device Classification: Backend update failure,Bit locker check
- DNS security - Enhancement - PTR related case

**Description**: Review Notes:
- Steering and Exception:
     - Android and ChromeOS has 4 Issues under this catagotry and mostly with tunnel stability
 - Backend : Clearning cache, Secure Config, Device classification
- Flexible Dynamic steering: Steering mode change, Bypass logic & Secure config API.
- Cloud Firewall: Network switch, Bypass logic, IPV4/IPv6 traffic exception handling w/wo handling exceptionbydriver
- Install/Upgrade: Client rollback and UI issue.
- GSLB - Tunnel disconnect, Device offline/online - check GSLB flow
- Device Classification: Backend update failure,Bit locker check
- DNS security - Enhancement - PTR related case

| Field | Value |
|-------|-------|
| OS Platform | N/A |
| Feature | N/A |
| Regression | N/A |
| Bug Type | N/A |
| Automatable | N/A |
| Interop | N/A |
| QE Owner | N/A |
| Source Sheet | Escalation Bug-Review Q226 (Feb) |

**Test Case Needed**: N/A

---



## --- Added from Excel (not previously in bugs/) ---

## 60. ENG-437202

**Jira**: [ENG-437202](https://netskope.atlassian.net/browse/ENG-437202)

**Description**: Android clients getting disconnected intermittently

| Field | Value |
|-------|-------|
| OS Platform | Android |
| Feature | Data path |
| Regression | No |
| Bug Type | Test Gap(Improve Platform Coverage) |
| Automatable | Yes |
| Interop | No |
| Source Sheet | Customer Escalations - Overall |

**Comments**: - Specific to Lenovo platform.
- Test Gap scope: platform coverage

---
## 61. ENG-627806

**Jira**: [ENG-627806](https://netskope.atlassian.net/browse/ENG-627806)

**Description**: Intermittent segmentation fault in Linux NS Client R117 and R122: crash

| Field | Value |
|-------|-------|
| OS Platform | Linux |
| Feature |  |
| Source Sheet | Q226 Feb |

---
## 62. ENG-635063

**Jira**: [ENG-635063](https://netskope.atlassian.net/browse/ENG-635063)

**Description**: [ Lucid Motors ] Linux client is crashing often

| Field | Value |
|-------|-------|
| OS Platform | Windows |
| Feature | NSC-FT-Service |
| Source Sheet | Q226 Feb |

---
## 63. ENG-679477

**Jira**: [ENG-679477](https://netskope.atlassian.net/browse/ENG-679477)

**Description**: Intermittent segmentation fault in Linux NS Client R117 and R122: crash

| Field | Value |
|-------|-------|
| OS Platform | Linux |
| Feature | NSC FT Service |
| Regression | No |
| Bug Type | Corner case |
| Automatable | Yes |
| Interop | No |
| Source Sheet | Customer Escalations - Overall |

**Comments**: - The tie socket instance was freed before the callback function of the object finishes.
- The fix is Hold tie socket instance till the end of the callback to avoid use-after-free situation.
- It appears the issue exists in older build as well, but it is not clear this is a Day-1 issue or not. 
- Corner case.

---
## 64. ENG-774714

**Jira**: [ENG-774714](https://netskope.atlassian.net/browse/ENG-774714)

**Description**: No connectivity on 802.1x Network with NSC enabled in Linux

| Field | Value |
|-------|-------|
| OS Platform | Linux |
| Feature | Data path |
| Regression | Day-1 |
| Bug Type | SetupIssue |
| Automatable | No |
| Interop | No |
| Source Sheet | Customer Escalations - Overall |

**Comments**: New feature flag added for 802.1x network, however automation can be run only once setup is available tracked by ENG-795961

---
