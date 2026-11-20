#!/usr/bin/env python3
"""Build tokens.json (W3C DTCG, Tokens Studio multi-set layout) from the raw captures.

Sources, read from copy.ai on 2026-11-12:
  raw/css-vars.json          the custom properties copy.ai's Webflow sheets
                             declare — the named --colors--* brand palette plus
                             the legacy --old-swatches--* set — read from the
                             cross-origin cdn.prod.website-files.com responses
                             plus the inline style blocks (tools/capture/vars.mjs),
                             resolved on a probe document (one light theme)
  raw/component-tokens.json  the token tree (tools/build_component_tokens.py): each leaf either
                             names a variable ("var") resolved per theme, or carries a measured
                             value and the measurement it came from ("source")
Every token carries $extensions.source: "css-var <name>" or "measured <where>".

copy.ai's public surface paints a single light theme with ink-dark bands
inside it (the top banner, the deep-purple feature card, the inverted CTA's
band). The export holds core, light and dark: light roles are aliases over
the measured neutrals and the #693ee0 action purple, and "dark" is the small
role set those bands paint — not a user-selectable theme.

Deterministic: same inputs, byte-identical output. Edit the raw inputs, never tokens.json.
"""
import json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
V = json.loads((RAW / "css-vars.json").read_text())
SPEC = json.loads((RAW / "component-tokens.json").read_text())

# Resolved declarations per theme. vars.mjs resolves each custom property on a
# probe document once light (:root) and once dark (html.dark), so
# DECL[theme][name] is what the browser paints in that theme. A name declared
# only on :root resolves the same in both.
DECL = {t: {n: v.get("value", v["raw"]) for n, v in V.get("resolved", {}).get(t, {}).items()} for t in ("light", "dark")}
# cosmos.so resolves both declared sets in one pass: the --dark-* names sit in
# resolved.light, so the dark map is those names lifted out. var leaves then
# carry their own --dark-* names, keeping the declared name honest.
if not DECL["dark"]:
    DECL["dark"] = {n: v for n, v in DECL["light"].items() if n.startswith("--dark-")}


# ---- CSS Color 4 -> sRGB (finding 15-10). tools/catalog.py reads only hex/rgb()/rgba(), so a lab(), lch(),
# oklab(), oklch() or color-mix() value left as written is never contrast-checked. These are converted the
# way the browser paints them and the authored form is kept in $extensions.authored.
import math as _math


def _gamma(c):
    return 12.92 * c if c <= 0.0031308 else 1.055 * c ** (1 / 2.4) - 0.055


def _rgb255(lin):
    return [round(min(1, max(0, _gamma(c))) * 255) for c in lin]


def _oklab_lin(L, a, b):
    l_ = (L + 0.3963377774 * a + 0.2158037573 * b) ** 3
    m_ = (L - 0.1055613458 * a - 0.0638541728 * b) ** 3
    s_ = (L - 0.0894841775 * a - 1.2914855480 * b) ** 3
    return [4.0767416621 * l_ - 3.3077115913 * m_ + 0.2309699292 * s_,
            -1.2684380046 * l_ + 2.6097574011 * m_ - 0.3413193965 * s_,
            -0.0041960863 * l_ - 0.7034186147 * m_ + 1.7076147010 * s_]


def _lab_lin(L, a, b):
    """CIE Lab (D50) -> linear sRGB (D65), Bradford-adapted as CSS Color 4 specifies."""
    k, e = 24389 / 27, 216 / 24389
    fy = (L + 16) / 116
    fx, fz = fy + a / 500, fy - b / 200
    x = fx ** 3 if fx ** 3 > e else (116 * fx - 16) / k
    y = ((L + 16) / 116) ** 3 if L > k * e else L / k
    z = fz ** 3 if fz ** 3 > e else (116 * fz - 16) / k
    X, Y, Z = x * 0.3457 / 0.3585, y, z * (1 - 0.3457 - 0.3585) / 0.3585
    M1 = [[0.9554734527042182, -0.023098536874261423, 0.0632593086610217],
          [-0.028369706963208136, 1.0099954580058226, 0.021041398966943008],
          [0.012314001688319899, -0.020507696433477912, 1.3303659366080753]]
    X, Y, Z = (sum(M1[i][j] * v for j, v in enumerate((X, Y, Z))) for i in range(3))
    M2 = [[3.2409699419045226, -1.537383177570094, -0.4986107602930034],
          [-0.9692436362808796, 1.8759675015077202, 0.04155505740717559],
          [0.05563007969699366, -0.20397695888897652, 1.0569715142428786]]
    return [sum(M2[i][j] * v for j, v in enumerate((X, Y, Z))) for i in range(3)]


