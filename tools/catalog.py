#!/usr/bin/env python3
"""Check the catalog, and build the data the web app reads.

    python3 tools/catalog.py check            validate catalog.json against the packages
    python3 tools/catalog.py build            write web/data/data.json, thumbs/, refero/ and export/
    python3 tools/catalog.py find WORDS...    rank packages by name, use, tags and themes
    python3 tools/catalog.py export SLUG      print a package's tokens as CSS variables (or --format json)
    python3 tools/catalog.py export --file tokens.json --themes light,dark   the same for any token file
    python3 tools/catalog.py contrast FILE --theme light FG:BG[@3]...         WCAG AA check of token pairs
    python3 tools/catalog.py scan systems/SLUG --redact FILE                   find private text left in a package
    python3 tools/catalog.py design-md [SLUG...] [--check | --lint | --stdout]  write each package's DESIGN.md

Standard library only, except `design-md --lint`, which runs Google's DESIGN.md linter
through npx. Thumbnails use macOS `sips` or Pillow (see
tools/requirements-capture.txt); with neither, each one falls back to the
full-size image and `build` warns once. Run from anywhere.
"""
from __future__ import annotations

import argparse
import functools
import importlib.util
import json
import math
import os
import re
import shutil
import tempfile
import posixpath
import subprocess
import sys
import urllib.parse
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
# The generated data the Next.js app (web/) reads at request time: the catalog
# table, screenshot thumbnails, the refero JSON index and the token exports.
DATA = ROOT / "web" / "data"


def _thumbs() -> Path:
    # Derived at call time so a patched DATA (tests) moves the thumbnails too.
    return DATA / "thumbs"
IMAGE_EXT = {".png", ".jpg", ".jpeg", ".webp", ".gif"}
COMPONENT_EXT = IMAGE_EXT | {".svg"}
SWATCH_ROLES = ("page", "surface", "text", "muted", "accent", "border")
THUMB_WIDTH = 640

# Every package exposes these at its top level, whatever shape it has.
REQUIRED_FILES = ("README.md", "style-guide.html", "tools")
# The standard layout (docs/PACKAGE.md#layout). `make check` fails when a package lacks a part
# its catalog entry does not declare under `layoutGaps` with the reason, or has a top-level
# entry its README's file table does not describe. Each Health section repeats the gaps.
STANDARD_PARTS = ("README.md", "icon.png", "DESIGN.md", "tokens.json", "style-guide.html", "components.md",
                  "patterns.md", "components/", "icons/", "screenshots/", "raw/", "tools/")
REQUIRED_FIELDS = ("slug", "name", "url", "category", "platform", "goodFor", "shape", "captured",
                   "themes", "entry", "tokens", "styleGuide", "preview", "tags", "capture")
# What the product runs on. The scorecard grades a package against its platform's wording
# of each criterion (scorecard/criteria.json); web is the base wording, `doneWhen`.
PLATFORMS = ("web", "mobile", "desktop")
# The capture routes docs/CAPTURE.md describes: how the package's extraction ran.
CAPTURE_ROUTES = ("dom-snapshot", "iphone-mirroring", "electron-cdp", "web-inspector",
                  "native-pixels", "stylesheets", "headless", "public-web")


def atomic_write(path: Path, text: str) -> None:
    """Write text to path through a temp file and a rename, so a concurrent reader,
    or a deploy building while a generator runs, never sees a half-written file.
    The temp file is unique to the call: two writers of the same path cannot steal
    each other's rename. Every generator that writes a committed or generated file
    uses this."""
    fd, tmp = tempfile.mkstemp(dir=str(path.parent), prefix=path.name + ".", suffix=".tmp")
    try:
        # mkstemp creates the file 0600; os.replace would keep that mode, and a
        # web server reading the result as another user (the design-systems
        # deploy serves `site/` through a containerised nginx) would answer 403.
        os.fchmod(fd, 0o644)
        # UTF-8 whatever the locale: generated files hold non-ASCII text ("café").
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            f.write(text)
        os.replace(tmp, path)
    except BaseException:
        Path(tmp).unlink(missing_ok=True)
        raise


def load_catalog() -> dict:
    return json.loads((ROOT / "catalog.json").read_text(encoding="utf-8"))


# ---------------------------------------------------------------- generated files on a pull request


def _catalog_at(ref: str, root: Path) -> dict | None:
    try:
        raw = subprocess.run(["git", "show", f"{ref}:catalog.json"], cwd=root, check=True,
                             capture_output=True, text=True, encoding="utf-8").stdout
        found = json.loads(raw)
    except (OSError, subprocess.CalledProcessError, json.JSONDecodeError):
        return None
    rows = {s["slug"]: s for s in found.get("systems") or [] if isinstance(s, dict) and isinstance(s.get("slug"), str)}
    return rows or None


def pull_request_catalogs(root: Path | None = None) -> tuple[dict, dict] | None:
    """(base rows, branch rows), each keyed by slug, when GitHub is checking a pull
    request: the base branch's catalog and the pull request head's. None outside a pull
    request or when either cannot be read, and the caller then demands an exact match.
    The Check and Research app workflows fetch both refs."""
    base_ref, head = os.environ.get("GITHUB_BASE_REF"), os.environ.get("GITHUB_HEAD_SHA")
    if not base_ref or not head:
        return None
    base = _catalog_at(f"origin/{base_ref}", root or ROOT)
    branch = _catalog_at(head, root or ROOT)
    return (base, branch) if base and branch else None


def lagging_subset(named: set, head_rows: dict, root: Path | None = None) -> list[dict] | None:
    """The catalog rows a generated file may be derived from on a pull request, or None.

    GitHub checks the merge result, which can hold packages the file never saw: the ones
    this pull request adds, and the ones main gained after the branch started. The file
    may leave those out and nothing else. So `named`, the packages the committed file
    covers, must sit inside the merge's catalog (a removed package still listed fails)
    and hold every package that is on the base, on the branch and in the merge. The
    caller then derives the file from the returned rows, in catalog order, and demands
    an exact match, so a hand edit, a stale row or a wrong total still fails."""
    catalogs = pull_request_catalogs(root)
    if catalogs is None or not named:
        return None
    base, branch = catalogs
    if not named <= set(head_rows):
        return None
    if (set(head_rows) & set(base) & set(branch)) - named:
        return None
    return [row for slug, row in head_rows.items() if slug in named]


# ---------------------------------------------------------------- tokens


def flatten(tokens: dict) -> dict[str, object]:
    """Map dotted paths to raw values. Reads DTCG ($value) and Tokens Studio (value)."""
    flat: dict[str, object] = {}

    def walk(node, path):
        if not isinstance(node, dict):
            return
        if "$value" in node:
            flat[".".join(path)] = node["$value"]
            return
        if "value" in node and not isinstance(node["value"], dict):
            flat[".".join(path)] = node["value"]
            return
        for key, child in node.items():
            if not key.startswith("$"):
                walk(child, path + [key])

    walk(tokens, [])
    return flat


def _hex(value) -> str | None:
    """DTCG 2025 colour objects carry components, not a string."""
    if isinstance(value, dict) and "components" in value:
        if value.get("hex"):
            return value["hex"]
        r, g, b = (round(c * 255) for c in value["components"][:3])
        alpha = value.get("alpha", 1)
        return f"#{r:02x}{g:02x}{b:02x}" + ("" if alpha == 1 else f"{round(alpha * 255):02x}")
    return None


class Resolver:
    """Resolves {alias} references the way Tokens Studio does with every set active:
    first inside the token's own set, then in `core`, then from the root."""

    def __init__(self, tokens: dict):
        self.flat = flatten(tokens)

    def lookup(self, path: str, depth: int = 0):
        if path not in self.flat:
            return None
        return self._resolve(self.flat[path], path.split(".")[0], depth)

    def _resolve(self, value, set_name: str, depth: int):
        if depth > 12:
            return None
        as_hex = _hex(value)
        if as_hex:
            return as_hex
        if isinstance(value, list):
            return ", ".join(str(v) for v in value)
        if not isinstance(value, str):
            return value
        match = re.fullmatch(r"\{([^}]+)\}", value.strip())
        if not match:
            return value
        ref = match.group(1)
        for candidate in (f"{set_name}.{ref}", f"core.{ref}", ref):
            if candidate in self.flat:
                return self.lookup(candidate, depth + 1)
        return None


    def final(self, path: str, depth: int = 0, theme: str | None = None):
        """The raw value at `path` with every alias resolved, including aliases inside
        lists and objects (a shadow's colour). Keeps the structure lookup() flattens.
        `theme` is a set to try after the token's own one, for shared tokens in `core`
        that point at a theme's colours (Duolingo's lip shadows)."""
        if path not in self.flat:
            return None
        return self._deep(self.flat[path], path.split(".")[0], depth, theme)

    def _deep(self, value, set_name: str, depth: int, theme: str | None = None):
        if depth > 12:
            return None
        if isinstance(value, str):
            match = re.fullmatch(r"\{([^}]+)\}", value.strip())
            if not match:
                return value
            ref = match.group(1)
            sets = [set_name] + ([theme] if theme and theme != set_name else []) + ["core"]
            for candidate in [f"{s}.{ref}" for s in sets] + [ref]:
                if candidate in self.flat:
                    return self.final(candidate, depth + 1, theme)
            return None
        if isinstance(value, list):
            return [self._deep(v, set_name, depth, theme) for v in value]
        if isinstance(value, dict):
            return {k: self._deep(v, set_name, depth, theme) for k, v in value.items()}
        return value


def resolver_for(tokens_path: str) -> Resolver:
    """The Resolver of a tokens file, cached by the file's modification time and size, so a
    long-running server sees an edited file instead of the copy it read first."""
    st = (ROOT / tokens_path).stat()
    return _resolver(tokens_path, st.st_mtime_ns, st.st_size)


@functools.lru_cache(maxsize=256)
def _resolver(tokens_path: str, mtime_ns: int, size: int) -> Resolver:
    return Resolver(json.loads((ROOT / tokens_path).read_text(encoding="utf-8")))


resolver_for.cache_clear = _resolver.cache_clear


def swatches(system: dict) -> dict[str, list[dict]]:
    res = resolver_for(system["tokens"])
    out = {}
    for theme, roles in system["preview"].get("swatches", {}).items():
        out[theme] = [{"role": role, "token": path, "value": res.lookup(path)}
                      for role, path in roles.items()]
    return out


def fonts(system: dict) -> list[dict]:
    res = resolver_for(system["tokens"])
    out = []
    for path in system["preview"].get("fonts", []):
        stack = res.lookup(path)
        if isinstance(stack, str):
            first = stack.split(",")[0].strip().strip("'\"[] ")
            out.append({"token": path, "family": first, "stack": stack})
    return out


_CSS_IDENT = re.compile(r"-?[A-Za-z_][A-Za-z0-9_-]*")


def _font_name(name: str) -> str:
    name = name.strip()
    if name.startswith(("'", '"')) or name.startswith("var(") or all(_CSS_IDENT.fullmatch(w) for w in name.split()):
        return name
    return '"' + name.replace('"', '\\"') + '"'


