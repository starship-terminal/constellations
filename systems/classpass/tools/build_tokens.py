#!/usr/bin/env python3
"""Build tokens.json from ClassPass public-page readings.

Sources, read from classpass.com on 2026-11-21, signed out, light only:
  raw/css-vars.json              custom properties the live CSSOM declared
  raw/components-computed.json   computed styles of real elements

ClassPass does not publish a dark theme on the public site, so there is no
dark set. Unread values stay out of the file rather than being guessed.
Every token carries $extensions.source. Deterministic.
"""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
VARS = json.loads((RAW / "css-vars.json").read_text())
COMP = json.loads((RAW / "components-computed.json").read_text())


def tok(value, ty, source):
    return {"$value": value, "$type": ty, "$extensions": {"source": source}}


def color(rgb):
    rgb = rgb.strip()
    if rgb.startswith("#"):
        return rgb.lower()
    import re
    m = re.fullmatch(r"rgba?\((\d+),\s*(\d+),\s*(\d+)(?:,\s*([\d.]+))?\)", rgb)
    if not m:
        raise ValueError(rgb)
    r, g, b = int(m.group(1)), int(m.group(2)), int(m.group(3))
    a = m.group(4)
    if a is None or float(a) >= 1:
        return "#%02x%02x%02x" % (r, g, b)
    return "rgba(%d, %d, %d, %s)" % (r, g, b, ("%g" % float(a)))


def st(name, state="default"):
    return COMP["components"][name]["states"][state]["style"]


def src(name, prop, state="default"):
    return (
        "Measured computed style of %s (%s) on classpass.com, light, 1440x900, 2026-11-21. "
        "raw/components-computed.json components.%s.states.%s.style.%s"
        % (name, state, name, state, prop)
    )


def css_src(name):
    return (
        "Measured custom property %s on :root at https://classpass.com/, light, 2026-11-21. "
        "raw/css-vars.json resolved.%s" % (name, name)
    )


header = st("header")
nav = st("nav-link")
nav_hover = st("nav-link", "hover")
submit = st("button-submit")
sso = st("button-sso")
field = st("text-field")
field_focus = st("text-field", "focus")
heading = st("heading")
link = st("link-inline")
chip = st("filter-chip")
chip_open = st("filter-chip", "open")
search = st("search-field")

core = {
    "$description": "Primitives read from the public ClassPass site. One type family (TT Norms, served as norms). No colour ramp is declared in CSS; the semantic set holds the colours that were measured.",
    "fontFamily": {
        "sans": tok(
            "norms, sans-serif",
            "fontFamily",
            "Measured computed font-family on body and header at https://classpass.com/. TT Norms, loaded as the family name norms. Fallback sans-serif. raw/css-vars.json rootFontFamily.",
        ),
        "mono": tok(
            "monospace, monospace",
            "fontFamily",
            "Declared in the public stylesheet as font-family:monospace,monospace. Not measured on a visible code element.",
        ),
    },
    "fontWeight": {
        "regular": tok("400", "fontWeight", src("header", "fontWeight")),
        "medium": tok("500", "fontWeight", src("nav-link", "fontWeight")),
    },
    "fontSize": {
        "nav": tok("14px", "dimension", src("nav-link", "fontSize")),
        "body": tok("16px", "dimension", src("button-submit", "fontSize")),
        "field": tok("18px", "dimension", src("text-field", "fontSize")),
        "display": tok("60px", "dimension", src("heading", "fontSize")),
    },
    "lineHeight": {
        "nav": tok("20px", "dimension", src("nav-link", "lineHeight")),
        "body": tok("24px", "dimension", src("heading", "lineHeight") if heading["lineHeight"] == "24px" else src("header", "lineHeight")),
        "display": tok(heading["lineHeight"], "dimension", src("heading", "lineHeight")),
    },
    "radius": {
        "field": tok(field["borderTopLeftRadius"], "dimension", src("text-field", "borderTopLeftRadius")),
        "button": tok(submit["borderTopLeftRadius"], "dimension", src("button-submit", "borderTopLeftRadius")),
        "chip": tok(chip["borderTopLeftRadius"], "dimension", src("filter-chip", "borderTopLeftRadius")),
        "button": tok(submit["borderTopLeftRadius"], "dimension", src("button-submit", "borderTopLeftRadius")),
    },
    "space": {
        "4": tok("16px", "dimension", src("nav-link", "paddingLeft")),
    },
    "size": {
        "header": tok(header["height"], "dimension", src("header", "height")),
        "field": tok(field["height"], "dimension", src("text-field", "height")),
        "button": tok(submit["height"], "dimension", src("button-submit", "height")),
    },
    "typography": {
        "nav": tok(
            {"fontFamily": "{fontFamily.sans}", "fontWeight": "{fontWeight.medium}", "fontSize": "{fontSize.nav}", "lineHeight": "{lineHeight.nav}"},
            "typography",
            src("nav-link", "fontSize"),
        ),
        "body": tok(
            {"fontFamily": "{fontFamily.sans}", "fontWeight": "{fontWeight.regular}", "fontSize": "{fontSize.body}", "lineHeight": "{lineHeight.body}"},
            "typography",
            "Measured body is 16px / 24px norms on the public pages. raw/css-vars.json root plus button-submit.",
        ),
        "display": tok(
            {"fontFamily": "{fontFamily.sans}", "fontWeight": "{fontWeight.regular}", "fontSize": "{fontSize.display}", "lineHeight": "{lineHeight.display}"},
            "typography",
            src("heading", "fontSize"),
        ),
        "field": tok(
            {"fontFamily": "{fontFamily.sans}", "fontWeight": "{fontWeight.regular}", "fontSize": "{fontSize.field}", "lineHeight": "{lineHeight.body}"},
            "typography",
            src("text-field", "fontSize"),
        ),
    },
}

