#!/usr/bin/env python3
"""
Deploy new pages to Confluence under specified parent folders.

Task 1: en/escalation_bug_flow_analysis.md → folder 7793148030 (with mermaid rendering)
Task 2: bugs/*.md → folder 7793410061 (no mermaid, plain markdown conversion)
"""
import re
import sys
import os
import json
import base64
import time
import requests
import html as html_module

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.normpath(os.path.join(SCRIPT_DIR, '..'))
CHAPTERS_DIR = os.path.join(PROJECT_ROOT, 'chapters')
MERMAID_IMAGES_DIR = os.path.join(PROJECT_ROOT, 'mermaid_images')
HTML_OUTPUT_DIR = os.path.join(PROJECT_ROOT, 'html_output')
BUGS_DIR = os.path.join(PROJECT_ROOT, 'bugs')
EN_DIR = os.path.join(PROJECT_ROOT, 'en')

CONFLUENCE_URL = "https://netskope.atlassian.net/wiki"
USERNAME = os.environ.get("CONFLUENCE_USERNAME", "klin@netskope.com")
API_TOKEN = os.environ["CONFLUENCE_API_TOKEN"]
SPACE_KEY = "CDTBA"


def render_mermaid_to_png(mermaid_code, output_path, max_retries=3):
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


def upload_attachment(page_id, file_path, filename, max_retries=3):
    url = f"{CONFLUENCE_URL}/rest/api/content/{page_id}/child/attachment"

    for attempt in range(max_retries):
        try:
            resp = requests.get(url, params={'filename': filename}, auth=(USERNAME, API_TOKEN))
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
                print(f"    Upload attempt {attempt+1} failed ({resp.status_code}): {resp.text[:200]}")
        except Exception as e:
            print(f"    Upload attempt {attempt+1} error: {e}")

        time.sleep(3)

    print(f"    FAILED to upload {filename} after {max_retries} attempts")
    return False


def extract_mermaid_blocks(markdown_content):
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
    # First escape HTML entities in the raw text, but preserve markdown syntax
    # We need to handle this carefully: escape &, <, > but not markdown markers
    text = text.replace('&', '&amp;')
    text = text.replace('<', '&lt;')
    text = text.replace('>', '&gt;')
    # Now apply markdown formatting (these produce HTML tags, so they must come after escaping)
    text = re.sub(r'`([^`]+)`', lambda m: f'<code>{m.group(1)}</code>', text)
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


def convert_markdown_to_confluence_html(markdown_content, mermaid_filenames=None):
    if mermaid_filenames is None:
        mermaid_filenames = {}

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

        header_match = re.match(r'^(#{1,6})\s+(.+)$', line)
        if header_match:
            level = len(header_match.group(1))
            text = header_match.group(2)
            html_lines.append(f'<h{level}>{convert_inline_formatting(text)}</h{level}>')
            i += 1
            continue

        if re.match(r'^---+$', line):
            html_lines.append('<hr />')
            i += 1
            continue

        if line.startswith('>'):
            text = line.lstrip('> ')
            text = convert_inline_formatting(text)
            html_lines.append(f'<blockquote><p>{text}</p></blockquote>')
            i += 1
            continue

        if not line.strip():
            i += 1
            continue

        paragraph = convert_inline_formatting(line)
        html_lines.append(f'<p>{paragraph}</p>')
        i += 1

    return '\n'.join(html_lines)


def find_page_by_title(title, parent_id):
    """Check if a page with this title already exists under parent."""
    url = f"{CONFLUENCE_URL}/rest/api/content"
    params = {
        'title': title,
        'spaceKey': SPACE_KEY,
        'type': 'page',
        'expand': 'version'
    }
    resp = requests.get(url, params=params, auth=(USERNAME, API_TOKEN))
    if resp.status_code == 200:
        results = resp.json().get('results', [])
        for r in results:
            return r['id'], r['version']['number']
    return None, None


def create_page(title, html_content, parent_id):
    """Create a new Confluence page under parent_id."""
    url = f"{CONFLUENCE_URL}/rest/api/content"
    payload = {
        "type": "page",
        "title": title,
        "space": {"key": SPACE_KEY},
        "ancestors": [{"id": str(parent_id)}],
        "body": {
            "storage": {
                "value": html_content,
                "representation": "storage"
            }
        }
    }
    resp = requests.post(
        url,
        data=json.dumps(payload),
        headers={"Content-Type": "application/json"},
        auth=(USERNAME, API_TOKEN)
    )
    if resp.status_code == 200:
        page_id = resp.json()['id']
        print(f"  Created page: {title} (id={page_id})")
        return page_id
    else:
        print(f"  Create failed ({resp.status_code}): {resp.text[:300]}")
        return None


