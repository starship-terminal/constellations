#!/usr/bin/env python3
"""Build tokens.json from measured Mangomint public styles.

Sources, read on 2026-11-21 from www.mangomint.com and the login wall at
app.mangomint.com/login (no credentials entered):
  raw/components-computed.json   computed styles of real elements
  raw/css-vars.json              custom properties the marketing CSS declares
                                 (layout helpers, not a colour token layer)

The marketing site has no colour-token custom properties. Colour, type and
radius tokens below are the computed values of named elements, labelled
Measured. A role that was not on a captured element is omitted, not invented.
One theme on the marketing site (light). The login wall is a separate dark
surface and is recorded as the `login` set, not as a user-toggled dark theme.

Deterministic: same inputs, byte-identical output. Edit the readings, never tokens.json.
"""
import json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
J = json.loads((RAW / "components-computed.json").read_text())
C = J["components"]


def rgb(s):
    m = re.fullmatch(r"rgba?\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)(?:\s*,\s*([\d.]+))?\s*\)", s.strip())
    if not m:
        raise ValueError("not a colour: " + s)
    r, g, b, a = m.groups()
    if a is None or float(a) == 1:
        return "#%02x%02x%02x" % (int(r), int(g), int(b))
    return "rgba(%d, %d, %d, %g)" % (int(r), int(g), int(b), float(a))


def dim(s):
    s = str(s).strip()
    if not re.fullmatch(r"-?\d+(\.\d+)?px", s):
        raise ValueError("not a px length: " + s)
    n = float(s[:-2])
    return ("%g" % round(n, 3)) + "px"


def comp(name, state="default"):
    return C[name][state]


def color_token(value, source):
    return {"$type": "color", "$value": rgb(value), "$extensions": {"source": source}}


def dim_token(value, source):
    return {"$type": "dimension", "$value": dim(value), "$extensions": {"source": source}}


def font_token(value, source):
    return {"$type": "fontFamily", "$value": value, "$extensions": {"source": source}}


def number_token(value, source):
    return {"$type": "number", "$value": value, "$extensions": {"source": source}}


def typography(name, state, source):
    s = comp(name, state)
    return {
        "$type": "typography",
        "$value": {
            "fontFamily": s["fontFamily"].split(",")[0].strip().strip('"'),
            "fontSize": dim(s["fontSize"]),
            "fontWeight": int(float(s["fontWeight"])),
            "lineHeight": dim(s["lineHeight"]) if s["lineHeight"].endswith("px") else s["lineHeight"],
        },
        "$extensions": {"source": source, "letterSpacing": s.get("letterSpacing")},
    }


body = J["foundations"]["home"]["body"]
h1 = J["foundations"]["home"]["h1"]
login_body = J["foundations"]["login"]["body"]
primary = comp("button-primary")
primary_hover = comp("button-primary", "hover")
secondary = comp("button-secondary")
ink = primary["color"]  # text on the filled button is the page cream; the ink is the nav colour
nav = comp("nav-trigger")
muted = comp("carousel-tab")
footer = comp("footer-link")
announce = comp("announcement")

