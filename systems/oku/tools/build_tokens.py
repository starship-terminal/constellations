#!/usr/bin/env python3
"""Build tokens.json from the public Oku readings.

Oku declares no design-token custom properties of its own. The --toastify-* and
--swiper-* names in the stylesheets belong to vendors and are not tokenised.
Every value here is a computed style read on oku.club on 2026-11-21, signed out,
in headless Chromium, light and dark (prefers-color-scheme). Sources name the
reading. A value that was not read is absent, never filled in.

Deterministic: same inputs, byte-identical output. Edit the readings, never tokens.json.
"""
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
READ = json.loads((RAW / "capture-readings.json").read_text())
COMP = json.loads((RAW / "components-computed.json").read_text())

INTER = 'Inter, -apple-system, "system-ui", "Segoe UI", Helvetica, Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol"'
SERIF = 'FabricSerifWeb, Georgia, Cambria, "Times New Roman", Times, serif'


def color(v):
    v = v.strip().lower()
    m = re.fullmatch(r"rgba?\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)(?:\s*,\s*([\d.]+))?\s*\)", v)
    if not m:
        raise ValueError("not a colour: " + v)
    r, g, b, a = m.groups()
    if a is None or float(a) == 1:
        return "#%02x%02x%02x" % (int(r), int(g), int(b))
    return "rgba(%s, %s, %s, %g)" % (r, g, b, float(a))


def dim(v):
    if isinstance(v, (int, float)):
        return "%gpx" % v
    m = re.fullmatch(r"(-?\d+(?:\.\d+)?)px", str(v).strip())
    if not m:
        raise ValueError("not a px length: " + str(v))
    return "%gpx" % float(m.group(1))


def leaf(ty, val, source, description=None):
    if ty == "color":
        val = color(val) if str(val).startswith("rgb") else val
    if ty == "dimension":
        val = dim(val)
    if ty == "fontWeight":
        val = int(val)
    token = {"$value": val, "$type": ty, "$extensions": {"source": source}}
    if description:
        token["$description"] = description
    return token


def border_color(css):
    m = re.search(r"rgba?\([^)]+\)", css)
    if not m:
        raise ValueError("no colour in border: " + css)
    return m.group(0)


def shadow(css, source):
    """One measured box-shadow layer. Inset layers are dropped; the first outer layer is kept."""
    # rgba(0, 0, 0, 0.25) 0px 4px 4px -5px
    layers = re.findall(r"(?:inset\s+)?rgba?\([^)]+\)\s+-?\d+(?:\.\d+)?px(?:\s+-?\d+(?:\.\d+)?px){3}", css)
    outer = [p for p in layers if "inset" not in p]
    if not outer:
        raise ValueError("no outer shadow: " + css)
    m = re.search(
        r"(rgba?\([^)]+\))\s+(-?\d+(?:\.\d+)?px)\s+(-?\d+(?:\.\d+)?px)\s+(-?\d+(?:\.\d+)?px)\s+(-?\d+(?:\.\d+)?px)",
        outer[0],
    )
    if not m:
        raise ValueError("unparsed shadow: " + outer[0])
    return {
        "$value": {
            "color": color(m.group(1)),
            "offsetX": dim(m.group(2)),
            "offsetY": dim(m.group(3)),
            "blur": dim(m.group(4)),
            "spread": dim(m.group(5)),
        },
        "$type": "shadow",
        "$extensions": {"source": source},
    }


home_l = READ["themes"]["light"]["pages"]["home"]
home_d = READ["themes"]["dark"]["pages"]["home"]
join_l = COMP["light"]["home"]["joinFree"]
sign_l = COMP["light"]["home"]["signIn"]
dialog_l = COMP["light"]["dialog"]
dialog_d = COMP["dark"]["dialog"]
price_l = COMP["light"]["pricing"]["price"]
price_d = COMP["dark"]["pricing"]["price"]
book_l = COMP["light"]["book"]["h1"]
focus = next(i for i in READ["themes"]["light"]["interactions"] if i["name"] == "nav-link-states")

