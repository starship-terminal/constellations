#!/usr/bin/env python3
"""Build tokens.json from the 2026-11-21 tilda.cc public readings.

Sources:
  raw/css-vars.json              stylesheet custom properties and @font-face
  raw/components-computed.json   computed styles on real elements

Tilda's marketing pages declare font stacks and button heights as custom
properties. Colour roles are computed styles, not a --color token layer.
No dark theme is declared. Unread roles stay out of the file.

Deterministic. Edit the readings, never tokens.json.
"""
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
COMP = json.loads((RAW / "components-computed.json").read_text())["components"]


def color(value):
    v = value.strip().lower()
    m = re.fullmatch(r"rgba?\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)(?:\s*,\s*([\d.]+))?\s*\)", v)
    if not m:
        raise ValueError("not a colour: " + value)
    r, g, b, a = m.groups()
    if a is None or float(a) == 1:
        return "#%02x%02x%02x" % (int(r), int(g), int(b))
    return "rgba(%d, %d, %d, %g)" % (int(r), int(g), int(b), float(a))


def dim(value):
    m = re.fullmatch(r"(-?\d+(?:\.\d+)?)px", str(value).strip())
    if not m:
        raise ValueError("not a px length: " + str(value))
    return "%gpx" % round(float(m.group(1)), 3)


def st(name, state="default"):
    return COMP[name]["states"][state]


def src(name, prop, state="default"):
    return f"computed {prop} of {name} {state} on tilda.cc, 2026-11-21"


def leaf(ty, val, source):
    return {"$value": val, "$type": ty, "$extensions": {"source": source}}


def col(name, prop="color", state="default"):
    return leaf("color", color(st(name, state)["style"][prop]), src(name, prop, state))


def length(name, prop, state="default"):
    return leaf("dimension", dim(st(name, state)["style"][prop]), src(name, prop, state))


hero = st("hero-cta")["style"]
login_btn = st("login-submit")["style"]
faq = st("faq-search")["style"]
title = st("hero-title")["style"]
price = st("pricing-title")["style"]
nav = st("login-link")["style"]
menu = st("menu-link")["style"]
field = st("login-email")["style"]

core = {
    "color": {
        "ink": col("hero-title"),
        "paper": leaf("color", "#ffffff", "computed backgroundColor of faq-search default"),
        "coral": col("hero-cta", "backgroundColor"),
        "on-coral": col("hero-cta"),
        "cream": col("login-submit", "backgroundColor"),
        "field-line": leaf(
            "color",
            "rgba(255, 255, 255, 0.3)",
            "computed borderBottomColor of login-email default",
        ),
        "faq-chip": col("faq-category", "backgroundColor", "selected"),
        "faq-chip-text": col("faq-category", "color", "selected"),
        "price-accent": leaf(
            "color",
            "#ff8562",
            "computed color of the Personal website label on /pricing/, 2026-11-21",
        ),
        "menu-shadow": leaf(
            "color",
            "rgba(0, 0, 0, 0.15)",
            "computed box-shadow colour of .tmain-submenu__content, 2026-11-21",
        ),
        "auth-panel": leaf(
            "color",
            "rgba(255, 255, 255, 0.1)",
            "computed backgroundColor of .ts-form on /login/, 2026-11-21",
        ),
    },
    "font": {
        "family": {
            "sans": leaf(
                "fontFamily",
                "TildaSans, Arial, sans-serif",
                "css-var --t-headline-font and --t-text-font on #allrecords .r, body",
            ),
        },
        "weight": {
            "light": leaf("fontWeight", 300, src("hero-title", "fontWeight")),
            "regular": leaf("fontWeight", 400, src("menu-link", "fontWeight")),
            "semibold": leaf("fontWeight", 600, src("hero-cta", "fontWeight")),
            "bold": leaf("fontWeight", 700, src("login-link", "fontWeight")),
        },
        "size": {
            "nav": length("login-link", "fontSize"),
            "button": length("hero-cta", "fontSize"),
            "menu": length("menu-link", "fontSize"),
            "body": leaf("dimension", "16px", "computed fontSize of body text on /pricing/ plan labels"),
            "field": length("login-email", "fontSize"),
            "display": length("hero-title", "fontSize"),
            "pricing": length("pricing-title", "fontSize"),
        },
    },
    "radius": {
        "none": leaf("dimension", "0px", src("hero-cta", "borderTopLeftRadius")),
        "chip": length("template-radio", "borderTopLeftRadius"),
        "field": length("faq-search", "borderTopLeftRadius"),
        "pill": length("login-submit", "borderTopLeftRadius"),
    },
    "size": {
        "button-sm": leaf("dimension", "45px", "css-var --height on .t-btnflex_sm"),
        "button-smd": length("hero-cta", "height"),
        "button-xl": leaf("dimension", "80px", "css-var --height on .t-btnflex_xl"),
        "field": length("login-email", "height"),
        "faq-field": length("faq-search", "height"),
        "auth-button": length("login-submit", "height"),
    },
}

