"""The tool layer behind the gallery chat and the MCP server: read-only functions
over the two stores (systems/ packages and the refero snapshot). chat.py wraps
them for a model's tool calls; routes.py surfaces their results to the page.

Every tool returns a JSON-able dict. Slugs resolve against catalog.json first,
then refero.db. File access is bounded the way catalog.repo_file is: a resolved
path must stay inside the package folder it names. Media tools return
site-relative URLs (the local server answers /systems/... from the checkout), and
view_media returns a {"_image": ...} marker dict that chat.py turns into an image
block for the provider.
"""
from __future__ import annotations

import base64
import importlib.util
import json
import os
import posixpath
import sqlite3
import sys
import threading
import urllib.parse
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "tools"))
import catalog  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
REFERO_DB = ROOT / "refero" / "refero.db"

IMAGE_TYPES = {".png": "image/png", ".jpg": "image/jpeg", ".jpeg": "image/jpeg",
               ".webp": "image/webp", ".gif": "image/gif"}
TEXT_TYPES = {".md", ".txt", ".json", ".css", ".html", ".svg", ".csv"}
MEDIA_DIRS = ("screenshots", "components", "icons", "boards")
# Package paths the tools never read, matching the research app's package
# document rules (app/src/server/sources/files.ts) and the package entries in
# .gitignore: raw captures, fonts, dependency and capture-scratch folders, and
# any dot segment.
PRIVATE_DIRS = {"raw", "fonts", "node_modules", "__pycache__"}
PRIVATE_PREFIXES = ("tools/capture/dumps/", "tools/capture/out/", "tools/capture/winid")

# A tool result's JSON text is capped before it goes back to the model: a whole
# token group or a README can run past what a turn should carry.
# Sizes are UTF-8 bytes of compact JSON, measured the same way in the web twin.
RESULT_CAP = 32_000
DOC_CAP = 24_000
TOKEN_PAGE = RESULT_CAP - 1_000  # bytes of name/value pairs one get_tokens page carries
# How a handoff prompt names the library's checkout.
HOME_VAR = "$DESIGN_SYSTEMS_HOME"
IMAGE_CAP = 3_500_000  # bytes on disk; bigger shots are refused unless Pillow shrinks them


class ToolError(Exception):
    """A tool's readable failure, returned to the model as its result text."""


def _json_size(obj) -> int:
    """UTF-8 bytes of obj as compact JSON: Buffer.byteLength(JSON.stringify(obj))
    in the web twin."""
    return len(json.dumps(obj, ensure_ascii=False, separators=(",", ":")).encode("utf-8", "replace"))


def _catalog() -> dict:
    """catalog.json, parsed once per change of the file rather than per tool
    call (it is ~1.5 MB). library.py is re-executed on every /api/ request so
    a deploy needs no restart (server/api.py), so the cache lives on the
    long-lived catalog module, keyed on the file's mtime and size; a pull that
    changes the file misses it. Callers only read the result."""
    st = (catalog.ROOT / "catalog.json").stat()
    key = (str(catalog.ROOT), st.st_mtime_ns, st.st_size)
    cached = getattr(catalog, "_library_cache", None)
    if cached is not None and cached[0] == key:
        return cached[1]
    # api.py serves requests on threads: one parses, the others wait for it.
    # The lock lives on the catalog module too, so every copy of library.py
    # shares it (setdefault is atomic under the GIL).
    with catalog.__dict__.setdefault("_library_lock", threading.Lock()):
        cached = getattr(catalog, "_library_cache", None)
        if cached is None or cached[0] != key:
            cached = catalog._library_cache = (key, catalog.load_catalog())
    return cached[1]


def _entry(slug: str) -> dict:
    for s in _catalog()["systems"]:
        if s["slug"] == slug:
            return s
    raise ToolError(f"no systems package '{slug}'")


def _pkg_dir(entry: dict) -> Path:
    return (ROOT / "systems" / entry["slug"]).resolve()


def _repo_file(rel: str) -> Path:
    """A repo-relative path from the catalog, resolved the bounded way."""
    target = catalog.repo_file("/" + rel.lstrip("/"))
    if target is None:
        raise ToolError(f"path outside the served set: {rel}")
    return target


