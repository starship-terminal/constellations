#!/usr/bin/env python3
"""Write raw/component-tokens.json, the token spec build_tokens.py reads.

Fernand ships three public surfaces on one flat :root palette
(--white/--grey-light/--grey/--grey-medium/--grey-strong/--black/--blue/
--blue-pale/--orange/--orange-pale/--red/--red-pale/--green/--green-pale/
--green-dark/--border/--border-strong):

  getfernand.com        the Nuxt marketing site — light only, the palette in
                        an inline :root block, self-hosted Inter
  app.getfernand.com    the Vue SPA — the same palette names with its own
                        grey-family resolutions (--grey #e6e9eb,
                        --grey-medium #5e6271, --grey-strong #9fa3b5) plus
                        --orange-pale/--green-pale, the scoped overrides and
                        component vars (--head/--subtle/--focused/--disabled/
                        --search/--compose/--filters/--inline/--tooltip/…);
                        /auth/login and /create are reachable signed out
  help.getfernand.com   the Nuxt docs site — the same palette plus
                        --grey-medium/--grey-strong and a body.dark-mode remap
                        behind the real "Switch to dark mode" link

The palette names are the semantic layer — the sites style components
straight off them — so every shared name is emitted at the same path in the
set its host paints: core holds the marketing resolution (the canonical
palette), app overrides at those paths with the SPA's own values plus its
app-only names, and dark overrides them with the docs dark-mode resolution.
Measured computed styles from raw/components-computed.json fill the rest:

  core      Inter + the measured marketing type ramp, radius scale and
            control transition
  light     measured semantic roles (ink, surfaces, CTA fill) aliased to the
            palette values they match
  app       the SPA vocabulary at its own resolutions + the measured
            login/signup roles
  dark      the docs dark palette + roles measured under body.dark-mode
            (the real toggle, not a reconstruction)
"""

import json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
V = json.loads((RAW / "css-vars.json").read_text())
RV = V.get("resolved", {})
R = {n: (v.get("value", v.get("raw")) if isinstance(v, dict) else v) for n, v in RV.get("light", {}).items()}
RH = {n: (v.get("value", v.get("raw")) if isinstance(v, dict) else v) for n, v in RV.get("help", {}).items()}
A = {n: (v.get("value", v.get("raw")) if isinstance(v, dict) else v) for n, v in RV.get("app", {}).items()}
D = {n: (v.get("value", v.get("raw")) if isinstance(v, dict) else v) for n, v in RV.get("dark", {}).items()}
C = json.loads((RAW / "components-computed.json").read_text())["components"]

# Which host's sheets declare each theme-bin name — the file label vars.mjs
# stamps on every rule starts with the host word.
HOST_NAMES = {"marketing": set(), "app": set(), "help": set()}
for rule in V.get("theme", []):
    host = (rule.get("file") or "").split(" ", 1)[0]
    if host in HOST_NAMES:
        HOST_NAMES[host].update(rule.get("properties") or {})

SPEC = {"_about": (
    "The token tree build_tokens.py turns into tokens.json. Fernand's three "
    "public hosts declare one flat palette on :root (raw/css-vars.json) and "
    "each resolves it slightly differently — core.* carries the marketing "
    "resolution as the canonical palette, and every host re-emits its "
    "vocabulary at the same paths in its surface set: light (marketing), "
    "help (docs light), app (the SPA's grey family and --viewport-"
    "vars) and dark (the docs body.dark-mode remap) — so each theme resolves "
    "its own values. Measured roles alias to the declared values they match."),
    "core": {}, "light": {}, "help": {}, "app": {}, "dark": {}, "component": {}}


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


def lit(value, ty, src, desc):
    return {"value": norm_color(value) if ty == "color" else value, "type": ty, "source": src, "description": desc}


def var(name, ty="color", **kw):
    d = {"var": name, "type": ty}
    d.update(kw)
    return d


EMITTED = {}   # variable name -> dotted token path it was actually written to
_OWNER = {}    # dotted token path -> variable name holding it


def _leaf(d):
    return isinstance(d, dict) and ("var" in d or "value" in d)


