#!/usr/bin/env python3
"""Build tokens.json from systems/helloivy/raw/readings.json.

Every leaf is a computed style read on www.helloivy.co or the public login
wall at app.helloivy.co/login on 2026-11-21. Nothing was inferred from a
screenshot. A role the pages do not paint is omitted, not guessed.

Hello Ivy's marketing site is light only (html toggle-theme="light"). The
export has core and light. There is no dark set.
"""
import json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = json.loads((HERE / "raw" / "readings.json").read_text())
OUT = HERE / "tokens.json"

SRC = "Measured computed style, headless Chromium, 1440x900, 2026-11-21. raw/readings.json"


def color(rgb):
    m = re.fullmatch(r"rgba?\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*(?:,\s*([\d.]+)\s*)?\)", rgb.strip())
    if not m:
        raise ValueError(rgb)
    r, g, b, a = m.groups()
    if a is None or float(a) == 1:
        return "#%02x%02x%02x" % (int(r), int(g), int(b))
    return "rgba(%d, %d, %d, %g)" % (int(r), int(g), int(b), float(a))


def px(v):
    m = re.fullmatch(r"(-?\d*\.?\d+)px", str(v).strip())
    if not m:
        raise ValueError(v)
    f = float(m.group(1))
    return ("%g" % round(f, 2)) + "px"


def tok(ty, val, where):
    return {"$type": ty, "$value": val, "$extensions": {"source": f"{SRC}. {where}"}}


def col(rgb, where):
    return tok("color", color(rgb), where)


def dim(v, where):
    return tok("dimension", px(v), where)


h = RAW["home"]
login = RAW["login"]

core = {
  "color": {
    "paper": col(h["bodyBg"], "body backgroundColor on www.helloivy.co/"),
    "ink": col(h["bodyColor"], "body color on www.helloivy.co/"),
    "white": col(h["cta"]["color"], "Get Started label color (the painted p inside the pill)"),
    "ink-22": col(login["continueBtn"]["backgroundColor"], "login Continue backgroundColor"),
    "field": col(login["email"]["backgroundColor"], "login email input backgroundColor"),
    "field-border": col(login["password"]["borderTopColor"], "login password borderTopColor"),
    "field-border-strong": col(login["email"]["borderTopColor"], "login email borderTopColor (focused-looking hairline)"),
    "muted": col(login["googleBtn"]["color"], "Login with Google label color"),
    "on-accent": col(login["continueBtn"]["color"], "login Continue color"),
  },
  "font": {
    "family": {
      "display": tok("fontFamily", "Unbounded, sans-serif", "h1 fontFamily on www.helloivy.co/ (placeholder face dropped)"),
      "text": tok("fontFamily", "Inter, sans-serif", "nav link and intro fontFamily; login body fontFamily"),
    },
    "weight": {
      "regular": tok("fontWeight", 400, "intro fontWeight 400"),
      "medium": tok("fontWeight", 500, "h1 fontWeight 500"),
      "semibold": tok("fontWeight", 600, "nav link fontWeight 600"),
    },
    "size": {
      "nav": dim(h["navLink"]["fontSize"], "Features link fontSize"),
      "button": dim(h["cta"]["fontSize"], "Get Started label fontSize"),
      "body": dim(h["intro"]["fontSize"], "home intro paragraph fontSize"),
      "display": dim(h["h1"]["fontSize"], "home h1 fontSize"),
      "display-lg": dim(RAW["pricing"]["h1s"][0]["fontSize"], "pricing h1 fontSize"),
      "price": dim("28px", "pricing plan price span fontSize, raw/extra-styles.json"),
      "field": dim(login["email"]["fontSize"], "login email fontSize"),
      "login-button": dim(login["continueBtn"]["fontSize"], "login Continue fontSize"),
    },
    "lineHeight": {
      "nav": dim(h["navLink"]["lineHeight"], "Features link lineHeight"),
      "button": dim(h["cta"]["lineHeight"], "Get Started label lineHeight"),
      "body": dim(h["intro"]["lineHeight"], "home intro lineHeight"),
      "display": dim(h["h1"]["lineHeight"], "home h1 lineHeight"),
      "field": dim(login["email"]["lineHeight"], "login email lineHeight"),
    },
  },
  "radius": {
    "pill": dim(h["ctaBox"]["borderRadius"], "Get Started anchor borderRadius"),
    "control": dim(login["email"]["borderRadius"], "login email borderRadius"),
    "none": dim("0px", "pricing Try for Free anchor borderRadius is 0px"),
  },
  "space": {
    "6": dim("6px", "pricing CTA columnGap"),
    "10": dim(h["ctaBox"]["gap"], "Get Started gap"),
    "12": dim(login["email"]["paddingTop"], "login email paddingTop"),
    "15": dim(h["ctaBox"]["paddingTop"], "Get Started paddingTop"),
    "16": dim(login["continueBtn"]["paddingTop"], "login Continue paddingTop"),
    "20": dim(login["email"]["paddingLeft"], "login email paddingLeft"),
    "30": dim(h["ctaBox"]["paddingLeft"], "Get Started paddingLeft"),
    "48": dim("48px", "home content inset, h1 rect.x"),
  },
  "layout": {
    "header-cta-height": dim(h["ctaBox"]["height"], "Get Started height"),
    "login-field-height": dim(login["email"]["height"], "login email height"),
    "login-button-height": dim(login["continueBtn"]["height"], "login Continue height"),
    "login-field-width": dim(login["email"]["width"], "login email width at 1440"),
    "content-width": dim(h["h1"]["width"], "home h1 width at 1440"),
  },
  "border": {
    "hairline": dim(login["password"]["borderTopWidth"], "login password borderTopWidth"),
    "strong": dim(login["googleBtn"]["borderTopWidth"], "Login with Google borderTopWidth"),
  },
  "typography": {
    "display": tok("typography", {
      "fontFamily": "{font.family.display}",
      "fontSize": "{font.size.display}",
      "fontWeight": "{font.weight.medium}",
      "lineHeight": "{font.lineHeight.display}",
    }, "home h1"),
    "body": tok("typography", {
      "fontFamily": "{font.family.text}",
      "fontSize": "{font.size.body}",
      "fontWeight": "{font.weight.regular}",
      "lineHeight": "{font.lineHeight.body}",
    }, "home intro paragraph"),
    "nav": tok("typography", {
      "fontFamily": "{font.family.text}",
      "fontSize": "{font.size.nav}",
      "fontWeight": "{font.weight.semibold}",
      "lineHeight": "{font.lineHeight.nav}",
    }, "header Features link"),
    "button": tok("typography", {
      "fontFamily": "{font.family.text}",
      "fontSize": "{font.size.button}",
      "fontWeight": "{font.weight.semibold}",
      "lineHeight": "{font.lineHeight.button}",
    }, "Get Started label"),
  },
}

