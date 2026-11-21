#!/usr/bin/env python3
"""Build systems/kraken/tokens.json from raw/css-vars.json.

Live public marketing uses .magic-light-theme. Dark tokens are declared on
.default-dark-theme, .magic-dark-theme in the same stylesheets and were not
switched on a public page, so the dark set is labelled Declared, not live.
"""
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = json.loads((HERE / "raw" / "css-vars.json").read_text())


def src(evidence, selector, name, note=None):
    o = {
        "evidence": evidence,
        "file": "raw/css-vars.json",
        "selector": selector,
        "property": name,
        "url": "https://www.kraken.com/",
        "captured": "2026-11-21",
    }
    if note:
        o["note"] = note
    return o


def color(value, evidence, selector, name, note=None):
    return {
        "$type": "color",
        "$value": value,
        "$extensions": {"source": src(evidence, selector, name, note)},
    }


def dim(value, evidence, selector, name, note=None):
    return {
        "$type": "dimension",
        "$value": value,
        "$extensions": {"source": src(evidence, selector, name, note)},
    }


def find(selector_has, name):
    for rule in RAW["rules"]:
        if selector_has in rule["selector"] and name in rule["props"]:
            return rule["props"][name], rule["selector"]
    return None, None


LIGHT_SEL = ".default-light-theme, .magic-light-theme"
DARK_SEL = ".default-dark-theme, .magic-dark-theme"
TYPE_SEL = ":root, .marketing-text-theme"
SHAPE_SEL = ".default-shape-theme, :root"
SPACE_SEL = ".default-spacing-theme, :root"

# Semantic colours the public light theme actually applies.
LIGHT_ROLES = {
    "page": "--colors-ds-semantic-surface-page",
    "surface": "--colors-ds-semantic-surface-raised",
    "canvas": "--colors-ds-semantic-surface-canvas",
    "overlay": "--colors-ds-semantic-surface-overlay",
    "sunken": "--colors-ds-semantic-surface-sunken",
    "hover": "--colors-ds-semantic-surface-hover",
    "selected": "--colors-ds-semantic-surface-selected",
    "scrim": "--colors-ds-semantic-overlay-scrim",
    "text": "--colors-ds-semantic-content-primary",
    "muted": "--colors-ds-semantic-content-neutral",
    "dimmed": "--colors-ds-semantic-content-dimmed",
    "disabled": "--colors-ds-semantic-content-disabled",
    "inverse": "--colors-ds-semantic-content-inverse",
    "link": "--colors-ds-semantic-content-brand",
    "accent": "--colors-ds-semantic-content-brand",
    "accentHover": "--colors-ds-semantic-action-primary-background-hover",
    "onAccent": "--colors-ds-semantic-action-primary-foreground",
    "border": "--colors-ds-semantic-border-default",
    "borderStrong": "--colors-ds-semantic-border-strong",
    "focus": "--colors-ds-semantic-focus-ring",
    "success": "--colors-ds-semantic-content-positive",
    "successFill": "--colors-ds-semantic-status-positive-solid",
    "successSubtle": "--colors-ds-semantic-status-positive-subtle",
    "warning": "--colors-ds-semantic-content-warning",
    "warningFill": "--colors-ds-semantic-status-warning-solid",
    "warningSubtle": "--colors-ds-semantic-status-warning-subtle",
    "danger": "--colors-ds-semantic-content-negative",
    "dangerFill": "--colors-ds-semantic-status-negative-solid",
    "dangerSubtle": "--colors-ds-semantic-status-negative-subtle",
    "info": "--colors-ds-semantic-content-info",
    "infoFill": "--colors-ds-semantic-status-info-solid",
    "infoSubtle": "--colors-ds-semantic-status-info-subtle",
    "secondary": "--colors-ds-semantic-action-secondary-background",
    "secondaryHover": "--colors-ds-semantic-action-secondary-background-hover",
    "secondaryText": "--colors-ds-semantic-action-secondary-foreground",
}

DARK_NOTE = "Declared on the dark theme selector in the same public stylesheet. The public marketing site did not apply this theme; preferTheme=dark is a sign-in query, which was not followed."


def semantic(theme):
    sel = LIGHT_SEL if theme == "light" else DARK_SEL
    evidence = "Measured" if theme == "light" else "Declared"
    note = None if theme == "light" else DARK_NOTE
    group = {}
    for role, prop in LIGHT_ROLES.items():
        value, found = find(sel, prop)
        if not value:
            group[role] = {
                "$type": "color",
                "$value": "Not captured",
                "$extensions": {"source": src("Not captured", sel, prop, "Property missing on this selector")},
            }
            continue
        # Keep authored aliases as the resolved fallback when the declaration is var(--x,#hex).
        m = re.search(r"#[0-9a-fA-F]{3,8}", value)
        shown = m.group(0) if value.startswith("var(") and m else value
        group[role] = color(shown, evidence, found or sel, prop, note)
    return group


