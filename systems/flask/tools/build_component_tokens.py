#!/usr/bin/env python3
"""Write raw/component-tokens.json, the token spec build_tokens.py reads.

flask.do is one public surface signed out: a React-Router app that declares a
real design-token layer in the inline `<style id="ds-theme">` block every page
ships plus the linked root-*.css bundle (raw/css-vars.json):

  --ds-surface-0…4      the near-black surface ramp (12/18/24/31/42 greys)
  --ds-fg-1…4, --ds-fg-lead/-subhead/-placeholder
                        the 4-step foreground ramp plus named text roles
  --ds-line-1…3, --ds-line-edge
                        hairline greys
  --ds-brand*           the brand grey (173 173 173 — a neutral brand on the
                        marketing surfaces) with tint/highlight/fg
  --ds-danger-*, --ds-warning-*, --ds-success-*, --ds-info-*
                        the four status palettes (base, edge, fg, highlight,
                        shade, text, tint, bevel)
  --ds-live-*           the red "live" recording palette
  --ds-flair-1…3        the purple/orange/sand gradient accents
  --ds-glass-*, --ds-glow-*, --ds-metal-*, --ds-showcase-*
                        the translucent glass, glow, metallic and showcase
                        ingredient colours the marketing demo paints with
  --ds-fill/-hover/-pressed/-selected/-highlight/-row-hover/-row-selected,
  --ds-control-*, --ds-chip-*, --ds-marker-*, --ds-scrollbar-*,
  --ds-scrim-*, --ds-track*, --ds-well, --ds-media-*, --ds-on-media*,
  --ds-card-veil, --ds-dot-glow, --ds-drop(-soft/-strong), --ds-edge-sweep*,
  --ds-raised-*, --ds-ring-soft, --ds-primary-*, --ds-search-border,
  --ds-selection-outline, --ds-shimmer-peak, --ds-toast-sweep,
  --ds-warning-tint-hover, --ds-focus(-ring)
                        the interaction-opacity and overlay ingredient colours
  --ds-shadow-*         mostly shadow *colours* ("0 0 0 / 0.45" channel lists);
                        --ds-shadow-card/-float/-overlay/-popover are real
                        shadow declarations
  --ds-font-sans        the system-ui sans stack
  --ds-radius, --ds-radius-control, --radius
                        12px cards / 9999px pills
  --ease-in-out, --ease-out
                        the declared easing curves

Every colour is held as a Tailwind-style channel list — "250 250 250" or
"250 250 250 / 0.18" — that utilities composite with rgb() / alpha; the spec
converts each to the hex/rgba() the browser paints (labelled on source).

Every public page paints the dark `default` theme: the only --ds-* layer the
bundle declares, resolved here once on :root in the live dark context
(vars.mjs). No light variant or theme toggle exists; tokens.json therefore
carries a single `dark` set plus `core` (theme-invariant scales) and
`component` (measured geometry). Measured roles alias to the declared token
whose painted value they match.

Deterministic: same inputs, byte-identical output.
"""
import json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
V = json.loads((RAW / "css-vars.json").read_text())
R = V.get("resolved", {}).get("dark", {})
C = json.loads((RAW / "components-computed.json").read_text())["components"]

SPEC = {"_about": (
    "The token tree build_tokens.py turns into tokens.json. flask.do "
    "declares its design-token layer in the inline ds-theme stylesheet and "
    "the linked root-*.css bundle (raw/css-vars.json): the --ds-* roles held "
    "as rgb channel lists, plus --ds-font-sans, --ds-radius(-control), "
    "--radius and the --ease-* curves. The dark set is the only theme the "
    "site ships — every public page paints it. Measured roles alias to the "
    "declared values where they match."),
    "core": {}, "dark": {}, "component": {}}


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
    """'250 250 250', '250 250 250 / 0.18', #hex, rgb()/rgba() -> the hex or
    rgba() the browser paints. The channel-list form is how the ds-theme
    block declares every colour."""
    v = (v or "").strip()
    m = re.fullmatch(r"(\d+(?:\.\d+)?)\s+(\d+(?:\.\d+)?)\s+(\d+(?:\.\d+)?)\s*(?:/\s*([\d.]+))?", v)
    if m:
        r, g, b = (int(float(m.group(i))) for i in (1, 2, 3))
        a = float(m.group(4)) if m.group(4) is not None else 1
        return "#%02x%02x%02x" % (r, g, b) if a == 1 else "rgba(%d, %d, %d, %g)" % (r, g, b, a)
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
    """Write `leaf` at a dotted path (`surface.0`). A leaf that must share a
    node with a group moves inside it under `default`."""
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


