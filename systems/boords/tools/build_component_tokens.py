#!/usr/bin/env python3
"""Write raw/component-tokens.json, the token spec build_tokens.py reads.

boords.com is a Next.js/Tailwind app: raw/css-vars.json (read by
tools/capture/vars.mjs) shows a thin declared layer — the names that exist are
Tailwind internals and component-scoped vars — so every design token here is a
**measured computed value** from raw/components-computed.json:

  neutrals    ink #121212, body rgba(18,18,18,.6), muted #7b7b7b, line
              rgba(18,18,18,.15), paper #fff, cream card #f3f3e9
              -> core.color.neutral
  accents     amber #e8aa42/#d89b3c CTA borders, ink-outlined plan CTAs,
              dark footer fill -> core.color.brand
  fonts       the matter stack -> core.font.family
  ramp        measured display/title/body/nav/meta sizes -> core.font.*
  shape       9999px pills, 24px card radius, 16px media radius
              -> core.radius, component.*
  states      1px #005fcc focus rings, hover fills -> core.measured

A leaf is {"var": "--name"} (resolved per theme by build_tokens.py) or
{"value": ..., "source": "..."} for a measured value. The site paints one
light theme; the `dark` set is left empty so build_tokens.py emits core and
light only.
"""
import json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
V = json.loads((RAW / "css-vars.json").read_text())
RL = V["resolved"]["light"]
C = json.loads((RAW / "components-computed.json").read_text())["components"]
R = {n: v.get("value", v.get("raw")) for n, v in RL.items()}


def var(name, ty="color", **kw):
    d = {"var": name, "type": ty}
    d.update(kw)
    return d


