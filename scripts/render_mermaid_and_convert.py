#!/usr/bin/env python3
"""
Pipeline: Markdown → English HTML with rendered Mermaid diagrams for Confluence.

Steps:
1. Read markdown file
2. Extract mermaid code blocks
3. Render each mermaid diagram to PNG via mermaid.ink API
4. Upload PNGs as Confluence page attachments
5. Convert markdown to Confluence storage format HTML (English)
   - Replace mermaid blocks with <ac:image> tags referencing attachments
6. Optionally update the Confluence page
"""
import re
import sys
import os
import json
import base64
import zlib
import time
import requests
import html as html_module

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.normpath(os.path.join(SCRIPT_DIR, '..'))
CHAPTERS_DIR = os.path.join(PROJECT_ROOT, 'chapters')
MERMAID_IMAGES_DIR = os.path.join(PROJECT_ROOT, 'mermaid_images')
HTML_OUTPUT_DIR = os.path.join(PROJECT_ROOT, 'html_output')

CONFLUENCE_URL = "https://netskope.atlassian.net/wiki"
USERNAME = os.environ.get("CONFLUENCE_USERNAME", "klin@netskope.com")
API_TOKEN = os.environ["CONFLUENCE_API_TOKEN"]


def render_mermaid_to_png(mermaid_code, output_path, max_retries=3):
    """Render mermaid code to PNG using mermaid.ink API."""
    encoded = base64.urlsafe_b64encode(mermaid_code.encode('utf-8')).decode('ascii')
    url = f"https://mermaid.ink/img/{encoded}?type=png&bgColor=white"

    for attempt in range(max_retries):
        try:
            resp = requests.get(url, timeout=30)
            if resp.status_code == 200 and len(resp.content) > 100:
                with open(output_path, 'wb') as f:
                    f.write(resp.content)
                return True
            else:
                print(f"    Attempt {attempt+1}: HTTP {resp.status_code}, size={len(resp.content)}")
        except Exception as e:
            print(f"    Attempt {attempt+1}: {e}")
        time.sleep(2)

    print(f"    FAILED to render after {max_retries} attempts")
    return False


def upload_attachment(page_id, file_path, filename):
    """Upload a file as attachment to a Confluence page."""
    url = f"{CONFLUENCE_URL}/rest/api/content/{page_id}/child/attachment"

    # Check if attachment already exists
    resp = requests.get(
        url,
        params={'filename': filename},
        auth=(USERNAME, API_TOKEN)
    )
    existing_id = None
    if resp.status_code == 200:
        results = resp.json().get('results', [])
        if results:
            existing_id = results[0]['id']

    headers = {"X-Atlassian-Token": "nocheck"}
    with open(file_path, 'rb') as f:
        files = {'file': (filename, f, 'image/png')}

        if existing_id:
            upload_url = f"{CONFLUENCE_URL}/rest/api/content/{page_id}/child/attachment/{existing_id}/data"
            resp = requests.post(upload_url, files=files, headers=headers, auth=(USERNAME, API_TOKEN))
        else:
            resp = requests.post(url, files=files, headers=headers, auth=(USERNAME, API_TOKEN))

    if resp.status_code in (200, 201):
        print(f"    Uploaded: {filename}")
        return True
    else:
        print(f"    Upload failed ({resp.status_code}): {resp.text[:200]}")
        return False


def extract_mermaid_blocks(markdown_content):
    """Extract mermaid code blocks and their positions."""
    pattern = r'```mermaid\s*\n(.*?)```'
    blocks = []
    for match in re.finditer(pattern, markdown_content, re.DOTALL):
        blocks.append({
            'start': match.start(),
            'end': match.end(),
            'code': match.group(1).strip(),
            'full_match': match.group(0)
        })
    return blocks


def escape_html(text):
    return html_module.escape(text)


def convert_inline_formatting(text):
    """Apply inline formatting conversions."""
    text = re.sub(r'`([^`]+)`', lambda m: f'<code>{escape_html(m.group(1))}</code>', text)
    text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
    text = re.sub(r'(?<!\*)\*([^\*]+?)\*(?!\*)', r'<em>\1</em>', text)
    text = re.sub(r'\[([^\]]+)\]\(([^\)]+)\)', r'<a href="\2">\1</a>', text)
    return text


def convert_table_row(line, is_header=False):
    cells = [cell.strip() for cell in line.split('|')[1:-1]]
    tag = 'th' if is_header else 'td'
    result = '<tr>'
    for cell in cells:
        result += f'<{tag}>{convert_inline_formatting(cell)}</{tag}>'
    result += '</tr>'
    return result


