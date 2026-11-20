#!/usr/bin/env python3
"""Write raw/component-tokens.json, the token spec build_tokens.py reads.

frame.io is two public surfaces signed out. The site (frame.io/...) is a
Next.js app styled with CSS modules whose stylesheets declare a real
design-token layer (raw/css-vars.json):

  --color-grey-00..100      the 19-step neutral ramp the whole painted dark
                            theme is built from (00 = #000000 field, 05 =
                            #0d0d18 surface, 100 = #fcfcfc ink)
  --color-{coral,iris,electric,cobalt,turquoise-triumph}{,-light,-dark}
                            the five brand hues and their steps
  --color-{hue}-NN          per-hue alpha tints (--color-cobalt-20 …)
  --color-alpha-{black,dark,light}-*, --color-alpha-{perano,cinder,hawkes,grey}-*
                            the alpha ladders and named alpha tints
  --color-accent(-default)  the light-grey accent role
  --overlay-*               the dim/light overlays (rgb(0 0 0 / 20%) …)
  --font-main/-secondary/-tertiary
                            the three served stacks — FrameGothic (headings,
                            400-600 variable), NeueMachinaInktrap (labels),
                            Inter variable 100-900 (UI) — declared on the
                            Next.js font-variable classes (.__variable_*), so
                            they emit from the declaration's raw string
  --font-size-base          1.6rem = 16px
  --main-font-color         the ink role (#fcfcfc)
  --spacer-0..480           the rem spacing scale (0.8rem steps)
  --grid-number-of-columns, --grid-max-content-width, --global-max-width,
  --nav-height(-padded)     the 12-column, 108rem marketing grid and the 8rem
                            fixed header
  --duration-*ms, --animation-duration, --ease-*, --card-hover-*
                            the motion layer (0.3s / cubic-bezier(0.25,0.1,
                            0.25,1) is the default control ease)
  --z-index-*               the 0..105 stacking map (nav 100, modal, max)

Every public page paints the one dark theme — the site ships no theme
switch (no [data-theme] scope, no toggle control) — so the package ships a
single `dark` token set resolved on :root, and vars.mjs's second probe pass
is a sanity check that returns the same values. accounts.frame.io/welcome
(the sign-in surface) is a light styled-components page on a different
stack; its measured values land under component.productShell.* as literals.

Deterministic: same inputs, byte-identical output.
"""
import json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
V = json.loads((RAW / "css-vars.json").read_text())
RL = V.get("resolved", {}).get("light", {})   # the :root probe — the painted theme
C = json.loads((RAW / "components-computed.json").read_text())["components"]
R = {n: (v.get("value", v.get("raw")) if isinstance(v, dict) else v) for n, v in RL.items()}

# A variable the probe cannot resolve (declared on a scoped class the probe
# div does not carry, e.g. the Next.js font-variable classes on <html>) is
# still evidence: read its raw declaration from the stylesheet rules.
RAW_DECL = {}
for r in (V.get("theme") or []) + (V.get("app") or []):
    for n, raw in (r.get("properties") or {}).items():
        RAW_DECL.setdefault(n, (raw, r.get("selector", "")))


def var(name, ty="color", **kw):
    d = {"var": name, "type": ty}
    d.update(kw)
    return d


