#!/usr/bin/env python3
"""Build tokens.json from the measured Promova readings in raw/.

Every value below was read from computed styles on promova.com on 2026-11-19
(signed out). The mapping is the product-specific part; the checks are generic.
Edit the readings, then rerun this script. Do not hand-edit tokens.json.
"""
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"

# Measured computed colours. Sources are named in each token's $extensions.source.
# Page ground is body backgroundColor #000000. Section islands and the nav bar
# sit on that black with a 20px gutter at 1440.

def color(value, source, description):
    return {
        "$value": value,
        "$type": "color",
        "$extensions": {"source": source},
        "$description": description,
    }


def dim(value, source, description):
    return {
        "$value": value,
        "$type": "dimension",
        "$extensions": {"source": source},
        "$description": description,
    }


def font(value, source, description):
    return {
        "$value": value,
        "$type": "fontFamily",
        "$extensions": {"source": source},
        "$description": description,
    }


def text_style(family, size, weight, line_height, source, description, letter_spacing=None):
    value = {
        "fontFamily": family,
        "fontSize": size,
        "fontWeight": weight,
        "lineHeight": line_height,
    }
    if letter_spacing:
        value["letterSpacing"] = letter_spacing
    return {
        "$value": value,
        "$type": "typography",
        "$extensions": {"source": source},
        "$description": description,
    }


S_BODY = "computed backgroundColor of body on https://promova.com/ at 1440x900 (raw/nav.json, raw/harvest.json)"
S_NAV = "computed backgroundColor of .landing_navigation__navigation__mSH6vN (raw/nav.json)"
S_HERO = "computed backgroundColor of section.hero_section_concept5__section__kNr4Qo (raw/harvest.json)"
S_BTN = "computed backgroundColor of a.navigation_actions__main_button__KANxM7 (raw/nav.json)"
S_SIGN = "computed styles of https://promova.com/sign-up form (raw/signup.json)"
S_VARS = "computed custom properties on :root at https://promova.com/ (preview evaluate, 2026-11-19)"
HAND = "Reconstruction: entered by hand at capture time; no reading in raw/ holds it"
S_HOVER = HAND + " (stylesheet rule .navigation_actions__login__zl9Mva:hover and :active, and .navigation_actions__main_button__KANxM7:hover and :active, read in the preview browser; raw/extra.json rules is empty)"

