#!/usr/bin/env python3
"""Build tokens.json from the Rox public-site readings.

Sources, read from www.rox.com on 2026-11-21, signed out:
  raw/css-vars.json   Framer custom properties resolved on the pricing page
  raw/states.json     computed styles of nav, primary button, plan CTA, field
  raw/live-styles.json  painted type roles on the home and contact pages

One theme. The site does not restyle under color-scheme: dark. Framer token
names are opaque hashes, so semantic names here are roles we measured, each
citing the reading. A value that was not read is absent, never invented.
"""
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
VARS = json.loads((RAW / "css-vars.json").read_text())
STATES = json.loads((RAW / "states.json").read_text())
LIVE = json.loads((RAW / "live-styles.json").read_text())

RESOLVED = VARS["resolved"]["light"]


def hex_of(value):
    value = value.strip().lower()
    if re.fullmatch(r"#[0-9a-f]{6}", value):
        return value
    if re.fullmatch(r"#[0-9a-f]{3}", value):
        return "#" + "".join(c * 2 for c in value[1:])
    m = re.fullmatch(r"rgb\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*\)", value)
    if m:
        return "#%02x%02x%02x" % tuple(int(x) for x in m.groups())
    m = re.fullmatch(r"rgba\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*,\s*([\d.]+)\s*\)", value)
    if m:
        r, g, b, a = m.groups()
        a = float(a)
        if a == 1:
            return "#%02x%02x%02x" % (int(r), int(g), int(b))
        return "rgba(%s, %s, %s, %g)" % (r, g, b, a)
    raise ValueError("not a colour: " + value)


def token_named(value):
    """The first Framer custom property that resolves to this hex, if one does."""
    want = value.lower()
    for name, raw in RESOLVED.items():
        if raw.strip().lower() == want:
            return name
    return None


def color(path, value, where):
    name = token_named(value)
    source = "measured " + where
    if name:
        source += "; css-var " + name
    return {
        "$type": "color",
        "$value": hex_of(value) if value.startswith("rgb") else value,
        "$extensions": {"source": source},
    }


def dim(path, value, where):
    if not re.fullmatch(r"-?\d+(\.\d+)?px", value):
        raise ValueError(path + " dimension " + value)
    return {"$type": "dimension", "$value": value, "$extensions": {"source": "measured " + where}}


def num(value, where, ty="number"):
    return {"$type": ty, "$value": value, "$extensions": {"source": "measured " + where}}


def font(stack, where):
    return {"$type": "fontFamily", "$value": stack, "$extensions": {"source": "measured " + where}}


# Roles read on the live page. Framer hashes are cited when a declaration matches.
page = "#f7f6f4"  # body background rgb(247, 246, 244); not a named --token
ink = "#1c1917"
ink_deep = "#0c0a09"
paper = "#fafafa"
stone = "#403f3e"
muted = "#a6a09b"
muted_2 = "#57534d"
field = "#f4f4f3"
card = "#faf9f7"
blue = "#0b63e8"
amber = "#f0c030"
orange = "#f9700a"
red = "#e5484d"
violet = "#9458ff"
focus = "#005fcc"

core = {
    "color": {
        "page": color("core.color.page", page, "document.body backgroundColor on www.rox.com/"),
        "paper": color("core.color.paper", paper, "header Start now and Contact Sales background; also a --token"),
        "card": color("core.color.card", card, "pricing plan card ancestor background rgb(250, 249, 247)"),
        "field": color("core.color.field", field, "contact email field wrapper background rgb(244, 244, 243)"),
        "ink": color("core.color.ink", ink, "display and heading color rgb(28, 25, 23); css-var match"),
        "ink-deep": color("core.color.ink-deep", ink_deep, "Start now hover background rgb(12, 10, 9)"),
        "stone": color("core.color.stone", stone, "plan CTA default background rgb(64, 63, 62)"),
        "muted": color("core.color.muted", muted, "contact field label color rgb(166, 160, 155)"),
        "muted-2": color("core.color.muted-2", muted_2, "Gartner toast text rgb(87, 83, 77)"),
        "on-ink": color("core.color.on-ink", paper, "Start now label rgb(250, 250, 250)"),
        "blue": color("core.color.blue", blue, "declared Framer colour used on the site; not the nav text"),
        "amber": color("core.color.amber", amber, "declared Framer colour"),
        "orange": color("core.color.orange", orange, "declared Framer colour"),
        "red": color("core.color.red", red, "declared Framer colour"),
        "violet": color("core.color.violet", violet, "declared Framer colour"),
        "focus": color("core.color.focus", focus, "Start now outline on keyboard focus rgb(0, 95, 204)"),
        "white": color("core.color.white", "#ffffff", "declared #fff"),
        "black": color("core.color.black", "#000000", "declared #000 and plan CTA hover background"),
    },
    "font": {
        "family": {
            "display": font("Season Mix-TRIAL Regular, sans-serif", "home display heading computed fontFamily"),
            "sans": font("Geist, sans-serif", "nav and button computed fontFamily"),
            "mono": font("Geist Mono, ui-monospace, monospace", "@font-face on the pricing page; Fragment Mono also declared"),
            "fallback": font("Inter, sans-serif", "@font-face on the pricing page; not the painted marketing text"),
        }
    },
    "typography": {
        "display": {
            "$type": "typography",
            "$value": {
                "fontFamily": "{core.font.family.display}",
                "fontSize": "56px",
                "fontWeight": 420,
                "lineHeight": "67.2px",
                "letterSpacing": "-1.12px",
            },
            "$extensions": {"source": "measured home hero 'The Revenue Agent for the Global 2000'"},
        },
        "title": {
            "$type": "typography",
            "$value": {
                "fontFamily": "{core.font.family.display}",
                "fontSize": "42px",
                "fontWeight": 420,
                "lineHeight": "50.4px",
                "letterSpacing": "-0.84px",
            },
            "$extensions": {"source": "measured contact heading 'Get in touch.'"},
        },
        "nav": {
            "$type": "typography",
            "$value": {
                "fontFamily": "{core.font.family.sans}",
                "fontSize": "14px",
                "fontWeight": 500,
                "lineHeight": "14px",
                "letterSpacing": "0px",
            },
            "$extensions": {"source": "measured header Platform link"},
        },
        "body": {
            "$type": "typography",
            "$value": {
                "fontFamily": "{core.font.family.sans}",
                "fontSize": "14px",
                "fontWeight": 400,
                "lineHeight": "16.8px",
                "letterSpacing": "-0.28px",
            },
            "$extensions": {"source": "measured contact email input"},
        },
        "button": {
            "$type": "typography",
            "$value": {
                "fontFamily": "{core.font.family.sans}",
                "fontSize": "16px",
                "fontWeight": 500,
                "lineHeight": "16px",
                "letterSpacing": "0px",
            },
            "$extensions": {"source": "measured contact 'Get in touch' button label"},
        },
    },
    "radius": {
        "none": dim("core.radius.none", "0px", "header buttons and plan cards"),
        "field": dim("core.radius.field", "4px", "contact email field wrapper"),
    },
    "space": {
        "button-y": dim("core.space.button-y", "8px", "header button padding-top"),
        "button-x": dim("core.space.button-x", "13px", "header button padding-left"),
        "field": dim("core.space.field", "16px", "textarea padding"),
    },
    "size": {
        "header-button": dim("core.size.header-button", "30px", "Contact Sales and Start now height"),
        "nav-row": dim("core.size.nav-row", "64px", "Platform link hit height"),
        "plan-cta": dim("core.size.plan-cta", "41px", "Start for free height"),
        "field": dim("core.size.field", "49px", "email field wrapper height"),
        "menu-button": dim("core.size.menu-button", "33px", "phone menu icon button"),
    },
}

