#!/usr/bin/env python3
"""Write raw/component-tokens.json, the token spec build_tokens.py reads.

Epic's public surfaces signed out paint one theme: the dark EGS v2 store
(store.epicgames.com — Discover, Browse, product pages, Free Games, News,
Download), the Epic account sign-in dialog on www.epicgames.com/id, the
OpenSans marketing home and the support centre. The store's stylesheet
declares a real design-token layer — Epic's EDS system (raw/css-vars.json):
~130 --color-palette-* hue ramps, a semantic --color-* layer (background,
foreground, border, neutral, transparent) plus --size-dimension-*/
--size-borderRadius-*/--size-borderWidth-*/--size-font-*/--size-lineHeight-*/
--size-letterSpacing-* scales, --typography-heading|text|ui-* roles,
--font-family-*/--font-weight-*, --animation-* durations and easings,
--opacity-*, --shadow-*, --effect-*, --gradient-*/--gradientComponents-* and
the component-geometry groups (--action-*, --control-*, --input-*,
--navigation-*, --selection-*, --status-*, --table-*, --feedback-*,
--identity-*, --egs-*). A second layer of hashed --eds_370_* variables is
emitted by the same bundle but resolves only through component classes; the
semantic names on :root are the readable layer and the ones exported here.

Theme-invariant scales land under core.*; the --color-* semantic layer and
every measured role land under dark.* (the only painted theme). Measured
roles alias to the declared values they match.

Measured computed styles from raw/components-computed.json:

  dark        #101014 canvas, #18181c footer and elevated-low, #202024 fields
              and elevated-medium, #fff strong-fill CTAs with near-black ink,
              the #26bbff brand blue on the nav Download and sign-in Continue,
              rgba(255,255,255,.95) primary and .65 secondary text,
              #ffffff26 subtle borders, the white focus ring
  fonts       Inter (every control and body), Inter Tight (display headings),
              OpenSans (www marketing), Recursive Mono (declared code face)
  ramp        measured 12/13.33/14/16/20/24/32/40/52/64px steps
  shape       4px badges, 6px nav buttons, 8px cards, 10px CTAs/wishlist,
              24px help tiles, 9999px pills (search field, pager)
  motion      the measured 0.2s transitions match the declared durations
"""

import json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
V = json.loads((RAW / "css-vars.json").read_text())
RD = V.get("resolved", {}).get("dark", {})
C = json.loads((RAW / "components-computed.json").read_text())["components"]
D = {n: (v.get("value", v.get("raw")) if isinstance(v, dict) else v) for n, v in RD.items()}
KIND = {n: (v.get("kind") if isinstance(v, dict) else None) for n, v in RD.items()}


def var(name, ty="color", **kw):
    d = {"var": name, "type": ty}
    d.update(kw)
    return d


SPEC = {"_about": (
    "The token tree build_tokens.py turns into tokens.json. store.epicgames.com "
    "declares its EDS design-token layer in the egs-v2 stylesheet "
    "(raw/css-vars.json): theme-invariant scales under core.* and the semantic "
    "--color-* layer under dark.*, the only painted theme signed out. Measured "
    "roles alias to the declared values where they match."),
    "core": {}, "dark": {}, "component": {}}


# A named row whose reading is missing is recorded here instead of being
# dropped silently; the build stops on any gap not listed in KNOWN_GAPS (at the
# end), and listed ones are written to raw/component-tokens.json `_gaps`.
GAPS = []


def gap(what):
    GAPS.append(what)


def split_shadow(v):
    """Top-level comma split of a computed box-shadow list."""
    return [x.strip() for x in re.split(r",\s*(?![^()]*\))", v or "") if x.strip()]


