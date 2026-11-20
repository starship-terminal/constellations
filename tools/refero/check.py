#!/usr/bin/env python3
"""Check that the refero stores agree.

    python3 tools/refero/check.py [--refero DIR]

The stores: the styles rows in refero.db, the refero/<slug>/ folders and
their meta.json (+ components.json where upstream shipped markup), the
committed refero/catalog.json, and the derived stores — similar table vs
similar.json, collections tables vs collections.json, screens table vs
directory.json, coverage.json vs a recomputation. Every disagreement is
printed and the exit code is 1 when any is found.

The committed text dump in refero/.dump/ must be exactly what
tools/refero/dump.py writes from refero.db (the dump is the merge surface).

File-only safe: when refero.db is missing or is not a readable sqlite (a
clone without `git lfs pull` holds the LFS pointer file), the folder and
catalog checks still run and the db side (dump comparison included) is
skipped with a note.
"""

import argparse
import json
import re
import sqlite3
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REFERO = ROOT / "refero"

sys.path.insert(0, str(Path(__file__).resolve().parent))
import coverage as coverage_mod  # noqa: E402  (sibling module)
import dump as refero_dump  # noqa: E402  (sibling module)

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import catalog  # noqa: E402  (tools/catalog.py)

# The files every style folder carries. prompt.txt lives only in the db
# (refero/README.md).
STYLE_FILES = ("meta.json", "design-system.json", "DESIGN.md", "variables.css",
               "theme.css", "tokens.json")

# styles columns catalog.json entries repeat, in either's key naming.
CATALOG_FIELDS = ("slug", "name", "tagline", "uuid", "page_url", "source_url",
                  "theme", "product_type", "design_style", "tags",
                  "extracted_at", "fetched_at")
# catalog.json entries also carry fields derived from the component columns
# and the similar/collections tables; checked against those stores, not the
# styles row itself.
CATALOG_DERIVED_FIELDS = ("has_components", "similar", "collections")
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
        if (folder / "components.json").is_file():
            try:
                comps = json.loads((folder / "components.json").read_text())
                if not isinstance(comps, list):
                    problems.append(f"{tag}: components.json is not a list")
            except (OSError, json.JSONDecodeError) as e:
                problems.append(f"{tag}: components.json does not parse: {e}")
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
    tables: set[str] = set()
    sim_map: dict[str, list] = {}
    coll_map: dict[str, set] = {}
    similar_styles = ncoll = nscreens = 0
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
        tables = {r[0] for r in db.execute(
            "SELECT name FROM sqlite_master WHERE type='table'")}
        if "similar" in tables:
            for u, s in db.execute(
                    "SELECT uuid, matched_slug FROM similar "
                    "WHERE matched_slug IS NOT NULL ORDER BY uuid, rank"):
                sim_map.setdefault(u, []).append(s)
            similar_styles = db.execute(
                "SELECT COUNT(DISTINCT uuid) FROM similar").fetchone()[0]
        if "collection_styles" in tables:
            for u, c in db.execute(
                    "SELECT style_uuid, collection_slug "
                    "FROM collection_styles"):
                coll_map.setdefault(u, set()).add(c)
        if "collections" in tables:
            ncoll = db.execute("SELECT COUNT(*) FROM collections").fetchone()[0]
        if "screens" in tables:
            nscreens = db.execute("SELECT COUNT(*) FROM screens").fetchone()[0]
        db.close()
        # ---- the committed text dump (refero/.dump/, the merge surface) is
        # exactly what the db dumps to
        try:
            problems += refero_dump.compare(refero / "refero.db")
        except (refero_dump.DumpError, sqlite3.Error, OSError) as e:
            problems.append(f"refero/{refero_dump.DUMP_DIRNAME}: cannot compare "
                            f"with refero.db: {e}")

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
            has_data = row.get("components_json") is not None
            has_file = (refero / slug / "components.json").is_file()
            if has_file != has_data:
                problems.append(
                    f"refero/{slug}: components.json "
                    f"{'missing for' if has_data else 'present but'}"
                    f" a styles row with{'out' if has_data else ''}"
                    f" components_json")
            if bool(meta.get("has_components", False)) != has_data:
                problems.append(f"refero/{slug}: meta.json has_components "
                                f"does not match the styles row")
        for slug in sorted(set(catalog) & set(rows)):
            entry, row = catalog[slug], rows[slug]
            for field in CATALOG_FIELDS:
                if norm(field, entry.get(field)) != norm(field, row.get(field)):
                    problems.append(f"refero/catalog.json: {slug} {field} "
                                    f"does not match the styles row")
            if "has_components" in entry and bool(entry["has_components"]) \
                    != (row.get("components_json") is not None):
                problems.append(f"refero/catalog.json: {slug} has_components "
                                f"does not match the styles row")
            if "similar" in entry and entry["similar"] \
                    != sim_map.get(row["uuid"], []):
                problems.append(f"refero/catalog.json: {slug} similar "
                                f"does not match the similar table")
            if "collections" in entry and entry["collections"] \
                    != sorted(coll_map.get(row["uuid"], ())):
                problems.append(f"refero/catalog.json: {slug} collections "
                                f"does not match the collection_styles table")

        # ---- derived index files match their db tables
        if "similar" in tables:
            try:
                sj = json.loads((refero / "similar.json").read_text())
                n = len(sj.get("styles") or [])
                if sj.get("count") != similar_styles or n != similar_styles:
                    problems.append(
                        "refero/similar.json: styles count does not match "
                        "the similar table")
            except (OSError, json.JSONDecodeError) as e:
                problems.append(f"refero/similar.json does not parse: {e}")
        if "collections" in tables:
            try:
                cj = json.loads((refero / "collections.json").read_text())
                n = len(cj.get("collections") or [])
                if cj.get("count") != ncoll or n != ncoll:
                    problems.append(
                        "refero/collections.json: collections count does not "
                        "match the collections table")
            except (OSError, json.JSONDecodeError) as e:
                problems.append(f"refero/collections.json does not parse: {e}")
        if "screens" in tables:
            try:
                dj = json.loads((refero / "directory.json").read_text())
                n = sum(len(e.get("screens") or [])
                        for k in ("ios_apps", "web_sites")
                        for e in (dj.get(k) or []))
                if n != nscreens:
                    problems.append(
                        "refero/directory.json: embedded screens do not "
                        "match the screens table")
            except (OSError, json.JSONDecodeError) as e:
                problems.append(f"refero/directory.json does not parse: {e}")
    else:
        # Without the db, meta.json is the row's stand-in: the catalog fields
        # it shares with meta.json are still compared.
        for slug in sorted(set(metas) & set(catalog)):
            meta, entry = metas[slug], catalog[slug]
            for field in CATALOG_FIELDS:
                if norm(field, entry.get(field)) != norm(field, meta.get(field)):
                    problems.append(f"refero/catalog.json: {slug} {field} "
                                    f"does not match meta.json")

    # ---- coverage.json: a generated diff (directory.json x the systems
    # catalog.json); recompute it and demand the file match exactly.
    # On a pull request the file may lag packages the merge adds; it must
    # still be the exact derivation of the packages it names.
    try:
        directory = json.loads((refero / "directory.json").read_text())
        systems_cat = json.loads((ROOT / "catalog.json").read_text())
    except (OSError, json.JSONDecodeError):
        directory = systems_cat = None
    if directory is not None and systems_cat is not None:
        expected_cov = coverage_mod.build(directory, systems_cat)
        try:
            actual_cov = json.loads((refero / "coverage.json").read_text())
        except (OSError, json.JSONDecodeError) as e:
            problems.append(f"refero/coverage.json does not parse: {e}")
        else:
            if actual_cov != expected_cov and not coverage_matches_base(
                    directory, systems_cat, actual_cov, expected_cov):
                problems.append("refero/coverage.json is stale; "
                                "run tools/refero/coverage.py")

    # ---- refero/README.md's stated style count stays honest
    readme = refero / "README.md"
    if readme.is_file():
        m = re.search(r"([\d,]+)\s+styles", readme.read_text())
        if m and int(m.group(1).replace(",", "")) != len(dirs):
            problems.append(f"refero/README.md says {m.group(1)} styles; "
                            f"{len(dirs)} folders exist")
    return problems


