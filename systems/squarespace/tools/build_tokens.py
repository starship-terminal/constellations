#!/usr/bin/env python3
"""Build tokens.json from systems/squarespace/raw/component-tokens.json.

Squarespace's marketing CSS is cross-origin, so vars.mjs could not read custom
properties from the CSSOM (raw/foundations.json records varCount 0). Every
token here is a computed style read on a live element on 2026-11-21, or a
derivation of one of those readings. A value that was not read is not in this
file; the coverage table says Not captured.

Deterministic: same input, same bytes.
"""
import json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
SPEC = json.loads((RAW / "component-tokens.json").read_text())

DIM = re.compile(r"-?\d+(\.\d+)?(px|rem|em)")
COLOR = re.compile(r"^(#[0-9a-f]{6}|rgba?\([^)]+\))$")


def check(path, ty, val):
    if isinstance(val, str) and val.startswith("{"):
        return
    if ty == "dimension" and not DIM.fullmatch(str(val)):
        raise ValueError(f"{path}: dimension {val!r}")
    if ty == "color" and not (isinstance(val, str) and (val.startswith("{") or COLOR.fullmatch(val))):
        raise ValueError(f"{path}: color {val!r}")
    if ty == "fontWeight" and not isinstance(val, int):
        raise ValueError(f"{path}: fontWeight {val!r}")
    if ty == "duration" and not re.fullmatch(r"\d+ms", str(val)):
        raise ValueError(f"{path}: duration {val!r}")
    if ty == "shadow":
        for layer in val:
            for k in ("offsetX", "offsetY", "blur", "spread"):
                if not DIM.fullmatch(layer[k]):
                    raise ValueError(f"{path}: shadow {k} {layer[k]!r}")
    if ty == "typography":
        for k in ("fontFamily", "fontSize", "fontWeight", "lineHeight"):
            if k not in val:
                raise ValueError(f"{path}: typography missing {k}")


def leaf(path, spec):
    val, ty = spec["value"], spec["type"]
    check(path, ty, val)
    token = {"$value": val, "$type": ty, "$extensions": {"source": spec["source"]}}
    if spec.get("description"):
        token["$description"] = spec["description"]
    return token


def build(node, path=""):
    if isinstance(node, dict) and "type" in node and "value" in node:
        return leaf(path, node)
    return {k: build(v, f"{path}.{k}" if path else k) for k, v in node.items()}


core = build(SPEC["core"])
light = build(SPEC["light"])


def tokens_of(tree, prefix=""):
    for k, v in tree.items():
        if isinstance(v, dict) and "$value" in v:
            yield prefix + k, v
        elif isinstance(v, dict):
            yield from tokens_of(v, prefix + k + ".")


NAMES = {n for n, _ in tokens_of(core)}
NAMES_L = NAMES | {n for n, _ in tokens_of(light)}


def aliases(v):
    if isinstance(v, str):
        return re.findall(r"\{([^{}]+)\}", v)
    if isinstance(v, dict):
        return [a for x in v.values() for a in aliases(x)]
    if isinstance(v, list):
        return [a for x in v for a in aliases(x)]
    return []


for n, t in tokens_of(core):
    for a in aliases(t["$value"]):
        if a not in NAMES:
            raise KeyError(f"core.{n}: alias {{{a}}} points at nothing")
for n, t in tokens_of(light):
    for a in aliases(t["$value"]):
        if a not in NAMES_L:
            raise KeyError(f"light.{n}: alias {{{a}}} points at nothing")

tokens = {
    "core": core,
    "light": light,
    "$themes": [{
        "id": "light",
        "name": "Light",
        "selectedTokenSets": {"core": "source", "light": "enabled"},
        "$description": "The marketing site paints one light page. The header and menus invert to black on the hero and in the open panel; that inversion is tokens, not a second theme.",
    }],
    "$metadata": {"tokenSetOrder": ["core", "light"]},
}
(HERE / "tokens.json").write_text(json.dumps(tokens, indent=2, ensure_ascii=False) + "\n")


def count(d):
    return sum(count(v) for v in d.values()) if isinstance(d, dict) and "$value" not in d else 1


print({k: count(v) for k, v in tokens.items() if k in ("core", "light")})
