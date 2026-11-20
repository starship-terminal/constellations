#!/usr/bin/env python3
"""Write raw/component-tokens.json, the token spec build_tokens.py reads.

www.framer.com is itself a Framer site whose declared design-token layer is
the project's colour styles: ~576 `--token-<uuid>` custom properties declared
on `body` (raw/css-vars.json). The uuid names are opaque project ids, not
semantic roles — and they deduplicate hard: 576 declarations collapse to ~68
distinct painted values, the achromatic ramp #000..#fff, the white-alpha and
black-alpha hairlines, the #cbff00 lime and a handful of vivid accents used
in gradient art. This spec therefore publishes one palette token per distinct
resolved value (`palette.neutral-<rr>`, `palette.alpha-white.<pct>`,
`palette.alpha-black.<pct>`, `palette.accent.<name>`), each bound to the
alphabetically-first --token-<uuid> that declares it; the full uuid->value
map stays in raw/css-vars.json.

Sizes, spacing, radii and text styles live inline per element on a Framer
site — they are measured values. Measured roles (header link ink, CTA fill,
page field, plan-card surface) alias to the palette token whose painted
value they match, labelled with the measurement they came from.

The community stack (/community/gallery, /marketplace) and the light auth
shell (/login) are different apps that do not share the --token-* layer;
their values are measured component tokens.

Deterministic: same inputs, byte-identical output.
"""
import json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
V = json.loads((RAW / "css-vars.json").read_text())
R = V.get("resolved", {}).get("dark", {})
C = json.loads((RAW / "components-computed.json").read_text())["components"]

SPEC = {"_about": (
    "The token tree build_tokens.py turns into tokens.json. www.framer.com "
    "declares its design-token layer as ~576 `--token-<uuid>` colour styles "
    "on `body` (raw/css-vars.json) — opaque-named paint styles that "
    "deduplicate to ~68 painted values: the achromatic ramp, white/black "
    "alpha hairlines, the #cbff00 lime and the vivid gradient accents. "
    "Everything else is measured. The dark set is the only surface the "
    "marketing site paints; the community stack is dark too, the /login "
    "auth shell is light. Measured roles alias to the declared values "
    "where they match."),
    "core": {}, "dark": {}, "auth": {}, "component": {}}

# The /login shell is a separate light app that declares none of the www
# --token-* layer: its readings go to the `auth` set, as literals, never into
# `dark` and never aliased to a www palette name that happens to match.
AUTH_COMPONENTS = {"login-email", "login-google", "login-panel"}


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
    """#hex, rgb()/rgba() -> the hex or rgba() the browser paints."""
    v = (v or "").strip()
    m = re.fullmatch(r"#([0-9a-fA-F]{3,8})", v)
    if m:
        h = m.group(1).lower()
        if len(h) in (3, 4):
            h = "".join(c * 2 for c in h)
        return "#" + h[:6]
    m = re.fullmatch(r"rgba?\(([\d.]+),?\s+([\d.]+),?\s+([\d.]+)(?:\s*[,/]\s*([\d.]+%?))?\)", v)
    if m:
        r, g, b, a = m.groups()
        a = 1 if a is None else (float(a[:-1]) / 100 if a.endswith("%") else float(a))
        if a >= 1:
            return "#%02x%02x%02x" % (int(float(r)), int(float(g)), int(float(b)))
        return f"rgba({int(float(r))}, {int(float(g))}, {int(float(b))}, {'%g' % a})"
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


def emit_at(root, path, leaf, name=None):
    """Write `leaf` at a dotted path. A leaf that must share a node with a
    group moves inside it under `default`."""
    node = root
    parts = path.split(".")
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
    full = ".".join(parts)
    if last in node and not _leaf(node[last]):
        for key in ("default", "base", "self"):
            if key not in node[last]:
                node[last][key] = leaf
                full += "." + key
                break
        else:
            raise ValueError(f"{path}: no free key to hold the leaf beside its group")
    else:
        if last in node:
            raise ValueError(f"{path}: duplicate token path")
        node[last] = leaf
    if name:
        EMITTED[name] = full
        _OWNER[full] = name


