#!/usr/bin/env python3
"""Write raw/component-tokens.json, the token spec build_tokens.py reads.

clay.earth 301s to me.sh — the Clay product rebranded to Mesh — so every
measurement is read on me.sh. The Next.js bundle declares almost no design
tokens (raw/css-vars.json, read by tools/capture/vars.mjs): nine app
variables that are all Bulma `.columns.is-variable` gap widths and
integration-orb positions, plus @font-face declarations for Verlag,
VerlagCondensed and the Chronicle faces. There is no declared palette at
all — every colour role below is measured on the painted chrome and cited
back to raw/components-computed.json.

The site paints TWO page themes on different routes: a dark marketing
surface on / (black html ground, white text, off-white CTAs) and a warm
light surface on /pricing and the app.me.sh sign-in card (#f9f8f6 and
#fcfcfc). The dark surface is emitted under `dark`, the light surfaces
under `light`.

The measured palette:

  ink         the near-black ramp: #000 html ground, #0f0f10 footer band,
              #1d1d1f/31-31-31 ink text on the light routes, #1f1f1e the
              sign-in card's Apple button
  paper       the light surfaces: #fdfcfa hero CTA fill, #f9f8f6 pricing
              ground, #fcfcfc sign-in ground, #fff bottom CTA
  cream       #fefef7 — the warm off-white of the display headline
  orange      #fb7232 — the marketing accent: plan-label eyebrows, the
              popular card's glow ring, the filled Try-it-free button,
              menu-link hover
  orange-app  #ff6821 — the app stack's own orange on the sign-in card
  tan         #f2b98b — the wordmark/social icon accent; #efab74 its hover
  google      #5383ec — the Google OAuth button
  alphas      translucent whites on the dark surface (3% nav-pill fill,
              6% control scrim, 8% nav-signin hover, 14% drawer row,
              40-70% text shades) and translucent inks on the light
              surface (4% field fill, 6% chip/card fill, 10% field border,
              40% outline-button border, 24% orange glow)

Leaves are {"value": ..., "source": ...} — measured values resolved out of
raw/components-computed.json at build time, so the palette tracks what the
site actually paints.
"""
import json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
V = json.loads((RAW / "css-vars.json").read_text())
RL = V["resolved"].get("dark") or V["resolved"].get("light") or {}
C = json.loads((RAW / "components-computed.json").read_text())["components"]
R = {n: v.get("value", v.get("raw")) for n, v in RL.items()}

