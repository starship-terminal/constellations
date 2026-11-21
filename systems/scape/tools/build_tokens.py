#!/usr/bin/env python3
"""Build systems/scape/tokens.json from the public CSS of scape.com.

Values are the :root custom properties in the Next.js stylesheets captured
on 2026-11-21 (raw/css-vars.json) and computed styles on the live pages
(raw/computed.json). Unread roles stay Not captured. There is no dark theme.
"""
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
VARS = json.loads((RAW / "css-vars.json").read_text())
COMPUTED = json.loads((RAW / "computed.json").read_text())

CSS = "declared on :root in scape.com Next.js stylesheets (raw/css-vars.json), captured 2026-11-21"
COMP = "computed style on the live public page (raw/computed.json), captured 2026-11-21"


def norm_color(v):
    v = v.strip().lower()
    m = re.fullmatch(r"#([0-9a-f]{3,8})", v)
    if m:
        h = m.group(1)
        if len(h) in (3, 4):
            h = "".join(c * 2 for c in h)
        if len(h) == 8 and h[6:] == "ff":
            h = h[:6]
        if len(h) == 6:
            return "#" + h
        raise ValueError("not a solid colour: " + v)
    m = re.fullmatch(r"rgba?\(\s*(\d+)[,\s]+(\d+)[,\s]+(\d+)(?:\s*[,/]\s*([\d.]+))?\s*\)", v)
    if m:
        r, g, b, a = m.groups()
        a = float(a) if a is not None else 1
        if a >= 1:
            return "#%02x%02x%02x" % (int(r), int(g), int(b))
        return "rgba(%d, %d, %d, %s)" % (int(r), int(g), int(b), "%g" % round(a, 3))
    m = re.fullmatch(r"hsla?\(\s*([\d.]+)[,\s]+([\d.]+)%[,\s]+([\d.]+)%(?:\s*[,/]\s*([\d.]+))?\s*\)", v)
    if m:
        H, S, L, a = m.groups()
        a = float(a) if a is not None else 1
        return hsla_to_css(float(H), float(S) / 100, float(L) / 100, a)
    raise ValueError("not a colour: " + v)


def hsla_to_css(h, s, l, a):
    c = (1 - abs(2 * l - 1)) * s
    hp = (h % 360) / 60
    x = c * (1 - abs(hp % 2 - 1))
    if hp < 1:
        r, g, b = c, x, 0
    elif hp < 2:
        r, g, b = x, c, 0
    elif hp < 3:
        r, g, b = 0, c, x
    elif hp < 4:
        r, g, b = 0, x, c
    elif hp < 5:
        r, g, b = x, 0, c
    else:
        r, g, b = c, 0, x
    m = l - c / 2
    rgb = [round((ch + m) * 255) for ch in (r, g, b)]
    if a >= 1:
        return "#%02x%02x%02x" % tuple(rgb)
    return "rgba(%d, %d, %d, %s)" % (*rgb, "%g" % round(a, 3))


def color(name, source=CSS, description=""):
    raw = VARS[name]
    val = norm_color(raw) if not raw.startswith("var(") else None
    if val is None:
        raise ValueError(name + " is an alias: " + raw)
    token = {"$value": val, "$type": "color", "$extensions": {"source": f"Measured. {source}. Custom property {name}: {raw}"}}
    if description:
        token["$description"] = description
    return token


def dim(value, source, description=""):
    if not re.fullmatch(r"-?\d+(\.\d+)?(px|rem)", str(value)):
        raise ValueError("dimension " + str(value))
    token = {"$value": value, "$type": "dimension", "$extensions": {"source": source}}
    if description:
        token["$description"] = description
    return token


def alias(path, source, description=""):
    token = {"$value": "{" + path + "}", "$type": "color", "$extensions": {"source": source}}
    if description:
        token["$description"] = description
    return token


def other(value, ty, source, description=""):
    token = {"$value": value, "$type": ty, "$extensions": {"source": source}}
    if description:
        token["$description"] = description
    return token


body = COMPUTED["home"]["body"]
h1 = COMPUTED["home"]["h1"]
h2 = COMPUTED["home"]["h2"]
button = COMPUTED["home"]["findRoom"]
nav = COMPUTED["home"]["nav"]

