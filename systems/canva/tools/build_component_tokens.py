#!/usr/bin/env python3
"""Write raw/component-tokens.json, the token spec build_tokens.py reads.

canva.com's public signed-out surface is a StyleX app: its CSS arrives as
linked bundles from static.canva.com (cross-origin to the CSSOM, so vars.mjs
reads every body off the network) and declares a real but hash-named custom-
property layer — StyleX variables like --8jnd6g resolved per theme in
raw/css-vars.json, with .light/.dark redeclarations on the site's own theme
classes. Those become {"var": ...} leaves resolved per theme by
build_tokens.py. Everything else is **measured computed values** from
raw/components-computed.json:

  neutrals    the #0f1015 ink (all text, button labels, hairline outlines),
              white surfaces (page, plan cards, flyout, auth card), the
              #f6f7f8 footer fade, field borders #767676, and the translucent
              layers the dark band paints: rgba(255,255,255,0.898) text and
              button fills, rgba(255,255,255,0.07/0.15) ghost-button states
  brand       the Canva purple ramp measured off the real actions:
              #8b3dff default (Sign up pill, plan CTAs, the billing switch,
              mobile Log in), #7630d7 hover, #612dae pressed; the declared
              deep purple #4a2e7e and the #00c4cc->#7d2ae8 brand gradient
              in the StyleX layer
  states      hover = rgba(64,79,109,0.06) / pressed = rgba(57,70,96,0.14)
              ink washes on light; on dark = rgba(255,255,255,0.07/0.15)
              and rgba(163,112,252,0.2) purple-tint; focus = 1-2px auto
              outlines — #99c8ff on the dark band, #005fcc on light,
              #e59700 inside the mobile menu
  hairline    secondary buttons and fields carry no border: a 1px inset
              rgba(53,65,90,0.2) box-shadow ring instead
  font        "Canva Sans" everywhere text is styled (a hash-named StyleX
              family name on unstyled containers reads Times/Arial fallbacks)
  ramp        measured 80/88 display (hero), 64/70.4 display (page titles),
              56/61.6 h2, 45/49.5 display at 390, 28/35 card titles, 24/33.6
              lede, 21/26 mobile-menu rows, 18/24 section labels, 16/22-24
              body, 14/22 controls and nav, 12/20 plan meta
  shape       9999px pills (tabs, the billing switch), 20px hero CTA, 12px
              buttons/links/fields/cards, 10px header controls, 14px
              comparison rows, 16px plan-card surface, 32px flyout column

A leaf is {"var": ...} (resolved per theme) or {"value": ..., "source": ...}
for a measured value. Only the signed-out public surface was read; the
"dark" set is the dark-painted header/hero band and the dark feature
sections the light page shows, not a user-selectable theme.
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
    "The token tree build_tokens.py turns into tokens.json. canva.com's "
    "public surface is a StyleX app whose hashed custom-property layer "
    "(raw/css-vars.json — .light/.dark redeclarations on the site's own "
    "theme classes) is var-referenced where it declares the brand colours, "
    "and measured computed values (raw/components-computed.json) cover the "
    "ink/white neutrals, the #8b3dff action ramp, the ink-wash and white "
    "state layers, the inset hairline ring, Canva Sans, the pill/12px "
    "radii and the 0.1s/0.2s control motion. The 'dark' set is the dark-"
    "painted header/hero band and dark feature sections the light page "
    "shows — the site paints it through .theme.dark elements, not a user "
    "toggle."),
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
    """First resolved light var whose value matches (the StyleX names are
    hashed, so names carry no meaning — a match on value is the evidence)."""
    for n, v in R.items():
        if v == value and (contains is None or contains in n):
            return n
    return None


# ------------------------------------------------------------------- fonts

fam = SPEC["core"].setdefault("font", {}).setdefault("family", {})
if have("plan-cta", "default", "fontFamily"):
    fam["sans"] = {"value": st("plan-cta", "default")["fontFamily"], "type": "fontFamily",
                   "source": "computed fontFamily of plan-cta default (raw/components-computed.json); the @font-face blocks are served from static.canva.com (raw/css-vars.json fonts)",
                   "description": "The one family the styled surface paints: Canva Sans, falling back to system sans."}
weights = SPEC["core"].setdefault("font", {}).setdefault("weight", {})
for key, comp, state, desc in [
    ("regular", "hero-sub", "default", "Body and display weight (400)."),
    ("medium", "m-nav-item", "default", "The 500 weight on menu rows, footer links and plan prices."),
    ("semibold", "plan-cta", "default", "The 600 weight on every button, nav label and section label."),
]:
    v = ts(comp, state, "fontWeight")
    if v:
        weights[key] = {"value": int(v), "type": "fontWeight",
                        "source": f"computed fontWeight of {comp} {state} (raw/components-computed.json)",
                        "description": desc}

# ------------------------------------------------------- declared colours

brand = SPEC["core"].setdefault("color", {}).setdefault("brand", {})
# The purple ramp measured off the real actions, plus the declared StyleX
# values that match — var-referenced where a StyleX variable resolves to it.
for key, comp, state, prop, want, desc in [
    ("purple", "plan-cta", "default", "backgroundColor", "#8b3dff",
     "The Canva purple #8b3dff: the Sign up pill, every plan CTA, the billing switch and the mobile Log in fill."),
    ("purple-hover", "plan-cta", "hover", "backgroundColor", "#7630d7",
     "The #7630d7 hover step every purple button takes."),
    ("purple-pressed", "plan-cta", "pressed", "backgroundColor", "#612dae",
     "The #612dae pressed step."),
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
# deep purple + brand gradient, declared in the StyleX layer
for key, want, desc in [
    ("purple-deep", "#4a2e7e", "The declared deep purple #4a2e7e in the StyleX layer."),
]:
    vn = find_var(want)
    if vn:
        brand[key] = var(vn, "color",
                         source=f"css-var {vn} resolved light (raw/css-vars.json)",
                         description=desc)
gv = next((n for n, v in R.items() if isinstance(v, str) and "linear-gradient" in v and "#00c4cc" in v and "#7d2ae8" in v), None)
if gv:
    brand["gradient"] = {"value": [{"color": "#00c4cc", "position": 0}, {"color": "#7d2ae8", "position": 1}],
                         "type": "gradient",
                         "source": f"css-var {gv} resolved light (raw/css-vars.json): the #00c4cc -> #7d2ae8 brand gradient the Canva logo mark carries",
                         "description": "The teal-to-purple Canva brand gradient."}
# declared status hues in the StyleX layer
status = SPEC["core"].setdefault("color", {}).setdefault("status", {})
for key, want, desc in [
    ("error", "#db142c", "The declared error red #db142c."),
    ("warning-text", "#ad5a00", "The declared warning text #ad5a00."),
    ("info", "#3d8bff", "The declared info blue #3d8bff."),
]:
    vn = find_var(want)
    if vn:
        status[key] = var(vn, "color",
                          source=f"css-var {vn} resolved light (raw/css-vars.json)",
                          description=desc)

# measured neutrals
neutral = SPEC["core"].setdefault("color", {}).setdefault("neutral", {})
for key, comp, state, prop, desc in [
    ("ink", "oauth-button", "default", "color", "The #0f1015 ink: all body text, button labels on white fills, field borders' colour base."),
    ("white", "search-field", "default", "ancestor-white", "The #ffffff surface: page field, plan cards, flyout panel, auth card, the switch thumb."),
    ("muted", "plan-card", "default", "muted-text", "The rgba(16,18,25,0.698) secondary text (plan card labels, flyout description)."),
    ("footer-fade", "footer", "default", "footer-bg", "The #f6f7f8 the footer fades to."),
    ("wash-hover", "oauth-button", "hover", "backgroundColor", "The rgba(64,79,109,0.06) hover wash on secondary actions and tabs."),
    ("wash-pressed", "oauth-button", "pressed", "backgroundColor", "The rgba(57,70,96,0.14) pressed wash on secondary actions and accordion rows."),
    ("hairline", "oauth-button", "default", "hairline", "The rgba(53,65,90,0.2) 1px inset ring secondary buttons and fields carry instead of a border."),
    ("scrim", "header", "default", "scrim", "The rgba(19,22,32,0.6) overlay the StyleX layer declares for scrims."),
]:
    try:
        if prop == "ancestor-white":
            hit = next((a.get("bg") for a in C[comp]["states"][state].get("ancestors", []) if a.get("bg")), None)
            v = norm_color(hit) if hit else None  # no reading, no token (never a typed #ffffff)
        elif prop == "muted-text":
            v = norm_color((C[comp]["states"][state].get("textStyle") or {}).get("color"))
        elif prop == "footer-bg":
            img = st(comp, state).get("backgroundImage") or ""
            m = re.search(r"rgb\(([\d,\s]+)\)", img)
            v = "rgb(" + m.group(1).strip() + ")" if m else None
        elif prop == "hairline":
            m = re.search(r"rgba\(([\d,\s.]+)\)\s+0px 0px 0px 1px inset", st(comp, state).get("boxShadow") or "")
            v = "rgba(" + m.group(1) + ")" if m else None
        elif prop == "scrim":
            vn = find_var("rgba(19, 22, 32, 0.6)")
            if vn:
                neutral[key] = var(vn, "color", source=f"css-var {vn} resolved light (raw/css-vars.json)", description=desc)
            continue
        else:
            v = norm_color(st(comp, state).get(prop, ""))
        if v:
            neutral[key] = {"value": v, "type": "color",
                            "source": f"computed {prop} of {comp} {state} (raw/components-computed.json)",
                            "description": desc}
    except KeyError:
        pass

# -------------------------------------------------------------------- roles

light = SPEC["light"]
ALIAS = "role alias over the core palette"
for name, target, desc in [
    ("--text-primary", "color.neutral.ink", "Body and display ink on light."),
    ("--text-muted", "color.neutral.muted", "Secondary text on light."),
    ("--surface-page", "color.neutral.white", "The white page field."),
    ("--surface-card", "color.neutral.white", "Plan cards, the flyout panel, the auth card."),
    ("--surface-footer", "color.neutral.footer-fade", "The footer's #f6f7f8 fade."),
    ("--action-primary", "color.brand.purple", "The #8b3dff action fill."),
    ("--action-primary-hover", "color.brand.purple-hover", "The hover step."),
    ("--action-primary-pressed", "color.brand.purple-pressed", "The pressed step."),
    ("--text-on-action", "#ffffff", "White labels on the purple fill."),
    ("--state-hover", "color.neutral.wash-hover", "The 6% ink wash on hover."),
    ("--state-pressed", "color.neutral.wash-pressed", "The 14% ink wash on pressed."),
    ("--border-hairline", "color.neutral.hairline", "The inset hairline ring on secondary actions."),
    ("--scrim", "color.neutral.scrim", "The declared 60% ink scrim."),
]:
    if target.startswith("{"):
        continue
    root_bag = target.split(".")[1] if "." in target else None
    root_key = target.split(".")[-1]
    bag = {"neutral": neutral, "brand": brand, "status": status}.get(root_bag)
    if bag and root_key in bag:
        emit(light, name, {"value": "{" + target + "}", "type": "color",
                           "source": ALIAS, "description": desc})
    elif root_bag is None:
        emit(light, name, {"value": target, "type": "color",
                           "source": "computed color of plan-cta / oauth-button labels (raw/components-computed.json)",
                           "description": desc})

def read_somewhere(value, comps):
    """True when one of comps' states reads `value` as a colour, fill, text colour or painted layer."""
    want = norm_color(value)
    for comp in comps:
        for s in (C.get(comp) or {}).get("states", {}).values():
            sty = s.get("style") or {}
            pool = [sty.get(k) for k in ("color", "backgroundColor", "borderTopColor")]
            pool += [(s.get("textStyle") or {}).get("color")]
            pool += [x.get("bg") for x in s.get("paint") or []]
            pool += [c for x in s.get("paint") or [] for c in re.findall(r"rgba?\([^)]*\)", str(x.get("shadow", "")))]
            pool += re.findall(r"rgba?\([^)]*\)", str(sty.get("boxShadow", "")))
            if any(v and norm_color(v) == want for v in pool):
                return True
    return False


