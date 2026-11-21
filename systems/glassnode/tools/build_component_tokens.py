#!/usr/bin/env python3
"""Write raw/component-tokens.json from css-vars.json and components-computed.json.

Studio paints Ant Design tokens on a theme holder (not :root). Marketing
headings use fraktion and Inter, read as computed styles. One light theme.
"""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
V = json.loads((RAW / "css-vars.json").read_text())
C = json.loads((RAW / "components-computed.json").read_text())["components"]
H = V["resolved"]["holder"]
M = V["computed"]["marketing"]["samples"]


def var(name, ty="color"):
    if name not in H:
        raise KeyError(name)
    return {"var": name, "type": ty}


def measured(value, source, ty):
    return {"value": value, "type": ty, "source": source}


def comp(name, state, prop, ty):
    row = C[name][state]
    return measured(row[prop], f"measured {name} {state} {prop}", ty)


SPEC = {
    "_about": "Token tree for Glassnode public capture, 2026-11-21. Studio roles are Ant Design custom properties resolved on the theme holder at studio.glassnode.com. Marketing display type is a computed style on glassnode.com h1. One light theme.",
    "core": {
        "color": {
            "primary": var("--ant-color-primary"),
            "primary-hover": var("--ant-color-primary-hover"),
            "primary-active": var("--ant-color-primary-active"),
            "info": var("--ant-color-info"),
            "success": var("--ant-color-success"),
            "warning": var("--ant-color-warning"),
            "error": var("--ant-color-error"),
            "link-marketing": measured(
                C["button-contact"]["default"]["color"],
                "measured button-contact default color (marketing link blue)",
                "color",
            ),
        },
        "font": {
            "family": {
                "ui": measured(
                    C["button-primary"]["default"]["fontFamily"],
                    "measured button-primary default fontFamily",
                    "fontFamily",
                ),
                "marketing": measured(
                    C["button-launch"]["default"]["fontFamily"],
                    "measured button-launch default fontFamily",
                    "fontFamily",
                ),
                "display": measured(
                    M["h1"]["fontFamily"],
                    "measured glassnode.com h1 fontFamily",
                    "fontFamily",
                ),
                "code": var("--ant-font-family-code", "fontFamily"),
                "auth": measured(
                    C["auth-email"]["default"]["fontFamily"],
                    "measured auth-email default fontFamily",
                    "fontFamily",
                ),
            },
            "size": {
                "body": var("--ant-font-size", "dimension"),
                "sm": var("--ant-font-size-sm", "dimension"),
                "lg": var("--ant-font-size-lg", "dimension"),
                "h1": var("--ant-font-size-heading-1", "dimension"),
                "h3": var("--ant-font-size-heading-3", "dimension"),
                "h4": var("--ant-font-size-heading-4", "dimension"),
                "h5": var("--ant-font-size-heading-5", "dimension"),
                "display": measured(M["h1"]["fontSize"], "measured glassnode.com h1 fontSize", "dimension"),
            },
            "weight": {
                "display": measured(int(M["h1"]["fontWeight"]), "measured glassnode.com h1 fontWeight", "fontWeight"),
                "ui": measured(int(C["button-primary"]["default"]["fontWeight"]), "measured button-primary default fontWeight", "fontWeight"),
            },
        },
        "radius": {
            "control": var("--ant-border-radius", "dimension"),
            "xs": var("--ant-border-radius-xs", "dimension"),
        },
        "border": {
            "width": var("--ant-line-width", "dimension"),
            "width-bold": var("--ant-line-width-bold", "dimension"),
            "width-focus": var("--ant-line-width-focus", "dimension"),
        },
        "size": {
            "control": var("--ant-control-height", "dimension"),
            "control-lg": var("--ant-control-height-lg", "dimension"),
            "control-sm": var("--ant-control-height-sm", "dimension"),
            "icon": var("--ant-font-size-icon", "dimension"),
        },
        "motion": {
            "fast": var("--ant-motion-duration-fast", "duration"),
            "mid": var("--ant-motion-duration-mid", "duration"),
            "slow": var("--ant-motion-duration-slow", "duration"),
            "ease-out": var("--ant-motion-ease-out", "cubicBezier"),
            "ease-in-out": var("--ant-motion-ease-in-out", "cubicBezier"),
        },
        "space": {
            "unit": var("--ant-size-unit", "dimension") if "--ant-size-unit" in H else measured("4px", "Not captured as a named scale; Ant size unit unread", "dimension"),
        },
    },
    "light": {
        "page": var("--ant-color-bg-base"),
        "surface": var("--ant-color-bg-container"),
        "raised": var("--ant-color-bg-elevated"),
        "layout": var("--ant-color-bg-layout"),
        "scrim": var("--ant-color-bg-mask"),
        "text": var("--ant-color-text"),
        "text-heading": var("--ant-color-text-heading"),
        "muted": var("--ant-color-text-secondary"),
        "disabled": var("--ant-color-text-disabled"),
        "on-accent": var("--ant-color-text-light-solid"),
        "link": var("--ant-color-link"),
        "border": var("--ant-color-border"),
        "border-strong": var("--ant-color-border-secondary"),
        "accent": var("--ant-color-primary"),
        "accent-hover": var("--ant-color-primary-hover"),
        "accent-pressed": var("--ant-color-primary-active"),
        "success": var("--ant-color-success"),
        "warning": var("--ant-color-warning"),
        "danger": var("--ant-color-error"),
        "info": var("--ant-color-info"),
        "focus-ring": measured("Not captured", "no focus-ring colour was readable as a stable token", "other"),
    },
    "component": {
        "button": {
            "primary-bg": measured(C["button-primary"]["default"]["backgroundColor"], "measured button-primary default backgroundColor", "color"),
            "primary-fg": measured(C["button-primary"]["default"]["color"], "measured button-primary default color", "color"),
            "primary-radius": measured(C["button-primary"]["default"]["borderRadius"], "measured button-primary default borderRadius", "dimension"),
            "primary-height": measured(C["button-primary"]["default"]["height"], "measured button-primary default height", "dimension"),
            "primary-font-size": measured(C["button-primary"]["default"]["fontSize"], "measured button-primary default fontSize", "dimension"),
            "login-fg": measured(C["button-login"]["default"]["color"], "measured button-login default color", "color"),
        },
        "field": {
            "search-bg": measured(C["search-field"]["default"]["backgroundColor"], "measured search-field default backgroundColor", "color"),
            "search-height": measured(C["search-field"]["default"]["height"], "measured search-field default height", "dimension"),
            "auth-height": measured(C["auth-email"]["default"]["height"], "measured auth-email default height", "dimension"),
        },
        "type": {
            "display-size": measured(M["h1"]["fontSize"], "measured glassnode.com h1 fontSize", "dimension"),
            "display-line-height": measured(M["h1"]["lineHeight"], "measured glassnode.com h1 lineHeight", "dimension"),
            "display-color": measured(M["h1"]["color"], "measured glassnode.com h1 color", "color"),
        },
    },
}

# drop the unread focus token rather than invent a value
del SPEC["light"]["focus-ring"]
if "--ant-size-unit" not in H:
    del SPEC["core"]["space"]

(RAW / "component-tokens.json").write_text(json.dumps(SPEC, indent=2) + "\n")
print("wrote component-tokens", sum(1 for _ in SPEC["core"]), "core groups")
