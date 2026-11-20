#!/usr/bin/env python3
"""Write raw/component-tokens.json, the token spec build_tokens.py reads.

FlowMapp ships two public surfaces signed out, each with its own declared
vocabulary on :root:

  www.flowmapp.com    the Webflow marketing site — light only. Two declared
                      layers in one bundled sheet + inline blocks: a legacy
                      flat palette (--bg/--black/--white/--dodger-blue/
                      --primary-blue/--basic-blue/--alice-blue/--gainsboro/
                      --light-steel-blue/--dark-grey/--service-grey/
                      --yellow-green/--pale-violet-red) and the Webflow
                      "_apps" variable collections (--_apps---typography--*,
                      --_apps---sizes--*, --_apps---colors--*, --_apps---
                      charts--*, --_apps---sidebar--*). The _apps colours
                      declare -dark twins, but nothing signed out switches to
                      them — declared evidence, never a painted surface.

  app.flowmapp.com    the React/Ant Design SPA under CSS modules — its own
                      ramp: --primary-basic-*/--primary-red-500, the
                      --secondary-<hue> family with 8/20/32/56/64 alpha
                      steps, the --neutral-gray-* greys and --transparent.
                      /signin, /signup and /restore paint it, and the
                      published read-only demo project at
                      /share/projects/215285 (sitemap + user-flow viewers)
                      resolves the identical set.

The palette names are emitted at their natural paths in the set whose host
declares them: core holds the marketing vocabulary (the canonical set —
shared names like --white have no other resolution to fight), app holds the
SPA ramp. Measured computed styles from raw/components-computed.json fill
the semantic roles and alias back to the declared values they match:

  core      the declared marketing vocabulary, Inter + the measured type
            ramp, radius scale and control transition
  light     measured semantic roles on the marketing surface (ink, CTA fill
            and ring, card surfaces) aliased to the palette values they match
  app       the SPA vocabulary at its own resolutions + the measured
            auth-form and share-viewer roles (field fill, the disabled and
            enabled submit fills)
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
# stamps on every rule starts with the host word. The share viewer's sheets
# re-declare the app's set verbatim (share-only resolved names: none), so
# "share" folds into "app".
HOST_NAMES = {"marketing": set(), "app": set()}
for binname in ("theme", "app"):
    for rule in V.get(binname, []):
        host = (rule.get("file") or "").split(" ", 1)[0]
        if host in ("app", "share"):
            HOST_NAMES["app"].update(rule.get("properties") or {})
        elif host in HOST_NAMES:
            HOST_NAMES[host].update(rule.get("properties") or {})

SPEC = {"_about": (
    "The token tree build_tokens.py turns into tokens.json. FlowMapp's two "
    "public surfaces declare separate vocabularies on :root "
    "(raw/css-vars.json): core.* carries the marketing site's flat legacy "
    "palette plus the Webflow _apps variable layer (including the declared "
    "but never-painted -dark twins), app.* carries the SPA's "
    "--primary-*/--secondary-*/--neutral-gray-* ramp that the signed-out "
    "auth forms and the public share viewer paint. Measured roles alias to "
    "the declared values they match, inside their own surface set."),
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

    FlowMapp's Webflow layer names read --_apps---colors--primary: parts are
    sanitized (empty segments dropped, leading underscores stripped) so the
    path is apps.colors.primary. A declared name can be both a leaf and the
    parent of other names; when a leaf and a group must share a node, the
    leaf moves inside the group under the first free of `default`, `base`,
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
    ring (the hero/plan CTAs' dodger-blue-20 halo over a solid dodger-blue
    .btn__wrapper)."""
    c = C[comp]["states"][state]
    for p in c.get("paint") or []:
        bg = p.get("bg") or ""
        m = re.fullmatch(r"rgba?\(([\d.]+),\s*([\d.]+),\s*([\d.]+)(?:,\s*([\d.]+))?\)", bg)
        if m and (m.group(4) is None or float(m.group(4)) >= 1):
            return bg
    raise KeyError("innerFill")


# ------------------------------------------------------------------- fonts
#
# Both surfaces set Inter: the marketing site self-hosts woff2 faces on the
# Webflow CDN (400–700), the app loads Inter 500 from Google Fonts. No
# marketing size variable exists — the ramp is measured px on real
# components, honestly labelled; --_apps---typography--* declares the family
# on :root and is emitted with the palette below.

