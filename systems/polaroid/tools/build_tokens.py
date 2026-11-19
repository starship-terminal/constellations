#!/usr/bin/env python3
"""Build tokens.json from the Polaroid public-store readings. Deterministic."""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = pathlib.Path("/tmp/polaroid-raw")

SRC = "computed style, www.polaroid.com/en_sg, 2026-11-19, signed out"


def color(value, source):
    return {"$type": "color", "$value": value, "$extensions": {"source": source}}


def dim(value, source):
    return {"$type": "dimension", "$value": value, "$extensions": {"source": source}}


def font(families, source):
    return {"$type": "fontFamily", "$value": families, "$extensions": {"source": source}}


def typo(family, size, weight, line_height, source, letter_spacing=None):
    value = {
        "fontFamily": family,
        "fontSize": size,
        "fontWeight": weight,
        "lineHeight": line_height,
    }
    if letter_spacing:
        value["letterSpacing"] = letter_spacing
    return {"$type": "typography", "$value": value, "$extensions": {"source": source}}


def cubic(value, source):
    return {"$type": "cubicBezier", "$value": value, "$extensions": {"source": source}}


def duration(value, source):
    return {"$type": "duration", "$value": value, "$extensions": {"source": source}}


def text(value, source):
    return {"$type": "other", "$value": value, "$extensions": {"source": source}}


S = SRC
display = "{core.font.family.display}"
text_face = "{core.font.family.text}"
mono = "{core.font.family.mono}"

tokens = {
    "$description": "Polaroid public storefront (www.polaroid.com/en_sg). Signed out, 2026-11-19. One light theme. polaroid.com redirects to /en_sg.",
    "core": {
        "font": {
            "family": {
                "display": font(
                    ["REAL_HEADER_OFFC_DEMIBOLD", "Arial", "sans-serif"],
                    S + "; computed font on h1 (RealHeadOffc Demibold, weight 600)",
                ),
                "text": font(
                    ["REAL_HEADER_OFFC_REGULAR", "Arial", "sans-serif"],
                    S + "; computed font on nav, price, and the email field",
                ),
                "mono": font(
                    ["COMMIT_MONO", "Arial", "sans-serif"],
                    S + "; computed font on Shop Bundles, Continue, and Add to Bag",
                ),
                "serif": font(
                    ["SAOL_TEXT", "Times", "serif"],
                    "declared @font-face and --font-saol-text, www.polaroid.com/en_sg 2026-11-19; not computed on a visible specimen",
                ),
            }
        },
        "typography": {
            "display": typo(display, "62px", 600, "62px", S + "; listing and product h1"),
            "hero": typo(display, "40px", 600, "40px", S + "; home hero h1"),
            "title": typo(display, "32px", 600, "32px", S + "; login h1, letter-spacing -1.28px", "-1.28px"),
            "nav-panel": typo(display, "26px", 600, "31.2px", S + "; mega-menu links, letter-spacing -0.845px", "-0.845px"),
            "nav": typo(text_face, "13px", 400, "15.6px", S + "; header nav, letter-spacing -0.2106px", "-0.2106px"),
            "price": typo(text_face, "13px", 400, "15.6px", S + "; product price span"),
            "body": typo(text_face, "16px", 400, "19.2px", S + "; email input"),
            "button": typo(mono, "12px", 400, "14.4px", S + "; Shop Bundles, Continue, Add to Bag"),
        },
        "radius": {
            "none": dim("0px", S + "; Shop Bundles, Continue, Add to Bag, email field, product card"),
            "pill": dim("100px", S + "; Product Finder link"),
        },
        "space": {
            "page-margin": dim("15px", S + "; --page-margin .9375rem at 1024px and up (16px root)"),
            "nav-safe": dim("81.6px", S + "; --page-nav-safe-area 5.1rem at 1024px and up"),
            "button-pad-x": dim("15px", S + "; Shop Bundles padding-left 15.04px"),
            "button-pad-y": dim("13px", S + "; Shop Bundles padding-top 12.96px"),
            "field-pad-x": dim("15px", S + "; email input padding-left 15.04px"),
            "promo-height": dim("30px", S + "; announcement bar SFI2JW_container"),
        },
        "border": {
            "solid": dim("1px", S + "; --border-solid-width, and the email field wrapper"),
        },
        "control": {
            "shop-height": dim("42px", S + "; Shop Bundles and Get Inspired"),
            "continue-height": dim("45px", S + "; Continue and Add to Bag"),
            "field-height": dim("45px", S + "; email field wrapper IEMMsq_inputContainer"),
            "finder-height": dim("32px", S + "; Product Finder"),
            "search-size": dim("20px", S + "; header search button"),
        },
        "motion": {
            "duration-fast": duration("200ms", "declared transition-duration 0.2s in stylesheets, www.polaroid.com/en_sg 2026-11-19"),
            "duration": duration("300ms", "declared transition-duration 0.3s in stylesheets, www.polaroid.com/en_sg 2026-11-19"),
            "easing-standard": cubic(
                [0.45, 0.02, 0.09, 0.98],
                "declared transition-timing-function, www.polaroid.com/en_sg 2026-11-19",
            ),
            "easing-card": cubic(
                [0.38, 0.07, 0.41, 0.88],
                "declared --card-grid-ease-background on .eKUYtG_container, www.polaroid.com/en_sg 2026-11-19",
            ),
        },
        "aspect": {
            "polaroid": text("18.75 / 22.8", S + "; --aspect-ratio-polaroid"),
        },
    },
    "light": {
        "page": color("#ffffff", S + "; body background rgb(255, 255, 255)"),
        "surface": color("#e9e9e9", S + "; --color-grey-200, product card background rgb(233, 233, 233)"),
        "text": color("#151515", S + "; --color-secondary, body color rgb(21, 21, 21)"),
        "muted": color("#e9e9e9", S + "; --color-grey-200. Used as the muted swatch because no separate muted text colour was computed. Same value as light.surface."),
        "accent": color("#151515", S + "; Continue and Add to Bag background rgb(21, 21, 21)"),
        "on-accent": color("#ffffff", S + "; Continue and Add to Bag color rgb(255, 255, 255)"),
        "border": color("#151515", S + "; --border-solid-color and the email field wrapper"),
        "promo": color("#151515", S + "; announcement bar SFI2JW_container background"),
        "on-promo": color("#ffffff", S + "; announcement bar color"),
        "nav-active": color("#d60026", S + "; Holidays nav link color rgb(214, 0, 38) on the cameras page"),
        "error": color("#d31f26", S + "; --color-error"),
        "highlight": color("#27b4da", S + "; --color-highlight on :root and html.light-mode"),
        "inverse": color("#ffffff", S + "; --color-primary, the light page fill"),
        "badge": color("#151515", S + "; Bundle Savings tag background rgb(21, 21, 21)"),
        "on-badge": color("#ffffff", S + "; Bundle Savings tag color"),
        "card-hover": color("#c6c6c6", "declared color-mix(in srgb, var(--color-grey-200) 85%, black) on card hover; not a live hover reading"),
    },
    "$themes": [
        {
            "id": "light",
            "name": "light",
            "selectedTokenSets": {"core": "source", "light": "enabled"},
        }
    ],
}

out = HERE / "tokens.json"
out.write_text(json.dumps(tokens, indent=2) + "\n")
print(f"wrote {out}")
