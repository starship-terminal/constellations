#!/usr/bin/env python3
"""Build tokens.json from Sharewillow's declared CSS custom properties.

Sources, read from www.sharewillow.com on 2026-11-21:
  raw/css-vars.json            --color-*, --font-*, --radius-*, --spacing,
                               --ease-* declared on :root in the Next.js CSS
  raw/components-computed.json computed styles for the public button, field,
                               nav link and login wall (app.sharewillow.com)

The marketing site ships one light theme. --color-hero-* paints a dark
section inside that page. It is not a theme toggle, so there is no dark set.

Unread interaction values stay out. A token that could not be read is not invented.
"""
import json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
V = json.loads((RAW / "css-vars.json").read_text())
DECL = {n: rec.get("value") or rec.get("raw") for n, rec in V["resolved"]["light"].items()}


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
            return "rgba(%d, %d, %d, %s)" % (r, g, b, ("%g" % a))
        return "#%02x%02x%02x" % (r, g, b)
    m = re.fullmatch(r"rgba?\(\s*(\d+)[,\s]+(\d+)[,\s]+(\d+)(?:\s*[,/]\s*([\d.]+))?\s*\)", v)
    if m:
        r, g, b, a = m.groups()
        if a is None or float(a) == 1:
            return "#%02x%02x%02x" % (int(r), int(g), int(b))
        return "rgba(%s, %s, %s, %g)" % (r, g, b, float(a))
    raise ValueError("not a colour: " + v)


def color(name, description=None):
    val = norm_color(DECL[name])
    t = {"$value": val, "$type": "color", "$extensions": {"source": f"Measured css-var {name} on :root, www.sharewillow.com, 2026-11-21, light"}}
    if description:
        t["$description"] = description
    return t


def dim_from_var(name):
    raw = DECL[name].strip()
    if raw.endswith("rem"):
        px = float(raw[:-3]) * 16
        val = "%gpx" % px
        src = f"Derived {name} {raw} at 16px root, declared on :root"
    elif raw.endswith("px"):
        val = raw
        src = f"Measured css-var {name} on :root"
    else:
        raise ValueError(name + " " + raw)
    return {"$value": val, "$type": "dimension", "$extensions": {"source": src}}


def ease(name):
    raw = DECL[name].strip()
    m = re.fullmatch(r"cubic-bezier\(\s*([-\d.]+)[,\s]+([-\d.]+)[,\s]+([-\d.]+)[,\s]+([-\d.]+)\s*\)", raw)
    if not m:
        raise ValueError(raw)
    val = [float(x) for x in m.groups()]
    return {"$value": val, "$type": "cubicBezier", "$extensions": {"source": f"Measured css-var {name} on :root ({raw})"}}


def measured_color(value, where):
    return {"$value": norm_color(value), "$type": "color", "$extensions": {"source": f"Measured computed style, {where}"}}


def measured_dim(value, where):
    return {"$value": value, "$type": "dimension", "$extensions": {"source": f"Measured computed style, {where}"}}