SPEC = {"_about": (
    "The token tree build_tokens.py turns into tokens.json. frame.io "
    "declares its design-token layer in the site's stylesheets "
    "(raw/css-vars.json): the theme-invariant scales under core.* (the "
    "grey/brand/alpha palette, the spacer scale, the grid, the durations "
    "and easings, the z-index map) and the painted roles under dark.* — "
    "the site's one theme, measured on the live pages and aliased to the "
    "declared variables whose values match. accounts.frame.io's sign-in "
    "surface is a different stack; its measured values live under "
    "component.productShell.* as literals."),
    "core": {}, "dark": {}, "component": {}}


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
    v = (v or "").strip()
    m = re.fullmatch(r"#([0-9a-fA-F]{3,8})", v)
    if m:
        h = m.group(1).lower()
        if len(h) in (3, 4):
            h = "".join(c * 2 for c in h)
        return "#" + h[:6]
    m = re.fullmatch(r"rgba?\(\s*([\d.]+)\s*,\s*([\d.]+)\s*,\s*([\d.]+)\s*(?:,\s*([\d.]+%?))?\)", v)
    if m:
        r, g, b, a = m.groups()
        if a is None or float(a.rstrip("%")) >= (100 if a.endswith("%") else 1):
            return "#%02x%02x%02x" % (int(float(r)), int(float(g)), int(float(b)))
        a = float(a[:-1]) / 100 if a.endswith("%") else float(a)
        return f"rgba({int(float(r))}, {int(float(g))}, {int(float(b))}, {'%g' % round(a, 3)})"
    # `rgb(0 0 0 / 20%)` space-and-slash syntax, as Chromium serialises the
    # --overlay-* declarations.
    m = re.fullmatch(r"rgba?\(\s*([\d.]+)\s+([\d.]+)\s+([\d.]+)\s*/\s*([\d.]+%?)\s*\)", v)
    if m:
        r, g, b, a = m.groups()
        a = float(a[:-1]) / 100 if a.endswith("%") else float(a)
        return f"rgba({int(float(r))}, {int(float(g))}, {int(float(b))}, {'%g' % round(a, 3)})"
    m = re.fullmatch(r"okl(?:ch|ab)\(\s*([\d.]+)\s+(?:0(?:\.0+)?|none)\s+(?:none|[-\d.]+)\s*(?:/\s*([\d.]+%?))?\s*\)", v)
    if m:
        lvl = round(float(m.group(1)) * 255)
        a = m.group(2)
        a = float(a[:-1]) / 100 if a and a.endswith("%") else float(a or 1)
        return "#%02x%02x%02x" % (lvl, lvl, lvl) if a >= 1 else "rgba(%d, %d, %d, %g)" % (lvl, lvl, lvl, round(a, 3))
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
    """Write `leaf` at a dotted path (`theme.btn.primary.bg`). A leaf that must
    share a node with a group moves inside it under `default`."""
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


DECL_SRC = "declared design-system variable in the site's stylesheets (raw/css-vars.json)"


def declared(name):
    """The resolved :root value, or None when the var never resolved."""
    v = R.get(name)
    return v if v not in (None, "") else None


def norm_len(v):
    m = re.fullmatch(r"(-?[\d.]+[eE][+-]?\d+)(px|rem)", str(v).strip())
    if not m:
        return v
    return f"{float(m.group(1)):f}".rstrip("0").rstrip(".") + m.group(2)


def decl(name, ty="dimension"):
    v = declared(name)
    desc = f"The declared `{name}`."
    if ty == "dimension":
        nv = norm_len(v)
        if nv != v:
            raw = (RL.get(name) or {}).get("raw")
            desc = f"The declared `{name}` — `{raw}`, which Chromium resolves to {nv}."
            v = nv
        if not re.fullmatch(r"-?\d+(\.\d+)?(px|rem)", str(v).strip()):
            ty = "other"
    return lit(v, ty, f"{DECL_SRC}: {name}", desc)


COLOR_V = re.compile(r"(#[0-9a-fA-F]{3,8}|rgba?\([^)]*\)|hsla?\([^)]*\)|(ok)?lab\([^)]*\)|(ok)?lch\([^)]*\)|color-mix\([^)]*\)|color\([^)]*\))")


def decl_color(name):
    v = declared(name)
    nv = norm_color(v)
    ty = "color" if COLOR_V.fullmatch(str(nv).strip()) else "other"
    src = f"{DECL_SRC}: {name}"
    if nv != v:
        src += f"; `{v}` normalised to {nv} (the colour the browser paints)"
        v = nv
    return lit(v, ty, src, f"The declared `{name}`.")


def num_decl(name):
    v = declared(name)
    return lit(v, "number", f"{DECL_SRC}: {name}", f"The declared `{name}`.")


