#!/usr/bin/env python3
"""Build tokens.json from OneSoil public-page readings.

Sources, read on 2026-11-21 from onesoil.ai/en and its public marketing pages,
signed out, in headless Chromium at 1440x900:

  raw/components-computed.json   computed styles of real controls
  raw/foundations.json           the colour, type and radius notes this builder
                                 also writes, so a rebuild can be checked

OneSoil's marketing site does not publish a product token layer. The custom
properties on the page are Tailwind internals. Every colour here was read from
a computed style (Measured) or from a flat pixel on a raw screenshot before
quantising (Sampled). A value that could not be read is not invented.

There is no dark theme. prefers-color-scheme: dark left the page cream and
ink. The token file has core and light only.

Deterministic: same inputs, same bytes.
"""
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
COMP = json.loads((RAW / "components-computed.json").read_text())

SRC = "Measured computed style, onesoil.ai public marketing, 2026-11-21, 1440x900, signed out"
SAMPLED = "Sampled flat pixel on the raw screenshot before quantising, 2026-11-21"


def color(value, source):
    return {"$type": "color", "$value": value, "$extensions": {"source": source}}


def dim(value, source):
    if not (str(value).startswith("{") or re.fullmatch(r"-?\d+(\.\d+)?(px|rem)", value)):
        raise ValueError(f"not a dimension: {value}")
    return {"$type": "dimension", "$value": value, "$extensions": {"source": source}}


def num(value, source):
    return {"$type": "number", "$value": value, "$extensions": {"source": source}}


def font_weight(value, source):
    return {"$type": "fontWeight", "$value": int(value), "$extensions": {"source": source}}


def duration(value, source):
    return {"$type": "duration", "$value": value, "$extensions": {"source": source}}


def bezier(value, source):
    return {"$type": "cubicBezier", "$value": value, "$extensions": {"source": source}}


def family(value, source):
    return {"$type": "fontFamily", "$value": value, "$extensions": {"source": source}}


def typography(font_family, font_size, font_weight, line_height, letter_spacing, source):
    return {
        "$type": "typography",
        "$value": {
            "fontFamily": font_family,
            "fontSize": font_size,
            "fontWeight": font_weight,
            "lineHeight": line_height,
            "letterSpacing": letter_spacing,
        },
        "$extensions": {"source": source},
    }


def shadow(layers, source):
    return {"$type": "shadow", "$value": layers, "$extensions": {"source": source}}


GEOL = "{font.family.geologica}"

