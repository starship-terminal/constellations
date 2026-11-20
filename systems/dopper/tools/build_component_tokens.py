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


# Three focus-visible states (nav-link, m-burger, m-menu-pill) were recorded `via: focus failed`;
# their via was later rewritten by hand to this sentence, not re-measured. They are treated as
# failed focus: never a token source.
HAND_RELABELLED_FOCUS = "el.focus() — a real ring painted; document.activeElement read the shadow host (check fixed in kbFocus)"


def not_captured(v):
    return (bool(v.get("skipped")) or v.get("via") in ("focus failed", HAND_RELABELLED_FOCUS)
            or (v.get("focus") or {}).get("matches") is False)


def st(comp, state):
    v = C[comp]["states"][state]
    if not_captured(v):
        raise KeyError(f"{comp} {state}: keyboard focus never confirmed (via {v.get('via')!r}); not a reading")
    return v["style"]


def colour_at(comp, state, where):
    """The colour one reading holds: a style property, `text.color` (first text node),
    `::before.<prop>`, or `paint:<node fragment>.<bg|border|outline>` (a painted layer)."""
    if C[comp].get("missing"):
        raise KeyError(f"{comp}: flagged missing (misidentified); not a reading")
    v = C[comp]["states"][state]
    style = st(comp, state)
    if where == "text.color":
        raw = (v.get("textStyle") or {}).get("color")
    elif where.startswith("::before."):
        raw = (v.get("::before") or {}).get(where.split(".", 1)[1])
    elif where.startswith("paint:"):
        frag, field = where[6:].rsplit(".", 1)
        # a painted layer only counts when it has a size: a 0 x 0 node paints nothing visible
        layer = next((n for n in v.get("paint") or [] if frag in (n.get("node") or "")
                      and not re.match(r"0(\.0+)?(px)?x", n.get("size") or "0x")), None)
        raw = (layer or {}).get(field)
        if raw and field in ("border", "outline"):
            raw = re.search(r"rgba?\([^)]*\)", raw).group(0)
    else:
        raw = style.get(where)
    if not raw:
        raise KeyError(f"{comp} {state}: no {where} reading")
    return norm_color(raw)


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
# Each named weight comes from a reading whose family matches the name:
# Gilroy 400 body text, Gilroy-Medium 500 nav, Gilroy-Bold 600 CTA labels,
# Dopper 400 display. (The section headings are Dopper at 400, not a bold.)
for key, comp, state, desc in [
    ("regular", "breadcrumb", "default", "The 400 reading on body copy and secondary text (Gilroy)."),
    ("medium", "nav-link", "default", "The 500 reading on header links and card titles (Gilroy-Medium)."),
    ("bold", "add-to-cart", "default", "The 600 reading on CTA labels, prices and shop headings (Gilroy-Bold)."),
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


def role(name, target, desc, source=None, readings=()):
    """A role colour. `readings` are the (component, state, where) readings that paint it; each
    must hold the target or the build stops, and they become the source. A role with no reading
    carries its declared variable alone."""
    for comp_, state_, where_ in readings:
        got = colour_at(comp_, state_, where_)
        if got != target:
            raise ValueError(f"{name}: {comp_} {state_} {where_} reads {got}, not {target}")
    if readings:
        source = "computed " + "; ".join(f"{w} of {c} {s_}" for c, s_, w in readings) + " (raw/components-computed.json)"
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


role("--surface-page", "#fcfaf2", "The #fcfaf2 cream page field (sand-3/--white).",
     readings=[("shop-header", "default", "backgroundColor"), ("newsletter-input", "default", "backgroundColor")])
# The only #f9f3df readings are the footer's social chips, which read 0 x 0: declared --sand-2 alone.
role("--surface-card", "#f9f3df", "The sand-2 card field (declared; no captured visible surface paints it).")
role("--surface-band", "#cce2ff", "The darkBlue-3 light-blue band: the PLP filter sheet, the cart strip, the New Customers card.",
     readings=[("new-card", "default", "backgroundColor"), ("cart-strip", "default", "backgroundColor")])
# The opened Bottle mega-menu was screenshotted, not measured (the stored flyout reading is a
# misidentified static section): the role carries the declared --yellow alone.
role("--surface-menu", "#fed200", "The yellow mega-menu panel (declared --yellow; the opened panel was not measured).")
role("--surface-menu-mobile", "#0067e5", "The darkBlue full-screen mobile menu.",
     readings=[("m-menu-open", "default", "paint:dialog__background.bg")])
role("--surface-deep", "#000f2e", "The deep-sea surface (filled pills, the × close button).",
     readings=[("btn-dark", "default", "paint:burstButton_fakeButton.bg")])
role("--text-primary", "#000f2e", "The deep-sea ink on headings and primary copy.",
     readings=[("plp-h1", "default", "color")])
# No reading holds #515a8a: the role carries the declared --deep-sea-1 alone.
role("--text-muted", "#515a8a", "The deep-sea-1 secondary text (declared; no captured component paints it).")
role("--text-on-dark", "#fcfaf2", "Cream text on darkBlue/deep-sea surfaces.",
     readings=[("m-nav-item", "default", "color"), ("m-menu-open", "default", "text.color")])
role("--action-primary", "#0067e5", "The darkBlue fill on Add to cart / Sign in / shop CTAs.",
     readings=[("add-to-cart", "default", "backgroundColor"), ("shop-hero-button", "default", "::before.backgroundColor")])
role("--action-dark", "#000f2e", "The deep-sea fill on 'Watch now', Sign in, × close.",
     readings=[("btn-dark", "default", "paint:burstButton_fakeButton.bg"), ("login-button", "default", "::before.backgroundColor")])
role("--action-accent", "#0abeaa", "The carribean '+ Filters' pill.",
     readings=[("filters-button", "default", "::before.backgroundColor")])
# The flyout-tab reading is misidentified and m-burger paints no yellow: declared --yellow alone.
role("--action-warm", "#fed200", "The yellow active tab / burger fill (declared --yellow; no captured reading paints it).")
role("--border-ink", "#000f2e", "The deep-sea rings on the Sign in pill and the option radios (the ghost pill measured on media paints cream).",
     readings=[("login-button", "default", "paint:button::before.border"), ("content-card", "default", "paint:RoiProductItem_radioButton.border")])
# nav-link, m-burger and m-menu-pill focus-visible are hand-relabelled failed focus; these
# controls took a confirmed keyboard focus (Shift+Tab, Tab) and paint the same ring.
role("--focus-ring", "#005fcc", "The keyboard focus ring on the marketing chrome (buttons, pills, tabs).",
     readings=[("btn-outline", "focus-visible", "outlineColor"), ("collection-tab", "focus-visible", "outlineColor")])
role("--focus-ring-shop", "#000f2e", "The keyboard focus ring on shop controls.",
     readings=[("shop-nav-link", "focus-visible", "outlineColor")])

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
    ("focus-ring", "btn-outline", "focus-visible", "outlineColor", "color", "The keyboard focus ring colour on marketing controls (the header links' focus was never confirmed)."),
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

TRANSPARENT = "rgba(0, 0, 0, 0)"


def cover(st_):
    """The colour that paints the component's surface when the wrapper's own
    backgroundColor is transparent: the largest painted layer inside the box
    (a child div or the element's own ::before — Dopper's pills and overlays
    paint there), then the immediate ancestor's fill. None when nothing
    covers — a missing fill is never published as transparent."""
    r = st_.get("rect") or {}
    area = (r.get("w") or 0) * (r.get("h") or 0)
    best = None
    for p in st_.get("paint") or []:
        if not p.get("bg"):
            continue
        m = re.match(r"([\d.]+)(?:px)?x([\d.]+)(?:px)?", p.get("size") or "")
        if not m:
            continue
        pa = float(m.group(1)) * float(m.group(2))
        if area and pa < 0.5 * area:
            continue
        if best is None or pa > best[0]:
            best = (pa, p)
    if best:
        return best[1]["bg"], f"computed backgroundColor of the {best[1]['node']} layer inside"
    for a in st_.get("ancestors") or []:
        if a.get("bg") and a["bg"] != TRANSPARENT:
            return a["bg"], f"computed backgroundColor of the {a['node']} ancestor"
    return None, None


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
        if C[cname].get("missing"):
            continue  # a misidentified entry is a gap, not a value
        c = C[cname]["states"][state]
        if prop == "placeholder":
            v = (c.get("placeholder") or {}).get("color")
            src = f"computed {prop} of {cname} {state} (raw/components-computed.json)"
        elif prop == "backgroundColor" and (c["style"].get(prop) or TRANSPARENT) == TRANSPARENT:
            v, how = cover(c)
            src = f"{how} {cname} {state} (raw/components-computed.json)" if how else None
        else:
            v = c["style"].get(prop)
            src = f"computed {prop} of {cname} {state} (raw/components-computed.json)"
        if v:
            vn = find_var(norm_color(v))
            leaf = ({"var": vn, "type": "color",
                     "source": f"{src}; matches css-var {vn} resolved light", "description": desc}
                    if vn else
                    {"value": norm_color(v), "type": "color",
                     "source": src, "description": desc})
            comp[key] = leaf
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
        if C[cname].get("missing"):
            continue
        v = C[cname]["states"][state]["style"].get(prop)
        if v:
            vn = find_var(v)
            comp[key] = ({"var": vn, "type": "dimension",
                          "source": f"computed {prop} of {cname} {state}; matches css-var {vn} resolved light (raw/components-computed.json, raw/css-vars.json)",
                          "description": desc}
                         if vn else
                         {"value": v, "type": "dimension",
                          "source": f"computed {prop} of {cname} {state} (raw/components-computed.json)",
                          "description": desc})
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
