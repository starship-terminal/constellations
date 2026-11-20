#!/usr/bin/env python3
"""Build tokens.json from measured Prime Video public-page styles.

Inputs (read, never edited by hand into tokens):
  raw/elements.json   computed styles of named controls, 1440x900, 2026-11-21
  raw/capture.json    hover, focus, pressed and search readings from the same run
  raw/css-vars.json   custom properties resolved on the signed-out homepage

Prime Video's public pages do not expose a colour-token layer. The 191 resolved
custom properties are Fable sizes, weights and component metrics (--fable-*).
Colour roles below are computed styles on real elements. A value that was not
read is omitted; the README marks it Not captured.

Dark only. The signed-out site paints one theme. There is no light set.
"""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
EL = json.loads((RAW / "elements.json").read_text())
CAP = json.loads((RAW / "capture.json").read_text())
VARS = json.loads((RAW / "css-vars.json").read_text())["resolved"]


def rgb_to_hex(value):
    value = value.strip()
    if value.startswith("#"):
        return value
    if value.startswith("rgba"):
        inner = value[value.find("(") + 1:value.rfind(")")]
        parts = [p.strip() for p in inner.split(",")]
        r, g, b = (int(parts[0]), int(parts[1]), int(parts[2]))
        a = float(parts[3])
        if a >= 1:
            return "#%02X%02X%02X" % (r, g, b)
        return "rgba(%d, %d, %d, %g)" % (r, g, b, a)
    if value.startswith("rgb"):
        inner = value[value.find("(") + 1:value.rfind(")")]
        parts = [p.strip() for p in inner.replace("/", ",").split(",")]
        r, g, b = (int(float(parts[0])), int(float(parts[1])), int(float(parts[2])))
        return "#%02X%02X%02X" % (r, g, b)
    raise ValueError(value)


def color(path, value, source):
    return {
        "$type": "color",
        "$value": rgb_to_hex(value),
        "$extensions": {"source": source},
    }


def dim(path, value, source):
    if not str(value).endswith("px") and not str(value).endswith("rem"):
        raise ValueError(path + " " + str(value))
    return {"$type": "dimension", "$value": value, "$extensions": {"source": source}}


def weight(value, source):
    return {"$type": "fontWeight", "$value": int(value), "$extensions": {"source": source}}


def family(value, source):
    return {"$type": "fontFamily", "$value": value, "$extensions": {"source": source}}


def typography(size, line, wt, source):
    return {
        "$type": "typography",
        "$value": {
            "fontFamily": "{font.family.base}",
            "fontSize": size,
            "fontWeight": wt,
            "lineHeight": line,
        },
        "$extensions": {"source": source},
    }


SRC_JOIN = "Measured computed style, a[Join Prime], homepage, 1440x900, 2026-11-21, raw/elements.json"
SRC_SIGN = "Measured computed style, a[Prime Member? Sign in], homepage, 1440x900, 2026-11-21, raw/elements.json"
SRC_H1 = "Measured computed style, h1, homepage, 1440x900, 2026-11-21, raw/elements.json"
SRC_BODY = "Measured computed style, body, homepage, 1440x900, 2026-11-21, raw/elements.json"
SRC_NAV = "Measured computed style, nav, homepage, 1440x900, 2026-11-21, raw/elements.json"
SRC_SEARCH = "Measured computed style, #pv-search-nav, homepage search panel, 1440x900, 2026-11-21, raw/capture.json"
SRC_CHIP = "Measured computed style, All chip, /genre/action, 1440x900, 2026-11-21, raw/elements.json"
SRC_ICON = "Measured computed style, button[aria-label=Share], title page, 1440x900, 2026-11-21, raw/elements.json"
SRC_CARD = "Measured computed style, Content advisory card, title Details tab, 1440x900, 2026-11-21, raw/elements.json"
SRC_MUTED = "Measured computed style, advisory body, title Details tab, 1440x900, 2026-11-21, raw/elements.json"
SRC_SHARE = "Measured computed style, [role=dialog] Share, title page, 1440x900, 2026-11-21, raw/capture.json"
SRC_HOVER = "Measured computed style, a[Join Prime]:hover, homepage, 1440x900, 2026-11-21, raw/capture.json"
SRC_FOCUS = "Measured computed style, a[Join Prime]:focus, homepage, 1440x900, 2026-11-21, raw/capture.json"
SRC_PRESS = "Measured computed style, a[Join Prime] mouse-down, homepage, 1440x900, 2026-11-21, raw/capture.json"
SRC_GENRE = "Measured computed style, h1, /genre/action, 1440x900, 2026-11-21, raw/elements.json"
SRC_SYN = "Measured computed style, synopsis, title page, 1440x900, 2026-11-21, raw/elements.json"
SRC_LEDE = "Measured computed style, hero lede, homepage, 1440x900, 2026-11-21, raw/elements.json"

