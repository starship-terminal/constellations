#!/usr/bin/env python3
"""Build tokens.json from Matter's raw captures.

Sources:
  raw/css-vars.json           --mr-* custom properties resolved on a probe
  raw/component-tokens.json   the token tree (tools/build_component_tokens.py)

Deterministic: same inputs, byte-identical output.
"""
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
V = json.loads((RAW / "css-vars.json").read_text())
SPEC = json.loads((RAW / "component-tokens.json").read_text())
DECL = {t: {n: v.get("value", v["raw"]) for n, v in V["resolved"][t].items()} for t in V["resolved"]}


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
            return "#%02x%02x%02x" % (r, g, b) if a == 1 else "rgba(%d, %d, %d, %s)" % (r, g, b, ("%g" % a))
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
    if ty == "color":
        norm_color(val)
    if ty == "number" and not isinstance(val, (int, float)):
        raise ValueError(f"{path}: number {val!r}")


def leaf(path, spec, theme):
    ty = spec["type"]
    if "var" in spec:
        name = spec["var"]
        if name not in DECL[theme]:
            raise KeyError(f"{path}: {name} is not a resolved variable ({theme})")
        val = DECL[theme][name]
        src = f"css-var {name} ({theme})"
        if spec.get("source"):
            src += "; " + spec["source"]
    else:
        val = spec["value"]
        src = spec["source"]
    if ty == "color" and not str(val).startswith("{"):
        val = norm_color(val)
    if ty == "dimension":
        if isinstance(val, (int, float)):
            val = "%gpx" % val
        elif isinstance(val, str) and re.fullmatch(r"-?\d+(\.\d+)?", val.strip()):
            val = val.strip() + "px"
        elif isinstance(val, str) and val.endswith("px"):
            val = "%gpx" % float(val[:-2])
    if ty == "number" and isinstance(val, str) and re.fullmatch(r"-?\d+(\.\d+)?", val):
        val = float(val) if "." in val else int(val)
    check(path, ty, val)
    return {"$value": val, "$type": ty, "$extensions": {"source": src}}


def build(node, theme, path=""):
    if isinstance(node, dict) and "type" in node and ("value" in node or "var" in node):
        return leaf(path, node, theme)
    return {k: build(v, theme, f"{path}.{k}" if path else k) for k, v in node.items() if not k.startswith("_")}


core = build(SPEC["core"], "light")
light = build(SPEC["light"], "light")
dark = build(SPEC["dark"], "dark")
if SPEC.get("component"):
    dark["component"] = build(SPEC["component"], "dark")

def tokens_of(tree, prefix=""):
    for k, v in tree.items():
        if k.startswith("$"):
            continue
        if isinstance(v, dict) and "$value" in v:
            yield prefix + k, v
        elif isinstance(v, dict):
            yield from tokens_of(v, prefix + k + ".")


def aliases(v):
    if isinstance(v, str):
        return re.findall(r"\{([^{}]+)\}", v)
    if isinstance(v, dict):
        return [a for x in v.values() for a in aliases(x)]
    if isinstance(v, list):
        return [a for x in v for a in aliases(x)]
    return []


MEMBER = {"fontFamily": "fontFamily", "fontSize": "dimension", "fontWeight": "fontWeight",
          "lineHeight": "dimension", "letterSpacing": "dimension", "color": "color"}


def check_aliases(sets):
    """The kit's alias pass: every alias resolves in core or its own set, to a token of the type
    its place needs (a colour that aliases a dimension, or a typography size that aliases a
    colour, used to pass)."""
    core_tok = dict(tokens_of(sets["core"]))
    for name, tree in sets.items():
        by = dict(core_tok)
        by.update(dict(tokens_of(tree)))
        for n, t in tokens_of(tree):
            v = t["$value"]
            for a in aliases(v):
                if a not in by:
                    raise KeyError(f"{name}.{n}: alias {{{a}}} points at nothing")
            if isinstance(v, str) and aliases(v) and t["$type"] in ("color", "dimension", "fontFamily", "fontWeight"):
                if by[aliases(v)[0]]["$type"] != t["$type"]:
                    raise TypeError(f"{name}.{n}: alias {v} is a {by[aliases(v)[0]]['$type']}, not a {t['$type']}")
            items = v.items() if isinstance(v, dict) else [(k, x) for layer in v for k, x in layer.items()] if isinstance(v, list) and v and isinstance(v[0], dict) else []
            for k, m in items:
                want = MEMBER.get(k)
                if want and isinstance(m, str) and aliases(m) and by[aliases(m)[0]]["$type"] != want:
                    raise TypeError(f"{name}.{n}: {k} {m} is a {by[aliases(m)[0]]['$type']}, not a {want}")
            if t["$type"] == "shadow" and not isinstance(v, str):
                for layer in v:
                    for k in ("offsetX", "offsetY", "blur", "spread"):
                        if not re.fullmatch(r"-?\d*\.?\d+px", str(layer.get(k, ""))):
                            raise ValueError(f"{name}.{n}: shadow {k} {layer.get(k)!r}")
            if t["$type"] == "gradient" and not isinstance(v, str):
                if not all(isinstance(st, dict) and "color" in st and "position" in st for st in v):
                    raise ValueError(f"{name}.{n}: gradient {v!r} is not a list of colour stops")


check_aliases({"core": core, "light": light, "dark": dark})

tokens = {
    "core": core,
    "light": light,
    "dark": dark,
    "$themes": [
        {"id": "dark", "name": "Dark", "selectedTokenSets": {"core": "source", "dark": "enabled"},
         "$description": "The marketing site paints this near-black theme."},
        {"id": "light", "name": "Light", "selectedTokenSets": {"core": "source", "light": "enabled"},
         "$description": "The web reader sign-in card and the public newsletter paint light surfaces. These roles are the declared light --mr-* colours."},
    ],
    "$metadata": {"tokenSetOrder": ["core", "light", "dark"]},
}
TEXT = json.dumps(tokens, indent=2, ensure_ascii=False) + "\n"


def count(d):
    return sum(count(v) for v in d.values()) if isinstance(d, dict) and "$value" not in d else 1


if __name__ == "__main__":
    (HERE / "tokens.json").write_text(TEXT)
    print({k: count(v) for k, v in tokens.items() if k in ("core", "light", "dark")})
