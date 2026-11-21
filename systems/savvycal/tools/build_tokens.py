#!/usr/bin/env python3
"""Build tokens.json from SavvyCal public-page readings.

Sources, read from savvycal.com on 2026-11-21, signed out:
  raw/css-vars.json              stylesheet harvest. Marketing pages declare
                                 --nav-height only. Brand colours are Tailwind
                                 utilities, read as computed styles.
  raw/components-computed.json   getComputedStyle on real controls.

Every token carries $extensions.source. A value that was not read is not
invented. The marketing surface paints one light theme. Login CSS includes
unused dark: utilities; no dark theme was switched on, so dark is omitted
from $themes.

Deterministic: same inputs, same bytes.
"""
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"


def src(text):
    return {"$extensions": {"source": text}}


def color(value, source):
    return {"$type": "color", "$value": value, **src(source)}


def dim(value, source):
    return {"$type": "dimension", "$value": value, **src(source)}


def font(value, source):
    return {"$type": "fontFamily", "$value": value, **src(source)}


def weight(value, source):
    return {"$type": "fontWeight", "$value": value, **src(source)}


def num(value, source):
    return {"$type": "number", "$value": value, **src(source)}


def typography(family, size, weight_v, line, source):
    return {
        "$type": "typography",
        "$value": {
            "fontFamily": family,
            "fontSize": size,
            "fontWeight": weight_v,
            "lineHeight": line,
        },
        **src(source),
    }


# oklch() computed colours converted with the CSS oklab matrix, then sRGB.
# The hex is Derived from the measured oklch. rgb() values are Measured.
INK = "#0c0c09"          # oklch(0.153 0.006 107.1) nav, headings
OLIVE_50 = "#fbfbf9"     # oklch(0.988 0.003 106.5) footer hover
OLIVE_400 = "#abab9c"    # oklch(0.737 0.021 106.9) footer link
OLIVE_600 = "#5b5b4b"    # oklch(0.466 0.025 107.3)
OLIVE_800 = "#2b2b22"    # oklch(0.286 0.016 107.4)
ZINC = "#09090b"         # oklch(0.141 0.005 285.823) login field text
ZINC_210 = "#18181b"     # oklch(0.21 0.006 285.885) login submit text
FOCUS_BLUE = "#155dfc"   # oklch(0.546 0.245 262.881) login field focus ring

OATMEAL = "#fcf7ed"      # rgb(252, 247, 237)
SAND = "#f4ebda"         # rgb(244, 235, 218)
ORANGE = "#f54320"       # rgb(245, 67, 32)
ORANGE_HOVER = "#e03a18" # rgb(224, 58, 24)
NEON = "#b9ff78"         # rgb(185, 255, 120)
WHITE = "#ffffff"

core = {
    "color": {
        "brand": {
            "oatmeal": color(OATMEAL, "Measured: computed background of body.bg-brand-oatmeal on https://savvycal.com/"),
            "sand": color(SAND, "Measured: computed background of .bg-brand-sand on the homepage"),
            "orange": color(ORANGE, "Measured: computed background of the hero CTA (Try SavvyCal risk-free)"),
            "orange-hover": color(ORANGE_HOVER, "Measured: computed background of the hero CTA in hover"),
            "neon-green": color(NEON, "Measured: computed background of the login Sign In button"),
            "white": color(WHITE, "Measured: computed color of the hero CTA label"),
        },
        "olive": {
            "950": color(INK, "Derived: oklch(0.153 0.006 107.1) computed color of the homepage nav link, converted to sRGB"),
            "800": color(OLIVE_800, "Derived: oklch(0.286 0.016 107.4) computed color of .text-olive-800, converted to sRGB"),
            "600": color(OLIVE_600, "Derived: oklch(0.466 0.025 107.3) computed color of .text-olive-600, converted to sRGB"),
            "400": color(OLIVE_400, "Derived: oklch(0.737 0.021 106.9) computed color of the Privacy footer link, converted to sRGB"),
            "50": color(OLIVE_50, "Derived: oklch(0.988 0.003 106.5) computed color of the footer link in hover, converted to sRGB"),
        },
        "zinc": {
            "950": color(ZINC, "Derived: oklch(0.141 0.005 285.823) computed color of the login email field, converted to sRGB"),
            "900": color(ZINC_210, "Derived: oklch(0.21 0.006 285.885) computed color of the login Sign In label, converted to sRGB"),
        },
        "focus": {
            "blue": color(FOCUS_BLUE, "Derived: oklch(0.546 0.245 262.881) in the login email focused box-shadow, converted to sRGB"),
        },
    },
    "font": {
        "family": {
            "ui": font("InterVariable, sans-serif", "Measured: computed font-family of the hero CTA and nav"),
            "display": font("GT-Alpina-Condensed", "Measured: computed font-family of the homepage h1"),
            "auth": font("GT-America-Standard", "Measured: computed font-family of the Google sign-in button"),
        }
    },
    "typography": {
        "display": typography("{font.family.display}", "88px", 700, "83.6px", "Measured: homepage h1 computed font-size 88px, weight 700, line-height 83.6px"),
        "body": typography("{font.family.ui}", "16px", 400, "28px", "Measured: FAQ summary computed font-size 16px, weight 400, line-height 28px"),
        "label": typography("{font.family.ui}", "14px", 500, "26px", "Measured: nav link and hero CTA computed font-size 14px, weight 500, line-height 26px"),
        "field": typography("{font.family.ui}", "14px", 400, "24px", "Measured: login email field computed font-size 14px, weight 400, line-height 24px"),
    },
    "radius": {
        "pill": dim("9999px", "Derived: computed border-radius 3.35544e+07px on the hero CTA, the pill form of a fully rounded control"),
        "control": dim("8px", "Measured: login email field and Google button border-radius 8px"),
    },
    "spacing": {
        "1": dim("4px", "Measured: nav Sign up padding-top 4px"),
        "2": dim("6px", "Measured: billing toggle padding-top 6px"),
        "3": dim("8px", "Measured: search field padding-top 8px"),
        "4": dim("10px", "Measured: hero CTA padding-top 10px"),
        "5": dim("14px", "Measured: nav Sign up padding-left 14px"),
        "6": dim("16px", "Measured: FAQ summary padding-top 16px"),
        "7": dim("20px", "Measured: hero CTA padding-left 20px"),
    },
    "size": {
        "nav-height": dim("5.25rem", "Measured: custom property --nav-height on :root"),
        "hero-cta-height": dim("46px", "Measured: hero CTA bounding box height"),
        "nav-cta-height": dim("34px", "Measured: nav Sign up bounding box height"),
        "field-height": dim("36px", "Measured: login email field bounding box height"),
        "oauth-height": dim("48px", "Measured: Google sign-in button bounding box height"),
        "icon-button": dim("36px", "Measured: phone menu button bounding box 36x36"),
    },
    "focus": {
        "cta-width": dim("2px", "Measured: hero CTA focus-visible outline-width"),
        "cta-offset": dim("2px", "Measured: hero CTA focus-visible outline-offset"),
        "link-width": dim("1px", "Measured: nav link focus-visible outline-width"),
    },
}

