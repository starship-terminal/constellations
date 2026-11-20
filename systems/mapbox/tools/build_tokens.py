#!/usr/bin/env python3
"""Build tokens.json from Mapbox public CSS readings.

Sources, read from https://www.mapbox.com/ on 2026-11-21, signed out:
  raw/css-vars.json              custom properties resolved on :root
  raw/components-computed.json   painted controls (the CTA face is .button_inner)

The marketing site paints one light theme. There is no dark set.
Every token carries $extensions.source. Unread values are not filled in.
"""
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
V = json.loads((RAW / "css-vars.json").read_text())
VARS = V["resolved"]["light"]["vars"]
CAPTURED = "2026-11-21"


def src(name):
    return {
        "source": f"Measured css-var {name} on :root at https://www.mapbox.com/ ({CAPTURED}), raw/css-vars.json",
        "evidence": "Measured",
    }


def color_token(name):
    raw = VARS[name].strip().lower()
    if raw == "white":
        val = "#ffffff"
    elif raw == "black":
        val = "#000000"
    elif re.fullmatch(r"#[0-9a-f]{6}", raw):
        val = raw
    else:
        raise ValueError(f"{name}: not a flat colour ({raw})")
    return {"$type": "color", "$value": val, "$extensions": src(name)}


def dim_token(name):
    raw = VARS[name].strip()
    if raw.startswith("."):
        raw = "0" + raw
    if not re.fullmatch(r"-?\d+(\.\d+)?(px|rem)", raw):
        raise ValueError(f"{name}: not a dimension ({raw})")
    return {"$type": "dimension", "$value": raw, "$extensions": src(name)}


def number_token(name):
    raw = VARS[name].strip()
    if not re.fullmatch(r"-?\d+(\.\d+)?", raw):
        raise ValueError(f"{name}: not a number ({raw})")
    val = float(raw) if "." in raw else int(raw)
    return {"$type": "number", "$value": val, "$extensions": src(name)}


def group(prefix, maker, skip_deleted=True):
    out = {}
    for name, _ in sorted(VARS.items()):
        if not name.startswith(prefix):
            continue
        if skip_deleted and "<deleted" in name:
            continue
        leaf = name[len(prefix):].replace("--", "-").replace("---", "-")
        leaf = re.sub(r"[^a-zA-Z0-9-]", "-", leaf).strip("-")
        out[leaf] = maker(name)
    return out


core_color = {
    "blue": group("--_colors---blue--blue", color_token),
    "gray": group("--_colors---gray--gray", color_token),
    "green": group("--_colors---green--green", color_token),
    "orange": group("--_colors---orange--orange", color_token),
    "purple": group("--_colors---purple--purple", color_token),
    "red": group("--_colors---red--red", color_token),
    "yellow": group("--_colors---yellow--yellow", color_token),
    "primary": group("--_colors---primary--primary", color_token),
    "white": color_token("--_colors---white--white"),
    "black": color_token("--_colors---black--black"),
}
# group() on "blue" also matches blue10 because prefix is blue. Fix by rebuilding ramps from exact steps.
STEPS = ["5", "10", "20", "30", "40", "50", "60", "70", "80", "90"]


def ramp(hue):
    out = {}
    for step in STEPS:
        name = f"--_colors---{hue}--{hue}{step}"
        if name in VARS:
            out[step] = color_token(name)
    return out