def painted_ring(sty):
    """(colour, how) of the focus ring a state really paints: a drawn outline
    (style not none or auto, width above 0), else the outermost visible
    box-shadow layer with a spread. An outline colour under outline-style none
    is the inactive default, not a ring, so it is never returned."""
    if sty.get("outlineStyle", "none") not in ("none", "auto") and float(sty.get("outlineWidth", "0px")[:-2] or 0) > 0 \
            and sty.get("outlineColor") != "rgba(0, 0, 0, 0)":
        return sty["outlineColor"], f"outline {sty['outlineWidth']} {sty['outlineStyle']}"
    ring = None
    for layer in split_shadow(sty.get("boxShadow", "none")):
        m = re.match(r"^(rgba?\([^)]*\))\s+(-?[\d.]+)px\s+(-?[\d.]+)px\s+(-?[\d.]+)px\s+(-?[\d.]+)px(\s+inset)?$", layer)
        if not m or m.group(6) or float(m.group(5)) <= 0 or re.fullmatch(r"rgba\(\s*\d+,\s*\d+,\s*\d+,\s*0\s*\)", m.group(1)):
            continue
        ring = (m.group(1), f"box-shadow {m.group(5)}px spread")
    if ring:
        return ring
    raise KeyError("no painted ring")


def _list(v):
    """A computed comma list, split only at commas outside parentheses."""
    return [x.strip() for x in re.split(r",(?![^()]*\))", v or "") if x.strip()]


def transition(s):
    """The computed transition lists as one valid shorthand: CSS repeats the
    duration/easing/delay lists to the length of transition-property, so each
    property is paired with its own entry by index. A 0s entry is kept (it
    can override an earlier `all`); only a list that is 0s throughout means
    no transition."""
    props = _list(s.get("transitionProperty") or "all")
    durs = _list(s.get("transitionDuration") or "0s")
    eases = _list(s.get("transitionTimingFunction") or "ease")
    delays = _list(s.get("transitionDelay") or "0s")
    if all(d in ("0s", "0ms") for d in durs):
        return ""
    parts = []
    for i, p in enumerate(props):
        d, e, dl = durs[i % len(durs)], eases[i % len(eases)], delays[i % len(delays)]
        parts.append(" ".join([p, d, e] + ([dl] if dl not in ("0s", "0ms") else [])))
    return ", ".join(parts)


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
        if len(h) == 8:
            a = round(int(h[6:8], 16) / 255, 2)
            return "#" + h[:6] if a >= 1 else f"rgba({int(h[0:2], 16)}, {int(h[2:4], 16)}, {int(h[4:6], 16)}, {'%g' % a})"
        return "#" + h[:6]
    m = re.fullmatch(r"rgba?\(\s*([\d.]+)[,\s]+([\d.]+)[,\s]+([\d.]+)(?:[,\s/]+([\d.]+%?))?\s*\)", v)
    if m:
        r, g, b, a = m.groups()
        if a is None or float(str(a).rstrip("%")) >= (100 if str(a).endswith("%") else 1):
            return "#%02x%02x%02x" % (int(float(r)), int(float(g)), int(float(b)))
        a = float(a[:-1]) / 100 if str(a).endswith("%") else float(a)
        return f"rgba({int(float(r))}, {int(float(g))}, {int(float(b))}, {'%g' % round(a, 2)})"
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


def emit(root, name, leaf):
    """Write `leaf` at name's dotted path.

    A declared name can be both a leaf and the parent of other names
    (`--color-background-default` vs `--color-background-default-*`). When a
    leaf and a group must share a node, the leaf moves inside the group under
    the first free of `default`, `base`, `self`.
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


def emitted_path(name):
    return EMITTED[name]


def painted(comp, state, want=None):
    """First painted fill on or under the component (optionally one matching `want`)."""
    try:
        c = C[comp]["states"][state]
    except KeyError:
        return None
    for n in c.get("paint") or []:
        if n.get("bg") and (want is None or want(n["bg"])):
            return n["bg"]
    for n in c.get("ancestors") or []:
        if n.get("bg") and (want is None or want(n["bg"])):
            return n["bg"]
    return None


DECL_SRC = "declared EDS design-system variable in the egs-v2 stylesheet (raw/css-vars.json)"

COLOR_V = re.compile(r"(#[0-9a-fA-F]{3,8}|rgba?\([^)]*\)|hsla?\([^)]*\)|(ok)?lab\([^)]*\)|(ok)?lch\([^)]*\)|color-mix\([^)]*\))")


def decl(name, ty=None):
    """A declared variable as a leaf, typed from the resolver's kind."""
    v = D[name]
    if ty is None:
        ty = {"color": "color", "dimension": "dimension", "number": "number",
              "duration": "duration", "easing": "cubicBezier",
              "fontFamily": "fontFamily"}.get(KIND.get(name), "other")
    if ty == "dimension" and not re.fullmatch(r"-?\d+(\.\d+)?(px|rem)", str(v).strip()):
        ty = "other"
    if ty == "color" and not COLOR_V.fullmatch(str(v).strip()):
        ty = "other"
    return lit(v, ty, f"{DECL_SRC}: {name}", f"The declared `{name}`.")