CORE = {
    "palette": {
        "ivory": color("--color-ivory", "Page ground. Same value as --color-bg."),
        "paper": color("--color-paper"),
        "surface2": color("--color-surface-2"),
        "espresso": color("--color-espresso", "Ink. Same value as --color-ink."),
        "inkMuted": color("--color-ink-muted"),
        "inkSubtle": color("--color-ink-subtle"),
        "lemon": color("--color-lemon", "Accent. Same value as --color-accent."),
        "lemonDeep": color("--color-lemon-deep"),
        "lime": color("--color-lime"),
        "peach": color("--color-peach"),
        "sky": color("--color-sky"),
        "rose": color("--color-rose"),
        "heroBg": color("--color-hero-bg"),
        "heroSurface": color("--color-hero-surface"),
        "heroSurface2": color("--color-hero-surface-2"),
        "heroInk": color("--color-hero-ink"),
        "heroInkMuted": color("--color-hero-ink-muted"),
        "heroInkSubtle": color("--color-hero-ink-subtle"),
        "heroBorder": color("--color-hero-border"),
        "heroBorderStrong": color("--color-hero-border-strong"),
        "border": color("--color-border"),
        "borderStrong": color("--color-border-strong"),
        "buttonHover": measured_color("rgb(43, 26, 16)", "primary Book a demo button :hover, homepage, 2026-11-21"),
        "heroInkOnButton": measured_color("rgb(245, 242, 224)", "primary button text, homepage, 2026-11-21"),
    },
    "font": {
        "family": {
            "sans": {"$value": DECL["--font-sans"], "$type": "fontFamily", "$extensions": {"source": "Measured css-var --font-sans on :root"}},
            "display": {"$value": DECL["--font-display"], "$type": "fontFamily", "$extensions": {"source": "Measured css-var --font-display on :root"}},
            "mono": {"$value": DECL["--font-mono"], "$type": "fontFamily", "$extensions": {"source": "Measured css-var --font-mono on :root"}},
        }
    },
    "typography": {
        "display": {
            "$type": "typography",
            "$value": {
                "fontFamily": "{core.font.family.display}",
                "fontSize": "80px",
                "fontWeight": 500,
                "lineHeight": "80px",
                "letterSpacing": "-2.4px",
            },
            "$extensions": {"source": "Measured homepage h1 computed style, 2026-11-21: 80px/80px, weight 500, letter-spacing -2.4px, Mackinac. Size is rendered, not a named CSS token."},
        },
        "body": {
            "$type": "typography",
            "$value": {
                "fontFamily": "{core.font.family.sans}",
                "fontSize": "16px",
                "fontWeight": 400,
                "lineHeight": "{core.leading.relaxed}",
            },
            "$extensions": {"source": "Measured body font-size 16px on the homepage; line-height aliases --leading-relaxed"},
        },
        "label": {
            "$type": "typography",
            "$value": {
                "fontFamily": "{core.font.family.sans}",
                "fontSize": "14px",
                "fontWeight": 500,
                "lineHeight": "1.25",
            },
            "$extensions": {"source": "Measured nav link 14px and primary button label 16px/500. Label role uses the nav size."},
        },
        "caption": {
            "$type": "typography",
            "$value": {
                "fontFamily": "{core.font.family.sans}",
                "fontSize": "13px",
                "fontWeight": 400,
                "lineHeight": "1.375",
            },
            "$extensions": {"source": "Measured announcement bar 13px, homepage, 2026-11-21"},
        },
    },
    "leading": {
        "tight": {"$value": 1.25, "$type": "number", "$extensions": {"source": "Measured css-var --leading-tight"}},
        "snug": {"$value": 1.375, "$type": "number", "$extensions": {"source": "Measured css-var --leading-snug"}},
        "relaxed": {"$value": 1.625, "$type": "number", "$extensions": {"source": "Measured css-var --leading-relaxed"}},
    },
    "weight": {
        "normal": {"$value": 400, "$type": "fontWeight", "$extensions": {"source": "Measured css-var --font-weight-normal"}},
        "medium": {"$value": 500, "$type": "fontWeight", "$extensions": {"source": "Measured css-var --font-weight-medium"}},
        "semibold": {"$value": 600, "$type": "fontWeight", "$extensions": {"source": "Measured css-var --font-weight-semibold"}},
        "bold": {"$value": 700, "$type": "fontWeight", "$extensions": {"source": "Measured css-var --font-weight-bold"}},
    },
    "radius": {
        "sm": dim_from_var("--radius-sm"),
        "md": dim_from_var("--radius-md"),
        "lg": dim_from_var("--radius-lg"),
        "xl": dim_from_var("--radius-xl"),
        "2xl": dim_from_var("--radius-2xl"),
        "3xl": dim_from_var("--radius-3xl"),
        "button": measured_dim("28px", "Derived from the primary button height 56px: the control is a full pill (computed radius exceeded the height). Stored as half the height so DESIGN.md can read a px length."),
        "field": measured_dim("16px", "demo page text field border-radius, 2026-11-21"),
        "loginButton": measured_dim("8px", "app.sharewillow.com/login Login button, wall only, not submitted"),
    },
    "space": {
        "1": {"$value": "4px", "$type": "dimension", "$extensions": {"source": "Derived --spacing .25rem at 16px root = 4px. The scale is 4px steps."}},
        "2": {"$value": "8px", "$type": "dimension", "$extensions": {"source": "Derived 2 * --spacing"}},
        "3": {"$value": "12px", "$type": "dimension", "$extensions": {"source": "Derived 3 * --spacing"}},
        "4": {"$value": "16px", "$type": "dimension", "$extensions": {"source": "Derived 4 * --spacing"}},
        "6": {"$value": "24px", "$type": "dimension", "$extensions": {"source": "Derived 6 * --spacing"}},
        "8": {"$value": "32px", "$type": "dimension", "$extensions": {"source": "Derived 8 * --spacing"}},
    },
    "motion": {
        "easeOut": ease("--ease-out"),
        "easeInOut": ease("--ease-in-out"),
        "easeOutQuart": ease("--ease-out-quart"),
    },
    "size": {
        "buttonHeight": measured_dim("56px", "primary Book a demo computed height, homepage 1440, 2026-11-21"),
        "fieldHeight": measured_dim("48px", "demo page text field computed height"),
        "loginButtonHeight": measured_dim("44px", "login wall Login button computed height"),
        "navLink": measured_dim("14px", "header Pricing link font-size"),
    },
}

