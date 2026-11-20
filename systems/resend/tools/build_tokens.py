#!/usr/bin/env python3
"""Write tokens.json from raw/foundations.json.

Values were read with getComputedStyle on resend.com on 2026-11-19. This
script does not invent colours. Re-run only after updating the raw file.
"""
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = json.loads((HERE / "raw" / "foundations.json").read_text())
OUT = HERE / "tokens.json"


def tok(type_, value, source):
    return {"$type": type_, "$value": value, "$extensions": {"source": source}}


def color(value, source):
    return tok("color", value, source)


def dim(value, source):
    return tok("dimension", value, source)


def gradient_base(component):
    """The first stop of a measured linear-gradient fill, as #rrggbbaa. A missing or unparseable
    reading fails the build rather than falling back to a guessed opaque fill."""
    image = (RAW["components"].get(component) or {}).get("backgroundImage", "")
    # The first stop is the first colour after the optional angle or direction; it must be rgba().
    m = re.match(r"linear-gradient\(\s*(?:[^,()]+,\s*)?rgba\((\d+),\s*(\d+),\s*(\d+),\s*([\d.]+)\)", image)
    if not m:
        raise SystemExit(f"{component} backgroundImage is not a readable linear-gradient: {image!r}")
    r, g, b = (int(m.group(i)) for i in (1, 2, 3))
    return "#%02x%02x%02x%02x" % (r, g, b, round(float(m.group(4)) * 255)), image