dark = SPEC["dark"]
# The dark-painted band (header + hero + feature sections): white text and
# fills are translucent so the gradient media shows through.
DARKSURF = find_var("#16171d")
for name, target, desc in [
    ("--text-primary", "rgba(255, 255, 255, 0.898)", "The rgba(255,255,255,0.898) on-dark text — white at 90%, never pure."),
    ("--text-strong", "#ffffff", "Pure white reserved for the nav triggers' labels."),
    ("--surface-page", "DARKSURF", "The darkest surface the .dark layer declares; the hero band itself is a gradient media layer, not a flat fill — see patterns.md."),
    ("--action-ghost", "rgba(255, 255, 255, 0)", "Ghost buttons on dark start fully transparent."),
    ("--action-ghost-hover", "rgba(255, 255, 255, 0.07)", "The 7% white fill a dark ghost button takes on hover (signup-cta)."),
    ("--action-ghost-pressed", "rgba(255, 255, 255, 0.15)", "The 15% white fill on pressed (nav triggers, ghost buttons)."),
    ("--action-ghost-tint", "rgba(163, 112, 252, 0.2)", "The 20% purple-tint hover the nav triggers take."),
    ("--action-secondary", "rgba(255, 255, 255, 0.898)", "The 90% white fill the secondary buttons on dark carry (Log in, hero CTA, Explore)."),
    ("--action-secondary-hover", "#ffffff", "Hover takes the white fill to 100%."),
    ("--action-secondary-pressed", "rgba(255, 255, 255, 0.8)", "Pressed drops the fill to 80%."),
    ("--text-on-action", "{color.neutral.ink}", "Ink labels on the white fills."),
    ("--border-ghost", "rgba(255, 255, 255, 0.2)", "The 20% white inset ring ghost buttons carry (signup-cta shadow)."),
]:
    if target == "DARKSURF" and DARKSURF:
        emit(dark, name, var(DARKSURF, "color",
                             source=f"css-var {DARKSURF} resolved dark (raw/css-vars.json)",
                             description=desc))
    elif target == "DARKSURF":
        # No resolved var holds the dark surface: keep the typed value, labelled as typed (D2).
        emit(dark, name, {"value": "#16171d", "type": "color",
                          "source": "Reconstruction: entered by hand at capture time as the .theme.dark surface; raw/css-vars.json resolves no variable to it",
                          "description": desc})
    else:
        if target.startswith("{"):
            src_ = ALIAS
        elif read_somewhere(target, ("signup-cta", "login-link", "nav-trigger", "hero-cta")):
            src_ = "computed colors of signup-cta / login-link / nav-trigger / hero-cta states over the dark band (raw/components-computed.json)"
        else:
            src_ = "Reconstruction: entered by hand at capture time; no reading of signup-cta / login-link / nav-trigger / hero-cta holds it"
        emit(dark, name, {"value": target, "type": "color",
                          "source": src_,
                          "description": desc})