DECL_SRC = "declared design-system variable in the ds-theme stylesheets (raw/css-vars.json)"


def declared(name):
    v = R.get(name)
    return v if v not in (None, "") else None


def var(name, ty="color", **kw):
    d = {"var": name, "type": ty}
    d.update(kw)
    return d


def is_channel(v):
    return bool(re.fullmatch(r"\d+(\.\d+)?\s+\d+(\.\d+)?\s+\d+(\.\d+)?(\s+/\s*[\d.]+)?", str(v).strip()))


COLOR_V = re.compile(r"(#[0-9a-fA-F]{3,8}|rgba?\([^)]*\)|hsla?\([^)]*\)|color-mix\([^)]*\)|\d+(\.\d+)?\s+\d+(\.\d+)?\s+\d+(\.\d+)?(\s+/\s*[\d.]+)?)")

SHADOW_V = re.compile(r"^(?:inset\s+)?-?[\d.]+(?:px|rem)?\s+-?[\d.]+(?:px|rem)?(\s+-?[\d.]+(?:px|rem)?){0,2}\s+.*rgb")


def _px(v):
    """'0' -> '0px'; lengths keep their unit."""
    v = v.strip()
    return v if re.search(r"[a-zA-Z%]$", v) else v + "px"


def split_shadow(raw):
    """'x y blur spread color, x2 y2 …' -> the DTCG shadow layer list."""
    layers, depth, cur, out = [], 0, "", []
    for ch in str(raw):
        if ch in "([":
            depth += 1
        elif ch in ")]":
            depth -= 1
        if ch == "," and depth == 0:
            out.append(cur)
            cur = ""
        else:
            cur += ch
    out.append(cur)
    for l in out:
        l = l.strip()
        inset = l.startswith("inset")
        l = re.sub(r"^inset\s+", "", l)
        m = re.match(r"(.+?)\s+(-?[\d.]+px)\s+(-?[\d.]+px)\s+(-?[\d.]+px)(?:\s+(-?[\d.]+px))?\s*$", l[::-1])
        # colour first then offsets, or offsets then colour — try colour-last
        m2 = re.match(r"^(-?[\d.]+(?:px|rem)?)\s+(-?[\d.]+(?:px|rem)?)\s+(-?[\d.]+(?:px|rem)?)(?:\s+(-?[\d.]+(?:px|rem)?))?\s+(.+)$", l)
        if not m2:
            return None
        x, y, blur, spread, col = _px(m2.group(1)), _px(m2.group(2)), _px(m2.group(3)), _px(m2.group(4) or "0px"), m2.group(5)
        d = {"color": norm_color(col), "offsetX": x, "offsetY": y, "blur": blur, "spread": spread}
        if inset:
            d["inset"] = True
        layers.append(d)
    return layers


def decl_color(name):
    v = declared(name)
    nv = norm_color(v)
    src = f"{DECL_SRC}: {name}"
    if is_channel(str(v).strip()):
        src += f"; the channel list `{v}` normalised to {nv}"
    return lit(nv, "color", src, f"The declared `{name}`.")


# ------------------------------------------------------------------- fonts

