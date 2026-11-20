#!/usr/bin/env python3
"""Write raw/component-tokens.json, the token spec build_tokens.py reads.

editorx.com is a redirect shell for Wix Studio: every path 301s to
wix.com/studio except /pricing, which still serves a Wix plans page on the
domain itself. The surface is a thunderbolt build whose inline styles declare
the site theme layer — --color_0..65 (the studio palette), --font_0..10 (the
spx-scaled site fonts) and the --wst-* semantic set (action/text/fill/button
roles) — all resolved once in raw/css-vars.json. Those become {"var": ...}
leaves resolved by build_tokens.py. Everything else is **measured computed
values** from raw/components-computed.json:

  neutrals    #000 ink (all text on the marketing surface), #000624 plan ink,
              white surfaces, the #eeeeee/#c7c7c7/#8d8d8d shade ramp, the
              #0e0e0e near-black chrome (the footer) with #f6f6f6
              text and #828282 muted, hairlines #d8e2ec / #dfe5eb
  brand       the Wix Studio purple #3910ed measured off the real actions
              (header Start Creating, hero "Start creating" pill), the lime
              #deff00 closing band, the declared #1a6aff thunderbolt action
              blue, and the #116dff link blue on the pricing error pane
  states      menu links and CTAs take #3910ed or the family-700 weight on
              hover; footer links dim to #828282; focus-visible draws a
              double box-shadow ring — white 2px + #116dff 4px on content
              controls, #000 1px + 3px in the header, #828282 in the footer
  font        Madefor throughout, under five @font-face names: the marketing
              chrome uses Madefor-Display / Madefor-Text, the thunderbolt
              content wix-madefor-display-v2 / wix-madefor-text-v2, and the
              plans page plain Madefor
  ramp        measured 157.5px studio display, 80.25/88.27 hero, 75/72.6/61/
              60 page displays, 54 and 48 section headings, 34.5/38 mobile
              hero, 32/36 plans h1, 24/31 faq question, 23.25/32.55 hero-cta
              label, 18 ledes and menu links, 16 nav/body/controls, 14/20
              footer meta, 12/19 card meta, 10/24 plan badge
  shape       sharp 0px corners are the default; the pills are stadiums —
              1123.88px computed (hero CTA), 50px (section links, enterprise
              CTA), 21px (template card action), 2px on the template card,
              50% circles for the footer social buttons

A leaf is {"var": ...} (resolved light) or {"value": ..., "source": ...} for a
measured value. Only the signed-out public surface was read; the "dark" set is
the near-black chrome (the footer) the light page paints — not a
user-selectable theme.
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
    "The token tree build_tokens.py turns into tokens.json. editorx.com "
    "redirects to wix.com/studio: a thunderbolt build whose inline theme "
    "layer (--color_*, --wst-*, --font_*; raw/css-vars.json) is var-"
    "referenced where it declares the studio palette and site fonts, and "
    "measured computed values (raw/components-computed.json) cover the "
    "Wix Studio purple #3910ed and lime #deff00 actions, the ink/white "
    "neutrals and #0e0e0e chrome, the double focus rings, Madefor under "
    "its five face names, the stadium pills and the spx-scaled display "
    "ramp. The 'dark' set is the near-black footer chrome "
    "the light page paints — not a user toggle."),
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


def paint(comp, state, key, match=None):
    """A painted-layer value inside a component (fill, border, radius...)."""
    for n in C[comp]["states"][state].get("paint") or []:
        v = n.get(key)
        if v and (match is None or match in str(v)):
            return v
    return None


def ancestor(comp, state, key):
    for a in C[comp]["states"][state].get("ancestors") or []:
        if a.get(key):
            return a[key]
    return None


# ------------------------------------------------------------------- fonts

fam = SPEC["core"].setdefault("font", {}).setdefault("family", {})
for key, comp, desc in [
    ("display", "hero-title", "The thunderbolt display face, served as wix-madefor-display-v2 (Madefor Display)."),
    ("text", "faq-question", "The thunderbolt text face, served as wix-madefor-text-v2 (Madefor Text)."),
    ("chrome-display", "nav-trigger", "The marketing chrome's display face, served as Madefor-Display."),
    ("chrome-text", "nav-cta", "The marketing chrome's text face, served as Madefor-Text."),
    ("plans", "plans-h1", "The plans page's face, served as plain Madefor."),
]:
    v = ts(comp, "default", "fontFamily")
    if v:
        fam[key] = {"value": v, "type": "fontFamily",
                    "source": f"computed fontFamily of {comp} default text (raw/components-computed.json); the @font-face blocks are served from static.parastorage.com (raw/css-vars.json fonts)",
                    "description": desc}

weights = SPEC["core"].setdefault("font", {}).setdefault("weight", {})
for key, comp, state, desc in [
    ("regular", "hero-sub", "default", "Body and display weight (400)."),
    ("medium", "faq-question", "default", "The 500 weight on FAQ questions and plan labels."),
    ("mediumbold", "template-card", "default", "The 530 variable weight the wds buttons paint."),
    ("bold", "plans-h1", "default", "The 700 weight on plan headings, badges and menu links."),
]:
    v = ts(comp, state, "fontWeight")
    if v:
        weights[key] = {"value": int(float(v)), "type": "fontWeight",
                        "source": f"computed fontWeight of {comp} {state} (raw/components-computed.json)",
                        "description": desc}

# ------------------------------------------------------- declared colours
# The thunderbolt site theme: --color_* is the raw palette, --wst-* the
# semantic layer. Var-referenced where a variable resolves the same value.

brand = SPEC["core"].setdefault("color", {}).setdefault("brand", {})
for key, comp, state, prop, desc in [
    ("studio-purple", "nav-cta", "default", "backgroundColor",
     "The Wix Studio purple #3910ed: the header Start Creating and the hero 'Start creating' pill."),
    ("lime", "cta-band", "default", "backgroundColor",
     "The Wix Studio lime #deff00 the closing CTA band paints."),
    ("link", "pricing-refresh", "default", "color",
     "The #116dff link blue (the pricing error pane's Refresh)."),
    ("link-hover", "pricing-refresh", "hover", "color",
     "The #0f62e6 hover step on the link blue."),
]:
    try:
        measured = norm_color(st(comp, state)[prop])
        leaf_ = {"type": "color",
                 "source": f"computed {prop} of {comp} {state} (raw/components-computed.json)",
                 "description": desc}
        leaf_["value"] = measured
        brand[key] = leaf_
    except KeyError:
        pass

for key, vn, desc in [
    ("studio-blue", "--wst-color-action", "The declared thunderbolt action blue #1a6aff (--color_18; the --wst-* action/fill/button roles all resolve to it)."),
    ("blue-100", "--color_16", "The declared lightest blue #dce8ff."),
    ("blue-200", "--color_17", "The declared mid light blue #95b9ff."),
    ("blue-700", "--color_19", "The declared deep blue #094bcc."),
    ("lime-deep", "--color_22", "The declared lime variant #deff06 in the site palette."),
    ("lime-100", "--color_20", "The declared pale lime #dbff81."),
    ("lime-tint", "--color_21", "The declared lime-tinted surface #f3f8f0."),
    ("olive-300", "--color_23", "The declared olive #92b079."),
    ("olive-500", "--color_24", "The declared olive #618741."),
    ("olive-700", "--color_25", "The declared deep olive #39641d."),
    ("clay-100", "--color_26", "The declared pale clay #f2eae7."),
    ("clay-200", "--color_27", "The declared clay #e5cec0."),
    ("clay-400", "--color_28", "The declared clay #a9806f."),
    ("clay-600", "--color_29", "The declared clay #8b614f."),
    ("clay-800", "--color_30", "The declared deep clay #633c2b."),
    ("orange-100", "--color_31", "The declared pale orange #ffe9df."),
    ("orange-200", "--color_32", "The declared light orange #ffbfa1."),
    ("orange-400", "--color_33", "The declared orange #fa854f."),
    ("orange-500", "--color_34", "The declared orange #ea6020."),
    ("orange-700", "--color_35", "The declared deep orange #c94001."),
]:
    if vn in R:
        brand[key] = var(vn, "color",
                         source=f"css-var {vn} resolved light (raw/css-vars.json)",
                         description=desc)

status = SPEC["core"].setdefault("color", {}).setdefault("status", {})
for key, vn, desc in [
    ("error", "--color_3", "The declared error red #ed1c24 in the site palette."),
    ("info", "--color_4", "The declared info blue #0088cb."),
    ("warning", "--color_5", "The declared warning yellow #ffcb05."),
    ("disabled", "--wst-color-disabled", "The declared disabled grey #c7c7c7."),
]:
    if vn in R:
        status[key] = var(vn, "color",
                          source=f"css-var {vn} resolved light (raw/css-vars.json)",
                          description=desc)

# measured + declared neutrals
neutral = SPEC["core"].setdefault("color", {}).setdefault("neutral", {})
for key, comp, state, prop, desc in [
    ("ink", "hero-title", "default", "ts-color", "The #000 ink: nearly all text on the marketing surface."),
    ("ink-plans", "plans-h1", "default", "ts-color", "The #000624 near-black the plans page paints."),
    ("white", "plan-card", "default", "backgroundColor", "The #ffffff surface: page field, plan cards, template cards."),
    ("footer-ink", "footer-link", "default", "color", "The #f6f6f6 text the dark chrome paints."),
    ("footer-muted", "footer-link", "hover", "color", "The #828282 muted/hover text on the dark chrome."),
    ("hairline", "nav-dropdown", "default", "paint-border", "The #d8e2ec hairline under the opened mega-menu."),
    ("card-line", "plan-card", "default", "paint-border-side", "The #dfe5eb 1px border the plan cards carry on three sides."),
    ("navy", "plan-card", "default", "borderTopColor", "The #0e106a 3px accent border on the recommended plan card's top edge."),
    ("badge-mint", "plan-badge", "default", "paint-bg", "The #a6ffd8 mint the RECOMMENDED badge paints."),
    ("surface-dark", "footer", "default", "paint-bg", "The #0e0e0e near-black chrome: the footer."),
    ("footer-divider", "footer", "default", "paint-shadow", "The #848280 1px rule inside the dark footer."),
]:
    try:
        if prop == "ts-color":
            v = norm_color(ts(comp, state, "color"))
        elif prop == "paint-border":
            hit = paint(comp, state, "border", "1px solid")
            v = norm_color(re.search(r"rgba?\([\d.,\s]+\)|#[0-9a-fA-F]+", hit).group(0)) if hit else None
        elif prop == "paint-border-side":
            hit = paint(comp, state, "border", "R:")
            m = re.search(r"R:1px solid (rgba?\([\d.,\s]+\))", hit or "")
            v = norm_color(m.group(1)) if m else None
        elif prop == "paint-bg":
            v = norm_color(paint(comp, state, "bg"))
        elif prop == "paint-shadow":
            hit = paint(comp, state, "shadow")
            v = norm_color(re.search(r"rgba?\([\d.,\s]+\)", hit).group(0)) if hit else None
        else:
            v = norm_color(st(comp, state).get(prop, ""))
        if v:
            neutral[key] = {"value": v, "type": "color",
                            "source": f"computed {prop} of {comp} {state} (raw/components-computed.json)",
                            "description": desc}
    except KeyError:
        pass

for key, vn, desc in [
    ("shade-1", "--wst-color-fill-base-shade-1", "The declared lightest shade #eeeeee."),
    ("shade-2", "--wst-color-fill-base-shade-2", "The declared mid shade #c7c7c7."),
    ("shade-3", "--wst-color-fill-base-shade-3", "The declared deep shade #8d8d8d — also the --wst-* secondary text."),
    ("grey-600", "--color_6", "The declared #727272 grey in the site palette."),
]:
    if vn in R:
        neutral[key] = var(vn, "color",
                           source=f"css-var {vn} resolved light (raw/css-vars.json)",
                           description=desc)

# -------------------------------------------------------------------- roles

light = SPEC["light"]
ALIAS = "role alias over the core palette"
for name, target, desc in [
    ("--text-primary", "color.neutral.ink", "Body and display ink on light."),
    ("--text-muted", "color.neutral.shade-3", "Secondary text on light (the declared --wst-* secondary)."),
    ("--text-on-dark", "color.neutral.footer-ink", "The #f6f6f6 text on the #0e0e0e chrome."),
    ("--surface-page", "color.neutral.white", "The white page field."),
    ("--surface-tint", "color.neutral.shade-1", "The declared #eeeeee secondary fill."),
    ("--surface-dark", "color.neutral.surface-dark", "The #0e0e0e footer chrome on the light page."),
    ("--surface-accent", "color.brand.lime", "The lime closing band."),
    ("--surface-badge", "color.neutral.badge-mint", "The mint RECOMMENDED badge."),
    ("--action-primary", "color.brand.studio-purple", "The #3910ed action fill."),
    ("--action-secondary", "color.neutral.ink", "The black pill fill the section links / enterprise CTA carry."),
    ("--action-link", "color.brand.link", "The #116dff link blue."),
    ("--action-link-hover", "color.brand.link-hover", "The #0f62e6 link hover."),
    ("--text-on-action", "#ffffff", "White labels on the purple and black fills."),
    ("--text-hover-accent", "color.brand.studio-purple", "The #3910ed a menu link takes on hover."),
    ("--border-hairline", "color.neutral.hairline", "The #d8e2ec hairline (mega-menu, page rules)."),
    ("--border-card", "color.neutral.card-line", "The #dfe5eb card border."),
    ("--border-accent", "color.neutral.navy", "The #0e106a top accent on the recommended plan card."),
]:
    root_bag = target.split(".")[1] if "." in target else None
    root_key = target.split(".")[-1]
    bag = {"neutral": neutral, "brand": brand, "status": status}.get(root_bag)
    if bag and root_key in bag:
        emit(light, name, {"value": "{" + target + "}", "type": "color",
                           "source": ALIAS, "description": desc})
    elif root_bag is None:  # --text-on-action: the header action's label ink, read
        emit(light, name, {"value": norm_color(st("nav-cta", "default")["color"]), "type": "color",
                           "source": "computed color of nav-cta default (raw/components-computed.json)",
                           "description": desc})

dark = SPEC["dark"]
# The near-black chrome (the footer) the light page paints.
for name, target, desc in [
    ("--text-primary", "{color.neutral.footer-ink}", "The #f6f6f6 text on the dark chrome."),
    ("--text-muted", "{color.neutral.footer-muted}", "The #828282 muted/hover text on dark."),
    ("--surface-page", "{color.neutral.surface-dark}", "The #0e0e0e chrome surface."),
    ("--border", "{color.neutral.footer-ink}", "The 1px #f6f6f6 ring the footer's 50%-radius social buttons carry."),
    ("--border-divider", "{color.neutral.footer-divider}", "The #848280 hairline inside the footer."),
    ("--action-primary", "{color.brand.studio-purple}", "The #3910ed action fill; the dark footer carries no action of its own, the role is kept for completeness."),
    ("--text-on-action", None, "White labels on the action fill; the dark footer carries no action, so this is the header action's label ink."),
]:
    if target is None:
        emit(dark, name, {"value": norm_color(st("nav-cta", "default")["color"]), "type": "color",
                          "source": "computed color of nav-cta default (raw/components-computed.json)",
                          "description": desc})
        continue
    emit(dark, name, {"value": target, "type": "color", "source": ALIAS, "description": desc})

# ------------------------------------------------------------- type scale

type_scale = SPEC["core"].setdefault("font", {}).setdefault("size", {})
for key, comp, state, desc in [
    ("display-max", "design-h1", "default", "The 157.5px studio display (/studio/design; spx-scaled, so viewport-dependent)."),
    ("display-hero", "hero-title", "default", "The 80.25px home hero display."),
    ("display-page", "academy-h1", "default", "The 75px page display (/studio/academy)."),
    ("display-2", "inspo-h1", "default", "The 72.57px gallery display (/studio/inspiration)."),
    ("display-3", "feat-h1", "default", "The 60.9px features display."),
    ("display-4", "ent-h1", "default", "The 60px enterprise display."),
    ("h2", "section-h2", "default", "The 54px home section heading."),
    ("h2-2", "design-h2", "default", "The 48px /studio/design section heading."),
    ("display-mobile", "m-hero", "default", "The 34.5px hero display at 390 wide."),
    ("h3", "plans-h1", "default", "The 32px plans heading (700)."),
    ("card-title", "academy-card", "default", "The 26.6px academy card title."),
    ("question", "faq-question", "default", "The 24px FAQ question (500)."),
    ("cta-label", "hero-cta", "default", "The 23.25px hero-pill label."),
    ("filter", "inspo-filter", "default", "The 20px gallery filter label."),
    ("lede", "hero-sub", "default", "The 18px hero lede."),
    ("menu", "menu-link", "default", "The 18px mega-menu link (700)."),
    ("body", "nav-link", "default", "The 16px nav/body/control size."),
    ("card-action", "template-card", "default", "The 16px card action (530)."),
    ("footer-meta", "footer", "default", "The 14px footer meta text."),
    ("link", "pricing-support", "default", "The 14px inline link text."),
    ("meta", "inspo-card", "default", "The 12px card meta text."),
    ("badge", "plan-badge", "default", "The 10px plan badge label (700)."),
]:
    v = ts(comp, state, "fontSize")
    if v:
        type_scale[key] = {"type": "dimension", "value": v,
                           "source": f"computed fontSize of {comp} {state} (raw/components-computed.json)",
                           "description": desc}

leading = SPEC["core"].setdefault("font", {}).setdefault("lineHeight", {})
for key, comp, state, desc in [
    ("display-max", "design-h1", "default", "Display leading (157.5px, 1.0)."),
    ("display-hero", "hero-title", "default", "Hero leading (88.27px on 80.25px)."),
    ("display-page", "academy-h1", "default", "Page-display leading (75px, 1.0)."),
    ("h2", "section-h2", "default", "Section heading leading (54px, 1.0)."),
    ("display-mobile", "m-hero", "default", "Mobile hero leading (37.98px on 34.53px)."),
    ("h3", "plans-h1", "default", "Plans heading leading (36px on 32px)."),
    ("question", "faq-question", "default", "FAQ question leading (31.2px on 24px)."),
    ("cta-label", "hero-cta", "default", "Hero-pill label leading (32.55px on 23.25px)."),
    ("lede", "hero-sub", "default", "Lede leading (28.8px on 18px)."),
    ("card-action", "template-card", "default", "Card action leading (24px on 16px)."),
    ("footer-link", "footer-link", "default", "Footer link leading (34px on 16px)."),
    ("footer-meta", "footer", "default", "Footer meta leading (20px on 14px)."),
    ("link", "pricing-support", "default", "Link leading (18px on 14px)."),
    ("meta", "inspo-card", "default", "Card meta leading (19.2px on 12px)."),
    ("badge", "plan-badge", "default", "Badge leading (24px on 10px)."),
]:
    v = ts(comp, state, "lineHeight")
    if v and v != "normal":
        leading[key] = {"type": "dimension", "value": v,
                        "source": f"computed lineHeight of {comp} {state} (raw/components-computed.json)",
                        "description": desc}

tracking = SPEC["core"].setdefault("font", {}).setdefault("letterSpacing", {})
for key, comp, state, desc in [
    ("display", "hero-title", "default", "The -2.4px (~-0.03em) tracking the display faces carry."),
    ("question", "faq-question", "default", "The -0.48px (~-0.02em) tracking on FAQ questions."),
    ("mobile", "m-hero", "default", "The -0.35px (~-0.01em) tracking at 390 wide."),
]:
    v = ts(comp, state, "letterSpacing")
    if v and v != "normal":
        tracking[key] = {"type": "dimension", "value": v,
                         "source": f"computed letterSpacing of {comp} {state} (raw/components-computed.json)",
                         "description": desc}

# ---------------------------------------------------------- radius, spacing

radius = SPEC["core"].setdefault("radius", {})
for key, comp, state, prop, desc in [
    ("stadium", "hero-cta", "default", "borderTopLeftRadius", "The stadium pill on the hero CTA (the computed cap reads 1123.88px; the ends are semicircles)."),
    ("pill", "section-link", "default", "borderTopLeftRadius", "The 50px pill on section links and the enterprise CTA."),
    ("card", "template-card", "default", "borderTopLeftRadius", "The 2px radius on template cards."),
    ("none", "nav-cta", "default", "borderTopLeftRadius", "The sharp 0px default: header CTA, plan cards, bands — corners stay square."),
]:
    if have(comp, state, prop):
        radius[key] = {"value": st(comp, state)[prop], "type": "dimension",
                       "source": f"computed {prop} of {comp} {state} (raw/components-computed.json)",
                       "description": desc}
inner_r = paint("template-card", "default", "radius", "21px")
if inner_r:
    radius["button-card"] = {"value": "21px", "type": "dimension",
                             "source": "painted layer radius inside template-card (raw/components-computed.json)",
                             "description": "The 21px radius on the template card's white action button."}
social_r = paint("footer", "default", "radius", "50%")
if social_r:
    radius["circle"] = {"value": "9999px", "type": "dimension",
                        "source": "painted layer radius '50%' on the footer's social buttons (raw/components-computed.json); exported as a full circle",
                        "description": "The 50% circle on the footer's social buttons (36px)."}

spacing = SPEC["core"].setdefault("spacing", {})
for key, comp, state, prop, desc in [
    ("card-pad", "template-card", "default", "paddingTop", "The 12px card padding."),
    ("control-pad-y", "m-nav-item", "default", "paddingTop", "The 15px vertical padding on nav rows and mobile menu items."),
    ("control-pad-r", "section-link", "default", "paddingRight", "The 22px trailing padding before a link's arrow."),
    ("menu-pad-x", "m-nav-item", "default", "paddingLeft", "The ~27px horizontal gutter at 390 wide."),
    ("cta-pad-x", "nav-cta", "default", "paddingLeft", "The 35px horizontal padding on the header CTA."),
    ("dropdown-pad-y", "nav-dropdown", "default", "paddingTop", "The 47px top padding inside the mega-menu."),
    ("dropdown-pad-b", "nav-dropdown", "default", "paddingBottom", "The 66px bottom padding inside the mega-menu."),
    ("dropdown-pad-x", "nav-dropdown", "default", "paddingRight", "The 72-100px horizontal padding inside the mega-menu."),
]:
    if have(comp, state, prop):
        spacing[key] = {"value": st(comp, state)[prop], "type": "dimension",
                        "source": f"computed {prop} of {comp} {state} (raw/components-computed.json)",
                        "description": desc}

# ------------------------------------------------------------- measured extras

meas = SPEC["core"].setdefault("measured", {})
for key, comp, state, prop, ty, desc in [
    ("focus-ring-content", "hero-cta", "focus-visible", "boxShadow", "shadow", "The double keyboard ring on content controls: 2px white + 4px #116dff."),
    ("focus-ring-chrome", "nav-link", "focus-visible", "boxShadow", "shadow", "The double keyboard ring in the header: 1px + 3px black."),
    ("focus-ring-footer", "footer-link", "focus-visible", "boxShadow", "shadow", "The double keyboard ring on the dark chrome: 1px + 3px #828282."),
    ("focus-ring-auto", "pricing-support", "focus-visible", "outlineColor", "color", "The #005fcc auto outline the link-blue controls take (1px)."),
    ("focus-ring-link", "pricing-refresh", "focus-visible", "outlineColor", "color", "The 3px solid #116dff outline the standalone Refresh link takes on focus."),
]:
    try:
        if prop == "boxShadow":
            s = st(comp, state)[prop]
            layers = re.findall(r"(rgba?\([\d.,\s]+\))\s+(-?\d+(?:\.\d+)?px)\s+(-?\d+(?:\.\d+)?px)\s+(-?\d+(?:\.\d+)?px)\s+(-?\d+(?:\.\d+)?px)( inset)?", s)
            layers = [l for l in layers if l[0] != "rgba(0, 0, 0, 0)"]
            if layers:
                meas[key] = {"value": [{"color": norm_color(a), "offsetX": x, "offsetY": y, "blur": bl, "spread": sp, "inset": bool(i)} for a, x, y, bl, sp, i in layers],
                             "type": "shadow",
                             "source": f"computed boxShadow of {comp} {state} (raw/components-computed.json)",
                             "description": desc}
            continue
        if have(comp, state, prop):
            meas[key] = {"value": norm_color(st(comp, state)[prop]), "type": ty,
                         "source": f"computed {prop} of {comp} {state} (raw/components-computed.json)",
                         "description": desc}
    except KeyError:
        pass

# the recommended plan card's elevation (read off its badge's ancestor)
plancard_shadow = ancestor("plan-badge", "default", "shadow")
if plancard_shadow:
    layers = re.findall(r"(rgba?\([\d.,\s]+\))\s+(-?\d+(?:\.\d+)?px)\s+(-?\d+(?:\.\d+)?px)\s+(-?\d+(?:\.\d+)?px)\s+(-?\d+(?:\.\d+)?px)( inset)?", plancard_shadow)
    if layers:
        meas["card-elevation"] = {"value": [{"color": norm_color(a), "offsetX": x, "offsetY": y, "blur": bl, "spread": sp, "inset": bool(i)} for a, x, y, bl, sp, i in layers],
                                  "type": "shadow",
                                  "source": "ancestor boxShadow of plan-badge (raw/components-computed.json): the recommended plan card's elevation",
                                  "description": "The plan card's soft elevation: 6px/5% and 18px/10% ink-plans washes."}

for key, comp, state, desc in [
    ("transition-cta", "nav-cta", "default", "The 0.4s ease colour transition the CTAs run (color, background-color)."),
    ("transition-control", "ent-cta", "default", "The 0.2s ease control transition (all)."),
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
    ("button-cta.height", "nav-cta", "default", "height", "The 57px header CTA height."),
    ("button-pill.height", "hero-cta", "default", "height", "The ~56px hero 'Start creating' pill."),
    ("button-secondary.height", "ent-cta", "default", "height", "The 52px enterprise/secondary pill."),
    ("link-pill.height", "section-link", "default", "height", "The 32px section-link pill."),
    ("filter.height", "inspo-filter", "default", "height", "The 32px gallery filter chip."),
    ("header.height", "nav-bar", "default", "height", "The 56px desktop header."),
    ("header-mobile.height", "m-header", "default", "height", "The 47px mobile header."),
    ("menurow.height", "m-nav-item", "default", "height", "The 50px mobile-menu row."),
    ("menubutton.height", "m-menu-button", "default", "height", "The 46px mobile menu button (50px wide)."),
    ("footer.height", "footer", "default", "height", "The 793px dark footer."),
    ("dropdown.height", "nav-dropdown", "default", "height", "The ~400-510px mega-menu panel."),
    ("plancard.height", "plan-card", "default", "height", "The 574px plan card."),
    ("plancard.width", "plan-card", "default", "width", "The ~202px plan card column."),
    ("templatecard.height", "template-card", "default", "height", "The ~395px template card."),
    ("faqrow.height", "faq-question", "default", "height", "The ~131px FAQ row, closed."),
    ("ctaband.height", "cta-band", "default", "height", "The 171px lime closing band."),
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
