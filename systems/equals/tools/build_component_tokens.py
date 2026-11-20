#!/usr/bin/env python3
"""Write raw/component-tokens.json, the token spec build_tokens.py reads.

Equals' signed-out surface is three public sites, captured on 2026-11-13:

  equals.com      the marketing site: light only, BEM classes, a --brand-*
                  palette on :root (raw/css-vars.json) and per-page
                  .accent--*/.label--* body themes (the accent dictionary in
                  resolved.accents). Unica77 body, Serrif Condensed display,
                  Aeonik Fono eyebrows, 14-18px marketing text on a
                  cream #FAF9F5 field, 60px-pill CTAs on accent backgrounds.
  go.equals.com   the sign-in card: light only, the Rails app's one public
                  view, a Tailwind-style --color-* ramp palette on :root
                  (--color-grey-25..900, --color-purple-*, --color-primary
                  #7839e5) with neue-haas-unica text, an 8px-radius field and
                  the #7c3aed Continue submit.
  docs.equals.com the Mintlify docs: real light AND dark themes
                  (html.light/html.dark over prefers-color-scheme), Inter on
                  --gray-* triplets, --primary #7839e5, --background-light
                  #ffffff / --background-dark #0b0a0f and
                  --default-border-color that genuinely flips per theme
                  (#f1eff5 / #29272c).

Declared scales land under core.*; per-theme semantics under light.* and
dark.*; measured geometry under component.*. The marketing site and sign-in
card paint light only, so their roles exist only in the light set — the
dark set holds the docs theme alone.
"""

import json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
V = json.loads((RAW / "css-vars.json").read_text())
RL = V.get("resolved", {}).get("light", {})
RD = V.get("resolved", {}).get("dark", {})
ACC = V.get("resolved", {}).get("accents", {})
C = json.loads((RAW / "components-computed.json").read_text())["components"]
R = {n: (v.get("value", v.get("raw")) if isinstance(v, dict) else v) for n, v in RL.items()}
D = {n: (v.get("value", v.get("raw")) if isinstance(v, dict) else v) for n, v in RD.items()}


def var(name, ty="color", **kw):
    d = {"var": name, "type": ty}
    d.update(kw)
    return d


SPEC = {"_about": (
    "The token tree build_tokens.py turns into tokens.json. Equals' public "
    "surface is three sites: the equals.com marketing pages (light only, "
    "--brand-* palette and .accent--*/.label--* body themes), the "
    "go.equals.com sign-in card (light, --color-* Tailwind-style ramps) and "
    "the docs.equals.com Mintlify docs (light and dark, --primary/--gray-*/"
    "--background-* semantics). Declared scales under core.*; the marketing "
    "and sign-in roles under light.*; the docs roles under both light.* and "
    "dark.* (Mintlify's dark is a real theme). Measured roles alias the "
    "declared values they match."),
    "core": {}, "light": {}, "dark": {}, "component": {}, "_gaps": []}


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


def _srgb_to_hex(r, g, b):
    return "#%02x%02x%02x" % tuple(max(0, min(255, round(x * 255))) for x in (r, g, b))


def _linear(u):
    return u / 12.92 if u <= 0.04045 else ((u + 0.055) / 1.055) ** 2.4


def _gamma(u):
    return 12.92 * u if u <= 0.0031308 else 1.055 * u ** (1 / 2.4) - 0.055


def oklab_to_rgb(L, a, b):
    """Björn Ottosson's OKLab -> sRGB matrix, for the oklab()/oklch() tints
    Mintlify's Tailwind-v4 stylesheet paints (nav-item hovers, dark overlay
    alphas). Returns 'rgba(...)' when an alpha is given."""
    l_ = L + 0.3963377774 * a + 0.2158037573 * b
    m_ = L - 0.1055613458 * a - 0.0638541728 * b
    s_ = L - 0.0894841775 * a - 1.2914855480 * b
    l_, m_, s_ = l_ ** 3, m_ ** 3, s_ ** 3
    r = +4.0767416621 * l_ - 3.3077115913 * m_ + 0.2309699292 * s_
    g = -1.2684380046 * l_ + 2.6097574011 * m_ - 0.3413193965 * s_
    b_ = -0.0041960863 * l_ - 0.7034186147 * m_ + 1.7076147010 * s_
    return _gamma(r), _gamma(g), _gamma(b_)