# ------------------------------------------------------------------- fonts
#
# The store loads Inter (300/400/500/700) for every control and Inter Tight
# (700/900) for display headings; --font-family-base and --font-family-code are
# declared. The www marketing home paints OpenSans and the support centre the
# same Inter layer.

fam = SPEC["core"].setdefault("font", {}).setdefault("family", {})
for key, comp, state, desc in [
    ("display", "p-title", "default", "The display family the product page title paints (Inter Tight)."),
    ("marketing", "w-tile", "default", "The marketing surface's family (OpenSans on www.epicgames.com)."),
    ("help", "h-h1", "default", "The support centre's heading family."),
]:
    if have(comp, state, "fontFamily"):
        v = ts(comp, state, "fontFamily")
        fam[key] = {"value": v, "type": "fontFamily",
                    "source": f"computed fontFamily of {comp} {state} (raw/components-computed.json)",
                    "description": desc}
    else:
        gap(f"font.family.{key}: no {comp} {state} fontFamily reading")

weights = SPEC["core"].setdefault("font", {}).setdefault("weight", {})
for key, comp, desc in [
    ("measured-regular", "card-price", "The card price weight (prices and meta text)."),
    ("measured-medium", "hero-cta", "500 — CTA labels and nav actions."),
    ("measured-display", "p-title", "The product page display weight."),
]:
    try:
        w = int(float(ts(comp, "default", "fontWeight")))
        weights[key] = lit(w, "fontWeight",
                           f"computed fontWeight of {comp} default (raw/components-computed.json)", desc)
    except (KeyError, TypeError, ValueError):
        gap(f"font.weight.{key}: no {comp} default fontWeight reading")

# ------------------------------------------------- declared scales (EDS)
#
# The EDS layer declares the design system outright on :root
# (raw/css-vars.json): --color-palette-* hue ramps, --size-* scales,
# --typography-* roles, --font-*, --animation-*, --opacity-*, --shadow-*,
# --effect-*, --gradient-*/--gradientComponents-* and the component-geometry
# groups. All of it is declared once and is theme-invariant -> core.*. The
# --color-* semantic layer (background, foreground, border, neutral,
# transparent) is emitted under dark.* below.

color_alias = {}   # normalized colour -> token path for aliasing
CORE_PREFIXES = (
    "--gradient-", "--gradientComponents-", "--size-", "--typography-", "--font-",
    "--animation-", "--opacity-", "--shadow-", "--effect-",
    "--action-", "--control-", "--input-", "--navigation-", "--selection-",
    "--status-", "--table-", "--feedback-", "--identity-", "--egs-",
)
for name in sorted(D):
    if name.startswith("--color-palette-"):
        leaf = decl(name)
        emit(SPEC["core"], name, leaf)
        if leaf["type"] == "color":
            color_alias.setdefault(norm_color(D[name]), EMITTED[name])
    elif any(name.startswith(p) for p in CORE_PREFIXES):
        emit(SPEC["core"], name, decl(name))