def build():
    src = RAW["source"]
    c = RAW["colors"]
    t = RAW["type"]
    fonts = RAW["fonts"]
    gray = {k: color(v, src + " --gray-" + k) for k, v in c["gray"].items()}
    core = {
        "color": {
            "gray": gray,
            "white": color(c["white"], src + " --color-white"),
            "black": color(c["black"], src + " --color-black"),
            "forge": {
                "green": color(c["forgeGreen"], src + " --color-forge-green"),
                "red": color(c["forgeRed"], src + " --color-forge-red"),
            },
            "automationOrange": color(c["automationOrange"], src + " --color-automation-orange"),
            "code": color(c["codeText"], src + " home code sample color"),
        },
        "font": {
            "family": {
                "sans": tok("fontFamily", fonts["sans"], src + " --font-sans"),
                "display": tok("fontFamily", fonts["display"], src + " --font-display"),
                "hero": tok("fontFamily", fonts["hero"], src + " h1 font-family domaine"),
                "mono": tok("fontFamily", fonts["mono"], src + " --font-mono"),
                "docs": tok("fontFamily", fonts["docs"], src + " docs body fontFamily"),
            },
            "weight": {
                "regular": tok("fontWeight", 400, src + " body and hero font-weight"),
                "medium": tok("fontWeight", 500, src + " nav link and auth h1 font-weight"),
                "semibold": tok("fontWeight", 600, src + " button and docs h1 font-weight"),
            },
            "size": {
                "xs": dim("12px", src + " password hint and status link"),
                "sm": dim("14px", src + " nav, label, button"),
                "md": dim("16px", src + " body and field"),
                "lg": dim("18px", src + " home lede"),
                "xl": dim("20px", src + " feature h2"),
                "auth": dim("28px", src + " auth h1"),
                "docs": dim("36px", src + " docs h1"),
                "section": dim("56px", src + " marketing h2"),
                "pricing": dim("76.8px", src + " pricing h1 at 1169px"),
                "hero": dim("96px", src + " home h1 at 1169px"),
            },
        },
        "typography": {
            "hero": {
                "$type": "typography",
                "$value": {
                    "fontFamily": fonts["hero"],
                    "fontSize": "96px",
                    "fontWeight": 400,
                    "lineHeight": "96px",
                    "letterSpacing": "-0.96px",
                },
                "$extensions": {"source": src + " home h1"},
            },
            "section": {
                "$type": "typography",
                "$value": {
                    "fontFamily": fonts["displayComputed"],
                    "fontSize": "56px",
                    "fontWeight": 400,
                    "lineHeight": "67.2px",
                    "letterSpacing": "-2.8px",
                },
                "$extensions": {"source": src + " home h2"},
            },
            "authTitle": {
                "$type": "typography",
                "$value": {
                    "fontFamily": fonts["displayComputed"],
                    "fontSize": "28px",
                    "fontWeight": 500,
                    "lineHeight": "34px",
                    "letterSpacing": "-0.72px",
                },
                "$extensions": {"source": src + " login h1"},
            },
            "docsTitle": {
                "$type": "typography",
                "$value": {
                    "fontFamily": fonts["docs"],
                    "fontSize": "36px",
                    "fontWeight": 600,
                    "lineHeight": "40px",
                },
                "$extensions": {"source": src + " docs h1"},
            },
            "lede": {
                "$type": "typography",
                "$value": {
                    "fontFamily": "Inter Website",
                    "fontSize": "18px",
                    "fontWeight": 400,
                    "lineHeight": "27px",
                },
                "$extensions": {"source": src + " home lede"},
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
                    "fontFamily": fonts["sans"],
                    "fontSize": "14px",
                    "fontWeight": 600,
                    "lineHeight": "20px",
                },
                "$extensions": {"source": src + " header Get started"},
            },
            "code": {
                "$type": "typography",
                "$value": {
                    "fontFamily": fonts["mono"],
                    "fontSize": "14px",
                    "fontWeight": 400,
                    "lineHeight": "20px",
                },
                "$extensions": {"source": src + " home pre"},
            },
        },
        "radius": {
            "xs": dim("2px", src + " --radius-xs 0.125rem"),
            "sm": dim("4px", src + " --radius-sm 0.25rem"),
            "md": dim("6px", src + " --radius-md 0.375rem"),
            "lg": dim("8px", src + " --radius-lg 0.5rem"),
            "xl": dim("12px", src + " --radius-xl 0.75rem"),
            "2xl": dim("16px", src + " button, field and pricing card"),
            "3xl": dim("24px", src + " --radius-3xl 1.5rem"),
            "4xl": dim("32px", src + " --radius-4xl 2rem"),
        },
        "spacing": {
            "1": dim("4px", src + " --spacing 0.25rem"),
            "2": dim("8px", src + " 2 steps of --spacing"),
            "3": dim("12px", src + " auth h1 letter context and field pad start"),
            "4": dim("16px", src + " button padding and code pad"),
            "5": dim("20px", src + " hero button horizontal padding"),
            "6": dim("24px", src + " pricing card padding"),
        },
    }
    dark = {
        "surface": {
            "page": color(c["page"], src + " body background and --background"),
            "raised": color(c["gray"]["1"], src + " --gray-1"),
            "overlay": color("#000000", src + " --bg-overlay painted opaque"),
        },
        "text": {
            "primary": color(c["text"], src + " body color --gray-12"),
            "secondary": color(c["muted"], src + " nav and lede --gray-11"),
            "placeholder": color(c["placeholder"], src + " --text-placeholder --gray-8"),
            "onAccent": color(c["textOnAccent"], src + " --text-on-accent"),
        },
        "accent": color(c["accent"], src + " --bg-accent white"),
        "accentHover": color(c["accentHover"], src + " --bg-accent-hover --gray-12"),
        "border": {
            "default": color(c["gray"]["4"], src + " --gray-4, nearest opaque step to the white/5 field border"),
            "subtle": color(c["gray"]["3"], src + " --gray-3"),
        },
        "status": {
            "forgeGreen": color(c["forgeGreen"], src + " --color-forge-green"),
            "forgeRed": color(c["forgeRed"], src + " --color-forge-red"),
        },
        "component": {
            "button": {
                "bg": color(BUTTON_BG, src + " hero Get started backgroundImage " + BUTTON_IMAGE + ": its first stop. The fill is that translucent gradient over the black page, not an opaque colour"),
                "text": color(c["white"], src + " Get started color"),
                "radius": dim("16px", src + " Get started border-radius"),
                "height": dim("40px", src + " header Get started height"),
                "padding": dim("16px", src + " header Get started horizontal padding"),
            },
            "field": {
                "text": color(c["white"], src + " login email color"),
                "radius": dim("16px", src + " login email border-radius"),
                "height": dim("48px", src + " login email height"),
                "padding": dim("16px", src + " login email horizontal padding"),
            },
        },
    }
    # Docs light was measured (main #ffffff, h1 #161616, search #6f6f6f, border #eeeeee)
# and is kept in raw/foundations.json. It is not a token set: the catalog
# DESIGN.md export prefers a light set over the marketing theme, and marketing
# pages have no light theme.
    doc = {
        "$schema": "https://www.designtokens.org/schemas/2025.10/format/",
        "core": core,
        "dark": dark,
        "$themes": [
            {"name": "dark", "selectedTokenSets": {"core": "enabled", "dark": "enabled"}},
        ],
    }
    return json.dumps(doc, indent=2) + "\n"


BUTTON_BG, BUTTON_IMAGE = gradient_base("getStartedHero")

if __name__ == "__main__":
    OUT.write_text(build())
    print(f"wrote {OUT}")
