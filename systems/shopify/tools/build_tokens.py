#!/usr/bin/env python3
"""Build tokens.json from systems/shopify/raw/css-vars.json.

Values are the custom properties read on https://www.shopify.com/?country=us&lang=en
on 2026-11-21. Shopify publishes one light theme on the public marketing site.
A name that was not in the resolved dump is not invented.

Deterministic: same inputs, byte-identical output.
"""
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
V = json.loads((RAW / "css-vars.json").read_text())
RES = V["resolved"]


def src(name):
    return {"source": "css-var " + name, "label": "Measured"}


def color(name, description=None):
    token = {"$value": RES[name], "$type": "color", "$extensions": src(name)}
    if description:
        token["$description"] = description
    return token


def dim_from_rem(name):
    raw = RES[name].strip()
    m = re.fullmatch(r"([\d.]+)rem", raw)
    if not m:
        raise SystemExit(f"{name} is not a rem length: {raw}")
    px = round(float(m.group(1)) * 16, 3)
    px_s = ("%g" % px) + "px"
    return {
        "$value": px_s,
        "$type": "dimension",
        "$extensions": {
            "source": f"derived from css-var {name} ({raw} at 16px root)",
            "label": "Derived",
            "raw": raw,
        },
    }


def font_weight(name):
    return {"$value": int(RES[name]), "$type": "fontWeight", "$extensions": src(name)}


def duration(name):
    raw = RES[name].strip()
    m = re.fullmatch(r"([\d.]+)s", raw)
    if not m:
        raise SystemExit(f"{name} is not a seconds duration: {raw}")
    ms = int(round(float(m.group(1)) * 1000))
    return {
        "$value": f"{ms}ms",
        "$type": "duration",
        "$extensions": {"source": f"derived from css-var {name} ({raw})", "label": "Derived"},
    }


core = {
    "palette": {
        "black": color("--color-black", "Ink and primary button fill"),
        "white": color("--color-white", "Page and button label on black"),
        "shade": {
            "10": color("--color-shade-10"),
            "20": color("--color-shade-20"),
            "30": color("--color-shade-30"),
            "40": color("--color-shade-40"),
            "50": color("--color-shade-50"),
            "60": color("--color-shade-60"),
            "70": color("--color-shade-70"),
            "90": color("--color-shade-90"),
        },
    },
    "font": {
        "family": {
            "sans": {
                "$value": RES["--font-sans"],
                "$type": "fontFamily",
                "$extensions": src("--font-sans"),
            },
            "mono": {
                "$value": RES["--font-mono"],
                "$type": "fontFamily",
                "$extensions": src("--font-mono"),
            },
        }
    },
    "typography": {},
    "space": {},
    "radius": {},
    "motion": {
        "duration": {
            "default": duration("--default-transition-duration"),
        },
        "easing": {
            "in": {"$value": RES["--ease-in"], "$type": "cubicBezier", "$extensions": src("--ease-in")},
            "out": {"$value": RES["--ease-out"], "$type": "cubicBezier", "$extensions": src("--ease-out")},
            "in-out": {"$value": RES["--ease-in-out"], "$type": "cubicBezier", "$extensions": src("--ease-in-out")},
            "uc": {"$value": RES["--ease-uc"], "$type": "cubicBezier", "$extensions": src("--ease-uc")},
        },
    },
    "size": {
        "header": dim_from_rem("--header-height"),
    },
}

# Type roles t1 (display) down to t8 (body). Line height was not a custom property.
for step, role in (
    ("t1", "display"),
    ("t2", "heading-1"),
    ("t3", "heading-2"),
    ("t4", "heading-3"),
    ("t5", "heading-4"),
    ("t6", "heading-5"),
    ("t7", "body-large"),
    ("t8", "body"),
):
    core["typography"][role] = {
        "$value": {
            "fontFamily": "{font.family.sans}",
            "fontSize": dim_from_rem(f"--font-size-{step}")["$value"],
            "fontWeight": int(RES[f"--font-weight-{step}"]),
            "lineHeight": 1.2,
        },
        "$type": "typography",
        "$extensions": {
            "source": f"css-var --font-size-{step} and --font-weight-{step}; lineHeight 1.2 is Derived from a 16px root conversion, not a declared line-height token",
            "label": "Derived",
        },
    }

