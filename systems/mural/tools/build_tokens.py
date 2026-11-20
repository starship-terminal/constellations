#!/usr/bin/env python3
"""Build tokens.json from the Mural public-site readings.

Sources, read on 2026-11-19 from https://www.mural.co/ and the signed-out
https://app.mural.co/signin page, light only, 1440 CSS px:

  raw/css-vars.json              custom properties resolved on :root
  raw/components-computed.json   computed styles of the controls that were measured
  raw/components-extra.json      navbar pill, hero email, pricing card, focus ring

Mural publishes one light theme on these surfaces. The marketing hero is a
black canvas; the rest of the site and the auth pages are a white page. There
is no dark theme switch on the pages that were opened, so this file has no
dark set. Every token carries $extensions.source. Re-running on the same
inputs writes the same bytes.
"""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
V = json.loads((RAW / "css-vars.json").read_text())
RES = V["resolved"]

SRC_ROOT = "Measured. Custom property on :root of https://www.mural.co/, resolved by the browser, 1440 CSS px, light, 2026-11-19."
SRC_COMPUTED = "Measured. Computed style on a signed-out page, 1440 CSS px, light, 2026-11-19."


def color(value, source):
    return {"$type": "color", "$value": value, "$extensions": {"source": source}}


def dim(value, source):
    return {"$type": "dimension", "$value": value, "$extensions": {"source": source}}


def font(family, size, weight, line, tracking, source):
    return {
        "$type": "typography",
        "$value": {
            "fontFamily": family,
            "fontSize": size,
            "fontWeight": weight,
            "lineHeight": line,
            "letterSpacing": tracking,
        },
        "$extensions": {"source": source},
    }


def shadow(layers, source):
    return {"$type": "shadow", "$value": layers, "$extensions": {"source": source}}


def var(name):
    if name not in RES:
        raise SystemExit("missing custom property " + name)
    return RES[name]


def hex_of(value):
    named = {"black": "#000000", "white": "#ffffff"}
    v = value.strip().lower()
    if v in named:
        return named[v]
    if v.startswith("#") and len(v) == 4:
        return "#" + "".join(c * 2 for c in v[1:])
    return v


# Named brand colours declared on :root. Two greens disagree: the old --mint
# is #b4f5c8 and the primitive --_primitives---color--mint is #b4f5c0. Both
# are kept, under the names the stylesheet uses.
PALETTE = {
    "black": "--_primitives---color--black",
    "white": "--_primitives---color--white",
    "grey100": "--_primitives---color--grey-100",
    "grey200": "--_primitives---color--grey-200",
    "grey500": "--_primitives---color--grey-500",
    "grey700": "--_primitives---color--grey-700",
    "grey900": "--_primitives---color--grey-900",
    "mint": "--_primitives---color--mint",
    "jade": "--_primitives---color--jade",
    "spring": "--_primitives---color--spring",
    "muralBlue": "--_primitives---color--mural-blue",
    "muralGreen": "--_primitives---color--mural-green",
    "muralPink": "--_primitives---color--mural-pink",
    "lemon": "--lemon",
    "natural": "--natural",
    "lavender": "--lavender",
    "ice": "--ice",
    "sky": "--sky",
    "indigo": "--indigo",
    "violet": "--violet",
    "grape": "--grape",
    "blush": "--blush",
    "flamingo": "--flamingo",
    "burgundy": "--burgundy",
    "orange": "--orange",
    "canary": "--canary",
    "muralRed": "--mural-red",
    "muralYellow": "--mural-yellow",
    "lightGrey": "--lightgrey",
    "grey": "--grey",
}

core_color = {}
for key, prop in PALETTE.items():
    core_color[key] = color(hex_of(var(prop)), SRC_ROOT + " " + prop + " = " + var(prop) + ".")

