#!/usr/bin/env python3
"""Build tokens.json from raw/css-vars.json and raw/states.json.

Colour ramps and semantic aliases are the values getComputedStyle resolved on
https://www.synthesia.io/ at 1440x900. Declared var() aliases are kept when
they resolve to the same colour as the target. Component geometry comes from
measured controls. Synthesia's public site ships one theme.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
VARS = json.loads((RAW / "css-vars.json").read_text())
STATES = json.loads((RAW / "states.json").read_text())
RESOLVED = VARS["resolved"]
DECLARED = VARS["declared"]
SRC = "computed on https://www.synthesia.io/ at 1440x900, 2026-11-19 (raw/css-vars.json)"


def tok(value, typ, source):
    return {"$value": value, "$type": typ, "$extensions": {"source": source}}


def color_token(name, source=None):
    value = RESOLVED[name]
    if value == "white":
        value = "#ffffff"
    elif value == "transparent":
        value = "rgba(0, 0, 0, 0)"
    return tok(value, "color", source or f"{SRC}; {name}")


def slug(name: str) -> str:
    name = name.removeprefix("--")
    name = name.replace("_semantic---", "semantic.")
    name = name.replace("_typography---", "type.")
    name = name.replace("-", ".")
    name = name.replace("..", ".")
    return name


def group(parts, node):
    cursor = {}
    for path, token in parts:
        bits = path.split(".")
        cur = cursor
        for bit in bits[:-1]:
            cur = cur.setdefault(bit, {})
        cur[bits[-1]] = token
    return cursor


RAMP_PREFIXES = (
    "--indigo-", "--grey-", "--error-", "--success-", "--warning-",
    "--lime-", "--orange-", "--pink-", "--teal-", "--yellow-",
    "--base-dark", "--base-white",
)

core_color = {}
base = {}
for name in sorted(RESOLVED):
    if name.startswith("--base-dark") or name.startswith("--base-white"):
        key = name.removeprefix("--base-").replace("-", ".")
        bucket, _, rest = key.partition(".")
        if rest:
            base.setdefault(bucket, {})[rest.replace(".", "-")] = color_token(name)
        else:
            base[bucket] = color_token(name)
        continue
    if not name.startswith(RAMP_PREFIXES):
        continue
    hue, rest = name.removeprefix("--").split("-", 1)
    step = rest.replace("-main", "")
    core_color.setdefault(hue, {})[step] = color_token(name)
core_color["base"] = base

# Painted nav button, which the semantic sheet does not name.
core_color["ink"] = tok("#090b22", "color", "measured nav primary button background (raw/states.json buttonPrimaryDefault)")
core_color["inkHover"] = tok("#0d0f2ccc", "color", "measured nav primary button hover background rgba(13, 15, 44, 0.8)")
core_color["shadow"] = color_token("--shadow")

semantic = {}
for name in sorted(RESOLVED):
    if not name.startswith("--_semantic---"):
        continue
    path = name.removeprefix("--_semantic---").replace("-", ".")
    declared = DECLARED.get(name, {}).get("value", "")
    alias = re.fullmatch(r"var\((--[A-Za-z0-9_-]+)\)", declared)
    if alias and alias.group(1) in RESOLVED and RESOLVED[alias.group(1)] == RESOLVED[name]:
        raw = alias.group(1).removeprefix("--")
        raw = raw.replace("-main", "")
        if raw.startswith("base-"):
            target = "color.base." + raw.removeprefix("base-").split("-")[0]
        else:
            hue, _, step = raw.partition("-")
            target = f"color.{hue}.{step}"
        semantic[path] = tok("{" + target + "}", "color", f"{SRC}; declared {declared}, resolved {RESOLVED[name]}")
    else:
        semantic[path] = color_token(name, f"{SRC}; declared {declared or 'n/a'}, resolved {RESOLVED[name]} (alias dropped: resolution differs)")

type_roles = {}
role_names = set()
for name in RESOLVED:
    if name.startswith("--_typography---") and name.endswith("-font-size"):
        role_names.add(name.removeprefix("--_typography---").removesuffix("-font-size"))

for role in sorted(role_names):
    prefix = f"--_typography---{role}-"
    size = RESOLVED.get(prefix + "font-size")
    lh = RESOLVED.get(prefix + "line-height")
    ls = RESOLVED.get(prefix + "letter-spacing")
    if not size or not lh:
        continue
    key = role.replace("-", ".")
    if ls and ls.startswith(("-.", ".")):
        ls = ls.replace(".", "0.", 1)  # -.275rem -> -0.275rem
    type_roles[key] = tok({
        "fontFamily": "{font.family.brand}",
        "fontWeight": "500" if role.startswith("heading") else "400",
        "fontSize": size,
        "lineHeight": lh,
        "letterSpacing": ls or "0rem",
    }, "typography", f"Measured size, line height and tracking: {SRC}; --_typography---{role}-*. "
       "fontWeight is Derived by rule (500 for heading roles, 400 for the rest), not read: "
       "the fluid sheet declares no weight.")

# Measured hero and buttons override the fluid sheet for the roles we saw.
type_roles["hero"] = tok({
    "fontFamily": "{font.family.brand}",
    "fontWeight": "500",
    "fontSize": "56px",
    "lineHeight": "56px",
    "letterSpacing": "-3.08px",
}, "typography", "measured h1.heading-large on / at 1440 (raw/states.json h1)")

spacing = {}
for name, value in sorted(RESOLVED.items()):
    if not name.startswith("--base-spacing-"):
        continue
    key = name.removeprefix("--base-spacing-")
    spacing[key] = tok(value if value != ".25rem" else "0.25rem", "dimension", f"{SRC}; {name}")
    if spacing[key]["$value"].startswith("."):
        spacing[key]["$value"] = "0" + spacing[key]["$value"]

radius = {}
for name, value in sorted(RESOLVED.items()):
    if not name.startswith("--border-radius-"):
        continue
    key = name.removeprefix("--border-radius-")
    shown = value if not value.startswith(".") else "0" + value
    radius[key] = tok(shown, "dimension", f"{SRC}; {name}")

component = {
    "button": {
        "primary": {
            "background": tok("{color.ink}", "color", "raw/states.json buttonPrimaryDefault"),
            "color": tok("#ffffff", "color", "raw/states.json buttonPrimaryDefault"),
            "radius": tok("8px", "dimension", "raw/states.json nav .button.is-small"),
            "padding": {  # the computed shorthand 8px 16px, one px length per axis
                "block": tok("8px", "dimension", "raw/states.json buttonPrimaryDefault pad 8px 16px"),
                "inline": tok("16px", "dimension", "raw/states.json buttonPrimaryDefault pad 8px 16px"),
            },
            "fontSize": tok("14px", "dimension", "raw/states.json buttonPrimaryDefault"),
            "hoverBackground": tok("{color.inkHover}", "color", "raw/states.json buttonPrimaryHover"),
            "shadow": tok("0px 2px 10px 0px #10182814", "shadow", "measured rgba(16, 24, 40, 0.08) 0px 2px 10px 0px; --shadow is #10182814"),
        },
        "secondary": {
            "background": tok("#ffffff", "color", "raw/measurements.json home.secondary"),
            "color": tok("{color.ink}", "color", "raw/measurements.json home.secondary"),
            "radius": tok("10px", "dimension", "raw/measurements.json home.secondary"),
            "shadow": tok("inset 0px 0px 0px 1px #dadadd", "shadow", "measured inset ring rgb(218, 218, 221), grey-300"),
        },
    },
    "field": {
        "background": tok("#ffffff", "color", "raw/states.json fieldDefault"),
        "color": tok("#363636", "color", "raw/states.json fieldDefault"),
        "radius": tok("8px", "dimension", "raw/states.json fieldDefault"),
        "height": tok("48px", "dimension", "raw/states.json fieldDefault"),
        "fontSize": tok("16px", "dimension", "raw/states.json fieldDefault"),
    },
    "nav": {
        "height": tok("72px", "dimension", "raw/states.json nav"),
        "link": tok("#68686a", "color", "raw/states.json loginDefault rgb(104, 104, 106)"),
        "linkHover": tok("{color.ink}", "color", "raw/states.json loginHover"),
    },
}

tokens = {
    "core": {
        "color": core_color,
        "font": {
            "family": {
                "brand": tok("\"Basiersquare Webfont\", sans-serif", "fontFamily", f"{SRC}; --_typography---basier"),
            }
        },
        "typography": type_roles,
        "spacing": spacing,
        "radius": radius,
        "component": component,
    },
    "light": semantic and {"color": semantic} or {"color": {}},
    "$themes": [{"id": "light", "name": "Light", "selectedTokenSets": {"core": "source", "light": "enabled"}}],
}

# light.color was built as a flat dotted dict. Nest it.
nested = {}
for path, token in semantic.items():
    bits = path.split(".")
    cur = nested
    for bit in bits[:-1]:
        cur = cur.setdefault(bit, {})
    cur[bits[-1]] = token
tokens["light"] = {"color": nested}



def render():
    """tokens.json's exact text; importing this module writes nothing."""
    return json.dumps(tokens, indent=2) + "\n"


if __name__ == "__main__":
    out = HERE / "tokens.json"
    out.write_text(render())
    print(f"wrote {out} ramps={len(core_color)} semantic={len(semantic)} type={len(type_roles)}")
