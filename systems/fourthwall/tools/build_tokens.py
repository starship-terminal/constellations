#!/usr/bin/env python3
"""Build tokens.json from Fourthwall's declared custom properties.

Source: raw/css-vars.json, read live from https://fourthwall.com/ on 2026-11-21,
signed out. Fourthwall declares a primitive set (--_primitives---*), a surface
role set (--_surface---*), and older ramps (--gs*, --b*, --g*, --r*, --y*).
Fluid clamps and percentages are recorded under $extensions.notTokenised
because DTCG dimensions here are one px or rem length.

The public site paints one light theme. Dark is not present. Every token
carries $extensions.source. Deterministic.
"""
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = json.loads((HERE / "raw" / "css-vars.json").read_text())
RES = RAW["resolved"]
SRC = "declared on :root, live https://fourthwall.com/ 2026-11-21 (raw/css-vars.json)"


def norm_color(v):
    v = str(v).strip().lower()
    named = {"white": "#ffffff", "black": "#000000"}
    if v in named:
        return named[v]
    m = re.fullmatch(r"#([0-9a-f]{3,8})", v)
    if m:
        h = m.group(1)
        if len(h) in (3, 4):
            h = "".join(c * 2 for c in h)
        if len(h) == 8:
            a = int(h[6:8], 16) / 255
            if a >= 0.999:
                return "#" + h[:6]
            return "rgba(%d, %d, %d, %s)" % (*[int(h[i:i + 2], 16) for i in (0, 2, 4)], "%g" % round(a, 3))
        return "#" + h
    m = re.fullmatch(r"rgba?\(\s*(\d+)[,\s]+(\d+)[,\s]+(\d+)(?:\s*[,/]\s*([\d.]+))?\s*\)", v)
    if m:
        r, g, b, a = m.groups()
        a = float(a) if a else 1
        if a >= 1:
            return "#%02x%02x%02x" % (int(r), int(g), int(b))
        return "rgba(%d, %d, %d, %s)" % (int(r), int(g), int(b), "%g" % round(a, 3))
    raise ValueError("not a colour: " + v)


def color(name, token_name, description):
    return {
        "$value": norm_color(RES[name]),
        "$type": "color",
        "$description": description,
        "$extensions": {"source": f"Measured. {SRC}. {name}={RES[name]}"},
    }


def dim(name, description):
    val = RES[name].strip()
    if not re.fullmatch(r"-?\d*\.?\d+px", val):
        raise ValueError(name + " is not a px length: " + val)
    return {
        "$value": val,
        "$type": "dimension",
        "$description": description,
        "$extensions": {"source": f"Measured. {SRC}. {name}={val}"},
    }


def number(name, description, typ="number"):
    val = RES[name].strip()
    if typ == "fontWeight":
        return {"$value": int(float(val)), "$type": "fontWeight", "$description": description,
                "$extensions": {"source": f"Measured. {SRC}. {name}={val}"}}
    return {"$value": float(val) if "." in val else int(val), "$type": "number", "$description": description,
            "$extensions": {"source": f"Measured. {SRC}. {name}={val}"}}


def font_family(name, description):
    return {
        "$value": RES[name].strip().strip('"'),
        "$type": "fontFamily",
        "$description": description,
        "$extensions": {"source": f"Measured. {SRC}. {name}={RES[name]}"},
    }


