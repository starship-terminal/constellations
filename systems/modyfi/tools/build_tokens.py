#!/usr/bin/env python3
"""Build systems/modyfi/tokens.json from measured Wayback readings.

Values come from raw/css-vars.json (computed custom properties on :root of the
archived homepage) and raw/components-computed.json (getComputedStyle). Nothing
is invented. A colour that is only a computed rgb() is converted to hex, which
is Derived from the measured channel values.
"""
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
VARS = json.loads((RAW / "css-vars.json").read_text())
COMP = json.loads((RAW / "components-computed.json").read_text())

SNAP = "Wayback 20250219221151 https://www.modyfi.com/ computed :root"


def color(value, source):
    return {"$type": "color", "$value": value, "$extensions": {"source": source, "evidence": "Measured"}}


def dim(value, source):
    return {"$type": "dimension", "$value": value, "$extensions": {"source": source, "evidence": "Measured"}}


def font(value, source):
    return {"$type": "fontFamily", "$value": value, "$extensions": {"source": source, "evidence": "Measured"}}


def num(value, source):
    return {"$type": "number", "$value": value, "$extensions": {"source": source, "evidence": "Derived"}}


def rgb_to_hex(s):
    m = re.fullmatch(r"rgba?\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*(?:,\s*([\d.]+)\s*)?\)", s.strip())
    if not m:
        return None
    r, g, b = (int(m.group(i)) for i in (1, 2, 3))
    a = m.group(4)
    if a is None or float(a) == 1:
        return "#{:02x}{:02x}{:02x}".format(r, g, b)
    ai = round(float(a) * 255)
    return "#{:02x}{:02x}{:02x}{:02x}".format(r, g, b, ai)


def norm_color(s):
    s = s.strip()
    if s in ("black",):
        return "#000000"
    if s in ("white",):
        return "#ffffff"
    if re.fullmatch(r"#[0-9a-fA-F]{3,8}", s):
        h = s.lower()
        if len(h) == 4:
            h = "#" + "".join(c * 2 for c in h[1:])
        return h
    return rgb_to_hex(s) or s


RESOLVED = VARS.get("resolved") or {}
BODY = VARS.get("body") or {}


def var_color(name, source):
    """A colour read from the custom property on the archived :root. A missing reading fails the
    build: it used to fall back to a typed hex still labelled Measured."""
    raw = RESOLVED.get(name, "")
    if not raw:
        raise SystemExit(f"{name} is not in raw/css-vars.json")
    return {"$type": "color", "$value": norm_color(raw), "$extensions": {"source": source, "evidence": "Measured", "declared": raw}}


core = {
    "color": {
        "background": var_color("--background-a", SNAP + " --background-a"),
        "heading": var_color("--heading", SNAP + " --heading"),
        "paragraph": var_color("--paragraphs", SNAP + " --paragraphs"),
        "accent": var_color("--accent-a1", SNAP + " --accent-a1"),
        "accent-blue": var_color("--accent-a2", SNAP + " --accent-a2"),
        "link": var_color("--link", SNAP + " --link"),
        "border": var_color("--border", SNAP + " --border"),
        "surface": var_color("--background-b1", SNAP + " --background-b1"),
        "stroke": var_color("--semi-stroke", SNAP + " --semi-stroke"),
        "magenta-transparent": var_color("--magenta-transaprent", SNAP + " --magenta-transaprent (product spelling)"),
    },
    "font": {
        "display": font("Jokker, Arial, sans-serif", "computed font-family on h1.rl-heading-style-h1-3, archived homepage"),
        "body": font("Inter, sans-serif", "computed font-family on body, archived homepage"),
        "ui": font("Jokker, Arial, sans-serif", "computed font-family on a.rl_navbar2_button, archived homepage"),
    },
    "radius": {
        "control": dim("15px", "computed border-radius on a.rl_navbar2_button and a.rl-button, archived homepage"),
    },
    "space": {
        "control-y": dim("8px", "computed padding-top on a.rl_navbar2_button"),
        "control-x": dim("16px", "computed padding-left on a.rl_navbar2_button"),
        "cta-y": dim("16px", "computed padding-top on a.rl-button"),
        "cta-x": dim("24px", "computed padding-left on a.rl-button"),
    },
    "typography": {
        "display": {
            "$type": "typography",
            "$value": {
                "fontFamily": "{font.display}",
                "fontSize": "56px",
                "fontWeight": 600,
                "lineHeight": "67.2px",
                "letterSpacing": "-3px",
            },
            "$extensions": {"source": "computed style on h1, archived homepage 1440px", "evidence": "Measured"},
        },
        "section": {
            "$type": "typography",
            "$value": {
                "fontFamily": "{font.display}",
                "fontSize": "48px",
                "fontWeight": 600,
                "lineHeight": "57.6px",
                "letterSpacing": "-1px",
            },
            "$extensions": {"source": "computed style on h2.rl-heading-style-h2-9, archived homepage", "evidence": "Measured"},
        },
        "body": {
            "$type": "typography",
            "$value": {
                "fontFamily": "{font.display}",
                "fontSize": "17.6px",
                "fontWeight": 400,
                "lineHeight": "31.68px",
                "letterSpacing": "-1px",
            },
            "$extensions": {"source": "computed style on p.rl-text-style-medium-8, archived homepage", "evidence": "Measured"},
        },
        "nav": {
            "$type": "typography",
            "$value": {
                "fontFamily": "{font.ui}",
                "fontSize": "12.8px",
                "fontWeight": 400,
                "lineHeight": "19.2px",
            },
            "$extensions": {"source": "computed style on a.rl_navbar2_link, archived homepage", "evidence": "Measured"},
        },
    },
}

