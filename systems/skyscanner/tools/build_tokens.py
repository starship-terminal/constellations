#!/usr/bin/env python3
"""Build tokens.json from the live readings in raw/.

Every colour and length below was read from computed style or a custom
property on https://www.skyscanner.com.sg/ (redirected from
https://www.skyscanner.com/) and https://help.skyscanner.net/hc/en-gb on
2026-11-19. Nothing here is sampled from a screenshot.
"""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
OUT = HERE / "tokens.json"

VARS = json.loads((RAW / "css-vars.json").read_text())
COMP = json.loads((RAW / "components.json").read_text())

SRC = (
    "Measured computed custom property on :root, "
    "https://www.skyscanner.com.sg/, 1440x900, 2026-11-19"
)
HOME = (
    "Measured computed style, https://www.skyscanner.com.sg/, "
    "1440x900, dpr 2, 2026-11-19"
)
PHONE = (
    "Measured computed style, https://www.skyscanner.com.sg/, "
    "390x844, dpr 2, 2026-11-19"
)
HELP = (
    "Measured computed style, https://help.skyscanner.net/hc/en-gb, "
    "1169x731, dpr 2, 2026-11-19"
)


def color(value, source):
    return {"$type": "color", "$value": value, "$extensions": {"source": source}}


def dim(value, source):
    return {"$type": "dimension", "$value": value, "$extensions": {"source": source}}


def font(value, source):
    return {"$type": "fontFamily", "$value": value, "$extensions": {"source": source}}


def text_style(size, weight, line_height, source, letter_spacing=None):
    value = {
        "fontFamily": "{font.family.relative}",
        "fontSize": size,
        "fontWeight": weight,
        "lineHeight": line_height,
    }
    if letter_spacing:
        value["letterSpacing"] = letter_spacing
    return {"$type": "typography", "$value": value, "$extensions": {"source": source}}


def duration(value, source):
    return {"$type": "duration", "$value": value, "$extensions": {"source": source}}


def cubic(value, source):
    return {"$type": "cubicBezier", "$value": value, "$extensions": {"source": source}}


C = VARS["core"]

