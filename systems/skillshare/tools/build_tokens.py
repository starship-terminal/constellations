#!/usr/bin/env python3
"""Build tokens.json from measured Skillshare public-surface readings.

Values were read on 2026-11-21 from signed-out pages in headless Chromium.
Skillshare's marketing CSS declares no design custom properties on :root
(raw/capture-readings.json and the stylesheet probe). Every token here is a
computed style or a flat fill sampled from a raw screenshot before quantize.

Do not invent values. A role that was not read is absent, not guessed.
"""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent.parent
OUT = HERE / "tokens.json"


def color(value, source, description):
    return {
        "$value": value,
        "$type": "color",
        "$description": description,
        "$extensions": {"source": source},
    }


def dim(value, source, description):
    return {
        "$value": value,
        "$type": "dimension",
        "$description": description,
        "$extensions": {"source": source},
    }


def font_family(value, source, description):
    return {
        "$value": value,
        "$type": "fontFamily",
        "$description": description,
        "$extensions": {"source": source},
    }


def weight(value, source, description):
    return {
        "$value": value,
        "$type": "fontWeight",
        "$description": description,
        "$extensions": {"source": source},
    }


def alias(path, description):
    return {
        "$value": "{" + path + "}",
        "$type": "color",
        "$description": description,
        "$extensions": {"source": "alias of " + path},
    }


tokens = {
    "core": {
        "color": {
            "ink": color(
                "#0b1215",
                "computed color of the Sign Up button and the login Sign In button, 2026-11-21",
                "Near-black ink on green buttons and form text.",
            ),
            "black": color(
                "#000000",
                "computed color of the home h1, and a flat fill of the promo bar in about-light-video.png before quantize",
                "Hero ink and the promo bar fill.",
            ),
            "paper": color(
                "#ffffff",
                "computed background of the login email field and the Continue with Google button",
                "Page and control paper.",
            ),
            "canvas": color(
                "#f4f4f4",
                "computed backgroundColor of the body on /en/login",
                "Login page canvas.",
            ),
            "footer": color(
                "#020404",
                "sampled flat fill of the footer in about-light-video.png at (40, 850) before quantize",
                "Footer fill. Sampled, not a declared token.",
            ),
            "green": color(
                "#55da9b",
                "computed backgroundColor of the header Sign Up button and the login Sign In button",
                "Primary action fill.",
            ),
            "green-hover": color(
                "#50cf93",
                "computed backgroundColor of the Sign Up button with CDP forcePseudoState hover",
                "Primary action hover fill.",
            ),
            "link": color(
                "#5620c1",
                "computed color of Continue with email and the login Sign up link",
                "Link and focus purple.",
            ),
            "line": color(
                "#dcdee1",
                "computed borderTopColor of the search box and the login email field",
                "Field and search hairline.",
            ),
            "line-strong": color(
                "#394649",
                "computed borderTopColor of the Continue with Google button",
                "Social button border.",
            ),
            "muted": color(
                "#555555",
                "computed color of the Help Center search input",
                "Help search text. Help Center only.",
            ),
        },
        "font": {
            "family": {
                "sans": font_family(
                    '"GT Walsheim Pro", Arial, sans-serif',
                    "computed fontFamily of the Sign Up button; @font-face src https://static.skillshare.com/assets/fonts/gt-walsheim-pro/",
                    "Marketing and product UI stack. The face is served, not bundled.",
                ),
            },
            "size": {
                "hero": dim("46px", "computed fontSize of the home h1", "Home hero."),
                "teams-hero": dim("50px", "computed fontSize of the teams h1", "Teams hero."),
                "help-title": dim("36px", "computed fontSize of the Help Center h1", "Help Center title."),
                "button": dim("18px", "computed fontSize of the Sign Up button", "Primary button label."),
                "body": dim("16px", "computed fontSize of Continue with Google", "Social button label."),
                "nav": dim("15px", "computed fontSize of the Browse trigger", "Header nav."),
                "field": dim("15px", "computed fontSize of the login email field", "Login field."),
            },
            "weight": {
                "bold": weight(700, "computed fontWeight of the home h1 and the Sign Up button", "Headings and actions."),
                "regular": weight(400, "computed fontWeight of the login email field", "Field text."),
            },
            "line-height": {
                "hero": dim("57.96px", "computed lineHeight of the home h1", "Home hero line height."),
                "button": dim("39px", "computed lineHeight of the Sign Up button", "Button line height."),
            },
        },
        "radius": {
            "control": dim("4px", "computed borderRadius of the Sign Up button, search box, and login email field", "Shared control radius."),
        },
        "size": {
            "header": dim("80px", "measured height of the painted header bar on the home page", "Desktop header."),
            "button": dim("40px", "computed height of the Sign Up button and the login Sign In button", "Primary button."),
            "search": dim("40px", "computed height of the search combobox", "Search field."),
            "social": dim("40px", "computed height of Continue with Google on the home page", "Home social button. The login page social buttons measure 55px."),
        },
        "border": {
            "width": dim("1px", "computed borderTopWidth of the Sign Up button and the search box", "Control border."),
        },
    },
    "light": {
        "page": alias("core.color.paper", "Page paper."),
        "surface": alias("core.color.canvas", "Login canvas."),
        "text": alias("core.color.ink", "Button and form ink."),
        "muted": alias("core.color.muted", "Help search text."),
        "accent": alias("core.color.green", "Primary action."),
        "border": alias("core.color.line", "Field hairline."),
        "link": alias("core.color.link", "Link purple."),
        "focus": color(
            "#5620c1",
            "computed outline of the Sign Up button with CDP forcePseudoState focus-visible: rgb(86, 32, 193) auto 1px",
            "Focus ring. Same purple as links.",
        ),
        "component": {
            "button": {
                "background": alias("core.color.green", "Sign Up and login Sign In fill."),
                "text": alias("core.color.ink", "Sign Up label."),
                "radius": dim("4px", "computed borderRadius of the Sign Up button", "Button radius."),
                "height": dim("40px", "computed height of the Sign Up button", "Button height."),
            },
            "button-hover": {
                "background": alias("core.color.green-hover", "Sign Up hover fill."),
            },
            "field": {
                "background": alias("core.color.paper", "Email field fill."),
                "text": alias("core.color.ink", "Email field text."),
                "border": alias("core.color.line", "Email field border."),
                "radius": dim("4px", "computed borderRadius of the login email field", "Field radius."),
                "height": dim("40px", "computed height of the login email field", "Field height."),
            },
        },
    },
    "$themes": [
        {"id": "light", "name": "light", "selectedTokenSets": {"core": "source", "light": "enabled"}},
    ],
}

# Drop empty groups if any builder expects no dark set. Light only.
OUT.write_text(json.dumps(tokens, indent=2) + "\n")
print("wrote", OUT)