core = {
    "font": {
        "family": {
            "body": leaf("fontFamily", INTER, "computed fontFamily of body on https://oku.club/ (capture-readings.json, light)", "Inter, then the system sans stack. Oku ships no --font token."),
            "display": leaf("fontFamily", SERIF, "computed fontFamily of h1 on https://oku.club/ (capture-readings.json, light)", "FabricSerifWeb for display and book titles. The file is not in this package."),
        },
        "size": {
            "display": leaf("dimension", home_l["h1"]["fontSize"], "computed fontSize of h1 on https://oku.club/ at 1440 (capture-readings.json)"),
            "price": leaf("dimension", price_l["size"], "computed fontSize of the $0 price on /pricing (components-computed.json)"),
            "book": leaf("dimension", book_l["size"], "computed fontSize of the book h1 on /book/taipei-story (components-computed.json)"),
            "body": leaf("dimension", home_l["bodySize"], "computed fontSize of body on https://oku.club/"),
            "nav": leaf("dimension", home_l["navExplore"]["fontSize"], "computed fontSize of the Explore nav link"),
            "button": leaf("dimension", home_l["joinButton"]["fontSize"], "computed fontSize of the header Join button"),
            "hero-cta": leaf("dimension", join_l["size"], "computed fontSize of the hero Join for free button"),
            "field": leaf("dimension", dialog_l["input"]["size"], "computed fontSize of the signup dialog email field"),
        },
        "weight": {
            "display": leaf("fontWeight", home_l["h1"]["fontWeight"], "computed fontWeight of h1"),
            "body": leaf("fontWeight", 400, "computed fontWeight of body text (Inter 400)"),
            "button": leaf("fontWeight", home_l["joinButton"]["fontWeight"], "computed fontWeight of the header Join button"),
        },
        "line-height": {
            "display": leaf("dimension", home_l["h1"]["lineHeight"], "computed lineHeight of h1 (48px * 1.3)"),
            "nav": leaf("dimension", home_l["navExplore"]["lineHeight"], "computed lineHeight of the Explore nav link"),
        },
        "letter-spacing": {
            "display": leaf("dimension", home_l["h1"]["letterSpacing"], "computed letterSpacing of h1"),
        },
    },
    "radius": {
        "control": leaf("dimension", home_l["joinButton"]["borderRadius"], "computed borderRadius of the header Join button"),
        "dialog": leaf("dimension", dialog_l["panel"]["radius"], "computed borderRadius of the Join dialog panel"),
    },
    "space": {
        "button-x": leaf("dimension", "24px", "computed paddingRight of the header Join button (capture-readings.json, dark join.paddingRight 24px; light pad matches)"),
        "field-x": leaf("dimension", "16px", "computed paddingLeft of the signup dialog email field"),
        "header-height": leaf("dimension", "80px", "measured height of the fixed header on https://oku.club/ at 1440"),
    },
    "size": {
        "button-height": leaf("dimension", home_l["joinButton"]["box"]["h"], "bounding box height of the header Join button at 1440"),
        "hero-cta-height": leaf("dimension", join_l["box"]["h"], "bounding box height of Join for free"),
        "field-height": leaf("dimension", dialog_l["input"]["box"]["h"], "bounding box height of the signup email field"),
        "dialog-width": leaf("dimension", dialog_l["panel"]["box"]["w"], "bounding box width of the Join dialog panel"),
    },
    "shadow": {
        "button": shadow(home_l["joinButton"]["boxShadow"], "computed boxShadow of the header Join button (light)"),
    },
}

light = {
    "color": {
        "page": leaf("color", home_l["htmlBg"], "computed backgroundColor of html on https://oku.club/ (light)"),
        "text": leaf("color", home_l["h1"]["color"], "computed color of h1 (light)"),
        "text-secondary": leaf("color", home_l["navExplore"]["color"], "computed color of the Explore nav link (light)"),
        "on-accent": leaf("color", home_l["joinButton"]["color"], "computed color of the header Join label (light)"),
        "accent": leaf("color", home_l["joinButton"]["backgroundColor"], "computed backgroundColor of the header Join button (light). Oku has no separate brand hue; the accent is ink."),
        "border": leaf("color", "rgba(19, 19, 20, 0.22)", "the inset 1px ring colour on the Sign in button, parsed from its boxShadow (components-computed.json, light)"),
        "field-border": leaf("color", border_color(dialog_l["input"]["border"]), "computed borderTopColor of the signup email field (components-computed.json, light)"),
        "scrim": leaf("color", dialog_l["scrim"], "computed backgroundColor of the Join dialog scrim"),
    },
    "component": {
        "button": {
            "background": leaf("color", home_l["joinButton"]["backgroundColor"], "computed backgroundColor of header Join (light)"),
            "text": leaf("color", home_l["joinButton"]["color"], "computed color of header Join (light)"),
            "radius": leaf("dimension", home_l["joinButton"]["borderRadius"], "computed borderRadius of header Join (light)"),
            "height": leaf("dimension", home_l["joinButton"]["box"]["h"], "bounding box height of header Join (light)"),
        },
        "sign-in": {
            "background": leaf("color", sign_l["bg"], "computed backgroundColor of the header Sign in button (light)"),
            "text": leaf("color", sign_l["color"], "computed color of the header Sign in button (light)"),
        },
        "dialog": {
            "background": leaf("color", dialog_l["panel"]["bg"], "computed backgroundColor of the Join dialog panel (light)"),
            "radius": leaf("dimension", dialog_l["panel"]["radius"], "computed borderRadius of the Join dialog panel (light)"),
            "width": leaf("dimension", dialog_l["panel"]["box"]["w"], "bounding box width of the Join dialog panel (light)"),
        },
        "field": {
            "height": leaf("dimension", dialog_l["input"]["box"]["h"], "bounding box height of the signup email field (light)"),
            "radius": leaf("dimension", dialog_l["input"]["radius"], "computed borderRadius of the signup email field"),
        },
    },
}