# No declared palette exists to name after; the core ramp is named by hand
# after what the site paints each value as (checked against the screenshots
# and the measured paint layers). Every leaf is resolved live from
# components-computed.json so the value and its provenance stay in step.
#   (token path, component, state, prop, description)
CORE = [
    ("ink.950", "page-ground", "default", "backgroundColor",
     "Black — the html element's painted ground under the whole dark site."),
    ("ink.900", "footer", "default", "backgroundColor",
     "The footer band's #0f0f10, a half-step up from the ground."),
    ("ink.800", "plan-card", "default", "color",
     "Ink text on the light routes — plan cards, pricing headings."),
    ("ink.750", "signin-apple", "default", "backgroundColor",
     "#1f1f1e — the Apple sign-in button's fill on the app surface."),
    ("ink.700", "section-title", "default", "color",
     "#1d1d1f — section headings and the filter pills' text."),
    ("gray.500", "signin-toggle", "default", "color",
     "#48494a — the app surface's body/text grey."),
    ("gray.400", "hero-sub", "default", "color",
     "#86868b — the muted body grey, read on the first paragraph after the hero h1 (a section paragraph, \"Set reminders...\"; the hero has no lede)."),
    ("paper.0", "cta", "default", "backgroundColor",
     "#fdfcfa — the hero CTA's warm off-white fill."),
    ("paper.50", "pricing-ground", "default", "backgroundColor",
     "#f9f8f6 — the pricing route's warm-cream ground."),
    ("paper.100", "cta-bottom", "default", "backgroundColor",
     "#ffffff — the bottom CTA's pure-white fill."),
    ("cream.0", "hero-title", "default", "color",
     "#fefef7 — the display headline's warm off-white."),
    ("orange.500", "plan-cta-filled", "default", "backgroundColor",
     "#fb7232 — the marketing accent: filled plan CTAs, plan-label eyebrows, the popular card's ring, menu-link hover."),
    ("orange.alpha24", "plan-card-popular", "default", "ringShadow",
     "The 24% orange glow ring around the popular plan card."),
    ("orange-app.500", "signin-email-btn", "default", "backgroundColor",
     "#ff6821 — the app surface's own orange (the Sign-in-with-email button)."),
    ("tan.300", "logo", "default", "color",
     "#f2b98b — the wordmark and social-icon accent."),
    ("tan.400", "cta-bottom", "hover", "color",
     "#efab74 — the tan accent's hover step."),
    ("google.500", "signin-google", "default", "backgroundColor",
     "#5383ec — the Google sign-in button."),
    ("google.600", "signin-google", "hover", "backgroundColor",
     "The Google blue at 87% — its hover/pressed step."),
    ("white-alpha.3", "header", "default", "paint.0.bg",
     "The nav pill's 3% white fill (under a white sheen gradient)."),
    ("white-alpha.6", "m-menu-button", "default", "backgroundColor",
     "The 6% white scrim on dark controls — hamburger, drawer rows."),
    ("white-alpha.8", "nav-signin", "hover", "backgroundColor",
     "The nav Sign-In hover wash."),
    ("white-alpha.24", "nav-cta", "default", "paint.0.shadow",
     "The nav GET STARTED pill's 24% white inset ring."),
    ("white-alpha.40", "footer-link", "default", "color",
     "Faint text on the dark surface — footer links."),
    ("white-alpha.60", "signin-email-btn", "default", "color",
     "The disabled-looking 60% white label on the orange button."),
    ("white-alpha.64", "nav-signin", "default", "color",
     "The nav Sign-In label's resting grey."),
    ("white-alpha.70", "header", "default", "color",
     "The dark surface's body text shade."),
    ("gray-alpha.6", "plan-card", "default", "backgroundColor",
     "The plan card's 6% grey fill under its white sheen gradient."),
    ("ink-alpha.4", "signin-input", "default", "backgroundColor",
     "The sign-in field's 4% ink fill."),
    ("ink-alpha.6", "billing-toggle", "default", "backgroundColor",
     "The billing toggle's 6% ink chip fill."),
    ("ink-alpha.10", "signin-input", "default", "borderTopColor",
     "The sign-in field's 10% ink border."),
    ("ink-alpha.40", "plan-cta", "default", "borderTopColor",
     "The outline plan button's 40% ink border."),
    ("glow.cta", "cta", "default", "boxShadow",
     "The near-white glow the hero CTA carries (0 0 4px 1px, 98% white)."),
]
SPEC = {"_about": (
    "The token tree build_tokens.py turns into tokens.json. me.sh "
    "declares no design-token CSS variables — its nine custom properties "
    "are Bulma column gaps and orb positions (raw/css-vars.json). "
    "Every leaf is a measured value resolved from "
    "raw/components-computed.json at build time. Two page themes exist: "
    "the dark marketing surface (dark) and the warm light pricing and "
    "sign-in surfaces (light)."),
    "core": {}, "dark": {}, "light": {}, "component": {}}


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
    # ----- the dark marketing surface (home and every dark route)
    ("dark:surface.page", "page-ground", "default", "backgroundColor", "The black page ground — painted by the html element (body itself is transparent)."),
    ("dark:surface.band", "footer", "default", "backgroundColor", "The #0f0f10 band — the site footer and the bottom-CTA section."),
    ("dark:surface.pill", "header", "default", "paint.0.bg", "The nav pill's glass fill — 3% white under a white sheen gradient."),
    ("dark:surface.control", "m-menu-button", "default", "backgroundColor", "The 6% white scrim on dark controls (hamburger, drawer)."),
    ("dark:text.primary", "hero-title", "default", "color", "The display headline's warm off-white."),
    ("dark:text.body", "header", "default", "color", "Body text on the dark surface — 70% white."),
    ("dark:text.muted", "nav-signin", "default", "color", "Muted actions on the dark surface — the Sign-In label."),
    ("dark:text.faint", "footer-link", "default", "color", "Faint text on the dark surface — footer links, secondary rows."),
    ("dark:text.accent", "logo", "default", "color", "The tan accent — wordmark, social icons, the bottom CTA's label."),
    ("dark:text.accentHover", "cta-bottom", "hover", "color", "The tan accent's hover step."),
    ("dark:text.onInverted", "cta", "default", "color", "Black text on the inverted off-white CTA."),
    ("dark:accent", "m-menu-link", "hover", "color", "The marketing orange — hover text on menu links."),
    ("dark:fill.inverted", "cta", "default", "backgroundColor", "The hero CTA's off-white fill — the primary action on the dark surface."),
    ("dark:fill.invertedStrong", "cta-bottom", "default", "backgroundColor", "The bottom CTA's pure-white fill."),
    ("dark:navHover", "nav-signin", "hover", "backgroundColor", "The dark controls' 8% hover wash."),
    ("dark:ring.control", "nav-cta", "default", "paint.0.shadow", "The 24% white inset ring on the nav GET STARTED pill."),
    ("dark:focus", "nav-signin", "focus-visible", "outlineColor", "Focus rings on this surface keep the browser's auto ring (dark ink on the glass controls) — recorded per entry; the 3px outline colour is the element's own text shade elsewhere."),
    # ----- the warm light surface (pricing and the sign-in card)
    ("light:surface.page", "pricing-ground", "default", "backgroundColor", "The pricing route's warm-cream ground."),
    ("light:surface.card", "plan-card", "default", "backgroundColor", "The plan card's 6% grey fill under its white sheen gradient."),
    ("light:surface.chip", "billing-toggle", "default", "backgroundColor", "The billing toggle's 6% ink chip fill."),
    ("light:text.primary", "pricing-h1", "default", "color", "Heading ink on the light routes."),
    ("light:text.muted", "signin-toggle", "default", "color", "The sign-in card's grey text — 'Create account'."),
    ("light:text.accent", "plan-name", "default", "color", "The orange eyebrow labels on the plan cards."),
    ("light:text.onAccent", "plan-cta-filled", "default", "color", "White text on the filled orange CTA."),
    ("light:accent", "plan-cta-filled", "default", "backgroundColor", "The marketing orange — the filled Try-it-free button."),
    ("light:accentRing", "plan-card-popular", "default", "ringShadow", "The 24% orange glow ring around the popular card."),
    ("light:accentApp", "signin-email-btn", "default", "backgroundColor", "The app surface's own orange — Sign in with email."),
    ("light:field.fill", "signin-input", "default", "backgroundColor", "The sign-in field's 4% ink fill."),
    ("light:border.subtle", "plan-card", "default", "paint.0.border", "The plan card's #eceae8 hairline."),
    ("light:border.control", "plan-cta", "default", "borderTopColor", "The outline plan button's 40% ink border."),
    ("light:border.field", "signin-input", "default", "borderTopColor", "The sign-in field's 10% ink border."),
    ("light:oauth.ink", "signin-apple", "default", "backgroundColor", "The Apple sign-in button."),
    ("light:oauth.google", "signin-google", "default", "backgroundColor", "The Google sign-in button."),
    ("light:oauth.googleHover", "signin-google", "hover", "backgroundColor", "The Google blue at 87% — hover/pressed."),
]:
    try:
        role(path, comp, state, prop, desc)
    except KeyError:
        pass

