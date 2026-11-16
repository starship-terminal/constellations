#!/usr/bin/env python3
"""Write raw/component-tokens.json, the token spec build_tokens.py reads.

GlossGenius ships three public surfaces signed out, each with its own
declared vocabulary:

  glossgenius.com     the Webflow marketing site — light only. A bundled
                      Webflow-variables layer: --_color---primary--*
                      (gloss-black #17150e / gloss-white #f0f7f6 / gray-*),
                      --_color---super--* (a 16-hue accent family: amber,
                      cerulean, coral, fuchsia, gold, jade, mauve, midnight,
                      opal, orchid, pine, sage, sienna, smoke, sunset,
                      violet), --_color---primary-opacity--* alpha steps,
                      flat --bg-* names, plus the --_size---*px,
                      --_typography---*, --_layout---*, --_components---*
                      and stock --_apps---* collections and a
                      --_theme-v2---* layer. The marketing sheets also
                      carry [data-theme="dark"]/[data-theme="light"]
                      blocks from an embedded stylesheet — nothing signed
                      out sets the attribute, so they are declared evidence,
                      never a painted surface.

  app.glossgenius.com the Next.js SPA under CSS modules — the glossDS token
                      layer on :root and scoped .light/.dark classes:
                      --content-*, --surface-*, --gray-*/--gloss-gray-*,
                      --brand-* (gloss-black/gloss-white, gold/pink/sky
                      ramps, single-hue accents), --border-*, --space-*x,
                      --size-*x, --radius-*, --font-* and component vars
                      (--button-*, --input-*, --checkbox-*). /login,
                      /signup and /forgot-password paint the light set;
                      .dark is declared but nothing signed out applies it.

  honeyhivesalon.glossgenius.com  a real published booking website (every
                      business gets a public <name>.glossgenius.com site) —
                      its own CSS-module token family under
                      .tokens_glossDS__* classes: --button-*, --text-*,
                      --space-*, --chip-*, --input-*, --gray-*, --bg-* plus
                      layout-scoped overrides (OrganicLayout,
                      PlayfulLayout, BillboardLayout, CanvasLayout…). A
                      --widget-tokens dark class is declared for embedded
                      widgets; the site itself paints light.

Each host's names are emitted at their natural paths in the set whose host
declares them: core holds the marketing vocabulary (the canonical set),
app holds the app's glossDS layer, booking the booking site's layer.
Measured computed styles from raw/components-computed.json fill the
semantic roles and alias back to the declared values they match:

  core      the declared marketing vocabulary + the measured type ramp,
            radius scale and control transition
  light     measured semantic roles on the marketing surface (ink, CTA
            fills, card surfaces) aliased to the palette values they match
  app       the app's declared vocabulary + the measured auth-form roles
            (field fill, the primary submit fill and ink)
  booking   the booking site's declared vocabulary + the measured booking
            roles (service card, select control, BOOK button)
  component theme-independent measured geometry (bar heights, card and
            field sizes) hanging off core
"""

import json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
V = json.loads((RAW / "css-vars.json").read_text())
RV = V.get("resolved", {})
R = {n: (v.get("value", v.get("raw")) if isinstance(v, dict) else v) for n, v in RV.get("light", {}).items()}
A = {n: (v.get("value", v.get("raw")) if isinstance(v, dict) else v) for n, v in RV.get("app", {}).items()}
B = {n: (v.get("value", v.get("raw")) if isinstance(v, dict) else v) for n, v in RV.get("booking", {}).items()}
C = json.loads((RAW / "components-computed.json").read_text())["components"]

# Which host's sheets declare each theme-bin name — the file label vars.mjs
# stamps on every rule starts with the host word.
HOST_NAMES = {"marketing": set(), "app": set(), "booking": set()}
for binname in ("theme", "app"):
    for rule in V.get(binname, []):
        host = (rule.get("file") or "").split(" ", 1)[0]
        if host in HOST_NAMES:
            HOST_NAMES[host].update(rule.get("properties") or {})

