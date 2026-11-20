#!/usr/bin/env python3
"""Build tokens.json from the Mangomint public capture.

Marketing colour is CSS-module literals, measured on live elements on
2026-11-18. The app host declares --color-* on :root (raw/css-vars.json).
The booking host declares --base-color, --button-color and --mt-duration-*.
One painted marketing theme (light). The login wall paints navy; that is a
surface, not a second theme. No dark set.
"""
import json
import re
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
sys.path.insert(0, str(HERE / "tools"))
import motion as motion_mod

MOTION = json.loads((RAW / "motion.json").read_text()) if (RAW / "motion.json").exists() else None

M = "Measured computed style, public Mangomint pages, 2026-11-18, light, 1440"
A = "Measured computed style, app.mangomint.com/login, 2026-11-18, light, 1440"
B = "Measured computed style, booking.mangomint.com/737397, 2026-11-18, light, 1440"
D = "Derived from a measured computed style on the same capture"
V = "Declared custom property, app.mangomint.com main stylesheet :root, 2026-11-18"


def color(value, source):
    return {"$value": value, "$type": "color", "$extensions": {"source": source}}


def dim(value, source):
    return {"$value": value, "$type": "dimension", "$extensions": {"source": source}}


def num(value, source, ty="number"):
    return {"$value": value, "$type": ty, "$extensions": {"source": source}}


def font(value, source):
    return {"$value": value, "$type": "fontFamily", "$extensions": {"source": source}}


