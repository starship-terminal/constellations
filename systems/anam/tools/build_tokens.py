#!/usr/bin/env python3
"""Build tokens.json (W3C DTCG, Tokens Studio multi-set layout) from the raw captures.

Sources, read from anam.ai on 2026-11-09, CSS dump refreshed 2026-11-21:
  raw/css-vars.json          every custom property the public pages declare, by stylesheet,
                             selector and media condition, sorted by owner
                             (tools/capture/vars.mjs):
                               framer    the marketing pages' --token-* names on `body`
                               anam      the Next.js sub-apps' (:root) set on /pricing,
                                         /get-demo and /tools
                               mintlify  the docs' Tailwind v4 theme vars and RGB-triplet
                                         palette on :root
  raw/component-tokens.json  the token tree: each leaf either names a variable ("var" + "owner")
                             whose value is read from css-vars.json, or carries a measured value
                             and the measurement it came from ("source")
Every token carries $extensions.source: "css-var <name> (<selector>)" or the measurement.

anam.ai is three public surfaces. The marketing pages are Framer: one orange accent and a pair of
warm tokens on `body`, everything else painted directly. The app pages (/pricing, /get-demo,
/tools) are Next.js and declare a small semantic set on :root. The docs are Mintlify: a warm-stone
gray ramp and RGB triplets on :root, with a real dark theme under `.dark` (the only surface that
has one). Light decls are the media=None blocks on :root/body; dark decls are the `.dark`-scoped
ones, falling back to the shared ramp. A leaf's "var" resolves inside its owner's declarations for
the set's theme, following var() chains; RGB triplets like "255 98 0" normalise to hex.

Deterministic: same inputs, byte-identical output. Edit the raw inputs, never tokens.json.
"""
import json, pathlib, re, sys

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
V = json.loads((RAW / "css-vars.json").read_text())
SPEC = json.loads((RAW / "component-tokens.json").read_text())

OWNERS = ("framer", "anam", "mintlify")


def is_dark(d):
    sel = d["selector"]
    return ".dark" in sel or "prefers-color-scheme: dark" in (d["media"] or "")


# The preferred declaration of each name per owner and theme. Root-level blocks win
# (framer's `body`, the apps' and docs' `:root`), then any other selector; an arbitrary-property
# utility (`.[--x:y]`) ranks below them all — it is a one-off override on one element, not a
# theme token. Narrow media queries rank below the default block.
RANK = {"body": 0, ":root": 0, "html": 0, ":root, :host": 1, ".dark": 0, ".dark :root": 1, "html.dark": 1}
DECL = {o: {"light": {}, "dark": {}} for o in OWNERS}
for d in V["decls"]:
    o = d["owner"]
    if o not in OWNERS:
        continue
    theme = "dark" if is_dark(d) else "light"
    media = d["media"] or ""
    narrow = "max-width" in media or "min-width" in media
    rank = RANK.get(d["selector"], 2) + (3 if narrow else 0) + (9 if "[--" in d["selector"] else 0)
    cur = DECL[o][theme].get(d["name"])
    if cur is None or rank < cur[0]:
        DECL[o][theme][d["name"]] = (rank, d)


def resolve(owner, theme, name, seen=None):
    """Follow var() chains inside the owner's declarations. Returns (value, chain)."""
    seen = seen or []
    if name in seen:
        raise ValueError("var() cycle: " + " -> ".join(seen + [name]))
    seen = seen + [name]
    d = DECL[owner][theme].get(name) or DECL[owner]["light"].get(name)
    if not d:
        raise KeyError(f"{name} is not a {owner} variable in raw/css-vars.json")
    val, sel = d[1]["value"].strip(), d[1]["selector"]
    m = re.fullmatch(r"var\((--[\w-]+)\)", val)
    if m:
        v2, chain = resolve(owner, theme, m.group(1), seen)
        return v2, chain + [(name, sel)]
    return val, [(name, sel)]


# ---------------------------------------------------------------- colour helpers


def srgb_chan(c):
    c = max(0.0, min(1.0, c))
    return round((12.92 * c if c <= 0.0031308 else 1.055 * c ** (1 / 2.4) - 0.055) * 255)


