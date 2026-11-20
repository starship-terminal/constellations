#!/usr/bin/env python3
"""Build tokens.json from raw/readings.json for the Microsoft Teams public site.

Every colour, size and family below is a computed style or a resolved
--ds-app-* custom property from the 2026-11-19 capture. Re-running this
script on the same readings writes the same bytes.
"""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
RAW = json.loads((HERE / "raw" / "readings.json").read_text())
RES = RAW["vars"]["resolved"]
SRC = "computed on https://www.microsoft.com/en-us/microsoft-teams/group-chat-software/ 2026-11-19, 1440x900, signed out"

def color(value, source):
    return {"$type": "color", "$value": value, "$extensions": {"source": source}}

def dim(value, source):
    return {"$type": "dimension", "$value": value, "$extensions": {"source": source}}

def num(value, source):
    return {"$type": "number", "$value": value, "$extensions": {"source": source}}

def font_family(value, source):
    return {"$type": "fontFamily", "$value": value, "$extensions": {"source": source}}

def typography(family, size, weight, line_height, source, tracking=None):
    value = {
        "fontFamily": family,
        "fontSize": size,
        "fontWeight": weight,
        "lineHeight": line_height,
    }
    if tracking:
        value["letterSpacing"] = tracking
    return {"$type": "typography", "$value": value, "$extensions": {"source": source}}

def var(name):
    if name not in RES:
        raise SystemExit(f"missing {name}")
    return RES[name]

def rem_px(value):
    value = value.strip()
    if value.endswith("rem"):
        px = float(value[:-3]) * 16
        text = ("%g" % round(px, 3)) + "px"
        return text
    if value.endswith("px"):
        return value
    raise SystemExit(f"not a length: {value}")

# Painted roles. #5d5bd4 is the computed fill of a.btn (rgb(93, 91, 212)),
# not --ds-app-color-interactive-primary-bg-default (#0078d4), which the
# marketing buttons do not use.
PAINTED = "Measured computed style, " + SRC
DECLARED = "Resolved --ds-app-* on :root, main-teams.css, " + SRC

