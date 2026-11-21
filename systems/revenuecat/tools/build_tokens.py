#!/usr/bin/env python3
"""Build tokens.json from the public RevenueCat readings.

Sources, read on 2026-11-21 from www.revenuecat.com (signed out) and the public
docs at /docs:
  raw/css-vars.json              custom properties declared on :root
  raw/components-computed.json   computed styles of real controls
  raw/layout.json                header height and viewport at 1440, 1024, 390

Marketing ships one light theme. Docs ship a second theme, recorded as `dark`
from the live toggle on /docs. A value that was not read is left out.
"""
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
CSS = json.loads((RAW / "css-vars.json").read_text())
COMP = json.loads((RAW / "components-computed.json").read_text())
LAYOUT = json.loads((RAW / "layout.json").read_text())
RES = CSS["resolved"]


def tok(value, kind, source):
    return {"$value": value, "$type": kind, "$extensions": {"source": source}}


def hex_of(rgb):
    m = re.fullmatch(r"rgb\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*\)", rgb.strip())
    if not m:
        return None
    return "#{:02x}{:02x}{:02x}".format(*map(int, m.groups()))


def put(tree, path, value, kind, source):
    node = tree
    parts = path.split(".")
    for key in parts[:-1]:
        node = node.setdefault(key, {})
    node[parts[-1]] = tok(value, kind, source)


core = {}
light = {}
dark = {}

# Brand ramps declared as hex on :root. Names keep the site's own words.
RAMPS = {
    "blue": ("--rc-blue-primary", "--rc-blue-secondary", "--rc-blue-tertiary"),
    "red": ("--rc-red-primary", "--rc-red-secondary", "--rc-red-tertiary"),
    "green": ("--rc-green-primary", "--rc-green-secondary", "--rc-green-tertiary"),
    "orange": ("--rc-orange-primary", "--rc-orange-secondary", "--rc-orange-tertiary"),
    "teal": ("--rc-teal-primary", "--rc-teal-secondary", "--rc-teal-tertiary"),
    "violet": ("--rc-violet-primary", "--rc-violet-secondary", "--rc-violet-tertiary"),
    "yellow": ("--rc-yellow-primary", "--rc-yellow-secondary", "--rc-yellow-tertiary"),
    "froggy": ("--rc-froggy-primary", "--rc-froggy-secondary", "--rc-froggy-tertiary"),
}
STEPS = ("primary", "secondary", "tertiary")
for hue, names in RAMPS.items():
    for step, name in zip(STEPS, names):
        put(core, f"color.{hue}.{step}", RES[name], "color",
            f"Measured: raw/css-vars.json resolved {name} on :root, www.revenuecat.com 2026-11-21")

# Gray ramp is authored as HSL triplets. Keep the authored string; do not convert.
for name, value in sorted(RES.items()):
    if re.fullmatch(r"--gray-\d+", name):
        put(core, f"color.gray.{name.split('-')[-1]}", value, "other",
            f"Measured: raw/css-vars.json resolved {name} (HSL triplet, not converted) on :root")

# Docs Infima ramps are hex and belong to the docs surface, not the marketing page.
for name, value in sorted(RES.items()):
    if name.startswith("--ifm-color-") and re.fullmatch(r"#[0-9a-fA-F]{3,8}", value):
        slug = name.removeprefix("--ifm-color-").replace("-", ".")
        put(core, f"color.docs.{slug}", value, "color",
            f"Measured: raw/css-vars.json resolved {name} from /docs stylesheets")

put(core, "font.family.object-sans", RES["--font-object-sans"], "fontFamily",
    "Measured: raw/css-vars.json resolved --font-object-sans")
put(core, "font.family.helvetica-neue", RES["--font-helvetica-neue"], "fontFamily",
    "Measured: raw/css-vars.json resolved --font-helvetica-neue")
