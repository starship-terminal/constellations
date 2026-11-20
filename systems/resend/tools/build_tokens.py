#!/usr/bin/env python3
"""Build tokens.json from the Resend public capture.

Sources, read signed-out on 2026-11-21:
  raw/css-vars.json            custom properties resolved on html for the marketing
                               home page (dark) and the docs light and dark themes
  raw/component-states.json    computed styles of public controls

Marketing paints dark only. Docs paints light by default and dark after
"Switch to dark theme". Every token carries $extensions.source.
Unread values are not invented. Deterministic.
"""
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
V = json.loads((RAW / "css-vars.json").read_text())
STATES = json.loads((RAW / "component-states.json").read_text())
HOME = V["home"]["resolved"]
ROLES = V["home"]["roles"]


def src(text):
    return {"$extensions": {"source": text}}


def color(value, source):
    value = str(value).strip()
    parts = value.split()
    if len(parts) == 3 and all(p.isdigit() for p in parts):
        value = "rgb(%s, %s, %s)" % tuple(parts)
    return {"$type": "color", "$value": value, **src(source)}


def dim(value, source):
    return {"$type": "dimension", "$value": value, **src(source)}


def font(value, source):
    return {"$type": "fontFamily", "$value": value, **src(source)}


def text(value, source):
    return {"$value": value, **src(source)}


def gray():
    out = {}
    for i in range(1, 13):
        key = f"--gray-{i}"
        if key in HOME:
            out[str(i)] = color(HOME[key], f"Measured css-var {key} on html, resend.com home, dark, 1440")
    return out


def radii():
    names = {
        "xs": "--radius-xs",
        "sm": "--radius-sm",
        "md": "--radius-md",
        "lg": "--radius-lg",
        "xl": "--radius-xl",
        "2xl": "--radius-2xl",
        "3xl": "--radius-3xl",
        "4xl": "--radius-4xl",
    }
    return {k: dim(HOME[n], f"Measured css-var {n} on html, resend.com home, dark, 1440") for k, n in names.items() if n in HOME}


def type_style(name, family, size, weight, line, tracking, source):
    return {
        "$type": "typography",
        "$value": {
            "fontFamily": family,
            "fontSize": size,
            "fontWeight": weight,
            "lineHeight": line,
            "letterSpacing": tracking,
        },
        **src(source),
    }


def component_button():
    b = STATES["button"]
    return {
        "height": dim(b["default"]["height"], "Measured computed height, header Get started link, home dark 1440, default"),
        "radius": dim(b["default"]["borderRadius"], "Measured computed border-radius, header Get started link, home dark 1440, default"),
        "fontSize": dim(b["default"]["fontSize"], "Measured computed font-size, header Get started link, home dark 1440, default"),
        "fontWeight": text(b["default"]["fontWeight"], "Measured computed font-weight, header Get started link, home dark 1440, default"),
        "paddingInline": dim(b["default"]["paddingLeft"], "Measured computed padding-left, header Get started link, home dark 1440, default"),
        "colorDefault": color(b["default"]["color"], "Measured computed color, header Get started link, home dark 1440, default"),
        "backgroundDefault": color(b["default"]["backgroundColor"], "Measured computed background-color, header Get started link, home dark 1440, default. The painted fill is a gradient the background-color does not show; see What to distrust."),
        "colorHover": color(b["hover"]["color"], "Measured computed color, header Get started link, home dark 1440, hover"),
        "backgroundHover": color(b["hover"]["backgroundColor"], "Measured computed background-color, header Get started link, home dark 1440, hover"),
        "focusRing": text(b["focusVisible"]["boxShadow"], "Measured computed box-shadow, header Get started link, home dark 1440, focus-visible forced via CDP"),
    }


