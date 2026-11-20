#!/usr/bin/env python3
"""Write raw/component-tokens.json, the token spec build_tokens.py reads.

fibery.com paints one surface signed out: a light-only marketing site (home,
/pricing, /templates, plus the captured /features, /blog, /customer-stories
and /101-questions-about-fibery pages). fibery.io/sign-up and
fibery.io/login/ — the public workspace-creation wizard and sign-in — serve
the same stylesheets and the same token layer. There is no theme toggle and
no dark scope anywhere public; the signed-in app's dark/system theme (its
login page advertises it) is behind sign-in and was not captured.

The site declares a real design-token layer in the linked
/_next/static/css/ bundle (raw/css-vars.json), all on :root:

  --fibery-<name>      the named palette: warm neutrals milk/cream/soup/
                       peach-soup/tea, the rust family rusty/rusty-peach/
                       rusty-text/terracotta/architect-rust, mud-text,
                       greyhound ink, green-olives, website-blue
  --fibery-basic-*     the saturated brand ramp (red yellow blue pink orange
                       green violet mint + black white)
  --fibery-secondary-* the mid tint of each hue
  --fibery-tertiary-*  the light tint
  --fibery-quaternary-*the lightest tint (quaternary-yellow #fbf0e1 tints
                       the pricing plan cards)
  --fibery-page-*      page roles: body #faebd6, body-light #fdf7ef,
                       main #309fb6 (the teal accent), menu-bg #fff5e8;
                       page-secondary ships the literal `undefined`
  --fibery-text-*      ink roles: default #251d1a, secondary rgba(.5),
                       opposite #fffdfa; text-selection ships `undefined`
  --fibery-gray-* /    utility surfaces and the icon/border greys
  --fibery-*-gray-*
  --fibery-form-*/     the form surface white and the form/business blue
  --fibery-business-*  #3b758c (website-blue under three names)
  --fibery-shadow-m    the one declared drop shadow

There is no declared type ramp, spacing scale, radius scale or breakpoint
in the CSS layer — those arrive measured from raw/components-computed.json
(the kit's computed styles on the live pages):

  fonts       Suisse Intl (100–900, every control and body), Fraunces Var
              (the serif display on headlines and quotes), Casuar and
              Plus Jakarta Sans on special surfaces — @font-face in the
              same bundle
  ramp        measured steps: the hero headline, section h2, nav pill,
              button and lede sizes at 1440 and 390
  shape       measured radii: the pill nav/buttons, rounded cards and the
              prompt field
  motion      the measured control transitions (no declared motion layer)
"""

import json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
V = json.loads((RAW / "css-vars.json").read_text())
RL = V.get("resolved", {}).get("light", {})
C = json.loads((RAW / "components-computed.json").read_text())["components"]
R = {n: (v.get("value", v.get("raw")) if isinstance(v, dict) else v) for n, v in RL.items()}


def var(name, ty="color", **kw):
    d = {"var": name, "type": ty}
    d.update(kw)
    return d


