#!/usr/bin/env python3
"""Write raw/component-tokens.json, the token spec build_tokens.py reads.

figma.com is two public surfaces signed out. The marketing site
(www.figma.com/...) is a Next.js + Emotion app that declares a real
design-token layer in its stylesheet (raw/css-vars.json):

  --fig-typography-*   a variable-font type ramp: --fig-typography-size-*
                       (formLabel 12px through display1 88px), the
                       --fig-typography-lh-* unitless line-height steps,
                       --fig-typography-ls-* letter-spacing (the negative
                       -0.078125rem/-0.04125rem tracking is Figma's
                       signature display tightness), the
                       --fig-typography-variation-* font-variation axes
                       (wght 400/600/700, wdth 96/98/100, slnt -6, mono)
  --fig-space-*        the 4/6/8/12/16/24/32/40/56/64/80/120px space scale
  --fig-radius-*       2/4/8/12/16/24/28px plus the 9999px full pill
  --fig-grid-*         the marketing grid: 12 columns, 16px gutter, 40px
                       margin, 95rem max content width
  --fig-elevation-*    the two shadow steps (0 4px 32px / 0 24px 70px at
                       10% black)
  --fig-animation-*    180/250/400ms durations
  --fig-section-*      the 80px section block padding
  --fig-theme-*        the semantic roles redeclared under
                       :root[data-theme="dark"]: bg, fg, fg-muted, card-bg,
                       border(-hover), badge-*, btn-primary/secondary/
                       ghost/transparent-*, form-*
  --global-font-*/--global-cursor-*   the figmaSans/figmaMono stacks and
                       cursor keywords
  --f-*                the page-level marketing frame vars (columns 48,
                       gutter, col-width, max-content-width 1440px,
                       lego-block-padding) — overridden per page and per
                       breakpoint; resolved here on the home page at 1440

Every public page paints :root light — no page carried data-theme="dark"
while captured, so the dark set resolves declarations the site ships but
did not paint (labelled on each dark token's source). /community, /login
and /signup are the product app shell, a different stack that does not
share the --fig-* layer; its measured values land under component.* as
literals.

Deterministic: same inputs, byte-identical output.
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
    "The token tree build_tokens.py turns into tokens.json. figma.com "
    "declares its design-token layer in the marketing site's stylesheets "
    "(raw/css-vars.json): theme-invariant --fig-*/--global-* scales under "
    "core.* and the :root/:root[data-theme='dark']-switching --fig-theme-* "
    "roles emitted under both light.* and dark.* so each scope resolves "
    "its own value. Measured roles alias to the declared values where "
    "they match. The dark set resolves declarations that no public page "
    "painted while captured."),
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
    # Achromatic oklch()/oklab() — how Chromium serialises the site's
    # color-mix tint roles on a measured element (oklch(0 0 none / 0.85)):
    # L 0 is black, L 1 is white, the trailing /a is the alpha. Written as
    # the rgba() the browser paints so a measured tint aliases its declared
    # rgba token (the same normalisation build_tokens.py applies).
    m = re.fullmatch(r"okl(?:ch|ab)\(\s*([\d.]+)\s+(?:0(?:\.0+)?|none)\s+(?:none|[-\d.]+)\s*(?:/\s*([\d.]+))?\s*\)", v)
    if m:
        # an achromatic OKLab colour is linear grey L^3, then sRGB gamma:
        # oklch(0.5 0 0) is #636363, not L x 255 (2026-11 audit, finding 14-22)
        lin = float(m.group(1)) ** 3
        lvl = max(0, min(255, round((12.92 * lin if lin <= 0.0031308 else 1.055 * lin ** (1 / 2.4) - 0.055) * 255)))
        a = float(m.group(2) or 1)
        return "#%02x%02x%02x" % (lvl, lvl, lvl) if a == 1 else "rgba(%d, %d, %d, %g)" % (lvl, lvl, lvl, a)
    m = re.fullmatch(r"color-mix\(in (?:oklch|srgb|hsl|lab|oklab|lch|hwb|xyz[^)]*),\s*(#[0-9a-fA-F]{3,8}),\s*transparent\s+([\d.]+)%\)", v)
    if m:
        # figma.com spells its translucent roles as
        # `color-mix(in oklch, #000000, transparent 92%)`: a flat colour at
        # (100-N)% alpha. The probe resolves the same value as
        # `oklch(0 0 none / 0.08)`, which DTCG cannot hold — the rgba()
        # form here is the same colour the browser paints.
        hexc, pct = m.group(1), float(m.group(2))
        h = hexc.lstrip("#")
        if len(h) in (3, 4):
            h = "".join(c * 2 for c in h)
        r, g, b = (int(h[i:i + 2], 16) for i in (0, 2, 4))
        a = round(1 - pct / 100, 3)
        return f"rgba({r}, {g}, {b}, {'%g' % a})" if a < 1 else "#%02x%02x%02x" % (r, g, b)
    return v


def have(comp, state, prop=None):
    try:
        s = st(comp, state)
        return prop is None or bool((s.get(prop) or "").strip())
    except KeyError:
        return False



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


def emit_at(root, path, leaf, name=None):
    """Write `leaf` at a dotted path (`theme.btn.primary.bg`). A leaf that must
    share a node with a group moves inside it under `default`."""
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


DECL_SRC = "declared design-system variable in the site's stylesheets (raw/css-vars.json)"


def declared(name):
    """The resolved light-set value, or None when the var never resolved."""
    v = R.get(name)
    return v if v not in (None, "") else None


def norm_len(v):
    """Exponential lengths become ordinary pixel strings: Chromium serialises
    `calc(infinity * 1px)` as `3.35544e+07px`, which is a real length, not an
    `other` — it is how the site spells a full pill."""
    m = re.fullmatch(r"(-?[\d.]+[eE][+-]?\d+)(px|rem)", str(v).strip())
    if not m:
        return v
    return f"{float(m.group(1)):f}".rstrip("0").rstrip(".") + m.group(2)


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


COLOR_V = re.compile(r"(#[0-9a-fA-F]{3,8}|rgba?\([^)]*\)|hsla?\([^)]*\)|(ok)?lab\([^)]*\)|(ok)?lch\([^)]*\)|color-mix\([^)]*\)|color\([^)]*\))")


def decl_color(name):
    v = declared(name)
    nv = norm_color(v)
    ty = "color" if COLOR_V.fullmatch(str(nv).strip()) else "other"
    src = f"{DECL_SRC}: {name}"
    if nv != v:
        src += f"; `{v}` normalised to {nv} (the colour-mix the browser paints)"
        v = nv
    return lit(v, ty, src, f"The declared `{name}`.")


def num_decl(name):
    v = declared(name)
    return lit(v, "number", f"{DECL_SRC}: {name}", f"The declared `{name}`.")


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


# Names whose :root declaration is overridden in a @media (min|max-width)
# block — the resolved value is the 1440px view; the override list travels on
# $extensions.responsive.
MEDIA_OVERRIDES = {}
for rule in V.get("theme", []):
    ctx = " ".join(rule.get("context") or [])
    mq = re.search(r"@media \((min|max)-width: (\d+)px\)", ctx)
    if mq and rule.get("selector") == ":root":
        for n in rule.get("properties") or {}:
            tag = f"{mq.group(1)}-width:{mq.group(2)}px"
            MEDIA_OVERRIDES.setdefault(n, [])
            if tag not in MEDIA_OVERRIDES[n]:
                MEDIA_OVERRIDES[n].append(tag)


def resp_kw(name):
    if name in MEDIA_OVERRIDES:
        return {"responsive": "viewport-conditional: also declared under @media (" + ", ".join(MEDIA_OVERRIDES[name]) + "); resolved at 1440 x 900"}
    return {}


# ------------------------------------------------------------------- fonts
#
# figma.com serves figmaSans (a variable face — the weight/width axes ride the
# --fig-typography-variation-* tokens) and figmaMono, each with an
# Arial-metric fallback, declared on :root as --global-font-*/--font-figma-*.

fam = SPEC["core"].setdefault("font", {}).setdefault("family", {})
for key, name, desc in [
    ("sans", "--global-font-sans", "figmaSans — every heading, control and body on the marketing site; Arial-metric fallback then SF Pro Display/system-ui."),
    ("mono", "--global-font-mono", "figmaMono — code and numeric styling; Arial-metric fallback then SF Mono/menlo."),
]:
    if name in R:
        fam[key] = var(name, "fontFamily", description=desc)

weights = SPEC["core"].setdefault("font", {}).setdefault("weight", {})
for name in sorted(k for k in R if re.fullmatch(r"--fig-typography-variation-wght-[a-z]+", k)):
    weights[name[len("--fig-typography-variation-wght-"):]] = num_decl(name)

axes = SPEC["core"].setdefault("font", {}).setdefault("variationAxis", {})
for name in sorted(k for k in R if re.fullmatch(r"--fig-typography-variation-(?:(?:wdth|slnt|mono)-[a-z]+|mono)", k)):
    axes[name[len("--fig-typography-variation-"):]] = num_decl(name)

# ------------------------------------------------------------- type ramp
#
# --fig-typography-size-* sizes with the --fig-typography-lh-*/--fig-typography-ls-*
# companions. The display sizes override under 1024px/1600px breakpoints;
# the override is kept on $extensions.responsive.

sizes = SPEC["core"].setdefault("font", {}).setdefault("size", {})
for name in sorted(k for k in R if re.fullmatch(r"--fig-typography-size-[a-zA-Z0-9]+", k)):
    key = name[len("--fig-typography-size-"):]
    sizes[key] = var(name, "dimension", **resp_kw(name))

lineheights = SPEC["core"].setdefault("font", {}).setdefault("lineHeight", {})
for name in sorted(k for k in R if re.fullmatch(r"--fig-typography-lh-[a-z]+", k)):
    lineheights[name[len("--fig-typography-lh-"):]] = num_decl(name)

tracking = SPEC["core"].setdefault("font", {}).setdefault("tracking", {})
for name in sorted(k for k in R if re.fullmatch(r"--fig-typography-ls-[a-z]+", k)):
    tracking[name[len("--fig-typography-ls-"):]] = decl(name)

# ---------------------------------------------------------- core scales
#
# Theme-invariant declarations: the space scale, radii, the layout grid,
# elevations, durations, the section padding and the marketing frame vars.
# These resolve identically in both scopes.

spacing = SPEC["core"].setdefault("spacing", {})
for name in sorted(k for k in R if re.fullmatch(r"--fig-space-\d+|--fig-space-none", k)):
    spacing[name[len("--fig-space-"):]] = decl(name)

radius_alias = {}
radii = SPEC["core"].setdefault("radius", {})
for name in sorted(k for k in R if re.fullmatch(r"--fig-radius-\d+|--fig-radius-full", k)):
    radii[name[len("--fig-radius-"):]] = decl(name)
    radius_alias[norm_len(R[name])] = name[len("--fig-radius-"):]

layout = SPEC["core"].setdefault("layout", {})
grid = layout.setdefault("grid", {})
for name in sorted(k for k in R if re.fullmatch(r"--fig-grid-[a-z-]+", k)):
    key = name[len("--fig-grid-"):]
    ty = "number" if key == "columns" else "dimension"
    grid[key] = decl(name, ty) if ty == "dimension" else num_decl(name)
    if "responsive" in resp_kw(name):
        grid[key]["responsive"] = resp_kw(name)["responsive"]
if declared("--fig-section-block-padding") is not None:
    layout["sectionBlockPadding"] = lit(declared("--fig-section-block-padding"), "dimension",
                                        f"{DECL_SRC}: --fig-section-block-padding",
                                        "The 80px block padding between marketing sections.")
    layout["sectionBlockPadding"].update(resp_kw("--fig-section-block-padding"))

frame = layout.setdefault("frame", {})
FRAME_DESC = {
    "--f-columns": "The marketing content frame's 48-column grid on the home page; per-page and per-breakpoint.",
    "--f-col-width": "One column of that frame — calc(min(100vw,1440px)/48); resolved at 1440.",
    "--f-gutter": "The frame gutter — two columns; resolved at 1440.",
    "--f-max-content-width": "The 1440px marketing content maximum.",
    "--f-lego-block-padding": "The 120px lego-block vertical padding; per-breakpoint.",
}
for name in sorted(k for k in R if re.fullmatch(r"--f-[a-z-]+", k) and declared(k) is not None):
    key = re.sub(r"-([a-z])", lambda m: m.group(1).upper(), name[len("--f-"):])
    v = declared(name)
    ty = "number" if re.fullmatch(r"-?\d+(\.\d+)?", str(v)) else "dimension"
    frame[key] = lit(v, ty if re.fullmatch(r"-?\d+(\.\d+)?(px|rem)|-?\d+(\.\d+)?", str(v)) else "other",
                     f"{DECL_SRC}: {name}", FRAME_DESC.get(name, f"The declared `{name}` (page-level frame var, resolved on the home page at 1440)."))
    frame[key].update(resp_kw(name))

# Elevation: the two declared shadow steps. The resolved colour is
# `oklch(0 0 none / 0.1)` — 10% black; DTCG keeps it as rgba.
def shadow_decl(name):
    raw = declared(name)
    m = re.search(r"oklch\(0 0 none / ([\d.]+)\)\s+(-?[\d.]+)px\s+(-?[\d.]+)px\s+(-?[\d.]+)px\s+(-?[\d.]+)px", str(raw))
    if not m:
        return lit(raw, "other", f"{DECL_SRC}: {name}", f"The declared `{name}` shadow.")
    a, x, y, blur, spread = float(m.group(1)), m.group(2), m.group(3), m.group(4), m.group(5)
    return lit([{"color": f"rgba(0, 0, 0, {'%g' % a})", "offsetX": f"{x}px", "offsetY": f"{y}px", "blur": f"{blur}px", "spread": f"{spread}px"}],
               "shadow", f"{DECL_SRC}: {name}; the oklch(0 0 none / {a}) colour normalised to rgba(0,0,0,{a})",
               f"The declared `{name}` shadow step.")

elevation = SPEC["core"].setdefault("elevation", {})
for name in sorted(k for k in R if re.fullmatch(r"--fig-elevation-\d+(?:-shadow)?", k)):
    key = name[len("--fig-elevation-"):].replace("-shadow", "Shadow")
    elevation[key] = shadow_decl(name)

durations = SPEC["core"].setdefault("duration", {})
for name in sorted(k for k in R if re.fullmatch(r"--fig-animation-\d+", k)):
    durations[name[len("--fig-animation-"):]] = lit(declared(name), "duration", f"{DECL_SRC}: {name}", f"The declared `{name}` duration.")

cursors = SPEC["core"].setdefault("cursor", {})
CURSOR_DESC = {
    "--global-cursor-default": "default", "--global-cursor-pointer": "pointer",
    "--global-cursor-grab": "grab", "--global-cursor-grabbing": "grabbing", "--global-cursor-text": "text",
}
for name in sorted(k for k in R if k.startswith("--global-cursor-")):
    cursors[name[len("--global-cursor-"):]] = lit(declared(name), "other", f"{DECL_SRC}: {name}", f"The declared `{name}` cursor keyword.")

# -------------------------------------- per-scope semantic variables
#
# The 22 --fig-theme-* names redeclared under :root[data-theme='dark'] are
# the site's semantic roles: bg/fg/fg-muted, card-bg, border(-hover),
# badge-*, btn-* and form-*. Each is emitted under both sets so each scope
# resolves its own value. No public page painted data-theme="dark" while
# captured — the dark set resolves declarations the site ships but did not
# display.

mode_names = set()
for rule in V.get("theme", []):
    sel = " ".join(rule.get("context") or []) + " " + rule.get("selector", "")
    if "data-theme" in sel:
        mode_names.update(rule.get("properties") or {})
mode_names.update(n for n in R if n.startswith("--fig-theme-"))


def theme_path(name):
    """--fig-theme-btn-primary-bg -> theme.btn.primary.bg"""
    return "theme." + name[len("--fig-theme-"):].replace("-", ".")


for root in (SPEC["light"], SPEC["dark"]):
    for name in sorted(mode_names):
        leaf_ = var(name, "color" if COLOR_V.fullmatch(str(norm_color(R.get(name, ""))).strip()) else "other")
        emit_at(root, theme_path(name), leaf_, name)

# ----------------------------------------------------- measured roles
#
# Roles measured on the real pages; each aliases to the declared token its
# value matches.

def res_color(name, theme):
    v = (R if theme == "light" else D).get(name)
    return norm_color(v) if v is not None else None


role_alias = {"light": {}, "dark": {}}
# A colour several roles share must resolve to the same alias every build:
# set iteration order differs across Python processes, and an alphabetical
# sort alone would pin theme.badge.fg as the canonical #000000. Rank the
# roles a label should prefer (the semantic roles before component-specific
# badge/btn/form leaves), then sort by name so the pick is deterministic.
ALIAS_FIRST = ["theme.bg", "theme.fg.default", "theme.fg.muted",
               "theme.border.default", "theme.card.bg", "theme.form.input.bg",
               "theme.btn.primary.fg"]
ALIAS_RANK = {p: i for i, p in enumerate(ALIAS_FIRST)}
for name in sorted(mode_names, key=lambda n: (ALIAS_RANK.get(EMITTED.get(n) or "", len(ALIAS_RANK)), n)):
    p = EMITTED.get(name)
    if not p:
        continue
    lc, dc = res_color(name, "light"), res_color(name, "dark")
    if lc:
        role_alias["light"].setdefault(lc, p)
    if dc:
        role_alias["dark"].setdefault(dc, p)


def semcolor(raw, src, desc, theme="light"):
    alias = role_alias[theme].get(norm_color(raw))
    value = f"{{{alias}}}" if alias else norm_color(raw)
    return lit(value, "color", src + (f"; matches declared {alias}" if alias else ""), desc)


sem = SPEC["light"]
for key, comp, state, prop, group, desc in [
    ("ink", "hero-h1", "default", "color", "text",
     "The near-black ink on display copy, headings and body."),
    ("navInk", "nav-pricing", "default", "color", "text",
     "The header link ink."),
    ("ctaFill", "nav-cta", "default", "backgroundColor", "action",
     "The black fill of the 'Get started'/'Get started for free' CTA pills."),
    ("ctaInk", "nav-cta", "default", "color", "action",
     "The white text on the dark CTA pill."),
    ("ctaHover", "nav-cta", "hover", "backgroundColor", "action",
     "The CTA pill's hover fill — the 15%-lifted black wash."),
    ("focusRing", "nav-cta", "focus-visible", "outlineColor", "border",
     "The keyboard focus ring colour on the header CTA."),
    ("fieldBg", "field-email", "default", "backgroundColor", "form",
     "The 8%-black contact field fill (form-input-bg)."),
    ("fieldInk", "field-email", "default", "color", "form",
     "The field text ink."),
    ("placeholder", "field-email", "default", "placeholder", "form",
     "The placeholder ink (form-placeholder)."),
    ("submitFill", "next-btn", "default", "backgroundColor", "action",
     "The 'Next step' button fill on the contact form."),
    ("submitInk", "next-btn", "default", "color", "action",
     "The 'Next step' button text."),
    ("planCardBg", "plan-card", "default", "backgroundColor", "surface",
     "The plan card's tinted fill on /pricing."),
]:
    try:
        if prop == "color":
            # The element's own `color` is often inherited onto an unpainted
            # wrapper; the kit's first-text-node reading is the painted ink.
            raw = ts(comp, state, "color")
            src = f"computed color of {comp} {state} — the first text node's reading where the kit recorded one (raw/components-computed.json)"
        elif prop == "placeholder":
            raw = (C[comp]["states"][state].get("placeholder") or {}).get("color")
            src = f"computed ::placeholder color of {comp} {state} (raw/components-computed.json)"
        elif prop == "insetShadowColor":
            raw = inset_shadow_color(comp, state)
            src = f"the inset box-shadow layer painted on {comp} {state} (raw/components-computed.json)"
        else:
            raw = st(comp, state)[prop]
            src = f"computed {prop} of {comp} {state} (raw/components-computed.json)"
        if raw in (None, "") or (prop == "backgroundColor" and TRANSPARENT.fullmatch(str(raw).strip())):
            raise KeyError(prop)
        sem.setdefault(group, {})[key] = semcolor(raw, src, desc, "light")
    except KeyError:
        pass

# The white page field: --fig-theme-bg paints the whole marketing surface.
if declared("--fig-theme-bg") is not None:
    sem.setdefault("background", {})["page"] = lit(
        "{theme.bg}", "color",
        "the :root --fig-theme-bg resolved on the marketing pages (raw/css-vars.json); visible as the white field behind every page (screenshots/*-light-*.png)",
        "The white page field — --fig-theme-bg.")

# ------------------------------------------------------------- type ramp
#
# Measured steps that land on declared sizes alias them.

size_alias = {}
for name in sorted(k for k in R if re.fullmatch(r"--fig-typography-size-[a-zA-Z0-9]+", k)):
    size_alias.setdefault(str(R[name]), f"font.size.{name[len('--fig-typography-size-'):]}")
for key, comp, state, desc in [
    ("hero", "hero-h1", "default", "The hero display heading — aliases --fig-typography-size-display* where it matches."),
    ("body", "section-h2", "default", "A section heading size."),
]:
    try:
        raw = st(comp, state)["fontSize"]
        src = f"computed fontSize of {comp} {state} (raw/components-computed.json)"
        alias = size_alias.get(raw)
        SPEC["core"].setdefault("font", {}).setdefault("size", {}).setdefault("measured", {})[key] = lit(
            f"{{{alias}}}" if alias else raw, "dimension",
            src + (f"; matches declared {alias}" if alias else ""), desc)
    except KeyError:
        pass

# ------------------------------------------------------------------ shape

for key, comp, state, prop, desc in [
    ("cta", "nav-cta", "default", "borderTopLeftRadius", "The CTA pill radius — the 9999px full pill (radius-full)."),
    ("navLink", "nav-pricing", "default", "borderTopLeftRadius", "The header link radius."),
    ("card", "plan-card", "default", "borderTopLeftRadius", "The plan-card corner radius."),
    ("field", "field-email", "default", "borderTopLeftRadius", "The contact field radius."),
    ("dropdown", "nav-panel", "default", "borderTopLeftRadius", "The products-dropdown panel corner radius."),
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
            radii[key] = lit(f"{{radius.{dkey}}}", "dimension", src + f"; matches declared --fig-radius-{dkey}", desc)
        else:
            radii[key] = lit(v, "dimension" if re.fullmatch(r"-?[0-9.]+(px|rem)", v or "") else "other", src, desc)
    except KeyError:
        pass

# ------------------------------------------------------------------ motion

mo = SPEC["core"].setdefault("motion", {})
try:
    s = st("nav-cta", "default")
    dur, ease = s.get("transitionDuration"), s.get("transitionTimingFunction")
    if dur and dur != "0s":
        # A CSS transition list pairs every comma entry with its own duration
        # and easing; dur/ease are themselves comma lists, so each property is
        # paired index-wise (the components.md builder reads them the same
        # way), never with the whole list appended per property.
        props = [p.strip() for p in s.get("transitionProperty", "all").split(",") if p.strip()]
        durs = [d.strip() for d in dur.split(",")]
        tfs = re.findall(r"cubic-bezier\([^)]*\)|steps\([^)]*\)|[a-z-]+", ease or "")
        parts = []
        for i, p in enumerate(props):
            d = durs[i % len(durs)]
            if d == "0s":
                continue
            parts.append(f"{p} {d} {tfs[i % len(tfs)] if tfs else ''}".strip())
        if parts:
            mo["control"] = lit(", ".join(parts), "other",
                "computed transition of nav-cta default (raw/components-computed.json); the --fig-animation-* steps are the declared durations",
                "The control transition on the header CTA.")
except KeyError:
    pass

# ------------------------------------------------------------- components

comp = SPEC["component"]
for name, cname, state, prop, ty_, desc in [
    ("topbar-height", "mkt-header", "default", "h", "dimension", "The marketing header bar height."),
    ("cta-height", "nav-cta", "default", "h", "dimension", "The header CTA pill height."),
    ("dropdown-width", "nav-panel", "default", "w", "dimension", "The open products-dropdown panel width."),
    ("hero-headline-width", "hero-h1", "default", "w", "dimension", "The hero display heading's measure."),
    ("field-height", "field-email", "default", "h", "dimension", "The contact field height."),
    ("topic-field-width", "field-topic", "default", "w", "dimension", "The topic input width on the sales form's first step."),
    ("next-width", "next-btn", "default", "w", "dimension", "The 'Next step' button width."),
    ("next-height", "next-btn", "default", "h", "dimension", "The 'Next step' button height."),
    ("plan-card-width", "plan-card", "default", "w", "dimension", "The plan-card column width."),
    ("toggle-width", "price-toggle", "default", "w", "dimension", "The Monthly/Annual toggle width."),
    ("comm-card-width", "comm-card", "default", "w", "dimension", "A community resource card's width."),
    ("comm-search-width", "comm-search", "default", "w", "dimension", "The community search input width."),
    ("mobile-topbar-height", "m-topbar", "default", "h", "dimension", "The phone header bar height."),
]:
    try:
        v = rc(cname, state, prop)
        comp[name] = lit(("%g" % v) + "px" if isinstance(v, (int, float)) else str(v) + "px",
                         ty_, f"measured {prop} of {cname} {state} (raw/components-computed.json)", desc)
    except KeyError:
        pass

# The product app shell (/community, /login, /signup) is a different stack
# that does not share the marketing --fig-* layer; its measured values are
# kept as literals, honestly labelled.
shell = comp.setdefault("productShell", {})
for name, cname, state, prop, ty_, desc in [
    ("login-panel-width", "login-panel", "default", "w", "dimension", "The sign-in card width on /login."),
    ("login-field-height", "login-email", "default", "h", "dimension", "The sign-in e-mail field height."),
    ("login-submit-fill", "login-submit", "default", "backgroundColor", "color", "The 'Log in' button fill on the product shell."),
    ("login-submit-ink", "login-submit", "default", "color", "color", "The 'Log in' button text."),
    ("google-btn-fill", "login-google", "default", "backgroundColor", "color", "The 'Continue with Google' button fill."),
    ("comm-signup-fill", "comm-signup", "default", "backgroundColor", "color", "The community 'Sign up' button fill (the product shell's accent)."),
    ("comm-signup-ink", "comm-signup", "default", "color", "color", "The community 'Sign up' button text."),
    ("comm-search-bg", "comm-search", "default", "backgroundColor", "color", "The community search field fill."),
]:
    try:
        if prop in ("w", "h"):
            v = rc(cname, state, prop)
            shell[name] = lit(("%g" % v) + "px", ty_, f"measured {prop} of {cname} {state} on the product app shell (raw/components-computed.json)", desc)
        else:
            shell[name] = lit(norm_color(opaque(st(cname, state)[prop])), "color",
                f"computed {prop} of {cname} {state} on the product app shell (raw/components-computed.json)", desc)
    except KeyError:
        pass

(RAW / "component-tokens.json").write_text(json.dumps(SPEC, indent=2, ensure_ascii=False) + "\n")
print("component-tokens.json:", {k: len(v) for k, v in SPEC.items() if k != "_about"})