def update_page(page_id, title, html_content, version):
    """Update an existing Confluence page."""
    url = f"{CONFLUENCE_URL}/rest/api/content/{page_id}"
    payload = {
        "id": page_id,
        "type": "page",
        "title": title,
        "space": {"key": SPACE_KEY},
        "body": {"storage": {"value": html_content, "representation": "storage"}},
        "version": {"number": version + 1, "message": "Updated content"}
    }
    for attempt in range(3):
        try:
            resp = requests.put(
                url,
                data=json.dumps(payload),
                headers={"Content-Type": "application/json"},
                auth=(USERNAME, API_TOKEN)
            )
            if resp.status_code == 200:
                print(f"  Updated page: {title} (id={page_id})")
                return page_id
            else:
                print(f"  Update failed ({resp.status_code}): {resp.text[:300]}")
                return None
        except requests.exceptions.ConnectionError as e:
            print(f"  Update attempt {attempt+1} connection error: {e}")
            if attempt < 2:
                time.sleep(5)
    print(f"  Update failed after 3 attempts: {title}")
    return None


def create_or_update_page(title, html_content, parent_id):
    """Create page if not exists, update if exists."""
    existing_id, version = find_page_by_title(title, parent_id)
    if existing_id:
        print(f"  Page exists (id={existing_id}), updating...")
        return update_page(existing_id, title, html_content, version)
    else:
        return create_page(title, html_content, parent_id)


# ─── Task 1: Escalation Bug Flow Analysis (with mermaid) ───

def deploy_escalation_report():
    """Deploy en/escalation_bug_flow_analysis.md with mermaid rendering."""
    PARENT_ID = "7793148030"
    TITLE = "Escalation Bug & Critical Code Flow Cross-Analysis Report"
    MD_FILE = os.path.join(EN_DIR, "escalation_bug_flow_analysis.md")

    print(f"\n{'='*60}")
    print(f"Task 1: Deploy Escalation Bug Flow Analysis")
    print(f"  Source: {MD_FILE}")
    print(f"  Parent folder: {PARENT_ID}")
    print(f"{'='*60}")

    with open(MD_FILE, 'r', encoding='utf-8') as f:
        md_content = f.read()

    # 1. Extract mermaid blocks
    mermaid_blocks = extract_mermaid_blocks(md_content)
    print(f"  Found {len(mermaid_blocks)} mermaid diagrams")

    # 2. Create/update page first (need page_id for attachments)
    # Use placeholder HTML first to get page ID
    placeholder_html = "<p>Uploading content...</p>"
    page_id = create_or_update_page(TITLE, placeholder_html, PARENT_ID)
    if not page_id:
        print("  FAILED: Could not create page")
        return False

    # 3. Render mermaid to PNG and upload
    os.makedirs(MERMAID_IMAGES_DIR, exist_ok=True)
    base_name = "escalation_bug_flow_analysis"
    mermaid_filenames = {}

    for idx, block in enumerate(mermaid_blocks):
        fname = f"{base_name}_diagram_{idx+1:02d}.png"
        fpath = os.path.join(MERMAID_IMAGES_DIR, fname)
        print(f"  Rendering diagram {idx+1}/{len(mermaid_blocks)}: {fname}")
        if render_mermaid_to_png(block['code'], fpath):
            mermaid_filenames[idx] = fname
        else:
            print(f"    WARNING: Skipping failed diagram {idx+1}")

    # 4. Upload PNGs (with delay to avoid rate limiting)
    print(f"  Uploading {len(mermaid_filenames)} attachments...")
    for i, (idx, fname) in enumerate(mermaid_filenames.items()):
        fpath = os.path.join(MERMAID_IMAGES_DIR, fname)
        upload_attachment(page_id, fpath, fname)
        if i < len(mermaid_filenames) - 1:
            time.sleep(1)

    # 5. Convert markdown with image references
    print(f"  Converting markdown to Confluence HTML...")
    html_content = convert_markdown_to_confluence_html(md_content, mermaid_filenames)

    # 6. Save HTML locally
    os.makedirs(HTML_OUTPUT_DIR, exist_ok=True)
    html_path = os.path.join(HTML_OUTPUT_DIR, f"{base_name}.html")
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html_content)
    print(f"  Saved HTML: {html_path} ({len(html_content)} chars)")

    # 7. Update page with real content
    # Need to get current version since we just created/updated it
    existing_id, version = find_page_by_title(TITLE, PARENT_ID)
    if existing_id:
        update_page(existing_id, TITLE, html_content, version)

    print(f"  DONE: {CONFLUENCE_URL}/spaces/{SPACE_KEY}/pages/{page_id}")
    return True