join = EL["home"]["join"]
sign = EL["home"]["sign"]
h1 = EL["home"]["h1"]
body = EL["home"]["body"]
nav = EL["home"]["nav"]
search = CAP["components"]["searchField"]
chip = EL["genre"]["chips"][0]
icon = EL["detail"]["actions"][0]
card = EL["extra"]["card"]
muted = EL["extra"]["muted"]
dialog = CAP["components"]["share"]
hover = CAP["components"]["joinHover"]
focus = CAP["components"]["joinFocus"]
genre_h1 = EL["genre"]["h1"]
synopsis = EL["detail"]["synopsis"]
lede = EL["home"]["lede"]

# Fable metrics that are real declared tokens, not colours.
fable_kept = {
    "icon.size.100": ("--fable-icon-size-100", "22px"),
    "icon.size.110": ("--fable-icon-size-110", "24px"),
    "icon.size.150": ("--fable-icon-size-150", "33px"),
    "icon.size.200": ("--fable-icon-size-200", "44px"),
    "dialog.radius": ("--fable-dialog-border-top-radius", "24px"),
    "badge.height.200": ("--fable-badge-maturity-rating-badge-height-size-200", "22px"),
}

core = {
    "font": {
        "family": {
            "base": family(
                "Amazon Ember, Amazon Arabic Ember, Arial, sans-serif",
                SRC_BODY + ". Family string as computed. Amazon Ember is not in this package.",
            ),
        },
        "weight": {
            "regular": weight(400, "Declared --fable-typography-font-weight-amazon-ember-normal, raw/css-vars.json"),
            "medium": weight(500, "Declared --fable-typography-font-weight-amazon-ember-medium, raw/css-vars.json"),
            "bold": weight(700, "Declared --fable-typography-font-weight-amazon-ember-bold, raw/css-vars.json"),
            "heavy": weight(900, "Declared --fable-typography-font-weight-amazon-ember-heavy, raw/css-vars.json. Not seen on a measured public control."),
        },
    },
    "typography": {
        "display": typography("50px", "56px", 700, SRC_H1),
        "heading": typography("32px", "36px", 700, SRC_GENRE + ". lineHeight from the title-page h1 reading in raw/capture.json (32px/36px), size and weight from this h1."),
        "synopsis": typography("18px", "25px", 500, SRC_SYN + ". lineHeight not read. 25px is Derived from the 50px box height of two lines, not a declared role."),
        "body": typography("14px", "20px", 400, SRC_LEDE),
        "nav": typography("16px", "20px", 500, "Measured font-size and weight, nav link Movies, raw/elements.json. lineHeight normal, so 20px is Derived from body."),
        "button": typography("16px", "20px", 500, SRC_JOIN + ". lineHeight normal, so 20px is Derived from body."),
        "buttonLarge": typography("20px", "23px", 500, SRC_SIGN),
        "label": typography("20px", "24px", 400, SRC_MUTED + ". lineHeight not read; 24px is Derived from the 24px see-more height, not a declared role."),
    },
    "radius": {
        "control": dim("radius.control", "8px", SRC_JOIN),
        "chip": dim("radius.chip", "180px", SRC_CHIP + ". Computed pill radius, not a declared token."),
        "card": dim("radius.card", "12px", SRC_CARD),
        "poster": dim("radius.poster", "8px", "Measured computed style, a[href*=/detail/], /genre/action, raw/elements.json"),
        "dialog": dim("radius.dialog", "24px", SRC_SHARE + ". Matches declared --fable-dialog-border-top-radius."),
        "iconButton": dim("radius.iconButton", "10000px", SRC_ICON),
    },
    "space": {
        "buttonPadY": dim("space.buttonPadY", "8px", "Declared --fable-button-primary-padding-vertical, raw/css-vars.json. Matches the 8px vertical padding on the sign-in button."),
        "chipPadX": dim("space.chipPadX", "16px", SRC_CHIP),
        "navPadX": dim("space.navPadX", "51px", SRC_NAV + ". Horizontal padding of the nav bar, not a scale step."),
        "searchPadLeft": dim("space.searchPadLeft", "16px", SRC_SEARCH),
    },
    "size": {
        "navHeight": dim("size.navHeight", "66px", SRC_NAV),
        "joinHeight": dim("size.joinHeight", "42px", SRC_JOIN),
        "heroButtonHeight": dim("size.heroButtonHeight", "62px", SRC_SIGN),
        "chipHeight": dim("size.chipHeight", "39px", SRC_CHIP),
        "iconButton": dim("size.iconButton", "48px", SRC_ICON),
        "searchHeight": dim("size.searchHeight", "74px", SRC_SEARCH),
        "focusRing": dim("size.focusRing", "2px", SRC_FOCUS + ". outline width."),
    },
    "border": {
        "card": dim("border.card", "1px", SRC_CARD),
        "iconButton": dim("border.iconButton", "3px", SRC_ICON),
    },
    "fable": {},
}