def _shadow(layer) -> str | None:
    if not isinstance(layer, dict) or "offsetX" not in layer or "offsetY" not in layer:
        return None
    colour = _hex(layer.get("color")) or layer.get("color")
    # DTCG writes an inner shadow as inset: true; Tokens Studio as type: "innerShadow".
    parts = ["inset"] if layer.get("inset") or layer.get("type") == "innerShadow" else []
    parts += [str(_dimension(layer[k]) or layer[k]) for k in ("offsetX", "offsetY", "blur", "spread") if k in layer]
    if not isinstance(colour, str):
        return None
    return " ".join(parts + [colour])


def _dimension(value) -> str | None:
    """DTCG 2025 dimensions and durations are {value, unit} objects."""
    if isinstance(value, dict) and set(value) == {"value", "unit"}:
        return f"{value['value']}{value['unit']}"
    return None


def css_value(raw) -> str | None:
    """One CSS value for a fully resolved DTCG value, or None when there is none
    (typography objects, booleans, mixed lists)."""
    if isinstance(raw, bool) or raw is None:
        return None
    if isinstance(raw, (int, float)):
        return str(raw)
    if isinstance(raw, str):
        return raw
    as_hex = _hex(raw)
    if as_hex:
        return as_hex
    if _dimension(raw):
        return _dimension(raw)
    if isinstance(raw, dict):
        return _shadow(raw)
    if isinstance(raw, list) and raw:
        if len(raw) == 4 and all(isinstance(v, (int, float)) and not isinstance(v, bool) for v in raw):
            return "cubic-bezier(" + ", ".join(str(v) for v in raw) + ")"
        if all(isinstance(v, str) for v in raw):
            return ", ".join(_font_name(v) for v in raw)
        layers = [_shadow(v) for v in raw]
        if all(layers):
            return ", ".join(layers)
    return None


def _unresolved(raw) -> bool:
    """True when an alias somewhere in a resolved value pointed at nothing."""
    if raw is None:
        return True
    if isinstance(raw, dict):
        return any(_unresolved(v) for v in raw.values())
    if isinstance(raw, list):
        return any(_unresolved(v) for v in raw)
    return False


def _css_name(path: list[str]) -> str:
    return "--" + "-".join(re.sub(r"[^A-Za-z0-9_-]+", "-", part) for part in path).strip("-")


def export_tokens(tokens: dict, themes: list[str]) -> dict:
    """Resolve a token file into flat name -> value maps.

    Returns {"base": {...}, "themes": {theme: {...}}, "skipped": [paths],
    "unresolved": [paths]}. Sets named
    after a theme become per-theme maps with the set name dropped; `core` is merged
    into base with its name dropped; any other set (an audit package's `app`, `web`)
    goes into base under its own name. Shadows, cubic-bezier easings, font stacks and
    {value, unit} dimensions become CSS; values with no single CSS form (typography
    objects) are listed in `skipped`. A token with a `{reference}` that points at
    nothing, anywhere inside it, is listed in `unresolved` instead and never exported.

    A `core` token whose aliases only resolve inside a theme set (Duolingo's lip
    shadows point at each theme's colours) goes into each theme's map, unless that
    theme defines a token with the same CSS name itself. It must resolve in every theme;
    otherwise a light-only value on :root would leak into the other themes, so it
    is unresolved.
    """
    res = Resolver(tokens)
    theme_sets = [t for t in themes if t in tokens]
    out: dict = {"base": {}, "themes": {t: {} for t in theme_sets}, "skipped": [], "unresolved": []}
    # Names each theme defines itself, whether or not they resolve, so a shared value
    # never replaces one (`light.foo-bar` and `core.foo.bar` are both --foo-bar).
    own = {t: {_css_name(p.split(".")[1:]) for p in res.flat if p.split(".")[0] == t} for t in theme_sets}
    for path in res.flat:
        parts = path.split(".")
        raw = res.final(path)
        broken = _unresolved(raw)
        value = None if broken else css_value(raw)
        if value is None and parts[0] == "core" and theme_sets:
            per_raw = {t: res.final(path, theme=t) for t in theme_sets}
            broken = any(_unresolved(r) for r in per_raw.values())
            per_theme = {t: None if broken else css_value(r) for t, r in per_raw.items()}
            if not broken and all(v is not None for v in per_theme.values()):
                name = _css_name(parts[1:])
                for theme, themed in per_theme.items():
                    if name not in own[theme]:
                        out["themes"][theme][name] = str(themed)
                continue
        if broken:
            out["unresolved"].append(path)
            continue
        if value is None:
            out["skipped"].append(path)
            continue
        if parts[0] in theme_sets:
            out["themes"][parts[0]][_css_name(parts[1:])] = str(value)
        elif parts[0] == "core":
            out["base"][_css_name(parts[1:])] = str(value)
        else:
            out["base"][_css_name(parts)] = str(value)
    return out


def export_css(exported: dict) -> str:
    """The first theme shares :root with the base values; each other theme overrides
    under [data-theme="<name>"]."""
    themes = list(exported["themes"])
    root = dict(exported["base"])
    if themes:
        root.update(exported["themes"][themes[0]])
    block = lambda sel, vals: sel + " {\n" + "".join(f"  {k}: {v};\n" for k, v in vals.items()) + "}\n"
    css = block(":root", root)
    for theme in themes[1:]:
        css += "\n" + block(f'[data-theme="{theme}"]', exported["themes"][theme])
    if exported.get("unresolved"):
        css += (f"\n/* {len(exported['unresolved'])} tokens not exported because a reference points at nothing: "
                + ", ".join(exported["unresolved"]).replace("*/", "* /") + " */\n")
    if exported["skipped"]:
        css += f"\n/* {len(exported['skipped'])} composite tokens (typography objects and other values with no single CSS form) not exported */\n"
    return css


def parse_colour(value) -> tuple | None:
    """(r, g, b, alpha) with channels 0-255 and alpha 0-1, from hex or rgb()/rgba()."""
    if not isinstance(value, str):
        return None
    v = value.strip().lower()
    m = re.fullmatch(r"#([0-9a-f]{3,8})", v)
    if m:
        h = m.group(1)
        if len(h) in (3, 4):
            h = "".join(c * 2 for c in h)
        if len(h) not in (6, 8):
            return None
        return (int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16),
                int(h[6:8], 16) / 255 if len(h) == 8 else 1.0)
    m = re.fullmatch(r"rgba?\(([^)]+)\)", v)
    if not m:
        return None
    parts = [x for x in re.split(r"[,\s/]+", m.group(1)) if x]
    if len(parts) < 3:
        return None
    rgb = [float(x.rstrip("%")) * (2.55 if x.endswith("%") else 1) for x in parts[:3]]
    alpha = float(parts[3].rstrip("%")) / (100 if parts[3].endswith("%") else 1) if len(parts) > 3 else 1.0
    return (*rgb, alpha)


def _over(top: tuple, below: tuple) -> tuple:
    a = top[3]
    return tuple(top[i] * a + below[i] * (1 - a) for i in range(3)) + (1.0,)


def contrast_ratio(fg: tuple, bg: tuple) -> float:
    def lum(c):
        ch = [x / 255 for x in c[:3]]
        ch = [x / 12.92 if x <= 0.04045 else ((x + 0.055) / 1.055) ** 2.4 for x in ch]
        return 0.2126 * ch[0] + 0.7152 * ch[1] + 0.0722 * ch[2]
    hi, lo = sorted((lum(fg), lum(bg)), reverse=True)
    return (hi + 0.05) / (lo + 0.05)


def contrast(tokens: dict, theme: str, pairs: list[str], over: str | None = None) -> list[dict]:
    """Check FG:BG token pairs (paths inside `theme`) against WCAG 2.2 AA: 4.5:1, or 3:1
    with an @3 suffix. A translucent foreground is blended over its background; a
    translucent background is blended over `over` (a token path), and without one the
    pair is unchecked, which counts as a failure."""
    res = Resolver(tokens)
    look = lambda path: res.lookup(f"{theme}.{path}") if f"{theme}.{path}" in res.flat else res.lookup(path)
    backdrop = parse_colour(look(over)) if over else None
    results = []
    for pair in pairs:
        spec, _, level = pair.partition("@")
        need = 3.0 if level == "3" else 4.5
        fg_path, _, bg_path = spec.partition(":")
        fg_raw, bg_raw = look(fg_path), look(bg_path)
        fg, bg = parse_colour(fg_raw), parse_colour(bg_raw)
        row = {"fg": fg_path, "bg": bg_path, "fgValue": fg_raw, "bgValue": bg_raw, "need": need, "ratio": None}
        if not fg or not bg:
            row["status"] = "missing"
        elif bg[3] < 1 and not (backdrop and backdrop[3] == 1):
            row["status"] = "unchecked"
        else:
            solid_bg = _over(bg, backdrop) if bg[3] < 1 else bg
            ratio = contrast_ratio(_over(fg, solid_bg), solid_bg)
            # Judge the exact ratio; truncate for display so a fail never reads as 4.50.
            row["ratio"] = math.floor(ratio * 100) / 100
            row["status"] = "pass" if ratio >= need else "fail"
        results.append(row)
    return results


SCAN_SKIP_DIRS = {".git", "node_modules", "__pycache__"}


def is_text_file(f: Path) -> bool:
    """Whether `scan` reads a file: anything with no NUL byte in its first 8 KiB. An extension
    allowlist missed .tsx, .sh, .swift, .plist, extensionless files; images, fonts and archives
    all carry NUL bytes near the start."""
    with open(f, "rb") as fh:
        return b"\0" not in fh.read(8192)


# The credential-carrying URL parameters, one list for scan, the kit's unsnap.py and (a checked
# copy in) its snapshot.js. Built the way unsnap.py builds it.
SIGNED_PARAMS = ROOT / "tools" / "kit" / "capture" / "signed-in" / "signed-params.json"


def signed_url_pattern(spec: dict) -> re.Pattern:
    names = [re.escape(p) + r"[A-Za-z0-9-]*" for p in spec["prefixes"]] + [re.escape(p) for p in spec["params"]]
    return re.compile(r"(?:[?&#]|%3F|%26|%23)(?:amp;)?(" + "|".join(names) + r")(?:=|%3D)", re.I)


SIGNED_URL = signed_url_pattern(json.loads(SIGNED_PARAMS.read_text(encoding="utf-8")))


def input_error(message: str):
    """A bad input file: one `error:` line on stderr and exit 2, argparse's code for bad usage.
    Exit 1 stays what `scan` returns for found private text, so a caller can tell the two apart."""
    print(f"error: {message}", file=sys.stderr)
    raise SystemExit(2)


def read_json_object(path, what: str) -> dict:
    """The JSON object in `path` (`what` names the file's role in the error), or `input_error`
    when it is missing, unreadable, not valid JSON or not an object."""
    path = Path(path).expanduser()
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        input_error(f"{what} {path} not found")
    except (OSError, UnicodeDecodeError) as e:
        input_error(f"{what} {path} cannot be read: {getattr(e, 'strerror', None) or e}")
    except json.JSONDecodeError as e:
        input_error(f"{what} {path} is not valid JSON: {e.msg} (line {e.lineno}, column {e.colno})")
    if not isinstance(data, dict):
        input_error(f"{what} {path} has the wrong shape: expected a JSON object, got {type(data).__name__}")
    return data