def lab_rgb(L, a, b):
    """CIELAB D50 -> sRGB, per CSS Color 4."""
    fy = (L + 16) / 116
    fx, fz = fy + a / 500, fy - b / 200
    eps, kap = 216 / 24389, 24389 / 27
    def f(t):
        t3 = t ** 3
        return t3 if t3 > eps else (116 * t - 16) / kap
    X, Y, Z = 0.96422 * f(fx), f(fy), 0.82521 * f(fz)
    r = 3.1338561 * X - 1.6168667 * Y - 0.4906146 * Z
    g = -0.9787684 * X + 1.9161415 * Y + 0.0334540 * Z
    bl = 0.0719453 * X - 0.2289914 * Y + 1.4052427 * Z
    return [srgb_chan(v) for v in (r, g, bl)]


def oklab_rgb(L, a, b):
    l = (L + 0.3963377774 * a + 0.2158037573 * b) ** 3
    m = (L - 0.1055613458 * a - 0.0638541728 * b) ** 3
    s = (L - 0.0894841775 * a - 1.2914855480 * b) ** 3
    rgb = [4.0767416621 * l - 3.3077115913 * m + 0.2309699292 * s,
           -1.2684380046 * l + 2.6097574011 * m - 0.3413193965 * s,
           -0.0041960863 * l - 0.7034186147 * m + 1.7076147010 * s]
    return [srgb_chan(x) for x in rgb]


def fmt_color(rgb, a):
    a = round(float(a), 3)
    if a >= 1:
        return "#%02x%02x%02x" % tuple(rgb)
    return "rgba(%d, %d, %d, %s)" % (rgb[0], rgb[1], rgb[2], "%g" % a)


def norm_color(v):
    """Any colour string -> '#rrggbb' or 'rgba(r, g, b, a)'."""
    v = v.strip().lower()
    m = re.fullmatch(r"(\d{1,3})\s+(\d{1,3})\s+(\d{1,3})", v)
    if m:  # Mintlify's RGB triplets: "255 98 0" on :root
        return fmt_color([int(x) for x in m.groups()], 1)
    m = re.fullmatch(r"#([0-9a-f]{3,8})", v)
    if m:
        h = m.group(1)
        if len(h) in (3, 4):
            h = "".join(c * 2 for c in h)
        r, g, b = (int(h[i:i + 2], 16) for i in (0, 2, 4))
        if len(h) == 8:
            a = round(int(h[6:8], 16) / 255, 3)
            return fmt_color((r, g, b), a)
        return fmt_color((r, g, b), 1)
    m = re.fullmatch(r"rgba?\(\s*(\d+)[,\s]+(\d+)[,\s]+(\d+)(?:\s*[,/]\s*([\d.]+%?))?\s*\)", v)
    if m:
        r, g, b, a = m.groups()
        a = float(a[:-1]) / 100 if a and a.endswith("%") else float(a or 1)
        return fmt_color((int(r), int(g), int(b)), a)
    m = re.fullmatch(r"hsla?\(\s*([\d.]+)[,\s]+([\d.]+)%[,\s]+([\d.]+)%(?:\s*[,/]\s*([\d.]+%?))?\s*\)", v)
    if m:
        h, s, l, a = m.groups()
        a = float(a[:-1]) / 100 if a and a.endswith("%") else float(a or 1)
        h, s, l = float(h) / 360, float(s) / 100, float(l) / 100
        if s == 0:
            return fmt_color((round(l * 255),) * 3, a)
        q = l * (1 + s) if l < 0.5 else l + s - l * s
        p = 2 * l - q
        def hue(t):
            t %= 1
            if t < 1 / 6: return p + (q - p) * 6 * t
            if t < 1 / 2: return q
            if t < 2 / 3: return p + (q - p) * (2 / 3 - t) * 6
            return p
        return fmt_color([round(hue(h + d) * 255) for d in (1 / 3, 0, -1 / 3)], a)
    m = re.fullmatch(r"(?:ok)?lab\(\s*([-\d.e]+%?)\s+([-\d.e]+)\s+([-\d.e]+)(?:\s*/\s*([\d.]+%?))?\s*\)", v)
    if m:
        L, a_, b_, al = m.groups()
        L = float(L[:-1]) / 100 if L.endswith("%") else float(L)
        al = float(al[:-1]) / 100 if al and al.endswith("%") else float(al or 1)
        fn = oklab_rgb if v.startswith("oklab") else lab_rgb
        return fmt_color(fn(float(L), float(a_), float(b_)), al)
    m = re.fullmatch(r"oklch\(\s*([-\d.e]+%?)\s+([-\d.e]+)\s+([-\d.e]+)(?:\s*/\s*([\d.]+%?))?\s*\)", v)
    if m:
        L, c_, h_, al = m.groups()
        L = float(L[:-1]) / 100 if L.endswith("%") else float(L)
        al = float(al[:-1]) / 100 if al and al.endswith("%") else float(al or 1)
        import math
        a_, b_ = float(c_) * math.cos(math.radians(float(h_))), float(c_) * math.sin(math.radians(float(h_)))
        return fmt_color(oklab_rgb(float(L), a_, b_), al)
    raise ValueError("not a colour: " + v)


