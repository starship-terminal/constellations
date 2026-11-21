#!/usr/bin/env python3
"""Build tokens.json (W3C DTCG, Tokens Studio multi-set layout) from the raw captures.

Sources, read from westelm.com on 2026-11-21:
  raw/css-vars.json          every custom property the pages declare (almost none are the design
                             system's: two app vars, Tailwind framework internals, an Adyen vendor
                             block) — recorded as evidence, not tokenised
  raw/component-tokens.json  the token tree: each leaf is {"type", "value", "source"} where value
                             is a computed measurement and source names where it was read
                             (raw/components-computed.json, a stylesheet rule, or a painted layer)

westelm.com paints a single light theme on the pages that loaded, so tokens.json holds `core` and `light` only. Every token
carries $extensions.source. Aliases are unprefixed ("{color.blue.default}") and resolve against
core first, then the leaf's own set. The builder refuses an alias that points at nothing, a colour
it cannot parse, a dimension that is not one px or rem length, and a leaf without a source.
Deterministic: same inputs, byte-identical output.
"""
import json, pathlib, re, sys

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
SPEC = json.loads((RAW / "component-tokens.json").read_text())


# ---------------------------------------------------------------- value helpers


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
    if ty == "cubicBezier" and not (isinstance(val, list) and len(val) == 4):
        raise ValueError(f"{path}: cubicBezier {val!r}")


# ---------------------------------------------------------------- leaves


def leaf(path, spec):
    ty = spec["type"]
    if not spec.get("source"):
        raise ValueError(f"{path}: leaf without a source")
    val = spec["value"]
    if ty == "color" and not str(val).startswith("{"):
        val = norm_color(val)
    if ty in ("fontWeight", "number") and isinstance(val, str) and val.isdigit():
        val = int(val)
    if ty == "dimension" and isinstance(val, str) and re.fullmatch(r"-?\d+(\.\d+)?", val):
        val += "px"
    if ty == "duration" and isinstance(val, str) and re.fullmatch(r"\d+(\.\d+)?s", val):
        val = ("%g" % (float(val[:-1]) * 1000)) + "ms"
    check(path, ty, val)
    t = {"$value": val, "$type": ty, "$extensions": {"source": spec["source"]}}
    if spec.get("description"):
        t["$description"] = spec["description"]
    return t


def build(node, path=""):
    if isinstance(node, dict) and "type" in node and "value" in node:
        return leaf(path, node)
    if isinstance(node, dict) and "$value" in node:
        return node  # already a DTCG leaf (typography composites)
    out = {}
    for k, v in node.items():
        if k.startswith("_"):
            continue
        if k == "$description":
            out[k] = v
            continue
        out[k] = build(v, f"{path}.{k}" if path else k)
    return out


core = build(SPEC["core"])
light = build(SPEC["light"])

# every alias must point at a token in its own set or core
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from token_checks import alias_errors  # noqa: E402

_errors = alias_errors(core, light, {})
if _errors:
    raise KeyError("; ".join(_errors))

tokens = {
    "core": core,
    "light": light,
    "$themes": [
        {"id": "light", "name": "Light", "selectedTokenSets": {"core": "source", "light": "enabled"},
         "$description": "The only theme westelm.com painted on the pages that loaded. No dark theme control was found."},
    ],
    "$metadata": {"tokenSetOrder": ["core", "light"]},
}
(HERE / "tokens.json").write_text(json.dumps(tokens, indent=1, ensure_ascii=False) + "\n")


def count(d):
    return sum(1 if "$value" in v else count(v) for v in d.values() if isinstance(v, dict))


print(f"tokens.json: core {count(core)} + light {count(light)} = {count(core) + count(light)} tokens, 1 theme")
