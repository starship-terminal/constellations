#!/usr/bin/env python3
"""Build tokens.json from Marathon's public capture.

Sources, read from onmarathon.com on 2026-11-18, signed out:
  raw/css-vars.json            custom properties from the live CSSOM. Light is
                               :root and .light (html.light is what the public
                               pages paint). Dark is .dark and
                               @media (prefers-color-scheme: dark), resolved on
                               a probe. The public pages never painted dark.
  raw/component-tokens.json    measured type, radii, control sizes and motion
                               from computed styles on the public pages.

Every token carries $extensions.source. Deterministic.
"""
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
ROOT = HERE.parent
RAW = ROOT / "raw"
V = json.loads((RAW / "css-vars.json").read_text())
SPEC = json.loads((RAW / "component-tokens.json").read_text())

DECL = {
    t: {n: v.get("value", v.get("raw")) for n, v in V["resolved"][t].items()}
    for t in ("light", "dark")
}


def norm_color(v):
    v = str(v).strip().lower()
    m = re.fullmatch(r"#([0-9a-f]{3,8})", v)
    if m:
        h = m.group(1)
        if len(h) in (3, 4):
            h = "".join(c * 2 for c in h)
        r, g, b = (int(h[i:i + 2], 16) for i in (0, 2, 4))
        if len(h) == 8:
            a = round(int(h[6:8], 16) / 255, 3)
            return "#%02x%02x%02x" % (r, g, b) if a == 1 else "rgba(%d, %d, %d, %g)" % (r, g, b, a)
        return "#%02x%02x%02x" % (r, g, b)
    m = re.fullmatch(r"rgba?\(\s*(\d+)[,\s]+(\d+)[,\s]+(\d+)(?:\s*[,/]\s*([\d.]+%?))?\s*\)", v)
    if m:
        r, g, b, a = m.groups()
        if a is None:
            return "#%02x%02x%02x" % (int(r), int(g), int(b))
        a = float(a[:-1]) / 100 if a.endswith("%") else float(a)
        return "#%02x%02x%02x" % (int(r), int(g), int(b)) if a == 1 else "rgba(%s, %s, %s, %g)" % (r, g, b, a)
    raise ValueError("not a colour: " + v)


DIM = re.compile(r"-?\d+(\.\d+)?(px|rem)")


def check(path, ty, val):
    if isinstance(val, str) and val.startswith("{"):
        return
    if ty == "dimension" and not DIM.fullmatch(str(val)):
        raise ValueError(f"{path}: dimension must be one px or rem length, got {val!r}")
    if ty == "color" and not str(val).startswith("{"):
        norm_color(val)
    if ty == "number" and not isinstance(val, (int, float)):
        raise ValueError(f"{path}: number {val!r}")
    if ty == "fontFamily" and not isinstance(val, str):
        raise ValueError(f"{path}: fontFamily {val!r}")
    if ty == "typography" and not isinstance(val, dict):
        raise ValueError(f"{path}: typography {val!r}")
    if ty == "fontWeight" and not isinstance(val, (int, float)):
        raise ValueError(f"{path}: fontWeight {val!r}")
    if ty == "duration" and not re.fullmatch(r"\d+(\.\d+)?ms", str(val)):
        raise ValueError(f"{path}: duration {val!r}")
    if ty == "cubicBezier" and not (isinstance(val, list) and len(val) == 4):
        raise ValueError(f"{path}: cubicBezier {val!r}")


def leaf(path, spec, theme):
    ty = spec["type"]
    if "var" in spec:
        name = spec["var"]
        if name not in DECL[theme]:
            raise KeyError(f"{path}: {name} is not resolved in raw/css-vars.json ({theme})")
        val = DECL[theme][name]
        src = f"css-var {name} ({theme}); raw/css-vars.json"
        if spec.get("source"):
            src += "; " + spec["source"]
    else:
        val = spec["value"]
        src = spec["source"]
    if ty == "color" and not str(val).startswith("{"):
        val = norm_color(val)
    if ty == "dimension" and isinstance(val, str) and re.fullmatch(r"-?\d+(\.\d+)?", val.strip()):
        val = val.strip() + "px"
    if ty == "fontWeight" and isinstance(val, str) and re.fullmatch(r"\d+", val):
        val = int(val)
    if ty == "number" and isinstance(val, str) and re.fullmatch(r"-?\d+(\.\d+)?", val):
        val = float(val) if "." in val else int(val)
    check(path, ty, val)
    token = {"$value": val, "$type": ty, "$extensions": {"source": src}}
    if spec.get("description"):
        token["$description"] = spec["description"]
    return token


def build(node, theme, path=""):
    if isinstance(node, dict) and "type" in node and ("value" in node or "var" in node):
        return leaf(path, node, theme)
    return {k: build(v, theme, f"{path}.{k}" if path else k) for k, v in node.items() if not k.startswith("_")}


core = build(SPEC["core"], "light")
light = build(SPEC["light"], "light")
dark = build(SPEC["dark"], "dark")
light["component"] = build(SPEC["component"], "light")


def tokens_of(tree, prefix=""):
    for k, v in tree.items():
        if isinstance(v, dict) and "$value" in v:
            yield prefix + k, v
        elif isinstance(v, dict):
            yield from tokens_of(v, prefix + k + ".")


NAMES = {n for n, _ in tokens_of(core)}
NAMES_L = NAMES | {n for n, _ in tokens_of(light)}
NAMES_D = NAMES | {n for n, _ in tokens_of(dark)}


def aliases(v):
    if isinstance(v, str):
        return re.findall(r"\{([^{}]+)\}", v)
    if isinstance(v, dict):
        return [a for x in v.values() for a in aliases(x)]
    if isinstance(v, list):
        return [a for x in v for a in aliases(x)]
    return []


for prefix, tree, names in (("core", core, NAMES), ("light", light, NAMES_L), ("dark", dark, NAMES_D)):
    for n, t in list(tokens_of(tree)):
        for a in aliases(t["$value"]):
            if a not in names:
                raise KeyError(f"{prefix}.{n}: alias {{{a}}} points at nothing")

tokens = {
    "core": core,
    "light": light,
    "dark": dark,
    "$themes": [
        {
            "id": "light",
            "name": "Light",
            "selectedTokenSets": {"core": "source", "light": "enabled"},
            "$description": "Public pages paint html.light. Measured on onmarathon.com, 2026-11-18.",
        },
        {
            "id": "dark",
            "name": "Dark (declared, not painted)",
            "selectedTokenSets": {"core": "source", "dark": "enabled"},
            "$description": "Resolved from .dark and prefers-color-scheme: dark on a probe. No public page painted this set.",
        },
    ],
    "$metadata": {"tokenSetOrder": ["core", "light", "dark"]},
}
(ROOT / "tokens.json").write_text(json.dumps(tokens, indent=2, ensure_ascii=False) + "\n")


def count(d):
    return sum(count(v) for v in d.values()) if isinstance(d, dict) and "$value" not in d else 1


print({k: count(v) for k, v in tokens.items() if k in ("core", "light", "dark")})
