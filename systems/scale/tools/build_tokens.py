#!/usr/bin/env python3
"""Build tokens.json from Scale's raw readings.

Sources, read from scale.com on 2026-11-21:
  raw/css-vars.json            custom properties parsed from live stylesheets,
                               plus computed styles on home and demo
  raw/components-computed.json computed styles of public controls

Marketing pages paint one light theme. A dark semantic set is declared on
`[data-theme="dark"] body` in the same bundle and is recorded as declared,
not as a live marketing theme. Docs (scale.com/docs) paints a separate
`.dark` shell; its page colour is a computed reading, not this semantic set.

Every token carries $extensions.source. Unread values are omitted, never filled.
"""
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
V = json.loads((RAW / "css-vars.json").read_text())
C = json.loads((RAW / "components-computed.json").read_text())

DECLS = V["decls"]


def decl(name, selector_has):
    hits = [d for d in DECLS if d["name"] == name and selector_has in (d.get("selector") or "")]
    if not hits:
        raise KeyError(f"no declaration {name} on {selector_has}")
    return hits[0]["value"]


def src_var(name, selector_has):
    return f"Measured: custom property {name} on `{selector_has}`, raw/css-vars.json, scale.com 2026-11-21"


def src_computed(component, state):
    return (
        f"Measured: computed style of {component} {state}, "
        "raw/components-computed.json, scale.com 2026-11-21, viewport 1440x900"
    )


def color(value, source):
    return {"$type": "color", "$value": value, "$extensions": {"source": source}}


def dim(value, source):
    return {"$type": "dimension", "$value": value, "$extensions": {"source": source}}


def font(value, source):
    return {"$type": "fontFamily", "$value": value, "$extensions": {"source": source}}


def weight(value, source):
    return {"$type": "fontWeight", "$value": value, "$extensions": {"source": source}}


def num(value, source):
    return {"$type": "number", "$value": value, "$extensions": {"source": source}}


def duration(value, source):
    return {"$type": "duration", "$value": value, "$extensions": {"source": source}}


def bezier(value, source):
    return {"$type": "cubicBezier", "$value": value, "$extensions": {"source": source}}


def hsl_triplet(raw):
    """`240 10% 3.9%` as authored on [data-theme=dark] body. Keep the authored form."""
    parts = raw.split()
    if len(parts) != 3 or not parts[1].endswith("%"):
        raise ValueError(f"not an HSL triplet: {raw!r}")
    return f"hsl({parts[0]} {parts[1]} {parts[2]})"


def rgb_to_hex(value):
    m = re.fullmatch(r"rgba?\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)(?:\s*,\s*([\d.]+))?\s*\)", value.strip())
    if not m:
        return value
    r, g, b, a = m.groups()
    if a is None or float(a) == 1:
        return "#%02x%02x%02x" % (int(r), int(g), int(b))
    return f"rgba({r}, {g}, {b}, {a})"


def comp(component, state, prop):
    node = C["components"][component][state]
    if node.get("missing"):
        raise KeyError(component + " " + state)
    return rgb_to_hex(node[prop]) if prop in ("color", "backgroundColor", "borderTopColor") else node[prop]


LIGHT_SEL = '[data-theme="light"] body'
DARK_SEL = '[data-theme="dark"] body'
ROOT = ":root, :host"

nav_light = {
    "background": color(decl("--nav-background", LIGHT_SEL), src_var("--nav-background", LIGHT_SEL)),
    "text": color(decl("--nav-text", LIGHT_SEL), src_var("--nav-text", LIGHT_SEL)),
    "dropdown": color(decl("--nav-dropdown-background", LIGHT_SEL), src_var("--nav-dropdown-background", LIGHT_SEL)),
    "panel": color(decl("--nav-panel-background", LIGHT_SEL), src_var("--nav-panel-background", LIGHT_SEL)),
    "card": color(decl("--nav-card-background", LIGHT_SEL), src_var("--nav-card-background", LIGHT_SEL)),
    "loginText": color(decl("--nav-login-cta-text", LIGHT_SEL), src_var("--nav-login-cta-text", LIGHT_SEL)),
    "loginBorder": color(decl("--nav-login-cta-border", LIGHT_SEL), src_var("--nav-login-cta-border", LIGHT_SEL)),
    "demoBg": color(decl("--nav-demo-desktop-cta-bg", LIGHT_SEL), src_var("--nav-demo-desktop-cta-bg", LIGHT_SEL)),
    "demoText": color(decl("--nav-demo-desktop-cta-text", LIGHT_SEL), src_var("--nav-demo-desktop-cta-text", LIGHT_SEL)),
    "shadow": color(decl("--nav-shadow", LIGHT_SEL), src_var("--nav-shadow", LIGHT_SEL)),
}
nav_dark = {
    "background": color(decl("--nav-background", DARK_SEL), src_var("--nav-background", DARK_SEL)),
    "text": color(decl("--nav-text", DARK_SEL), src_var("--nav-text", DARK_SEL)),
    "dropdown": color(decl("--nav-dropdown-background", DARK_SEL), src_var("--nav-dropdown-background", DARK_SEL)),
    "panel": color(decl("--nav-panel-background", DARK_SEL), src_var("--nav-panel-background", DARK_SEL)),
    "demoBg": color(decl("--nav-demo-desktop-cta-bg", DARK_SEL), src_var("--nav-demo-desktop-cta-bg", DARK_SEL)),
    "demoText": color(decl("--nav-demo-desktop-cta-text", DARK_SEL), src_var("--nav-demo-desktop-cta-text", DARK_SEL)),
}

