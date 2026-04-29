You are writing a chapter for the NSClient System Test Plan. The target chapter is: $ARGUMENTS

Follow these stages in order. Complete each stage fully before moving to the next.

---

## Stage 1: Identify Data Sources

1. Read all 4 bug data files: `bugs/install_upgrade.md`, `bugs/steering.md`, `bugs/tunneling.md`, `bugs/failclose.md`
2. Determine which file is the **primary source** for this chapter:
   - Chapter 01 → `bugs/install_upgrade.md`
   - Chapter 05 → `bugs/steering.md`
   - Chapter 07 → `bugs/tunneling.md`
   - Chapter 11 → `bugs/failclose.md`
   - All other chapters → cross-reference ALL 4 files for topic-relevant bugs
3. Extract every entry with a real ENG-XXXXXX ID. For each bug, record: Bug ID, Platform, Description, Root Cause, Classification (Regression / Day-1 / Test Gap / Corner Case)
4. Skip entries without real bug IDs — they are summary or review notes

Report how many bugs you found before continuing.

---

## Stage 2: Map Bugs to Code Flows

For each extracted bug:
1. Read the root cause from the bug data
2. Identify which code module and function it affects in the client source code
3. Determine which flow step it breaks (e.g., "Auto-Upgrade Flow → Package Download")
4. Note the expected vs actual behavior

Also identify **predicted risks**: code paths where analysis reveals potential failure but no escalation bug exists yet. These will become 🟡 Warning nodes.

Report your bug-to-flow mapping before continuing.

---

## Stage 3: Build Mermaid Diagrams

Create flow diagrams modeling real code paths. Annotate with bug failure points:

- Confirmed bugs: `BUG_X["🔴 BUG ENG-XXXXXX<br/>description"]`
- Predicted risks: `RISK_X["🟡 Warning: description"]`
- Do NOT use `style fill` for bug/risk nodes
- OK to use `style fill` for functional endpoints: green (`#4CAF50`) for success, blue (`#2196F3`) for continue/tunnel

Split complex flows into multiple smaller diagrams rather than one giant diagram — Mermaid rendering fails on overly complex graphs.

---

## Stage 4: Assemble the Chapter

Read the template at `docs/chapter_template.md` and follow its structure exactly. Write the chapter file at `chapters/XX_name.md`.

Key rules:
- Write a narrative paragraph BEFORE every diagram — explain what it shows and why it matters
- Organize platform sections in order: Windows → macOS → Linux → Android → iOS → ChromeOS → Backend
- Every test case must include: ID (TC-XX-NN), Test Case, Severity (S1-S5), Auto Priority (P1-P3), Gap Type
- Bug Quick Reference table goes in **Appendix A** at the end
- All content in **English only** — including Mermaid node labels and edge labels
- Code references: `lib/module/file.cpp::functionName()` — never reference line numbers
- Cross-references: use markdown links like `[07. Tunnel Management](07_tunnel_management.md)`

---

## Stage 5: Quality Review

Check every item. Fix any failures before reporting done.

- [ ] Every 🔴 node has a real ENG-XXXXXX that exists in `bugs/*.md`
- [ ] Every 🟡 node is covered by at least one TC-XX-NN test case
- [ ] Every diagram has a preceding narrative paragraph
- [ ] Platform sections cover at least Windows / macOS / Linux
- [ ] Test cases have Severity, Auto Priority, and Gap Type columns
- [ ] Bug Quick Reference is in Appendix A (at the end, not the beginning)
- [ ] All content is in English
- [ ] No line number references in code citations
- [ ] No hallucinated bug IDs — every ENG-XXXXXX can be grep'd in `bugs/*.md`

Report what you wrote and any issues found.