def _num(s, pct_scale=1.0):
    s = s.strip()
    return float(s[:-1]) * pct_scale / 100 if s.endswith("%") else float(s)


def _fmt(rgb, alpha):
    alpha = round(alpha, 4)
    if alpha >= 1:
        return "#%02x%02x%02x" % tuple(rgb)
    return "rgba(%d, %d, %d, %g)" % (rgb[0], rgb[1], rgb[2], alpha)


_FN = re.compile(r"(lab|lch|oklab|oklch)\(\s*([^)]*)\)", re.I)


def css4_parts(v):
    """(r, g, b) 0-255 and alpha for a lab()/lch()/oklab()/oklch() value, or None."""
    m = _FN.fullmatch(v.strip())
    if not m:
        return None
    kind, body = m.group(1).lower(), m.group(2)
    main, _, alpha = body.partition("/")
    p = main.split()
    if len(p) != 3:
        raise ValueError("cannot read colour " + v)
    p = ["0" if x == "none" else x.replace("deg", "") for x in p]
    a = 1.0 if not alpha.strip() else _num(alpha, 1.0)
    if kind in ("lab", "lch"):
        L = _num(p[0], 100)
        if kind == "lab":
            A, B = _num(p[1], 125), _num(p[2], 125)
        else:
            c, h = _num(p[1], 150), _math.radians(float(p[2]))
            A, B = c * _math.cos(h), c * _math.sin(h)
        return _rgb255(_lab_lin(L, A, B)), a
    L = _num(p[0], 1)
    if kind == "oklab":
        A, B = _num(p[1], 0.4), _num(p[2], 0.4)
    else:
        c, h = _num(p[1], 0.4), _math.radians(float(p[2]))
        A, B = c * _math.cos(h), c * _math.sin(h)
    return _rgb255(_oklab_lin(L, A, B)), a


def css4_srgb(v):
    """A lab()/lch()/oklab()/oklch() value, or color-mix(in <space>, <one of those or rgb()> P%, transparent),
    as #rrggbb or rgba(); None when v is none of these. Mixing a colour with transparent keeps the colour and
    scales its alpha (premultiplied), in any interpolation space. Any other color-mix raises."""
    v = v.strip()
    if v.lower().startswith("color-mix("):
        m = re.fullmatch(r"color-mix\(\s*in\s+[a-z0-9-]+(?:\s+[a-z]+\s+hue)?\s*,\s*(.+?)\s+([\d.]+)%\s*,\s*transparent\s*\)", v, re.I)
        if not m:
            raise ValueError("cannot convert " + v)
        inner = m.group(1)
        parts = css4_parts(inner)
        if parts is None:
            rm = re.fullmatch(r"rgba?\(\s*(\d+)[,\s]+(\d+)[,\s]+(\d+)(?:\s*[,/]\s*([\d.]+))?\s*\)", inner)
            if not rm:
                raise ValueError("cannot convert " + v)
            parts = [int(rm.group(i)) for i in (1, 2, 3)], float(rm.group(4) or 1)
        rgb, a = parts
        return _fmt(rgb, a * float(m.group(2)) / 100)
    parts = css4_parts(v)
    return _fmt(*parts) if parts else None


