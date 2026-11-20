#!/usr/bin/env python3
"""Build tokens.json from the Zendesk public capture.

Sources, read on 2026-11-19 from live computed styles (raw/components-computed.json)
and the :root custom properties in raw/css-vars.json. The marketing site is
styled-components: colours are computed, spacing and radius are declared.

The public surfaces paint one light theme. A dark hero (rgb(17, 17, 13)) sits
on a white page. There is no dark theme switch. Deterministic.
"""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"


def color(value, source):
    return {"$value": value, "$type": "color", "$extensions": {"source": source}}


def dim(value, source):
    return {"$value": value, "$type": "dimension", "$extensions": {"source": source}}


def font_family(value, source):
    return {"$value": value, "$type": "fontFamily", "$extensions": {"source": source}}


def num(value, source):
    return {"$value": value, "$type": "number", "$extensions": {"source": source}}


def shadow(value, source):
    return {"$value": value, "$type": "shadow", "$extensions": {"source": source}}


def cubic(value, source):
    return {"$value": value, "$type": "cubicBezier", "$extensions": {"source": source}}


def duration(value, source):
    return {"$value": value, "$type": "duration", "$extensions": {"source": source}}


def typography(family, weight, size, line, source, letter=None):
    value = {
        "fontFamily": family,
        "fontWeight": weight,
        "fontSize": size,
        "lineHeight": line,
    }
    if letter:
        value["letterSpacing"] = letter
    return {"$value": value, "$type": "typography", "$extensions": {"source": source}}


S_HOME = "computed on https://www.zendesk.com/sg/ at 1440x900, 2026-11-19 (raw/components-computed.json)"
S_VAR = "declared on :root in the marketing stylesheet, 1440 breakpoint (raw/css-vars.json)"
S_LOGIN = "computed on https://www.zendesk.com/sg/login/, 2026-11-19"
S_PRICE = "computed on https://www.zendesk.com/sg/pricing/, 2026-11-19"
S_REG = "computed on https://www.zendesk.com/sg/register/, 2026-11-19, form not submitted"
S_HELP = "computed on https://support.zendesk.com/hc/en-us, 2026-11-19"

core = {
    "font": {
        "family": {
            "sans": font_family(
                "Vanilla Sans, Arial, sans-serif",
                "computed font-family on body and every measured control, " + S_HOME,
            ),
        }
    },
    "typography": {
        "display": typography("{core.font.family.sans}", "500", "68px", "71.4px",
                               "h1 'Build for better outcomes', " + S_HOME),
        "heading": typography("{core.font.family.sans}", "500", "42px", "48.3px",
                               "section h2 and login h1, " + S_HOME),
        "title": typography("{core.font.family.sans}", "500", "26px", "32.5px",
                             "feature h3, " + S_HOME),
        "eyebrow": typography("{core.font.family.sans}", "700", "14px", "18.2px",
                               "uppercase eyebrow, letter-spacing 0.75px, " + S_HOME,
                               letter="0.75px"),
        "body": typography("{core.font.family.sans}", "400", "16px", "23.2px",
                            "hero lede, " + S_HOME),
        "label": typography("{core.font.family.sans}", "600", "16px", "23px",
                             "nav primary button, " + S_HOME),
        "button": typography("{core.font.family.sans}", "600", "18px", "28px",
                              "hero and login submit, 48px tall, " + S_HOME),
        "field": typography("{core.font.family.sans}", "400", "15px", "21px",
                             "email and subdomain inputs, " + S_HOME),
        "price": typography("{core.font.family.sans}", "600", "20px", "28px",
                             "plan price 'US$ 19', " + S_PRICE),
    },
    "radius": {
        "field": dim("12px", "email, subdomain and contact fields, " + S_HOME),
        "button": dim("16px", "primary and secondary buttons, " + S_HOME),
        "card": dim("40px", "pricing plan card, " + S_PRICE),
        "badge": dim("40px", "MOST POPULAR badge, " + S_PRICE),
        "pill": dim("100px", "help-centre Free trial and search, " + S_HELP),
        "root-desktop": dim("20px", S_VAR + "; --radius at min-width 1150px. Controls use 12px and 16px instead."),
    },
    "space": {
        "text-sm": dim("8px", "--space-textMarginSm, " + S_VAR),
        "text-md": dim("16px", "--space-textMarginMd at min-width 768px, " + S_VAR),
        "text-lg": dim("24px", "--space-textMarginLg, " + S_VAR),
        "content-sm": dim("24px", "--space-contentMarginSm, " + S_VAR),
        "content-md": dim("40px", "--space-contentMarginMd at min-width 768px, " + S_VAR),
        "content-lg": dim("48px", "--space-contentMarginLg at min-width 0, " + S_VAR),
        "section": dim("88px", "--space-sectionPadding at min-width 1150px, " + S_VAR),
        "page": dim("16px", "--space-globalPadding, " + S_VAR),
        "button-x": dim("20px", "submit padding-left/right, " + S_HOME),
        "button-y": dim("10px", "submit padding-top/bottom, " + S_HOME),
        "field": dim("12px", "input padding, " + S_HOME),
    },
    "size": {
        "control": dim("48px", "email field and hero submit height, " + S_HOME),
        "nav-button": dim("43px", "nav Try it for free height, " + S_HOME),
        "header": dim("115px", "--headerHeight at min-width 1150px, matching the 1440 capture; 65px below that breakpoint, " + S_VAR),
        "content": dim("1150px", "--contentWidth at min-width 1150px, " + S_VAR),
        "content-wide": dim("1600px", "--contentWidth at min-width 1600px, " + S_VAR),
    },
    "stroke": {
        "field": dim("1px", "inset ring on resting fields, " + S_LOGIN),
        "focus": dim("2px", "inset ring on focused fields and the focus outline, " + S_HOME),
    },
    "motion": {
        "duration": {
            "button": duration("600ms", "transition-duration 0.6s on primary buttons, " + S_HOME),
            "field": duration("250ms", "transition-duration 0.25s on the email field, " + S_HOME),
        },
        "easing": {
            "button": cubic([0.7, 0, 0.3, 1], "cubic-bezier(0.7, 0, 0.3, 1) on primary buttons, " + S_HOME),
            "field": cubic([0.42, 0, 0.58, 1], "ease-in-out keyword on the email field, expanded, " + S_HOME),
        },
    },
}

