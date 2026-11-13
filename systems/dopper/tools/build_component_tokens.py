#!/usr/bin/env python3
"""Write raw/component-tokens.json, the token spec build_tokens.py reads.

dopper.com's public surface is two hosts, one brand system:

  www.dopper.com   Next.js/Storyblok — declares a real named :root custom-
                  property layer (raw/css-vars.json resolved.light: the
                  --darkBlue/--deep-sea/--sand/--yellow/--carribean/
                  --glowing-coral ramps, --border-radius-*, --ease-*/--bounce-*
                  easings, --z-* and --touch-target-min). Those become
                  {"var": ...} leaves resolved by build_tokens.py.
  shop.dopper.com  Magento 2 (theme Dopper/dopper_b2c) — the same palette
                  compiled to literals; its values are measured computed
                  styles, not declared names.

Everything the :root layer does not declare is **measured** off
raw/components-computed.json (tools/capture/public/measure.mjs): the
deep-sea text colour, the pill CTAs, the darkBlue-3 filter/cart bands, the
yellow mega-menu, the field surfaces and the state colours.

A leaf is {"var": ...} or {"value": ..., "source": ...}. Light-only: no dark
theme mechanism exists on either host (vars.mjs records theme:"light"), so
there is no "dark" set — the darkBlue and deep-sea surfaces are brand-painted
bands of the light page, not a theme.
"""
import json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
V = json.loads((RAW / "css-vars.json").read_text())
RL = V.get("resolved", {}).get("light", {})
C = json.loads((RAW / "components-computed.json").read_text())["components"]
R = {n: v.get("value", v.get("raw")) for n, v in RL.items()}


def var(name, ty="color", **kw):
    d = {"var": name, "type": ty}
    d.update(kw)
    return d


SPEC = {"_about": (
    "The token tree build_tokens.py turns into tokens.json. dopper.com "
    "declares its palette, radii, easings, z scale and touch-target floor as "
    "named :root custom properties (raw/css-vars.json resolved.light); the "
    "shop compiles the same values to literals, so component surfaces are "
    "var-referenced where a name exists and measured computed values "
    "(raw/components-computed.json) elsewhere. Light-only: the darkBlue and "
    "deep-sea surfaces are brand bands of the light page, not a theme."),
    "core": {}, "light": {}, "dark": {}, "component": {}}


def descend(root, parts):
    node = root
    for p in parts[:-1]:
        child = node.setdefault(p, {})
        if "var" in child or "value" in child or "$value" in child:
            node[p] = {"default": child}
            child = node[p]
        node = child
    last = parts[-1]
    cur = node.get(last)
    if isinstance(cur, dict) and cur and not ("var" in cur or "value" in cur or "$value" in cur):
        node = cur
        node.setdefault("default", None)
        last = "default"
    return node, last


def emit(root, name, leaf):
    node, last = descend(root, name[2:].split("-"))
    node[last] = leaf


def st(comp, state):
    return C[comp]["states"][state]["style"]


def ts(comp, state, prop):
    """The first text node's reading (textStyle) when the kit recorded one —
    the wrapper's own fontSize can be the container's, not the text's."""
    try:
        c = C[comp]["states"][state]
        t = c.get("textStyle") or {}
        v = t.get(prop)
        return v if v else c["style"].get(prop)
    except KeyError:
        return None


def norm_color(v):
    v = (v or "").strip()
    m = re.fullmatch(r"#([0-9a-fA-F]{3,8})", v)
    if m:
        h = m.group(1).lower()
        if len(h) in (3, 4):
            h = "".join(c * 2 for c in h)
        return "#" + h[:6]
    m = re.fullmatch(r"rgba?\(([\d.]+),\s*([\d.]+),\s*([\d.]+)(?:,\s*([\d.]+))?\)", v)
    if m:
        r, g, b, a = m.groups()
        if a is None or float(a) >= 1:
            return "#%02x%02x%02x" % (int(float(r)), int(float(g)), int(float(b)))
        return f"rgba({int(float(r))}, {int(float(g))}, {int(float(b))}, {'%g' % float(a)})"
    return v


def have(comp, state, prop=None):
    try:
        s = st(comp, state)
        return prop is None or bool((s.get(prop) or "").strip())
    except KeyError:
        return False


def find_var(value, contains=None):
    """First resolved light var whose value matches."""
    for n, v in R.items():
        if v == value and (contains is None or contains in n):
            return n
    return None


# ------------------------------------------------------------------- fonts

