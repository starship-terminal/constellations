#!/usr/bin/env python3
"""Write raw/component-tokens.json, the token spec build_tokens.py reads.

b150.ai is a Next.js/Tailwind v4 site whose stylesheet declares a real theme
layer in `@layer theme` on `:root`: --color-*, --font-*, --text-* (sizes with
line-height/letter-spacing pairs), --radius-*, --container-*, --spacing and
--ease-* (raw/css-vars.json, bin `app`, 66 names). Each leaf below names that
variable ("var") resolved per theme where the site declares one, or carries a
measured value and the measurement it came from ("source") — the fully-round
pill radius (Tailwind `rounded-full` computes to calc(infinity * 1px)), the
hover fills and the focus ring have no declaring variable.

Roles in `light` are asserted only where a measured component wears the
value. The site paints one theme; `dark` is empty.
"""
import json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
C = json.loads((RAW / "components-computed.json").read_text())["components"]


def current(comp):
    """The component's entry, refused when the last run did not read it: missing
    (no states) or recaptureMissed (earlier states kept under their own
    provenance) is not a current reading, so it cannot source a role."""
    c = C[comp]
    if c.get("missing") or c.get("recaptureMissed"):
        raise KeyError(f"{comp}: not a current reading (missing or recaptureMissed)")
    return c

SPEC = {"_about": (
    "The token tree build_tokens.py turns into tokens.json. b150.ai is a "
    "Tailwind v4 site whose `@layer theme` block declares --color-*, "
    "--font-*, --text-*, --radius-*, --container-*, --spacing and --ease-* "
    "(66 vars in raw/css-vars.json's app bin): each leaf either names that "
    "variable ('var') or carries a measured value ('source') where nothing "
    "declares it. The site paints one theme; dark is empty."),
    "core": {}, "light": {}, "dark": {}, "component": {}}


def descend(root, parts):
    node = root
    for p in parts[:-1]:
        node = node.setdefault(p, {})
    return node, parts[-1]


def emit(root, dotted, leaf):
    node, last = descend(root, dotted.split("-"))
    node[last] = leaf


def V(var, ty, desc="", extra_src=""):
    leaf = {"var": var, "type": ty}
    if extra_src:
        leaf["source"] = extra_src
    if desc:
        leaf["description"] = desc
    return leaf


def M(value, ty, where, desc=""):
    leaf = {"value": value, "type": ty, "source": where}
    if desc:
        leaf["description"] = desc
    return leaf


def st(comp, state="default"):
    return C[comp]["states"][state]


def style(comp, state="default"):
    return st(comp, state)["style"]


def norm_color(v):
    v = (v or "").strip()
    m = re.fullmatch(r"#([0-9a-fA-F]{3,8})", v)
    if m:
        h = m.group(1).lower()
        if len(h) == 3:
            h = "".join(c * 2 for c in h)
        return "#" + h
    m = re.fullmatch(r"rgba?\(([\d.]+),\s*([\d.]+),\s*([\d.]+)(?:,\s*([\d.]+))?\)", v)
    if m:
        r, g, b, a = m.groups()
        if a is None or float(a) >= 1:
            return "#%02x%02x%02x" % (int(float(r)), int(float(g)), int(float(b)))
        return f"rgba({int(float(r))}, {int(float(g))}, {int(float(b))}, {'%g' % float(a)})"
    return v


# ------------------------------------------------- declared palette
for name, var, desc in [
    ("paper", "--color-paper", "The warm-cream section ground."),
    ("cream", "--color-cream", "The slightly lighter cream (hero display text)."),
    ("light", "--color-light", "The near-white cream: nav ink and CTA fills."),
    ("ink", "--color-ink", "The warm near-black body ink."),
    ("black", "--color-black", "The footer surface."),
    ("white", "--color-white", "The SIGN UP / SEND MESSAGE pill fill."),
    ("muted", "--color-muted", "Muted text."),
    ("grey", "--color-grey", "Secondary grey."),
    ("rule", "--color-rule", "Hairline borders, field fills, CTA hover."),
]:
    emit(SPEC["core"], f"color-neutral-{name}", V(var, "color", desc))
for name, var, desc in [
    ("coral", "--color-coral", "The coral accent."),
    ("coralDeep", "--color-coral-deep", "The deep coral."),
    ("blue", "--color-blue", "Blue accent."),
    ("green", "--color-green", "Green accent."),
    ("red", "--color-red", "Red accent."),
    ("lime", "--color-lime", "Lime accent."),
]:
    emit(SPEC["core"], f"color-accent-{name}", V(var, "color", desc))

# --------------------------------------------------------------- fonts
SPEC["core"]["font"] = {"family": {}, "weight": {}, "size": {}, "leading": {}, "tracking": {}}
emit(SPEC["core"], "font-family-sans", V("--font-sans", "fontFamily", "Geist Variable stack: body and display copy."))
emit(SPEC["core"], "font-family-mono", V("--font-mono", "fontFamily", "Fragment Mono stack: labels, nav, buttons, footer."))
for key, var, comp, desc in [
    ("label", "--text-label", "nav-item", "Labels, nav, buttons (10px measured on nav-item)."),
    ("small", "--text-small", "footer-link", "Small text (10px measured on footer-link)."),
    ("body", "--text-body", "contact-input", "Body/field text (12px measured on contact-input)."),
    ("h1", "--text-h1", "hero", "Display (120px measured on the hero)."),
    ("h2", "--text-h2", "res-title", "Page titles (96px measured on res-title)."),
    ("h3", "--text-h3", "about-body", "(32px measured on about-body)."),
]:
    emit(SPEC["core"], f"font-size-{key}", V(var, "dimension", desc, f"verified: computed fontSize of {comp} (raw/components-computed.json)"))
