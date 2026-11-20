#!/usr/bin/env python3
"""Write raw/component-tokens.json, the token spec build_tokens.py reads.

elevenreader.io is a Next.js site over Tailwind v4 that declares a real
design-token layer — harvested into raw/css-vars.json by
tools/capture/vars.mjs:

  --themed-*        RGB triplets, re-bound on a .dark scope (nothing on the
                    public surface applies .dark — the dark set is a declared
                    inversion, documented as such)
  --color-*         rgb(var(--themed-*)) roles plus the full Tailwind default
                    palette, all resolved per theme
  --f-*             the type scale: display, heading, subhead, description,
                    body and ui roles, each size/weight/leading/tracking
  --font-*          family stacks and weights
  --spacing-*       the 4px base unit, gutters and section spacing
  --container-*     the layout container steps
  --ease-*, --focus-ring, --grid-columns, --reader-*
                    motion, focus, grid and the reader app's declared palette

Public surfaces paint light. The .dark scope inverts the same --themed-*
triplets, so a single {"var": "--color-*"} leaf resolves light in the light
pass and dark in the dark pass. Painted-but-undeclared values (the promo
band #F5F3F1, the FAQ tint #FAF8F8, the plan card #FDFCFC, the Save badge,
the black hover #6E6E6E, the measured 9999px pill radius) are measured
leaves from raw/components-computed.json.
"""
import json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
V = json.loads((RAW / "css-vars.json").read_text())
RES = V.get("resolved", {})
RL = RES.get("light", {})
C = json.loads((RAW / "components-computed.json").read_text())["components"]
R = {n: v.get("value", v.get("raw")) for n, v in RL.items()}


def var(name, ty="color", **kw):
    d = {"var": name, "type": ty}
    d.update(kw)
    return d


SPEC = {"_about": (
    "The token tree build_tokens.py turns into tokens.json. elevenreader.io "
    "declares a Tailwind v4 token layer (--themed-* RGB triplets bound into "
    "--color-* roles, a --f-* type scale, --font-*, --spacing-*, --container-*) "
    "and paints every public surface light; the stylesheet's .dark scope "
    "inverts the same triplets but no public page applies it, so the dark set "
    "is a declared inversion, not a painted surface. Declared variables become "
    "var leaves; painted values without a variable are measured leaves from "
    "raw/components-computed.json."),
    "core": {}, "light": {}, "dark": {}, "component": {}}


def descend(root, parts):
    node = root
    for p in parts[:-1]:
        child = node.setdefault(p, {})
        if "var" in child or "value" in child or "$value" in child:
            node[p] = {"default": child}
            child = node[p]
        node = child
    last = parts[-1]
    cur = node.get(last)
    if isinstance(cur, dict) and cur and not ("var" in cur or "value" in cur or "$value" in cur):
        node = cur
        node.setdefault("default", None)
        last = "default"
    return node, last


def place(root, parts, leaf):
    """Put a leaf at a token path. Two sources landing on one path (--color-foo and
    --color-foo-default, say) stop the build instead of one silently replacing the other."""
    node, last = descend(root, parts)
    if node.get(last) is not None:
        raise SystemExit(f"{'.'.join(parts)}: token path already holds a leaf")
    node[last] = leaf


def emit(root, name, leaf):
    place(root, name[2:].split("-"), leaf)


def st(comp, state):
    return C[comp]["states"][state]["style"]


def ts(comp, state, prop):
    """The first text node's reading (textStyle) when the kit recorded one —
    the wrapper's own fontSize can be the container's, not the text's."""
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


def shadow_layers(spec):
    """Parse 'rgba(...) x y blur sp [inset], ...' into DTCG shadow layers, dropping fully transparent no-ops."""
    out = []
    for m in re.finditer(
            r"(inset\s+)?(rgba?\(\s*[\d.]+,?\s*[\d.]+,?\s*[\d.]+(?:,?\s*[\d.]+)?\)|#[0-9a-fA-F]{3,8})\s+"
            r"(-?[\d.]+)px\s+(-?[\d.]+)px\s+(-?[\d.]+)px(?:\s+(-?[\d.]+)px)?(\s+inset)?", spec or ""):
        ins1, col, x, y, bl, sp, ins2 = m.groups()
        if col.startswith("rgba") and col.rstrip(")").endswith(", 0"):
            continue  # the rgba(0,0,0,0) placeholders Tailwind emits
        layer = {"color": norm_color(col), "offsetX": f"{x}px", "offsetY": f"{y}px",
                 "blur": f"{bl}px", "spread": f"{sp or 0}px"}
        if ins1 or ins2:  # an inner shadow stays inner
            layer["inset"] = True
        out.append(layer)
    return out


