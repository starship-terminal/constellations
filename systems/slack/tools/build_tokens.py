#!/usr/bin/env python3
"""Build tokens.json from Slack's measured public styles.

Sources, read on 2026-11-21 from https://slack.com/intl/en-sg/:
  raw/components-computed.json   computed styles of public controls
  raw/css-vars.json              declared custom properties (hashed colour
                                 names plus font families)
  raw/page-colors.json           body and section backgrounds

The public site painted light only. There is no dark semantic set.
Unread values stay out. Edit the raw inputs, never tokens.json.
"""
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
COMP = json.loads((RAW / "components-computed.json").read_text())
VARS = json.loads((RAW / "css-vars.json").read_text())


def rgb_to_hex(value):
    value = value.strip()
    m = re.fullmatch(r"rgba?\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)(?:\s*,\s*([\d.]+))?\s*\)", value)
    if not m:
        if re.fullmatch(r"#[0-9a-fA-F]{3,8}", value):
            return value.lower()
        raise ValueError("not a colour: " + value)
    r, g, b, a = m.groups()
    if a is None or float(a) == 1:
        return "#%02x%02x%02x" % (int(r), int(g), int(b))
    return "rgba(%d, %d, %d, %g)" % (int(r), int(g), int(b), float(a))


def dim(value):
    value = str(value).strip()
    if re.fullmatch(r"-?\d+(\.\d+)?px", value):
        num = float(value[:-2])
        return ("%gpx" % round(num, 2))
    raise ValueError("not a dimension: " + value)


def state(key, name="default"):
    entry = COMP["components"][key]
    if entry.get("miss"):
        raise KeyError(key + " was not measured")
    st = entry["states"].get(name)
    if not st or st.get("error") or st.get("miss"):
        raise KeyError(f"{key}.{name} was not measured")
    return st


def color(path, key, prop, st="default"):
    raw = state(key, st)[prop]
    return {
        "$value": rgb_to_hex(raw),
        "$type": "color",
        "$extensions": {"source": f"Measured computed {prop} on {key} {st}, {COMP['source']}, raw/components-computed.json"},
    }


def dimension(path, key, prop, st="default"):
    raw = state(key, st)[prop]
    return {
        "$value": dim(raw),
        "$type": "dimension",
        "$extensions": {"source": f"Measured computed {prop} on {key} {st}, {COMP['source']}, raw/components-computed.json"},
    }


def font_family(name):
    raw = VARS["resolved"]["light"][name]["raw"]
    return {
        "$value": raw,
        "$type": "fontFamily",
        "$extensions": {"source": f"Measured css-var {name} resolved on the slack.com probe, raw/css-vars.json"},
    }


def typography(role, key, family_token):
    st = state(key)
    size = dim(st["fontSize"])
    line = dim(st["lineHeight"]) if re.fullmatch(r"-?\d+(\.\d+)?px", str(st["lineHeight"])) else None
    weight = int(float(st["fontWeight"]))
    letter = st.get("letterSpacing")
    value = {
        "fontFamily": family_token,
        "fontSize": size,
        "fontWeight": weight,
    }
    if line:
        value["lineHeight"] = line
    if letter and letter != "normal" and re.fullmatch(r"-?\d+(\.\d+)?px", letter):
        value["letterSpacing"] = dim(letter)
    return {
        "$value": value,
        "$type": "typography",
        "$extensions": {"source": f"Measured computed type on {key} default, {COMP['source']}, raw/components-computed.json"},
    }


primary = color("accent", "button-primary", "backgroundColor")
primary_hover = color("accentHover", "button-primary", "backgroundColor", "hover")
on_accent = color("onAccent", "button-primary", "color")
text = color("text", "link-nav", "color")
ink = color("ink", "heading-display", "color")
link = color("link", "menu-link", "color")
link_hover = color("linkHover", "menu-link", "color", "hover")
field_border = color("fieldBorder", "text-field", "borderTopColor")
focus = color("focus", "button-primary", "outlineColor", "focus-visible")
page_bg = {
    "$value": "#ffffff",
    "$type": "color",
    "$extensions": {"source": "Measured: body background was transparent and the painted page behind the hero is white in screenshots/home-light-default.png; section aubergine rgb(72, 26, 84) is light.surface.aubergine from raw/page-colors.json"},
}
aubergine = {
    "$value": "#481a54",
    "$type": "color",
    "$extensions": {"source": "Measured computed backgroundColor rgb(72, 26, 84) on a homepage section, raw/page-colors.json"},
}
sidebar = {
    "$value": rgb_to_hex(VARS["resolved"]["light"]["--sidebar-color"]["value"]),
    "$type": "color",
    "$extensions": {"source": "Measured css-var --sidebar-color on the slack.com probe, raw/css-vars.json. Used by the marketing app-demo chrome, not a signed-in workspace."},
}