DECL_SRC = "the Framer project's declared --token-<uuid> colour styles on `body` (raw/css-vars.json)"


def resolved(name):
    e = R.get(name)
    if isinstance(e, dict):
        return e.get("value", e.get("raw"))
    return e


def painted_bg(comp, state):
    """The fill a surface role should publish: the box's own background when it
    paints one, else the nearest recorded ancestor that does. The /login e-mail
    input is transparent — the div wrapping it paints the field — so reading the
    element alone loses the visible fill. Returns (None, None) when neither the
    box nor a recorded ancestor paints, leaving the role unpublished rather than
    exporting a transparent heading as a page surface (the case galBg hits: the
    gallery page's field was never measured)."""
    own = st(comp, state).get("backgroundColor")
    if own and norm_color(own) != "rgba(0, 0, 0, 0)":
        return own, f"computed backgroundColor of {comp} {state} (raw/components-computed.json)"
    for a in C[comp]["states"][state].get("ancestors", []):
        bg = a.get("bg")
        if bg and norm_color(bg) != "rgba(0, 0, 0, 0)":
            return bg, (f"computed backgroundColor of {a['node']}, the ancestor that paints "
                        f"the {comp} {state} fill (raw/components-computed.json)")
    return None, None


def var(name, ty="color", **kw):
    d = {"var": name, "type": ty}
    d.update(kw)
    return d


# ------------------------------------------------ the --token-<uuid> layer
#
# One palette token per distinct resolved value. Achromatic hexes read
# `neutral-<rr>`; white/black alphas read `alpha-white.<pct>` /
# `alpha-black.<pct>`; chromatic paints get a curated colour-word name (the
# name describes the painted colour, not a product role: the uuid names are
# opaque and no semantic mapping can be observed). Every leaf binds the
# alphabetically-first --token-<uuid> declaring the value; the description
# records how many styles share it.

ACCENT_NAMES = {
    "#cbff00": "lime", "#0099ff": "blue", "#6600ff": "violet",
    "#8a58ff": "purple", "#9900ff": "purple-deep", "#ff0066": "rose",
    "#ff0022": "red", "#78a9ff": "sky", "#00de68": "green",
    "#4cd963": "mint", "#22dddd": "cyan", "#f7b95c": "peach",
    "#ffbb00": "amber", "#9da2ad": "slate",
    "#090a0c": "ink", "#17191e": "ink-soft", "#f0f1f3": "paper",
}
TOK = re.compile(r"^--token-[0-9a-f]{8}-")

byval = {}
for name in sorted(k for k in R if TOK.match(k)):
    nv = norm_color(str(resolved(name) or ""))
    if not nv or nv == "none":
        continue
    byval.setdefault(nv, []).append(name)

pal = SPEC["core"].setdefault("color", {}).setdefault("palette", {})
pal["$description"] = ("The Framer project's colour styles, deduplicated: %d `--token-<uuid>` "
                       "properties on `body` resolve to %d distinct values. Names are opaque "
                       "project ids, so each token names its painted colour and binds one "
                       "declaring var; the uuid->value map is raw/css-vars.json." % (
                           sum(len(v) for v in byval.values()), len(byval)))
used = set()
for nv in sorted(byval):
    names = byval[nv]
    rep = names[0]
    m = re.fullmatch(r"#([0-9a-f]{6})", nv)
    if m:
        r, g, b = (int(m.group(1)[i:i + 2], 16) for i in (0, 2, 4))
        if max(r, g, b) - min(r, g, b) <= 4:
            path = "palette.neutral-%02x" % r
        else:
            path = "palette.accent." + ACCENT_NAMES.get(nv, "hue-%02x%02x%02x" % (r, g, b))
    else:
        m = re.fullmatch(r"rgba\((\d+), (\d+), (\d+), ([\d.]+)\)", nv)
        if m:
            r, g, b, a = int(m.group(1)), int(m.group(2)), int(m.group(3)), float(m.group(4))
            if r == g == b == 255:
                path = "palette.alpha-white.%d" % round(a * 100)
            elif r == g == b == 0:
                path = "palette.alpha-black.%d" % round(a * 100)
            else:
                path = "palette.accent.%s-%d" % (ACCENT_NAMES.get("#%02x%02x%02x" % (r, g, b), "mix-%02x%02x%02x" % (r, g, b)), round(a * 100))
        else:
            path = "palette.accent.other"
    if path in used:
        path += "-" + names[0][8:14]
    used.add(path)
    desc = "Declared by %s" % rep
    if len(names) > 1:
        desc += " and %d other --token-<uuid> styles" % (len(names) - 1)
    desc += "; resolves to %s." % nv
    emit_at(SPEC["core"]["color"], path,
            var(rep, "color", description=desc), rep)

