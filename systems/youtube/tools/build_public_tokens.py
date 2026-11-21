#!/usr/bin/env python3
"""Build tokens.public.json from the 2026-11-21 public web readings.

Values are computed styles from www.youtube.com and accounts.google.com,
signed out. The native iOS tokens.json is left in place. This file is the
web pass. Every token carries $extensions.source.
"""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent.parent
OUT = HERE / "tokens.public.json"

SRC = "raw/public-readings.json and raw/public-measured.json, signed-out Chromium, 2026-11-21"


def tok(value, typ, desc, evidence="Measured"):
    return {
        "$value": value,
        "$type": typ,
        "$description": desc,
        "$extensions": {"source": {"evidence": evidence, "capture": SRC}},
    }


def color(value, desc, evidence="Measured"):
    return tok(value, "color", desc, evidence)


core = {
    "font": {
        "family": {
            "sans": tok("Roboto, Arial, sans-serif", "fontFamily", "Computed font-family on the search field, Sign in, and the watch title."),
            "player": tok('"YouTube Noto", Roboto, Arial, Helvetica, sans-serif', "fontFamily", "Computed font-family on #movie_player."),
            "accounts": tok('"Google Sans", roboto, arial, sans-serif', "fontFamily", "Computed font-family on the accounts.google.com sign-in body."),
        }
    },
    "typography": {
        "empty-title": tok({"fontFamily": "{core.font.family.sans}", "fontSize": "18px", "fontWeight": "900", "lineHeight": "26px"}, "typography", "ytd-feed-nudge-renderer h2, dark home."),
        "watch-title": tok({"fontFamily": "{core.font.family.sans}", "fontSize": "20px", "fontWeight": "700", "lineHeight": "28px"}, "typography", "Watch page h1."),
        "result-title": tok({"fontFamily": "{core.font.family.sans}", "fontSize": "18px", "fontWeight": "400", "lineHeight": "26px"}, "typography", "Search result a#video-title."),
        "search": tok({"fontFamily": "{core.font.family.sans}", "fontSize": "16px", "fontWeight": "400", "lineHeight": "22px"}, "typography", "input#search."),
        "button": tok({"fontFamily": "{core.font.family.sans}", "fontSize": "14px", "fontWeight": "500", "lineHeight": "40px"}, "typography", "Sign in and Subscribe."),
        "meta": tok({"fontFamily": "{core.font.family.sans}", "fontSize": "12px", "fontWeight": "400"}, "typography", "Search result metadata line."),
        "account-heading": tok({"fontFamily": "{core.font.family.accounts}", "fontSize": "36px", "fontWeight": "400"}, "typography", "accounts.google.com h1, light sign-in."),
    },
    "radius": {
        "pill": tok("20px", "dimension", "Sign in and Subscribe border-radius."),
        "guide": tok("10px", "dimension", "Selected guide row border-radius."),
        "card": tok("12px", "dimension", "Empty-state card and settings menu border-radius."),
        "field": tok("4px", "dimension", "accounts.google.com identifier field border-radius."),
    },
    "size": {
        "masthead": tok("56px", "dimension", "ytd-masthead height at 1440."),
        "mini-guide": tok("72px", "dimension", "ytd-mini-guide-renderer width."),
        "guide": tok("240px", "dimension", "Open guide drawer width."),
        "guide-row": tok("40px", "dimension", "Guide entry height."),
        "control": tok("40px", "dimension", "Sign in and Subscribe height."),
        "chip": tok("32px", "dimension", "Search chip height."),
        "menu": tok("300px", "dimension", "Settings menu width."),
    },
    "space": {
        "page": tok("16px", "dimension", "Watch player inset from the viewport edge."),
        "control-x": tok("16px", "dimension", "Subscribe horizontal padding."),
    },
    "color": {
        "brand-red": color("#FF0033", "Computed fill of the wordmark path, #logo-icon svg path."),
    },
}