def _private(rel: str) -> bool:
    """True for a package-relative path the tools must not read."""
    if rel in ("", "."):
        return False
    return (any(p.startswith(".") or p in PRIVATE_DIRS for p in rel.split("/"))
            or any(rel == pre.rstrip("/") or rel.startswith(pre) for pre in PRIVATE_PREFIXES))


def _walk_files(d: Path) -> list[Path]:
    """Every regular file under d, symlinks skipped (neither followed into a
    directory nor listed as a file), sorted by path like the web twin."""
    out = []
    for cur, dirs, files in os.walk(d, followlinks=False):
        for name in files:
            p = Path(cur) / name
            if not p.is_symlink() and p.is_file():
                out.append(p)
    return sorted(out, key=lambda p: p.as_posix())


def _bounded(entry: dict, rel: str) -> Path:
    """Resolve a package-relative path, refusing anything that climbs out.
    Accepts the repo-relative and site-absolute forms other tools emit, and
    the /media/ URL list_media returns (percent-decoded), so the model can pass
    a path it saw verbatim. Containment is checked on the resolved path, so a
    symlink inside the package cannot point out of it, and private folders
    (raw/, fonts/, dot paths) are refused under either name."""
    base = _pkg_dir(entry)
    slug = entry["slug"]
    raw = str(rel)
    if raw.lstrip("/").startswith("media/"):
        raw = urllib.parse.unquote(raw.split("?", 1)[0].split("#", 1)[0])
    clean = posixpath.normpath("/" + raw.lstrip("/")).lstrip("/")
    for prefix in (f"media/systems/{slug}/", f"systems/{slug}/"):
        if clean.startswith(prefix):
            clean = clean[len(prefix):]
            break
    target = (base / clean).resolve()
    if target != base and base not in target.parents:
        raise ToolError(f"path leaves the package: {rel}")
    if _private(posixpath.normpath(clean)) or _private(target.relative_to(base).as_posix()):
        raise ToolError(f"not readable through the tools: {rel}")
    return target


def _site_url(path: Path) -> str:
    # The app's /media/ route answers repo files on every frontend that serves
    # them (Next dev, standalone, the deployment); a bare /<repo path> only the
    # retired python server ever answered.
    # Each segment is quoted the way the web twin's encodeURIComponent does.
    rel = path.resolve().relative_to(ROOT.resolve()).as_posix()
    return "/media/" + "/".join(urllib.parse.quote(seg, safe="!~*'()") for seg in rel.split("/"))


# ---------------------------------------------------------------- refero store


def _refero_db() -> sqlite3.Connection | None:
    """A read-only handle, or None when the db is absent or an LFS pointer."""
    if not REFERO_DB.is_file():
        return None
    try:
        db = sqlite3.connect(f"file:{REFERO_DB}?mode=ro", uri=True)
    except sqlite3.Error:
        return None
    try:
        db.row_factory = sqlite3.Row
        db.execute("SELECT 1 FROM styles LIMIT 1").fetchone()
    except sqlite3.Error:
        db.close()
        return None
    return db


def _refero_search(words: list[str], style: str | None, limit: int) -> list[dict]:
    db = _refero_db()
    if db is None:
        return []
    rows = db.execute(
        "SELECT slug, name, tagline, theme, source_url, product_type, design_style, tags "
        "FROM styles WHERE slug IS NOT NULL").fetchall()
    db.close()
    hits = []
    for r in rows:
        labels = []
        try:
            labels = [str(t).lower() for t in json.loads(r["tags"] or "[]")]
        except (TypeError, ValueError):
            pass
        if style and r["design_style"] != style:
            continue
        # The source's host, not its full URL: the web twin's index.json only
        # holds the host, so both score "https" and paths the same (not at all).
        host = catalog._refero_host(r["source_url"])
        strong = " ".join([r["slug"] or "", r["name"] or "", r["design_style"] or "",
                           r["product_type"] or "", *labels]).lower()
        weak = " ".join([r["tagline"] or "", r["theme"] or "", host or ""]).lower()
        score = sum(2 if w in strong else 1 if w in weak else 0 for w in words)
        if score or not words:
            hits.append((score, r, host))
    hits.sort(key=lambda x: (-x[0], x[1]["slug"]))
    return [{"store": "refero", "slug": r["slug"], "name": r["name"], "score": score,
             "tagline": r["tagline"], "theme": r["theme"], "designStyle": r["design_style"],
             "productType": r["product_type"], "src": host}
            for score, r, host in hits[:limit] if score or not words]


