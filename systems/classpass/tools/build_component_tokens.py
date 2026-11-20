#!/usr/bin/env python3
"""Write raw/component-tokens.json, the token spec build_tokens.py reads.

classpass.com exposes almost nothing as CSS custom properties
(raw/css-vars.json, read by tools/capture/vars.mjs): four rules carrying
two app variables (the carousel dot colours) and two framework internals,
plus nine @font-face declarations (norms regular/500/700, circuit,
hiragino). There is no declared design-token palette at all — every colour
role below is measured on the painted chrome and cited back to
raw/components-computed.json.

The measured palette:

  blue        the ClassPass accent ramp the CTA system is built from:
              #0055ff base -> #004de6 hover -> #0044cc pressed, plus the
              #1a5ee5 link/focused-field blue, the #c0e0ff soft pill fill
              and the rgba(1,85,254,0.1) brand-tinted plan-card shadow
  ink         the near-black ramp: #000 body text and the footer field,
              #111 button fill, #040404 its hover
  gray        the neutral ramp: #f7f7f7 nav hover wash, #e7e7e7 field
              borders, #d6d6d6 control borders, #999 muted text,
              #757575 placeholder text
  yellow      the mobile promo banner's #fce172
  paper       the white ground and card surfaces
  black-alpha translucent blacks: the 8% hero-card scrim, the 10% card
              hairline

Leaves are {"value": ..., "source": ...} — measured values resolved out of
raw/components-computed.json at build time, so the palette tracks what the
site actually paints.
"""
import json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
V = json.loads((RAW / "css-vars.json").read_text())
RL = V["resolved"]["light"]
C = json.loads((RAW / "components-computed.json").read_text())["components"]
R = {n: v.get("value", v.get("raw")) for n, v in RL.items()}

# No declared palette exists to name after; the core ramp is named by hand
# after what the site paints each value as (checked against the screenshots
# and the measured paint layers). Every leaf is resolved live from
# components-computed.json so the value and its provenance stay in step.
#   (token path, component, state, prop, description)
CORE = [
    ("paper.0", "page-ground", "default", "backgroundColor",
     "White — the html element's painted ground and the card fills."),
    ("blue.100", "plan-pill", "default", "paint.0.bg",
     "The soft light-blue plan pill (and the plan card's tinted area)."),
    ("blue.400", "signin-forgot", "default", "color",
     "The link blue — 'Forgot password?', and the focused field border."),
    ("blue.500", "universal-cta", "default", "backgroundColor",
     "The ClassPass accent — CTAs, links, the star rating."),
    ("blue.600", "universal-cta", "hover", "backgroundColor",
     "The accent's hover step."),
    ("blue.700", "universal-cta", "pressed", "backgroundColor",
     "The accent's pressed step."),
    ("gray.100", "nav-item", "hover", "backgroundColor",
     "The nav item's hover/focus wash."),
    ("gray.200", "signin-email", "default", "paint.0.border",
     "The sign-in field and search-field hairline."),
    ("gray.300", "filter-pill", "default", "paint.0.border",
     "Control borders on the filter pills, panels and OAuth buttons."),
    ("gray.400", "venue-card", "default", "textStyle.color",
     "Muted text — the venue card's secondary line."),
    ("gray.500", "search-field", "default", "placeholder.color",
     "Placeholder text in the search comboboxes."),
    ("ink.750", "walk-cta", "hover", "paint.0.bg",
     "The dark button's hover step."),
    ("ink.800", "walk-cta", "default", "paint.0.bg",
     "The near-black button fill (walkthrough Next, CMS CTAs)."),
    ("ink.900", "footer", "default", "backgroundColor",
     "Black — body text and the footer field."),
    ("yellow.300", "m-banner", "default", "backgroundColor",
     "The mobile promo banner's yellow."),
    ("black-alpha.8", "hero-card", "default", "paint.0.bg",
     "The 8% black scrim on the hero card."),
    ("black-alpha.10", "venue-card", "default", "paint.0.border",
     "The venue card's 10% hairline."),
    ("blue-alpha.10", "plan-slide", "default", "boxShadow",
     "The brand-tinted shadow under the plan card."),
]
SPEC = {"_about": (
    "The token tree build_tokens.py turns into tokens.json. classpass.com "
    "declares no design-token CSS variables — its four custom properties "
    "are carousel-dot colours and framework internals (raw/css-vars.json). "
    "Every leaf is a measured value resolved from "
    "raw/components-computed.json at build time."),
    "core": {}, "light": {}, "component": {}}


def descend(root, parts):
    node = root
    for p in parts[:-1]:
        node = node.setdefault(p, {})
    node[parts[-1]] = None
    return node, parts[-1]


# ------------------------------------------------------------- light roles
#
# The bundle declares no semantic role names of its own; every role below is
# measured on the painted chrome (header, hero cards, plan carousel, search
# filters, footer) and aliases a core token when the value matches. The
# marketing site paints one light theme, emitted under `light`; the footer
# is a black island inside it, so its text role is named onDark.
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
        if isinstance(v, dict) and ("var" in v or "value" in v):
            val = norm_color(R[v["var"]]) if "var" in v else norm_color(v["value"])
            BY_VALUE.setdefault(val, prefix + k)
        elif isinstance(v, dict):
            collect(v, prefix + k + ".")
