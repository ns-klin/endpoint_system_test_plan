#!/usr/bin/env python3
"""
Split en/escalation_bug_flow_analysis.md into per-platform reports.
Each platform file includes:
1. Platform-specific executive summary
2. Bug Quick Reference filtered by platform
3. Flow diagrams with platform-filtered Bug Mapping tables
4. Test cases filtered by platform relevance
5. Cross-flow analysis (shared)
6. Filtered appendix
"""
import re
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.normpath(os.path.join(SCRIPT_DIR, '..'))
EN_DIR = os.path.join(PROJECT_ROOT, 'en')

SOURCE = os.path.join(EN_DIR, "escalation_bug_flow_analysis.md")
OUTPUT_DIR = EN_DIR

# Platform matching rules: which Platform column values belong to each platform
PLATFORM_MATCH = {
    "windows": ["Windows", "Win/Mac", "Win/Mac/Linux"],
    "macos":   ["macOS", "Mac", "Win/Mac", "Win/Mac/Linux"],
    "android": ["Android"],
    "ios":     ["iOS"],
    "linux":   ["Linux", "Win/Mac/Linux"],
    "chromeos": ["ChromeOS"],
    "backend": ["Backend"],
}

# Bug-to-platform mapping (from Section 2.5 Bug Quick Reference)
# Used to filter Bug Mapping tables in sections 3-7
BUG_PLATFORM = {
    "ENG-384041": ["Windows"],
    "ENG-393015": ["Windows"],
    "ENG-395253": ["Mac"],
    "ENG-398819": ["Windows"],
    "ENG-406879": ["Windows"],
    "ENG-420917": ["Win/Mac"],
    "ENG-422599": ["Windows"],
    "ENG-424991": ["Android"],
    "ENG-429034": ["Android"],
    "ENG-434019": ["Windows"],
    "ENG-438566": ["Windows"],
    "ENG-441957": ["Android"],
    "ENG-445563": ["Windows"],
    "ENG-446703": ["Windows"],
    "ENG-448002": ["Windows"],
    "ENG-450735": ["iOS"],
    "ENG-455132": ["Windows"],
    "ENG-456732": ["Windows"],
    "ENG-463329": ["Windows"],
    "ENG-466704": ["Windows"],
    "ENG-472565": ["macOS"],
    "ENG-482990": ["Win/Mac"],
    "ENG-487939": ["Windows"],
    "ENG-497728": ["Backend", "Windows", "macOS", "Android", "iOS", "Linux", "ChromeOS"],
    "ENG-503501": ["Windows"],
    "ENG-533221": ["Windows"],
    "ENG-533981": ["Android"],
    "ENG-543228": ["macOS"],
    "ENG-543661": ["Windows"],
    "ENG-548975": ["Win/Mac"],
    "ENG-551274": ["Windows"],
    "ENG-556081": ["Windows"],
    "ENG-557778": ["Windows"],
    "ENG-561500": ["Windows"],
    "ENG-570306": ["Windows"],
    "ENG-573164": ["Windows"],
    "ENG-587497": ["Windows"],
    "ENG-591721": ["Windows"],
    "ENG-591725": ["Win/Mac/Linux"],
    "ENG-592681": ["Android"],
    "ENG-593503": ["Windows"],
    "ENG-593814": ["Windows"],
    "ENG-595031": ["Windows"],
    "ENG-601667": ["Windows"],
    "ENG-608191": ["Backend"],
    "ENG-609001": ["Linux"],
    "ENG-624953": ["Windows"],
    "ENG-625957": ["Windows"],
    "ENG-637576": ["Windows"],
    "ENG-649593": ["Windows"],
    "ENG-652754": ["Android"],
    "ENG-654108": ["Windows"],
    "ENG-659009": ["Windows"],
    "ENG-671659": ["iOS"],
    "ENG-671884": ["macOS"],
    "ENG-680385": ["macOS"],
    "ENG-718498": ["Windows"],
    "ENG-726784": ["Windows"],
    "ENG-729176": ["Windows"],
    "ENG-733657": ["Windows"],
    "ENG-739968": ["Windows"],
    "ENG-742949": ["Windows"],
    "ENG-746099": ["macOS"],
    "ENG-750658": ["Windows"],
    "ENG-751720": ["Windows"],
    "ENG-752117": ["Windows"],
    "ENG-773191": ["macOS"],
    "ENG-782593": ["Backend"],
    "ENG-793442": ["Windows"],
    "ENG-795413": ["Windows"],
    "ENG-801565": ["Windows"],
    "ENG-805334": ["Windows"],
    "ENG-846555": ["Linux"],
    "ENG-851222": ["Windows"],
    "ENG-855335": ["Mac"],
    "ENG-872456": ["ChromeOS"],
    "ENG-895081": ["Windows"],
    "ENG-917549": ["Android"],
    "ENG-918131": ["Windows"],
    "ENG-918451": ["Windows"],
    "ENG-925894": ["Windows"],
    "ENG-928461": ["Windows"],
    "ENG-948106": ["Linux"],
    "ENG-949874": ["Windows"],
}

