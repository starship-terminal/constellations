#!/usr/bin/env python3
"""Build tokens.json from raw/readings.json.

Every value below was read on 2026-11-19 from the live Todoist pages named in
raw/readings.json (custom properties resolved on :root, or getComputedStyle).
oklch() roles are stored as their sRGB hex, a conversion labelled Derived whose
source keeps the declared oklch(), so hex-only readers (contrast checks, DESIGN.md)
can parse them and a reader can compare them with the rgb() the browser painted. Nothing here is recalled.
"""
import json
import math
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
RAW = json.loads((HERE / "raw" / "readings.json").read_text())
M = RAW["customProperties"]["marketing"]
A = RAW["customProperties"]["app"]


def tok(value, type_, source):
    return {"$value": value, "$type": type_, "$extensions": {"source": source}}


def oklch_hex(value):
    """A declared oklch(L C H [/ A]) as lower-case sRGB #rrggbb, or #rrggbbaa below full alpha
    (Oklab to linear sRGB, then the sRGB transfer curve). Raises on an out-of-gamut colour rather
    than clipping it, and on anything that is not oklch()."""
    m = re.fullmatch(r"oklch\(\s*([\d.]+)(%?)\s+([\d.]+)\s+([\d.]+)\s*(?:/\s*([\d.]+)(%?))?\s*\)", value.strip())
    if not m:
        raise ValueError(f"not an oklch() colour: {value!r}")
    L = float(m.group(1)) / (100 if m.group(2) else 1)
    C, H = float(m.group(3)), math.radians(float(m.group(4)))
    a, b = C * math.cos(H), C * math.sin(H)
    l = (L + 0.3963377774 * a + 0.2158037573 * b) ** 3
    mm = (L - 0.1055613458 * a - 0.0638541728 * b) ** 3
    s = (L - 0.0894841775 * a - 1.2914855480 * b) ** 3
    linear = (4.0767416621 * l - 3.3077115913 * mm + 0.2309699292 * s,
              -1.2684380046 * l + 2.6097574011 * mm - 0.3413193965 * s,
              -0.0041960863 * l - 0.7034186147 * mm + 1.7076147010 * s)
    if any(x < -0.002 or x > 1.002 for x in linear):
        raise ValueError(f"{value} is outside sRGB")
    def encode(x):
        x = min(1.0, max(0.0, x))
        return 12.92 * x if x <= 0.0031308 else 1.055 * x ** (1 / 2.4) - 0.055
    out = "#%02x%02x%02x" % tuple(round(encode(x) * 255) for x in linear)
    if m.group(5) is not None:
        alpha = float(m.group(5)) / (100 if m.group(6) else 1)
        if alpha < 1:
            out += "%02x" % int(alpha * 255 + 0.5)
    return out


def color(value, source):
    """A declared oklch() is stored as its sRGB hex, labelled Derived, with the declaration kept in
    the source; every other colour is stored as read."""
    if value.strip().startswith("oklch("):
        return tok(oklch_hex(value), "color", f"Derived: sRGB conversion of the declared {value.strip()}. " + source)
    return tok(value, "color", source)


SRC_HOME = "custom property resolved on :root at https://www.todoist.com/ on 2026-11-19"
SRC_APP = "custom property resolved on :root at https://app.todoist.com/auth/login on 2026-11-19"
SRC_COMPUTED = "getComputedStyle on the live page named in raw/readings.json"