def coverage_matches_base(directory: dict, head_catalog: dict,
                          actual: dict, expected: dict) -> bool:
    """True when GitHub is checking a pull request and the committed file is
    the exact derivation of the packages it names, leaving out only packages
    this pull request adds or main gained after the branch started.

    The file is re-derived from the merge's own catalog and directory, never
    taken from the branch, and compared whole: every row and every total. A
    hand edit, a stale row or a removed package still named fails
    (tools/catalog.py lagging_subset)."""
    head_rows = {s.get("slug"): s for s in head_catalog.get("systems") or []}
    kept = catalog.lagging_subset(packages_in_coverage(actual), head_rows, ROOT)
    if kept is None:
        return False
    built = coverage_mod.build(directory, {**head_catalog, "systems": kept})
    return coverage_same_rows(actual, built)


def packages_in_coverage(actual: dict) -> set[str]:
    """Slugs the committed coverage file derived a row for."""
    found = set()
    for row in (actual.get("matched") or {}).values():
        for pkg in row.get("pkgs") or []:
            if pkg.get("slug"):
                found.add(pkg["slug"])
    for row in (actual.get("systems_absent_from_catalog") or {}).values():
        for pkg in row:
            if isinstance(pkg, dict) and pkg.get("slug"):
                found.add(pkg["slug"])
    return found


def coverage_same_rows(actual: dict, built: dict) -> bool:
    """True when the two files are the same document apart from list order.

    The builder walks catalog systems in list order, and a subset built
    from a set walks them in hash order, so the same packages can produce
    the same rows in a different order. Everything else is compared: every
    group, every domain row, the totals, `about` and any extra field, so a
    row added to a second group or a stray top-level key still fails."""
    return _order_free(actual) == _order_free(built)


def _order_free(value):
    """The value with list order removed and every field kept.

    Package lists and catalog lists change order when the subset walks a
    set. A changed name, url, or name_match stays a difference."""
    if isinstance(value, list):
        return sorted((_order_free(item) for item in value), key=_sort_key)
    if isinstance(value, dict):
        return {key: _order_free(item) for key, item in value.items()}
    return value


def _sort_key(value) -> str:
    return json.dumps(value, sort_keys=True, default=str)


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