SPEC = {"_about": (
    "The token tree build_tokens.py turns into tokens.json. boords.com "
    "declares almost no :root design vars; its Tailwind values are compiled, "
    "so the tree is built from measured computed styles on the running pages "
    "(raw/components-computed.json). Semantic roles land in the light set "
    "(the only theme the site paints)."),
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


APP = {n for r in V.get("app", []) for n in r.get("properties", [])}


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
    m = re.fullmatch(r"rgba?\((\d+(?:\.\d+)?),\s*(\d+(?:\.\d+)?),\s*(\d+(?:\.\d+)?)(?:,\s*([\d.]+))?\)", v)
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
for key, comp, state, desc in [
    ("body", "hero-sub", "default", "The single matter stack used everywhere."),
    ("display", "hero-title", "default", "The matter stack at display size."),
]:
    if have(comp, state, "fontFamily"):
        fam[key] = {"value": ts(comp, state, "fontFamily"), "type": "fontFamily",
                    "source": f"computed fontFamily of {comp} {state} (raw/components-computed.json)",
                    "description": desc}

# ------------------------------------------------------- measured colours

neutral = SPEC["core"].setdefault("color", {}).setdefault("neutral", {})
for key, comp, state, prop, desc in [
    ("ink", "hero-title", "default", "color", "Headline/button ink (#121212)."),
    ("body", "nav-link", "default", "color", "Nav/body text at 60% ink."),
    ("muted", "hero-sub", "default", "color", "The grey lede/meta text."),
    ("line", "timer-toggle", "default", "borderTopColor", "The 1px hairline on toggles/cards."),
    ("paper", "plan-card", "default", "backgroundColor", "The white page/card field."),
]:
    if have(comp, state, prop):
        v = norm_color(st(comp, state).get(prop, ""))
        if v and v != "transparent":
            neutral[key] = {"value": v, "type": "color",
                            "source": f"computed {prop} of {comp} {state} (raw/components-computed.json)",
                            "description": desc}
v = norm_color(painted("feature-card", "default") or "")
if v and v != "transparent" and not v.startswith("rgba("):
    neutral["cream"] = {"value": v, "type": "color",
                        "source": "painted fill of feature-card (raw/components-computed.json)",
                        "description": "The #f3f3e9 cream section/card fill."}

brand = SPEC["core"].setdefault("color", {}).setdefault("brand", {})
for key, comp, state, prop, desc in [
    ("amber", "hero-cta", "default", "borderTopColor", "The amber CTA border (the hero action)."),
    ("amber-hover", "hero-cta", "hover", "borderTopColor", "Amber border on hover."),
]:
    if have(comp, state, prop):
        v = norm_color(st(comp, state).get(prop, ""))
        if v and v != "transparent":
            brand[key] = {"value": v, "type": "color",
                          "source": f"computed {prop} of {comp} {state} (raw/components-computed.json)",
                          "description": desc}
v = norm_color(painted("footer", "default") or "")
if v and v != "transparent" and not v.startswith("rgba("):
    brand["ink"] = {"value": v, "type": "color",
                    "source": "painted fill of the footer (raw/components-computed.json)",
                    "description": "The near-black footer fill."}

# -------------------------------------------------------------------- roles

light = SPEC["light"]
ALIAS = "role alias over the measured core palette"
if "ink" in neutral:
    emit(light, "--text-primary", {"value": "{color.neutral.ink}", "type": "color",
                                   "source": ALIAS, "description": "Headline and button ink."})
if "body" in neutral:
    emit(light, "--text-secondary", {"value": "{color.neutral.body}", "type": "color",
                                     "source": ALIAS, "description": "Nav and body text."})
if "muted" in neutral:
    emit(light, "--text-muted", {"value": "{color.neutral.muted}", "type": "color",
                                 "source": ALIAS, "description": "Lede and meta text."})
if "paper" in neutral:
    emit(light, "--surface-page", {"value": "{color.neutral.paper}", "type": "color",
                                   "source": ALIAS, "description": "The white page field."})
if "cream" in neutral:
    emit(light, "--surface-card", {"value": "{color.neutral.cream}", "type": "color",
                                   "source": ALIAS, "description": "The cream section/card fill."})
if "ink" in brand:
    emit(light, "--surface-inverse", {"value": "{color.brand.ink}", "type": "color",
                                      "source": ALIAS, "description": "The near-black footer fill."})
if "amber" in brand:
    emit(light, "--action-outline", {"value": "{color.brand.amber}", "type": "color",
                                     "source": ALIAS, "description": "The amber outlined-CTA border."})
if "line" in neutral:
    emit(light, "--border-hairline", {"value": "{color.neutral.line}", "type": "color",
                                      "source": ALIAS, "description": "The 1px toggle/card hairline."})

# ------------------------------------------------------------- type scale

type_scale = SPEC["core"].setdefault("font", {}).setdefault("size", {})
leading = SPEC["core"].setdefault("font", {}).setdefault("lineHeight", {})
weight = SPEC["core"].setdefault("font", {}).setdefault("weight", {})
for key, comp, state, prop, bag, ty, desc in [
    ("display", "hero-title", "default", "fontSize", type_scale, "dimension", "The page/hero display size."),
    ("display", "hero-title", "default", "lineHeight", leading, "dimension", "Display line height."),
    ("display", "hero-title", "default", "fontWeight", weight, "number", "Display weight."),
    ("cta", "hero-cta", "default", "fontSize", type_scale, "dimension", "Hero CTA size."),
    ("body", "timer-field", "default", "fontSize", type_scale, "dimension", "Field/body size."),
    ("nav", "nav-link", "default", "fontSize", type_scale, "dimension", "Nav/footer label size."),
    ("nav", "nav-link", "default", "fontWeight", weight, "number", "Nav label weight."),
    ("meta", "footer-link", "default", "fontSize", type_scale, "dimension", "Small footer/meta size."),
    ("price", "plan-price", "default", "fontSize", type_scale, "dimension", "Plan price size."),
    ("price", "plan-price", "default", "fontWeight", weight, "number", "Plan price weight."),
]:
    v = ts(comp, state, prop)
    if v:
        bag[key] = {"type": ty, "value": v,
                    "source": f"computed {prop} of {comp} {state} (raw/components-computed.json)",
                    "description": desc}

# ---------------------------------------------------------- radius, extras

radius = SPEC["core"].setdefault("radius", {})
for key, comp, state, prop, desc in [
    ("pill", "cta-demo", "default", "borderTopLeftRadius", "The 9999px pill on header buttons/CTAs."),
    ("card", "plan-card", "default", "borderTopLeftRadius", "The 24px card radius."),
    ("media", "timer-toggle", "default", "borderTopLeftRadius", "The 16px media/inner radius."),
]:
    if have(comp, state, prop):
        radius[key] = {"value": st(comp, state)[prop], "type": "dimension",
                       "source": f"computed {prop} of {comp} {state} (raw/components-computed.json)",
                       "description": desc}

shadow = SPEC["core"].setdefault("shadow", {})
for key, comp, state, desc in [
    ("card", "plan-card", "default", "A plan card's resting shadow."),
    ("header", "header", "default", "The floating header pill's shadow."),
]:
    try:
        sh = st(comp, state)["boxShadow"]
        if sh and sh != "none" and not sh.startswith("rgba(0, 0, 0, 0)"):
            m = re.findall(r"(rgba?\([\d.,\s]+\)|#[0-9a-fA-F]{3,8})\s+(-?\d+(?:\.\d+)?px)\s+(-?\d+(?:\.\d+)?px)\s+(-?\d+(?:\.\d+)?px)\s+(-?\d+(?:\.\d+)?px)", sh)
            if m:
                layers = [{"color": norm_color(a), "offsetX": x, "offsetY": y, "blur": bl, "spread": sp}
                          for a, x, y, bl, sp in m]
                shadow[key] = {"value": layers, "type": "shadow",
                               "source": f"computed boxShadow of {comp} {state} (raw/components-computed.json)",
                               "description": desc}
    except KeyError:
        pass

meas = SPEC["core"].setdefault("measured", {})
for key, comp, state, prop, ty, desc in [
    ("focus-outline", "nav-link", "focus-visible", "outlineColor", "color", "The keyboard-focus ring on nav/footer links."),
    ("hover-dim", "cta-demo", "hover", "backgroundColor", "color", "The 5% ink hover fill on header buttons."),
    ("toggle-border", "timer-toggle", "default", "borderTopColor", "color", "The toggle hairline."),
]:
    if have(comp, state, prop):
        v = st(comp, state)[prop]
        if ty == "color":
            v = norm_color(v)
        meas[key] = {"value": v, "type": ty,
                     "source": f"computed {prop} of {comp} {state} (raw/components-computed.json)",
                     "description": desc}
for key, comp, state, desc in [
    ("cta-transition", "hero-cta", "default", "The CTA's 0.15s ease transition."),
    ("nav-transition", "nav-link", "default", "The nav's 0.2s ease transition."),
]:
    try:
        s = st(comp, state)
        d = s["transitionDuration"]
        if d and d != "0s" and "," not in d:
            meas[key] = {"value": d, "type": "duration",
                         "source": f"computed transition of {comp} {state} (raw/components-computed.json)",
                         "description": desc + f" ({s['transitionProperty']})"}
    except (KeyError, TypeError):
        pass

# ------------------------------------------------------------------ component

comp = SPEC["component"]
for key, cname, state, prop, desc in [
    ("control.height", "cta-demo", "default", "height", "The header CTA height."),
    ("control.radius", "cta-demo", "default", "borderTopLeftRadius", "Header pill radius."),
    ("cta.height", "hero-cta", "default", "height", "The hero CTA height."),
    ("header.height", "header", "default", "height", "The floating header height."),
    ("field.radius", "timer-field", "default", "borderTopLeftRadius", "The script textarea radius."),
    ("field.border", "timer-toggle", "default", "borderTopWidth", "Toggle border width."),
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