core = {
    "color": {
        "page": color("#f6f4ef", SRC + "; document.body backgroundColor rgb(246, 244, 239)"),
        "ink": color("#151515", SRC + "; h1 and Schedule a demo fill rgb(21, 21, 21)"),
        "body": color("#171717", SRC + "; document.body color rgb(23, 23, 23)"),
        "muted": color("#6d6351", SRC + "; footer-adjacent link and placeholder rgb(109, 99, 81)"),
        "white": color("#ffffff", SRC + "; button label color"),
        "accent": color("#27ae60", SRC + "; Try Free backgroundColor rgb(39, 174, 96)"),
        "accent-text": color("#1e9852", SRC + "; green words inside the home h1 rgb(30, 152, 82)"),
        "accent-hover": color("#3bb56f", SAMPLED + "; Try Free hovered, dominant pixel (59, 181, 111) in /tmp/onesoil-free-hover.png. Computed style stayed oklab(0.662876 -0.141961 0.0743057 / 0.9)"),
        "ink-hover": color("#2b2b2b", SAMPLED + "; Schedule a demo hovered, dominant pixel (43, 43, 43) in home-light-cta-hover.png. Computed style stayed oklab(0.195735 0 0 / 0.9)"),
        "focus": color("#005fcc", SRC + "; Schedule a demo focus-visible outlineColor rgb(0, 95, 204)"),
        "field": color("#f6f4ef", SRC + "; contact name field backgroundColor"),
        "field-focus": color("#ffffff", SRC + "; contact name field focused backgroundColor"),
        "chip-selected": color("#ede8e2", SRC + "; Agronomist radio selected backgroundColor rgb(237, 232, 226)"),
        "hairline": color("rgba(109, 99, 81, 0.2)", SRC + "; role chip borderTopColor and focused field borderTopColor"),
        "nav-selected": color("rgba(21, 21, 21, 0.05)", "Derived from the computed oklab(0.204606 0 0 / 0.05) on the open Products trigger. The oklab form was not converted by the browser to sRGB, so the alpha is the measured one and the ink is the measured #151515"),
        "menu-card": color("rgba(21, 21, 21, 0.05)", "Derived the same way from menu-card default background oklab(0.195735 0 0 / 0.05)"),
        "menu-card-hover": color("rgba(21, 21, 21, 0.1)", "Derived from menu-card hover background oklab(0.195735 0 0 / 0.1)"),
    },
    "font": {
        "family": {
            "geologica": family(
                "geologica, \"geologica Fallback\", system-ui, sans-serif",
                SRC + "; computed fontFamily on body, h1 and header buttons",
            ),
            "help": family(
                "\"Noto Sans\", \"Noto Sans Fallback\"",
                SRC + "; help.onesoil.ai search field computed fontFamily. A different product surface.",
            ),
        },
        "weight": {
            "regular": font_weight(400, SRC + "; body and buttons"),
            "light": font_weight(300, SRC + "; contact fields and the platform link"),
        },
        "size": {
            "body": dim("16px", SRC + "; body fontSize"),
            "field": dim("18px", SRC + "; contact field fontSize"),
            "display": dim("72px", SRC + "; home h1 fontSize"),
        },
        "line-height": {
            "body": dim("24px", SRC + "; body lineHeight"),
            "display": dim("75.6px", SRC + "; home h1 lineHeight"),
            "field": dim("25.2px", SRC + "; contact field lineHeight"),
        },
        "letter-spacing": {
            "display": dim("-2.88px", SRC + "; home h1 letterSpacing"),
        },
    },
    "typography": {
        "display": typography(GEOL, "72px", 400, "75.6px", "-2.88px", SRC + "; home h1"),
        "body": typography(GEOL, "16px", 400, "24px", "0px", SRC + "; body. letterSpacing computed as normal, recorded as 0px"),
        "field": typography(GEOL, "18px", 300, "25.2px", "0px", SRC + "; contact name field"),
        "button": typography(GEOL, "16px", 400, "24px", "0px", SRC + "; Schedule a demo"),
    },
    "radius": {
        "pill": dim("9999px", "Derived. Computed border radius on Schedule a demo and Try Free was 3.35544e+07px, which is Tailwind's rounded-full. Stored as 9999px because a dimension that large is the pill sentinel, not a measured corner."),
        "header": dim("40px", SRC + "; header island borderRadius, read from the painted bar"),
        "card": dim("16px", SRC + "; products menu card borderTopLeftRadius"),
        "audience": dim("24px", SRC + "; home audience card borderTopLeftRadius"),
        "field": dim("13px", SRC + "; contact field borderTopLeftRadius"),
    },
    "space": {
        "2": dim("8px", SRC + "; role chip paddingTop"),
        "3": dim("12px", SRC + "; button paddingTop and field padding"),
        "4": dim("16px", SRC + "; button paddingRight"),
        "6": dim("24px", SRC + "; menu card padding and header inline padding"),
    },
    "size": {
        "button": dim("48px", SRC + "; Schedule a demo and Try Free height"),
        "submit": dim("40px", SRC + "; contact Submit height"),
        "chip": dim("34px", SRC + "; role chip height"),
        "field": dim("53.1875px", SRC + "; contact name field height"),
        "menu-card": dim("120px", SRC + "; products menu card height"),
    },
    "border": {
        "field": dim("2px", SRC + "; contact field borderTopWidth"),
        "chip": dim("1px", SRC + "; role chip borderTopWidth"),
        "focus": dim("2px", SRC + "; focus-visible outlineWidth"),
    },
    "duration": {
        "fast": duration("150ms", "Derived from computed transitionDuration 0.15s on buttons and fields"),
    },
    "easing": {
        "standard": bezier([0.4, 0, 0.2, 1], SRC + "; button transitionTimingFunction cubic-bezier(0.4, 0, 0.2, 1)"),
    },
    "layout": {
        "desktop": dim("1440px", "Measured window.innerWidth on desktop captures"),
        "phone": dim("390px", "Measured window.innerWidth on phone captures"),
        "header-bar": dim("1392px", SRC + "; header island width at 1440"),
    },
}