def core():
    return {
        "font": {
            "family": {
                "sans": tok(
                    "Graphik, Arial, Helvetica Neue, Helvetica, sans-serif",
                    "fontFamily",
                    SRC_HOME + "; --font-family-sans computed family Graphik-1bbd4a4c7a2fb472. Hashed face name shortened to Graphik.",
                ),
                "body": tok(
                    "Inter, Arial, Helvetica Neue, Helvetica, sans-serif",
                    "fontFamily",
                    SRC_HOME + "; --font-family-body computed family Inter-5486e50ce5a4efdf.",
                ),
                "serif": tok(
                    "Caecilia, Times New Roman, serif",
                    "fontFamily",
                    SRC_HOME + "; --font-family-serif. Not used on the measured controls.",
                ),
                "app": tok(
                    "-apple-system, BlinkMacSystemFont, Segoe UI, Noto Sans, system-ui, sans-serif",
                    "fontFamily",
                    SRC_APP + "; --td-ui-font-family. Login body computed fontFamily was -apple-system.",
                ),
            }
        },
        "typography": {
            "display": tok(
                {
                    "fontFamily": "{font.family.sans}",
                    "fontSize": "55px",
                    "fontWeight": "600",
                    "lineHeight": "63.25px",
                    "letterSpacing": "-0.55px",
                },
                "typography",
                SRC_COMPUTED + "; home visible h1 at innerWidth 1169. Declared --major-2xl-font-size is a clamp, not this painted size.",
            ),
            "plan-name": tok(
                {
                    "fontFamily": "{font.family.sans}",
                    "fontSize": "31px",
                    "fontWeight": "600",
                    "lineHeight": "1.28",
                    "letterSpacing": "-0.01em",
                },
                "typography",
                SRC_COMPUTED + "; pricing h2/h3 Pro, Beginner, Business. Line height is --major-sm-line-height, not a computed line-height on that heading.",
            ),
            "lede": tok(
                {
                    "fontFamily": "{font.family.body}",
                    "fontSize": "20.5px",
                    "fontWeight": "500",
                    "lineHeight": "32.8px",
                    "letterSpacing": "0",
                },
                "typography",
                SRC_COMPUTED + "; paragraph under the home h1, painted 20.5008px / 32.8013px, rounded to 0.1px.",
            ),
            "nav": tok(
                {
                    "fontFamily": "{font.family.body}",
                    "fontSize": "15.5px",
                    "fontWeight": "500",
                    "lineHeight": "20.925px",
                    "letterSpacing": "0.155px",
                },
                "typography",
                SRC_COMPUTED + "; home nav link Individual.",
            ),
            "button": tok(
                {
                    "fontFamily": "{font.family.body}",
                    "fontSize": "18.5px",
                    "fontWeight": "600",
                    "lineHeight": "25.9px",
                    "letterSpacing": "0.185px",
                },
                "typography",
                SRC_COMPUTED + "; home hero Start for free, xl.",
            ),
            "app-title": tok(
                {
                    "fontFamily": "{font.family.app}",
                    "fontSize": "32px",
                    "fontWeight": "700",
                    "lineHeight": "1",
                    "letterSpacing": "0",
                },
                "typography",
                SRC_COMPUTED + "; login h1 Welcome back! Matches --td-ui-font-size-header-xlarge and --td-ui-font-weight-strong. Line height was normal, stored as 1.",
            ),
            "app-button": tok(
                {
                    "fontFamily": "{font.family.app}",
                    "fontSize": "18px",
                    "fontWeight": "700",
                    "lineHeight": "36px",
                    "letterSpacing": "0",
                },
                "typography",
                SRC_COMPUTED + "; login Log in submit and Continue with Google.",
            ),
            "app-label": tok(
                {
                    "fontFamily": "{font.family.app}",
                    "fontSize": "12px",
                    "fontWeight": "400",
                    "lineHeight": "21px",
                    "letterSpacing": "0",
                },
                "typography",
                SRC_COMPUTED + "; login Email label. Matches --td-ui-font-size-caption.",
            ),
        },
        "radius": {
            "sm": tok("6px", "dimension", SRC_HOME + "; --border-radius-sm. Also --product-library-radius-button on the login page."),
            "base": tok("8px", "dimension", SRC_HOME + "; --border-radius-base. Home nav links painted 8px."),
            "lg": tok("10px", "dimension", SRC_HOME + "; --border-radius-lg and --card-border-radius. Pricing articles painted 10px."),
            "xl": tok("15px", "dimension", SRC_HOME + "; --border-radius-2xl. Home xl Start for free painted 15px."),
            "full": tok("9999px", "dimension", SRC_HOME + "; --border-radius-full."),
        },
        "spacing": {
            "4": tok("4px", "dimension", SRC_HOME + "; --space-4 is 0.25rem. Derived px at the browser default 16px root. Login field wrapper painted padding included 4px."),
            "8": tok("8px", "dimension", SRC_HOME + "; --space-8 is 0.5rem. Login field wrapper painted padding 8px."),
            "12": tok("12px", "dimension", SRC_HOME + "; --space-12 is 0.75rem. Home xl button painted padding-block 12px."),
            "14": tok("14px", "dimension", SRC_COMPUTED + "; home nav link and pricing Get started painted padding-inline 14px. No matching --space token."),
            "16": tok("16px", "dimension", SRC_HOME + "; --space-16 is 1rem. Home xl button painted padding-inline 16px. Login SSO painted padding-inline 16px."),
            "24": tok("24px", "dimension", SRC_HOME + "; --space-24 is 1.5rem. Home nav painted padding-inline 24px. Pricing articles painted padding-block 24px."),
            "32": tok("32px", "dimension", SRC_HOME + "; --space-32 is 2rem. Pricing articles painted padding-inline 32px."),
        },
        "motion": {
            "duration": {
                "150": tok("150ms", "duration", SRC_HOME + "; --animation-duration-150 is .15s."),
                "350": tok("350ms", "duration", SRC_HOME + "; --animation-duration-350 is .35s."),
            },
            "easing": {
                "base": tok([0.2, 0.8, 0.2, 1], "cubicBezier", SRC_HOME + "; --animation-ease-base cubic-bezier(.2, .8, .2, 1)."),
            },
        },
        "size": {
            "nav-height": tok("72px", "dimension", SRC_COMPUTED + "; home nav height 72 at innerWidth 1169."),
            "button-xl": tok("64px", "dimension", SRC_COMPUTED + "; home hero Start for free height 64."),
            "button-nav": tok("39px", "dimension", SRC_COMPUTED + "; home nav link height 39."),
            "login-control": tok("48px", "dimension", SRC_COMPUTED + "; login SSO link and Log in button height 48."),
            "login-field": tok("65px", "dimension", SRC_COMPUTED + "; login email field wrapper height 65."),
            "login-column": tok("376px", "dimension", SRC_COMPUTED + "; login h1, SSO link and Log in button width 376."),
        },
    }