def painted(comp, state, key):
    """A reading from the kit's paint list — the layers actually painted
    (rounded children, pseudo-elements, inset shadows) rather than the
    wrapper's computed style, which is often an unpainted positioning box."""
    c = C[comp]["states"][state]
    entries = [p for p in c.get("paint") or [] if p.get(key)]
    if not entries:
        raise KeyError(key)
    rect = c.get("rect") or {}
    for p in entries:
        m = re.fullmatch(r"([\d.]+)x([\d.]+)", str(p.get("size") or ""))
        if m and abs(float(m.group(1)) - rect.get("w", -9)) <= 1 and abs(float(m.group(2)) - rect.get("h", -9)) <= 1:
            return p[key]
    return entries[0][key]


def inset_shadow_color(comp, state):
    """The colour of the painted inset (hairline) box-shadow layer — how the
    site draws a 'border' when border-width is 0."""
    sh = painted(comp, state, "shadow")
    m = re.search(COLOR_V.pattern + r"(?:\s+-?[\d.]+px){2,4}\s+inset", sh)
    if not m:
        raise KeyError("insetShadowColor")
    return m.group(1)


# Names whose :root declaration is overridden in a @media (min|max-width)
# block — the resolved value is the 1440px view; the override list travels on
# $extensions.responsive.
MEDIA_OVERRIDES = {}
for rule in V.get("theme", []):
    ctx = " ".join(rule.get("context") or [])
    mq = re.search(r"@media \((min|max)-width: (\d+)px\)", ctx)
    if mq and rule.get("selector") == ":root":
        for n in rule.get("properties") or {}:
            tag = f"{mq.group(1)}-width:{mq.group(2)}px"
            MEDIA_OVERRIDES.setdefault(n, [])
            if tag not in MEDIA_OVERRIDES[n]:
                MEDIA_OVERRIDES[n].append(tag)


def resp_kw(name):
    if name in MEDIA_OVERRIDES:
        return {"responsive": "viewport-conditional: also declared under @media (" + ", ".join(MEDIA_OVERRIDES[name]) + "); resolved at 1440 x 900"}
    return {}


# ------------------------------------------------------------------- fonts
#
# --font-main/-secondary/-tertiary are declared on the Next.js font-variable
# classes (.__variable_* on <html>/<body>), so the probe cannot resolve them
# — the raw declaration string is the evidence and is labelled so.

fam = SPEC["core"].setdefault("font", {}).setdefault("family", {})
for key, name, desc in [
    ("gothic", "--font-main", "FrameGothic — every display heading on the site (a 400-600 variable face with an Arial-metric fallback), declared as --font-main."),
    ("machina", "--font-secondary", "NeueMachinaInktrap — labels, kickers and the mono-flavoured UI type, declared as --font-secondary."),
    ("inter", "--font-tertiary", "Inter — body copy and UI text (a 100-900 variable face), declared as --font-tertiary."),
]:
    raw, sel = RAW_DECL.get(name, (None, ""))
    if raw:
        fam[key] = lit(raw, "fontFamily",
                       f"css-var {name} declared on {sel or 'a scoped class'} (raw/css-vars.json); the probe cannot resolve a class-scoped declaration",
                       desc)
    elif name in R:
        fam[key] = var(name, "fontFamily", description=desc)

font = SPEC["core"]["font"]
if declared("--font-size-base") is not None:
    font.setdefault("size", {})["base"] = lit(declared("--font-size-base"), "dimension",
        f"{DECL_SRC}: --font-size-base", "The 1.6rem (16px) root font size the rem grid is built on.")

# ---------------------------------------------------------- core scales
#
# The palette: --color-grey-* under color.grey, the five brand hues (and
# their -light/-dark/-NN steps) under color.brand.<hue>, the alpha ladders
# under color.alpha.*, every other --color-* name under color.*. The
# --overlay-* roles under overlay.*.

color = SPEC["core"].setdefault("color", {})
HUES = ("coral", "iris", "electric", "cobalt", "turquoise-triumph")


def camel(s):
    return re.sub(r"-([a-z0-9])", lambda m: m.group(1).upper(), s)


