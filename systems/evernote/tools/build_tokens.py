#!/usr/bin/env python3
"""Build tokens.json from raw/readings.json. Does not recapture the site."""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
readings = json.loads((ROOT / "raw" / "readings.json").read_text())
home = readings["home"]
plans = readings["plans"]
ai = readings["aiFeatures"]
login = readings["loginWall"]


def color(value, source, description):
    return {
        "$value": value,
        "$type": "color",
        "$description": description,
        "$extensions": {"source": source},
    }


def dim(value, source, description, type_="dimension"):
    return {
        "$value": value,
        "$type": type_,
        "$description": description,
        "$extensions": {"source": source},
    }


def font(value, source, description):
    return {
        "$value": value,
        "$type": "fontFamily",
        "$description": description,
        "$extensions": {"source": source},
    }


tokens = {
    "$description": (
        "Evernote public signed-out surfaces, measured 2026-11-22 from computed "
        "styles on https://evernote.com/, https://evernote.com/en-us/compare-plans, "
        "https://evernote.com/en-us/features/ai-features, and the empty login wall "
        "at https://accounts.evernote.com/login. The homepage and plans page paint "
        "the light set. The AI Features page puts class dark on header and main "
        "and paints the dark set. There is no theme switch. prefers-color-scheme "
        "was dark in the measurement browser and the homepage stayed light."
    ),
    "core": {
        "color": {
            "cream": color(
                "#f9f6f2",
                "Computed backgroundColor of header on https://evernote.com/ is rgb(249, 246, 242). :root --color-bg-primary is #F9F6F2.",
                "Page and header cream.",
            ),
            "sand": color(
                "#f4eee5",
                "Computed backgroundColor of the homepage hero card is rgb(244, 238, 229). :root --color-bg-secondary is #F4EEE5.",
                "Secondary sand surface.",
            ),
            "ink": color(
                "#141414",
                "Computed color of homepage h1 is rgb(20, 20, 20). Start for free backgroundColor is the same rgb(20, 20, 20). :root --color-text-primary is #141414.",
                "Primary ink for type and the filled button.",
            ),
            "ink-soft": color(
                "#262626",
                "Computed color of the homepage hero paragraph is rgb(38, 38, 38). :root --color-text-secondary is #262626. The homepage dark band backgroundColor is the same rgb(38, 38, 38).",
                "Secondary ink and the dark marketing band.",
            ),
            "tertiary": color(
                "#4e4d4c",
                "Computed color of the plans page 'Pay $79.90 / year' is rgb(78, 77, 76). Class text-text-tertiary. :root --color-text-tertiary is #4E4D4C.",
                "Tertiary grey type.",
            ),
            "white": color(
                "#ffffff",
                "Computed color of the Start for free label span on https://evernote.com/ is rgb(255, 255, 255). Login wall body backgroundColor is rgb(255, 255, 255).",
                "White label on the ink button, and the login wall field.",
            ),
            "green": color(
                "#00a82d",
                "Stylesheet rule .bg-green and .text-green set rgb(0, 168, 45). The favicon SVG path fill is #00A82D. An AI Features SVG computed color is rgb(0, 168, 45). The button hover rule .hover:bg-green:hover was not hovered.",
                "Evernote green. Declared as the hover fill. Not sampled from a hovered button.",
            ),
            "lime": color(
                "#94e130",
                "Computed backgroundColor of the homepage Capture chip and Discover more button is rgb(148, 225, 48). Class bg-green-secondary. On the AI Features page, Start for free backgroundColor is the same rgb(148, 225, 48).",
                "Lime secondary green, painted on chips and on the dark-page primary button.",
            ),
            "stroke-button": color(
                "#a1a1a1",
                "Computed borderTopColor of Choose Starter on https://evernote.com/en-us/compare-plans is rgb(161, 161, 161). :root --color-stroke-buttons is #A1A1A1.",
                "Outline of the secondary plan button.",
            ),
            "stroke-card": color(
                "#e7e7e7",
                "Computed borderTopColor of the homepage hero card is rgb(231, 231, 231). :root --color-stroke-cards is #E7E7E7.",
                "Card hairline.",
            ),
            "field-line": color(
                "#cccccc",
                "Computed borderTopColor of the empty email field on https://accounts.evernote.com/login is rgb(204, 204, 204). The disabled Continue button uses the same rgb(204, 204, 204).",
                "Login field border and disabled Continue fill.",
            ),
            "auth-ink": color(
                "#333333",
                "Computed color of Continue with Apple on the login wall is rgb(51, 51, 51). The control was not clicked.",
                "Identity-provider label ink. The control was not used.",
            ),
        },
        "font": {
            "display": font(
                "Figtree, \"Figtree Fallback\"",
                "Computed fontFamily of homepage h1, header nav, and Start for free. :root --font-figtree is \"Figtree\",\"Figtree Fallback\".",
                "Marketing display and UI face.",
            ),
            "text": font(
                "Inter, \"Inter Fallback\"",
                "Computed fontFamily of the homepage hero paragraph and of the login wall body. :root --font-inter is \"Inter\",\"Inter Fallback\".",
                "Body and auth face.",
            ),
        },
        "fontSize": {
            "display": dim("72px", "Computed fontSize of homepage h1.", "Hero display size."),
            "title": dim("50px", "Computed fontSize of homepage h2.", "Section title size."),
            "auth-title": dim("32px", "Computed fontSize of the login wall h1.", "Auth heading size."),
            "lede": dim("20px", "Computed fontSize of the homepage hero paragraph and of the Discover more label.", "Lede and large button label."),
            "body": dim("16px", "Computed fontSize of body, nav, and Start for free.", "Body and control size."),
            "field": dim("15px", "Computed fontSize of the login email field.", "Auth field size."),
        },
        "fontWeight": {
            "regular": dim("400", "Computed fontWeight of body and nav links.", "Regular.", "fontWeight"),
            "medium": dim("500", "Computed fontWeight of the phone-banner Download control.", "Medium.", "fontWeight"),
            "semibold": dim("600", "Computed fontWeight of homepage h1 and of the Start for free label.", "Semibold.", "fontWeight"),
        },
        "lineHeight": {
            "display": dim("72px", "Computed lineHeight of homepage h1.", "Display leading."),
            "title": dim("55px", "Computed lineHeight of homepage h2.", "Title leading."),
            "lede": dim("30px", "Computed lineHeight of the homepage hero paragraph.", "Lede leading."),
            "body": dim("24px", "Computed lineHeight of body.", "Body leading."),
        },
        "letterSpacing": {
            "display": dim("-3.6px", "Computed letterSpacing of homepage h1.", "Display tracking."),
            "title": dim("-2.5px", "Computed letterSpacing of homepage h2.", "Title tracking."),
            "lede": dim("-1px", "Computed letterSpacing of the homepage hero paragraph.", "Lede tracking."),
        },
        "radius": {
            "button": dim("5px", "Computed borderRadius of Start for free and Choose Starter.", "Control radius."),
            "nav": dim("10px", "Computed borderRadius of the AI Features nav link.", "Nav link radius."),
            "card": dim("16px", "Computed borderRadius of the homepage hero card.", "Card radius."),
            "field": dim("6px", "Computed borderRadius of the login email field.", "Auth field radius."),
            "auth-button": dim("8px", "Computed borderRadius of the disabled Continue button.", "Auth button radius."),
            "chip": dim("52px", "Computed borderRadius of the Capture chip.", "Pill chip radius."),
        },
        "size": {
            "header": dim("81px", "Computed height of the fixed header on https://evernote.com/.", "Header height."),
            "button": dim("46px", "Computed height of Start for free.", "Header button height."),
            "button-hero": dim("59px", "Computed height of Get Evernote free.", "Hero button height."),
            "field": dim("50px", "Computed height of the login email field and Continue.", "Auth control height."),
        },
        "space": {
            "button-x": dim("28px", "Computed padding-left of Start for free is 28px (padding 10px 28px).", "Header button inline padding."),
            "button-y": dim("10px", "Computed padding-top of Start for free is 10px.", "Header button block padding."),
            "hero-button-x": dim("40px", "Computed padding-left of Get Evernote free is 40px.", "Hero button inline padding."),
            "hero-button-y": dim("16px", "Computed padding-top of Get Evernote free is 16px.", "Hero button block padding."),
        },
        "duration": {
            "button": dim(
                "150ms",
                "Computed transitionDuration of Discover more is 0.15s.",
                "Button motion duration.",
                "duration",
            ),
        },
        "easing": {
            "button": {
                "$value": "cubic-bezier(0.4, 0, 0.2, 1)",
                "$type": "cubicBezier",
                "$description": "Button easing.",
                "$extensions": {
                    "source": "Computed transitionTimingFunction of Discover more is cubic-bezier(0.4, 0, 0.2, 1)."
                },
            }
        },
    },
    "light": {
        "color": {
            "page": color(
                "{core.color.cream}",
                "Computed header and footer backgroundColor on https://evernote.com/ is rgb(249, 246, 242).",
                "Light page and chrome.",
            ),
            "surface": color(
                "{core.color.sand}",
                "Computed homepage hero card backgroundColor is rgb(244, 238, 229).",
                "Raised sand card.",
            ),
            "band": color(
                "{core.color.ink-soft}",
                "Computed backgroundColor of the homepage section.bg-bg-secondary.background-image--v11-da is rgb(38, 38, 38).",
                "Dark band painted on the light homepage.",
            ),
            "text": color(
                "{core.color.ink}",
                "Computed color of homepage h1 is rgb(20, 20, 20).",
                "Primary type.",
            ),
            "text-secondary": color(
                "{core.color.ink-soft}",
                "Computed color of the homepage hero paragraph is rgb(38, 38, 38).",
                "Secondary type.",
            ),
            "text-tertiary": color(
                "{core.color.tertiary}",
                "Computed color of plans 'Pay $79.90 / year' is rgb(78, 77, 76).",
                "Tertiary type.",
            ),
            "on-button": color(
                "{core.color.white}",
                "Computed color of the Start for free label span on the homepage is rgb(255, 255, 255).",
                "Label on the ink button.",
            ),
            "button": color(
                "{core.color.ink}",
                "Computed backgroundColor of Start for free on the homepage is rgb(20, 20, 20).",
                "Primary button fill on light pages.",
            ),
            "accent": color(
                "{core.color.lime}",
                "Computed backgroundColor of Capture and Discover more on the homepage is rgb(148, 225, 48).",
                "Painted lime accent.",
            ),
            "on-accent": color(
                "{core.color.ink}",
                "Computed color of the Capture chip and of the Discover more label is rgb(20, 20, 20).",
                "Ink on the lime accent.",
            ),
            "border": color(
                "{core.color.stroke-card}",
                "Computed borderTopColor of the homepage hero card is rgb(231, 231, 231).",
                "Card border.",
            ),
            "border-strong": color(
                "{core.color.stroke-button}",
                "Computed borderTopColor of Choose Starter is rgb(161, 161, 161).",
                "Outline button border.",
            ),
            "field": color(
                "{core.color.white}",
                "Login wall body backgroundColor is rgb(255, 255, 255). The email field backgroundColor is transparent over that field.",
                "Auth page field.",
            ),
            "field-border": color(
                "{core.color.field-line}",
                "Computed borderTopColor of the empty login email field is rgb(204, 204, 204).",
                "Auth field border.",
            ),
            "disabled": color(
                "{core.color.field-line}",
                "Computed backgroundColor of the empty-state Continue button is rgb(204, 204, 204). The button was not clicked.",
                "Disabled Continue fill.",
            ),
        }
    },
    "dark": {
        "$description": "Painted where header and main carry class dark, measured on https://evernote.com/en-us/features/ai-features. Not a site-wide theme. The homepage stayed light while prefers-color-scheme was dark.",
        "color": {
            "page": color(
                "#141414",
                "header computed --color-bg-primary is #141414. header and main backgroundColor are rgb(20, 20, 20), which is the same hex.",
                "Dark page and header.",
            ),
            "surface": color(
                "#262626",
                "header computed --color-bg-secondary is #262626. Declared on .dark. Not sampled from a painted card on this page.",
                "Dark secondary surface token.",
            ),
            "text": color(
                "#ffffff",
                "Computed color of the AI Features h2 and of the AI Features nav label is rgb(255, 255, 255). header computed --color-text-primary is #FFFFFF.",
                "Type on the dark page.",
            ),
            "text-secondary": color(
                "#fdfcfc",
                "header computed --color-text-secondary is #FDFCFC. Declared on .dark. Not sampled from a painted paragraph on this page.",
                "Secondary type token on the dark page.",
            ),
            "button": color(
                "{core.color.lime}",
                "Computed backgroundColor of Start for free inside the dark header is rgb(148, 225, 48). Class includes dark:bg-green-secondary.",
                "Primary button fill on the dark page.",
            ),
            "on-button": color(
                "{core.color.ink}",
                "Computed color of the Start for free label inside the dark header is rgb(20, 20, 20).",
                "Label on the lime button.",
            ),
            "border": color(
                "#ffffff33",
                "header computed --color-stroke-cards is #FFFFFF33. Declared on .dark.",
                "Dark card stroke token.",
            ),
            "border-strong": color(
                "#ffffff66",
                "header computed --color-stroke-buttons is #FFFFFF66. Declared on .dark.",
                "Dark button stroke token.",
            ),
        }
    },
    "$themes": [
        {
            "id": "light",
            "name": "Light",
            "selectedTokenSets": {"core": "source", "light": "enabled"},
        },
        {
            "id": "dark",
            "name": "Dark",
            "selectedTokenSets": {"core": "source", "dark": "enabled"},
        },
    ],
}

# Keep the plans and login readings referenced so a rebuild fails if they drift.
assert plans["chooseStarter"]["border"] == "1px solid rgb(161, 161, 161)"
assert login["continue"]["notClicked"] is True
assert ai["headerVars"]["--color-bg-primary"] == "#141414"
assert home["vars"]["--color-bg-primary"] == "#F9F6F2"

(ROOT / "tokens.json").write_text(json.dumps(tokens, indent=2) + "\n")
print(f"wrote tokens.json ({sum(1 for _ in json.dumps(tokens))} chars)")