def light():
    return {
        "background": {
            "page": color(M["--neutral"], SRC_HOME + "; --neutral. body backgroundColor computed oklch(0.9945 0.0017 67.8)."),
            "surface": color(M["--card-background-idle"], SRC_HOME + "; --card-background-idle. Pricing article backgroundColor computed rgb(255, 255, 255)."),
            "muted": color(M["--productui-sidebar"], SRC_HOME + "; --productui-sidebar #fcfaf8. Login body backgroundColor computed rgb(252, 250, 248)."),
            "action": color(M["--actionable-primary-background-idle"], SRC_HOME + "; --actionable-primary-background-idle. Home hero CTA backgroundColor computed the same oklch."),
            "action-hover": color(M["--actionable-primary-background-onhover"], SRC_HOME + "; --actionable-primary-background-onhover. Declared hover, not forced on an element."),
            "secondary": color(M["--actionable-secondary-background-idle"], SRC_HOME + "; --actionable-secondary-background-idle. Pricing Get started backgroundColor computed rgba(37, 34, 30, 0.07)."),
            "overlay": color(A["--product-library-background-overlay"], SRC_APP + "; --product-library-background-overlay. Declared, no open dialog was measured."),
        },
        "text": {
            "primary": color(M["--display-onlight-primary"], SRC_HOME + "; --display-onlight-primary. Home body color computed rgb(37, 34, 30)."),
            "secondary": color(M["--display-onlight-secondary"], SRC_HOME + "; --display-onlight-secondary. Home lede color computed rgba(37, 34, 30, 0.66)."),
            "tertiary": color(M["--display-onlight-tertiary"], SRC_HOME + "; --display-onlight-tertiary."),
            "on-action": color("#ffffff", SRC_COMPUTED + "; home hero CTA color computed oklch(1 0 0). Login submit color computed rgb(255, 255, 255)."),
            "link": color(A["--product-library-display-accent-primary-tint"], SRC_APP + "; login links Forgot your password? and Sign up computed rgb(211, 51, 34), which is #d33322."),
            "app": color(A["--product-library-display-primary-idle-tint"], SRC_APP + "; login body color computed rgb(32, 32, 32)."),
            "app-muted": color(A["--product-library-display-secondary-idle-tint"], SRC_APP + "; --product-library-display-secondary-idle-tint. Not painted on a measured text node."),
        },
        "border": {
            "card": color(M["--card-border-idle"], SRC_HOME + "; --card-border-idle. Pricing article border computed the same oklch at 0.12, a quieter step."),
            "field": color(A["--product-library-border-idle-tint"], SRC_APP + "; login field wrapper border computed rgb(229, 229, 229)."),
            "focus": color(A["--product-library-border-focus-tint"], SRC_APP + "; login field wrapper border computed rgb(184, 184, 184) after input.focus()."),
        },
        "shadow": {
            "focus-ring": tok(
                re.sub(r"oklch\([^)]*\)", lambda m: oklch_hex(m.group(0)), M["--shadow-focusvisible-default"]),
                "shadow",
                "Derived: the colours are sRGB conversions of the declared "
                + M["--shadow-focusvisible-default"] + ". " + SRC_HOME
                + "; --shadow-focusvisible-default. Home hero CTA boxShadow after element.focus() matched this shadow.",
            ),
        },
        "status": {
            "danger": color(A["--product-library-info-attention-primary-idle-fill"], SRC_APP + "; --product-library-info-attention-primary-idle-fill."),
            "warning": color(A["--product-library-info-warning-primary-on-idle-fill"], SRC_APP + "; --product-library-info-warning-primary-on-idle-fill."),
            "success": color(A["--product-library-info-positive-primary-idle-fill"], SRC_APP + "; --product-library-info-positive-primary-idle-fill."),
            "info": color(A["--product-library-info-neutral-primary-idle-fill"], SRC_APP + "; --product-library-info-neutral-primary-idle-fill."),
        },
        "brand": {
            "primary-hex": color(M["--color-td-primary"], SRC_HOME + "; --color-td-primary. Safari pinned tab mask-icon color on the homepage is #e44332."),
            "cta-hover-hex": color(M["--color-td-cta-hover"], SRC_HOME + "; --color-td-cta-hover. Declared, not forced."),
            "cta-active-hex": color(M["--color-td-cta-active"], SRC_HOME + "; --color-td-cta-active. Declared, not forced."),
            "app-action": color(A["--product-library-actionable-primary-idle-fill"], SRC_APP + "; login submit backgroundColor computed rgb(211, 51, 34)."),
            "app-action-hover": color(A["--product-library-actionable-primary-hover-fill"], SRC_APP + "; declared hover fill. Not forced."),
            "priority-1": color(M["--product-ui-priority-1"], SRC_HOME + "; --product-ui-priority-1."),
            "priority-2": color(M["--product-ui-priority-2"], SRC_HOME + "; --product-ui-priority-2."),
            "priority-3": color(M["--product-ui-priority-3"], SRC_HOME + "; --product-ui-priority-3."),
            "priority-4": color(M["--product-ui-priority-4"], SRC_HOME + "; --product-ui-priority-4."),
        },
        "component": {
            "button-primary": {
                "background": color("{background.action}", "alias of the home hero CTA fill"),
                "text": color("{text.on-action}", "alias of the home hero CTA text"),
                "radius": tok("{radius.xl}", "dimension", "home hero Start for free painted border-radius 15px"),
                "padding": {  # computed shorthand 12px 16px, one px length per axis
                    "block": tok("12px", "dimension", SRC_COMPUTED + "; home hero Start for free padding 12px 16px"),
                    "inline": tok("16px", "dimension", SRC_COMPUTED + "; home hero Start for free padding 12px 16px"),
                },
                "height": tok("{size.button-xl}", "dimension", "home hero Start for free height"),
            },
            "button-secondary": {
                "background": color("{background.secondary}", "alias of the pricing Get started fill"),
                "text": color("{text.primary}", "pricing Get started color computed rgb(37, 34, 30)"),
                "radius": tok("{radius.base}", "dimension", "pricing Get started painted border-radius 8px"),
            },
            "field": {
                "background": color("#ffffff", SRC_COMPUTED + "; login field wrapper backgroundColor was transparent. This hex is the card white, not a painted field fill. Gap."),
                "text": color("{text.app}", "login input color"),
                "radius": tok("{radius.sm}", "dimension", "login field wrapper painted border-radius 6px"),
                "height": tok("{size.login-field}", "dimension", "login email wrapper height"),
            },
        },
    }


def document():
    return {
        "$description": "Todoist public marketing site and signed-out login, measured 2026-11-19. Light only. Dark theme was not on these pages.",
        "core": core(),
        "light": light(),
        "$themes": [{"id": "light", "name": "Light", "selectedTokenSets": {"core": "enabled", "light": "enabled"}}],
    }


def build():
    text = json.dumps(document(), indent=2) + "\n"
    (HERE / "tokens.json").write_text(text)
    print(f"wrote {HERE / 'tokens.json'} ({len(text)} bytes)")


if __name__ == "__main__":
    build()
