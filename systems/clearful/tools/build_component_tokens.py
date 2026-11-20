#!/usr/bin/env python3
"""Write raw/component-tokens.json, the token spec build_tokens.py reads.

Clearful's marketing site is a Webflow build (stable Webflow class names,
Manrope UI text, Literatatt display), its /library route a separate
Tailwind build in Mulish, and its sign-in (app.clearful.com) a Flutter
canvas app measured through the semantics overlay at devicePixelRatio 1 —
the canvas paints its own colours, which CSSOM cannot read; the app-surface
values below are pixel-sampled from the full-colour sign-in screenshot and
documented as such.

Unlike the previous captures, the Webflow stylesheet DOES declare a real
design-token palette (raw/css-vars.json, tools/capture/vars.mjs — the CDN
sheet is cross-origin, so vars.mjs fetches and reparses it directly): a
ten-step base-color-brand--blue ramp, a ten-step grey ramp plus white,
four radius steps and a full semantic layer (text-color--text-*,
background-color--background-*, border-color--border-*, button-color--*,
tabs-color--tabs-*). Declared leaves cite the custom property name; every
role below is still measured on the painted chrome and cited back to
raw/components-computed.json — declarations say what Clearful named, the
measurements say what it paints.

The site paints ONE light theme (white ground, #f7f7f7 secondary bands,
#d6e0ff brand-light sections, #1953ff brand controls). The Flutter
sign-in is a second stack's surface, not a second theme; its handful of
sampled values sit under core.sampled.app.*.

The measured palette:

  blue      #1953ff brand blue (blue-500) -> #1b1bbc hover/pressed
            (blue-600, shipped under a deleted variable), #adc2ff the
            hero CTA's halo ring (blue-200), #d6e0ff brand-light bands
            (blue-100), #001452 navy headings (blue-900)
  grey      #f7f7f7 secondary surface (grey-000) -> #222 primary ink
            (grey-900); #515151 muted text (grey-700); #e1e1e1 hairline
            (grey-100)
  app       the Flutter sign-in's own shades: #f7f7f7 ground, #222 Apple
            button, #1a73e8 Google button, white email button — all
            pixel-sampled, canvas-painted
"""
import json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
V = json.loads((RAW / "css-vars.json").read_text())
# clearful paints light only (catalog theme list): resolve against the light pass, never a dark probe.
RL = V["resolved"]["light"]
C = json.loads((RAW / "components-computed.json").read_text())["components"]
R = {n: v.get("value", v.get("raw")) for n, v in RL.items()}