# Test case platform relevance
TC_PLATFORM = {
    "TC-01-01": ["windows"],
    "TC-01-02": ["windows"],
    "TC-01-03": ["windows", "macos"],
    "TC-01-04": ["windows"],
    "TC-01-05": ["windows", "macos"],
    "TC-01-06": ["macos"],
    "TC-01-07": ["windows"],
    "TC-01-08": ["linux"],
    "TC-01-09": ["windows", "macos"],
    "TC-01-10": ["windows"],
    "TC-01-11": ["windows", "macos", "android", "ios", "linux", "chromeos", "backend"],
    "TC-01-12": ["macos"],
    "TC-01-13": ["windows"],
    "TC-05-01": ["windows", "macos", "android", "linux"],
    "TC-05-02": ["windows", "macos", "android", "ios", "linux", "chromeos"],
    "TC-05-03": ["windows", "macos", "android", "ios", "linux", "chromeos"],
    "TC-05-04": ["windows", "macos", "android", "ios", "linux", "chromeos"],
    "TC-05-05": ["windows", "macos", "android", "ios", "linux"],
    "TC-05-06": ["windows", "macos", "android"],
    "TC-05-07": ["windows"],
    "TC-05-08": ["windows", "macos"],
    "TC-05-09": ["windows"],
    "TC-05-10": ["windows", "macos", "android", "ios", "linux", "chromeos"],
    "TC-05-11": ["windows", "backend"],
    "TC-05-12": ["windows", "macos", "android", "ios", "linux", "chromeos"],
    "TC-05-13": ["windows", "macos", "android", "ios", "linux", "chromeos"],
    "TC-05-14": ["windows", "macos", "android", "ios", "linux"],
    "TC-05-15": ["windows", "macos", "android", "ios", "linux", "chromeos"],
    "TC-05-16": ["windows"],
    "TC-05-17": ["windows", "macos", "android", "linux"],
    "TC-07-01": ["windows", "macos", "android", "linux"],
    "TC-07-02": ["windows", "macos"],
    "TC-07-03": ["windows", "macos", "android", "linux"],
    "TC-07-04": ["windows", "macos"],
    "TC-07-05": ["windows", "macos"],
    "TC-07-06": ["windows", "macos", "android"],
    "TC-07-07": ["windows"],
    "TC-07-08": ["windows", "macos", "android"],
    "TC-07-09": ["windows"],
    "TC-07-10": ["windows", "macos", "android", "linux"],
    "TC-07-11": ["windows", "macos", "android", "linux"],
    "TC-07-12": ["android"],
    "TC-11-01": ["windows", "macos"],
    "TC-11-02": ["windows", "macos"],
    "TC-11-03": ["windows", "macos"],
    "TC-11-04": ["windows", "macos"],
    "TC-11-05": ["windows", "macos"],
    "TC-11-06": ["windows"],
    "TC-11-07": ["windows", "macos"],
    "TC-11-08": ["windows", "macos", "android", "ios"],
    "TC-11-09": ["windows", "macos"],
    "TC-11-10": ["windows"],
    "TC-CF-01": ["windows", "macos", "android", "linux"],
    "TC-CF-02": ["windows"],
    "TC-CF-03": ["windows", "macos", "android"],
    "TC-CF-04": ["windows"],
    "TC-CF-05": ["windows", "macos"],
    "TC-CF-06": ["windows", "macos"],
    "TC-CF-07": ["windows"],
    "TC-CF-08": ["windows", "macos", "android", "ios", "linux", "chromeos"],
    "TC-CF-09": ["windows", "macos", "android", "linux"],
    "TC-CF-10": ["windows", "macos", "android", "linux"],
    "TC-CF-11": ["windows", "macos", "android", "linux"],
    "TC-CF-12": ["windows", "macos"],
    "TC-CF-13": ["windows", "macos", "android", "linux", "chromeos"],
}