fam = SPEC["core"].setdefault("font", {}).setdefault("family", {})
if declared("--ds-font-sans"):
    fam["sans"] = var("--ds-font-sans", "fontFamily",
                      description="The --ds-font-sans stack: ui-sans-serif/system-ui plus the emoji fallbacks — every heading, control and body on the public surface.")

# ------------------------------------------------------------- radii

radii = SPEC["core"].setdefault("radius", {})
for name, key, desc in [
    ("--ds-radius", "default", "The 12px card/panel radius."),
    ("--ds-radius-control", "control", "The 9999px full-pill radius on buttons and chips."),
    ("--radius", "base", "The shared --radius alias the Tailwind-style utilities read (12px)."),
]:
    if declared(name):
        emit_at(radii, key, var(name, "dimension", description=desc), name)

radius_alias = {}
for name, key in [("--ds-radius", "default"), ("--ds-radius-control", "control"), ("--radius", "base")]:
    if declared(name):
        radius_alias.setdefault(str(R[name]).strip(), key)

# ------------------------------------------------------------- motion

mo = SPEC["core"].setdefault("motion", {})
ease = mo.setdefault("ease", {})
for name, key, desc in [
    ("--ease-out", "out", "The declared --ease-out curve."),
    ("--ease-in-out", "inOut", "The declared --ease-in-out curve."),
]:
    if declared(name):
        emit_at(ease, key, var(name, "cubicBezier", description=desc), name)

# -------------------------------------------------- the --ds-* colour layer
#
# Every --ds-* name whose resolved value is a channel list becomes a dark
# token at its namespaced path (--ds-surface-0 -> surface.0); the four real
# shadow declarations become shadow composites; --ds-shadow-* channel lists
# become shadow colour ingredients under shadow.color.*.

dark = SPEC["dark"]
for name in sorted(k for k in R if k.startswith("--ds-")):
    if name in ("--ds-font-sans", "--ds-radius", "--ds-radius-control"):
        continue
    v = declared(name)
    if v is None:
        continue
    rest = name[len("--ds-"):]
    path = rest.replace("-", ".")
    if SHADOW_V.match(str(v).strip()):
        layers = split_shadow(v)
        if layers:
            emit_at(dark, path, lit(layers, "shadow", f"{DECL_SRC}: {name}; the declared shadow, resolved verbatim",
                                    f"The declared `{name}` shadow."), name)
            continue
    if is_channel(str(v).strip()):
        if rest.startswith("shadow-"):
            path = "shadow.color." + rest[len("shadow-"):]
        emit_at(dark, path, decl_color(name), name)
        continue
    # Anything else declared (a stray keyword) is kept as `other`, labelled.
    emit_at(dark, path, lit(v, "other", f"{DECL_SRC}: {name}", f"The declared `{name}`."), name)

# -------------------------------------------- measured roles -> aliases
#
# Roles measured on the real pages; each aliases to the declared token its
# painted value matches.

role_alias = {}
for name in sorted(k for k in EMITTED):
    nv = norm_color(R.get(name, ""))
    if nv and nv.startswith("#"):
        role_alias.setdefault(nv, EMITTED[name])
# A colour several roles share resolves to the same alias every build; rank
# the canonical names so the pick is deterministic.
ALIAS_FIRST = ["surface.0", "surface.1", "surface.2", "fg.1", "fg.2", "fg.3", "line.1", "brand.default", "brand.fg"]
ALIAS_RANK = {p: i for i, p in enumerate(ALIAS_FIRST)}
role_alias = {}
cands = {}
for name in sorted(k for k in EMITTED):
    nv = norm_color(R.get(name, ""))
    if not nv:
        continue
    p = EMITTED[name]
    cur = cands.get(nv)
    if cur is None or (ALIAS_RANK.get(p, 99), p) < (ALIAS_RANK.get(cur, 99), cur):
        cands[nv] = p
role_alias = cands


def semcolor(raw, src, desc):
    nv = norm_color(raw)
    alias = role_alias.get(nv)
    value = f"{{{alias}}}" if alias else nv
    return lit(value, "color", src + (f"; matches declared {alias}" if alias else ""), desc)


