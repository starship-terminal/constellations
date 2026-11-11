#!/usr/bin/env python3
"""Write raw/component-tokens.json, the token spec build_tokens.py reads.

bezi.com is a Framer site; its bundle declares on `body`
(raw/css-vars.json, read by tools/capture/vars.mjs):

  --token-<uuid>   the project's palette, 47 declarations covering 36 unique
                   values (several uuids repeat #000000, #ffffff and the
                   common white alphas; the repeats are folded onto the first
                   uuid that resolves to the value):
                   * an orange ramp around the CTA colour #f84503 -> color.orange.*
                   * a dark neutral ramp plus black and white -> color.ink.*
                   * translucent whites and blacks for hairlines, fills and
                     scrims -> color.white-alpha.* / color.black-alpha.*
                   * pastel accents for the engine/tool chips and the Free
                     band -> color.pastel.*
  --framer-*       Framer's own layout/effect internals, not a design scale;
                   recorded in css-vars.json but not tokenised
  --token-font-*   314 @font-face declarations, recorded in css-vars.json

A leaf is {"var": "--name"} (resolved by build_tokens.py) or {"value": ...,
"source": "..."} for a measured value. The readable token name is decided
here, so build_tokens.py's spec carries names like color.orange.600 while the
"var" still points at the real --token-<uuid> declaration.
"""
import json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
V = json.loads((RAW / "css-vars.json").read_text())
RL = V["resolved"]["light"]
C = json.loads((RAW / "components-computed.json").read_text())["components"]
R = {n: v.get("value", v.get("raw")) for n, v in RL.items()}

# The product's own palette among the --token-* declarations, named by hand
# after what the site paints them as (checked against the screenshots and the
# measured paint layers):
#   orange       the CTA/highlight ramp around #f84503, incl. its 35% scrim
#   ink          the dark neutral ramp the pages and cards are built from
#   white-alpha  translucent whites: hairlines, fills, the header scrim
#   black-alpha  translucent blacks: scrims and the plan-CTA fill
#   pastel       the accent colours of the engine/tool chips and the Free band
PALETTE = {
    # orange ramp, darkest to lightest; .500 is the painted CTA colour
    "#e34a12": "orange.700", "#f84503": "orange.600", "#ff6b36": "orange.500",
    "#ff7340": "orange.400", "#ff8d63": "orange.300", "#edc1af": "orange.100",
    "rgba(248, 69, 3, 0.35)": "orange.alpha-35",
    # dark neutrals
    "#000000": "ink.950", "#141414": "ink.900", "#262626": "ink.800",
    "#424242": "ink.700", "#595959": "ink.600",
    "#c1c5c6": "ink.300", "#d9d9d9": "ink.200", "#dedede": "ink.100",
    "#ffffff": "ink.0",
    # translucent whites (rgba(255,255,255,a))
    "rgba(255, 255, 255, 0)": "white-alpha.0",
    "rgba(255, 255, 255, 0.05)": "white-alpha.5",
    "rgba(255, 255, 255, 0.1)": "white-alpha.10",
    "rgba(255, 255, 255, 0.15)": "white-alpha.15",
    "rgba(255, 255, 255, 0.2)": "white-alpha.20",
    "rgba(255, 255, 255, 0.25)": "white-alpha.25",
    "rgba(255, 255, 255, 0.3)": "white-alpha.30",
    "rgba(255, 255, 255, 0.35)": "white-alpha.35",
    "rgba(255, 255, 255, 0.6)": "white-alpha.60",
    "rgba(255, 255, 255, 0.8)": "white-alpha.80",
    # translucent blacks (rgba(0,0,0,a))
    "rgba(0, 0, 0, 0.3)": "black-alpha.30",
    "rgba(0, 0, 0, 0.6)": "black-alpha.60",
    "rgba(0, 0, 0, 0.8)": "black-alpha.80",
    # pastel accents
    "#7dadd1": "pastel.sky", "#34739b": "pastel.blue", "#3c4276": "pastel.indigo",
    "#ce9fcc": "pastel.lilac", "#e3e3ff": "pastel.periwinkle",
    "#e3f2ff": "pastel.ice", "#f3ffe2": "pastel.mint",
    "#f6ff85": "pastel.lemon", "#fde4f9": "pastel.pink",
}


def descend(root, parts):
    node = root
    for p in parts[:-1]:
        node = node.setdefault(p, {})
    node[parts[-1]] = None
    return node, parts[-1]


SPEC = {"_about": (
    "The token tree build_tokens.py turns into tokens.json. bezi.com is a "
    "Framer build: its --token-<uuid> palette is the product's own orange, "
    "ink, alpha and pastel colours (duplicated uuids folded onto the first "
    "one that resolves to the value). \"var\" leaves resolve through the "
    "live document; \"value\" leaves are measured."),
    "core": {}, "dark": {}, "component": {}}