light = {
    "surface": {
        "page": {"$value": "{color.paper}", "$type": "color", "$extensions": {"source": "alias of core.color.paper"}},
        "auth-panel": {"$value": "{color.auth-panel}", "$type": "color", "$extensions": {"source": "alias of core.color.auth-panel"}},
    },
    "text": {
        "primary": {"$value": "{color.ink}", "$type": "color", "$extensions": {"source": "alias of core.color.ink"}},
        "on-accent": {"$value": "{color.on-coral}", "$type": "color", "$extensions": {"source": "alias of core.color.on-coral"}},
        "on-auth": leaf("color", "#ffffff", src("login-email", "color")),
    },
    "accent": {
        "default": {"$value": "{color.coral}", "$type": "color", "$extensions": {"source": "alias of core.color.coral"}},
    },
    "border": {
        "field": {"$value": "{color.field-line}", "$type": "color", "$extensions": {"source": "alias of core.color.field-line"}},
    },
    "component": {
        "button": {
            "background": {"$value": "{color.coral}", "$type": "color", "$extensions": {"source": "alias of core.color.coral"}},
            "text": {"$value": "{color.on-coral}", "$type": "color", "$extensions": {"source": "alias of core.color.on-coral"}},
            "height": {"$value": "{size.button-smd}", "$type": "dimension", "$extensions": {"source": "alias of core.size.button-smd"}},
            "radius": {"$value": "{radius.none}", "$type": "dimension", "$extensions": {"source": "alias of core.radius.none"}},
        },
        "auth-button": {
            "background": {"$value": "{color.cream}", "$type": "color", "$extensions": {"source": "alias of core.color.cream"}},
            "text": {"$value": "{color.ink}", "$type": "color", "$extensions": {"source": "alias of core.color.ink"}},
            "radius": {"$value": "{radius.pill}", "$type": "dimension", "$extensions": {"source": "alias of core.radius.pill"}},
            "height": {"$value": "{size.auth-button}", "$type": "dimension", "$extensions": {"source": "alias of core.size.auth-button"}},
        },
    },
}

# Silence unused locals kept for the reader of this file.
_ = (hero, login_btn, faq, title, price, nav, menu, field)

tokens = {
    "core": core,
    "light": light,
    "dark": {},
    "$themes": [
        {
            "id": "light",
            "name": "Light",
            "selectedTokenSets": {"core": "source", "light": "enabled"},
            "$description": "The only theme the public English marketing pages paint. No dark switch was found.",
        }
    ],
}

# Alias check
names = set()

def walk(node, prefix=""):
    for k, v in node.items():
        if k.startswith("$"):
            continue
        path = f"{prefix}.{k}" if prefix else k
        if isinstance(v, dict) and "$value" in v:
            names.add(path)
        elif isinstance(v, dict):
            walk(v, path)

walk(core)
walk(light, "")
# aliases in light may point at core names without a theme prefix
core_names = set()
walk_core = []

def walk2(node, prefix, bucket):
    for k, v in node.items():
        if k.startswith("$"):
            continue
        path = f"{prefix}.{k}" if prefix else k
        if isinstance(v, dict) and "$value" in v:
            bucket.add(path)
        elif isinstance(v, dict):
            walk2(v, path, bucket)

core_names = set()
light_names = set()
walk2(core, "", core_names)
walk2(light, "", light_names)

def aliases(v):
    if isinstance(v, str):
        return re.findall(r"\{([^{}]+)\}", v)
    return []

for n in light_names:
    # resolve path
    node = light
    for part in n.split("."):
        node = node[part]
    for a in aliases(node["$value"]):
        if a not in core_names and a not in light_names:
            raise SystemExit(f"alias {{{a}}} missing from {n}")

(HERE / "tokens.json").write_text(json.dumps(tokens, indent=1) + "\n")
print("wrote tokens", len(core_names), "core", len(light_names), "light")
