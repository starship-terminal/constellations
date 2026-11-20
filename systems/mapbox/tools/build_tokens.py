#!/usr/bin/env python3
"""Build tokens.json from the Mapbox public capture.

Sources, read from www.mapbox.com on 2026-11-18:
  raw/css-vars.json   Webflow custom properties, resolved in a probe document
  raw/components-computed.json   measured control sizes

The marketing site paints one light theme. Docs also set data-theme="light"
on the captured pages. No dark set is emitted.

Deterministic: same inputs, byte-identical output.
"""
import json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
V = json.loads((RAW / "css-vars.json").read_text())
DECL = {n: v.get("value", v.get("raw")) for n, v in V["resolved"]["light"].items() if v.get("kind") == "color" and isinstance(v.get("value"), str)}

# Webflow names that resolve to a solid colour, kept as the product's ramps.
RAMPS = {
    "gray": "--_colors---gray--gray",
    "blue": "--_colors---blue--blue",
    "primary": "--_colors---primary--primary",
    "green": "--_colors---green--green",
    "orange": "--_colors---orange--orange",
    "red": "--_colors---red--red",
    "yellow": "--_colors---yellow--yellow",
}


def leaf_color(name, source):
    val = DECL[name]
    return {"$value": val, "$type": "color", "$extensions": {"source": source}}


def dim(value, source):
    if isinstance(value, (int, float)):
        value = "%gpx" % value
    return {"$value": value, "$type": "dimension", "$extensions": {"source": source}}


def font_family(value, source):
    return {"$value": value, "$type": "fontFamily", "$extensions": {"source": source}}


def number(value, source):
    return {"$value": value, "$type": "number", "$extensions": {"source": source}}


core_color = {}
for ramp, prefix in RAMPS.items():
    steps = {}
    for step in ["5", "10", "20", "30", "40", "50", "60", "70", "80", "90"]:
        name = prefix + step
        if name not in DECL:
            continue
        steps[step] = leaf_color(name, f"css-var {name}")
    if ramp == "primary" and prefix in ("--_colors---primary--primary",) and "--_colors---primary--primary" in DECL:
        steps["base"] = leaf_color("--_colors---primary--primary", "css-var --_colors---primary--primary")
    core_color[ramp] = steps
if "--_colors---white--white" in DECL:
    core_color["white"] = {"0": leaf_color("--_colors---white--white", "css-var --_colors---white--white")}

# Text sizes the bundle declares, in px as the probe resolved them.
SIZE_NAMES = {
    "xxsmall": "--_text-styles---text-sizes--text-size-xxsmall",
    "xsmall": "--_text-styles---text-sizes--text-size-xsmall",
    "small": "--_text-styles---text-sizes--text-size-small",
    "regular": "--_text-styles---text-sizes--text-size-regular",
    "medium": "--_text-styles---text-sizes--text-size-medium",
    "large": "--_text-styles---text-sizes--text-size-large",
    "xlarge": "--_text-styles---text-sizes--text-size-xlarge",
    "xxlarge": "--_text-styles---text-sizes--text-size-xxlarge",
}
sizes = {}
for key, name in SIZE_NAMES.items():
    raw = V["resolved"]["light"].get(name, {})
    val = raw.get("value")
    if isinstance(val, str) and val.endswith("px"):
        sizes[key] = dim(val, f"css-var {name}")

# Measured display size from the home h1, recorded after the component pass.
comp = {}
comp_path = RAW / "components-computed.json"
if comp_path.exists():
    comp = json.loads(comp_path.read_text()).get("components", {})

def measured_px(key, prop, fallback=None):
    """A px reading from raw/components-computed.json. A missing one fails the build: the typed
    fallback used to stand in under the measured source."""
    st = (comp.get(key) or {}).get("states", {}).get("default", {})
    style = st.get("style") or {}
    val = style.get(prop)
    if isinstance(val, str) and re.fullmatch(r"-?\d+(\.\d+)?px", val):
        return val
    raise SystemExit(f"{key} default {prop} is not a px reading in raw/components-computed.json: {val!r}")

hero_size = measured_px("hero-h1", "fontSize", "56px")
hero_lh = measured_px("hero-h1", "lineHeight", "70px")
nav_h = measured_px("nav-signup", "height")
cta_h = measured_px("cta-primary", "height")
cta_radius = measured_px("cta-primary", "borderTopLeftRadius", "100px")

