#!/usr/bin/env python3
"""Build tokens.json from measured public-site readings.

Hand-adapted for the public Capy marketing site. Values come from
raw/css-vars.json and raw/home-measured.json, read on https://capy.ai/
on 2026-11-22. Auth colours are the computed oklch values converted to
hex. Nothing is recalled from memory of the product.
"""
import json
import pathlib

ADAPTED_FOR = "capy"

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"


def color(value, source):
    return {
        "$type": "color",
        "$value": value,
        "$extensions": {"source": source},
    }


def dim(value, source):
    return {
        "$type": "dimension",
        "$value": value,
        "$extensions": {"source": source},
    }


def font(value, source):
    return {
        "$type": "fontFamily",
        "$value": value,
        "$extensions": {"source": source},
    }


def number(value, source):
    return {
        "$type": "number",
        "$value": value,
        "$extensions": {"source": source},
    }


def shadow(value, source):
    return {
        "$type": "shadow",
        "$value": value,
        "$extensions": {"source": source},
    }


def cubic(value, source):
    return {
        "$type": "cubicBezier",
        "$value": value,
        "$extensions": {"source": source},
    }


HOME = "Computed style on https://capy.ai/ at 1440 by 900 on 2026-11-22. raw/home-measured.json."
VAR = "Computed custom property on https://capy.ai/ at 1440 by 900 on 2026-11-22. raw/css-vars.json."
AUTH = "Computed style on https://capy.ai/sign-in, prefers-color-scheme dark, 2026-11-22. oklch converted to hex."
AUTH_LIGHT = "Computed style on https://capy.ai/sign-in, prefers-color-scheme light, 2026-11-22. oklch converted to hex."
PRICE = "Computed style on https://capy.ai/pricing at 1440 by 900 on 2026-11-22. raw/pricing-measured.json."