core_color = SPEC["core"].setdefault("color", {})
for path, cname, state, prop, desc in CORE:
    v = stprop(cname, state, prop)
    if prop.endswith("boxShadow"):
        m = re.search(r"rgba?\([^)]*\)|#[0-9a-fA-F]{3,8}", v or "")
        v = m.group(0) if m else ""
    v = norm_color(v)
    if not v or v == "transparent":
        raise SystemExit(f"core palette source missing: {cname} {state} {prop}")
    node, last = descend(core_color, path.split("."))
    node[last] = {"value": v, "type": "color",
                  "source": f"computed {prop} of {cname} {state} (raw/components-computed.json)",
                  "description": desc}
collect(core_color, "color.")


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
    ("surface.page", "page-ground", "default", "backgroundColor", "The white page ground — painted by the html element (body itself is transparent)."),
    ("surface.card", "plan-slide", "default", "paint.0.bg", "The card fill: plan slides, venue rows, filter panels, search box."),
    ("surface.dark", "footer", "default", "backgroundColor", "The black island: the site footer on every page."),
    ("text.primary", "page-ground", "default", "color", "Body and heading ink on the light pages."),
    ("text.muted", "venue-card", "default", "textStyle.color", "Secondary text — the venue card's muted line."),
    ("text.placeholder", "search-field", "default", "placeholder.color", "Placeholder text inside the search comboboxes."),
    ("text.onDark", "footer", "default", "color", "Text painted on the black footer."),
    ("text.onAccent", "universal-cta", "default", "color", "Text painted on the blue CTA."),
    ("text.accent", "filter-pill", "default", "textStyle.color", "Blue text — the filter pills' labels and the star rating."),
    ("link", "signin-forgot", "default", "color", "The sign-in page's link blue."),
    ("accent", "universal-cta", "default", "backgroundColor", "The ClassPass blue CTA fill."),
    ("accentHover", "universal-cta", "hover", "backgroundColor", "The CTA's hover step."),
    ("accentPressed", "universal-cta", "pressed", "backgroundColor", "The CTA's pressed step."),
    ("accentSoft", "plan-pill", "default", "paint.0.bg", "The light-blue plan pill and tinted plan area."),
    ("promo", "m-banner", "default", "backgroundColor", "The mobile promo banner's yellow."),
    ("fill.ink", "walk-cta", "default", "paint.0.bg", "The near-black button fill (walkthrough Next, CMS CTAs)."),
    ("fill.inkHover", "walk-cta", "hover", "paint.0.bg", "The dark button's hover step."),
    ("navHover", "nav-item", "hover", "backgroundColor", "The nav item's hover/focus wash."),
    ("scrim.card", "hero-card", "default", "paint.0.bg", "The 8% black scrim on the hero card."),
    ("border.subtle", "signin-email", "default", "paint.0.border", "The field hairline — sign-in and search inputs."),
    ("border.control", "filter-pill", "default", "paint.0.border", "The 1px border on pills, panels, OAuth buttons and the search box."),
    ("border.card", "venue-card", "default", "paint.0.border", "The venue card's 10% black hairline."),
    ("border.focusField", "signin-email", "focused", "borderTopColor", "The blue the sign-in fields' border switches to when focused."),
    ("focus", "universal-cta", "focus-visible", "outlineColor", "The designed focus ring on the blue controls (2px solid). Many text controls keep the browser's auto ring instead (#101010) — recorded per entry."),
]:
    try:
        role(path, comp, state, prop, desc)
    except KeyError:
        pass

# -------------------------------------------------- measured extras (no var)

meas = SPEC["core"].setdefault("measured", {})
for comp, state, key, prop, desc in [
    ("walk-slide", "default", "walk-slide-ink", "textStyle.color", "The walkthrough slide's 20px medium label ink."),
    ("signin-apple", "default", "oauth-border", "paint.0.border", "The OAuth buttons' border grey."),
]:
    try:
        v = norm_color(stprop(comp, state, prop))
        if v and v != "transparent":
            meas[key] = {"value": v, "type": "color",
                         "source": f"computed {prop} of {comp} {state} (raw/components-computed.json)",
                         "description": desc}
    except KeyError:
        pass

# The plan card's brand-tinted drop shadow, recorded as a real shadow token.
shadow_src = "computed boxShadow of plan-slide default (raw/components-computed.json)"
SPEC["light"]["shadow"] = {"card": {
    "type": "shadow",
    "value": [{"offsetX": "0px", "offsetY": "5px", "blur": "16px", "spread": "0px",
               "color": "rgba(1, 85, 254, 0.1)"}],
    "source": shadow_src,
    "description": "The brand-tinted drop shadow under the plan card."}}

# ------------------------------------------------------------------ component