light = {
    "background": {
        "page": color("{color.page}", SRC),
        "surface": color("{color.white}", SRC + "; contact form card is white against the cream page"),
        "raised": color("{color.field}", SRC + "; empty field fill, same cream as the page"),
        "overlay": color("{color.white}", "Not captured as a separate overlay fill. The products panel is a white header island, so overlay aliases white. The phone menu is a dark panel and is not tokenised as a theme."),
        "scrim": {"$type": "color", "$value": "#151515", "$extensions": {"source": "Not captured as a scrim colour. Phone menu fill was observed as near-black in mobile-home-light-menu.png and is recorded as the ink colour, not a measured scrim token."}},
    },
    "text": {
        "primary": color("{color.ink}", SRC),
        "secondary": color("{color.muted}", SRC),
        "disabled": {"$type": "color", "$value": "#6d6351", "$extensions": {"source": "Not captured. No disabled control was shown on the public pages. The token repeats the muted colour so the role exists, and the coverage row says not captured."}},
        "on-accent": color("{color.white}", SRC + "; Try Free and Schedule a demo label"),
        "link": color("{color.muted}", SRC + "; platform link in the header island footer area computed color rgb(109, 99, 81)"),
        "accent": color("{color.accent-text}", SRC),
    },
    "border": {
        "default": color("{color.hairline}", SRC),
        "strong": color("{color.ink}", "Not captured as a strong border on a control. Ink is the text colour. Recorded so the role is not invented as a new hex."),
        "focus": color("{color.focus}", SRC),
    },
    "action": {
        "primary": color("{color.ink}", SRC + "; Schedule a demo"),
        "primary-hover": color("{color.ink-hover}", SAMPLED),
        "accent": color("{color.accent}", SRC + "; Try Free"),
        "accent-hover": color("{color.accent-hover}", SAMPLED),
        "pressed": color("{color.ink-hover}", "Pressed was forced with CSS.forcePseudoState active+hover. Schedule a demo pressed computed the same oklab as hover, so pressed aliases the sampled hover ink."),
    },
    "status": {
        "success": color("{color.accent}", "Not captured as a status colour. The green is the brand accent, not a success message."),
        "warning": {"$type": "color", "$value": "#6d6351", "$extensions": {"source": "Not captured. No warning colour was painted."}},
        "danger": {"$type": "color", "$value": "#6d6351", "$extensions": {"source": "Not captured. No error colour was painted. Forms were not submitted."}},
        "info": color("{color.focus}", "Not captured as an info status. This is the focus ring colour."),
    },
    "focus": {
        "ring": color("{color.focus}", SRC),
        "width": dim("{border.focus}", SRC),
        "offset": dim("2px", SRC + "; focus-visible outlineOffset 2px on Schedule a demo"),
    },
    "component": {
        "button-primary-bg": color("{color.ink}", SRC),
        "button-primary-text": color("{color.white}", SRC),
        "button-accent-bg": color("{color.accent}", SRC),
        "button-accent-text": color("{color.white}", SRC),
        "field-bg": color("{color.field}", SRC),
        "field-text": color("{color.ink}", SRC),
        "field-radius": dim("{radius.field}", SRC),
        "button-height": dim("{size.button}", SRC),
        "button-radius": dim("{radius.pill}", "Derived from rounded-full"),
    },
}

# The disabled/warning/danger placeholders above would look measured. Remove
# them: a role that was not read is listed under notTokenised, not given a hex.
del light["text"]["disabled"]
del light["status"]["warning"]
del light["status"]["danger"]
del light["background"]["scrim"]
del light["border"]["strong"]

tokens = {
    "$schema": "https://www.designtokens.org/schemas/2025.10/format.json",
    "core": core,
    "light": light,
    "$themes": [{"name": "light", "selectedTokenSets": {"core": "source", "light": "enabled"}}],
    "$extensions": {
        "notTokenised": [
            "Dark theme: not present. prefers-color-scheme dark left body at rgb(246, 244, 239) and h1 at rgb(21, 21, 21). No theme switch exists.",
            "text.disabled, status.warning, status.danger, background.scrim, border.strong: not captured on the public pages.",
            "Pressed colour of Try Free: computed style stayed oklab and was not sampled from a held press.",
            "Elevation: header island shadow computed as none. No dialog shadow was measured.",
            "Spacing scale: OneSoil does not declare one. core.space holds the measured paddings only.",
            "Phone menu fill: observed near-black in the screenshot, not read as a computed colour in this pass.",
        ]
    },
}


def check(node, path=""):
    for key, value in node.items():
        if key.startswith("$") and key not in ("$type", "$value", "$extensions", "$schema", "$themes"):
            continue
        if isinstance(value, dict) and "$value" in value:
            source = value.get("$extensions", {}).get("source", "")
            if not source:
                raise SystemExit(f"missing source: {path}.{key}")
            if value["$type"] == "dimension" and not re.fullmatch(r"-?\d+(\.\d+)?(px|rem)", str(value["$value"])) and not str(value["$value"]).startswith("{"):
                raise SystemExit(f"bad dimension: {path}.{key} {value['$value']}")
        elif isinstance(value, dict) and not key.startswith("$"):
            check(value, f"{path}.{key}")


check(tokens)
out = HERE / "tokens.json"
out.write_text(json.dumps(tokens, indent=2) + "\n")
notes = {
    "captured": "2026-11-21",
    "url": "https://onesoil.ai/en",
    "theme": "light only",
    "widths": [1440, 390],
    "font": "geologica, geologica Fallback, system-ui, sans-serif",
    "sampled": {
        "ink-hover": "#2b2b2b",
        "accent-hover": "#3bb56f",
    },
}
(RAW / "foundations.json").write_text(json.dumps(notes, indent=2) + "\n")
print("wrote", out)