def css_color(v):
    """Normalize a computed colour string to hex/rgba. Handles rgb(), hex,
    color(srgb ...), oklab() and oklch() — the forms the computed styles carry."""
    v = (v or "").strip()
    m = re.fullmatch(r"color\(srgb ([\d.]+) ([\d.]+) ([\d.]+)(?: / ([\d.]+))?\)", v)
    if m:
        r, g, b, a = (float(x) if x else None for x in m.groups())
        if a is None or a >= 1:
            return _srgb_to_hex(r, g, b)
        return "rgba(%d, %d, %d, %s)" % (round(r * 255), round(g * 255), round(b * 255), "%g" % a)
    m = re.fullmatch(r"oklab\(([\d.]+) ([-\d.]+) ([-\d.]+)(?: / ([\d.]+))?\)", v)
    if m:
        L, a, b, al = (float(x) if x else None for x in m.groups())
        r, g, b2 = oklab_to_rgb(L, a, b)
        if al is None or al >= 1:
            return _srgb_to_hex(r, g, b2)
        return "rgba(%d, %d, %d, %s)" % (round(r * 255), round(g * 255), round(b2 * 255), "%g" % al)
    m = re.fullmatch(r"oklch\(([\d.]+) ([\d.]+) ([\d.]+)(?:deg)?(?: / ([\d.]+))?\)", v)
    if m:
        import math
        L, cc, h, al = (float(x) if x else None for x in m.groups())
        a = cc * math.cos(math.radians(h))
        b = cc * math.sin(math.radians(h))
        r, g, b2 = oklab_to_rgb(L, a, b)
        if al is None or al >= 1:
            return _srgb_to_hex(r, g, b2)
        return "rgba(%d, %d, %d, %s)" % (round(r * 255), round(g * 255), round(b2 * 255), "%g" % al)
    return norm_color(v)


COLOR_FULL = re.compile(r"(#[0-9a-fA-F]{3,8}|rgba?\([^)]*\))")


def need(comp, state, prop=None):
    """The style (or one property) of a reading a row relies on. A renamed or missing
    component, state or property stops the build: a silent skip would drop the token and
    still pass."""
    try:
        s = C[comp]["states"][state]
    except KeyError:
        raise SystemExit(f"{comp} {state}: no such reading in raw/components-computed.json; fix the row or recapture")
    if "style" not in s or s.get("skipped") or s.get("via") == "focus failed":
        raise SystemExit(f"{comp} {state}: no usable reading ({s.get('skipped') or s.get('error') or s.get('via')})")
    if prop is None:
        return s["style"]
    v = s["style"].get(prop)
    if v is None or not str(v).strip():
        raise SystemExit(f"{comp} {state}: no {prop} in its reading")
    return v


def gap(path, why):
    """A token the spec deliberately leaves out, with the reason; written to
    raw/component-tokens.json `_gaps` so the omission is on the record."""
    SPEC["_gaps"].append({"token": path, "why": why})


def transparent(v):
    return bool(re.fullmatch(r"rgba\(\s*\d+,\s*\d+,\s*\d+,\s*0\s*\)", css_color(v)))


def split_list(v):
    """Top-level comma split of a computed list value (transitions, shadows)."""
    return [p.strip() for p in re.split(r",\s*(?![^()]*\))", v or "") if p.strip()]


UA_RING = "#101010"  # Chrome's own -webkit-focus-ring-color: an `auto` outline in it is the browser default


def painted_ring(sty):
    """(colour, how) of the focus ring a state really paints, from its computed style: a drawn
    outline (a style other than none, a width above 0, and not the browser's default `auto` ring
    colour), else the outermost visible box-shadow layer with a spread, else None. Ported from
    fal's builder."""
    style, colour = sty.get("outlineStyle", "none"), sty.get("outlineColor")
    if style != "none" and float(sty.get("outlineWidth", "0px")[:-2] or 0) > 0 and not transparent(colour) \
            and not (style == "auto" and css_color(colour) == UA_RING):
        return colour, f"outline {sty['outlineWidth']} {style}"
    ring = None
    for layer in split_list(sty.get("boxShadow", "none")):
        m = re.match(r"^(\S+\([^)]*\)|#[0-9a-fA-F]+)\s+(-?[\d.]+)px\s+(-?[\d.]+)px\s+(-?[\d.]+)px\s+(-?[\d.]+)px(\s+inset)?$", layer)
        if not m or m.group(6) or float(m.group(5)) <= 0 or transparent(m.group(1)):
            continue
        ring = (m.group(1), f"box-shadow {m.group(5)}px spread")
    return ring


def transition(s):
    """The transition shorthand of a computed style, one `<property> <duration> <easing>` item
    per property: CSS repeats the duration and easing lists to the length of the property list,
    so they are paired by index, never pasted after the whole property list."""
    props = split_list(s.get("transitionProperty") or "all")
    durs = split_list(s.get("transitionDuration") or "0s")
    eases = split_list(s.get("transitionTimingFunction") or "ease")
    return ", ".join(f"{p} {durs[i % len(durs)]} {eases[i % len(eases)]}" for i, p in enumerate(props))


def lit(value, ty, src, desc):
    return {"value": css_color(value) if ty == "color" else value, "type": ty, "source": src, "description": desc}


