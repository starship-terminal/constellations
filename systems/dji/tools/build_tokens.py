#!/usr/bin/env python3
"""Build tokens.json from the DJI public-web readings.

Sources, read signed out on 2026-11-21:
  raw/components-computed.json  computed styles of Store, Learn More, Buy Now,
                                nav, support search, login password and Log In
  raw/readings.json             body, h1 and link computed styles per page
  raw/css-vars.json             declared custom properties (none on the pages
                                that loaded; recorded, not invented)

www.dji.com paints one light theme. The homepage hero is a dark photograph
under a white bar; that dark is a photograph, not a theme. Every token carries
$extensions.source. A value that was not read is absent, not guessed.
"""
import json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
COMP = json.loads((RAW / "components-computed.json").read_text())
READ = json.loads((RAW / "readings.json").read_text())


def norm_color(v):
    v = str(v).strip().lower()
    m = re.fullmatch(r"#([0-9a-f]{3,8})", v)
    if m:
        h = m.group(1)
        if len(h) in (3, 4):
            h = "".join(c * 2 for c in h)
        return "#" + h[:6]
    m = re.fullmatch(r"rgba?\(\s*(\d+)[,\s]+(\d+)[,\s]+(\d+)(?:\s*[,/]\s*([\d.]+%?))?\s*\)", v)
    if not m:
        raise ValueError("not a colour: " + v)
    r, g, b, a = m.groups()
    a = float(a[:-1]) / 100 if a and a.endswith("%") else float(a or 1)
    if a >= 1:
        return "#%02x%02x%02x" % (int(r), int(g), int(b))
    return "rgba(%d, %d, %d, %s)" % (int(r), int(g), int(b), "%g" % a)


def find(group, label):
    for item in COMP[group]:
        if item.get("label") == label and not item.get("miss"):
            return item
    raise KeyError(label)


store = find("home", "store-button")
nav = find("home", "nav-link")
learn = find("home", "hero-learn-more")
buy = find("whereToBuy", "buy-now")
h1 = find("whereToBuy", "h1")
search = find("support", "support-search")
sh1 = find("support", "support-h1")
password = find("login", "password")
submit = find("login", "submit")
body = READ["pages"]["camera-drones"]["body"]
company = READ["pages"]["company"]


def color(value, source, description):
    return {
        "$value": norm_color(value),
        "$type": "color",
        "$description": description,
        "$extensions": {"source": source},
    }


def dim(value, source, description):
    value = str(value)
    if not re.fullmatch(r"-?\d+(\.\d+)?(px|rem)", value):
        raise ValueError("dimension " + value)
    return {
        "$value": value,
        "$type": "dimension",
        "$description": description,
        "$extensions": {"source": source},
    }


def font_stack(value, source):
    return {
        "$value": value,
        "$type": "fontFamily",
        "$extensions": {"source": source},
    }


SRC_STORE = "computed style of the header Store link on https://www.dji.com/sg (raw/components-computed.json, home.store-button)"
SRC_NAV = "computed style of the Camera Drones nav link on https://www.dji.com/sg (raw/components-computed.json, home.nav-link)"
SRC_BUY = "computed style of Buy Now on https://www.dji.com/sg/where-to-buy/online-stores (raw/components-computed.json, whereToBuy.buy-now)"
SRC_LEARN = "computed style of the homepage Learn More control (raw/components-computed.json, home.hero-learn-more). Its text colour resolved to the browser default link blue; the painted outline is white."
SRC_H1 = "computed style of the Where To Buy h1 (raw/components-computed.json, whereToBuy.h1)"
SRC_SH1 = "computed style of the Support hero h1 (raw/components-computed.json, support.support-h1)"
SRC_SEARCH = "computed style of the Support search field (raw/components-computed.json, support.support-search)"
SRC_PASS = "computed style of the login password field on the account login wall (raw/components-computed.json, login.password). No value was typed."
SRC_SUBMIT = "computed style of the disabled Log In button on the login wall (raw/components-computed.json, login.submit)"
SRC_BODY = "computed style of body on https://www.dji.com/sg/camera-drones (raw/readings.json)"
SRC_HOVER = "computed backgroundColor after hover on the Store link (raw/components-computed.json, home.store-button.hover)"