# ---------------------------------------------------------------- tools


def search_styles(query: str, store: str = "all", platform: str | None = None,
                  style: str | None = None, limit: int = 8) -> dict:
    """Rank styles by free-text words. systems hits score name/tag hits double."""
    words = [w.lower() for w in str(query or "").split() if w.strip()]
    limit = max(1, min(int(limit or 8), 20))
    out: list[dict] = []
    # The catalog's platforms are web, mobile and desktop; "ios" stays an alias
    # for mobile, the value the schema offered first.
    wanted = "mobile" if platform == "ios" else platform
    if store in ("all", "systems"):
        # One catalog read per call, not one per hit.
        parsed = _catalog()
        by_slug = {s["slug"]: s for s in parsed["systems"]}
        for hit in catalog.find(words, parsed):
            e = by_slug.get(hit["slug"])
            if e is None:
                continue
            # The platform field only: a tag such as `mobile` marks a 390px pass of a web
            # package (mwm), which is not a mobile app.
            if platform and e.get("platform") != wanted:
                continue
            out.append({"store": "systems", "slug": hit["slug"], "name": hit["name"],
                        "score": hit["score"], "goodFor": hit["goodFor"], "tags": hit["tags"],
                        "themes": hit["themes"], "platform": e.get("platform")})
    if store in ("all", "refero"):
        out += _refero_search(words, style, limit)
    out.sort(key=lambda h: (h["store"] != "systems", -(h["score"] or 0)))
    return {"query": query, "hits": out[:limit],
            "note": "systems/ values carry evidence labels; prefer them over refero when both fit"}


def get_style(slug: str, store: str | None = None) -> dict:
    """The catalog entry distilled: what the style is for, what was captured,
    and which files hold the detail. `store` disambiguates a slug the two
    stores share; without it systems wins, then refero."""
    e = None
    if store in (None, "systems"):
        try:
            e = _entry(slug)
        except ToolError:
            if store == "systems":
                raise
    if e is None:
        db = _refero_db()
        if db is None:
            raise ToolError(f"no systems package '{slug}'")
        row = db.execute(
            "SELECT slug, name, tagline, theme, source_url, page_url, product_type, "
            "design_style, tags FROM styles WHERE slug=?", (slug,)).fetchone()
        db.close()
        if not row:
            raise ToolError(f"no {'refero ' if store == 'refero' else ''}style '{slug}'")
        row = dict(row)
        # refero.db stores tags as JSON text; the web twin returns the list.
        try:
            tags = json.loads(row.get("tags") or "[]")
        except (TypeError, ValueError):
            tags = []
        row["tags"] = tags if isinstance(tags, list) else []
        return {"store": "refero", **row,
                "note": "interpreted third-party data; browse screenshots and tokens, "
                        "never treat a value as measured"}
    return {"store": "systems", "slug": e["slug"], "name": e["name"], "url": e.get("url"),
            "category": e.get("category"), "goodFor": e.get("goodFor"), "tags": e.get("tags", []),
            "themes": e.get("themes", []), "platform": e.get("platform"), "shape": e.get("shape"),
            "widths": e.get("widths", []), "captured": e.get("captured"), "access": e.get("access"),
            "capture": e.get("capture"), "swatches": catalog.swatches(e),
            "files": {"readme": e.get("entry"), "tokens": e.get("tokens"),
                      "styleGuide": e.get("styleGuide"), "dir": f"systems/{e['slug']}"}}


