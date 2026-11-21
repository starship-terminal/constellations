#!/usr/bin/env python3
"""Build tokens.json from raw/component-tokens.json.

Dopper publishes no design-token custom properties. Every leaf in the spec is a
computed style read on 2026-11-21, except color.green, which is sampled from the
Filters pill before quantize because the stylesheet does not name it.

Light only. No dark theme was found. Deterministic.
"""
import json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent.parent
SPEC = json.loads((HERE / "raw" / "component-tokens.json").read_text())

DIM = re.compile(r"-?\d+(\.\d+)?(px|rem)")


def norm_color(v):
    v = v.strip().lower()
    m = re.fullmatch(r"#([0-9a-f]{6})", v)
    if not m:
        raise ValueError("not a colour: " + v)
    return "#" + m.group(1)


def leaf(path, spec):
    if not spec.get("source"):
        raise ValueError(path + ": leaf without a source")
    ty, val = spec["type"], spec["value"]
    if ty == "color":
        val = norm_color(val)
    if ty == "dimension" and not DIM.fullmatch(str(val)):
        raise ValueError(f"{path}: dimension {val!r}")
    if ty == "fontWeight" and not isinstance(val, int):
        raise ValueError(f"{path}: fontWeight {val!r}")
    token = {"$type": ty if ty != "fontFamily" else "fontFamily", "$value": val,
             "$extensions": {"source": spec["source"]}}
    if ty == "fontFamily":
        token["$type"] = "fontFamily"
    return token


def walk(node, prefix=""):
    out = {}
    for k, v in node.items():
        path = f"{prefix}.{k}" if prefix else k
        if isinstance(v, dict) and "type" in v:
            out[k] = leaf(path, v)
        elif isinstance(v, dict):
            out[k] = walk(v, path)
        else:
            raise ValueError(path)
    return out


core = walk(SPEC)
light = {
    "background": {
        "page": {"$type": "color", "$value": "{color.paper}", "$extensions": {"source": "alias of measured page background"}},
        "surface": {"$type": "color", "$value": "{color.paper}", "$extensions": {"source": "alias of measured page background"}},
        "hero": {"$type": "color", "$value": "{color.blue}", "$extensions": {"source": "alias of measured accent; hero field is a photograph on blue"}},
        "raised": {"$type": "color", "$value": "#cce2ff", "$extensions": {"source": "sampled filter sheet ground (204, 226, 255) on shop-bottles-light-filters.png before quantize"}},
    },
    "text": {
        "primary": {"$type": "color", "$value": "{color.ink}", "$extensions": {"source": "alias of measured shop body color"}},
        "on-hero": {"$type": "color", "$value": "{color.cream}", "$extensions": {"source": "alias of measured hero h1 color"}},
        "on-accent": {"$type": "color", "$value": "{color.cream-deep}", "$extensions": {"source": "alias of measured add-to-cart text"}},
        "link": {"$type": "color", "$value": "{color.blue}", "$extensions": {"source": "alias of measured a.level-top color"}},
    },
    "action": {
        "primary": {"$type": "color", "$value": "{color.blue}", "$extensions": {"source": "alias of measured button.tocart background"}},
        "ink": {"$type": "color", "$value": "{color.black}", "$extensions": {"source": "alias of measured marketing primary button fill, observed on home hero"}},
    },
    "border": {
        "focus": {"$type": "color", "$value": "{color.focus-ring}", "$extensions": {"source": "alias of measured focus outline"}},
    },
}

doc = {
    "core": core,
    "light": light,
    "$themes": [{"id": "light", "name": "Light", "selectedTokenSets": {"core": "source", "light": "enabled"}}],
}
text = json.dumps(doc, indent=2) + "\n"
(HERE / "tokens.json").write_text(text)
print("wrote tokens.json", text.count("\n"), "lines")
