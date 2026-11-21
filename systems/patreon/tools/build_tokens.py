#!/usr/bin/env python3
"""Build tokens.json from raw/css-vars.json.

Values are the literals declared on `.QbDuzW_definitions` (the logged-out app's
studio tokens) and on marketing `:root`. A `--global-*` name is an alias of
`--light-global-*` or `--dark-global-*`. Unread values stay out. No value is
invented.

Deterministic: same inputs, same bytes.
"""
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = json.loads((HERE / "raw" / "css-vars.json").read_text())
SRC = "css-var {name} ({selector})"


def decl(name, selector_prefix):
    hits = [d for d in RAW["decls"] if d["name"] == name and d["selector"].startswith(selector_prefix) and not d.get("media")]
    if not hits:
        raise KeyError(name + " " + selector_prefix)
    return hits[0]


def color(name, selector, description):
    d = decl(name, selector)
    return {
        "$value": d["value"],
        "$type": "color",
        "$extensions": {"source": SRC.format(name=name, selector=d["selector"]), "evidence": "Measured"},
        "$description": description,
    }


def dim(name, selector, description):
    d = decl(name, selector)
    value = d["value"]
    if not re.fullmatch(r"-?\d+(\.\d+)?(px|rem|em)", value) and value != "0":
        raise ValueError(f"{name} is not a dimension: {value}")
    if value == "0":
        value = "0px"
    return {
        "$value": value,
        "$type": "dimension",
        "$extensions": {"source": SRC.format(name=name, selector=d["selector"]), "evidence": "Measured"},
        "$description": description,
    }


def text_token(name, selector, type_, description):
    d = decl(name, selector)
    return {
        "$value": d["value"],
        "$type": type_,
        "$extensions": {"source": SRC.format(name=name, selector=d["selector"]), "evidence": "Measured"},
        "$description": description,
    }


APP = ".QbDuzW_definitions"
ROOT = ":root"

core = {
    "font": {
        "app": text_token("--desktop-type-body-fontStack", APP, "fontFamily", "ABC Oracle Plus Variable stack on the logged-out app"),
        "marketing": text_token("--font-primary-stack", ROOT, "fontFamily", "Oracle plus Noto Sans fallbacks on the marketing site"),
        "heading": text_token("--font-heading", ROOT, "fontFamily", "PatreonOracle_Regular, declared on marketing :root"),
    },
    "radius": {
        "none": dim("--shared-global-radius-none", APP, "0"),
        "sm": dim("--shared-global-radius-sm", APP, "4px"),
        "sm-md": dim("--shared-global-radius-smMd", APP, "6px"),
        "md": dim("--shared-global-radius-md", APP, "8px. A second declaration on the same selector says 10px; the first measured declaration is kept"),
        "lg": dim("--shared-global-radius-lg", APP, "12px"),
        "xl": dim("--shared-global-radius-xl", APP, "16px"),
        "pill": dim("--shared-global-radius-pill", APP, "9999px"),
    },
    "space": {
        "0": dim("--shared-global-space-x0", APP, "0"),
        "2": dim("--shared-global-space-x2", APP, "2px"),
        "4": dim("--shared-global-space-x4", APP, "4px"),
        "8": dim("--shared-global-space-x8", APP, "8px"),
        "12": dim("--shared-global-space-x12", APP, "12px"),
        "16": dim("--shared-global-space-x16", APP, "16px"),
        "24": dim("--shared-global-space-x24", APP, "24px"),
        "32": dim("--shared-global-space-x32", APP, "32px"),
        "48": dim("--shared-global-space-x48", APP, "48px"),
    },
    "border": {
        "thin": dim("--shared-global-borderWidth-thin", APP, "1px"),
        "thick": dim("--shared-global-borderWidth-thick", APP, "2px"),
    },
    "shadow": {
        "low": text_token("--shared-global-boxShadow-low", APP, "shadow", "0px 1px 4px 0px #0000000f"),
        "mid": text_token("--shared-global-boxShadow-mid", APP, "shadow", "0px 4px 14px 0px #0000001a"),
        "high": text_token("--shared-global-boxShadow-high", APP, "shadow", "0px 6px 24px 0px #00000024"),
    },
    "typography": {
        "body": {
            "$type": "typography",
            "$value": {
                "fontFamily": "{font.app}",
                "fontSize": decl("--desktop-type-body-fontSizes-md", APP)["value"],
                "fontWeight": decl("--desktop-type-body-fontWeights-normal", APP)["value"],
                "lineHeight": decl("--desktop-type-body-lineHeight", APP)["value"],
            },
            "$extensions": {"source": "css-var --desktop-type-body-* (.QbDuzW_definitions)", "evidence": "Measured"},
        },
        "heading": {
            "$type": "typography",
            "$value": {
                "fontFamily": "{font.app}",
                "fontSize": decl("--desktop-type-heading-fontSizes-lg", APP)["value"],
                "fontWeight": decl("--desktop-type-heading-fontWeights-medium", APP)["value"],
                "lineHeight": decl("--desktop-type-heading-lineHeight", APP)["value"],
            },
            "$extensions": {"source": "css-var --desktop-type-heading-* (.QbDuzW_definitions)", "evidence": "Measured"},
        },
        "display": {
            "$type": "typography",
            "$value": {
                "fontFamily": "{font.app}",
                "fontSize": decl("--desktop-type-display-fontSizes-xl", APP)["value"],
                "fontWeight": decl("--desktop-type-display-fontWeights-medium", APP)["value"],
                "lineHeight": decl("--desktop-type-display-lineHeight", APP)["value"],
            },
            "$extensions": {"source": "css-var --desktop-type-display-* (.QbDuzW_definitions)", "evidence": "Measured"},
        },
    },
    "motion": {
        "duration": text_token("--animation-duration", ROOT, "duration", "0.5s on marketing :root"),
        "side-nav": text_token("--_side-nav-new-transition-duration", ".SideNav", "duration", "320ms on the app side nav"),
    },
}