core = {
    "color": {
        "black": color("#000000", S_BODY, "Declared --black and the painted page ground."),
        "white": color("#ffffff", S_NAV, "Declared --white. Nav bar, cards, footer, field fill."),
        "ink": {
            "30": color("rgba(0, 0, 0, 0.3)", "computed border-top-color of input.input__input__0C3wAo (raw/signup.json)", "Field hairline and muted ink at 30%."),
            "50": color("rgba(0, 0, 0, 0.5)", HAND + " (the sign-up hint 'Minimum 6 characters' and the 'or' divider, read in the preview browser)", "Hint and divider ink."),
        },
        "gray": {
            "100": color("#f5f5f5", "computed backgroundColor of section.what-you-get-concept8 (raw/harvest.json); its use as the SIGN UP hover wash is " + S_HOVER, "SIGN UP hover wash, and the 'Why Promova' section."),
            "200": color("#e0e0e0", S_HOVER, "SIGN UP pressed wash."),
            "300": color("#eeeeee", S_SIGN, "Sign-up page ground."),
            "400": color("#f4f4f4", "computed backgroundColor of the FAQ section (raw/harvest.json)", "FAQ section ground."),
        },
        "ink-hover": color("#262626", S_HOVER, "GET STARTED hover, rgb(38, 38, 38)."),
        "ink-pressed": color("#404040", S_HOVER, "GET STARTED pressed, rgb(64, 64, 64)."),
        "lavender": color("#bec8ff", S_HERO, "Home hero section."),
        "lavender-soft": color("#dfe3ff", "computed backgroundColor of .cta_modal__main_block__SiOPXk (preview evaluate)", "Entry promo modal."),
        "lilac": color("#d7d4e2", "computed backgroundColor of the language-picker block (raw/harvest.json)", "Language picker block."),
        "yellow": color("#fff584", "computed announcement-bar fill, visible in screenshots/home and the header crop", "Announcement strip."),
        "yellow-soft": color("#fff8a7", "computed backgroundColor of the 93% confidence section (raw/harvest.json)", "Confidence statistic section."),
        "mint": color("#bcf0d0", "computed backgroundColor of the quote section (raw/harvest.json)", "Quote section."),
        "lime": color("#e3efc3", "computed backgroundColor of the 'How to get started' left column (raw/harvest.json)", "Get-started column."),
        "lime-soft": color("#eef5db", "computed backgroundColor of the 'How to get started' right column (raw/harvest.json)", "Get-started companion column."),
        "blush": color("#f5a3d0", "computed backgroundColor of the awards section (raw/harvest.json)", "Awards section."),
        "sand": color("#ebe0d3", "computed backgroundColor of the resources section (raw/harvest.json)", "Resources and links section."),
        "ice": color("#f2f4ff", "computed backgroundColor of the reviews section (raw/harvest.json)", "Reviews section."),
        "progress": color("#fffd00", HAND + " (declared --bprogress-color on :root, read in the preview browser)", "Route-progress bar. Not a brand accent."),
    },
    "font": {
        "family": {
            "display": font(
                "nekst, Rubik, Arial, Lucida Grande, -apple-system, BlinkMacSystemFont, sans-serif",
                S_VARS + " --heading-font / --nekst-font",
                "Display and button face. Computed as nekst / Nekst.",
            ),
            "ui": font(
                "manrope, Manrope, Rubik, Arial, Lucida Grande, -apple-system, BlinkMacSystemFont, sans-serif",
                S_VARS + " --body-font / --manrope-font",
                "Body face. Computed as manrope / Manrope.",
            ),
        },
        "size": {
            "nav": dim("14px", "computed font-size of SIGN UP and GET STARTED (raw/nav.json)", "Nav actions."),
            "body-2": dim("15px", S_VARS + " --body2-font-size; also field text", "Fields and nav triggers."),
            "body": dim("16px", "derived: raw/ holds no reading of body itself; the nav header, which inherits the body face, computes 16px (raw/nav.json header)", "Body."),
            "body-1": dim("18px", S_VARS + " --body1-font-size; filled CTA", "Filled CTA and footer links."),
            "hero-phone": dim("50px", "computed font-size of h1 at 390px (raw/harvest.json mobile-home)", "Hero title on the phone width."),
            "course": dim("60px", "computed font-size of h1 on /learn-english-online (raw/harvest.json)", "Course-page title."),
            "display": dim("70px", "computed font-size of h1 on / at 1440 (raw/nav.json)", "Home hero and statistic numerals."),
            "auth-title": dim("35px", "computed font-size of h3.yK4sDq_title on /sign-up (raw/signup.json)", "Sign-up title."),
        },
    },
    "typography": {
        "display": text_style("{core.font.family.display}", "70px", 700, "70px", "computed h1 on / at 1440 (raw/harvest.json)", "Home hero title."),
        "display-phone": text_style("{core.font.family.display}", "50px", 700, "50px", "computed h1 at 390 (raw/harvest.json)", "Home hero title at 390. Letter-spacing measured -1px."),
        "section": text_style("{core.font.family.display}", "24px", 400, "24px", "computed h2 on / (preview evaluate)", "Section titles, including the FAQ summary."),
        "body": text_style("{core.font.family.ui}", "16px", 400, "26px", "derived: raw/ holds no reading of body itself; the nav header, which inherits the body face, computes manrope 16px 400 (raw/nav.json header). The 26px line height is " + HAND + " (--body1-line-height, declared at 18px; body itself computes 16px/normal)", "Default body. Line-height token uses the declared body1 step."),
        "body-lg": text_style("{core.font.family.ui}", "24px", 400, "34px", "manrope 24px 400 in raw/harvest.json fonts; the 34px line height of p.hero_section_concept5__description__ZIW-SC is " + HAND, "Hero lede."),
        "nav": text_style("{core.font.family.display}", "15px", 400, "18px", "computed button.navigation_list__navmenu_trigger (preview evaluate)", "Nav triggers."),
        "button": text_style("{core.font.family.display}", "18px", 700, "18px", "computed TRY NOW (preview evaluate): 18px/700, line-height 18px, letter-spacing 0.72px, uppercase", "Filled CTA."),
        "field": text_style("{core.font.family.ui}", "15px", 500, "22px", S_SIGN, "Email and password fields."),
        "auth-title": text_style("{core.font.family.display}", "35px", 400, "35px", S_SIGN, "Join Promova title."),
    },
    "radius": {
        "none": dim("0px", "computed border-radius of filled and outlined marketing buttons (raw/harvest.json). The shell carries pGCWia_square_buttons.", "Marketing buttons are square."),
        "field": dim("5px", S_SIGN + " and the blog search field", "Text fields and the message textarea."),
        "auth-button": dim("10px", "computed border-radius of button._GUtPG_filled on /sign-up (raw/signup.json)", "Sign-up submit. Marketing CTAs stay at 0."),
        "card-phone": dim("20px", "computed section border-radius at 390 (raw/harvest.json mobile-home)", "Section islands on the phone width."),
        "auth-card": dim("20px", "computed border-radius of .sG6Sda_form_container (raw/signup.json)", "Sign-up card."),
        "section": dim("30px", "computed border-radius of the nav bar and home sections at 1440 (raw/nav.json)", "Nav, hero, sections, footer."),
    },
    "spacing": {
        "gutter": dim("20px", "section.getBoundingClientRect().x at 1440 (raw/nav.json gutter.x)", "Inset of the nav and sections from the viewport edge."),
        "nav-pad": dim("30px", "computed padding of the nav bar, 0px 30px (raw/nav.json)", "Nav horizontal padding."),
        "field-pad": dim("20px", "computed padding-left of the email field (raw/signup.json)", "Field horizontal padding."),
        "section-pad": dim("60px", "computed padding of the numbers section (preview evaluate)", "Numbers section padding."),
        "auth-card-pad": dim("15px", "computed padding of .sG6Sda_form_container (raw/signup.json)", "Sign-up card padding."),
        "modal-pad": dim("30px", "computed padding of .cta_modal__main_block (preview evaluate)", "Entry promo padding."),
    },
    "motion": {
        "nav-hover": {
            "$value": "0.2s",
            "$type": "duration",
            "$extensions": {"source": "computed transition-duration opacity 0.2s ease-out on nav triggers (preview evaluate)"},
            "$description": "Nav trigger opacity.",
        },
        "button": {
            "$value": "0.25s",
            "$type": "duration",
            "$extensions": {"source": "computed transition background-color 0.25s ease-in-out on .PEtu1G_btn_filled (preview evaluate)"},
            "$description": "Filled CTA background repaint.",
        },
        "page": {
            "$value": "0.5s",
            "$type": "duration",
            "$extensions": {"source": HAND + " (transition 0.5s background-color on body, read in the preview browser)"},
            "$description": "Body background transition. The black ground does not animate between the captured routes.",
        },
    },
}

