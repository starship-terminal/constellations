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
COMP = json.loads((HERE / "raw" / "components-computed.json").read_text())["components"]
MOTION = json.loads((HERE / "raw" / "motion.json").read_text())
SRC = "css-var"
# docs/EVIDENCE.md: a value typed into the builder with no reading in raw/ is a Reconstruction.
HAND = "Reconstruction: entered by hand at capture time; no reading in raw/ holds it."
# CSS easing keywords as the cubic-bezier() they are defined to be (CSS Easing Functions 1).
KEYWORD_EASING = {"ease": [0.25, 0.1, 0.25, 1], "ease-in": [0.42, 0, 1, 1], "ease-out": [0, 0, 0.58, 1],
                  "ease-in-out": [0.42, 0, 0.58, 1], "linear": [0, 0, 1, 1]}


def reading(comp, state="default"):
    """One state of a measured component in raw/components-computed.json; a missing one raises."""
    return COMP[comp]["states"][state]


def declared_transition(selector):
    """The transition the atomic sheet declares on `selector`, as raw/motion.json recorded it."""
    for page in MOTION["pages"].values():
        for d in page["declared"]:
            if d["selector"] == selector:
                return d["transition"]
    raise KeyError(f"{selector}: no declared transition in raw/motion.json")


def first_declared_with(word):
    """The first selector (by name) whose declared transition uses an easing keyword."""
    hits = sorted({(d["selector"], d["transition"]) for page in MOTION["pages"].values()
                   for d in page["declared"] if re.search(rf"(?<![\w-]){re.escape(word)}(?![\w-])", d["transition"])})
    if not hits:
        raise KeyError(f"no declared transition in raw/motion.json uses {word}")
    return hits[0]


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


def dim_ms(name):
    v = str(RESOLVED.get(name) or declared(name)).strip()
    m = re.fullmatch(r"([\d.]+)(m?s)", v)
    if not m:
        raise ValueError(f"{name}: not a duration: {v}")
    return "%gms" % (float(m.group(1)) * (1 if m.group(2) == "ms" else 1000))


def declared(name):
    for d in RAW["declarations"]:
        props = d.get("properties") or d.get("props") or {}
        if name in props:
            return props[name]
    raise KeyError(f"{name}: not declared in raw/css-vars.json")


def nest(tree, parts, leaf):
    """Place a leaf at a path without nesting it inside another leaf.

    --kds-color-x and --kds-color-x-y both split on "-", so the second would land
    inside the first leaf, where tools/catalog.py's flatten (it stops at $value)
    never sees it. When the walk reaches a leaf, the rest of the name stays joined
    with "-" as a sibling key (x and x-y). A path that is already taken raises.
    """
    node = tree
    for i, p in enumerate(parts[:-1]):
        nxt = node.get(p)
        if isinstance(nxt, dict) and "$value" in nxt:
            parts = parts[:i] + ["-".join(parts[i:])]
            break
        node = node.setdefault(p, {})
    if parts[-1] in node:
        raise ValueError("token path already taken: " + ".".join(parts))
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
        "$value": [f.strip().strip('"') for f in RAW["fontBody"].split(",")],
        "$extensions": {"source": "computed font-family on body, https://www.kickstarter.com/ 2026-11-18 (raw/css-vars.json fontBody); Inter loaded from fonts.googleapis.com. Effra is declared in one @font-face and was not the computed body family."},
    }


def typography():
    # display is the home hero h1 as raw/components-computed.json read it. The
    # other roles were typed in at capture time from the atomic type class names;
    # no reading in raw/ holds them, so they are Reconstructions.
    h1 = reading("hero-h1")["style"]
    roles = {
        "display": {"fontSize": h1["fontSize"], "lineHeight": h1["lineHeight"], "fontWeight": int(h1["fontWeight"]),
                    "source": "computed fontSize, lineHeight and fontWeight of hero-h1 default on https://www.kickstarter.com/, 2026-11-18 (raw/components-computed.json): the home hero h1"},
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
                "fontFamily": "{font.family.sans}",
                "fontSize": r["fontSize"],
                "fontWeight": r["fontWeight"],
                "lineHeight": r["lineHeight"],
            },
            "$extensions": {"source": r.get("source") or f"{HAND} Intended for {r['note']}."},
        }
    return out