dark_roles = {}
for token, var in {
    "page": "--background",
    "card": "--card",
    "text": "--foreground",
    "muted": "--muted",
    "mutedText": "--muted-foreground",
    "border": "--border",
    "accent": "--accent",
    "primary": "--primary",
    "primaryText": "--primary-foreground",
    "destructive": "--destructive",
    "ring": "--ring",
    "input": "--input",
    "popover": "--popover",
    "secondary": "--secondary",
}.items():
    dark_roles[token] = color(hsl_triplet(decl(var, DARK_SEL)), src_var(var, DARK_SEL) + ". Declared, not painted on the marketing pages captured.")

home_body = V["computed"]["home"]["body"]
demo_h1 = V["computed"]["demo"]["h1"]

core = {
    "fontFamily": {
        "sans": font(
            ["aeonik", "aeonik Fallback", "ui-sans-serif", "system-ui", "sans-serif"],
            "Measured: computed font-family on body, raw/css-vars.json computed.home.body, scale.com 2026-11-21. Aeonik is proprietary and is not committed.",
        ),
        "mono": font(
            ["mono", "mono Fallback", "ui-monospace"],
            "Measured: --font-mono resolved on :root, raw/css-vars.json resolved.home, scale.com 2026-11-21.",
        ),
    },
    "fontWeight": {
        "normal": weight(400, "Measured: --font-weight-normal resolved 400, raw/css-vars.json resolved.home"),
        "medium": weight(500, "Measured: --font-weight-medium resolved 500, raw/css-vars.json resolved.home"),
        "semibold": weight(600, "Measured: --font-weight-semibold resolved 600, raw/css-vars.json resolved.home"),
        "bold": weight(700, "Measured: --font-weight-bold resolved 700, raw/css-vars.json resolved.home"),
    },
    "typography": {
        "body": {
            "$type": "typography",
            "$value": {
                "fontFamily": "{fontFamily.sans}",
                "fontSize": "16px",
                "fontWeight": 400,
                "lineHeight": "24px",
            },
            "$extensions": {"source": "Measured: computed style on body, raw/css-vars.json computed.home.body"},
        },
        "display": {
            "$type": "typography",
            "$value": {
                "fontFamily": "{fontFamily.sans}",
                "fontSize": demo_h1["fontSize"],
                "fontWeight": int(demo_h1["fontWeight"]),
                "lineHeight": demo_h1["lineHeight"],
                "letterSpacing": demo_h1["letterSpacing"],
            },
            "$extensions": {"source": "Measured: computed style on demo h1, raw/css-vars.json computed.demo.h1"},
        },
        "nav": {
            "$type": "typography",
            "$value": {
                "fontFamily": "{fontFamily.sans}",
                "fontSize": comp("nav-link", "default", "fontSize"),
                "fontWeight": int(comp("nav-link", "default", "fontWeight")),
                "lineHeight": comp("nav-link", "default", "lineHeight"),
            },
            "$extensions": {"source": src_computed("nav-link", "default")},
        },
    },
    "radius": {
        "xs": dim(V["resolved"]["home"]["--radius-xs"], "Measured: --radius-xs resolved on :root, raw/css-vars.json resolved.home"),
        "sm": dim(V["resolved"]["home"]["--radius-sm"], "Measured: --radius-sm resolved on :root, raw/css-vars.json resolved.home"),
        "md": dim(V["resolved"]["home"]["--radius-md"], "Measured: --radius-md resolved on :root, raw/css-vars.json resolved.home"),
        "lg": dim(V["resolved"]["home"]["--radius-lg"], "Measured: --radius-lg resolved on :root, raw/css-vars.json resolved.home"),
        "xl": dim(V["resolved"]["home"]["--radius-xl"], "Measured: --radius-xl resolved on :root, raw/css-vars.json resolved.home"),
        "2xl": dim(V["resolved"]["home"]["--radius-2xl"], "Measured: --radius-2xl resolved on :root, raw/css-vars.json resolved.home"),
        "control": dim(comp("button-primary", "default", "borderRadius"), src_computed("button-primary", "default") + " borderRadius"),
        "field": dim(comp("text-field", "default", "borderRadius"), src_computed("text-field", "default") + " borderRadius"),
    },
    "spacing": {
        "base": dim("4px", "Derived: --spacing resolved .25rem on :root (raw/css-vars.json resolved.home) at the measured 16px root font size"),
        "2": dim("8px", "Derived: 2 steps of --spacing (.25rem) at 16px root"),
        "3": dim("12px", "Derived: 3 steps of --spacing"),
        "4": dim("16px", "Derived: 4 steps of --spacing, equal to the body font size"),
        "6": dim("24px", "Derived: 6 steps of --spacing, equal to the body line height"),
        "8": dim("32px", "Derived: 8 steps of --spacing"),
    },
    "motion": {
        "duration": duration("150ms", "Derived: --default-transition-duration resolved .15s, raw/css-vars.json resolved.home"),
        "ease": bezier([0.4, 0, 0.2, 1], "Measured: --default-transition-timing-function cubic-bezier(.4, 0, .2, 1), raw/css-vars.json resolved.home"),
    },
    "layout": {
        "headerHeight": dim("88px", "Measured: header bounding height on scale.com/ at 1440, raw/css-vars.json computed.home.header"),
        "controlHeight": dim(comp("button-primary", "default", "height"), src_computed("button-primary", "default") + " height"),
        "content7xl": dim("80rem", "Measured: --container-7xl resolved 80rem, raw/css-vars.json resolved.home"),
    },
}

