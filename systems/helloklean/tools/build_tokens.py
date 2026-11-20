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
C = json.loads((RAW / "components-computed.json").read_text())
C = C.get("components", C)
FONTS = {(f["family"], f["weight"]) for f in V["fonts"]}


def computed(comp, prop, state="default"):
    """A computed style read on a component; raises when the reading is missing."""
    v = (C[comp]["states"][state].get("style") or {}).get(prop)
    if not v:
        raise KeyError(f"{comp} {state}: no {prop} reading")
    return v


def line_ratio(comp):
    """lineHeight / fontSize of a measured component, e.g. 41.8px / 38px -> 1.1."""
    lh, fs = computed(comp, "lineHeight"), computed(comp, "fontSize")
    return round(float(lh.removesuffix("px")) / float(fs.removesuffix("px")), 3)


def loaded(family, weight):
    if (family, str(weight)) not in FONTS:
        raise KeyError(f"{family} {weight} is not in raw/css-vars.json fonts")
    return weight


HAND = "Reconstruction — entered by hand at capture time, no raw reading behind it"


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
        "regular": tok(loaded("HKRepro", 400), "fontWeight", "HKRepro 400 loaded (raw/css-vars.json fonts)"),
        "medium": tok(loaded("HKRepro", 500), "fontWeight", "HKRepro 500 loaded (raw/css-vars.json fonts)"),
    },
    "typography": {
        # Sizes are the declared :root vars. A line height is measured only where a component
        # was read at that size (hero-title is heading-1); the rest were entered by hand.
        "heading-1": tok({"fontFamily": "{fontFamily.display}", "fontSize": "{fontSize.heading-1}", "fontWeight": "{fontWeight.regular}", "lineHeight": line_ratio("hero-title")}, "typography", SRC + " --heading-1; lineHeight computed on hero-title default (" + computed("hero-title", "lineHeight") + " / " + computed("hero-title", "fontSize") + ", raw/components-computed.json)"),
        "heading-2": tok({"fontFamily": "{fontFamily.display}", "fontSize": "{fontSize.heading-2}", "fontWeight": "{fontWeight.regular}", "lineHeight": 1.15}, "typography", SRC + " --heading-2; lineHeight " + HAND),
        "heading-3": tok({"fontFamily": "{fontFamily.display}", "fontSize": "{fontSize.heading-3}", "fontWeight": "{fontWeight.regular}", "lineHeight": 1.2}, "typography", SRC + " --heading-3; lineHeight " + HAND),
        "heading-4": tok({"fontFamily": "{fontFamily.display}", "fontSize": "{fontSize.heading-4}", "fontWeight": "{fontWeight.medium}", "lineHeight": 1.3}, "typography", SRC + " --heading-4; fontWeight and lineHeight " + HAND),
        "body": tok({"fontFamily": "{fontFamily.body}", "fontSize": "{fontSize.body}", "fontWeight": "{fontWeight.regular}", "lineHeight": 1.5}, "typography", SRC + " --body; lineHeight " + HAND),
        # The hero CTA (a primary button at the declared 14px) measures weight 400 and a 14px line.
        "button": tok({"fontFamily": "{fontFamily.body}", "fontSize": "{fontSize.button}", "fontWeight": "{fontWeight.regular}" if computed("hero-cta", "fontWeight") == "400" else "{fontWeight.medium}", "lineHeight": line_ratio("hero-cta")}, "typography", SRC + " --button-font-size; fontWeight and lineHeight computed on hero-cta default (" + computed("hero-cta", "fontWeight") + ", " + computed("hero-cta", "lineHeight") + ", raw/components-computed.json)"),
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
        "muted": {"$value": "#6e6e73", "$type": "color", "$extensions": {"source": HAND + " (the shop-card subtitle colour on /en-int/collections/hello-klean-2-0; no component reading or :root property holds it)"}},
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

# Aliases name the token path without its set ({color.ink}, not {core.color.ink}): that is
# how DTCG and Tokens Studio resolve them across sets.

if (RAW / "motion.json").exists():
    import sys
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
    import motion
    core["motion"], _motion_skipped = motion.build(json.loads((RAW / "motion.json").read_text()))
    if _motion_skipped:
        core["$extensions"] = {"notTokenised": _motion_skipped}

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
for n, t in list(walk(core)) + list(walk(light)):
    for a in re.findall(r"\{([^{}]+)\}", json.dumps(t["$value"])):
        if a not in names:
            raise KeyError(f"{n}: alias {{{a}}} points at nothing")

def count(d):
    return sum(count(v) for k, v in d.items() if not k.startswith("$")) if isinstance(d, dict) and "$value" not in d else 1


if __name__ == "__main__":
    (HERE / "tokens.json").write_text(json.dumps(tokens, indent=2, ensure_ascii=False) + "\n")
    print({k: count(v) for k, v in tokens.items() if k in ("core", "light")})