light = {
    "page": color("{color.brand.oatmeal}", "Alias of the measured body background"),
    "surface": color("{color.brand.sand}", "Alias of the measured sand surface"),
    "text": color("{color.olive.950}", "Alias of the measured nav and heading ink"),
    "muted": color("{color.olive.400}", "Alias of the measured footer link colour"),
    "accent": color("{color.brand.orange}", "Alias of the measured hero CTA fill"),
    "accent-hover": color("{color.brand.orange-hover}", "Alias of the measured hero CTA hover fill"),
    "on-accent": color("{color.brand.white}", "Alias of the measured CTA label"),
    "border": color("{color.olive.800}", "Derived from the measured olive-800 text role; no separate border token was declared"),
    "neon": color("{color.brand.neon-green}", "Alias of the measured login submit fill"),
    "focus": color("{color.brand.orange}", "Measured: hero CTA focus-visible outline-color rgb(245, 67, 32)"),
    "link-focus": color("{color.focus.blue}", "Derived from the measured nav-link focus outline rgb(0, 95, 204) is the browser default; the login field ring is oklch(0.546 0.245 262.881)"),
    "component": {
        "button": {
            "bg": color("{color.brand.orange}", "Measured: hero CTA background"),
            "text": color("{color.brand.white}", "Measured: hero CTA color"),
            "radius": dim("{radius.pill}", "Measured pill radius on the hero CTA"),
            "height": dim("46px", "Measured: hero CTA height"),
            "padding": dim("10px", "Measured: hero CTA padding-top"),
        },
        "field": {
            "bg": color("{color.brand.white}", "Measured: search field background rgb(255, 255, 255)"),
            "text": color("{color.zinc.950}", "Measured colour of the login email field"),
            "radius": dim("8px", "Measured: login email border-radius"),
            "height": dim("36px", "Measured: login email height"),
        },
    },
}

doc = {
    "$schema": "https://tr.designtokens.org/format/modules/2025.10/",
    "core": core,
    "light": light,
    "$themes": [{"name": "light", "selectedTokenSets": {"core": "source", "light": "enabled"}}],
    "$extensions": {
        "source": "Measured from https://savvycal.com/ on 2026-11-21, signed out, headless Chromium. oklch values converted to sRGB are Derived. Unread roles are absent, not guessed.",
        "notTokenised": [
            "Dark theme: login CSS includes dark: utilities. No control switched a dark theme. Not captured.",
            "Success, warning, danger, info roles: not painted on the public pages. Not captured.",
            "Elevation scale: public controls paint box-shadow none, except focus rings. Not captured as a scale.",
            "Motion durations: not read as a declared scale. Not captured.",
            "Pressed colour: CDP active+hover did not change the hero CTA fill from default. Not captured as a distinct colour.",
        ],
    },
}

# Resolve aliases that are dimension aliases written as {radius.pill} inside $value strings
# The catalog resolver handles {aliases}. Keep them.


def check(node, path=""):
    if isinstance(node, dict) and "$value" in node:
        ty = node.get("$type")
        val = node["$value"]
        if not node.get("$extensions", {}).get("source"):
            raise SystemExit(f"missing source at {path}")
        if ty == "color" and isinstance(val, str) and not val.startswith("{"):
            if not re.fullmatch(r"#[0-9a-f]{6}", val):
                raise SystemExit(f"bad color {path}: {val}")
        if ty == "dimension" and isinstance(val, str) and not val.startswith("{"):
            if not re.fullmatch(r"-?\d+(\.\d+)?(px|rem)", val):
                raise SystemExit(f"bad dimension {path}: {val}")
        return
    if isinstance(node, dict):
        for k, v in node.items():
            if k.startswith("$"):
                continue
            check(v, f"{path}.{k}" if path else k)


check(core, "core")
check(light, "light")
out = HERE / "tokens.json"
out.write_text(json.dumps(doc, indent=2) + "\n")
print("wrote", out, "core groups", list(core), "light keys", list(light))
