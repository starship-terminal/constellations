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
import os
import re
import sqlite3
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REFERO = ROOT / "refero"

sys.path.insert(0, str(Path(__file__).resolve().parent))
import coverage as coverage_mod  # noqa: E402  (sibling module)
import dump as refero_dump  # noqa: E402  (sibling module)

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
    # A pull request that only adds catalog rows cannot regenerate this
    # file for the merge commit, because the merge is not on a branch.
    # Compare the added rows against the base file instead.
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


def branch_catalog() -> dict | None:
    """Catalog rows on the pull request branch, keyed by slug.

    GitHub checks the merge commit, so the working tree already includes
    captures that landed on the base after this branch was pushed. The
    workflow fetches the branch tip to GITHUB_HEAD_SHA. A depth-1 checkout
    has no second parent, so HEAD^2 is not that tip."""
    sha = os.environ.get("GITHUB_HEAD_SHA")
    if not sha or not os.environ.get("GITHUB_BASE_REF"):
        return None
    try:
        raw = subprocess.run(
            ["git", "show", f"{sha}:catalog.json"],
            cwd=ROOT, check=True, capture_output=True, text=True,
        ).stdout
        catalog = json.loads(raw)
    except (OSError, subprocess.CalledProcessError, json.JSONDecodeError):
        return None
    return {s.get("slug"): s for s in catalog.get("systems") or []}


def base_catalog(head_catalog: dict) -> dict | None:
    """The catalog on the pull request's base, when GitHub is merging one.

    Returns None outside a pull request, or when the base blob cannot be
    read. The caller then keeps the exact-match rule."""
    base = os.environ.get("GITHUB_BASE_REF")
    if not base:
        return None
    try:
        raw = subprocess.run(
            ["git", "show", f"origin/{base}:catalog.json"],
            cwd=ROOT, check=True, capture_output=True, text=True,
        ).stdout
        return json.loads(raw)
    except (OSError, subprocess.CalledProcessError, json.JSONDecodeError):
        return None


def coverage_matches_base(directory: dict, head_catalog: dict,
                          actual: dict, expected: dict) -> bool:
    """True when the committed file matches the base, and this pull request
    only adds catalog rows.

    Removing or editing a row changes the derived coverage, so that still
    fails until the file is regenerated."""
    base = base_catalog(head_catalog)
    if base is None:
        return False
    base_rows = {s.get("slug"): s for s in base.get("systems") or []}
    head_rows = {s.get("slug"): s for s in head_catalog.get("systems") or []}
    # GitHub checks the merge. A branch started before later captures landed
    # is missing those rows, so a strict superset is the wrong test. Every
    # row the branch does carry must be unchanged, and it must add one.
    if not base_rows:
        return False
    if any(slug in base_rows and head_rows[slug] != base_rows[slug]
           for slug in head_rows):
        return False
    # This pull request regenerated the file, then main gained another
    # capture before the check ran. The merge catalog has that capture
    # and may add no row of its own. The committed file is current when
    # it matches the branch tip.
    branch_rows = branch_catalog()
    if branch_rows is not None and set(branch_rows) < set(head_rows):
        if all(head_rows.get(slug) == row for slug, row in branch_rows.items()):
            branch_expected = coverage_mod.build(
                directory, {**head_catalog, "systems": list(branch_rows.values())})
            if actual == branch_expected:
                return True
    if not set(head_rows) - set(base_rows):
        return False
    # The committed file may be the current base, or a base that already
    # included some of the added rows (the PR regenerated it, then main
    # gained other captures). Either way the shared rows must agree, and
    # every domain in the committed file must still be derived from the
    # merged catalog. A hand-edited domain fails.
    base_expected = coverage_mod.build(directory, base)
    if actual == base_expected or actual == expected:
        return True
    # The branch regenerated coverage against an older base. Shared domains
    # must still match the merge. A domain only the branch file has must be
    # one of the rows this pull request adds, unchanged.
    added = [row for slug, row in head_rows.items() if slug not in base_rows]
    added_expected = coverage_mod.build(
        directory, {**head_catalog, "systems": list(base.get("systems") or []) + added})
    if (coverage_shared_ok(added_expected, actual)
            and coverage_extras_are_added(actual, expected, added_expected)):
        return True
    # The committed file may also lag packages already merged to the base.
    # It is still current when it is exactly the derivation of the packages
    # it names, and those packages are an unchanged subset of this catalog.
    return coverage_is_prior_derivation(directory, head_catalog, actual)


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


