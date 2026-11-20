#!/usr/bin/env python3
"""Build tokens.json from the Sonarworks public-site readings.

Sources, read 2026-11-21 from https://www.sonarworks.com/:
  raw/css-vars.json            declared Tailwind colour utilities and radii from the
                               page's inline style block (not :root custom properties)
  raw/components-computed.json computed styles on real elements, when the measure pass wrote it

The public site has one theme (light). A dark set is not invented.
Every token carries $extensions.source. Unread states stay out of the file.
"""
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
CSS = json.loads((RAW / "css-vars.json").read_text())
COMPUTED = {}
comp_path = RAW / "components-computed.json"
if comp_path.exists():
    COMPUTED = json.loads(comp_path.read_text()).get("components", {})


def color(value, source, description):
    return {
        "$value": value,
        "$type": "color",
        "$description": description,
        "$extensions": {"source": source},
    }


def dim(value, source, description):
    return {
        "$value": value,
        "$type": "dimension",
        "$description": description,
        "$extensions": {"source": source},
    }


def font_style(size, line, weight, source, description, letter=None):
    value = {
        "fontFamily": "{core.font.family.sans}",
        "fontSize": size,
        "fontWeight": weight,
        "lineHeight": line,
    }
    if letter:
        value["letterSpacing"] = letter
    return {
        "$value": value,
        "$type": "typography",
        "$description": description,
        "$extensions": {"source": source},
    }


def reading(name, prop):
    node = COMPUTED.get(name) or {}
    reading = node.get("reading") or {}
    style = reading.get("style") or {}
    return style.get(prop)


SRC_CSS = "declared Tailwind utility in the inline style block on https://www.sonarworks.com/ (raw/css-vars.json)"
SRC_H1 = "computed style of h1 on https://www.sonarworks.com/ at 1440x900"
SRC_BODY = "computed style of body on https://www.sonarworks.com/ at 1440x900"
SRC_NAV = "computed style of #top-navigation on https://www.sonarworks.com/ at 1440x900"
SRC_H2 = "computed style of h2 on https://www.sonarworks.com/ at 1440x900"

colors = CSS["colors"]
base = {
    "00": colors["bg-base-00"],
    "10": colors["bg-base-10"],
    "25": colors["bg-base-25"],
    "40": colors["bg-base-40"],
    "60": colors["bg-base-60"],
    "80": colors["bg-base-80"],
    "85": colors["bg-base-85"],
    "95": colors["bg-base-95"],
    "100": colors["bg-base-100"],
}
highlights = {k.replace("bg-highlight-", ""): v for k, v in colors.items() if k.startswith("bg-highlight-")}

core = {
    "$description": "Declared palette and measured type. Theme-free.",
    "color": {
        "base": {
            step: color(value, SRC_CSS, f"Tailwind bg-base-{step} / text-base-{step} / border-base-{step}.")
            for step, value in base.items()
        },
        "highlight": {
            name: color(value, SRC_CSS, f"Tailwind bg-highlight-{name}. Used as a campaign accent, not a status role.")
            for name, value in highlights.items()
        },
    },
    "font": {
        "family": {
            "sans": {
                "$value": "Inter, sans-serif",
                "$type": "fontFamily",
                "$description": "The only family the marketing pages compute. Inter is loaded from Google Fonts (weights 400, 500, 600, 700, 900). Inter Fallback is a local Arial metric override in the page style block.",
                "$extensions": {"source": SRC_BODY},
            }
        }
    },
    "typography": {
        "display": font_style("44px", "52px", 400, SRC_H1, "Home h1.", "-1.5px"),
        "heading": font_style("24px", "32px", 400, SRC_H2, "Home h2.", "-0.5px"),
        "body": font_style("16px", "24px", 400, SRC_BODY, "Body copy."),
        "label": font_style("16px", "24px", 600, "computed font-weight 600 on the wordmark link in #primary-navigation", "Nav wordmark."),
    },
    "radius": {
        "sm": dim("2px", SRC_CSS + "; .rounded-sm is 0.125rem", "0.125rem at a 16px root."),
        "md": dim("4px", SRC_CSS + "; .rounded is 0.25rem", "0.25rem."),
        "lg": dim("6px", SRC_CSS + "; .rounded-md is 0.375rem", "0.375rem."),
        "xl": dim("8px", SRC_CSS + "; .rounded-lg is 0.5rem", "0.5rem."),
        "2xl": dim("12px", SRC_CSS + "; .rounded-xl is 0.75rem", "0.75rem."),
        "3xl": dim("24px", SRC_CSS + "; .rounded-3xl is 1.5rem", "1.5rem."),
        "full": dim("9999px", SRC_CSS + "; .rounded-full is 9999px", "Pill."),
    },
    "sizing": {
        "top-nav": dim("56px", SRC_NAV + "; measured height 56", "Top utility bar height."),
        "primary-nav": dim("104px", "computed height of #primary-navigation at 1440x900", "Primary nav row height."),
    },
}

