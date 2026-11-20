#!/usr/bin/env python3
"""Build tokens.json from raw/measured.json.

Values are the ones read on 2026-11-19. A colour that was only a computed
rgb() is stored as the hex the custom property already resolved to, and the
source string keeps the rgb reading. Nothing here invents a ramp step.
"""
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent
MEASURED = json.loads((ROOT / "raw" / "measured.json").read_text())


def color(value, source, description):
    return {
        "$type": "color",
        "$value": value,
        "$description": description,
        "$extensions": {"source": source},
    }


def dim(value, source, description):
    return {
        "$type": "dimension",
        "$value": value,
        "$description": description,
        "$extensions": {"source": source},
    }


def font(value, source, description):
    return {
        "$type": "fontFamily",
        "$value": value,
        "$description": description,
        "$extensions": {"source": source},
    }


def cubic(value, source, description):
    return {
        "$type": "cubicBezier",
        "$value": value,
        "$description": description,
        "$extensions": {"source": source},
    }


def typography(value, source, description):
    return {
        "$type": "typography",
        "$value": value,
        "$description": description,
        "$extensions": {"source": source},
    }


def shadow(value, source, description):
    return {
        "$type": "shadow",
        "$value": value,
        "$description": description,
        "$extensions": {"source": source},
    }


M = "Computed custom property on html.dark at https://retool.com/, 2026-11-19."
L = "Computed custom property after html class was set to light on https://retool.com/. The page's own themeMode is dark. Painted hero text did not follow the swap."
LOGIN = "Computed style on https://login.retool.com/auth/login, 2026-11-19. Fields were left empty."
DOCS = "Computed custom property on https://docs.retool.com/ with data-theme=dark, 2026-11-19."
HOME = "getComputedStyle on https://retool.com/, viewport 1169x731, devicePixelRatio 2."


