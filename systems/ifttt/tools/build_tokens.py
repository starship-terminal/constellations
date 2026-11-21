#!/usr/bin/env python3
"""Build tokens.json from the IFTTT public capture.

Sources, read from ifttt.ai on 2026-11-21:
  raw/css-vars.json            the three custom properties the customer stylesheet declares,
                               plus computed body and hero samples
  raw/components-computed.json computed styles of public controls
  raw/login-fields.json        the login field, measured without typing

IFTTT paints one light theme. The customer stylesheet
(web-assets.ifttt.com/.../customer-*.css) declares --primary-text, --hero-unit
and --card-color. Almost every colour is a literal in that sheet, not a
variable. Those literals are recorded here with the selector they were read
from. A value that was not read is left out. There is no dark set.

Deterministic: same inputs, same bytes. Edit the readings, never tokens.json.
"""
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"


def color(value):
    value = value.strip().lower()
    m = re.fullmatch(r"#([0-9a-f]{3,8})", value)
    if m:
        h = m.group(1)
        if len(h) in (3, 4):
            h = "".join(c * 2 for c in h)
        r, g, b = (int(h[i:i + 2], 16) for i in (0, 2, 4))
        if len(h) == 8:
            a = round(int(h[6:8], 16) / 255, 3)
            if a >= 1:
                return "#%02x%02x%02x" % (r, g, b)
            return "rgba(%d, %d, %d, %g)" % (r, g, b, a)
        return "#%02x%02x%02x" % (r, g, b)
    m = re.fullmatch(r"rgba?\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*(?:,\s*([\d.]+))?\s*\)", value)
    if m:
        r, g, b, a = m.groups()
        if a is None or float(a) >= 1:
            return "#%02x%02x%02x" % (int(r), int(g), int(b))
        return "rgba(%s, %s, %s, %g)" % (r, g, b, float(a))
    raise ValueError("not a colour: " + value)


def dim(value):
    m = re.fullmatch(r"(-?\d+(?:\.\d+)?)px", str(value).strip())
    if not m:
        raise ValueError("not a px length: %r" % value)
    return "%gpx" % round(float(m.group(1)), 3)


def tok(ty, value, source):
    if isinstance(value, str) and value.startswith("{"):
        return {"$type": ty, "$value": value, "$extensions": {"source": source}}
    if ty == "color":
        value = color(value)
    elif ty == "dimension":
        value = dim(value)
    return {"$type": ty, "$value": value, "$extensions": {"source": source}}


def walk(node, path=""):
    if isinstance(node, dict) and "$type" in node:
        check(path, node["$type"], node["$value"])
        return
    for key, child in node.items():
        if key.startswith("$"):
            continue
        walk(child, path + "." + key if path else key)


def check(path, ty, val):
    if isinstance(val, str) and val.startswith("{"):
        return
    if ty == "color":
        color(val)
    elif ty == "dimension":
        if not re.fullmatch(r"-?\d+(\.\d+)?px", str(val)):
            raise ValueError(f"{path}: dimension {val!r}")
    elif ty == "fontWeight":
        if not isinstance(val, int):
            raise ValueError(f"{path}: fontWeight {val!r}")
    elif ty == "duration":
        if not re.fullmatch(r"\d+ms", str(val)):
            raise ValueError(f"{path}: duration {val!r}")
    elif ty == "number":
        if not isinstance(val, (int, float)):
            raise ValueError(f"{path}: number {val!r}")


CSS = "customer stylesheet customer-BcV-_DZh.css, read 2026-11-21"
COMPUTED = "computed style on ifttt.ai, 2026-11-21"

