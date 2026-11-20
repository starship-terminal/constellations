#!/usr/bin/env python3
"""Build tokens.json from raw/css-vars.json.

Every colour, type size, and font family is a custom property resolved on
www.monarch.com on 2026-11-21. The public site paints one light theme.
Osano consent variables are left out. A name that did not resolve is not
invented. Dark is an empty stub.
"""
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
V = json.loads((RAW / "css-vars.json").read_text())
RES = V["resolved"]["light"]

SKIP_PREFIX = ("--osano", "--tw-", "--media-", "--theme-")


def src(name):
    return f"css-var {name} resolved on www.monarch.com :root, 2026-11-21, raw/css-vars.json"


def color_token(name):
    row = RES[name]
    if row.get("kind") != "color" or "value" not in row:
        raise KeyError(name)
    return {
        "$value": row["value"],
        "$type": "color",
        "$extensions": {"source": src(name)},
    }


def dim_token(name):
    row = RES[name]
    if row.get("kind") != "dimension" or "value" not in row:
        raise KeyError(name)
    val = row["value"]
    if not re.fullmatch(r"-?\d+(\.\d+)?(px|rem)", str(val)):
        raise ValueError(f"{name}: {val!r}")
    return {
        "$value": val,
        "$type": "dimension",
        "$extensions": {"source": src(name)},
    }


def num_token(name):
    row = RES[name]
    if row.get("kind") != "number" or "value" not in row:
        raise KeyError(name)
    return {
        "$value": row["value"],
        "$type": "number",
        "$extensions": {"source": src(name)},
    }


def font_token(name):
    row = RES[name]
    val = row.get("raw") or row.get("value")
    if not val:
        raise KeyError(name)
    return {
        "$value": val,
        "$type": "fontFamily",
        "$extensions": {"source": src(name) + "; family string, not a loaded file"},
    }


def ramp(prefix, steps):
    return {str(i): color_token(f"--{prefix}-{i}") for i in steps}


def brand(name):
    out = {"base": color_token("--" + name)}
    for stop in ("lightest", "lighter", "light", "dark", "darker", "darkest"):
        css = f"--{name}-{stop}"
        if css not in RES or RES[css].get("kind") != "color":
            continue
        out[stop] = color_token(css)
    return out


STEPS = list(range(1, 13))
BRANDS = [
    "aster", "evergreen", "goldenrod", "grey", "mahogany", "milkweed",
    "monarch-orange", "pool-blue", "walnut", "wheat",
]

core = {
    "color": {
        "gray": ramp("gray", STEPS),
        "orange": ramp("orange", STEPS),
        "blue": ramp("blue", STEPS),
        "green": ramp("green", STEPS),
        "red": ramp("red", STEPS),
        "yellow": ramp("yellow", STEPS),
        "indigo": ramp("indigo", STEPS),
        "pink": ramp("pink", STEPS),
        "purple": ramp("purple", STEPS),
        "brand": {name: brand(name) for name in BRANDS},
        "named": {
            "charcoal": color_token("--charcoal"),
            "daisy": color_token("--daisy"),
            "parchment": color_token("--parchment"),
            "sunbeam": color_token("--sunbeam"),
            "sky": color_token("--sky"),
            "subtle": color_token("--subtle"),
            "darkGrey": color_token("--dark-grey"),
            "lightAster": color_token("--light-aster"),
            "lightGoldenrod": color_token("--light-goldenrod"),
            "lightMilkweed": color_token("--light-milkweed"),
            "lightMonarchOrange": color_token("--light-monarch-orange"),
            "lightPersimmon": color_token("--light-persimmon"),
            "lightSky": color_token("--light-sky"),
            "secondaryGrey": color_token("--secondary-grey"),
            "tertiaryGrey": color_token("--tertiary-grey"),
        },
    },
    "font": {
        "primary": font_token("--font-primary"),
        "display": font_token("--font-display"),
        "secondary": font_token("--font-secondary"),
        "accent": font_token("--font-accent"),
    },
    "typography": {},
}