# -------------------------------------------- measured roles -> aliases

role_alias = {}
ALIAS_FIRST = [
    "palette.neutral-00", "palette.neutral-11", "palette.neutral-1f",
    "palette.neutral-24", "palette.neutral-2b", "palette.neutral-30",
    "palette.ff", "palette.f3", "palette.99", "palette.66",
    "palette.alpha-white.7", "palette.accent.lime",
]
ALIAS_RANK = {p: i for i, p in enumerate(ALIAS_FIRST)}
cands = {}
for name in sorted(k for k in EMITTED):
    nv = norm_color(str(resolved(name) or ""))
    if not nv:
        continue
    p = EMITTED[name]
    cur = cands.get(nv)
    if cur is None or (ALIAS_RANK.get(p, 99), p) < (ALIAS_RANK.get(cur, 99), cur):
        cands[nv] = p
role_alias = {nv: "color." + p for nv, p in cands.items()}


def semcolor(raw, src, desc):
    nv = norm_color(raw)
    alias = role_alias.get(nv)
    value = "{%s}" % alias if alias else nv
    return lit(value, "color", src + ("; matches declared %s" % alias if alias else ""), desc)


sem = SPEC["dark"]
for key, comp, state, prop, group, desc in [
    ("ink", "hero-h1", "default", "color", "text",
     "The bright ink on display copy and headings."),
    ("navInk", "nav-pricing", "default", "color", "text",
     "The header link ink."),
    ("navInkHover", "nav-pricing", "hover", "color", "text",
     "The header link ink on hover."),
    ("ctaFill", "nav-cta", "default", "backgroundColor", "action",
     "The header \"Sign up\" button fill."),
    ("ctaInk", "nav-cta", "default", "color", "action",
     "The text on the header \"Sign up\" button."),
    ("ctaHover", "nav-cta", "hover", "backgroundColor", "action",
     "The header \"Sign up\" hover fill."),
    ("focusRing", "nav-cta", "focus-visible", "outlineColor", "border",
     "The keyboard focus ring colour on the header CTA."),
    ("heroCtaFill", "hero-cta", "default", "backgroundColor", "action",
     "The hero \"Get started for free\" pill fill — white."),
    ("heroCtaInk", "hero-cta", "default", "color", "action",
     "The hero CTA text."),
    ("heroGhost", "hero-mcp", "default", "backgroundColor", "action",
     "The \"Install the MCP\" ghost button fill."),
    ("fieldBg", "login-email", "default", "paintedBg", "form",
     "The sign-in e-mail field fill on the light auth shell — painted on the "
     "field's wrapper div; the input itself is transparent."),
    ("fieldInk", "login-email", "default", "color", "form",
     "The field text ink on the auth shell."),
    ("placeholder", "login-email", "default", "placeholder", "form",
     "The placeholder ink ('Enter your work email…')."),
    ("googleFill", "login-google", "default", "backgroundColor", "action",
     "The 'Continue with Google' button fill on the login card."),
    ("googleInk", "login-google", "default", "color", "action",
     "The 'Continue with Google' button text."),
    ("loginPanel", "login-panel", "default", "backgroundColor", "surface",
     "The login card surface on the light auth shell."),
    ("planCtaFill", "plan-cta", "default", "backgroundColor", "action",
     "The Pro plan CTA button fill."),
    ("planCtaInk", "plan-cta", "default", "color", "action",
     "The Pro plan CTA button text."),
    ("faqInk", "faq-acc", "default", "color", "text",
     "The FAQ question ink."),
    ("footerBg", "footer", "default", "backgroundColor", "surface",
     "The footer surface fill."),
    # galBg stays unpublished today: gal-h1 is the transparent masthead, not
    # the page surface, and no ancestor or page paint was recorded for it —
    # the role appears only once a painted gallery surface is measured.
    ("galBg", "gal-h1", "default", "paintedBg", "surface",
     "The community-gallery page surface (the dark community stack)."),
    ("galCardBtn", "gal-open", "default", "backgroundColor", "action",
     "A gallery card's \"Open\" button fill."),
    ("galFilterInk", "gal-filter", "default", "color", "text",
     "A gallery sort button's ink."),
    ("menuPanel", "nav-panel", "default", "backgroundColor", "surface",
     "The Platform mega-dropdown panel fill — transparent: the menu floats "
     "over the page field and only its item pills paint."),
]:
    try:
        if prop == "color":
            raw = ts(comp, state, "color")
            src = f"computed color of {comp} {state} — the first text node's reading where the kit recorded one (raw/components-computed.json)"
        elif prop == "placeholder":
            raw = (C[comp]["states"][state].get("placeholder") or {}).get("color")
            src = f"computed ::placeholder color of {comp} {state} (raw/components-computed.json)"
        elif prop == "paintedBg":
            raw, src = painted_bg(comp, state)
        else:
            raw = st(comp, state)[prop]
            src = f"computed {prop} of {comp} {state} (raw/components-computed.json)"
        if raw in (None, ""):
            raise KeyError(prop)
        if comp in AUTH_COMPONENTS:
            SPEC["auth"].setdefault("color", {}).setdefault(group, {})[key] = lit(raw, "color", src, desc)
        else:
            sem.setdefault("color", {}).setdefault(group, {})[key] = semcolor(raw, src, desc)
    except KeyError:
        pass