def type_role(name):
    size, _ = find(TYPE_SEL, f"--fontSize-ds-{name}")
    lh, _ = find(TYPE_SEL, f"--lineHeight-ds-{name}")
    weight, _ = find(TYPE_SEL, f"--fontWeight-ds-{name}")
    family, _ = find(TYPE_SEL, f"--fontFamily-ds-{name}")
    if not size:
        return None
    return {
        "$type": "typography",
        "$value": {
            "fontFamily": family or "Kraken-Product",
            "fontSize": size,
            "fontWeight": weight or "400",
            "lineHeight": lh or size,
        },
        "$extensions": {"source": src("Measured", TYPE_SEL, f"--fontSize-ds-{name}")},
    }


ROLES = [
    "display1", "display2", "display3", "display4",
    "heading1", "heading2", "heading3", "heading4", "heading5", "heading6",
    "body1", "body2", "body3", "caption1", "caption2",
    "label1", "label2", "label3",
]
RADII = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "round"]

core = {
    "fontFamily": {
        "brand": {
            "$type": "fontFamily",
            "$value": "Kraken-Brand, \"IBM Plex Sans\", Helvetica, Arial, sans-serif",
            "$extensions": {"source": src(
                "Measured", "h1 computed", "fontFamily",
                RAW["computed"]["h1"]["fontFamily"],
            )},
        },
        "product": {
            "$type": "fontFamily",
            "$value": "Kraken-Product, \"IBM Plex Sans\", Helvetica, Arial, sans-serif",
            "$extensions": {"source": src(
                "Measured", "a[href='/sign-up'] computed", "fontFamily",
                RAW["computed"]["signup"]["fontFamily"],
            )},
        },
    },
    "typography": {},
    "radius": {},
    "space": {
        "1": dim("4px", "Derived", SHAPE_SEL, "--border-radius-ds-2", "4px is the ds-2 radius step; used as the spacing base the control padding sits on"),
        "2": dim("8px", "Measured", "a[href='/sign-up'] computed", "padding-block", RAW["computed"]["signup"]["padding"]),
        "3": dim("12px", "Measured", "a[href='/sign-up'] computed", "padding-inline", RAW["computed"]["signup"]["padding"]),
        "4": dim("16px", "Measured", SHAPE_SEL, "--border-radius-ds-6"),
        "5": dim("24px", "Derived", SHAPE_SEL, "--spacing-ds-checkbox-icon-lg", "24px is the large checkbox icon size declared on the spacing theme"),
        "6": dim("32px", "Measured", SHAPE_SEL, "--border-radius-ds-8"),
    },
    "size": {
        "buttonMd": dim("36px", "Measured", "a[href='/sign-up'] computed", "height", RAW["computed"]["signup"]["height"]),
        "radiusControl": dim("12px", "Measured", "a[href='/sign-up'] computed", "borderRadius", RAW["computed"]["signup"]["borderRadius"]),
    },
}

for name in ROLES:
    token = type_role(name)
    if token:
        core["typography"][name] = token

for step in RADII:
    value, sel = find(SHAPE_SEL, f"--border-radius-ds-{step}")
    if value:
        core["radius"][step] = dim(value, "Measured", sel or SHAPE_SEL, f"--border-radius-ds-{step}")

light = semantic("light")
dark = semantic("dark")

# Computed check: body background matches the page token.
body_bg = RAW["computed"]["body"]["backgroundColor"]
light["page"]["$extensions"]["source"]["computedBodyBackground"] = body_bg

doc = {
    "$schema": "https://www.designtokens.org/schemas/2025.10/format.json",
    "core": core,
    "light": light,
    "dark": dark,
    "$themes": [
        {"id": "light", "name": "Magic light", "selectedTokenSets": {"core": "source", "light": "enabled"}},
        {"id": "dark", "name": "Magic dark (declared)", "selectedTokenSets": {"core": "source", "dark": "enabled"}},
    ],
    "$metadata": {
        "tokenSetOrder": ["core", "light", "dark"],
        "product": "Kraken",
        "captured": "2026-11-21",
        "route": "public",
        "signed_in": False,
    },
}

(HERE / "tokens.json").write_text(json.dumps(doc, indent=1) + "\n")
print("wrote", HERE / "tokens.json", "light", len(light), "dark", len(dark), "type", len(core["typography"]))
