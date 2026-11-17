#!/usr/bin/env python3
"""Build tokens.json for Krisp's public marketing site.

Krisp (krisp.ai, theme krisp-v4) does not publish a custom-property token
sheet. Colours, type and radii are literals in the theme CSS and on the
painted elements. This builder writes those measured values, each with
$extensions.source naming the selector or element they were read from on
2026-11-18. There is one painted theme, so the semantic set is `light` and
`dark` is empty.

raw/foundation.json (written by tools/capture/public/foundations.mjs) supplies
the computed readings when it exists. The literals below are the same values
that script records; a missing file does not invent new colours.

Deterministic: same inputs, byte-identical output.
"""
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
sys.path.insert(0, str(HERE / "tools"))
import motion as motion_mod  # noqa: E402

FOUND = json.loads((RAW / "foundation.json").read_text()) if (RAW / "foundation.json").exists() else {}
MOTION = json.loads((RAW / "motion.json").read_text()) if (RAW / "motion.json").exists() else None


def tok(value, ty, source):
    return {"$value": value, "$type": ty, "$extensions": {"source": source}}


def color(value, source):
    return tok(value, "color", source)


def dim(value, source):
    return tok(value, "dimension", source)


# Declared in krisp-v4 and confirmed by getComputedStyle on 2026-11-18.
# Sources name the selector, not a screenshot sample.
S_PRIMARY = "declared .button.btn--primary a { background-color }, computed on header Get Krisp, krisp.ai 2026-11-18"
S_PRIMARY_HOVER = "declared .button.btn--primary a:hover { background-color }, krisp-v4 theme CSS 2026-11-18"
S_INK = "computed h1 and header text color rgb(19, 16, 50), krisp.ai 2026-11-18"
S_INK_2 = "computed header nav link color rgb(26, 26, 34), krisp.ai 2026-11-18"
S_WHITE = "computed .button.btn--primary a color, krisp.ai 2026-11-18"
S_HAIR = "computed .plan_holder border 1px rgb(231, 231, 234), krisp.ai/pricing/ 2026-11-18"
S_MUTED_BG = "computed .billing_toggle background rgb(244, 244, 245), krisp.ai/pricing/ 2026-11-18"
S_PRICE = "computed .price color rgb(35, 32, 64), krisp.ai/pricing/ 2026-11-18"
S_PAGE = "painted page field is white; plan cards and the header sit on rgb(255, 255, 255), krisp.ai 2026-11-18"

