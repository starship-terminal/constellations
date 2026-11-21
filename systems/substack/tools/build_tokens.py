#!/usr/bin/env python3
"""Build tokens.json from the public Substack CSS custom properties read on 2026-11-21.

Values are the resolved primitives behind the pencraft names on the sign-in stylesheet
(substackcdn.com bundle css/65979). Computed colours on the live pages are display-p3 and
are recorded in raw/public-readings.json. This builder uses the sRGB rgb() primitives the
stylesheet names, which match those computed channels.

python3 tools/build_tokens.py
"""
import json
import pathlib

PKG = pathlib.Path(__file__).resolve().parent.parent

def tok(value, typ, desc, evidence="Extracted", capture="raw/public-readings.json"):
    return {
        "$value": value,
        "$type": typ,
        "$description": desc,
        "$extensions": {"source": {"evidence": evidence, "capture": capture}},
    }

ORANGE = "#ff6719"
PAGE_DARK = "#161718"
TEXT_DARK = "#eeeeee"
MUTED = "#777777"
SURFACE_DARK = "#232525"
PAGE_LIGHT = "#ffffff"
TEXT_LIGHT = "#363737"
BORDER_DARK = "rgba(255, 255, 255, 0.1)"
BORDER_LIGHT = "rgba(0, 0, 0, 0.1)"
FOCUS = "#0076ff"
DISABLED_BG = "#232525"
DISABLED_FG = "#5a5b5b"
ERROR = "#ff7772"
SUCCESS = "#3d9a6a"
WARN = "#e6b325"

core = {
    "color": {
        "orange": tok(ORANGE, "color", "Pencraft --color-primitive-orange-500-rgb, 255,103,25. The public accent."),
        "focus": tok(FOCUS, "color", "Computed focus border on the email field, color(display-p3 0 0.463 1), written as sRGB #0076ff.", "Sampled"),
    },
    "fontFamily": {
        "sans": tok("system-ui", "fontFamily", "Computed font on buttons and fields: system-ui, then -apple-system, Segoe UI, Roboto, Helvetica, Arial.", "Sampled"),
        "serif": tok("Spectral", "fontFamily", "Computed body font on the logged-out home and the publication post. Loaded from fonts.gstatic.com. Files are not in this package.", "Sampled"),
        "display": tok("Cahuenga", "fontFamily", "Computed font on the About hero h1, 88px. The file is not in this package.", "Sampled"),
        "title": tok("SF Pro Display", "fontFamily", "Computed font on the sign-in heading, named SF Pro Display, then system-ui.", "Sampled"),
    },
    "fontSize": {
        "15": tok("15px", "dimension", "Button and field size. --font-size-15."),
        "19": tok("19px", "dimension", "Body size on the logged-out home and a publication post.", "Sampled"),
        "30": tok("30px", "dimension", "Sign-in heading. --font-size-30."),
        "88": tok("88px", "dimension", "About hero. Computed on h1.", "Sampled"),
    },
    "fontWeight": {
        "regular": tok("400", "fontWeight", "--font-weight-regular."),
        "semibold": tok("600", "fontWeight", "--font-weight-semibold. Primary buttons."),
        "bold": tok("700", "fontWeight", "--font-weight-bold."),
        "heavy": tok("800", "fontWeight", "--font-weight-heavy. Sign-in heading."),
    },
    "radius": {
        "xs": tok("4px", "dimension", "--border-radius-xs. Checkbox."),
        "sm": tok("8px", "dimension", "--border-radius-sm. Header buttons and the email field."),
        "md": tok("12px", "dimension", "--border-radius-md. Sign-in Continue and the About hero button."),
        "lg": tok("20px", "dimension", "--border-radius-lg. The homepage sign-in dialog."),
    },
    "size": {
        "button": tok("40px", "dimension", "Header Start your Substack and the signup Continue, computed height.", "Sampled"),
        "buttonTall": tok("48px", "dimension", "Sign-in Continue, computed height.", "Sampled"),
        "field": tok("40px", "dimension", "Email field, computed height.", "Sampled"),
        "header": tok("64px", "dimension", "Logged-out home header, from the accessibility tree.", "Sampled"),
    },
}

def semantic(theme):
    dark = theme == "dark"
    return {
        "page": tok(PAGE_DARK if dark else PAGE_LIGHT, "color", "Dark is --color-primitive-gray-900-rgb (22,23,24). Light is --color-primitive-gray-100-rgb."),
        "surface": tok(SURFACE_DARK if dark else "#f6f6f6", "color", "Dark elevated secondary, gray-800 35,37,37. Light is the About search field fill, sampled.", "Extracted" if dark else "Sampled"),
        "text": tok(TEXT_DARK if dark else TEXT_LIGHT, "color", "Dark --color-dark-fg-primary (gray-200). Light --color-light-fg-primary (gray-700)."),
        "muted": tok(MUTED, "color", "--color-fg-secondary, gray-500, both themes."),
        "accent": tok(ORANGE, "color", "--color-accent resolves to orange-500 in both themes."),
        "onAccent": tok("#ffffff", "color", "Computed colour on the orange Continue button.", "Sampled"),
        "border": tok(BORDER_DARK if dark else BORDER_LIGHT, "color", "--color-utility-detail. Dark is white at 10%. Light is black at 10%."),
        "focus": tok(FOCUS, "color", "Email field border while focused.", "Sampled"),
        "disabled": tok(DISABLED_FG if dark else MUTED, "color", "Signup Continue label while the terms box is unchecked.", "Sampled" if dark else "Not captured"),
        "disabledBg": tok(DISABLED_BG if dark else "#e6e6e6", "color", "Signup Continue fill while disabled.", "Sampled" if dark else "Not captured"),
        "error": tok(ERROR if dark else "#c53e41", "color", "Dark --color-dark-semantic-error-fg-primary (red-400). Light is red-600."),
        "success": tok("#7dcea0" if dark else SUCCESS, "color", "Named semantic success. Not seen on a public control."),
        "link": tok(ORANGE, "color", "Create account and Sign in links on the auth walls, computed as orange.", "Sampled"),
    }

doc = {
    "core": core,
    "dark": semantic("dark"),
    "light": semantic("light"),
    "$themes": [
        {"id": "dark", "name": "dark", "selectedTokenSets": {"core": "source", "dark": "enabled"}},
        {"id": "light", "name": "light", "selectedTokenSets": {"core": "source", "light": "enabled"}},
    ],
}
(PKG / "tokens.json").write_text(json.dumps(doc, indent=1) + "\n")
print("tokens", sum(len(v) for v in doc["core"].values()) + len(doc["dark"]) + len(doc["light"]))
