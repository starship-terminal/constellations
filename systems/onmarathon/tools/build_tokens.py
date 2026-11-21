#!/usr/bin/env python3
"""Build tokens.json from the onmarathon.com readings.

Sources, read on 2026-11-21:
  raw/css-vars.json            custom properties from the site CSS, resolved
                               on a probe with html.light and, separately,
                               with class dark forced. The dark probe is not
                               a live theme.
  raw/components-computed.json computed styles of public controls.

The live archive paints one light theme. Semantic colour tokens alias the
declared custom properties. Component sizes are measured. Dark role values
are recorded under $extensions.darkProbe and are not a theme set.

Deterministic: same inputs, same bytes.
"""
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
V = json.loads((RAW / "css-vars.json").read_text())
C = json.loads((RAW / "components-computed.json").read_text())["components"]

LIGHT = {n: d["value"] for n, d in V["resolved"]["light"].items()}
DARK = {n: d["value"] for n, d in V["resolved"]["dark"].items()}


def oklch_to_srgb(value):
    """oklch(L C H) as the browser computed it, to #rrggbb. Hex and rgb pass through."""
    v = value.strip()
    if v.startswith("#") or v.startswith("rgb"):
        return norm_color(v)
    m = re.fullmatch(r"oklch\(\s*([\d.]+)\s+([\d.]+)\s+([\d.]+)\s*\)", v)
    if not m:
        raise ValueError("not a colour: " + value)
    L, C, H = (float(x) for x in m.groups())
    h = H * 3.141592653589793 / 180
    a = C * __import__("math").cos(h)
    b = C * __import__("math").sin(h)
    l_ = L + 0.3963377774 * a + 0.2158037573 * b
    m_ = L - 0.1055613458 * a - 0.0638541728 * b
    s_ = L - 0.0894841775 * a - 1.2914855480 * b
    l_, m_, s_ = (x ** 3 for x in (l_, m_, s_))
    r = +4.0767416621 * l_ - 3.3077115913 * m_ + 0.2309699292 * s_
    g = -1.2684380046 * l_ + 2.6097574011 * m_ - 0.3413193965 * s_
    bch = -0.0041960863 * l_ - 0.7034186147 * m_ + 1.7076147010 * s_

    def lin_to_srgb(c):
        c = min(1, max(0, c))
        return 12.92 * c if c <= 0.0031308 else 1.055 * (c ** (1 / 2.4)) - 0.055

    rgb = tuple(round(lin_to_srgb(c) * 255) for c in (r, g, bch))
    return "#%02x%02x%02x" % rgb


def norm_color(v):
    v = v.strip().lower()
    if v.startswith("oklch"):
        return oklch_to_srgb(v)
    m = re.fullmatch(r"#([0-9a-f]{3,8})", v)
    if m:
        h = m.group(1)
        if len(h) in (3, 4):
            h = "".join(c * 2 for c in h)
        r, g, b = (int(h[i:i + 2], 16) for i in (0, 2, 4))
        return "#%02x%02x%02x" % (r, g, b)
    m = re.fullmatch(r"rgba?\(\s*(\d+)[,\s]+(\d+)[,\s]+(\d+)(?:\s*[,/]\s*([\d.]+))?\s*\)", v)
    if m:
        r, g, b, a = m.groups()
        if a is None or float(a) == 1:
            return "#%02x%02x%02x" % (int(r), int(g), int(b))
        return "rgba(%s, %s, %s, %g)" % (r, g, b, float(a))
    raise ValueError("not a colour: " + v)


def color_token(name, css_var):
    raw = LIGHT[css_var]
    token = {
        "$value": norm_color(raw),
        "$type": "color",
        "$extensions": {"source": f"Measured. css-var {css_var} on html.light, resolved {raw}"},
    }
    dark_raw = DARK.get(css_var)
    if dark_raw and dark_raw != raw:
        token["$extensions"]["darkProbe"] = norm_color(dark_raw)
        token["$extensions"]["darkProbeSource"] = (
            f"Not a live theme. Probe added class dark and removed light. Declared {dark_raw}."
        )
    return token


def dim(px, source):
    return {"$value": px, "$type": "dimension", "$extensions": {"source": source}}


def num(value, source):
    return {"$value": value, "$type": "number", "$extensions": {"source": source}}


def weight(value, source):
    return {"$value": value, "$type": "fontWeight", "$extensions": {"source": source}}


def duration(value, source):
    return {"$value": value, "$type": "duration", "$extensions": {"source": source}}


