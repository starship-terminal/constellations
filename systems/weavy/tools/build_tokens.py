#!/usr/bin/env python3
"""Write tokens.json from the 2026-11-19 Weavy / Figma Weave readings.

Values are the ones read off the live pages. Marketing colours are the
:root custom properties in weavy-ai.webflow.shared CSS. Sign-in colours are
the computed light roles on app.weavy.ai/signin, plus the dark theme rule
resolved against the same ramps. A role that was not on the page is absent.
"""
import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
RAW = ROOT / "raw" / "readings.json"


def color(value, source):
    return {"$type": "color", "$value": value, "$extensions": {"source": source}}


def dim(value, source):
    return {"$type": "dimension", "$value": value, "$extensions": {"source": source}}


def font(value, source):
    return {"$type": "fontFamily", "$value": value, "$extensions": {"source": source}}


def number(value, source):
    return {"$type": "number", "$value": value, "$extensions": {"source": source}}


def typography(family, size, weight, line_height, letter_spacing, source):
    value = {
        "fontFamily": family,
        "fontSize": size,
        "fontWeight": weight,
        "lineHeight": line_height,
    }
    if letter_spacing is not None:
        value["letterSpacing"] = letter_spacing
    return {"$type": "typography", "$value": value, "$extensions": {"source": source}}


M = "Measured on https://weave.figma.com/ at 1440x900 on 2026-11-19"
S = "Measured on https://app.weavy.ai/signin at 1440x900 on 2026-11-19, light theme painted"
D = "Declared on [data-preferred-theme=dark] in app.weavy.ai/assets/index-bgQwFbjP.css and resolved against the page ramps. The sign-in page did not paint this theme."


