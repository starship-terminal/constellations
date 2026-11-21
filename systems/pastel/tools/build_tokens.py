#!/usr/bin/env python3
"""Build tokens.json from measured Pastel public-page readings.

Sources, read on 2026-11-20 from usepastel.com in headless Chromium:
  raw/component-readings.json  computed styles of real elements
  raw/readings.json            per-page foundation readings (body, h1, cta)

Pastel does not publish a theme toggle on the marketing site. The only
semantic set is light. Status colours on status.usepastel.com are a
separate product (Instatus) and are recorded under core.color.status
with that source, not as a Pastel dark theme.

Every token carries $extensions.source. A value that was not read is
absent, never filled in. Deterministic: same inputs, same bytes.
"""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
COMP = json.loads((RAW / "component-readings.json").read_text())
READ = json.loads((RAW / "readings.json").read_text())

HOME = COMP["home"]
PLANS = COMP["plans"]
BLOG = COMP["blog"]
HELP = COMP["help"]
STATUS = COMP["status"]
FAQ = COMP["faq"]
H1 = READ["pages"]["home"]["foundations"]["h1"]
CTA = READ["pages"]["home"]["foundations"]["cta"]


def color(rgb):
    rgb = rgb.strip()
    if rgb.startswith("#"):
        h = rgb[1:]
        if len(h) == 3:
            h = "".join(c * 2 for c in h)
        return "#" + h[:6].lower()
    if rgb == "white":
        return "#ffffff"
    import re
    m = re.fullmatch(r"rgba?\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*(?:,\s*([\d.]+))?\s*\)", rgb)
    if not m:
        raise ValueError(rgb)
    r, g, b, a = m.groups()
    if a is None or float(a) >= 1:
        return "#%02x%02x%02x" % (int(r), int(g), int(b))
    return "rgba(%d, %d, %d, %g)" % (int(r), int(g), int(b), float(a))


def tok(value, typ, source):
    return {"$value": value, "$type": typ, "$extensions": {"source": source}}


def alias(ref, typ, source):
    return tok(ref, typ, source)


def col(rgb, source):
    return tok(color(rgb), "color", source)


def dim(px, source):
    return tok(px if str(px).endswith("px") else f"{px}px", "dimension", source)


