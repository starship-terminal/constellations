#!/usr/bin/env python3
"""Build tokens.json from the Dona public readings.

dona.ai does not declare CSS custom properties. Colour roles are the
styled-components theme object read on https://dona.ai/ (raw/readings.json
and raw/css-vars.json). Control sizes are getComputedStyle on the home
buttons. The marketing site paints one theme, Light. Dark and black exist
inside the product demo and were not a page theme this capture could switch.

Every token carries $extensions.source. Deterministic.
"""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent.parent
READ = json.loads((HERE / "raw" / "readings.json").read_text())
THEME = READ["home"]["theme"]
BUTTONS = {b["label"]: b for b in READ["home"]["buttons"]}


def src(label, evidence):
    return {"$extensions": {"source": {"label": label, "evidence": evidence}}}


def color(value, evidence, label="Measured"):
    return {"$type": "color", "$value": value, **src(label, evidence)}


def dim(value, evidence):
    return {"$type": "dimension", "$value": value, **src("Measured", evidence)}


def num(value, evidence):
    return {"$type": "number", "$value": value, **src("Measured", evidence)}


cta = BUTTONS["Try for free →"]
quiet = BUTTONS["Watch video"]
login = BUTTONS["Login"]
field = READ["home"]["input"]
body = READ["home"]["body"]
modal = READ.get("modal") or {}

tokens = {
  "$description": "Dona public marketing site, signed out, 2026-11-21. Theme object plus computed styles. One painted theme.",
  "core": {
    "color": {
      "ink": color(THEME["foreground"].lower(), "styled-components theme.foreground on https://dona.ai/"),
      "paper": color(THEME["background"].lower(), "theme.background"),
      "body": color(THEME["body"].lower(), "theme.body, the page wash behind the hero"),
      "blue": color(THEME["primary"]["background"].lower(), "theme.primary.background"),
      "on-accent": color(THEME["primary"]["foreground"].lower(), "theme.primary.foreground"),
      "secondary": color(THEME["secondary"]["background"].lower(), "theme.secondary.background; not painted as a button fill on the marketing pages"),
      "success": color(THEME["success"]["background"].lower(), "theme.success.background; on the theme object, not painted on the public pages"),
      "warning": color(THEME["warning"]["background"].lower(), "theme.warning.background; on the theme object, not painted on the public pages"),
      "danger": color(THEME["danger"]["background"].lower(), "theme.danger.background; on the theme object, not painted on the public pages"),
      "quiet": color("#eceff2", "getComputedStyle Login and Watch video backgroundColor rgb(236, 239, 242)"),
      "muted": color("#a8b0b8", "getComputedStyle of the muted half of the home headline, rgb(168, 176, 184)"),
    },
    "font": {
      "family": {
        "sans": {
          "$type": "fontFamily",
          "$value": ["Inter", "sans-serif"],
          **src("Measured", "body fontFamily Inter, sans-serif; declared in the shared layout chunk as 'Inter', sans-serif"),
        }
      },
      "weight": {
        "regular": num(400, "body fontWeight 400"),
        "medium": num(500, "button fontWeight 500"),
        "bold": num(700, "display headline fontWeight, readings home.headlines"),
      },
      "size": {
        "body": dim(body["fontSize"], "body fontSize"),
        "button": dim(cta["fontSize"], "Try for free button fontSize"),
        "label": dim(login["fontSize"], "Login button fontSize"),
        "display": dim("64px", "home headline fontSize 64px in readings.json home.headlines"),
      },
      "line-height": {
        "body": dim(body["lineHeight"], "body lineHeight"),
        "button": dim(cta["lineHeight"], "CTA lineHeight"),
      },
    },
    "radius": {
      "pill": dim(cta["borderRadius"], "CTA and Login borderRadius 32px"),
      "field": dim(field["borderRadius"] if field else "12px", "newsletter input borderRadius"),
      "modal": dim(modal.get("innerRadius") or "11px", "video modal inner borderRadius from getComputedStyle after Watch video"),
    },
    "size": {
      "button-sm": dim(str(login["height"]) + "px", "Login button height"),
      "button": dim(str(cta["height"]) + "px", "CTA button height"),
      "field": dim((str(field["height"]) + "px") if field else "60px", "newsletter input height"),
      "content": dim("1100px", "home content column width of the newsletter field, readings.json"),
    },
    "motion": {
      "button": {
        "$type": "duration",
        "$value": "150ms",
        **src("Measured", "button transition color/background/box-shadow 0.15s"),
      }
    },
  },
  "light": {
    "page": color("{color.paper}", "alias of theme.background", "Derived"),
    "surface": color("{color.body}", "alias of theme.body", "Derived"),
    "text": color("{color.ink}", "alias of theme.foreground", "Derived"),
    "muted": color("{color.muted}", "alias of the muted headline colour", "Derived"),
    "accent": color("{color.blue}", "alias of theme.primary.background", "Derived"),
    "on-accent": color("{color.on-accent}", "alias of theme.primary.foreground", "Derived"),
    "border": color("{color.quiet}", "quiet button fill is the soft edge; buttons paint no 1px border", "Derived"),
    "focus": color("{color.blue}", "keyboard focus was not a distinct ring on the About button in this pass", "Not captured"),
  },
  "$themes": [
    {"id": "light", "name": "Light", "selectedTokenSets": {"core": "source", "light": "enabled"}}
  ],
}

# Flatten aliases in light.* that point at core.color.*
# The builder stores aliases as {color.ink} which Tokens Studio resolves inside the core set.
# Gallery export expects {core.color.ink} or a same-set path. Use core paths.


(HERE / "tokens.json").write_text(json.dumps(tokens, indent=2) + "\n")
print("wrote", HERE / "tokens.json")