core = {
    "font": {
        "family": {
            "display": font_family(
                ["Segoe UI Variable Display", "Segoe UI", "segoeui", "Helvetica Neue", "helvetica", "arial", "sans-serif"],
                "computed font-family on h1, " + SRC,
            ),
            "text": font_family(
                ["Segoe UI Variable Text", "Segoe UI", "segoeui", "Helvetica Neue", "helvetica", "arial", "sans-serif"],
                "computed font-family on a.btn.btn--md and body, " + SRC,
            ),
            "uhf": font_family(
                ["Segoe UI", "SegoeUI", "Helvetica Neue", "Helvetica", "Arial", "sans-serif"],
                "computed font-family on header.uhf-header links, " + SRC,
            ),
        }
    },
    "fontSize": {
        "nav": dim("13px", "computed on header Try for free / Sign in, " + SRC),
        "body-xs": dim(rem_px(var("--ds-app-type-body-xs-font-size")), DECLARED + " --ds-app-type-body-xs-font-size"),
        "body-s": dim(rem_px(var("--ds-app-type-body-s-font-size")), DECLARED + " --ds-app-type-body-s-font-size"),
        "button": dim("15px", "computed on a.btn.btn--md Download now, " + SRC),
        "body": dim(rem_px(var("--ds-app-type-body-m-font-size")), DECLARED + " --ds-app-type-body-m-font-size; also computed body"),
        "body-l": dim(rem_px(var("--ds-app-type-body-l-font-size")), DECLARED + " --ds-app-type-body-l-font-size"),
        "heading-xs": dim(rem_px(var("--ds-app-type-heading-xs-font-size")), DECLARED),
        "heading-s": dim(rem_px(var("--ds-app-type-heading-s-font-size")), DECLARED),
        "heading-m": dim(rem_px(var("--ds-app-type-heading-m-font-size")), DECLARED + "; computed h2 Ask Microsoft is 48px"),
        "hero": dim("62px", "computed font-size on home h1, " + SRC),
        "heading-l": dim(rem_px(var("--ds-app-type-heading-l-font-size")), DECLARED),
    },
    "spacing": {
        "2": dim("2px", "derived from the 2px transparent border on a.btn, " + SRC),
        "4": dim("4px", "computed padding-top on header Sign in, " + SRC),
        "8": dim(rem_px(var("--ds-app-space-micro-xs")), DECLARED + " --ds-app-space-micro-xs; button padding-block"),
        "12": dim(rem_px(var("--ds-app-space-micro-s")), DECLARED + " --ds-app-space-micro-s"),
        "16": dim(rem_px(var("--ds-app-space-micro-m")), DECLARED + " --ds-app-space-micro-m; button padding-inline"),
        "24": dim(rem_px(var("--ds-app-space-micro-l")), DECLARED + " --ds-app-space-micro-l"),
        "32": dim(rem_px(var("--ds-app-space-micro-xl")), DECLARED + " --ds-app-space-micro-xl"),
        "48": dim(rem_px(var("--ds-app-space-micro-2xl")), DECLARED + " --ds-app-space-micro-2xl"),
        "72": dim(rem_px(var("--ds-app-space-micro-3xl")), DECLARED + " --ds-app-space-micro-3xl"),
        "96": dim(rem_px(var("--ds-app-space-micro-4xl")), DECLARED + " --ds-app-space-micro-4xl"),
    },
    "radius": {
        "uhf": dim("3px", "computed border-radius on header Try for free / Sign in, " + SRC),
        "control": dim("8px", "computed border-radius on a.btn.btn--md and the Ask Microsoft field, " + SRC),
        "pill": dim("999px", "observed fully rounded segment on the pricing audience switcher; not a named --ds-app radius"),
    },
    "typography": {
        "hero": typography("{core.font.family.display}", "62px", 500, "72px",
                           "computed h1, " + SRC, "-1.55px"),
        "heading-m": typography("{core.font.family.display}", "48px", 500, "56px",
                                "computed h2 Ask Microsoft, " + SRC),
        "body": typography("{core.font.family.text}", "16px", 400, "24px",
                           "computed body, " + SRC),
        "button": typography("{core.font.family.text}", "15px", 600, "22px",
                             "computed a.btn.btn--md, " + SRC, "-0.3px"),
        "nav": typography("{core.font.family.uhf}", "13px", 400, "20px",
                          "computed header action links, " + SRC),
        "link": typography("{core.font.family.text}", "14px", 600, "20px",
                           "computed a.link Learn more, " + SRC),
        "eyebrow": typography("{core.font.family.text}", rem_px(var("--ds-app-type-label-eyebrow-font-size")), 600, rem_px(var("--ds-app-type-label-eyebrow-line-height")),
                              DECLARED + " --ds-app-type-label-eyebrow-*"),
        "footer": typography("{core.font.family.uhf}", "11px", 400, "16px",
                             "computed footer, " + SRC),
    },
}