core = {
    "$description": "Fourthwall primitives declared on :root. One light theme on the public site.",
    "color": {
        "ink": color("--_primitives---color--ink", "ink", "Near-black ink. Page text and the action fill."),
        "inkDeep": color("--_primitives---color--ink-deep", "inkDeep", "A deeper ink for sunken dark bands."),
        "inkSoft": color("--_primitives---color--ink-soft", "inkSoft", "Soft ink, one step off deep."),
        "inkSunken": color("--_primitives---color--ink-sunken", "inkSunken", "Sunken ink."),
        "inkViolet": color("--_primitives---color--ink-violet", "inkViolet", "A violet-cast ink."),
        "muted": color("--_primitives---color--muted", "muted", "Muted grey for secondary text."),
        "notice": color("--_primitives---color--notice", "notice", "Pale notice yellow."),
        "paper": color("--_primitives---color--paper", "paper", "Page paper. Declared as white."),
        "paperSoft": color("--_primitives---color--paper-soft", "paperSoft", "Soft paper for quiet sections."),
        "paperSunken": color("--_primitives---color--paper-sunken", "paperSunken", "Sunken paper, the canvas."),
        "inkAlpha06": color("--_primitives---color--ink-alpha-06", "inkAlpha06", "Ink at 6%."),
        "inkAlpha11": color("--_primitives---color--ink-alpha-11", "inkAlpha11", "Ink at 11%."),
        "inkAlpha16": color("--_primitives---color--ink-alpha-16", "inkAlpha16", "Ink at 16%. The hairline."),
        "inkAlpha25": color("--_primitives---color--ink-alpha-25", "inkAlpha25", "Ink at 25%."),
        "inkAlpha60": color("--_primitives---color--ink-alpha-60", "inkAlpha60", "Ink at 60%. Soft text."),
        "paperAlpha08": color("--_primitives---color--paper-alpha-08", "paperAlpha08", "Paper at 8%."),
        "paperAlpha16": color("--_primitives---color--paper-alpha-16", "paperAlpha16", "Paper at 16%."),
        "paperAlpha50": color("--_primitives---color--paper-alpha-50", "paperAlpha50", "Paper at 50%."),
        "paperAlpha85": color("--_primitives---color--paper-alpha-85", "paperAlpha85", "Paper at 85%."),
        "gray": {
            "0": color("--gs0", "gray.0", "Grey ramp, lightest. Declared white."),
            "100": color("--gs100", "gray.100", "Grey ramp 100."),
            "200": color("--gs200", "gray.200", "Grey ramp 200."),
            "300": color("--gs300", "gray.300", "Grey ramp 300."),
            "400": color("--gs400", "gray.400", "Grey ramp 400."),
            "500": color("--gs500", "gray.500", "Grey ramp 500."),
            "550": color("--gs550", "gray.550", "Grey ramp 550."),
            "600": color("--gs600", "gray.600", "Grey ramp 600."),
            "700": color("--gs700", "gray.700", "Grey ramp 700."),
            "800": color("--gs800", "gray.800", "Grey ramp 800."),
            "900": color("--gs900", "gray.900", "Grey ramp 900."),
            "1000": color("--gs1000", "gray.1000", "Grey ramp, darkest. Same ink as the primitive."),
        },
        "blue": {str(n): color(f"--b{n}", f"blue.{n}", f"Blue ramp {n}.") for n in (100, 200, 300, 400, 500, 600, 700)},
        "green": {str(n): color(f"--g{n}", f"green.{n}", f"Green ramp {n}.") for n in (100, 200, 300, 400, 500)},
        "red": {str(n): color(f"--r{n}", f"red.{n}", f"Red ramp {n}.") for n in (100, 200, 300, 400, 500)},
        "yellow": {str(n): color(f"--y{n}", f"yellow.{n}", f"Yellow ramp {n}.") for n in (100, 200, 300, 400, 500)},
        "twitch": color("--twitch", "twitch", "Twitch purple, a partner accent on audience pages."),
    },
    "font": {
        "family": {
            "body": font_family("--_primitives---font-family--body", "Suisse Intl for body. Arial is the fallback."),
            "display": font_family("--_primitives---font-family--display", "Saans for display. Not captured as a file."),
            "heading": font_family("--font-heading", "PP Telegraf for headings. A second display family, declared as --font-heading."),
        },
        "size": {
            "body": dim("--_primitives---font-size--body-static", "Static body size. Fluid sizes are not tokenised."),
            "labelXs": dim("--_primitives---font-size--label-xs", "Smallest label."),
            "labelSm": dim("--_primitives---font-size--label-sm", "Small label."),
            "labelMd": dim("--_primitives---font-size--label-md", "Medium label."),
            "labelLg": dim("--_primitives---font-size--label-lg", "Large label."),
        },
        "weight": {
            str(w): number(f"--_primitives---weight--{w}", f"Variable-font weight {w}.", "fontWeight")
            for w in (300, 400, 420, 435, 450, 465, 480, 500, 600, 700)
        },
        "lineHeight": {
            name: number(f"--_primitives---line-height--{name}", f"Unitless line height {name}.")
            for name in ("none", "flat", "tight", "compact", "snug", "normal", "relaxed")
        },
    },
    "radius": {
        "xs": dim("--_primitives---radius--xs", "6px."),
        "sm": dim("--_primitives---radius--sm", "8px."),
        "md": dim("--_primitives---radius--md", "10px."),
        "lg": dim("--_primitives---radius--lg", "12px."),
        "xl": dim("--_primitives---radius--xl", "14px."),
        "2xl": dim("--_primitives---radius--2xl", "18px."),
        "pill": dim("--_primitives---radius--pill", "999px pill."),
    },
    "space": {
        n: dim(f"--_primitives---space--{n}", f"{n}px space step.")
        for n in ("1", "2", "4", "6", "8", "10", "12", "14", "16", "18", "20", "22", "24", "28", "32", "36", "40", "48", "56", "64", "80", "88", "96", "120", "140", "180", "200")
    },
    "layout": {
        "column": dim("--_primitives---layout--column", "A 768px column."),
        "pageMax": dim("--_primitives---layout--page-max", "The page max width."),
        "sectionPadX": dim("--_rhythm---section--pad-x", "Horizontal section padding."),
        "sectionPadYXs": dim("--_rhythm---section--pad-y-xs", "Smallest section padding."),
        "sectionPadYMd": dim("--_rhythm---section--pad-y-md", "Medium section padding."),
        "cardPad": dim("--_rhythm---card--pad", "Card padding."),
        "cardGap": dim("--_rhythm---card--gap", "Card gap."),
        "stackXs": dim("--_rhythm---stack--xs", "Smallest stack gap."),
    },
    "typography": {
        "body": {
            "$value": {"fontFamily": "{font.family.body}", "fontSize": "{font.size.body}", "fontWeight": "{font.weight.400}", "lineHeight": "{font.lineHeight.relaxed}"},
            "$type": "typography",
            "$extensions": {"source": "Derived from declared body family, static 16px size, weight 400 and line-height relaxed."},
        },
        "label": {
            "$value": {"fontFamily": "{font.family.body}", "fontSize": "{font.size.labelLg}", "fontWeight": "{font.weight.450}", "lineHeight": "{font.lineHeight.snug}"},
            "$type": "typography",
            "$extensions": {"source": "Derived. Nav and button labels read 450 on Suisse Intl at 14px in raw/components-computed.json when that file has a button reading; the size and weight are the declared tokens."},
        },
        "heading": {
            "$value": {"fontFamily": "{font.family.heading}", "fontSize": "{font.size.labelLg}", "fontWeight": "{font.weight.500}", "lineHeight": "{font.lineHeight.tight}"},
            "$type": "typography",
            "$extensions": {"source": "Derived from --font-heading. Display sizes are fluid clamps and are not tokenised."},
        },
    },
}

