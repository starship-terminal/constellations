#!/usr/bin/env python3
"""Build tokens.json from Hello Klean's raw/css-vars.json.

The site declares one light token layer on :root (Shopify theme BF26 /
Quickfire 3.0): a near-black ink (#1d1d1f) and a warm paper (#f5f4f1), a
heading scale, and a three-button matrix with 25px pill radii. There is no
dark scope. Motion, when raw/motion.json exists, is summarised into
core.motion by the kit's motion.py when that file's shape matches; this
builder writes the declared layer either way.

Deterministic: same inputs, same bytes.
"""
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
V = json.loads((RAW / "css-vars.json").read_text())
DECL = {n: d["value"] for n, d in V["resolved"]["light"].items()}


def color(name, source):
    val = DECL[name]
    if not re.fullmatch(r"#[0-9a-fA-F]{6}|rgba?\([^)]+\)|transparent", val.strip()):
        raise ValueError(f"{name}: not a colour: {val}")
    return {"$value": val.strip().lower() if val.startswith("#") else val.strip(), "$type": "color",
            "$extensions": {"source": source}}


def dim(name, source):
    val = DECL[name].strip()
    if not re.fullmatch(r"-?\d+(\.\d+)?(px|rem)", val):
        raise ValueError(f"{name}: not a length: {val}")
    return {"$value": val, "$type": "dimension", "$extensions": {"source": source}}


def tok(value, ty, source, description=None):
    t = {"$value": value, "$type": ty, "$extensions": {"source": source}}
    if description:
        t["$description"] = description
    return t


SRC = "css-var on :root, resolved on helloklean.com/en-int (light)"

core = {
    "color": {
        "ink": color("--primary-color", SRC + " --primary-color"),
        "paper": color("--secondary-color", SRC + " --secondary-color"),
        "white": color("--text-alternate-color", SRC + " --text-alternate-color"),
    },
    "fontFamily": {
        "display": tok("HKRepro, 'DM Sans', sans-serif", "fontFamily",
                       "document.fonts on /en-int: HKRepro 400 and 500 loaded; DM Sans declared as fallback"),
        "body": tok("'DM Sans', sans-serif", "fontFamily",
                    "document.fonts on /en-int lists DM Sans 400/500/700"),
    },
    "fontWeight": {
        "regular": tok(400, "fontWeight", "HKRepro 400 loaded"),
        "medium": tok(500, "fontWeight", "HKRepro 500 loaded"),
    },
    "typography": {
        "heading-1": tok({"fontFamily": "{fontFamily.display}", "fontSize": "{fontSize.heading-1}", "fontWeight": "{fontWeight.regular}", "lineHeight": 1.1}, "typography", SRC + " --heading-1"),
        "heading-2": tok({"fontFamily": "{fontFamily.display}", "fontSize": "{fontSize.heading-2}", "fontWeight": "{fontWeight.regular}", "lineHeight": 1.15}, "typography", SRC + " --heading-2"),
        "heading-3": tok({"fontFamily": "{fontFamily.display}", "fontSize": "{fontSize.heading-3}", "fontWeight": "{fontWeight.regular}", "lineHeight": 1.2}, "typography", SRC + " --heading-3"),
        "heading-4": tok({"fontFamily": "{fontFamily.display}", "fontSize": "{fontSize.heading-4}", "fontWeight": "{fontWeight.medium}", "lineHeight": 1.3}, "typography", SRC + " --heading-4"),
        "body": tok({"fontFamily": "{fontFamily.body}", "fontSize": "{fontSize.body}", "fontWeight": "{fontWeight.regular}", "lineHeight": 1.5}, "typography", SRC + " --body"),
        "button": tok({"fontFamily": "{fontFamily.body}", "fontSize": "{fontSize.button}", "fontWeight": "{fontWeight.medium}", "lineHeight": 1.2}, "typography", SRC + " --button-font-size"),
    },
    "fontSize": {
        "heading-1": dim("--heading-1", SRC + " --heading-1"),
        "heading-2": dim("--heading-2", SRC + " --heading-2"),
        "heading-3": dim("--heading-3", SRC + " --heading-3"),
        "heading-4": dim("--heading-4", SRC + " --heading-4"),
        "heading-1-mobile": dim("--heading-1-mobile", SRC + " --heading-1-mobile"),
        "heading-2-mobile": dim("--heading-2-mobile", SRC + " --heading-2-mobile"),
        "heading-3-mobile": dim("--heading-3-mobile", SRC + " --heading-3-mobile"),
        "body": dim("--body", SRC + " --body"),
        "button": dim("--button-font-size", SRC + " --button-font-size"),
    },
    "radius": {
        "button": dim("--button-1-radius", SRC + " --button-1-radius"),
    },
    "spacing": {
        "button-x": dim("--button-h-padding", SRC + " --button-h-padding"),
        "button-y": dim("--button-v-padding", SRC + " --button-v-padding"),
    },
}

