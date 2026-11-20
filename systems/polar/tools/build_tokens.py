#!/usr/bin/env python3
"""Write tokens.json from raw/foundations.json.

The values in raw/foundations.json were read with getComputedStyle on polar.sh
on 2026-11-19. This script does not invent colours. Lab colours were converted
to hex by filling a 1x1 canvas in that same page. Re-run only after updating
the raw file.
"""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = json.loads((HERE / "raw" / "foundations.json").read_text())
OUT = HERE / "tokens.json"


def tok(type_, value, source):
    return {
        "$type": type_,
        "$value": value,
        "$extensions": {"source": source},
    }


def color(value, source):
    return tok("color", value, source)


def dim(value, source):
    return tok("dimension", value, source)


def build():
    src = RAW["source"]
    polar = RAW["polar"]
    semantic_dark = RAW["semanticDark"]
    semantic_light_docs = RAW["semanticLightDocs"]
    blue = RAW["blue"]
    status = RAW["status"]
    type_ = RAW["type"]
    radius = RAW["radius"]
    space = RAW["space"]
    motion = RAW["motion"]
    components = RAW["components"]

    core = {
        "color": {
            "polar": {k: color(v, src + " --color-polar-" + k) for k, v in polar.items()},
            "blue": {k: color(v, src + " canvas hex of --color-blue-" + k) for k, v in blue.items()},
            "white": color("#ffffff", src + " --color-white"),
            "black": color("#000000", src + " --color-black"),
            "red": {
                "400": color(status["red400"], src + " canvas hex of --color-red-400"),
                "500": color(status["red500"], src + " canvas hex of --color-red-500"),
                "600": color(status["red600"], src + " canvas hex of --color-red-600"),
            },
            "green": {"500": color(status["green500"], src + " canvas hex of --color-green-500")},
            "amber": {"500": color(status["amber500"], src + " canvas hex of --color-amber-500")},
            "yellow": {"500": color(status["yellow500"], src + " canvas hex of --color-yellow-500")},
        },
        "font": {
            "family": {
                "sans": tok("fontFamily", type_["sans"], src + " --font-sans"),
                "display": tok("fontFamily", type_["display"], src + " --font-display"),
                "mono": tok("fontFamily", type_["mono"], src + " --font-mono"),
                "docs": tok("fontFamily", type_["docs"], src + " docs body fontFamily"),
                "docsMono": tok("fontFamily", type_["docsMono"], src + " docs code fontFamily"),
            },
            "weight": {
                "regular": tok("fontWeight", 450, src + " computed font-weight on body text"),
                "medium": tok("fontWeight", 500, src + " blog h1 font-weight"),
                "button": tok("fontWeight", 550, src + " button font-[550]"),
                "semibold": tok("fontWeight", 600, src + " docs h1 font-weight"),
                "bold": tok("fontWeight", 700, src + " pricing th font-weight"),
            },
            "size": {
                "xs": dim("12px", src + " auth legal links"),
                "sm": dim("14px", src + " button and email field"),
                "md": dim("16px", src + " body"),
                "lg": dim("18px", src + " docs lede and pricing h3"),
                "xl": dim("20px", src + " blog lede"),
                "2xl": dim("24px", src + " feature h3 and auth h2"),
                "3xl": dim("30px", src + " section h2"),
                "4xl": dim("36px", src + " home h1"),
                "5xl": dim("60px", src + " pricing h1"),
                "6xl": dim("72px", src + " blog post h1"),
            },
            "leading": {
                "body": dim("24px", src + " body line-height"),
                "button": dim("20px", src + " button line-height"),
                "h1": dim("45px", src + " home h1 line-height"),
                "h2": dim("41.25px", src + " section h2 line-height"),
                "display": dim("72px", src + " blog post h1 line-height"),
                "pricing": dim("75px", src + " pricing h1 line-height"),
            },
            "tracking": {
                "body": dim("0.24px", src + " body letter-spacing"),
                "button": dim("0.14px", src + " button letter-spacing 0.01em at 14px"),
            },
        },
        "radius": {k: dim(v, src + " " + note) for k, (v, note) in radius.items()},
        "space": {k: dim(v, src + " " + note) for k, (v, note) in space.items()},
        "motion": {
            "duration": {
                "fast": tok("duration", motion["fast"], src + " --default-transition-duration"),
                "accordion": tok("duration", motion["accordion"], src + " --animate-accordion-down"),
            },
            "easing": {
                "standard": tok("cubicBezier", [0.4, 0, 0.2, 1], src + " --default-transition-timing-function"),
                "out": tok("cubicBezier", [0, 0, 0.2, 1], src + " --ease-out"),
            },
        },
        "typography": {
            "body": tok("typography", {
                "fontFamily": "{font.family.sans}",
                "fontWeight": "{font.weight.regular}",
                "fontSize": "{font.size.md}",
                "lineHeight": "{font.leading.body}",
                "letterSpacing": "{font.tracking.body}",
            }, src + " body computed font"),
            "button": tok("typography", {
                "fontFamily": "{font.family.display}",
                "fontWeight": "{font.weight.button}",
                "fontSize": "{font.size.sm}",
                "lineHeight": "{font.leading.button}",
                "letterSpacing": "{font.tracking.button}",
            }, src + " Get Started button"),
            "h1": tok("typography", {
                "fontFamily": "{font.family.sans}",
                "fontWeight": "{font.weight.regular}",
                "fontSize": "{font.size.4xl}",
                "lineHeight": "{font.leading.h1}",
            }, src + " home h1 Meet Polar"),
            "h2": tok("typography", {
                "fontFamily": "{font.family.sans}",
                "fontWeight": "{font.weight.regular}",
                "fontSize": "{font.size.3xl}",
                "lineHeight": "{font.leading.h2}",
            }, src + " home h2"),
            "display": tok("typography", {
                "fontFamily": "{font.family.display}",
                "fontWeight": "{font.weight.medium}",
                "fontSize": "{font.size.6xl}",
                "lineHeight": "{font.leading.display}",
            }, src + " blog post h1"),
            "docsTitle": tok("typography", {
                "fontFamily": "{font.family.docs}",
                "fontWeight": "{font.weight.semibold}",
                "fontSize": "{font.size.4xl}",
                "lineHeight": "40px",
            }, src + " docs h1"),
        },
    }

    def semantic(values, label):
        return {
            "surface": {
                "page": color(values["page"], label + " page"),
                "raised": color(values["raised"], label + " raised"),
                "sunken": color(values["sunken"], label + " sunken"),
                "header": color(values["header"], label + " header"),
            },
            "text": {
                "primary": color(values["text"], label + " text"),
                "secondary": color(values["muted"], label + " muted"),
                "onAccent": color(values["onAccent"], label + " on accent"),
            },
            "accent": color(values["accent"], label + " accent"),
            "border": {"default": color(values["border"], label + " border")},
            "status": {
                "danger": color(values["danger"], label + " danger"),
                "success": color(values["success"], label + " success"),
            },
        }

    light = semantic(semantic_light_docs, src + " docs light")
    dark = semantic(semantic_dark, src + " marketing dark")
    dark["component"] = {
        "button": {
            "primary": {
                "bg": color(components["primaryButton"]["bg"], src + " Get Started background"),
                "text": color(components["primaryButton"]["text"], src + " Get Started color"),
                "radius": dim(components["primaryButton"]["radius"], src + " Get Started border-radius pill"),
                "padding": dim("12px", src + " header Get Started padding-block"),
                "height": dim("40px", src + " header Get Started height"),
            },
            "ghost": {
                "bg": color(components["ghostButton"]["bg"], src + " Sign in background"),
                "text": color(components["ghostButton"]["text"], src + " Sign in color"),
                "radius": dim(components["ghostButton"]["radius"], src + " Sign in border-radius pill"),
                "height": dim("40px", src + " Sign in height"),
            },
            "secondary": {
                "bg": color(components["secondaryButton"]["bg"], src + " Sign in with Apple background"),
                "text": color(components["secondaryButton"]["text"], src + " Sign in with Apple color"),
                "radius": dim("9999px", src + " auth secondary button pill"),
                "height": dim("40px", src + " auth secondary button height"),
            },
        },
        "field": {
            "email": {
                "bg": color(components["field"]["bg"], src + " auth email background"),
                "text": color(components["field"]["text"], src + " auth email color"),
                "radius": dim(components["field"]["radius"], src + " auth email border-radius"),
                "height": dim("40px", src + " auth email height"),
                "padding": dim("8px", src + " auth email padding-block"),
            }
        },
        "nav": {
            "height": dim("72px", src + " marketing nav height"),
            "padding": dim("16px", src + " marketing nav padding-block"),
        },
        "code": {
            "bg": color(components["code"]["bg"], src + " blog pre background"),
            "text": color(components["code"]["text"], src + " blog pre color"),
            "radius": dim(components["code"]["radius"], src + " blog pre border-radius"),
        },
    }

    doc = {
        "$schema": "https://www.designtokens.org/schemas/2025.10/format/",
        "core": core,
        "light": light,
        "dark": dark,
        "$themes": [
            {"name": "light", "selectedTokenSets": {"core": "source", "light": "enabled"}},
            {"name": "dark", "selectedTokenSets": {"core": "source", "dark": "enabled"}},
        ],
    }
    return doc


def main():
    """Write tokens.json; build() alone writes nothing."""
    OUT.write_text(json.dumps(build(), indent=2) + "\n")
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()
