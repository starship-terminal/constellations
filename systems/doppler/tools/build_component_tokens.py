#!/usr/bin/env python3
"""Write raw/component-tokens.json, the token spec build_tokens.py reads.

doppler.com is a Next.js/Tailwind marketing site; the whole public surface
paints one dark theme (warm-black #1c1624). Its token layer is not custom
properties — it is a named Tailwind utility palette and type scale, harvested
by tools/capture/vars.mjs into:

  raw/css-vars.json          the few real custom properties the bundle declares
                             (--global-ease/--global-transition on :root, the
                             --font-doppler-* / --font-inter stacks on the
                             .__variable_* classes) plus the 22 @font-face
                             declarations; `resolved.dark` is what the probe
                             resolves on the painted surface
  raw/utility-classes.json   the named utility declarations: the .bg-*/.text-*/
                             .border-* colour palette, the .text-h*/.text-p*/
                             .text-label*/.text-navLink type scale, the
                             rounded-*/shadow-*/ease-*/duration-* scale and the
                             .interactive-card / hover: / focus: / active:
                             state variants
  raw/components-computed.json  every component's computed styles and painted
                             layers per state (tools/capture/public/measure.mjs)

A leaf is {"var": "--name"} (resolved through raw/css-vars.json), {"value": ...,
"source": "..."} for a measured or class-declared value. Sources name the
evidence: "declared .bg-warm-black (raw/utility-classes.json)" for palette
values, "computed <prop> of <component> <state> (raw/components-computed.json)"
for measured ones.
"""
import json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
V = json.loads((RAW / "css-vars.json").read_text())
U = json.loads((RAW / "utility-classes.json").read_text())
C = json.loads((RAW / "components-computed.json").read_text())["components"]

# ----------------------------------------------------------- utility lookup
# The utility harvest keys every rule by its selector text; media-context
# rules keep their context list. cls(".bg-warm-black") -> properties dict.
def st(comp, state):
    c = C[comp]
    if c.get("missing") or c.get("recaptureMissed"):
        raise KeyError(comp)
    return c["states"][state]["style"]


def missed(comp):
    """A source note for a component a later run could not find (its states are an earlier run's)."""
    d = C[comp].get("recaptureMissed")
    return f"; the {d} run did not find {comp}, so these are its {C[comp].get('run')} states (recaptureMissed); recapture needed" if d else ""


def unescape(sel):
    return sel.replace("\\", "")

CLASSES = {}
for r in U.get("classes", []):
    sel = r.get("selector", "")
    props = r.get("properties", {})
    for s in sel.split(","):
        s = unescape(s.strip())
        CLASSES.setdefault(s, {}).update(props)
        CLASSES.setdefault(s + "|ctx:" + ">".join(r.get("context", [])), {}).update(props)


def cls(sel):
    """Declared properties of a single-class selector (media context allowed via |ctx:)."""
    if sel not in CLASSES:
        raise KeyError(sel + " not in raw/utility-classes.json")
    return CLASSES[sel]


def color_of(sel, prop="background-color"):
    return cls(sel).get(prop, "")


SPEC = {"_about": (
    "The token tree build_tokens.py turns into tokens.json. doppler.com is a "
    "Next.js/Tailwind marketing site painting one dark theme; its token layer "
    "is a named utility palette (.bg-warm-black, .text-silver, "
    ".bg-flourescent-green, .border-glow-stroke...) and a named type scale "
    "(.text-h1Mobile/.text-h3/.text-p2/.text-labelSm/.text-navLink), not a "
    "custom-property layer. \"var\" leaves resolve through raw/css-vars.json; "
    "\"value\" leaves cite the utility declaration or the measured component."),
    "core": {}, "dark": {}, "component": {}}


def put(root, path, leaf):
    node = root
    parts = path.split(".")
    for p in parts[:-1]:
        node = node.setdefault(p, {})
    node[parts[-1]] = leaf


