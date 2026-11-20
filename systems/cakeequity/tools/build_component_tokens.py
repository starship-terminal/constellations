#!/usr/bin/env python3
"""Write raw/component-tokens.json, the token spec build_tokens.py reads.

cakeequity.com is a Webflow marketing site (the cakester.shared.* bundle) that
declares a real design-token layer — the --blackberry-*/--plum-*/--berry-*/
--lemon-*/--lime-*/--tangerine-* custom properties harvested into
raw/css-vars.json (tools/capture/vars.mjs): a near-black ink family, a six-step
plum accent ramp, four bright secondary ramps and the alpha steps of each.
Those become {"var": ...} leaves. The bundle also ships ~30
``<deleted|variable-…>`` names — vestigial variables from vendored component
libraries (untitled-ui, alley, elements-webflow, flowstica, waves) that no live
rule still needs; they are recorded in raw/css-vars.json but not tokenised.

What the declared layer does not name is measured from
raw/components-computed.json:

  ink         #18161a headings/nav ink, the white page field, #ececf0 grey
              fields, #fafaf8 warm-white declared but rarely painted
  plum        #4823ff button fills and link hover, #2b1599 pressed/hover,
              #ede9ff most-popular pill, rgba(126,120,255,0.1) menu hover
  surfaces    #0e0d12 the single dark band (Cake MCP section), #faf9ff the
              plan-card header, #c6f0dc the save-pill, #ebe8f2 chip borders,
              #d9d9e0 field borders -> #3898ec on focus
  auth        the Kinde hosted-login card: #5a38fd primary, #f5f5f5 oauth,
              #1c029d links, #0054f0 2px focus ring — a second, older palette
  dark        the footer's #18161a field and the #0e0d12 band paint the site's
              two dark surfaces: white text, #7e78ff link hover, rgba(244,244,
              244,0.18) hairlines, #e7ff6e eyebrows — a dark set, not a theme
  type        Exposure Light display 60/66 -2px (52/57.2 at 390), h2 44/44 -1,
              Inter body 16, lede 20/32 300, nav 14, eyebrow 16 caps 600,
              badge 13, price 40, Kinde's own 24/16 auth scale
  shape       100px/999px pills everywhere, 20px cards and dropdowns, 28px the
              dark band, 16px story/auth cards, 8px Kinde controls
  motion      0.2s all on buttons, 0.4s on the ghost CTA, 0.3s transform on
              the FAQ card, 0.15s on Kinde, 0.5s the mega-nav grid
  states      the 1px auto outline #005fcc focus ring (the Webflow/UA ring),
              plum-dark hover fills, plum-10 menu wash, rgba(0,0,0,0.2)
              0 2px 10px -8px the opened FAQ card draws

A leaf is {"var": "--name"} (resolved per theme by build_tokens.py) or
{"value": ..., "source": "..."} for a measured value. The site is light-only —
no stylesheet binds a dark theme — but two dark surfaces are painted on the
page, so the dark set holds their roles.
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
    "The token tree build_tokens.py turns into tokens.json. cakeequity.com "
    "declares a --blackberry/--plum/--berry/--lemon/--lime/--tangerine "
    "design-token layer in its Webflow bundle (raw/css-vars.json); the light "
    "set is built from those declared variables plus measured computed "
    "styles, and the dark set from measured computed styles on the page's "
    "two dark surfaces — the #18161a footer and the #0e0d12 Cake-MCP band "
    "(raw/components-computed.json)."),
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


def paint_node(comp, state, needle):
    """The paint-layer entry whose node name contains needle."""
    try:
        for n in C[comp]["states"][state].get("paint") or []:
            if needle in n.get("node", ""):
                return n
    except KeyError:
        pass
    return None


# ------------------------------------------------------------------- fonts

fam = SPEC["core"].setdefault("font", {}).setdefault("family", {})
for key, comp, state, desc in [
    ("display", "hero-title", "default",
     "The display serif face (Exposure Light first) on every h1/h2 — served from the Webflow CDN, falls back to Times New Roman."),
    ("body", "nav-link", "default",
     "The UI/body stack (Inter first) on nav, buttons, copy and cards — served alongside Exposure."),
    ("auth", "login-card", "default",
     "The Kinde hosted-auth stack (Inter, then system-ui) — a different, older toolchain than the marketing pages."),
]:
    if have(comp, state, "fontFamily"):
        fam[key] = {"value": st(comp, state)["fontFamily"], "type": "fontFamily",
                    "source": f"computed fontFamily of {comp} {state} (raw/components-computed.json)",
                    "description": desc}
# Faces the bundle serves (@font-face in raw/css-vars.json) that nothing on the
# measured components painted — declared evidence, marked as such.
for key, face, desc in [
    ("served-display-bold", "Exposure Bold",
     "Served @font-face (plus italic) in the Webflow bundle; not painted on any measured component on this pass."),
    ("served-youth", "Youth",
     "Served @font-face in the Webflow bundle; not painted on any measured component on this pass."),
    ("served-cabinet", "Cabinetgrotesk",
     "Served @font-face in the Webflow bundle; not painted on any measured component on this pass."),
    ("served-mono", "Inconsolata",
     "Served via fonts.googleapis.com (the mono face); not painted on any measured component on this pass."),
    ("served-jakarta", "Plus Jakarta Sans",
     "Served via fonts.googleapis.com; not painted on any measured component on this pass."),
]:
    if any(f.get("font-family", "").strip('"').lower() == face.lower() for f in V.get("fonts", [])):
        fam[key] = {"value": face, "type": "fontFamily",
                    "source": "@font-face declaration in the served stylesheets (raw/css-vars.json fonts); declared, not observed painting",
                    "description": desc}

# ------------------------------------------------------- declared colours

ink = SPEC["core"].setdefault("color", {}).setdefault("ink", {})
for key, vname, desc in [
    ("100", "--blackberry--100", "The near-black ink #18161a: headings, hero text, the footer field and the billing toggle's active pill."),
    ("75", "--blackberry--75", "The 75% ink alpha."),
    ("50", "--blackberry--50", "The 50% ink alpha — the muted eyebrow and secondary copy tone."),
    ("25", "--blackberry--25", "The 25% ink alpha."),
    ("10", "--blackberry--10", "The 10% ink hairline under FAQ cards, plan-card headers and pricing rows."),
]:
    if vname in R:
        ink[key] = var(vname, "color", description=desc)

neutral = SPEC["core"].setdefault("color", {}).setdefault("neutral", {})
for key, vname, desc in [
    ("white", "--white", "The page field and card fill."),
    ("warm-white", "--warm-white", "The declared warm white #fafaf8 (sections that opt into it; the page itself paints pure white)."),
    ("grey", "--grey", "The light grey #ececf0 field of tinted sections and pills."),
    ("dark-grey", "--dark-grey", "The declared navy-leaning #161640."),
    ("black", "--black", "The declared black, the same #18161a as blackberry--100."),
    ("white-50", "--50-white", "Half-alpha white for muted text on dark surfaces."),
    ("white-25", "--25-white", "Quarter-alpha white."),
    ("white-90", "--90-white", "The 70% #fafafa white."),
    ("grey-50", "--50-grey", "Half-alpha #ececf0."),
]:
    if vname in R:
        neutral[key] = var(vname, "color", description=desc)

plum = SPEC["core"].setdefault("color", {}).setdefault("plum", {})
for key, vname, desc in [
    ("bright", "--plum--bright-plum", "The brand violet #4823ff: every primary button fill, link hover and icon accent."),
    ("dark", "--plum--dark-plum", "The pressed/hover violet #2b1599 every primary control darkens to."),
    ("new", "--plum--new-plum", "The declared mid violet #6d67fb."),
    ("100", "--plum--100", "The declared plum #7e78ff: footer-link hover, FAQ +/- icon bars, the top nav accent line."),
    ("light", "--plum--light-plum", "The declared light plum #b2aeff."),
    ("lighter", "--plum--lighter-plum", "The #ede9ff most-popular-pill and tint fill."),
    ("lightest", "--plum--lightest-plum", "The #f5f4fb plum-tinted section field."),
    ("contrast", "--plum--contrast", "The declared magenta-plum #932a74 accent."),
    ("5", "--plum--5", "The 5% plum wash."),
    ("10", "--plum--10", "The 10% plum wash a mega-nav link paints on hover."),
    ("25", "--plum--25", "The 25% plum — the featured plan card's border."),
    ("50", "--plum--50", "The 50% plum alpha."),
    ("75", "--plum--75", "The 75% plum alpha."),
]:
    if vname in R:
        plum[key] = var(vname, "color", description=desc)

for group, rows in [
    ("berry", [("100", "--berry--100", "The sky #99cefe accent."),
               ("highlight", "--berry--highlight-berry", "The strong sky #0e87d7."),
               ("light", "--berry--light-berry", "The pale sky #ebf5ff."),
               ("15", "--berry--15", "The 15% sky wash."),
               ("25", "--berry--25", "The 25% sky wash."),
               ("50", "--berry--50", "The 50% sky.")]),
    ("lemon", [("100", "--lemon--100", "The acid lemon #e7ff6e — the dark band's eyebrow and highlight text."),
               ("highlight", "--lemon--highlight-lemon", "The dark lemon #556309 (lemon on light)."),
               ("light", "--lemon--light-lemon", "The pale lemon #f6fdd1."),
               ("25", "--lemon--25", "The 25% lemon wash."),
               ("50", "--lemon--50", "The 50% lemon.")]),
    ("lime", [("100", "--lime--100", "The lime #9aff91 accent."),
              ("highlight", "--lime--highlight-lime", "The green #078f00."),
              ("go-green", "--lime--go-green", "The declared #e3f9c9 green tint."),
              ("light", "--lime--light-lime", "The pale lime #ebffe9 — the now-live pill fill."),
              ("25", "--lime--25", "The 15% lime wash (declared as --lime--25)."),
              ("50", "--lime--50", "The 50% lime.")]),
    ("tangerine", [("100", "--tangerine--100", "The tangerine #ffa360 accent."),
                   ("highlight", "--tangerine--highlight-tangerine", "The deep tangerine #e27500."),
                   ("light", "--tangerine--light-tangerine", "The pale tangerine #ffeddf."),
                   ("25", "--tangerine--25", "The 25% tangerine wash."),
                   ("50", "--tangerine--50", "The 50% tangerine.")]),
]:
    g = SPEC["core"].setdefault("color", {}).setdefault(group, {})
    for key, vname, desc in rows:
        if vname in R:
            g[key] = var(vname, "color", description=desc)

# ------------------------------------------------------- measured colours

meas_c = SPEC["core"].setdefault("color", {}).setdefault("measured", {})
for key, comp, state, prop, desc in [
    ("nav-text", "nav-link", "default", "color",
     "The rgb(34,34,34) nav-link ink — the bundle's base body colour, lighter than the #18161a heading ink."),
    ("dark-band", "dark-section", "default", "backgroundColor",
     "The #0e0d12 near-black of the Cake-MCP band — the site's darkest painted surface, darker than the footer ink."),
    ("plan-top", "plan-card", "default", "paint-bg:.pricing-card-top",
     "The #faf9ff violet-tinted header of a plan card."),
    ("save-pill", "billing-toggle", "default", "paint-bg:.save-pill-div",
     "The #c6f0dc mint of the '-20% save' pills — between the declared lime tints."),
    ("chip-border", "announce-pill", "default", "borderTopColor",
     "The #ebe8f2 border on the announcement chip."),
    ("field-border", "country-select", "default", "borderTopColor",
     "The #d9d9e0 border on the region select and the billing-toggle shell."),
    ("field-focus", "country-select", "focused", "borderTopColor",
     "The #3898ec blue the select border gains on focus."),
    ("focus", "nav-cta", "focus-visible", "outlineColor",
     "The #005fcc of the 1px auto focus ring (the Webflow/UA ring) every focused control draws."),
    ("dark-hairline", "dark-section", "default", "paint-border:.hp26-acc",
     "The rgba(244,244,244,0.18) hairline between the dark band's rows."),
]:
    try:
        if prop.startswith("paint-bg:"):
            n = paint_node(comp, state, prop.split(":", 1)[1])
            v = norm_color((n or {}).get("bg"))
        elif prop.startswith("paint-border:"):
            n = paint_node(comp, state, prop.split(":", 1)[1])
            b = (n or {}).get("border", "")
            m = re.search(r"(rgba?\([\d.,\s]+\)|#[0-9a-fA-F]{3,8})", b)
            v = norm_color(m.group(1)) if m else None
        else:
            v = norm_color(st(comp, state).get(prop, ""))
        if v and v != "transparent" and v != "rgba(0, 0, 0, 0)":
            meas_c[key] = {"value": v, "type": "color",
                           "source": f"computed {prop} of {comp} {state} (raw/components-computed.json)",
                           "description": desc}
    except KeyError:
        pass

# ------------------------------------------------------- Kinde auth colours

auth = SPEC["core"].setdefault("color", {}).setdefault("auth", {})
for key, comp, state, prop, desc in [
    ("primary", "login-cta", "default", "backgroundColor",
     "The Kinde primary #5a38fd on Continue — close to but not the marketing #4823ff."),
    ("oauth", "login-oauth", "default", "backgroundColor",
     "The #f5f5f5 OAuth-button fill."),
    ("oauth-hover", "login-oauth", "hover", "backgroundColor",
     "The #ebebeb the OAuth fill darkens to on hover."),
    ("oauth-pressed", "login-oauth", "pressed", "backgroundColor",
     "The #dbdbdb the OAuth fill darkens to when pressed."),
    ("text", "login-title", "default", "color",
     "The #0f0f0f auth heading ink."),
    ("muted", "login-card", "default", "color",
     "The #2b2b2b auth body ink."),
    ("link", "login-link", "default", "color",
     "The #1c029d of the Create-one link — Kinde's link hue."),
    ("field-border", "login-field", "default", "paint-border:input",
     "The #ababab border on the auth email field."),
    ("focus", "login-cta", "focus-visible", "outlineColor",
     "The #0054f0 of the 2px solid auth focus ring, offset 2px."),
]:
    try:
        if prop.startswith("paint-border:"):
            n = paint_node(comp, state, prop.split(":", 1)[1])
            b = (n or {}).get("border", "")
            m = re.search(r"(rgba?\([\d.,\s]+\)|#[0-9a-fA-F]{3,8})", b)
            v = norm_color(m.group(1)) if m else None
        else:
            v = norm_color(st(comp, state).get(prop, ""))
        if v and v != "transparent" and v != "rgba(0, 0, 0, 0)":
            auth[key] = {"value": v, "type": "color",
                         "source": f"computed {prop} of {comp} {state} (raw/components-computed.json)",
                         "description": desc}
    except KeyError:
        pass

# -------------------------------------------------------------------- roles

light = SPEC["light"]
ALIAS = "role alias over the core palette"


def role(root, name, target, desc):
    emit(root, name, {"value": target, "type": "color", "source": ALIAS, "description": desc})


if "100" in ink:
    role(light, "--text-primary", "{color.ink.100}", "Heading and body ink.")
    role(light, "--surface-dark", "{color.ink.100}", "The footer field — a dark surface painted on the light page.")
if "nav-text" in meas_c:
    role(light, "--text-secondary", "{color.measured.nav-text}", "Nav-link and base text, one step softer than the ink.")
if "50" in ink:
    role(light, "--text-muted", "{color.ink.50}", "Muted eyebrow/secondary copy (50% ink).")
if "bright" in plum:
    role(light, "--text-link", "{color.plum.bright}", "Link and hover violet.")
    role(light, "--action-primary", "{color.plum.bright}", "Every primary button fill.")
    role(light, "--action-ghost-border", "{color.plum.bright}", "The ghost button's border and label violet.")
if "dark" in plum:
    role(light, "--action-primary-hover", "{color.plum.dark}", "The violet a primary control darkens to on hover/press.")
if "white" in neutral:
    role(light, "--text-on-accent", "{color.neutral.white}", "Label on the violet fills.")
    role(light, "--text-on-dark", "{color.neutral.white}", "Text on the dark surfaces.")
    role(light, "--surface-page", "{color.neutral.white}", "The white page field (body paints white).")
    role(light, "--surface-card", "{color.neutral.white}", "Card and panel fill.")
if "warm-white" in neutral:
    role(light, "--surface-warm", "{color.neutral.warm-white}", "The declared warm-white field.")
if "grey" in neutral:
    role(light, "--surface-muted", "{color.neutral.grey}", "The light grey tinted field.")
if "lightest" in plum:
    role(light, "--surface-tint", "{color.plum.lightest}", "The plum-tinted section field.")
if "plan-top" in meas_c:
    role(light, "--surface-plan-top", "{color.measured.plan-top}", "The plan card's violet header.")
if "lighter" in plum:
    role(light, "--accent-subtle", "{color.plum.lighter}", "The most-popular pill / badge fill.")
if "save-pill" in meas_c:
    role(light, "--accent-success", "{color.measured.save-pill}", "The mint save-pill fill.")
if "field-border" in meas_c:
    role(light, "--border-field", "{color.measured.field-border}", "The #d9d9e0 field/select border.")
if "field-focus" in meas_c:
    role(light, "--border-field-focus", "{color.measured.field-focus}", "The #3898ec the select border gains on focus.")
if "10" in ink:
    role(light, "--border-subtle", "{color.ink.10}", "The 10% ink hairline.")
if "chip-border" in meas_c:
    role(light, "--border-chip", "{color.measured.chip-border}", "The chip border.")
if "25" in plum:
    role(light, "--border-plan", "{color.plum.25}", "The featured plan card's 25% plum border.")
if "focus" in meas_c:
    role(light, "--focus-ring", "{color.measured.focus}", "The 1px auto focus ring (the Webflow/UA ring).")
if "10" in plum:
    role(light, "--state-hover-wash", "{color.plum.10}", "The 10% plum wash a mega-nav link paints on hover.")
# Kinde auth roles
if "primary" in auth:
    role(light, "--auth-action-primary", "{color.auth.primary}", "The hosted-auth primary fill.")
if "oauth" in auth:
    role(light, "--auth-surface-secondary", "{color.auth.oauth}", "The OAuth button fill.")
if "field-border" in auth:
    role(light, "--auth-border-field", "{color.auth.field-border}", "The auth field border.")
if "link" in auth:
    role(light, "--auth-text-link", "{color.auth.link}", "The auth link hue.")
if "focus" in auth:
    role(light, "--auth-focus-ring", "{color.auth.focus}", "The 2px auth focus ring.")

dark = SPEC["dark"]
if "dark-band" in meas_c:
    role(dark, "--surface-band", "{color.measured.dark-band}", "The Cake-MCP band — the darkest painted surface.")
if "100" in ink:
    role(dark, "--surface-page", "{color.ink.100}", "The footer field.")
if "white" in neutral:
    role(dark, "--text-primary", "{color.neutral.white}", "Text on the dark surfaces.")
if "white-50" in neutral:
    role(dark, "--text-muted", "{color.neutral.white-50}", "Muted text on dark.")
if "100" in plum:
    role(dark, "--text-link-hover", "{color.plum.100}", "The #7e78ff a footer link turns on hover.")
if "100" in SPEC["core"].get("color", {}).get("lemon", {}):
    role(dark, "--text-eyebrow", "{color.lemon.100}", "The lemon eyebrow on the dark band.")
if "dark-hairline" in meas_c:
    role(dark, "--border-hairline", "{color.measured.dark-hairline}", "The 18% white hairline inside the dark band.")
if "10" in plum:
    role(dark, "--border-accent", "{color.plum.10}", "Reserved plum-10 accent border on dark.")

# ------------------------------------------------------------- type scale

type_scale = SPEC["core"].setdefault("font", {}).setdefault("size", {})
for key, comp, state, use_ts, desc in [
    ("display", "hero-title", "default", False, "The Exposure display size on every marketing h1 (pricing, feature, blog and demo heads share it)."),
    ("display-mobile", "m-hero", "default", False, "The display size at 390px."),
    ("h2", "section-h2", "default", False, "The Exposure section-heading size (also the blog card title)."),
    ("price", "plan-price", "default", True, "The plan-card price figure."),
    ("auth-heading", "login-title", "default", False, "The Kinde Welcome-back heading."),
    ("faq-question", "faq-item", "default", True, "The FAQ question size."),
    ("lede", "hero-sub", "default", False, "The hero sub-copy size."),
    ("plan-name", "plan-card", "default", True, "The plan name (Growth)."),
    ("story", "story-card", "default", True, "The story-card quote size."),
    ("menu-link", "menu-link", "default", False, "The mega-nav link size."),
    ("eyebrow", "eyebrow", "default", False, "The section eyebrow size."),
    ("body", "collection-card", "default", False, "The base body size."),
    ("footer-link", "footer-link", "default", False, "The footer link size."),
    ("pill", "announce-pill", "default", False, "The announcement-chip size."),
    ("plan-cta", "plan-cta", "default", False, "The plan CTA label size."),
    ("nav", "nav-link", "default", False, "The nav link / small button size."),
    ("badge", "plan-badge", "default", False, "The most-popular badge size."),
]:
    v = ts(comp, state, "fontSize") if use_ts else (st(comp, state).get("fontSize") if have(comp, state) else None)
    if v:
        type_scale[key] = {"type": "dimension", "value": v,
                           "source": f"computed fontSize of {comp} {state} (raw/components-computed.json)",
                           "description": desc}

leading = SPEC["core"].setdefault("font", {}).setdefault("lineHeight", {})
for key, comp, state, use_ts, desc in [
    ("display", "hero-title", "default", False, "Display leading (1.1x)."),
    ("display-mobile", "m-hero", "default", False, "Mobile display leading."),
    ("h2", "section-h2", "default", False, "Heading leading (1x)."),
    ("lede", "hero-sub", "default", False, "Lede leading (1.6x)."),
    ("faq-question", "faq-item", "default", True, "FAQ-question leading."),
    ("menu-link", "menu-link", "default", False, "Mega-nav link leading."),
    ("nav", "nav-link", "default", False, "Nav link leading."),
    ("body", "collection-card", "default", False, "Body leading."),
]:
    v = ts(comp, state, "lineHeight") if use_ts else (st(comp, state).get("lineHeight") if have(comp, state) else None)
    if v:
        leading[key] = {"type": "dimension", "value": v,
                        "source": f"computed lineHeight of {comp} {state} (raw/components-computed.json)",
                        "description": desc}

weight = SPEC["core"].setdefault("font", {}).setdefault("weight", {})
for key, comp, state, use_ts, desc in [
    ("display", "hero-title", "default", False, "Exposure renders its light face at 400 on h1s."),
    ("heading", "section-h2", "default", False, "The 300 of section headings (Exposure Light)."),
    ("lede", "hero-sub", "default", False, "The 300 lede."),
    ("menu-link", "menu-link", "default", False, "The 600 mega-nav link."),
    ("eyebrow", "eyebrow", "default", False, "The 600 eyebrow."),
    ("body", "collection-card", "default", False, "The 400 base."),
    ("pill", "announce-pill", "default", False, "The 500 chip label."),
    ("badge", "plan-badge", "default", False, "The 500 badge."),
    ("footer-link", "footer-link", "default", False, "The 300 footer link."),
]:
    v = ts(comp, state, "fontWeight") if use_ts else (st(comp, state).get("fontWeight") if have(comp, state) else None)
    if v:
        weight[key] = {"type": "fontWeight", "value": v,
                       "source": f"computed fontWeight of {comp} {state} (raw/components-computed.json)",
                       "description": desc}

tracking = SPEC["core"].setdefault("font", {}).setdefault("letterSpacing", {})
for key, comp, state, use_ts, desc in [
    ("display", "hero-title", "default", False, "The -2px display tracking."),
    ("h2", "section-h2", "default", False, "The -1px heading tracking."),
    ("lede", "hero-sub", "default", False, "The -0.3px lede tracking."),
    ("eyebrow", "eyebrow", "default", False, "The +0.8px eyebrow tracking."),
    ("price", "plan-price", "default", True, "The -1.6px price tracking."),
    ("footer-link", "footer-link", "default", False, "The -0.16px footer link tracking."),
]:
    v = ts(comp, state, "letterSpacing") if use_ts else (st(comp, state).get("letterSpacing") if have(comp, state) else None)
    if v:
        tracking[key] = {"type": "dimension", "value": v,
                         "source": f"computed letterSpacing of {comp} {state} (raw/components-computed.json)",
                         "description": desc}

# ---------------------------------------------------------- radius, shadow

radius = SPEC["core"].setdefault("radius", {})
for key, comp, state, prop, desc in [
    ("pill", "nav-cta", "default", "borderTopLeftRadius", "The 100px pill on every button and the region select."),
    ("toggle", "billing-toggle", "default", "paint-radius:.ms-switch-bg", "The 999px billing-toggle shell."),
    ("nav-login", "nav-login", "default", "borderTopLeftRadius", "The 50px Login pill — half the standard pill."),
    ("dropdown", "header", "default", "paint-radius:.nav-container", "The 20px mega-nav panel."),
    ("dark-band", "dark-section", "default", "borderTopLeftRadius", "The 28px dark band."),
    ("card", "story-card", "default", "borderTopLeftRadius", "The 16px card radius (story card, plan card top, Kinde card)."),
    ("auth", "login-field", "default", "borderTopLeftRadius", "The 8px Kinde control radius."),
    ("menu-button", "m-menu-button", "default", "borderTopLeftRadius", "The 4px hamburger radius."),
]:
    try:
        if prop.startswith("paint-radius:"):
            n = paint_node(comp, state, prop.split(":", 1)[1])
            v = (n or {}).get("radius")
            if v and v != "0px":
                radius[key] = {"value": v, "type": "dimension",
                               "source": f"painted layer radius under {comp} {state} (raw/components-computed.json)",
                               "description": desc}
            continue
        if have(comp, state, prop):
            v = st(comp, state)[prop]
            if v != "0px":
                radius[key] = {"value": v, "type": "dimension",
                               "source": f"computed {prop} of {comp} {state} (raw/components-computed.json)",
                               "description": desc}
    except KeyError:
        pass


def shadow_of(comp, state, prop="boxShadow", needle=None):
    try:
        if needle:
            n = paint_node(comp, state, needle)
            v = (n or {}).get("shadow")
        else:
            v = st(comp, state).get(prop)
        if not v or v == "none":
            return None
        m = re.findall(r"(rgba?\([\d.,\s]+\)|#[0-9a-fA-F]{3,8})\s+(-?\d+(?:\.\d+)?px)\s+(-?\d+(?:\.\d+)?px)\s+(-?\d+(?:\.\d+)?px)\s+(-?\d+(?:\.\d+)?px)", v)
        if m:
            return [{"color": norm_color(a), "offsetX": x, "offsetY": y, "blur": bl, "spread": sp} for a, x, y, bl, sp in m]
    except KeyError:
        pass
    return None


shadow = SPEC["core"].setdefault("shadow", {})
for key, comp, state, needle, desc in [
    ("nav", "header", "default", None, "The navbar's rgba(0,0,0,0.2) 0 2px 20px -19px drop (plus a second 0 1px 30px rgba(0,0,0,0.1) layer)."),
    ("dropdown", "header", "default", ".nav-container", "The mega-nav panel's rgba(24,22,26,0.25) 0 0 20px -5px."),
    ("card", "story-card", "default", None, "The story/tooltip card's rgba(0,0,0,0.2) 0 2px 5px."),
    ("faq-open", "faq-item", "opened", None, "The rgba(0,0,0,0.2) 0 2px 10px -8px an opened FAQ card draws, with its -2px lift."),
]:
    layers = shadow_of(comp, state, needle=needle)
    if layers:
        shadow[key] = {"value": layers, "type": "shadow",
                       "source": f"computed boxShadow of {comp} {state} (raw/components-computed.json)",
                       "description": desc}

# ------------------------------------------------------------- gradient

grad = SPEC["core"].setdefault("gradient", {})
try:
    n = paint_node("announce-pill", "default", ".pm-pulley-tag")
    bg = (n or {}).get("bgImage", "")
    inner = re.match(r"linear-gradient\((.*)\)", bg)
    if inner:
        body = inner.group(1)
        # An angle only leads when the first token is not a colour.
        a = re.match(r"(to\s+[\w\s]+|-?\d+(?:\.\d+)?deg)\s*,", body)
        stops = re.findall(r"(rgba?\([\d.,\s]+\)|#[0-9a-fA-F]{3,8})\s+(\d+(?:\.\d+)?)%", body)
        if stops:
            grad["pulley-tag"] = {
                "value": [{"color": norm_color(c), "position": float(p) / 100} for c, p in stops],
                "type": "gradient",
                "source": "computed backgroundImage of the pm-pulley-tag layer under announce-pill (raw/components-computed.json)",
                "angle": (a.group(1) if a else "180deg"),
                "description": "The olive-to-rust gradient on the Pulley tag inside the announcement chip."}
except KeyError:
    pass

# ---------------------------------------------------------------- motion

motion = SPEC["core"].setdefault("duration", {})
for key, comp, state, i, desc in [
    ("button", "nav-cta", "default", 0, "The 0.2s all transition on every button and link."),
    ("ghost", "hero-demo", "default", 0, "The 0.4s all transition on the ghost CTA."),
    ("faq", "faq-item", "default", 0, "The 0.3s transform transition on the FAQ card (the opened lift)."),
    ("story", "story-card", "default", 0, "The 0.2s opacity fade of the hover quote cards."),
    ("auth", "login-cta", "default", 0, "The 0.15s transition on Kinde controls."),
]:
    try:
        s = st(comp, state)
        d = s["transitionDuration"].split(",")[i].strip()
        if d and d != "0s":
            motion[key] = {"value": d, "type": "duration",
                           "source": f"computed transition of {comp} {state} (raw/components-computed.json)",
                           "description": desc + f" ({s['transitionProperty'].split(',')[i].strip() if i < len(s['transitionProperty'].split(',')) else s['transitionProperty']})"}
    except (KeyError, TypeError):
        pass
# The mega-nav grid and panel transitions, read from the home sheet rules
# recorded in raw/components-computed.json _meta.sheets (no element reading holds them).
SHEETS = json.loads((RAW / "components-computed.json").read_text())["_meta"].get("sheets", {}).get("home", [])
for key, sel, desc in [
    ("mega-nav", ".nav-dropdown-grid", "The mega-nav grid's open animation."),
    ("nav-panel", ".nav-container.for-dropdown", "The mega-nav panel's transition."),
]:
    rule = next((x for x in SHEETS if x.get("selector") == sel), None)
    d = re.match(r"^\s*(\d*\.?\d+m?s)\b", (rule or {}).get("transition") or "")
    if d and key not in motion:
        motion[key] = {"value": d.group(1), "type": "duration",
                       "source": f"{sel} transition in the home stylesheets (raw/components-computed.json _meta.sheets: '{rule['transition']}')",
                       "description": desc}

# ------------------------------------------------------------- measured

meas = SPEC["core"].setdefault("measured", {})
# the focus ring is the 1px auto outline the UA/Webflow draws
try:
    s = st("nav-cta", "focus-visible")
    if s.get("outlineStyle") not in (None, "none"):
        meas["focus-outline"] = {"value": f"{s['outlineWidth']} {s['outlineStyle']} {norm_color(s['outlineColor'])}",
                                 "type": "other",
                                 "source": "computed outline of nav-cta focus-visible (raw/components-computed.json)",
                                 "description": "The 1px auto #005fcc focus ring, ~1px offset, on every focused marketing control."}
except KeyError:
    pass
try:
    s = st("login-cta", "focus-visible")
    if s.get("outlineStyle") not in (None, "none"):
        meas["auth-focus-outline"] = {"value": f"{s['outlineWidth']} {s['outlineStyle']} {norm_color(s['outlineColor'])} offset {s['outlineOffset']}",
                                      "type": "other",
                                      "source": "computed outline of login-cta focus-visible (raw/components-computed.json)",
                                      "description": "The 2px solid #0054f0 ring, 2px offset, on Kinde controls."}
except KeyError:
    pass
# the opened FAQ card lifts 2px
try:
    t = st("faq-item", "opened").get("transform", "")
    if t and t != "none":
        meas["faq-open-lift"] = {"value": t, "type": "other",
                                 "source": "computed transform of faq-item opened (raw/components-computed.json)",
                                 "description": "The translateY(-2px) an opened FAQ card takes, over the faq-open shadow."}
except KeyError:
    pass
# the mobile page forces a ~745px layout viewport
try:
    w = C["m-header"]["states"]["default"]["rect"]["w"]
    if w:
        meas["mobile-layout-width"] = {"value": round(w, 2), "type": "number",
                                       "source": "m-header default rect width (raw/components-computed.json)",
                                       "description": "The ~745px layout viewport the page forces at 390 visual width — .comparison-grid{min-width:700px} plus navbar chrome; phones pan horizontally."}
except KeyError:
    pass

# ------------------------------------------------------------------ component

comp = SPEC["component"]
for key, cname, state, prop, desc in [
    ("control.height", "hero-cta", "default", "height", "The hero CTA height."),
    ("button.height", "nav-cta", "default", "height", "The header Get-started-free height."),
    ("plan-cta.height", "plan-cta", "default", "height", "The plan-card Start-free height."),
    ("field.height", "country-select", "default", "height", "The region select height (the Kinde field shares it)."),
    ("header.height", "header", "default", "height", "The marketing header height."),
    ("header.height-mobile", "m-header", "default", "height", "The marketing header at 390 visual width (745 layout)."),
    ("plan-card.width", "plan-card", "default", "width", "A plan card's width."),
    ("login-card.width", "login-card", "default", "width", "The Kinde auth card width."),
    ("nav-dropdown.width", "nav-dropdown", "default", "width", "The Product mega-nav panel width."),
    ("menu-button.size", "m-menu-button", "default", "width", "The hamburger hit area."),
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
