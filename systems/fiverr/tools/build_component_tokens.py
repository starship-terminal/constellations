#!/usr/bin/env python3
"""Write raw/component-tokens.json, the token spec build_tokens.py reads.

fiverr.com is a React app styled with atomic hashed classes (_1xeo152 …): its
served sheets declare ~1,290 custom properties on :root, all named by content
hash (raw/css-vars.json, read by tools/capture/vars.mjs) — a token-free layer
with no semantic names to alias, plus the Macan @font-face rules and
scattered component/vendor vars. Every design token here is therefore a
measured computed value read off the running pages
(raw/components-computed.json), never a var alias:

  brand colours      the dark action fills (Join, the search submit,
                     Continue) and the fiverr green accent -> core.color.brand
  dark band          the hero/search-form dark skin -> core.color.dark
  chrome neutrals    text ink, muted ink, hairlines, the white page and the
                     off-white section surface -> core.color.neutral
  fonts              the Macan stack and fallbacks -> core.font.family
  scales             measured type steps, control spacing, radii and the
                     component metrics -> core.font.*, core.measured,
                     component.*

A leaf is {"var": "--name"} (resolved per theme by build_tokens.py — unused
this pass) or {"value": ..., "source": "..."} for a measured value. The site
paints one light theme; the `dark` set is left empty so build_tokens.py emits
core and light only.

Deterministic: same inputs, byte-identical output.
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
    "The token tree build_tokens.py turns into tokens.json. fiverr.com's "
    "sheets declare ~1,290 custom properties on :root, all named by "
    "content hash — a token-free layer with no semantic names to alias — "
    "so the tree is built from measured computed styles on the "
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


APP = {n for r in V.get("app", []) for n in r.get("properties", [])}


def st(comp, state):
    return C[comp]["states"][state]["style"]


def ts(comp, state, prop):
    """The first text node's reading (textStyle) when the kit recorded one —
    the wrapper's own font can be the container's, not the text's."""
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
        # A state recorded as failed (via: "focus failed" — the element would
        # not hold a real keyboard focus) is not a reading of that state: a
        # focus-ring token must never be sourced from an unfocused style.
        if C[comp]["states"][state].get("via") == "focus failed":
            return False
        s = st(comp, state)
        return prop is None or bool((s.get(prop) or "").strip())
    except KeyError:
        return False


def painted(comp, state):
    """First painted fill on or under the component: styleOf's `paint` lists the
    first nodes inside that paint a fill/border; `ancestors` the same outwards.
    Needed because the kit selects the wrapper while the fill sits on a child
    or a parent."""
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


def greenish(v):
    c = rgb_of(v)
    return bool(c and c[1] > c[0] + 30 and c[1] > c[2] + 30 and c[1] > 120)


def lightgrey(v):
    c = rgb_of(v)
    return bool(c and 200 <= c[0] < 250 and abs(c[0] - c[1]) < 12 and abs(c[1] - c[2]) < 12)


# -------------------------------------------------------------------- fonts

fam = SPEC["core"].setdefault("font", {}).setdefault("family", {})
for key, comp, state, desc in [
    ("sans", "hero-h1", "default", "The Macan headline stack."),
    ("body", "section-h2", "default", "The body/section stack."),
    ("ui", "nav-join", "default", "The UI/control stack."),
]:
    if have(comp, state, "fontFamily"):
        fam[key] = {"value": ts(comp, state, "fontFamily"), "type": "fontFamily",
                    "source": f"computed fontFamily of {comp} {state} (raw/components-computed.json)",
                    "description": desc}

# ------------------------------------------------------------ measured colours

