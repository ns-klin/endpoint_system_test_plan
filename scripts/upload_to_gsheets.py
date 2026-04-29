#!/usr/bin/env python3
"""
Upload TC CSV files to Google Sheets.

Prerequisites:
    pip3 install gspread google-auth

Authentication:
    Option 1: Service account — place credentials JSON at ~/.config/gspread/service_account.json
    Option 2: OAuth — run `gspread` auth flow (will open browser)

Usage:
    python3 upload_to_gsheets.py
"""

import os
import csv
import sys

try:
    import gspread
except ImportError:
    print("ERROR: gspread not installed. Run:")
    print("  pip3 install gspread google-auth")
    sys.exit(1)

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.normpath(os.path.join(SCRIPT_DIR, '..'))

SPREADSHEET_ID = "1ackCZ-EcepXw1BkSGoi5Go9Ex1I72-fXqcqLGMGiuio"
TC_EXPORT_DIR = os.path.join(PROJECT_ROOT, "tc_export")

# Sheet names matching chapter numbers
SHEET_NAMES = {
    "01": "01 Installation",
    "02": "02 Enrollment",
    "03": "03 Service Lifecycle",
    "04": "04 Config Download",
    "05": "05 Steering Config",
    "06": "06 Client Status",
    "07": "07 Tunnel Mgmt",
    "08": "08 Gateway Selection",
    "09": "09 Traffic Steering",
    "10": "10 Bypass",
    "11": "11 FailClose",
    "12": "12 Device Classification",
    "13": "13 Certificate Mgmt",
    "14": "14 Proxy Management",
    "15": "15 NPA Integration",
    "16": "16 DEM",
    "17": "17 IPC NSCom2",
    "18": "18 Security",
    "19": "19 Integration",
    "20": "20 Supportability",
    "21": "21 Watchdog",
}


def get_csv_files():
    """Get all CSV files from tc_export directory, sorted by chapter number."""
    files = []
    for f in sorted(os.listdir(TC_EXPORT_DIR)):
        if f.endswith('.csv') and f[:2].isdigit() and f != "00_SUMMARY.csv":
            files.append(os.path.join(TC_EXPORT_DIR, f))
    return files


def read_csv(filepath):
    """Read CSV file and return as list of lists."""
    with open(filepath, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        return list(reader)


def main():
    print("Authenticating with Google Sheets...")

    # Try service account first, then OAuth
    auth_method = None
    try:
        gc = gspread.service_account()
        auth_method = "service_account"
    except Exception:
        pass

    if not auth_method:
        # Try OAuth with credentials.json in the default gspread directory
        creds_dir = os.path.expanduser("~/.config/gspread")
        creds_file = os.path.join(creds_dir, "credentials.json")

        if not os.path.exists(creds_file):
            print(f"\nNo credentials found at {creds_file}")
            print("\nTo set up authentication:")
            print("  1. Go to https://console.cloud.google.com/apis/credentials")
            print("  2. Create an OAuth 2.0 Client ID (Desktop App)")
            print("  3. Download the JSON file")
            print(f"  4. Save it as: {creds_file}")
            print("  5. Re-run this script (it will open a browser for auth)")
            print(f"\n  mkdir -p {creds_dir}")
            print(f"  mv ~/Downloads/client_secret_*.json {creds_file}")
            sys.exit(1)

        try:
            gc = gspread.oauth()
            auth_method = "oauth"
        except Exception as e:
            print(f"OAuth failed: {e}")
            sys.exit(1)

    print(f"  Authenticated via {auth_method}")

    print(f"Opening spreadsheet: {SPREADSHEET_ID}")
    try:
        sh = gc.open_by_key(SPREADSHEET_ID)
    except Exception as e:
        print(f"Failed to open spreadsheet: {e}")
        sys.exit(1)

    existing_sheets = {ws.title: ws for ws in sh.worksheets()}
    csv_files = get_csv_files()

    for filepath in csv_files:
        chapter_num = os.path.basename(filepath)[:2]
        sheet_name = SHEET_NAMES.get(chapter_num, f"Ch{chapter_num}")
        data = read_csv(filepath)

        if not data:
            continue

        rows = len(data)
        cols = len(data[0]) if data else 0

        print(f"  Writing {sheet_name}: {rows - 1} test cases...", end=" ")

        try:
            if sheet_name in existing_sheets:
                ws = existing_sheets[sheet_name]
                ws.clear()
                ws.resize(rows=rows, cols=cols)
            else:
                ws = sh.add_worksheet(title=sheet_name, rows=rows, cols=cols)

            ws.update(range_name='A1', values=data)

            # Format header row (bold)
            ws.format('1:1', {'textFormat': {'bold': True}})

            print("OK")
        except Exception as e:
            print(f"FAILED: {e}")

    # Write summary sheet
    summary_path = os.path.join(TC_EXPORT_DIR, "00_SUMMARY.csv")
    if os.path.exists(summary_path):
        summary_data = read_csv(summary_path)
        sheet_name = "Summary"
        print(f"  Writing {sheet_name}...", end=" ")
        try:
            if sheet_name in existing_sheets:
                ws = existing_sheets[sheet_name]
                ws.clear()
            else:
                ws = sh.add_worksheet(title=sheet_name, rows=len(summary_data), cols=3)
            ws.update(range_name='A1', values=summary_data)
            ws.format('1:1', {'textFormat': {'bold': True}})
            print("OK")
        except Exception as e:
            print(f"FAILED: {e}")

    print("\nDone! Check your spreadsheet.")


if __name__ == "__main__":
    main()
