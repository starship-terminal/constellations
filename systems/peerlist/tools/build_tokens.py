#!/usr/bin/env python3
"""Build tokens.json from raw/readings.json. Measured values only."""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
RAW = json.loads((HERE / "raw" / "readings.json").read_text())
SRC = "Computed on peerlist.io, 2026-11-18, T3 preview, html.light."


def color(value, source=SRC):
    return {"$type": "color", "$value": value, "$extensions": {"source": source}}


def dim(value, source=SRC):
    return {"$type": "dimension", "$value": value, "$extensions": {"source": source}}


def font(value, source=SRC):
    return {"$type": "fontFamily", "$value": value, "$extensions": {"source": source}}


def shadow(value, source=SRC):
    return {"$type": "shadow", "$value": value, "$extensions": {"source": source}}


def cubic(value, source=SRC):
    return {"$type": "cubicBezier", "$value": value, "$extensions": {"source": source}}


def duration(value, source=SRC):
    return {"$type": "duration", "$value": value, "$extensions": {"source": source}}


def text(family, size, line, weight, source=SRC):
    return {
        "$type": "typography",
        "$value": {
            "fontFamily": family,
            "fontSize": size,
            "fontWeight": weight,
            "lineHeight": line,
        },
        "$extensions": {"source": source},
    }


GRAY_LIGHT = {
    "00": "rgb(255 255 255)",
    "25": "rgb(248 249 251)",
    "50": "rgb(248 250 252)",
    "100": "rgb(241 245 249)",
    "200": "rgb(226 232 240)",
    "300": "rgb(203 213 225)",
    "400": "rgb(148 163 184)",
    "500": "rgb(100 116 139)",
    "600": "rgb(71 85 105)",
    "700": "rgb(51 65 85)",
    "800": "rgb(30 41 59)",
    "900": "rgb(15 23 42)",
    "1k": "rgb(13 13 13)",
}
GRAY_DARK = {
    "00": "rgb(23 23 23)",
    "25": "rgb(30 30 30)",
    "50": "rgb(38 38 38)",
    "100": "rgb(51 51 51)",
    "200": "rgb(64 64 64)",
    "300": "rgb(82 82 82)",
    "400": "rgb(115 115 115)",
    "500": "rgb(138 138 138)",
    "600": "rgb(163 163 163)",
    "700": "rgb(212 212 212)",
    "800": "rgb(229 229 229)",
    "900": "rgb(245 245 245)",
    "1k": "rgb(250 250 250)",
}

PALETTE = {
    "green": "rgb(0 170 69)",
    "green-00": "rgb(227 245 234)",
    "green-100": "rgb(111 207 151)",
    "green-200": "rgb(82 192 120)",
    "green-500": "rgb(30 135 75)",
    "green-800": "rgb(1 83 0)",
    "mark-stroke": "#219653",
    "red": "rgb(235 87 87)",
    "red-00": "rgb(255 234 234)",
    "red-200": "rgb(244 121 116)",
    "red-600": "rgb(194 13 13)",
    "orange": "rgb(249 115 22)",
    "blue": "rgb(47 128 237)",
    "blue-figma": "rgb(27 134 255)",
    "white": "rgb(255 255 255)",
    "ink": "rgb(0 0 0)",
}

SHEET = "Declared in the Peerlist stylesheet, 2026-11-18. Not observed painted, because html stayed class light."


def gray_group(table, source):
    return {k: color(v, source) for k, v in table.items()}


def semantic(theme):
    page = "{color.gray.00}" if theme == "light" else "{color.gray.00}"
    return {
        "page": color(page, SRC if theme == "light" else SHEET),
        "surface": color("{color.gray.00}", SRC if theme == "light" else SHEET),
        "surface-muted": color("{color.gray.25}", SRC if theme == "light" else SHEET),
        "text": color("{color.ink}" if theme == "light" else "{color.gray.1k}", SRC if theme == "light" else SHEET),
        "text-strong": color("{color.gray.1k}", SRC if theme == "light" else SHEET),
        "muted": color("{color.gray.700}" if theme == "light" else "{color.gray.500}", SRC if theme == "light" else SHEET),
        "placeholder": color("{color.gray.300}", SRC if theme == "light" else SHEET),
        "accent": color("{color.green}", SRC),
        "accent-border": color("{color.green-500}", SRC),
        "on-accent": color("{color.white}", SRC),
        "action": color("{color.gray.900}", SRC if theme == "light" else SHEET),
        "on-action": color("{color.white}" if theme == "light" else "{color.gray.00}", SRC if theme == "light" else SHEET),
        "border": color("{color.gray.200}" if theme == "light" else "{color.gray.100}", SRC if theme == "light" else SHEET),
        "field-border": color("{color.gray.300}", SRC),
        "danger": color("{color.red}", SRC),
        "focus": shadow(
            "0px 0px 0px 4px #e1e4e880" if theme == "light" else "0px 0px 0px 4px rgb(38 38 38)",
            SRC if theme == "light" else SHEET,
        ),
    }


