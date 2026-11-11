#!/usr/bin/env python3
"""Write raw/component-tokens.json, the token spec build_tokens.py reads.

busuu.com is a Bootstrap marketing front over a React styled-components app:
raw/css-vars.json (read by tools/capture/vars.mjs) is nearly empty — the site
declares almost no custom properties (compiled Sass + styled-components), so
every design token is a **measured computed value** from
raw/components-computed.json:

  neutrals    ink #252b2f, grey #666e7e, hairline #d6dee6, white, black text
  brand       green #11ee92/#41f1a8 CTAs, blue #116eee links, purple #5438dc
              premium buttons, indigo #221658 plan cards, mist #f2f7fd footer
  fonts       Nista (marketing) and NistaFonts (app pages) stacks
  ramp        measured 48/40/32/18/16/14 steps -> core.font.*
  shape       45px and 26px pills, 16px cards, 8px plan cards -> core.radius
  states      the green->light-green hover, #f3f8fe option hover, the 1px
              #005fcc focus ring -> core.measured

A leaf is {"var": "--name"} (resolved per theme by build_tokens.py) or
{"value": ..., "source": "..."} for a measured value. The site paints one
light theme; the `dark` set is left empty so build_tokens.py emits core and
light only.
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
    "The token tree build_tokens.py turns into tokens.json. busuu.com "
    "declares almost no custom properties (compiled Sass + styled-components), "
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
for key, comp, state, desc in [
    ("marketing", "hero-title", "default", "The marketing stack (Nista first)."),
    ("app", "course-title", "default", "The app-page stack (NistaFonts first)."),
    ("body", "hero-sub", "default", "Body/nav text (Nista first)."),
]:
    if have(comp, state, "fontFamily"):
        fam[key] = {"value": ts(comp, state, "fontFamily"), "type": "fontFamily",
                    "source": f"computed fontFamily of {comp} {state} (raw/components-computed.json)",
                    "description": desc}

# ------------------------------------------------------- measured colours

neutral = SPEC["core"].setdefault("color", {}).setdefault("neutral", {})
for key, comp, state, prop, desc in [
    ("ink", "register-title", "default", "color", "The near-black body ink (#252b2f)."),
    ("muted", "flag-card", "default", "color", "The grey meta text (#666e7e)."),
    ("line", "footer", "default", "color", "The footer select hairline sibling (#d6dee6 measured on the select)."),
]:
    if key == "line":
        v = norm_color("#d6dee6")
        neutral[key] = {"value": v, "type": "color",
                        "source": "computed borderTopColor of the footer language select (raw/components-computed.json footer paint)",
                        "description": desc}
        continue
    if have(comp, state, prop):
        v = norm_color(st(comp, state).get(prop, ""))
        if v and v != "transparent":
            neutral[key] = {"value": v, "type": "color",
                            "source": f"computed {prop} of {comp} {state} (raw/components-computed.json)",
                            "description": desc}
neutral["paper"] = {"value": "#ffffff", "type": "color",
                    "source": "body backgroundColor computes transparent; the canvas paints white (verified against the screenshots)",
                    "description": "The white page field."}

brand = SPEC["core"].setdefault("color", {}).setdefault("brand", {})
for key, comp, state, prop, desc in [
    ("green", "cta-signup", "default", "backgroundColor", "The Busuu green on every Learn-for-free CTA."),
    ("green-hover", "cta-signup", "hover", "backgroundColor", "The green's lighter hover."),
    ("blue", "language-item", "default", "color", "The action/link blue #116eee (option text, course-cta text, hover borders)."),
    ("purple", "plan-cta", "default", "color", "The Premium purple #5438dc on button text/borders."),
]:
    if have(comp, state, prop):
        v = norm_color(st(comp, state).get(prop, ""))
        if v and v != "transparent":
            brand[key] = {"value": v, "type": "color",
                          "source": f"computed {prop} of {comp} {state} (raw/components-computed.json)",
                          "description": desc}
def ancestor_fill(comp, state):
    """The band fill painted by a component's ancestor (the footer band lives
    on .main-footer; the footer root's own children paint only the social-icon
    circles)."""
    try:
        c = C[comp]["states"][state]
    except KeyError:
        return None
    for n in c.get("ancestors") or []:
        if n.get("bg"):
            return n["bg"]
    return None


for key, comp, state, desc in [
    ("indigo", "plan-card", "default", "The deep indigo #221658 plan-card fill."),
]:
    v = norm_color(painted(comp, state) or "")
    if v and v != "transparent" and not v.startswith("rgba("):
        brand[key] = {"value": v, "type": "color",
                      "source": f"painted fill of {comp} {state} (raw/components-computed.json)",
                      "description": desc}
# indigo is on the element itself, not a paint layer
if "indigo" not in brand and have("plan-card", "default", "backgroundColor"):
    v = norm_color(st("plan-card", "default")["backgroundColor"])
    if v and v != "transparent":
        brand["indigo"] = {"value": v, "type": "color",
                           "source": "computed backgroundColor of plan-card (raw/components-computed.json)",
                           "description": "The deep indigo #221658 plan-card fill."}
# The footer band: the footer root computes transparent; div.main-footer (the
# recorded ancestor) paints #f2f7fd. The #a7b0b7 social-icon circles inside it
# are a separate paint, so a painted()-child read would return the icon grey.
v = norm_color(ancestor_fill("footer", "default") or "")
if v and v != "transparent" and not v.startswith("rgba("):
    brand["mist"] = {"value": v, "type": "color",
                     "source": "painted backgroundColor of the footer ancestor div.main-footer (raw/components-computed.json footer ancestors)",
                     "description": "The pale blue #f2f7fd footer fill. The #a7b0b7 social-icon circles inside it are a separate paint."}

# -------------------------------------------------------------------- roles

light = SPEC["light"]
ALIAS = "role alias over the measured core palette"
if "ink" in neutral:
    emit(light, "--text-primary", {"value": "{color.neutral.ink}", "type": "color",
                                   "source": ALIAS, "description": "Body and heading ink."})
if "muted" in neutral:
    emit(light, "--text-muted", {"value": "{color.neutral.muted}", "type": "color",
                                 "source": ALIAS, "description": "Meta and secondary text."})
if "blue" in brand:
    emit(light, "--text-accent", {"value": "{color.brand.blue}", "type": "color",
                                  "source": ALIAS, "description": "Links and inline accents."})
if "paper" in neutral:
    emit(light, "--surface-page", {"value": "{color.neutral.paper}", "type": "color",
                                   "source": ALIAS, "description": "The white page field."})
if "mist" in brand:
    emit(light, "--surface-mist", {"value": "{color.brand.mist}", "type": "color",
                                   "source": ALIAS, "description": "The pale-blue footer field."})
if "indigo" in brand:
    emit(light, "--surface-inverse", {"value": "{color.brand.indigo}", "type": "color",
                                      "source": ALIAS, "description": "The indigo plan-card fill."})
if "green" in brand:
    emit(light, "--action-primary", {"value": "{color.brand.green}", "type": "color",
                                     "source": ALIAS, "description": "The green Learn-for-free CTAs."})
if "line" in neutral:
    emit(light, "--border-field", {"value": "{color.neutral.line}", "type": "color",
                                   "source": ALIAS, "description": "The form field hairline."})
if "blue" in brand:
    emit(light, "--border-hover", {"value": "{color.brand.blue}", "type": "color",
                                   "source": "the measured 1px hover border on language options",
                                   "description": "The blue border a selectable option takes on hover."})

# ------------------------------------------------------------- type scale

type_scale = SPEC["core"].setdefault("font", {}).setdefault("size", {})
leading = SPEC["core"].setdefault("font", {}).setdefault("lineHeight", {})
weight = SPEC["core"].setdefault("font", {}).setdefault("weight", {})
for key, comp, state, prop, bag, ty, desc in [
    ("display", "course-title", "default", "fontSize", type_scale, "dimension", "The course-page display size."),
    ("hero", "hero-title", "default", "fontSize", type_scale, "dimension", "The home hero size."),
    ("title", "register-title", "default", "fontSize", type_scale, "dimension", "The signup/page title size."),
    ("subtitle", "premium-title", "default", "fontSize", type_scale, "dimension", "The Premium page title."),
    ("price", "plan-price", "default", "fontSize", type_scale, "dimension", "Plan price size."),
    ("body", "hero-sub", "default", "fontSize", type_scale, "dimension", "Body/lede size."),
    ("nav", "nav-dropdown", "default", "fontSize", type_scale, "dimension", "Nav link size."),
    ("meta", "footer-link", "default", "fontSize", type_scale, "dimension", "Footer/meta size."),
    ("cta", "cta-signup", "default", "fontSize", type_scale, "dimension", "CTA label size."),
    ("mobile-display", "m-hero", "default", "fontSize", type_scale, "dimension", "The hero at 390px."),
]:
    v = ts(comp, state, prop)
    if v:
        bag[key] = {"type": ty, "value": v,
                    "source": f"computed {prop} of {comp} {state} (raw/components-computed.json)",
                    "description": desc}

# ---------------------------------------------------------- radius, extras

radius = SPEC["core"].setdefault("radius", {})
for key, comp, state, prop, desc in [
    ("pill", "cta-signup", "default", "borderTopLeftRadius", "The ~45px pill on the green CTAs."),
    ("button", "plan-cta", "default", "borderTopLeftRadius", "The ~26px pill on Premium buttons."),
    ("card", "flag-card", "default", "borderTopLeftRadius", "The 16px language-card radius."),
    ("panel", "plan-card", "default", "borderTopLeftRadius", "The 8px plan-card radius."),
]:
    if have(comp, state, prop):
        radius[key] = {"value": st(comp, state)[prop], "type": "dimension",
                       "source": f"computed {prop} of {comp} {state} (raw/components-computed.json)",
                       "description": desc}

shadow = SPEC["core"].setdefault("shadow", {})
try:
    sh = st("cta-signup", "default")["boxShadow"]
    if sh and sh != "none":
        m = re.findall(r"(rgba?\([\d.,\s]+\)|#[0-9a-fA-F]{3,8})\s+(-?\d+(?:\.\d+)?px)\s+(-?\d+(?:\.\d+)?px)\s+(-?\d+(?:\.\d+)?px)\s+(-?\d+(?:\.\d+)?px)", sh)
        if m:
            shadow["cta"] = {"value": [{"color": norm_color(a), "offsetX": x, "offsetY": y, "blur": bl, "spread": sp} for a, x, y, bl, sp in m],
                             "type": "shadow",
                             "source": "computed boxShadow of cta-signup (raw/components-computed.json)",
                             "description": "The green CTA's resting shadow."}
except KeyError:
    pass

meas = SPEC["core"].setdefault("measured", {})
for key, comp, state, prop, ty, desc in [
    ("focus-outline", "footer-link", "focus-visible", "outlineColor", "color", "The 1px keyboard-focus ring."),
    ("option-hover-border", "language-item", "hover", "borderTopColor", "color", "The blue border a language option takes on hover."),
]:
    if have(comp, state, prop):
        v = st(comp, state)[prop]
        if ty == "color":
            v = norm_color(v)
        meas[key] = {"value": v, "type": ty,
                     "source": f"computed {prop} of {comp} {state} (raw/components-computed.json)",
                     "description": desc}
# The option hover fill: the option's own box stays transparent in every
# state; the painted label child (p.sc-hCPjZK) carries the #f3f8fe wash.
v = norm_color(painted("language-item", "hover") or "")
if v and v != "transparent" and not v.startswith("rgba("):
    meas["option-hover-fill"] = {"value": v, "type": "color",
                                 "source": "computed backgroundColor of language-item hover's painted label child (raw/components-computed.json; the option's own box stays transparent)",
                                 "description": "The pale-blue hover fill inside a language option."}
for key, comp, state, desc in [
    ("cta-transition", "cta-signup", "default", "The green CTA's 0.2s transition."),
    ("card-transition", "flag-card", "default", "The language card's 0.15s transition."),
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
    ("control.height", "cta-signup", "default", "height", "The Learn-for-free CTA height."),
    ("control.radius", "cta-signup", "default", "borderTopLeftRadius", "CTA pill radius."),
    ("button.height", "plan-cta", "default", "height", "The Get Premium button height."),
    ("card.radius", "plan-card", "default", "borderTopLeftRadius", "Plan-card corner radius."),
    ("option.height", "language-item", "default", "height", "A language option's height."),
    ("header.height", "nav-dropdown", "default", "height", "The nav bar height."),
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
