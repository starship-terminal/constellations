#!/usr/bin/env python3
"""Fetch every style from styles.refero.design into refero/.

Writes refero/refero.db (sqlite, canonical store), refero/<slug>/ artifact
files, and refero/catalog.json. Resumable: already-fetched styles are skipped
unless --force is given. Node.js is required for the export pass, which runs
Refero's own serialization code (tools/refero/generators.js).

Usage:
    python3 tools/refero/fetch.py [--workers 8] [--limit N] [--force]
    python3 tools/refero/fetch.py --export-only        # regenerate files/db artifacts from stored result_json
    python3 tools/refero/fetch.py --enrich-media       # backfill video_url/poster columns + meta.json keys

Media keys (video_url, video_poster_url, video_detail_url,
video_detail_poster_url, video_w, video_h, video_ms) are scraped from the
escaped JSON in each page's __next_f.push payload. They are always written
to meta.json (null when absent) so the file has a fixed schema, and the four
URL fields are stored as styles columns. media_fetched_at marks when the
extraction ran; --enrich-media backfills rows where it is still NULL.
"""

import argparse
import concurrent.futures
import html as html_lib
import json
import re
import sqlite3
import subprocess
import sys
import time
import urllib.request
import urllib.error
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REFERO = ROOT / "refero"
WORK = REFERO / ".work"
DB = REFERO / "refero.db"
BASE = "https://styles.refero.design"
SITEMAP = BASE + "/sitemaps/styles.xml"
EXPORT_JS = Path(__file__).resolve().parent / "export.js"

UA = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml",
}

SCHEMA = """
CREATE TABLE IF NOT EXISTS styles (
  uuid TEXT PRIMARY KEY,
  slug TEXT UNIQUE,
  name TEXT,
  tagline TEXT,
  page_url TEXT NOT NULL,
  source_url TEXT,
  theme TEXT,
  extracted_at TEXT,
  fetched_at TEXT NOT NULL,
  design_md TEXT,
  variables_css TEXT,
  theme_css TEXT,
  tokens_json TEXT,
  design_system_json TEXT,
  prompt_txt TEXT,
  result_json TEXT,
  screenshot_url TEXT,
  video_url TEXT,
  video_poster_url TEXT,
  video_detail_url TEXT,
  video_detail_poster_url TEXT,
  media_fetched_at TEXT
);
CREATE TABLE IF NOT EXISTS fetch_errors (
  uuid TEXT PRIMARY KEY,
  page_url TEXT,
  error TEXT,
  at TEXT NOT NULL
);
"""

PUSH_RE = re.compile(r'self\.__next_f\.push\(\[1,("(?:[^"\\]|\\.)*")\]\)')
PRE_RE = re.compile(r'<pre class="whitespace-pre-wrap[^"]*"><code[^>]*>(.*?)</code></pre>', re.S)
TITLE_RE = re.compile(r'<title>(.*?)\s*\|\s*Refero Styles</title>', re.S)
RESULT_KEY = '"result":{'

# Added after the initial schema shipped; init_db() ALTERs existing DBs.
MEDIA_COLUMNS = ["video_url", "video_poster_url", "video_detail_url",
                 "video_detail_poster_url", "media_fetched_at"]

# Media fields live in the raw page as escaped JSON inside __next_f.push
# strings, e.g.  \"previewVideoUrl\":\"https://images.refero.design/...\".
# The backslashes are literal characters, hence the \\*" fragments below.
MEDIA_URL_FIELDS = {
    "video_url": "previewVideoUrl",
    "video_poster_url": "previewVideoPosterUrl",
    "video_detail_url": "previewVideoDetailUrl",
    "video_detail_poster_url": "previewVideoDetailPosterUrl",
}
MEDIA_INT_FIELDS = {
    "video_w": "previewVideoWidth",
    "video_h": "previewVideoHeight",
    "video_ms": "previewVideoDurationMs",
}


def get(url, binary=True, tries=4):
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers=UA)
            data = urllib.request.urlopen(req, timeout=90).read()
            return data if binary else data.decode("utf-8", "replace")
        except Exception:
            if i == tries - 1:
                raise
            time.sleep(2 ** i)


def slugify(name):
    s = re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")
    return s or "unnamed"


def flight_blob(page):
    return "".join(json.loads(c) for c in PUSH_RE.findall(page))