# The measured neutral ramp: ink #222325 (nav/logo/button fill), body
# #404145 (section text), muted #62646a (nav/chrome text), faint #74767e
# (footer utility text), the #dadbdd footer hairline and the #c5c6c9 field
# border, plus paper/field whites, the #f5f5f5 nav-hover wash, the
# rgba(255,255,255,0.1) on-dark chip wash and the black scrim behind search.
neutral = SPEC["core"].setdefault("color", {}).setdefault("neutral", {})
for key, comp, state, prop, desc in [
    ("ink", "nav-seller", "default", "color", "The dark ink (nav text, logo, the dark Join/submit button fill)."),
    ("body", "section-h2", "default", "color", "Body/section heading text."),
    ("muted", "cat-nav", "default", "color", "Muted chrome text (nav strip, footer)."),
    ("faint", "footer-currency", "default", "color", "Fainter utility text (footer locale buttons)."),
    ("line", "footer", "default", "borderTopColor", "The footer's hairline."),
    ("field-line", "hero-search-input", "default", "borderTopColor", "The field border grey."),
    ("nav-ink", "nav-seller", "default", "color", "The nav link ink."),
]:
    if have(comp, state, prop):
        v = norm_color(st(comp, state).get(prop, ""))
        if v and v != "transparent" and not v.startswith("rgba("):
            neutral[key] = {"value": v, "type": "color",
                            "source": f"computed {prop} of {comp} {state} (raw/components-computed.json)",
                            "description": desc}

# Painted fills that sit on a child or ancestor rather than the selected node.
for key, comp, state, desc in [
    ("paper", "hero-search-input", "default", "The page/field white."),
    ("scrim", "mkt-header", "default", "The black dim layer the search bar paints (its dim-background child)."),
]:
    v = norm_color(painted(comp, state) or "")
    if v and v != "transparent":
        neutral[key] = {"value": v, "type": "color",
                        "source": f"painted fill inside/under {comp} {state} (raw/components-computed.json)",
                        "description": desc}
# Hover and on-dark washes.
# nav-seller paints no wash on hover (its hover backgroundColor reads
# rgba(0, 0, 0, 0)); the light-grey wash appears only while it is pressed. A
# transparent reading is never committed as a fill.
if have("nav-seller", "pressed", "backgroundColor"):
    v = norm_color(st("nav-seller", "pressed")["backgroundColor"])
    if v != "transparent" and not re.search(r",\s*0\)$", v):
        neutral["press-wash"] = {"value": v, "type": "color",
                                 "source": "computed backgroundColor of nav-seller pressed (raw/components-computed.json)",
                                 "description": "The light-grey nav wash, painted while a nav link is pressed (hover paints none)."}
if have("popular-chip", "default", "backgroundColor"):
    v = norm_color(st("popular-chip", "default")["backgroundColor"])
    if v.startswith("rgba("):
        neutral["on-dark-wash"] = {"value": v, "type": "color",
                                   "source": "computed backgroundColor of popular-chip default (raw/components-computed.json)",
                                   "description": "The translucent white chip wash on the dark hero band."}

# The brand accent and the dark action fills. fiverr's signed-out primary
# buttons (Join, the search submit, Continue) paint the #222325 ink fill;
# the #1dbf73 brand green surfaces as the category-nav hover underline.
brand = SPEC["core"].setdefault("color", {}).setdefault("brand", {})
for key, comp, state, desc in [
    ("fill", "nav-join", "default", "The dark action fill of the Join pill."),
    ("fill-hover", "nav-join", "hover", "The action fill on hover."),
    ("submit", "hero-search-btn", "default", "The search submit's dark fill."),
    ("submit-hover", "hero-search-btn", "hover", "The submit fill on hover."),
    ("cta", "gig-continue", "default", "The gig Continue button's fill."),
]:
    v = norm_color(painted(comp, state) or "")
    if v and v != "transparent":
        brand[key] = {"value": v, "type": "color",
                      "source": f"painted fill inside {comp} {state} (raw/components-computed.json)",
                      "description": desc}
try:
    v = norm_color(C["cat-nav"]["states"]["hover"]["::after"]["backgroundColor"])
    if v:
        brand["accent"] = {"value": v, "type": "color",
                           "source": "computed backgroundColor of the cat-nav hover ::after underline (raw/components-computed.json)",
                           "description": "The fiverr green accent (the category-nav hover underline)."}
except KeyError:
    pass

# -------------------------------------------------------------------- roles

light = SPEC["light"]
ALIAS = "role alias over the measured core palette"
if "ink" in neutral:
    emit(light, "--text-primary", {"value": "{color.neutral.ink}", "type": "color",
                                   "source": ALIAS, "description": "Headline, nav and strong text."})
if "body" in neutral:
    emit(light, "--text-body", {"value": "{color.neutral.body}", "type": "color",
                                 "source": ALIAS, "description": "Body and section text."})
if "muted" in neutral:
    emit(light, "--text-muted", {"value": "{color.neutral.muted}", "type": "color",
                                  "source": ALIAS, "description": "Muted chrome text."})
