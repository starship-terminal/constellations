#!/usr/bin/env python3
"""Write raw/component-tokens.json, the token spec build_tokens.py reads.

enode.com is one marketing surface signed out: every page paints
<html data-mode="light" data-ink="alpha">, with scoped [data-mode="dark"]
showcase sections inside the light page (the hero media panel, the demo
tiles, the mega-menu). platform.enode.com/login is a separate app — a light
sign-in panel over a dark product showcase — that does not share the
marketing token layer; its values land under component.* as measured
literals.

The site declares a real design-token layer in its inline app-css bundle
(raw/css-vars.json): the --color-brand-* and --color-gray-* palette scales
with --color-gray-alpha-*/--color-white-alpha-* partners, named hues
(--color-enode-green-*, --color-signal-brand, --color-deep-black,
--color-warm-grey), the --text-* type ramp with --leading-*/--tracking-/
--font-weight-* companions, --font-sans/--font-mono, --spacing, --radius-*,
--container-*, --grid-*/--gutter-*, --breakpoint-md, --blur-*, --ease-* and
--default-transition-* — plus a semantic layer redeclared under
[data-mode="light"] and [data-mode="dark"]: --color-background-*,
--color-text-*, --color-foreground-*, --color-border-*, --color-line-*,
--color-card-*, --color-nav-ink*, --color-button-ink, --color-node*,
--color-browser-*, --color-phone-*, --color-diagram-*, --color-visual-*
and the --shadow-* hairlines. Declared scales land under core.*; every
[data-mode]-switching name is emitted under both light.* and dark.* as a
{"var": ...} leaf so each scope resolves its own value.

Measured computed styles from raw/components-computed.json:

  light       #f0fde8 mint page field (brand-75 via the html inline
              --color-page-background), #252322 ink, the dark pill CTAs,
              nav pills in rgba ink, the dark glass mega-menu
  dark        the scoped showcase: #151413 panel, #ededed-at-alpha ink,
              brand-green #b0f87c node/sign accents, hairline borders
  fonts       Enode Sans VF (375–635, marketing + UI) and Enode Mono VF
              (product demo/code frames) — a variable-weight file, so the
              ramp uses 450/470/475/490/510/520 steps, not CSS stock names
  ramp        declared 68/44/40/36/36/30/24/22/20/18/15/14/12px steps with
              <48rem overrides for the display sizes
  shape       2/4/6/10px radius scale plus the full pill (radius-full);
              pills on nav links and CTAs, rounded cards
  motion      the declared 0.15s cubic-bezier(.4,0,.2,1) control
              transition; a 0.4s --theme-fade for [data-mode] swaps
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
    "The token tree build_tokens.py turns into tokens.json. enode.com "
    "declares its design-token layer in the inline app-css bundle "
    "(raw/css-vars.json): theme-invariant scales under core.* and a "
    "[data-mode]-switching semantic layer emitted under both light.* and "
    "dark.* so each scope resolves its own value. Measured roles alias to "
    "the declared values where they match."),
    "core": {}, "light": {}, "dark": {}, "component": {}}


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


def emitted_path(name):
    return EMITTED[name]


DECL_SRC = "declared design-system variable in the site's inline app-css bundle (raw/css-vars.json)"


def declared(name):
    """The resolved light-set value, or None when the var never resolved."""
    v = R.get(name)
    return v if v not in (None, "") else None


def decl(name, ty="dimension"):
    v = declared(name)
    desc = f"The declared `{name}`."
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
    ty = "color" if COLOR_V.fullmatch(str(v).strip()) else "other"
    return lit(v, ty, f"{DECL_SRC}: {name}", f"The declared `{name}`.")


def ratio(name):
    """calc(a/b) -> float for a line-height var; everything else stays raw."""
    v = declared(name)
    m = re.fullmatch(r"calc\(\s*(-?\d*\.?\d+)\s*/\s*(-?\d*\.?\d+)\s*\)", str(v))
    if m:
        return lit(round(float(m.group(1)) / float(m.group(2)), 4), "number",
                   f"{DECL_SRC}: {name}", f"The declared `{name}` line-height ratio.")
    return decl(name, "other")


def norm_len(v):
    """Exponential lengths become ordinary pixel strings: Chromium serialises
    `calc(infinity * 1px)` as `3.35544e+07px`, which is a real length, not an
    `other` — it is how the site spells a full pill."""
    m = re.fullmatch(r"(-?[\d.]+[eE][+-]?\d+)(px|rem)", str(v).strip())
    if not m:
        return v
    return f"{float(m.group(1)):f}".rstrip("0").rstrip(".") + m.group(2)


def painted(comp, state, key):
    """A reading from the kit's paint list — the layers actually painted
    (rounded children, pseudo-elements, inset shadows) rather than the
    wrapper's computed style, which is often an unpainted positioning box.
    An entry whose recorded size matches the element's own rect wins."""
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


