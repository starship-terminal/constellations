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
video_detail_poster_url) are scraped from the escaped JSON in each page's
__next_f.push payload. They are always written to meta.json (null when
absent) so the file has a fixed schema, and stored as styles columns.
media_fetched_at marks when the extraction ran; --enrich-media backfills
rows where it is still NULL.
"""

import argparse
import concurrent.futures
import html as html_lib
import http.client
import json
import os
import re
import sqlite3
import subprocess
import sys
import time
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import dump as refero_dump  # noqa: E402  (refreshes refero/.dump/ after a write)

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
  media_fetched_at TEXT,
  product_type TEXT,
  design_style TEXT,
  tags TEXT
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

# Label columns are written by tools/refero/classify.py, not by the fetch pass.
LABEL_COLUMNS = ["product_type", "design_style", "tags"]

# Resolved component markup and when it was fetched; NULL when upstream has
# shipped no component html for the style. backfill_components.py fills these
# for styles fetched before the column existed.
COMPONENT_COLUMNS = ["components_json", "components_at"]

# Media fields live in the raw page as escaped JSON inside __next_f.push
# strings, e.g.  \"previewVideoUrl\":\"https://images.refero.design/...\".
# The backslashes are literal characters, hence the \\*" fragments below.
MEDIA_URL_FIELDS = {
    "video_url": "previewVideoUrl",
    "video_poster_url": "previewVideoPosterUrl",
    "video_detail_url": "previewVideoDetailUrl",
    "video_detail_poster_url": "previewVideoDetailPosterUrl",
}
# Refero also ships previewVideoWidth/Height/DurationMs, but the values were
# null for every fetched style, nothing reads them, and the raw page is not
# kept around to re-check against; they were dropped rather than carried.


# The largest response get() reads: well above any page or API listing
# Refero serves, and a bound on what a misbehaving server can make us hold.
MAX_RESPONSE = 64 * 1024 * 1024


class TooLarge(ValueError):
    """A response body over MAX_RESPONSE bytes."""


class RedirectRefused(ValueError):
    """A redirect to a URL the caller does not allow."""


def https_only(url):
    return url.startswith("https://")


class CheckedRedirect(urllib.request.HTTPRedirectHandler):
    """Follow a redirect only to a URL `allowed(url)` accepts. urllib joins a
    relative Location onto the request URL before this sees it."""

    def __init__(self, allowed):
        super().__init__()
        self.allowed = allowed

    def redirect_request(self, req, fp, code, msg, headers, newurl):
        if not self.allowed(newurl):
            raise RedirectRefused(f"refusing a redirect from {req.full_url} to {newurl!r}")
        return super().redirect_request(req, fp, code, msg, headers, newurl)


def opener(allowed):
    return urllib.request.build_opener(CheckedRedirect(allowed))


def get(url, binary=True, tries=4, allowed=https_only):
    """GET url with retry/backoff. Every redirect target must pass `allowed`
    (default: https only). Raises, without retrying, RedirectRefused for any
    other target and TooLarge for a body over MAX_RESPONSE bytes. A body
    shorter than its Content-Length (a dropped connection) is retried."""
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers=UA)
            with opener(allowed).open(req, timeout=90) as r:
                data = r.read(MAX_RESPONSE + 1)
                declared = (r.headers.get("Content-Length") or "").strip()
            # read(n), unlike read(), returns a cut-short body without raising.
            if declared.isdigit() and len(data) < int(declared) and len(data) <= MAX_RESPONSE:
                raise http.client.IncompleteRead(data, int(declared) - len(data))
            break
        except RedirectRefused:
            raise
        except Exception:
            if i == tries - 1:
                raise
            time.sleep(2 ** i)
    if len(data) > MAX_RESPONSE:
        raise TooLarge(f"{url}: response over {MAX_RESPONSE} bytes")
    return data if binary else data.decode("utf-8", "replace")


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

    Returns a dict with the MEDIA_URL_FIELDS keys; values are None when the
    style has no video (the field is emitted as null).

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
    return media


FLIGHT_REF_RE = re.compile(r"^\$[0-9a-z]+$")


def resolve_component_html(result, blob):
    """Resolve designSystem.components[].html flight refs in place.

    A component's html arrives as "$<hexid>" — a reference to a text row
    "<hexid>:T<hex-byte-length>,<utf8 text>" elsewhere in the same flight
    blob. The row length counts UTF-8 bytes, so the slice happens on the
    encoded blob. Refs that do not resolve become None (the miss is still
    counted) rather than surviving as a broken "$<hexid>" string.
    Returns the number of refs that did not resolve.
    """
    comps = (result.get("designSystem") or {}).get("components") or []
    encoded, misses = None, 0
    for comp in comps:
        html = comp.get("html")
        if html == "$undefined":
            comp["html"] = None
            continue
        if not isinstance(html, str) or not FLIGHT_REF_RE.match(html):
            continue
        if encoded is None:
            encoded = blob.encode("utf-8")
        m = re.search(rb"(?<![0-9a-zA-Z])" + html[1:].encode()
                      + rb":T([0-9a-f]+),", encoded)
        if not m:
            comp["html"] = None
            misses += 1
            continue
        n = int(m.group(1), 16)
        comp["html"] = encoded[m.end():m.end() + n].decode("utf-8", "replace")
    return misses


def parse_page(page):
    """Return (result dict, design_md str) or raise."""
    blob = flight_blob(page)
    result = extract_result(blob)
    if result is None:
        raise ValueError("no result object in flight payload")
    misses = resolve_component_html(result, blob)
    if misses:
        print(f"warning: {misses} component html refs unresolved",
              file=sys.stderr)
    return result, extract_design_md(page)


def style_name(result, page):
    name = (result.get("meta") or {}).get("siteName")
    if name:
        return name.strip()
    m = TITLE_RE.search(page)
    return m.group(1).strip() if m else None


# The styles columns a fetch writes, in insert order; uuid first. The export
# columns (variables_css, theme_css, tokens_json, design_system_json,
# prompt_txt) belong to cmd_export and a refetch keeps them.
FETCHED_COLUMNS = (
    "uuid", "slug", "name", "tagline", "page_url", "source_url", "theme",
    "extracted_at", "fetched_at", "design_md", "result_json", "screenshot_url",
    "video_url", "video_poster_url", "video_detail_url",
    "video_detail_poster_url", "media_fetched_at",
    "product_type", "design_style", "tags",
    "components_json", "components_at")
UPSERT_STYLE = (
    "INSERT INTO styles (" + ", ".join(FETCHED_COLUMNS) + ") VALUES ("
    + ", ".join("?" * len(FETCHED_COLUMNS)) + ") ON CONFLICT(uuid) DO UPDATE SET "
    + ", ".join(f"{c}=excluded.{c}" for c in FETCHED_COLUMNS[1:]))


def init_db():
    REFERO.mkdir(exist_ok=True)
    WORK.mkdir(exist_ok=True)
    if DB.exists():
        with open(DB, "rb") as f:
            if f.read(64).startswith(b"version https://git-lfs"):
                sys.exit(f"error: {DB} is a Git LFS pointer; "
                         "run: git lfs install && git lfs pull")
    db = sqlite3.connect(DB)
    db.execute("PRAGMA busy_timeout=30000")
    db.executescript(SCHEMA)
    have = {r[1] for r in db.execute("PRAGMA table_info(styles)")}
    for col in MEDIA_COLUMNS + LABEL_COLUMNS + COMPONENT_COLUMNS:
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


# A unique temp file and a rename, so a crash never leaves a truncated file
# and two processes writing one file (classify and backfill both write
# meta.json) cannot rename each other's half-written copy.
write_atomic = refero_dump.write_atomic


def style_dir(slug, old_slug=None):
    """refero/<slug>/, created if needed. A refetch whose name now slugs
    differently moves the style's old folder (and its exported files) to the
    new slug, so the old one is not left behind as an orphan check.py fails on."""
    outdir = REFERO / slug
    old_dir = REFERO / old_slug if old_slug and old_slug != slug else None
    if old_dir and old_dir.is_dir() and not outdir.exists():
        os.replace(old_dir, outdir)
    outdir.mkdir(exist_ok=True)
    return outdir


def style_meta(uuid, slug, name, result, media, labels, fetched_at):
    """The meta.json object a fetched style gets: uuid/slug/name, tagline and
    theme from designSystem, the classify.py label keys, the URLs, then the
    media keys (fixed schema; null when absent). write_meta's rebuild selects
    the same keys back out of the styles row."""
    meta = result.get("meta") or {}
    ds = result.get("designSystem") or {}
    return {
        "uuid": uuid,
        "slug": slug,
        "name": name,
        "tagline": ds.get("northStar"),
        "theme": ds.get("theme"),
        **labels,
        "page_url": f"{BASE}/style/{uuid}",
        "source_url": meta.get("url"),
        "extracted_at": meta.get("extractedAt"),
        "fetched_at": fetched_at,
        "screenshot_url": (result.get("screenshot") or {}).get("url"),
        **media,
        "has_components": any(
            c.get("html") for c in ds.get("components") or []),
    }


def write_meta(db, slug, media):
    """Merge media keys into refero/<slug>/meta.json, preserving key order.

    A missing meta.json is rebuilt from the styles row; one that does not
    parse is moved aside to meta.json.bad first, so a torn file is never
    replaced by a media-keys-only file that drops
    uuid/slug/name/source_url/page_url.
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
                  f"{bad.name} and rebuilt from the db", file=sys.stderr)
            meta_obj = None
    if meta_obj is None:
        row = db.execute(
            """SELECT uuid, slug, name, tagline, theme,
                      product_type, design_style, tags, page_url,
                      source_url, extracted_at, fetched_at, screenshot_url
               FROM styles WHERE slug=?""", (slug,)).fetchone()
        meta_obj = {
            "uuid": row[0],
            "slug": row[1],
            "name": row[2],
            "tagline": row[3],
            "theme": row[4],
            "product_type": row[5],
            "design_style": row[6],
            "tags": json.loads(row[7] or "[]"),
            "page_url": row[8],
            "source_url": row[9],
            "extracted_at": row[10],
            "fetched_at": row[11],
            "screenshot_url": row[12],
        } if row else {}
    meta_obj.update(media)
    row = db.execute(
        "SELECT components_json IS NOT NULL FROM styles WHERE slug=?",
        (slug,)).fetchone()
    if row:
        meta_obj["has_components"] = bool(row[0])
    meta_path.parent.mkdir(exist_ok=True)
    write_atomic(meta_path, json.dumps(meta_obj, indent=2) + "\n")


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

            name = name or uuid
            slug = unique_slug(db, name, uuid)
            # A refetch must not erase labels classify.py or a human already set.
            old = db.execute(
                "SELECT product_type, design_style, tags, slug FROM styles WHERE uuid=?",
                (uuid,)).fetchone()
            labels = {"product_type": old[0], "design_style": old[1],
                      "tags": json.loads(old[2] or "[]")} if old and old[0] \
                     else {"product_type": None, "design_style": None, "tags": []}
            write_atomic(WORK / f"{uuid}.json", json.dumps(result))
            outdir = style_dir(slug, old[3] if old else None)
            if design_md:
                write_atomic(outdir / "DESIGN.md", design_md)
            meta_obj = style_meta(
                uuid, slug, name, result, media, labels,
                time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()))
            write_atomic(outdir / "meta.json", json.dumps(meta_obj, indent=2) + "\n")
            comps = (result.get("designSystem") or {}).get("components") or []
            resolved = [c for c in comps if c.get("html")]
            cpath = outdir / "components.json"
            if resolved:
                write_atomic(cpath, json.dumps(comps, indent=2) + "\n")
            elif cpath.exists():
                cpath.unlink()
            # An upsert, not INSERT OR REPLACE: a replace deletes the row
            # first, so a refetch would NULL the export columns
            # (variables_css ... prompt_txt) until a later export succeeds.
            db.execute(
                UPSERT_STYLE,
                (uuid, slug, name, meta_obj["tagline"], url, meta_obj["source_url"],
                 meta_obj["theme"], meta_obj["extracted_at"], meta_obj["fetched_at"],
                 design_md, json.dumps(result), meta_obj["screenshot_url"],
                 media["video_url"], media["video_poster_url"],
                 media["video_detail_url"], media["video_detail_poster_url"],
                 meta_obj["fetched_at"], meta_obj["product_type"],
                 meta_obj["design_style"], json.dumps(meta_obj["tags"]),
                 json.dumps(comps) if resolved else None,
                 meta_obj["fetched_at"] if resolved else None))
            # Clear the row's earlier failure, if any, in the same commit.
            db.execute("DELETE FROM fetch_errors WHERE uuid=?", (uuid,))
            db.commit()
            fetched += 1
            if fetched % 50 == 0:
                print(f"fetched {fetched}/{len(uuids)}")
    total_errors = db.execute(
        "SELECT COUNT(*) FROM fetch_errors").fetchone()[0]
    print(f"fetched {fetched}, errors {len(uuids) - fetched} "
          f"({total_errors} in fetch_errors)")
    db.close()


