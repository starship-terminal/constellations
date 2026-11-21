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

body = measured["body"]
h2 = measured["h2"]
nav = measured["nav"]
sub = measured["subscribe"]
tokens = {
    "$schema": "https://design-tokens.org/schema.json",
    "core": {
        "font": {"family": {"ui": font(body["fontFamily"], "computed font-family on body")}},
        "typography": {
            "heading": {
                "$value": {"fontFamily": "{core.font.family.ui}", "fontSize": h2["fontSize"], "fontWeight": h2["fontWeight"], "lineHeight": h2["lineHeight"]},
                "$type": "typography",
                "$extensions": {"source": "computed style on the homepage h2 at 1440"},
            },
            "body": {
                "$value": {"fontFamily": "{core.font.family.ui}", "fontSize": body["fontSize"], "fontWeight": body["fontWeight"], "lineHeight": body["lineHeight"]},
                "$type": "typography",
                "$extensions": {"source": "computed style on body"},
            },
            "nav": {
                "$value": {"fontFamily": "{core.font.family.ui}", "fontSize": nav["fontSize"], "fontWeight": nav["fontWeight"], "lineHeight": nav["lineHeight"]},
                "$type": "typography",
                "$extensions": {"source": "computed style on a header nav link"},
            },
        },
        "radius": {
            "button": dim(sub["borderRadius"], "computed border-radius on Subscribe"),
            "card": dim(measured["productCard"]["borderRadius"], "computed border-radius on a product card"),
            "field": dim(measured["email"]["borderRadius"], "computed border-radius on the newsletter email field"),
            "nav": dim(nav["borderRadius"], "computed border-radius on a header nav link"),
        },
    },
    "light": {
        "color": {
            "page": color(body["backgroundColor"], "computed background-color on body"),
            "page-features": color(measured["slices"]["features"], "computed background on the features slice"),
            "page-get": color(measured["slices"]["get"], "computed background on the get slice"),
            "ink": color(body["color"], "computed color on body"),
            "heading": color(h2["color"], "computed color on the homepage h2"),
            "muted": color(measured["heroLede"]["color"], "computed color on the hero lede"),
            "nav": color(nav["color"], "computed color on a header nav link"),
            "link": color(measured["seeFeatures"]["color"], "computed color on See features"),
            "button": color(sub["backgroundColor"], "computed background on Subscribe"),
            "on-button": color(sub["color"], "computed color on Subscribe"),
            "field": color(measured["email"]["backgroundColor"], "computed background on the newsletter email field"),
            "field-border": color("rgb(223, 227, 232)", "computed border-color on the newsletter email field"),
            "footer": color(measured["footerLink"]["color"], "computed color on a footer link"),
            "card": color(measured["productCard"]["backgroundColor"], "computed background on a product card"),
            "focus": color("rgb(229, 151, 0)", "computed outline-color on a focused header nav link"),
        }
    },
}
(ROOT / "tokens.json").write_text(json.dumps(tokens, indent=2) + "\n")
print("wrote", ROOT / "tokens.json")
