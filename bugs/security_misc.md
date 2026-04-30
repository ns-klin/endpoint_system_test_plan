# Security / PKI / Config Encryption Bugs

Bugs related to PKI certificate management, PSIRT security issues, config encryption, and other security-related client issues.

> Source: Escalation Bug Review spreadsheet, filtered by keywords: PKI, PSIRT, certificate, config encryption, security, MITM, tamperproof.

**Total: 8 bugs**

---

## 1. ENG-499787

**Jira**: [ENG-499787](https://netskope.atlassian.net/browse/ENG-499787)

**Description**: macOS nsclient pop up authentication dialog in CA rotation

| Field | Value |
|-------|-------|
| OS Platform | Mac |
| Feature | Cert Rotation |
| Regression | Yes |
| Bug Type | Missing in Regressions |
| Automatable | No |
| Interop | No |
| Source Sheet | Customer Escalations - Overall |

**Comments**: - AM2 cert rotation fix - If the CA is expired, the trust checked will fail. Fix is If the trust check failure is due to the expired CA, don’t try to set trust
- Need to include this case on every cert rotatrion changes.
- Test case exists in test plan but this was not executed due to test bed lag and End phase stage should have covered this case.

---
## 2. ENG-538206

**Jira**: [ENG-538206](https://netskope.atlassian.net/browse/ENG-538206)

**Description**: NS Client crashes in MacOS

| Field | Value |
|-------|-------|
| OS Platform | Mac |
| Feature | Unicode |
| Regression | No |
| Bug Type | Corner case |
| Automatable | No |
| Interop | No |
| Source Sheet | Customer Escalations - Overall |

**Comments**: - Need to add test case for Unicode. may be a test suite is needed for Unicode support for NWSclient.
- Issue is specific to appllications which use the Multibype/Unicode process names. This is a corner case
-----------------------------------
comment from QA
This is a corner case, To simulate this we need a multibyte character language application 
Will add the testcase but the test case will have dependency on the multibyte third party application
Handling invalid UTF-8 sequences
- Test Gap scope: Negative testing

---
## 3. ENG-619728

**Jira**: [ENG-619728](https://netskope.atlassian.net/browse/ENG-619728)

**Description**: Open Redirect leading to Man-in-the-Middle Attack

| Field | Value |
|-------|-------|
| OS Platform |  |
| Feature |  |
| Source Sheet | Internal Bugs |

**Comments**: Security bug and the earlier fix is not working and it's re-opened. This is a must fix

---
## 4. ENG-785573

**Jira**: [ENG-785573](https://netskope.atlassian.net/browse/ENG-785573)

**Description**: PSIRT: Shared trusted root cert among MPs allows MITM on Netskope tenant user (windows)

| Field | Value |
|-------|-------|
| OS Platform | Windows |
| Feature | PKI |
| Regression | No |
| Bug Type | Enhancement |
| Automatable | Yes |
| Interop | No |
| Source Sheet | Customer Escalations - Overall |

**Comments**: Security Enhancement

---
## 5. ENG-785574

**Jira**: [ENG-785574](https://netskope.atlassian.net/browse/ENG-785574)

**Description**: PSIRT: Shared trusted root cert among MPs allows MITM on Netskope tenant user (Mac)

| Field | Value |
|-------|-------|
| OS Platform | Mac |
| Feature | PKI |
| Regression | No |
| Bug Type | Enhancement |
| Automatable | Yes |
| Interop | No |
| Source Sheet | Customer Escalations - Overall |

**Comments**: Security Enhancement

---
## 6. ENG-842447

**Jira**: [ENG-842447](https://netskope.atlassian.net/browse/ENG-842447)

**Description**: [Bharat Heavy] NSC crashing deleting user cert and SE tokens.

| Field | Value |
|-------|-------|
| OS Platform | Windows |
| Feature | Config Encryption |
| Regression | Day-1 |
| Bug Type | Enhancement |
| Automatable | Yes |
| Interop | No |
| Source Sheet | Customer Escalations - Overall |

**Comments**: New backup files have been created. Suggest to create new regression test cases based on: https://netskope.testrail.io/index.php?/cases/view/2616126

---
## 7. ENG-873979

**Jira**: [ENG-873979](https://netskope.atlassian.net/browse/ENG-873979)

**Description**: [NPP][Corebridge Financial (SAFG)] NSClient is disabled on multiple machines including both VDI and non-VDI machine

| Field | Value |
|-------|-------|
| OS Platform | Windows |
| Feature | Config Encryption |
| Regression | Day-1 |
| Bug Type | Internal found |
| Automatable | No |
| Source Sheet | Customer Escalations - Overall |

**Comments**: In CConfig::checkCertStatus(), read the user certificate with the "readAny" flag. Each time you load the user certificate file, verify if the correct file exists; if not, recover it.

---
## 8. ENG-924382

**Jira**: [ENG-924382](https://netskope.atlassian.net/browse/ENG-924382)

**Description**: CLONE - [MAIF] Nsclient create a wrong policy files for Firefox breaking the policy functionality in the browser

| Field | Value |
|-------|-------|
| OS Platform | Linux |
| Feature | PKI |
| Regression | Day 1 |
| Bug Type | Corner Case |
| Automatable | No |
| Source Sheet | Customer Escalations - Overall |

**Comments**: Verify firefox policies are maintained even with removal of policies file

---