def extract_result(blob):
    """Return the parsed {meta, raw, designSystem, screenshot} object, or None."""
    for m in re.finditer(re.escape(RESULT_KEY), blob):
        start = m.end() - 1
        depth, i, instr, esc = 0, start, False, False
        while i < len(blob):
            c = blob[i]
            if esc:
                esc = False
            elif c == "\\" and instr:
                esc = True
            elif c == '"':
                instr = not instr
            elif not instr:
                if c == "{":
                    depth += 1
                elif c == "}":
                    depth -= 1
                    if depth == 0:
                        break
            i += 1
        try:
            obj = json.loads(blob[start:i + 1])
        except json.JSONDecodeError:
            continue
        if isinstance(obj, dict) and "designSystem" in obj and "meta" in obj:
            return obj
    return None


def extract_design_md(page):
    m = PRE_RE.search(page)
    if not m:
        return None
    return html_lib.unescape(m.group(1))


SHOT_RE = re.compile(
    r'\\"screenshot\\":\s*{\\"url\\":\\*"(https://images\.refero\.design/[^"\\]+)')
SHOT_URL_RE = re.compile(r'screenshotUrl\\*":\\*"')


def extract_media(page):
    """Pull preview-video fields out of the raw page's escaped flight JSON.

    Returns a dict with the MEDIA_URL_FIELDS/MEDIA_INT_FIELDS keys; values
    are None when the style has no video (the field is emitted as null).

    The page serializes ~20 other styles' records after the main one (a
    related-styles list), so each field is read only inside the record whose
    screenshotUrl matches the style's own result.screenshot.url. Falls back
    to the first occurrence when that anchor is not found.
    """
    start = 0
    shot = SHOT_RE.search(page)
    if shot:
        own = re.search(SHOT_URL_RE.pattern + re.escape(shot.group(1)), page)
        if own:
            start = own.end()
            nxt = SHOT_URL_RE.search(page, start)
            end = nxt.start() if nxt else start + 4000
            window = page[start:end]
        else:
            window = page
    else:
        window = page
    media = {}
    for key, field in MEDIA_URL_FIELDS.items():
        # The style's own record precedes the related-styles records, so the
        # first field occurrence wins whether its value is a URL or null.
        m = re.search(
            field + r'\\*"\s*:\s*(?:\\*"(https://images\.refero\.design/[^"\\]+)\\*"|null)',
            window)
        media[key] = m.group(1) if m else None
    for key, field in MEDIA_INT_FIELDS.items():
        m = re.search(field + r'\\*":(?:null|(\d+))', window)
        media[key] = int(m.group(1)) if m and m.group(1) else None
    return media


def parse_page(page):
    """Return (result dict, design_md str) or raise."""
    result = extract_result(flight_blob(page))
    if result is None:
        raise ValueError("no result object in flight payload")
    return result, extract_design_md(page)


def style_name(result, page):
    name = (result.get("meta") or {}).get("siteName")
    if name:
        return name.strip()
    m = TITLE_RE.search(page)
    return m.group(1).strip() if m else None


def init_db():
    REFERO.mkdir(exist_ok=True)
    WORK.mkdir(exist_ok=True)
    db = sqlite3.connect(DB)
    db.executescript(SCHEMA)
    have = {r[1] for r in db.execute("PRAGMA table_info(styles)")}
    for col in MEDIA_COLUMNS:
        if col not in have:
            db.execute(f"ALTER TABLE styles ADD COLUMN {col} TEXT")
    db.commit()
    return db


def fetch_sitemap_uuids():
    xml = get(SITEMAP).decode()
    return re.findall(r"/style/([0-9a-f-]{36})", xml)


def unique_slug(db, name, uuid=None):
    base = slugify(name or "unnamed")
    slug, n = base, 1
    while db.execute("SELECT 1 FROM styles WHERE slug = ? AND uuid IS NOT ?",
                     (slug, uuid)).fetchone():
        n += 1
        slug = f"{base}-{n}"
    return slug


def fetch_one(uuid):
    url = f"{BASE}/style/{uuid}"
    page = get(url).decode("utf-8", "replace")
    result, design_md = parse_page(page)
    return uuid, url, result, design_md, style_name(result, page), extract_media(page)