light = {
  "page": {"$value": "{color.paper}", "$type": "color", "$extensions": {"source": "alias of core.color.paper"}},
  "surface": {"$value": "{color.paper}", "$type": "color", "$extensions": {"source": "alias of core.color.paper. Raised cards were not a separate computed fill on the probed nodes."}},
  "text": {"$value": "{color.ink}", "$type": "color", "$extensions": {"source": "alias of core.color.ink"}},
  "muted": {"$value": "{color.muted}", "$type": "color", "$extensions": {"source": "alias of core.color.muted. This is the Google button label, not a marketing secondary text colour. Marketing secondary text was not isolated."}},
  "accent": {"$value": "{color.ink}", "$type": "color", "$extensions": {"source": "alias of core.color.ink. Primary pills paint black."}},
  "on-accent": {"$value": "{color.white}", "$type": "color", "$extensions": {"source": "alias of core.color.white"}},
  "border": {"$value": "{color.field-border}", "$type": "color", "$extensions": {"source": "alias of core.color.field-border"}},
  "field": {"$value": "{color.field}", "$type": "color", "$extensions": {"source": "alias of core.color.field"}},
  "component": {
    "button": {
      "background": {"$value": "{color.ink}", "$type": "color", "$extensions": {"source": "Get Started anchor backgroundColor"}},
      "text": {"$value": "{color.white}", "$type": "color", "$extensions": {"source": "Get Started label color"}},
      "radius": {"$value": "{radius.pill}", "$type": "dimension", "$extensions": {"source": "Get Started borderRadius"}},
      "height": {"$value": "{layout.header-cta-height}", "$type": "dimension", "$extensions": {"source": "Get Started height"}},
    },
    "field": {
      "background": {"$value": "{color.field}", "$type": "color", "$extensions": {"source": "login email backgroundColor"}},
      "text": col(login["email"]["color"], "login email color"),
      "radius": {"$value": "{radius.control}", "$type": "dimension", "$extensions": {"source": "login email borderRadius"}},
      "height": {"$value": "{layout.login-field-height}", "$type": "dimension", "$extensions": {"source": "login email height"}},
    },
  },
}

doc = {
  "$description": "Hello Ivy public marketing site and login wall, measured 2026-11-21. Light only.",
  "core": core,
  "light": light,
  "$themes": [{"id": "light", "name": "Light", "selectedTokenSets": {"core": "enabled", "light": "enabled"}}],
}

# Fix the price size source: it is measured, recorded in extra-styles, not a string guess.
# The dim() call above used a literal that was read in the same session. Keep the source honest.
core["font"]["size"]["price"]["$extensions"]["source"] = (
    "Measured computed style, pricing page span text '$12', fontSize 28px, Unbounded 500. "
    "raw/extra-styles.json. 2026-11-21."
)

OUT.write_text(json.dumps(doc, indent=2) + "\n")
print("wrote", OUT)
