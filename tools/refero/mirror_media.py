#!/usr/bin/env python3
"""Mirror refero media assets (screenshots, posters, videos, favicons) locally.

Reads refero/refero.db and downloads into a media root (default:
$DESIGN_SYSTEMS_MEDIA or ~/services/design-systems/media/refero):

    shots/<slug>.jpg           styles.screenshot_url
    posters/<slug>.jpg         styles.video_poster_url
    videos/<slug>.mp4          styles.video_url
    detail/<slug>.mp4          styles.video_detail_url
    detail-posters/<slug>.jpg  styles.video_detail_poster_url
    favicons/<slug>.png        Google faviconV2 for the source_url host

Resumable: existing non-empty files are skipped unless --force. Downloads go
to <name>.partial and are renamed on success; a response whose Content-Type
does not match the expected image/ or video/ prefix is discarded (guards
against 404 HTML error pages). Only https URLs are fetched (redirects too), and a row whose
slug is not lowercase letters, digits and hyphens is skipped and reported
(--check fails on it): both come from the db, which merges from a committed
text dump, so neither may reach a local file or a path outside the root.

Usage:
    python3 tools/refero/mirror_media.py [--media-root DIR] [--workers 6]
        [--limit N] [--only shots,posters] [--force] [--compress-videos]
    python3 tools/refero/mirror_media.py --check   # exit 1 if any expected file is absent

--compress-videos needs ffmpeg on PATH (a ~/.nix-profile/bin/ffmpeg install is
tried as a fallback); without it the flag warns and videos are mirrored raw.
"""

import argparse
import concurrent.futures
import os
import shutil
import sqlite3
import subprocess
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DB = ROOT / "refero" / "refero.db"
sys.path.insert(0, str(Path(__file__).resolve().parent))
import refero_media  # noqa: E402

UA = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml",
}

# The kind -> (extension, Content-Type) table, /refero-media path builders and
# the gstatic favicon URL all live in refero_media.py, shared with catalog.py's
# emitted `local`/`remote` fields.
KINDS = refero_media.KINDS
FAVICON_API = refero_media.FAVICON_API
favicon_url = refero_media.favicon_url
media_dest = refero_media.media_dest

# Some CDNs serve media with a generic type; still not an HTML error page.
GENERIC_CT = {"application/octet-stream", "binary/octet-stream"}


def style_urls(row):
    """All candidate (kind, url) pairs for one styles row."""
    slug, shot, poster, video, detail, detail_poster, source = row
    return {
        "shots": shot,
        "posters": poster,
        "videos": video,
        "detail": detail,
        "detail-posters": detail_poster,
        "favicons": favicon_url(source),
    }


class NotHttps(ValueError):
    """A URL, or a redirect target, that is not https."""


def require_https(url, what="url"):
    if urllib.parse.urlsplit(url).scheme.lower() != "https":
        raise NotHttps(f"refusing a non-https {what} {url!r}")


class HttpsOnlyRedirect(urllib.request.HTTPRedirectHandler):
    """Follow a redirect only when its target is https too."""

    def redirect_request(self, req, fp, code, msg, headers, newurl):
        require_https(newurl, "redirect to")
        return super().redirect_request(req, fp, code, msg, headers, newurl)


# Every download goes through this opener, never the global urlopen.
OPENER = urllib.request.build_opener(HttpsOnlyRedirect)


def download(kind, url, dest):
    """GET url with retry/backoff, verify Content-Type, write dest atomically.

    Refuses anything but an https URL before opening it, and any redirect
    away from https: urllib would read a file:// URL from the local disk (and
    guess an image/ type for a .jpg), and follows https -> http redirects."""
    require_https(url)
    for i in range(4):
        try:
            req = urllib.request.Request(url, headers=UA)
            with OPENER.open(req, timeout=120) as r:
                ct = (r.headers.get("Content-Type") or "").split(";")[0] \
                    .strip().lower()
                data = r.read()
            break
        except NotHttps:
            raise
        except Exception:
            if i == 3:
                raise
            time.sleep(2 ** i)
    if not (ct.startswith(KINDS[kind][1]) or ct in GENERIC_CT):
        raise ValueError(f"unexpected content-type {ct or 'none'}")
    tmp = dest.parent / (dest.name + ".partial")
    try:
        tmp.write_bytes(data)
        os.replace(tmp, dest)
    except BaseException:
        tmp.unlink(missing_ok=True)
        raise