core = {
    "color": {
        "blue": ramp("blue"),
        "gray": ramp("gray"),
        "green": ramp("green"),
        "orange": ramp("orange"),
        "purple": ramp("purple"),
        "red": ramp("red"),
        "yellow": ramp("yellow"),
        "primary": ramp("primary"),
        "white": color_token("--_colors---white--white"),
        "black": color_token("--_colors---black--black"),
        "ink": color_token("--_color-mode---text--cm_text-neutral-01"),
    },
    "font": {
        "family": {
            "ui": {
                "$type": "fontFamily",
                "$value": "Cera pro, Trebuchet MS, sans-serif",
                "$extensions": {
                    "source": "Measured computed font-family on body at https://www.mapbox.com/ (2026-11-21), raw/css-vars.json resolved.light.body",
                    "evidence": "Measured",
                },
            }
        },
        "weight": {
            "regular": {"$type": "fontWeight", "$value": 400, "$extensions": {"source": "Measured computed font-weight 400 on body", "evidence": "Measured"}},
            "medium": {"$type": "fontWeight", "$value": 500, "$extensions": {"source": "Measured @font-face Cera pro 500 in raw/css-vars.json fonts", "evidence": "Measured"}},
            "bold": {"$type": "fontWeight", "$value": 700, "$extensions": {"source": "Measured css-var --_heading-styles---font-weight = 700", "evidence": "Measured"}},
        },
        "size": {
            "body": dim_token("--_text-styles---font-size"),
            "xsmall": dim_token("--_text-styles---text-sizes--text-size-xsmall"),
            "small": dim_token("--_text-styles---text-sizes--text-size-small"),
            "regular": dim_token("--_text-styles---text-sizes--text-size-regular"),
            "medium": dim_token("--_text-styles---text-sizes--text-size-medium"),
            "large": dim_token("--_text-styles---text-sizes--text-size-large"),
            "navbar": dim_token("--_text-styles---text-sizes--text-size-navbar"),
            "h1": dim_token("--_heading-styles---heading-style-h1--heading-size-h1"),
            "h2": dim_token("--_heading-styles---heading-style-h2--heading-size-h2"),
            "h3": dim_token("--_heading-styles---heading-style-h3--heading-size-h3"),
            "h4": dim_token("--_heading-styles---heading-style-h4--heading-size-h4"),
            "h5": dim_token("--_heading-styles---heading-style-h5--heading-size-h5"),
            "h6": dim_token("--_heading-styles---heading-style-h6--heading-size-h6"),
        },
        "lineHeight": {
            "body": number_token("--_text-styles---line-height"),
            "h1": number_token("--_heading-styles---heading-style-h1--heading-line-height-h1"),
            "h2": number_token("--_heading-styles---heading-style-h2--heading-line-height-h2"),
        },
    },
    "space": group("--_dimensions---spacers--", dim_token),
    "radius": group("--_dimensions---border-radius--border-radius-", dim_token),
    "icon": group("--_dimensions---icon--icon-size-", dim_token),
    "layout": group("--_dimensions---max-width--max-width-", dim_token),
    "typography": {
        "body": {
            "$type": "typography",
            "$value": {
                "fontFamily": "{font.family.ui}",
                "fontSize": "{font.size.body}",
                "fontWeight": "{font.weight.regular}",
                "lineHeight": "1.6",
            },
            "$extensions": {"source": "Derived from measured body font, --_text-styles---font-size and --_text-styles---line-height", "evidence": "Derived"},
        },
        "heading": {
            "$type": "typography",
            "$value": {
                "fontFamily": "{font.family.ui}",
                "fontSize": "{font.size.h1}",
                "fontWeight": "{font.weight.bold}",
                "lineHeight": "1.2",
            },
            "$extensions": {"source": "Derived from measured h1 size/weight/line-height vars and computed Cera pro on h1", "evidence": "Derived"},
        },
    },
}

