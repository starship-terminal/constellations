#!/usr/bin/env python3
"""Build systems/fibery/tokens.json from raw/css-vars.json and raw/computed.json.

Every colour token is a custom property read on https://fibery.com/ on
2026-11-21, or a computed style named in raw/computed.json. Sizes are the
computed styles of the elements named there. Nothing is filled from memory.
"""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
VARS = json.loads((RAW / "css-vars.json").read_text())["vars"]
COMP = json.loads((RAW / "computed.json").read_text())


def color(name, value, source, description=None):
    token = {
        "$value": value,
        "$type": "color",
        "$extensions": {"source": source},
    }
    if description:
        token["$description"] = description
    return token


def dim(value, source, description=None):
    token = {
        "$value": value,
        "$type": "dimension",
        "$extensions": {"source": source},
    }
    if description:
        token["$description"] = description
    return token


def font(value, source):
    return {
        "$value": value,
        "$type": "fontFamily",
        "$extensions": {"source": source},
    }


def typo(size, weight, line, source):
    return {
        "fontFamily": "{core.font.family.sans}",
        "fontSize": size,
        "fontWeight": weight,
        "lineHeight": line,
        "$type": "typography",
        "$extensions": {"source": source},
    }


def by_name(name):
    for item in COMP["components"]:
        if item["name"] == name:
            return item
    raise KeyError(name)


SRC = "css-var on https://fibery.com/ 2026-11-21"
primary = by_name("button-primary")
quiet = by_name("button-quiet")
pill = by_name("pill")
display = by_name("display")
heading = by_name("heading")
title = by_name("title")
body = by_name("body")
email = by_name("login-email")

