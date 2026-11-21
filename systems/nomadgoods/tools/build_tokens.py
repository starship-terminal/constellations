#!/usr/bin/env python3
"""Build tokens.json from raw/component-tokens.json.

Values were read from nomadgoods.com/sg/ on 2026-11-21: computed styles on
the live page, plus the cross-origin stylesheets the CSSOM could not read
(buttons-FS3QHQ7I.css, css-bundle). Every leaf needs a source. A leaf whose
source starts with "Not captured" is skipped, not invented.
"""
import json
import pathlib
import re
import sys

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
            a = round(int(h[6:8], 16) / 255, 3)
            return "#%02x%02x%02x" % tuple(int(h[i:i + 2], 16) for i in (0, 2, 4)) if a >= 1 else "rgba(%d, %d, %d, %g)" % (*[int(h[i:i + 2], 16) for i in (0, 2, 4)], a)
        return "#" + h[:6]
    m = re.fullmatch(r"rgba?\(\s*(\d+)[,\s]+(\d+)[,\s]+(\d+)(?:\s*[,/]\s*([\d.]+%?))?\s*\)", v)
    if m:
        r, g, b, a = m.groups()
        a = float(a[:-1]) / 100 if a and a.endswith("%") else float(a or 1)
        if a >= 1:
            return "#%02x%02x%02x" % (int(r), int(g), int(b))
        return "rgba(%d, %d, %d, %g)" % (int(r), int(g), int(b), a)
    raise ValueError("not a colour: " + v)


DIM = re.compile(r"-?\d*\.?\d+(px|rem)")


def check(path, ty, val):
    if isinstance(val, str) and val.startswith("{"):
        return
    if ty == "dimension" and not DIM.fullmatch(str(val)):
        raise ValueError(f"{path}: dimension must be one px or rem length, got {val!r}")
    if ty == "color":
        norm_color(val)
    if ty == "number" and not isinstance(val, (int, float)):
        raise ValueError(f"{path}: number {val!r}")
    if ty == "fontWeight" and not isinstance(val, int):
        raise ValueError(f"{path}: fontWeight {val!r}")
    if ty == "duration" and not re.fullmatch(r"\d+ms", str(val)):
        raise ValueError(f"{path}: duration {val!r}")


def leaf(path, spec):
    source = spec.get("source") or ""
    if source.startswith("Not captured"):
        print("skip", path, source[:80])
        return None
    if not source:
        raise ValueError(f"{path}: leaf without a source")
    ty = spec["type"]
    val = spec["value"]
    if ty == "color" and not str(val).startswith("{"):
        val = norm_color(val)
    if ty == "fontWeight" and isinstance(val, str) and val.isdigit():
        val = int(val)
    check(path, ty, val)
    t = {"$value": val, "$type": ty, "$extensions": {"source": source}}
    if spec.get("description"):
        t["$description"] = spec["description"]
    return t


def build(node, path=""):
    if isinstance(node, dict) and "$value" in node:
        return node
    if isinstance(node, dict) and "type" in node and "value" in node:
        return leaf(path, node)
    out = {}
    for k, v in node.items():
        if k.startswith("_"):
            continue
        if k == "$description":
            out[k] = v
            continue
        built = build(v, f"{path}.{k}" if path else k)
        if built is None:
            continue
        if isinstance(built, dict) and not built:
            continue
        out[k] = built
    return out


core = build(SPEC["core"])
light = build(SPEC["light"])

# Drop the unused sale primitive if its source was Not captured.
if "color" in core and "sale" in core["color"] and not core["color"]["sale"]:
    del core["color"]["sale"]

tokens = {
    "core": core,
    "light": light,
    "$themes": [{
        "id": "light",
        "name": "Light",
        "selectedTokenSets": {"core": "source", "light": "enabled"},
        "$description": "The public Nomad storefront paints one light theme. No dark theme switch was found.",
    }],
    "$metadata": {"tokenSetOrder": ["core", "light"]},
}
(HERE / "tokens.json").write_text(json.dumps(tokens, indent=1, ensure_ascii=False) + "\n")


def count(d):
    return sum(1 if "$value" in v else count(v) for v in d.values() if isinstance(v, dict))


print(f"tokens.json: core {count(core)} + light {count(light)} = {count(core) + count(light)}")
