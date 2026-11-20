#!/usr/bin/env python3
"""Write raw/component-tokens.json, the token spec build_tokens.py reads.

byborre.com is a Nuxt marketing/catalogue app whose Tailwind theme declares a
real custom-property layer — the --color-primary-50..950 green ramp and
--color-gray-DEFAULT harvested into raw/css-vars.json (tools/capture/vars.mjs),
held as Tailwind channel triplets ("0 230 6") that utilities composite with an
alpha. Those become {"var": ...} leaves, resolved per theme by build_tokens.py
(the triplet is a raw rgb() channel list). Everything else is **measured
computed values** from raw/components-computed.json:

  neutrals    the black-BRAND ink #1b1b1b and the cream ramp the site paints:
              #f5f5f0 canvas/buttons, #e5e5e1 filter-bar hairline, #ccccc4
              field/tab/chip borders, #999993 muted icons + chip hover ring +
              the "Collaboration" badge outline, #646e69 field placeholders +
              text-link hover, #454542 the footer's on-dark divider, white
              field fills
  brand       the declared --color-primary-* green ramp (DEFAULT 500 #00e606,
              the focus outline on cards/links; dark flips DEFAULT to 400);
              the #fae210 yellow every ink button takes on hover and its
              #c8b50d hover border; --color-gray-DEFAULT #7c7c7c
  dark        the ink surfaces the light page paints — the #1b1b1b footer
              panel (24px top radius), the marquee bar and the hero media:
              white text, #f5f5f0 labels, the same yellow hover accent
  font        Helvetica Neue 400/500/700 (declared @font-face) everywhere
  ramp        measured 80/84 display, 48/48-53 headings, 24/32 lede, 16/24
              body+buttons, 16/20 nav, 13/19.5 small, 12/16 meta, 11/12 marquee,
              10/12.5 footer links
  shape       10px controls (buttons/fields/tabs/dropdown), 8px links/nav,
              9999px chips/swatches/badge, 24px footer panel
  states      focus = a 2px transparent outline offset 2px PLUS an inset
              box-shadow ring (white 0 0 0 0, ink 0 0 0 2px); cards/links fall
              back to `1px auto` outlines (#00e606 primary, #005fcc UA);
              hover turns ink buttons #fae210 yellow; pressed scales 0.98;
              controls transition 0.15s, fades 0.3s cubic-bezier(0.4,0,0.2,1)

A leaf is {"var": "--name"} (resolved per theme) or
{"value": ..., "source": "..."} for a measured value. Only the signed-out
public surface was read; the "dark" set is the ink-painted surfaces (footer,
marquee, hero media), not a user toggle.
"""
import json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
V = json.loads((RAW / "css-vars.json").read_text())
RL = V.get("resolved", {}).get("light", {})
C = json.loads((RAW / "components-computed.json").read_text())["components"]


def current(comp):
    """The component's entry, refused when the last run did not read it: missing
    (no states) or recaptureMissed (earlier states kept under their own
    provenance) is not a current reading, so it cannot source a role."""
    c = C[comp]
    if c.get("missing") or c.get("recaptureMissed"):
        raise KeyError(f"{comp}: not a current reading (missing or recaptureMissed)")
    return c
R = {n: v.get("value", v.get("raw")) for n, v in RL.items()}


def var(name, ty="color", **kw):
    d = {"var": name, "type": ty}
    d.update(kw)
    return d