# ─── Task 2: Bug files (no mermaid) ───

BUGS_PAGES = [
    {"md": os.path.join(BUGS_DIR, "README.md"),          "title": "Escalation Bug Review - Overview"},
    {"md": os.path.join(BUGS_DIR, "install_upgrade.md"),  "title": "Escalation Bugs - Install / Upgrade / Enrollment"},
    {"md": os.path.join(BUGS_DIR, "tunneling.md"),        "title": "Escalation Bugs - Tunneling / Gateway"},
    {"md": os.path.join(BUGS_DIR, "steering.md"),         "title": "Escalation Bugs - Steering / Bypass / Exception"},
    {"md": os.path.join(BUGS_DIR, "failclose.md"),        "title": "Escalation Bugs - FailClose / FailOpen"},
]


def deploy_bugs():
    """Deploy bugs/*.md files as pages under the bugs folder."""
    PARENT_ID = "7793410061"

    print(f"\n{'='*60}")
    print(f"Task 2: Deploy Bug Files")
    print(f"  Parent folder: {PARENT_ID}")
    print(f"{'='*60}")

    os.makedirs(HTML_OUTPUT_DIR, exist_ok=True)

    for bug_page in BUGS_PAGES:
        md_file = bug_page['md']
        title = bug_page['title']
        print(f"\n  Processing: {md_file} → {title}")

        with open(md_file, 'r', encoding='utf-8') as f:
            md_content = f.read()

        html_content = convert_markdown_to_confluence_html(md_content)

        # Save HTML locally
        base_name = os.path.splitext(os.path.basename(md_file))[0]
        html_path = os.path.join(HTML_OUTPUT_DIR, f"bugs_{base_name}.html")
        with open(html_path, 'w', encoding='utf-8') as f:
            f.write(html_content)
        print(f"  Saved HTML: {html_path} ({len(html_content)} chars)")

        page_id = create_or_update_page(title, html_content, PARENT_ID)
        if page_id:
            print(f"  DONE: {CONFLUENCE_URL}/spaces/{SPACE_KEY}/pages/{page_id}")
        else:
            print(f"  FAILED: {title}")


# ─── Task 3: Platform-specific Escalation Reports (with mermaid) ───

PLATFORM_PAGES = [
    {"md": os.path.join(EN_DIR, "escalation_bug_flow_windows.md"), "title": "Escalation Bug Cross-Analysis — Windows"},
    {"md": os.path.join(EN_DIR, "escalation_bug_flow_macos.md"),   "title": "Escalation Bug Cross-Analysis — macOS"},
    {"md": os.path.join(EN_DIR, "escalation_bug_flow_android.md"),  "title": "Escalation Bug Cross-Analysis — Android"},
    {"md": os.path.join(EN_DIR, "escalation_bug_flow_ios.md"),      "title": "Escalation Bug Cross-Analysis — iOS"},
    {"md": os.path.join(EN_DIR, "escalation_bug_flow_linux.md"),    "title": "Escalation Bug Cross-Analysis — Linux"},
    {"md": os.path.join(EN_DIR, "escalation_bug_flow_chromeos.md"), "title": "Escalation Bug Cross-Analysis — ChromeOS"},
    {"md": os.path.join(EN_DIR, "escalation_bug_flow_backend.md"),  "title": "Escalation Bug Cross-Analysis — Backend"},
]


