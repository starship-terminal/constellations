#!/usr/bin/env python3
"""Build tokens.json from raw/readings.json.

Public Notion marketing site, measured 2026-11-21 from https://www.notion.com/.
One painted light theme. Values are computed styles. Nothing is filled from memory.
"""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = json.loads((HERE / "raw" / "readings.json").read_text())
PAGE = RAW["readings"]["page"]
RUN = RAW["readings"]["captured"]


def src(note, prop):
    return {
        "label": "Measured",
        "file": "raw/readings.json",
        "property": prop,
        "page": PAGE,
        "run": RUN,
        "note": note,
    }


def color(value, note, prop):
    return {"$type": "color", "$value": value, "$extensions": {"source": src(note, prop)}}


def dim(value, note, prop):
    return {"$type": "dimension", "$value": value, "$extensions": {"source": src(note, prop)}}


def font(value, note, prop):
    return {"$type": "fontFamily", "$value": value, "$extensions": {"source": src(note, prop)}}


def weight(value, note, prop):
    return {"$type": "fontWeight", "$value": value, "$extensions": {"source": src(note, prop)}}


c = RAW["readings"]["computed"]
pricing = RAW["pricing"]
login = RAW["login"]
blue = next(p for p in pricing if p["text"] == "Get Notion free")
soft = next(p for p in pricing if p["backgroundColor"] == "rgb(230, 243, 254)")

tokens = {
    "core": {
        "font": {
            "display": font(
                c["h1"]["fontFamily"],
                "Homepage h1 family. NotionInter, then Inter.",
                "readings.computed.h1.fontFamily",
            ),
            "body": font(
                c["body"]["fontFamily"],
                "Body family on www.notion.com.",
                "readings.computed.body.fontFamily",
            ),
            "app": font(
                login["input"]["fontFamily"],
                "Login field on app.notion.com. Inter, no NotionInter.",
                "login.input.fontFamily",
            ),
        },
        "fontSize": {
            "display": dim(c["h1"]["fontSize"], "Homepage h1.", "readings.computed.h1.fontSize"),
            "body": dim(c["body"]["fontSize"], "Body.", "readings.computed.body.fontSize"),
            "button": dim(c["navCta"]["fontSize"], "Header Get Notion free.", "readings.computed.navCta.fontSize"),
            "login-heading": dim("22px", "Login heading on app.notion.com.", "login.heading"),
            "login-field": dim(login["input"]["fontSize"], "Login email field.", "login.input.fontSize"),
        },
        "lineHeight": {
            "display": dim(c["h1"]["lineHeight"], "Homepage h1.", "readings.computed.h1.lineHeight"),
            "body": dim(c["body"]["lineHeight"], "Body.", "readings.computed.body.lineHeight"),
            "button": dim(c["navCta"]["lineHeight"], "Header Get Notion free.", "readings.computed.navCta.lineHeight"),
        },
        "fontWeight": {
            "display": weight(c["h1"]["fontWeight"], "Homepage h1.", "readings.computed.h1.fontWeight"),
            "body": weight(c["body"]["fontWeight"], "Body.", "readings.computed.body.fontWeight"),
            "button": weight(c["navCta"]["fontWeight"], "Header Get Notion free.", "readings.computed.navCta.fontWeight"),
        },
        "letterSpacing": {
            "display": dim(c["h1"]["letterSpacing"], "Homepage h1.", "readings.computed.h1.letterSpacing"),
        },
        "space": {
            "nav-button-x": dim("14px", "Header Get Notion free horizontal padding.", "readings.computed.navCta.padding"),
            "nav-button-y": dim("4px", "Header Get Notion free vertical padding.", "readings.computed.navCta.padding"),
            "hero-button-x": dim("15px", "Hero Get Notion free horizontal padding.", "readings.computed.heroCta.padding"),
            "hero-button-y": dim("6px", "Hero Get Notion free vertical padding.", "readings.computed.heroCta.padding"),
        },
        "radius": {
            "button": dim(c["navCta"]["borderRadius"], "Header and pricing primary buttons.", "readings.computed.navCta.borderRadius"),
            "nav-item": dim(c["product"]["borderRadius"], "Product and Resources triggers.", "readings.computed.product.borderRadius"),
            "login-button": dim(login["continue"]["borderRadius"], "Login Continue.", "login.continue.borderRadius"),
        },
        "size": {
            "nav-button": dim(c["navCta"]["height"], "Header Get Notion free.", "readings.computed.navCta.height"),
            "hero-button": dim(c["heroCta"]["height"], "Hero Get Notion free.", "readings.computed.heroCta.height"),
            "login-button": dim(login["continue"]["height"], "Login Continue.", "login.continue.height"),
            "login-field": dim(login["input"]["height"], "Login email input. The visible ring is on a parent.", "login.input.height"),
        },
    },
    "light": {
        "color": {
            "page": color(c["body"]["backgroundColor"], "Body background.", "readings.computed.body.backgroundColor"),
            "text": color(c["body"]["color"], "Body text.", "readings.computed.body.color"),
            "text-nav": color(c["product"]["color"], "Product trigger.", "readings.computed.product.color"),
            "accent": color(c["navCta"]["backgroundColor"], "Header Get Notion free fill. Same blue as pricing Get Notion free.", "readings.computed.navCta.backgroundColor"),
            "accent-on": color(c["navCta"]["color"], "Label on the blue button.", "readings.computed.navCta.color"),
            "accent-soft": color(soft["backgroundColor"], "Pricing Free Sign up fill.", "pricing.Sign up.backgroundColor"),
            "accent-soft-text": color(soft["color"], "Pricing Free Sign up label.", "pricing.Sign up.color"),
            "link": color("rgb(9, 127, 232)", "Pricing Contact Sales label.", "pricing.Contact Sales.color"),
            "login-accent": color(login["continue"]["backgroundColor"], "Continue on app.notion.com. A different blue from the marketing button.", "login.continue.backgroundColor"),
            "login-text": color(login["input"]["color"], "Login field text.", "login.input.color"),
        }
    },
    "$themes": [
        {"id": "light", "name": "Light", "selectedTokenSets": {"core": "source", "light": "enabled"}}
    ],
}

# silence unused
_ = blue
(HERE / "tokens.json").write_text(json.dumps(tokens, indent=1) + "\n")
print("wrote", HERE / "tokens.json")
