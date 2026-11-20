"""The /refero-media path contract, shared between the emit and fetch sides.

    /refero-media/<kind>/<slug><ext>   served by the site (catalog.py emits it
                                       as a media entry's `local`)
    <media_root>/<kind>/<slug><ext>    where mirror_media.py downloads it to

catalog.py's emitted `local` paths, mirror_media.py's destinations and the
nginx alias for /refero-media/ all come back to this one table, so a kind or
extension change lands on every side at once. mirror_media.py --check walks
the styles rows and verifies each expected file exists.

Slugs are already URL-safe (fetch.slugify), so neither side URL-encodes them.
media_dest() refuses any other slug: it comes from the db, which merges from
the committed text dump, so a path-like one must never become a file path.
"""

import os
import re
import urllib.parse
from pathlib import Path


# The .env keys the repo's Python reads: media locations, the API server's allowed hosts, the chat
# and classify key and model, the R2 upload credentials. Nothing else in .env (the site password,
# anything added later) is ever copied into os.environ by this module.
ENV_KEYS = ("DESIGN_SYSTEMS_MEDIA", "DESIGN_SYSTEMS_MEDIA_BASE", "DESIGN_SYSTEMS_ALLOWED_HOSTS",
            "ANTHROPIC_API_KEY", "DS_CHAT_MODEL",
            "R2_ACCOUNT_ID", "R2_ACCESS_KEY_ID", "R2_SECRET_ACCESS_KEY", "R2_BUCKET")


def load_env(keys=ENV_KEYS, env_file=None):
    """Copy the named keys from the repo's gitignored .env into os.environ; variables already set
    win. Returns the keys it set. An entry point that needs a secret calls this with just the keys
    it reads (server/chat.py: load_env(("ANTHROPIC_API_KEY", "DS_CHAT_MODEL"))). Nothing loads
    .env on import, and a call whose keys are all set already never opens it."""
    env = Path(env_file) if env_file else Path(__file__).resolve().parents[2] / ".env"
    wanted, done = {k for k in keys if k not in os.environ}, []
    if not wanted or not env.is_file():
        return done
    for line in env.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, val = line.partition("=")
        key, val = key.strip(), val.strip().strip('"').strip("'")
        if key.startswith("export "):
            key = key[len("export "):].strip()
        if key in wanted and key not in os.environ:
            os.environ[key] = val
            done.append(key)
    return done


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

# Google's faviconV2 endpoint for the source host: where mirror_media.py and
# fetch_icon.py download a favicon, host-side. Never emitted to a browser
# (catalog.py's favicon pair has no remote), so browsing tells Google nothing.
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


# What fetch.slugify produces: lowercase letters and digits joined by single
# hyphens. catalog.py's REFERO_SLUG is the same rule on the emit side.
SLUG = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*")


def safe_slug(slug):
    """True when slug is one fetch.slugify could have produced."""
    return isinstance(slug, str) and SLUG.fullmatch(slug) is not None


def media_dest(media_root, kind, slug):
    """The file local_path() resolves to under a media root.

    Raises ValueError for a slug that is not lowercase letters, digits and
    hyphens, so `../x` or `a/b` can never name a file outside the root."""
    if not safe_slug(slug):
        raise ValueError(f"unsafe refero slug {slug!r}")
    return Path(media_root) / kind / (slug + KINDS[kind][0])


# Where the mirrored tree lives: $DESIGN_SYSTEMS_MEDIA, else a sibling of the
# checkout under ~/services. Shared by mirror_media.py's downloads and
# catalog.py's /refero-media/ serving, so both agree on one root.
def media_base():
    """Public base URL for mirrored media (the R2 bucket), prepended to
    /refero-media paths by the emitted JSON's `mediaBase` and the app.

    DESIGN_SYSTEMS_MEDIA_BASE overrides it; set it empty to serve the paths
    from the site itself (a local mirror, or the deployed nginx alias)."""
    load_env(("DESIGN_SYSTEMS_MEDIA_BASE",))
    return os.environ.get("DESIGN_SYSTEMS_MEDIA_BASE",
                          "https://pub-b22e019453104cc8b3c214b1009a6c42.r2.dev")


def default_media_root():
    load_env(("DESIGN_SYSTEMS_MEDIA",))
    return Path(
        os.environ.get("DESIGN_SYSTEMS_MEDIA")
        or "~/services/design-systems/media/refero").expanduser()