def measured_color(key, comp, state, prop, desc):
    try:
        v = norm_color(st(comp, state)[prop])
        if v and v != "rgba(0, 0, 0, 0)":
            return {"value": v, "type": "color",
                    "source": f"computed {prop} of {comp} {state} (raw/components-computed.json)",
                    "description": desc}
    except KeyError:
        return None


def measured_dim(key, comp, state, prop, desc):
    try:
        v = st(comp, state)[prop]
        if v:
            return {"value": v, "type": "dimension",
                    "source": f"computed {prop} of {comp} {state} (raw/components-computed.json)",
                    "description": desc}
    except KeyError:
        return None


# ------------------------------------------------------------------- fonts

fam = SPEC["core"].setdefault("font", {}).setdefault("family", {})
for key, comp, state, desc in [
    ("inter", "hero-cta", "default",
     "Inter (+ its 'Inter Fallback' metrics clone): every UI, body and form "
     "text on the public surface."),
    ("waldenburg", "hero-h1", "default",
     "Waldenburg: the display face on h1s, pricing/audiobook titles, section "
     "heads and the FAQ."),
]:
    if have(comp, state, "fontFamily"):
        fam[key] = {"value": st(comp, state)["fontFamily"], "type": "fontFamily",
                    "source": f"computed fontFamily of {comp} {state} (raw/components-computed.json)",
                    "description": desc}
for key, vname, desc in [
    ("sans", "--font-sans", "The declared system-ui fallback stack (--font-sans)."),
    ("serif", "--font-serif", "The declared serif fallback stack (--font-serif)."),
    ("mono", "--font-mono", "The declared monospace stack (--font-mono)."),
]:
    if vname in R:
        fam[key] = var(vname, "fontFamily", description=desc)

weight = SPEC["core"].setdefault("font", {}).setdefault("weight", {})
for name, desc in [
    ("normal", "400 — body, UI labels, the Waldenburg book weight."),
    ("medium", "500 — SSO buttons, badges, rail links, footer columns."),
    ("semibold", "600 — declared."),
    ("bold", "700 — the declared f-* bold steps (uppercase UI labels)."),
]:
    vname = f"--font-weight-{name}"
    if vname in R:
        weight[name] = var(vname, "fontWeight", description=desc)
# The Waldenburg headings paint 375/400 — the book weight the variable layer
# calls f-heading-*. Record the painted weight on the display role.
if have("hero-h1", "default", "fontWeight"):
    weight["display"] = {"value": int(st("hero-h1", "default")["fontWeight"]),
                         "type": "fontWeight",
                         "source": "computed fontWeight of hero-h1 default (raw/components-computed.json)",
                         "description": "The painted Waldenburg weight on h1s (400 — the f-heading steps declare 700 but the loaded book face paints lighter)."}

# ------------------------------------------------------------- color ramps
# The --color-* layer: themed roles (re-bound on .dark) plus the full Tailwind
# default palette. Every declared var becomes a core token; themed vars carry
# their dark inversion automatically through the resolve pass.

color = SPEC["core"].setdefault("color", {})

THEMED = "declared --color-* var over the --themed-* triplets; the .dark scope inverts it"
PLAIN = "declared Tailwind v4 default palette var (same value both themes)"

