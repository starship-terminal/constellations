#!/usr/bin/env python3
"""Build tokens.json (W3C DTCG, Tokens Studio multi-set layout) from the raw captures.

Sources, read from front.com's public surfaces:
  raw/css-vars.json          the custom properties the surfaces' stylesheets
                             declare and resolve: app.frontapp.com's signin
                             shell (--color-primitive-* ramps + the
                             --color-*/semantics, resolved under
                             data-theme=light and =dark), the Froyo token
                             sheet companion.frontapp.com ships (@layer
                             tokens --colors-*/--sizes-*/--spacing-*/--radii-*/
                             --font-*/--shadows-*/--easings-*/--durations-*,
                             with [data-theme] semantic repointings),
                             help.front.com's inline :root block, and
                             dev.frontapp.com's ReadMe vendor vars
  raw/css-classes.json       front.com's compiled design layer: the bespoke
                             semantic classes (.surface-*/.text-*/.button-*)
                             per [data-theme] section theme, the hue-utility
                             palette, and the type/radius/motion scales
  raw/component-tokens.json  the token tree (tools/build_component_tokens.py):
                             each leaf either names a resolved variable
                             ("var") or carries a value and the evidence it
                             came from ("source")
Every token carries $extensions.source.

Nine token sets: core (scales + ramps), violet/light/gray (the marketing
site's three section themes), app/dark (the signin shell's --color-* layer),
companion/companionDark (the Froyo messenger layer's [data-theme] semantics),
and help (the Knowledge Base :root block).

Deterministic: same inputs, byte-identical output. Edit the raw inputs, never tokens.json.
"""
import json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
V = json.loads((RAW / "css-vars.json").read_text())
CL = json.loads((RAW / "css-classes.json").read_text())
SPEC = json.loads((RAW / "component-tokens.json").read_text())

# Resolved declarations per set. The marketing sets and component leaves are
# literal; the app/dark/help sets resolve their `var` leaves against the
# live-page resolutions captured in raw/css-vars.json.
RES = V.get("resolved", {})
DECL = {
    "core": {},
    "violet": {}, "light": {}, "gray": {},
    "app": {n: v.get("value", v.get("raw")) for n, v in RES.get("app", {}).items()},
    "dark": {n: v.get("value", v.get("raw")) for n, v in RES.get("appDark", {}).items()},
    "companion": {}, "companionDark": {},
    "help": {n: v.get("value", v.get("raw")) for n, v in RES.get("help", {}).items()},
    "component": {},
}
SETS = ["core", "violet", "light", "gray", "app", "dark", "companion", "companionDark", "help"]


def norm_color(v):
    """#rgb, #rrggbb, #rrggbbaa, rgb(), rgba(), hsla() -> #rrggbb or rgba(r, g, b, a)."""
    v = v.strip().lower()
    # Tailwind-compiled utilities leave var() inside the colour: read the
    # declared fallback (rgb(240 244 254/var(--tw-bg-opacity,1)) -> .../1).
    v = re.sub(r"var\(--[\w-]+\s*,\s*([\d.]+%?)\)", r"\1", v)
    v = re.sub(r"var\(--[\w-]+\)", "1", v)
    if v == "transparent":
        return "rgba(0, 0, 0, 0)"
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
    m = re.fullmatch(r"okl(?:ch|ab)\(\s*([\d.]+)\s+[\d.]+\s+(?:none|[-\d.]+)\s+(?:none\s+)?(?:/\s*([\d.]+))?\s*\)", v)
    if m:
        lvl = round(float(m.group(1)) * 255)
        a = float(m.group(2) or 1)
        return "#%02x%02x%02x" % (lvl, lvl, lvl) if a == 1 else "rgba(%d, %d, %d, %g)" % (lvl, lvl, lvl, a)
    raise ValueError("not a colour: " + v)


DIM = re.compile(r"-?(?:\d+\.?\d*|\.\d+)(px|rem)")


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
        bucket = spec.get("resolve", theme)
        if name not in DECL[bucket]:
            raise KeyError(f"{path}: {name} is not a resolved variable in raw/css-vars.json ({bucket})")
        val = DECL[bucket][name]
        src = f"css-var {name} ({bucket})"
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


LEAF_KEYS = {"value", "var", "type", "source", "description", "resolve", "responsive", "angle"}