def compress_video(path, ffmpeg):
    """Re-encode path in place (faststart, <=960px wide, crf 28, no audio).

    Keeps the smaller of the two files; returns True if replaced, False if
    the encode came out no smaller. Raises RuntimeError when ffmpeg fails."""
    tmp = path.parent / (path.stem + ".compress" + path.suffix)
    try:
        proc = subprocess.run(
            [ffmpeg, "-y", "-i", str(path), "-movflags", "+faststart",
             "-vf", "scale='min(960,iw)':-2", "-crf", "28", "-an", str(tmp)],
            capture_output=True, timeout=600)
        ok = (proc.returncode == 0 and tmp.exists()
              and tmp.stat().st_size > 0)
        if not ok:
            tail = proc.stderr.decode(errors="replace").strip().splitlines()
            raise RuntimeError(
                tail[-1] if tail else f"ffmpeg exit {proc.returncode}")
        if tmp.stat().st_size < path.stat().st_size:
            os.replace(tmp, path)
            return True
        return False
    finally:
        tmp.unlink(missing_ok=True)


def missing_files(rows, media_root, only):
    """(kind, slug) pairs whose emitted local file is absent or empty.

    A remote URL exists for the row but the mirror file does not, so a page
    serving /refero-media would 404 and fall back to the CDN."""
    missing = []
    for row in rows:
        slug = row[0]
        for kind, url in style_urls(row).items():
            if kind not in only or not url:
                continue
            dest = media_dest(media_root, kind, slug)
            if not (dest.is_file() and dest.stat().st_size > 0):
                missing.append((kind, slug))
    return missing


def open_db():
    """Open refero.db read-only.

    Exits with a clear message when the db is missing (a bare
    sqlite3.connect would create a 0-byte file that then dies on
    'no such table'), or is still a Git LFS pointer (a clone without
    `git lfs pull`)."""
    if not DB.exists():
        sys.exit(f"error: {DB} not found; run tools/refero/fetch.py first")
    with open(DB, "rb") as f:
        if f.read(64).startswith(b"version https://git-lfs"):
            sys.exit(f"error: {DB} is a Git LFS pointer; "
                     "run: git lfs install && git lfs pull")
    db = sqlite3.connect(f"file:{DB}?mode=ro", uri=True)
    db.execute("PRAGMA busy_timeout=30000")
    return db


