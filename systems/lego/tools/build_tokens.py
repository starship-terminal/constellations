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
C = json.loads((RAW / "components-computed.json").read_text())["components"]


def comp(key, state, prop):
    """A computed style of a measured component. Raises when the reading is missing."""
    try:
        v = C[key][state]["style"]["style"][prop]
    except KeyError:
        raise SystemExit("no reading for %s %s %s in raw/components-computed.json" % (key, state, prop))
    if v in (None, ""):
        raise SystemExit("empty reading for %s %s %s" % (key, state, prop))
    return v


def measured(key, state, prop):
    return "measured %s on %s %s (raw/components-computed.json, lego.com 2026-11-18)" % (prop, key, state)


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
    """Place a token. A path that would make a token also hold child tokens raises:
    tools/catalog.py stops at $value, so those children would vanish from every export."""
    node = tree
    for part in path[:-1]:
        node = node.setdefault(part, {})
        if "$value" in node:
            raise ValueError("token %s would also contain %s" % (".".join(path[:-1]), path[-1]))
    if path[-1] in node:
        raise ValueError("duplicate token path " + ".".join(path))
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
        # --ds-color-layer-neutral-static and its -inverted sibling: a dotted
        # split would nest one token inside the other, so name the child as a
        # hyphenated sibling instead.
        if tail == "neutral.static.inverted":
            tail = "neutral.static-inverted"
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

# Shadows. Each declared layer becomes one DTCG shadow layer. The parser splits
# on top-level commas only (rgb()/rgba() carry commas), takes the colour in any
# position (hex, rgb(), rgba()), keeps `inset` wherever it stands, and raises on
# a layer it cannot read instead of dropping it.
def split_top(value):
    out, depth, cur = [], 0, ""
    for ch in value:
        if ch == "(":
            depth += 1
        elif ch == ")":
            depth -= 1
        if ch == "," and depth == 0:
            out.append(cur.strip())
            cur = ""
        else:
            cur += ch
    if cur.strip():
        out.append(cur.strip())
    return out


COLOR_RE = re.compile(r"rgba?\([^)]*\)|#[0-9a-fA-F]{3,8}\b")


def shadow_layers(name, value):
    layers = []
    for part in split_top(str(value)):
        inset = bool(re.search(r"\binset\b", part))
        rest = re.sub(r"\binset\b", " ", part)
        colours = COLOR_RE.findall(rest)
        rest = COLOR_RE.sub(" ", rest)
        lengths = rest.split()
        if len(colours) != 1 or not 2 <= len(lengths) <= 4:
            raise SystemExit("%s: shadow layer not understood: %r" % (name, part))
        nums = []
        for n in lengths:
            m = re.fullmatch(r"(-?[\d.]+)(px)?", n)
            if not m or (m.group(2) is None and float(m.group(1)) != 0):
                raise SystemExit("%s: shadow length not understood: %r" % (name, n))
            nums.append("%gpx" % float(m.group(1)))
        while len(nums) < 4:
            nums.append("0px")
        layer = {"offsetX": nums[0], "offsetY": nums[1], "blur": nums[2], "spread": nums[3],
                 "color": norm_color(colours[0])}
        if inset:
            layer["inset"] = True
        layers.append(layer)
    return layers


for name, raw in sorted(LIGHT.items()):
    if not re.fullmatch(r"--ds-shadow-\d+", name):
        continue
    put(core, ["shadow", name.rsplit("-", 1)[-1]], tok(shadow_layers(name, raw), "shadow", "css-var %s" % name))

# Type. Cera Pro is the computed UI family on every measured control; the
# stack is the computed one, quotes dropped. Cera Pro is proprietary and not
# committed.
def family(key, state="default"):
    return ", ".join(f.strip().strip('"\'') for f in comp(key, state, "fontFamily").split(","))


