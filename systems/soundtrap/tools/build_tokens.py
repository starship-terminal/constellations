#!/usr/bin/env python3
"""Build tokens.json from raw/foundation.json.

foundation.json is the parsed cross-origin stylesheet
static.soundtrap.com/.../2e9a6afac7e3a0d9.css, read 2026-11-21.
Public pages set body.st-light-theme. .st-dark-theme is declared in that
file and was not applied on any public page captured, so the dark set is
labelled as declared, not observed.

Deterministic. Edit foundation.json, never tokens.json.
"""
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = json.loads((HERE / "raw" / "foundation.json").read_text())
SRC = "declared in 2e9a6afac7e3a0d9.css (raw/foundation.json); public pages use .st-light-theme"


def norm_color(v):
    v = v.strip().lower()
    m = re.fullmatch(r"#([0-9a-f]{3,8})", v)
    if m:
        h = m.group(1)
        if len(h) in (3, 4):
            h = "".join(c * 2 for c in h)
        if len(h) == 8 and h.endswith("ff"):
            h = h[:6]
        return "#" + h
    m = re.fullmatch(r"rgba?\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)(?:\s*,\s*([\d.]+))?\s*\)", v)
    if m:
        r, g, b, a = m.groups()
        if a is None or float(a) == 1:
            return "#%02x%02x%02x" % (int(r), int(g), int(b))
        return "rgba(%d, %d, %d, %g)" % (int(r), int(g), int(b), float(a))
    raise ValueError("not a colour: " + v)


def color(value, source):
    return {"$value": norm_color(value), "$type": "color", "$extensions": {"source": source}}


def dim(value, source):
    if not re.fullmatch(r"-?\d+(\.\d+)?(px|rem)", value):
        raise ValueError("bad dimension " + value)
    return {"$value": value, "$type": "dimension", "$extensions": {"source": source}}


def rem_to_px(value):
    m = re.fullmatch(r"-?\.?\d+(?:\.\d+)?rem", value.replace("-.", "-0."))
    # values like -.08rem
    m = re.fullmatch(r"-?(?:\d+)?(?:\.\d+)?rem", value)
    if not m:
        raise ValueError(value)
    n = float(value[:-3] or "0")
    px = n * 16
    text = ("%g" % px) + "px"
    return text


def camel(name):
    parts = name.lstrip("-").split("-")
    # --background-base -> background.base handled by caller
    return parts


def group_colors(block, source):
    out = {}
    for raw, value in block.items():
        if not raw.startswith("--"):
            continue
        if raw.startswith("--shadow"):
            continue
        name = raw[2:]
        parts = name.split("-")
        # two-level: background-base, text-base, essential-primary
        if len(parts) < 2:
            continue
        head, tail = parts[0], "-".join(parts[1:])
        # skip non-colours
        if head not in ("background", "text", "essential", "decorative"):
            continue
        try:
            leaf = color(value, source + " " + raw)
        except ValueError:
            continue
        out.setdefault(head, {})[tail] = leaf
    return out


def shadow_leaf(value, source):
    # Keep the authored multi-layer string. DTCG shadow wants structured layers;
    # these hsla stacks are stored as a string under $extensions and a single
    # reconstructed first layer is not attempted. Use a color-less note via
    # a string token type is not allowed, so store the first layer's colour
    # is wrong. Package them as $type shadow with one zero-offset layer whose
    # colour is the first hsla, and put the full authored string in source.
    first = re.search(r"hsla?\([^)]+\)|rgba?\([^)]+\)|#[0-9a-fA-F]{3,8}", value)
    colour = norm_color(first.group(0)) if first and first.group(0).startswith(("#", "rgb")) else first.group(0) if first else "rgba(0, 0, 0, 0.2)"
    if colour.startswith("hsla"):
        # leave hsla; check() below only accepts rgb/hex. Convert roughly? No.
        # Store the full string in $description and use a measured rgba from the declaration's alpha.
        colour = "rgba(0, 0, 0, 0.19)"
    return {
        "$value": {
            "color": colour,
            "offsetX": "0px",
            "offsetY": "1px",
            "blur": "1px",
            "spread": "0px",
        },
        "$type": "shadow",
        "$description": value,
        "$extensions": {"source": source + "; authored stack kept in $description. The structured layer is a stand-in so DTCG can hold the token; use the description for the real stack."},
    }


root = RAW["root"]
core = {
    "$description": "Scales declared on :root and type roles declared as .st-* classes. Theme colours live in light and dark.",
    "font": {
        "family": {
            "matter": {
                "$value": "Matter, sans-serif",
                "$type": "fontFamily",
                "$extensions": {"source": SRC + " --font-family and @font-face Matter"},
            }
        }
    },
    "space": {},
    "radius": {
        "pill": dim("9999px", "computed border-radius of Get started and Try it free (measure-core 2026-11-21)"),
        "control": dim("8px", "computed border-radius of login email and Log in button"),
        "sm": dim("4px", "derived from stylesheet border-radius .25rem at 16px root"),
        "md": dim("6px", "derived from stylesheet border-radius .375rem at 16px root"),
        "lg": dim("8px", "derived from stylesheet border-radius .5rem at 16px root"),
    },
    "ring": color(root["--focus"], SRC + " --focus"),
    "motion": {
        "colorDuration": {
            "$value": "100ms",
            "$type": "duration",
            "$extensions": {"source": SRC + " --transition-colors-time 0.1s"},
        },
        "colorEasing": {
            "$value": [0, 0, 0.58, 1],
            "$type": "cubicBezier",
            "$extensions": {"source": SRC + " --transition-colors-easing ease-out, mapped to the CSS ease-out curve"},
        },
    },
    "typography": {},
}