light = {
    "background": {
        "page": color("{core.color.black}", S_BODY, "Page ground. Painted on body, not on html."),
        "surface": color("{core.color.white}", S_NAV, "Nav, cards, footer, field fill."),
        "hero": color("{core.color.lavender}", S_HERO, "Home hero island."),
        "muted": color("{core.color.gray.100}", "computed backgroundColor of the Why Promova section (raw/harvest.json)", "Neutral section island."),
        "auth": color("{core.color.gray.300}", S_SIGN, "Sign-up page ground."),
        "action": color("{core.color.black}", S_BTN, "Filled button."),
        "action-hover": color("{core.color.ink-hover}", S_HOVER, "Filled nav button hover."),
        "action-pressed": color("{core.color.ink-pressed}", S_HOVER, "Filled nav button pressed."),
        "announcement": color("{core.color.yellow}", "announcement strip in the header crop", "Top announcement strip."),
    },
    "text": {
        "primary": color("{core.color.black}", "computed color of h1 and body (raw/nav.json)", "Ink on white and on the pastel islands."),
        "on-action": color("{core.color.white}", "computed color of GET STARTED (raw/nav.json)", "Ink on the filled button."),
        "secondary": color("{core.color.ink.50}", HAND + " (the sign-up hint, read in the preview browser)", "Hints and the 'or' divider."),
        "muted": color("{core.color.ink.30}", "computed color used at 30% black on fields and disabled-looking chrome", "30% ink. Used as the field border; text at this step was not a separate computed color on body copy."),
    },
    "border": {
        "stroke": color("{core.color.ink.30}", S_SIGN, "Field border, 1px solid rgba(0,0,0,0.3)."),
        "strong": color("{core.color.black}", "computed border of SIGN UP (1px solid #000) and the FAQ item (1px #000) (raw/harvest.json, raw/extra.json)", "Outlined controls and FAQ rules."),
    },
    "component": {
        "button": {
            "nav": {
                "height": dim("40px", "computed height of SIGN UP and GET STARTED (raw/nav.json)", "Nav actions."),
                "padding": dim("10px", "computed padding 0px 10px (raw/nav.json)", "Nav action horizontal padding."),
                "radius": dim("{core.radius.none}", "computed border-radius 0px (raw/nav.json)", "Square."),
                "font-size": dim("14px", "computed font-size (raw/nav.json)", "Nav action type."),
            },
            "cta": {
                "height": dim("60px", "computed height of TRY NOW (preview evaluate)", "Marketing filled CTA."),
                "radius": dim("{core.radius.none}", "computed border-radius 0px", "Square, from pGCWia_square_buttons."),
                "font-size": dim("18px", "computed font-size of TRY NOW", "CTA type."),
            },
            "auth": {
                "height": dim("60px", S_SIGN, "SIGN UP submit."),
                "radius": dim("{core.radius.auth-button}", S_SIGN, "10px, unlike the marketing squares."),
                "font-size": dim("18px", S_SIGN, "Submit type."),
            },
            "oauth": {
                "height": dim("50px", "computed height of Sign up with Google (preview evaluate)", "Google and Apple buttons."),
                "radius": dim("{core.radius.none}", "computed border-radius 0px", "Square, 1px solid #000."),
            },
        },
        "field": {
            "height": dim("50px", S_SIGN, "Email and password."),
            "radius": dim("{core.radius.field}", S_SIGN, "5px."),
            "padding": dim("20px", S_SIGN, "Horizontal padding. Password adds 50px on the right for the visibility icon."),
        },
        "nav": {
            "height": dim("100px", "computed height of the white nav bar (raw/nav.json)", "Desktop nav."),
            "radius": dim("{core.radius.section}", "computed border-radius 30px (raw/nav.json)", "Nav island."),
            "inset": dim("{core.spacing.gutter}", "nav x = 20 at 1440 (raw/nav.json)", "Inset from the viewport."),
        },
        "card": {
            "auth-radius": dim("{core.radius.auth-card}", S_SIGN, "Sign-up card."),
            "section-radius": dim("{core.radius.section}", S_HERO, "Marketing section islands."),
        },
    },
}