light = {
    "background": {
        "page": color("light.background.page", page, "document.body"),
        "surface": color("light.background.surface", paper, "header button and form panel"),
        "raised": color("light.background.raised", card, "pricing plan card"),
        "field": color("light.background.field", field, "contact field wrapper"),
        "inverse": color("light.background.inverse", ink, "Start now fill and phone menu"),
    },
    "text": {
        "primary": color("light.text.primary", ink, "display and headings"),
        "secondary": color("light.text.secondary", stone, "nav link color"),
        "muted": color("light.text.muted", muted, "field label"),
        "on-accent": color("light.text.on-accent", paper, "Start now and plan CTA label"),
    },
    "border": {
        "default": color("light.border.default", "#e7e5e4", "declared stone hairline on the pricing page"),
        "strong": color("light.border.strong", stone, "plan CTA fill, used as the strong edge"),
    },
    "accent": {
        "default": color("light.accent.default", ink, "primary button fill"),
        "hover": color("light.accent.hover", ink_deep, "Start now hover background"),
        "pressed": color("light.accent.pressed", "#000000", "plan CTA hover and pressed background"),
    },
    "status": {
        "info": color("light.status.info", blue, "declared blue; not observed as a status chip"),
        "warning": color("light.status.warning", amber, "declared amber; not observed as a status chip"),
        "danger": color("light.status.danger", red, "declared red; not observed as a status chip"),
    },
    "focus": {
        "ring": color("light.focus.ring", focus, "Start now keyboard focus outline"),
    },
    "component": {
        "button-primary-bg": color("light.component.button-primary-bg", ink, "Start now"),
        "button-primary-text": color("light.component.button-primary-text", paper, "Start now label"),
        "button-secondary-bg": color("light.component.button-secondary-bg", paper, "Contact Sales"),
        "button-secondary-text": color("light.component.button-secondary-text", stone, "Contact Sales label"),
        "button-plan-bg": color("light.component.button-plan-bg", stone, "Start for free"),
        "field-bg": color("light.component.field-bg", field, "email field wrapper"),
        "field-radius": dim("light.component.field-radius", "4px", "email field wrapper"),
    },
}

doc = {
    "$schema": "https://www.designtokens.org/schemas/2025.10/format.json",
    "core": core,
    "light": light,
    "$themes": [
        {"name": "light", "group": "light", "selectedTokenSets": {"core": "source", "light": "enabled"}}
    ],
    "$extensions": {
        "source": "www.rox.com public site, 2026-11-21, signed out. One theme.",
        "notTokenised": [
            "Header button inset shadows are recorded in raw/states.json and not flattened into a shadow token.",
            "Framer --token-* names are opaque hashes. Semantic names here are roles, each citing the element they were read from.",
            "Motion durations were not isolated from Framer transition strings. Not captured.",
            "Dark theme: not present. color-scheme dark left body rgb(247, 246, 244).",
        ],
    },
}


def walk(node, path=""):
    if isinstance(node, dict) and "$value" in node:
        ty = node.get("$type")
        val = node["$value"]
        if isinstance(val, str) and val.startswith("{"):
            return
        if ty == "color":
            hex_of(val) if not val.startswith("rgba") else None
        if ty == "dimension" and not re.fullmatch(r"-?\d+(\.\d+)?px", str(val)):
            raise ValueError(path + " " + str(val))
        if "source" not in node.get("$extensions", {}):
            raise ValueError(path + " missing source")
        return
    if isinstance(node, dict):
        for k, v in node.items():
            if k.startswith("$"):
                continue
            walk(v, path + "." + k)


walk(doc)
out = HERE / "tokens.json"
out.write_text(json.dumps(doc, indent=1) + "\n")
print("wrote", out, "bytes", out.stat().st_size)
