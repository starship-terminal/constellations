#!/usr/bin/env python3
"""Build tokens.json from raw/component-tokens.json.

Every leaf was measured on the live public pages of me.sh, the 301 target of
clay.earth, on 2026-11-19. Edit the raw file, never tokens.json.
"""
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
SPEC = json.loads((RAW / "component-tokens.json").read_text())


def norm_color(v):
    v = v.strip()
    m = re.fullmatch(r"#([0-9a-fA-F]{6})", v)
    if m:
        return "#" + m.group(1).lower()
    m = re.fullmatch(r"rgba?\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)(?:\s*,\s*([\d.]+))?\s*\)", v)
    if m:
        r, g, b, a = m.groups()
        if a is None or float(a) == 1:
            return "#%02x%02x%02x" % (int(r), int(g), int(b))
        return "rgba(%d, %d, %d, %g)" % (int(r), int(g), int(b), float(a))
    raise ValueError("not a colour: " + v)


DIM = re.compile(r"-?\d+(\.\d+)?(px|rem)")


def check(path, ty, val):
    if ty == "dimension" and not DIM.fullmatch(str(val)):
        raise ValueError(f"{path}: dimension {val!r}")
    if ty == "color":
        norm_color(val)
    if ty == "fontWeight" and not isinstance(val, int):
        raise ValueError(f"{path}: fontWeight {val!r}")
    if ty == "duration" and not re.fullmatch(r"\d+ms", str(val)):
        raise ValueError(f"{path}: duration {val!r}")
    if ty == "cubicBezier" and not (isinstance(val, list) and len(val) == 4):
        raise ValueError(f"{path}: cubicBezier {val!r}")
    if ty == "fontFamily" and not isinstance(val, str):
        raise ValueError(f"{path}: fontFamily {val!r}")


def leaf(path, spec):
    ty = spec["type"]
    val = spec["value"]
    if ty == "color":
        val = norm_color(val)
    check(path, ty, val)
    token = {"$value": val, "$type": ty, "$extensions": {"source": spec["source"]}}
    if spec.get("description"):
        token["$description"] = spec["description"]
    return token


def build(node, path=""):
    if isinstance(node, dict) and "type" in node and "value" in node:
        return leaf(path, node)
    return {k: build(v, f"{path}.{k}" if path else k) for k, v in node.items() if not k.startswith("_")}


core = build(SPEC["core"])
dark = build(SPEC["dark"])
light = build(SPEC["light"])
core["component"] = build(SPEC["component"])

tokens = {
    "core": core,
    "dark": dark,
    "light": light,
    "$themes": [
        {"id": "dark", "name": "Dark", "selectedTokenSets": {"core": "source", "dark": "enabled"},
         "$description": "The black marketing surface me.sh paints on / and the dark routes. clay.earth 301s here."},
        {"id": "light", "name": "Light", "selectedTokenSets": {"core": "source", "light": "enabled"},
         "$description": "The warm cream surface me.sh paints on /pricing and the light app.me.sh sign-in card."},
    ],
    "$metadata": {"tokenSetOrder": ["core", "dark", "light"]},
}
(HERE / "tokens.json").write_text(json.dumps(tokens, indent=2, ensure_ascii=False) + "\n")


def count(d):
    return sum(count(v) for v in d.values()) if isinstance(d, dict) and "$value" not in d else 1


print({k: count(v) for k, v in tokens.items() if k in ("core", "dark", "light")})