# Computed colours that are not a :root custom property.
core_color["heroMuted"] = color("#8c8c8c", SRC_COMPUTED + " h1.home_hero-h1 color rgb(140, 140, 140) on the home hero. The stylesheet also declares --grey: #8c8c8c.")
core_color["authText"] = color("#1b1f22", SRC_COMPUTED + " input#work-email-input color rgb(27, 31, 34) on app.mural.co/signin.")
core_color["authPlaceholder"] = color("#63707e", SRC_COMPUTED + " ::placeholder on input#work-email-input, rgb(99, 112, 126).")
core_color["authBorder"] = color("#282e34", SRC_COMPUTED + " input#work-email-input border-top-color rgb(40, 46, 52).")
core_color["authPage"] = color("#f9fafa", SRC_COMPUTED + " .page.redesign-p2-container background rgb(249, 250, 250) on app.mural.co/signin.")
core_color["authRed"] = color("#e02935", SRC_COMPUTED + " the Log in button background rgb(224, 41, 53) on app.mural.co/signin.")
core_color["authRedHover"] = color("#b3212a", SRC_COMPUTED + " the Log in button background on hover, rgb(179, 33, 42).")
core_color["authFocus"] = color("#306ae3", SRC_COMPUTED + " outline-color on input#work-email-input after keyboard focus, rgb(48, 106, 227) solid 2px.")
core_color["authLink"] = color("#48525b", SRC_COMPUTED + " the Sign up for free link color rgb(72, 82, 91).")
core_color["heroFieldBorder"] = color("#4f5457", SRC_COMPUTED + " the home hero email field border rgb(79, 84, 87), the same hex as --_primitives---color--grey-700.")

spacing = {
    "0": dim("0px", SRC_ROOT + " --_primitives---space--space-0 = 0rem."),
    "4": dim("4px", SRC_ROOT + " --_spacing-old---spacing--2xs = 0.25rem."),
    "8": dim("8px", SRC_ROOT + " --_spacing-old---spacing--xs = 0.5rem."),
    "12": dim("12px", SRC_ROOT + " --_semantics---space--spacer-0-75rem resolved to 0.75rem."),
    "16": dim("16px", SRC_ROOT + " --_spacing-old---spacing--sm = 1rem."),
    "20": dim("20px", SRC_ROOT + " --_semantics---space--spacer-1-25rem resolved to 1.25rem."),
    "24": dim("24px", SRC_ROOT + " --_spacing-old---spacing--nl = 1.5rem."),
    "28": dim("28px", SRC_ROOT + " --_semantics---space--spacer-1-75rem resolved to 1.75rem."),
    "32": dim("32px", SRC_ROOT + " --_spacing-old---spacing--md = 2rem."),
    "40": dim("40px", SRC_ROOT + " --_semantics---space--spacer-2-5rem = 2.5rem."),
    "48": dim("48px", SRC_ROOT + " --_spacing-old---spacing--lg = 3rem."),
    "64": dim("64px", SRC_ROOT + " --_spacing-old---spacing--xl = 4rem."),
    "80": dim("80px", SRC_ROOT + " --_primitives---space--space-5rem = 5rem."),
    "96": dim("96px", SRC_ROOT + " --_spacing-old---spacing--hg = 6rem."),
}

radius = {
    "sm": dim("4px", SRC_ROOT + " --_utilities---radius--sm = 0.25rem."),
    "button": dim("8px", SRC_ROOT + " --_semantics---radius--button-radius resolved to 0.5rem. Buttons and the email field measure 8px."),
    "md": dim("12px", SRC_ROOT + " --_utilities---radius--mdl = 0.75rem."),
    "nav": dim("16px", SRC_ROOT + " --_primitives---radius--radius-16 = 1rem. The navbar pill measures 16px."),
    "card": dim("20px", SRC_COMPUTED + " .pricing-card_content border-radius 20px. The token --_primitives---radius--radius-20 is 1.25rem."),
    "pill": dim("999px", SRC_ROOT + " --_semantics---radius--pill-radius resolved to 999rem, stored as 999px so a length token stays a length."),
}

