# Device Classification Bugs

Bugs related to Device Classification rules, AV checks, UPN/cert-based classification, BitLocker checks, and Device Posture.

> Source: Escalation Bug Review spreadsheet, filtered by keywords: device classification, AV check, UPN, cert check, BitLocker, device posture, smart card.

**Total: 13 bugs**

---

## 1. ENG-425999

**Jira**: [ENG-425999](https://netskope.atlassian.net/browse/ENG-425999)

**Description**: UPN and Email change : After changing the UPN and email, client UI shows the old email

| Field | Value |
|-------|-------|
| OS Platform | Windows |
| Feature | UPN |
| Regression | Yes |
| Bug Type | Missing in Regression(Broken by ENG-355696) |
| Automatable | No |
| Interop | No |
| Source Sheet | Customer Escalations - Overall |

**Comments**: - Regression Issue - Broken by ENG-355696)
- Need to add test case in Test rail
- Must include it in Monthly regression.

---
## 2. ENG-501419

**Jira**: [ENG-501419](https://netskope.atlassian.net/browse/ENG-501419)

**Description**: [Embecta] Custom Device Classification Status not retrieved on NS Client - VDI machines

| Field | Value |
|-------|-------|
| OS Platform | Windows |
| Feature | Device Classification |
| Regression | No |
| Bug Type | Missing in Regression |
| Automatable | Yes |
| Interop | No |
| Source Sheet | Customer Escalations - Overall |

**Comments**: - Custom Device Classification is delivered to Device page and Real-Time policy correctly. Only Client UI is not notified by NSClient correctly. There is limited impact on the endpoint
- Cover it in monthly regression

---
## 3. ENG-553715

**Jira**: [ENG-553715](https://netskope.atlassian.net/browse/ENG-553715)

**Description**: [ Device Classification ] AV Checks Failing with error code 0x80070426

| Field | Value |
|-------|-------|
| OS Platform | Windows |
| Feature | Device Classification |
| Regression | No |
| Bug Type | Test Gap(This fix caused an regression ENG-571382 reported by QA and it is fixed. |
| Automatable | No |
| Interop | No |
| Source Sheet | Customer Escalations - Overall |

**Comments**: - Add test case
- Can be automatable
- Test Gap scope: Negative testing
Interop: AV- CrowdStrike

---
## 4. ENG-606802

**Jira**: [ENG-606802](https://netskope.atlassian.net/browse/ENG-606802)

**Description**: Smart Card PIN check DC not working as expected

| Field | Value |
|-------|-------|
| OS Platform | NSC-SVC-Device-Classification |
| Feature | Device Classification |
| Source Sheet | Q226 Feb |

---
## 5. ENG-618817

**Jira**: [ENG-618817](https://netskope.atlassian.net/browse/ENG-618817)

**Description**: device-classification in pending state on MEL2

| Field | Value |
|-------|-------|
| OS Platform |  |
| Feature |  |
| Source Sheet | Internal Bugs |

**Comments**: It is specific to Mel2 DC and thr action item on the PE team to increase/scale the PO count for DC

---
## 6. ENG-649419

**Jira**: [ENG-649419](https://netskope.atlassian.net/browse/ENG-649419)

**Description**: Bitlocket DC rule is not working intermittently

| Field | Value |
|-------|-------|
| OS Platform | Windows |
| Feature | Device Classification |
| Regression | No |
| Bug Type | Corner case |
| Automatable | No |
| Interop | No |
| Source Sheet | Customer Escalations - Overall |

**Comments**: - This is a corrner case and it happens randomly without any specific pattern.
- But this one needs coverage in Device classifiication.
- Negative testing.

---
## 7. ENG-658568

**Jira**: [ENG-658568](https://netskope.atlassian.net/browse/ENG-658568)

**Description**: Crit POV - WebUI - Device Classification Rule for Windows with Registry would not allow to set REG_DWORD with value 0

| Field | Value |
|-------|-------|
| OS Platform | NSC-SVC-Device-Classification (Backend) |
| Feature | Device Classification |
| Regression | No |
| Bug Type | Test Gap |
| Automatable | Yes |
| Interop | No |
| Source Sheet | Customer Escalations - Overall |

**Comments**: -  Web UI to backend update failure.
- Need to make sure the all the fields in Device Classification Web UI to Backend API CRED function works fine.
- Test Gap scope: Need-Additional Coverage

---
## 8. ENG-728913

**Jira**: [ENG-728913](https://netskope.atlassian.net/browse/ENG-728913)

**Description**: ENG-728913 CLONE - [fortescue] Cert Check + UPN Device Classification failing on MAC

| Field | Value |
|-------|-------|
| OS Platform | Mac |
| Feature | Check UPN |
| Regression | Day-1 |
| Bug Type | Corner case |
| Automatable | No |
| Interop | No |
| Source Sheet | Customer Escalations - Overall |

**Comments**: - This is a Day-1 issue.
-  This ticket is still being worked by the Dev Eng and not yet complete.

---
## 9. ENG-798635

**Jira**: [ENG-798635](https://netskope.atlassian.net/browse/ENG-798635)

**Description**: [The Chugoku Electric Power Company Inc] Device classification status is downloaded every second

| Field | Value |
|-------|-------|
| OS Platform | Windows |
| Feature | NSC-FT-DeviceClassification |
| Regression | Day-1 |
| Bug Type | Enhancement |
| Automatable | No |
| Interop | No |
| Source Sheet | Customer Escalations - Overall |

**Comments**: The symptom of this issue is frequent Device Classification checks. It only occurs when users frequently plug and unplug the smart card. We disabled the smart card check when the Check Smart Card setting is not enabled.

---
## 10. ENG-824383

**Jira**: [ENG-824383](https://netskope.atlassian.net/browse/ENG-824383)

**Description**: Smart Card PIN check DC not working as expected- Continuation of ENG-603548

| Field | Value |
|-------|-------|
| OS Platform | Windows |
| Feature | NSC-FT-DeviceClassification |
| Regression | No |
| Bug Type | Corner Case |
| Automatable | No |
| Interop | No |
| Source Sheet | Customer Escalations - Overall |

**Comments**: The vendor issuing smart cards for customers updated their custom minidriver, causing third-party software like NSClient to be unable to access the smart card cert store directly through the Windows API. We resolved the issue by added an alternative approach: when the cert store is inaccessible, it falls back to accessing the cache to retrieve the certificate.

---
## 11. ENG-824828

**Jira**: [ENG-824828](https://netskope.atlassian.net/browse/ENG-824828)

**Description**: [Wistron] Device Classification AV check failing

| Field | Value |
|-------|-------|
| OS Platform | Windows |
| Feature | NSC-FT-DeviceClassification |
| Regression | No |
| Bug Type | Corner Case |
| Automatable | No |
| Source Sheet | Customer Escalations - Overall |

**Comments**: The issue is relat to custom AV where some specific AV like Trend Micro Apex one antivirus was not detected. We validate with Trend Micro where Trend Micro Apex one antivirus is completely different than what we used

---
## 12. ENG-841829

**Jira**: [ENG-841829](https://netskope.atlassian.net/browse/ENG-841829)

**Description**: [Southcoast Health System] DC rule AV not working

| Field | Value |
|-------|-------|
| OS Platform | Windows |
| Feature | NSC-FT-DeviceClassification |
| Regression | Yes |
| Bug Type | Corner Case |
| Automatable | No |
| Source Sheet | Customer Escalations - Overall |

**Comments**: The issue observed specifically with Custom AV Cortex XDR™ Advanced Endpoint Protection where the Upper TM was not able to match the string. The Test cases has been added to verfiy the Upper/Lower cap which appears as in AV
Corner Case

---
## 13. ENG-894015

**Jira**: [ENG-894015](https://netskope.atlassian.net/browse/ENG-894015)

**Description**: CLONE - [Clinisys] BWAN client shows device as Unmanaged, while NS Client detected as managed

| Field | Value |
|-------|-------|
| OS Platform | Windows |
| Feature | NSC-FT-DeviceClassification |
| Regression | Day-1 |
| Bug Type | Test Gap |
| Automatable | Yes |
| Interop | No |
| Source Sheet | Customer Escalations - Overall |

**Comments**: The Client validation done without BWAN configuration. This one  is part of integration testing and need to be added as part of Client  testing 
- Test Gap scope: Negative/Resilience (missing resilience scenario on DC download failure and nsuser.conf cache handling)
- Integration- BWAN

---