# ------------------------------------------------- dark semantic variables
#
# Every non-palette --color-* name is the EDS semantic layer: background,
# foreground, border, neutral and transparent roles. The store paints only
# dark signed out, so they land under dark.* resolved in the dark probe.

for name in sorted(k for k in D if k.startswith("--color-") and not k.startswith("--color-palette-")):
    leaf = decl(name)
    emit(SPEC["dark"], name, leaf)
    if leaf["type"] == "color":
        color_alias.setdefault(norm_color(D[name]), EMITTED[name])

# --------------------------------------------- measured roles (dark set)
#
# Roles measured on the painted surfaces; each aliases to the declared token
# its value matches, else stays a measured literal.

role_alias = dict(color_alias)


def semcolor(raw, src, desc):
    alias = role_alias.get(norm_color(raw))
    value = f"{{{alias}}}" if alias else norm_color(raw)
    return lit(value, "color", src + (f"; matches declared {alias}" if alias else ""), desc)


dsem = SPEC["dark"]
for key, comp, state, prop, group, desc in [
    ("canvas", "store-tabs", "default", "backgroundColor", "background",
     "The #101014 store canvas under every store page."),
    ("footer", "egs-footer", "default", "backgroundColor", "background",
     "The #18181c footer field (elevated-low)."),
    ("field", "search-field", "default", "backgroundColor", "background",
     "The #202024 input field (elevated-medium)."),
    ("hero-art", "hero-slide", "default", "_paint-hero", "background",
     "The hero slide's painted art layer."),
    ("dialog", "s-dialog", "default", "_paint-dialog", "background",
     "The sign-in dialog card."),
    ("primary", "egs-nav", "default", "color", "text",
     "The white-95% primary text and nav ink."),
    ("secondary", "card-price", "default", "color", "text",
     "The card price and meta text ink (it paints the same value as the primary ink)."),
    ("inverse", "hero-cta", "default", "color", "text",
     "The near-black ink on white strong-fill CTAs."),
    ("heading", "b-h1", "default", "color", "text",
     "The browse page heading ink."),
    ("accent-brand", "nav-download", "default", "backgroundColor", "action",
     "The #26bbff brand blue on the nav Download button — painted, not declared in the readable EDS layer."),
    ("accent-brand-hover", "nav-download", "hover", "backgroundColor", "action",
     "The lighter brand blue the nav Download lifts to on hover."),
    ("accent-eds", "s-continue", "default", "backgroundColor", "action",
     "The EDS accent fill on the sign-in Continue and free-games CTA."),
    ("accent-eds-hover", "s-continue", "hover", "backgroundColor", "action",
     "The lighter fill the EDS accent lifts to on hover."),
    ("fill-subtle", "nav-signin", "default", "backgroundColor", "action",
     "The white-15% subtle fill on the Sign in ghost button and pager buttons."),
    ("fill-subtle-hover", "nav-signin", "hover", "backgroundColor", "action",
     "The hover lift of the subtle fill."),
    ("fill-strong", "hero-cta", "default", "backgroundColor", "action",
     "The #fff strong fill of the hero CTA and View More buttons."),
    ("focus", "store-tab", "focus-visible", "_focus", "border",
     "The white focus ring drawn on keyboard focus."),
    ("price", "card-price", "default", "color", "text",
     "The card price/muted text value."),
    ("free-badge", "fg-badge", "default", "_paint-free", "background",
     "The 'Free Now' badge fill on free-games cards."),
    ("tile", "h-tile", "default", "backgroundColor", "background",
     "The support-centre category tile fill."),
    ("marketing-ink", "w-tile", "default", "color", "text",
     "The www marketing tile's ink."),
]:
    try:
        if prop == "_paint-hero":
            raw = painted(comp, state, lambda bg: bg not in ("rgba(0, 0, 0, 0)", "none"))
            src = f"painted art layer of {comp} {state} (raw/components-computed.json)"
        elif prop == "_paint-dialog":
            raw = st(comp, state)["backgroundColor"]
            if norm_color(raw) in ("rgba(0, 0, 0, 0)", "#000000"):
                raw = painted(comp, state, lambda bg: bg not in ("rgba(0, 0, 0, 0)", "none"))
            src = f"computed/painted background of {comp} {state} (raw/components-computed.json)"
        elif prop == "_paint-free":
            raw = st(comp, state)["backgroundColor"]
            if not raw or raw == "rgba(0, 0, 0, 0)":
                raw = painted(comp, state, lambda bg: bg not in ("rgba(0, 0, 0, 0)", "none"))
            src = f"painted badge fill of {comp} {state} (raw/components-computed.json)"
        elif prop == "_focus":
            if C[comp]["states"][state].get("via") == "focus failed":
                raise KeyError("focus failed")
            raw, how = painted_ring(st(comp, state))
            src = f"computed focus ring ({how}) of {comp} {state} (raw/components-computed.json)"
        else:
            raw = st(comp, state)[prop]
            src = f"computed {prop} of {comp} {state} (raw/components-computed.json)"
        if not raw or raw == "rgba(0, 0, 0, 0)":
            gap(f"{group}.{key}: {comp} {state} {prop} paints nothing")
            continue
        dsem.setdefault(group, {})[key] = semcolor(raw, src, desc)
    except (KeyError, StopIteration):
        gap(f"{group}.{key}: no {comp} {state} {prop} reading")

