# Traffic Steering / Bypass / Exception Bugs

Bugs related to traffic steering, bypass rules, exceptions, domain matching, DNS security, cloud firewall, SSL interception, WFP/Network Extension, IPv6, and split tunnel.

> Source: Escalation Bug Review spreadsheet, filtered by keywords: steering, bypass, exception, traffic, cloud firewall, DNS security, SSL, filter, IPv6, split tunnel.

**Total: 110 bugs**

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

## 2. Cloud Firewall

**Description**: Cloud Firewall

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
| Steering & Exception | Missing in regression |
| Client Endpoint Bug | 5.0 |

**Test Case Needed**: N/A

---

## 3. DNS Security

**Description**: DNS Security

| Field | Value |
|-------|-------|
| OS Platform | 6.0 |
| Feature | Abhishek Sharma |
| Regression | N/A |
| Bug Type | N/A |
| Automatable | N/A |
| Interop | N/A |
| QE Owner | N/A |
| Source Sheet | Customer Escalations - Overall |
| Steering & Exception | ChromeOS |

**Test Case Needed**: N/A

---

## 4. ENG-384041

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

## 5. ENG-395253

**Jira**: [ENG-395253](https://netskope.atlassian.net/browse/ENG-395253)

**Description**: ENG-395253 CLONE - [Marriott] Traffic bypassed due to category exception mismatch

| Field | Value |
|-------|-------|
| OS Platform | Mac |
| Feature | Catagory Bypass |
| Regression | Day-1 |
| Bug Type | Corner case |
| Automatable | Yes |
| Interop | No |
| QE Owner | Deepthi K S |
| Source Sheet | Customer Escalations - Overall |

**Test Case Needed**: Yes 

Deepthi - Only regression tests were involved with this No new TCs required.

**Comments**:
-This is day 1 issue by design. The NSClient query category by using IP address causes problem.
-  test case link added in the bug is not covering the exact test case.
- Missing regression coverage for monthly release.
https://netskope.testrail.com/index.php?/suites/view/963&group_by=cases:section_id&group_order=asc&display_deleted_cases=0&group_id=106106

Deepthis --> DSE automation runs has Category bypass tests that runs every regression

---

## 6. ENG-398387

**Jira**: [ENG-398387](https://netskope.atlassian.net/browse/ENG-398387)

**Description**: ENG-398387 CLONE - [Gilead] CFW No Longer Recognizing Traffic As Belonging to CFW App, Causing App Access Failure

| Field | Value |
|-------|-------|
| OS Platform | Windows & Mac |
| Feature | Cloud Firewall |
| Regression | Day-1 |
| Bug Type | Test Gap |
| Automatable | Yes |
| Interop | Yes |
| QE Owner | Karthic Mariappan |
| Source Sheet | Customer Escalations - Overall |

**Test Case Needed**: No

**Comments**:
- As per dev- it is a day-1 issue.
- Need to add this in automation.
- Test Gap Scope: Day-1 Issue
- Interop scope: VDI - Amazon Workspace

Deepthi - Regression Tests to be run. I see this issue is only on windows VDI Amazon. Also the Test cases are part of CFW cases already.  Karthic Mariappan Can you check if this needs to be added as part of VDI / Interop tests.

---

## 7. ENG-402499

**Jira**: [ENG-402499](https://netskope.atlassian.net/browse/ENG-402499)

**Description**: ENG-402499 CLONE - [NSclient Android] - Traffic not steered due to Quic protocol

| Field | Value |
|-------|-------|
| OS Platform | Windows |
| Feature | Steering&Exception |
| Regression | Day-1 |
| Bug Type | Test Gap |
| Automatable | Yes |
| Interop | No |
| QE Owner | N/A |
| Source Sheet | Customer Escalations - Overall |

**Test Case Needed**: No

**Comments**:
- QUIC protocol can not be supported by proxy. It’s the udp/443. Windows/mac/ios/linux clients as of today drop the Quic pkts
- Wrong test case mapping in Test rail.
- Need to Add a new test case and include it for Auromation regression.
- Test Gap Scope: Day-1 Issue

---

## 8. ENG-419687

**Jira**: [ENG-419687](https://netskope.atlassian.net/browse/ENG-419687)

**Description**: ENG-419687 CLONE - Device Classification Based on Cert : By just having a CA cert the status changes to Managed

| Field | Value |
|-------|-------|
| OS Platform | Windows & Mac |
| Feature | Device Classification |
| Regression | No |
| Bug Type | Feature is not working as per the design.
Test Gap |
| Automatable | No |
| Interop | No |
| QE Owner | Sean Chen |
| Source Sheet | Customer Escalations - Overall |

**Test Case Needed**: Yes

**Comments**:
- Feature is not working as per the design.when we just add/import CA certificate(without any Client certificate) under the "Current User" > Personal, the status changes to "Managed", so  user can get access to the CA certificate and can bypass these rules easily
-Test Gap scope: Negative testing

---

## 9. ENG-422599

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

## 10. ENG-425429

**Jira**: [ENG-425429](https://netskope.atlassian.net/browse/ENG-425429)

**Description**: ENG-425429 CLONE - CGGlobal: NS Client doesn't steer traffic when enabled

| Field | Value |
|-------|-------|
| OS Platform | Windows |
| Feature | Flexible Dynamic Steering |
| Regression | Yes |
| Bug Type | Corner case |
| Automatable | No |
| Interop | No |
| QE Owner | Deepthi K S |
| Source Sheet | Customer Escalations - Overall |

**Test Case Needed**: Yes

**Comments**:
- Issue specific to Dynamic steering.
- No test case details in the ticket.
- QE need to revisit.

Deepthi - Internal found issue - ENG-216546(oct/2022) is specific to Linux then it was raise part of a new OS support testing So not related to DS. Also the current issue is specific to windows and its a corner case .

---

## 11. ENG-434019

**Jira**: [ENG-434019](https://netskope.atlassian.net/browse/ENG-434019)

**Description**: ENG-434019 CLONE - Steering/Client config names get garbled in NS Client > Configuration window if names contain Japanese characters

| Field | Value |
|-------|-------|
| OS Platform | Windows |
| Feature | i18N |
| Regression | Day-1 |
| Bug Type | Test Gap |
| Automatable | No |
| Interop | No |
| QE Owner | Kim Shaw |
| Source Sheet | Customer Escalations - Overall |

**Test Case Needed**: Yes

**Comments**:
-Need to move this to respective testrail folder.
- Add this as part of Monthly regression.
- Include this for automation.
- Test Gap scope: Day-1 Issue(Localization)

---

## 12. ENG-434212

**Jira**: [ENG-434212](https://netskope.atlassian.net/browse/ENG-434212)

**Description**: ENG-434212 CLONE - [Morgan Stanley] Netskope client stays in "Disabled due to error" status after coming up from sleep

| Field | Value |
|-------|-------|
| OS Platform | Windows |
| Feature | AOAC |
| Regression | No |
| Bug Type | Test Gap( Test case never executed before due to GRE/IPsec setup limitation) |
| Automatable | No |
| Interop | No |
| QE Owner | Devendra Shirsath |
| Source Sheet | Customer Escalations - Overall |

**Test Case Needed**: Yes

**Comments**:
- Test case never executed before due to GRE/IPsec setup limitation.
- Need to add other steering mode cases for Montly regression.
- Test Gap scope: Need-Additional Coverage, Integration

---

## 13. ENG-436114

**Jira**: [ENG-436114](https://netskope.atlassian.net/browse/ENG-436114)

**Description**: ENG-436114 CLONE - [Nintendo of Europe GmbH] | macOS device not honoring the IPv6 local link DNS with NS client enabled

| Field | Value |
|-------|-------|
| OS Platform | Mac |
| Feature | IPv6,Steering&Exception |
| Regression | No |
| Bug Type | Test Gap(Need to add case for IPv6 Local IP) |
| Automatable | No |
| Interop | No |
| QE Owner | N/A |
| Source Sheet | Customer Escalations - Overall |

**Test Case Needed**: No

**Comments**:
- Destination use IPv6 address.
- Need to use IPv6 only or Dual Stack environment.
- Test case is not updated in test rail. Should be captured in CFW or IPv6 test suite.
- Test Gap scope: Need-Additional Coverage

---

## 14. ENG-438565

**Jira**: [ENG-438565](https://netskope.atlassian.net/browse/ENG-438565)

**Description**: ENG-438565 CLONE - Larger TCP segmented packets from loopback dropped when NSclient is enabled

| Field | Value |
|-------|-------|
| OS Platform | Windows |
| Feature | Steering&Exception |
| Regression | No |
| Bug Type | Test Gap(Corner case and not easy to replicate, however it would be better to add test case to cover large TCP segments On Loopback, Steering and DNS security features). |
| Automatable | No |
| Interop | Yes |
| QE Owner | Abhishek Sharma |
| Source Sheet | Customer Escalations - Overall |

**Test Case Needed**: Yes

**Comments**:
- The issue is due to arge segment packet drop in the loopback communication.
- Need to add the test case in test rail
-------------------------------------
comment from QA
Will add the test cases 
- Test Gap scope: need-additional coverage

---

## 15. ENG-438566

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

## 16. ENG-441957

**Jira**: [ENG-441957](https://netskope.atlassian.net/browse/ENG-441957)

**Description**: ENG-441957 CLONE - [Altec][Android] NPA disconnections after Network Switch

| Field | Value |
|-------|-------|
| OS Platform | Android |
| Feature | Steering&Exception |
| Regression | Yes |
| Bug Type | Internal found |
| Automatable | No |
| Interop | No |
| QE Owner | Anand Kumar S |
| Source Sheet | Customer Escalations - Overall |

**Test Case Needed**: Yes

**Comments**:
- Need extentive testing on Network switch case for Every Monthly release.
- QE has already reported this issue(ENG-410908) and this seems to be a regression which was broken in one of the earlier release but no trace.
- Test Gap scope: Negative testing

---

## 17. ENG-448002

**Jira**: [ENG-448002](https://netskope.atlassian.net/browse/ENG-448002)

**Description**: ENG-448002 CLONE - [Novartis] Client steering UDP 3478 port while on "All web traffic" steering

| Field | Value |
|-------|-------|
| OS Platform | Windows |
| Feature | DNS Security,
Steering&Exception |
| Regression | No |
| Bug Type | Test Gap(Custom ports with All traffic/Web mode - Steering and Bypass combination). Test it with Both TCP and UDP |
| Automatable | Yes |
| Interop | No |
| QE Owner | Abhishek Sharma |
| Source Sheet | Customer Escalations - Overall |

**Test Case Needed**: Yes

**Comments**:
- Add test case
- Can be automatable
-------------------------------
comment from QA
Will need to add the test for automation
- Test Gap scope: Need-Additional Coverage

---

## 18. ENG-450735

**Jira**: [ENG-450735](https://netskope.atlassian.net/browse/ENG-450735)

**Description**: ENG-450735 CLONE - After upgrade to 114, iOS users cannot access critical internal apps

| Field | Value |
|-------|-------|
| OS Platform | iOS |
| Feature | Steering&Exception |
| Regression | Yes |
| Bug Type | Missing in Regression |
| Automatable | No |
| Interop | No |
| QE Owner | Kim Shaw |
| Source Sheet | Customer Escalations - Overall |

**Test Case Needed**: Yes

**Comments**:
- This regression was caused by ENG-441957
- Need to cover this in Monthly regression.

---

## 19. ENG-451987

**Jira**: [ENG-451987](https://netskope.atlassian.net/browse/ENG-451987)

**Description**: ENG-451987 CLONE - [Morgan Stanley] Netskope Client status changed to "Enabled" state even though IPSec steering method was detected

| Field | Value |
|-------|-------|
| OS Platform | Windows |
| Feature | Steering&Exception |
| Regression | Yes |
| Bug Type | Corner case( Test case never executed before due to GRE/IPsec setup limitation) |
| Automatable | Yes |
| Interop | No |
| QE Owner | Deepthi K S |
| Source Sheet | Customer Escalations - Overall |

**Test Case Needed**: Yes

**Comments**:
- Need to add test case
- Can be automatable
- Need to add this test case for GRE/IPsec 

Deepthi - Karthic Mariappan Please change the assignment from Flexible Dynamic Steerign to Steerign MEthods. The QE link is wrongly Attached, As no Section for Steerign method is available.

---

## 20. ENG-453051

**Jira**: [ENG-453051](https://netskope.atlassian.net/browse/ENG-453051)

**Description**: ENG-453051 CLONE - [Idwall Tecnologia LTDA] Multiple issues encountered with NS client: SIGTERM

| Field | Value |
|-------|-------|
| OS Platform | Linux |
| Feature | Steering&Exception |
| Regression | No |
| Bug Type | Test Gap (Client service restart issue) |
| Automatable | No |
| Interop | No |
| QE Owner | Jithan A N |
| Source Sheet | Customer Escalations - Overall |

**Test Case Needed**: Yes

**Comments**:
- Test case exist but need to add detailed steps.
- https://netskope.testrail.io/index.php?/cases/view/1406712&group_by=cases:section_id&group_id=97481&group_order=asc&display_deleted_cases=0
Test Gap scope: Negative testing

---

## 21. ENG-454765

**Jira**: [ENG-454765](https://netskope.atlassian.net/browse/ENG-454765)

**Description**: ENG-454765 CLONE - Android devices not handling bypassed traffic properly

| Field | Value |
|-------|-------|
| OS Platform | Android |
| Feature | Steering&Exception |
| Regression | No |
| Bug Type | Test Gap(No setup to test this case) |
| Automatable | No |
| Interop | No |
| QE Owner | Anand Kumar S |
| Source Sheet | Customer Escalations - Overall |

**Test Case Needed**: No

**Comments**:
- No setup to test
- Need to discuss with Anand.
- Test Gap scope: Feature coverage

---

## 22. ENG-455132

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

## 23. ENG-456732

**Jira**: [ENG-456732](https://netskope.atlassian.net/browse/ENG-456732)

**Description**: ENG-456732 CLONE - [Stone Pagamentos] Windows NS Client 115.0.0.2048 and causing BSOD

| Field | Value |
|-------|-------|
| OS Platform | Windows |
| Feature | DNS Security |
| Regression | No |
| Bug Type | Test Gap(Need to add Longivity/Stress test) |
| Automatable | No |
| Interop | Yes |
| QE Owner | Abhishek Sharma |
| Source Sheet | Customer Escalations - Overall |

**Test Case Needed**: No

**Comments**:
- revert code change for dns/tcp handling caused by ENG-438566
-  Need to check if we need to add more scenarios/Longivity test
- Test Gap scope: Longevity tests, 
- Interop scope: Identity Security-CyberArk

---

## 24. ENG-482990

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

## 25. ENG-490822

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

## 26. ENG-495212

**Jira**: [ENG-495212](https://netskope.atlassian.net/browse/ENG-495212)

**Description**: ENG-495212 CLONE - Dem config exceptions in customer environment

| Field | Value |
|-------|-------|
| OS Platform | Windows |
| Feature | DEM |
| Regression | No |
| Bug Type | Corner case |
| Automatable | Yes |
| Interop | Yes |
| QE Owner | Abhishek Sharma |
| Source Sheet | Customer Escalations - Overall |

**Test Case Needed**: Yes

**Comments**:
- Need to add test case with 3rd party interop.
- Can be automatable
"- Need to add this case.
------------------------------------
Comments from dev
This is a third party library issue
------------------------------------
Comment from QA
This is not reproducible
Added an aditional check before calling the library. 
No addition automation or test required for this, Existing automation considered for this case

---

## 27. ENG-496412

**Jira**: [ENG-496412](https://netskope.atlassian.net/browse/ENG-496412)

**Description**: ENG-496412 CLONE - [Freeths LLP] Issue with NCP app in IOS device when Netskope client is enabled

| Field | Value |
|-------|-------|
| OS Platform | iOS |
| Feature | Steering&Exception |
| Regression | Day-1 |
| Bug Type | Enhancement |
| Automatable | Yes |
| Interop | No |
| QE Owner | Kim Shaw |
| Source Sheet | Customer Escalations - Overall |

**Test Case Needed**: No

**Comments**:
- Need to add detailed steps in https://netskope.testrail.io/index.php?/cases/view/2154206
- TCP over DNS is not supported for IOS and it was taken as enhancement and fixed for the customer.

---

## 28. ENG-499052

**Jira**: [ENG-499052](https://netskope.atlassian.net/browse/ENG-499052)

**Description**: ENG-499052 CLONE - Teams send messages not working with NSC on Android

| Field | Value |
|-------|-------|
| OS Platform | Android |
| Feature | Steering&Exception |
| Regression | Yes |
| Bug Type | Missing in Regressions |
| Automatable | Yes |
| Interop | No |
| QE Owner | Karthic Mariappan |
| Source Sheet | Customer Escalations - Overall |

**Test Case Needed**: No

**Comments**:
- Cert Pinned exceptions were not enforced for teams app at os level from 112.1 onwards.  This change might have introduced the issue. Reintroduce the os level bypass
- Need to include this in automation.
- Add test casae onadding  “Microsoft Teams” app on both Cloud Steering and Cert pinned exception rule
- Can be auromatable
- Test Gap scope:Need-Additional Coverage

---

## 29. ENG-525399

**Jira**: [ENG-525399](https://netskope.atlassian.net/browse/ENG-525399)

**Description**: ENG-525399 CLONE - CertPinned app exception bypass causing ALL traffic to be bypassed

| Field | Value |
|-------|-------|
| OS Platform | Android |
| Feature | Steering&Exception |
| Regression | No |
| Bug Type | Test Gap( Need to inlude Native Apps and use regular expression on Cert pinned apps) |
| Automatable | Yes |
| Interop | No |
| QE Owner | Anand Kumar S |
| Source Sheet | Customer Escalations - Overall |

**Test Case Needed**: Yes

**Comments**:
-Need to add test case
- Can be automatable
- Test Gap scope: Need-Additional Coverage

---

## 30. ENG-533981

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

## 31. ENG-538734

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

## 32. ENG-543661

**Jira**: [ENG-543661](https://netskope.atlassian.net/browse/ENG-543661)

**Description**: ENG-543661 CLONE - [CEPSA CORP and EP] Extreme degradation in download speed with NS client

| Field | Value |
|-------|-------|
| OS Platform | Win |
| Feature | IPV6 Perf |
| Regression | No |
| Bug Type | Enhancement |
| Automatable | No |
| Interop | Yes |
| QE Owner | N/A |
| Source Sheet | Customer Escalations - Overall |

**Test Case Needed**: No

**Comments**:
- Improved the IPV6 Performance degradation.
- Include IPv6 Perf test for Golden release
- Test Gap scope: Performance testing
- Interop Scope: AV- Trendmicro

---

## 33. ENG-555622

**Jira**: [ENG-555622](https://netskope.atlassian.net/browse/ENG-555622)

**Description**: ENG-555622 CLONE - [Constantia Business Services GmbH] Citrix servers are experiencing BSOD with Netskope

| Field | Value |
|-------|-------|
| OS Platform | Windows |
| Feature | DNS Security |
| Regression | No |
| Bug Type | Corner case(Need to include cases where DNS IP shuold be in Steering and Bypass list) |
| Automatable | Yes |
| Interop | Yes |
| QE Owner | Abhishek Sharma |
| Source Sheet | Customer Escalations - Overall |

**Test Case Needed**: Yes

**Comments**:
- Need to add Load test with DNS security as per verificaiton.
- Can be automatable.
- Test Gap scope: Need-Additional Coverage
- Interop Scope: VDI-Citrix VDI

---

## 34. ENG-557778

**Jira**: [ENG-557778](https://netskope.atlassian.net/browse/ENG-557778)

**Description**: ENG-557778 CLONE - Unable to remotely collect logs from any device post Steering Hardening - nspubkey.pem.enc, err:2

| Field | Value |
|-------|-------|
| OS Platform | Windows |
| Feature | Secure Enrollment |
| Regression | No |
| Bug Type | Test Gap - missing test case. Neither dev nor QE test it. |
| Automatable | Yes |
| Interop | No |
| QE Owner | Jackal Kao |
| Source Sheet | Customer Escalations - Overall |

**Test Case Needed**: Yes

**Comments**:
- Need to add test case
- Can be automatable
- This is a missing test case. Neither dev nor QE test it. We should add it to QE test case. (Secure Config, encryptClientConfig)
- Test Gap scope: Need-Additional Coverage

**Action Items**:
Automation Task - https://netskope.atlassian.net/browse/ENG-782325

---

## 35. ENG-561500

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

## 36. ENG-577918

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

## 37. ENG-579740

**Jira**: [ENG-579740](https://netskope.atlassian.net/browse/ENG-579740)

**Description**: ENG-579740 CLONE - [TK] DNS Traffic is getting steered - exception rule not working properly

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
- Need to add PTR related cases in Test rail.
- Test cases can be automated
-- Test Gap scope: Need-Additional Coverage

========================
comment from QA
This is a new enhancement, where PTR record type will support the domain name

---

## 38. ENG-591725

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

## 39. ENG-592681

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

## 40. ENG-593481

**Jira**: [ENG-593481](https://netskope.atlassian.net/browse/ENG-593481)

**Description**: ENG-593481 CLONE - [Maif] apt-get update on Linux host is failing with Client enabled

| Field | Value |
|-------|-------|
| OS Platform | Linux |
| Feature | Flexible Dynamic Steering |
| Regression | Day-1 |
| Bug Type | Test Gap |
| Automatable | Yes |
| Interop | No |
| QE Owner | Jithan A N |
| Source Sheet | Customer Escalations - Overall |
| Steering & Exception | Yes |

**Test Case Needed**: No

**Comments**:
- apt-get update fails on Linux (Ubuntu 22.04), Instead of steering the traffix, it bypass it wrongly.
- similar to a previous fixed issue (ENG-270784) and it again resurfaced.

---

## 41. ENG-595031

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

## 42. ENG-609001

**Jira**: [ENG-609001](https://netskope.atlassian.net/browse/ENG-609001)

**Description**: ENG-609001 Installation with deb file creates cert errors for browser traffic

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
new enhancement request. .deb packag with Ubuntu 24.04 is not supported.

---

## 43. ENG-619327

**Jira**: [ENG-619327](https://netskope.atlassian.net/browse/ENG-619327)

**Description**: ENG-619327 [BUG] CLONE - PSIRT: Out-of-Bounds Read Vulnerability

| Field | Value |
|-------|-------|
| OS Platform | Windows |
| Feature | N/A |
| Regression | No |
| Bug Type | Security Fix / Corner Case |
| Automatable | No |
| Interop | No |
| QE Owner | Abhishek Sharma |
| Source Sheet | Customer Escalations - Overall |
| Steering & Exception | Yes |

**Test Case Needed**: Yes

**Comments**:
-Security Fix
- Client handling the Malformed DNS packet with larger size could corrupt the stack.
- Not easy to replicate and verify. Dev verify through UNit test.

---

## 44. ENG-624953

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

## 45. ENG-625957

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

## 46. ENG-629428

**Jira**: [ENG-629428](https://netskope.atlassian.net/browse/ENG-629428)

**Description**: ENG-629428 Windows server 2012 : NS client uses Traffic steering type as "All web traffic" when Traffic steering type configured is "All traffic"

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
Looks win-2012 specific and needs investigation.

---

## 47. ENG-635104

**Jira**: [ENG-635104](https://netskope.atlassian.net/browse/ENG-635104)

**Description**: ENG-635104 CLONE - CFW Not Blocking Tor Anonymity Browser

| Field | Value |
|-------|-------|
| OS Platform | Windows |
| Feature | Cloud Firewall |
| Regression | No |
| Bug Type | Internal found |
| Automatable | Yes |
| Interop | No |
| QE Owner | Deepthi K S |
| Source Sheet | Customer Escalations - Overall |
| Steering & Exception | Yes |

**Test Case Needed**: Yes

**Comments**:
- Block action witjh CFW steering was broken.
- Already QE has reported this issue internally(ENG-449139)
- Need to be covered by automation.

Deepthi - It is covered in Testcases and also in Automation in DSE. It runs every release

---

## 48. ENG-637794

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

## 49. ENG-645301

**Jira**: [ENG-645301](https://netskope.atlassian.net/browse/ENG-645301)

**Description**: ENG-645301 MacOS NSClient exclude DHCP on CFW mode

| Field | Value |
|-------|-------|
| OS Platform | Mac |
| Feature | Cloud Firewall |
| Regression | No |
| Bug Type | Corner case |
| Automatable | No |
| Interop | No |
| QE Owner | Snehalkumar Donga |
| Source Sheet | Customer Escalations - Overall |
| Steering & Exception | No |

**Test Case Needed**: Yes

**Comments**:
- macOS 15.4 bug breaks DHCP in NSClient CFW mode when removing network dongle.User needs to reboot to workaround it.
- Negative Test case

---

## 50. ENG-649593

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

## 51. ENG-652754

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

## 52. ENG-654108

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

## 53. ENG-655009

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

## 54. ENG-671659

**Jira**: [ENG-671659](https://netskope.atlassian.net/browse/ENG-671659)

**Description**: ENG-671659 CLONE - [Bureau Veritas SA] iOS device not honoring the IPv6 local link DNS with NS client enabled

| Field | Value |
|-------|-------|
| OS Platform | iOS |
| Feature | Steering&Exception |
| Regression | Day-1 |
| Bug Type | Test-gap |
| Automatable | No |
| Interop | No |
| QE Owner | Kim Shaw |
| Source Sheet | Customer Escalations - Overall |

**Test Case Needed**: No

**Comments**:
- The problem affects all users globally when iOS devices connect via hotspot to another iOS device
- On iOS, for the DNS UDP bypassing, if the destination is IPv6 Linklocal address, set the interface scope_id, if any, to the destination socket address
- Test Gap scope: Negative testing(Day-1)

---

## 55. ENG-672788

**Jira**: [ENG-672788](https://netskope.atlassian.net/browse/ENG-672788)

**Description**: ENG-672788 CLONE - [Maurices] Internal Website access is broken on iOS

| Field | Value |
|-------|-------|
| OS Platform | iOS |
| Feature | Steering&Exception |
| Regression | No |
| Bug Type | Corner case |
| Automatable | Yes |
| Interop | No |
| QE Owner | Kim Shaw |
| Source Sheet | Customer Escalations - Overall |

**Test Case Needed**: Yes

**Comments**:
- Internal IPs (10.96.70.11, 10.96.70.12) and domains are configured for bypass, but iOS NPA prevents system-level private IP bypass.
- Fix: when NPA is enabled, if the exceptional IP does not overlap with the NPA IP ranges, it should be added to the system's excludeRoute.
- Corner case.

---

## 56. ENG-680385

**Jira**: [ENG-680385](https://netskope.atlassian.net/browse/ENG-680385)

**Description**: ENG-680385 CLONE - macOS users unable to receive DHCP address when changing networks on 15.5 with 126 (ENG-642315 related)

| Field | Value |
|-------|-------|
| OS Platform | Mac |
| Feature | Steering&Exception |
| Regression | No |
| Bug Type | Corner case |
| Automatable | No |
| Interop | No |
| QE Owner | Poovarasan Chitravel |
| Source Sheet | Customer Escalations - Overall |

**Test Case Needed**: No

**Comments**:
- Apple macOS 15.4 and 15.5 have a bug that passes the DHCP traffic to system extension transparentProxy. OS Upgrade
- Not easy to reproduce.
- Fix: NSClient always exclude DHCP traffic via system excludeRules on macOS no matter what steering type it is.
- Corner case.

---

## 57. ENG-685566

**Jira**: [ENG-685566](https://netskope.atlassian.net/browse/ENG-685566)

**Description**: ENG-685566 CLONE - [Sentry Insurance Company] Netbios traffic is bypassed with CFW enabled

| Field | Value |
|-------|-------|
| OS Platform | Windows |
| Feature | Windows |
| Regression | Day-1 |
| Bug Type | Enhancement |
| Automatable | Yes |
| Interop | No |
| QE Owner | Deepthi K S |
| Source Sheet | Customer Escalations - Overall |

**Test Case Needed**: Yes

**Comments**:
- The issue involved Netbios traffic bypassing Netskope CFW and being blocked by the customer's firewall.
- The problem was identified when traffic to a malware site was blocked on port 443 but not on port 137.

---

## 58. ENG-690881

**Jira**: [ENG-690881](https://netskope.atlassian.net/browse/ENG-690881)

**Description**: ENG-690881 CLONE - [bb.goskope.com] MACos user with admin level can uninstall NSC with password protection.

| Field | Value |
|-------|-------|
| OS Platform | Mac |
| Feature | Install & Upgrade |
| Regression | Day-1 |
| Bug Type | Enhancement |
| Automatable | Yes |
| Interop | No |
| QE Owner | Ganesa Pandian S |
| Source Sheet | Customer Escalations - Overall |

**Test Case Needed**: No

**Comments**:
Users with admin level can uninstall Netskope from their Macs without inputting or bypassing the uninstall code requirement using this command:
sudo '/Library/Application Support/Netskope/STAgent/Remove Netskope Client.app/Contents/MacOS/Remove Netskope Client' auto_uninstall\
The fix now added checks for password before doing uninstallation. I have added https://netskope.testrail.io/index.php?/cases/view/2413804 to do Mac NS client uninstallation using this option

---

## 59. ENG-693785

**Jira**: [ENG-693785](https://netskope.atlassian.net/browse/ENG-693785)

**Description**: ENG-693785 CLONE - Users getting incorrect steering configs

| Field | Value |
|-------|-------|
| OS Platform | Provisioner Platform (Prov) |
| Feature | Prov-User-Manager |
| Regression | No |
| Bug Type | Corner case |
| Automatable | No |
| Interop | No |
| QE Owner | Harmeet Singh Gujral |
| Source Sheet | Customer Escalations - Overall |

**Test Case Needed**: Yes

**Comments**:
- Some part of code treated user,usergroup and IDs as case-sensitive (preserving the original case), while others treated them as case-insensitive (converting everything to lowercase). This mismatch led to duplicate or mismatched records in the database, causing users to receive incorrect configurations.
- skip_user_id_mapping_lookup feature flag was introduce. When enabled, this flag skips the problematic lookup in the user_id_mapping collection that could point to deleted or mixed-case records, ensuring the system fetches the correct active user record. And cache entrise were also cleanedup.

**Action Items**:
Corner case Not automatable - The issue was caused due to the mis-matched user record created on the DB and it lead to pick the wrong configuration.

---

## 60. ENG-707515

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

## 61. ENG-710784

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

## 62. ENG-718498

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

## 63. ENG-718773

**Jira**: [ENG-718773](https://netskope.atlassian.net/browse/ENG-718773)

**Description**: ENG-718773 CLONE - [Swift] Tamperproof protection bypass

| Field | Value |
|-------|-------|
| OS Platform | Windows |
| Feature | Self-Protection |
| Regression | Day-1 |
| Bug Type | Enhancement |
| Automatable | N/A |
| Interop | No |
| Reported Version | 126.0.0 |
| QE Owner | Kim Shaw |
| Source Sheet | Customer Escalations - Overall |

**Test Case Needed**: No

**Comments**:
- This is a Day-1 issue.
- when we use the ‘Save logs’ option from Client UI, user can navigate into the protected folders, the fix prevents this to happen when Protect Client Configuration enabled

---

## 64. ENG-729025

**Jira**: [ENG-729025](https://netskope.atlassian.net/browse/ENG-729025)

**Description**: ENG-729025 CLONE - Continue with ENG-611760 || User unable to search google while Netskope is enabled

| Field | Value |
|-------|-------|
| OS Platform | Mac |
| Feature | N/A |
| Regression | Day-1 |
| Bug Type | Corner case |
| Automatable | No |
| Interop | No |
| Reported Version | 125.0.0 |
| QE Owner | Deepthi K S |
| Source Sheet | Customer Escalations - Overall |

**Test Case Needed**: No

**Comments**:
This is not reproduced inhouse. This requires 
1. stf0 environment 
2. FF bypassPreferredIPv4macOS to be enabled
3. Network to be ipv4 only

---

## 65. ENG-729176

**Jira**: [ENG-729176](https://netskope.atlassian.net/browse/ENG-729176)

**Description**: ENG-729176 CLONE - [fnbo] High CPU on Domain Controller after installing 123.0.15.2461

| Field | Value |
|-------|-------|
| OS Platform | Windows |
| Feature | Steering&Exception |
| Regression | Yes |
| Bug Type | Test Gap |
| Automatable | Yes |
| Interop | No |
| Reported Version | 123.0.0 |
| QE Owner | Austin Cheng |
| Source Sheet | Customer Escalations - Overall |

**Test Case Needed**: No

**Comments**:
- The issue is generated with massive SMB connections when it is web traffic steering mode. Non-web traffic should not be handled by the driver.

- Need to test Cloud App mode and Web Traffic mode with both Web and non-Web traffic. Then monitor the resource status such as CPU.

**Action Items**:
Automation Task - https://netskope.atlassian.net/browse/ENG-782341

---

## 66. ENG-733735

**Jira**: [ENG-733735](https://netskope.atlassian.net/browse/ENG-733735)

**Description**: ENG-733735 CLONE - [Thai Petroleum] Android client - Enable button is greyed out once the Client is disabled by User

| Field | Value |
|-------|-------|
| OS Platform | Android |
| Feature | Client UI |
| Regression | Day-1 |
| Bug Type | Enhancement |
| Automatable | Yes |
| Interop | No |
| Reported Version | 129.0.0 |
| QE Owner | Anand Kumar S |
| Source Sheet | Customer Escalations - Overall |

**Test Case Needed**: Yes

**Comments**:
The problem happened because on Android we don't have separate enable/disable button for SWG and NPA. Currently, if it detects steering mode is NONE, it will grey out the Enable button. This logic is incorrect when NPA is enabled in the configuration. To fix this issue, we will also check if NPA is enabled, if yes, we will leave the Enable button in enabled state instead of greyed out.

---

## 67. ENG-739968

**Jira**: [ENG-739968](https://netskope.atlassian.net/browse/ENG-739968)

**Description**: ENG-739968 CLONE - [Southcoast Health System] Netskope Client steering private IPs to SWG

| Field | Value |
|-------|-------|
| OS Platform | Windows |
| Feature | Steering&Exception |
| Regression | Day-1 |
| Bug Type | Corner case |
| Automatable | No |
| Interop | No |
| Reported Version | 123.0.0 |
| QE Owner | Poovarasan Chitravel |
| Source Sheet | Customer Escalations - Overall |

**Test Case Needed**: No

**Comments**:
- This is a corner case and race condition happened when writing and reading nsexception.json. 
- We already have the automation coverage for this scenario, this use case cannot be caught with automation.

---

## 68. ENG-742949

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

## 69. ENG-744457

**Jira**: [ENG-744457](https://netskope.atlassian.net/browse/ENG-744457)

**Description**: ENG-744457 CLONE - [tricare] One way audio issue for WFC app on Zebra Android phone

| Field | Value |
|-------|-------|
| OS Platform | Android |
| Feature | Steering&Exception |
| Regression | Yes |
| Bug Type | Missing in Regression |
| Automatable | Yes |
| Interop | No |
| Reported Version | 129.0.0 |
| QE Owner | Anand Kumar S |
| Source Sheet | Customer Escalations - Overall |

**Test Case Needed**: No

**Comments**:
- This issue was caused due to the fix ENG-673392.
- We have this test case in the existing automation(Cert Pinned apps). Need to improve the validation steps the current automation.

**Action Items**:
Automation task: https://netskope.atlassian.net/browse/ENG-782346

---

## 70. ENG-747635

**Jira**: [ENG-747635](https://netskope.atlassian.net/browse/ENG-747635)

**Description**: ENG-747635 CLONE - client crashing on windows 10

| Field | Value |
|-------|-------|
| OS Platform | Windows |
| Feature | Steering&Exception |
| Regression | No |
| Bug Type | Corner case |
| Automatable | Yes |
| Interop | No |
| Reported Version | 126.0.0 |
| QE Owner | Austin Cheng |
| Source Sheet | Customer Escalations - Overall |

**Test Case Needed**: N/A

**Comments**:
- This issue is difficult to reproduce. In massive connections with rapidly connection changing(create/delete) environment could help to be easier to reproduce. Consider to add this test into automation.

---

## 71. ENG-752117

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

## 72. ENG-753965

**Jira**: [ENG-753965](https://netskope.atlassian.net/browse/ENG-753965)

**Description**: ENG-753965 CLONE - [Ross Stores] NSC incorrectly bypassing traffic due to incorrect session ID being used.

| Field | Value |
|-------|-------|
| OS Platform | Windows |
| Feature | Steering&Exception |
| Regression | Day-1 |
| Bug Type | Corner Case |
| Automatable | No |
| Interop | No |
| Reported Version | 126.0.0 |
| QE Owner | Anand Kumar S |
| Source Sheet | Customer Escalations - Overall |

**Test Case Needed**: No

**Comments**:
This issue specifically occurs in systems where a user's re-login generates a new session ID rather than reusing the previous one. Nsclient incorrect caching to update this change in this specific corner-case is the root cause of the packet misdirection.

---

## 73. ENG-765691

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

## 74. ENG-773191

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

## 75. ENG-782593

**Jira**: [ENG-782593](https://netskope.atlassian.net/browse/ENG-782593)

**Description**: ENG-782593 Device Classification Rule Cannot Be Saved When AV Product Name Contains ™ (TM) Symbol gives 400 Bad Request as error

| Field | Value |
|-------|-------|
| OS Platform | Backend |
| Feature | NSC-FT-DeviceClassification |
| Regression | Day-1 |
| Bug Type | Enhancement |
| Automatable | Yes |
| Interop | Yes |
| Reported Version | 131.0.0 |
| QE Owner | Sean Chen |
| Source Sheet | Customer Escalations - Overall |

**Test Case Needed**: Yes

**Comments**:
The regular expression that Backend used for filtering AV name applys white list machenism, we only allow common used characters as AV name previously.

---

## 76. ENG-784777

**Jira**: [ENG-784777](https://netskope.atlassian.net/browse/ENG-784777)

**Description**: ENG-784777 CLONE - websites timing out when attempted to open the first time on Linux machines

| Field | Value |
|-------|-------|
| OS Platform | Linux |
| Feature | Steering&Exception |
| Regression | No |
| Bug Type | Corner Case |
| Automatable | No |
| Interop | No |
| Reported Version | 129.1.0 |
| QE Owner | Jithan A N |
| Source Sheet | Customer Escalations - Overall |

**Test Case Needed**: N/A

**Comments**:
Limit the port range, run traffic and check the packet captures to ensure that ACKs are received

---

## 77. ENG-793442

**Jira**: [ENG-793442](https://netskope.atlassian.net/browse/ENG-793442)

**Description**: ENG-793442 CLONE - [ForceMotors] Blocked Websites are accessible when NS Client Network is changed

| Field | Value |
|-------|-------|
| OS Platform | Windows |
| Feature | Steering&Exception |
| Regression | Day-1 |
| Bug Type | Test Gap |
| Automatable | No |
| Interop | No |
| Reported Version | 130.0.0 |
| QE Owner | Poovarasan Chitravel |
| Source Sheet | Customer Escalations - Overall |

**Test Case Needed**: No

**Comments**:
This blocked website is able to access when change the network with IPv6. Disabling IPv6 on affected machines resulted in the expected blocking behavior within 30 seconds, indicating a possible IPv6-related processing delay.
Test Gap - Negative tests

---

## 78. ENG-803728

**Jira**: [ENG-803728](https://netskope.atlassian.net/browse/ENG-803728)

**Description**: ENG-803728 CLONE - [Visa Technology] Blank page for login.microsoftonline.com on IOS

| Field | Value |
|-------|-------|
| OS Platform | iOS |
| Feature | Steering&Exception |
| Regression | Day-1 |
| Bug Type | Corner Case |
| Automatable | No |
| Interop | No |
| Reported Version | 131.0.0 |
| QE Owner | Poovarasan Chitravel |
| Source Sheet | Customer Escalations - Overall |

**Test Case Needed**: No

**Comments**:
It is a corner case, this happens in a specific scenario where two consecutive DNS queries for the same domain (login.microsoftonline.com) happened very closely, the second DNS response has completely different IP addresses. The iOS app updates the IP mapping; it impacts the existing connections. The fix is, the NSC app will retain existing connection mapping when the private IP to public IP mapping changes.

---

## 79. ENG-805334

**Jira**: [ENG-805334](https://netskope.atlassian.net/browse/ENG-805334)

**Description**: ENG-805334 CLONE - [Deloitte] NS Client and Citrix Secure Access VPN/Cisco AnyConnect Inter-Op issue

| Field | Value |
|-------|-------|
| OS Platform | Windows |
| Feature | Steering&Exception |
| Regression | No |
| Bug Type | Corner Case |
| Automatable | No |
| Interop | Yes |
| Reported Version | 129.2.0 |
| QE Owner | Poovarasan Chitravel |
| Source Sheet | Customer Escalations - Overall |

**Test Case Needed**: Yes

**Comments**:
The problem arose after upgrading Citrix Secure Access to version 25.1.1.27, where WFP mode is enabled by default, causing DNS failures at the transport layer. Enabling the "injectDNSAtNetworkLayer" flag resolves the issue for Citrix VPN users but conflicts with Cisco VPN users.

---

## 80. ENG-851222

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

## 81. ENG-855335

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

## 82. ENG-872456

**Jira**: [ENG-872456](https://netskope.atlassian.net/browse/ENG-872456)

**Description**: ENG-872456 [Android/ChromeOS] NS Client keeps crashing when enrolling to a tenant with over 30,000 domains

| Field | Value |
|-------|-------|
| OS Platform | ChromeOS |
| Feature | Client Crash |
| Regression | N/A |
| Bug Type | Internal found |
| Automatable | N/A |
| Interop | N/A |
| Reported Version | 133.0.0 |
| QE Owner | Andy Su |
| Source Sheet | Customer Escalations - Overall |

**Test Case Needed**: N/A

**Comments**:
It is usually unusual to have so many (30,000+) domains in steering config, but it is not impossible, so QE better to prepare a test tenant that have volume test data

---

## 83. ENG-895081

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

## 84. ENG-897416

**Jira**: [ENG-897416](https://netskope.atlassian.net/browse/ENG-897416)

**Description**: CLONE - [FedRAMP][Netskope PS] FedRAMP / PBMM NSClient initiates outbound connections to sfchecker.goskope.com (commercial domain) despite govskope tenant context

| Field | Value |
|-------|-------|
| OS Platform | All |
| Feature | PKI/Other steering method |
| Regression | Day-1 |
| Bug Type | Test Gap |
| Automatable | Yes |
| Interop | No |
| Reported Version | 132.0.0 |
| QE Owner | Suresh Vinjamuru |
| Source Sheet | Customer Escalations - Overall |

**Test Case Needed**: N/A

**Comments**:
Currently Secure Forwarder functionality is deprecated or non-impacting, the presence of outbound DNS resolution and connection attempts to a commercial domain is problematic for regulated environments and often violates customer firewall allow-listing policies.

With this fix, we stopped sending dns resolutions to sfchecker.goskope.com
- Test Gap scope: Negative case (wrong legacy behavior still running)

---

## 85. ENG-906435

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

## 86. ENG-917549

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

## 87. ENG-918131

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

## 88. ENG-918451

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

## 89. ENG-925885

**Jira**: [ENG-925885](https://netskope.atlassian.net/browse/ENG-925885)

**Description**: CLONE - [PSIRT] Anti-Tampering Bypass in Client Driver

| Field | Value |
|-------|-------|
| OS Platform | Windows |
| Feature | PSIRIT |
| Regression | Day 1 |
| Bug Type | Corner Case |
| Automatable | No |
| Interop | N/A |
| Reported Version | 129.1.0 |
| QE Owner | Austin Cheng |
| Source Sheet | Customer Escalations - Overall |

**Test Case Needed**: N/A

**Comments**:
This can be only replicated with specific IOCTL tool to attack stadrv to get the permission.

---

## 90. ENG-925887

**Jira**: [ENG-925887](https://netskope.atlassian.net/browse/ENG-925887)

**Description**: CLONE - [PSIRT] DISABLING NETSKOPE Client VIA ANTI-TAMPERING BYPASS

| Field | Value |
|-------|-------|
| OS Platform | Windows |
| Feature | PSIRIT |
| Regression | Day 1 |
| Bug Type | Corner Case |
| Automatable | No |
| Interop | N/A |
| Reported Version | 129.1.0 |
| QE Owner | Austin Cheng |
| Source Sheet | Customer Escalations - Overall |

**Test Case Needed**: N/A

**Comments**:
This can be only replicated with specific IOCTL tool to attack stadrv to get the permission.

---

## 91. ENG-928461

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

## 92. ENG-948106

**Jira**: [ENG-948106](https://netskope.atlassian.net/browse/ENG-948106)

**Description**: CLONE - [Samsung Research America Inc] - Netskope client causing crashes on linux.

| Field | Value |
|-------|-------|
| OS Platform | Linux |
| Feature | Performance |
| Regression | Day 1 |
| Bug Type | Corner Case |
| Automatable | Yes |
| Interop | N/A |
| Reported Version | 135.1.0 |
| QE Owner | Jithan A N |
| Source Sheet | Customer Escalations - Overall |

**Test Case Needed**: N/A

**Comments**:
Create a steering config with domains between 230 chars to 255 chars, and more than 35k of them to check if we see a crash.

---

## 93. Flexible Dynamic Steering

**Description**: Flexible Dynamic Steering

| Field | Value |
|-------|-------|
| OS Platform | 4.0 |
| Feature | Deepthi K S |
| Regression | N/A |
| Bug Type | N/A |
| Automatable | N/A |
| Interop | N/A |
| QE Owner | N/A |
| Source Sheet | Customer Escalations - Overall |
| Steering & Exception | Test Gap |

**Test Case Needed**: N/A

---

## 94. IPv6

**Description**: IPv6

| Field | Value |
|-------|-------|
| OS Platform | 1.0 |
| Feature | Deepthi K S |
| Regression | N/A |
| Bug Type | N/A |
| Automatable | N/A |
| Interop | N/A |
| QE Owner | N/A |
| Source Sheet | Customer Escalations - Overall |

**Test Case Needed**: N/A

---

## 95. Interoperability Product Issues -Summary

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

## 96. Review  summary notes  for Feb to May 2024 - Tickets
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

## 97. Review  summary notes for Feb 2026:

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

## 98. Review  summary notes for Jan 2026:

- Windows leads with 3 reported issues, followed by Mac and ChromeOS with 2 each. Android and Linux each have 1 issue, with an additional 1 affecting both Windows and Mac.
- Config Encryption with 2 issues, followed by Client Crash and Integration (NPA and DEM) with 2 issues each.
- R133.0.0 and R132.0.0 are the most affected releases, each with 4 reported issues.
-Learnings + Action Items: Improve coverage with Config Encryption(Steering Hardening), Include test case with Limt testing

**Description**: Review  summary notes for Jan 2026:

- Windows leads with 3 reported issues, followed by Mac and ChromeOS with 2 each. Android and Linux each have 1 issue, with an additional 1 affecting both Windows and Mac.
- Config Encryption with 2 issues, followed by Client Crash and Integration (NPA and DEM) with 2 issues each.
- R133.0.0 and R132.0.0 are the most affected releases, each with 4 reported issues.
-Learnings + Action Items: Improve coverage with Config Encryption(Steering Hardening), Include test case with Limt testing

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

## 99. Review  summary notes for Nov 2025:

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

## 100. Review  summary notes for Sep 2025:

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

## 101. Review  summary notes for reference:
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

## 102. Review Notes:
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

## 103. Steering & Bypass

**Description**: Steering & Bypass

| Field | Value |
|-------|-------|
| OS Platform | 16.0 |
| Feature | Deepthi K S Abhishek Sharma Karthic Mariappan |
| Regression | N/A |
| Bug Type | N/A |
| Automatable | N/A |
| Interop | N/A |
| QE Owner | N/A |
| Source Sheet | Customer Escalations - Overall |
| Steering & Exception | Corner case |

**Test Case Needed**: N/A

---



## --- Added from Excel (not previously in bugs/) ---

## 104. ENG-394366

**Jira**: [ENG-394366](https://netskope.atlassian.net/browse/ENG-394366)

**Description**: [Reybanpac] Android devices with NSClient are unable to login to MS Teams due of Reverse Proxy

| Field | Value |
|-------|-------|
| OS Platform | Android |
| Feature | Client-Reverse proxy |
| Regression | Yes |
| Bug Type | Missing in Regression |
| Automatable | No |
| Interop | No |
| Source Sheet | Customer Escalations - Overall |

**Comments**: - Regression(Issue not seen in R108 and noticied with R112)  and it breaks reverse Proxy
- need to setup ADFS - Reverse proxy integration test for Monthly Regression.
- https://netskope.testrail.io/index.php?/cases/view/1792510&group_by=cases:section_id&group_id=124890&group_order=asc&display_deleted_cases=0
- Integration test

---
## 105. ENG-430841

**Jira**: [ENG-430841](https://netskope.atlassian.net/browse/ENG-430841)

**Description**: i18n issue with user alert justification hint

| Field | Value |
|-------|-------|
| OS Platform | Windows |
| Feature | i18N |
| Regression | Day-1 |
| Bug Type | Test Gap(Need to improve Localization language support) |
| Automatable | No |
| Interop | No |
| Source Sheet | Customer Escalations - Overall |

**Comments**: - From the bug history it appears to be there from Day-1
- Need to move this ticket in Customer found defects or i18N test rail folder.
- Test Gap scope: Day-1 Issue

---
## 106. ENG-487256

**Jira**: [ENG-487256](https://netskope.atlassian.net/browse/ENG-487256)

**Description**: [Fannie Mae] Users reporting slowness/upload failures with Workday/Microsoft Teams chat on R117

| Field | Value |
|-------|-------|
| OS Platform | Windows |
| Feature | Proxy |
| Regression | Yes |
| Bug Type | Missing in Regression |
| Automatable | No |
| Interop | Yes |
| Source Sheet | Customer Escalations - Overall |

**Comments**: - (Was broken due to another fix ENG-390309)
- Make sure to add  it in Monthly or Golden release regression.
- Interop Scope: Proxy - squid

---
## 107. ENG-505439

**Jira**: [ENG-505439](https://netskope.atlassian.net/browse/ENG-505439)

**Description**: EPoC where EP is Netskope EP 163.116.128.80 (Port 80)

| Field | Value |
|-------|-------|
| OS Platform | Windows |
| Feature | Proxy |
| Regression | No |
| Bug Type | Corner case. (Added FF ignoreInactiveSystemProxy) |
| Automatable | No |
| Interop | Yes |
| Source Sheet | Customer Escalations - Overall |

**Comments**: - Need to add test case
- new FF - ignoreInactiveSystemProxy
- Interop Scope: Proxy - squid

---
## 108. ENG-596840

**Jira**: [ENG-596840](https://netskope.atlassian.net/browse/ENG-596840)

**Description**: Inconsistent Client Configuration Display for Nested AD Groups on Netskope Tenant UI

| Field | Value |
|-------|-------|
| OS Platform | Web UI |
| Feature | NSC-FT-ClientConfiguration |
| Source Sheet | Q226 Feb |

---
## 109. ENG-664964

**Jira**: [ENG-664964](https://netskope.atlassian.net/browse/ENG-664964)

**Description**: [Emirates National Oil Company] client config failed to download due to 405 error

| Field | Value |
|-------|-------|
| OS Platform | NSC-SVC-Addonman (Backend) |
| Feature | NSC-FT-CLientConfiguration |
| Regression | No |
| Bug Type | Corner case |
| Automatable | Yes |
| Interop | No |
| Source Sheet | Customer Escalations - Overall |

**Comments**: When there is a new FF request initiated and the backed is already processing the POST /client/config might end up crfeating the stale entry.
- Need to add test case to cover this scenario.
- Bug in Open state as on Jun 1st. But issue already identified and addressed in ENG-661846

---
## 110. ENG-795746

**Jira**: [ENG-795746](https://netskope.atlassian.net/browse/ENG-795746)

**Description**: [Tier 1/Stellantis]100+ Clients Unable to Update Configuration After Enabling Secure Configuration Service

| Field | Value |
|-------|-------|
| OS Platform | Windows |
| Feature | NSC-FT-ClientConfiguration |
| Regression | Day-1 |
| Bug Type | Corner Case |
| Automatable | yes |
| Interop | No |
| Source Sheet | Customer Escalations - Overall |

**Comments**: This is a corner case where NSconfig.Json is corrupted for some unknown reason and QE is not able to replicate this issue. the fix is addressing issues where certificates were not decrypting or being removed, with ongoing work to resolve PKI parsing errors

---