LIGHT = {
    "background": {
        "page": {"$value": "{core.palette.ivory}", "$type": "color", "$extensions": {"source": "Measured --color-bg alias of ivory"}},
        "surface": {"$value": "{core.palette.paper}", "$type": "color", "$extensions": {"source": "Measured --color-surface"}},
        "surface2": {"$value": "{core.palette.surface2}", "$type": "color", "$extensions": {"source": "Measured --color-surface-2"}},
        "hero": {"$value": "{core.palette.heroBg}", "$type": "color", "$extensions": {"source": "Measured --color-hero-bg, dark section inside the light page"}},
        "heroSurface": {"$value": "{core.palette.heroSurface}", "$type": "color", "$extensions": {"source": "Measured --color-hero-surface"}},
        "scrim": {"$value": "Not captured", "$type": "color", "$extensions": {"source": "Not captured. No scrim token declared. Menus open without a measured overlay colour."}},
    },
    "text": {
        "primary": {"$value": "{core.palette.espresso}", "$type": "color", "$extensions": {"source": "Measured --color-ink"}},
        "muted": {"$value": "{core.palette.inkMuted}", "$type": "color", "$extensions": {"source": "Measured --color-ink-muted"}},
        "subtle": {"$value": "{core.palette.inkSubtle}", "$type": "color", "$extensions": {"source": "Measured --color-ink-subtle"}},
        "onAccent": {"$value": "{core.palette.espresso}", "$type": "color", "$extensions": {"source": "Measured --color-accent-ink"}},
        "onButton": {"$value": "{core.palette.heroInkOnButton}", "$type": "color", "$extensions": {"source": "Measured primary button text"}},
        "hero": {"$value": "{core.palette.heroInk}", "$type": "color", "$extensions": {"source": "Measured --color-hero-ink"}},
        "heroMuted": {"$value": "{core.palette.heroInkMuted}", "$type": "color", "$extensions": {"source": "Measured --color-hero-ink-muted"}},
        "disabled": {"$value": "Not captured", "$type": "color", "$extensions": {"source": "Not captured. No disabled text colour was reached on a public control."}},
        "link": {"$value": "{core.palette.espresso}", "$type": "color", "$extensions": {"source": "Measured quiet link 'See the app' computed color rgb(24, 6, 0)"}},
    },
    "border": {
        "default": {"$value": "{core.palette.border}", "$type": "color", "$extensions": {"source": "Measured --color-border"}},
        "strong": {"$value": "{core.palette.borderStrong}", "$type": "color", "$extensions": {"source": "Measured --color-border-strong"}},
        "focus": {"$value": "Not captured", "$type": "color", "$extensions": {"source": "Not captured. Keyboard focus on the primary button did not change the computed border or outline in this pass."}},
    },
    "accent": {
        "default": {"$value": "{core.palette.lemon}", "$type": "color", "$extensions": {"source": "Measured --color-accent"}},
        "deep": {"$value": "{core.palette.lemonDeep}", "$type": "color", "$extensions": {"source": "Measured --color-lemon-deep"}},
        "hover": {"$value": "Not captured", "$type": "color", "$extensions": {"source": "Not captured as a lemon hover step. The primary button hover shifts espresso to rgb(43, 26, 16), recorded as core.palette.buttonHover."}},
        "pressed": {"$value": "{core.palette.buttonHover}", "$type": "color", "$extensions": {"source": "Measured primary button :active:hover via CDP, same fill as hover in this pass"}},
    },
    "status": {
        "success": {"$value": "{core.palette.lime}", "$type": "color", "$extensions": {"source": "Measured --color-lime. Used in marketing demo charts. Not a full status set."}},
        "warning": {"$value": "{core.palette.peach}", "$type": "color", "$extensions": {"source": "Measured --color-peach. Role inferred from the palette name only; no warning component was captured."}},
        "danger": {"$value": "{core.palette.rose}", "$type": "color", "$extensions": {"source": "Measured --color-rose. Role inferred from the palette name only."}},
        "info": {"$value": "{core.palette.sky}", "$type": "color", "$extensions": {"source": "Measured --color-sky. Role inferred from the palette name only."}},
    },
    "component": {
        "button": {
            "background": {"$value": "{core.palette.espresso}", "$type": "color", "$extensions": {"source": "Measured primary button background"}},
            "text": {"$value": "{core.palette.heroInkOnButton}", "$type": "color", "$extensions": {"source": "Measured primary button text"}},
            "radius": {"$value": "{core.radius.button}", "$type": "dimension", "$extensions": {"source": "Alias of measured pill radius"}},
            "height": {"$value": "{core.size.buttonHeight}", "$type": "dimension", "$extensions": {"source": "Alias of measured button height"}},
        },
        "field": {
            "background": {"$value": "{core.palette.paper}", "$type": "color", "$extensions": {"source": "Measured demo field background #fff"}},
            "text": {"$value": "{core.palette.espresso}", "$type": "color", "$extensions": {"source": "Measured demo field text color"}},
            "radius": {"$value": "{core.radius.field}", "$type": "dimension", "$extensions": {"source": "Alias of measured field radius"}},
            "height": {"$value": "{core.size.fieldHeight}", "$type": "dimension", "$extensions": {"source": "Alias of measured field height"}},
        },
    },
}