# --------------------------------------------------------------- palette
# Named colour utilities -> token paths. The class name is the product's own
# name for the value; duplicates (.border-carmine == .bg-brand-orange) fold
# onto one token and are named in the description.
PALETTE = [
    # warm darks
    ("warm.black", ".bg-warm-black", "background-color", "warm-black #1c1624: the page ground the whole surface paints."),
    ("warm.basalt", ".bg-basalt", "background-color", "basalt #241e2c: a slightly lifted warm-black (sections, overlays)."),
    ("warm.charcoal", ".bg-charcoal", "background-color", "charcoal #45403d: raised warm fills and gradient ends."),
    ("warm.stone", ".border-stone-700", "border-color", "stone-700 #44403c: the spend field's border and dark UI lines."),
    ("warm.raised", ".bg-[#2D2734]", "background-color", "#2d2734: the inactive filter/category chip fill."),
    ("warm.badge", ".bg-[#302C37]", "background-color", "#302c37: the plan badge's fill."),
    ("warm.glowStrokeLight", ".border-glow-stroke-light", "border-color", "glow-stroke-light #55505b: the opaque header/dropdown hairline."),
    # warm neutrals
    ("neutral.warmWhite", ".text-warm-white", "color", "warm-white #f1f0ec: primary text and borders."),
    ("neutral.cloud", ".text-cloud", "color", "cloud #e5e8ed: near-white secondary text."),
    ("neutral.silver", ".text-silver", "color", "silver #d0c9c4: muted body text, nav links, placeholders."),
    ("neutral.aluminum", ".text-aluminum", "color", "aluminum #8b877d: deepest muted text and field borders."),
    ("neutral.white", ".bg-white", "background-color", "pure white, used sparingly (logos, glows)."),
    ("neutral.black", ".bg-black", "background-color", "pure black, used for deep fills."),
    # brand hues
    ("brand.orange", ".bg-brand-orange", "background-color", "brand-orange / carmine #f55c15: Doppler's signature orange — inline code, gradient ends, accents (.border-carmine and .text-carmine resolve to the same value)."),
    ("brand.orange300", ".bg-orange-300", "background-color", "orange-300 #fdba74: a soft orange tint."),
    ("brand.purple", ".bg-purple", "background-color", "purple #6b13f5: the secondary brand hue (gradients, glows)."),
    ("brand.lightPurple", ".text-light-purple", "color", "light-purple #b997ff: section headings, chip hover, field focus, active filters."),
    ("brand.lilac", ".text-lilac", "color", "lilac #ff9efa: gradient midpoint."),
    ("brand.green", ".bg-flourescent-green", "background-color", "flourescent-green #00f575: the primary CTA fill (spelled 'flourescent' in the bundle)."),
    ("brand.greenDark", ".active:bg-flourescent-green-dark:active", "background-color", "flourescent-green-dark #00bf5b: CTA hover/pressed fill and hover text."),
    ("brand.red", ".text-flourescent-red", "color", "flourescent-red #ff5449: errors and warnings."),
    ("brand.redDark", ".bg-red-600", "background-color", "red-600 #dc2626."),
    ("brand.yellow", ".bg-yellow-300", "background-color", "yellow-300 #fde047."),
    # status tints
    ("tint.green", ".bg-subtle-green", "background-color", "subtle-green: #69fc51 at 8% — success surfaces."),
    ("tint.orange", ".bg-subtle-orange", "background-color", "subtle-orange: #fc9c51 at 8% — warning surfaces."),
    ("tint.red", ".bg-subtle-red", "background-color", "subtle-red: #fc6151 at 8% — error surfaces."),
    # warm-white alphas (the bundle names them 'black4' etc. though they are white)
    ("alpha.w4", ".bg-black4", "background-color", "black4 rgba(242,241,237,0.04): card grounds, chip fills, code chips — a warm-white 4% veil."),
    ("alpha.w8", ".bg-black8", "background-color", "black8 rgba(242,241,237,0.08): hover fills."),
    ("alpha.w32", ".bg-black32", "background-color", "black32 rgba(242,241,237,0.32)."),
    ("alpha.w64", ".text-black64", "color", "black64 rgba(242,241,237,0.64): disabled/secondary text."),
    ("alpha.glow", ".border-glow-stroke", "border-top-color", "glow-stroke rgba(255,255,255,0.08): the translucent hairline on cards, footer links and dividers."),
    ("alpha.w8border", ".border-black8", "border-top-color", "black8 rgba(242,241,237,0.08) as a border colour."),
]

for path, sel, prop, desc in PALETTE:
    try:
        v = color_of(sel, prop)
    except KeyError:
        raise SystemExit(f"declared utility missing for {path}: {sel}")
    if not v:
        raise SystemExit(f"{sel} has no {prop}")
    put(SPEC["core"].setdefault("color", {}), path,
        {"value": v, "type": "color", "source": f"declared {sel} {prop} (raw/utility-classes.json)", "description": desc})


