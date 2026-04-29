#!/usr/bin/env python3
"""
Convert markdown to Confluence storage format HTML
"""
import re
import html

def escape_html(text):
    """Escape HTML special characters"""
    return html.escape(text)

def convert_code_block(match):
    """Convert markdown code block to Confluence macro"""
    lang = match.group(1) or ""
    code = match.group(2)

    # Escape the code content
    code = code.strip()

    result = '<ac:structured-macro ac:name="code">'
    if lang:
        result += f'<ac:parameter ac:name="language">{lang}</ac:parameter>'
    result += f'<ac:plain-text-body><![CDATA[{code}]]></ac:plain-text-body>'
    result += '</ac:structured-macro>'

    return result

def convert_inline_code(match):
    """Convert inline code to Confluence code tag"""
    code = match.group(1)
    return f'<code>{escape_html(code)}</code>'

def convert_headers(line):
    """Convert markdown headers to HTML headers"""
    match = re.match(r'^(#{1,6})\s+(.+)$', line)
    if match:
        level = len(match.group(1))
        text = match.group(2)
        return f'<h{level}>{escape_html(text)}</h{level}>'
    return None

def convert_bold(text):
    """Convert **bold** to <strong>"""
    text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
    return text

def convert_italic(text):
    """Convert *italic* to <em>"""
    text = re.sub(r'\*(.+?)\*', r'<em>\1</em>', text)
    return text

def convert_links(text):
    """Convert [text](url) to <a href>"""
    text = re.sub(r'\[([^\]]+)\]\(([^\)]+)\)', r'<a href="\2">\1</a>', text)
    return text

def convert_table_row(line, is_header=False):
    """Convert markdown table row to HTML"""
    cells = [cell.strip() for cell in line.split('|')[1:-1]]
    tag = 'th' if is_header else 'td'

    result = '<tr>'
    for cell in cells:
        cell_content = convert_inline_formatting(cell)
        result += f'<{tag}>{cell_content}</{tag}>'
    result += '</tr>'

    return result

def convert_inline_formatting(text):
    """Apply inline formatting conversions"""
    # Inline code first (to avoid processing code content)
    text = re.sub(r'`([^`]+)`', lambda m: f'<code>{escape_html(m.group(1))}</code>', text)

    # Bold
    text = convert_bold(text)

    # Italic (careful not to match **bold**)
    text = re.sub(r'(?<!\*)\*([^\*]+?)\*(?!\*)', r'<em>\1</em>', text)

    # Links
    text = convert_links(text)

    return text

def convert_markdown_to_confluence(markdown_content):
    """Main conversion function"""
    lines = markdown_content.split('\n')
    html_lines = []

    in_code_block = False
    code_block_lang = ""
    code_block_content = []

    in_table = False
    table_rows = []

    in_list = False
    list_items = []
    list_type = None  # 'ul' or 'ol'

    i = 0
    while i < len(lines):
        line = lines[i]

        # Code block detection
        if line.startswith('```'):
            if not in_code_block:
                # Start code block
                in_code_block = True
                code_block_lang = line[3:].strip()
                code_block_content = []
            else:
                # End code block
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

        # Table detection
        if '|' in line and line.strip().startswith('|'):
            if not in_table:
                in_table = True
                table_rows = []

            # Check if it's a separator row
            if re.match(r'^\|[\s\-:|]+\|$', line):
                i += 1
                continue

            # Add table row
            is_header = len(table_rows) == 0
            table_rows.append(convert_table_row(line, is_header))

            # Check if next line is not a table row
            if i + 1 >= len(lines) or not lines[i + 1].strip().startswith('|'):
                # End table
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

            # Check if next line is not a list item
            if i + 1 >= len(lines) or not re.match(r'^(\s*)([-*]|\d+\.)\s+', lines[i + 1]):
                # End list
                html_lines.extend(list_items)
                html_lines.append(f'</{list_type}>')

                in_list = False
                list_items = []
                list_type = None

            i += 1
            continue

        # Header detection
        header = convert_headers(line)
        if header:
            html_lines.append(header)
            i += 1
            continue

        # Horizontal rule
        if re.match(r'^---+$', line):
            html_lines.append('<hr />')
            i += 1
            continue

        # Empty line
        if not line.strip():
            # Skip empty lines in output (Confluence handles spacing differently)
            i += 1
            continue

        # Regular paragraph
        paragraph = convert_inline_formatting(line)
        html_lines.append(f'<p>{paragraph}</p>')

        i += 1

    return '\n'.join(html_lines)

if __name__ == '__main__':
    import sys

    if len(sys.argv) < 2:
        print("Usage: python convert_to_confluence.py <markdown_file>")
        sys.exit(1)

    with open(sys.argv[1], 'r', encoding='utf-8') as f:
        markdown = f.read()

    html = convert_markdown_to_confluence(markdown)
    print(html)
