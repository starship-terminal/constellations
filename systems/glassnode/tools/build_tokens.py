#!/usr/bin/env python3
"""Build tokens.json from raw/css-vars.json and raw/component-tokens.json.

Studio roles come from Ant Design custom properties resolved on the theme
holder. Marketing display type is measured. One light theme. Unread values
are omitted, never guessed.
"""
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
V = json.loads((RAW / "css-vars.json").read_text())
SPEC = json.loads((RAW / "component-tokens.json").read_text())
DECL = V["resolved"]["holder"]


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
            return "#%02x%02x%02x" % (r, g, b) if a >= 1 else "rgba(%d, %d, %d, %s)" % (r, g, b, ("%g" % a))
        return "#%02x%02x%02x" % (r, g, b)
    m = re.fullmatch(r"rgba?\(\s*([\d.]+)[,\s]+([\d.]+)[,\s]+([\d.]+)(?:\s*[,/]\s*([\d.]+%?))?\s*\)", v)
    if m:
        r, g, b = (round(float(x)) for x in m.group(1, 2, 3))
        a = m.group(4)
        if a is None:
            return "#%02x%02x%02x" % (r, g, b)
        a = float(a[:-1]) / 100 if a.endswith("%") else float(a)
        a = round(a, 3)
        return "#%02x%02x%02x" % (r, g, b) if a >= 1 else "rgba(%d, %d, %d, %g)" % (r, g, b, a)
    raise ValueError("not a colour: " + v)


DIM = re.compile(r"-?\d+(\.\d+)?(px|rem|em)")


def check(path, ty, val):
    if isinstance(val, str) and val.startswith("{"):
        return
    if ty == "dimension" and not DIM.fullmatch(str(val).strip()):
        raise ValueError(f"{path}: dimension {val!r}")
    if ty == "color":
        norm_color(val)
    if ty == "fontWeight" and not isinstance(val, int):
        raise ValueError(f"{path}: fontWeight {val!r}")
    if ty == "duration" and not re.fullmatch(r"\d+ms", str(val)):
        raise ValueError(f"{path}: duration {val!r}")
    if ty == "cubicBezier" and not (isinstance(val, list) and len(val) == 4):
        raise ValueError(f"{path}: cubicBezier {val!r}")
    if ty == "fontFamily" and not isinstance(val, str):
        raise ValueError(f"{path}: fontFamily {val!r}")


def leaf(path, spec):
    ty = spec["type"]
    if ty == "other":
        raise ValueError(path + " is not tokenised")
    if "var" in spec:
        name = spec["var"]
        if name not in DECL:
            raise KeyError(f"{path}: {name} unread")
        val = DECL[name]
        src = f"css-var {name} resolved on studio theme holder"
    else:
        val = spec["value"]
        src = spec["source"]
        if isinstance(val, str) and val.strip().lower() == "not captured":
            raise ValueError(path + " not captured")
    if ty == "color":
        val = norm_color(val)
    if ty == "cubicBezier" and isinstance(val, str):
        m = re.fullmatch(r"cubic-bezier\(\s*([-\d.]+)[,\s]+([-\d.]+)[,\s]+([-\d.]+)[,\s]+([-\d.]+)\s*\)", val.strip())
        if not m:
            raise ValueError(f"{path}: easing {val!r}")
        val = [float(x) for x in m.groups()]
    if ty == "duration" and isinstance(val, str):
        m = re.fullmatch(r"([\d.]+)s", val.strip())
        if m:
            val = "%gms" % (float(m.group(1)) * 1000)
    if ty == "dimension" and isinstance(val, str):
        val = re.sub(r"(\d+\.\d{3})\d+", lambda m: "%g" % round(float(m.group(1)), 3), val.strip())
        if " " in val:
            # multi-corner radius: keep the first length if all match, else first
            parts = val.split()
            if len(set(parts)) == 1:
                val = parts[0]
            else:
                val = parts[0]
                src += "; corners " + spec["value"]
    if ty == "fontWeight" and isinstance(val, str) and val.isdigit():
        val = int(val)
    check(path, ty, val)
    return {"$value": val, "$type": ty, "$extensions": {"source": src}}


def build(node, path=""):
    if isinstance(node, dict) and "type" in node and ("value" in node or "var" in node):
        return leaf(path, node)
    return {k: build(v, f"{path}.{k}" if path else k) for k, v in node.items() if not k.startswith("_")}


core = build(SPEC["core"])
light = build(SPEC["light"])
light["component"] = build(SPEC["component"])

# typography composites from measured display + ant body
core["typography"] = {
    "display": {
        "$type": "typography",
        "$value": {
            "fontFamily": core["font"]["family"]["display"]["$value"],
            "fontSize": core["font"]["size"]["display"]["$value"],
            "fontWeight": core["font"]["weight"]["display"]["$value"],
            "lineHeight": light["component"]["type"]["display-line-height"]["$value"],
        },
        "$extensions": {"source": "measured glassnode.com h1 computed style"},
    },
    "body": {
        "$type": "typography",
        "$value": {
            "fontFamily": core["font"]["family"]["ui"]["$value"],
            "fontSize": core["font"]["size"]["body"]["$value"],
            "fontWeight": core["font"]["weight"]["ui"]["$value"],
            "lineHeight": "22px",
        },
        "$extensions": {"source": "css-var --ant-font-size plus measured Sign up button font; line-height measured button-primary default lineHeight"},
    },
}
# fix body line-height from the measurement rather than a literal
lh = json.loads((RAW / "components-computed.json").read_text())["components"]["button-primary"]["default"]["lineHeight"]
core["typography"]["body"]["$value"]["lineHeight"] = ("%g" % round(float(lh.replace("px", "")), 3)) + "px"
core["typography"]["body"]["$extensions"]["source"] = "font family and size from Sign up button and --ant-font-size; line-height measured button-primary default"

tokens = {
    "core": core,
    "light": light,
    "$themes": [{
        "id": "light",
        "name": "Light",
        "selectedTokenSets": {"core": "source", "light": "enabled"},
        "$description": "The only theme captured. Neither glassnode.com nor the public Studio shell exposed a theme switch.",
    }],
    "$metadata": {"tokenSetOrder": ["core", "light"]},
}
(HERE / "tokens.json").write_text(json.dumps(tokens, indent=2, ensure_ascii=False) + "\n")


def count(d):
    return sum(count(v) for v in d.values()) if isinstance(d, dict) and "$value" not in d else 1


print({k: count(v) for k, v in tokens.items() if k in ("core", "light")})