# ----------------------------------------------------------------- fonts
# The three families resolve through the --font-* vars on the .__variable_*
# classes and paint through .font-sans / .font-mono / .font-inter.
# The three families resolve through the --font-* vars on the .__variable_* classes and paint
# through .font-sans / .font-mono / .font-inter. Each stack is the computed fontFamily of a
# component that paints it (Next.js's hashed face names, as the browser reads them).
FAMILY = [
    ("sans", "header", "declared .font-sans -> var(--font-doppler-repro); 8 @font-face files (400/700, normal/italic) — a variable weight paints 450",
     "Doppler Repro: headings, nav, buttons, body."),
    ("mono", "code-chip", "declared .font-mono -> var(--font-doppler-repro-mono); paints on span.text-code",
     "Doppler Repro Mono: inline code chips and CLI samples."),
    ("inter", "check-item", "declared .font-inter -> var(--font-inter); paints on the demo checklist copy",
     "Inter: long-form/supporting text where a more neutral sans is wanted."),
]
for k, comp_name, decl, desc in FAMILY:
    put(SPEC["core"].setdefault("font", {}).setdefault("family", {}), k,
        {"value": st(comp_name, "default")["fontFamily"], "type": "fontFamily",
         "source": f"computed fontFamily of {comp_name} default (raw/components-computed.json); {decl} (raw/css-vars.json theme + raw/utility-classes.json)",
         "description": desc})

# The declared type scale: every .text-* size step (media-context steps keep
# their breakpoint in the description). Desktop is >=1023px ('md:').
SIZE = [
    ("h1", ".md:text-h1", "@media (min-width: 1023px)", "Display h1: 96px at >=1023px (pricing/blog headlines paint it)."),
    ("h1Mobile", ".text-h1Mobile", None, "h1 below 1023px: 64px."),
    ("h2", ".md:text-h2", "@media (min-width: 1023px)", "h2: 64px at >=1023px."),
    ("h2Mobile", ".text-h2Mobile", None, "h2 below 1023px: 52px."),
    ("h3", ".text-h3", None, "h3: 48px (the hero headline at 1440px)."),
    ("h3Mobile", ".text-h3Mobile", None, "h3 below 1023px: 36px."),
    ("h4", ".text-h4", None, "h4: 32px."),
    ("h4Mobile", ".text-h4Mobile", None, "h4 below 1023px: 24px."),
    ("h5", ".md:text-h5", "@media (min-width: 1023px)", "h5: 24px at >=1023px."),
    ("articleCard", ".md:text-articleCard", "@media (min-width: 1023px)", "Article-card title: 40px at >=1023px (24px below)."),
    ("p1", ".text-p1", None, "p1 lead: 24px."),
    ("p2", ".text-p2", None, "p2 body: 18px."),
    ("p3", ".text-p3", None, "p3 small body: 14px."),
    ("small", ".text-small", None, "small: 12px."),
    ("label", ".text-label", None, "label: 14px."),
    ("labelSm", ".text-labelSm", None, "labelSm: 10px micro-label (chips, badges)."),
    ("navLink", ".text-navLink", None, "navLink: 15px bold link text."),
    ("code", ".text-code", None, "code/blog: 16px."),
    ("8xl", ".text-8xl", None, "Tailwind 8xl: 100px (the giant footer wordmark scale)."),
]
for k, sel, ctx, desc in SIZE:
    try:
        v = cls(sel)["font-size"]
    except KeyError:
        raise SystemExit(f"missing size declaration {sel}")
    if ctx and ctx not in desc:
        desc += f" (declared inside {ctx})"
    put(SPEC["core"]["font"].setdefault("size", {}), k,
        {"value": v, "type": "dimension", "source": f"declared {sel} font-size (raw/utility-classes.json)", "description": desc})

LH = [
    ("90", ".text-h1Mobile", "line-height", "h1Mobile's 90% line-height."),
    ("100", ".text-h2Mobile", "line-height", "100% line-height."),
    ("105", ".md:text-h1", "line-height", "Display h1's 105%."),
    ("115", ".md:text-h2", "line-height", "h2's 115%."),
    ("120", ".text-h3", "line-height", "120% line-height."),
    ("140", ".md:text-p1", "line-height", "Body text 140%."),
    ("150", ".text-blog", "line-height", "Blog prose 150%."),
    ("160", ".text-code", "line-height", "Code text 160%."),
    ("170", ".leading-170", "line-height", "Checklist copy 170%."),
]
for k, sel, prop, desc in LH:
    try:
        v = cls(sel)["line-height"]
    except KeyError:
        continue
    put(SPEC["core"]["font"].setdefault("lineHeight", {}), k,
        {"value": v, "type": "number", "source": f"declared {sel} line-height (raw/utility-classes.json)", "description": desc})
