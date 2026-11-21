#!/usr/bin/env python3
"""Build tokens.json from Stocktwits readings. Edit the readings, never tokens.json.

Sources, read from stocktwits.com on 2026-11-21, signed out, light theme, 1440x900:
  raw/components-computed.json  computed styles and the custom properties
                                resolved on :root (html.light, data-theme=light).
  raw/extra-readings.json       sign-in field and sentiment chips, measured in a
                                fresh context after Cloudflare blocked a second
                                navigation in the first session.
Dark theme: the product paints light even when the browser prefers dark.
No dark set is written.
"""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
COMP = json.loads((RAW / "components-computed.json").read_text())
VARS = COMP["_meta"]["foundations"]["resolved"]


def src_var(name):
    return f"css-var {name} resolved on :root (raw/components-computed.json, html.light, 1440x900, 2026-11-21)"


def src_comp(key, state, prop):
    return f"computed {prop} of {key} {state} (raw/components-computed.json)"


def color(value, source, description):
    return {"$value": value, "$type": "color", "$extensions": {"source": source}, "$description": description}


def dim(value, source, description):
    return {"$value": value, "$type": "dimension", "$extensions": {"source": source}, "$description": description}


def font(value, source, description):
    return {"$value": value, "$type": "fontFamily", "$extensions": {"source": source}, "$description": description}


def weight(value, source, description):
    return {"$value": value, "$type": "fontWeight", "$extensions": {"source": source}, "$description": description}


def number(value, source, description):
    return {"$value": value, "$type": "number", "$extensions": {"source": source}, "$description": description}


def alias(path, source, description, ty="color"):
    return {"$value": "{" + path + "}", "$type": ty, "$extensions": {"source": source}, "$description": description}


def v(name):
    if name not in VARS:
        raise KeyError(name)
    return VARS[name]


body_font = COMP["components"]["button-primary"]["default"]["style"]["fontFamily"]