def get_tokens(slug: str, group: str | None = None, offset: int = 0, limit: int | None = None) -> dict:
    """Resolved token values. Without a group it lists the groups and their sizes;
    with one it returns that group's flat name -> CSS value map. A group too big
    for one result comes back a page at a time: `offset` and `limit` count
    tokens, and a truncated page names the `nextOffset` to ask for."""
    e = _entry(slug)
    tokens = json.loads(_repo_file(e["tokens"]).read_text())
    exported = catalog.export_tokens(tokens, e.get("themes", []))
    groups = {"base": exported["base"], **exported["themes"]}
    if not group:
        return {"slug": slug, "groups": {k: len(v) for k, v in groups.items()},
                "skipped": len(exported["skipped"]), "unresolved": len(exported["unresolved"]),
                "note": "call again with group=<name> for its values"}
    if group not in groups:
        raise ToolError(f"no token group '{group}'; groups: {', '.join(groups)}")
    offset = int(offset or 0)
    limit = None if limit is None else int(limit)
    if offset < 0:
        raise ToolError("offset must be 0 or more")
    if limit is not None and limit < 1:
        raise ToolError("limit must be 1 or more")
    # Sorted by name so a page holds the same tokens in both twins (JSON.parse
    # reorders integer-like keys, so the file's order cannot be shared).
    items = sorted(groups[group].items())
    page, used = {}, 2
    for name, value in items[offset:]:
        if limit is not None and len(page) >= limit:
            break
        size = _json_size(name) + _json_size(value) + 2  # the colon and comma
        if page and used + size > TOKEN_PAGE:
            break
        page[name] = value
        used += size
    end = offset + len(page)
    out = {"slug": slug, "group": group, "tokens": page, "count": len(items), "offset": offset,
           "truncated": end < len(items)}
    if out["truncated"]:
        out["nextOffset"] = end
    return out


def read_doc(slug: str, path: str | None = None, offset: int = 0) -> dict:
    """A text file from the package: its README (the default), components.md,
    patterns.md, tokens.json. Path is relative to systems/<slug>/. A file over
    DOC_CAP characters comes back a page at a time: `offset` is where the page
    starts, and a truncated page names the `nextOffset` to ask for."""
    e = _entry(slug)
    rel = path or Path(e["entry"]).name
    offset = int(offset or 0)
    if offset < 0:
        raise ToolError("offset must be 0 or more")
    target = _bounded(e, rel)
    if target.is_dir():
        raise ToolError(f"{rel} is a directory")
    if not target.is_file():
        raise ToolError(f"no file {rel} in systems/{slug}/")
    if target.suffix.lower() not in TEXT_TYPES:
        raise ToolError(f"not a text file: {rel}")
    text = target.read_text(errors="replace")
    end = offset + DOC_CAP
    truncated = len(text) > end
    out = {"slug": slug, "path": f"systems/{slug}/{target.relative_to(_pkg_dir(e)).as_posix()}",
           "text": text[offset:end], "truncated": truncated, "offset": offset, "length": len(text)}
    if truncated:
        out["nextOffset"] = end
    return out


def list_media(slug: str, kind: str | None = None) -> dict:
    """Screenshot, crop, icon and board files with site-relative URLs the page
    can render. kind is one of screenshots|components|icons|boards."""
    e = _entry(slug)
    kinds = [kind] if kind else list(MEDIA_DIRS)
    if any(k not in MEDIA_DIRS for k in kinds):
        raise ToolError(f"kind must be one of {', '.join(MEDIA_DIRS)}")
    items = []
    base = _pkg_dir(e)
    for k in kinds:
        d = base / k
        # A symlinked media folder is skipped like any other symlink.
        if d.is_symlink() or not d.is_dir():
            continue
        for p in _walk_files(d):
            if p.suffix.lower() in IMAGE_TYPES and not _private(p.relative_to(base).as_posix()):
                items.append({"kind": k, "name": p.stem, "url": _site_url(p)})
    return {"slug": slug, "count": len(items), "items": items[:60],
            "capped": len(items) > 60}