def convert_markdown_to_confluence_html(markdown_content, mermaid_filenames):
    """Convert markdown to Confluence storage format HTML.
    mermaid_filenames: dict mapping mermaid block index to attachment filename.
    """
    lines = markdown_content.split('\n')
    html_lines = []

    in_code_block = False
    code_block_lang = ""
    code_block_content = []
    in_mermaid_block = False
    mermaid_index = -1

    in_table = False
    table_rows = []

    in_list = False
    list_items = []
    list_type = None

    i = 0
    while i < len(lines):
        line = lines[i]

        # Code block detection
        if line.startswith('```'):
            if not in_code_block and not in_mermaid_block:
                lang = line[3:].strip()
                if lang == 'mermaid':
                    in_mermaid_block = True
                    mermaid_index += 1
                    i += 1
                    continue
                else:
                    in_code_block = True
                    code_block_lang = lang
                    code_block_content = []
            elif in_mermaid_block:
                in_mermaid_block = False
                # Insert image reference
                if mermaid_index in mermaid_filenames:
                    fname = mermaid_filenames[mermaid_index]
                    html_lines.append(
                        f'<ac:image ac:align="center" ac:width="800">'
                        f'<ri:attachment ri:filename="{fname}" />'
                        f'</ac:image>'
                    )
                else:
                    html_lines.append('<p><em>[Diagram rendering failed]</em></p>')
                i += 1
                continue
            else:
                in_code_block = False
                code = '\n'.join(code_block_content)
                html_lines.append('<ac:structured-macro ac:name="code">')
                if code_block_lang:
                    html_lines.append(f'<ac:parameter ac:name="language">{code_block_lang}</ac:parameter>')
                html_lines.append(f'<ac:plain-text-body><![CDATA[{code}]]></ac:plain-text-body>')
                html_lines.append('</ac:structured-macro>')
                code_block_content = []
                code_block_lang = ""
            i += 1
            continue

        if in_code_block:
            code_block_content.append(line)
            i += 1
            continue

        if in_mermaid_block:
            i += 1
            continue

        # Table detection
        if '|' in line and line.strip().startswith('|'):
            if not in_table:
                in_table = True
                table_rows = []
            if re.match(r'^\|[\s\-:|]+\|$', line):
                i += 1
                continue
            is_header = len(table_rows) == 0
            table_rows.append(convert_table_row(line, is_header))
            if i + 1 >= len(lines) or not lines[i + 1].strip().startswith('|'):
                html_lines.append('<table><tbody>')
                html_lines.extend(table_rows)
                html_lines.append('</tbody></table>')
                in_table = False
                table_rows = []
            i += 1
            continue

        # List detection
        list_match = re.match(r'^(\s*)([-*]|\d+\.)\s+(.+)$', line)
        if list_match:
            indent = len(list_match.group(1))
            marker = list_match.group(2)
            content = list_match.group(3)
            current_list_type = 'ol' if marker[0].isdigit() else 'ul'
            if not in_list:
                in_list = True
                list_type = current_list_type
                list_items = []
                html_lines.append(f'<{list_type}>')
            content = convert_inline_formatting(content)
            list_items.append(f'<li>{content}</li>')
            if i + 1 >= len(lines) or not re.match(r'^(\s*)([-*]|\d+\.)\s+', lines[i + 1]):
                html_lines.extend(list_items)
                html_lines.append(f'</{list_type}>')
                in_list = False
                list_items = []
                list_type = None
            i += 1
            continue

        # Header detection
        header_match = re.match(r'^(#{1,6})\s+(.+)$', line)
        if header_match:
            level = len(header_match.group(1))
            text = header_match.group(2)
            html_lines.append(f'<h{level}>{escape_html(text)}</h{level}>')
            i += 1
            continue

        # Horizontal rule
        if re.match(r'^---+$', line):
            html_lines.append('<hr />')
            i += 1
            continue

        # Blockquote
        if line.startswith('>'):
            text = line.lstrip('> ')
            text = convert_inline_formatting(text)
            html_lines.append(f'<blockquote><p>{text}</p></blockquote>')
            i += 1
            continue

        # Empty line
        if not line.strip():
            i += 1
            continue

        # Regular paragraph
        paragraph = convert_inline_formatting(line)
        html_lines.append(f'<p>{paragraph}</p>')
        i += 1

    return '\n'.join(html_lines)


def get_page_info(page_id):
    url = f"{CONFLUENCE_URL}/rest/api/content/{page_id}"
    resp = requests.get(url, params={'expand': 'version,space'}, auth=(USERNAME, API_TOKEN))
    if resp.status_code == 200:
        return resp.json()
    return None