def cmd_export():
    """Run the node export pass over every stored result, update files + db."""
    db = init_db()
    rows = db.execute(
        "SELECT uuid, slug FROM styles WHERE result_json IS NOT NULL").fetchall()
    jobs = []
    for uuid, slug in rows:
        rpath = WORK / f"{uuid}.json"
        # A torn cache file must not shadow the good copy in the db.
        try:
            json.loads(rpath.read_text())
            usable = True
        except (OSError, ValueError):
            usable = False
        if not usable:
            row = db.execute("SELECT result_json FROM styles WHERE uuid=?",
                             (uuid,)).fetchone()
            write_atomic(rpath, row[0])
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
            # meta.json first, then the db: a crash between the two leaves a
            # retryable NULL media_fetched_at, not an enriched row with a
            # meta.json that lacks the media keys.
            write_meta(db, slug, media)
            db.execute(
                """UPDATE styles SET video_url=?, video_poster_url=?,
                   video_detail_url=?, video_detail_poster_url=?,
                   media_fetched_at=? WHERE uuid=?""",
                (media["video_url"], media["video_poster_url"],
                 media["video_detail_url"], media["video_detail_poster_url"],
                 time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), uuid))
            db.execute("DELETE FROM fetch_errors WHERE uuid=?", (uuid,))
            db.commit()
            done += 1
            if done % 50 == 0:
                print(f"enriched {done}/{len(rows)}")
    total_errors = db.execute(
        "SELECT COUNT(*) FROM fetch_errors").fetchone()[0]
    print(f"enriched {done}, errors {len(rows) - done} "
          f"({total_errors} in fetch_errors)")
    db.close()