SPEC = {"_about": (
    "The token tree build_tokens.py turns into tokens.json. fibery.com "
    "declares its design-token layer on :root in the /_next/static/css/ "
    "bundle (raw/css-vars.json): the --fibery-* named palette, the four-tier "
    "basic/secondary/tertiary/quaternary hue ramp, the page/text/gray "
    "semantic roles and --fibery-shadow-m — all theme-invariant, so they "
    "land under core.*; the semantic roles are also surfaced under light.* "
    "as {var} leaves. Measured roles alias to the declared values where "
    "they match. There is no dark scope on the public site: no dark set is "
    "emitted and $themes carries only light."),
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



# A transparent reading is no fill (the colour comes from an ancestor), so it
# is never committed as one (2026-11 audit, finding 14-8).
TRANSPARENT = re.compile(r"transparent|rgba\(\s*[\d.]+[,\s]+[\d.]+[,\s]+[\d.]+\s*[,/]\s*0(\.0+)?%?\s*\)")


def opaque(v):
    """v unless it is a transparent reading; a KeyError skips the token."""
    if v is None or TRANSPARENT.fullmatch(str(v).strip()):
        raise KeyError("transparent")
    return v

def lit(value, ty, src, desc):
    return {"value": norm_color(value) if ty == "color" else value, "type": ty, "source": src, "description": desc}


EMITTED = {}   # variable name -> dotted token path it was actually written to
_OWNER = {}    # dotted token path -> variable name holding it


def _leaf(d):
    return isinstance(d, dict) and ("var" in d or "value" in d)


def emit(root, name, leaf_):
    """Write `leaf` at name's dotted path under root (the --fibery- prefix is
    kept: fibery's own names are already the taxonomy)."""
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
                node[last][key] = leaf_
                path += "." + key
                break
        else:
            raise ValueError(f"{name}: no free key to hold the leaf beside its group")
    else:
        if last in node:
            raise ValueError(f"{name}: duplicate token path {path}")
        node[last] = leaf_
    EMITTED[name] = path
    _OWNER[path] = name


def emitted_path(name):
    return EMITTED[name]


DECL_SRC = ("declared :root variable in fibery.com's /_next/static/css/ "
            "bundle (raw/css-vars.json)")


def declared(name):
    """The resolved value, or None when the var never resolved. Fibery's two
    `undefined` declarations resolve to the literal 'undefined' — kept as
    a string so the broken declaration is documented, not dropped."""
    v = R.get(name)
    return v if v not in (None, "") else None


def decl(name, ty="dimension"):
    v = declared(name)
    desc = f"The declared `{name}`."
    if v == "undefined":
        return lit("undefined", "other",
                   f"{DECL_SRC}: {name} — declared as the literal `undefined`, which resolves to nothing",
                   f"The declared `{name}` — Fibery ships it as `undefined`; it resolves to nothing on the page.")
    if ty == "dimension":
        nv = norm_len(v)
        if nv != v:
            raw = (RL.get(name) or {}).get("raw")
            desc = f"The declared `{name}` — `{raw}`, which Chromium resolves to {nv} (effectively a full pill)."
            v = nv
        if not re.fullmatch(r"-?\d+(\.\d+)?(px|rem)", str(v).strip()):
            ty = "other"
    return lit(v, ty, f"{DECL_SRC}: {name}", desc)


COLOR_V = re.compile(r"(#[0-9a-fA-F]{3,8}|rgba?\([^)]*\)|hsla?\([^)]*\)|(ok)?lab\([^)]*\)|(ok)?lch\([^)]*\)|color-mix\([^)]*\))")


def decl_color(name):
    v = declared(name)
    if v == "undefined":
        return decl(name, "other")
    ty = "color" if COLOR_V.fullmatch(str(v).strip()) else "other"
    return lit(v, ty, f"{DECL_SRC}: {name}", f"The declared `{name}`.")


def norm_len(v):
    """Exponential lengths become ordinary pixel strings."""
    m = re.fullmatch(r"(-?[\d.]+[eE][+-]?\d+)(px|rem)", str(v).strip())
    if not m:
        return v
    return f"{float(m.group(1)):f}".rstrip("0").rstrip(".") + m.group(2)


def painted(comp, state, key):
    """A reading from the kit's paint list — the layers actually painted
    rather than the wrapper's computed style."""
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
    """The colour of a painted inset (hairline) box-shadow layer."""
    sh = painted(comp, state, "shadow")
    m = re.search(COLOR_V.pattern + r"(?:\s+-?[\d.]+px){2,4}\s+inset", sh)
    if not m:
        raise KeyError("insetShadowColor")
    return m.group(1)


# ------------------------------------------------------------------- core
#
# The declared token layer: every --fibery-* name on :root, emitted under
# its own name (the prefix is stripped; the names are already the taxonomy:
# color.named.*, color.basic.*, color.secondary.*, color.tertiary.*,
# color.quaternary.*, page.*, text.*, gray.*, form/business, shadow.m).

colors = SPEC["core"].setdefault("color", {})
color_alias = {}   # normalized colour -> 'color.<path>' for aliasing

NAMED = {
    "milk": "The warmest white #fffdfa — card fills and text-opposite ink.",
    "cream": "The page-body-light cream #fdf7ef.",
    "soup": "The page-body soup #faebd6 — the warm field behind the pages.",
    "peach-soup": "A deeper peach #eed0bf.",
    "tea": "The warm tan #f6d3a0.",
    "rusty": "The mid rust #c17b58.",
    "rusty-peach": "The soft rust peach #f0b89b.",
    "rusty-text": "The rust ink #a26e51 — brand-tinted text accents.",
    "terracotta": "The terracotta accent #e89469.",
    "architect-rust": "The deepest rust #cb5800.",
    "mud-text": "The muted mud ink #9f8b7f.",
    "greyhound": "The warm grey #3c3c3b.",
    "green-olives": "The olive green #66753d (same value as basic-green).",
    "website-blue": "The website blue #3b758c — form buttons, business links.",
}
for name, desc in NAMED.items():
    vn = f"--fibery-{name}"
    if declared(vn) is not None:
        key = re.sub(r"-([a-z])", lambda m: m.group(1).upper(), name)
        colors.setdefault("named", {})[key] = decl_color(vn)
        color_alias.setdefault(norm_color(R[vn]), f"color.named.{key}")

TIERS = ("basic", "secondary", "tertiary", "quaternary")
HUES = ("red", "yellow", "blue", "pink", "orange", "green", "violet", "mint",
        "black", "white")
TIER_DESC = {
    "basic": "The saturated brand ramp — plan icons, chart accents, tag fills.",
    "secondary": "The mid tint of each hue.",
    "tertiary": "The light tint of each hue.",
    "quaternary": "The lightest tint — quaternary-yellow tints the pricing plan cards.",
}
for tier in TIERS:
    for hue in HUES:
        vn = f"--fibery-{tier}-{hue}"
        if declared(vn) is not None:
            colors.setdefault(tier, {})[hue] = lit(
                R[vn], "color" if COLOR_V.fullmatch(str(R[vn]).strip()) else "other",
                f"{DECL_SRC}: {vn}", TIER_DESC[tier])
            color_alias.setdefault(norm_color(R[vn]), f"color.{tier}.{hue}")
vn = "--fibery-form-white"
if declared(vn) is not None:
    colors.setdefault("form", {})["white"] = decl_color(vn)
    color_alias.setdefault(norm_color(R[vn]), "color.form.white")

# The declared drop shadow — kept as the full box-shadow string.
if declared("--fibery-shadow-m") is not None:
    SPEC["core"].setdefault("shadow", {})["m"] = lit(
        (RL.get("--fibery-shadow-m") or {}).get("value") or R["--fibery-shadow-m"],
        "other", f"{DECL_SRC}: --fibery-shadow-m",
        "The one declared elevation: 0 10px 16px -3px rgba(20,21,26,.08), 0 1px 2px rgba(20,21,26,.05).")

# ------------------------------------------------------------------- fonts
#
# @font-face declarations in the same bundle (no font variables are
# declared): Suisse Intl carries the UI, Fraunces Var the serif display,
# Casuar and Inter Var special surfaces. Families land under core.font,
# evidenced by the @font-face declarations plus the computed fontFamily the
# kit measured on real components.

FONTS = [
    ("suisse", "Suisse Intl", ("hero-cta", "default"),
     "Suisse Intl — every control, nav item and body copy (100–900 static weights in the bundle)."),
    ("fraunces", "Fraunces Var", ("section-h2", "default"),
     "Fraunces Var — the serif display on headlines, section titles and quotes (a variable face, wght 100–900)."),
    ("casuar", "Casuar", None,
     "Casuar — a display face declared in the bundle for special surfaces."),
    ("inter", "Inter Var", None,
     "Inter Var — declared for embedded/widget surfaces."),
]
fam = SPEC["core"].setdefault("font", {}).setdefault("family", {})
faces = {(f.get("font-family") or "").strip('"').lower() for f in V.get("fonts", [])}
for key, family, meas, desc in FONTS:
    src = f"@font-face for \"{family}\" in the /_next/static/css/ bundle (raw/css-vars.json fonts)"
    if family.lower() not in faces:
        continue
    if meas:
        try:
            cf = st(*meas).get("fontFamily", "")
            if family.split()[0].lower() in cf.lower():
                src += f"; computed fontFamily of {meas[0]} {meas[1]}"
            fam[key] = lit(f'"{family}", sans-serif', "fontFamily", src, desc)
            continue
        except KeyError:
            pass
    fam[key] = lit(f'"{family}", sans-serif', "fontFamily", src, desc)

# ------------------------------------------------------------- type ramp
#
# Fibery declares no size ramp in CSS — the steps are measured on the real
# components at 1440 x 900 (and the mobile hero at 390 x 844).

sizes = SPEC["core"].setdefault("font", {}).setdefault("size", {})
for key, comp, state, desc in [
    ("display", "hero-h1", "default", "The hero headline step — Fraunces at the top of the ramp."),
    ("h2", "section-h2", "default", "The section-heading step."),
    ("lede", "hero-lede", "default", "The supporting-paragraph step."),
    ("nav", "nav-item", "default", "The nav-pill/button text step."),
    ("body", "faq-item", "default", "The body copy step on the pricing FAQ."),
    ("displayMobile", "m-hero-h1", "default", "The hero headline at 390 wide."),
]:
    try:
        raw = st(comp, state)["fontSize"]
        lh = st(comp, state)["lineHeight"]
        sizes[key] = lit(raw, "dimension",
                         f"computed fontSize of {comp} {state} (raw/components-computed.json)",
                         desc + f" Line-height {lh}." if lh else desc)
    except KeyError:
        pass
for key, comp, state, desc in [
    ("display", "hero-h1", "default", "The hero display weight."),
    ("h2", "section-h2", "default", "The section-heading weight."),
    ("nav", "nav-item", "default", "The nav-pill weight."),
    ("button", "hero-cta", "default", "The button label weight."),
    ("body", "faq-item", "default", "The body copy weight."),
]:
    try:
        v = st(comp, state)["fontWeight"]
        SPEC["core"]["font"].setdefault("weight", {})[key] = lit(
            int(v), "fontWeight",
            f"computed fontWeight of {comp} {state} (raw/components-computed.json)", desc)
    except (KeyError, ValueError):
        pass

# ------------------------------------------------------------------ shape
#
# No declared radius scale — the corners are measured.

radii = SPEC["core"].setdefault("radius", {})
for key, comp, state, prop, desc in [
    ("pill", "hero-cta", "default", "borderTopLeftRadius",
     "The fully-rounded button/nav pill (FiberyButton)."),
    ("card", "plan-card", "default", "borderTopLeftRadius",
     "The plan-card corner."),
    ("field", "su-field", "default", "borderTopLeftRadius",
     "The sign-up prompt field corner."),
    ("menu", "nav-panel", "default", "borderTopLeftRadius",
     "The dropdown panel corner."),
]:
    try:
        v = norm_len(st(comp, state)[prop])
        radii[key] = lit(v, "dimension" if re.fullmatch(r"[0-9.]+(px|rem)", v or "") else "other",
                         f"computed {prop} of {comp} {state} (raw/components-computed.json)", desc)
    except KeyError:
        pass

# ------------------------------------------------------------------ motion

mo = SPEC["core"].setdefault("motion", {})
for key, comp, desc in [
    ("control", "hero-cta", "The button/pill hover transition."),
    ("navItem", "nav-item", "The nav-link hover transition."),
]:
    try:
        s = st(comp, "default")
        dur, ease = s.get("transitionDuration"), s.get("transitionTimingFunction")
        if dur and dur != "0s":
            props = [p.strip() for p in s.get("transitionProperty", "all").split(",") if p.strip()]
            val = ", ".join(f"{p} {dur} {ease or ''}".strip() for p in props)
            mo[key] = lit(val, "other",
                          f"computed transition of {comp} default (raw/components-computed.json)", desc)
    except KeyError:
        pass

# -------------------------------------------------------- semantic roles
#
# The --fibery-page-*/text-*/gray-*/menu/form/business roles emitted under
# light.* as {var} leaves; the two `undefined` declarations are kept, marked
# unresolved.

sem = SPEC["light"]
for name in sorted(n for n in R if re.fullmatch(
        r"--fibery-(page|text|menu|gray|light-gray|medium-gray|form|business)-[a-z-]*color", n)):
    emit(sem, name, var(name, "color" if COLOR_V.fullmatch(str(R.get(name, "")).strip()) else "other"))

# ------------------------------------------------------------- measured
#
# Roles measured on the real pages; each aliases to the declared token its
# value matches.

role_alias = dict(color_alias)
for name, p in EMITTED.items():
    if R.get(name):
        role_alias.setdefault(norm_color(R[name]), p)


def semcolor(raw, src, desc):
    alias = role_alias.get(norm_color(raw))
    value = f"{{{alias}}}" if alias else norm_color(raw)
    return lit(value, "color", src + (f"; matches declared {alias}" if alias else ""), desc)


for key, comp, state, prop, group, desc in [
    ("ink", "hero-h1", "default", "color", "text",
     "The #251d1a near-black on display copy, headings and controls (text-default-color)."),
    ("muted", "hero-lede", "default", "color", "text",
     "The secondary ink on lede copy."),
    ("ctaFill", "hero-cta", "default", "backgroundColor", "action",
     "The fill of the dark 'Sign up' pill buttons."),
    ("ctaInk", "hero-cta", "default", "color", "action",
     "The text on the dark pill buttons."),
    ("ctaOutline", "hero-cta2", "default", "borderTopColor", "border",
     "The border of the outlined 'Book a Demo' button."),
    ("focusRing", "nav-item", "focus-visible", "outlineColor", "border",
     "The keyboard focus ring colour."),
    ("link", "footer-link", "default", "color", "text",
     "The footer link ink."),
    ("planTint", "plan-card", "default", "backgroundColor", "background",
     "The tinted plan-card surface (quaternary-yellow on the Free plan)."),
    ("field", "su-field", "default", "backgroundColor", "background",
     "The sign-up prompt field fill."),
    ("fieldInk", "su-field", "default", "color", "text",
     "The field text ink."),
    ("oauthFill", "login-google", "default", "backgroundColor", "background",
     "The OAuth button fill on the sign-in."),
    ("menuBg", "nav-panel", "default", "backgroundColor", "background",
     "The open dropdown panel fill (menu-bg cream)."),
]:
    try:
        if prop == "color":
            raw = ts(comp, state, "color")
            src = f"computed color of {comp} {state} — the first text node's reading where the kit recorded one (raw/components-computed.json)"
        else:
            raw = st(comp, state)[prop]
            src = f"computed {prop} of {comp} {state} (raw/components-computed.json)"
        if raw in (None, "") or (prop == "backgroundColor" and TRANSPARENT.fullmatch(str(raw).strip())):
            raise KeyError(prop)
        sem.setdefault(group, {})[key] = semcolor(raw, src, desc)
    except KeyError:
        pass

# The page field: --fibery-page-body-color paints the warm soup behind the
# marketing pages; page-body-color-light the cream of the content cards.
if declared("--fibery-page-body-color") is not None:
    p = EMITTED.get("--fibery-page-body-color")
    sem.setdefault("background", {})["page"] = lit(
        "{%s}" % p if p else norm_color(R["--fibery-page-body-color"]),
        "color",
        f"{DECL_SRC}: --fibery-page-body-color; visible as the warm soup field behind the marketing pages (screenshots/home-light-*.png)",
        "The warm soup page field.")

# ------------------------------------------------------------- components

comp = SPEC["component"]
for name, cname, state, prop, ty_, desc in [
    ("header-height", "mkt-header", "default", "h", "dimension", "The marketing header bar height."),
    ("logo-width", "mkt-logo", "default", "w", "dimension", "The Fibery wordmark width."),
    ("nav-item-height", "nav-item", "default", "h", "dimension", "The nav-link height."),
    ("nav-button-height", "nav-signup", "default", "h", "dimension", "The header button height."),
    ("dropdown-width", "nav-panel", "default", "w", "dimension", "The open dropdown panel width."),
    ("dropdown-height", "nav-panel", "default", "h", "dimension", "The open dropdown panel height."),
    ("hero-measure", "hero-h1", "default", "w", "dimension", "The hero headline measure."),
    ("hero-cta-height", "hero-cta", "default", "h", "dimension", "The hero button height."),
    ("plan-card-width", "plan-card", "default", "w", "dimension", "The plan-card width."),
    ("plan-card-height", "plan-card", "default", "h", "dimension", "The plan-card height."),
    ("faq-head-height", "faq-item", "default", "h", "dimension", "A closed FAQ row height."),
    ("signup-panel-width", "su-panel", "default", "w", "dimension", "The sign-up wizard panel width."),
    ("prompt-field-height", "su-field", "default", "h", "dimension", "The AI prompt textarea height."),
    ("login-panel-width", "login-panel", "default", "w", "dimension", "The sign-in panel width."),
    ("oauth-height", "login-google", "default", "h", "dimension", "The OAuth button height."),
    ("mobile-topbar-height", "m-topbar", "default", "h", "dimension", "The phone top bar height."),
    ("mobile-menu-size", "m-menu-btn", "default", "w", "dimension", "The sandwich button size."),
]:
    try:
        v = rc(cname, state, prop)
        comp[name] = lit(("%g" % v) + "px" if isinstance(v, (int, float)) else str(v) + "px",
                         ty_, f"measured {prop} of {cname} {state} (raw/components-computed.json)", desc)
    except KeyError:
        pass

(RAW / "component-tokens.json").write_text(json.dumps(SPEC, indent=2, ensure_ascii=False) + "\n")
print("component-tokens.json:", {k: len(v) for k, v in SPEC.items() if k != "_about"})