# The themed ramps + named roles that make the design's own palette.
NAMED = {
    "black": "Black — the inverse fill, heading ink, focus ring (inverts to white on .dark).",
    "white": "White — the default surface and inverse text (inverts to black on .dark).",
    "accent": "Accent blue #4680fd — the declared action accent (declared; the marketing surface paints black/white).",
    "surface": "Surface #f6f6f6 — the nav-link hover fill and raised card tone.",
    "hovered": "Hovered #f0f0f0 — the cover-card backing and hover fill.",
    "forest-green": "Forest green #003412 — a named brand hue (iconic-voices accents).",
    "magenta-light": "Magenta light #510142 — a named brand hue.",
    "tan": "Tan #ac8a65 — a named brand hue.",
    "mauve": "Mauve #9967a0 — a named brand hue.",
    "sage": "Sage #96bda3 — a named brand hue.",
    "pink": "Pink #e099ad — a named brand hue.",
    "sea": "Sea #94c1c5 — a named brand hue.",
    "sky-blue": "Sky blue #98c7eb — a named brand hue.",
    "lime": "Lime #d9de95 — a named brand hue.",
    "gold": "Gold #fdb95f — a named brand hue.",
    "grapefruit": "Grapefruit #f58971 — a named brand hue.",
    "indigo": "Indigo #7072bc — a named brand hue.",
    "fog-gray": "Fog gray #babcd3 — a named brand hue.",
}

for name in sorted(n for n in R if n.startswith("--color-")):
    key = name[len("--color-"):]
    if key in ("transparent", "current", "inherit"):
        continue
    desc = NAMED.get(key)
    if desc is None:
        if re.fullmatch(r"(neutral|blue|cyan|green|yellow|magenta|red)-\d+", key):
            desc = f"Themed {key.replace('-', ' ')} step — re-bound on .dark."
            ty_src = THEMED
        elif re.fullmatch(r"(black|white)-alpha-\d+", key):
            desc = f"Declared {key.replace('-', ' ')} translucency — overlays, veils, scrims."
            ty_src = THEMED
        else:
            ty_src = PLAIN
            desc = f"Tailwind v4 palette {key} (declared)."
    else:
        ty_src = THEMED
    place(color, key.split("-"), var(name, "color", source=ty_src, description=desc))

# Measured paints that have no declared variable.
meas_col = color.setdefault("painted", {})
for key, comp, state, prop, desc in [
    ("banner", "promo-banner", "default", "backgroundColor",
     "The #F5F3F1 announcement-band fill (arbitrary value, not a token var)."),
    ("faq", "faq-item", "default", "backgroundColor",
     "The #FAF8F8 closed-FAQ tint (arbitrary value)."),
    ("plan-card", "plan-card", "default", "backgroundColor",
     "The #FDFCFC plan-card field (the reader-page off-white, arbitrary)."),
    ("plan-card-border", "plan-card", "default", "borderTopColor",
     "The #EAE9E9 plan-card hairline (arbitrary rgba)."),
    ("save-badge-bg", "save-badge", "default", "backgroundColor",
     "The #E1F5E0 Save-25% badge fill (arbitrary value)."),
    ("save-badge-fg", "save-badge", "default", "color",
     "The #307D18 Save-25% badge text (arbitrary value)."),
    ("primary-hover", "hero-cta", "hover", "backgroundColor",
     "The #6E6E6E dark-button hover (bg-darkest role, painted not declared)."),
    ("overlay-hover", "sso-google", "hover", "backgroundColor",
     "The 10% black overlay the secondary buttons paint on hover (bg-overlay-darker)."),
    ("input-border", "email-field", "default", "borderTopColor",
     "The #E5E5E5 input hairline (border-gray-alpha-200)."),
    ("menu-hairline", "nav-dropdown", "default", "borderTopColor",
     "The #F2F2F2 mega-menu border."),
]:
    m = measured_color(key, comp, state, prop, desc)
    if m:
        meas_col[key] = m

