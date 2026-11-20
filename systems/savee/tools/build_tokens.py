#!/usr/bin/env python3
"""Write tokens.json from raw/foundations.json.

Values were read with getComputedStyle on savee.com on 2026-11-19. This
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
    light = RAW["colors"]["light"]
    dark = RAW["colors"]["dark"]
    gray = RAW["colors"]["baseGray"]
    named = RAW["colors"]["named"]
    fonts = RAW["type"]["family"]
    roles = RAW["type"]["roles"]
    radius = RAW["radius"]
    motion = RAW["motion"]

    core = {
        "color": {
            "gray": {k: color(v, src + " --color-base-gray-" + k) for k, v in gray.items()},
            "white": color("#fdfdfd", src + " --color-base-white"),
            "black": color("#0a0a0a", src + " --color-base-black"),
            "pageDark": color("#0e0e0e", src + " --color-base-page-dark"),
            "shell": color(light["shell"], src + " home shell bg-[#F3F3F3]"),
            "brand": color(named["brand"], src + " --color-base-brand"),
            "brand2": color(named["brand2"], src + " --color-base-brand-2"),
            "destructive": color(named["destructive"], src + " --color-destructive"),
            "like": color(named["like"], src + " --color-like"),
            "available": color(named["available"], src + " --color-available"),
        },
        "font": {
            "family": {
                "sans": tok("fontFamily", fonts, src + " body font-family"),
                "italic": tok("fontFamily", RAW["type"]["italicFamily"], src + " --font-savee-italic, unloaded"),
            },
            "weight": {
                "regular": tok("fontWeight", 400, src + " body font-weight"),
                "medium": tok("fontWeight", 500, src + " h1 and primary button font-weight"),
                "semibold": tok("fontWeight", 600, src + " faq h1 font-weight"),
            },
            "size": {
                "tooltip": dim("11px", src + " " + roles["tooltip"]["where"]),
                "badge": dim("13px", src + " " + roles["badge"]["where"]),
                "legal": dim("13px", src + " " + roles["legal"]["where"]),
                "sm": dim("14px", src + " " + roles["buttonSm"]["where"]),
                "body": dim("16px", src + " " + roles["body"]["where"]),
                "searchChip": dim("18px", src + " home search chip burnt orange"),
                "lede": dim("21px", src + " " + roles["lede"]["where"]),
                "faqQuestion": dim("30px", src + " " + roles["faqQuestion"]["where"]),
                "auth": dim("35.07px", src + " " + roles["authTitle"]["where"]),
                "price": dim("48px", src + " " + roles["price"]["where"]),
                "section": dim("52.605px", src + " " + roles["section"]["where"]),
                "faq": dim("60px", src + " " + roles["faqTitle"]["where"]),
                "featuresHero": dim("70.14px", src + " " + roles["featuresHero"]["where"]),
                "hero": dim("77.7385px", src + " " + roles["hero"]["where"]),
            },
        },
        "typography": {
            "hero": {
                "$type": "typography",
                "$value": {
                    "fontFamily": fonts,
                    "fontSize": roles["hero"]["size"],
                    "fontWeight": roles["hero"]["weight"],
                    "lineHeight": roles["hero"]["lineHeight"],
                    "letterSpacing": roles["hero"]["letterSpacing"],
                },
                "$extensions": {"source": src + " " + roles["hero"]["where"]},
            },
            "section": {
                "$type": "typography",
                "$value": {
                    "fontFamily": fonts,
                    "fontSize": roles["section"]["size"],
                    "fontWeight": roles["section"]["weight"],
                    "lineHeight": roles["section"]["lineHeight"],
                    "letterSpacing": roles["section"]["letterSpacing"],
                },
                "$extensions": {"source": src + " " + roles["section"]["where"]},
            },
            "authTitle": {
                "$type": "typography",
                "$value": {
                    "fontFamily": fonts,
                    "fontSize": roles["authTitle"]["size"],
                    "fontWeight": roles["authTitle"]["weight"],
                    "lineHeight": roles["authTitle"]["lineHeight"],
                    "letterSpacing": roles["authTitle"]["letterSpacing"],
                },
                "$extensions": {"source": src + " " + roles["authTitle"]["where"]},
            },
            "body": {
                "$type": "typography",
                "$value": {
                    "fontFamily": fonts,
                    "fontSize": "16px",
                    "fontWeight": 400,
                    "lineHeight": "24px",
                    "letterSpacing": "0px",
                },
                "$extensions": {"source": src + " body"},
            },
            "nav": {
                "$type": "typography",
                "$value": {
                    "fontFamily": "saveeFont, \"saveeFont Fallback\"",
                    "fontSize": "16px",
                    "fontWeight": 500,
                    "lineHeight": "22px",
                    "letterSpacing": "-0.16px",
                },
                "$extensions": {"source": src + " home nav links"},
            },
            "button": {
                "$type": "typography",
                "$value": {
                    "fontFamily": "saveeFont, \"saveeFont Fallback\"",
                    "fontSize": "16px",
                    "fontWeight": 500,
                    "lineHeight": "16px",
                    "letterSpacing": "-0.16px",
                },
                "$extensions": {"source": src + " hero Join for free"},
            },
        },
        "radius": {
            "xs": dim("2px", src + " --radius-xs"),
            "sm": dim("4px", src + " --radius-sm"),
            "md": dim("6px", src + " --radius-md and --grid-corner-radius"),
            "lg": dim("8px", src + " --radius-lg and login save tile and tooltip"),
            "xl": dim("12px", src + " --radius-xl"),
            "tile": dim("16px", src + " Save tile rounded-2xl"),
            "field": dim("14px", src + " contact field"),
            "plan": dim("24px", src + " pricing card rounded-3xl"),
            "4xl": dim("32px", src + " --radius-4xl"),
            "pill": dim("16777200px", src + " pill button computed border-radius"),
        },
        "spacing": {
            "unit": dim("4px", src + " --spacing 0.25rem"),
            "2": dim("8px", src + " tooltip padding 4px 8px"),
            "3": dim("12px", src + " field padding top"),
            "4": dim("16px", src + " field padding and nav button padding-y"),
            "5": dim("20px", src + " hero button padding-y"),
            "8": dim("32px", src + " plan card padding"),
            "10": dim("40px", src + " hero button padding-x"),
            "nav": dim("64px", src + " rendered nav height"),
            "navToken": dim("100px", src + " --nav-height, not the rendered bar"),
            "page": dim("33px", src + " --page-margin round(100px / 3)"),
        },
        "motion": {
            "duration": {
                "default": tok("duration", "150ms", src + " --default-transition-duration"),
                "over": tok("duration", "180ms", src + " --transition-duration-over"),
                "overLong": tok("duration", "300ms", src + " --transition-duration-over-long"),
                "slide": tok("duration", "350ms", src + " --transition-duration-slide"),
            },
            "easing": {
                "default": tok("cubicBezier", [0.4, 0, 0.2, 1], src + " --default-transition-timing-function"),
                "inOut": tok("cubicBezier", [0.3, 0, 0, 1], src + " --ease-in-out"),
                "out": tok("cubicBezier", [0.25, 0.25, 0, 1], src + " --ease-out"),
                "in": tok("cubicBezier", [0.875, 0, 0.05, 1], src + " --ease-in"),
                "outExpo": tok("cubicBezier", [0.16, 1, 0.3, 1], src + " --ease-out-expo"),
            },
        },
    }

    light_set = {
        "surface": {
            "page": color(light["page"], src + " theme-light html background"),
            "shell": color(light["shell"], src + " home shell"),
            "raised": color(light["card"], src + " theme-light --color-card"),
            "popover": color(light["popover"], src + " theme-light --color-popover"),
        },
        "text": {
            "primary": color(light["text"], src + " theme-light h1"),
            "body": color(light["body"], src + " theme-light body"),
            "secondary": color(light["muted"], src + " theme-light --color-muted-foreground"),
            "footer": color(light["footerLink"], src + " footer link"),
            "onAccent": color("#fdfdfd", src + " primary button text"),
        },
        "accent": color(light["text"], src + " primary button background, theme-light"),
        "border": {
            "default": color(light["border"], src + " theme-light --color-border"),
            "strong": color("#0a0a0a", src + " login field border-bottom"),
            "ring": color(light["ring"], src + " theme-light --color-ring"),
            "social": color("#c4c4c4", src + " Continue with Google ring"),
        },
        "status": {
            "destructive": color(named["destructive"], src + " --color-destructive"),
            "like": color(named["like"], src + " --color-like"),
            "available": color(named["available"], src + " --color-available"),
            "brand": color(named["brand"], src + " --color-brand"),
        },
        "component": {
            "button": {
                "bg": color("#0a0a0a", src + " Join for free background"),
                "text": color("#fdfdfd", src + " Join for free color"),
                "radius": dim("16777200px", src + " pill button radius"),
                "padding": dim("20px", src + " hero button padding-block"),
                "height": dim("56px", src + " hero button height"),
            },
            "field": {
                "text": color("#0a0a0a", src + " login field color"),
                "radius": dim("0px", src + " login field radius"),
                "height": dim("49px", src + " login field height"),
            },
        },
    }

    dark_set = {
        "surface": {
            "page": color(dark["page"], src + " theme-dark body background"),
            "shell": color(dark["page"], src + " theme-dark body background"),
            "raised": color(dark["card"], src + " theme-dark --color-card"),
            "popover": color(dark["popover"], src + " theme-dark --color-popover"),
        },
        "text": {
            "primary": color(dark["text"], src + " theme-dark contact h1"),
            "body": color(dark["body"], src + " theme-dark --color-foreground"),
            "secondary": color(dark["muted"], src + " theme-dark --color-muted-foreground"),
            "footer": color(dark["quiet"], src + " faq quiet text"),
            "onAccent": color("#0e0e0e", src + " theme-dark primary button text"),
        },
        "accent": color("#fdfdfd", src + " theme-dark Join for free background"),
        "border": {
            "default": color(dark["border"], src + " theme-dark --color-border"),
            "strong": color("#e5e5e5", src + " contact focus ring"),
            "ring": color(dark["ring"], src + " theme-dark --color-ring"),
            "social": color("#c4c4c4", "Reconstruction: the light social ring reading (" + src
                            + "), copied into dark by hand at capture time; not remeasured in dark"),
        },
        "status": {
            "destructive": color(named["destructive"], src + " --color-destructive"),
            "like": color(named["like"], src + " --color-like"),
            "available": color(named["available"], src + " --color-available"),
            "brand": color(named["brand"], src + " --color-brand"),
        },
        "component": {
            "button": {
                "bg": color("#fdfdfd", src + " theme-dark Join for free background"),
                "text": color("#0e0e0e", src + " theme-dark Join for free color"),
                "radius": dim("16777200px", src + " pill button radius"),
                "padding": dim("20px", src + " Contact us padding-block"),
                "height": dim("56px", src + " Contact us height"),
            },
            "field": {
                "bg": color("#1e1e1e", src + " contact field background"),
                "text": color("#a3a3a3", src + " contact field color"),
                "radius": dim("14px", src + " contact field radius"),
                "height": dim("46px", src + " contact field height"),
            },
        },
    }

    doc = {
        "$schema": "https://www.designtokens.org/schemas/2025.10/format/",
        "core": core,
        "light": light_set,
        "dark": dark_set,
        "$themes": [
            {"name": "light", "selectedTokenSets": {"core": "source", "light": "enabled"}},
            {"name": "dark", "selectedTokenSets": {"core": "source", "dark": "enabled"}},
        ],
    }
    return doc


def render():
    """tokens.json's exact text; nothing is written."""
    return json.dumps(build(), indent=2) + "\n"


if __name__ == "__main__":
    OUT.write_text(render())
    print(f"wrote {OUT}")
