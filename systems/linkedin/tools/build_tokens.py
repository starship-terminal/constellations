#!/usr/bin/env python3
"""Build tokens.json from LinkedIn's guest homepage stylesheet and measured controls.

Sources, read on 2026-11-21:
  raw/css-extract.json          hashed custom properties from
                                https://static.licdn.com/aero-v1/sc/h/assets/DD4d0Fjc.css
                                palette: :root in @layer rootTheme (the block that declares
                                --cfsa41: #0A66C2)
                                semantic: :root, .cfsa light-dark() aliases
  raw/components-computed.json  computed styles on the live guest pages
  raw/layout.json               body and h1 computed styles
  raw/surfaces.json             painted section backgrounds

The guest homepage does not apply the class that binds the semantic aliases, so
those aliases are labelled as declared CSS, not as the painted page. Painted
roles come from computed styles. A value that was not read is left out.

Deterministic: same inputs, byte-identical output. Edit the raw inputs, never tokens.json.
"""
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
EXTRACT = json.loads((RAW / "css-extract.json").read_text())
COMP = json.loads((RAW / "components-computed.json").read_text())
LAYOUT = json.loads((RAW / "layout.json").read_text())

PALETTE = EXTRACT["palette"]
SEMANTIC = EXTRACT["semantic"]
SHEET = EXTRACT["sourceStylesheet"]


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
    m = re.fullmatch(r"rgba?\(\s*(\d+)[,\s]+(\d+)[,\s]+(\d+)(?:\s*[,/]\s*([\d.]+))?\s*\)", v)
    if m:
        r, g, b, a = m.groups()
        if a is None or float(a) == 1:
            return "#%02x%02x%02x" % (int(r), int(g), int(b))
        return "rgba(%s, %s, %s, %g)" % (r, g, b, float(a))
    raise ValueError("not a colour: " + v)


def color(value, source):
    return {"$value": norm_color(value), "$type": "color", "$extensions": {"source": source}}


def dim(value, source):
    if not re.fullmatch(r"-?\d+(\.\d+)?(px|rem)", str(value)):
        raise ValueError("not a dimension: %r" % value)
    return {"$value": value, "$type": "dimension", "$extensions": {"source": source}}


def weight(value, source):
    return {"$value": int(value), "$type": "fontWeight", "$extensions": {"source": source}}


def text(value, source):
    return {"$value": value, "$type": "fontFamily", "$extensions": {"source": source}}


def typography(family, size, weight_v, line, source):
    return {
        "$type": "typography",
        "$value": {
            "fontFamily": family,
            "fontSize": size,
            "fontWeight": weight_v,
            "lineHeight": line,
        },
        "$extensions": {"source": source},
    }


def state(key, name="default"):
    node = COMP["components"][key]["states"][name]
    if node.get("missing") or node.get("error"):
        raise KeyError(key + " " + name)
    return node["style"]


def measured(key, prop, state_name="default"):
    return "%s %s %s, computed on %s" % (prop, key, state_name, COMP["components"][key]["page"])


# Brand blue is the one named colour the guest stylesheet spells out and the
# painted primary button matches. The rest of the ramp stays under its hashed
# name so a reader can find it in the stylesheet.
BRAND = "--cfsa41"
BRAND_PRESSED = "--cfsa42"

core = {
    "color": {
        "brand": {
            "50": color(PALETTE["--cfsa4s"], "css-var --cfsa4s declared on :root in %s" % SHEET),
            "70": color(PALETTE[BRAND], "css-var --cfsa41 (#0A66C2) declared on :root in %s" % SHEET),
            "80": color(PALETTE[BRAND_PRESSED], "css-var --cfsa42 declared on :root in %s" % SHEET),
            "90": color(PALETTE["--cfsa43"], "css-var --cfsa43 declared on :root in %s" % SHEET),
        },
        "neutral": {
            "white": color(PALETTE["--cfsbdf"], "css-var --cfsbdf declared on :root in %s" % SHEET),
            "black": color(PALETTE["--cfsa4m"], "css-var --cfsa4m declared on :root in %s" % SHEET),
            "ink-90": color("rgba(0, 0, 0, 0.9)", "computed body color on https://www.linkedin.com/"),
            "ink-75": color("rgba(0, 0, 0, 0.75)", measured("button-email", "color")),
        },
    },
    "fontFamily": {
        "ui": text(LAYOUT["body"]["font"], "computed font-family on body, https://www.linkedin.com/"),
        "mono": text(EXTRACT["fonts"]["--cfsc"], "css-var --cfsc declared in %s" % SHEET),
    },
    "fontSize": {
        "body": dim("16px", "computed font-size on body, https://www.linkedin.com/"),
        "display": dim(LAYOUT["h1"]["size"], "computed font-size on h1, https://www.linkedin.com/"),
        "scale-d": dim("1.2rem", "css-var --cfsd declared on :root, .cfsa in %s" % SHEET),
        "scale-e": dim("1.4rem", "css-var --cfse declared on :root, .cfsa in %s" % SHEET),
        "scale-f": dim("1.6rem", "css-var --cfsf declared on :root, .cfsa in %s" % SHEET),
        "scale-g": dim("1.8rem", "css-var --cfsg declared on :root, .cfsa in %s" % SHEET),
        "scale-h": dim("2rem", "css-var --cfsh declared on :root, .cfsa in %s" % SHEET),
        "scale-i": dim("2.4rem", "css-var --cfsi declared on :root, .cfsa in %s" % SHEET),
        "scale-j": dim("3rem", "css-var --cfsj declared on :root, .cfsa in %s" % SHEET),
        "scale-k": dim("3.6rem", "css-var --cfsk declared on :root, .cfsa in %s" % SHEET),
        "scale-l": dim("4.8rem", "css-var --cfsl declared on :root, .cfsa in %s" % SHEET),
        "scale-m": dim("6rem", "css-var --cfsm declared on :root, .cfsa in %s" % SHEET),
    },
    "fontWeight": {
        "regular": weight(400, "computed font-weight on h1, https://www.linkedin.com/"),
        "semibold": weight(600, measured("button-primary", "fontWeight")),
    },
    "radius": {
        "pill": dim(state("button-primary")["borderRadius"], measured("button-primary", "borderRadius")),
        "field": dim("4px", "computed border-radius on the visible email field, https://www.linkedin.com/login/"),
    },
    "space": {
        "control-padding-x": dim(state("button-primary")["paddingLeft"], measured("button-primary", "paddingLeft")),
        "field-padding-x": dim("12px", "computed padding-left on the visible email field, https://www.linkedin.com/login/"),
    },
    "typography": {
        "display": typography(
            "{fontFamily.ui}", "48px", 400, "60px",
            "computed h1 on https://www.linkedin.com/"),
        "body": typography(
            "{fontFamily.ui}", "16px", 400, "24px",
            "computed body on https://www.linkedin.com/"),
        "button": typography(
            "{fontFamily.ui}", "16px", 600, "24px",
            measured("button-primary", "font")),
        "link": typography(
            "{fontFamily.ui}", "14px", 600, "20px",
            "computed User Agreement link on https://www.linkedin.com/"),
    },
}

