#!/usr/bin/env python3
"""Build tokens.json from raw/css-vars.json and raw/components-computed.json.

LottieFiles public site, read 2026-11-21. One light theme. Custom properties
are oklch. Component colours that the browser returned as oklch are kept as
the declared token and also recorded as the sRGB sample taken from the raw
screenshot of the same control, before quantize. A value that was not read
is not invented.
"""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
V = json.loads((RAW / "css-vars.json").read_text())
LIVE = V["liveRoot"]["values"]

def css(name):
    if name not in LIVE:
        raise KeyError(name)
    return LIVE[name]


def color(path, value, source, description):
    return {
        path: {
            "$value": value,
            "$type": "color",
            "$description": description,
            "$extensions": {"source": source},
        }
    }


def dim(path, value, source, description):
    return {
        path: {
            "$value": value,
            "$type": "dimension",
            "$description": description,
            "$extensions": {"source": source},
        }
    }


def font(path, value, source, description):
    return {
        path: {
            "$value": value,
            "$type": "fontFamily",
            "$description": description,
            "$extensions": {"source": source},
        }
    }


def weight(path, value, source, description):
    return {
        path: {
            "$value": value,
            "$type": "fontWeight",
            "$description": description,
            "$extensions": {"source": source},
        }
    }


def nest(flat):
    root = {}
    for path, leaf in flat.items():
        cur = root
        parts = path.split(".")
        for p in parts[:-1]:
            cur = cur.setdefault(p, {})
        cur[parts[-1]] = leaf
    return root


core_flat = {}
core_flat.update(color(
    "color.brand.primary",
    "oklch(62.6% 0.11 185.333)",
    "css-var --color-primary, computed on :root at https://lottiefiles.com/ (raw/css-vars.json liveRoot)",
    "Primary teal. The hero and Sign up buttons paint this.",
))
core_flat.update(color(
    "color.brand.primary-hover",
    "oklab(0.626 -0.109524 -0.0102239 / 0.9)",
    "computed backgroundColor of the Get started for free link while the pointer is over it (raw/components-computed.json button-primary hover)",
    "Primary at 90% opacity on hover. Left as the computed oklab string.",
))
core_flat.update(color(
    "color.brand.primary-srgb",
    "#28aca2",
    "sampled sRGB from the raw (pre-quantize) home-light-default.png pixel on the Get started for free button, 2026-11-21",
    "Displayed sRGB of the primary fill. The token behind it is oklch.",
))
core_flat.update(color(
    "color.page",
    "oklch(100% 0 0)",
    "css-var --color-background, computed on :root",
    "Page background.",
))
core_flat.update(color(
    "color.surface",
    "oklch(100% 0 0)",
    "css-var --color-card, computed on :root",
    "Card surface. Same as the page on the public marketing site.",
))
core_flat.update(color(
    "color.faint",
    "oklch(98.5% 0 0)",
    "css-var --color-faint, computed on :root",
    "Search field and sidebar background.",
))
core_flat.update(color(
    "color.text",
    "oklch(14.1% 0.005 285.823)",
    "css-var --color-foreground, computed on :root",
    "Primary text.",
))
core_flat.update(color(
    "color.on-accent",
    "oklch(98.5% 0 0)",
    "css-var --color-primary-foreground, computed on :root",
    "Text on the primary button.",
))
core_flat.update(color(
    "color.muted",
    "oklch(55.2% 0.016 285.938)",
    "css-var --color-muted-foreground, computed on :root",
    "Secondary text and the search placeholder.",
))
core_flat.update(color(
    "color.border",
    "oklch(92% 0.004 286.32)",
    "css-var --color-border, computed on :root",
    "Default border and the search outline.",
))
core_flat.update(color(
    "color.accent-wash",
    "oklch(96.7% 0.001 286.375)",
    "css-var --color-accent, computed on :root",
    "Nav hover wash. Named accent in the CSS, not the teal brand.",
))
core_flat.update(color(
    "color.destructive",
    "oklch(57.7% 0.245 27.325)",
    "css-var --color-destructive, computed on :root",
    "Destructive role. Not shown on a public confirmation dialog.",
))
core_flat.update(color(
    "color.warning",
    "oklch(70.5% 0.213 47.604)",
    "css-var --color-warning, computed on :root",
    "Warning role declared in CSS. Not shown on a public form error.",
))
core_flat.update(color(
    "color.inverse",
    "oklch(14.1% 0.005 285.823)",
    "css-var --color-background-inverse, computed on :root",
    "Inverse surface. Used by the footer band, not as a theme.",
))

