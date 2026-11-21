#!/usr/bin/env python3
"""Build tokens.json from Typefully's public CSS and computed styles.

Sources, read on 2026-11-21 from https://typefully.com/pricing and the
homepage login dialog, signed out:
  raw/css-vars.json              custom properties from the pricing stylesheets
  raw/components-computed.json   computed styles of public controls

The public site has no theme toggle. One light semantic set is written.
A dark class on a probe document did not change any resolved value, so no
dark set is invented.

Every token carries $extensions.source. Deterministic: same inputs, same output.
"""
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
VARS = json.loads((RAW / "css-vars.json").read_text())
COMP = json.loads((RAW / "components-computed.json").read_text())
LIGHT = VARS["resolved"]["light"]


def rgb_to_hex(value):
    value = value.strip()
    m = re.fullmatch(r"rgb\((\d+),\s*(\d+),\s*(\d+)\)", value)
    if m:
        return "#%02x%02x%02x" % tuple(int(x) for x in m.groups())
    m = re.fullmatch(r"rgba\((\d+),\s*(\d+),\s*(\d+),\s*([\d.]+)\)", value)
    if m:
        r, g, b, a = m.groups()
        a = float(a)
        if a == 1:
            return "#%02x%02x%02x" % (int(r), int(g), int(b))
        return "rgba(%s, %s, %s, %g)" % (r, g, b, a)
    if value.startswith("#") or value.startswith("rgba("):
        return value
    raise ValueError("not a colour: " + value)


def var_color(name):
    item = LIGHT[name]
    if item.get("kind") != "color":
        raise KeyError(name)
    return rgb_to_hex(item["value"])


def color(value, source):
    return {
        "$type": "color",
        "$value": value,
        "$extensions": {"source": source},
    }


def dim(value, source):
    return {
        "$type": "dimension",
        "$value": value,
        "$extensions": {"source": source},
    }


def other(ty, value, source):
    return {"$type": ty, "$value": value, "$extensions": {"source": source}}


def measured(name, state, prop):
    node = COMP["components"][name][state]
    return node[prop]


SRC_VARS = "Measured CSS custom property from https://typefully.com/pricing stylesheets, raw/css-vars.json, 2026-11-21"
SRC_COMP = "Measured computed style on a public control, raw/components-computed.json, 2026-11-21"


def ramp():
    steps = [
        "25", "50", "75", "100", "150", "200", "250", "300", "350", "400",
        "450", "500", "550", "600", "650", "675", "700", "750", "800", "825",
        "850", "900", "925", "950", "975",
    ]
    out = {}
    for step in steps:
        name = f"--color-typ-{step}"
        out[step] = color(var_color(name), f"{SRC_VARS}; {name}")
    return out


