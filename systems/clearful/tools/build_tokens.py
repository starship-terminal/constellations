#!/usr/bin/env python3
"""Build tokens.json from Clearful's public Webflow stylesheet and live readings.

Sources, read on 2026-11-21 from clearful.com, signed out:
  raw/css-vars.json           every custom property declared on :root in
                              clearful.webflow.*.min.css, resolved in a probe
                              document (tools/capture/vars.mjs)
  raw/component-tokens.json   measured control metrics (tools/build_component_tokens.py)

Deleted Webflow variable names (the stylesheet still references them, but they
are not declared) are not emitted as tokens. The live hover colour they paint
is recorded as a measured colour on light.accent.hover.

One theme. The stylesheet binds no dark class and no prefers-color-scheme rule.
"""
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
V = json.loads((RAW / "css-vars.json").read_text())
SPEC = json.loads((RAW / "component-tokens.json").read_text())
DECL = V["resolved"]["light"]


def norm_color(v):
    v = str(v).strip().lower()
    if v == "white":
        return "#ffffff"
    if v == "black":
        return "#000000"
    m = re.fullmatch(r"#([0-9a-f]{3,8})", v)
    if m:
        h = m.group(1)
        if len(h) in (3, 4):
            h = "".join(c * 2 for c in h)
        r, g, b = (int(h[i:i + 2], 16) for i in (0, 2, 4))
        if len(h) == 8:
            a = round(int(h[6:8], 16) / 255, 3)
            return "#%02x%02x%02x" % (r, g, b) if a == 1 else "rgba(%d, %d, %d, %s)" % (r, g, b, ("%g" % a))
        return "#%02x%02x%02x" % (r, g, b)
    m = re.fullmatch(r"rgba?\(\s*(\d+)[,\s]+(\d+)[,\s]+(\d+)(?:\s*[,/]\s*([\d.]+%?))?\s*\)", v)
    if m:
        r, g, b, a = m.groups()
        if a is None or a in ("1", "1.0"):
            return "#%02x%02x%02x" % (int(r), int(g), int(b))
        if a.endswith("%"):
            a = float(a[:-1]) / 100
        else:
            a = float(a)
        return "#%02x%02x%02x" % (int(r), int(g), int(b)) if a == 1 else "rgba(%s, %s, %s, %g)" % (r, g, b, a)
    raise ValueError("not a colour: " + v)


DIM = re.compile(r"-?\d+(\.\d+)?(px|rem)")


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
    if ty == "fontFamily" and not isinstance(val, str):
        raise ValueError(f"{path}: fontFamily {val!r}")


def leaf(path, spec):
    ty = spec["type"]
    if "var" in spec:
        name = spec["var"]
        if name not in DECL:
            raise KeyError(f"{path}: {name} is not in raw/css-vars.json")
        val = DECL[name]
        src = f"css-var {name} (light)"
        if spec.get("source"):
            src += "; " + spec["source"]
    else:
        val = spec["value"]
        src = spec["source"]
    if ty == "color" and not str(val).startswith("{"):
        val = norm_color(val)
    if ty in ("fontWeight", "number") and isinstance(val, str) and re.fullmatch(r"-?\d+(\.\d+)?", val):
        val = float(val) if "." in val else int(val)
    if ty == "dimension":
        if isinstance(val, (int, float)):
            val = "%gpx" % val
        elif isinstance(val, str) and re.fullmatch(r"-?\d+(\.\d+)?", val.strip()):
            val = val.strip() + "px"
        elif isinstance(val, str):
            val = val.strip()
            if val.startswith("."):
                val = "0" + val
    check(path, ty, val)
    token = {"$value": val, "$type": ty, "$extensions": {"source": src}}
    if spec.get("description"):
        token["$description"] = spec["description"]
    return token


def build(node, path=""):
    if isinstance(node, dict) and "type" in node and ("value" in node or "var" in node):
        return leaf(path, node)
    if isinstance(node, dict) and "$value" in node:
        return node
    return {k: build(v, f"{path}.{k}" if path else k) for k, v in node.items() if not k.startswith("_")}


core = build(SPEC["core"])
light = build(SPEC["light"])
light["component"] = build(SPEC["component"])


def tokens_of(tree, prefix=""):
    for k, v in tree.items():
        if isinstance(v, dict) and "$value" in v:
            yield prefix + k, v
        elif isinstance(v, dict):
            yield from tokens_of(v, prefix + k + ".")


NAMES = {n for n, _ in tokens_of(core)} | {n for n, _ in tokens_of(light)}


def aliases(v):
    if isinstance(v, str):
        return re.findall(r"\{([^{}]+)\}", v)
    if isinstance(v, dict):
        return [a for x in v.values() for a in aliases(x)]
    if isinstance(v, list):
        return [a for x in v for a in aliases(x)]
    return []


for n, t in list(tokens_of(core)) + list(tokens_of(light)):
    for a in aliases(t["$value"]):
        if a not in NAMES:
            raise KeyError(f"{n}: alias {{{a}}} points at nothing")

tokens = {
    "core": core,
    "light": light,
    "$themes": [{
        "id": "light",
        "name": "Light",
        "selectedTokenSets": {"core": "source", "light": "enabled"},
        "$description": "The only theme clearful.com paints. The Webflow stylesheet declares no dark class and no prefers-color-scheme rule.",
    }],
    "$metadata": {"tokenSetOrder": ["core", "light"]},
}
(HERE / "tokens.json").write_text(json.dumps(tokens, indent=2, ensure_ascii=False) + "\n")


def count(d):
    return sum(count(v) for v in d.values()) if isinstance(d, dict) and "$value" not in d else 1


print({k: count(v) for k, v in tokens.items() if k in ("core", "light")})