for key, var in [("label", "--text-label--line-height"), ("small", "--text-small--line-height"), ("body", "--text-body--line-height"),
                 ("h1", "--text-h1--line-height"), ("h2", "--text-h2--line-height"), ("h3", "--text-h3--line-height"), ("normal", "--leading-normal")]:
    emit(SPEC["core"], f"font-leading-{key}", V(var, "number"))
for key, var in [("label", "--text-label--letter-spacing"), ("normal", "--tracking-normal")]:
    emit(SPEC["core"], f"font-tracking-{key}", V(var, "dimension"))
for key, var in [("normal", "--font-weight-normal"), ("medium", "--font-weight-medium"), ("semibold", "--font-weight-semibold"), ("bold", "--font-weight-bold")]:
    emit(SPEC["core"], f"font-weight-{key}", V(var, "fontWeight"))

# --------------------------------------------------------------- radius/layout/motion
emit(SPEC["core"], "radius-card", V("--radius-card", "dimension", "Card corners."))
emit(SPEC["core"], "radius-lg", V("--radius-lg", "dimension", "Fields and smaller cards (8px measured on contact-input/talent-card).", "verified: computed borderTopLeftRadius of contact-input and talent-card (raw/components-computed.json)"))
emit(SPEC["core"], "radius-xl", V("--radius-xl", "dimension"))
# Tailwind rounded-full computes to calc(infinity * 1px) = 3.35544e+07px; the
# plain-number spelling keeps the reading and parses in consumers.
emit(SPEC["core"], "radius-pill", M("33554432px", "dimension", "computed borderTopLeftRadius of signup-btn/hero-cta/contact-button/m-cta (rounded-full = calc(infinity * 1px)) (raw/components-computed.json)", "The fully-round pill radius."))
emit(SPEC["core"], "layout-container", V("--container-main", "dimension", "The content container width."))
emit(SPEC["core"], "layout-spacing", V("--spacing", "dimension", "The Tailwind spacing unit."))
emit(SPEC["core"], "motion-ease-inout", V("--ease-in-out", "cubicBezier"))
emit(SPEC["core"], "motion-ease-outQuart", V("--ease-out-quart", "cubicBezier", "The signature easing."))
emit(SPEC["core"], "motion-duration", V("--default-transition-duration", "duration"))

# --------------------------------------------------------------- measured extras
try:
    emit(SPEC["core"], "measured-focus-ring", M(norm_color(style("nav-item", "focus-visible")["outlineColor"]), "color", "computed outlineColor of nav-item focus-visible (raw/components-computed.json)", "The browser focus ring."))
except KeyError:
    pass

# --------------------------------------------------------------- roles
ROLES = [
    ("text-primary", "--color-ink", "nav-item/footer/body text where it sits on cream (verified: signup-btn/vibe-cta fg)", "Body ink on the cream surfaces."),
    ("text-inverse", "--color-light", "nav-item/footer-link fg on the dark chrome", "Cream ink on the dark chrome."),
    ("surface-page", "--color-paper", "home-section/vibe-card bg", "The warm-cream section ground."),
    ("surface-inverse", "--color-black", "footer bg", "The near-black footer/chrome surface."),
    ("surface-field", "--color-rule", "contact-input/talent-card bg", "Field fills and hairlines."),
    ("action-primary", "--color-white", "signup-btn/contact-button/m-cta bg", "The white pill fill."),
    ("action-secondary", "--color-light", "hero-cta/talent-cta bg", "The cream JOIN THE BETA fill."),
    ("action-primaryText", "--color-ink", "signup-btn fg", "Text on the pills."),
    ("action-hover", "--color-rule", "hero-cta hover bg", "The CTA's hover fill."),
    ("border-default", "--color-rule", "signup-btn border color", "The pill hairline."),
]
for role, var, verif, desc in ROLES:
    emit(SPEC["light"], role, V(var, "color", desc, f"verified: {verif} (raw/components-computed.json)"))
_ring = norm_color(current("nav-item")["states"]["focus-visible"]["style"].get("outlineColor", ""))
if not _ring:
    raise KeyError("nav-item focus-visible has no outlineColor reading")  # no typed fallback
emit(SPEC["light"], "focus-ring", M(_ring, "color", "computed outlineColor of nav-item/footer-link focus-visible (raw/components-computed.json)", "The focus ring."))

# ------------------------------------------------------------------ component
comp_spec = SPEC["component"]
for key, cname, state, prop, desc in [
    ("control.height", "signup-btn", "default", "height", "The SIGN UP pill height."),
    ("control.ctaHeight", "hero-cta", "default", "height", "The JOIN THE BETA CTA height."),
    ("control.fieldHeight", "contact-input", "default", "height", "Contact field height."),
    ("header.height", "header", "default", "height", "The desktop header height."),
    ("header.heightMobile", "m-header", "default", "height", "The mobile header height."),
]:
    try:
        node = comp_spec
        parts = key.split(".")
        for p in parts[:-1]:
            node = node.setdefault(p, {})
        node[parts[-1]] = {"type": "dimension", "value": st(cname, state)["style"][prop],
                           "source": f"computed {prop} of {cname} {state} (raw/components-computed.json)",
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
