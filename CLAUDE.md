# Claude Code Instructions

## Project Overview

Bug-driven technical knowledge base for NSClient (Netskope Client) grey box testing. 174 escalation bugs mapped to 22 chapters with mermaid flow diagrams, test cases, and automation coverage.

**Language**: English only — all content, mermaid labels, narrative text.

## File Layout

```
chapters/      # 22 chapter files (00_overview.md through 21_watchdog.md)
bugs/          # Raw bug data (4 files: install_upgrade, steering, tunneling, failclose)
scripts/       # Python tooling for Confluence deployment and test case export
docs/          # Human-readable guides (playbook, template, methodology)
```

## Chapter Rules

### Bug Data Sources

| Type | Chapters | Source |
|------|----------|--------|
| Primary | 01, 05, 07, 11 | Dedicated `bugs/*.md` file |
| Cross-ref | All others | Bugs extracted from all 4 `bugs/*.md` files by topic relevance |

### Structure

Every chapter follows the template in `docs/chapter_template.md`. Key points:
- Narrative paragraphs precede every diagram
- Bug Quick Reference goes in **Appendix A** (end, not beginning)
- Platform sections: Windows → macOS → Linux → Android → iOS → ChromeOS → Backend

### Mermaid Diagrams

```
🔴 confirmed bug  → BUG_X["🔴 BUG ENG-XXXXXX<br/>description"]
🟡 predicted risk → RISK_X["🟡 Warning: description"]
Do NOT use style fill for bug/risk nodes (Confluence doesn't render them)
OK to use style fill for functional nodes: green (#4CAF50), blue (#2196F3)
```

### Code References

```
✅ lib/nsConfig/config.cpp::checkConfigVersion()
❌ config.cpp:1234  (never reference line numbers)
```

### Cross-References

```
✅ See [07. Tunnel Management](chapters/07_tunnel_management.md)
❌ See Chapter 7
```

## Test Case Format

| Column | Values |
|--------|--------|
| ID | TC-XX-NN |
| Severity | S1-S5 |
| Auto Priority | P1-P3 |
| Gap Type | Regression / Day-1 / Test Gap / Corner Case |

## Quality Checklist

After updating any chapter:
- [ ] Every 🔴 node has a real ENG-XXXXXX verifiable in `bugs/*.md`
- [ ] Every 🟡 node is covered by at least one test case
- [ ] Every diagram has a preceding narrative paragraph
- [ ] Platform sections cover at least Windows/macOS/Linux
- [ ] Bug Quick Reference is in Appendix A
- [ ] All content in English
- [ ] No line number references in code citations

## Key Terms

| Term | Meaning |
|------|---------|
| NSC / STAgent | Netskope Client |
| NPA | Netskope Private Access (ZTNA) |
| MP / DP | Management Plane / Data Plane |
| WFP / NE / VIF | Windows Filtering Platform / macOS Network Extension / Linux TUN |
| GSLB | Global Server Load Balancing (gateway selection) |
| FailClose | Block traffic when tunnel disconnects |
| SPDY | HTTP/2-like multiplexing protocol for tunnel |

## Confluence Deployment

```bash
cd scripts/
export CONFLUENCE_API_TOKEN="your-token"
python3 render_mermaid_and_convert.py XX    # single chapter
python3 render_mermaid_and_convert.py all   # all chapters
```

Page ID mapping:
```
00 → 7776206958    07 → 7775420785    14 → 7775223994
01 → 7775256801    08 → 7775453376    15 → 7773193015
02 → 7772898132    09 → 7775813750    16 → 7776305291
03 → 7776305272    10 → 7775912130    17 → 7774602055
04 → 7775715658    11 → 7775715680    18 → 7775781177
05 → 7775682854    12 → 7775715699    19 → 7775027357
06 → 7775191215    13 → 7775355168    20 → 7776141570
                                       21 → 7850557719
```