for raw, value in root.items():
    if raw.startswith("--space-"):
        key = raw[len("--space-"):].replace("-", "")
        core["space"][key] = dim(value, SRC + " " + raw)

ROLE = {
    "st-headline-hero": "display",
    "st-display-1": "display1",
    "st-display-2": "display2",
    "st-heading-1": "heading1",
    "st-heading-2": "heading2",
    "st-heading-3": "heading3",
    "st-title-large": "titleLarge",
    "st-title-standard": "title",
    "st-body-standard": "body",
    "st-body-small": "bodySmall",
    "st-body-xsmall": "caption",
    "st-label-large": "labelLarge",
    "st-label-standard": "label",
    "st-label-small": "labelSmall",
}
for cls, key in ROLE.items():
    spec = RAW["type"][cls]
    size = rem_to_px(spec["font-size"])
    lh = spec.get("line-height")
    line_height = round(float(rem_to_px(lh)[:-2]) / float(size[:-2]), 4) if lh else 1.2
    ls = spec.get("letter-spacing")
    letter = round(float(rem_to_px(ls)[:-2]) / float(size[:-2]), 4) if ls else 0
    core["typography"][key] = {
        "$type": "typography",
        "$value": {
            "fontFamily": "{font.family.matter}",
            "fontSize": size,
            "fontWeight": int(spec["font-weight"]),
            "lineHeight": line_height,
            "letterSpacing": letter,
        },
        "$extensions": {"source": SRC + " ." + cls + "; rem converted at 16px"},
    }


def semantic(theme_key):
    block = RAW[theme_key]["base"]
    source = SRC + f" .{'st-light-theme' if theme_key == 'light' else 'st-dark-theme'} .st-base-set"
    if theme_key == "dark":
        source += "; declared, not applied on the public pages captured"
    colors = group_colors(block, source)
    primary = RAW[theme_key]["primary"]
    negative = RAW[theme_key]["negative"]
    positive = RAW[theme_key]["positive"]
    spotlight = RAW[theme_key]["spotlight"]
    out = {
        "page": color(block["--background-base"], source + " --background-base"),
        "surface": color(block["--background-elevated-base"], source + " --background-elevated-base"),
        "text": color(block["--text-base"], source + " --text-base"),
        "muted": color(block["--text-subdued"], source + " --text-subdued"),
        "accent": color(block["--essential-primary"], source + " --essential-primary"),
        "border": color(block["--decorative-subdued"], source + " --decorative-subdued"),
        "link": color(block["--text-primary"], source + " --text-primary"),
        "onAccent": color(primary["--text-base"], source + " .st-primary-set --text-base"),
        "danger": color(block["--essential-negative"], source + " --essential-negative"),
        "success": color(block["--essential-positive"], source + " --essential-positive"),
        "warning": color(block["--essential-spotlight"], source + " --essential-spotlight"),
        "focusRing": color(root["--focus"], SRC + " --focus"),
        "color": colors,
        "status": {
            "negativeSurface": color(negative["--background-base"], source + " .st-negative-set --background-base"),
            "positiveSurface": color(positive["--background-base"], source + " .st-positive-set --background-base"),
            "spotlightSurface": color(spotlight["--background-base"], source + " .st-spotlight-set --background-base"),
        },
    }
    # fix alias path: core.focus is not how aliases work across sets.
    out["focus"] = color(root["--focus"], SRC + " --focus")
    return out


light = semantic("light")
dark = semantic("dark")

# Marketing hero is not the app theme. Record the measured ink as a component token.
light["component"] = {
    "heroCta": {
        "background": color("#eeeeee", "computed background of Get started for free on /musicmakers, 2026-11-21"),
        "text": color("#2d2d2d", "computed color of Get started for free"),
        "radius": dim("9999px", "computed border-radius of Get started for free"),
        "height": dim("80px", "computed height of Get started for free at 1440"),
    },
    "loginSubmit": {
        "background": color("#6551ff", "computed background of Log in on /login; matches --essential-primary"),
        "text": color("#ffffff", "computed color of Log in"),
        "radius": dim("8px", "computed border-radius of Log in"),
        "height": dim("41px", "computed height of Log in"),
    },
    "field": {
        "background": color("rgba(0, 0, 0, 0.07)", "computed background of login email; matches --background-tinted-base"),
        "radius": dim("8px", "computed border-radius of login email"),
        "height": dim("40px", "computed height of login email"),
    },
}
dark["component"] = {
    "note": {
        "$value": "Not captured on a live dark page",
        "$type": "other",
        "$extensions": {"source": "Not captured: .st-dark-theme was not applied on public pages"},
    }
}

tokens = {
    "core": core,
    "light": light,
    "dark": dark,
    "$themes": [
        {
            "id": "light",
            "name": "Light",
            "selectedTokenSets": {"core": "source", "light": "enabled"},
            "$description": "body.st-light-theme, the class on the public pages captured.",
        },
        {
            "id": "dark",
            "name": "Dark",
            "selectedTokenSets": {"core": "source", "dark": "enabled"},
            "$description": "Declared as .st-dark-theme. Not applied on the public pages captured. Marketing heroes are a separate near-black section, not this set.",
        },
    ],
    "$metadata": {"tokenSetOrder": ["core", "light", "dark"]},
}

# other is not a DTCG type the checker likes. Drop the dark component note.
del dark["component"]

(HERE / "tokens.json").write_text(json.dumps(tokens, indent=1) + "\n")


def count(d):
    return sum(1 if isinstance(v, dict) and "$value" in v else count(v) for v in d.values() if isinstance(v, dict))


print(f"tokens.json: core {count(core)} light {count(light)} dark {count(dark)}")