for name in sorted(k for k in R if k.startswith("--color-") and declared(k) is not None):
    rest = name[len("--color-"):]
    if rest.startswith("alpha-"):
        path = "color.alpha." + ".".join(camel(p) for p in rest[len("alpha-"):].split("-"))
    elif rest.startswith("grey-"):
        path = "color.grey." + rest[len("grey-"):]
    elif rest.split("-")[0] in HUES:
        hue, _, sub = rest.partition("-")
        path = "color.brand." + hue + ("." + camel(sub) if sub else ".default")
    elif re.fullmatch(r"[a-z]+-\d+", rest) and rest.split("-")[0] in HUES:
        path = "color.brand." + rest.split("-")[0] + ".alpha" + rest.split("-")[1]
    else:
        path = "color." + camel(rest)
    emit_at(SPEC["core"], path, decl_color(name), name)

over = SPEC["core"].setdefault("overlay", {})
for name in sorted(k for k in R if k.startswith("--overlay-") and declared(k) is not None):
    over[camel(name[len("--overlay-"):])] = decl_color(name)

spacing = SPEC["core"].setdefault("spacing", {})
for name in sorted(k for k in R if re.fullmatch(r"--spacer-\d+", k)):
    spacing[name[len("--spacer-"):]] = decl(name)

radius_alias = {}
radii = SPEC["core"].setdefault("radius", {})
for name in sorted(k for k in R if re.fullmatch(r"--(border-)?radius-[a-z0-9-]+", k)):
    key = camel(re.sub(r"^--(border-)?radius-", "", name))
    radii[key] = decl(name)
    v = declared(name)
    if v:
        radius_alias[norm_len(v)] = key

layout = SPEC["core"].setdefault("layout", {})
grid = layout.setdefault("grid", {})
for name, key in [("--grid-number-of-columns", "columns"), ("--grid-max-content-width", "maxContentWidth")]:
    if declared(name) is not None:
        grid[key] = num_decl(name) if key == "columns" else decl(name)
        grid[key].update(resp_kw(name))
for name, key in [("--global-max-width", "maxWidth"), ("--nav-height", "navHeight"), ("--nav-height-padded", "navHeightPadded")]:
    if declared(name) is not None:
        layout[key] = decl(name)
        layout[key].update(resp_kw(name))

mo = SPEC["core"].setdefault("motion", {})
dur = mo.setdefault("duration", {})
for name in sorted(k for k in R if re.fullmatch(r"--duration-[a-z0-9-]+|--animation-duration|--card-hover-duration", k)):
    key = camel(re.sub(r"^--(duration|animation-duration|card-hover-duration)-?", "", name) or "default")
    dur[key] = lit(declared(name), "duration", f"{DECL_SRC}: {name}", f"The declared `{name}` duration.")
ease = mo.setdefault("easing", {})
for name in sorted(k for k in R if re.fullmatch(r"--ease-[a-z-]+|--card-hover-ease", k)):
    key = camel(re.sub(r"^--(ease|card-hover-ease)-?", "", name) or "default")
    ease[key] = lit(declared(name), "cubicBezier", f"{DECL_SRC}: {name}", f"The declared `{name}` easing.")

zx = SPEC["core"].setdefault("zIndex", {})
for name in sorted(k for k in R if k.startswith("--z-index-")):
    zx[camel(name[len("--z-index-"):])] = num_decl(name)

# ----------------------------------------------------- measured roles
#
# Roles measured on the real pages; each aliases to the declared palette
# token its value matches.

PALETTE_ALIAS = {norm_color(R[n]): EMITTED[n] for n in sorted(EMITTED) if EMITTED[n].startswith("color.") and norm_color(R.get(n, "")).startswith(("#", "rgba"))}
# Prefer the neutral grey and the accent role over a brand-tint duplicate:
# the same #fcfcfc is both color.grey.100 and color.accent; the grey step
# names the scale the site is built on.
ALIAS_FIRST = ["color.grey.100", "color.grey.00", "color.grey.05", "color.brand.cobalt.default", "color.accent.default"]
PALETTE_ALIAS = {}
for n in sorted(EMITTED, key=lambda n: (ALIAS_FIRST.index(EMITTED[n]) if EMITTED[n] in ALIAS_FIRST else len(ALIAS_FIRST), n)):
    p = EMITTED.get(n)
    v = norm_color(R.get(n, ""))
    if p and p.startswith("color.") and v.startswith(("#", "rgba")):
        PALETTE_ALIAS.setdefault(v, p)


