#!/usr/bin/env python3
"""Build tokens.json from raw/readings.json.

Every colour, length and font name in this file is a value read from
spyglass.so on 2026-11-19: a declared custom property (hex, kept over the
duplicate lab() declaration) or a computed style on a live element. A role
that was not on the public page is omitted. Dark shadcn and data-spyglass-theme
values are stylesheet declarations, labelled as such, because the public pages
ship html.light and never mount those selectors.
"""
from __future__ import annotations

import json
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
RAW = json.loads((HERE / "raw" / "readings.json").read_text())

SRC_DECL = (
    "Measured. Declared custom property on :root in "
    "https://spyglass.so/_next/static/chunks/*.css, read from the live home page "
    "on 2026-11-19 (hex declaration kept; the duplicate lab() declaration is the same colour)."
)
SRC_DECL_DARK = (
    "Measured. Declared custom property on .dark in the same stylesheet. "
    "The public pages set class light on html and do not mount .dark, so this is "
    "the stylesheet value, not a computed style of a visible dark page."
)
SRC_SPY_LIGHT = (
    "Measured. Declared on [data-spyglass-theme=light] in the home stylesheet. "
    "The public marketing pages do not set data-spyglass-theme, so this token is "
    "the declaration, not a computed style of a visible element."
)
SRC_SPY_DARK = (
    "Measured. Declared on [data-spyglass-theme=dark] in the home stylesheet. "
    "Not mounted on the public pages captured here."
)


def color(value, source):
    return {"$value": value, "$type": "color", "$extensions": {"source": source}}


def dim(value, source):
    return {"$value": value, "$type": "dimension", "$extensions": {"source": source}}


def font(value, source):
    return {"$value": value, "$type": "fontFamily", "$extensions": {"source": source}}


def weight(value, source):
    return {"$value": value, "$type": "fontWeight", "$extensions": {"source": source}}


def number(value, source):
    return {"$value": value, "$type": "number", "$extensions": {"source": source}}


def text(value, source):
    return {"$value": value, "$type": "other", "$extensions": {"source": source}}


def cubic(value, source):
    return {"$value": value, "$type": "cubicBezier", "$extensions": {"source": source}}


def shadow(value, source):
    return {"$value": value, "$type": "shadow", "$extensions": {"source": source}}


def duration(value, source):
    return {"$value": value, "$type": "duration", "$extensions": {"source": source}}


def comp_source(where):
    return f"Measured. Computed style on {where}, spyglass.so, 2026-11-19, desktop 1440x900 unless noted."


LIGHT = RAW["declared"]["light"]
DARK = RAW["declared"]["dark"]
SPY_L = RAW["declared"]["spyglassLight"]
SPY_D = RAW["declared"]["spyglassDark"]
COMP = RAW["computed"]


def pick(table, name):
    if name not in table:
        raise SystemExit(f"missing declared token {name}")
    return table[name]