# ------------------------------------------------------------- type ramp

size_alias = {}  # 'NNpx' -> (token path, var name)
for n, v in D.items():
    if re.match(r"--(size-font-|typography-(heading|text|ui|code)-size-)", n) and re.fullmatch(r"\d+(\.\d+)?px", str(v)):
        size_alias.setdefault(v, (EMITTED[n], n))

ty = SPEC["core"].setdefault("font", {}).setdefault("size", {})
for key, comp, state, desc in [
    ("meta", "card-price", "default", "The 12px card price and meta size."),
    ("ui", "hero-cta", "default", "The 14px CTA and button label size."),
    ("body", "egs-nav", "default", "The 16px nav/body size."),
    ("title", "p-title", "default", "The product page display size."),
    ("browse-h1", "b-h1", "default", "The 'Popular Genres' heading size."),
    ("help-h1", "h-h1", "default", "The support-centre display size."),
    ("signin", "s-title", "default", "The sign-in dialog title size."),
]:
    try:
        raw = st(comp, state)["fontSize"]
        src = f"computed fontSize of {comp} {state} (raw/components-computed.json)"
        alias = size_alias.get(raw)
        ty[key] = lit(f"{{{alias[0]}}}" if alias else raw, "dimension",
                      src + (f"; matches declared {alias[1]}" if alias else ""), desc)
    except KeyError:
        gap(f"font.size.{key}: no {comp} {state} fontSize reading")

# ------------------------------------------------------------------ shape

radii = SPEC["core"].setdefault("radius", {})
radius_alias = {str(D[n]): EMITTED[n] for n in D if n.startswith("--size-borderRadius-")}
for key, comp, state, desc in [
    ("badge", "fg-badge", "default", "The small badge radius."),
    ("nav-button", "nav-signin", "default", "The 6px nav button radius."),
    ("card", "game-card", "default", "The 8px card radius."),
    ("cta", "hero-cta", "default", "The 10px CTA/wishlist radius."),
    ("tile", "h-tile", "default", "The support-tile radius."),
    ("dialog", "s-dialog", "default", "The sign-in dialog radius."),
    ("pill", "search-field", "default", "The 9999px pill — the search field and round pager buttons."),
]:
    try:
        v = st(comp, state)["borderTopLeftRadius"]
        src = f"computed borderTopLeftRadius of {comp} {state} (raw/components-computed.json)"
        dkey = radius_alias.get(v)
        radii[key] = lit(f"{{{dkey}}}" if dkey else v, "dimension",
                         src + (f"; matches declared {dkey}" if dkey else ""), desc)
    except KeyError:
        gap(f"radius.{key}: no {comp} {state} borderTopLeftRadius reading")

