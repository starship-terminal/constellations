#!/usr/bin/env python3
"""Backfill reconstructed component HTML into refero styles.

Upstream, each style's designSystem.components[] entries gain an `html`
field after an enrichment pass. Styles fetched before that pass ran hold
html: null (or, from older runs, an unresolved "$1e" flight reference) in
styles.result_json.
This tool re-scrapes the style pages, resolves the React flight references
("$1e" -> the `1e:T<hex-byte-length>,<utf8 text>` row in the same
__next_f.push blob, sliced by UTF-8 bytes), and rewrites each row:

  - styles.result_json / design_md / name / tagline / theme /
    extracted_at / source_url / screenshot_url (fresh values; the
    product_type / design_style / tags labels are preserved as cmd_fetch
    does), the four media columns + media_fetched_at, fetched_at=now
  - styles.components_json / components_at (added here, idempotent)
  - refero/<slug>/components.json (the designSystem.components array,
    written only when the style ends up with >=1 resolved html; deleted
    otherwise) and a has_components key in meta.json
  - the export artifacts (variables.css, theme.css, tokens.json,
    design-system.json, prompt.txt) via one batched node export.js run

Selection: every styles row whose stored designSystem.components has no
element with resolved html (covers complete-but-empty and
pending-may-be-complete). An unresolved "$xx" reference is not html, so a
style whose only html values are such references is selected too; a ref
that still does not resolve is stored as null, never as "$xx". Pass
--uuids to force specific styles in (e.g. for testing).

Usage:
    python3 tools/refero/backfill_components.py [--workers 8] [--limit N]
        [--dry-run] [--uuids UUID [UUID ...]]
"""

import argparse
import concurrent.futures
import json
import re
import sqlite3
import subprocess
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import fetch  # noqa: E402
import dump as refero_dump  # noqa: E402  (refreshes refero/.dump/ after a write)

REFERO = fetch.REFERO
WORK = fetch.WORK
BASE = fetch.BASE
EXPORT_JS = fetch.EXPORT_JS

# A React flight reference looks like "$1e": the model text lives in a
# `1e:T<hex-byte-length>,<text>` row of the same blob.
REF_RE = re.compile(r"^\$[0-9a-z]+$")


def has_truthy_html(result_json):
    """True when the stored result has a component with resolved html. A
    leftover "$xx" reference is not html, so its style stays selected."""
    try:
        result = json.loads(result_json or "")
    except json.JSONDecodeError:
        return False
    comps = (result.get("designSystem") or {}).get("components") or []
    return any(isinstance(c, dict) and c.get("html")
               and not (isinstance(c["html"], str) and REF_RE.match(c["html"]))
               for c in comps)


def resolve_ref(blob_bytes, ref_id):
    """Slice the `<id>:T<hex>,<text>` row out of the blob. The length counts
    UTF-8 bytes, not characters, so the slice runs on the encoded blob."""
    pat = re.compile(
        rb"(?<![0-9a-zA-Z])" + re.escape(ref_id.encode()) + rb":T([0-9a-f]+),")
    for m in pat.finditer(blob_bytes):
        n = int(m.group(1), 16)
        raw = blob_bytes[m.end():m.end() + n]
        if len(raw) < n:
            continue
        try:
            return raw.decode("utf-8")
        except UnicodeDecodeError:
            continue
    return None


def resolve_components(result, blob_bytes):
    """Resolve designSystem.components[].html refs in place.

    Returns (resolved, unresolved): how many components ended up with real
    HTML (already-text values count) versus how many "$xx" refs could not
    be resolved. Like fetch.resolve_component_html, an unresolved ref and
    "$undefined" become None, never a "$xx" string stored as html.
    """
    comps = (result.get("designSystem") or {}).get("components") or []
    resolved = unresolved = 0
    for c in comps:
        if not isinstance(c, dict):
            continue
        h = c.get("html")
        if h == "$undefined":
            c["html"] = None
        elif isinstance(h, str) and REF_RE.match(h):
            text = resolve_ref(blob_bytes, h[1:])
            if text is None:
                c["html"] = None
                unresolved += 1
            else:
                c["html"] = text
                resolved += 1
        elif h:
            resolved += 1
    return resolved, unresolved


def fetch_and_resolve(uuid):
    """fetch_one plus the flight blob, so component html refs resolve."""
    url = f"{BASE}/style/{uuid}"
    page = fetch.get(url).decode("utf-8", "replace")
    blob = fetch.flight_blob(page)
    result = fetch.extract_result(blob)
    if result is None:
        raise ValueError("no result object in flight payload")
    resolved, unresolved = resolve_components(result, blob.encode("utf-8"))
    return (uuid, url, result, fetch.extract_design_md(page),
            fetch.style_name(result, page), fetch.extract_media(page),
            resolved, unresolved)


