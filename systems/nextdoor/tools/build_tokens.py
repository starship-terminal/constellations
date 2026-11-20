#!/usr/bin/env python3
"""Build tokens.json from raw/css-vars.json for the Nextdoor public capture.

The homepage declares Theme UI and --nd-* custom properties. This builder
keeps the semantic colour roles, the green and blue-gray ramps, the type
roles, the space and radius scales, and the motion tokens. Every token
carries $extensions.source. A name that is not in the readings is not
invented.

Dark values come from the .dark:root declarations the stylesheet harvest
resolved. The public pages do not apply that class. See the README.
"""
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
V = json.loads((RAW / "css-vars.json").read_text())
LIGHT = V["resolved"]["light"]
DARK = V["resolved"]["dark"]

# Product font weights are 420 and 620 (variable-font book and semibold).
# DESIGN.md and the DTCG fontWeight type want 100-900. The measured value
# stays in $extensions.measuredWeight.
WEIGHT = {420: 400, 620: 600}


def src(name, theme="light"):
    return f"css-var {name} ({theme}), raw/css-vars.json, nextdoor.com homepage 2026-11-21"


def val(theme, name):
    bag = LIGHT if theme == "light" else DARK
    item = bag.get(name)
    if not item or "value" not in item:
        raise KeyError(name)
    return item["value"]


def color(theme, name):
    return {
        "$value": val(theme, name),
        "$type": "color",
        "$extensions": {"source": src(name, theme)},
    }


def dim_from(theme, name):
    v = val(theme, name)
    if isinstance(v, (int, float)):
        v = f"{v:g}px"
    return {
        "$value": v,
        "$type": "dimension",
        "$extensions": {"source": src(name, theme)},
    }


def number_token(theme, name, as_weight=False):
    v = val(theme, name)
    measured = v
    if as_weight:
        v = WEIGHT.get(int(v), int(v))
    return {
        "$value": v,
        "$type": "fontWeight" if as_weight else "number",
        "$extensions": {"source": src(name, theme), "measuredWeight": measured} if as_weight else {"source": src(name, theme)},
    }


def font_family(theme, name):
    return {
        "$value": val(theme, name),
        "$type": "fontFamily",
        "$extensions": {"source": src(name, theme)},
    }


def duration(theme, name):
    v = val(theme, name)
    # readings come back as 0.5s; DTCG duration in this repo is Nms
    m = re.fullmatch(r"([\d.]+)s", str(v))
    if m:
        v = f"{float(m.group(1)) * 1000:g}ms"
    return {
        "$value": v,
        "$type": "duration",
        "$extensions": {"source": src(name, theme)},
    }


def easing(theme, name):
    raw = val(theme, name)
    m = re.fullmatch(r"cubic-bezier\(\s*([-\d.]+)[,\s]+([-\d.]+)[,\s]+([-\d.]+)[,\s]+([-\d.]+)\s*\)", str(raw))
    if not m:
        raise ValueError(raw)
    return {
        "$value": [float(x) for x in m.groups()],
        "$type": "cubicBezier",
        "$extensions": {"source": src(name, theme)},
    }


def semantic(theme):
    roles = {
        "page": "--nd-color-bgPrimary",
        "surface": "--nd-color-bgBase",
        "elevated": "--nd-color-bgElevated",
        "emphasis": "--nd-color-bgEmphasis",
        "overlay": "--nd-color-bgTint",
        "underlay": "--nd-color-bgUnderlay",
        "text": "--nd-color-fgPrimary",
        "muted": "--nd-color-fgSecondary",
        "onAccent": "--theme-ui-colors-on-brand-logo",
        "link": "--theme-ui-colors-fg-blue",
        "accent": "--nd-color-brandLogo",
        "accentPressed": "--theme-ui-colors-brand-lime-logo",
        "border": "--theme-ui-colors-blueGray10",
        "borderStrong": "--theme-ui-colors-blueGray70",
        "focus": "--theme-ui-colors-blue60",
        "success": "--theme-ui-colors-green40",
        "warning": "--nd-color-bgWarning",
        "danger": "--theme-ui-colors-fg-error",
        "info": "--theme-ui-colors-fg-blue",
        "errorSurface": "--nd-color-bgError",
    }
    return {k: color(theme, n) for k, n in roles.items()}


def ramp(theme, prefix, steps):
    out = {}
    for step in steps:
        name = f"--theme-ui-colors-{prefix}{step}"
        out[str(step)] = color(theme, name)
    return out


