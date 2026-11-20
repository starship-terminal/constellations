#!/usr/bin/env python3
"""Write raw/component-tokens.json, the token spec build_tokens.py reads.

dropbox.com's public signed-out surface is server-rendered "warp" marketing
pages on the dwg-component library, and it declares two real token layers in
its served stylesheets (harvested into raw/css-vars.json by
tools/capture/vars.mjs):

  dig       the generated DIG foundations file (dig-components/tokens.css,
            @dropbox/dig-components 25.1.0, foundations 7.1.0): the
            --dig-spacing__dimension__* scale, --dig-type__* ramp and font
            stacks, --dig-radius__*, --dig-motion__*, --dig-breakpoint__*,
            --dig-utilities__*, and the --dig-color__* role palette scoped
            under .dig-Theme--bright/.dig-Theme--dark and
            .dig-Theme-vis2023--bright/.dig-Theme-vis2023--dark. The whole
            public surface paints dig-Theme-vis2023--bright on
            dig-Mode--bright; the dark scope is declared but never paints
            signed out, so the "dark" set is the declared dark palette,
            documented as unpainted.
  dwg       the component layer: --DWG__TEMP__color__* brand palette on
            :root (coconut/graphite ramps, named accent hues, button and
            status roles), rebound per painted section as
            --dwg-theme__color__* roles under .dwg-theme--coconut (the nav
            and cream sections), .dwg-theme--graphite (the dark in-page
            bands) and .dwg-theme--navy.

Every declared leaf is {"var": <name>, "resolve": <probe pass>} so
build_tokens.py resolves it on the right scope; measured computed values
from raw/components-computed.json carry {"value", "source"}: the real
control heights, painted radii, focus rings and state colours the
components show.
"""
import json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
V = json.loads((RAW / "css-vars.json").read_text())
RES = V.get("resolved", {})
RL = RES.get("light", {})
C = json.loads((RAW / "components-computed.json").read_text())["components"]


def resolved(pass_, name):
    e = RES.get(pass_, {}).get(name)
    return e.get("value", e.get("raw")) if e else None


def var(name, ty="color", resolve="light", **kw):
    d = {"var": name, "type": ty}
    if resolve != "light":
        d["resolve"] = resolve
    d.update(kw)
    return d


