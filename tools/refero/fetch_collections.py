#!/usr/bin/env python3
"""Fetch Refero's curated collections into refero/collections.json + db tables.

Reads https://styles.refero.design/sitemaps/collections.xml, fetches every
listed page on that host over https (except the homepage), and parses each collection's sections and
ordered style references out of the page's __next_f.push flight payload.

Flight structure (verified 2026-10): each editorial section is an h2 with
id="group-N" followed by a `grid grid-cols` div whose children array mixes
inline card elements `["$","$Lxx","<uuid>",{"style":{"id":"<uuid>",...}}]`
with deferred references `"$L<chunkid>"` that resolve to later flight chunks
holding the same card shape. The JSON-LD ItemList on the page lists the same
styles in the same order, which the parser output is checked against.

Pages with no sections/cards (prose pages like design-md/* guides) are
skipped and logged. Results land in refero/collections.json (atomic write)
and two refero.db tables — collections(slug, url, title, description) and
collection_styles(collection_slug, section, rank, style_uuid) — rebuilt in
one transaction each run.

The store is rebuilt from the pages fetched, so a run writes nothing unless
every listed page fetched: a failed page exits non-zero with the store left
as it was, and so does a sitemap that lists no pages. --limit N fetches only
the first N pages as a dry run and never writes the store.

Usage:
    python3 tools/refero/fetch_collections.py [--workers 4] [--limit N]
"""

import argparse
import concurrent.futures
import html as html_lib
import json
import re
import sqlite3
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import dump as refero_dump  # noqa: E402  (refreshes refero/.dump/ after a write)
import fetch as refero_fetch  # noqa: E402  (its get(): retries and a size cap)

ROOT = Path(__file__).resolve().parents[2]
REFERO = ROOT / "refero"
DB = REFERO / "refero.db"
OUT = REFERO / "collections.json"
BASE = "https://styles.refero.design"
SITEMAP = BASE + "/sitemaps/collections.xml"

SCHEMA = """
CREATE TABLE IF NOT EXISTS collections (
  slug TEXT PRIMARY KEY,
  url TEXT,
  title TEXT,
  description TEXT
);
CREATE TABLE IF NOT EXISTS collection_styles (
  collection_slug TEXT,
  section TEXT,
  rank INTEGER,
  style_uuid TEXT
);
"""

# Same pattern fetch.py uses to pull each flight chunk string.
PUSH_RE = re.compile(r'self\.__next_f\.push\(\[1,("(?:[^"\\]|\\.)*")\]\)')
TITLE_RE = re.compile(r'<title>(.*?)\s*\|\s*Refero Styles</title>', re.S)
TITLE_ANY_RE = re.compile(r'<title>(.*?)</title>', re.S)
DESC_RE = re.compile(r'<meta name="description" content="([^"]*)"')
LOC_RE = re.compile(r'<loc>(.*?)</loc>')

# Section anchors: h2 id="group-N" whose children is the heading string,
# then the first `grid grid-cols` children array holding the style cards.
H2_RE = re.compile(r'"id":"(group-\d+)","className":"[^"]*","children":"((?:[^"\\]|\\.)*)"')
GRID_RE = re.compile(r'"className":"[^"]*grid grid-cols[^"]*","children":\[')
CARD_RE = re.compile(
    r'\["\$","\$L[0-9a-f]+","([0-9a-f-]{36})",\{"style":\{"id":"([0-9a-f-]{36})"')
REF_RE = re.compile(r'"\$L([0-9a-f]{1,3})"')
CHUNK_RE = re.compile(r'\n([0-9a-f]{1,3}):')
CHUNK_CARD_RE = re.compile(
    r'^[0-9a-f]{1,3}:\["\$","\$L[0-9a-f]+","([0-9a-f-]{36})",\{"style":\{"id"')
# Fallback: JSON-LD ItemList order of style urls (same order as the grids).
ITEMLIST_RE = re.compile(
    r'"position":\d+,"url":"https://styles\.refero\.design/style/([0-9a-f-]{36})"')


def on_base(url):
    """True for an https URL on BASE: the only pages, and redirect targets,
    this tool fetches."""
    return url.startswith(BASE + "/")