# The reader app's own declared palette — themed, unpainted on the public
# surface but part of the product's token layer.
reader = color.setdefault("reader", {})
for key, desc in [
    ("page-bg", "Reader page background (#ffffff light / #000000 dark)."),
    ("active-sentence-bg", "Active-sentence highlight (#ddf5ff)."),
    ("active-word-bg", "Active-word highlight (#73dbf2)."),
    ("bookmark-bg", "Bookmark fill (#fff7dc)."),
    ("bookmark-hover-bg", "Bookmark hover fill (#ffe69c)."),
    ("find-match-bg", "Find-match highlight (#fff1a8)."),
    ("find-current-bg", "Current find match (#ffc94a)."),
    ("podcast-warning-bg", "Podcast warning fill."),
    ("podcast-warning-text", "Podcast warning text."),
]:
    canon = {"page-bg": "--reader-page-bg",
             "active-sentence-bg": "--reader-active-sentence-bg-color",
             "active-word-bg": "--reader-active-word-bg-color",
             "bookmark-bg": "--reader-bookmark-bg-color",
             "bookmark-hover-bg": "--reader-bookmark-hover-bg-color",
             "find-match-bg": "--reader-find-match-bg-color",
             "find-current-bg": "--reader-find-current-bg-color",
             "podcast-warning-bg": "--reader-podcast-warning-bg-color",
             "podcast-warning-text": "--reader-podcast-warning-text-color"}[key]
    if canon in R:
        reader[key] = var(canon, "color",
                          description=desc + " (reader app role; declared on the site sheet, unpainted on the public surface)")

# ------------------------------------------------------------- type scale
# One composite per f-* role, resolved on the light pass at 1440px (the sheet
# steps sizes at min-width: 40rem / 64rem / 80rem; the mobile base is recorded
# on the leaf's responsive extension).

typestyles = SPEC["core"].setdefault("typography", {})
FAMILY = {"display": "{font.family.inter}", "heading": "{font.family.waldenburg}",
          "subhead": "{font.family.inter}", "description": "{font.family.inter}",
          "body": "{font.family.inter}", "ui": "{font.family.inter}"}
FAM_DESC = {"display": "display", "heading": "Waldenburg heading",
            "subhead": "bold subhead", "description": "lede/description",
            "body": "body", "ui": "UI label"}
for role in ["display", "heading", "subhead", "description", "body", "ui"]:
    for i in range(1, 9):
        n = f"--f-{role}-0{i}-font-size"
        if n not in R:
            continue
        base = f"--f-{role}-0{i}"
        # the mobile (base) declaration sits in the theme rules before the
        # min-width overrides; the resolved pass holds the 1440px value.
        # The resolved letter-spacing came from a generic probe element, so an
        # em value resolved against the probe's font size, not the role's:
        # heading.04's .01em resolved to 0.171875px where the 32px role makes
        # it 0.32px. Re-resolve the declared relative value against this
        # step's own font-size; an already-absolute value passes through.
        ls = R.get(base + "-letter-spacing", "0px")
        ls_raw = str((RL.get(base + "-letter-spacing") or {}).get("raw") or "").strip()
        m = re.fullmatch(r"(-?[\d.]+)em", ls_raw)
        if m:
            ls = f"{float(R[base + '-font-size'].rstrip('px')) * float(m.group(1)):g}px"
        val = {"fontFamily": FAMILY[role],
               "fontSize": R[base + "-font-size"],
               "fontWeight": int(float(R.get(base + "-font-weight", "400"))),
               "lineHeight": float(R.get(base + "-line-height", "100%").rstrip("%")) / 100,
               "letterSpacing": ls}
        if R.get(base + "-text-transform"):
            val["textTransform"] = R[base + "-text-transform"]
        leaf = {"$value": val, "$type": "typography",
                "$extensions": {"source": f"css-var {base}-* (light, resolved at 1440px)"},
                "$description": f"The f-{role}-0{i} {FAM_DESC[role]} step (desktop 1440px; the sheet steps it down at <80rem and <64rem)."}
        node = typestyles.setdefault(role, {})
        node[f"0{i}"] = leaf

# ---------------------------------------------------------- radius, easing

radius = SPEC["core"].setdefault("radius", {})
if have("hero-cta", "default", "borderTopLeftRadius"):
    radius["pill"] = {"value": st("hero-cta", "default")["borderTopLeftRadius"], "type": "dimension",
                      "source": "computed borderTopLeftRadius of hero-cta default (raw/components-computed.json)",
                      "description": "The 9999px pill every button, chip, input and badge paints (rounded-full)."}
if "--shadcn-radius" in R:
    radius["shadcn"] = var("--shadcn-radius", "dimension",
                           description="The declared 8px shadcn radius (book covers, small cards).")
