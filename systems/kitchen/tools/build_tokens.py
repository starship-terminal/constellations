#!/usr/bin/env python3
"""Build tokens.json from Kitchen.co computed-style readings.

Kitchen.co is a public marketing site. It declares almost no custom properties
(only --about, --dark, --white in main.css). Every colour, size and radius
here was read from a computed style on a real element on 2026-11-18.

One painted theme. The dark set stays empty.
"""
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
C = json.loads((RAW / "components-computed.json").read_text())["components"]

sys.path.insert(0, str(HERE / "tools"))


def src(where):
    return {"source": f"Measured computed style, {where}, kitchen.co 2026-11-18"}


def color(value, where):
    return {"$type": "color", "$value": value, "$extensions": src(where)}


def dim(value, where):
    return {"$type": "dimension", "$value": value, "$extensions": src(where)}


def font_family(value, where):
    return {"$type": "fontFamily", "$value": value, "$extensions": src(where)}


def weight(value, where):
    return {"$type": "fontWeight", "$value": int(value), "$extensions": src(where)}


def st(key, state="default"):
    node = C[key]["states"][state]
    if "style" not in node:
        raise KeyError(key)
    return node["style"]


def rect(key, state="default"):
    return C[key]["states"][state]["rect"]


def rgb_hex(c):
    c = (c or "").strip()
    m = re.fullmatch(r"rgba?\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)(?:\s*,\s*([\d.]+))?\s*\)", c)
    if not m:
        return c
    r, g, b, a = m.groups()
    if a is None or float(a) == 1:
        return "#%02x%02x%02x" % (int(r), int(g), int(b))
    return "rgba(%s, %s, %s, %g)" % (r, g, b, float(a))


def px(v):
    m = re.fullmatch(r"(-?\d*\.?\d+)px", str(v).strip())
    if not m:
        return None
    return "%gpx" % round(float(m.group(1)), 2)


def fam(v):
    return (v or "").split(",")[0].strip().strip('"')


promo = st("promo-bar")
ink_btn = st("nav-try")
outline = st("nav-login")
coral = st("cta-coral")
hero = st("hero-title")
body = st("hero-body")
nav = st("nav-link")
plan = st("plan-card")
faq = st("faq-row")
field = st("search-field")
footer = st("footer")

core = {
    "font": {
        "family": {
            "sans": font_family(f'"{fam(hero["fontFamily"])}", "Helvetica Neue", Arial, sans-serif', "h1.hero__title font-family"),
        },
        "weight": {
            "regular": weight(400, "body"),
            "medium": weight(500, "Graphik Medium is declared in @font-face; UI buttons use 700"),
            "bold": weight(700, "h1.hero__title and a.btn"),
            "black": weight(900, "Graphik Black is declared in @font-face"),
        },
        "size": {
            "nav": dim(px(nav["fontSize"]), "nav.nav a"),
            "button-small": dim(px(ink_btn["fontSize"]), "a.btn.btn--small"),
            "body": dim(px(body["fontSize"]), ".hero__entry p"),
            "button": dim(px(coral["fontSize"]), "a.btn coral"),
            "faq": dim(px(faq["fontSize"]), "button.accordion__head"),
            "hero": dim(px(hero["fontSize"]), "h1.hero__title"),
        },
    },
    "radius": {
        "button": dim(px(coral["borderTopLeftRadius"]), "a.btn border-radius"),
        "control": dim("5px", "a.btn and form controls share 5px"),
    },
    "space": {
        "button-pad-y": dim(px(coral["paddingTop"]), "a.btn padding-top"),
        "button-pad-x": dim(px(coral["paddingRight"]), "a.btn padding-right"),
        "small-pad-y": dim(px(ink_btn["paddingTop"]), "a.btn.btn--small padding-top"),
        "small-pad-x": dim(px(ink_btn["paddingRight"]), "a.btn.btn--small padding-right"),
    },
    "size": {
        "promo-bar": dim(px(str(rect("promo-bar")["h"]) + "px") or "56px", "a.bar height"),
        "button-small": dim(px(str(rect("nav-try")["h"]) + "px") or "44px", "header Try it FREE height"),
        "button": dim(px(str(rect("cta-coral")["h"]) + "px") or "52px", "coral CTA height"),
        "shell": dim("1280px", ".shell content width on the home hero"),
    },
}

light = {
    "background": {
        "page": color("#ffffff", "body background-color rgb(255, 255, 255)"),
        "promo": color(rgb_hex(promo["backgroundColor"]), "a.bar"),
        "sand": color("#f8f6f4", "main.css sand field, the recurring warm surface"),
        "footer": color(rgb_hex(footer["backgroundColor"]), "footer.footer"),
    },
    "text": {
        "primary": color(rgb_hex(hero["color"]), "h1.hero__title"),
        "secondary": color("#707070", "main.css muted grey"),
        "on-ink": color(rgb_hex(ink_btn["color"]), "a.btn.btn--dark"),
        "on-coral": color(rgb_hex(coral["color"]), "a.btn coral"),
        "promo-gold": color("#ffdc4d", "promo bar strong, main.css"),
        "link": color("#0000ee", "a.logo computed color, the UA link blue on the wordmark"),
    },
    "action": {
        "ink": color(rgb_hex(ink_btn["backgroundColor"]), "a.btn.btn--dark"),
        "coral": color(rgb_hex(coral["backgroundColor"]), "a.btn coral Get Started"),
        "outline": color(rgb_hex(outline["borderTopColor"]), "a.btn.is-outline border"),
    },
    "border": {
        "stroke": color("#e5e5e5", "main.css hairline"),
        "field": color("#dcdcdc", "main.css field border"),
        "strong": color(rgb_hex(outline["borderTopColor"]), "a.btn.is-outline"),
    },
    "component": {
        "button-radius": dim(px(coral["borderTopLeftRadius"]), "a.btn"),
        "button-height": dim("52px", "a.btn"),
        "button-small-height": dim("44px", "a.btn.btn--small"),
        "plan-card-bg": color(rgb_hex(plan["backgroundColor"]), ".plan"),
    },
}

# Alias component colours that match semantic roles.
if light["component"]["plan-card-bg"]["$value"] in ("rgba(0, 0, 0, 0)", "transparent"):
    light["component"]["plan-card-bg"] = {
        "$type": "color",
        "$value": "{background.page}",
        "$extensions": src(".plan background is transparent; the page shows through"),
    }

doc = {
    "$description": "Kitchen.co public marketing surface, measured 2026-11-18. One theme.",
    "core": core,
    "light": light,
    "dark": {},
    "$themes": [
        {"name": "light", "selectedTokenSets": {"core": "source", "light": "enabled"}},
    ],
}

motion_path = RAW / "motion.json"
if motion_path.exists():
    from motion import build as motion_build
    group, _skipped = motion_build(json.loads(motion_path.read_text()))
    if group:
        core["motion"] = group

(HERE / "tokens.json").write_text(json.dumps(doc, indent=1) + "\n")
print("tokens.json", "light colours", sum(1 for g in light.values() for v in g.values() if v.get("$type") == "color"))
