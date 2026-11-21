#!/usr/bin/env python3
"""Build tokens.json from the Pattern Brands public-site readings.

Sources, read from https://www.patternbrands.com/ on 2026-11-21:
  raw/css-vars.json              :root custom properties, resolved on the live page
  raw/components-computed.json   computed styles of the elements that paint

The site ships one light theme. Webflow's starter palette (blue, pink, success,
warning, error) is declared on :root and is recorded under core.palette.starter.
Those names are not painted on the captured pages, so they are not semantic roles.
Every token carries $extensions.source. The builder refuses a leaf without a source.
"""
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"


def color(value, source, description=""):
    token = {
        "$value": value,
        "$type": "color",
        "$extensions": {"source": source},
    }
    if description:
        token["$description"] = description
    return token


def dim(value, source, description=""):
    token = {
        "$value": value,
        "$type": "dimension",
        "$extensions": {"source": source},
    }
    if description:
        token["$description"] = description
    return token


def other(value, typ, source, description=""):
    token = {
        "$value": value,
        "$type": typ,
        "$extensions": {"source": source},
    }
    if description:
        token["$description"] = description
    return token


CSS = "declared on :root in pattern-staging.webflow CSS, resolved on https://www.patternbrands.com/ (raw/css-vars.json)"
COMP = "computed style on https://www.patternbrands.com/ at 1440x900 (raw/components-computed.json)"