def deploy_platform_reports():
    """Deploy platform-specific escalation reports with mermaid rendering."""
    PARENT_ID = "7793148030"

    print(f"\n{'='*60}")
    print(f"Task 3: Deploy Platform-Specific Reports")
    print(f"  Parent folder: {PARENT_ID}")
    print(f"{'='*60}")

    os.makedirs(MERMAID_IMAGES_DIR, exist_ok=True)
    os.makedirs(HTML_OUTPUT_DIR, exist_ok=True)

    for page in PLATFORM_PAGES:
        md_file = page['md']
        title = page['title']
        print(f"\n  Processing: {md_file} → {title}")

        with open(md_file, 'r', encoding='utf-8') as f:
            md_content = f.read()

        mermaid_blocks = extract_mermaid_blocks(md_content)
        print(f"  Found {len(mermaid_blocks)} mermaid diagrams")

        placeholder_html = "<p>Uploading content...</p>"
        page_id = create_or_update_page(title, placeholder_html, PARENT_ID)
        if not page_id:
            print(f"  FAILED: Could not create page for {title}")
            continue

        base_name = os.path.splitext(os.path.basename(md_file))[0]
        mermaid_filenames = {}

        for idx, block in enumerate(mermaid_blocks):
            fname = f"{base_name}_diagram_{idx+1:02d}.png"
            fpath = os.path.join(MERMAID_IMAGES_DIR, fname)
            print(f"    Rendering diagram {idx+1}/{len(mermaid_blocks)}: {fname}")
            if render_mermaid_to_png(block['code'], fpath):
                mermaid_filenames[idx] = fname
            else:
                print(f"    WARNING: Skipping failed diagram {idx+1}")

        print(f"  Uploading {len(mermaid_filenames)} attachments...")
        for i, (idx, fname) in enumerate(mermaid_filenames.items()):
            fpath = os.path.join(MERMAID_IMAGES_DIR, fname)
            upload_attachment(page_id, fpath, fname)
            if i < len(mermaid_filenames) - 1:
                time.sleep(1)

        print(f"  Converting markdown to Confluence HTML...")
        html_content = convert_markdown_to_confluence_html(md_content, mermaid_filenames)

        html_path = os.path.join(HTML_OUTPUT_DIR, f"{base_name}.html")
        with open(html_path, 'w', encoding='utf-8') as f:
            f.write(html_content)
        print(f"  Saved HTML: {html_path} ({len(html_content)} chars)")

        existing_id, version = find_page_by_title(title, PARENT_ID)
        if existing_id:
            update_page(existing_id, title, html_content, version)

        print(f"  DONE: {CONFLUENCE_URL}/spaces/{SPACE_KEY}/pages/{page_id}")


# ─── Task 4: Hub/Index page (replace original full report) ───

def deploy_hub_page():
    """Replace the original full report page with the hub/index page."""
    PAGE_ID = "7794032641"
    TITLE = "Escalation Bug & Critical Code Flow Cross-Analysis Report"
    MD_FILE = os.path.join(EN_DIR, "escalation_bug_flow_hub.md")

    print(f"\n{'='*60}")
    print(f"Task 4: Deploy Hub/Index Page (replace original report)")
    print(f"  Source: {MD_FILE}")
    print(f"  Page ID: {PAGE_ID}")
    print(f"{'='*60}")

    with open(MD_FILE, 'r', encoding='utf-8') as f:
        md_content = f.read()

    print(f"  Converting markdown to Confluence HTML...")
    html_content = convert_markdown_to_confluence_html(md_content)

    os.makedirs(HTML_OUTPUT_DIR, exist_ok=True)
    html_path = os.path.join(HTML_OUTPUT_DIR, 'escalation_bug_flow_hub.html')
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html_content)
    print(f"  Saved HTML: {html_path} ({len(html_content)} chars)")

    # Get current version
    url = f"{CONFLUENCE_URL}/rest/api/content/{PAGE_ID}?expand=version"
    resp = requests.get(url, auth=(USERNAME, API_TOKEN))
    if resp.status_code != 200:
        print(f"  FAILED: Could not get page info ({resp.status_code})")
        return False
    version = resp.json()['version']['number']

    update_page(PAGE_ID, TITLE, html_content, version)
    print(f"  DONE: {CONFLUENCE_URL}/spaces/{SPACE_KEY}/pages/{PAGE_ID}")
    return True


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python deploy_new_pages.py all          # Deploy everything")
        print("  python deploy_new_pages.py escalation   # Deploy escalation report only")
        print("  python deploy_new_pages.py bugs         # Deploy bug files only")
        print("  python deploy_new_pages.py platforms    # Deploy platform-specific reports")
        print("  python deploy_new_pages.py hub          # Deploy hub/index page")
        sys.exit(1)

    target = sys.argv[1].lower()

    if target in ('all', 'escalation'):
        deploy_escalation_report()

    if target in ('all', 'platforms'):
        deploy_platform_reports()

    if target in ('all', 'bugs'):
        deploy_bugs()

    if target in ('all', 'hub'):
        deploy_hub_page()

    print("\n\nAll done!")
