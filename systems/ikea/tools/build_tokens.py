#!/usr/bin/env python3
"""Build systems/ikea/tokens.json from raw/css-vars.json.

IKEA declares colours as comma-separated RGB channels on :root
(--colour-neutral-1: 255, 255, 255). This builder turns those channels
into hex and labels every token Measured. Typography sizes were read
from computed styles on the public homepage (h1, body) and are Derived
only where a px value was computed, with the source naming the element.
"""
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = json.loads((HERE / "raw" / "css-vars.json").read_text())
RESOLVED = RAW["resolved"]


def hex_of(channels):
    parts = [int(x.strip()) for x in channels.split(",")[:3]]
    if len(parts) != 3:
        raise ValueError(channels)
    return "#%02x%02x%02x" % tuple(parts)


def color(name, description):
    key = "--colour-" + name
    if key not in RESOLVED:
        raise SystemExit("missing " + key)
    return {
        "$value": hex_of(RESOLVED[key]),
        "$type": "color",
        "$description": description,
        "$extensions": {
            "source": "Measured: computed custom property %s on :root at https://www.ikea.com/sg/en/ (raw/css-vars.json, 2026-11-21)" % key,
            "evidence": "Measured",
        },
    }


def dim(value, source, description):
    if not re.fullmatch(r"-?\d+(\.\d+)?(px|rem)", value):
        raise SystemExit("bad dimension " + value)
    return {
        "$value": value,
        "$type": "dimension",
        "$description": description,
        "$extensions": {"source": source, "evidence": "Measured"},
    }


core = {
    "$description": "IKEA public storefront scales. Colours alias the light semantic set.",
    "font": {
        "family": {
            "sans": {
                "$value": "Noto IKEA, Noto Sans, system-ui, sans-serif",
                "$type": "fontFamily",
                "$description": "The first real family in --ikea-font after currency-symbol faces.",
                "$extensions": {
                    "source": "Measured: computed --ikea-font and body fontFamily on https://www.ikea.com/sg/en/",
                    "evidence": "Measured",
                },
            }
        }
    },
    "typography": {
        "display": {
            "$type": "typography",
            "$value": {
                "fontFamily": "{font.family.sans}",
                "fontSize": "40px",
                "fontWeight": 700,
                "lineHeight": "50px",
            },
            "$extensions": {
                "source": "Measured: computed style of h1.pub__typography-heading-xl on the homepage",
                "evidence": "Measured",
            },
        },
        "body": {
            "$type": "typography",
            "$value": {
                "fontFamily": "{font.family.sans}",
                "fontSize": "14px",
                "fontWeight": 400,
                "lineHeight": "14px",
            },
            "$extensions": {
                "source": "Measured: computed font-size 14px and font-weight 400 on body at https://www.ikea.com/sg/en/. lineHeight was not read. The 14px line height repeats the font size so the composite token stays valid. It is not a measured line height.",
                "evidence": "Derived",
            },
        },
        "label": {
            "$type": "typography",
            "$value": {
                "fontFamily": "{font.family.sans}",
                "fontSize": "12px",
                "fontWeight": 700,
                "lineHeight": "16px",
            },
            "$extensions": {
                "source": "Not captured as a custom property. Size is the utility-bar label seen in the header screenshot; weight 700 is the bold utility text. Treat as Observed until a computed reading is stored.",
                "evidence": "Not captured",
            },
        },
    },
    "radius": {
        "none": dim("0px", "Measured: --product-image-radius-m and --product-image-radius-s are 0px", "Product images are square."),
        "pill": {
            "$value": "64px",
            "$type": "dimension",
            "$description": "Primary buttons are pills. Exact radius was not a custom property.",
            "$extensions": {
                "source": "Not captured: pill radius is visible on Log in and cookie buttons but was not read from CSS.",
                "evidence": "Not captured",
            },
        },
    },
    "space": {
        "1": dim("4px", "Not captured as a declared scale. 4px is a Derived step from the 8px rhythm visible in header padding.", "Not a declared token."),
    },
}

# The space.1 source says Not captured. Do not pretend it is a scale.
# Remove the invented space token so the package does not ship a guessed scale.
del core["space"]
del core["typography"]["label"]
del core["radius"]["pill"]

light = {
    "$description": "IKEA light theme. The public Singapore site had no dark theme switch.",
    "color": {
        "neutral": {str(i): color("neutral-%d" % i, "Neutral step %d." % i) for i in range(1, 8)},
        "text": {
            "primary": color("text-and-icon-1", "Primary text and icons."),
            "secondary": color("text-and-icon-2", "Body text."),
            "muted": color("text-and-icon-3", "Muted text."),
            "disabled": color("text-and-icon-4", "Disabled text."),
            "onAccent": color("text-and-icon-5", "Text on a dark or accent fill."),
        },
        "brand": {
            "blue": color("static-ikea-brand-blue", "IKEA blue."),
            "yellow": color("static-ikea-brand-yellow", "IKEA yellow."),
            "family": color("static-ikea-family", "IKEA Family blue."),
        },
        "interactive": {
            "primary": color("interactive-primary-bg-default", "Primary button fill."),
            "primaryHover": color("interactive-primary-bg-hover", "Primary button hover."),
            "primaryPressed": color("interactive-primary-bg-pressed", "Primary button pressed."),
            "secondary": color("interactive-secondary-bg-default", "Secondary button fill."),
            "emphasised": color("interactive-emphasised-bg-default", "Emphasised (blue) button fill."),
            "destructive": color("interactive-destructive-bg-default", "Destructive button fill."),
        },
        "semantic": {
            "info": color("semantic-informative", "Informative."),
            "success": color("semantic-positive", "Positive."),
            "warning": color("semantic-caution", "Caution."),
            "danger": color("semantic-negative", "Negative."),
        },
        "elevation": {
            "1": color("elevation-1", "Raised surface."),
            "border": color("elevation-1-border", "Raised surface border."),
        },
        "commercial": {
            "new": color("commercial-message-new", "New badge."),
            "lowerPrice": color("commercial-message-new-lower-price", "Lower price badge."),
        },
    },
    "background": {
        "page": color("neutral-1", "Page ground."),
        "surface": color("neutral-2", "Inset surface, category tiles, search field."),
        "inverse": color("neutral-7", "Utility bar and primary button."),
    },
    "text": {
        "primary": color("text-and-icon-1", "Primary text."),
        "secondary": color("text-and-icon-2", "Body text."),
        "muted": color("text-and-icon-3", "Muted text."),
        "onAccent": color("text-and-icon-5", "Text on inverse."),
        "link": color("static-ikea-brand-blue", "Brand blue used for informative and emphasised actions."),
    },
    "border": {
        "default": color("neutral-3", "Default keyline."),
        "strong": color("neutral-7", "Strong keyline and selected border."),
    },
    "accent": {
        "default": color("static-ikea-brand-yellow", "IKEA yellow. Used on the logo, not as a page fill."),
        "blue": color("static-ikea-brand-blue", "IKEA blue."),
    },
}

tokens = {
    "$schema": "https://design-tokens.org/schema.json",
    "core": core,
    "light": light,
    "$themes": [
        {"id": "light", "name": "Light", "selectedTokenSets": {"core": "enabled", "light": "enabled"}}
    ],
}

out = HERE / "tokens.json"
out.write_text(json.dumps(tokens, indent=1) + "\n")
print("wrote", out, "light colours", sum(1 for _ in light["color"]["neutral"]))