# line-height values arrive as percentages; store them as unitless ratios.
for k, leaf in SPEC["core"]["font"]["lineHeight"].items():
    v = leaf["value"]
    if isinstance(v, str) and v.endswith("%"):
        leaf["value"] = round(float(v[:-1]) / 100, 4)

TRACK = [
    ("h1", ".md:text-h1", "-1.92px on the 96px display step."),
    ("h2", ".md:text-h2", "-1.28px on the 64px step."),
    ("h3", ".text-h3", "-0.96px on the 48px step."),
    ("h4", ".text-h4", "-0.64px on the 32px step."),
    ("h5", ".md:text-h5", "-0.48px on the 24px step."),
    ("p1", ".text-p1", "-0.24px on the 24px lead."),
    ("p2", ".text-p2", "-0.18px on the 18px body."),
    ("p3", ".text-p3", "+0.42px on the 14px small body."),
    ("small", ".text-small", "+0.36px on 12px."),
    ("label", ".text-label", "0px on labels."),
    ("labelSm", ".text-labelSm", "+1px on 10px micro-labels."),
    ("navLink", ".text-navLink", "+0.15px on 15px nav links."),
    ("blog", ".text-blog", "-0.16px on blog prose."),
    ("zero", ".tracking-0", "0px."),
]
for k, sel, desc in TRACK:
    try:
        v = cls(sel)["letter-spacing"]
    except KeyError:
        continue
    put(SPEC["core"]["font"].setdefault("tracking", {}), k,
        {"value": v, "type": "dimension", "source": f"declared {sel} letter-spacing (raw/utility-classes.json)", "description": desc})

# Each named weight is the computed fontWeight of a component that paints it.
WEIGHT = [
    ("regular", "hero-sub", ".font-normal / the painted body weight; Doppler Repro also paints 450."),
    ("mid", "hero-title", "The display weight: every h*/p* step declares font-weight:450 (a variable instance of Doppler Repro)."),
    ("medium", "search-field", ".font-medium / the .text-label weight."),
    ("bold", "nav-link", ".font-bold / .text-labelSm and .text-navLink weight."),
]
for k, comp_name, desc in WEIGHT:
    put(SPEC["core"]["font"].setdefault("weight", {}), k,
        {"value": int(st(comp_name, "default")["fontWeight"]), "type": "fontWeight",
         "source": f"computed fontWeight of {comp_name} default (raw/components-computed.json)", "description": desc})

# --------------------------------------------------------------- radii etc.
for k, sel, desc in [
    ("6", ".rounded-6", "6px: code chips, spend field."),
    ("8", ".rounded-8", "8px: small controls."),
    ("12", ".rounded-12", "12px: buttons (the green CTA, Sign In, plan CTAs)."),
    ("15", ".rounded-15", "15px."),
    ("16", ".rounded-16", "16px: form fields; the header's bottom corners."),
    ("20", ".rounded-20", "20px: .interactive-card tiles, footer links, dropdown bottom corners, footer top corners."),
    ("56", ".rounded-56", "56px: large pill sections."),
    ("full", ".rounded-full", "9999px: pagination buttons, avatars."),
]:
    put(SPEC["core"].setdefault("radius", {}), k,
        {"value": cls(sel)["border-top-left-radius"], "type": "dimension",
         "source": f"declared {sel} (raw/utility-classes.json)", "description": desc})


def shadow_layers(s):
    layers = []
    for l in re.split(r",(?![^(]*\))", s):
        m = re.match(r"\s*([\d.]+)(?:px)?\s+([\d.]+)(?:px)?\s+([\d.]+)(?:px)?(?:\s+([\d.]+)(?:px)?)?\s+(rgba?\([^)]*\))", l)
        if m:
            layers.append({"offsetX": m.group(1) + "px", "offsetY": m.group(2) + "px",
                           "blur": m.group(3) + "px", "spread": (m.group(4) or "0") + "px",
                           "color": m.group(5)})
    return layers