def build():
    home = MEASURED["pages"]["home"]
    login = MEASURED["pages"]["login"]
    assert home["primaryCta"]["backgroundColor"] == "rgb(233, 235, 223)"
    assert login["email"]["backgroundColor"] == "rgb(247, 248, 244)"
    assert login["submit"]["backgroundColor"] == "rgb(21, 21, 21)"

    core = {
        "color": {
            "raw": {
                "black-0": color("#000000", M + " --raw-neutral-dark-black-0.", "Raw black."),
                "black-1": color("#0e0e0e", M + " --raw-neutral-dark-black-1.", "Raw black 1."),
                "black-2": color("#151515", M + " --raw-neutral-dark-black-2-primary. Homepage body computed rgb(21, 21, 21).", "Page black."),
                "black-3": color("#242424", M + " --raw-neutral-dark-black-3.", "Raw black 3."),
                "black-4": color("#2e2f2d", M + " --raw-neutral-dark-black-4.", "Raw black 4."),
                "black-5": color("#3f403d", M + " --raw-neutral-dark-black-5.", "Raw black 5."),
                "white-0": color("#ffffff", M + " --raw-neutral-light-white-0.", "Raw white."),
                "white-1": color("#f7f8f4", M + " --raw-neutral-light-white-1. Login field computed rgb(247, 248, 244).", "Warm white 1."),
                "white-2": color("#e9ebdf", M + " --raw-neutral-light-white-2-primary. Homepage text computed rgb(233, 235, 223).", "Ink white."),
                "white-3": color("#cbccc4", M + " --raw-neutral-light-white-3. Pricing muted note computed rgb(203, 204, 196).", "Muted white 3."),
                "white-4": color("#b6b8af", M + " --raw-neutral-light-white-4. Docs body computed rgb(182, 184, 175).", "Muted white 4."),
                "white-5": color("#94958e", M + " --raw-neutral-light-white-5.", "Muted white 5."),
                "gray": color("#8b867f", M + " --raw-gray-primary. Book a demo border computed rgb(139, 134, 127).", "Gray stroke."),
                "gray-lightened": color("#c8bfb5", M + " --raw-gray-lightened.", "Gray lightened."),
                "gray-lightest": color("#ded9d3", M + " --raw-gray-lightest.", "Gray lightest."),
                "gray-darkened": color("#433e38", M + " --raw-gray-darkened.", "Gray darkened."),
                "gray-darkest": color("#282522", M + " --raw-gray-darkest.", "Gray darkest."),
                "blue": color("#518dd2", M + " --raw-blue-primary. Submit prompt computed rgb(81, 141, 210). Login focus outline rgb(81, 141, 210).", "Blue."),
                "blue-light": color("#71a2da", M + " --raw-blue-light.", "Blue light."),
                "blue-lighter": color("#b0ccea", M + " --raw-blue-lighter.", "Blue lighter."),
                "blue-lightest": color("#d8e6f3", M + " --raw-blue-lightest.", "Blue lightest."),
                "blue-dark": color("#2d4c71", M + " --raw-blue-dark.", "Blue dark."),
                "blue-darker": color("#1b2e44", M + " --raw-blue-darker.", "Blue darker."),
                "blue-darkest": color("#101e2d", M + " --raw-blue-darkest.", "Blue darkest."),
                "green": color("#4d9987", M + " --raw-green-primary.", "Green."),
                "orange": color("#e8765e", M + " --raw-orange-primary.", "Orange."),
                "pink": color("#cc64ce", M + " --raw-pink-primary.", "Pink."),
                "purple": color("#9874d2", M + " --raw-purple-primary.", "Purple."),
                "red": color("#ef4444", M + " --raw-red-primary.", "Red."),
                "yellow": color("#eca438", M + " --raw-yellow-primary.", "Yellow."),
                "lime": color("#e0d643", M + " --raw-lime-primary.", "Lime."),
                "critical-8": color("#e79295", M + " --raw-semantic-critical-8.", "Critical 8."),
                "critical-10": color("#f15264", M + " --raw-semantic-critical-10. Dark input error stroke.", "Critical 10."),
                "critical-11": color("#c72844", M + " --raw-semantic-critical-11.", "Critical 11."),
                "critical-12": color("#651722", M + " --raw-semantic-critical-12. Dark alert background.", "Critical 12."),
                "success-8": color("#52bb9d", M + " --raw-semantic-success-8.", "Success 8."),
                "success-10": color("#11997a", M + " --raw-semantic-success-10.", "Success 10."),
                "success-11": color("#008163", M + " --raw-semantic-success-11.", "Success 11."),
                "success-12": color("#1a3c32", M + " --raw-semantic-success-12.", "Success 12."),
                "warning-8": color("#e0a24e", M + " --raw-semantic-warning-8.", "Warning 8."),
                "warning-10": color("#f1a42e", M + " --raw-semantic-warning-10.", "Warning 10."),
                "warning-11": color("#aa6800", M + " --raw-semantic-warning-11.", "Warning 11."),
                "warning-12": color("#4b371d", M + " --raw-semantic-warning-12.", "Warning 12."),
            },
            "login": {
                "page": color("#ffffff", LOGIN + " Body computed rgb(255, 255, 255). --background-surface.", "Login page."),
                "text": color("#222222", LOGIN + " Body computed rgb(34, 34, 34). --text-primary.", "Login body text."),
                "text-ink": color("#151515", LOGIN + " Welcome back computed rgb(21, 21, 21).", "Login heading ink."),
                "muted": color("#808080", LOGIN + " --text-secondary.", "Login secondary text."),
                "disabled": color("#b3b3b3", LOGIN + " --text-disabled.", "Login disabled text."),
                "field": color("#f7f8f4", LOGIN + " Email field computed rgb(247, 248, 244).", "Login field fill."),
                "button": color("#151515", LOGIN + " Sign in button computed rgb(21, 21, 21).", "Login submit fill."),
                "button-text": color("#f7f8f4", LOGIN + " Sign in label computed rgb(247, 248, 244).", "Login submit label."),
                "google-border": color("#ebebeb", LOGIN + " Google button border computed rgb(235, 235, 235). --gray-150.", "Google button stroke."),
                "focus": color("#518dd2", LOGIN + " Email :focus outline rgb(81, 141, 210) solid 2px, offset 2px.", "Login focus ring."),
                "brand": color("#3170f9", LOGIN + " --text-brand and --icon-brand.", "Login brand blue."),
                "critical": color("#dc2626", LOGIN + " --text-critical.", "Login critical text."),
                "success": color("#059669", LOGIN + " --text-success.", "Login success text."),
                "warning": color("#cd6f00", LOGIN + " --text-warning.", "Login warning text."),
            },
        },
        "font": {
            "family": {
                "display": font(
                    "saansFont, saansFont Fallback, sans-serif",
                    HOME + " h1 fontFamily saansFont. Docs body SaansReg. Login h1 Saans. Not shipped.",
                    "Display family named on the marketing page.",
                ),
                "ui": font(
                    "pxGroteskFont, pxGroteskFont Fallback, sans-serif",
                    HOME + " Start for free fontFamily pxGroteskFont, 400 loaded.",
                    "Marketing UI family. Not shipped.",
                ),
                "sans": font(
                    "Inter, -apple-system, system-ui, sans-serif",
                    LOGIN + " Body font Inter var. Inter 400 and 600 loaded.",
                    "Login family.",
                ),
                "mono": font(
                    "ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace",
                    M + " --font-mono. Docs --ifm-font-family-monospace names PxGrotesk.",
                    "Marketing mono stack.",
                ),
            }
        },
        "radius": {
            "pill": dim("9999px", HOME + " Start for free borderRadius computed as a full pill (1.67772e+07px).", "Marketing pill."),
            "login-field": dim("8px", LOGIN + " Email borderRadius 8px.", "Login field."),
            "login-button": dim("6px", LOGIN + " Sign in button borderRadius 6px.", "Login submit."),
            "card": dim("12px", "Pricing grid computed borderRadius 12px on https://retool.com/pricing.", "Pricing card."),
            "sm": dim("4px", M + " --radius-sm is 0.25rem.", "Tailwind sm."),
            "md": dim("6px", M + " --radius-md is 0.375rem.", "Tailwind md."),
            "lg": dim("8px", M + " --radius-lg is 0.5rem.", "Tailwind lg."),
            "xl": dim("12px", M + " --radius-xl is 0.75rem.", "Tailwind xl."),
            "2xl": dim("16px", M + " --radius-2xl is 1rem.", "Tailwind 2xl."),
            "3xl": dim("24px", M + " --radius-3xl is 1.5rem.", "Tailwind 3xl."),
        },
        "spacing": {
            "hairline": dim("1px", M + " --spacing-hairline is 0.0625rem. Book a demo border computed 1px.", "Hairline."),
            "2": dim("8px", M + " --spacing is 0.25rem, so step 2 is 8px. Starter prompts left padding computed 8px.", "8px."),
            "3": dim("12px", HOME + " Sign in padding computed 0 12px.", "12px."),
            "4": dim("16px", LOGIN + " Email padding computed 16px. Pricing table cell padding starts at 16px.", "16px."),
            "5": dim("20px", HOME + " Start for free padding computed 0 20px.", "20px."),
            "6": dim("24px", "Pricing card header padding computed 24px 24px 0.", "24px."),
            "nav": dim("80px", M + " --dvt-nav-height is 5rem. Header content box computed 120px including the 40px banner.", "Nav height."),
            "banner": dim("40px", M + " --dvt-banner-height is 2.5rem.", "Top banner height."),
            "button": dim("40px", HOME + " Start for free height computed 40px.", "Marketing button height."),
            "login-button": dim("44px", LOGIN + " Sign in height computed 44px.", "Login button height."),
            "field": dim("40px", LOGIN + " Email height computed 40px.", "Login field height."),
        },
        "typography": {
            "display": typography(
                {
                    "fontFamily": "{font.family.display}",
                    "fontSize": "66.7885px",
                    "fontWeight": "300",
                    "lineHeight": "70.1279px",
                    "letterSpacing": "-1.46935px",
                },
                HOME + " h1 Secure your vibe-coded apps.",
                "Homepage display.",
            ),
            "title": typography(
                {
                    "fontFamily": "{font.family.display}",
                    "fontSize": "54.7885px",
                    "fontWeight": "300",
                    "lineHeight": "1.25",
                    "letterSpacing": "-0.01em",
                },
                "h1 on https://retool.com/pricing computed 54.7885px, weight 300, saansFont.",
                "Pricing title.",
            ),
            "login-title": typography(
                {
                    "fontFamily": "Saans, sans-serif",
                    "fontSize": "36px",
                    "fontWeight": "380",
                    "lineHeight": "37.8px",
                    "letterSpacing": "-0.81576px",
                },
                LOGIN + " h1 Welcome back.",
                "Login title.",
            ),
            "plan": typography(
                {
                    "fontFamily": "{font.family.display}",
                    "fontSize": "21.3942px",
                    "fontWeight": "380",
                    "lineHeight": "26px",
                    "letterSpacing": "-0.01em",
                },
                "Plan name on pricing computed 21.3942px, weight 380.",
                "Plan name.",
            ),
            "body": typography(
                {
                    "fontFamily": "{font.family.sans}",
                    "fontSize": "16px",
                    "fontWeight": "300",
                    "lineHeight": "24px",
                    "letterSpacing": "0.01em",
                },
                M + " --font-weight-body 300, --letter-spacing-body 0.01em, --text size 16px on the body.",
                "Marketing body weight.",
            ),
            "caption": typography(
                {
                    "fontFamily": "{font.family.ui}",
                    "fontSize": "12.6971px",
                    "fontWeight": "400",
                    "lineHeight": "15.2365px",
                    "letterSpacing": "0px",
                },
                HOME + " Start for free and Pricing nav link.",
                "Marketing caption.",
            ),
            "field": typography(
                {
                    "fontFamily": "{font.family.sans}",
                    "fontSize": "16px",
                    "fontWeight": "400",
                    "lineHeight": "18.4px",
                    "letterSpacing": "0px",
                },
                LOGIN + " Email field.",
                "Login field text.",
            ),
            "button": typography(
                {
                    "fontFamily": "{font.family.sans}",
                    "fontSize": "15px",
                    "fontWeight": "600",
                    "lineHeight": "20px",
                    "letterSpacing": "0px",
                },
                LOGIN + " Sign in button.",
                "Login button text.",
            ),
        },
        "motion": {
            "duration": {
                "button": {"$type": "duration", "$value": "300ms", "$description": "Marketing button.", "$extensions": {"source": HOME + " Start for free transition-duration 0.3s."}},
                "default": {"$type": "duration", "$value": "150ms", "$description": "Default duration.", "$extensions": {"source": M + " --default-transition-duration 0.15s."}},
            },
            "easing": {
                "in-out": cubic(
                    [0.72, 0, 0.12, 1],
                    M + " --dvt-ease-in-out. Start for free timing function cubic-bezier(0.72, 0, 0.12, 1).",
                    "In-out.",
                ),
                "out": cubic([0.12, 1, 0.72, 1], M + " --dvt-ease-out.", "Out."),
                "out-soft": cubic([0.24, 0.01, 0.36, 1], M + " --dvt-ease-out-soft.", "Soft out."),
            },
        },
        "shadow": {
            "login-google": shadow(
                {
                    "color": "#0000000a",
                    "offsetX": "0px",
                    "offsetY": "1px",
                    "blur": "2px",
                    "spread": "0px",
                },
                LOGIN + " Google button box-shadow rgba(0, 0, 0, 0.04) 0px 1px 2px 0px.",
                "Google button shadow.",
            )
        },
    }

    dark = {
        "page": color("#151515", M + " --surface-background-base. Body computed rgb(21, 21, 21).", "Page."),
        "surface": color("#242424", M + " --surface-background-focused and --btn-tertiary-default-background.", "Raised surface."),
        "muted-surface": color("#0e0e0e", M + " --surface-background-muted.", "Muted surface."),
        "text": color("#e9ebdf", M + " --surface-text-primary. Body computed rgb(233, 235, 223).", "Text."),
        "muted": color("#cbccc4", M + " --surface-text-muted. Pricing note computed rgb(203, 204, 196).", "Muted text."),
        "accent": color("#518dd2", M + " --nav-items-default-selected and submit-prompt computed rgb(81, 141, 210).", "Selected accent."),
        "border": color("#e9ebdf1f", M + " --surface-details-neutral-alpha-12. Pricing card border computed rgba(233, 235, 223, 0.2), which is alpha 20.", "Hairline."),
        "border-strong": color("#8b867f", M + " --btn-secondary-gray-default-stroke. Book a demo border computed rgb(139, 134, 127).", "Strong stroke."),
        "button": color("#e9ebdf", M + " --btn-primary-default-background. Start for free computed rgb(233, 235, 223).", "Primary button."),
        "button-text": color("#151515", M + " --btn-primary-default-text. Start for free computed rgb(21, 21, 21).", "Primary button text."),
        "button-hover": color("#ffffff", M + " --btn-primary-hover-background. Hover was not held.", "Primary hover."),
        "focus": color("#151515", HOME + " Start for free :focus outline rgb(21, 21, 21) auto 1px, offset 1px.", "Marketing focus."),
        "scrim": color("#00000099", M + " --surface-lightbox-scrim is #0009.", "Scrim."),
        "footer": color("#151515", M + " --footer-background. Footer computed rgb(21, 21, 21).", "Footer."),
        "critical": color("#f15264", M + " --input-default-error-stroke.", "Error stroke."),
        "alert": color("#651722", M + " --alert-default-background.", "Alert fill."),
    }

    light = {
        "page": color("#e9ebdf", L + " --surface-background-base. Body computed rgb(233, 235, 223) after the class swap.", "Page."),
        "surface": color("#f7f8f4", L + " --surface-background-focused.", "Raised surface."),
        "muted-surface": color("#cbccc4", L + " --surface-background-muted.", "Muted surface."),
        "text": color("#151515", L + " --surface-text-primary. Body computed rgb(21, 21, 21) after the class swap.", "Text."),
        "muted": color("#242424", L + " --surface-text-muted.", "Muted text."),
        "accent": color("#518dd2", L + " --nav-items-default-selected stayed #518dd2.", "Selected accent."),
        "border": color("#1515151f", L + " --input-default-stroke.", "Hairline."),
        "border-strong": color("#8b867f", L + " Book a demo border stayed rgb(139, 134, 127) because the painted control did not restyle.", "Strong stroke."),
        "button": color("#151515", L + " --btn-primary-default-background. The painted Start for free stayed rgb(233, 235, 223).", "Primary button token."),
        "button-text": color("#e9ebdf", L + " --btn-primary-default-text.", "Primary button text token."),
        "button-hover": color("#2e2f2d", L + " --btn-primary-hover-background. Hover was not held.", "Primary hover."),
        "focus": color("#518dd2", LOGIN + " The live focus ring was read on the login field, not on a light marketing control.", "Focus."),
        "scrim": color("#00000099", "Not read after the class swap: the value is the dark set's --surface-lightbox-scrim (#0009). The light source this cited, --nav-scrolled-background (#000c), is the scrolled nav fill, not a scrim.", "Scrim."),
        "footer": color("#151515", L + " --footer-background stayed #151515.", "Footer."),
        "critical": color("#c72844", L + " --input-default-error-stroke.", "Error stroke."),
        "alert": color("#e79295", L + " --alert-default-background.", "Alert fill."),
    }

    tokens = {
        "$schema": "https://schemas.design/tokens.json",
        "core": core,
        "light": light,
        "dark": dark,
        "$themes": [
            {"id": "light", "name": "Light", "selectedTokenSets": {"core": "source", "light": "enabled"}},
            {"id": "dark", "name": "Dark", "selectedTokenSets": {"core": "source", "dark": "enabled"}},
        ],
    }
    relabel_unread(tokens)
    return tokens