def emit(root, name, leaf):
    """Write `leaf` at name's dotted path.

    A declared name can be both a leaf and the parent of other names. When a
    leaf and a group must share a node, the leaf moves inside the group under
    the first free of `default`, `base`, `self` — never silently overwriting
    tokens that resolve to different states.
    """
    node = root
    parts = name[2:].split("-")
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
    path = ".".join(parts)
    if last in node and not _leaf(node[last]):
        for key in ("default", "base", "self"):
            if key not in node[last]:
                node[last][key] = leaf
                path += "." + key
                break
        else:
            raise ValueError(f"{name}: no free key to hold the leaf beside its group")
    else:
        if last in node:
            raise ValueError(f"{name}: duplicate token path {path}")
        node[last] = leaf
    EMITTED[name] = path
    _OWNER[path] = name


DECL_SRC = "declared design-system variable in the host's own stylesheet (raw/css-vars.json)"


def declared(name, theme="light"):
    pool = {"light": R, "help": RH, "app": A, "dark": D}[theme]
    v = pool.get(name)
    return v if v not in (None, "") else None


def norm_len(v):
    m = re.fullmatch(r"(-?[\d.]+[eE][+-]?\d+)(px|rem)", str(v).strip())
    if not m:
        return v
    return f"{float(m.group(1)):f}".rstrip("0").rstrip(".") + m.group(2)


COLOR_V = re.compile(r"(#[0-9a-fA-F]{3,8}|rgba?\([^)]*\)|hsla?\([^)]*\)|(ok)?lab\([^)]*\)|(ok)?lch\([^)]*\)|color-mix\([^)]*\))")


def leaf_type(name, val):
    """The DTCG type a declared value honestly is."""
    v = str(val or "").strip()
    if COLOR_V.fullmatch(v):
        return "color"
    if re.fullmatch(r"-?\d+(\.\d+)?(px|rem)", v):
        return "dimension"
    if re.fullmatch(r"[\d.]+m?s", v):
        return "duration"
    if "cubic-bezier" in v or v in ("ease", "ease-in", "ease-out", "ease-in-out", "linear"):
        return "cubicBezier"
    return "other"


def painted(comp, state, key):
    """A reading from the kit's paint list — the layers actually painted."""
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
    sh = painted(comp, state, "shadow")
    m = re.search(COLOR_V.pattern + r"(?:\s+-?[\d.]+px){2,4}\s+inset", sh)
    if not m:
        raise KeyError("insetShadowColor")
    return m.group(1)


# ------------------------------------------------------------------- fonts
#
# The palette sites ship self-hosted Inter (300–700 + italics) but no font
# custom property — the family is measured on real components. The app adds
# --viewport-height, emitted with its set below.

fam = SPEC["core"].setdefault("font", {}).setdefault("family", {})
try:
    v = st("hero-h1", "default")["fontFamily"]
    fam["inter"] = lit(v, "fontFamily",
        "computed fontFamily of hero-h1 default (raw/components-computed.json); the self-hosted Inter @font-face faces in raw/css-vars.json",
        "Inter — the self-hosted family every surface sets (weights 300–700 plus italics; the docs and app use a narrower weight band).")
except KeyError:
    pass

weights = SPEC["core"].setdefault("font", {}).setdefault("weight", {})
# Names follow the measured values, not the usual weight names: the public
# surfaces set nothing heavier than 600, and the display headings are 400.
for key, comp, state, desc in [
    ("regular", "hero-sub", "default", "The 400 body weight."),
    ("medium", "nav-cta", "default", "The 500 weight on buttons and nav links."),
    ("semibold", "pricing-eyebrow", "default", "The 600 weight on plan eyebrows, card titles and table heads — the heaviest weight the public surfaces set."),
    ("display", "hero-h1", "default", "The display-heading weight: the 38px masthead measures 400, not bold."),
]:
    try:
        w = ts(comp, state, "fontWeight") or st(comp, state)["fontWeight"]
        if w:
            weights[key] = lit(int(float(w)), "fontWeight",
                f"computed fontWeight of {comp} {state} (raw/components-computed.json)", desc)
    except (KeyError, ValueError):
        pass

