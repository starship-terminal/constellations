#!/usr/bin/env python3
"""Build tokens.json from forhims.co.uk's declared custom properties.

Source: raw/css-vars.json, resolved on documentElement in headless Chromium
on 2026-11-19. The UK site paints one light theme
(html.brand-hims.variant-care-sans). No dark variant was found.

Semantic roles come from the --colors-* layer (canvas, text, button, brand,
ui, form). Type comes from --fontSizes-* and --b-font-family-*. Spacing,
radius and motion come from --spacing-*, --sizing-radius and --transitions-*.
The Bonsai ramps (--b-color-*, --bonsai-colors-*) stay in core.color as the
declared palette. Every token carries $extensions.source.

Deterministic. Edit the raw input, never tokens.json.
"""
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = json.loads((HERE / "raw" / "css-vars.json").read_text())
RESOLVED = RAW["resolved"]["light"]
SRC = "css-var"


def norm_color(v):
    v = str(v).strip()
    if v.lower() in ("transparent", "rgba(0, 0, 0, 0)", "rgba(0,0,0,0)"):
        return "rgba(0, 0, 0, 0)"
    m = re.fullmatch(r"#([0-9a-fA-F]{3,8})", v)
    if m:
        h = m.group(1)
        if len(h) in (3, 4):
            h = "".join(c * 2 for c in h)
        r, g, b = (int(h[i:i + 2], 16) for i in (0, 2, 4))
        if len(h) == 8:
            a = int(h[6:8], 16) / 255
            if a >= 0.999:
                return "#%02x%02x%02x" % (r, g, b)
            return "rgba(%d, %d, %d, %g)" % (r, g, b, round(a, 3))
        return "#%02x%02x%02x" % (r, g, b)
    m = re.fullmatch(r"rgba?\(\s*([\d.]+)\s*,\s*([\d.]+)\s*,\s*([\d.]+)\s*(?:,\s*([\d.]+)\s*)?\)", v)
    if m:
        r, g, b = (int(round(float(x))) for x in m.group(1, 2, 3))
        if m.group(4) is None or float(m.group(4)) >= 0.999:
            return "#%02x%02x%02x" % (r, g, b)
        return "rgba(%d, %d, %d, %g)" % (r, g, b, round(float(m.group(4)), 3))
    raise ValueError("not a colour: " + v)


def color_token(name):
    return {
        "$type": "color",
        "$value": norm_color(RESOLVED[name]),
        "$extensions": {"source": f"{SRC} {name}"},
    }


def dim_from(name, raw=None):
    v = str(raw if raw is not None else RESOLVED[name]).strip()
    if re.fullmatch(r"-?\d+(\.\d+)?rem", v) or re.fullmatch(r"-?\d+(\.\d+)?px", v):
        return {"$type": "dimension", "$value": v, "$extensions": {"source": f"{SRC} {name}"}}
    raise ValueError(f"{name}: not a dimension: {v}")


def number_token(name):
    v = str(RESOLVED[name]).strip()
    if not re.fullmatch(r"-?\d+(\.\d+)?", v):
        raise ValueError(f"{name}: not a number: {v}")
    return {"$type": "number", "$value": float(v) if "." in v else int(v), "$extensions": {"source": f"{SRC} {name}"}}


def string_token(name):
    return {"$type": "fontFamily", "$value": RESOLVED[name], "$extensions": {"source": f"{SRC} {name}"}}


def duration_token(name):
    v = str(RESOLVED[name]).strip()
    if not re.fullmatch(r"\d+ms", v):
        raise ValueError(f"{name}: not a duration: {v}")
    return {"$type": "duration", "$value": v, "$extensions": {"source": f"{SRC} {name}"}}


def cubic(name):
    v = str(RESOLVED[name]).strip()
    m = re.fullmatch(r"cubic-bezier\(\s*([-\d.]+)\s*,\s*([-\d.]+)\s*,\s*([-\d.]+)\s*,\s*([-\d.]+)\s*\)", v)
    if not m:
        return None
    return {
        "$type": "cubicBezier",
        "$value": [float(x) for x in m.groups()],
        "$extensions": {"source": f"{SRC} {name}"},
    }


def pxish(part):
    part = part.strip()
    if re.fullmatch(r"-?\d+(?:\.\d+)?", part):
        return part + "px"
    if re.fullmatch(r"-?\d+(?:\.\d+)?px", part):
        return part
    raise ValueError("not a shadow length: " + part)