def semcolor(raw, src, desc):
    alias = PALETTE_ALIAS.get(norm_color(raw))
    value = f"{{{alias}}}" if alias else norm_color(raw)
    return lit(value, "color", src + (f"; matches declared {alias}" if alias else ""), desc)


sem = SPEC["dark"]
for path, comp, state, prop, desc in [
    ("theme.bg", "page-field", "default", "backgroundColor",
     "The near-black page field every public page paints."),
    ("theme.fg.default", "hero-h1", "default", "color",
     "The #fcfcfc ink on display copy, headings and body (grey-100)."),
    ("theme.fg.muted", "section-h2", "default", "color",
     "The section-heading ink."),
    ("theme.fg.nav", "nav-pricing", "default", "color",
     "The header link ink."),
    ("theme.btn.primary.bg", "nav-cta", "default", "backgroundColor",
     "The white fill of the 'Start Free Trial' pill — the site's primary action inverts to ink-on-paper."),
    ("theme.btn.primary.fg", "nav-cta", "default", "color",
     "The near-black text on the white CTA pill."),
    ("theme.btn.primary.hoverBg", "nav-cta", "hover", "backgroundColor",
     "The CTA pill's hover fill."),
    ("theme.border.focus", "nav-cta", "focus-visible", "outlineColor",
     "The keyboard focus ring colour on the header CTA."),
    ("theme.btn.secondary.border", "hero-tour", "default", "borderTopColor",
     "The 'Take a Product Tour' ghost button's border."),
    ("theme.btn.secondary.fg", "hero-tour", "default", "color",
     "The ghost button's ink."),
    ("theme.banner.bg", "announcement", "default", "backgroundColor",
     "The announcement banner's cobalt-violet fill."),
    ("theme.banner.fg", "announcement", "default", "color",
     "The announcement banner's ink."),
    ("theme.surface.card", "plan-card", "default", "backgroundColor",
     "The plan card's raised dark fill on /pricing."),
    ("theme.form.field.ink", "form-email", "default", "color",
     "The contact field's text ink."),
    ("theme.form.placeholder", "form-email", "default", "placeholder",
     "The field label/placeholder ink."),
    ("theme.form.field.border", "form-email", "default", "borderBottomColor",
     "The contact field's underline border."),
    ("theme.form.submit.bg", "form-submit", "default", "backgroundColor",
     "The contact form 'Submit' pill fill."),
    ("theme.form.submit.fg", "form-submit", "default", "color",
     "The 'Submit' pill text."),
    ("theme.fg.footer", "footer-link", "default", "color",
     "The footer link ink."),
]:
    try:
        if prop == "color":
            raw = ts(comp, state, "color")
            src = f"computed color of {comp} {state} — the first text node's reading where the kit recorded one (raw/components-computed.json)"
        elif prop == "placeholder":
            raw = (C[comp]["states"][state].get("placeholder") or {}).get("color")
            src = f"computed ::placeholder color of {comp} {state} (raw/components-computed.json)"
        elif prop == "insetShadowColor":
            raw = inset_shadow_color(comp, state)
            src = f"the inset box-shadow layer painted on {comp} {state} (raw/components-computed.json)"
        else:
            raw = st(comp, state)[prop]
            src = f"computed {prop} of {comp} {state} (raw/components-computed.json)"
        if raw in (None, ""):
            raise KeyError(prop)
        emit_at(sem, path, semcolor(raw, src, desc))
    except KeyError:
        pass

# The declared roles that no component spec named: --main-font-color and
# --color-accent(-default) emit as declared theme roles too.
if declared("--main-font-color") is not None:
    sem.setdefault("theme", {}).setdefault("fg", {})["declared"] = var("--main-font-color", "color",
        description="The declared --main-font-color ink role (#fcfcfc).")