core = {
    "color": {
        "neutral": ramp(),
        "accent": color(var_color("--color-typ-accent"), f"{SRC_VARS}; --color-typ-accent"),
        "ai": color(var_color("--color-typ-ai"), f"{SRC_VARS}; --color-typ-ai"),
        "aiDark": color(var_color("--color-typ-ai-dark"), f"{SRC_VARS}; --color-typ-ai-dark"),
        "aiLight": color(var_color("--color-typ-ai-light"), f"{SRC_VARS}; --color-typ-ai-light"),
        "error": color(var_color("--color-typ-error"), f"{SRC_VARS}; --color-typ-error"),
        "success": color(var_color("--color-typ-success"), f"{SRC_VARS}; --color-typ-success"),
        "orange": color(var_color("--color-typ-orange"), f"{SRC_VARS}; --color-typ-orange"),
        "linkedin": color(var_color("--color-typ-linkedin"), f"{SRC_VARS}; --color-typ-linkedin"),
        "white": color(var_color("--color-typ-white"), f"{SRC_VARS}; --color-typ-white"),
        "black": color(var_color("--color-typ-black"), f"{SRC_VARS}; --color-typ-black"),
    },
    "fontFamily": {
        "inter": other(
            "fontFamily",
            "Inter, -apple-system, system-ui, Helvetica Neue, Helvetica, sans-serif",
            SRC_COMP + "; body and button fontFamily on /pricing",
        ),
        "system": other(
            "fontFamily",
            LIGHT["--font-system"]["raw"],
            SRC_VARS + "; --font-system",
        ),
        "mono": other("fontFamily", LIGHT["--font-mono"]["raw"], SRC_VARS + "; --font-mono"),
    },
    "fontWeight": {
        "regular": other("fontWeight", "400", SRC_VARS + "; --font-weight-normal"),
        "medium": other("fontWeight", "500", SRC_VARS + "; --font-weight-medium"),
        "semibold": other("fontWeight", "600", SRC_VARS + "; --font-weight-semibold"),
        "bold": other("fontWeight", "700", SRC_VARS + "; --font-weight-bold"),
    },
    "typography": {
        "display": other("typography", {
            "fontFamily": "{fontFamily.inter}",
            "fontSize": "40px",
            "fontWeight": "{fontWeight.bold}",
            "lineHeight": "40px",
        }, SRC_COMP + "; heading Pricing on /pricing"),
        "body": other("typography", {
            "fontFamily": "{fontFamily.inter}",
            "fontSize": "14px",
            "fontWeight": "{fontWeight.regular}",
            "lineHeight": "20px",
        }, SRC_COMP + "; text-field on the login dialog"),
        "label": other("typography", {
            "fontFamily": "{fontFamily.inter}",
            "fontSize": "14px",
            "fontWeight": "{fontWeight.semibold}",
            "lineHeight": "18.2px",
        }, SRC_COMP + "; button-primary Get started"),
        "nav": other("typography", {
            "fontFamily": "{fontFamily.system}",
            "fontSize": "14.5px",
            "fontWeight": "{fontWeight.regular}",
            "lineHeight": "21.75px",
        }, SRC_COMP + "; link-nav Pricing"),
    },
    "radius": {
        "xs": dim(LIGHT["--radius-xs"]["value"], SRC_VARS + "; --radius-xs computed at 1440"),
        "sm": dim(LIGHT["--radius-sm"]["value"], SRC_VARS + "; --radius-sm computed"),
        "md": dim(LIGHT["--radius-md"]["value"], SRC_VARS + "; --radius-md computed"),
        "lg": dim(LIGHT["--radius-lg"]["value"], SRC_VARS + "; --radius-lg computed"),
        "xl": dim(LIGHT["--radius-xl"]["value"], SRC_VARS + "; --radius-xl computed"),
        "button": dim("9.6px", SRC_COMP + "; button-primary borderTopLeftRadius"),
        "card": dim("12px", SRC_COMP + "; button-secondary borderTopLeftRadius, the quiet plan card button"),
        "pill": dim("9999px", "Derived from a computed pill radius of 3.35544e+07px on link-cta, which is a full pill"),
    },
    "space": {
        "1": dim("4px", SRC_COMP + "; link-nav paddingTop 4px"),
        "2": dim("8px", SRC_COMP + "; text-field paddingTop 8px"),
        "3": dim("12px", SRC_COMP + "; button-primary paddingLeft 12px"),
        "4": dim("16px", SRC_COMP + "; link-cta paddingLeft 16px"),
        "5": dim("18px", SRC_COMP + "; button-auth paddingLeft 18px"),
    },
    "size": {
        "button": dim("32px", SRC_COMP + "; button-primary height"),
        "buttonAuth": dim("38px", SRC_COMP + "; button-auth height 37.9958px, rounded"),
        "field": dim("32px", SRC_COMP + "; text-field height"),
        "navLink": dim("30px", SRC_COMP + "; link-nav height 29.75px, rounded"),
    },
    "motion": {
        "fast": other("duration", "100ms", SRC_COMP + "; link-cta transitionDuration 0.1s"),
        "base": other("duration", "150ms", SRC_COMP + "; button-primary transitionDuration 0.15s"),
        "slow": other("duration", "200ms", SRC_COMP + "; button-auth transitionDuration 0.2s"),
        "ease": other("cubicBezier", [0.4, 0, 0.2, 1], SRC_COMP + "; button-primary transitionTimingFunction"),
    },
    "layout": {
        "desktop": dim("1440px", "Requested desktop viewport, confirmed by screenshot sidecar innerWidth"),
        "phone": dim("390px", "Requested phone viewport"),
    },
}