SPEC = {"_about": (
    "The token tree build_tokens.py turns into tokens.json. dropbox.com's "
    "public surface declares two token layers: the generated DIG layer "
    "(--dig-*, resolved on the painted dig-Theme-vis2023--bright scope for "
    "'light' and the declared-but-unpainted vis2023--dark scope for 'dark') "
    "and the dwg-component layer (--DWG__TEMP__color__* brand palette in "
    "'core', rebound per painted section as --dwg-theme__color__* roles in "
    "'light.dwg.coconut|graphite|navy'). Scales (spacing, type, radius, "
    "motion, breakpoints, font stacks) are declared var leaves in 'core'; "
    "measured computed styles add the real control heights, focus rings, "
    "painted radii and transition values."),
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


def emit(root, name, leaf):
    # A suffix such as "border--faint" must not split into an empty-named
    # group (the exported path would carry a double dot); drop empty parts.
    node, last = descend(root, [p for p in name[2:].split("-") if p])
    node[last] = leaf


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


ALL = sorted({n for p in RES.values() for n in p})
LIT = {n: e.get("value", e.get("raw")) for n, e in RL.items()}


def dig_color_tokens(pass_):
    """Emit every --dig-color__* var under color.<role>.<name> on one set."""
    out = {}
    root = SPEC["dark" if pass_ == "dark" else "light"]
    for n in ALL:
        if not n.startswith("--dig-color__") or resolved(pass_, n) is None:
            continue
        suffix = n[len("--dig-color__"):]
        key = "--color-" + suffix.replace("__", "-").replace("--", "-")
        emit(root, key, var(n, "color", resolve=pass_,
                            source=f"css-var {n} resolved {pass_} (raw/css-vars.json)",
                            description=f"The declared DIG role {n[2:]}."))
        out[suffix] = n
    return out


LROLES = dig_color_tokens("light")
DROLES = dig_color_tokens("dark")

# The scheme flags + foundation version: provenance tokens, type "other".
for pass_, root in (("light", SPEC["light"]), ("dark", SPEC["dark"])):
    for n in ("--dig-color-scheme", "--scheme__color"):
        if resolved(pass_, n) is not None:
            key = "--scheme-" + n.lstrip("-").replace("__", "-")
            emit(root, key, var(n, "other", resolve=pass_,
                                source=f"css-var {n} resolved {pass_} (raw/css-vars.json)",
                                description="The theme flag this scope declares."))

# ------------------------------------------------------------------- fonts

fam = SPEC["core"].setdefault("font", {}).setdefault("family", {})
for key, n, desc in [
    ("body", "--dig-type__bodyfontstack", "Atlas Grotesk — body, actions, controls and most UI text."),
    ("title", "--dig-type__titlefontstack", "Sharp Grotesk — headings and display type."),
    ("mono", "--dig-type__monospacefontstack", "The monospace stack."),
]:
    if n in LIT:
        fam[key] = var(n, "fontFamily",
                       source=f"css-var {n} resolved light (raw/css-vars.json)",
                       description=desc)
for n in ALL:
    m = re.fullmatch(r"--dig-type__family__([\w-]+)", n)
    if m and n in LIT and m.group(1) not in fam:
        fam["role-" + m.group(1)] = var(n, "fontFamily",
                                        source=f"css-var {n} resolved light (raw/css-vars.json)",
                                        description=f"A named family role ({n[2:]}).")

sizes = SPEC["core"].setdefault("font", {}).setdefault("size", {})
for n in ALL:
    m = re.fullmatch(r"--dig-type__size__([\w-]+)__([\w-]+)", n)
    if m and n in LIT:
        sizes[f"{m.group(1)}-{m.group(2)}"] = var(n, "dimension",
                                                 source=f"css-var {n} resolved light (raw/css-vars.json)",
                                                 description=f"The declared {m.group(1)} {m.group(2)} size.")
# measured sizes that fall outside the declared ramp
for key, comp, state, desc in [
    ("display-hero", "hero-title", "default", "The hero display size on the home page."),
    ("display-mobile", "m-hero", "default", "The display size at 390 wide."),
    ("section-h2", "section-h2", "default", "A section heading size."),
    ("price", "plan-price", "default", "The plan price figure size."),
    ("menu-item", "m-nav-item", "default", "A mobile-menu row size."),
]:
    v = ts(comp, state, "fontSize")
    if not v:
        continue
    # The ramp's leaves are var leaves: compare against what each resolves to (a
    # comparison against "value" never matched, so every reading read as outside).
    step = next((k for k, x in sizes.items() if not k.startswith("measured-")
                 and str(resolved(x.get("resolve", "light"), x["var"]) if "var" in x else x.get("value")) == v), None)
    src = f"computed fontSize of {comp} {state} (raw/components-computed.json)"
    if step:
        sizes["measured-" + key] = {"type": "dimension", "value": "{font.size." + step + "}", "source": src,
                                    "description": desc + f" Measured; it equals the declared {step} step."}
    else:
        sizes["measured-" + key] = {"type": "dimension", "value": v, "source": src,
                                    "description": desc + " Measured — outside the declared ramp."}

leading = SPEC["core"].setdefault("font", {}).setdefault("lineHeight", {})
for n in ALL:
    m = re.fullmatch(r"--dig-type__lineheight__([\w-]+)__([\w-]+)", n)
    if m and n in LIT:
        leading[f"{m.group(1)}-{m.group(2)}"] = var(n, "dimension",
                                                   source=f"css-var {n} resolved light (raw/css-vars.json)",
                                                   description=f"The declared {m.group(1)} {m.group(2)} line height.")

weights = SPEC["core"].setdefault("font", {}).setdefault("weight", {})
for n in ALL:
    m = re.fullmatch(r"--dig-type__weight__([\w-]+)", n)
    if m and n in LIT:
        weights[m.group(1)] = var(n, "fontWeight",
                                  source=f"css-var {n} resolved light (raw/css-vars.json)",
                                  description=f"The declared {m.group(1)} weight.")

spacing_l = SPEC["core"].setdefault("font", {}).setdefault("letterSpacing", {})
for n in ALL:
    m = re.fullmatch(r"--dig-type__letterspacing__([\w-]+)", n)
    if m and n in LIT:
        spacing_l[m.group(1)] = var(n, "other",
                                    source=f"css-var {n} resolved light (raw/css-vars.json)",
                                    description=f"The declared {m.group(1)} letter spacing.")

# Named type roles: composites over the scale, so DESIGN.md's typography
# section lists them.
typo = SPEC["core"].setdefault("typography", {})
for key, famref, size, lh, wt, desc in [
    ("title-xlarge", "font.family.title", "font.size.title-xlarge", "font.lineHeight.title-xlarge", "font.weight.base", "Sharp Grotesk 40/48 — the biggest declared title step."),
    ("title-large", "font.family.title", "font.size.title-large", "font.lineHeight.title-large", "font.weight.base", "Sharp Grotesk 28/36."),
    ("title-medium", "font.family.title", "font.size.title-medium", "font.lineHeight.title-medium", "font.weight.base", "Sharp Grotesk 22/28."),
    ("title-small", "font.family.title", "font.size.title-small", "font.lineHeight.title-small", "font.weight.base", "Sharp Grotesk 16/26."),
    ("text-xlarge", "font.family.body", "font.size.text-xlarge", "font.lineHeight.text-xlarge", "font.weight.base", "Atlas Grotesk 20/30 — the largest body step."),
    ("text-large", "font.family.body", "font.size.text-large", "font.lineHeight.text-large", "font.weight.base", "Atlas Grotesk 16/24."),
    ("text-medium", "font.family.body", "font.size.text-medium", "font.lineHeight.text-medium", "font.weight.base", "Atlas Grotesk 14/22 — the standard body."),
    ("text-small", "font.family.body", "font.size.text-small", "font.lineHeight.text-small", "font.weight.base", "Atlas Grotesk 12/20."),
    ("text-xsmall", "font.family.body", "font.size.text-xsmall", "font.lineHeight.text-xsmall", "font.weight.base", "Atlas Grotesk 10/18."),
    ("action-large", "font.family.body", "font.size.action-large", "font.lineHeight.text-large", "font.weight.strong", "Atlas Grotesk 16/24 500 — button labels."),
    ("action-medium", "font.family.body", "font.size.action-medium", "font.lineHeight.label-large", "font.weight.strong", "Atlas Grotesk 14/20 500."),
    ("action-small", "font.family.body", "font.size.action-small", "font.lineHeight.label-medium", "font.weight.strong", "Atlas Grotesk 12/18 500."),
]:
    def ok(ref):
        node = SPEC["core"]
        for p in ref.split("."):
            node = node.get(p) if isinstance(node, dict) else None
            if node is None:
                return False
        return True
    if all(ok(r) for r in (famref, size, lh, wt)):
        typo[key] = {"value": {"fontFamily": "{%s}" % famref, "fontSize": "{%s}" % size,
                               "fontWeight": "{%s}" % wt, "lineHeight": "{%s}" % lh},
                     "type": "typography",
                     "source": "declared roles composed over the --dig-type__* ramp (raw/css-vars.json)",
                     "description": desc}

# --------------------------------------------------------- the brand palette
# --DWG__TEMP__color__* on :root: the named hues the dwg-theme sections paint.
brand = SPEC["core"].setdefault("color", {}).setdefault("brand", {})
BUCKETS = {
    "brand": "color-brand", "accent": "color-brand-accent", "button": "color-brand-button",
    "alert": "color-brand-status-alert", "attention": "color-brand-status-attention",
    "disabled": "color-brand-status-disabled", "faint": "color-brand-status-faint",
    "success": "color-brand-status-success", "warning": "color-brand-status-warning",
    "inverse": "color-brand-status-inverse", "core": "color-brand-core",
    "identity": "color-brand-identity", "opacity": "color-brand-opacity",
}
for n in ALL:
    m = re.fullmatch(r"--DWG__TEMP__color__([\w-]+?)__(.+)", n)
    if not m or n not in LIT:
        continue
    bucket, rest = m.group(1), m.group(2).replace("__", "-").replace("_", "-")
    emit(SPEC["core"], "--" + BUCKETS.get(bucket, "color-brand-" + bucket) + "-" + rest,
         var(n, "color",
             source=f"css-var {n} resolved light (raw/css-vars.json); a TEMP name the dwg layer still carries",
             description=f"The declared {bucket} palette value {rest}."))

# ------------------------------------------------- dwg-theme section roles
# --dwg-theme__color__* rebound per .dwg-theme--* class: the painted section
# palettes. coconut is the nav and the cream sections, graphite the dark
# in-page bands, navy the navy band.
dwg = SPEC["light"].setdefault("dwg", {})
for scope in ("coconut", "graphite", "navy"):
    bag = dwg.setdefault(scope, {})
    for n in ALL:
        if not n.startswith("--dwg-theme__color__") or resolved(scope, n) is None:
            continue
        suffix = n[len("--dwg-theme__color__"):].replace("__", "-").replace("--", "-")
        emit(bag, "--" + suffix, var(n, "color", resolve=scope,
                                     source=f"css-var {n} resolved {scope} (raw/css-vars.json)",
                                     description=f"The dwg-theme role {n[len('--dwg-theme__color__'):]} as the {scope} section paints it."))

# ------------------------------------------------------------ light roles
# Top-level gallery roles aliased to the declared palette, so the preview
# swatches and DESIGN.md's colour table read plainly. The alias target is
# found by walking the emitted tree: descend() wraps a leaf that shares a
# node with children under ".default", so the path is not guessable.
def find_path(node, want, pre="color"):
    for k, v in node.items():
        p = pre + "." + k
        if isinstance(v, dict):
            if v.get("var") == want:
                return p
            r = find_path(v, want, p)
            if r:
                return r
    return None


for root, pass_ in ((SPEC["light"], "light"), (SPEC["dark"], "dark")):
    for name, suffix, desc in [
        ("--page", "background__base", "The page field."),
        ("--surface", "background__subtle", "The subtle surface (cream on light)."),
        ("--surface-raised", "background__raised", "Cards and raised surfaces."),
        ("--surface-sunken", "background__sunken", "Sunken wells."),
        ("--overlay", "background__overlay", "Translucent overlay surface."),
        ("--text", "text__base", "Primary text."),
        ("--muted", "text__subtle", "Secondary text."),
        ("--accent", "primary__base", "The Dropbox blue #0061fe."),
        ("--accent-hover", "primary__base--state-1", "The accent hover step."),
        ("--accent-pressed", "primary__base--state-2", "The accent pressed step."),
        ("--cta", "primary-cta__base", "The primary-CTA fill (black in vis2023 bright, near-white in dark)."),
        ("--cta-text", "primary-cta__on-base", "Text on the primary CTA."),
        ("--border", "border__base", "The default border."),
        ("--border-subtle", "border__subtle", "Hairline borders."),
        ("--border-bold", "border__bold", "Strong borders."),
        ("--focus", "utility__focus-ring", "The focus-ring colour."),
        ("--scrim", "utility__overlay", "The overlay scrim."),
        ("--error", "alert__base", "The alert/danger fill."),
        ("--error-text", "alert__on-surface", "Alert text on its surface."),
        ("--error-surface", "alert__surface", "The alert surface."),
        ("--warning-text", "warning__on-surface", "Warning text on its surface."),
        ("--warning-surface", "warning__surface", "The warning surface."),
        ("--success", "success__base", "The success fill."),
        ("--success-text", "success__on-surface", "Success text on its surface."),
        ("--success-surface", "success__surface", "The success surface."),
        ("--disabled-text", "disabled__on-surface", "Disabled text."),
        ("--disabled-surface", "disabled__surface", "The disabled fill."),
        ("--link", "primary__on-surface", "Link/action text on a surface."),
    ]:
        n = "--dig-color__" + suffix
        target = resolved(pass_, n) is not None and find_path(root.get("color", {}), n)
        if target:
            emit(root, name, {"value": "{" + target + "}", "type": "color",
                              "source": f"role alias over {n} resolved {pass_} (raw/css-vars.json)",
                              "description": desc})

# --------------------------------------------------- declared box shadows
# --dig-utilities__boxshadow__* resolve to real shadow stacks per theme.
def parse_shadow(s):
    """Every layer of a resolved shadow stack; a layer it cannot read stops the build
    instead of being dropped (findall used to skip it silently)."""
    if not s or s.strip() == "none":
        return []
    out, depth, cur, parts = [], 0, "", []
    for ch in s:
        depth += ch == "("
        depth -= ch == ")"
        if ch == "," and depth == 0:
            parts.append(cur.strip())
            cur = ""
        else:
            cur += ch
    parts.append(cur.strip())
    for part in parts:
        m = re.fullmatch(r"(inset\s+)?(rgba?\([\d.,\s]+\)|#[0-9a-fA-F]{3,8})\s+(-?\d+(?:\.\d+)?px)\s+(-?\d+(?:\.\d+)?px)"
                         r"\s+(-?\d+(?:\.\d+)?px)(?:\s+(-?\d+(?:\.\d+)?px))?(\s+inset)?", part)
        if not m:
            raise SystemExit(f"shadow layer not understood: {part!r}")
        i1, a, x, y, bl, sp, i2 = m.groups()
        out.append({"color": norm_color(a), "offsetX": x, "offsetY": y, "blur": bl,
                    "spread": sp or "0px", "inset": bool(i1 or i2)})
    return out


for root, pass_ in ((SPEC["light"], "light"), (SPEC["dark"], "dark")):
    bag = root.setdefault("shadow", {})
    for n in ALL:
        m = re.fullmatch(r"--dig-utilities__boxshadow__([\w-]+)", n)
        if not m:
            continue
        v = resolved(pass_, n)
        if v is None:
            continue
        layers = parse_shadow(v)
        key = m.group(1).replace("_", "-")
        if layers:
            bag[key] = {"value": layers, "type": "shadow",
                        "source": f"css-var {n} resolved {pass_} (raw/css-vars.json)",
                        "description": f"The declared {key} elevation."}
        else:
            bag[key] = var(n, "other", resolve=pass_,
                           source=f"css-var {n} resolved {pass_} (raw/css-vars.json)",
                           description=f"The declared {key} elevation (unparsed).")

# ------------------------------------------------------- scales and motion
spacing = SPEC["core"].setdefault("spacing", {})
for n in ALL:
    m = re.fullmatch(r"--dig-spacing__([\w-]+)__([\w-]+)", n)
    if m and n in LIT:
        spacing[f"{m.group(1)}-{m.group(2)}"] = var(n, "dimension",
                                                   source=f"css-var {n} resolved light (raw/css-vars.json)",
                                                   description=f"The declared {m.group(1)} {m.group(2)} step.")

radius = SPEC["core"].setdefault("radius", {})
for n in ALL:
    m = re.fullmatch(r"--dig-radius__([\w-]+)", n)
    if m and n in LIT:
        radius[m.group(1)] = var(n, "dimension",
                                 source=f"css-var {n} resolved light (raw/css-vars.json)",
                                 description=f"The declared {m.group(1)} radius (the vis2023 theme's values; the old dig-Theme paints all-zero radii).")

dur = SPEC["core"].setdefault("duration", {})
for n in ALL:
    m = re.fullmatch(r"--dig-motion__duration__([\w-]+)", n)
    if m and n in LIT:
        dur[m.group(1)] = var(n, "duration",
                              source=f"css-var {n} resolved light (raw/css-vars.json)",
                              description=f"The declared {m.group(1)} duration.")
ease = SPEC["core"].setdefault("easing", {})
for n in ALL:
    m = re.fullmatch(r"--dig-motion__easing__([\w-]+)", n)
    if m and n in LIT:
        ease[m.group(1).replace("_", "-")] = var(n, "cubicBezier",
                                                 source=f"css-var {n} resolved light (raw/css-vars.json)",
                                                 description=f"The declared {m.group(1)} easing.")

layout = SPEC["core"].setdefault("layout", {})
for n in ALL:
    m = re.fullmatch(r"--dig-breakpoint__([\w-]+)", n)
    if m and n in LIT:
        v = LIT[n]
        layout["breakpoint-" + m.group(1)] = var(n, "dimension" if isinstance(v, str) and v.endswith("px") else "number",
                                                 source=f"css-var {n} resolved light (raw/css-vars.json)",
                                                 description=f"The declared {m.group(1)} breakpoint.")
for n, key, desc in [
    ("--dig-utilities__focus-ring__thickness", "focus-ring-width", "The declared 3px focus-ring thickness."),
    ("--dig-utilities__blur", "blur", "The declared backdrop blur."),
    ("--dig-utilities__overlay-blur", "overlay-blur", "The declared overlay blur."),
    ("--dig-foundations-version", "dig-foundations-version", "The generated DIG foundations version the site serves."),
]:
    if n in LIT:
        layout[key] = var(n, "other" if "version" in n else "dimension",
                          source=f"css-var {n} resolved light (raw/css-vars.json)",
                          description=desc)
# measured layout values
for key, comp, state, prop, desc in [
    ("nav-height", "header", "default", "height", "The 72px sticky nav height."),
    ("nav-height-mobile", "m-header", "default", "height", "The mobile nav height."),
]:
    if have(comp, state, prop):
        layout[key] = {"type": "dimension", "value": st(comp, state)[prop],
                       "source": f"computed {prop} of {comp} {state} (raw/components-computed.json)",
                       "description": desc}

# ------------------------------------------------------------- measured
meas = SPEC["core"].setdefault("measured", {})
for key, comp, state, prop, ty, desc in [
    ("cta-fill", "plan-cta", "default", "backgroundColor", "color", "The fill a primary marketing CTA paints — #0061fe blue, not the declared primary-cta role (#050505) the older DIG components use."),
    ("cta-fill-hover", "plan-cta", "hover", "backgroundColor", "color", "The painted CTA hover — the --dwg-theme__color__primary__button--hover value."),
    ("cta-fill-pressed", "plan-cta", "pressed", "backgroundColor", "color", "The painted CTA pressed — the --dwg-theme__color__primary__button--active value."),
    ("cta-text", "plan-cta", "default", "color", "color", "Text on the painted CTA."),
    ("focus-ring", "nav-cta", "focus-visible", "boxShadow", "shadow", "The keyboard focus ring painted on a real control — a 3px #428bff shadow ring."),
    ("focus-ring-field", "email-field", "focused", "boxShadow", "shadow", "The focus ring on the email field."),
    ("menu-hover-wash", "menu-link", "hover", "backgroundColor", "color", "The coconut-tinted wash a menu row paints on hover."),
    ("display-tracking", "hero-title", "default", "letterSpacing", "other", "The display heading's painted tracking."),
]:
    try:
        if prop == "boxShadow":
            s = st(comp, state)[prop]
            layers = parse_shadow(s)
            layers = [l for l in layers if l["color"] not in ("rgba(0, 0, 0, 0)",)]
            if layers:
                meas[key] = {"value": layers, "type": "shadow",
                             "source": f"computed boxShadow of {comp} {state} (raw/components-computed.json)",
                             "description": desc}
            continue
        if have(comp, state, prop):
            meas[key] = {"value": norm_color(st(comp, state)[prop]), "type": ty,
                         "source": f"computed {prop} of {comp} {state} (raw/components-computed.json)",
                         "description": desc}
    except KeyError:
        pass

# measured painted radii (vis2023 declares 4-24px; what the components paint)
for key, comp, state, desc in [
    ("radius-button", "hero-cta", "default", "The radius a primary CTA paints."),
    ("radius-nav-cta", "nav-cta", "default", "The radius the header Get-started pill paints."),
    ("radius-card", "plan-card", "default", "The radius a plan card paints."),
    ("radius-pill", "billing-radio", "default", "The radius the billing radio paints."),
    ("radius-field", "email-field", "default", "The radius a text field paints."),
]:
    if have(comp, state, "borderTopLeftRadius"):
        meas[key] = {"value": st(comp, state)["borderTopLeftRadius"], "type": "dimension",
                     "source": f"computed borderTopLeftRadius of {comp} {state} (raw/components-computed.json)",
                     "description": desc}
# measured transition
for key, comp, state, desc in [
    ("control-transition", "hero-cta", "default", "The transition a primary control paints."),
]:
    try:
        s = st(comp, state)
        d = s["transitionDuration"]
        first = d.split(",")[0].strip()
        if first and first != "0s":
            meas[key] = {"value": first, "type": "duration",
                         "source": f"computed transition of {comp} {state} (raw/components-computed.json)",
                         "description": desc + f" ({s['transitionProperty']})"}
    except (KeyError, TypeError):
        pass
# pressed scale, if a pressed control shrinks
try:
    d0 = C["hero-cta"]["states"]["default"]["rect"]["w"]
    dp = C["hero-cta"]["states"]["pressed"]["rect"]["w"]
    if d0 and dp and dp < d0:
        meas["pressed-scale"] = {"value": round(dp / d0, 4), "type": "number",
                                 "source": "pressed rect / default rect of hero-cta (raw/components-computed.json)",
                                 "description": "The scale a pressed button takes."}
except KeyError:
    pass

# ------------------------------------------------------------------ component

comp = SPEC["component"]
for key, cname, state, prop, desc in [
    ("button-cta.height", "hero-cta", "default", "height", "The hero primary CTA height."),
    ("button.height", "plan-cta", "default", "height", "The standard primary button height (plan actions, auth Continue)."),
    ("button-nav.height", "nav-cta", "default", "height", "The header Get-started pill height."),
    ("navitem.height", "nav-link", "default", "height", "A top-level nav item height."),
    ("field.height", "email-field", "default", "height", "The auth email-field height."),
    ("sso.height", "sso-button", "default", "height", "The SSO button height."),
    ("radio.height", "billing-radio", "default", "height", "The billing-radio label height."),
    ("iconbutton.height", "icon-button", "default", "height", "The dwg-icon-button box."),
    ("menurow.height", "m-nav-item", "default", "height", "A mobile-menu row height."),
    ("nav.height", "header", "default", "height", "The 72px desktop nav."),
    ("nav.height-mobile", "m-header", "default", "height", "The mobile nav."),
    ("plancard.height", "plan-card", "default", "height", "A plan card's height."),
    ("plancard.width", "plan-card", "default", "width", "A plan card's width."),
    ("authcard.height", "auth-card", "default", "height", "The auth card's height."),
    ("dropdown.width", "nav-dropdown", "default", "width", "The Products mega-menu panel width."),
]:
    if have(cname, state, prop):
        node = comp
        parts = key.split(".")
        for p in parts[:-1]:
            node = node.setdefault(p, {})
        node[parts[-1]] = {"type": "dimension", "value": st(cname, state)[prop],
                           "source": f"computed {prop} of {cname} {state} (raw/components-computed.json)",
                           "description": desc}

(RAW / "component-tokens.json").write_text(json.dumps(SPEC, indent=1, ensure_ascii=False) + "\n")


def count(d):
    if not isinstance(d, dict):
        return 1
    if "var" in d or "value" in d or "$value" in d:
        return 1
    return sum(count(v) for v in d.values())


print({k: count(v) for k, v in SPEC.items() if not k.startswith("_")})