# ------------------------------------------------------------------- fonts
#
# enode ships two variable fonts: Enode Sans (wght 375–635) for all text and
# Enode Mono (375–635) for product demos and code frames. Both are declared
# in the token layer.

fam = SPEC["core"].setdefault("font", {}).setdefault("family", {})
for key, name, desc in [
    ("sans", "--font-sans", "Enode Sans VF — every heading, control and body."),
    ("mono", "--font-mono", "Enode Mono VF — product demo and code frames."),
]:
    if name in R:
        fam[key] = {"var": name, "type": "fontFamily", "description": desc}
        fam[key + "FeatureSettings"] = decl(name + "--font-feature-settings", "other")

weights = SPEC["core"].setdefault("font", {}).setdefault("weight", {})
for name in sorted(k for k in R if k == "--font-weight-light" or k == "--font-weight-medium"):
    weights[name[len("--font-weight-"):]] = decl(name, "fontWeight")
# The ramp steps are variable-font weights; each is declared per text style.
for name in sorted(k for k in R if re.fullmatch(r"--text-[a-z0-9]+(-[a-z0-9]+)*--font-weight", k)):
    weights[name[len("--text-"):].replace("--font-weight", "")] = decl(name, "fontWeight")

# ------------------------------------------------------------- type ramp
#
# --text-* sizes with their --line-height/--letter-spacing/--font-weight
# companions. The display sizes override under 48rem; the override is kept
# on $extensions.responsive.

RESPONSIVE_SIZE = {
    "--text-display": "2.125rem under 48rem",
    "--text-h1": "1.875rem under 48rem",
    "--text-h2": "1.5625rem under 48rem",
    "--text-lede": "1.5rem under 48rem",
    "--text-quote": "1.125rem under 48rem",
    "--text-quote-lg": "1.5rem under 48rem",
}
# Small-viewport sizes measured on the 390px phone capture.
MOBILE_MEASURED = {}
try:
    MOBILE_MEASURED["masthead"] = st("m-hero-h1", "default")["fontSize"]
except KeyError:
    gap("mobile masthead: no m-hero-h1 default fontSize reading")
sizes = SPEC["core"].setdefault("font", {}).setdefault("size", {})
for name in sorted(k for k in R if re.fullmatch(r"--text-[a-z0-9]+(-[a-z0-9]+)*", k)):
    key = name[len("--text-"):]
    raw = str((RL.get(name) or {}).get("raw") or "")
    responsive = RESPONSIVE_SIZE.get(name)
    if responsive is None and raw and not re.fullmatch(r"-?[\d.]+(px|rem)", raw):
        # The declaration is a fluid expression, not a fixed step: the exported
        # px is only its resolution at the 1440px capture viewport, so the
        # expression is preserved here and applying it reproduces smaller
        # viewports.
        responsive = f"fluid — apply `{raw}`; the px value resolves it at 1440 x 900"
        if key in MOBILE_MEASURED:
            responsive += f" (measured {MOBILE_MEASURED[key]} at 390 x 844)"
    sizes[key] = var(name, "dimension", responsive=responsive)

