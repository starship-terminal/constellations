#!/usr/bin/env python3
"""Build tokens.json for the Leonardo.Ai public marketing capture.

Sources, read on 2026-11-21 from https://leonardo.ai/ in headless Chromium:
  raw/components-computed.json  computed styles of real controls
  raw/css-vars.json             custom properties on :root, when the harvest landed

The public site paints one theme: black page, violet display type, white and
violet pills. There is no light theme and no theme toggle on the marketing
pages. The export therefore has core plus dark. A light set is not invented.

Every token carries $extensions.source. Unread values stay out.
Deterministic: same inputs, same bytes.
"""
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
COMP = json.loads((RAW / "components-computed.json").read_text())


def src(text):
    return {"$extensions": {"source": text}}


def color(value, source):
    return {"$type": "color", "$value": value, **src(source)}


def dim(value, source):
    return {"$type": "dimension", "$value": value, **src(source)}


def font(value, source):
    return {"$type": "fontFamily", "$value": value, **src(source)}


def weight(value, source):
    return {"$type": "fontWeight", "$value": value, **src(source)}


def number(value, source):
    return {"$type": "number", "$value": value, **src(source)}


def state(name, which="default"):
    return COMP["components"][name]["states"][which]


def measured(name, which, prop):
    return f"measured {name}/{which} {prop} on https://leonardo.ai/ 2026-11-21"


# Pill radius is computed as a huge pixel length (border-radius: 9999px style).
# Record the authored intent as 9999px, labelled Derived from that computed value.
PILL = "9999px"

doc = {
    "core": {
        "color": {
            "page": color("#000000", "measured body background rgb(0, 0, 0) on https://leonardo.ai/ and sampled #000000 from home-dark-default.png before quantise"),
            "violet": color("#6e60ee", "sampled flat fill from home-dark-default.png display type and not-found 404, confirmed rgb(110, 96, 238) on pricing tab selected"),
            "white": color("#ffffff", "measured button-login/default backgroundColor rgb(255, 255, 255)"),
            "ink": color("#000000", "measured button-login/default color rgb(0, 0, 0)"),
            "muted": color("#ededed", "measured price/default color rgb(237, 237, 237)"),
            "menu": color("#111111", "sampled menu panel fill from home-dark-create-menu.png before quantise"),
            "green": color("#03e65b", "sampled Support and billing pill on contact-dark-default.png before quantise"),
            "yellow": color("#f8c030", "sampled ESSENTIAL plan label on pricing-dark-default.png before quantise"),
            "red": color("#f85848", "sampled ULTIMATE plan label on pricing-dark-default.png before quantise"),
            "tab-idle": color("rgba(255, 255, 255, 0.1)", "measured tab/default backgroundColor oklab white at 0.1 alpha, recorded as the equivalent sRGB alpha"),
            "text-secondary": color("rgba(255, 255, 255, 0.7)", "measured billing-toggle/default color oklab white at 0.7 alpha"),
        },
        "font": {
            "sans": font("canvaSans, sans-serif", measured("button-login", "default", "fontFamily") + "; computed family canvaSans. Proprietary Canva face, not redistributed"),
            "display": font("ufficioDisplay, sans-serif", "measured h1 fontFamily ufficioDisplay on https://leonardo.ai/ 2026-11-21, size 34.425px weight 500"),
            "poster": font("leoSans, sans-serif", "measured hero poster spans fontFamily leoSans, size 76px, weight 900, on https://leonardo.ai/ 2026-11-21"),
        },
        "fontWeight": {
            "medium": weight(500, "measured h1 fontWeight 500 and button-login fontWeight 500"),
            "black": weight(900, "measured hero poster span fontWeight 900"),
        },
        "fontSize": {
            "nav": dim("14px", measured("wordmark", "default", "fontSize") + " 14px"),
            "button": dim("16px", measured("button-login", "default", "fontSize") + " 16px"),
            "hero": dim("34.425px", "measured h1 fontSize 34.425px on https://leonardo.ai/"),
            "price": dim("40.5px", measured("price", "default", "fontSize") + " 40.5px"),
            "poster": dim("76px", "measured hero poster span fontSize 76px on https://leonardo.ai/"),
        },
        "radius": {
            "pill": dim(PILL, "Derived: computed borderRadius on button-login and pricing tabs is 3.35544e+07px, the browser's expansion of a full pill"),
            "none": dim("0px", measured("display", "default", "borderRadius") + " 0px"),
        },
        "size": {
            "login-height": dim("35px", measured("button-login", "default", "rect.h") + " 34.8px"),
            "hero-button-height": dim("48px", measured("button-subscribe", "default", "rect.h") + " 48.3px"),
            "tab-height": dim("61px", measured("tab", "selected", "rect.h") + " 60.7px"),
        },
    },
    "dark": {
        "page": color("{core.color.page}", "alias of measured page black"),
        "surface": color("{core.color.menu}", "alias of sampled menu surface"),
        "text": color("{core.color.white}", "alias of measured white text and login fill"),
        "muted": color("{core.color.muted}", "alias of measured price colour"),
        "accent": color("{core.color.violet}", "alias of measured violet"),
        "border": color("rgba(255, 255, 255, 0.16)", "Observed hairline on pricing cards and the Developer API pill; exact computed border was not isolated, so this is the visible white alpha. Labelled Observed, not a CSS variable."),
        "button": {
            "login": {
                "background": color("{core.color.white}", measured("button-login", "default", "backgroundColor")),
                "text": color("{core.color.ink}", measured("button-login", "default", "color")),
            },
            "subscribe": {
                "background": color("{core.color.violet}", measured("button-subscribe", "default", "backgroundColor") + " rgb(110, 96, 238)"),
                "text": color("{core.color.white}", measured("button-subscribe", "default", "color")),
            },
            "tutorial": {
                "text": color("{core.color.white}", measured("button-tutorial", "default", "color")),
            },
        },
        "tab": {
            "selected": color("{core.color.violet}", measured("tab", "selected", "backgroundColor")),
            "idle": color("{core.color.tab-idle}", measured("tab", "default", "backgroundColor")),
        },
    },
    "$themes": [
        {"id": "dark", "name": "dark", "selectedTokenSets": {"core": "source", "dark": "enabled"}},
    ],
}

# Resolve aliases for the check, then write aliases as stored.
def walk(node, path=""):
    if isinstance(node, dict) and "$value" in node:
        val = node["$value"]
        ty = node.get("$type")
        if isinstance(val, str) and val.startswith("{") and val.endswith("}"):
            return
        if ty == "dimension" and not re.fullmatch(r"-?\d+(\.\d+)?(px|rem)", str(val)):
            raise SystemExit(f"{path}: bad dimension {val}")
        if ty == "color" and not (str(val).startswith("#") or str(val).startswith("rgb")):
            raise SystemExit(f"{path}: bad color {val}")
        if "$extensions" not in node or "source" not in node["$extensions"]:
            raise SystemExit(f"{path}: missing source")
        return
    if isinstance(node, dict):
        for k, v in node.items():
            if k.startswith("$"):
                continue
            walk(v, path + "." + k)

walk(doc)
out = HERE / "tokens.json"
out.write_text(json.dumps(doc, indent=2) + "\n")
print("wrote", out, "bytes", out.stat().st_size)