core = {
    "color": {
        "ink": color("#191e49", f"{M}: body, h1 and nav text rgb(25, 30, 73); also {V}: --color-primary and --color-navy-600"),
        "page": color("#fcfafa", f"{M}: body background rgb(252, 250, 250)"),
        "white": color("#ffffff", f"{A}: login card field sits on navy; booking card is white"),
        "magenta": color("#bc269b", f"{M}: Try it now fill and Book a demo ink rgb(188, 38, 155)"),
        "magentaPressed": color("#921185", f"{M}: Try it now hover and video-tour hover rgb(146, 17, 133)"),
        "cream": color("#fcfafa", f"{M}: text on the filled magenta button rgb(252, 250, 250)"),
        "focus": color("#005fcc", f"{M}: focus-visible outline on Log in and Businesses rgb(0, 95, 204)"),
        "navy125": color("#f1f2f6", f"{V}: --color-navy-125. Not sampled on a painted marketing element"),
        "navy400": color("#697498", f"{V}: --color-navy-400"),
        "gray200": color("#dfe2e8", f"{V}: --color-gray-200"),
        "purple100": color("#f6f1fe", f"{V}: --color-purple-100"),
        "blue": color("#2e3289", f"{A}: filled email field border rgb(46, 50, 137); also {V}: --color-blue"),
        "fieldMuted": color("#afb8ce", f"{A}: login placeholder and field text rgb(175, 184, 206)"),
        "loginButton": color("#b28eff", f"{A}: Log In button fill rgb(178, 142, 255)"),
        "loginButtonHover": color("#c1a5ff", f"{A}: Log In button hover rgb(193, 165, 255)"),
        "fieldWash": color("rgba(255, 255, 255, 0.1)", f"{A}: login field background"),
        "fieldWashFilled": color("rgba(255, 255, 255, 0.15)", f"{A}: login email field after a throwaway address was typed"),
        "iconOnNavy": color("rgba(255, 255, 255, 0.6)", f"{A}: password visibility icon"),
        "iconOnNavyHover": color("rgba(255, 255, 255, 0.9)", f"{A}: password visibility icon hover"),
        "bookInk": color("#474f7b", f"{B}: Rebook a past service rgb(71, 79, 123)"),
        "searchPlaceholder": color("#787fa7", f"{M}: Learning Center search placeholder rgb(120, 127, 167)"),
        "searchFill": color("#fdfdff", f"{M}: Learning Center search background rgb(253, 253, 255)"),
    },
    "font": {
        "family": {
            "sans": font("tt-commons-pro, sans-serif", f"{M}: body font-family"),
            "app": font("tt-commons, sans-serif", f"{A}: login field and Log In button"),
            "mono": font("tt-commons-mono, monospace", f"{M}: Watch a video tour"),
            "fallback": font("Muli, sans-serif", f"{A}: password visibility button; the icon is the visible content"),
        },
        "weight": {
            "regular": num(400, f"{M}: body and menu item", "fontWeight"),
            "medium": num(500, f"{A}: Log In button", "fontWeight"),
            "semibold": num(540, f"{M}: nav and filled button. The computed weight is 540, not 600", "fontWeight"),
            "display": num(620, f"{M}: home h1 computed font-weight 620", "fontWeight"),
        },
        "size": {
            "caption": dim("14px", f"{M}: video tour; also {B}: rebook link"),
            "body": dim("16px", f"{M}: body and buttons"),
            "nav": dim("17px", f"{M}: nav link and Businesses button"),
            "display": dim("54px", f"{M}: home h1"),
            "displayLine": dim("60px", f"{M}: home h1 line-height"),
        },
        "lineHeight": {
            "body": dim("22.4px", f"{M}: body line-height"),
            "nav": dim("21px", f"{M}: nav link line-height"),
            "button": dim("16px", f"{M}: filled button line-height equals its font size"),
        },
    },
    "typography": {
        "display": {
            "$type": "typography",
            "$value": {
                "fontFamily": "{font.family.sans}",
                "fontSize": "{font.size.display}",
                "fontWeight": "{font.weight.display}",
                "lineHeight": "{font.size.displayLine}",
            },
            "$extensions": {"source": f"{M}: home h1 'Everything you need to power your salon and spa'"},
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
        "label": {
            "$type": "typography",
            "$value": {
                "fontFamily": "{font.family.sans}",
                "fontSize": "{font.size.nav}",
                "fontWeight": "{font.weight.semibold}",
                "lineHeight": "{font.lineHeight.nav}",
            },
            "$extensions": {"source": f"{M}: nav link"},
        },
        "button": {
            "$type": "typography",
            "$value": {
                "fontFamily": "{font.family.sans}",
                "fontSize": "{font.size.body}",
                "fontWeight": "{font.weight.semibold}",
                "lineHeight": "{font.lineHeight.button}",
            },
            "$extensions": {"source": f"{M}: Try it now and Book a demo"},
        },
        "caption": {
            "$type": "typography",
            "$value": {
                "fontFamily": "{font.family.mono}",
                "fontSize": "{font.size.caption}",
                "fontWeight": "{font.weight.regular}",
                "lineHeight": "19.6px",
                "letterSpacing": "0.42px",
            },
            "$extensions": {"source": f"{M}: Watch a video tour, uppercase mono"},
        },
    },
    "space": {
        "2": dim("8px", f"{M}: nav link padding"),
        "4": dim("16px", f"{M}: button padding-block and menu item padding-block"),
        "5": dim("20px", f"{A}: login field padding-left"),
        "6": dim("25px", f"{M}: button padding-inline"),
        "10": dim("40px", f"{M}: header padding-inline"),
    },
    "radius": {
        "pill": dim("48px", f"{M}: Book a demo and Try it now border-radius"),
        "login": dim("5px", f"{A}: Log In button border-radius"),
    },
    "size": {
        "button": dim("48px", f"{M}: Try it now and Book a demo height"),
        "nav": dim("37px", f"{M}: Log in link height"),
        "field": dim("50px", f"{A}: login email and password height"),
        "loginButton": dim("45.5px", f"{A}: Log In button height"),
        "icon": dim("24px", f"{A}: password visibility toggle"),
        "header": dim("80px", f"{M}: marketing header height"),
        "focus": dim("1px", f"{M}: focus-visible outline width on Log in"),
    },
    "layout": {
        "desktop": dim("1440px", f"{M}: capture viewport width"),
        "phone": dim("390px", "Phone capture viewport width, 390 CSS px at deviceScaleFactor 2"),
        "header": dim("80px", f"{M}: marketing header"),
    },
}

light = {
    "page": color("{color.page}", f"{M}: body background"),
    "surface": color("{color.white}", f"{B}: booking card; pricing cards sit on the page wash"),
    "text": color("{color.ink}", f"{M}: body and headings"),
    "textMuted": color("{color.searchPlaceholder}", f"{M}: Learning Center placeholder. Marketing has no separate muted body token"),
    "textOnAccent": color("{color.cream}", f"{M}: text on Try it now"),
    "link": color("{color.magenta}", f"{M}: Log in hover and Book a demo ink"),
    "accent": color("{color.magenta}", f"{M}: Try it now fill"),
    "accentHover": color("{color.magentaPressed}", f"{M}: Try it now hover fill"),
    "border": color("{color.ink}", f"{M}: text colour doubles as the hairline on FAQ and nav; no separate border token was painted on marketing"),
    "focus": color("{color.focus}", f"{M}: focus-visible outline"),
    "login": {
        "page": color("{color.ink}", f"{A}: login body background rgb(25, 30, 73)"),
        "field": color("{color.fieldWash}", f"{A}: email and password fill"),
        "fieldText": color("{color.fieldMuted}", f"{A}: field text and placeholder"),
        "button": color("{color.loginButton}", f"{A}: Log In fill"),
        "buttonHover": color("{color.loginButtonHover}", f"{A}: Log In hover"),
        "buttonText": color("{color.ink}", f"{A}: Log In label"),
    },
    "component": {
        "button": {
            "background": color("{color.magenta}", f"{M}: Try it now"),
            "text": color("{color.cream}", f"{M}: Try it now label"),
            "radius": dim("{radius.pill}", f"{M}: 48px pill"),
            "height": dim("{size.button}", f"{M}: 48px"),
        },
        "field": {
            "background": color("{color.fieldWash}", f"{A}: login email"),
            "text": color("{color.fieldMuted}", f"{A}: login email text"),
            "height": dim("{size.field}", f"{A}: 50px"),
        },
    },
}

doc = {
    "core": core,
    "light": light,
    "$themes": [{"id": "light", "name": "Light", "selectedTokenSets": {"core": "source", "light": "enabled"}}],
    "$metadata": {"tokenSetOrder": ["core", "light"]},
}

if MOTION:
    core["motion"], extra = motion_mod.build(MOTION)
    if extra:
        core["motion"].setdefault("$extensions", {})["notTokenised"] = extra



def tokens_of(tree, prefix=""):
    for k, v in tree.items():
        if k.startswith("$"):
            continue
        if isinstance(v, dict) and "$value" in v:
            yield prefix + k, v
        elif isinstance(v, dict):
            yield from tokens_of(v, prefix + k + ".")


def aliases(v):
    if isinstance(v, str):
        return re.findall(r"\{([^{}]+)\}", v)
    if isinstance(v, dict):
        return [a for x in v.values() for a in aliases(x)]
    if isinstance(v, list):
        return [a for x in v for a in aliases(x)]
    return []


MEMBER = {"fontFamily": "fontFamily", "fontSize": "dimension", "fontWeight": "fontWeight",
          "lineHeight": "dimension", "letterSpacing": "dimension", "duration": "duration",
          "delay": "duration", "timingFunction": "cubicBezier"}


def check(sets):
    """The kit's alias and type pass: every alias resolves in core or its own set and has the type its
    place needs, and every literal colour, dimension and weight is in a form DTCG reads."""
    core_names = dict(tokens_of(sets["core"]))
    for setname, tree in sets.items():
        names = dict(core_names)
        names.update(dict(tokens_of(tree)))
        for n, t in tokens_of(tree):
            v, ty = t["$value"], t.get("$type")
            if not ty:
                raise ValueError(f"{setname}.{n}: no $type")
            for a in aliases(v):
                if a not in names:
                    raise KeyError(f"{setname}.{n}: alias {{{a}}} points at nothing")
            # Readers resolve only a whole-string reference, and a loop resolves to nothing: refuse a
            # reference mixed into other text, and follow every chain to its literal.
            refs = [v] if isinstance(v, str) else [m for m in v.values() if isinstance(m, str)] if isinstance(v, dict) else []
            for r in refs:
                if aliases(r) and not re.fullmatch(r"\{[^{}]+\}", r):
                    raise ValueError(f"{setname}.{n}: {r!r} mixes a reference into other text")
                seen = {n}
                while isinstance(r, str) and re.fullmatch(r"\{[^{}]+\}", r):
                    target = r[1:-1]
                    if target in seen:
                        raise ValueError(f"{setname}.{n}: reference loop through {target}")
                    seen.add(target)
                    r = names[target]["$value"]
            if isinstance(v, str) and aliases(v) and ty in ("color", "dimension", "fontFamily", "fontWeight", "duration"):
                if names[aliases(v)[0]].get("$type") != ty:
                    raise TypeError(f"{setname}.{n}: alias {v} is a {names[aliases(v)[0]].get('$type')}, not a {ty}")
            if isinstance(v, dict):
                for k, want in MEMBER.items():
                    m = v.get(k)
                    if isinstance(m, str) and aliases(m) and names[aliases(m)[0]].get("$type") != want:
                        raise TypeError(f"{setname}.{n}: {k} {m} is not a {want}")
            if isinstance(v, str) and aliases(v):
                continue
            if ty == "dimension" and not re.fullmatch(r"-?\d*\.?\d+(px|rem)", str(v)):
                raise ValueError(f"{setname}.{n}: dimension {v!r} is not one px or rem length")
            if ty == "color" and not re.fullmatch(r"#[0-9a-f]{6}([0-9a-f]{2})?|rgba\(\d+, \d+, \d+, [\d.]+\)", str(v)):
                raise ValueError(f"{setname}.{n}: colour {v!r}")
            if ty == "fontWeight" and not isinstance(v, int):
                raise ValueError(f"{setname}.{n}: fontWeight {v!r} is not a number")


check({"core": core, "light": light})
TEXT = json.dumps(doc, indent=2) + "\n"

if __name__ == "__main__":
    (HERE / "tokens.json").write_text(TEXT)
    print("wrote", HERE / "tokens.json")
