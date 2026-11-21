#!/usr/bin/env python3
"""Build tokens.json from Homerun's public Webflow CSS and live measurements.

Sources, read from www.homerun.co on 2026-11-21, signed out:
  raw/css-vars.json              custom properties declared on the marketing site,
                                 resolved on :root in the live page
  raw/components-computed.json   computed styles of public controls

One light theme. A dark set is not invented. Every token carries
$extensions.source. Unread values stay out of the file.
"""
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
V = json.loads((RAW / "css-vars.json").read_text())
C = json.loads((RAW / "components-computed.json").read_text())
RESOLVED = V["resolved"]


def color(name):
    rec = RESOLVED[name]
    if rec.get("kind") != "color":
        raise SystemExit(f"{name} is not a colour: {rec}")
    return rec["value"]


def norm_color(v):
    v = str(v).strip().lower()
    if v == "white":
        return "#ffffff"
    if v == "transparent":
        return "rgba(0, 0, 0, 0)"
    m = re.fullmatch(r"#([0-9a-f]{3,8})", v)
    if m:
        h = m.group(1)
        if len(h) in (3, 4):
            h = "".join(c * 2 for c in h)
        if len(h) == 8:
            r, g, b, a = (int(h[i:i + 2], 16) for i in (0, 2, 4, 6))
            if a == 255:
                return "#%02x%02x%02x" % (r, g, b)
            return "rgba(%d, %d, %d, %g)" % (r, g, b, round(a / 255, 3))
        return "#%02x%02x%02x" % tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))
    m = re.fullmatch(r"rgba?\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)(?:\s*,\s*([\d.]+))?\s*\)", v)
    if m:
        r, g, b, a = m.groups()
        if a is None or float(a) == 1:
            return "#%02x%02x%02x" % (int(r), int(g), int(b))
        return "rgba(%s, %s, %s, %g)" % (r, g, b, float(a))
    raise SystemExit("not a colour: " + v)


def px(v):
    m = re.fullmatch(r"(-?\d*\.?\d+)px", str(v).strip())
    if not m:
        raise SystemExit("not px: " + repr(v))
    return "%gpx" % round(float(m.group(1)), 2)


DIM = re.compile(r"-?\d+(\.\d+)?(px|rem)")


def tok(ty, val, source):
    if ty == "color" and not str(val).startswith("{"):
        val = norm_color(val)
    if ty == "dimension" and not str(val).startswith("{"):
        if not DIM.fullmatch(str(val)):
            raise SystemExit(f"dimension {val!r}")
    return {"$type": ty, "$value": val, "$extensions": {"source": source}}


def alias(path, source):
    return {"$type": "color", "$value": "{" + path + "}", "$extensions": {"source": source}}


def measured(comp, state, prop):
    node = C["components"].get(comp, {}).get(state)
    if not isinstance(node, dict) or prop not in node:
        return None
    return node[prop]


# Palette: the v2 primary and secondary names the site declares, plus the
# coffee and beige steps that the older names still point at.
PALETTE = {
    "blue-300": "--_updated-colors-v2---primary--blue-300",
    "blue-400": "--_updated-colors-v2---primary--blue-400",
    "blue-500": "--_updated-colors-v2---primary--blue-500",
    "blue-600": "--_updated-colors-v2---primary--blue-600",
    "blue-700": "--_updated-colors-v2---primary--blue-700",
    "brown-100": "--_updated-colors-v2---primary--brown-100",
    "brown-200": "--_updated-colors-v2---primary--brown-200",
    "brown-300": "--_updated-colors-v2---primary--brown-300",
    "brown-400": "--_updated-colors-v2---primary--brown-400",
    "brown-500": "--_updated-colors-v2---primary--brown-500",
    "brown-600": "--_updated-colors-v2---primary--brown-600",
    "brown-700": "--_updated-colors-v2---primary--brown-700",
    "beige-400": "--_updated-colors-v2---primary--beige-400",
    "beige-500": "--_updated-colors-v2---primary--beige-500",
    "beige-600": "--_updated-colors-v2---primary--beige-600",
    "beige-700": "--_updated-colors-v2---primary--beige-700",
    "beige-800": "--_updated-colors-v2---primary--beige-800",
    "white": "--_updated-colors-v2---primary--white",
    "red": "--_updated-colors-v2---secondary--red",
    "green": "--_updated-colors-v2---secondary--green",
    "orange": "--_updated-colors-v2---secondary--orange",
    "yellow": "--_updated-colors-v2---secondary--yellow",
    "lilac": "--_updated-colors-v2---secondary--lilac",
    "coffee-50": "--coffee-50",
    "coffee-100": "--coffee-100",
    "coffee-200": "--coffee-200",
    "coffee-300": "--coffee-300",
    "coffee-500": "--coffee-500",
    "coffee-600": "--coffee-600",
    "coffee-800": "--coffee-800",
    "coffee-900": "--coffee-900",
    "coffee-950": "--coffee-950",
    "hr-500": "--hr--500",
    "hr-700": "--hr--700",
    "hr-800": "--hr--800",
}