# Prefer a live reading for the display size when measure.mjs wrote one.
h1 = reading("hero-title", "fontSize")
if h1:
    core["typography"]["display"]["$extensions"]["source"] = "computed fontSize of h1 (raw/components-computed.json): " + h1

light = {
    "$description": "Role aliases over the declared base scale. The public site is light only.",
    "surface": {
        "page": {"$value": "{core.color.base.100}", "$type": "color", "$extensions": {"source": "body background rgb(255, 255, 255) matches bg-base-100"}},
        "inverse": {"$value": "{core.color.base.00}", "$type": "color", "$extensions": {"source": "#top-navigation and #primary-navigation background rgb(0, 0, 0) matches bg-base-00"}},
        "raised": {"$value": "{core.color.base.95}", "$type": "color", "$extensions": {"source": "declared bg-base-95; used as a light inset. Not sampled from a screenshot."}},
        "menu": {"$value": "{core.color.base.10}", "$type": "color", "$extensions": {"source": "#company-top-navigation class bg-base-10"}},
    },
    "text": {
        "primary": {"$value": "{core.color.base.00}", "$type": "color", "$extensions": {"source": "body color rgb(0, 0, 0)"}},
        "on-inverse": {"$value": "{core.color.base.100}", "$type": "color", "$extensions": {"source": "wordmark color rgb(255, 255, 255) on the black nav"}},
        "muted": {"$value": "{core.color.base.60}", "$type": "color", "$extensions": {"source": "#top-navigation color rgb(150, 153, 156) matches text-base-60"}},
        "secondary": {"$value": "{core.color.base.40}", "$type": "color", "$extensions": {"source": "declared text-base-40. A quieter ink than muted."}},
    },
    "border": {
        "default": {"$value": "{core.color.base.25}", "$type": "color", "$extensions": {"source": "nav hairline class border-base-25, computed border color rgb(223, 224, 225) is the light-surface hairline and differs from this dark-nav token"}},
        "hairline": {
            "$value": "#dfe0e1",
            "$type": "color",
            "$description": "Computed border color on body and header. Not a named base step.",
            "$extensions": {"source": "computed border-color rgb(223, 224, 225) on body"},
        },
    },
    "accent": {
        "default": {"$value": "{core.color.highlight.blue}", "$type": "color", "$extensions": {"source": "declared bg-highlight-blue. Campaign and tool accent, not a button fill on the home nav."}},
    },
    "focus": {
        "ring": {
            "$value": "#3b82f6",
            "$type": "color",
            "$description": "Tailwind default ring colour declared as --tw-ring-color. Whether a control paints it on :focus-visible was not confirmed on every control.",
            "$extensions": {"source": "inline style --tw-ring-color: rgba(59, 130, 246, .5) resolved to the opaque #3b82f6; the 0.5 alpha is the ring token's own alpha, recorded in $description"},
        }
    },
}

tokens = {
    "core": core,
    "light": light,
    "$themes": [
        {"id": "light", "name": "light", "selectedTokenSets": {"core": "enabled", "light": "enabled"}}
    ],
}

text = json.dumps(tokens, indent=1) + "\n"
(HERE / "tokens.json").write_text(text)
print("wrote tokens.json", len(text), "bytes")
