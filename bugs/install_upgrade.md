# Install / Upgrade / Enrollment Bugs

Bugs related to installation, upgrade, downgrade, uninstall, enrollment, and onboarding of NSClient.

> Source: Escalation Bug Review spreadsheet, filtered by keywords: install, upgrade, uninstall, enrollment, migration, addon, onboard.

**Total: 63 bugs**

---

## 1. CLONE - [ Rockland Trust ] Client service not starting with error " The dependency service or group failed to start

**Description**: CLONE - [ Rockland Trust ] Client service not starting with error " The dependency service or group failed to start

| Field | Value |
|-------|-------|
| OS Platform | Windows |
| Feature | Upgrade/Rollback |
| Regression | Yes |
| Bug Type | Test Gap (Negative Scenario) |
| Automatable | Yes |
| Interop | No |
| QE Owner | Ganesa Pandian S |
| Source Sheet | Escalation Bug-Review Q226 (Feb) |
| Steering & Exception | No |
| Client Endpoint Bug | Yes |
| Backend Issue | No |

**Test Case Needed**: No

**Comments**:
- Both Auto upgrdae and Rollback has failed.
-  Need to update the detail steps to similate the scenario - https://netskope.testrail.io/index.php?/cases/view/1489422
- Need to check this can be automatable.

---

## 2. ENG-420917

