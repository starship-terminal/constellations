#!/usr/bin/env python3
"""Write tokens.json from the public Zoom readings of 2026-11-21.

Colours are the computed sRGB values in raw/controls.json and raw/colors.json.
Nothing here is recalled from memory of the brand.

python3 tools/build_tokens.py
"""
import json
import pathlib

PKG = pathlib.Path(__file__).resolve().parent.parent


def tok(value, typ, desc, evidence="Sampled", capture="raw/controls.json"):
    return {
        "$value": value,
        "$type": typ,
        "$description": desc,
        "$extensions": {"source": {"evidence": evidence, "capture": capture}},
    }


BLUE = "#0b5cff"
BLUE_NEXT = "#0d6bde"
NAVY = "#00053d"
INK = "#222325"
PAGE_LIGHT = "#f1f4f6"
WHITE = "#ffffff"
PALE = "#e6f0ff"
PLAN = "#f3f8ff"
FOCUS = "#4b96f1"
DISABLED = "#adb1b8"
DISABLED_BG = "rgba(173, 177, 184, 0.25)"
FOOTER = "#00053d"
HERO_TEXT = "#ffffff"

core = {
    "color": {
        "blue": tok(BLUE, "color", "Computed background of Sign Up Free and Buy now. rgb(11, 92, 255)."),
        "blueNext": tok(BLUE_NEXT, "color", "Computed background of the sign-in Next button. rgb(13, 107, 222).", "Sampled", "raw/controls.json"),
        "navy": tok(NAVY, "color", "Computed text on the marketing header and the footer fill. rgb(0, 5, 61).", "Sampled", "raw/colors.json"),
        "ink": tok(INK, "color", "Computed colour of the sign-in heading. rgb(34, 35, 37)."),
        "focus": tok(FOCUS, "color", "Computed border on the focused sign-in field. rgb(75, 150, 241)."),
        "disabled": tok(DISABLED, "color", "Computed text on the empty signup Continue. rgb(173, 177, 184)."),
    },
    "fontFamily": {
        "sans": tok("Inter", "fontFamily", "Computed family on the marketing header buttons. Inter, then Helvetica.", "Sampled", "raw/colors.json"),
        "display": tok("Newsreader", "fontFamily", "Computed family on the homepage h1, 54px, weight 500.", "Sampled", "raw/public-readings.json"),
        "app": tok("Almaden Sans", "fontFamily", "Computed family on pricing, sign-in, and signup. Files are not in this package."),
    },
    "fontSize": {
        "14": tok("14px", "dimension", "Sign Up Free on the marketing header, and the pricing Buy now label."),
        "16": tok("16px", "dimension", "Explore products and the sign-in field."),
        "32": tok("32px", "dimension", "Sign in heading."),
        "36": tok("36px", "dimension", "Sign up for free heading."),
        "50": tok("50px", "dimension", "About h1. Computed on the About page.", "Sampled", "raw/colors.json"),
        "54": tok("54px", "dimension", "Homepage h1.", "Sampled", "raw/public-readings.json"),
    },
    "fontWeight": {
        "regular": tok("400", "fontWeight", "Body and the sign-in field."),
        "medium": tok("500", "fontWeight", "Homepage display, pricing Buy now, sign-in heading."),
        "semibold": tok("600", "fontWeight", "Sign Up Free and Contact Sales."),
        "bold": tok("700", "fontWeight", "Sign up for free heading."),
    },
    "radius": {
        "sm": tok("8px", "dimension", "Sign Up Free radius in one header reading, before the 12px reading on the same control."),
        "md": tok("12px", "dimension", "Sign Up Free, Contact Sales, Explore products, Find your plan, Buy now, the sign-in field, and Continue."),
        "card": tok("16px", "dimension", "Most popular badge, top corners only. 16px 16px 0 0."),
    },
    "size": {
        "button": tok("46px", "dimension", "Sign Up Free, Contact Sales, Explore products, and Find your plan. Computed height.", "Sampled", "raw/colors.json"),
        "buttonBuy": tok("48px", "dimension", "Buy now on pricing."),
        "field": tok("48px", "dimension", "Sign-in email field."),
        "header": tok("78px", "dimension", "Marketing header on the homepage at 1440."),
        "headerPricing": tok("72px", "dimension", "Header on the pricing page."),
    },
}


def semantic(theme):
    dark = theme == "dark"
    return {
        "page": tok(
            FOOTER if dark else PAGE_LIGHT,
            "color",
            "Dark page is the homepage navy, rgb(0, 5, 61), also the footer fill. Light page is the pricing canvas, rgb(241, 244, 246).",
            "Sampled",
            "raw/colors.json",
        ),
        "surface": tok(
            WHITE,
            "color",
            "Mega menu panel and the signup card. rgb(255, 255, 255).",
        ),
        "text": tok(
            HERO_TEXT if dark else INK,
            "color",
            "Dark text is the homepage hero, rgb(255, 255, 255). Light text is the sign-in heading, rgb(34, 35, 37).",
        ),
        "muted": tok(
            "not captured",
            "color",
            "A muted text role was not isolated. Pricing body text is rgb(35, 35, 51). That is recorded in raw/controls.json and is not promoted to a token.",
            "Not captured",
        ),
        "accent": tok(BLUE, "color", "Sign Up Free and Buy now. rgb(11, 92, 255)."),
        "onAccent": tok(WHITE, "color", "Text on Sign Up Free and Buy now."),
        "border": tok(
            "rgba(255, 255, 255, 0.16)" if dark else "rgba(0, 5, 61, 0.12)",
            "color",
            "Not declared as a token. Derived from the hairline under the light header and the dark header rule.",
            "Derived",
        ),
        "focus": tok(FOCUS, "color", "Sign-in field border when focused. rgb(75, 150, 241)."),
        "secondary": tok(
            PALE if not dark else PLAN,
            "color",
            "Contact Sales fill, rgb(230, 240, 255). Find your plan is rgb(243, 248, 255).",
            "Sampled",
            "raw/colors.json",
        ),
        "disabled": tok(DISABLED, "color", "Empty signup Continue text."),
        "disabledBg": tok(DISABLED_BG, "color", "Empty signup Continue fill. rgba(173, 177, 184, 0.25)."),
    }


doc = {
    "core": core,
    "dark": semantic("dark"),
    "light": semantic("light"),
    "$themes": [
        {"name": "dark", "group": "dark"},
        {"name": "light", "group": "light"},
    ],
}
(PKG / "tokens.json").write_text(json.dumps(doc, indent=1) + "\n")
print("wrote", PKG / "tokens.json")