core = {
    "color": {
        "gray": gray_group(GRAY_LIGHT, SRC + " :root custom properties, resolved on the light root."),
        "green": color(PALETTE["green"], SRC + " .bg-green rule."),
        "green-00": color(PALETTE["green-00"]),
        "green-100": color(PALETTE["green-100"]),
        "green-200": color(PALETTE["green-200"]),
        "green-500": color(PALETTE["green-500"], SRC + " Create Profile border."),
        "green-800": color(PALETTE["green-800"]),
        "mark-stroke": color(PALETTE["mark-stroke"], "Inline logo SVG fill #219653."),
        "red": color(PALETTE["red"], SRC + " .bg-red / .text-red rule."),
        "red-00": color(PALETTE["red-00"]),
        "red-200": color(PALETTE["red-200"]),
        "red-600": color(PALETTE["red-600"]),
        "orange": color(PALETTE["orange"]),
        "blue": color(PALETTE["blue"]),
        "blue-figma": color(PALETTE["blue-figma"]),
        "white": color(PALETTE["white"]),
        "ink": color(PALETTE["ink"], SRC + " body color."),
    },
    "font": {
        "family": {
            "ui": font("Geist, sans-serif", SRC + " body font-family."),
            "display": font("instrument, sans-serif", SRC + " h1 font-family."),
            "mono": font("Geist Mono, ui-monospace, monospace", "Declared --font-geist-mono. Not measured on a visible control."),
        }
    },
    "typography": {
        "body": text("{font.family.ui}", "16px", "24px", "400"),
        "display": text("{font.family.display}", "48px", "57.6px", "400", SRC + " Home h1 at 1440."),
        "section": text("{font.family.display}", "40px", "48px", "400", SRC + " Home h2 and auth h2."),
        "title": text("{font.family.ui}", "20px", "28px", "600", SRC + " Home h3."),
        "subhead": text("{font.family.ui}", "18px", "28px", "400", SRC + " Home subhead, text-gray-700."),
        "ui": text("{font.family.ui}", "14px", "20px", "500", SRC + " Nav link."),
        "label": text("{font.family.ui}", "14px", "20px", "600", SRC + " Auth label and buttons."),
        "field": text("{font.family.ui}", "14px", "20px", "400", SRC + " Login email input."),
        "username": text("{font.family.ui}", "20px", "28px", "400", SRC + " Home username input."),
        "fine": text("{font.family.ui}", "12px", "16px", "600", SRC + " Forgot password link."),
        "app-title": text("{font.family.ui}", "16px", "22px", "600", SRC + " Jobs, Scroll, Launchpad h1."),
    },
    "radius": {
        "sm": dim("2px", "Tailwind .rounded-sm, declared."),
        "md": dim("6px", "Tailwind .rounded-md, declared."),
        "control": dim("8px", SRC + " Login input border-radius."),
        "button": dim("12px", SRC + " Log in and Create Profile."),
        "card": dim("16px", SRC + " Username field, auth card, project card."),
        "nav": dim("24px", SRC + " Nav link."),
        "pill": dim("9999px", SRC + " Ads pill and avatars."),
        "check": dim("4px", SRC + " Search checkbox."),
    },
    "spacing": {
        "1": dim("4px"),
        "2": dim("8px", SRC + " Nav link horizontal padding and field padding."),
        "3": dim("12px", SRC + " Username field padding."),
        "4": dim("16px", SRC + " Button horizontal padding and job-row vertical padding."),
        "5": dim("20px", SRC + " Username field left padding."),
        "6": dim("24px", SRC + " Auth card padding and job-row horizontal padding."),
        "header": dim("56px", SRC + " Sticky header height."),
        "control": dim("32px", SRC + " Small button and text field height."),
        "control-lg": dim("40px", SRC + " Login submit height."),
        "shell": dim("568px", SRC + " Marketing column max-width."),
        "auth": dim("380px", SRC + " Auth card max-width."),
        "field": dim("446px", SRC + " Username field max-width."),
        "feed": dim("640px", SRC + " Job row and scroll post width at 1440."),
    },
    "shadow": {
        "5": shadow(RAW["rootTokens"]["light"]["--shadow-5"], SRC + " :root --shadow-5, on Log in."),
        "10": shadow(RAW["rootTokens"]["light"]["--shadow-10"], SRC + " :root --shadow-10, on Create Profile."),
        "15": shadow(RAW["rootTokens"]["light"]["--shadow-15"], SRC + " :root --shadow-15."),
    },
    "motion": {
        "duration": {
            "button": duration("75ms", SRC + " Log in transition-duration."),
            "nav": duration("200ms", SRC + " Nav link transition-duration."),
            "color": duration("300ms", SRC + " Hero word buttons and tooltip delay."),
        },
        "easing": {
            "standard": cubic([0.4, 0, 0.2, 1], SRC + " Nav and hero word timing function."),
            "in": cubic([0.4, 0, 1, 1], SRC + " Button timing function."),
        },
    },
}

tokens = {
    "$schema": "https://design-tokens.github.io/community-group/format/",
    "core": core,
    "light": semantic("light"),
    "dark": semantic("dark"),
    "$themes": [
        {"id": "light", "name": "Light", "selectedTokenSets": {"core": "source", "light": "enabled"}},
        {"id": "dark", "name": "Dark", "selectedTokenSets": {"core": "source", "dark": "enabled"}},
    ],
    "$extensions": {
        "source": SRC,
        "dark": "The .dark custom properties were read from the stylesheet. The live pages stayed on html.light, so dark colours are declared, not painted.",
        "screenshots": RAW["screenshot"],
    },
}

out = HERE / "tokens.json"
out.write_text(json.dumps(tokens, indent=2) + "\n")
print(f"wrote {out}")
