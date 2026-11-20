#!/usr/bin/env python3
"""Write raw/component-tokens.json, the token spec build_tokens.py reads.

www.gofundme.com is a Next.js app on its "hrt" design system: the declared
token layer is ~700 `--hrt-*` custom properties on `:root` /
`:where([data-theme="consumer"])` (raw/css-vars.json) — real semantic names
(`--hrt-color-button-primary-surface-hover`, `--hrt-size-text-heading-xl`,
`--hrt-spacing-4`), not opaque ids. This spec publishes every resolved
consumer value under its own name: `--hrt-color-*` names land in the `light`
set (the only theme the consumer site paints), the non-colour scales land in
`core` (size, spacing, radius, type, font, motion, z-index, grid), and
component-scoped vars (`--hrt-header-*`, `--hrt-tooltip-*`, `--hrt-goal-bar-*`
…) sit in `core.componentVars`. A `[data-theme="pro"]` layer exists in the
CSS but never paints on the consumer surfaces; it stays in
raw/css-vars.json as declared evidence, not tokens.

The /c/* marketing pages are the WordPress content stack (wp-* blocks over
an older hrt-base-* layer) and /sign-in is the auth boundary;
their values are measured component tokens, labelled.

Measured roles (button fills, header ink, card geometry) alias to the
declared --hrt-* token whose painted value they match, labelled with the
measurement they came from.

Deterministic: same inputs, byte-identical output.
"""
import json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
V = json.loads((RAW / "css-vars.json").read_text())
RL = V.get("resolved", {}).get("light", {})
R = RL  # resolved() below reads entries of this map
C = json.loads((RAW / "components-computed.json").read_text())["components"]

SPEC = {"_about": (
    "The token tree build_tokens.py turns into tokens.json. gofundme.com "
    "declares its design-token layer as ~700 `--hrt-*` custom properties "
    "on :root / the consumer theme scope (raw/css-vars.json): semantic "
    "colour roles, size/spacing/radius scales, the type system, motion "
    "and z-index — every resolved consumer value is published under its "
    "own name. The /c/* pages are the WordPress content stack and "
    "/sign-in the auth boundary; their values are measured. "
    "Measured roles alias to the declared values where they match."),
    "core": {}, "light": {}, "component": {}}

def st(comp, state):
    return C[comp]["states"][state]["style"]


def rc(comp, state, key):
    return C[comp]["states"][state]["rect"][key]


def ts(comp, state, prop):
    """The first text node's reading (textStyle) when the kit recorded one."""
    try:
        c = C[comp]["states"][state]
        t = c.get("textStyle") or {}
        v = t.get(prop)
        return v if v else c["style"].get(prop)
    except KeyError:
        return None


def norm_color(v):
    """#hex, rgb()/rgba() -> the hex or rgba() the browser paints."""
    v = (v or "").strip()
    m = re.fullmatch(r"#([0-9a-fA-F]{3,8})", v)
    if m:
        h = m.group(1).lower()
        if len(h) in (3, 4):
            h = "".join(c * 2 for c in h)
        return "#" + h[:6]
    m = re.fullmatch(r"rgba?\(([\d.]+),?\s+([\d.]+),?\s+([\d.]+)(?:\s*[,/]\s*([\d.]+%?))?\)", v)
    if m:
        r, g, b, a = m.groups()
        a = 1 if a is None else (float(a[:-1]) / 100 if a.endswith("%") else float(a))
        if a >= 1:
            return "#%02x%02x%02x" % (int(float(r)), int(float(g)), int(float(b)))
        return f"rgba({int(float(r))}, {int(float(g))}, {int(float(b))}, {'%g' % a})"
    return v


def have(comp, state, prop=None):
    try:
        s = st(comp, state)
        return prop is None or bool((s.get(prop) or "").strip())
    except KeyError:
        return False


def lit(value, ty, src, desc):
    return {"value": norm_color(value) if ty == "color" else value, "type": ty, "source": src, "description": desc}


EMITTED = {}   # variable name -> dotted token path it was actually written to
_OWNER = {}    # dotted token path -> variable name holding it


