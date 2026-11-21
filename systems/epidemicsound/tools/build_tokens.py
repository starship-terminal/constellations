#!/usr/bin/env python3
"""Build tokens.json from the Epidemic Sound public capture readings.

Sources, read on 2026-11-21 from www.epidemicsound.com, signed out:
  raw/css-vars.json              declared --es-* and brand custom properties
  raw/components-computed.json   computed styles of visible public controls

The public marketing site paints one light theme. The --es-color-* set on
:root is the product dark palette. It is recorded under `product` and is not
treated as a theme the public site showed.

Deterministic. Edit the raw files, never tokens.json.
"""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = json.loads((HERE / "raw" / "css-vars.json").read_text())
COMP = json.loads((HERE / "raw" / "components-computed.json").read_text())
R = RAW["resolved"]


def color(value, source):
    return {"$type": "color", "$value": value, "$extensions": {"source": source}}


def dim(value, source):
    return {"$type": "dimension", "$value": value, "$extensions": {"source": source}}


def font(value, source):
    return {"$type": "fontFamily", "$value": value, "$extensions": {"source": source}}


def weight(value, source):
    return {"$type": "fontWeight", "$value": value, "$extensions": {"source": source}}


def dur(value, source):
    return {"$type": "duration", "$value": value, "$extensions": {"source": source}}


def bez(value, source):
    return {"$type": "cubicBezier", "$value": value, "$extensions": {"source": source}}


def num(value, source):
    return {"$type": "number", "$value": value, "$extensions": {"source": source}}


def alias(path):
    return "{" + path + "}"


def measured(name):
    return COMP[name]


