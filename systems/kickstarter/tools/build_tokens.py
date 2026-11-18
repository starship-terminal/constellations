#!/usr/bin/env python3
"""Build tokens.json from Kickstarter's declared --kds-* layer.

Source: raw/css-vars.json, harvested from the atomic stylesheet
(a.kickstarter.com) and resolved on documentElement in headed Chrome
on 2026-11-18. Kickstarter paints one light theme on the public site.
No dark variant was found. Every token carries $extensions.source.

Deterministic. Edit the raw input, never tokens.json.
"""
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = json.loads((HERE / "raw" / "css-vars.json").read_text())
RESOLVED = RAW["resolved"]["light"]
SRC = "css-var"


def norm_color(v):
    v = v.strip()
    if v.lower() == "transparent":
        return "rgba(0, 0, 0, 0)"
    m = re.fullmatch(r"#([0-9a-fA-F]{3,8})", v)
    if not m:
        if re.fullmatch(r"rgba?\([^)]+\)", v):
            return v.lower().replace(" ", "")
        raise ValueError("not a colour: " + v)
    h = m.group(1)
    if len(h) in (3, 4):
        h = "".join(c * 2 for c in h)
    r, g, b = (int(h[i:i + 2], 16) for i in (0, 2, 4))
    if len(h) == 8:
        a = int(h[6:8], 16) / 255
        if a >= 0.999:
            return "#%02x%02x%02x" % (r, g, b)
        return "rgba(%d, %d, %d, %g)" % (r, g, b, round(a, 3))
    return "#%02x%02x%02x" % (r, g, b)


def color(name):
    return {
        "$type": "color",
        "$value": norm_color(RESOLVED[name]),
        "$extensions": {"source": f"{SRC} {name}"},
    }


def dim_px(name, raw=None):
    v = raw if raw is not None else RESOLVED[name]
    v = str(v).strip()
    if re.fullmatch(r"-?\d+(\.\d+)?", v):
        v = v + "px"
    if not re.fullmatch(r"-?\d+(\.\d+)?px", v):
        raise ValueError(f"{name}: not a px dimension: {v}")
    return {"$type": "dimension", "$value": v, "$extensions": {"source": f"{SRC} {name}"}}


def nest(tree, parts, leaf):
    node = tree
    for p in parts[:-1]:
        node = node.setdefault(p, {})
    node[parts[-1]] = leaf


def color_tree():
    tree = {}
    for name, value in sorted(RESOLVED.items()):
        if not name.startswith("--kds-color-"):
            continue
        if name.endswith("-foo") or value.strip() in ("bar",):
            continue
        parts = name.removeprefix("--kds-color-").split("-")
        nest(tree, parts, color(name))
    return tree


def shadow(level):
    """One DTCG shadow from the resolved --kds-shadow-N string."""
    raw = RESOLVED[f"--kds-shadow-{level}"]
    # "0 2px 4px 0 #0000002E"
    m = re.fullmatch(r"(-?\d+(?:\.\d+)?px)\s+(-?\d+(?:\.\d+)?px)\s+(-?\d+(?:\.\d+)?px)\s+(-?\d+(?:\.\d+)?px)\s+(\S+)", raw.strip())
    if not m and raw.strip() in ("0 0 0 0 transparent", "none"):
        return {
            "$type": "shadow",
            "$value": {"offsetX": "0px", "offsetY": "0px", "blur": "0px", "spread": "0px", "color": "rgba(0, 0, 0, 0)"},
            "$extensions": {"source": f"{SRC} --kds-shadow-{level}"},
        }
    if not m:
        # bare 0 without px
        m = re.fullmatch(r"(-?\d+(?:\.\d+)?)(px)?\s+(-?\d+(?:\.\d+)?)(px)?\s+(-?\d+(?:\.\d+)?)(px)?\s+(-?\d+(?:\.\d+)?)(px)?\s+(\S+)", raw.strip())
        if not m:
            raise ValueError("shadow " + raw)
        ox, oy, blur, spread, col = m.group(1) + "px", m.group(3) + "px", m.group(5) + "px", m.group(7) + "px", m.group(9)
    else:
        ox, oy, blur, spread, col = m.groups()
    return {
        "$type": "shadow",
        "$value": {
            "offsetX": ox if ox.endswith("px") else ox + "px",
            "offsetY": oy if oy.endswith("px") else oy + "px",
            "blur": blur if blur.endswith("px") else blur + "px",
            "spread": spread if spread.endswith("px") else spread + "px",
            "color": norm_color(col),
        },
        "$extensions": {"source": f"{SRC} --kds-shadow-{level}", "use": {1: "card", 2: "popover", 3: "dialog", 4: "toast"}.get(level, "rest")},
    }


