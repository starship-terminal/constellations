#!/usr/bin/env python3
"""Build systems/miro/tokens.json from raw/pricing-root-vars.json and raw/components-computed.json.

The pricing page is the token source. Its :root custom properties are the product's
named colours, shadows and radii. Component measurements fill the roles those names
do not cover (page background, auth card, error text). Light only: no dark theme
was on any public page.
"""
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
VARS = json.loads((RAW / "pricing-root-vars.json").read_text())["variables"]
COMP = json.loads((RAW / "components-computed.json").read_text())

SRC_VAR = "Measured. getComputedStyle(document.documentElement) on https://miro.com/pricing/, 2026-11-18, viewport 1169x731."
SRC_COMP = "Measured. Computed style on a live element, T3 preview browser, 2026-11-18."
# raw/pricing-root-vars.json excludes --tw-* and --wcds-* by design, so no file in raw/ holds those
# readings: they were typed in from the capture session (docs/EVIDENCE.md, Reconstruction).
SRC_TW = ("Reconstruction. Entered by hand at capture time; no file in raw/ holds this reading "
          "(raw/pricing-root-vars.json excludes --tw-* Tailwind names). Capture note:")
SRC_WCDS = ("Reconstruction. Read from the wrong element: --wcds-* names belong to the cookie-consent banner's "
            "design system, not Miro's, and raw/pricing-root-vars.json excludes them; recapture needed. Capture note:")


def color(value):
    value = str(value).strip()
    hex8 = re.fullmatch(r"#([0-9a-fA-F]{8})", value)
    if hex8:
        raw = hex8.group(1).lower()
        r, g, b, a = (int(raw[i:i + 2], 16) for i in (0, 2, 4, 6))
        if a == 255:
            return "#%02x%02x%02x" % (r, g, b)
        return "rgba(%d, %d, %d, %g)" % (r, g, b, round(a / 255, 3))
    hex6 = re.fullmatch(r"#([0-9a-fA-F]{6})", value)
    if hex6:
        return "#" + hex6.group(1).lower()
    hex3 = re.fullmatch(r"#([0-9a-fA-F]{3})", value)
    if hex3:
        return "#" + "".join(ch * 2 for ch in hex3.group(1).lower())
    rgb = re.fullmatch(r"rgba?\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*(?:,\s*([\d.]+)\s*)?\)", value)
    if rgb:
        r, g, b = (int(rgb.group(i)) for i in (1, 2, 3))
        alpha = rgb.group(4)
        if alpha is None or float(alpha) >= 1:
            return "#%02x%02x%02x" % (r, g, b)
        return "rgba(%d, %d, %d, %g)" % (r, g, b, float(alpha))
    if value.startswith("oklch(") or value.startswith("lab("):
        return value
    raise ValueError("colour not understood: " + value)


def token(value, type_, source, extra=None):
    out = {"$value": value, "$type": type_, "$extensions": {"source": source}}
    if extra:
        out["$extensions"].update(extra)
    return out


def var_color(name):
    return token(color(VARS[name]), "color", SRC_VAR + " " + name)


def comp_color(value, where):
    return token(color(value), "color", SRC_COMP + " " + where)


def dim(value, source):
    return token(value, "dimension", source)


CORE_COLORS = {
    "black": "--colors-black",
    "white": "--colors-white",
    "transparent": "--colors-transparent",
    "miroYellow": "--colors-miro-yellow",
    "blue": {str(step): "--colors-blue-" + str(step) for step in (
        50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900, 950)},
    "gray": {str(step): "--colors-gray-" + str(step) for step in (
        50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900, 950)},
    "green": {str(step): "--colors-green-" + str(step) for step in (
        50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900, 950)},
    "red": {str(step): "--colors-red-" + str(step) for step in (
        50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900, 950)},
    "yellow": {str(step): "--colors-yellow-" + str(step) for step in (
        50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900, 950)},
    "coral": {"500": "--colors-coral-500"},
    "cyan": {"500": "--colors-cyan-500"},
    "lilac": {"200": "--colors-lilac-200", "450": "--colors-lilac-450", "500": "--colors-lilac-500"},
    "lime": {"400": "--colors-lime-400"},
    "moss": {"450": "--colors-moss-450"},
    "ocean": {"500": "--colors-ocean-500"},
    "orange": {"500": "--colors-orange-500"},
    "pink": {"400": "--colors-pink-400"},
    "sunshine": {"450": "--colors-sunshine-450"},
    "teal": {"350": "--colors-teal-350"},
}