DECL_SRC = "declared variable in the public stylesheets (raw/css-vars.json)"

colors = SPEC["core"].setdefault("color", {})
color_alias = {}   # normalized colour -> 'color.<path>' for aliasing measured roles


# ------------------------------------------------------------- brand palette
#
# equals.com declares --brand-* on :root: the cream/black/grey neutrals and
# the nine-hue accent set the .accent--* body themes draw from.

brand = colors.setdefault("brand", {})
for name in sorted(k for k in R if k.startswith("--brand-")):
    key = name[len("--brand-"):]
    brand[key] = {"var": name, "type": "color" if COLOR_FULL.fullmatch(str(R[name]).strip()) else "other",
                  "description": f"The declared `{name}` — the marketing brand scale."}
    if brand[key]["type"] == "color":
        color_alias.setdefault(norm_color(R[name]), f"color.brand.{key}")

# ------------------------------------------------- app palette (go.equals)
#
# go.equals.com's stylesheet declares a Tailwind-style palette on :root:
# grey-25..900, the hue ramps (blue, cyan, emerald, green, orange, pink,
# purple, red, teal, yellow) and the --color-background/--color-primary/
# --color-shadow roles the sign-in card reads.

app = colors.setdefault("app", {})
for name in sorted(k for k in R if k.startswith("--color-")):
    rest = name[len("--color-"):]
    m = re.fullmatch(r"([a-z]+)-(\d+)", rest)
    node = app.setdefault(m.group(1), {}) if m else app
    key = m.group(2) if m else rest
    ty = "color" if COLOR_FULL.fullmatch(str(R[name]).strip()) else "other"
    node[key] = {"var": name, "type": ty, "description": f"The declared `{name}` — the app's Tailwind-style palette."}
    if ty == "color":
        color_alias.setdefault(norm_color(R[name]),
                               f"color.app.{m.group(1)}.{m.group(2)}" if m else f"color.app.{rest}")

# ------------------------------------------------- docs scale (Mintlify)
#
# docs.equals.com declares Tailwind-style --gray-*/*--primary* triplets
# (resolved to hex by vars.mjs) plus --background-light/--background-dark and
# --default-border-color, the one var that really flips per theme.

docs_c = colors.setdefault("docs", {})
for name in sorted(k for k in R if re.fullmatch(r"--gray-\d+", k)):
    key = name[len("--gray-"):]
    docs_c.setdefault("gray", {})[key] = {"var": name, "type": "color",
                                          "description": f"The declared `{name}` — the docs grey ramp."}
    color_alias.setdefault(norm_color(R[name]), f"color.docs.gray.{key}")
for name, key in [("--primary", "primary"), ("--primary-light", "primary-light"),
                  ("--primary-dark", "primary-dark"), ("--tooltip-foreground", "tooltip-foreground")]:
    if name in R:
        docs_c[key] = {"var": name, "type": "color" if COLOR_FULL.fullmatch(str(R[name]).strip()) else "other",
                       "description": f"The declared `{name}`."}
        if docs_c[key]["type"] == "color":
            color_alias.setdefault(norm_color(R[name]), f"color.docs.{key}")

# ------------------------------------------------------------------- fonts
#
# The marketing site serves Unica77 (body), Serrif Condensed (display),
# Aeonik Fono (eyebrow labels) and Aeonik Pro (sans fallback), plus Lato,
# Inter and Anthropic/HubSpot faces for embedded mockups; the app declares
# neue-haas-unica and JetBrains Mono; the docs read Inter and Paper Mono.

fam = SPEC["core"].setdefault("font", {}).setdefault("family", {})
for name, key, desc in [
    ("--font-unica", "unica", "Unica77 — the marketing body/UI face (nav, lede, buttons, workbook mockup)."),
    ("--font-serif-condensed", "serif-condensed", "Serrif Condensed — the marketing display face ('What's after Excel?', 'ARR Dashboard')."),
    ("--font-fono", "fono", "Aeonik Fono — the monospaced eyebrow labels ('1. TRUST')."),
    ("--font-sans-serif", "sans-serif", "Aeonik Pro — the declared sans stack behind Unica77."),
    ("--font-lato", "lato", "Lato — a declared secondary stack."),
    ("--font-inter", "inter", "Inter — declared; the docs body/UI face."),
    ("--font-hubspot", "hubspot", "HubSpot Sans — a declared mockup face."),
    ("--font-anthropic-sans", "anthropic-sans", "Anthropic Sans — a declared mockup face (the Claude demo)."),
    ("--font-anthropic-serif", "anthropic-serif", "Anthropic Serif — a declared mockup face."),
    ("--font-app", "app", "neue-haas-unica — the go.equals.com app face (the sign-in card)."),
    ("--font-mono", "mono", "JetBrains Mono — the app's declared mono stack."),
    ("--font-paper-mono", "paper-mono", "Paper Mono — the docs code face."),
    ("--font-default", "default", "The docs' declared default stack (Inter first)."),
    ("--default-mono-font-family", "default-mono", "The docs' declared default mono stack (Paper Mono first)."),
]:
    if name in R:
        fam[key] = {"var": name, "type": "fontFamily", "description": desc}

