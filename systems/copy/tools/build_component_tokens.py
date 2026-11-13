#!/usr/bin/env python3
"""Write raw/component-tokens.json, the token spec build_tokens.py reads.

copy.ai's public signed-out surface is a Webflow marketing site: its styles
arrive as linked sheets from cdn.prod.website-files.com (cross-origin to the
CSSOM, so vars.mjs reads every body off the network) and declare a small named
custom-property layer on :root — the --colors--* brand palette plus a legacy
--old-swatches--* set — resolved in raw/css-vars.json. Those become
{"var": ...} leaves resolved by build_tokens.py. Everything else is
**measured computed values** from raw/components-computed.json:

  neutrals    the #171717 ink (all display text, the black buttons, the
              top-banner fill), white surfaces, the #222222 nav ink, the
              #5d5d5d declared muted, the #566b76 slate lede and the
              #3a4554 FAQ answer gray, the #f6fafb field fill
  brand       the #693ee0 primary purple — declared as
              --colors--primary-purple and measured on btn-nav, plan-price,
              the SAVING badge and the auth Continue; the measured auth-host
              ramp #5b36c3 hover / #4e22b1 pressed; the #a284ff light
              purple and the #29007a deep band purple; the auth host's
              #5753c6 sign-up link
  states      the black buttons' signature move: fill lifts to purple on
              hover (#683ee4/#693ee0 on plan-cta, hero-submit, invert-cta);
              the nav triggers take an ink inset underline; the auth host's
              OAuth buttons ring with a 19%→27% black inset and take a 6%
              black pressed wash
  borders     #e0e0e0 cards/menu-row hairlines, #e4edf1 field, #ccd9e0 the
              playbook chip, #e5e7eb on the auth card, #4a4b52 declared dark
  focus       #005fcc 1px auto on buttons/links, #4d65ff 2px solid on
              dropdown/accordion rows, #a396ff on the auth host
  font        "ABC Normal" display (88/72/64/56/42.9 headings, 24-32 card
              titles), Inter for UI (16/24 controls and body, 14/20 small,
              12/22 badge); the auth host paints its own "interFont" stack
  shape       4px nav CTA / sales, 4.5px auth buttons, 3.5px auth field,
              5px contact fields, 8px big CTAs and secondary buttons,
              40px badge pill, 48px plan-toggle pill
  elevation   the plan-toggle's rgba(0,0,0,0.06) 0 28 64 float, the mega-
              menu's rgba(0,0,0,0.03) 0 40 34 drop, the playbook chip's
              inset rgba(204,217,224,0.2) 0 -3 0, the nav underline's
              0 -1 0 ink inset, the OAuth ring's 1px 19-27% black inset

A leaf is {"var": ...} (resolved by build_tokens.py) or
{"value": ..., "source": ...} for a measured value. Only the signed-out
public surface was read; the "dark" set is the ink/purple bands the light
pages paint (top banner, the deep-purple feature card, the inverted CTA's
own band), not a user-selectable theme.
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
    "The token tree build_tokens.py turns into tokens.json. copy.ai's "
    "public surface is a Webflow site whose small --colors--* declaration "
    "(raw/css-vars.json — the brand palette plus the legacy "
    "--old-swatches--* set) is var-referenced where it names the brand and "
    "neutral values, and measured computed values "
    "(raw/components-computed.json) cover the ink/white neutrals, the "
    "#693ee0 action purple and its auth-host ramp, the black-button "
    "hover-to-purple state move, the hairline borders, the inset shadows, "
    "ABC Normal and Inter type, the 4/4.5/5/8/40/48px radii and the "
    "0.1-0.4s control motion. The 'dark' set is the ink banner and the "
    "deep-purple card bands the light pages paint, not a user toggle."),
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
    """First resolved var whose value matches; prefer a --colors--* name."""
    best = None
    for n, v in R.items():
        if v == value and (contains is None or contains in n):
            if n.startswith("--colors--"):
                return n
            best = best or n
    return best


# ------------------------------------------------------------------- fonts

fam = SPEC["core"].setdefault("font", {}).setdefault("family", {})
if have("hero-title", "default", "fontFamily"):
    fam["display"] = {"value": st("hero-title", "default")["fontFamily"], "type": "fontFamily",
                      "source": "computed fontFamily of hero-title default (raw/components-computed.json); the @font-face blocks are served from cdn.prod.website-files.com (raw/css-vars.json fonts)",
                      "description": "The display family: ABC Normal (licensed, not distributed), falling back to sans."}
if have("btn-nav", "default", "fontFamily"):
    fam["sans"] = {"value": st("btn-nav", "default")["fontFamily"], "type": "fontFamily",
                   "source": "computed fontFamily of btn-nav default (raw/components-computed.json)",
                   "description": "The UI family: Inter, falling back to sans."}
if have("auth-continue", "default", "fontFamily"):
    fam["auth"] = {"value": st("auth-continue", "default")["fontFamily"], "type": "fontFamily",
                   "source": "computed fontFamily of auth-continue default (raw/components-computed.json)",
                   "description": "The auth host's stack (login.copy.ai): its own interFont bundle then system sans."}
weights = SPEC["core"].setdefault("font", {}).setdefault("weight", {})
for key, comp, state, desc in [
    ("regular", "hero-sub", "default", "Body and small weight (400)."),
    ("medium", "dd-link", "default", "The 500 weight on nav items, controls and prices."),
    ("semibold", "hero-title", "default", "The 600 weight on display headings."),
    ("bold", "plan-cta", "default", "The 700 weight on button labels and the contact display."),
]:
    v = ts(comp, state, "fontWeight")
    if v:
        weights[key] = {"value": int(v), "type": "fontWeight",
                        "source": f"computed fontWeight of {comp} {state} (raw/components-computed.json)",
                        "description": desc}

# ------------------------------------------------------- declared colours

brand = SPEC["core"].setdefault("color", {}).setdefault("brand", {})
for key, want, desc in [
    ("purple", "#693ee0", "The Copy.ai purple #693ee0 — declared as --colors--primary-purple, painted by the nav CTA, plan prices, the SAVING badge and the auth Continue."),
    ("purple-light", "#a284ff", "The declared light purple #a284ff (--colors--light-purple)."),
]:
    vn = find_var(want)
    if vn:
        brand[key] = var(vn, "color",
                         source=f"css-var {vn} resolved light (raw/css-vars.json)",
                         description=desc)
# measured purple steps: the auth host's own ramp and the deep band
for key, comp, state, prop, desc in [
    ("purple-hover", "auth-continue", "hover", "backgroundColor", "The auth host's #5b36c3 hover step on Continue with email."),
    ("purple-pressed", "auth-continue", "pressed", "backgroundColor", "The auth host's #4e22b1 pressed step."),
    ("purple-deep", "platform-card", "default", "backgroundColor", "The #29007a deep purple the platform-feature band paints."),
]:
    try:
        v = norm_color(st(comp, state)[prop])
        brand[key] = {"value": v, "type": "color",
                      "source": f"computed {prop} of {comp} {state} (raw/components-computed.json)",
                      "description": desc}
    except KeyError:
        pass
try:
    brand["link"] = {"value": norm_color(st("auth-signup", "default")["color"]), "type": "color",
                     "source": "computed color of auth-signup default (raw/components-computed.json)",
                     "description": "The auth host's #5753c6 link purple (Sign up, Terms)."}
except KeyError:
    pass

# measured + declared neutrals
neutral = SPEC["core"].setdefault("color", {}).setdefault("neutral", {})
for key, value, desc in [
    ("ink", "#171717", "The #171717 ink: display text, the black buttons, the top-banner fill — also declared as --colors--primary-black."),
    ("white", "#ffffff", "The #ffffff surface: page, cards, the mega-menu panel, inverted CTA fills."),
    ("off-white", "#fbfbfc", "The declared off-white #fbfbfc (--colors--off-white / --colors--primary-gray-white)."),
    ("muted", "#5d5d5d", "The declared muted gray #5d5d5d (--colors--grey / --text-gray)."),
    ("border", "#e0e0e0", "The declared #e0e0e0 hairline (--colors--borders-lite-grey): cards, the mobile menu rows, the mega-menu's top edge."),
    ("border-dark", "#4a4b52", "The declared dark border #4a4b52 (--colors--borders-dark-grey)."),
]:
    vn = find_var(value)
    if vn:
        neutral[key] = var(vn, "color",
                           source=f"css-var {vn} resolved light (raw/css-vars.json)",
                           description=desc)
    else:
        neutral[key] = {"value": value, "type": "color",
                        "source": "declared value (raw/css-vars.json)",
                        "description": desc}
for key, comp, state, prop, desc in [
    ("nav-ink", "dd-link", "default", "color", "The #222222 nav/menu ink (mega-menu links are #171717; the nav triggers read #222222)."),
    ("lede", "hero-sub", "default", "color", "The #566b76 slate the hero lede paints."),
    ("faq-text", "faq-item", "default", "color", "The #3a4554 blue-gray of FAQ answers and fine print."),
    ("field", "hero-email", "default", "backgroundColor", "The #f6fafb field fill."),
    ("border-field", "hero-email", "default", "borderTopColor", "The #e4edf1 field border."),
    ("border-card", "playbook-card", "default", "borderTopColor", "The #ccd9e0 border on the playbook chip."),
]:
    try:
        neutral[key] = {"value": norm_color(st(comp, state)[prop]), "type": "color",
                        "source": f"computed {prop} of {comp} {state} (raw/components-computed.json)",
                        "description": desc}
    except KeyError:
        pass
# the auth host's own neutrals
for key, comp, state, prop, desc in [
    ("auth-ink", "auth-card", "default", "color", "The auth host's #202020 ink (login.copy.ai — a different system from the marketing site)."),
    ("auth-border", "auth-card", "default", "borderTopColor", "The auth card's #e5e7eb border."),
]:
    try:
        neutral[key] = {"value": norm_color(st(comp, state)[prop]), "type": "color",
                        "source": f"computed {prop} of {comp} {state} (raw/components-computed.json)",
                        "description": desc}
    except KeyError:
        pass

# the legacy --old-swatches--* set still declared on :root (the previous
# design's palette; nothing measured paints it)
legacy = SPEC["core"].setdefault("color", {}).setdefault("legacy", {})
for key, vn, desc in [
    ("navy", "--old-swatches--black", "The legacy #160647 dark navy."),
    ("accent", "--old-swatches--accent", "The legacy #47beb9 teal accent."),
    ("purple", "--old-swatches--color-2", "The legacy #6122e8 purple."),
    ("slate", "--old-swatches--dark-slate-blue", "The legacy #30187b slate purple."),
]:
    if vn in R:
        legacy[key] = var(vn, "color",
                          source=f"css-var {vn} resolved light (raw/css-vars.json)",
                          description=desc + " Declared under --old-swatches--* on :root but not measured anywhere on the captured surface — kept as provenance, not a design value.")

# -------------------------------------------------------------------- roles

light = SPEC["light"]
ALIAS = "role alias over the core palette"
for name, target, desc in [
    ("--text-primary", "color.neutral.ink", "Display and body ink on light."),
    ("--text-nav", "color.neutral.nav-ink", "The #222222 nav/menu ink."),
    ("--text-muted", "color.neutral.muted", "Declared muted gray."),
    ("--text-lede", "color.neutral.lede", "The slate lede under the hero."),
    ("--text-fine", "color.neutral.faq-text", "FAQ answers and fine print."),
    ("--surface-page", "color.neutral.white", "The white page field."),
    ("--surface-card", "color.neutral.white", "Plan cards, the mega-menu panel, blog cards."),
    ("--surface-field", "color.neutral.field", "The #f6fafb field fill."),
    ("--surface-banner", "color.neutral.ink", "The #171717 top-banner fill."),
    ("--action-primary", "color.brand.purple", "The #693ee0 action fill."),
    ("--action-dark", "color.neutral.ink", "The black button fill (hero submit, plan CTA, Send message)."),
    ("--text-on-action", "#ffffff", "White labels on purple and black fills."),
    ("--border-default", "color.neutral.border", "The #e0e0e0 hairline."),
    ("--border-field", "color.neutral.border-field", "The #e4edf1 field border."),
    ("--border-card", "color.neutral.border-card", "The #ccd9e0 chip border."),
]:
    if target.startswith("{"):
        continue
    root_bag = target.split(".")[1] if "." in target else None
    root_key = target.split(".")[-1]
    bag = {"neutral": neutral, "brand": brand, "status": {}, "legacy": legacy}.get(root_bag)
    if bag and root_key in bag:
        emit(light, name, {"value": "{" + target + "}", "type": "color",
                           "source": ALIAS, "description": desc})
    elif root_bag is None:
        emit(light, name, {"value": target, "type": "color",
                           "source": "computed color of button/menu labels (raw/components-computed.json)",
                           "description": desc})

# the state layer: the black buttons' hover-to-purple signature
state = light.setdefault("state", {})
try:
    state["dark-hover"] = {"value": norm_color(st("plan-cta", "hover")["backgroundColor"]), "type": "color",
                           "source": "computed backgroundColor of plan-cta hover (raw/components-computed.json); hero-submit and invert-cta hover to #693ee0/#683ee4 the same way",
                           "description": "The signature state move: a black button's fill lifts to purple on hover."}
except KeyError:
    pass
try:
    state["pressed-oauth"] = {"value": norm_color(st("auth-oauth", "pressed")["backgroundColor"]), "type": "color",
                              "source": "computed backgroundColor of auth-oauth pressed (raw/components-computed.json)",
                              "description": "The 6% black wash an OAuth button takes pressed."}
except KeyError:
    pass

dark = SPEC["dark"]
# The ink/purple bands the light page paints: top banner, the deep-purple
# feature card, the inverted CTA's own band.
for name, target, desc in [
    ("--text-primary", "#ffffff", "White text on the ink banner and the deep-purple band."),
    ("--surface-page", "color.neutral.ink", "The #171717 top-banner fill."),
    ("--surface-band", "color.brand.purple-deep", "The #29007a deep-purple feature band."),
    ("--action-secondary", "#ffffff", "The white fill the inverted CTA carries on the dark band."),
    ("--text-on-action", "color.neutral.ink", "Ink labels on the white inverted fills."),
]:
    if target.startswith("{") or target.startswith("#"):
        bag_key = target.strip("{}")
        if target.startswith("{") and "." in bag_key:
            emit(dark, name, {"value": target, "type": "color", "source": ALIAS, "description": desc})
        elif target.startswith("#"):
            emit(dark, name, {"value": target, "type": "color",
                              "source": "computed colors of top-banner / platform-card / invert-cta (raw/components-computed.json)",
                              "description": desc})
    else:
        root_bag = target.split(".")[1]
        root_key = target.split(".")[-1]
        bag = {"neutral": neutral, "brand": brand}.get(root_bag)
        if bag and root_key in bag:
            emit(dark, name, {"value": "{" + target + "}", "type": "color", "source": ALIAS, "description": desc})

# ------------------------------------------------------------- type scale

type_scale = SPEC["core"].setdefault("font", {}).setdefault("size", {})
for key, comp, state, desc in [
    ("display-hero", "hero-title", "default", "The 88px hero display (home)."),
    ("display", "contact-h1", "default", "The 72px 'Got Questions?' display."),
    ("display-page", "pricing-h1", "default", "The 64px page-title display (pricing)."),
    ("h2", "section-h2", "default", "The 56px section heading."),
    ("display-mobile", "m-hero", "default", "The ~43px display at 390 wide."),
    ("card-title", "plan-card", "default", "The 32px card title (plan card)."),
    ("card-title-2", "platform-card", "default", "The 28px feature-card title."),
    ("h4", "blog-card", "default", "The 24px heading (FAQ questions, blog cards)."),
    ("body", "dd-link", "default", "The 16px body/control size."),
    ("control", "hero-sub", "default", "The 14px small text."),
    ("badge", "saving-badge", "default", "The 12px badge/meta size."),
]:
    v = ts(comp, state, "fontSize")
    if v:
        type_scale[key] = {"type": "dimension", "value": v,
                           "source": f"computed fontSize of {comp} {state} (raw/components-computed.json)",
                           "description": desc}

leading = SPEC["core"].setdefault("font", {}).setdefault("lineHeight", {})
for key, comp, state, desc in [
    ("display-hero", "hero-title", "default", "Hero display leading (88px on 88px)."),
    ("display", "contact-h1", "default", "Display leading (82px on 72px)."),
    ("h2", "section-h2", "default", "Heading leading (66px on 56px)."),
    ("card-title", "plan-card", "default", "Card-title leading (42px on 32px)."),
    ("h4", "blog-card", "default", "Heading-4 leading (33.6px on 24px)."),
    ("body", "dd-link", "default", "Body leading (24px on 16px)."),
    ("lede", "hero-sub", "default", "Lede leading (22px on 14px)."),
    ("badge", "saving-badge", "default", "Badge leading (22px on 12px)."),
]:
    v = ts(comp, state, "lineHeight")
    if v:
        leading[key] = {"type": "dimension", "value": v,
                        "source": f"computed lineHeight of {comp} {state} (raw/components-computed.json)",
                        "description": desc}

# ---------------------------------------------------------- radius, motion

radius = SPEC["core"].setdefault("radius", {})
for key, comp, state, prop, desc in [
    ("nav", "btn-nav", "default", "borderTopLeftRadius", "The 4px radius on the nav CTA and the mobile sales action."),
    ("field-auth", "auth-email", "default", "borderTopLeftRadius", "The 3.5px radius on the auth field."),
    ("button-auth", "auth-continue", "default", "borderTopLeftRadius", "The 4.5px radius on the auth buttons."),
    ("field", "name-input", "default", "borderTopLeftRadius", "The 5px radius on the contact fields."),
    ("button", "plan-cta", "default", "borderTopLeftRadius", "The 8px radius on the big CTAs (plan, inverted, Send, mobile Login)."),
    ("badge", "saving-badge", "default", "borderTopLeftRadius", "The 40px badge pill."),
    ("toggle", "plan-toggle", "default", "borderTopLeftRadius", "The 48px segmented-control pill."),
]:
    if have(comp, state, prop):
        radius[key] = {"value": st(comp, state)[prop], "type": "dimension",
                       "source": f"computed {prop} of {comp} {state} (raw/components-computed.json)",
                       "description": desc}

meas = SPEC["core"].setdefault("measured", {})
for key, comp, state, prop, ty, desc in [
    ("focus-ring-light", "btn-nav", "focus-visible", "outlineColor", "color", "The #005fcc blue keyboard ring on buttons and links (1px auto)."),
    ("focus-ring-blue", "dd-link", "focus-visible", "outlineColor", "color", "The #4d65ff blue ring on dropdown and accordion rows (2px solid)."),
    ("focus-ring-auth", "auth-continue", "focus-visible", "outlineColor", "color", "The #a396ff violet ring on the auth host (2px solid)."),
    ("nav-underline", "nav-dd-toggle", "hover", "boxShadow", "shadow", "The 0 -1px ink inset the nav triggers paint as their hover underline."),
    ("toggle-shadow", "plan-toggle", "default", "boxShadow", "shadow", "The rgba(0,0,0,0.06) 0 28 64 float under the segmented control."),
    ("flyout-shadow", "nav-dd-panel", "default", "boxShadow", "shadow", "The rgba(0,0,0,0.03) 0 40 34 drop under the mega-menu."),
    ("chip-inset", "playbook-card", "default", "boxShadow", "shadow", "The inset rgba(204,217,224,0.2) 0 -3 0 the playbook chip paints."),
]:
    try:
        s = st(comp, state)[prop]
        if prop == "boxShadow":
            layers = re.findall(r"(rgba?\([\d.,\s]+\))\s+(-?\d+(?:\.\d+)?px)\s+(-?\d+(?:\.\d+)?px)\s+(-?\d+(?:\.\d+)?px)\s+(-?\d+(?:\.\d+)?px)( inset)?", s)
            layers = [l for l in layers if l[0] != "rgba(0, 0, 0, 0)"]
            if layers:
                meas[key] = {"value": [{"color": norm_color(a), "offsetX": x, "offsetY": y, "blur": bl, "spread": sp, "inset": bool(i)} for a, x, y, bl, sp, i in layers],
                             "type": "shadow",
                             "source": f"computed boxShadow of {comp} {state} (raw/components-computed.json)",
                             "description": desc}
            continue
        if s:
            meas[key] = {"value": norm_color(s), "type": ty,
                         "source": f"computed {prop} of {comp} {state} (raw/components-computed.json)",
                         "description": desc}
    except KeyError:
        pass
# the OAuth inset ring's two steps
try:
    for key, stname, desc in [
        ("oauth-ring", "default", "The 1px 19%-black inset ring the auth OAuth buttons draw instead of a border."),
        ("oauth-ring-hover", "hover", "The ring darkens to 27% black on hover."),
    ]:
        s = st("auth-oauth", stname)["boxShadow"]
        layers = re.findall(r"(rgba?\([\d.,\s]+\))\s+(-?\d+(?:\.\d+)?px)\s+(-?\d+(?:\.\d+)?px)\s+(-?\d+(?:\.\d+)?px)\s+(-?\d+(?:\.\d+)?px)( inset)?", s)
        layers = [l for l in layers if l[0] != "rgba(0, 0, 0, 0)"]
        if layers:
            meas[key] = {"value": [{"color": norm_color(a), "offsetX": x, "offsetY": y, "blur": bl, "spread": sp, "inset": bool(i)} for a, x, y, bl, sp, i in layers],
                         "type": "shadow",
                         "source": f"computed boxShadow of auth-oauth {stname} (raw/components-computed.json)",
                         "description": desc}
except KeyError:
    pass
for key, comp, state, desc in [
    ("nav-transition", "nav-dd-toggle", "default", "The 0.4s box-shadow transition behind the nav underline."),
    ("button-transition", "hero-submit", "default", "The 0.3s border-color + background-color transition on the black buttons."),
    ("field-transition", "hero-email", "default", "The 0.2s border-color + box-shadow transition on fields."),
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

# ------------------------------------------------------------------ component

comp = SPEC["component"]
for key, cname, state, prop, desc in [
    ("header.height", "header", "default", "height", "The 88px desktop sticky nav."),
    ("header.height-mobile", "m-header", "default", "height", "The 80px mobile header."),
    ("banner.height", "top-banner", "default", "height", "The 48px promo strip."),
    ("navcta.height", "btn-nav", "default", "height", "The 47px nav CTA."),
    ("button.height", "plan-cta", "default", "height", "The 47px standard dark button (plan CTA)."),
    ("button-cta.height", "invert-cta", "default", "height", "The 63px big inverted CTA (Send message matches)."),
    ("button-submit.height", "hero-submit", "default", "height", "The 40px hero submit."),
    ("field.height", "name-input", "default", "height", "The 48px contact field."),
    ("field-hero.height", "hero-email", "default", "height", "The 42px hero email field."),
    ("field-auth.height", "auth-email", "default", "height", "The 38px auth field."),
    ("toggle.height", "plan-toggle", "default", "height", "The 56px segmented control."),
    ("badge.height", "saving-badge", "default", "height", "The 24px SAVING badge."),
    ("burger.height", "m-menu-button", "default", "height", "The 46px circled burger."),
    ("menurow.height", "m-nav-item", "default", "height", "The 89px mobile-menu accordion row."),
    ("menuoverlay.height", "m-menu-open", "default", "height", "The mobile menu overlay — full 844px viewport height."),
    ("megapanel.height", "nav-dd-panel", "default", "height", "The 389px mega-menu panel."),
    ("plancard.height", "plan-card", "default", "height", "The ~595px plan card."),
    ("faqrow.height", "faq-item", "default", "height", "The 82px FAQ accordion row."),
    ("authcard.height", "auth-card", "default", "height", "The ~284px auth card."),
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