SPEC = {"_about": (
    "The token tree build_tokens.py turns into tokens.json. byborre.com "
    "declares a Tailwind custom-property layer in its Nuxt bundle "
    "(raw/css-vars.json) — the --color-primary-* green ramp and "
    "--color-gray-DEFAULT, held as rgb() channel triplets — plus measured "
    "computed styles (raw/components-computed.json) for the ink/cream "
    "neutrals, the yellow hover accent, Helvetica Neue, the 10px control "
    "radius and the 0.15s/0.3s motion. The 'dark' set is the #1b1b1b ink "
    "surfaces the light page paints (footer, marquee, hero media), not a "
    "user-selectable theme."),
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


def painted(comp, state):
    """First painted fill on or under the component."""
    try:
        c = C[comp]["states"][state]
    except KeyError:
        return None
    for n in c.get("paint") or []:
        if n.get("bg"):
            return n["bg"]
    for n in c.get("ancestors") or []:
        if n.get("bg"):
            return n["bg"]
    return None


def paint_node(comp, state, prop):
    """A property of the first painted layer under the component."""
    try:
        for n in C[comp]["states"][state].get("paint") or []:
            if n.get(prop):
                return n[prop]
    except KeyError:
        pass
    return None


# ------------------------------------------------------------------- fonts

fam = SPEC["core"].setdefault("font", {}).setdefault("family", {})
if have("hero-cta", "default", "fontFamily"):
    fam["sans"] = {"value": st("hero-cta", "default")["fontFamily"], "type": "fontFamily",
                   "source": "computed fontFamily of hero-cta default (raw/components-computed.json); @font-face 'Helvetica Neue' 400/500/700 declared in raw/css-vars.json",
                   "description": "The one stack the whole site paints: Helvetica Neue first, Arial and the system sans fallbacks."}
weights = SPEC["core"].setdefault("font", {}).setdefault("weight", {})
for key, comp, state, desc in [
    ("regular", "nav-link", "default", "Body/nav weight (400)."),
    ("medium", "page-title", "default", "Display and button-label weight (500)."),
]:
    if have(comp, state, "fontWeight"):
        weights[key] = {"value": st(comp, state)["fontWeight"], "type": "fontWeight",
                        "source": f"computed fontWeight of {comp} {state} (raw/components-computed.json)",
                        "description": desc}
weights["bold"] = {"value": 700, "type": "fontWeight",
                   "source": "@font-face 'Helvetica Neue' weight 700 in raw/css-vars.json",
                   "description": "The declared bold face; nothing on the captured surface paints it."}

# ------------------------------------------------------- declared colours

neutral = SPEC["core"].setdefault("color", {}).setdefault("neutral", {})
for key, comp, state, prop, desc in [
    ("ink", "hero-cta", "default", "color", "The black-BRAND ink #1b1b1b: all text, the dark button fill, the footer/marquee panels and the focus ring."),
    ("cream", "filter-bar", "default", "backgroundColor", "The cream #f5f5f0 canvas — page field, filter bar, secondary buttons, view tabs and the mobile menu."),
    ("field", "text-field", "default", "backgroundColor", "The white #ffffff fill inside the 1px field border."),
    ("line", "text-field", "default", "borderTopColor", "The cream-300 #ccccc4 on every field, tab, dropdown, colour-chip ring and mobile-menu row border."),
    ("muted", "text-field", "default", "placeholder", "The cream-500 #646e69 on field placeholders and text-link hover."),
]:
    try:
        if prop == "placeholder":
            v = norm_color(C[comp]["states"][state].get("placeholder", {}).get("color"))
        else:
            v = norm_color(st(comp, state).get(prop, ""))
        if v and v != "transparent":
            neutral[key] = {"value": v, "type": "color",
                            "source": f"computed {prop} of {comp} {state} (raw/components-computed.json)",
                            "description": desc}
    except KeyError:
        pass
# cream tones only visible on painted layers/icons
for key, comp, state, prop, node_re, desc in [
    ("hairline", "filter-bar", "default", "border", r"229,\s*229,\s*225", "The cream-200 #e5e5e1 hairline painted inside the collection filter bar."),
    ("icon-muted", "view-tab", "default", "bg", r"153,\s*153,\s*147", "The cream-400 #999993 on the tabs' + icon, the Collaboration badge outline and the colour-chip hover ring."),
    ("divider-dark", "footer", "default", "border", r"69,\s*69,\s*66", "The cream-600 #454542 divider inside the ink footer panel."),
]:
    try:
        hit = None
        for n in C[comp]["states"][state].get("paint") or []:
            val = n.get(prop) or ""
            if re.search(node_re, val):
                hit = re.search(node_re, val).group(0)
                break
        if hit:
            neutral[key] = {"value": "rgb(" + hit + ")", "type": "color",
                            "source": f"painted layer {prop} of {comp} {state} (raw/components-computed.json)",
                            "description": desc}
    except KeyError:
        pass

brand = SPEC["core"].setdefault("color", {}).setdefault("brand", {})
# the declared green ramp, var-referenced so both themes resolve it
for step in ("50", "100", "200", "300", "400", "500", "600", "700", "800", "900", "950"):
    vn = f"--color-primary-{step}"
    if vn in R:
        brand[f"primary-{step}"] = var(vn, "color",
                                       description=f"The declared primary {step} channel triplet (Tailwind rgb(var(--{vn[2:]}) / a)).")
if "--color-primary-DEFAULT" in R:
    brand["primary"] = var("--color-primary-DEFAULT", "color",
                           description="primary DEFAULT: 500 in light, 400 under .dark.")
if "--color-gray-DEFAULT" in R:
    neutral["grey"] = var("--color-gray-DEFAULT", "color",
                          description="The declared --color-gray-DEFAULT channel triplet #7c7c7c.")
# measured accents
if have("order-cta", "hover", "backgroundColor"):
    brand["accent"] = {"value": norm_color(st("order-cta", "hover")["backgroundColor"]), "type": "color",
                       "source": "computed backgroundColor of order-cta hover (raw/components-computed.json)",
                       "description": "The #fae210 yellow every ink button and the hero CTA takes on hover — the site's signature accent."}
try:
    b = norm_color(st("order-cta", "hover")["borderTopColor"])
    if b != norm_color(st("order-cta", "hover")["backgroundColor"]):
        brand["accent-border"] = {"value": b, "type": "color",
                                  "source": "computed borderTopColor of order-cta hover (raw/components-computed.json)",
                                  "description": "The deeper #c8b50d edge the yellow hover keeps."}
except KeyError:
    pass

# -------------------------------------------------------------------- roles

light = SPEC["light"]
ALIAS = "role alias over the core palette"
for name, target, desc in [
    ("--text-primary", "color.neutral.ink", "Body and display ink."),
    ("--text-muted", "color.neutral.muted", "Placeholders and text-link hover."),
    ("--text-on-dark", None, "The white on the ink footer, marquee and hero media."),
    ("--surface-page", "color.neutral.cream", "The cream page field."),
    ("--surface-field", "color.neutral.field", "The white field fill."),
    ("--surface-alt", "color.neutral.cream", "View tabs, filter bar, mobile menu and secondary buttons."),
    ("--action-primary", "color.neutral.ink", "The ink button fill."),
    ("--action-primary-hover", "color.brand.accent", "The yellow every ink button takes on hover."),
    ("--text-on-action", "color.neutral.cream", "The cream label on the ink buttons."),
    ("--border-field", "color.neutral.line", "The 1px field/tab/dropdown border."),
    ("--border-hairline", "color.neutral.hairline", "The #e5e5e1 hairline."),
    ("--border-focus", "color.neutral.icon-muted", "The colour-chip ring's hover tone (#999993)."),
    ("--divider-on-dark", "color.neutral.divider-dark", "The footer divider on ink."),
    ("--icon-muted", "color.neutral.icon-muted", "Muted glyph colour (+ icons, badge outline)."),
]:
    if target is None:
        _on_dark = {norm_color(current(c)["states"]["default"]["style"].get("color", "")) for c in ("footer-link", "hero-title")}
        if len(_on_dark) != 1:
            raise ValueError(f"{name}: readings differ: {sorted(_on_dark)}")
        emit(light, name, {"value": _on_dark.pop(), "type": "color",
                           "source": "computed color of footer-link/hero-title (raw/components-computed.json)",
                           "description": desc})
    else:
        root_key = target.split(".")[-1]
        root_bag = target.split(".")[1]
        if root_key in (neutral if root_bag == "neutral" else brand):
            emit(light, name, {"value": "{" + target + "}", "type": "color",
                               "source": ALIAS, "description": desc})

dark = SPEC["dark"]
for name, target, desc in [
    ("--text-primary", "#ffffff", "Text on the ink surfaces (footer links, hero title over dark media)."),
    ("--text-on-dark", "#ffffff", "White on ink."),
    ("--text-secondary", "{color.neutral.cream}", "The #f5f5f0 label on the ink buttons and the marquee bar."),
    ("--surface-page", "{color.neutral.ink}", "The ink surface: footer panel, marquee bar, hero media."),
    ("--action-primary", "{color.neutral.ink}", "The ink button fill (unchanged)."),
    ("--action-primary-hover", "{color.brand.accent}", "The same yellow hover accent."),
    ("--text-on-action", "{color.neutral.cream}", "Cream on the ink buttons."),
    ("--divider", "{color.neutral.divider-dark}", "The #454542 footer divider."),
    ("--border-focus", "{color.brand.primary}", "The #00e606 primary focus outline on links and cards."),
]:
    emit(dark, name, {"value": target, "type": "color",
                      "source": ALIAS if target.startswith("{") else "computed color of footer/hero-title over ink (raw/components-computed.json)",
                      "description": desc})

# ------------------------------------------------------------- type scale

type_scale = SPEC["core"].setdefault("font", {}).setdefault("size", {})
for key, comp, state, desc in [
    ("display", "page-title", "default", "The 80px display (Textile Room, FAQ, Contact titles)."),
    ("display-mobile", "m-hero", "default", "The 48px display at 390px."),
    ("h2", "section-h2", "default", "The 48px section heading."),
    ("title", "textile-title", "default", "The 48px textile-detail title."),
    ("lede", "hero-sub", "default", "The 24px hero lede."),
    ("name", "person-card", "default", "The 40px contact-name size."),
    ("body", "hero-cta", "default", "The 16px body/button/nav size."),
    ("small", "filter-bar", "default", "The 13px small text (filter bar, cards, spec rows, FAQ rows)."),
    ("meta", "pattern-dropdown", "default", "The 12px meta size (dropdown trigger, card labels, nav badge)."),
    ("micro", "marquee", "default", "The 11px marquee text."),
    ("foot", "footer-link", "default", "The 10px footer links."),
]:
    v = ts(comp, state, "fontSize")
    if v:
        type_scale[key] = {"type": "dimension", "value": v,
                           "source": f"computed fontSize of {comp} {state} (raw/components-computed.json)",
                           "description": desc}

leading = SPEC["core"].setdefault("font", {}).setdefault("lineHeight", {})
for key, comp, state, desc in [
    ("display", "page-title", "default", "Display leading (84px on 80px type)."),
    ("h2", "section-h2", "default", "Heading leading."),
    ("lede", "hero-sub", "default", "Lede leading."),
    ("body", "hero-cta", "default", "Body/button leading."),
    ("small", "filter-bar", "default", "Small-text leading."),
    ("micro", "marquee", "default", "Marquee leading."),
]:
    v = ts(comp, state, "lineHeight")
    if v:
        leading[key] = {"type": "dimension", "value": v,
                        "source": f"computed lineHeight of {comp} {state} (raw/components-computed.json)",
                        "description": desc}

# ---------------------------------------------------------- radius, motion

radius = SPEC["core"].setdefault("radius", {})
for key, comp, state, prop, desc in [
    ("control", "hero-cta", "default", "borderTopLeftRadius", "The 10px radius on buttons, fields, tabs and the dropdown trigger."),
    ("link", "nav-link", "default", "borderTopLeftRadius", "The 8px radius on nav links, flyout links, swatches and menu rows."),
    ("panel", "footer", "default", "borderTopLeftRadius", "The 24px top radius on the ink footer panel."),
]:
    if have(comp, state, prop):
        radius[key] = {"value": st(comp, state)[prop], "type": "dimension",
                       "source": f"computed {prop} of {comp} {state} (raw/components-computed.json)",
                       "description": desc}
chip_r = paint_node("colour-chip", "default", "radius")
if chip_r:
    radius["chip"] = {"value": chip_r, "type": "dimension",
                      "source": "painted layer radius of colour-chip (raw/components-computed.json)",
                      "description": "The 9999px pill on colour chips, the card badge and the card's circle actions."}
card_r = paint_node("textile-card", "default", "radius")
if card_r:
    radius["card"] = {"value": card_r, "type": "dimension",
                      "source": "painted layer radius of textile-card (raw/components-computed.json)",
                      "description": "The 10px radius on the textile-card image tile."}

meas = SPEC["core"].setdefault("measured", {})
# the focus ring is a transparent 2px outline offset 2px PLUS an inset ink shadow
try:
    s = st("nav-link", "focus-visible")
    if s.get("boxShadow") and s["boxShadow"] != "none":
        m = re.findall(r"(rgba?\([\d.,\s]+\)|#[0-9a-fA-F]{3,8})\s+(-?\d+(?:\.\d+)?px)\s+(-?\d+(?:\.\d+)?px)\s+(-?\d+(?:\.\d+)?px)\s+(-?\d+(?:\.\d+)?px)( inset)?", s["boxShadow"])
        if m:
            meas["focus-ring"] = {"value": [{"color": norm_color(a), "offsetX": x, "offsetY": y, "blur": bl, "spread": sp, "inset": bool(i)} for a, x, y, bl, sp, i in m],
                                  "type": "shadow",
                                  "source": "computed boxShadow of nav-link focus-visible (raw/components-computed.json)",
                                  "description": "The keyboard-focus ring on links/buttons/fields: a white 0-spread layer plus a 2px ink ring drawn inset — the outline itself is 2px rgba(0,0,0,0) offset 2px."}
except KeyError:
    pass
for key, comp, state, prop, ty, desc in [
    ("focus-accent", "textile-card", "focus-visible", "outlineColor", "color", "The #00e606 primary outline links and cards take on keyboard focus (1px auto)."),
    ("focus-fallback", "faq-question", "focus-visible", "outlineColor", "color", "The #005fcc UA fallback outline the FAQ rows and view tabs get — the site styles no ring on them."),
    ("chip-hover-border", "colour-chip", "hover", "child-border", "color", "The #999993 ring a colour chip takes on hover (was #ccccc4)."),
    ("dropdown-hover", "pattern-dropdown", "hover", "backgroundColor", "color", "The 10%-black wash the Pattern dropdown gets on hover."),
    ("card-scrim", "textile-card", "default", "scrim", "color", "The 30%-black scrim over textile-card imagery."),
    ("chip-blue", "colour-chip", "default", "chip-fill", "color", "The #0e4c92 fill the BLUE colour chip paints — a textile colour, not a UI role."),
]:
    try:
        if prop == "child-border":
            hit = next((n.get("border") for n in C[comp]["states"][state].get("paint", []) if n.get("border")), None)
            if hit:
                m = re.search(r"(rgba?\([\d.,\s]+\)|#[0-9a-fA-F]{3,8})", hit)
                if m:
                    meas[key] = {"value": norm_color(m.group(1)), "type": ty,
                                 "source": f"painted layer border of {comp} {state} (raw/components-computed.json)",
                                 "description": desc}
            continue
        if prop == "scrim":
            hit = next((n.get("bg") for n in C[comp]["states"][state].get("paint", []) if n.get("bg") and "0.3" in str(n.get("bg"))), None)
            if hit:
                meas[key] = {"value": norm_color(hit), "type": ty,
                             "source": f"painted scrim layer of {comp} {state} (raw/components-computed.json)",
                             "description": desc}
            continue
        if prop == "chip-fill":
            hit = next((n.get("bg") for n in C[comp]["states"][state].get("paint", []) if n.get("bg") and "76" in str(n.get("bg"))), None)
            if hit:
                meas[key] = {"value": norm_color(hit), "type": ty,
                             "source": f"painted swatch fill of {comp} {state} (raw/components-computed.json)",
                             "description": desc}
            continue
        if have(comp, state, prop):
            v = norm_color(st(comp, state)[prop]) if ty == "color" else st(comp, state)[prop]
            meas[key] = {"value": v, "type": ty,
                         "source": f"computed {prop} of {comp} {state} (raw/components-computed.json)",
                         "description": desc}
    except KeyError:
        pass
for key, comp, state, desc in [
    ("control-transition", "hero-cta", "default", "The 0.15s control transition (colour/background)."),
    ("link-transition", "nav-link", "default", "The nav link's 0.15s transition."),
]:
    try:
        s = st(comp, state)
        d = s["transitionDuration"]
        first = d.split(",")[0].strip()
        if first and first != "0s":
            meas[key] = {"value": first, "type": "duration",
                         "source": f"computed transition of {comp} {state} (raw/components-computed.json)",
                         "description": desc + f" ({s['transitionProperty']})"}
    except (KeyError, TypeError):
        pass
# pressed buttons shrink to ~98%
try:
    d0 = C["hero-cta"]["states"]["default"]["rect"]["w"]
    dp = C["hero-cta"]["states"]["pressed"]["rect"]["w"]
    if d0 and dp and dp < d0:
        meas["pressed-scale"] = {"value": round(dp / d0, 4), "type": "number",
                                 "source": "pressed rect / default rect of hero-cta (raw/components-computed.json)",
                                 "description": "The 0.98 scale a pressed button takes."}
except KeyError:
    pass
# motion declared in the readable sheets (computed rows cover the painted rules)
meas["marquee-duration"] = {"value": "10000ms", "type": "duration",
                            "source": "animation 'marquee-063d6d2b' 10s linear infinite in the readable stylesheet (raw/css-vars.json) and the reducedMotion probe in raw/components-computed.json",
                            "description": "The top ticker's 10s linear scroll; it keeps running under prefers-reduced-motion."}
meas["fade-300"] = {"value": "300ms", "type": "duration",
                    "source": "transition declarations in the readable sheets (raw/components-computed.json _meta.sheets)",
                    "description": "The 0.3s cubic-bezier(0.4,0,0.2,1) opacity/transform/max-height the site's toggles declare."}
meas["ease-default"] = {"value": [0.4, 0, 0.2, 1], "type": "cubicBezier",
                        "source": "transition declarations in the readable sheets (raw/components-computed.json _meta.sheets)",
                        "description": "The cubic-bezier(0.4,0,0.2,1) easing on the 0.3s toggles."}

# ------------------------------------------------------------------ component

comp = SPEC["component"]
for key, cname, state, prop, desc in [
    ("button.height", "hero-cta", "default", "height", "The 48px primary/secondary button height."),
    ("field.height", "text-field", "default", "height", "The 48px field height."),
    ("tab.height", "view-tab", "default", "height", "The 36px view-tab height."),
    ("dropdown.height", "pattern-dropdown", "default", "height", "The 32px dropdown-trigger height."),
    ("chip.size", "colour-chip", "default", "height", "The 32px colour-chip circle."),
    ("iconbutton.size", "cart-button", "default", "width", "The 32px header icon buttons."),
    ("navlink.height", "nav-link", "default", "height", "The 28px nav-link row."),
    ("menurow.height", "m-nav-item", "default", "height", "The 48px mobile-menu row."),
    ("header.height", "header", "default", "height", "The 57px desktop header."),
    ("header.height-mobile", "m-header", "default", "height", "The 64px mobile header."),
    ("flyout.height", "nav-dropdown", "default", "height", "The 210px nav flyout."),
    ("faqrow.height", "faq-question", "default", "height", "The 56px accordion row."),
]:
    if have(cname, state, prop):
        node = comp
        parts = key.split(".")
        for p in parts[:-1]:
            node = node.setdefault(p, {})
        node[parts[-1]] = {"type": "dimension", "value": st(cname, state)[prop],
                           "source": f"computed {prop} of {cname} {state} (raw/components-computed.json)",
                           "description": desc}

(RAW / "component-tokens.json").write_text(json.dumps(SPEC, indent=1, ensure_ascii=False) + "\n")


def count(d):
    if not isinstance(d, dict):
        return 1
    if "var" in d or "value" in d or "$value" in d:
        return 1
    return sum(count(v) for v in d.values())


print({k: count(v) for k, v in SPEC.items() if not k.startswith("_")})