def coverage_is_prior_derivation(directory: dict, head_catalog: dict,
                                 actual: dict) -> bool:
    """True when the file is the derivation of an unchanged subset.

    A capture merge does not rewrite this file, so the next add-only pull
    request still carries the older derivation. GitHub then merges that
    branch with a base that already has later captures, so the branch
    catalog is missing those rows. The file is still current when it
    matches a derivation of the base rows it names, and every catalog row
    the branch does carry is unchanged. A hand-edited domain does not
    equal that derivation and still fails."""
    base = base_catalog(head_catalog)
    if base is None:
        return False
    base_rows = {s.get("slug"): s for s in base.get("systems") or []}
    head_rows = {s.get("slug"): s for s in head_catalog.get("systems") or []}
    if not base_rows:
        return False
    named = packages_in_coverage(actual)
    # A regenerated file also names the package this pull request adds.
    # A file that names some other package is not a derivation of this
    # catalog.
    if not named or not named <= set(base_rows) | set(head_rows):
        return False
    kept = [base_rows[slug] if slug in base_rows else head_rows[slug]
            for slug in named]
    built = coverage_mod.build(directory, {**base, "systems": kept})
    return coverage_same_rows(actual, built)


def coverage_same_rows(actual: dict, built: dict) -> bool:
    """True when both files name the same domain rows, ignoring order.

    The builder walks catalog systems in list order, and a subset built
    from a set walks them in hash order. The same packages then produce
    the same domain rows in a different order. A changed row still fails."""
    def rows(doc):
        found = {}
        for key in ("matched", "missing", "systems_absent_from_catalog"):
            for dom, row in (doc.get(key) or {}).items():
                found[dom] = (key, row)
        return found
    left, right = rows(actual), rows(built)
    if set(left) != set(right):
        return False
    # Counts do not depend on package order. A wrong total is a hand edit.
    if actual.get("totals") != built.get("totals"):
        return False
    return all(same_coverage_row(left[dom], right[dom]) for dom in left)


def same_coverage_row(left, right) -> bool:
    key_l, row_l = left
    key_r, row_r = right
    if key_l != key_r:
        return False
    return _order_free(row_l) == _order_free(row_r)


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


def _pkg_slugs(row) -> set[str]:
    pkgs = row if isinstance(row, list) else (row or {}).get("pkgs") or []
    return {pkg.get("slug") for pkg in pkgs if isinstance(pkg, dict) and pkg.get("slug")}


def coverage_shared_ok(expected: dict, actual: dict) -> bool:
    """Every domain in the committed file still agrees with the merge.

    A later capture can move a domain from missing to matched. An added
    package on a domain the file already covers changes the package list
    without making the file stale. A package the file names and the merge
    does not, or a changed package row, still fails."""
    expected_flat = {}
    for key in ("matched", "missing", "systems_absent_from_catalog"):
        expected_flat.update(expected.get(key) or {})
    for key in ("matched", "missing", "systems_absent_from_catalog"):
        for dom, row in (actual.get(key) or {}).items():
            if dom not in expected_flat:
                continue
            other = expected_flat[dom]
            if _pkg_slugs(row) - _pkg_slugs(other):
                return False
            other_pkgs = other if isinstance(other, list) else (other or {}).get("pkgs") or []
            by_slug = {pkg.get("slug"): pkg for pkg in other_pkgs if isinstance(pkg, dict)}
            pkgs = row if isinstance(row, list) else (row or {}).get("pkgs") or []
            for pkg in pkgs:
                if not isinstance(pkg, dict) or pkg.get("slug") not in by_slug:
                    continue
                if pkg != by_slug[pkg.get("slug")]:
                    return False
    return True


def coverage_extras_are_added(actual: dict, expected: dict, added_expected: dict) -> bool:
    """A domain only the committed file has is exactly what the added rows derive."""
    for key in ("matched", "missing", "systems_absent_from_catalog"):
        actual_map = actual.get(key) or {}
        expected_map = expected.get(key) or {}
        added_map = added_expected.get(key) or {}
        for dom, row in actual_map.items():
            if dom in expected_map:
                continue
            if added_map.get(dom) != row:
                return False
    return True


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