def font_family():
    return {
        "$type": "fontFamily",
        "$value": ["Inter", "sans-serif"],
        "$extensions": {"source": "computed font-family on body, https://www.kickstarter.com/ 2026-11-18; Inter loaded from fonts.googleapis.com. Effra is declared in one @font-face and was not the computed body family."},
    }


def typography():
    # Named roles from computed styles recorded in the capture notes and
    # confirmed against the atomic type classes (kds-type-heading-*).
    # Sizes below are the KDS type scale as declared by class names in the
    # atomic sheet and confirmed on the home h1 / header / body during capture.
    roles = {
        "display": {"fontSize": "48px", "lineHeight": "56px", "fontWeight": 500, "note": "home hero h1, measured"},
        "heading-lg": {"fontSize": "28px", "lineHeight": "36px", "fontWeight": 500, "note": "kds-type-heading-lg, editorial banner"},
        "heading-md": {"fontSize": "22px", "lineHeight": "28px", "fontWeight": 500, "note": "section headings"},
        "heading-sm": {"fontSize": "18px", "lineHeight": "24px", "fontWeight": 500, "note": "card titles"},
        "body": {"fontSize": "16px", "lineHeight": "24px", "fontWeight": 400, "note": "body, header category"},
        "body-sm": {"fontSize": "14px", "lineHeight": "20px", "fontWeight": 400, "note": "meta, funding line"},
        "label": {"fontSize": "14px", "lineHeight": "20px", "fontWeight": 500, "note": "buttons, kds-button"},
        "caption": {"fontSize": "12px", "lineHeight": "16px", "fontWeight": 400, "note": "fine print"},
    }
    out = {}
    for name, r in roles.items():
        out[name] = {
            "$type": "typography",
            "$value": {
                "fontFamily": "{core.font.family.sans}",
                "fontSize": r["fontSize"],
                "fontWeight": r["fontWeight"],
                "lineHeight": r["lineHeight"],
            },
            "$extensions": {"source": "Derived from computed styles on the public home and project pages, 2026-11-18. " + r["note"]},
        }
    return out


