#!/usr/bin/env python3
"""Build tokens.json from the Limitless public capture.

Limitless ships one painted theme (light). Colour is Tailwind utilities
(slate, zinc, purple-500) plus a few measured fills, not a custom-property
system. Every value here was read from a computed style on 2026-11-18
or derived from those readings. There is no dark set: the product does
not paint one on the public surface.
"""
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
sys.path.insert(0, str(HERE / "tools"))
import motion as motion_mod

MOTION = json.loads((RAW / "motion.json").read_text()) if (RAW / "motion.json").exists() else None


def color(value, source):
    return {"$value": value, "$type": "color", "$extensions": {"source": source}}


def dim(value, source):
    return {"$value": value, "$type": "dimension", "$extensions": {"source": source}}


def num(value, source, ty="number"):
    return {"$value": value, "$type": ty, "$extensions": {"source": source}}


def font(value, source):
    return {"$value": value, "$type": "fontFamily", "$extensions": {"source": source}}


M = "Measured computed style, public Limitless pages, 2026-11-18, light, 1440"
D = "Derived from measured computed styles on the same capture"

core = {
    "color": {
        "slate": {
            "900": color("#0f172a", f"{M}: hero and product titles (text-slate-900)"),
            "800": color("#1e293b", f"{M}: nav link hover ink"),
            "700": color("#334155", f"{M}: help link and carousel icon"),
            "600": color("#475569", f"{M}: nav link and body copy (text-slate-600)"),
            "500": color("#64748b", f"{M}: sign-in link, alpha 0.7 over white"),
            "400": color("#94a3b8", f"{D}: Tailwind slate-400, the muted caption step between 500 and 300"),
            "300": color("#cbd5e1", f"{D}: Tailwind slate-300"),
            "200": color("#e2e8f0", f"{D}: Tailwind slate-200"),
            "100": color("#f1f5f9", f"{M}: code block fill (bg-slate-100)"),
            "50": color("#f8fafc", f"{M}: carousel icon-button hover fill"),
        },
        "zinc": {
            "800": color("#27272a", f"{M}: sign-in card ink and email field"),
            "700": color("#3f3f46", f"{M}: menu item hover ink"),
            "600": color("#52525b", f"{M}: Solutions menu item"),
            "200": color("#e4e4e7", f"{D}: Tailwind zinc-200, the sign-in field hairline family"),
        },
        "gray": {
            "900": color("#111827", f"{M}: FAQ summary ink"),
            "100": color("#f3f4f6", f"{M}: FAQ summary fill"),
        },
        "purple": {
            "500": color("#a855f7", f"{M}: Copy button and developer anchor (purple-500)"),
            "600": color("#9333ea", f"{M}: Copy button hover"),
            "700": color("#7c3aed", f"{M}: sign-in Google button focus ring"),
            "tint": color("rgba(109, 40, 217, 0.05)", f"{M}: Solutions menu item hover fill"),
        },
        "white": color("#ffffff", f"{M}: page, cards, Google button"),
        "ink": color("#1a1a1a", f"{M}: help collection card text, search field focused"),
        "footer": color("#d1d5db", f"{M}: footer link on the dark footer band"),
        "navHover": color("rgba(51, 65, 85, 0.08)", f"{M}: nav link and Solutions hover fill"),
        "focus": color("#005fcc", f"{M}: browser focus-visible outline on links and buttons"),
    },
    "font": {
        "family": {
            "sans": font(
                "Greycliff, system-ui, -apple-system, Roboto, Open Sans, sans-serif",
                f"{M}: body font-family is __greycliff (next/font). The woff files are not shipped; the stack is the declared fallback.",
            ),
            "mono": font(
                "ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace",
                f"{M}: developer code samples",
            ),
        },
        "weight": {
            "regular": num(400, f"{M}: body copy", "fontWeight"),
            "medium": num(500, f"{M}: sign-in link, menu item, Google button", "fontWeight"),
            "semibold": num(600, f"{M}: nav, hero title, help link", "fontWeight"),
            "bold": num(700, f"{M}: wordmark, product title, FAQ, section heading", "fontWeight"),
        },
        "size": {
            "caption": dim("14px", f"{M}: footer link and code"),
            "menu": dim("13px", f"{M}: Solutions menu item, 12.8px rounded"),
            "body": dim("16px", f"{M}: nav, buttons, fields"),
            "body-lg": dim("18px", f"{M}: letter body and FAQ"),
            "heading": dim("36px", f"{M}: section heading on /for/voice-recorder"),
            "display": dim("60px", f"{M}: hero and product titles"),
        },
        "lineHeight": {
            "display": dim("60px", f"{M}: hero title line-height equals 60px size"),
            "body": dim("24px", f"{M}: 16px body, 24px line"),
            "body-lg": dim("28px", f"{D}: 18px letter copy reads relaxed; measured leading-relaxed"),
        },
        "tracking": {
            "display": dim("-1.5px", f"{M}: hero letter-spacing"),
        },
    },
    "typography": {
        "display": {
            "$type": "typography",
            "$value": {
                "fontFamily": "{font.family.sans}",
                "fontSize": "{font.size.display}",
                "fontWeight": "{font.weight.semibold}",
                "lineHeight": "{font.lineHeight.display}",
                "letterSpacing": "{font.tracking.display}",
            },
            "$extensions": {"source": f"{M}: h1 on the acquisition home"},
        },
        "heading": {
            "$type": "typography",
            "$value": {
                "fontFamily": "{font.family.sans}",
                "fontSize": "{font.size.heading}",
                "fontWeight": "{font.weight.bold}",
                "lineHeight": "41px",
            },
            "$extensions": {"source": f"{M}: section h2 on /for/voice-recorder"},
        },
        "body": {
            "$type": "typography",
            "$value": {
                "fontFamily": "{font.family.sans}",
                "fontSize": "{font.size.body}",
                "fontWeight": "{font.weight.regular}",
                "lineHeight": "{font.lineHeight.body}",
            },
            "$extensions": {"source": f"{M}: body default"},
        },
        "body-lg": {
            "$type": "typography",
            "$value": {
                "fontFamily": "{font.family.sans}",
                "fontSize": "{font.size.body-lg}",
                "fontWeight": "{font.weight.regular}",
                "lineHeight": "29px",
            },
            "$extensions": {"source": f"{M}: letter paragraphs, text-lg leading-relaxed"},
        },
        "label": {
            "$type": "typography",
            "$value": {
                "fontFamily": "{font.family.sans}",
                "fontSize": "{font.size.body}",
                "fontWeight": "{font.weight.semibold}",
                "lineHeight": "{font.lineHeight.body}",
            },
            "$extensions": {"source": f"{M}: nav links"},
        },
        "caption": {
            "$type": "typography",
            "$value": {
                "fontFamily": "{font.family.sans}",
                "fontSize": "{font.size.caption}",
                "fontWeight": "{font.weight.medium}",
                "lineHeight": "20px",
            },
            "$extensions": {"source": f"{M}: footer links"},
        },
        "code": {
            "$type": "typography",
            "$value": {
                "fontFamily": "{font.family.mono}",
                "fontSize": "{font.size.caption}",
                "fontWeight": "{font.weight.regular}",
                "lineHeight": "20px",
            },
            "$extensions": {"source": f"{M}: developer code samples"},
        },
    },
    "space": {
        "1": dim("4px", f"{D}: Tailwind spacing unit the utilities are built on"),
        "2": dim("8px", f"{M}: Solutions button padding-block"),
        "3": dim("12px", f"{D}: 4px base times 3"),
        "4": dim("16px", f"{M}: Solutions button padding-inline, body size"),
        "5": dim("20px", f"{D}: 4px base times 5"),
        "6": dim("24px", f"{M}: body line-height, letter card radius"),
        "8": dim("32px", f"{D}: 4px base times 8, nav vertical rhythm"),
        "10": dim("40px", f"{M}: nav control height and carousel icon button"),
        "12": dim("48px", f"{M}: Google button height"),
        "16": dim("64px", f"{D}: 4px base times 16"),
    },
    "radius": {
        "code": dim("4px", f"{M}: code chip and Copy button"),
        "menu": dim("6px", f"{M}: Solutions menu item"),
        "control": dim("8px", f"{M}: FAQ summary, Google button, help card"),
        "search": dim("10px", f"{M}: help search field"),
        "card": dim("24px", f"{M}: letter card"),
        "pill": dim("9999px", f"{M}: nav links, Solutions, carousel arrows"),
    },
    "border": {
        "hairline": dim("1px", f"{M}: focus outline width"),
        "focus": dim("1px", f"{M}: focus-visible outline"),
    },
    "elevation": {
        "card": {
            "$type": "shadow",
            "$value": [{"color": "rgba(15, 23, 42, 0.15)", "offsetX": "0px", "offsetY": "25px", "blur": "50px", "spread": "-12px"}],
            "$extensions": {"source": f"{M}: letter and video cards use shadow-2xl / shadow-slate-800/15"},
        },
        "popover": {
            "$type": "shadow",
            "$value": [{"color": "rgba(15, 23, 42, 0.12)", "offsetX": "0px", "offsetY": "12px", "blur": "24px", "spread": "-8px"}],
            "$extensions": {"source": f"{M}: Solutions menu panel"},
        },
        "control": {
            "$type": "shadow",
            "$value": [{"color": "rgba(0, 0, 0, 0.1)", "offsetX": "0px", "offsetY": "1px", "blur": "2px", "spread": "0px"}],
            "$extensions": {"source": f"{M}: carousel icon button"},
        },
    },
    "layout": {
        "page": dim("1440px", f"{M}: desktop capture width"),
        "phone": dim("390px", f"{M}: phone capture width"),
        "content": dim("1024px", f"{M}: letter card width, max-w-5xl"),
        "prose": dim("896px", f"{M}: hero title width, max-w-4xl"),
        "navHeight": dim("64px", f"{M}: top bar"),
    },
}