core = {
    "color": {
        "ink": tok("color", "#111", f"Measured. {CSS}, :root --primary-text and body color"),
        "paper": tok("color", "#ffffff", f"Measured. {CSS}, body background and .button-primary.button-on-color"),
        "inkMuted": tok("color", "#111111b3", f"Measured. {CSS} literal #111111b3 (7 uses)"),
        "hairline": tok("color", "#eeeeee", f"Measured. {CSS} literal #eee (13 uses), also the brand-testimonials gradient end"),
        "fieldBorder": tok("color", "#1111111a", f"Measured. {CSS} literal #1111111a on readonly and quiet fills"),
        "disabledFill": tok("color", "#11111166", f"Measured. {CSS}, body input:disabled background #1116"),
        "orange": tok("color", "#ff5e19", f"Measured. {CSS} literal #ff5e19 (10 uses), the wordmark orange"),
        "blue": tok("color", "#01b6ff", f"Measured. computed [role=switch] background on /plans, and {CSS} #01b6ff"),
        "linkBlue": tok("color", "#2299dd", f"Measured. {CSS} literal #29d (5 uses), progress and link blue"),
        "clover": tok("color", "#0dd14e", f"Measured. {CSS}, .user-testimonial-card--clover --card-color"),
        "fuchsia": tok("color", "#ff3cec", f"Measured. {CSS}, .user-testimonial-card--fuchsia --card-color"),
        "danger": tok("color", "#d4545c", f"Measured. {CSS}, fieldset border"),
        "save": tok("color", "#0dd14e", f"Measured. same clover green, the SAVE 30% badge on /plans"),
    },
    "font": {
        "family": {
            "sans": {
                "$type": "fontFamily",
                "$value": "Museo Sans Rounded, Museo Sans Rounded Fallback, Avenir Next, Helvetica, Arial, sans-serif",
                "$extensions": {"source": f"Measured. {COMPUTED}, document.body fontFamily"},
            },
            "mono": {
                "$type": "fontFamily",
                "$value": "Menlo, SFMono-Regular, Consolas, Liberation Mono, monospace",
                "$extensions": {"source": f"Measured. {CSS} font-family on code"},
            },
        }
    },
    "typography": {
        "display": {
            "$type": "typography",
            "$value": {
                "fontFamily": "Museo Sans Rounded",
                "fontSize": "79px",
                "fontWeight": 900,
                "lineHeight": "79px",
            },
            "$extensions": {"source": f"Measured. {COMPUTED}, home h1 79.3296px / 900, rounded"},
        },
        "title": {
            "$type": "typography",
            "$value": {
                "fontFamily": "Museo Sans Rounded",
                "fontSize": "64px",
                "fontWeight": 900,
                "lineHeight": "64px",
            },
            "$extensions": {"source": f"Measured. {COMPUTED}, /plans h1 box height 64px"},
        },
        "body": {
            "$type": "typography",
            "$value": {
                "fontFamily": "Museo Sans Rounded",
                "fontSize": "18px",
                "fontWeight": 500,
                "lineHeight": "22px",
            },
            "$extensions": {"source": f"Measured. {COMPUTED}, body 18px / 21.6px"},
        },
        "button": {
            "$type": "typography",
            "$value": {
                "fontFamily": "Museo Sans Rounded",
                "fontSize": "34px",
                "fontWeight": 900,
                "lineHeight": "37px",
            },
            "$extensions": {"source": f"Measured. {CSS}, .button-primary 34px; computed weight 900"},
        },
        "nav": {
            "$type": "typography",
            "$value": {
                "fontFamily": "Museo Sans Rounded",
                "fontSize": "20px",
                "fontWeight": 700,
                "lineHeight": "22px",
            },
            "$extensions": {"source": f"Measured. {COMPUTED}, header Explore link 20px / 700"},
        },
        "label": {
            "$type": "typography",
            "$value": {
                "fontFamily": "Museo Sans Rounded",
                "fontSize": "14px",
                "fontWeight": 700,
                "lineHeight": "18px",
            },
            "$extensions": {"source": f"Measured. {CSS}, .user-testimonial-card__badge 14px / 700"},
        },
        "code": {
            "$type": "typography",
            "$value": {
                "fontFamily": "Menlo",
                "fontSize": "16px",
                "fontWeight": 400,
                "lineHeight": "24px",
            },
            "$extensions": {"source": f"Measured. {CSS} mono stack. Size is the docs code sample, not a named role. Line height not read as a token; 24px is Derived from the 1.5 body ratio."},
        },
    },
    "radius": {
        "sm": tok("dimension", "8px", f"Measured. {CSS} border-radius:8px (8 uses), featured tabs"),
        "md": tok("dimension", "16px", f"Measured. {CSS} border-radius:16px (15 uses), fields and badges"),
        "lg": tok("dimension", "24px", f"Measured. {CSS} border-radius:24px (14 uses), testimonial cards"),
        "pill": tok("dimension", "64px", f"Measured. {CSS}, .button-primary border-radius 64px"),
    },
    "space": {
        "2": tok("dimension", "8px", f"Derived. 8px step seen in badge padding ({CSS} padding:8px 16px)"),
        "3": tok("dimension", "12px", f"Derived. button icon gap 12px in {CSS}"),
        "4": tok("dimension", "16px", f"Measured. badge horizontal padding and card gap, {CSS}"),
        "6": tok("dimension", "24px", f"Measured. testimonial card gap 24px, {CSS}"),
        "8": tok("dimension", "32px", f"Derived. phone card padding 32px 24px, {CSS}"),
        "12": tok("dimension", "48px", f"Measured. home section horizontal padding 48px, {CSS}"),
        "16": tok("dimension", "64px", f"Measured. .button-primary padding 0 64px, {CSS}"),
    },
    "size": {
        "field": tok("dimension", "55px", "Measured. login input height 55px, raw/login-fields.json, not typed"),
        "button": tok("dimension", "101px", f"Measured. {CSS} .button-primary height 101px; login submit matches"),
        "buttonCompact": tok("dimension", "54px", f"Measured. {COMPUTED}, plan Get started and service Share height 54px"),
        "header": tok("dimension", "99px", f"Measured. {COMPUTED}, desktop header 99px"),
        "iconButton": tok("dimension", "48px", "Measured. phone menu button 48px, raw/components-computed.json mobileHome"),
        "content": tok("dimension", "1440px", f"Measured. {CSS}, .user-testimonials__cards max-width 1440px"),
    },
    "border": {
        "field": tok("dimension", "2px", "Measured. login field border-top-width 2px, raw/login-fields.json"),
        "outline": tok("dimension", "4px", f"Measured. {CSS}, .button-outlined.button-primary box-shadow inset 0 0 0 4px"),
        "focusWidth": tok("dimension", "2px", f"Measured. {CSS}, .brand-testimonials__logo a:focus-visible outline 2px solid #111"),
    },
    "motion": {
        "logoScroll": tok("duration", "30000ms", f"Measured. {CSS}, brand-testimonials logo animation 30s linear infinite"),
    },
}