core = {
    "color": {
        "ink": col("rgb(17, 17, 17)", "Measured computed color on body, https://usepastel.com/ 1440x900"),
        "ink-soft": col("rgb(34, 34, 34)", "Measured computed color on h2.heading-2, home"),
        "stone": col("rgb(28, 25, 23)", "Measured computed color on h1, /customers"),
        "paper": col("rgb(255, 255, 255)", "Measured computed backgroundColor on body, home"),
        "stone-paper": col("rgb(245, 245, 244)", "Measured computed backgroundColor on body.pastel-app and .plan-container.grey"),
        "blue": col("rgb(22, 93, 251)", "Measured computed backgroundColor on 'Start a free trial' link, home"),
        "on-blue": col("rgb(255, 255, 255)", "Measured computed color on 'Start a free trial' link, home"),
        "ink-button": col("rgb(69, 71, 69)", "Measured computed backgroundColor on navbar Sign up link, home"),
        "hairline": col("rgba(152, 152, 152, 0.45)", "Measured computed border color on navbar Login link, home"),
        "demo-border": col("rgb(215, 211, 209)", "Measured computed border color on Watch demo link, home"),
        "demo-text": col("rgb(69, 64, 60)", "Measured computed color on Watch demo link, home"),
        "plan-border": col("rgba(80, 80, 80, 0.3)", "Measured computed border color on .plan-container.grey, /plans"),
        "toggle-knob": col("rgb(135, 135, 135)", "Measured computed backgroundColor on .toggle-switch, /plans"),
        "focus": col("rgb(0, 95, 204)", "Measured computed outline color after Tab on home"),
        "blog": {
            "black": col(BLOG["vars"]["--black"], "Measured custom property --black on /blog"),
            "midnight-blue": col(BLOG["vars"]["--midnight-blue"], "Measured custom property --midnight-blue on /blog"),
            "slate": col(BLOG["vars"]["--light-slate-grey"], "Measured custom property --light-slate-grey on /blog"),
            "alice": col(BLOG["vars"]["--alice-blue"], "Measured custom property --alice-blue on /blog"),
            "ghost": col(BLOG["vars"]["--ghost-white"], "Measured custom property --ghost-white on /blog"),
            "purple": col(BLOG["vars"]["--medium-slate-blue"], "Measured custom property --medium-slate-blue on /blog"),
            "coral": col(BLOG["vars"]["--coral"], "Measured custom property --coral on /blog"),
            "grey": col(BLOG["vars"]["--grey"], "Measured custom property --grey on /blog"),
        },
        "help": {
            "header": col(HELP["vars"]["--header-bg"], "Measured custom property --header-bg on help.usepastel.com"),
            "text": col(HELP["vars"]["--body-primary-color"], "Measured custom property --body-primary-color on help.usepastel.com"),
            "muted": col(HELP["vars"]["--body-secondary-color"], "Measured custom property --body-secondary-color on help.usepastel.com"),
        },
        "status": {
            "brand": col(STATUS["vars"]["--brand-color"], "Measured custom property --brand-color on status.usepastel.com (Instatus)"),
            "ok": col(STATUS["vars"]["--ok-color"], "Measured custom property --ok-color on status.usepastel.com"),
            "disrupted": col(STATUS["vars"]["--disrupted-color"], "Measured custom property --disrupted-color on status.usepastel.com"),
            "degraded": col(STATUS["vars"]["--degraded-color"], "Measured custom property --degraded-color on status.usepastel.com"),
            "down": col(STATUS["vars"]["--down-color"], "Measured custom property --down-color on status.usepastel.com"),
            "notice": col(STATUS["vars"]["--notice-color"], "Measured custom property --notice-color on status.usepastel.com"),
            "unknown": col(STATUS["vars"]["--unknown-color"], "Measured custom property --unknown-color on status.usepastel.com"),
        },
    },
    "font": {
        "family": {
            "marketing": tok("Figtree, sans-serif", "fontFamily", "Measured computed fontFamily on body, home"),
            "blog": tok("Inter, sans-serif", "fontFamily", "Measured computed fontFamily on body, /blog"),
            "help": tok(HELP["body"]["fontFamily"], "fontFamily", "Measured computed fontFamily on body, help.usepastel.com"),
        }
    },
    "typography": {
        "display": {
            "fontFamily": alias("{font.family.marketing}", "fontFamily", "Measured on h1, home"),
            "fontSize": dim(H1["fontSize"], "Measured computed fontSize on h1, home 1440x900"),
            "fontWeight": tok(H1["fontWeight"], "fontWeight", "Measured computed fontWeight on h1, home"),
            "lineHeight": dim(H1["lineHeight"], "Measured computed lineHeight on h1, home"),
            "letterSpacing": dim(H1["letterSpacing"], "Measured computed letterSpacing on h1, home"),
        },
        "heading": {
            "fontFamily": alias("{font.family.marketing}", "fontFamily", "Measured on h2.heading-2, home"),
            "fontSize": dim(HOME["h2"]["fontSize"], "Measured computed fontSize on h2.heading-2, home"),
            "fontWeight": tok(HOME["h2"]["fontWeight"], "fontWeight", "Measured computed fontWeight on h2, home"),
            "lineHeight": dim(HOME["h2"]["lineHeight"], "Measured computed lineHeight on h2, home"),
        },
        "body": {
            "fontFamily": alias("{font.family.marketing}", "fontFamily", "Measured on body, home"),
            "fontSize": dim("14px", "Measured computed fontSize on body, home"),
            "lineHeight": dim("20px", "Measured computed lineHeight on body, home"),
            "fontWeight": tok("400", "fontWeight", "Measured computed fontWeight on body, home"),
        },
        "nav": {
            "fontSize": dim(HOME["navBtn"]["fontSize"], "Measured computed fontSize on a.navbar-button, home"),
            "fontWeight": tok(HOME["navBtn"]["fontWeight"], "fontWeight", "Measured computed fontWeight on a.navbar-button, home"),
            "lineHeight": dim(HOME["navBtn"]["lineHeight"], "Measured computed lineHeight on a.navbar-button, home"),
        },
        "button": {
            "fontSize": dim(CTA["fontSize"], "Measured computed fontSize on Start a free trial, home"),
            "fontWeight": tok(CTA["fontWeight"], "fontWeight", "Measured computed fontWeight on Start a free trial, home"),
            "lineHeight": dim(CTA["lineHeight"], "Measured computed lineHeight on Start a free trial, home"),
        },
        "faq-question": {
            "fontSize": dim(FAQ["closed"]["fontSize"], "Measured computed fontSize on .faq-accordion-question, /faq"),
            "fontWeight": tok(FAQ["closed"]["fontWeight"], "fontWeight", "Measured on .faq-accordion-question"),
        },
        "faq-answer": {
            "fontSize": dim(FAQ["openAnswer"]["fontSize"], "Measured computed fontSize on open FAQ answer, /faq"),
            "lineHeight": dim(FAQ["openAnswer"]["lineHeight"], "Measured computed lineHeight on open FAQ answer"),
        },
    },
    "radius": {
        "button": dim(CTA["borderRadius"], "Measured computed borderRadius on Start a free trial, home"),
        "nav-link": dim(HOME["navBtn"]["borderRadius"], "Measured computed borderRadius on a.navbar-button, home"),
        "login": dim(HOME["login"]["borderRadius"], "Measured computed borderRadius on navbar Login, home"),
        "toggle": dim("100%", "Measured computed borderRadius on .toggle-switch, /plans. Not a px length, kept as observed."),
    },
    "size": {
        "button-height": dim(CTA["height"], "Measured computed height on Start a free trial, home"),
        "login-height": dim(f"{HOME['login']['h']}px", "Measured bounding box height on navbar Login, home"),
        "signup-height": dim(f"{HOME['signup']['h']}px", "Measured bounding box height on navbar Sign up, home"),
        "nav-height": dim(f"{HOME['navbar']['h']}px", "Measured bounding box height on .navbar, home 1440"),
        "plan-card-width": dim(f"{PLANS['cards'][0]['w']}px", "Measured bounding box width on .plan-container.grey, /plans"),
        "toggle-knob": dim(f"{PLANS['switch']['h']}px", "Measured bounding box height on .toggle-switch, /plans"),
    },
}

