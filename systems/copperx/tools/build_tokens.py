#!/usr/bin/env python3
"""Build tokens.json from Copperx's measured public surface.

Copperx does not publish a design-token custom-property layer. The marketing
site is Tailwind utility classes, so every value here is a computed style
read on copperx.io on 2026-11-18 (raw/foundations.json) or a duration read
by the motion probe (raw/motion.json, when present).

One light theme. Dark is not a published theme on the signed-out site.
Deterministic: same inputs, same bytes.
"""
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent
RAW = ROOT / "raw"
sys.path.insert(0, str(HERE))

F = json.loads((RAW / "foundations.json").read_text())


def color(value, source, description=""):
    tok = {
        "$value": value,
        "$type": "color",
        "$extensions": {"source": source},
    }
    if description:
        tok["$description"] = description
    return tok


def dim(value, source, description=""):
    tok = {
        "$value": value,
        "$type": "dimension",
        "$extensions": {"source": source},
    }
    if description:
        tok["$description"] = description
    return tok


def typography(family, size, weight, line, tracking, source):
    return {
        "$value": {
            "fontFamily": family,
            "fontSize": size,
            "fontWeight": weight,
            "lineHeight": line,
            "letterSpacing": tracking,
        },
        "$type": "typography",
        "$extensions": {"source": source},
    }


def shadow(source):
    return {
        "$value": [{
            "color": "rgba(0, 0, 0, 0.06)",
            "offsetX": "0px",
            "offsetY": "1px",
            "blur": "2px",
            "spread": "0px",
        }, {
            "color": "rgba(106, 115, 133, 0.16)",
            "offsetX": "0px",
            "offsetY": "0px",
            "blur": "0px",
            "spread": "1px",
        }],
        "$type": "shadow",
        "$extensions": {"source": source},
    }


SRC = "computed on https://copperx.io/ 2026-11-18 (raw/foundations.json)"

core = {
    "color": {
        "ink": color("#13171f", SRC, "Button label on the light control. rgb(19, 23, 31)."),
        "ink-strong": color("#1e232e", SRC, "Hero headline and the dark button's hover. rgb(30, 35, 46)."),
        "body": color("#6a7385", SRC, "Secondary copy. rgb(106, 115, 133)."),
        "muted": color("#8d9097", SRC, "Menu description copy. rgb(141, 144, 151)."),
        "indigo": color("#4c63ed", SRC, "The word Stablecoin in the hero, Tailwind text-indigo-500. rgb(76, 99, 237)."),
        "indigo-link": color("#5f76f9", SRC, "Menu link colour, Tailwind text-indigo-400. rgb(95, 118, 249)."),
        "indigo-deep": color("#3e50b7", SRC, "Painted indigo block. rgb(62, 80, 183)."),
        "teal": color("#2e9fb2", SRC, "Painted teal block. rgb(46, 159, 178)."),
        "paper": color("#f7f9fc", SRC, "Light button hover and the cool page wash. rgb(247, 249, 252)."),
        "line": color("#bcc3d1", SRC, "Default border colour the buttons inherit. rgb(188, 195, 209)."),
        "white": color("#ffffff", SRC, "Page and header."),
        "black": color("#000000", SRC, "Primary button fill."),
        "focus": color("#005fcc", SRC, "Browser focus outline on the header buttons. rgb(0, 95, 204)."),
    },
    "font": {
        "family": {
            "sans": {
                "$value": "Euclid Circular A",
                "$type": "fontFamily",
                "$extensions": {"source": SRC},
                "$description": "The marketing site sets Euclid Circular A on headings, body and buttons. The files are proprietary and are not shipped. Fall back to ui-sans-serif.",
            }
        }
    },
    "typography": {
        "display": typography("Euclid Circular A", "96px", 500, "96px", "-3.84px", SRC + " h1"),
        "title": typography("Euclid Circular A", "48px", 500, "52px", "-1.2px", SRC + " product h1"),
        "heading": typography("Euclid Circular A", "16px", 500, "24px", "0px", SRC + " menu heading"),
        "body": typography("Euclid Circular A", "16px", 400, "24px", "0px", SRC + " nav"),
        "ui": typography("Euclid Circular A", "14px", 500, "20px", "0px", SRC + " button"),
        "caption": typography("Euclid Circular A", "14px", 400, "19.6px", "0px", SRC + " menu description"),
    },
    "radius": {
        "control": dim("8px", SRC + " .btn"),
        "panel": dim("16px", SRC + " rounded-2xl menu panel"),
    },
    "spacing": {
        "2": dim("8px", SRC + " button padding-block"),
        "3": dim("12px", SRC + " button padding-inline"),
        "4": dim("16px", SRC + " derived 4px step"),
        "6": dim("24px", SRC + " derived 4px step"),
    },
    "size": {
        "button": dim("36px", SRC + " .btn height"),
        "header": dim("85px", SRC + " header height"),
    },
    "elevation": {
        "control": shadow(SRC + " .btn box-shadow"),
    },
}

light = {
    "background": {
        "page": color("{color.white}", SRC, "Header and page field."),
        "wash": color("{color.paper}", SRC, "Light button hover and cool section wash."),
        "inverse": color("{color.black}", SRC, "Primary button."),
    },
    "text": {
        "primary": color("{color.ink-strong}", SRC, "Headlines."),
        "body": color("{color.body}", SRC, "Secondary copy."),
        "muted": color("{color.muted}", SRC, "Descriptions."),
        "inverse": color("{color.white}", SRC, "Label on the black button."),
        "link": color("{color.indigo-link}", SRC, "Menu links."),
    },
    "accent": {
        "default": color("{color.indigo}", SRC),
        "deep": color("{color.indigo-deep}", SRC),
        "teal": color("{color.teal}", SRC),
    },
    "border": {
        "default": color("rgba(0, 0, 0, 0.12)", SRC + " header border-bottom"),
        "control": color("rgba(106, 115, 133, 0.16)", SRC + " button ring"),
        "focus": color("{color.focus}", SRC),
    },
    "action": {
        "primary": color("{color.black}", SRC),
        "primary-hover": color("{color.ink-strong}", SRC),
        "secondary": color("{color.white}", SRC),
        "secondary-hover": color("{color.paper}", SRC),
    },
    "component": {
        "button": {
            "bg": color("{color.black}", SRC),
            "text": color("{color.white}", SRC),
            "radius": dim("8px", SRC),
            "height": dim("36px", SRC),
        },
        "button-secondary": {
            "bg": color("{color.white}", SRC),
            "text": color("{color.ink}", SRC),
            "radius": dim("8px", SRC),
        },
    },
}

tokens = {
    "core": core,
    "light": light,
    "$themes": [{
        "id": "light",
        "name": "light",
        "selectedTokenSets": {"core": "source", "light": "enabled"},
    }],
    "$metadata": {
        "tokenSetOrder": ["core", "light"],
    },
}

motion_path = RAW / "motion.json"
if motion_path.exists():
    import motion
    group = motion.build(json.loads(motion_path.read_text()))
    # motion.build returns [description, group, notTokenised].
    if isinstance(group, (list, tuple)) and len(group) >= 2 and isinstance(group[1], dict):
        tokens["core"]["motion"] = group[1]
    elif isinstance(group, dict):
        tokens["core"]["motion"] = group

(ROOT / "tokens.json").write_text(json.dumps(tokens, indent=2) + "\n")
print("wrote", ROOT / "tokens.json")