# The page field behind every www page: the declared #000 token, visible as
# the black field in every screenshot.
black = cands.get("#000000")
sem.setdefault("color", {}).setdefault("background", {})["page"] = lit(
    "{color.%s}" % black if black else "#000000", "color",
        "the body-declared #000 token (raw/css-vars.json); visible as the black field behind every marketing page (screenshots/*-dark-*.png)",
        "The black page field — #000.")

# ------------------------------------------------------------- type ramp
#
# A Framer site sets text styles inline per element; these are measured
# steps, labelled.

for key, comp, state, prop, desc in [
    ("hero", "hero-h1", "default", "fontSize", "The hero display heading size."),
    ("section", "section-h2", "default", "fontSize", "A section heading size."),
    ("nav", "nav-pricing", "default", "fontSize", "The header link size."),
    ("body", "footer-link", "default", "fontSize", "A footer link size."),
    ("faq", "faq-acc", "default", "fontSize", "A FAQ question size."),
    ("button", "hero-cta", "default", "fontSize", "The hero CTA label size."),
    ("plan", "plan-cta", "default", "fontSize", "A plan CTA label size."),
]:
    try:
        raw = ts(comp, state, prop) or st(comp, state)[prop]
        SPEC["core"].setdefault("font", {}).setdefault("size", {}).setdefault("measured", {})[key] = lit(
            raw, "dimension", f"computed {prop} of {comp} {state} (raw/components-computed.json)", desc)
    except KeyError:
        pass

for key, comp, state, desc in [
    ("hero", "hero-h1", "default", "The hero display heading weight."),
    ("section", "section-h2", "default", "A section heading weight."),
    ("nav", "nav-pricing", "default", "The header link weight."),
    ("body", "footer-link", "default", "The footer link weight."),
    ("button", "hero-cta", "default", "The hero CTA label weight."),
]:
    try:
        raw = ts(comp, state, "fontWeight") or st(comp, state)["fontWeight"]
        if raw:
            SPEC["core"].setdefault("font", {}).setdefault("weight", {}).setdefault("measured", {})[key] = lit(
                int(float(raw)), "fontWeight", f"computed fontWeight of {comp} {state} (raw/components-computed.json)", desc)
    except (KeyError, ValueError):
        pass