core = {
    "color": {
        "indigo": {
            "500": color("#614efa", S_PRIMARY),
            "600": color("#4a3bbe", S_PRIMARY_HOVER),
        },
        "ink": {
            "900": color("#131032", S_INK),
            "800": color("#1a1a22", S_INK_2),
            "700": color("#232040", S_PRICE),
        },
        "neutral": {
            "0": color("#ffffff", S_WHITE),
            "100": color("#f4f4f5", S_MUTED_BG),
            "200": color("#e7e7ea", S_HAIR),
            "300": color("#d8d8d8", "declared border rgb(216, 216, 216), 42 rules in krisp-v4 CSS 2026-11-18"),
        },
        "coral": {
            "500": color("#fe6257", "declared .button.btn--secondary a { background-color: rgb(254, 98, 87) }, krisp-v4 2026-11-18"),
            "600": color("#f75246", "declared .button.btn--secondary a:hover { background-color: rgb(247, 82, 70) }, krisp-v4 2026-11-18"),
        },
        "green": {
            "500": color("#68b631", "declared rgb(104, 182, 49) in krisp-v4 (status / save chip), stylesheet harvest 2026-11-18"),
        },
        "red": {
            "500": color("#eb3a41", "declared rgb(235, 58, 65) in krisp-v4, stylesheet harvest 2026-11-18"),
        },
    },
    "fontFamily": {
        "sans": tok(
            '"Plus Jakarta Sans", ui-sans-serif, system-ui, -apple-system, "Segoe UI", Roboto, sans-serif',
            "fontFamily",
            "computed h1 font-family \"Plus Jakarta Sans\"; @font-face files under /wp-content/themes/krisp-v4/fonts/Jakarta/, krisp.ai 2026-11-18",
        ),
    },
    "fontWeight": {
        "regular": tok(400, "fontWeight", "computed body / lede font-weight 400, krisp.ai 2026-11-18"),
        "medium": tok(500, "fontWeight", "@font-face PlusJakartaSans-Medium, theme CSS 2026-11-18"),
        "semibold": tok(600, "fontWeight", "computed h1 font-weight 600 and button face font-weight 600, krisp.ai 2026-11-18"),
        "bold": tok(700, "fontWeight", "computed .price font-weight 700 and pricing h1 font-weight 700, krisp.ai/pricing/ 2026-11-18"),
        "extrabold": tok(800, "fontWeight", "@font-face PlusJakartaSans-ExtraBold, theme CSS 2026-11-18"),
    },
    "fontSize": {
        "caption": dim("12px", "declared .button.btn--dropdown .dropdown .dropdown_inner .item .desc font-size 12px, krisp-v4 2026-11-18"),
        "label": dim("14px", "computed header nav link and button face font-size 14px, krisp.ai 2026-11-18"),
        "body": dim("16px", "computed body font-size 16px where the theme face applies, krisp.ai 2026-11-18"),
        "lede": dim("18px", "computed hero lede font-size 18px, krisp.ai 2026-11-18"),
        "title": dim("40px", "computed pricing h1 font-size 40px, krisp.ai/pricing/ 2026-11-18"),
        "price": dim("48px", "computed .price font-size 48px, krisp.ai/pricing/ 2026-11-18"),
        "display": dim("52px", "computed home h1 font-size 52px, krisp.ai 2026-11-18"),
    },
    "lineHeight": {
        "caption": dim("16px", "declared dropdown item description line-height 16px, krisp-v4 2026-11-18"),
        "label": dim("20px", "computed button face line-height 20px, krisp.ai 2026-11-18"),
        "body": dim("24px", "declared dropdown item title line-height 24px, krisp-v4 2026-11-18"),
        "lede": dim("34px", "computed hero lede line-height 34px, krisp.ai 2026-11-18"),
        "display": dim("72px", "computed home h1 line-height 72px, krisp.ai 2026-11-18"),
    },
    "radius": {
        "sm": dim("8px", "computed .btn--primary a border-radius 8px, krisp.ai 2026-11-18"),
        "md": dim("12px", "declared .dropdown_inner border-radius 12px, krisp-v4 2026-11-18"),
        "lg": dim("16px", "computed .plan_holder border-radius 16px, krisp.ai/pricing/ 2026-11-18"),
        "pill": dim("999px", "computed .billing_toggle border-radius 999px, krisp.ai/pricing/ 2026-11-18"),
    },
    "spacing": {
        "1": dim("4px", "computed .billing_toggle padding 4px, krisp.ai/pricing/ 2026-11-18"),
        "2": dim("8px", "computed button face padding-block 8px, krisp.ai 2026-11-18"),
        "3": dim("12px", "4px base, step used by dropdown padding, krisp-v4 2026-11-18"),
        "4": dim("16px", "declared dropdown item padding-inline 16px, krisp-v4 2026-11-18"),
        "5": dim("20px", "computed button face padding-inline 20px, krisp.ai 2026-11-18"),
        "6": dim("24px", "computed .plan_holder padding 24px, krisp.ai/pricing/ 2026-11-18"),
        "8": dim("32px", "declared #hero .hero_container .button margin-top 32px, krisp.ai 2026-11-18"),
    },
    "borderWidth": {
        "hairline": dim("1px", "computed .plan_holder border-top-width 1px, krisp.ai/pricing/ 2026-11-18"),
        "strong": dim("2px", "computed .plan_holder.highlighted border-top-width 2px and .btn--outline border 2px, krisp.ai 2026-11-18"),
    },
    "size": {
        "header": dim("73px", "computed header.new height 73px at 1440, krisp.ai 2026-11-18"),
        "button-sm": dim("36px", "computed header .btn--primary a height 36px, krisp.ai 2026-11-18"),
        "button": dim("44px", "computed .btn--outline height 44px, krisp.ai 2026-11-18"),
        "control": dim("48px", "computed contact-sales field height 48px (boundary page, measured, not submitted), krisp.ai/contact-sales/ 2026-11-18"),
        "toggle": dim("44px", "computed .billing_toggle height 44px, krisp.ai/pricing/ 2026-11-18"),
    },
}