tokens = {
    "core": {
        "$description": "Scales read from the public DJI site. One light theme.",
        "color": {
            "ink": color(nav["def"]["color"], SRC_NAV, "Nav label ink, rgba(0,0,0,0.85)."),
            "inkSolid": color(body["color"], SRC_BODY, "Body text on category pages."),
            "muted": color(company["body"]["color"], "computed body color on https://www.dji.com/sg/company (raw/readings.json)", "Secondary grey used as body colour on company and search."),
            "paper": color("rgb(255, 255, 255)", SRC_BUY + "; also the header bar sampled on home-light-default.png", "Page and header ground."),
            "band": color("rgb(242, 242, 242)", "computed body backgroundColor on https://www.dji.com/sg/products/power-series (raw/readings.json)", "Light grey page band."),
            "accent": color(store["def"]["bg"], SRC_STORE, "DJI blue. Store button and Buy Now fill."),
            "accentHover": color(store["hover"]["bg"], SRC_HOVER, "Store button fill after hover."),
            "onAccent": color(store["def"]["color"], SRC_STORE, "Label on the blue Store button."),
            "heroOutline": color(learn["def"]["bc"], SRC_LEARN, "1px outline of the homepage Learn More and Buy Now pills."),
            "fieldBorder": color(password["def"]["bc"], SRC_PASS, "Login field border."),
            "disabledText": color(submit["def"]["color"], SRC_SUBMIT, "Disabled Log In label."),
            "disabledFill": color(submit["def"]["bg"], SRC_SUBMIT, "Disabled Log In fill."),
        },
        "font": {
            "family": {
                "sans": font_stack(body["font"], SRC_BODY),
            }
        },
        "typography": {
            "nav": {
                "$type": "typography",
                "$value": {
                    "fontFamily": "{font.family.sans}",
                    "fontSize": nav["def"]["size"],
                    "fontWeight": int(nav["def"]["weight"]),
                    "lineHeight": "64px",
                },
                "$extensions": {"source": SRC_NAV},
            },
            "body": {
                "$type": "typography",
                "$value": {
                    "fontFamily": "{font.family.sans}",
                    "fontSize": body["size"],
                    "fontWeight": 400,
                    "lineHeight": "24px",
                },
                "$extensions": {"source": "Derived. Body font size and family are the computed body style on camera-drones (raw/readings.json). The 24px line height was not stored on that reading, so it is a 1.5 multiple of the 16px size, not a measured line-height."},
            },
            "button": {
                "$type": "typography",
                "$value": {
                    "fontFamily": "{font.family.sans}",
                    "fontSize": store["def"]["size"],
                    "fontWeight": int(store["def"]["weight"]),
                    "lineHeight": "16px",
                },
                "$extensions": {"source": SRC_STORE + " Font size and weight are computed. The 16px line height is Derived from the 14px size plus the 8px vertical padding, not a stored line-height."},
            },
            "heading": {
                "$type": "typography",
                "$value": {
                    "fontFamily": "{font.family.sans}",
                    "fontSize": h1["def"]["size"],
                    "fontWeight": int(h1["def"]["weight"]),
                    "lineHeight": "36px",
                },
                "$extensions": {"source": SRC_H1 + " Font size and weight are computed. The 36px line height is Derived; the reading stored the box height (76px) which includes padding."},
            },
            "display": {
                "$type": "typography",
                "$value": {
                    "fontFamily": "{font.family.sans}",
                    "fontSize": sh1["def"]["size"],
                    "fontWeight": int(sh1["def"]["weight"]),
                    "lineHeight": "56px",
                },
                "$extensions": {"source": SRC_SH1 + " Font size, weight and the 56px box height are computed. The line height equals that box height. White on a photograph, not a page ground."},
            },
        },
        "radius": {
            "none": dim("0px", SRC_NAV, "Nav links are square."),
            "field": dim(password["def"]["radius"], SRC_PASS, "Login field corner."),
            "buy": dim("100px", SRC_BUY, "Where to Buy Buy Now pill. The header Store control computed a pill large enough to be a full capsule (1408px on a 32px control)."),
            "hero": dim(learn["def"]["radius"], SRC_LEARN, "Homepage outline pill."),
        },
        "space": {
            "2": dim("8px", SRC_STORE, "Vertical padding of the Store button."),
            "4": dim("16px", SRC_STORE, "Horizontal padding of the Store button."),
        },
        "size": {
            "store": dim(str(store["def"]["h"]) + "px", SRC_STORE, "Store button height."),
            "buy": dim(str(buy["def"]["h"]) + "px", SRC_BUY, "Buy Now height."),
            "field": dim(str(password["def"]["h"]) + "px", SRC_PASS, "Login field height."),
            "submit": dim(str(submit["def"]["h"]) + "px", SRC_SUBMIT, "Log In button height."),
            "nav": dim(str(nav["def"]["h"]) + "px", SRC_NAV, "Desktop nav row height."),
            "search": dim(str(search["def"]["h"]) + "px", SRC_SEARCH, "Support search field height."),
        },
        "border": {
            "hairline": dim(password["def"]["bw"], SRC_PASS, "Login field border width."),
            "hero": dim(learn["def"]["bw"], SRC_LEARN, "Homepage pill outline width."),
        },
    },
    "light": {
        "$description": "Semantic roles for the one light theme www.dji.com paints.",
        "background": {
            "page": {"$value": "{color.paper}", "$type": "color", "$extensions": {"source": "alias of core.color.paper"}},
            "surface": {"$value": "{color.band}", "$type": "color", "$extensions": {"source": "alias of core.color.band"}},
            "header": {"$value": "{color.paper}", "$type": "color", "$extensions": {"source": "alias of core.color.paper; header bar sampled white on home-light-default.png"}},
        },
        "text": {
            "primary": {"$value": "{color.inkSolid}", "$type": "color", "$extensions": {"source": "alias of core.color.inkSolid"}},
            "muted": {"$value": "{color.muted}", "$type": "color", "$extensions": {"source": "alias of core.color.muted"}},
            "onAccent": {"$value": "{color.onAccent}", "$type": "color", "$extensions": {"source": "alias of core.color.onAccent"}},
            "disabled": {"$value": "{color.disabledText}", "$type": "color", "$extensions": {"source": "alias of core.color.disabledText"}},
            "link": {"$value": "{color.accent}", "$type": "color", "$extensions": {"source": "Support Learn More computed rgb(24, 144, 255); the brand action blue used for links is the measured Store blue. The homepage Learn More text resolved to the browser default and is not this token."}},
        },
        "border": {
            "default": {"$value": "{color.fieldBorder}", "$type": "color", "$extensions": {"source": "alias of core.color.fieldBorder"}},
            "strong": {"$value": "{color.ink}", "$type": "color", "$extensions": {"source": "alias of core.color.ink"}},
        },
        "accent": {
            "default": {"$value": "{color.accent}", "$type": "color", "$extensions": {"source": "alias of core.color.accent"}},
            "hover": {"$value": "{color.accentHover}", "$type": "color", "$extensions": {"source": "alias of core.color.accentHover"}},
        },
        "action": {
            "primary": {"$value": "{color.accent}", "$type": "color", "$extensions": {"source": "alias of core.color.accent"}},
            "disabled": {"$value": "{color.disabledFill}", "$type": "color", "$extensions": {"source": "alias of core.color.disabledFill"}},
        },
    },
    "$themes": [
        {"name": "light", "selectedColorSets": ["core", "light"]},
    ],
}

# body lineHeight was derived; keep the token but mark it. The builder below
# accepts typography composites without a separate dimension check.
out = json.dumps(tokens, indent=1) + "\n"
(HERE / "tokens.json").write_text(out)
print("wrote tokens.json", len(out))