lineheights = SPEC["core"].setdefault("font", {}).setdefault("lineHeight", {})
for name in sorted(k for k in R if k.startswith("--leading-")):
    v = str(R[name])
    if "calc" in v:
        lineheights[name[len("--leading-"):]] = ratio(name)
    elif re.fullmatch(r"-?\d+(\.\d+)?", v):
        lineheights[name[len("--leading-"):]] = lit(float(v), "number", f"{DECL_SRC}: {name}", f"The declared `{name}` line-height ratio.")
    else:
        lineheights[name[len("--leading-"):]] = decl(name, "other")
for name in sorted(k for k in R if re.fullmatch(r"--text-[a-z0-9]+(-[a-z0-9]+)*--line-height", k)):
    lineheights[name[len("--text-"):].replace("--line-height", "")] = ratio(name)

tracking = SPEC["core"].setdefault("font", {}).setdefault("tracking", {})
for name in sorted(k for k in R if k.startswith("--tracking-")):
    tracking[name[len("--tracking-"):]] = decl(name)
for name in sorted(k for k in R if re.fullmatch(r"--text-[a-z0-9]+(-[a-z0-9]+)*--letter-spacing", k)):
    tracking[name[len("--text-"):].replace("--letter-spacing", "")] = decl(name, "other")

# ---------------------------------------------------------- core scales
#
# Theme-invariant declarations: the palette scales and named hues, spacing
# base, radii, containers, the layout grid, breakpoints, blurs, easings and
# durations. These resolve identically in both data-mode scopes.

color_alias = {}   # normalized colour -> 'color.<path>' for aliasing
colors = SPEC["core"].setdefault("color", {})

for name in sorted(k for k in R if re.fullmatch(r"--color-brand-\d+", k)):
    colors.setdefault("brand", {})[name[len("--color-brand-"):]] = decl_color(name)
    color_alias.setdefault(norm_color(R[name]), f"color.brand.{name[len('--color-brand-'):]}")
for name in sorted(k for k in R if re.fullmatch(r"--color-gray-\d+", k)):
    colors.setdefault("gray", {})[name[len("--color-gray-"):]] = decl_color(name)
    color_alias.setdefault(norm_color(R[name]), f"color.gray.{name[len('--color-gray-'):]}")
for name in sorted(k for k in R if re.fullmatch(r"--color-gray-alpha-\d+", k)):
    colors.setdefault("grayAlpha", {})[name[len("--color-gray-alpha-"):]] = decl_color(name)
for name in sorted(k for k in R if re.fullmatch(r"--color-white-alpha-\d+", k)):
    colors.setdefault("whiteAlpha", {})[name[len("--color-white-alpha-"):]] = decl_color(name)

NAMED = {
    "white": "Pure white — secondary surface, pill ink on dark buttons.",
    "black": "Pure black.",
    "deep-black": "The warm near-black of the dark showcase (#161514).",
    "warm-grey": "The warm off-white surface (#efedec).",
    "enode-green": "The brand green (#b0f87d) — accent, node sign, focus ring base.",
    "enode-green-deep": "A deeper brand green (#99e467).",
    "enode-green-mid": "A mid brand green (#a9ee77).",
    "enode-green-soft": "A soft brand green (#c5ff9b).",
    "enode-green-softest": "The softest brand green (#cfffad).",
    "signal-brand": "The signal brand green — control link/focus ring source.",
    "control-link": "The declared control link colour (brand green).",
    "control-focus-ring": "The declared keyboard focus ring (brand green).",
    "transparent": "Fully transparent.",
    "current": "currentColor passthrough.",
}
for name, desc in NAMED.items():
    vn = f"--color-{name}"
    if declared(vn) is not None:
        colors[re.sub(r"-([a-z])", lambda m: m.group(1).upper(), name)] = lit(
            R[vn], "color" if COLOR_V.fullmatch(str(R[vn]).strip()) else "other",
            f"{DECL_SRC}: {vn}", desc)
        color_alias.setdefault(norm_color(R[vn]), "color." + re.sub(r"-([a-z])", lambda m: m.group(1).upper(), name))

