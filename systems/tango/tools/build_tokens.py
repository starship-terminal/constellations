#!/usr/bin/env python3
"""Write tokens.json from the Tango readings in raw/foundations.json.

Values are the colours, type, radii and spacing measured on 2026-11-19.
Nothing here invents a token the page did not show.
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "raw" / "foundations.json"
OUT = ROOT / "tokens.json"

SOURCE = (
    "getComputedStyle on tango.ai and app.tango.us, 2026-11-19, "
    "T3 preview tab, viewport 1169x731 at devicePixelRatio 2"
)


def color(value: str, source: str) -> dict:
    return {"$type": "color", "$value": value, "$extensions": {"source": f"{SOURCE} {source}"}}


def dim(value: str, source: str) -> dict:
    return {"$type": "dimension", "$value": value, "$extensions": {"source": f"{SOURCE} {source}"}}


def font(value: str, source: str) -> dict:
    return {"$type": "fontFamily", "$value": value, "$extensions": {"source": f"{SOURCE} {source}"}}


def text(value: dict, source: str) -> dict:
    return {"$type": "typography", "$value": value, "$extensions": {"source": f"{SOURCE} {source}"}}


def shadow(value: str, source: str) -> dict:
    return {"$type": "shadow", "$value": value, "$extensions": {"source": f"{SOURCE} {source}"}}


def hand(token: dict) -> dict:
    """Relabel a declared value that no raw/ file holds: Reconstruction, entered by hand."""
    note = token["$extensions"]["source"][len(SOURCE) + 1:]
    token["$extensions"]["source"] = (
        f"Reconstruction: entered by hand at capture time from {note} (T3 preview tab, 2026-11-19); "
        "no raw/ file holds this reading"
    )
    return token


def duration(value: str, source: str) -> dict:
    return {"$type": "duration", "$value": value, "$extensions": {"source": f"{SOURCE} {source}"}}


def other(value: str, source: str) -> dict:
    return {"$type": "other", "$value": value, "$extensions": {"source": f"{SOURCE} {source}"}}


def build() -> dict:
    raw = json.loads(RAW.read_text())
    assert raw["viewport"]["innerWidth"] == 1169
    return {
        "$schema": "https://design-tokens.org/schema.json",
        "core": {
            "color": {
                "purple": {
                    "400": color("#6f26d0", "--color--purple--400 and --topaz-colors-purple500"),
                    "600": color("#5d1b98", "--topaz-colors-purple600"),
                    "700": hand(color("#40125e", "--topaz-colors-purple700")),
                    "100": hand(color("#f4ecf9", "--topaz-colors-purple100")),
                    "300": color("#dec4f3", "--topaz-colors-purple300"),
                },
                "orange": {
                    "400": color("#ff8c49", "--color--orange--400, enterprise Talk to sales face"),
                    "500": color("#f9650f", "--color--orange--400 token and Annual pricing face"),
                },
                "pink": color("#ffa3c6", "--color--brand--pink"),
                "yellow": color("#fdd543", "--color--brand--yellow"),
                "warmWhite": color("#fafafa", "--color--brand--warm-white and body background"),
                "ink": color("#383838", "body color and --color--neutral--500"),
                "black": hand(color("#0d0d0d", "--color--grey--950 and --_color---fill--primary")),
                "border": hand(color("#cccccc", "--_color---border--default")),
                "error": hand(color("#ff2323", "--_color---border--error")),
                "cardBorder": color("#989595", "pricing card border rgb(152, 149, 149)"),
            },
            "font": {
                "family": {
                    "display": font("Gelica, Arial, sans-serif", "marketing h1 and app h2"),
                    "body": font("\"Apercu Pro\", Arial, sans-serif", "marketing body"),
                    "app": font("Apercu, ui-sans-serif, system-ui, sans-serif", "app.tango.us body"),
                    "secondary": hand(font("\"Inter Variable\", Arial, sans-serif", "--_typography---font-family--secondary")),
                    "tertiary": hand(font("Lato, Arial, sans-serif", "--_typography---font-family--tertiary")),
                }
            },
            "typography": {
                "display": text(
                    {"fontFamily": "Gelica, Arial, sans-serif", "fontSize": "63.4314px", "fontWeight": 400, "lineHeight": "69.7746px"},
                    "home h1 at 1169px",
                ),
                "heading": text(
                    {"fontFamily": "Gelica, serif", "fontSize": "32px", "fontWeight": 400, "lineHeight": "41.6px", "letterSpacing": "-0.1px"},
                    "app sign-in h2",
                ),
                "body": text(
                    {"fontFamily": "\"Apercu Pro\", Arial, sans-serif", "fontSize": "16px", "fontWeight": 400, "lineHeight": "22.4px"},
                    "marketing body and nav links",
                ),
                "lede": text(
                    {"fontFamily": "\"Apercu Pro\", Arial, sans-serif", "fontSize": "21.2129px", "fontWeight": 400, "lineHeight": "27.5767px"},
                    "home hero paragraph",
                ),
                "ui": text(
                    {"fontFamily": "Apercu, sans-serif", "fontSize": "13px", "fontWeight": 500, "letterSpacing": "0.1px"},
                    "app buttons and fields",
                ),
                "label": text(
                    {"fontFamily": "Apercu, sans-serif", "fontSize": "12px", "fontWeight": 500, "letterSpacing": "0.1px"},
                    "app field labels",
                ),
            },
            "radius": {
                "button": dim("731px", "marketing pill, computed from 100vh at this viewport"),
                "card": dim("16px", "pricing card"),
                "navCard": dim("24px", "navbar dropdown card and app demo card"),
                "appPanel": dim("32px", "sign-in panel, --topaz-radii-xl"),
                "appControl": dim("10px", "app field and button, --topaz-radii-sm"),
                "appXs": dim("6px", "--topaz-radii-xs, password eye"),
                "full": dim("9999px", "help button and --topaz-radii-full"),
            },
            "spacing": {
                "2": dim("8px", "--topaz-space-2 and pricing toggle padding"),
                "3": dim("12px", "--topaz-space-3 and field horizontal padding"),
                "4": dim("16px", "--topaz-space-4 and app button padding"),
                "5": dim("24px", "pricing card padding"),
                "nav": dim("4rem", "--navbar--height"),
            },
            "motion": {
                "button": other("all 0.35s ease", "marketing .button computed transition"),
                "appButton": other("background, color, border, border-color, opacity, box-shadow 0.2s ease-in-out", "app button computed transition"),
                "navDropdown": hand(duration("400ms", "--navbar--dropdown-duration .4s")),
            },
            "$extensions": {"notTokenised": [
                "--_sizes---radius--button is declared as 100vh, a viewport-height length DTCG cannot hold as one "
                "px value; the marketing pill computed it as 731px at the 731px-tall viewport (core.radius.button). "
                "Entered by hand at capture time; no raw/ file holds the declaration.",
            ]},
        },
        "light": {
            "surface": {
                "page": color("#fafafa", "marketing body background and --_color---background--primary"),
                "raised": color("#ffffff", "app field and --topaz-colors-surface"),
                "panel": color("#faf9fa", "sign-in panel rgb(250, 249, 250) and --topaz-colors-gray70"),
            },
            "text": {
                "primary": color("#383838", "marketing body color"),
                "secondary": color("#524d59", "app lede and labels, --topaz-colors-textBody"),
                "muted": color("#75717b", "or-divider span rgb(117, 113, 123)"),
                "onAccent": color("#ffffff", "primary button text"),
                "placeholder": color("#c2c0c6", "app field placeholder"),
                "ink": color("#251f2d", "app heading, --topaz-colors-textPrimary"),
            },
            "accent": color("#6f26d0", "primary button and --topaz-colors-accent"),
            "accentHover": color("#5d1b98", "--topaz-colors-accentHover, not shown as a live hover"),
            "highlight": color("#f9650f", "Annual pricing selected face and logo colour rgb(249, 101, 15)"),
            "border": {
                "default": hand(color("#cccccc", "--_color---border--default")),
                "card": color("#989595", "Free and Enterprise pricing card border"),
                "field": color("#96949a", "app field border rgb(150, 148, 154)"),
                "focus": color("#dec4f3", "focused field outline rgb(222, 196, 243)"),
            },
            "status": {
                "error": hand(color("#ff2323", "--_color---border--error, declared, not shown on a live field")),
                "disabled": color("#9b98a0", "disabled Continue text"),
                "disabledSurface": color("#e8e6ea", "disabled Continue background"),
            },
            "component": {
                "button": {
                    "bg": color("#6f26d0", "Get started for free"),
                    "text": color("#ffffff", "Get started for free"),
                    "radius": dim("731px", "marketing pill at this viewport"),
                    "padding": dim("16px", "hero primary vertical padding"),
                    "height": dim("60px", "hero primary height 60.2px, rounded"),
                },
                "field": {
                    "bg": color("#ffffff", "app email field wrap"),
                    "text": color("#251f2d", "app input color"),
                    "radius": dim("10px", "app field wrap"),
                    "height": dim("36px", "app field wrap"),
                },
            },
            "shadow": {
                "toggle": shadow("0px 1px 8px 0px rgba(0, 0, 0, 0.06)", "pricing toggle wrap"),
                "button": shadow("0px 1px 2px 0px rgba(0, 0, 0, 0.05)", "app Google button"),
            },
        },
        "$themes": [
            {"name": "light", "selectedTokenSets": {"core": "enabled", "light": "enabled"}}
        ],
    }


def main() -> None:
    OUT.write_text(json.dumps(build(), indent=2) + "\n")
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()