fam = SPEC["core"].setdefault("font", {}).setdefault("family", {})
if have("hero-display", "default", "fontFamily"):
    fam["display"] = {"value": st("hero-display", "default")["fontFamily"], "type": "fontFamily",
                      "source": "computed fontFamily of hero-display default (raw/components-computed.json); the Dopper-Regular webfont is served from www.dopper.com (raw/css-vars.json fonts)",
                      "description": "The Dopper display family used for h1s, the logo area and big menu rows."}
if have("nav-link", "default", "fontFamily"):
    fam["sans"] = {"value": st("nav-link", "default")["fontFamily"], "type": "fontFamily",
                   "source": "computed fontFamily of nav-link default (raw/components-computed.json); Gilroy-Medium/Gilroy-Bold webfonts from www.dopper.com (raw/css-vars.json fonts)",
                   "description": "The Gilroy stack on nav links, buttons and body text."}
weights = SPEC["core"].setdefault("font", {}).setdefault("weight", {})
for key, comp, state, desc in [
    ("regular", "nav-link", "default", "The 400/medium reading on nav and body copy (Gilroy-Medium is styled as 400)."),
    ("bold", "collections-heading", "default", "The heavy reading on section headings and buttons (Gilroy-Bold, styled 600-700)."),
    ("display", "hero-display", "default", "The Dopper display weight on h1s."),
]:
    v = ts(comp, state, "fontWeight")
    if v:
        weights[key] = {"value": int(v), "type": "fontWeight",
                        "source": f"computed fontWeight of {comp} {state} (raw/components-computed.json)",
                        "description": desc}

# ------------------------------------------------------- declared colours

# Every named palette var resolves to a token under color.<ramp>.<step>.
color = SPEC["core"].setdefault("color", {})
for ramp in ("darkBlue", "deep-sea", "sand", "yellow", "carribean", "glowing-coral"):
    bag = color.setdefault(ramp.replace("-", "_"), {})
    for n, v in sorted(R.items()):
        if not n.startswith("--" + ramp):
            continue
        step = n[len(ramp) + 2:] or "base"
        step = "base" if step == "" else step
        bag["default" if step == "base" else step] = var(n, "color",
            source=f"css-var {n} resolved light (raw/css-vars.json)",
            description=f"The declared {n} swatch ({v}).")
neutral = color.setdefault("neutral", {})
if "--black" in R:
    neutral["ink"] = var("--black", "color", source="css-var --black resolved light (raw/css-vars.json)", description="The declared #000 black.")
if "--white" in R:
    neutral["paper"] = var("--white", "color", source="css-var --white resolved light (raw/css-vars.json)", description="The declared #fcfaf2 off-white — the site's page field (sand-3 shares the value).")
if "--deep-sea-overlay" in R:
    neutral["scrim"] = var("--deep-sea-overlay", "color", source="css-var --deep-sea-overlay resolved light (raw/css-vars.json)", description="The declared 80% deep-sea overlay.")
if "--darkTeal" in R:
    status = color.setdefault("status", {})
    status["teal"] = var("--darkTeal", "color", source="css-var --darkTeal resolved light (raw/css-vars.json)", description="The declared dark teal.")

# Measured role colours that the :root layer does not cover.
if have("hero-display", "default"):
    v = norm_color(st("hero-display", "default").get("color"))
    if v:
        neutral["display-ink"] = {"value": v, "type": "color",
            "source": "computed color of hero-display default (raw/components-computed.json)",
            "description": "The sand (#f6ecc8-family) display ink on media heroes."}
if have("nav-link", "default"):
    v = norm_color(st("nav-link", "default").get("color"))
    if v:
        neutral["text"] = {"value": v, "type": "color",
            "source": "computed color of nav-link default (raw/components-computed.json)",
            "description": "The link/body ink (deep-sea on the marketing chrome)."}

# -------------------------------------------------------------------- roles

light = SPEC["light"]
ALIAS = "role alias over the measured palette"


def role(name, target, desc, source=None):
    if target.startswith("{"):
        emit(light, name, {"value": target, "type": "color",
                           "source": source or ALIAS, "description": desc})
    else:
        vn = find_var(target)
        if vn:
            emit(light, name, var(vn, "color",
                                  source=(source + "; " if source else "") + f"css-var {vn} resolved light (raw/css-vars.json)",
                                  description=desc))
        else:
            emit(light, name, {"value": target, "type": "color",
                               "source": source or "measured value (raw/components-computed.json)",
                               "description": desc})