core = {
    "color": {
        "ink": color(C["primary"], f"{SRC} --bpk-core-primary"),
        "accent": color(C["accent"], f"{SRC} --bpk-core-accent"),
        "eco": color(C["eco"], f"{SRC} --bpk-core-eco"),
        "text": color(C["textPrimary"], f"{SRC} --bpk-text-primary"),
        "muted": color(C["textSecondary"], f"{SRC} --bpk-text-secondary"),
        "danger": color(C["statusDanger"], f"{SRC} --bpk-status-danger-spot"),
        "success": color(C["statusSuccess"], f"{SRC} --bpk-status-success-spot"),
        "warning": color(C["statusWarning"], f"{SRC} --bpk-status-warning-spot"),
        "loyalty": color(C["statusLoyalty"], f"{SRC} --bpk-status-loyalty-spot"),
        "canvas": color("#ffffff", f"{SRC} --bpk-canvas-default"),
        "canvas-contrast": color(C["canvasContrast"], f"{SRC} --bpk-canvas-contrast"),
        "highlight": color(C["surfaceHighlight"], f"{SRC} --bpk-surface-highlight"),
        "low": color(C["surfaceLowContrast"], f"{SRC} --bpk-surface-low-contrast"),
        "subtle": color(C["surfaceSubtle"], f"{SRC} --bpk-surface-subtle"),
        "danger-fill": color(C["surfaceDangerFill"], f"{SRC} --bpk-surface-danger-fill"),
        "success-fill": color(C["surfaceSuccessFill"], f"{SRC} --bpk-surface-success-fill"),
        "warning-fill": color(C["surfaceWarningFill"], f"{SRC} --bpk-surface-warning-fill"),
        "line": color(C["borderDefault"], f"{SRC} --bpk-border-default"),
        "pressed": color(C["buttonPrimaryPressed"], f"{SRC} --bpk-private-button-colour-bg-primary-pressed"),
        "feature-pressed": color(C["buttonFeaturePressed"], f"{SRC} --bpk-private-button-colour-bg-feature-pressed"),
        "cookie": color("#f1f2f8", f"{HOME} cookie banner background"),
        "shadow": color("#25201f", f"{HOME} painted shadow rgb(37, 32, 31)"),
        "help-link": color("#0a6cff", f"{HELP} link color"),
    },
    "font": {
        "family": {
            "relative": font(
                "Skyscanner Relative, -apple-system, system-ui, Roboto, sans-serif",
                f"{HOME} computed font-family. Files live on js.skyscnr.com and are not in this package.",
            )
        }
    },
    "typography": {
        "caption": text_style("12px", "400", "16px", f"{HOME} .bpk-text--caption"),
        "label-3": text_style("12px", "700", "16px", f"{HOME} .bpk-text--label-3"),
        "footnote": text_style("14px", "400", "20px", f"{HOME} .bpk-text--footnote"),
        "label-2": text_style("14px", "700", "20px", f"{HOME} .bpk-text--label-2"),
        "body": text_style("16px", "400", "20.8px", f"{HOME} body computed line-height 20.8px"),
        "label-1": text_style("16px", "700", "24px", f"{HOME} .bpk-text--label-1 and button label"),
        "heading-5": text_style("16px", "700", "20px", f"{HOME} .bpk-text--heading-5"),
        "heading-3": text_style("24px", "700", "28px", f"{HOME} .bpk-text--heading-3"),
        "heading-2": text_style("32px", "700", "40px", f"{HOME} .bpk-text--heading-2"),
        "hero-6": text_style("40px", "900", "40px", f"{HOME} login modal .bpk-text--hero-6"),
        "promo": text_style(
            "48px", "900", "48px", f"{HOME} graphic promo headline", letter_spacing="-1.92px"
        ),
        "help-body": text_style("20px", "400", "30px", f"{HELP} body"),
        "help-title": text_style("32px", "700", "48px", f"{HELP} h1"),
    },
    "radius": {
        "none": dim("0px", f"{SRC} --bpk-radius-none"),
        "xs": dim("4px", f"{SRC} --bpk-radius-xs 0.25rem, and the checkbox"),
        "sm": dim("8px", f"{SRC} --bpk-radius-sm 0.5rem, and button, chip"),
        "md": dim("12px", f"{SRC} --bpk-radius-md 0.75rem, and search field, Search button, card"),
        "nav-tab": dim("18px", f"{HOME} navigation tab border-radius. Token --bpk-radius-nav-tabs is 1.125rem"),
        "lg": dim("24px", f"{SRC} --bpk-radius-lg 1.5rem, and Help search field"),
        "xl": dim("48px", f"{SRC} --bpk-radius-xl 3rem"),
        "pill": dim("999px", f"{SRC} --bpk-radius-full 62.4375rem. Close button computed 100%"),
    },
    "spacing": {
        "xxs": dim("1px", f"{SRC} --bpk-spacing-xxs 0.0625rem"),
        "xs": dim("2px", f"{SRC} --bpk-spacing-xs 0.125rem"),
        "sm": dim("4px", f"{SRC} --bpk-spacing-sm 0.25rem"),
        "md": dim("8px", f"{SRC} --bpk-spacing-md 0.5rem, and tab group gap"),
        "base": dim("16px", f"{SRC} --bpk-spacing-base 1rem, and field padding-inline"),
        "lg": dim("24px", f"{SRC} --bpk-spacing-lg 1.5rem"),
        "xl": dim("32px", f"{SRC} --bpk-spacing-xl 2rem"),
        "xxl": dim("40px", f"{SRC} --bpk-spacing-xxl 2.5rem"),
        "xxxl": dim("64px", f"{SRC} --bpk-spacing-xxxl 4rem"),
        "xxxxl": dim("96px", f"{SRC} --bpk-spacing-xxxxl 6rem"),
        "footer-desktop": dim("48px", f"{HOME} footer padding-inline"),
        "phone-gutter": dim("16px", f"{PHONE} hero and footer padding-inline"),
    },
    "size": {
        "checkbox": dim("20px", f"{HOME} checkbox 20x20"),
        "chip": dim("32px", f"{HOME} chip height"),
        "close": dim("32px", f"{HOME} close button 32x32"),
        "button": dim("36px", f"{HOME} login and icon button height. Token min-height is 2.25rem"),
        "swap": dim("40px", f"{HOME} swap button 40x40"),
        "banner-button": dim("40px", f"{HOME} cookie banner button height"),
        "field-phone": dim("48px", f"{PHONE} search field and Search button height"),
        "button-large": dim("48px", f"{HOME} large featured button height. Token min-height-large is 3rem"),
        "help-search": dim("60px", f"{HELP} search field height"),
        "field": dim("72px", f"{HOME} desktop search field and Search button height"),
        "nav-card": dim("72px", f"{HOME} homepage nav card height"),
    },
    "motion": {
        "duration": {
            "200ms": duration("200ms", f"{HOME} nav card transition-duration"),
            "400ms": duration("400ms", f"{HOME} swap button transition-duration"),
        },
        "easing": {
            "ease": cubic([0.25, 0.1, 0.25, 1], f"{HOME} keyword ease, expanded. Evidence: Derived"),
            "ease-in-out": cubic([0.42, 0, 0.58, 1], f"{HOME} keyword ease-in-out on nav card shadow. Evidence: Derived"),
        },
    },
}