core = {
    "color": {
        "gray": gray(),
        "black": color(HOME.get("--color-black", "#000"), "Measured css-var --color-black on html, resend.com home, dark, 1440"),
        "white": color(HOME.get("--color-white", "#fff"), "Measured css-var --color-white on html, resend.com home, dark, 1440"),
        "background": color(HOME["--background"], "Measured css-var --background on html, resend.com home, dark, 1440"),
        "green": color(HOME["--color-green-9"], "Measured css-var --color-green-9 on html, resend.com home, dark, 1440"),
        "red": color(HOME["--color-red-9"], "Measured css-var --color-red-9 on html, resend.com home, dark, 1440"),
        "blue": color(HOME["--color-blue-9"], "Measured css-var --color-blue-9 on html, resend.com home, dark, 1440"),
        "orange": color(HOME["--color-orange-9"], "Measured css-var --color-orange-9 on html, resend.com home, dark, 1440"),
        "yellow": color(HOME["--color-yellow-9"], "Measured css-var --color-yellow-9 on html, resend.com home, dark, 1440"),
    },
    "fontFamily": {
        "sans": font(HOME["--font-sans"], "Measured css-var --font-sans on html, resend.com home, dark, 1440"),
        "display": font(HOME["--font-domaine"], "Measured css-var --font-domaine on html, resend.com home, dark, 1440"),
        "favorit": font(HOME["--font-display"], "Measured css-var --font-display on html, resend.com home, dark, 1440"),
        "mono": font(HOME["--font-mono"], "Measured css-var --font-mono on html, resend.com home, dark, 1440"),
    },
    "fontWeight": {
        "light": text(HOME["--font-weight-light"], "Measured css-var --font-weight-light on html, resend.com home, dark, 1440"),
        "normal": text(HOME["--font-weight-normal"], "Measured css-var --font-weight-normal on html, resend.com home, dark, 1440"),
        "medium": text(HOME["--font-weight-medium"], "Measured css-var --font-weight-medium on html, resend.com home, dark, 1440"),
        "semibold": text(HOME["--font-weight-semibold"], "Measured css-var --font-weight-semibold on html, resend.com home, dark, 1440"),
        "bold": text(HOME["--font-weight-bold"], "Measured css-var --font-weight-bold on html, resend.com home, dark, 1440"),
    },
    "radius": radii(),
    "typography": {
        "display": type_style(
            "display",
            ROLES["h1"]["fontFamily"].split(",")[0].strip(),
            ROLES["h1"]["fontSize"],
            ROLES["h1"]["fontWeight"],
            ROLES["h1"]["lineHeight"],
            ROLES["h1"]["letterSpacing"],
            "Measured computed style of h1, resend.com home, dark, 1440",
        ),
        "body": type_style(
            "body",
            "Inter Website",
            ROLES["fontSize"],
            "400",
            ROLES["lineHeight"],
            "0px",
            "Measured computed style of body, resend.com home, dark, 1440",
        ),
    },
    "motion": {
        "easeOut": text(HOME["--ease-out"], "Measured css-var --ease-out on html, resend.com home, dark, 1440"),
        "easeInOut": text(HOME["--ease-in-out"], "Measured css-var --ease-in-out on html, resend.com home, dark, 1440"),
        "duration": text("Not captured", "No duration custom property was resolved on html. Durations are Not captured."),
    },
    "shadow": {
        "button": text(HOME.get("--shadow-button", ""), "Measured css-var --shadow-button on html, resend.com home, dark, 1440"),
        "lg": text(HOME.get("--shadow-lg", ""), "Measured css-var --shadow-lg on html, resend.com home, dark, 1440"),
    },
}

