# Escalation Bug Review - Categorized

> Extracted from `Escalation Bug review.xlsx` on 2026-04-18

## Categories

| Category | File | Bug Count |
|----------|------|-----------|
| Install / Upgrade / Enrollment | [install_upgrade.md](install_upgrade.md) | 54 |
| Tunneling / Gateway | [tunneling.md](tunneling.md) | 59 |
| Steering / Bypass / Exception | [steering.md](steering.md) | 103 |
| FailClose / FailOpen | [failclose.md](failclose.md) | 28 |

**Unique bugs across all categories**: 174

*Note: Some bugs appear in multiple categories (e.g., a FailClose bug may also be tagged under Steering).*

## Quick Stats

### Install/Upgrade (54 bugs)

**By Platform**: Windows: 24, Mac: 8, Windows & Mac: 3, Linux: 2, Android: 1, iOS: 1, Backend: 1, Win: 1, Client Services (Backend): 1, ChromeOS: 1, 5.0: 1, 4.0: 1

**Regression**: Yes: 14, No: 19, Day-1: 9

**By Type**: Test Gap: 12, Missing in Regression: 5, Corner case: 5, Enhancement: 5, Corner case.: 3, Corner Case: 3, Test Gap : 2, Internal found: 2, Test Gap(Improve Platform Coverage): 1, Test Gap (Add more verification on Upgrade negative scenarios): 1, Test gap: 1, Test Gap - missing test case. Neither dev nor QE test it. : 1, Test Gap( Need to include more test on OTP backend): 1, Test Gap (Negative Scenario): 1

### Tunneling (59 bugs)

**By Platform**: Windows: 27, Android: 11, Mac: 6, Windows & Mac: 2, iOS: 1, ChromeOS: 1, Windows, Mac, Linux: 1, Windows, Mac: 1, Windows and Mac: 1, 5.0: 1, 2.0: 1

**Regression**: Yes: 21, No: 11, Day-1: 19

**By Type**: Test Gap: 11, Corner case: 9, Corner Case: 9, Enhancement: 7, Missing in Regression: 4, Internal found: 3, Corner case (needs to have scenarios which exposes the Crash issues): 2, Test Gap : 1, Test Gap.(Need to add DNS Tunnel health check up case for 1 hr duration): 1, Test Gap (NPA Integration): 1, Missing in Regression(bypassIpExceptionAtAndroidOs): 1, Missing in Regression ( If. this is automated, It should've been caught by automation.): 1, Missing in Regression(Negative Scenario): 1

### Steering (103 bugs)

**By Platform**: Windows: 44, Android: 14, Mac: 9, iOS: 5, Linux: 4, Windows & Mac: 3, Win: 2, ChromeOS: 2, Windows, Mac, Linux: 1, Provisioner Platform (Prov): 1, Backend: 1, All: 1, 16.0: 1, 6.0: 1, 4.0: 1, 1.0: 1

**Regression**: Yes: 21, No: 31, Day-1: 32

**By Type**: Corner case: 16, Enhancement: 16, Test Gap: 13, Corner Case: 11, Missing in Regression: 5, Internal found: 5, Missing in Regression : 1, Feature is not working as per the design.
Test Gap: 1, Test Gap( Test case never executed before due to GRE/IPsec setup limitation): 1, Test Gap(Need to add case for IPv6 Local IP): 1, Test Gap(Corner case and not easy to replicate, however it would be better to add test case to cover large TCP segments On Loopback, Steering and DNS security features).: 1, Test Gap(Custom ports with All traffic/Web mode - Steering and Bypass combination). Test it with Both TCP and UDP: 1, Corner case( Test case never executed before due to GRE/IPsec setup limitation): 1, Test Gap (Client service restart issue): 1, Test Gap(No setup to test this case): 1, Test Gap(Need to add Longivity/Stress test): 1, Missing in Regressions: 1, Test Gap( Need to inlude Native Apps and use regular expression on Cert pinned apps): 1, Test Gap.(Need to add DNS Tunnel health check up case for 1 hr duration): 1, Corner case(Need to include cases where DNS IP shuold be in Steering and Bypass list): 1, Test Gap - missing test case. Neither dev nor QE test it. : 1, Test Gap (NPA Integration): 1, Missing in Regression(bypassIpExceptionAtAndroidOs): 1, Missing in Regression ( If. this is automated, It should've been caught by automation.): 1, Security Fix / Corner Case: 1, Test-gap: 1

### FailClose (28 bugs)

**By Platform**: Windows: 18, Windows & Mac: 2, Win: 1, 5.0: 1

**Regression**: Yes: 4, No: 6, Day-1: 9

**By Type**: Test Gap: 8, Enhancement: 5, Corner Case: 3, Missing in Regression: 2, Missing in Regression : 1, Corner case(Log changefor fal-close): 1