TRANSPARENT = re.compile(r"transparent|rgba\(\s*\d+,\s*\d+,\s*\d+,\s*0(\.0+)?\s*\)")
SIDES = {"to top": "0deg", "to right": "90deg", "to bottom": "180deg", "to left": "270deg"}


def split_top(v):
    out, depth, cur = [], 0, ""
    for ch in v:
        depth += ch == "("
        depth -= ch == ")"
        if ch == "," and depth == 0:
            out.append(cur.strip())
            cur = ""
        else:
            cur += ch
    return out + [cur.strip()]


def gradient_of(comp, state):
    """The element's own linear-gradient backgroundImage as a DTCG gradient, or None."""
    img = st(comp, state).get("backgroundImage") or ""
    m = re.fullmatch(r"linear-gradient\((.*)\)", img.strip())
    if not m:
        return None
    parts = split_top(m.group(1))
    angle = "180deg"
    if parts[0] in SIDES or re.fullmatch(r"-?[\d.]+deg", parts[0]):
        angle = SIDES.get(parts[0], parts[0])
        parts = parts[1:]
    stops = []
    for i, part in enumerate(parts):
        mm = re.fullmatch(r"(rgba?\([^)]*\))\s*(?:([\d.]+)%)?", part)
        if not mm:
            raise ValueError(f"{comp} {state}: gradient stop {part!r}")
        pos = float(mm.group(2)) / 100 if mm.group(2) else i / max(1, len(parts) - 1)
        stops.append({"color": norm_color(mm.group(1)), "position": round(pos, 4)})
    return {"value": stops, "type": "gradient", "angle": angle,
            "source": f"computed backgroundImage of {comp} {state} ({img}); its backgroundColor reads transparent (raw/components-computed.json)"}


def painted_ring(comp, state):
    """The focus ring as painted: the outline when it has a style and a width, else the first
    box-shadow layer that draws a solid spread ring (Tailwind's ring utilities)."""
    s = st(comp, state)
    if s.get("outlineStyle") not in (None, "none", "auto") and s.get("outlineWidth", "0px") not in ("0px", "0"):
        return s["outlineColor"], f"computed outlineColor of {comp} {state} (raw/components-computed.json)"
    for layer in split_top(s.get("boxShadow") or ""):
        mm = re.fullmatch(r"(rgba?\([^)]*\))\s+0px\s+0px\s+0px\s+([\d.]+)px(\s+inset)?", layer)
        if mm and float(mm.group(2)) > 0 and not TRANSPARENT.fullmatch(norm_color(mm.group(1))):
            return mm.group(1), (f"computed boxShadow ring of {comp} {state} ({mm.group(2)}px spread; the outline is "
                                 f"{s.get('outlineStyle')} {s.get('outlineWidth')}) (raw/components-computed.json)")
    raise KeyError(f"{comp} {state}: no painted ring")