light = {
    "background": {
        "page": color("#f7f7f7", "computed background-color on body, " + SRC),
        "header": color("#ffffff", "computed background-color on header.uhf-header, " + SRC),
        "footer": color("#f2f2f2", "computed background-color on footer, " + SRC),
        "action": color("#5d5bd4", "computed background-color on a.btn Download now and header Try for free, rgb(93, 91, 212), " + SRC),
        "action-hover": color("#5553c1", "computed background-color on a.btn Download now while hovered, rgb(85, 83, 193), " + SRC),
        "hero": color("#f4fafd", DECLARED + " --ds-app-color-base-default-bg-opt1; the hero wash sits over this declared stop"),
        "hero-deep": color("#dceef8", DECLARED + " --ds-app-color-base-default-bg-opt2"),
        "surface": color("#ffffff", DECLARED + " --ds-app-color-base-default-bg-opt3; also the header fill"),
    },
    "text": {
        "heading": color("#0e1726", "computed color on h1, rgb(14, 23, 38), " + SRC),
        "body": color("#17253d", "computed color on body, rgb(23, 37, 61), " + SRC),
        "nav": color("#262626", "computed color on header.uhf-header, rgb(38, 38, 38), " + SRC),
        "link": color("#333275", "computed color on a.link, rgb(51, 50, 117), " + SRC),
        "on-action": color("#ffffff", "computed color on a.btn, " + SRC),
        "footer": color("#616161", "computed color on footer, rgb(97, 97, 97), " + SRC),
        "declared-accent": color("#0078d4", DECLARED + " --ds-app-color-base-default-fg-accent; not the painted button fill"),
        "declared-body": color("#3a4c56", DECLARED + " --ds-app-color-base-default-fg-body"),
    },
    "border": {
        "uhf": color("#000000", "computed 1px solid border on header Sign in, " + SRC),
        "subtle": color("#cbe6f4", DECLARED + " --ds-app-color-base-default-border-subtle"),
        "strong": color("#002948", DECLARED + " --ds-app-color-base-default-border-strong"),
        "secondary": color("#333275", "computed 2px border on a.btn.btn--secondary Try for free on pricing, " + SRC),
        "focus": color("#ffffff", "computed outline on focused a.btn: 3px dotted white, offset -6px, " + SRC),
    },
    "interactive": {
        "primary-bg": color("#0078d4", DECLARED + " --ds-app-color-interactive-primary-bg-default"),
        "primary-bg-hover": color("#006dc1", DECLARED + " --ds-app-color-interactive-primary-bg-hover"),
        "primary-bg-active": color("#004275", DECLARED + " --ds-app-color-interactive-primary-bg-active"),
        "primary-fg": color("#ffffff", DECLARED + " --ds-app-color-interactive-primary-fg-default"),
        "secondary-fg": color("#2a446f", DECLARED + " --ds-app-color-interactive-secondary-fg-default"),
        "secondary-bg": color("#e6f2fb", DECLARED + " --ds-app-color-interactive-secondary-bg-default"),
    },
    "component": {
        "button": {
            "background": color("{light.background.action}", "alias of the painted a.btn fill"),
            "text": color("{light.text.on-action}", "alias of the painted a.btn label"),
            "radius": dim("{core.radius.control}", "alias of the measured 8px control radius"),
            "padding": dim("8px", "computed padding-block on a.btn.btn--md, " + SRC),
            "height": dim("44px", "computed height of a.btn.btn--md Download now, " + SRC),
        },
        "header-button": {
            "background": color("{light.background.action}", "alias; header Try for free uses the same purple"),
            "text": color("{light.text.on-action}", "alias"),
            "radius": dim("{core.radius.uhf}", "alias of the 3px UHF radius"),
            "height": dim("31px", "computed height of header Try for free, " + SRC),
        },
        "field": {
            "text": color("#000000", "computed color on the Ask Microsoft input, " + SRC),
            "radius": dim("{core.radius.control}", "alias"),
            "height": dim("64px", "computed height of the Ask Microsoft input, " + SRC),
            "padding": dim("20px", "computed padding-block on that input, " + SRC),
        },
    },
}

doc = {
    "$description": "Microsoft Teams public marketing site, captured 2026-11-19 signed out. One painted light theme. Button purple is the computed a.btn fill, not the declared Fluent interactive blue.",
    "core": core,
    "light": light,
    "$themes": [
        {"name": "light", "selectedTokenSets": {"core": "source", "light": "enabled"}},
    ],
}

text = json.dumps(doc, indent=1) + "\n"
if __name__ == "__main__":
    (HERE / "tokens.json").write_text(text)
    print("wrote", HERE / "tokens.json", "bytes", len(text))