def semantic(prefix):
    roles = {
        "page": color(f"--{prefix}-global-bg-page-default", APP, "Page ground"),
        "surface": color(f"--{prefix}-global-bg-elevated-default", APP, "Elevated surface"),
        "surface-alt": color(f"--{prefix}-global-bg-baseAlt-default", APP, "Alternate base surface"),
        "text": color(f"--{prefix}-global-content-regular-default", APP, "Regular text"),
        "text-muted": color(f"--{prefix}-global-content-muted-default", APP, "Muted text"),
        "text-primary": color(f"--{prefix}-global-content-primary-default", APP, "Primary content"),
        "border": color(f"--{prefix}-global-border-muted-default", APP, "Muted border"),
        "border-strong": color(f"--{prefix}-global-border-strong-default", APP, "Strong border"),
        "critical": color(f"--{prefix}-global-content-critical-default", APP, "Critical text"),
        "success": color(f"--{prefix}-global-content-success-default", APP, "Success text"),
        "warning": color(f"--{prefix}-global-content-warning-default", APP, "Warning text"),
    }
    if prefix == "light":
        roles["accent"] = {
            "$value": "rgb(175, 2, 16)",
            "$type": "color",
            "$extensions": {
                "source": "computed backgroundColor of Join for free on /cw/GlamorousTrash/membership, 2026-11-20",
                "evidence": "Measured",
            },
            "$description": "Creator-page primary button fill in light. Not a studio token name. Marketing pages use black and white instead.",
        }
    else:
        roles["accent"] = {
            "$value": "rgb(175, 2, 16)",
            "$type": "color",
            "$extensions": {
                "source": "copied from light.accent; dark appearance was not clicked in this capture",
                "evidence": "Derived",
            },
            "$description": "Same fill as the light membership button. A live dark Join fill was not measured.",
        }
    return roles


tokens = {
    "core": core,
    "light": semantic("light"),
    "dark": semantic("dark"),
    "$themes": [
        {"id": "light", "name": "light", "selectedTokenSets": {"core": "enabled", "light": "enabled"}},
        {"id": "dark", "name": "dark", "selectedTokenSets": {"core": "enabled", "dark": "enabled"}},
    ],
    "$extensions": {
        "notTokenised": [
            "Marketing --color-neutral-* values are color-mix() aliases, recorded in raw/css-vars.json, not copied as a second ramp.",
            "Creator accent rgb(175, 2, 16) is one creator's button, measured on Glamorous Trash membership. Other creators may theme it.",
            "Focus ring colour was not read from a focus-visible state. Not captured.",
            "Logged-out app home (Home | Patreon) was mapped, then later loads of / served the marketing homepage. App-home screenshots are not in this package.",
        ]
    },
}

out = HERE / "tokens.json"
out.write_text(json.dumps(tokens, indent=2) + "\n")
print("wrote", out, "light.page", tokens["light"]["page"]["$value"], "dark.page", tokens["dark"]["page"]["$value"])
