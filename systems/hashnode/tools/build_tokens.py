#!/usr/bin/env python3
"""Build tokens.json (W3C DTCG, Tokens Studio multi-set layout) from the raw captures.

Sources, read from hashnode.com and townhall.hashnode.com (the hosted blog
engine — one design system, two surfaces):
  raw/css-vars.json          the custom properties the surfaces' stylesheets
                             declare — the Tailwind v4 @theme layer and the
                             hand-written semantic layer: the role set
                             (--background/--foreground, --primary/-secondary/
                             -accent/-muted/-card/-popover(+ foregrounds),
                             --destructive/-success/-warning families,
                             --disabled-foreground, --highlight, --toolbar,
                             --border/--input/--ring, --brand, --link,
                             --sidebar-*, --chart-1..5, --code-block(-fg|-muted),
                             --reading-text, --surface, --scrim, --selection,
                             --scroll-shadow, --scrollbar-thumb, --command),
                             the scene palettes (--ai-*, --buildful*, --pro-*,
                             --landing-*, --tod-* time-of-day hero), the
                             --elevation-* shadow stacks, the --font-* faces
                             (system stack + next/font Inter), the
                             --text-* ramp and prose roles, --radius(-xs),
                             --spacing, --container-*/--breakpoint-*, and the
                             motion vars; resolved in a probe carrying the
                             real sheets and the live pages' own classes
                             under <html class="light"> and again under
                             class="dark" (tools/capture/vars.mjs), and
                             binned theme / skins / app / vendor / utility /
                             tailwind
  raw/component-tokens.json  the token tree (tools/build_component_tokens.py): each leaf either
                             names a variable ("var") resolved per theme, or carries a measured
                             value and the measurement it came from ("source")
Every token carries $extensions.source: "css-var <name>" or "measured <where>".

hashnode.com boots html.light and the sidebar's own Theme menu (Light /
Dark / System) repaints html.dark; townhall.hashnode.com paints html.dark
under prefers-color-scheme (its toggle produced no repaint headless).
`.dark`/`:root.dark` re-point the semantic roles: `light` is the painted
default, `dark` the re-pointed set. --command is declared under .dark only
and exists in the dark set alone — never inferred for light.

Deterministic: same inputs, byte-identical output. Edit the raw inputs, never tokens.json.
"""
import json, pathlib, re, sys

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
sys.path.insert(0, str(HERE / "tools"))
import motion as motion_mod  # tools/motion.py -> core.motion (docs/decisions/0001)

V = json.loads((RAW / "css-vars.json").read_text())
SPEC = json.loads((RAW / "component-tokens.json").read_text())
MOTION = json.loads((RAW / "motion.json").read_text()) if (RAW / "motion.json").exists() else None