def update_meta(db, slug, fresh, has_components):
    """Merge the fresh style_meta fields + has_components into meta.json.

    Existing key order and older extra keys (video_w & co.) are preserved;
    refreshed values update in place and new keys append at the end. A
    missing meta.json is rebuilt from the fresh fields (same shape
    style_meta produces); one that does not parse is moved aside first,
    mirroring write_meta.
    """
    meta_path = REFERO / slug / "meta.json"
    meta_obj = None
    if meta_path.exists():
        try:
            meta_obj = json.loads(meta_path.read_text())
            if not isinstance(meta_obj, dict):
                raise ValueError("not an object")
        except (ValueError, UnicodeDecodeError):
            bad = meta_path.with_name(meta_path.name + ".bad")
            meta_path.rename(bad)
            print(f"warning: {meta_path} does not parse; moved to "
                  f"{bad.name} and rebuilt", file=sys.stderr)
            meta_obj = None
    if meta_obj is None:
        meta_obj = {}
    meta_obj.update(fresh)
    meta_obj["has_components"] = has_components
    meta_path.parent.mkdir(exist_ok=True)
    fetch.write_atomic(meta_path, json.dumps(meta_obj, indent=2) + "\n")


def apply_row(db, uuid, url, result, design_md, name, media,
              resolved, now):
    """Rewrite one styles row from a fresh fetch; returns (slug, has_comps)."""
    old = db.execute(
        "SELECT slug, product_type, design_style, tags FROM styles "
        "WHERE uuid=?", (uuid,)).fetchone()
    old_slug = old[0] if old else None
    # A refetch must not erase labels classify.py or a human already set.
    labels = {"product_type": old[1], "design_style": old[2],
              "tags": json.loads(old[3] or "[]")} if old and old[1] \
             else {"product_type": None, "design_style": None, "tags": []}
    name = name or uuid
    slug = fetch.unique_slug(db, name, uuid)
    if old_slug and slug != old_slug:
        # Upstream renamed the site: move the folder so the db row, the
        # directory and catalog.json keep pointing at the same slug.
        old_dir = REFERO / old_slug
        try:
            old_meta = json.loads((old_dir / "meta.json").read_text())
        except (OSError, ValueError):
            old_meta = {}
        if old_dir.is_dir() and old_meta.get("uuid") == uuid \
                and not (REFERO / slug).exists():
            old_dir.rename(REFERO / slug)
        print(f"note: {old_slug} renamed to {slug}", file=sys.stderr)

    fetch.write_atomic(WORK / f"{uuid}.json", json.dumps(result))
    outdir = REFERO / slug
    outdir.mkdir(exist_ok=True)
    if design_md:
        (outdir / "DESIGN.md").write_text(design_md)

    comps = (result.get("designSystem") or {}).get("components") or []
    has_components = resolved >= 1
    comps_path = outdir / "components.json"
    comps_json = json.dumps(comps, indent=2) + "\n" if has_components else None
    if has_components:
        fetch.write_atomic(comps_path, comps_json)
    else:
        comps_path.unlink(missing_ok=True)

    meta_obj = fetch.style_meta(uuid, slug, name, result, media, labels, now)
    update_meta(db, slug, meta_obj, has_components)

    db.execute(
        """UPDATE styles SET slug=?, name=?, tagline=?, page_url=?,
           source_url=?, theme=?, extracted_at=?, fetched_at=?,
           design_md=?, result_json=?, screenshot_url=?,
           video_url=?, video_poster_url=?, video_detail_url=?,
           video_detail_poster_url=?, media_fetched_at=?,
           product_type=?, design_style=?, tags=?,
           components_json=?, components_at=?
           WHERE uuid=?""",
        (slug, name, meta_obj["tagline"], url, meta_obj["source_url"],
         meta_obj["theme"], meta_obj["extracted_at"], meta_obj["fetched_at"],
         design_md, json.dumps(result), meta_obj["screenshot_url"],
         media["video_url"], media["video_poster_url"],
         media["video_detail_url"], media["video_detail_poster_url"],
         meta_obj["fetched_at"], meta_obj["product_type"],
         meta_obj["design_style"], json.dumps(meta_obj["tags"]),
         comps_json, meta_obj["fetched_at"] if has_components else None,
         uuid))
    # Clear the row's earlier failure, if any, in the same commit.
    db.execute("DELETE FROM fetch_errors WHERE uuid=?", (uuid,))
    db.commit()
    return slug, has_components


