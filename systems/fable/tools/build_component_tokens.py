#!/usr/bin/env python3
"""Write raw/component-tokens.json, the token spec build_tokens.py reads.

fable.co paints two different skins signed out:

  emotion   the marketing pages (home, sign-in, support, /discover) —
            Emotion styled components (class names like css-1nlrkcz) on
            cream (#fcf9f5 pearl-50 / #f7f4ee pearl-extra-light) and deep
            forest-green (#064c37 forest-200 / #053829 forest-300) bands,
            "Heldane Display" mastheads over Inter body, 60px-radius pill
            controls with 2px same-as-fill borders, ink #161015
            (quote-theme-6) on light and #f7f4ee on dark, royal-blue
            #116ecd focus outlines.
  catalog   the product catalog (club/book/club-detail/search surfaces) —
            CSS-module components (*-module-scss-module__*) on a white field,
            the same Heldane display + Inter pairing through the
            lower-case 'heldane' webfont family, ink #1b1a1b
            (graphite-600 / --color-text-primary), 9999px pill buttons and
            chips, 24px search modal, focus ring --color-focus #0064c3.

The site ships a real Tailwind-style token layer in its app bundle
(raw/css-vars.json): palette scales
(--color-graphite/pearl/forest/olive/royal/iris/coral/rose/scarlet/amber-*,
plus partial sky/lemon/meadow/fern/indigo steps and black-100/white-100),
alpha ramps (--color-dark-fade-*, --color-white-fade-*, and per-hue
olive/royal/scarlet/amber fades), a 12-step --color-quote-theme-* set for
the reader's quote cards, a semantic layer
(--color-background-*/--color-text-*/--color-border-*/--color-line-*,
--color-focus, --color-primary/--color-secondary/--color-olive) redeclared
under a scoped `.dark` class (the app's dark reading/detail surfaces — not
a user toggle on the public pages), font stacks
(--font-body/--font-heading/--font-note/--font-script) fed by next/font
module variables (--font-inter, --font-heldane, --font-palmer-lake-print,
--font-des-montilles) plus seven --font-list-* reader-theme faces, a
--radius-0..40 + --radius-full scale, --shadow-above/below-1..4,
--border-width-1..3, --breakpoint-*, --spacing and --animate-flicker.
Component-scoped skins exist too (ListDetailView darkOnLight/lightOnDark,
ClubCard fixedLight, ShareMenu panelLight) — the same semantic names
re-pointed inside a component.

The probe in tools/capture/vars.mjs resolves every name on a plain <html>:
:root declarations resolve, `.dark` declarations can be resolved only by
following their declared var() chains — build_tokens.py does that for the
dark set.

Measured computed styles from raw/components-computed.json (78 components,
all states):

  ramp      Heldane display sizes 80/72/64/58/46/36/26px across the two
            skins (72px home hero, 46px at 390px; 58px clubs/support
            mastheads, 46px book/club detail titles, 64px discover),
            Inter body 16/15/14px, meta 12/10px, 13.333px browser-default
            Arial on unstyled controls
  shape     declared radius-full on catalog pills/buttons; emotion
            controls use literal 60px pills and a 44px text-input shell;
            24px modal, 12px inputs/tiles, 8px cover thumbnails
  motion    0.15s ease on catalog controls (Button module), 0.2s ease on
            emotion controls, 0.4s ease-in-out scale(1.01) card zoom
"""

import json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
V = json.loads((RAW / "css-vars.json").read_text())
RL = V.get("resolved", {}).get("light", {})
C = json.loads((RAW / "components-computed.json").read_text())["components"]
R = {n: (v.get("value", v.get("raw")) if isinstance(v, dict) else v) for n, v in RL.items()}

# Raw declarations per selector — for names that live on module classes
# (next/font variables) and never resolve on a bare <html>.
DECLARED = {}   # name -> (selector, raw value)
for r in V.get("theme", []) + V.get("app", []):
    sel = (r.get("selector") or "").strip()
    for n, val in (r.get("properties") or {}).items():
        DECLARED.setdefault(n, (sel, val))


def var(name, ty="color", **kw):
    d = {"var": name, "type": ty}
    d.update(kw)
    return d