# ------------------------------------------------------------- type scale

type_scale = SPEC["core"].setdefault("font", {}).setdefault("size", {})
for key, comp, state, desc in [
    ("display-hero", "hero-title", "default", "The 80px hero display (home)."),
    ("display", "pricing-h1", "default", "The 64px page-title display (pricing, templates)."),
    ("display-mobile", "m-hero", "default", "The 45px display at 390 wide."),
    ("h2", "section-h2", "default", "The 56px section heading."),
    ("card-title", "tool-panel", "default", "The 28px card/panel title (tool panel, feature card)."),
    ("price", "plan-price", "default", "The ~29px plan price figure."),
    ("lede", "hero-sub", "default", "The 24px hero lede / card titles."),
    ("menu-item", "m-nav-item", "default", "The 21px mobile-menu rows."),
    ("section-label", "feature-accordion", "default", "The 18px comparison-row / tab label."),
    ("body", "hero-cta", "default", "The 16px body/button size."),
    ("control", "plan-cta", "default", "The 14px control/nav text."),
    ("meta", "plan-card", "default", "The 12px plan-card meta text."),
]:
    v = ts(comp, state, "fontSize")
    if v:
        type_scale[key] = {"type": "dimension", "value": v,
                           "source": f"computed fontSize of {comp} {state} (raw/components-computed.json)",
                           "description": desc}