def bezier(value, source):
    return {"$value": value, "$type": "cubicBezier", "$extensions": {"source": source}}


def st(name, state="default"):
    return C[name]["states"][state]


def measured_px(name, state, prop):
    return st(name, state)[prop]


# Root 110% on html makes 1rem = 17.6px. The --radius declaration is 1rem.
RADIUS = "17.6px"
SRC_RADIUS = "Derived. --radius is 1rem; computed on the plan card as 17.6px (html font-size 110%)."

core = {
    "color": {
        "lime": color_token("lime", "--primary"),
        "limeHover": color_token("limeHover", "--primary-hover"),
        "ink": color_token("ink", "--foreground"),
        "inkMuted": color_token("inkMuted", "--muted-foreground"),
        "page": color_token("page", "--background"),
        "surface": color_token("surface", "--card"),
        "muted": color_token("muted", "--muted"),
        "border": color_token("border", "--border"),
        "destructive": color_token("destructive", "--destructive"),
        "onAccent": color_token("onAccent", "--primary-foreground"),
        "white": {
            "$value": "#ffffff",
            "$type": "color",
            "$extensions": {"source": "Measured. Get Started text color oklch(1 0 0) and the Free card background rgb(255, 255, 255)."},
        },
        "buttonHover": {
            "$value": "#404040",
            "$type": "color",
            "$extensions": {"source": "Measured. Get Started hover background rgb(64, 64, 64), class hover:bg-neutral-700."},
        },
        "focus": {
            "$value": "#005fcc",
            "$type": "color",
            "$extensions": {"source": "Measured. Keyboard focus outline on desktop links and buttons, rgb(0, 95, 204). Browser auto ring, not a site token."},
        },
    },
    "font": {
        "sans": {
            "$value": "Inter, \"Inter Fallback\", system-ui, sans-serif",
            "$type": "fontFamily",
            "$extensions": {"source": "Measured. Computed font-family on the nav link. --font-inter declares Inter, Inter Fallback."},
        },
        "display": {
            "$value": "graphik, \"graphik Fallback\", Inter, \"Inter Fallback\", system-ui, sans-serif",
            "$type": "fontFamily",
            "$extensions": {"source": "Measured. Computed font-family on the homepage h1. @font-face graphik weights 400 and 500."},
        },
    },
    "typography": {
        "display": {
            "$value": {
                "fontFamily": "{font.display}",
                "fontSize": "81.4px",
                "fontWeight": 500,
                "lineHeight": 1,
            },
            "$type": "typography",
            "$extensions": {"source": "Measured. Homepage h1: 81.4px / 81.4px, weight 500, graphik."},
        },
        "body": {
            "$value": {
                "fontFamily": "{font.sans}",
                "fontSize": "17.6px",
                "fontWeight": 400,
                "lineHeight": 1.5,
            },
            "$type": "typography",
            "$extensions": {"source": "Measured. Plan card body: 17.6px / 26.4px, weight 400, Inter. 17.6px is 1rem at the 110% root."},
        },
        "label": {
            "$value": {
                "fontFamily": "{font.sans}",
                "fontSize": "15.4px",
                "fontWeight": 500,
                "lineHeight": 1.43,
            },
            "$type": "typography",
            "$extensions": {"source": "Measured. Nav link and Get Started: 15.4px / 22px, weight 500."},
        },
        "caption": {
            "$value": {
                "fontFamily": "{font.sans}",
                "fontSize": "13.2px",
                "fontWeight": 500,
                "lineHeight": 1.33,
            },
            "$type": "typography",
            "$extensions": {"source": "Measured. Archive banner: 13.2px / 17.6px, weight 500."},
        },
    },
    "radius": {
        "md": dim(RADIUS, SRC_RADIUS),
        "pill": dim("9999px", "Measured. Get Started, billing toggle, badge and menu button border-radius."),
    },
    "space": {
        "2": dim("8.8px", "Measured. Billing toggle vertical padding and badge horizontal padding. 0.5rem at 17.6px root."),
        "3": dim("13.2px", "Measured. Archive banner padding and Get Started horizontal padding. 0.75rem."),
        "4": dim("17.6px", "Measured. Phone menu vertical padding. 1rem."),
        "5": dim("22px", "Measured. Billing toggle horizontal padding."),
        "6": dim("26.4px", "Measured. Phone menu horizontal padding. 1.5rem."),
        "10": dim("44px", "Measured. Plan card padding on all sides. 2.5rem."),
    },
    "motion": {
        "duration": duration("150ms", "Measured. Nav link, Get Started and banner transition-duration 0.15s."),
        "easing": bezier([0.4, 0, 0.2, 1], "Measured. transition-timing-function cubic-bezier(0.4, 0, 0.2, 1) on nav links and buttons."),
    },
}