unmatched = []
seen = {}
for name in sorted(n for n in R if n.startswith("--token-")):
    v = R[name]
    path = PALETTE.get(v)
    if not path:
        unmatched.append((name, v))
        continue
    if v in seen:
        continue  # a second uuid resolving to the same value folds onto the first leaf
    seen[v] = name
    node, last = descend(SPEC["core"].setdefault("color", {}), path.split("."))
    node[last] = {"var": name, "type": "color"}
if unmatched:
    raise SystemExit("unmapped --token colours: " + "; ".join(f"{v} {n}" for n, v in unmatched))

# ------------------------------------------------------------- dark roles
#
# The bundle declares no semantic role names of its own; these roles are
# measured on the painted chrome (header, hero, footer) and point at palette
# tokens where the value matches. The site paints one dark theme, emitted
# under `dark` (the spotify convention for a single painted dark set).
def st(comp, state):
    c = C[comp]
    if c.get("missing") or c.get("recaptureMissed"):
        raise KeyError(comp)
    return c["states"][state]["style"]


def stprop(comp, state, prop):
    """prop may be `styleProp`, `textStyle.prop`, `paint.N.prop` (the Nth
    painted child layer) or the special `ringShadow`: resolve the dotted path
    inside the measured state (the anchors keep UA-default colour, so painted
    text/fill lives on the text child, a sibling layer or a pseudo).
    `ringShadow` returns the colour of the `0 0 0 Npx` ring layer in the
    element's own boxShadow — the hairline many Framer controls paint instead
    of a real border."""
    d = C[comp]["states"][state]
    if prop == "ringShadow":
        sh = d.get("style", {}).get("boxShadow", "") or ""
        for layer in re.split(r",(?![^(]*\))", sh):
            if re.search(r"0px 0px 0px\s+(?:0\.[5-9]|[1-9])[\d.]*px", layer):
                m = re.search(r"rgba?\([^)]*\)|#[0-9a-fA-F]{3,8}", layer)
                if m:
                    return m.group(0)
        return ""
    # A bare property reads the computed style block (backgroundColor); a
    # dotted path walks the state dict (textStyle.color, paint.2.bg,
    # ancestors.0.bg), a numeric step indexing a list. A `.border` tail reads
    # the colour out of the "T:1px solid rgba(...)" string styleOf records.
    if "." not in prop:
        return d.get("style", {}).get(prop, "")
    node = d
    for part in prop.split("."):
        if isinstance(node, list) and part.isdigit():
            node = node[int(part)] if int(part) < len(node) else None
        elif isinstance(node, dict):
            node = node.get(part)
        else:
            return ""
        if node is None:
            return ""
    if isinstance(node, str) and prop.endswith(".border"):
        m = re.search(r"rgba?\([^)]*\)|#[0-9a-fA-F]{3,8}", node)
        return m.group(0) if m else ""
    return node if isinstance(node, str) else ""


def norm_color(v):
    v = (v or "").strip()
    m = re.fullmatch(r"#([0-9a-fA-F]{3,8})", v)
    if m:
        h = m.group(1).lower()
        if len(h) in (3, 4):
            h = "".join(c * 2 for c in h)
        return "#" + h
    m = re.fullmatch(r"rgba?\(([\d.]+),\s*([\d.]+),\s*([\d.]+)(?:,\s*([\d.]+))?\)", v)
    if m:
        r, g, b, a = m.groups()
        if a is None or float(a) >= 1:
            return "#%02x%02x%02x" % (int(float(r)), int(float(g)), int(float(b)))
        return f"rgba({int(float(r))}, {int(float(g))}, {int(float(b))}, {'%g' % float(a)})"
    m = re.fullmatch(r"rgb\(([\d.]+)\s+([\d.]+)\s+([\d.]+)\s*/\s*([\d.]+%?)\)", v)
    if m:
        r, g, b, a = m.groups()
        a = float(a[:-1]) / 100 if a.endswith("%") else float(a)
        return f"rgba({int(float(r))}, {int(float(g))}, {int(float(b))}, {'%g' % a})"
    m = re.fullmatch(r"oklab\(\s*([\d.]+)\s+(-?[\d.]+)\s+(-?[\d.]+)(?:\s*/\s*([\d.]+%?))?\s*\)", v)
    if m:
        # Framer paints some alpha greys as oklab(); convert to sRGB.
        L, A, B = (float(m.group(i)) for i in (1, 2, 3))
        l_ = (L + 0.3963377774 * A + 0.2158037573 * B) ** 3
        m_ = (L - 0.1055613458 * A - 0.0638541729 * B) ** 3
        s_ = (L - 0.0894841775 * A - 1.2914855480 * B) ** 3
        R_ = +4.0767416621 * l_ - 3.3077115913 * m_ + 0.2309699292 * s_
        G_ = -1.2684380046 * l_ + 2.6097574011 * m_ - 0.3413193965 * s_
        B_ = -0.0041960863 * l_ - 0.7034186147 * m_ + 1.7076147010 * s_
        gam = lambda x: max(0, min(255, round((12.92 * x if x <= 0.0031308 else 1.055 * x ** (1 / 2.4) - 0.055) * 255)))
        a = m.group(4)
        a = float(a[:-1]) / 100 if a and a.endswith("%") else float(a) if a else 1
        if a >= 1:
            return "#%02x%02x%02x" % (gam(R_), gam(G_), gam(B_))
        return f"rgba({gam(R_)}, {gam(G_)}, {gam(B_)}, {'%g' % a})"
    return v