def norm_color(v):
    """#rgb, #rrggbb, #rrggbbaa, rgb(), rgba(), hsla(), "R G B" channels -> #rrggbb or rgba(r, g, b, a)."""
    v = v.strip().lower()
    m = re.fullmatch(r"(\d+)\s+(\d+)\s+(\d+)", v)
    if m:  # channel triplets ("0 230 6") that rgb(var(--x) / a) composites
        return "#%02x%02x%02x" % (int(m.group(1)), int(m.group(2)), int(m.group(3)))
    m = re.fullmatch(r"#([0-9a-f]{3,8})", v)
    if m:
        h = m.group(1)
        if len(h) in (3, 4):
            h = "".join(c * 2 for c in h)
        r, g, b = (int(h[i:i + 2], 16) for i in (0, 2, 4))
        if len(h) == 8:
            a = round(int(h[6:8], 16) / 255, 3)
            return "#%02x%02x%02x" % (r, g, b) if a == 1 else "rgba(%d, %d, %d, %s)" % (r, g, b, ("%g" % a))
        return "#%02x%02x%02x" % (r, g, b)
    m = re.fullmatch(r"rgba?\(\s*(\d+)[,\s]+(\d+)[,\s]+(\d+)(?:\s*[,/]\s*([\d.]+%?))?\s*\)", v)
    if m:
        r, g, b, a = m.groups()
        if a is None:
            return "#%02x%02x%02x" % (int(r), int(g), int(b))
        a = float(a[:-1]) / 100 if a.endswith("%") else float(a)
        return "#%02x%02x%02x" % (int(r), int(g), int(b)) if a == 1 else "rgba(%s, %s, %s, %g)" % (r, g, b, a)
    m = re.fullmatch(r"hsla?\(\s*0\s*,\s*0%\s*,\s*([\d.]+)%\s*(?:,\s*([\d.]+))?\)", v)
    if m:
        lvl = round(float(m.group(1)) * 2.55)
        a = float(m.group(2) or 1)
        return "#%02x%02x%02x" % (lvl, lvl, lvl) if a == 1 else "rgba(%d, %d, %d, %g)" % (lvl, lvl, lvl, a)
    # CSS Color 4 / composited values convert to sRGB (lab, lch, oklab, oklch, color-mix with transparent)
    c4 = css4_srgb(v)
    if c4:
        return c4
    raise ValueError("not a colour: " + v)


DIM = re.compile(r"-?\d+(\.\d+)?(px|rem)")


def check(path, ty, val):
    """Refuse a value that is not the DTCG type it claims. An alias is checked by the alias pass."""
    if isinstance(val, str) and val.startswith("{"):
        return
    if ty == "dimension" and not DIM.fullmatch(str(val)):
        raise ValueError(f"{path}: dimension must be one px or rem length, got {val!r}")
    if ty == "color":
        norm_color(val) if not str(val).startswith("{") else None
    if ty == "shadow":
        for layer in val:
            for k in ("offsetX", "offsetY", "blur", "spread"):
                if not DIM.fullmatch(layer[k]):
                    raise ValueError(f"{path}: shadow {k} {layer[k]!r}")
    if ty == "number" and not isinstance(val, (int, float)):
        raise ValueError(f"{path}: number {val!r}")
    if ty == "fontWeight" and not isinstance(val, int):
        raise ValueError(f"{path}: fontWeight {val!r}")
    if ty == "duration" and not re.fullmatch(r"\d+ms", str(val)):
        raise ValueError(f"{path}: duration {val!r}")
    if ty == "cubicBezier" and not (isinstance(val, list) and len(val) == 4):
        raise ValueError(f"{path}: cubicBezier {val!r}")
    if ty == "gradient":
        for stop in val:
            if not str(stop["color"]).startswith("{"):
                norm_color(stop["color"])
            if not 0 <= stop["position"] <= 1:
                raise ValueError(f"{path}: gradient position {stop['position']!r}")


