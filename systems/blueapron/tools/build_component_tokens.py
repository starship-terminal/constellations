#!/usr/bin/env python3
"""Write raw/component-tokens.json, the token spec build_tokens.py reads.

blog.blueapron.com is a Squarespace 7.1 site ("Extra Helpings"), so it has a
real declared token layer: raw/css-vars.json (read by tools/capture/vars.mjs)
holds the site's palette and type vars — the accent blue #2959e0
(--sqsp-palette-accent-color), the navy #002856 dark accent, the cream
#f2f0e5 page field, a 64/44.8/35.2/25.6px heading ramp and the Ovo/Almarai
font vars. Where a token maps to a declared name the spec uses a `var` leaf;
everything else is a measured computed value from
raw/components-computed.json:

  palette            accent/navy/cream + the measured neutrals
                     -> core.color.brand / core.color.neutral
  fonts              Ovo display, Ivory serif (custom.css override on h1-h4),
                     Almarai text -> core.font.family
  type ramp          declared --heading-*-size vars + measured sizes
                     -> core.font.size / lineHeight / weight
  pills              300px radii on every button; the 65px CTA height
                     -> core.radius, component.*
  states             2px black (white on navy) focus rings, the secondary
                     button's transparent -> accent hover fill -> core.measured

A leaf is {"var": "--name"} (resolved per theme by build_tokens.py) or
{"value": ..., "source": "..."} for a measured value. The site paints one
light theme (with a dark-bold footer section); the `dark` set is left empty
so build_tokens.py emits core and light only.
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
    "The token tree build_tokens.py turns into tokens.json. blog.blueapron.com "
    "is Squarespace, so declared names (var leaves) cover the palette and the "
    "type ramp where they exist; measured computed styles on the running "
    "pages (raw/components-computed.json) cover everything else. Semantic "
    "roles land in the light set (the only theme the site paints)."),
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
    """First painted fill on or under the component (the fill sits on a child
    or the section chrome, not the selected node)."""
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
    ("display", "article-title", "default", "The display serif on headlines and card titles (Ovo first)."),
    ("serif", "faq-heading", "default", "The editorial serif custom.css puts on h1-h4 (Ivory first)."),
    ("body", "article-body", "default", "The body/nav text stack (Almarai first)."),
    ("announce", "announcement-bar", "default", "The announcement-bar stack (Almarai first)."),
]:
    if have(comp, state, "fontFamily"):
        fam[key] = {"value": ts(comp, state, "fontFamily"), "type": "fontFamily",
                    "source": f"computed fontFamily of {comp} {state} (raw/components-computed.json)",
                    "description": desc}

# ------------------------------------------------------- measured colours

neutral = SPEC["core"].setdefault("color", {}).setdefault("neutral", {})
for key, comp, state, prop, desc in [
    ("ink", "article-body", "default", "color", "Body text."),
    ("line", "search-field", "default", "borderTopColor", "The 1px field hairline."),
    ("white", "header-cta", "default", "color", "Text on accent/navy fills."),
]:
    if have(comp, state, prop):
        v = norm_color(st(comp, state).get(prop, ""))
        if v and v != "transparent" and not v.startswith("rgba("):
            neutral[key] = {"value": v, "type": "color",
                            "source": f"computed {prop} of {comp} {state} (raw/components-computed.json)",
                            "description": desc}

brand = SPEC["core"].setdefault("color", {}).setdefault("brand", {})
# Declared palette names where the site has them; measured fills for the rest.
if "--sqsp-palette-accent-color" in R:
    brand["accent"] = var("--sqsp-palette-accent-color",
                          description="The Blue Apron action blue: CTAs, links, headline accents.")
if "--announcement-bar-background-color" in R:
    brand["navy"] = var("--announcement-bar-background-color",
                        description="The deep navy of the announcement bar and the dark-bold footer sections.")
for key, comp, state, desc in [
    ("cream", "cart-page", "default", "The cream page field (#f2f0e5)."),
]:
    v = norm_color(painted(comp, state) or "")
    if v and v != "transparent" and not v.startswith("rgba("):
        brand[key] = {"value": v, "type": "color",
                      "source": f"painted fill inside {comp} {state} (raw/components-computed.json)",
                      "description": desc}
# The navy fill the footer section paints is the same --darkAccent; confirm by measurement.
v = norm_color(painted("footer", "default") or "")
if v and v != "transparent" and not v.startswith("rgba(") and "navy" not in brand:
    brand["navy"] = {"value": v, "type": "color",
                     "source": "painted fill of the footer section (raw/components-computed.json)",
                     "description": "The deep navy footer field."}

# -------------------------------------------------------------------- roles

light = SPEC["light"]
ALIAS = "role alias over the measured core palette"
if "ink" in neutral:
    emit(light, "--text-primary", {"value": "{color.neutral.ink}", "type": "color",
                                   "source": ALIAS, "description": "Body and UI text."})
    emit(light, "--focus-ring", {"value": "{color.neutral.ink}", "type": "color",
                                 "source": "the measured 2px focus outline on light surfaces",
                                 "description": "The keyboard-focus ring on light surfaces."})
if "white" in neutral:
    emit(light, "--text-inverse", {"value": "{color.neutral.white}", "type": "color",
                                   "source": ALIAS, "description": "Text on accent/navy fills."})
    emit(light, "--focus-ring-inverse", {"value": "{color.neutral.white}", "type": "color",
                                         "source": "the measured 2px focus outline on the navy announcement bar",
                                         "description": "The keyboard-focus ring on navy fills."})
if "accent" in brand:
    emit(light, "--text-accent", {"value": "{color.brand.accent}", "type": "color",
                                  "source": ALIAS, "description": "Links and headline accents."})
    emit(light, "--action-primary", {"value": "{color.brand.accent}", "type": "color",
                                     "source": ALIAS, "description": "Primary CTAs (Shop Now, Learn more hover)."})
if "cream" in brand:
    emit(light, "--surface-page", {"value": "{color.brand.cream}", "type": "color",
                                   "source": ALIAS, "description": "The cream page field."})
if "navy" in brand:
    emit(light, "--surface-inverse", {"value": "{color.brand.navy}", "type": "color",
                                      "source": ALIAS, "description": "Announcement bar and dark-bold footer."})
if "line" in neutral:
    emit(light, "--border-field", {"value": "{color.neutral.line}", "type": "color",
                                   "source": ALIAS, "description": "The 1px search-field border."})

# ------------------------------------------------------------- type scale

type_scale = SPEC["core"].setdefault("font", {}).setdefault("size", {})
leading = SPEC["core"].setdefault("font", {}).setdefault("lineHeight", {})
weight = SPEC["core"].setdefault("font", {}).setdefault("weight", {})
# Declared ramp where the site has it.
for key, name, desc in [
    ("h1", "--heading-1-size", "The declared h1 step."),
    ("h2", "--heading-2-size", "The declared h2 step."),
    ("h3", "--heading-3-size", "The declared h3 step."),
    ("h4", "--heading-4-size", "The declared h4 step."),
    ("base", "--base-font-size", "The declared body size."),
]:
    if name in R:
        type_scale[key] = var(name, "dimension", description=desc)
# Measured steps the declared ramp does not name.
for key, comp, state, prop, bag, ty, desc in [
    ("display", "article-title", "default", "fontSize", type_scale, "dimension", "The guide headline size at 1440."),
    ("display", "article-title", "default", "lineHeight", leading, "dimension", "Guide headline line height."),
    ("display", "article-title", "default", "fontWeight", weight, "number", "Guide headline weight."),
    ("title", "card-title", "default", "fontSize", type_scale, "dimension", "The blog card title size."),
    ("title", "card-title", "default", "lineHeight", leading, "dimension", "Card title line height."),
    ("small", "card-excerpt", "default", "fontSize", type_scale, "dimension", "The excerpt/small size."),
    ("small", "card-excerpt", "default", "lineHeight", leading, "dimension", "Excerpt line height."),
    ("announce", "announcement-bar", "default", "fontSize", type_scale, "dimension", "Announcement text size."),
    ("announce", "announcement-bar", "default", "fontWeight", weight, "number", "Announcement text weight."),
    ("nav", "nav-link", "default", "fontSize", type_scale, "dimension", "Nav link size."),
    ("nav", "nav-link", "default", "lineHeight", leading, "dimension", "Nav link line height."),
    ("meta", "card-meta", "default", "fontSize", type_scale, "dimension", "Card meta (date/author) size."),
    ("menu", "m-nav-item", "default", "fontSize", type_scale, "dimension", "The mobile menu's big nav size."),
]:
    v = ts(comp, state, prop)
    if v:
        bag[key] = {"type": ty, "value": v,
                    "source": f"computed {prop} of {comp} {state} (raw/components-computed.json)",
                    "description": desc}

# ---------------------------------------------------------- radius, extras

radius = SPEC["core"].setdefault("radius", {})
for key, comp, state, prop, desc in [
    ("pill", "header-cta", "default", "borderTopLeftRadius", "The 300px pill on every button."),
]:
    if have(comp, state, prop):
        radius[key] = {"value": st(comp, state)[prop], "type": "dimension",
                       "source": f"computed {prop} of {comp} {state} (raw/components-computed.json)",
                       "description": desc}

meas = SPEC["core"].setdefault("measured", {})
for key, comp, state, prop, ty, desc in [
    ("focus-outline", "nav-link", "focus-visible", "outlineColor", "color", "The 2px keyboard ring on light surfaces."),
    ("focus-outline-inverse", "announcement-close", "focus-visible", "outlineColor", "color", "The 2px keyboard ring on navy."),
    ("secondary-hover", "button-secondary", "hover", "backgroundColor", "color", "The secondary button's hover fill (transparent -> accent)."),
    ("field-border", "search-field", "default", "borderTopColor", "color", "The 1px search-field border."),
]:
    if have(comp, state, prop):
        v = st(comp, state)[prop]
        if ty == "color":
            v = norm_color(v)
        meas[key] = {"value": v, "type": ty,
                     "source": f"computed {prop} of {comp} {state} (raw/components-computed.json)",
                     "description": desc}
# Transitions measured on components.
for key, comp, state, desc in [
    ("cta-transition", "header-cta", "default", "The CTA's 0.1s opacity fade."),
    ("menu-transition", "m-nav-item", "default", "The mobile menu's 0.25s fade."),
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
    ("control.height", "header-cta", "default", "height", "The Shop Now CTA height."),
    ("control.radius", "header-cta", "default", "borderTopLeftRadius", "Button corner radius (300px pill)."),
    ("control.padding", "header-cta", "default", "paddingLeft", "CTA horizontal padding."),
    ("field.height", "search-field", "default", "height", "The search field height."),
    ("announcement.height", "announcement-bar", "default", "height", "The navy announcement strip height."),
    ("header.height", "header", "default", "height", "The header height (announcement + bar)."),
    ("card-image.radius", "card-image", "default", "borderTopLeftRadius", "Blog card image corner radius."),
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
