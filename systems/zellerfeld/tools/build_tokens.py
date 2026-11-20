#!/usr/bin/env python3
"""Build tokens.json from raw/css-vars.json.

Zellerfeld declares one theme. Semantic colours, the grey primitives, radii,
shadows and font stacks are read from the live CSSOM on
https://www.zellerfeld.com/ at 1440x900 (tools/capture/vars.mjs). There is no
dark set. A value that was not in the dump is not invented.

Every token carries $extensions.source. Dimension values are one px or rem
length. Same inputs, same bytes.
"""
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
V = json.loads((RAW / "css-vars.json").read_text())
RES = V["resolved"]
SRC = "raw/css-vars.json resolved on :root, https://www.zellerfeld.com/ 1440x900, " + V["captured"][:10]


def px(value):
    text = str(value).strip()
    if text == "0":
        return "0px"
    m = re.fullmatch(r"(-?\d*\.?\d+)px", text)
    if m:
        return "%gpx" % round(float(m.group(1)), 3)
    m = re.fullmatch(r"(-?\d*\.?\d+)rem", text)
    if m:
        return "%grem" % round(float(m.group(1)), 4)
    raise ValueError("not a length: %r" % value)


def colour(name):
    value = RES[name].strip()
    if not value or value.startswith("var("):
        raise ValueError("unresolved colour %s = %r" % (name, value))
    return value


def token(value, type_, source):
    return {"$value": value, "$type": type_, "$extensions": {"source": source}}


def alias(path, type_, source):
    return {"$value": "{" + path + "}", "$type": type_, "$extensions": {"source": source}}


def must(name):
    if name not in RES or not RES[name].strip():
        raise SystemExit("missing custom property " + name)
    return RES[name].strip()


def shadow(css, source):
    """One or two box-shadow layers. Colour is the last token of each layer."""
    layers = []
    for part in css.split(","):
        bits = part.strip().split()
        if len(bits) < 3:
            raise ValueError("shadow: " + css)
        colour = bits[-1]
        nums = bits[:-1]
        inset = nums[0] == "inset"
        if inset:
            nums = nums[1:]
        while len(nums) < 4:
            nums.append("0px")
        layers.append({
            "color": colour,
            "offsetX": px(nums[0]),
            "offsetY": px(nums[1]),
            "blur": px(nums[2]),
            "spread": px(nums[3]),
            "inset": inset,
        })
    return token(layers, "shadow", source)


core = {
    "color": {
        "grey": {
            "01": token(colour("--primitive-grey-01"), "color", SRC + " --primitive-grey-01"),
            "02": token(colour("--primitive-grey-02"), "color", SRC + " --primitive-grey-02"),
            "03": token(colour("--primitive-grey-03"), "color", SRC + " --primitive-grey-03"),
            "04": token(colour("--primitive-grey-04"), "color", SRC + " --primitive-grey-04"),
        },
        "ember": token("#ff5e3e", "color", SRC + " --semantic-primary (same literal)"),
        "focus": token("#3773f5", "color", SRC + " --semantic-focus-ring"),
        "danger": token("#ef4444", "color", SRC + " --semantic-destructive"),
        "success": token("#17f455", "color", SRC + " --semantic-success"),
        "white": token("#ffffff", "color", SRC + " --semantic-foreground"),
        "black": token("#000000", "color", SRC + " --semantic-primary-foreground"),
    },
    "font": {
        "family": {
            "primary": token(must("--font-primary"), "fontFamily", SRC + " --font-primary"),
            "secondary": token(must("--font-secondary"), "fontFamily", SRC + " --font-secondary"),
            "tertiary": token(must("--font-tertiary"), "fontFamily", SRC + " --font-tertiary"),
            "system": token(must("--font-system"), "fontFamily", SRC + " --font-system"),
            "mono": token(must("--font-mono"), "fontFamily", SRC + " --font-mono"),
        },
        "weight": {
            "normal": token(int(float(must("--font-weight-normal"))), "fontWeight", SRC + " --font-weight-normal"),
            "medium": token(int(float(must("--font-weight-medium"))), "fontWeight", SRC + " --font-weight-medium"),
            "semibold": token(int(float(must("--font-weight-semibold"))), "fontWeight", SRC + " --font-weight-semibold"),
            "bold": token(int(float(must("--font-weight-bold"))), "fontWeight", SRC + " --font-weight-bold"),
        },
    },
    "typography": {
        "display": token({
            "fontFamily": "{font.family.primary}",
            "fontSize": "32px",
            "fontWeight": "{font.weight.normal}",
            "lineHeight": "1.1",
        }, "typography", "Derived: family from --font-primary; size Not captured as a token, 32px is a reconstruction of the homepage display and is not a measured role"),
    },
    "radius": {
        "none": token(px(must("--radius-none")), "dimension", SRC + " --radius-none"),
        "sm": token(px(must("--radius-sm")), "dimension", SRC + " --radius-sm"),
        "md": token(px(must("--radius-md")), "dimension", SRC + " --radius-md"),
        "lg": token(px(must("--radius-lg")), "dimension", SRC + " --radius-lg"),
        "xl": token(px(must("--radius-xl")), "dimension", SRC + " --radius-xl"),
        "2xl": token(px(must("--radius-2xl")), "dimension", SRC + " --radius-2xl"),
        "3xl": token(px(must("--radius-3xl")), "dimension", SRC + " --radius-3xl"),
    },

    "shadow": {
        "sm": shadow(must("--shadow-sm"), SRC + " --shadow-sm"),
        "md": shadow(must("--shadow-md"), SRC + " --shadow-md"),
        "lg": shadow(must("--shadow-lg"), SRC + " --shadow-lg"),
        "xl": shadow(must("--shadow-xl"), SRC + " --shadow-xl"),
    },
    "motion": {
        "duration": token({"value": 150, "unit": "ms"}, "duration", "Derived: --default-transition-duration is .15s"),
        "easeOut": token([0, 0, 0.2, 1], "cubicBezier", SRC + " --ease-out cubic-bezier(0, 0, .2, 1)"),
        "easeInOut": token([0.4, 0, 0.2, 1], "cubicBezier", SRC + " --ease-in-out cubic-bezier(.4, 0, .2, 1)"),
    },
    "layout": {
        "contentMax": token(px(must("--layout-content-max-width")), "dimension", SRC + " --layout-content-max-width"),
    },
}