# Drop tokens whose value is the string "Not captured" from the colour type
# check by storing them as a description-only gap is not valid DTCG. Remove
# those leaves and record them in raw/gaps.json instead.
GAPS = []

def strip_gaps(node, path=""):
    if isinstance(node, dict) and "$value" in node and node["$value"] == "Not captured":
        GAPS.append({"path": path, "source": node["$extensions"]["source"]})
        return None
    if isinstance(node, dict) and "$value" not in node:
        out = {}
        for k, v in node.items():
            child = strip_gaps(v, f"{path}.{k}" if path else k)
            if child is not None:
                out[k] = child
        return out
    return node

LIGHT = strip_gaps(LIGHT)
(RAW / "gaps.json").write_text(json.dumps(GAPS, indent=2) + "\n")

doc = {
    "core": CORE,
    "light": LIGHT,
    "$themes": [{"id": "light", "name": "Light", "selectedTokenSets": {"core": "enabled", "light": "enabled"}}],
}

# Refuse a colour token that is not a colour or an alias.
def check(node, path=""):
    if isinstance(node, dict) and "$value" in node:
        val, ty = node["$value"], node["$type"]
        if isinstance(val, str) and val.startswith("{"):
            return
        if ty == "color":
            norm_color(val)
        if ty == "dimension" and not re.fullmatch(r"-?\d+(\.\d+)?(px|rem)", str(val)):
            raise SystemExit(f"{path} bad dimension {val}")
        if "$extensions" not in node or "source" not in node["$extensions"]:
            raise SystemExit(f"{path} missing source")
        return
    if isinstance(node, dict):
        for k, v in node.items():
            if k.startswith("$"):
                continue
            check(v, f"{path}.{k}")

check(doc)
(HERE / "tokens.json").write_text(json.dumps(doc, indent=2) + "\n")
print("wrote tokens.json", "gaps", len(GAPS))
