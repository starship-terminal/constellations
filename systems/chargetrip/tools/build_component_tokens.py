#!/usr/bin/env python3
"""Write raw/component-tokens.json, the token spec build_tokens.py reads.

chargetrip.com is a Framer site; its bundle declares on `body`
(raw/css-vars.json, read by tools/capture/vars.mjs):

  --token-<uuid>   the project's palette, 28 declarations covering 20 unique
                   values (several uuids repeat #262322, #f94d00, #dd3b00,
                   #f4f3f2 and #ffecd2; the repeats are folded onto the first
                   uuid that resolves to the value):
                   * a warm paper ramp the light pages are built from
                     (#fffffb -> #c7c0aa) -> color.paper.*
                   * a warm ink ramp for text and dark fills -> color.ink.*
                   * an orange ramp around the CTA colour #f94d00, plus its
                     12% tint and 15% nav-hover wash -> color.orange.*
                   * the two green status colours -> color.green.*
                   * translucent warm whites/neutrals for scrims and muted
                     text over the dark hero -> color.white-alpha.* /
                     color.paper-alpha.*
  --framer-*       Framer's own layout/effect internals, not a design scale;
                   recorded in css-vars.json but not tokenised
  83 @font-face    Inter, Geist (ui), Cirka (display serif), Fragment/Geist
                   Mono, recorded in css-vars.json

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
#   paper        the warm off-white ramp the light pages, cards and footer are
#                built from (#fffffb page card -> #c7c0aa the darkest cream)
#   ink          the warm dark ramp: body text #262322, dark fills #44403f,
#                hover lift #59524f, muted text #877f78
#   orange       the CTA/highlight ramp around #f94d00 plus its 12% tint
#   green        the "All systems" status-dot ramp
#   white-alpha  translucent warm whites: muted text and scrims over the
#                dark hero and dark plan card
#   paper-alpha  translucent creams: the dark card's hairline washes
PALETTE = {
    # paper ramp, lightest to darkest
    "#fffffb": "paper.0", "#f4f3f2": "paper.100", "#efede5": "paper.200",
    "#e4e1d5": "paper.300", "#c8c5c0": "paper.400", "#c7c0aa": "paper.500",
    # warm ink ramp, lightest to darkest
    "#877f78": "ink.300", "#59524f": "ink.500", "#4d4846": "ink.600",
    "#44403f": "ink.700", "#262322": "ink.800", "#2c241e": "ink.900",
    # orange ramp, lightest to darkest; .500 is the painted CTA colour
    "#ffecd2": "orange.100", "#fa6d2e": "orange.400", "#f94d00": "orange.500",
    "#dd3b00": "orange.600", "#a32c09": "orange.700",
    "rgba(249, 77, 0, 0.12)": "orange.alpha-12",
    # green status ramp
    "#2c9a65": "green.500", "#0d7b46": "green.600",
    # translucent warm whites over dark surfaces
    "rgba(255, 255, 251, 0.52)": "white-alpha.52",
    # translucent creams (hairlines and washes on the dark card)
    "rgba(199, 192, 170, 0.2)": "paper-alpha.20",
}


def descend(root, parts):
    node = root
    for p in parts[:-1]:
        node = node.setdefault(p, {})
    node[parts[-1]] = None
    return node, parts[-1]


SPEC = {"_about": (
    "The token tree build_tokens.py turns into tokens.json. chargetrip.com "
    "is a Framer build: its --token-<uuid> palette is the product's own "
    "paper, ink, orange, green and alpha colours (duplicated uuids folded "
    "onto the first one that resolves to the value). \"var\" leaves resolve "
    "through the live document; \"value\" leaves are measured."),
    "core": {}, "light": {}, "component": {}}

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

# ------------------------------------------------------------- light roles
#
# The bundle declares no semantic role names of its own; these roles are
# measured on the painted chrome (header, hero, plan cards, footer) and
# point at palette tokens where the value matches. The marketing site paints
# one light theme, emitted under `light`; the hero and the "Popular" plan
# card are dark islands inside it, so their text roles are named onDark.
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
    m = re.fullmatch(r"oklch\(\s*([\d.]+%?)\s+([\d.]+)\s+([\d.]+)(?:\s*/\s*([\d.]+%?))?\s*\)", v)
    if m:
        # account.chargetrip.io's Tailwind v4 sheet paints oklch(); convert
        # through OKLab to sRGB so the token is a usable colour value.
        import math
        L = float(m.group(1).rstrip("%"))
        if m.group(1).endswith("%"):
            L /= 100
        C_, H = float(m.group(2)), math.radians(float(m.group(3)))
        A, B = C_ * math.cos(H), C_ * math.sin(H)
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
    node = SPEC["light"]
    parts = path.split(".")
    for p in parts[:-1]:
        node = node.setdefault(p, {})
    node[parts[-1]] = leaf


for path, comp, state, prop, desc in [
    ("surface.page", "page-ground", "default", "backgroundColor", "The warm-cream page ground (the body element's own fill, painted identically at both widths)."),
    ("surface.card", "plan-card", "default", "paint.0.bg", "The plan-card and footer-panel fill, a near-white on the cream page."),
    ("surface.dark", "plan-card-dark", "default", "paint.0.bg", "The dark island: the hero band and the 'Popular' plan card."),
    ("text.primary", "section-title", "default", "color", "Body and heading ink on the light pages."),
    ("text.muted", "footer", "default", "textStyle.color", "Secondary text on the light pages: the footer's column headings (Products, Resources)."),
    ("text.onDark", "hero-title", "default", "color", "Text painted on the dark hero band and dark plan card."),
    ("text.onDarkMuted", "hero-sub", "default", "color", "Muted text on the dark hero band."),
    ("accent", "cta-accent", "default", "paint.0.bg", "The orange CTA fill (painted by a layer inside the control)."),
    ("accentText", "cta-accent", "default", "textStyle.color", "Text painted on the orange CTA."),
    ("fill.ink", "nav-cta", "default", "paint.0.bg", "The dark pill fill (nav CTA, sign-in submit, logo-chip band)."),
    ("fill.inkHover", "form-submit", "hover", "paint.0.bg", "The lifted ink the dark pills pick up on hover."),
    ("navHover", "nav-item", "hover", "paint.0.bg", "The translucent orange wash behind a nav item on hover."),
    ("border.subtle", "plan-card", "default", "paint.1.border", "The dashed cream hairline inside the light plan card."),
    ("border.onDark", "plan-card-dark", "default", "paint.1.border", "The dashed ink hairline inside the dark plan card."),
    ("status.online", "status-pill", "default", "paint.0.bg", "The 'All systems operational' dot: the only painted child (8 x 8, radius 100%) of the footer column the status-pill selector caught."),
    ("focus", "cta-accent", "focus-visible", "outlineColor", "The keyboard-focus ring the header/footer controls draw (1px auto); plan, slider and form controls still draw the #005fcc ring — recorded per entry."),
]:
    try:
        role(path, comp, state, prop, desc)
    except KeyError:
        pass

# -------------------------------------------------- measured extras (no var)

meas = SPEC["core"].setdefault("measured", {})
for comp, state, key, prop, desc in [
    ("cta-accent", "default", "cta-orbit", "paint.1.bg", "The decorative orange disc behind the CTA group."),
    ("cta-accent", "default", "cta-orbit-deep", "paint.2.bg", "The darker orange disc layered under it."),
    ("plan-cta-dark", "default", "dark-orbit", "paint.1.bg", "The lifted-ink disc inside the dark plan card."),
    ("form-input", "default", "form-ink", "color", "The sales-form field text, a near-black teal unrelated to the ink ramp."),
    ("signin-create", "default", "signin-paper", "backgroundColor", "The account.chargetrip.io 'Create account' card fill (oklch, resolved)."),
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
    ("control.heightCta", "cta-accent", "default", "height", "The hero/marketing CTA button height."),
    ("control.heightNav", "nav-cta", "default", "height", "Header pills are 40px."),
    ("control.heightPlan", "plan-cta", "default", "height", "The plan-card CTA height."),
    ("control.heightInput", "signin-input", "default", "height", "The sign-in field height on account.chargetrip.io."),
    ("control.radiusButton", "cta-accent", "default", "paint.0.radius", "CTA corners are 8px."),
    ("control.radiusSubmit", "form-submit", "default", "paint.0.radius", "The sales-form submit corners, 10px."),
    ("card.radiusPlan", "plan-card", "default", "paint.0.radius", "The light plan card's 24px corner."),
    ("card.radiusPlanDark", "plan-card-dark", "default", "paint.0.radius", "The dark plan card's 16px corner."),
    ("card.radiusDemo", "demo-card", "default", "paint.0.radius", "The demo-card's 12px corner."),
    ("header.height", "header", "default", "height", "The header block at 1440px."),
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

# ------------------------------------------------------------- typography
#
# The bundle declares no type-scale variables; families, sizes, weights and
# line-heights are measured on the components that paint them. Families land
# under core.font.family, the measured scale under core.font.size with the
# line-height paired in the description.

font = SPEC["core"].setdefault("font", {})
for key, cname, desc in [
    ("family.ui", "cta-accent", "Geist Variable across the UI: controls, nav, body copy (Placeholder is Framer's in-canvas stand-in)."),
    ("family.display", "plan-card", "Cirka, the editorial serif of the display headings and plan-card prices."),
]:
    try:
        f = (stprop(cname, "default", "textStyle.fontFamily") or "").strip()
        if f:
            node = font
            for p in key.split(".")[:-1]:
                node = node.setdefault(p, {})
            node[key.split(".")[-1]] = {"type": "fontFamily", "value": f,
                                        "source": f"computed textStyle.fontFamily of {cname} default (raw/components-computed.json)",
                                        "description": desc}
    except KeyError:
        pass

for key, cname, desc in [
    ("size.display", "hero-title", "The hero's 88px display serif (78px line-height)."),
    ("size.h1", "contact-h1", "The page-H1 size away from the home hero, 64px."),
    ("size.h2", "section-title", "Section headings, 48px at 48px line-height."),
    ("size.body", "nav-item", "Nav and body copy, 18px at 28.8px."),
    ("size.control", "cta-accent", "Control labels, 16px at 24px."),
    ("size.small", "footer-link", "Footer links and check-list items, 16px at 22.4px."),
]:
    try:
        sz = stprop(cname, "default", "textStyle.fontSize") or stprop(cname, "default", "fontSize")
        if sz:
            node = font
            for p in key.split(".")[:-1]:
                node = node.setdefault(p, {})
            node[key.split(".")[-1]] = {"type": "dimension", "value": sz,
                                        "source": f"computed textStyle.fontSize of {cname} default (raw/components-computed.json)",
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
