# Client Status / UI / Logging Bugs

Bugs related to client status reporting, device visibility, client UI, notifications, log collection, and backend service issues.

> Source: Escalation Bug Review spreadsheet, filtered by keywords: client status, device page, notifications, log collection, UI, backend services.

**Total: 19 bugs**

---

## 1. ENG-392768

**Jira**: [ENG-392768](https://netskope.atlassian.net/browse/ENG-392768)

**Description**: Refine Device Posture Change event and Customer issue(ENG-489089)

| Field | Value |
|-------|-------|
| OS Platform | Windows |
| Feature | Client Status - with Device Classification |
| Regression | Yes |
| Bug Type | Test Gap |
| Automatable | Yes - Need to automate |
| Interop | No |
| Source Sheet | Customer Escalations - Overall |

**Comments**: - Looks like monthly regression was not executed for this case.
- Include it in Automation.
- Improve Decice Classification coverage with Client status.
- Test Gap scope: Negative testing

---
## 2. ENG-418774

**Jira**: [ENG-418774](https://netskope.atlassian.net/browse/ENG-418774)

**Description**: Device is not visible on the Devices page on the Netskope portal

| Field | Value |
|-------|-------|
| OS Platform | Windows & Mac |
| Feature | NSC-SVC-Client status |
| Regression | No |
| Bug Type | Internal found |
| Automatable | Yes |
| Interop | No |
| Source Sheet | Customer Escalations - Overall |

**Comments**: - INternal defect (ENG-408293)
- Need to add this special case in test rail and aurtomate it
- Test Gap scope - feature coverage (Client status-Backend)

---
## 3. ENG-428536

**Jira**: [ENG-428536](https://netskope.atlassian.net/browse/ENG-428536)

**Description**: Devices missing from Tenant || Teknor Apex Company
https://netskope.atlassian.net/browse/ENG-428794 - Same area

| Field | Value |
|-------|-------|
| OS Platform | Windows |
| Feature | Client Status |
| Regression | Yes |
| Bug Type | Test Gap |
| Automatable | No |
| Interop | No |
| Source Sheet | Customer Escalations - Overall |

**Comments**: - There are many fixes in this device enrty for nsdeviceuid and old_nsdeviceuid.Hope this is already taken case in both Backend and E2E testing.
- Test Gap scope: Negative testing

---
## 4. ENG-469289

**Jira**: [ENG-469289](https://netskope.atlassian.net/browse/ENG-469289)

**Description**: [Jones Lang Lasalle] No Client user notification pop up due to absence of longpoll connection

| Field | Value |
|-------|-------|
| OS Platform | Windows |
| Feature | Client Notification |
| Regression | No |
| Bug Type | Corner case (Need improvemenr on Long poll connection feature) |
| Automatable | No |
| Interop | No |
| Source Sheet | Customer Escalations - Overall |

**Comments**: Check if automation is possible.
-= Alert/block Notification issue due to longpoll connection not triggered.

---
## 5. ENG-504528

**Jira**: [ENG-504528](https://netskope.atlassian.net/browse/ENG-504528)

**Description**: [Bosch]Client logs download failed - "failed to download client logs" - The specified key does not exist

| Field | Value |
|-------|-------|
| OS Platform | Windows |
| Feature | Logging |
| Regression | No |
| Bug Type | Corner case |
| Automatable | Yes |
| Interop | No |
| Source Sheet | Customer Escalations - Overall |

**Comments**: - Need to add test case.
- Cn be automatable.

---
## 6. ENG-564408

**Jira**: [ENG-564408](https://netskope.atlassian.net/browse/ENG-564408)

**Description**: [ Lucid Motors ] Mac address not being displayed for some machines in the Devices page ...

| Field | Value |
|-------|-------|
| OS Platform | Mac |
| Feature | Client Status |
| Regression | No |
| Bug Type | Corner case (Issue is seen when client fails to send the mac Address and not easy to reproduce) |
| Automatable | No |
| Interop | No |
| Source Sheet | Customer Escalations - Overall |

**Comments**: - Already added the test case. No action needed

---
## 7. ENG-594892

**Jira**: [ENG-594892](https://netskope.atlassian.net/browse/ENG-594892)

**Description**: Failed to download client logs from UI

| Field | Value |
|-------|-------|
| OS Platform | Client Services (Backend) |
| Feature | NSC-SVC-Pycore |
| Regression | Yes |
| Bug Type | Test Gap |
| Automatable | Yes |
| Interop | No |
| Source Sheet | Customer Escalations - Overall |

**Comments**: - Need to add scenario to include Uppercase/Lowercase every keyname for cloud storage platform.
- Update the test case to include the lower case,upper case and with mixerd combination and add the same in automation - https://netskope.testrail.io/index.php?/cases/view/1541958&group_by=cases:section_id&group_order=asc&display_deleted_cases=0&group_id=106112
- Test Gap scope: Need-Additional Coverage

---
## 8. ENG-622617

**Jira**: [ENG-622617](https://netskope.atlassian.net/browse/ENG-622617)

**Description**: Bulk Client Enable via Admin UI Does Not Reflect on All Devices — Only Manual Enable

| Field | Value |
|-------|-------|
| OS Platform | Client Services (Backend) |
| Feature | NSC-SVC-Pycore |
| Regression | Yes |
| Bug Type | Test Gap (Backend Cache clearing case and provisioner integration) |
| Automatable | Yes |
| Interop | No |
| Source Sheet | Customer Escalations - Overall |

**Comments**: - Need to automate this case.
- Issue is due to backend cache clearing gap and in was introduced due to a change in provisioner side.
- Make sure to have a test case with E2E to cover Bulk Enable/Disable client from Tenant Web UI.
- Test Gap scope: Need-Additional Coverage

---
## 9. ENG-626799

**Jira**: [ENG-626799](https://netskope.atlassian.net/browse/ENG-626799)

**Description**: -NSC send clientstatus, but don't see event on Device apge

| Field | Value |
|-------|-------|
| OS Platform |  |
| Feature |  |
| Source Sheet | Internal Bugs |

**Comments**: Looks to be a stack specific issue.

---
## 10. ENG-630626

**Jira**: [ENG-630626](https://netskope.atlassian.net/browse/ENG-630626)

**Description**: Unable to Download Client Logs - Decryption Failure (AttributeError: 'File_Decrypt' object has no attribute 'backup_pubkey')

| Field | Value |
|-------|-------|
| OS Platform | Windows,Mac |
| Feature | Logging |
| Regression | Yes |
| Bug Type | Test Gap |
| Automatable | Yes |
| Interop | No |
| Source Sheet | Customer Escalations - Overall |

**Comments**: The issue happens when both the encryption configuration flag and per-user mode are enabled.
- We need to have test case without FF and enable the FF to verify the functionality.
- Test Gap scope: Need-Additional Coverage

---
## 11. ENG-651043

**Jira**: [ENG-651043](https://netskope.atlassian.net/browse/ENG-651043)

**Description**: [Jio] ChromeOS - MAC and Serial number details are not captured by client

| Field | Value |
|-------|-------|
| OS Platform | Android |
| Feature | Client Status |
| Regression | Day-1 |
| Bug Type | Test Gap |
| Automatable | Yes |
| Interop | No |
| Source Sheet | Customer Escalations - Overall |

**Comments**: - Day-1 issue and this was reproduced even in R112(! year old build)
- Test Gap scope- Day-1 issue

---
## 12. ENG-684014

**Jira**: [ENG-684014](https://netskope.atlassian.net/browse/ENG-684014)

**Description**: Netskope client status to follow the IDP user status

| Field | Value |
|-------|-------|
| OS Platform | NSC-SVC-Pycore |
| Feature | Client Status |
| Regression | Yes |
| Bug Type | Test-gap |
| Automatable | Yes |
| Interop | No |
| Source Sheet | Customer Escalations - Overall |

**Comments**: The behaviour should be same once start using mongo
We will revert the logic to “Before R125“ with replacing the direct mongo query with UM users API call, and adding a default on feature flag disable_nsclient_when_mongo_user_disabled. If there are few customers hoping to keep their NSClients enabled while users get disabled, they can request to turn off the flag.
- Looks like the Change implemented in R125 is broken and it was decided to revert back
- I see the test rail link in the ticket points to the entire suite, Not sure this needs full test coverage, But it should be better to cover the test QE recommednation from Dev.
- Test Gap: Need-Additional Coverage

---
## 13. ENG-686265

**Jira**: [ENG-686265](https://netskope.atlassian.net/browse/ENG-686265)

**Description**: Post R127 getting error "Cannot find any matched client configuration" post on Devices page due to incorrect client config name in the API

| Field | Value |
|-------|-------|
| OS Platform | Windows |
| Feature | Client Status |
| Regression | No |
| Bug Type | Corner case |
| Automatable | Yes |
| Interop | No |
| Source Sheet | Customer Escalations - Overall |

**Comments**: - The issue was caused by a missing space between the dash and ""Corporate"" in the client configuration name.
- The client configuration name in the backend table did not match the client config sent by the WebUI API and client status message because of a spacing issue.
- The issue has been fixed in client, and now handles spaces in configuration names correctly.
- Corner case.

---
## 14. ENG-769147

**Jira**: [ENG-769147](https://netskope.atlassian.net/browse/ENG-769147)

**Description**: [Clone] FR4 - [ACPL Systems Pvt. Ltd] - Customer is trying to disable Clients from tenant UI, we can see request submitted but NSclient does not download the supportability params to update

| Field | Value |
|-------|-------|
| OS Platform | Backend |
| Feature | NSC-SVC-Clientservices |
| Regression | No |
| Bug Type | Corner Case |
| Automatable | Yes |
| Interop | No |
| Source Sheet | Customer Escalations - Overall |

**Comments**: https://docs.google.com/document/d/1J6U1B7yCZaNq5lvxfnj_d3JDJr7meAlxioxb2GbRRrM/edit?tab=t.0

---
## 15. ENG-781045

**Jira**: [ENG-781045](https://netskope.atlassian.net/browse/ENG-781045)

**Description**: Netskope Notification Templates HTML % encoding issue duplicates the last 7 characters of the message body

| Field | Value |
|-------|-------|
| OS Platform | Windows |
| Feature | NSC-FT-Notification |
| Interop | No |
| Source Sheet | Customer Escalations - Overall |

**Comments**: - Not a client team owned scenario.
-The issue has been verified by Prashant Kumar Pathak

---
## 16. ENG-857166

**Jira**: [ENG-857166](https://netskope.atlassian.net/browse/ENG-857166)

**Description**: [SARPI Veolia] Netskope client v133 freezing on ChromeOS 138.

| Field | Value |
|-------|-------|
| OS Platform | ChromeOS |
| Feature | Client Crash |
| Regression | Day-1 |
| Bug Type | Enhacement |
| Automatable | Yes |
| Interop | No |
| Source Sheet | Customer Escalations - Overall |

**Comments**: NS Client app crashes on ChromeOS 138 as it doesn't have x86_64 native support.

---
## 17. ENG-880058

**Jira**: [ENG-880058](https://netskope.atlassian.net/browse/ENG-880058)

**Description**: [IndMoney] MAC Client disabling frequently and enables only after reboot

| Field | Value |
|-------|-------|
| OS Platform | Mac |
| Feature | Mac proxy / NE component |
| Regression | Day-1 |
| Bug Type | Corner Case |
| Interop | No |
| Source Sheet | Customer Escalations - Overall |

**Comments**: This issue was consistently reproducible on the Dev setup only. Although the same steps were followed on other environments (MAC M5, Intel Core, Parallels VM), the termination behavior was not observed, as it is environment-specific.

As per the root-cause description, the issue should occur during sleep-wake cycles with macOS AO (Always On) support and VIF mode enabled. However, even after multiple attempts, we were unable to reproduce the actual issue organically; therefore, we simulated the failure by explicitly sending a SIGPIPE signal to the Netskope proxy service.

---
## 18. ENG-932854

**Jira**: [ENG-932854](https://netskope.atlassian.net/browse/ENG-932854)

**Description**: CLONE - [Jones Lang Lasalle Inc] Log bundle is missing nsdebuglog.1.log file while saving logs

| Field | Value |
|-------|-------|
| OS Platform | Windows |
| Feature | Logging |
| Regression | Day 1 |
| Bug Type | Corner Case |
| Automatable | No |
| Source Sheet | Customer Escalations - Overall |

**Comments**: Hard to reproduce in the right timing (collecting log at the log rotation time)

---
## 19. ENG-954726

**Jira**: [ENG-954726](https://netskope.atlassian.net/browse/ENG-954726)

**Description**: [CLONE] Admin gets emails every 5 minutes about client log collection status

| Field | Value |
|-------|-------|
| OS Platform | All |
| Feature | Logging |
| Source Sheet | Customer Escalations - Overall |

---
