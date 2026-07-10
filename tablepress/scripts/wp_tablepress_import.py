#!/usr/bin/env python3
"""
Create a TablePress table via WP Admin form (free plan compatible).
Returns the new table ID on success.

Usage:
  python3 wp_tablepress_import.py \
    --url https://bfshow.com.br \
    --user venturelabs --pass "v%8bNch!P$E0msO8maMIPET7" \
    --data '[["Col1","Col2"],["val1","val2"]]' \
    --name "Minha Tabela"
"""

import argparse
import json
import re
import sys
import requests


def login(session: requests.Session, base_url: str, username: str, password: str) -> bool:
    resp = session.post(
        f"{base_url}/wp-login.php",
        data={
            "log": username,
            "pwd": password,
            "wp-submit": "Log In",
            "redirect_to": "/wp-admin/",
            "testcookie": "1",
        },
        headers={"Cookie": "wordpress_test_cookie=WP+Cookie+check"},
        allow_redirects=True,
    )
    return "wp-admin" in resp.url or "dashboard" in resp.text


def get_import_nonce(session: requests.Session, base_url: str) -> str:
    resp = session.get(f"{base_url}/wp-admin/admin.php?page=tablepress&action=import")
    match = re.search(r'name="_wpnonce"\s+value="([^"]+)"', resp.text)
    if not match:
        # Try alternate pattern used in newer WP
        match = re.search(r'"_wpnonce":"([^"]+)"', resp.text)
    if not match:
        sys.exit("ERROR: Could not find nonce on import page. Check credentials.")
    return match.group(1)


def import_table(
    session: requests.Session,
    base_url: str,
    nonce: str,
    data: str,
    import_type: str = "add",
    existing_table: str = "",
) -> str:
    """Returns the new/updated table ID."""
    resp = session.post(
        f"{base_url}/wp-admin/admin.php?page=tablepress&action=import",
        data={
            "_wpnonce": nonce,
            "import[source]": "form-field",
            "import[type]": import_type,
            "import[form-field]": data,
            "import[existing_table]": existing_table,
        },
        allow_redirects=True,
    )
    # On success, WP redirects to edit screen: ?page=tablepress&action=edit&table_id=N
    match = re.search(r"table_id=([^&\"'\s]+)", resp.url)
    if match:
        return match.group(1)
    # Fallback: search in response body
    match = re.search(r"table_id=([^&\"'\s]+)", resp.text)
    if match:
        return match.group(1)
    sys.exit(f"ERROR: Import failed or could not extract table ID.\nFinal URL: {resp.url}")


def rename_table(session: requests.Session, base_url: str, table_id: str, name: str) -> None:
    """Update table name via the AJAX save endpoint."""
    # Get edit page nonce first
    resp = session.get(f"{base_url}/wp-admin/admin.php?page=tablepress&action=edit&table_id={table_id}")
    match = re.search(r'"_ajax_nonce":"([^"]+)"', resp.text)
    if not match:
        print(f"  WARNING: Could not rename table to '{name}' (nonce not found). Rename manually in WP Admin.")
        return
    ajax_nonce = match.group(1)
    session.post(
        f"{base_url}/wp-admin/admin-ajax.php",
        data={
            "action": "tablepress_save_table",
            "_ajax_nonce": ajax_nonce,
            "tablepress[id]": table_id,
            "tablepress[name]": name,
            "tablepress[data]": "[]",  # empty — just updating name
        },
    )


def main():
    parser = argparse.ArgumentParser(description="Import a table into TablePress via WP Admin.")
    parser.add_argument("--url", required=True, help="WordPress base URL, no trailing slash")
    parser.add_argument("--user", required=True, help="WP username")
    parser.add_argument("--pass", dest="password", required=True, help="WP password")
    parser.add_argument("--data", required=True, help="JSON 2D array or CSV string")
    parser.add_argument("--name", default="", help="Table name (optional)")
    parser.add_argument("--type", default="add", choices=["add", "replace", "append"], help="Import type")
    parser.add_argument("--existing-table", default="", help="Existing table ID (for replace/append)")
    args = parser.parse_args()

    session = requests.Session()
    session.headers["User-Agent"] = "Mozilla/5.0 (compatible; TablePress-Script)"

    print(f"Logging in to {args.url}...")
    if not login(session, args.url, args.user, args.password):
        sys.exit("ERROR: Login failed. Check credentials.")
    print("  Login OK")

    print("Fetching import nonce...")
    nonce = get_import_nonce(session, args.url)
    print(f"  Nonce: {nonce[:8]}...")

    # Validate JSON if provided
    data = args.data
    try:
        parsed = json.loads(data)
        data = json.dumps(parsed)  # normalize whitespace
        print(f"  Data: JSON with {len(parsed)} rows")
    except json.JSONDecodeError:
        print(f"  Data: CSV ({len(data.splitlines())} lines)")

    print(f"Importing table (type={args.type})...")
    table_id = import_table(session, args.url, nonce, data, args.type, args.existing_table)
    print(f"  Table ID: {table_id}")

    if args.name:
        print(f"Setting table name to '{args.name}'...")
        rename_table(session, args.url, table_id, args.name)

    print(f"\nDone! Embed with: [table id={table_id} /]")
    print(f"Edit at: {args.url}/wp-admin/admin.php?page=tablepress&action=edit&table_id={table_id}")
    return table_id


if __name__ == "__main__":
    main()