core = {
    "$description": "Primitives read from scape.com :root custom properties and computed styles. One light theme.",
    "color": {
        "black": color("--scape-black", description="Named black. Also the value of --primary."),
        "white": color("--scape-white", description="The page cream. Named white in the product tokens, not #fff."),
        "paper": color("--white", description="Plain white, used as a solid header ground."),
        "ink": {
            "$value": "#212529",
            "$type": "color",
            "$extensions": {"source": f"Measured. {COMP}. body color {body['color']}. The stylesheet writes color:#212529 once; it is not a --scape-* custom property."},
            "$description": "Body text. Bootstrap-adjacent ink, not the named black.",
        },
        "darkGrey": color("--scape-dark-grey"),
        "lightGrey": color("--scape-light-grey"),
        "darkWhite": color("--scape-dark-white"),
        "card": color("--scape-card-bg"),
        "pink": color("--scape-pink", description="The brand pink. Solid header logo colour."),
        "red": color("--scape-red"),
        "darkRed": color("--scape-dark-red", description="Promo-strip text colour."),
        "green": color("--scape-green"),
        "darkGreen": color("--scape-dark-green"),
        "brightGreen": color("--scape-bright-green"),
        "turquoise": color("--scape-turquoise"),
        "purple": color("--scape-purple"),
        "darkPurple": color("--scape-dark-purple"),
        "lightPurple": color("--scape-light-purple"),
        "lightPink": color("--scape-light-pink"),
        "brightBlue": color("--scape-bright-blue"),
        "lightBlue": color("--scape-light-blue"),
        "brightOrange": color("--scape-bright-orange"),
        "brightYellow": color("--scape-bright-yellow"),
        "lightYellow": color("--scape-light-yellow"),
        "tintBlack16": color("--scape-tints-black-16"),
        "tintBlack20": color("--scape-tints-black-20"),
        "tintBlack50": color("--scape-tints-black-50"),
        "tintBlack80": color("--scape-tints-black-80"),
        "tintWhite50": color("--scape-tints-white-50"),
        "tintWhite80": color("--scape-tints-white-80"),
        "darkRedTint50": color("--scape-dark-red-tint-50"),
        "darkGreenTint50": color("--scape-dark-green-tint-50"),
        "darkPurpleTint50": color("--scape-dark-purple-tint-50"),
        "lightBlueTint50": color("--scape-light-blue-tint-50"),
        "lightGreenTint50": color("--scape-light-green-tint-50"),
        "lightPinkTint50": color("--scape-light-pink-tint-50"),
    },
    "font": {
        "family": {
            "sans": other(
                "Visuelt, Arial, sans-serif",
                "fontFamily",
                f"Measured. {COMP}. body fontFamily {body['font']}. @font-face declares Visuelt at 400, 500 and 700. Proprietary; the guide falls back to Arial.",
            ),
            "display": other(
                "GrotzecCondensed, Inter, sans-serif",
                "fontFamily",
                f"Measured. {COMP}. h1 fontFamily {h1['font']}. :root --richtext-heading-font-family is \"GrotzecCondensed\",Inter. @font-face declares GrotzecCondensed at 700. Proprietary.",
            ),
        }
    },
    "typography": {
        "display": other(
            {"fontFamily": "{font.family.display}", "fontSize": h2["size"], "fontWeight": int(h2["weight"]), "lineHeight": h2["lh"], "letterSpacing": "0px"},
            "typography",
            f"Measured. {COMP}. Home h2 'STUDENT LIVING LIKE NO OTHER' is {h2['size']} / {h2['lh']} / {h2['weight']}, text-transform {h2['tt']}.",
        ),
        "heading": other(
            {"fontFamily": "{font.family.display}", "fontSize": h1["size"], "fontWeight": int(h1["weight"]), "lineHeight": h1["lh"], "letterSpacing": "0px"},
            "typography",
            f"Measured. {COMP}. Home h1 'QUICK QUESTIONS' is {h1['size']} / {h1['lh']} / {h1['weight']}, text-transform {h1['tt']}.",
        ),
        "body": other(
            {"fontFamily": "{font.family.sans}", "fontSize": body["size"], "fontWeight": int(body["weight"]), "lineHeight": body["lh"], "letterSpacing": "0px"},
            "typography",
            f"Measured. {COMP}. body is {body['size']} / {body['lh']} / {body['weight']}.",
        ),
        "label": other(
            {"fontFamily": "{font.family.sans}", "fontSize": button["size"], "fontWeight": int(button["weight"]), "lineHeight": button["lh"], "letterSpacing": "0px"},
            "typography",
            f"Measured. {COMP}. FIND A ROOM is {button['size']} / {button['lh']}, text-transform {button['tt']}. :root --button-primary-font-size is 14px.",
        ),
        "nav": other(
            {"fontFamily": "{font.family.sans}", "fontSize": nav["size"], "fontWeight": int(nav["weight"]), "lineHeight": nav["lh"], "letterSpacing": "0px"},
            "typography",
            f"Measured. {COMP}. Header nav link is {nav['size']} / {nav['lh']}.",
        ),
    },
    "space": {
        "xs": dim(VARS["--spacing-xs"], f"Measured. {CSS}. --spacing-xs"),
        "s": dim(VARS["--spacing-s"], f"Measured. {CSS}. --spacing-s"),
        "base": dim(VARS["--spacing-base"], f"Measured. {CSS}. --spacing-base"),
        "m": dim(VARS["--spacing-m"], f"Measured. {CSS}. --spacing-m"),
        "l": dim(VARS["--spacing-l"], f"Measured. {CSS}. --spacing-l"),
        "xl": dim(VARS["--spacing-xl"], f"Measured. {CSS}. --spacing-xl"),
        "2xl": dim(VARS["--spacing-2xl"], f"Measured. {CSS}. --spacing-2xl"),
    },
    "radius": {
        "none": dim("0px", f"Measured. {COMP}. body and headings border-radius {body['radius']}."),
        "tab": dim(VARS["--button-tab-radius"], f"Measured. {CSS}. --button-tab-radius"),
        "field": dim(VARS["--form-input-border-radius"], f"Measured. {CSS}. --form-input-border-radius"),
        "pill": dim(VARS["--button-primary-radius"], f"Measured. {CSS}. --button-primary-radius. FIND A ROOM computed radius {button['radius']}."),
    },
    "size": {
        "button": dim(VARS["--button-height"], f"Measured. {CSS}. --button-height. FIND A ROOM computed height {button['h']}px."),
        "icon": dim(VARS["--icon-height"], f"Measured. {CSS}. --icon-height and --icon-width."),
        "header": dim(VARS["--header-height"], f"Measured. {CSS}. --header-height."),
        "banner": dim(VARS["--banner-height"], f"Measured. {CSS}. --banner-height."),
        "focusOffset": dim(VARS["--pex-focus-offset"], f"Measured. {CSS}. --pex-focus-offset."),
    },
    "border": {
        "width": dim("1px", f"Measured. {CSS}. --button-primary-border-width and --accordion-trigger-border-top-width are 1px."),
    },
    "shadow": {
        "card": other(VARS["--scape-card-shadow"], "shadow", f"Measured. {CSS}. --scape-card-shadow"),
        "cardHover": other(VARS["--scape-card-shadow-hover"], "shadow", f"Measured. {CSS}. --scape-card-shadow-hover"),
    },
    "motion": {
        "card": other("300ms", "duration", f"Derived. {CSS}. --card-transition is 'ease all 0.3s', converted to ms."),
        "easing": other("cubic-bezier(0.22, 1, 0.36, 1)", "cubicBezier", f"Measured. Stylesheet cubic-bezier(.22,1,.36,1), one of three curves in the public CSS. Not a named token."),
    },
    "layout": {
        "page": dim(VARS["--design-desktop-breakpoint"], f"Measured. {CSS}. --design-desktop-breakpoint. Capture viewport was 1440."),
        "mobile": dim(VARS["--mobile-max-breakpoint"], f"Measured. {CSS}. --mobile-max-breakpoint. Phone capture viewport was 390, inside this max."),
        "tablet": dim(VARS["--tablet-min-breakpoint"], f"Measured. {CSS}. --tablet-min-breakpoint."),
        "desktop": dim(VARS["--desktop-min-breakpoint"], f"Measured. {CSS}. --desktop-min-breakpoint."),
        "content": dim(VARS["--pex-container-width"], f"Measured. {CSS}. --pex-container-width."),
    },
}

