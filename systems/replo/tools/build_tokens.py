#!/usr/bin/env python3
"""Build tokens.json from the Replo public capture.

Sources, read from www.replo.app on 2026-11-21:
  raw/css-vars.json     stylesheet custom properties (tools/capture/vars.mjs)
  raw/live.json         computed styles of real elements on the home page
The marketing site paints one dark surface. :root in the bundle is a light
shadcn set that the homepage does not apply (html has no .dark class, body
paints black). Those light names are recorded as declared, not as the
painted theme. Every token carries $extensions.source.
"""
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
V = json.loads((RAW / "css-vars.json").read_text())
LIVE = json.loads((RAW / "live.json").read_text())
RES = V["resolved"]["light"]


def color(name, value, source):
    return {"$value": value, "$type": "color", "$extensions": {"source": source}}


def dim(value, source):
    if not re.fullmatch(r"-?\d+(\.\d+)?(px|rem)", str(value)):
        raise ValueError(f"{name}: not a dimension: {value}")
    return {"$value": value, "$type": "dimension", "$extensions": {"source": source}}


def font(value, source):
    return {"$value": value, "$type": "fontFamily", "$extensions": {"source": source}}


def number(value, source):
    return {"$value": value, "$type": "number", "$extensions": {"source": source}}


def text(value, source):
    return {"$value": value, "$type": "other", "$extensions": {"source": source}}


def from_var(token_name):
    hit = RES.get(token_name)
    if not hit or "value" not in hit:
        raise KeyError(token_name)
    return hit["value"], f"css-var {token_name} (raw/css-vars.json, resolved on the home-page probe)"


def live_src(el, prop):
    return f"measured computed {prop} of {el} on https://www.replo.app/ at 1440x900 (raw/live.json)"


# Brand colours the stylesheet names and the probe resolved to sRGB.
brand = {
    "cream": from_var("--color-replo-cream"),
    "ink": from_var("--color-ink"),
    "ink-muted": from_var("--color-ink-muted"),
    "ink-faint": from_var("--color-ink-faint"),
    "button": from_var("--color-replo-button"),
    "button-fg": from_var("--color-replo-button-fg"),
    "panel": from_var("--color-replo-panel"),
    "surface-card": from_var("--color-surface-card"),
    "surface-glass": from_var("--color-surface-glass"),
    "black": from_var("--color-black"),
    "white": from_var("--color-white"),
    "accent-blue": from_var("--color-accent-blue"),
    "accent-green": from_var("--color-accent-green"),
    "accent-magenta": from_var("--color-accent-magenta"),
    "accent-pink": from_var("--color-accent-pink"),
    "accent-purple": from_var("--color-accent-purple"),
}

# Hex form of the painted page, read off the body, matching --color-black.
page_bg = LIVE["body"]["bg"]  # rgb(0, 0, 0)
text_color = LIVE["body"]["color"]  # rgb(245, 250, 217) == --color-ink

core = {
    "color": {
        "brand": {k: color(k, v, s) for k, (v, s) in brand.items()},
    },
    "font": {
        "family": {
            "sans": font(
                'archivo, "archivo Fallback", Arial, sans-serif',
                live_src("body", "fontFamily"),
            ),
            "display": font(
                'archivo, "archivo Fallback", Arial, sans-serif',
                live_src("h1", "fontFamily"),
            ),
        },
        "size": {
            "body": dim(LIVE["body"]["size"], live_src("body", "fontSize")),
            "display": dim(LIVE["h1"]["size"], live_src("h1", "fontSize")),
            "nav": dim(LIVE["product"]["size"], live_src("Product button", "fontSize")),
            "button": dim(LIVE["start"]["size"], live_src("Start for free", "fontSize")),
        },
        "weight": {
            "body": number(int(LIVE["body"]["weight"]), live_src("body", "fontWeight")),
            "display": number(int(LIVE["h1"]["weight"]), live_src("h1", "fontWeight")),
        },
        "line-height": {
            "body": dim(LIVE["body"]["lh"], live_src("body", "lineHeight")),
            "display": dim(LIVE["h1"]["lh"], live_src("h1", "lineHeight")),
        },
    },
    "radius": {
        "pill": dim("9999px", live_src("Start for free", "borderRadius")),
        "control": dim("10px", "derived from --radius .625rem at a 16px root (raw/css-vars.json :root --radius)"),
    },
    "spacing": {
        "button-x": dim("16px", live_src("Start for free", "paddingLeft")),
        "nav-x": dim("12px", live_src("Product button", "paddingLeft")),
        "nav-y": dim("8px", live_src("Product button", "paddingTop")),
    },
}

