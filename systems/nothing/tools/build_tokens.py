#!/usr/bin/env python3
"""Build tokens.json from raw/css-vars.json and raw/component-tokens.json.

Read from nothing.tech on 2026-11-21. The storefront declares one :root sheet.
html.dark does not change those custom properties (resolved light and dark
differ by 0). The dark set aliases the greyscale-dm tokens that the product
page paints with html.dark. Every token carries $extensions.source.
Unread values stay out of the file.
"""
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
V = json.loads((RAW / "css-vars.json").read_text())
SPEC = json.loads((RAW / "component-tokens.json").read_text())
DECL = {
    theme: {name: item.get("value") if isinstance(item, dict) else item
            for name, item in V["resolved"][theme].items()}
    for theme in ("light", "dark")
}

CHANNEL = re.compile(r"^(\d{1,3})\s+(\d{1,3})\s+(\d{1,3})$")
DIM = re.compile(r"-?\d+(\.\d+)?(px|rem)")


def norm_color(value):
    value = str(value).strip().lower()
    channel = CHANNEL.fullmatch(value)
    if channel:
        r, g, b = (int(x) for x in channel.groups())
        return "#%02x%02x%02x" % (r, g, b)
    match = re.fullmatch(r"#([0-9a-f]{3,8})", value)
    if match:
        hexes = match.group(1)
        if len(hexes) in (3, 4):
            hexes = "".join(ch * 2 for ch in hexes)
        r, g, b = (int(hexes[i:i + 2], 16) for i in (0, 2, 4))
        return "#%02x%02x%02x" % (r, g, b)
    match = re.fullmatch(r"rgba?\(\s*(\d+)[,\s]+(\d+)[,\s]+(\d+)\s*\)", value)
    if match:
        return "#%02x%02x%02x" % tuple(int(x) for x in match.groups())
    raise ValueError("not a colour: " + value)


def check(path, kind, value):
    if isinstance(value, str) and value.startswith("{"):
        return
    if kind == "dimension" and not DIM.fullmatch(str(value)):
        raise ValueError(f"{path}: dimension must be one px or rem length, got {value!r}")
    if kind == "color":
        norm_color(value)


def leaf(path, spec):
    kind = spec["type"]
    if "var" in spec:
        name = spec["var"]
        if name not in DECL["light"]:
            raise KeyError(f"{path}: {name} is not resolved in raw/css-vars.json")
        value = DECL["light"][name]
        if value in (None, ""):
            raise ValueError(f"{path}: {name} resolved empty")
        source = f"css-var {name} (light)"
        if spec.get("source"):
            source += "; " + spec["source"]
        if spec.get("channels"):
            value = norm_color(value)
            kind = "color"
    else:
        value = spec["value"]
        source = spec["source"]
    if kind == "color" and not str(value).startswith("{"):
        value = norm_color(value)
    check(path, kind, value)
    return {
        "$value": value,
        "$type": kind,
        "$extensions": {"source": source},
    }


def walk(node, prefix=""):
    out = {}
    for key, spec in node.items():
        if key.startswith("_"):
            continue
        path = f"{prefix}.{key}" if prefix else key
        if isinstance(spec, dict) and "type" in spec:
            out[key] = leaf(path, spec)
        elif isinstance(spec, dict):
            out[key] = walk(spec, path)
        else:
            raise ValueError(f"{path}: not a token spec")
    return out


def aliases(node, known, prefix=""):
    if not isinstance(node, dict):
        return
    if "$value" in node and isinstance(node["$value"], str):
        for ref in re.findall(r"\{([^{}]+)\}", node["$value"]):
            if ref not in known:
                raise KeyError(f"{prefix} aliases {{{ref}}}, which is not a token")
    else:
        for key, child in node.items():
            if not key.startswith("$"):
                aliases(child, known, f"{prefix}.{key}" if prefix else key)


def flatten(node, prefix=""):
    known = set()
    def walk_known(current, path):
        for key, child in current.items():
            if key.startswith("$"):
                continue
            here = f"{path}.{key}" if path else key
            if isinstance(child, dict) and "$value" in child:
                known.add(here)
            elif isinstance(child, dict):
                walk_known(child, here)
    walk_known(node, prefix)
    return known


core = walk(SPEC["core"])
light = walk(SPEC["light"])
dark = walk(SPEC["dark"])
known = flatten(core) | flatten(light) | flatten(dark)
aliases(core, known)
aliases(light, known)
aliases(dark, known)

doc = {
    "core": core,
    "light": light,
    "dark": dark,
    "$themes": [
        {"id": "light", "name": "Light", "selectedTokenSets": {"core": "source", "light": "enabled"}},
        {"id": "dark", "name": "Dark", "selectedTokenSets": {"core": "source", "dark": "enabled"}},
    ],
}
text = json.dumps(doc, indent=2) + "\n"
(HERE / "tokens.json").write_text(text)
print(f"wrote tokens.json ({text.count(chr(10))} lines)")