if declared("--spacing") is not None:
    SPEC["core"].setdefault("spacing", {})["base"] = decl("--spacing")

radius_alias = {}
radii = SPEC["core"].setdefault("radius", {})
for name in sorted(k for k in R if re.fullmatch(r"--radius-[a-z]+", k)):
    radii[name[len("--radius-"):]] = decl(name)
    radius_alias[norm_len(R[name])] = name[len("--radius-"):]

containers = SPEC["core"].setdefault("container", {})
for name in sorted(k for k in R if re.fullmatch(r"--container-[a-z0-9]+", k)):
    containers[name[len("--container-"):]] = decl(name)

layout = SPEC["core"].setdefault("layout", {})
for key, name, desc, kw in [
    ("gridMax", "--grid-max", "The 1308px content grid maximum.", {}),
    ("gridInset", "--grid-inset", "The grid side inset — 40px at 1440; 24px from 48rem, narrower below.",
     {"responsive": "1.5rem from 48rem; 2.5rem from 64rem (resolved at 1440 x 900)"}),
    ("gutterBase", "--gutter-base", "The 20px base gutter.", {}),
    ("gutterTight", "--gutter-tight", "The 8px tight gutter.", {}),
    ("heroMediaOvershoot", "--hero-media-overshoot", "The 48px the hero media panel overshoots.", {}),
]:
    if declared(name) is not None:
        layout[key] = lit(R[name], "dimension" if re.fullmatch(r"-?\d+(\.\d+)?(px|rem)", str(R[name])) else "other",
                          f"{DECL_SRC}: {name}", desc)
        layout[key].update(kw)
if declared("--enabler-grid-shift") is not None:
    layout["enablerGridShift"] = decl("--enabler-grid-shift", "number")

if declared("--breakpoint-md") is not None:
    SPEC["core"].setdefault("breakpoint", {})["md"] = decl("--breakpoint-md")

if declared("--aspect-video") is not None:
    SPEC["core"].setdefault("aspect", {})["video"] = decl("--aspect-video", "other")

for name in sorted(k for k in R if re.fullmatch(r"--blur-[a-z]+", k)):
    SPEC["core"].setdefault("blur", {})[name[len("--blur-"):]] = decl(name)

easing = SPEC["core"].setdefault("easing", {})
for name in sorted(k for k in R if k.startswith("--ease-")):
    easing[name[len("--ease-"):]] = decl(name, "cubicBezier")
if declared("--default-transition-timing-function") is not None:
    easing["default"] = decl("--default-transition-timing-function", "cubicBezier")
if declared("--default-transition-duration") is not None:
    SPEC["core"].setdefault("duration", {})["default"] = decl("--default-transition-duration", "duration")
if declared("--theme-fade-duration") is not None:
    SPEC["core"].setdefault("duration", {})["themeFade"] = lit(
        declared("--theme-fade-duration"), "duration", f"{DECL_SRC}: --theme-fade-duration",
        "The 0.4s cross-fade duration applied when [data-mode] scopes swap (declared on html).")

# ------------------------------------------ per-scope semantic variables
#
# Everything redeclared inside [data-mode="light"] and [data-mode="dark"]
# switches value between the scopes — every such name is emitted under both
# sets so each resolves its own value. The page always carries
# data-ink="alpha"; the login app does not share this layer.

mode_names = set()
for rule in V.get("theme", []):
    sel = " ".join(rule.get("context") or []) + " " + rule.get("selector", "")
    if 'data-mode="light"' in sel or 'data-mode="dark"' in sel or "[data-mode=" in sel:
        mode_names.update(rule.get("properties") or {})
# --showcase-flush* sits in the app bin (:root + [data-mode="dark"]) but
# switches per scope the same way.
mode_names.update(n for n in R if n.startswith("--showcase-"))

