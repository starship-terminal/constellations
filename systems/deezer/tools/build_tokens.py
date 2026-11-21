#!/usr/bin/env python3
"""Build tokens.json from raw/css-vars.json and raw/computed-samples.json.

Values come from Deezer's Tempo custom properties on the signed-out player
(https://www.deezer.com/en/channels/explore, color-scheme dark, 2026-11-21)
and from computed styles on the public marketing homepage and the login wall.
A token whose source key is missing is omitted. Nothing is filled from memory.
"""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
VARS = json.loads((RAW / "css-vars.json").read_text())["resolved"]
SAMPLES = json.loads((RAW / "computed-samples.json").read_text())


def var(name):
    key = name if name.startswith("--") else "--" + name
    if key not in VARS or VARS[key] == "":
        raise KeyError(key)
    return VARS[key]


def color(name, description=None):
    token = {
        "$value": var(name),
        "$type": "color",
        "$extensions": {"source": "css-var " + (name if name.startswith("--") else "--" + name)},
    }
    if description:
        token["$description"] = description
    return token


def dim(value, source):
    return {"$value": value, "$type": "dimension", "$extensions": {"source": source}}


def num(value, source):
    return {"$value": value, "$type": "number", "$extensions": {"source": source}}


def text(value, source):
    return {"$value": value, "$type": "fontFamily" if "font" in source else "other", "$extensions": {"source": source}}