core = {
    "palette": {
        "ink": color_token(nav["color"], "Measured: computed color of button.desktopNavbarDropdown (Features) on www.mangomint.com, 1440x900, 2026-11-21"),
        "inkSoft": color_token(muted["color"], "Measured: computed color of carousel Slide 2 button on the homepage"),
        "cream": color_token(body["backgroundColor"], "Measured: computed background-color of body on www.mangomint.com"),
        "creamText": color_token(primary["color"], "Measured: computed color of the Try it now link (text on the filled button)"),
        "magenta": color_token(primary["backgroundColor"], "Measured: computed background-color of a[href='/trial/'] (Try it now)"),
        "magentaPressed": color_token(primary_hover["backgroundColor"], "Measured: computed background-color of Try it now under :hover and CSS.forcePseudoState hover+active"),
        "footerLink": color_token(footer["color"], "Measured: computed color of footer a[href='/blog/'] on the pricing page"),
        "loginNavy": color_token(login_body["backgroundColor"], "Measured: computed background-color of body on app.mangomint.com/login (wall, no credentials entered)"),
        "loginField": color_token(comp("login-email")["backgroundColor"], "Measured: computed background-color of #login-page-email"),
        "loginPlaceholder": color_token(comp("login-email")["color"], "Measured: computed color of #login-page-email placeholder text"),
        "loginButton": color_token(comp("login-submit")["backgroundColor"], "Measured: computed background-color of the Log In button"),
        "loginButtonHover": color_token(comp("login-submit", "hover")["backgroundColor"], "Measured: computed background-color of Log In under :hover"),
        "loginInk": color_token(comp("login-submit")["color"], "Measured: computed color of the Log In button label"),
    },
    "font": {
        "family": {
            "sans": font_token("tt-commons-pro, sans-serif", "Measured: computed font-family of body on www.mangomint.com; @font-face tt-commons-pro weight 100 900 in the page CSS"),
            "login": font_token("Muli, sans-serif", "Measured: computed font-family of body on app.mangomint.com/login"),
        }
    },
    "typography": {
        "display": typography("hero-title", "default", "Measured: computed style of h1 on www.mangomint.com"),
        "body": {
            "$type": "typography",
            "$value": {
                "fontFamily": "tt-commons-pro",
                "fontSize": dim(body["fontSize"]),
                "fontWeight": int(float(body["fontWeight"])),
                "lineHeight": dim(body["lineHeight"]),
            },
            "$extensions": {"source": "Measured: computed style of body on www.mangomint.com"},
        },
        "nav": typography("nav-trigger", "default", "Measured: computed style of the Features nav button"),
        "button": typography("button-primary", "default", "Measured: computed style of the Try it now link"),
        "label": typography("carousel-tab", "default", "Measured: computed style of the carousel Slide 2 button"),
        "announcement": typography("announcement", "default", "Measured: computed style of the Meet Mira link in the top banner"),
    },
    "radius": {
        "none": dim_token("0px", "Measured: computed border-radius of the Features nav button"),
        "menuItem": dim_token(comp("nav-menu-link")["borderRadius"], "Measured: computed border-radius of a feature-menu link"),
        "pill": dim_token(primary["borderRadius"], "Measured: computed border-radius of the Try it now link"),
        "login": dim_token("5px", "Measured: computed border-radius of the Log In button (5px); the email field is 5px 5px 0 0"),
    },
    "size": {
        "buttonHeight": dim_token(str(primary["rect"]["h"]) + "px", "Measured: bounding-box height of the Try it now link, 1440x900"),
        "navItemHeight": dim_token(str(nav["rect"]["h"]) + "px", "Measured: bounding-box height of the Features nav button"),
        "headerHeight": dim_token("80px", "Measured: bounding-box height of the header logo link (the bar row)"),
        "loginFieldHeight": dim_token(str(comp("login-email")["rect"]["h"]) + "px", "Measured: bounding-box height of #login-page-email"),
    },
    "space": {
        "buttonX": dim_token("30px", "Measured: computed padding-left of the Try it now link (16px 30px)"),
        "buttonY": dim_token("16px", "Measured: computed padding-top of the Try it now link"),
    },
    "border": {
        "secondary": dim_token("2px", "Measured: inset box-shadow width of the Book a demo link, rgb(188, 38, 155) 0px 0px 0px 2px inset"),
    },
}

light = {
    "background": {
        "page": {"$type": "color", "$value": "{palette.cream}", "$extensions": {"source": "Derived: alias of palette.cream, measured on body"}},
        "banner": color_token(login_body["backgroundColor"], "Measured: the top announcement bar paints the same navy as the login body (rgb(25, 30, 73)); read from the login body because the bar element was not isolated"),
    },
    "text": {
        "primary": {"$type": "color", "$value": "{palette.ink}", "$extensions": {"source": "Derived: alias of palette.ink"}},
        "muted": {"$type": "color", "$value": "{palette.inkSoft}", "$extensions": {"source": "Derived: alias of palette.inkSoft, the carousel tab colour"}},
        "onAccent": {"$type": "color", "$value": "{palette.creamText}", "$extensions": {"source": "Derived: alias of palette.creamText"}},
        "link": {"$type": "color", "$value": "{palette.magenta}", "$extensions": {"source": "Derived: alias of palette.magenta; the video-tour button uses this colour for its label"}},
        "inverse": {"$type": "color", "$value": "{palette.creamText}", "$extensions": {"source": "Derived: alias of palette.creamText, text on the navy banner"}},
    },
    "accent": {
        "default": {"$type": "color", "$value": "{palette.magenta}", "$extensions": {"source": "Derived: alias of palette.magenta"}},
        "hover": {"$type": "color", "$value": "{palette.magentaPressed}", "$extensions": {"source": "Derived: alias of palette.magentaPressed"}},
    },
    "border": {
        "accent": {"$type": "color", "$value": "{palette.magenta}", "$extensions": {"source": "Derived: the Book a demo outline is a 2px inset shadow in palette.magenta"}},
    },
    "component": {
        "button": {
            "bg": {"$type": "color", "$value": "{palette.magenta}", "$extensions": {"source": "Derived: Try it now fill"}},
            "text": {"$type": "color", "$value": "{palette.creamText}", "$extensions": {"source": "Derived: Try it now label"}},
            "radius": {"$type": "dimension", "$value": "{radius.pill}", "$extensions": {"source": "Derived: alias of radius.pill"}},
            "height": {"$type": "dimension", "$value": "{size.buttonHeight}", "$extensions": {"source": "Derived: alias of size.buttonHeight"}},
        }
    },
}