core = {
    "color": core_color,
    "font": {
        "family": {
            "display": {"$type": "fontFamily", "$value": '"STK Bureau", "Times New Roman", sans-serif',
                        "$extensions": {"source": SRC_ROOT + " --_typography-old---type--stk-bureau. Proprietary. The declared stack, copied as written, falls back to Times New Roman, then sans-serif."}},
            "sans": {"$type": "fontFamily", "$value": "ABC Social, Arial, sans-serif",
                     "$extensions": {"source": SRC_ROOT + " --_typography-old---type--abc-social. Proprietary; the tokens fall back to Arial. The auth app computes the same face as abcsocial, sans-serif."}},
        }
    },
    "typography": {
        "display": font('"STK Bureau", "Times New Roman", sans-serif', "80px", 300, "88px", "-4px",
                        SRC_COMPUTED + " h1.home_hero-h1 on the home hero, 80px / 88px, weight 300, letter-spacing -4px."),
        "pageTitle": font('"STK Bureau", "Times New Roman", sans-serif', "64px", 300, "70.4px", "-3.2px",
                          SRC_COMPUTED + " the pricing h1, 64px / 70.4px, weight 300, letter-spacing -3.2px."),
        "cardTitle": font('"STK Bureau", "Times New Roman", sans-serif', "28px", 300, "28px", "-0.56px",
                          SRC_COMPUTED + " the first text node inside a pricing card, 28px, weight 300, letter-spacing -0.56px."),
        "body": font("ABC Social, Arial, sans-serif", "16px", 300, "24px", "0px",
                     SRC_COMPUTED + " body on www.mural.co, 16px / 24px, weight 300."),
        "lede": font("ABC Social, Arial, sans-serif", "18px", 300, "27px", "0px",
                     SRC_COMPUTED + " the home hero paragraph, 18px / 27px, weight 300, color white."),
        "ui": font("ABC Social, Arial, sans-serif", "16px", 500, "24px", "0px",
                   SRC_COMPUTED + " the Sign up free label, 16px, weight 500."),
        "eyebrow": font("ABC Social, Arial, sans-serif", "14px", 300, "15.4px", "3.5px",
                        SRC_COMPUTED + " h2.logos_h2, 14px, weight 300, letter-spacing 3.5px, uppercase."),
        "field": font("ABC Social, Arial, sans-serif", "14px", 400, "20px", "0px",
                      SRC_COMPUTED + " input#work-email-input, 14px / 20px, weight 400."),
        "buttonAuth": font("ABC Social, Arial, sans-serif", "14px", 700, "20px", "0px",
                           SRC_COMPUTED + " the Log in button label, 14px, weight 700."),
    },
    "spacing": spacing,
    "radius": radius,
    "shadow": {
        "elevated": shadow([
            {"color": "rgba(11, 41, 70, 0.32)", "offsetX": "0px", "offsetY": "0px", "blur": "1px", "spread": "0px"},
            {"color": "rgba(42, 82, 121, 0.08)", "offsetX": "0px", "offsetY": "24px", "blur": "20px", "spread": "0px"},
        ], SRC_ROOT + " --elevated-shadow, and the measured box-shadow of .navbar_inner."),
        "interactive": shadow([
            {"color": "rgba(0, 0, 0, 0.08)", "offsetX": "0px", "offsetY": "4px", "blur": "4px", "spread": "0px"},
        ], SRC_ROOT + " --interactive-shadow-default."),
        "interactiveHover": shadow([
            {"color": "rgba(0, 0, 0, 0.12)", "offsetX": "0px", "offsetY": "12px", "blur": "12px", "spread": "0px"},
        ], SRC_ROOT + " --interactive-shadow-hover."),
    },
    "layout": {
        "navHeight": dim("64px", SRC_COMPUTED + " .navbar_inner height."),
        "navWidth": dim("1360px", SRC_COMPUTED + " .navbar_inner width at a 1440 CSS px viewport."),
        "container": dim("1440px", SRC_ROOT + " --_primitives---layout--container-l = 90rem."),
        "authForm": dim("416px", SRC_COMPUTED + " the sign-in form column width."),
        "planCard": dim("328px", SRC_COMPUTED + " .pricing-card_content width."),
    },
}

