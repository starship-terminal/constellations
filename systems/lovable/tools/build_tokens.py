#!/usr/bin/env python3
"""Build tokens.json from raw/css-vars.json.

lovable.dev declares a named token layer (--bg-*, --fg-*, --border-*,
--shadow-*, --text-*-lmk, --radius-*-lmk, --font-*) and resolves it under
html.light and html.dark. Public marketing paints light. /enterprise-form
paints dark. Docs (docs.lovable.dev) is a separate host and is not in this
token file.

Every token carries $extensions.source. Deterministic.
"""
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent.parent
V = json.loads((HERE / "raw" / "css-vars.json").read_text())
LIGHT = V["resolved"]["light"]
DARK = V["resolved"]["dark"]

ROLES = [
    "page", "surface", "raised", "overlay", "scrim",
    "text", "textSecondary", "textDisabled", "textOnAccent", "link",
    "border", "borderStrong", "focus",
    "accent", "accentHover", "accentPressed",
    "success", "warning", "danger", "info",
]

# role -> css variable. Same names in both themes; values differ.
ROLE_VARS = {
    "page": "--bg-base",
    "surface": "--bg-secondary",
    "raised": "--bg-primary",
    "overlay": "--bg-translucent",
    "scrim": "--bg-scrim",
    "text": "--fg-primary",
    "textSecondary": "--fg-secondary",
    "textDisabled": "--fg-quaternary",
    "textOnAccent": "--fg-inverse",
    "link": "--fg-accent",
    "border": "--border-base",
    "borderStrong": "--border-primary",
    "focus": "--border-focus",
    "accent": "--bg-accent",
    "accentHover": "--glow-accent-hover",
    "accentPressed": "--glow-accent-pressed",
    "success": "--bg-positive",
    "warning": "--bg-attention",
    "danger": "--bg-destructive",
    "info": "--bg-special",
}


def val(theme, name):
    box = (LIGHT if theme == "light" else DARK).get(name) or {}
    v = box.get("value", box.get("raw"))
    if v in (None, ""):
        raise KeyError(f"{theme} {name} was not resolved")
    return v


def color_token(theme, name):
    return {
        "$value": val(theme, name),
        "$type": "color",
        "$extensions": {"source": f"css-var {name} resolved on html.{theme}"},
    }


def dim_token(name, source):
    v = val("light", name)
    if isinstance(v, (int, float)):
        v = f"{v:g}px"
    return {
        "$value": v,
        "$type": "dimension",
        "$extensions": {"source": source},
    }


def theme_set(theme):
    out = {}
    for role, name in ROLE_VARS.items():
        out[role] = color_token(theme, name)
    # Extra paints the product names and the public surface uses.
    extras = {
        "inverse": "--bg-inverse",
        "accentForeground": "--fg-on-attention",
        "destructiveForeground": "--fg-destructive",
        "positive": "--bg-positive",
        "attention": "--bg-attention",
        "special": "--bg-special",
        "muted": "--bg-muted",
        "depth": "--bg-depth",
    }
    for role, name in extras.items():
        if name in (LIGHT if theme == "light" else DARK):
            out[role] = color_token(theme, name)
    return out