for key, comp, state, desc in [
    ("faq", "faq-item", "default", "The 20px FAQ-item radius."),
    ("plan-card", "plan-card", "default", "The 40px plan-card radius."),
    ("cover-orbit", "book-cover", "default", "The 16px orbit cover-card radius."),
    ("compare-link", "cmp-link", "default", "The 10px compare-link radius."),
]:
    if have(comp, state, "borderTopLeftRadius"):
        radius[key] = {"value": st(comp, state)["borderTopLeftRadius"], "type": "dimension",
                       "source": f"computed borderTopLeftRadius of {comp} {state} (raw/components-computed.json)",
                       "description": desc}

easing = SPEC["core"].setdefault("easing", {})
for key, vname, desc in [
    ("standard", "--default-transition-timing-function", "The default transition curve (cubic-bezier(.4,0,.2,1))."),
    ("out", "--ease-out", "Declared ease-out (0,0,.2,1)."),
    ("in-out", "--ease-in-out", "Declared ease-in-out (.4,0,.2,1)."),
]:
    if vname in R:
        easing[key] = var(vname, "cubicBezier", description=desc)

duration = SPEC["core"].setdefault("duration", {})
if "--default-transition-duration" in R:
    duration["default"] = var("--default-transition-duration", "duration",
                              description="The declared default transition duration (0.15s).")

# ------------------------------------------------------------- space, layout

spacing = SPEC["core"].setdefault("spacing", {})
if "--spacing" in R:
    spacing["unit"] = var("--spacing", "dimension",
                          description="The 4px Tailwind base unit every spacing utility multiplies.")
for name, desc in [
    ("inner-gutter", "Inner gutter (20px at 1440px)."),
    ("outer-gutter", "Outer gutter (64px at 1440px)."),
    ("outer-content", "Outer content spacing (100px)."),
    ("content-wide", "Wide content spacing (160px)."),
    ("content-xwide", "Extra-wide content spacing (200px)."),
]:
    vname = f"--spacing-{name}"
    if vname in R:
        spacing[name] = var(vname, "dimension",
                            description=desc + " Declared --spacing var; responsive.")

layout = SPEC["core"].setdefault("layout", {})
for key, vname, desc in [
    ("container-sm", "--container-sm", "Container sm (384px)."),
    ("container-md", "--container-md", "Container md (448px)."),
    ("container-2xl", "--container-2xl", "Container 2xl (672px)."),
    ("container-3xl", "--container-3xl", "Container 3xl (768px)."),
    ("container-4xl", "--container-4xl", "Container 4xl (896px)."),
    ("container-5xl", "--container-5xl", "Container 5xl (1024px)."),
    ("container-6xl", "--container-6xl", "Container 6xl (1152px)."),
]:
    if vname in R:
        layout[key] = var(vname, "dimension", description=desc)
if "--grid-columns" in R:
    layout["grid-columns"] = var("--grid-columns", "number",
                                 description="The declared 12-column grid.")
for key, comp, state, prop, desc in [
    ("container", "header", "default", "width", "The 1304px content width inside the 1440px viewport (inner + outer gutters)."),
    ("header-height", "header", "default", "height", "The 64px header bar."),
    ("header-height-mobile", "m-header", "default", "height", "The 64px mobile header."),
    ("promo-height", "promo-banner", "default", "height", "The 49px promo band."),
]:
    m = measured_dim(key, comp, state, prop, desc)
    if m:
        layout[key] = m

# ----------------------------------------------------------------- shadows

shadow = SPEC["core"].setdefault("shadow", {})
if "--drop-shadow-lg" in R:
    layers = shadow_layers(R["--drop-shadow-lg"])
    if layers:
        shadow["drop-lg"] = {"value": layers, "type": "shadow",
                             "source": "css-var --drop-shadow-lg (light)",
                             "description": "The declared lg drop shadow (rgba(0,0,0,.15) 0 4 4)."}