def _leaf(d):
    return isinstance(d, dict) and ("var" in d or "value" in d)


def emit_at(root, path, leaf, name=None):
    """Write `leaf` at a dotted path. A leaf that must share a node with a
    group moves inside it under `default`."""
    node = root
    parts = path.split(".")
    for i, p in enumerate(parts[:-1]):
        nxt = node.get(p)
        prefix = ".".join(parts[:i + 1])
        if nxt is None:
            nxt = node[p] = {}
        elif _leaf(nxt):
            owner = _OWNER.pop(prefix, None)
            nxt = node[p] = {"default": nxt}
            if owner:
                EMITTED[owner] = prefix + ".default"
                _OWNER[prefix + ".default"] = owner
        node = nxt
    last = parts[-1]
    full = ".".join(parts)
    if last in node and not _leaf(node[last]):
        for key in ("default", "base", "self"):
            if key not in node[last]:
                node[last][key] = leaf
                full += "." + key
                break
        else:
            raise ValueError(f"{path}: no free key to hold the leaf beside its group")
    else:
        if last in node:
            raise ValueError(f"{path}: duplicate token path")
        node[last] = leaf
    if name:
        EMITTED[name] = full
        _OWNER[full] = name


def resolved(name):
    e = R.get(name)
    if isinstance(e, dict):
        return e.get("value", e.get("raw"))
    return e


def var(name, ty="color", **kw):
    d = {"var": name, "type": ty}
    d.update(kw)
    return d


# ------------------------------------------------ the --hrt-* token layer
#
# Every resolved consumer value is published under its own semantic name:
# the selector declares it, the probe resolved it, the token is the same
# value — a one-to-one declared layer, evidence "css-var <name> (light)".
# Groups map the name's family; the leaf name is the rest of the var name
# split on '-' into nested groups (`--hrt-color-button-primary-surface-hover`
# -> light.color.button.primary.surface.hover, with a `default` key when a
# name is both a leaf and a group's prefix).

DECL_SRC = "goFundMe's declared --hrt-* custom properties on :root / the consumer theme scope (raw/css-vars.json)"

KIND_TY = {
    "color": "color", "dimension": "dimension", "duration": "duration",
    "number": "number", "fontFamily": "fontFamily",
}

COLOR_FAMILY = re.compile(r"^--hrt-(?:color|data|icon)-")
CORE_GROUPS = [
    (re.compile(r"^--hrt-size-"), "core.size"),
    (re.compile(r"^--hrt-spacing-"), "core.spacing"),
    (re.compile(r"^--hrt-radius-"), "core.radius"),
    (re.compile(r"^--hrt-shadow-"), "core.shadow"),
    (re.compile(r"^--hrt-type-"), "core.type"),
    (re.compile(r"^--hrt-typography-"), "core.type"),
    (re.compile(r"^--hrt-text-"), "core.type"),
    (re.compile(r"^--hrt-line-height-"), "core.font.height"),
    (re.compile(r"^--hrt-letter-spacing-"), "core.font.tracking"),
    (re.compile(r"^--hrt-font-"), "core.font.family"),
    (re.compile(r"^--hrt-motion-"), "core.motion"),
    (re.compile(r"^--hrt-ease-"), "core.motion.ease"),
    (re.compile(r"^--hrt-time-"), "core.motion.duration"),
    (re.compile(r"^--hrt-z-index-"), "core.zIndex"),
    (re.compile(r"^--hrt-row-"), "core.grid"),
    (re.compile(r"^--hrt-col-"), "core.grid"),
    (re.compile(r"^--hrt-gradient-"), "light.gradient"),
    (re.compile(r"^--hrt-texture-"), "light.texture"),
]

STRIP = re.compile(
    r"^--hrt-(?:color|data|icon|size|spacing|radius|shadow|type|typography|text|"
    r"line-height|letter-spacing|font|motion|ease|time|z-index|row|col|gradient|texture)-")

