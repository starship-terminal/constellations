#!/usr/bin/env python3
"""Write raw/component-tokens.json, the token spec build_tokens.py reads.

Glorify ships two public surfaces signed out, each with its own declared
vocabulary on :root:

  glorify.com         the Framer marketing site — light only. The declared
                      layer is the hashed Framer token set (--token-<uuid>…)
                      on :root, resolved per name by vars.mjs. The
                      --framer-* typography/layout engine variables are the
                      framework's own and stay in the vendor bin — they are
                      declared evidence in raw/css-vars.json, not tokens.

  app.glorify.com     the product SPA — dark chrome. Its own semantic
                      vocabulary on :root: the --light-*/--dark-* ramps,
                      --neutral-light-*, --active-*/--hover-* state colours,
                      --icon-*/--disabled-*/--field-* roles, the
                      --error-*/--info-*/--green-*/--orange-*/--pink-*
                      ramps, --cta-300, --glori-gradient and the --header/
                      --hero/--inspector/--assets layout names.
                      /dashboard/login and /dashboard/register paint it, and
                      the anonymous editor at /designer/use-template/0 (the
                      upload onboarding, the Craft dialog and the canvas
                      chrome) resolves the identical set.

The palette names are emitted at their natural paths in the set whose host
declares them: core holds the marketing vocabulary (the hashed --token-*
names land under token.<uuid parts>), app holds the SPA vocabulary.
Measured computed styles from raw/components-computed.json fill the
semantic roles and alias back to the declared values they match:

  core      the declared marketing vocabulary + the measured type ramp,
            radius scale and control transition
  light     measured semantic roles on the marketing surface (ink, CTA fill
            and ring, card surfaces) aliased to the token-* values they
            match
  app       the SPA vocabulary at its own resolutions + the measured
            auth-card, onboarding and editor-chrome roles (field fill, the
            disabled and enabled submit fills, the inspector surfaces)
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
C = json.loads((RAW / "components-computed.json").read_text())["components"]

# Which host's sheets declare each theme-bin name — the file label vars.mjs
# stamps on every rule starts with the host word. The anonymous editor's
# sheets re-declare the app's :root verbatim, so "editor" folds into "app".
HOST_NAMES = {"marketing": set(), "app": set()}
for binname in ("theme", "app"):
    for rule in V.get(binname, []):
        host = (rule.get("file") or "").split(" ", 1)[0]
        if host in ("app", "editor"):
            HOST_NAMES["app"].update(rule.get("properties") or {})
        elif host in HOST_NAMES:
            HOST_NAMES[host].update(rule.get("properties") or {})

SPEC = {"_about": (
    "The token tree build_tokens.py turns into tokens.json. Glorify's two "
    "public surfaces declare separate vocabularies on :root "
    "(raw/css-vars.json): core.* carries the marketing site's hashed Framer "
    "--token-* declarations, app.* carries the SPA's own semantic vocabulary "
    "(--light-*/--dark-*/--neutral-light-*/--active-*/--field-*/the accent "
    "ramps/--glori-gradient) that the signed-out auth cards and the "
    "anonymous editor paint. Measured roles alias to the declared values "
    "they match, inside their own surface set."),
    "core": {}, "light": {}, "app": {}, "component": {}}


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
    v = str(v or "").strip()
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
    m = re.fullmatch(r"(\d{1,3}),\s*(\d{1,3}),\s*(\d{1,3})", v)
    if m:  # Tailwind channel triplets: --theme-*: "99, 200, 217"
        return "#%02x%02x%02x" % tuple(int(x) for x in m.groups())
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

    Glorify's marketing names are hashed Framer tokens
    (--token-f8b21c3f-9c41-…): parts are sanitized (empty segments dropped,
    leading underscores stripped) so the path is token.f8b21c3f.9c41.…; the
    app's semantic names land at natural paths (active.primary,
    neutral.light.100…). A declared name can be both a leaf and the parent
    of other names; when a leaf and a group must share a node, the leaf
    moves inside the group under the first free of `default`, `base`,
    `self` — never silently overwriting tokens that resolve to different
    states.
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
    pool = {"light": R, "app": A}[theme]
    v = pool.get(name)
    return v if v not in (None, "") else None


def norm_len(v):
    m = re.fullmatch(r"(-?[\d.]+[eE][+-]?\d+)(px|rem)", str(v).strip())
    if not m:
        return v
    return f"{float(m.group(1)):f}".rstrip("0").rstrip(".") + m.group(2)


COLOR_V = re.compile(r"(#[0-9a-fA-F]{3,8}|rgba?\([^)]*\)|hsla?\([^)]*\)|(ok)?lab\([^)]*\)|(ok)?lch\([^)]*\)|color-mix\([^)]*\)|\d{1,3},\s*\d{1,3},\s*\d{1,3})")


def leaf_type(name, val):
    """The DTCG type a declared value honestly is."""
    v = str(val or "").strip()
    if COLOR_V.fullmatch(v):
        return "color"
    if re.fullmatch(r"-?\d+(\.\d+)?(px|rem)", v):
        return "dimension"
    if re.fullmatch(r"[\d.]+m?s", v):
        return "duration"
    if re.fullmatch(r"cubic-bezier\([^)]*\)", v) or v in ("ease", "ease-in", "ease-out", "ease-in-out", "linear"):
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


def paint_match(comp, state, node_re, key="bg"):
    """The painted `key` of the layer whose node name matches `node_re` — for
    surfaces an ancestor paints (the .field-container fill under the
    transparent auth inputs)."""
    rx = re.compile(node_re)
    c = C[comp]["states"][state]
    for p in c.get("paint") or []:
        if p.get(key) and rx.search(p.get("node") or ""):
            return p[key]
    raise KeyError("paintMatch")


def paint_border(comp, state):
    """The colour of the first painted border inside the component — for the
    hero CTA, whose ::after layer carries the 1px white stroke on the dark
    band (the anchor's own border is the unstyled link default)."""
    c = C[comp]["states"][state]
    for p in c.get("paint") or []:
        b = p.get("border") or ""
        m = re.search(r"(#[0-9a-fA-F]{3,8}|rgba?\([^)]*\))", b)
        if m:
            return m.group(1)
    raise KeyError("paintBorder")


def inner_fill(comp, state):
    """The first opaque painted layer inside the component — the fill the
    eye actually sees when the element's own box only paints a translucent
    wrapper (a pill halo or a card chrome over a solid inner node)."""
    c = C[comp]["states"][state]
    for p in c.get("paint") or []:
        bg = p.get("bg") or ""
        m = re.fullmatch(r"rgba?\(([\d.]+),\s*([\d.]+),\s*([\d.]+)(?:,\s*([\d.]+))?\)", bg)
        if m and (m.group(4) is None or float(m.group(4)) >= 1):
            return bg
    raise KeyError("innerFill")


# ------------------------------------------------------------------- fonts
#
# The marketing sheet is a Framer bundle: font faces arrive through the
# bundle's @font-face rules (kept in raw/css-vars.json fonts) and the
# family lands in computed styles. The app loads its own faces. No
# marketing size variable exists — the ramp is measured px on real
# components, honestly labelled.

fam = SPEC["core"].setdefault("font", {}).setdefault("family", {})
for comp, state, key, desc in [
    ("hero-h1", "default", "display", "The display family the marketing headings set, measured on the hero masthead."),
    ("plan-row", "default", "body", "The body family the marketing prose and nav set, measured on a pricing row."),
    ("feat-prose", "default", "body", "The body family the marketing prose sets, measured on a feature paragraph."),
]:
    if key in fam:
        continue
    try:
        v = st(comp, state)["fontFamily"]
    except KeyError:
        continue
    fam[key] = lit(v, "fontFamily",
        f"computed fontFamily of {comp} {state} (raw/components-computed.json); the host's @font-face faces in raw/css-vars.json",
        desc)

weights = SPEC["core"].setdefault("font", {}).setdefault("weight", {})
# Each weight token is named for the weight it measures (400 regular, 500 medium, ...), never for the
# weight a component was expected to have: a semibold key holding 500 sends a consumer the wrong face.
WEIGHT_NAMES = {100: "thin", 200: "extralight", 300: "light", 400: "regular", 500: "medium",
                600: "semibold", 700: "bold", 800: "extrabold", 900: "black"}
seen_weights = {}
for comp, state, role in [
    ("plan-row", "default", "pricing plan rows"),
    ("nav-link", "default", "header nav links"),
    ("nav-cta", "default", "the header call to action"),
    ("hero-h1", "default", "the hero heading"),
]:
    try:
        w = ts(comp, state, "fontWeight") or st(comp, state)["fontWeight"]
    except KeyError:
        continue
    if not w:
        continue
    w = int(float(w))
    seen_weights.setdefault(w, []).append((comp, state, role))
for w, reads in sorted(seen_weights.items()):
    key = WEIGHT_NAMES.get(w, "w%d" % w)
    weights[key] = lit(w, "fontWeight",
        "computed fontWeight of %s (raw/components-computed.json)" % ", ".join(f"{c} {s}" for c, s, _ in reads),
        "The %d weight, measured on %s." % (w, "; ".join(r for _, _, r in reads)))

# Measured marketing type ramp — the marketing sheets carry no readable size
# variables (the --framer-* text engine stays vendor), so the ramp is
# computed px on real components, honestly labelled.
sizes = SPEC["core"].setdefault("font", {}).setdefault("size", {})
for key, comp, state, desc in [
    ("display", "feat-h1", "default", "The feature-page display heading."),
    ("hero", "hero-h1", "default", "The hero masthead."),
    ("h2", "home-h2", "default", "A home section heading."),
    ("button", "nav-cta", "default", "The header button size."),
    ("planName", "plan-price", "default", "The plan price figure."),
    ("body", "plan-row", "default", "The body/prose size."),
    ("eyebrow", "learn-tag", "default", "The article-tag and small-label size."),
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
    ("eyebrow", "learn-tag", "default", "The small-label leading."),
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
# The marketing :root vocabulary — the canonical declaration. The hashed
# --token-* names land under token.*; the app's own vocabulary lands in the
# app set.

mkt_names = sorted(n for n in HOST_NAMES["marketing"] if declared(n, "light") is not None)
app_names = sorted(n for n in HOST_NAMES["app"] if declared(n, "app") is not None)


def emit_named(setroot, name, val):
    """Emit a declared name at its natural path in the set."""
    emit(setroot, name, var(name, leaf_type(name, val)))


for name in mkt_names:
    emit_named(SPEC["core"], name, R.get(name))

# The alias maps are collected in a second pass: emit() can rename a leaf to
# `name.default` when a later variable needs its path as a group, and
# EMITTED is only final once the whole set is written.
color_alias = {}   # normalized colour -> token path for light-set aliasing
# The hashed --token-* layer is the marketing design system; third-party
# widget vars that happen to declare the same colour (chat, captcha…) must
# not win the alias — token names are preferred, then everything else.
for name in sorted(mkt_names, key=lambda n: (0 if n.startswith("--token") else 1, n)):
    color_alias.setdefault(norm_color(R.get(name)), EMITTED[name])

for name in app_names:
    emit_named(SPEC["app"], name, A.get(name))

app_alias = {}
for name in app_names:
    app_alias.setdefault(norm_color(A.get(name)), EMITTED[name])

# Measured roles alias to the declared token the value matches — inside the
# set the role lives in. Only the set's own declarations are safe targets.
role_alias = {
    "light": dict(color_alias),
    "app": app_alias,
}


def semcolor(raw, src, desc, theme="light"):
    alias = role_alias[theme].get(norm_color(raw))
    value = f"{{{alias}}}" if alias else norm_color(raw)
    return lit(value, "color", src + (f"; matches declared {alias}" if alias else ""), desc)


sem, asem = SPEC["light"], SPEC["app"]
for root, theme, key, comp, state, prop, group, desc in [
    (sem, "light", "ink", "feat-h1", "default", "color", "text",
     "The marketing heading ink on the white field — the feature-page h1 (the hero h1 is white on the dark hero band instead)."),
    (sem, "light", "body", "feat-prose", "default", "color", "text",
     "The marketing body-copy ink."),
    (sem, "light", "muted", "hero-sub", "default", "color", "text",
     "The hero subline's ink — the quieter marketing text role."),
    (sem, "light", "link", "footer-link", "default", "color", "text",
     "A footer link's ink — a muted gray on the dark footer band."),
    (sem, "light", "cta-fill", "nav-play", "default", "backgroundColor", "action",
     "The header 'Play for free' button's fill — the same blue the 'Get Started Now' CTA paints inside its Button Wrap on /pricing."),
    (sem, "light", "cta-ink", "nav-play", "default", "color", "action",
     "The text on the header CTA button."),
    (sem, "light", "hero-cta-fill", "hero-cta", "default", "backgroundColor", "action",
     "The hero 'Play for free' action's fill — honestly transparent: it is an outlined ghost on the dark hero band (unlike the filled nav and feature CTAs)."),
    (sem, "light", "hero-cta-ink", "hero-cta", "default", "color", "action",
     "The white text on the hero action."),
    (sem, "light", "hero-cta-border", "hero-cta", "default", "paintBorder", "action",
     "The 1px white stroke the hero ghost CTA's ::after paints on the dark band."),
    (sem, "light", "card", "plan-card", "default", "backgroundColor", "surface",
     "The pricing-card surface."),
    (sem, "light", "focus-ring", "nav-cta", "focus-visible", "outlineColor", "border",
     "The keyboard focus ring on controls, where the browser paints one."),
    (asem, "app", "ink", "login-title", "default", "color", "text",
     "The app heading ink on the dark chrome."),
    (asem, "app", "body", "ob-title", "default", "color", "text",
     "The onboarding headline ink — the 'Create designs' headline sits on the white upload card inside the dark editor field."),
    (asem, "app", "muted", "login-field", "default", "color", "text",
     "The auth field's typed-text ink."),
    (asem, "app", "link", "login-forgot", "default", "color", "text",
     "The 'Forgot password?' link ink."),
    (asem, "app", "card", "login-card", "default", "innerFill", "surface",
     "The auth card's painted surface on the dark field — the card's own box is transparent, the fill is its inner panel."),
    (asem, "app", "field-bg", "login-card", "default", "paintMatch:field-container", "surface",
     "The auth-field fill — the .field-container paint under the transparent inputs."),
    (asem, "app", "field-border", "login-field", "default", "borderTopColor", "border",
     "The auth-field border, where the field paints one."),
    (asem, "app", "field-focus", "login-field", "focused", "borderTopColor", "border",
     "The auth-field border or ring while focused."),
    (asem, "app", "oauth-fill", "login-google", "default", "backgroundColor", "action",
     "The Google OAuth button's fill — honestly transparent: it is an outlined ghost button with a blue border on the dark card."),
    (asem, "app", "oauth-ink", "login-google", "default", "color", "action",
     "The text on the OAuth button."),
    (asem, "app", "primary-fill", "login-submit", "enabled", "backgroundColor", "action",
     "The enabled submit fill, painted once sample text sits in both fields — never submitted."),
    (asem, "app", "primary-fill-disabled", "login-submit", "default", "backgroundColor", "action",
     "The submit's disabled fill at rest."),
    (asem, "app", "primary-ink", "login-submit", "enabled", "color", "action",
     "The text on the app primary button."),
    (asem, "app", "chrome-fill", "ed-header", "default", "innerFill", "surface",
     "The editor header bar's fill on the dark chrome — the header's own box is transparent, the fill is its inner panel."),
    (asem, "app", "inspector-fill", "ed-inspector", "default", "innerFill", "surface",
     "The inspector panel's fill."),
    (asem, "app", "tool-fill-active", "ed-tool-active", "default", "backgroundColor", "action",
     "The selected tool's highlighted fill on the left rail."),
    (asem, "app", "signup-fill", "ed-signup", "default", "backgroundColor", "action",
     "The filled Signup button's paint in the editor header."),
    (asem, "app", "signup-ink", "ed-signup", "default", "color", "action",
     "The text on the filled Signup button."),
    (asem, "app", "dialog-fill", "ed-craft", "default", "innerFill", "surface",
     "The Craft dialog's painted surface — the modal box's own box is transparent, the fill is its inner panel."),
    (asem, "app", "craft-cta-fill", "ed-add", "enabled", "backgroundColor", "action",
     "The 'Add to canvas' fill once a style is picked — measured at rest; the screenshot pass pressed it once (an AI generation), measure.mjs never did."),
    (asem, "app", "craft-cta-disabled", "ed-add", "default", "backgroundColor", "action",
     "The 'Add to canvas' fill before a style is picked — measured identical to the enabled fill, the button does not dim."),
    (asem, "app", "style-selected-border", "ed-craft-style", "opened", "borderTopColor", "border",
     "The border the picked Craft style card paints."),
]:
    try:
        if prop == "color":
            raw = ts(comp, state, "color")
            src = f"computed color of {comp} {state} — the first text node's reading where the kit recorded one (raw/components-computed.json)"
        elif prop == "innerFill":
            raw = inner_fill(comp, state)
            src = f"the first opaque painted layer inside {comp} {state} (raw/components-computed.json paint list)"
        elif prop.startswith("paintMatch:"):
            raw = paint_match(comp, state, prop.split(":", 1)[1])
            src = f"the painted fill of the {prop.split(':', 1)[1]} layer inside {comp} {state} (raw/components-computed.json paint list)"
        elif prop == "paintBorder":
            raw = paint_border(comp, state)
            src = f"the colour of the first painted border inside {comp} {state} (raw/components-computed.json paint list)"
        else:
            raw = st(comp, state)[prop]
            src = f"computed {prop} of {comp} {state} (raw/components-computed.json)"
        if raw in (None, ""):
            raise KeyError(prop)
        root.setdefault(group, {})[key] = semcolor(raw, src, desc, theme)
    except KeyError:
        pass

# The page field: the marketing body and the app body measured directly.
try:
    sem.setdefault("background", {})["page"] = semcolor(
        st("page-bg", "default")["backgroundColor"],
        "computed backgroundColor of the marketing body (raw/components-computed.json page-bg default); the painted field behind every marketing page (screenshots/*-light-*.png)",
        "The marketing page field.")
except KeyError:
    pass
try:
    asem.setdefault("background", {})["page"] = semcolor(
        st("app-bg", "default")["backgroundColor"],
        "computed backgroundColor of the app body (raw/components-computed.json app-bg default); the dark field behind the auth cards and editor chrome (screenshots/*-app-*.png)",
        "The app page field — the dark chrome.")
except KeyError:
    pass

# ------------------------------------------------------------------ shape
#
# No readable radius variable survives in the marketing sheet (the hashed
# tokens declare colours; the --framer-* engine is vendor), so the scale is
# measured on real controls and cards.

radii = SPEC["core"].setdefault("radius", {})
for key, comp, state, prop, desc in [
    ("control", "nav-link", "default", "borderTopLeftRadius", "The radius on nav links and small controls."),
    ("button", "nav-play", "default", "borderTopLeftRadius", "The radius on the header 'Play for free' button — an 8px rounded rectangle, not a pill."),
    ("field", "login-field", "default", "borderTopLeftRadius", "The radius on the app auth fields and submit."),
    ("app-button", "login-submit", "default", "borderTopLeftRadius", "The radius on the app primary submit."),
    ("card", "plan-card", "default", "borderTopLeftRadius", "The pricing-card radius."),
    ("dialog", "ed-craft", "default", "borderTopLeftRadius", "The Craft dialog's radius."),
    ("cta", "hero-cta", "default", "borderTopLeftRadius", "The hero CTA's radius — an 8px rounded rectangle."),
    ("inspector", "ed-inspector", "default", "borderTopLeftRadius", "The inspector panel's radius."),
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
for comp in ("nav-link", "nav-cta", "hero-cta", "plan-card", "login-forgot", "ed-tool"):
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
    ("nav-cta-height", "nav-cta", "default", "h", "dimension", "The header button height."),
    ("hero-cta-height", "hero-cta", "default", "h", "dimension", "The hero action height."),
    ("hero-cta-width", "hero-cta", "default", "w", "dimension", "The hero action width."),
    ("hero-width", "hero-h1", "default", "w", "dimension", "The hero masthead measure."),
    ("billing-tab-height", "bill-yearly", "default", "h", "dimension", "The billing-tab height."),
    ("plan-card-width", "plan-card", "default", "w", "dimension", "The pricing-card width."),
    ("plan-card-height", "plan-card", "default", "h", "dimension", "The pricing-card height."),
    ("plan-cta-height", "plan-cta", "default", "h", "dimension", "The plan-CTA height."),
    ("tpl-card-width", "tpl-card", "default", "w", "dimension", "The template card width."),
    ("tpl-card-height", "tpl-card", "default", "h", "dimension", "The template card height."),
    ("learn-card-width", "learn-card", "default", "w", "dimension", "The Learn article card width."),
    ("mobile-topbar-height", "m-topbar", "default", "h", "dimension", "The phone header height."),
    ("mobile-cta-height", "m-hero-cta", "default", "h", "dimension", "The hero action at 390 wide."),
]:
    try:
        v = rc(cname, state, prop)
        comp_t[name] = lit(("%g" % v) + "px" if isinstance(v, (int, float)) else str(v) + "px",
                          ty_, f"measured {prop} of {cname} {state} (raw/components-computed.json)", desc)
    except KeyError:
        pass

# The signed-out app surfaces and the anonymous editor: measured literals on
# their own surface.
appf = comp_t.setdefault("app", {})
for name, cname, state, prop, ty_, desc in [
    ("card-width", "login-card", "default", "w", "dimension", "The auth card width."),
    ("card-height", "login-card", "default", "h", "dimension", "The auth card height."),
    ("field-height", "login-field", "default", "h", "dimension", "The auth field height."),
    ("field-width", "login-field", "default", "w", "dimension", "The auth field width."),
    ("submit-height", "login-submit", "default", "h", "dimension", "The primary submit height."),
    ("header-height", "ed-header", "default", "h", "dimension", "The editor header height."),
    ("tool-btn", "ed-tool", "default", "h", "dimension", "The tool-rail icon-button size."),
    ("inspector-width", "ed-inspector", "default", "w", "dimension", "The inspector panel width."),
    ("inspector-height", "ed-inspector", "default", "h", "dimension", "The inspector panel height."),
    ("zoom-height", "ed-zoom", "default", "h", "dimension", "The zoom control height."),
    ("craft-cta-height", "ed-add", "default", "h", "dimension", "The 'Add to canvas' button height."),
]:
    try:
        if prop in ("w", "h"):
            v = rc(cname, state, prop)
            appf[name] = lit(("%g" % v) + "px", ty_, f"measured {prop} of {cname} {state} on app.glorify.com (raw/components-computed.json)", desc)
        else:
            v = st(cname, state)[prop]
            appf[name] = lit(v, ty_, f"computed {prop} of {cname} {state} on app.glorify.com (raw/components-computed.json)", desc)
    except KeyError:
        pass

(RAW / "component-tokens.json").write_text(json.dumps(SPEC, indent=2, ensure_ascii=False) + "\n")
print("component-tokens.json:", {k: len(v) for k, v in SPEC.items() if k != "_about"})