doc = {
    "$description": "Public Capy marketing tokens, measured 2026-11-22. catalog.json was not updated.",
    "core": {
        "font": {
            "family": {
                "display": font(
                    "bebasNeue Inline, bebasNeue, bebasNeue Fallback DIN, Impact, sans-serif",
                    HOME + " h1 fontFamily.",
                ),
                "body": font(
                    "abcSocialMono, abcSocialMono Fallback Menlo, Consolas, Courier, monospace",
                    HOME + " body and button fontFamily. --font-sans.",
                ),
                "menu": font(
                    "DM Mono, Menlo, Consolas, Courier New, monospace",
                    "Computed fontFamily on the open Product menu link, 2026-11-22.",
                ),
                "auth": font(
                    "Inter, ui-sans-serif, system-ui, sans-serif",
                    AUTH + " heading and button fontFamily.",
                ),
            }
        },
        "typography": {
            "display": {
                "$type": "typography",
                "$value": {
                    "fontFamily": "{font.family.display}",
                    "fontSize": "64px",
                    "fontWeight": 400,
                    "lineHeight": "64px",
                    "letterSpacing": "-0.704px",
                },
                "$extensions": {"source": HOME + " h1."},
            },
            "pricingTitle": {
                "$type": "typography",
                "$value": {
                    "fontFamily": "{font.family.display}",
                    "fontSize": "56px",
                    "fontWeight": 400,
                    "lineHeight": "38px",
                },
                "$extensions": {"source": PRICE + " h1."},
            },
            "price": {
                "$type": "typography",
                "$value": {
                    "fontFamily": "{font.family.display}",
                    "fontSize": "56px",
                    "fontWeight": 400,
                    "lineHeight": "50px",
                },
                "$extensions": {"source": PRICE + " $0."},
            },
            "body": {
                "$type": "typography",
                "$value": {
                    "fontFamily": "{font.family.body}",
                    "fontSize": "18px",
                    "fontWeight": 400,
                    "lineHeight": "25.2px",
                },
                "$extensions": {"source": HOME + " hero paragraph."},
            },
            "ui": {
                "$type": "typography",
                "$value": {
                    "fontFamily": "{font.family.body}",
                    "fontSize": "16px",
                    "fontWeight": 400,
                    "lineHeight": "24px",
                },
                "$extensions": {"source": HOME + " Download button."},
            },
            "menuItem": {
                "$type": "typography",
                "$value": {
                    "fontFamily": "{font.family.menu}",
                    "fontSize": "18px",
                    "fontWeight": 400,
                    "lineHeight": "25px",
                },
                "$extensions": {"source": "Product menu link, 2026-11-22."},
            },
            "authHeading": {
                "$type": "typography",
                "$value": {
                    "fontFamily": "{font.family.auth}",
                    "fontSize": "22px",
                    "fontWeight": 500,
                    "lineHeight": "26.4px",
                },
                "$extensions": {"source": AUTH + " h1."},
            },
            "authControl": {
                "$type": "typography",
                "$value": {
                    "fontFamily": "{font.family.auth}",
                    "fontSize": "13px",
                    "fontWeight": 500,
                    "lineHeight": "16.25px",
                },
                "$extensions": {"source": AUTH + " Continue button."},
            },
        },
        "radius": {
            "xs": dim("0.125rem", VAR + " --radius-xs."),
            "sm": dim("0.25rem", VAR + " --radius-sm."),
            "md": dim("0.375rem", VAR + " --radius-md."),
            "lg": dim("0.5rem", VAR + " --radius-lg."),
            "xl": dim("0.75rem", VAR + " --radius-xl."),
            "2xl": dim("1rem", VAR + " --radius-2xl."),
            "3xl": dim("1.5rem", VAR + " --radius-3xl."),
            "control": dim("8px", HOME + " Download button borderRadius."),
            "auth": dim("6px", AUTH + " Continue and email field borderRadius."),
            "pill": dim("999px", PRICE + " Monthly toggle borderRadius was a full pill."),
        },
        "size": {
            "header": dim("65px", HOME + " header height. --header-height is 4rem."),
            "headerButton": dim("36px", HOME + " header Download height."),
            "heroButton": dim("35px", HOME + " hero Download height."),
            "pricingButton": dim("40px", PRICE + " Start free height."),
            "authControl": dim("32px", AUTH + " Continue and email field height."),
            "menuButton": dim("24px", "Phone header menu button, 24 by 24, measured at 390."),
        },
        "shadow": {
            "offsetGray": shadow(
                [{"color": "#888888", "offsetX": "-2px", "offsetY": "2px", "blur": "0px", "spread": "0px"}],
                HOME + " hero Download box-shadow hard offset.",
            ),
            "offsetInk": shadow(
                [{"color": "#000000", "offsetX": "-2px", "offsetY": "2px", "blur": "0px", "spread": "0px"}],
                HOME + " Continue in web box-shadow hard offset.",
            ),
        },
        "motion": {
            "easeOutQuart": cubic([0.165, 0.84, 0.44, 1], VAR + " --ease-out-quart."),
            "navDuration": dim("150ms", "Product trigger class duration-150, read from the class name on the live button."),
        },
        "layout": {
            "desktop": dim("1440px", "Requested and measured innerWidth on the desktop captures."),
            "phone": dim("390px", "Requested and measured innerWidth on the phone captures."),
            "desktopHeight": dim("900px", "Measured innerHeight on the desktop captures."),
            "phoneHeight": dim("844px", "Measured innerHeight on the phone captures. PNG height is 1688 at devicePixelRatio 2."),
        },
    },
    "light": {
        "color": {
            "page": color("#ffffff", HOME + " body backgroundColor."),
            "ink": color("#000000", HOME + " body and h1 color."),
            "header": color("#000000", HOME + " header backgroundColor."),
            "onHeader": color("#ffffff", HOME + " Sign in color."),
            "headerButton": color("#ffffff", HOME + " header Download background."),
            "headerButtonText": color("#000000", HOME + " header Download color."),
            "primary": color("#000000", HOME + " hero Download background."),
            "onPrimary": color("#ffffff", HOME + " hero Download color."),
            "secondary": color("#ffffff", HOME + " Continue in web background."),
            "onSecondary": color("#000000", HOME + " Continue in web color."),
            "offset": color("#888888", HOME + " hero Download shadow color."),
            "muted": color("#6d6d6d", VAR + " --color-black-500."),
            "mutedStrong": color("#3d3d3d", VAR + " --color-black-900."),
            "surface": color("#f6f6f6", VAR + " --color-black-50."),
            "line": color("#e7e7e7", VAR + " --color-black-100."),
            "accent": color("#7699fb", VAR + " --color-primary."),
            "accentDark": color("#2a44af", VAR + " --color-primary-dark. --color-link is the same."),
            "link": color("#2a44af", VAR + " --color-link. Current nav item paints this blue."),
            "orange": color("#ff4512", VAR + " --color-orange-red."),
            "yuzu": color("#ebc04b", VAR + " --color-yuzu-yellow-400."),
            "focus": color("#e59700", "Product menu focus outline rgb(229, 151, 0) auto 1px, offset 1px, 2026-11-22."),
            "menuText": color("#4f4f4f", "Product menu link color rgb(79, 79, 79)."),
            "authPage": color("#f4f4f5", AUTH_LIGHT + " html background oklch(0.962 0.0025 290)."),
            "authAccent": color("#4c6fff", "Continue button on the light sign-in wall. Sampled as the painted blue; the dark-scheme reading was oklch(0.58 0.213 267.8)."),
            "authOnAccent": color("#ffffff", AUTH + " Continue color oklch(1 0 0)."),
        }
    },
    "dark": {
        "color": {
            "page": color("#121214", AUTH + " html background oklch(0.1403 0.0022 286.1)."),
            "text": color("#efefef", AUTH + " h1 color oklch(0.9404 0.0013 286.4)."),
            "field": color("#1c1c1e", AUTH + " email background oklch(0.2182 0.0019 286.2)."),
            "ghost": color("#1a1a1b", AUTH + " Google button background color(srgb 0.102836 0.10285 0.106458)."),
            "accent": color("#4d6fe8", AUTH + " Continue background oklch(0.58 0.213 267.8)."),
            "onAccent": color("#ffffff", AUTH + " Continue color."),
            "border": color("#ffffff1f", AUTH + " field border oklch(1 0 0 / 0.12)."),
        }
    },
    "$themes": [
        {"id": "light", "name": "light", "selectedTokenSets": {"core": "source", "light": "enabled"}},
        {"id": "dark", "name": "dark", "selectedTokenSets": {"core": "source", "dark": "enabled"}},
    ],
}

# Fill $type on composite typography groups so DTCG readers accept them.
out = HERE / "tokens.json"
out.write_text(json.dumps(doc, indent=2) + "\n")
print("wrote", out)