role("--surface-page", "#fcfaf2", "The #fcfaf2 cream page field (sand-3/--white).", "computed body/page background on both hosts")
role("--surface-card", "#f9f3df", "The sand-2 card field.", "computed card surfaces (raw/components-computed.json)")
role("--surface-band", "#cce2ff", "The darkBlue-3 light-blue band: the PLP filter sheet, the cart strip, the New Customers card.", "computed filter-panel/new-card/cart-strip background (raw/components-computed.json)")
role("--surface-menu", "#fed200", "The yellow mega-menu panel.", "computed flyout background (raw/components-computed.json)")
role("--surface-menu-mobile", "#0067e5", "The darkBlue full-screen mobile menu.", "computed m-menu-open background (raw/components-computed.json)")
role("--surface-deep", "#000f2e", "The deep-sea surface (filled pills, the × close button).", "computed btn-dark fill (raw/components-computed.json)")
role("--text-primary", "#000f2e", "The deep-sea ink on headings and primary copy.", "computed color of plp-h1 / headings (raw/components-computed.json)")
role("--text-muted", "#515a8a", "The deep-sea-1 secondary text (item counts, meta).", "computed muted text inside filter rows (raw/components-computed.json)")
role("--text-on-dark", "#fcfaf2", "Cream text on darkBlue/deep-sea surfaces.", "computed color of m-menu rows / btn-dark label (raw/components-computed.json)")
role("--action-primary", "#0067e5", "The darkBlue fill on Add to cart / Sign in / shop CTAs.", "computed backgroundColor of add-to-cart / shop-hero-button (raw/components-computed.json)")
role("--action-dark", "#000f2e", "The deep-sea fill on 'Watch now', Sign in, × close.", "computed backgroundColor of btn-dark / filter-close (raw/components-computed.json)")
role("--action-accent", "#0abeaa", "The carribean '+ Filters' pill.", "computed backgroundColor of filters-button (raw/components-computed.json)")
role("--action-warm", "#fed200", "The yellow active tab / burger fill.", "computed flyout-tab active state and m-burger fill (raw/components-computed.json)")
role("--border-ink", "#000f2e", "The deep-sea outline on ghost pills and filter rings.", "computed borders of btn-outline / filter rows (raw/components-computed.json)")
role("--focus-ring", "#0067e5", "Keyboard focus ring colour where the page paints one.", "computed outlineColor of focus-visible states (raw/components-computed.json)")

# ------------------------------------------------------------- type scale

type_scale = SPEC["core"].setdefault("font", {}).setdefault("size", {})
for key, comp, state, desc in [
    ("display", "plp-h1", "default", "The page/PLP display size (~80px Dopper)."),
    ("display-hero", "hero-display", "default", "The hero display size."),
    ("display-mobile", "m-hero", "default", "The display size at 390 wide."),
    ("h2", "collections-heading", "default", "The section heading size."),
    ("menu-item", "m-nav-item", "default", "The ~40px mobile-menu rows."),
    ("card-title", "content-card", "default", "Card/section copy heading size."),
    ("body", "nav-link", "default", "The 20.8px nav/body size."),
    ("control", "btn-dark", "default", "Button label size."),
    ("price", "pdp-price", "default", "The PDP/card price size."),
    ("meta", "product-price", "default", "PLP card price/meta size."),
    ("label", "login-label", "default", "Form label size."),
]:
    v = ts(comp, state, "fontSize")
    if v:
        type_scale[key] = {"type": "dimension", "value": v,
                           "source": f"computed fontSize of {comp} {state} (raw/components-computed.json)",
                           "description": desc}

leading = SPEC["core"].setdefault("font", {}).setdefault("lineHeight", {})
for key, comp, state, desc in [
    ("display", "plp-h1", "default", "Display leading."),
    ("display-hero", "hero-display", "default", "Hero display leading."),
    ("h2", "collections-heading", "default", "Heading leading."),
    ("body", "nav-link", "default", "Body/link leading."),
    ("control", "btn-dark", "default", "Button label leading."),
]:
    v = ts(comp, state, "lineHeight")
    if v:
        leading[key] = {"type": "dimension", "value": v,
                        "source": f"computed lineHeight of {comp} {state} (raw/components-computed.json)",
                        "description": desc}

# ---------------------------------------------------------- radius, motion

radius = SPEC["core"].setdefault("radius", {})
for n in sorted(R):
    if n.startswith("--border-radius-"):
        key = n.replace("--border-radius-", "")
        radius[key] = var(n, "dimension",
                          source=f"css-var {n} resolved light (raw/css-vars.json)",
                          description=f"The declared {n}.")
if have("filters-button", "default", "borderTopLeftRadius"):
    radius["pill"] = {"value": st("filters-button", "default")["borderTopLeftRadius"], "type": "dimension",
                      "source": "computed borderTopLeftRadius of filters-button default (raw/components-computed.json)",
                      "description": "The pill radius on + Filters / CTA pills (measured; bigger than radius-l)."}
