#!/usr/bin/env python3
"""Build tokens.json from raw/component-tokens.json.

FeedHive's public site paints one light theme. Values are computed styles
read on 2026-11-21. The marketing site does not expose a product token sheet:
colours are Tailwind utilities. Every token carries $extensions.source.
"""
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
SPEC = json.loads((RAW / "component-tokens.json").read_text())


def norm_color(v):
    v = v.strip().lower()
    m = re.fullmatch(r"#([0-9a-f]{6})", v)
    if not m:
        raise ValueError("not a colour: " + v)
    return "#" + m.group(1)


def leaf(spec):
    ty = spec["type"]
    val = spec["value"]
    if ty == "color":
        val = norm_color(val)
    if ty == "dimension" and not re.fullmatch(r"-?\d+(\.\d+)?px", str(val)):
        raise ValueError("dimension must be px: " + str(val))
    if not spec.get("source"):
        raise ValueError("leaf without a source")
    return {"$value": val, "$type": ty, "$extensions": {"source": spec["source"]}}


def group(node):
    return {k: leaf(v) for k, v in node.items() if not k.startswith("_")}


core = {
    "font": group(SPEC["font"]),
    "type": group(SPEC["type"]),
    "radius": group(SPEC["radius"]),
    "size": group(SPEC["size"]),
}
light = {"color": group(SPEC["color"])}

tokens = {
    "core": core,
    "light": light,
    "$themes": [
        {"id": "light", "name": "Light", "selectedTokenSets": {"core": "enabled", "light": "enabled"}}
    ],
}
out = HERE / "tokens.json"
out.write_text(json.dumps(tokens, indent=2) + "\n")
print(f"wrote {out} core={sum(len(v) for v in core.values())} light={len(light['color'])}")