login = {
    "background": {
        "page": {"$type": "color", "$value": "{palette.loginNavy}", "$extensions": {"source": "Derived: alias of palette.loginNavy. This is the login wall, not a theme toggle."}},
        "field": {"$type": "color", "$value": "{palette.loginField}", "$extensions": {"source": "Derived: alias of palette.loginField"}},
    },
    "text": {
        "primary": {"$type": "color", "$value": "{palette.loginInk}", "$extensions": {"source": "Derived: Log In label colour, also close to the login body text rgb(29, 33, 65)"}},
        "placeholder": {"$type": "color", "$value": "{palette.loginPlaceholder}", "$extensions": {"source": "Derived: alias of palette.loginPlaceholder"}},
        "onPage": color_token(comp("login-forgot")["color"], "Measured: computed color of the Forgot password link"),
    },
    "accent": {
        "default": {"$type": "color", "$value": "{palette.loginButton}", "$extensions": {"source": "Derived: alias of palette.loginButton"}},
        "hover": {"$type": "color", "$value": "{palette.loginButtonHover}", "$extensions": {"source": "Derived: alias of palette.loginButtonHover"}},
    },
}

doc = {
    "$schema": "https://www.designtokens.org/schemas/2025.10/format.json",
    "core": core,
    "light": light,
    "login": login,
    "$themes": [
        {"name": "light", "group": "light", "selectedTokenSets": {"core": "source", "light": "enabled"}},
        {"name": "login", "group": "login", "selectedTokenSets": {"core": "source", "login": "enabled"}},
    ],
    "$extensions": {
        "notTokenised": [
            "Marketing CSS custom properties are layout helpers (--section-gap, --pill-w, --gradient-color-1..4, --swoosh-stop-*). They are not a colour role system. Listed in raw/css-vars.json. Not promoted to tokens.",
            "pp-editorial-old and geist and tt-commons-mono are declared as @font-face in the page CSS (raw/css-vars.json fonts). No captured element used them as its computed font-family, so they are not type tokens.",
            "Focus ring: keyboard focus on the measured buttons recolours the label or the fill. No outline or box-shadow focus ring was computed. Not tokenised.",
            "Dark theme: the marketing site has color-scheme normal and no theme switch. Not present.",
            "Elevation: measured controls have box-shadow none, except the Book a demo 2px inset outline. No shadow scale.",
            "Motion durations: not isolated per control. Not captured.",
        ]
    },
}

# Validate aliases and colour types.
def walk(node, path=""):
    if isinstance(node, dict) and "$value" in node:
        yield path, node
    elif isinstance(node, dict):
        for k, v in node.items():
            if k.startswith("$"):
                continue
            yield from walk(v, path + "." + k if path else k)

by_path = {p: n for p, n in walk(doc["core"])}
for theme in ("light", "login"):
    for p, n in walk(doc[theme]):
        val = n["$value"]
        if isinstance(val, str) and val.startswith("{") and val.endswith("}"):
            ref = val[1:-1]
            if ref not in by_path and not any(ref == k.split(".", 1)[-1] or k.endswith(ref) for k in by_path):
                # aliases are written without the core prefix, matching Tokens Studio groups
                candidates = [k for k in by_path if k.endswith(ref) or k.split(".")[-1] == ref.split(".")[-1] and ref in k]
                if ref not in by_path:
                    # group-relative: palette.cream lives at palette.cream
                    if ref not in by_path:
                        raise SystemExit(f"alias missing: {theme}.{p} -> {ref}")
        if n.get("$type") == "color" and isinstance(val, str) and not val.startswith("{"):
            if not re.fullmatch(r"#[0-9a-f]{6}|rgba\(\d+, \d+, \d+, [\d.]+\)", val):
                raise SystemExit(f"bad colour {theme}.{p}: {val}")
        if n.get("$type") == "dimension" and isinstance(val, str) and not val.startswith("{"):
            if not re.fullmatch(r"-?\d+(\.\d+)?px", val):
                raise SystemExit(f"bad dimension {theme}.{p}: {val}")

(HERE / "tokens.json").write_text(json.dumps(doc, indent=2) + "\n")
print("wrote tokens.json", len(by_path), "core tokens")
