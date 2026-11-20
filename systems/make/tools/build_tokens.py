#!/usr/bin/env python3
"""Build tokens.json from the Make public capture.

Marketing pages declare a Webflow token set on :root (--_default---swatch--*,
--_theme---*, --_typography---*). Those literals are copied from
raw/css-vars.json. Computed styles on 2026-11-18 confirm the painted roles.
There is no dark set: the captured public pages do not paint one.
"""
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
sys.path.insert(0, str(HERE / "tools"))
import motion as motion_mod

MOTION = json.loads((RAW / "motion.json").read_text()) if (RAW / "motion.json").exists() else None
CSS = json.loads((RAW / "css-vars.json").read_text())
DECLARED = CSS["pages"]["https://www.make.com/"]["declared"]

M = "Measured computed style or declared custom property, public Make pages, 2026-11-18, light, 1440"
D = "Derived from the declared swatch set on the same capture"


def color(value, source):
    return {"$value": value, "$type": "color", "$extensions": {"source": source}}


def dim(value, source):
    return {"$value": value, "$type": "dimension", "$extensions": {"source": source}}


def num(value, source, ty="number"):
    return {"$value": value, "$type": ty, "$extensions": {"source": source}}


def font(value, source):
    return {"$value": value, "$type": "fontFamily", "$extensions": {"source": source}}


def swatch(name):
    key = f"--_default---swatch--{name}"
    value = DECLARED[key]
    return color(value, f"{M}: {key} = {value}")


def ramp(prefix):
    steps = {}
    for key, value in sorted(DECLARED.items()):
        if not key.startswith(f"--_default---swatch--{prefix}-"):
            continue
        step = key.split(f"--_default---swatch--{prefix}-", 1)[1]
        if not re.match(r"\d", step):
            continue
        token = step.replace("-main", "")
        steps[token] = color(value, f"{M}: {key} = {value}")
    return steps


core = {
    "color": {
        "brand": ramp("brand"),
        "neutral": ramp("neutral"),
        "accent": ramp("accent"),
        "green": ramp("green"),
        "red": ramp("red"),
        "yellow": ramp("yellow"),
        "gray": ramp("gray"),
        "white": color("#ffffff", f"{M}: --_theme---background resolves to rgb(255, 255, 255)"),
        "ink": color("#342237", f"{M}: --_default---swatch--neutral-900, hero colour"),
        "signinGradientStart": color("#ff00ff", f"{M}: sign-in submit radial-gradient start rgb(255, 0, 255)"),
        "signinGradientEnd": color("#724ebf", f"{M}: sign-in submit radial-gradient end rgb(114, 78, 191)"),
        "googleInk": color("#1d1d1d", f"{M}: Continue with Google label"),
    },
    "font": {
        "family": {
            "sans": font("Satoshi, Arial, sans-serif", f"{M}: --_typography---font--primary-family"),
            "fallback": font("Arial, Helvetica, sans-serif", f"{M}: templates body before Satoshi paints the heading"),
        },
        "weight": {
            "regular": num(400, f"{M}: --_typography---font--primary-regular", "fontWeight"),
            "medium": num(500, f"{M}: --_typography---font--primary-medium; hero h1", "fontWeight"),
            "bold": num(800, f"{M}: --_typography---font--primary-bold", "fontWeight"),
        },
        "size": {
            "chip": dim("14px", f"{M}: category chip and billing toggle"),
            "body": dim("16px", f"{M}: Try it free and body"),
            "price": dim("30px", f"{M}: plan price $16"),
            "credits": dim("36px", f"{M}: 10,000 credits/mo"),
            "heading": dim("48px", f"{M}: pricing h1"),
            "display": dim("60px", f"{M}: home h1"),
        },
        "lineHeight": {
            "display": dim("72px", f"{M}: home h1 line-height"),
            "body": dim("24px", f"{D}: 16px body at 1.5"),
        },
        "tracking": {
            "display": dim("-1.2px", f"{M}: home h1 letter-spacing"),
        },
    },
    "radius": {
        "small": dim("8px", f"{M}: --_default---radius--small is .5rem; Try it free is 8px"),
        "medium": dim("12px", f"{M}: --_default---radius--medium is .75rem; Google button is 12px"),
        "signin": dim("10px", f"{M}: sign-in submit border-radius"),
        "search": dim("16px", f"{M}: templates search shell"),
        "main": dim("16px", f"{M}: --_default---radius--main is 1rem"),
        "pill": dim("9999px", f"{M}: Popular and Save 15% badges"),
        "chip": dim("38px", f"{M}: templates category chip"),
    },
    "space": {
        "2": dim("8px", f"{D}: 0.5rem step beside the declared radii"),
        "4": dim("16px", f"{M}: search shell radius and a common padding step"),
        "5": dim("18px", f"{M}: Try it free padding-inline"),
    },
    "elevation": {
        "search": {
            "$type": "shadow",
            "$value": [{
                "color": "rgba(0, 0, 0, 0.12)",
                "offsetX": "0px",
                "offsetY": "5px",
                "blur": "10px",
                "spread": "0px",
            }],
            "$extensions": {"source": f"{M}: templates search shell box-shadow"},
        },
    },
    "typography": {
        "display": {
            "$type": "typography",
            "$value": {
                "fontFamily": "{font.family.sans}",
                "fontSize": "{font.size.display}",
                "fontWeight": "{font.weight.medium}",
                "lineHeight": "{font.lineHeight.display}",
                "letterSpacing": "{font.tracking.display}",
            },
            "$extensions": {"source": f"{M}: home h1"},
        },
        "heading": {
            "$type": "typography",
            "$value": {
                "fontFamily": "{font.family.sans}",
                "fontSize": "{font.size.heading}",
                "fontWeight": "{font.weight.medium}",
                "lineHeight": "60px",
            },
            "$extensions": {"source": f"{M}: pricing h1, 48px"},
        },
        "body": {
            "$type": "typography",
            "$value": {
                "fontFamily": "{font.family.sans}",
                "fontSize": "{font.size.body}",
                "fontWeight": "{font.weight.regular}",
                "lineHeight": "{font.lineHeight.body}",
            },
            "$extensions": {"source": f"{M}: body and primary button"},
        },
        "label": {
            "$type": "typography",
            "$value": {
                "fontFamily": "{font.family.sans}",
                "fontSize": "{font.size.chip}",
                "fontWeight": "{font.weight.regular}",
                "lineHeight": "20px",
            },
            "$extensions": {"source": f"{M}: billing toggle and category chip"},
        },
    },
    "layout": {
        "desktop": dim("1440px", "Reconstruction: the desktop capture viewport of 2026-11-18, not a width the product declares"),
        "phone": dim("390px", "Reconstruction: the phone capture viewport of 2026-11-18, not a width the product declares"),
    },
}

