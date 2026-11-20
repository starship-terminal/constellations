#!/usr/bin/env python3
"""Build tokens.json from raw/css-vars.json and raw/components-computed.json.

Unsplash declares a light palette on :root and semantic names on .light.
A .dark class exists in the stylesheet. The public pages never apply it, so
dark values are recorded as declared, not as a painted theme. The package
exports core and light only. A dark set would look like a shipped theme.

Every token carries $extensions.source. Unread values stay out.
"""
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
V = json.loads((RAW / "css-vars.json").read_text())
DECL = {d["name"]: d for d in V["decls"]}


def css(name):
    if name not in DECL:
        raise KeyError(name)
    return DECL[name]


def norm_color(v):
    v = v.strip().lower()
    if v == "white":
        return "#ffffff"
    if v == "black":
        return "#000000"
    m = re.fullmatch(r"#([0-9a-f]{3,8})", v)
    if m:
        h = m.group(1)
        if len(h) in (3, 4):
            h = "".join(c * 2 for c in h)
        if len(h) == 8:
            r, g, b = (int(h[i:i + 2], 16) for i in (0, 2, 4))
            a = int(h[6:8], 16) / 255
            if a >= 0.999:
                return "#%02x%02x%02x" % (r, g, b)
            return "rgba(%d, %d, %d, %g)" % (r, g, b, round(a, 3))
        return "#%02x%02x%02x" % tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))
    m = re.fullmatch(r"rgba?\(\s*(\d+)[,\s]+(\d+)[,\s]+(\d+)(?:\s*[,/]\s*([\d.]+))?\s*\)", v)
    if m:
        r, g, b, a = m.groups()
        if a is None or float(a) == 1:
            return "#%02x%02x%02x" % (int(r), int(g), int(b))
        return "rgba(%s, %s, %s, %g)" % (r, g, b, float(a))
    raise ValueError("not a colour: " + v)


def resolve(name, seen=None):
    seen = seen or []
    if name in seen:
        raise ValueError("cycle " + name)
    d = css(name)
    val = d["value"].strip()
    m = re.fullmatch(r"var\((--[\w-]+)\)", val)
    if m:
        return resolve(m.group(1), seen + [name])
    return val, d


def color_token(path, name):
    val, d = resolve(name)
    return {
        "$type": "color",
        "$value": norm_color(val),
        "$extensions": {"source": f"Measured css-var {name} selector {d['selector']} page {d['page']} ({V['read']})"},
    }


def dim_token(name):
    d = css(name)
    val = d["value"].strip()
    if val.endswith("s") and not val.endswith("ms"):
        # duration, not a dimension
        ms = int(round(float(val[:-1]) * 1000))
        return {"$type": "duration", "$value": f"{ms}ms",
                "$extensions": {"source": f"Measured css-var {name} ({d['value']}) selector {d['selector']}"}}
    if not re.fullmatch(r"-?\d+(\.\d+)?px", val):
        raise ValueError(f"{name} is not a px length: {val}")
    return {"$type": "dimension", "$value": val,
            "$extensions": {"source": f"Measured css-var {name} selector {d['selector']} page {d['page']}"}}


def measured_color(value, where):
    return {"$type": "color", "$value": norm_color(value),
            "$extensions": {"source": f"Measured computed style {where}"}}


core = {
    "color": {
        "black": color_token("color.black", "--color-black"),
        "white": color_token("color.white", "--color-white"),
        "blue": color_token("color.blue", "--color-blue"),
        "blue-dark": color_token("color.blue-dark", "--color-blue-dark"),
        "green": color_token("color.green", "--color-green"),
        "green-dark": color_token("color.green-dark", "--color-green-dark"),
        "pink": color_token("color.pink", "--color-pink"),
        "pink-dark": color_token("color.pink-dark", "--color-pink-dark"),
        "red": color_token("color.red", "--color-red"),
        "red-dark": color_token("color.red-dark", "--color-red-dark"),
        "gray": {
            "100": color_token("color.gray.100", "--color-gray-100"),
            "200": color_token("color.gray.200", "--color-gray-200"),
            "400": color_token("color.gray.400", "--color-gray-400"),
            "600": color_token("color.gray.600", "--color-gray-600"),
            "700": color_token("color.gray.700", "--color-gray-700"),
            "800": color_token("color.gray.800", "--color-gray-800"),
        },
        "border-opacity": color_token("color.border-opacity", "--color-border-opacity"),
        "backdrop": color_token("color.backdrop", "--color-backdrop-bg"),
    },
    "font": {
        "family": {
            "$type": "fontFamily",
            "$value": "ui-sans-serif, system-ui, sans-serif",
            "$extensions": {"source": "Measured computed style body fontFamily on https://unsplash.com/ (css-vars.json computed.home.roles.body)"},
        },
    },
    "typography": {},
    "radius": {
        "button": dim_token("--button-border-radius"),
        "modal": dim_token("--modal-border-radius"),
    },
    "space": {
        "unit": dim_token("--spacing-unit"),
        "nav": dim_token("--nav-height"),
        "control-small": dim_token("--height-small"),
        "control-medium": dim_token("--height-medium"),
        "control-large": dim_token("--height-large"),
    },
    "motion": {
        "base": dim_token("--transition-speed-base"),
    },
}