def get(url, binary=True, tries=4):
    """fetch.get (retries, a size cap) that follows redirects only on BASE."""
    return refero_fetch.get(url, binary, tries, allowed=on_base)


def collection_urls(xml):
    """The sitemap's page URLs, minus the homepage and anything off-site.

    The sitemap is third-party data, so only https URLs on BASE are fetched:
    a file://, plain-http or other-host <loc> is reported and skipped."""
    urls = []
    for u in (u.strip() for u in LOC_RE.findall(xml)):
        if u.rstrip("/") == BASE:  # the homepage
            continue
        if on_base(u):
            urls.append(u)
        else:
            print(f"SKIP off-site sitemap url {u!r}", file=sys.stderr)
    return urls


def flight_blob(page):
    return "".join(json.loads(c) for c in PUSH_RE.findall(page))


def chunk_map(blob):
    """Map flight chunk id -> payload text (the 'id:...' line without \\n)."""
    starts = [(m.start(), m.group(1)) for m in CHUNK_RE.finditer(blob)]
    starts.append((len(blob), None))
    out = {}
    for i, (pos, cid) in enumerate(starts[:-1]):
        out[cid] = blob[pos + 1:starts[i + 1][0]]
    return out


def array_end(s, i):
    """i is just past '['; return index of the matching ']' (strings aware)."""
    depth, instr, esc = 1, False, False
    while i < len(s):
        c = s[i]
        if esc:
            esc = False
        elif c == "\\" and instr:
            esc = True
        elif c == '"':
            instr = not instr
        elif not instr:
            if c in "[{":
                depth += 1
            elif c in "]}":
                depth -= 1
                if depth == 0:
                    return i
        i += 1
    return -1


def grid_uuids(seg, chunks):
    """Ordered style uuids inside one grid children array.

    Elements are either inline card elements or "$L<chunkid>" references to
    deferred flight chunks that hold a card element.
    """
    uuids, pos = [], 0
    while pos < len(seg):
        m = CARD_RE.match(seg, pos)
        if m:
            uuids.append(m.group(1))
            pos = m.end()
            continue
        m = REF_RE.match(seg, pos)
        if m:
            cm = CHUNK_CARD_RE.match(chunks.get(m.group(1), ""))
            if cm:
                uuids.append(cm.group(1))
            pos = m.end()
            continue
        pos += 1
    return uuids


def parse_collection(page):
    """Return (title, description, sections) where sections is a list of
    {heading, uuids} in page order, or None when the page has no flight data."""
    blob = flight_blob(page)
    if not blob:
        return None

    m = TITLE_RE.search(page) or TITLE_ANY_RE.search(page)
    title = html_lib.unescape(m.group(1).strip()) if m else None
    m = DESC_RE.search(page)
    description = html_lib.unescape(m.group(1)) if m else None

    chunks = chunk_map(blob)
    h2s = list(H2_RE.finditer(blob))
    sections = []
    for k, h in enumerate(h2s):
        heading = json.loads('"' + h.group(2) + '"')
        bound = h2s[k + 1].start() if k + 1 < len(h2s) else len(blob)
        g = GRID_RE.search(blob, h.end(), bound)
        uuids = grid_uuids(blob[g.end():array_end(blob, g.end())], chunks) if g else []
        sections.append({"heading": heading, "uuids": uuids})

    if not sections:
        # Fallback: no group sections — take ordered card uuids (grids or
        # deferred chunks) and, if none inline, the JSON-LD ItemList order.
        uuids = []
        for g in GRID_RE.finditer(blob):
            uuids += grid_uuids(blob[g.end():array_end(blob, g.end())], chunks)
        if not uuids:
            all_cards = [m.group(1) for m in CARD_RE.finditer(blob)]
            seen, uuids = set(), [u for u in all_cards if not (u in seen or seen.add(u))]
        if not uuids:
            uuids = ITEMLIST_RE.findall(blob)
        if uuids:
            sections = [{"heading": None, "uuids": uuids}]
    return title, description, sections


def fetch_page(url):
    page = get(url).decode("utf-8", "replace")
    parsed = parse_collection(page)
    if parsed is None:
        raise ValueError("no flight payload")
    return parsed


