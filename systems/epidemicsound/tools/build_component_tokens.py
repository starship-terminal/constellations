#!/usr/bin/env python3
"""Write raw/component-tokens.json, the token spec build_tokens.py reads.

epidemicsound.com is two surfaces signed out: the alternative-light (ecru)
marketing shell on /, /pricing/, /music/, /sound-effects/ and /how-it-works/,
and the dark catalog shell on /music/genres/*, /music/themes/*, /artists/*
and /sound-effects/categories/* — plus the dark Keycloak account forms on
login.epidemicsound.com. The site declares a real design-token layer outright
(raw/css-vars.json): 151 semantic --es-color-* roles (action/background/
border/icon/input/misc/platform/text/track + brand and data-viz palettes),
--es-heading-*/--es-subheading-*/--es-text-* type scales, --es-radius-*,
--es-elevation-*, --es-grid-*, --es-play-button-size-*, --es-trackrow-*,
--es-i-*/--es-button-*/--es-header-font-family internals, the
--es-text-font-family/--es-header-font-family stacks (Inter + Sebenta),
Tailwind --font-weight-*/--radius-*/--ease-*/--breakpoint-*/--container-*
and --spacing. The colour roles switch value between themes so every
--es-color-* is emitted under both light.* and dark.* as a {"var": ...}
leaf; the type/space/shape/motion scales are theme-invariant and land
under core.*.

The radius story needs noting: :root declares --es-radius-small 2px /
medium 4px / large 8px / circle 10000px, `body` zeroes every radius, and
the `radii-override` class every shipped page carries re-enables
button 10000px (pill), surface 16px, element 8px, detail 4px, tiny 2px —
the resolved values below are the radii-override ones, so buttons are
full pills while small/medium/large stay 0.

Measured computed styles from raw/components-computed.json:

  light       #000000 ink and primary fills on the #f1f0eb ecru field,
              rgba(61,77,116,.12) secondary buttons, #000 focus ring
  dark        #121418 canvas, rgba(207,214,229,.08) surfaces, #ffffff
              text and primary fills, #20afff focus, #ff82c2 brand pink
              on the genre banner
  fonts       Sebenta (all display headings, 500) and Inter (UI text)
  ramp        declared heading 20/24/32/40/48/64/80/128, text 12-18,
              button 12/14/16, subheading 14/16/20
  shape       pill buttons, 16px surfaces, 8px elements, 4px details
"""

import json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
V = json.loads((RAW / "css-vars.json").read_text())
# The light set is what the marketing pages paint: alternative-light.
RL = V.get("resolved", {}).get("alternativeLight", {})
RD = V.get("resolved", {}).get("dark", {})
C = json.loads((RAW / "components-computed.json").read_text())["components"]
R = {n: (v.get("value", v.get("raw")) if isinstance(v, dict) else v) for n, v in RL.items()}
D = {n: (v.get("value", v.get("raw")) if isinstance(v, dict) else v) for n, v in RD.items()}


def var(name, ty="color", **kw):
    d = {"var": name, "type": ty}
    d.update(kw)
    return d


SPEC = {"_about": (
    "The token tree build_tokens.py turns into tokens.json. epidemicsound.com "
    "declares its design-token layer in its stylesheets "
    "(raw/css-vars.json): theme-invariant scales under core.* and the "
    "semantic --es-color-* layer emitted under both light.* and dark.* so "
    "each theme resolves its own value. Measured roles alias to the "
    "declared values where they match."),
    "core": {}, "light": {}, "dark": {}, "component": {}}


# A named row whose reading is missing is recorded here instead of being
# dropped silently; the build stops on any gap not listed in KNOWN_GAPS (at the
# end), and listed ones are written to raw/component-tokens.json `_gaps`.
GAPS = []


def gap(what):
    GAPS.append(what)


HAND = "entered by hand at capture time, not measured: "


def body_fill(comp, state):
    """The <body> fill among a component's recorded ancestors."""
    return next(a["bg"] for a in C[comp]["states"][state].get("ancestors") or []
                if a.get("node", "").startswith("body") and a.get("bg"))


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