# ------------------------------------------------------------- elevation

sh = SPEC["core"].setdefault("shadow", {})
for key, comp, state, desc in [
    ("dialog", "s-dialog", "default", "The sign-in modal's computed box-shadow (none on this capture)."),
    ("drawer", "mobile-discover-dark-drawer", "default", "The mobile drawer shadow."),
]:
    try:
        sh[key] = lit(st(comp, state)["boxShadow"], "other",
                      f"computed boxShadow of {comp} {state} (raw/components-computed.json)", desc)
    except KeyError:
        gap(f"shadow.{key}: no {comp} {state} boxShadow reading")

# ------------------------------------------------------------------ motion

mo = SPEC["core"].setdefault("motion", {})
for key, comp, state, desc in [
    ("control", "nav-signin", "default", "The control transition on nav buttons and CTAs."),
    ("card", "game-card", "default", "The card hover transition."),
]:
    try:
        v = transition(st(comp, state))
        if v:
            mo[key] = lit(v, "other",
                          f"computed transition of {comp} {state} (raw/components-computed.json)", desc)
        else:
            gap(f"motion.{key}: {comp} {state} has no transition")
    except KeyError:
        gap(f"motion.{key}: no {comp} {state} reading")

# ------------------------------------------------------------- components

comp = SPEC["component"]
for name, cname, state, prop, ty_, desc in [
    ("nav-height", "egs-nav", "default", "h", "dimension", "The 72px store nav rail."),
    ("tabbar-height", "store-tabs", "default", "h", "dimension", "The ~100px store tab bar under the nav."),
    ("hero-height", "hero-slide", "default", "h", "dimension", "The hero slide height on Discover."),
    ("hero-width", "hero-slide", "default", "w", "dimension", "The hero slide width on Discover."),
    ("card-height", "game-card", "default", "h", "dimension", "The 100px shelf game-card height."),
    ("search-width", "search-field", "default", "w", "dimension", "The 230px store search field."),
    ("search-height", "search-field", "default", "h", "dimension", "The 40px store search field height."),
    ("pager", "pager-next", "default", "h", "dimension", "The 30px round carousel pager."),
    ("carousel-thumb", "carousel-thumb", "default", "w", "dimension", "The 180px hero carousel thumbnail."),
    ("dialog-width", "s-dialog", "default", "w", "dimension", "The sign-in dialog card width."),
    ("filter-rail", "b-filters", "default", "w", "dimension", "The browse filters rail width."),
    ("mobile-nav-height", "m-egs-nav", "default", "h", "dimension", "The mobile nav rail height."),
]:
    try:
        v = rc(cname, state, prop)
        comp[name] = lit(("%g" % v) + "px" if isinstance(v, (int, float)) else str(v) + "px",
                         ty_, f"measured {prop} of {cname} {state} (raw/components-computed.json)", desc)
    except KeyError:
        gap(f"component.{name}: no {cname} {state} {prop} reading")

# Rows missing from the committed readings, kept visible in `_gaps` (they
# were dropped silently before 2026-11): the badge and the support tile paint
# no fill of their own, no drawer component was measured, and the game card's
# computed transition is 0s.
KNOWN_GAPS = {
    "background.free-badge: fg-badge default _paint-free paints nothing",
    "background.tile: h-tile default backgroundColor paints nothing",
    "shadow.drawer: no mobile-discover-dark-drawer default boxShadow reading",
    "motion.card: game-card default has no transition",
}
_new = [g for g in GAPS if g not in KNOWN_GAPS]
if _new:
    raise SystemExit("missing readings for named token rows (recapture, or list them in KNOWN_GAPS):\n  " + "\n  ".join(_new))
if GAPS:
    SPEC["_gaps"] = GAPS

(RAW / "component-tokens.json").write_text(json.dumps(SPEC, indent=2, ensure_ascii=False) + "\n")
print("component-tokens.json:", {k: len(v) for k, v in SPEC.items() if k != "_about"})
