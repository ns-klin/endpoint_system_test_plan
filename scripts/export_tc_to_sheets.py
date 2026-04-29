#!/usr/bin/env python3
"""
Export all TC-XX-XX test cases from chapter .md files to CSV files (one per chapter),
ready for import into Google Sheets.

Output: tc_export/ directory with one CSV per chapter that has test cases.
"""

import os
import re
import csv

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.normpath(os.path.join(SCRIPT_DIR, '..'))
CHAPTERS_DIR = os.path.join(PROJECT_ROOT, 'chapters')
OUTPUT_DIR = os.path.join(PROJECT_ROOT, "tc_export")
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Chapters that have test cases (determined by grep)
CHAPTERS_WITH_TCS = [
    "01_installation.md",
    "02_enrollment.md",
    "04_config_download.md",
    "06_client_status.md",
    "08_gateway_selection.md",
    "09_traffic_steering.md",
    "10_bypass.md",
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

# Chapter titles
CHAPTER_TITLES = {
    "01": "Installation & Upgrade",
    "02": "Enrollment",
    "04": "Config Download",
    "06": "Client Status",
    "08": "Gateway Selection",
    "09": "Traffic Steering",
    "10": "Bypass Mechanisms",
    "12": "Device Classification",
    "13": "Certificate Management",
    "14": "Proxy Management",
    "15": "NPA Integration",
    "16": "DEM",
    "17": "IPC NSCom2",
    "18": "Security",
    "19": "Integration Architecture",
    "20": "Supportability",
    "21": "Watchdog",
}


def parse_table_format(content, chapter_num):
    """Parse test cases in markdown table format (Ch06, Ch08, Ch09, Ch12, Ch13, Ch14, Ch15, Ch16, Ch18, Ch20)."""
    test_cases = []

    # Pattern for table rows with TC-XX-XX
    # Various formats seen in the files
    # Format 1: | TC-06-01 | description | S1 | ENG-xxx | code_ref | Gap Type | P1 |
    # Format 2: | TC-08-01 | description | S2 | P1 | Gap Type |
    # Format 3: | TC-09-01 | description | S1 | P1 | Gap Type | Platform |
    # Format 4: | TC-12-01 | description | S2 | P1 | Gap Type |
    # Format 5: | TC-15-01 | description | S1 | P1 | Gap Type | Platform |
    # Format 6: | TC-18-01 | description | S1 | P1 | Gap Type | Platform |
    # Format 7: | TC-20-01 | description | S2 | P1 | Gap Type |

    lines = content.split('\n')
    for line in lines:
        # Match lines that start a test case row
        tc_match = re.match(r'\|\s*(TC-\d{2}-\d{2})\s*\|(.+)', line)
        if tc_match:
            tc_id = tc_match.group(1)
            rest = tc_match.group(2)
            cells = [c.strip() for c in rest.split('|')]
            # Remove empty cells from trailing |
            cells = [c for c in cells if c != '']

            tc = {"id": tc_id, "chapter": chapter_num}

            if chapter_num == "06":
                # | TC-06-01 | desc | S1 | ENG-xxx | code_ref | Gap Type | P1 |
                tc["description"] = cells[0] if len(cells) > 0 else ""
                tc["severity"] = cells[1] if len(cells) > 1 else ""
                tc["related_bugs"] = cells[2] if len(cells) > 2 else ""
                tc["flow_point"] = cells[3] if len(cells) > 3 else ""
                tc["gap_type"] = cells[4] if len(cells) > 4 else ""
                tc["auto_priority"] = cells[5] if len(cells) > 5 else ""
                tc["platform"] = ""
            elif chapter_num in ("09", "15", "18"):
                # | TC-09-01 | desc | S1 | P1 | Gap Type | Platform |
                tc["description"] = cells[0] if len(cells) > 0 else ""
                tc["severity"] = cells[1] if len(cells) > 1 else ""
                tc["auto_priority"] = cells[2] if len(cells) > 2 else ""
                tc["gap_type"] = cells[3] if len(cells) > 3 else ""
                tc["platform"] = cells[4] if len(cells) > 4 else ""
                tc["related_bugs"] = ""
                tc["flow_point"] = ""
            elif chapter_num == "08":
                # | TC-08-01 | desc | S2 | P1 | Gap Type |
                tc["description"] = cells[0] if len(cells) > 0 else ""
                tc["severity"] = cells[1] if len(cells) > 1 else ""
                tc["auto_priority"] = cells[2] if len(cells) > 2 else ""
                tc["gap_type"] = cells[3] if len(cells) > 3 else ""
                tc["related_bugs"] = ""
                tc["flow_point"] = ""
                tc["platform"] = ""
            elif chapter_num in ("12", "14", "20"):
                # | TC-12-01 | desc | S2 | P1 | Gap Type |
                tc["description"] = cells[0] if len(cells) > 0 else ""
                tc["severity"] = cells[1] if len(cells) > 1 else ""
                tc["auto_priority"] = cells[2] if len(cells) > 2 else ""
                tc["gap_type"] = cells[3] if len(cells) > 3 else ""
                tc["related_bugs"] = ""
                tc["flow_point"] = ""
                tc["platform"] = ""
            elif chapter_num == "13":
                # | TC-13-01 | desc | S2 | ENG-xxx | flow_point | Gap Type | P1 |
                tc["description"] = cells[0] if len(cells) > 0 else ""
                tc["severity"] = cells[1] if len(cells) > 1 else ""
                tc["related_bugs"] = cells[2] if len(cells) > 2 else ""
                tc["flow_point"] = cells[3] if len(cells) > 3 else ""
                tc["gap_type"] = cells[4] if len(cells) > 4 else ""
                tc["auto_priority"] = cells[5] if len(cells) > 5 else ""
                tc["platform"] = ""
            elif chapter_num == "16":
                # | TC-16-01 | desc | S1 | P1 | Gap Type |
                tc["description"] = cells[0] if len(cells) > 0 else ""
                tc["severity"] = cells[1] if len(cells) > 1 else ""
                tc["auto_priority"] = cells[2] if len(cells) > 2 else ""
                tc["gap_type"] = cells[3] if len(cells) > 3 else ""
                tc["related_bugs"] = ""
                tc["flow_point"] = ""
                tc["platform"] = ""
            else:
                # Generic fallback
                tc["description"] = cells[0] if len(cells) > 0 else ""
                tc["severity"] = cells[1] if len(cells) > 1 else ""
                tc["auto_priority"] = cells[2] if len(cells) > 2 else ""
                tc["gap_type"] = cells[3] if len(cells) > 3 else ""
                tc["related_bugs"] = ""
                tc["flow_point"] = ""
                tc["platform"] = ""

            test_cases.append(tc)

    return test_cases


def parse_heading_format(content, chapter_num):
    """Parse test cases in heading format (### TC-XX-XX: Title) used by Ch04."""
    test_cases = []

    # Pattern: ### TC-XX-XX: Title
    tc_pattern = re.compile(r'###\s+TC-(\d{2})-(\d{2}):\s*(.+)')
    matches = list(tc_pattern.finditer(content))

    for i, match in enumerate(matches):
        tc_chap = match.group(1)
        tc_num = match.group(2)
        tc_title = match.group(3).strip()
        tc_id = f"TC-{tc_chap}-{tc_num}"

        start = match.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(content)
        block = content[start:end]

        tc = {
            "id": tc_id,
            "chapter": chapter_num,
            "description": "",
            "severity": "",
            "related_bugs": "",
            "flow_point": "",
            "gap_type": "",
            "auto_priority": "",
            "platform": "",
            "preconditions": "",
            "steps": "",
            "expected_result": "",
        }

        # Extract from table: | **Field** | Value |
        desc_match = re.search(r'\*\*Test Case\*\*\s*\|\s*(.+?)(?:\s*\||\s*$)', block)
        tc["description"] = desc_match.group(1).strip() if desc_match else tc_title

        sev_match = re.search(r'\*\*Severity\*\*\s*\|\s*(\S+)', block)
        if sev_match:
            tc["severity"] = sev_match.group(1)

        bugs_match = re.search(r'\*\*Related Bugs\*\*\s*\|\s*(.+?)(?:\s*\||\s*$)', block)
        if bugs_match:
            tc["related_bugs"] = bugs_match.group(1).strip()

        flow_match = re.search(r'\*\*Flow Point\*\*\s*\|\s*(.+?)(?:\s*\||\s*$)', block)
        if flow_match:
            tc["flow_point"] = flow_match.group(1).strip()

        gap_match = re.search(r'\*\*Gap Type\*\*\s*\|\s*(.+?)(?:\s*\||\s*$)', block)
        if gap_match:
            tc["gap_type"] = gap_match.group(1).strip()

        prio_match = re.search(r'\*\*Automation Priority\*\*\s*\|\s*(.+?)(?:\s*\||\s*$)', block)
        if prio_match:
            tc["auto_priority"] = prio_match.group(1).strip()

        precond_match = re.search(r'\*\*Preconditions\*\*\s*\|\s*(.+?)(?:\s*\||\s*$)', block)
        if precond_match:
            tc["preconditions"] = precond_match.group(1).strip()

        steps_match = re.search(r'\*\*Steps\*\*\s*\|\s*(.+?)(?:\s*\||\s*$)', block)
        if steps_match:
            tc["steps"] = steps_match.group(1).strip()

        expected_match = re.search(r'\*\*Expected Result\*\*\s*\|\s*(.+?)(?:\s*\||\s*$)', block)
        if expected_match:
            tc["expected_result"] = expected_match.group(1).strip()

        # Determine platform from context
        tc["platform"] = determine_platform_from_context(content, match.start(), chapter_num)

        test_cases.append(tc)

    return test_cases


def parse_detailed_format(content, chapter_num):
    """Parse test cases in detailed block format (Ch01, Ch02, Ch04, Ch10, Ch17, Ch19, Ch21)."""
    test_cases = []

    # Pattern: **TC-XX-XX: Title**
    tc_pattern = re.compile(r'\*\*TC-(\d{2})-(\d{2}):\s*(.+?)\*\*')

    # Find all test case blocks
    matches = list(tc_pattern.finditer(content))

    for i, match in enumerate(matches):
        tc_chap = match.group(1)
        tc_num = match.group(2)
        tc_title = match.group(3).strip()
        tc_id = f"TC-{tc_chap}-{tc_num}"

        # Get block content (from this match to the next one or end)
        start = match.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(content)
        block = content[start:end]

        tc = {
            "id": tc_id,
            "chapter": chapter_num,
            "description": tc_title,
            "severity": "",
            "related_bugs": "",
            "flow_point": "",
            "gap_type": "",
            "auto_priority": "",
            "platform": "",
            "preconditions": "",
            "steps": "",
            "expected_result": "",
        }

        # Extract from table fields
        sev_match = re.search(r'\*\*Severity\*\*\s*\|\s*(\S+)', block)
        if sev_match:
            tc["severity"] = sev_match.group(1)

        bugs_match = re.search(r'\*\*Related Bugs\*\*\s*\|\s*(.+?)(?:\s*\||\s*$)', block)
        if bugs_match:
            tc["related_bugs"] = bugs_match.group(1).strip()

        flow_match = re.search(r'\*\*Flow Point\*\*\s*\|\s*(.+?)(?:\s*\||\s*$)', block)
        if flow_match:
            tc["flow_point"] = flow_match.group(1).strip()

        gap_match = re.search(r'\*\*Gap Type\*\*\s*\|\s*(.+?)(?:\s*\||\s*$)', block)
        if gap_match:
            tc["gap_type"] = gap_match.group(1).strip()

        prio_match = re.search(r'\*\*Automation Priority\*\*\s*\|\s*(.+?)(?:\s*\||\s*$)', block)
        if prio_match:
            tc["auto_priority"] = prio_match.group(1).strip()

        platform_match = re.search(r'\*\*Platforms?\*\*\s*\|\s*(.+?)(?:\s*\||\s*$)', block)
        if platform_match:
            tc["platform"] = platform_match.group(1).strip()

        precond_match = re.search(r'\*\*Preconditions\*\*:\s*(.+?)(?:\n\*\*|\n---)', block, re.DOTALL)
        if precond_match:
            tc["preconditions"] = precond_match.group(1).strip().replace('\n', ' ')

        steps_match = re.search(r'\*\*Steps\*\*:\s*\n((?:\d+\..+\n?)+)', block)
        if steps_match:
            steps_text = steps_match.group(1).strip()
            tc["steps"] = steps_text.replace('\n', ' | ')

        expected_match = re.search(r'\*\*Expected Result\*\*:\s*(.+?)(?:\n\*\*|\n---|\n\n)', block, re.DOTALL)
        if expected_match:
            tc["expected_result"] = expected_match.group(1).strip().replace('\n', ' ')

        test_cases.append(tc)

    return test_cases


def determine_platform_from_context(content, tc_start_pos, chapter_num):
    """Determine platform based on section headers above the test case."""
    # Look backwards from the TC position for platform headers
    before = content[:tc_start_pos]
    platform_patterns = [
        (r'##\s+Windows', 'Windows'),
        (r'##\s+macOS', 'macOS'),
        (r'##\s+Linux', 'Linux'),
        (r'##\s+Android', 'Android'),
        (r'##\s+iOS', 'iOS'),
        (r'##\s+ChromeOS', 'ChromeOS'),
        (r'##\s+Backend', 'Backend'),
        (r'##\s+Cross-Platform', 'Cross-Platform'),
        (r'###\s+Windows Test Cases', 'Windows'),
        (r'###\s+macOS Test Cases', 'macOS'),
        (r'###\s+Linux Test Cases', 'Linux'),
        (r'###\s+Android Test Cases', 'Android'),
        (r'###\s+Cross-Platform Test Cases', 'Cross-Platform'),
        (r'###\s+Cross-Flow Test Cases', 'Cross-Flow'),
    ]

    last_match_pos = -1
    platform = ""
    for pattern, plat in platform_patterns:
        for m in re.finditer(pattern, before):
            if m.start() > last_match_pos:
                last_match_pos = m.start()
                platform = plat

    return platform


def parse_chapter(filename):
    """Parse a chapter file and extract all test cases."""
    filepath = os.path.join(CHAPTERS_DIR, filename)
    chapter_num = filename[:2]

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Chapters with detailed block format (TC-XX-XX: Title)
    detailed_chapters = {"01", "02", "10", "19", "21"}
    # Chapters with table format
    table_chapters = {"06", "08", "09", "12", "13", "14", "15", "16", "17", "18", "20"}
    # Chapters with heading format (### TC-XX-XX: Title)
    heading_chapters = {"04"}

    test_cases = []

    if chapter_num in detailed_chapters:
        test_cases = parse_detailed_format(content, chapter_num)
        # Fill in platform from context
        for tc in test_cases:
            tc_find = re.search(r'\*\*' + re.escape(tc["id"]) + r':', content)
            if tc_find and not tc.get("platform"):
                tc["platform"] = determine_platform_from_context(content, tc_find.start(), chapter_num)
    elif chapter_num in heading_chapters:
        test_cases = parse_heading_format(content, chapter_num)
    elif chapter_num in table_chapters:
        test_cases = parse_table_format(content, chapter_num)
        # Fill in platform from context for table-format TCs
        for tc in test_cases:
            if not tc.get("platform"):
                tc_find = re.search(re.escape(tc["id"]), content)
                if tc_find:
                    tc["platform"] = determine_platform_from_context(content, tc_find.start(), chapter_num)

    # Also check for cross-flow test cases (TC-CF-XX-XX format)
    cf_pattern = re.compile(r'\*\*(TC-CF-\d{2}-\d{2}):\s*(.+?)\*\*')
    cf_matches = list(cf_pattern.finditer(content))
    for i, match in enumerate(cf_matches):
        tc_id = match.group(1)
        tc_title = match.group(2).strip()

        start = match.end()
        end = cf_matches[i + 1].start() if i + 1 < len(cf_matches) else len(content)
        block = content[start:end]

        tc = {
            "id": tc_id,
            "chapter": chapter_num,
            "description": tc_title,
            "severity": "",
            "related_bugs": "",
            "flow_point": "",
            "gap_type": "",
            "auto_priority": "",
            "platform": "Cross-Flow",
            "preconditions": "",
            "steps": "",
            "expected_result": "",
        }

        sev_match = re.search(r'\*\*Severity\*\*\s*\|\s*(\S+)', block)
        if sev_match:
            tc["severity"] = sev_match.group(1)

        bugs_match = re.search(r'\*\*Related Bugs\*\*\s*\|\s*(.+?)(?:\s*\||\s*$)', block)
        if bugs_match:
            tc["related_bugs"] = bugs_match.group(1).strip()

        gap_match = re.search(r'\*\*Gap Type\*\*\s*\|\s*(.+?)(?:\s*\||\s*$)', block)
        if gap_match:
            tc["gap_type"] = gap_match.group(1).strip()

        prio_match = re.search(r'\*\*Automation Priority\*\*\s*\|\s*(.+?)(?:\s*\||\s*$)', block)
        if prio_match:
            tc["auto_priority"] = prio_match.group(1).strip()

        test_cases.append(tc)

    return test_cases


def write_csv(chapter_num, test_cases, title):
    """Write test cases to a CSV file."""
    filename = f"{chapter_num}_{title.replace(' ', '_').replace('/', '_').replace('&', 'and')}.csv"
    filepath = os.path.join(OUTPUT_DIR, filename)

    headers = [
        "ID",
        "Description",
        "Severity",
        "Auto Priority",
        "Gap Type",
        "Platform",
        "Related Bugs",
        "Flow Point",
        "Preconditions",
        "Steps",
        "Expected Result",
    ]

    with open(filepath, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        for tc in test_cases:
            writer.writerow([
                tc.get("id", ""),
                tc.get("description", ""),
                tc.get("severity", ""),
                tc.get("auto_priority", ""),
                tc.get("gap_type", ""),
                tc.get("platform", ""),
                tc.get("related_bugs", ""),
                tc.get("flow_point", ""),
                tc.get("preconditions", ""),
                tc.get("steps", ""),
                tc.get("expected_result", ""),
            ])

    return filepath, len(test_cases)


def main():
    print("=" * 60)
    print("NSClient Knowledge Base — Test Case Export")
    print("=" * 60)
    print()

    total_tcs = 0
    all_results = []

    for filename in CHAPTERS_WITH_TCS:
        chapter_num = filename[:2]
        title = CHAPTER_TITLES.get(chapter_num, "Unknown")

        try:
            test_cases = parse_chapter(filename)
            if test_cases:
                filepath, count = write_csv(chapter_num, test_cases, title)
                total_tcs += count
                all_results.append((chapter_num, title, count, filepath))
                print(f"  Ch{chapter_num} ({title}): {count} test cases → {os.path.basename(filepath)}")
            else:
                print(f"  Ch{chapter_num} ({title}): 0 test cases (skipped)")
        except Exception as e:
            print(f"  Ch{chapter_num} ({title}): ERROR — {e}")

    print()
    print(f"Total: {total_tcs} test cases across {len(all_results)} chapters")
    print(f"Output directory: {OUTPUT_DIR}")
    print()

    # Also write a combined summary CSV
    summary_path = os.path.join(OUTPUT_DIR, "00_SUMMARY.csv")
    with open(summary_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["Chapter", "Title", "Test Case Count"])
        for ch_num, title, count, _ in all_results:
            writer.writerow([f"Ch{ch_num}", title, count])
        writer.writerow(["", "TOTAL", total_tcs])

    print(f"Summary: {summary_path}")


if __name__ == "__main__":
    main()