put(core, "font.family.ibm-plex-mono", RES["--font-ibm-plex-mono"], "fontFamily",
    "Measured: raw/css-vars.json resolved --font-ibm-plex-mono")
put(core, "font.family.body", RES["--rc-font-family-body"], "fontFamily",
    "Measured: raw/css-vars.json resolved --rc-font-family-body (docs body stack)")

# Radius scale from declared tokens. pill is the computed pill radius, which
# the browser reports as a huge px value for a full-round corner.
for name in ("--radius-xs", "--radius-sm", "--radius-md", "--radius-lg", "--radius-xl",
             "--radius-2xl", "--radius-3xl", "--radius-4xl"):
    step = name.removeprefix("--radius-")
    put(core, f"radius.{step}", RES[name], "dimension",
        f"Measured: raw/css-vars.json resolved {name}")
put(core, "radius.pill", "9999px", "dimension",
    "Derived: marketing pills use an oversized border-radius (computed 3.35544e+07px on nav-signup); recorded as the authored full-round length, not the computed overflow")

put(core, "space.unit", RES["--spacing"], "dimension",
    "Measured: raw/css-vars.json resolved --spacing (Tailwind spacing unit)")
put(core, "space.header", "64px", "dimension",
    "Measured: raw/layout.json widths.1440./.header.h on www.revenuecat.com")

put(core, "motion.duration", RES["--default-transition-duration"], "duration",
    "Measured: raw/css-vars.json resolved --default-transition-duration")
put(core, "motion.easing", RES["--default-transition-timing-function"], "cubicBezier",
    "Measured: raw/css-vars.json resolved --default-transition-timing-function")
put(core, "motion.docs-fast", RES["--ifm-transition-fast"], "duration",
    "Measured: raw/css-vars.json resolved --ifm-transition-fast")
put(core, "motion.docs-slow", RES["--ifm-transition-slow"], "duration",
    "Measured: raw/css-vars.json resolved --ifm-transition-slow")

put(core, "border.width", RES["--ifm-global-border-width"], "dimension",
    "Measured: raw/css-vars.json resolved --ifm-global-border-width")
put(core, "shadow.docs-low", RES["--ifm-global-shadow-lw"], "shadow",
    "Measured: raw/css-vars.json resolved --ifm-global-shadow-lw")
put(core, "shadow.docs-md", RES["--ifm-global-shadow-md"], "shadow",
    "Measured: raw/css-vars.json resolved --ifm-global-shadow-md")

# Type composites from computed styles. lineHeight stays a px length when the
# browser reported one.
TYPE = {
    "display": ("pages.home.h1", "home h1, www.revenuecat.com /"),
    "display-pricing": ("pages.pricing.h1", "pricing h1, /pricing"),
    "title-sales": ("pages.sales.h1", "sales h1, /talk-to-sales"),
    "docs-title": ("pages.docs.h1", "docs h1, /docs light"),
    "body": None,
    "nav": ("pages.home.navTrigger", "nav trigger, /"),
    "button": ("pages.home.signup", "Sign up link, /"),
    "button-lg": ("pages.home.heroCta", "Start for free, /"),
}
home_body = COMP["pages"]["home"]["body"]


def style_of(path):
    node = COMP
    for part in path.split("."):
        node = node[part]
    return node["style"]


def type_token(style, source):
    family = style["fontFamily"].split(",")[0].strip().strip('"')
    return tok({
        "fontFamily": family,
        "fontSize": style["fontSize"],
        "fontWeight": int(style["fontWeight"]) if str(style["fontWeight"]).isdigit() else style["fontWeight"],
        "lineHeight": style["lineHeight"],
    }, "typography", source)