write_atomic = refero_dump.write_atomic


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--workers", type=int, default=4)
    ap.add_argument("--limit", type=int, default=0,
                    help="fetch only the first N pages; a dry run that "
                         "never writes the store")
    args = ap.parse_args()

    urls = collection_urls(get(SITEMAP).decode())
    if args.limit:
        urls = urls[:args.limit]
    print(f"sitemap: {len(urls)} collection pages")
    if not urls:
        sys.exit("sitemap lists no collection pages; store left unchanged")

    results, failures = {}, []
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as pool:
        futures = {pool.submit(fetch_page, u): u for u in urls}
        for fut in concurrent.futures.as_completed(futures):
            url = futures[fut]
            slug = url.rstrip("/").rsplit("/", 1)[-1]
            try:
                results[url] = fut.result()
            except Exception as ex:
                failures.append((slug, url, str(ex)[:200]))
                print(f"FAIL {slug}: {ex}", file=sys.stderr)

    # The tables and collections.json are rebuilt from `results` alone, so a
    # page missing from it would delete that collection from the store.
    if failures:
        sys.exit(f"failed {len(failures)} pages: "
                 + ", ".join(s for s, _, _ in failures)
                 + "; store left unchanged")

    db = sqlite3.connect(DB)
    db.execute("PRAGMA busy_timeout=30000")
    if not args.limit:  # a dry run leaves the db exactly as it was
        db.executescript(SCHEMA)
    slug_of = {u: s for u, s in db.execute("SELECT uuid, slug FROM styles")}

    collections, skipped, total_styles = [], [], 0
    for url in urls:
        slug = url.rstrip("/").rsplit("/", 1)[-1]
        if url not in results:
            continue
        title, description, sections = results[url]
        # Dedupe style uuids across the whole collection, first section wins.
        seen, clean = set(), []
        for sec in sections:
            us = [u for u in sec["uuids"] if not (u in seen or seen.add(u))]
            if us:
                clean.append({"heading": sec["heading"], "uuids": us})
        n = sum(len(s["uuids"]) for s in clean)
        if n == 0:
            skipped.append((slug, url))
            print(f"SKIP {slug}: no collection styles (prose page?)")
            continue
        total_styles += n
        print(f"{slug}: {len(clean)} sections, {n} styles")
        collections.append({
            "slug": slug,
            "url": url,
            "title": title,
            "description": description,
            "sections": [
                {"heading": sec["heading"],
                 "styles": [{"uuid": u, "slug": slug_of.get(u)} for u in sec["uuids"]]}
                for sec in clean
            ],
        })

    if args.limit:
        db.close()
        print(f"\n--limit {args.limit}: dry run, {len(collections)} collections "
              f"parsed; store not written")
        return

    doc = {
        "version": 1,
        "about": "Curated collections scraped from styles.refero.design — "
                 "third-party interpreted data.",
        "source": SITEMAP,
        "count": len(collections),
        "collections": collections,
    }
    write_atomic(OUT, json.dumps(doc, indent=2) + "\n")

    # Rebuild both tables fully in one transaction.
    db.execute("BEGIN")
    db.execute("DELETE FROM collections")
    db.execute("DELETE FROM collection_styles")
    for c in collections:
        db.execute(
            "INSERT INTO collections (slug, url, title, description) VALUES (?,?,?,?)",
            (c["slug"], c["url"], c["title"], c["description"]))
        for sec in c["sections"]:
            for rank, st in enumerate(sec["styles"]):
                db.execute(
                    "INSERT INTO collection_styles (collection_slug, section, rank, style_uuid)"
                    " VALUES (?,?,?,?)",
                    (c["slug"], sec["heading"], rank, st["uuid"]))
    db.commit()

    resolved = sum(1 for c in collections for s in c["sections"]
                   for st in s["styles"] if st["slug"])
    print(f"\n{len(collections)} collections, {total_styles} style refs "
          f"({resolved} resolved to local slugs, "
          f"{total_styles - resolved} unknown)")
    if skipped:
        print(f"skipped {len(skipped)} pages with no styles: "
              + ", ".join(s for s, _ in skipped))
    db.close()
    refero_dump.refresh(DB)


if __name__ == "__main__":
    main()