light = {
    "page": {"$type": "color", "$value": "{color.white}", "$extensions": {"source": "Alias of --_color-mode---background--cm_bg-neutral-01 = white, confirmed computed body background rgb(255,255,255)", "evidence": "Measured"}},
    "surface": {"$type": "color", "$value": "{color.gray.5}", "$extensions": {"source": "Alias of --_color-mode---background--cm_bg-neutral-02 = #f7f9fc", "evidence": "Measured"}},
    "surface-raised": {"$type": "color", "$value": "{color.gray.10}", "$extensions": {"source": "Alias of --_color-mode---background--cm_bg-neutral-03 = #eceff5", "evidence": "Measured"}},
    "text": {
        "primary": {"$type": "color", "$value": "{color.ink}", "$extensions": {"source": "Alias of --_color-mode---text--cm_text-neutral-01 = #0e1012", "evidence": "Measured"}},
        "secondary": {"$type": "color", "$value": "#333943", "$extensions": src("--_color-mode---text--cm_text-neutral-02")},
        "muted": {"$type": "color", "$value": "#566171", "$extensions": src("--_color-mode---text--cm_text-neutral-03")},
        "disabled": {"$type": "color", "$value": "#8b96aa", "$extensions": src("--_color-mode---text--cm_text-neutral-04")},
        "on-accent": {"$type": "color", "$value": "#ffffff", "$extensions": {"source": "Measured computed color rgb(255,255,255) on a.button.is-nav and .button_inner", "evidence": "Measured"}},
        "link": {"$type": "color", "$value": "{color.blue.50}", "$extensions": {"source": "Alias of --text-colors--text-primary = #007afc (deleted-name twin of the live primary text colour)", "evidence": "Measured"}},
    },
    "border": {
        "default": {"$type": "color", "$value": "#d5dae2", "$extensions": src("--nav--light-divider")},
        "strong": {"$type": "color", "$value": "#bbc2ce", "$extensions": {"source": "Measured computed border rgb(187,194,206) on a.button.stroke", "evidence": "Measured"}},
        "input": {"$type": "color", "$value": "#e3e6e8", "$extensions": {"source": "Measured css-var --hsf-field-input__border-color and computed border on the contact text field", "evidence": "Measured"}},
        "focus": {"$type": "color", "$value": "{color.blue.50}", "$extensions": {"source": "Measured computed border-top-color rgb(0,122,252) on the focused contact text field", "evidence": "Measured"}},
    },
    "accent": {
        "default": {"$type": "color", "$value": "{color.blue.50}", "$extensions": {"source": "Alias of --_colors---primary--primary = #007afc, confirmed computed background on .button_inner", "evidence": "Measured"}},
        "hover": {"$type": "color", "$value": "{color.blue.40}", "$extensions": {"source": "Measured computed background rgb(49,149,255) on .button_inner:hover and a.button.is-nav:hover", "evidence": "Measured"}},
        "soft": {"$type": "color", "$value": "{color.blue.5}", "$extensions": {"source": "Alias of --_color-mode---background--cm_bg-primary-01 = #eff7ff", "evidence": "Measured"}},
    },
    "status": {
        "success": {"$type": "color", "$value": "{color.green.50}", "$extensions": {"source": "Declared status green. No success toast was shown on the public pages.", "evidence": "Measured"}},
        "warning": {"$type": "color", "$value": "{color.orange.50}", "$extensions": {"source": "Declared status orange. No warning toast was shown.", "evidence": "Measured"}},
        "danger": {"$type": "color", "$value": "{color.red.50}", "$extensions": {"source": "Declared status red. No error toast was shown.", "evidence": "Measured"}},
        "info": {"$type": "color", "$value": "{color.blue.50}", "$extensions": {"source": "Declared info blue, same as accent.", "evidence": "Measured"}},
    },
    "nav": {
        "text": {"$type": "color", "$value": "#1c1f24", "$extensions": src("--nav--light-text-primary")},
        "muted": {"$type": "color", "$value": "#566171", "$extensions": src("--nav--light-text-secondary")},
        "menu": {"$type": "color", "$value": "#1c1f24", "$extensions": src("--nav--light-menu")},
    },
    "component": {
        "button": {
            "bg": {"$type": "color", "$value": "{accent.default}", "$extensions": {"source": "Measured .button_inner background #007afc", "evidence": "Measured"}},
            "text": {"$type": "color", "$value": "{text.on-accent}", "$extensions": {"source": "Measured .button_inner color #ffffff", "evidence": "Measured"}},
            "radius": {"$type": "dimension", "$value": "100px", "$extensions": {"source": "Measured border-radius 100px on .button_inner and a.button.is-nav; also --hsf-button__border-radius", "evidence": "Measured"}},
            "height": {"$type": "dimension", "$value": "52px", "$extensions": {"source": "Measured box height 52px on the home hero .button_inner", "evidence": "Measured"}},
            "padding": {"$type": "dimension", "$value": "21px", "$extensions": {"source": "Measured padding-right 21px on .button_inner (padding-top 15.8px is not a single length token)", "evidence": "Measured"}},
        },
        "button-stroke": {
            "bg": {"$type": "color", "$value": "#ffffff", "$extensions": {"source": "Measured a.button.stroke background transparent over white page; recorded as page white", "evidence": "Measured"}},
            "text": {"$type": "color", "$value": "#1c1f24", "$extensions": {"source": "Measured computed color rgb(28,31,36) on a.button.stroke", "evidence": "Measured"}},
            "border": {"$type": "color", "$value": "{border.strong}", "$extensions": {"source": "Measured 1px solid rgb(187,194,206) on a.button.stroke", "evidence": "Measured"}},
            "radius": {"$type": "dimension", "$value": "100px", "$extensions": {"source": "Measured border-radius 100px on a.button.stroke", "evidence": "Measured"}},
        },
        "field": {
            "radius": {"$type": "dimension", "$value": "0.5rem", "$extensions": {"source": "Measured --hsf-field-input__border-radius and computed 8px on the contact input", "evidence": "Measured"}},
            "height": {"$type": "dimension", "$value": "44px", "$extensions": {"source": "Measured contact text field box height 44px", "evidence": "Measured"}},
            "border": {"$type": "color", "$value": "{border.input}", "$extensions": {"source": "Measured contact field border #e3e6e8", "evidence": "Measured"}},
            "focus": {"$type": "color", "$value": "{border.focus}", "$extensions": {"source": "Measured contact field focus border #007afc", "evidence": "Measured"}},
        },
        "menu-link": {
            "radius": {"$type": "dimension", "$value": "6px", "$extensions": {"source": "Measured border-radius 6px on the open Products menu Mapbox GL JS link", "evidence": "Measured"}},
        },
        "nav": {
            "height": {"$type": "dimension", "$value": "63px", "$extensions": {"source": "Measured header nav box height 63px at 1440", "evidence": "Measured"}},
        },
    },
}

doc = {
    "$description": "Mapbox public marketing site, measured 2026-11-21 from https://www.mapbox.com/. Light theme only.",
    "core": core,
    "light": light,
    "$themes": [
        {"id": "light", "name": "Light", "selectedTokenSets": {"core": "enabled", "light": "enabled"}},
    ],
}

# Drop the unused core_color builder residue by not writing it.
text = json.dumps(doc, indent=2) + "\n"
(HERE / "tokens.json").write_text(text)
print("wrote", HERE / "tokens.json", "bytes", len(text))