# The layered ring shadow the white pills, chips, fields and selected billing
# segment paint (Tailwind shadow-input + shadow lift).
for key, comp, state, desc in [
    ("pill", "hero-cta-2", "default", "The layered ring shadow the secondary pills paint (ring 6% + 1px/2px lifts, 4% black)."),
    ("menu", "nav-dropdown", "default", "The mega-menu/card elevation (16,24,40 at .03/.08)."),
    ("faq-open", "faq-item", "open", "The open-FAQ lift (1px ring 40% + 1-2px lifts 4%)."),
]:
    try:
        layers = shadow_layers(st(comp, state)["boxShadow"])
        if layers:
            shadow[key] = {"value": layers, "type": "shadow",
                           "source": f"computed boxShadow of {comp} {state} (raw/components-computed.json)",
                           "description": desc}
    except KeyError:
        pass

# ---------------------------------------------------------------- measured

meas = SPEC["core"].setdefault("measured", {})
# The keyboard focus ring: a 2px solid black outline, offset 2px.
try:
    s = st("hero-cta", "focus-visible")
    if s.get("outlineWidth"):
        meas["focus-ring"] = {"value": norm_color(s["outlineColor"]), "type": "color",
                              "source": "computed outline of hero-cta focus-visible (raw/components-computed.json)",
                              "description": f"The {s['outlineWidth']} solid {norm_color(s['outlineColor'])} keyboard-focus outline (offset {s.get('outlineOffset')}); the declared --focus-ring var inverts to white on .dark."}
        meas["focus-ring-width"] = {"value": s["outlineWidth"], "type": "dimension",
                                    "source": "computed outlineWidth of hero-cta focus-visible (raw/components-computed.json)",
                                    "description": "The 2px focus outline width."}
        meas["focus-ring-offset"] = {"value": s["outlineOffset"], "type": "dimension",
                                     "source": "computed outlineOffset of hero-cta focus-visible (raw/components-computed.json)",
                                     "description": "The 2px focus outline offset."}
except KeyError:
    pass
# transitions worth naming
for key, comp, state, desc in [
    ("color", "hero-cta", "default", "The standard colour/background transition."),
    ("menu", "nav-dropdown", "default", "The mega-menu open animation."),
    ("faq", "faq-item", "default", "The FAQ open/close animation."),
    ("mobile-menu", "m-menu-open", "default", "The mobile menu slide-in."),
]:
    try:
        s = st(comp, state)
        d = (s.get("transitionDuration") or "").split(",")[0].strip()
        if d and d != "0s":
            meas[key] = {"value": d, "type": "duration",
                         "source": f"computed transition of {comp} {state} (raw/components-computed.json)",
                         "description": desc + f" ({s.get('transitionProperty')})"}
    except (KeyError, TypeError):
        pass

# -------------------------------------------------------------------- roles
# Semantic roles over the palette. The same var leaf resolves per theme — the
# .dark scope inverts the themed triplets, so one spec line serves both sets.

ALIAS = "role alias over the core palette"
DECL = "declared --color-* role"


def role(name, ref, ty="color", desc=""):
    return {"value": ref, "type": ty, "source": ALIAS, "description": desc}