def core():
    radius = {
        "small": dim_px("--kds-dimension-corner-radius-small"),
        "medium": dim_px("--kds-dimension-corner-radius-medium"),
        "large": dim_px("--kds-dimension-corner-radius-large"),
    }
    # The spacing steps were picked by hand at capture time on a 4px module; Kickstarter
    # declares no spacing scale, so every step but the measured search height is a
    # Reconstruction. Steps that equal a declared value say which.
    def step(px, note):
        return {"$type": "dimension", "$value": f"{px}px", "$extensions": {"source": f"{HAND} {note}"}}

    def same_as(name):
        v = dim_px(name)["$value"]
        return v, f"Equals the declared {name} ({v}), which is not a spacing value."

    v2, n2 = same_as("--kds-elevation-1-y")
    v4, n4 = same_as("--kds-dimension-corner-radius-small")
    v8, n8 = same_as("--kds-dimension-corner-radius-medium")
    v16, n16 = same_as("--kds-dimension-corner-radius-large")
    search = reading("search")
    named = {
        "0": step(0, "The zero step of the 4px module."),
        "2": step(int(v2[:-2]), n2),
        "4": step(int(v4[:-2]), "The 4px module base. " + n4),
        "8": step(int(v8[:-2]), n8),
        "12": step(12, "3 x the 4px module."),
        "16": step(int(v16[:-2]), n16),
        "24": step(24, "6 x the 4px module, used as the header and card padding step."),
        "32": step(32, "8 x the 4px module."),
        "40": step(40, "A control height; the measured header search is 48px including padding."),
        "48": {"$type": "dimension", "$value": "%gpx" % search["rect"]["h"],
               "$extensions": {"source": "measured height of search default on https://www.kickstarter.com/, 2026-11-18 (raw/components-computed.json): the home header search field"}},
        "64": step(64, "16 x the 4px module, used as the section gap."),
    }
    h1 = reading("hero-h1")["style"]
    font_size = {
        "caption": step(12, "The caption step of the Inter scale."),
        "label": step(14, "The label and meta step."),
        "body": step(16, "The body size."),
        "heading-sm": step(18, "The card-title step."),
        "heading-md": step(22, "The section-heading step."),
        "heading-lg": step(28, "Named after the kds-type-heading-lg class on the editorial banner."),
        "display": {"$type": "dimension", "$value": h1["fontSize"],
                    "$extensions": {"source": "computed fontSize of hero-h1 default on https://www.kickstarter.com/, 2026-11-18 (raw/components-computed.json): the home hero h1"}},
    }
    for v in font_size.values():
        v["$type"] = "dimension"
    expand = declared_transition(".expandable-background")
    fast = re.match(r"(?:\S+\s+)?([\d.]+)(m?s)\b", expand)
    fast_ms = "%gms" % (float(fast.group(1)) * (1 if fast.group(2) == "ms" else 1000))
    out_sel, out_tr = first_declared_with("ease-out")
    motion = {
        "duration": {
            "fast": {"$type": "duration", "$value": fast_ms, "$extensions": {"source": f"declared transition `{expand}` on .expandable-background in the atomic sheet (raw/motion.json)"}},
            "nav": {"$type": "duration", "$value": dim_ms("--creator-nav-transition-duration"), "$extensions": {"source": "declared --creator-nav-transition-duration under prefers-reduced-motion: no-preference (raw/css-vars.json)"}},
            "enter": {"$type": "duration", "$value": "300ms", "$extensions": {"source": f"{HAND} Typed from the 300ms translate on .creator-nav__submenu when open."}},
        },
        "easing": {
            "out": {"$type": "cubicBezier", "$value": KEYWORD_EASING["ease-out"], "$extensions": {"source": f"the ease-out keyword as CSS defines it, cubic-bezier(0, 0, 0.58, 1); declared on {out_sel} (`{out_tr}`) and other kds rules in raw/motion.json"}},
            "nav": {"$type": "cubicBezier", "$value": [0, 1, 1, 1], "$extensions": {"source": f"{HAND} Typed from cubic-bezier(0, 1, 1, 1) on .creator-nav__submenu."}},
        },
    }
    bordered = sorted(k for k, c in COMP.items() if c["states"].get("default", {}).get("style", {}).get("borderTopWidth") == "1px")
    border_width = {
        "hairline": {"$type": "dimension", "$value": reading(bordered[0])["style"]["borderTopWidth"],
                     "$extensions": {"source": f"computed borderTopWidth of {bordered[0]} default, 2026-11-18 (raw/components-computed.json); the same 1px on {', '.join(bordered[1:])}"}},
        "none": step(0, "The zero border."),
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


def build():
    """The whole token document, checked, without writing it."""
    doc = {
        "$description": "Kickstarter public design system (KDS), captured 2026-11-18 from kickstarter.com signed out. One light theme.",
        "core": core(),
        "light": light(),
        "$themes": [{"id": "light", "name": "Light", "selectedTokenSets": {"core": "source", "light": "enabled"}}],
    }
    check(doc["core"])
    check(doc["light"])
    return doc


def main():
    doc = build()
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