if declared("--color-accent") is not None:
    emit_at(sem, "theme.accent", var("--color-accent", "color",
        description="The declared --color-accent role — the light-grey accent (#f5f5f8)."), "--color-accent")

# ------------------------------------------------------------- type ramp
#
# The site typesets through CSS-module classes rather than size variables
# (only --font-size-base is declared), so the ramp is measured.

size_alias = {str(declared("--font-size-base")): "font.size.base"} if declared("--font-size-base") else {}
for key, comp, state, desc in [
    ("hero", "hero-h1", "default", "The home hero display heading (FrameGothic 80px at 1440)."),
    ("sectionH2", "section-h2", "default", "A section heading size."),
    ("navLink", "nav-pricing", "default", "The header link size."),
    ("button", "nav-cta", "default", "The pill button label size."),
    ("body", "footer-link", "default", "Footer/body copy size."),
    ("priceH1", "price-h1", "default", "The /pricing masthead size."),
]:
    try:
        raw = ts(comp, state, "fontSize") or st(comp, state)["fontSize"]
        src = f"computed fontSize of {comp} {state} (raw/components-computed.json)"
        alias = size_alias.get(raw)
        SPEC["core"]["font"].setdefault("size", {}).setdefault("measured", {})[key] = lit(
            f"{{{alias}}}" if alias else raw, "dimension",
            src + (f"; matches declared {alias}" if alias else ""), desc)
    except KeyError:
        pass

for key, comp, state, prop, desc in [
    ("heroWeight", "hero-h1", "default", "fontWeight", "The hero display weight (FrameGothic 400-600 variable)."),
    ("buttonWeight", "nav-cta", "default", "fontWeight", "The pill label weight."),
]:
    try:
        raw = ts(comp, state, prop) or st(comp, state)[prop]
        SPEC["core"]["font"].setdefault("weight", {})[key] = lit(
            int(float(raw)) if re.fullmatch(r"[\d.]+", str(raw)) else raw, "fontWeight" if re.fullmatch(r"[\d.]+", str(raw)) else "other",
            f"computed {prop} of {comp} {state} (raw/components-computed.json)", desc)
    except KeyError:
        pass

for key, comp, state, desc in [
    ("hero", "hero-h1", "default", "The hero display letter-spacing."),
    ("navLink", "nav-pricing", "default", "The header link tracking."),
]:
    try:
        raw = ts(comp, state, "letterSpacing") or st(comp, state)["letterSpacing"]
        SPEC["core"]["font"].setdefault("tracking", {})[key] = lit(
            raw, "dimension" if re.fullmatch(r"-?[\d.]+(px|rem)", str(raw)) else "other",
            f"computed letterSpacing of {comp} {state} (raw/components-computed.json)", desc)
    except KeyError:
        pass

# ------------------------------------------------------------------ shape

for key, comp, state, prop, desc in [
    ("cta", "nav-cta", "default", "borderTopLeftRadius", "The CTA pill radius."),
    ("navLink", "nav-pricing", "default", "borderTopLeftRadius", "The header link radius."),
    ("card", "plan-card", "default", "borderTopLeftRadius", "The plan-card corner radius."),
    ("field", "form-email", "default", "borderTopLeftRadius", "The contact field radius."),
    ("panel", "nav-panel", "default", "borderTopLeftRadius", "The mega-menu panel corner radius."),
    ("menuBtn", "m-menu-btn", "default", "borderTopLeftRadius", "The phone menu button radius."),
]:
    try:
        v = norm_len(st(comp, state)[prop])
        src = f"computed {prop} of {comp} {state} (raw/components-computed.json)"
        dkey = radius_alias.get(v)
        if dkey:
            radii[key] = lit(f"{{radius.{dkey}}}", "dimension", src + f"; matches declared --radius-{dkey}", desc)
        else:
            radii[key] = lit(v, "dimension" if re.fullmatch(r"-?[0-9.]+(px|rem)", v or "") else "other", src, desc)
    except KeyError:
        pass

# ------------------------------------------------------------------ motion

