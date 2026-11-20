#!/usr/bin/env python3
"""Write raw/component-tokens.json, the token spec build_tokens.py reads.

deezer.com is two surfaces signed out: a marketing site (the light hero on
/en/ over a dark top bar, dark offers/features/download pages) and the dark
Chakra-UI web app that serves the public catalog pages (/en/artist/*,
/en/album/*, /en/playlist/*) plus the dark account.deezer.com forms. The
site declares a real design-token layer — Deezer's Tempo system
(raw/css-vars.json): ~950 --tempo-colors-* entries (per-theme palette
scales AND semantic background-/icon-/text-/border- roles), --tempo-space-/
--tempo-sizes-/ --tempo-radii-/ --tempo-shadows-/ --tempo-transition-/
--tempo-letterSpacings-/ --tempo-lineHeights-/ --tempo-fonts-/
--tempo-fontWeights-/ --tempo-breakpoints- scales, a --color-*/--background-*/
--text-*/--divider-* marketing semantic layer, the --font-deezer/--font-default
stacks and --ease-* curves. Declared scales land under core.*; every
theme-switching semantic variable is emitted under both light.* and dark.*
as a {"var": ...} leaf so each theme resolves its own value.

Measured computed styles from raw/components-computed.json:

  light       #0f0d13 ink on the white hero (Deezer Brand 140px/800 display),
              #fdfcfe header text and plan-card fill, the #a238ff light accent
              on Try-for-free/Sign-up CTAs, #121216 dark button fill
  dark        #0f0d13 canvas, #141216 sidebar and popover surface, #242326
              fields, #fdfcfe text, the #ad47ff dark accent with #bb73ff
              hover, #a19fa4 muted, #38373b dividers, the #ead1ff signup
              banner, the 2px #ad47ff focus border on fields
  fonts       Deezer Brand (marketing display), Deezer Product (marketing
              headings/mobile), Deezer Headline VF (app headings), Inter (UI)
  ramp        measured 140/78/56/40/35/24/20/16/15/13px steps
  shape       4px plan cards, 8px promo card, 12px small pills, 16px
              CTAs/search/mix, 24px popover, 256px-pill toggles and round
              play buttons
  motion      the measured 0.2s background/border transitions match the
              declared --tempo-transition-duration-normal (200ms)
"""

import json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
V = json.loads((RAW / "css-vars.json").read_text())
RL = V.get("resolved", {}).get("light", {})
RD = V.get("resolved", {}).get("dark", {})
C = json.loads((RAW / "components-computed.json").read_text())["components"]
R = {n: (v.get("value", v.get("raw")) if isinstance(v, dict) else v) for n, v in RL.items()}
D = {n: (v.get("value", v.get("raw")) if isinstance(v, dict) else v) for n, v in RD.items()}


def var(name, ty="color", **kw):
    d = {"var": name, "type": ty}
    d.update(kw)
    return d


SPEC = {"_about": (
    "The token tree build_tokens.py turns into tokens.json. deezer.com "
    "declares its Tempo design-token layer in its stylesheets "
    "(raw/css-vars.json): theme-invariant scales under core.* and a "
    "semantic --tempo-colors-*/--color-*/--background-*/--text-*/--divider-* "
    "layer emitted under both light.* and dark.* so each theme resolves "
    "its own value. Measured roles alias to the declared values where "
    "they match."),
    "core": {}, "light": {}, "dark": {}, "component": {}}


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


EMITTED = {}   # variable name -> dotted token path it was actually written to
_OWNER = {}    # dotted token path -> variable name holding it


def _leaf(d):
    return isinstance(d, dict) and ("var" in d or "value" in d)