put(core, ["font", "family", "ui"], tok(family("product-card"), "fontFamily", measured("product-card", "default", "fontFamily")))
put(core, ["font", "weight", "regular"], tok(int(comp("product-card", "default", "fontWeight")), "fontWeight", measured("product-card", "default", "fontWeight")))
put(core, ["font", "weight", "medium"], tok(int(comp("pdp-add", "default", "fontWeight")), "fontWeight", measured("pdp-add", "default", "fontWeight") + "; Add to Bag on the product page"))
put(core, ["font", "weight", "bold"], tok(int(comp("pdp-price", "default", "fontWeight")), "fontWeight", measured("pdp-price", "default", "fontWeight")))
put(core, ["font", "size", "body"], tok(px_of(comp("product-price", "default", "fontSize")), "dimension", measured("product-price", "default", "fontSize") + "; product card price row"))
put(core, ["font", "size", "button"], tok(px_of(comp("pdp-add", "default", "fontSize")), "dimension", measured("pdp-add", "default", "fontSize")))
put(core, ["font", "size", "price"], tok("%gpx" % round(float(px_of(comp("pdp-price", "default", "fontSize"))[:-2])), "dimension",
                                         "derived: %s, rounded to the whole pixel" % measured("pdp-price", "default", "fontSize")))


def line_height(key, state="default"):
    """Unitless ratio of the computed line-height to the computed font-size."""
    lh = float(px_of(comp(key, state, "lineHeight"))[:-2])
    fs = float(px_of(comp(key, state, "fontSize"))[:-2])
    return "%g" % round(lh / fs, 2)


for role, key, size, weight in (
    ("body", "product-price", "body", "regular"),
    ("button", "pdp-add", "button", "medium"),
    ("price", "pdp-price", "price", "bold"),
):
    put(core, ["typography", role], {
        "$type": "typography",
        "$value": {
            "fontFamily": "{font.family.ui}",
            "fontSize": "{font.size.%s}" % size,
            "fontWeight": "{font.weight.%s}" % weight,
            "lineHeight": line_height(key),
        },
        "$extensions": {"source": "derived: lineHeight is %s lineHeight / fontSize; the other fields alias measured tokens" % key},
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
# The keyboard focus ring is a 2px box-shadow in --ds-color-focused-default.
# account-button is read because its hover paints nothing, so its
# focus-visible reading is not mixed with a hover fill.
FOCUS_VAR = "--ds-color-focused-default"
ring = comp("account-button", "focus-visible", "boxShadow")
if norm_color(COLOR_RE.findall(ring)[0]) != norm_color(LIGHT[FOCUS_VAR]):
    raise SystemExit("focus ring %r does not paint %s %s" % (ring, FOCUS_VAR, LIGHT[FOCUS_VAR]))
light["focus"] = tok(norm_color(LIGHT[FOCUS_VAR]), "color",
                     "css-var %s; painted as the 2px box-shadow ring (%s)" % (FOCUS_VAR, measured("account-button", "focus-visible", "boxShadow")))

# Component dimensions from the PDP measurement.
light["component"] = {
    "button": {
        "radius": tok(px_of(comp("pdp-add", "default", "borderTopLeftRadius")), "dimension", measured("pdp-add", "default", "borderTopLeftRadius") + "; --ds-layout-radius-pill"),
        "padding-x": tok(px_of(comp("pdp-add", "default", "paddingLeft")), "dimension", measured("pdp-add", "default", "paddingLeft")),
        "font-size": tok(px_of(comp("pdp-add", "default", "fontSize")), "dimension", measured("pdp-add", "default", "fontSize")),
    },
    "stepper": {
        "radius": tok(px_of(comp("quantity", "default", "borderTopLeftRadius")), "dimension", measured("quantity", "default", "borderTopLeftRadius")),
        "border": tok(px_of(comp("quantity", "default", "borderTopWidth")), "dimension", measured("quantity", "default", "borderTopWidth")),
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
