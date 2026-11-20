#!/usr/bin/env python3
"""Build tokens.json from ROVR's live readings.

Sources, read from www.rovr.live on 2026-11-21, signed out, dark theme:
  raw/components-computed.json  roles.painted: each shadcn token as the live
                                page computed it (hsl() on a probe element),
                                plus component computed styles
  raw/css-vars.json             declared custom properties. The stylesheet
                                harvest resolved those names on a blank probe,
                                which does not carry the .dark class, so those
                                resolved values are the light defaults. The
                                painted dark values come from the live page.

ROVR paints one dark theme (html.dark, color-scheme: dark). No light set is
emitted. Unread values stay out of the file.
"""
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
C = json.loads((RAW / "components-computed.json").read_text())
PAINTED = C["roles"]["painted"]


def rgb_to_hex(v):
    v = v.strip()
    m = re.fullmatch(r"rgb\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*\)", v)
    if m:
        return "#%02x%02x%02x" % tuple(int(x) for x in m.groups())
    m = re.fullmatch(r"rgba\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*,\s*([\d.]+)\s*\)", v)
    if m:
        r, g, b, a = m.groups()
        a = float(a)
        if a == 1:
            return "#%02x%02x%02x" % (int(r), int(g), int(b))
        return "rgba(%s, %s, %s, %g)" % (r, g, b, a)
    if re.fullmatch(r"#[0-9a-fA-F]{6}", v):
        return v.lower()
    raise ValueError("not a colour: " + v)


def color(path, value, source):
    return {"$value": rgb_to_hex(value), "$type": "color", "$extensions": {"source": source}}


def dim(path, value, source):
    if not re.fullmatch(r"-?\d+(\.\d+)?(px|rem)", str(value)):
        raise ValueError(f"{path}: dimension {value!r}")
    return {"$value": value, "$type": "dimension", "$extensions": {"source": source}}


def num(value, source, ty="number"):
    return {"$value": value, "$type": ty, "$extensions": {"source": source}}


def font_family(value, source):
    return {"$value": value, "$type": "fontFamily", "$extensions": {"source": source}}


def typography(font_family, size, weight, line_height, style, source, letter_spacing=None, text_case=None):
    val = {
        "fontFamily": font_family,
        "fontSize": size,
        "fontWeight": weight,
        "lineHeight": line_height,
        "fontStyle": style,
    }
    if letter_spacing:
        val["letterSpacing"] = letter_spacing
    if text_case:
        val["textCase"] = text_case
    return {"$value": val, "$type": "typography", "$extensions": {"source": source}}


def role(name):
    rec = PAINTED["--" + name]
    return color(
        name,
        rec["painted"],
        f"measured html.dark computed --{name} ({rec['raw']}) painted {rec['painted']} on https://www.rovr.live/ 2026-11-21",
    )


def comp(key, state="default"):
    st = C["components"][key]["states"][state]
    if "error" in st or st.get("missing"):
        raise KeyError(key)
    return st


src_kern = "measured computed fontFamily on body, https://www.rovr.live/ 2026-11-21; declared --font-kern-standard"
src_gt = "declared --font-gt-alpina in raw/css-vars.json; not read on a captured element"
src_roboto = "declared --font-roboto in raw/css-vars.json; @font-face present; not read on a captured element"

menu = comp("menu-button")
play = comp("play-button")
nav = comp("nav-link")
title = comp("display-title")
curator = comp("curator-name")
footer = comp("footer-link")
field = comp("text-field")
signin = comp("sign-in-button")
tab = comp("tab")
quick = comp("quick-menu")
manifesto = comp("manifesto")
search = comp("search-field")

kern = "kernStandard, kernStandard Fallback, system-ui, sans-serif"

