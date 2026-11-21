#!/usr/bin/env python3
"""Build tokens.json from Lummi's measured CSS custom properties.

Sources, read signed-out from https://www.lummi.ai/ on 2026-11-21:
  raw/css-vars.json     declared custom properties (HSL triplets on :root)
  raw/live-colors.json  those triplets resolved to sRGB on the live homepage

The public site paints light by default and dark when prefers-color-scheme is
dark and html has no data-theme="light". The *-dark names are the dark set.
Every token carries $extensions.source. Unread values are not invented.
"""
import json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
COLORS = json.loads((RAW / "live-colors.json").read_text())["out"]


def rgb_to_hex(v):
    m = re.fullmatch(r"rgb\((\d+), (\d+), (\d+)\)", v.strip())
    if not m:
        raise ValueError(v)
    return "#%02x%02x%02x" % tuple(int(m.group(i)) for i in (1, 2, 3))


def color(name, theme):
    key = name if theme == "light" or name in DARK_SAME else name + "-dark"
    rec = COLORS[key]
    if rec["kind"] != "color":
        raise KeyError(key)
    note = "same value in dark; no --yellow-dark declaration" if theme == "dark" and name in DARK_SAME else theme
    return {
        "$value": rgb_to_hex(rec["value"]),
        "$type": "color",
        "$extensions": {
            "source": f"Measured: getComputedStyle on https://www.lummi.ai/ resolved hsl({rec['raw']}) from custom property {key} ({note})",
        },
    }


def dim(value, source):
    return {"$value": value, "$type": "dimension", "$extensions": {"source": source}}


def font(value, source):
    return {"$value": value, "$type": "fontFamily", "$extensions": {"source": source}}


S = "Measured: computed style on https://www.lummi.ai/ at 1440x900, signed out, 2026-11-21 (raw/live-resolved.json)"

core = {
    "font": {
        "family": {
            "sans": font('Inter, "Inter Fallback"', S + "; body fontFamily"),
        },
        "size": {
            "display": dim("141.12px", S + "; h1 fontSize, fluid at 1440"),
            "body": dim("16px", S + "; body fontSize"),
            "label": dim("14px", S + "; search input and Try Pro button fontSize"),
        },
        "lineHeight": {
            "display": dim("144px", S + "; h1 lineHeight"),
            "body": dim("24px", S + "; body lineHeight"),
            "label": dim("24px", S + "; button lineHeight"),
        },
        "weight": {
            "regular": {"$value": 400, "$type": "fontWeight", "$extensions": {"source": S + "; body fontWeight"}},
            "medium": {"$value": 500, "$type": "fontWeight", "$extensions": {"source": S + "; Try Pro button fontWeight"}},
            "semibold": {"$value": 600, "$type": "fontWeight", "$extensions": {"source": S + "; h1 fontWeight"}},
        },
        "tracking": {
            "display": dim("-7.056px", S + "; h1 letterSpacing at 1440"),
        },
    },
    "radius": {
        "sm": dim("4px", "Measured: --radius computes to 4px (0.25rem) on :root; Try Pro button borderRadius is 4px"),
    },
    "space": {
        "3": dim("12px", S + "; Try Pro button padding-inline"),
    },
    "size": {
        "control": dim("40px", S + "; Try Pro button height"),
        "field": dim("38px", S + "; search input height"),
    },
    "typography": {
        "display": {
            "$type": "typography",
            "$value": {
                "fontFamily": "{font.family.sans}",
                "fontSize": "{font.size.display}",
                "fontWeight": "{font.weight.semibold}",
                "lineHeight": "{font.lineHeight.display}",
                "letterSpacing": "{font.tracking.display}",
            },
            "$extensions": {"source": "Derived: h1 computed style on the homepage hero"},
        },
        "body": {
            "$type": "typography",
            "$value": {
                "fontFamily": "{font.family.sans}",
                "fontSize": "{font.size.body}",
                "fontWeight": "{font.weight.regular}",
                "lineHeight": "{font.lineHeight.body}",
            },
            "$extensions": {"source": "Derived: body computed style"},
        },
        "label": {
            "$type": "typography",
            "$value": {
                "fontFamily": "{font.family.sans}",
                "fontSize": "{font.size.label}",
                "fontWeight": "{font.weight.medium}",
                "lineHeight": "{font.lineHeight.label}",
            },
            "$extensions": {"source": "Derived: Try Pro button and search field computed style"},
        },
    },
}