ROLES = {
    "display": "display",
    "heading1": "heading-1",
    "heading2": "heading-2",
    "heading3": "heading-3",
    "heading4": "heading-4",
    "heading5": "heading-5",
    "heading6": "heading-6",
    "body": "body",
    "small": "small",
    "extraSmall": "extra-small",
    "eyebrow": "eyebrow",
}
for key, slug in ROLES.items():
    size = RES[f"--type-{slug}-size"]["value"]
    leading = RES[f"--type-{slug}-leading"]["value"]
    weight = RES[f"--type-{slug}-weight"]["value"]
    core["typography"][key] = {
        "$type": "typography",
        "$value": {
            "fontFamily": "{font.primary}",
            "fontSize": size,
            "fontWeight": weight,
            "lineHeight": leading,
        },
        "$extensions": {
            "source": f"css-var --type-{slug}-size/leading/weight resolved on www.monarch.com, 2026-11-21. Family is --font-primary. Letter-spacing is Not captured as a token (raw string in css-vars.json).",
        },
    }
core["typography"]["display"]["$value"]["fontFamily"] = "{font.display}"
core["typography"]["display"]["$extensions"]["source"] += " Display family is --font-display (ABC Otto)."

light = {
    "page": color_token("--background"),
    "surface": color_token("--card"),
    "raised": color_token("--popover"),
    "text": color_token("--foreground"),
    "muted": color_token("--muted-foreground"),
    "accent": color_token("--primary"),
    "accentHover": color_token("--primary-hover"),
    "onAccent": color_token("--primary-foreground"),
    "border": color_token("--border"),
    "input": color_token("--input"),
    "ring": color_token("--ring"),
    "destructive": color_token("--destructive"),
    "onDestructive": color_token("--destructive-foreground"),
    "success": color_token("--success"),
    "successText": color_token("--success-foreground"),
    "warning": color_token("--warning"),
    "warningText": color_token("--warning-foreground"),
    "info": color_token("--info"),
    "infoText": color_token("--info-foreground"),
    "error": color_token("--error"),
    "errorText": color_token("--error-foreground"),
    "secondary": color_token("--secondary"),
    "secondaryText": color_token("--secondary-foreground"),
    "mutedSurface": color_token("--muted"),
    "cardText": color_token("--card-foreground"),
    "parchment": color_token("--parchment"),
    "wheat": color_token("--wheat"),
    "wheatLighter": color_token("--wheat-lighter"),
}

# page role: the painted body is parchment, while --background is the gray-2 surface.
# Record both. The catalog swatch for page should be the painted body.
light["page"] = {
    "$value": RES["--parchment"]["value"],
    "$type": "color",
    "$extensions": {
        "source": "computed body background rgb(253, 248, 237) on www.monarch.com homepage, matching css-var --parchment. --background resolves to "
        + RES["--background"]["value"]
        + " and is light.surfaceToken.",
    },
}
light["surfaceToken"] = color_token("--background")
light["button"] = {
    "$value": "#f35b16",
    "$type": "color",
    "$extensions": {
        "source": "computed backgroundColor of the header Sign up link on www.monarch.com, 2026-11-21, raw/components-computed.json signup.bg rgb(243, 91, 22). --primary resolves to #ff692d and is light.accent. --monarch-orange resolves to the same #f35b16.",
    },
}
light["buttonHover"] = {
    "$value": "#e64818",
    "$type": "color",
    "$extensions": {
        "source": "computed backgroundColor of the header Sign up link on hover, raw/components-computed.json signupHover.bg rgb(230, 72, 24). Matches --persimmon.",
    },
}
light["focusRing"] = {
    "$value": "#22201d",
    "$type": "color",
    "$extensions": {
        "source": "computed box-shadow of the focused Sign in link, raw/components-computed.json signinFocus.shadow: daisy 2px gap plus charcoal 4px ring.",
    },
}

tokens = {
    "core": core,
    "light": light,
    "dark": {},
    "$themes": [
        {
            "id": "light",
            "name": "Light",
            "selectedTokenSets": {"core": "source", "light": "enabled"},
            "$description": "The only theme the public site paints. No dark switch on www.monarch.com.",
        }
    ],
    "$metadata": {"tokenSetOrder": ["core", "light", "dark"]},
}

(HERE / "tokens.json").write_text(json.dumps(tokens, indent=2, ensure_ascii=False) + "\n")
print("wrote", HERE / "tokens.json")
print("core colors", sum(1 for _ in json.dumps(core["color"])))