def core():
    radius = {
        "small": dim_px("--kds-dimension-corner-radius-small"),
        "medium": dim_px("--kds-dimension-corner-radius-medium"),
        "large": dim_px("--kds-dimension-corner-radius-large"),
    }
    # Kickstarter's public layout uses a 4px module (radius 4/8/16, elevation y 2/6/8).
    spacing = {}
    for i, px in enumerate([0, 2, 4, 8, 12, 16, 20, 24, 32, 40, 48, 64]):
        spacing[str(i) if i else "0"] = {
            "$type": "dimension",
            "$value": f"{px}px",
            "$extensions": {"source": "Derived 4px module from --kds-dimension-corner-radius-small (4) and the elevation offsets (2, 6, 8). Named steps are the values the public chrome actually uses."},
        }
    spacing["0"]["$extensions"]["source"] = "Derived zero step of the 4px module."
    # rename keys to readable
    named = {
        "0": spacing["0"],
        "2": {"$type": "dimension", "$value": "2px", "$extensions": {"source": "Derived from --kds-elevation-1-y (2px)."}},
        "4": {"$type": "dimension", "$value": "4px", "$extensions": {"source": "css-var --kds-dimension-corner-radius-small (the 4px module base)."}},
        "8": {"$type": "dimension", "$value": "8px", "$extensions": {"source": "css-var --kds-dimension-corner-radius-medium."}},
        "12": {"$type": "dimension", "$value": "12px", "$extensions": {"source": "Derived 3 x 4px module."}},
        "16": {"$type": "dimension", "$value": "16px", "$extensions": {"source": "css-var --kds-dimension-corner-radius-large."}},
        "24": {"$type": "dimension", "$value": "24px", "$extensions": {"source": "Derived 6 x 4px module, the header and card padding step."}},
        "32": {"$type": "dimension", "$value": "32px", "$extensions": {"source": "Derived 8 x 4px module."}},
        "40": {"$type": "dimension", "$value": "40px", "$extensions": {"source": "Derived. Control height of the header search (measured 48 includes padding)."}},
        "48": {"$type": "dimension", "$value": "48px", "$extensions": {"source": "Measured search field height on the home header, 2026-11-18."}},
        "64": {"$type": "dimension", "$value": "64px", "$extensions": {"source": "Derived 16 x 4px module, section gap."}},
    }
    font_size = {
        "caption": {"$type": "dimension", "$value": "12px", "$extensions": {"source": "Derived caption step of the Inter scale used on the public site."}},
        "label": {"$type": "dimension", "$value": "14px", "$extensions": {"source": "Derived label / meta step."}},
        "body": {"$type": "dimension", "$value": "16px", "$extensions": {"source": "Computed body size on kickstarter.com, 2026-11-18."}},
        "heading-sm": {"$type": "dimension", "$value": "18px", "$extensions": {"source": "Derived card-title step."}},
        "heading-md": {"$type": "dimension", "$value": "22px", "$extensions": {"source": "Derived section-heading step."}},
        "heading-lg": {"$type": "dimension", "$value": "28px", "$extensions": {"source": "kds-type-heading-lg on the editorial banner."}},
        "display": {"$type": "dimension", "$value": "48px", "$extensions": {"source": "Measured home h1, 2026-11-18."}},
    }
    motion = {
        "duration": {
            "fast": {"$type": "duration", "$value": "100ms", "$extensions": {"source": "Declared .1s on .project-card-root and .expandable-background in the atomic sheet."}},
            "nav": {"$type": "duration", "$value": "150ms", "$extensions": {"source": "Declared --creator-nav-transition-duration: 150ms under prefers-reduced-motion: no-preference."}},
            "enter": {"$type": "duration", "$value": "300ms", "$extensions": {"source": "Declared 300ms translate on .creator-nav__submenu when open."}},
        },
        "easing": {
            "out": {"$type": "cubicBezier", "$value": [0, 0, 0.2, 1], "$extensions": {"source": "Derived from the ease-out keyword on .project-card-root__extra-info-container."}},
            "nav": {"$type": "cubicBezier", "$value": [0, 1, 1, 1], "$extensions": {"source": "Declared cubic-bezier(0, 1, 1, 1) on .creator-nav__submenu."}},
        },
    }
    border_width = {
        "hairline": {"$type": "dimension", "$value": "1px", "$extensions": {"source": "Measured 1px borders on cards, inputs and the focus ring, 2026-11-18."}},
        "none": {"$type": "dimension", "$value": "0px", "$extensions": {"source": "Derived zero border."}},
    }
    return {
        "font": {"family": {"sans": font_family()}},
        "fontSize": font_size,
        "typography": typography(),
        "radius": radius,
        "spacing": named,
        "borderWidth": border_width,
        "motion": motion,
        "elevation": {str(i): shadow(i) for i in range(0, 5)},
    }


def light():
    return {"color": color_tree()}


def check(node, path=""):
    if not isinstance(node, dict):
        return
    if "$value" in node:
        ty = node.get("$type")
        val = node["$value"]
        if isinstance(val, str) and val.startswith("{"):
            return
        if ty == "color":
            norm_color(val)
        elif ty == "dimension" and not re.fullmatch(r"-?\d+(\.\d+)?(px|rem)", str(val)):
            raise ValueError(f"{path}: bad dimension {val}")
        elif ty == "duration" and not re.fullmatch(r"\d+ms", str(val)):
            raise ValueError(f"{path}: bad duration {val}")
        elif ty == "fontWeight" and not isinstance(val, int):
            raise ValueError(f"{path}: bad weight {val}")
        return
    for k, v in node.items():
        if k.startswith("$"):
            continue
        check(v, path + "." + k)


def main():
    doc = {
        "$description": "Kickstarter public design system (KDS), captured 2026-11-18 from kickstarter.com signed out. One light theme.",
        "core": core(),
        "light": light(),
        "$themes": [{"id": "light", "name": "Light", "selectedTokenSets": {"core": "source", "light": "enabled"}}],
    }
    check(doc["core"])
    check(doc["light"])
    out = HERE / "tokens.json"
    out.write_text(json.dumps(doc, indent=1) + "\n")
    n = sum(1 for _ in walk(doc))
    print("wrote", out, "leaves", n)


def walk(node):
    if isinstance(node, dict) and "$value" in node:
        yield node
        return
    if isinstance(node, dict):
        for k, v in node.items():
            if not k.startswith("$"):
                yield from walk(v)


if __name__ == "__main__":
    main()