# Measured marketing type ramp — the marketing sheets carry no size
# variables, so the ramp is computed px on real components, honestly labelled.
sizes = SPEC["core"].setdefault("font", {}).setdefault("size", {})
for key, comp, state, desc in [
    ("hero", "hero-h1", "default", "The 38px hero masthead."),
    ("lede", "hero-sub", "default", "The hero standfirst size."),
    ("quote", "testimonial", "default", "The 22px testimonial display copy."),
    ("body", "channels-card", "default", "The card/body copy size."),
    ("button", "nav-cta", "default", "The 14px button/nav size."),
    ("eyebrow", "section-tag", "default", "The small eyebrow-pill size."),
    ("mobileHero", "m-hero-h1", "default", "The masthead at 390 wide."),
]:
    try:
        v = ts(comp, state, "fontSize") or st(comp, state)["fontSize"]
        sizes[key] = lit(v, "dimension", f"computed fontSize of {comp} {state} (raw/components-computed.json)", desc)
    except KeyError:
        pass

lh = SPEC["core"].setdefault("font", {}).setdefault("lineHeight", {})
for key, comp, state, desc in [
    ("hero", "hero-h1", "default", "The hero masthead leading."),
    ("body", "hero-sub", "default", "The body leading."),
    ("quote", "testimonial", "default", "The testimonial leading (1.55)."),
]:
    try:
        # Size and leading come off the same node: the wrapper's own style is
        # what children inherit, while the visible text can set its own pair —
        # testimonial's wrapper is 16/16 under the 22/34.1 quote text, so the
        # textStyle pair (when the kit recorded one) is the honest ratio.
        c = C[comp]["states"][state]
        t = c.get("textStyle") or {}
        fsraw = t.get("fontSize") or c["style"]["fontSize"]
        v = t.get("lineHeight") or c["style"]["lineHeight"]
        fs = float(fsraw[:-2])
        if v == "normal":
            lh[key] = lit("normal", "other", f"computed lineHeight of {comp} {state} (raw/components-computed.json)", desc)
        elif v.endswith("px"):
            lh[key] = lit(round(float(v[:-2]) / fs, 4), "number", f"computed lineHeight/fontSize of {comp} {state} ({v} over {fsraw}, raw/components-computed.json)", desc)
    except (KeyError, ValueError):
        pass

# ----------------------------------------------------------- core colors
#
# The marketing :root palette — the canonical resolution. The app and docs
# sets re-emit the shared names at these same paths with their own values.

PALETTE = re.compile(r"^--(white|grey(-\w+)?|black|blue(-\w+)?|orange(-\w+)?|red(-\w+)?|green(-\w+)?|border(-\w+)?)$")
mkt_names = sorted(n for n in HOST_NAMES["marketing"] if declared(n, "light") is not None)
help_names = sorted(n for n in HOST_NAMES["help"] if declared(n, "help") is not None)
app_names = sorted(n for n in HOST_NAMES["app"] if declared(n, "app") is not None)
dark_names = sorted(n for n in HOST_NAMES["help"] | HOST_NAMES["marketing"] if declared(n, "dark") is not None)

def emit_named(setroot, name, val):
    """Emit a declared name at its natural path in the set — the shared
    palette names land on identical paths in every surface set, which is the
    theme-override mechanism."""
    emit(setroot, name, var(name, leaf_type(name, val)))


for name in mkt_names:
    emit_named(SPEC["core"], name, R.get(name))

# The alias maps are collected in a second pass: emit() can rename a leaf to
# `name.default` when a later variable needs its path as a group (--blue ->
# blue.default when --blue-pale lands at blue.pale), and EMITTED is only final
# once the whole set is written.
color_alias = {}   # normalized colour -> token path for light-set aliasing
for name in mkt_names:
    color_alias.setdefault(norm_color(R.get(name)), EMITTED[name])

