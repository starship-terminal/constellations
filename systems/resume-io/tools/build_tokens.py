#!/usr/bin/env python3
"""Build tokens.json from raw/measured.json.

Every colour, size and shadow in raw/measured.json was read from resume.io on
2026-11-19: custom properties from getComputedStyle(documentElement) on the
marketing home and the signed-out sign-in shell, plus computed styles on the
painted controls. This file does not invent a ramp step, a dark theme, or a
state that was not read.

Light is the only theme. The footer paints a dark band inside that theme; those
colours stay under light.background.footer and light.text.on-footer.
"""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = json.loads((HERE / "raw" / "measured.json").read_text())

HOME = "https://resume.io/ on 2026-11-19, getComputedStyle(documentElement), landing CSS"
APP = "https://resume.io/app/auth/sign-in on 2026-11-19, getComputedStyle(documentElement), builder CSS"
COMPUTED = "computed style on the live signed-out page, 2026-11-19"


def tok(value, typ, source, evidence="Measured"):
    return {
        "$type": typ,
        "$value": value,
        "$extensions": {"source": source, "evidence": evidence},
    }


def color(name, group):
    return tok(RAW["palette"][group][name], "color", f"{HOME}; --{group}-{name}")


core_color = {}
for group, steps in RAW["palette"].items():
    core_color[group] = {step: color(step, group) for step in steps}

brand = {}
for name, value in RAW["brand"].items():
    brand[name] = tok(value, "color", f"{HOME}; --{name}")

spacing = {}
for name, value in RAW["spacing"].items():
    spacing[name] = tok(value, "dimension", f"{APP}; --spacing-{name}")

font_size = {}
for name, value in RAW["fontSize"].items():
    font_size[name] = tok(value, "dimension", f"{APP}; --font-{name}")

line = {}
for name, value in RAW["lineHeight"].items():
    line[name] = tok(value, "dimension", f"{APP}; --line-{name}")

weight = {}
for name, value in RAW["weight"].items():
    weight[name] = tok(value, "fontWeight", f"{APP}; --weight-{name}")

shadows = {}
for name, value in RAW["shadow"].items():
    shadows[name] = tok(value, "shadow", f"{APP}; --{name}")

families = {
    "commons": tok(RAW["fontFamily"]["commons"], "fontFamily", f"{COMPUTED}; body font-family on https://resume.io/"),
    "talent": tok(RAW["fontFamily"]["talent"], "fontFamily", f"{COMPUTED}; body font-family on {APP.split(';')[0]}"),
    "tricks": tok(RAW["fontFamily"]["tricks"], "fontFamily", f"{HOME}; @font-face TT Tricks in landing CSS (declared, not used on the measured body)"),
}

typography = {}
for name, spec in RAW["typography"].items():
    typography[name] = tok(
        {
            "fontFamily": spec["fontFamily"],
            "fontSize": spec["fontSize"],
            "fontWeight": spec["fontWeight"],
            "lineHeight": spec["lineHeight"],
            "letterSpacing": spec.get("letterSpacing", "0px"),
        },
        "typography",
        spec["source"],
    )

radius = {name: tok(value, "dimension", source) for name, (value, source) in RAW["radius"].items()}

tokens = {
    "core": {
        "color": core_color,
        "brand": brand,
        "spacing": spacing,
        "fontSize": font_size,
        "lineHeight": line,
        "fontWeight": weight,
        "shadow": shadows,
        "fontFamily": families,
        "typography": typography,
        "radius": radius,
        "layout": {
            "container": tok(RAW["layout"]["container"], "dimension", f"{HOME}; --container-width"),
            "nav-height": tok(RAW["layout"]["navHeight"], "dimension", f"{COMPUTED}; header.nav height on https://resume.io/"),
        },
    },
    "light": {
        "background": {k: tok(v, "color", s) for k, (v, s) in RAW["semantic"]["background"].items()},
        "text": {k: tok(v, "color", s) for k, (v, s) in RAW["semantic"]["text"].items()},
        "border": {k: tok(v, "color", s) for k, (v, s) in RAW["semantic"]["border"].items()},
        "component": {k: tok(v, "color", s) for k, (v, s) in RAW["semantic"]["component"].items()},
    },
    "$themes": [
        {"id": "light", "name": "light", "selectedTokenSets": {"core": "source", "light": "enabled"}}
    ],
}

out = HERE / "tokens.json"
out.write_text(json.dumps(tokens, indent=2) + "\n")
print(f"wrote {out} ({out.stat().st_size} bytes)")