core = {
    "font": {
        "sans": font(
            'Geist, "Geist Fallback", sans-serif',
            comp_source("document.body font-family (Geist variable font, weight 100-900, woff2)"),
        ),
        "display": font(
            '"Familjen Grotesk", "Familjen Grotesk Fallback", sans-serif',
            comp_source("home h1 font-family"),
        ),
        "mono": font(
            '"Geist Mono", "Geist Mono Fallback", ui-monospace, monospace',
            "Measured. @font-face and --font-geist-mono on body (geist_mono variable class). Not used as body text on the public pages.",
        ),
    },
    "fontWeight": {
        "regular": weight("400", SRC_DECL + " --font-weight-normal."),
        "medium": weight("500", SRC_DECL + " --font-weight-medium."),
        "semibold": weight("600", SRC_DECL + " --font-weight-semibold."),
        "bold": weight("700", SRC_DECL + " --font-weight-bold."),
    },
    "fontSize": {
        "xs": dim(pick(LIGHT, "--text-xs"), SRC_DECL + " --text-xs."),
        "sm": dim(pick(LIGHT, "--text-sm"), SRC_DECL + " --text-sm."),
        "base": dim(pick(LIGHT, "--text-base"), SRC_DECL + " --text-base."),
        "lg": dim(pick(LIGHT, "--text-lg"), SRC_DECL + " --text-lg."),
        "xl": dim(pick(LIGHT, "--text-xl"), SRC_DECL + " --text-xl."),
        "2xl": dim(pick(LIGHT, "--text-2xl"), SRC_DECL + " --text-2xl."),
        "3xl": dim(pick(LIGHT, "--text-3xl"), SRC_DECL + " --text-3xl."),
        "4xl": dim(pick(LIGHT, "--text-4xl"), SRC_DECL + " --text-4xl."),
        "5xl": dim(pick(LIGHT, "--text-5xl"), SRC_DECL + " --text-5xl."),
        "display": dim("70px", comp_source("home h1 at 1440 (class md:text-[70px])")),
        "displayPhone": dim("46px", "Derived. Authored class text-[46px] on the home h1, the base size before the md: breakpoint. Not recomputed at 390 in this pass."),
        "pageTitle": dim("40px", comp_source("pricing and FAQ h1")),
        "section": dim("56px", comp_source("pricing closing heading 'Stop screenshotting at midnight'")),
        "authTitle": dim("28px", comp_source("sign-in h1")),
    },
    "lineHeight": {
        "body": dim("24px", comp_source("document.body line-height")),
        "sm": dim("20px", comp_source("header button and primary link line-height")),
        "display": dim("70px", comp_source("home h1 line-height (leading-none at 70px)")),
        "pageTitle": dim("44px", comp_source("pricing h1 line-height")),
        "authTitle": dim("32px", comp_source("sign-in h1 line-height")),
    },
    "letterSpacing": {
        "display": dim("-2.1px", comp_source("home h1 letter-spacing (tracking-[-0.0225em] at 70px)")),
        "pageTitle": dim("-1.2px", comp_source("pricing h1 letter-spacing")),
        "authTitle": dim("-0.84px", comp_source("sign-in h1 letter-spacing")),
        "nav": dim("-0.22px", comp_source("header Product button letter-spacing")),
        "familjen": text("-0.03em", SRC_DECL + " --font-familjen-tracking."),
    },
    "space": {
        "1": dim("4px", "Derived. --spacing is 0.25rem (4px at the 16px root) on :root."),
        "2": dim("8px", "Derived. 2 x --spacing. Also the primary button's block padding."),
        "3": dim("12px", "Derived. 3 x --spacing. Header nav button inline padding and the prompt card padding at sm."),
        "4": dim("16px", "Derived. 4 x --spacing. Primary button inline padding."),
        "5": dim("20px", comp_source("FAQ row button padding")),
        "header": dim("59px", comp_source("header height at 1440")),
    },
    "radius": {
        "xs": dim(pick(LIGHT, "--radius-xs"), SRC_DECL + " --radius-xs."),
        "sm": dim("6px", comp_source("primary link, Sign in link, and sign-in field wrapper border-radius (rounded-sm / rounded-[6px])")),
        "md": dim("8px", comp_source("home prompt card and FAQ row wrapper border-radius; also the phone menu button")),
        "lg": dim(pick(LIGHT, "--radius"), SRC_DECL + " --radius (0.625rem, 10px)."),
        "xl": dim(pick(LIGHT, "--radius-2xl"), SRC_DECL + " --radius-2xl."),
        "2xl": dim("24px", comp_source("open Product menu panel border-radius")),
        "3xl": dim(pick(LIGHT, "--radius-3xl"), SRC_DECL + " --radius-3xl."),
        "4xl": dim(pick(LIGHT, "--radius-4xl"), SRC_DECL + " --radius-4xl."),
        "pill": dim("9999px", comp_source("header nav button border-radius (computed as a full pill)")),
        "chip": dim("20px", comp_source("FAQ category chip border-radius")),
    },
    "borderWidth": {
        "hairline": dim("1px", comp_source("Sign in link and sign-in field wrapper border-top-width")),
    },
    "size": {
        "buttonMd": dim("36px", comp_source("primary link and Sign in link height")),
        "buttonAuth": dim("44px", comp_source("Continue with Google button height on /sign-in")),
        "field": dim("40px", comp_source("sign-in email field wrapper height (h-10)")),
        "nav": dim("39px", comp_source("header Product button height")),
        "iconButton": dim("40px", comp_source("phone Open menu button, 390px viewport")),
        "icon": dim("16px", comp_source("header and prompt inline SVG icons")),
        "menu": dim("380px", comp_source("open Product menu panel width")),
    },
    "shadow": {
        "menu": shadow(
            "0px 24px 60px -15px rgba(0, 0, 0, 0.18)",
            comp_source("open Product menu panel box-shadow"),
        ),
    },
    "motion": {
        "duration": {
            "fast": duration("150ms", SRC_DECL + " --default-transition-duration (.15s)."),
        },
        "easing": {
            "standard": cubic(
                [0.4, 0, 0.2, 1],
                SRC_DECL + " --default-transition-timing-function and --ease-in-out.",
            ),
            "out": cubic([0, 0, 0.2, 1], SRC_DECL + " --ease-out."),
        },
    },
    "layout": {
        "desktop": dim("1440px", "Measured. Playwright viewport innerWidth on the desktop pass."),
        "phone": dim("390px", "Measured. Playwright viewport innerWidth on the phone pass."),
        "contentPrompt": dim("672px", comp_source("home prompt card width")),
        "authColumn": dim("517px", comp_source("sign-in form column width")),
    },
}