# ------------------------------------------------- per-surface vocabularies
#
# Every host re-emits its own declared names at the same emitted paths in
# its surface set — the palette paths the theme mechanism overrides:
# light — the marketing surface: the canonical palette already lives in core
#        (a source set in every theme), so light holds only the measured
#        semantic roles aliased back to it.
# help — the docs vocabulary resolved on the docs light shell: the shared
#        palette names carry the docs' own values (#f7fafc grey-light,
#        #5f667d grey-medium, #d1d5e6 border-strong).
# app — every app-declared name (palette names override core;
#       --viewport-height is a new path), resolved on the app shell.
# dark — the docs vocabulary resolved under body.dark-mode: palette names
#        override core with the remapped values.

for name in help_names:
    emit_named(SPEC["help"], name, RH.get(name))

help_alias = {}
for name in help_names:
    help_alias.setdefault(norm_color(RH.get(name)), EMITTED[name])

for name in app_names:
    emit_named(SPEC["app"], name, A.get(name))

app_alias = {}
for name in app_names:
    app_alias.setdefault(norm_color(A.get(name)), EMITTED[name])

for name in dark_names:
    if declared(name, "dark") is not None:
        emit_named(SPEC["dark"], name, D.get(name))

dark_alias = {}
for name in dark_names:
    if declared(name, "dark") is not None:
        dark_alias.setdefault(norm_color(D.get(name)), EMITTED[name])

# Measured roles alias to the declared token the value matches — inside the
# set the role lives in. Only the set's own declarations are safe targets:
# the hosts remap the shared palette names (dark --white is #161618), so an
# alias {white} written in the dark set resolves to the remapped value, not
# the measured #ffffff. A measured value that matches a canonical marketing
# name but not the surface's own resolution stays a literal.
role_alias = {
    "light": dict(color_alias),
    "help": help_alias,
    "app": app_alias,
    "dark": dark_alias,
}


def semcolor(raw, src, desc, theme="light"):
    alias = role_alias[theme].get(norm_color(raw))
    value = f"{{{alias}}}" if alias else norm_color(raw)
    return lit(value, "color", src + (f"; matches declared {alias}" if alias else ""), desc)


sem, hsem, asem, dsem = SPEC["light"], SPEC["help"], SPEC["app"], SPEC["dark"]
for root, theme, key, comp, state, prop, group, desc in [
    (sem, "light", "ink", "hero-h1", "default", "color", "text",
     "The near-black ink on headings and body copy (the --black navy)."),
    (sem, "light", "muted", "hero-sub", "default", "color", "text",
     "The mid-grey lede/secondary ink."),
    (sem, "light", "cta-fill", "hero-cta", "default", "backgroundColor", "action",
     "The near-black fill of the primary buttons."),
    (sem, "light", "cta-ink", "hero-cta", "default", "color", "action",
     "The white text on the dark buttons."),
    (sem, "light", "card", "channels-card", "default", "backgroundColor", "surface",
     "The light-grey card surface (the --grey-light field)."),
    (sem, "light", "focus-ring", "nav-cta", "focus-visible", "outlineColor", "border",
     "The keyboard focus ring on controls, where the browser paints one."),
    (sem, "light", "link", "nav-link", "default", "color", "text",
     "The nav/footer link ink."),
    (hsem, "help", "card", "help-card", "default", "backgroundColor", "surface",
     "The docs collection-card surface in light."),
    (hsem, "help", "ink", "help-h1", "default", "color", "text",
     "The docs article heading ink in light."),
    (hsem, "help", "field-bg", "help-search", "default", "backgroundColor", "surface",
     "The docs search field fill in light."),
    (asem, "app", "ink", "login-h1", "default", "color", "text",
     "The app's heading ink on the signed-out forms."),
    (asem, "app", "field-bg", "login-field", "default", "backgroundColor", "surface",
     "The sign-in field fill."),
    (asem, "app", "field-ink", "login-field", "default", "color", "text",
     "The field text ink."),
    (asem, "app", "primary-fill", "login-submit", "default", "backgroundColor", "action",
     "The app primary button fill."),
    (asem, "app", "primary-ink", "login-submit", "default", "color", "action",
     "The app primary button text."),
    (dsem, "dark", "page", "hd-page", "default", "backgroundColor", "background",
     "The docs page field under dark-mode."),
    (dsem, "dark", "ink", "hd-h1", "default", "color", "text",
     "The docs heading ink under dark-mode."),
    (dsem, "dark", "card", "hd-card", "default", "backgroundColor", "surface",
     "The docs card surface under dark-mode."),
    (dsem, "dark", "muted", "hd-prose", "default", "color", "text",
     "The docs body/prose ink under dark-mode."),
    (dsem, "dark", "link", "hd-nav-item", "default", "color", "text",
     "The active docs nav item ink under dark-mode (the blue)."),
    (dsem, "dark", "raised", "hd-nav-item", "default", "backgroundColor", "surface",
     "The filled list-item surface under dark-mode."),
]:
    try:
        if prop == "color":
            raw = ts(comp, state, "color")
            src = f"computed color of {comp} {state} — the first text node's reading where the kit recorded one (raw/components-computed.json)"
        elif prop == "insetShadowColor":
            raw = inset_shadow_color(comp, state)
            src = f"the inset box-shadow layer painted on {comp} {state} (raw/components-computed.json)"
        else:
            raw = st(comp, state)[prop]
            src = f"computed {prop} of {comp} {state} (raw/components-computed.json)"
        if raw in (None, ""):
            raise KeyError(prop)
        root.setdefault(group, {})[key] = semcolor(raw, src, desc, theme)
    except KeyError:
        pass