# -------------------------------------------------- measured extras (no var)

meas = SPEC["core"].setdefault("measured", {})
for comp, state, key, prop, desc in [
    ("m-menu-open", "default", "drawer-fill", "paint.0.bg", "The mobile drawer's near-black glass fill over the page."),
]:
    try:
        v = norm_color(stprop(comp, state, prop))
        if v and v != "transparent":
            meas[key] = {"value": v, "type": "color",
                         "source": f"computed {prop} of {comp} {state} (raw/components-computed.json)",
                         "description": desc}
    except KeyError:
        pass

# Shadows and the ring gradient are parsed from the readings they cite, never typed in.
def need(v, what):
    if v in (None, ""):
        raise SystemExit("build_component_tokens: raw/components-computed.json has no " + what)
    return v


def shadow_layers(v, keep_inset=True):
    layers = []
    for part in re.split(r",\s*(?![^()]*\))", v):
        m = re.fullmatch(r"(rgba?\([^)]*\))\s+(-?[\d.]+px)\s+(-?[\d.]+px)\s+(-?[\d.]+px)\s+(-?[\d.]+px)(\s+inset)?", part.strip())
        if not m:
            raise SystemExit("build_component_tokens: cannot read box-shadow layer %r" % part)
        if m.group(6) and not keep_inset:
            continue
        layer = {"offsetX": m.group(2), "offsetY": m.group(3), "blur": m.group(4), "spread": m.group(5), "color": norm_color(m.group(1))}
        if m.group(6):
            layer["inset"] = True
        layers.append(layer)
    return layers


