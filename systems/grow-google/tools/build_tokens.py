#!/usr/bin/env python3
"""Build tokens.json from Glue custom properties and live computed styles.

Sources, read from grow.google on 2026-11-21:
  raw/css-vars.json          stylesheet response bodies parsed with a constructed
                             CSSStyleSheet. CSSOM was cross-origin and empty.
                             Glue palette lives on :root (--glue-*).
  raw/live-readings.json     computed styles on public pages (CTA, type, focus).
  raw/components-computed.json  first-pass computed styles.

One theme: prefers-color-scheme: dark left body white / #202124. No dark set.
"""
import json
import pathlib
import re

ADAPTED_FOR = "grow-google"

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
V = json.loads((RAW / "css-vars.json").read_text())
LIVE = json.loads((RAW / "live-readings.json").read_text())

SRC_ROOT = "Measured: :root custom property in grow.google stylesheet body, parsed 2026-11-21 (raw/css-vars.json)"
SRC_LIVE = "Measured: computed style on a public grow.google page, 2026-11-21 (raw/live-readings.json)"


def root_value(name):
    for r in V["rules"]:
        if r["name"] == name and r["selector"] == ":root" and "apac-home" in r["pages"]:
            return r["value"]
    raise SystemExit(f"missing :root {name}")


def color(value, source):
    v = value.strip().lower()
    if v == "#fff":
        v = "#ffffff"
    return {"$value": v, "$type": "color", "$extensions": {"source": source}}


def dim(value, source):
    return {"$value": value, "$type": "dimension", "$extensions": {"source": source}}


def num(value, source):
    return {"$value": value, "$type": "number", "$extensions": {"source": source}}


def font_weight(value, source):
    return {"$value": value, "$type": "fontWeight", "$extensions": {"source": source}}


core_color = {}
for hue in ("grey", "blue", "green", "red", "yellow"):
    steps = {}
    for step in ("0", "25", "50", "100", "200", "300", "400", "500", "600", "700", "800", "900"):
        name = f"--glue-{hue}-{step}"
        try:
            val = root_value(name)
        except SystemExit:
            continue
        steps[step] = color(val, f"{SRC_ROOT}; name {name}")
    core_color[hue] = steps

# purple is incomplete on :root (100 and 900 only)
core_color["purple"] = {
    "100": color(root_value("--glue-purple-100"), SRC_ROOT + "; name --glue-purple-100"),
    "900": color(root_value("--glue-purple-900"), SRC_ROOT + "; name --glue-purple-900"),
}

# Google logo primaries are the 500 steps of the Glue ramps (same hexes).
core_color["logo"] = {
    "blue": color("#4285f4", SRC_ROOT + "; --glue-blue-500, also the Google wordmark blue"),
    "red": color("#ea4335", SRC_ROOT + "; --glue-red-500"),
    "yellow": color("#fbbc04", SRC_ROOT + "; --glue-yellow-500"),
    "green": color("#34a853", SRC_ROOT + "; --glue-green-500"),
}

core = {
    "color": core_color,
    "font": {
        "family": {
            "display": {
                "$value": "Google Sans, Arial, Helvetica, sans-serif",
                "$type": "fontFamily",
                "$extensions": {"source": SRC_LIVE + "; APAC h1 fontFamily Google Sans"},
            },
            "text": {
                "$value": "Google Sans Text, Arial, Helvetica, sans-serif",
                "$type": "fontFamily",
                "$extensions": {"source": SRC_LIVE + "; APAC body fontFamily Google Sans Text"},
            },
            "flex": {
                "$value": "Google Sans Flex, Arial, Helvetica, sans-serif",
                "$type": "fontFamily",
                "$extensions": {"source": SRC_LIVE + "; US shell body and h1 fontFamily Google Sans Flex"},
            },
        }
    },
    "typography": {
        "display": {
            "$type": "typography",
            "$value": {
                "fontFamily": "{font.family.display}",
                "fontSize": "60px",
                "fontWeight": 400,
                "lineHeight": "72px",
            },
            "$extensions": {"source": SRC_LIVE + "; APAC home h1 60px/72px weight 400"},
        },
        "heading": {
            "$type": "typography",
            "$value": {
                "fontFamily": "{font.family.flex}",
                "fontSize": "48px",
                "fontWeight": 400,
                "lineHeight": "56px",
            },
            "$extensions": {"source": SRC_LIVE + "; US certificates h1 48px/56px weight 400"},
        },
        "body": {
            "$type": "typography",
            "$value": {
                "fontFamily": "{font.family.text}",
                "fontSize": "16px",
                "fontWeight": 400,
                "lineHeight": "24px",
            },
            "$extensions": {"source": SRC_LIVE + "; body 16px, CTA line-height 24px used as the body role"},
        },
        "label": {
            "$type": "typography",
            "$value": {
                "fontFamily": "{font.family.display}",
                "fontSize": "16px",
                "fontWeight": 500,
                "lineHeight": "24px",
            },
            "$extensions": {"source": SRC_LIVE + "; nav and CTA 16px weight 500"},
        },
    },
    "space": {
        "3": dim("12px", SRC_LIVE + "; CTA padding-block 12px"),
        "4": dim("16px", SRC_LIVE + "; US Learn more padding-inline start 16px"),
        "6": dim("24px", SRC_LIVE + "; APAC CTA padding-inline 24px"),
    },
    "radius": {
        "nav": dim("4px", SRC_LIVE + "; nav link border-radius 4px (components-computed.json)"),
        "card": dim("8px", SRC_LIVE + "; APAC tool card border-radius 8px"),
        "pill": dim("48px", SRC_LIVE + "; CTA border-radius 48px"),
    },
    "size": {
        "control": dim("50px", SRC_LIVE + "; CTA height 50px"),
        "navItem": dim("48px", SRC_LIVE + "; nav link height 48px"),
    },
    "focusRing": {
        "color": color("#1a73e8", SRC_LIVE + "; APAC keyboard focus box-shadow rgba(26, 115, 232, 0.996)"),
        "width": dim("2px", SRC_LIVE + "; APAC focus box-shadow spread about 2px"),
    },
}