doc = {
    "$schema": "https://design-tokens.org/schema.json",
    "core": {
        "color": {
            "off-white": color(R["--es-color-brand-off-white"]["value"], "css-var --es-color-brand-off-white; painted page background"),
            "black": color(R["--color-brand-black"]["value"], "css-var --color-brand-black; painted text and primary fill"),
            "white": color(R["--color-brand-white"]["value"], "css-var --color-brand-white; text on primary buttons"),
            "ink-soft": color("#272727", "measured header Create free account hover background, home 1440"),
            "secondary-fill": color("rgba(61, 77, 116, 0.12)", "measured Contact sales and Log in button background"),
            "ghost-hover": color("rgba(61, 77, 116, 0.08)", "measured Music nav button hover background"),
            "muted": color("rgba(0, 0, 0, 0.6)", "measured footer link color"),
            "yellow": color(R["--es-color-brand-yellow"]["value"], "css-var --es-color-brand-yellow; declared brand, not a painted marketing fill on the captured pages"),
            "focus": color(R["--es-color-misc-focused"]["value"], "css-var --es-color-misc-focused; declared. Public buttons painted a white 2px outline on focus, not this blue"),
            "product-base": color(R["--es-color-background-base"]["value"], "css-var --es-color-background-base; product dark palette, not the painted marketing page"),
            "product-accent": color(R["--es-color-action-accent"]["value"], "css-var --es-color-action-accent; product dark palette"),
        },
        "font": {
            "display": font("Sebenta, Georgia, \"Times New Roman\", \"Noto Serif\", serif", "css-var --es-i-header-font-family; computed on h1"),
            "sans": font("Inter, Arial, \"Helvetica Neue\", sans-serif", "css-var --es-i-text-font-family; computed on body and buttons"),
        },
        "typography": {
            "display": {
                "$type": "typography",
                "$value": {
                    "fontFamily": alias("core.font.display"),
                    "fontSize": "80px",
                    "fontWeight": 500,
                    "lineHeight": "80px",
                },
                "$extensions": {"source": "measured h1 on / at 1440; family Sebenta weight 500"},
            },
            "heading": {
                "$type": "typography",
                "$value": {
                    "fontFamily": alias("core.font.display"),
                    "fontSize": "64px",
                    "fontWeight": 500,
                    "lineHeight": "64px",
                },
                "$extensions": {"source": "css-var --es-heading-xl-font-size 4rem on body; weight from the display face"},
            },
            "body": {
                "$type": "typography",
                "$value": {
                    "fontFamily": alias("core.font.sans"),
                    "fontSize": "16px",
                    "fontWeight": 400,
                    "lineHeight": "16px",
                },
                "$extensions": {"source": "measured body on / at 1440"},
            },
            "button-s": {
                "$type": "typography",
                "$value": {
                    "fontFamily": alias("core.font.sans"),
                    "fontSize": "14px",
                    "fontWeight": 600,
                    "lineHeight": "24px",
                },
                "$extensions": {"source": "measured header Create free account, class es-text-button-s"},
            },
            "button-m": {
                "$type": "typography",
                "$value": {
                    "fontFamily": alias("core.font.sans"),
                    "fontSize": "16px",
                    "fontWeight": 600,
                    "lineHeight": "24px",
                },
                "$extensions": {"source": "measured Contact sales, class es-text-button-m"},
            },
            "nav": {
                "$type": "typography",
                "$value": {
                    "fontFamily": alias("core.font.sans"),
                    "fontSize": "14px",
                    "fontWeight": 600,
                    "lineHeight": "24px",
                },
                "$extensions": {"source": "measured header Music button"},
            },
        },
        "radius": {
            "none": dim("0px", "css-var --es-radius-button on body is 0; marketing controls override to a pill"),
            "medium": dim(R["--es-radius-medium"]["value"], "css-var --es-radius-medium"),
            "large": dim("8px", "css-var --es-radius-large on :root"),
            "pill": dim("10000px", "measured border-radius on primary, secondary and nav buttons; .radii-override sets --es-radius-button to 10000px"),
        },
        "size": {
            "button-s": dim(measured("button-primary-default")["height"], "measured header Create free account height"),
            "button-m": dim(measured("button-secondary-hero")["height"], "measured Contact sales height"),
            "nav": dim(measured("nav-button")["height"], "measured Music nav button height"),
            "header": dim("100px", "measured header height at 1440"),
            "switch": dim("40px", "measured pricing billing switch width; height 24px"),
        },
        "space": {
            "button-s-x": dim("16px", "measured primary button padding-left"),
            "button-s-y": dim("4px", "measured primary button padding-top"),
            "button-m-x": dim("24px", "measured Contact sales padding-left"),
            "nav-x": dim("16px", "measured Music button padding-left"),
        },
        "motion": {
            "duration": dur("150ms", "measured button class duration-150; declared --animation-duration is 600ms and was not the control transition"),
            "easing": bez([0, 0, 0.2, 1], "css-var --ease-out"),
        },
        "focus": {
            "outline-width": dim("2px", "measured focus outline on header Create free account"),
            "outline-color": color("#ffffff", "measured focus outline color on the black primary button"),
        },
    },
    "light": {
        "background": {
            "page": color(alias("core.color.off-white"), "painted body background rgb(241, 240, 235)"),
            "surface": color("#ffffff", "measured nav panel and pricing card fill"),
            "header": color("rgba(0, 0, 0, 0)", "measured header background; the bar reads as a white pill over the page"),
        },
        "text": {
            "primary": color(alias("core.color.black"), "measured body and h1 color"),
            "muted": color(alias("core.color.muted"), "measured footer link color"),
            "on-accent": color(alias("core.color.white"), "measured primary button text"),
        },
        "border": {
            "default": color(alias("core.color.black"), "computed border color on text; most controls use fill, not a stroke"),
        },
        "action": {
            "primary": color(alias("core.color.black"), "measured Create free account background"),
            "primary-hover": color(alias("core.color.ink-soft"), "measured Create free account hover background"),
            "secondary": color(alias("core.color.secondary-fill"), "measured Contact sales background"),
            "ghost-hover": color(alias("core.color.ghost-hover"), "measured Music button hover background"),
        },
        "accent": color(alias("core.color.black"), "the public site uses black as the only strong fill; brand yellow is declared and not used as a marketing accent on the captured pages"),
    },
    "$themes": [
        {"id": "light", "name": "light", "selectedTokenSets": {"core": "source", "light": "enabled"}},
    ],
}

out = HERE / "tokens.json"
out.write_text(json.dumps(doc, indent=2) + "\n")
print("wrote", out, "tokens")