put(core, "typography.display", None, "typography", "")  # replaced below
core["typography"] = {
    "display": type_token(style_of("pages.home.h1"),
                          "Measured: raw/components-computed.json pages.home.h1 on / at 1440"),
    "display-pricing": type_token(style_of("pages.pricing.h1"),
                                  "Measured: raw/components-computed.json pages.pricing.h1 on /pricing"),
    "title-sales": type_token(style_of("pages.sales.h1"),
                              "Measured: raw/components-computed.json pages.sales.h1 on /talk-to-sales"),
    "docs-title": type_token(style_of("pages.docs.h1"),
                             "Measured: raw/components-computed.json pages.docs.h1 on /docs light"),
    "body": tok({
        "fontFamily": "helveticaNeue",
        "fontSize": home_body["fontSize"],
        "fontWeight": 400,
        "lineHeight": home_body["lineHeight"],
    }, "typography", "Measured: raw/components-computed.json pages.home.body on /"),
    "nav": type_token(style_of("pages.home.navTrigger"),
                      "Measured: raw/components-computed.json pages.home.navTrigger on /"),
    "button": type_token(style_of("pages.home.signup"),
                         "Measured: raw/components-computed.json pages.home.signup on /"),
    "button-lg": type_token(style_of("pages.home.heroCta"),
                            "Measured: raw/components-computed.json pages.home.heroCta on /"),
}

# Semantic light roles. Page and text come from the body computed style.
# Accent is the declared --rc-blue-primary, which matches the Sign up fill
# (#576cdb == rgb(87, 109, 219)).
put(light, "page", "#ffffff", "color",
    "Measured: raw/css-vars.json pages./.root.background rgb(255, 255, 255) and resolved --surface-primary")
put(light, "surface", "#f9fafb", "color",
    "Measured: raw/components-computed.json pages.sales.field backgroundColor rgb(249, 250, 251) on /talk-to-sales")
put(light, "text", "#1f1f47", "color",
    "Measured: raw/css-vars.json pages./.root.color rgb(31, 31, 71)")
put(light, "muted", "#3d3d5c", "color",
    "Measured: raw/components-computed.json pages.home.login color rgb(61, 61, 92)")
put(light, "accent", RES["--rc-blue-primary"], "color",
    "Measured: raw/css-vars.json resolved --rc-blue-primary; matches Sign up background rgb(87, 109, 219)")
put(light, "accent-hover", "#3e52b9", "color",
    "Measured: raw/components-computed.json pages.home.signupHover backgroundColor rgb(62, 82, 185)")
put(light, "on-accent", "#ffffff", "color",
    "Measured: raw/components-computed.json pages.home.signup color rgb(255, 255, 255)")
put(light, "link", "#3d52b8", "color",
    "Measured: raw/components-computed.json pages.home.contact color rgb(61, 82, 184)")
put(light, "border", "#eaedf6", "color",
    "Measured: raw/components-computed.json pages.home.email borderTopColor rgb(234, 237, 246)")
put(light, "border-strong", "#e3e6e8", "color",
    "Measured: raw/components-computed.json pages.sales.field borderTopColor rgb(227, 230, 232)")
put(light, "focus", "#576ddc", "color",
    "Measured: raw/components-computed.json pages.home.emailFocus borderTopColor rgb(89, 111, 220)")
put(light, "brand", RES["--rc-red-primary"], "color",
    "Measured: raw/css-vars.json resolved --rc-red-primary; nav trigger hover computed rgb(231, 82, 91), close to this declared red")
put(light, "success", RES["--rc-green-primary"], "color",
    "Measured: raw/css-vars.json resolved --rc-green-primary and --success-primary")
put(light, "warning", RES["--rc-yellow-primary"], "color",
    "Measured: raw/css-vars.json resolved --rc-yellow-primary and --warning-primary")
put(light, "danger", RES["--error-primary"], "color",
    "Measured: raw/css-vars.json resolved --error-primary")
put(light, "info", RES["--ifm-color-info"], "color",
    "Measured: raw/css-vars.json resolved --ifm-color-info (docs status hue; not seen as a marketing banner)")