for k, sel, desc in [
    ("mediumDark", ".shadow-medium-dark", "0 8px 30px rgba(0,0,0,.45): the medium drop on dark surfaces."),
    ("people", ".shadow-people", "The five-layer ambient shadow used on imagery."),
]:
    raw = cls(sel).get("--tw-shadow", "")
    layers = shadow_layers(raw)
    if not layers:
        raise SystemExit(f"no shadow layers in {sel}")
    put(SPEC["core"].setdefault("shadow", {}), k,
        {"value": layers, "type": "shadow", "source": f"declared {sel} --tw-shadow (raw/utility-classes.json)", "description": desc})

for k, spec in [
    ("global", {"var": "--global-ease", "description": "The site's signature ease, cubic-bezier(0.9,0.1,0.1,0.9), declared on :root and used by --global-transition."}),
    ("globalUtility", {"value": cls(".ease-global")["transition-timing-function"], "source": "declared .ease-global (raw/utility-classes.json)", "description": "The .ease-global utility curve, cubic-bezier(0.8,0.01,0.11,0.98) — a second, slightly different 'global' ease used by utility classes."}),
    ("inOut", {"value": cls(".ease-in-out")["transition-timing-function"], "source": "declared .ease-in-out (raw/utility-classes.json)", "description": "Tailwind in-out, cubic-bezier(0.4,0,0.2,1)."}),
    ("out", {"value": cls(".ease-out")["transition-timing-function"], "source": "declared .ease-out (raw/utility-classes.json)", "description": "Tailwind out, cubic-bezier(0,0,0.2,1)."}),
]:
    leaf = dict(spec)
    leaf["type"] = "cubicBezier"
    if "value" in leaf:
        leaf["source"] = leaf.get("source", "")
    else:
        leaf["source"] = leaf.pop("source", "")
    put(SPEC["core"].setdefault("easing", {}), k, leaf)

for k, sel, desc in [
    ("global", ":root", "The declared --global-transition duration, 350ms."),
    ("150", ".duration-150", "150ms quick transitions."),
    ("200", ".duration-200", "200ms."),
    ("300", ".duration-300", "300ms — the FAQ chevron rotation and link hovers."),
    ("350", ".duration-[350ms]", "350ms explicit steps."),
    ("400", ".duration-[400ms]", "400ms."),
    ("500", ".duration-500", "500ms — the interactive-card hover sheen."),
]:
    if sel == ":root":
        raw_v = V["resolved"]["dark"]["--global-transition"]["raw"]
        v = re.match(r"([\d.]+m?s)", raw_v).group(1)
        src = "declared --global-transition on :root resolves to 350ms var(--global-ease) (raw/css-vars.json resolved.dark)"
    else:
        v = cls(sel)["transition-duration"]
        src = f"declared {sel} (raw/utility-classes.json)"
    put(SPEC["core"].setdefault("duration", {}), k,
        {"value": v, "type": "duration", "source": src, "description": desc})

# ---------------------------------------------------- measured component bits
def stprop(comp, state, prop):
    """A bare property reads the computed style block; a dotted path walks the
    state dict (textStyle.color, paint.0.bg, ancestors.N.bg). A component the
    capture could not find has no reading."""
    if C[comp].get("missing"):
        raise KeyError(comp)
    d = C[comp]["states"][state]
    if "." not in prop:
        return d.get("style", {}).get(prop, "")
    node = d
    for part in prop.split("."):
        if isinstance(node, list) and part.isdigit():
            node = node[int(part)] if int(part) < len(node) else None
        elif isinstance(node, dict):
            node = node.get(part)
        else:
            return ""
        if node is None:
            return ""
    return node if isinstance(node, (str, int, float)) else ""