dark = {
    "color": {
        "page": leaf("color", home_d["htmlBg"], "computed backgroundColor of html on https://oku.club/ with prefers-color-scheme: dark"),
        "text": leaf("color", home_d["h1"]["color"], "computed color of h1 (dark)"),
        "text-secondary": leaf("color", home_d["navExplore"]["color"], "computed color of the Explore nav link (dark)"),
        "text-muted": leaf("color", price_d["color"], "computed color of the $0 price on /pricing (dark)"),
        "on-accent": leaf("color", home_d["joinButton"]["color"], "computed color of the header Join label (dark)"),
        "accent": leaf("color", home_d["joinButton"]["backgroundColor"], "computed backgroundColor of the header Join button (dark)"),
        "field-border": leaf("color", border_color(dialog_d["input"]["border"]), "computed borderTopColor of the signup email field (dark)"),
        "scrim": leaf("color", dialog_d["scrim"], "computed backgroundColor of the Join dialog scrim (dark). Same 0.6 black as light."),
        "field": leaf("color", dialog_d["input"]["bg"], "computed backgroundColor of the signup email field (dark)"),
        "disabled": leaf("color", dialog_d["submit"]["bg"], "computed backgroundColor of Create a free account before the form is filled (dark). The control is painted, not a disabled attribute."),
    },
    "component": {
        "button": {
            "background": leaf("color", home_d["joinButton"]["backgroundColor"], "computed backgroundColor of header Join (dark)"),
            "text": leaf("color", home_d["joinButton"]["color"], "computed color of header Join (dark)"),
            "radius": leaf("dimension", home_d["joinButton"]["borderRadius"], "computed borderRadius of header Join (dark)"),
            "height": leaf("dimension", home_d["joinButton"]["box"]["h"], "bounding box height of header Join (dark)"),
        },
        "dialog": {
            "background": leaf("color", dialog_d["panel"]["bg"], "computed backgroundColor of the Join dialog panel (dark)"),
            "radius": leaf("dimension", dialog_d["panel"]["radius"], "computed borderRadius of the Join dialog panel (dark)"),
        },
        "field": {
            "background": leaf("color", dialog_d["input"]["bg"], "computed backgroundColor of the signup email field (dark)"),
            "text": leaf("color", dialog_d["input"]["color"], "computed color of the signup email field placeholder text (dark)"),
            "radius": leaf("dimension", dialog_d["input"]["radius"], "computed borderRadius of the signup email field (dark)"),
        },
    },
}

# Focus: outline width was 0. Record that as not tokenised rather than inventing a ring.
not_tokenised = {
    "focus-ring": "Nav link focus-visible computed outlineWidth 0px and boxShadow none (capture-readings.json nav-link-states). No focus ring was painted.",
    "hover": "Header Join hover computed the same background and color as default (nav-link-states.joinHover). No hover colour was painted.",
    "motion": "No duration or easing was read off a running transition. Toastify and Swiper vendor variables were not tokenised.",
    "spacing-scale": "No spacing custom properties. Only the measured paddings in core.space are tokenised.",
    "status-colours": "No success, warning, danger, or info colour was painted on a public control. Toastify declares those variables; Oku never showed a toast.",
    "pressed": "A pressed state was not held. Not captured.",
    "disabled-attribute": "No control with the disabled attribute was on the public pages.",
}


def check(tree, path=""):
    for k, v in tree.items():
        if isinstance(v, dict) and "$value" in v:
            p = f"{path}.{k}" if path else k
            ty, val = v["$type"], v["$value"]
            if not v.get("$extensions", {}).get("source"):
                raise SystemExit("missing source: " + p)
            if ty == "dimension" and isinstance(val, str) and not val.startswith("{") and not re.fullmatch(r"-?\d+(\.\d+)?px", val):
                raise SystemExit(f"{p}: bad dimension {val}")
            if ty == "color" and isinstance(val, str) and not val.startswith("{") and not re.match(r"^(#[0-9a-f]{6}|rgba?\()", val):
                raise SystemExit(f"{p}: bad color {val}")
        elif isinstance(v, dict) and not k.startswith("$"):
            check(v, f"{path}.{k}" if path else k)


check(core)
check(light)
check(dark)

tokens = {
    "core": core,
    "light": light,
    "dark": dark,
    "$themes": [
        {"id": "light", "name": "Light", "selectedTokenSets": {"core": "source", "light": "enabled"},
         "$description": "Default public surface. html background #ffffff."},
        {"id": "dark", "name": "Dark", "selectedTokenSets": {"core": "source", "dark": "enabled"},
         "$description": "prefers-color-scheme: dark. No in-page theme switch on the public surface."},
    ],
    "$metadata": {"tokenSetOrder": ["core", "light", "dark"]},
    "$extensions": {"notTokenised": not_tokenised, "focusProbe": focus["focus"]},
}
(HERE / "tokens.json").write_text(json.dumps(tokens, indent=2, ensure_ascii=False) + "\n")


def count(d):
    return sum(count(v) for v in d.values()) if isinstance(d, dict) and "$value" not in d else 1


print({k: count(v) for k, v in tokens.items() if k in ("core", "light", "dark")})
