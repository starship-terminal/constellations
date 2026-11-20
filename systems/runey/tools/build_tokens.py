#!/usr/bin/env python3
"""Build tokens.json from the Runey public-site readings.

Sources, read from https://runey.app/ on 2026-11-21, signed out:
  raw/token-blocks.json   the :root and .dark custom properties in
                          assets/index-*.css (HSL channels, shadcn names)
  raw/controls.json       computed styles of the painted controls
  raw/readings.json       page background, body font, use counts

The public site paints one light theme. The .dark block is in the same
stylesheet and is the signed-in theme switch (help documents Dark & Light
Mode). Those values are Measured from the stylesheet. They were not seen
on a public page, so the README says so.

Every token carries $extensions.source. A dimension is one px or rem length.
"""
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
BLOCKS = json.loads((RAW / "token-blocks.json").read_text())
CONTROLS = json.loads((RAW / "controls.json").read_text())
READINGS = json.loads((RAW / "readings.json").read_text())

CSS = "https://runey.app/assets/index-BNow9ey6.css"
DATE = "2026-11-21"


def hsl_channels(value):
    parts = value.split()
    if len(parts) != 3:
        raise ValueError("not HSL channels: " + value)
    h, s, l = parts
    if not s.endswith("%") or not l.endswith("%"):
        raise ValueError("not HSL channels: " + value)
    return float(h), float(s[:-1]) / 100, float(l[:-1]) / 100


def hsl_to_hex(value):
    h, s, l = hsl_channels(value)
    c = (1 - abs(2 * l - 1)) * s
    hp = (h % 360) / 60
    x = c * (1 - abs(hp % 2 - 1))
    if 0 <= hp < 1:
        r, g, b = c, x, 0
    elif 1 <= hp < 2:
        r, g, b = x, c, 0
    elif 2 <= hp < 3:
        r, g, b = 0, c, x
    elif 3 <= hp < 4:
        r, g, b = 0, x, c
    elif 4 <= hp < 5:
        r, g, b = x, 0, c
    else:
        r, g, b = c, 0, x
    m = l - c / 2
    rgb = [round((ch + m) * 255) for ch in (r, g, b)]
    return "#%02x%02x%02x" % tuple(rgb)


def color(value, source):
    return {
        "$type": "color",
        "$value": hsl_to_hex(value),
        "$extensions": {
            "source": source,
            "authored": value,
            "evidence": "Measured",
        },
    }


def dim(value, source):
    if not re.fullmatch(r"-?\d*\.?\d+(px|rem)", value):
        raise ValueError("not a dimension: " + value)
    return {
        "$type": "dimension",
        "$value": value,
        "$extensions": {"source": source, "evidence": "Measured"},
    }


def num(value, source, typ="number"):
    return {
        "$type": typ,
        "$value": value,
        "$extensions": {"source": source, "evidence": "Measured"},
    }


def font_stack(value, source):
    return {
        "$type": "fontFamily",
        "$value": value,
        "$extensions": {"source": source, "evidence": "Measured"},
    }


root = next(b for b in BLOCKS["blocks"] if b["selector"] == ":root")["props"]
dark = next(b for b in BLOCKS["blocks"] if b["selector"] == ".dark")["props"]


def semantic(props, selector, seen):
    source = f"{CSS} {selector}, captured {DATE}. HSL channels converted to sRGB."
    if not seen:
        source += " Declared in the stylesheet. Not applied on a public page."
    names = [
        "background", "foreground", "card", "card-foreground", "popover", "popover-foreground",
        "primary", "primary-light", "primary-foreground", "secondary", "secondary-foreground",
        "muted", "muted-foreground", "accent", "accent-foreground", "destructive",
        "destructive-foreground", "success", "success-foreground", "warning", "warning-foreground",
        "orange", "orange-foreground", "border", "input", "ring", "chart-1", "chart-2", "chart-3",
        "chart-4", "chart-5", "sidebar-background", "sidebar-foreground", "sidebar-primary",
        "sidebar-primary-foreground", "sidebar-accent", "sidebar-accent-foreground",
        "sidebar-border", "sidebar-ring", "customer-pane",
    ]
    color_set = {}
    for name in names:
        key = "--" + name
        if key not in props:
            continue
        token = color(props[key], source + f" {key}.")
        if not seen:
            token["$extensions"]["evidence"] = "Measured"
            token["$extensions"]["seen"] = "not on a public page"
        color_set[name] = token
    return {"color": color_set}


def painted(record, field):
    node = record.get("painted") or record
    return node[field]


start = CONTROLS["Start for free"]
see = CONTROLS["See features"]
yearly = CONTROLS["Yearly"]
email = CONTROLS["email"]
email_focus = CONTROLS["emailFocus"]
google = CONTROLS["Continue with Google"]
h1 = BLOCKS["h1"]