def group_of(name):
    if COLOR_FAMILY.match(name):
        return "light.color"
    for rx, g in CORE_GROUPS:
        if rx.match(name):
            return g
    if name == "--hrt-base-px-font-size":
        return "core.font.size"
    if name == "--hrt-typeface":
        return "core.font.family"
    # component-scoped vars: --hrt-<component>-*
    m = re.match(r"^--hrt-([a-z-]+?)-", name)
    return "core.componentVars." + (m.group(1) if m else "misc")

def leaf_path(group, name):
    if name == "--hrt-base-px-font-size":
        return "base-px"
    if name == "--hrt-typeface":
        return "typeface"
    if group.startswith("core.componentVars."):
        # strip the component prefix: --hrt-header-height inside
        # componentVars.header -> "height"
        comp = group.rsplit(".", 1)[1]
        rest = re.sub(r"^--hrt-" + re.escape(comp) + "-?", "", name)
        return rest or "default"
    rest = STRIP.sub("", name)
    return rest or "default"

counts = {"declared": 0, "skipped": 0}
for name in sorted(k for k in R if k.startswith("--hrt-")):
    e = R.get(name)
    if not isinstance(e, dict) or e.get("value") in (None, ""):
        counts["skipped"] += 1
        continue
    # The sheets carry --hrt-typography-* as a byte-identical re-declaration
    # of the --hrt-type-* block (44 twins, same raw and resolved values).
    # A twin collapses onto its type token instead of writing a second leaf
    # at the same path; the type leaf names the alias in its description.
    if name.startswith("--hrt-typography-"):
        twin = "--hrt-type-" + name[len("--hrt-typography-"):]
        t = R.get(twin)
        if isinstance(t, dict) and t.get("raw") == e.get("raw"):
            counts["twinned"] = counts.get("twinned", 0) + 1
            continue
    kind = e.get("kind", "other")
    ty = KIND_TY.get(kind, "other")
    if kind == "easing":
        ty = "cubicBezier" if "cubic-bezier" in str(e.get("raw", "")) else "other"
    if kind == "shadow":
        ty = "other"  # composite strings stay verbatim
    group = group_of(name)
    root = SPEC["light"] if group.startswith("light.") else SPEC["core"]
    # descend under the group's segments after the set name
    # ("light.color.button..." -> holder is root["color"]["button"])
    holder = root
    for seg in group.split(".")[1:]:
        holder = holder.setdefault(seg, {})
    parts = leaf_path(group, name).split("-")
    twin_note = ""
    if name.startswith("--hrt-type-"):
        twin = "--hrt-typography-" + name[len("--hrt-type-"):]
        t = R.get(twin)
        if isinstance(t, dict) and t.get("raw") == e.get("raw"):
            twin_note = f" {twin} declares the identical value (a re-declared alias layer in the sheets)."
    emit_at(holder, ".".join(parts),
            var(name, ty,
                description="Resolved in the consumer (light) scope; declared on :where(:root)/:where([data-theme=consumer])." + twin_note),
            name)
    counts["declared"] += 1

SPEC["core"].setdefault("componentVars", {}).setdefault(
    "$description",
    "Component-scoped --hrt-<component>-* variables (header, tooltip, "
    "dropdown, popover, bubble, toast, goal-bar, choice, pagination-dots): "
    "declared values resolved in the consumer scope.")

# -------------------------------------------- measured roles -> aliases

# When several declared --hrt-color-* vars resolve to the same colour, a
# measured role aliases only to a var of its own kind: an ink to text.* (or a
# button's text.*), a fill to surface.* (or a button's surface.*), a border to
# border.*. A role with no var of its kind stays a literal, so a change to some
# unrelated token that happens to share the value never recolours it. Within
# a kind the shortest, then first-sorted, path wins.
CANDS = {}
for name in sorted(k for k in EMITTED):
    nv = norm_color(str(resolved(name) or ""))
    if nv and nv.startswith(("#", "rgba")):
        CANDS.setdefault(nv, []).append(EMITTED[name])