light = {
    "page": color(rgb_to_hex(home_body["backgroundColor"]), "Measured: computed background-color on body, raw/css-vars.json computed.home.body, scale.com/ 2026-11-21"),
    "text": color(rgb_to_hex(home_body["color"]), "Measured: computed color on body, raw/css-vars.json computed.home.body"),
    "textSecondary": color(rgb_to_hex(demo_h1["color"]), "Measured: computed color on demo h1, raw/css-vars.json computed.demo.h1"),
    "surface": color("#f5f5f5", src_var("--nav-panel-background", LIGHT_SEL)),
    "border": color("#c7c7c7", src_var("--nav-login-cta-border", LIGHT_SEL)),
    "muted": color("#929292", src_var("--nav-login-cta-text", LIGHT_SEL)),
    "accent": color("#000000", src_var("--nav-demo-desktop-cta-bg", LIGHT_SEL) + ". The marketing primary action is black, not a hue."),
    "onAccent": color("#ffffff", src_computed("button-primary", "default") + " color"),
    "link": color("#006cff", "Derived: :root --primary is the triplet 0 108 255 (raw/css-vars.json), which is rgb(0, 108, 255). Docs use this as --color-primary. Marketing links were not separately measured."),
    "nav": nav_light,
    "component": {
        "button": {
            "primary": {
                "bg": color(comp("button-primary", "default", "backgroundColor"), src_computed("button-primary", "default")),
                "text": color(comp("button-primary", "default", "color"), src_computed("button-primary", "default")),
                "radius": dim(comp("button-primary", "default", "borderRadius"), src_computed("button-primary", "default")),
                "height": dim(comp("button-primary", "default", "height"), src_computed("button-primary", "default")),
                "fontSize": dim(comp("button-primary", "default", "fontSize"), src_computed("button-primary", "default")),
            },
            "secondary": {
                "text": color(comp("button-secondary", "default", "color"), src_computed("button-secondary", "default")),
                "radius": dim(comp("button-secondary", "default", "borderRadius"), src_computed("button-secondary", "default")),
            },
        },
        "field": {
            "bg": color(comp("text-field", "default", "backgroundColor"), src_computed("text-field", "default")),
            "text": color(comp("text-field", "default", "color"), src_computed("text-field", "default")),
            "radius": dim(comp("text-field", "default", "borderRadius"), src_computed("text-field", "default")),
            "fontSize": dim(comp("text-field", "default", "fontSize"), src_computed("text-field", "default")),
        },
    },
}

dark = {
    **dark_roles,
    "nav": nav_dark,
    "docsPage": color(
        "#090b10",
        "Measured: computed background-color on documentElement after choosing Dark in the docs theme menu, scale.com/docs 2026-11-21. This is the docs shell, not the marketing [data-theme=dark] set.",
    ),
}

tokens = {
    "$schema": "https://tr.designtokens.org/format/dtcg/2024-05",
    "core": core,
    "light": light,
    "dark": dark,
    "$themes": [
        {"id": "light", "name": "light", "selectedTokenSets": {"core": "enabled", "light": "enabled"}},
        {"id": "dark", "name": "dark", "selectedTokenSets": {"core": "enabled", "dark": "enabled"}},
    ],
    "$extensions": {
        "notTokenised": [
            "Marketing pages did not change under prefers-color-scheme: dark (raw/css-vars.json themeChecks). The dark set is the declared [data-theme=dark] body block, not a live marketing capture.",
            "Docs dark page colour (#090b10) does not match the declared --background hsl(240 10% 3.9%). They are separate shells.",
            "Hover and focus-visible on the header Get Started control did not change background or color in the computed reading. A painted hover shift was not captured.",
            "Pressed, disabled, loading, and error states were not captured. Forms were not submitted.",
            "Aeonik files are proprietary and are not in the package.",
        ]
    },
}

(HERE / "tokens.json").write_text(json.dumps(tokens, indent=1) + "\n")
print("wrote", HERE / "tokens.json")
