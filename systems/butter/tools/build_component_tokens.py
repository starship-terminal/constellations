#!/usr/bin/env python3
"""Write raw/component-tokens.json, the token spec build_tokens.py reads.

butter.video is a Next.js marketing app (styled-components) that declares a
real design-token layer — the --butter-* custom properties harvested into
raw/css-vars.json (tools/capture/vars.mjs): 11 colours, 2 font stacks and 2
easings. Those become {"var": ...} leaves. The dark app shell on /explore,
/blocks and /templates is an MUI surface with no declared variables, so its
tokens are **measured computed values** from raw/components-computed.json:

  light       #0f0f0f ink on white, #1e1e1e nav text/buttons, #ededed footer
              and plan-card fields, the #4dc5e5 accent painted inside buttons
  accents     declared --butter-green/-pink/-red/-yellow (used in gradients
              and illustrations, rarely painted on the captured components)
  dark        #0a0909 canvas, #151515 cards with #212121 borders, #1d1d1d
              raised buttons, #252525 active nav, #f5f5f5 text, #a1a1aa muted
  fonts       DieGrotesk (marketing), ABCDiatype (marketing meta text),
              dieGroteskA (the dark app shell)
  ramp        measured 107.57/60.4/56.7/24.5/20.7/18/16/13.5px steps plus the
              dark shell's 24/14/13/12
  shape       16px button pills, 10px controls, 12px nav pills/badges,
              32px cards, 42px dark tiles, 8px header island
  states      the #3c3c3c 1px focus ring (a box-shadow, not an outline),
              the dark shell's 0.16s transitions, the 0.5s billing/nav fades

A leaf is {"var": "--name"} (resolved per theme by build_tokens.py) or
{"value": ..., "source": "..."} for a measured value. The site paints two
surfaces: the light marketing pages and the dark app shell, so both the
light and dark sets are populated.
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
    "The token tree build_tokens.py turns into tokens.json. butter.video "
    "declares a --butter-* design-token layer in its stylesheets "
    "(raw/css-vars.json); the light marketing set is built from those "
    "declared variables plus measured computed styles, and the dark set "
    "from measured computed styles on the /explore app shell "
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


# ------------------------------------------------------------------- fonts

fam = SPEC["core"].setdefault("font", {}).setdefault("family", {})
if "--butter-font-primary" in R:
    fam["marketing"] = var("--butter-font-primary", "fontFamily",
                           description="The marketing stack (DieGrotesk first), declared on butter.video.")
if "--butter-font-secondary" in R:
    fam["meta"] = var("--butter-font-secondary", "fontFamily",
                      description="The ABCDiatype stack used for meta/label text on the marketing pages.")
for key, comp, state, desc in [
    ("app", "d-sidebar", "default", "The dark app-shell stack (dieGroteskA first)."),
    ("body", "hero-sub", "default", "Body/lede text (DieGrotesk first)."),
]:
    if have(comp, state, "fontFamily"):
        v = ts(comp, state, "fontFamily")
        if key == "app":
            v = st(comp, state)["fontFamily"]
        fam[key] = {"value": v, "type": "fontFamily",
                    "source": f"computed fontFamily of {comp} {state} (raw/components-computed.json)",
                    "description": desc}

# ------------------------------------------------------- declared colours

neutral = SPEC["core"].setdefault("color", {}).setdefault("neutral", {})
for key, vname, desc in [
    ("ink", "--butter-true-black", "The near-black ink #0f0f0f on hero and heading text."),
    ("soft-ink", "--butter-black", "The softer black #1e1e1e on nav text, logos and the dark button fills."),
    ("paper-warm", "--butter-white", "The declared white #fafafa on plan-card name chips."),
    ("off-white", "--butter-off-white", "The declared off-white #f7f7f7."),
    ("grey", "--butter-light-grey", "The light grey #ededed footer, plan-card and dropdown-pill field."),
    ("grey-2", "--butter-dark-grey", "The darker declared grey #e2e2e2."),
    ("charcoal", "--butter-charcoal", "The charcoal #3c3c3c the 1px focus ring is drawn in."),
]:
    if vname in R:
        neutral[key] = var(vname, "color", description=desc)
# measured additions the declared layer does not name
if have("feature-row", "default", "borderTopColor"):
    neutral["hairline"] = {"value": norm_color(st("feature-row", "default")["borderTopColor"]),
                           "type": "color",
                           "source": "computed borderTopColor of feature-row (raw/components-computed.json)",
                           "description": "The rgba(15,15,15,0.15) hairline under feature rows and the nav dropdown."}
for key, comp, state, prop, desc in [
    ("faint", "m-menu-open", "default", "textStyle-color", "The 50% black used for muted marketing text."),
]:
    try:
        v = norm_color(C[comp]["states"][state].get("textStyle", {}).get("color"))
        if v and v != "transparent":
            neutral[key] = {"value": v, "type": "color",
                            "source": f"computed textStyle color of {comp} {state} (raw/components-computed.json)",
                            "description": desc}
    except KeyError:
        pass
neutral["paper"] = {"value": "#ffffff", "type": "color",
                    "source": "body backgroundColor computes transparent; the marketing canvas paints white (verified against the screenshots)",
                    "description": "The white marketing page field."}

brand = SPEC["core"].setdefault("color", {}).setdefault("brand", {})
for key, vname, desc in [
    ("blue", "--butter-blue", "The cyan #4dc5e5 painted inside the buttons as the accent layer."),
    ("green", "--butter-green", "The declared accent green #63ad45."),
    ("pink", "--butter-pink", "The declared accent pink #f9abff."),
    ("red", "--butter-red", "The declared accent red #ff3333."),
    ("yellow", "--butter-yellow", "The declared accent yellow #e9d352."),
]:
    if vname in R:
        brand[key] = var(vname, "color", description=desc)

# ------------------------------------------------------- dark shell colours

appc = SPEC["core"].setdefault("color", {}).setdefault("app", {})
for key, comp, state, prop, desc in [
    ("canvas", "d-sidebar", "default", "paint", "The near-black #0a0909 app-shell canvas."),
    ("text", "d-sidebar", "default", "color", "The #f5f5f5 app-shell text."),
    ("muted", "d-sidebar", "default", "textStyle-color", "The #a1a1aa muted app-shell text."),
    ("card", "d-card", "default", "backgroundColor", "The #151515 card fill."),
    ("card-border", "d-card", "default", "borderTopColor", "The #212121 card border."),
    ("raised", "d-login", "default", "backgroundColor", "The #1d1d1d raised button fill."),
    ("active", "d-nav-link", "default", "paint", "The #252525 active nav-item pill."),
    ("action-ink", "d-signup", "default", "color", "The #0a0909 text on the inverted light buttons."),
]:
    try:
        if prop == "paint":
            v = norm_color(painted(comp, state) or "")
        elif prop == "textStyle-color":
            v = norm_color(C[comp]["states"][state].get("textStyle", {}).get("color"))
        else:
            v = norm_color(st(comp, state).get(prop, ""))
        if v and v != "transparent":
            appc[key] = {"value": v, "type": "color",
                         "source": f"computed {prop} of {comp} {state} (raw/components-computed.json)",
                         "description": desc}
    except KeyError:
        pass

# -------------------------------------------------------------------- roles

light = SPEC["light"]
ALIAS = "role alias over the core palette"
if "ink" in neutral:
    emit(light, "--text-primary", {"value": "{color.neutral.ink}", "type": "color",
                                   "source": ALIAS, "description": "Body and heading ink."})
if "soft-ink" in neutral:
    emit(light, "--text-secondary", {"value": "{color.neutral.soft-ink}", "type": "color",
                                     "source": ALIAS, "description": "Nav text and the dark button fills."})
if "faint" in neutral:
    emit(light, "--text-muted", {"value": "{color.neutral.faint}", "type": "color",
                                 "source": ALIAS, "description": "Muted marketing text (50% black)."})
if "paper" in neutral:
    emit(light, "--surface-page", {"value": "{color.neutral.paper}", "type": "color",
                                   "source": ALIAS, "description": "The white marketing page field."})
if "grey" in neutral:
    emit(light, "--surface-grey", {"value": "{color.neutral.grey}", "type": "color",
                                   "source": ALIAS, "description": "The light-grey footer, plan-card and dropdown-pill field."})
if "paper-warm" in neutral:
    emit(light, "--surface-chip", {"value": "{color.neutral.paper-warm}", "type": "color",
                                   "source": ALIAS, "description": "The #fafafa chip fill inside plan cards."})
if "soft-ink" in neutral:
    emit(light, "--action-primary", {"value": "{color.neutral.soft-ink}", "type": "color",
                                     "source": ALIAS, "description": "The dark #1e1e1e button fill."})
# button label colour is --butter-light #ebebeb, measured as rgb(235,235,235)
emit(light, "--text-on-dark", {"var": "--butter-light", "type": "color",
                               "description": "The #ebebeb label on the dark buttons."})
if "blue" in brand:
    emit(light, "--action-accent", {"value": "{color.brand.blue}", "type": "color",
                                    "source": ALIAS, "description": "The cyan accent layer inside the buttons."})
if "hairline" in neutral:
    emit(light, "--border-field", {"value": "{color.neutral.hairline}", "type": "color",
                                   "source": ALIAS, "description": "The 15%-black hairline."})
if "charcoal" in neutral:
    emit(light, "--focus-ring", {"value": "{color.neutral.charcoal}", "type": "color",
                                 "source": ALIAS, "description": "The 1px #3c3c3c keyboard-focus ring (a box-shadow)."})

dark = SPEC["dark"]
if "text" in appc:
    emit(dark, "--text-primary", {"value": "{color.app.text}", "type": "color",
                                  "source": ALIAS, "description": "App-shell text."})
if "muted" in appc:
    emit(dark, "--text-muted", {"value": "{color.app.muted}", "type": "color",
                                "source": ALIAS, "description": "Muted app-shell text."})
if "canvas" in appc:
    emit(dark, "--surface-page", {"value": "{color.app.canvas}", "type": "color",
                                  "source": ALIAS, "description": "The app-shell canvas."})
if "card" in appc:
    emit(dark, "--surface-card", {"value": "{color.app.card}", "type": "color",
                                  "source": ALIAS, "description": "The app-shell card fill."})
if "raised" in appc:
    emit(dark, "--surface-raised", {"value": "{color.app.raised}", "type": "color",
                                    "source": ALIAS, "description": "The raised button fill."})
if "active" in appc:
    emit(dark, "--surface-active", {"value": "{color.app.active}", "type": "color",
                                    "source": ALIAS, "description": "The active nav-item pill."})
if "card-border" in appc:
    emit(dark, "--border-card", {"value": "{color.app.card-border}", "type": "color",
                                 "source": ALIAS, "description": "The card border."})
if "text" in appc:
    emit(dark, "--action-primary", {"value": "{color.app.text}", "type": "color",
                                    "source": ALIAS, "description": "The inverted light button fill."})
if "action-ink" in appc:
    emit(dark, "--text-on-action", {"value": "{color.app.action-ink}", "type": "color",
                                    "source": ALIAS, "description": "Text on the inverted light buttons."})

# ------------------------------------------------------------- type scale

type_scale = SPEC["core"].setdefault("font", {}).setdefault("size", {})
for key, comp, state, prop, bag, ty, desc in [
    ("display", "hero-title", "default", "fontSize", type_scale, "dimension", "The marketing display size (Engineered for Creativity)."),
    ("h2", "section-h2", "default", "fontSize", type_scale, "dimension", "The marketing section-heading size."),
    ("price", "plan-price", "default", "fontSize", type_scale, "dimension", "The plan-card price figure."),
    ("display-mobile", "m-hero", "default", "fontSize", type_scale, "dimension", "The display size at 390px."),
    ("lede", "hero-sub", "default", "fontSize", type_scale, "dimension", "The hero sub-copy / FAQ-question size."),
    ("subtitle", "footer-link", "default", "fontSize", type_scale, "dimension", "Footer-link and billing-toggle text."),
    ("body", "header", "default", "fontSize", type_scale, "dimension", "The page base size."),
    ("nav", "nav-link", "default", "fontSize", type_scale, "dimension", "Nav link / button label size."),
    ("meta", "footer", "default", "fontSize", type_scale, "dimension", "The ABCDiatype meta size."),
    ("app-section", "d-section", "default", "fontSize", type_scale, "dimension", "The dark shell's section heading."),
    ("app-nav", "d-nav-link", "default", "fontSize", type_scale, "dimension", "The dark shell's nav/button text."),
    ("app-meta", "d-sidebar", "default", "fontSize", type_scale, "dimension", "The dark shell's smallest label size."),
]:
    v = ts(comp, state, prop)
    if v:
        bag[key] = {"type": ty, "value": v,
                    "source": f"computed {prop} of {comp} {state} (raw/components-computed.json)",
                    "description": desc}

leading = SPEC["core"].setdefault("font", {}).setdefault("lineHeight", {})
for key, comp, state, desc in [
    ("display", "hero-title", "default", "Tight display leading (0.99x)."),
    ("h2", "section-h2", "default", "Tight heading leading."),
    ("nav", "nav-link", "default", "Nav link leading."),
]:
    v = ts(comp, state, "lineHeight")
    if v:
        leading[key] = {"type": "dimension", "value": v,
                        "source": f"computed lineHeight of {comp} {state} (raw/components-computed.json)",
                        "description": desc}

# ---------------------------------------------------------- radius, easing

radius = SPEC["core"].setdefault("radius", {})
for key, comp, state, prop, desc in [
    ("menu", "m-menu-button", "default", "borderTopLeftRadius", "The 5px menu-button radius."),
    ("nav-pill", "d-nav-link", "default", "borderTopLeftRadius", "The 12px dark nav-item pill and cursor badge."),
    ("control", "d-login", "default", "borderTopLeftRadius", "The 10px dark control radius (also the header CTA's painted layer)."),
    ("button", "hero-cta", "default", "paint-radius", "The 16px pill the button paint draws."),
    ("card", "d-card", "default", "borderTopLeftRadius", "The 32px card radius (plan cards and dark cards)."),
    ("tile", "d-block-card", "default", "borderTopLeftRadius", "The 42px dark tile radius."),
]:
    if prop == "paint-radius":
        try:
            pr = next((n.get("radius") for n in C[comp]["states"][state].get("paint", []) if n.get("radius") and n["radius"] != "0px"), None)
            if pr:
                radius[key] = {"value": pr, "type": "dimension",
                               "source": f"painted layer radius under {comp} {state} (raw/components-computed.json)",
                               "description": desc}
        except KeyError:
            pass
        continue
    if have(comp, state, prop):
        radius[key] = {"value": st(comp, state)[prop], "type": "dimension",
                       "source": f"computed {prop} of {comp} {state} (raw/components-computed.json)",
                       "description": desc}

easing = SPEC["core"].setdefault("easing", {})
for key, vname, desc in [
    ("out", "--butter-ease-out", "The declared ease-out curve."),
    ("in-out", "--butter-ease-in-out", "The declared ease-in-out curve."),
]:
    if vname in R:
        easing[key] = var(vname, "cubicBezier", description=desc)

# ---------------------------------------------------------------- measured

meas = SPEC["core"].setdefault("measured", {})
# the focus ring is drawn as a 1px box-shadow, not an outline
try:
    s = st("nav-cta", "focus-visible")
    if s.get("boxShadow") and s["boxShadow"] != "none":
        m = re.findall(r"(rgba?\([\d.,\s]+\)|#[0-9a-fA-F]{3,8})\s+(-?\d+(?:\.\d+)?px)\s+(-?\d+(?:\.\d+)?px)\s+(-?\d+(?:\.\d+)?px)\s+(-?\d+(?:\.\d+)?px)", s["boxShadow"])
        if m:
            meas["focus-ring"] = {"value": [{"color": norm_color(a), "offsetX": x, "offsetY": y, "blur": bl, "spread": sp} for a, x, y, bl, sp in m],
                                  "type": "shadow",
                                  "source": "computed boxShadow of nav-cta focus-visible (raw/components-computed.json)",
                                  "description": "The 1px #3c3c3c keyboard-focus ring every focused control draws as a zero-offset shadow."}
except KeyError:
    pass
for key, comp, state, prop, ty, desc in [
    ("card-border", "d-card", "default", "borderTopColor", "color", "The #212121 dark card border."),
    ("focus-outline", "hero-cta", "focus-visible", "child-outline", "color", "The 3px #4dc5e5 outline (offset 3px) a focused button's inner layer draws."),
]:
    if prop == "child-outline":
        try:
            outl = next((n.get("outline") for n in C[comp]["states"][state].get("paint", []) if n.get("outline")), None)
            if outl:
                m = re.search(r"(rgba?\([\d.,\s]+\)|#[0-9a-fA-F]{3,8})", outl)
                if m:
                    meas[key] = {"value": norm_color(m.group(1)), "type": ty,
                                 "source": f"painted outline under {comp} {state} (raw/components-computed.json)",
                                 "description": desc}
        except KeyError:
            pass
        continue
    if have(comp, state, prop):
        v = st(comp, state)[prop]
        if ty == "color":
            v = norm_color(v)
        meas[key] = {"value": v, "type": ty,
                     "source": f"computed {prop} of {comp} {state} (raw/components-computed.json)",
                     "description": desc}
for key, comp, state, desc in [
    ("control-transition", "d-login", "default", "The dark shell controls' 0.16s transition."),
    ("tile-transition", "d-block-card", "default", "The dark tile's transform/background transition."),
    ("fade-transition", "nav-trigger", "default", "The nav triggers' 0.5s opacity fade."),
    ("toggle-transition", "billing-toggle", "default", "The billing toggle's 0.5s colour/opacity change."),
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
# the dark card's hover shrinks it ~2%
try:
    d0 = C["d-card"]["states"]["default"]["rect"]["w"]
    dh = C["d-card"]["states"]["hover"]["rect"]["w"]
    if d0 and dh and dh < d0:
        meas["card-hover-scale"] = {"value": round(dh / d0, 4), "type": "number",
                                    "source": "hover rect / default rect of d-card (raw/components-computed.json)",
                                    "description": "The ~0.98 scale a dark card takes on hover."}
except KeyError:
    pass

# ------------------------------------------------------------------ component

comp = SPEC["component"]
for key, cname, state, prop, desc in [
    ("control.height", "hero-cta", "default", "height", "The marketing CTA height."),
    ("button.height", "nav-cta", "default", "height", "The header Try-for-free height."),
    ("plan-cta.height", "plan-cta", "default", "height", "The plan-card Choose-Pro height."),
    ("card.radius", "d-card", "default", "borderTopLeftRadius", "Card corner radius."),
    ("navlink.height", "d-nav-link", "default", "height", "A dark nav item's height."),
    ("sidebar.width", "d-sidebar", "default", "width", "The app-shell sidebar width."),
    ("header.height", "header", "default", "height", "The marketing header height."),
    ("header.height-mobile", "m-header", "default", "height", "The marketing header at 390px."),
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
