#!/usr/bin/env python3
"""Mirror refero media assets (screenshots, posters, videos, favicons) locally.

Reads refero/refero.db and downloads into a media root (default:
$DESIGN_SYSTEMS_MEDIA or ~/services/design-systems/media/refero):

    shots/<slug>.jpg      styles.screenshot_url
    posters/<slug>.jpg    styles.video_poster_url
    videos/<slug>.mp4     styles.video_url
    detail/<slug>.mp4     styles.video_detail_url
    favicons/<slug>.png   Google faviconV2 for the source_url host

Resumable: existing non-empty files are skipped unless --force. Downloads go
to <name>.partial and are renamed on success; a response whose Content-Type
does not match the expected image/ or video/ prefix is discarded (guards
against 404 HTML error pages).

Usage:
    python3 tools/refero/mirror_media.py [--media-root DIR] [--workers 6]
        [--limit N] [--only shots,posters] [--force] [--compress-videos]
"""

import argparse
import concurrent.futures
import os
import shutil
import sqlite3
import subprocess
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DB = ROOT / "refero" / "refero.db"
DEFAULT_MEDIA_ROOT = Path(
    os.environ.get("DESIGN_SYSTEMS_MEDIA")
    or "~/services/design-systems/media/refero").expanduser()

UA = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml",
}

# kind -> (extension, required Content-Type prefix)
KINDS = {
    "shots": (".jpg", "image/"),
    "posters": (".jpg", "image/"),
    "videos": (".mp4", "video/"),
    "detail": (".mp4", "video/"),
    "favicons": (".png", "image/"),
}
# Some CDNs serve media with a generic type; still not an HTML error page.
GENERIC_CT = {"application/octet-stream", "binary/octet-stream"}
FAVICON_API = ("https://t0.gstatic.com/faviconV2?client=SOCIAL&type=FAVICON"
               "&fallback_opts=TYPE,SIZE,URL&size=128&url=")


def favicon_url(source_url):
    """gstatic faviconV2 for the source host. The url param needs a scheme;
    a bare host returns 404."""
    if not source_url:
        return None
    parsed = urllib.parse.urlparse(
        source_url if "://" in source_url else "https://" + source_url)
    if not parsed.netloc:
        return None
    return FAVICON_API + urllib.parse.quote("https://" + parsed.netloc,
                                            safe="")


def style_urls(row):
    """All candidate (kind, url) pairs for one styles row."""
    slug, shot, poster, video, detail, source = row
    return {
        "shots": shot,
        "posters": poster,
        "videos": video,
        "detail": detail,
        "favicons": favicon_url(source),
    }


def download(kind, url, dest):
    """GET url with retry/backoff, verify Content-Type, write dest atomically."""
    for i in range(4):
        try:
            req = urllib.request.Request(url, headers=UA)
            with urllib.request.urlopen(req, timeout=120) as r:
                ct = (r.headers.get("Content-Type") or "").split(";")[0] \
                    .strip().lower()
                data = r.read()
            break
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

    Keeps the smaller of the two files; returns True if replaced."""
    tmp = path.parent / (path.stem + ".compress" + path.suffix)
    try:
        proc = subprocess.run(
            [ffmpeg, "-y", "-i", str(path), "-movflags", "+faststart",
             "-vf", "scale='min(960,iw)':-2", "-crf", "28", "-an", str(tmp)],
            capture_output=True, timeout=600)
        if (proc.returncode == 0 and tmp.exists()
                and 0 < tmp.stat().st_size < path.stat().st_size):
            os.replace(tmp, path)
            return True
        return False
    finally:
        tmp.unlink(missing_ok=True)


def do_job(job, ffmpeg):
    kind, slug, url, dest, compress = job
    try:
        download(kind, url, dest)
    except Exception as ex:
        return kind, "failed", False, f"{slug}: {ex}"
    compressed = False
    if compress and kind in ("videos", "detail") and ffmpeg:
        try:
            compressed = compress_video(dest, ffmpeg)
        except Exception:
            pass
    return kind, "downloaded", compressed, None


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--media-root", type=Path, default=DEFAULT_MEDIA_ROOT)
    ap.add_argument("--workers", type=int, default=6)
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--only", type=str, default="",
                    help="comma list of " + ",".join(KINDS))
    ap.add_argument("--force", action="store_true")
    ap.add_argument("--compress-videos", action="store_true")
    args = ap.parse_args()

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

    db = sqlite3.connect(DB)
    rows = db.execute(
        """SELECT slug, screenshot_url, video_poster_url, video_url,
                  video_detail_url, source_url
           FROM styles ORDER BY slug""").fetchall()
    db.close()
    if args.limit:
        rows = rows[:args.limit]

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
            dest = args.media_root / kind / (slug + KINDS[kind][0])
            if (dest.exists() and dest.stat().st_size > 0
                    and not args.force):
                counts[kind]["skipped"] += 1
                continue
            dest.parent.mkdir(parents=True, exist_ok=True)
            jobs.append((kind, slug, url, dest, args.compress_videos))

    print(f"{len(jobs)} files to fetch under {args.media_root}")
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