def read_redaction(paths) -> dict:
    """One or more redaction files ({"replace": [[pattern, flags, replacement], ...],
    "email_allow": [...]}) merged, in order. The one reader for scan and redact_images.py.
    A missing, non-JSON or wrongly shaped file exits 2 with a one-line error naming it."""
    merged = {"replace": [], "email_allow": []}
    for path in ([paths] if isinstance(paths, (str, Path)) else paths or []):
        data = read_json_object(path, "redaction file")
        replace, allow = data.get("replace", []), data.get("email_allow", [])
        if not (isinstance(replace, list) and all(isinstance(r, list) and r and isinstance(r[0], str) for r in replace)):
            input_error(f"redaction file {path} has the wrong shape: \"replace\" must be a list of [pattern, flags, replacement] rows")
        if not (isinstance(allow, list) and all(isinstance(a, str) for a in allow)):
            input_error(f"redaction file {path} has the wrong shape: \"email_allow\" must be a list of strings")
        merged["replace"] += replace
        merged["email_allow"] += allow
    return merged


def redaction_patterns(redact: dict, ignorecase: bool = False) -> list[re.Pattern]:
    """The compiled `replace` patterns, one per row and in order: case-insensitive when the
    row's flags hold "i" or `ignorecase` (OCR reads case unreliably), and matched literally
    when a row is not a valid regex, so a bad row still guards instead of crashing."""
    out = []
    for row in redact.get("replace", []):
        pat = row[0]
        flags = re.I if ignorecase or (len(row) > 1 and "i" in str(row[1])) else 0
        try:
            out.append(re.compile(pat, flags))
        except re.error:
            out.append(re.compile(re.escape(pat), flags))
    return out


def scan(folder: Path, redact: dict) -> list[str]:
    """Every text file under `folder` (any extension or none; see is_text_file) checked against the redaction file's patterns (the
    [pattern, flags, replacement] triples unsnap.py uses) and for URL signing parameters.
    Returns "path:line: what" for each hit; the matched text itself is never printed. A
    missing folder, a folder with no text files, or a file that cannot be read is an error,
    so a check that looked at nothing never reads as clean."""
    if not folder.is_dir():
        raise SystemExit(f"scan: {folder} is not a folder")
    rules = [(rx, n) for n, rx in enumerate(redaction_patterns(redact), 1)]
    hits, checked = [], 0
    for f in sorted(folder.rglob("*")):
        if not f.is_file() or SCAN_SKIP_DIRS & set(f.relative_to(folder).parts):
            continue
        try:
            if not is_text_file(f):
                continue
            lines = f.read_text(errors="replace").splitlines()
        except OSError as e:
            hits.append(f"{f}: could not be read ({e.strerror})")
            continue
        checked += 1
        for i, line in enumerate(lines, 1):
            for rx, n in rules:
                if rx.search(line):
                    hits.append(f"{f}:{i}: redaction pattern {n}")
            if SIGNED_URL.search(line):
                hits.append(f"{f}:{i}: signed URL")
    if not checked:
        raise SystemExit(f"scan: no text files under {folder}; is it the right folder?")
    return hits


def find(words: list[str], catalog: dict | None = None) -> list[dict]:
    """Packages ranked by how many query words they match; a tag hit outranks a name hit,
    which outranks a goodFor/category/theme hit. Substring matching means "ios" can live
    inside a slug like acnestudios, so name and tag hits are scored separately. `catalog`
    is an already-parsed catalog.json (server/library.py passes its cached copy); omitted,
    the file is read."""
    catalog = load_catalog() if catalog is None else catalog
    ranked = []
    for s in catalog["systems"]:
        name = " ".join([s["slug"], s["name"]]).lower()
        tags = " ".join(s.get("tags", [])).lower()
        weak = " ".join([s["goodFor"], s["category"], catalog.get("categories", {}).get(s["category"], ""),
                         *s["themes"]]).lower()
        score = sum(3 if w in tags else 2 if w in name else 1 if w in weak else 0 for w in (w.lower() for w in words))
        if score or not words:
            ranked.append((score, s))
    ranked.sort(key=lambda x: (-x[0], x[1]["slug"]))
    return [{"slug": s["slug"], "name": s["name"], "score": score, "goodFor": s["goodFor"],
             "tags": s.get("tags", []), "themes": s["themes"], "entry": s["entry"],
             "tokens": s["tokens"], "styleGuide": s["styleGuide"]} for score, s in ranked]


# ---------------------------------------------------------------- DESIGN.md

# Google's DESIGN.md format (github.com/google-labs-code/design.md, docs/spec.md). Each
# package gets one, generated from its tokens file and README. It is a lossy, read-only
# export for tools that read DESIGN.md; the tokens file stays the source of truth.
DESIGN_MD_SPEC = "alpha"
DESIGN_MD_LINTER = "@google/design.md@0.4.0"
# Lint rules the export cannot satisfy without inventing data. docs/PACKAGE.md says why.
DESIGN_MD_ALLOWED = {"orphaned-tokens", "contrast-ratio"}
# DESIGN.md colour name -> catalog swatch role it is copied from.
DESIGN_MD_ROLES = (("primary", "accent"), ("neutral", "page"), ("surface", "surface"),
                   ("on-surface", "text"), ("on-surface-variant", "muted"), ("outline", "border"))
FONT_WEIGHTS = {"thin": 100, "hairline": 100, "extralight": 200, "ultralight": 200, "light": 300,
                "normal": 400, "regular": 400, "book": 400, "medium": 500, "semibold": 600,
                "demibold": 600, "bold": 700, "extrabold": 800, "ultrabold": 800, "black": 900,
                "heavy": 900}
# Polaris-style typography is one token per property, named <style>-<suffix>.
SPLIT_TYPE = (("font-family", "fontFamily"), ("font-size", "fontSize"), ("font-weight", "fontWeight"),
              ("font-line-height", "lineHeight"), ("font-letter-spacing", "letterSpacing"))
# The last word of a component token's name -> the DESIGN.md component property it fills.
# Tokens ending in any other word (hover, lip, rule, ring, and fill or label, which name an
# illustration's paint or a label's own background as often as a component's) are left out.
COMPONENT_PROPS = {"bg": "backgroundColor", "background": "backgroundColor", "face": "backgroundColor",
                   "surface": "backgroundColor", "text": "textColor", "fg": "textColor",
                   "foreground": "textColor",
                   "radius": "rounded", "padding": "padding", "height": "height", "width": "width",
                   "size": "size"}
# README sections copied into the body, by heading. First match wins; the rest stay in README.md.
README_SECTIONS = (("Colors", r"\bcolou?rs?\b"), ("Typography", r"\bfonts?\b|typograph"),
                   ("Layout", r"layout|geometry|spacing"),
                   ("Components", r"button|component|badge|patterns|screen to get right"),
                   ("Do's and Don'ts", r"\bdo'?s? and don|distrust|limits|gaps"))
FUNCTIONAL_COLOUR = re.compile(r"(rgba?|hsla?|hwb|oklch|oklab|lch|lab|color-mix)\(.+\)", re.I)


def _num(n: float) -> str:
    text = format(float(n), ".6f").rstrip("0").rstrip(".")
    return "0" if text in ("-0", "") else text


def md_name(rest: str) -> str:
    """A token path tail as a DESIGN.md token name: dots and anything unusual become hyphens."""
    return re.sub(r"[^A-Za-z0-9_-]+", "-", rest).strip("-")


def md_colour(value) -> str | None:
    if not isinstance(value, str):
        return None
    v = value.strip()
    if parse_colour(v) or v.lower() == "transparent" or FUNCTIONAL_COLOUR.fullmatch(v):
        return v
    return None


def md_dimension(value, percent_as_em: bool = False) -> str | None:
    """A px, rem or em string, the only units DESIGN.md allows. Bare numbers are px; a
    percentage becomes em only where that is what it means (letter spacing)."""
    value = _dimension(value) or value
    if isinstance(value, bool):
        return None
    if isinstance(value, (int, float)):
        return f"{_num(value)}px"
    if not isinstance(value, str):
        return None
    m = re.fullmatch(r"(-?\d*\.?\d+)(px|rem|em|%)?", value.strip())
    if not m:
        return None
    number, unit = float(m.group(1)), m.group(2)
    if unit == "%":
        return f"{_num(number / 100)}em" if percent_as_em else None
    return f"{_num(number)}{unit or 'px'}"


def md_line_height(value):
    """Unitless multipliers stay numbers; percentages become multipliers."""
    if isinstance(value, (int, float)) and not isinstance(value, bool):
        return value
    if isinstance(value, str):
        v = value.strip()
        if re.fullmatch(r"\d*\.?\d+", v):
            return float(v)
        if re.fullmatch(r"\d*\.?\d+%", v):
            return float(_num(float(v[:-1]) / 100))
    return md_dimension(value)


def md_font_weight(value) -> int | None:
    if isinstance(value, (int, float)) and not isinstance(value, bool):
        return int(value)
    if isinstance(value, str):
        v = value.strip().lower().replace("-", "").replace(" ", "")
        return int(float(v)) if re.fullmatch(r"\d+(\.\d+)?", v) else FONT_WEIGHTS.get(v)
    return None


def first_family(value) -> str | None:
    """The first family of a stack, which is what DESIGN.md's fontFamily names."""
    if isinstance(value, list):
        value = next((v for v in value if isinstance(v, str)), None)
    if not isinstance(value, str):
        return None
    name = value.split(",")[0].strip().strip("'\"").strip()
    return name or None


def md_typography(style: dict) -> dict:
    out = {}
    if (family := first_family(style.get("fontFamily"))):
        out["fontFamily"] = family
    if (size := md_dimension(style.get("fontSize"))):
        out["fontSize"] = size
    if (weight := md_font_weight(style.get("fontWeight"))) is not None:
        out["fontWeight"] = weight
    if (line := md_line_height(style.get("lineHeight"))) is not None:
        out["lineHeight"] = line
    if (spacing := md_dimension(style.get("letterSpacing"), percent_as_em=True)):
        out["letterSpacing"] = spacing
    return out


def design_md_theme(system: dict) -> str:
    """The theme the file actually exports. `themes` names the surfaces a
    capture saw, not the palettes the token file ships, so the preferred light
    theme can have no swatch set (Framer's /login is a captured light surface
    while tokens.json only carries `dark`): the label is the swatch set the
    export falls back to, not the preference. A catalog `defaultTheme` names the
    theme the product paints by default (Leonardo's app is dark; its only light
    surface is the docs site) and wins over the light preference."""
    swatch_sets = system.get("preview", {}).get("swatches", {})
    wanted = system.get("defaultTheme") or next((t for t in system["themes"] if t.startswith("light")),
                                                system["themes"][0])
    return wanted if wanted in swatch_sets else next(iter(swatch_sets), wanted)


def _roles(system: dict) -> dict:
    swatch_sets = system["preview"]["swatches"]
    return swatch_sets.get(design_md_theme(system)) or next(iter(swatch_sets.values()))


def design_md_sources(system: dict, res: Resolver) -> dict:
    """Token path prefixes for each front-matter group. The defaults fit the reference
    shape: the semantic set the catalog's swatches point at, and core's scales. A
    package's catalog entry overrides any of them under `designMd`."""
    has = lambda prefix: any(p.startswith(prefix) for p in res.flat)
    sources = {
        "colors": [_roles(system)["page"].split(".")[0] + "."],
        "typography": ["core.typography."],
        "rounded": ["core.radius."],
        "spacing": [next((p for p in ("core.spacing.", "core.space.") if has(p)), "core.spacing.")],
    }
    for group, prefixes in system.get("designMd", {}).items():
        sources[group] = [prefixes] if isinstance(prefixes, str) else list(prefixes)
    return sources