def norm_color(v):
    v = (v or "").strip()
    # rgb(r g b/var(--tw-x-opacity,A)) -> rgb(r g b / A): keep the fallback alpha, never assume 1
    v = re.sub(r"\s*/\s*var\(--tw-[a-z-]*-opacity,\s*([\d.]+%?)\)", r" / \1", v)
    m = re.fullmatch(r"rgb\((\d+)\s+(\d+)\s+(\d+)\s*/\s*([\d.]+%?)\)", v)
    if m:
        a = float(m.group(4)[:-1]) / 100 if m.group(4).endswith("%") else float(m.group(4))
        r, g, b = (int(m.group(i)) for i in (1, 2, 3))
        return "#%02x%02x%02x" % (r, g, b) if a >= 1 else f"rgba({r}, {g}, {b}, {'%g' % a})"
    m = re.fullmatch(r"rgb\((\d+)\s+(\d+)\s+(\d+)\)", v)  # space-separated rgb()
    if m:
        return "#%02x%02x%02x" % (int(m.group(1)), int(m.group(2)), int(m.group(3)))
    m = re.fullmatch(r"#([0-9a-fA-F]{3,8})", v)
    if m:
        h = m.group(1).lower()
        if len(h) in (3, 4):
            h = "".join(c * 2 for c in h)
        return "#" + h
    m = re.fullmatch(r"rgba?\(([\d.]+),?\s*([\d.]+),?\s*([\d.]+)(?:,?\s*/?\s*([\d.]+%?))?\)", v)
    if m:
        r, g, b, a = m.groups()
        if a is not None:
            a = float(a[:-1]) / 100 if str(a).endswith("%") else float(a)
        if a is None or a >= 1:
            return "#%02x%02x%02x" % (int(float(r)), int(float(g)), int(float(b)))
        return f"rgba({int(float(r))}, {int(float(g))}, {int(float(b))}, {'%g' % a})"
    return v


BY_VALUE = {}
def collect(node, prefix=""):
    for k, v in node.items():
        if isinstance(v, dict) and "value" in v and v.get("type") == "color":
            BY_VALUE.setdefault(norm_color(v["value"]), prefix + k)
        elif isinstance(v, dict):
            collect(v, prefix + k + ".")
collect(SPEC["core"]["color"], "color.")


def role(path, comp, state, prop, desc):
    raw = stprop(comp, state, prop)
    if "|" in str(raw) or "solid" in str(raw):  # a paint border string "T:1px solid rgb(..) | R:.."
        m = re.search(r"rgba?\([^)]*\)|#[0-9a-fA-F]{3,8}", str(raw))
        raw = m.group(0) if m else ""
    v = norm_color(raw)
    if not v or v in ("transparent", "rgba(0, 0, 0, 0)"):
        return
    target = BY_VALUE.get(v)
    leaf = {"type": "color", "description": desc}
    if target:
        leaf["value"] = "{%s}" % target
        leaf["source"] = f"computed {prop} of {comp} {state} (raw/components-computed.json); same value as core.{target}"
    else:
        leaf["value"] = v
        leaf["source"] = f"computed {prop} of {comp} {state} (raw/components-computed.json)"
    put(SPEC["dark"], path, leaf)


for path, comp, state, prop, desc in [
    ("page", "footer", "default", "backgroundColor", "warm-black #1c1624: every route's ground (the footer's own fill; html/body compute to the same value)."),
    ("surface", "feature-card", "default", "backgroundColor", "The .interactive-card ground: a 4% warm-white veil (black4)."),
    ("surfaceRaised", "cat-chip", "default", "paint.0.bg", "The raised chip fill #2d2734 (inactive category/filter chips)."),
    ("badge", "plan-badge", "default", "paint.0.bg", "The plan badge fill #302c37."),
    ("text", "menu-link", "default", "color", "warm-white #f1f0ec primary text."),
    ("muted", "nav-link", "default", "color", "silver #d0c9c4 muted text (nav links, lede copy, Read-More)."),
    ("accent", "nav-cta", "default", "backgroundColor", "flourescent-green #00f575: the primary CTA fill."),
    ("accentText", "nav-cta", "default", "textStyle.color", "warm-black #1c1624 text on the green CTA."),
    ("accentHover", "nav-cta", "hover", "paint.0.bg", "flourescent-green-dark #00bf5b: the CTA fill on hover/press."),
    ("link", "footer-link", "default", "color", "warm-white link text."),
    ("linkMuted", "read-more", "default", "color", "silver secondary links."),
    ("linkHover", "read-more", "hover", "color", "Links brighten to warm-white on hover."),
    ("border", "footer-link", "default", "borderTopColor", "glow-stroke rgba(255,255,255,0.08): the translucent hairline."),
    ("borderStrong", "header", "default", "paint.0.border", "glow-stroke-light #55505b: the opaque 1px line on the header bar and mega-menu."),
    ("field", "demo-field", "default", "borderTopColor", "aluminum #8b877d: form-field borders."),
    ("fieldFocus", "demo-field", "focused", "borderTopColor", "light-purple #b997ff: the field border on focus (the site swaps the border colour instead of drawing a ring)."),
    ("chip", "filter-chip", "default", "paint.0.bg", "Inactive chip fill #2d2734."),
    ("chipHover", "cat-chip", "hover", "paint.0.bg", "light-purple #b997ff: chips light up on hover."),
    ("chipActive", "cat-chip-active", "default", "paint.0.bg", "light-purple #b997ff: the selected filter chip."),
    ("chipActiveText", "cat-chip-active", "default", "textStyle.color", "warm-black #1c1624 text on the active chip."),
    ("code", "code-chip", "default", "color", "brand-orange #f55c15 inline-code text."),
    ("codeSurface", "code-chip", "default", "backgroundColor", "The inline code chip's black4 ground."),
    ("focus", "nav-cta", "focus-visible", "outlineColor", "The keyboard-focus ring is the browser's default auto outline (rgb(0,95,204) on links); doppler.com restyles fields with a light-purple border instead."),
    ("purple", "h2-section", "default", "color", "light-purple #b997ff section headings."),
    ("orange", "code-chip", "default", "color", "brand-orange #f55c15 accents."),
]:
    try:
        role(path, comp, state, prop, desc)
    except KeyError:
        pass