core_flat.update(font(
    "font.family.sans",
    '"Inter LF", sans-serif',
    "css-var --font-sans, computed on :root; also computed fontFamily of header buttons",
    "UI and control family.",
))
core_flat.update(font(
    "font.family.display",
    '"DM Sans LF", "DM Sans", sans-serif',
    "computed fontFamily of the home h1 and the hero paragraph, 2026-11-21",
    "Display and hero body family.",
))
core_flat.update(font(
    "font.family.mono",
    'ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace',
    "css-var --font-mono, computed on :root",
    "Code family. Not shown in a public code block on the captured pages.",
))

core_flat.update(dim("font.size.display", "96px", "computed fontSize of the home h1", "Home display size."))
core_flat.update(dim("font.size.hero", "24px", "computed fontSize of the hero paragraph", "Hero supporting line."))
core_flat.update(dim("font.size.body", "16px", "computed fontSize of the hero CTA", "Control and body size."))
core_flat.update(dim("font.size.nav", "14px", "computed fontSize of header nav and Sign up", "Header control size."))
core_flat.update(weight("font.weight.display", 500, "computed fontWeight of the home h1", "Display weight."))
core_flat.update(weight("font.weight.control", 500, "computed fontWeight of the hero CTA and Sign up", "Control weight."))
core_flat.update(dim("font.line-height.display", "99.84px", "computed lineHeight of the home h1", "Display line height."))
core_flat.update(dim("font.letter-spacing.display", "-4.8px", "computed letterSpacing of the home h1", "Display tracking."))

core_flat.update(dim("radius.control", "12px", "computed borderRadius of the hero CTA", "Hero button radius."))
core_flat.update(dim("radius.nav", "6px", "computed borderRadius of Sign up and Log in", "Header control radius."))
core_flat.update(dim("radius.md", "0.5rem", "css-var --radius, computed on :root", "Base radius token."))
core_flat.update(dim("space.control-x", "24px", "computed paddingLeft of the hero CTA", "Hero button horizontal padding."))
core_flat.update(dim("space.nav-x", "16px", "computed paddingLeft of Sign up", "Header control horizontal padding."))
core_flat.update(dim("size.control", "48px", "computed height of the hero CTA", "Hero button height."))
core_flat.update(dim("size.nav", "36px", "computed height of Sign up and the search button", "Header control height."))
core_flat.update(dim("border.width", "1px", "computed borderTopWidth of Log in and Get in touch", "Quiet button border."))

core = nest(core_flat)
core["shadow"] = {
    "control": {
        "$value": {
            "offsetX": "0px",
            "offsetY": "1px",
            "blur": "2px",
            "spread": "0px",
            "color": "rgba(0, 0, 0, 0.05)",
        },
        "$type": "shadow",
        "$description": "The painted layer of the hero button shadow. The computed value also lists four transparent layers.",
        "$extensions": {
            "source": "computed boxShadow of Get started for free (raw/components-computed.json button-primary default)"
        },
    }
}

light = {
    "page": {"$value": "{core.color.page}", "$type": "color", "$extensions": {"source": "alias of core.color.page"}},
    "surface": {"$value": "{core.color.surface}", "$type": "color", "$extensions": {"source": "alias of core.color.surface"}},
    "text": {"$value": "{core.color.text}", "$type": "color", "$extensions": {"source": "alias of core.color.text"}},
    "muted": {"$value": "{core.color.muted}", "$type": "color", "$extensions": {"source": "alias of core.color.muted"}},
    "accent": {"$value": "{core.color.brand.primary}", "$type": "color", "$extensions": {"source": "alias of core.color.brand.primary"}},
    "on-accent": {"$value": "{core.color.on-accent}", "$type": "color", "$extensions": {"source": "alias of core.color.on-accent"}},
    "border": {"$value": "{core.color.border}", "$type": "color", "$extensions": {"source": "alias of core.color.border"}},
    "component": {
        "button-primary": {
            "background": {"$value": "{core.color.brand.primary}", "$type": "color", "$extensions": {"source": "alias"}},
            "text": {"$value": "{core.color.on-accent}", "$type": "color", "$extensions": {"source": "alias"}},
            "radius": {"$value": "{core.radius.control}", "$type": "dimension", "$extensions": {"source": "alias"}},
            "height": {"$value": "{core.size.control}", "$type": "dimension", "$extensions": {"source": "alias"}},
        },
        "button-quiet": {
            "background": {"$value": "{core.color.page}", "$type": "color", "$extensions": {"source": "alias"}},
            "text": {"$value": "{core.color.text}", "$type": "color", "$extensions": {"source": "alias"}},
            "border": {"$value": "{core.color.border}", "$type": "color", "$extensions": {"source": "alias"}},
        },
    },
}

doc = {
    "core": core,
    "light": light,
    "$themes": [
        {"id": "light", "name": "Light", "selectedTokenSets": {"core": "source", "light": "enabled"}},
    ],
}

(HERE / "tokens.json").write_text(json.dumps(doc, indent=2) + "\n")
print("wrote tokens.json")
