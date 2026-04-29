# NSClient System Test Plan

A bug-driven knowledge base for Netskope Client (NSClient) grey box testing. 174 customer escalation bugs mapped to code flow diagrams, testing gaps identified, test cases proposed.

## What's in here

**22 chapters** covering every major NSClient subsystem. Each chapter contains:
- Mermaid flow diagrams annotated with known bug failure points
- Platform-specific analysis (Windows, macOS, Linux, Android, iOS, ChromeOS)
- Test cases derived from real escalation data
- Cross-flow interaction analysis

**4 bug data files** with raw escalation ticket data:

| File | Feature Area | Bugs |
|------|-------------|------|
| [install_upgrade.md](bugs/install_upgrade.md) | Installation & Upgrade | 54 |
| [steering.md](bugs/steering.md) | Steering Config | 103 |
| [tunneling.md](bugs/tunneling.md) | Tunnel Management | 59 |
| [failclose.md](bugs/failclose.md) | FailClose | 28 |

## Chapters

### Core Architecture & Lifecycle
| # | Chapter | Bugs |
|---|---------|------|
| [00](chapters/00_overview.md) | Architecture Overview | — |
| [01](chapters/01_installation.md) | Installation & Upgrade | **54** |
| [02](chapters/02_enrollment.md) | Enrollment | cross-ref |
| [03](chapters/03_service_lifecycle.md) | Service Lifecycle | cross-ref |

### Config & MP Interaction
| # | Chapter | Bugs |
|---|---------|------|
| [04](chapters/04_config_download.md) | Config Download & Management | cross-ref |
| [05](chapters/05_steering_config.md) | Steering Config | **103** |
| [06](chapters/06_client_status.md) | Client Status Reporting | cross-ref |

### Tunnel & Traffic
| # | Chapter | Bugs |
|---|---------|------|
| [07](chapters/07_tunnel_management.md) | Tunnel Management | **59** |
| [08](chapters/08_gateway_selection.md) | Gateway Selection (GSLB) | cross-ref |
| [09](chapters/09_traffic_steering.md) | Traffic Interception & Packets | cross-ref |
| [10](chapters/10_bypass.md) | Bypass Mechanisms | cross-ref |

### Security & Advanced Features
| # | Chapter | Bugs |
|---|---------|------|
| [11](chapters/11_failclose.md) | FailClose | **28** |
| [12](chapters/12_device_classification.md) | Device Classification | cross-ref |
| [13](chapters/13_certificate_management.md) | Certificate Management | cross-ref |
| [14](chapters/14_proxy_management.md) | Proxy Detection & Management | cross-ref |

### Integration & Other
| # | Chapter | Bugs |
|---|---------|------|
| [15](chapters/15_npa_integration.md) | NPA (Private Access) | cross-ref |
| [16](chapters/16_dem.md) | DEM | cross-ref |
| [17](chapters/17_ipc_nscom2.md) | IPC (NSCom2/NSMsg2) | cross-ref |
| [18](chapters/18_security.md) | Security Mechanisms | cross-ref |
| [19](chapters/19_integration_architecture.md) | Multi-Component Integration | cross-ref |
| [20](chapters/20_supportability.md) | Supportability | cross-ref |
| [21](chapters/21_watchdog.md) | Watchdog | cross-ref |

> Chapters with **bold bug counts** have dedicated bug data. "cross-ref" chapters pull relevant bugs from all 4 bug data files.

## Bug Statistics

| Feature Area | Bugs | Regression | Day-1 | Test Gap | Corner Case |
|---|---|---|---|---|---|
| Install / Upgrade | 54 | 14 (26%) | 9 (17%) | 12 (22%) | 8 (15%) |
| Steering | 103 | 21 (20%) | 32 (31%) | 13 (13%) | 27 (26%) |
| Tunneling | 59 | 21 (36%) | 19 (32%) | 11 (19%) | 18 (31%) |
| FailClose | 28 | 4 (14%) | 9 (32%) | 8 (29%) | 3 (11%) |

37 bugs (21%) span multiple categories — cross-flow interactions are the largest testing gap.

## How to reproduce this work

See **[docs/playbook.md](docs/playbook.md)** — the step-by-step guide for writing a chapter from scratch, including the exact prompt sequence for Claude Code.

Supporting docs:
- [docs/chapter_template.md](docs/chapter_template.md) — the structural template every chapter follows
- [docs/writing_methodology.md](docs/writing_methodology.md) — how chapter 01 was built (the gold standard)

## Deploying to Confluence

```bash
cd scripts/
export CONFLUENCE_API_TOKEN="your-token"
python3 render_mermaid_and_convert.py 01       # single chapter
python3 render_mermaid_and_convert.py 01 05 07  # multiple chapters
python3 render_mermaid_and_convert.py all       # all chapters
```

## Claude Code Skill

If you use Claude Code, you can install the `/write-chapter` skill to generate chapters via slash command:

```bash
mkdir -p .claude/commands
cp skill/write-chapter.md .claude/commands/write-chapter.md
```

Then use it:
```
/project:write-chapter 07
```

See [skill/README.md](skill/README.md) for details.

## Repo Structure

```
├── README.md                 # This file
├── CLAUDE.md                 # Claude Code machine instructions
├── chapters/                 # 22 chapter files (00-21)
├── bugs/                     # Raw escalation bug data (4 files)
├── scripts/                  # Confluence deployment & export tools
├── docs/
│   ├── playbook.md           # How to write a chapter (human guide)
│   ├── chapter_template.md   # Chapter structure template
│   └── writing_methodology.md # How chapter 01 was built
└── skill/
    ├── README.md             # Skill installation & usage guide
    └── write-chapter.md      # Claude Code slash command file
```