tokens = {
    "core": {
        "palette": {
            "ink": color("ink", VARS["--fibery-basic-black"], f"{SRC}; --fibery-basic-black", "Page text and the filled signup button"),
            "soup": color("soup", VARS["--fibery-soup"], f"{SRC}; --fibery-soup", "Page background"),
            "cream": color("cream", VARS["--fibery-cream"], f"{SRC}; --fibery-cream", "Quiet button and light page wash"),
            "milk": color("milk", VARS["--fibery-milk"], f"{SRC}; --fibery-milk", "Text on the filled button, and the login control face"),
            "menu": color("menu", VARS["--fibery-menu-bg-color"], f"{SRC}; --fibery-menu-bg-color"),
            "peach-soup": color("peach-soup", VARS["--fibery-peach-soup"], f"{SRC}; --fibery-peach-soup"),
            "tea": color("tea", VARS["--fibery-tea"], f"{SRC}; --fibery-tea"),
            "rusty": color("rusty", VARS["--fibery-rusty"], f"{SRC}; --fibery-rusty"),
            "terracotta": color("terracotta", VARS["--fibery-terracotta"], f"{SRC}; --fibery-terracotta"),
            "architect-rust": color("architect-rust", VARS["--fibery-architect-rust"], f"{SRC}; --fibery-architect-rust"),
            "website-blue": color("website-blue", VARS["--fibery-website-blue"], f"{SRC}; --fibery-website-blue", "Named page accent; also the form-button blue"),
            "mint": color("mint", VARS["--fibery-basic-mint"], f"{SRC}; --fibery-basic-mint"),
            "green": color("green", VARS["--fibery-basic-green"], f"{SRC}; --fibery-basic-green"),
            "red": color("red", VARS["--fibery-basic-red"], f"{SRC}; --fibery-basic-red"),
            "yellow": color("yellow", VARS["--fibery-basic-yellow"], f"{SRC}; --fibery-basic-yellow"),
            "blue": color("blue", VARS["--fibery-basic-blue"], f"{SRC}; --fibery-basic-blue"),
            "pink": color("pink", VARS["--fibery-basic-pink"], f"{SRC}; --fibery-basic-pink"),
            "orange": color("orange", VARS["--fibery-basic-orange"], f"{SRC}; --fibery-basic-orange"),
            "violet": color("violet", VARS["--fibery-basic-violet"], f"{SRC}; --fibery-basic-violet"),
            "chat-accent": color("chat-accent", VARS["--chat-accent"], f"{SRC}; --chat-accent"),
            "focus": color("focus", "rgb(0, 95, 204)", "computed outline on the first Tab stop, https://fibery.com/ 2026-11-21; browser default, not a product token"),
        },
        "font": {
            "family": {
                "sans": font("Suisse Intl, sans-serif", "computed font-family on body, https://fibery.com/ 2026-11-21"),
            }
        },
        "typography": {
            "display": typo(display["fontSize"], display["fontWeight"], display["lineHeight"], "computed h1, https://fibery.com/"),
            "heading": typo(heading["fontSize"], heading["fontWeight"], heading["lineHeight"], "computed h2, https://fibery.com/"),
            "title": typo(title["fontSize"], title["fontWeight"], title["lineHeight"], "computed h3, https://fibery.com/"),
            "body": typo(body["fontSize"], body["fontWeight"], body["lineHeight"], "computed body, https://fibery.com/"),
            "button": typo(primary["fontSize"], primary["fontWeight"], primary["lineHeight"], "computed header a[href=/sign-up]"),
        },
        "radius": {
            "control": dim(primary["borderRadius"], "computed border-radius on header signup link"),
            "pill": dim(pill["borderRadius"], "computed border-radius on TabPillButton"),
            "composer": dim(VARS["--chat-composer-radius"], f"{SRC}; --chat-composer-radius"),
        },
        "space": {
            "control-x": dim("16px", "computed padding-inline on header signup link"),
            "control-y": dim("0px", "computed padding-block on header signup link"),
            "login-x": dim("12px", "computed padding-inline on Continue with Email, https://fibery.io/login"),
            "login-y": dim("8px", "computed padding-block on Continue with Email"),
            "pill-x": dim("12px", "computed padding-inline on TabPillButton"),
            "pill-y": dim("6px", "computed padding-block on TabPillButton"),
            "header": dim("12px", "computed padding on header"),
        },
        "size": {
            "button": dim(primary["height"], "computed height of header signup link"),
            "login-button": dim(email["height"], "computed height of Continue with Email"),
            "pill": dim(pill["height"], "computed height of TabPillButton"),
            "header": dim("88px", "computed height of header at 1440"),
        },
        "shadow": {
            "m": {
                "$value": VARS["--fibery-shadow-m"],
                "$type": "shadow",
                "$extensions": {"source": f"{SRC}; --fibery-shadow-m"},
            }
        },
    },
    "light": {
        "background": {
            "page": color("page", "{core.palette.soup}", f"{SRC}; --fibery-page-body-color matches --fibery-soup"),
            "surface": color("surface", "{core.palette.cream}", f"{SRC}; --fibery-page-body-color-light matches --fibery-cream"),
            "menu": color("menu", "{core.palette.menu}", f"{SRC}; --fibery-menu-bg-color"),
            "action": color("action", "{core.palette.ink}", "computed background of header a[href=/sign-up]"),
            "quiet": color("quiet", "{core.palette.cream}", "computed background of header a[href=/login]"),
            "pill": color("pill", "rgb(240, 215, 200)", "computed background of TabPillButton; no matching custom property"),
        },
        "text": {
            "primary": color("primary", "{core.palette.ink}", f"{SRC}; --fibery-text-default-color"),
            "on-action": color("on-action", "{core.palette.soup}", "computed color of header signup link; matches page soup"),
            "opposite": color("opposite", "{core.palette.milk}", f"{SRC}; --fibery-text-opposite-color"),
            "secondary": color("secondary", VARS["--fibery-text-secondary-color"], f"{SRC}; --fibery-text-secondary-color"),
            "muted": color("muted", VARS["--fibery-mud-text"], f"{SRC}; --fibery-mud-text"),
        },
        "border": {
            "default": color("default", VARS["--fibery-light-gray-border-color"], f"{SRC}; --fibery-light-gray-border-color"),
            "strong": color("strong", "{core.palette.ink}", "computed text colour used as the hairline on ink controls"),
        },
        "accent": {
            "default": color("default", "{core.palette.website-blue}", f"{SRC}; --fibery-page-main-color and --fibery-website-blue"),
        },
        "status": {
            "danger": color("danger", "{core.palette.red}", f"{SRC}; --fibery-basic-red"),
            "warning": color("warning", "{core.palette.yellow}", f"{SRC}; --fibery-basic-yellow"),
            "success": color("success", "{core.palette.green}", f"{SRC}; --fibery-basic-green"),
            "info": color("info", "{core.palette.mint}", f"{SRC}; --fibery-basic-mint"),
        },
        "focus": {
            "ring": color("ring", "{core.palette.focus}", "computed outline on first Tab stop; browser default"),
        },
    },
    "$themes": [
        {"id": "light", "name": "light", "selectedTokenSets": {"core": "source", "light": "enabled"}}
    ],
}

(HERE / "tokens.json").write_text(json.dumps(tokens, indent=2) + "\n")
print("wrote", HERE / "tokens.json")