light = {
    "background": {
        "page": {"$value": "{color.paper}", "$type": "color", "$extensions": {"source": "alias of core.color.paper (--secondary-color)"}},
        "inverse": {"$value": "{color.ink}", "$type": "color", "$extensions": {"source": "alias of core.color.ink (--primary-color); announcement bar and primary buttons"}},
        "card": {"$value": "{color.white}", "$type": "color", "$extensions": {"source": "alias of core.color.white (--text-alternate-color)"}},
    },
    "text": {
        "primary": {"$value": "{color.ink}", "$type": "color", "$extensions": {"source": "alias of --text-primary-color"}},
        "inverse": {"$value": "{color.paper}", "$type": "color", "$extensions": {"source": "alias of --button-1-text-color"}},
        "on-inverse": {"$value": "{color.white}", "$type": "color", "$extensions": {"source": "alias of --text-alternate-color"}},
        "muted": {"$value": "#6e6e73", "$type": "color", "$extensions": {"source": "computed color of the shop-card subtitle on /en-int/collections/hello-klean-2-0; not a :root custom property"}},
    },
    "border": {
        "default": {"$value": "{color.ink}", "$type": "color", "$extensions": {"source": "alias of --button-1-border-color"}},
        "quiet": {"$value": "{color.paper}", "$type": "color", "$extensions": {"source": "alias of --button-2-border-color"}},
    },
    "action": {
        "primary-bg": color("--button-1-color", SRC + " --button-1-color"),
        "primary-text": color("--button-1-text-color", SRC + " --button-1-text-color"),
        "primary-hover-bg": color("--button-1-hover-color", SRC + " --button-1-hover-color"),
        "primary-hover-text": color("--button-1-hover-text-color", SRC + " --button-1-hover-text-color"),
        "secondary-bg": color("--button-2-color", SRC + " --button-2-color"),
        "secondary-text": color("--button-2-text-color", SRC + " --button-2-text-color"),
        "secondary-hover-bg": color("--button-2-hover-color", SRC + " --button-2-hover-color"),
        "ghost-text": color("--button-3-text-color", SRC + " --button-3-text-color"),
        "ghost-hover-bg": color("--button-3-hover-color", SRC + " --button-3-hover-color"),
    },
    "focus": {
        "ring": {"$value": "{color.ink}", "$type": "color", "$extensions": {"source": "no authored focus token; browser outline on ink, recorded as the ink role"}},
    },
}

# Fix aliases: color.* lives under core, so alias paths from light need the set.
# Tokens Studio aliases are relative to the token tree root of the exported file
# when written as {core.color.ink}. Rewrite the short aliases.
def rewrite(node):
    if isinstance(node, dict):
        if "$value" in node and isinstance(node["$value"], str):
            node["$value"] = re.sub(r"\{(color|fontFamily|fontWeight|fontSize)\.", r"{core.\1.", node["$value"])
        for v in node.values():
            rewrite(v)
    return node

rewrite(core)
rewrite(light)

if (RAW / "motion.json").exists():
    import sys
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
    import motion
    core["motion"], _motion_skipped = motion.build(json.loads((RAW / "motion.json").read_text()))

tokens = {
    "core": core,
    "light": light,
    "$themes": [{
        "id": "light",
        "name": "Light",
        "selectedTokenSets": {"core": "source", "light": "enabled"},
        "$description": "Hello Klean paints one light theme: warm paper #f5f4f1, near-black ink #1d1d1f, pill buttons at 25px radius. No dark scope exists.",
    }],
    "$metadata": {"tokenSetOrder": ["core", "light"]},
}

# Alias check
def walk(tree, prefix=""):
    for k, v in tree.items():
        if isinstance(v, dict) and "$value" in v:
            yield prefix + k, v
        elif isinstance(v, dict):
            yield from walk(v, prefix + k + ".")

names = {n for n, _ in walk(core)} | {n for n, _ in walk(light)}
# aliases use core. prefix which is a set name, not a token path. Accept both.
all_names = names | {"core." + n for n in names if not n.startswith("core.")}
for n, t in list(walk(core)) + list(walk(light)):
    for a in re.findall(r"\{([^{}]+)\}", json.dumps(t["$value"])):
        if a not in names and a not in all_names and not a.startswith("core."):
            raise KeyError(f"{n}: alias {{{a}}} points at nothing")

(HERE / "tokens.json").write_text(json.dumps(tokens, indent=2, ensure_ascii=False) + "\n")


def count(d):
    return sum(count(v) for v in d.values()) if isinstance(d, dict) and "$value" not in d else 1

print({k: count(v) for k, v in tokens.items() if k in ("core", "light")})