if "faint" in neutral:
    emit(light, "--text-faint", {"value": "{color.neutral.faint}", "type": "color",
                                  "source": ALIAS, "description": "The faintest utility text."})
if "paper" in neutral:
    emit(light, "--surface-page", {"value": "{color.neutral.paper}", "type": "color",
                                   "source": ALIAS, "description": "The page background."})
    emit(light, "--surface-card", {"value": "{color.neutral.paper}", "type": "color",
                                   "source": ALIAS, "description": "Card panels (join/login cards, pricing card)."})
if "line" in neutral:
    emit(light, "--border-hairline", {"value": "{color.neutral.line}", "type": "color",
                                      "source": ALIAS, "description": "Footer and card hairlines."})
if "field-line" in neutral:
    emit(light, "--border-field", {"value": "{color.neutral.field-line}", "type": "color",
                                   "source": ALIAS, "description": "The search/auth field border."})
if "cta" in brand:
    emit(light, "--action-primary", {"value": "{color.brand.cta}", "type": "color",
                                     "source": ALIAS, "description": "Primary CTAs (Continue, Join, search submit)."})
elif "fill" in brand:
    emit(light, "--action-primary", {"value": "{color.brand.fill}", "type": "color",
                                     "source": ALIAS, "description": "Primary CTAs (Join, Continue, search submit)."})
if "fill-hover" in brand:
    emit(light, "--action-primary-hover", {"value": "{color.brand.fill-hover}", "type": "color",
                                           "source": ALIAS, "description": "Primary fills on hover."})
if "accent" in brand:
    emit(light, "--action-accent", {"value": "{color.brand.accent}", "type": "color",
                                    "source": ALIAS, "description": "The fiverr green accent (hover underlines, brand marks)."})
if have("nav-join", "default", "color"):
    emit(light, "--text-onAccent", {"value": norm_color(st("nav-join", "default")["color"]), "type": "color",
                                     "source": "computed color of nav-join default (raw/components-computed.json)",
                                     "description": "Text on the dark action fills."})
# ------------------------------------------------------------- type scale

type_scale = SPEC["core"].setdefault("font", {}).setdefault("size", {})
leading = SPEC["core"].setdefault("font", {}).setdefault("lineHeight", {})
weight = SPEC["core"].setdefault("font", {}).setdefault("weight", {})
for key, comp, state, prop, bag, desc in [
    ("hero", "hero-h1", "default", "fontSize", type_scale, "The hero display size."),
    ("hero", "hero-h1", "default", "lineHeight", leading, "Hero line height."),
    ("hero", "hero-h1", "default", "fontWeight", weight, "Hero weight."),
    ("section", "section-h2", "default", "fontSize", type_scale, "A section heading size."),
    ("section", "section-h2", "default", "fontWeight", weight, "Section heading weight."),
    ("title", "gig-h1", "default", "fontSize", type_scale, "The gig title size."),
    ("title", "search-h1", "default", "fontSize", type_scale, "The results masthead size (fallback while gig pages are unmeasured)."),
    ("body", "footer-link", "default", "fontSize", type_scale, "Body/footer text size."),
    ("label", "nav-seller", "default", "fontSize", type_scale, "Nav label size."),
    ("label", "nav-seller", "default", "fontWeight", weight, "Nav label weight."),
    ("chip", "popular-chip", "default", "fontSize", type_scale, "Popular-chip label size."),
    ("price", "pkg-price", "default", "fontSize", type_scale, "The package price size."),
]:
    # A fallback row (search-h1 for gig-h1, say) fills the slot only while the
    # preferred measurement is absent — a later reading must never be
    # overwritten by the fallback listed after it.
    v = ts(comp, state, prop)
    if v and key not in bag:
        bag[key] = {
            "type": "number" if prop == "fontWeight" else "dimension",
            "value": v,
            "source": f"computed {prop} of {comp} {state} (raw/components-computed.json)",
            "description": desc}

# ---------------------------------------------------------- spacing/radius