# The dark muted role's fallback when the dedicated prose paragraph was not
# captured: the page wrapper's own colour is the inherited body ink (the first
# text *node* inside it is the ⌘K shortcut, not body copy, so textStyle is not
# a safe source here).
if "muted" not in dsem.get("text", {}):
    try:
        raw = st("hd-page", "default")["color"]
        dsem.setdefault("text", {})["muted"] = semcolor(
            raw, "computed color of hd-page default — the wrapper's own colour, the inherited body-copy ink (raw/components-computed.json)",
            "The docs body/prose ink under dark-mode.", "dark")
    except KeyError:
        pass

# The page field: the marketing body paints on the white root field, and the
# docs site keeps that convention under dark-mode — the measured wrappers are
# transparent over the root field, so both page tokens alias the declared
# --white rather than a transparent reading.
if "--white" in EMITTED:
    sem.setdefault("background", {})["page"] = lit(
        "{%s}" % EMITTED["--white"], "color",
        "the body/html field behind every marketing page (screenshots/home-light-*.png); the declared --white",
        "The white page field — every marketing and docs light page paints on it.")
    dsem.setdefault("background", {})["page"] = lit(
        "{%s}" % EMITTED["--white"], "color",
        "the body/html field behind the docs pages under body.dark-mode (screenshots/help-dark-*.png) — the docs redeclare --white #161618; the measured wrappers are transparent over it",
        "The docs dark page field — the remapped --white.")

# ------------------------------------------------------------------ shape
#
# The marketing sheets declare no radius variables; the scale is measured on
# real controls and cards.

radii = SPEC["core"].setdefault("radius", {})
for key, comp, state, prop, desc in [
    ("control", "nav-cta", "default", "borderTopLeftRadius", "The ~6px radius on header buttons and links."),
    ("button", "hero-cta", "default", "borderTopLeftRadius", "The 8px radius on the primary buttons."),
    ("card", "channels-card", "default", "borderTopLeftRadius", "The 10px card radius."),
    ("panel", "price-free", "default", "borderTopLeftRadius", "The 16px pricing-card radius."),
    ("pill", "section-tag", "default", "borderTopLeftRadius", "The 40px eyebrow-pill radius."),
    ("field", "login-field", "default", "borderTopLeftRadius", "The app field radius."),
    ("bubble", "launcher", "default", "borderTopLeftRadius", "The widget launcher bubble radius."),
]:
    try:
        if prop == "paint:radius":
            v = norm_len(painted(comp, state, "radius"))
            src = f"the painted radius of {comp}'s rounded child {state} (raw/components-computed.json paint list)"
        else:
            v = norm_len(st(comp, state)[prop])
            src = f"computed {prop} of {comp} {state} (raw/components-computed.json)"
        radii[key] = lit(v, "dimension" if re.fullmatch(r"[0-9.]+(px|rem)", v or "") else "other", src, desc)
    except KeyError:
        pass

