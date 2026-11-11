#!/usr/bin/env python3
"""Write raw/component-tokens.json, the token spec build_tokens.py reads.

bloomberg.com's news surface ("phoenix") is a CSS-module React app that
inlines its sheets; it declares almost no token layer — :root carries no
custom properties and the names that exist are component-scoped media-ui
vars or Tailwind internals (raw/css-vars.json, read by tools/capture/
vars.mjs). PerimeterX rate-limited this pass, so the harvest is thin and
every design token here is a measured computed value, not a var alias:

  chrome neutrals      logo bar / nav / ticker blacks and the page's
                       text/border greys -> core.color.neutral
  accents              the Subscribe blue, live red, gain/loss market
                       colours, paywall band -> core.color.brand /
                       core.color.market
  fonts                BWHaasGroteskWeb, AvenirNextPForBBG stacks ->
                       core.font.family
  scales               measured story/nav/field spacing and the component
                       metrics -> core.measured, component.*

A leaf is {"var": "--name"} (resolved per theme by build_tokens.py) or
{"value": ..., "source": "..."} for a measured value. The site paints one
light theme; the `dark` set is left empty so build_tokens.py emits core
and light only.
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
    "The token tree build_tokens.py turns into tokens.json. bloomberg.com "
    "declares almost no :root custom properties; its CSS-module values are "
    "inline, so the tree is built from measured computed styles on the "
    "running pages (raw/components-computed.json). Semantic roles land in "
    "the light set (the only theme the site paints)."),
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


# Names the site's own sheets declare (the `app` bin); PerimeterX throttled
# the harvest on this pass so it is empty and no --color-* ramp is exported.
APP = {n for r in V.get("app", []) for n in r.get("properties", [])}

# --------------------------------------------------------------- core ramps

for name in sorted(n for n in R if n.startswith("--color-") and n in APP):
    emit(SPEC["core"], name, var(name))

# ------------------------------------------------------------------- fonts

# The stacks are read from the measured components, not vars: body text and
# headlines run BWHaasGroteskWeb, UI labels run AvenirNextPForBBG.


def st(comp, state):
    return C[comp]["states"][state]["style"]


def ts(comp, state, prop):
    """The first text node's reading (textStyle) when the kit recorded one —
    the wrapper's own fontSize can be the container's, not the text's (the
    ticker wrapper reads 16px while its quote text paints at 14px)."""
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
    """First painted fill on or under the component: styleOf's `paint` lists the
    first nodes inside that paint a fill/border; `ancestors` the same outwards.
    Needed because the kit selects the wrapper while the fill sits on a child
    (the wp-ga-button anchor) or the parent chrome (the black logo bar)."""
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


def find_paint(comp, state, pred):
    """Every painted fill on/under the component, filtered by pred(rgb string)."""
    try:
        c = C[comp]["states"][state]
    except KeyError:
        return None
    for n in (c.get("paint") or []) + (c.get("ancestors") or []):
        bg = n.get("bg")
        if bg and pred(bg):
            return bg
    return None


def rgb_of(v):
    m = re.match(r"rgba?\(([\d.]+),\s*([\d.]+),\s*([\d.]+)", v or "")
    return (int(float(m.group(1))), int(float(m.group(2))), int(float(m.group(3)))) if m else None


def reddish(v):
    c = rgb_of(v)
    return bool(c and c[0] > c[1] + 60 and c[0] > c[2] + 60)


def lightgrey(v):
    c = rgb_of(v)
    return bool(c and 200 <= c[0] < 250 and abs(c[0] - c[1]) < 12 and abs(c[1] - c[2]) < 12)


fam = SPEC["core"].setdefault("font", {}).setdefault("family", {})
for key, comp, state, desc in [
    ("headline", "hero-headline", "default", "The headline stack (BWHaasHead first)."),
    ("ui", "nav-link", "default", "The UI/label stack (BWHaasGroteskWeb first)."),
    ("body", "dek", "default", "The body-text stack (BWHaasGroteskWeb first)."),
    ("utility", "utility-bar", "default", "The utility-strip stack (AvenirNextPForBBG first)."),
]:
    if have(comp, state, "fontFamily"):
        fam[key] = {"value": ts(comp, state, "fontFamily"), "type": "fontFamily",
                    "source": f"computed fontFamily of {comp} {state} (raw/components-computed.json)",
                    "description": desc}

# ------------------------------------------------------- measured colours

neutral = SPEC["core"].setdefault("color", {}).setdefault("neutral", {})
for key, comp, state, prop, desc in [
    ("ink", "hero-headline", "default", "color", "Headline text."),
    ("body", "dek", "default", "color", "Body text."),
    ("line", "ticker-bar", "default", "borderBottomColor", "The 1px hairline rails (the ticker rail's edges; utility separators share it)."),
    ("line-strong", "subscribe-nav", "default", "borderTopColor", "The darker border on bordered buttons."),
    ("paper", "plan-card", "default", "backgroundColor", "The white surface (page and cards)."),
    ("ticker", "ticker-pill", "default", "backgroundColor", "The near-black ticker chip fill."),
]:
    if have(comp, state, prop):
        v = norm_color(st(comp, state).get(prop, ""))
        if v and v != "transparent" and not v.startswith("rgba("):
            neutral[key] = {"value": v, "type": "color",
                            "source": f"computed {prop} of {comp} {state} (raw/components-computed.json)",
                            "description": desc}

# Painted fills that sit on a child or ancestor rather than the selected node.
for key, comp, state, desc in [
    ("chrome", "logo-bar", "default", "The black logo-bar / section-nav chrome."),
]:
    v = norm_color(painted(comp, state) or "")
    if v and v != "transparent" and not v.startswith("rgba("):
        neutral[key] = {"value": v, "type": "color",
                        "source": f"painted fill inside/under {comp} {state} (raw/components-computed.json)",
                        "description": desc}
# The light grey the Claim button repaints to on hover.
v = norm_color(find_paint("claim-offer", "hover", lightgrey) or "")
if v:
    neutral["smoke"] = {"value": v, "type": "color",
                        "source": "painted fill inside claim-offer hover (raw/components-computed.json)",
                        "description": "The light grey hover fill on the paywall's Claim button."}

brand = SPEC["core"].setdefault("color", {}).setdefault("brand", {})
for key, comp, state, prop, desc in [
    ("paywall", "paywall", "default", "backgroundColor", "The paywall band's dark fill."),
]:
    if have(comp, state, prop):
        v = norm_color(st(comp, state).get(prop, ""))
        if v and v != "transparent" and not v.startswith("rgba("):
            brand[key] = {"value": v, "type": "color",
                          "source": f"computed {prop} of {comp} {state} (raw/components-computed.json)",
                          "description": desc}
for key, comp, state, desc in [
    ("accent", "offer-cta", "default", "The Bloomberg CTA blue (offer Continue)."),
    ("accent-hover", "offer-cta", "hover", "CTA blue on hover."),
]:
    v = norm_color(painted(comp, state) or "")
    if v and v != "transparent" and not v.startswith("rgba("):
        brand[key] = {"value": v, "type": "color",
                      "source": f"painted fill inside {comp} {state} (raw/components-computed.json)",
                      "description": desc}

market = SPEC["core"].setdefault("color", {}).setdefault("market", {})
for key, comp, state, desc in [
    ("live", "section-nav", "default", "The Live TV red in the section nav."),
    ("live-strong", "live-paywall", "default", "The stronger live red on the player surface."),
]:
    v = norm_color(find_paint(comp, state, reddish) or "")
    if v:
        market[key] = {"value": v, "type": "color",
                       "source": f"painted fill inside {comp} {state} (raw/components-computed.json)",
                       "description": desc}

# -------------------------------------------------------------------- roles

light = SPEC["light"]
ALIAS = "role alias over the measured core palette"
if "ink" in neutral:
    emit(light, "--text-primary", {"value": "{color.neutral.ink}", "type": "color",
                                   "source": ALIAS, "description": "Body and headline text."})
    emit(light, "--surface-chrome", {"value": "{color.neutral.chrome}", "type": "color",
                                     "source": ALIAS, "description": "The black header chrome."})
if "paper" in neutral:
    emit(light, "--surface-page", {"value": "{color.neutral.paper}", "type": "color",
                                   "source": ALIAS, "description": "The page background."})
if "line" in neutral:
    emit(light, "--border-hairline", {"value": "{color.neutral.line}", "type": "color",
                                      "source": ALIAS, "description": "Story-block hairlines."})
if "accent" in brand:
    emit(light, "--action-primary", {"value": "{color.brand.accent}", "type": "color",
                                     "source": ALIAS, "description": "Primary CTAs (Continue, checkout)."})

# ------------------------------------------------------------- type scale

type_scale = SPEC["core"].setdefault("font", {}).setdefault("size", {})
leading = SPEC["core"].setdefault("font", {}).setdefault("lineHeight", {})
weight = SPEC["core"].setdefault("font", {}).setdefault("weight", {})
for key, comp, state, prop, bag, desc in [
    ("hero", "hero-headline", "default", "fontSize", type_scale, "The lead headline size."),
    ("hero", "hero-headline", "default", "lineHeight", leading, "Lead headline line height."),
    ("hero", "hero-headline", "default", "fontWeight", weight, "Lead headline weight."),
    ("title", "section-title", "default", "fontSize", type_scale, "A front-page module title."),
    ("body", "dek", "default", "fontSize", type_scale, "Story dek size."),
    ("body", "dek", "default", "lineHeight", leading, "Story dek line height."),
    ("label", "nav-link", "default", "fontSize", type_scale, "Nav label size."),
    ("label", "nav-link", "default", "fontWeight", weight, "Nav label weight."),
    ("caption", "byline", "default", "fontSize", type_scale, "Byline/caption size."),
    ("ticker", "ticker-item", "default", "fontSize", type_scale, "Ticker quote size."),
]:
    v = ts(comp, state, prop)
    if v:
        bag[key] = {
            "type": "number" if prop == "fontWeight" else "dimension",
            "value": v,
            "source": f"computed {prop} of {comp} {state} (raw/components-computed.json)",
            "description": desc}

# ---------------------------------------------------------- spacing/radius

meas = SPEC["core"].setdefault("measured", {})
for key, comp, state, prop, ty, desc in [
    ("gutter", "hero-story", "default", "paddingLeft", "dimension", "The front grid's gutter."),
    ("block-gap", "story-secondary", "default", "marginTop", "dimension", "Gap between story blocks."),
    ("focus-outline", "nav-link", "focus-visible", "outlineColor", "color", "The keyboard-focus ring on nav items."),
    ("button-hover", "subscribe-nav", "hover", "backgroundColor", "color", "The Subscribe button's hover fill."),
]:
    if have(comp, state, prop):
        v = st(comp, state)[prop]
        if ty == "color":
            v = norm_color(v)
        meas[key] = {"value": v, "type": ty,
                     "source": f"computed {prop} of {comp} {state} (raw/components-computed.json)",
                     "description": desc}

# ------------------------------------------------------------------ component

comp = SPEC["component"]
for key, cname, state, prop, desc in [
    ("control.height", "subscribe-nav", "default", "height", "The Subscribe button height."),
    ("control.radius", "subscribe-nav", "default", "borderTopLeftRadius", "Button corner radius."),
    ("control.fieldHeight", "signin-email", "default", "height", "The sign-in field height."),
    ("ticker.height", "ticker-item", "default", "height", "Ticker chip height."),
    ("header.height", "logo-bar", "default", "height", "The black logo bar height."),
    ("nav.height", "section-nav", "default", "height", "The section nav strip height."),
    ("paywall.padding", "paywall", "default", "paddingTop", "Paywall band vertical padding."),
    ("plan-card.radius", "plan-card", "default", "borderTopLeftRadius", "Plan card corner radius."),
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