light = {
    "$description": "Semantic roles. Fourthwall's public site ships one light theme.",
    "background": {
        "page": {"$value": "{color.paper}", "$type": "color", "$extensions": {"source": f"Measured alias of --_surface---bg--page ({RES['--_surface---bg--page']}). {SRC}"}},
        "surface": {"$value": "{color.paperSoft}", "$type": "color", "$extensions": {"source": f"Measured alias of --_surface---bg--section-soft ({RES['--_surface---bg--section-soft']}). {SRC}"}},
        "canvas": {"$value": "{color.paperSunken}", "$type": "color", "$extensions": {"source": f"Measured alias of --_surface---bg--canvas ({RES['--_surface---bg--canvas']}). {SRC}"}},
        "subtle": {"$value": "{color.inkAlpha06}", "$type": "color", "$extensions": {"source": f"Measured alias of --_surface---surface-bg--subtle ({RES['--_surface---surface-bg--subtle']}). {SRC}"}},
        "raised": {"$value": "{color.paper}", "$type": "color", "$description": "No separate raised token. Menus paint on paper.", "$extensions": {"source": "Derived. --_surface has no raised role. Menus use the page paper."}},
    },
    "text": {
        "primary": {"$value": "{color.ink}", "$type": "color", "$extensions": {"source": f"Measured alias of --_surface---text--body ({RES['--_surface---text--body']}). {SRC}"}},
        "heading": {"$value": "{color.ink}", "$type": "color", "$extensions": {"source": f"Measured alias of --_surface---text--heading ({RES['--_surface---text--heading']}). {SRC}"}},
        "secondary": {"$value": "{color.inkAlpha60}", "$type": "color", "$extensions": {"source": f"Measured alias of --_surface---text--soft ({RES['--_surface---text--soft']}). {SRC}"}},
        "muted": {"$value": "{color.muted}", "$type": "color", "$extensions": {"source": f"Measured alias of --_primitives---color--muted ({RES['--_primitives---color--muted']}). {SRC}"}},
        "link": {"$value": "{color.ink}", "$type": "color", "$extensions": {"source": f"Measured alias of --_surface---text--link ({RES['--_surface---text--link']}). Links are ink, not a second hue. {SRC}"}},
        "onAccent": {"$value": "{color.paper}", "$type": "color", "$extensions": {"source": f"Measured alias of --_surface---text--action ({RES['--_surface---text--action']}). {SRC}"}},
        "disabled": {"$value": "{color.muted}", "$type": "color", "$description": "No disabled text token was declared. This aliases muted and is labelled Derived.", "$extensions": {"source": "Derived. No --_surface text disabled token. Not captured as its own role."}},
    },
    "border": {
        "default": {"$value": "{color.inkAlpha16}", "$type": "color", "$extensions": {"source": f"Measured alias of --_surface---border--hairline ({RES['--_surface---border--hairline']}). {SRC}"}},
        "strong": {"$value": "{color.ink}", "$type": "color", "$description": "No strong border token. Ink is the strong edge.", "$extensions": {"source": "Derived. No --_surface border strong token."}},
        "focus": {"$value": "{color.ink}", "$type": "color", "$description": "No focus-ring colour was declared.", "$extensions": {"source": "Not captured as a declared token. Derived to ink so the role exists; confirm against a focus-visible crop."}},
    },
    "accent": {
        "default": {"$value": "{color.ink}", "$type": "color", "$extensions": {"source": f"Measured alias of --_surface---bg--action ({RES['--_surface---bg--action']}). The action fill is ink, not a brand hue. {SRC}"}},
        "hover": {"$value": "{color.inkSoft}", "$type": "color", "$description": "No action-hover token was declared.", "$extensions": {"source": "Not captured. No --_surface action hover token. inkSoft is the nearest declared dark step, marked Derived."}},
        "pressed": {"$value": "{color.inkDeep}", "$type": "color", "$description": "No action-pressed token was declared.", "$extensions": {"source": "Not captured. No --_surface action pressed token. inkDeep is the nearest declared dark step, marked Derived."}},
    },
    "status": {
        "success": {"$value": "{color.green.400}", "$type": "color", "$extensions": {"source": "Derived from the green ramp. Fourthwall declares no success role."}},
        "warning": {"$value": "{color.yellow.300}", "$type": "color", "$extensions": {"source": "Derived from the yellow ramp. Fourthwall declares no warning role. --_primitives---color--notice is the pale notice yellow."}},
        "danger": {"$value": "{color.red.300}", "$type": "color", "$extensions": {"source": "Derived from the red ramp. Fourthwall declares no danger role."}},
        "info": {"$value": "{color.blue.500}", "$type": "color", "$extensions": {"source": "Derived from the blue ramp. Fourthwall declares no info role."}},
    },
}