def select_rows(db, args):
    """(uuid, slug, name) rows needing the pass, --uuids rows first."""
    seen, rows = set(), []
    for u in args.uuids or []:
        row = db.execute(
            "SELECT uuid, slug, name FROM styles WHERE uuid=?", (u,)).fetchone()
        if row is None:
            print(f"warning: --uuids: {u} is not a styles row",
                  file=sys.stderr)
            continue
        if u not in seen:
            seen.add(u)
            rows.append(row)
    for uuid, slug, name, result_json in db.execute(
            "SELECT uuid, slug, name, result_json FROM styles ORDER BY slug"):
        if uuid in seen or has_truthy_html(result_json):
            continue
        seen.add(uuid)
        rows.append((uuid, slug, name))
    if args.limit:
        rows = rows[:args.limit]
    return rows


def run_export(db, jobs_rows):
    """One batched export.js pass over every refetched style, then the same
    artifact-column UPDATE cmd_export applies."""
    jobs = [{"uuid": uuid, "slug": slug,
             "resultPath": str(WORK / f"{uuid}.json"),
             "outDir": str(REFERO / slug)} for uuid, slug in jobs_rows]
    jobs_file = WORK / "backfill-jobs.json"
    jobs_file.write_text(json.dumps(jobs))
    print(f"exporting {len(jobs)} styles")
    proc = subprocess.run(["node", str(EXPORT_JS), str(jobs_file)])
    if proc.returncode != 0:
        sys.exit(proc.returncode)
    for line in open(str(jobs_file) + ".artifacts.jsonl"):
        rec = json.loads(line)
        if "error" in rec:
            print(f"export FAIL {rec['uuid']}: {rec['error']}",
                  file=sys.stderr)
            continue
        a = rec["artifacts"]
        db.execute(
            """UPDATE styles SET variables_css=?, theme_css=?, tokens_json=?,
               design_system_json=?, prompt_txt=? WHERE uuid=?""",
            (a["variables.css"], a["theme.css"], a["tokens.json"],
             a["design-system.json"], a["prompt.txt"], rec["uuid"]))
    db.commit()
    print("db updated")


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--workers", type=int, default=8)
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--dry-run", action="store_true",
                    help="list the selected styles without fetching")
    ap.add_argument("--uuids", nargs="+", default=[],
                    help="force these style uuids into the selection "
                         "(resolved first, ahead of --limit)")
    args = ap.parse_args()

    db = fetch.init_db()  # adds the component columns too
    rows = select_rows(db, args)
    print(f"to refetch: {len(rows)}")
    if args.dry_run:
        for uuid, slug, name in rows:
            print(f"  {slug}  {uuid}  {name}")
        db.close()
        return
    if not rows:
        db.close()
        return
    try:
        refetch(db, rows, args)
    finally:
        refero_dump.refresh(fetch.DB)


def refetch(db, rows, args):
    done = with_components = still_pending = failed = unresolved_refs = 0
    export_rows = []
    with concurrent.futures.ThreadPoolExecutor(
            max_workers=args.workers) as pool:
        futures = {pool.submit(fetch_and_resolve, u): u
                   for u, _, _ in rows}
        for fut in concurrent.futures.as_completed(futures):
            uuid = futures[fut]
            try:
                (uuid, url, result, design_md, name, media,
                 resolved, unresolved) = fut.result()
            except Exception as ex:
                db.execute(
                    "INSERT OR REPLACE INTO fetch_errors "
                    "(uuid, page_url, error, at) VALUES (?,?,?,?)",
                    (uuid, f"{BASE}/style/{uuid}", str(ex)[:500],
                     time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())))
                db.commit()
                failed += 1
                print(f"FAIL {uuid}: {ex}", file=sys.stderr)
                continue
            now = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
            slug, has_components = apply_row(
                db, uuid, url, result, design_md, name, media, resolved, now)
            export_rows.append((uuid, slug))
            done += 1
            unresolved_refs += unresolved
            if has_components:
                with_components += 1
            else:
                still_pending += 1
            if unresolved:
                print(f"note: {slug}: {unresolved} component html ref(s) "
                      f"did not resolve", file=sys.stderr)
            if done % 50 == 0:
                print(f"refetched {done}/{len(rows)}")

    if export_rows:
        run_export(db, export_rows)
    print(f"refetched {done}, with-components {with_components}, "
          f"still-pending {still_pending}, errors {failed}, "
          f"unresolved component refs {unresolved_refs}")
    db.close()


if __name__ == "__main__":
    main()
