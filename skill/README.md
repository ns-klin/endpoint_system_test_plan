# Claude Code Skill: write-chapter

A reusable slash command that generates a complete chapter for the NSClient System Test Plan.

## What it does

When you type `/write-chapter 07`, Claude Code will:

1. Read all 4 bug data files and extract relevant bugs
2. Map each bug to the code flow step it affects
3. Build Mermaid flow diagrams annotated with bug failure points
4. Assemble a complete chapter following the project template
5. Run a quality checklist and fix issues

## Installation

Copy `write-chapter.md` into your Claude Code project commands directory:

```bash
# From the repo root
mkdir -p .claude/commands
cp skill/write-chapter.md .claude/commands/write-chapter.md
```

That's it. The skill is now available as `/project:write-chapter` in Claude Code.

> **Note**: The `.claude/commands/` directory is project-scoped. If you want the skill available across all projects, copy it to `~/.claude/commands/` instead — it will then appear as `/user:write-chapter`.

## Usage

```
/project:write-chapter 07
/project:write-chapter 11
/project:write-chapter 21
```

The argument is the chapter number (or chapter number + name). Claude Code will figure out the rest from the bug data files and template.

## Prerequisites

The skill expects this repo's directory structure:

```
├── bugs/           # 4 bug data files (required)
├── chapters/       # Output location for chapter files
├── docs/
│   └── chapter_template.md   # Structural template (required)
└── .claude/
    └── commands/
        └── write-chapter.md  # This skill
```

If you're using this skill in a different repo, make sure the `bugs/` and `docs/chapter_template.md` paths exist.

## Customization

The skill file is plain markdown — edit it to fit your workflow:

- **Add a code path**: If your client source code is at a known location, add it to Stage 2 so Claude reads the code directly
- **Change the template**: Edit `docs/chapter_template.md` to change the chapter structure, and the skill will follow it
- **Add a deploy step**: Append a Stage 6 that runs `python3 scripts/render_mermaid_and_convert.py XX` to auto-deploy to Confluence

## Related docs

- [docs/playbook.md](../docs/playbook.md) — Human-readable version of the same process
- [docs/chapter_template.md](../docs/chapter_template.md) — The structural template
- [docs/writing_methodology.md](../docs/writing_methodology.md) — How chapter 01 was built (the gold standard)
