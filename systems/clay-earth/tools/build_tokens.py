#!/usr/bin/env python3
"""Build tokens.json from raw/component-tokens.json.

Clay's public site (clay.earth) 301s to me.sh. The marketing CSS modules
declare no custom properties, so every token here is a computed style read
on 2026-11-21 by tools/capture/public/read.mjs and the follow-up probe
stored in raw/component-tokens.json. Edit that file, never tokens.json.
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
        r, g, b = (int(h[i:i + 2], 16) for i in (0, 2, 4))
        return "#%02x%02x%02x" % (r, g, b)
    m = re.fullmatch(r"rgba?\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)(?:\s*,\s*([\d.]+))?\s*\)", v)
    if not m:
        raise ValueError("not a colour: " + v)
    r, g, b, a = m.groups()
    if a is None or float(a) == 1:
        return "#%02x%02x%02x" % (int(r), int(g), int(b))
    return "rgba(%s, %s, %s, %s)" % (r, g, b, ("%g" % float(a)))


def emit(node):
    if isinstance(node, dict) and "value" in node and "type" in node:
        val = node["value"]
        ty = node["type"]
        if ty == "color":
            val = norm_color(val)
        elif ty == "fontFamily":
            val = str(val)
        out = {"$value": val, "$type": ty, "$extensions": {"source": node["source"]}}
        return out
    if not isinstance(node, dict):
        raise ValueError(node)
    return {k: emit(v) for k, v in node.items() if not k.startswith("_")}


tokens = emit({k: v for k, v in SPEC.items() if k in ("core", "dark", "light")})
tokens["$themes"] = [
    {"id": "dark", "name": "dark", "selectedTokenSets": {"core": "source", "dark": "enabled"}},
    {"id": "light", "name": "light", "selectedTokenSets": {"core": "source", "light": "enabled"}},
]
(HERE / "tokens.json").write_text(json.dumps(tokens, indent=2) + "\n")
print("wrote", HERE / "tokens.json")