light = {
    "page": {"$value": "{color.page}", "$type": "color", "$extensions": {"source": "Alias of color.page. html.light --background."}},
    "surface": {"$value": "{color.surface}", "$type": "color", "$extensions": {"source": "Alias of color.surface. html.light --card. The Free plan card paints rgb(255, 255, 255), the same value."}},
    "text": {"$value": "{color.ink}", "$type": "color", "$extensions": {"source": "Alias of color.ink. html.light --foreground. Measured on the h1 and the wordmark."}},
    "muted": {"$value": "{color.inkMuted}", "$type": "color", "$extensions": {"source": "Alias of color.inkMuted. html.light --muted-foreground. Measured on the resting nav link."}},
    "accent": {"$value": "{color.lime}", "$type": "color", "$extensions": {"source": "Alias of color.lime. Painted on the archive banner and the Pro plan card as rgb(215, 253, 81). The CSS name is --primary."}},
    "accentText": {"$value": "{color.onAccent}", "$type": "color", "$extensions": {"source": "Alias of color.onAccent. html.light --primary-foreground. The banner text uses this."}},
    "onAccent": {"$value": "{color.white}", "$type": "color", "$extensions": {"source": "Measured. Get Started label is oklch(1 0 0) on the ink button."}},
    "border": {"$value": "{color.border}", "$type": "color", "$extensions": {"source": "Alias of color.border. html.light --border. Declared. No captured control paints a 1px border in this colour."}},
    "link": {"$value": "{color.inkMuted}", "$type": "color", "$extensions": {"source": "Measured. Resting nav and footer links use --muted-foreground. Hover moves them to --foreground."}},
    "destructive": {"$value": "{color.destructive}", "$type": "color", "$extensions": {"source": "Declared as --destructive on :root and .light. Not painted on any captured public control."}},
    "focus": {"$value": "{color.focus}", "$type": "color", "$extensions": {"source": "Measured. Desktop keyboard focus outline rgb(0, 95, 204), 1px auto, offset 1px."}},
    "button": {
        "$value": "{color.ink}",
        "$type": "color",
        "$extensions": {"source": "Measured. Get Started and Return Home background oklch(0.15 0 0), the same value as --foreground."},
    },
    "buttonHover": {
        "$value": "{color.buttonHover}",
        "$type": "color",
        "$extensions": {"source": "Measured. Get Started hover background rgb(64, 64, 64)."},
    },
    "component": {
        "button": {
            "height": dim("39.594px", "Measured. Get Started height 39.5938px at 1440."),
            "radius": dim("9999px", "Measured. Get Started border-radius."),
            "paddingX": dim("13.2px", "Measured. Get Started horizontal padding."),
        },
        "banner": {
            "height": dim("43.969px", "Measured. Archive banner height 43.9688px at 1440."),
        },
        "header": {
            "height": dim("56px", "Observed. Header row class is h-[56px]. Not read as a custom property."),
        },
        "nav": {
            "fontSize": dim("15.4px", "Measured. Nav link font-size."),
        },
        "plan": {
            "radius": dim(RADIUS, SRC_RADIUS),
            "padding": dim("44px", "Measured. Plan card padding 44px."),
        },
        "menuButton": {
            "size": dim("39.594px", "Measured. Open menu button 39.5938px square at 390."),
        },
        "focus": {
            "width": dim("1px", "Measured. focus-visible outline-width on desktop links."),
            "offset": dim("1px", "Measured. focus-visible outline-offset on desktop links. The phone menu button's ring offset was not recorded."),
        },
    },
}

tokens = {
    "core": core,
    "light": light,
    "$themes": [{
        "id": "light",
        "name": "Light",
        "selectedTokenSets": {"core": "source", "light": "enabled"},
        "$description": "The only theme the public archive paints. html carries class light. A .dark rule exists and was probed; it is not a live theme.",
    }],
    "$metadata": {"tokenSetOrder": ["core", "light"]},
}

(HERE / "tokens.json").write_text(json.dumps(tokens, indent=2, ensure_ascii=False) + "\n")
print("wrote tokens.json")