def write_meta(slug, media):
    """Merge media keys into refero/<slug>/meta.json, preserving key order."""
    meta_path = REFERO / slug / "meta.json"
    meta_obj = {}
    if meta_path.exists():
        try:
            meta_obj = json.loads(meta_path.read_text())
        except json.JSONDecodeError:
            pass
    meta_obj.update(media)
    meta_path.parent.mkdir(exist_ok=True)
    meta_path.write_text(json.dumps(meta_obj, indent=2) + "\n")


def cmd_fetch(args):
    db = init_db()
    uuids = fetch_sitemap_uuids()
    print(f"sitemap: {len(uuids)} styles")

    if not args.force:
        done = {r[0] for r in db.execute("SELECT uuid FROM styles")}
        uuids = [u for u in uuids if u not in done]
    else:
        db.execute("DELETE FROM fetch_errors")
        db.commit()
    if args.limit:
        uuids = uuids[:args.limit]
    print(f"to fetch: {len(uuids)}")
    if not uuids:
        return

    fetched = 0
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as pool:
        futures = {pool.submit(fetch_one, u): u for u in uuids}
        for fut in concurrent.futures.as_completed(futures):
            uuid = futures[fut]
            try:
                uuid, url, result, design_md, name, media = fut.result()
            except Exception as ex:
                db.execute(
                    "INSERT OR REPLACE INTO fetch_errors (uuid, page_url, error, at) VALUES (?,?,?,?)",
                    (uuid, f"{BASE}/style/{uuid}", str(ex)[:500],
                     time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())))
                db.commit()
                print(f"FAIL {uuid}: {ex}", file=sys.stderr)
                continue

            meta = result.get("meta") or {}
            ds = result.get("designSystem") or {}
            name = name or uuid
            slug = unique_slug(db, name, uuid)
            (WORK / f"{uuid}.json").write_text(json.dumps(result))
            outdir = REFERO / slug
            outdir.mkdir(exist_ok=True)
            if design_md:
                (outdir / "DESIGN.md").write_text(design_md)
            meta_obj = {
                "uuid": uuid,
                "slug": slug,
                "name": name,
                "tagline": ds.get("northStar"),
                "theme": ds.get("theme"),
                "page_url": url,
                "source_url": meta.get("url"),
                "extracted_at": meta.get("extractedAt"),
                "fetched_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
                "screenshot_url": (result.get("screenshot") or {}).get("url"),
                **media,
            }
            (outdir / "meta.json").write_text(json.dumps(meta_obj, indent=2) + "\n")
            db.execute(
                """INSERT OR REPLACE INTO styles
                   (uuid, slug, name, tagline, page_url, source_url, theme,
                    extracted_at, fetched_at, design_md, result_json, screenshot_url,
                    video_url, video_poster_url, video_detail_url,
                    video_detail_poster_url, media_fetched_at)
                   VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
                (uuid, slug, name, meta_obj["tagline"], url, meta_obj["source_url"],
                 meta_obj["theme"], meta_obj["extracted_at"], meta_obj["fetched_at"],
                 design_md, json.dumps(result), meta_obj["screenshot_url"],
                 media["video_url"], media["video_poster_url"],
                 media["video_detail_url"], media["video_detail_poster_url"],
                 meta_obj["fetched_at"]))
            db.commit()
            fetched += 1
            if fetched % 50 == 0:
                print(f"fetched {fetched}/{len(uuids)}")
    print(f"fetched {fetched}, errors {len(uuids) - fetched}")
    db.close()


def cmd_export():
    """Run the node export pass over every stored result, update files + db."""
    db = init_db()
    rows = db.execute(
        "SELECT uuid, slug FROM styles WHERE result_json IS NOT NULL").fetchall()
    jobs = []
    for uuid, slug in rows:
        rpath = WORK / f"{uuid}.json"
        if not rpath.exists():
            row = db.execute("SELECT result_json FROM styles WHERE uuid=?",
                             (uuid,)).fetchone()
            rpath.write_text(row[0])
        jobs.append({"uuid": uuid, "slug": slug, "resultPath": str(rpath),
                     "outDir": str(REFERO / slug)})
    jobs_file = WORK / "jobs.json"
    jobs_file.write_text(json.dumps(jobs))
    print(f"exporting {len(jobs)} styles")
    proc = subprocess.run(["node", str(EXPORT_JS), str(jobs_file)])
    if proc.returncode != 0:
        sys.exit(proc.returncode)

    for line in open(str(jobs_file) + ".artifacts.jsonl"):
        rec = json.loads(line)
        if "error" in rec:
            print(f"export FAIL {rec['uuid']}: {rec['error']}", file=sys.stderr)
            continue
        a = rec["artifacts"]
        db.execute(
            """UPDATE styles SET variables_css=?, theme_css=?, tokens_json=?,
               design_system_json=?, prompt_txt=? WHERE uuid=?""",
            (a["variables.css"], a["theme.css"], a["tokens.json"],
             a["design-system.json"], a["prompt.txt"], rec["uuid"]))
    db.commit()
    print("db updated")
    db.close()


def enrich_one(url):
    return extract_media(get(url).decode("utf-8", "replace"))


def cmd_enrich_media(args):
    """Backfill media columns for styles fetched before they existed."""
    db = init_db()
    if args.force:
        rows = db.execute(
            "SELECT uuid, slug, page_url FROM styles ORDER BY slug").fetchall()
    else:
        rows = db.execute(
            "SELECT uuid, slug, page_url FROM styles "
            "WHERE media_fetched_at IS NULL ORDER BY slug").fetchall()
    if args.limit:
        rows = rows[:args.limit]
    print(f"to enrich: {len(rows)}")
    if not rows:
        db.close()
        return

    done = 0
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as pool:
        futures = {pool.submit(enrich_one, page_url): (uuid, slug, page_url)
                   for uuid, slug, page_url in rows}
        for fut in concurrent.futures.as_completed(futures):
            uuid, slug, page_url = futures[fut]
            try:
                media = fut.result()
            except Exception as ex:
                db.execute(
                    "INSERT OR REPLACE INTO fetch_errors (uuid, page_url, error, at) VALUES (?,?,?,?)",
                    (uuid, page_url, str(ex)[:500],
                     time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())))
                db.commit()
                print(f"FAIL {slug}: {ex}", file=sys.stderr)
                continue
            db.execute(
                """UPDATE styles SET video_url=?, video_poster_url=?,
                   video_detail_url=?, video_detail_poster_url=?,
                   media_fetched_at=? WHERE uuid=?""",
                (media["video_url"], media["video_poster_url"],
                 media["video_detail_url"], media["video_detail_poster_url"],
                 time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), uuid))
            db.commit()
            write_meta(slug, media)
            done += 1
            if done % 50 == 0:
                print(f"enriched {done}/{len(rows)}")
    print(f"enriched {done}, errors {len(rows) - done}")
    db.close()


def cmd_catalog():
    db = init_db()
    rows = db.execute(
        """SELECT slug, name, tagline, uuid, page_url, source_url, theme,
                  extracted_at, fetched_at FROM styles ORDER BY name""").fetchall()
    catalog = {
        "version": 1,
        "about": "Snapshot of styles.refero.design — third-party interpreted "
                 "design data, not measured evidence. See refero/README.md.",
        "source": BASE,
        "sitemap": SITEMAP,
        "count": len(rows),
        "styles": [
            {"slug": s, "name": n, "tagline": t, "uuid": u,
             "page_url": p, "source_url": su, "theme": th,
             "extracted_at": ea, "fetched_at": fa}
            for s, n, t, u, p, su, th, ea, fa in rows
        ],
    }
    (REFERO / "catalog.json").write_text(json.dumps(catalog, indent=2) + "\n")
    print(f"catalog.json: {len(rows)} styles")
    db.close()


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--workers", type=int, default=8)
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--force", action="store_true")
    ap.add_argument("--export-only", action="store_true")
    ap.add_argument("--catalog-only", action="store_true")
    ap.add_argument("--enrich-media", action="store_true")
    args = ap.parse_args()

    if args.enrich_media and (args.export_only or args.catalog_only):
        ap.error("--enrich-media is mutually exclusive with "
                 "--export-only/--catalog-only")
    if args.enrich_media:
        cmd_enrich_media(args)
        cmd_catalog()
        return
    if args.catalog_only:
        cmd_catalog()
        return
    if args.export_only:
        cmd_export()
        cmd_catalog()
        return
    cmd_fetch(args)
    cmd_export()
    cmd_catalog()


if __name__ == "__main__":
    main()