def view_media(slug: str, path: str) -> dict:
    """One image from the package as an image block the model can see. Path is
    relative to systems/<slug>/ (as list_media reports it)."""
    e = _entry(slug)
    target = _bounded(e, path)
    media_type = IMAGE_TYPES.get(target.suffix.lower())
    if not target.is_file() or not media_type:
        raise ToolError(f"no image at {path}")
    data = target.read_bytes()
    if len(data) > IMAGE_CAP:
        shrunk = _shrink(target, media_type)
        if shrunk is None:
            raise ToolError(f"image is {len(data) // 1000} KB, over the {IMAGE_CAP // 1000} KB cap; "
                            "ask list_media for a thumbnail instead")
        data, media_type = shrunk
    return {"_image": {"media_type": media_type, "data": base64.b64encode(data).decode(),
                       "url": _site_url(target), "name": f"{slug}/{target.name}"}}


def _shrink(path: Path, media_type: str):
    """Downscale an oversized PNG/JPEG to the size a vision call wants, or None
    when Pillow is not installed (server/mcp.py can run a bare python3)."""
    try:
        import io
        from PIL import Image
    except ImportError:
        return None
    try:
        im = Image.open(path)
        im.thumbnail((1568, 1568))
        buf = io.BytesIO()
        im.convert("RGB").save(buf, "JPEG", quality=85)
        return buf.getvalue(), "image/jpeg"
    except Exception:
        return None


def handoff_prompt(slug: str, app_description: str | None = None) -> dict:
    """The apply-style prompt for a coding agent, the same shape the gallery's
    'Copy agent prompt' button writes."""
    e = _entry(slug)
    tokens = json.loads(_repo_file(e["tokens"]).read_text())
    groups = ", ".join(k for k in tokens if not k.startswith("$"))
    # Paths are repo-relative under $DESIGN_SYSTEMS_HOME, the variable the
    # design-systems plugin and AGENTS.md use to find a checkout, so the
    # prompt works on the agent's machine instead of naming the server's.
    root = HOME_VAR
    target = f" for {app_description}" if app_description else ""
    text = (f"Match the {e['name']} design style from my design-systems library{target}.\n"
            f"{root} is that library's checkout on this machine (set it, or replace it with the path).\n"
            f"1. Read {root}/{e['entry']} in full first. It says what was captured and what to distrust.\n"
            f"2. Take colour, type, spacing and radius values from {root}/{e['tokens']}. Its top-level "
            f"token groups are {groups}; the README says which group holds colour roles and which holds "
            f"scales. Never read a colour off a screenshot.\n"
            f"3. Use {root}/systems/{slug}/screenshots/ for layout and proportion only. "
            f"{root}/{e['styleGuide']} renders every token.\n"
            f"4. Borrow structure and proportions, not the product's logo, icons, illustrations or brand colours.\n"
            f"5. In your summary, name the package and the tokens you used.")
    return {"slug": slug, "prompt": text}


# ---------------------------------------------------------------- dispatch