PLATFORM_INFO = {
    "windows": {
        "name": "Windows",
        "pct": "46%",
        "key_gaps": "VDI scenarios, AOAC, Domain Controller, Self-Protection + Upgrade",
        "bug_count_approx": "~80",
    },
    "macos": {
        "name": "macOS",
        "pct": "10%",
        "key_gaps": "System Extension restart, AOAC/Dark Wake, DHCP interop, Uninstall status",
        "bug_count_approx": "~18",
    },
    "android": {
        "name": "Android",
        "pct": "15%",
        "key_gaps": "Network state machine, NPA integration, Tunnel flapping, Stuck Connecting",
        "bug_count_approx": "~26",
    },
    "ios": {
        "name": "iOS",
        "pct": "4%",
        "key_gaps": "IPv6 DNS handling, NPA integration, Steering coverage",
        "bug_count_approx": "~7",
    },
    "linux": {
        "name": "Linux",
        "pct": "3%",
        "key_gaps": "Large domain crash, /tmp noexec installation, SELinux hardening, auto-upgrade",
        "bug_count_approx": "~5",
    },
    "chromeos": {
        "name": "ChromeOS",
        "pct": "2%",
        "key_gaps": "Large domain steering config crash, NPA bypass",
        "bug_count_approx": "~3",
    },
    "backend": {
        "name": "Backend",
        "pct": "3%",
        "key_gaps": "JWT signature validation, AV name regex, Branding cache key collision",
        "bug_count_approx": "~5",
    },
}


def read_source():
    with open(SOURCE, 'r', encoding='utf-8') as f:
        return f.read()


def platform_matches(platform_col, target_platform):
    """Check if a table cell's Platform value matches the target platform."""
    col = platform_col.strip()
    return col in PLATFORM_MATCH.get(target_platform, [])


def bug_matches_platform(eng_id, target_platform):
    """Check if a bug ID belongs to the target platform."""
    if eng_id not in BUG_PLATFORM:
        return True  # Unknown bug, keep it
    bug_plats = BUG_PLATFORM[eng_id]
    for bp in bug_plats:
        if bp in PLATFORM_MATCH.get(target_platform, []):
            return True
    return False


def row_has_platform_relevant_bug(row, target_platform):
    """Check if a Bug Mapping table row contains a bug relevant to this platform."""
    eng_ids = re.findall(r'ENG-\d+', row)
    if not eng_ids:
        return True  # No ENG- reference (e.g. predicted risk rows), keep it
    return any(bug_matches_platform(eid, target_platform) for eid in eng_ids)


def filter_bug_table(table_lines, target_platform):
    """Filter a markdown table by Platform column."""
    if len(table_lines) < 3:
        return table_lines
    header = table_lines[0]
    separator = table_lines[1]

    cols = [c.strip() for c in header.split('|')]
    platform_idx = None
    for i, c in enumerate(cols):
        if c in ('Platform', '----------'):
            platform_idx = i
            break

    if platform_idx is None:
        return table_lines

    filtered = [header, separator]
    for row in table_lines[2:]:
        cells = row.split('|')
        if platform_idx < len(cells):
            if platform_matches(cells[platform_idx], target_platform):
                filtered.append(row)

    return filtered


def filter_appendix_a_table(table_lines, target_platform):
    """Filter Appendix A tables by Platform column."""
    if len(table_lines) < 3:
        return table_lines
    header = table_lines[0]
    separator = table_lines[1]

    cols = [c.strip() for c in header.split('|')]
    platform_idx = None
    for i, c in enumerate(cols):
        if 'Platform' in c:
            platform_idx = i
            break

    if platform_idx is None:
        return table_lines

    filtered = [header, separator]
    for row in table_lines[2:]:
        cells = row.split('|')
        if platform_idx < len(cells):
            if platform_matches(cells[platform_idx], target_platform):
                filtered.append(row)

    return filtered


def filter_bug_mapping_table(table_lines, target_platform):
    """Filter Bug Mapping tables in sections 3-7 by bug platform relevance."""
    if len(table_lines) < 3:
        return table_lines
    header = table_lines[0]
    separator = table_lines[1]

    filtered = [header, separator]
    for row in table_lines[2:]:
        if row_has_platform_relevant_bug(row, target_platform):
            filtered.append(row)

    return filtered


def get_bug_platform_label(eng_id):
    """Get a human-readable platform label for a bug."""
    if eng_id not in BUG_PLATFORM:
        return None
    plats = BUG_PLATFORM[eng_id]
    return "/".join(plats)


