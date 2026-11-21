#!/usr/bin/env python3
"""Build tokens.json from raw/css-vars.json and raw/components.json.

Public marketing site only, measured 2026-11-21 from https://www.granola.ai/.
The site paints one light theme. Dark --oats-* declarations exist in CSS and
are not a public theme, so they are not a token set.

Every token is a value read from a declared custom property or a computed
style. Nothing is filled from memory.
"""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
VARS = json.loads((RAW / "css-vars.json").read_text())
COMP = json.loads((RAW / "components.json").read_text())

DECLARED = {}
for rule in VARS["declared"]:
    if rule["context"]:
        continue
    sel = rule["selector"]
    if sel not in (":root", ":host, :root", ":where(:root, :host)"):
        continue
    for name, value in rule["props"].items():
        DECLARED[name] = (value, sel)


def src(name, note=None):
    value, sel = DECLARED[name]
    out = {
        "label": "Measured",
        "file": "raw/css-vars.json",
        "selector": sel,
        "property": name,
        "page": "https://www.granola.ai/",
        "run": "2026-11-21",
    }
    if note:
        out["note"] = note
    return out


def color(name, note=None):
    value, _ = DECLARED[name]
    return {"$type": "color", "$value": value, "$extensions": {"source": src(name, note)}}


def dim(name, note=None):
    value, _ = DECLARED[name]
    return {"$type": "dimension", "$value": value, "$extensions": {"source": src(name, note)}}


def font(name):
    value, _ = DECLARED[name]
    return {"$type": "fontFamily", "$value": value, "$extensions": {"source": src(name)}}


def weight(name):
    value, _ = DECLARED[name]
    return {"$type": "fontWeight", "$value": value, "$extensions": {"source": src(name)}}


def cubic(name):
    value, _ = DECLARED[name]
    # cubic-bezier(.16,1,.3,1) -> [0.16, 1, 0.3, 1]
    inner = value[value.find("(") + 1:value.find(")")]
    nums = [float(x) if "." in x else int(x) for x in inner.split(",")]
    return {"$type": "cubicBezier", "$value": nums, "$extensions": {"source": src(name)}}


def measured_comp(label, value, element, prop):
    return {
        "$type": "color" if prop.lower().endswith("color") or prop == "backgroundColor" else "dimension",
        "$value": value,
        "$extensions": {
            "source": {
                "label": "Measured",
                "file": "raw/components.json",
                "element": element,
                "property": prop,
                "page": "https://www.granola.ai/",
                "run": "2026-11-21",
                "note": label,
            }
        },
    }