put(light, "disabled", RES["--action-disabled"], "color",
    "Measured: raw/css-vars.json resolved --action-disabled; no disabled control was on the captured public pages")
put(light, "disabled-text", RES["--action-disabled-text"], "color",
    "Measured: raw/css-vars.json resolved --action-disabled-text")

# Component colours, light marketing.
COMPONENTS = {
    "button-primary-bg": ("pages.home.signup", "backgroundColor", "color"),
    "button-primary-bg-hover": ("pages.home.signupHover", "backgroundColor", "color"),
    "button-primary-text": ("pages.home.signup", "color", "color"),
    "button-primary-radius": ("pages.home.signup", "borderTopLeftRadius", "other"),
    "button-primary-height": ("pages.home.signup", "height", "dimension"),
    "button-lg-height": ("pages.home.heroCta", "height", "dimension"),
    "button-outline-text": ("pages.home.contact", "color", "color"),
    "button-outline-border": ("pages.home.contact", "borderTopColor", "other"),
    "field-bg": ("pages.home.email", "backgroundColor", "color"),
    "field-border": ("pages.home.email", "borderTopColor", "color"),
    "field-border-focus": ("pages.home.emailFocus", "borderTopColor", "color"),
    "field-height": ("pages.home.email", "height", "dimension"),
    "field-radius": ("pages.home.email", "borderTopLeftRadius", "other"),
    "nav-height": ("pages.home.navTrigger", "height", "dimension"),
    "nav-hover": ("pages.home.navTriggerHover", "color", "color"),
}
for path, (node, prop, kind) in COMPONENTS.items():
    style = style_of(node)
    value = style[prop]
    if kind == "color":
        value = hex_of(value) or value
    if kind == "dimension" and not re.fullmatch(r"-?\d+(\.\d+)?(px|rem|em)", str(value)):
        kind = "other"
    put(light, "component." + path, value, kind,
        f"Measured: raw/components-computed.json {node}.style.{prop}")

# Docs dark. Only the heading colour was re-read after the live toggle.
# The page fill was not read as a computed style, so there is no dark.page token.
put(dark, "text", "#e3e3e3", "color",
    "Measured: raw/components-computed.json pages.docs.h1Dark color rgb(227, 227, 227) after the docs theme toggle")
put(dark, "accent", RES["--rc-blue-primary"], "color",
    "Measured: the docs primary button stayed the marketing blue in screenshots/docs-light-dark.png; --rc-blue-primary. Button fill was not re-read after the toggle, so this is the declared token, not a second computed reading.")
put(dark, "on-accent", "#ffffff", "color",
    "Observed: docs primary button label stayed white in screenshots/docs-light-dark.png. Not re-read as a computed style after the toggle.")

# Fix dark.page: the comment above is the evidence. Leave the Derived label.

out = {
    "core": core,
    "light": light,
    "dark": dark,
    "$themes": [
        {
            "id": "light",
            "name": "Light",
            "selectedTokenSets": {"core": "source", "light": "enabled"},
            "$description": "Marketing site theme. prefers-color-scheme dark did not change www.revenuecat.com (raw/css-vars.json themeChecks).",
        },
        {
            "id": "dark",
            "name": "Docs dark",
            "selectedTokenSets": {"core": "source", "dark": "enabled"},
            "$description": "Docs-only theme, switched live on /docs. Marketing pages have no dark theme. Several dark roles are not captured.",
        },
    ],
    "$metadata": {"tokenSetOrder": ["core", "light", "dark"]},
}

# cubicBezier must be a 4-number list for some consumers. The site authored a
# CSS function. Keep the string and use type other if the kit's guide cannot
# render cubicBezier strings. build_style_guide treats cubicBezier as a list.
core["motion"]["easing"]["$type"] = "other"

text = json.dumps(out, indent=2) + "\n"
(HERE / "tokens.json").write_text(text)
print("wrote tokens.json", "core", len(core), "light", len(light), "dark", len(dark))