# raw/measured.json is the only file in raw/. A token whose value it does not hold (in hex, rgb() or
# px form) was typed in from the capture session; its source says so (docs/EVIDENCE.md, Reconstruction).
HAND = "Reconstruction. Entered by hand at capture time; raw/measured.json holds no reading of this value. Capture note: "
RAW_TEXT = re.sub(r"\s+", "", (ROOT / "raw" / "measured.json").read_text().lower())



def _colours(text):
    """Every colour written in raw/, as (r, g, b, alpha): rgb()/rgba() with commas, spaces or a slash
    alpha, and #rgb/#rrggbb/#rrggbbaa."""
    out = []
    for m in re.finditer(r"rgba?\(\s*(\d+)[,\s]+(\d+)[,\s]+(\d+)\s*(?:[,/]\s*(\d*\.?\d+)(%?))?\s*\)", text):
        a = 1.0 if m.group(4) is None else float(m.group(4)) / (100 if m.group(5) else 1)
        out.append((int(m.group(1)), int(m.group(2)), int(m.group(3)), a))
    for m in re.finditer(r"#([0-9a-f]{8}|[0-9a-f]{6}|[0-9a-f]{3})(?![0-9a-z])", text):
        out.append(_hex(m.group(0)))
    return out


def _hex(value):
    h = value.lstrip("#")
    if len(h) == 3:
        h = "".join(c * 2 for c in h)
    return (int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16), int(h[6:8], 16) / 255 if len(h) == 8 else 1.0)