# One schema serves both provider adapters: chat.py maps it onto Anthropic's
# `tools` and OpenAI's `functions` wire shapes.
SPECS = [
    {"name": "search_styles", "fn": search_styles,
     "description": "Rank styles by free-text words across the systems packages "
                    "(measured, preferred) and the refero snapshot (interpreted). "
                    "Returns slugs the page renders as cards.",
     "parameters": {"type": "object", "additionalProperties": False, "properties": {
         "query": {"type": "string", "description": "Free text: mood, layout, use, product words"},
         "store": {"type": "string", "enum": ["all", "systems", "refero"], "default": "all"},
         "platform": {"type": "string", "enum": ["web", "mobile", "desktop", "ios"],
                      "description": "The catalog's platform; ios is an alias for mobile"},
         "style": {"type": "string", "description": "Refero design_style label filter"},
         "limit": {"type": "integer", "minimum": 1, "maximum": 20, "default": 8}},
         "required": ["query"]}},
    {"name": "get_style", "fn": get_style,
     "description": "A style's distilled catalog entry: what it is for, its themes, "
                    "palette preview and which files hold the detail. Pass the store "
                    "a search_styles hit came from so a shared slug keeps its identity.",
     "parameters": {"type": "object", "additionalProperties": False, "properties": {
         "slug": {"type": "string"},
         "store": {"type": "string", "enum": ["systems", "refero"]}},
         "required": ["slug"]}},
    {"name": "get_tokens", "fn": get_tokens,
     "description": "Resolved token values for a systems package. Call without a "
                    "group to list groups, then with one for its flat map. A large "
                    "group comes back in pages: when truncated is true, call again "
                    "with offset=nextOffset.",
     "parameters": {"type": "object", "additionalProperties": False, "properties": {
         "slug": {"type": "string"},
         "group": {"type": "string", "description": "e.g. light, dark, base"},
         "offset": {"type": "integer", "minimum": 0, "default": 0,
                    "description": "Token index to start from (a previous page's nextOffset)"},
         "limit": {"type": "integer", "minimum": 1,
                   "description": "Most tokens to return; a page also stops before the result cap"}},
         "required": ["slug"]}},
    {"name": "read_doc", "fn": read_doc,
     "description": "Read a text file inside a package: its README (default), "
                    "components.md, patterns.md, tokens.json. Long files come back "
                    "in pages: when truncated is true, call again with offset=nextOffset.",
     "parameters": {"type": "object", "additionalProperties": False, "properties": {
         "slug": {"type": "string"},
         "path": {"type": "string", "description": "Package-relative path (a systems/<slug>/ or "
                                                   "/systems/<slug>/ path also works); default README.md"},
         "offset": {"type": "integer", "minimum": 0, "default": 0,
                    "description": "Character offset to start from (a previous page's nextOffset)"}},
         "required": ["slug"]}},
    {"name": "list_media", "fn": list_media,
     "description": "List a package's screenshots, component crops, icons and boards "
                    "with page-renderable URLs.",
     "parameters": {"type": "object", "additionalProperties": False, "properties": {
         "slug": {"type": "string"},
         "kind": {"type": "string", "enum": list(MEDIA_DIRS)}},
         "required": ["slug"]}},
    {"name": "view_media", "fn": view_media,
     "description": "See one image from a systems package (a screenshot or crop). "
                    "Use for questions tags cannot answer: density, layout, mood.",
     "parameters": {"type": "object", "additionalProperties": False, "properties": {
         "slug": {"type": "string"},
         "path": {"type": "string", "description": "Package-relative path (or a list_media url)"}},
         "required": ["slug", "path"]}},
    {"name": "handoff_prompt", "fn": handoff_prompt,
     "description": "The apply-style prompt that hands a chosen style to a coding "
                    "agent, for 'use this one'.",
     "parameters": {"type": "object", "additionalProperties": False, "properties": {
         "slug": {"type": "string"},
         "app_description": {"type": "string", "description": "What the style is being applied to"}},
         "required": ["slug"]}},
]

_BY_NAME = {s["name"]: s for s in SPECS}


def call(name: str, args: dict) -> dict:
    """Run one tool by name, capping the JSON the caller sends on. Every failure
    (missing arguments, bad types, tool errors) surfaces as a ToolError so one
    bad call can never take down a caller's loop."""
    spec = _BY_NAME.get(name)
    if not spec:
        raise ToolError(f"unknown tool '{name}'")
    props = spec["parameters"]["properties"]
    args = {k: v for k, v in (args or {}).items() if k in props}
    missing = [k for k in spec["parameters"].get("required", []) if k not in args]
    if missing:
        raise ToolError(f"{name} needs {', '.join(missing)}")
    try:
        result = spec["fn"](**args)
    except ToolError:
        raise
    except (TypeError, ValueError) as e:
        # A bad argument (int("x"), a wrong type): the message is about the
        # caller's own input.
        raise ToolError(f"{name} failed: {e}")
    except Exception as e:
        # Anything else (an OSError names an absolute path, sqlite errors name
        # the store) is logged here and reaches the caller, and through the
        # chat a third-party model, only as its type.
        print(f"library: {name}: {type(e).__name__}: {e}", file=sys.stderr)
        raise ToolError(f"{name} failed ({type(e).__name__})")
    if "_image" in result:
        return result
    size = _json_size(result)
    if size > RESULT_CAP:
        text = json.dumps(result, ensure_ascii=False, separators=(",", ":"))
        partial = text.encode("utf-8", "replace")[:RESULT_CAP].decode("utf-8", "ignore")
        result = {"truncated": True, "bytes": size, "partial": partial}
    return result