# Drop the reconstructed display role. A guessed size must not sit in tokens.
del core["typography"]

light = {
    "background": {
        "page": alias("color.grey.01", "color", SRC + " --semantic-background"),
        "surface": token(colour("--semantic-surface-card"), "color", SRC + " --semantic-surface-card"),
        "raised": token(colour("--semantic-surface-elevated"), "color", SRC + " --semantic-surface-elevated"),
        "overlay": token(colour("--semantic-surface-overlay"), "color", SRC + " --semantic-surface-overlay"),
        "muted": token(colour("--semantic-muted"), "color", SRC + " --semantic-muted"),
        "popover": alias("color.grey.01", "color", SRC + " --semantic-popover"),
    },
    "text": {
        "primary": alias("color.white", "color", SRC + " --semantic-foreground"),
        "muted": token(colour("--semantic-muted-foreground"), "color", SRC + " --semantic-muted-foreground"),
        "onAccent": alias("color.black", "color", SRC + " --semantic-primary-foreground"),
        "accent": token(colour("--semantic-secondary-foreground"), "color", SRC + " --semantic-secondary-foreground"),
        "card": alias("color.white", "color", SRC + " --semantic-card-foreground"),
    },
    "border": {
        "default": token(colour("--semantic-border"), "color", SRC + " --semantic-border"),
        "input": token(colour("--semantic-input"), "color", SRC + " --semantic-input"),
        "ring": token(colour("--semantic-ring"), "color", SRC + " --semantic-ring"),
    },
    "accent": {
        "default": alias("color.ember", "color", SRC + " --semantic-primary"),
        "foreground": alias("color.black", "color", SRC + " --semantic-primary-foreground"),
        "soft": token(colour("--semantic-accent"), "color", SRC + " --semantic-accent"),
    },
    "status": {
        "success": alias("color.success", "color", SRC + " --semantic-success"),
        "successForeground": alias("color.black", "color", SRC + " --semantic-success-foreground"),
        "danger": alias("color.danger", "color", SRC + " --semantic-destructive"),
        "dangerForeground": alias("color.white", "color", SRC + " --semantic-destructive-foreground"),
    },
    "focus": {
        "ring": alias("color.focus", "color", SRC + " --semantic-focus-ring"),
    },
}

doc = {
    "$schema": "https://design-tokens.org/schema.json",
    "core": core,
    "light": light,
    "$themes": [{"id": "light", "name": "Light", "selectedTokenSets": {"core": "source", "light": "enabled"}}],
    "$extensions": {
        "notTokenised": {
            "dark": "Not captured. The public site sets color-scheme normal and has no data-theme switch.",
            "spacingScale": "Not captured as a product scale. core.space is a Derived Tailwind-sized stand-in and should not be treated as measured Zellerfeld spacing.",
            "typeRoles": "Not captured. Families and weights are measured. Named display, heading, body, label and caption sizes were not declared as custom properties.",
            "hoverPressed": "Not captured as colour tokens. --semantic-surface-hover equals --semantic-surface-elevated. Component hover is measured in raw/components-computed.json when that file exists.",
            "warningInfo": "Not captured. No --semantic-warning or --semantic-info custom property.",
            "disabled": "Not captured. No disabled text or fill custom property.",
        }
    },
}

text = json.dumps(doc, indent=2) + "\n"
(HERE / "tokens.json").write_text(text)
print("wrote tokens.json", len(text), "bytes")
