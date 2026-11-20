#!/usr/bin/env python3
"""Build systems/orchids/tokens.json from the measured readings in raw/.

Values are copied from raw/css-vars.json and raw/components-computed.json.
Nothing here invents a colour the pages did not return.
"""

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "raw"


def src(label, detail):
    return {"$extensions": {"source": {"label": label, "detail": detail}}}


def color(value, detail):
    return {"$type": "color", "$value": value, **src("Measured", detail)}


def dim(value, detail):
    return {"$type": "dimension", "$value": value, **src("Measured", detail)}


def font(value, detail):
    return {"$type": "fontFamily", "$value": value, **src("Measured", detail)}


def num(value, detail, typ="number"):
    return {"$type": typ, "$value": value, **src("Measured", detail)}


def hexrgb(value):
    """rgb(0, 112, 243) as #0070f3, the form the rest of the library uses; a hex passes through."""
    m = re.fullmatch(r"rgb\((\d+),\s*(\d+),\s*(\d+)\)", value.strip())
    if m:
        return "#%02x%02x%02x" % tuple(int(x) for x in m.groups())
    if re.fullmatch(r"#[0-9a-fA-F]{6}", value):
        return value.lower()
    raise SystemExit(f"not an sRGB colour: {value!r}")


def build():
    """The token document, built in memory from raw/; main() writes it."""
    vars_ = json.loads((RAW / "css-vars.json").read_text())
    shared = vars_["lightAndDarkShared"]
    paused = vars_["pausedDeployment"]

    core = {
        "color": {
            "primary": color("#fcaa26", "docs :root --primary 252 170 38"),
            "gray": {
                "50": color("#faf8f4", "--gray-50 250 248 244"),
                "100": color("#f5f3ef", "--gray-100 245 243 239"),
                "200": color("#e6e3df", "--gray-200 230 227 223"),
                "300": color("#d5d3cf", "--gray-300 213 211 207"),
                "400": color("#a6a39f", "--gray-400 166 163 159"),
                "500": color("#777571", "--gray-500 119 117 113"),
                "600": color("#575551", "--gray-600 87 85 81"),
                "700": color("#46433f", "--gray-700 70 67 63"),
                "800": color("#2d2a26", "--gray-800 45 42 38"),
                "900": color("#1e1b17", "--gray-900 30 27 23"),
                "950": color("#110f0b", "--gray-950 17 15 11"),
            },
            "backgroundLight": color("#ffffff", "--background-light 255 255 255"),
            "backgroundDark": color("#0e0c0c", "--background-dark 14 12 12"),
            "green600": color(shared["--color-green-600"], "Tailwind --color-green-600, declared, not seen as a control"),
            "blue600": color(shared["--color-blue-600"], "Tailwind --color-blue-600, declared, not seen as a control"),
            "paused": {
                "link": color(hexrgb(paused["link"]["color"]), "Vercel paused page link, www.orchids.app, computed rgb(0, 112, 243)"),
                "guilty": color("#ed367f", "Vercel paused page .error-title-guilty border"),
                "innocent": color("#59b89c", "Vercel paused page .error-title-innocent border"),
                "selection": color(paused["selection"], "Vercel paused page ::selection"),
                "devinfoBorder": color("#dddddd", "Vercel paused page .devinfo-container border"),
            },
        },
        "font": {
            "family": {
                "sans": font(
                    "Inter, ui-sans-serif, system-ui, sans-serif",
                    "computed --default-font-family on docs, first families kept",
                ),
                "mono": font(
                    "Paper Mono, ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace",
                    "computed --font-paper-mono",
                ),
                "paused": font(
                    "sf pro text, sf pro icons, helvetica neue, helvetica, arial, sans-serif",
                    "Vercel paused page body, not the product",
                ),
            }
        },
        "typography": {
            "display": {
                "$type": "typography",
                "$value": {
                    "fontFamily": "{core.font.family.sans}",
                    "fontSize": "36px",
                    "fontWeight": 600,
                    "lineHeight": "40px",
                    "letterSpacing": "-0.9px",
                },
                **src("Measured", "docs h1 Introduction"),
            },
            "heading": {
                "$type": "typography",
                "$value": {
                    "fontFamily": "{core.font.family.sans}",
                    "fontSize": "24px",
                    "fontWeight": 600,
                    "lineHeight": "32px",
                },
                **src("Measured", "pricing h2 Available Plans"),
            },
            "body": {
                "$type": "typography",
                "$value": {
                    "fontFamily": "{core.font.family.sans}",
                    "fontSize": "18px",
                    "fontWeight": 400,
                    "lineHeight": "28px",
                },
                **src("Measured", "docs lead paragraph"),
            },
            "label": {
                "$type": "typography",
                "$value": {
                    "fontFamily": "{core.font.family.sans}",
                    "fontSize": "14px",
                    "fontWeight": 500,
                    "lineHeight": "20px",
                },
                **src("Measured", "Start a Project and sidebar links"),
            },
            "code": {
                "$type": "typography",
                "$value": {
                    "fontFamily": "{core.font.family.mono}",
                    "fontSize": "14px",
                    "fontWeight": 400,
                    "lineHeight": "24px",
                },
                **src("Measured", "pricing page code sample, Paper Mono 14px"),
            },
        },
        "space": {
            "1": dim("4px", "--spacing .25rem"),
            "2": dim("8px", "search gap 8px"),
            "3": dim("12px", "copy button horizontal padding 12px"),
            "4": dim("16px", "sidebar link padding-left 16px"),
            "5": dim("20px", "card padding-top 20px"),
            "6": dim("24px", "plan card padding 24px"),
        },
        "radius": {
            "sm": dim("4px", "Vercel paused .devinfo-container"),
            "md": dim("8px", "search button and plan card"),
            "lg": dim("12px", "copy button left radius"),
            "xl": dim("16px", "feature card 16px"),
            "dialog": dim("20px", "search dialog"),
            "full": dim("9999px", "theme switch and send button"),
        },
        "motion": {
            "duration": {
                "fast": num("150ms", "--default-transition-duration .15s", "duration"),
                "overlay": num("250ms", "search overlay transition 0.25s", "duration"),
            },
            "easing": {
                "standard": {
                    "$type": "cubicBezier",
                    "$value": [0.4, 0, 0.2, 1],
                    **src("Measured", "--ease-in-out cubic-bezier(.4, 0, .2, 1)"),
                },
                "overlay": {
                    "$type": "cubicBezier",
                    "$value": [0.22, 1, 0.36, 1],
                    **src("Measured", "search overlay computed transition-timing-function"),
                },
            },
        },
    }

    light = {
        "page": color("#ffffff", "html background in html.light"),
        "surface": color("#ffffff", "search and copy button background in light"),
        "raised": color("#faf8f4", "--gray-50, header is near this; header pixel sampled #f8f7f7"),
        "text": color("#1e1b17", "h1 color in light, --gray-900"),
        "textBody": color("#46433f", "lead paragraph in light, --gray-700"),
        "muted": color("#777571", "search placeholder in light, --gray-500"),
        "accent": color("{core.color.primary}", "Start a Project span and current nav"),
        "border": color("#f5f3ef", "--default-border-color in light, --gray-100"),
        "borderStrong": color("#e6e3df", "copy button border in light, --gray-200"),
        "focus": color("{core.color.primary}", ":focus-visible outline-color rgb(var(--primary))"),
        "link": color("{core.color.primary}", "current sidebar link"),
    }
    dark = {
        "page": color("#0e0c0c", "html background in html.dark, --background-dark"),
        "surface": color("#0e0c0c", "search and copy button background in dark"),
        "raised": color("#1e1b17", "selected theme switch background, --gray-900"),
        "text": color("#e6e3df", "h1 color in dark, --gray-200"),
        "textBody": color("#a6a39f", "lead paragraph in dark, --gray-400"),
        "muted": color("#777571", "unselected theme icon, --gray-500"),
        "accent": color("{core.color.primary}", "Start a Project and current nav, same amber"),
        "border": color("#2d2a26", "--default-border-color in dark, --gray-800"),
        "focus": color("{core.color.primary}", ":focus-visible outline-color"),
        "link": color("{core.color.primary}", "current sidebar link"),
    }

    tokens = {
        "core": core,
        "light": light,
        "dark": dark,
        "$themes": [
            {"id": "light", "name": "light", "selectedTokenSets": {"core": "source", "light": "enabled"}},
            {"id": "dark", "name": "dark", "selectedTokenSets": {"core": "source", "dark": "enabled"}},
        ],
    }
    return tokens


def main():
    (ROOT / "tokens.json").write_text(json.dumps(build(), indent=2) + "\n")
    print("wrote", ROOT / "tokens.json")


if __name__ == "__main__":
    main()