for key, comp, state, desc in [
    ("hero", "hero-h1", "default", "The hero display heading line-height."),
    ("nav", "nav-pricing", "default", "The header link line-height."),
    ("body", "footer-link", "default", "The footer link line-height."),
]:
    try:
        raw = ts(comp, state, "lineHeight") or st(comp, state)["lineHeight"]
        SPEC["core"].setdefault("font", {}).setdefault("height", {}).setdefault("measured", {})[key] = lit(
            raw, "dimension" if re.fullmatch(r"-?[0-9.]+(px|rem)", raw or "") else "other",
            f"computed lineHeight of {comp} {state} (raw/components-computed.json)", desc)
    except KeyError:
        pass

for key, comp, state, desc in [
    ("display", "hero-h1", "default", "The display/heading face the marketing pages set."),
    ("body", "nav-pricing", "default", "The face on nav links and body copy."),
    ("auth", "login-google", "default", "The face on the auth shell."),
    ("community", "gal-h1", "default", "The face on the community stack."),
]:
    try:
        raw = ts(comp, state, "fontFamily") or st(comp, state)["fontFamily"]
        if raw:
            SPEC["core"].setdefault("font", {}).setdefault("family", {}).setdefault("measured", {})[key] = lit(
                raw, "fontFamily", f"computed fontFamily of {comp} {state} (raw/components-computed.json)", desc)
    except KeyError:
        pass

# ------------------------------------------------------------------ shape
#
# No radius is declared; every radius here is measured.

for key, comp, state, prop, desc in [
    ("cta", "nav-cta", "default", "borderTopLeftRadius", "The header \"Sign up\" radius."),
    ("heroCta", "hero-cta", "default", "borderTopLeftRadius", "The hero pill radius."),
    ("navLink", "nav-pricing", "default", "borderTopLeftRadius", "The header link radius."),
    ("menuPanel", "nav-panel", "default", "borderTopLeftRadius", "The mega-dropdown panel radius."),
    ("planCard", "plan-card", "default", "borderTopLeftRadius", "A plan card radius."),
    ("field", "login-email", "default", "borderTopLeftRadius", "The sign-in field radius."),
    ("button", "login-google", "default", "borderTopLeftRadius", "The auth shell button radius."),
    ("select", "credits-select", "default", "borderTopLeftRadius", "The credits select radius."),
    ("chip", "gal-filter", "default", "borderTopLeftRadius", "A gallery sort-button radius."),
]:
    try:
        v = st(comp, state)[prop]
        if v in (None, ""):
            raise KeyError(prop)
        emit_at(SPEC["core"].setdefault("radius", {}), "measured." + key,
                lit(v, "dimension" if re.fullmatch(r"-?[0-9.]+(px|rem)", v or "") else "other",
                    f"computed {prop} of {comp} {state} (raw/components-computed.json)", desc))
    except KeyError:
        pass

# ------------------------------------------------------------------ shadow

for key, comp, state, prop, desc in [
    ("menuPanel", "nav-panel", "default", "boxShadow", "The mega-dropdown panel shadow."),
    ("planCard", "plan-card", "default", "boxShadow", "A plan card's shadow."),
    ("loginCard", "login-panel", "default", "boxShadow", "The login card's shadow."),
    ("headerBar", "mkt-header", "default", "boxShadow", "The header bar's shadow (none, unless it floats)."),
]:
    try:
        v = st(comp, state)[prop]
        if not v or v == "none":
            raise KeyError(prop)
        emit_at(SPEC["auth" if comp in AUTH_COMPONENTS else "dark"].setdefault("shadow", {}), "measured." + key,
                lit(v, "other", f"computed {prop} of {comp} {state} (raw/components-computed.json)", desc))
    except KeyError:
        pass

# ------------------------------------------------------------------ spacing