core["$extensions"] = {"notTokenised": [
    {"name": "radius.round", "value": "50%",
     "why": "a percentage, not one px or rem length; the promo close control button.qkTZoW_close_button, read in the preview browser (raw/harvest.json radii lists 50%)"},
]}


def build():
    """The token document, checked, without writing it."""
    doc = {
        "core": core,
        "light": light,
        "$themes": [
            {
                "id": "light",
                "name": "light",
                "selectedTokenSets": {"core": "source", "light": "enabled"},
            }
        ],
        "$metadata": {
            "tokenSetOrder": ["core", "light"],
        },
    }
    walk(doc["core"])
    walk(doc["light"])
    return json.loads(json.dumps(doc))


DIM = re.compile(r"-?\d+(\.\d+)?(px|rem)")


def check(path, node):
    ty = node.get("$type")
    val = node.get("$value")
    if isinstance(val, str) and val.startswith("{"):
        return
    if ty == "color":
        if not (isinstance(val, str) and (val.startswith("#") or val.startswith("rgb"))):
            raise ValueError(f"{path}: colour {val!r}")
    if ty == "dimension" and not (isinstance(val, str) and DIM.fullmatch(val)):
        raise ValueError(f"{path}: dimension {val!r}")
    if ty == "typography":
        for key in ("fontFamily", "fontSize", "fontWeight", "lineHeight"):
            if key not in val:
                raise ValueError(f"{path}: typography missing {key}")
    if "$extensions" not in node or "source" not in node["$extensions"]:
        raise ValueError(f"{path}: missing source")


def walk(node, path=""):
    if isinstance(node, dict) and "$value" in node:
        check(path, node)
        return
    if isinstance(node, dict):
        for k, v in node.items():
            if k.startswith("$"):
                continue
            walk(v, f"{path}.{k}" if path else k)


def main():
    out = HERE / "tokens.json"
    out.write_text(json.dumps(build(), indent=2) + "\n")
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