core = {
    "color": {
        "brand": {
            "yellow": color("brand.yellow", menu["backgroundColor"], "measured menu-button default backgroundColor, home 1440"),
            "yellow-hover": color("brand.yellow-hover", menu["states"]["hover"]["backgroundColor"] if False else C["components"]["menu-button"]["states"]["hover"]["backgroundColor"], "measured menu-button hover backgroundColor"),
            "ink": color("brand.ink", menu["color"], "measured menu-button default color"),
            "paper": color("brand.paper", C["roles"]["body"]["color"], "measured body color"),
            "page": color("brand.page", C["roles"]["body"]["backgroundColor"], "measured body backgroundColor"),
            "nav-quiet": color("brand.nav-quiet", nav["color"], "measured nav-link default color"),
        },
        "status": {
            "error-text": {
                "$value": "#e60000",
                "$type": "color",
                "$extensions": {"source": "css-var --error-text hsl(360, 100%, 45%) in raw/css-vars.json; not painted on a captured public control"},
            },
            "success-text": {
                "$value": "#008a1f",
                "$type": "color",
                "$extensions": {"source": "Derived from declared --success-text hsl(140, 100%, 27%); not painted on a captured public control"},
            },
            "info-text": {
                "$value": "#0955db",
                "$type": "color",
                "$extensions": {"source": "Derived from declared --info-text hsl(210, 92%, 45%); not painted on a captured public control"},
            },
            "warning-text": {
                "$value": "#dc6b09",
                "$type": "color",
                "$extensions": {"source": "Derived from declared --warning-text hsl(31, 92%, 45%); not painted on a captured public control"},
            },
        },
    },
    "font": {
        "family": {
            "display": font_family(kern, src_kern),
            "body": font_family(kern, src_kern),
            "gt-alpina": font_family("gtAlpina, gtAlpina Fallback", src_gt),
            "roboto": font_family("Roboto, Roboto Fallback", src_roboto),
        }
    },
    "typography": {
        "display": typography("{core.font.family.display}", "51px", 700, "53.55px", "normal", "measured display-title default on home", text_case="uppercase"),
        "manifesto": typography("{core.font.family.display}", "72px", 800, "72px", "normal", "measured manifesto default on /about"),
        "curator": typography("{core.font.family.display}", "40.8px", 400, "44.88px", "normal", "measured curator-name default on home"),
        "nav": typography("{core.font.family.body}", "15px", 400, "22.5px", "italic", "measured nav-link default"),
        "button": typography("{core.font.family.body}", "15px", 700, "15px", "italic", "measured menu-button default"),
        "body": typography("{core.font.family.body}", "16px", 400, "24px", "normal", "measured body fontSize and play-button lineHeight"),
        "label": typography("{core.font.family.body}", "14px", 700, "20px", "normal", "measured archive tab default"),
        "caption": typography("{core.font.family.body}", "10px", 400, "15px", "normal", "measured footer-link default"),
        "field": typography("{core.font.family.body}", "14px", 400, "20px", "normal", "measured sign-in email field; field was not filled"),
    },
    "radius": {
        "none": dim("radius.none", "0px", "measured nav-link and sign-in button borderRadius"),
        "pill": dim("radius.pill", "30px", "measured menu-button borderRadius"),
        "full": dim("radius.full", "9999px", "measured play-button and quick-menu borderRadius"),
        "shadcn": dim("radius.shadcn", "8px", "declared --radius .5rem, resolved 8px in raw/css-vars.json; not the radius the chrome paints"),
    },
    "spacing": {
        "tab-x": dim("spacing.tab-x", "16px", "measured archive tab paddingLeft"),
        "control-40": dim("spacing.control-40", "40px", "measured quick-menu width and height"),
        "play": dim("spacing.play", "70px", "measured play-button width and height"),
    },
    "border": {
        "hairline": dim("border.hairline", "1px", "measured archive tab borderTopWidth"),
        "ring": dim("border.ring", "2px", "measured quick-menu borderTopWidth"),
    },
}

# Status colours above were hand-converted. Replace with exact hsl conversion
# so the file does not carry a guessed hex. Compute from the declared hsl.

def hsl_to_hex(h, s, l):
    s, l = s / 100, l / 100
    c = (1 - abs(2 * l - 1)) * s
    x = c * (1 - abs((h / 60) % 2 - 1))
    m = l - c / 2
    if h < 60: r, g, b = c, x, 0
    elif h < 120: r, g, b = x, c, 0
    elif h < 180: r, g, b = 0, c, x
    elif h < 240: r, g, b = 0, x, c
    elif h < 300: r, g, b = x, 0, c
    else: r, g, b = c, 0, x
    return "#%02x%02x%02x" % tuple(round((n + m) * 255) for n in (r, g, b))