semantic_names = sorted(n for n in mode_names if declared(n) is not None or D.get(n) is not None)
for root in (SPEC["light"], SPEC["dark"]):
    for name in semantic_names:
        leaf_ = var(name, "color" if COLOR_V.fullmatch(str(R.get(name, "")).strip()) else "other")
        if name.startswith("--shadow-"):
            leaf_["type"] = "other"
        emit(root, name, leaf_)

# --------------------------------------------- measured roles
#
# Roles measured on the real pages; each aliases to the declared token its
# value matches.

role_alias = {"light": dict(color_alias), "dark": dict(color_alias)}
for name in semantic_names:
    p = EMITTED[name]
    if R.get(name):
        role_alias["light"].setdefault(norm_color(R[name]), p)
    if D.get(name):
        role_alias["dark"].setdefault(norm_color(D[name]), p)


def semcolor(raw, src, desc, theme="light"):
    alias = role_alias[theme].get(norm_color(raw))
    value = f"{{{alias}}}" if alias else norm_color(raw)
    return lit(value, "color", src + (f"; matches declared {alias}" if alias else ""), desc)


sem, dsem = SPEC["light"], SPEC["dark"]
for root, theme, key, comp, state, prop, group, desc in [
    (sem, "light", "ink", "hero-h1", "default", "color", "text",
     "The near-black ink on display copy, headings and card text."),
    (sem, "light", "nav-ink", "nav-link", "default", "color", "text",
     "The translucent nav-pill ink."),
    (sem, "light", "cta-fill", "nav-cta", "default", "backgroundColor", "action",
     "The dark fill of the 'Talk to our team' pill CTAs."),
    (sem, "light", "cta-ink", "nav-cta", "default", "color", "action",
     "The white text on the dark CTA pill."),
    (sem, "light", "cta-outline", "hero-cta2", "default", "insetShadowColor", "border",
     "The translucent inset ring of the 'Explore our platform' secondary pill — a 1px inset shadow; its border-width is 0."),
    # Read from nav-link, whose focus-visible paints a 2px solid outline:
    # nav-menu-btn's focus-visible outline is none/0px with no shadow, so its
    # outlineColor was never painted.
    (sem, "light", "focus-ring", "nav-link", "focus-visible", "_ring", "border",
     "The brand-green keyboard focus ring (focus-visible:outline-control-focus-ring)."),
    (sem, "light", "stat-ink", "stat-card", "default", "color", "text",
     "The stat-card figure ink."),
    (dsem, "dark", "panel", "dark-showcase", "default", "backgroundColor", "background",
     "The near-black showcase panel fill inside the light page."),
    (dsem, "dark", "ink", "demo-card", "default", "color", "text",
     "The brand-green label ink inside the dark showcase (the demo diagram's PRODUCING/CHARGING/BALANCING metrics)."),
]:
    try:
        if prop == "color":
            # The element's own `color` is often inherited onto an unpainted
            # wrapper; the kit's first-text-node reading is the painted ink.
            raw = ts(comp, state, "color")
            src = f"computed color of {comp} {state} — the first text node's reading where the kit recorded one (raw/components-computed.json)"
        elif prop == "_ring":
            if C[comp]["states"][state].get("via") == "focus failed":
                raise KeyError("focus failed")
            raw, how = painted_ring(st(comp, state))
            src = f"computed focus ring ({how}) of {comp} {state} (raw/components-computed.json)"
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
        gap(f"{theme}.{group}.{key}: no {comp} {state} {prop} reading")

# The mint page field: <html> sets --color-page-background:var(--color-brand-75)
# inline, so the whole light page paints brand-75 rather than
# --color-background-primary.
if declared("--color-brand-75") is not None:
    sem.setdefault("background", {})["page"] = lit(
        "{color.brand.75}", "color",
        "the <html> element's inline style --color-page-background:var(--color-brand-75); visible as the mint field behind every marketing page (screenshots/home-light-*.png)",
        "The mint page field — brand-75, set inline on <html>.")