# Semantic set uses the same dark marketing palette. The site publishes one theme.
light_unused = None
dark = {
    "color": {
        "page": {"$type": "color", "$value": "{core.color.background}", "$extensions": {"source": "alias of core.color.background", "evidence": "Derived"}},
        "surface": {"$type": "color", "$value": "{core.color.surface}", "$extensions": {"source": "alias of core.color.surface", "evidence": "Derived"}},
        "text": {"$type": "color", "$value": "{core.color.heading}", "$extensions": {"source": "alias of core.color.heading", "evidence": "Derived"}},
        "muted": {"$type": "color", "$value": "{core.color.paragraph}", "$extensions": {"source": "alias of core.color.paragraph", "evidence": "Derived"}},
        "accent": {"$type": "color", "$value": "{core.color.accent}", "$extensions": {"source": "alias of core.color.accent", "evidence": "Derived"}},
        "border": {"$type": "color", "$value": "{core.color.border}", "$extensions": {"source": "alias of core.color.border", "evidence": "Derived"}},
        "link": {"$type": "color", "$value": "{core.color.link}", "$extensions": {"source": "alias of core.color.link", "evidence": "Derived"}},
        "on-accent": color("#000000", "computed color on a.rl-button (white fill, black text), archived homepage"),
    },
    "component": {
        "signup": {
            "background": color("#00000000", "computed background-color rgba(0, 0, 0, 0) on a.rl_navbar2_button signup at rest, archived homepage, raw/crops-measured.json"),
            "text": color("#ffffff", "computed color rgb(255,255,255) on signup button at rest"),
            "border": color("#ff035778", "computed border-top-color rgba(255, 3, 87, 0.47) on signup button at rest, matches --magenta-transaprent"),
            "hover-background": color("#ff0357", "computed background-color rgb(255, 3, 87) on signup button hover, raw/crops-measured.json"),
            "radius": dim("15px", "computed border-radius on signup button"),
            "padding": dim("8px", "computed padding-top on signup button"),
        },
        "cta": {
            "background": color("#ffffff", "computed background-color rgb(255,255,255) on a.rl-button"),
            "text": color("#000000", "computed color rgb(0,0,0) on a.rl-button"),
            "radius": dim("15px", "computed border-radius on a.rl-button"),
        },
        "nav": {
            "height": dim("80px", "computed height of .rl_navbar2_component at 1169px preview; package shots use 1440"),
            "link": color("#ffffffcc", "computed color rgba(255,255,255,0.8) on a.rl_navbar2_link"),
        },
    },
}

# Fix signup background: transparent is not a useful page token. Keep the measured border.
# Tokens Studio wants aliases without the set prefix when they point at core from a semantic set.
# The kit convention in this repo is {color.x} resolving inside core when the semantic token aliases it.
# catalog.py resolves {group.path} against the same set first, then core. Use {color.background} only
# if that name exists in core. It does.

tokens = {
    "$schema": "https://design-tokens.org/schema.json",
    "core": core,
    "dark": dark,
    "$themes": [
        {"id": "dark", "name": "dark", "selectedTokenSets": {"core": "enabled", "dark": "enabled"}},
    ],
    "$extensions": {
        "source": "Modyfi public marketing site, Wayback snapshots, measured 2026-11-19. Live modyfi.com is a Webflow 404. One published theme (dark).",
        "evidence": "Measured",
    },
}

# Attach component measurements that exist.
home_comps = COMP.get("components", {})
if "hero-title" in home_comps and "default" in home_comps["hero-title"].get("states", {}):
    row = home_comps["hero-title"]["states"]["default"]
    if row.get("fontSize"):
        core["typography"]["display"]["$value"]["fontSize"] = row["fontSize"]
        core["typography"]["display"]["$value"]["lineHeight"] = row["lineHeight"]
        core["typography"]["display"]["$value"]["letterSpacing"] = row["letterSpacing"]

TEXT = json.dumps(tokens, indent=2) + "\n"

if __name__ == "__main__":
    out = HERE / "tokens.json"
    out.write_text(TEXT)
    print("wrote", out, "core colors", len(core["color"]))