def emit(root, name, leaf):
    """Write `leaf` at name's dotted path.

    A declared name can be both a leaf and the parent of other names
    (`--color-accent` vs `--color-accent-light`; `--color-border-neutral-primary`
    vs the Tempo `--tempo-colors-border-neutral-primary-default` that maps onto
    the same path). When a leaf and a group must share a node, the leaf moves
    inside the group under the first free of `default`, `base`, `self` — never
    silently overwriting tokens that resolve to different states.
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


DECL_SRC = "declared Tempo design-system variable in the site stylesheet (raw/css-vars.json)"


def decl(name, ty="dimension"):
    v = R[name]
    if ty == "dimension" and not re.fullmatch(r"-?\d+(\.\d+)?(px|rem)", str(v).strip()):
        ty = "other"
    return lit(v, ty, f"{DECL_SRC}: {name}", f"The declared `{name}`.")


COLOR_V = re.compile(r"(#[0-9a-fA-F]{3,8}|rgba?\([^)]*\)|hsla?\([^)]*\)|(ok)?lab\([^)]*\)|(ok)?lch\([^)]*\)|color-mix\([^)]*\))")


def decl_color(name):
    v = R[name]
    ty = "color" if COLOR_V.fullmatch(str(v).strip()) else "other"
    return lit(v, ty, f"{DECL_SRC}: {name}", f"The declared `{name}`.")


def decl_any(name, bag, ty="dimension", key=None):
    bag[key if key is not None else name.split("-")[-1]] = decl(name, ty)


# ------------------------------------------------------------------- fonts
#
# deezer loads four families: Inter for every UI control, Deezer Product for
# marketing headings and the mobile product surface, Deezer Brand for the
# condensed marketing display, and Deezer Headline VF for app page headings.

fam = SPEC["core"].setdefault("font", {}).setdefault("family", {})
if "--font-default" in R:
    fam["ui"] = {"var": "--font-default", "type": "fontFamily",
                 "description": "The declared Inter stack — every UI control, body and meta text."}
if "--font-deezer" in R:
    fam["product"] = {"var": "--font-deezer", "type": "fontFamily",
                      "description": "The declared Deezer Product stack — marketing headings, plan cards, the mobile surface."}
for key, comp, state, desc in [
    ("brand", "hero-h1", "default", "Deezer Brand — the condensed marketing display (hero 140px, section 56px, hero-sub 35px)."),
    ("headline", "artist-name", "default", "Deezer Headline VF — app page headings (artist/album 56px at wght 640)."),
]:
    if have(comp, state, "fontFamily"):
        v = ts(comp, state, "fontFamily")
        fam[key] = {"value": v, "type": "fontFamily",
                    "source": f"computed fontFamily of {comp} {state} (raw/components-computed.json)",
                    "description": desc}

weights = SPEC["core"].setdefault("font", {}).setdefault("weight", {})
for key, comp, desc in [
    ("regular", "track-row", "400 — app body and track text."),
    ("book", "a-search", "450 — the app search field's text weight."),
    ("medium", "a-signup", "550 — the app pill buttons and Mix."),
    ("semibold", "tab-item", "600 — the selected catalog tab."),
    ("demi", "artist-name", "640 — the app display headings (Deezer Headline VF)."),
    ("bold", "offers-h1", "700 — marketing headings, nav links, CTAs."),
    ("extrabold", "hero-h1", "800 — the marketing display size."),
]:
    try:
        w = int(float(ts(comp, "default", "fontWeight")))
        weights[key] = lit(w, "fontWeight",
                           f"computed fontWeight of {comp} default (raw/components-computed.json)", desc)
    except (KeyError, TypeError, ValueError):
        pass

# ------------------------------------------------- declared scales (Tempo)
#
# The Tempo layer declares the design system outright (raw/css-vars.json):
# palette scales and semantic colour roles under --tempo-colors-*, spacing,
# sizes, radii, shadows, transitions, letter spacings, line heights, font
# families and weights, breakpoints, borders, blurs and z-indices. The
# numeric-stepped palette scales are theme-invariant and go to core.*; every
# semantic name is emitted per-theme below.

color_alias = {}   # normalized colour -> 'color.<path>' for aliasing
colors = SPEC["core"].setdefault("color", {})
semantic_names = []
for name in sorted(k for k in R if k.startswith("--tempo-colors-")):
    rest = name[len("--tempo-colors-"):]
    if re.search(r"-\d+$", rest):
        # palette scale: <palette>-<step>; kept under color.tempo so it never
        # collides with the marketing layer's own --color-* names
        group, key = rest.rsplit("-", 1)
        colors.setdefault("tempo", {}).setdefault(group, {})[key] = decl_color(name)
        if colors["tempo"][group][key]["type"] == "color":
            color_alias.setdefault(norm_color(R[name]), f"color.tempo.{group}.{key}")
    else:
        semantic_names.append(name)

for name in sorted(k for k in R if k.startswith("--tempo-space-")):
    SPEC["core"].setdefault("spacing", {})[name[len("--tempo-space-"):]] = decl(name)

sizes = SPEC["core"].setdefault("size", {})
for name in sorted(k for k in R if k.startswith("--tempo-sizes-")):
    rest = name[len("--tempo-sizes-"):]
    if rest.startswith("container-"):
        sizes.setdefault("container", {})[rest[len("container-"):]] = decl(name)
    else:
        sizes[rest] = decl(name)

for name in sorted(k for k in R if k.startswith("--tempo-radii-")):
    SPEC["core"].setdefault("radius", {})[name[len("--tempo-radii-"):]] = decl(name)

for name in sorted(k for k in R if k.startswith("--tempo-shadows-")):
    SPEC["core"].setdefault("shadow", {})[name[len("--tempo-shadows-"):]] = decl(name, "other")

for name in sorted(k for k in R if k.startswith("--tempo-transition-duration-")):
    SPEC["core"].setdefault("duration", {})[name[len("--tempo-transition-duration-"):]] = decl(name, "other")
for name in sorted(k for k in R if re.match(r"--tempo-transition-(property|timing)", k)):
    SPEC["core"].setdefault("motion", {})[name[len("--tempo-transition-"):]] = decl(name, "other")

for name in sorted(k for k in R if k.startswith("--tempo-letterSpacings-")):
    SPEC["core"].setdefault("font", {}).setdefault("tracking", {})[name[len("--tempo-letterSpacings-"):]] = decl(name, "other")

for name in sorted(k for k in R if k.startswith("--tempo-lineHeights-")):
    SPEC["core"].setdefault("font", {}).setdefault("lineHeight", {})[name[len("--tempo-lineHeights-"):]] = decl(name)

size_alias = {}   # 'NNpx' -> ('font.size.<path>', '--var') for aliasing + evidence
for name in sorted(k for k in R if k.startswith("--tempo-font-size-")):
    key = name[len("--tempo-font-size-"):]
    SPEC["core"].setdefault("font", {}).setdefault("size", {}).setdefault("tempo", {})[key] = decl(name)
    size_alias.setdefault(R[name], (f"font.size.tempo.{key}", name))

for name in sorted(k for k in R if k.startswith("--tempo-fonts-")):
    SPEC["core"].setdefault("font", {}).setdefault("family", {}).setdefault("declared", {})[name[len("--tempo-fonts-"):]] = decl(name, "fontFamily")

for name in sorted(k for k in R if k.startswith("--tempo-fontWeights-")):
    SPEC["core"].setdefault("font", {}).setdefault("weight", {}).setdefault("declared", {})[name[len("--tempo-fontWeights-"):]] = decl(name, "other")

for name in sorted(k for k in R if k.startswith("--tempo-breakpoints-")):
    SPEC["core"].setdefault("breakpoint", {})[name[len("--tempo-breakpoints-"):]] = decl(name)

for name in sorted(k for k in R if k.startswith("--tempo-borders-")):
    SPEC["core"].setdefault("border", {})[name[len("--tempo-borders-"):]] = decl(name, "other")

for name in sorted(k for k in R if k.startswith("--tempo-blur-")):
    SPEC["core"].setdefault("blur", {})[name[len("--tempo-blur-"):]] = decl(name, "other")

for name in sorted(k for k in R if re.match(r"--tempo-z", k)):
    SPEC["core"].setdefault("zIndex", {})[name.split("-")[-1]] = decl(name, "other")

# the marketing layer's own declared names
for name in sorted(k for k in R if re.match(r"--font-size-", k)):
    key = name[len("--font-size-"):]
    SPEC["core"].setdefault("font", {}).setdefault("size", {}).setdefault("marketing", {})[key] = decl(name)

easing = SPEC["core"].setdefault("easing", {})
for name in sorted(k for k in R if k.startswith("--ease-")):
    easing[name[len("--ease-"):]] = decl(name, "cubicBezier")

# ------------------------------------------- per-theme semantic variables
#
# The semantic layer switches value between the light (data-theme="light",
# the marketing site) and dark (chakra-ui-dark/[data-theme="dark"], the app
# and offers band) resolutions — every such name is emitted under both sets
# so each theme resolves its own value.

SEMANTIC = re.compile(r"^--(color-|background-|text-|divider-|layout-|popper-|thumbnail-|control-bar-|transparent)")

# A renamed Tempo semantic can share its path with a real --color-* variable
# (--tempo-colors-black and --color-black are the same #000). When the twin
# resolves identically in both themes the second emit is skipped as one token
# under two names; a real value difference is left for emit() to reject.
TWINS = {}
for n in semantic_names:
    rn = n.replace("--tempo-colors-", "--color-")
    if rn in R and rn != n:
        same = (norm_color(R.get(rn)) == norm_color(R.get(n)) and
                norm_color(D.get(rn)) == norm_color(D.get(n)))
        if same:
            TWINS[rn] = n

for root in (SPEC["light"], SPEC["dark"]):
    for name in sorted(semantic_names):
        emit(root, name.replace("--tempo-colors-", "--color-"), var(name, "color" if decl_color(name)["type"] == "color" else "other"))
    for name in sorted(k for k in R if SEMANTIC.match(k)):
        if name in TWINS:
            continue
        ty = "color" if COLOR_V.fullmatch(str(R[name]).strip()) else "other"
        emit(root, name, var(name, ty))

# --------------------------------------------- measured roles (light set)
#
# Roles measured on the light marketing surface; each aliases to the
# declared token its value matches.

sem = SPEC["light"]
dsem = SPEC["dark"]
# Alias maps must be per-theme: the same hex can back different token names in
# the light and dark resolutions (e.g. #0f0d13 is --color-text-main in light
# but --color-bg-main in dark). Each set's map only sees its own values plus
# the theme-invariant palette scales.
role_alias = {"light": dict(color_alias), "dark": dict(color_alias)}
for name in sorted(semantic_names):
    p = EMITTED[name.replace("--tempo-colors-", "--color-")]
    role_alias["light"].setdefault(norm_color(R[name]), p)
    role_alias["dark"].setdefault(norm_color(D[name]), p)
for name in sorted(k for k in R if SEMANTIC.match(k)):
    p = EMITTED[name]
    role_alias["light"].setdefault(norm_color(R[name]), p)
    role_alias["dark"].setdefault(norm_color(D[name]), p)


def semcolor(raw, src, desc, theme="light"):
    alias = role_alias[theme].get(norm_color(raw))
    value = f"{{{alias}}}" if alias else norm_color(raw)
    return lit(value, "color", src + (f"; matches declared {alias}" if alias else ""), desc)


def layer(comp, state, node):
    """The background of the first painted layer of comp/state whose node starts with `node`."""
    return next(pl["bg"] for pl in C[comp]["states"][state]["paint"] if pl.get("bg") and pl.get("node", "").startswith(node))


for root, theme, key, comp, state, prop, group, desc in [
    (sem, "light", "page", "hero-h1", "default", "_body-bg", "background",
     "The white field the home hero paints."),
    (sem, "light", "ink", "hero-h1", "default", "color", "text",
     "The #0f0d13 ink — display headings, plan price lines and card text on the light surface."),
    (sem, "light", "on-dark", "mkt-nav-link", "default", "color", "text",
     "The #fdfcfe header text on the dark marketing top bar."),
    (sem, "light", "accent", "hero-cta", "default", "backgroundColor", "action",
     "The #a238ff light-theme accent on Try-for-free, Sign-up and plan chips."),
    (sem, "light", "dark-button", "plan-cta", "default", "backgroundColor", "action",
     "The #121216 near-black fill of the plan cards' Try-for-free action."),
    (sem, "light", "card", "plan-card", "default", "_paint", "background",
     "The #fdfcfe plan-card field on the offers band."),
    (sem, "light", "chip", "plan-card", "default", "_paint-chip", "background",
     "The #ebe7ee chip inside the plan cards."),
    (sem, "light", "chip-accent", "plan-title", "default", "backgroundColor", "action",
     "The #a238ff PREMIUM chip on the plan cards."),
    (sem, "light", "focus", "mkt-login", "focus-visible", "borderTopColor", "border",
     "The #555257 border the light header's Log-in button draws on keyboard focus."),
    (dsem, "dark", "canvas", "m-drawer", "default", "_paint-canvas", "background",
     "The #0f0d13 app canvas."),
    (dsem, "dark", "surface", "a-sidebar", "default", "backgroundColor", "background",
     "The #141216 sidebar and popover surface."),
    (dsem, "dark", "raised", "a-playlist-promo", "default", "backgroundColor", "background",
     "The #242326 raised field — promo cards and the search input."),
    (dsem, "dark", "field-focus", "a-search", "focused", "backgroundColor", "background",
     "The #2e2c30 a focused field lifts to."),
    (dsem, "dark", "text", "track-row", "default", "color", "text",
     "The #fdfcfe app text."),
    (dsem, "dark", "muted", "artist-fans", "default", "color", "text",
     "The #a19fa4 muted count text."),
    (dsem, "dark", "accent", "a-signup", "default", "backgroundColor", "action",
     "The #ad47ff dark-theme accent on Sign-up, Mix, track play and the login submit."),
    (dsem, "dark", "accent-hover", "a-signup", "hover", "backgroundColor", "action",
     "The #bb73ff the dark accent lifts to on hover."),
    (dsem, "dark", "divider", "player-bar", "default", "borderTopColor", "border",
     "The #38373b hairline over the player bar and between menu items."),
    (dsem, "dark", "focus", "a-search", "focused", "borderTopColor", "border",
     "The 2px #ad47ff border fields draw on focus."),
    (dsem, "dark", "banner", "signup-banner", "default", "_paint-banner", "background",
     "The #ead1ff 'Live the music with Deezer' signup banner."),
    (dsem, "dark", "toggle", "billing-toggle", "default", "backgroundColor", "background",
     "The #29282d billing-toggle track on the offers band."),
]:
    try:
        # Paint layers are picked by the element that paints them, never by the
        # colour they are expected to have.
        if prop == "_paint":
            raw = layer(comp, state, "div.unlogged-card")
            src = f"painted div.unlogged-card fill inside {comp} {state} (raw/components-computed.json)"
        elif prop == "_paint-chip":
            raw = layer(comp, state, "span.unlogged-card-tag")
            src = f"painted span.unlogged-card-tag chip fill inside {comp} {state} (raw/components-computed.json)"
        elif prop == "_paint-banner":
            raw = layer(comp, state, "div.css-18x5i1s")
            src = f"painted banner fill (the first div.css-18x5i1s layer) inside {comp} {state} (raw/components-computed.json)"
        elif prop == "_paint-canvas":
            raw = layer(comp, state, "ul.nav.burger-menu-content")
            src = f"painted ul.burger-menu-content canvas inside {comp} {state} (raw/components-computed.json)"
        elif prop == "_body-bg":
            # No measured element reports the page field: a screenshot sample.
            raw = "#ffffff"
            src = ("sampled, not measured: the white field behind the home hero read off screenshots/home-light-*.png; "
                   "no computed reading of the page field")
        else:
            raw = st(comp, state)[prop]
            src = f"computed {prop} of {comp} {state} (raw/components-computed.json)"
        root.setdefault(group, {})[key] = semcolor(raw, src, desc, theme)
    except (KeyError, StopIteration):
        pass

# ------------------------------------------------------------- type ramp

ty = SPEC["core"].setdefault("font", {}).setdefault("size", {})
for key, comp, state, desc in [
    ("xs", "a-signup", "default", "The 13px app pill-button label."),
    ("app", "mix-btn", "default", "The 15px app control and tab size."),
    ("body", "track-row", "default", "The 16px body, nav and track-text size."),
    ("app-section", "a-section-h2", "default", "The 20px app section heading."),
    ("plan-title", "plan-title", "default", "The 24px plan-name heading."),
    ("hero-sub", "hero-sub", "default", "The 35px hero sub-copy."),
    ("mobile-display", "m-hero-name", "default", "The 40px display size at 390px."),
    ("section", "section-h2", "default", "The 56px section heading; also the app's page display (Deezer Headline VF)."),
    ("h1", "offers-h1", "default", "The 78px offers display heading."),
    ("display", "hero-h1", "default", "The 140px home hero display."),
]:
    try:
        raw = st(comp, state)["fontSize"]
        src = f"computed fontSize of {comp} {state} (raw/components-computed.json)"
        alias = size_alias.get(raw)
        ty[key] = lit(f"{{{alias[0]}}}" if alias else raw, "fontSize",
                      src + (f"; matches declared {alias[1]}" if alias else ""), desc)
    except KeyError:
        pass

# ------------------------------------------------------------------ shape

radii = SPEC["core"].setdefault("radius", {})
radius_alias = {v: k for k, v in ((n, R[n]) for n in R if n.startswith("--tempo-radii-"))}
for key, comp, state, prop, desc in [
    ("card", "plan-card", "default", "_paint-card", "The 4px plan-card radius."),
    ("promo", "a-playlist-promo", "default", "borderTopLeftRadius", "The 8px sidebar promo-card radius."),
    ("pill-s", "a-signup", "default", "borderTopLeftRadius", "The 12px small pill (Sign up, Log in, mobile CTAs)."),
    ("control", "a-search", "default", "borderTopLeftRadius", "The 16px control radius — fields, Mix, CTAs, banner buttons."),
    ("popover", "menu-popover", "default", "borderTopLeftRadius", "The 24px overflow-popover radius."),
    ("full", "billing-toggle", "default", "borderTopLeftRadius", "The 256px full pill — the billing toggle and round icon buttons."),
]:
    try:
        if prop == "_paint-card":
            v = next(pl["radius"] for pl in C[comp]["states"][state]["paint"] if pl.get("bg") == "rgb(253, 252, 254)" and pl.get("radius"))
            src = f"painted radius of the plan card inside {comp} {state} (raw/components-computed.json)"
        else:
            v = st(comp, state)[prop]
            src = f"computed {prop} of {comp} {state} (raw/components-computed.json)"
        dkey = radius_alias.get(v)
        if dkey:
            radii[key] = lit(f"{{radius.{dkey[len('--tempo-radii-'):]}}}", "dimension", src + f"; matches declared {dkey}", desc)
        else:
            radii[key] = lit(v, "dimension" if re.fullmatch(r"[0-9.]+(px|rem)", v or "") else "other", src, desc)
    except (KeyError, StopIteration):
        pass

# ------------------------------------------------------------- elevation

sh = SPEC["core"].setdefault("shadow", {})
try:
    sh["popover"] = lit(st("menu-popover", "default")["boxShadow"], "other",
        "computed boxShadow of menu-popover default (raw/components-computed.json)",
        "The layered black shadow the overflow popover carries.")
except KeyError:
    pass

# ------------------------------------------------------------------ motion

mo = SPEC["core"].setdefault("motion", {})
try:
    s = st("a-signup", "default")
    dur, ease = s.get("transitionDuration"), s.get("transitionTimingFunction")
    if dur and dur != "0s":
        mo["control"] = lit(f"{s.get('transitionProperty', 'all')} {dur} {ease or ''}".strip(), "other",
            "computed transition of a-signup/a-search/mix-btn default (raw/components-computed.json); matches declared --tempo-transition-duration-normal",
            "The 0.2s background-color/border-color transition on buttons and fields.")
except KeyError:
    pass

# ------------------------------------------------------------- components

comp = SPEC["component"]
for name, cname, state, prop, ty_, desc in [
    ("topbar-height", "mkt-header", "default", "h", "dimension", "The 80px marketing top bar (matches declared --layout-topbar-height)."),
    ("sidebar-width", "a-sidebar", "default", "w", "dimension", "The 243px app sidebar rail."),
    ("player-bar-height", "player-bar", "default", "h", "dimension", "The 80px player bar."),
    ("banner-height", "signup-banner", "default", "h", "dimension", "The 80px signup banner pinned over the player."),
    ("track-row-height", "track-row", "default", "h", "dimension", "The 56px track-list row."),
    ("artist-image", "artist-avatar", "default", "w", "dimension", "The 278px round artist image."),
    ("popover-width", "menu-popover", "default", "w", "dimension", "The 308px track-overflow popover."),
    ("plan-card-width", "plan-card", "default", "w", "dimension", "The 600px offers plan card."),
    ("logo-width", "mkt-logo", "default", "w", "dimension", "The 107px header wordmark."),
    ("search-height", "a-search", "default", "h", "dimension", "The 48px header search field."),
    ("mobile-topbar-height", "m-topbar", "default", "h", "dimension", "The 60px phone top bar."),
]:
    try:
        v = rc(cname, state, prop)
        comp[name] = lit(("%g" % v) + "px" if isinstance(v, (int, float)) else str(v) + "px",
                         ty_, f"measured {prop} of {cname} {state} (raw/components-computed.json)", desc)
    except KeyError:
        pass

# A component the last run could not find keeps its earlier states (measure.mjs marks it
# recaptureMissed and keeps the first run's page/run/url). Say so on every token read from it,
# so a kept reading never ships as if the latest run had confirmed it.
FLAGGED = {k: v["recaptureMissed"] for k, v in C.items() if v.get("recaptureMissed")}


def note_flagged(node):
    if isinstance(node, dict):
        src = node.get("source")
        if isinstance(src, str):
            for k, missed in FLAGGED.items():
                if re.search(rf"(?<![\w-]){re.escape(k)}(?![\w-])", src) and f"{k} was not found" not in src:
                    node["source"] = src = (src + f"; {k} was not found by the {missed} re-run (recaptureMissed),"
                                            " so this is the reading kept from the earlier run")
        for v in node.values():
            note_flagged(v)


note_flagged(SPEC)

(RAW / "component-tokens.json").write_text(json.dumps(SPEC, indent=2, ensure_ascii=False) + "\n")
print("component-tokens.json:", {k: len(v) for k, v in SPEC.items() if k != "_about"})