# Semantic colours used on the public light pages, plus declared theme tokens.
light_color = {
    "page": color("#ffffff", SRC_DECL + " --background. Computed body background is lab(100 0 0), the same white."),
    "ink": color("#0a0a0a", SRC_DECL + " --foreground. Header computed color is rgb(10, 10, 10)."),
    "inkSoft": color("#212121", comp_source("home h1 color rgb(33, 33, 33)")),
    "nav": color("#3b3b3b", comp_source("header Product button color rgb(59, 59, 59)")),
    "muted": color("#737373", SRC_DECL + " --muted-foreground."),
    "surface": color("#ffffff", SRC_DECL + " --card."),
    "surfaceMuted": color("#f5f5f5", SRC_DECL + " --muted and --secondary."),
    "surfaceSection": color("#fafafa", comp_source("home section background rgb(250, 250, 250)")),
    "surfaceInverse": color("#212121", comp_source("home dark band background rgb(33, 33, 33)")),
    "footer": color("#292929", comp_source("footer background rgb(41, 41, 41)")),
    "onInverse": color("#ffffff", comp_source("inverse section heading color rgb(255, 255, 255)")),
    "primary": color("#171717", SRC_DECL + " --primary. Primary link computed background is lab(7.78201 0 0), the same near-black."),
    "onPrimary": color("#fafafa", SRC_DECL + " --primary-foreground."),
    "border": color("#e5e5e5", SRC_DECL + " --border. Sign in link computed border is lab(90.952 0 0), the same grey."),
    "fieldBorder": color("#d9d9d9", comp_source("sign-in email wrapper border-top-color rgb(217, 217, 217)")),
    "destructive": color("#e40014", SRC_DECL + " --destructive. Declared, not painted on the public pages captured."),
    "onDestructive": color("#fafafa", SRC_DECL + " --destructive-foreground."),
    "ring": color("#a1a1a1", SRC_DECL + " --ring. Keyboard focus on the public buttons did not paint a visible outline (outline-style none)."),
    "lime": color("#d5fd00", SRC_DECL + " --accent-lime. Declared on :root and .dark. Not painted on the public marketing pages."),
    "footerLink": color("rgba(255, 255, 255, 0.8)", comp_source("footer Pricing link color")),
    "scrim": color("rgba(255, 255, 255, 0.7)", comp_source("open Product menu panel background")),
    "navHover": color("rgba(0, 0, 0, 0.04)", comp_source("header Product button background while its menu is open")),
    "primaryHover": color("rgba(23, 23, 23, 0.9)", "Measured. Primary link background on real hover: oklab(0.205 0 0 / 0.9), the --primary colour at 90%."),
    "outlineHover": color("#f5f5f5", "Measured. Sign in link background on real hover, lab(96.52 0 0), the same as --secondary."),
}