if have("filter-close", "default", "borderTopLeftRadius"):
    radius["circle"] = {"value": st("filter-close", "default")["borderTopLeftRadius"], "type": "dimension",
                        "source": "computed borderTopLeftRadius of filter-close default (raw/components-computed.json)",
                        "description": "The 50% circle on the × close and icon buttons."}
if have("login-card", "default", "borderTopLeftRadius"):
    radius["card"] = {"value": st("login-card", "default")["borderTopLeftRadius"], "type": "dimension",
                      "source": "computed borderTopLeftRadius of login-card default (raw/components-computed.json)",
                      "description": "The card radius on the login/panel cards."}
if have("login-email", "default", "borderTopLeftRadius"):
    radius["field"] = {"value": st("login-email", "default")["borderTopLeftRadius"], "type": "dimension",
                       "source": "computed borderTopLeftRadius of login-email default (raw/components-computed.json)",
                       "description": "The field radius on the white inputs."}

motion = SPEC["core"].setdefault("motion", {})
ease = motion.setdefault("easing", {})
for n in sorted(R):
    if n.startswith("--ease-") or n.startswith("--bounce-"):
        key = n[2:].replace("--", "-")
        ease[key] = var(n, "cubicBezier",
                        source=f"css-var {n} resolved light (raw/css-vars.json)",
                        description=f"The declared {n} easing.")
for key, comp, state, prop, ty, desc in [
    ("control-duration", "btn-dark", "default", "transitionDuration", "duration", "The control transition duration (hover fill)."),
    ("menu-duration", "nav-trigger", "default", "transitionDuration", "duration", "Nav/flyout transition duration."),
]:
    try:
        d = st(comp, state)[prop].split(",")[0].strip()
        if d and d != "0s":
            motion.setdefault("duration", {})[key] = {"value": d, "type": ty,
                "source": f"computed transition of {comp} {state} (raw/components-computed.json)",
                "description": desc}
    except (KeyError, TypeError):
        pass

layout = SPEC["core"].setdefault("layout", {})
if "--touch-target-min" in R:
    layout["touch-target-min"] = var("--touch-target-min", "dimension",
                                     source="css-var --touch-target-min resolved light (raw/css-vars.json)",
                                     description="The declared 44px minimum touch target.")
zidx = layout.setdefault("z-index", {})
for n in sorted(R):
    if n.startswith("--z-"):
        zidx[n[4:]] = {"value": R[n], "type": "number",
                       "source": f"css-var {n} resolved light (raw/css-vars.json)",
                       "description": f"The declared {n}."}

meas = SPEC["core"].setdefault("measured", {})
for key, comp, state, prop, ty, desc in [
    ("focus-ring", "nav-link", "focus-visible", "outlineColor", "color", "The keyboard focus ring colour on the header links."),
    ("focus-ring-shop", "shop-nav-link", "focus-visible", "outlineColor", "color", "The focus ring on the shop nav."),
    ("header-shadow", "header", "default", "boxShadow", "shadow", "Any elevation the header bar paints."),
]:
    try:
        s = st(comp, state)
        if prop == "boxShadow":
            layers = re.findall(r"(rgba?\([\d.,\s]+\))\s+(-?\d+(?:\.\d+)?px)\s+(-?\d+(?:\.\d+)?px)\s+(-?\d+(?:\.\d+)?px)\s+(-?\d+(?:\.\d+)?px)( inset)?", s.get(prop) or "")
            layers = [l for l in layers if l[0] != "rgba(0, 0, 0, 0)"]
            if layers:
                meas[key] = {"value": [{"color": norm_color(a), "offsetX": x, "offsetY": y, "blur": bl, "spread": sp, "inset": bool(i)} for a, x, y, bl, sp, i in layers],
                             "type": ty,
                             "source": f"computed {prop} of {comp} {state} (raw/components-computed.json)",
                             "description": desc}
            continue
        if have(comp, state, prop):
            meas[key] = {"value": norm_color(s[prop]), "type": ty,
                         "source": f"computed {prop} of {comp} {state} (raw/components-computed.json)",
                         "description": desc}
    except KeyError:
        pass

# ------------------------------------------------------------------ component