DIM = re.compile(r"-?\d*\.?\d+(px|rem)")


def dim(v):
    """A dimension string, resolving rem factors and calc(var(--x) * n)."""
    v = v.strip()
    if DIM.fullmatch(v):
        return v
    m = re.fullmatch(r"calc\(var\((--[\w-]+)\)\s*\*\s*([\d.]+)\)", v)
    if m:
        base = dim(resolve("mintlify", "light", m.group(1))[0])
        n = float(base[:-3] if base.endswith("rem") else base[:-2])
        unit = "rem" if base.endswith("rem") else "px"
        return ("%g" % round(n * float(m.group(2)), 4)) + unit
    raise ValueError("not a px/rem length: " + v)


def duration(v):
    v = v.strip()
    m = re.fullmatch(r"([\d.]+)(m?s)", v)
    if not m:
        raise ValueError("not a duration: " + v)
    return ("%g" % round(float(m.group(1)) * (1 if m.group(2) == "ms" else 1000), 3)) + "ms"


def bezier(v):
    m = re.fullmatch(r"cubic-bezier\(\s*([-\d.e]+)[,\s]+([-\d.e]+)[,\s]+([-\d.e]+)[,\s]+([-\d.e]+)\s*\)", v.strip())
    if not m:
        raise ValueError("not a cubic-bezier: " + v)
    return [float("%g" % float(x)) for x in m.groups()]


def check(path, ty, val):
    if isinstance(val, str) and val.startswith("{"):
        return
    if ty == "dimension" and not DIM.fullmatch(str(val)):
        raise ValueError(f"{path}: dimension must be one px or rem length, got {val!r}")
    if ty == "color":
        norm_color(val)
    if ty == "shadow":
        for layer in val:
            for k in ("offsetX", "offsetY", "blur", "spread"):
                if not DIM.fullmatch(str(layer[k])):
                    raise ValueError(f"{path}: shadow {k} {layer[k]!r}")
            norm_color(layer["color"])
    if ty == "number" and not isinstance(val, (int, float)):
        raise ValueError(f"{path}: number {val!r}")
    if ty == "fontWeight" and not isinstance(val, int):
        raise ValueError(f"{path}: fontWeight {val!r}")
    if ty == "duration" and not re.fullmatch(r"\d+ms", str(val)):
        raise ValueError(f"{path}: duration {val!r}")
    if ty == "cubicBezier" and not (isinstance(val, list) and len(val) == 4):
        raise ValueError(f"{path}: cubicBezier {val!r}")


# ---------------------------------------------------------------- leaves


