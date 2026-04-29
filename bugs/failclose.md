# FailClose / FailOpen Bugs

Bugs related to FailClose activation, FailOpen behavior, captive portal detection, on-prem detection, and traffic blocking when tunnel is disconnected.

> Source: Escalation Bug Review spreadsheet, filtered by keywords: failclose, fail close, fail open, captive portal, on-prem, backed off, block traffic.

**Total: 28 bugs**

---

## 1. ENG-384041

**Jira**: [ENG-384041](https://netskope.atlassian.net/browse/ENG-384041)

**Description**: ENG-384041 CLONE - [NSclient] Client is going into Fail Close mode instead of Backed off when on-prem with steering is set to None.

| Field | Value |
|-------|-------|
| OS Platform | Windows |
| Feature | Fail-close &  Flexible Dynamic Steering |
| Regression | Yes |
| Bug Type | Missing in Regression |
| Automatable | Yes - Need to automate |
| Interop | No |
| QE Owner | Deepthi K S |
| Source Sheet | Customer Escalations - Overall |

**Test Case Needed**: Yes - Test case - https://netskope.testrail.com/index.php?/cases/view/1541571 need to be enhanced based on the customer flexible dynamic steering.


Changed it to - https://netskope.testrail.com/index.php?/suites/view/963&group_by=cases:section_id&group_order=asc&display_deleted_cases=0&group_id=106120

**Comments**:
- Based on the fix, tgis flow was not handled well as part of the feature enhancement.
- This should have caught or discussed during FS/test plan review.
- Looks regression was not included for Monthly release.
- Test Gap Scope:feature coverage

Deepthi -
 - This was tested during DSE Feature - Worked fine, inbetween it broke no-one could Root cause What broke this.
 - New Link to be updated - https://netskope.testrail.com/index.php?/suites/view/963&group_by=cases:section_id&group_order=asc&display_deleted_cases=0&group_id=106120

---

## 2. ENG-422599

**Jira**: [ENG-422599](https://netskope.atlassian.net/browse/ENG-422599)

**Description**: ENG-422599 CLONE - [NSclient] Client going to fail-close after config update

| Field | Value |
|-------|-------|
| OS Platform | Win |
| Feature | Fail-close &  Flexible Dynamic Steering |
| Regression | Yes |
| Bug Type | Missing in Regression |
| Automatable | No |
| Interop | No |
| QE Owner | Ganesa Pandian S |
| Source Sheet | Customer Escalations - Overall |

**Test Case Needed**: Yes

**Comments**:
- Regression due to Flexible Dynamic steering Change(ENG-182503)
- Need to include this in Montly regression.
- Test Gap scope:Negative testing

---

## 3. ENG-455132

**Jira**: [ENG-455132](https://netskope.atlassian.net/browse/ENG-455132)

**Description**: ENG-455132 CLONE - Even though a Windows PC is at On-Premise, Off-Premise Steering Firewall app (ICMP)Exception is applied

| Field | Value |
|-------|-------|
| OS Platform | Windows |
| Feature | Cloud firewall,Flexible Dynamic Steering |
| Regression | Day-1 |
| Bug Type | Test Gap |
| Automatable | Yes |
| Interop | No |
| QE Owner | Deepthi K S |
| Source Sheet | Customer Escalations - Overall |

**Test Case Needed**: No

**Comments**:
- this is legacy bug before dynamic steering enhancement(before R107)
-  fix off-prem rule apply to on-prem
- Can be automatable (Need to include SSH/SMB protocol as well),
- Test Gap Scope: Day-1 Issue

Deepthi - All the ICMP cases already part of DSE Autmation runs and are executed every Release

---

## 4. ENG-482990

**Jira**: [ENG-482990](https://netskope.atlassian.net/browse/ENG-482990)

**Description**: ENG-482990 CLONE - [RSM] Captive portal not detected

| Field | Value |
|-------|-------|
| OS Platform | Windows & Mac |
| Feature | Fail-close- Steering&Exception |
| Regression | Day-1 |
| Bug Type | Enhancement |
| Automatable | No |
| Interop | No |
| QE Owner | Ganesa Pandian S |
| Source Sheet | Customer Escalations - Overall |

**Test Case Needed**: Yes

**Comments**:
- The nsclient never support meta refresh element HTTP redirection since day 1. Fix is to support simple meta refresh element.
- Need to add a detailed steps in test rail and have test case in Fail-close suite
https://netskope.testrail.io/index.php?/cases/view/2105055

---

## 5. ENG-548975

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

## 6. ENG-561500

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

## 7. ENG-566579

**Jira**: [ENG-566579](https://netskope.atlassian.net/browse/ENG-566579)

**Description**: ENG-566579 CLONE - [HubSpot][hubspot.goskope.com] Need to fix failclose NSClient log issue

| Field | Value |
|-------|-------|
| OS Platform | Windows |
| Feature | Fail-close |
| Regression | No |
| Bug Type | Corner case(Log changefor fal-close) |
| Automatable | Yes |
| Interop | No |
| QE Owner | Ganesa Pandian S |
| Source Sheet | Customer Escalations - Overall |

**Test Case Needed**: Yes

**Comments**:
- Need to add test case for Validatimng the change in Log event and can be automatable.

---

## 8. ENG-570306

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

## 9. ENG-649593

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

## 10. ENG-654108

**Jira**: [ENG-654108](https://netskope.atlassian.net/browse/ENG-654108)

**Description**: ENG-654108 CLONE - Citrix VPN traffic showing up as SYSTEM rather than nsload.exe after 114->125 upgrade, which MS Defender blocks

| Field | Value |
|-------|-------|
| OS Platform | Windows |
| Feature | Cloud Firewall-Steering&Exception |
| Regression | No |
| Bug Type | Enhancement |
| Automatable | Yes |
| Interop | Yes |
| QE Owner | Deepthi K S |
| Source Sheet | Customer Escalations - Overall |

**Test Case Needed**: Yes

**Comments**:
- For R122 and later, in CFW mode, both IPv4 and IPv6 web traffic exception handling is performed at the service level to address performance issues caused by handling IPv6 exceptions at the driver.  Fix- IPv4 web traffic exception handling must be performed at the driver level in CFW mode and IPV6 use service level(Customer has to use handleExceptionsAtDriver FF to have IPV6 exception at driver level.
- This is due to a design change/Performance improvement done on the R122.
- Make sure to have a very detailed coverage on Steering and Exception with Both CFW and Web Mode.
- Test case link is poining to [NPLAN-3020] 
- Interop: VPN, AV

Deepthi --> Thsi was an enhancement ticket for DSE to bypass traffic at driver. All the cases are available and  automated. They are run every release.

**Action Items**:
Corner case:  The issue happens in a specific environment and it is not reproduced in our lab and the test case is already automated.

---

## 11. ENG-718498

**Jira**: [ENG-718498](https://netskope.atlassian.net/browse/ENG-718498)

**Description**: ENG-718498 CLONE - [Netskope Internal Account] Large DNS over TCP bypassed with Cert Pinned Block in Place

| Field | Value |
|-------|-------|
| OS Platform | Windows |
| Feature | CertPinned app |
| Regression | No |
| Bug Type | Enhancement |
| Automatable | N/A |
| Interop | No |
| Reported Version | 126.0.0 |
| QE Owner | Abhishek Sharma |
| Source Sheet | Customer Escalations - Overall |

**Test Case Needed**: Yes

**Comments**:
This is an enhancement 
If certpinned app traffic is marked for block, DNS TCP traffic generated by app is getting bypassed. 
Enhancement is behind enableExceptionCheckForTcpDns
Added tests under the dns security:
C2464675
C2464676

---

## 12. ENG-733657

**Jira**: [ENG-733657](https://netskope.atlassian.net/browse/ENG-733657)

**Description**: ENG-733657 CLONE - Auto-upgrade From R126 to R129 failing in many windows machines

| Field | Value |
|-------|-------|
| OS Platform | Windows |
| Feature | AOAC |
| Regression | Yes |
| Bug Type | Test Gap |
| Automatable | N/A |
| Interop | No |
| Reported Version | 126.0.0 |
| QE Owner | Devendra Shirsath |
| Source Sheet | Customer Escalations - Overall |

**Test Case Needed**: No

**Comments**:
- The issue occurs because Post R125 its mandatory to enable the flag 
"disableWinStopServiceProtection": "True". If this flag is not enabled the install/upgrade fails - This is applicable only when user enables Self Portection or Password Uninstall or Fail Close

---

## 13. ENG-750658

**Jira**: [ENG-750658](https://netskope.atlassian.net/browse/ENG-750658)

**Description**: ENG-750658 CLONE - [Sunlife] Captive portal not detected and blocked due to failclose

| Field | Value |
|-------|-------|
| OS Platform | Windows |
| Feature | Fail-Close |
| Regression | No |
| Bug Type | Enhancement |
| Automatable | No |
| Interop | No |
| Reported Version | 129.0.0 |
| QE Owner | Kim Shaw |
| Source Sheet | Customer Escalations - Overall |

**Test Case Needed**: No

**Comments**:
client didn't accept signle quote and refresh time in MS captive portal detection file, the fix in client R133 has taken care of both issues.

---

## 14. ENG-751720

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

## 15. ENG-752117

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

## 16. ENG-795413

**Jira**: [ENG-795413](https://netskope.atlassian.net/browse/ENG-795413)

**Description**: ENG-795413 CLONE - [JN Data] Captive Portal URL detection is failing due to meta format

| Field | Value |
|-------|-------|
| OS Platform | Windows |
| Feature | Captive Portal Detection |
| Regression | Day-1 |
| Bug Type | Corner Case |
| Automatable | Yes |
| Interop | Yes |
| Reported Version | 132.0.0 |
| QE Owner | Anand Kumar S |
| Source Sheet | Customer Escalations - Overall |

**Test Case Needed**: Yes

**Comments**:
Issue arises due to multiple meta refresh tags in the response. While NS Client supports meta refresh tags, the presence of multiple tags on the captive portal response prevents the Embedded Browser from launching

---

## 17. ENG-801565

**Jira**: [ENG-801565](https://netskope.atlassian.net/browse/ENG-801565)

**Description**: CLONE - [JLL] NSC crash

| Field | Value |
|-------|-------|
| OS Platform | Windows |
| Feature | Fail-close |
| Regression | Day-1 |
| Bug Type | Test Gap |
| Automatable | No |
| Interop | No |
| Reported Version | 129.1.0 |
| QE Owner | Austin Cheng |
| Source Sheet | Customer Escalations - Overall |

**Test Case Needed**: No

**Comments**:
This is a corner case which can can only replicated by stress test for multiple hours. The test scenrio will be included in the future regular stability test.
Test Gap - load testing

---

## 18. ENG-851222

**Jira**: [ENG-851222](https://netskope.atlassian.net/browse/ENG-851222)

**Description**: ENG-851222 CLONE - On-prem detection using Egress IP does not work as expected.

| Field | Value |
|-------|-------|
| OS Platform | Windows |
| Feature | On-prem Detection |
| Regression | N/A |
| Bug Type | Enhancement |
| Automatable | No |
| Interop | N/A |
| Reported Version | 132.0.0 |
| QE Owner | Kim Shaw |
| Source Sheet | Customer Escalations - Overall |

**Test Case Needed**: N/A

**Comments**:
Need to prepare Egress IP, and non-Egress IP for testing, change configs on webui accordingly, the fix did fix the None steering mode which was supposed to do onprem dectection, also found Linux client had Egress IP feature issue that is tracked by another ticket

---

## 19. ENG-895081

**Jira**: [ENG-895081](https://netskope.atlassian.net/browse/ENG-895081)

**Description**: CLONE - [Bravo Servicos] Fail close not dropping traffic after a reboot.

| Field | Value |
|-------|-------|
| OS Platform | Windows |
| Feature | Steering&Exception |
| Regression | Day-1 |
| Bug Type | Test Gap |
| Automatable | No |
| Interop | No |
| Reported Version | 132.0.0 |
| QE Owner | Ganesa Pandian S |
| Source Sheet | Customer Escalations - Overall |

**Test Case Needed**: Yes

**Comments**:
NS client is failing to enforce failclose when NSGW is not reachable after system reboot
- Test Gap scope: negative case (reboot/startup flow under fail close with backend blocked (Fail-close+On-prem detection+ Reboot)

---

## 20. ENG-918451

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

## 21. ENG-928461

**Jira**: [ENG-928461](https://netskope.atlassian.net/browse/ENG-928461)

**Description**: CLONE - SK Finance || Netskope client disconnects and goes in Fail close state for multiple users

| Field | Value |
|-------|-------|
| OS Platform | Windows |
| Feature | Steering&Exception |
| Regression | N/A |
| Bug Type | N/A |
| Automatable | N/A |
| Interop | N/A |
| Reported Version | 132.0.0 |
| QE Owner | Poovarasan Chitravel |
| Source Sheet | Customer Escalations - Overall |

**Test Case Needed**: N/A

---

## 22. Fail Close & Captive portal

**Description**: Fail Close & Captive portal

| Field | Value |
|-------|-------|
| OS Platform | 5.0 |
| Feature | Ganesa Pandian S |
| Regression | N/A |
| Bug Type | N/A |
| Automatable | N/A |
| Interop | N/A |
| QE Owner | N/A |
| Source Sheet | Customer Escalations - Overall |

**Test Case Needed**: N/A

---

## 23. Interoperability Product Issues -Summary

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

## 24. Review  summary notes  for Feb to May 2024 - Tickets
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

## 25. Review  summary notes for Feb 2026:

- Nine issues were addressed in Feb 2026.
- Windows - 4, Mac - 2, Android - 2, All - 1
- Steering & Exception - 2, On-prem detection - 2, VDI - 1, NPA/BWAN Integration - 2, PKI - 1
- R132.0.0 (5) and R133.0.0 (3) had most issues; R129 (1) had fewer. Most issues occurred in Golden release versions (R132 &  one issue with R129).
- Learnings and action items: Improve coverage with negative scenarios using different features (device reboot, network switch). Improve test coverage with On-prem detection features (dynamic steering, fail-close, etc.).

**Description**: Review  summary notes for Feb 2026:

- Nine issues were addressed in Feb 2026.
- Windows - 4, Mac - 2, Android - 2, All - 1
- Steering & Exception - 2, On-prem detection - 2, VDI - 1, NPA/BWAN Integration - 2, PKI - 1
- R132.0.0 (5) and R133.0.0 (3) had most issues; R129 (1) had fewer. Most issues occurred in Golden release versions (R132 &  one issue with R129).
- Learnings and action items: Improve coverage with negative scenarios using different features (device reboot, network switch). Improve test coverage with On-prem detection features (dynamic steering, fail-close, etc.).

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

## 26. Review  summary notes for Nov 2025:

- Totally 10 issues were addressed in November.Most reported tickets are from the Windows platform and 2 issues related to iOS platform..
-  DEM Integration(2 issues), Backend(2 issues), Steering&Exception(2 issues), Interop (1 issue) and more than 1 issues in other components(Fail-close,captive Portal etc.,)

**Description**: Review  summary notes for Nov 2025:

- Totally 10 issues were addressed in November.Most reported tickets are from the Windows platform and 2 issues related to iOS platform..
-  DEM Integration(2 issues), Backend(2 issues), Steering&Exception(2 issues), Interop (1 issue) and more than 1 issues in other components(Fail-close,captive Portal etc.,)

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

## 27. Review  summary notes for Sep 2025:

- Totally 13 issues were addressed in September.Most reported tickets are from the Windows platform.
- Steering & Exception(5 issues), Fail-close(3) and AOAC(2 issues) components had more than 1 issues.
- AOAC quality needs to be improved(Create & review the Testplan and  execute in the coming release). 
- Need to Prioritize the Fail-close existing Blocker and Critical issues

**Description**: Review  summary notes for Sep 2025:

- Totally 13 issues were addressed in September.Most reported tickets are from the Windows platform.
- Steering & Exception(5 issues), Fail-close(3) and AOAC(2 issues) components had more than 1 issues.
- AOAC quality needs to be improved(Create & review the Testplan and  execute in the coming release). 
- Need to Prioritize the Fail-close existing Blocker and Critical issues

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

## 28. Review  summary notes for reference:
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

