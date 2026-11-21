#!/usr/bin/env python3
"""Build tokens.json from raw/css-vars.json and raw/home-roles.json.

Every colour and length here was read from www.useparallel.com on 2026-11-21.
Declared names come from the site's stylesheets. Computed roles that the
marketing shell paints without a custom property come from home-roles.json.
A value that was not read is not invented.

The public site paints one light theme. No dark toggle was found, so the
file has core and light only.
"""
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
V = json.loads((RAW / "css-vars.json").read_text())
ROLES = json.loads((RAW / "home-roles.json").read_text())
DECL = {n: v for n, v in V["resolved"]["light"].items() if v.get("kind") in ("color", "dimension", "fontFamily")}


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
            if a == 1:
                return "#%02x%02x%02x" % (r, g, b)
            return "rgba(%d, %d, %d, %g)" % (r, g, b, a)
        return "#%02x%02x%02x" % (r, g, b)
    m = re.fullmatch(r"rgba?\(\s*(\d+)[,\s]+(\d+)[,\s]+(\d+)(?:\s*[,/]\s*([\d.]+%?))?\s*\)", v)
    if m:
        r, g, b, a = m.groups()
        if a is None or float(a) == 1:
            return "#%02x%02x%02x" % (int(r), int(g), int(b))
        a = float(a[:-1]) / 100 if str(a).endswith("%") else float(a)
        return "rgba(%s, %s, %s, %g)" % (r, g, b, a)
    raise ValueError("not a colour: " + v)


def color(name, source):
    return {
        "$value": norm_color(DECL[name]["value"]),
        "$type": "color",
        "$extensions": {"source": source},
    }


def dim(name, source):
    value = DECL[name]["value"]
    if not re.fullmatch(r"-?\d+(\.\d+)?(px|rem)", value):
        raise ValueError(f"{name}: {value}")
    return {"$value": value, "$type": "dimension", "$extensions": {"source": source}}


def font(name, source):
    return {
        "$value": DECL[name]["value"],
        "$type": "fontFamily",
        "$extensions": {"source": source},
    }


def measured_color(value, source):
    return {"$value": norm_color(value), "$type": "color", "$extensions": {"source": source}}


def measured_dim(value, source):
    if not re.fullmatch(r"-?\d+(\.\d+)?(px|rem)", value):
        raise ValueError(value)
    return {"$value": value, "$type": "dimension", "$extensions": {"source": source}}


core = {
    "color": {
        "black": color("--color-black", "css-var --color-black"),
        "white": color("--color-white", "css-var --color-white"),
        "off-white": color("--color-off-white", "css-var --color-off-white"),
        "light-gray": color("--color-light-gray", "css-var --color-light-gray"),
        "gray": color("--color-gray", "css-var --color-gray"),
        "green": color("--color-green", "css-var --color-green"),
        "orange": color("--color-orange", "css-var --color-orange"),
        "pink": color("--color-pink", "css-var --color-pink"),
        "purple": color("--color-purple", "css-var --color-purple"),
        "red": color("--color-red", "css-var --color-red"),
        "red-200": color("--color-red-200", "css-var --color-red-200"),
        "red-400": color("--color-red-400", "css-var --color-red-400"),
        "yellow": color("--color-yellow", "css-var --color-yellow"),
        "scrollbar-thumb": color("--prll-scrollbar-thumb-color", "css-var --prll-scrollbar-thumb-color"),
        "app-background": color("--app-background", "css-var --app-background"),
        "input-hover-border": color("--input-hover-border-color", "css-var --input-hover-border-color"),
        "input-focus-border": color("--input-focus-border-color", "css-var --input-focus-border-color"),
    },
    "font": {
        "family": {
            "primary": font("--font-family-primary", "css-var --font-family-primary"),
            "secondary": font("--font-family-secondary", "css-var --font-family-secondary"),
            "tertiary": font("--font-family-tertiary", "css-var --font-family-tertiary"),
            "display": {
                "$value": ROLES["h1"]["fontFamily"],
                "$type": "fontFamily",
                "$extensions": {"source": "computed fontFamily of h1 on / (raw/home-roles.json)"},
            },
        },
        "size": {
            "display": measured_dim(ROLES["h1"]["fontSize"], "computed fontSize of h1 on / (raw/home-roles.json)"),
            "body": measured_dim(ROLES["page"]["fontSize"], "computed fontSize of body on / (raw/home-roles.json)"),
        },
        "weight": {
            "display": {
                "$value": int(ROLES["h1"]["fontWeight"]),
                "$type": "fontWeight",
                "$extensions": {"source": "computed fontWeight of h1 on / (raw/home-roles.json)"},
            },
        },
        "line-height": {
            "display": measured_dim(ROLES["h1"]["lineHeight"], "computed lineHeight of h1 on / (raw/home-roles.json)"),
        },
        "letter-spacing": {
            "display": measured_dim(ROLES["h1"]["letterSpacing"], "computed letterSpacing of h1 on / (raw/home-roles.json)"),
        },
    },
    "space": {
        "grid-1": dim("--prll-gt-1", "css-var --prll-gt-1"),
        "grid-2": dim("--prll-gt-2", "css-var --prll-gt-2"),
        "column-1": dim("--prll-g-1", "css-var --prll-g-1"),
        "column-2": dim("--prll-g-2", "css-var --prll-g-2"),
        "column-3": dim("--prll-g-3", "css-var --prll-g-3"),
        "column-4": dim("--prll-g-4", "css-var --prll-g-4"),
        "column-5": dim("--prll-g-5", "css-var --prll-g-5"),
        "column-6": dim("--prll-g-6", "css-var --prll-g-6"),
        "column-7": dim("--prll-g-7", "css-var --prll-g-7"),
        "column-8": dim("--prll-g-8", "css-var --prll-g-8"),
        "column-9": dim("--prll-g-9", "css-var --prll-g-9"),
        "column-10": dim("--prll-g-10", "css-var --prll-g-10"),
        "column-11": dim("--prll-g-11", "css-var --prll-g-11"),
        "column-12": dim("--prll-g-12", "css-var --prll-g-12"),
    },
    "size": {
        "scrollbar": dim("--prll-scrollbar-size", "css-var --prll-scrollbar-size"),
        "scrollbar-thumb-border": dim("--prll-scrollbar-thumb-border-size", "css-var --prll-scrollbar-thumb-border-size"),
        "scrollbar-track-margin": dim("--prll-scrollbar-track-margin", "css-var --prll-scrollbar-track-margin"),
    },
}