fam = SPEC["core"].setdefault("font", {}).setdefault("family", {})
try:
    v = st("hero-h1", "default")["fontFamily"]
    fam["inter"] = lit(v, "fontFamily",
        "computed fontFamily of hero-h1 default (raw/components-computed.json); the self-hosted Inter @font-face faces and the declared --_apps---typography--* vars in raw/css-vars.json",
        "Inter — the family every surface sets: self-hosted woff2 on the marketing site (400–700), Google-Fonts Inter 500 on the app.")
except KeyError:
    pass

weights = SPEC["core"].setdefault("font", {}).setdefault("weight", {})
for key, comp, state, desc in [
    ("regular", "plan-row", "default", "The 400 body weight on plan rows, FAQ and app fields."),
    ("medium", "hero-eyebrow", "default", "The 500 weight on the trust eyebrow and app headings."),
    ("semibold", "nav-cta", "default", "The 600 weight on nav links, buttons and body lead-ins."),
    ("bold", "hero-h1", "default", "The display-heading weight: the 72px masthead and section headings are 700."),
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
    ("display", "feat-h1", "default", "The 96px feature-page display heading."),
    ("hero", "hero-h1", "default", "The 72px hero masthead and section headings."),
    ("planName", "plan-card", "default", "The 36px plan-name heading inside pricing cards."),
    ("button", "hero-cta", "default", "The 30px hero-button size."),
    ("tab", "ptab-annual", "default", "The 25.6px billing-tab size."),
    ("planCta", "plan-cta", "default", "The 24px plan-CTA size."),
    ("faq", "faq-q", "default", "The 20px FAQ-question and contact-field size."),
    ("body", "plan-row", "default", "The 16px body/nav size."),
    ("eyebrow", "hero-eyebrow", "default", "The 12px trust-eyebrow size."),
    ("mobileHero", "m-hero-h1", "default", "The masthead at 390 wide."),
]:
    try:
        v = ts(comp, state, "fontSize") or st(comp, state)["fontSize"]
        sizes[key] = lit(norm_len(v), "dimension", f"computed fontSize of {comp} {state} (raw/components-computed.json)", desc)
    except KeyError:
        pass