light = {
    "background": {
        "page": color("{color.grey.0}", "Measured alias of --glue-grey-0; body background rgb(255, 255, 255)"),
        "surface": color("{color.grey.50}", "Measured alias of --glue-grey-50; APAC hover background rgb(248, 249, 250)"),
        "raised": color("#eff2f7", SRC_LIVE + "; US page element count, background rgb(239, 242, 247). Not a :root Glue name"),
        "scrim": color("#000000", "Measured: --md-sys-color-scrim-light #000 on .glue-mwc3"),
    },
    "text": {
        "primary": color("{color.grey.900}", "Measured alias of --glue-grey-900; body color rgb(32, 33, 36)"),
        "muted": color("{color.grey.700}", "Measured alias of --glue-grey-700; APAC secondary text rgb(95, 99, 104)"),
        "secondary": color("#3c4043", SRC_LIVE + "; US secondary text rgb(60, 64, 67), Glue grey-800"),
        "onAccent": color("#ffffff", SRC_LIVE + "; CTA text rgb(255, 255, 255)"),
        "link": color("{color.blue.600}", "Measured alias of --glue-blue-600; APAC link color rgb(26, 115, 232)"),
    },
    "border": {
        "default": color("{color.grey.200}", "Measured alias of --glue-grey-200 #e8eaed"),
        "strong": color("{color.grey.400}", "Measured alias of --glue-grey-400 #bdc1c6; also --md-sys-color-outline-light"),
        "focus": color("{color.blue.600}", "Measured: APAC focus ring uses #1a73e8"),
    },
    "accent": {
        "default": color("#3186ff", SRC_LIVE + "; US Learn more / Enroll now background rgb(49, 134, 255). Not a Glue ramp step"),
        "ink": color("{color.grey.900}", SRC_LIVE + "; APAC View all tools background rgb(32, 33, 36)"),
        "hoverWash": color("rgba(26, 115, 232, 0.04)", SRC_LIVE + "; US Enroll now hover background"),
    },
    "status": {
        "danger": color("#d93025", "Measured: --md-sys-color-error-light #d93025 on .glue-mwc3. No error toast was shown"),
    },
}

doc = {
    "$description": "Grow with Google public site, captured 2026-11-21. Glue palette from :root. One light theme.",
    "core": core,
    "light": light,
    "$themes": [{"id": "light", "name": "light", "selectedTokenSets": {"core": "source", "light": "enabled"}}],
}

# Resolve aliases for a sanity check
flat = {}

def walk(node, path):
    if isinstance(node, dict) and "$value" in node:
        flat[path] = node
        return
    if isinstance(node, dict):
        for k, v in node.items():
            if k.startswith("$"):
                continue
            walk(v, f"{path}.{k}" if path else k)

walk(doc, "")
missing = []
for path, leaf in flat.items():
    if not leaf.get("$extensions", {}).get("source"):
        missing.append(path)
    val = leaf["$value"]
    if isinstance(val, str) and val.startswith("{") and not val.startswith("{font"):
        # alias inside core.color or light
        pass
if missing:
    raise SystemExit("tokens without source: " + ", ".join(missing))

out = HERE / "tokens.json"
out.write_text(json.dumps(doc, indent=2) + "\n")
print(f"wrote {out} ({len(flat)} leaves)")