def walk_colors(node):
    if isinstance(node, str):
        return var_color(node)
    return {key: walk_colors(value) for key, value in node.items()}


def shadow_token(name):
    return token(VARS[name], "shadow", SRC_VAR + " " + name)


pricing = COMP["pages"]["pricing"]
login = COMP["pages"]["login"]
signup = COMP["pages"]["signup"]
home = COMP["pages"]["home"]

doc = {
    "$schema": "https://design-tokens.org/schema.json",
    "core": {
        "color": walk_colors(CORE_COLORS),
        "font": {
            "family": {
                "display": token(
                    "roobertPROLocal, \"roobertPROLocal Fallback\", Helvetica, Arial, sans-serif",
                    "fontFamily",
                    SRC_COMP + " body on https://miro.com/pricing/."),
                "pro": token(
                    "\"Roobert PRO\", Helvetica, Arial, sans-serif",
                    "fontFamily",
                    SRC_COMP + " body on https://miro.com/login/."),
                "noto": token(
                    "\"Noto Sans\", \"Noto Sans Fallback\", system-ui, sans-serif",
                    "fontFamily",
                    SRC_COMP + " pricing outline button."),
                "apris": token(
                    home["h1"]["fontFamily"],
                    "fontFamily",
                    SRC_COMP + " h1 on https://miro.com/."),
            },
            "weight": {
                "regular": token("400", "fontWeight", SRC_TW + " --tw-font-weight-regular."),
                "medium": token("500", "fontWeight", SRC_TW + " --tw-font-weight-medium."),
                "semibold": token("600", "fontWeight", SRC_TW + " --tw-font-weight-semibold."),
                "bold": token("700", "fontWeight", SRC_TW + " --tw-font-weight-bold."),
            },
            "size": {
                "xs": dim("0.75rem", SRC_TW + " --tw-text-xs."),
                "sm": dim("0.875rem", SRC_TW + " --tw-text-sm."),
                "base": dim("1rem", SRC_TW + " --tw-text-base."),
                "lg": dim("1.125rem", SRC_TW + " --tw-text-lg."),
                "xl": dim("1.25rem", SRC_TW + " --tw-text-xl."),
                "2xl": dim("1.5rem", SRC_TW + " --tw-text-2xl."),
                "3xl": dim("1.875rem", SRC_TW + " --tw-text-3xl."),
                "4xl": dim("2.25rem", SRC_TW + " --tw-text-4xl."),
                "5xl": dim("3rem", SRC_TW + " --tw-text-5xl."),
                "display": dim("48px", SRC_COMP + " pricing h1 font-size."),
                "authTitle": dim("44px", SRC_COMP + " login h1 font-size."),
                "plan": dim("32px", SRC_COMP + " pricing plan title font-size."),
            },
        },
        "radius": {
            "sm": dim("0.25rem", SRC_WCDS + " --wcds-border-radius-sm."),
            "md": dim("0.5rem", SRC_WCDS + " --wcds-border-radius."),
            "control": dim("8px", SRC_COMP + " pricing primary button border-radius."),
            "lg": dim("0.75rem", SRC_WCDS + " --wcds-border-radius-lg."),
            "card": dim("12px", SRC_COMP + " login card border-radius."),
            "xl": dim("1rem", SRC_WCDS + " --wcds-border-radius-xl."),
            "plan": dim("20px", SRC_COMP + " pricing plan card border-radius."),
            "pill": dim("40px", SRC_COMP + " pricing billing toggle border-radius."),
        },
        "space": {
            "100": dim("0.5rem", SRC_WCDS + " --wcds-space-100."),
            "200": dim("1rem", SRC_WCDS + " --wcds-space-200."),
            "300": dim("1.5rem", SRC_WCDS + " --wcds-space-300."),
            "nav": dim("8px", SRC_COMP + " pricing nav item padding-block."),
            "card": dim("24px", SRC_COMP + " pricing plan card padding."),
            "auth": dim("48px", SRC_COMP + " login card padding."),
        },
        "shadow": {
            "50": shadow_token("--shadow-50"),
            "100": shadow_token("--shadow-100"),
            "200": shadow_token("--shadow-200"),
            "500": shadow_token("--shadow-500"),
        },
        "motion": {
            "duration": {
                "fast": token("150ms", "duration", SRC_TW + " --tw-default-transition-duration, .15s."),
                "cookie": token("250ms", "duration", "Reconstruction. Read from the wrong element: the OneTrust Accept All Cookies button is the consent banner, not Miro; recapture needed from a Miro control. The reading is raw/components-computed.json pages.home.cookieBanner.accept.transition, background, color 0.25s ease."),
            },
            "easing": {
                "standard": token([0.4, 0, 0.2, 1], "cubicBezier", SRC_TW + " --tw-ease-in-out."),
                "out": token([0, 0, 0.2, 1], "cubicBezier", SRC_TW + " --tw-ease-out."),
            },
        },
    },
    "light": {
        "page": comp_color(pricing["bodyBackground"], "body background on https://miro.com/pricing/."),
        "pageWarm": comp_color(login["bodyBackground"], "body background on https://miro.com/login/."),
        "pageHome": comp_color(home["bodyBackground"], "body background on https://miro.com/."),
        "surface": var_color("--colors-white"),
        "text": var_color("--text-colors-text-default-text-primary"),
        "textMuted": var_color("--text-colors-text-default-text-secondary"),
        "textOnAccent": var_color("--text-colors-text-default-text-tertiary"),
        "accent": var_color("--button-primary-bg-btn-primary-idle"),
        "accentHover": var_color("--button-primary-bg-btn-primary-hover"),
        "accentPressed": var_color("--button-primary-bg-btn-primary-down"),
        "accentBorder": var_color("--colors-blue-400"),
        "authAction": comp_color(login["submit"]["background"], "login Continue with email background."),
        "border": var_color("--button-outline-border-btn-outline-idle"),
        "borderSubtle": var_color("--border-colors-border-actionable-border-default-idle"),
        "divider": var_color("--border-colors-divider-divider-light"),
        "focus": var_color("--border-colors-border-actionable-border-default-active"),
        "error": var_color("--text-colors-text-semantic-text-error-idle"),
        "errorField": comp_color("rgb(220, 53, 69)", "signup invalid email field border."),
        "errorText": comp_color(signup["error"]["color"], "signup .invalid-feedback color."),
        "success": var_color("--text-colors-text-semantic-text-success-idle"),
        "warning": var_color("--colors-yellow-400"),
        "yellow": var_color("--colors-miro-yellow"),
        "disabled": var_color("--text-colors-text-actionable-text-default-disabled"),
        "link": var_color("--text-colors-text-actionable-text-default-idle"),
        "linkVisited": var_color("--text-colors-text-actionable-text-default-visited"),
        "toggleTrack": comp_color(pricing["billingToggle"]["trackBackground"], "pricing billing toggle track."),
        "authCardBorder": comp_color("rgb(68, 71, 73)", "login card border color."),
        "featuredPlanBorder": comp_color("rgb(56, 89, 255)", "pricing Business card border."),
    },
    "$themes": [
        {
            "id": "light",
            "name": "Light",
            "selectedTokenSets": {"core": "source", "light": "enabled"},
            "$extensions": {"source": "Public pages had no dark theme switch. Pricing, product, login and signup all painted light."},
        }
    ],
}

# Drop transparent from the colour ramp: DTCG colour with alpha 0 is fine, but
# DESIGN.md colour export wants opaque roles. Keep it; catalog resolves hex and oklch.
if __name__ == "__main__":
    (HERE / "tokens.json").write_text(json.dumps(doc, indent=2) + "\n")
    print("wrote", HERE / "tokens.json")