lh = SPEC["core"].setdefault("font", {}).setdefault("lineHeight", {})
for key, comp, state, desc in [
    ("hero", "hero-h1", "default", "The hero masthead leading (72/72)."),
    ("body", "plan-row", "default", "The body leading."),
    ("eyebrow", "hero-eyebrow", "default", "The trust-eyebrow leading."),
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
# The marketing :root vocabulary — the canonical declaration. The flat
# legacy palette lands at natural paths (dodger.blue, light.steel.blue…);
# the Webflow _apps--- layer lands under apps.* (its -dark twins are
# declared-but-unpainted evidence kept verbatim).

mkt_names = sorted(n for n in HOST_NAMES["marketing"] if declared(n, "light") is not None)
app_names = sorted(n for n in HOST_NAMES["app"] if declared(n, "app") is not None)


def emit_named(setroot, name, val):
    """Emit a declared name at its natural path in the set."""
    emit(setroot, name, var(name, leaf_type(name, val)))


for name in mkt_names:
    emit_named(SPEC["core"], name, R.get(name))

# The alias maps are collected in a second pass: emit() can rename a leaf to
# `name.default` when a later variable needs its path as a group, and
# EMITTED is only final once the whole set is written. The flat legacy
# palette is the vocabulary components are actually styled with — a measured
# #000000 aliases {black}, not the _apps layer's foreground that merely
# shares the value — so flat names claim a shared colour first.
color_alias = {}   # normalized colour -> token path for light-set aliasing
for name in sorted(mkt_names, key=lambda n: n.startswith("--_apps")):
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
    (sem, "light", "ink", "hero-h1", "default", "color", "text",
     "The black ink on headings and body copy (the declared --black)."),
    (sem, "light", "muted", "nav-link", "default", "color", "text",
     "The #222 nav-link ink — one step off pure black."),
    (sem, "light", "cta-ring", "hero-cta", "default", "backgroundColor", "action",
     "The translucent dodger-blue halo the pill buttons paint as their outer box (the declared --dodger-blue-20)."),
    (sem, "light", "cta-fill", "hero-cta", "default", "innerFill", "action",
     "The solid #0080ff fill the CTA's inner .btn__wrapper paints (the declared --dodger-blue)."),
    (sem, "light", "cta-ink", "hero-cta", "default", "color", "action",
     "The white text on the blue pills (the declared --white)."),
    (sem, "light", "nav-fill", "nav-cta", "default", "backgroundColor", "action",
     "The near-black fill of the header 'Try for free' pill (the declared --black)."),
    (sem, "light", "nav-ink", "nav-cta", "default", "color", "action",
     "The white text on the black header pill."),
    (sem, "light", "card", "plan-card", "default", "backgroundColor", "surface",
     "The white pricing-card surface (the declared --white)."),
    (sem, "light", "card-featured", "plan-card-paid", "default", "backgroundColor", "surface",
     "The inverted black featured-plan card (Team)."),
    (sem, "light", "field", "contact-field", "default", "backgroundColor", "surface",
     "The white contact-field surface."),
    (sem, "light", "focus-ring", "nav-cta", "focus-visible", "outlineColor", "border",
     "The keyboard focus ring on controls, where the browser paints one."),
    (asem, "app", "ink", "login-h1", "default", "color", "text",
     "The app's heading ink #1f1f1f (the declared --primary-basic-gray-880)."),
    (asem, "app", "muted", "login-field", "default", "color", "text",
     "The field placeholder/hint ink #999 (the declared --primary-basic-gray-400)."),
    (asem, "app", "link", "login-forgot", "default", "color", "text",
     "The 'Forgot password?' grey link ink."),
    (asem, "app", "field-bg", "login-field", "default", "backgroundColor", "surface",
     "The #f5f5f5 auth-field fill (the declared --neutral-gray-40 / --primary-basic-gray-40)."),
    (asem, "app", "oauth-border", "login-google", "default", "borderTopColor", "border",
     "The OAuth button's 1px rgba(0,0,0,0.12) hairline (the declared --neutral-gray-opacity-120)."),
    (asem, "app", "primary-fill", "login-submit", "enabled", "backgroundColor", "action",
     "The enabled submit fill #0050ff (the declared --primary-basic-blue), painted once sample text sits in both fields — never submitted."),
    (asem, "app", "primary-fill-disabled", "login-submit", "default", "backgroundColor", "action",
     "The submit's disabled fill #9fb8f9 at rest — a desaturated blue no declared name holds."),
    (asem, "app", "primary-ink", "login-submit", "enabled", "color", "action",
     "The white text on the app primary button."),
    (asem, "app", "viewer-ink", "sh-menu", "default", "color", "text",
     "The share viewer's #707070 button ink (the declared --primary-basic-gray-560)."),
    (asem, "app", "popup", "sh-popup", "default", "backgroundColor", "surface",
     "The sign-up nudge's rgba(0,0,0,0.56) dark toast fill."),
    (asem, "app", "share-card", "sh-card", "default", "backgroundColor", "surface",
     "The white sitemap page-card fill on the shared canvas."),
    (asem, "app", "share-card-border", "sh-card", "default", "borderTopColor", "border",
     "The page card's 2px #1f1f1f outline (the declared --primary-basic-gray-880)."),
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

# The page field: the marketing body paints on the declared --bg #f6f8fa
# (the page chrome behind every white card), the app keeps a near-white
# root field behind the auth card.
if "--bg" in EMITTED:
    sem.setdefault("background", {})["page"] = lit(
        "{%s}" % EMITTED["--bg"], "color",
        "the body/html field behind every marketing page (screenshots/*-light-*.png); the declared --bg",
        "The #f6f8fa page field the marketing pages paint on.")
if "--primary-basic-white" in EMITTED:
    asem.setdefault("background", {})["page"] = lit(
        "{%s}" % EMITTED["--primary-basic-white"], "color",
        "the body field behind the signed-out auth cards and the share viewer chrome (screenshots/login-*, share-*); the declared --primary-basic-white",
        "The white app page field.")

# ------------------------------------------------------------------ shape
#
# The marketing sheets declare one radius variable
# (--_apps---sizes--radius, 20px, emitted with the palette); the rest of the
# scale is measured on real controls and cards.

radii = SPEC["core"].setdefault("radius", {})
for key, comp, state, prop, desc in [
    ("control", "nav-link", "default", "borderTopLeftRadius", "The 8px radius on nav links and flyout rows."),
    ("button", "nav-cta", "default", "borderTopLeftRadius", "The 12px radius on the header pill buttons."),
    ("app-button", "sh-menu", "default", "borderTopLeftRadius", "The 12px radius on the share viewer's buttons."),
    ("field", "login-field", "default", "borderTopLeftRadius", "The 16px radius on the app auth fields and submit."),
    ("share-card", "sh-card", "default", "borderTopLeftRadius", "The 16px radius on the shared sitemap page cards."),
    ("card", "plan-card", "default", "borderTopLeftRadius", "The 24px pricing-card radius."),
    ("pill", "hero-cta", "default", "borderTopLeftRadius", "The pill radius on the big CTAs — the sheets set it to 1600px, far past any rendered length."),
    ("popup", "sh-popup", "default", "borderTopLeftRadius", "The 14px radius on the share viewer's sign-up toast."),
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
for comp in ("nav-link", "nav-cta", "login-forgot", "sh-card"):
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
    ("nav-cta-height", "nav-cta", "default", "h", "dimension", "The header pill height."),
    ("nav-pop-width", "nav-pop-item", "default", "w", "dimension", "The Features flyout row width."),
    ("hero-cta-height", "hero-cta", "default", "h", "dimension", "The hero pill height including its halo."),
    ("hero-cta-width", "hero-cta", "default", "w", "dimension", "The hero pill width."),
    ("hero-width", "hero-h1", "default", "w", "dimension", "The hero masthead measure."),
    ("ptab-height", "ptab-annual", "default", "h", "dimension", "The billing-tab pill height."),
    ("plan-card-width", "plan-card", "default", "w", "dimension", "The pricing-card width."),
    ("plan-card-height", "plan-card", "default", "h", "dimension", "The pricing-card height."),
    ("plan-cta-height", "plan-cta", "default", "h", "dimension", "The plan-CTA pill height."),
    ("faq-row-height", "faq-q", "default", "h", "dimension", "The closed FAQ row height."),
    ("contact-field-width", "contact-field", "default", "w", "dimension", "The contact-field width."),
    ("mobile-topbar-height", "m-topbar", "default", "h", "dimension", "The phone header height."),
    ("mobile-cta-height", "m-hero-cta", "default", "h", "dimension", "The hero pill at 390 wide."),
]:
    try:
        v = rc(cname, state, prop)
        comp_t[name] = lit(("%g" % v) + "px" if isinstance(v, (int, float)) else str(v) + "px",
                          ty_, f"measured {prop} of {cname} {state} (raw/components-computed.json)", desc)
    except KeyError:
        pass

# The signed-out app forms and the share viewer: measured literals on their
# own surface.
appf = comp_t.setdefault("app", {})
for name, cname, state, prop, ty_, desc in [
    ("card-width", "login-card", "default", "w", "dimension", "The auth card width."),
    ("card-height", "login-card", "default", "h", "dimension", "The auth card height."),
    ("field-height", "login-field", "default", "h", "dimension", "The auth field height."),
    ("field-width", "login-field", "default", "w", "dimension", "The auth field width."),
    ("submit-height", "login-submit", "default", "h", "dimension", "The primary submit height."),
    ("share-menu-width", "sh-menu", "default", "w", "dimension", "The share viewer 'Demo Project' button width."),
    ("share-toolbar-btn", "sh-toolbar-btn", "default", "h", "dimension", "The canvas toolbar icon-button size."),
    ("share-card-width", "sh-card", "default", "w", "dimension", "The sitemap page-card width at the captured zoom."),
    ("share-card-height", "sh-card", "default", "h", "dimension", "The sitemap page-card height at the captured zoom."),
    ("share-popup-width", "sh-popup", "default", "w", "dimension", "The sign-up nudge toast width."),
    ("userflow-card-width", "uf-card", "default", "w", "dimension", "The user-flow card width at the captured zoom."),
    ("userflow-card-height", "uf-card", "default", "h", "dimension", "The user-flow card height at the captured zoom."),
]:
    try:
        if prop in ("w", "h"):
            v = rc(cname, state, prop)
            appf[name] = lit(("%g" % v) + "px", ty_, f"measured {prop} of {cname} {state} on app.flowmapp.com (raw/components-computed.json)", desc)
        else:
            v = st(cname, state)[prop]
            appf[name] = lit(v, ty_, f"computed {prop} of {cname} {state} on app.flowmapp.com (raw/components-computed.json)", desc)
    except KeyError:
        pass

(RAW / "component-tokens.json").write_text(json.dumps(SPEC, indent=2, ensure_ascii=False) + "\n")
print("component-tokens.json:", {k: len(v) for k, v in SPEC.items() if k != "_about"})