SPEC = {"_about": (
    "The token tree build_tokens.py turns into tokens.json. GlossGenius's "
    "three public surfaces declare separate vocabularies "
    "(raw/css-vars.json): core.* carries the marketing site's Webflow "
    "variable layer and flat palette (including the declared but "
    "never-painted [data-theme=dark] declarations), app.* carries the "
    "glossDS layer the signed-out auth forms paint, booking.* the "
    "published booking site's own token family. Measured roles alias to "
    "the declared values they match, inside their own surface set."),
    "core": {}, "light": {}, "app": {}, "booking": {}, "component": {}}


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
    # Resolved values are not all strings — a var can resolve to a bare
    # number (opacity, a count). Those are not colours; return None for them.
    v = ("" if v is None else str(v)).strip()
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

    GlossGenius's Webflow layer names read --_color---primary--gloss-black:
    parts are sanitized (empty segments dropped, leading underscores
    stripped) so the path is color.primary.gloss.black. A declared name can
    be both a leaf and the parent of other names; when a leaf and a group
    must share a node, the leaf moves inside the group under the first free
    of `default`, `base`, `self` — never silently overwriting tokens that
    resolve to different states.
    """
    node = root
    parts = [q for q in (p.lstrip("_") for p in name[2:].split("-")) if q]
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
    pool = {"light": R, "app": A, "booking": B}[theme]
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


def inner_fill(comp, state):
    """The first opaque painted layer inside the component — the fill the
    eye actually sees when the element's own box only paints a translucent
    or transparent outer shell."""
    c = C[comp]["states"][state]
    for p in c.get("paint") or []:
        bg = p.get("bg") or ""
        m = re.fullmatch(r"rgba?\(([\d.]+),\s*([\d.]+),\s*([\d.]+)(?:,\s*([\d.]+))?\)", bg)
        if m and (m.group(4) is None or float(m.group(4)) >= 1):
            return bg
    raise KeyError("innerFill")


# ------------------------------------------------------------------- fonts
#
# The marketing site and the app both set a Basel/Inter stack: the app
# declares --font-family-ui ('baselGrotesk'), --font-family-display
# ('baselClassic'), --font-family-base (Inter) and --font-fraunces /
# --font-beau-rivage display faces; the marketing sheets self-host the same
# faces through the Webflow CDN. The measured family comes off the hero.

fam = SPEC["core"].setdefault("font", {}).setdefault("family", {})
try:
    v = st("hero-h1", "default")["fontFamily"]
    fam["display"] = lit(v, "fontFamily",
        "computed fontFamily of hero-h1 default (raw/components-computed.json); the declared --font-family-* vars in raw/css-vars.json",
        "The display family the surfaces set on headings (baselGrotesk/baselClassic over Helvetica fallbacks).")
except KeyError:
    pass
try:
    v = st("home-prose", "default")["fontFamily"]
    fam["body"] = lit(v, "fontFamily",
        "computed fontFamily of home-prose default (raw/components-computed.json); the declared --font-family-base/--font-family-ui vars in raw/css-vars.json",
        "The body family on marketing copy.")
except KeyError:
    pass

weights = SPEC["core"].setdefault("font", {}).setdefault("weight", {})
for key, comp, state, desc in [
    ("regular", "plan-row", "default", "The 400 body weight on plan rows, FAQ and fields."),
    ("medium", "hero-eyebrow", "default", "The 500 weight on the eyebrow and app labels."),
    ("semibold", "nav-link", "default", "The 600 weight on nav links, buttons and card headings."),
    ("bold", "hero-h1", "default", "The display-heading weight."),
]:
    try:
        w = ts(comp, state, "fontWeight") or st(comp, state)["fontWeight"]
        if w:
            weights[key] = lit(int(float(w)), "fontWeight",
                f"computed fontWeight of {comp} {state} (raw/components-computed.json)", desc)
    except (KeyError, ValueError):
        pass

# Measured marketing type ramp — computed px on real components, honestly
# labelled.
sizes = SPEC["core"].setdefault("font", {}).setdefault("size", {})
for key, comp, state, desc in [
    ("display", "feat-h1", "default", "The feature-page display heading."),
    ("hero", "hero-h1", "default", "The hero masthead and section headings."),
    ("planName", "plan-card", "default", "The plan-name heading inside pricing cards."),
    ("button", "hero-cta", "default", "The hero-button size."),
    ("planCta", "plan-cta", "default", "The plan-CTA size."),
    ("faq", "faq-item", "default", "The FAQ-question and form-label size."),
    ("body", "plan-row", "default", "The body/nav size."),
    ("eyebrow", "hero-eyebrow", "default", "The eyebrow size."),
    ("mobileHero", "m-hero-h1", "default", "The masthead at 390 wide."),
]:
    try:
        v = ts(comp, state, "fontSize") or st(comp, state)["fontSize"]
        sizes[key] = lit(norm_len(v), "dimension", f"computed fontSize of {comp} {state} (raw/components-computed.json)", desc)
    except KeyError:
        pass

lh = SPEC["core"].setdefault("font", {}).setdefault("lineHeight", {})
for key, comp, state, desc in [
    ("hero", "hero-h1", "default", "The hero masthead leading."),
    ("body", "plan-row", "default", "The body leading."),
    ("eyebrow", "hero-eyebrow", "default", "The eyebrow leading."),
]:
    try:
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
# The marketing vocabulary — the canonical declaration. The Webflow
# --_x---* collections land at natural paths (color.primary.gloss.black,
# size.64px…); the flat --bg-* names under bg.*; the [data-theme="dark"]
# declarations are evidence under their own selectors in raw/css-vars.json,
# not painted themes.

mkt_names = sorted(n for n in HOST_NAMES["marketing"] if declared(n, "light") is not None)
app_names = sorted(n for n in HOST_NAMES["app"] if declared(n, "app") is not None)
bk_names = sorted(n for n in HOST_NAMES["booking"] if declared(n, "booking") is not None)


def emit_named(setroot, name, val):
    """Emit a declared name at its natural path in the set."""
    emit(setroot, name, var(name, leaf_type(name, val)))


for name in mkt_names:
    emit_named(SPEC["core"], name, R.get(name))

# The alias maps are collected in a second pass: emit() can rename a leaf to
# `name.default` when a later variable needs its path as a group, and
# EMITTED is only final once the whole set is written.
color_alias = {}   # normalized colour -> token path for light-set aliasing
for name in sorted(mkt_names, key=lambda n: n.startswith("--_")):
    color_alias.setdefault(norm_color(R.get(name)), EMITTED[name])

for name in app_names:
    emit_named(SPEC["app"], name, A.get(name))

app_alias = {}
for name in app_names:
    app_alias.setdefault(norm_color(A.get(name)), EMITTED[name])

for name in bk_names:
    emit_named(SPEC["booking"], name, B.get(name))

bk_alias = {}
for name in bk_names:
    bk_alias.setdefault(norm_color(B.get(name)), EMITTED[name])

# Measured roles alias to the declared token the value matches — inside the
# set the role lives in. Only the set's own declarations are safe targets.
role_alias = {
    "light": dict(color_alias),
    "app": app_alias,
    "booking": bk_alias,
}


def semcolor(raw, src, desc, theme="light"):
    alias = role_alias[theme].get(norm_color(raw))
    value = f"{{{alias}}}" if alias else norm_color(raw)
    return lit(value, "color", src + (f"; matches declared {alias}" if alias else ""), desc)


sem, asem, bsem = SPEC["light"], SPEC["app"], SPEC["booking"]
for root, theme, key, comp, state, prop, group, desc in [
    (sem, "light", "ink", "feat-h1", "default", "color", "text",
     "The near-black display and body ink (the declared --_color---primary--gloss-black #17150e family); the photo-hero masthead inverts to gloss-white."),
    (sem, "light", "muted", "ptoggle", "default", "color", "text",
     "The muted ink the billing-toggle's unselected labels paint — a mid gray off the gloss ramp."),
    (sem, "light", "cta-fill", "plan-cta", "default", "backgroundColor", "action",
     "The black pill fill the plan 'Get started' and form 'Submit' buttons paint."),
    (sem, "light", "cta-ink", "plan-cta", "default", "color", "action",
     "The gloss-white text on the black pills."),
    (sem, "light", "nav-fill", "nav-demo", "default", "backgroundColor", "action",
     "The header 'Book a demo' outline pill — a transparent fill over the photo hero."),
    (sem, "light", "nav-ink", "nav-demo", "default", "color", "action",
     "The white text on the header outline pill over the photo hero."),
    (sem, "light", "hero-fill", "hero-cta", "default", "backgroundColor", "action",
     "The hero's white 'Start free trial' pill fill over the photograph."),
    (sem, "light", "hero-ink", "hero-cta", "default", "color", "action",
     "The near-black ink inside the hero's white pill."),
    (sem, "light", "card", "plan-card-popular", "default", "backgroundColor", "surface",
     "The white .card_new plan-card surface, read on the 'Most popular' column."),
    (sem, "light", "card-popular", "plan-card-popular", "default", "backgroundColor", "surface",
     "The 'Most popular' Gold card surface — the same white card carrying the amber tag."),
    (sem, "light", "field", "demo-field", "default", "backgroundColor", "surface",
     "The demo-form field surface — a white tile."),
    (sem, "light", "field-border", "demo-field", "default", "borderTopColor", "border",
     "The demo-form field border — the fields are borderless white tiles; the border reads transparent."),
    (sem, "light", "focus-ring", "nav-link", "focus-visible", "outlineColor", "border",
     "The keyboard focus outline on controls — a 1px near-black auto outline."),
    (sem, "light", "accordion", "faq-item", "default", "backgroundColor", "surface",
     "The FAQ accordion row surface — transparent rows parted by a gray hairline."),
    (asem, "app", "ink", "login-h1", "default", "color", "text",
     "The app's heading ink (the declared --content-primary)."),
    (asem, "app", "muted", "login-card", "default", "color", "text",
     "The muted hint ink inside the auth card (a mid glossDS gray)."),
    (asem, "app", "link", "login-forgot", "default", "color", "text",
     "The 'Forgot Password?' link ink."),
    (asem, "app", "field-bg", "login-field", "default", "backgroundColor", "surface",
     "The auth-field fill — the glossDS inputs paint transparent on the page field."),
    (asem, "app", "field-border", "login-field", "default", "borderTopColor", "border",
     "The auth field's declared border colour — the boxes paint 0 border width, so the ink is the declaration, not a drawn edge."),
    (asem, "app", "primary-fill", "login-submit", "default", "backgroundColor", "action",
     "The 'Log in' submit fill at rest — measured, never submitted."),
    (asem, "app", "primary-ink", "login-submit", "default", "color", "action",
     "The text on the app primary button."),
    (asem, "app", "card", "login-card", "default", "backgroundColor", "surface",
     "The auth 'card' surface — the form paints no card chrome; the fields sit on the page field."),
    (bsem, "booking", "ink", "bk-title", "default", "color", "text",
     "The booking site's heading ink — this business's site paints a dark field with white type."),
    (bsem, "booking", "muted", "bk-badge", "default", "color", "text",
     "The 'powered by GlossGenius' badge gray — the muted ink on the dark field."),
    (bsem, "booking", "card", "bk-service-card", "default", "backgroundColor", "surface",
     "The service-card surface — the rows paint no card fill over the dark field."),
    (bsem, "booking", "select-fill", "bk-service-select", "default", "backgroundColor", "action",
     "A service row's 'Select' button fill — transparent inside its white outline."),
    (bsem, "booking", "select-ink", "bk-service-select", "default", "color", "action",
     "The white 'Select' button ink on the dark field."),
    (bsem, "booking", "book-fill", "bk-book-btn", "default", "backgroundColor", "action",
     "The 'BOOK n SERVICE' bar's painted fill — transparent over the dark header."),
    (bsem, "booking", "book-ink", "bk-book-btn", "default", "color", "action",
     "The white 'BOOK n SERVICE' bar ink."),
]:
    try:
        if prop == "color":
            raw = ts(comp, state, "color")
            src = f"computed color of {comp} {state} — the first text node's reading where the kit recorded one (raw/components-computed.json)"
        elif prop == "innerFill":
            raw = inner_fill(comp, state)
            src = f"the first opaque painted layer inside {comp} {state} (raw/components-computed.json paint list)"
        else:
            raw = st(comp, state)[prop]
            src = f"computed {prop} of {comp} {state} (raw/components-computed.json)"
        if raw in (None, ""):
            raise KeyError(prop)
        root.setdefault(group, {})[key] = semcolor(raw, src, desc, theme)
    except KeyError:
        pass

# The page fields: the marketing body field, the app's field behind the
# auth card, the booking site's field.
for root, theme, comp, desc in [
    (sem, "light", "mkt-header", "The page field behind the marketing pages (the html/body field under every white card)."),
    (asem, "app", "login-footer", "The page field behind the signed-out auth surfaces."),
    (bsem, "booking", "bk-nav", "The page field behind the published booking site."),
]:
    pass  # filled by measured roles above when the fields themselves paint a colour

# ------------------------------------------------------------------ shape
#
# The app declares --radius-* and --button-*-radius; the marketing radius
# scale is measured on real controls and cards.

radii = SPEC["core"].setdefault("radius", {})
for key, comp, state, prop, desc in [
    ("control", "nav-link", "default", "borderTopLeftRadius", "The radius on nav links and menu rows."),
    ("button", "nav-demo", "default", "borderTopLeftRadius", "The radius on the header pill buttons."),
    ("field", "demo-field", "default", "borderTopLeftRadius", "The radius on the demo-form fields."),
    ("app-field", "login-field", "default", "borderTopLeftRadius", "The radius on the app auth fields and submit."),
    ("card", "plan-card", "default", "borderTopLeftRadius", "The pricing-card radius."),
    ("pill", "hero-cta", "default", "borderTopLeftRadius", "The pill radius on the big CTAs."),
    ("service-card", "bk-service-card", "default", "borderTopLeftRadius", "The booking service-card radius."),
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
for comp in ("nav-link", "nav-demo", "login-forgot", "bk-service-card"):
    try:
        s = st(comp, "default")
        dur, ease = s.get("transitionDuration"), s.get("transitionTimingFunction")
        if dur and dur != "0s":
            props = [p.strip() for p in s.get("transitionProperty", "all").split(",") if p.strip()]
            durs = [p.strip() for p in dur.split(",")]
            val = ", ".join(f"{p} {durs[i % len(durs)]} {ease or ''}".strip() for i, p in enumerate(props))
            mo["control"] = lit(val, "other",
                f"computed transition of {comp} default (raw/components-computed.json)",
                "The control transition the site puts on nav links, buttons and cards.")
            break
    except KeyError:
        continue

# ------------------------------------------------------------- components
#
# Theme-independent measured geometry.

comp_t = SPEC["component"]
for name, cname, state, prop, ty_, desc in [
    ("topbar-height", "mkt-header", "default", "h", "dimension", "The marketing header bar height."),
    ("nav-link-height", "nav-link", "default", "h", "dimension", "The nav-link hit height."),
    ("nav-pill-height", "nav-demo", "default", "h", "dimension", "The header 'Book a demo' pill height."),
    ("hero-cta-height", "hero-cta", "default", "h", "dimension", "The hero pill height."),
    ("hero-cta-width", "hero-cta", "default", "w", "dimension", "The hero pill width."),
    ("hero-width", "hero-h1", "default", "w", "dimension", "The hero masthead measure."),
    ("plan-card-width", "plan-card", "default", "w", "dimension", "The pricing-card width."),
    ("plan-card-height", "plan-card", "default", "h", "dimension", "The pricing-card height."),
    ("plan-cta-height", "plan-cta", "default", "h", "dimension", "The plan-CTA height."),
    ("faq-row-height", "faq-item", "default", "h", "dimension", "The closed FAQ row height."),
    ("demo-field-width", "demo-field", "default", "w", "dimension", "The demo-form field width."),
    ("mobile-topbar-height", "m-topbar", "default", "h", "dimension", "The phone header height."),
    ("mobile-cta-height", "m-hero-cta", "default", "h", "dimension", "The hero pill at 390 wide."),
]:
    try:
        v = rc(cname, state, prop)
        comp_t[name] = lit(("%g" % v) + "px" if isinstance(v, (int, float)) else str(v) + "px",
                          ty_, f"measured {prop} of {cname} {state} (raw/components-computed.json)", desc)
    except KeyError:
        pass

# The signed-out app forms and the booking site: measured literals on their
# own surfaces.
appf = comp_t.setdefault("app", {})
for name, cname, state, prop, ty_, desc in [
    ("card-width", "login-card", "default", "w", "dimension", "The auth card width."),
    ("card-height", "login-card", "default", "h", "dimension", "The auth card height."),
    ("field-height", "login-field", "default", "h", "dimension", "The auth field height."),
    ("field-width", "login-field", "default", "w", "dimension", "The auth field width."),
    ("submit-height", "login-submit", "default", "h", "dimension", "The primary submit height."),
]:
    try:
        if prop in ("w", "h"):
            v = rc(cname, state, prop)
            appf[name] = lit(("%g" % v) + "px", ty_, f"measured {prop} of {cname} {state} on app.glossgenius.com (raw/components-computed.json)", desc)
        else:
            v = st(cname, state)[prop]
            appf[name] = lit(v, ty_, f"computed {prop} of {cname} {state} on app.glossgenius.com (raw/components-computed.json)", desc)
    except KeyError:
        pass

bkf = comp_t.setdefault("booking", {})
for name, cname, state, prop, ty_, desc in [
    ("nav-height", "bk-nav", "default", "h", "dimension", "The booking-site nav bar height."),
    ("select-height", "bk-pro-select", "default", "h", "dimension", "The 'Select a Professional' control height."),
    ("select-width", "bk-pro-select", "default", "w", "dimension", "The 'Select a Professional' control width."),
    ("service-card-height", "bk-service-card", "default", "h", "dimension", "A service card's height."),
    ("service-card-width", "bk-service-card", "default", "w", "dimension", "A service card's width."),
    ("book-bar-height", "bk-book-btn", "default", "h", "dimension", "The 'BOOK n SERVICE' button height."),
    ("calendar-width", "bk-cal", "default", "w", "dimension", "The date-picker calendar width."),
    ("day-cell", "bk-day", "default", "h", "dimension", "A calendar day cell's size."),
]:
    try:
        v = rc(cname, state, prop)
        bkf[name] = lit(("%g" % v) + "px", ty_, f"measured {prop} of {cname} {state} on the published booking site (raw/components-computed.json)", desc)
    except KeyError:
        pass

(RAW / "component-tokens.json").write_text(json.dumps(SPEC, indent=2, ensure_ascii=False) + "\n")
print("component-tokens.json:", {k: len(v) for k, v in SPEC.items() if k != "_about"})
