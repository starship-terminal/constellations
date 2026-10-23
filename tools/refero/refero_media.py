"""The /refero-media path contract, shared between the emit and fetch sides.

    /refero-media/<kind>/<slug><ext>   served by the site (catalog.py emits it
                                       as a media entry's `local`)
    <media_root>/<kind>/<slug><ext>    where mirror_media.py downloads it to

catalog.py's emitted `local` paths, mirror_media.py's destinations and the
nginx alias for /refero-media/ all come back to this one table, so a kind or
extension change lands on every side at once. mirror_media.py --check walks
the styles rows and verifies each expected file exists.

Slugs are already URL-safe (fetch.slugify), so neither side URL-encodes them.
"""

import urllib.parse
from pathlib import Path

# media dir -> (file extension, required Content-Type prefix).
# catalog.py maps its payload keys (shot, poster, video, detail,
# detail_poster, favicon) onto these dir names; app.js's rfLocalMedia
# hardcodes the same paths for index cards, pinned by tools/test_refero.py.
KINDS = {
    "shots": (".jpg", "image/"),
    "posters": (".jpg", "image/"),
    "videos": (".mp4", "video/"),
    "detail": (".mp4", "video/"),
    "detail-posters": (".jpg", "image/"),
    "favicons": (".png", "image/"),
}

# The favicon "remote" is Google's faviconV2 endpoint for the source host;
# the mirrored file is what that URL returned.
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


def local_path(kind, slug):
    """The `local` path emitted into refero JSON, e.g. /refero-media/shots/x.jpg."""
    return f"/refero-media/{kind}/{slug}{KINDS[kind][0]}"


def media_dest(media_root, kind, slug):
    """The file local_path() resolves to under a media root."""
    return Path(media_root) / kind / (slug + KINDS[kind][0])