light = {
    "color": {
        "bg": {
            "page": color(var_color("--color-typ-bg0"), f"{SRC_VARS}; --color-typ-bg0"),
            "surface": color(var_color("--color-typ-bg1"), f"{SRC_VARS}; --color-typ-bg1"),
            "raised": color(var_color("--color-typ-white"), f"{SRC_VARS}; --color-typ-white"),
            "muted": color(var_color("--color-typ-bg3"), f"{SRC_VARS}; --color-typ-bg3"),
        },
        "text": {
            "primary": color(var_color("--color-typ-c1"), f"{SRC_VARS}; --color-typ-c1"),
            "secondary": color(var_color("--color-typ-c2"), f"{SRC_VARS}; --color-typ-c2"),
            "muted": color(var_color("--color-typ-c3"), f"{SRC_VARS}; --color-typ-c3"),
            "disabled": color(var_color("--color-typ-c4"), f"{SRC_VARS}; --color-typ-c4. Role assigned from the ramp name, not from a disabled control"),
            "onAccent": color(var_color("--color-typ-white"), f"{SRC_VARS}; --color-typ-white. Measured on button-primary as rgb(255, 255, 255)"),
            "link": color(var_color("--color-typ-accent"), f"{SRC_VARS}; --color-typ-accent. Measured on link-nav"),
        },
        "border": {
            "default": color(var_color("--color-typ-c6"), f"{SRC_VARS}; --color-typ-c6. Measured on button-secondary border rgb(230, 232, 234)"),
            "subtle": color(var_color("--color-typ-c7"), f"{SRC_VARS}; --color-typ-c7. Measured on text-field border rgb(238, 240, 241)"),
            "focus": color(var_color("--color-typ-accent"), f"{SRC_VARS}; --color-typ-accent. Focus ring uses this hue at low alpha; the ring itself is a box-shadow, Not captured as a single colour token"),
        },
        "accent": {
            "default": color(var_color("--color-typ-accent"), f"{SRC_VARS}; --color-typ-accent"),
            "hover": color(var_color("--color-typ-accent"), f"{SRC_COMP}; hover on button-primary did not change backgroundColor. Hover colour Not captured as a distinct value"),
        },
        "status": {
            "success": color(var_color("--color-typ-success"), f"{SRC_VARS}; --color-typ-success"),
            "danger": color(var_color("--color-typ-error"), f"{SRC_VARS}; --color-typ-error"),
            "warning": color(var_color("--color-typ-orange"), f"{SRC_VARS}; --color-typ-orange. No warning component was on screen; the token is the declared orange"),
            "info": color(var_color("--color-typ-accent"), f"{SRC_VARS}; --color-typ-accent"),
        },
    },
    "component": {
        "button": {
            "bg": color("{color.accent.default}", "alias"),
            "text": color("{color.text.onAccent}", "alias"),
            "radius": dim("{radius.button}", "alias"),
            "height": dim("{size.button}", "alias"),
        },
    },
}

# alias values that are not colours should not use color(). Fix component aliases.
light["component"]["button"]["radius"] = {"$type": "dimension", "$value": "{radius.button}", "$extensions": {"source": "alias of core.radius.button"}}
light["component"]["button"]["height"] = {"$type": "dimension", "$value": "{size.button}", "$extensions": {"source": "alias of core.size.button"}}
light["component"]["button"]["bg"] = {"$type": "color", "$value": "{color.accent.default}", "$extensions": {"source": "alias"}}
light["component"]["button"]["text"] = {"$type": "color", "$value": "{color.text.onAccent}", "$extensions": {"source": "alias"}}

doc = {
    "$schema": "https://www.w3.org/community/design-tokens/",
    "core": core,
    "light": light,
    "$themes": [{"id": "light", "name": "Light", "selectedTokenSets": {"core": "source", "light": "enabled"}}],
    "$metadata": {"tokenSetOrder": ["core", "light"]},
}

out = HERE / "tokens.json"
out.write_text(json.dumps(doc, indent=2) + "\n")
print("wrote", out, "core groups", list(core), "light groups", list(light))