# Semantic aliases are declared, not painted on the guest homepage. Keep a
# count in the README; do not invent role names for hashed light-dark() pairs.
core["$extensions"] = {
    "declaredSemanticCount": len(SEMANTIC),
    "declaredPaletteCount": len(PALETTE),
    "note": "Hashed --cfs* names are not renamed. The semantic block uses light-dark() and is not applied on the guest homepage.",
}

light = {
    "page": color("#ffffff", "sampled flat fill at (20, 40) of raw-shots/home-light-default.png before quantize"),
    "surface": color("#f3f2f0", "sampled flat fill at (20, 760) of raw-shots/home-light-default.png before quantize"),
    "text": color(LAYOUT["body"]["color"], "computed body color on https://www.linkedin.com/"),
    "muted": color(state("button-email")["color"], measured("button-email", "color")),
    "accent": color(state("button-primary")["backgroundColor"], measured("button-primary", "backgroundColor")),
    "border": color("rgba(0, 0, 0, 0.75)", "computed border-top-color on the visible email field, https://www.linkedin.com/login/"),
    "link": color("rgb(10, 102, 194)", "computed color of the User Agreement link on https://www.linkedin.com/"),
    "onAccent": color(state("button-primary")["color"], measured("button-primary", "color")),
    "accentHover": color(state("button-primary", "hover")["backgroundColor"], measured("button-primary", "backgroundColor", "hover")),
    "accentPressed": color(state("button-primary", "active")["backgroundColor"], measured("button-primary", "backgroundColor", "active")),
    "helpHeader": color("rgb(0, 115, 177)", "computed background of .global-header on https://www.linkedin.com/help/linkedin"),
    "component": {
        "button": {
            "height": dim(state("button-primary")["height"], measured("button-primary", "height")),
            "radius": dim("{core.radius.pill}".replace("{core.radius.pill}", state("button-primary")["borderRadius"]), measured("button-primary", "borderRadius")),
            "paddingX": dim(state("button-primary")["paddingLeft"], measured("button-primary", "paddingLeft")),
            "fontSize": dim(state("button-primary")["fontSize"], measured("button-primary", "fontSize")),
        },
        "field": {
            "height": dim("48px", "computed height of the visible email field, https://www.linkedin.com/login/"),
            "radius": dim("4px", "computed border-radius of the visible email field, https://www.linkedin.com/login/"),
        },
        "chip": {
            "radius": dim(state("chip")["borderRadius"], measured("chip", "borderRadius")),
        },
    },
}

# Dark is declared in the stylesheet and not painted on any captured page.
dark = {
    "$extensions": {
        "source": "Not captured as a painted theme. The guest stylesheet declares light-dark() aliases on :root, .cfsa and a [data-color-scheme=light] block. No captured public page binds a dark scheme.",
    }
}

tokens = {
    "core": core,
    "light": light,
    "dark": dark,
    "$themes": [
        {"id": "light", "name": "light", "selectedTokenSets": {"core": "enabled", "light": "enabled"}},
        {"id": "dark", "name": "dark", "selectedTokenSets": {"core": "enabled", "dark": "enabled"}},
    ],
}

# Fix the accidental string replace above by rewriting button radius cleanly.
light["component"]["button"]["radius"] = dim(
    state("button-primary")["borderRadius"], measured("button-primary", "borderRadius"))

text_out = json.dumps(tokens, indent=2) + "\n"
(HERE / "tokens.json").write_text(text_out)
print("wrote", HERE / "tokens.json", "tokens")
