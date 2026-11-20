#!/usr/bin/env python3
"""Write raw/component-tokens.json, the token spec build_tokens.py reads.

dock.us's public signed-out surface is a Webflow marketing site plus the
Chakra auth app on auth.dock.us. Its CSS arrives same-origin from
cdn.prod.website-files.com (vars.mjs reads every body off the CSSOM) and
declares a real custom-property layer — the marketing --ds-*/--color-*/
--space-*/--text-*/--radius-*/--shadow-* vars scoped to .dock-shared-shell
and #dock-native-home, the _anchor colour ramp on the shared shell, and the
auth app's --chakra-* theme — all resolved per theme in raw/css-vars.json.
Those become {"var": ...} leaves resolved per theme by build_tokens.py.
Everything else is **measured computed values** from
raw/components-computed.json:

  neutrals    the #121722 ink (all text), white surfaces (header bar, menu
              viewport, plan cards, auth cards), the #f8f8f9/#f2f2f3 control
              washes, the #dedfe3 hairline and the rgba(18,23,34,0.2) inset
              ring that stands in for a border on white controls
  brand       the marketing blue ramp measured off the real actions:
              #0068f9 default (Start for free, plan CTA, Copy prompt),
              #0060eb hover, #005fe4 pressed, #002fa6 the hero band; the
              auth app's royal blue #4058ff (Chakra button fill), the
              #d5ecff selected filter pill; plus the declared illustration
              accents --color-green/pink/purple/sky/warm/yellow
  states      hover #f8f8f9 / pressed #f2f2f3 ink washes on light controls;
              on the deep-blue band = rgba(255,255,255,0.06)/0.1 ghost fills;
              focus = 2px rgba(18,23,34,0.6) ink outline on light, 2px
              #0068f9 on the pricing buttons, 3px white on the blue fill
  hairline    white controls carry no border: a 0.5px inset
              color(srgb .07 .09 .133 / .2) ring (nav buttons, demo form
              fields use rgba(18,23,34,0.1) 1px), primary buttons a 0.5px
              inset rgba(11,68,147,0.4)
  font        three painted families: DockWebflowNavigation (header,
              footer, menus), DockWebflowHome (home hero + sections),
              Roobert (pricing, customers, templates, demo and the auth
              app); Roobert ships as real @font-face files
  ramp        measured 80.6/84.3 display (demo h1), 70/72 (customers h1),
              62/70.4 (home hero), 60/64 (pricing h1), 38/44 (templates h1),
              29/34 mobile hero; 20/28 plan names, 19/24 prices, 18/21.6
              section labels, 16/19.2-24 controls and body, 15.5/20 menu,
              14.5/20 group headings, 14/16.8-21 auth controls/fields,
              12.5/15 trust badges
  shape       100px pills (nav controls, CTAs, filter pills), 19px menu
              viewport, 18.9px hero artwork, 12px popular column, 8px menu
              items, 60px filter pill, 6px HubSpot fields, 4-6px Chakra
              controls

A leaf is {"var": ...} (resolved per theme) or {"value": ..., "source": ...}
for a measured value. Only the signed-out public surface was read; the
"dark" set is the deep-blue hero band and the auth page's dark testimonial
pane the light site paints — not a user-selectable theme (light and dark
resolve the same in raw/css-vars.json apart from one menu value).
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
    "The token tree build_tokens.py turns into tokens.json. dock.us's "
    "public surface is a Webflow marketing site plus the Chakra auth app on "
    "auth.dock.us: its custom-property layer (raw/css-vars.json — the "
    "--ds-*/--color-*/--space-* marketing layer on .dock-shared-shell and "
    "#dock-native-home, the _anchor ramp, and the auth app's --chakra-* "
    "theme) is var-referenced where it declares the brand colours, the "
    "space scale and the marketing radii; measured computed values "
    "(raw/components-computed.json) cover the #121722 ink, the #0068f9 "
    "action ramp, the light control washes, the inset hairline rings, the "
    "three painted font stacks, the pill/card radii and the state outlines. "
    "The 'dark' set is the deep-blue hero band and the auth signup pane the "
    "light site paints — not a user toggle: the light and dark resolutions "
    "in raw/css-vars.json are identical apart from one menu value."),
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


# Eight header/footer focus-visible states were recorded `via: focus failed` by the run that wrote
# them; their via was later rewritten by hand to this sentence (commit 492e65670), not re-measured.
# They are treated as failed focus everywhere: never a token source, never counted as a ring.
HAND_RELABELLED_FOCUS = "el.focus() — a real ring painted; document.activeElement read the shadow host (check fixed in kbFocus)"


def not_captured(v):
    """A state whose reading is not what its name says: skipped, focus that never landed, or one
    of the hand-relabelled focus states above."""
    return (bool(v.get("skipped")) or v.get("via") in ("focus failed", HAND_RELABELLED_FOCUS)
            or (v.get("focus") or {}).get("matches") is False)


def st(comp, state):
    v = C[comp]["states"][state]
    if not_captured(v):
        raise KeyError(f"{comp} {state}: focus never confirmed (via {v.get('via')!r}); not a reading")
    return v["style"]


def missed(comp):
    """A source note for a component a later run could not find (its states are an earlier run's)."""
    d = C[comp].get("recaptureMissed")
    return f"; the {d} run did not find {comp}, so these are its {C[comp].get('run')} states (recaptureMissed); recapture needed" if d else ""


def reading(comp, state, prop):
    """One measured colour, normalised; a missing or unconfirmed reading stops the build."""
    v = st(comp, state).get(prop)
    if not v:
        raise KeyError(f"{comp} {state}: no {prop} reading")
    return norm_color(v)


def ts(comp, state, prop):
    """The first text node's reading (textStyle) when the kit recorded one —
    the wrapper's own fontSize can be the container's, not the text's. A
    sup/sub first child is a glyph, not the running text (plan-price's "$"
    sits in a 12px sup over the 19px figure), so for those the element's own
    computed style is the reading."""
    try:
        c = C[comp]["states"][state]
        t = c.get("textStyle") or {}
        v = t.get(prop)
        if v and str(t.get("node") or "").split(".")[0] not in ("sup", "sub"):
            return v
        return c["style"].get(prop) or v
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
    m = re.fullmatch(r"color\(srgb\s+([\d.]+)\s+([\d.]+)\s+([\d.]+)(?:\s*/\s*([\d.]+))?\)", v)
    if m:
        r, g, b, a = m.groups()
        r, g, b = (round(float(x) * 255) for x in (r, g, b))
        if a is None or float(a) >= 1:
            return "#%02x%02x%02x" % (r, g, b)
        return f"rgba({r}, {g}, {b}, {'%g' % float(a)})"
    return v


def have(comp, state, prop=None):
    try:
        s = st(comp, state)
        return prop is None or bool((s.get(prop) or "").strip())
    except KeyError:
        return False


def find_var(value, contains=None):
    """First resolved light var whose value matches, preferring the site's
    own token names over hash- or framework-named ones."""
    best = None
    for n, v in R.items():
        if v == value and (contains is None or contains in n):
            if best is None or len(n) < len(best):
                best = n
    return best


# ------------------------------------------------------------------- fonts

fam = SPEC["core"].setdefault("font", {}).setdefault("family", {})
for key, comp, state, desc in [
    ("nav", "nav-trigger", "default",
     "DockWebflowNavigation (a subset Roobert build): the header, footer and menu layer."),
    ("home", "hero-title", "default",
     "DockWebflowHome: the home hero and section display layer."),
    ("roobert", "pricing-h1", "default",
     "Roobert: pricing, customers, templates, /demo and the auth app — the product face."),
]:
    if have(comp, state, "fontFamily"):
        fam[key] = {"value": st(comp, state)["fontFamily"], "type": "fontFamily",
                    "source": f"computed fontFamily of {comp} {state} (raw/components-computed.json); the @font-face blocks are same-origin Webflow CDN Roobert woff2 (raw/css-vars.json fonts)",
                    "description": desc}
weights = SPEC["core"].setdefault("font", {}).setdefault("weight", {})
for key, comp, state, desc in [
    ("regular", "footer-link", "default", "Body and link weight (400)."),
    ("medium", "nav-trigger", "default", "The 500 weight on controls, nav labels and plan names."),
    ("semibold", "hero-title", "default", "The 600 weight on hero and page display text."),
    ("bold", "customers-h1", "default", "The 700 weight on the customers/templates display and the selected filter pill."),
]:
    v = ts(comp, state, "fontWeight")
    if v:
        weights[key] = {"value": int(v), "type": "fontWeight",
                        "source": f"computed fontWeight of {comp} {state} (raw/components-computed.json)",
                        "description": desc}

# ------------------------------------------------------- declared colours

brand = SPEC["core"].setdefault("color", {}).setdefault("brand", {})
# The action-blue ramp measured off the real controls, plus the declared
# marketing variables that match — var-referenced where the layer names it.
for key, comp, state, prop, desc in [
    ("blue", "nav-cta", "default", "backgroundColor",
     "The Dock blue #0068f9: Start-for-free pill, plan CTA, Copy prompt, demo submit — every primary action."),
    ("blue-hover", "nav-cta", "hover", "backgroundColor",
     "The #0060eb hover step every blue button takes."),
    ("blue-pressed", "nav-cta", "pressed", "backgroundColor",
     "The #005fe4 pressed step."),
]:
    try:
        measured = norm_color(st(comp, state)[prop])
        vn = find_var(measured)
        leaf_ = {"type": "color",
                 "source": f"computed {prop} of {comp} {state} (raw/components-computed.json)" + (f"; css-var {vn}" if vn else ""),
                 "description": desc}
        if vn:
            leaf_["var"] = vn
        else:
            leaf_["value"] = measured
        brand[key] = leaf_
    except KeyError:
        pass
# --color-blue-deep is declared; the component once cited for it (hero-lede) read the hero eyebrow
# pill, not the lede (README: known wrong), so the token carries the declaration alone.
brand["blue-deep"] = var("--color-blue-deep", "color",
                         source="css-var --color-blue-deep resolved light (raw/css-vars.json)",
                         description="The declared #002fa6 deep blue of the home hero; also the base of its oklch gradient.")
# Declared marketing values: the auth royal blue, the selected-filter tint
# and the illustration accents the --color-* layer names.
for key, want, desc in [
    ("royal", "#4058ff", "The auth app's royal blue #4058ff (--royal-blue): the Chakra button fill on auth.dock.us."),
    ("blue-light", "#afdeff", "The declared light blue --color-blue-light #afdeff."),
    ("blue-soft", "#e5f4ff", "The declared soft blue --color-blue-soft #e5f4ff."),
    ("blue-tint", "#d5ecff", "The selected-filter pill fill #d5ecff (_anchor blue-100)."),
    ("green", "#22aba0", "The declared illustration green --color-green #22aba0."),
    ("pink", "#ff93e8", "The declared illustration pink --color-pink #ff93e8."),
    ("purple", "#7000f9", "The declared illustration purple --color-purple #7000f9."),
    ("sky", "#4db5ff", "The declared illustration sky --color-sky #4db5ff; its 40% alpha is the ghost ring on the blue band."),
    ("warm", "#e49a52", "The declared warm accent --color-warm #e49a52."),
    ("yellow", "#ebd94d", "The declared yellow accent --color-yellow #ebd94d."),
]:
    vn = find_var(want)
    if vn:
        brand[key] = var(vn, "color",
                         source=f"css-var {vn} resolved light (raw/css-vars.json)",
                         description=desc)

# measured neutrals
neutral = SPEC["core"].setdefault("color", {}).setdefault("neutral", {})
for key, comp, state, prop, desc in [
    ("ink", "nav-trigger", "default", "color", "The #121722 ink: all body text and labels (--black)."),
    ("ink-auth", "login-card", "default", "color", "The auth app's #1a202c ink (Chakra gray-800)."),
    ("white", "header", "default", "ancestor-white", "The #ffffff surface: header bar, menu viewport, plan cards, auth cards."),
    ("muted", "trust-badge", "default", "color", "The rgba(18,23,34,0.8) secondary text (trust badges, meta)."),
    ("surface-subtle", "pr-sticky", "default", "popular-col", "The #f7f7f8 fill the popular plan column paints."),
    ("wash-hover", "nav-link", "hover", "backgroundColor", "The ~#f8f8f9 hover wash on header controls."),
    ("wash-pressed", "nav-demo", "pressed", "backgroundColor", "The ~#f2f2f3 pressed wash on header controls."),
    ("hairline", "nav-demo", "default", "hairline", "The 0.5px inset rgba(18,23,34,0.2) ring white controls draw instead of a border."),
]:
    try:
        if prop == "ancestor-white":
            hit = next((a.get("bg") for a in C[comp]["states"][state].get("ancestors", []) if a.get("bg")), None)
            if not hit:
                raise ValueError(f"{comp} {state}: no painted ancestor; the white surface has no reading")
            v = norm_color(hit)
        elif prop == "popular-col":
            hit = next((n.get("bg") for n in C[comp]["states"][state].get("paint", [])
                        if n.get("bg") and "popular" in (n.get("node") or "")), None)
            v = norm_color(hit) if hit else None
        elif prop == "hairline":
            m = re.search(r"(color\(srgb\s+[\d.]+\s+[\d.]+\s+[\d.]+\s*/\s*[\d.]+\))\s+0px 0px 0px 0\.5px inset", st(comp, state).get("boxShadow") or "")
            v = norm_color(m.group(1)) if m else None
        else:
            v = norm_color(st(comp, state).get(prop, ""))
        if v:
            neutral[key] = {"value": v, "type": "color",
                            "source": f"computed {prop} of {comp} {state} (raw/components-computed.json)",
                            "description": desc}
    except KeyError:
        pass
# Declared neutral layer values
for key, want, desc in [
    ("border", "#dedfe3", "The --ds-border hairline the pricing sticky bar and menu dividers paint."),
    ("base-200", "#faf9f7", "The _anchor base-200 off-white page field."),
    ("base-300", "#efefef", "The _anchor base-300 subtle fill."),
]:
    vn = find_var(want)
    if vn:
        neutral[key] = var(vn, "color",
                           source=f"css-var {vn} resolved light (raw/css-vars.json)",
                           description=desc)

# -------------------------------------------------------------------- roles

light = SPEC["light"]
ALIAS = "role alias over the core palette"
for name, target, desc in [
    ("--text-primary", "color.neutral.ink", "Body and display ink on light."),
    ("--text-primary-auth", "color.neutral.ink-auth", "The auth app's #1a202c ink."),
    ("--text-muted", "color.neutral.muted", "Secondary text at 80% ink."),
    ("--surface-page", "color.neutral.white", "The white page field."),
    ("--surface-card", "color.neutral.white", "Menu viewport, plan cards, auth cards."),
    ("--surface-subtle", "color.neutral.surface-subtle", "The #f7f7f8 popular-column fill."),
    ("--surface-tint", "color.brand.blue-tint", "The #d5ecff selected filter pill."),
    ("--action-primary", "color.brand.blue", "The #0068f9 action fill."),
    ("--action-primary-hover", "color.brand.blue-hover", "The #0060eb hover step."),
    ("--action-primary-pressed", "color.brand.blue-pressed", "The #005fe4 pressed step."),
    ("--action-auth", "color.brand.royal", "The auth app's #4058ff Chakra fill."),
    ("--text-on-action", ("nav-cta", "default", "color"), "White labels on the blue fills."),
    ("--state-hover", "color.neutral.wash-hover", "The ~#f8f8f9 control hover wash."),
    ("--state-pressed", "color.neutral.wash-pressed", "The ~#f2f2f3 control pressed wash."),
    ("--border", "color.neutral.border", "The #dedfe3 hairline."),
    ("--border-hairline", "color.neutral.hairline", "The inset 0.5px ring white controls carry instead of a border."),
    ("--focus-ring", ("mcp-copy", "focus-visible", "outlineColor"), "The 2px 60%-ink keyboard outline on light surfaces."),
    ("--focus-ring-blue", "color.brand.blue", "The 2px #0068f9 keyboard outline on the pricing buttons."),
]:
    if isinstance(target, tuple):
        emit(light, name, {"value": reading(*target), "type": "color",
                           "source": "computed {2} of {0} {1} (raw/components-computed.json)".format(*target),
                           "description": desc})
        continue
    parts = target.split(".")
    root_bag = parts[1] if len(parts) > 1 and parts[0] == "color" else None
    root_key = parts[-1]
    bag = {"neutral": neutral, "brand": brand}.get(root_bag)
    if bag and root_key in bag:
        emit(light, name, {"value": "{" + target + "}", "type": "color",
                           "source": ALIAS, "description": desc})

dark = SPEC["dark"]
# The dark-painted islands on the light site: the #002fa6 hero band and the
# auth signup's deep-blue testimonial pane. Ghost buttons paint white-alpha
# fills and a 40% sky-blue inset ring.
def shadow_colour(comp, state):
    """The colour of a single-layer box-shadow reading."""
    m = re.match(r"(color\(srgb[^)]*\)|rgba?\([^)]*\))", st(comp, state).get("boxShadow") or "")
    if not m:
        raise KeyError(f"{comp} {state}: no shadow colour reading")
    return norm_color(m.group(1))


for name, target, desc in [
    ("--text-primary", ("hero-title", "default", "color"), "White text on the deep-blue band (hero headline, ghost labels)."),
    ("--surface-band", "{color.brand.blue-deep}", "The #002fa6 hero band; the page-placeholder gradient runs to oklch(0.397 0.194 263.2)."),
    ("--surface-pane", "#242d7d", "The auth signup's testimonial pane base (radial-gradient #242d7d -> #3542af)."),
    ("--action-ghost", ("hero-demo", "default", "backgroundColor"), "Ghost buttons on the band start fully transparent (hero Request demo)."),
    ("--action-ghost-hover", ("hero-demo", "hover", "backgroundColor"), "The 6% white fill a band ghost button takes on hover."),
    ("--action-ghost-pressed", ("hero-demo", "pressed", "backgroundColor"), "The 10% white fill on pressed."),
    ("--border-ghost", ("hero-demo", "default", "boxShadow"), "The 0.5px inset sky ring ghost and primary buttons on the band carry (--color-sky at 40%)."),
    ("--action-primary", "{color.brand.blue}", "The #0068f9 primary fill reads the same on the band."),
    ("--text-on-action", ("hero-cta", "default", "color"), "White labels on the blue fill."),
    ("--focus-ring", ("hero-cta", "focus-visible", "outlineColor"), "The same 2px 60%-ink keyboard outline paints over the band."),
]:
    if isinstance(target, tuple):
        v = shadow_colour(*target[:2]) if target[2] == "boxShadow" else reading(*target)
        emit(dark, name, {"value": v, "type": "color",
                          "source": "computed {2} of {0} {1} (raw/components-computed.json)".format(*target),
                          "description": desc})
    elif target.startswith("{"):
        emit(dark, name, {"value": target, "type": "color",
                          "source": ALIAS, "description": desc})
    else:
        # No reading of auth.dock.us's signup pane is in raw/: the value was entered by hand.
        emit(dark, name, {"value": target, "type": "color",
                          "source": "Reconstruction: entered by hand at capture time from the auth signup pane's background; no reading in raw/ holds it",
                          "description": desc})

# ------------------------------------------------------------- type scale

type_scale = SPEC["core"].setdefault("font", {}).setdefault("size", {})
for key, comp, state, desc in [
    ("display-demo", "demo-h1", "default", "The ~81px display on /demo."),
    ("display-customers", "customers-h1", "default", "The 70px display on /customers."),
    ("display-hero", "hero-title", "default", "The 62px home hero display."),
    ("display", "pricing-h1", "default", "The 60px page-title display (pricing)."),
    ("display-mobile", "m-hero", "default", "The ~29px hero at 390 wide."),
    ("h1-templates", "templates-h1", "default", "The 38px templates heading."),
    ("card-title", "plan-name", "default", "The 20px plan/card title."),
    ("price", "plan-price", "default", "The 19px plan price figure."),
    ("section-label", "section-h2", "default", "The 18px section label."),
    ("menu-item-mobile", "m-nav-item", "default", "The 18px mobile-menu rows."),
    ("body", "header", "default", "The 16px body/nav size."),
    ("menu", "menu-link", "default", "The 15.5px menu link size."),
    ("group", "menu-group", "default", "The 14.5px menu group heading."),
    ("control-auth", "continue-btn", "default", "The 14px auth control size."),
    ("field", "signup-field", "default", "The 14px auth field text."),
    ("meta", "trust-badge", "default", "The 12.5px trust-badge/meta size."),
]:
    v = ts(comp, state, "fontSize")
    if v:
        type_scale[key] = {"type": "dimension", "value": v,
                           "source": f"computed fontSize of {comp} {state} (raw/components-computed.json)" + missed(comp),
                           "description": desc}

leading = SPEC["core"].setdefault("font", {}).setdefault("lineHeight", {})
for key, comp, state, desc in [
    ("display-hero", "hero-title", "default", "Hero leading (70.4px on 62px)."),
    ("display", "pricing-h1", "default", "Page-title leading (64px on 60px)."),
    ("display-customers", "customers-h1", "default", "Customers display leading (72px on 70px)."),
    ("menu-item-mobile", "m-nav-item", "default", "Mobile-menu leading (21.6px on 18px)."),
    ("card-title", "plan-name", "default", "Card-title leading (28px on 20px)."),
    ("price", "plan-price", "default", "Price leading (24px on 19px)."),
    ("control", "nav-trigger", "default", "Control leading (19.2px on 16px)."),
    ("body", "footer-link", "default", "Body/link leading (22.4px on 16px)."),
    ("menu", "menu-link", "default", "Menu leading (20px on 15.5px)."),
    ("control-auth", "continue-btn", "default", "Auth control leading (16.8px on 14px)."),
    ("meta", "trust-badge", "default", "Meta leading (15px on 12.5px)."),
]:
    v = ts(comp, state, "lineHeight")
    if v:
        leading[key] = {"type": "dimension", "value": v,
                        "source": f"computed lineHeight of {comp} {state} (raw/components-computed.json)" + missed(comp),
                        "description": desc}

# ---------------------------------------------------------------- spacing

space = SPEC["core"].setdefault("space", {})
for key, want, desc in [
    ("1", "--space-1", "The 4px base step."),
    ("1-5", "--space-1-5", "The 6px step."),
    ("2", "--space-2", "The 8px step."),
    ("2-5", "--space-2-5", "The 10px step."),
    ("3", "--space-3", "The 12px step."),
    ("4", "--space-4", "The 16px step."),
    ("6", "--space-6", "The 24px step."),
    ("8", "--space-8", "The 32px step."),
    ("10", "--space-10", "The 40px step."),
    ("14", "--space-14", "The 56px step."),
]:
    if want in R:
        space[key] = var(want, "dimension",
                         source=f"css-var {want} resolved light (raw/css-vars.json)",
                         description=desc)

# ---------------------------------------------------------- radius, motion

radius = SPEC["core"].setdefault("radius", {})
for key, comp, state, prop, desc in [
    ("pill", "nav-cta", "default", "borderTopLeftRadius", "The 100px pill on nav controls, CTAs and filter pills."),
    ("menu-item", "menu-link", "default", "borderTopLeftRadius", "The 8px radius on mega-menu items."),
    ("auth-control", "continue-btn", "default", "borderTopLeftRadius", "The 4px radius on the auth app's buttons."),
    ("auth-field", "signup-field", "default", "borderTopLeftRadius", "The 4px radius on auth fields."),
]:
    if have(comp, state, prop):
        radius[key] = {"value": st(comp, state)[prop], "type": "dimension",
                       "source": f"computed {prop} of {comp} {state} (raw/components-computed.json)" + missed(comp),
                       "description": desc}
for key, comp, want, desc in [
    ("menu-panel", "nav-dropdown", "19.1", "The ~19px radius the mega-menu viewport paints."),
    ("hero-art", "hero-card", "18.9", "The ~19px radius the hero artwork frame paints."),
    ("popular-col", "pr-sticky", "12", "The 12px top radius on the popular plan column."),
    ("filter-pill", "filter-radio", "60", "The 60px radius on the selected filter pill."),
    ("field", "demo-field", "6", "The 6px radius on HubSpot form fields."),
]:
    hit = None
    try:
        for n in C[comp]["states"]["default"].get("paint") or []:
            if n.get("radius") and want in str(n["radius"]):
                hit = n["radius"]
                break
    except KeyError:
        pass
    if hit:
        # DTCG dimensions are a single length; a "12px 12px 0px 0px" corner
        # list keeps its first (uniform) value.
        v = hit.split()[0] if isinstance(hit, str) and " " in hit else hit
        radius[key] = {"value": v, "type": "dimension",
                       "source": f"painted layer radius inside {comp} (raw/components-computed.json): {hit!r}",
                       "description": desc}
# declared marketing radii
for key, want, desc in [
    ("item", "--radius-item", "The declared 8px item radius."),
    ("pill-var", "--radius-pill", "The declared 100px pill radius."),
]:
    if want in R:
        radius[key] = var(want, "dimension",
                          source=f"css-var {want} resolved light (raw/css-vars.json)",
                          description=desc)

meas = SPEC["core"].setdefault("measured", {})
for key, comp, state, prop, ty, desc in [
    ("focus-ring", "mcp-copy", "focus-visible", "outlineColor", "color", "The 2px rgba(18,23,34,0.6) ink keyboard outline on light controls."),
    ("focus-ring-blue", "plan-cta", "focus-visible", "outlineColor", "color", "The 2px #0068f9 keyboard outline on pricing buttons."),
    ("focus-ring-on-blue", "hero-cta", "focus-visible", "outlineColor", "color", "The keyboard outline over the blue band."),
    ("ring-on-blue", "hero-cta", "default", "boxShadow", "shadow", "The 0.5px inset rgba(77,181,255,0.4) sky ring primary buttons paint on the band."),
    ("ring-primary", "nav-cta", "default", "boxShadow", "shadow", "The 0.5px inset rgba(11,68,147,0.4) deep-blue ring the primary action paints."),
    ("hairline", "nav-demo", "default", "boxShadow", "shadow", "The 0.5px inset rgba(18,23,34,0.2) ring white controls draw instead of a border."),
    ("field-ring", "demo-field", "default", "paint-ring", "shadow", "The 1px inset rgba(18,23,34,0.1) ring the HubSpot fields draw."),
    ("control-shadow", "plan-cta", "default", "boxShadow", "shadow", "The pricing button's layered shadow (0.5px drop + ink hairline)."),
]:
    try:
        if prop == "paint-ring":
            hit = next((n.get("shadow") for n in C[comp]["states"][state].get("paint", []) if n.get("shadow")), None)
            if hit:
                s = hit
                layers = re.findall(r"(rgba?\([\d.,\s]+\))\s+(-?\d+(?:\.\d+)?px)\s+(-?\d+(?:\.\d+)?px)\s+(-?\d+(?:\.\d+)?px)\s+(-?\d+(?:\.\d+)?px)( inset)?", s)
                if layers:
                    meas[key] = {"value": [{"color": norm_color(a), "offsetX": x, "offsetY": y, "blur": bl, "spread": sp, "inset": bool(i)} for a, x, y, bl, sp, i in layers],
                                 "type": "shadow",
                                 "source": f"painted layer shadow inside {comp} {state} (raw/components-computed.json)",
                                 "description": desc}
            continue
        if prop == "boxShadow":
            s = st(comp, state)[prop]
            # srgb-space rgba() and rgb() layers both parse
            s = re.sub(r"color\(srgb\s+([\d.]+)\s+([\d.]+)\s+([\d.]+)\s*/\s*([\d.]+)\)",
                       lambda m: "rgba(%d, %d, %d, %s)" % tuple([round(float(x) * 255) for x in m.groups()[:3]] + [float(m.group(4))]), s)
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
for key, comp, state, desc in [
    ("control-transition", "nav-cta", "default", "The control transition duration."),
    ("menu-transition", "nav-trigger", "default", "The menu/control transition."),
]:
    try:
        s = st(comp, state)
        d = s["transitionDuration"]
        first = d.split(",")[0].strip()
        if first and first != "0s":
            meas[key] = {"value": first, "type": "duration",
                         "source": f"computed transition of {comp} {state} (raw/components-computed.json)",
                         "description": desc + f" ({s['transitionProperty'][:80]})"}
    except (KeyError, TypeError):
        pass
# declared motion
for key, want, ty, desc in [
    ("duration-fast", "--duration-fast", "duration", "The declared .14s fast duration."),
    ("duration-menu", "--duration-menu", "duration", "The declared .24s menu duration."),
    ("ease-menu", "--ease-menu", "cubicBezier", "The declared menu easing cubic-bezier(.22,1,.36,1)."),
]:
    if want in R:
        meas[key] = var(want, ty,
                        source=f"css-var {want} resolved light (raw/css-vars.json)",
                        description=desc)

# ------------------------------------------------------------------ component

comp = SPEC["component"]
for key, cname, state, prop, desc in [
    ("header.height", "header", "default", "height", "The ~70px desktop header bar."),
    ("header.height-mobile", "m-header", "default", "height", "The 76px mobile header."),
    ("navcontrol.height", "nav-trigger", "default", "height", "The ~38px header controls."),
    ("navcta.height", "nav-cta", "default", "height", "The ~38px header actions."),
    ("menurow.height", "menu-link", "default", "height", "The 40px mega-menu link row."),
    ("menurow-mobile.height", "m-nav-item", "default", "height", "The 56px mobile-menu row."),
    ("menupanel.height", "nav-dropdown", "default", "height", "The 258px mega-menu panel."),
    ("menupanel-mobile.height", "m-menu-open", "default", "height", "The ~386px opened mobile menu panel."),
    ("ctabutton.height", "hero-cta", "default", "height", "The ~45px hero CTA height."),
    ("plancta.height", "plan-cta", "default", "height", "The 40px pricing button."),
    ("filter.height", "filter-radio", "default", "height", "The 36px filter pill."),
    ("field-auth.height", "subdomain-field", "default", "height", "The 36px auth field."),
    ("button-auth.height", "continue-btn", "default", "height", "The 36px auth button."),
    ("field-demo.height", "demo-field", "default", "height", "The 48px HubSpot field."),
    ("plancard.height", "plan-card", "default", "height", "The ~300px plan column."),
    ("faqrow.height", "faq-item", "default", "height", "The 80px pricing FAQ row."),
    ("authcard.height", "login-card", "default", "height", "The ~323px login card."),
    ("sticky.height", "pr-sticky", "default", "height", "The 152px sticky plan bar."),
]:
    if have(cname, state, prop):
        node = comp
        parts = key.split(".")
        for p in parts[:-1]:
            node = node.setdefault(p, {})
        node[parts[-1]] = {"type": "dimension", "value": st(cname, state)[prop],
                           "source": f"computed {prop} of {cname} {state} (raw/components-computed.json)" + missed(cname),
                           "description": desc}

(RAW / "component-tokens.json").write_text(json.dumps(SPEC, indent=1, ensure_ascii=False) + "\n")


def count(d):
    if not isinstance(d, dict):
        return 1
    if "var" in d or "value" in d or "$value" in d:
        return 1
    return sum(count(v) for v in d.values())


print({k: count(v) for k, v in SPEC.items() if not k.startswith("_")})