meas = SPEC["core"].setdefault("measured", {})
for key, comp, state, prop, ty, desc in [
    ("button-radius", "nav-join", "default", "borderTopLeftRadius", "dimension", "The Join pill's corner radius."),
    ("search-radius", "hero-search-input", "default", "borderTopLeftRadius", "dimension", "The search field's corner radius."),
    ("card-radius", "gig-card", "default", "borderTopLeftRadius", "dimension", "The gig card's corner radius."),
    ("card-radius", "popular-chip", "default", "borderTopLeftRadius", "dimension", "The chip's corner radius (fallback while gig cards are unmeasured)."),
    ("field-radius", "login-email", "default", "borderTopLeftRadius", "dimension", "The auth field's corner radius."),
    ("field-radius", "hero-search-input", "default", "borderTopLeftRadius", "dimension", "The search field's corner radius (fallback while auth fields are unmeasured)."),
    ("chip-radius", "popular-chip", "default", "borderTopLeftRadius", "dimension", "The popular-chip corner radius."),
    ("control-height", "nav-join", "default", "height", "dimension", "The header CTA height."),
    ("field-height", "login-email", "default", "height", "dimension", "The auth field height."),
    ("field-height", "hero-search-input", "default", "height", "dimension", "The search field height (fallback while auth fields are unmeasured)."),
    ("search-height", "hero-search-input", "default", "height", "dimension", "The hero search field height."),
    ("header-padding-x", "mkt-header", "default", "paddingLeft", "dimension", "The header's horizontal padding."),
    ("focus-outline", "nav-seller", "focus-visible", "outlineColor", "color", "The keyboard-focus ring colour."),
    ("focus-outline", "filter-btn", "focus-visible", "outlineColor", "color", "The keyboard-focus ring colour (fallback source)."),
    ("focus-outline", "m-menu-btn", "focus-visible", "outlineColor", "color", "The keyboard-focus ring colour (fallback source)."),
    ("focus-outline-width", "nav-seller", "focus-visible", "outlineWidth", "dimension", "The focus ring width."),
    ("focus-outline-width", "filter-btn", "focus-visible", "outlineWidth", "dimension", "The focus ring width (fallback source)."),
    ("focus-outline-width", "m-menu-btn", "focus-visible", "outlineWidth", "dimension", "The focus ring width (fallback source)."),
    ("hover-fill", "popular-chip", "hover", "backgroundColor", "color", "The chip's hover fill."),
    ("control-transition", "nav-join", "default", "transitionDuration", "duration", "The control transition duration."),
]:
    # Fallback rows fill a missing slot only; they never replace a reading the
    # preferred row already wrote (popular-chip vs gig-card, the search field
    # vs the auth field).
    if have(comp, state, prop) and key not in meas:
        v = st(comp, state)[prop]
        if ty == "color":
            v = norm_color(v)
        meas[key] = {"value": v, "type": ty,
                     "source": f"computed {prop} of {comp} {state} (raw/components-computed.json)",
                     "description": desc}

# ------------------------------------------------------------------ component

comp = SPEC["component"]
for key, cname, state, prop, desc in [
    ("header.height", "mkt-header", "default", "height", "The sticky header height."),
    ("cta.height", "nav-join", "default", "height", "The header Join pill height."),
    ("cta.width", "nav-join", "default", "width", "The header Join pill width."),
    ("search.height", "hero-search-input", "default", "height", "The hero search field height."),
    ("search.width", "hero-search-input", "default", "width", "The hero search field width."),
    ("field.height", "login-email", "default", "height", "The auth field height."),
    ("field.height", "hero-search-input", "default", "height", "The search field height (fallback)."),
    ("drawer.width", "drawer", "default", "width", "The categories drawer width."),
    ("gig-card.width", "gig-card", "default", "width", "The search gig card width."),
    ("gig-card.height", "gig-card", "default", "height", "The search gig card height."),
    ("price-card.width", "pkg-tablist", "default", "width", "The pricing card's tablist width."),
    ("panel.width", "login-panel", "default", "width", "The auth panel width."),
    ("panel.width", "join-panel", "default", "width", "The join panel width (fallback)."),
    ("mobile-topbar.height", "m-topbar", "default", "height", "The mobile header height."),
]:
    if have(cname, state, prop):
        node = comp
        parts = key.split(".")
        for p in parts[:-1]:
            node = node.setdefault(p, {})
        # Same fill-only rule: the fallback row (join-panel for login-panel,
        # the search field for the auth field) never overwrites a set leaf.
        if parts[-1] not in node:
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