status_src = {
    "error-text": (360, 100, 45, "--error-text"),
    "success-text": (140, 100, 27, "--success-text"),
    "info-text": (210, 92, 45, "--info-text"),
    "warning-text": (31, 92, 45, "--warning-text"),
}
for name, (h, s, l, var) in status_src.items():
    core["color"]["status"][name] = {
        "$value": hsl_to_hex(h % 360, s, l),
        "$type": "color",
        "$extensions": {"source": f"Derived from declared {var} hsl({h}, {s}%, {l}%) in raw/css-vars.json; not painted on a captured public control"},
    }

dark = {
    "page": {"$value": "{core.color.brand.page}", "$type": "color", "$extensions": {"source": "alias of measured body background"}},
    "surface": role("card"),
    "text": {"$value": "{core.color.brand.paper}", "$type": "color", "$extensions": {"source": "alias of measured body color"}},
    "muted": role("muted-foreground"),
    "accent": {"$value": "{core.color.brand.yellow}", "$type": "color", "$extensions": {"source": "alias of measured menu-button fill; painted yellow, not the --primary probe"}},
    "border": role("border"),
    "primary": role("primary"),
    "primary-foreground": role("primary-foreground"),
    "secondary": role("secondary"),
    "destructive": role("destructive"),
    "ring": role("ring"),
    "popover": role("popover"),
    "input": role("input"),
    "focus": {
        "ring": role("ring"),
    },
    "component": {
        "button": {
            "bg": {"$value": "{core.color.brand.yellow}", "$type": "color", "$extensions": {"source": "measured menu-button backgroundColor"}},
            "text": {"$value": "{core.color.brand.ink}", "$type": "color", "$extensions": {"source": "measured menu-button color"}},
            "radius": {"$value": "{core.radius.pill}", "$type": "dimension", "$extensions": {"source": "measured menu-button borderRadius"}},
            "height": dim("component.button.height", "24px", "measured menu-button height"),
        },
        "play": {
            "bg": {"$value": "{core.color.brand.yellow}", "$type": "color", "$extensions": {"source": "measured play-button backgroundColor"}},
            "size": dim("component.play.size", "70px", "measured play-button width"),
            "radius": {"$value": "{core.radius.full}", "$type": "dimension", "$extensions": {"source": "measured play-button borderRadius"}},
        },
        "field": {
            "text": color("field.text", field["color"], "measured sign-in email field color; field not filled"),
            "size": dim("component.field.size", "14px", "measured sign-in email field fontSize"),
            "height": dim("component.field.height", "20px", "measured sign-in email field height"),
        },
        "tab": {
            "bg": color("tab.bg", tab["backgroundColor"], "measured archive Shows tab backgroundColor"),
            "text": color("tab.text", tab["color"], "measured archive Shows tab color"),
            "height": dim("component.tab.height", "40px", "measured archive Shows tab height"),
        },
    },
}

tokens = {
    "core": core,
    "dark": dark,
    "$themes": [{
        "id": "dark",
        "name": "Dark",
        "selectedTokenSets": {"core": "source", "dark": "enabled"},
        "$description": "The only theme www.rovr.live paints. html carries class dark and color-scheme dark.",
    }],
    "$metadata": {"tokenSetOrder": ["core", "dark"]},
}

# alias check
def walk(tree, prefix=""):
    for k, v in tree.items():
        if isinstance(v, dict) and "$value" in v:
            yield prefix + k, v
        elif isinstance(v, dict):
            yield from walk(v, prefix + k + ".")

names = {n for n, _ in walk(core)} | {"core." + n for n, _ in walk(core)} | {n for n, _ in walk(dark)}
for n, t in list(walk(core)) + list(walk(dark)):
    for a in re.findall(r"\{([^{}]+)\}", json.dumps(t["$value"])):
        if a not in names and a.removeprefix("core.") not in names:
            raise SystemExit(f"missing alias {a} from {n}")

(HERE / "tokens.json").write_text(json.dumps(tokens, indent=2) + "\n")
print("wrote tokens", len(list(walk(core))), "core", len(list(walk(dark))), "dark")
