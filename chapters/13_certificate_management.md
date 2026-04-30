# 13. Certificate Management

**Escalation Bug Count**: 16 (cross-referenced) | **Regression**: 4 (33%) | **Day-1**: 3 (25%) | **Test Gap**: 3 (25%)

📋 **[Test Cases — Google Sheet](https://docs.google.com/spreadsheets/d/1ackCZ-EcepXw1BkSGoi5Go9Ex1I72-fXqcqLGMGiuio/edit?gid=2121756775#gid=2121756775)**

> This chapter covers how NSClient manages SSL/TLS certificates across the full lifecycle: downloading from Management Plane, installing into platform-specific trust stores, validating certificate chains, rotating CA certificates, and handling cert-pinned applications. Certificate management is foundational to NSClient's SSL interception capability and tunnel authentication. While no bugs are filed directly under "Certificate Management" as a feature category, **12 escalation bugs from other feature areas** directly involve certificate-related failures -- making this a critical cross-cutting concern.

---

## Overview

NSClient sits between the endpoint and the internet, intercepting HTTPS traffic for inspection by the Netskope Cloud. For this to work, three certificate-dependent operations must all succeed:

1. **Root CA + Tenant CA installation** -- The endpoint must trust a Netskope-issued root CA certificate so that the cloud can re-sign inspected traffic without triggering browser certificate errors. Each platform has its own trust store mechanism (Windows CryptoAPI, macOS Keychain, Linux system CA directory).
2. **User certificate authentication** -- Each device needs a unique PKCS#12 user certificate to authenticate when establishing the SPDY tunnel to the Netskope gateway.
3. **Cert-pinned application handling** -- Applications that reject non-default CAs must be identified and either bypassed, blocked, or allowed through with special handling.

Without proper certificate management, HTTPS interception fails (users see certificate errors on every site), tunnel establishment fails (gateway rejects unauthenticated devices), and certificate rotation becomes a fleet-wide outage event.

The highest-risk areas identified from cross-referenced escalation bugs are:

- **Linux certificate installation failures** (ENG-609001, ENG-846555) -- Ubuntu 24.04 boundary conditions, /tmp noexec blocking cert operations, Firefox policies.json corruption risk
- **Config encryption + certificate interaction** (ENG-557778) -- nspubkey.pem.enc rendered unusable after Secure Enrollment
- **Cert-pinned application logic errors** (ENG-595031, ENG-742949, ENG-525399, ENG-499052) -- Wrong API endpoints, bypass failures, Android-specific exceptions
- **TLS/DTLS tunnel authentication** (ENG-503501, ENG-429034) -- DTLS-to-TLS fallback failures, SSL_read errors

---

## Certificate Types and Hierarchy

NSClient uses a three-tier certificate chain: Root CA -> Tenant CA (intermediate) -> User Cert. This design allows per-tenant isolation (each tenant gets a unique intermediate CA), independent rotation (root and tenant CA can be rotated independently), and user-level authentication (each user/device gets a unique PKCS#12 certificate for tunnel auth).

| Certificate | File Name | Format | Purpose | Scope | Rotation |
|---|---|---|---|---|---|
| **Root CA** | `nscacert.pem` | PEM | Trust anchor for SSL interception; installed into OS trust store | Per-organization | Rare; triggers CA rotation flow |
| **Tenant CA** | `nstenantcert.pem` | PEM | Intermediate CA; signs user certs; installed into intermediate store | Per-tenant | Can rotate independently of root CA |
| **User Cert** | `nsusercert.p12` | PKCS#12 | Device/user authentication for tunnel establishment | Per-user per-device | On CA rotation or re-enrollment |
| **Root CA Backup** | `nscacert_bak.pem` | PEM | Fallback if new root CA installation fails | Per-organization | Updated after successful install |
| **Tenant CA Backup** | `nstenantcert_bak.pem` | PEM | Fallback if new tenant CA installation fails | Per-tenant | Updated after successful install |
| **Log Encryption Key** | `nspubkey.pem` | PEM | Public key for encrypting log files before upload | Per-organization | Downloaded during config sync |

**Key source files**:
- `lib/nsConfig/config.h` -- Certificate file name definitions, API endpoint definitions, CA_ROTATION_STATUS enum
- `lib/nsConfig/config.cpp` -- Download, install, rotation, and validation logic
- `lib/nsConfig/win/cert.h` / `cert.cpp` -- Windows certificate store operations
- `lib/nsConfig/osx/cert.h` / `cert.cpp` -- macOS Keychain operations
- `lib/nsConfig/linux/cert.h` / `cert.cpp` -- Linux system CA and browser-specific installation
- `lib/nsConfig/ios/cert.cpp` -- iOS certificate operations (stub/no-op, handled by MDM)
- `lib/nsCert/peer.cpp` -- Peer certificate verification for tunnel TLS
- `lib/nsConfig/nsConfigSec.h` -- Config encryption module (handles `.enc` suffix for encrypted cert files)

---

## Certificate Lifecycle Flow (All Platforms)

The following diagram shows the complete certificate lifecycle from first enrollment through ongoing rotation, annotated with known failure points from escalation bugs. Certificate download happens every 300 seconds (`CERTS_DOWNLOAD_INTERVAL`). The most dangerous operation is CA rotation, where a failed installation triggers a fallback mechanism that restores backup certificates -- but race conditions during multi-user scenarios can leave individual users with stale certificates.

```mermaid
flowchart TD
    START[Device Installed] --> ENROLL[Enrollment Flow]
    ENROLL --> DL_ROOT[Download Root CA<br/>nscacert.pem]
    DL_ROOT --> DL_TENANT[Download Tenant CA<br/>nstenantcert.pem]
    DL_TENANT --> INSTALL{Install to<br/>System Store}

    INSTALL -->|Windows| WIN_STORE["CryptoAPI Import<br/>ROOT + CA stores"]
    INSTALL -->|macOS| MAC_STORE["Keychain Import<br/>+ Trust Policy"]
    INSTALL -->|Linux| LINUX_STORE["Write to<br/>/usr/local/share/ca-certificates/"]

    WIN_STORE --> FF_WIN["Firefox: certutil<br/>download + NSS db"]
    MAC_STORE --> FF_MAC["Firefox: certutil<br/>download + NSS db"]
    LINUX_STORE --> UPDATE_CA["update-ca-certificates"]
    UPDATE_CA --> FF_LINUX["Firefox: policies.json"]
    FF_LINUX --> RISK_FF["🟡 Warning: policies.json<br/>structure corruption risk"]
    LINUX_STORE --> BUG_UBUNTU["🔴 BUG ENG-609001<br/>Ubuntu 24.04 cert path<br/>boundary condition"]
    LINUX_STORE --> BUG_NOEXEC["🔴 BUG ENG-846555<br/>/tmp noexec blocks<br/>cert operations"]
    UPDATE_CA --> CHROME_LINUX["Chrome: certutil<br/>to ~/.pki/nssdb"]

    FF_WIN --> DL_USER[Download User Cert<br/>nsusercert.p12]
    FF_MAC --> DL_USER
    CHROME_LINUX --> DL_USER

    DL_USER --> VALIDATE[Validate Chain<br/>User -> Tenant CA -> Root CA]
    VALIDATE -->|Valid| READY[Certificates Ready]
    VALIDATE -->|Invalid| HEAL[Self-Healing:<br/>Re-download CA + Reinstall]
    HEAL --> VALIDATE

    READY --> PERIODIC["Periodic Check<br/>Every 300s"]
    PERIODIC -->|CA Changed| ROTATION[CA Rotation Flow]
    PERIODIC -->|No Change| READY
    PERIODIC -.->|Bug| BUG_499787["🔴 ENG-499787<br/>macOS pop up authentication<br/>dialog in CA rotation"]

    ROTATION --> BACKUP[Backup Old Certs]
    BACKUP --> INSTALL_NEW[Install New CA]
    INSTALL_NEW -->|Success| MARK_USERS["Mark All Users<br/>certRotated=true"]
    INSTALL_NEW -->|Failed| FALLBACK["Fallback to Backup Certs<br/>Status: SYS_FAIL"]
    MARK_USERS --> REDOWNLOAD[Re-download<br/>All User Certs]
    REDOWNLOAD --> READY
    FALLBACK --> RISK_RACE["🟡 Warning: Multi-user<br/>race condition during<br/>cert rotation"]

    DL_ROOT -.->|MITM risk| BUG_785573["🔴 ENG-785573<br/>PSIRT: Shared trusted root cert<br/>among MPs allows MITM (Win)"]
    DL_ROOT -.->|MITM risk| BUG_785574["🔴 ENG-785574<br/>PSIRT: Shared trusted root cert<br/>among MPs allows MITM (Mac)"]
    FF_LINUX -.->|Policy corrupt| BUG_924382["🔴 ENG-924382<br/>Nsclient creates wrong<br/>policy files for Firefox"]

    style READY fill:#4CAF50,color:#fff
    style FALLBACK fill:#FF9800,color:#fff
```

### Node Risk Assessment: Certificate Lifecycle

| Node | Risk | Assessment |
|---|---|---|
| Download Root CA | Low | Standard HTTPS download from MP; retries built in |
| Download Tenant CA | Low | Same download mechanism as Root CA |
| Install to System Store | **High** | Platform-specific; multiple failure modes (permissions, locked keychain, noexec) |
| Firefox: policies.json | 🟡 **Medium** | Predicted risk: structure corruption breaks Firefox trust |
| Ubuntu 24.04 cert path | **High** | ENG-609001 -- .deb package boundary condition on Ubuntu 24.04 |
| /tmp noexec | **High** | ENG-846555 -- Security hardening blocks cert file operations |
| Download User Cert | Medium | Requires successful CA installation first |
| Validate Chain | Medium | Chain validation can trigger self-healing re-download loop |
| CA Rotation Flow | **High** | Fleet-wide operation; failure can break SSL interception for all users |
| Fallback to Backup | Medium | Restores old certs but multi-user race condition exists |
| Mark All Users certRotated | Medium | No atomic lock between flag write and cert download |

---

## Certificate Download and Installation Flow (All Platforms)

NSClient downloads certificates from the Management Plane (addonman API) during initial enrollment and periodically during operation. The API endpoints have evolved across three security generations (V1 legacy, V5 API Security with HMAC, V7 Secure Config with JWT). The client selects the API version based on feature flags: `validateConfig == true` uses V7, `enableAPISecurity == true` uses V5, otherwise V1/V2 legacy.

The download sequence is sequential: Root CA first, then Tenant CA, then install both, then User Cert. If any step fails, later steps are skipped. This sequential dependency means a transient MP outage during Root CA download silently prevents User Cert refresh as well.

```mermaid
sequenceDiagram
    participant SVC as stAgentSvc
    participant CFG as CConfig
    participant MP as Management Plane<br/>(addonman)
    participant STORE as OS Cert Store

    Note over SVC: checkAndDownloadCerts() called every 300s

    SVC->>CFG: checkAndDownloadCerts(sessID)
    CFG->>CFG: Check time since last download

    alt Time elapsed > CERTS_DOWNLOAD_INTERVAL
        CFG->>CFG: Backup existing CA cert<br/>(nscacert_bak.pem)
        CFG->>MP: GET /v7/config/ca/cert
        MP-->>CFG: nscacert.pem (PEM data)
        CFG->>CFG: validateCertFile()

        CFG->>CFG: Backup existing Tenant cert<br/>(nstenantcert_bak.pem)
        CFG->>MP: GET /v7/config/org/cert
        MP-->>CFG: nstenantcert.pem (PEM data)
        CFG->>CFG: validateCertFile()

        CFG->>CFG: installCACert()
        Note over CFG,STORE: Platform-specific install

        alt Windows
            CFG->>STORE: ImportCertificateFromBuffer(ROOT)
            CFG->>STORE: ImportCertificateFromBuffer(CA)
            CFG->>CFG: Check FedRAMP CN removal
        else macOS
            CFG->>STORE: ImportPEMFromBuffer(System.keychain)
            CFG->>STORE: SecTrustSettingsSetTrustSettings()
        else Linux
            CFG->>STORE: Write to /usr/local/share/ca-certificates/
            CFG->>CFG: update-ca-certificates -f
            CFG->>CFG: InstallCertFirefox()
            CFG->>CFG: InstallCertChrome() via nssdb
        end
    end

    CFG->>CFG: checkIfdownloadUserCert()

    alt User cert needs download
        CFG->>MP: GET /v7/config/user/cert
        MP-->>CFG: nsusercert.p12 (PKCS#12)
        CFG->>CFG: checkCertStatus() - validate chain

        alt Chain Invalid
            CFG->>CFG: Self-healing: re-download CA + Tenant
            CFG->>CFG: reinstall CA certs
            CFG->>CFG: retry checkCertStatus()
        end
    end
```

---

## Windows

**Bug Count**: 5 cross-referenced | **Key Gaps**: Config encryption, FedRAMP cert cleanup, cert-pinned bypass logic

Windows certificate installation uses the Windows CryptoAPI to import certificates into the machine-level certificate store (`CERT_SYSTEM_STORE_LOCAL_MACHINE`). The root CA goes to the `ROOT` store and the tenant CA goes to the `CA` (intermediate) store. A key design detail is that `ImportCertificateFromBuffer()` performs an automatic self-signed check -- if a certificate targeted for the ROOT store is not self-signed, it is redirected to the CA store instead.

FedRAMP environments have special certificate handling. When FedRAMP intermediate certificates are detected (by matching CN against "Netskope Tenant Authority (FedRAMP Intermediate)" or "Netskope Tenant Authority (FedRAMP Regional)"), the code removes old FedRAMP certificates from the ROOT store that may have been incorrectly placed there during upgrade scenarios. The ENG-897416 bug (FedRAMP client connecting to commercial domains) highlights the importance of testing FedRAMP-specific certificate and configuration isolation.

```mermaid
flowchart TD
    CERT["Certificate to Import"] --> SELF{IsSelfSigned?}
    SELF -->|Yes| ROOT_STORE["Import to ROOT Store"]
    SELF -->|No| FEDRAMP{CN matches FedRAMP<br/>Intermediate or Regional?}

    FEDRAMP -->|Yes| CLEANUP["Remove old FedRAMP certs<br/>from ROOT store"]
    CLEANUP --> CA_STORE["Import to CA Store"]

    FEDRAMP -->|No| CA_STORE

    ROOT_STORE --> MULTI{Multi-cert PEM?}
    CA_STORE --> MULTI
    MULTI -->|Yes| SPLIT["getCertsArray()<br/>Split and import each"]
    MULTI -->|No| ENC_CHECK{encryptClientConfig<br/>enabled?}
    SPLIT --> ENC_CHECK

    ENC_CHECK -->|Yes| ENCRYPT["Store as .enc<br/>(nsConfigSec)"]
    ENCRYPT --> BUG_ENC["🔴 BUG ENG-557778<br/>nspubkey.pem.enc<br/>unusable for remote logs"]
    ENC_CHECK -->|No| DONE[Import Complete]
    ENCRYPT --> DONE

    DONE --> FF{Firefox installed?}
    FF -->|Yes| FF_DL["Download certutil<br/>matched to Firefox version"]
    FF -->|No| FINAL[Ready]
    FF_DL --> FF_IMPORT["Import to Firefox<br/>NSS database"]
    FF_IMPORT --> FINAL

    style DONE fill:#4CAF50,color:#fff
    style FINAL fill:#4CAF50,color:#fff
```

### Windows Node Risk Assessment

| Node | Risk | Assessment |
|---|---|---|
| IsSelfSigned? | Low | Prevents intermediate certs in ROOT store |
| FedRAMP CN match | Medium | FedRAMP-specific cleanup; ENG-897416 shows FedRAMP isolation gaps |
| encryptClientConfig | **High** | ENG-557778 -- nspubkey.pem gets encrypted despite being on ignore list |
| Firefox certutil download | Medium | Version mismatch or download failure causes Firefox cert errors |
| getCertsArray() | Low | Multi-cert PEM splitting; well-tested path |

### Windows Bug Mapping

| Bug ID | Summary | Root Cause | Severity |
|---|---|---|---|
| ENG-557778 | nspubkey.pem.enc unusable for remote log collection | Secure Enrollment creates .enc before ignore list applied | S2 |
| ENG-595031 | Incorrect cert-pinned app definition applied | Client calls wrong API (steering/pinnedapps vs steering/dynamicpinnedapps) | S2 |
| ENG-649593 | ACK numbers mangled with local proxy + cert pin bypass | Day-1 packet handling bug in proxy + cert-pinned combination | S3 |
| ENG-718498 | DNS TCP bypassed with cert pinned block | DNS TCP traffic escapes cert-pinned block rule | S3 |
| ENG-742949 | Cert pinned bypass not working | Regression from ENG-649593 fix; bypass by tunnel still decrypted | S2 |

## macOS

**Bug Count**: 2 cross-referenced + known internal issues | **Key Gaps**: Trust policy recovery, Keychain permissions, Network Extension cert access

macOS uses the Security framework (`SecItemImport`, `SecTrustSettingsSetTrustSettings`) to import certificates into the System Keychain at `/Library/Keychains/System.keychain`. The root CA requires an explicit trust policy setting at the admin domain level. A known issue causes macOS to sometimes silently remove the trust policy for the Netskope root CA. The `ModifyCertTrustPolicy()` function checks whether the certificate is still trusted and re-applies the trust setting when a duplicate certificate import is detected.

On macOS Big Sur and above, an additional check using `SecTrustEvaluate()` distinguishes between "not trusted" and "expired" certificates -- expired certificates are intentionally not re-trusted.

```mermaid
flowchart TD
    IMPORT["ImportPEMFromBuffer()"] --> KEYCHAIN{Root User?}
    KEYCHAIN -->|Yes| SYS[Open System.keychain]
    KEYCHAIN -->|No| DEFAULT[Open Default Keychain]

    SYS --> SEC_IMPORT["SecItemImport()<br/>PEM format"]
    DEFAULT --> SEC_IMPORT

    SEC_IMPORT -->|errSecDuplicateItem| DUP_CHECK{Root Cert?}
    SEC_IMPORT -->|Success| ROOT_CHECK{Root Cert?}
    SEC_IMPORT -->|Error| RISK_PERM["🟡 Warning: Keychain<br/>access permission failure"]

    DUP_CHECK -->|Yes| TRUST_CHECK["ModifyCertTrustPolicy()"]
    DUP_CHECK -->|No| DONE_DUP[Certificate Already Exists]

    TRUST_CHECK --> TRUSTED{Still Trusted?}
    TRUSTED -->|Yes| DONE_DUP
    TRUSTED -->|No| BIGSUR{macOS Big Sur+?}

    BIGSUR -->|Yes| EVALUATE["SecTrustEvaluate()"]
    EVALUATE --> REASON{Failure Reason?}
    REASON -->|Not Trusted| REAPPLY["Re-apply Trust Setting"]
    REASON -->|Expired| SKIP["Do NOT Re-Trust<br/>Expired Certificate"]

    BIGSUR -->|No| REAPPLY

    ROOT_CHECK -->|Yes| SET_TRUST["SecTrustSettingsSetTrustSettings()<br/>kSecTrustSettingsDomainAdmin"]
    ROOT_CHECK -->|No| DONE[Import Complete]

    SET_TRUST --> DONE
    REAPPLY --> DONE

    BUG_DC["🔴 BUG ENG-419687<br/>DC based on cert: CA cert<br/>alone changes status to Managed"]

    style DONE fill:#4CAF50,color:#fff
    style DONE_DUP fill:#4CAF50,color:#fff
```

### macOS Node Risk Assessment

| Node | Risk | Assessment |
|---|---|---|
| Open System.keychain | Medium | Requires root; Network Extension sandbox may block |
| SecItemImport | Low | Standard Security framework import |
| ModifyCertTrustPolicy | 🟡 **High** | Predicted risk: macOS trust policy silently removed |
| SecTrustEvaluate | Medium | Big Sur+ only; distinguishes not-trusted from expired |
| Re-apply Trust Setting | Medium | Workaround for silent trust removal |
| Keychain access permission | Medium | App Sandbox restrictions in System Extension mode |

### macOS Bug Mapping

| Bug ID | Summary | Root Cause | Severity |
|---|---|---|---|
| ENG-419687 | Device Classification by cert: CA cert alone changes to Managed | CA cert in Personal store without client cert triggers Managed status | S3 |
| ENG-557778 | nspubkey.pem.enc unusable (shared with Windows) | Config encryption on Big Sur+ creates unusable encrypted key | S2 |

## Linux

**Bug Count**: 4 cross-referenced | **Key Gaps**: Ubuntu 24.04 support, /tmp noexec environments, Firefox policies.json, multi-distro coverage

Linux certificate installation is the most complex platform due to distribution diversity. The code writes PEM files to the system CA directory and runs the platform's certificate update command. It auto-detects the distribution: Debian/Ubuntu uses `/usr/local/share/ca-certificates/` with `update-ca-certificates`, while RHEL/CentOS uses `/etc/pki/ca-trust/source/anchors/` with `update-ca-trust`.

Firefox on Linux uses `policies.json` for enterprise certificate management, with paths varying by distribution and install method. Chrome uses the NSS database at `~/.pki/nssdb`. Four escalation bugs directly affect Linux certificate operations, making it the highest-risk platform for certificate installation failures.

```mermaid
flowchart TD
    CA_DATA["CA + Tenant CA Data"] --> DETECT{Distribution<br/>Detection}

    DETECT -->|update-ca-certificates exists| DEB["Debian/Ubuntu Path<br/>/usr/local/share/ca-certificates/"]
    DETECT -->|update-ca-trust exists| RHEL["RHEL/CentOS Path<br/>/etc/pki/ca-trust/source/anchors/"]

    DEB --> SAME_CHECK{Certs same<br/>as installed?}
    RHEL --> SAME_CHECK

    SAME_CHECK -->|Yes| SKIP[Skip Install]
    SAME_CHECK -->|No| REMOVE_OLD[Remove Old Certs]

    REMOVE_OLD --> WRITE_NEW["Write nscacert.crt<br/>+ nstenantcert.crt"]
    WRITE_NEW --> BUG_UBUNTU["🔴 BUG ENG-609001<br/>Ubuntu 24.04 cert path<br/>boundary condition"]
    WRITE_NEW --> BUG_NOEXEC["🔴 BUG ENG-846555<br/>/tmp noexec blocks<br/>cert file operations"]
    WRITE_NEW --> UPDATE["Run update-ca-certificates -f<br/>or update-ca-trust"]

    UPDATE --> FIREFOX["InstallCertFirefox()"]

    FIREFOX --> FF_STD{"/usr/lib/firefox/<br/>distribution/policies.json"}
    FIREFOX --> FF_SNAP{"/etc/firefox/<br/>policies/policies.json"}
    FIREFOX --> FF_RHEL{"/usr/lib64/firefox/<br/>distribution/policies.json"}

    FF_STD --> WRITE_JSON["Write policies.json<br/>with Install array +<br/>ImportEnterpriseRoots: true"]
    FF_SNAP --> WRITE_JSON
    FF_RHEL --> WRITE_JSON

    WRITE_JSON --> RISK_JSON["🟡 Warning: ImportEnterpriseRoots<br/>at wrong JSON level risk"]

    UPDATE --> CHROME["InstallCertChrome()"]
    CHROME --> NSSDB["certutil -d sql:~/.pki/nssdb<br/>-A -t 'C,,' -n nscacert"]

    SKIP --> DONE[Ready]
    NSSDB --> DONE
    WRITE_JSON --> DONE

    style DONE fill:#4CAF50,color:#fff
```

### Linux Node Risk Assessment

| Node | Risk | Assessment |
|---|---|---|
| Distribution Detection | Low | Simple file existence check |
| Write nscacert.crt | **High** | ENG-609001 (Ubuntu 24.04) + ENG-846555 (/tmp noexec) |
| update-ca-certificates | Medium | Can fail silently; must run with -f flag |
| InstallCertFirefox | 🟡 **High** | Predicted risk: policies.json corruption |
| Firefox Snap path | Medium | Different path than standard Firefox; Ubuntu 22+ only |
| InstallCertChrome (nssdb) | Medium | Existing cert with same nickname causes failure; code retries once |

### Linux Bug Mapping

| Bug ID | Summary | Root Cause | Severity |
|---|---|---|---|
| ENG-609001 | Ubuntu 24.04 cert errors from .deb install | .deb package not supported on Ubuntu 24.04; cert path boundary | S2 |
| ENG-846555 | Linux auto-upgrade fails with /tmp noexec security hardening | Installer uses /tmp; noexec blocks cert operations | S2 |
| *(predicted)* | Firefox policies.json: ImportEnterpriseRoots at wrong JSON level | Code analysis reveals incorrect JSON structure risk | S3 |

## Android

**Bug Count**: 2 cross-referenced | **Key Gaps**: Cert-pinned app exceptions, OS-level bypass behavior

Android certificate handling is primarily delegated to the Java/Kotlin layer via JNI callbacks. The native C++ service calls `downloadCACert()` which triggers the Java layer to install certificates using the Android KeyStore API. On Android 7+ (SDK 24+), user-installed CA certificates are not trusted by default for apps, requiring the VPN service's network security config or MDM push as system-level trust anchor.

The main certificate-related bugs on Android involve cert-pinned application exception handling rather than certificate installation itself. ENG-499052 shows that cert-pinned exceptions were not enforced at the OS level from R112.1 onwards, and ENG-525399 shows that a cert-pinned app regex bypass error can cause ALL traffic to be bypassed.

### Android Bug Mapping

| Bug ID | Summary | Root Cause | Severity |
|---|---|---|---|
| ENG-499052 | Teams cert-pinned exceptions not enforced at OS level | Cert-pinned OS-level bypass removed in R112.1; regression | S2 |
| ENG-525399 | CertPinned app exception bypass causing ALL traffic bypassed | Native apps with regex on cert-pinned list cause over-broad bypass | S2 |

## iOS

iOS certificate installation is handled entirely via MDM profile distribution. The `lib/nsConfig/ios/cert.cpp` file contains stub implementations that return success without performing actual operations. All certificate functions are no-ops because iOS does not allow apps to install certificates into the system trust store programmatically. The MDM administrator must push a configuration profile containing the Netskope root CA, and the user must manually trust the profile in Settings > General > About > Certificate Trust Settings.

*No escalation bugs specific to iOS certificate management. iOS cert-related bugs (ENG-450735) are steering/exception issues rather than certificate installation failures.*

## ChromeOS

ChromeOS uses the Android certificate handling path. Certificate installation goes through the Android KeyStore API via the VPN service. No escalation bugs directly reference ChromeOS certificate installation.

*TODO: Validate ChromeOS cert-pinned app behavior matches Android expectations.*

---

## Backend

Backend certificate management involves the Management Plane (addonman) serving certificate files through versioned API endpoints, CA rotation coordination, and cert-pinned app list distribution.

The ENG-897416 bug highlights a backend-related certificate concern: FedRAMP/PBMM NSClient initiates outbound connections to the commercial domain `sfchecker.goskope.com` despite being configured for a govskope tenant. While this is primarily a configuration/steering issue, it demonstrates that certificate trust domain boundaries can be violated by legacy code paths.

## CA Certificate Rotation Flow (All Platforms)

CA rotation is a critical fleet-wide operation that replaces the root CA and/or tenant CA. The state machine tracks rotation progress using `CA_ROTATION_STATUS` (NONE, IN_PROGRESS, FRESH_SYS_FAIL, SYS_FAIL). A separate `CA_ROTATION_3RD_STATUS` tracks third-party store installation (Firefox, Java/Android). The highest risk during rotation is the multi-user race condition: `updateAllUserCertRotated()` iterates all user configs and sets `certRotated=true`, but if a user's tunnel is simultaneously downloading a user cert, the old cert may be written after the flag is set.

```mermaid
sequenceDiagram
    participant MP as Management Plane
    participant SVC as stAgentSvc
    participant CFG as CConfig
    participant STORE as OS Cert Store
    participant UI as stAgentUI

    Note over MP: Admin rotates tenant CA

    SVC->>CFG: Periodic checkAndDownloadCerts()
    CFG->>MP: Download nscacert.pem
    CFG->>MP: Download nstenantcert.pem

    CFG->>CFG: Compare with backup: isCAUpdated()

    alt CA content changed
        CFG->>CFG: updateCARotationStatus(IN_PROGRESS)
        CFG->>CFG: installCACert()

        alt Install succeeded
            CFG->>CFG: Backup new certs
            CFG->>CFG: updateCARotationStatus(NONE)
            CFG->>CFG: updateAllUserCertRotated()
            Note over CFG: Sets certRotated=true in ALL users' nsuser.conf
            CFG->>UI: onCaRotationDone()
            CFG->>MP: handleCAInstallationStatus("CA Installation Change")
        else Install failed
            CFG->>CFG: fallbackCAAndTenantCert()
            Note over CFG: Restore from backup files
            CFG->>CFG: updateCARotationStatus(SYS_FAIL)
            CFG->>MP: handleCAInstallationStatus("CA Installation Failure")
        end
    end

    Note over SVC: Next user cert download cycle
    SVC->>CFG: checkIfdownloadUserCert()
    CFG->>CFG: certRotated == true?

    alt Cert rotated flag set
        CFG->>MP: Download new nsusercert.p12
        CFG->>CFG: checkCertStatus() - Validate new chain

        alt Chain valid
            CFG->>CFG: setCertRotated(false)
        else Chain invalid
            CFG->>CFG: Re-download CA + Tenant CA
            CFG->>CFG: Reinstall CA certs
            CFG->>CFG: Re-validate chain
        end
    end
```

---

## Certificate Chain Validation (All Platforms)

After downloading the user certificate, NSClient validates the complete certificate chain: User Cert -> Tenant CA -> Root CA. If the chain is invalid (`USER_CERT_CHAIN_INVALID`), the code attempts a self-healing flow: re-download the CA and Tenant CA, reinstall them, and retry validation. This self-healing mechanism handles the case where the CA was rotated but the new CA was not yet installed when the user cert was downloaded.

```mermaid
flowchart TD
    DL["downloadUserCert()"] --> VALIDATE["checkCertStatus()<br/>User Cert -> Tenant CA -> Root CA"]
    VALIDATE --> RESULT{Chain Valid?}

    RESULT -->|Yes| OK[Certificate Ready]
    RESULT -->|No| ERROR{Error Type?}

    ERROR -->|USER_CERT_CHAIN_INVALID| HEAL["Self-Healing Flow"]
    ERROR -->|Other Error| FAIL[Report Error]

    HEAL --> RE_CA["downloadCACert()"]
    RE_CA --> RE_TENANT["downloadTenantCert()"]
    RE_TENANT --> RE_INSTALL["installCACert()"]
    RE_INSTALL --> RETRY["Retry checkCertStatus()"]

    RETRY --> RETRY_RESULT{Chain Valid<br/>After Retry?}
    RETRY_RESULT -->|Yes| OK
    RETRY_RESULT -->|No| FAIL

    style OK fill:#4CAF50,color:#fff
```

---

## Certificate-Pinned Application Handling (All Platforms)

Some applications use certificate pinning to reject any CA not in their built-in trust list. NSClient maintains a `certPinnedAppList` configuration specifying how to handle these applications. The list is downloaded via the addonman API (`getCertPinnedListV3()` or `getCertPinnedListV2()`). ENG-595031 exposed a critical bug where the client called the wrong API endpoint (`steering/pinnedapps` instead of `steering/dynamicpinnedapps`) when Secure Config Validation and Dynamic Steering were both enabled.

Cert-pinned app handling involves three key bugs that form a regression chain: ENG-649593 (original ACK mangling bug with proxy + cert pin) was fixed, but the fix caused ENG-742949 (cert-pinned bypass stopped working), which required a subsequent fix.

```mermaid
flowchart TD
    TRAFFIC["Outbound HTTPS Traffic"] --> MATCH{Matches<br/>certPinnedAppList?}

    MATCH -->|No| NORMAL["Normal SSL Interception"]
    MATCH -->|Yes| ACTION{Action?}

    ACTION -->|BYPASS (1)| BYPASS["Bypass SSL Interception"]
    ACTION -->|BLOCK (0)| BLOCK["Block Traffic"]
    ACTION -->|BMD (2)| DC_CHECK{Device<br/>Managed?}
    ACTION -->|CUSTOM_DC (3)| LABEL_CHECK{Custom DC<br/>Label Match?}
    ACTION -->|DECRYPTION (4)| DECRYPT["Attempt Decryption"]

    DC_CHECK -->|Yes| BYPASS
    DC_CHECK -->|No| BLOCK

    LABEL_CHECK -->|Yes| BYPASS
    LABEL_CHECK -->|No| BLOCK

    BYPASS --> MODE{Mode?}
    MODE -->|direct| DIRECT["Traffic bypasses tunnel entirely"]
    MODE -->|tunnel| TUNNEL["Traffic through tunnel,<br/>no SSL interception"]

    TUNNEL --> BUG_BYPASS["🔴 BUG ENG-742949<br/>Cert pinned bypass<br/>still decrypted intermittently"]

    BLOCK --> DNS_CHECK{DNS TCP<br/>from same app?}
    DNS_CHECK -->|Yes| BUG_DNS["🔴 BUG ENG-718498<br/>DNS TCP bypassed<br/>despite block"]
    DNS_CHECK -->|No| DROP[Traffic Dropped]

    DIRECT --> BUG_API["🔴 BUG ENG-595031<br/>Wrong API endpoint:<br/>pinnedapps vs dynamicpinnedapps"]

    NORMAL --> DONE[Continue to Cloud]
    DROP --> DONE
    DIRECT --> DONE
    TUNNEL --> DONE

    style DONE fill:#2196F3,color:#fff
```

### Cert-Pinned App Node Risk Assessment

| Node | Risk | Assessment |
|---|---|---|
| certPinnedAppList match | Medium | Regex matching can cause over-broad matches (ENG-525399 on Android) |
| Action selection | Low | Simple enum lookup |
| Bypass (direct mode) | **High** | ENG-595031 -- Wrong API endpoint for dynamic steering + secure config |
| Bypass (tunnel mode) | **High** | ENG-742949 -- Traffic still decrypted intermittently after bypass |
| Block + DNS TCP | **High** | ENG-718498 -- DNS TCP escapes cert-pinned block |
| Device Managed check | Medium | ENG-419687 -- CA cert alone triggers Managed status |

---

## Config Encryption and Certificates (All Platforms)

When `encryptClientConfig` is enabled, certificate files are stored with a `.enc` suffix (e.g., `nscacert.pem.enc`). The `CConfigSec` class handles transparent encryption/decryption. The `nspubkey.pem` file is explicitly listed in `m_ignoredFiles` in `nsConfigSec.h`, meaning it should NOT be encrypted -- it is a public key used for log encryption and must be readable without decryption.

However, ENG-557778 demonstrated that the Secure Enrollment flow can create `nspubkey.pem.enc` before the ignore list is applied, rendering remote log collection non-functional. This bug was classified as "missing test case -- neither dev nor QE test it" and highlights the need for config encryption + certificate interaction testing.

Config encryption is supported on: Windows (always), macOS (Big Sur+ only), Linux (available), Android/iOS (not supported).

---

## Automation Coverage Summary

The following table maps test cases to existing automation in the golden regression suite at `golden_regression/tests/features/`.

| Test Area | Golden Regression Suite Coverage | Status |
|---|---|---|
| **SSL Pinned App Bypass** | `ssl_pinned_app/test_p0.py::test_12_ssl_pinned_bypass` | ✅ Covered |
| **SSL Pinned App Block/Drop** | `ssl_pinned_app/test_p0.py::test_13_ssl_pinned_drop` | ✅ Covered |
| **SSL Pinned App Drop Events** | `ssl_pinned_app/test_p0.py::test_14_ssl_pinned_drop_events_log` | ✅ Covered |
| **SSL Pinned App Web Mode** | `ssl_pinned_app/test_p0.py::test_15_ssl_pinned_web_mode` | ✅ Covered |
| **SSL Pinned App On-Prem** | `ssl_pinned_app/test_p0.py::test_18_ssl_pinned_bypass_on_prem` | ✅ Covered |
| **SSL Pinned App Off-Prem** | `ssl_pinned_app/test_p0.py::test_19_ssl_pinned_bypass_off_prem` | ✅ Covered |
| **Root CA Installation** | -- | ❌ Not covered |
| **CA Rotation Flow** | -- | ❌ Not covered |
| **CA Rotation Fallback** | -- | ❌ Not covered |
| **Config Encryption + Certs** | -- | ❌ Not covered |
| **Firefox policies.json (Linux)** | -- | ❌ Not covered |
| **Chrome NSS db (Linux)** | -- | ❌ Not covered |
| **FedRAMP Cert Cleanup** | -- | ❌ Not covered |
| **macOS Trust Policy Recovery** | -- | ❌ Not covered |
| **Cert Chain Validation + Self-Healing** | -- | ❌ Not covered |
| **DTLS-to-TLS Fallback** | -- | ❌ Not covered |
| **DNS TCP + Cert Pinned Block** | -- | ❌ Not covered |
| **Cert Pinned + Dynamic Steering + Secure Config** | -- | ❌ Not covered |
| **Remote Log Collection + encryptClientConfig** | -- | ❌ Not covered |
| **Ubuntu 24.04 Cert Installation** | -- | ❌ Not covered |
| **/tmp noexec Cert Installation** | -- | ❌ Not covered |

**Coverage Summary**: 6 of 21 test areas covered (29%). The ssl_pinned_app suite provides good coverage for basic cert-pinned bypass/block scenarios, but CA lifecycle operations (installation, rotation, fallback, chain validation) and platform-specific cert installation (Linux, macOS trust policy) have zero automation coverage.

---

## Cross-Flow Interactions

Certificate management interacts with nearly every other NSClient subsystem. The following interactions have been validated through escalation bug analysis.

### Interaction 1: Certificate + Tunnel Authentication

When the user certificate is invalid or expired, tunnel establishment fails. The tunnel authentication flow (`lib/nsCert/peer.cpp`) uses the Windows CertGetCertificateChain API (on Windows) or equivalent platform APIs to validate against the machine's certificate store. If the tunnel reply contains a "Cert Revoked" (0xab) status, the client triggers a certificate re-download.

ENG-503501 (DTLS-to-TLS fallback failure) and ENG-429034 (Android TLS SSL_read failure) both affect the TLS layer that depends on valid certificates for authentication.

### Interaction 2: Certificate + Config Encryption

ENG-557778 demonstrates that config encryption (`encryptClientConfig`) can create encrypted versions of certificate-adjacent files (nspubkey.pem.enc) that break downstream functionality. The intersection of Secure Enrollment + Config Encryption + Certificate Management is undertested.

### Interaction 3: Certificate + Steering (Cert-Pinned Apps)

Cert-pinned app handling depends on correct API endpoint selection (V2 vs V3 format, static vs dynamic steering lists), correct bypass mode enforcement (direct vs tunnel), and correct DNS TCP handling. The regression chain ENG-649593 -> ENG-742949 shows that fixes in this area have high regression risk.

### Interaction 4: Certificate + FailClose

During CA rotation, if FailClose is active and the CA installation fails, the fallback mechanism restores old certificates -- but the FailClose rules remain based on the old tunnel session. If the tunnel needs to reconnect with new certificates during this window, users can experience network outage.

### Cross-Flow Risk Matrix (Chapter-Relevant)

| Interaction | Chapters Involved | Risk Level | Test Coverage |
|---|---|---|---|
| CA Rotation + Tunnel Reconnect | Ch.13 + Ch.07 | **Critical** | ❌ Not covered |
| Config Encryption + Cert Files | Ch.13 + Ch.18 | **High** | ❌ Not covered |
| Cert-Pinned + Dynamic Steering + Secure Config | Ch.13 + Ch.05 | **High** | ❌ Not covered |
| CA Rotation + FailClose | Ch.13 + Ch.11 | **High** | ❌ Not covered |
| Cert-Pinned Bypass + Proxy | Ch.13 + Ch.14 | **Medium** | ⚠️ Partial |
| Linux Cert Install + Browser Trust | Ch.13 + Ch.01 | **High** | ❌ Not covered |
| CA Rotation + Multi-User VDI | Ch.13 + Ch.07 | **High** | ❌ Not covered |
| DTLS/TLS Fallback + Cert Auth | Ch.13 + Ch.07 | **Medium** | ❌ Not covered |

## Troubleshooting

### Log Keywords

| Keyword | Context | Meaning |
|---|---|---|
| `downloading ca cert` | `config.cpp` | Root CA download started |
| `downloading tenant cert` | `config.cpp` | Tenant CA download started |
| `downloading user cert` | `config.cpp` | User cert download started |
| `ca cert downloaded successfully` | `config.cpp` | Root CA download succeeded |
| `downloaded ca cert is invalid` | `config.cpp` | Root CA validation failed |
| `cacert imported successfully` | `cert.cpp` | Certificate installed to OS store |
| `failed to import cacert` | `cert.cpp` | Certificate install failed |
| `Failed to set trust setting error` | `osx/cert.cpp` | macOS trust policy setting failed |
| `CA is installed to system` | `linux/cert.cpp` | Linux system CA updated |
| `installed nssdb` | `linux/cert.cpp` | Linux Chrome/NSS db updated |
| `write firefox policy file` | `linux/cert.cpp` | Linux Firefox policies.json updated |
| `cert rotating, update all users tag` | `config.cpp` | CA rotation marking all users for re-download |
| `Set ca cert update status to` | `config.cpp` | CA rotation status changed |
| `Install CA failed, ca rotation status` | `config.cpp` | CA install failed, fallback initiated |
| `checkCertStatus return` | `config.cpp` | Certificate chain validation result |
| `USER_CERT_CHAIN_INVALID` | `config.cpp` | User cert chain does not validate against CA |
| `need to download user cert again` | `config.cpp` | User cert will be re-downloaded (certRotated=true) |
| `Certificate is already in store` | `osx/cert.cpp` | Duplicate cert detected (not an error) |
| `Certificate deleted successfully` | `win/cert.cpp` | FedRAMP cert cleanup on Windows |

### Certificate File Locations

| Platform | Data Path | Download Path |
|---|---|---|
| **Windows** | `%ProgramData%\Netskope\STAgent\data\` | `%ProgramData%\Netskope\STAgent\download\` |
| **macOS** | `/Library/Application Support/Netskope/STAgent/data/` | `/Library/Application Support/Netskope/STAgent/download/` |
| **Linux** | `/opt/netskope/stagent/data/` | `/opt/netskope/stagent/download/` |

### Constants

| Constant | Value | Description |
|---|---|---|
| `CERTS_DOWNLOAD_INTERVAL` | 300 seconds | Minimum interval between certificate download attempts |
| Issuer Email | `certadmin@netskope.com` | Email address used to identify Netskope-issued certificates |

---

## Appendix A: Bug Quick Reference

All certificate-related bugs cross-referenced from escalation bug data across all 4 feature categories (install/upgrade, steering, tunneling, failclose).

| Bug ID | Summary | Platform | Primary Feature | Root Cause | Severity | Bug Type |
|---|---|---|---|---|---|---|
| ENG-419687 | DC based on cert: CA cert alone changes status to Managed | Windows/Mac | Device Classification | CA cert in Personal store without client cert triggers Managed | S3 | Test Gap |
| ENG-429034 | Android tunnel disconnects with TLS SSL_read failed | Android | Tunneling | SSL_read error on specific Samsung devices with data switch | S3 | Corner Case |
| ENG-499052 | Teams cert-pinned exceptions not enforced at OS level | Android | Steering | OS-level bypass removed in R112.1 | S2 | Regression |
| ENG-503501 | DTLS doesn't fallback to TLS | Windows | Tunneling | Regression from ENG-445563: TLS fallback not executed | S2 | Regression |
| ENG-525399 | CertPinned app exception bypass causing ALL traffic bypassed | Android | Steering | Native apps with regex cause over-broad bypass | S2 | Test Gap |
| ENG-557778 | nspubkey.pem.enc unusable for remote log collection | Windows | Install/Config | Secure Enrollment creates .enc before ignore list applied | S2 | Test Gap |
| ENG-595031 | Incorrect cert-pinned app definition applied | Windows | Steering/Config | Wrong API endpoint with Secure Config + Dynamic Steering | S2 | Regression |
| ENG-609001 | Ubuntu 24.04 cert errors from .deb install | Linux | Install | .deb package not supported on Ubuntu 24.04 | S2 | Day-1 |
| ENG-649593 | ACK numbers mangled with proxy + cert pin bypass | Windows | Steering | Day-1 packet handling bug in specific combination | S3 | Day-1 |
| ENG-718498 | DNS TCP bypassed with cert pinned block | Windows | Steering/FailClose | DNS TCP escapes cert-pinned block rule | S3 | Enhancement |
| ENG-742949 | Cert pinned bypass not working | Windows | Steering | Regression from ENG-649593 fix | S2 | Regression |
| ENG-846555 | Linux auto-upgrade fails with /tmp noexec | Linux | Install | Installer uses /tmp; noexec blocks operations | S2 | Day-1 |
| ENG-897416 | FedRAMP NSClient connects to commercial domain | All | Steering/PKI | Deprecated sfchecker still sends DNS to commercial domain | S2 | Day-1 |
| [ENG-499787](https://netskope.atlassian.net/browse/ENG-499787) | macOS nsclient pop up authentication dialog in CA rotation |
| [ENG-785573](https://netskope.atlassian.net/browse/ENG-785573) | PSIRT: Shared trusted root cert among MPs allows MITM on Netskope tenant user (w |
| [ENG-785574](https://netskope.atlassian.net/browse/ENG-785574) | PSIRT: Shared trusted root cert among MPs allows MITM on Netskope tenant user (M |
| [ENG-924382](https://netskope.atlassian.net/browse/ENG-924382) | CLONE - [MAIF] Nsclient create a wrong policy files for Firefox breaking the pol |

---

## Appendix B: Methodology

### Severity Rating Definitions

| Rating | Definition |
|---|---|
| **S1** | Complete loss of certificate functionality; HTTPS interception broken for all users; tunnel cannot establish |
| **S2** | Certificate functionality degraded for specific platform, configuration, or user scenario; workaround available |
| **S3** | Minor certificate issue; edge case or cosmetic; does not block core functionality |

### Test Case Format

| Field | Description |
|---|---|
| **ID** | TC-13-NN format (chapter 13, sequential number) |
| **Test Case** | Description of what to test |
| **Severity** | S1-S3 impact if test fails |
| **Related Bugs** | ENG-XXXXXX references from escalation data |
| **Flow Point** | Which diagram node this test validates |
| **Gap Type** | Regression / Day-1 / Test Gap / Corner Case |
| **Auto Priority** | P1 (must automate) / P2 (should automate) / P3 (manual OK) |

### Gap Type Taxonomy

| Gap Type | Definition |
|---|---|
| **Regression** | Previously working feature broken by a code change |
| **Day-1** | Bug existed since feature was first implemented |
| **Test Gap** | No test case exists for this scenario |
| **Corner Case** | Scenario difficult to reproduce; environment-specific |

### Bug Cross-Reference Methodology

This chapter has 0 bugs filed directly under "Certificate Management" as a feature category. All 15 bugs were identified by searching across `bugs/install_upgrade.md` (54 bugs), `bugs/steering.md` (103 bugs), `bugs/tunneling.md` (59 bugs), and `bugs/failclose.md` (28 bugs) for any mention of: certificate, cert, SSL, TLS, HTTPS, pinned, CA, root cert, trust store, MITM, decrypt, nspubkey, nscacert, nstenantcert, nsusercert, policies.json, certutil, Firefox trust, Chrome trust, FedRAMP cert, DTLS.

---

**Related Chapters**:
- [01_installation.md](01_installation.md) -- Certificate installation during initial enrollment
- [02_enrollment.md](02_enrollment.md) -- Certificates provisioned during initial enrollment flow
- [04_config_download.md](04_config_download.md) -- Config download infrastructure shared by cert downloads
- [05_steering_config.md](05_steering_config.md) -- Cert-pinned app list as part of steering config
- [07_tunnel_management.md](07_tunnel_management.md) -- User certificate used for tunnel authentication; DTLS/TLS
- [10_bypass.md](10_bypass.md) -- Cert-pinned applications bypass SSL interception
- [11_failclose.md](11_failclose.md) -- FailClose interaction during CA rotation
- [12_device_classification.md](12_device_classification.md) -- Certificate-based device classification
- [14_proxy_management.md](14_proxy_management.md) -- Proxy + cert-pinned app interaction
- [18_security.md](18_security.md) -- Config encryption (encryptClientConfig) affecting cert file storage
