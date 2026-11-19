#!/usr/bin/env python3
"""Build tokens.json from IKEA Singapore's declared Skapa colour layer.

Source: raw/css-vars.json, harvested from www.ikea.com/sg/en/ stylesheets
on 2026-11-19. Colour roles are rgb triplets (the Skapa --colour-* form)
resolved on documentElement. Radius, space, duration and easing are the
declared --radius-*, --space-*, --duration-*-web and --ease-* values.
One light theme. Every token carries $extensions.source.

Deterministic. Edit the raw input, never tokens.json.
"""
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = json.loads((HERE / "raw" / "css-vars.json").read_text())
DECLARED = RAW["declared"]
SRC = "css-var"


def rgb_triplet(name):
    raw = DECLARED[name].strip()
    m = re.fullmatch(r"(\d+),\s*(\d+),\s*(\d+)", raw)
    if not m:
        raise ValueError(f"{name}: not an rgb triplet: {raw}")
    r, g, b = (int(x) for x in m.groups())
    return "#%02x%02x%02x" % (r, g, b)


def color(name):
    return {
        "$type": "color",
        "$value": rgb_triplet(name),
        "$extensions": {"source": f"{SRC} {name} (rgb triplet, www.ikea.com/sg/en 2026-11-19)"},
    }


def rem_to_px(value):
    value = value.strip()
    m = re.fullmatch(r"(-?\d*\.?\d+)rem", value)
    if m:
        px = float(m.group(1)) * 16
        if abs(px - round(px)) < 0.01:
            return "%dpx" % round(px)
        return ("%gpx" % round(px, 2))
    m = re.fullmatch(r"(-?\d+(?:\.\d+)?)px", value)
    if m:
        return value if value.endswith("px") else value + "px"
    if re.fullmatch(r"0", value):
        return "0px"
    raise ValueError("not a length: " + value)


def dim(name, value=None):
    raw = DECLARED[name] if value is None else value
    return {
        "$type": "dimension",
        "$value": rem_to_px(raw) if value is None else value,
        "$extensions": {"source": f"{SRC} {name}"},
    }


def duration(name):
    raw = DECLARED[name].strip()
    if raw == "0":
        raw = "0ms"
    elif raw.endswith("s") and not raw.endswith("ms"):
        ms = float(raw[:-1]) * 1000
        raw = "%dms" % round(ms)
    return {
        "$type": "duration",
        "$value": raw,
        "$extensions": {"source": f"{SRC} {name}"},
    }


def easing(name):
    raw = re.sub(r",\s*", ", ", DECLARED[name].strip())
    m = re.fullmatch(r"cubic-bezier\(([^)]+)\)", raw)
    if not m:
        raise ValueError(name + ": " + raw)
    nums = [float(x) for x in m.group(1).split(",")]
    return {
        "$type": "cubicBezier",
        "$value": nums,
        "$extensions": {"source": f"{SRC} {name}"},
    }


def nest(tree, parts, leaf):
    node = tree
    for p in parts[:-1]:
        node = node.setdefault(p, {})
    node[parts[-1]] = leaf


def colour_tree():
    tree = {}
    for name in sorted(DECLARED):
        if not name.startswith("--colour-"):
            continue
        parts = name.removeprefix("--colour-").split("-")
        nest(tree, parts, color(name))
    return tree


def radius():
    out = {}
    for name in sorted(DECLARED):
        if not name.startswith("--radius-"):
            continue
        key = name.removeprefix("--radius-")
        out[key] = dim(name)
    return out


def space():
    out = {}
    for name in sorted(DECLARED):
        if not name.startswith("--space-"):
            continue
        if name.startswith("--tw-"):
            continue
        key = name.removeprefix("--space-")
        out[key] = dim(name)
    return out


def font_family():
    return {
        "$type": "fontFamily",
        "$value": ["Noto IKEA", "Noto Sans", "system-ui", "sans-serif"],
        "$extensions": {
            "source": "computed font-family on body, www.ikea.com/sg/en/ 2026-11-19. The live stack leads with currency-symbol faces, then Noto IKEA. Noto IKEA is proprietary and is not loaded here."
        },
    }