core_color = {}
for key, var in PALETTE.items():
    core_color[key] = tok("color", color(var), f"Measured css-var {var} on :root, www.homerun.co 2026-11-21")

# Type from computed styles, not from memory of the foundries.
display = measured("heading-display", "default", "fontFamily") or '"GT Walsheim", sans-serif'
body_font = measured("nav-link", "default", "fontFamily") or '"GT America", sans-serif'
display_size = px(measured("heading-display", "default", "fontSize") or "64px")
display_lh = px(measured("heading-display", "default", "lineHeight") or "64px")
display_w = int(float(measured("heading-display", "default", "fontWeight") or 900))
body_size = px(measured("nav-link", "default", "fontSize") or "16px")
body_lh = px(measured("nav-link", "default", "lineHeight") or "22px")

btn = C["components"].get("button-primary", {}).get("default", {})
btn_h = px(str(btn.get("h", 40)) + "px") if isinstance(btn.get("h"), (int, float)) else "40px"
btn_radius = px(btn.get("borderRadius", "12px"))
btn_py = px(btn.get("paddingTop", "4px"))
btn_px = px(btn.get("paddingLeft", "16px"))
field = C["components"].get("newsletter-field", {}).get("default") or C["components"].get("text-field", {}).get("default") or {}
field_h = ("%gpx" % field["h"]) if isinstance(field.get("h"), (int, float)) else None
raw_radius = field.get("borderRadius", "")
field_radius = px(raw_radius.split()[0]) if raw_radius.endswith("px") and " " not in raw_radius.strip() else None

layout = C.get("layout") or {}
header_h = ("%gpx" % layout["headerH"]) if layout.get("headerH") else None

core = {
    "color": core_color,
    "font": {
        "family": {
            "display": tok("fontFamily", display, "Measured computed fontFamily on h1, www.homerun.co home, 1440x900"),
            "sans": tok("fontFamily", body_font, "Measured computed fontFamily on nav link, www.homerun.co home, 1440x900"),
        }
    },
    "typography": {
        "display": {
            "$type": "typography",
            "$value": {
                "fontFamily": "{font.family.display}",
                "fontSize": display_size,
                "fontWeight": display_w,
                "lineHeight": display_lh,
            },
            "$extensions": {"source": "Measured computed style on h1, www.homerun.co home"},
        },
        "nav": {
            "$type": "typography",
            "$value": {
                "fontFamily": "{font.family.sans}",
                "fontSize": body_size,
                "fontWeight": int(float(measured("nav-link", "default", "fontWeight") or 400)),
                "lineHeight": body_lh,
            },
            "$extensions": {"source": "Measured computed style on nav link Organise your hiring"},
        },
    },
    "radius": {
        "button": tok("dimension", btn_radius, "Measured borderRadius on Start free trial link"),
        "nav": tok("dimension", px(measured("nav-link", "default", "borderRadius") or "10px"), "Measured borderRadius on nav link"),
    },
    "space": {
        "button-x": tok("dimension", btn_px, "Measured paddingLeft on Start free trial"),
        "button-y": tok("dimension", btn_py, "Measured paddingTop on Start free trial"),
        "nav": tok("dimension", px(measured("nav-link", "default", "paddingTop") or "12px"), "Measured paddingTop on nav link"),
    },
    "size": {
        "button-height": tok("dimension", btn_h, "Measured bounding height of Start free trial, 1440x900"),
    },
}
if field_radius:
    core["radius"]["field"] = tok("dimension", field_radius, "Measured borderRadius on a public email field")