weights = SPEC["core"].setdefault("font", {}).setdefault("weight", {})
for name, key, desc in [
    ("--font-weight-normal", "normal", "400 — body and UI text everywhere."),
    ("--font-weight-medium", "medium", "500 — the workbook mockup's cell labels, docs code."),
    ("--font-weight-semibold", "semibold", "600 — docs headings."),
    ("--font-weight-bold", "bold", "700 — declared."),
    ("--font-weight-extrabold", "extrabold", "800 — declared."),
]:
    if name in R:
        weights[key] = {"var": name, "type": "fontWeight", "description": desc}

# ------------------------------------------------------------- type ramp

size = SPEC["core"].setdefault("font", {}).setdefault("size", {})
for key, comp, state, desc in [
    ("tab", "wb-sheet-tab", "default", "The 11px workbook sheet-tab label."),
    ("app", "signin-continue", "default", "The 12px go.equals.com app text — sign-in field, submit, footer."),
    ("cell", "wb-cell", "default", "The 12px workbook cell label."),
    ("small", "mkt-nav-link", "default", "The 14px marketing UI size — nav links, eyebrow labels, buttons, plan features' chrome."),
    ("field", "hero-email", "default", "The 16px field and plan-feature text."),
    ("body", "faq-question", "default", "The 18px marketing body size (plan cards, FAQ, header text)."),
    ("docs-body", "docs-para", "default", "The 18px docs paragraph size."),
    ("lede", "hero-sub", "default", "The 24px hero lede and use-case lede."),
    ("signin-display", "signin-heading", "default", "The 30px 'Sign in to Equals' card heading — Serrif Condensed inside the app."),
    ("docs-h1", "docs-h1", "default", "The 36px docs page heading."),
    ("section", "section-h2", "default", "The 48px marketing section heading; also the mobile display size."),
    ("mobile-display", "m-hero-h1", "default", "The 48px display at 390px."),
    ("display", "hero-h1", "default", "The 110px marketing display ('What's after Excel?', 'ARR Dashboard')."),
]:
    need(comp, state, "fontSize")
    size[key] = lit(ts(comp, state, "fontSize"), "dimension",
                    f"computed fontSize of {comp} {state} (raw/components-computed.json)", desc)

lh = SPEC["core"].setdefault("font", {}).setdefault("lineHeight", {})
for name, key, desc in [
    ("--leading-tight", "tight", "1.25 — declared tight leading."),
    ("--leading-normal", "normal", "1.5 — declared normal leading."),
    ("--leading-relaxed", "relaxed", "1.625 — declared relaxed leading."),
]:
    if name in R:
        lh[key] = {"var": name, "type": "number", "description": desc}
for key, comp, desc in [
    ("display", "hero-h1", "The 110px/110px display's own leading (ratio 1)."),
    ("label", "section-label", "The eyebrow's 24px line on 14px."),
    ("body", "faq-question", "The 24px marketing body line on 18px."),
    ("lede", "hero-sub", "The 32px lede line on 24px."),
    ("docs-body", "docs-para", "The 28px docs paragraph line on 18px."),
    ("app", "signin-continue", "The app's tight 15-16px control leading."),
]:
    state = "default"
    need(comp, state, "lineHeight")
    lh[key] = lit(ts(comp, state, "lineHeight"), "dimension",
                  f"computed lineHeight of {comp} {state} (raw/components-computed.json)", desc)

tr = SPEC["core"].setdefault("font", {}).setdefault("tracking", {})
for name, key, desc in [
    ("--tracking-tighter", "tighter", "-0.05em — declared."),
    ("--tracking-tight", "tight", "-0.025em — declared."),
    ("--tracking-wide", "wide", "0.025em — declared."),
]:
    if name in R:
        tr[key] = {"var": name, "type": "other", "description": desc}
for key, comp, desc in [
    ("display", "hero-h1", "The display's -0.02em tightening (-2.2px on 110px)."),
    ("body", "mkt-nav-link", "The marketing UI's -0.005em (-0.09px on 14-18px)."),
    ("label", "section-label", "The eyebrow's +0.02em (+0.28px on 14px)."),
    ("caption", "wb-cell", "The mockup caption's +0.015em (+0.18px)."),
]:
    state = "default"
    need(comp, state, "letterSpacing")
    if ts(comp, state, "letterSpacing") != "normal":
        tr[key] = lit(ts(comp, state, "letterSpacing"), "dimension",
                      f"computed letterSpacing of {comp} {state} (raw/components-computed.json)", desc)