# Heading and text scales are unitless line-heights plus px sizes. Keep them as
# typography composites. Line height is derived from the declared ratio.
for role, size_name, weight_name, lh_name in (
    ("heading-xxl", "--heading-xxl-font-size", "--heading-xxl-font-weight", "--heading-xxl-line-height"),
    ("heading-xl", "--heading-xl-font-size", "--heading-xl-font-weight", "--heading-xl-line-height"),
    ("heading-l", "--heading-l-font-size", "--heading-l-font-weight", "--heading-l-line-height"),
    ("heading-m", "--heading-m-font-size", "--heading-m-font-weight", "--heading-m-line-height"),
    ("heading-s", "--heading-s-font-size", "--heading-s-font-weight", "--heading-s-line-height"),
    ("heading-xs", "--heading-xs-font-size", "--heading-xs-font-weight", "--heading-xs-line-height"),
    ("heading-xxs", "--heading-xxs-font-size", "--heading-xxs-font-weight", "--heading-xxs-line-height"),
):
    size = css(size_name)["value"].strip()
    weight = int(css(weight_name)["value"].strip())
    ratio = float(css(lh_name)["value"].strip())
    px = float(size[:-2])
    lh = ("%g" % round(px * ratio, 2)) + "px"
    core["typography"][role] = {
        "$type": "typography",
        "$value": {
            "fontFamily": "{font.family}",
            "fontSize": size,
            "fontWeight": weight,
            "lineHeight": lh,
        },
        "$extensions": {
            "source": f"Measured css-var {size_name} {weight_name}; lineHeight Derived from {lh_name} {css(lh_name)['value']} times the size",
        },
    }

for role, size_name, lh_name in (
    ("text-m", "--text-m-font-size", "--text-m-line-height"),
    ("text-s", "--text-s-font-size", "--text-s-line-height"),
    ("text-xs", "--text-xs-font-size", "--text-xs-line-height"),
):
    size = css(size_name)["value"].strip()
    ratio = float(css(lh_name)["value"].strip())
    px = float(size[:-2])
    lh = ("%g" % round(px * ratio, 2)) + "px"
    core["typography"][role] = {
        "$type": "typography",
        "$value": {
            "fontFamily": "{font.family}",
            "fontSize": size,
            "fontWeight": 400,
            "lineHeight": lh,
        },
        "$extensions": {
            "source": f"Measured css-var {size_name}; fontWeight 400 is the body computed weight, not a declared token; lineHeight Derived from {lh_name}",
        },
    }

body = V["computed"]["home"]["roles"]["body"]
core["typography"]["body"] = {
    "$type": "typography",
    "$value": {
        "fontFamily": "{font.family}",
        "fontSize": body["fontSize"],
        "fontWeight": 400,
        "lineHeight": body["lineHeight"],
    },
    "$extensions": {"source": "Measured computed style body on https://unsplash.com/ (css-vars.json computed.home.roles.body)"},
}

light = {
    "page": color_token("page", "--color-white"),
    "surface": color_token("surface", "--color-gray-100"),
    "text": color_token("text", "--color-black"),
    "muted": color_token("muted", "--color-gray-700"),
    "accent": color_token("accent", "--color-black"),
    "border": color_token("border", "--color-gray-400"),
    "link": color_token("link", "--link-text-color"),
    "link-hover": color_token("link-hover", "--link-text-color-hover"),
    "button": color_token("button", "--button-primary-background-color"),
    "button-hover": color_token("button-hover", "--button-primary-background-color-hover"),
    "button-text": color_token("button-text", "--button-primary-text-color"),
    "placeholder": color_token("placeholder", "--placeholder-background-color"),
    "separator": color_token("separator", "--color-separator"),
    "scrim": color_token("scrim", "--color-backdrop-bg"),
    "success": color_token("success", "--color-green"),
    "danger": color_token("danger", "--color-red"),
    "info": color_token("info", "--color-blue"),
    "focus": measured_color("rgb(17, 17, 17)", "submit-button focus-visible color, components-computed.json"),
}

# Hover of the primary button was also measured on the login submit.
light["button-hover"]["$extensions"]["source"] += "; confirmed computed rgb(34, 34, 34) on login-submit hover"

doc = {
    "core": core,
    "light": light,
    "$themes": [{"name": "light", "selectedTokenSets": {"core": "source", "light": "enabled"}}],
}

out = HERE / "tokens.json"
out.write_text(json.dumps(doc, indent=1) + "\n")
print("wrote", out, "core groups", list(core), "light", len(light))