light = {
    "page": color("{color.white}", f"{M}: marketing page background"),
    "surface": color("{color.white}", f"{M}: letter card, help card, Google button"),
    "surfaceMuted": color("{color.gray.100}", f"{M}: FAQ summary"),
    "surfaceCode": color("{color.slate.100}", f"{M}: inline code"),
    "text": color("{color.slate.900}", f"{M}: titles"),
    "textBody": color("{color.slate.600}", f"{M}: letter and nav"),
    "textMuted": color("rgba(100, 116, 139, 0.7)", f"{M}: Sign In link"),
    "textOnAccent": color("{color.white}", f"{M}: Copy button label"),
    "link": color("{color.purple.500}", f"{M}: developer anchors"),
    "accent": color("{color.purple.500}", f"{M}: Copy, wordmark, Join #developers"),
    "accentHover": color("{color.purple.600}", f"{M}: Copy hover"),
    "navHover": color("{color.navHover}", f"{M}: nav hover wash"),
    "focus": color("{color.focus}", f"{M}: focus-visible outline"),
    "border": color("{color.slate.200}", f"{D}: hairline family around cards"),
    "footerInk": color("{color.footer}", f"{M}: footer links"),
    "helpBand": color("#8a54e1", f"Measured from the help center stylesheet harvest: purple header band"),
}