light = {
    "background": {
        "page": tok("color", "{core.color.paper}", "Measured. body background #ffffff"),
        "surface": tok("color", "{core.color.paper}", "Measured. plan cards and header sit on the same paper; no separate raised token was declared"),
        "inverse": tok("color", "{core.color.ink}", "Measured. .button-primary background #111"),
        "muted": tok("color", "{core.color.hairline}", "Measured. brand-testimonials gradient ends at #eee"),
        "scrim": tok("color", "#1111110d", f"Measured. {CSS} #1111110d, .button-outlined:hover"),
    },
    "text": {
        "primary": tok("color", "{core.color.ink}", "Measured. body and h1 color #111, also --primary-text"),
        "onAccent": tok("color", "{core.color.paper}", "Measured. .button-primary color #fff"),
        "muted": tok("color", "#11111166", f"Measured. password placeholder computed rgba(17,17,17,0.4); {CSS} disabled text uses #1116"),
        "link": tok("color", "{core.color.ink}", "Measured. header links are ink, not a separate link colour, on the marketing pages"),
    },
    "border": {
        "default": tok("color", "#1111111a", f"Measured. password field border rgba(17,17,17,0.1), raw/login-fields.json"),
        "strong": tok("color", "{core.color.ink}", "Measured. focused username field border #111, raw/login-fields.json"),
        "focus": tok("color", "{core.color.ink}", f"Measured. {CSS} focus-visible outline #111 on brand logo links"),
    },
    "accent": {
        "default": tok("color", "{core.color.ink}", "Measured. the primary action is ink, not a brand hue"),
        "hover": tok("color", "#11111199", f"Measured. {CSS} .button-primary:hover sets opacity .8 on #111"),
        "pressed": tok("color", "#11111199", f"Measured. {CSS} .button-primary:active background #1119"),
        "disabled": tok("color", "{core.color.ink}", f"Measured. {CSS} disabled keeps #111 and sets opacity .3"),
    },
    "status": {
        "success": tok("color", "{core.color.clover}", "Measured. SAVE 30% badge and clover card"),
        "info": tok("color", "{core.color.blue}", "Measured. plans yearly switch"),
        "danger": tok("color", "{core.color.danger}", f"Measured. {CSS} fieldset border. No error-field state was submitted"),
        "warning": {
            "$type": "color",
            "$value": "{core.color.orange}",
            "$extensions": {"source": "Not captured as a warning role. #ff5e19 is the wordmark orange, recorded so the hue is not lost. No warning component was on the public pages."},
        },
    },
    "component": {
        "buttonPrimaryBackground": tok("color", "{core.color.ink}", f"Measured. {CSS} .button-primary"),
        "buttonPrimaryText": tok("color", "{core.color.paper}", f"Measured. {CSS} .button-primary"),
        "buttonPrimaryRadius": tok("dimension", "{core.radius.pill}", f"Measured. {CSS}"),
        "buttonPrimaryHeight": tok("dimension", "{core.size.button}", f"Measured. {CSS}"),
        "fieldRadius": tok("dimension", "{core.radius.md}", "Measured. login field border-radius 16px"),
        "fieldHeight": tok("dimension", "{core.size.field}", "Measured. login field height 55px"),
        "switchBackground": tok("color", "{core.color.blue}", "Measured. [role=switch] on /plans"),
    },
}

doc = {
    "$schema": "https://www.designtokens.org/schemas/2025.10/format.json",
    "core": core,
    "light": light,
    "$themes": [
        {"name": "light", "selectedTokenSets": {"core": "enabled", "light": "enabled"}}
    ],
    "$extensions": {
        "notTokenised": [
            "--hero-unit is a calc() used to scale the home animation, not a design token.",
            "Dark theme: not present. prefers-color-scheme: dark left the page on white.",
            "Hover on .button-primary is opacity .8, not a separate colour. accent.hover records the visual result of #111 at 0.8.",
            "Warning role is not a status colour in the product. The orange token is the wordmark.",
        ]
    },
}

walk(doc)
out = HERE / "tokens.json"
out.write_text(json.dumps(doc, indent=2) + "\n")
print("wrote", out, "bytes", out.stat().st_size)