def update_page(page_id, title, html_content):
    page_info = get_page_info(page_id)
    if not page_info:
        return False
    current_version = page_info['version']['number']
    space_key = page_info['space']['key']
    url = f"{CONFLUENCE_URL}/rest/api/content/{page_id}"
    payload = {
        "id": page_id,
        "type": "page",
        "title": title,
        "space": {"key": space_key},
        "body": {"storage": {"value": html_content, "representation": "storage"}},
        "version": {"number": current_version + 1, "message": "Deep-dive update with rendered diagrams"}
    }
    resp = requests.put(url, data=json.dumps(payload),
                        headers={"Content-Type": "application/json"},
                        auth=(USERNAME, API_TOKEN))
    if resp.status_code == 200:
        print(f"  Page updated: {title}")
        return True
    else:
        print(f"  Page update failed ({resp.status_code}): {resp.text[:300]}")
        return False


def process_chapter(md_file, page_id, page_title):
    """Full pipeline for one chapter."""
    print(f"\n{'='*60}")
    print(f"Processing: {md_file} → {page_title}")
    print(f"{'='*60}")

    with open(md_file, 'r', encoding='utf-8') as f:
        md_content = f.read()

    # 1. Extract mermaid blocks
    mermaid_blocks = extract_mermaid_blocks(md_content)
    print(f"  Found {len(mermaid_blocks)} mermaid diagrams")

    # 2. Render each to PNG
    os.makedirs(MERMAID_IMAGES_DIR, exist_ok=True)
    base_name = os.path.splitext(os.path.basename(md_file))[0]
    mermaid_filenames = {}

    for idx, block in enumerate(mermaid_blocks):
        fname = f"{base_name}_diagram_{idx+1:02d}.png"
        fpath = os.path.join(MERMAID_IMAGES_DIR, fname)
        print(f"  Rendering diagram {idx+1}/{len(mermaid_blocks)}: {fname}")
        if render_mermaid_to_png(block['code'], fpath):
            mermaid_filenames[idx] = fname
        else:
            print(f"    WARNING: Skipping failed diagram {idx+1}")

    # 3. Upload PNGs as attachments
    print(f"  Uploading {len(mermaid_filenames)} attachments to page {page_id}...")
    for idx, fname in mermaid_filenames.items():
        fpath = os.path.join(MERMAID_IMAGES_DIR, fname)
        upload_attachment(page_id, fpath, fname)

    # 4. Convert markdown to Confluence HTML with image references
    print(f"  Converting markdown to Confluence HTML...")
    html_content = convert_markdown_to_confluence_html(md_content, mermaid_filenames)

    # 5. Save HTML locally
    os.makedirs(HTML_OUTPUT_DIR, exist_ok=True)
    html_path = os.path.join(HTML_OUTPUT_DIR, f"{base_name}.html")
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html_content)
    print(f"  Saved HTML: {html_path} ({len(html_content)} chars)")

    # 6. Update Confluence page
    print(f"  Updating Confluence page...")
    success = update_page(page_id, page_title, html_content)
    return success