# ------------------------------------------------- declared layout metrics
#
# --header-height/--spacing/--radius-xl/--container-* are the few
# dimension tokens the public sheets declare; everything else measured.

dim = SPEC["core"].setdefault("size", {})
for name, key, desc in [
    ("--header-height", "header", "The declared 52px marketing header (measured 52 desktop, 53 mobile)."),
    ("--banner-height", "banner", "The declared 0px promo banner slot."),
    ("--spacing", "base", "The docs/Tailwind 4px spacing base."),
    ("--radius-xl", "radius-xl", "The declared 12px extra-large radius (docs nav items, the mega-menu, the workbook mockup)."),
]:
    if name in R:
        dim[key] = {"var": name, "type": "dimension", "description": desc}
cont = dim.setdefault("container", {})
for name in sorted(k for k in R if k.startswith("--container-")):
    cont[name[len("--container-"):]] = {"var": name, "type": "dimension",
                                        "description": f"The declared `{name}` docs container width."}

radii = SPEC["core"].setdefault("radius", {})
for key, comp, state, prop, desc in [
    ("control", "wb-toolbar-button", "default", "borderTopLeftRadius", "The 4px toolbar-button radius inside the workbook mockup."),
    ("small", "docs-code", "default", "borderTopLeftRadius", "The 6px inline-code and menu-item radius."),
    ("field", "signin-email", "default", "borderTopLeftRadius", "The 8px sign-in field and submit radius."),
    ("card", "mkt-menu", "default", "borderTopLeftRadius", "The 12px card/menu/mockup radius (matches declared --radius-xl)."),
    ("cta", "hero-cta", "default", "borderTopLeftRadius", "The 60px pill radius of the marketing CTAs."),
    ("pill", "docs-search", "default", "borderTopLeftRadius", "The 9999px fully-round radius of the docs search/assistant pills."),
]:
    radii[key] = lit(need(comp, state, prop), "dimension",
                     f"computed {prop} of {comp} {state} (raw/components-computed.json)", desc)

# ------------------------------------------------------------- elevation

sh = SPEC["core"].setdefault("shadow", {})
for key, comp, desc in [
    ("menu", "mkt-menu", "The three-layer card shadow the mega-menu carries (0.5px ring + soft drop + larger drop)."),
    ("card", "wb-mockup", "The ring + drop pair the workbook mockup carries."),
]:
    state = "default"
    if need(comp, state, "boxShadow") == "none":
        gap(f"core.shadow.{key}", f"{comp} {state} computes no box-shadow")
    else:
        sh[key] = lit(need(comp, state, "boxShadow"), "other",
                      f"computed boxShadow of {comp} {state} (raw/components-computed.json)", desc)
if need("hero-cta", "pressed", "boxShadow") == "none":
    gap("core.shadow.pressed", "hero-cta pressed computes no box-shadow")
else:
    sh["pressed"] = lit(need("hero-cta", "pressed", "boxShadow"), "other",
                        "computed boxShadow of hero-cta pressed (raw/components-computed.json)",
                        "The 1px 3px inset shadow a marketing CTA draws when active.")
if "--twoslash-popup-shadow" in R:
    sh["popup"] = {"var": "--twoslash-popup-shadow", "type": "other",
                   "description": "The docs' declared code-popup shadow."}

# ------------------------------------------------------------------ motion

mo = SPEC["core"].setdefault("motion", {})
for name, key, ty, desc in [
    ("--default-transition-duration", "duration", "duration", "The declared 150ms default transition duration."),
    ("--default-transition-timing-function", "easing", "cubicBezier", "The declared default curve (ease-in-out)."),
    ("--ease-in", "ease-in", "cubicBezier", "The declared ease-in curve."),
    ("--ease-out", "ease-out", "cubicBezier", "The declared ease-out curve."),
    ("--ease-in-out", "ease-in-out", "cubicBezier", "The declared ease-in-out curve."),
]:
    if name in R:
        mo[key] = {"var": name, "type": ty, "description": desc}
if need("hero-cta", "default", "transitionDuration") != "0s":
    mo["control"] = lit(transition(need("hero-cta", "default")), "other",
                        "computed transition of hero-cta default (raw/components-computed.json)",
                        "The marketing button's transition.")
else:
    gap("core.motion.control", "hero-cta default declares no transition")

# ------------------------------------------------------------- breakpoints
#
# The marketing sheet's media contexts (raw/css-vars.json rules) — the page
# reflows at these widths; they are declared @media conditions, so the source
# is the stylesheet, not a guess.

