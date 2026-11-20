#!/usr/bin/env python3
"""Build tokens.json from raw/css-vars.json.

Every colour, length, shadow and font below is a computed custom property
read from documentElement on the signed-out Washington Post homepage
(headed Chrome, 1440x900, 2026-11-21). The site paints one light theme.
A dark set is not invented.

Deterministic. Edit the raw file, never tokens.json.
"""
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = json.loads((HERE / "raw" / "css-vars.json").read_text())
V = RAW["root"]
WHEN = "computed on documentElement, washingtonpost.com homepage, headed Chrome, 2026-11-21"


def norm_color(v):
    v = v.strip()
    m = re.fullmatch(r"#([0-9a-fA-F]{3,8})", v)
    if m:
        h = m.group(1).lower()
        if len(h) in (3, 4):
            h = "".join(c * 2 for c in h)
        r, g, b = (int(h[i:i + 2], 16) for i in (0, 2, 4))
        if len(h) == 8 and h[6:] != "ff":
            a = round(int(h[6:8], 16) / 255, 3)
            return "rgba(%d, %d, %d, %g)" % (r, g, b, a)
        return "#%02x%02x%02x" % (r, g, b)
    m = re.fullmatch(r"rgba?\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*(?:,\s*([\d.]+))?\s*\)", v.replace(" ", ""))
    if not m:
        m = re.fullmatch(r"rgba?\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*(?:,\s*([\d.]+))?\s*\)", v)
    if m:
        r, g, b, a = m.groups()
        if a is None or float(a) == 1:
            return "#%02x%02x%02x" % (int(r), int(g), int(b))
        return "rgba(%d, %d, %d, %g)" % (int(r), int(g), int(b), float(a))
    raise ValueError("not a colour: " + v)


def color(name, desc):
    return {
        "$value": norm_color(V[name]),
        "$type": "color",
        "$description": desc,
        "$extensions": {"source": f"Measured. {name} {WHEN}. raw/css-vars.json"},
    }


def dim(name, desc):
    val = V[name].strip()
    if not re.fullmatch(r"-?\d+(\.\d+)?(px|rem)", val):
        raise ValueError(f"{name} is not a dimension: {val}")
    return {
        "$value": val,
        "$type": "dimension",
        "$description": desc,
        "$extensions": {"source": f"Measured. {name} {WHEN}. raw/css-vars.json"},
    }


def font(name, desc):
    return {
        "$value": V[name].strip(),
        "$type": "fontFamily",
        "$description": desc,
        "$extensions": {"source": f"Measured. {name} {WHEN}. raw/css-vars.json"},
    }


def weight(name, desc):
    return {
        "$value": int(V[name]),
        "$type": "fontWeight",
        "$description": desc,
        "$extensions": {"source": f"Measured. {name} {WHEN}. raw/css-vars.json"},
    }


def number(name, desc):
    return {
        "$value": float(V[name]) if "." in V[name] else int(V[name]),
        "$type": "number",
        "$description": desc,
        "$extensions": {"source": f"Measured. {name} {WHEN}. raw/css-vars.json"},
    }


def duration(name, desc):
    val = V[name].strip()
    if not re.fullmatch(r"\d+(\.\d+)?s", val):
        raise ValueError(val)
    ms = int(round(float(val[:-1]) * 1000))
    return {
        "$value": f"{ms}ms",
        "$type": "duration",
        "$description": desc,
        "$extensions": {"source": f"Derived. {name} is {val}; stored as {ms}ms. {WHEN}."},
    }


def shadow(name, desc):
    # "0px 1px 2px 0px rgba(0, 0, 0, 0.15)"
    raw = V[name].strip()
    m = re.fullmatch(
        r"(-?\d+px)\s+(-?\d+px)\s+(-?\d+px)\s+(-?\d+px)\s+(.+)",
        raw,
    )
    if not m:
        raise ValueError("shadow " + raw)
    return {
        "$value": [{
            "color": norm_color(m.group(5)),
            "offsetX": m.group(1),
            "offsetY": m.group(2),
            "blur": m.group(3),
            "spread": m.group(4),
        }],
        "$type": "shadow",
        "$description": desc,
        "$extensions": {"source": f"Measured. {name} {WHEN}. raw/css-vars.json"},
    }


def alias(path, desc):
    return {
        "$value": path,
        "$type": "color",
        "$description": desc,
        "$extensions": {"source": f"Derived. Alias of a measured WPDS custom property. {WHEN}."},
    }