EMITTED = {}   # emitted name -> dotted token path it was actually written to
_OWNER = {}    # dotted token path -> emitted name holding it


def _leaf(d):
    return isinstance(d, dict) and ("var" in d or "value" in d)


def emit(root, name, leaf):
    """Write `leaf` at name's dotted path.

    `name` is the emitted (possibly rewritten) name — the path is built from
    it, while `leaf["var"]` holds the real stylesheet variable. A leaf and a
    group can share a node; the leaf moves under `default`/`base`/`self`.
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


DECL_SRC = "declared Epidemic Sound design-system variable in the site stylesheet (raw/css-vars.json)"


def decl(name, ty="dimension", bag=R):
    v = bag[name]
    if ty == "dimension" and not re.fullmatch(r"-?\d+(\.\d+)?(px|rem)", str(v).strip()):
        ty = "other"
    return lit(v, ty, f"{DECL_SRC}: {name}", f"The declared `{name}`.")


COLOR_V = re.compile(r"(#[0-9a-fA-F]{3,8}|rgba?\([^)]*\)|hsla?\([^)]*\)|(ok)?lab\([^)]*\)|(ok)?lch\([^)]*\))")


def decl_color(name, bag=R):
    v = bag[name]
    ty = "color" if COLOR_V.fullmatch(str(v).strip()) else "other"
    return lit(v, ty, f"{DECL_SRC}: {name}", f"The declared `{name}`.")


# ------------------------------------------------------------------- fonts
#
# ES ships two families: Inter for every UI control and body text, Sebenta
# (500 with serif fallbacks) for every heading — declared as
# --es-text-font-family and --es-header-font-family, mirrored under
# --es-i-*/--pds-* internal aliases.

fam = SPEC["core"].setdefault("font", {}).setdefault("family", {})
for key, name, desc in [
    ("ui", "--es-text-font-family", "The declared Inter stack — every UI control, body and meta text (aliases --es-i-text-font-family, --pds-font-primary)."),
    ("display", "--es-header-font-family", "The declared Sebenta stack — every es-heading/es-subheading and the h1-h6 layer (alias --es-i-header-font-family)."),
]:
    if name in R:
        fam[key] = var(name, "fontFamily", description=desc)

weights = SPEC["core"].setdefault("font", {}).setdefault("weight", {})
for key, comp, desc in [
    ("regular", "track-row", "400 — the es-text-xs meta weight; body text sits at 500."),
    ("medium", "genre-h1", "500 — every es-heading, es-subheading-l, es-text-l/xl/m/s and buttons' base weight."),
    ("semibold", "btn-signup", "600 — es-text-button-*, es-subheading-s/m and the overlines."),
    ("bold", None, "700 — declared --font-weight-bold; used by utility text, not the es-* scales."),
]:
    if comp is None:
        if "--font-weight-bold" in R:
            weights[key] = decl("--font-weight-bold", "fontWeight")
        continue
    try:
        # The element's own fontWeight, not ts(): a row's textStyle is its
        # semibold title span, which would mislabel the 400 row as 600.
        w = int(float(st(comp, "default")["fontWeight"]))
        weights[key] = lit(w, "fontWeight",
                           f"computed fontWeight of {comp} default (raw/components-computed.json)", desc)
    except (KeyError, TypeError, ValueError):
        pass
weights["declared"] = {}
for name in sorted(k for k in R if k.startswith("--font-weight-")):
    weights["declared"][name[len("--font-weight-"):]] = decl(name, "fontWeight")
if not weights["declared"]:
    del weights["declared"]

# ------------------------------------------------- declared scales (es-*)
#
# Type scales: --es-heading-*, --es-subheading-*, --es-text-* each declare
# font-size/line-height/letter-spacing/font-weight per step. They are
# theme-invariant and land under core.font.

PROP_MAP = {"font-size": "size", "font-weight": "weight",
            "line-height": "lineHeight", "letter-spacing": "tracking"}
for name in sorted(R):
    m = re.fullmatch(r"--es-(heading|subheading|text)-(.*?)-(font-size|font-weight|line-height|letter-spacing)", name)
    if not m:
        continue
    group, step, prop = m.groups()
    bag = SPEC["core"].setdefault("font", {}).setdefault(PROP_MAP[prop], {}).setdefault(group, {})
    ty = {"size": "dimension", "weight": "fontWeight", "lineHeight": "dimension", "tracking": "other"}[PROP_MAP[prop]]
    leaf = decl(name, ty)
    if PROP_MAP[prop] == "weight":
        leaf["type"] = "fontWeight"
        try:
            leaf["value"] = int(float(leaf["value"]))
        except (TypeError, ValueError):
            pass
    bag[step] = leaf

# Radii — resolved under the radii-override class the shipped pages carry.
radii = SPEC["core"].setdefault("radius", {})
for name in sorted(k for k in R if k.startswith("--es-radius-")):
    radii[name[len("--es-radius-"):]] = decl(name)
RADII_NOTE = ("Resolved under `radii-override` (raw/css-vars.json): :root declares "
              "2/4/8/10000px, body zeroes every radius, and radii-override re-enables "
              "the values below — buttons are 10000px pills while small/medium/large stay 0.")
for name in radii:
    radii[name]["source"] += "; " + RADII_NOTE

# Elevation, grid, borders, tracks, play-button sizes, internals.
for name in sorted(k for k in R if k.startswith("--es-elevation-")):
    SPEC["core"].setdefault("elevation", {})[name[len("--es-elevation-"):]] = decl(name, "other")

grid = SPEC["core"].setdefault("grid", {})
for name in sorted(k for k in R if k.startswith("--es-grid-")):
    rest = name[len("--es-grid-"):]
    if "-" in rest:
        g, k2 = rest.split("-", 1)
        grid.setdefault(g, {})[k2] = decl(name)
    else:
        grid[rest] = decl(name)
if "--full-page-grid-max-width" in R:
    grid.setdefault("page", {})["maxWidth"] = decl("--full-page-grid-max-width")

for name in sorted(k for k in R if k.startswith("--es-border-width-")):
    SPEC["core"].setdefault("border", {}).setdefault("width", {})[name[len("--es-border-width-"):]] = decl(name)

# Tailwind-layer utility scales the site also declares.
for name in sorted(k for k in R if re.fullmatch(r"--radius-(sm|md|lg|xl|\d+xl)", k)):
    SPEC["core"].setdefault("radius", {}).setdefault("tailwind", {})[name[len("--radius-"):]] = decl(name)
if "--spacing" in R:
    SPEC["core"].setdefault("spacing", {})["unit"] = decl("--spacing")
for name in sorted(k for k in R if k.startswith("--container-")):
    SPEC["core"].setdefault("container", {})[name[len("--container-"):]] = decl(name)
for name in sorted(k for k in R if k.startswith("--breakpoint-")):
    SPEC["core"].setdefault("breakpoint", {})[name[len("--breakpoint-"):]] = decl(name)
for name in sorted(k for k in R if k.startswith("--blur-")):
    SPEC["core"].setdefault("blur", {})[name[len("--blur-"):]] = decl(name)

easing = SPEC["core"].setdefault("easing", {})
for name in sorted(k for k in R if k.startswith("--ease-")):
    easing[name[len("--ease-"):]] = decl(name, "cubicBezier")

for name in sorted(k for k in R if k.startswith(("--animate-", "--animation-", "--default-transition-"))):
    ty = "duration" if name.endswith("duration") else ("cubicBezier" if name.endswith("timing-function") else "other")
    emit(SPEC["core"], "--motion" + name[1:], decl(name, ty))

# brand black/white declared at :root (the Tailwind-layer twins of the
# --es-color-brand-off-* tokens)
for name in sorted(k for k in R if re.fullmatch(r"--color-brand-(black|white)", k)):
    emit(SPEC["core"], name, decl_color(name))

# ------------------------------------------- per-theme semantic variables
#
# Every --es-color-* switches between the alternative-light marketing theme
# and the dark catalog theme — emitted under both sets so each resolves its
# own value. A few (the overlay fade gradients) only resolve in one pass and
# are emitted under the set that has them.

for root, bag in ((SPEC["light"], R), (SPEC["dark"], D)):
    for name in sorted(k for k in bag if k.startswith("--es-color-")):
        emitted = name.replace("--es-color-", "--color-")
        ty = "color" if decl_color(name, bag)["type"] == "color" else "other"
        emit(root, emitted, var(name, ty))

# ------------------------------------------------ measured semantic roles
#
# Roles measured on the painted surfaces; each aliases to the declared
# --es-color-* token whose per-theme value it matches.

role_alias = {"light": {}, "dark": {}}
for theme, bag in (("light", R), ("dark", D)):
    for name in sorted(k for k in bag if k.startswith("--es-color-")):
        emitted = name.replace("--es-color-", "--color-")
        if emitted in EMITTED:
            role_alias[theme].setdefault(norm_color(bag[name]), EMITTED[emitted])
# colour-invariant tokens can still alias through core emits (brand b/w)
for theme in ("light", "dark"):
    for name in ("--color-brand-black", "--color-brand-white"):
        if name in R:
            role_alias[theme].setdefault(norm_color(R[name]), EMITTED.get("--color-brand-" + name[len("--color-brand-"):]))


def semcolor(raw, src, desc, theme="light"):
    alias = role_alias[theme].get(norm_color(raw))
    value = f"{{{alias}}}" if alias else norm_color(raw)
    return lit(value, "color", src + (f"; matches declared {alias}" if alias else ""), desc)


sem = SPEC["light"]
dsem = SPEC["dark"]
desc_reason = {
    "divider": "no measured border paints it (rgba(207,214,229,.16) appears only as icon-button pressed fills)",
    "liked": "no liked-state icon was measured (the value equals the genre banner's pink)",
}
for root, theme, key, comp, state, prop, group, desc in [
    (sem, "light", "page", "header", "default", "_body", "background",
     "The ecru field every marketing page paints (alternative-light)."),
    (sem, "light", "ink", "hero-h1", "default", "color", "text",
     "The #000 ink — display headings and body text on ecru."),
    (sem, "light", "muted", "section-h2", "default", "_paint-muted", "text",
     "The rgba(0,0,0,.6) secondary text on the light surface."),
    (sem, "light", "primary", "btn-signup", "default", "backgroundColor", "action",
     "The #000 primary button fill (inverse of the light surface)."),
    (sem, "light", "primary-hover", "btn-signup", "hover", "backgroundColor", "action",
     "The #272727 the light primary fill lifts to on hover."),
    (sem, "light", "secondary", "btn-login", "default", "backgroundColor", "action",
     "The rgba(61,77,116,.12) secondary button fill."),
    (sem, "light", "secondary-hover", "btn-login", "hover", "backgroundColor", "action",
     "The rgba(61,77,116,.18) secondary fill on hover."),
    (sem, "light", "focus", "nav-pricing", "focus-visible", "outlineColor", "border",
     "The #000 focus ring the light surface draws on keyboard focus."),
    (sem, "light", "switch", "billing-switch", "default", "backgroundColor", "action",
     "The plan-period switch track on pricing."),
    (dsem, "dark", "canvas", "c-header", "default", "_body", "background",
     "The #121418 dark canvas every catalog page and the account forms paint."),
    (dsem, "dark", "surface", "sfx-row", "hover", "backgroundColor", "background",
     "The rgba(207,214,229,.08) surface tint — cards, hover fills, the want-more strip edges."),
    (dsem, "dark", "text", "genre-h1", "default", "_paint-text", "text",
     "The #fff primary text (genre h1 prints dark on its pink banner, so the row text carries this)."),
    (dsem, "dark", "muted", "track-row", "default", "_paint-muted", "text",
     "The rgba(255,255,255,.72) secondary text on dark."),
    (dsem, "dark", "primary", "c-signup", "default", "backgroundColor", "action",
     "The #fff primary button fill on dark (inverse of the canvas)."),
    (dsem, "dark", "primary-hover", "c-signup", "hover", "backgroundColor", "action",
     "The #e7e7e7 the dark primary fill dims to on hover."),
    (dsem, "dark", "secondary", "btn-login", "default", "_paint-secondary", "action",
     "The rgba(207,214,229,.16) secondary button fill on dark."),
    (dsem, "dark", "focus", "nav-pricing", "focus-visible", "_paint-focus", "border",
     "The #20afff azur focus ring the dark surface draws."),
    (dsem, "dark", "accent", "genre-banner", "default", "backgroundColor", "action",
     "The #ff82c2 brand pink — the genre banner fill and action-accent."),
    (dsem, "dark", "divider", None, "default", "rgba(207, 214, 229, 0.16)", "border",
     "The rgba(207,214,229,.16) hairline divider on dark."),
    (dsem, "dark", "liked", None, "default", "#ff82c2", "action",
     "The #ff82c2 liked state — icon-liked and the pink accent."),
    (dsem, "dark", "upsell", "wantmore", "default", "_paint-upsell", "background",
     "The #ff82c2 pink 'Want more music?' card inside the dark catalog."),
]:
    try:
        prefer = None
        if prop.startswith("_paint"):
            raw = None
        elif prop.startswith("#") or prop.startswith("rgba"):
            raw = prop
            prop = "_literal"
        elif prop == "_body":
            raw = None
        else:
            raw = st(comp, state)[prop]
        if prop == "_literal":
            # No reading in raw/ holds these: say so rather than cite screenshots.
            src = HAND + f"{desc_reason.get(key, 'no component in raw/ paints it')}; recapture needed"
        elif prop == "_body":
            raw = body_fill(comp, state)
            src = f"computed body fill among the ancestors of {comp} {state} (raw/components-computed.json)"
        elif prop == "_paint-muted":
            # The secondary text is a painted text layer whose colour differs
            # from the component's own (primary) ink: picked by role, not by
            # matching the expected value.
            own = (C[comp]["states"][state].get("textStyle") or {}).get("color") or st(comp, state)["color"]
            raw = next(pl["color"] for pl in C[comp]["states"][state].get("paint") or [] if pl.get("color") and pl["color"] != own)
            src = f"painted secondary text colour inside {comp} {state} (raw/components-computed.json)"
        elif prop == "_paint-text":
            # The first text node's colour: the row's primary ink.
            raw = C["track-row"]["states"]["default"]["textStyle"]["color"]
            src = "computed first text node colour of track-row default (raw/components-computed.json)"
        elif prop == "_paint-secondary":
            # No dark secondary button was measured (every dark icon button is
            # a transparent ghost), so the role resolves to its declaration —
            # measuring track-like would alias the ghost's zero-opacity fill.
            raw = D.get("--es-color-action-secondary")
            prefer = EMITTED.get("--color-action-secondary")
            src = "declared --es-color-action-secondary (raw/css-vars.json)"
        elif prop == "_paint-focus":
            # track-like's focus-visible draws the real 2px solid #20afff azur
            # ring; track-play's own focus-visible only reports the album-cover
            # button's 1px auto fallback outline (#101010), so it is not read.
            raw = st("track-like", "focus-visible").get("outlineColor") or st("track-like", "focus-visible").get("borderTopColor")
            src = "computed focus outline of a dark-surface icon button (raw/components-computed.json)"
        elif prop == "_paint-upsell":
            # The banner is the largest painted layer inside the component.
            def area(pl):
                # "1328.0x244.0" for elements, "32pxx16px" for ::before/::after
                n = [float(x) for x in re.findall(r"[\d.]+", pl.get("size") or "")[:2]]
                return n[0] * n[1] if len(n) == 2 else 0.0
            raw = max((pl for pl in C[comp]["states"][state].get("paint") or [] if pl.get("bg")), key=area)["bg"]
            src = f"painted banner fill (the largest painted layer) inside {comp} {state} (raw/components-computed.json)"
        else:
            raw = st(comp, state)[prop]
            src = f"computed {prop} of {comp} {state} (raw/components-computed.json)"
        if raw:
            # A declared role of the same name and value wins over a
            # coincidental value match: action.secondary aliases
            # color.action.secondary.default, not the ghost that shares it.
            if prefer is None:
                declvar = f"--es-color-{group}-{key}"
                bag = {"light": R, "dark": D}[theme]
                if declvar in bag and norm_color(bag[declvar]) == norm_color(raw):
                    prefer = EMITTED.get(declvar.replace("--es-color-", "--color-"))
            root.setdefault(group, {})[key] = (lit(f"{{{prefer}}}", "color", f"{src}; declared as {prefer}", desc)
                                             if prefer else semcolor(raw, src, desc, theme))
        else:
            gap(f"{theme}.{group}.{key}: {comp} {state} {prop} is empty")
    except (KeyError, StopIteration, ValueError):
        gap(f"{theme}.{group}.{key}: no {comp} {state} {prop} reading")

# ------------------------------------------------------------- type ramp
#
# Measured sizes alias to the declared --es-* scale step they match.

size_alias = {}
for name in R:
    m = re.match(r"--es-(heading|subheading|text)-(.*?)-font-size$", name)
    if m:
        size_alias.setdefault(R[name], (f"font.size.{m.group(1)}.{m.group(2)}", name))

ty = SPEC["core"].setdefault("font", {}).setdefault("size", {}).setdefault("measured", {})
for key, comp, state, desc in [
    ("button-s", "btn-signup", "default", "The 14px es-text-button-s header button label."),
    ("h1-genre", "genre-h1", "default", "The 40px es-heading-m genre page heading."),
    ("h1-pricing", "pr-h1", "default", "The 64px es-heading-xl pricing heading."),
    ("h1-home", "hero-h1", "default", "The home hero display heading size."),
    ("plan-name", "plan-name", "default", "The 20px es-subheading-l plan name."),
    ("kc-h1", "kc-h1", "default", "The Keycloak login heading size."),
]:
    try:
        raw = st(comp, state)["fontSize"]
        src = f"computed fontSize of {comp} {state} (raw/components-computed.json)"
        alias = size_alias.get(raw)
        ty[key] = lit(f"{{{alias[0]}}}" if alias else raw, "dimension",
                      src + (f"; matches declared {alias[1]}" if alias else ""), desc)
    except KeyError:
        gap(f"font.size.measured.{key}: no {comp} {state} fontSize reading")
if not ty:
    SPEC["core"]["font"]["size"].pop("measured", None)

# ------------------------------------------------------------------ shape

radius_alias = {R[n]: n for n in R if n.startswith("--es-radius-")}
for key, comp, state, prop, desc in [
    ("measured-pill", "btn-signup", "default", "borderTopLeftRadius", "The measured button radius — 10000px pill under radii-override."),
    ("measured-surface", "genre-banner", "default", "borderTopLeftRadius", "The genre banner's surface radius."),
    ("measured-detail", "track-play", "default", "borderTopLeftRadius", "The track-play cover's detail radius."),
]:
    try:
        v = st(comp, state)[prop]
        src = f"computed {prop} of {comp} {state} (raw/components-computed.json)"
        dkey = radius_alias.get(v)
        if dkey:
            radii[key] = lit(f"{{radius.{dkey[len('--es-radius-'):]}}}", "dimension", src + f"; matches declared {dkey}", desc)
        else:
            radii[key] = lit(v, "dimension" if re.fullmatch(r"[0-9.]+(px|rem)", v or "") else "other", src, desc)
    except KeyError:
        gap(f"radius.{key}: no {comp} {state} {prop} reading")

# ------------------------------------------------------------------ motion

try:
    # Each property paired with its own duration/easing by index.
    val = transition(st("c-signup", "default"))
    if val:
        mo = SPEC["core"].setdefault("motion", {})
        emit(SPEC["core"], "--motion-control", lit(val, "other",
            "computed transition of c-signup default (raw/components-computed.json)",
            "The measured control transition on buttons."))
    else:
        gap("motion.control: c-signup default has no transition")
except KeyError:
    gap("motion.control: no c-signup default reading")

# ------------------------------------------------------------- components

comp = SPEC["component"]
for name, cname, state, prop, ty_, desc in [
    ("header-height", "header", "default", "h", "dimension", "The 100px sticky site header."),
    ("track-row-height", "track-row", "default", "h", "dimension", "The 56px track row — matches declared --es-trackrow-size."),
    ("track-play-size", "track-play", "default", "w", "dimension", "The 56px album-cover play button — matches --es-play-button-size-m."),
    ("icon-button", "track-like", "default", "h", "dimension", "The 44px ghost icon button on track rows."),
    ("nav-button-height", "nav-pricing", "default", "h", "dimension", "The 44px header control height."),
    ("login-card-width", "kc-card", "default", "w", "dimension", "The Keycloak form card width."),
    ("login-field-height", "kc-email", "default", "h", "dimension", "The Keycloak input height."),
    ("login-submit-height", "kc-submit", "default", "h", "dimension", "The Keycloak primary button height."),
    ("billing-switch", "billing-switch", "default", "w", "dimension", "The plan-period switch track width."),
    ("mobile-header-height", "m-header", "default", "h", "dimension", "The phone top bar height."),
    ("genre-banner-height", "genre-banner", "default", "h", "dimension", "The genre banner card height."),
]:
    try:
        v = rc(cname, state, prop)
        comp[name] = lit(("%g" % v) + "px" if isinstance(v, (int, float)) else str(v) + "px",
                         ty_, f"measured {prop} of {cname} {state} (raw/components-computed.json)", desc)
    except KeyError:
        gap(f"component.{name}: no {cname} {state} {prop} reading")

# Declared component internals (--es-trackrow-*, --es-play-button-size-*,
# --es-i-*, --es-button-*, --es-select-*, --es-dropdown-*, --es-iconbutton-*,
# --es-header-font-family): resolved values where they exist, and every
# remaining declared name under its own group with the declared value.
DECL_ONLY = {}
for r in V.get("theme", []):
    sel = r.get("selector") or ""
    for n, v in (r.get("properties") or {}).items():
        if n.startswith("--es-") and n not in R:
            DECL_ONLY.setdefault(n, v)
        elif n.startswith("--es-"):
            DECL_ONLY.setdefault(n, None)  # resolved elsewhere

for name in sorted(k for k in R if k.startswith("--es-trackrow-")):
    emit(comp, name.replace("--es-trackrow-", "--trackrow-"), decl(name))
for name in sorted(k for k in R if k.startswith("--es-play-button-size-")):
    emit(comp, name.replace("--es-play-button-size-", "--play-"), decl(name))
for name in sorted(k for k in R if k.startswith("--es-i-")):
    emit(comp, name.replace("--es-i-", "--i-"), decl(name, "other"))
for name in sorted(DECL_ONLY):
    if DECL_ONLY[name] is None or name in R:
        continue
    rest = name[len("--es-"):].replace("-", ".")
    ty = "other"
    v = DECL_ONLY[name]
    leaf = lit(v, ty, f"{DECL_SRC}: {name} (component-scoped declaration, not :root-resolved)", f"The declared `{name}`.")
    emit(comp, "--declared-" + name[len("--es-"):], leaf)

# Rows missing from the committed readings, kept visible in `_gaps` (they
# were dropped silently before 2026-11): no measured component paints the
# muted text as its own layer, and c-signup's computed transition is 0s.
KNOWN_GAPS = {
    "light.text.muted: no section-h2 default _paint-muted reading",
    "dark.text.muted: no track-row default _paint-muted reading",
    "motion.control: c-signup default has no transition",
}
_new = [g for g in GAPS if g not in KNOWN_GAPS]
if _new:
    raise SystemExit("missing readings for named token rows (recapture, or list them in KNOWN_GAPS):\n  " + "\n  ".join(_new))
if GAPS:
    SPEC["_gaps"] = GAPS

(RAW / "component-tokens.json").write_text(json.dumps(SPEC, indent=2, ensure_ascii=False) + "\n")
print("component-tokens.json:", {k: len(v) for k, v in SPEC.items() if k != "_about"})