tokens = {
    "core": {
        "color": {
            "page": color(v("--primary-background"), src_var("--primary-background"), "Page background."),
            "surface": color(v("--secondary-background"), src_var("--secondary-background"), "Raised surface, also the field fill."),
            "surface-sidebar": color(v("--sidebar-background"), src_var("--sidebar-background"), "Left rail wash."),
            "text": color(v("--st-primary-text"), src_var("--st-primary-text"), "Primary text."),
            "text-secondary": color(v("--st-secondary-text"), src_var("--st-secondary-text"), "Secondary text."),
            "text-tertiary": color(v("--st-tertiary-text"), src_var("--st-tertiary-text"), "Muted labels and inactive tabs."),
            "text-on-accent": color(v("--primary-button-text"), src_var("--primary-button-text"), "Text on a filled black or blue button."),
            "border": color(v("--primary-border"), src_var("--primary-border"), "Hairline and control border."),
            "link": color(v("--blue-5"), src_var("--blue-5"), "Inline link and announcement blue."),
            "accent": color("#000000", src_comp("button-primary", "default", "backgroundColor"), "Filled pill. Sign Up paints black, not the blue token."),
            "accent-hover": color("#2c2c2e", src_comp("button-primary", "hover", "backgroundColor"), "Filled pill on hover."),
            "disabled": color("#d1d1d6", "computed backgroundColor of the disabled Log In button on /signin (raw/extra-readings.json)", "Disabled submit."),
            "up": color(v("--sentiment-green"), src_var("--sentiment-green"), "Gain and bullish."),
            "down": color(v("--sentiment-red"), src_var("--sentiment-red"), "Loss and bearish."),
            "up-wash": color(v("--tag-green"), src_var("--tag-green"), "Bullish chip fill."),
            "down-wash": color(v("--tag-red"), src_var("--tag-red"), "Bearish chip fill."),
            "field": color(v("--st-input-background"), src_var("--st-input-background"), "Text field fill."),
            "live": color("#6d28d9", "Not captured as a custom property. The Earnings badge paints a purple chip in screenshots/home-light-default.png. Value unread.", "Unread. Kept out of the token set."),
        },
        "font": {
            "family": {
                "ui": font(body_font, src_comp("button-primary", "default", "fontFamily"), "Source Sans 3, with the site's fallback face."),
            },
            "size": {
                "body": dim("16px", "computed fontSize of body (raw/components-computed.json _meta.foundations.body)", "Body size."),
                "button": dim("15px", src_comp("button-primary", "default", "fontSize"), "Filled button label."),
                "nav": dim("13px", src_comp("nav-link", "default", "fontSize"), "Top nav label."),
                "tab": dim("16px", src_comp("tab", "default", "fontSize"), "Feed tab."),
                "link": dim("14px", src_comp("link", "default", "fontSize"), "Inline link."),
                "field": dim("16px", "computed fontSize of input[name=login] on /signin (raw/extra-readings.json)", "Text field."),
                "heading": dim("20px", "computed fontSize of h1 Log In on /signin (raw/extra-readings.json)", "Auth heading. Display sizes on marketing pages were not measured."),
            },
            "weight": {
                "regular": weight(400, src_comp("link", "default", "fontWeight"), "Body and links."),
                "semibold": weight(600, src_comp("button-primary", "default", "fontWeight"), "Buttons."),
                "bold": weight(700, "computed fontWeight of h1 Log In on /signin (raw/extra-readings.json)", "Auth heading."),
            },
            "lineHeight": {
                "body": number(1.5, "Derived: body line-height 24px / font-size 16px (raw/components-computed.json)", "Body line height."),
            },
        },
        "radius": {
            "pill": dim("9999px", src_comp("button-primary", "default", "borderRadius"), "Buttons, chips, search."),
            "field": dim("8px", "computed borderRadius of input[name=login] on /signin (raw/extra-readings.json)", "Text field."),
            "card": dim("16px", "Not captured as a computed radius on a card crop. Trending cards look rounded in screenshots/home-light-default.png. Value unread.", "Unread."),
        },
        "size": {
            "button-md": dim("40px", "Observed height of Sign Up and the sign-in Log In button. Recorded as 40px from the sign-in reading (raw/extra-readings.json).", "Medium control."),
            "button-xs": dim("24px", "css-var --size on .STButton_xs (stylesheets, 2026-11-21 probe)", "Icon button."),
            "field": dim("40px", "computed height of input[name=login] (raw/extra-readings.json)", "Text field."),
        },
        "space": {
            "field-x": dim("12px", "computed paddingLeft of input[name=login] (raw/extra-readings.json)", "Field horizontal padding."),
            "field-y": dim("8px", "computed paddingTop of input[name=login] (raw/extra-readings.json)", "Field vertical padding."),
            "button-x": dim("20px", "computed paddingLeft of the sign-in Log In button (raw/extra-readings.json)", "Button horizontal padding."),
        },
    },
    "light": {
        "page": alias("core.color.page", "alias of core.color.page", "Page."),
        "surface": alias("core.color.surface", "alias of core.color.surface", "Surface."),
        "text": alias("core.color.text", "alias of core.color.text", "Primary text."),
        "muted": alias("core.color.text-tertiary", "alias of core.color.text-tertiary", "Muted text."),
        "accent": alias("core.color.accent", "alias of core.color.accent", "Filled action."),
        "border": alias("core.color.border", "alias of core.color.border", "Border."),
        "link": alias("core.color.link", "alias of core.color.link", "Link."),
        "up": alias("core.color.up", "alias of core.color.up", "Gain."),
        "down": alias("core.color.down", "alias of core.color.down", "Loss."),
        "component": {
            "button-primary-background": alias("core.color.accent", "alias", "Sign Up fill.", "color"),
            "button-primary-text": alias("core.color.text-on-accent", "alias", "Sign Up label.", "color"),
            "button-primary-radius": alias("core.radius.pill", "alias", "Pill radius.", "dimension"),
            "button-disabled-background": alias("core.color.disabled", "alias", "Disabled Log In.", "color"),
            "field-background": alias("core.color.field", "alias", "Field fill.", "color"),
            "field-radius": alias("core.radius.field", "alias", "Field radius.", "dimension"),
            "bullish-background": alias("core.color.up-wash", "alias", "Bullish chip.", "color"),
            "bearish-background": alias("core.color.down-wash", "alias", "Bearish chip.", "color"),
        },
    },
    "$themes": [
        {"id": "light", "name": "light", "selectedTokenSets": {"core": "source", "light": "enabled"}},
    ],
}

# Drop the unread live colour so no token lacks a measured source.
del tokens["core"]["color"]["live"]
del tokens["core"]["radius"]["card"]

out = HERE / "tokens.json"
out.write_text(json.dumps(tokens, indent=2) + "\n")
print("wrote", out)