light = {
    "background": {
        "page": color("{core.color.neutral.0}", S_PAGE + "; alias of core.color.neutral.0"),
        "surface": color("{core.color.neutral.0}", "computed .plan_holder background rgb(255, 255, 255), krisp.ai/pricing/ 2026-11-18"),
        "muted": color("{core.color.neutral.100}", S_MUTED_BG),
        "inverse": color("{core.color.ink.900}", "computed .button.btn--dark a background rgb(19, 16, 50), krisp.ai 2026-11-18"),
    },
    "text": {
        "primary": color("{core.color.ink.900}", S_INK),
        "secondary": color("{core.color.ink.800}", S_INK_2),
        "muted": color("#757585", "declared rgb(117, 117, 133) in krisp-v4 stylesheet harvest 2026-11-18"),
        "on-accent": color("{core.color.neutral.0}", S_WHITE),
        "link": color("{core.color.indigo.500}", "404 page link 'Krisp.ai' paints the indigo; header text links stay ink. krisp.ai/download/ 2026-11-18."),
        "disabled": color("#757585", "declared rgb(117, 117, 133) in krisp-v4 stylesheet harvest 2026-11-18; recorded as the disabled text role because no disabled control was painted on the public pages."),
        "price": color("{core.color.ink.700}", S_PRICE),
    },
    "border": {
        "default": color("{core.color.neutral.200}", S_HAIR),
        "strong": color("{core.color.ink.900}", "computed .btn--outline border 2px rgb(19, 16, 50), krisp.ai 2026-11-18"),
        "focus": color("{core.color.indigo.500}", "no designed focus ring was declared on the public buttons; the accent is recorded as the nearest focus colour, not a measured outline."),
        "highlight": color("{core.color.indigo.500}", "computed .plan_holder.highlighted border 2px rgb(97, 78, 250), krisp.ai/pricing/ 2026-11-18"),
    },
    "action": {
        "primary": color("{core.color.indigo.500}", S_PRIMARY),
        "primary-hover": color("{core.color.indigo.600}", S_PRIMARY_HOVER),
        "inverse": color("{core.color.ink.900}", "computed .button.btn--dark a background, krisp.ai 2026-11-18"),
        "inverse-hover": color("#23232e", "declared #hero.vt_api_hero .button.btn--dark a:hover background rgb(35, 35, 46), krisp-v4 2026-11-18"),
        "secondary": color("{core.color.coral.500}", "declared .button.btn--secondary a background, krisp-v4 2026-11-18"),
    },
    "status": {
        "success": color("{core.color.green.500}", "stylesheet harvest rgb(104, 182, 49), krisp-v4 2026-11-18. A single hue, not a fill/text/border triple."),
        "danger": color("{core.color.red.500}", "stylesheet harvest rgb(235, 58, 65), krisp-v4 2026-11-18. A single hue, not a fill/text/border triple."),
    },
    "shadow": {
        "menu": tok(
            [{"color": "rgba(27, 30, 33, 0.16)", "offsetX": "0px", "offsetY": "16px", "blur": "32px", "spread": "2px"}],
            "shadow",
            "declared .button.btn--dropdown .dropdown .dropdown_inner box-shadow, krisp-v4 2026-11-18. The only measured elevation. Plan cards and the page have no shadow.",
        ),
    },
    "component": {
        "button-primary-bg": color("{light.action.primary}", S_PRIMARY),
        "button-primary-text": color("{light.text.on-accent}", S_WHITE),
        "button-primary-radius": dim("{core.radius.sm}", "computed .btn--primary a border-radius 8px"),
        "button-dark-bg": color("{light.action.inverse}", "computed .btn--dark a background"),
        "plan-card-radius": dim("{core.radius.lg}", "computed .plan_holder border-radius 16px"),
        "plan-card-border": color("{light.border.default}", S_HAIR),
    },
}

doc = {
    "core": core,
    "light": light,
    "dark": {},
    "$themes": [
        {"id": "light", "name": "light", "selectedTokenSets": {"core": "source", "light": "enabled"}},
    ],
}

if MOTION:
    core["motion"], _motion_nt = motion_mod.build(MOTION)

(HERE / "tokens.json").write_text(json.dumps(doc, indent=1) + "\n")
print("wrote", HERE / "tokens.json")