light = {
    "background": {
        "page": color("{color.canvas}", f"{HOME} Homepage_backgroundContainer"),
        "surface": color("{color.canvas}", f"{HOME} search field and modal"),
        "contrast": color("{color.ink}", f"{HOME} hero Homepage_searchControlsContainer and footer"),
        "canvas": color("{color.canvas-contrast}", f"{SRC} --bpk-canvas-contrast"),
        "action": color("{color.accent}", f"{HOME} Search button and selected Flights tab"),
        "action-pressed": color("{color.feature-pressed}", f"{SRC} featured pressed"),
        "primary": color("{color.ink}", f"{HOME} Accept all button"),
        "primary-pressed": color("{color.pressed}", f"{SRC} primary pressed"),
        "secondary": color("{color.highlight}", f"{HOME} secondary and stepper buttons"),
        "login": color("#eff3f8", f"{HOME} Log in button. Same value as --bpk-canvas-contrast"),
        "disabled": color("{color.highlight}", f"{SRC} --bpk-private-button-colour-bg-disabled"),
        "chip-on": color("{color.ink}", f"{HOME} selected Airport chip"),
        "cookie": color("{color.cookie}", f"{HOME} cookie banner"),
        "promo": color("{color.canvas-contrast}", f"{HOME} graphic promo card"),
        "danger-fill": color("{color.danger-fill}", f"{SRC} --bpk-surface-danger-fill"),
        "success-fill": color("{color.success-fill}", f"{SRC} --bpk-surface-success-fill"),
        "warning-fill": color("{color.warning-fill}", f"{SRC} --bpk-surface-warning-fill"),
        "subtle": color("{color.subtle}", f"{SRC} --bpk-surface-subtle"),
    },
    "text": {
        "primary": color("{color.text}", f"{SRC} --bpk-text-primary"),
        "secondary": color("{color.muted}", f"{HOME} field placeholder and modal links"),
        "on-contrast": color("#ffffff", f"{HOME} hero heading and Search label"),
        "on-footer": color("#eff3f8", f"{HOME} footer color"),
        "disabled": color("#00000033", f"{SRC} --bpk-text-disabled #0003"),
        "disabled-on-dark": color("#ffffff80", f"{SRC} --bpk-text-disabled-on-dark"),
        "danger": color("{color.danger}", f"{SRC} --bpk-text-error"),
        "success": color("{color.success}", f"{SRC} --bpk-text-success"),
        "help-link": color("{color.help-link}", f"{HELP} link"),
        "help-ink": color("{color.ink}", f"{HELP} body and h1"),
    },
    "border": {
        "default": color("{color.line}", f"{SRC} --bpk-border-default and idle chip inset"),
        "focus": color("{color.accent}", f"{HOME} Search button outline and --bpk-border-focus"),
        "selected": color("{color.ink}", f"{SRC} --bpk-border-selected and swap button"),
        "checkbox": color("{color.muted}", f"{HOME} checkbox 3px border"),
        "danger": color("{color.danger}", f"{SRC} --bpk-border-danger"),
        "on-dark": color("#ffffff80", f"{HOME} chip on dark inset rgba(255,255,255,0.5)"),
        "tab-idle": color("#ffffff33", f"{HOME} idle tab inset rgba(255,255,255,0.2)"),
    },
    "shadow": {
        "card": color("#25201f4d", f"{HOME} nav card rgba(37, 32, 31, 0.3)"),
        "popover": color("#25201f40", f"{HOME} popover and cookie banner rgba(37, 32, 31, 0.25)"),
    },
}

doc = {
    "$description": (
        "Skyscanner public marketing and search form, measured 2026-11-19 on "
        "www.skyscanner.com.sg after a geo redirect from www.skyscanner.com. "
        "Light only. The declared sheets include a dark canvas, but the painted "
        "page resolved light Backpack tokens. No dark theme switch was found."
    ),
    "core": core,
    "light": light,
    "$themes": [
        {
            "id": "light",
            "name": "Light",
            "selectedTokenSets": {"core": "source", "light": "enabled"},
        }
    ],
}

OUT.write_text(json.dumps(doc, indent=2) + "\n")
print(f"wrote {OUT}")