def cmd_catalog():
    db = init_db()
    rows = db.execute(
        """SELECT slug, name, tagline, uuid, page_url, source_url, theme,
                  extracted_at, fetched_at, product_type, design_style, tags,
                  components_json IS NOT NULL
           FROM styles ORDER BY name""").fetchall()
    tables = {r[0] for r in db.execute(
        "SELECT name FROM sqlite_master WHERE type='table'")}
    similar, colls = {}, {}
    if "similar" in tables:
        for u, s in db.execute(
                "SELECT uuid, matched_slug FROM similar "
                "WHERE matched_slug IS NOT NULL ORDER BY uuid, rank"):
            similar.setdefault(u, []).append(s)
    if "collection_styles" in tables:
        for u, c in db.execute(
                "SELECT style_uuid, collection_slug FROM collection_styles"):
            colls.setdefault(u, set()).add(c)
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
             "product_type": pt, "design_style": st, "tags": json.loads(tg or "[]"),
             "extracted_at": ea, "fetched_at": fa,
             "has_components": bool(hc),
             "similar": similar.get(u, []),
             "collections": sorted(colls.get(u, ()))}
            for s, n, t, u, p, su, th, ea, fa, pt, st, tg, hc in rows
        ],
    }
    write_atomic(REFERO / "catalog.json", json.dumps(catalog, indent=2) + "\n")
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
    try:
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
    finally:
        # However the run ends, the committed text dump follows the db
        # (refero/README.md, "Merging").
        refero_dump.refresh(DB)


if __name__ == "__main__":
    main()