**Jira**: [ENG-420917](https://netskope.atlassian.net/browse/ENG-420917)

**Description**: ENG-420917 CLONE - Some active devices do not show on the Devices page
ENG-420918 CLONE - [Home Depot] Device is not visible on the Devices Page
ENG-421086 CLONE - Multiple Devices are missing from the tenant UI( Setting>Security cloud platform> Devices)

| Field | Value |
|-------|-------|
| OS Platform | Windows & Mac |
| Feature | Client Status |
| Regression | Yes |
| Bug Type | Test Gap |
| Automatable | No |
| Interop | No |
| QE Owner | N/A |
| Source Sheet | Customer Escalations - Overall |

**Test Case Needed**: No

**Comments**:
- Backend Migration issue.
- Need to add test case for this use case and have more verification.
- Test Gap scope: Negative testing

---

## 3. ENG-420918

**Jira**: [ENG-420918](https://netskope.atlassian.net/browse/ENG-420918)

**Description**: ENG-420918 CLONE - [Home Depot] Device is not visible on the Devices Page

| Field | Value |
|-------|-------|
| OS Platform | Windows & Mac |
| Feature | Client Status |
| Regression | Yes |
| Bug Type | Test Gap |
| Automatable | No |
| Interop | No |
| QE Owner | N/A |
| Source Sheet | Customer Escalations - Overall |

**Test Case Needed**: No

**Comments**:
"- Backend Migration issue.
- Need to add test case for this use case and have more verification."
- Test Gap scope: Negative testing

---

## 4. ENG-424991

**Jira**: [ENG-424991](https://netskope.atlassian.net/browse/ENG-424991)

**Description**: ENG-424991 CLONE - [ZOOP] Xiaomi Android agent failed to enroll

| Field | Value |
|-------|-------|
| OS Platform | Android |
| Feature | IDP |
| Regression | No |
| Bug Type | Test Gap(Improve Platform Coverage) |
| Automatable | Yes |
| Interop | No |
| QE Owner | Anand Kumar S |
| Source Sheet | Customer Escalations - Overall |

**Test Case Needed**: Yes

**Comments**:
- Issue specifc to Xiaomi model
- Purchased Xiomi for testing and included in Regression.
- Test Gap scope: Platform coverage

---

## 5. ENG-429954

**Jira**: [ENG-429954](https://netskope.atlassian.net/browse/ENG-429954)

**Description**: ENG-429954 client_install_time is getting changed more oftenly in client_status

| Field | Value |
|-------|-------|
| OS Platform | Windows |
| Feature | DEM |
| Regression | No |
| Bug Type | Test Gap |
| Automatable | No |
| Interop | No |
| QE Owner | Jackal Kao |
| Source Sheet | Customer Escalations - Overall |

**Test Case Needed**: Yes

**Comments**:
- test case marked in the testrail needs improbment. 
- Have to rewrite the case and have backend and E2E validation.
-Test Gap scope:  Integration test
- Negative testing,

---

## 6. ENG-446703

**Jira**: [ENG-446703](https://netskope.atlassian.net/browse/ENG-446703)

**Description**: ENG-446703 CLONE - [NSclient] - MSI files pilling up - upgrade from R108 to R111.1 failing

| Field | Value |
|-------|-------|
| OS Platform | Windows |
| Feature | Install & Upgrade |
| Regression | No |
| Bug Type | Test Gap (Add more verification on Upgrade negative scenarios) |
| Automatable | No |
| Interop | No |
| QE Owner | Ganesa Pandian S |
| Source Sheet | Customer Escalations - Overall |

**Test Case Needed**: Yes

**Comments**:
- MSI files pile-up issue was acknowledged and partially fixed in versions R105/R107, but problems persist in R108.
- Add a new test case.
- Difficult to automate.
- Test Gap scope: Negative testing

---

## 7. ENG-450735

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

## 8. ENG-463329

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

## 9. ENG-466704

**Jira**: [ENG-466704](https://netskope.atlassian.net/browse/ENG-466704)

**Description**: ENG-466704 CLONE - Secure Enrolment is failing for random users on Citrix machine after Client upgrade to 114.

| Field | Value |
|-------|-------|
| OS Platform | Windows |
| Feature | Secure Enrollment |
| Regression | Day-1 |
| Bug Type | Test Gap |
| Automatable | No |
| Interop | Yes |
| QE Owner | N/A |
| Source Sheet | Customer Escalations - Overall |

**Test Case Needed**: No

**Comments**:
- day 1 issue on UPN secure enrollment. The nsclient code has a bug that when there is enrollment failure
-Not automatable. Manual and Multiuser.
- Test Gap Scope: Day-1 Issue
- Interop Scope: VDI - Citrix/AVD

---

## 10. ENG-472565

**Jira**: [ENG-472565](https://netskope.atlassian.net/browse/ENG-472565)

**Description**: ENG-472565 CLONE - [Nsclient] - Autoupgrade not triggering R111 to R114
ENG-470539 CLONE - [BNC] - Netskope Client upgrade doesn't trigger on MAC devices

| Field | Value |
|-------|-------|
| OS Platform | Mac |
| Feature | Install & Upgrade |
| Regression | No |
| Bug Type | Test Gap |
| Automatable | No |
| Interop | No |
| QE Owner | N/A |
| Source Sheet | Customer Escalations - Overall |

**Test Case Needed**: No

**Comments**:
- Need to have different cases for Auto Upgrade
- Test Gap scope: Need-Additional Coverage(Install/Upgrade)

---

## 11. ENG-487939

**Jira**: [ENG-487939](https://netskope.atlassian.net/browse/ENG-487939)

**Description**: ENG-487939 CLONE - Client unable to upgrade until Client Self Protection is disabled

| Field | Value |
|-------|-------|
| OS Platform | Windows |
| Feature | Self Protection |
| Regression | Yes |
| Bug Type | Missing in Regression |
| Automatable | Yes |
| Interop | Yes |
| QE Owner | N/A |
| Source Sheet | Customer Escalations - Overall |

**Test Case Needed**: No

**Comments**:
- This issue was caused by the Log Improvement change.
- Can be automatable
- Include Self-protection case in Auto-upgrade.
- Test Gap scope: Need-Additional Coverage
- Interop Scope: VDI - Citrix/AVD

---

## 12. ENG-497728

**Jira**: [ENG-497728](https://netskope.atlassian.net/browse/ENG-497728)

**Description**: ENG-497728 Order of getbrandingbyemail and getbrandingbyupn can cause incorrect error response to be cached and returned to user

| Field | Value |
|-------|-------|
| OS Platform | Backend |
| Feature | Secure Enrollment |
| Regression | No |
| Bug Type | Test Gap |
| Automatable | No |
| Interop | No |
| QE Owner | Sean Chen |
| Source Sheet | Customer Escalations - Overall |

**Test Case Needed**: Yes

**Comments**:
- The issue was identified in the provisioner common code, where email and UPN cache keys were not properly distinguished. The fix is to include qualifiers in cache keys to differentiate between UPN and email data.
- Test with Both UPN adn Email E2E and verify both client and Server side-interpolated into redis keys.
- Need to add testcase in Backend suite
- Test Gap scope: Need-Additional Coverage

---

## 13. ENG-533221

**Jira**: [ENG-533221](https://netskope.atlassian.net/browse/ENG-533221)

**Description**: ENG-533221 CLONE - Netskope Client disabled with no error

| Field | Value |
|-------|-------|
| OS Platform | Windows |
| Feature | Install & Upgrade |
| Regression | Day-1 |
| Bug Type | Test Gap |
| Automatable | No |
| Interop | NO |
| QE Owner | Devendra Shirsath |
| Source Sheet | Customer Escalations - Overall |

**Test Case Needed**: Yes

**Comments**:
- Day 1 issue
- Need to add this case in Schedule upgrade
- Need to include in monthly/Golden release upgrade.
- Test Gap Scope: Day-1 Issue

---

## 14. ENG-534944

**Jira**: [ENG-534944](https://netskope.atlassian.net/browse/ENG-534944)

**Description**: ENG-534944 CLONE - [Deliveroo] Monitored users not showing the agents that were online for reported time

| Field | Value |
|-------|-------|
| OS Platform | Mac |
| Feature | DEM |
| Regression | Yes |
| Bug Type | Missing in Regression |
| Automatable | Yes |
| Interop | No |
| QE Owner | Abhishek Sharma |
| Source Sheet | Customer Escalations - Overall |

**Test Case Needed**: Yes

**Comments**:
- Need to add test case for DEm Health monitor
- Can be automatable
----------------------------------------------
This regression was caught due to another fix ENG-429954 
https://github.com/netSkope/client/pull/6101/files.  missed the upgrade case when nsclient older that R120 will not be having the "appinstalltimestamp" in nsconfig.json.
Fix made under the ClientStatusHandler::prepareMessageForDem
This change is related to clientstatus. Install time reported as part of the client status. Karthic to add test case in DEM clientstatus.

**Action Items**:
Automation Task - https://netskope.atlassian.net/browse/ENG-782310

---

## 15. ENG-543228

**Jira**: [ENG-543228](https://netskope.atlassian.net/browse/ENG-543228)

**Description**: ENG-543228 CLONE - [Qualcomm] Install script falling back to idp mode of installation for hostname/account name with 'idp' keyword

| Field | Value |
|-------|-------|
| OS Platform | Mac |
| Feature | MDM Script |
| Regression | Yes |
| Bug Type | Test gap |
| Automatable | N/A |
| Interop | Yes |
| QE Owner | Ganesa Pandian S |
| Source Sheet | Customer Escalations - Overall |

**Test Case Needed**: Yes

**Comments**:
- Need to add seperate cases with the newsly updated JAMF script file.
- Test all deployment mode which uses IDP and UPN.
- Test Gap scope: install-upgrade testing, interop test
- Interop : MDM

---

## 16. ENG-543428

**Jira**: [ENG-543428](https://netskope.atlassian.net/browse/ENG-543428)

**Description**: ENG-543428 CLONE - [Phillips-Van Heusen] Client enrollment failures on Windows devices

| Field | Value |
|-------|-------|
| OS Platform | Win |
| Feature | Secure Enrollment |
| Regression | No |
| Bug Type | Test Gap |
| Automatable | Yes |
| Interop | No |
| QE Owner | Jithan A N |
| Source Sheet | Customer Escalations - Overall |

**Test Case Needed**: Yes

**Comments**:
- Need to come up more cases on IDP with Secure tokens.
- Need to monthly or golden releqase regression on Multi-user
- Test Gap scope: interop test
- Interop: VDI - Citrix/AVD

---

## 17. ENG-544070

**Jira**: [ENG-544070](https://netskope.atlassian.net/browse/ENG-544070)

**Description**: ENG-544070 CLONE - [Telstra] Multiuser machines Second user - No Enrollment needed

| Field | Value |
|-------|-------|
| OS Platform | Windows |
| Feature | IDP |
| Regression | Day-1 |
| Bug Type | Enhancement |
| Automatable | Yes |
| Interop | No |
| QE Owner | Karthic Mariappan |
| Source Sheet | Customer Escalations - Overall |

**Test Case Needed**: No

**Comments**:
- The reason that the IDP is not kicked in for the second user is because its UPN enrollment is successful, the user’s branding file is there already
- The fix would be if the NSC is in IDP mode, meaning there is valid nsidpconfig.json in %ProgramData% folder, the NSC will not try UPN enrollment no matter secure enrollment is enabled or not.

**Action Items**:
Automation Task- https://netskope.atlassian.net/browse/ENG-782313

---

## 18. ENG-551274

**Jira**: [ENG-551274](https://netskope.atlassian.net/browse/ENG-551274)

**Description**: ENG-551274 CLONE - Client on R117.1.3.2130 will not automatically upgrade to R120.1.2.2190 even after a reboot or a Network change.

| Field | Value |
|-------|-------|
| OS Platform | Windows |
| Feature | Install & Upgrade |
| Regression | No |
| Bug Type | Corner case |
| Automatable | No |
| Interop | No |
| QE Owner | Snehalkumar Donga |
| Source Sheet | Customer Escalations - Overall |

**Test Case Needed**: Yes

**Comments**:
- Logs folder is normally created under AppData by stAgentUI process, But somehow it was not created during the upgrade. Looks to be. acorner case and not able to simulated in QE lab. 
- Add test case(Based on QA recommendation)

---

## 19. ENG-556081

**Jira**: [ENG-556081](https://netskope.atlassian.net/browse/ENG-556081)

**Description**: ENG-556081 NS Client Enrollment with MS Autopilot failed.

| Field | Value |
|-------|-------|
| OS Platform | Windows |
| Feature | Secure Enrollment |
| Regression | No |
| Bug Type | Corner case |
| Automatable | No |
| Interop | Yes |
| QE Owner | Poovarasan Chitravel |
| Source Sheet | Customer Escalations - Overall |

**Test Case Needed**: Yes

**Comments**:
- Need to add Test case.
- Include this case in Monthly or golden release validation.
- Interop: Intune MDM

---

## 20. ENG-557778

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

## 21. ENG-573164

**Jira**: [ENG-573164](https://netskope.atlassian.net/browse/ENG-573164)

**Description**: ENG-573164 CLONE - One time password for disabling client gets disabled after few attempts

| Field | Value |
|-------|-------|
| OS Platform | Windows |
| Feature | OTP |
| Regression | No |
| Bug Type | Test Gap( Need to include more test on OTP backend) |
| Automatable | No |
| Interop | No |
| QE Owner | Sean Chen |
| Source Sheet | Customer Escalations - Overall |

**Test Case Needed**: Yes

**Comments**:
- Need to add test case. The issue is due to the backend API ENG-475524 [OTP][Addonman] Addonman crashed while posting OTP api with incorrect payload. 
- Add a test case for Backend OTP API test plan to cover this scenario.
- Test Gap scope: Need-Additional Coverage

---

## 22. ENG-577598

**Jira**: [ENG-577598](https://netskope.atlassian.net/browse/ENG-577598)

**Description**: ENG-577598 CLONE - After editing “Email Invitation Expired” template Customisations in "Email Invitation Expired" Template Saved but Not Reflected in Rendered Page

| Field | Value |
|-------|-------|
| OS Platform | Windows & Mac |
| Feature | Install & Upgrade |
| Regression | No |
| Bug Type | Corner case |
| Automatable | Yes |
| Interop | No |
| QE Owner | N/A |
| Source Sheet | Customer Escalations - Overall |

**Test Case Needed**: No

**Comments**:
- Can be automatable

---

## 23. ENG-591721

**Jira**: [ENG-591721](https://netskope.atlassian.net/browse/ENG-591721)

**Description**: ENG-591721 CLONE - [ TIVIT TERCEIRIZACAO DE PROCESSOS] NSComs module in service can't accept internal communication connection. (NSC deadlock issue)

| Field | Value |
|-------|-------|
| OS Platform | Windows |
| Feature | Multi-user |
| Regression | No |
| Bug Type | Corner case. |
| Automatable | No |
| Interop | No |
| QE Owner | Karthic Mariappan |
| Source Sheet | Escalation Bug-Review Q226 (Feb) |
| Steering & Exception | No |
| Client Endpoint Bug | Yes |
| Backend Issue | No |

**Test Case Needed**: No

**Comments**:
- NSComs module issue to handle the communication between stagensvc and UI(client service socket connection error). and this causes enroll issue with multi-user.
- Not easy to reproduce

---

## 24. ENG-593814

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

## 25. ENG-601667

**Jira**: [ENG-601667](https://netskope.atlassian.net/browse/ENG-601667)

**Description**: ENG-601667 CLONE - [ Rockland Trust ] Client service not starting with error " The dependency service or group failed to start "

| Field | Value |
|-------|-------|
| OS Platform | Windows |
| Feature | Install & Upgrade |
| Regression | Day-1 |
| Bug Type | Corner case |
| Automatable | Yes |
| Interop | No |
| QE Owner | Ganesa Pandian S |
| Source Sheet | Customer Escalations - Overall |

**Test Case Needed**: Yes

**Comments**:
- During upgrade failure happens, client installer attempts to rollback to previously installed version and update the event to the backend(client status0, but in this bug it updates with Wrong cloient version.
- Test case is not added in to the test rail- Need to include it  in Rollback or Upgrade test plan.
- Negative Testing

---

## 26. ENG-608191

**Jira**: [ENG-608191](https://netskope.atlassian.net/browse/ENG-608191)

**Description**: ENG-608191 CLONE - [NPA Browser Access] nsconfig.json failing to download FRA2

| Field | Value |
|-------|-------|
| OS Platform | Client Services (Backend) |
| Feature | NSC-SVC-Addon |
| Regression | Yes |
| Bug Type | Missing in Regression |
| Automatable | Yes |
| Interop | No |
| QE Owner | Andy Su |
| Source Sheet | Customer Escalations - Overall |
| Steering & Exception | No |

**Test Case Needed**: No

**Comments**:
- Current `/v6/addon/publisher/config` use `authorizeV7` instaed of `authorizeV5` ast result it check for JWT signature and return error `401`
- NPA Integration issue. Need to cover new publisher deployment with latest latest client services supporting all V2, V5 and V7 API's
- Suggest  NPA QE to include this case as well.
- Test Gap scope: Need-Additional Coverage, Integration- NPA

---

## 27. ENG-609001

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

## 28. ENG-624445

**Jira**: [ENG-624445](https://netskope.atlassian.net/browse/ENG-624445)

**Description**: ENG-624445 Deploy-125.0.0.2584 | fed02-mp-preprod | stork_addonman Deploy Failed

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
| Client Endpoint Bug | No |
| Backend Issue | Yes |

**Test Case Needed**: N/A

---

## 29. ENG-625672

**Jira**: [ENG-625672](https://netskope.atlassian.net/browse/ENG-625672)

**Description**: ENG-625672 Windows 8 : NS client created with Window 2012 support is not getting installed and getting "A digitally signed driver is required" notification

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
Need to understand is this specific to NSclient -2k12 support build or the previous build as well. If this is regressiom then it needs to be fixed.

---

## 30. ENG-637576

**Jira**: [ENG-637576](https://netskope.atlassian.net/browse/ENG-637576)

**Description**: ENG-637576 CLONE - [PDEM-Professional] user scores are blank in useroverview;nsclient messages does say payload validation issue: tenant ID does not match

| Field | Value |
|-------|-------|
| OS Platform | Windows |
| Feature | DEM |
| Regression | Yes |
| Bug Type | Corner case. |
| Automatable | Yes |
| Interop | No |
| QE Owner | Abhishek Sharma |
| Source Sheet | Escalation Bug-Review Q226 (Feb) |
| Steering & Exception | No |
| Client Endpoint Bug | Yes |
| Backend Issue | No |

**Test Case Needed**: Yes

**Comments**:
- During Config update, While rotating the securing enrollment token gets rthe error, client reset the tenent id as '0'.This caused the DEM post wrong data and failure.
- Need to add a test case.(QE details were udpated with  bug ID, need to add a new test case in ter tails

---

## 31. ENG-654108

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

## 32. ENG-671884

**Jira**: [ENG-671884](https://netskope.atlassian.net/browse/ENG-671884)

**Description**: ENG-671884 CLONE - [Dream11] MAC - Client not posting the Uninstall status to backend

| Field | Value |
|-------|-------|
| OS Platform | Mac |
| Feature | Install & Upgrade |
| Regression | No |
| Bug Type | Corner case. |
| Automatable | No |
| Interop | No |
| QE Owner | Ganesa Pandian S |
| Source Sheet | Customer Escalations - Overall |

**Test Case Needed**: Yes

**Comments**:
- This issue happen only when flag clientEncryptBranding set to 1.
- move "InstallerUtil --post_uninstall" cmd calling sequence. 
Perform this cmd before calling uninstallAuxilirySvc().
- Recommendation: Make sure to add this test case in Golden regression suite where all feature flags are enabled in the tenant.
- Corner case.

---

## 33. ENG-680208

**Jira**: [ENG-680208](https://netskope.atlassian.net/browse/ENG-680208)

**Description**: ENG-654877 CLONE - NS client compatibility issues on macos

| Field | Value |
|-------|-------|
| OS Platform | Mac |
| Feature | Install & Upgrade |
| Regression | No |
| Bug Type | Internal found |
| Automatable | No |
| Interop | No |
| QE Owner | Deepthi K S |
| Source Sheet | Customer Escalations - Overall |

**Test Case Needed**: No

**Comments**:
- Due to the recent Mac UI changes, it introduces this issue, This issue was internally reported by QE(ENG-536868 & ENG-528321)
- Install and Upgarde path.

Deepthi - Internally reported and doesnt need any new cases as this is found via observations

---

## 34. ENG-680385

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

## 35. ENG-690881

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

## 36. ENG-726784

**Jira**: [ENG-726784](https://netskope.atlassian.net/browse/ENG-726784)

**Description**: ENG-726784 CLONE - [Multiple Customers] Duplicate device entries after upgrading to 126.0.0.2387 and client installation date is missing

| Field | Value |
|-------|-------|
| OS Platform | Windows |
| Feature | AOAC |
| Regression | Yes |
| Bug Type | Test Gap |
| Automatable | No |
| Interop | No |
| Reported Version | 126.0.0 |
| QE Owner | Devendra Shirsath |
| Source Sheet | Customer Escalations - Overall |

**Test Case Needed**: No

**Comments**:
- We never tried Install Upgrade on AOAC devices hence the issue occurs.
- We have added AOAC in our test plan 
- NSC-Windows may fall back to the legacy method of generating nsdeviceuid

---

## 37. ENG-729176

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

## 38. ENG-733657

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

## 40. ENG-756815

**Jira**: [ENG-756815](https://netskope.atlassian.net/browse/ENG-756815)

**Description**: ENG-756815 CLONE - [IPF] Client auto-upgrade schedule is not working

| Field | Value |
|-------|-------|
| OS Platform | Windows |
| Feature | Install & Upgrade |
| Regression | No |
| Bug Type | Test Gap |
| Automatable | Yes |
| Interop | No |
| Reported Version | 123.0.0 |
| QE Owner | Austin Cheng |
| Source Sheet | Customer Escalations - Overall |

**Test Case Needed**: Yes

**Comments**:
- Update schedule has issues with the 3rd Wed monthly. It is better to have all test combination (behind/ahead schedule, daily, weekly, monthly)

---

## 41. ENG-773191

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

## 42. ENG-840031

**Jira**: [ENG-840031](https://netskope.atlassian.net/browse/ENG-840031)

**Description**: ENG-840031 CLONE - Crash investigation - WSL segfault when starting nsclient enrollment after install.

| Field | Value |
|-------|-------|
| OS Platform | Linux |
| Feature | IDP |
| Regression | No |
| Bug Type | Enhancement |
| Automatable | No |
| Interop | N/A |
| Reported Version | 131.0.0 |
| QE Owner | Kim Shaw |
| Source Sheet | Customer Escalations - Overall |

**Test Case Needed**: N/A

**Comments**:
WSL IDP is not supported, customer somehow wanted to try it with custom configurations, I have tested client to ensure IDP doesn't cause WSL or Windows to crash, and cli stress test passed.

---

## 43. ENG-846555

**Jira**: [ENG-846555](https://netskope.atlassian.net/browse/ENG-846555)

**Description**: ENG-846555 CLONE - [STONE INSTITUICAO] Linux - Auto-Upgrade fails with Security hardening

| Field | Value |
|-------|-------|
| OS Platform | Linux |
| Feature | Install & Upgrade |
| Regression | Day-1 |
| Bug Type | Enhancement |
| Automatable | Yes |
| Interop | N/A |
| Reported Version | 120.0.0 |
| QE Owner | Jithan A N |
| Source Sheet | Customer Escalations - Overall |

**Test Case Needed**: N/A

**Comments**:
Installation of client uses /tmp folder on linux. If customer has enabled security hardening like not executing any files from /tmp, then our client install fails. The fix is : If /tmp has noexec permission set, then /opt/netskope/stagent/makeself would be used else /tmp would be used.

---

## 44. ENG-872456

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

## 45. ENG-925894

**Jira**: [ENG-925894](https://netskope.atlassian.net/browse/ENG-925894)

**Description**: CLONE - Netskope install failing on Amazon Workspaces

| Field | Value |
|-------|-------|
| OS Platform | Windows |
| Feature | Install/Upgrade |
| Regression | Day 1 |
| Bug Type | Corner Case |
| Automatable | No |
| Interop | N/A |
| Reported Version | 132.0.0 |
| QE Owner | Sean Chen |
| Source Sheet | Customer Escalations - Overall |

**Test Case Needed**: N/A

**Comments**:
The issue is caused by a missing smart card DLL during service startup on certain Windows setups, such as VDI, when the smart card check is enabled.
Hard to reproduce because DLL loading timing is controlled by the OS driver scheduler.

---

## 46. ENG-951409

**Jira**: [ENG-951409](https://netskope.atlassian.net/browse/ENG-951409)

**Description**: CLONE - [Genpact] Customer have noticed that on user machine NSC suddenly was removed silently, this happens while upgrading client to 135.1.4.2595

| Field | Value |
|-------|-------|
| OS Platform | Windows |
| Feature | Install/Upgrade |
| Regression | Day-1 |
| Bug Type | Test Gap |
| Automatable | No |
| Interop | N/A |
| Reported Version | 135.0.0 |
| QE Owner | Austin Cheng |
| Source Sheet | Customer Escalations - Overall |

**Test Case Needed**: N/A

**Comments**:
The spec is UI need to be dismissed after enrollment. We did not focus on testing this behavior.

---

## 47. Install & Upgrade

**Description**: Install & Upgrade

| Field | Value |
|-------|-------|
| OS Platform | 4.0 |
| Feature | Snehalkumar Donga |
| Regression | N/A |
| Bug Type | N/A |
| Automatable | N/A |
| Interop | N/A |
| QE Owner | N/A |
| Source Sheet | Customer Escalations - Overall |

**Test Case Needed**: N/A

---

## 48. Interoperability Product Issues -Summary

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

## 49. NSC-SVC-Addon

**Description**: NSC-SVC-Addon

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

## 50. Review  summary notes  for Feb to May 2024 - Tickets
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

## 51. Review  summary notes for Aug - 2025:

- Most reported tickets are from the Windows platform.
- 40% of issues contributed from the AOAC feature. Currently, QE does not test the Upgrade and Key AOAC functional cases. We need to strengthen the functional cases for AOAC by rewriting the test plan and getting it reviewed with Dev and QE. Next, include monthly regression coverage to identify issues.
- 25% of issues are Day-1 and have been enhanced.

**Description**: Review  summary notes for Aug - 2025:

- Most reported tickets are from the Windows platform.
- 40% of issues contributed from the AOAC feature. Currently, QE does not test the Upgrade and Key AOAC functional cases. We need to strengthen the functional cases for AOAC by rewriting the test plan and getting it reviewed with Dev and QE. Next, include monthly regression coverage to identify issues.
- 25% of issues are Day-1 and have been enhanced.

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

## 52. Review  summary notes for reference:
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

## 53. Review Notes:
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

## 54. Secure Enrollment

**Description**: Secure Enrollment

| Field | Value |
|-------|-------|
| OS Platform | 5.0 |
| Feature | Jithan A N |
| Regression | N/A |
| Bug Type | N/A |
| Automatable | N/A |
| Interop | N/A |
| QE Owner | N/A |
| Source Sheet | Customer Escalations - Overall |

**Test Case Needed**: N/A

---



## --- Added from Excel (not previously in bugs/) ---

## 55. ENG-457109

**Jira**: [ENG-457109](https://netskope.atlassian.net/browse/ENG-457109)

**Description**: Since upgrading to R113 my customer noticed that they are unable to run outer pcaps on NS Client unless they disabled "Protect Client configuration and resources" in Tamperproof set

| Field | Value |
|-------|-------|
| OS Platform | Windows |
| Feature | Self Protection |
| Regression | Yes |
| Bug Type | Missing in Regression |
| Automatable | Yes |
| Interop | No |
| Source Sheet | Customer Escalations - Overall |

**Comments**: - In R113 refactored the nsclient log improvement and it caused this regression.
- Need to add Test case.
- Can be automatable

---
## 56. ENG-493685

**Jira**: [ENG-493685](https://netskope.atlassian.net/browse/ENG-493685)

**Description**: Android NS Client. User required to enter tenant name

| Field | Value |
|-------|-------|
| OS Platform | Android |
| Feature | MDM |
| Regression | No |
| Bug Type | Test Gap |
| Automatable | No |
| Interop | Yes |
| Source Sheet | Customer Escalations - Overall |

**Comments**: - Need to include this case in MDM and add the validation.
- Test Gap scope: Interop test
- Interop: MDM

---
## 57. ENG-529561

**Jira**: [ENG-529561](https://netskope.atlassian.net/browse/ENG-529561)

**Description**: "OTP of given user,device and tenantID is not found, agent needs to request OTP" error on devices UI page for some tenants.

| Field | Value |
|-------|-------|
| OS Platform | Windows |
| Feature | OTP |
| Regression | No |
| Bug Type | Test Gap |
| Automatable | Yes |
| Interop | No |
| Source Sheet | Customer Escalations - Overall |

**Comments**: Add Backend detailed test case as per the QA recommendation.
- Test Gap scope: Negative testing

---
## 58. ENG-647666

**Jira**: [ENG-647666](https://netskope.atlassian.net/browse/ENG-647666)

**Description**: [NSW Police] NPA getting disconnected for all Andriod Users after NSClient OPT Enabled

| Field | Value |
|-------|-------|
| OS Platform | Android |
| Feature | OTP |
| Regression | Yes |
| Bug Type | Corner case |
| Automatable | No |
| Interop | No |
| Source Sheet | Customer Escalations - Overall |

**Comments**: - Regression.
- This issue was caused when both enableSaveBatteryForSleepMode and OTP  FF are enabled.

---
## 59. ENG-729324

**Jira**: [ENG-729324](https://netskope.atlassian.net/browse/ENG-729324)

**Description**: [TD Bank] nsdiag.exe not working with tamperproof enabled after upgrading to 127.1

| Field | Value |
|-------|-------|
| OS Platform | Windows |
| Feature | Self-Protection |
| Regression | No |
| Bug Type | Corner case |
| Automatable | No |
| Interop | Yes |
| Source Sheet | Customer Escalations - Overall |

**Comments**: With Tamper proof enabled, The customer updated from R114 to R127.1.0.2437 & after that, Customer faced this issue of nsdiag hanging on 2 off 3 clients. To further analyze, capturing dumps was tried, but due to tamper proof, it will not allow READ access. As also, nsdiag hanging looks to be an interop issue due to the removal of READ permission with tamper proof enabled. So a flag allowProcessReadPermission was created to access, by which if enabled, READ permission will be granted. Also for any issue analysis, we can now take process dumps also with tamper proof enabled as well.

---
## 60. ENG-768398

**Jira**: [ENG-768398](https://netskope.atlassian.net/browse/ENG-768398)

**Description**: [CLONE] EHF build for EIMF-61 Revert Downloader Security Enhancement

| Field | Value |
|-------|-------|
| OS Platform | Backend |
| Feature | NSC-SVC-Downloader |
| Regression | No |
| Bug Type | Enhancement |
| Automatable | Yes |
| Interop | No |
| Source Sheet | Customer Escalations - Overall |

**Comments**: -An update to downloader API `/dlr/:ostype/get` was made for R131 which requires the presence of an activation key in the downloader URL.
Although this endpoint is internal, some customers were using it and were not properly informed of the update resulting in the security enhancement to the API to impact them. 
-The fix was to revert the changes to /dlr/:ostype/get API which enforce the usage of activation key in request.

---
## 61. ENG-781465

**Jira**: [ENG-781465](https://netskope.atlassian.net/browse/ENG-781465)

**Description**: [vgh.goskope.com] NS client gray out after upgrading NS client from 126 to 129.

| Field | Value |
|-------|-------|
| OS Platform | Windows |
| Feature | NSC-FT-TamperProofing |
| Interop | No |
| Source Sheet | Customer Escalations - Overall |

**Comments**: ProductID in registry can change due to system settings changed, that caused Client not enabled, fix in Client is able to the change, and keep Client enabled.

---
## 62. ENG-792144

**Jira**: [ENG-792144](https://netskope.atlassian.net/browse/ENG-792144)

**Description**: Adding more than one iOS link to email invite template leads to invalid App Store link

| Field | Value |
|-------|-------|
| OS Platform | iOS |
| Feature | iOS- Backend |
| Regression | Day-1 |
| Bug Type | Corner Case |
| Automatable | yes |
| Interop | No |
| Source Sheet | Customer Escalations - Overall |

**Comments**: Normal email invitations are working. This issue arises when a customer creates an email template with two instances of the variable `{i{NS_IOSCLIENT}}` and sends a new email invitation.

---
## 63. ENG-832690

**Jira**: [ENG-832690](https://netskope.atlassian.net/browse/ENG-832690)

**Description**: [Nintendo] Disable Internet Security by OTP not working on MAC

| Field | Value |
|-------|-------|
| OS Platform | Mac |
| Feature | OTP |
| Regression | Yes |
| Bug Type | Missing in Regressions |
| Automatable | Yes |
| Interop | No |
| Source Sheet | Customer Escalations - Overall |

**Comments**: NPLAN-5196 feature code merge removed some existing code causing OTP and Master password feature to break
 Missing in Regression

---
