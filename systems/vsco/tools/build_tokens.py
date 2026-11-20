#!/usr/bin/env python3
"""Build tokens.json from raw/component-tokens.json for the VSCO public site.

One theme. Every leaf needs a source. Aliases resolve against core, then the
leaf's own set. Deterministic.
"""
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent.parent
SPEC = json.loads((HERE / "raw" / "component-tokens.json").read_text())


def norm_color(v):
    v = v.strip().lower()
    m = re.fullmatch(r"#([0-9a-f]{3,8})", v)
    if m:
        h = m.group(1)
        if len(h) in (3, 4):
            h = "".join(c * 2 for c in h)
        return "#" + h[:6]
    m = re.fullmatch(r"rgba?\(\s*(\d+)[,\s]+(\d+)[,\s]+(\d+)", v)
    if m:
        return "#%02x%02x%02x" % tuple(int(x) for x in m.groups())
    raise ValueError("not a colour: " + v)


DIM = re.compile(r"-?\d+(\.\d+)?(px|rem)")


def check(path, ty, val):
    if isinstance(val, str) and val.startswith("{"):
        return
    if ty == "dimension" and not DIM.fullmatch(str(val)):
        raise ValueError(f"{path}: dimension {val!r}")
    if ty == "color":
        norm_color(val)
    if ty == "fontWeight" and not isinstance(val, int):
        raise ValueError(f"{path}: fontWeight {val!r}")
    if ty == "duration" and not re.fullmatch(r"\d+ms", str(val)):
        raise ValueError(f"{path}: duration {val!r}")


def leaf(path, spec):
    if not spec.get("source"):
        raise ValueError(f"{path}: leaf without a source")
    ty = spec["type"]
    val = spec["value"]
    if ty == "color" and not str(val).startswith("{"):
        val = norm_color(val)
    if ty == "typography":
        val = dict(val)
        if isinstance(val.get("fontWeight"), str) and val["fontWeight"].isdigit():
            val["fontWeight"] = int(val["fontWeight"])
    check(path, ty, val if ty != "typography" else "0px")
    token = {"$value": val, "$type": ty, "$extensions": {"source": spec["source"]}}
    if spec.get("description"):
        token["$description"] = spec["description"]
    return token


def build(node, path=""):
    if isinstance(node, dict) and "type" in node and "value" in node:
        return leaf(path, node)
    out = {}
    for k, v in node.items():
        if k.startswith("_") or k.startswith("$"):
            if k == "$description":
                out[k] = v
            continue
        out[k] = build(v, f"{path}.{k}" if path else k)
    return out


def resolve(token, tokens, seen=()):
    val = token["$value"]
    if not isinstance(val, str) or not val.startswith("{"):
        return val
    name = val.strip("{}")
    if name in seen:
        raise ValueError("alias cycle " + name)
    target = tokens
    for part in name.split("."):
        target = target[part]
    return resolve(target, tokens, seen + (name,))


doc = {
    "core": build(SPEC["core"]),
    "light": build(SPEC["light"]),
    "$themes": [{"id": "light", "name": "Light", "selectedTokenSets": {"core": "source", "light": "enabled"}}],
}
# alias check
flat = {}

def walk(node, prefix=""):
    for k, v in node.items():
        if k.startswith("$"):
            continue
        if isinstance(v, dict) and "$value" in v:
            flat[prefix + k] = v
        elif isinstance(v, dict):
            walk(v, prefix + k + ".")

walk(doc["core"])
walk(doc["light"])
for name, token in flat.items():
    val = token["$value"]
    if isinstance(val, str) and val.startswith("{"):
        resolve(token, {**doc["core"], **doc["light"]})
    if "source" not in token.get("$extensions", {}):
        raise SystemExit("missing source " + name)

(HERE / "tokens.json").write_text(json.dumps(doc, indent=1) + "\n")
print("tokens", len(flat))
