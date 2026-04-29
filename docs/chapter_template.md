# Chapter Template

> Copy this template when starting a new chapter. Replace all `XX`, `N`, and placeholder text.

---

## Required Structure

Every chapter must follow this exact structure in this exact order.

```markdown
# XX. Chapter Title

**Escalation Bug Count**: N | **Regression**: N (%) | **Day-1**: N (%) | **Test Gap**: N (%)

> Brief description of what this chapter covers.

---

## Overview

Narrative introduction: what this feature does, why it matters, highest risks.
1-3 paragraphs of context before any diagrams.

---

## Shared Flow Name (All Platforms)

Narrative paragraph explaining this flow, what can go wrong, why it matters for testing.

    ```mermaid
    flowchart TD
        STEP1[Step One] --> STEP2[Step Two]
        STEP1 --> BUG_X["🔴 BUG ENG-XXXXXX<br/>description"]
        STEP2 --> RISK_Y["🟡 Warning: description"]
    ```

---

## Windows

**Bug Count**: N | **Key Gaps**: ...

Narrative introduction to Windows-specific behavior and risks.

### Windows Flow Name

Narrative paragraph before mermaid diagram.

    ```mermaid
    ...
    ```

### Windows Test Cases

| ID | Test Case | Severity | Auto Priority | Gap Type |
|----|-----------|----------|---------------|----------|
| TC-XX-01 | ... | S1 | P1 | ... |

---

## macOS

(Same sub-structure as Windows)

## Linux

(Same sub-structure as Windows)

## Android
## iOS
## ChromeOS
## Backend

---

## Cross-Platform Test Cases

| ID | Test Case | Severity | Auto Priority | Gap Type |
|----|-----------|----------|---------------|----------|

---

## Cross-Flow Interactions

### Interaction Name

Narrative + sequence/flow diagram showing multi-module failure scenarios.

### Cross-Flow Risk Matrix (Chapter-Relevant)

### Cross-Flow Test Cases

---

## Appendix A: Bug Quick Reference

Full bug lookup table — ALL bugs for this feature area.

| Bug ID | Summary | Platform | Root Cause | Severity |
|--------|---------|----------|------------|----------|

---

## Appendix B: Methodology

Severity rating definitions, test case format, gap type taxonomy.
```

---

## Mermaid Diagram Rules

| Element | How to Mark | Example |
|---------|-------------|---------|
| Confirmed bug | 🔴 emoji in node label | `BUG_X["🔴 BUG ENG-XXXXXX<br/>description"]` |
| Predicted risk | 🟡 emoji in node label | `RISK_Y["🟡 Warning: description"]` |
| Success endpoint | Green `style fill` | `style SUCCESS fill:#4CAF50,color:#fff` |
| Continue/tunnel | Blue `style fill` | `style TUNNEL fill:#2196F3,color:#fff` |
| Bug/risk nodes | **NO** `style fill` | Confluence doesn't render node coloring consistently |

---

## Test Case Format

Each test case must include all 5 columns:

| Column | Values | Description |
|--------|--------|-------------|
| ID | `TC-XX-NN` | Chapter number + sequence |
| Test Case | Free text | What to test |
| Severity | S1-S5 | Impact if bug exists |
| Auto Priority | P1-P3 | Automation urgency |
| Gap Type | Regression / Day-1 / Test Gap / Corner Case | How the gap was found |

---

## Code Reference Format

```
✅ lib/nsConfig/config.cpp::checkConfigVersion()
✅ stAgent/stAgentSvc/tunnelMgr.cpp
❌ config.cpp:1234        ← never reference line numbers
```

---

## Cross-Reference Format

```
✅ See [07. Tunnel Management](../chapters/07_tunnel_management.md)
❌ See Chapter 7           ← must use markdown links
```
