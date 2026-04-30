# IDP / Multi-User Bugs

Bugs related to IDP authentication, multi-user VDI enrollment, user session management, and credential handling.

> Source: Escalation Bug Review spreadsheet, filtered by keywords: IDP, multi-user, VDI, enrollment, authentication, session, credential.

**Total: 5 bugs**

---

## 1. ENG-565711

**Jira**: [ENG-565711](https://netskope.atlassian.net/browse/ENG-565711)

**Description**: [Orbia] Unsuccessful Netskope client enrolment in IDP mode due to caching

| Field | Value |
|-------|-------|
| OS Platform | Windows |
| Feature | IDP |
| Regression | No |
| Bug Type | Test Gap (Should have IDP with wrong user login negative cases) |
| Automatable | No |
| Interop | Yes |
| Source Sheet | Customer Escalations - Overall |

**Comments**: - Need to add test case
- Test Gap scope: Negative testing
- Interop Scope: Azure Entra

Deepthi - Thsi is related to Azure + IDP + Caching : This needs to added as part of Inerop. I think we can discuss around this as many cases are specific to Azure / Citrix VDI

---
## 2. ENG-669129

**Jira**: [ENG-669129](https://netskope.atlassian.net/browse/ENG-669129)

**Description**: [Petrobras] Netskope is not populating email address on the configuration pop-up for few users

| Field | Value |
|-------|-------|
| OS Platform | Windows |
| Feature | Multi-user |
| Regression | Day-1 |
| Bug Type | Corner case. |
| Automatable | No |
| Interop | Yes |
| Source Sheet | Customer Escalations - Overall |

**Comments**: - The issue involves user emails not appearing in the Netskope client configuration pop-up on VDI machines
- This setup involves User roaming profiles which was mounted on Remore Shared network for Non-persistent VDI

---
## 3. ENG-704508

**Jira**: [ENG-704508](https://netskope.atlassian.net/browse/ENG-704508)

**Description**: ENG-704508 CLONE - [Southcoast Health] IDP authentication State is not changing during secondary window popup by Webview2

| Field | Value |
|-------|-------|
| OS Platform | Windows |
| Feature | IDP |
| Regression | No |
| Bug Type | Corner case |
| Automatable | No |
| Interop | No |
| Source Sheet | Customer Escalations - Overall |

**Comments**: - Some part of code treated user,usergroup and IDs as case-sensitive (preserving the original case), while others treated them as case-insensitive (converting everything to lowercase). This mismatch led to duplicate or mismatched records in the database, causing users to receive incorrect configurations.
- skip_user_id_mapping_lookup feature flag was introduce. When enabled, this flag skips the problematic lookup in the user_id_mapping collection that could point to deleted or mixed-case records, ensuring the system fetches the correct active user record. And cache entrise were also cleanedup.

---
## 4. ENG-772404

**Jira**: [ENG-772404](https://netskope.atlassian.net/browse/ENG-772404)

**Description**: If the CA certificate download fails, the client does not retry fetching it. Instead, it continues downloading the user certificate, whose validation inevitably fails because its is

| Field | Value |
|-------|-------|
| OS Platform | Windows |
| Feature | Multi-user |
| Regression | Day-1 |
| Bug Type | Enhancement |
| Automatable | No |
| Interop | No |
| Source Sheet | Customer Escalations - Overall |

**Comments**: The fix adds a retry mechanism of downloading root and tenant ca cert when the certificate status check fails due to a chain error.

---
## 5. ENG-942287

**Jira**: [ENG-942287](https://netskope.atlassian.net/browse/ENG-942287)

**Description**: [IAG] - Some users are unable to print documents using different applications like Adobe and Outlook.

| Field | Value |
|-------|-------|
| OS Platform | Windows |
| Feature | Multi-user |
| Regression | Day 1 |
| Bug Type | Corner Case |
| Automatable | No |
| Source Sheet | Customer Escalations - Overall |

**Comments**: With FF (master_passcode_for_client_enablement) enabled, set master password. Now disable FF & test disabling services, which in previous builds retained the earlier set password. With 137 & above, the salt and hash values in nsconfig.json will contain empty/blank values if FF is disabled.

---