def core():
    c = {"color": {}, "fontFamily": {}, "fontWeight": {}, "typography": {}, "radius": {}, "space": {}, "elevation": {}, "duration": {}, "easing": {}, "layout": {}}
    # A short named palette, light values. These are brand constants the dark
    # theme does not invert (accent, destructive, positive, attention).
    palette = {
        "accent": "--bg-accent",
        "destructive": "--bg-destructive",
        "positive": "--bg-positive",
        "attention": "--bg-attention",
        "special": "--bg-special",
        "highlight": "--bg-highlight",
        "focus": "--border-focus",
        "marketingAccent": "--marketing-accent-primary",
    }
    for key, name in palette.items():
        c["color"][key] = color_token("light", name)
        c["color"][key]["$extensions"]["source"] += "; constant paint, same hex in the light capture"

    c["fontFamily"]["sans"] = {
        "$value": val("light", "--font-sans"),
        "$type": "fontFamily",
        "$extensions": {"source": "css-var --font-sans on html.light; @font-face Camera Plain Variable is in the bundle, files not committed"},
    }
    c["fontFamily"]["mono"] = {
        "$value": val("light", "--font-mono"),
        "$type": "fontFamily",
        "$extensions": {"source": "css-var --font-mono on html.light; Roboto Mono Variable @font-face, files not committed"},
    }
    c["fontFamily"]["serif"] = {
        "$value": val("light", "--font-serif"),
        "$type": "fontFamily",
        "$extensions": {"source": "css-var --font-serif on html.light; a system serif stack, not a webfont"},
    }
    for key, name, num in (
        ("normal", "--font-weight-normal", 400),
        ("medium", "--font-weight-medium", 480),
        ("semibold", "--font-weight-semibold", 600),
    ):
        c["fontWeight"][key] = {
            "$value": num,
            "$type": "fontWeight",
            "$extensions": {"source": f"css-var {name} resolved to {val('light', name)}"},
        }

    type_roles = {
        "display": "--text-heading-lg-lmk",
        "heading": "--text-heading-md-lmk",
        "title": "--text-title-lmk",
        "label": "--text-label-lmk",
        "body": "--text-ui-lmk",
        "caption": "--text-ui-sm-lmk",
    }
    for role, name in type_roles.items():
        size = val("light", name)
        lh = val("light", name + "--line-height")
        ls = val("light", name + "--letter-spacing")
        fw = val("light", name + "--font-weight")
        c["typography"][role] = {
            "$value": {
                "fontFamily": "{core.fontFamily.sans}",
                "fontSize": size if isinstance(size, str) else f"{size:g}px",
                "fontWeight": int(float(fw)) if not isinstance(fw, int) else fw,
                "lineHeight": lh if isinstance(lh, (int, float)) else lh,
                "letterSpacing": ls if isinstance(ls, str) else f"{ls:g}px",
            },
            "$type": "typography",
            "$extensions": {"source": f"css-var {name} and its --line-height/--letter-spacing/--font-weight companions"},
        }

    for key, name in (
        ("trigger", "--radius-trigger-lmk"),
        ("menu", "--radius-menu-lmk"),
        ("menuItem", "--radius-menu-item-lmk"),
        ("menuLink", "--radius-menu-link-lmk"),
        ("menuCard", "--radius-menu-card-lmk"),
        ("menuBlock", "--radius-menu-block-lmk"),
        ("focus", "--radius-focus-lmk"),
    ):
        c["radius"][key] = dim_token(name, f"css-var {name}")

    c["space"]["unit"] = {
        "$value": "4px",
        "$type": "dimension",
        "$extensions": {"source": "css-var --spacing is .25rem, which computes to 4px at the default root size"},
    }
    c["border"] = {
        "default": {
            "$value": val("light", "--border-default") if isinstance(val("light", "--border-default"), str) else f"{val('light', '--border-default'):g}px",
            "$type": "dimension",
            "$extensions": {"source": "css-var --border-default"},
        }
    }
    # One elevation sample. The full shadow strings are long computed values.
    shadow = val("light", "--shadow-surface-xxs")
    c["elevation"]["surfaceXxs"] = {
        "$value": shadow if isinstance(shadow, str) else str(shadow),
        "$type": "other",
        "$extensions": {"source": "css-var --shadow-surface-xxs computed box-shadow on html.light"},
    }
    c["duration"]["default"] = {
        "$value": "150ms",
        "$type": "duration",
        "$extensions": {"source": "css-var --default-transition-duration is .15s"},
    }
    c["easing"]["default"] = {
        "$value": [0.4, 0, 0.2, 1],
        "$type": "cubicBezier",
        "$extensions": {"source": "css-var --default-transition-timing-function cubic-bezier(.4, 0, .2, 1)"},
    }
    c["layout"]["desktop"] = {
        "$value": "1440px",
        "$type": "dimension",
        "$extensions": {"source": "measured viewport width of the desktop captures"},
    }
    c["layout"]["phone"] = {
        "$value": "390px",
        "$type": "dimension",
        "$extensions": {"source": "measured viewport width of the phone captures"},
    }
    c["layout"]["header"] = {
        "$value": "56px",
        "$type": "dimension",
        "$extensions": {"source": "measured header height on https://lovable.dev/ at 1440"},
    }
    return c


def check_color(v):
    if isinstance(v, str) and (v.startswith("#") or v.startswith("rgb") or v.startswith("okl")):
        return
    raise ValueError(f"not a colour: {v!r}")


tokens = {
    "core": core(),
    "light": theme_set("light"),
    "dark": theme_set("dark"),
    "$themes": [
        {"id": "light", "name": "Light", "selectedTokenSets": {"core": "source", "light": "enabled"},
         "$description": "Painted on the public marketing routes (html.light)."},
        {"id": "dark", "name": "Dark", "selectedTokenSets": {"core": "source", "dark": "enabled"},
         "$description": "Declared as html.dark and painted on /enterprise-form. Marketing routes stay light."},
    ],
    "$metadata": {"tokenSetOrder": ["core", "light", "dark"]},
}

for theme in ("light", "dark"):
    for role, leaf in tokens[theme].items():
        check_color(leaf["$value"])

(HERE / "tokens.json").write_text(json.dumps(tokens, indent=2, ensure_ascii=False) + "\n")
print("wrote tokens", {k: len(v) if isinstance(v, dict) else 0 for k, v in tokens.items()})