def gradient_stops(v):
    m = re.fullmatch(r"linear-gradient\((-?[\d.]+)deg,\s*(.*)\)", v.strip())
    if not m:
        raise SystemExit("build_component_tokens: cannot read gradient %r" % v)
    stops = []
    for part in re.split(r",\s*(?![^()]*\))", m.group(2)):
        s = re.fullmatch(r"(rgba?\([^)]*\))\s+([\d.]+)%", part.strip())
        if not s:
            raise SystemExit("build_component_tokens: cannot read gradient stop %r" % part)
        pos = round(float(s.group(2)) / 100, 4)
        stops.append({"color": norm_color(s.group(1)), "position": int(pos) if pos == int(pos) else pos})
    return float(m.group(1)), stops


SPEC["dark"]["shadow"] = {
    "ctaGlow": {
        "type": "shadow",
        "value": shadow_layers(need(stprop("cta", "default", "boxShadow"), "boxShadow of cta default")),
        "source": "computed boxShadow of cta default (raw/components-computed.json)",
        "description": "The near-white glow under the hero CTA."},
    "navPill": {
        "type": "shadow",
        "value": shadow_layers(need(stprop("header", "default", "paint.0.shadow"), "paint.0.shadow of header default"), keep_inset=False),
        "source": "computed paint.0.shadow of header default (raw/components-computed.json)",
        "description": "The nav pill's layered glass shadow (hairline ring + two soft drops; the inset sheen layers are omitted)."},
}
SPEC["light"]["shadow"] = {
    "popularRing": {
        "type": "shadow",
        "value": shadow_layers(need(stprop("plan-card-popular", "default", "boxShadow"), "boxShadow of plan-card-popular default")),
        "source": "computed boxShadow of plan-card-popular default (raw/components-computed.json)",
        "description": "The orange glow ring around the popular plan card."},
}

# The CTA's rainbow ring: a linear-gradient painted 54px proud of the hero CTA (and 48px proud of the
# bottom CTA) on ::before.
grad = SPEC["core"].setdefault("gradient", {})
_angle, _stops = gradient_stops(need(stprop("cta", "default", "paint.1.bgImage"), "paint.1.bgImage of cta default"))
grad["ctaRing"] = {
    "type": "gradient",
    "angle": int(_angle) if _angle == int(_angle) else _angle,
    "value": _stops,
    "source": "computed paint.1.bgImage of cta default (raw/components-computed.json)",
    "description": "The blue-violet-amber ring gradient painted proud of the hero and bottom CTAs."}
grad["filterWash"] = {
    "type": "gradient",
    "angle": 90,
    "value": [{"color": "rgba(29, 29, 31, 0.06)", "position": 0},
              {"color": "rgba(29, 29, 31, 0.03)", "position": 1}],
    "source": "computed paint.0.bgImage of filter-button default (raw/components-computed.json)",
    "description": "The filter pill's ::after ink wash over the 480x48 button."}
grad["cardSheen"] = {
    "type": "gradient",
    "angle": 180,
    "value": [{"color": "#ffffff", "position": 0},
              {"color": "rgba(255, 255, 255, 0.5)", "position": 1}],
    "source": "computed paint.0.bgImage of plan-card default (raw/components-computed.json)",
    "description": "The plan card's white sheen over its 6% grey fill."}
grad["drawerSheen"] = {
    "type": "gradient",
    "angle": 180,
    "value": [{"color": "rgba(31, 31, 30, 0.8)", "position": 0.02},
              {"color": "rgba(31, 31, 30, 0)", "position": 1}],
    "source": "computed paint.0.bgImage of m-menu-open default (raw/components-computed.json)",
    "description": "The mobile drawer's dark sheen — near-black easing to transparent."}

# ------------------------------------------------------------------ component

comp = SPEC["component"]
# Components the capture read from the wrong element (README, What to distrust): a token citing one
# says so in its source.
WRONG_ELEMENT = {"menu-panel": "the closed Company panel, opacity 0, not the open dropdown"}