ROLES = [
    # (token path, var name, description)  — emitted into light and dark
    ("surface.page", "--color-white", "The default page field (bg-default)."),
    ("surface.card", "--color-surface", "The raised card surface (#f6f6f6)."),
    ("surface.hovered", "--color-hovered", "The hover fill (#f0f0f0)."),
    ("surface.inverse", "--color-black", "The inverse fill — dark buttons, chips-on-dark (bg-inverse)."),
    ("surface.sunken", "--color-neutral-50", "The sunken surface — the Google SSO fill, cover backings (bg-dark)."),
    ("surface.overlay", "--color-black-alpha-5", "The 5% overlay fill (bg-overlay)."),
    ("surface.overlayDarker", "--color-black-alpha-10", "The 10% overlay — secondary-button hover (bg-overlay-darker)."),
    ("surface.scrim", "--color-black-alpha-60", "The 60% scrim (bg-overlay-darkest)."),
    ("surface.informative", "--color-blue-200", "Informative surface (bg-informative)."),
    ("surface.positive", "--color-green-200", "Positive surface (bg-positive)."),
    ("surface.negative", "--color-red-200", "Negative surface (bg-negative)."),
    ("surface.warning", "--color-yellow-100", "Warning surface (bg-warning)."),
    ("text.default", "--color-black", "Primary text (text-default)."),
    ("text.secondary", "--color-neutral-600", "Secondary text (text-light-ish)."),
    ("text.muted", "--color-neutral-500", "Muted text (text-lighter)."),
    ("text.faint", "--color-neutral-400", "Faint text (text-lightest)."),
    ("text.inverse", "--color-white", "Text on inverse fills (text-inverse)."),
    ("text.inverseMuted", "--color-neutral-200", "Muted text on dark (text-inverse-light)."),
    ("text.accent", "--color-accent", "Accent text/link (text-accent)."),
    ("text.error", "--color-red-500", "Error text (text-error)."),
    ("text.negative", "--color-red-800", "Negative text on negative surfaces (text-negative)."),
    ("text.positive", "--color-green-800", "Positive text on positive surfaces (text-positive)."),
    ("border.default", "--color-neutral-100", "The default hairline (border-default)."),
    ("border.light", "--color-neutral-50", "The lighter hairline (border-light)."),
    ("border.strong", "--color-neutral-400", "Strong borders (border-strong)."),
    ("border.darker", "--color-neutral-900", "Darker borders (border-darker)."),
    ("border.darkest", "--color-black", "The darkest border (border-darkest)."),
    ("border.input", "--color-neutral-100", "Input hairline (border-gray-alpha-200 paints #E5E5E5)."),
    ("border.inverse", "--color-white", "Borders on inverse fills (border-inverse)."),
    ("border.negative", "--color-red-800", "Negative borders."),
    ("border.positive", "--color-green-800", "Positive borders."),
    ("accent", "--color-accent", "The declared accent blue (#4680fd)."),
    ("focusRing", "--focus-ring", "The declared focus ring (black light / white dark)."),
]

for theme in ("light", "dark"):
    bag = SPEC[theme]
    for path, name, desc in ROLES:
        if name in RES[theme]:
            place(bag, path.split("."), var(name, "color", source=DECL, description=desc))

# Painted roles without a declared var.
for key, comp, state, prop, desc in [
    ("surface.banner", "promo-banner", "default", "backgroundColor",
     "The #F5F3F1 announcement band (painted, not declared)."),
    ("surface.faq", "faq-item", "default", "backgroundColor",
     "The #FAF8F8 closed-FAQ tint."),
    ("surface.planCard", "plan-card", "default", "backgroundColor",
     "The #FDFCFC plan-card field."),
    ("surface.saveBadge", "save-badge", "default", "backgroundColor",
     "The #E1F5E0 Save-badge fill."),
    ("text.saveBadge", "save-badge", "default", "color",
     "The #307D18 Save-badge text."),
    ("surface.primaryHover", "hero-cta", "hover", "backgroundColor",
     "The #6E6E6E dark-button hover (bg-darkest)."),
    ("border.planCard", "plan-card", "default", "borderTopColor",
     "The #EAE9E9 plan-card hairline."),
]:
    m = measured_color(key, comp, state, prop, desc)
    if m:
        place(SPEC["light"], key.split("."), m)

# ------------------------------------------------------------------ component