# Resolved declarations per theme. vars.mjs resolves each custom property on a
# probe document carrying the real sheets and the live page's own classes,
# once under <html class="light"> and once under class="dark" — the
# html.light/html.dark theme classes both surfaces paint. DECL[theme][name] is what the
# browser paints in that scope.
DECL = {
    "dark": {n: v.get("value", v["raw"]) for n, v in V["resolved"]["dark"].items()},
    "light": {n: v.get("value", v["raw"]) for n, v in V["resolved"]["light"].items()},
}


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
    # Chromium may resolve tint roles to color-mix(in oklch,
    # <colour>, transparent <p>%): a p% transparent share leaves the colour at
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
    # lab() as computed by Chromium on hashnode (CIE Lab: L 0-100, a, b,
    # optional /alpha). Converted through XYZ D50 -> sRGB.
    m = re.fullmatch(r"lab\(\s*([\d.]+)\s+(-?[\d.]+)\s+(-?[\d.]+)\s*(?:/\s*([\d.]+%?))?\s*\)", v)
    if m:
        L, A, B, a = m.groups()
        fy = (float(L) + 16) / 116
        fx, fz = fy + float(A) / 500, fy - float(B) / 200
        d = 6 / 29
        f = lambda t: t ** 3 if t > d else 3 * d ** 2 * (t - 4 / 29)
        x, y, z = f(fx) * 0.96422, f(fy) * 1.0, f(fz) * 0.82521
        # XYZ (D50) -> linear sRGB via the Bradford-adapted matrix
        r = 3.1338561 * x - 1.6168667 * y - 0.4906146 * z
        g = -0.9787684 * x + 1.9161415 * y + 0.0334540 * z
        b = 0.0719453 * x - 0.2289914 * y + 1.4052427 * z
        gam = lambda c: 12.92 * c if c <= 0.0031308 else 1.055 * c ** (1 / 2.4) - 0.055
        r, g, b = (max(0, min(255, round(gam(c) * 255))) for c in (r, g, b))
        if a is None:
            return "#%02x%02x%02x" % (r, g, b)
        al = float(a[:-1]) / 100 if a.endswith("%") else float(a)
        return "#%02x%02x%02x" % (r, g, b) if al == 1 else "rgba(%d, %d, %d, %g)" % (r, g, b, al)
    # oklch()/oklab() (the elevation and tint formulas): the full OKLab -> sRGB conversion,
    # so chroma and hue survive and L is not mapped linearly to grey.
    m = re.fullmatch(r"okl(ch|ab)\(\s*([\d.]+%?)\s+(none|-?[\d.]+%?)\s+(none|-?[\d.]+(?:deg)?)\s*(?:/\s*([\d.]+%?))?\s*\)", v)
    if m:
        import math
        kind, L, x, y, a = m.groups()
        L = float(L[:-1]) / 100 if L.endswith("%") else float(L)
        num = lambda w, scale: 0.0 if w == "none" else (float(w[:-1]) / 100 * scale if w.endswith("%") else float(w.replace("deg", "")))
        if kind == "ch":
            C, h = num(x, 0.4), num(y, 1)
            A, B = C * math.cos(math.radians(h)), C * math.sin(math.radians(h))
        else:
            A, B = num(x, 0.4), num(y, 0.4)
        l_ = (L + 0.3963377774 * A + 0.2158037573 * B) ** 3
        m_ = (L - 0.1055613458 * A - 0.0638541728 * B) ** 3
        s_ = (L - 0.0894841775 * A - 1.2914855480 * B) ** 3
        lin = (4.0767416621 * l_ - 3.3077115913 * m_ + 0.2309699292 * s_,
               -1.2684380046 * l_ + 2.6097574011 * m_ - 0.3413193965 * s_,
               -0.0041960863 * l_ - 0.7034186147 * m_ + 1.7076147010 * s_)
        gam = lambda c: 12.92 * c if c <= 0.0031308 else 1.055 * c ** (1 / 2.4) - 0.055
        r, g, b = (max(0, min(255, round(gam(max(0.0, c)) * 255))) for c in lin)
        al = 1 if a is None else (float(a[:-1]) / 100 if a.endswith("%") else float(a))
        return "#%02x%02x%02x" % (r, g, b) if al == 1 else "rgba(%d, %d, %d, %g)" % (r, g, b, al)
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
# The component tokens live in their own top-level spec tree but are
# theme-independent measured geometry (header height, sidebar width,
# dialog and card sizes), so they hang off core and reach both themes.
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
         "$description": "The painted default: hashnode.com and townhall.hashnode.com boot html.light — a white ground, near-black ink, the #2962ff brand/link blue."},
        {"id": "dark", "name": "Dark", "selectedTokenSets": {"core": "source", "dark": "enabled"},
         "$description": "The painted dark surface: hashnode.com's sidebar Theme menu (Light / Dark / System) flips html.dark; the blog engine paints the same classes under prefers-color-scheme. .dark/:root.dark re-point the roles — #0d0f14 ground, #e6e8eb ink, #6293ff blue. --command exists in dark only."},
    ],
    "$metadata": {"tokenSetOrder": ["core", "light", "dark"]},
}
(HERE / "tokens.json").write_text(json.dumps(tokens, indent=2, ensure_ascii=False) + "\n")


def count(d):
    return sum(count(v) for v in d.values()) if isinstance(d, dict) and "$value" not in d else 1


print({k: count(v) for k, v in tokens.items() if k in ("core", "light", "dark")})