def do_job(job, ffmpeg):
    kind, slug, url, dest, compress = job
    status = "downloaded"
    if url is not None:
        try:
            download(kind, url, dest)
        except Exception as ex:
            return kind, "failed", False, f"{slug}: {ex}"
    else:
        # A compress-only job over an already-mirrored file.
        status = "skipped"
    compressed = False
    if compress and kind in ("videos", "detail") and ffmpeg:
        try:
            compressed = compress_video(dest, ffmpeg)
        except Exception as ex:
            return kind, status, False, f"{slug}: compress: {ex}"
    return kind, status, compressed, None


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--media-root", type=Path, default=None,
                    help="media dir (default: $DESIGN_SYSTEMS_MEDIA or "
                         "~/services/design-systems/media/refero)")
    ap.add_argument("--workers", type=int, default=6)
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--only", type=str, default="",
                    help="comma list of " + ",".join(KINDS))
    ap.add_argument("--force", action="store_true")
    ap.add_argument("--compress-videos", action="store_true")
    ap.add_argument("--check", action="store_true",
                    help="verify every expected file exists under the media root; "
                         "downloads nothing")
    args = ap.parse_args()
    if args.media_root is None:
        args.media_root = refero_media.default_media_root()

    only = (set(KINDS) if not args.only
            else {s.strip() for s in args.only.split(",") if s.strip()})
    bad = only - set(KINDS)
    if bad:
        ap.error(f"unknown --only kinds: {', '.join(sorted(bad))}")

    ffmpeg = None
    if args.compress_videos:
        ffmpeg = shutil.which("ffmpeg")
        if not ffmpeg:
            cand = Path.home() / ".nix-profile" / "bin" / "ffmpeg"
            ffmpeg = str(cand) if cand.exists() else None
        if not ffmpeg:
            print("warning: ffmpeg not found, skipping --compress-videos",
                  file=sys.stderr)

    db = open_db()
    try:
        rows = db.execute(
            """SELECT slug, screenshot_url, video_poster_url, video_url,
                      video_detail_url, video_detail_poster_url, source_url
               FROM styles ORDER BY slug""").fetchall()
    except sqlite3.DatabaseError as ex:
        sys.exit(f"error: {DB}: {ex}; run tools/refero/fetch.py first")
    finally:
        db.close()
    if args.limit:
        rows = rows[:args.limit]
    unsafe = [row[0] for row in rows if not refero_media.safe_slug(row[0])]
    rows = [row for row in rows if refero_media.safe_slug(row[0])]
    for slug in unsafe:
        print(f"FAIL {slug!r}: unsafe slug, skipped", file=sys.stderr)

    if args.check:
        missing = missing_files(rows, args.media_root, only)
        if unsafe and not missing:
            sys.exit(f"{len(unsafe)} styles rows have an unsafe slug")
        if not missing:
            print(f"media root ok: every expected file exists under "
                  f"{args.media_root}")
            return
        by_kind = {k: [] for k in KINDS}
        for kind, slug in missing:
            by_kind[kind].append(slug)
        for kind in KINDS:
            slugs = by_kind[kind]
            if not slugs:
                continue
            print(f"{kind}: {len(slugs)} missing "
                  f"(e.g. {', '.join(slugs[:3])})", file=sys.stderr)
        sys.exit(f"{len(missing)} expected files missing under "
                 f"{args.media_root}"
                 + (f"; {len(unsafe)} styles rows have an unsafe slug"
                    if unsafe else ""))

    counts = {k: {"downloaded": 0, "skipped": 0, "missing": 0, "failed": 0,
                  "compressed": 0} for k in KINDS}
    jobs = []
    for row in rows:
        slug = row[0]
        for kind, url in style_urls(row).items():
            if kind not in only:
                continue
            if not url:
                counts[kind]["missing"] += 1
                continue
            dest = media_dest(args.media_root, kind, slug)
            if (dest.exists() and dest.stat().st_size > 0
                    and not args.force):
                if args.compress_videos and kind in ("videos", "detail"):
                    jobs.append((kind, slug, None, dest, True))
                    continue
                counts[kind]["skipped"] += 1
                continue
            dest.parent.mkdir(parents=True, exist_ok=True)
            jobs.append((kind, slug, url, dest, args.compress_videos))

    print(f"{len(jobs)} files to fetch or compress under {args.media_root}")
    done = 0
    with concurrent.futures.ThreadPoolExecutor(
            max_workers=args.workers) as pool:
        for kind, status, compressed, err in pool.map(
                lambda j: do_job(j, ffmpeg), jobs):
            counts[kind][status] += 1
            if compressed:
                counts[kind]["compressed"] += 1
            if err:
                print(f"FAIL {err}", file=sys.stderr)
            done += 1
            if done % 50 == 0:
                print(f"{done}/{len(jobs)}")

    header = ["kind", "downloaded", "skipped", "missing", "failed"]
    if args.compress_videos:
        header.append("compressed")
    print(("{:<10}" + "{:>12}" * (len(header) - 1)).format(*header))
    for kind in KINDS:
        if kind not in only:
            continue
        c = counts[kind]
        cells = [kind, c["downloaded"], c["skipped"], c["missing"],
                 c["failed"]]
        if args.compress_videos:
            cells.append(c["compressed"])
        print(("{:<10}" + "{:>12}" * (len(cells) - 1)).format(*cells))


if __name__ == "__main__":
    main()
