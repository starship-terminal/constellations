#!/usr/bin/env python3
"""Build tokens.json from systems/pampam/raw readings.

Brand colours, type roles and control sizes come from raw/component-tokens.json
(computed styles and utility-class declarations, 2026-11-21). The Panda preset
scales (spacing, radii, duration, easing, breakpoints) come from raw/css-vars.json.
PamPam publishes one light theme. Every token carries $extensions.source.
"""
import json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
SPEC = json.loads((RAW / "component-tokens.json").read_text())
VARS = json.loads((RAW / "css-vars.json").read_text())

DIM = re.compile(r"-?\d*\.?\d+(px|rem)")


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


def check(path, ty, val):
    if isinstance(val, str) and val.startswith("{"):
        return
    if ty == "dimension" and not DIM.fullmatch(str(val)):
        raise ValueError(f"{path}: dimension must be one px or rem length, got {val!r}")
    if ty == "color":
        norm_color(val)
    if ty == "fontWeight" and not isinstance(val, int):
        raise ValueError(f"{path}: fontWeight {val!r}")
    if ty == "duration" and not re.fullmatch(r"\d+ms", str(val)):
        raise ValueError(f"{path}: duration {val!r}")
    if ty == "cubicBezier" and not (isinstance(val, list) and len(val) == 4):
        raise ValueError(f"{path}: cubicBezier {val!r}")


def leaf(path, spec):
    ty = spec["type"]
    if not spec.get("source"):
        raise ValueError(f"{path}: leaf without a source")
    val = spec["value"]
    if ty == "color" and not str(val).startswith("{"):
        val = norm_color(val)
    if ty == "fontWeight" and isinstance(val, str) and val.isdigit():
        val = int(val)
    if ty == "dimension" and isinstance(val, str) and re.fullmatch(r"-?\d+(\.\d+)?", val):
        val += "px"
    check(path, ty, val)
    token = {"$value": val, "$type": ty, "$extensions": {"source": spec["source"]}}
    if spec.get("description"):
        token["$description"] = spec["description"]
    return token


def build(node, path=""):
    if isinstance(node, dict) and "type" in node and "value" in node:
        return leaf(path, node)
    if isinstance(node, dict) and "$value" in node:
        return node
    out = {}
    for k, v in node.items():
        if k.startswith("_"):
            continue
        out[k] = build(v, f"{path}.{k}" if path else k)
    return out


def panda_dim(name, value, source):
    if not DIM.fullmatch(value):
        raise ValueError(f"{name}: {value!r}")
    return {"$value": value, "$type": "dimension", "$extensions": {"source": source}}


def core_scales():
    src = "Measured. Panda preset custom property in the 2026-11-21 stylesheet, raw/css-vars.json."
    space, radius, motion = {}, {}, {}
    for name, value in VARS["scale"].items():
        if name.startswith("--spacing-"):
            space[name.removeprefix("--spacing-")] = panda_dim(name, value, src + f" {name}.")
        elif name.startswith("--radii-"):
            radius[name.removeprefix("--radii-")] = panda_dim(name, value, src + f" {name}.")
        elif name.startswith("--durations-"):
            motion[name.removeprefix("--durations-")] = {
                "$value": value, "$type": "duration", "$extensions": {"source": src + f" {name}."}
            }
    easing = {
        "$value": [0.4, 0, 0.2, 1],
        "$type": "cubicBezier",
        "$extensions": {"source": src + " --easings-default: cubic-bezier(0.4, 0, 0.2, 1)."},
    }
    return space, radius, motion, easing


def main():
    space, panda_radius, durations, easing = core_scales()
    built = build(SPEC)
    core = {
        "color": built["color"],
        "font": built["font"],
        "typography": built["typography"],
        "radius": {**panda_radius, "control": built["radius"]},
        "space": space,
        "size": built["size"],
        "shadow": built["shadow"],
        "motion": {**durations, "easing": easing, "observed": built["motion"]},
        "layout": built["layout"],
    }
    light = {
        "background": {
            "page": alias("color.white", "Page behind marketing sections is white. The home hero is a photograph, not a token."),
            "surface": alias("color.card", "Pricing plan cards."),
            "parchment": alias("color.parchment", "Feature tile fill."),
            "quiet": alias("color.quiet", "Quiet button fill."),
            "inverse": alias("color.black", "Make map control fill."),
        },
        "text": {
            "primary": alias("color.ink", "Headings and plan names."),
            "muted": alias("color.lavender", "Nav, footer and lede."),
            "menu": alias("color.menu", "Solutions menu items."),
            "disabled": alias("color.ash", "Quiet button label."),
            "onAccent": alias("color.white", "Primary button label."),
            "link": alias("color.lavender", "Nav and footer links. Hover on the Pricing link did not change colour."),
        },
        "border": {
            "default": alias("color.hairline", "Quiet button hairline."),
            "strong": alias("color.planBorder", "Business plan card."),
            "accent": alias("color.blueDeep", "Primary button border."),
        },
        "accent": {
            "default": alias("color.blue", "Get Explorer / Get Business fill."),
            "pressed": alias("color.blueDeep", "Primary button border. A distinct pressed fill was not captured."),
            "lip": alias("color.blueLip", "Primary button inset highlight."),
        },
        "focus": {
            "ring": alias("color.focus", "Browser outline on the focused Pricing link. The product does not paint its own ring."),
        },
    }
    doc = {
        "$schema": "https://www.designtokens.org/schemas/2025.10/format.json",
        "core": core,
        "light": light,
        "$themes": [{"id": "light", "name": "Light", "selectedTokenSets": {"core": "source", "light": "enabled"}}],
    }
    (HERE / "tokens.json").write_text(json.dumps(doc, indent=2) + "\n")
    print("wrote", HERE / "tokens.json")


def alias(path, note):
    return {
        "$value": "{" + path + "}",
        "$type": "color",
        "$description": note,
        "$extensions": {"source": "Derived. Alias of core." + path + ". " + note},
    }


if __name__ == "__main__":
    main()