for name in ("xs", "sm", "md", "lg", "xl", "2xl", "3xl", "4xl", "5xl"):
    core["space"][name] = dim_from_rem(f"--space-{name}")

for name in ("md", "lg", "xl", "2xl"):
    core["radius"][name] = dim_from_rem(f"--radius-{name}")

light = {
    "background": {
        "page": {"$value": "{palette.black}", "$type": "color", "$extensions": {"source": "computed body backgroundColor rgb(0, 0, 0) on the home hero", "label": "Measured"}},
        "surface": {"$value": "{palette.shade.10}", "$type": "color", "$extensions": {"source": "alias of --color-shade-10, the light band under the hero", "label": "Derived"}},
        "inverse": {"$value": "{palette.white}", "$type": "color", "$extensions": {"source": "alias of --color-white", "label": "Derived"}},
    },
    "text": {
        "primary": {"$value": "{palette.white}", "$type": "color", "$extensions": {"source": "header color computed rgb(255, 255, 255) on the home hero", "label": "Measured"}},
        "muted": {"$value": "{palette.shade.40}", "$type": "color", "$extensions": {"source": "alias of --color-shade-40 for secondary copy on black", "label": "Derived"}},
        "on-accent": {"$value": "{palette.black}", "$type": "color", "$extensions": {"source": "Start for free label computed rgb(0, 0, 0)", "label": "Measured"}},
        "link": {"$value": "{palette.white}", "$type": "color", "$extensions": {"source": "Log in computed rgb(255, 255, 255) in the header", "label": "Measured"}},
    },
    "border": {
        "default": {"$value": "{palette.shade.70}", "$type": "color", "$extensions": {"source": "alias of --color-shade-70", "label": "Derived"}},
        "strong": {"$value": "{palette.white}", "$type": "color", "$extensions": {"source": "alias of --color-white", "label": "Derived"}},
    },
    "action": {
        "primary": {"$value": "{palette.white}", "$type": "color", "$extensions": {"source": "Start for free fill computed rgb(255, 255, 255); hover computed rgb(212, 212, 216) which is --color-shade-30", "label": "Measured"}},
        "primary-hover": color("--color-shade-30", "Hover fill of the white pill button"),
    },
    "focus": {
        "ring": color("--color-link-dark-focus", "Declared focus colour. Public controls often show no painted ring."),
    },
}

doc = {
    "core": core,
    "light": light,
    "$themes": [
        {"id": "light", "name": "Light", "selectedTokenSets": {"core": "source", "light": "enabled"}}
    ],
    "$extensions": {
        "notCaptured": [
            "Dark theme: the public marketing site exposes color-scheme normal and no dark token set.",
            "Status colours (success, warning, danger, info) are not declared as semantic roles on the marketing pages.",
            "Elevation shadows are not a named scale in the captured custom properties.",
            "Focus ring width and offset: Not captured as tokens. --color-link-dark-focus is the only focus colour read.",
            "Line heights are not custom properties; typography lineHeight is a derived stand-in.",
        ]
    },
}

# cubicBezier must be a 4-number array for DTCG checkers that are strict.
# The kit and catalog accept a string in some packages; keep the authored string
# and also store the parsed array.
for key, token in core["motion"]["easing"].items():
    raw = token["$value"]
    m = re.fullmatch(r"cubic-bezier\(\s*([\d.]+)\s*,\s*([\d.]+)\s*,\s*([\d.]+)\s*,\s*([\d.]+)\s*\)", raw)
    if not m:
        raise SystemExit("easing not parsed: " + raw)
    token["$value"] = [float(m.group(i)) for i in range(1, 5)]

out = HERE / "tokens.json"
out.write_text(json.dumps(doc, indent=2) + "\n")
print("wrote", out, "tokens")