light = {
    "page": color("{color.white}", SRC_ROOT + " --_semantics---color--surface-base resolves to white. Body background on www.mural.co is rgb(255, 255, 255)."),
    "pageInverse": color("{color.black}", SRC_COMPUTED + " the home hero paints on a black canvas. Body text on that canvas is white."),
    "surface": color("{color.white}", SRC_COMPUTED + " .pricing-card_content and .navbar_inner background rgb(255, 255, 255)."),
    "surfaceMuted": color("{color.authPage}", "Alias of the measured auth page background."),
    "text": color("{color.black}", SRC_ROOT + " --_semantics---color--text-main resolves to black."),
    "textBody": color("{color.heroMuted}", "The hero's muted display line, and --grey."),
    "textInverse": color("{color.white}", SRC_ROOT + " --_semantics---color--text-inverse resolves to white."),
    "textMuted": color("{color.grey500}", SRC_ROOT + " --_semantics---color--text-muted resolves to #828c92."),
    "accent": color("{color.jade}", SRC_ROOT + " --_primitives---color--jade is #00c27a. The home Get started control paints in this green."),
    "accentText": color("{color.black}", SRC_COMPUTED + " the Sign up free label computes to black on the green control."),
    "border": color("{color.grey100}", SRC_ROOT + " --_semantics---color--border-default resolves to #dce1e5."),
    "borderHover": color("{color.grey200}", SRC_ROOT + " --_semantics---color--border-hover resolves to #b8c1cc. The Book a demo border moves to rgb(184, 193, 204) on hover."),
    "focus": color("{color.authFocus}", "The keyboard focus outline on the sign-in email field."),
    "danger": color("{color.authRed}", "The Log in and Sign up buttons on app.mural.co."),
    "dangerHover": color("{color.authRedHover}", "The Log in button on hover."),
    "component": {
        "buttonPrimary": {
            "background": color("{color.jade}", SRC_COMPUTED + " a.button_component Sign up free background rgb(0, 194, 122), which is --jade."),
            "text": color("{color.black}", SRC_COMPUTED + " the Sign up free label color."),
            "radius": dim("{radius.button}", "The Sign up free control measures 8px."),
            "height": dim("40px", SRC_COMPUTED + " the Sign up free control height."),
        },
        "buttonOutline": {
            "background": color("{color.white}", SRC_COMPUTED + " Book a demo has a transparent fill on the white navbar."),
            "text": color("{color.black}", SRC_COMPUTED + " Book a demo label color."),
            "radius": dim("{radius.button}", "Book a demo measures 8px."),
            "height": dim("40px", SRC_COMPUTED + " Book a demo height."),
        },
        "buttonAuth": {
            "background": color("{color.authRed}", SRC_COMPUTED + " the Log in button."),
            "text": color("{color.white}", SRC_COMPUTED + " the Log in label."),
            "radius": dim("{radius.button}", "The Log in button measures 8px."),
            "height": dim("40px", SRC_COMPUTED + " the Log in button height."),
        },
        "field": {
            "background": color("{color.white}", SRC_COMPUTED + " input#work-email-input background."),
            "text": color("{color.authText}", SRC_COMPUTED + " the field's text color."),
            "radius": dim("{radius.button}", "The field measures 8px."),
            "height": dim("40px", SRC_COMPUTED + " the field height."),
        },
        "nav": {
            "background": color("{color.white}", SRC_COMPUTED + " .navbar_inner background."),
            "radius": dim("{radius.nav}", "The navbar pill measures 16px."),
            "height": dim("64px", SRC_COMPUTED + " .navbar_inner height."),
        },
        "card": {
            "background": color("{color.white}", SRC_COMPUTED + " .pricing-card_content background."),
            "radius": dim("{radius.card}", "The pricing card content measures 20px."),
        },
    },
}

tokens = {
    "core": core,
    "light": light,
    "$themes": [{
        "id": "light",
        "name": "Light",
        "selectedTokenSets": {"core": "source", "light": "enabled"},
        "$extensions": {"source": "The public site and the signed-out auth pages ship one light theme. No dark switch was found."},
    }],
}

out = json.dumps(tokens, indent=1) + "\n"
if __name__ == "__main__":
    (HERE / "tokens.json").write_text(out)
    print("wrote tokens.json", len(out), "bytes")
