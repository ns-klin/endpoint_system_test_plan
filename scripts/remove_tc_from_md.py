#!/usr/bin/env python3
"""
Remove TC definitions from markdown chapters.
Preserves all other content (narrative, diagrams, bug tables, etc.).

Handles three TC formats:
1. Detailed: **TC-XX-XX: Title** blocks with metadata tables
2. Table: | TC-XX-XX | ... | rows within ### Test Cases sections
3. Heading: ### TC-XX-XX: Title blocks

Also removes:
- ### XX Test Cases subsections (header + table)
- ## Cross-Platform Test Cases sections
- ### Cross-Flow Test Cases subsections
"""

import re
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.normpath(os.path.join(SCRIPT_DIR, '..'))
CHAPTERS_DIR = os.path.join(PROJECT_ROOT, 'chapters')

CHAPTERS = [
    "01_installation.md",
    "02_enrollment.md",
    "03_service_lifecycle.md",
    "04_config_download.md",
    "05_steering_config.md",
    "06_client_status.md",
    "07_tunnel_management.md",
    "08_gateway_selection.md",
    "09_traffic_steering.md",
    "10_bypass.md",
    "11_failclose.md",
    "12_device_classification.md",
    "13_certificate_management.md",
    "14_proxy_management.md",
    "15_npa_integration.md",
    "16_dem.md",
    "17_ipc_nscom2.md",
    "18_security.md",
    "19_integration_architecture.md",
    "20_supportability.md",
    "21_watchdog.md",
]

# Section headers that contain TC definitions
TC_SECTION_PATTERNS = [
    r'^###\s+.*Test Cases\s*$',           # ### Windows Test Cases, ### Cross-Flow Test Cases, etc.
    r'^##\s+Cross-Platform Test Cases\s*$', # ## Cross-Platform Test Cases
]


def find_section_end(lines, start_idx):
    """Find end of a section (next heading at same or higher level, or EOF)."""
    start_line = lines[start_idx]
    start_level = len(start_line) - len(start_line.lstrip('#'))

    for i in range(start_idx + 1, len(lines)):
        line = lines[i]
        if line.startswith('#'):
            level = len(line) - len(line.lstrip('#'))
            if level <= start_level:
                return i
    return len(lines)


def remove_tc_sections(content):
    """Remove all TC definition sections from content."""
    lines = content.split('\n')
    remove_ranges = []

    for i, line in enumerate(lines):
        for pattern in TC_SECTION_PATTERNS:
            if re.match(pattern, line):
                end = find_section_end(lines, i)
                # Also remove trailing blank lines and --- separators
                while end < len(lines) and (lines[end].strip() == '' or lines[end].strip() == '---'):
                    end += 1
                remove_ranges.append((i, end))
                break

    # Also find ## Cross-Platform Test Cases
    for i, line in enumerate(lines):
        if re.match(r'^##\s+Cross-Platform Test Cases', line):
            end = find_section_end(lines, i)
            while end < len(lines) and (lines[end].strip() == '' or lines[end].strip() == '---'):
                end += 1
            remove_ranges.append((i, end))

    # Merge overlapping ranges
    remove_ranges.sort()
    merged = []
    for start, end in remove_ranges:
        if merged and start <= merged[-1][1]:
            merged[-1] = (merged[-1][0], max(merged[-1][1], end))
        else:
            merged.append((start, end))

    # Build result excluding removed ranges
    keep = []
    pos = 0
    for start, end in merged:
        keep.extend(lines[pos:start])
        pos = end
    keep.extend(lines[pos:])

    return '\n'.join(keep)


def remove_detailed_tc_blocks(content):
    """Remove **TC-XX-XX: Title** detailed blocks that may exist outside sections."""
    # Match from **TC-XX-XX: to next **TC- or next ## heading or ---
    pattern = re.compile(
        r'\*\*(TC-(?:CF-)?\d{2}-\d{2}):\s*.+?\*\*'
        r'.*?'
        r'(?=\*\*TC-(?:CF-)?\d{2}-\d{2}:|^#{2,3}\s|\Z|^---\s*$)',
        re.DOTALL | re.MULTILINE
    )
    return pattern.sub('', content)


def remove_heading_tc_blocks(content):
    """Remove ### TC-XX-XX: Title heading blocks (Ch04 style)."""
    lines = content.split('\n')
    remove_ranges = []

    for i, line in enumerate(lines):
        if re.match(r'^###\s+TC-\d{2}-\d{2}:', line):
            end = find_section_end(lines, i)
            while end < len(lines) and (lines[end].strip() == '' or lines[end].strip() == '---'):
                end += 1
            remove_ranges.append((i, end))

    if not remove_ranges:
        return content

    remove_ranges.sort()
    keep = []
    pos = 0
    for start, end in remove_ranges:
        keep.extend(lines[pos:start])
        pos = end
    keep.extend(lines[pos:])
    return '\n'.join(keep)


def cleanup_empty_sections(content):
    """Remove sections that became empty after TC removal."""
    # Clean up multiple consecutive blank lines (3+ -> 2)
    content = re.sub(r'\n{4,}', '\n\n\n', content)
    # Clean up --- followed by blank then ---
    content = re.sub(r'---\s*\n\s*\n\s*---', '---', content)
    return content


def process_chapter(filename):
    filepath = os.path.join(CHAPTERS_DIR, filename)
    if not os.path.exists(filepath):
        return 0

    with open(filepath, 'r', encoding='utf-8') as f:
        original = f.read()

    # Count TCs before
    tc_before = len(re.findall(r'TC-(?:CF-)?\d{2}-\d{2}', original))
    if tc_before == 0:
        return 0

    content = original

    # Step 1: Remove TC section blocks (### XX Test Cases, ## Cross-Platform Test Cases)
    content = remove_tc_sections(content)

    # Step 2: Remove any remaining detailed TC blocks
    content = remove_detailed_tc_blocks(content)

    # Step 3: Remove heading-style TC blocks (### TC-04-01: ...)
    content = remove_heading_tc_blocks(content)

    # Step 4: Cleanup
    content = cleanup_empty_sections(content)

    # Count TCs after
    tc_after = len(re.findall(r'TC-(?:CF-)?\d{2}-\d{2}', content))

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    return tc_before - tc_after


def main():
    print("Removing TC definitions from markdown chapters")
    print("=" * 50)

    total_removed = 0
    for filename in CHAPTERS:
        removed = process_chapter(filename)
        if removed > 0:
            # Verify
            filepath = os.path.join(CHAPTERS_DIR, filename)
            with open(filepath) as f:
                remaining = len(re.findall(r'TC-(?:CF-)?\d{2}-\d{2}', f.read()))
            print(f"  {filename[:2]}: removed {removed} TC refs, {remaining} remaining")
            total_removed += removed

    print(f"\nTotal TC references removed: {total_removed}")


if __name__ == "__main__":
    main()
