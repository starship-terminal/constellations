#!/usr/bin/env python3
"""Build tokens.json from the public cursor.com readings.

PRODUCT (adapt): Cursor marketing site, captured signed out on 2026-11-22.
Inputs are raw/css-vars.json (declared custom properties on the homepage)
and raw/home-computed.json (computed styles). Values that are color-mix,
lab(), or aliases are kept only when a resolved hex was declared or computed.
The kit example is not used.
"""
import json
import pathlib

ADAPTED_FOR = "cursor"

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
VARS = json.loads((RAW / "css-vars.json").read_text())["vars"]
HOME = json.loads((RAW / "home-computed.json").read_text())


def color(value, source):
    return {"$value": value, "$type": "color", "$extensions": {"source": source}}


def dim(value, source):
    return {"$value": value, "$type": "dimension", "$extensions": {"source": source}}


def font(value, source):
    return {"$value": value, "$type": "fontFamily", "$extensions": {"source": source}}


def typography(value, source):
    return {"$value": value, "$type": "typography", "$extensions": {"source": source}}


def declared(name):
    return VARS[name]


tokens = {
    "$schema": "https://design-tokens.org/schema.json",
    "core": {
        "color": {
            "page": color(declared("--color-theme-bg"), "css-var --color-theme-bg declared #14120b"),
            "fg": color(declared("--color-theme-fg"), "css-var --color-theme-fg declared #edecec"),
            "fg02": color(declared("--color-theme-fg-02"), "css-var --color-theme-fg-02 declared #d7d6d5"),
            "accent": color(declared("--color-theme-accent"), "css-var --color-theme-accent declared #f54e00"),
            "card": color(declared("--color-theme-card-hex"), "css-var --color-theme-card-hex declared #1b1913"),
            "card01": color(declared("--color-theme-card-01-hex"), "css-var --color-theme-card-01-hex declared #1d1b15"),
            "card02": color(declared("--color-theme-card-02-hex"), "css-var --color-theme-card-02-hex declared #201e18"),
            "card03": color(declared("--color-theme-card-03-hex"), "css-var --color-theme-card-03-hex declared #26241e"),
            "card04": color(declared("--color-theme-card-04-hex"), "css-var --color-theme-card-04-hex declared #2b2923"),
            "cardHover": color(declared("--color-theme-card-hover-hex"), "css-var --color-theme-card-hover-hex declared #201e18"),
            "ansiGreen": color(declared("--color-theme-product-ansi-green"), "css-var --color-theme-product-ansi-green declared #1f8a65"),
            "ansiRed": color(declared("--color-theme-product-ansi-red"), "css-var --color-theme-product-ansi-red declared #cf2d56"),
            "ink": color("#000000", "css-var --color-black declared #000"),
            "paper": color("#ffffff", "css-var --color-white declared #fff"),
        },
        "font": {
            "family": {
                "ui": font(
                    'CursorGothic, "CursorGothic Fallback", system-ui, "Helvetica Neue", Helvetica, Arial, sans-serif',
                    "computed font-family on body and h1 at 1440. The site serves CursorGothic. It is not included.",
                ),
                "display": font(
                    declared("--font-cursor-display"),
                    "css-var --font-cursor-display",
                ),
            }
        },
        "radius": {
            "2xs": dim(declared("--radius-2xs"), "css-var --radius-2xs declared 2px"),
            "xs": dim(declared("--radius-xs"), "css-var --radius-xs declared 4px"),
            "sm": dim("4px", "derived from --radius-sm .25rem at 16px"),
            "md": dim(declared("--radius-md"), "css-var --radius-md declared 8px, also --border-radius"),
            "lg": dim("8px", "derived from --radius-lg .5rem at 16px"),
            "xl": dim("12px", "derived from --radius-xl .75rem at 16px"),
            "2xl": dim(declared("--radius-2xl"), "css-var --radius-2xl declared 1rem"),
            "3xl": dim(declared("--radius-3xl"), "css-var --radius-3xl declared 1.5rem"),
            "pill": dim("9999px", "computed border-radius on the nav Download link was a pill (3.35544e+07px). Stored as 9999px."),
        },
        "space": {
            "buttonX": dim("10.5px", "computed horizontal padding on the nav Download link"),
            "buttonY": dim("5.6px", "computed top padding on the nav Download link"),
        },
        "typography": {
            "body": typography(
                {"fontFamily": "{core.font.family.ui}", "fontSize": "16px", "fontWeight": "400", "lineHeight": "24px"},
                "computed body style at 1440. Matches --text-base 1rem and line-height 1.5.",
            ),
            "hero": typography(
                {"fontFamily": "{core.font.family.ui}", "fontSize": HOME["h1Style"]["size"], "fontWeight": HOME["h1Style"]["weight"], "lineHeight": HOME["h1Style"]["lh"]},
                "computed style on the homepage h1 at 1440. The painted hero is 26px, not the display scale.",
            ),
            "button": typography(
                {"fontFamily": "{core.font.family.ui}", "fontSize": "14px", "fontWeight": "400", "lineHeight": "20px"},
                "computed font-size and weight on the nav Download link. Line height was not isolated.",
            ),
        },
    },
    "dark": {
        "color": {
            "bg": {
                "page": color("{core.color.page}", "computed body background rgb(20, 18, 11), matching --color-theme-bg"),
                "card": color("{core.color.card}", "css-var --color-theme-card-hex #1b1913"),
                "elevated": color("{core.color.card02}", "css-var --color-theme-card-02-hex #201e18, also --color-theme-card-hover-hex"),
            },
            "text": {
                "primary": color("{core.color.fg}", "computed body color rgb(237, 236, 236), matching --color-theme-fg"),
                "secondary": color("{core.color.fg02}", "css-var --color-theme-fg-02 #d7d6d5. --color-theme-text-sec is a 60% mix and was not resolved."),
            },
            "action": {
                "fill": color("{core.color.fg}", "computed background of the nav Download link, rgb(237, 236, 236)"),
                "onFill": color("{core.color.page}", "computed color of the nav Download link, rgb(20, 18, 11)"),
                "accent": color("{core.color.accent}", "css-var --color-theme-accent #f54e00"),
            },
            "status": {
                "success": color("{core.color.ansiGreen}", "css-var --color-theme-product-ansi-green #1f8a65"),
                "danger": color("{core.color.ansiRed}", "css-var --color-theme-product-ansi-red #cf2d56"),
                "warning": color("{core.color.accent}", "css-var --color-warning aliases --color-theme-accent"),
            },
        },
        "component": {
            "buttonPrimary": {
                "radius": dim("{core.radius.pill}", "computed border-radius on the nav Download link, a pill"),
                "height": dim("27px", "computed height of the nav Download link, 27.4688px, rounded"),
                "padding": dim("5.6px 10.5px", "computed padding of the nav Download link"),
            }
        },
    },
    "$themes": [
        {"id": "dark", "name": "Dark", "selectedTokenSets": {"core": "source", "dark": "enabled"}}
    ],
}

out = HERE / "tokens.json"
out.write_text(json.dumps(tokens, indent=2) + "\n")
print(f"wrote {out}")