light = {
    "background": {
        "page": leaf_color("--_color-mode---background--cm_bg-neutral-01", "css-var --_color-mode---background--cm_bg-neutral-01"),
        "surface": leaf_color("--_color-mode---background--cm_bg-neutral-02", "css-var --_color-mode---background--cm_bg-neutral-02"),
        "raised": leaf_color("--_color-mode---background--cm_bg-neutral-03", "css-var --_color-mode---background--cm_bg-neutral-03"),
        "accent": leaf_color("--_colors---blue--blue50", "css-var --_colors---blue--blue50"),
        "accentHover": leaf_color("--_colors---blue--blue40", "css-var --_colors---blue--blue40; nav sign-up hover painted #3195ff, which is blue40"),
    },
    "text": {
        "primary": leaf_color("--_color-mode---text--cm_text-neutral-01", "css-var --_color-mode---text--cm_text-neutral-01"),
        "secondary": leaf_color("--_color-mode---text--cm_text-neutral-02", "css-var --_color-mode---text--cm_text-neutral-02"),
        "muted": leaf_color("--_color-mode---text--cm_text-neutral-03", "css-var --_color-mode---text--cm_text-neutral-03"),
        "disabled": leaf_color("--_color-mode---text--cm_text-neutral-05", "css-var --_color-mode---text--cm_text-neutral-05"),
        "onAccent": leaf_color("--_colors---white--white", "css-var --_colors---white--white; painted on the blue sign-up pill"),
        "link": leaf_color("--_colors---blue--blue50", "css-var --_colors---blue--blue50"),
    },
    "border": {
        "default": leaf_color("--_colors---gray--gray20", "css-var --_colors---gray--gray20"),
        "strong": leaf_color("--_colors---gray--gray40", "css-var --_colors---gray--gray40"),
        "focus": leaf_color("--_colors---blue--blue50", "css-var --_colors---blue--blue50"),
    },
    "status": {
        "success": leaf_color("--_colors---green--green50", "css-var --_colors---green--green50"),
        "warning": leaf_color("--_colors---yellow--yellow50", "css-var --_colors---yellow--yellow50"),
        "danger": leaf_color("--_colors---red--red50", "css-var --_colors---red--red50"),
        "info": leaf_color("--_colors---blue--blue50", "css-var --_colors---blue--blue50"),
    },
}
if nav_h:
    light["control"] = {
        "navHeight": dim(nav_h, "computed nav a.button.is-nav height on www.mapbox.com"),
    }
    if cta_h:
        light["control"]["ctaHeight"] = dim(cta_h, "computed .button_inner height on the home hero CTA")
    if cta_radius:
        light["control"]["pillRadius"] = dim(cta_radius, "computed border-radius on .button_inner (pill)")

core = {
    "color": core_color,
    "font": {
        "family": {
            "display": font_family('Cera Pro, "Trebuchet MS", sans-serif', "computed font-family on the home h1"),
            "body": font_family("Open Sans, sans-serif", "@font-face on docs.mapbox.com and the marketing bundle"),
        },
        "size": sizes,
        "weight": {
            "regular": number(400, "@font-face Cera pro 400"),
            "medium": number(500, "@font-face Cera pro 500"),
            "bold": number(700, "@font-face Cera pro 700 and --_heading-styles---font-weight: 700"),
        },
    },
}
if hero_size:
    core["font"]["size"]["display"] = dim(hero_size, "computed font-size on the home h1")
if hero_lh:
    core["font"]["lineHeight"] = {"display": dim(hero_lh, "computed line-height on the home h1")}

tokens = {
    "core": core,
    "light": light,
    "$themes": [{
        "id": "light",
        "name": "Light",
        "selectedTokenSets": {"core": "source", "light": "enabled"},
        "$description": "The only theme the captured public pages paint. The nav carries color-mode-light. Docs set data-theme=light.",
    }],
    "$metadata": {"tokenSetOrder": ["core", "light"]},
}
(HERE / "tokens.json").write_text(json.dumps(tokens, indent=2, ensure_ascii=False) + "\n")
print("wrote tokens.json", "colors", sum(len(v) for v in core_color.values()), "sizes", len(sizes))