shadows = {
    "primary": ("8px", "8px", "0px", "#0f0f0f", "--shadow-primary"),
    "secondary": ("6px", "6px", "0px", "#0f0f0f", "--shadow-secondary"),
}
core["shadow"] = {}
for key, (x, y, blur, colour, var) in shadows.items():
    raw = V["resolved"]["light"][var]["raw"]
    core["shadow"][key] = {
        "$type": "shadow",
        "$value": {
            "offsetX": x,
            "offsetY": y,
            "blur": blur,
            "spread": "0px",
            "color": norm_color(colour),
        },
        "$extensions": {"source": f"css-var {var} ({raw})"},
    }

light = {
    "surface": {
        "page": measured_color(ROLES["page"]["backgroundColor"], "computed backgroundColor of body on / (raw/home-roles.json)"),
        "paper": {"$value": "{core.color.off-white}", "$type": "color", "$extensions": {"source": "alias of css-var --color-off-white"}},
        "white": {"$value": "{core.color.white}", "$type": "color", "$extensions": {"source": "alias of css-var --color-white"}},
        "app": {"$value": "{core.color.app-background}", "$type": "color", "$extensions": {"source": "alias of css-var --app-background"}},
    },
    "text": {
        "primary": measured_color(ROLES["page"]["color"], "computed color of body on / (raw/home-roles.json)"),
        "on-hero": measured_color(ROLES["h1"]["color"], "computed color of h1 on / (raw/home-roles.json)"),
        "ink": {"$value": "{core.color.black}", "$type": "color", "$extensions": {"source": "alias of css-var --color-black"}},
    },
    "border": {
        "strong": {"$value": "{core.color.black}", "$type": "color", "$extensions": {"source": "alias of css-var --color-black; --border-primary is 2px solid #0f0f0f"}},
        "input-hover": {"$value": "{core.color.input-hover-border}", "$type": "color", "$extensions": {"source": "alias of css-var --input-hover-border-color"}},
        "focus": {"$value": "{core.color.input-focus-border}", "$type": "color", "$extensions": {"source": "alias of css-var --input-focus-border-color"}},
    },
    "accent": {
        "yellow": {"$value": "{core.color.yellow}", "$type": "color", "$extensions": {"source": "alias of css-var --color-yellow"}},
        "pink": {"$value": "{core.color.pink}", "$type": "color", "$extensions": {"source": "alias of css-var --color-pink"}},
        "red": {"$value": "{core.color.red}", "$type": "color", "$extensions": {"source": "alias of css-var --color-red"}},
        "green": {"$value": "{core.color.green}", "$type": "color", "$extensions": {"source": "alias of css-var --color-green"}},
    },
}

doc = {
    "core": core,
    "light": light,
    "$themes": [{
        "id": "light",
        "name": "Light",
        "selectedTokenSets": {"core": "source", "light": "enabled"},
        "$description": "The only theme the public useparallel.com pages painted on 2026-11-21. No dark toggle was found.",
    }],
    "$metadata": {"tokenSetOrder": ["core", "light"]},
}

(HERE / "tokens.json").write_text(json.dumps(doc, indent=2) + "\n")
print("wrote tokens.json")