light = {
    "$description": "The only theme the public site paints. No dark switch was found.",
    "background": {
        "page": alias("color.white", f"Measured. {CSS}. --secondary is #fef5f0, the same value as --scape-white. Body computed background {body['bg']}."),
        "surface": alias("color.card", f"Measured. {CSS}. --scape-card-bg."),
        "raised": alias("color.paper", f"Measured. {CSS}. --header-solid-header-bg is var(--scape-white) in the product naming, but the solid header token --white is #fff. Recorded as the solid paper."),
        "overlay": alias("color.tintBlack16", f"Measured. {CSS}. --header-transparent-dark-header-bg. Header computed background on the home hero."),
        "scrim": alias("color.tintBlack50", f"Measured. {CSS}. --scape-tints-black-50. Used as a tint, not observed as a modal scrim colour in this capture."),
    },
    "text": {
        "primary": alias("color.ink", f"Measured. {COMP}. body and card text {body['color']}."),
        "secondary": alias("color.darkGrey", f"Measured. {CSS}. --scape-dark-grey. Not read as a dedicated muted text role on a labelled element; the named grey is the closest published step."),
        "muted": alias("color.darkGrey", f"Measured. {CSS}. Same published grey as text.secondary. No separate muted text colour was painted on a labelled element."),
        "disabled": {
            "$value": "Not captured",
            "$type": "other",
            "$extensions": {"source": "Not captured. No disabled control was on the public pages."},
        },
        "onAccent": alias("color.white", f"Measured. {CSS}. --button-secondary-color is var(--scape-white)."),
        "link": alias("color.pink", f"Measured. {COMP}. Footer logo link computed color rgb(236, 108, 231), which is --scape-pink. --link-color aliases --primary (black) and was not the colour painted on that link."),
        "onDark": alias("color.white", f"Measured. {COMP}. Footer text {COMPUTED['home']['footer']['color']} and transparent-header nav {nav['color']}."),
    },
    "border": {
        "default": alias("color.tintBlack20", f"Measured. {CSS}. --accordion-trigger-border-top-color and --form-input-border-* use --scape-tints-black-20. Filter chips computed border rgba(0,0,0,0.2)."),
        "strong": alias("color.black", f"Measured. {CSS}. --button-primary-border-color and --form-input-border-*-focus use --scape-black."),
        "focus": alias("color.black", f"Measured. {CSS}. --pex-focus-outline is '1px dashed var(--scape-black)'."),
    },
    "accent": {
        "default": alias("color.pink", f"Measured. {CSS}. --header-solid-logo-color is var(--scape-pink)."),
        "hover": {
            "$value": "Not captured",
            "$type": "other",
            "$extensions": {"source": "Not captured. Dispatching mouseenter on FIND A ROOM did not change its computed background. --button-primary-background-hover is transparent."},
        },
        "pressed": {
            "$value": "Not captured",
            "$type": "other",
            "$extensions": {"source": "Not captured. --button-primary-background-active is transparent. A pressed fill was not read."},
        },
    },
    "status": {
        "success": alias("color.brightGreen", f"Measured as a palette step only. {CSS}. --scape-bright-green. Not observed on a success message."),
        "warning": alias("color.brightOrange", f"Measured as a palette step only. {CSS}. --scape-bright-orange. Not observed on a warning."),
        "danger": alias("color.red", f"Measured as a palette step only. {CSS}. --scape-red. Not observed on an error."),
        "info": alias("color.brightBlue", f"Measured as a palette step only. {CSS}. --scape-bright-blue. Not observed on an info message."),
    },
    "action": {
        "primary": {
            "background": alias("color.white", f"Measured. {COMP}. FIND A ROOM background {button['bg']}."),
            "text": alias("color.black", f"Measured. {COMP}. FIND A ROOM color {button['color']}."),
            "radius": dim(button["radius"], f"Measured. {COMP}. FIND A ROOM border-radius."),
        },
        "secondary": {
            "background": alias("color.black", f"Measured. {CSS}. --button-secondary-background is var(--primary), and --primary is #000."),
            "text": alias("color.white", f"Measured. {CSS}. --button-secondary-color is var(--scape-white)."),
        },
    },
    "focus": {
        "ring": other(VARS["--pex-focus-outline"], "other", f"Measured. {CSS}. --pex-focus-outline. Offset is --pex-focus-offset {VARS['--pex-focus-offset']}."),
    },
}

# fix status/disabled types: catalog and DESIGN.md want colours. Keep Not captured as other.
# action radius is a dimension inside a colour-ish group; that is fine if typed dimension.

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from token_checks import alias_errors  # noqa: E402

errors = alias_errors(core, light, {})
if errors:
    raise SystemExit("\n".join(errors))

tokens = {
    "core": core,
    "light": light,
    "$themes": [{
        "id": "light",
        "name": "Light",
        "selectedTokenSets": {"core": "source", "light": "enabled"},
        "$description": "The only theme scape.com paints on the public site.",
    }],
    "$metadata": {"tokenSetOrder": ["core", "light"]},
}
(HERE / "tokens.json").write_text(json.dumps(tokens, indent=1, ensure_ascii=False) + "\n")


def count(d):
    return sum(1 if isinstance(v, dict) and "$value" in v else count(v) if isinstance(v, dict) else 0 for v in d.values())


print(f"tokens.json: core {count(core)} + light {count(light)}")