core = {
    "$description": "Scales and the Webflow starter palette. Semantic roles live in light.",
    "palette": {
        "brandGreen": color("#084935", CSS + ", --base-color-brand--green", "The house green. Footer fill, button fill, visit links."),
        "brandBlack": color("#1e1e1e", CSS + ", --base-color-brand--black", "Body and heading ink. Not pure black."),
        "white": color("#ffffff", CSS + ", --base-color-neutral--white", "Page ground and text on green."),
        "hoverGreen": color("#1d9671", COMP + ", backgroundColor of .btn__circle", "The circle that scales over the button on hover."),
        "wordGreen": color(
            "#13af7f",
            "Sampled from a flat run of pixels on the rotating word in raw-shots/home-light-default.png before quantize. Computed color of .rotating-text__word stayed #1e1e1e; the green is painted by the page script.",
            "The accent painted on the rotating word (thoughtful, innovative, beautiful). Sampled, not a custom property.",
        ),
        "focusBlue": color(
            "#005fcc",
            COMP + ", outlineColor of a.btn after Tab. The stylesheet's *[tabindex]:focus-visible rule names #4d65ff; the browser painted the UA outline instead.",
            "The outline the browser painted on keyboard focus of Contact Us.",
        ),
        "starter": {
            "$description": "Webflow starter names declared on :root. Not painted on the captured pages.",
            "blue": color("#2d62ff", CSS + ", --base-color-brand--blue"),
            "pink": color("#dd23bb", CSS + ", --base-color-brand--pink"),
            "pinkLight": color("#ffaefe", CSS + ", --base-color-brand--pink-light"),
            "pinkDark": color("#3c043b", CSS + ", --base-color-brand--pink-dark"),
            "success": color("#cef5ca", CSS + ", --base-color-system--success-green"),
            "successDark": color("#114e0b", CSS + ", --base-color-system--success-green-dark"),
            "warning": color("#fcf8d8", CSS + ", --base-color-system--warning-yellow"),
            "warningDark": color("#5e5515", CSS + ", --base-color-system--warning-yellow-dark"),
            "error": color("#f8e4e4", CSS + ", --base-color-system--error-red"),
            "errorDark": color("#3b0b0b", CSS + ", --base-color-system--error-red-dark"),
            "neutralLightest": color("#eeeeee", CSS + ", --base-color-neutral--neutral-lightest"),
            "neutralLighter": color("#cccccc", CSS + ", --base-color-neutral--neutral-lighter"),
            "neutralLight": color("#aaaaaa", CSS + ", --base-color-neutral--neutral-light"),
            "neutral": color("#666666", CSS + ", --base-color-neutral--neutral"),
            "neutralDark": color("#444444", CSS + ", --base-color-neutral--neutral-dark"),
            "neutralDarker": color("#222222", CSS + ", --base-color-neutral--neutral-darker"),
            "neutralDarkest": color("#111111", CSS + ", --base-color-neutral--neutral-darkest"),
            "black": color("#000000", CSS + ", --base-color-neutral--black"),
        },
    },
    "font": {
        "family": {
            "display": other(
                '"P22 Mackinac Pro", Georgia, sans-serif',
                "fontFamily",
                COMP + ", fontFamily of h2.heading-style-h4, body, a.btn and legal h1. @font-face family P22 Mackinac Pro, weight 400.",
            ),
            "footer": other(
                "Cadiz, Arial, sans-serif",
                "fontFamily",
                COMP + ", fontFamily of footer.footer_component and a.footer_link. @font-face family Cadiz, weight 400.",
            ),
        },
        "weight": {
            "regular": other(400, "fontWeight", COMP + ", fontWeight 400 on heading, body, button and footer link. No other weight was served."),
        },
    },
    "typography": {
        "display": other(
            {"fontFamily": "{font.family.display}", "fontSize": "48px", "fontWeight": 400, "lineHeight": "52.8px"},
            "typography",
            COMP + ", h1 on /terms-of-service at 1440. Phone width measured 40px / 44px.",
        ),
        "heading": other(
            {"fontFamily": "{font.family.display}", "fontSize": "28.8px", "fontWeight": 400, "lineHeight": "31.68px"},
            "typography",
            COMP + ", h2.heading-style-h4 on the home page at 1440. Phone width measured 24px / 26.4px.",
        ),
        "body": other(
            {"fontFamily": "{font.family.display}", "fontSize": "16px", "fontWeight": 400, "lineHeight": "20.8px"},
            "typography",
            COMP + ", p.text-size-regular and legal paragraphs. Same size at 390.",
        ),
        "label": other(
            {"fontFamily": "{font.family.display}", "fontSize": "16px", "fontWeight": 400, "lineHeight": "20.8px"},
            "typography",
            COMP + ", a.btn and the 404 Go Home link.",
        ),
        "footer": other(
            {"fontFamily": "{font.family.footer}", "fontSize": "14px", "fontWeight": 400, "lineHeight": "18.2px"},
            "typography",
            COMP + ", a.footer_link and .footer_credit-text.",
        ),
    },
    "radius": {
        "none": dim("0px", COMP + ", borderRadius of a.product_item, footer and headings."),
        "button": dim("24px", COMP + ", borderRadius of .btn__bg."),
        "pill": dim("1600px", COMP + ", borderRadius of the 404 a.button.w-button."),
        "circle": dim("50%", COMP + ", borderRadius of .btn__circle. A percentage, not a px length.", "Hover circle. Not a px length."),
    },
    "space": {
        "8": dim("8px", COMP + ", padding of .spacer-xsmall (padding-top 8px) and the 404 button's vertical padding."),
        "12": dim("12px", COMP + ", paddingTop of a.btn."),
        "16": dim("16px", COMP + ", padding of .spacer-small."),
        "20": dim("20px", COMP + ", paddingLeft of a.btn. Phone page padding of .padding-global is 20px."),
        "24": dim("24px", COMP + ", padding of the 404 button's horizontal padding, and footer_link-wrapper padding-top."),
        "32": dim("32px", COMP + ", padding of .padding-section-small and .spacer-medium."),
        "40": dim("40px", COMP + ", paddingLeft of .padding-global at 1440."),
    },
    "size": {
        "buttonHeight": dim("44px", COMP + ", height of a.btn at 1440 and 390."),
        "errorButtonHeight": dim("37px", COMP + ", height of the 404 Go Home link at 1440."),
        "contentWidth": dim("736px", COMP + ", width of .container-large at 1440."),
        "pagePadding": dim("40px", COMP + ", horizontal padding of .padding-global at 1440."),
        "phonePadding": dim("20px", COMP + ", horizontal padding of .padding-global at 390 (container 350 inside 390)."),
        "cardImageHeight": dim("192px", COMP + ", height of .product_image at 1440. Phone measured 280px."),
        "focusWidth": dim("1px", COMP + ", outlineWidth of a.btn after Tab."),
        "focusOffset": dim("1px", COMP + ", outlineOffset of a.btn after Tab."),
    },
    "motion": {
        "button": other("700ms", "duration", "Inline stylesheet on the home page: .btn .btn__text and .btn .btn__circle transition 0.7s."),
        "easing": other([0.625, 0.05, 0, 1], "cubicBezier", "Inline stylesheet: cubic-bezier(0.625, 0.05, 0, 1) on the button hover."),
        "imageScale": other("1.1", "number", COMP + ", transform matrix(1.1, 0, 0, 1.1, 0, 0) on .product_image while a.product_item is hovered."),
        "arrowShift": dim("4px", "Inline style .product_item:hover .product_arrow { transform: translateX(4px) }, confirmed by computed matrix(1, 0, 0, 1, 4, 0)."),
    },
}