def filter_node_risk_table(table_lines, target_platform):
    """Filter Node Risk Assessment table: downgrade off-platform bugs from High to Medium."""
    if len(table_lines) < 3:
        return table_lines
    info = PLATFORM_INFO[target_platform]
    header = table_lines[0]
    separator = table_lines[1]
    filtered = [header, separator]

    for row in table_lines[2:]:
        eng_ids = re.findall(r'ENG-\d+', row)
        if eng_ids and '🔴 High' in row and '**Bug**:' in row:
            all_off_platform = all(
                not bug_matches_platform(eid, target_platform)
                for eid in eng_ids
            )
            if all_off_platform:
                plat_label = get_bug_platform_label(eng_ids[0]) or "other"
                new_row = row.replace('🔴 High', '🟡 Medium')
                new_row = new_row.replace('**Bug**:', f'**Bug on {plat_label}**:')
                filtered.append(new_row)
                continue
        filtered.append(row)

    return filtered


def extract_tc_id(line):
    """Extract test case ID like TC-01-01 from a line."""
    m = re.search(r'(TC-(?:\d{2}-\d{2}|CF-\d{2}))', line)
    return m.group(1) if m else None


def is_bug_mapping_header(line):
    """Detect Bug Mapping, Predicted Risk, or Critical Bug Concentration headers."""
    return (line.startswith('**Bug Mapping') or
            line.startswith('**Predicted Risk Points') or
            line.startswith('**Critical Bug Concentration'))


def filter_mermaid_block(mermaid_lines, target_platform):
    """Filter platform-specific content within mermaid blocks."""
    filtered = []
    skip_subgraph = False
    skip_styles = set()

    # Platform prefix mapping for section 4.6
    platform_prefixes = {
        "windows": "W_",
        "macos": "M_",
        "linux": "L_",
        "android": "A_",
        "ios": "I_",
    }
    platform_subgraph_names = {
        "windows": "Windows",
        "macos": "macOS",
        "linux": "Linux",
        "android": "Android",
        "ios": "iOS",
    }

    is_coverage_matrix = any('subgraph Windows' in l for l in mermaid_lines)
    has_launchd = any('launchd' in l for l in mermaid_lines)

    if is_coverage_matrix:
        # Section 4.6: only keep the relevant platform subgraph + all styles
        relevant_name = platform_subgraph_names.get(target_platform)
        relevant_prefix = platform_prefixes.get(target_platform)

        if not relevant_name:
            # ChromeOS/Backend: not in the matrix, skip entire diagram
            return None

        in_relevant = False
        in_any_subgraph = False
        for line in mermaid_lines:
            stripped = line.strip()
            if stripped.startswith('subgraph '):
                sg_name = stripped[len('subgraph '):]
                if sg_name == relevant_name:
                    in_relevant = True
                    in_any_subgraph = True
                    filtered.append(line)
                else:
                    in_any_subgraph = True
                    in_relevant = False
                continue
            if stripped == 'end' and in_any_subgraph:
                if in_relevant:
                    filtered.append(line)
                in_any_subgraph = False
                in_relevant = False
                continue
            if in_relevant:
                filtered.append(line)
            elif not in_any_subgraph:
                # Keep lines outside subgraphs (graph TB, styles for relevant prefix)
                if stripped.startswith('style '):
                    if relevant_prefix and relevant_prefix in stripped:
                        filtered.append(line)
                else:
                    filtered.append(line)
        return filtered

    if has_launchd:
        # Section 3.2: filter macOS-specific lines for non-macOS
        for line in mermaid_lines:
            if 'launchd' in line or 'ENG-472565' in line:
                if target_platform in ('macos',):
                    filtered.append(line)
                # Skip for other platforms
            else:
                filtered.append(line)
        return filtered

    return mermaid_lines  # No filtering needed