# ------------------------------------------------------------- type ramp
#
# One measured step per headline: the hero masthead aliases the declared
# 68px --text-masthead it matches.

size_alias = {}
for name in sorted(k for k in R if re.fullmatch(r"--text-[a-z0-9]+(-[a-z0-9]+)*", k)):
    size_alias.setdefault(R[name], (f"font.size.{name[len('--text-'):]}", name))
measured_size = {}
for key, comp, state, desc in [
    ("masthead", "hero-h1", "default", "The 68px hero masthead — aliases --text-masthead."),
    ("body", "stat-card", "default", "The stat-card copy size."),
]:
    try:
        raw = st(comp, state)["fontSize"]
        src = f"computed fontSize of {comp} {state} (raw/components-computed.json)"
        alias = size_alias.get(raw)
        SPEC["core"].setdefault("font", {}).setdefault("size", {}).setdefault("measured", {})[key] = lit(
            f"{{{alias[0]}}}" if alias else raw, "dimension",
            src + (f"; matches declared {alias[1]}" if alias else ""), desc)
        measured_size[key] = raw
    except KeyError:
        gap(f"font.size.measured.{key}: no {comp} {state} fontSize reading")

# ------------------------------------------------------------------ shape

for key, comp, state, prop, desc in [
    ("cta", "nav-cta", "default", "borderTopLeftRadius", "The fully-rounded CTA pill radius (radius-full)."),
    ("navPill", "nav-link", "default", "borderTopLeftRadius", "The 4px nav-pill radius (rounded-sm → radius-sm)."),
    ("menu", "nav-panel", "default", "paint:radius", "The mega-menu panel corner radius — read from the painted rounded-lg child; the wrapper itself is unrounded."),
    ("statCard", "stat-card", "default", "borderTopLeftRadius", "The stat-card corner radius."),
    ("field", "field-firstname", "default", "borderTopLeftRadius", "The contact field radius."),
]:
    try:
        if prop == "paint:radius":
            v = norm_len(painted(comp, state, "radius"))
            src = f"the painted radius of {comp}'s rounded child {state} (raw/components-computed.json paint list)"
        else:
            v = norm_len(st(comp, state)[prop])
            src = f"computed {prop} of {comp} {state} (raw/components-computed.json)"
        dkey = radius_alias.get(v)
        if dkey:
            radii[key] = lit(f"{{radius.{dkey}}}", "dimension", src + f"; matches declared --radius-{dkey}", desc)
        else:
            radii[key] = lit(v, "dimension" if re.fullmatch(r"[0-9.]+(px|rem)", v or "") else "other", src, desc)
    except KeyError:
        gap(f"radius.{key}: no {comp} {state} {prop} reading")

# ------------------------------------------------------------------ motion

mo = SPEC["core"].setdefault("motion", {})
try:
    # Each property paired with its own duration/easing by index: appending
    # the whole duration/easing lists after every property gives an invalid
    # shorthand once either list has more than one entry.
    val = transition(st("nav-cta", "default"))
    if val:
        mo["control"] = lit(val, "other",
            "computed transition of nav-cta default (raw/components-computed.json); the declared --default-transition-duration/.4-0-.2-1 pair",
            "The 0.15s transition on pills and controls.")
    else:
        gap("motion.control: nav-cta default has no transition")
except KeyError:
    gap("motion.control: no nav-cta default reading")

# ------------------------------------------------------------- components

