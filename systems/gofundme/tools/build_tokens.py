#!/usr/bin/env python3
"""Build tokens.json (W3C DTCG, Tokens Studio multi-set layout) from the raw captures.

Sources, read from gofundme.com:
  raw/css-vars.json          the custom properties www.gofundme.com's
                             stylesheets declare — the hrt design system:
                             ~700 `--hrt-*` semantic custom properties on
                             `:root` / `:where([data-theme="consumer"])`
                             (the consumer light theme: brand green
                             #4A9D44/#274A34/#CCF88E roles, neutral ramps,
                             blue/pink/purple/yellow accents, size,
                             spacing, radius, type, motion and z-index
                             scales), plus a `[data-theme="pro"]` layer
                             that never paints on the consumer surfaces —
                             resolved on `document.documentElement` in a
                             probe carrying the real sheets
                             (tools/capture/vars.mjs) and binned theme /
                             app / skins / vendor / utility
  raw/component-tokens.json  the token tree (tools/build_component_tokens.py): each leaf either
                             names a variable ("var") resolved in the consumer scope, or carries a
                             measured value and the measurement it came from ("source")
Every token carries $extensions.source: "css-var <name>" or "measured <where>".

gofundme.com paints one surface signed out: the consumer light theme every
marketing, discover and fundraiser page resolves from the :root-declared
--hrt-* roles; no dark variant or theme toggle exists on the consumer site
(the [data-theme="pro"] layer is a declared Pro skin, kept in
raw/css-vars.json but never painted here). The /c/* pages are the
WordPress content stack — a different public system — and /sign-in is the
auth boundary; their values are measured component tokens.
tokens.json therefore carries a single `light` set besides `core`; the
measured roles alias to the declared --hrt-* token whose painted value
they match.

Deterministic: same inputs, byte-identical output. Edit the raw inputs, never tokens.json.
"""
import json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
V = json.loads((RAW / "css-vars.json").read_text())
SPEC = json.loads((RAW / "component-tokens.json").read_text())

# Resolved declarations per theme. vars.mjs resolves each custom property on a
# probe document once in the consumer scope (:root / data-theme="consumer")
# and once inside a data-theme="pro" wrapper, so DECL[theme][name] is what the
# browser paints in that scope. A name declared only on :root resolves the
# same in both.
# vars.mjs resolves every custom property on `document.documentElement` —
# :root is the selector that declares the consumer --hrt-* layer — in the
# only scope the consumer site paints.
DECL = {"light": {n: (v.get("value", v.get("raw")) if isinstance(v, dict) else v) for n, v in V["resolved"]["light"].items()}}


