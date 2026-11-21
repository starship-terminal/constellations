#!/usr/bin/env python3
"""Write raw/component-tokens.json, the token spec build_tokens.py reads.

factory.com declares on :root (raw/css-vars.json, tools/capture/vars.mjs):

  brand paints      --accent-100..300, --dark-base-*, --light-base-*,
                    --surface-page/raised/sunken, --neutral-100..1000
                    -> core.color.* (constants; same in both themes)
  role aliases      --color-background, --color-foreground, --color-base-*,
                    --color-surface-raised, --color-accent-*, --color-*-base-*
                    These invert under [data-theme="light"] versus the theme
                    layer default. They become light.* and dark.*.
  scales            --radius*, --spacing, --text-*, --font-weight-*,
                    --tracking-*, --ease-*, --default-transition-duration,
                    --content-column, --content-gutter
                    -> core.*
  measured          control heights, paddings and the painted CTA colours
                    read from getComputedStyle on the live home page
                    -> light.component.*

A leaf is {"var": "--name"} (resolved by build_tokens.py) or {"value": ...,
"source": "..."} for a measured value.
"""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"


def var(name, ty):
    return {"var": name, "type": ty}


def val(value, ty, source):
    return {"value": value, "type": ty, "source": source}


SPEC = {
    "_about": (
        "Token tree for factory.com, read 2026-11-21. Brand paints and scales "
        "are :root custom properties. Role colours invert between the painted "
        "light theme and the theme-layer dark default. Component leaves are "
        "computed styles on the live home page."
    ),
    "core": {
        "color": {
            "accent": {
                "100": var("--accent-100", "color"),
                "200": var("--accent-200", "color"),
                "300": var("--accent-300", "color"),
            },
            "base": {
                "darkPrimary": var("--dark-base-primary", "color"),
                "darkSecondary": var("--dark-base-secondary", "color"),
                "lightPrimary": var("--light-base-primary", "color"),
                "lightSecondary": var("--light-base-secondary", "color"),
            },
            "surface": {
                "page": var("--surface-page", "color"),
                "raised": var("--surface-raised", "color"),
                "sunken": var("--surface-sunken", "color"),
            },
            "neutral": {
                "100": var("--neutral-100", "color"),
                "200": var("--neutral-200", "color"),
                "300": var("--neutral-300", "color"),
                "400": var("--neutral-400", "color"),
                "500": var("--neutral-500", "color"),
                "600": var("--neutral-600", "color"),
                "700": var("--neutral-700", "color"),
                "800": var("--neutral-800", "color"),
                "900": var("--neutral-900", "color"),
                "1000": var("--neutral-1000", "color"),
            },
            "black": var("--color-black", "color"),
            "white": var("--color-white", "color"),
        },
        "radius": {
            "xs": var("--radius-xs", "dimension"),
            "sm": var("--radius-sm", "dimension"),
            "md": var("--radius-md", "dimension"),
            "lg": var("--radius-lg", "dimension"),
            "xl": var("--radius-xl", "dimension"),
            "2xl": var("--radius-2xl", "dimension"),
            "3xl": var("--radius-3xl", "dimension"),
            "default": var("--radius", "dimension"),
        },
        "space": {
            "unit": var("--spacing", "dimension"),
            "1": val("4px", "dimension", "derived: 1 x --spacing (4px), factory.com :root"),
            "2": val("8px", "dimension", "derived: 2 x --spacing"),
            "3": val("12px", "dimension", "derived: 3 x --spacing"),
            "4": val("16px", "dimension", "derived: 4 x --spacing"),
            "5": val("20px", "dimension", "derived: 5 x --spacing"),
            "6": val("24px", "dimension", "derived: 6 x --spacing"),
            "8": val("32px", "dimension", "derived: 8 x --spacing"),
            "9": val("36px", "dimension", "derived: --content-gutter at min-width 64rem, resolved 36px"),
        },
        "fontWeight": {
            "light": var("--font-weight-light", "fontWeight"),
            "regular": var("--font-weight-normal", "fontWeight"),
            "medium": var("--font-weight-medium", "fontWeight"),
            "semibold": var("--font-weight-semibold", "fontWeight"),
            "bold": var("--font-weight-bold", "fontWeight"),
        },
        "fontFamily": {
            "sans": val(
                'Geist, "Geist Fallback", sans-serif',
                "fontFamily",
                "measured: getComputedStyle(body).fontFamily on factory.com home, 2026-11-21. --font-sans aliases --font-geist-sans, which is set by next/font and did not resolve on the probe.",
            ),
            "pixel": var("--font-pixel", "fontFamily"),
            "mono": val(
                "ui-monospace, monospace",
                "fontFamily",
                "declared fallback of --font-pixel and --default-mono-font-family. --font-geist-mono did not resolve on the probe. Not captured as a loaded face.",
            ),
        },
        "typography": {
            "display": {
                "type": "typography",
                "value": {
                    "fontFamily": "{fontFamily.sans}",
                    "fontSize": "60.48px",
                    "fontWeight": "{fontWeight.medium}",
                    "lineHeight": "60.48px",
                    "letterSpacing": "-2.4192px",
                },
                "source": "measured: h1 on factory.com home, 1440px, 2026-11-21. text-transform uppercase.",
            },
            "body": {
                "type": "typography",
                "value": {
                    "fontFamily": "{fontFamily.sans}",
                    "fontSize": "{text.base}",
                    "fontWeight": "{fontWeight.regular}",
                    "lineHeight": "24px",
                },
                "source": "measured: body on factory.com home. Size aliases --text-base (16px).",
            },
            "nav": {
                "type": "typography",
                "value": {
                    "fontFamily": "{fontFamily.sans}",
                    "fontSize": "12px",
                    "fontWeight": "{fontWeight.regular}",
                    "lineHeight": "12px",
                },
                "source": "measured: header Pricing link on factory.com home.",
            },
            "button": {
                "type": "typography",
                "value": {
                    "fontFamily": "{fontFamily.sans}",
                    "fontSize": "{text.base}",
                    "fontWeight": "{fontWeight.regular}",
                    "lineHeight": "24px",
                },
                "source": "measured: DOWNLOAD FOR MAC and BOOK DEMO on factory.com home.",
            },
        },
        "text": {
            "xs": var("--text-xs", "dimension"),
            "sm": var("--text-sm", "dimension"),
            "base": var("--text-base", "dimension"),
            "lg": var("--text-lg", "dimension"),
            "xl": var("--text-xl", "dimension"),
            "2xl": var("--text-2xl", "dimension"),
            "3xl": var("--text-3xl", "dimension"),
            "4xl": var("--text-4xl", "dimension"),
            "5xl": var("--text-5xl", "dimension"),
            "7xl": var("--text-7xl", "dimension"),
            "8xl": var("--text-8xl", "dimension"),
        },
        "duration": {
            "default": val("150ms", "duration", "derived: --default-transition-duration .15s on :root @layer theme"),
        },
        "easing": {
            "standard": var("--default-transition-timing-function", "cubicBezier"),
            "inOut": var("--ease-in-out", "cubicBezier"),
            "out": var("--ease-out", "cubicBezier"),
        },
        "layout": {
            "contentColumn": var("--content-column", "dimension"),
            "contentGutter": var("--content-gutter", "dimension"),
            "breakpoint3xl": val("1920px", "dimension", "derived: --breakpoint-3xl 120rem at 16px root"),
        },
    },
}

