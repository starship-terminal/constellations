#!/usr/bin/env python3
"""Build tokens.json from raw/component-tokens.json.

Overflow's public site declares one custom property (--swiper-theme-color).
The rest of the tokens are computed styles measured on overflow.io on
2026-11-21. One light theme. Deterministic.
"""
import json, pathlib, re, sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from token_checks import alias_errors

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
SPEC = json.loads((RAW / "component-tokens.json").read_text())

DIM = re.compile(r"-?\d+(\.\d+)?(px|rem)")


def norm_color(v):
    v = str(v).strip().lower()
    if v.startswith("{"):
        return v
    m = re.fullmatch(r"#([0-9a-f]{3,8})", v)
    if m:
        h = m.group(1)
        if len(h) in (3, 4):
            h = "".join(c * 2 for c in h)
        r, g, b = (int(h[i:i + 2], 16) for i in (0, 2, 4))
        return "#%02x%02x%02x" % (r, g, b)
    m = re.fullmatch(r"rgba?\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)(?:\s*,\s*([\d.]+))?\s*\)", v)
    if m:
        r, g, b, a = m.groups()
        if a is None or float(a) == 1:
            return "#%02x%02x%02x" % (int(r), int(g), int(b))
        return "rgba(%s, %s, %s, %g)" % (r, g, b, float(a))
    raise ValueError("not a colour: " + v)


def px(v):
    v = str(v).strip()
    if v.startswith("{"):
        return v
    m = re.fullmatch(r"(-?\d+(?:\.\d+)?)px", v)
    if not m:
        raise ValueError("not a px length: " + v)
    return "%gpx" % round(float(m.group(1)), 3)


def leaf(spec):
    ty = spec["type"]
    val = spec["value"]
    src = spec["source"]
    if ty == "color":
        val = norm_color(val)
    elif ty == "dimension":
        val = px(val)
    elif ty == "shadow":
        for layer in val:
            for k in ("offsetX", "offsetY", "blur", "spread"):
                layer[k] = px(layer[k])
            layer["color"] = norm_color(layer["color"])
    elif ty == "typography":
        val = dict(val)
        val["fontSize"] = px(val["fontSize"])
        val["lineHeight"] = px(val["lineHeight"])
        val["letterSpacing"] = px(val["letterSpacing"])
    elif ty == "duration" and isinstance(val, str) and val.endswith("ms"):
        pass
    elif ty == "fontWeight":
        val = int(val)
    elif ty == "fontFamily":
        val = str(val)
    elif ty == "cubicBezier":
        val = [float(x) for x in val]
    else:
        raise ValueError("unknown type " + ty)
    return {"$value": val, "$type": ty, "$extensions": {"source": src}}


def build(node):
    if isinstance(node, dict) and "type" in node and "value" in node:
        return leaf(node)
    return {k: build(v) for k, v in node.items()}


core = build(SPEC["core"])
light = build(SPEC["light"])
light["component"] = build(SPEC["component"])

errors = alias_errors(core, light, {})
if errors:
    raise SystemExit("\n".join(errors))

tokens = {
    "core": core,
    "light": light,
    "$themes": [{
        "id": "light",
        "name": "Light",
        "selectedTokenSets": {"core": "source", "light": "enabled"},
        "$description": "The only theme overflow.io paints on the public pages captured 2026-11-21. No dark toggle was found.",
    }],
    "$metadata": {"tokenSetOrder": ["core", "light"]},
}
(HERE / "tokens.json").write_text(json.dumps(tokens, indent=2, ensure_ascii=False) + "\n")


def count(d):
    return sum(count(v) for v in d.values()) if isinstance(d, dict) and "$value" not in d else 1


print({k: count(v) for k, v in tokens.items() if k in ("core", "light")})