src_ctrl = "computed style on https://runey.app/ 1440x900, 2026-11-21, raw/controls.json"
src_h1 = "computed style of h1 on https://runey.app/, 2026-11-21, raw/token-blocks.json"
src_page = "computed style of body on https://runey.app/, 2026-11-21, raw/readings.json"
src_auth = "computed style on https://runey.app/auth, 2026-11-21, raw/controls.json. Fields were not filled."

tokens = {
    "core": {
        "color": {
            "ink": color("0 0% 10%", src_page + " body color rgb(26, 26, 26), matches :root --foreground."),
            "paper": color("0 0% 98%", src_page + " body background rgb(250, 250, 250), matches :root --background."),
            "white": color("0 0% 100%", src_auth + " email field background rgb(255, 255, 255)."),
            "muted": color("0 0% 46%", f"{CSS} :root --muted-foreground, captured {DATE}."),
        },
        "font": {
            "family": {
                "sans": font_stack(
                    ["Poppins", "sans-serif"],
                    src_page + " font-family Poppins, sans-serif. Poppins is loaded by the site; the package does not ship the font files.",
                ),
            },
        },
        "typography": {
            "display": {
                "$type": "typography",
                "$value": {
                    "fontFamily": "{font.family.sans}",
                    "fontSize": "64px",
                    "fontWeight": 600,
                    "lineHeight": "67.2px",
                    "letterSpacing": "-1.92px",
                },
                "$extensions": {"source": src_h1 + " text-[2.25rem] md:text-[4rem] font-semibold tracking-[-0.03em] leading-[1.05].", "evidence": "Measured"},
            },
            "body": {
                "$type": "typography",
                "$value": {
                    "fontFamily": "{font.family.sans}",
                    "fontSize": "16px",
                    "fontWeight": 400,
                    "lineHeight": "24px",
                },
                "$extensions": {"source": src_h1 + " body size from the hero lead and the use-count peak (16px on 366 nodes).", "evidence": "Measured"},
            },
            "button": {
                "$type": "typography",
                "$value": {
                    "fontFamily": "{font.family.sans}",
                    "fontSize": painted(start, "fontSize"),
                    "fontWeight": int(painted(start, "fontWeight")),
                    "lineHeight": painted(start, "lineHeight"),
                },
                "$extensions": {"source": src_ctrl + " header Start for free.", "evidence": "Measured"},
            },
            "nav": {
                "$type": "typography",
                "$value": {
                    "fontFamily": "{font.family.sans}",
                    "fontSize": "13px",
                    "fontWeight": 500,
                    "lineHeight": "19.5px",
                },
                "$extensions": {"source": "computed style of a nav link on https://runey.app/, 2026-11-21, raw/readings.json nav-link.", "evidence": "Measured"},
            },
            "label": {
                "$type": "typography",
                "$value": {
                    "fontFamily": "{font.family.sans}",
                    "fontSize": painted(yearly, "fontSize"),
                    "fontWeight": int(painted(yearly, "fontWeight")),
                    "lineHeight": painted(yearly, "lineHeight"),
                },
                "$extensions": {"source": src_ctrl + " pricing Yearly segment.", "evidence": "Measured"},
            },
            "field": {
                "$type": "typography",
                "$value": {
                    "fontFamily": "{font.family.sans}",
                    "fontSize": email["fontSize"],
                    "fontWeight": int(email["fontWeight"]),
                    "lineHeight": email["lineHeight"],
                },
                "$extensions": {"source": src_auth, "evidence": "Measured"},
            },
        },
        "radius": {
            "control": dim("9999px", src_ctrl + " Start for free, See features, pricing segment, and auth fields are pill (9999px)."),
            "card": dim("12px", "computed style of the FAQ accordion button, raw/readings.json accordion borderRadius 12px."),
            "sheet": dim(root["--radius"], f"{CSS} :root --radius, captured {DATE}. Auth card uses a close value; the token is the declared one."),
        },
        "space": {
            "2": dim("8px", "Derived from the 4px step visible in control padding. Not a named scale in the stylesheet."),
            "3": dim("12px", "Derived. Pricing and FAQ cards use 12px radius and similar inset padding."),
            "4": dim("16px", "Derived. Body size and the common gap. The product does not publish a spacing scale."),
        },
        "size": {
            "control-sm": dim(painted(start, "height") if False else "32px", src_ctrl + " header Start for free painted height 32px."),
            "control-md": dim("44px", src_ctrl + " See features and auth fields are 44px tall."),
            "control-segment": dim("28px", src_ctrl + " pricing segment height 28px."),
        },
        "focus": {
            "ring": dim(email_focus["outlineWidth"], src_auth + " focused email outlineWidth. outlineColor is transparent; the visible ring is the box-shadow."),
            "offset": dim("2px", src_auth + " focused email box-shadow starts with rgb(250, 250, 250) 0px 0px 0px 2px."),
        },
    },
    "light": semantic(root, ":root", True),
    "dark": semantic(dark, ".dark", False),
    "$themes": [
        {"id": "light", "name": "light", "selectedTokenSets": {"core": "source", "light": "enabled"}},
        {"id": "dark", "name": "dark", "selectedTokenSets": {"core": "source", "dark": "enabled"}},
    ],
}

