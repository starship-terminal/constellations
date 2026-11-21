#!/usr/bin/env python3
"""Build tokens.json from raw/component-tokens.json.

Fable's public pages do not declare a product token set. Each leaf in
component-tokens.json is a computed style read on 2026-11-21, with a source
string. This builder copies those leaves into a Tokens Studio multi-set file
and refuses a leaf with no source, a colour it cannot parse, or a dimension
that is not one px or rem length.
"""
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
SPEC = json.loads((RAW / "component-tokens.json").read_text())


def norm_color(v):
    v = str(v).strip().lower()
    m = re.fullmatch(r"#([0-9a-f]{3,8})", v)
    if m:
        h = m.group(1)
        if len(h) in (3, 4):
            h = "".join(c * 2 for c in h)
        if len(h) == 8:
            return "rgba(%d, %d, %d, %s)" % (*[int(h[i:i + 2], 16) for i in (0, 2, 4)], "%g" % round(int(h[6:8], 16) / 255, 3))
        return "#" + h[:6]
    m = re.fullmatch(r"rgba?\(\s*(\d+)[,\s]+(\d+)[,\s]+(\d+)(?:\s*[,/]\s*([\d.]+%?))?\s*\)", v)
    if m:
        r, g, b, a = m.groups()
        a = float(a[:-1]) / 100 if a and a.endswith("%") else float(a or 1)
        if a >= 1:
            return "#%02x%02x%02x" % (int(r), int(g), int(b))
        return "rgba(%d, %d, %d, %s)" % (int(r), int(g), int(b), "%g" % a)
    raise ValueError("not a colour: " + v)


DIM = re.compile(r"-?\d*\.?\d+(px|rem)")


def check(path, ty, val):
    if isinstance(val, str) and val.startswith("{"):
        return
    if ty == "color":
        norm_color(val)
    elif ty == "dimension" and not DIM.fullmatch(str(val)):
        raise ValueError(f"{path}: dimension {val!r}")
    elif ty == "fontWeight" and not isinstance(val, int):
        raise ValueError(f"{path}: fontWeight {val!r}")
    elif ty == "typography":
        if not isinstance(val, dict):
            raise ValueError(f"{path}: typography must be an object")
        if "fontSize" in val and not (str(val["fontSize"]).startswith("{") or DIM.fullmatch(str(val["fontSize"]))):
            raise ValueError(f"{path}: fontSize {val['fontSize']!r}")


def walk(node, path, out):
    if isinstance(node, dict) and "type" in node and "value" in node:
        if not node.get("source"):
            raise ValueError(f"{path}: missing source")
        check(path, node["type"], node["value"])
        leaf = {"$type": node["type"], "$value": node["value"], "$extensions": {"source": node["source"]}}
        cur = out
        parts = path.split(".")
        for part in parts[:-1]:
            cur = cur.setdefault(part, {})
        cur[parts[-1]] = leaf
        return
    for key, child in node.items():
        if key in ("captured", "route", "note"):
            continue
        walk(child, f"{path}.{key}" if path else key, out)


sets = {}
for name in ("core", "light"):
    sets[name] = {}
    walk(SPEC[name], "", sets[name])

doc = {
    "$description": "Fable public site, measured 2026-11-21 from computed styles. One light theme.",
    **sets,
    "$themes": [{"id": "light", "name": "light", "selectedTokenSets": {"core": "source", "light": "enabled"}}],
}
(HERE / "tokens.json").write_text(json.dumps(doc, indent=2) + "\n")
print("wrote tokens.json")