tokens = {
    "core": {
        "fontFamily": {
            "heading": font_family("--font-family-heading"),
            "body": font_family("--font-family-body"),
            "monospace": font_family("--font-family-monospace"),
        },
        "typography": {
            "display": typography("display", "heading-display", "{core.fontFamily.heading}"),
            "body": typography("body", "body-lead", "{core.fontFamily.body}"),
            "label": typography("label", "button-primary", "{core.fontFamily.body}"),
            "nav": typography("nav", "link-nav", "{core.fontFamily.body}"),
        },
        "radius": {
            "control": dimension("radius.control", "button-primary", "borderTopLeftRadius"),
            "field": dimension("radius.field", "text-field", "borderTopLeftRadius"),
        },
        "spacing": {
            "field-pad-x": dimension("spacing.field-pad-x", "text-field", "paddingLeft"),
            "button-pad-x": dimension("spacing.button-pad-x", "button-primary", "paddingLeft"),
        },
        "fontSize": {
            "body": {
                "$value": "16px",
                "$type": "dimension",
                "$extensions": {"source": "Measured computed font-size on body, raw/page-colors.json"},
            },
        },
    },
    "light": {
        "page": page_bg,
        "surface": {
            "default": page_bg,
            "aubergine": aubergine,
            "sidebar": sidebar,
        },
        "text": {
            "primary": text,
            "ink": ink,
            "on-accent": on_accent,
            "link": link,
        },
        "muted": {
            "$value": rgb_to_hex(state("text-field")["borderTopColor"]),
            "$type": "color",
            "$extensions": {"source": "Measured computed border colour on text-field default, used as the quiet ink on form chrome, raw/components-computed.json. A dedicated muted text role was not a separate token on the page."},
        },
        "accent": {
            "default": primary,
            "hover": primary_hover,
        },
        "border": {
            "default": field_border,
            "accent": color("border.accent", "button-outline", "borderTopColor"),
        },
        "focus": {
            "ring": focus,
        },
        "link": {
            "default": link,
            "hover": link_hover,
        },
        "component": {
            "button": {
                "height": dimension("button.height", "button-primary", "height"),
                "radius": dimension("button.radius", "button-primary", "borderTopLeftRadius"),
                "outline-height": dimension("button.outline-height", "button-outline", "height"),
            },
            "field": {
                "height": dimension("field.height", "text-field", "height"),
                "radius": dimension("field.radius", "text-field", "borderTopLeftRadius"),
                "border-width": dimension("field.border-width", "text-field", "borderTopWidth"),
            },
            "focus": {
                "width": dimension("focus.width", "button-primary", "outlineWidth", "focus-visible"),
                "offset": dimension("focus.offset", "button-primary", "outlineOffset", "focus-visible"),
            },
        },
    },
    "$themes": [
        {
            "id": "light",
            "name": "Light",
            "selectedTokenSets": {"core": "source", "light": "enabled"},
            "$description": "The theme the public marketing pages painted on 2026-11-21.",
        }
    ],
    "$metadata": {"tokenSetOrder": ["core", "light"]},
}

# focus offset
focus_state = state("button-primary", "focus-visible")
tokens["light"]["component"]["focus"]["offset"] = {
    "$value": dim(focus_state["outlineOffset"]),
    "$type": "dimension",
    "$extensions": {"source": "Measured computed outlineOffset on button-primary focus-visible, raw/components-computed.json"},
}

(HERE / "tokens.json").write_text(json.dumps(tokens, indent=2) + "\n")
print("wrote tokens.json")
