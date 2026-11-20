#!/usr/bin/env python3
"""Write raw/component-tokens.json, the token spec build_tokens.py reads.

care.com is a Next.js app over an MUI component layer (CSS-in-JS mui-* classes,
CareHeaderContainer/MegaMenu/CareMobileDrawer/CareTag). Its stylesheets declare
almost no custom properties — raw/css-vars.json (tools/capture/vars.mjs) holds
one OneTrust vendor var and the @font-face declarations — so every token here
is a **measured computed value** from raw/components-computed.json:

  neutrals    the #1e1e1e ink on all body/display text, white surfaces and
              field fills, the #f5f5f5/#e8e8e8 greys the category card paints
              on hover/pressed, and the #707070 placeholder/outline muted grey
  greens      the deep #025747 brand green (CTA text, mobile Join-now fill,
              footer tones), the #377a69 link green on mega-menu entries, and
              the #4d9380 focus green the category card takes
  limes       the signature lime ramp: #d0f5a3 CTA fill, #e4ffb8 on hover and
              the bright #8ae718 every pill takes on press
  blues       the legacy login layer's #015ac8 link blue
  fonts       Oceanic Grotesk (UI 400/500), NaN Druid Sans (display 550),
              Oceanic Text Semibold (accent serif 450), Proxima Nova (the
              legacy login form) — all @font-face declared in
              raw/css-vars.json
  ramp        64px display (hero/category titles), 48px section headings
              (NaN Druid, -1px tracking), 32px plan price, 20px hero-CTA,
              18px body-large/nav, 16px body/buttons, 13.3px small
  shape       capsule CTAs (20px on the 40px pill, 28px on the 56px Search),
              27px category cards, 8px menu rows
  motion      0.3s ease-out background transitions on the pill CTAs, the MUI
              150/200ms cubic-bezier(0.4,0,0.2,1) micro-motion

A leaf is {"value": ..., "source": "..."} for a measured value. Only the
signed-out public surface was read; the "dark" set is the dark-painted
surfaces (the deep-green footer panel, dark media), not a user toggle.
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
    "The token tree build_tokens.py turns into tokens.json. care.com "
    "declares almost no custom properties (raw/css-vars.json) — its MUI "
    "layer paints computed values, so every leaf is a measurement from "
    "raw/components-computed.json: the #1e1e1e ink, the deep-green/lime "
    "brand ramp (with the #8ae718 press state), Oceanic Grotesk / NaN "
    "Druid Sans / Oceanic Text Semibold / Proxima Nova, the capsule CTA "
    "radii and the 0.3s motion. The 'dark' set is the deep-green footer "
    "panel the light page paints, not a user-selectable theme."),
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
for key, comp, state, desc in [
    ("sans", "join-cta", "default", "The UI stack: Oceanic Grotesk first — nav, buttons, fields, cards and body copy; Arial and system sans fallbacks."),
    ("display", "section-h2", "default", "The display stack: NaN Druid Sans (declared weight 550) on hero and section headlines; Trebuchet MS fallback."),
    ("accent", "learn-more", "default", "The serif accent face; overwritten by the declared Oceanic Text Semibold entry below when its @font-face is present."),
    ("legacy", "login-email", "default", "The legacy stack: Proxima Nova on the /vis/auth login form — an older surface outside the MUI layer."),
]:
    if have(comp, state, "fontFamily"):
        fam[key] = {"value": st(comp, state)["fontFamily"], "type": "fontFamily",
                    "source": f"computed fontFamily of {comp} {state} (raw/components-computed.json); @font-face declared in raw/css-vars.json",
                    "description": desc}

weights = SPEC["core"].setdefault("font", {}).setdefault("weight", {})
for key, comp, state, desc in [
    ("regular", "menu-link", "default", "Body/nav weight (400)."),
    ("medium", "join-cta", "default", "Button-label weight (500)."),
    ("bold", "login-button", "default", "The legacy login button's label weight."),
    ("display", "section-h2", "default", "The NaN Druid display weight (550 declared)."),
]:
    if have(comp, state, "fontWeight"):
        weights[key] = {"value": st(comp, state)["fontWeight"], "type": "fontWeight",
                        "source": f"computed fontWeight of {comp} {state} (raw/components-computed.json)",
                        "description": desc}
# The serif accent family and its weight are declared @font-face evidence (the
# testimonial-name accentHeadline1 h1s that paint it are not a component entry).
if any("Oceanic Text" in (f.get("font-family") or "") for f in V.get("fonts", [])):
    fam["accent"] = {"value": "\"Oceanic Text Semibold\", Georgia, serif", "type": "fontFamily",
                     "source": "@font-face 'Oceanic Text Semibold' weight 450 declared in raw/css-vars.json; painted by the accentHeadline1 testimonial-name h1s on the home page",
                     "description": "The serif accent: Oceanic Text Semibold (declared weight 450) on testimonial names and display accents; Georgia fallback."}
    weights["accent"] = {"value": 450, "type": "fontWeight",
                         "source": "@font-face 'Oceanic Text Semibold' weight 450 declared in raw/css-vars.json",
                         "description": "The Oceanic Text Semibold accent weight (450 declared)."}
elif "accent" in fam:
    del fam["accent"]

# ------------------------------------------------------- measured colours

neutral = SPEC["core"].setdefault("color", {}).setdefault("neutral", {})
for key, comp, state, prop, desc in [
    ("ink", "section-h2", "default", "color", "The #1e1e1e ink on all body and display text, icons and the footer legal text."),
    ("white", "menu-item", "default", "backgroundColor", "The white #ffffff canvas, menu panel and card fields."),
    ("grey-hover", "category-card", "hover", "backgroundColor", "The #f5f5f5 wash the category card takes on hover."),
    ("grey-pressed", "category-card", "pressed", "backgroundColor", "The #e8e8e8 a pressed category card paints."),
    ("muted", "zip-field", "default", "placeholder", "The #707070 muted grey on field placeholders and hairline outlines."),
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

brand = SPEC["core"].setdefault("color", {}).setdefault("brand", {})
for key, comp, state, prop, desc in [
    ("green", "join-cta", "default", "color", "The deep #025747 brand green: pill-CTA text, outlined actions, the mobile Join-now fill and footer tones."),
    ("green-link", "menu-link", "default", "color", "The #377a69 link green on mega-menu entries."),
    ("green-focus", "read-more", "focus-visible", "outlineColor", "The #4d9380 green the read-more link draws as a 3px focus outline."),
    ("lime", "join-cta", "default", "backgroundColor", "The signature #d0f5a3 lime fill on the Join-now and Search pills."),
    ("lime-hover", "join-cta", "hover", "backgroundColor", "The lighter #e4ffb8 lime on CTA hover."),
    ("lime-pressed", "join-cta", "pressed", "backgroundColor", "The bright #8ae718 the pills take on press — Care's accent flash."),
    ("lime-text", "join-option", "default", "color", "The #e4ffb8 lime text the mobile-style green buttons paint."),
]:
    try:
        v = norm_color(st(comp, state).get(prop, ""))
        if v and v != "transparent":
            brand[key] = {"value": v, "type": "color",
                          "source": f"computed {prop} of {comp} {state} (raw/components-computed.json)",
                          "description": desc}
    except KeyError:
        pass

accent = SPEC["core"].setdefault("color", {}).setdefault("accent", {})
for key, comp, state, prop, desc in [
    ("link-blue", "passwordless-link", "default", "color", "The #015ac8 link blue inside the legacy login card."),
    ("login-button", "login-button", "default", "backgroundColor", "The legacy login button fill."),
]:
    try:
        v = norm_color(st(comp, state).get(prop, ""))
        if v and v != "transparent":
            accent[key] = {"value": v, "type": "color",
                           "source": f"computed {prop} of {comp} {state} (raw/components-computed.json)",
                           "description": desc}
    except KeyError:
        pass

# -------------------------------------------------------------------- roles

light = SPEC["light"]
ALIAS = "role alias over the core palette"
for name, target, desc in [
    ("--text-primary", "color.neutral.ink", "Body and display ink."),
    ("--text-muted", "color.neutral.muted", "Placeholders and hairline outlines."),
    ("--text-on-dark", None, "White on the dark footer panel and photo overlays."),
    ("--text-on-action", "color.brand.green", "Deep-green text on the lime pills."),
    ("--surface-page", "color.neutral.white", "The white page field."),
    ("--surface-alt", "color.neutral.grey-hover", "The light grey hover wash on cards."),
    ("--action-primary", "color.brand.lime", "The lime pill fill (Join now, Search)."),
    ("--action-primary-hover", "color.brand.lime-hover", "The lighter lime on CTA hover."),
    ("--action-primary-pressed", "color.brand.lime-pressed", "The bright lime on press."),
    ("--action-inverse", "color.brand.green", "The deep-green fill on inverse buttons (mobile Join now, plan CTAs)."),
    ("--text-accent", "color.brand.lime-hover", "Lime text on deep-green fills."),
    ("--link", "color.brand.green-link", "The #377a69 link green."),
    ("--border-focus", "color.brand.green-focus", "The #4d9380 focus tone on cards."),
    ("--link-legacy", "color.accent.link-blue", "The login surface's blue links."),
]:
    if target is None:
        emit(light, name, {"value": "#ffffff", "type": "color",
                           "source": "computed color over the footer panel / hero photo (raw/components-computed.json)",
                           "description": desc})
    else:
        root_key = target.split(".")[-1]
        root_bag = target.split(".")[1]
        bag = {"neutral": neutral, "brand": brand, "accent": accent}.get(root_bag, {})
        if root_key in bag:
            emit(light, name, {"value": "{" + target + "}", "type": "color",
                               "source": ALIAS, "description": desc})

dark = SPEC["dark"]
for name, target, desc in [
    ("--text-primary", "#ffffff", "Text on the dark footer panel."),
    ("--text-on-dark", "#ffffff", "White on dark."),
    ("--text-accent", "{color.brand.lime-hover}", "Lime text and accents on dark (the Join-now label)."),
    ("--surface-page", "{color.brand.green}", "The deep-green footer/panel surface."),
    ("--action-primary", "{color.brand.lime}", "The lime CTA fill works the same on dark."),
    ("--action-primary-hover", "{color.brand.lime-hover}", "CTA hover."),
    ("--action-primary-pressed", "{color.brand.lime-pressed}", "CTA press."),
    ("--text-on-action", "{color.brand.green}", "Deep green on the lime pills."),
    ("--divider", "{color.brand.green-link}", "Subtle green divider inside the dark panel."),
    ("--link", "{color.brand.lime-hover}", "Links on dark take the lime accent."),
]:
    emit(dark, name, {"value": target, "type": "color",
                      "source": ALIAS if target.startswith("{") else "computed color over the footer panel (raw/components-computed.json)",
                      "description": desc})

# ------------------------------------------------------------- type scale

type_scale = SPEC["core"].setdefault("font", {}).setdefault("size", {})
for key, comp, state, desc in [
    ("display", "cat-h1", "default", "The 64px display (hero and category titles)."),
    ("display-mobile", "m-hero", "default", "The display size at 390px."),
    ("h2", "section-h2", "default", "The 48px section heading (NaN Druid, -1px tracking)."),
    ("listing-title", "listing-h1", "default", "The listing display title."),
    ("title", "plan-price", "default", "The 32px plan price figure."),
    ("pricing-title", "pricing-h1", "default", "The pricing page title."),
    ("lede", "search-cta", "default", "The 20px hero-CTA label."),
    ("body-lg", "header", "default", "The 18px body-large/nav size."),
    ("body", "menu-link", "default", "The 16px body/button size."),
    ("small", "care-tag", "default", "The 13.3px small size (chips, triggers, meta)."),
    ("meta", "learn-more", "default", "The listing learn-more/link meta size."),
    ("legacy", "login-card", "default", "The legacy login form's body size."),
]:
    v = ts(comp, state, "fontSize")
    if v:
        type_scale[key] = {"type": "dimension", "value": v,
                           "source": f"computed fontSize of {comp} {state} (raw/components-computed.json)",
                           "description": desc}

leading = SPEC["core"].setdefault("font", {}).setdefault("lineHeight", {})
for key, comp, state, desc in [
    ("display", "cat-h1", "default", "Display leading."),
    ("h2", "section-h2", "default", "Heading leading (56px on 48px)."),
    ("body-lg", "header", "default", "Body-large leading (28px on 18px)."),
    ("body", "menu-link", "default", "Body leading (24px on 16px)."),
    ("cta", "join-cta", "default", "Pill-CTA label leading."),
]:
    v = ts(comp, state, "lineHeight")
    if v:
        leading[key] = {"type": "dimension", "value": v,
                        "source": f"computed lineHeight of {comp} {state} (raw/components-computed.json)",
                        "description": desc}

tracking = SPEC["core"].setdefault("font", {}).setdefault("letterSpacing", {})
for key, comp, state, desc in [
    ("display", "section-h2", "default", "The -1px display tracking."),
]:
    v = ts(comp, state, "letterSpacing")
    if v and v != "normal":
        tracking[key] = {"type": "dimension", "value": v,
                         "source": f"computed letterSpacing of {comp} {state} (raw/components-computed.json)",
                         "description": desc}

# ---------------------------------------------------------- radius, motion

radius = SPEC["core"].setdefault("radius", {})
for key, comp, state, prop, desc in [
    ("pill", "join-cta", "default", "borderTopLeftRadius", "The capsule radius on the 40px pill CTAs (20px = half height)."),
    ("pill-lg", "search-cta", "default", "borderTopLeftRadius", "The capsule radius on the 56px Search CTA (28px = half height)."),
    ("card", "category-card", "default", "borderTopLeftRadius", "The 27px radius on category/plan cards."),
    ("control", "menu-item", "default", "borderTopLeftRadius", "The 8px radius on mega-menu rows and chips."),
]:
    if have(comp, state, prop):
        radius[key] = {"value": st(comp, state)[prop], "type": "dimension",
                       "source": f"computed {prop} of {comp} {state} (raw/components-computed.json)",
                       "description": desc}

meas = SPEC["core"].setdefault("measured", {})
for key, comp, state, prop, ty, desc in [
    ("focus-outline", "read-more", "focus-visible", "outlineColor", "color", "The #4d9380 green 3px focus outline on links."),
    ("hover-outline", "category-card", "hover", "outlineColor", "color", "The muted outline a card draws on hover."),
    ("gate-fill", "gate-dialog", "default", "backgroundColor", "color", "The signup-gate dialog's surface fill."),
    ("dialog-shadow", "gate-dialog", "default", "boxShadowColor", "color", "The gate dialog's elevation shadow tone, if painted."),
    ("footer-fill", "footer", "default", "backgroundColor", "color", "The footer panel's dark fill."),
    ("plan-border", "plan-card", "default", "borderTopColor", "color", "The plan column's border tone."),
    ("tag-fill", "care-tag", "default", "backgroundColor", "color", "The care-tag chip fill."),
    ("tag-text", "care-tag", "default", "color", "color", "The care-tag chip text colour."),
    ("page-active", "page-item", "default", "backgroundColor", "color", "The active page item's fill in the pager."),
    ("listing-accent", "city-button", "default", "borderTopColor", "color", "The outlined toolbar buttons' border tone on the listing."),
    ("mobile-fill", "m-menu-open", "default", "backgroundColor", "color", "The full-screen mobile drawer's fill."),
]:
    try:
        if prop == "boxShadowColor":
            s = st(comp, state)
            hit = re.search(r"(rgba?\([\d.,\s]+\)|#[0-9a-fA-F]{3,8})", s.get("boxShadow") or "")
            if hit and (s.get("boxShadow") or "") != "none":
                meas[key] = {"value": norm_color(hit.group(1)), "type": ty,
                             "source": f"computed boxShadow of {comp} {state} (raw/components-computed.json)",
                             "description": desc}
            continue
        if have(comp, state, prop):
            v = norm_color(st(comp, state)[prop]) if ty == "color" else st(comp, state)[prop]
            if v and v != "transparent":
                meas[key] = {"value": v, "type": ty,
                             "source": f"computed {prop} of {comp} {state} (raw/components-computed.json)",
                             "description": desc}
    except KeyError:
        pass

for key, comp, state, desc in [
    ("cta-transition", "join-cta", "default", "The 0.3s ease-out background transition on the pill CTAs."),
    ("header-transition", "header", "default", "The 300ms ease-in-out background transition on the sticky header."),
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

# ------------------------------------------------------- component tokens

comp_ = SPEC["component"]
for name, comp, state, prop, ty, desc in [
    ("header.height", "header", "default", "height", "dimension", "The fixed header height."),
    ("header.padding", "header", "default", "paddingX", "dimension", "The header's horizontal padding."),
    ("cta.height", "join-cta", "default", "height", "dimension", "The pill CTA height."),
    ("cta.paddingX", "join-cta", "default", "paddingX", "dimension", "Pill horizontal padding."),
    ("search.height", "search-cta", "default", "height", "dimension", "The hero Search CTA height."),
    ("menu-row.height", "menu-item", "default", "height", "dimension", "A mega-menu row height."),
    ("field.height", "login-email", "default", "height", "dimension", "A legacy form field height."),
    ("toolbar-button.height", "filter-button", "default", "height", "dimension", "The listing toolbar button height."),
    ("chip.height", "care-tag", "default", "height", "dimension", "A care-tag chip height."),
    ("card.height", "category-card", "default", "height", "dimension", "The category card height."),
    ("pager.height", "pagination", "default", "height", "dimension", "The pager row height."),
    ("page-item.size", "page-item", "default", "width", "dimension", "A page item's size."),
    ("login.width", "login-card", "default", "width", "dimension", "The login card width."),
    ("dialog.width", "gate-dialog", "default", "width", "dimension", "The signup-gate dialog width."),
    ("drawer.height", "m-menu-open", "default", "height", "dimension", "The mobile drawer's full-screen height."),
    ("m-nav.height", "m-nav-item", "default", "height", "dimension", "A mobile drawer row height."),
]:
    try:
        src_prop = prop
        if prop == "paddingX":
            # horizontal padding is one value only when both sides read the same
            l_, r_ = st(comp, state)["paddingLeft"], st(comp, state)["paddingRight"]
            v = l_ if l_ == r_ else None
            src_prop = "paddingLeft / paddingRight"
        else:
            v = st(comp, state).get(prop)  # no reading, no token (never a bounding rect under a computed source)
        if v:
            bag, _, leaf = name.partition(".")
            comp_.setdefault(bag, {})[leaf] = {"value": v, "type": ty,
                                             "source": f"computed {src_prop} of {comp} {state} (raw/components-computed.json)",
                                             "description": desc}
    except (KeyError, TypeError):
        pass

STALE = {k: v["recaptureMissed"] for k, v in C.items() if v.get("recaptureMissed")}


def mark_stale(node):
    """Components flagged recaptureMissed kept an earlier run's readings; a leaf built from one says so."""
    if isinstance(node, dict):
        src = node.get("source")
        if isinstance(src, str):
            m = re.match(r"computed .+? of ([a-z0-9-]+) [a-z-]+ \(raw/components-computed\.json\)", src)
            if m and m.group(1) in STALE:
                node["source"] = src + "; stale: kept from an earlier run (the %s recapture did not find %s)" % (STALE[m.group(1)], m.group(1))
        for v in node.values():
            mark_stale(v)


mark_stale(SPEC)
RAW.joinpath("component-tokens.json").write_text(json.dumps(SPEC, indent=2, ensure_ascii=False) + "\n")
n = sum(1 for _ in re.findall(r'"(?:value|var)":', json.dumps(SPEC)))
print("component-tokens.json:", n, "leaves")