# Alias check
def walk(node, prefix=""):
    for k, v in node.items():
        if k.startswith("$"):
            continue
        path = f"{prefix}.{k}" if prefix else k
        if isinstance(v, dict) and "$value" in v:
            yield path, v
        elif isinstance(v, dict):
            yield from walk(v, path)

names = {n for n, _ in walk(core)}
names |= {n for n, _ in walk(light)}
import re
def alias_ok(alias):
    if alias in names:
        return True
    # {color.slate.900} is core.color.slate.900
    return alias.startswith("color.") and alias in names

def strings(v):
    if isinstance(v, str):
        yield v
    elif isinstance(v, dict):
        for x in v.values():
            yield from strings(x)
    elif isinstance(v, list):
        for x in v:
            yield from strings(x)

for path, tok in list(walk({"core": core, "light": light})):
    for blob in strings(tok["$value"]):
        for alias in re.findall(r"\{([^{}]+)\}", blob):
            if not alias_ok(alias):
                raise SystemExit(f"{path} alias {{{alias}}} missing")

if MOTION:
    core["motion"], extra = motion_mod.build(MOTION)
    if extra:
        core["motion"].setdefault("$extensions", {})["notTokenised"] = extra

tokens = {
    "core": core,
    "light": light,
    "$themes": [{
        "id": "light",
        "name": "Light",
        "selectedTokenSets": {"core": "source", "light": "enabled"},
        "$description": "The only painted theme on the public Limitless site, 2026-11-18.",
    }],
    "$metadata": {"tokenSetOrder": ["core", "light"]},
}
(HERE / "tokens.json").write_text(json.dumps(tokens, indent=2) + "\n")
print("tokens", len(names))
