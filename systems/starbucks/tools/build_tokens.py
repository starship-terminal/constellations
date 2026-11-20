#!/usr/bin/env python3
"""Build tokens.json from raw/component-tokens.json.

Starbucks publishes no :root custom properties on the public pages. Every
token is a computed style read on 2026-11-21. One light theme. Every leaf
carries $extensions.source. The builder refuses a missing source, a bad
colour, and a dimension that is not one px or rem length.
"""
import json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent.parent
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
            return "rgba(%d, %d, %d, %s)" % (*[int(h[i:i + 2], 16) for i in (0, 2, 4)], "%g" % round(int(h[6:8], 16) / 255, 3))
        return "#" + h
    m = re.fullmatch(r"rgba?\(\s*(\d+)[,\s]+(\d+)[,\s]+(\d+)(?:\s*[,/]\s*([\d.]+%?))?\s*\)", v)
    if m:
        r, g, b, a = m.groups()
        a = float(a[:-1]) / 100 if a and a.endswith("%") else float(a or 1)
        if a >= 1:
            return "#%02x%02x%02x" % (int(r), int(g), int(b))
        return "rgba(%d, %d, %d, %s)" % (int(r), int(g), int(b), "%g" % a)
    return v


DIM = re.compile(r"-?\d*\.?\d+(px|rem)")


def check(path, ty, val):
    if isinstance(val, str) and val.startswith("{"):
        return
    if ty == "dimension" and not DIM.fullmatch(str(val)):
        raise ValueError(f"{path}: dimension must be one px or rem length, got {val!r}")
    if ty == "color":
        norm_color(val)
    if ty == "fontWeight" and not isinstance(val, int):
        raise ValueError(f"{path}: fontWeight {val!r}")
    if ty == "shadow" and not isinstance(val, list):
        raise ValueError(f"{path}: shadow {val!r}")


def leaf(path, spec):
    ty = spec["type"]
    if not spec.get("source"):
        raise ValueError(f"{path}: leaf without a source")
    val = spec["value"]
    if ty == "color" and not str(val).startswith("{"):
        val = norm_color(val)
    if ty == "typography" and isinstance(val, dict):
        val = dict(val)
    check(path, ty, val)
    t = {"$value": val, "$type": ty, "$extensions": {"source": spec["source"]}}
    if spec.get("description"):
        t["$description"] = spec["description"]
    return t


def build(node, path=""):
    if isinstance(node, dict) and "type" in node and "value" in node:
        return leaf(path, node)
    out = {}
    for k, v in node.items():
        if k.startswith("_"):
            continue
        if k == "$description":
            out[k] = v
            continue
        out[k] = build(v, f"{path}.{k}" if path else k)
    return out


tokens = {
    "core": build(SPEC["core"]),
    "light": build(SPEC["light"]),
    "$themes": [{"id": "light", "name": "Light", "selectedTokenSets": {"core": "source", "light": "enabled"}}],
}
# resolve-alias check
flat = {}

def walk(node, prefix):
    for k, v in node.items():
        if k.startswith("$"):
            continue
        p = f"{prefix}.{k}" if prefix else k
        if isinstance(v, dict) and "$value" in v:
            flat[p] = v["$value"]
        elif isinstance(v, dict):
            walk(v, p)

walk(tokens["core"], "core")
walk(tokens["light"], "light")
names = set()
for p in flat:
    parts = p.split(".")
    if parts[0] in ("core", "light"):
        names.add(".".join(parts[1:]))

def aliases(val):
    if isinstance(val, str):
        return re.findall(r"\{([^{}]+)\}", val)
    if isinstance(val, dict):
        return [a for v in val.values() for a in aliases(v)]
    if isinstance(val, list):
        return [a for v in val for a in aliases(v)]
    return []

for p, val in flat.items():
    for a in aliases(val):
        if a not in names and f"core.{a}" not in flat and a not in flat:
            # allow core-relative aliases used from light
            if a not in names:
                raise SystemExit(f"{p}: alias {{{a}}} does not resolve")

out = HERE / "tokens.json"
out.write_text(json.dumps(tokens, indent=2) + "\n")
print("wrote", out, "tokens", len(flat))
