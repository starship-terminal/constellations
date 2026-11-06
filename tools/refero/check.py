#!/usr/bin/env python3
"""Check that the three refero stores agree.

    python3 tools/refero/check.py [--refero DIR]

The stores: the styles rows in refero.db, the refero/<slug>/ folders and
their meta.json, and the committed refero/catalog.json. Every disagreement
is printed and the exit code is 1 when any is found.

File-only safe: when refero.db is missing or is not a readable sqlite (a
clone without `git lfs pull` holds the LFS pointer file), the folder and
catalog checks still run and the db side is skipped with a note.
"""

import argparse
import json
import re
import sqlite3
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REFERO = ROOT / "refero"

# The files every style folder carries. prompt.txt lives only in the db
# (refero/README.md).
STYLE_FILES = ("meta.json", "design-system.json", "DESIGN.md", "variables.css",
               "theme.css", "tokens.json")

# styles columns catalog.json entries repeat, in either's key naming.
CATALOG_FIELDS = ("slug", "name", "tagline", "uuid", "page_url", "source_url",
                  "theme", "product_type", "design_style", "tags",
                  "extracted_at", "fetched_at")
# meta.json repeats the media URLs on top of the catalog fields.
META_FIELDS = CATALOG_FIELDS + ("screenshot_url", "video_url", "video_poster_url",
                                "video_detail_url", "video_detail_poster_url")


def norm(field, value):
    """tags is a JSON string in the db and catalog, an array in meta.json."""
    if field == "tags":
        if isinstance(value, str):
            try:
                return json.loads(value)
            except json.JSONDecodeError:
                return value
        return value or []
    return value


def open_db(refero: Path):
    """(db connection, why-not string). A missing or non-sqlite refero.db is
    not a failure: clones without `git lfs pull` still check the rest."""
    path = refero / "refero.db"
    if not path.is_file():
        return None, "no refero.db"
    try:
        db = sqlite3.connect(f"file:{path}?mode=ro", uri=True)
    except sqlite3.Error:
        return None, "refero.db is not a readable sqlite database (LFS pointer?)"
    try:
        db.row_factory = sqlite3.Row
        db.execute("SELECT 1 FROM styles LIMIT 1").fetchone()
    except sqlite3.Error:
        db.close()
        return None, "refero.db is not a readable sqlite database (LFS pointer?)"
    return db, None


