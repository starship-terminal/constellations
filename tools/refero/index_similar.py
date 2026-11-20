#!/usr/bin/env python3
"""Materialize the cross-style "similar" graph from refero.db.

    python3 tools/refero/index_similar.py [--refero DIR]

Every styles.result_json carries designSystem.similar: a short list of
{business, why} objects naming another product whose design Refero considers
close. Most of those businesses are external (Aesop, Are.na, Resn, ...);
where the name resolves to a style in the snapshot, matched_slug links the
edge into the graph.

Writes a fresh `similar` table (uuid, business, why, rank, matched_slug) and
refero/similar.json. Pure derivation from stored result_json, no network.
Re-run after fetch.py.
"""

import argparse
import json
import re
import sqlite3
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import dump as refero_dump  # noqa: E402  (refreshes refero/.dump/ after a write)

ROOT = Path(__file__).resolve().parents[2]
REFERO = ROOT / "refero"
DB = REFERO / "refero.db"


def slugify(name):
    return re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")


# Business-name variants seen in designSystem.similar, cheapest first:
# "Locomotive (locomotive.ca)" carries a parenthesised domain, "Tana Inc" a
# legal suffix, "Get X"/"Try X" a call-to-action verb, "Things 3" a version,
# "Arc Browser"/"Phantom Wallet" a product-surface word tacked onto the brand.
TRAILING_PAREN = re.compile(r"\s*\([^)]*\)\s*$")
LEGAL_SUFFIX = re.compile(
    r"\s+(inc|llc|ltd|gmbh|sarl|pty|plc|co|corp|corporation|company)\.?\s*$",
    re.I)
LEADING_VERB = re.compile(r"^(?:get|try|use|join|meet|hello|hey)\s+", re.I)
TRAILING_VERSION = re.compile(r"[\s-]+v?\d+$", re.I)

# Last-slug-segment drops that produced correct matches on this snapshot
# ("Arc Browser" -> arc, "Kinfolk Magazine" -> kinfolk, "Runway ML" -> runway).
# Deliberately excludes ambiguous business-type words (ventures, capital,
# health, design, ...): dropping those linked different companies, e.g.
# "Notion Capital" -> notion and "Index Ventures" -> index are false edges.
SURFACE_WORDS = {
    "app", "browser", "wallet", "press", "magazine", "blog", "docs",
    "changelog", "reader", "terminal", "cms", "studio", "analytics",
    "money", "mtl", "films", "itself", "music", "store", "shop", "events",
    "sessions", "newsroom", "marketplace", "showcase", "templates",
    "codespaces", "dashboard", "geist", "marketing", "homepage",
    "editorial", "shots", "gaming", "arcade", "card", "tv", "watch",
    "fitness", "ml", "pro", "ios", "hq", "ai",
}


def business_variants(business):
    """Ordered name forms to try, most faithful first."""
    out, seen = [], set()

    def add(value):
        value = value.strip()
        key = value.lower()
        if value and key not in seen:
            seen.add(key)
            out.append(value)

    business = business.strip()
    add(business)
    no_paren = TRAILING_PAREN.sub("", business)
    add(no_paren)
    for base in (business, no_paren):
        stripped = LEGAL_SUFFIX.sub("", base)
        add(stripped)
        add(TRAILING_VERSION.sub("", stripped))
        m = LEADING_VERB.match(stripped)
        if m:
            add(stripped[m.end():])
    # "It's Nice That" -> "its-nice-that"
    squashed = business.replace("’", "").replace("'", "")
    if squashed != business:
        add(squashed)
    return out


def make_resolver(slugs, by_name):
    def resolve(business):
        for variant in business_variants(business):
            slug = slugify(variant)
            candidates = [slug]
            parts = slug.split("-")
            if len(parts) > 1 and parts[-1] in SURFACE_WORDS:
                candidates.append("-".join(parts[:-1]))
            for candidate in candidates:
                if candidate in slugs:
                    return candidate
                if candidate in by_name:
                    return by_name[candidate]
            lower = variant.lower()
            if lower in by_name:
                return by_name[lower]
        return None
    return resolve


