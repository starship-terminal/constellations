#!/usr/bin/env python3
"""Write tokens.json from raw/foundations.json.

Values were read with getComputedStyle on stellate.co on 2026-11-19. This
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
    c = RAW["colors"]
    fonts = RAW["fonts"]
    core = {
        "color": {
            "neutral": color(c["neutral"], src + " body color rgb(59, 76, 106)"),
            "neutral110": color(c["neutral110"], src + " h1 text-neutral-110"),
            "blue": color(c["blue"], src + " .bg-blue"),
            "blue110": color(c["blue110"], src + " .bg-blue-110"),
            "magenta": color(c["magenta"], src + " .bg-magenta"),
            "red": color(c["red"], src + " .bg-red"),
            "purple": color(c["purple"], src + " .bg-purple"),
            "yellow": color(c["yellow"], src + " .bg-yellow"),
            "green": color(c["green"], src + " .text-green"),
            "grey": color(c["grey"], src + " .bg-grey page"),
            "gray150": color(c["gray150"], src + " header Get started bg-gray-150"),
            "white": color(c["white"], src + " .bg-white"),
            "github": color(c["github"], src + " Login with GitHub background"),
            "gitlab": color(c["gitlab"], src + " Login with GitLab background"),
            "docsDarkPage": color(c["docsDarkPage"], src + " docs html.dark background"),
            "docsLightPage": color(c["docsLightPage"], src + " docs html.light background"),
        },
        "font": {
            "family": {
                "sans": tok("fontFamily", fonts["sans"], src + " computed font-family ttCommons"),
                "mono": tok("fontFamily", fonts["mono"], src + " @font-face Fira Code"),
                "docs": tok("fontFamily", fonts["docs"], src + " docs body font-family"),
            },
            "weight": {
                "regular": tok("fontWeight", 400, src + " body font-weight 400"),
                "medium": tok("fontWeight", 450, src + " font-medium computed 450"),
                "demibold": tok("fontWeight", 550, src + " font-demibold computed 550"),
                "bold": tok("fontWeight", 650, src + " font-bold computed 650"),
            },
            "size": {
                "sm": dim("13px", src + " signup legal link font-size"),
                "nav": dim("15px", src + " nav link font-size"),
                "body": dim("16px", src + " body font-size"),
                "docs": dim("17px", src + " docs paragraph font-size"),
                "button": dim("15px", src + " marketing button font-size"),
                "field": dim("18px", src + " email field font-size"),
                "h2": dim("38px", src + " home h2 lg:text-38"),
                "h1": dim("48px", src + " home h1 lg:text-48"),
                "display": dim("64px", src + " product page h1"),
            },
        },
        "radius": {
            "sm": dim("4px", src + " docs sidebar link and search kbd border-radius 4px"),
            "md": dim("6px", src + " .rounded-6 and field border-radius"),
            "lg": dim("8px", src + " .rounded-8 marketing button"),
            "xl": dim("12px", src + " .rounded-12 menu and cookie banner"),
            "2xl": dim("16px", src + " .rounded-2xl 1rem"),
        },
        "spacing": {
            "2": dim("8px", src + " menu column padding p-2"),
            "3": dim("12px", src + " OAuth button vertical padding"),
            "4": dim("16px", src + " marketing button horizontal padding"),
            "5": dim("20px", src + " header vertical padding and menu item padding"),
            "6": dim("24px", src + " section horizontal padding px-6"),
            "8": dim("32px", src + " cookie banner and pricing card padding"),
        },
        "typography": {
            "body": {
                "$type": "typography",
                "$value": {
                    "fontFamily": fonts["sans"],
                    "fontSize": "16px",
                    "fontWeight": 400,
                    "lineHeight": "24px",
                },
                "$extensions": {"source": src + " body computed type"},
            },
            "nav": {
                "$type": "typography",
                "$value": {
                    "fontFamily": fonts["sans"],
                    "fontSize": "15px",
                    "fontWeight": 550,
                    "lineHeight": "22.5px",
                },
                "$extensions": {"source": src + " nav Pricing link"},
            },
            "h1": {
                "$type": "typography",
                "$value": {
                    "fontFamily": fonts["sans"],
                    "fontSize": "48px",
                    "fontWeight": 650,
                    "lineHeight": "52.8px",
                },
                "$extensions": {"source": src + " home h1"},
            },
            "h2": {
                "$type": "typography",
                "$value": {
                    "fontFamily": fonts["sans"],
                    "fontSize": "38px",
                    "fontWeight": 650,
                    "lineHeight": "57px",
                },
                "$extensions": {"source": src + " home h2"},
            },
            "button": {
                "$type": "typography",
                "$value": {
                    "fontFamily": fonts["sans"],
                    "fontSize": "15px",
                    "fontWeight": 550,
                    "lineHeight": "15px",
                },
                "$extensions": {"source": src + " Get started for free"},
            },
            "field": {
                "$type": "typography",
                "$value": {
                    "fontFamily": fonts["sans"],
                    "fontSize": "18px",
                    "fontWeight": 450,
                    "lineHeight": "20px",
                },
                "$extensions": {"source": src + " login email field"},
            },
        },
        "motion": {
            "duration": {
                "default": tok("duration", "250ms", src + " .transition duration 0.25s"),
            },
            "easing": {
                "standard": tok("cubicBezier", [0.25, 0, 0, 1], src + " .transition timing-function"),
            },
        },
    }
    light = {
        "surface": {
            "page": color(c["grey"], src + " marketing and auth page .bg-grey"),
            "raised": color(c["white"], src + " menu, cookie banner and pricing card background"),
            "inverse": color(c["neutral110"], src + " home dark band .bg-neutral-110"),
        },
        "text": {
            "primary": color(c["neutral110"], src + " home h1 color"),
            "secondary": color(c["neutral"], src + " body and nav color"),
            "muted": color(c["gray600"], src + " .text-gray-600 placeholder"),
            "onAccent": color(c["white"], src + " blue button text"),
            "inverse": color(c["grey"], src + " dark band h2 color rgb(248, 250, 252)"),
        },
        "accent": color(c["blue"], src + " .bg-blue primary"),
        "accentHover": color(c["blue110"], src + " hover:bg-blue-110 declared, not shown"),
        "border": {
            "default": color(c["borderHex"], src + " .border-neutral-25-hex"),
            # The alpha is kept (0.15 -> 26). raw/ holds no reading of this border, so it is a hand entry.
            "subtle": color("#3b4c6a26", "Reconstruction: entered by hand at capture time from the cookie banner "
                            "border, computed rgba(59, 76, 106, 0.15) (" + src + "); no raw/ file holds this reading"),
        },
        "status": {
            "magenta": color(c["magenta"], src + " Metrics button"),
            "red": color(c["red"], src + " Security button and Reject All"),
            "green": color(c["green"], src + " .text-green"),
            "yellow": color(c["yellow"], src + " .bg-yellow"),
        },
        "component": {
            "button": {
                "bg": color(c["blue"], src + " Get started for free is gray; Learn more about Caching is blue. Primary accent button uses blue"),
                "text": color(c["white"], src + " blue button text"),
                "radius": dim("8px", src + " marketing button border-radius"),
                "height": dim("40px", src + " marketing button height"),
                "padding": dim("16px", src + " marketing button horizontal padding"),
            },
            "field": {
                "bg": color(c["white"], src + " email field background"),
                "text": color(c["blue"], src + " email field color when filled"),
                "radius": dim("6px", src + " email field border-radius"),
                "height": dim("48px", src + " email field height"),
                "padding": dim("17px", src + " email field horizontal padding 17px"),
            },
        },
    }
    dark = {
        "surface": {
            "page": color(c["docsDarkPage"], src + " docs html.dark background #18181b"),
            "raised": color(c["docsDarkPage"], src + " docs kbd background #18181b"),
        },
        "text": {
            "primary": color(c["docsDarkHeading"], src + " docs h1 canvas hex of lab slate-100"),
            "secondary": color(c["docsDarkBody"], src + " docs paragraph canvas hex of lab slate-200"),
            "muted": color(c["docsKbd"], src + " docs search kbd color"),
            "onAccent": color(c["white"], src + " docs Get Started link color"),
        },
        "accent": color(c["docsDarkLink"], src + " docs link rgb(26, 163, 255)"),
        "border": {
            "default": color(c["docsKbdBorder"], src + " docs kbd border lab neutral-800 canvas #262626"),
        },
        "component": {
            "button": {
                "text": color(c["white"], src + " docs Get Started color"),
            },
        },
    }
    doc = {
        "$schema": "https://www.designtokens.org/schemas/2025.10/format/",
        "core": core,
        "light": light,
        "dark": dark,
        "$themes": [
            {"name": "light", "selectedTokenSets": {"core": "enabled", "light": "enabled"}},
            {"name": "dark", "selectedTokenSets": {"core": "enabled", "dark": "enabled"}},
        ],
    }
    return doc


if __name__ == "__main__":
    OUT.write_text(json.dumps(build(), indent=2) + "\n")
    print(OUT)
