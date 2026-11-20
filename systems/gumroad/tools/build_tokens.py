#!/usr/bin/env python3
"""Build tokens.json (W3C DTCG, Tokens Studio multi-set layout) from the raw captures.

Sources, read from gumroad.com:
  raw/css-vars.json          the custom properties gumroad.com's stylesheets
                             declare — the Tailwind v4 @theme layer and the
                             hand-written semantic layer: the --pink/--purple/
                             --green/--orange/--red/--yellow brand set, the
                             `R G B` channel-triplet roles (--accent/--color/
                             --filled/--primary/--success/--warning/--danger/
                             --info/--active-bg/--contrast-*/--neutral-*), the
                             --color-* resolved wrappers, --body-bg, the
                             --border/--border-alpha shorthand pair, the
                             --box-shadow-1/2 hard offset shadows, the
                             --spacer-*/--border-radius-*/--text-* scales,
                             --font-family (ABC Favorit) and the motion and
                             z-index vars; resolved in a probe carrying the
                             real sheets under emulated colour-scheme light
                             and again dark — the media the product's own
                             @media (prefers-color-scheme:dark) :root block
                             answers (tools/capture/vars.mjs), and binned
                             theme / darkscope / app / vendor / utility /
                             tailwind
  raw/component-tokens.json  the token tree (tools/build_component_tokens.py): each leaf either
                             names a variable ("var") resolved per theme, or carries a measured
                             value and the measurement it came from ("source")
Every token carries $extensions.source: "css-var <name>" or "measured <where>".

gumroad.com declares `color-scheme: light dark` and answers the OS/browser
scheme — there is no in-page toggle: `light` and `dark` are both painted by
the product's own media block. The product subdomain's inline :root pins a
light palette, so a <creator>.gumroad.com page never darkens — captured as
the product-light/product-dark resolutions in css-vars.json, not a third
token theme.

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
# probe document carrying the real sheets, once under emulated colour-scheme
# light and once under dark — the @media (prefers-color-scheme:*) mechanism
# the live page answers. DECL[theme][name] is what the browser paints in that
# scope.
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
    # Achromatic oklch()/oklab() (the elevation and tint formulas): L 0 is
    # black, L 1 is white, the trailing /a is the alpha.
    m = re.fullmatch(r"okl(?:ch|ab)\(\s*([\d.]+)\s+[\d.]+\s+(?:none|[-\d.]+)\s+(?:none\s+)?(?:/\s*([\d.]+))?\s*\)", v)
    if m:
        lvl = round(float(m.group(1)) * 255)
        a = float(m.group(2) or 1)
        return "#%02x%02x%02x" % (lvl, lvl, lvl) if a == 1 else "rgba(%d, %d, %d, %g)" % (lvl, lvl, lvl, a)
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


SHADOW_COLOUR = re.compile(r"rgba?\([^()]*\)|#(?:[0-9a-fA-F]{3,4}|[0-9a-fA-F]{6}|[0-9a-fA-F]{8})")
SHADOW_LENGTH = re.compile(r"-?(?:\d+(?:\.\d+)?|\.\d+)(?:px|rem)|-?0(?:\.0+)?")


def parse_shadow(val, path=""):
    """A box-shadow list as DTCG layers. Top-level commas split layers (commas inside rgb() stay whole); each
    layer is whole space-separated pieces: at most one `inset`, exactly one colour (rgb()/rgba() or a 3, 4, 6
    or 8 digit hex), and two to four lengths (blur and spread default to 0px, a unitless 0 is 0px). Each piece
    must match as a whole, so `1px2px` or `#12345` refuses the build: a layer that cannot be read is never
    dropped, split into invented lengths or given a guessed colour."""
    layers = []
    for part in re.split(r",\s*(?![^(]*\))", val.strip()):
        pieces = re.findall(r"[^\s(]+\([^)]*\)|\S+", part.strip())
        inset, colours, lengths = 0, [], []
        for x in pieces:
            if x == "inset":
                inset += 1
            elif SHADOW_COLOUR.fullmatch(x):
                colours.append(x)
            elif SHADOW_LENGTH.fullmatch(x):
                lengths.append(x)
            else:
                raise ValueError(f"{path}: cannot read box-shadow layer {part!r} (piece {x!r})")
        if inset > 1 or len(colours) != 1 or not 2 <= len(lengths) <= 4:
            raise ValueError(f"{path}: cannot read box-shadow layer {part!r}")
        lengths = [x if x.endswith(("px", "rem")) else "0px" for x in lengths] + ["0px"] * (4 - len(lengths))
        layer = {"color": norm_color(colours[0]), "offsetX": lengths[0], "offsetY": lengths[1],
                 "blur": lengths[2], "spread": lengths[3]}
        if inset:
            layer["inset"] = True
        layers.append(layer)
    return layers


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
    if ty == "shadow" and isinstance(val, str):
        val = parse_shadow(val, path)
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
# theme-independent measured geometry (header height, card sizes), so
# they hang off core and reach both themes. Merged, not replaced:
# build_component_tokens.py also emits declared component constants
# (--form-element-height, --border-width, --button-hover-offset) into
# core.component — overwriting would drop them.
core.setdefault("component", {}).update(build(SPEC["component"], "light"))
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
         "$description": "The light painted surface — gumroad.com's default under light colour schemes: a warm off-white ground (#f4f4f0), black ink, the pink accent (#ff90e8), hard 4px offset shadows."},
        {"id": "dark", "name": "Dark", "selectedTokenSets": {"core": "source", "dark": "enabled"},
         "$description": "The dark painted surface: @media (prefers-color-scheme:dark) re-points the channel roles — #242423 ground, #ddd ink, the pink accent unchanged, borders fade to alpha .35 and the hard shadows flip to light. Painted by the OS/browser scheme; no in-page toggle."},
    ],
    "$metadata": {"tokenSetOrder": ["core", "light", "dark"]},
}


def count(d):
    return sum(count(v) for v in d.values()) if isinstance(d, dict) and "$value" not in d else 1


if __name__ == "__main__":
    (HERE / "tokens.json").write_text(json.dumps(tokens, indent=2, ensure_ascii=False) + "\n")
    print({k: count(v) for k, v in tokens.items() if k in ("core", "light", "dark")})