INK = [("button", ".text"), ("text", "")]
FILL = [("button", ".surface"), ("surface", "")]
KIND = {
    ("text", "color"): [("text", "")],
    ("action", "color"): INK,
    ("action", "backgroundColor"): FILL,
    ("border", "outlineColor"): [("border", "")],
    ("surface", "backgroundColor"): [("surface", "")],
    ("data", "backgroundColor"): [("data", ""), ("progress", ""), ("goal", "")],
    ("form", "color"): [("input", ".text"), ("text", "")],
    ("form", "placeholder"): [("input", ".placeholder"), ("text", "")],
    ("form", "backgroundColor"): [("input", ".surface"), ("surface", "")],
    ("form", "borderTopColor"): [("input", ".border"), ("border", "")],
}


def role_alias(nv, group, prop):
    kinds = KIND.get((group, prop), [])
    best = None
    for p in CANDS.get(nv, []):
        for i, (fam, sub) in enumerate(kinds):
            if p.split(".", 1)[0] == fam and (not sub or sub + "." in "." + p + "."):
                key = (i, p.count("."), p)
                if best is None or key < best[0]:
                    best = (key, p)
                break
    return "color." + best[1] if best else None


def semcolor(raw, src, desc, group, prop):
    nv = norm_color(raw)
    alias = role_alias(nv, group, prop)
    value = "{%s}" % alias if alias else nv
    return lit(value, "color", src + ("; matches declared %s" % alias if alias else ""), desc)


sem = SPEC["light"].setdefault("measured", {})
sem["$description"] = ("Roles read off the running pages (computed styles, "
                       "raw/components-computed.json) that alias to the declared "
                       "--hrt-* token painting the same colour where one matches; "
                       "the /c/* content stack and the headless sign-in shell are "
                       "measured-only (their values never alias).")
for key, comp, state, prop, group, desc in [
    ("ink", "hero-h1", "default", "color", "text",
     "The ink on the hero display heading."),
    ("navInk", "nav-search", "default", "color", "text",
     "The header control ink."),
    ("navInkHover", "nav-search", "hover", "color", "text",
     "The header control ink on hover."),
    ("ctaFill", "nav-start", "default", "backgroundColor", "action",
     "The header \"Start a GoFundMe\" pill fill."),
    ("ctaInk", "nav-start", "default", "color", "action",
     "The text on the header CTA pill."),
    ("ctaHover", "nav-start", "hover", "backgroundColor", "action",
     "The header CTA hover fill."),
    ("focusRing", "nav-start", "focus-visible", "outlineColor", "border",
     "The keyboard focus ring colour on the header CTA."),
    ("heroCtaFill", "hero-cta", "default", "backgroundColor", "action",
     "The hero \"Start a GoFundMe\" primary button fill."),
    ("heroCtaInk", "hero-cta", "default", "color", "action",
     "The hero CTA text."),
    ("donateFill", "f-donate", "default", "backgroundColor", "action",
     "The \"Donate now\" button fill on a fundraiser page (measured, never pressed)."),
    ("donateInk", "f-donate", "default", "color", "action",
     "The \"Donate now\" button text."),
    ("shareInk", "f-share", "default", "color", "action",
     "The \"Share\" button ink on a fundraiser page."),
    ("promoFill", "mkt-promo", "default", "backgroundColor", "surface",
     "The global promo banner fill."),
    ("cardBg", "fundraiser-card", "default", "backgroundColor", "surface",
     "A discover fundraiser card surface."),
    ("goalBarFill", "f-goal-bar", "default", "backgroundColor", "data",
     "The goal-bar track fill on a fundraiser page."),
    ("menuPanel", "nav-panel", "default", "backgroundColor", "surface",
     "The header dropdown panel fill."),
    ("fieldBg", "create-zip", "default", "backgroundColor", "form",
     "The wizard postcode field fill."),
    ("fieldInk", "create-zip", "default", "color", "form",
     "The field text ink in the wizard."),
    ("placeholder", "create-zip", "default", "placeholder", "form",
     "The postcode field's placeholder ink."),
    ("fieldBorder", "create-zip", "default", "borderTopColor", "form",
     "The field border colour."),
    ("countryFieldBg", "create-country", "default", "backgroundColor", "form",
     "The country select's fill."),
    ("continueFill", "create-continue", "default", "backgroundColor", "action",
     "The wizard \"Continue\" button fill (measured, never pressed)."),
    ("pillInk", "create-pill", "default", "color", "form",
     "A category pill's ink."),
    ("pillBorder", "create-pill", "default", "borderTopColor", "form",
     "A category pill's border."),
    ("footerBg", "footer", "default", "backgroundColor", "surface",
     "The footer surface fill."),
    ("footerInk", "footer-link", "default", "color", "text",
     "A footer link's ink."),
    ("wpButtonFill", "wp-button", "default", "backgroundColor", "action",
     "A wp-block CTA fill on the /c/* content stack."),
    ("wpButtonInk", "wp-button", "default", "color", "action",
     "A wp-block CTA's text."),
    ("priceH1", "price-h1", "default", "color", "text",
     "The pricing masthead ink on the content stack."),
]:
    try:
        if prop == "color":
            raw = ts(comp, state, "color")
            src = f"computed color of {comp} {state} — the first text node's reading where the kit recorded one (raw/components-computed.json)"
        elif prop == "placeholder":
            raw = (C[comp]["states"][state].get("placeholder") or {}).get("color")
            src = f"computed ::placeholder color of {comp} {state} (raw/components-computed.json)"
        else:
            raw = st(comp, state)[prop]
            src = f"computed {prop} of {comp} {state} (raw/components-computed.json)"
        if raw in (None, ""):
            raise KeyError(prop)
        sem.setdefault("color", {}).setdefault(group, {})[key] = semcolor(raw, src, desc, group, prop)
    except KeyError:
        pass