comp = SPEC["component"]
for key, cname, state, prop, desc in [
    ("button-dark-fill", "btn-dark", "default", "backgroundColor", "Deep-sea fill of the dark pill CTAs."),
    ("button-dark-fill-hover", "btn-dark", "hover", "backgroundColor", "Hover step of the dark pill."),
    ("button-dark-fill-pressed", "btn-dark", "pressed", "backgroundColor", "Pressed step of the dark pill."),
    ("button-dark-ink", "btn-dark", "default", "color", "Cream label on the dark pill."),
    ("button-primary-fill", "add-to-cart", "default", "backgroundColor", "darkBlue fill of Add to cart / Sign in / Create an Account."),
    ("button-primary-fill-hover", "add-to-cart", "hover", "backgroundColor", "Hover step of the blue CTA."),
    ("button-primary-ink", "add-to-cart", "default", "color", "Cream label on the blue CTA."),
    ("button-outline-border", "btn-outline", "default", "borderTopColor", "The deep-sea outline ring on ghost pills."),
    ("button-outline-ink", "btn-outline", "default", "color", "Ink on the ghost pill."),
    ("button-teal-fill", "filters-button", "default", "backgroundColor", "The carribean filter pill fill."),
    ("nav-trigger-fill-hover", "nav-trigger", "hover", "backgroundColor", "Hover fill the nav triggers take."),
    ("link-color", "nav-link", "default", "color", "Header link ink."),
    ("link-color-hover", "nav-link", "hover", "color", "Header link hover ink."),
    ("header-bg", "header", "default", "backgroundColor", "The header bar background (transparent over media)."),
    ("menu-bg", "m-menu-open", "default", "backgroundColor", "The darkBlue mobile menu fill."),
    ("flyout-bg", "flyout", "default", "backgroundColor", "The yellow mega-menu panel field."),
    ("filter-panel-bg", "filter-panel", "default", "backgroundColor", "The darkBlue-3 filter sheet fill."),
    ("filter-close-fill", "filter-close", "default", "backgroundColor", "The deep-sea × close circle."),
    ("badge-chip-border", "product-badge", "default", "borderTopColor", "The outlined 'New' chip ring."),
    ("badge-chip-ink", "product-badge", "default", "color", "The 'New' chip ink."),
    ("card-bg", "content-card", "default", "backgroundColor", "Content card field."),
    ("login-card-bg", "login-card", "default", "backgroundColor", "The darkBlue 'Registered Customers' card."),
    ("new-card-bg", "new-card", "default", "backgroundColor", "The darkBlue-3 'New Customers' card."),
    ("field-bg", "login-email", "default", "backgroundColor", "The white input fill on the blue card."),
    ("field-ink", "login-email", "default", "color", "Input text ink."),
    ("field-placeholder", "login-email", "default", "placeholder", "Placeholder ink."),
    ("signin-fill", "login-button", "default", "backgroundColor", "The deep-sea Sign in pill on the blue card."),
    ("checkbox-ink", "login-checkbox", "default", "color", "Checkbox row ink on the blue card."),
    ("footer-bg", "footer", "default", "backgroundColor", "The sand footer field."),
    ("price-ink", "product-price", "default", "color", "PLP price ink."),
    ("cart-strip-bg", "cart-strip", "default", "backgroundColor", "The darkBlue-3 cart strip."),
]:
    try:
        c = C[cname]["states"][state]
        if prop == "placeholder":
            v = (c.get("placeholder") or {}).get("color")
        else:
            v = c["style"].get(prop)
        if v:
            comp[key] = {"value": norm_color(v), "type": "color",
                         "source": f"computed {prop} of {cname} {state} (raw/components-computed.json)",
                         "description": desc}
    except KeyError:
        pass

for key, cname, state, prop, desc in [
    ("button-height", "add-to-cart", "default", "height", "The 54px pill CTA height."),
    ("button-padding-x", "add-to-cart", "default", "paddingLeft", "Pill horizontal padding."),
    ("button-radius", "add-to-cart", "default", "borderTopLeftRadius", "The pill radius on the blue CTA."),
    ("field-height", "login-email", "default", "height", "The 54px field height."),
    ("nav-height", "header", "default", "height", "The ~110px marketing header (content row is slimmer)."),
]:
    try:
        v = C[cname]["states"][state]["style"].get(prop)
        if v:
            comp[key] = {"value": v, "type": "dimension",
                         "source": f"computed {prop} of {cname} {state} (raw/components-computed.json)",
                         "description": desc}
    except KeyError:
        pass

(RAW / "component-tokens.json").write_text(json.dumps(SPEC, indent=1) + "\n")
n = 0
def walk(d):
    global n
    for v in d.values():
        if isinstance(v, dict):
            if "value" in v or "var" in v:
                n += 1
            else:
                walk(v)
walk(SPEC)
print("component-tokens.json:", n, "leaves")