for key, comp, state, prop, desc in [
    ("headerPaddingX", "mkt-header", "default", "paddingLeft", "The header bar's horizontal padding."),
    ("ctaPaddingX", "nav-cta", "default", "paddingLeft", "The header CTA's horizontal padding."),
    ("ctaPaddingY", "nav-cta", "default", "paddingTop", "The header CTA's vertical padding."),
    ("fieldPaddingX", "login-email", "default", "paddingLeft", "The sign-in field's horizontal padding."),
    ("chipPaddingX", "gal-filter", "default", "paddingLeft", "A gallery sort button's horizontal padding."),
]:
    try:
        v = st(comp, state)[prop]
        if v in (None, ""):
            raise KeyError(prop)
        emit_at(SPEC["core"].setdefault("spacing", {}), "measured." + key,
                lit(v, "dimension" if re.fullmatch(r"-?[0-9.]+(px|rem)", v or "") else "other",
                    f"computed {prop} of {comp} {state} (raw/components-computed.json)", desc))
    except KeyError:
        pass

# ------------------------------------------------------------------ motion

try:
    s = st("nav-pricing", "default")
    dur, e = s.get("transitionDuration"), s.get("transitionTimingFunction")
    if dur and dur != "0s":
        props = [p.strip() for p in s.get("transitionProperty", "all").split(",") if p.strip()]
        durs = [d.strip() for d in dur.split(",")]
        tfs = re.findall(r"cubic-bezier\([^)]*\)|steps\([^)]*\)|[a-z-]+", e or "")
        parts = []
        for i, p in enumerate(props):
            d = durs[i % len(durs)]
            if d == "0s":
                continue
            parts.append(f"{p} {d} {tfs[i % len(tfs)] if tfs else ''}".strip())
        if parts:
            SPEC["core"].setdefault("motion", {})["control"] = lit(", ".join(parts), "other",
                "computed transition of nav-pricing default (raw/components-computed.json)",
                "The control transition on a header link.")
except KeyError:
    pass

# ------------------------------------------------------------- components

comp = SPEC["component"]
for name, cname, state, prop, ty_, desc in [
    ("topbar-height", "mkt-header", "default", "h", "dimension", "The site header bar height."),
    ("cta-height", "nav-cta", "default", "h", "dimension", "The header \"Sign up\" height."),
    ("hero-cta-height", "hero-cta", "default", "h", "dimension", "The hero pill height."),
    ("nav-link-height", "nav-pricing", "default", "h", "dimension", "A header link's hit height."),
    ("menu-panel-width", "nav-panel", "default", "w", "dimension", "The Platform mega-dropdown panel width."),
    ("hero-headline-width", "hero-h1", "default", "w", "dimension", "The hero display heading's measure."),
    ("plan-card-width", "plan-card", "default", "w", "dimension", "A plan column's width."),
    ("credits-select-width", "credits-select", "default", "w", "dimension", "The credits select width."),
    ("login-panel-width", "login-panel", "default", "w", "dimension", "The sign-in card width on /login."),
    ("login-field-height", "login-email", "default", "h", "dimension", "The sign-in e-mail field height."),
    ("login-button-height", "login-google", "default", "h", "dimension", "The 'Continue with Google' button height."),
    ("gallery-filter-height", "gal-filter", "default", "h", "dimension", "A gallery sort button's height."),
    ("gallery-card-btn-width", "gal-open", "default", "w", "dimension", "A gallery 'Open' button's width."),
    ("mobile-topbar-height", "m-topbar", "default", "h", "dimension", "The phone header bar height."),
]:
    try:
        v = rc(cname, state, prop)
        comp[name] = lit(("%g" % v) + "px" if isinstance(v, (int, float)) else str(v) + "px",
                         ty_, f"measured {prop} of {cname} {state} (raw/components-computed.json)", desc)
    except KeyError:
        pass

(RAW / "component-tokens.json").write_text(json.dumps(SPEC, indent=2, ensure_ascii=False) + "\n")
print("component-tokens.json:", {k: len(v) for k, v in SPEC.items() if k != "_about"})