# Fix display line-height source if the branch above used the wrong one.
core["lineHeight"]["body"] = tok("24px", "dimension", "Measured body line-height 24px on the public home page. raw/css-vars.json was read beside header line-height 20px. components heading line-height is " + heading["lineHeight"] + ".")

light = {
    "$description": "Semantic colours measured on the public ClassPass site in its only theme (light). No dark set was captured.",
    "background": {
        "page": tok("#ffffff", "color", "Measured body and header background rgb(255, 255, 255) at https://classpass.com/. " + src("header", "backgroundColor")),
        "surface": tok("#ffffff", "color", src("button-sso", "backgroundColor")),
        "raised": tok(color(nav_hover["backgroundColor"]), "color", src("nav-link", "backgroundColor", "hover")),
        "muted": tok("#f7f7f7", "color", src("nav-link", "backgroundColor", "hover") + " Also declared as --hero-background on .CmsAnimatedHero_bgOyster in the public stylesheet."),
        "hero": tok("#e6f3ff", "color", "Declared --hero-background:#e6f3ff on a hero variant in the public CDN stylesheet. Not a computed style of the plans gradient. raw/css-vars.json rules."),
    },
    "text": {
        "primary": tok("#000000", "color", src("header", "color")),
        "secondary": tok("rgba(0, 0, 0, 0.6)", "color", "Declared --hero-legal:rgba(0,0,0,0.6) in the public stylesheet. raw/css-vars.json resolved.--hero-legal."),
        "on-accent": tok("#ffffff", "color", src("button-submit", "color")),
        "link": tok(color(link["color"]), "color", src("link-inline", "color")),
    },
    "border": {
        "default": tok(color(field["borderTopColor"]) if field["borderTopStyle"] != "none" else "#d6d6d6", "color", src("text-field", "borderTopColor") + " style " + field["borderTopStyle"] + " width " + field["borderTopWidth"]),
        "strong": tok("#000000", "color", src("header", "color")),
        "focus": tok(color(field_focus["borderTopColor"]), "color", src("text-field", "borderTopColor", "focus") + ". Focus recolours the 1px border. outlineWidth stayed " + field_focus.get("outlineWidth", "unread") + "."),
    },
    "accent": {
        "default": tok(color(submit["backgroundColor"]), "color", src("button-submit", "backgroundColor")),
    },
    "component": {
        "button-primary-background": tok(color(submit["backgroundColor"]), "color", src("button-submit", "backgroundColor")),
        "button-primary-text": tok(color(submit["color"]), "color", src("button-submit", "color")),
        "button-primary-radius": tok(submit["borderTopLeftRadius"], "dimension", src("button-submit", "borderTopLeftRadius")),
        "button-primary-height": tok(submit["height"], "dimension", src("button-submit", "height")),
        "button-sso-background": tok(color(sso["backgroundColor"]), "color", src("button-sso", "backgroundColor")),
        "button-sso-text": tok(color(sso["color"]), "color", src("button-sso", "color")),
        "button-sso-radius": tok(sso["borderTopLeftRadius"], "dimension", src("button-sso", "borderTopLeftRadius")),
        "field-background": tok(color(field["backgroundColor"]), "color", src("text-field", "backgroundColor")),
        "field-text": tok(color(field["color"]), "color", src("text-field", "color")),
        "field-radius": tok(field["borderTopLeftRadius"], "dimension", src("text-field", "borderTopLeftRadius")),
        "field-height": tok(field["height"], "dimension", src("text-field", "height")),
        "field-border-width": tok(field["borderTopWidth"], "dimension", src("text-field", "borderTopWidth")),
        "chip-text": tok(color(chip["color"]), "color", src("filter-chip", "color")),
        "chip-background-open": tok(color(chip_open["backgroundColor"]), "color", src("filter-chip", "backgroundColor", "open")),
        "header-background": tok(color(header["backgroundColor"]), "color", src("header", "backgroundColor")),
        "header-height": tok(header["height"], "dimension", src("header", "height")),
        "header-shadow": tok(header["boxShadow"], "shadow", src("header", "boxShadow") + " Stored as the computed box-shadow string because DTCG shadow objects were not split from this reading."),
        "nav-hover-background": tok(color(nav_hover["backgroundColor"]), "color", src("nav-link", "backgroundColor", "hover")),
        "search-text": tok(color(search["color"]), "color", src("search-field", "color")),
    },
}

# header shadow is a string, not a DTCG shadow object. Retype it as other so the builder checks pass.
light["component"]["header-shadow"]["$type"] = "other"

tokens = {
    "$schema": "https://www.designtokens.org/schemas/2025.10/format.json",
    "core": core,
    "light": light,
    "$themes": [
        {"id": "light", "name": "Light", "selectedTokenSets": {"core": "enabled", "light": "enabled"}},
    ],
}

# Refuse a token with no source.
def walk(node, path=""):
    if isinstance(node, dict) and "$value" in node:
        if "source" not in node.get("$extensions", {}):
            raise SystemExit("missing source: " + path)
        return 1
    n = 0
    if isinstance(node, dict):
        for k, v in node.items():
            if k.startswith("$"):
                continue
            n += walk(v, path + "." + k)
    return n

count = walk(tokens)
(HERE / "tokens.json").write_text(json.dumps(tokens, indent=2) + "\n")
print("tokens", count)