# ------------------------------------------------------ measured extras
meas = SPEC["core"].setdefault("measured", {})
for comp, state, key, prop, desc in [
    ("nav-signin", "hover", "hover-fill", "paint.0.bg", "black8 rgba(242,241,237,0.08): the fill bordered buttons pick up on hover."),
    ("page-number", "hover", "page-hover", "color", "flourescent-green-dark #00bf5b pagination hover text."),
    ("industry-chip", "default", "chip-text-active", "textStyle.color", "The active industry chip's green text."),
    ("nav-link", "hover", "link-hover-text", "color", "Nav links go warm-white on hover."),
]:
    try:
        v = norm_color(stprop(comp, state, prop))
        if v and v != "transparent":
            meas[key] = {"value": v, "type": "color",
                         "source": f"computed {prop} of {comp} {state} (raw/components-computed.json)",
                         "description": desc}
    except KeyError:
        pass

# ------------------------------------------------------------- gradients
def gradient_leaves():
    out = {}
    m = re.search(r"linear-gradient\((-?[\d.]+)deg,\s*(.*)\)", stprop("hero-title", "default", "paint.0.bgImage") or "")
    if m:
        stops = []
        for cm in re.finditer(r"(rgba?\([^)]*\)|#[0-9a-fA-F]{3,8})\s+(-?[\d.]+)%", m.group(2)):
            stops.append({"color": norm_color(cm.group(1)), "position": round(float(cm.group(2)) / 100, 4)})
        if len(stops) >= 2:
            out["headline"] = {"value": stops, "type": "gradient", "angle": "%gdeg" % float(m.group(1)),
                               "source": "computed paint.0.bgImage of hero-title default (raw/components-computed.json): the lilac-to-carmine gradient text span",
                               "description": "The display-headline gradient, ~91deg from #855aff to #ff5632."}
    m = re.search(r"linear-gradient\((-?[\d.]+)deg,\s*(.*)\)", stprop("feature-card", "default", "paint.1.bgImage") or "")
    if m:
        stops = []
        for cm in re.finditer(r"(rgba?\([^)]*\)|#[0-9a-fA-F]{3,8})\s+(-?[\d.]+)%", m.group(2)):
            stops.append({"color": norm_color(cm.group(1)), "position": round(float(cm.group(2)) / 100, 4)})
        if len(stops) >= 2:
            out["cardSheen"] = {"value": stops, "type": "gradient", "angle": "%gdeg" % float(m.group(1)),
                                "source": "computed paint.1.bgImage of feature-card default (raw/components-computed.json): the interactive-card ::before sheen",
                                "description": "The diagonal sheen painted across .interactive-card tiles (white 16% fading out)."}
    # declared brand gradient stops: from-purple / via-lilac / to-light-purple.
    # cls() returns each declaration's VALUE ("#6b13f5 var(--tw-gradient-from-position)"),
    # so the hex is matched inside the value, not after a property name.
    try:
        frm = re.search(r"#[0-9a-fA-F]{3,8}", color_of(".from-purple", "--tw-gradient-from")).group(0)
        via = re.search(r",\s*(#[0-9a-fA-F]{3,8})\s+var", color_of(".via-lilac", "--tw-gradient-stops")).group(1)
        to = re.search(r"#[0-9a-fA-F]{3,8}", color_of(".to-light-purple", "--tw-gradient-to")).group(0)
        out["brand"] = {"value": [{"color": norm_color(frm), "position": 0},
                                  {"color": norm_color(via), "position": 0.5},
                                  {"color": norm_color(to), "position": 1}],
                        "type": "gradient", "angle": "120deg",
                        "source": "declared .from-purple + .via-lilac + .to-light-purple stops (raw/utility-classes.json); "
                                  "direction from the computed 120deg brand gradient on demo-card/post-card (raw/components-computed.json)",
                        "description": "The brand gradient stops used on glows and text: purple -> lilac -> light-purple."}
    except (KeyError, AttributeError):
        pass
    return out