# The page field behind every consumer page: the declared surface token,
# visible as the white field in every screenshot.
page_bg = role_alias("#ffffff", "surface", "backgroundColor")
sem.setdefault("color", {}).setdefault("background", {})["page"] = lit(
    "{%s}" % page_bg if page_bg else "#ffffff", "color",
        "the :root-declared surface token (raw/css-vars.json); visible as the page field behind every consumer page (screenshots/*-light-*.png)",
        "The page field — the consumer light surface.")

# ------------------------------------------------------------- type ramp
#
# The hrt type scale is declared (--hrt-type-*/--hrt-typography-*); the steps
# here are measured readings that anchor it to real elements.

for key, comp, state, prop, desc in [
    ("hero", "hero-h1", "default", "fontSize", "The hero display heading size."),
    ("fundraiserTitle", "f-title", "default", "fontSize", "The fundraiser page title size."),
    ("section", "section-h2", "default", "fontSize", "A section heading size."),
    ("nav", "nav-search", "default", "fontSize", "The header control size."),
    ("body", "footer-link", "default", "fontSize", "A footer link size."),
    ("button", "hero-cta", "default", "fontSize", "The hero CTA label size."),
    ("donate", "f-donate", "default", "fontSize", "The Donate button label size."),
    ("priceHero", "price-h1", "default", "fontSize", "The content-stack masthead size."),
]:
    try:
        raw = ts(comp, state, prop) or st(comp, state)[prop]
        SPEC["core"].setdefault("font", {}).setdefault("size", {}).setdefault("measured", {})[key] = lit(
            raw, "dimension", f"computed {prop} of {comp} {state} (raw/components-computed.json)", desc)
    except KeyError:
        pass

for key, comp, state, desc in [
    ("hero", "hero-h1", "default", "The hero display heading weight."),
    ("section", "section-h2", "default", "A section heading weight."),
    ("nav", "nav-search", "default", "The header control weight."),
    ("body", "footer-link", "default", "The footer link weight."),
    ("button", "hero-cta", "default", "The hero CTA label weight."),
]:
    try:
        raw = ts(comp, state, "fontWeight") or st(comp, state)["fontWeight"]
        if raw:
            SPEC["core"].setdefault("font", {}).setdefault("weight", {}).setdefault("measured", {})[key] = lit(
                int(float(raw)), "fontWeight", f"computed fontWeight of {comp} {state} (raw/components-computed.json)", desc)
    except (KeyError, ValueError):
        pass