light = {
    "page": color("{color.white}", f"{M}: --_theme---background"),
    "surface": color("{color.white}", f"{M}: search shell and Google button"),
    "surfaceMuted": color("{color.neutral.100}", f"{M}: nav hover wash rgb(243, 242, 243) and category chip"),
    "text": color("{color.ink}", f"{M}: --_theme---text"),
    "textBody": color("#69586c", f"{M}: --_theme---text-secondary resolves to rgb(105, 88, 108), swatch neutral-600"),
    "textMuted": color("#867489", f"{M}: --_theme---text-placeholder, swatch neutral-500"),
    "textTertiary": color("#58475a", f"{M}: nav link rgb(88, 71, 90), swatch neutral-700"),
    "textOnAccent": color("{color.white}", f"{M}: Try it free label"),
    "link": color("#803bbf", f"{M}: --_theme---text-link--text, brand-700"),
    "accent": color("#8f4bd2", f"{M}: --_theme---button-primary--background, brand-600"),
    "accentHover": color("#803bbf", f"{M}: --_theme---button-primary--background-hover, brand-700; Try it free hover"),
    "border": color("#dad4da", f"{M}: --_theme---border, swatch neutral-300"),
    "borderStrong": color("#b0a6b1", f"{M}: swatch neutral-400, the stronger hairline in the ramp"),
    "focus": color("#a66ee2", f"{M}: --_theme---border-brand, brand-500-main"),
    "successFill": color("{color.green.50}", f"{M}: Save 15% badge fill rgb(240, 253, 244)"),
    "successText": color("{color.green.800}", f"{M}: Save 15% text rgb(21, 128, 61) is green-800"),
    "badgeFill": color("{color.brand.50}", f"{M}: Popular badge fill rgb(250, 247, 254)"),
    "badgeText": color("{color.brand.700}", f"{M}: Popular badge text"),
    "signinGradientStart": color("{color.signinGradientStart}", f"{M}: sign-in submit gradient"),
    "signinGradientEnd": color("{color.signinGradientEnd}", f"{M}: sign-in submit gradient"),
}


def walk(node, prefix=""):
    for k, v in node.items():
        if k.startswith("$"):
            continue
        path = f"{prefix}.{k}" if prefix else k
        if isinstance(v, dict) and "$value" in v:
            yield path, v
        elif isinstance(v, dict):
            yield from walk(v, path)


names = {n for n, _ in walk(core)} | {n for n, _ in walk(light)}


def alias_ok(alias):
    return alias in names or (alias.startswith("color.") and alias in names)


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
        "$description": "The painted theme on captured Make public pages, 2026-11-18.",
    }],
    "$metadata": {"tokenSetOrder": ["core", "light"]},
}
TEXT = json.dumps(tokens, indent=2) + "\n"

if __name__ == "__main__":
    (HERE / "tokens.json").write_text(TEXT)
    print("tokens", len(names))