def build():
    readings = json.loads(RAW.read_text())
    assert readings["marketing"]["rootCustomProperties"]["--brand--lemon"] == "#f7ff9e"

    core = {
        "font": {
            "family": {
                "figma-sans": font(
                    "Figma Sans Regular, Arial, sans-serif",
                    "Computed font-family on body, headings and nav at weave.figma.com",
                ),
                "dm-sans": font(
                    "DM Sans, Arial, sans-serif",
                    "Computed font-family Dmsans on the pricing billing labels and FAQ heading",
                ),
                "inter": font(
                    "Inter, ui-sans-serif, system-ui, sans-serif",
                    "Computed --font-family-default on app.weavy.ai/signin",
                ),
            }
        },
        "typography": {
            "display": typography(
                "{font.family.figma-sans}", "94px", 400, "80px", "-4.32px",
                "Computed h1.heading_h1-hero at 1440: 94px / 79.9px / -4.32px. Authored 6.52778rem at a 14.4px root.",
            ),
            "heading": typography(
                "{font.family.figma-sans}", "94px", 400, "82px", "-4.61px",
                "Computed h2.heading-style-xl at 1440: 94px / 81.9999px / -4.608px",
            ),
            "pricing-title": typography(
                "{font.family.figma-sans}", "48px", 400, "58px", "-2.4px",
                "Computed .heading-pricing_xl: 48px / 57.5999px / -2.40048px",
            ),
            "plan-name": typography(
                "{font.family.figma-sans}", "24px", 500, "34px", None,
                "Computed .heading-plan-label: 24px / 500 / 33.6001px",
            ),
            "price": typography(
                "{font.family.figma-sans}", "48px", 700, "58px", "-1.3px",
                "Computed .price-amount: 48px / 700 / 57.5999px / -1.296px",
            ),
            "body": typography(
                "{font.family.figma-sans}", "18px", 400, "20px", None,
                "Computed p.text-size-large: 18px / 19.8px. Authored 1.25rem / 1.1.",
            ),
            "body-small": typography(
                "{font.family.figma-sans}", "15px", 400, "17px", None,
                "Computed .text-size-small: 15.12px / 17.388px. Authored 1.05rem.",
            ),
            "nav": typography(
                "{font.family.figma-sans}", "12px", 400, "12px", "0.15px",
                "Computed .nav_text-link: 12px / 12px / 0.15px, uppercase",
            ),
            "signin-title": typography(
                "{font.family.figma-sans}", "30px", 500, "39px", None,
                "Computed sign-in h1: 30px / 500 / 39px, color rgb(40, 40, 40)",
            ),
            "sso-label": typography(
                "{font.family.figma-sans}", "18px", 700, "18px", None,
                "Computed sign-in SSO button: 18px / 700. line-height was normal.",
            ),
            "legal": typography(
                "{font.family.figma-sans}", "12px", 400, "20px", "0.24px",
                "Computed sign-in legal paragraph: 12px / 20px / 0.24px",
            ),
            "faq-title": typography(
                "{font.family.dm-sans}", "43px", 400, "52px", None,
                "Computed pricing .heading-style-h2: Dmsans 43.2px / 51.84px",
            ),
        },
        "radius": {
            "nav": dim("4px", "Computed .nav_text-link border-radius 4px"),
            "plan": dim("13px", "Computed .pricing_plan-v4 border-radius 13px. Sign-in card is also 13px."),
            "start": dim("8px", "Computed .huge_nav-button.is-real border-bottom-left-radius 8px. Authored 1rem."),
            "primary": dim("8px", "Computed .button-primary border-radius 8.064px. Authored 0.56rem at a 14.4px root."),
            "pill": dim("144px", "Computed .billing-toggle_switch border-radius 144px"),
            "signin-button": dim("8px", "Computed sign-in SSO button border-radius 8px"),
        },
        "space": {
            "nav-x": dim("10px", "Computed .nav_text-link padding-left 10px"),
            "nav-y": dim("6px", "Computed .nav_text-link padding-top 6px"),
            "plan": dim("21px", "Computed .pricing_plan-v4 padding 21.0731px"),
            "plan-button-x": dim("22px", "Computed plan button padding-left 21.6px"),
            "plan-button-y": dim("11px", "Computed plan button padding-top 10.8px"),
            "signin-card-x": dim("48px", "Computed sign-in card padding-left 48px"),
            "signin-card-y": dim("84px", "Computed sign-in card padding-top 84px"),
        },
        "size": {
            "nav-link": dim("24px", "Computed .nav_text-link height 24px"),
            "plan-button": dim("42px", "Computed plan CTA height 42px"),
            "sso-button": dim("48px", "Computed sign-in SSO button height 48px"),
            "start-now": dim("90px", "Computed .huge_nav-button.is-real height 90px at 1440"),
        },
    }

    marketing = {
        "page": color("#ffffff", "Computed body background-color rgb(255, 255, 255). --brand--base--white is white."),
        "text": color("#333333", "Computed body color rgb(51, 51, 51)"),
        "text-strong": color("#000000", "Computed h1 color rgb(0, 0, 0). --brand--base--black is black."),
        "lemon": color("#f7ff9e", "Computed Start Now and slider button background. :root --brand--lemon."),
        "lemon-100": color("#f7ffa8", "Computed Contact Sales background rgb(247, 255, 168). :root --brand--lemon-100. Hover of the plan CTA also computed rgb(247, 255, 158), which is --brand--lemon."),
        "rich-black": color("#252525", "Computed footer background rgb(37, 37, 37). :root --brand--rich-black. Plan CTA fill matches."),
        "richer-black": color("#212126", "Computed current nav link and selected audience tab rgb(33, 33, 38). :root --brand--richer-black."),
        "surface": color("#f5f5f6", "Computed plan card background rgb(245, 245, 246). :root --brand--base--surface--grey-300."),
        "border": color("#e6e6e6", "Computed plan card border rgb(230, 230, 230)"),
        "french-gray": color("#c1cdd5", ":root --brand--french-gray. The home hero gradient uses rgba(193, 205, 213, 0.35)."),
        "ash-grey": color("#aeb3a9", ":root --brand--ash-grey. Declared, not a computed fill on the pages read."),
        "ink": color("#111111", ":root --wv--ink. Declared, not a computed fill on the pages read."),
        "on-lemon": color("#000000", "Computed Start Now text rgb(0, 0, 0)"),
        "on-dark": color("#ffffff", "Computed nav link and footer link color rgb(255, 255, 255)"),
        "nav-hover-text": color("#252525", "Computed .nav_text-link:hover color rgb(37, 37, 37)"),
        "primary-hover-text": color("#f0ffff", "Computed .button-primary:hover color rgb(240, 255, 255). The authored rule names var(--brand--azure), which the stylesheet sets to the keyword azure."),
        "faq-answer": color("#d0d0d2", "Computed .faq_answer color rgb(208, 208, 210). :root --border--soft-grey-200 is #d0d0d2."),
        "faq-border": color("#ffffff26", "Computed .faq_accordion border rgba(255, 255, 255, 0.15)"),
        "muted": color("#00000080", "Computed billing label inactive rgba(0, 0, 0, 0.5)"),
    }

    light = {
        "page": color("#ffffff", S + ". Computed --color-bg #fff. The page shell behind the card is rgb(44, 44, 44), recorded as shell."),
        "shell": color("#2c2c2c", "Computed sign-in page shell rgb(44, 44, 44), which is --ramp-grey-800."),
        "surface": color("#ffffff", "Computed sign-in card background rgb(255, 255, 255)"),
        "surface-secondary": color("#f5f5f5", "Computed --color-bg-secondary #f5f5f5. SSO button hover computed rgb(245, 245, 245)."),
        "surface-tertiary": color("#e6e6e6", "Computed --color-bg-tertiary #e6e6e6"),
        "text": color("#000000e5", "Computed --color-text #000000e5"),
        "text-secondary": color("#00000080", "Computed --color-text-secondary #00000080. Legal copy computed rgba(0, 0, 0, 0.5)."),
        "text-tertiary": color("#0000004d", "Computed --color-text-tertiary #0000004d"),
        "text-disabled": color("#0000004d", "Computed --color-text-disabled #0000004d"),
        "text-brand": color("#007be5", "Computed --color-text-brand #007be5"),
        "text-danger": color("#dc3412", "Computed --color-text-danger #dc3412"),
        "text-success": color("#009951", "Computed --color-text-success #009951"),
        "text-warning": color("#b86200", "Computed --color-text-warning #b86200"),
        "on-brand": color("#ffffff", "Computed --color-text-onbrand #fff"),
        "border": color("#e6e6e6", "Computed --color-border #e6e6e6. SSO button border matches."),
        "border-strong": color("#2c2c2c", "Computed --color-border-strong #2c2c2c"),
        "border-selected": color("#0d99ff", "Computed --color-border-selected #0d99ff"),
        "brand": color("#0d99ff", "Computed --color-bg-brand #0d99ff. Declared hover #007be5, pressed #0768cf."),
        "danger": color("#f24822", "Declared light --color-bg-danger var(--ramp-red-500), resolved #f24822"),
        "success": color("#14ae5c", "Declared light --color-bg-success var(--ramp-green-500), resolved #14ae5c"),
        "warning": color("#ffcd29", "Declared light --color-bg-warning var(--ramp-yellow-500), resolved #ffcd29"),
        "title": color("#282828", "Computed sign-in h1 color rgb(40, 40, 40)"),
        "sso-label": color("#0000004d", "Computed SSO button text rgba(0, 0, 0, 0.3)"),
        "link": color("#2c2c2c", "Computed sign-in legal link color rgb(44, 44, 44), underline"),
    }

    dark = {
        "page": color("#2c2c2c", D + " --color-bg var(--ramp-grey-800)."),
        "surface": color("#1e1e1e", D + " --color-bg-elevated var(--ramp-grey-900)."),
        "surface-secondary": color("#383838", D + " --color-bg-secondary var(--ramp-grey-700)."),
        "surface-tertiary": color("#444444", D + " --color-bg-tertiary var(--ramp-grey-600)."),
        "text": color("#ffffff", D + " --color-text var(--ramp-white-1000)."),
        "text-secondary": color("#ffffffb2", D + " --color-text-secondary var(--ramp-white-500)."),
        "text-tertiary": color("#ffffff66", D + " --color-text-tertiary var(--ramp-white-400)."),
        "text-disabled": color("#ffffff66", D + " --color-text-disabled var(--ramp-white-400)."),
        "text-brand": color("#80caff", D + " --color-text-brand var(--ramp-blue-400)."),
        "text-danger": color("#ffafa3", D + " --color-text-danger var(--ramp-red-400)."),
        "text-success": color("#8ddda4", D + " --color-text-success var(--ramp-green-400)."),
        "text-warning": color("#ffd966", D + " --color-text-warning var(--ramp-yellow-400)."),
        "on-brand": color("#ffffff", D + " --color-text-onbrand var(--ramp-white-1000)."),
        "border": color("#444444", D + " --color-border var(--ramp-grey-600)."),
        "border-strong": color("#ffffffe5", D + " --color-border-strong var(--ramp-white-800)."),
        "border-selected": color("#0d99ff", D + " --color-border-selected var(--ramp-blue-500)."),
        "brand": color("#0d99ff", D + " --color-bg-brand stays var(--ramp-blue-500)."),
        "danger": color("#f24822", D + " --color-bg-danger stays var(--ramp-red-500)."),
        "success": color("#14ae5c", D + " --color-bg-success stays var(--ramp-green-500)."),
        "warning": color("#ffcd29", D + " --color-bg-warning stays var(--ramp-yellow-500)."),
    }

    shadow = {
        "card": {
            "$type": "shadow",
            "$value": [
                {"color": "#00000026", "offsetX": "0px", "offsetY": "1px", "blur": "3px", "spread": "0px"},
                {"color": "#0000004d", "offsetX": "0px", "offsetY": "0px", "blur": "0.5px", "spread": "0px"},
            ],
            "$extensions": {
                "source": "Computed sign-in card box-shadow rgba(0, 0, 0, 0.15) 0px 1px 3px 0px, rgba(0, 0, 0, 0.3) 0px 0px 0.5px 0px (raw/readings.json); matches declared --elevation-100. Both layers."
            },
        }
    }

    doc = {
        "$description": "Weavy public marketing (now Figma Weave at weave.figma.com) and the signed-out app.weavy.ai/signin page. Measured 2026-11-19.",
        "core": core,
        "light": {
            "color": {"marketing": marketing, "app": light},
            "shadow": shadow,
        },
        "dark": {"color": {"app": dark}},
        "$themes": [
            {"id": "light", "name": "Light", "selectedTokenSets": {"core": "enabled", "light": "enabled"}},
            {"id": "dark", "name": "Dark", "selectedTokenSets": {"core": "enabled", "dark": "enabled"}},
        ],
        "$metadata": {"tokenSetOrder": ["core", "light", "dark"]},
    }
    label_hand_entries(doc)
    check(doc)
    return doc


