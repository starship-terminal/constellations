#!/usr/bin/env python3
"""Build tokens.json (W3C DTCG, Tokens Studio multi-set layout) from the raw captures.

Sources, read from the public, signed-out www.intercom.com pages:
  raw/css-vars.json          the custom properties the site declares — the
                             Tailwind v4 @layer theme set on :root (the warm
                             neutral ramp, the blueprint blues, the product
                             accents, the responsive --text-{style}-{bp}
                             scale, the radius/blur/container/z-index geometry
                             and the --ease-* curves), the unlayered --button-*
                             state matrix and --body-bg, the .theme-light nav
                             roles (--color-nav-*), and the scoped sets on
                             .brand-i2y4, .intercom-legacy and
                             [data-media-player]; resolved by
                             tools/capture/vars.mjs on probes carrying the
                             real sheets, then binned theme / nav / brand /
                             legacy / media / component / utility / tailwind
  raw/component-tokens.json  the token tree (tools/build_component_tokens.py):
                             each leaf either names a variable ("var") resolved
                             per scope, or carries a measured value and the
                             measurement it came from ("source")
Every token carries $extensions.source: "css-var <name> (<scope>)" or the
measurement description.

www.intercom.com paints one theme: body.theme-light everywhere, no dark
control or dark repaint anywhere (themeChecks in raw/css-vars.json). The
package therefore ships `core` and `light` only — there is no dark set to
declare, and inventing one would misstate the product.

Deterministic: same inputs, byte-identical output. Edit the raw inputs, never tokens.json.
"""
import json, math, pathlib, re, sys

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
sys.path.insert(0, str(HERE / "tools"))
import motion as motion_mod  # tools/motion.py -> core.motion (docs/decisions/0001)

V = json.loads((RAW / "css-vars.json").read_text())
SPEC = json.loads((RAW / "component-tokens.json").read_text())
MOTION = json.loads((RAW / "motion.json").read_text()) if (RAW / "motion.json").exists() else None

# Resolved declarations per scope. vars.mjs resolves each custom property on
# probes carrying the real sheets and the live page's own classes: the light
# probe is the page's body.theme-light context; "brand"/"legacy"/"media" are
# the .brand-i2y4/.intercom-legacy/[data-media-player] probes. A scoped leaf
# sees its own scope's declarations layered over the light set, which is how
# the cascade paints a descendant of that element.
DECL = {"light": {n: v.get("value", v["raw"]) for n, v in V["resolved"]["light"].items()}}
for scope, names in (V["resolved"].get("scopes") or {}).items():
    DECL[scope] = {**DECL["light"], **{n: v.get("value", v["raw"]) for n, v in names.items()}}


def _gam(c):
    return 12.92 * c if c <= 0.0031308 else 1.055 * c ** (1 / 2.4) - 0.055


def _oklab(L, a, b):
    """OKLab -> sRGB (Ottosson). L in 0..1, a/b chroma components."""
    l_ = L + 0.3963377774 * a + 0.2158037573 * b
    m_ = L - 0.1055613458 * a - 0.0638541729 * b
    s_ = L - 0.0894841775 * a - 1.2914855480 * b
    l, m, s = l_ ** 3, m_ ** 3, s_ ** 3
    r = +4.0767416621 * l - 3.3077115913 * m + 0.2309699292 * s
    g = -1.2684380046 * l + 2.6097574011 * m - 0.3413193965 * s
    bl = -0.0041960863 * l - 0.7034186147 * m + 1.7076147010 * s
    return tuple(max(0, min(255, round(_gam(c) * 255))) for c in (r, g, bl))


def _lab(L, A, B):
    """CIE Lab (D50) -> sRGB."""
    fy = (L + 16) / 116
    fx, fz = fy + A / 500, fy - B / 200
    d = 6 / 29
    f = lambda t: t ** 3 if t > d else 3 * d ** 2 * (t - 4 / 29)
    x, y, z = f(fx) * 0.96422, f(fy) * 1.0, f(fz) * 0.82521
    r = 3.1338561 * x - 1.6168667 * y - 0.4906146 * z
    g = -0.9787684 * x + 1.9161415 * y + 0.0334540 * z
    b = 0.0719453 * x - 0.2289914 * y + 1.4052427 * z
    return tuple(max(0, min(255, round(_gam(c) * 255))) for c in (r, g, b))


def _hex(r, g, b, a=None):
    if a is None or a >= 1:
        return "#%02x%02x%02x" % (r, g, b)
    return "rgba(%d, %d, %d, %g)" % (r, g, b, a)


def _alpha(a):
    if a is None:
        return None
    return float(a[:-1]) / 100 if a.endswith("%") else float(a)


def _pct_or_num(v, scale=1.0):
    v = v.strip()
    return float(v[:-1]) / 100 * scale if v.endswith("%") else float(v) * scale