def norm_color(v):
    """#rgb, #rrggbb, #rrggbbaa, rgb(), rgba(), hsla() -> #rrggbb or rgba(r, g, b, a)."""
    v = v.strip().lower()
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
    # A channel list — "250 250 250" or "250 250 250 / 0.18" — is how some
    # declarations carry their colour.
    m = re.fullmatch(r"(\d+(?:\.\d+)?)\s+(\d+(?:\.\d+)?)\s+(\d+(?:\.\d+)?)\s*(?:/\s*([\d.]+))?", v)
    if m:
        r, g, b = (int(float(m.group(i))) for i in (1, 2, 3))
        a = float(m.group(4)) if m.group(4) is not None else 1
        return "#%02x%02x%02x" % (r, g, b) if a == 1 else "rgba(%d, %d, %d, %g)" % (r, g, b, a)
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
    # Chromium resolves some tint roles to color-mix(in oklch, <colour>,
    # transparent <p>%): a p% transparent share leaves the colour at
    # alpha (1 - p/100) over an achromatic oklch path — i.e. rgba(c, 1-p/100).
    m = re.fullmatch(r"color-mix\(in\s+\w+,\s*(.+?)\s*(?:([\d.]+)%)?,\s*(.+?)\s*(?:([\d.]+)%)?\)", v)
    if m:
        c1, p1, c2, p2 = m.groups()
        if c1.strip() == "transparent" or c2.strip() == "transparent":
            if c1.strip() == "transparent":
                c1, c2, p1, p2 = c2, c1, p2, p1  # c1 is now the colour
            p1 = float(p1) / 100 if p1 else (1 - float(p2) / 100 if p2 else 0.5)
            base = norm_color(c1)
            if base.startswith("rgba("):
                mm = re.fullmatch(r"rgba\((\d+), (\d+), (\d+), ([\d.]+)\)", base)
                r, g, b, a = mm.groups()
                a = round(float(a) * p1, 4)
            else:
                r, g, b = (int(base[i:i + 2], 16) for i in (1, 3, 5))
                a = round(p1, 4)
            return "#%02x%02x%02x" % (r, g, b) if a == 1 else "rgba(%d, %d, %d, %g)" % (r, g, b, a)
    # Achromatic oklch()/oklab() (the elevation and tint formulas): L 0 is
    # black, L 1 is white, the trailing /a is the alpha.
    m = re.fullmatch(r"okl(?:ch|ab)\(\s*([\d.]+)\s+[\d.]+\s+(?:none|[-\d.]+)\s+(?:none\s+)?(?:/\s*([\d.]+))?\s*\)", v)
    if m:
        lvl = round(float(m.group(1)) * 255)
        a = float(m.group(2) or 1)
        return "#%02x%02x%02x" % (lvl, lvl, lvl) if a == 1 else "rgba(%d, %d, %d, %g)" % (lvl, lvl, lvl, a)
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
    if ty == "color" and not str(val).startswith("{"):
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
        elif isinstance(val, str) and re.fullmatch(r"-?\d+(\.\d+)?", val.strip()):
            val = val.strip() + "px"
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
        return node  # already a DTCG leaf (typography composites)
    out = {}
    for k, v in node.items():
        if k.startswith("_"):
            continue
        if k.startswith("$"):
            out[k] = v  # a group annotation ($description) passes through verbatim
            continue
        out[k] = build(v, theme, f"{path}.{k}" if path else k)
    return out


core = build(SPEC["core"], "light")  # scales are theme-independent
light = build(SPEC["light"], "light")
# The component tokens live in their own top-level spec tree but are
# theme-independent measured geometry (header heights, button heights,
# field heights), so they hang off core.
core["component"] = build(SPEC["component"], "light")

# motion, as measured on the page: durations, easing curves, which properties
# transition, animations and @keyframes, and what prefers-reduced-motion:
# reduce changes (raw/motion.json, written by tools/capture/motion-probe.mjs;
# motion.py is the product-free mapping). A package that has not run the
# probe has no motion group.
if (RAW / "motion.json").exists():
    import sys
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
    import motion
    core["motion"], motion_not_core = motion.build(json.loads((RAW / "motion.json").read_text()))
    # what DTCG cannot carry (steps()/linear() easings, an easing left as var()) is listed, not dropped
    if motion_not_core:
        core.setdefault("$extensions", {}).setdefault("notTokenised", []).extend(motion_not_core)


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
         "$description": "The surface every www.gofundme.com consumer page paints: the light palette the :root-declared --hrt-* colour roles resolve to. No dark variant or theme toggle exists on the consumer site; the [data-theme=\"pro\"] layer is a declared GoFundMe Pro skin kept in raw/css-vars.json, never painted here. The /c/* pages are the WordPress content stack and /sign-in the auth boundary, recorded as measured component values."},
    ],
    "$metadata": {"tokenSetOrder": ["core", "light"]},
}
(HERE / "tokens.json").write_text(json.dumps(tokens, indent=2, ensure_ascii=False) + "\n")


def count(d):
    return sum(count(v) for v in d.values()) if isinstance(d, dict) and "$value" not in d else 1


print({k: count(v) for k, v in tokens.items() if k in ("core", "light")})