def build(node, theme, path=""):
    if isinstance(node, dict) and "type" in node and ("value" in node or "var" in node):
        # A leaf that also holds child tokens must never be emitted quietly:
        # the children would drop out of tokens.json with no trace.
        extra = set(node) - LEAF_KEYS
        if extra:
            raise ValueError(f"{path}: token leaf also holds child tokens {sorted(extra)} — keep base values and variants as separate leaves")
        return leaf(path, node, theme)
    if isinstance(node, dict) and "$value" in node:
        return node  # already a DTCG leaf (typography composites)
    return {k: build(v, theme, f"{path}.{k}" if path else k) for k, v in node.items() if not k.startswith("_")}


sets = {s: build(SPEC[s], s) for s in SETS}
# The component tokens live in their own top-level spec tree but are
# theme-independent measured geometry and paint, so they hang off core and
# reach every theme.
sets["core"]["component"] = build(SPEC["component"], "component")


# every alias must point at a token that exists
def tokens_of(tree, prefix=""):
    for k, v in tree.items():
        if isinstance(v, dict) and "$value" in v:
            yield prefix + k, v
        elif isinstance(v, dict):
            yield from tokens_of(v, prefix + k + ".")


def aliases(v):
    if isinstance(v, str):
        return re.findall(r"\{([^{}]+)\}", v)
    if isinstance(v, dict):
        return [a for x in v.values() for a in aliases(x)]
    if isinstance(v, list):
        return [a for x in v for a in aliases(x)]
    return []


NAMES = {n for n, _ in tokens_of(sets["core"])}
for s in SETS[1:]:
    names_s = NAMES | {n for n, _ in tokens_of(sets[s])}
    for n, t in list(tokens_of(sets[s])):
        for a in aliases(t["$value"]):
            if a not in names_s:
                raise KeyError(f"{s}.{n}: alias {{{a}}} points at nothing")

tokens = dict(sets)
tokens["$themes"] = [
    {"id": "violet", "name": "Marketing: dark violet", "selectedTokenSets": {"core": "source", "violet": "enabled"},
     "$description": "front.com's signature plum sections: [data-theme=theme-dark-violet] (the site's default) — surface-l0 #300c41 through surface-highlight citron, with the button layer repointed at the citron primary."},
    {"id": "light", "name": "Marketing: white", "selectedTokenSets": {"core": "source", "light": "enabled"},
     "$description": "front.com's [data-theme=theme-white] sections — white/l0 surfaces, ink text, the violet primary button."},
    {"id": "gray", "name": "Marketing: gray", "selectedTokenSets": {"core": "source", "gray": "enabled"},
     "$description": "front.com's [data-theme=theme-gray] sections — the same roles as white with the l0/l1 steps swapped and different disabled shades."},
    {"id": "app", "name": "App shell: light", "selectedTokenSets": {"core": "source", "app": "enabled"},
     "$description": "app.frontapp.com's signin shell under data-theme=light — the --color-* semantic layer resolved live on the page."},
    {"id": "dark", "name": "App shell: dark", "selectedTokenSets": {"core": "source", "dark": "enabled"},
     "$description": "app.frontapp.com's signin shell under [data-theme=\"dark\"] — the same --color-* names repointed, resolved live (front-theme-preference + prefers-color-scheme)."},
    {"id": "companion", "name": "Froyo messenger: light", "selectedTokenSets": {"core": "source", "companion": "enabled"},
     "$description": "The --colors-* semantic layer Front's Companion messenger ships (@layer tokens, [data-theme=\"light\"] repointings resolved through the same sheet)."},
    {"id": "companionDark", "name": "Froyo messenger: dark", "selectedTokenSets": {"core": "source", "companionDark": "enabled"},
     "$description": "The same --colors-* semantics under [data-theme=\"dark\"] — declared, resolved through the Froyo sheet's dark ramps."},
    {"id": "help", "name": "Help centre", "selectedTokenSets": {"core": "source", "help": "enabled"},
     "$description": "help.front.com's :root block — Front's own Knowledge Base product vars (--primary-color, --gray-shade*, --article-*, button/field vars)."},
]
tokens["$metadata"] = {"tokenSetOrder": SETS}
(HERE / "tokens.json").write_text(json.dumps(tokens, indent=2, ensure_ascii=False) + "\n")


def count(d):
    return sum(count(v) for v in d.values()) if isinstance(d, dict) and "$value" not in d else 1


print({k: count(v) for k, v in tokens.items() if k in SETS})