ROLES = [
    ("page", "--background"),
    ("surface", "--card"),
    ("popover", "--popover"),
    ("text", "--foreground"),
    ("text-on-surface", "--card-foreground"),
    ("text-on-popover", "--popover-foreground"),
    ("muted", "--muted-foreground"),
    ("muted-surface", "--muted"),
    ("faint", "--faint-foreground"),
    ("faint-surface", "--faint"),
    ("accent", "--primary"),
    ("accent-foreground", "--primary-foreground"),
    ("accent-hover", "--primary-hover"),
    ("secondary", "--secondary"),
    ("secondary-foreground", "--secondary-foreground"),
    ("secondary-hover", "--secondary-hover"),
    ("accent-quiet", "--accent"),
    ("accent-quiet-foreground", "--accent-foreground"),
    ("destructive", "--destructive"),
    ("destructive-foreground", "--destructive-foreground"),
    ("destructive-hover", "--destructive-hover"),
    ("border", "--border"),
    ("input", "--input"),
    ("focus", "--ring"),
    ("highlight", "--highlight"),
    ("yellow", "--yellow"),
]

# --yellow has no --yellow-dark declaration. Dark uses the same measured yellow.
DARK_SAME = {"--yellow"}


def semantic(theme):
    out = {}
    for token, var in ROLES:
        out[token] = color(var, theme)
    return out


def nest(flat):
    """Group related colours. Catalog paths stay flat tokens.

    catalog.json on main names light.text, light.textMuted, light.accent and
    light.border as colour values. The catalog resolver stops at the first
    $value, so those names cannot also be groups. Related colours sit under
    ink, brand and line. This capture does not edit catalog.json.
    """
    groups = {
        "page": "page",
        "surface": "surface",
        "popover": "popover",
        "text": "text",
        "text-on-surface": "ink.on-surface",
        "text-on-popover": "ink.on-popover",
        "muted": "textMuted",
        "muted-surface": "surface.muted",
        "faint": "ink.faint",
        "faint-surface": "surface.faint",
        "accent": "accent",
        "accent-foreground": "brand.foreground",
        "accent-hover": "brand.hover",
        "secondary": "brand.secondary",
        "secondary-foreground": "brand.secondary-foreground",
        "secondary-hover": "brand.secondary-hover",
        "accent-quiet": "brand.quiet",
        "accent-quiet-foreground": "brand.quiet-foreground",
        "destructive": "status.destructive",
        "destructive-foreground": "status.destructive-foreground",
        "destructive-hover": "status.destructive-hover",
        "border": "border",
        "input": "line.input",
        "focus": "focus",
        "highlight": "highlight",
        "yellow": "status.yellow",
    }
    tree = {}
    for src, dest in groups.items():
        node = tree
        parts = dest.split(".")
        for p in parts[:-1]:
            node = node.setdefault(p, {})
        node[parts[-1]] = flat[src]
    return tree


light = nest(semantic("light"))
dark = nest(semantic("dark"))

tokens = {
    "core": core,
    "light": light,
    "dark": dark,
    "$themes": [
        {"id": "light", "name": "Light", "selectedTokenSets": {"core": "source", "light": "enabled"}},
        {"id": "dark", "name": "Dark", "selectedTokenSets": {"core": "source", "dark": "enabled"}},
    ],
    "$metadata": {"tokenSetOrder": ["core", "light", "dark"]},
}

(HERE / "tokens.json").write_text(json.dumps(tokens, indent=2) + "\n")
print("wrote tokens", sum(1 for _ in json.dumps(tokens)))