def _under(res: Resolver, prefixes: list[str]):
    """(name, path) for every token under the prefixes. The name is the path below the
    prefix's last whole group, so `light.space.space-` gives `space-100`, the token's own
    name, and two prefixes in one group never give the same name."""
    for prefix in prefixes:
        group = prefix if prefix.endswith(".") else prefix.rsplit(".", 1)[0] + "."
        for path in res.flat:
            if path.startswith(prefix):
                yield md_name(path[len(group):]), path


def design_md_tokens(system: dict, res: Resolver | None = None) -> dict:
    """The front matter as a dict, plus what the body needs: which token each role colour
    came from, the shadows, and every token that had no DESIGN.md form."""
    res = res or resolver_for(system["tokens"])
    sources = design_md_sources(system, res)
    roles = _roles(system)
    skipped: list[str] = []

    colors, role_from = {}, {}
    for name, role in DESIGN_MD_ROLES:
        value = md_colour(res.lookup(roles[role]))
        if value:
            colors[name], role_from[name] = value, roles[role]
    colour_paths = {}
    for name, path in _under(res, sources["colors"]):
        value = md_colour(res.lookup(path))
        if not value:
            skipped.append(path)
            continue
        if name in colors and colors[name] != value:
            name = f"{name}-token"
        colors.setdefault(name, value)
        colour_paths[path] = name

    styles: dict[str, dict] = {}
    for name, path in _under(res, sources["typography"]):
        value = res.final(path)
        if isinstance(value, dict):
            styles[name] = value
            continue
        for suffix, prop in SPLIT_TYPE:
            if name.endswith("-" + suffix):
                styles.setdefault(name[: -len(suffix) - 1], {})[prop] = value
                break
        else:
            skipped.append(path)
    typography = {name: t for name, style in styles.items() if (t := md_typography(style))}

    def scale(group, allow_number=False):
        out = {}
        for name, path in _under(res, sources[group]):
            raw = res.final(path)
            value = md_dimension(raw)
            if value is None and allow_number and isinstance(raw, (int, float)) and not isinstance(raw, bool):
                value = raw
            if value is None:
                skipped.append(path)
            else:
                out[name] = value
        return out

    rounded, spacing = scale("rounded"), scale("spacing", allow_number=True)

    components: dict[str, dict] = {}
    for path, name in colour_paths.items():
        words = name.split("-")
        if "component" not in path.split(".") or len(words) < 3 or words[-1] not in COMPONENT_PROPS:
            continue
        prop = COMPONENT_PROPS[words[-1]]
        if prop in ("backgroundColor", "textColor"):
            key = "-".join(words[1:-1] if words[0] == "component" else words[:-1])
            components.setdefault(key, {})[prop] = "{colors." + name + "}"
    for prefix in sources["colors"]:
        for path in res.flat:
            if not path.startswith(prefix + "component.") or path in colour_paths:
                continue
            words = md_name(path[len(prefix + "component."):]).split("-")
            prop, value = COMPONENT_PROPS.get(words[-1]), md_dimension(res.final(path))
            if len(words) > 1 and prop in ("rounded", "padding", "height", "width", "size") and value:
                components.setdefault("-".join(words[:-1]), {})[prop] = value

    sets = {p.split(".")[0] for p in sources["colors"]} | {"core"}
    theme_set = sources["colors"][0].split(".")[0]
    shadows = []
    for path in res.flat:
        parts = path.split(".")
        if parts[0] not in sets or not any(re.search(r"shadow|elevation", p, re.I) for p in parts[1:]):
            continue
        css = css_value(res.final(path, theme=theme_set))
        if css and css != "none" and not md_colour(css):
            shadows.append((path, css))

    theme_sets: list[str] = []
    for path in res.flat:
        set_name = path.split(".")[0]
        if set_name.startswith("$") or set_name == "core" or set_name in theme_sets:
            continue
        theme_sets.append(set_name)

    front = {"version": DESIGN_MD_SPEC, "name": system["name"], "description": system["goodFor"]}
    omitted = []
    for group, data in (("typography", typography), ("rounded", rounded), ("spacing", spacing),
                        ("components", components)):
        if not data:
            where = ("the colour set's `component` group" if group == "components"
                     else " or ".join(f"`{p.rstrip('.')}`" for p in sources[group]))
            omitted.append({"section": group,
                            "reason": f"{Path(system['tokens']).name} has no {group} tokens under {where}"})
    if omitted:
        front["omitted"] = omitted
    front.update({k: v for k, v in (("colors", colors), ("typography", typography), ("rounded", rounded),
                                    ("spacing", spacing), ("components", components)) if v})
    return {"front": front, "theme": design_md_theme(system), "sources": sources,
            "roleFrom": role_from, "shadows": shadows, "skipped": skipped,
            "sets": theme_sets}


def _yaml_key(key: str) -> str:
    plain = re.fullmatch(r"[A-Za-z_][A-Za-z0-9_-]*", key) and key.lower() not in (
        "true", "false", "null", "yes", "no", "on", "off", "y", "n")
    return key if plain else json.dumps(key)


def _yaml_scalar(value) -> str:
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, (int, float)):
        return _num(value)
    return json.dumps(str(value), ensure_ascii=False)


def to_yaml(data: dict, indent: int = 0) -> list[str]:
    """Just enough YAML for the front matter: nested maps, lists of scalars or flat maps,
    every string double-quoted."""
    pad, lines = "  " * indent, []
    for key, value in data.items():
        if isinstance(value, dict):
            lines.append(f"{pad}{_yaml_key(key)}:")
            lines += to_yaml(value, indent + 1)
        elif isinstance(value, list):
            lines.append(f"{pad}{_yaml_key(key)}:")
            for item in value:
                if isinstance(item, dict):
                    for i, (k, v) in enumerate(item.items()):
                        lines.append(f"{pad}{'  - ' if i == 0 else '    '}{_yaml_key(k)}: {_yaml_scalar(v)}")
                else:
                    lines.append(f"{pad}  - {_yaml_scalar(item)}")
        else:
            lines.append(f"{pad}{_yaml_key(key)}: {_yaml_scalar(value)}")
    return lines


def readme_parts(text: str) -> tuple[str, list[tuple[str, str]]]:
    """(intro, [(heading, body)]): the prose between the title and the first `##` with
    tables dropped, then every `##` section with its headings pushed one level down so
    none of them reads as a DESIGN.md section."""
    intro, sections, current, fenced = [], [], None, False
    for line in text.splitlines():
        if line.lstrip().startswith("```"):
            fenced = not fenced
        if not fenced and line.startswith("## "):
            current = (line[3:].strip(), [])
            sections.append(current)
            continue
        if not fenced and line.startswith("#"):
            if current is None:
                continue
            line = "#" + line
        if current is None:
            if not line.lstrip().startswith("|"):
                intro.append(line)
        else:
            current[1].append(line)
    tidy = lambda lines: re.sub(r"\n{3,}", "\n\n", "\n".join(lines)).strip()
    return tidy(intro), [(h, tidy(body)) for h, body in sections]


def _readme_for(section: str, parts: list[tuple[str, str]]) -> str:
    picked = []
    for heading, body in parts:
        home = next((name for name, rx in README_SECTIONS if re.search(rx, heading, re.I)), None)
        if home == section and body:
            picked.append(f"### {heading} (from README.md)\n\n{body}")
    return "\n\n".join(picked)


def _scale_line(values: dict) -> str:
    return ", ".join(f"`{k}` {v}" for k, v in values.items())


def design_md(system: dict) -> str:
    """The DESIGN.md for one package, deterministic so a regeneration that changes nothing
    proves the committed file is current."""
    data = design_md_tokens(system)
    front, theme, sources = data["front"], data["theme"], data["sources"]
    pkg = ROOT / "systems" / system["slug"]
    tokens_rel = Path(system["tokens"]).relative_to(f"systems/{system['slug']}").as_posix()
    intro, parts = readme_parts((pkg / "README.md").read_text(encoding="utf-8"))
    src = lambda group: " and ".join(f"`{p.rstrip('.')}`" for p in sources[group])
    # The themes the token file holds beyond the exported one — the catalog's
    # `themes` can name captured surfaces that never became a token set
    # (Framer's light /login shell), so keep only names that are token sets.
    token_sets = set(data["sets"])
    other_themes = [t for t in system["themes"] if t != theme and t in token_sets]

    body = [f"# {system['name']}", "",
            f"Generated from [{tokens_rel}]({tokens_rel}) and [README.md](README.md) by the "
            "design-systems catalog tool. Do not edit this file: change the tokens through the "
            "package's builders, then run `make design-md` at the repository root.", "",
            f"It follows the DESIGN.md spec, version {DESIGN_MD_SPEC}. That format has no themes, no "
            "per-value provenance and only px, em and rem units, so this file holds the "
            f"`{theme}` theme alone with every alias resolved. [{tokens_rel}]({tokens_rel}) is the "
            "source of truth: it records where each value was read"
            + (f", holds the {', '.join(f'`{t}`' for t in other_themes)} "
               f"theme{'s' if len(other_themes) > 1 else ''}" if other_themes else "")
            + f", and keeps the {len(data['skipped'])} tokens from these groups that DESIGN.md "
            "cannot hold (gradients, shadows, percentages, durations and other non-colour or "
            "non-px values)."]

    body += ["", "## Overview", "", f"Good for: {system['goodFor']}.", "",
             f"Captured {system['captured']}" + (f", {system['access']}" if system.get("access") else "")
             + f". Themes: {', '.join(system['themes'])}."]
    if intro:
        body += ["", intro]

    colors = front.get("colors", {})
    body += ["", "## Colors", "",
             f"The roles below are the catalog's swatches for the `{theme}` theme. The front matter "
             f"then lists every colour token under {src('colors')}, named by its path with dots "
             "turned into hyphens.", ""]
    body += [f"- **{name} ({colors[name]}):** `{data['roleFrom'][name]}`"
             for name, _ in DESIGN_MD_ROLES if name in data["roleFrom"]]
    if (readme := _readme_for("Colors", parts)):
        body += ["", readme]

    body += ["", "## Typography", ""]
    if front.get("typography"):
        families = sorted({s["fontFamily"] for s in front["typography"].values() if "fontFamily" in s})
        body.append(f"{len(front['typography'])} styles from {src('typography')}. `fontFamily` is the "
                    "first family of each stack; the full stacks, and properties DESIGN.md has no "
                    f"field for (text case, decoration), are in {tokens_rel}. Families: "
                    + ", ".join(families) + ".")
    else:
        body.append(f"No composite type styles in {tokens_rel}; the README text below names the faces and sizes.")
    if (readme := _readme_for("Typography", parts)):
        body += ["", readme]

    body += ["", "## Layout", "",
             f"Spacing from {src('spacing')}: {_scale_line(front['spacing'])}."
             if front.get("spacing") else f"No spacing scale in {tokens_rel}."]
    if (readme := _readme_for("Layout", parts)):
        body += ["", readme]

    body += ["", "## Elevation & Depth", ""]
    if data["shadows"]:
        body += ["Shadows, resolved to CSS:", "", "| Token | box-shadow |", "|---|---|"]
        body += [f"| `{path}` | `{css}` |" for path, css in data["shadows"]]
    else:
        body.append("No shadow tokens were captured; depth comes from surface colours and borders. "
                    "See [style-guide.html](style-guide.html).")

    body += ["", "## Shapes", "",
             f"Corner radii from {src('rounded')}: {_scale_line(front['rounded'])}."
             if front.get("rounded") else f"No radius scale in {tokens_rel}."]

    body += ["", "## Components", "",
             f"{len(front['components'])} components from the `component` tokens of the `{theme}` "
             "set, keeping only the properties DESIGN.md defines." if front.get("components")
             else "No component tokens map onto DESIGN.md's component properties."]
    guides = [f"[{n}]({n})" for n in ("components.md", "components") if (pkg / n).exists()]
    body += ["", "Measured states, crops and the full inventory: "
             + ", ".join(guides + ["[style-guide.html](style-guide.html)"]) + "."]
    if (readme := _readme_for("Components", parts)):
        body += ["", readme]

    body += ["", "## Do's and Don'ts", "",
             f"- Do take values from [{tokens_rel}]({tokens_rel}) when you need another theme, a "
             "value's source, or a token this file leaves out.",
             "- Do read [README.md](README.md) before relying on a value; it says what is known to be wrong.",
             "- Don't read colours off the screenshots; they are 256-colour PNGs.",
             "- Don't copy the product's logo, icons, illustrations or brand colours into something "
             "that ships. Borrow structure and proportions.",
             "- Don't edit this file; it is regenerated from the tokens."]
    if (readme := _readme_for("Do's and Don'ts", parts)):
        body += ["", readme]

    header = [f"# Generated by tools/catalog.py from {tokens_rel} and README.md. Do not edit.",
              f"# Source of truth: {tokens_rel}. DESIGN.md spec version {DESIGN_MD_SPEC}."]
    return "---\n" + "\n".join(header + to_yaml(front)) + "\n---\n\n" + "\n".join(body).rstrip() + "\n"