# ------------------------------------------------------------------ motion

mo = SPEC["core"].setdefault("motion", {})
for comp in ("hero-cta", "nav-cta", "wpg-color"):
    try:
        s = st(comp, "default")
        dur, ease = s.get("transitionDuration"), s.get("transitionTimingFunction")
        if dur and dur != "0s":
            # zip the lists per index, wrapping the shorter as CSS does: "color 0.2s ease, background-color
            # 0.2s ease", never every property with the whole duration and easing lists
            split = lambda v: [x.strip() for x in re.split(r",(?![^(]*\))", v or "") if x.strip()]
            props, durs, eases = split(s.get("transitionProperty", "all")) or ["all"], split(dur), split(ease) or ["ease"]
            val = ", ".join(f"{p} {durs[i % len(durs)]} {eases[i % len(eases)]}" for i, p in enumerate(props))
            mo["control"] = lit(val, "other",
                f"computed transition of {comp} default (raw/components-computed.json)",
                "The control transition the site puts on buttons and swatches.")
            break
    except KeyError:
        continue

# ------------------------------------------------------------- components
#
# Theme-independent measured geometry.

comp_t = SPEC["component"]
for name, cname, state, prop, ty_, desc in [
    ("topbar-height", "mkt-header", "default", "h", "dimension", "The marketing header bar height."),
    ("hero-cta-height", "hero-cta", "default", "h", "dimension", "The primary button height."),
    ("nav-cta-height", "nav-cta", "default", "h", "dimension", "The header button height."),
    ("hero-width", "hero-h1", "default", "w", "dimension", "The hero masthead measure."),
    ("channel-card-width", "channels-card", "default", "w", "dimension", "The 300px channel-card width."),
    ("pricing-card-width", "price-free", "default", "w", "dimension", "The pricing-card width."),
    ("tag-height", "section-tag", "default", "h", "dimension", "The eyebrow-pill height."),
    ("launcher-size", "launcher", "default", "h", "dimension", "The widget launcher bubble size."),
    ("ai-menu-width", "ai-setup-item", "default", "w", "dimension", "The Install-with-AI menu width."),
    ("help-search-width", "help-search", "default", "w", "dimension", "The docs search field width."),
    ("help-card-width", "help-card", "default", "w", "dimension", "The docs collection-card width."),
    ("mobile-topbar-height", "m-topbar", "default", "h", "dimension", "The phone header height."),
]:
    try:
        v = rc(cname, state, prop)
        comp_t[name] = lit(("%g" % v) + "px" if isinstance(v, (int, float)) else str(v) + "px",
                          ty_, f"measured {prop} of {cname} {state} (raw/components-computed.json)", desc)
    except KeyError:
        pass

# The signed-out app forms: measured literals on their own surface.
appf = comp_t.setdefault("app", {})
for name, cname, state, prop, ty_, desc in [
    ("login-h1-size", "login-h1", "default", "fontSize", "other", "The 25px 'Welcome back' sign-in heading."),
    ("field-height", "login-field", "default", "h", "dimension", "The sign-in field height."),
    ("field-width", "login-field", "default", "w", "dimension", "The sign-in field width."),
    ("submit-height", "login-submit", "default", "h", "dimension", "The primary submit height."),
    ("create-panel-width", "create-panel", "default", "w", "dimension", "The signup intro panel width."),
]:
    try:
        if prop in ("w", "h"):
            v = rc(cname, state, prop)
            appf[name] = lit(("%g" % v) + "px", ty_, f"measured {prop} of {cname} {state} on app.getfernand.com (raw/components-computed.json)", desc)
        else:
            v = st(cname, state)[prop]
            appf[name] = lit(v, ty_, f"computed {prop} of {cname} {state} on app.getfernand.com (raw/components-computed.json)", desc)
    except KeyError:
        pass

(RAW / "component-tokens.json").write_text(json.dumps(SPEC, indent=2, ensure_ascii=False) + "\n")
print("component-tokens.json:", {k: len(v) for k, v in SPEC.items() if k != "_about"})