try:
    s = st("nav-cta", "default")
    dur_, ease_ = s.get("transitionDuration"), s.get("transitionTimingFunction")
    if dur_ and dur_ != "0s":
        props = [p.strip() for p in s.get("transitionProperty", "all").split(",") if p.strip()]
        durs = [d.strip() for d in dur_.split(",")]
        tfs = re.findall(r"cubic-bezier\([^)]*\)|steps\([^)]*\)|[a-z-]+", ease_ or "")
        parts = []
        for i, p in enumerate(props):
            d = durs[i % len(durs)]
            if d == "0s":
                continue
            parts.append(f"{p} {d} {tfs[i % len(tfs)] if tfs else ''}".strip())
        if parts:
            mo["control"] = lit(", ".join(parts), "other",
                "computed transition of nav-cta default (raw/components-computed.json); the --duration-*/--ease-* steps are the declared durations and curves",
                "The control transition on the header CTA.")
except KeyError:
    pass

# ------------------------------------------------------------- components

comp = SPEC["component"]
for name, cname, state, prop, ty_, desc in [
    ("topbar-height", "mkt-header", "default", "h", "dimension", "The fixed site header bar height."),
    ("announcement-height", "announcement", "default", "h", "dimension", "The announcement banner height."),
    ("cta-height", "nav-cta", "default", "h", "dimension", "The header CTA pill height."),
    ("nav-panel-width", "nav-panel", "default", "w", "dimension", "The open mega-menu panel width."),
    ("nav-panel-height", "nav-panel", "default", "h", "dimension", "The open mega-menu panel height."),
    ("hero-headline-width", "hero-h1", "default", "w", "dimension", "The hero display heading's measure."),
    ("field-height", "form-email", "default", "h", "dimension", "The contact field height."),
    ("submit-width", "form-submit", "default", "w", "dimension", "The contact 'Submit' pill width."),
    ("submit-height", "form-submit", "default", "h", "dimension", "The contact 'Submit' pill height."),
    ("plan-card-width", "plan-card", "default", "w", "dimension", "The plan-card column width."),
    ("toggle-width", "price-toggle", "default", "w", "dimension", "The Monthly/Annually toggle's Monthly side width."),
    ("mobile-topbar-height", "m-topbar", "default", "h", "dimension", "The phone header bar height."),
]:
    try:
        v = rc(cname, state, prop)
        comp[name] = lit(("%g" % v) + "px" if isinstance(v, (int, float)) else str(v) + "px",
                         ty_, f"measured {prop} of {cname} {state} (raw/components-computed.json)", desc)
    except KeyError:
        pass

# accounts.frame.io/welcome is a different stack (styled-components, a light
# page) that does not share the marketing --* layer; its measured values are
# kept as literals, honestly labelled.
shell = comp.setdefault("productShell", {})
for name, cname, state, prop, ty_, desc in [
    ("login-panel-width", "login-panel", "default", "w", "dimension", "The sign-in card width on accounts.frame.io/welcome."),
    ("login-field-height", "login-email", "default", "h", "dimension", "The sign-in e-mail field height."),
    ("login-field-bg", "login-email", "default", "backgroundColor", "color", "The sign-in e-mail field fill."),
    ("login-submit-fill", "login-submit", "default", "backgroundColor", "color", "The 'Let's go' button fill (the accounts stack's cobalt)."),
    ("login-submit-ink", "login-submit", "default", "color", "color", "The 'Let's go' button text."),
]:
    try:
        if prop in ("w", "h"):
            v = rc(cname, state, prop)
            shell[name] = lit(("%g" % v) + "px", ty_, f"measured {prop} of {cname} {state} on the accounts sign-in surface (raw/components-computed.json)", desc)
        else:
            shell[name] = lit(norm_color(st(cname, state)[prop]), "color",
                f"computed {prop} of {cname} {state} on the accounts sign-in surface (raw/components-computed.json)", desc)
    except KeyError:
        pass

(RAW / "component-tokens.json").write_text(json.dumps(SPEC, indent=2, ensure_ascii=False) + "\n")
print("component-tokens.json:", {k: len(v) for k, v in SPEC.items() if k != "_about"})