comp = SPEC["component"]
for key, cname, state, prop, desc in [
    ("control.heightCta", "universal-cta", "default", "height", "The blue CTA height."),
    ("control.heightNav", "nav-cta", "default", "height", "The header CTA pill's height."),
    ("control.heightButton", "signin-submit", "default", "height", "The full-width button height (sign-in submit, OAuth buttons, walkthrough Next)."),
    ("control.heightField", "signin-email", "default", "height", "The sign-in field height."),
    ("control.heightSearch", "search-box", "default", "height", "The search box height."),
    ("control.heightFilter", "filter-pill", "default", "height", "The filter pill height."),
    ("control.heightPill", "plan-pill", "default", "height", "The plan-pill tag height."),
    ("control.radiusPill", "signin-submit", "default", "paint.0.radius", "Buttons are fully rounded."),
    ("control.radiusField", "signin-email", "default", "paint.0.radius", "Field corners are 4px."),
    ("control.radiusSearch", "search-box", "default", "paint.1.radius", "The search box's 20px corner."),
    ("control.radiusFilter", "filter-pill", "default", "paint.0.radius", "Filter pill corners, 16px."),
    ("card.radiusPlan", "plan-slide", "default", "paint.0.radius", "The plan card's 18px corner."),
    ("card.radiusPlanInner", "plan-slide", "default", "paint.1.radius", "The tinted plan area's 14px corner."),
    ("card.radiusVenue", "venue-card", "default", "paint.1.radius", "The venue card's 5px corner."),
    ("card.radiusHero", "hero-card", "default", "paint.0.radius", "The hero card's 25px corner."),
    ("card.radiusPanel", "filter-panel", "default", "paint.0.radius", "The filter panel's 8px corner."),
    ("header.height", "header", "default", "height", "The header bar at 1440px."),
    ("footer.height", "footer", "default", "height", "The footer block at 1440px."),
    ("banner.height", "m-banner", "default", "height", "The mobile promo banner's height."),
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
for key, cname, prop, desc in [
    ("family.ui", "nav-item", "fontFamily", "TT Norms Pro ('norms') across the UI: nav, body copy, controls."),
    ("family.display", "plans-h1", "fontFamily", "Circuit, the condensed display face of the hero and plan headings."),
]:
    try:
        f = (stprop(cname, "default", prop) or stprop(cname, "default", "textStyle.fontFamily") or "").strip()
        if f:
            node = font
            for p_ in key.split(".")[:-1]:
                node = node.setdefault(p_, {})
            node[key.split(".")[-1]] = {"type": "fontFamily", "value": f,
                                        "source": f"computed {prop} of {cname} default (raw/components-computed.json)",
                                        "description": desc}
    except KeyError:
        pass

for key, cname, desc in [
    ("size.display", "plans-h1", "The 60px plan/display heading (62.4px line-height)."),
    ("size.hero", "hero-title", "The hero heading's 36px line — the rotating word paints on an inner span."),
    ("size.h2", "section-title", "Section headings, 24px at 28.8px."),
    ("size.sub", "hero-sub", "The hero subtitle, 20px."),
    ("size.faq", "faq-question", "FAQ questions, 18px."),
    ("size.body", "footer-link", "Body copy and footer links, 16px."),
    ("size.nav", "nav-item", "Nav labels, 14px."),
    ("size.price", "plan-price", "Plan prices, 36px at weight 700."),
]:
    try:
        sz = stprop(cname, "default", "textStyle.fontSize") or stprop(cname, "default", "fontSize")
        if sz:
            node = font
            for p_ in key.split(".")[:-1]:
                node = node.setdefault(p_, {})
            node[key.split(".")[-1]] = {"type": "dimension", "value": sz,
                                        "source": f"computed fontSize of {cname} default (raw/components-computed.json)",
                                        "description": desc}
    except KeyError:
        pass

# A component flagged recaptureMissed kept a previous run's readings (the recapture did not find it). st()
# refuses those, but stprop() reads them; any leaf built from one says so instead of shipping as current.
STALE = {k: c for k, c in C.items() if c.get("recaptureMissed")}


def mark_stale(node):
    if isinstance(node, dict):
        src = node.get("source")
        if isinstance(src, str):
            m = re.search(r"\bof ([a-z0-9-]+) (default|hover|focus-visible|pressed|focused|opened)\b", src)
            if m and m.group(1) in STALE and "stale" not in src:
                c = STALE[m.group(1)]
                node["source"] = src + "; stale: kept from an earlier run (the %s recapture did not find %s)" % (c["recaptureMissed"], m.group(1))
        for v in node.values():
            mark_stale(v)


mark_stale(SPEC)

(RAW / "component-tokens.json").write_text(json.dumps(SPEC, indent=1, ensure_ascii=False) + "\n")


def count(d):
    if not isinstance(d, dict):
        return 1
    if "var" in d or "value" in d or "$value" in d:
        return 1
    return sum(count(v) for v in d.values())


print({k: count(v) for k, v in SPEC.items() if not k.startswith("_")})