leading = SPEC["core"].setdefault("font", {}).setdefault("lineHeight", {})
for key, comp, state, desc in [
    ("display-hero", "hero-title", "default", "Hero display leading (88px on 80px)."),
    ("display", "pricing-h1", "default", "Page-title leading (70.4px on 64px)."),
    ("h2", "section-h2", "default", "Heading leading (61.6px on 56px)."),
    ("card-title", "tool-panel", "default", "Card-title leading (35px on 28px)."),
    ("lede", "hero-sub", "default", "Lede leading (33.6px on 24px)."),
    ("control", "plan-cta", "default", "Control leading (22px on 14px)."),
    ("meta", "plan-card", "default", "Meta leading (20px on 12px)."),
]:
    v = ts(comp, state, "lineHeight")
    if v:
        leading[key] = {"type": "dimension", "value": v,
                        "source": f"computed lineHeight of {comp} {state} (raw/components-computed.json)",
                        "description": desc}

# ---------------------------------------------------------- radius, motion

radius = SPEC["core"].setdefault("radius", {})
for key, comp, state, prop, desc in [
    ("button", "plan-cta", "default", "borderTopLeftRadius", "The 12px radius on buttons, links, fields and cards."),
    ("header-control", "signup-cta", "default", "borderTopLeftRadius", "The 10px radius on header actions."),
    ("cta", "hero-cta", "default", "borderTopLeftRadius", "The 20px radius on the hero CTA."),
    ("row", "feature-accordion", "default", "borderTopLeftRadius", "The 14px radius on comparison rows."),
    ("pill", "tool-tab", "default", "borderTopLeftRadius", "The 9999px pill on tabs and the billing switch."),
]:
    if have(comp, state, prop):
        radius[key] = {"value": st(comp, state)[prop], "type": "dimension",
                       "source": f"computed {prop} of {comp} {state} (raw/components-computed.json)",
                       "description": desc}