seen = set()
bps = SPEC["core"].setdefault("breakpoint", {})
for bin_ in ("theme", "app", "docs", "utility", "tailwind"):
    for r in V.get(bin_, []):
        for ctx in r.get("context", []):
            for m in re.finditer(r"(min|max)-width:\s*([\d.]+)px|width\s*(>=|<=)\s*([\d.]+)px", ctx or ""):
                kind = m.group(1) or {" >=": "min", " <=": "max"}.get(" " + m.group(3), m.group(3))
                kind = {"min": "min", "max": "max", ">=": "min", "<=": "max"}[kind]
                num = m.group(2) or m.group(4)
                val = num + "px"
                if val in seen:
                    continue
                seen.add(val)
                bps[f"{kind}-{num.replace('.', '-')}"] = lit(
                    val, "dimension", f"`{ctx.strip()}` in a public stylesheet (raw/css-vars.json rules)",
                    "A declared breakpoint in the public CSS.")

# ------------------------------------------- per-theme semantic variables
#
# The docs' Mintlify layer genuinely switches: --default-border-color and the
# --twoslash-* code-theme vars resolve differently under html.dark. They are
# emitted as {"var"} leaves so each set resolves its own value.

ld, dd = SPEC["light"].setdefault("docs", {}), SPEC["dark"].setdefault("docs", {})
for name, key in [("--background-light", "surface"), ("--default-border-color", "border"),
                  ("--primary", "primary")]:
    if name in R:
        ld[key] = {"var": name, "type": "color", "description": f"The declared `{name}`."}
for name, key in [("--background-dark", "surface"), ("--default-border-color", "border"),
                  ("--primary", "primary")]:
    if name in D:
        dd[key] = {"var": name, "type": "color", "description": f"The declared `{name}`."}
for name in sorted(k for k in R if k.startswith("--twoslash-")):
    key = name[len("--twoslash-"):]
    ty = "color" if COLOR_FULL.fullmatch(str(R[name]).strip()) else "other"
    ld.setdefault("twoslash", {})[key] = var(name, ty)
    dd.setdefault("twoslash", {})[key] = var(name, ty)

# --------------------------------------------- measured roles
#
# Roles measured on the real components; each aliases to the declared token
# its value matches (semcolor maps a normalized colour to its core path,
# then a few per-theme docs semantic names).

role_alias = {"light": dict(color_alias), "dark": dict(color_alias)}
for name in ("--default-border-color", "--primary"):
    role_alias["light"].setdefault(norm_color(R.get(name)), "docs.border" if "border" in name else "docs.primary")
    role_alias["dark"].setdefault(norm_color(D.get(name)), "docs.border" if "border" in name else "docs.primary")


def semcolor(raw, src, desc, theme="light"):
    v = css_color(raw)
    alias = role_alias[theme].get(v)
    value = f"{{{alias}}}" if alias else v
    return lit(value, "color", src + (f"; matches declared {alias}" if alias else ""), desc)


L = SPEC["light"]


def role(root, where, key, comp, state, prop, desc, theme):
    """One measured colour role. `prop` is a computed property, "_placeholder" (the field's
    placeholder colour), "_canvas" (the declared app background) or "ring" (the focus ring the
    state really paints). A reading that paints nothing (a transparent fill, the browser's default
    focus ring) is recorded under _gaps instead of published."""
    path = f"{theme}.{where}.{key}"
    if prop == "_canvas":
        raw = R.get("--color-background")
        if not raw:
            raise SystemExit("--color-background is not resolved in raw/css-vars.json")
        src = "css-var --color-background behind the sign-in card (raw/css-vars.json)"
    elif prop == "_placeholder":
        need(comp, state)
        try:
            raw = C[comp]["states"][state]["placeholder"]["color"]
        except (KeyError, TypeError):
            raise SystemExit(f"{comp} {state}: no placeholder colour in raw/components-computed.json")
        src = f"computed placeholder colour of {comp} {state} (raw/components-computed.json)"
    elif prop == "ring":
        sty = need(comp, state)
        ring = painted_ring(sty)
        if not ring:
            return gap(path, f"{comp} {state} paints no focus ring of its own: outline {sty.get('outlineWidth')} "
                             f"{sty.get('outlineStyle')} {css_color(sty.get('outlineColor'))} is the browser's default "
                             f"auto ring, and no box-shadow layer has a spread")
        raw, how = ring
        src = f"the {how} focus ring of {comp} {state} (raw/components-computed.json outline/boxShadow)"
    else:
        raw = need(comp, state, prop)
        if prop == "backgroundColor" and transparent(raw):
            return gap(path, f"{comp} {state} computes a transparent {prop} (rgba(0, 0, 0, 0)) and paints no fill of its own")
        src = f"computed {prop} of {comp} {state} (raw/components-computed.json)"
    if str(raw).startswith(("oklab", "oklch")):
        src += f"; the browser painted {raw}, converted here"
    root[key] = semcolor(raw, src, desc, theme)