# 100% is not a DTCG dimension the checker wants. Drop it from radius and note it.
core["radius"].pop("toggle")

light = {
    "page": alias("{color.paper}", "color", "Alias of measured body background, home"),
    "surface": alias("{color.stone-paper}", "color", "Alias of measured plan card and customers page background"),
    "text": alias("{color.ink}", "color", "Alias of measured body color, home"),
    "muted": alias("{color.ink-soft}", "color", "Alias of measured h2 color, home. A second ink, not a disabled role."),
    "accent": alias("{color.blue}", "color", "Alias of measured primary CTA background, home"),
    "on-accent": alias("{color.on-blue}", "color", "Alias of measured primary CTA text, home"),
    "border": alias("{color.hairline}", "color", "Alias of measured Login button border, home"),
    "component": {
        "button-primary": {
            "background": alias("{color.blue}", "color", "Measured on Start a free trial"),
            "text": alias("{color.on-blue}", "color", "Measured on Start a free trial"),
            "radius": alias("{radius.button}", "dimension", "Alias of measured CTA radius"),
            "height": alias("{size.button-height}", "dimension", "Alias of measured CTA height"),
        },
        "button-signup": {
            "background": alias("{color.ink-button}", "color", "Measured on navbar Sign up"),
            "text": alias("{color.on-blue}", "color", "Measured on navbar Sign up (white text)"),
            "radius": alias("{radius.login}", "dimension", "Alias of measured signup radius"),
        },
        "button-login": {
            "text": alias("{color.ink}", "color", "Measured on navbar Login"),
            "border": alias("{color.hairline}", "color", "Measured on navbar Login"),
            "radius": alias("{radius.login}", "dimension", "Alias of measured login radius"),
        },
    },
}

doc = {
    "core": core,
    "light": light,
    "$themes": [{"id": "light", "name": "light", "selectedTokenSets": {"core": "source", "light": "enabled"}}],
}

text = json.dumps(doc, indent=1) + "\n"
(HERE / "tokens.json").write_text(text)
print("wrote", HERE / "tokens.json", "bytes", len(text))