ALL_PAGES = {
    "00": {"id": "7776206958", "title": "00. NSClient Architecture Overview", "md": os.path.join(CHAPTERS_DIR, "00_overview.md"), "md_fallback": os.path.join(PROJECT_ROOT, "en", "00_overview.md")},
    "01": {"id": "7775256801", "title": "01. Installation, Upgrade and Uninstallation", "md": os.path.join(CHAPTERS_DIR, "01_installation.md"), "md_fallback": os.path.join(PROJECT_ROOT, "en", "01_installation.md")},
    "02": {"id": "7772898132", "title": "02. Enrollment Flow", "md": os.path.join(CHAPTERS_DIR, "02_enrollment.md"), "md_fallback": os.path.join(PROJECT_ROOT, "en", "02_enrollment.md")},
    "03": {"id": "7776305272", "title": "03. Service Lifecycle", "md": os.path.join(CHAPTERS_DIR, "03_service_lifecycle.md"), "md_fallback": os.path.join(PROJECT_ROOT, "en", "03_service_lifecycle.md")},
    "04": {"id": "7775715658", "title": "04. Config Download and Management", "md": os.path.join(CHAPTERS_DIR, "04_config_download.md"), "md_fallback": os.path.join(PROJECT_ROOT, "en", "04_config_download.md")},
    "05": {"id": "7775682854", "title": "05. Traffic Steering Configuration", "md": os.path.join(CHAPTERS_DIR, "05_steering_config.md"), "md_fallback": os.path.join(PROJECT_ROOT, "en", "05_steering_config.md")},
    "06": {"id": "7775191215", "title": "06. Client Status Reporting", "md": os.path.join(CHAPTERS_DIR, "06_client_status.md"), "md_fallback": os.path.join(PROJECT_ROOT, "en", "06_client_status.md")},
    "07": {"id": "7775420785", "title": "07. Tunnel Establishment and Management", "md": os.path.join(CHAPTERS_DIR, "07_tunnel_management.md"), "md_fallback": os.path.join(PROJECT_ROOT, "en", "07_tunnel_management.md")},
    "08": {"id": "7775453376", "title": "08. Gateway Selection (GSLB)", "md": os.path.join(CHAPTERS_DIR, "08_gateway_selection.md"), "md_fallback": os.path.join(PROJECT_ROOT, "en", "08_gateway_selection.md")},
    "09": {"id": "7775813750", "title": "09. Traffic Interception and Packet Processing", "md": os.path.join(CHAPTERS_DIR, "09_traffic_steering.md"), "md_fallback": os.path.join(PROJECT_ROOT, "en", "09_traffic_steering.md")},
    "10": {"id": "7775912130", "title": "10. Bypass Mechanism", "md": os.path.join(CHAPTERS_DIR, "10_bypass.md"), "md_fallback": os.path.join(PROJECT_ROOT, "en", "10_bypass.md")},
    "11": {"id": "7775715680", "title": "11. FailClose Mechanism", "md": os.path.join(CHAPTERS_DIR, "11_failclose.md"), "md_fallback": os.path.join(PROJECT_ROOT, "en", "11_failclose.md")},
    "12": {"id": "7775715699", "title": "12. Device Classification (DC)", "md": os.path.join(CHAPTERS_DIR, "12_device_classification.md"), "md_fallback": os.path.join(PROJECT_ROOT, "en", "12_device_classification.md")},
    "13": {"id": "7775355168", "title": "13. Certificate Management", "md": os.path.join(CHAPTERS_DIR, "13_certificate_management.md"), "md_fallback": os.path.join(PROJECT_ROOT, "en", "13_certificate_management.md")},
    "14": {"id": "7775223994", "title": "14. Proxy Detection and Handling", "md": os.path.join(CHAPTERS_DIR, "14_proxy_management.md"), "md_fallback": os.path.join(PROJECT_ROOT, "en", "14_proxy_management.md")},
    "15": {"id": "7773193015", "title": "15. NPA (Private Access) Integration", "md": os.path.join(CHAPTERS_DIR, "15_npa_integration.md"), "md_fallback": os.path.join(PROJECT_ROOT, "en", "15_npa_integration.md")},
    "16": {"id": "7776305291", "title": "16. DEM (Digital Experience Monitoring)", "md": os.path.join(CHAPTERS_DIR, "16_dem.md"), "md_fallback": os.path.join(PROJECT_ROOT, "en", "16_dem.md")},
    "17": {"id": "7774602055", "title": "17. IPC Communication (NSCom2/NSMsg2)", "md": os.path.join(CHAPTERS_DIR, "17_ipc_nscom2.md"), "md_fallback": os.path.join(PROJECT_ROOT, "en", "17_ipc_nscom2.md")},
    "18": {"id": "7775781177", "title": "18. Security Mechanisms", "md": os.path.join(CHAPTERS_DIR, "18_security.md"), "md_fallback": os.path.join(PROJECT_ROOT, "en", "18_security.md")},
    "19": {"id": "7775027357", "title": "19. Multi-Component Integration Architecture", "md": os.path.join(CHAPTERS_DIR, "19_integration_architecture.md"), "md_fallback": os.path.join(PROJECT_ROOT, "en", "19_integration_architecture.md")},
    "20": {"id": "7776141570", "title": "20. Supportability and Troubleshooting", "md": os.path.join(CHAPTERS_DIR, "20_supportability.md"), "md_fallback": os.path.join(PROJECT_ROOT, "en", "20_supportability.md")},
    "21": {"id": "7850557719", "title": "21. Watchdog", "md": os.path.join(CHAPTERS_DIR, "21_watchdog.md")},
}


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python render_mermaid_and_convert.py <chapter_numbers...>")
        print("Example: python render_mermaid_and_convert.py 05 07")
        print("Use 'all' to process all chapters.")
        sys.exit(1)

    chapters = sys.argv[1:]
    if 'all' in chapters:
        chapters = sorted(ALL_PAGES.keys())

    for ch in chapters:
        if ch not in ALL_PAGES:
            print(f"Unknown chapter: {ch}")
            continue
        info = ALL_PAGES[ch]
        md_path = info['md']
        if not os.path.exists(md_path) and 'md_fallback' in info:
            md_path = info['md_fallback']
            print(f"  Note: Chapter file not found, using fallback: {md_path}")
        if not os.path.exists(md_path):
            print(f"  ERROR: File not found: {md_path}")
            continue
        process_chapter(md_path, info['id'], info['title'])