SPEC = {"_about": (
    "The token tree build_tokens.py turns into tokens.json. fable.co "
    "declares a Tailwind-style token layer in its app bundle "
    "(raw/css-vars.json): theme-invariant palettes and scales under "
    "core.*, and a semantic layer the stylesheet redeclares under a "
    "scoped `.dark` class — emitted under both light.* and dark.* so "
    "each scope resolves its own value (the dark set follows the "
    "declared var() chains; no captured public page paints .dark). "
    "Measured roles alias to the declared values they match."),
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


def lit(value, ty, src, desc):
    return {"value": norm_color(value) if ty == "color" else value, "type": ty, "source": src, "description": desc}


EMITTED = {}   # variable name -> dotted token path it was actually written to
_OWNER = {}    # dotted token path -> variable name holding it


def _leaf(d):
    return isinstance(d, dict) and ("var" in d or "value" in d)


def emit(root, name, leaf):
    """Write `leaf` at name's dotted path (a --color-graphite-600 style name
    maps to color.graphite.600; dashes camelCase). A name that is both a leaf
    and the parent of other names parks its leaf under `default`."""
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


DECL_SRC = "declared design-system variable in fable.co's app bundle (raw/css-vars.json)"


def declared(name):
    v = R.get(name)
    return v if v not in (None, "") else None


COLOR_V = re.compile(r"(#[0-9a-fA-F]{3,8}|rgba?\([^)]*\)|hsla?\([^)]*\)|(ok)?lab\([^)]*\)|(ok)?lch\([^)]*\)|color-mix\([^)]*\))")


def decl_color(name):
    v = declared(name)
    ty = "color" if COLOR_V.fullmatch(str(v).strip()) else "other"
    return lit(v, ty, f"{DECL_SRC}: {name}", f"The declared `{name}`.")


def decl(name, ty="dimension"):
    v = declared(name)
    if ty == "dimension" and not re.fullmatch(r"-?\d+(\.\d+)?(px|rem)", str(v).strip()):
        ty = "other"
    return lit(v, ty, f"{DECL_SRC}: {name}", f"The declared `{name}`.")


def norm_len(v):
    m = re.fullmatch(r"(-?[\d.]+[eE][+-]?\d+)(px|rem)", str(v).strip())
    if not m:
        return v
    return f"{float(m.group(1)):f}".rstrip("0").rstrip(".") + m.group(2)


def painted(comp, state, key):
    """A reading from the kit's paint list — the layers actually painted
    (rounded children, pseudo-elements, shadows) rather than the wrapper's
    computed style, which is often an unpainted positioning box. An entry
    whose recorded size matches the element's own rect wins."""
    c = C[comp]["states"][state]
    entries = [p for p in c.get("paint") or [] if p.get(key)]
    if not entries:
        raise KeyError(key)
    rect = c.get("rect") or {}
    for p in entries:
        m = re.fullmatch(r"([\d.]+)x([\d.]+)", str(p.get("size") or ""))
        if m and abs(float(m.group(1)) - rect.get("w", -9)) <= 1.5 and abs(float(m.group(2)) - rect.get("h", -9)) <= 1.5:
            return p[key]
    return entries[0][key]


def ancestor(comp, state, key):
    """A reading from the kit's ancestor list (a painted wrapper above the
    element — the masthead band, the app-banner bar)."""
    c = C[comp]["states"][state]
    for a in c.get("ancestors") or []:
        if a.get(key) not in (None, ""):
            return a[key]
    raise KeyError(key)


# ------------------------------------------------------------------- fonts
#
# Four declared stacks on :root: --font-body (Inter), --font-heading
# (Heldane Display), --font-note (PalmerLakePrint) and --font-script
# (DesMontilles), each fed by a next/font module variable. Seven further
# --font-list-* faces ship for the reader's list/quote theming; they are
# declared on module classes so they never resolve on :root — emitted as
# literal stacks with their declaration as the source.

fam = SPEC["core"].setdefault("font", {}).setdefault("family", {})
for key, name, desc in [
    ("body", "--font-body", "Inter — every control, body and caption."),
    ("heading", "--font-heading", "Heldane Display — mastheads, section and detail titles."),
    ("note", "--font-note", "PalmerLakePrint — the hand-drawn annotation face."),
    ("script", "--font-script", "DesMontilles — the script/display accent face."),
]:
    if name in R:
        fam[key] = {"var": name, "type": "fontFamily", "description": desc}

LIST_FONTS = {
    "workSans": "--font-list-work-sans",
    "cormorantGaramond": "--font-list-cormorant-garamond",
    "newRocker": "--font-list-new-rocker",
    "pirataOne": "--font-list-pirata-one",
    "savate": "--font-list-savate",
    "specialElite": "--font-list-special-elite",
    "tradeWinds": "--font-list-trade-winds",
}
for key, name in LIST_FONTS.items():
    selraw = DECLARED.get(name)
    if selraw:
        sel, raw = selraw
        fam.setdefault("list", {})[key] = lit(
            raw, "fontFamily",
            f"declared on the {sel.split()[0]} next/font module class (raw/css-vars.json); a reader list/quote theme face, not resolved on :root",
            f"The reader list-theme face `{key}`.")

# ------------------------------------------------- measured type ramp
#
# fable declares no --text-* size ramp; the ramp is the measured sizes of
# the real headlines, per skin. Display sizes shrink on the phone capture.

sizes = SPEC["core"].setdefault("font", {}).setdefault("size", {})
lineheights = SPEC["core"].setdefault("font", {}).setdefault("lineHeight", {})
weights = SPEC["core"].setdefault("font", {}).setdefault("weight", {})

MEASURED_SIZES = [
    ("display", "section-h2", "default", "The 80px marketing section display (Heldane Display).", None),
    ("masthead", "hero-h1", "default", "The 72px home hero masthead — Heldane Display, 62px line.",
     "46px measured at 390 x 844 (m-hero-h1)"),
    ("discoverTitle", "disc-h1", "default", "The 64px /discover headline — Heldane Display, cream ink.", None),
    ("pageTitle", "clubs-h1", "default", "The 58px catalog/support masthead (clubs index, support).", None),
    ("detailTitle", "book-h1", "default", "The 46px book/club detail title — also the 390px hero size.", None),
    ("sectionTitle", "club-h2", "default", "The 36px in-page section title.", None),
    ("panelTitle", "signin-h1", "default", "The 26px sign-in panel title.", None),
    ("feature", "feature-h", "default", "The 24px marketing feature heading.", None),
    ("body", "faq-q", "default", "The 16px body/support copy size.", None),
    ("small", "search-input", "default", "The 15px search-field text.", None),
    ("control", "btn-primary", "default", "The 14px control label.", None),
    ("footerText", "footer-link", "default", "The 14px footer-link text.", None),
    ("trigger", "search-trigger", "default", "The 14px Inter label inside the unstyled 13.333px search-trigger shell.", None),
    ("meta", "author-link", "default", "The 12px byline/meta size.", None),
    ("micro", "spoiler-pill", "default", "The 10px badge/pill label.", None),
    ("fallback", "icon-btn", "default", "The 13.333px browser-default Arial left on icon-only controls — no font styles reach them.", None),
]
for key, comp, state, desc, resp in MEASURED_SIZES:
    # Prefer the kit's first-text-node reading (textStyle): a wrapper's own
    # fontSize is what children inherit, not what the visible text paints —
    # footer-link's shell is 15px over 14px text, search-trigger's is the
    # 13.333px browser default under a 14px Inter label.
    raw = ts(comp, state, "fontSize")
    if not raw:
        continue
    sizes[key] = lit(raw, "dimension",
                     f"computed fontSize of {comp} {state} — the first text node's reading where the kit recorded one (raw/components-computed.json)", desc)
    if resp:
        sizes[key]["responsive"] = resp

MEASURED_LH = [
    ("masthead", "hero-h1", "default", "The 62px hero masthead line (~0.86x)."),
    ("sectionTitle", "club-h2", "default", "The 36px section-title line (1x)."),
    ("detailTitle", "book-h1", "default", "The 48px detail-title line."),
    ("body", "faq-q", "default", "The 20px body line (1.25x)."),
    ("control", "btn-primary", "default", "The 21px control-label line on the emotion skin."),
]
for key, comp, state, desc in MEASURED_LH:
    raw = ts(comp, state, "lineHeight")
    if raw in (None, "normal", ""):
        continue
    lineheights[key] = lit(raw, "dimension",
                           f"computed lineHeight of {comp} {state} — the first text node's reading where the kit recorded one (raw/components-computed.json)", desc)

for key, w, comp, state, desc in [
    ("regular", 400, "mkt-header", "default", "Body/regular weight."),
    ("medium", 500, "hero-h1", "default", "The Heldane display weight on mastheads."),
    ("semibold", 600, "btn-primary", "default", "Control-label weight."),
    ("bold", 700, "clubs-h1", "default", "The heldane bold masthead weight (catalog skin)."),
]:
    try:
        st(comp, state)
        weights[key] = lit(w, "fontWeight",
                           f"computed fontWeight of {comp} {state} (raw/components-computed.json)", desc)
    except KeyError:
        pass

# ---------------------------------------------------------- core scales
#
# Theme-invariant declarations: the palette scales, alpha fade ramps,
# quote themes, named singles, radii, shadows, border widths, breakpoints,
# spacing and the one declared animation.

SEMANTIC_PREFIX = re.compile(r"^--color-(background|text|border|line)-")
SEMANTIC_NAMES = SEMANTIC_PREFIX  # kept readable below
SEMANTIC_EXTRA = {"--color-focus", "--color-primary", "--color-secondary", "--color-olive"}

def is_semantic(n):
    return bool(SEMANTIC_PREFIX.match(n)) or n in SEMANTIC_EXTRA

def cam(name):
    return re.sub(r"-([a-z])", lambda m: m.group(1).upper(), name)

for name in sorted(k for k in R if k.startswith("--color-") and not is_semantic(k)):
    emit(SPEC["core"], name, decl_color(name))
# normalized-colour -> core token path, for aliasing measured roles
color_alias = {}
for n, p in EMITTED.items():
    if p.startswith("color.") and declared(n) is not None and COLOR_V.fullmatch(str(R.get(n, "")).strip()):
        color_alias.setdefault(norm_color(R[n]), p)

radii = SPEC["core"].setdefault("radius", {})
radius_alias = {}
for name in sorted(k for k in R if re.fullmatch(r"--radius-[a-z0-9]+", k)):
    radii[name[len("--radius-"):]] = decl(name)
    radius_alias[str(R[name])] = name[len("--radius-"):]

shadows = SPEC["core"].setdefault("shadow", {})
for name in sorted(k for k in R if re.fullmatch(r"--shadow-(above|below)-\d", k)):
    m = re.fullmatch(r"--shadow-(above|below)-(\d)", name)
    shadows.setdefault(m.group(1), {})[m.group(2)] = lit(
        R[name], "other", f"{DECL_SRC}: {name}", f"The declared `{name}` elevation layer.")

bw = SPEC["core"].setdefault("border", {}).setdefault("width", {})
for name in sorted(k for k in R if re.fullmatch(r"--border-width-\d", k)):
    bw[name[len("--border-width-"):]] = decl(name)

bps = SPEC["core"].setdefault("breakpoint", {})
for name in sorted(k for k in R if re.fullmatch(r"--breakpoint-[a-z0-9-]+", k)):
    bps[cam(name[len("--breakpoint-"):])] = decl(name)

if declared("--spacing") is not None:
    SPEC["core"].setdefault("spacing", {})["base"] = decl("--spacing")

if declared("--animate-flicker") is not None:
    SPEC["core"].setdefault("animate", {})["flicker"] = lit(
        R["--animate-flicker"], "other", f"{DECL_SRC}: --animate-flicker",
        "The declared `flicker 1s linear infinite` keyframe animation.")

# ------------------------------------------ per-scope semantic variables
#
# The semantic names are redeclared under `.dark` (the app's scoped dark
# surfaces — reading/detail views; module-scoped twins darkOnLight/
# fixedLight/panelLight exist too). Every semantic name is emitted under
# both sets; build_tokens resolves .dark declarations by following their
# declared var() chains and falls back to the :root value for names the
# .dark block does not redeclare.

semantic_names = sorted(n for n in set(list(R) + list(DECLARED)) if is_semantic(n) and (declared(n) is not None or n in DECLARED))
for root in (SPEC["light"], SPEC["dark"]):
    for name in semantic_names:
        emit(root, name, var(name, "color" if COLOR_V.fullmatch(str(R.get(name, "")).strip()) else "other"))

# -------------------------------------------------- measured light roles

def semcolor(raw, src, desc):
    alias = color_alias.get(norm_color(raw))
    value = f"{{{alias}}}" if alias else norm_color(raw)
    return lit(value, "color", src + (f"; matches declared {alias}" if alias else ""), desc)


sem = SPEC["light"]
for key, comp, state, prop, group, desc in [
    ("ink", "cat-nav-link", "default", "ts:color", "text",
     "The near-black catalog ink (graphite-600 / --color-text-primary)."),
    ("emotionInk", "signin-h1", "default", "color", "text",
     "The softer near-black the emotion marketing pages use (quote-theme-6 #161015)."),
    ("onDark", "hero-h1", "default", "color", "text",
     "The cream display ink on forest and dark bands (pearl-extra-light #f7f4ee)."),
    ("muted", "read-more", "default", "ts:color", "text",
     "The graphite secondary text (--color-text-secondary #4b4649); the club card mutes to #3f383d and the footer to #847f7c."),
    ("footerMuted", "footer", "default", "ts:color", "text",
     "The warm grey footer text (#847f7c — unnamed in the stylesheet)."),
    ("ctaFill", "btn-primary", "default", "backgroundColor", "action",
     "The near-black catalog CTA fill (graphite-600)."),
    ("ctaInk", "btn-primary", "default", "color", "action",
     "The white ink on the catalog CTA."),
    ("emotionCtaFill", "submit-btn", "default", "backgroundColor", "action",
     "The dark emotion pill fill (named --color-graphite #292229)."),
    ("emotionCtaInk", "submit-btn", "default", "color", "action",
     "The white ink on the dark emotion pill."),
    ("focusRing", "btn-primary", "focus-visible", "outlineColor", "border",
     "The catalog keyboard focus ring (declared --color-focus #0064c3)."),
    ("emotionFocusRing", "mkt-nav-link", "focus-visible", "outlineColor", "border",
     "The emotion pages' lighter blue focus outline (#116ecd — a literal, not a declared var)."),
    ("hairline", "genre-pill", "default", "paint:border", "border",
     "The graphite-300 hairline on white pills/chips (--color-border-primary)."),
]:
    try:
        if prop == "ts:color":
            raw = ts(comp, state, "color")
            src = f"computed color of {comp} {state} — the first text node's reading where the kit recorded one (raw/components-computed.json)"
        elif prop == "paint:border":
            p = painted(comp, state, "border")
            raw = p.split("|")[0].split(" ", 1)[1].strip()
            src = f"the 1px border painted on {comp} {state} (raw/components-computed.json paint list)"
        else:
            raw = st(comp, state)[prop]
            src = f"computed {prop} of {comp} {state} (raw/components-computed.json)"
        if raw in (None, ""):
            raise KeyError(prop)
        sem.setdefault(group, {})[key] = semcolor(raw, src, desc)
    except KeyError:
        pass

for key, comp, state, how, desc in [
    ("page", "search-modal", "default", "ancestor:bg",
     "The white catalog page field (--color-background-primary)."),
    ("surface", "search-icon-btn", "default", "backgroundColor",
     "The pearl-100 raised surface on circular icon buttons (--color-background-secondary)."),
    ("surfaceHover", "search-icon-btn", "hover", "backgroundColor",
     "The pearl-200 hover fill on icon buttons (--color-background-tertiary #ebe7d9)."),
    ("band", "support-masthead", "default", "ancestor:bg",
     "The deep forest-green masthead band (forest-200 #064c37 = --color-background-forest)."),
    ("appBanner", "app-banner", "default", "backgroundColor",
     "The darker forest app-download banner (forest-300 #053829)."),
    ("footer", "footer", "default", "backgroundColor",
     "The near-black footer field (black-100 #070607)."),
]:
    try:
        if how == "ancestor:bg":
            raw = ancestor(comp, state, "bg")
            src = f"the painted background of {comp}'s wrapper ancestor {state} (raw/components-computed.json)"
        else:
            raw = st(comp, state)[how]
            src = f"computed {how} of {comp} {state} (raw/components-computed.json)"
        sem.setdefault("background", {})[key] = semcolor(raw, src, desc)
    except KeyError:
        pass

# -------------------------------------------------- measured dark roles
#
# The dark set is the stylesheet's scoped `.dark` theme — declared, not
# painted on any captured page. The two measured dark surfaces that do
# exist signed out (the footer and the /discover cover wall) line up with
# its values and are aliased honestly.

dsem = SPEC["dark"]
for key, comp, state, prop, group, desc in [
    ("discoverInk", "disc-h1", "default", "color", "text",
     "The cream ink over the /discover cover wall (pearl-extra-light)."),
    ("footerInk", "footer", "default", "color", "text",
     "The white footer ink (text-ondark)."),
]:
    try:
        raw = st(comp, state)[prop]
        src = f"computed {prop} of {comp} {state} (raw/components-computed.json)"
        dsem.setdefault(group, {})[key] = semcolor(raw, src, desc)
    except KeyError:
        pass
try:
    dsem.setdefault("background", {})["footer"] = semcolor(
        st("footer", "default")["backgroundColor"],
        "computed backgroundColor of footer default (raw/components-computed.json); matches the .dark scope's --color-background-primary (black-100)",
        "The measured near-black footer — the same #070607 the .dark scope paints as background-primary.")
except KeyError:
    pass

# ------------------------------------------------------------------ shape

for key, comp, state, prop, desc in [
    ("pill", "btn-primary", "default", "borderTopLeftRadius",
     "The catalog pill radius (radius-full 9999px)."),
    ("emotionPill", "getapp-hero", "default", "paint:radius",
     "The emotion skin's 60px pill radius — a literal, not a declared var."),
    ("fieldShell", "show-btn", "default", "ancestor:radius",
     "The 44px radius of the sign-in text-input shell."),
    ("modal", "search-modal", "default", "paint:radius",
     "The search modal corner radius (radius-24)."),
    ("input", "search-input", "default", "paint:radius",
     "The search input corner radius (radius-12)."),
    ("cover", "book-card", "default", "paint:radius",
     "The book-cover thumbnail radius (radius-8)."),
]:
    try:
        if prop == "paint:radius":
            v = norm_len(painted(comp, state, "radius"))
            src = f"the painted radius of {comp}'s rounded layer {state} (raw/components-computed.json paint list)"
        elif prop == "ancestor:radius":
            v = norm_len(ancestor(comp, state, "radius"))
            src = f"the painted radius of {comp}'s wrapper ancestor {state} (raw/components-computed.json)"
        else:
            v = norm_len(st(comp, state)[prop])
            src = f"computed {prop} of {comp} {state} (raw/components-computed.json)"
        dkey = radius_alias.get(v)
        if dkey:
            radii[key] = lit(f"{{radius.{dkey}}}", "dimension", src + f"; matches declared --radius-{dkey}", desc)
        else:
            radii[key] = lit(v, "dimension" if re.fullmatch(r"[0-9.]+(px|rem)", v or "") else "other", src, desc)
    except KeyError:
        pass

# ------------------------------------------------------------------ motion

mo = SPEC["core"].setdefault("motion", {})
for key, comp, desc in [
    ("catalogControl", "btn-primary", "The 0.15s ease on catalog controls (the Button module's background/color/opacity/border transition)."),
    ("emotionControl", "getapp-hero", "The 0.2s ease on emotion pill controls."),
    ("cardZoom", "club-card", "The 0.4s ease-in-out transform on the marketing club card (scale 1.01 on hover)."),
]:
    try:
        s = st(comp, "default")
        dur, ease = s.get("transitionDuration"), s.get("transitionTimingFunction")
        if dur and dur != "0s":
            props = [p.strip() for p in s.get("transitionProperty", "all").split(",") if p.strip()]
            durs = [d.strip() for d in dur.split(",")]
            eases = [e.strip() for e in (ease or "ease").split(",")]
            val = ", ".join(f"{p} {durs[min(i, len(durs)-1)]} {eases[min(i, len(eases)-1)]}"
                            for i, p in enumerate(props))
            mo[key] = lit(val, "other",
                          f"computed transition of {comp} default (raw/components-computed.json)", desc)
    except KeyError:
        pass
mo["hoverFade"] = lit("0.85", "number",
                      "computed opacity of btn-primary hover/pressed (raw/components-computed.json)",
                      "The 0.85 opacity the catalog primary button fades to on hover/pressed.")

# ------------------------------------------------------------- components
#
# Measured geometry and the skin-specific measured literals — the emotion
# marketing skin, the catalog skin, and the /discover cover wall.

comp = SPEC["component"]
for name, cname, state, prop, desc in [
    ("headerHeight", "cat-header", "default", "h", "The 60px header bar (identical on both skins)."),
    ("logoWidth", "mkt-logo", "default", "w", "The ~82px Fable wordmark."),
    ("heroMastheadW", "hero-h1", "default", "w", "The hero masthead measure."),
    ("heroCoverW", "hero-cover", "default", "w", "The 151px hero cover tile."),
    ("heroCoverH", "hero-cover", "default", "h", "The 225px hero cover height."),
    ("marketingPillH", "getapp-hero", "default", "h", "The 52px marketing pill height."),
    ("marketingPillRadius", "getapp-hero", "default", "paint:radius", "The 60px emotion pill radius."),
    ("ctaHeight", "getapp-cta", "default", "h", "The 44px 'Get the app' CTA height."),
    ("catalogButtonH", "btn-primary", "default", "h", "The 52px catalog button height."),
    ("catalogButtonW", "btn-primary", "default", "w", "The 361px catalog button width (form-width)."),
    ("genrePillH", "genre-pill", "default", "h", "The 46px genre chip height."),
    ("iconBtn", "icon-btn", "default", "w", "The 40px round icon button."),
    ("searchIconBtn", "search-icon-btn", "default", "w", "The 44px pearl search button."),
    ("searchTriggerW", "search-trigger", "default", "w", "The 440px clubs search pill."),
    ("searchTriggerH", "search-trigger", "default", "h", "The 52px clubs search pill height."),
    ("searchModalW", "search-modal", "default", "w", "The 480px search modal."),
    ("searchModalH", "search-modal", "default", "h", "The 497px search modal height."),
    ("searchInputH", "search-input", "default", "h", "The 41px modal search input."),
    ("spoilerPillH", "spoiler-pill", "default", "h", "The 28px 'Spoilers' sizeXs badge."),
    ("clubCardW", "club-card-cat", "default", "w", "The 256px stacked-cover club card."),
    ("clubCardH", "club-card-cat", "default", "h", "The 372px club card height."),
    ("bookCoverW", "book-card", "default", "w", "The 167px book card cover width."),
    ("appBannerH", "app-banner", "default", "h", "The 132px app-download banner."),
    ("signinPanelW", "signin-panel", "default", "w", "The ~396px sign-in panel width."),
    ("signinFieldH", "field-email", "default", "h", "The ~50px sign-in field height (52px painted shell)."),
    ("signinButtonH", "submit-btn", "default", "h", "The 44px sign-in button height."),
    ("supportCardPad", "help-card", "default", "paddingTop", "The 18px support-card padding."),
    ("footerPadY", "footer", "default", "paddingTop", "The 100px footer padding (80px on the phone)."),
    ("mHeaderH", "m-header", "default", "h", "The 60px phone header."),
    ("mClubCardW", "m-club-card", "default", "w", "The ~317px phone club card."),
    ("mFooterPadY", "m-footer", "default", "paddingTop", "The 80px phone footer padding."),
    ("discoverFieldW", "disc-field", "default", "w", "The 420px discover search field."),
    ("discoverFieldH", "disc-field", "default", "h", "The ~60px discover search field height."),
    ("discoverPillH", "disc-random", "default", "h", "The ~50px discover pill height."),
    ("discoverWordmarkW", "disc-wordmark", "default", "w", "The ~81px discover wordmark."),
]:
    try:
        if prop.startswith("paint:"):
            v = painted(cname, state, prop[6:])
            val = v if re.search(r"[a-z]$", str(v)) else str(v) + "px"
        elif prop in ("w", "h"):
            v = rc(cname, state, prop)
            val = ("%g" % v) + "px"
        else:
            val = st(cname, state)[prop]
        ty_ = "dimension" if re.fullmatch(r"-?\d+(\.\d+)?(px|rem)", str(val)) else "other"
        comp[name] = lit(val, ty_, f"measured {prop} of {cname} {state} (raw/components-computed.json)", desc)
    except KeyError:
        pass

# The /discover cover-wall surface and the two skins' measured literals.
sk = comp.setdefault("skin", {})
for key, cname, state, prop, group, desc in [
    ("marketingInk", "signin-h1", "default", "color", "marketing",
     "The emotion skin's near-black ink (#161015, quote-theme-6)."),
    ("marketingPillFill", "getapp-dark", "default", "backgroundColor", "marketing",
     "The dark emotion pill fill (--color-graphite #292229)."),
    ("marketingPillHoverFill", "getapp-dark", "hover", "backgroundColor", "marketing",
     "The dark pill's hover fill (#433944 — a literal)."),
    ("marketingPillInk", "getapp-hero", "default", "color", "marketing",
     "The ink on the white emotion pill (#161015)."),
    ("marketingPillHoverInk", "getapp-hero", "hover", "color", "marketing",
     "The hover ink on emotion pills (#332e32 — a literal)."),
    ("textInputBorder", "signin-panel", "default", "paint:border", "marketing",
     "The #bcbcbc sign-in text-input hairline — a literal, not a declared var."),
    ("catalogFocus", "cat-nav-link", "focus-visible", "outlineColor", "catalog",
     "The catalog focus ring #0064c3 (--color-focus)."),
    ("catalogChipHover", "genre-pill", "hover", "backgroundColor", "catalog",
     "The #f8f8f8 chip hover (graphite-100)."),
    ("coverPlaceholder", "book-card", "default", "paint:bg", "catalog",
     "The pearl-200 #ebe7d9 book-cover placeholder fill."),
    ("discoverPillFill", "disc-random", "default", "paint:bg", "discover",
     "The forest-400 #042119 discover pill fill."),
    ("discoverPillInk", "disc-random", "default", "color", "discover",
     "The muted lilac-grey discover pill ink (#c5c1c5 — a literal)."),
    ("discoverFieldInk", "disc-field", "default", "color", "discover",
     "The #161015 ink inside the white discover field."),
    ("bannerInk", "app-banner", "default", "color", "catalog",
     "The forest-200 #064c37 headline inside the forest-300 banner."),
]:
    try:
        if prop == "paint:border":
            raw = painted(cname, state, "border").split("|")[0].split(" ", 1)[1].strip()
            src = f"the 1px border painted on {cname}'s input shell {state} (raw/components-computed.json paint list)"
        elif prop == "paint:bg":
            raw = painted(cname, state, "bg")
            src = f"the painted background of {cname}'s layer {state} (raw/components-computed.json paint list)"
        else:
            raw = st(cname, state)[prop]
            src = f"computed {prop} of {cname} {state} (raw/components-computed.json)"
        sk.setdefault(group, {})[key] = semcolor(raw, src, desc)
    except KeyError:
        pass

for key, cname, state, prop, group, desc, ty_ in [
    ("wallScrim", "disc-wall", "default", "backgroundImage", "discover",
     "The layered radial-gradient scrim over the cover wall — rgba(12,92,66,0.85) lead stop, transparent by ~64%.", "other"),
    ("fieldShadow", "disc-field", "default", "boxShadow", "discover",
     "The discover field's drop shadow — rgba(12,12,12,0.45) 0px 10px 34px.", "other"),
    ("modalShadow", "search-modal", "default", "paint:shadow", "catalog",
     "The search modal's elevation shadow.", "other"),
]:
    try:
        if prop.startswith("paint:"):
            raw = painted(cname, state, prop[6:])
            src = f"the painted {prop[6:]} of {cname} {state} (raw/components-computed.json paint list)"
        else:
            raw = st(cname, state)[prop]
            src = f"computed {prop} of {cname} {state} (raw/components-computed.json)"
        sk.setdefault(group, {})[key] = lit(raw, ty_, src, desc)
    except KeyError:
        pass

(RAW / "component-tokens.json").write_text(json.dumps(SPEC, indent=2, ensure_ascii=False) + "\n")
print("component-tokens.json:", {k: len(v) for k, v in SPEC.items() if k != "_about"})