def names_by_lower(rows):
    """Lower-cased style name -> slug, for names exactly one style carries.

    A name several styles share (Apple x6) is left out, so a business with
    that name links only through an exact slug match: picking one of them
    would follow the db's row order, which a dump reload or a refetch changes
    with no change in the data. catalog.py's build_refero applies the same
    rule to the names it resolves."""
    count, slug_of = {}, {}
    for _, slug, name, _ in rows:
        if name:
            key = name.lower()
            count[key] = count.get(key, 0) + 1
            slug_of[key] = slug
    return {key: slug for key, slug in slug_of.items() if count[key] == 1}


write_atomic = refero_dump.write_atomic


def open_db(refero: Path):
    path = refero / "refero.db"
    if not path.is_file():
        sys.exit(f"error: no {path}")
    with open(path, "rb") as f:
        if f.read(64).startswith(b"version https://git-lfs"):
            sys.exit(f"error: {path} is a Git LFS pointer; "
                     "run: git lfs install && git lfs pull")
    # Autocommit mode: main() opens its one write transaction itself, since
    # the legacy implicit transactions never cover DROP or CREATE.
    db = sqlite3.connect(path, isolation_level=None)
    db.execute("PRAGMA busy_timeout=30000")
    return db


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--refero", type=Path, default=REFERO,
                    help="the refero/ folder to index (default: the repo's)")
    args = ap.parse_args()
    if not args.refero.is_dir():
        sys.exit(f"{args.refero} is not a folder")

    db = open_db(args.refero)
    rows = db.execute(
        "SELECT uuid, slug, name, result_json FROM styles").fetchall()
    slugs = {slug for _, slug, _, _ in rows}
    by_name = names_by_lower(rows)
    resolve = make_resolver(slugs, by_name)

    edges = []          # (uuid, business, why, rank, matched_slug)
    json_styles = []    # [{slug, uuid, similar: [{business, why, slug}]}]
    unmatched = {}
    for uuid, slug, name, result_json in rows:
        if not result_json:
            continue
        result = json.loads(result_json)
        similar = (result.get("designSystem") or {}).get("similar")
        if not similar:
            continue
        entry_similar = []
        for rank, entry in enumerate(similar, start=1):
            if not isinstance(entry, dict):
                continue
            business = (entry.get("business") or "").strip()
            if not business:
                continue
            why = entry.get("why")
            matched = resolve(business)
            edges.append((uuid, business, why, rank, matched))
            entry_similar.append(
                {"business": business, "why": why, "slug": matched})
            if matched is None:
                unmatched[business] = unmatched.get(business, 0) + 1
        if entry_similar:
            json_styles.append(
                {"slug": slug, "uuid": uuid, "similar": entry_similar})

    json_styles.sort(key=lambda s: s["slug"])
    matched_count = sum(1 for e in edges if e[4] is not None)

    # One short transaction around the DROP, CREATE and INSERTs, so a failed
    # insert leaves the old table: other agents write refero.db concurrently.
    db.execute("BEGIN IMMEDIATE")
    try:
        db.execute("DROP TABLE IF EXISTS similar")
        db.execute("""CREATE TABLE similar (
            uuid TEXT, business TEXT, why TEXT, rank INTEGER,
            matched_slug TEXT)""")
        db.executemany(
            "INSERT INTO similar (uuid, business, why, rank, matched_slug)"
            " VALUES (?,?,?,?,?)", edges)
        db.execute("COMMIT")
    except BaseException:
        db.execute("ROLLBACK")
        raise
    finally:
        db.close()
    refero_dump.refresh(args.refero / "refero.db")

    write_atomic(args.refero / "similar.json", json.dumps({
        "version": 1,
        "about": "Similar-style graph derived from designSystem.similar in "
                 "refero.db — third-party interpreted data.",
        "source": "styles.refero.design",
        "count": len(json_styles),
        "styles": json_styles,
    }, indent=2) + "\n")

    print(f"styles processed: {len(rows)}")
    print(f"styles with similar lists: {len(json_styles)}")
    print(f"edges written: {len(edges)}")
    pct = matched_count / len(edges) * 100 if edges else 0
    print(f"matched to refero slugs: {matched_count} ({pct:.1f}%)")
    if unmatched:
        print("top unmatched businesses (not in the snapshot):")
        for business, count in sorted(
                unmatched.items(), key=lambda kv: (-kv[1], kv[0]))[:15]:
            print(f"  {count:4d}  {business}")


if __name__ == "__main__":
    main()