comp = SPEC["component"]
for name, cname, state, prop, ty_, desc in [
    ("topbar-height", "mkt-header", "default", "h", "dimension", "The 58px marketing header bar."),
    ("logo-width", "mkt-logo", "default", "w", "dimension", "The ~82px Enode wordmark."),
    ("nav-pill-height", "nav-link", "default", "h", "dimension", "The 34px nav pills."),
    ("cta-height", "nav-cta", "default", "h", "dimension", "The 32px CTA pills."),
    ("mega-menu-width", "nav-panel", "default", "w", "dimension", "The open mega-menu panel width."),
    ("mega-menu-height", "nav-panel", "default", "h", "dimension", "The open mega-menu panel height."),
    ("hero-masthead-width", "hero-h1", "default", "w", "dimension", "The hero masthead measure (max-w)."),
    ("stat-card-width", "stat-card", "default", "w", "dimension", "The stat-card width."),
    ("stat-card-height", "stat-card", "default", "h", "dimension", "The stat-card height."),
    ("showcase-height", "dark-showcase", "default", "h", "dimension", "The dark showcase panel height on the home hero."),
    ("field-height", "field-firstname", "default", "h", "dimension", "The 48px contact field height."),
    ("textarea-height", "field-inquiry", "default", "h", "dimension", "The ~100px inquiry textarea height."),
    ("send-width", "send-btn", "default", "w", "dimension", "The 'Send message' pill width."),
    ("visual-frame-width", "visual-frame", "default", "w", "dimension", "The product visual-frame tile width."),
    ("mobile-topbar-height", "m-topbar", "default", "h", "dimension", "The 60px phone top bar."),
    ("mobile-menu-size", "m-menu-btn", "default", "w", "dimension", "The 36px round mobile menu button."),
]:
    try:
        v = rc(cname, state, prop)
        comp[name] = lit(("%g" % v) + "px" if isinstance(v, (int, float)) else str(v) + "px",
                         ty_, f"measured {prop} of {cname} {state} (raw/components-computed.json)", desc)
    except KeyError:
        gap(f"component.{name}: no {cname} {state} {prop} reading")

# The platform login is a separate app outside the marketing token layer;
# its measured values are kept as literals, honestly labelled.
login = comp.setdefault("login", {})
for name, cname, state, prop, ty_, desc in [
    ("panel-width", "login-panel", "default", "w", "dimension", "The 600px light sign-in panel."),
    ("panel-height", "login-panel", "default", "h", "dimension", "The panel height."),
    ("panel-ink", "login-panel", "default", "color", "color", "The panel ink — the login form side paints light."),
    ("field-bg", "login-field", "default", "backgroundColor", "color", "The white e-mail field fill."),
    ("field-ink", "login-field", "default", "color", "color", "The field text ink."),
    ("field-height", "login-field", "default", "h", "dimension", "The e-mail field height."),
    ("submit-fill", "login-submit", "default", "backgroundColor", "color", "The dark 'Log in' button fill."),
    ("submit-ink", "login-submit", "default", "color", "color", "The button text."),
    ("submit-height", "login-submit", "default", "h", "dimension", "The button height."),
    ("sso-ink", "login-sso", "default", "color", "color", "The 'Continue with SAML SSO' link ink."),
]:
    try:
        if prop in ("w", "h"):
            v = rc(cname, state, prop)
            login[name] = lit(("%g" % v) + "px", ty_, f"measured {prop} of {cname} {state} on platform.enode.com/login (raw/components-computed.json)", desc)
        else:
            login[name] = semcolor(st(cname, state)[prop],
                f"computed {prop} of {cname} {state} on platform.enode.com/login (raw/components-computed.json)", desc)
    except KeyError:
        gap(f"component.login.{name}: no {cname} {state} {prop} reading")

# Rows missing from the committed readings, kept visible in `_gaps`.
KNOWN_GAPS = set()
_new = [g for g in GAPS if g not in KNOWN_GAPS]
if _new:
    raise SystemExit("missing readings for named token rows (recapture, or list them in KNOWN_GAPS):\n  " + "\n  ".join(_new))
if GAPS:
    SPEC["_gaps"] = GAPS

(RAW / "component-tokens.json").write_text(json.dumps(SPEC, indent=2, ensure_ascii=False) + "\n")
print("component-tokens.json:", {k: len(v) for k, v in SPEC.items() if k != "_about"})