sem = dark
for key, comp, state, prop, group, desc in [
    ("ink", "hero-h1", "default", "color", "text",
     "The bright ink on display copy, headings and body — the fg-1 role."),
    ("navInk", "nav-pricing", "default", "color", "text",
     "The header link ink — the fg-2 role."),
    ("ctaFill", "nav-cta", "default", "backgroundColor", "action",
     "The header CTA button fill (the primary-button face, usually the light brand grey)."),
    ("ctaInk", "nav-cta", "default", "color", "action",
     "The text on the header CTA button."),
    ("ctaHover", "nav-cta", "hover", "backgroundColor", "action",
     "The header CTA's hover fill."),
    ("focusRing", "nav-cta", "focus-visible", "outlineColor", "border",
     "The keyboard focus ring colour on the header CTA."),
    ("heroCtaFill", "hero-cta", "default", "backgroundColor", "action",
     "The hero CTA fill (button-primary in the marketing demo style)."),
    ("heroCtaInk", "hero-cta", "default", "color", "action",
     "The hero CTA text."),
    ("fieldBg", "login-email", "default", "backgroundColor", "form",
     "The sign-in e-mail field fill."),
    ("fieldInk", "login-email", "default", "color", "form",
     "The field text ink."),
    ("placeholder", "login-email", "default", "placeholder", "form",
     "The placeholder ink ('han@solo.com')."),
    ("googleFill", "login-google", "default", "backgroundColor", "action",
     "The 'Continue with Google' button fill on the login card."),
    ("googleInk", "login-google", "default", "color", "action",
     "The 'Continue with Google' button text."),
    ("demoCardBg", "demo-share-popover", "default", "backgroundColor", "surface",
     "The demo share popover's surface fill — the glass/surface-3 card."),
    ("demoTabInk", "demo-tab-context", "default", "color", "text",
     "The demo's active tab ink."),
    ("shareRowInk", "demo-acme-btn", "default", "color", "text",
     "The 'ACME Studios' share-popover button ink."),
    ("switchTrack", "billing-switch", "default", "backgroundColor", "action",
     "The billing switch track fill when on."),
    ("planCtaFill", "plan-cta", "default", "backgroundColor", "action",
     "The 'Get Started' plan button fill."),
    ("planCtaInk", "plan-cta", "default", "color", "action",
     "The 'Get Started' plan button text."),
    ("bookCallFill", "book-call", "default", "backgroundColor", "action",
     "The 'Book Call' button fill."),
    ("faqInk", "faq-acc", "default", "color", "text",
     "The FAQ question ink."),
    ("footerBg", "footer", "default", "backgroundColor", "surface",
     "The footer surface fill."),
]:
    try:
        if prop == "color":
            raw = ts(comp, state, "color")
            src = f"computed color of {comp} {state} — the first text node's reading where the kit recorded one (raw/components-computed.json)"
        elif prop == "placeholder":
            raw = (C[comp]["states"][state].get("placeholder") or {}).get("color")
            src = f"computed ::placeholder color of {comp} {state} (raw/components-computed.json)"
        else:
            raw = st(comp, state)[prop]
            src = f"computed {prop} of {comp} {state} (raw/components-computed.json)"
        if raw in (None, ""):
            raise KeyError(prop)
        if prop == "outlineColor":
            raw, src = painted_ring(comp, state)
        if prop == "backgroundColor" and TRANSPARENT.fullmatch(norm_color(raw)):
            # A transparent reading paints nothing: the fill is a gradient on the same element
            # (the light brand-grey button face), or there is no fill to commit.
            grad = gradient_of(comp, state)
            if grad:
                sem.setdefault(group, {})[key] = grad | {"description": desc}
            continue
        sem.setdefault(group, {})[key] = semcolor(raw, src, desc)
    except KeyError:
        pass

# The page field behind every public surface: the declared --ds-surface-0,
# visible as the near-black field in every screenshot.
if declared("--ds-surface-0") is not None:
    sem.setdefault("background", {})["page"] = lit(
        "{surface.0}", "color",
        "the :root --ds-surface-0 resolved on the public pages (raw/css-vars.json); visible as the near-black field behind every page (screenshots/*-dark-*.png)",
        "The near-black page field — --ds-surface-0.")

# ------------------------------------------------------------- type ramp
#
# Measured steps land as literals (the site declares no size ramp).

for key, comp, state, prop, desc in [
    ("hero", "hero-h1", "default", "fontSize", "The hero display heading size."),
    ("section", "section-h2", "default", "fontSize", "A section heading size."),
]:
    try:
        raw = st(comp, state)[prop]
        SPEC["core"].setdefault("font", {}).setdefault("size", {}).setdefault("measured", {})[key] = lit(
            raw, "dimension", f"computed {prop} of {comp} {state} (raw/components-computed.json)", desc)
    except KeyError:
        pass