SPEC["core"]["gradient"] = gradient_leaves()

# ------------------------------------------------------------- component dims
comp = SPEC["component"]
for key, cname, state, prop, desc in [
    ("control.heightNavCta", "nav-cta", "default", "height", "The header's 36px green pill."),
    ("control.heightButton", "hero-cta", "default", "height", "45px hero/plan buttons."),
    ("control.heightSubmit", "demo-submit", "default", "height", "The demo submit's 43px."),
    ("control.heightField", "demo-field", "default", "height", "43px form fields."),
    ("control.heightChip", "cat-chip", "default", "height", "22px category/filter chips."),
    ("control.heightBadge", "plan-badge", "default", "height", "22px plan badge."),
    ("control.heightPagination", "page-number", "default", "height", "30px round pagination buttons."),
    ("control.gap", "agents-cta", "default", "gap", "8px icon gap inside buttons."),
    ("header.height", "header", "default", "height", "72px sticky header bar."),
    ("header.widthInset", "header", "default", "rect.x", "The header is inset 14px from the viewport edge (1412px at 1440)."),
    ("menu.heightMobile", "m-menu-open", "default", "height", "The mobile menu sheet below the 55px offset."),
    ("slider.height", "seat-slider", "default", "height", "The 10px pricing seat slider track."),
    ("logo.height", "logo", "default", "height", "The wordmark height in the header."),
]:
    try:
        v = stprop(cname, state, prop)
        if not v:
            continue
        m = re.match(r"(-?[\d.]+)", str(v))
        put(comp, key, {"type": "dimension", "value": "%gpx" % float(m.group(1)),
                        "source": f"computed {prop} of {cname} {state} (raw/components-computed.json)" + missed(cname)
                        + ("; an outlined 'Start for Free' link, not the green hero CTA the name says: read from the wrong element, recapture needed" if cname == "hero-cta" else ""),
                        "description": desc})
    except (KeyError, AttributeError):
        pass


def radius_of(comp_name, state, paint_idx=0):
    p = C[comp_name]["states"][state].get("paint", [])
    if paint_idx < len(p):
        return p[paint_idx].get("radius", "")
    return C[comp_name]["states"][state]["style"].get("borderTopLeftRadius", "")


for key, cname, desc in [
    ("radius.button", "nav-cta", "12px button corners."),
    ("radius.field", "demo-field", "16px field corners."),
    ("radius.card", "feature-card", "20px card corners (.interactive-card)."),
    ("radius.codeChip", "code-chip", "6px code-chip corners."),
    ("radius.pagination", "page-number", "9999px pagination circles."),
]:
    try:
        v = radius_of(cname, "default") or stprop(cname, "default", "borderTopLeftRadius")
        if not v:
            continue
        m = re.match(r"([\d.]+)px", str(v))
        put(comp, key, {"type": "dimension", "value": "%gpx" % float(m.group(1)),
                        "source": f"computed radius of {cname} default (raw/components-computed.json)",
                        "description": desc})
    except (KeyError, AttributeError):
        pass

# Header and dropdown bottom radii arrive as "0px 0px 16px 16px" strings.
for key, cname, idx, desc in [
    ("header.radiusBottom", "header", 0, "16px bottom corners on the floating header bar."),
    ("dropdown.radiusBottom", "nav-dropdown", 0, "20px bottom corners on the mega-menu panel."),
    ("footer.radiusTop", "footer", 0, "20px top corners on the footer sheet."),
]:
    try:
        r = radius_of(cname, "default")
        m = re.findall(r"([\d.]+)px", str(r))
        if m:
            put(comp, key, {"type": "dimension", "value": "%gpx" % float(m[-1]),
                            "source": f"computed painted radius of {cname} default (raw/components-computed.json)",
                            "description": desc})
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