def norm_color(v):
    """#rgb/#rrggbb/#rrggbbaa, rgb(), hsl(), lab(), lch(), oklab(), oklch(),
    color-mix -> #rrggbb or rgba(r, g, b, a)."""
    v = v.strip().lower()
    m = re.fullmatch(r"#([0-9a-f]{3,8})", v)
    if m:
        h = m.group(1)
        if len(h) in (3, 4):
            h = "".join(c * 2 for c in h)
        r, g, b = (int(h[i:i + 2], 16) for i in (0, 2, 4))
        return _hex(r, g, b, int(h[6:8], 16) / 255 if len(h) == 8 else None)
    m = re.fullmatch(r"rgba?\(\s*(\d+)[,\s]+(\d+)[,\s]+(\d+)(?:\s*[,/]\s*([\d.]+%?))?\s*\)", v)
    if m:
        r, g, b, a = m.groups()
        return _hex(int(r), int(g), int(b), _alpha(a))
    # hsl()/hsla(): computed values on the marketing site occasionally keep
    # this form (Chromium serialises some resolved custom props verbatim).
    m = re.fullmatch(r"hsla?\(\s*(-?[\d.]+)(?:deg)?[,\s]+([\d.]+)%[,\s]+([\d.]+)%(?:\s*[,/]\s*([\d.]+%?))?\s*\)", v)
    if m:
        h, s, l, a = float(m.group(1)) % 360, float(m.group(2)) / 100, float(m.group(3)) / 100, _alpha(m.group(4))
        c = (1 - abs(2 * l - 1)) * s
        x = c * (1 - abs((h / 60) % 2 - 1))
        m0 = l - c / 2
        r, g, b = ((c, x, 0), (x, c, 0), (0, c, x), (0, x, c), (x, 0, c), (c, 0, x))[int(h // 60) % 6]
        return _hex(round((r + m0) * 255), round((g + m0) * 255), round((b + m0) * 255), a)
    m = re.fullmatch(r"oklab\(\s*([-\d.]+%?)\s+(-?[\d.]+)\s+(-?[\d.]+)\s*(?:/\s*([\d.]+%?))?\s*\)", v)
    if m:
        L, a, b, al = _pct_or_num(m.group(1)), float(m.group(2)), float(m.group(3)), _alpha(m.group(4))
        return _hex(*_oklab(L, a, b), al)
    m = re.fullmatch(r"oklch\(\s*([-\d.]+%?)\s+([-\d.]+)\s+(-?[\d.]+|none)(?:deg)?\s*(?:/\s*([\d.]+%?))?\s*\)", v)
    if m:
        L, c, h, al = _pct_or_num(m.group(1)), float(m.group(2)), m.group(3), _alpha(m.group(4))
        h = 0.0 if h == "none" else float(h)
        a, b = c * math.cos(math.radians(h)), c * math.sin(math.radians(h))
        return _hex(*_oklab(L, a, b), al)
    m = re.fullmatch(r"lab\(\s*([-\d.]+%?)\s+(-?[\d.]+)\s+(-?[\d.]+)\s*(?:/\s*([\d.]+%?))?\s*\)", v)
    if m:
        L = _pct_or_num(m.group(1), 100.0)
        return _hex(*_lab(L, float(m.group(2)), float(m.group(3))), _alpha(m.group(4)))
    m = re.fullmatch(r"lch\(\s*([-\d.]+%?)\s+([\d.]+)\s+(-?[\d.]+|none)(?:deg)?\s*(?:/\s*([\d.]+%?))?\s*\)", v)
    if m:
        L, c, h, al = _pct_or_num(m.group(1), 100.0), float(m.group(2)), m.group(3), _alpha(m.group(4))
        h = 0.0 if h == "none" else float(h)
        return _hex(*_lab(L, c * math.cos(math.radians(h)), c * math.sin(math.radians(h))), al)
    m = re.fullmatch(r"color\(srgb\s+([\d.]+%?)\s+([\d.]+%?)\s+([\d.]+%?)\s*(?:/\s*([\d.]+%?))?\s*\)", v)
    if m:
        r, g, b = (round(_pct_or_num(x) * 255) if x.endswith("%") else round(float(x) * 255) for x in m.groups()[:3])
        return _hex(r, g, b, _alpha(m.group(4)))
    # color-mix(in <space>, <colour> p%, transparent): a transparent share
    # leaves the colour at alpha over an achromatic path.
    m = re.fullmatch(r"color-mix\(in\s+\w+,\s*(.+?)\s*(?:([\d.]+)%)?,\s*(.+?)\s*(?:([\d.]+)%)?\)", v)
    if m:
        c1, p1, c2, p2 = m.groups()
        if c1.strip() == "transparent" or c2.strip() == "transparent":
            if c1.strip() == "transparent":
                c1, c2, p1, p2 = c2, c1, p2, p1
            p1 = float(p1) / 100 if p1 else (1 - float(p2) / 100 if p2 else 0.5)
            base = norm_color(c1)
            if base.startswith("rgba("):
                mm = re.fullmatch(r"rgba\((\d+), (\d+), (\d+), ([\d.]+)\)", base)
                r, g, b, a = mm.groups()
                a = round(float(a) * p1, 4)
            else:
                r, g, b = (int(base[i:i + 2], 16) for i in (1, 3, 5))
                a = round(p1, 4)
            return _hex(int(r), int(g), int(b), a)
    raise ValueError("not a colour: " + v)


DIM = re.compile(r"-?(\d+(\.\d+)?|\.\d+)(px|rem)")


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
            norm_color(layer["color"])
    if ty == "number" and not isinstance(val, (int, float)):
        raise ValueError(f"{path}: number {val!r}")
    if ty == "fontWeight" and not isinstance(val, (int, float)):
        raise ValueError(f"{path}: fontWeight {val!r}")
    if ty == "fontFamily" and not isinstance(val, str):
        raise ValueError(f"{path}: fontFamily {val!r}")
    if ty == "duration" and not re.fullmatch(r"\d+ms", str(val)):
        raise ValueError(f"{path}: duration {val!r}")
    if ty == "cubicBezier" and not (isinstance(val, list) and len(val) == 4):
        raise ValueError(f"{path}: cubicBezier {val!r}")
    if ty == "other":
        return


def leaf(path, spec, theme):
    ty = spec["type"]
    if "var" in spec:
        name = spec["var"]
        scope = spec.get("scope") or theme
        if name not in DECL.get(scope, {}):
            raise KeyError(f"{path}: {name} is not a resolved variable in raw/css-vars.json ({scope})")
        val = DECL[scope][name]
        src = f"css-var {name} ({scope} scope)" if scope != "light" else f"css-var {name}"
        if spec.get("source"):
            src += "; " + spec["source"]
    else:
        val = spec["value"]
        src = spec["source"]
    if ty == "color" and not str(val).startswith("{"):
        val = norm_color(val)
    if ty == "shadow":
        for layer in val:
            if not str(layer["color"]).startswith("{"):
                layer["color"] = norm_color(layer["color"])
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
            val = val.strip()
            if re.fullmatch(r"-?\.\d+(px|rem)", val):
                val = ("-0" if val.startswith("-") else "0") + val.lstrip("-")
            elif re.fullmatch(r"-?\d+(\.\d+)?", val):
                val = val + "px"
    check(path, ty, val)
    t = {"$value": val, "$type": ty, "$extensions": {"source": src}}
    if spec.get("description"):
        t["$description"] = spec["description"]
    if spec.get("responsive"):
        t["$extensions"]["responsive"] = spec["responsive"]
    return t


def build(node, theme, path=""):
    if isinstance(node, dict) and "type" in node and ("value" in node or "var" in node):
        return leaf(path, node, theme)
    if isinstance(node, dict) and "$value" in node:
        return node  # already a DTCG leaf (typography composites, parsed shadows)
    return {k: build(v, theme, f"{path}.{k}" if path else k) for k, v in node.items() if not k.startswith("_")}


core = build(SPEC["core"], "light")  # scales are theme-independent
light = build(SPEC["light"], "light")
# The component tokens live in their own top-level spec tree but are
# theme-independent declared/measurement tokens (the --button-* state matrix,
# the media player's geometry), so they hang off core.
core["component"] = build(SPEC["component"], "light")
# docs/decisions/0001: the motion probe's measured durations, easings,
# transitions and animations are tokens too; curves a cubicBezier cannot
# carry (steps(), linear()) are recorded under the group's notTokenised.
if MOTION:
    core["motion"], motion_nt = motion_mod.build(MOTION)
    if motion_nt:
        core["motion"].setdefault("$extensions", {})["notTokenised"] = motion_nt


# every alias must point at a token that exists
def tokens_of(tree, prefix=""):
    for k, v in tree.items():
        if isinstance(v, dict) and "$value" in v:
            yield prefix + k, v
        elif isinstance(v, dict):
            yield from tokens_of(v, prefix + k + ".")


NAMES = {n for n, _ in tokens_of(core)}
NAMES_L = NAMES | {n for n, _ in tokens_of(light)}


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

tokens = {
    "core": core,
    "light": light,
    "$themes": [
        {"id": "light", "name": "Light", "selectedTokenSets": {"core": "source", "light": "enabled"},
         "$description": "The only painted theme: every public www.intercom.com page boots body.theme-light — a cream ground, off-black ink, blueprint blues and the Fin orange. The stylesheet declares no dark theme and no control repaints one, so no dark set exists to capture."},
    ],
    "$metadata": {"tokenSetOrder": ["core", "light"]},
}
(HERE / "tokens.json").write_text(json.dumps(tokens, indent=2, ensure_ascii=False) + "\n")


def count(d):
    return sum(count(v) for v in d.values()) if isinstance(d, dict) and "$value" not in d else 1


print({k: count(v) for k, v in tokens.items() if k in ("core", "light")})
