# Chapter Writing Methodology

> How Chapter 01 (Installation & Upgrade) was built — the gold standard for all chapters.

---

## Data Sources

Every chapter draws from **verified data sources** — never from general knowledge or hallucinated content:

1. **Bug data files** in `bugs/` directory — The primary structured input. Each entry has a real ENG-XXXXXX Jira ID, platform, feature area, regression classification, bug type, and QE owner comments.
2. **Client source code** at `/Users/klin/Documents/PyLark/Development/client/` — For code flow analysis.
3. **Golden regression suite** at `/Users/klin/Documents/PyLark/Development/nsclient_golden_regression_suite/golden_regression/tests/` — For automation coverage mapping.

### Bug Data Files (4 primary sources)

| Bug Data File | Primary Chapter | Bug Count |
|---|---|---|
| `bugs/install_upgrade.md` | 01_installation.md | 54 |
| `bugs/steering.md` | 05_steering_config.md | 103 |
| `bugs/tunneling.md` | 07_tunnel_management.md | 59 |
| `bugs/failclose.md` | 11_failclose.md | 28 |

**RULE**: Chapters 01/05/07/11 use their dedicated bug file. All other chapters (00, 02-04, 06, 08-10, 12-20) cross-reference ALL 4 bug files for bugs that touch their topic area. Every ENG-XXXXXX must be verifiable in one of these 4 files.

---

## Step-by-Step: How Chapter 01 Was Built

### Step 1: Extract Real Bug IDs from bugs/install_upgrade.md

Read every entry in the bug data file. For each bug with a real ENG-XXXXXX ID, extract:
- Bug ID (e.g., ENG-446703)
- Platform (e.g., Windows)
- Feature area (e.g., Install & Upgrade)
- Bug description (from the **Description** field)
- Root cause (from the **Comments** field)
- Bug type (Regression, Day-1, Test Gap, Corner Case, etc.)
- Whether a test case is needed

**Chapter 01 used 28 unique bug IDs** from the 54 entries (some entries were summary/review notes, not actual bugs).

### Step 2: Map Bugs to Code Flows

For each bug, identify which code flow step it affects:
- ENG-446703 → MSI file pile-up → maps to "Auto-Upgrade Flow — Package Download" step
- ENG-497728 → Cache key collision → maps to "MSI Installation Flow — CA_GetNsbrandingJsonFile" step
- ENG-733657 → Self-Protection flag → maps to "Auto-Upgrade Flow — Upgrade Window Check" step

This mapping is derived from reading the bug's **Comments** field and cross-referencing with the client source code.

### Step 3: Build Mermaid Diagrams with Bug Annotations

Each diagram represents a real code flow (installation, upgrade, enrollment, etc.). Bug failure points are added as annotated nodes:

**Confirmed bugs (🔴 red) — use emoji in node label, no style fill:**
```mermaid
    BUG_BRAND["🔴 BUG ENG-497728<br/>Email/UPN cache key collision"]
```

**Predicted risks (🟡 yellow) — use emoji in node label, no style fill:**
```mermaid
    RISK_DRIVER["🟡 Warning: Error 1275<br/>Secure Boot/AV conflict"]
```

**Rules for bug annotation in mermaid:**
1. Every 🔴 node MUST have a real ENG-XXXXXX ID from the bug data file
2. 🟡 nodes are for predicted risks where NO known escalation bug exists but code analysis reveals potential
3. Node labels must include the emoji + bug ID + a short description
4. Do NOT use `style NODE fill:#FF6B6B` or `fill:#FFD93D` to paint bug/risk nodes — use 🔴/🟡 emoji in the label text instead (Confluence status diagrams don't support full-node coloring consistently)
5. Green nodes (`fill:#4CAF50,color:#fff`) for success/completion endpoints — these are functional markers, not bug markers, so `style` fill is OK
6. Blue nodes (`fill:#2196F3,color:#fff`) for continue/tunnel endpoints — `style` fill is OK

### Step 4: Create Supporting Tables

**Node Risk Assessment** — For every node in the main flow diagram:
| Node | Risk | Assessment |
|---|---|---|
| CA_GetNsbrandingJsonFile | 🔴 High | **ENG-497728** — Email/UPN cache key collision |
| CA_InstallDriver | 🟡 Medium | Predicted: driver signature + Secure Boot conflict |

**Confirmed Bug Mapping** — Links flow steps to known bugs:
| Flow Step | Known Bugs | Root Cause | Automation |
|---|---|---|---|
| FindRelatedProducts | ENG-446703 (MSI pile-up) | Registry residue | ❌ Not covered |

**Predicted Risk Points** — No known escalation, but code review suggests risk:
| Flow Step | Predicted Risk | Potential Impact | Automation |
|---|---|---|---|
| CA_InstallDriver | Driver signature + Secure Boot | Error 1275 | ❌ Not covered |

### Step 5: Create Platform Sections

Organize by platform, each with:
- Bug count specific to that platform
- Platform-specific flow diagrams (with bug annotations)
- Platform-specific bug tables
- Platform-specific test cases

**Platform order**: Windows → macOS → Linux → Android → iOS → ChromeOS → Backend

### Step 6: Write Test Cases

Every test case must reference **real bugs** from the data file:

```markdown
**TC-01-02: Upgrade During FailClose Active**

| Field | Value |
|---|---|
| **Severity** | S1 |
| **Related Bugs** | ENG-733657, ENG-895081 |
| **Flow Point** | Auto-Upgrade Flow — Launch Installer |
| **Gap Type** | Missing |
| **Automation Priority** | P1 |

**Preconditions**: FailClose enabled, tunnel disconnected
**Steps**: [numbered list]
**Expected Result**: [what should happen]
**Failure Indicators**: [grep patterns to check logs]
**Risk if Untested**: [consequence of not testing]
```

### Step 7: Add Cross-Flow Interactions

Identify bugs that span multiple feature areas (e.g., Installation + FailClose = ENG-733657). These go in the Cross-Flow section with:
- Risk matrix table
- Sequence/flow diagrams showing multi-module failure
- Cross-flow test cases

### Step 8: Build Appendix A (Bug Quick Reference)

ALL bugs from the data file that relate to this chapter, in a single lookup table at the end:

| Bug ID | Problem Summary | Root Cause | Fix | Platform |
|---|---|---|---|---|
| **ENG-446703** | MSI file pile-up | Residual MSI files not cleaned | Stronger negative scenario validation | Windows |

### Step 9: Add Appendix B (Methodology)

Standard severity and test case format definitions (same across all data-rich chapters).

---

## Quality Checklist

Before a data-rich chapter is complete:

- [ ] Every red mermaid node has a real ENG-XXXXXX ID from `bugs/*.md`
- [ ] Every yellow mermaid node is explicitly labeled as "predicted risk" (no bug ID)
- [ ] Mermaid styling: 🔴 emoji in node label for confirmed bugs, 🟡 emoji in node label for predicted risks — NO `style fill` for bug/risk nodes
- [ ] Node Risk Assessment table covers all diagram nodes
- [ ] Confirmed Bug Mapping table links flow steps → real bug IDs
- [ ] Test cases have Related Bugs field referencing real ENG-XXXXXX IDs
- [ ] Platform sections match platforms found in bug data
- [ ] Appendix A contains ALL bugs from the source data file
- [ ] Appendix B has standard methodology definitions
- [ ] All narrative paragraphs precede their corresponding diagrams
- [ ] No hallucinated bug IDs — every ENG-XXXXXX can be found in `bugs/*.md`