def shadow_token(name):
    raw = RESOLVED[name].strip()
    m = re.fullmatch(
        r"(-?\d+(?:\.\d+)?(?:px)?)\s+(-?\d+(?:\.\d+)?(?:px)?)\s+(-?\d+(?:\.\d+)?(?:px)?)\s+(-?\d+(?:\.\d+)?(?:px)?)\s+(\S+)",
        raw,
    )
    if not m:
        raise ValueError("shadow " + raw)
    ox, oy, blur, spread = (pxish(x) for x in m.group(1, 2, 3, 4))
    col = m.group(5)
    return {
        "$type": "shadow",
        "$value": {
            "offsetX": ox,
            "offsetY": oy,
            "blur": blur,
            "spread": spread,
            "color": norm_color(col),
        },
        "$extensions": {"source": f"{SRC} {name}"},
    }


def slug(name, prefix):
    rest = name.removeprefix(prefix)
    return re.sub(r"[^a-zA-Z0-9]+", "-", rest).strip("-").lower()


def group_colors(prefix):
    out = {}
    for name in sorted(RESOLVED):
        if not name.startswith(prefix):
            continue
        try:
            out[slug(name, prefix)] = color_token(name)
        except ValueError:
            continue
    return out


def core():
    palette = {}
    for prefix in ("--b-color-", "--bonsai-colors-", "--colors-"):
        for name in sorted(RESOLVED):
            if not name.startswith(prefix):
                continue
            key = slug(name, "--")
            try:
                palette[key] = color_token(name)
            except ValueError:
                continue
    font = {
        "sans": string_token("--b-font-family-sans"),
        "serif": string_token("--b-font-family-serif"),
    }
    type_size = {}
    for name in sorted(RESOLVED):
        if name.startswith("--fontSizes-"):
            type_size[slug(name, "--fontSizes-")] = dim_from(name)
    type_weight = {}
    for name in sorted(RESOLVED):
        if name.startswith("--fontWeights-"):
            type_weight[slug(name, "--fontWeights-")] = number_token(name)
    spacing = {}
    for name in sorted(RESOLVED):
        if name.startswith("--spacing-"):
            spacing[slug(name, "--spacing-")] = dim_from(name)
    radius = {"control": dim_from("--sizing-radius")}
    motion_duration = {}
    for name in sorted(RESOLVED):
        if name.startswith("--transitions-speed-"):
            motion_duration[slug(name, "--transitions-speed-")] = duration_token(name)
    motion_easing = {}
    not_tokenised = []
    for name in sorted(RESOLVED):
        if not name.startswith("--transitions-easing-"):
            continue
        tok = cubic(name)
        if tok:
            motion_easing[slug(name, "--transitions-easing-")] = tok
        else:
            not_tokenised.append({"name": name, "value": RESOLVED[name], "reason": "keyword easing, not a cubic-bezier"})
    elevation = {}
    for name in sorted(RESOLVED):
        if name.startswith("--bonsai-shadows-"):
            elevation[slug(name, "--bonsai-shadows-")] = shadow_token(name)
    typography = {}
    # Composite type styles from the declared size scale, Care Sans, regular weight.
    line = {
        "display-x-large": "1.05",
        "display-large": "1.05",
        "display-medium": "1.08",
        "display-small": "1.1",
        "heading-x-large": "1.15",
        "heading-large": "1.2",
        "heading-medium": "1.25",
        "heading-small": "1.3",
        "body-large": "1.4",
        "body-medium": "1.45",
        "body-small": "1.4",
        "caption": "1.35",
        "label": "1.3",
        "tiny": "1.2",
    }
    for key, size in type_size.items():
        style_key = key.replace("-", " ")
        # keys are already slug-like: bodylarge -> keep camel split
        pretty = re.sub(r"([a-z])([A-Z])", r"\1-\2", key).lower() if any(c.isupper() for c in key) else key
        # slug() already lowercased camel? fontSizes-bodyLarge -> bodylarge via non-alnum split which keeps camel
        pretty = re.sub(r"([a-z])([A-Z])", r"\1-\2", 
                        name_from_slug_source(key)).lower()
        typography[pretty] = {
            "$type": "typography",
            "$value": {
                "fontFamily": "{font.sans}",
                "fontSize": "{type.size." + key + "}",
                "fontWeight": "{type.weight.regular}",
                "lineHeight": line.get(pretty, "1.4"),
                "letterSpacing": "0em",
            },
            "$extensions": {"source": f"derived {SRC} --fontSizes-{key} + --b-font-family-sans"},
        }
    return {
        "color": palette,
        "font": font,
        "type": {"size": type_size, "weight": type_weight},
        "typography": typography,
        "spacing": spacing,
        "radius": radius,
        "elevation": elevation,
        "motion": {
            "duration": motion_duration,
            "easing": motion_easing,
            "$extensions": {"notTokenised": not_tokenised},
        },
    }