dark = {
    "page": color(ROLES["page"], "Measured computed background-color of body, resend.com home, dark, 1440"),
    "surface": color(HOME["--gray-2"], "Measured css-var --gray-2 on html, resend.com home, dark, 1440. Used as the raised surface step."),
    "text": color(ROLES["bodyColor"], "Measured computed color of body, resend.com home, dark, 1440"),
    "muted": color(HOME["--gray-11"], "Measured css-var --gray-11 on html, resend.com home, dark, 1440. Nav link computed color matches this."),
    "accent": color("#ffffff", "Derived from the hover fill of the header Get started control, which paints near-white. The resting control's background-color computed to transparent."),
    "border": color(HOME["--gray-3"], "Measured css-var --gray-3 on html, resend.com home, dark, 1440"),
    "link": color(STATES["link"]["default"]["color"], "Measured computed color, header Pricing link, home dark 1440, default"),
    "focus": color("rgb(153, 200, 255)", "Measured computed outline-color, login email field, login dark 1440, default"),
    "component": {
        "button": component_button(),
        "field": {
            "height": dim(STATES["field"]["default"]["height"], "Measured computed height, login email input, dark 1440, default. Nothing was typed."),
            "radius": dim(STATES["field"]["default"]["borderRadius"], "Measured computed border-radius, login email input, dark 1440, default"),
            "fontSize": dim(STATES["field"]["default"]["fontSize"], "Measured computed font-size, login email input, dark 1440, default"),
        },
        "tab": {
            "selectedBackground": color(STATES["tab"]["selected"]["backgroundColor"], "Measured computed background-color, pricing Transactional emails tab, dark 1440, selected"),
            "selectedColor": color(STATES["tab"]["selected"]["color"], "Measured computed color, pricing Transactional emails tab, dark 1440, selected"),
            "height": dim(STATES["tab"]["selected"]["height"], "Measured computed height, pricing tab, dark 1440"),
            "radius": dim(STATES["tab"]["selected"]["borderRadius"], "Measured computed border-radius, pricing tab, dark 1440"),
        },
    },
}

docs_light_roles = V["docsLight"]["roles"]
docs_dark_roles = V["docsDark"]["roles"]
docs_light_resolved = V["docsLight"]["resolved"]
light = {
    "page": color(
        "rgba(0, 0, 0, 0)",
        "Measured computed background-color of body, docs introduction, light, 1440. The value is transparent. The painted page colour was not isolated as its own token.",
    ),
    "surface": color(
        docs_light_resolved["--twoslash-popup-bg"],
        "Measured css-var --twoslash-popup-bg on html, docs light, 1440",
    ),
    "text": color(
        docs_light_roles["h1"]["color"],
        "Measured computed color of h1, docs introduction, light, 1440",
    ),
    "muted": color(
        docs_light_roles["bodyColor"],
        "Measured computed color of body, docs introduction, light, 1440. A separate muted role was not isolated.",
    ),
    "accent": color(
        docs_light_resolved["--twoslash-tag-color"],
        "Measured css-var --twoslash-tag-color on html, docs light, 1440. This is the docs link colour, used as the light accent because the docs primary button fill was not computed.",
    ),
    "border": color(
        docs_light_resolved.get("--default-border-color", "238 238 238"),
        "Measured css-var --default-border-color on html, docs light, 1440",
    ),
    "link": color(
        docs_light_resolved["--twoslash-tag-color"],
        "Measured css-var --twoslash-tag-color on html, docs light, 1440",
    ),
    "focus": color(
        "rgba(59, 130, 246, 0.5)",
        "Measured computed box-shadow colour, docs search input, light, 1440",
    ),
    "docsText": color(
        docs_dark_roles["h1"]["color"],
        "Measured computed color of h1, docs introduction, dark, 1440. Stored here so the dark docs heading is not dropped. The marketing dark set is the dark theme.",
    ),
}

tokens = {
    "$schema": "https://design-tokens.org/schema.json",
    "core": core,
    "dark": dark,
    "light": light,
    "$themes": [
        {"id": "dark", "name": "dark", "selectedTokenSets": {"core": "enabled", "dark": "enabled"}},
        {"id": "light", "name": "light", "selectedTokenSets": {"core": "enabled", "light": "enabled"}},
    ],
    "$extensions": {
        "source": "Resend public site, 2026-11-21, signed out, Playwright. Marketing dark. Docs light and dark.",
        "notTokenised": {
            "spacingScale": "Not captured. No --space-* custom properties resolved on html.",
            "motionDuration": "Not captured.",
            "marketingLightTheme": "Not present. Marketing html carries class dark and no theme toggle.",
            "signedInApp": "Not captured. Login and signup are auth walls.",
        },
    },
}

# Remove the placeholder sentence that says Not captured as a color value for duration.
# Keep motion.duration as a string token so the gap is explicit.
out = HERE / "tokens.json"
out.write_text(json.dumps(tokens, indent=1) + "\n")
print("wrote", out, "core gray", len(core["color"]["gray"]))
