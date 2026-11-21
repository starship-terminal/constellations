#!/usr/bin/env python3
"""Build tokens.json from raw/css-vars.json and raw/component-tokens.json.

getfernand.com paints one light theme. Brand colours are the site's --* custom
properties. WordPress --wp--preset--* names are not the product palette and are
left out. Deterministic: same inputs, same bytes.
"""
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
V = json.loads((RAW / "css-vars.json").read_text())
SPEC = json.loads((RAW / "component-tokens.json").read_text())
DECL = {n: v.get("value", "") for n, v in V["resolved"]["light"].items()}


def norm_color(v):
    v = str(v).strip().lower()
    m = re.fullmatch(r"#([0-9a-f]{3,8})", v)
    if m:
        h = m.group(1)
        if len(h) in (3, 4):
            h = "".join(c * 2 for c in h)
        r, g, b = (int(h[i:i + 2], 16) for i in (0, 2, 4))
        return "#%02x%02x%02x" % (r, g, b)
    m = re.fullmatch(r"rgba?\(\s*(\d+)[,\s]+(\d+)[,\s]+(\d+)(?:\s*[,/]\s*([\d.]+))?\s*\)", v)
    if m:
        r, g, b, a = m.groups()
        if a is None or float(a) == 1:
            return "#%02x%02x%02x" % (int(r), int(g), int(b))
        return "rgba(%s, %s, %s, %g)" % (r, g, b, float(a))
    raise ValueError("not a colour: " + v)


DIM = re.compile(r"-?\d+(\.\d+)?(px|rem)")


def check(path, ty, val):
    if isinstance(val, str) and val.startswith("{"):
        return
    if ty == "dimension" and not DIM.fullmatch(str(val)):
        raise ValueError(f"{path}: dimension {val!r}")
    if ty == "color":
        norm_color(val)
    if ty == "fontFamily" and not isinstance(val, str):
        raise ValueError(f"{path}: fontFamily {val!r}")


def leaf(path, spec):
    ty = spec["type"]
    if "var" in spec:
        name = spec["var"]
        if name not in DECL or not DECL[name]:
            raise KeyError(f"{path}: {name} is not a resolved variable")
        val = DECL[name]
        src = f"css-var {name} on :root at https://getfernand.com/"
        if spec.get("source"):
            src += "; " + spec["source"]
    else:
        val = spec["value"]
        src = spec["source"]
    if ty == "color" and not str(val).startswith("{"):
        val = norm_color(val)
    check(path, ty, val)
    token = {"$value": val, "$type": ty, "$extensions": {"source": src}}
    if spec.get("description"):
        token["$description"] = spec["description"]
    return token


def build(node, path=""):
    if isinstance(node, dict) and "type" in node and ("value" in node or "var" in node):
        return leaf(path, node)
    return {k: build(v, f"{path}.{k}" if path else k) for k, v in node.items() if not k.startswith("_")}


core = build(SPEC["core"])
light = build(SPEC["light"])


def tokens_of(tree, prefix=""):
    for k, v in tree.items():
        if isinstance(v, dict) and "$value" in v:
            yield prefix + k, v
        elif isinstance(v, dict):
            yield from tokens_of(v, prefix + k + ".")


NAMES = {n for n, _ in tokens_of(core)} | {n for n, _ in tokens_of(light)}


def aliases(v):
    if isinstance(v, str):
        return re.findall(r"\{([^{}]+)\}", v)
    if isinstance(v, dict):
        return [a for x in v.values() for a in aliases(x)]
    if isinstance(v, list):
        return [a for x in v for a in aliases(x)]
    return []


for scope, tree in (("core", core), ("light", light)):
    for n, t in tokens_of(tree):
        for a in aliases(t["$value"]):
            if a not in NAMES:
                raise KeyError(f"{scope}.{n}: alias {{{a}}} points at nothing")

tokens = {
    "core": core,
    "light": light,
    "$themes": [
        {"id": "light", "name": "Light", "selectedTokenSets": {"core": "source", "light": "enabled"},
         "$description": "The only theme getfernand.com paints on the public site. No dark theme switch was found."},
    ],
    "$metadata": {"tokenSetOrder": ["core", "light"]},
}
(HERE / "tokens.json").write_text(json.dumps(tokens, indent=2, ensure_ascii=False) + "\n")
print("wrote", {k: sum(1 for _ in tokens_of(v)) for k, v in tokens.items() if k in ("core", "light")})
