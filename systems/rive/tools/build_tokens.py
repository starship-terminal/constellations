#!/usr/bin/env python3
"""Build tokens.json from raw/css-vars.json and the computed-style readings in raw/computed.json.

rive.app marketing paints one dark theme. Framer declares --token-<uuid> colours on body.
Readable names are assigned here from the resolved sRGB value. Every leaf carries
$extensions.source. Edit the raw files, never tokens.json.
"""
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
V = json.loads((RAW / "css-vars.json").read_text())
C = json.loads((RAW / "computed.json").read_text())
DECL = {n: v.get("value", v.get("raw")) for n, v in V["resolved"]["light"].items()}

# First uuid that resolves to each colour. Names follow what the site paints.
PALETTE = {
    "#000000": "ink.950",
    "#0c0c0c": "ink.900",
    "#0d0d0c": "ink.850",
    "#121212": "ink.800",
    "#171717": "ink.700",
    "#181818": "ink.650",
    "#1d1d1d": "ink.600",
    "#222222": "ink.500",
    "#333333": "ink.400",
    "#555555": "ink.300",
    "#666666": "ink.250",
    "#aaaaaa": "ink.200",
    "#a1a1aa": "ink.150",
    "#f2f0f0": "ink.50",
    "#ffffff": "ink.0",
    "rgba(0, 0, 0, 0.1)": "black-alpha.10",
    "#ffa41c": "signal.amber",
    "#ff483c": "signal.red",
    "#f30058": "signal.magenta",
    "#3084ff": "signal.blue",
    "#19f2ff": "signal.cyan",
    "#71ff19": "signal.lime",
}

# uuid of the first declaration for each resolved value
SEEN = {}
for name, val in DECL.items():
    if not name.startswith("--token-"):
        continue
    if val not in SEEN:
        SEEN[val] = name

unmapped = [f"{v} {n}" for n, v in ((k, DECL[k]) for k in DECL if k.startswith("--token-")) if v not in PALETTE and v not in SEEN]
# duplicates are fine; unmapped values are not
missing = sorted({DECL[n] for n in DECL if n.startswith("--token-") and DECL[n] not in PALETTE})
if missing:
    raise SystemExit("unmapped token colours: " + ", ".join(missing))


def color(value, source):
    return {"$value": value, "$type": "color", "$extensions": {"source": source}}


def dim(value, source):
    if not re.fullmatch(r"-?\d+(\.\d+)?px", value):
        raise ValueError(value)
    return {"$value": value, "$type": "dimension", "$extensions": {"source": source}}


def num(value, source, ty="number"):
    return {"$value": value, "$type": ty, "$extensions": {"source": source}}


core_color = {}
for val, path in PALETTE.items():
    node = core_color
    parts = path.split(".")
    for p in parts[:-1]:
        node = node.setdefault(p, {})
    src = "css-var " + SEEN[val] + " on body (raw/css-vars.json resolved.light)"
    node[parts[-1]] = color(val, src)

H = C["home"]
core = {
    "color": core_color,
    "font": {
        "display": {
            "$value": H["h1"]["font"], "$type": "fontFamily",
            "$extensions": {"source": "computed fontFamily of h1 on https://rive.app/ (raw/computed.json home.h1)"},
        },
        "ui": {
            "$value": H["navBtn"]["font"], "$type": "fontFamily",
            "$extensions": {"source": "computed fontFamily of button.rn-top PRODUCTS (raw/computed.json home.navBtn)"},
        },
        "mono": {
            "$value": H["cta"]["font"], "$type": "fontFamily",
            "$extensions": {"source": "computed fontFamily of header GET STARTED (raw/computed.json home.cta)"},
        },
    },
    "typography": {
        "display": {
            "$value": {
                "fontFamily": "{font.display}",
                "fontSize": H["h1"]["size"],
                "fontWeight": int(H["h1"]["weight"]),
                "lineHeight": round(float(H["h1"]["lh"].replace("px", "")) / float(H["h1"]["size"].replace("px", "")), 3),
                "letterSpacing": H["h1"]["ls"],
            },
            "$type": "typography",
            "$extensions": {"source": "computed style of h1 on https://rive.app/ at 1440x900 (raw/computed.json home.h1)"},
        },
        "heading": {
            "$value": {
                "fontFamily": "{font.display}",
                "fontSize": H["h2"]["size"],
                "fontWeight": int(H["h2"]["weight"]),
                "lineHeight": round(float(H["h2"]["lh"].replace("px", "")) / float(H["h2"]["size"].replace("px", "")), 3),
            },
            "$type": "typography",
            "$extensions": {"source": "computed style of first h2 on https://rive.app/ (raw/computed.json home.h2)"},
        },
        "label": {
            "$value": {
                "fontFamily": "{font.ui}",
                "fontSize": H["navBtn"]["size"],
                "fontWeight": int(H["navBtn"]["weight"]),
                "letterSpacing": H["navBtn"]["ls"],
            },
            "$type": "typography",
            "$extensions": {"source": "computed style of button.rn-top (raw/computed.json home.navBtn)"},
        },
        "mono-label": {
            "$value": {
                "fontFamily": "{font.mono}",
                "fontSize": H["cta"]["size"],
                "fontWeight": int(H["cta"]["weight"]),
                "lineHeight": round(float(H["cta"]["lh"].replace("px", "")) / float(H["cta"]["size"].replace("px", "")), 3),
                "letterSpacing": H["cta"]["ls"],
            },
            "$type": "typography",
            "$extensions": {"source": "computed style of header GET STARTED (raw/computed.json home.cta)"},
        },
    },
    "radius": {
        "control": dim(H["cta"]["radius"], "computed borderRadius of header GET STARTED (raw/computed.json home.cta)"),
    },
    "space": {
        "cta-x": dim("9px", "computed padding-left of header GET STARTED, 5px 9px 6px (raw/computed.json home.cta.pad)"),
        "cta-y": dim("5px", "computed padding-top of header GET STARTED (raw/computed.json home.cta.pad)"),
    },
}

