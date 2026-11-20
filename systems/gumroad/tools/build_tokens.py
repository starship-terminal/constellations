#!/usr/bin/env python3
"""Build tokens.json from Gumroad's measured CSS variables and component readings.

Sources, read from gumroad.com on 2026-11-21, signed out:
  raw/css-vars.json           custom properties resolved in light and dark
  raw/component-tokens.json   the mapping from those readings to token paths

Every token carries $extensions.source. Edit the raw inputs, never tokens.json.
"""
import json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
V = json.loads((RAW / "css-vars.json").read_text())
SPEC = json.loads((RAW / "component-tokens.json").read_text())
DECL = {n: v.get("value", v.get("raw")) for n, v in V["resolved"]["light"].items()}


def norm_color(v):
    v = str(v).strip().lower()
    m = re.fullmatch(r"#([0-9a-f]{3,8})", v)
    if m:
        h = m.group(1)
        if len(h) in (3, 4):
            h = "".join(c * 2 for c in h)
        r, g, b = (int(h[i:i + 2], 16) for i in (0, 2, 4))
        return "#%02x%02x%02x" % (r, g, b)
    m = re.fullmatch(r"rgba?\(\s*(\d+)[,\s]+(\d+)[,\s]+(\d+)(?:\s*[,/]\s*([\d.]+))?\s*\)", v)
    if m:
        r, g, b, a = m.groups()
        if a is None or float(a) == 1:
            return "#%02x%02x%02x" % (int(r), int(g), int(b))
        return "rgba(%s, %s, %s, %g)" % (r, g, b, float(a))
    raise ValueError("not a colour: " + v)


DIM = re.compile(r"-?\d+(\.\d+)?(px|rem)")


def check(path, ty, val):
    if isinstance(val, str) and val.startswith("{"):
        return
    if isinstance(val, dict):
        return
    if ty == "dimension" and not DIM.fullmatch(str(val)):
        raise ValueError(f"{path}: dimension {val!r}")
    if ty == "color":
        norm_color(val)
    if ty == "fontWeight" and not isinstance(val, int):
        raise ValueError(f"{path}: fontWeight {val!r}")


def leaf(path, spec):
    ty = spec["type"]
    if "var" in spec:
        name = spec["var"]
        if name not in DECL:
            raise KeyError(f"{path}: {name} is not in raw/css-vars.json")
        val = DECL[name]
        src = f"css-var {name}"
        if spec.get("source"):
            src += "; " + spec["source"]
    else:
        val = spec["value"]
        src = spec.get("source", "measured")
    if ty == "color" and not str(val).startswith("{"):
        val = norm_color(val)
    if ty == "dimension" and isinstance(val, str) and re.fullmatch(r"-?\d+(\.\d+)?", val.strip()):
        val = val.strip() + "px"
    if ty == "typography":
        check(path, ty, val)
    else:
        check(path, ty, val)
    return {"$value": val, "$type": ty, "$extensions": {"source": src}}


def build(node, path=""):
    if isinstance(node, dict) and "type" in node and ("value" in node or "var" in node):
        return leaf(path, node)
    return {k: build(v, f"{path}.{k}" if path else k) for k, v in node.items()}


core = build(SPEC["core"])
light = build(SPEC["light"])
dark = build(SPEC["dark"])
light["component"] = build(SPEC["component"])
dark["component"] = build(SPEC["component"])

def tokens_of(tree, prefix=""):
    for k, v in tree.items():
        if isinstance(v, dict) and "$value" in v:
            yield prefix + k, v
        elif isinstance(v, dict):
            yield from tokens_of(v, prefix + k + ".")

NAMES = {n for n, _ in tokens_of(core)}

def aliases(v):
    if isinstance(v, str):
        return re.findall(r"\{([^{}]+)\}", v)
    if isinstance(v, dict):
        return [a for x in v.values() for a in aliases(x)]
    return []

for theme_name, theme in (("light", light), ("dark", dark)):
    names = NAMES | {n for n, _ in tokens_of(theme)}
    for n, t in tokens_of(theme):
        for a in aliases(t["$value"]):
            if a not in names and a not in NAMES:
                raise KeyError(f"{theme_name}.{n}: alias {{{a}}} points at nothing")
    for n, t in tokens_of(core):
        for a in aliases(t["$value"]):
            if a not in NAMES:
                raise KeyError(f"core.{n}: alias {{{a}}} points at nothing")

tokens = {
    "core": core,
    "light": light,
    "dark": dark,
    "$themes": [
        {"id": "light", "name": "Light", "selectedTokenSets": {"core": "source", "light": "enabled"}},
        {"id": "dark", "name": "Dark", "selectedTokenSets": {"core": "source", "dark": "enabled"}},
    ],
    "$metadata": {"tokenSetOrder": ["core", "light", "dark"]},
}
(HERE / "tokens.json").write_text(json.dumps(tokens, indent=2, ensure_ascii=False) + "\n")
print("wrote tokens.json", {k: sum(1 for _ in tokens_of(tokens[k])) for k in ("core", "light", "dark")})
