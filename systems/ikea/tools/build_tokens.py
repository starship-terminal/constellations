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
COMPUTED = json.loads((HERE / "raw" / "components-computed.json").read_text())["components"]
HAND = "Reconstruction — entered by hand at capture time, no raw reading behind it"


def reading(comp, prop):
    """A computed style (or rect h/w) of a component in raw/components-computed.json; raises when
    the reading is missing."""
    c = COMPUTED[comp]
    if prop in ("h", "w"):
        return f"{c['rect'][prop]:g}px"
    v = c["style"].get(prop)
    if not v:
        raise KeyError(f"{comp}: no {prop} reading")
    return v
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


def unnest(node):
    """Lift tokens that sit inside another token out as siblings: --colour-elevation-1 and
    --colour-elevation-1-border would make elevation.1 hold elevation.1.border, where DTCG walkers
    stop at $value and never look. The child becomes elevation.1-border."""
    for k in list(node):
        v = node[k]
        if not isinstance(v, dict) or k.startswith("$"):
            continue
        unnest(v)
        if "$value" in v:
            for c in [c for c in v if not c.startswith("$")]:
                if f"{k}-{c}" in node:
                    raise SystemExit(f"cannot lift {k}.{c}: {k}-{c} exists")
                node[f"{k}-{c}"] = v.pop(c)
    return node


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
    return unnest(tree)


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
            "source": "Reconstruction — abridged by hand from the computed font-family on body, www.ikea.com/sg/en/ 2026-11-19 "
                      "(raw/css-vars.json computed.bodyFont). The live stack leads with currency-symbol faces "
                      "(\"Omani Rial\", \"Emirati Dirham\", \"Saudi Riyal\"), then Noto IKEA and per-script Noto faces. "
                      "Noto IKEA is proprietary and is not loaded here."
        },
    }


# Type steps: each size is the declared Skapa variable (unitless px). A weight or line height is
# read where a component paints that step (its class names it: pp-skapa__typography-heading-l,
# pipcom-typography-heading-s); every other weight and line height was typed at capture time.
TYPE_STEPS = {
    "display-xl": ("--skapa-display-xl", 700, "80px", None),
    "display-l": ("--skapa-display-l", 700, "64px", None),
    "display-m": ("--skapa-display-m", 700, "48px", None),
    "heading-xl": ("--skapa-heading-xl", 700, "40px", None),
    "heading-l": ("--skapa-heading-l", 700, "32px", "login-heading"),
    "heading-m": ("--skapa-heading-m", 700, "24px", None),
    "heading-s": ("--skapa-heading-s", 700, "22px", "product-title"),
    "body-l": ("--skapa-body-l", 400, "24px", None),
    "body-m": ("--skapa-body-m", 400, "22px", None),
    "body-s": ("--skapa-body-s", 400, "18px", None),
    "price": ("--_skapa-price-font-size", 700, "32px", None),
}


def typography():
    out = {}
    for key, (var, weight, line, comp) in TYPE_STEPS.items():
        size = DECLARED[var].strip()
        if re.fullmatch(r"\d+(\.\d+)?", size):
            size += "px"
        elif size.endswith("rem"):
            size = "%gpx" % (float(size[:-3]) * 16)
        src = f"declared {var} (raw/css-vars.json)"
        if comp:
            c = COMPUTED[comp]
            if c["style"]["fontSize"] != size:
                raise ValueError(f"{key}: {comp} paints {c['style']['fontSize']}, the step declares {size}")
            weight, line = int(reading(comp, "fontWeight")), reading(comp, "lineHeight")
            src += f"; fontWeight and lineHeight computed on {comp} ({c['classes'].split()[-1]}, raw/components-computed.json)"
        else:
            src += f"; fontWeight and lineHeight: {HAND}"
        out[key] = {
            "$type": "typography",
            "$value": {"fontFamily": "{font.family.sans}", "fontSize": size, "fontWeight": weight, "lineHeight": line},
            "$extensions": {"source": src},
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
                "$value": "{accent}",
                "$extensions": {"source": "computed .pipf-btn__inner background on Add to cart, BILLY PDP 2026-11-19; matches --colour-interactive-emphasised-bg-default"},
            },
            "text": {
                "$type": "color",
                "$value": "{on-accent}",
                "$extensions": {"source": "computed colour on Add to cart label"},
            },
            "radius": {
                "$type": "dimension",
                "$value": "{radius.cap}",
                "$extensions": {"source": "computed border-radius 64px on .pipf-btn--emphasised"},
            },
            "height": {
                "$type": "dimension",
                "$value": reading("button-primary", "h"),
                "$extensions": {"source": "computed height of button-primary (Add to cart, BILLY PDP 2026-11-19, raw/components-computed.json)"},
            },
        },
        "search": {
            "height": {
                "$type": "dimension",
                "$value": reading("search", "h"),
                "$extensions": {"source": "computed height of search (the header search input, 2026-11-19, raw/components-computed.json)"},
            },
            "text": {
                "$type": "color",
                "$value": "{text}",
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
    names = set()

    def walk(n, p=""):
        for k, v in n.items():
            if isinstance(v, dict) and "$value" in v:
                names.add(p + k)
                yield p + k, v
            elif isinstance(v, dict) and not k.startswith("$"):
                yield from walk(v, p + k + ".")
    leaves = [x for setname in ("core", "light") for x in walk(tokens[setname])]
    for n, t in leaves:
        for a in re.findall(r"\{([^{}]+)\}", json.dumps(t["$value"])):
            if a not in names:
                raise KeyError(f"{n}: alias {{{a}}} points at nothing")
    return tokens


if __name__ == "__main__":
    tokens = build()
    (HERE / "tokens.json").write_text(json.dumps(tokens, indent=1) + "\n")
    print("wrote tokens.json", sum(1 for _ in json.dumps(tokens).split('"$type"')), "tokens")