def name_from_slug_source(key):
    # Recover camelCase from the original --fontSizes- name.
    for name in RESOLVED:
        if name.startswith("--fontSizes-") and slug(name, "--fontSizes-") == key:
            return name.removeprefix("--fontSizes-")
    return key


def light():
    return {
        "color": {
            "page": color_token("--colors-canvas-primaryLight"),
            "surface": color_token("--colors-canvas-primary"),
            "surface-white": color_token("--colors-canvas-white"),
            "text": color_token("--colors-text-primary"),
            "text-secondary": color_token("--colors-text-secondary"),
            "text-legal": color_token("--colors-text-legal"),
            "text-on-primary": color_token("--colors-text-onPrimary"),
            "accent": color_token("--colors-brand-default"),
            "accent-text": color_token("--colors-text-callout"),
            "border": color_token("--colors-ui-divider"),
            "button": {
                "primary": color_token("--colors-button-primary"),
                "primary-text": color_token("--colors-button-primaryText"),
                "primary-hover-text": color_token("--colors-button-primaryHoverText"),
                "accent": color_token("--colors-button-accent"),
                "accent-text": color_token("--colors-button-accentText"),
                "disabled": color_token("--colors-button-disabled"),
                "disabled-text": color_token("--colors-button-disabledText"),
            },
            "form": {
                "error": color_token("--colors-form-error"),
                "success": color_token("--colors-form-success"),
            },
            "canvas": group_colors("--colors-canvas-"),
            "brand": group_colors("--colors-brand-"),
        }
    }


def build():
    tokens = {
        "$schema": "https://design-tokens.org/schemas/2025.10/format.json",
        "core": core(),
        "light": light(),
        "$themes": [
            {"id": "light", "name": "Light", "selectedTokenSets": {"core": "source", "light": "enabled"}}
        ],
    }
    # One composite per declared --fontSizes-* step. Size and family are declared; the weight is
    # the same-named --fontWeights-* step where Bonsai declares one. Bonsai declares no line height
    # or letter spacing for these steps (the --b-line-height-* calc() roles belong to the newer
    # --b-* scale, and the measured titles paint neither), so those were typed at capture time
    # and the source says so.
    typo = {}
    line = {
        "displayXLarge": 1.05, "displayLarge": 1.05, "displayMedium": 1.08, "displaySmall": 1.1,
        "headingXLarge": 1.15, "headingLarge": 1.2, "headingMedium": 1.25, "headingSmall": 1.3,
        "bodyLarge": 1.4, "bodyMedium": 1.45, "bodySmall": 1.4, "caption": 1.35, "label": 1.3, "tiny": 1.2,
    }
    for name in sorted(RESOLVED):
        if not name.startswith("--fontSizes-"):
            continue
        raw_key = name.removeprefix("--fontSizes-")
        pretty = re.sub(r"([a-z])([A-Z])", r"\1-\2", raw_key).lower()
        size_key = slug(name, "--fontSizes-")
        weight_var = f"--fontWeights-{raw_key}"
        if weight_var in RESOLVED:
            weight = "{type.weight." + slug(weight_var, "--fontWeights-") + "}"
            weight_src = f"weight declared {weight_var}"
            hand = "lineHeight and letterSpacing"
        else:
            weight = "{type.weight.regular}"
            weight_src = None
            hand = "fontWeight, lineHeight and letterSpacing"
        src = f"declared {name} (size) and --b-font-family-sans (family)"
        if weight_src:
            src += f"; {weight_src}"
        src += f"; {hand}: Reconstruction — entered by hand at capture time, no raw reading behind it"
        typo[pretty] = {
            "$type": "typography",
            "$value": {
                "fontFamily": "{font.sans}",
                "fontSize": "{type.size." + size_key + "}",
                "fontWeight": weight,
                "lineHeight": line[raw_key],
                "letterSpacing": "0px",
            },
            "$extensions": {"source": src},
        }
    tokens["core"]["typography"] = typo
    return tokens


if __name__ == "__main__":
    tokens = build()
    out = HERE / "tokens.json"
    out.write_text(json.dumps(tokens, indent=2) + "\n")
    print("wrote", out, "core colors", len(tokens["core"]["color"]), "type", len(tokens["core"]["typography"]))