# ---- marketing surface (light only; the page body is .accent--* themed) ----
mkt = L.setdefault("marketing", {})
for key, comp, state, prop, desc in [
    ("surface", "mkt-header", "default", "backgroundColor", "The cream #FAF9F5 marketing field."),
    ("text", "faq-question", "default", "color", "The near-black marketing ink."),
    ("muted", "hero-email", "default", "_placeholder", "The 60%-black placeholder/muted marketing text."),
    ("line", "faq", "default", "borderTopColor", "The 10%-black hairline the FAQ dividers draw."),
    ("focus", "mkt-nav-link", "focus-visible", "ring", "The keyboard-focus ring on marketing links."),
    ("card", "plan-card", "default", "backgroundColor", "The cream plan-card field (same as the page — the cards separate by layout, not colour)."),
    ("menu-surface", "mkt-menu", "default", "backgroundColor", "The white mega-menu surface."),
    ("menu-hover", "mkt-menu-item", "hover", "backgroundColor", "The 5%-black hover wash on menu items."),
]:
    role(mkt, "marketing", key, comp, state, prop, desc, "light")

# The per-page accent themes: .accent--* sets --accent-background (and the
# lighter --accent-light-background used for washes) plus --accent-color for
# text on the accent; .label--* sets --section-label-color. Resolved on a
# probe body carrying each class (raw/css-vars.json resolved.accents).
acc = mkt.setdefault("accent", {})
for cls, vals in ACC.items():
    if not cls.startswith("accent--"):
        continue
    key = cls[len("accent--"):]
    entry = {}
    if vals.get("--accent-background"):
        entry["background"] = lit(vals["--accent-background"], "color",
            f"css-var --accent-background resolved on .{cls} (raw/css-vars.json resolved.accents)",
            f"The {key} accent fill — CTAs, hero pills, section bands on .{cls} pages.")
    if vals.get("--accent-light-background") and vals["--accent-light-background"] != vals.get("--accent-background"):
        entry["light"] = lit(vals["--accent-light-background"], "color",
            f"css-var --accent-light-background resolved on .{cls} (raw/css-vars.json resolved.accents)",
            f"The lighter {key} wash behind accent-tinted areas.")
    if vals.get("--accent-color"):
        entry["on"] = lit(vals["--accent-color"], "color",
            f"css-var --accent-color resolved on .{cls} (raw/css-vars.json resolved.accents)",
            f"Text and icons painted on the {key} accent.")
    if entry:
        acc[key] = entry

lab = mkt.setdefault("label", {})
for cls, vals in ACC.items():
    if not cls.startswith("label--") or not vals.get("--section-label-color"):
        continue
    key = cls[len("label--"):]
    lab[key] = lit(vals["--section-label-color"], "color",
        f"css-var --section-label-color resolved on .{cls} (raw/css-vars.json resolved.accents)",
        f"The eyebrow-label colour on .{cls} pages.")

# The marketing CTA's hover: a darker orchid the browser computes as
# color(srgb) (a color-mix of the accent).
mkt.setdefault("action", {})["hover"] = semcolor(
    need("hero-cta", "hover", "backgroundColor"), "computed backgroundColor of hero-cta hover (raw/components-computed.json); the browser-resolved color-mix of the orchid accent",
    "The darker accent the marketing CTA lifts to on hover.", "light")

# ---- sign-in surface (light only) ----
sgn = L.setdefault("signin", {})
for key, comp, state, prop, desc in [
    ("canvas", "signin-card", "default", "_canvas", "The #fcfcfc app canvas behind the sign-in card (declared --color-background, app grey-25)."),
    ("card", "signin-card", "default", "backgroundColor", "The sign-in card's own surface (transparent on the canvas)."),
    ("heading", "signin-heading", "default", "color", "The card heading ink."),
    ("text", "signin-email", "default", "color", "The field text colour (app grey-800)."),
    ("field", "signin-email", "default", "backgroundColor", "The #f5f5f5 sign-in field fill (app grey-100)."),
    ("placeholder", "signin-email", "default", "_placeholder", "The #a3a3a3 placeholder (app grey-400)."),
    ("focus", "signin-email", "focused", "borderTopColor", "The #7c3aed border the field draws when focused (app purple-600)."),
    ("action", "signin-continue", "default", "backgroundColor", "The #7c3aed Continue submit fill (app purple-600)."),
    ("action-hover", "signin-continue", "hover", "backgroundColor", "The #6d28d9 hover (app purple-700)."),
    ("on-action", "signin-continue", "default", "color", "White text on the submit."),
    ("muted", "signin-footer", "default", "color", "The #737373 footer copy (app grey-500)."),
]:
    role(sgn, "signin", key, comp, state, prop, desc, "light")