def core():
    space_steps = ["0", "0_25", "0_5", "1", "1_5", "2", "3", "4", "5", "6", "8", "10", "12", "16", "20"]
    space = {s.replace("_", "."): dim_from("light", f"--nd-space-{s}") for s in space_steps}
    radius = {
        "none": dim_from("light", "--nd-border-radius-none"),
        "xs": dim_from("light", "--nd-border-radius-0_5"),
        "sm": dim_from("light", "--nd-border-radius-2"),
        "md": dim_from("light", "--nd-border-radius-3"),
        "lg": dim_from("light", "--nd-border-radius-4"),
        "pill": dim_from("light", "--nd-border-radius-pill"),
    }
    type_roles = ["body", "bodyTitle", "detail", "mini", "sectionTitle", "headline", "shout", "folio"]
    typography = {}
    for role in type_roles:
        typography[role] = {
            "$value": {
                "fontFamily": val("light", f"--nd-font-family-{role}"),
                "fontSize": val("light", f"--nd-font-size-{role}"),
                "fontWeight": WEIGHT.get(int(val("light", f"--nd-font-weight-{role}")), int(val("light", f"--nd-font-weight-{role}"))),
                "lineHeight": "1.25",
            },
            "$type": "typography",
            "$extensions": {
                "source": src(f"--nd-font-size-{role}") + "; lineHeight is Not captured as a token (the stylesheet does not declare one for this role)",
                "measuredWeight": val("light", f"--nd-font-weight-{role}"),
                "lineHeight": "Not captured",
            },
        }
    motion = {}
    for step in ["3", "4", "6", "8", "10", "16", "20", "30", "40"]:
        motion["duration" + step] = duration("light", f"--nd-motion-duration-{step}")
    for name, var in [
        ("emphasized", "--nd-motion-easing-emphasized"),
        ("emphasizedAccelerate", "--nd-motion-easing-emphasizedAccelerate"),
        ("emphasizedDecelerate", "--nd-motion-easing-emphasizedDecelerate"),
    ]:
        motion[name] = easing("light", var)
    return {
        "color": {
            "green": ramp("light", "green", [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]),
            "blueGray": ramp("light", "blueGray", [0, 5, 10, 20, 30, 40, 50, 60, 70, 80, 90]),
            "blue": ramp("light", "blue", [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]),
            "red": ramp("light", "red", [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]),
            "orange": ramp("light", "orange", [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]),
        },
        "font": {
            "family": font_family("light", "--nd-font-family-body"),
            "weightBody": number_token("light", "--nd-font-weight-body", as_weight=True),
            "weightTitle": number_token("light", "--nd-font-weight-bodyTitle", as_weight=True),
        },
        "typography": typography,
        "space": space,
        "radius": radius,
        "motion": motion,
    }


def measured():
    """Values read from painted elements, not from a custom property."""
    return {
        "buttonHoverOpacity": {
            "$value": 0.88,
            "$type": "number",
            "$extensions": {"source": "Measured computed filter opacity(0.88) on the Sign up face while hovered, nextdoor.com homepage 2026-11-21"},
        },
        "fieldFocusRing": {
            "$value": "2px",
            "$type": "dimension",
            "$extensions": {"source": "Measured box-shadow inset 2px on the focused email field, nextdoor.com homepage 2026-11-21. Ring colour is light.color.borderStrong."},
        },
        "controlHeight": {
            "$value": "48px",
            "$type": "dimension",
            "$extensions": {"source": "Measured Sign up and Continue face height, nextdoor.com homepage 2026-11-21"},
        },
        "fieldHeight": {
            "$value": "56px",
            "$type": "dimension",
            "$extensions": {"source": "Measured email field height, nextdoor.com homepage 2026-11-21"},
        },
    }


doc = {
    "$description": "Nextdoor public web, measured 2026-11-21 from nextdoor.com custom properties. Dark is declared on .dark:root and is not applied on the public pages.",
    "core": core(),
    "light": {"color": semantic("light"), "measured": measured()},
    "dark": {"color": semantic("dark")},
    "$themes": [
        {"id": "light", "name": "light", "selectedTokenSets": {"core": "source", "light": "enabled"}},
        {"id": "dark", "name": "dark", "selectedTokenSets": {"core": "source", "dark": "enabled"}},
    ],
}

# Attach measured group source note
out = HERE / "tokens.json"
out.write_text(json.dumps(doc, indent=1) + "\n")
print("wrote", out, "light roles", len(doc["light"]["color"]), "dark roles", len(doc["dark"]["color"]))