core = {
    "color": {
        "purple": {
            "500": color("tempo-colors-purple-500", "Tempo brand purple step used as the marketing signup fill"),
        },
        "neutralPurple": {
            "00": color("tempo-colors-neutralPurple-00"),
            "190": color("tempo-colors-neutralPurple-190"),
            "200": color("tempo-colors-neutralPurple-200"),
        },
    },
    "fontFamily": {
        "body": {
            "$value": "Inter, Arial, sans-serif",
            "$type": "fontFamily",
            "$extensions": {"source": "css-var --tempo-fonts-body"},
        },
        "heading": {
            "$value": "Deezer Product, Tahoma, Arial, sans-serif",
            "$type": "fontFamily",
            "$extensions": {"source": "css-var --tempo-fonts-heading"},
        },
        "headline": {
            "$value": "Deezer Headline VF, Tahoma, Arial, sans-serif",
            "$type": "fontFamily",
            "$extensions": {"source": "css-var --tempo-fonts-headline"},
            "$description": "Condensed display face on the player shell titles",
        },
        "brand": {
            "$value": "Deezer Brand, Tahoma, sans-serif",
            "$type": "fontFamily",
            "$extensions": {"source": "computed h1 font-family on https://www.deezer.com/en/"},
            "$description": "Marketing homepage display face. Not a Tempo custom property.",
        },
        "mono": {
            "$value": "SFMono-Regular, Menlo, Monaco, Consolas, Liberation Mono, Courier New, monospace",
            "$type": "fontFamily",
            "$extensions": {"source": "css-var --tempo-fonts-mono"},
        },
    },
    "fontWeight": {
        "regular": {"$value": 400, "$type": "fontWeight", "$extensions": {"source": "css-var --tempo-fontWeights-normal"}},
        "medium": {"$value": 500, "$type": "fontWeight", "$extensions": {"source": "css-var --tempo-fontWeights-medium"}},
        "semibold": {"$value": 600, "$type": "fontWeight", "$extensions": {"source": "css-var --tempo-fontWeights-semibold"}},
        "bold": {"$value": 700, "$type": "fontWeight", "$extensions": {"source": "css-var --tempo-fontWeights-bold"}},
        "extrabold": {"$value": 800, "$type": "fontWeight", "$extensions": {"source": "css-var --tempo-fontWeights-extrabold"}},
        "black": {"$value": 900, "$type": "fontWeight", "$extensions": {"source": "css-var --tempo-fontWeights-black"}},
    },
    "fontSize": {
        "caption": dim(var("tempo-fontSizes-caption-regular"), "css-var --tempo-fontSizes-caption-regular"),
        "bodyS": dim(var("tempo-fontSizes-body-s"), "css-var --tempo-fontSizes-body-s"),
        "bodyM": dim(var("tempo-fontSizes-body-m"), "css-var --tempo-fontSizes-body-m"),
        "bodyL": dim(var("tempo-fontSizes-body-l"), "css-var --tempo-fontSizes-body-l"),
        "headingS": dim(var("tempo-fontSizes-heading-s"), "css-var --tempo-fontSizes-heading-s"),
        "headingM": dim(var("tempo-fontSizes-heading-m"), "css-var --tempo-fontSizes-heading-m"),
        "headingL": dim(var("tempo-fontSizes-heading-l"), "css-var --tempo-fontSizes-heading-l"),
        "headingXl": dim(var("tempo-fontSizes-heading-xl"), "css-var --tempo-fontSizes-heading-xl"),
        "displayS": dim(var("tempo-fontSizes-display-s"), "css-var --tempo-fontSizes-display-s"),
        "titleScreenDesktop": dim(var("tempo-fontSizes-title-screen-desktop"), "css-var --tempo-fontSizes-title-screen-desktop"),
        "marketingHero": dim("140px", "computed h1 font-size on https://www.deezer.com/en/ at 1440px"),
    },
    "lineHeight": {
        "caption": dim(var("tempo-lineHeights-caption-regular"), "css-var --tempo-lineHeights-caption-regular"),
        "bodyS": dim(var("tempo-lineHeights-body-s"), "css-var --tempo-lineHeights-body-s"),
        "bodyL": dim(var("tempo-lineHeights-body-l"), "css-var --tempo-lineHeights-body-l"),
        "headingM": dim(var("tempo-lineHeights-heading-m"), "css-var --tempo-lineHeights-heading-m"),
        "headingL": dim(var("tempo-lineHeights-heading-l"), "css-var --tempo-lineHeights-heading-l"),
        "marketingHero": dim("126px", "computed h1 line-height on https://www.deezer.com/en/"),
    },
    "space": {
        "1": dim(var("tempo-space-1"), "css-var --tempo-space-1"),
        "2": dim(var("tempo-space-2"), "css-var --tempo-space-2"),
        "3": dim(var("tempo-space-3"), "css-var --tempo-space-3"),
        "4": dim(var("tempo-space-4"), "css-var --tempo-space-4"),
        "5": dim(var("tempo-space-5"), "css-var --tempo-space-5"),
    },
    "radius": {
        "none": dim(var("tempo-radii-none"), "css-var --tempo-radii-none"),
        "xs": dim(var("tempo-radii-2xs"), "css-var --tempo-radii-2xs"),
        "sm": dim(var("tempo-radii-sm"), "css-var --tempo-radii-sm"),
        "md": dim(var("tempo-radii-md"), "css-var --tempo-radii-md"),
        "lg": dim(var("tempo-radii-lg"), "css-var --tempo-radii-lg"),
        "xl": dim(var("tempo-radii-xl"), "css-var --tempo-radii-xl"),
        "2xl": dim(var("tempo-radii-2xl"), "css-var --tempo-radii-2xl"),
        "3xl": dim(var("tempo-radii-3xl"), "css-var --tempo-radii-3xl"),
        "full": dim(var("tempo-radii-full"), "css-var --tempo-radii-full"),
        "marketingButton": dim("12px", "computed border-radius of Sign up on https://www.deezer.com/en/"),
        "field": dim("16px", "computed border-radius of login email field and explore search"),
    },
    "borderWidth": {
        "s": dim(var("tempo-borderWidths-border-s"), "css-var --tempo-borderWidths-border-s"),
        "m": dim(var("tempo-borderWidths-border-m"), "css-var --tempo-borderWidths-border-m"),
    },
    "size": {
        "iconS": dim(var("tempo-sizes-icon-s"), "css-var --tempo-sizes-icon-s"),
        "iconM": dim(var("tempo-sizes-icon-m"), "css-var --tempo-sizes-icon-m"),
        "iconL": dim(var("tempo-sizes-icon-l"), "css-var --tempo-sizes-icon-l"),
        "controlS": dim("37px", "computed height of marketing Log in and Sign up"),
        "field": dim("48px", "computed height of login email field and explore search"),
        "loginSubmit": dim("48px", "computed height of login wall Log in button"),
    },
    "duration": {
        "ultraFast": {"$value": var("tempo-transition-duration-ultra-fast"), "$type": "duration", "$extensions": {"source": "css-var --tempo-transition-duration-ultra-fast"}},
        "fast": {"$value": var("tempo-transition-duration-fast"), "$type": "duration", "$extensions": {"source": "css-var --tempo-transition-duration-fast"}},
        "normal": {"$value": var("tempo-transition-duration-normal"), "$type": "duration", "$extensions": {"source": "css-var --tempo-transition-duration-normal"}},
        "slow": {"$value": var("tempo-transition-duration-slow"), "$type": "duration", "$extensions": {"source": "css-var --tempo-transition-duration-slow"}},
    },
    "easing": {
        "easeOut": {"$value": var("tempo-transition-easing-ease-out"), "$type": "cubicBezier", "$extensions": {"source": "css-var --tempo-transition-easing-ease-out"}},
        "easeInOut": {"$value": var("tempo-transition-easing-ease-in-out"), "$type": "cubicBezier", "$extensions": {"source": "css-var --tempo-transition-easing-ease-in-out"}},
    },
}