def check(refero: Path) -> list[str]:
    problems = []

    # ---- style folders: files present, meta.json parses, slug matches the dir
    metas: dict[str, dict] = {}
    dirs = sorted(p for p in refero.iterdir()
                  if p.is_dir() and not p.name.startswith("."))
    for folder in dirs:
        tag = f"refero/{folder.name}"
        for name in STYLE_FILES:
            if not (folder / name).is_file():
                problems.append(f"{tag}: {name} is missing")
        try:
            meta = json.loads((folder / "meta.json").read_text())
        except (OSError, json.JSONDecodeError) as e:
            problems.append(f"{tag}: meta.json does not parse: {e}")
            continue
        if not isinstance(meta, dict):
            problems.append(f"{tag}: meta.json is not an object")
            continue
        metas[folder.name] = meta
        if meta.get("slug") != folder.name:
            problems.append(f"{tag}: meta.json slug is {meta.get('slug')!r}")
        if (folder / "design-system.json").is_file():
            try:
                json.loads((folder / "design-system.json").read_text())
            except (OSError, json.JSONDecodeError) as e:
                problems.append(f"{tag}: design-system.json does not parse: {e}")
    meta_uuids = [m.get("uuid") for m in metas.values()]
    for uuid in sorted({u for u in meta_uuids if u and meta_uuids.count(u) > 1}):
        problems.append(f"uuid {uuid} appears in more than one meta.json")

    # ---- catalog.json: parses, slugs unique, count agrees
    catalog: dict[str, dict] = {}
    cat_path = refero / "catalog.json"
    try:
        cat = json.loads(cat_path.read_text())
    except (OSError, json.JSONDecodeError) as e:
        problems.append(f"refero/catalog.json does not parse: {e}")
        cat = None
    if cat is not None:
        if not isinstance(cat, dict) or not isinstance(cat.get("styles"), list):
            problems.append("refero/catalog.json: styles is not a list")
        else:
            for entry in cat["styles"]:
                if not isinstance(entry, dict):
                    problems.append("refero/catalog.json: a styles entry is not an object")
                    continue
                slug = entry.get("slug")
                if slug in catalog:
                    problems.append(f"refero/catalog.json: slug {slug} appears twice")
                catalog[slug] = entry
            if cat.get("count") != len(cat["styles"]):
                problems.append(f"refero/catalog.json: count {cat.get('count')} "
                                f"!= {len(cat['styles'])} styles")

    # ---- refero.db: slugs/uuids unique, fetch_errors empty. None when the db
    # cannot be opened; the db-pair checks below are skipped then.
    rows: dict[str, dict] | None = None
    db, why = open_db(refero)
    if db is None:
        print(f"note: {why}; checking folders and catalog.json only", file=sys.stderr)
    else:
        rows = {}
        for row in db.execute("SELECT * FROM styles"):
            row = dict(row)
            slug = row.get("slug")
            if slug in rows:
                problems.append(f"refero.db: slug {slug} appears twice")
            rows[slug] = row
        uuids = [r["uuid"] for r in rows.values()]
        for uuid in sorted({u for u in uuids if uuids.count(u) > 1}):
            problems.append(f"refero.db: uuid {uuid} appears twice")
        try:
            errors = db.execute("SELECT count(*) FROM fetch_errors").fetchone()[0]
        except sqlite3.Error as e:
            problems.append(f"refero.db: cannot read fetch_errors: {e}")
        else:
            if errors:
                problems.append(f"refero.db: fetch_errors holds {errors} rows")
        db.close()

    # ---- the stores' slug sets agree
    for slug in sorted(set(metas) - set(catalog)):
        problems.append(f"refero/{slug}: no catalog.json entry")
    for slug in sorted(set(catalog) - set(metas)):
        problems.append(f"refero/catalog.json: {slug} has no refero/{slug}/ folder")
    if rows is not None:
        for slug in sorted(set(metas) - set(rows)):
            problems.append(f"refero/{slug}: no styles row in refero.db")
        for slug in sorted(set(rows) - set(metas)):
            problems.append(f"refero.db: {slug} has no refero/{slug}/ folder")
        for slug in sorted(set(catalog) - set(rows)):
            problems.append(f"refero/catalog.json: {slug} has no styles row in refero.db")

        # ---- field agreement: meta.json and catalog entry against the db row
        for slug in sorted(set(metas) & set(rows)):
            meta, row = metas[slug], rows[slug]
            for field in META_FIELDS:
                if norm(field, meta.get(field)) != norm(field, row.get(field)):
                    problems.append(f"refero/{slug}: meta.json {field} "
                                    f"does not match the styles row")
        for slug in sorted(set(catalog) & set(rows)):
            entry, row = catalog[slug], rows[slug]
            for field in CATALOG_FIELDS:
                if norm(field, entry.get(field)) != norm(field, row.get(field)):
                    problems.append(f"refero/catalog.json: {slug} {field} "
                                    f"does not match the styles row")
    else:
        # Without the db, meta.json is the row's stand-in: the catalog fields
        # it shares with meta.json are still compared.
        for slug in sorted(set(metas) & set(catalog)):
            meta, entry = metas[slug], catalog[slug]
            for field in CATALOG_FIELDS:
                if norm(field, entry.get(field)) != norm(field, meta.get(field)):
                    problems.append(f"refero/catalog.json: {slug} {field} "
                                    f"does not match meta.json")

    # ---- refero/README.md's stated style count stays honest
    readme = refero / "README.md"
    if readme.is_file():
        m = re.search(r"([\d,]+)\s+styles", readme.read_text())
        if m and int(m.group(1).replace(",", "")) != len(dirs):
            problems.append(f"refero/README.md says {m.group(1)} styles; "
                            f"{len(dirs)} folders exist")
    return problems


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--refero", type=Path, default=REFERO,
                    help="the refero/ folder to check (default: the repo's)")
    args = ap.parse_args()
    if not args.refero.is_dir():
        sys.exit(f"{args.refero} is not a folder")
    problems = check(args.refero)
    print("\n".join(problems) if problems else "refero ok")
    sys.exit(1 if problems else 0)


if __name__ == "__main__":
    main()