ROLES = {
    "background": "--color-background",
    "foreground": "--color-foreground",
    "surfaceRaised": "--color-surface-raised",
    "darkBasePrimary": "--color-dark-base-primary",
    "darkBaseSecondary": "--color-dark-base-secondary",
    "lightBasePrimary": "--color-light-base-primary",
    "lightBaseSecondary": "--color-light-base-secondary",
    "accent": "--color-accent-100",
    "accentHover": "--color-accent-200",
    "accentPressed": "--color-accent-300",
    "base": {
        "100": "--color-base-100",
        "200": "--color-base-200",
        "300": "--color-base-300",
        "400": "--color-base-400",
        "500": "--color-base-500",
        "600": "--color-base-600",
        "700": "--color-base-700",
        "800": "--color-base-800",
        "900": "--color-base-900",
        "1000": "--color-base-1000",
    },
}


def roles():
    out = {}
    for key, name in ROLES.items():
        if isinstance(name, dict):
            out[key] = {k: var(v, "color") for k, v in name.items()}
        else:
            out[key] = var(name, "color")
    return out


COMPONENT = {
    "control": {
        "heightCta": val("31px", "dimension", "measured: DOWNLOAD FOR MAC and BOOK DEMO bounding box on factory.com home, 1440px"),
        "radiusCta": val("3px", "dimension", "measured: BOOK DEMO border-radius. Primary split button uses 3px 0 0 3px on the label half."),
        "padXCta": val("14px", "dimension", "measured: padding-inline on DOWNLOAD FOR MAC and BOOK DEMO"),
        "heightNavLink": val("12px", "dimension", "measured: header Pricing link height"),
        "navSize": val("12px", "dimension", "measured: header Pricing link font-size"),
        "focusOutline": val("1px", "dimension", "measured: DOWNLOAD FOR MAC :focus-visible outline-width, outline-offset 4px, colour rgb(16, 16, 16)"),
        "focusOffset": val("4px", "dimension", "measured: DOWNLOAD FOR MAC :focus-visible outline-offset"),
    },
    "button": {
        "primaryBg": val("#101010", "color", "measured: DOWNLOAD FOR MAC background rgb(16, 16, 16), which is --dark-base-secondary"),
        "primaryText": val("#f9f9f9", "color", "measured: painted text child of DOWNLOAD FOR MAC, rgb(249, 249, 249), which is --surface-page"),
        "primaryHoverBg": val("#f9f9f9", "color", "measured: DOWNLOAD FOR MAC :hover background rgb(249, 249, 249)"),
        "primaryHoverText": val("#101010", "color", "measured: DOWNLOAD FOR MAC :hover text rgb(16, 16, 16)"),
        "secondaryBg": val("#f9f9f9", "color", "measured: BOOK DEMO background"),
        "secondaryText": val("#020202", "color", "measured: BOOK DEMO text rgb(2, 2, 2)"),
        "secondaryBorder": val("#a49d9a", "color", "measured: BOOK DEMO border-top-color rgb(164, 157, 154), which is --neutral-400"),
        "secondaryHoverBorder": val("#8a8380", "color", "measured: DOWNLOAD FOR MAC :hover border rgb(138, 131, 128), which is --neutral-500"),
    },
}

SPEC["light"] = roles()
SPEC["dark"] = roles()
SPEC["component"] = COMPONENT

(RAW / "component-tokens.json").write_text(json.dumps(SPEC, indent=1) + "\n")
print("wrote", RAW / "component-tokens.json")