def leaf(path, spec, theme):
    ty = spec["type"]
    if "var" in spec:
        name = spec["var"]
        if name not in DECL[theme]:
            raise KeyError(f"{path}: {name} is not a resolved variable in raw/css-vars.json ({theme})")
        val = DECL[theme][name]
        src = f"css-var {name} ({theme})"
        if spec.get("source"):
            src += "; " + spec["source"]
    else:
        val = spec["value"]
        src = spec["source"]
    authored = None
    if ty == "color" and not str(val).startswith("{"):
        if css4_srgb(str(val)):
            authored = str(val).strip()
        val = norm_color(val)
    if ty == "cubicBezier" and isinstance(val, str):
        m = re.fullmatch(r"cubic-bezier\(\s*([-\d.e]+)[,\s]+([-\d.e]+)[,\s]+([-\d.e]+)[,\s]+([-\d.e]+)\s*\)", val.strip())
        if m:
            val = [float("%g" % float(x)) for x in m.groups()]
        elif val.strip() in ("ease", "ease-in", "ease-out", "ease-in-out", "linear"):
            val = {"ease": [.25, .1, .25, 1], "ease-in": [.42, 0, 1, 1], "ease-out": [0, 0, .58, 1],
                   "ease-in-out": [.42, 0, .58, 1], "linear": [0, 0, 1, 1]}[val.strip()]
    if ty in ("fontWeight", "number") and isinstance(val, str):
        m = re.fullmatch(r"calc\((-?\d*\.?\d+)\s*/\s*(-?\d*\.?\d+)\)", val)
        if m:  # Tailwind v4 emits line-heights as calc(a/b) ratios
            val = round(float(m.group(1)) / float(m.group(2)), 4)
        elif re.fullmatch(r"-?\d+(\.\d+)?", val):
            val = float(val) if "." in val else int(val)
    if ty == "duration" and isinstance(val, str):
        m = re.fullmatch(r"([\d.]+)(m?s)", val.strip())
        if m:
            val = ("%g" % (float(m.group(1)) * (1 if m.group(2) == "ms" else 1000))) + "ms"
    if ty == "dimension":
        if isinstance(val, (int, float)):
            val = "%gpx" % val
        elif isinstance(val, str):
            val = re.sub(r"^(-?)\.(\d)", r"\g<1>0.\2", val.strip())
            if re.fullmatch(r"-?\d+(\.\d+)?", val):
                val = val + "px"
    check(path, ty, val)
    t = {"$value": val, "$type": ty, "$extensions": {"source": src}}
    if authored:
        t["$extensions"]["authored"] = authored
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
        return node  # already a DTCG leaf (typography composites)
    return {k: build(v, theme, f"{path}.{k}" if path else k) for k, v in node.items() if not k.startswith("_")}


core = build(SPEC["core"], "light")  # scales are theme-independent
light = build(SPEC["light"], "light")
dark = build(SPEC["dark"], "dark")
# The component tokens live in their own top-level spec tree but belong to the
# exported themes the components were measured on: light.component.*
light["component"] = build(SPEC["component"], "light")


# every alias must point at a token that exists
def tokens_of(tree, prefix=""):
    for k, v in tree.items():
        if isinstance(v, dict) and "$value" in v:
            yield prefix + k, v
        elif isinstance(v, dict):
            yield from tokens_of(v, prefix + k + ".")


NAMES = {n for n, _ in tokens_of(core)}
NAMES_L = NAMES | {n for n, _ in tokens_of(light)}
NAMES_D = NAMES | {n for n, _ in tokens_of(dark)}


def aliases(v):
    if isinstance(v, str):
        return re.findall(r"\{([^{}]+)\}", v)
    if isinstance(v, dict):
        return [a for x in v.values() for a in aliases(x)]
    if isinstance(v, list):
        return [a for x in v for a in aliases(x)]
    return []


for n, t in list(tokens_of(core)):
    for a in aliases(t["$value"]):
        if a not in NAMES:
            raise KeyError(f"core.{n}: alias {{{a}}} points at nothing")
for n, t in list(tokens_of(light)):
    for a in aliases(t["$value"]):
        if a not in NAMES_L:
            raise KeyError(f"light.{n}: alias {{{a}}} points at nothing")
for n, t in list(tokens_of(dark)):
    for a in aliases(t["$value"]):
        if a not in NAMES_D:
            raise KeyError(f"dark.{n}: alias {{{a}}} points at nothing")

tokens = {
    "core": core,
    "light": light,
    "dark": dark,
    "$themes": [
        {"id": "light", "name": "Light", "selectedTokenSets": {"core": "source", "light": "enabled"},
         "$description": "The public surface: home, pricing, contact, the mega-menu and the rest paint ink on white with #693ee0 actions."},
        {"id": "dark", "name": "Dark", "selectedTokenSets": {"core": "source", "dark": "enabled"},
         "$description": "The ink/deep-purple bands the light page paints — the top banner, the #29007a feature card, the inverted CTA's band — not a user toggle."},
    ],
    "$metadata": {"tokenSetOrder": ["core", "light", "dark"]},
}
(HERE / "tokens.json").write_text(json.dumps(tokens, indent=2, ensure_ascii=False) + "\n")


def count(d):
    return sum(count(v) for v in d.values()) if isinstance(d, dict) and "$value" not in d else 1


print({k: count(v) for k, v in tokens.items() if k in ("core", "light", "dark")})