dark = {
    "background": {
        "page": color("tempo-colors-background-neutral-primary-default", "Player page, black"),
        "surface": color("tempo-colors-background-neutral-secondary-default", "Raised panels such as the sidebar and channel cards"),
        "raised": color("tempo-colors-background-neutral-tertiary-default", "Fields and search"),
        "accent": color("tempo-colors-background-accent-primary-default", "Primary button fill in the player and on the login wall"),
        "accentHover": color("tempo-colors-background-accent-primary-hovered"),
        "accentPressed": color("tempo-colors-background-accent-primary-pressed"),
        "accentDisabled": color("tempo-colors-background-accent-primary-disabled"),
        "inverse": color("tempo-colors-background-neutral-inverse-default"),
        "success": color("tempo-colors-background-feedback-success-default"),
        "warning": color("tempo-colors-background-feedback-warning-default"),
        "danger": color("tempo-colors-background-feedback-error-default"),
    },
    "text": {
        "primary": color("tempo-colors-text-neutral-primary-default"),
        "secondary": color("tempo-colors-text-neutral-secondary-default"),
        "disabled": color("tempo-colors-text-neutral-primary-disabled"),
        "onAccent": color("tempo-colors-text-accent-onAccent-default"),
        "link": color("tempo-colors-text-accent-primary-default"),
        "linkHover": color("tempo-colors-text-accent-primary-hovered"),
        "success": color("tempo-colors-text-feedback-success-default"),
        "warning": color("tempo-colors-text-feedback-warning-default"),
        "danger": color("tempo-colors-text-feedback-error-default"),
    },
    "border": {
        "default": color("tempo-colors-border-neutral-primary-default"),
        "strong": color("tempo-colors-border-neutral-primary-hovered"),
        "focus": color("tempo-colors-border-neutral-primary-focused"),
        "accent": color("tempo-colors-border-accent-primary-default"),
        "danger": color("tempo-colors-border-feedback-error-default"),
    },
    "icon": {
        "primary": color("tempo-colors-icon-neutral-primary-default"),
        "secondary": color("tempo-colors-icon-neutral-secondary-default"),
    },
}

# Marketing homepage is light. These are computed, not Tempo semantic tokens.
m = SAMPLES["marketing"]
light = {
    "background": {
        "page": {
            "$value": "#ffffff",
            "$type": "color",
            "$extensions": {"source": "observed page fill on https://www.deezer.com/en/; body computed background was transparent"},
            "$description": "Marketing page is white. The computed body background was transparent.",
        },
        "header": {
            "$value": "#000000",
            "$type": "color",
            "$extensions": {"source": "observed header bar on https://www.deezer.com/en/"},
        },
        "accent": {
            "$value": "#a238ff",
            "$type": "color",
            "$extensions": {"source": "computed Sign up background-color rgb(162, 56, 255) on https://www.deezer.com/en/"},
            "$description": "Marketing purple. Darker than the player accent #ad47ff.",
        },
        "inkButton": {
            "$value": "#121216",
            "$type": "color",
            "$extensions": {"source": "computed Try for free background-color rgb(18, 18, 22)"},
        },
    },
    "text": {
        "primary": {
            "$value": "#0f0d13",
            "$type": "color",
            "$extensions": {"source": "computed h1 color rgb(15, 13, 19) on https://www.deezer.com/en/"},
        },
        "onHeader": {
            "$value": "#fdfcfe",
            "$type": "color",
            "$extensions": {"source": "computed Plans link color rgb(253, 252, 254)"},
        },
        "onAccent": {
            "$value": "#ffffff",
            "$type": "color",
            "$extensions": {"source": "computed Sign up color rgb(255, 255, 255)"},
        },
    },
    "border": {
        "login": {
            "$value": "#555257",
            "$type": "color",
            "$extensions": {"source": "computed Log in border-top-color rgb(85, 82, 87)"},
        },
    },
}

doc = {
    "core": core,
    "dark": dark,
    "light": light,
    "$themes": [
        {"id": "dark", "name": "Dark", "selectedTokenSets": {"core": "source", "dark": "enabled"}},
        {"id": "light", "name": "Light", "selectedTokenSets": {"core": "source", "light": "enabled"}},
    ],
    "$metadata": {
        "tokenSetOrder": ["core", "dark", "light"],
    },
}

# cubic bezier must be a list for some checkers; keep the CSS string and also a parsed list
for key, token in core["easing"].items():
    raw = token["$value"]
    if isinstance(raw, str) and raw.startswith("cubic-bezier"):
        nums = [float(x) for x in raw[raw.find("(") + 1:raw.find(")")].split(",")]
        token["$value"] = nums

out = HERE / "tokens.json"
out.write_text(json.dumps(doc, indent=2) + "\n")
print("wrote", out, "dark colours", sum(1 for g in dark.values() for _ in g))