for key, comp, state, desc in [
    ("hero", "hero-h1", "default", "The hero display heading weight."),
    ("body", "nav-pricing", "default", "The header link weight."),
]:
    try:
        raw = ts(comp, state, "fontWeight") or st(comp, state)["fontWeight"]
        if raw:
            SPEC["core"].setdefault("font", {}).setdefault("weight", {}).setdefault("measured", {})[key] = lit(
                int(float(raw)), "fontWeight", f"computed fontWeight of {comp} {state} (raw/components-computed.json)", desc)
    except (KeyError, ValueError):
        pass

# ------------------------------------------------------------------ shape

for key, comp, state, prop, desc in [
    ("cta", "nav-cta", "default", "borderTopLeftRadius", "The header CTA radius (the full control pill)."),
    ("button", "hero-copy-prompt", "default", "borderTopLeftRadius", "The secondary button radius (the hero 'Copy Prompt' pill)."),
    ("navLink", "nav-pricing", "default", "borderTopLeftRadius", "The header link radius."),
    ("card", "demo-share-popover", "default", "borderTopLeftRadius", "A demo popover/card radius."),
    ("field", "login-email", "default", "borderTopLeftRadius", "The sign-in field radius."),
    ("switch", "billing-switch", "default", "borderTopLeftRadius", "The billing switch track radius."),
]:
    try:
        v = st(comp, state)[prop]
        dkey = radius_alias.get(str(v).strip())
        if dkey:
            emit_at(radii, "measured." + key, lit(f"{{radius.{dkey}}}", "dimension",
                f"computed {prop} of {comp} {state} (raw/components-computed.json); matches declared radius.{dkey}", desc))
        else:
            emit_at(radii, "measured." + key, lit(v, "dimension" if re.fullmatch(r"-?[0-9.]+(px|rem)", v or "") else "other",
                f"computed {prop} of {comp} {state} (raw/components-computed.json)", desc))
    except KeyError:
        pass

# ------------------------------------------------------------------ motion

try:
    s = st("nav-cta", "default")
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
            mo["control"] = lit(", ".join(parts), "other",
                "computed transition of nav-cta default (raw/components-computed.json); the --ease-* steps are the declared curves",
                "The control transition on the header CTA.")
except KeyError:
    pass

# ------------------------------------------------------------- components

comp = SPEC["component"]
for name, cname, state, prop, ty_, desc in [
    ("topbar-height", "mkt-header", "default", "h", "dimension", "The site header bar height."),
    ("cta-height", "nav-cta", "default", "h", "dimension", "The header CTA pill height."),
    ("button-height", "hero-copy-prompt", "default", "h", "dimension", "The secondary button height (the 'Copy Prompt' pill)."),
    ("chip-height", "demo-version-chip", "default", "h", "dimension", "The demo version chip height."),
    ("hero-headline-width", "hero-h1", "default", "w", "dimension", "The hero display heading's measure."),
    ("login-panel-width", "login-panel", "default", "w", "dimension", "The sign-in card width on /login."),
    ("login-field-height", "login-email", "default", "h", "dimension", "The sign-in e-mail field height."),
    ("login-button-height", "login-google", "default", "h", "dimension", "The 'Continue with Google' button height."),
    ("switch-width", "billing-switch", "default", "w", "dimension", "The billing switch track width."),
    ("switch-height", "billing-switch", "default", "h", "dimension", "The billing switch track height."),
    ("mobile-topbar-height", "m-topbar", "default", "h", "dimension", "The phone header bar height."),
]:
    try:
        v = rc(cname, state, prop)
        comp[name] = lit(("%g" % v) + "px" if isinstance(v, (int, float)) else str(v) + "px",
                         ty_, f"measured {prop} of {cname} {state} (raw/components-computed.json)", desc)
    except KeyError:
        pass

if __name__ == "__main__":
    (RAW / "component-tokens.json").write_text(json.dumps(SPEC, indent=2, ensure_ascii=False) + "\n")
    print("component-tokens.json:", {k: len(v) for k, v in SPEC.items() if k != "_about"})