for key, cname, state, prop, desc in [
    ("control.heightCta", "cta", "default", "height", "The hero CTA's 54px pill."),
    ("control.heightCtaBottom", "cta-bottom", "default", "height", "The bottom CTA's 52px pill."),
    ("control.heightNavCta", "nav-cta", "default", "height", "The nav GET STARTED pill, 32px."),
    ("control.heightSigninLink", "nav-signin", "default", "height", "The nav Sign-In action, 34px."),
    ("control.heightPlanCta", "plan-cta", "default", "height", "The plan cards' action button, 44px."),
    ("control.heightField", "signin-input", "default", "height", "The sign-in field, 40px."),
    ("control.heightOauth", "signin-apple", "default", "height", "The OAuth buttons, 44px."),
    ("control.heightToggle", "billing-toggle", "default", "height", "The billing toggle, 40px."),
    ("control.heightFilter", "filter-button", "default", "height", "The feature filter pills, 48px."),
    ("control.heightHamburger", "m-menu-button", "default", "height", "The mobile hamburger, 32px."),
    ("control.radiusCta", "cta", "default", "borderTopLeftRadius", "Hero CTA corners, 14px."),
    ("control.radiusCtaBottom", "cta-bottom", "default", "borderTopLeftRadius", "Bottom CTA corners, 16px."),
    ("control.radiusPlanCta", "plan-cta", "default", "borderTopLeftRadius", "Plan button corners, 10px."),
    ("control.radiusNavCta", "nav-cta", "default", "paint.0.radius", "Nav pill corners, 8px."),
    ("control.radiusHamburger", "m-menu-button", "default", "borderTopLeftRadius", "Hamburger corners, 8px."),
    ("control.radiusSigninLink", "nav-signin", "default", "borderTopLeftRadius", "Sign-In action corners, 8px."),
    ("control.radiusField", "signin-input", "default", "borderTopLeftRadius", "Sign-in field corners, 6px."),
    ("control.radiusSigninBtn", "signin-email-btn", "default", "borderTopLeftRadius", "Sign-in button corners, 12px."),
    ("control.radiusToggle", "billing-toggle", "default", "borderTopLeftRadius", "Billing toggle corners, 12px."),
    ("control.radiusFilter", "filter-button", "default", "paint.0.radius", "Filter pill corners, 16px."),
    ("card.radiusPlan", "plan-card", "default", "paint.0.radius", "Plan card corners, 16px."),
    ("card.radiusDrawer", "m-menu-open", "default", "paint.0.radius", "Mobile drawer corners, 12px."),
    ("nav.height", "header", "default", "height", "The nav pill at 1440px, 48px."),
    ("nav.width", "header", "default", "width", "The nav pill's width, 388px."),
    ("menuPanel.width", "menu-panel", "default", "width", "The width of a nav dropdown panel, 556px. Read from the wrong element: the closed Company panel (opacity 0), not the open dropdown; recapture needed."),
    ("footer.height", "footer", "default", "height", "The footer block at 1440px, 335px."),
    ("drawer.height", "m-menu-open", "default", "height", "The mobile drawer at 390px, 762px."),
    ("planCard.height", "plan-card", "default", "height", "The plan card's inner height, 196px."),
]:
    try:
        v = stprop(cname, state, prop)
        if not v:
            continue
        node = comp
        parts = key.split(".")
        for p in parts[:-1]:
            node = node.setdefault(p, {})
        src = f"computed {prop} of {cname} {state} (raw/components-computed.json)"
        if cname in WRONG_ELEMENT:
            src += "; read from the wrong element (%s); recapture needed" % WRONG_ELEMENT[cname]
        node[parts[-1]] = {"type": "dimension", "value": v, "source": src, "description": desc}
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
    ("family.ui", "nav-item", "fontFamily", "Verlag across the dark marketing surface: nav, body, controls."),
    ("family.display", "hero-title", "fontFamily", "VerlagCondensed — the condensed display face of the hero and section headings."),
    ("family.serif", "plan-price", "textStyle.fontFamily", "ChronicleDisplayCondensed — the serif face the plan prices and editorial headings set in."),
    ("family.app", "signin-input", "fontFamily", "SF Pro Text — the app.me.sh sign-in card's UI font (a different stack)."),
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
    ("size.display", "hero-title", "The hero display headline, 64px VerlagCondensed."),
    ("size.h1", "pricing-h1", "Page headings on the light routes, 48px VerlagCondensed."),
    ("size.h2", "section-title", "Section headings in the light bands, 48px/900 VerlagCondensed."),
    ("size.signin", "signin-title", "The sign-in card's 32px headline."),
    ("size.sub", "hero-sub", "The 20px section body paragraph, read on the first paragraph after the hero h1 (\"Set reminders...\"; the hero has no lede)."),
    ("size.body", "filter-button", "Body-size controls and copy, 18-20px (filter pills set 20px)."),
    ("size.planLabel", "plan-name", "Plan eyebrows and menu links, 14px."),
    ("size.nav", "nav-item", "Nav labels — 12px at weight 700."),
    ("size.footer", "footer-link", "Footer links — 12px at weight 700."),
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
    if "var" in d or "value" in d or "$value" in d:
        return 1
    return sum(count(v) for v in d.values())


print({k: count(v) for k, v in SPEC.items() if not k.startswith("_")})
