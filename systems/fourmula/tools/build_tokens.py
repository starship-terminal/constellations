#!/usr/bin/env python3
"""Build tokens.json (W3C DTCG, Tokens Studio multi-set layout) from the raw captures.

Sources, read from fourmula.ai on 2026-11-16:
  raw/css-vars.json          the custom properties the fourmula.ai Webflow
                             bundle declares — the fluid --_fonts---* type
                             ramp, the --_font-family---* face and weights,
                             the --fonts-* alpha ink ramp, the themed
                             --mainbg/--secondbg/--lines/--menu/--menu-colors/
                             --dots-pattern/--mainbg-gradient colours and the
                             --user-zoom scale factor — resolved on a probe
                             document (tools/capture/vars.mjs) once with
                             class="body dark" (the site's inverted name for
                             its light paint, isDarkMode=true) and once with
                             class="body" (the dark paint)
  raw/css-vars-app.json      app.fourmula.ai's separate Tailwind v4 @theme
                             layer (--color-base-*/--color-accent-*, --text-*,
                             --radius-*, --spacing, --ease-*, --blur-*,
                             --container-*), resolved on the app's own probe;
                             the app ships dark only, so both probe paints
                             resolve identically
  raw/component-tokens.json  the token tree (tools/build_component_tokens.py): each leaf either
                             names a variable ("var") resolved per theme, or carries a measured
                             value and the measurement it came from ("source")
  raw/motion.json            measured motion (tools/capture/motion-probe.mjs), folded into
                             core.motion by tools/motion.py
Every token carries $extensions.source: "css-var <name>" or "measured <where>".

fourmula.ai's marketing site paints two themes behind a header toggle that
writes localStorage isDarkMode and flips `dark` on <body> — the class names
are inverted against the paint (`.body.dark` is the light surface, the
first-visit default; plain `.body` is the dark one). The `light` set holds
the .body.dark resolutions and `dark` the .body ones. app.fourmula.ai's
signed-out /start, /auth and /project/create-pdp are a dark-only
Next.js/Tailwind app whose measured values live under component.app.*.

Deterministic: same inputs, byte-identical output. Edit the raw inputs, never tokens.json.
"""
import json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
V = json.loads((RAW / "css-vars.json").read_text())
SPEC = json.loads((RAW / "component-tokens.json").read_text())

# Resolved declarations per theme. vars.mjs resolves each custom property on a
# probe document once light (data-mode="light") and once dark
# (data-mode="dark"), so DECL[theme][name] is what the browser paints in that
# scope. A name declared only on :root resolves the same in both.
DECL = {t: {n: v.get("value", v["raw"]) for n, v in V["resolved"][t].items()} for t in ("light", "dark")}


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
    return {k: build(v, theme, f"{path}.{k}" if path else k) for k, v in node.items() if not k.startswith("_")}


core = build(SPEC["core"], "light")  # scales are theme-independent
light = build(SPEC["light"], "light")
dark = build(SPEC["dark"], "dark")
# The component tokens live in their own top-level spec tree but are
# theme-independent measured geometry (header heights, field sizes, card
# radii, the app's measured colours), so they hang off core and reach both
# themes.
core["component"] = build(SPEC["component"], "light")

# motion, as measured on the page: durations, easing curves, which properties
# transition, animations and @keyframes, and what prefers-reduced-motion:
# reduce changes (raw/motion.json, written by tools/capture/motion-probe.mjs;
# motion.py is the product-free mapping). A package that has not run the
# probe has no motion group.
not_tokenised = []
if (RAW / "motion.json").exists():
    import sys
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
    import motion
    core["motion"], motion_not = motion.build(json.loads((RAW / "motion.json").read_text()))
    not_tokenised += motion_not

# Values the captures carry that no token should pretend to be. Finsweet's
# consent-layer custom properties and Webflow's platform internals are vendor
# plumbing, not the product's design; the media-query copies of the type ramp
# are the same declared steps at other viewports; and the rotating-word /
# dots-field mechanics are runtime plumbing recorded in raw/css-vars.json.
not_tokenised += [
    {"name": "--_font-family---size", "value": "0px",
     "why": "a Webflow placeholder variable that stays 0px; not a font size"},
    {"name": "@media copies of --_fonts---*", "value": "16 names",
     "why": "the same declared steps under the <=991px/<=767px rules; raw/css-vars.json keeps every context, and the mobile pass measures what 390px paints"},
    {"name": "Finsweet consent --fs-cc-*", "value": "the .cookies layer's variables",
     "why": "vendor (@finsweet cookie-consent) variables, not product design tokens; the layer itself is measured under component.marketing"},
    {"name": "--tx/--ty/--dot-size/--dot-gap", "value": "hero slider + dots field",
     "why": "runtime translate/density plumbing for the logo strips and dot pattern; recorded under core.heroSlider as raw values, not scales"},
]
core.setdefault("$extensions", {})["notTokenised"] = not_tokenised


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
         "$description": "fourmula.ai's light paint: <body class=\"body dark\"> (localStorage isDarkMode=true, the first-visit default). The class name is inverted against the paint — `.dark` styles the white surface with #020108 ink. The app.fourmula.ai signed-out surfaces are a separate dark-only Tailwind app under component.app.*."},
        {"id": "dark", "name": "Dark", "selectedTokenSets": {"core": "source", "dark": "enabled"},
         "$description": "fourmula.ai's dark paint: plain <body class=\"body\"> (isDarkMode=false): the #020108 field with white ink and white-filled CTAs — the same vars resolved under the .body declarations."},
    ],
    "$metadata": {"tokenSetOrder": ["core", "light", "dark"]},
}
(HERE / "tokens.json").write_text(json.dumps(tokens, indent=2, ensure_ascii=False) + "\n")


def count(d):
    return sum(count(v) for v in d.values()) if isinstance(d, dict) and "$value" not in d else 1


print({k: count(v) for k, v in tokens.items() if k in ("core", "light", "dark")})