def theme(page, text, muted, accent, surface, border, search_bg, search_text, subscribe_bg, subscribe_text, menu, chip_selected, scrim_note):
    return {
        "color": {
            "page": color(page, "Computed background of ytd-app / html."),
            "text": color(text, "Computed color of the empty-state h2 and the watch title."),
            "muted": color(muted, "Computed color of the search result metadata line."),
            "accent": color(accent, "Computed color of the Sign in link."),
            "surface": color(surface, "Computed background of the empty-state #content-wrapper."),
            "border": color(border, "Computed border-top-color of the Sign in outline."),
            "search-bg": color(search_bg, "Custom property --ytd-searchbox-background."),
            "search-text": color(search_text, "Custom property --ytd-searchbox-text-color."),
            "subscribe-bg": color(subscribe_bg, "Computed background of the Subscribe button in this theme. Dark reading reused for light where the light button was not separately measured.", "Measured" if subscribe_bg == "#F1F1F1" else "Derived"),
            "subscribe-text": color(subscribe_text, "Computed color of the Subscribe label."),
            "menu": color(menu, "Computed background of ytd-multi-page-menu-renderer in dark. Light menu was not separately measured.", "Measured" if menu == "#282828" else "Derived"),
            "chip-selected": color(chip_selected, "Computed background of the selected guide row."),
            "brand-red": color("{core.color.brand-red}", "Alias of the wordmark fill."),
        }
    }


dark = theme(
    page="#0F0F0F",
    text="#F1F1F1",
    muted="#AAAAAA",
    accent="#3EA6FF",
    surface="#212121",
    border="rgba(255, 255, 255, 0.2)",
    search_bg="hsl(0, 0%, 7%)",
    search_text="hsla(0, 100%, 100%, 0.88)",
    subscribe_bg="#F1F1F1",
    subscribe_text="#0F0F0F",
    menu="#282828",
    chip_selected="rgba(255, 255, 255, 0.1)",
    scrim_note="",
)
light = theme(
    page="#FFFFFF",
    text="#0F0F0F",
    muted="#606060",
    accent="#065FD4",
    surface="#FFFFFF",
    border="rgba(0, 0, 0, 0.1)",
    search_bg="hsl(0, 0%, 100%)",
    search_text="hsl(0, 0%, 6.7%)",
    subscribe_bg="#0F0F0F",
    subscribe_text="#FFFFFF",
    menu="#FFFFFF",
    chip_selected="rgba(0, 0, 0, 0.05)",
    scrim_note="",
)
# Light text on a white page is the product's near-black, measured as the searchbox text token.
light["color"]["text"] = color("#111111", "Derived from --ytd-searchbox-text-color hsl(0, 0%, 6.7%) on the light home. The empty-state heading paints the same near-black.", "Derived")
light["color"]["muted"] = color("#606060", "Not read from a light metadata element in this pass. Left as a placeholder grey so the light set has the same keys as dark. Do not treat it as a measured token.", "Not captured")
light["color"]["accent"] = color("#065FD4", "The dark stylesheet's paired value for --t2d807bb79e75606d, which resolves to #3ea6ff in dark and #065fd4 in light.", "Derived")
light["color"]["subscribe-bg"] = color("#0F0F0F", "Not measured on a light Subscribe button in this pass. The dark button inverts page and text, so the light button is recorded as the inverse of the light page.", "Derived")
light["color"]["subscribe-text"] = color("#FFFFFF", "Inverse of the derived light Subscribe fill.", "Derived")
light["color"]["menu"] = color("#FFFFFF", "Light settings menu was not opened. The light page fill is used.", "Not captured")
light["color"]["border"] = color("rgba(0, 0, 0, 0.1)", "Paired value of the dark Sign in border rgba(255, 255, 255, 0.2) in the same custom property.", "Derived")

doc = {
    "core": core,
    "dark": dark,
    "light": light,
    "$themes": [
        {"id": "dark", "name": "Dark", "selectedTokenSets": {"core": "source", "dark": "enabled"}},
        {"id": "light", "name": "Light", "selectedTokenSets": {"core": "source", "light": "enabled"}},
    ],
    "$metadata": {"tokenSetOrder": ["core", "dark", "light"]},
}
OUT.write_text(json.dumps(doc, indent=2) + "\n")
print("wrote", OUT)