def generate_platform_report(content, target_platform):
    """Generate a platform-specific report."""
    info = PLATFORM_INFO[target_platform]
    lines = content.split('\n')
    output_lines = []

    i = 0
    in_table = False
    table_buffer = []
    skip_tc = False

    in_section_25 = False
    in_appendix_a = False
    in_bug_mapping = False
    in_node_risk = False
    in_mermaid = False
    mermaid_buffer = []
    in_section_81 = False
    in_section_82 = False
    in_section_81_table = False
    in_section_82_table = False

    while i < len(lines):
        line = lines[i]

        # Replace title
        if i == 0 and line.startswith('# '):
            output_lines.append(f"# {info['name']} — Escalation Bug & Critical Code Flow Cross-Analysis")
            output_lines.append('')
            output_lines.append(f"**Platform Focus**: {info['name']} ({info['pct']} of total bugs)")
            output_lines.append(f"**Key Gaps**: {info['key_gaps']}")
            output_lines.append('')
            article = "an" if info['name'][0] in 'AEIOUaeiou' else "a"
            output_lines.append(f"> This report is {article} **{info['name']}-specific extract** from the full cross-analysis report.")
            output_lines.append(f"> Flow diagrams show the complete code logic (shared across all platforms) with bug annotations filtered for {info['name']} relevance.")
            output_lines.append(f"> Bug tables and test cases are filtered for {info['name']}.")
            i += 1
            while i < len(lines) and not lines[i].startswith('---'):
                i += 1
            output_lines.append('')
            output_lines.append('---')
            i += 1
            continue

        # Track section context
        if '## 2.5 Bug Quick Reference' in line:
            in_section_25 = True
            output_lines.append(line)
            i += 1
            continue

        if in_section_25 and line.startswith('## 3.'):
            in_section_25 = False

        if '## Appendix A' in line:
            in_appendix_a = True
        if in_appendix_a and line.startswith('## Appendix B'):
            in_appendix_a = False

        # Handle mermaid blocks
        if line.strip() == '```mermaid':
            in_mermaid = True
            mermaid_buffer = []
            i += 1
            continue

        if in_mermaid:
            if line.strip() == '```':
                in_mermaid = False
                filtered = filter_mermaid_block(mermaid_buffer, target_platform)
                if filtered is not None:
                    output_lines.append('```mermaid')
                    output_lines.extend(filtered)
                    output_lines.append('```')
                else:
                    output_lines.append(f'> *Platform coverage matrix not applicable to {info["name"]}.*')
                mermaid_buffer = []
            else:
                mermaid_buffer.append(line)
            i += 1
            continue

        # Detect Node Risk Assessment headers (in sections 3-7)
        if '**Node Risk Assessment**' in line and not in_section_25 and not in_appendix_a:
            in_node_risk = True
            output_lines.append(line)
            i += 1
            continue

        # Filter Node Risk Assessment tables: downgrade off-platform bugs
        if in_node_risk and '|' in line and line.strip().startswith('|'):
            if not in_table:
                in_table = True
                table_buffer = []
            table_buffer.append(line)

            if i + 1 >= len(lines) or not lines[i + 1].strip().startswith('|'):
                filtered = filter_node_risk_table(table_buffer, target_platform)
                output_lines.extend(filtered)
                in_table = False
                table_buffer = []
                in_node_risk = False
            i += 1
            continue

        if in_node_risk and not line.strip().startswith('|') and line.strip() != '':
            in_node_risk = False

        # Detect Bug Mapping / Predicted Risk headers (in sections 3-7)
        if is_bug_mapping_header(line) and not in_section_25 and not in_appendix_a:
            in_bug_mapping = True
            output_lines.append(line)
            i += 1
            continue

        # Filter Bug Mapping tables in sections 3-7
        if in_bug_mapping and '|' in line and line.strip().startswith('|'):
            if not in_table:
                in_table = True
                table_buffer = []
            table_buffer.append(line)

            if i + 1 >= len(lines) or not lines[i + 1].strip().startswith('|'):
                filtered = filter_bug_mapping_table(table_buffer, target_platform)
                if len(filtered) > 2:
                    output_lines.extend(filtered)
                else:
                    output_lines.append(f'*No {info["name"]}-relevant bugs at this flow point.*')
                in_table = False
                table_buffer = []
                in_bug_mapping = False
            i += 1
            continue

        if in_bug_mapping and not line.strip().startswith('|') and line.strip() != '':
            if not line.strip().startswith('|'):
                in_bug_mapping = False
                # Fall through to normal processing

        # Filter tables in Bug Quick Reference (section 2.5) and Appendix A
        if (in_section_25 or in_appendix_a) and '|' in line and line.strip().startswith('|'):
            if not in_table:
                in_table = True
                table_buffer = []
            table_buffer.append(line)

            if i + 1 >= len(lines) or not lines[i + 1].strip().startswith('|'):
                if in_section_25:
                    filtered = filter_bug_table(table_buffer, target_platform)
                else:
                    filtered = filter_appendix_a_table(table_buffer, target_platform)

                if len(filtered) > 2:
                    output_lines.extend(filtered)
                else:
                    output_lines.append(f'*No {info["name"]}-specific bugs in this category.*')

                in_table = False
                table_buffer = []

            i += 1
            continue

        if in_table:
            in_table = False
            if table_buffer:
                if in_section_25:
                    filtered = filter_bug_table(table_buffer, target_platform)
                elif in_appendix_a:
                    filtered = filter_appendix_a_table(table_buffer, target_platform)
                else:
                    filtered = filter_bug_mapping_table(table_buffer, target_platform)
                if len(filtered) > 2:
                    output_lines.extend(filtered)
                table_buffer = []

        # Track section 8.1 and 8.2
        if '### 8.1 Top 20' in line:
            in_section_81 = True
            in_section_82 = False
            output_lines.append(line)
            i += 1
            continue
        if '### 8.2 Platform Coverage Gap' in line:
            in_section_81 = False
            in_section_82 = True
            output_lines.append(line)
            i += 1
            continue
        if line.startswith('### 8.3'):
            in_section_81 = False
            in_section_82 = False

        # Filter Section 8.1 Top 20 table by TC_PLATFORM
        if in_section_81 and '|' in line and line.strip().startswith('|'):
            if not in_section_81_table:
                in_section_81_table = True
                table_buffer = []
            table_buffer.append(line)
            if i + 1 >= len(lines) or not lines[i + 1].strip().startswith('|'):
                header = table_buffer[0]
                sep = table_buffer[1]
                filtered = [header, sep]
                for row in table_buffer[2:]:
                    tc_id = extract_tc_id(row)
                    if tc_id is None or target_platform in TC_PLATFORM.get(tc_id, []):
                        filtered.append(row)
                if len(filtered) > 2:
                    output_lines.extend(filtered)
                else:
                    output_lines.append(f'*No {info["name"]}-relevant test cases in top 20.*')
                in_section_81_table = False
                table_buffer = []
            i += 1
            continue

        # Filter Section 8.2 Platform Coverage Gap to show only this platform
        if in_section_82 and '|' in line and line.strip().startswith('|'):
            if not in_section_82_table:
                in_section_82_table = True
                table_buffer = []
            table_buffer.append(line)
            if i + 1 >= len(lines) or not lines[i + 1].strip().startswith('|'):
                header = table_buffer[0]
                sep = table_buffer[1]
                filtered = [header, sep]
                for row in table_buffer[2:]:
                    if f'**{info["name"]}**' in row:
                        filtered.append(row)
                if len(filtered) > 2:
                    output_lines.extend(filtered)
                else:
                    output_lines.append(f'| **{info["name"]}** | {info["pct"]} | {info["key_gaps"]} |')
                in_section_82_table = False
                table_buffer = []
            i += 1
            continue

        # Detect test case blocks
        tc_match = re.match(r'^\*\*(TC-(?:\d{2}-\d{2}|CF-\d{2})):.*\*\*', line)
        if tc_match:
            tc_id = tc_match.group(1)
            applicable = TC_PLATFORM.get(tc_id, [])

            if target_platform in applicable:
                skip_tc = False
                output_lines.append(line)
            else:
                skip_tc = True
            i += 1
            continue

        if skip_tc:
            if re.match(r'^## \d|^## Appendix|^\*\*TC-', line):
                skip_tc = False
                continue
            elif line.strip() == '---':
                i += 1
                continue
            i += 1
            continue

        output_lines.append(line)
        i += 1

    return '\n'.join(output_lines)


def count_items(report, target_platform):
    """Count filtered bugs and test cases."""
    bug_count = len(re.findall(r'\| \*\*ENG-\d+\*\*', report))
    tc_count = len(re.findall(r'\*\*TC-(?:\d{2}-\d{2}|CF-\d{2}):', report))
    return bug_count, tc_count


def main():
    content = read_source()

    for platform in ['windows', 'macos', 'android', 'ios', 'linux', 'chromeos', 'backend']:
        info = PLATFORM_INFO[platform]
        report = generate_platform_report(content, platform)

        bug_count, tc_count = count_items(report, platform)

        outfile = os.path.join(OUTPUT_DIR, f"escalation_bug_flow_{platform}.md")
        with open(outfile, 'w', encoding='utf-8') as f:
            f.write(report)

        line_count = report.count('\n') + 1
        print(f"  {platform:10s}: {outfile} ({line_count} lines, {bug_count} bugs, {tc_count} test cases)")

    print("\nDone! Files generated in en/ directory.")


if __name__ == '__main__':
    main()