light = {
    "surface": {
        "page": color("#ffffff", "body background-color rgb(255, 255, 255), " + S_HOME),
        "hero": color("#11110d", "hero section background rgb(17, 17, 13), " + S_HOME),
        "forest": color("#203524", "report band background rgb(32, 53, 36), " + S_HOME),
        "raised": color("#11110d0d", "pricing card and resting subdomain field rgba(17, 17, 13, 0.05), " + S_PRICE),
        "card": color("#ffffff", "trial dialog background, " + S_REG),
    },
    "text": {
        "primary": color("#11110d", "nav, headings on white, field text rgb(17, 17, 13), " + S_HOME),
        "on-hero": color("#f5f5f2", "hero display and eyebrow rgb(245, 245, 242), " + S_HOME),
        "on-hero-body": color("#ffffff", "hero lede rgb(255, 255, 255), " + S_HOME),
        "inverse": color("#ffffff", "badge text and hero-submit text, " + S_PRICE),
        "muted": color("#11110db6", "rgba(17, 17, 13, 0.714) on secondary copy, colour frequency on the homepage, " + S_HOME),
        "link": color("#11110d", "the Sign in to Chat product link, computed color rgb(17, 17, 13) "
                      "(raw/components-computed.json controls.login.productLink), " + S_LOGIN),
    },
    "border": {
        "default": color("#d5d5d2", "email inset ring rgb(213, 213, 210), " + S_HOME),
        "strong": color("#11110d78", "subdomain inset ring rgba(17, 17, 13, 0.47), " + S_LOGIN),
        "focus": color("#11110d", "focused field inset ring rgb(17, 17, 13), " + S_HOME),
    },
    "accent": {
        "default": color("#d1f470", "primary button fill rgb(209, 244, 112), " + S_HOME),
        "text": color("#70a32a", "pricing accent text rgb(112, 163, 42), " + S_PRICE),
        "hover": color("#d1f470", "forced :hover keeps the same fill; text opacity changes. " + S_LOGIN),
        "pressed": color("#d1f470", "forced :active keeps the same fill. " + S_LOGIN),
    },
    "status": {
        "danger": color("#b84242", "register field error inset ring rgb(184, 66, 66) with aria-invalid=true, before typing, " + S_REG),
    },
    "component": {
        "button-primary": {
            "background": color("{light.accent.default}", "nav and login primary, " + S_HOME),
            "text": color("{light.text.primary}", "nav Try it for free and login Sign in text, " + S_HOME),
            "radius": dim("{core.radius.button}", "16px on primary buttons"),
            "height": dim("{core.size.control}", "48px on the hero and login submits"),
        },
        "button-on-hero": {
            "background": color("{light.accent.default}", "hero submit fill, " + S_HOME),
            "text": color("{light.text.inverse}", "hero submit text is white, unlike the nav primary, " + S_HOME),
            "radius": dim("{core.radius.button}", "16px"),
            "height": dim("{core.size.control}", "48px"),
        },
        "field": {
            "background": color("{light.surface.page}", "hero email field is white; login and contact fields use raised, " + S_HOME),
            "text": color("{light.text.primary}", "field text, " + S_HOME),
            "radius": dim("{core.radius.field}", "12px"),
            "height": dim("{core.size.control}", "48px"),
        },
        "badge": {
            "background": color("{light.surface.hero}", "MOST POPULAR fill, " + S_PRICE),
            "text": color("{light.text.inverse}", "MOST POPULAR text, " + S_PRICE),
            "radius": dim("{core.radius.badge}", "40px"),
        },
    },
}

themes = [{
    "id": "light",
    "name": "Light",
    "selectedTokenSets": {"core": "source", "light": "enabled"},
    "$description": "The only theme the public marketing site, login, pricing, register and help centre paint. No dark class or prefers-color-scheme repaint was found.",
}]

doc = {
    "$description": "Zendesk public signed-out surfaces, measured 2026-11-19. Marketing, login, pricing, register (not submitted), help centre. Garden is a separate site and is not in these tokens.",
    "core": core,
    "light": light,
    "$themes": themes,
}



def render():
    """tokens.json's exact text; importing this module writes nothing."""
    return json.dumps(doc, indent=2) + "\n"


if __name__ == "__main__":
    out = HERE / "tokens.json"
    out.write_text(render())
    print("wrote", out, "bytes", out.stat().st_size)
