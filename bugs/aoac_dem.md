# AOAC / DEM Bugs

Bugs related to Always On Always Connected (AOAC), Digital Experience Monitoring (DEM), device health monitoring, and sleep/wake behavior.

> Source: Escalation Bug Review spreadsheet, filtered by keywords: AOAC, DEM, sleep, wake, modern standby, device health, network events, performance monitoring.

**Total: 20 bugs**

---

## 1. ENG-421796

**Jira**: [ENG-421796](https://netskope.atlassian.net/browse/ENG-421796)

**Description**: Mac computers getting failed Disk consumption metrics

| Field | Value |
|-------|-------|
| OS Platform | Mac |
| Feature | DEM |
| Regression | Day-1 |
| Bug Type | Test Gap |
| Automatable | Yes |
| Interop | No |
| Source Sheet | Customer Escalations - Overall |

**Comments**: - Regression (This was  already tagged as regression on the cloned bug) But looks like the issue exisit from day-1.
- Test case is not mapped in the ticket. Need t check if QE has added the test case.
- Test Gap scope:  Integration test

---
## 2. ENG-424865

**Jira**: [ENG-424865](https://netskope.atlassian.net/browse/ENG-424865)

**Description**: [HubSpot] NSCOM connection broken multiple times - Causing outages on macOS devices

| Field | Value |
|-------|-------|
| OS Platform | Mac |
| Feature | DEM |
| Regression | Yes |
| Bug Type | Corner case |
| Automatable | Yes |
| Interop | Yes |
| Source Sheet | Customer Escalations - Overall |

**Comments**: - Regression issue.
- Clone bug doesn't include the test case in testrail
- Need to add it in Monthly regression.
---------------------------------------------------------------------------
comment from Dev engineer

We are avoiding a race condition.
Network watcher thread pushes new interfaces in a vector while the subsample thread is iterating over it.
After the fix:
New network that came up would be maintained in a separate vector and subsample thread will pick those in the next iteration!
-------------------------------------------
comment from QA engineer
Fix made to avoid the race condition, Existing automation covers that client is always recieving the network informaiton in metrics.json

---
## 3. ENG-429064

**Jira**: [ENG-429064](https://netskope.atlassian.net/browse/ENG-429064)

**Description**: Nsclient - Client not posting Client status after enabling DEM

| Field | Value |
|-------|-------|
| OS Platform | Windows |
| Feature | DEM |
| Regression | Day-1 |
| Bug Type | Test Gap |
| Automatable | No |
| Interop | No |
| Source Sheet | Customer Escalations - Overall |

**Comments**: - Day 1 issue
- Need to include in the manual regression.
- Test Gap Scope: Day-1 Issue
- Integration: DEM

---
## 4. ENG-431642

**Jira**: [ENG-431642](https://netskope.atlassian.net/browse/ENG-431642)

**Description**: [Deloitte] Route control enabled in client without backend flags being enabled

| Field | Value |
|-------|-------|
| OS Platform | Windows |
| Feature | DEM |
| Regression | Day-1 |
| Bug Type | Enhancement |
| Automatable | No |
| Interop | No |
| Source Sheet | Customer Escalations - Overall |

**Comments**: - Need to move this to respective testrail folder.
- Add this as part of Monthly regression.
- Include this for automation.
-There is a tag “DEM” attached to the Route Control related logs due to Polaris Route Control and irt caused the confusion
- Integration: DEM

---
## 5. ENG-483200

**Jira**: [ENG-483200](https://netskope.atlassian.net/browse/ENG-483200)

**Description**: [Windows] Frequent network events in the log when DEM device health is enabled and a crash seen at time

| Field | Value |
|-------|-------|
| OS Platform | Windows & Mac |
| Feature | DEM |
| Regression | Yes |
| Bug Type | Corner case |
| Automatable | Yes |
| Interop | No |
| Source Sheet | Customer Escalations - Overall |

**Comments**: - Need to add this case.
------------------------------------
Comments from dev
This is a synchronization issue in the network event
------------------------------------
Comment from QA
This can't be reproduce
Existing automation considered for this case

---
## 6. ENG-549966

**Jira**: [ENG-549966](https://netskope.atlassian.net/browse/ENG-549966)

**Description**: [hubspot]Ns client crash for Mac OS.

| Field | Value |
|-------|-------|
| OS Platform | Mac |
| Feature | DEM |
| Regression | No |
| Bug Type | Corner case |
| Automatable | No |
| Interop | No |
| Source Sheet | Customer Escalations - Overall |

**Comments**: - review the DEM Device Health metric Test plan has Network switch cases.
-----------------------------------------------------
comment from QA
Added a testcases for the network interface connect/disconnect events.
-Not easily reproducible

---
## 7. ENG-561138

**Jira**: [ENG-561138](https://netskope.atlassian.net/browse/ENG-561138)

**Description**: [Delta Dental of California] AOAC cached status sequence issue

| Field | Value |
|-------|-------|
| OS Platform | Windows |
| Feature | AOAC |
| Regression | No |
| Bug Type | (Need to improve the test coverage on AOAC)
Corner case |
| Automatable | No |
| Interop | Yes |
| Source Sheet | Customer Escalations - Overall |

**Comments**: - Create and update this case in AOAC test plan
- Test Gap scope: Negative testing
- Interop Scope: AV-CrowdStrike

---
## 8. ENG-561570

**Jira**: [ENG-561570](https://netskope.atlassian.net/browse/ENG-561570)

**Description**: [NSClient Windows] Sometimes the NSC service is not able to be restarted in Modern Standby mode

| Field | Value |
|-------|-------|
| OS Platform | Windows |
| Feature | AOAC |
| Regression | No |
| Bug Type | Corner case. |
| Automatable | No |
| Interop | No |
| Source Sheet | Customer Escalations - Overall |

**Comments**: - Create and update this case in AOAC test plan

---
## 9. ENG-669888

**Jira**: [ENG-669888](https://netskope.atlassian.net/browse/ENG-669888)

**Description**: [POV/DEM Enterprise] wireless strength is always shown as 0 in DEM UI

| Field | Value |
|-------|-------|
| OS Platform | Windows |
| Feature | DEM |
| Regression | No |
| Bug Type | Corner case. |
| Automatable | No |
| Interop | No |
| Source Sheet | Customer Escalations - Overall |

**Comments**: -windows API WlanGetNetworkBssList to get the available wifi list,If the wifi network is hidden, then there are chances that it will not be enumerated by this API.
- Fix is to use the parameter value ""pconnAttributes"" from existing winAPI call WlanQueryInterface() to read the signal stregth of connected wifi.

- Test cases added in the bug is pointing to DEM health metrics first  test case. Probably the scenario(Hidden wifi/Location service On/off) case needs to be included in the test case.
- Corner case.

---
## 10. ENG-683548

**Jira**: [ENG-683548](https://netskope.atlassian.net/browse/ENG-683548)

**Description**: Customer seeing more users than monitored

| Field | Value |
|-------|-------|
| OS Platform | Windows, Mac |
| Feature | DEM |
| Regression | No |
| Bug Type | Corner case |
| Automatable | No |
| Interop | No |
| Source Sheet | Customer Escalations - Overall |

**Comments**: The issue was caused by using wrong feature flag as DEM service status. the issue has been fixed in client and validated.

---
## 11. ENG-726488

**Jira**: [ENG-726488](https://netskope.atlassian.net/browse/ENG-726488)

**Description**: Deloitte Client version 128.2 not showing client user justifications POP ups

| Field | Value |
|-------|-------|
| OS Platform | Windows |
| Feature | AOAC |
| Regression | Yes |
| Bug Type | Test Gap |
| Automatable | No |
| Interop | No |
| Source Sheet | Customer Escalations - Overall |

**Comments**: - The issue has been ocurrs for AOAC devices when user came up from sleep - post enable the flag enable_aoac_by_prelogon found working

---
## 12. ENG-726602

**Jira**: [ENG-726602](https://netskope.atlassian.net/browse/ENG-726602)

**Description**: [JLL] Client disabled due to error when the device is waking from sleep/modern standby mode

| Field | Value |
|-------|-------|
| OS Platform | Windows |
| Feature | AOAC |
| Regression | Yes |
| Bug Type | Test Gap |
| Automatable | No |
| Interop | No |
| Source Sheet | Customer Escalations - Overall |

**Comments**: - The issue has been ocurrs for AOAC devices when device come up from sleep/modern standby

---
## 13. ENG-748332

**Jira**: [ENG-748332](https://netskope.atlassian.net/browse/ENG-748332)

**Description**: Client status is missing from Aug 22nd to Aug 26th for a device under settings > Security Cloud Platform > Netskope Client > Devices

| Field | Value |
|-------|-------|
| OS Platform | Windows & Mac |
| Feature | DEM |
| Regression | No |
| Bug Type | Enhancement |
| Automatable | No |
| Interop | No |
| Source Sheet | Customer Escalations - Overall |

**Comments**: This change enhances the existing code to prevent disabling the enableDemClientStatus flag from the Ursa configuration.
The client team is currently working on an enhancement to retire the legacy client status workflow and fully transition to the DEM client status flow. As part of this initiative, the backend has already begun consuming data from the DEM client status flow.

In this particular case, the customer likely requested to disable the enableDemClientStatus flag. However, since the backend continues to expect data from the DEM client status flow instead of the legacy one, the client status information was missing during that period.

---
## 14. ENG-754190

**Jira**: [ENG-754190](https://netskope.atlassian.net/browse/ENG-754190)

**Description**: [Elite Group Holding] Netskope client disconnects frequently for multiple users- see one service crash

| Field | Value |
|-------|-------|
| OS Platform | Windows |
| Feature | AOAC |
| Regression | No |
| Bug Type | Test Gap |
| Automatable | No |
| Interop | No |
| Source Sheet | Customer Escalations - Overall |

**Comments**: The issue associated wth AOAC devices which has been resolved. This was happening because of service crash only happen after power up/wake up from AOAC standby on Windows machine

---
## 15. ENG-766069

**Jira**: [ENG-766069](https://netskope.atlassian.net/browse/ENG-766069)

**Description**: [Elite Group Holding] Netskope client disconnects frequently for multiple users- write pkt thread error

| Field | Value |
|-------|-------|
| OS Platform | Windows |
| Feature | AOAC |
| Regression | Day-1 |
| Bug Type | Test Gap |
| Automatable | No |
| Interop | No |
| Source Sheet | Customer Escalations - Overall |

**Comments**: The issue was not able to test due to limited scope of testing with AOAC device - The issue has been fixed by adding code to check null pointer before use

---
## 16. ENG-783149

**Jira**: [ENG-783149](https://netskope.atlassian.net/browse/ENG-783149)

**Description**: [Elite Group Holding] Netskope client disconnects frequently for multiple users

| Field | Value |
|-------|-------|
| OS Platform | Windows |
| Feature | AOAC |
| Regression | Day-1 |
| Bug Type | Test Gap |
| Automatable | No |
| Interop | No |
| Source Sheet | Customer Escalations - Overall |

**Comments**: The issue was not able to test due to limited scope of testing with AOAC device - The issue has been fixed by adding code to check null pointer before use

---
## 17. ENG-789126

**Jira**: [ENG-789126](https://netskope.atlassian.net/browse/ENG-789126)

**Description**: [PDEM Professional] Network and Device events are missing for some users

| Field | Value |
|-------|-------|
| OS Platform | Windows & Mac |
| Feature | DEM |
| Regression | Day-1 |
| Bug Type | Enhancement |
| Automatable | No |
| Interop | No |
| Source Sheet | Customer Escalations - Overall |

**Comments**: Enhancement based on customer feedback upon cancelling the sampling. Now client will dump the information into the matrics.json.

---
## 18. ENG-802476

**Jira**: [ENG-802476](https://netskope.atlassian.net/browse/ENG-802476)

**Description**: Network Throughput Metrics Missing in tenant UI

| Field | Value |
|-------|-------|
| OS Platform | Windows |
| Feature | DEM |
| Regression | Day-1 |
| Bug Type | Test Gap |
| Automatable | Yes |
| Interop | No |
| Source Sheet | Customer Escalations - Overall |

**Comments**: NSclient adds nw throughput counters in English language.But  when using non-english ISOe(e.g.french), the counter name differed. This caused failure while adding the counters and nw throughput was not collected. Need to Include Localization test for DEM.

Test Gap Scope   Need Additional coverage

---
## 19. ENG-830275

**Jira**: [ENG-830275](https://netskope.atlassian.net/browse/ENG-830275)

**Description**: [CLONED][Elite Group Holding] Netskope client disconnects frequently for multiple users

| Field | Value |
|-------|-------|
| OS Platform | Windows |
| Feature | AOAC |
| Regression | No |
| Bug Type | Test Gap |
| Automatable | No |
| Source Sheet | Customer Escalations - Overall |

**Comments**: The issue found with AOAC device when wakeup from sleep. The validation done with various options from UI.
- Test Gap scope: Need-Additional Coverage

---
## 20. ENG-848014

**Jira**: [ENG-848014](https://netskope.atlassian.net/browse/ENG-848014)

**Description**: [DEM Enterprise] Site to POP connection time is high in Performance graph but could not track those high values in

| Field | Value |
|-------|-------|
| OS Platform | Windows & Mac |
| Feature | DEM Integration |
| Regression | Day-1 |
| Bug Type | Enhancement |
| Automatable | Yes |
| Interop | No |
| Source Sheet | Customer Escalations - Overall |

**Comments**: Some of the App probe stats are reported Negative values due to issues in the code. The fix addresses the issue by using curl API return code before using the delay calculated by the API.

---