not_tokenised = {
    "fluidType": {k: RES[k] for k in RES if "font-size--body-fluid" in k or "font-size--display" in k},
    "fluidRhythm": {k: RES[k] for k in RES if k.startswith("--_rhythm") and "clamp" in RES[k]},
    "radiusCircle": RES.get("--_primitives---radius--circle"),
    "letterSpacing": {k: RES[k] for k in RES if "letter-spacing" in k},
    "cookieConsent": "Cookiebot --cc-* variables were declared. The banner was hidden and never accepted. Those values are not Fourthwall's system and are not tokenised.",
    "unread": [
        "Dark theme: not present on the public site.",
        "Focus ring colour: not declared.",
        "Disabled, loading and error control colours: not reached. Nothing was submitted.",
        "Signed-in app tokens: not captured.",
    ],
}
core["$extensions"] = {"notTokenised": not_tokenised}

tokens = {
    "core": core,
    "light": light,
    "$themes": [{
        "id": "light",
        "name": "Light",
        "selectedTokenSets": {"core": "source", "light": "enabled"},
        "$description": "The only theme the public site paints. color-scheme was normal and data-theme was unset.",
    }],
    "$metadata": {"tokenSetOrder": ["core", "light"]},
}

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from token_checks import alias_errors  # noqa: E402

errors = alias_errors(core, light, {})
if errors:
    raise SystemExit("\n".join(errors))

(HERE / "tokens.json").write_text(json.dumps(tokens, indent=1, ensure_ascii=False) + "\n")


def count(d):
    return sum(1 if isinstance(v, dict) and "$value" in v else count(v) if isinstance(v, dict) else 0 for v in d.values())


print(f"tokens.json: core {count(core)} + light {count(light)} = {count(core) + count(light)}")