# Declared ramp values that raw/readings.json does not hold: the dark app set beyond the roles
# whose hex the readings contain, and the light status fills. They were typed in from the stylesheet.
HAND = {
    "light": ["danger", "success", "warning"],
    "dark": ["surface", "surface-secondary", "surface-tertiary", "text-brand", "text-danger", "text-success",
             "text-warning", "border", "danger", "success", "warning"],
}


def label_hand_entries(doc):
    for theme, keys in HAND.items():
        for key in keys:
            token = doc[theme]["color"]["app"][key]
            token["$extensions"]["source"] = (
                "Reconstruction: entered by hand at capture time; no raw/ file holds this reading. "
                + token["$extensions"]["source"]
            )


def walk(node, path=""):
    for key, value in node.items():
        if key.startswith("$") or not isinstance(value, dict):
            continue
        if "$value" in value:
            yield f"{path}{key}", value
        else:
            yield from walk(value, f"{path}{key}.")


def check(doc):
    """Refuse a token with no source, a colour that is not hex, or an alias that resolves nowhere
    (own set first, then core)."""
    problems = []
    sets = [s for s in ("core", "light", "dark") if s in doc]
    flat = {s: dict(walk(doc[s])) for s in sets}
    for s in sets:
        for path, token in flat[s].items():
            if not token.get("$extensions", {}).get("source"):
                problems.append(f"{s}.{path}: no source")
            values = token["$value"] if isinstance(token["$value"], list) else [token["$value"]]
            for v in values:
                parts = v.values() if isinstance(v, dict) else [v]
                for part in parts:
                    if isinstance(part, str) and part.startswith("{"):
                        ref = part[1:-1]
                        if ref not in flat[s] and ref not in flat["core"]:
                            problems.append(f"{s}.{path}: alias {part} resolves nowhere")
            if token["$type"] == "color" and not str(token["$value"]).startswith("{"):
                if not re.fullmatch(r"#[0-9a-f]{6}([0-9a-f]{2})?", token["$value"]):
                    problems.append(f"{s}.{path}: colour {token['$value']!r} is not hex")
    if problems:
        raise SystemExit("token check failed:\n" + "\n".join(problems))


if __name__ == "__main__":
    out = ROOT / "tokens.json"
    out.write_text(json.dumps(build(), indent=2) + "\n")
    print(f"wrote {out}")