def leaf(path, spec, theme):
    ty = spec["type"]
    if "var" in spec:
        name = spec["var"]
        owner = spec.get("owner", "anam")
        val, chain = resolve(owner, theme, name)
        src = "css-var " + " -> ".join(f"{n} ({s})" for n, s in reversed(chain))
        if spec.get("source"):
            src += "; " + spec["source"]
        # an alias when the chain ends on a variable that is itself a core token
        # holding the same resolved value
        if ty == "color" and chain[0][0] in ALIAS and norm_color(val) == ALIAS_VAL.get(ALIAS[chain[0][0]]):
            val = "{" + ALIAS[chain[0][0]] + "}"
        else:
            if ty == "color":
                val = norm_color(val)
            elif ty == "dimension":
                val = dim(val)
            elif ty == "duration":
                val = duration(val)
            elif ty == "cubicBezier":
                val = bezier(val)
    else:
        val = spec["value"]
        src = spec.get("source") or (f"alias of {val}" if str(val).startswith("{") else None)
        if not src:
            raise KeyError(f"{path}: leaf needs 'source' or 'var'")
        if ty == "color" and not str(val).startswith("{"):
            val = norm_color(val)
    if ty in ("fontWeight", "number") and isinstance(val, str) and val.isdigit():
        val = int(val)
    if ty == "dimension" and isinstance(val, str) and re.fullmatch(r"-?\d+(\.\d+)?", val):
        val += "px"
    check(path, ty, val)
    t = {"$value": val, "$type": ty, "$extensions": {"source": src}}
    if spec.get("description"):
        t["$description"] = spec["description"]
    if spec.get("responsive"):
        t["$extensions"]["responsive"] = spec["responsive"]
    if spec.get("angle"):
        t["$extensions"]["angle"] = spec["angle"]
    return t


def build(node, theme, path=""):
    if isinstance(node, dict) and "type" in node and ("value" in node or "var" in node):
        return leaf(path, node, theme)
    if isinstance(node, dict) and "$value" in node:
        return node  # already a DTCG leaf (typography composites, shadows)
    out = {}
    for k, v in node.items():
        if k.startswith("_"):
            continue
        if k == "$description":
            out[k] = v
            continue
        out[k] = build(v, theme, f"{path}.{k}" if path else k)
    return out


# map every var a core leaf names to its token path, so theme leaves can alias into core
ALIAS = {}
def collect(node, path=""):
    for k, v in node.items():
        if k.startswith("_"):
            continue
        p = f"{path}.{k}" if path else k
        if isinstance(v, dict) and "type" in v and "var" in v:
            ALIAS.setdefault(v["var"], p)
        elif isinstance(v, dict):
            collect(v, p)
collect(SPEC["core"])

# the resolved $value of each core token, for alias-vs-literal checks; empty
# while core itself builds (core leaves never alias out), populated after
ALIAS_VAL = {}
core = build(SPEC["core"], "light")

def _collect_vals(tree, prefix=""):
    for k, v in tree.items():
        if isinstance(v, dict) and "$value" in v:
            ALIAS_VAL[prefix + k] = v["$value"]
        elif isinstance(v, dict):
            _collect_vals(v, prefix + k + ".")
_collect_vals(core)

light = build(SPEC["light"], "light")
dark = build(SPEC["dark"], "dark")


# every alias must point at a token in its own set or core; light and dark should name the same roles
from token_checks import alias_errors, parity_gap  # noqa: E402

_errors = alias_errors(core, light, dark)
if _errors:
    raise KeyError("; ".join(_errors))
# Dark exists only on the docs surface (Mintlify's .dark theme); the marketing and app pages have
# no dark decls, so the dark set names fewer roles than light — reported, not fatal.
_only_light, _only_dark = parity_gap(light, dark)
if _only_light or _only_dark:
    print(f"warning: light and dark differ: {len(_only_light)} only in light ({', '.join(_only_light)}); "
          f"{len(_only_dark)} only in dark ({', '.join(_only_dark)})", file=sys.stderr)

tokens = {
    "core": core,
    "light": light,
    "dark": dark,
    "$themes": [
        {"id": "light", "name": "Light", "selectedTokenSets": {"core": "source", "light": "enabled"},
         "$description": "The only theme the marketing pages and the /pricing, /get-demo and /tools apps ship; the docs' default. Measured at 1440x900 and 390x844"},
        {"id": "dark", "name": "Dark", "selectedTokenSets": {"core": "source", "dark": "enabled"},
         "$description": "Only the Mintlify docs go dark (.dark on html, via the theme toggle; prefers-color-scheme does not switch the marketing site). Black ground, warm-stone text, the same orange accent"},
    ],
    "$metadata": {"tokenSetOrder": ["core", "light", "dark"]},
}
(HERE / "tokens.json").write_text(json.dumps(tokens, indent=2, ensure_ascii=False) + "\n")


def count(d):
    return sum(count(v) for v in d.values()) if isinstance(d, dict) and "$value" not in d else 1


print({k: count(v) for k, v in tokens.items() if k in ("core", "light", "dark")})