# Semantic set is the painted marketing surface. Named dark because that is
# the only surface the public pages paint. The bundle's :root light values
# are not applied on those pages.
dark = {
    "page": color("page", "#000000", live_src("body", "backgroundColor") + "; matches css-var --color-black"),
    "surface": color("surface", brand["surface-card"][0], brand["surface-card"][1]),
    "raised": color("raised", brand["surface-glass"][0], brand["surface-glass"][1]),
    "panel": color("panel", brand["panel"][0], brand["panel"][1]),
    "text": color("text", "#f5fad9", live_src("body", "color") + "; matches css-var --color-ink"),
    "muted": color("muted", brand["ink-muted"][0], brand["ink-muted"][1]),
    "faint": color("faint", brand["ink-faint"][0], brand["ink-faint"][1]),
    "accent": color("accent", brand["button"][0], brand["button"][1] + "; painted on Start for free as rgb(245, 250, 217)"),
    "accent-text": color("accent-text", brand["button-fg"][0], brand["button-fg"][1] + "; painted on Start for free as rgb(18, 18, 18)"),
    "border": color("border", "rgba(245, 250, 217, 0.24)", live_src("Book a demo", "borderTopColor")),
    "focus": color("focus", "#a1a1a1", "declared --ring on :root (raw/css-vars.json). Not observed as a painted ring on the marketing controls."),
    "destructive": color("destructive", "#ff6568", "declared --destructive on .dark (raw/css-vars.json). Not observed painted on the public marketing pages."),
    "component": {
        "control": {
            "height": dim(f"{LIVE['start']['h']}px", live_src("Start for free", "height")),
            "radius": {"$value": "{core.radius.pill}", "$type": "dimension", "$extensions": {"source": "alias of the painted pill radius"}},
        },
        "header": {
            "height": dim(f"{LIVE['header']['h']}px", live_src("header", "height")),
        },
        "type": {
            "display": dim(LIVE["h1"]["size"], live_src("h1", "fontSize")),
        },
    },
}

# Declared light set from :root hex (the values outside the lab() override).
# Labelled so a reader does not treat them as the painted marketing theme.
LIGHT_DECLARED = {
    "background": "#ffffff",
    "foreground": "#0a0a0a",
    "card": "#ffffff",
    "primary": "#171717",
    "primary-foreground": "#fafafa",
    "secondary": "#f5f5f5",
    "muted": "#737373",
    "destructive": "#e40014",
    "border": "#e5e5e5",
    "ring": "#a1a1a1",
}
light = {
    k: color(k, v, "declared :root custom property in the marketing stylesheet (raw/css-vars.json). The public pages do not apply this set: html has no .dark class and body paints #000000.")
    for k, v in LIGHT_DECLARED.items()
}

doc = {
    "core": core,
    "dark": dark,
    "light": light,
    "$themes": [
        {
            "id": "dark",
            "name": "Dark",
            "selectedTokenSets": {"core": "source", "dark": "enabled"},
            "$description": "The only theme www.replo.app paints on the public marketing pages.",
        }
    ],
    "$metadata": {"tokenSetOrder": ["core", "dark", "light"]},
}

out = HERE / "tokens.json"
out.write_text(json.dumps(doc, indent=2) + "\n")
print("wrote", out, "core colors", len(core["color"]["brand"]))