RAW_COLOURS = _colours((ROOT / "raw" / "measured.json").read_text().lower())


def colour_in_raw(value):
    """A hex colour is backed only by a raw colour with the same channels and the same opacity."""
    r, g, b, a = _hex(value)
    return any((r, g, b) == c[:3] and abs(a - c[3]) <= 0.01 for c in RAW_COLOURS)

def in_raw(value):
    v = str(value).strip().lower()
    forms = {v.replace(" ", "")}
    if re.fullmatch(r"#[0-9a-f]{6}([0-9a-f]{2})?", v):
        return colour_in_raw(v)
    if "," in v and not v.startswith(("#", "rgb")):
        forms.add('"' + v.split(",")[0].strip().strip("'\"") + '"')  # a font stack: its computed first family
    m = re.fullmatch(r"(\d*\.?\d+)ms", v)
    if m:
        forms.add(f"{float(m.group(1)) / 1000:g}s")
    m = re.fullmatch(r"(\d*\.?\d+)px", v)
    if m:
        n = float(m.group(1))
        forms |= {f":{n:g},", f":{n:g}}}"}  # a box size stored as a bare number ("height": 40)
    if v == "9999px":
        forms |= {"16777215px", "16777200px", "1.67772e+07px"}  # the full pill a computed rounded-full radius reports
    return any(f in RAW_TEXT for f in forms)


def leaves(node, path=""):
    for k, v in node.items():
        if k.startswith("$") or not isinstance(v, dict):
            continue
        here = f"{path}.{k}" if path else k
        if "$value" in v:
            yield here, v
        else:
            yield from leaves(v, here)


def relabel_unread(tokens):
    for _, tok in leaves(tokens):
        value = tok["$value"]
        if isinstance(value, str) and value.startswith("{"):
            continue  # an alias carries the evidence of the token it names
        if isinstance(value, (str, int, float)) and not in_raw(value):
            tok["$extensions"]["source"] = HAND + tok["$extensions"]["source"]


def write():
    (ROOT / "tokens.json").write_text(json.dumps(build(), indent=2) + "\n")
    print("wrote tokens.json")


if __name__ == "__main__":
    write()