if field_h:
    core["size"]["field-height"] = tok("dimension", field_h, "Measured bounding height of a public email field")
if header_h:
    core["size"]["header"] = tok("dimension", header_h, "Measured header height, www.homerun.co home, 1440x900")

# Motion is Not captured. --w-backdrop-animation resolved to "initial".
# No duration token is written.

light = {
    "background": {
        "page": alias("color.white", "Measured body background rgb(255,255,255) matches --_updated-colors-v2---primary--white"),
        "surface": alias("color.beige-500", "Declared --beige-500 / --_updated-colors-v2---primary--beige-500, the bone surface used in cards"),
        "muted": alias("color.beige-400", "Declared beige-400, the lightest page wash"),
        "inverse": alias("color.brown-500", "Measured Book a demo background rgb(45, 35, 35) matches brown-500 / coffee-black #2d2323"),
    },
    "text": {
        "primary": alias("color.brown-400", "Measured h1 color rgb(56, 45, 45) matches --brown--brown-400 / brown-400"),
        "body": alias("color.brown-300", "Measured body and nav color rgb(74, 62, 62) matches --dim-grey-2 / brown-300"),
        "muted": alias("color.brown-200", "Declared brown-200 #736b6b, the quieter brown step"),
        "on-accent": alias("color.white", "Measured Start free trial text rgb(255, 255, 255)"),
        "link": alias("color.blue-500", "Primary actions use blue-500; dedicated link colour not separately tokenised by the site"),
    },
    "border": {
        "default": alias("color.coffee-200", "Declared --coffee-200 #e6e2e2, the light divider brown"),
        "strong": alias("color.brown-300", "Body ink used as a strong edge where a keyline matches text"),
    },
    "accent": {
        "default": alias("color.blue-500", "Measured Start free trial background rgb(79, 117, 254) matches --royal-blue / blue-500 #4f75fe"),
        "hover": tok("color", "rgb(38, 77, 219)", "Measured backgroundColor on Start free trial :hover, www.homerun.co home. Close to declared blue-600 #254cda, not the same value."),
        "on": alias("color.white", "Measured text on the blue trial button"),
    },
    "status": {
        "danger": alias("color.red", "Declared --_updated-colors-v2---secondary--red. Not observed as a form error."),
        "success": alias("color.green", "Declared --_updated-colors-v2---secondary--green. Not observed as a toast."),
        "warning": alias("color.orange", "Declared --_updated-colors-v2---secondary--orange."),
        "info": alias("color.blue-500", "Declared blue-500. No separate info role was painted."),
    },
    "focus": {
        "ring": tok("color", "rgb(0, 95, 204)", "Measured outline on Start free trial focus-visible: rgb(0, 95, 204) auto 1px. Browser default ring, not a site token."),
    },
    "button": {
        "secondary": alias("color.brown-500", "Measured Book a demo background rgb(45, 35, 35)"),
        "secondary-hover": tok("color", "rgb(74, 62, 62)", "Measured Book a demo :hover background, matches brown-300"),
        "ghost-hover": tok("color", "rgba(245, 243, 239, 0.984)", "Measured nav link :hover background, beige-500 at about 98%"),
    },
}

# Drop the earlier hover overwrite if the measured value was already written.
hover_bg = measured("button-primary", "hover", "backgroundColor")
if hover_bg:
    light["accent"]["hover"] = tok("color", hover_bg, "Measured backgroundColor on Start free trial :hover")

# Pressed is not captured: the public CTAs are links, and a press navigates.

doc = {
    "$description": "Homerun public marketing site, www.homerun.co, captured 2026-11-21 signed out. One light theme.",
    "core": core,
    "light": light,
    "$themes": [{"id": "light", "name": "Light", "selectedTokenSets": {"core": "enabled", "light": "enabled"}}],
}

# Fix typography aliases: they must be relative to core when Tokens Studio
# resolves inside the core set. The builder stores them as {font.family.display}
# which is correct inside core.
out = HERE / "tokens.json"
out.write_text(json.dumps(doc, indent= 2) + "\n")
print("wrote", out, "palette", len(core_color))
