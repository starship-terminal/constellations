#!/usr/bin/env python3
"""Build tokens.json from raw/readings.json. Measured values only."""
import json
import re
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


def hex_of(value):
    """'255 255 255', 'rgb(0 170 69)', 'rgb(0, 0, 0)' or '#219653' as lower-case hex."""
    if value.startswith("#"):
        return value.lower()
    nums = re.findall(r"[\d.]+", value)
    if len(nums) != 3:
        raise SystemExit(f"not an opaque rgb triplet: {value!r}")
    return "#" + "".join(f"{round(float(n)):02x}" for n in nums)


def ramp(theme):
    """The --gray-* steps the stylesheet declares for one theme, from raw/readings.json."""
    table = RAW["rootTokens"][theme]
    return {k[len("--gray-"):]: hex_of(v) for k, v in table.items() if k.startswith("--gray-")}


GRAY_LIGHT = ramp("light")
GRAY_DARK = ramp("darkDeclared")

# Token name -> the palette rule's name in raw/readings.json paletteRules.
PALETTE_KEYS = {
    "green": "green", "green-00": "green-00", "green-100": "green-100", "green-200": "green-200",
    "green-500": "green-500", "green-800": "green-800", "mark-stroke": "mark-stroke",
    "red": "red", "red-00": "red-00", "red-200": "red-200", "red-600": "red-600",
    "orange": "orange", "blue": "blue-400", "blue-figma": "blue-figmaBlue",
}
PALETTE = {name: hex_of(RAW["paletteRules"][key]) for name, key in PALETTE_KEYS.items()}
PALETTE["white"] = hex_of(RAW["computed"]["buttonPrimary"]["color"])
PALETTE["ink"] = hex_of(RAW["computed"]["body"]["color"])

PALETTE_SRC = "Declared in the Peerlist stylesheet's palette rules (raw/readings.json paletteRules), 2026-11-18."
HAND = "Reconstruction: entered by hand at capture time; raw/readings.json holds no reading for it."
HAND_PART = " Reconstruction for %s: entered by hand at capture time; raw/readings.json holds no reading for it."
SHEET = "Declared in the Peerlist stylesheet, 2026-11-18. Not observed painted, because html stayed class light."


def gray_group(table, source):
    return {k: color(v, source) for k, v in table.items()}


def semantic(theme):
    """Light aliases the painted light ramp; dark aliases the ramp declared on .dark."""
    light = theme == "light"
    gray = "color.gray" if light else "color.gray-dark"
    src = SRC if light else SHEET
    focus = RAW["rootTokens"]["light" if light else "darkDeclared"]["--shadow-focus"]
    focus = re.sub(r"rgb\([^)]*\)", lambda m: hex_of(m.group(0)), focus)
    return {
        "page": color("{%s.00}" % gray, src),
        "surface": color("{%s.00}" % gray, src),
        "surface-muted": color("{%s.25}" % gray, src),
        "text": color("{color.ink}" if light else "{%s.1k}" % gray, src),
        "text-strong": color("{%s.1k}" % gray, src),
        "muted": color("{%s.700}" % gray if light else "{%s.500}" % gray, src),
        "placeholder": color("{%s.300}" % gray, src),
        "accent": color("{color.green}", SRC),
        "accent-border": color("{color.green-500}", SRC),
        "on-accent": color("{color.white}", SRC),
        "action": color("{%s.900}" % gray, src),
        "on-action": color("{color.white}" if light else "{%s.00}" % gray, src),
        "border": color("{%s.200}" % gray if light else "{%s.100}" % gray, src),
        "field-border": color("{%s.300}" % gray, src),
        "danger": color("{color.red}", SRC),
        "focus": shadow(focus, src),
    }


core = {
    "color": {
        "gray": gray_group(GRAY_LIGHT, SRC + " :root custom properties, resolved on the light root."),
        "gray-dark": gray_group(GRAY_DARK, SHEET + " The .dark rule's --gray-* custom properties, which the dark set aliases."),
        "green": color(PALETTE["green"], SRC + " .bg-green rule."),
        "green-00": color(PALETTE["green-00"], PALETTE_SRC),
        "green-100": color(PALETTE["green-100"], PALETTE_SRC),
        "green-200": color(PALETTE["green-200"], PALETTE_SRC),
        "green-500": color(PALETTE["green-500"], SRC + " Create Profile border."),
        "green-800": color(PALETTE["green-800"], PALETTE_SRC),
        "mark-stroke": color(PALETTE["mark-stroke"], "Inline logo SVG fill #219653."),
        "red": color(PALETTE["red"], SRC + " .bg-red / .text-red rule."),
        "red-00": color(PALETTE["red-00"], PALETTE_SRC),
        "red-200": color(PALETTE["red-200"], PALETTE_SRC),
        "red-600": color(PALETTE["red-600"], PALETTE_SRC),
        "orange": color(PALETTE["orange"], PALETTE_SRC),
        "blue": color(PALETTE["blue"], PALETTE_SRC + " Rule blue-400."),
        "blue-figma": color(PALETTE["blue-figma"], PALETTE_SRC + " Rule blue-figmaBlue."),
        "white": color(PALETTE["white"], SRC + " Create Profile text colour."),
        "ink": color(PALETTE["ink"], SRC + " body color."),
    },
    "font": {
        "family": {
            "ui": font("Geist, sans-serif", SRC + " body font-family."),
            "display": font("instrument, sans-serif", SRC + " h1 font-family, read as `instrument, instrument Fallback`; the generated Fallback face is written as sans-serif."),
            "mono": font("Geist Mono, ui-monospace, monospace", "Declared --font-geist-mono, read as `Geist Mono, Geist Mono Fallback`; the generated Fallback face is written as ui-monospace, monospace. Not measured on a visible control."),
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
        "field": text("{font.family.ui}", "14px", "20px", "400", SRC + " Login email input, size and line height." + HAND_PART % "fontWeight 400"),
        "username": text("{font.family.ui}", "20px", "28px", "400", SRC + " Home username input, size and line height." + HAND_PART % "fontWeight 400"),
        "fine": text("{font.family.ui}", "12px", "16px", "600", SRC + " Forgot password link, size and weight." + HAND_PART % "lineHeight 16px"),
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
        "1": dim("4px", HAND),
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

def build():
    return {
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


def main():
    out = HERE / "tokens.json"
    out.write_text(json.dumps(build(), indent=2) + "\n")
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
