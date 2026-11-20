#!/usr/bin/env python3
"""Write tokens.json from raw/foundations.json.

Every value in raw/foundations.json was read with getComputedStyle, or from a
stylesheet rule, on slab.com on 2026-11-19. This script does not invent colours.
Re-run only after updating the raw file.
"""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = json.loads((HERE / "raw" / "foundations.json").read_text())
OUT = HERE / "tokens.json"
SRC = (
    "getComputedStyle on slab.com, 2026-11-19, T3 preview tab, "
    "viewport 1169x731 at devicePixelRatio 2"
)


def tok(type_, value, source):
    return {"$type": type_, "$value": value, "$extensions": {"source": source}}


def color(value, source):
    return tok("color", value, source)


def dim(value, source):
    return tok("dimension", value, source)


def build():
    c = RAW["colors"]
    t = RAW["type"]
    core = {
        "color": {
            "coral": color(c["coral"], SRC + " Get Started background rgb(255, 65, 67)"),
            "coralHover": color(c["coralHover"], SRC + " stylesheet .Button-module--primary:hover rgb(255, 80, 82)"),
            "plum": color(c["plum"], SRC + " home nav and hero background rgb(66, 2, 46)"),
            "plumButton": color(c["plumButton"], SRC + " login Continue background rgb(126, 0, 72)"),
            "plumHover": color(c["plumHover"], SRC + " stylesheet .UntitledButton-module--primary:hover rgb(107, 0, 61)"),
            "plumPressed": color(c["plumPressed"], SRC + " stylesheet .UntitledButton-module--primary:active rgb(86, 0, 49)"),
            "maroon": color(c["maroon"], SRC + " pricing Contact Sales background rgb(116, 20, 72)"),
            "yellow": color(c["yellow"], SRC + " pricing Startup button rgb(252, 180, 21)"),
            "cyan": color(c["cyan"], SRC + " pricing Business button rgb(80, 197, 220)"),
            "slate": color(c["slate"], SRC + " pricing Free button rgb(47, 64, 80)"),
            "white": color(c["white"], SRC + " field and card background"),
            "text": color(c["text"], SRC + " body color rgb(69, 83, 96)"),
            "muted": color(c["muted"], SRC + " footer link color rgb(147, 149, 152)"),
            "ink": color(c["ink"], SRC + " login heading color rgb(51, 51, 51)"),
            "focus": color(c["focusOutline"], "Observed: Chromium's default focus ring (-webkit-focus-ring-color rgb(229, 151, 0), outline auto) on a focused link; Slab does not style link focus, so this is the browser default, not a product colour. " + SRC),
            "google": color(c["google"], SRC + " Sign up with Google background rgb(66, 133, 244)"),
        },
        "font": {
            "family": {
                "whitney": tok("fontFamily", t["whitney"], SRC + " body font-family"),
                "sentinel": tok("fontFamily", t["sentinel"], SRC + " hero h2 font-family"),
                "untitled": tok("fontFamily", t["untitled"], SRC + " login heading font-family"),
                "plex": tok("fontFamily", "IBM Plex Mono, ui-monospace, monospace", SRC + " @font-face IBM Plex Mono, weight 450, declared and not used on the pages opened"),
            },
            "weight": {
                "regular": tok("fontWeight", 400, SRC + " body font-weight"),
                "medium": tok("fontWeight", 500, SRC + " login heading and footer links"),
                "semibold": tok("fontWeight", 600, SRC + " Get Started and Log In"),
                "light": tok("fontWeight", 300, SRC + " pricing h1 font-weight"),
            },
            "size": {
                "category": dim("12px", SRC + " nav category label font-size"),
                "account": dim("14px", SRC + " login field and Continue font-size"),
                "footer": dim("16px", SRC + " footer link font-size"),
                "button": dim("18px", SRC + " Get Started font-size"),
                "body": dim("20px", SRC + " body font-size"),
                "accountTitle": dim("25px", SRC + " login h2 font-size"),
                "h3": dim("36px", SRC + " home h3 font-size"),
                "hero": dim("42px", SRC + " home hero h2 font-size at 1169px"),
                "h1": dim("56px", SRC + " pricing h1 font-size"),
            },
            "leading": {
                "account": dim("17px", SRC + " login field line-height"),
                "button": dim("24px", SRC + " Get Started line-height"),
                "body": dim("32px", SRC + " body line-height"),
                "accountTitle": dim("32px", SRC + " login h2 line-height"),
                "h3": dim("46px", SRC + " home h3 line-height"),
                "hero": dim("52px", SRC + " home hero line-height"),
                "h1": dim("64px", SRC + " pricing h1 line-height"),
            },
            "tracking": {
                "hero": dim("-0.75px", SRC + " home hero letter-spacing"),
                "accountTitle": dim("-0.5px", SRC + " login h2 letter-spacing"),
                "account": dim("-0.2px", SRC + " login field letter-spacing"),
            },
        },
        "radius": {
            "account": dim("2px", SRC + " login input and Continue border-radius"),
            "card": dim("4px", SRC + " login card border-radius"),
            "control": dim("6px", SRC + " Get Started and Work Email border-radius"),
            "pill": dim("18px", SRC + " pricing Annually track border-radius, height 36px so the track is a pill"),
        },
        "spacing": {
            "2": dim("2px", SRC + " Spacing-module xs is 0.2rem; html font-size is 10px"),
            "4": dim("4px", SRC + " Spacing-module sm is 0.4rem at a 10px root"),
            "8": dim("8px", SRC + " Spacing-module step 1 is 0.8rem; account button padding-block"),
            "12": dim("12px", SRC + " Spacing-module md is 1.2rem; field padding-inline"),
            "16": dim("16px", SRC + " Spacing-module step 2 is 1.6rem; short button padding-block"),
            "24": dim("24px", SRC + " Spacing-module step 3 is 2.4rem; short button padding-inline"),
            "32": dim("32px", SRC + " Spacing-module step 4 is 3.2rem"),
            "40": dim("40px", SRC + " Spacing-module step 5 is 4rem"),
            "48": dim("48px", SRC + " login card padding"),
        },
        "typography": {
            "body": tok("typography", {
                "fontFamily": "{font.family.whitney}",
                "fontWeight": "{font.weight.regular}",
                "fontSize": "{font.size.body}",
                "lineHeight": "{font.leading.body}",
            }, SRC + " body computed font"),
            "hero": tok("typography", {
                "fontFamily": "{font.family.sentinel}",
                "fontWeight": "{font.weight.regular}",
                "fontSize": "{font.size.hero}",
                "lineHeight": "{font.leading.hero}",
                "letterSpacing": "{font.tracking.hero}",
            }, SRC + " home hero h2"),
            "h1": tok("typography", {
                "fontFamily": "{font.family.sentinel}",
                "fontWeight": "{font.weight.light}",
                "fontSize": "{font.size.h1}",
                "lineHeight": "{font.leading.h1}",
            }, SRC + " pricing h1"),
            "h3": tok("typography", {
                "fontFamily": "{font.family.sentinel}",
                "fontWeight": "{font.weight.regular}",
                "fontSize": "{font.size.h3}",
                "lineHeight": "{font.leading.h3}",
            }, SRC + " home h3"),
            "button": tok("typography", {
                "fontFamily": "{font.family.whitney}",
                "fontWeight": "{font.weight.semibold}",
                "fontSize": "{font.size.button}",
                "lineHeight": "{font.leading.button}",
            }, SRC + " Get Started"),
            "accountTitle": tok("typography", {
                "fontFamily": "{font.family.untitled}",
                "fontWeight": "{font.weight.medium}",
                "fontSize": "{font.size.accountTitle}",
                "lineHeight": "{font.leading.accountTitle}",
                "letterSpacing": "{font.tracking.accountTitle}",
            }, SRC + " login h2 Welcome back"),
        },
    }
    light = {
        "surface": {
            "page": color(c["white"], SRC + " pricing page and footer background"),
            "hero": color(c["plum"], SRC + " home hero background"),
            "raised": color(c["white"], SRC + " login card background"),
            "soft": color(c["pageSoft"], SRC + " home migration band rgb(252, 252, 253)"),
            "account": color(c["accountPage"], SRC + " login body background rgb(252, 249, 248)"),
        },
        "text": {
            "primary": color(c["text"], SRC + " body color"),
            "onHero": color(c["textOnPlum"], SRC + " hero and plum nav text"),
            "muted": color(c["muted"], SRC + " footer Terms and Privacy"),
            "ink": color(c["ink"], SRC + " login heading"),
            "inkMuted": color(c["inkMuted"], SRC + " stylesheet account description rgb(144, 144, 144)"),
            "heading": color(c["slate"], SRC + " pricing h1 color"),
        },
        "accent": {
            "coral": color(c["coral"], SRC + " primary button"),
            "plum": color(c["plumButton"], SRC + " account primary and pricing pill selected"),
            "link": color(c["linkAccount"], SRC + " login Sign up for Slab rgb(162, 26, 104)"),
        },
        "border": {
            "default": color("#ebecec", SRC + " stylesheet file-other border rgb(235, 236, 236)"),
            "strong": color(c["slate"], SRC + " stylesheet secondary button border"),
            "account": color("#e3e3e3", SRC + " register Sign up with Google border rgb(227, 227, 227)"),
            "focus": color(c["focusOutline"], "Observed: Chromium's default focus ring (-webkit-focus-ring-color rgb(229, 151, 0), outline auto) on a focused link; Slab does not style link focus, so this is the browser default, not a product colour. " + SRC),
        },
        "component": {
            "button": {
                "bg": color(c["coral"], SRC + " Get Started background"),
                "text": color(c["white"], SRC + " Get Started color"),
                "radius": dim("6px", SRC + " Get Started border-radius"),
                "height": dim("56px", SRC + " Get Started height"),
                "padding": dim("16px", SRC + " Get Started padding-block"),
            },
            "field": {
                "bg": color(c["white"], SRC + " Work Email background"),
                "text": color("#000000", SRC + " Work Email color rgb(0, 0, 0)"),
                "radius": dim("6px", SRC + " Work Email border-radius"),
                "height": dim("56px", SRC + " Work Email height"),
            },
        },
    }
    tokens = {
        "$schema": "https://www.designtokens.org/schemas/2025.10/format/",
        "core": core,
        "light": light,
        "$themes": [{
            "id": "light",
            "name": "Light",
            "selectedTokenSets": {"core": "source", "light": "enabled"},
            "$description": "Public slab.com and the signed-out login page. No dark theme rule was found.",
        }],
        "$metadata": {"tokenSetOrder": ["core", "light"]},
    }
    OUT.write_text(json.dumps(tokens, indent=2) + "\n")
    print("wrote", OUT)


if __name__ == "__main__":
    build()
