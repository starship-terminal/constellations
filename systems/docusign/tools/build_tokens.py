#!/usr/bin/env python3
"""Build tokens.json from measured computed styles on www.docusign.com.

DocuSign's public marketing site declares no design-token custom properties.
Every value here was read from getComputedStyle on the live homepage in
headless Chromium on 2026-11-21 (signed out, 1440 x 900). The readings live
in raw/measurements.json. A value that was not read is absent, not guessed.

Light only. No dark theme was painted on the captured routes.
"""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = json.loads((HERE / "raw" / "measurements.json").read_text())


def color(value, source):
    return {"$value": value, "$type": "color", "$extensions": {"source": source}}


def dim(value, source):
    return {"$value": value, "$type": "dimension", "$extensions": {"source": source}}


def font_weight(value, source):
    return {"$value": value, "$type": "fontWeight", "$extensions": {"source": source}}


def font_family(value, source):
    return {"$value": value, "$type": "fontFamily", "$extensions": {"source": source}}


def duration(value, source):
    return {"$value": value, "$type": "duration", "$extensions": {"source": source}}


def cubic(value, source):
    return {"$value": value, "$type": "cubicBezier", "$extensions": {"source": source}}


def typography(size, weight, line_height, source):
    return {
        "$value": {
            "fontFamily": "{font.family.ui}",
            "fontSize": size,
            "fontWeight": weight,
            "lineHeight": line_height,
        },
        "$type": "typography",
        "$extensions": {"source": source},
    }


def number(value, source):
    return {"$value": value, "$type": "number", "$extensions": {"source": source}}


M = RAW["measured"]
S = "measured getComputedStyle on https://www.docusign.com/ signed out, 2026-11-21"

core = {
    "font": {
        "family": {
            "ui": font_family(M["fontFamily"], f"{S}; body, h1, buttons"),
            "fallback": font_family("Helvetica, Arial, sans-serif", f"{S}; the named fallbacks after DS Indigo"),
        },
        "weight": {
            "light": number(300, f"{S}; h1 font-weight"),
            "regular": number(400, f"{S}; body font-weight"),
            "medium": number(500, f"{S}; h3 font-weight"),
            "semibold": number(600, f"{S}; nav CTA font-weight"),
        },
    },
    "color": {
        "ink": color(M["ink"], f"{S}; body color"),
        "inkMuted": color(M["inkMuted"], f"{S}; first paragraph color"),
        "paper": color(M["paper"], f"{S}; body background"),
        "accent": color(M["accent"], f"{S}; TRY FOR FREE background and CONTACT SALES color"),
        "onAccent": color(M["onAccent"], f"{S}; TRY FOR FREE color"),
        "inkStrong": color(M["inkStrong"], f"{S}; Get Started button background"),
        "heroBand": color(M["heroBand"], f"{S}; a dark section background"),
        "sand": color(M["sand"], f"{S}; footer background"),
        "sandDeep": color(M["sandDeep"], f"{S}; locale strip background"),
        "fieldBorder": color(M["fieldBorder"], f"{S}; workEmail input border"),
        "focus": color(M["focus"], f"{S}; TRY FOR FREE outline after focus()"),
    },
    "radius": {
        "control": dim(M["radiusControl"], f"{S}; TRY FOR FREE border-radius"),
    },
    "space": {
        "controlX": dim("16px", f"{S}; TRY FOR FREE padding-inline"),
        "controlY": dim("12px", f"{S}; TRY FOR FREE padding-block"),
    },
    "size": {
        "control": dim(M["controlHeight"], f"{S}; TRY FOR FREE height"),
        "field": dim(M["fieldHeight"], f"{S}; workEmail input height"),
    },
    "motion": {
        "control": duration("100ms", f"{S}; button transition-duration 0.1s"),
        "ease": cubic([0.33, 0, 0.67, 1], f"{S}; button cubic-bezier(0.33, 0, 0.67, 1)"),
    },
    "typography": {
        "display": typography("80px", "{font.weight.light}", "86.4px", f"{S}; h1"),
        "heading": typography("58px", "{font.weight.light}", "62.64px", f"{S}; h2"),
        "title": typography("24px", "{font.weight.medium}", "29.76px", f"{S}; h3"),
        "body": typography("16px", "{font.weight.regular}", "24px", f"{S}; body font-size 16px; line-height was keyword normal, 24px is Derived"),
        "label": typography("14px", "{font.weight.semibold}", "21px", f"{S}; nav CTA"),
        "caption": typography("14px", "{font.weight.regular}", "21px", f"{S}; footer and first paragraph"),
    },
}

light = {
    "page": color("{color.paper}", "alias of measured body background"),
    "surface": color("{color.sand}", "alias of measured footer background"),
    "text": color("{color.ink}", "alias of measured body color"),
    "muted": color("{color.inkMuted}", "alias of measured paragraph color"),
    "accent": color("{color.accent}", "alias of measured primary button background"),
    "onAccent": color("{color.onAccent}", "alias of measured primary button color"),
    "border": color("{color.fieldBorder}", "alias of measured field border"),
    "focus": color("{color.focus}", "alias of measured focus outline"),
}

tokens = {
    "core": core,
    "light": light,
    "$themes": [
        {"id": "light", "name": "light", "selectedTokenSets": {"core": "enabled", "light": "enabled"}},
    ],
}

(HERE / "tokens.json").write_text(json.dumps(tokens, indent=1) + "\n")
print("wrote", HERE / "tokens.json")