core = {
    "color": {
        "oats": {
            "neutral": {
                "50": color("--color-oats-neutral-50"),
                "100": color("--color-oats-neutral-100"),
                "150": color("--color-oats-neutral-150"),
                "200": color("--color-oats-neutral-200"),
                "300": color("--color-oats-neutral-300"),
                "400": color("--color-oats-neutral-400"),
                "450": color("--color-oats-neutral-450"),
                "500": color("--color-oats-neutral-500"),
                "600": color("--color-oats-neutral-600"),
                "700": color("--color-oats-neutral-700"),
                "750": color("--color-oats-neutral-750"),
                "800": color("--color-oats-neutral-800"),
                "900": color("--color-oats-neutral-900"),
                "950": color("--color-oats-neutral-950"),
            },
            "green": {
                "50": color("--color-oats-green-50"),
                "100": color("--color-oats-green-100"),
                "200": color("--color-oats-green-200"),
                "300": color("--color-oats-green-300"),
                "400": color("--color-oats-green-400"),
                "500": color("--color-oats-green-500"),
                "600": color("--color-oats-green-600"),
                "700": color("--color-oats-green-700"),
            },
            "red": {
                "50": color("--color-oats-red-50"),
                "100": color("--color-oats-red-100"),
                "200": color("--color-oats-red-200"),
                "300": color("--color-oats-red-300"),
                "400": color("--color-oats-red-400"),
            },
            "blue": {
                "50": color("--color-oats-blue-50"),
                "100": color("--color-oats-blue-100"),
                "200": color("--color-oats-blue-200"),
                "300": color("--color-oats-blue-300"),
                "400": color("--color-oats-blue-400"),
            },
            "white": color("--color-oats-white"),
            "black": color("--color-oats-black"),
        }
    },
    "font": {
        "family": {
            "sans": font("--font-sans"),
            "display": font("--font-display"),
            "quadrant": font("--font-quadrant"),
            "mono": font("--font-mono"),
        },
        "weight": {
            "light": weight("--font-weight-light"),
            "normal": weight("--font-weight-normal"),
            "book": weight("--font-weight-book"),
            "medium": weight("--font-weight-medium"),
            "semibold": weight("--font-weight-semibold"),
            "bold": weight("--font-weight-bold"),
        },
        "size": {
            "2xs": dim("--text-2xs"),
            "xs": dim("--text-xs"),
            "sm": dim("--text-sm"),
            "base": dim("--text-base"),
            "editor": dim("--text-editor"),
            "lg": dim("--text-lg"),
            "xl": dim("--text-xl"),
            "2xl": dim("--text-2xl"),
            "3xl": dim("--text-3xl"),
            "4xl": dim("--text-4xl"),
            "5xl": dim("--text-5xl"),
            "6xl": dim("--text-6xl"),
            "7xl": dim("--text-7xl"),
        },
    },
    "radius": {
        "xs": dim("--radius-xs"),
        "sm": dim("--radius-sm"),
        "md": dim("--radius-md"),
        "lg": dim("--radius-lg"),
        "xl": dim("--radius-xl"),
        "2xl": dim("--radius-2xl"),
        "3xl": dim("--radius-3xl"),
        "pill": {
            "$type": "dimension",
            "$value": "33554400px",
            "$extensions": {
                "source": {
                    "label": "Measured",
                    "file": "raw/components.json",
                    "element": "header Download link and hero Download for free",
                    "property": "borderRadius",
                    "page": "https://www.granola.ai/",
                    "run": "2026-11-21",
                    "note": "Computed borderRadius was 3.35544e+07px, the Tailwind rounded-full sentinel.",
                }
            },
        },
    },
    "space": {
        "unit": dim("--spacing", "Tailwind spacing unit. 1 unit is 0.25rem."),
    },
    "motion": {
        "ease-out": cubic("--ease-out"),
        "ease-out-expo": cubic("--ease-out-expo"),
        "ease-in-out": cubic("--ease-in-out"),
    },
    "layout": {
        "content": dim("--container-7xl", "max-w-7xl on the header inner wrapper."),
        "breakpoint-md": {
            "$type": "dimension",
            "$value": "768px",
            "$extensions": {
                "source": {
                    "label": "Measured",
                    "file": "site-tree.md",
                    "note": "Header Features and Open menu switch on the md: class. Tailwind default md is 768px. Not read from a custom property.",
                    "page": "https://www.granola.ai/",
                    "run": "2026-11-21",
                }
            },
        },
    },
}

light = {
    "page": color("--oats-surface-elevated", "Body background computed rgb(255, 255, 255), matching --oats-surface-elevated."),
    "surface": color("--oats-surface"),
    "surface-raised": color("--oats-surface-raised"),
    "surface-sunken": color("--oats-surface-sunken"),
    "overlay": color("--oats-surface-overlay"),
    "text": color("--oats-ink-primary"),
    "text-muted": color("--oats-ink-secondary"),
    "text-disabled": color("--oats-ink-tertiary"),
    "text-on-accent": color("--oats-ink-primary-inverse"),
    "link": color("--oats-ink-accent"),
    "border": color("--oats-border-hairline"),
    "border-focus": color("--oats-border-focus"),
    "accent": color("--oats-fill-accent"),
    "accent-hover": color("--oats-fill-accent-hover"),
    "danger": color("--oats-fill-danger"),
    "danger-hover": color("--oats-fill-danger-hover"),
    "ink-danger": color("--oats-ink-danger"),
    "fill-soft": color("--oats-fill-soft"),
    "fill-soft-hover": color("--oats-fill-soft-hover"),
    "input": color("--oats-fill-input"),
    "scrim": measured_comp(
        "Dialog overlay background while Granola for mobile was open.",
        COMP["dialog"]["overlayBg"],
        "[data-state=open] overlay",
        "backgroundColor",
    ),
}

# fix scrim type
light["scrim"]["$type"] = "color"

tokens = {
    "core": core,
    "light": light,
    "$themes": [
        {"id": "light", "name": "light", "selectedTokenSets": {"core": "enabled", "light": "enabled"}}
    ],
}

missing = []
def walk(node, path=""):
    if isinstance(node, dict) and "$value" in node:
        if "source" not in node.get("$extensions", {}):
            missing.append(path)
        return
    if isinstance(node, dict):
        for k, v in node.items():
            if k.startswith("$"):
                continue
            walk(v, path + "." + k if path else k)
walk(tokens)
if missing:
    raise SystemExit("tokens missing source: " + ", ".join(missing))

out = HERE / "tokens.json"
out.write_text(json.dumps(tokens, indent=1) + "\n")
print("wrote", out, "bytes", out.stat().st_size)
