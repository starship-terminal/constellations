#!/usr/bin/env python3
"""Write tokens.json from raw/foundations.json.

Values were read with getComputedStyle on steel.dev on 2026-11-19. This
script does not invent colours. Re-run only after updating the raw file.
"""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = json.loads((HERE / "raw" / "foundations.json").read_text())
OUT = HERE / "tokens.json"


def tok(type_, value, source):
    return {"$type": type_, "$value": value, "$extensions": {"source": source}}


def color(value, source):
    return tok("color", value, source)


def dim(value, source):
    return tok("dimension", value, source)


def build():
    src = RAW["source"]
    dark = RAW["colors"]["dark"]
    light = RAW["colors"]["light"]
    fonts = RAW["fonts"]
    type_ = RAW["type"]
    motion = RAW["motion"]
    core = {
        "color": {
            "white": color(dark["white"], src + " --color-white"),
            "black": color("#000000", src + " auth primary button text rgb(0, 0, 0)"),
            "focus": color(dark["focus"], src + " --focus-ring"),
            "announce": color(dark["announce"], src + " home announcement bar"),
            "heroBand": color(dark["heroBg"], src + " --hero-bg"),
            "scale": color(dark["scalePlan"], src + " pricing Scale card"),
            "useCase": color(dark["useCaseBand"], src + " home use-case section"),
        },
        "font": {
            "family": {
                "sans": tok("fontFamily", fonts["sans"], src + " --font-sans"),
                "mono": tok("fontFamily", fonts["mono"], src + " --font-mono"),
                "inter": tok("fontFamily", fonts["inter"], src + " --font-inter"),
                "auth": tok("fontFamily", fonts["auth"], src + " auth body fontFamily"),
            }
        },
        "typography": {
            "hero": {
                "$type": "typography",
                "$value": {
                    "fontFamily": fonts["sans"],
                    "fontSize": type_["hero"]["size"],
                    "fontWeight": 400,
                    "lineHeight": type_["hero"]["lineHeight"],
                    "letterSpacing": type_["hero"]["letterSpacing"],
                },
                "$extensions": {"source": src + " home h1"},
            },
            "body": {
                "$type": "typography",
                "$value": {
                    "fontFamily": fonts["sans"],
                    "fontSize": "16px",
                    "fontWeight": 400,
                    "lineHeight": "24px",
                },
                "$extensions": {"source": src + " body"},
            },
            "button": {
                "$type": "typography",
                "$value": {
                    "fontFamily": fonts["mono"],
                    "fontSize": "12px",
                    "fontWeight": 400,
                    "lineHeight": "16px",
                    "letterSpacing": "0.18px",
                },
                "$extensions": {"source": src + " steel-button"},
            },
            "authTitle": {
                "$type": "typography",
                "$value": {
                    "fontFamily": fonts["auth"],
                    "fontSize": "20px",
                    "fontWeight": 500,
                    "lineHeight": "28px",
                },
                "$extensions": {"source": src + " auth h1"},
            },
        },
        "radius": {
            "button": dim("6px", src + " --radius-button"),
            "card": dim("8px", src + " --radius-card"),
            "md": dim("8px", src + " --radius-md"),
            "xs": dim("4px", src + " --radius-xs declared; brand page computed 0px"),
            "badge": dim("2px", src + " pricing POPULAR badge"),
            "search": dim("4px", src + " docs search control"),
        },
        "spacing": {
            "1": dim("4px", src + " --spacing 0.25rem"),
            "2": dim("8px", src + " badge padding and copy button gap"),
            "3": dim("12px", src + " field and button padding"),
            "4": dim("16px", src + " table cell padding and announcement padding"),
            "6": dim("24px", src + " --grid-gap and pricing card padding"),
            "8": dim("32px", src + " phone menu button"),
            "16": dim("64px", src + " auth card padding top"),
            "24": dim("96px", src + " footer padding top"),
        },
        "motion": {
            "duration": {
                "default": tok("duration", "150ms", src + " --default-transition-duration 0.15s"),
                "tooltip": tok("duration", "125ms", src + " --duration-tooltip"),
                "press": tok("duration", "160ms", src + " --duration-press"),
                "dropdown": tok("duration", "180ms", src + " --duration-dropdown"),
                "modal": tok("duration", "240ms", src + " --duration-modal"),
                "drawer": tok("duration", "380ms", src + " --duration-drawer"),
            },
            "easing": {
                "standard": tok("cubicBezier", [0.4, 0, 0.2, 1], src + " --default-transition-timing-function"),
                "out": tok("cubicBezier", [0.23, 1, 0.32, 1], src + " --ease-out and steel-button transition"),
                "in": tok("cubicBezier", [0.4, 0, 1, 1], src + " --ease-in"),
                "inOut": tok("cubicBezier", [0.77, 0, 0.175, 1], src + " --ease-in-out"),
                "drawer": tok("cubicBezier", [0.32, 0.72, 0, 1], src + " --ease-drawer"),
            },
        },
    }
    dark_set = {
        "surface": {
            "page": color(dark["page"], src + " body background and --bg"),
            "docs": color(dark["docsPage"], src + " docs body background"),
            "auth": color(dark["authPage"], src + " auth body background"),
            "raised": color(dark["bgSubtle"], src + " --bg-subtle"),
            "overlay": color("#000000", src + " --overlay painted opaque on black"),
        },
        "text": {
            "primary": color(dark["text"], src + " --text"),
            "secondary": color(dark["muted"], src + " --text-muted"),
            "dim": color(dark["dim"], src + " --text-dim"),
            "onAccent": color(dark["onSolid"], src + " --text-on-solid"),
        },
        "accent": color(dark["accent"], src + " --button-primary"),
        "border": {
            "default": color(dark["border"], src + " --line painted on black"),
            "subtle": color(dark["borderSubtle"], src + " --line-subtle painted on black"),
            "hairline": color(dark["hairline"], src + " --hairline"),
        },
        "status": {
            "danger": color(dark["danger"], src + " --danger-text"),
            "success": color(dark["success"], src + " --success-text"),
            "warning": color(dark["warning"], src + " --warning-solid"),
            "info": color(dark["accentText"], src + " --accent-text"),
            "focus": color(dark["focus"], src + " focused Start for free outline"),
        },
        "component": {
            "button": {
                "bg": color(dark["accent"], src + " START FOR FREE background"),
                "text": color("#141414", src + " START FOR FREE color rgb(20, 20, 20)"),
                "radius": dim("6px", src + " --radius-button"),
                "height": dim("36px", src + " hero steel-button height"),
            },
            "field": {
                "bg": color(dark["field"], src + " auth email input background"),
                "text": color(dark["text"], src + " auth email input color"),
                "radius": dim("6px", src + " auth email input radius"),
                "height": dim("36px", src + " auth email input height"),
            },
        },
    }
    light_set = {
        "surface": {
            "page": color(light["page"], src + " brand-kit Light radio, --bg"),
            "raised": color(light["surface"], src + " brand-kit Light --surface"),
        },
        "text": {
            "primary": color(light["text"], src + " brand-kit Light --text"),
            "secondary": color(light["muted"], src + " brand-kit Light --text-muted"),
            "dim": color(light["dim"], src + " brand-kit Light --text-dim"),
        },
        "accent": color(light["accent"], src + " brand-kit Light --button-primary"),
        "border": {
            "default": color(light["border"], src + " brand-kit Light --line"),
            "subtle": color(light["borderSubtle"], src + " brand-kit Light --line-subtle"),
        },
        "status": {
            "danger": color(light["danger"], src + " brand-kit Light --danger-text"),
            "success": color(light["success"], src + " brand-kit Light --success-text"),
            "focus": color(light["focus"], src + " brand-kit Light --focus-ring"),
        },
    }
    doc = {
        "$schema": "https://www.designtokens.org/schemas/2025.10/format/",
        "core": core,
        "dark": dark_set,
        "light": light_set,
        "$themes": [
            {"id": "dark", "name": "dark", "selectedTokenSets": {"core": "source", "dark": "enabled"}},
            {"id": "light", "name": "light", "selectedTokenSets": {"core": "source", "light": "enabled"}},
        ],
    }
    OUT.write_text(json.dumps(doc, indent=2) + "\n")
    print(f"wrote {OUT}")


if __name__ == "__main__":
    build()
