#!/usr/bin/env python3
"""Build tokens.json from raw/css-vars.json.

lego.com declares a Skroll design system as --ds-* custom properties.
The shop paints one light theme. A .dark probe resolves the same values,
so the export holds core and light only.

Every token carries $extensions.source. Deterministic.
"""
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
V = json.loads((RAW / "css-vars.json").read_text())
LIGHT = {n: d.get("value") or d.get("raw") for n, d in V["resolved"]["light"].items()}


def norm_color(v):
    v = str(v).strip().lower()
    m = re.fullmatch(r"#([0-9a-f]{3,8})", v)
    if m:
        h = m.group(1)
        if len(h) in (3, 4):
            h = "".join(c * 2 for c in h)
        r, g, b = (int(h[i:i + 2], 16) for i in (0, 2, 4))
        if len(h) == 8:
            a = round(int(h[6:8], 16) / 255, 3)
            if a == 1:
                return "#%02x%02x%02x" % (r, g, b)
            return "rgba(%d, %d, %d, %s)" % (r, g, b, ("%g" % a))
        return "#%02x%02x%02x" % (r, g, b)
    m = re.fullmatch(r"rgba?\(\s*(\d+)[,\s]+(\d+)[,\s]+(\d+)(?:\s*[,/]\s*([\d.]+%?))?\s*\)", v)
    if m:
        r, g, b, a = m.groups()
        if a is None:
            return "#%02x%02x%02x" % (int(r), int(g), int(b))
        a = float(a[:-1]) / 100 if a.endswith("%") else float(a)
        if a == 1:
            return "#%02x%02x%02x" % (int(r), int(g), int(b))
        return "rgba(%s, %s, %s, %g)" % (r, g, b, a)
    raise ValueError("not a colour: " + v)


def is_color(v):
    try:
        norm_color(v)
        return True
    except ValueError:
        return False


def px_of(v):
    v = str(v).strip()
    m = re.fullmatch(r"(-?[\d.]+)px", v)
    if m:
        return "%gpx" % float(m.group(1))
    m = re.fullmatch(r"(-?[\d.]+)rem", v)
    if m:
        return "%gpx" % (float(m.group(1)) * 16)
    return None


def tok(value, ty, source):
    return {"$value": value, "$type": ty, "$extensions": {"source": source}}


def put(tree, path, token):
    node = tree
    for part in path[:-1]:
        node = node.setdefault(part, {})
    node[path[-1]] = token


core = {}
light = {}

# Colour roles the shop declares and paints.
ROLE_GROUPS = {
    "color.brand": "--ds-color-brand-",
    "color.layer": "--ds-color-layer-",
    "color.text": "--ds-color-text-",
    "color.action": "--ds-color-action-",
    "color.border": "--ds-color-border-",
}
for group, prefix in ROLE_GROUPS.items():
    for name, raw in sorted(LIGHT.items()):
        if not name.startswith(prefix):
            continue
        if not is_color(raw):
            continue
        tail = name[len(prefix):].replace("-", ".")
        # Keep the semantic roles, not every theme-thumbnail colour.
        if group == "color.brand" and not re.match(
            r"^(black|white|bright|cool|dark|earth|extended)", tail
        ):
            continue
        if group == "color.brand" and tail.startswith("extended") and tail.count(".") > 1:
            continue
        put(core, (group + "." + tail).split("."), tok(
            norm_color(raw), "color", "css-var %s (resolved on :root, lego.com 2026-11-18)" % name,
        ))

# Spacing and radius scales (resolved px).
for name, raw in sorted(LIGHT.items()):
    if name.startswith("--ds-layout-spacing-") and re.fullmatch(r"--ds-layout-spacing-\d+", name):
        px = px_of(raw)
        if not px:
            continue
        step = name.rsplit("-", 1)[-1]
        put(core, ["space", step], tok(px, "dimension", "css-var %s" % name))
    if name.startswith("--ds-layout-radius-"):
        px = px_of(raw)
        if not px:
            continue
        step = name.rsplit("-", 1)[-1]
        put(core, ["radius", step], tok(px, "dimension", "css-var %s" % name))

# Shadows: keep the numeric ladder as strings under $extensions, and tokenise
# the first layer when it parses. DTCG shadow needs structured layers; store
# the declared string as a note and a single reconstructed layer when simple.
SHADOW_RE = re.compile(
    r"(-?[\d.]+)px\s+(-?[\d.]+)px\s+(-?[\d.]+)px\s+(-?[\d.]+)px\s+(#[0-9a-fA-F]{3,8})"
)
for name, raw in sorted(LIGHT.items()):
    if not re.fullmatch(r"--ds-shadow-\d+", name):
        continue
    layers = []
    for m in SHADOW_RE.finditer(str(raw)):
        col = m.group(5)
        if len(col) == 9:
            # #rrggbbaa
            try:
                col = norm_color(col)
            except ValueError:
                continue
        else:
            col = norm_color(col)
        layers.append({
            "offsetX": "%gpx" % float(m.group(1)),
            "offsetY": "%gpx" % float(m.group(2)),
            "blur": "%gpx" % float(m.group(3)),
            "spread": "%gpx" % float(m.group(4)),
            "color": col,
        })
    if layers:
        put(core, ["shadow", name.rsplit("-", 1)[-1]], tok(layers, "shadow", "css-var %s" % name))