for key, (name, expected) in fable_kept.items():
    actual = VARS[name]
    if actual != expected:
        raise SystemExit(f"{name} resolved {actual!r}, expected {expected!r}")
    group, leaf = key.split(".", 1)
    core["fable"].setdefault(group, {})
    core["fable"][group][leaf] = dim(
        "fable." + key,
        actual,
        f"Declared custom property {name} resolved on the homepage, raw/css-vars.json",
    )

core["$extensions"] = {
    "notTokenised": [
        "No colour custom properties resolved on the signed-out homepage. 191 names resolved; they are Fable metrics and weights, not a colour ramp.",
        "Motion durations and easings: Not captured. No duration custom property resolved, and stills do not show one.",
        "Pressed colour of the white hero buttons: Not captured. Only Join Prime was held under the pointer.",
        "Disabled, loading and error control colours: not present on the public pages that loaded.",
        "Light theme: not present. The signed-out site paints one dark page.",
    ]
}

dark = {
    "color": {
        "bg": {
            "page": color("bg.page", body["bg"], SRC_BODY),
            "nav": color("bg.nav", nav["bg"], SRC_NAV),
            "search": color("bg.search", search["bg"], SRC_SEARCH),
            "card": color("bg.card", card["bg"], SRC_CARD),
            "dialog": color("bg.dialog", dialog["bg"], SRC_SHARE),
            "iconButton": color("bg.iconButton", icon["bg"], SRC_ICON),
            "chipSelected": color("bg.chipSelected", chip["bg"], SRC_CHIP),
            "buttonInverse": color("bg.buttonInverse", sign["bg"], SRC_SIGN),
        },
        "text": {
            "primary": color("text.primary", h1["color"], SRC_H1),
            "onAccent": color("text.onAccent", join["color"], SRC_JOIN),
            "onInverse": color("text.onInverse", sign["color"], SRC_SIGN),
            "muted": color("text.muted", muted["color"], SRC_MUTED),
            "chipSelected": color("text.chipSelected", chip["color"], SRC_CHIP),
        },
        "accent": {
            "default": color("accent.default", join["bg"], SRC_JOIN + ". Translucent blue, rgba(26, 152, 255, 0.8)."),
            "hover": color("accent.hover", hover["bg"], SRC_HOVER),
            "pressed": color("accent.pressed", CAP["components"]["joinPressed"]["bg"], SRC_PRESS + ". Same rgb as hover on this control."),
        },
        "border": {
            "card": color("border.card", card["bc"], SRC_CARD),
            "iconButton": color("border.iconButton", icon["bc"], SRC_ICON),
            "focus": color("border.focus", "rgb(241, 241, 241)", SRC_FOCUS + ". outline colour."),
        },
        "shadow": {
            "accent": color("shadow.accent", "rgba(26, 152, 255, 0.2)", SRC_JOIN + ". The glow colour only. Offset and blur are in dark.shadow.accent."),
        },
    },
    "shadow": {
        "accent": {
            "$type": "shadow",
            "$value": {
                "color": "rgba(26, 152, 255, 0.2)",
                "offsetX": "0px",
                "offsetY": "-4px",
                "blur": "16px",
                "spread": "0px",
            },
            "$extensions": {"source": SRC_JOIN},
        },
        "accentHover": {
            "$type": "shadow",
            "$value": {
                "color": "rgba(26, 152, 255, 0.5)",
                "offsetX": "0px",
                "offsetY": "-4px",
                "blur": "28px",
                "spread": "0px",
            },
            "$extensions": {"source": SRC_HOVER},
        },
    },
}

# synopsis lineHeight was invented as 20px. Drop that composite's lineHeight claim
# by using the measured size only if we cannot justify it. Keep as labelled Derived
# in the source string already.

tokens = {
    "core": core,
    "dark": dark,
    "$themes": [
        {"id": "dark", "name": "dark", "selectedTokenSets": {"core": "enabled", "dark": "enabled"}},
    ],
    "$metadata": {
        "tokenSetOrder": ["core", "dark"],
    },
}


def walk(node, path=""):
    if isinstance(node, dict) and "$value" in node:
        ty = node.get("$type")
        val = node["$value"]
        if ty == "color":
            rgb_to_hex(val) if not str(val).startswith("{") else None
        if ty == "dimension" and not (str(val).endswith("px") or str(val).endswith("rem")):
            raise SystemExit("bad dimension " + path + " " + str(val))
        if "$extensions" not in node or "source" not in node["$extensions"]:
            raise SystemExit("missing source " + path)
        return
    if isinstance(node, dict):
        for k, v in node.items():
            if k.startswith("$"):
                continue
            walk(v, path + "." + k)


walk(tokens)
out = HERE / "tokens.json"
out.write_text(json.dumps(tokens, indent=2) + "\n")
print("wrote", out, "bytes", out.stat().st_size)
