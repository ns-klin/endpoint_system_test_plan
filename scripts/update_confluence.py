#!/usr/bin/env python3
"""
Update Confluence pages with converted HTML content
"""
import os
import requests
import json
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.normpath(os.path.join(SCRIPT_DIR, '..'))
HTML_OUTPUT_DIR = os.path.join(PROJECT_ROOT, 'html_output')

# Confluence credentials
CONFLUENCE_URL = "https://netskope.atlassian.net/wiki"
USERNAME = os.environ.get("CONFLUENCE_USERNAME", "klin@netskope.com")
API_TOKEN = os.environ["CONFLUENCE_API_TOKEN"]

def get_page_info(page_id):
    """Get current page info including version number"""
    url = f"{CONFLUENCE_URL}/rest/api/content/{page_id}"
    params = {
        'expand': 'version,space,ancestors'
    }

    response = requests.get(
        url,
        params=params,
        auth=(USERNAME, API_TOKEN)
    )

    if response.status_code != 200:
        print(f"Error getting page info: {response.status_code}")
        print(response.text)
        return None

    return response.json()

def update_page(page_id, title, html_content):
    """Update a Confluence page with new content"""
    # Get current page info
    page_info = get_page_info(page_id)
    if not page_info:
        return False

    current_version = page_info['version']['number']
    space_key = page_info['space']['key']

    # Prepare update payload
    url = f"{CONFLUENCE_URL}/rest/api/content/{page_id}"

    payload = {
        "id": page_id,
        "type": "page",
        "title": title,
        "space": {
            "key": space_key
        },
        "body": {
            "storage": {
                "value": html_content,
                "representation": "storage"
            }
        },
        "version": {
            "number": current_version + 1,
            "message": "Converted from markdown to proper Confluence storage format"
        }
    }

    headers = {
        "Content-Type": "application/json"
    }

    response = requests.put(
        url,
        data=json.dumps(payload),
        headers=headers,
        auth=(USERNAME, API_TOKEN)
    )

    if response.status_code == 200:
        page_url = f"{CONFLUENCE_URL}/spaces/{space_key}/pages/{page_id}"
        print(f"✓ Successfully updated: {title}")
        print(f"  URL: {page_url}")
        return True
    else:
        print(f"✗ Error updating {title}: {response.status_code}")
        print(response.text)
        return False

ALL_PAGES = [
    {"id": "7776206958", "title": "00. NSClient Architecture Overview", "html_file": os.path.join(HTML_OUTPUT_DIR, "00_overview.html")},
    {"id": "7775256801", "title": "01. Installation, Upgrade and Uninstallation", "html_file": os.path.join(HTML_OUTPUT_DIR, "01_installation.html")},
    {"id": "7772898132", "title": "02. Enrollment Flow", "html_file": os.path.join(HTML_OUTPUT_DIR, "02_enrollment.html")},
    {"id": "7776305272", "title": "03. Service Lifecycle", "html_file": os.path.join(HTML_OUTPUT_DIR, "03_service_lifecycle.html")},
    {"id": "7775715658", "title": "04. Config Download and Management", "html_file": os.path.join(HTML_OUTPUT_DIR, "04_config_download.html")},
    {"id": "7775682854", "title": "05. Traffic Steering Configuration", "html_file": os.path.join(HTML_OUTPUT_DIR, "05_steering_config.html")},
    {"id": "7775191215", "title": "06. Client Status Reporting", "html_file": os.path.join(HTML_OUTPUT_DIR, "06_client_status.html")},
    {"id": "7775420785", "title": "07. Tunnel Establishment and Management", "html_file": os.path.join(HTML_OUTPUT_DIR, "07_tunnel_management.html")},
    {"id": "7775453376", "title": "08. Gateway Selection (GSLB)", "html_file": os.path.join(HTML_OUTPUT_DIR, "08_gateway_selection.html")},
    {"id": "7775813750", "title": "09. Traffic Interception and Packet Processing", "html_file": os.path.join(HTML_OUTPUT_DIR, "09_traffic_steering.html")},
    {"id": "7775912130", "title": "10. Bypass Mechanism", "html_file": os.path.join(HTML_OUTPUT_DIR, "10_bypass.html")},
    {"id": "7775715680", "title": "11. FailClose Mechanism", "html_file": os.path.join(HTML_OUTPUT_DIR, "11_failclose.html")},
    {"id": "7775715699", "title": "12. Device Classification (DC)", "html_file": os.path.join(HTML_OUTPUT_DIR, "12_device_classification.html")},
    {"id": "7775355168", "title": "13. Certificate Management", "html_file": os.path.join(HTML_OUTPUT_DIR, "13_certificate_management.html")},
    {"id": "7775223994", "title": "14. Proxy Detection and Handling", "html_file": os.path.join(HTML_OUTPUT_DIR, "14_proxy_management.html")},
    {"id": "7773193015", "title": "15. NPA (Private Access) Integration", "html_file": os.path.join(HTML_OUTPUT_DIR, "15_npa_integration.html")},
    {"id": "7776305291", "title": "16. DEM (Digital Experience Monitoring)", "html_file": os.path.join(HTML_OUTPUT_DIR, "16_dem.html")},
    {"id": "7774602055", "title": "17. IPC Communication (NSCom2/NSMsg2)", "html_file": os.path.join(HTML_OUTPUT_DIR, "17_ipc_nscom2.html")},
    {"id": "7775781177", "title": "18. Security Mechanisms", "html_file": os.path.join(HTML_OUTPUT_DIR, "18_security.html")},
    {"id": "7775027357", "title": "19. Multi-Component Integration Architecture", "html_file": os.path.join(HTML_OUTPUT_DIR, "19_integration_architecture.html")},
    {"id": "7776141570", "title": "20. Supportability and Troubleshooting", "html_file": os.path.join(HTML_OUTPUT_DIR, "20_supportability.html")},
]

PARENT_PAGE_ID = "7764967482"  # Endpoint - System Testing


def main():
    import argparse

    parser = argparse.ArgumentParser(description="Update Confluence pages with HTML content")
    parser.add_argument("chapters", nargs="*", help="Chapter numbers to update (e.g. 01 05 07). If omitted, updates all.")
    args = parser.parse_args()

    if args.chapters:
        pages = [p for p in ALL_PAGES if any(os.path.basename(p["html_file"]).startswith(f"{c}_") for c in args.chapters)]
    else:
        pages = ALL_PAGES

    if not pages:
        print("No matching pages found.")
        return

    print(f"Will update {len(pages)} page(s):")
    for p in pages:
        print(f"  - {p['title']}")

    for page in pages:
        print(f"\nUpdating page: {page['title']}")

        try:
            with open(page['html_file'], 'r', encoding='utf-8') as f:
                html_content = f.read()
        except FileNotFoundError:
            print(f"  HTML file not found: {page['html_file']}")
            continue

        success = update_page(page['id'], page['title'], html_content)

        if not success:
            print(f"  Failed to update {page['title']}")

if __name__ == '__main__':
    main()