BY_VALUE = {}
def collect(node, prefix=""):
    for k, v in node.items():
        if isinstance(v, dict) and "var" in v:
            val = norm_color(R[v["var"]])
            BY_VALUE.setdefault(val, prefix + k)
        elif isinstance(v, dict):
            collect(v, prefix + k + ".")
collect(SPEC["core"].setdefault("color", {}), "color.")


def role(path, comp, state, prop, desc):
    v = norm_color(stprop(comp, state, prop))
    if not v or v == "transparent":
        return
    target = BY_VALUE.get(v)
    leaf = {"type": "color", "description": desc}
    if target:
        leaf["value"] = "{%s}" % target
        leaf["source"] = f"computed {prop} of {comp} {state} (raw/components-computed.json); same value as core.{target}"
    else:
        leaf["value"] = v
        leaf["source"] = f"computed {prop} of {comp} {state} (raw/components-computed.json)"
    node = SPEC["dark"]
    parts = path.split(".")
    for p in parts[:-1]:
        node = node.setdefault(p, {})
    node[parts[-1]] = leaf


for path, comp, state, prop, desc in [
    ("page", "page-ground", "default", "backgroundColor", "The near-black the whole page paints on (body's own fill)."),
    ("surface", "header", "default", "paint.0.bg", "The floating header pill's fill, a translucent near-black over the starfield."),
    ("text", "hero-title", "default", "color", "The display type's white."),
    ("muted", "hero-sub", "default", "textStyle.color", "Secondary text under the hero, painted on the inner span."),
    ("accent", "cta", "default", "paint.0.bg", "The orange CTA fill (painted by a layer inside the control)."),
    ("accentText", "cta", "default", "textStyle.color", "Text painted on the orange CTA (the anchor itself keeps the UA link colour)."),
    ("link", "footer-legal", "default", "color", "The muted legal/footer link colour."),
    ("border", "tools-button", "default", "paint.0.border", "The hairline of the corner-tick chips, rgba(242,241,236,0.32)."),
    ("chip", "announcement", "default", "backgroundColor", "The announcement strip's ground under the header."),
    ("focus", "nav-link", "focus-visible", "outlineColor", "The keyboard-focus ring where one is drawn (the browser's default auto outline)."),
]:
    try:
        role(path, comp, state, prop, desc)
    except KeyError:
        pass

# -------------------------------------------------- measured extras (no var)

meas = SPEC["core"].setdefault("measured", {})
for comp, state, key, prop, desc in [
    ("cta", "hover", "cta-hover", "paint.0.bg", "The CTA fill on hover."),
    ("view-all", "default", "viewall-fill", "backgroundColor", "The VIEW ALL chip's translucent white fill."),
    ("view-all", "default", "arrow-orange", "paint.2.bg", "The orange of the pixel-art arrow inside VIEW ALL."),
    ("plan-cta", "default", "plancta-fill", "paint.0.bg", "The Free band's dark CTA fill on the light-blue card."),
    ("tools-button", "default", "chip-text", "color", "The CONNECTED TOOLS chip's off-white."),
]:
    try:
        v = norm_color(stprop(comp, state, prop))
        if v and v != "transparent":
            meas[key] = {"value": v, "type": "color",
                         "source": f"computed {prop} of {comp} {state} (raw/components-computed.json)",
                         "description": desc}
    except KeyError:
        pass

# ------------------------------------------------------------------ component

comp = SPEC["component"]
for key, cname, state, prop, desc in [
    ("control.heightNav", "nav-link", "default", "height", "Nav controls are 38px."),
    ("control.heightCta", "cta", "default", "height", "The TRY FOR FREE pill height."),
    ("control.radiusPill", "header", "default", "paint.0.radius", "The header pill's corner, 144px."),
    ("header.height", "header", "default", "height", "The full header block at 1440px."),
    ("footer.height", "footer", "default", "height", "The footer block at 1440px."),
]:
    try:
        v = stprop(cname, state, prop)
        if not v:
            continue
        node = comp
        parts = key.split(".")
        for p in parts[:-1]:
            node = node.setdefault(p, {})
        node[parts[-1]] = {"type": "dimension", "value": v,
                           "source": f"computed {prop} of {cname} {state} (raw/components-computed.json)",
                           "description": desc}
    except KeyError:
        pass

(RAW / "component-tokens.json").write_text(json.dumps(SPEC, indent=1, ensure_ascii=False) + "\n")


def count(d):
    if not isinstance(d, dict):
        return 1
    if "var" in d or "value" in d or "$value" in d:
        return 1
    return sum(count(v) for v in d.values())


print({k: count(v) for k, v in SPEC.items() if not k.startswith("_")})