dark_color = {
    "page": color("#161616", SRC_DECL_DARK + " --background."),
    "ink": color("#fafafa", SRC_DECL_DARK + " --foreground."),
    "surface": color("#171717", SRC_DECL_DARK + " --card."),
    "surfaceMuted": color("#262626", SRC_DECL_DARK + " --muted."),
    "primary": color("#fafafa", SRC_DECL_DARK + " --primary."),
    "onPrimary": color("#0a0a0a", SRC_DECL_DARK + " --primary-foreground."),
    "border": color("#ffffff1a", SRC_DECL_DARK + " --border."),
    "input": color("#ffffff26", SRC_DECL_DARK + " --input."),
    "muted": color("#a1a1a1", SRC_DECL_DARK + " --muted-foreground."),
    "destructive": color("#ff6568", SRC_DECL_DARK + " --destructive."),
    "onDestructive": color("#0a0a0a", SRC_DECL_DARK + " --destructive-foreground."),
    "ring": color("#737373", SRC_DECL_DARK + " --ring."),
    "lime": color("#d5fd00", SRC_DECL_DARK + " --accent-lime."),
    "popover": color("#171717", SRC_DECL_DARK + " --popover."),
}

# Product theme used inside the signed-in app chrome. Declared, not mounted publicly.
def spy(table, source):
    out = {}
    for key, value in table.items():
        name = key.removeprefix("--spyglass-").replace("-", "_")
        # keep readable camel-ish names
        parts = key.removeprefix("--spyglass-").split("-")
        name = parts[0] + "".join(p.capitalize() for p in parts[1:])
        if value in ("transparent",) or value.startswith("inset") or " " in value and not value.startswith("#") and not value.startswith("rgb"):
            if value.startswith("inset") or "px" in value:
                out[name] = shadow(value, source + f" {key}.")
            else:
                out[name] = text(value, source + f" {key}.")
        elif value.startswith("#") or value.startswith("rgb") or value in ("white", "transparent"):
            out[name] = color(value if value != "white" else "#ffffff", source + f" {key}.")
        else:
            out[name] = text(value, source + f" {key}.")
    return out


chart_light = {
    "1": color("#f05100", SRC_DECL + " --chart-1."),
    "2": color("#009588", SRC_DECL + " --chart-2."),
    "3": color("#104e64", SRC_DECL + " --chart-3."),
    "4": color("#fcbb00", SRC_DECL + " --chart-4."),
    "5": color("#f99c00", SRC_DECL + " --chart-5."),
}
chart_dark = {
    "1": color("#1447e6", SRC_DECL_DARK + " --chart-1."),
    "2": color("#00bb7f", SRC_DECL_DARK + " --chart-2."),
    "3": color("#f99c00", SRC_DECL_DARK + " --chart-3."),
    "4": color("#ac4bff", SRC_DECL_DARK + " --chart-4."),
    "5": color("#ff2357", SRC_DECL_DARK + " --chart-5."),
}

tokens = {
    "$schema": "https://design-tokens.github.io/community-group/format/",
    "core": core,
    "light": {
        "color": light_color,
        "chart": chart_light,
        "spyglass": spy(SPY_L, SRC_SPY_LIGHT),
    },
    "dark": {
        "color": dark_color,
        "chart": chart_dark,
        "spyglass": spy(SPY_D, SRC_SPY_DARK),
    },
    "$themes": [
        {"id": "light", "name": "light", "selectedTokenSets": {"core": "enabled", "light": "enabled"}},
        {"id": "dark", "name": "dark", "selectedTokenSets": {"core": "source", "dark": "enabled"}},
    ],
    "$extensions": {
        "notTokenised": [
            "Hover on the primary link changes background to oklab(0.205 0 0 / 0.9). Recorded as light.color.primaryHover.",
            "Keyboard focus on Sign in and the primary link left outline-style none. No visible focus ring was computed.",
            "Pressed, loading, error, checkbox, radio, switch, select, textarea, toast, dialog, tooltip, avatar and table row states were not on the public pages.",
            "data-spyglass-theme tokens are declared and tokenised under light.spyglass and dark.spyglass. They are not computed on the public pages.",
            ".dark tokens are declared and tokenised under dark.color. The public pages do not mount .dark.",
        ]
    },
}

# silence unused
_ = COMP

out = HERE / "tokens.json"
out.write_text(json.dumps(tokens, indent=2) + "\n")
print(f"wrote {out} ({out.stat().st_size} bytes)")
