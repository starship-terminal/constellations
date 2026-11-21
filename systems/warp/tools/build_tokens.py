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
cta = measured["requestEarlyAccess"]
demo = measured["bookADemo"]
nav = measured["nav"]["button"]
tokens = {
    "$schema": "https://design-tokens.org/schema.json",
    "core": {
        "font": {
            "family": {
                "display": font(h1["fontFamily"], "computed font-family on the homepage h1"),
                "body": font(measured["body"]["fontFamily"], "computed font-family on body"),
                "ui": font(nav["fontFamily"], "computed font-family on the Products nav button"),
            }
        },
        "typography": {
            "display": {
                "$value": {
                    "fontFamily": "{core.font.family.display}",
                    "fontSize": h1["fontSize"],
                    "fontWeight": h1["fontWeight"],
                    "lineHeight": h1["lineHeight"],
                },
                "$type": "typography",
                "$extensions": {"source": "computed style on the homepage h1 at 1440"},
            },
            "body": {
                "$value": {
                    "fontFamily": "{core.font.family.body}",
                    "fontSize": measured["body"]["fontSize"],
                    "lineHeight": measured["body"]["lineHeight"],
                },
                "$type": "typography",
                "$extensions": {"source": "computed style on body"},
            },
            "nav": {
                "$value": {
                    "fontFamily": "{core.font.family.ui}",
                    "fontSize": nav["fontSize"],
                    "fontWeight": nav["fontWeight"],
                    "lineHeight": nav["lineHeight"],
                },
                "$type": "typography",
                "$extensions": {"source": "computed style on the Products nav button"},
            },
        },
        "radius": {
            "button": dim(cta["borderRadius"], "computed border-radius on request early access"),
            "pill": dim(demo["borderRadius"], "computed border-radius on Book a demo"),
        },
        "space": {
            "button-x": dim("16px", "computed horizontal padding on request early access"),
            "button-y": dim("6px", "computed vertical padding on request early access"),
        },
    },
    "light": {
        "color": {
            "page": color("rgb(254, 253, 254)", "sampled homepage page fill before quantize; html background is oklch(0.992495 0.00178735 220)"),
            "ink": color(h1["color"], "computed color on the homepage h1"),
            "muted": color(measured["lede"]["color"], "computed color on the homepage lede"),
            "nav": color(measured["nav"]["backgroundColor"], "computed background on the primary nav"),
            "cta": color(cta["backgroundColor"], "computed background on request early access"),
            "on-cta": color(cta["color"], "computed color on request early access"),
            "demo": color(demo["backgroundColor"], "computed background on Book a demo"),
            "on-demo": color(demo["color"], "computed color on Book a demo"),
            "banner": color(measured["sampledPngBeforeQuantize"]["banner"], "sampled top announcement bar before quantize"),
            "accent-declared": color(measured["declared"]["--color-theme-accent"], "declared --color-theme-accent, not the painted demo pill"),
        }
    },
    "$themes": [
        {"id": "light", "name": "Light", "selectedTokenSets": {"core": "enabled", "light": "enabled"}}
    ],
}
(ROOT / "tokens.json").write_text(json.dumps(tokens, indent=2) + "\n")
print("wrote tokens.json")
