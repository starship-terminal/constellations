#!/usr/bin/env python3
"""Build tokens.json from raw/component-tokens.json.

byborre.com paints one public theme. core holds the measured palette, type and
scales. light holds the semantic roles as aliases. There is no dark set: a
.dark rule exists in the CSS and was not applied on any public page.

Every leaf needs a source. Aliases resolve against core, then the leaf's set.
Deterministic: same inputs, byte-identical output.
"""
import json, pathlib, re, sys

HERE = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(HERE / "tools"))
from token_checks import alias_errors, tokens_of

RAW = HERE / "raw"
SPEC = json.loads((RAW / "component-tokens.json").read_text())


def norm_color(v):
    v = v.strip().lower()
    m = re.fullmatch(r"#([0-9a-f]{3,8})", v)
    if m:
        h = m.group(1)
        if len(h) in (3, 4):
            h = "".join(c * 2 for c in h)
        if len(h) == 8:
            a = round(int(h[6:8], 16) / 255, 3)
            rgb = tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))
            return "#%02x%02x%02x" % rgb if a >= 1 else "rgba(%d, %d, %d, %g)" % (*rgb, a)
        return "#" + h[:6]
    m = re.fullmatch(r"rgba?\(\s*(\d+)[,\s]+(\d+)[,\s]+(\d+)(?:\s*[,/]\s*([\d.]+%?))?\s*\)", v)
    if m:
        r, g, b, a = m.groups()
        if a is None or float(a.rstrip("%")) >= (100 if a.endswith("%") else 1):
            return "#%02x%02x%02x" % (int(r), int(g), int(b))
        af = float(a[:-1]) / 100 if a.endswith("%") else float(a)
        return "rgba(%d, %d, %d, %g)" % (int(r), int(g), int(b), af)
    raise ValueError("not a colour: " + v)


DIM = re.compile(r"-?\d+(\.\d+)?(px|rem)")


def check(path, ty, val):
    if isinstance(val, str) and val.startswith("{"):
        return
    if ty == "dimension" and not DIM.fullmatch(str(val)):
        raise ValueError(f"{path}: dimension must be one px or rem length, got {val!r}")
    if ty == "color":
        norm_color(val)
    if ty == "fontWeight" and not isinstance(val, int):
        raise ValueError(f"{path}: fontWeight {val!r}")


def leaf(path, spec):
    if not spec.get("source"):
        raise ValueError(f"{path}: leaf without a source")
    ty, val = spec["type"], spec["value"]
    if ty == "color" and not str(val).startswith("{"):
        val = norm_color(val)
    if ty == "dimension" and isinstance(val, (int, float)):
        val = f"{val:g}px"
    if ty == "typography":
        val = dict(val)
        if isinstance(val.get("fontWeight"), str) and val["fontWeight"].isdigit():
            val["fontWeight"] = int(val["fontWeight"])
    else:
        check(path, ty, val)
    return {"$value": val, "$type": ty, "$extensions": {"source": spec["source"]}}


def build(node, path=""):
    if isinstance(node, dict) and "type" in node and "value" in node:
        return leaf(path, node)
    out = {}
    for k, v in node.items():
        if k.startswith("_"):
            continue
        out[k] = build(v, f"{path}.{k}" if path else k)
    return out


CORE_KEYS = ("color", "font", "typography", "radius", "space", "size", "border")
core = {"$description": "Measured scales from the public byborre.com pages. One theme."}
for key in CORE_KEYS:
    core[key] = build(SPEC[key])
light = build(SPEC["light"])
light["$description"] = "Semantic roles for the one painted theme. Aliases point at core."

errors = alias_errors(core, light, light)
if errors:
    raise SystemExit("\n".join(errors))

doc = {
    "$description": "BYBORRE public site, measured 2026-11-21 from byborre.com. One light theme.",
    "core": core,
    "light": light,
    "$themes": [{"name": "light", "selectedTokenSets": {"core": "source", "light": "enabled"}}],
}
(HERE / "tokens.json").write_text(json.dumps(doc, indent=1) + "\n")
print(f"tokens.json: {sum(1 for _ in tokens_of(core))} core, {sum(1 for _ in tokens_of(light))} light")