dark = {
    "page": color("#000000", "computed backgroundColor of body on https://rive.app/ (raw/computed.json home.body); same value as core.color.ink.950"),
    "surface": color("#1d1d1d", "computed backgroundColor of pricing GET STARTED card control (raw/computed.json pricing.getStarted); same value as core.color.ink.600"),
    "text": color("#ffffff", "computed color of h1 (raw/computed.json home.h1); same value as core.color.ink.0"),
    "muted": color("rgba(255, 255, 255, 0.85)", "computed color of header PRICING link and button.rn-top (raw/computed.json home.pricing, home.navBtn)"),
    "muted-2": color("#aaaaaa", "computed color of MONTHLY label on /pricing (raw/computed.json pricing.monthly); same value as core.color.ink.200"),
    "on-accent": color("#000000", "computed color of header GET STARTED on white fill (raw/computed.json home.cta)"),
    "accent": color("#ffffff", "computed backgroundColor of header GET STARTED (raw/computed.json home.cta); same value as core.color.ink.0"),
    "border": color("rgba(255, 255, 255, 0.1)", "computed boxShadow inset ring of header GET STARTED, rgba(255, 255, 255, 0.1) 0px 0px 0px 1px inset (raw/computed.json home.cta.shadow)"),
    "link": color("rgba(255, 255, 255, 0.85)", "computed color of header nav anchors (raw/computed.json home.pricing)"),
    "heading": color("#f1f1f1", "computed color of first h2 (raw/computed.json home.h2)"),
    "focus": {
        "$value": "Not captured",
        "$extensions": {"source": "Not captured. Keyboard focus ring was not read as a stable computed outline on the marketing controls in this pass."},
    },
    "component": {
        "header": {
            "height": dim(str(H["navBtn"]["h"]) + "px", "computed height of button.rn-top at 1440x900 (raw/computed.json home.navBtn)"),
        },
        "cta": {
            "height": dim(str(H["cta"]["h"]) + "px", "computed height of header GET STARTED (raw/computed.json home.cta)"),
            "radius": dim(H["cta"]["radius"], "computed borderRadius of header GET STARTED"),
            "padding": {
                "$value": H["cta"]["pad"],
                "$extensions": {"source": "computed padding of header GET STARTED (raw/computed.json home.cta.pad). Not a single length, so it is not a dimension token."},
            },
        },
        "copy": {
            "height": dim(str(H["copy"]["h"]) + "px", "computed height of COPY button (raw/computed.json home.copy)"),
            "border": {
                "$value": H["copy"]["border"],
                "$extensions": {"source": "computed border of COPY button (raw/computed.json home.copy.border). A border shorthand, not a single colour token."},
            },
        },
    },
}

# fix font leaves that used a mistaken helper
# already written correctly above

tokens = {
    "core": core,
    "dark": dark,
    "$themes": [{
        "id": "dark",
        "name": "Dark",
        "selectedTokenSets": {"core": "source", "dark": "enabled"},
        "$description": "The only theme the rive.app marketing pages paint. Docs ship html.dark and a theme preference control; a light docs theme was not applied.",
    }],
    "$metadata": {"tokenSetOrder": ["core", "dark"]},
}

# drop the bogus font helper if any
(HERE / "tokens.json").write_text(json.dumps(tokens, indent=2, ensure_ascii=False) + "\n")
print("wrote", HERE / "tokens.json")