# Fix the paper/ink sources so they stay hex from the same converter.
tokens["core"]["color"]["ink"]["$value"] = "#1a1a1a"
tokens["core"]["color"]["ink"]["$extensions"]["authored"] = "rgb(26, 26, 26)"
tokens["core"]["color"]["paper"]["$value"] = "#fafafa"
tokens["core"]["color"]["paper"]["$extensions"]["authored"] = "rgb(250, 250, 250)"
tokens["core"]["color"]["white"]["$value"] = "#ffffff"
tokens["core"]["color"]["muted"]["$value"] = hsl_to_hex(root["--muted-foreground"])

# Semantic aliases the catalog-shaped roles can point at, as extra groups.
tokens["light"]["text"] = {
    "primary": {"$type": "color", "$value": "{color.foreground}", "$extensions": {"source": "alias of light.color.foreground", "evidence": "Derived"}},
    "muted": {"$type": "color", "$value": "{color.muted-foreground}", "$extensions": {"source": "alias of light.color.muted-foreground", "evidence": "Derived"}},
    "onAccent": {"$type": "color", "$value": "{color.primary-foreground}", "$extensions": {"source": "alias of light.color.primary-foreground", "evidence": "Derived"}},
}
tokens["light"]["background"] = {
    "page": {"$type": "color", "$value": "{color.background}", "$extensions": {"source": "alias of light.color.background", "evidence": "Derived"}},
    "surface": {"$type": "color", "$value": "{color.card}", "$extensions": {"source": "alias of light.color.card", "evidence": "Derived"}},
}
tokens["light"]["border"] = {
    "default": {"$type": "color", "$value": "{color.border}", "$extensions": {"source": "alias of light.color.border", "evidence": "Derived"}},
}
tokens["dark"]["text"] = {
    "primary": {"$type": "color", "$value": "{color.foreground}", "$extensions": {"source": "alias of dark.color.foreground. Not seen on a public page.", "evidence": "Derived"}},
    "muted": {"$type": "color", "$value": "{color.muted-foreground}", "$extensions": {"source": "alias of dark.color.muted-foreground. Not seen on a public page.", "evidence": "Derived"}},
    "onAccent": {"$type": "color", "$value": "{color.primary-foreground}", "$extensions": {"source": "alias of dark.color.primary-foreground. Not seen on a public page.", "evidence": "Derived"}},
}
tokens["dark"]["background"] = {
    "page": {"$type": "color", "$value": "{color.background}", "$extensions": {"source": "alias of dark.color.background. Not seen on a public page.", "evidence": "Derived"}},
    "surface": {"$type": "color", "$value": "{color.card}", "$extensions": {"source": "alias of dark.color.card. Not seen on a public page.", "evidence": "Derived"}},
}
tokens["dark"]["border"] = {
    "default": {"$type": "color", "$value": "{color.border}", "$extensions": {"source": "alias of dark.color.border. Not seen on a public page.", "evidence": "Derived"}},
}

# Record controls that are not tokens.
tokens["$extensions"] = {
    "notTokenised": {
        "button.primary.fill": painted(start, "backgroundColor"),
        "button.secondary.fill": painted(see, "backgroundColor"),
        "button.google.fill": painted(google, "backgroundColor"),
        "field.focus.shadow": email_focus["boxShadow"],
        "display.letterSpacing": h1["letterSpacing"],
        "note": "Primary buttons use the foreground ink as a fill. There is no second brand hue on the public site. Chart greens in the marketing demo are images, not tokens.",
    }
}

# Walk aliases and colours.
def walk(node, path=""):
    if isinstance(node, dict) and "$value" in node:
        val = node["$value"]
        typ = node.get("$type")
        if typ == "color" and isinstance(val, str) and not val.startswith("{"):
            if not re.fullmatch(r"#[0-9a-f]{6}", val):
                raise SystemExit(f"{path} colour {val}")
        if typ == "dimension" and not re.fullmatch(r"-?\d*\.?\d+(px|rem)", str(val)):
            raise SystemExit(f"{path} dimension {val}")
        if "source" not in node.get("$extensions", {}):
            raise SystemExit(f"{path} missing source")
        return
    if isinstance(node, dict):
        for k, v in node.items():
            if k.startswith("$"):
                continue
            walk(v, path + "." + k)

walk(tokens)
(HERE / "tokens.json").write_text(json.dumps(tokens, indent=2) + "\n")
print("wrote", HERE / "tokens.json")