# Type. Cera Pro is the computed UI family on every measured control.
put(core, ["font", "family", "ui"], tok(
    "Cera Pro, Noto Sans KR, sans-serif", "fontFamily",
    "measured fontFamily on .sk-button and h1, lego.com 2026-11-18; Cera Pro is proprietary and not committed",
))
put(core, ["font", "weight", "regular"], tok(400, "fontWeight", "measured fontWeight on body text"))
put(core, ["font", "weight", "medium"], tok(500, "fontWeight", "measured fontWeight on Add to Bag (.sk-button--emphasis)"))
put(core, ["font", "weight", "bold"], tok(700, "fontWeight", "measured fontWeight on product price (ds-heading-lg)"))
put(core, ["font", "size", "body"], tok("16px", "dimension", "measured fontSize on product card price row"))
put(core, ["font", "size", "button"], tok("18px", "dimension", "measured fontSize on Add to Bag"))
put(core, ["font", "size", "price"], tok("24px", "dimension", "measured fontSize on PDP price, rounded from 24.347px computed"))
put(core, ["typography", "body"], {
    "$type": "typography",
    "$value": {
        "fontFamily": "{font.family.ui}",
        "fontSize": "{font.size.body}",
        "fontWeight": "{font.weight.regular}",
        "lineHeight": "1.4",
    },
    "$extensions": {"source": "derived from measured Cera Pro body on the shop"},
})
put(core, ["typography", "button"], {
    "$type": "typography",
    "$value": {
        "fontFamily": "{font.family.ui}",
        "fontSize": "{font.size.button}",
        "fontWeight": "{font.weight.medium}",
        "lineHeight": "1.2",
    },
    "$extensions": {"source": "derived from measured Add to Bag"},
})
put(core, ["typography", "price"], {
    "$type": "typography",
    "$value": {
        "fontFamily": "{font.family.ui}",
        "fontSize": "{font.size.price}",
        "fontWeight": "{font.weight.bold}",
        "lineHeight": "1.2",
    },
    "$extensions": {"source": "derived from measured PDP price"},
})

# Motion from declared nav timings.
put(core, ["motion", "duration", "nav-open"], tok("200ms", "duration", "css-var --_nav-open-duration .2s"))
put(core, ["motion", "duration", "nav-close"], tok("130ms", "duration", "css-var --_nav-close-duration .13s"))
put(core, ["motion", "duration", "nav-panel"], tok("420ms", "duration", "css-var --_nav-panel-duration .42s"))
put(core, ["motion", "easing", "nav-panel"], tok([0.4, 0, 0.2, 1], "cubicBezier", "css-var --_nav-panel-easing"))
put(core, ["motion", "easing", "nav-open"], tok([0.32, 0.72, 0, 1], "cubicBezier", "css-var --_nav-open-easing"))

# Semantic roles, aliased to the declared colours a measurement confirmed.
def alias(path, source):
    return {"$value": "{" + path + "}", "$type": "color", "$extensions": {"source": source}}

light["page"] = alias("color.layer.default", "page background matches --ds-color-layer-default #ffffff")
light["surface"] = alias("color.layer.level.2.default", "raised wash --ds-color-layer-level-2-default")
light["text"] = alias("color.text.default", "ink on product cards and headings, --ds-color-text-default")
light["muted"] = alias("color.text.subdued", "secondary ink --ds-color-text-subdued")
light["accent"] = alias("color.action.primary.enabled", "Skroll primary blue --ds-color-action-primary-enabled; PDP Add to Bag paints emphasis orange instead")
light["border"] = alias("color.border.default", "field and stepper border --ds-color-border-default")
light["emphasis"] = alias("color.action.emphasis.enabled", "measured Add to Bag fill rgb(233, 111, 20) matches --ds-color-action-emphasis-enabled")
light["positive"] = alias("color.text.positive", "declared positive text")
light["warning"] = alias("color.text.warning", "declared warning text")
light["negative"] = alias("color.text.negative", "declared negative text")
light["focus"] = tok("#005ad2", "color", "measured: primary action blue used as the focus colour; outline width read per control")

# Component dimensions from the PDP measurement.
light["component"] = {
    "button": {
        "radius": tok("999px", "dimension", "measured borderRadius on Add to Bag, --ds-layout-radius-pill"),
        "padding-x": tok("20px", "dimension", "measured padding on Add to Bag"),
        "font-size": tok("18px", "dimension", "measured fontSize on Add to Bag"),
    },
    "stepper": {
        "radius": tok("4px", "dimension", "measured borderRadius on quantity stepper"),
        "border": tok("1px", "dimension", "measured borderTopWidth on quantity stepper"),
    },
}

doc = {
    "$schema": "https://design-tokens.org/schemas/2025.10/tokens.json",
    "core": core,
    "light": light,
    "$themes": [{"id": "light", "name": "Light", "selectedTokenSets": {"core": "source", "light": "enabled"}}],
}
(HERE / "tokens.json").write_text(json.dumps(doc, indent=1) + "\n")
print("tokens.json core groups", list(core), "light", list(light))