comp = SPEC["component"]
for key, cname, state, prop, ty, desc in [
    ("header.height", "header", "default", "height", "dimension", "The 64px header bar."),
    ("header.height-mobile", "m-header", "default", "height", "dimension", "The 64px mobile header."),
    ("header.container", "header", "default", "width", "dimension", "The 1304px content column at 1440px."),
    ("logo.width", "logo", "default", "width", "dimension", "The wordmark width (164px rendered)."),
    ("button.height.nav", "nav-cta", "default", "height", "dimension", "The 36px nav pill."),
    ("button.height.cta", "hero-cta", "default", "height", "dimension", "The 52px hero/pricing CTA."),
    ("button.height.chip", "genre-chip", "default", "height", "dimension", "The 44px chip / view-all pill."),
    ("button.height.small", "promo-cta", "default", "height", "dimension", "The 32px promo pill."),
    ("button.height.sso", "sso-google", "default", "height", "dimension", "The 40px SSO / form pill."),
    ("button.radius", "hero-cta", "default", "borderTopLeftRadius", "dimension", "Every button paints the 9999px pill."),
    ("nav-link.height", "nav-link", "default", "height", "dimension", "Nav link height (36px)."),
    ("mega-menu.width", "nav-dropdown", "default", "width", "dimension", "The Discover mega-menu width (846px)."),
    ("field.height", "email-field", "default", "height", "dimension", "The 40px auth input."),
    ("field.radius", "email-field", "default", "borderTopLeftRadius", "dimension", "Inputs paint the full pill."),
    ("auth-card.width", "signin-card", "default", "width", "dimension", "The 360px max-w-90 auth card column."),
    ("plan-card.width", "plan-card", "default", "width", "dimension", "Plan card width (584px)."),
    ("plan-card.radius", "plan-card", "default", "borderTopLeftRadius", "dimension", "The 40px plan-card radius."),
    ("plan-cta.height", "plan-cta", "default", "height", "dimension", "The 52px plan CTA."),
    ("faq.radius", "faq-item", "default", "borderTopLeftRadius", "dimension", "The 20px FAQ radius."),
    ("faq.height-closed", "faq-item", "default", "height", "dimension", "The 67px closed FAQ row."),
    ("billing.height", "billing-on", "default", "height", "dimension", "The 48px billing segment."),
    ("cover.radius", "book-cover", "default", "borderTopLeftRadius", "dimension", "The 16px orbit cover radius."),
    ("mobile-menu.item-height", "m-nav-item", "default", "height", "dimension", "Mobile menu item row height (24px)."),
    ("mobile-menu.button", "m-menu-button", "default", "height", "dimension", "The 40px hamburger button."),
]:
    if have(cname, state, prop):
        node = comp
        parts = key.split(".")
        for p in parts[:-1]:
            node = node.setdefault(p, {})
        node[parts[-1]] = {"type": ty, "value": st(cname, state)[prop],
                           "source": f"computed {prop} of {cname} {state} (raw/components-computed.json)",
                           "description": desc}

# component state colours (aliases onto the roles where they exist)
statec = comp.setdefault("state", {})
for key, comp2, state, prop, desc in [
    ("button.primary.bg", "hero-cta", "default", "backgroundColor", "Primary pill fill (#000)."),
    ("button.primary.fg", "hero-cta", "default", "color", "Text on the primary pill (#fff)."),
    ("button.primary.hoverBg", "hero-cta", "hover", "backgroundColor", "Primary pill hover (#6E6E6E)."),
    ("button.secondary.bg", "hero-cta-2", "default", "backgroundColor", "Secondary pill fill (#fff)."),
    ("button.sso.bg", "sso-google", "default", "backgroundColor", "The SSO fill (bg-dark #F2F2F2)."),
    ("button.sso.hoverBg", "sso-google", "hover", "backgroundColor", "SSO hover (10% overlay)."),
    ("chip.bg", "genre-chip", "default", "backgroundColor", "Genre chip fill."),
    ("badge.save.bg", "save-badge", "default", "backgroundColor", "Save badge fill (#E1F5E0)."),
    ("badge.save.fg", "save-badge", "default", "color", "Save badge text (#307D18)."),
    ("field.border", "email-field", "default", "borderTopColor", "Input hairline (#E5E5E5)."),
    ("nav-link.hoverBg", "nav-link", "hover", "backgroundColor", "Nav-link hover fill."),
]:
    try:
        v = norm_color(st(comp2, state)[prop])
        if v and v != "rgba(0, 0, 0, 0)":
            node = statec
            parts = key.split(".")
            for p in parts[:-1]:
                node = node.setdefault(p, {})
            node[parts[-1]] = {"type": "color", "value": v,
                               "source": f"computed {prop} of {comp2} {state} (raw/components-computed.json)",
                               "description": desc}
    except KeyError:
        pass

(RAW / "component-tokens.json").write_text(json.dumps(SPEC, indent=1, ensure_ascii=False) + "\n")


def count(d):
    if not isinstance(d, dict):
        return 1
    if "var" in d or "value" in d or "$value" in d:
        return 1
    return sum(count(v) for v in d.values())


print({k: count(v) for k, v in SPEC.items() if not k.startswith("_")})