for key, comp, state, desc in [
    ("hero", "hero-h1", "default", "The hero display heading line-height."),
    ("nav", "nav-search", "default", "The header control line-height."),
    ("body", "footer-link", "default", "The footer link line-height."),
]:
    try:
        raw = ts(comp, state, "lineHeight") or st(comp, state)["lineHeight"]
        SPEC["core"].setdefault("font", {}).setdefault("height", {}).setdefault("measured", {})[key] = lit(
            raw, "dimension" if re.fullmatch(r"-?[0-9.]+(px|rem)", raw or "") else "other",
            f"computed lineHeight of {comp} {state} (raw/components-computed.json)", desc)
    except KeyError:
        pass

for key, comp, state, desc in [
    ("display", "hero-h1", "default", "The display/heading face the consumer pages set."),
    ("body", "nav-search", "default", "The face on nav controls and body copy."),
    ("content", "price-h1", "default", "The face on the WordPress content stack."),
]:
    try:
        raw = ts(comp, state, "fontFamily") or st(comp, state)["fontFamily"]
        if raw:
            SPEC["core"].setdefault("font", {}).setdefault("family", {}).setdefault("measured", {})[key] = lit(
                raw, "fontFamily", f"computed fontFamily of {comp} {state} (raw/components-computed.json)", desc)
    except KeyError:
        pass

# ------------------------------------------------------------------ shape

for key, comp, state, prop, desc in [
    ("cta", "nav-start", "default", "borderTopLeftRadius", "The header CTA pill radius."),
    ("heroCta", "hero-cta", "default", "borderTopLeftRadius", "The hero primary button radius."),
    ("navControl", "nav-search", "default", "borderTopLeftRadius", "The header search control radius."),
    ("menuPanel", "nav-panel", "default", "borderTopLeftRadius", "The dropdown panel radius."),
    ("card", "fundraiser-card", "default", "borderTopLeftRadius", "A fundraiser card radius."),
    ("field", "create-zip", "default", "borderTopLeftRadius", "The wizard field radius."),
    ("pill", "create-pill", "default", "borderTopLeftRadius", "A category pill radius."),
    ("tag", "card-media-tag", "default", "borderTopLeftRadius", "A media tag chip radius."),
    ("wpButton", "wp-button", "default", "borderTopLeftRadius", "A content-stack button radius."),
]:
    try:
        v = st(comp, state)[prop]
        if v in (None, ""):
            raise KeyError(prop)
        emit_at(SPEC["core"].setdefault("radius", {}), "measured." + key,
                lit(v, "dimension" if re.fullmatch(r"-?[0-9.]+(px|rem)", v or "") else "other",
                    f"computed {prop} of {comp} {state} (raw/components-computed.json)", desc))
    except KeyError:
        pass

# ------------------------------------------------------------------ shadow

for key, comp, state, prop, desc in [
    ("menuPanel", "nav-panel", "default", "boxShadow", "The dropdown panel shadow."),
    ("card", "fundraiser-card", "default", "boxShadow", "A fundraiser card's shadow."),
    ("headerBar", "mkt-header", "default", "boxShadow", "The header bar's shadow (none, unless it floats)."),
    ("promoBanner", "mkt-promo", "default", "boxShadow", "The promo banner's shadow."),
]:
    try:
        v = st(comp, state)[prop]
        if not v or v == "none":
            raise KeyError(prop)
        emit_at(SPEC["light"].setdefault("shadow", {}), "measured." + key,
                lit(v, "other", f"computed {prop} of {comp} {state} (raw/components-computed.json)", desc))
    except KeyError:
        pass

# ------------------------------------------------------------------ spacing