light = {
    "$description": "The only theme the public site paints. prefers-color-scheme: dark left body, text and footer unchanged.",
    "background": {
        "page": color("{palette.white}", "Alias of the measured page ground. body backgroundColor rgb(255, 255, 255)."),
        "surface": color("{palette.white}", "The home section and legal pages sit on the same white. No raised surface was measured."),
        "inverse": color("{palette.brandGreen}", COMP + ", backgroundColor of footer.footer_component."),
    },
    "text": {
        "primary": color("{palette.brandBlack}", COMP + ", color of h2.heading-style-h4 and p.text-size-regular."),
        "onAccent": color("{palette.white}", COMP + ", color of a.btn and footer text."),
        "link": color("{palette.brandGreen}", COMP + ", color of .product_link."),
        "accentWord": color("{palette.wordGreen}", "The rotating word's painted green. Sampled. See core.palette.wordGreen."),
    },
    "action": {
        "primary": color("{palette.brandGreen}", COMP + ", backgroundColor of .btn__bg and of the 404 Go Home link."),
        "primaryHover": color("{palette.hoverGreen}", COMP + ", backgroundColor of .btn__circle while a.btn is hovered. The circle scales to cover the fill."),
    },
    "border": {
        "none": color("rgba(0, 0, 0, 0)", COMP + ", borders on buttons, cards and footer links were 0px."),
    },
    "focus": {
        "ring": color("{palette.focusBlue}", COMP + ", outlineColor after Tab on a.btn."),
    },
}

doc = {
    "core": core,
    "light": light,
    "$themes": [{"id": "light", "name": "Light", "selectedTokenSets": {"core": "source", "light": "enabled"}}],
    "$extensions": {
        "notTokenised": [
            "Webflow starter status colours are declared and unused on the captured pages. They stay in core.palette.starter and are not semantic roles.",
            "prefers-color-scheme: dark did not change body, text or footer. No dark set.",
            "No theme-color meta, no mask-icon, no web manifest.",
            "Disabled, loading, pressed colour, error-on-field, toast, dialog, menu, tabs, fields, checkbox, radio, switch, table, avatar and badge were not on the public pages.",
        ]
    },
}

# checks
DIM = re.compile(r"-?\d*\.?\d+(px|rem)|50%")


def walk(node, path=""):
    if isinstance(node, dict) and "$value" in node:
        if "$extensions" not in node or "source" not in node["$extensions"]:
            raise SystemExit(f"missing source: {path}")
        typ = node["$type"]
        val = node["$value"]
        if typ == "color" and isinstance(val, str) and not val.startswith("{") and not val.startswith("#") and not val.startswith("rgba"):
            raise SystemExit(f"bad color {path}: {val}")
        if typ == "dimension" and isinstance(val, str) and not val.startswith("{") and not DIM.fullmatch(val):
            raise SystemExit(f"bad dimension {path}: {val}")
        return
    if isinstance(node, dict):
        for k, v in node.items():
            if k.startswith("$"):
                continue
            walk(v, path + "." + k)


walk(doc)
out = HERE / "tokens.json"
out.write_text(json.dumps(doc, indent=1) + "\n")
print("wrote", out, "bytes", out.stat().st_size)
