#!/usr/bin/env python3
"""Fetch a product's app or site icon into its package as `icon.png`.

    python3 tools/fetch_icon.py SLUG...          fetch each package's icon
    python3 tools/fetch_icon.py SLUG --host H    read the icon from host H instead of the
                                                 catalog entry's product URL
    python3 tools/fetch_icon.py SLUG --url U     fetch this exact icon file
    python3 tools/fetch_icon.py --all            every package in catalog.json

The icon is what identifies the package at a glance: the gallery cards and
detail pages and the root README's catalog table show it. It sits at
`systems/<slug>/icon.png`, a 128 px PNG (Git LFS), and the catalog entry's
`preview.icon` names it.

Sources tried in order: the site's own `apple-touch-icon` link (or
/apple-touch-icon.png), the largest `<link rel="icon">` PNG the page declares,
then Google's faviconV2 endpoint (the same route the refero mirror uses). The
result is normalised to at most 128 px on a side with macOS `sips`, keeping its
format's transparency; SVG and unreadable responses are skipped, which is how
the faviconV2 fallback gets reached for sites that ship only vector icons.

Standard library only plus `sips`. Run from anywhere.
"""
from __future__ import annotations

import argparse
import importlib.util
import json
import re
import subprocess
import sys
import tempfile
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# The gstatic faviconV2 URL, shared with the refero favicon mirror
# (tools/refero/refero_media.py's FAVICON_API), imported by location so
# tools/refero/ stays off sys.path.
_spec = importlib.util.spec_from_file_location(
    "refero_media", Path(__file__).resolve().parent / "refero" / "refero_media.py")
refero_media = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(refero_media)

SIZE = 128
UA = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                    "AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.4 Safari/605.1.15"}
CONTENT_EXT = {"png": ".png", "x-icon": ".ico", "vnd.microsoft.icon": ".ico",
               "jpeg": ".jpg", "gif": ".gif", "webp": ".webp", "svg": ".svg"}


def fetch(url: str, timeout: int = 20) -> tuple[bytes, str] | None:
    """(body, content-type) of a URL, or None. A non-image response is None."""
    try:
        req = urllib.request.Request(url, headers=UA)
        with urllib.request.urlopen(req, timeout=timeout) as r:
            ctype = (r.headers.get("Content-Type") or "").split(";")[0].strip().lower()
            return r.read(8 << 20), ctype
    except (OSError, urllib.error.URLError):
        return None


def candidates(home: str) -> list[str]:
    """Icon URLs for a product page, best first: the apple-touch-icon the page
    declares (then the stock path), the largest PNG favicon link, then faviconV2."""
    parsed = urllib.parse.urlparse(home)
    base = f"{parsed.scheme}://{parsed.netloc}"
    out, page = [], fetch(home)
    links = []
    if page and "html" in page[1]:
        for tag in re.findall(r"<link\b[^>]*>", page[0].decode("utf-8", "replace"), re.I):
            rel = re.search(r'rel=["\']([^"\']+)', tag, re.I)
            href = re.search(r'href=["\']([^"\']+)', tag, re.I)
            sizes = re.search(r'sizes=["\'](\d+)', tag, re.I)
            if rel and href:
                links.append((rel.group(1).lower(), urllib.parse.urljoin(home, href.group(1)),
                              int(sizes.group(1)) if sizes else 0))
    out += [u for rel, u, _ in links if "apple-touch-icon" in rel]
    out.append(base + "/apple-touch-icon.png")
    raster = [(size, u) for rel, u, size in links
              if "icon" in rel and "apple" not in rel and not u.lower().endswith(".svg")]
    out += [u for _, u in sorted(raster, reverse=True)]
    if fav := refero_media.favicon_url(base):
        out.append(fav)
    return out


def convert(src: Path, dst: Path) -> bool:
    """src -> dst as a PNG of at most SIZE px on a side. sips reads what the file
    holds, not its extension, but it needs one it knows, so callers name the temp
    file after the response's Content-Type."""
    done = subprocess.run(["sips", "-s", "format", "png", "-Z", str(SIZE), str(src),
                           "--out", str(dst)], capture_output=True)
    return done.returncode == 0 and dst.exists() and dst.stat().st_size > 0


def fetch_icon(slug: str, home: str | None, icon_url: str | None) -> Path:
    if icon_url:
        urls = [icon_url]
    elif home:
        urls = candidates(home)
    else:
        entry = next((s for s in json.loads((ROOT / "catalog.json").read_text())["systems"]
                      if s["slug"] == slug), None)
        if not entry:
            raise SystemExit(f"{slug}: no catalog entry")
        urls = candidates(entry["url"])
    dst = ROOT / "systems" / slug / "icon.png"
    with tempfile.TemporaryDirectory() as tmp:
        for url in urls:
            got = fetch(url)
            if not got or not got[1].startswith("image/") or got[1].endswith("svg+xml"):
                continue
            ext = CONTENT_EXT.get(got[1].split("/")[-1], ".png")
            src = Path(tmp) / ("icon" + ext)
            src.write_bytes(got[0])
            if convert(src, dst):
                print(f"{slug}: {url} -> {dst.relative_to(ROOT)}")
                return dst
    raise SystemExit(f"{slug}: no icon source worked; try --host or --url")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("slugs", nargs="*")
    parser.add_argument("--all", action="store_true")
    parser.add_argument("--host", help="fetch the icon from this host instead of the catalog URL")
    parser.add_argument("--url", help="fetch this exact icon file")
    args = parser.parse_args()
    slugs = ([s["slug"] for s in json.loads((ROOT / "catalog.json").read_text())["systems"]]
             if args.all else args.slugs)
    if not slugs:
        parser.error("name at least one slug, or --all")
    if (args.host or args.url) and len(slugs) != 1:
        parser.error("--host and --url apply to a single slug")
    home = f"https://{args.host}" if args.host else None
    for slug in slugs:
        fetch_icon(slug, home, args.url)


if __name__ == "__main__":
    main()