# ---- docs measured roles, both themes ----
for root, theme, rows in [
    (ld, "light", [
        ("text", "docs-h1", "default", "color", "The docs heading ink (#1a181d, grey-900)."),
        ("body-text", "docs-para", "default", "color", "The docs paragraph colour (#424045, grey-700)."),
        ("muted", "docs-sidebar", "default", "color", "The docs rail/meta colour (#737176, grey-500)."),
        ("nav-hover", "docs-nav-item", "default", "backgroundColor", "The active nav item's primary tint (the browser paints it in oklab: ~primary at 10%)."),
        ("code-text", "docs-code", "default", "color", "The dark-navy inline-code ink (painted in oklch)."),
        ("code-bg", "docs-code", "default", "backgroundColor", "The near-white 50% code chip fill."),
        ("field", "docs-search", "default", "backgroundColor", "The 3%-ink search field wash."),
        ("focus", "docs-search", "focus-visible", "ring", "The primary outline the docs search draws on keyboard focus."),
    ]),
    (dd, "dark", [
        ("text", "d-docs-h1", "default", "color", "The docs dark heading ink (#e2e0e5, grey-200)."),
        ("body-text", "d-docs-para", "default", "color", "The docs dark paragraph colour (#a2a0a5, grey-400)."),
        ("muted", "d-docs-sidebar", "default", "color", "The docs dark rail/meta colour (#a2a0a5, grey-400)."),
        ("nav-hover", "d-docs-nav-item", "default", "backgroundColor", "The active nav item's primary tint on dark (~primary at 10%, painted in oklab)."),
        ("code-text", "d-docs-code", "default", "color", "The near-white code ink (#e2e0e5, grey-200)."),
        ("code-bg", "d-docs-code", "default", "backgroundColor", "The 5%-white code chip fill on dark."),
        ("field", "d-docs-search", "default", "backgroundColor", "The 3%-white search field wash on dark."),
        ("focus", "d-docs-search", "focus-visible", "ring", "The primary outline on dark."),
        ("line", "d-docs-sidebar", "default", "borderRightColor", "The 10%-white rail hairline on dark."),
    ]),
]:
    for key, comp, state, prop, desc in rows:
        role(root, "docs", key, comp, state, prop, desc, theme)

# ------------------------------------------------------------- components

comp = SPEC["component"]
for name, cname, state, prop, ty_, desc in [
    ("header-height", "mkt-header", "default", "h", "dimension", "The 52px marketing header (matches declared --header-height)."),
    ("mobile-header-height", "m-header", "default", "h", "dimension", "The 53px phone header."),
    ("hero-field-height", "hero-email", "default", "h", "dimension", "The 56px hero email capture."),
    ("mobile-field-height", "m-email", "default", "h", "dimension", "The 52px phone email capture."),
    ("signin-field-height", "signin-email", "default", "h", "dimension", "The 30px sign-in field."),
    ("signin-card-width", "signin-card", "default", "w", "dimension", "The 300px sign-in card."),
    ("cta-height", "hero-cta", "default", "h", "dimension", "The 44px hero CTA."),
    ("plan-cta-height", "plan-cta", "default", "h", "dimension", "The 42px plan-card action row."),
    ("app-submit-height", "signin-continue", "default", "h", "dimension", "The 27px Continue submit."),
    ("menu-width", "mkt-menu", "default", "w", "dimension", "The ~634px use-cases mega-menu."),
    ("nav-item-height", "docs-nav-item", "default", "h", "dimension", "The 32px docs nav item."),
    ("search-height", "docs-search", "default", "h", "dimension", "The 36px docs search pill."),
    ("theme-button", "docs-theme-btn", "default", "h", "dimension", "The 30px docs theme button."),
    ("docs-sidebar-width", "docs-sidebar", "default", "w", "dimension", "The 288px docs rail."),
    ("plan-card-width", "plan-card", "default", "w", "dimension", "The ~421px plan card."),
    ("workbook-mockup", "wb-mockup", "default", "w", "dimension", "The 980x640 workbook mockup frame."),
    ("sheet-tab-height", "wb-sheet-tab", "default", "h", "dimension", "The 32px mockup sheet tab."),
    ("hamburger", "m-hamburger", "default", "h", "dimension", "The 40px phone hamburger hit area."),
]:
    need(cname, state)
    v = rc(cname, state, prop)
    comp[name] = lit(("%g" % v) + "px" if isinstance(v, (int, float)) else str(v) + "px",
                     ty_, f"measured {prop} of {cname} {state} (raw/components-computed.json)", desc)

(RAW / "component-tokens.json").write_text(json.dumps(SPEC, indent=2, ensure_ascii=False) + "\n")
print("component-tokens.json:", {k: len(v) for k, v in SPEC.items() if k != "_about"})
for g in SPEC["_gaps"]:
    print("  gap:", g["token"], "-", g["why"])
