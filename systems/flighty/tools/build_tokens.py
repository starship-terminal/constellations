#!/usr/bin/env python3
"""Build tokens.json from the public Flighty readings.

Reads raw/home-computed.json, raw/detail-computed.json, and the banner
sample recorded in this file's BANNER constant (median pixel of the
homepage promo strip, sampled before quantise). Every token carries
$extensions.source. Edit the raw files, never tokens.json.
"""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
HOME = json.loads((RAW / "home-computed.json").read_text())
DETAIL = json.loads((RAW / "detail-computed.json").read_text())
D = DETAIL["detail"]
P = DETAIL["pricing"]
NF = DETAIL["notFound"]

# Median of the homepage promo strip, sampled from the raw PNG before quantise.
BANNER = "#12128c"


def color(value, source):
    return {"$type": "color", "$value": value, "$extensions": {"source": source}}


def dim(value, source):
    return {"$type": "dimension", "$value": value, "$extensions": {"source": source}}


def weight(value, source):
    return {"$type": "fontWeight", "$value": value, "$extensions": {"source": source}}


def family(value, source):
    return {"$type": "fontFamily", "$value": value, "$extensions": {"source": source}}


def typography(value, source):
    return {"$type": "typography", "$value": value, "$extensions": {"source": source}}


def font_stack():
    raw = D["h1"]["fontFamily"]
    parts = [p.strip().strip('"') for p in raw.split(",")]
    # The live stack repeats system-ui. Keep the first occurrence of each name.
    seen = []
    for part in parts:
        if part and part not in seen:
            seen.append(part)
    return seen


UI = "getComputedStyle on the public homepage, 2026-11-21, signed out"

tokens = {
    "$schema": "https://schemas.design/tokens.json",
    "core": {
        "font": {
            "family": {
                "ui": family(
                    font_stack(),
                    f"{UI}, h1 fontFamily",
                )
            }
        },
        "typography": {
            "display": typography(
                {
                    "fontFamily": "{font.family.ui}",
                    "fontSize": D["h1"]["fontSize"],
                    "fontWeight": D["h1"]["fontWeight"],
                    "lineHeight": D["h1"]["lineHeight"],
                    "letterSpacing": D["h1"]["letterSpacing"],
                },
                f"{UI}, h1 'Get the truth when you travel'",
            ),
            "heading": typography(
                {
                    "fontFamily": "{font.family.ui}",
                    "fontSize": HOME["h2"]["fontSize"],
                    "fontWeight": HOME["h2"]["fontWeight"],
                    "lineHeight": HOME["h2"]["lineHeight"],
                    "letterSpacing": HOME["h2"]["letterSpacing"],
                },
                f"{UI}, first h2",
            ),
            "nav": typography(
                {
                    "fontFamily": "{font.family.ui}",
                    "fontSize": D["navPricingP"]["fontSize"],
                    "fontWeight": D["navPricingP"]["fontWeight"],
                    "lineHeight": D["navPricingP"]["lineHeight"],
                    "letterSpacing": D["navPricingP"]["letterSpacing"],
                },
                f"{UI}, Pricing paragraph inside the nav link",
            ),
            "body": typography(
                {
                    "fontFamily": "{font.family.ui}",
                    "fontSize": D["lede"]["fontSize"],
                    "fontWeight": D["lede"]["fontWeight"],
                    "lineHeight": D["lede"]["lineHeight"],
                    "letterSpacing": "0px",
                },
                f"{UI}, homepage lede paragraph",
            ),
            "button": typography(
                {
                    "fontFamily": "{font.family.ui}",
                    "fontSize": D["whiteBtnP"]["fontSize"],
                    "fontWeight": D["whiteBtnP"]["fontWeight"],
                    "lineHeight": D["whiteBtnP"]["lineHeight"],
                    "letterSpacing": "0px",
                },
                f"{UI}, 'Give Flighty a try' label",
            ),
        },
        "radius": {
            "pill": dim(D["getAppA"]["borderRadius"], f"{UI}, Get the app borderRadius"),
            "button": dim(D["whiteBtn"]["borderRadius"], f"{UI}, Give Flighty a try borderRadius"),
            "pro": dim(P["tryBtn"]["borderRadius"], "getComputedStyle on /pricing Try it for free, borderRadius"),
        },
        "space": {
            "nav-x": dim("12px", f"{UI}, Get the app padding-left"),
            "button-y": dim("12px", f"{UI}, Give Flighty a try padding-top"),
            "button-x": dim("20px", f"{UI}, Give Flighty a try padding-left"),
        },
        "size": {
            "banner": dim(f"{D['banner']['height']}px", f"{UI}, promo bar height"),
            "nav": dim(f"{HOME['nav']['height']}px", f"{UI}, Desktop Navbar height including the promo"),
            "get-app": dim(f"{D['getAppA']['height']}px", f"{UI}, Get the app height"),
            "button": dim(f"{D['whiteBtn']['height']}px", f"{UI}, Give Flighty a try height"),
            "pro-button": dim(f"{P['tryBtn']['height']}px", "getComputedStyle on /pricing Try it for free, height"),
        },
    },
    "light": {
        "page": color(HOME["body"]["backgroundColor"].replace("rgb(255, 255, 255)", "#ffffff"), f"{UI}, body backgroundColor"),
        "text": color("#000000", f"{UI}, h1 color rgb(0, 0, 0)"),
        "muted": color(D["lede"]["color"], f"{UI}, lede color"),
        "nav": color(D["navPricingP"]["color"], f"{UI}, Pricing paragraph color"),
        "banner": color(BANNER, "sampled from the raw homepage PNG promo strip before quantise, median pixel (18, 18, 140)"),
        "accent": color("#bf59f2", "getComputedStyle on /pricing Try it for free backgroundColor rgb(191, 89, 242); confirmed by sampling the raw pricing PNG"),
        "surface": color("#ffffff", f"{UI}, Give Flighty a try (White) backgroundColor"),
        "ink": color("#000000", f"{UI}, Give Flighty a try (Black) backgroundColor"),
        "on-ink": color("#ffffff", f"{UI}, Black button label color"),
        "border": color("rgba(0, 0, 0, 0.12)", "inline style on the White button, --border-color"),
    },
    "dark": {
        "page": color("#000000", "getComputedStyle on /pricing, body backgroundColor rgb(0, 0, 0). A page paint, not a theme switch."),
        "page-error": color("#161616", "getComputedStyle on /login (404), body backgroundColor rgb(22, 22, 22)"),
        "text": color("#ffffff", "getComputedStyle on /pricing h1 color"),
        "accent": color("#bf59f2", "same Try it for free fill, on the dark pricing page"),
        "button": color("rgba(255, 255, 255, 0.08)", "getComputedStyle on /login Go back home backgroundColor"),
    },
    "$themes": [
        {"id": "light", "name": "light", "selectedTokenSets": {"core": "enabled", "light": "enabled"}},
        {"id": "dark", "name": "dark", "selectedTokenSets": {"core": "enabled", "dark": "enabled"}},
    ],
}

# Fix page color to a real hex. The replace above is brittle if the reading changes.
tokens["light"]["page"] = color("#ffffff", f"{UI}, body backgroundColor {HOME['body']['backgroundColor']}")

out = HERE / "tokens.json"
out.write_text(json.dumps(tokens, indent=2) + "\n")
print(f"wrote {out}")