for key, comp, state, prop, desc in [
    ("headerPaddingX", "mkt-header", "default", "paddingLeft", "The header bar's horizontal padding."),
    ("ctaPaddingX", "nav-start", "default", "paddingLeft", "The header CTA's horizontal padding."),
    ("ctaPaddingY", "nav-start", "default", "paddingTop", "The header CTA's vertical padding."),
    ("fieldPaddingX", "create-zip", "default", "paddingLeft", "The wizard field's horizontal padding."),
    ("donatePaddingX", "f-donate", "default", "paddingLeft", "The Donate button's horizontal padding."),
    ("donatePaddingY", "f-donate", "default", "paddingTop", "The Donate button's vertical padding."),
    ("pillPaddingX", "create-pill", "default", "paddingLeft", "A category pill's horizontal padding."),
]:
    try:
        v = st(comp, state)[prop]
        if v in (None, ""):
            raise KeyError(prop)
        emit_at(SPEC["core"].setdefault("spacing", {}), "measured." + key,
                lit(v, "dimension" if re.fullmatch(r"-?[0-9.]+(px|rem)", v or "") else "other",
                    f"computed {prop} of {comp} {state} (raw/components-computed.json)", desc))
    except KeyError:
        pass

# ------------------------------------------------------------------ motion

try:
    s = st("nav-search", "default")
    dur, e = s.get("transitionDuration"), s.get("transitionTimingFunction")
    if dur and dur != "0s":
        props = [p.strip() for p in s.get("transitionProperty", "all").split(",") if p.strip()]
        durs = [d.strip() for d in dur.split(",")]
        tfs = re.findall(r"cubic-bezier\([^)]*\)|steps\([^)]*\)|[a-z-]+", e or "")
        parts = []
        for i, p in enumerate(props):
            d = durs[i % len(durs)]
            if d == "0s":
                continue
            parts.append(f"{p} {d} {tfs[i % len(tfs)] if tfs else ''}".strip())
        if parts:
            SPEC["core"].setdefault("motion", {})["control"] = lit(", ".join(parts), "other",
                "computed transition of nav-search default (raw/components-computed.json)",
                "The control transition on a header control.")
except KeyError:
    pass

# ------------------------------------------------------------- components

comp = SPEC["component"]
for name, cname, state, prop, ty_, desc in [
    ("topbar-height", "mkt-header", "default", "h", "dimension", "The site header bar height."),
    ("promo-height", "mkt-promo", "default", "h", "dimension", "The global promo banner height."),
    ("cta-height", "nav-start", "default", "h", "dimension", "The header \"Start a GoFundMe\" height."),
    ("hero-cta-height", "hero-cta", "default", "h", "dimension", "The hero primary button height."),
    ("nav-control-height", "nav-search", "default", "h", "dimension", "A header control's hit height."),
    ("menu-panel-width", "nav-panel", "default", "w", "dimension", "The header dropdown panel width."),
    ("hero-headline-width", "hero-h1", "default", "w", "dimension", "The hero display heading's measure."),
    ("fundraiser-card-width", "fundraiser-card", "default", "w", "dimension", "A discover card's width."),
    ("fundraiser-card-height", "fundraiser-card", "default", "h", "dimension", "A discover card's height."),
    ("goal-bar-height", "f-goal-bar", "default", "h", "dimension", "The goal-bar element height."),
    ("donate-height", "f-donate", "default", "h", "dimension", "The Donate button height."),
    ("share-height", "f-share", "default", "h", "dimension", "The Share button height."),
    ("field-height", "create-zip", "default", "h", "dimension", "The wizard postcode field height."),
    ("country-select-height", "create-country", "default", "h", "dimension", "The country select height."),
    ("continue-height", "create-continue", "default", "h", "dimension", "The Continue button height."),
    ("pill-height", "create-pill", "default", "h", "dimension", "A category pill's height."),
    ("tag-height", "card-media-tag", "default", "h", "dimension", "A media tag chip's height."),
    ("avatar-size", "f-avatar", "default", "h", "dimension", "The organiser avatar size."),
    ("mobile-topbar-height", "m-header", "default", "h", "dimension", "The phone header bar height."),
]:
    try:
        v = rc(cname, state, prop)
        comp[name] = lit(("%g" % v) + "px" if isinstance(v, (int, float)) else str(v) + "px",
                         ty_, f"measured {prop} of {cname} {state} (raw/components-computed.json)", desc)
    except KeyError:
        pass

(RAW / "component-tokens.json").write_text(json.dumps(SPEC, indent=2, ensure_ascii=False) + "\n")
print("component-tokens.json:", {k: len(v) for k, v in SPEC.items() if k != "_about"}, counts)