def design_md_path(system: dict) -> Path:
    return ROOT / "systems" / system["slug"] / "DESIGN.md"


# What a child process (npx, sips, tesseract, node) may see of this one's environment: enough to
# find programs, a home and a temp folder, locale and proxies. Never the provider keys or R2
# credentials refero_media loads from .env.
TOOL_ENV_KEYS = ("PATH", "HOME", "USER", "LOGNAME", "SHELL", "TMPDIR", "TEMP", "TMP", "LANG", "LC_ALL",
                 "LC_CTYPE", "TERM", "SYSTEMROOT", "COMSPEC", "PATHEXT", "APPDATA", "LOCALAPPDATA",
                 "npm_config_cache", "NODE_EXTRA_CA_CERTS", "SSL_CERT_FILE", "TESSDATA_PREFIX",
                 "HTTP_PROXY", "HTTPS_PROXY", "NO_PROXY", "http_proxy", "https_proxy", "no_proxy")


def tool_env(**extra: str) -> dict:
    """A minimal environment for a subprocess: TOOL_ENV_KEYS from this one, plus `extra`."""
    return {**{k: os.environ[k] for k in TOOL_ENV_KEYS if k in os.environ}, **extra}


def lint_design_md(paths: list[Path]) -> tuple[list[str], dict]:
    """Run the pinned DESIGN.md linter on each file from a throwaway directory, so nothing
    npm writes lands in the repository. Returns (problems, {file: {rule: count}}): errors,
    and warnings from rules outside DESIGN_MD_ALLOWED, are problems."""
    import tempfile
    if not shutil.which("npx"):
        raise SystemExit("lint needs npx (Node.js 18 or later)")
    problems, counts = [], {}
    with tempfile.TemporaryDirectory() as tmp:
        for path in paths:
            done = subprocess.run(["npx", "--yes", DESIGN_MD_LINTER, "lint", "--format", "json",
                                   str(path.resolve())], cwd=tmp, capture_output=True, text=True,
                                  encoding="utf-8", env=tool_env())
            rel = path.resolve().relative_to(ROOT).as_posix()
            try:
                report = json.loads(done.stdout)
            except json.JSONDecodeError:
                problems.append(f"{rel}: linter failed: {(done.stderr or done.stdout).strip()[:300]}")
                continue
            tally = counts.setdefault(rel, {})
            for f in report["findings"]:
                rule = f.get("rule", "parse")
                if f["severity"] == "info":
                    continue
                key = f"{rule} {f['severity']}"
                tally[key] = tally.get(key, 0) + 1
                if f["severity"] == "error" or rule not in DESIGN_MD_ALLOWED:
                    problems.append(f"{rel}: {f['severity']} {rule} {f.get('path', '')}: {f['message']}")
    return problems, counts


# ---------------------------------------------------------------- images


def _tags_for(rel: Path) -> list[str]:
    words = set(re.split(r"[-_./]", rel.as_posix().lower()))
    return sorted(w for w in ("light", "dark", "mobile") if w in words)


def list_images(system: dict, folder: str, exts: set[str]) -> list[dict]:
    base = ROOT / "systems" / system["slug"] / folder
    if not base.is_dir():
        return []
    skip = [f"{folder}/{p}" for p in system["preview"].get("exclude", [])]
    items = []
    for f in sorted(base.rglob("*")):
        if f.suffix.lower() not in exts or not f.is_file():
            continue
        rel = f.relative_to(ROOT / "systems" / system["slug"])
        if any(rel.as_posix().startswith(s.rstrip("/") + "/") for s in skip):
            continue
        items.append({"path": f.relative_to(ROOT).as_posix(), "name": f.stem,
                      "group": rel.parent.as_posix(), "tags": _tags_for(rel)})
    return items


def _thumb_name(path: str) -> Path:
    return _thumbs() / (path.replace("/", "__").rsplit(".", 1)[0] + ".jpg")


def _thumb_ok(dst: Path) -> bool:
    """A cached thumbnail is only kept when it looks complete: non-empty and ending in
    the JPEG end-of-image marker. A file cut off mid-write regenerates below instead
    of being kept by the mtime short-circuit forever."""
    try:
        if dst.stat().st_size < 4:
            return False
        with dst.open("rb") as f:
            f.seek(-2, os.SEEK_END)
            return f.read() == b"\xff\xd9"
    except OSError:
        return False


@functools.lru_cache(maxsize=1)
def _thumb_backend() -> str | None:
    """What makes thumbnails: macOS `sips`, Pillow, or neither. Probed once per run."""
    if shutil.which("sips"):
        return "sips"
    try:
        from PIL import Image  # noqa: F401
    except ImportError:
        return None
    return "pillow"


def _make_thumb(src: Path, dst: Path) -> bool:
    if dst.exists() and dst.stat().st_mtime >= src.stat().st_mtime and _thumb_ok(dst):
        return True
    backend = _thumb_backend()
    if backend == "sips":
        done = subprocess.run(["sips", "-s", "format", "jpeg", "-s", "formatOptions", "78",
                               "--resampleWidth", str(THUMB_WIDTH), str(src), "--out", str(dst)],
                              capture_output=True, env=tool_env())
        return done.returncode == 0 and dst.exists()
    if backend != "pillow":
        return False
    from PIL import Image
    with Image.open(src) as im:
        im = im.convert("RGB")
        if im.width > THUMB_WIDTH:
            im = im.resize((THUMB_WIDTH, round(im.height * THUMB_WIDTH / im.width)))
        im.save(dst, quality=78)
    return True


def attach_thumbs(images: list[dict]) -> None:
    thumbs_dir = _thumbs()
    thumbs_dir.mkdir(parents=True, exist_ok=True)

    # A cover is usually also in the screenshot list. Make each thumbnail once so
    # two workers never write the same file.
    paths = sorted({item["path"] for item in images})

    # Drop thumbnails whose source image is gone, so a removed screenshot does not
    # leave its thumb behind.
    keep = {_thumb_name(p).name for p in paths}
    for stale in thumbs_dir.glob("*.jpg"):
        if stale.name not in keep:
            stale.unlink()

    def one(path):
        dst = _thumb_name(path)
        # Paths are relative to web/, so the app turns them into /media/data/… URLs.
        return path, dst.relative_to(DATA.parent).as_posix() if _make_thumb(ROOT / path, dst) else path

    with ThreadPoolExecutor(max_workers=8) as pool:
        thumbs = dict(pool.map(one, paths))
    for item in images:
        item["thumb"] = thumbs[item["path"]]

    degraded = [p for p in paths if thumbs[p] == p]
    if degraded:
        backend = _thumb_backend()
        if backend is None:
            why = ("no `sips` on PATH and Pillow is not importable; "
                   "pip install -r tools/requirements-capture.txt")
        else:
            why = f"`{backend}` could not convert them"
        print(f"warning: {len(degraded)} of {len(paths)} gallery thumbnails "
              f"fell back to the full-size screenshot ({why})", file=sys.stderr)


# ---------------------------------------------------------------- commands


def palette_problems(slug: str, preview: dict, themes: list[str]) -> list[str]:
    """Every package shows at least one palette, and every palette names all six roles."""
    palettes = preview.get("swatches") or {}
    if not palettes:
        return [f"{slug}: preview.swatches is empty; add at least one theme's palette"]
    problems = []
    for theme, roles in palettes.items():
        if theme not in themes:
            problems.append(f"{slug}: swatch theme {theme} is not in themes")
        missing = [r for r in SWATCH_ROLES if r not in roles]
        extra = [r for r in roles if r not in SWATCH_ROLES]
        if missing:
            problems.append(f"{slug}: swatches.{theme} is missing roles {', '.join(missing)}")
        if extra:
            problems.append(f"{slug}: swatches.{theme} has unknown roles {', '.join(extra)}")
    return problems


def capture_problems(slug: str, capture) -> list[str]:
    """The capture block's required fields and their types. A missing capture is
    already reported as a missing REQUIRED_FIELD, so None returns no problems.
    version and pr stay optional: not every capture recorded a product version,
    and packages that predate the PR workflow name none. durationMin is required
    but may be null — a duration never recorded is unknown, not zero."""
    if capture is None:
        return []
    if not isinstance(capture, dict):
        return [f"{slug}: capture must be an object"]
    problems = []
    for field in ("harness", "model", "route", "durationMin"):
        if field not in capture:
            problems.append(f"{slug}: capture is missing {field}")
    for field in ("harness", "model", "version", "pr"):
        if field in capture and not isinstance(capture[field], str):
            problems.append(f"{slug}: capture.{field} must be a string")
    route = capture.get("route")
    if isinstance(route, str) and route not in CAPTURE_ROUTES:
        problems.append(f"{slug}: capture.route {route!r} is not one of {CAPTURE_ROUTES}")
    elif route is not None and not isinstance(route, str):
        problems.append(f"{slug}: capture.route must be a string")
    duration = capture.get("durationMin")
    if duration is not None and (isinstance(duration, bool)
                                 or not isinstance(duration, (int, float))):
        problems.append(f"{slug}: capture.durationMin must be a number or null")
    return problems


