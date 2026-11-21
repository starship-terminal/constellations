#!/usr/bin/env python3
"""Write tokens.json from raw/measured.json. Does not sample screenshots."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
measured = json.loads((ROOT / "raw" / "measured.json").read_text())

def color(value, source):
    return {"$value": value, "$type": "color", "$extensions": {"source": source}}

def dim(value, source):
    return {"$value": value, "$type": "dimension", "$extensions": {"source": source}}

def font(value, source):
    return {"$value": value, "$type": "fontFamily", "$extensions": {"source": source}}

h1 = measured["h1"]
body = measured["body"]
menu = measured["menu"]
btn = measured["errorPage"]["links"][0]
card = measured["cards"][0]
tokens = {
    "$schema": "https://design-tokens.org/schema.json",
    "core": {
        "font": {
            "family": {
                "display": font(h1["fontFamily"], "computed font-family on the homepage h1"),
                "body": font(body["fontFamily"], "computed font-family on body"),
                "ui": font(menu["fontFamily"], "computed font-family on the Menu link"),
            }
        },
        "typography": {
            "display": {
                "$value": {
                    "fontFamily": "{core.font.family.display}",
                    "fontSize": h1["fontSize"],
                    "fontWeight": h1["fontWeight"],
                    "lineHeight": h1["lineHeight"],
                    "letterSpacing": h1["letterSpacing"],
                },
                "$type": "typography",
                "$extensions": {"source": "computed style on the homepage h1 at 1440"},
            },
            "body": {
                "$value": {
                    "fontFamily": "{core.font.family.body}",
                    "fontSize": body["fontSize"],
                    "lineHeight": body["lineHeight"],
                },
                "$type": "typography",
                "$extensions": {"source": "computed style on body"},
            },
            "nav": {
                "$value": {
                    "fontFamily": "{core.font.family.ui}",
                    "fontSize": menu["fontSize"],
                    "fontWeight": menu["fontWeight"],
                    "lineHeight": menu["lineHeight"],
                },
                "$type": "typography",
                "$extensions": {"source": "computed style on the Menu link"},
            },
        },
        "radius": {
            "button": dim(btn["borderRadius"], "computed border-radius on the error-page Drafts Home button"),
            "card": dim(card["borderRadius"], "computed border-radius on a homepage feature card"),
        },
        "space": {
            "button-x": dim("16px", "computed horizontal padding on the error-page button"),
            "button-y": dim("9px", "computed vertical padding on the error-page button"),
        },
    },
    "light": {
        "color": {
            "page": color(body["backgroundColor"], "computed background on body"),
            "ink": color(h1["color"], "computed color on the homepage h1"),
            "muted": color(measured["errorPage"]["lede"]["color"], "computed color on the error-page lede"),
            "tagline": color(measured["tagline"]["color"], "computed color on the homepage tagline span"),
            "nav": color(menu["color"], "computed color on the Menu link over the cover"),
            "cover": color(measured["sampledPngBeforeQuantize"]["cover"], "sampled cover photograph before quantize; the cover is a gradient, not a flat fill"),
            "footer": color(measured["footer"]["backgroundColor"], "computed background on footer"),
            "cta": color(btn["backgroundColor"], "computed background on the error-page button"),
            "on-cta": color(btn["color"], "computed color on the error-page button"),
            "primary-declared": color(measured["declared"]["--bs-primary"], "declared --bs-primary"),
        }
    },
    "$themes": [
        {"id": "light", "name": "Light", "selectedTokenSets": {"core": "enabled", "light": "enabled"}}
    ],
}
(ROOT / "tokens.json").write_text(json.dumps(tokens, indent=2) + "\n")
print("wrote tokens.json")