card_r = None
try:
    for n in C["nav-dropdown"]["states"]["default"].get("paint") or []:
        if n.get("radius") and str(n["radius"]).split()[0] == "32px":
            card_r = "32px"
            card_r_read = str(n["radius"])
            break
except KeyError:
    pass
if card_r:
    radius["flyout-panel"] = {"value": card_r, "type": "dimension",
                              "source": "painted layer radius inside nav-dropdown (raw/components-computed.json): '%s'" % card_r_read,
                              "description": "The 32px radius the mega-menu's white column paints on its left corners."}
plan_r = None
try:
    for n in C["plan-card"]["states"]["default"].get("paint") or []:
        if n.get("radius") and str(n["radius"]).split()[0] == "16px":
            plan_r = n["radius"]
except KeyError:
    pass
if plan_r:
    radius["card"] = {"value": plan_r, "type": "dimension",
                      "source": "painted layer radius inside plan-card (raw/components-computed.json)",
                      "description": "The 16px radius on the white plan-card surface."}

meas = SPEC["core"].setdefault("measured", {})
for key, comp, state, prop, ty, desc in [
    ("focus-ring-dark", "signup-cta", "focus-visible", "outlineColor", "color", "The #99c8ff light-blue keyboard ring on the dark band (1-2px auto)."),
    ("focus-ring-light", "plan-cta", "focus-visible", "outlineColor", "color", "The #005fcc blue keyboard ring on light surfaces (1px auto)."),
    ("focus-ring-mobile", "m-nav-item", "focus-visible", "outlineColor", "color", "The #e59700 amber keyboard ring inside the mobile menu (1px auto)."),
    ("hairline", "oauth-button", "default", "boxShadow", "shadow", "The inset 1px rgba(53,65,90,0.2) ring secondary buttons and fields draw instead of a border."),
    ("switch-thumb-shadow", "billing-switch", "default", "thumb-shadow", "shadow", "The layered elevation the switch thumb paints."),
]:
    try:
        if prop == "thumb-shadow":
            hit = next((n.get("shadow") for n in C[comp]["states"][state].get("paint", []) if n.get("shadow")), None)
            if hit:
                layers = re.findall(r"(rgba?\([\d.,\s]+\))\s+(-?\d+(?:\.\d+)?px)\s+(-?\d+(?:\.\d+)?px)\s+(-?\d+(?:\.\d+)?px)\s+(-?\d+(?:\.\d+)?px)( inset)?", hit)
                if layers:
                    meas[key] = {"value": [{"color": norm_color(a), "offsetX": x, "offsetY": y, "blur": bl, "spread": sp, "inset": bool(i)} for a, x, y, bl, sp, i in layers],
                                 "type": "shadow",
                                 "source": f"painted layer shadow inside {comp} {state} (raw/components-computed.json)",
                                 "description": desc}
            continue
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
for key, comp, state, desc in [
    ("control-transition", "hero-cta", "default", "The 0.1s control transition (background-color, box-shadow, color) with a 0.07s transform."),
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
# pressed buttons shrink (login-link 64.42 -> 63.78, hero-cta 192 -> 190.08)
try:
    d0 = C["hero-cta"]["states"]["default"]["rect"]["w"]
    dp = C["hero-cta"]["states"]["pressed"]["rect"]["w"]
    if d0 and dp and dp < d0:
        meas["pressed-scale"] = {"value": round(dp / d0, 4), "type": "number",
                                 "source": "pressed rect / default rect of hero-cta (raw/components-computed.json)",
                                 "description": "The ~0.99 scale a pressed button takes."}
except KeyError:
    pass

# ------------------------------------------------------------------ component

comp = SPEC["component"]
for key, cname, state, prop, desc in [
    ("button.height", "plan-cta", "default", "height", "The 40px standard button height (plan CTAs, auth buttons, mobile actions)."),
    ("button-cta.height", "hero-cta", "default", "height", "The 56px hero CTA height."),
    ("field.height", "username-input", "default", "height", "The 38px auth-field height."),
    ("field-search.height", "search-field", "default", "height", "The 46px template-search field."),
    ("switch.height", "billing-switch", "default", "height", "The 24px billing-switch pill (40 wide)."),
    ("navcontrol.height", "nav-trigger", "default", "height", "The 32px header controls."),
    ("menurow.height", "m-nav-item", "default", "height", "The 42px mobile-menu row."),
    ("header.height", "header", "default", "height", "The 80px desktop header."),
    ("header.height-mobile", "m-header", "default", "height", "The 80px mobile header."),
    ("flyout.height", "nav-dropdown", "default", "height", "The 478px mega-menu panel."),
    ("plancard.height", "plan-card", "default", "height", "The 353px plan card (measured inner column; the white surface is ~308 wide, 16px radius)."),
    ("accordionrow.height", "feature-accordion", "default", "height", "The 64px comparison-row height."),
    ("categorycard.height", "category-card", "default", "height", "The 80px template-category card."),
    ("authcard.height", "auth-card", "default", "height", "The ~350px auth card."),
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