core = {
    "color": {
        "gray": {step: color(f"--wpds-colors-gray{step}", f"WPDS gray {step}.") for step in ("0", "20", "40", "60", "80", "100", "200", "300", "400", "500", "600", "700")},
        "blue": {step: color(f"--wpds-colors-blue{step}", f"WPDS blue {step}.") for step in ("40", "60", "80", "100", "200", "300", "400", "500", "600")},
        "red": {step: color(f"--wpds-colors-red{step}", f"WPDS red {step}.") for step in ("40", "60", "80", "100", "200")},
        "green": {step: color(f"--wpds-colors-green{step}", f"WPDS green {step}.") for step in ("40", "60", "80", "100")},
        "orange": {step: color(f"--wpds-colors-orange{step}", f"WPDS orange {step}.") for step in ("60", "80", "100", "200")},
        "spark": {step: color(f"--wpds-colors-spark{step}", f"WPDS spark {step}, the opinions orange.") for step in ("80", "100", "200")},
    },
    "font": {
        "headline": font("--wpds-fonts-headline", "Headline stack. Postoni is licensed and not distributed."),
        "body": font("--wpds-fonts-body", "Body stack."),
        "meta": font("--wpds-fonts-meta", "UI and meta stack. Franklin is licensed and not distributed."),
        "subhead": font("--wpds-fonts-subhead", "Subhead stack."),
        "weight": {
            "light": weight("--wpds-fontWeights-light", "Light."),
            "regular": weight("--wpds-fontWeights-regular", "Regular."),
            "bold": weight("--wpds-fontWeights-bold", "Bold."),
            "ultra": weight("--wpds-fontWeights-ultra", "Ultra."),
        },
        "size": {step: dim(f"--wpds-fontSizes-{step}", f"WPDS font size {step}.") for step in ("075", "087", "100", "112", "125", "150", "200", "300")},
        "lineHeight": {
            "headline": number("--wpds-lineHeights-headline", "Headline line height."),
            "body": number("--wpds-lineHeights-body", "Body line height."),
            "meta": number("--wpds-lineHeights-meta", "Meta line height."),
        },
    },
    "space": {step: dim(f"--wpds-space-{step}", f"WPDS space {step}.") for step in ("025", "050", "075", "100", "150", "200", "300")},
    "radius": {step: dim(f"--wpds-radii-{step}", f"WPDS radius {step}.") for step in ("012", "025", "050", "100", "round")},
    "shadow": {
        "card": shadow("--wpds-shadows-50", "Card lip."),
        "sm": shadow("--wpds-shadows-100", "Small elevation."),
        "md": shadow("--wpds-shadows-300", "Medium elevation."),
        "lg": shadow("--wpds-shadows-500", "Large elevation."),
    },
    "motion": {
        "fast": duration("--wpds-transitions-fast", "Fast duration."),
        "normal": duration("--wpds-transitions-normal", "Normal duration."),
    },
}

light = {
    "page": alias("{core.color.gray.700}", "Page background."),
    "surface": alias("{core.color.gray.600}", "Raised surface (background-forSurfaces)."),
    "text": alias("{core.color.gray.20}", "Primary text."),
    "muted": color("--wpds-colors-onBackground-subtle", "Secondary text."),
    "accent": color("--wpds-colors-cta", "Subscribe and CTA blue."),
    "accentHover": color("--wpds-colors-cta-hover", "CTA hover."),
    "onAccent": color("--wpds-colors-onCta", "Text on the CTA."),
    "border": color("--wpds-colors-outline", "Default outline."),
    "borderStrong": color("--secondary-border-color", "Strong border."),
    "focus": color("--nested-focus-within-color", "Nested focus colour."),
    "link": color("--blue", "Brand link blue."),
    "success": color("--wpds-colors-success", "Success."),
    "warning": color("--wpds-colors-warning", "Warning."),
    "danger": color("--wpds-colors-error", "Error."),
    "disabled": color("--wpds-colors-disabled", "Disabled fill."),
    "onDisabled": color("--wpds-colors-onDisabled", "Text on disabled."),
    "opinions": color("--wpds-colors-opinions", "Opinions section accent."),
    "scrim": color("--wpds-colors-gray0", "Scrim black. Overlay alpha was not measured as its own token."),
}

tokens = {
    "core": core,
    "light": light,
    "$themes": [{"id": "light", "name": "light", "selectedTokenSets": {"core": "source", "light": "enabled"}}],
    "$extensions": {
        "notTokenised": [
            "Dark theme: the public site paints color-scheme normal and exposes no theme toggle. Not captured.",
            "Pressed, disabled and error control states were not held on a public control. Not captured.",
            "Info colour: WPDS publishes success, warning and error. No info role was read. Not captured.",
            "Easing as a cubicBezier token: --wpds-transitions-inOut was read as cubic-bezier(.4, 0, .2, 1) and is recorded in raw/css-vars.json. It is not a separate DTCG cubicBezier token here.",
        ]
    },
}

out = HERE / "tokens.json"
out.write_text(json.dumps(tokens, indent=2) + "\n")
print("wrote", out, "core groups", list(core), "light", len(light))