def typography():
    roles = {
        "display-xl": ("72px", "700", "80px"),
        "display-l": ("56px", "700", "64px"),
        "display-m": ("40px", "700", "48px"),
        "heading-xl": ("32px", "700", "40px"),
        "heading-l": ("24px", "700", "32px"),
        "heading-m": ("18px", "700", "24px"),
        "heading-s": ("16px", "700", "22px"),
        "body-l": ("16px", "400", "24px"),
        "body-m": ("14px", "400", "22px"),
        "body-s": ("12px", "400", "18px"),
        "price": ("28px", "700", "32px"),
    }
    sources = {
        "display-xl": "--skapa-display-xl = 72",
        "display-l": "--skapa-display-l = 56",
        "display-m": "--skapa-display-m = 40",
        "heading-xl": "--skapa-heading-xl = 32",
        "heading-l": "--skapa-heading-l = 24 (login h1 computed 24px)",
        "heading-m": "--skapa-heading-m = 18",
        "heading-s": "--skapa-heading-s = 16",
        "body-l": "--skapa-body-l = 16",
        "body-m": "--skapa-body-m = 14 (computed body size)",
        "body-s": "--skapa-body-s = 12",
        "price": "--_skapa-price-font-size = 1.75rem",
    }
    out = {}
    for key, (size, weight, line) in roles.items():
        out[key] = {
            "$type": "typography",
            "$value": {
                "fontFamily": "{core.font.family.sans}",
                "fontSize": size,
                "fontWeight": int(weight),
                "lineHeight": line,
            },
            "$extensions": {"source": f"Measured Skapa type step {sources[key]}, www.ikea.com/sg/en 2026-11-19"},
        }
    return out


def motion():
    return {
        "duration": {
            "instant": duration("--duration-instant-web"),
            "quick": duration("--duration-quick-web"),
            "standard": duration("--duration-standard-web"),
            "slow": duration("--duration-slow-web"),
        },
        "easing": {name.removeprefix("--ease-"): easing(name) for name in sorted(DECLARED) if name.startswith("--ease-")},
    }


def semantic():
    return {
        "page": color("--colour-neutral-1"),
        "surface": color("--colour-neutral-2"),
        "text": color("--colour-text-and-icon-1"),
        "muted": color("--colour-text-and-icon-2"),
        "accent": color("--colour-static-ikea-brand-blue"),
        "accent-hover": color("--colour-interactive-emphasised-bg-hover"),
        "yellow": color("--colour-static-ikea-brand-yellow"),
        "border": color("--colour-neutral-3"),
        "on-accent": color("--colour-text-and-icon-5"),
        "destructive": color("--colour-semantic-negative"),
        "positive": color("--colour-semantic-positive"),
        "family": color("--colour-static-ikea-family"),
        "focus": color("--colour-interactive-emphasised-border-selected"),
    }


def component():
    return {
        "button-primary": {
            "bg": {
                "$type": "color",
                "$value": "{light.accent}",
                "$extensions": {"source": "computed .pipf-btn__inner background on Add to cart, BILLY PDP 2026-11-19; matches --colour-interactive-emphasised-bg-default"},
            },
            "text": {
                "$type": "color",
                "$value": "{light.on-accent}",
                "$extensions": {"source": "computed colour on Add to cart label"},
            },
            "radius": {
                "$type": "dimension",
                "$value": "{core.radius.cap}",
                "$extensions": {"source": "computed border-radius 64px on .pipf-btn--emphasised"},
            },
            "height": {
                "$type": "dimension",
                "$value": "56px",
                "$extensions": {"source": "computed height of Add to cart, BILLY PDP 2026-11-19"},
            },
        },
        "search": {
            "height": {
                "$type": "dimension",
                "$value": "48px",
                "$extensions": {"source": "computed height of header search input, 2026-11-19"},
            },
            "text": {
                "$type": "color",
                "$value": "{light.text}",
                "$extensions": {"source": "computed colour of input[name=q]"},
            },
        },
    }


def build():
    tokens = {
        "$description": "IKEA Singapore public storefront (www.ikea.com/sg/en), captured 2026-11-19 signed out. Skapa --colour-* layer, one light theme. The global country picker at www.ikea.com is a separate page.",
        "core": {
            "font": {"family": {"sans": font_family()}},
            "typography": typography(),
            "radius": radius(),
            "space": space(),
            "motion": motion(),
        },
        "light": {
            **semantic(),
            "colour": colour_tree(),
            "component": component(),
        },
        "$themes": [{"id": "light", "name": "Light", "selectedTokenSets": {"core": "source", "light": "enabled"}}],
    }
    (HERE / "tokens.json").write_text(json.dumps(tokens, indent=1) + "\n")
    print("wrote tokens.json", sum(1 for _ in json.dumps(tokens).split('"$type"')), "tokens")


if __name__ == "__main__":
    build()