def check() -> list[str]:
    catalog = load_catalog()
    problems = []
    slugs = [s.get("slug") for s in catalog["systems"]]
    on_disk = sorted(p.name for p in (ROOT / "systems").iterdir() if p.is_dir())
    for missing in sorted(set(on_disk) - set(slugs)):
        problems.append(f"systems/{missing} has no catalog.json entry")
    for dup in sorted({s for s in slugs if s and slugs.count(s) > 1}):
        problems.append(f"{dup}: more than one catalog entry uses this slug")
    categories = catalog.get("categories", {})
    for s in catalog["systems"]:
        slug = s.get("slug", "?")
        for field in REQUIRED_FIELDS:
            if field not in s:
                problems.append(f"{slug}: missing field {field}")
        if "platform" in s and s["platform"] not in PLATFORMS:
            problems.append(f"{slug}: platform {s['platform']!r} is not one of {', '.join(PLATFORMS)}")
        if "category" in s and s["category"] not in categories:
            problems.append(f"{slug}: category {s['category']!r} is not in categories")
        if not (ROOT / "systems" / slug).is_dir():
            problems.append(f"{slug}: systems/{slug} does not exist")
            continue
        for name in REQUIRED_FILES:
            if not (ROOT / "systems" / slug / name).exists():
                problems.append(f"{slug}: systems/{slug}/{name} is missing")
        for field in ("entry", "tokens", "styleGuide"):
            if field in s and not (ROOT / s[field]).exists():
                problems.append(f"{slug}: {field} {s[field]} does not exist")
        extras = s.get("extras", [])
        if not isinstance(extras, list):
            problems.append(f"{slug}: extras must be a list of paths")
        else:
            for path in extras:
                if not isinstance(path, str):
                    problems.append(f"{slug}: extras path {path!r} is not a string")
                elif not (ROOT / path).exists():
                    problems.append(f"{slug}: extras path {path} does not exist")
        problems += capture_problems(slug, s.get("capture"))
        problems += layout_problems(s)
        if "preview" not in s or "tokens" not in s:
            continue
        cover = s["preview"].get("cover")
        if not cover or not (ROOT / cover).exists():
            problems.append(f"{slug}: preview.cover {cover} does not exist")
        icon = s["preview"].get("icon")
        # A package that declares icon.png under layoutGaps (the product publishes no icon)
        # has no icon to point at; layout_problems holds the declaration to the folder.
        icon_gap = isinstance(s.get("layoutGaps"), dict) and "icon.png" in s["layoutGaps"]
        if icon_gap and not icon:
            pass
        elif not icon or not (ROOT / icon).exists():
            problems.append(f"{slug}: preview.icon {icon} does not exist; run `python3 tools/fetch_icon.py {slug}`")
        problems += palette_problems(slug, s["preview"], s.get("themes", []))
        try:
            resolver_for(s["tokens"])
        except (OSError, ValueError) as e:     # missing (reported above) or not JSON: the token checks cannot run
            if (ROOT / s["tokens"]).exists():
                problems.append(f"{slug}: tokens {s['tokens']} cannot be read ({e.__class__.__name__}: {e})")
            continue
        for theme, roles in swatches(s).items():
            for sw in roles:
                if not isinstance(sw["value"], str):
                    problems.append(f"{slug}: swatch {theme}.{sw['role']} token {sw['token']} does not resolve")
        for path in s["preview"].get("fonts", []):
            if not isinstance(resolver_for(s["tokens"]).lookup(path), str):
                problems.append(f"{slug}: font token {path} does not resolve")
        problems += design_md_problems(s)
    manifest = ROOT / "webapps-manifest.json"
    if manifest.is_file():
        problems += manifest_problems(json.loads(manifest.read_text(encoding="utf-8")), catalog["systems"])
    return problems


