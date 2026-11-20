#!/usr/bin/env python3
"""Fetch the refero.design catalog directory and its preview screenshots.

    python3 tools/refero/fetch_screens.py [--refero DIR]

Two calls to api.refero.design's public /v1/*/available endpoints yield the
paid catalog directory (~312 iOS apps, ~439 web sites) and each entry's
five preview screenshots. Rows land in the `screens` table of refero.db —
one row per shot with the exact captured page_url (web only; iOS screens
carry page_id instead), thumbnail and the extracted colour palette — and
refero/directory.json is regenerated with the same screens embedded per
entry.

This is third-party index data over Refero's paid catalog: names, domains,
shot URLs and metadata only — the screenshot library itself is not
mirrored. The /v1/search endpoint exposes per-shot design_patterns and
page_elements tags; the preview records here do not, so patterns_json and
elements_json stay NULL until a separate pass fills them.
"""

import argparse
import json
import re
import sqlite3
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REFERO = ROOT / "refero"
DB = REFERO / "refero.db"
API = "https://api.refero.design"

sys.path.insert(0, str(Path(__file__).resolve().parent))
import fetch  # noqa: E402
import dump as refero_dump  # noqa: E402  (refreshes refero/.dump/ after a write)

SCHEMA = """
CREATE TABLE IF NOT EXISTS screens (
  entry_type TEXT,     -- 'ios' or 'web'
  entry_id INTEGER,    -- upstream numeric id
  entry_key TEXT,      -- domain for web, App Store numeric id for iOS
  shot_uuid TEXT,
  shot_url TEXT,       -- first url of the record's url field (web full pages
                       -- are multi-part arrays; the rest share the prefix)
  thumb_url TEXT,
  page_url TEXT,       -- exact captured URL, NULL for iOS screens
  page_id INTEGER,
  colors_json TEXT,    -- extracted 5-swatch RGB palette
  patterns_json TEXT,  -- NULL until a tag pass fills it
  elements_json TEXT,  -- NULL until a tag pass fills it
  shot_created_at TEXT,
  fetched_at TEXT
);
"""


def first_url(url):
    return url[0] if isinstance(url, list) and url else \
        url if isinstance(url, str) else None


def screens_for(entry_type, entry_id, entry_key, record, fetched_at):
    rows = []
    for shot in record.get("screenshots") or []:
        rows.append({
            "entry_type": entry_type,
            "entry_id": entry_id,
            "entry_key": entry_key,
            "shot_uuid": shot.get("uuid"),
            "shot_url": first_url(shot.get("url")),
            "thumb_url": shot.get("thumbnail_url"),
            "page_url": shot.get("page_url"),
            "page_id": shot.get("page_id"),
            "colors": shot.get("colors"),
            "shot_created_at": shot.get("created_at"),
            "fetched_at": fetched_at,
        })
    return rows


def app_store_id(store_url):
    m = re.search(r"/id(\d+)", store_url or "")
    return m.group(1) if m else None


# Each listing is one request of up to PER_PAGE records. The endpoints are
# not paged here, so a full page may have cut the listing short.
PER_PAGE = 500


def available(kind):
    """The records of /v1/<kind>/available. Exits, before anything is
    written, when the reply fills a whole page: the directory, the screens
    table and coverage.json would silently drop every entry past it."""
    records = json.loads(fetch.get(
        f"{API}/v1/{kind}/available?per_page={PER_PAGE}"))["records"]
    if len(records) >= PER_PAGE:
        sys.exit(f"error: /v1/{kind}/available returned {len(records)} records, "
                 f"a full page of {PER_PAGE}: the listing may be truncated. Raise "
                 "PER_PAGE or page through it before refreshing the directory.")
    return records


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--refero", type=Path, default=REFERO,
                    help="the refero/ folder to write (default: the repo's)")
    args = ap.parse_args()
    refero = args.refero
    db_path = refero / "refero.db"

    fetched_at = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    ios = available("apps")
    web = available("sites")
    print(f"api: {len(ios)} iOS apps, {len(web)} web sites")

    screens, ios_apps, web_sites = [], [], []
    for r in ios:
        key = app_store_id(r.get("store_url"))
        rows = screens_for("ios", r["id"], key, r, fetched_at)
        screens += rows
        ios_apps.append({
            "id": r["id"], "name": r.get("name"),
            "description": r.get("description"),
            "store_url": r.get("store_url"),
            "icon_url": r.get("icon_url"),
            "screens": [{
                "uuid": s["shot_uuid"], "url": s["shot_url"],
                "thumb": s["thumb_url"], "page_id": s["page_id"],
                "palette": s["colors"]} for s in rows],
        })
    for r in web:
        rows = screens_for("web", r["id"], r.get("domain"), r, fetched_at)
        screens += rows
        web_sites.append({
            "id": r["id"], "name": r.get("name"),
            "domain": r.get("domain"),
            "description": r.get("description"),
            "favicon_url": r.get("favicon_url"),
            "screens": [{
                "uuid": s["shot_uuid"], "url": s["shot_url"],
                "thumb": s["thumb_url"], "page_url": s["page_url"],
                "page_id": s["page_id"],
                "palette": s["colors"]} for s in rows],
        })

    if db_path.exists():
        with open(db_path, "rb") as f:
            if f.read(64).startswith(b"version https://git-lfs"):
                sys.exit("error: refero.db is a Git LFS pointer; "
                         "run: git lfs install && git lfs pull")
    # Autocommit mode plus an explicit transaction: the legacy implicit one
    # never covers DROP or CREATE (and executescript commits first), so a
    # failed insert would leave the table dropped or empty.
    db = sqlite3.connect(db_path, isolation_level=None)
    db.execute("PRAGMA busy_timeout=30000")
    db.execute("BEGIN IMMEDIATE")
    try:
        db.execute("DROP TABLE IF EXISTS screens")
        db.execute(SCHEMA)
        db.executemany(
            """INSERT INTO screens
               (entry_type, entry_id, entry_key, shot_uuid, shot_url,
                thumb_url, page_url, page_id, colors_json, patterns_json,
                elements_json, shot_created_at, fetched_at)
               VALUES (?,?,?,?,?,?,?,?,?,NULL,NULL,?,?)""",
            [(s["entry_type"], s["entry_id"], s["entry_key"], s["shot_uuid"],
              s["shot_url"], s["thumb_url"], s["page_url"], s["page_id"],
              json.dumps(s["colors"]) if s["colors"] else None,
              s["shot_created_at"], s["fetched_at"]) for s in screens])
        db.execute("COMMIT")
    except BaseException:
        db.execute("ROLLBACK")
        raise
    finally:
        db.close()
    refero_dump.refresh(db_path)

    directory = {
        "version": 1,
        "about": "Directory of the refero.design paid catalog (iOS apps + "
                 "web sites) with each entry's five preview screenshots — "
                 "names, domains, shot URLs, palettes and captured page URLs "
                 "from api.refero.design /v1/*/available. Third-party index "
                 "data; the screenshot library and flows themselves are not "
                 "mirrored.",
        "source": API,
        "fetched_at": fetched_at,
        "ios_apps": ios_apps,
        "web_sites": web_sites,
    }
    fetch.write_atomic(refero / "directory.json",
                       json.dumps(directory, indent=2, ensure_ascii=False)
                       + "\n")
    with_page_url = sum(1 for s in screens if s["page_url"])
    print(f"screens: {len(screens)} rows "
          f"({with_page_url} web shots with page_url)")


if __name__ == "__main__":
    main()