# The Webflow sheet declares the whole ramp, so core names follow the
# declaration: declared leaves resolve through R (the var name stays the
# provenance). The few core shades the site paints without declaring
# (the #1b1bbc hover step lives under a deleted variable, the #101010
# focus ring is a UA colour) are measured leaves cited to the component.
#   (token path, declared var name OR component tuple, description)
DECLARED = [
    ("blue.50", "--base-color-brand--blue-50", "Declared blue-50 (#ebf0ff)."),
    ("blue.100", "--base-color-brand--blue-100", "Declared blue-100 (#d6e0ff) — the brand-light section bands."),
    ("blue.200", "--base-color-brand--blue-200", "Declared blue-200 (#adc2ff) — the hero CTA's halo ring."),
    ("blue.300", "--base-color-brand--blue-300", "Declared blue-300 (#809fff)."),
    ("blue.400", "--base-color-brand--blue-400", "Declared blue-400 (#4d79ff)."),
    ("blue.500", "--base-color-brand--blue-500", "Declared blue-500 (#1953ff) — the brand blue: CTAs, hover links, footer dots."),
    ("blue.600", "--base-color-brand--blue-600", "Declared blue-600 (#0039e6)."),
    ("blue.hover", "--base-color-brand--blue-600<deleted|variable-78f99fb0>",
     "Declared #1b1bbc — the hover/pressed step on every blue control, shipped under a tombstoned duplicate of blue-600."),
    ("blue.700", "--base-color-brand--blue-700", "Declared blue-700 (#002db3)."),
    ("blue.800", "--base-color-brand--blue-800", "Declared blue-800 (#002185)."),
    ("blue.900", "--base-color-brand--blue-900", "Declared blue-900 (#001452) — the navy heading ink."),
    ("blue.950", "--base-color-brand--blue-950", "Declared blue-950 (#000e38)."),
    ("grey.000", "--base-color-neutral--grey-000", "Declared grey-000 (#f7f7f7) — the secondary surface."),
    ("grey.100", "--base-color-neutral--grey-100", "Declared grey-100 (#e1e1e1) — the hairline border."),
    ("grey.200", "--base-color-neutral--grey-200", "Declared grey-200 (#cfcfcf)."),
    ("grey.300", "--base-color-neutral--grey-300", "Declared grey-300 (#b1b1b1)."),
    ("grey.400", "--base-color-neutral--grey-400", "Declared grey-400 (#9e9e9e)."),
    ("grey.500", "--base-color-neutral--grey-500", "Declared grey-500 (#7e7e7e)."),
    ("grey.600", "--base-color-neutral--grey-600", "Declared grey-600 (#626262)."),
    ("grey.700", "--base-color-neutral--grey-700", "Declared grey-700 (#515151) — muted/footer text."),
    ("grey.800", "--base-color-neutral--grey-800", "Declared grey-800 (#3b3b3b)."),
    ("grey.900", "--base-color-neutral--grey-900", "Declared grey-900 (#222222) — the primary ink."),
    ("white", "--base-color-neutral--white", "Declared white (#ffffff) — the page ground and card fill."),
    ("black", "--base-color-neutral--black", "Declared black (#000000) — the library stack's body ink."),
]
CORE = [
    ("focus.0", "nav-cta", "focus-visible", "outlineColor",
     "#101010 — the 1px focus ring on this surface's controls."),
]
SPEC = {"_about": (
    "The token tree build_tokens.py turns into tokens.json. Clearful's "
    "Webflow stylesheet declares a real palette and semantic layer "
    "(raw/css-vars.json); the core ramps below are those declared values "
    "resolved at build time, with measured leaves for the few shades the "
    "site paints without declaring. Semantic roles are measured on the "
    "painted chrome in raw/components-computed.json and alias the core "
    "when the value matches. One theme exists (light); the Flutter "
    "sign-in's sampled shades live under core.sampled.app.*."),
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
        # Sheets can paint oklch(); convert through OKLab to sRGB so the
        # token is a usable colour value.
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
for path, var, desc in DECLARED:
    v = R.get(var)
    if not v:
        raise SystemExit(f"declared var missing: {var}")
    node, last = descend(core_color, path.split("."))
    node[last] = {"value": norm_color(v), "type": "color",
                  "source": f"declared {var} (raw/css-vars.json)",
                  "description": desc}
for path, cname, state, prop, desc in CORE:
    v = stprop(cname, state, prop)
    if "shadow" in prop.lower():
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
    v = stprop(comp, state, prop)
    if "shadow" in prop.lower():
        m = re.search(r"rgba?\([^)]*\)|#[0-9a-fA-F]{3,8}", v or "")
        v = m.group(0) if m else ""
    v = norm_color(v)
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
    theme, _, rest = path.partition(":")
    node = SPEC[theme or "dark"]
    parts = rest.split(".")
    for p in parts[:-1]:
        node = node.setdefault(p, {})
    node[parts[-1]] = leaf



for path, comp, state, prop, desc in [
    # ----- the single light surface (marketing routes, library, footer)
    ("light:surface.page", "page-ground", "default", "backgroundColor", "The white page ground — painted by the body (declared --background-color--background-primary = white)."),
    ("light:surface.secondary", "feature-card", "default", "backgroundColor", "The #f7f7f7 band — feature cards, feature rows, the footer (declared --background-color--background-secondary)."),
    ("light:surface.card", "prompt-card", "default", "backgroundColor", "The library prompt cards' white fill over the grey band."),
    ("light:surface.brandLight", "section-accent", "default", "backgroundColor", "The #d6e0ff brand-light band — mid-page accent sections (declared --background-color--background-brand-light)."),
    ("light:surface.hover", "nav-item", "hover", "backgroundColor", "The #f7f7f7 hover wash behind nav links."),
    ("light:text.primary", "nav-item", "default", "color", "The primary ink #222 — nav, body, buttons' borders (declared --text-color--text-primary)."),
    ("light:text.muted", "footer-link", "default", "color", "Muted text #515151 — footer links (declared --text-color--text-secondary)."),
    ("light:text.navy", "section-title", "default", "color", "Navy headings #001452 inside the brand-light bands (blue-900)."),
    ("light:text.accent", "footer-link", "hover", "color", "The brand blue as text — footer-link hover."),
    ("light:text.onAccent", "nav-cta", "default", "color", "White text on the blue controls (declared --text-color--text-alternate)."),
    ("light:text.appInk", "prompt-card", "default", "color", "#000 on the library cards — the Tailwind stack's body ink."),
    ("light:accent", "nav-cta", "default", "backgroundColor", "The brand blue — nav CTA, hero CTA, plan buttons (declared --button-color--button-brand-blue)."),
    ("light:accentHover", "nav-cta", "hover", "backgroundColor", "#1b1bbc — the hover/pressed step on every blue control (declared under a tombstoned blue-600 variable)."),
    ("light:ring.cta", "cta", "default", "paint.0.border", "The hero CTA's 6px #adc2ff halo ring (blue-200)."),
    ("light:border.subtle", "header", "default", "paint.0.border", "The #e1e1e1 hairline — header, footer, nav-item hover (declared --border-color--border-primary)."),
    ("light:border.brand", "nav-cta", "default", "borderTopColor", "The 1px brand-blue border on the blue pills (declared --border-color--border-brand-blue)."),
    ("light:border.tab", "billing-tab", "default", "color", "The pricing tabs' ink — Monthly/Yearly labels."),
    ("light:focus", "nav-cta", "focus-visible", "outlineColor", "The 1px #101010 focus ring — UA-style ring, consistent across the surface's controls."),
]:
    try:
        role(path, comp, state, prop, desc)
    except KeyError:
        pass

# ----- the Flutter sign-in surface: canvas-painted, CSSOM-blind
#
# The sign-in card paints on a Flutter canvas. These values are sampled
# straight off the full-colour sign-in screenshot (1440x900 at dsf1, kept
# outside the repo) at the measured control rects: painted pixels, not a
# stylesheet or computed-style reading. docs/EVIDENCE.md labels them Sampled
# and keeps them out of the semantic sets, so they live under core.sampled.
for path, hexval, pt, desc in [
    ("core:sampled.app.ground", "#f7f7f7", "60,450", "The sign-in page's grey ground — sampled off the screenshot at (60,450)."),
    ("core:sampled.app.oauth.ink", "#222222", "720,486", "The Continue-with-Apple button's near-black fill — sampled at the button centre."),
    ("core:sampled.app.oauth.google", "#1a73e8", "720,540", "The Continue-with-Google button's Google blue — sampled at the button centre."),
    ("core:sampled.app.oauth.email", "#ffffff", "720,412", "The Continue-with-email button's white fill — sampled at the button centre."),
    ("core:sampled.app.text.primary", "#222222", "720,417", "The sign-in card's ink — sampled on the email button's label."),
]:
    leaf = {"value": hexval, "type": "color", "description": desc,
            "source": f"Sampled: a screenshot pixel of the full-colour sign-in capture (kept outside the repo) at ({pt}); canvas-painted, CSSOM-blind, no element reading holds it"}
    theme, _, rest = path.partition(":")
    node = SPEC[theme]
    for p in rest.split(".")[:-1]:
        node = node.setdefault(p, {})
    node[rest.split(".")[-1]] = leaf

# -------------------------------------------------- measured extras (no var)

meas = SPEC["core"].setdefault("measured", {})
for comp, state, key, prop, desc in [
]:
    try:
        v = norm_color(stprop(comp, state, prop))
        if v and v != "transparent":
            meas[key] = {"value": v, "type": "color",
                         "source": f"computed {prop} of {comp} {state} (raw/components-computed.json)",
                         "description": desc}
    except KeyError:
        pass

# The prompt card's two-layer drop shadow (the third stack's only elevation).
SPEC["light"]["shadow"] = {
    "card": {
        "type": "shadow",
        "value": [{"offsetX": "0px", "offsetY": "4px", "blur": "6px", "spread": "-1px",
                   "color": "rgba(0, 0, 0, 0.1)"},
                  {"offsetX": "0px", "offsetY": "2px", "blur": "4px", "spread": "-2px",
                   "color": "rgba(0, 0, 0, 0.1)"}],
        "source": "computed boxShadow of prompt-card default (raw/components-computed.json)",
        "description": "The library prompt card's Tailwind shadow-md — the only painted elevation on the captured surface."},
}

# Declared radii: the sheet ships a four-step radius scale the pills override
# with a 999px cap.
rad = SPEC["core"].setdefault("radius", {})
for key, var, desc in [
    ("small", "--border-radius--border-radius-small", "Declared radius-small (4px)."),
    ("medium", "--border-radius--border-radius-medium", "Declared radius-medium (8px) — feature rows."),
    ("large", "--border-radius--border-radius-large", "Declared radius-large (16px) — prompt cards, small pills."),
    ("xlarge", "--border-radius--border-radius-xlarge", "Declared radius-xlarge (24px) — feature cards."),
]:
    v = R.get(var)
    if v:
        rad[key] = {"value": v, "type": "dimension",
                    "source": f"declared {var} (raw/css-vars.json)",
                    "description": desc}

# ------------------------------------------------------------------ component

comp = SPEC["component"]
for key, cname, state, prop, desc in [
    ("control.heightNavCta", "nav-cta", "default", "height", "The nav Start-a-journal pill, 50px."),
    ("control.heightCta", "cta", "default", "height", "The hero CTA's 82px pill."),
    ("control.heightPlanCta", "plan-cta", "default", "height", "The pricing cards' action button, 58px."),
    ("control.heightNavItem", "nav-item", "default", "height", "Nav links, 40px."),
    ("control.heightTab", "billing-tab", "default", "height", "The billing tabs, 40px."),
    ("control.heightHamburger", "m-menu-button", "default", "height", "The mobile menu button, 48px."),
    ("control.radiusPill", "cta", "default", "paint.0.radius", "The 999px cap on every button pill."),
    ("card.radiusFeature", "feature-card", "default", "borderTopLeftRadius", "Feature card corners, 24px."),
    ("card.radiusPrompt", "prompt-card", "default", "borderTopLeftRadius", "Library prompt-card corners, 16px."),
    ("card.radiusFeatureRow", "feature-row", "default", "borderTopLeftRadius", "Feature-row corners, 8px."),
    ("nav.height", "header", "default", "height", "The nav bar at 1440px, 72px."),
    ("footer.height", "footer", "default", "height", "The footer block at 1440px."),
    ("drawer.height", "m-menu-open", "default", "height", "The mobile menu overlay at 390px, 844px."),
    ("heroTitle.width", "hero-title", "default", "width", "The hero display line's measure, 1024px."),
    ("signin.buttonHeight", "signin-button", "default", "height", "The sign-in card's buttons, 56px."),
    ("signin.buttonWidth", "signin-button", "default", "width", "The sign-in card's buttons, 400px."),
    ("signin.cardImageWidth", "signin-image", "default", "width", "The sign-in card's illustration slot, 264px."),
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
# No type-scale variables are declared; families, sizes, weights and
# line-heights are measured on the components that paint them. Families land
# under core.font.family, the measured scale under core.font.size with the
# line-height paired in the description.

font = SPEC["core"].setdefault("font", {})
for key, cname, prop, desc in [
    ("family.display", "hero-title", "fontFamily", "Literatatt — the display face of hero, section and pricing headings."),
    ("family.ui", "nav-item", "fontFamily", "Manrope — UI text across the Webflow surface: nav, body, buttons."),
    ("family.library", "library-h1", "fontFamily", "Mulish — the /library Tailwind stack's font."),
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
    ("size.display", "hero-title", "The hero display headline, 72px/1.2 Literatatt."),
    ("size.h1", "pricing-title", "Page and section headings, 60px Literatatt."),
    ("size.library", "library-h1", "The library's h1, 60px/800 Mulish."),
    ("size.price", "plan-price", "Plan prices, 56px Manrope."),
    ("size.mHero", "m-hero", "The hero headline at 390px, 56px Literatatt."),
    ("size.cta", "cta", "The hero CTA's label, 20px/600 Manrope."),
    ("size.menuLink", "m-menu-link", "Mobile menu links, 18px/600 Manrope."),
    ("size.nav", "nav-item", "Nav labels and buttons, 16px/600 Manrope."),
    ("size.footer", "footer-link", "Footer links, 16px/400 Manrope."),
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

(RAW / "component-tokens.json").write_text(json.dumps(SPEC, indent=1, ensure_ascii=False) + "\n")


def count(d):
    if not isinstance(d, dict):
        return 1
    if "var" in d or "value" in d:
        return 1
    return sum(count(v) for v in d.values())


print({k: count(v) for k, v in SPEC.items() if not k.startswith("_")})