@functools.lru_cache(maxsize=1)
def _coverage_module():
    spec = importlib.util.spec_from_file_location(
        "refero_coverage", Path(__file__).resolve().parent / "refero" / "coverage.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _root_domain(url_or_host: str | None) -> str:
    """tools/refero/coverage.py's matching rule, so the queue and the coverage file agree."""
    coverage = _coverage_module()
    return coverage.root_domain(coverage.host_of(url_or_host))


def manifest_problems(manifest: dict, systems: list[dict]) -> list[str]:
    """webapps-manifest.json against catalog.json, so the capture queue cannot drift:
    a captured app names a package the catalog has, an app that is not captured names
    none and has no package on its domain, and the totals match the rows."""
    problems = []
    apps = manifest.get("apps") if isinstance(manifest.get("apps"), list) else []
    slugs = {s.get("slug") for s in systems}
    domains: dict[str, list[str]] = {}
    for s in systems:
        domains.setdefault(_root_domain(s.get("url")), []).append(s.get("slug"))
    for app in apps:
        where = f"webapps-manifest.json {app.get('domain')}"
        package, status = app.get("package"), app.get("status")
        if status == "captured":
            if package not in {f"systems/{s}" for s in slugs}:
                problems.append(f"{where}: captured, but its package {package!r} is not a systems/<slug> in catalog.json")
            continue
        if package:
            problems.append(f"{where}: status {status!r} with package {package!r}; a package means captured")
        taken = domains.get(_root_domain(app.get("domain")))
        if taken:
            problems.append(f"{where}: status {status!r}, but catalog.json already has "
                            f"{', '.join('systems/' + s for s in taken)} on that domain; mark it captured")
    totals = manifest.get("totals") or {}
    if totals.get("apps") != len(apps):
        problems.append(f"webapps-manifest.json: totals.apps is {totals.get('apps')}, the file lists {len(apps)}")
    batches = max((a.get("batch") for a in apps if isinstance(a.get("batch"), int)), default=0)
    if totals.get("batches") != batches:
        problems.append(f"webapps-manifest.json: totals.batches is {totals.get('batches')}, the highest batch is {batches}")
    return problems


def file_table(readme: str) -> list[str]:
    """The rows of a README's file table: the first table whose header starts with a
    `File` or `Path` column. Other tables that happen to mention a path do not count."""
    lines = readme.splitlines()
    for i, line in enumerate(lines):
        if re.match(r"\|\s*(files?|paths?)\s*\|", line, re.I):
            rows = []
            for row in lines[i + 1:]:
                if not row.startswith("|"):
                    break
                rows.append(row)
            return rows
    return []


def git_ignored(paths: list[Path]) -> set[Path]:
    """The paths git ignores here (a package's local fonts/, say). Outside a git checkout,
    or without git, nothing counts as ignored. NUL-separated both ways: without `-z` git
    quotes a non-ASCII name in its answer, which then matches no path asked about."""
    if not paths:
        return set()
    try:
        out = subprocess.run(["git", "-C", str(ROOT), "check-ignore", "-z", "--stdin"], capture_output=True,
                             input=b"\0".join(os.fsencode(p) for p in paths), timeout=30)
    except (OSError, subprocess.SubprocessError):
        return set()
    if out.returncode not in (0, 1):
        return set()
    return {Path(os.fsdecode(p)) for p in out.stdout.split(b"\0") if p}


def layout_gaps(slug: str) -> tuple[list[str], list[str]]:
    """(the STANDARD_PARTS a package lacks, its top-level entries that no row of the
    README's file table links or names). A folder is written with a trailing slash. What
    git ignores (local fonts, capture leftovers) is not part of the package, so it neither
    fills a standard part nor needs a row."""
    folder = ROOT / "systems" / slug
    if not folder.is_dir():
        return list(STANDARD_PARTS), []
    ignored = git_ignored(sorted(folder.iterdir()))
    missing = []
    for part in STANDARD_PARTS:
        path = folder / part.rstrip("/")
        if not path.exists() or path.is_dir() != part.endswith("/") or path in ignored:
            missing.append(part)
    readme = folder / "README.md"
    rows = file_table(readme.read_text(encoding="utf-8")) if readme.is_file() else []
    unlisted = []
    for entry in sorted(folder.iterdir()):
        if entry.name.startswith(".") or entry.name == "README.md" or entry in ignored:
            continue
        named = re.compile(r"(\]\((?:\./)?|`)" + re.escape(entry.name) + r"[/)`#]")
        if not any(named.search(row) for row in rows):
            unlisted.append(entry.name + ("/" if entry.is_dir() else ""))
    return missing, unlisted


def layout_problems(system: dict) -> list[str]:
    """A missing standard part the entry does not declare under `layoutGaps`, a declared gap
    that is no longer missing, and a top-level entry with no row in the README's file table."""
    slug = system["slug"]
    missing, unlisted = layout_gaps(slug)
    declared = system.get("layoutGaps", {})
    if not isinstance(declared, dict) or not all(isinstance(v, str) and v for v in declared.values()):
        return [f"{slug}: layoutGaps must map each missing part to the reason it is missing"]
    problems = [f"{slug}: no {part}; add it, or declare it under layoutGaps with the reason"
                for part in missing if part not in declared]
    problems += [f"{slug}: layoutGaps declares {part}, which the package has or which is not a standard part"
                 for part in declared if part not in missing]
    problems += [f"{slug}: {entry} has no row in the README's file table" for entry in unlisted]
    return problems


def design_md_problems(system: dict) -> list[str]:
    """Every `designMd` source prefix matches a token, and the committed DESIGN.md is what
    the generator writes now. Inputs the generator needs (README, tokens file, themes, a
    complete palette) are checked first, and any other generation error is reported, so
    `check()` always returns every problem instead of stopping at a traceback."""
    slug = system["slug"]
    inputs = [ROOT / "systems" / slug / "README.md", ROOT / system.get("tokens", f"systems/{slug}/tokens.json")]
    missing = [p.relative_to(ROOT).as_posix() for p in inputs if not p.is_file()]
    if missing:
        return [f"{slug}: cannot generate DESIGN.md without {', '.join(missing)}"]
    if not system.get("themes") or palette_problems(slug, system.get("preview", {}), system["themes"]):
        return [f"{slug}: cannot generate DESIGN.md until themes and preview.swatches are complete"]
    res = resolver_for(system["tokens"])
    problems = []
    overrides = system.get("designMd", {})
    if not isinstance(overrides, dict):
        return [f"{slug}: designMd must be an object of token path prefixes"]
    for group, prefixes in overrides.items():
        if group not in ("colors", "typography", "rounded", "spacing"):
            problems.append(f"{slug}: designMd.{group} is not one of colors, typography, rounded, spacing")
            continue
        prefixes = [prefixes] if isinstance(prefixes, str) else prefixes
        if not isinstance(prefixes, list) or not prefixes or not all(isinstance(p, str) and p for p in prefixes):
            problems.append(f"{slug}: designMd.{group} must be a prefix string or a non-empty list of them")
            continue
        for prefix in prefixes:
            if not any(p.startswith(prefix) for p in res.flat):
                problems.append(f"{slug}: designMd.{group} prefix {prefix} matches no token")
    if problems:
        return problems
    path = design_md_path(system)
    if not path.exists():
        return [f"{slug}: systems/{slug}/DESIGN.md is missing; run `make design-md`"]
    try:
        fresh = design_md(system)
    except Exception as e:  # report, so the rest of the catalog is still checked
        return [f"{slug}: DESIGN.md generation failed: {type(e).__name__}: {e}"]
    if path.read_text(encoding="utf-8") != fresh:
        return [f"{slug}: systems/{slug}/DESIGN.md is out of date or hand-edited; run `make design-md`"]
    return []


def latest_scores() -> dict[str, dict]:
    """Each package's grade counts from the newest scorecard audit, plus its contrast
    result when that criterion is not met, for the gallery cards and detail pages."""
    import scorecard  # tools/ is on the path; imported here so `check` never needs it
    criteria, audits = scorecard.load()
    # Malformed audit data must fail here with its clean report, not as a KeyError
    # mid-build or, worse, silently wrong score cells.
    problems = scorecard.check(criteria, audits)
    if problems:
        sys.exit("scorecard data problems:\n  " + "\n  ".join(problems))
    audit = audits[-1]
    out = {}
    for s in audit["systems"]:
        counts = {g: 0 for g in scorecard.GRADES}
        grades = s["grades"] if isinstance(s.get("grades"), dict) else {}
        for g in grades.values():
            if isinstance(g, dict) and isinstance(g.get("grade"), str) and g["grade"] in counts:
                counts[g["grade"]] += 1
        f15 = grades.get("F15") or {}
        out[s["slug"]] = {**counts, "applicable": len(grades) - counts["na"], "date": audit["date"],
                          "contrast": None if not isinstance(f15, dict)
                          or f15.get("grade") in (None, "meets", "na")
                          or not isinstance(f15.get("evidence"), str)
                          else f15["evidence"].removeprefix("Script: ")}
    return out


ICON_LIMIT = 96  # icon files listed per package in data.json; the gallery says how many more exist


def list_icons(slug: str) -> dict:
    """The package's icon images under icons/, sorted, capped at ICON_LIMIT, with the total."""
    base = ROOT / "systems" / slug / "icons"
    files = sorted(f.relative_to(ROOT).as_posix() for f in base.rglob("*")
                   if f.is_file() and f.suffix.lower() in COMPONENT_EXT) if base.is_dir() else []
    return {"total": len(files), "items": files[:ICON_LIMIT]}


def section_data(system: dict) -> dict:
    """What the gallery's Typography, Spacing, Corner radius, Shadows and Assets sections
    show, taken from design_md_tokens so each matches the package's DESIGN.md: the same
    theme, names and values, in the same order. `omitted` gives the reason for each scale
    DESIGN.md leaves out, and `layoutGaps` the reason for each standard part a package lacks."""
    tokens = design_md_tokens(system)
    front = tokens["front"]
    type_styles = [{"name": name, "family": t.get("fontFamily"), "size": t.get("fontSize"),
                    "weight": t.get("fontWeight"), "lineHeight": t.get("lineHeight"),
                    "letterSpacing": t.get("letterSpacing")}
                   for name, t in front.get("typography", {}).items()]
    return {
        "tokenTheme": tokens["theme"],
        "typeStyles": type_styles,
        "radii": [{"name": k, "value": v} for k, v in front.get("rounded", {}).items()],
        "spacing": [{"name": k, "value": v} for k, v in front.get("spacing", {}).items()],
        "shadows": [{"token": path, "css": css} for path, css in tokens["shadows"]],
        "omitted": {o["section"]: o["reason"] for o in front.get("omitted", [])},
        "icons": list_icons(system["slug"]),
        "layoutGaps": dict(system.get("layoutGaps", {})),
    }


# ---------------------------------------------------------------- refero

# Extracted third-party styles under refero/<slug>/ (meta.json + design-system.json
# plus DESIGN.md, variables.css, theme.css, tokens.json). The app's Refero section
# reads what build_refero writes under web/data/refero/. The `local` media paths
# are where a separate fetch job puts each remote file; both sides are emitted so a
# card can fall back to the remote while its file is missing.

# The /refero-media/<kind>/<slug>.<ext> contract is shared with
# tools/refero/mirror_media.py (which downloads those files) through
# tools/refero/refero_media.py, imported by location so tools/refero/ stays off
# sys.path.
_spec = importlib.util.spec_from_file_location(
    "refero_media", Path(__file__).resolve().parent / "refero" / "refero_media.py")
refero_media = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(refero_media)

# Every remote media file sits under one CDN prefix; index.json carries it once
# under `cdn` and each remote field keeps only the suffix after it.
REFERO_CDN = "https://images.refero.design/styles/refero.design/"


def _cdn_rel(url) -> str | None:
    """A url under REFERO_CDN becomes its path suffix; anything else stays absolute."""
    if not url:
        return None
    return url[len(REFERO_CDN):] if url.startswith(REFERO_CDN) else url


def _refero_host(url) -> str | None:
    """Hostname of a style's source_url, without a leading www."""
    if not isinstance(url, str) or not url:
        return None
    host = urllib.parse.urlparse(url if "//" in url else f"//{url}").hostname
    return host.removeprefix("www.") if host else None


def _refero_asset(kind: str, slug: str, remote) -> dict | None:
    """One media pair: the file's eventual local path and the remote it is fetched from."""
    if not remote:
        return None
    return {"local": refero_media.local_path(kind, slug), "remote": remote}


# Entity media key -> (refero_media kind, meta.json field the remote URL lives
# in). `favicon` has no meta field: mirror_media.py fetches it from a favicon
# service host-side, and the emitted pair keeps only the mirrored local path,
# since a browser asking that service for a style's host would tell it which
# styles are browsed.
REFERO_MEDIA = {
    "shot": ("shots", "screenshot_url"),
    "poster": ("posters", "video_poster_url"),
    "video": ("videos", "video_url"),
    "detail": ("detail", "video_detail_url"),
    "detail_poster": ("detail-posters", "video_detail_poster_url"),
    "favicon": ("favicons", None),
}

# The entity doc's `ds` keeps only what the app's ReferoDetail renders; meta,
# theme, industry, northStar and similar are lifted out or duplicated
# elsewhere, and components/imagery/layout/customSections/surfaces are shipped
# nowhere.
REFERO_DS_KEYS = ("description", "colors", "typography", "typeScale", "spacing",
                  "elevation", "elevationPhilosophy", "dos", "donts")


def load_refero() -> list[tuple[Path, dict, dict]]:
    """(folder, meta, design-system) for every refero/<slug>/ that has meta.json and
    design-system.json. A folder missing either, or one that does not parse, is
    skipped with a warning rather than failing the build."""
    base = ROOT / "refero"
    styles = []
    if not base.is_dir():
        return styles
    for folder in sorted(base.iterdir()):
        if not folder.is_dir() or folder.name.startswith("."):  # .work and the like are not styles
            continue
        meta_path, ds_path = folder / "meta.json", folder / "design-system.json"
        if not meta_path.is_file() or not ds_path.is_file():
            print(f"warning: skipping refero/{folder.name}: needs meta.json and design-system.json",
                  file=sys.stderr)
            continue
        try:
            meta = json.loads(meta_path.read_text(encoding="utf-8"))
            ds = json.loads(ds_path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as e:
            print(f"warning: skipping refero/{folder.name}: {e}", file=sys.stderr)
            continue
        styles.append((folder, meta, ds))
    return styles


def refero_card(slug: str, meta: dict, ds: dict) -> dict:
    """One row of refero/index.json. The card prefers the video poster and falls back
    to the screenshot; the remote card also tries the design-system's thumbnail.
    `card` keeps one bit ("p" poster, "s" shot); the gallery builds local media paths
    from the slug and joins remote suffixes onto the index's `cdn` prefix."""
    poster, shot = meta.get("video_poster_url"), meta.get("screenshot_url")
    ds_meta = ds.get("meta") if isinstance(ds.get("meta"), dict) else {}
    return {"slug": slug, "name": meta.get("name"), "tagline": meta.get("tagline"),
            "theme": meta.get("theme") or ds.get("theme"), "industry": ds.get("industry"),
            "type": meta.get("product_type"), "style": meta.get("design_style"),
            "tags": meta.get("tags") or [],
            "src": _refero_host(meta.get("source_url")),
            "card": "p" if poster else "s" if shot else None,
            "cardRemote": _cdn_rel(poster or ds_meta.get("thumbnailUrl") or shot),
            "video": bool(meta.get("video_url")),
            "videoRemote": _cdn_rel(meta.get("video_url"))}


def refero_entry(folder: Path, meta: dict, ds: dict, slug_of: dict) -> dict:
    """The JSON written to refero/<slug>.json: the meta fields, local+remote media
    pairs (null where meta.json has no remote for one yet), the docs files' text, the
    design-system keys the page renders (REFERO_DS_KEYS), and `similar` with each
    business name resolved to a refero slug where one matches."""
    slug = meta.get("slug") or folder.name
    text = lambda name: (folder / name).read_text(encoding="utf-8") if (folder / name).is_file() else None
    media = {
        key: _refero_asset(kind, slug, meta.get(field))
        for key, (kind, field) in REFERO_MEDIA.items() if field is not None
    }
    # The favicon exists in the mirror only when its source host does.
    media["favicon"] = ({"local": refero_media.local_path("favicons", slug), "remote": None}
                        if refero_media.favicon_url(meta.get("source_url")) else None)
    similar = [{"slug": slug_of.get(str(s.get("business") or "").lower()),
                "name": s.get("business"), "why": s.get("why")}
               for s in ds.get("similar") or [] if isinstance(s, dict)]
    return {"slug": slug, "name": meta.get("name"), "tagline": meta.get("tagline"),
            "theme": meta.get("theme") or ds.get("theme"), "industry": ds.get("industry"),
            "type": meta.get("product_type"), "style": meta.get("design_style"),
            "source_url": meta.get("source_url"), "page_url": meta.get("page_url"),
            "media": media,
            "docs": {"design_md": text("DESIGN.md"), "variables_css": text("variables.css"),
                     "theme_css": text("theme.css"), "tokens_json": text("tokens.json")},
            "ds": {k: ds[k] for k in REFERO_DS_KEYS if k in ds},
            "similar": similar,
            "mediaBase": refero_media.media_base()}


def build_refero() -> Path | None:
    """Write web/data/refero/index.json and one style/<slug>.json per style.
    Entities sit under style/ so no slug can collide with the index (a real
    style is slugged `index`). Returns the index path, or None when there is no
    refero/ folder; an empty or unparseable one clears the generated output."""
    styles = load_refero()
    if not (ROOT / "refero").is_dir():
        return None
    out_dir = DATA / "refero"
    ent_dir = out_dir / "style"
    ent_dir.mkdir(parents=True, exist_ok=True)
    name_count: dict[str, int] = {}
    for _, meta, _ in styles:
        if meta.get("name"):
            key = str(meta["name"]).lower()
            name_count[key] = name_count.get(key, 0) + 1
    # A `similar` business name resolves to a slug only when exactly one style
    # carries it. Names several styles share (Apple x6) would otherwise keep
    # the last alphabetical match, a confident wrong link; the gallery renders
    # a `slug: null` entry as an unlinked card with the name and why.
    slug_of = {str(meta["name"]).lower(): meta.get("slug") or folder.name
               for folder, meta, _ in styles
               if meta.get("name") and name_count[str(meta["name"]).lower()] == 1}
    ambiguous = {n for n, count in name_count.items() if count > 1}
    if ambiguous:
        dropped = sum(str(s.get("business") or "").lower() in ambiguous
                      for _, _, ds in styles for s in ds.get("similar") or []
                      if isinstance(s, dict))
        print(f"refero: {dropped} similar links left unlinked; "
              f"{len(ambiguous)} business names are not unique", file=sys.stderr)
    index = []
    written = set()
    # Each slug becomes a file name: refuse a path-like one before writing anything.
    for folder, meta, _ in styles:
        slug = meta.get("slug") or folder.name
        if not REFERO_SLUG.fullmatch(str(slug)):
            raise SystemExit(f"refero: {folder.name}: slug {slug!r} is not lowercase letters, digits and hyphens")
    for folder, meta, ds in styles:
        slug = meta.get("slug") or folder.name
        atomic_write(ent_dir / f"{slug}.json",
                     json.dumps(refero_entry(folder, meta, ds, slug_of), separators=(",", ":")))
        written.add(slug)
        index.append(refero_card(slug, meta, ds))
    # Prune after writing, not before: a style deleted from refero/ loses its page,
    # while a crash mid-build leaves retained styles' entities in place.
    for stale in ent_dir.glob("*.json"):
        if stale.stem not in written:
            stale.unlink()
    index.sort(key=lambda s: str(s["name"] or "").lower())
    out = out_dir / "index.json"
    atomic_write(out, json.dumps({"version": 2, "cdn": REFERO_CDN,
                                  "mediaBase": refero_media.media_base(),
                                  "styles": index},
                                 separators=(",", ":")))
    return out


REFERO_SLUG = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*")


def build() -> Path:
    problems = check()
    if problems:
        sys.exit("catalog check failed:\n  " + "\n  ".join(problems))
    catalog = load_catalog()
    scores = latest_scores()
    systems = []
    all_shots = []
    for s in catalog["systems"]:
        shots = list_images(s, "screenshots", IMAGE_EXT)
        cover = {"path": s["preview"]["cover"]}
        all_shots += shots + [cover]
        systems.append({
            **{k: s[k] for k in ("slug", "name", "url", "category", "goodFor", "shape", "captured",
                                 "themes", "tags", "entry", "tokens", "styleGuide")},
            "access": s.get("access", ""),
            "capture": s.get("capture"),
            "widths": s.get("widths", []),
            "notes": s.get("notes", ""),
            "dir": f"systems/{s['slug']}",
            "cover": cover,
            "icon": s["preview"].get("icon"),
            "swatches": swatches(s),
            "tokenGroups": [k for k in json.loads((ROOT / s["tokens"]).read_text(encoding="utf-8"))
                            if not k.startswith("$")],
            "fonts": fonts(s),
            "score": scores.get(s["slug"]),
            "screenshots": shots,
            "components": list_images(s, "components", COMPONENT_EXT),
            "docs": sorted(p.relative_to(ROOT).as_posix()
                           for p in (ROOT / "systems" / s["slug"]).glob("*.md")),
            **section_data(s),
        })
    attach_thumbs(all_shots)
    build_exports(systems)
    out = DATA / "data.json"
    # No absolute checkout path: nothing reads one, and web/data is served under /media/data/.
    atomic_write(out, json.dumps({"categories": catalog.get("categories", {}),
                                  "systems": systems},
                                 separators=(",", ":")))
    build_refero()
    return out


def build_exports(systems: list[dict]) -> None:
    """The schema extractor, materialised for the app: export/<slug>.css and
    export/<slug>.json hold the same text `catalog.py export` prints (custom
    properties, and the flat maps behind them), so the Overview can copy them.
    Files a deleted package left behind are pruned."""
    out_dir = DATA / "export"
    out_dir.mkdir(parents=True, exist_ok=True)
    written = set()
    for s in systems:
        tokens = json.loads((ROOT / s["tokens"]).read_text(encoding="utf-8"))
        exported = export_tokens(tokens, s["themes"])
        atomic_write(out_dir / f"{s['slug']}.css", export_css(exported) + "\n")
        atomic_write(out_dir / f"{s['slug']}.json", json.dumps(exported, indent=2) + "\n")
        written.add(s["slug"])
    for stale in out_dir.iterdir():
        if stale.stem not in written:
            stale.unlink()


# Repository paths the media route answers from the checkout: the gallery's
# screenshots and package files, and the files docs link to. They are never
# part of the docs site. server/library.py bounds package file reads
# through repo_file the same way web/lib/repo.ts does. /example/ holds only
# gitignored clones, so it is not served.
REPO_PATHS = ("/systems/", "/tools/", "/catalog.json", "/README.md")


def _ignored_or_private(target: Path) -> bool:
    """Whether repo_file must refuse a resolved file: anything in a fonts/ folder (proprietary
    fonts a style guide may use locally) or anything git ignores (capture dumps/, out/, local
    fonts). Inside a git checkout a git failure counts as ignored, so the guard fails closed."""
    root = ROOT.resolve()
    if "fonts" in target.relative_to(root).parts:
        return True
    if not (ROOT / ".git").exists():
        return False
    try:
        out = subprocess.run(["git", "-C", str(root), "check-ignore", "-q", "--", str(target)],
                             capture_output=True, timeout=30)
    except (OSError, subprocess.SubprocessError):
        return True
    return out.returncode != 1          # 0: ignored; 1: not ignored; anything else: git failed


def repo_file(url_path: str) -> Path | None:
    """The checkout file a request under REPO_PATHS maps to, or None.

    The path is unquoted and normalised before the prefix check, so `..` segments
    (plain or percent-encoded) can never climb out of the allowed folders, and the
    resolved file must still sit inside the checkout, so a symlink cannot either. A
    git-ignored file or anything in a fonts/ folder is refused (_ignored_or_private)."""
    clean = urllib.parse.unquote(url_path.split("?", 1)[0].split("#", 1)[0])
    norm = posixpath.normpath(clean)
    if not any(norm == p.rstrip("/") or norm.startswith(p) for p in REPO_PATHS):
        return None
    root = ROOT.resolve()
    target = (root / norm.lstrip("/")).resolve()
    allowed = [(root / p.strip("/")).resolve() for p in REPO_PATHS]
    if not any(target == a or a in target.parents for a in allowed):
        return None
    if _ignored_or_private(target):
        return None
    return target


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="cmd", required=True)
    sub.add_parser("check")
    sub.add_parser("build")
    p_find = sub.add_parser("find")
    p_find.add_argument("words", nargs="*")
    p_find.add_argument("--json", action="store_true")
    p_export = sub.add_parser("export")
    p_export.add_argument("slug", nargs="?")
    p_export.add_argument("--file", type=Path, help="export this token file instead of a package's")
    p_export.add_argument("--themes", default="light,dark",
                          help="with --file: comma-separated theme set names, first goes on :root")
    p_scan = sub.add_parser("scan", help="find private text left in a package")
    p_scan.add_argument("folder", type=Path)
    p_scan.add_argument("--redact", type=Path, required=True, help="the capture's redaction file")
    p_contrast = sub.add_parser("contrast", help="WCAG AA check of FG:BG token pairs")
    p_contrast.add_argument("file", type=Path)
    p_contrast.add_argument("--theme", required=True)
    p_contrast.add_argument("--over", help="token a translucent background sits on, e.g. background.page")
    p_contrast.add_argument("pairs", nargs="+", help="FG:BG paths inside the theme; add @3 for 3:1")
    p_export.add_argument("--format", choices=("css", "json"), default="css")
    p_md = sub.add_parser("design-md", help="write each package's DESIGN.md from its tokens and README")
    p_md.add_argument("slugs", nargs="*", help="packages to write (default: all)")
    mode = p_md.add_mutually_exclusive_group()
    mode.add_argument("--check", action="store_true", help="fail if a committed DESIGN.md is stale")
    mode.add_argument("--lint", action="store_true", help=f"run {DESIGN_MD_LINTER} on the committed files")
    mode.add_argument("--stdout", action="store_true", help="print instead of writing")
    args = parser.parse_args()
    if args.cmd == "check":
        problems = check()
        print("catalog ok" if not problems else "\n".join(problems))
        sys.exit(1 if problems else 0)
    if args.cmd == "build":
        print(f"built {build().relative_to(ROOT)}")
    if args.cmd == "find":
        hits = find(args.words)
        if args.json:
            print(json.dumps(hits, indent=2))
        for h in [] if args.json else hits:
            print(f"{h['slug']:<15} {h['score']}  {h['goodFor']}\n{'':<18}tags: {', '.join(h['tags'])}"
                  f" | themes: {', '.join(h['themes'])} | {h['entry']}")
        if not hits:
            sys.exit("no package matches")
    if args.cmd == "scan":
        hits = scan(args.folder, read_redaction(args.redact))
        print("\n".join(hits) if hits else f"no private text found in {args.folder}")
        sys.exit(1 if hits else 0)
    if args.cmd == "contrast":
        rows = contrast(json.loads(args.file.read_text(encoding="utf-8")), args.theme, args.pairs, args.over)
        for r in rows:
            ratio = f"{r['ratio']:5.2f}:1" if r["ratio"] is not None else "   -   "
            note = {"missing": "a token does not resolve to a colour",
                    "unchecked": "background is translucent; pass --over with what it sits on"}.get(r["status"], "")
            print(f"{r['status'].upper():<9} {ratio} (needs {r['need']}:1)  {r['fg']} {r['fgValue']} on "
                  f"{r['bg']} {r['bgValue']}  {note}".rstrip())
        sys.exit(0 if all(r["status"] == "pass" for r in rows) else 1)
    if args.cmd == "design-md":
        systems = load_catalog()["systems"]
        unknown = set(args.slugs) - {s["slug"] for s in systems}
        if unknown:
            sys.exit(f"no package {', '.join(sorted(unknown))}; run `find` to list them")
        systems = [s for s in systems if not args.slugs or s["slug"] in args.slugs]
        if args.check:
            problems = [p for s in systems for p in design_md_problems(s)]
            print("\n".join(problems) if problems else f"{len(systems)} DESIGN.md files are current")
            sys.exit(1 if problems else 0)
        if args.lint:
            problems, counts = lint_design_md([design_md_path(s) for s in systems])
            for rel, tally in counts.items():
                found = ", ".join(f"{n} {rule}" for rule, n in sorted(tally.items())) or "clean"
                print(f"{rel}: {found}")
            print("\n".join(problems) if problems else
                  f"lint ok: no errors, and warnings only from {', '.join(sorted(DESIGN_MD_ALLOWED))}")
            sys.exit(1 if problems else 0)
        for s in systems:
            text = design_md(s)
            if args.stdout:
                print(text)
            else:
                atomic_write(design_md_path(s), text)
                print(f"wrote {design_md_path(s).relative_to(ROOT)}")
    if args.cmd == "export":
        if not args.file and not args.slug:
            sys.exit("export needs a package slug or --file")
        if args.file:
            tokens_path, themes = args.file, [t for t in args.themes.split(",") if t]
        else:
            system = next((s for s in load_catalog()["systems"] if s["slug"] == args.slug), None)
            if not system:
                sys.exit(f"no package {args.slug}; run `find` to list them, or pass --file")
            tokens_path, themes = ROOT / system["tokens"], system["themes"]
        exported = export_tokens(json.loads(Path(tokens_path).read_text(encoding="utf-8")), themes)
        print(export_css(exported) if args.format == "css" else json.dumps(exported, indent=2))
        if exported["unresolved"]:
            print(f"warning: {len(exported['unresolved'])} tokens have a reference that points at nothing "
                  f"and were not exported: {', '.join(exported['unresolved'])}", file=sys.stderr)


if __name__ == "__main__":
    main()
