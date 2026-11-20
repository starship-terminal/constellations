#!/usr/bin/env python3
"""Write raw/component-tokens.json, the token spec build_tokens.py reads.

faire.com declares a real design-token layer — Slate, Faire's design system —
in its cdn.faire.com CSS bundles (read from network bodies by
tools/capture/vars.mjs into raw/css-vars.json, since the cross-origin sheets
are invisible to the CSSOM):

  --slate-color-*        grey/neutral ramps + blue/green/orange/red/teal/
                         yellow accents, the seasonal bsr-* ramp, transparent
                         greys — and the semantic layer they feed:
                         text/surface/border/icon roles, the action.* state
                         matrix (default/hover/active/disabled/inverse/
                         critical/favorited/neutral/subdued/placeholder/
                         focus_ring), button/message/tag/toggle/progress/
                         expressive/program roles. All land under light.color.*
                         (the only theme the signed-out site paints) or
                         core.color.* (the ramps).
  --slate-typography-*   the Graphik/Nantes type ramp: family + weight +
                         font-size/line-height/letter-spacing 100-800
  --f_t_*                the older f_t ramp still on the page (graphik/nantes
                         stacks, sizes 12-72, weights 200/400/500/700)
  --slate-spacing-*      element/group/layout/section spacing scale on the
                         4px --spacing base
  --slate-dimensions-*   the 4-80px px ramp (the rem-* duplicates resolve to
                         the same px values; only the px set is tokenised)
  --slate-radius-*, --radius-*   component and container radii
  --slate-elevation-*, --drop-shadow-*   the two elevation strings
  --container-*, --blur-*, --ease-*, --default-transition-*, --text-* and
                         companions    Tailwind-v4 theme vars in the same
                         bundle (kept as the utility ramp)
  .fs-mode-on-surface    a scoped remap of the action/button/tag/toggle roles
                         for elements painted on dark media; emitted under
                         light.color.onSurface.* with the var() chain in the
                         source string

Vendor vars are left out on purpose: --toastify-* (react-toastify) is a
library, and the OneTrust consent layer's vars come from the consent SDK.
The odd one-offs (--sa-uid, --gradient-angle, --transition-property-top,
--assistant-mode-*) are listed in _notTokenised.

Measured evidence (raw/components-computed.json, live DOM computed styles)
supplies the typography composites under core.typography.* and the geometry
under core.component.* (button heights, dialog widths, the 2px blue focus
ring, checkbox size, drawer width, header heights).

A leaf is {"var": "--name"} (resolved by build_tokens.py against the probe's
:root declarations), {"value": ..., "source": ...} for a measured value, or a
pre-built DTCG leaf for typography composites.
"""
import json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
V = json.loads((RAW / "css-vars.json").read_text())
RL = V["resolved"]["light"]
C = json.loads((RAW / "components-computed.json").read_text())["components"]
R = {n: v.get("value", v.get("raw")) for n, v in RL.items()}

SPEC = {
    "_about": (
        "The token tree build_tokens.py turns into tokens.json. Declared "
        "--slate-* names (plus the Tailwind theme vars in the same bundle and "
        "the legacy --f_t_* ramp) cover the scales under core.* and the "
        "semantic roles under light.color.* — the only theme the signed-out "
        "site paints. The .fs-mode-on-surface scope lands under "
        "light.color.onSurface.*. Measured computed styles cover the "
        "typography composites and core.component.* geometry. Vendor vars "
        "(toastify, OneTrust) are deliberately not tokenised."),
    "_notTokenised": [
        "--sa-uid", "--gradient-angle", "--header-glow-gradient-angle",
        "--assistant-mode-glow-angle", "--transition-property-top",
        "--toastify-* (react-toastify library vars)",
        "--ot-* / OneTrust consent-SDK vars",
        "--slate-dimensions-rem-* (rem duplicates of the px ramp)",
    ],
    "core": {}, "light": {}, "dark": {}, "component": {},
}


def var(name, ty="color", **kw):
    d = {"var": name, "type": ty}
    d.update(kw)
    return d


def val(value, ty, source, **kw):
    d = {"value": value, "type": ty, "source": source}
    d.update(kw)
    return d


def _is_leaf(node):
    return isinstance(node, dict) and ("var" in node or "value" in node or "$value" in node)


def put(root, parts, leaf):
    """Set tree[parts] = leaf. When a name is both a leaf and a prefix
    (--x-critical and --x-critical-hover), the leaf slides under "default"."""
    node = root
    for p in parts[:-1]:
        child = node.setdefault(p, {})
        if _is_leaf(child):
            node[p] = {"default": child}
            child = node[p]
        node = child
    last = parts[-1]
    cur = node.get(last)
    if isinstance(cur, dict) and cur and not _is_leaf(cur):
        cur["default"] = leaf
    else:
        node[last] = leaf


def camel(s):
    bits = re.split(r"[_\s]+", s)
    return bits[0] + "".join(b[:1].upper() + b[1:] for b in bits[1:] if b)


# ---------------------------------------------------------------- ramps ----
PALETTES = ("blue", "green", "grey", "neutral", "orange", "red", "teal", "yellow")

for name in R:
    m = re.fullmatch(r"--slate-color-(%s)-(\d+)" % "|".join(PALETTES), name)
    if m:
        put(SPEC["core"], ["color", m.group(1), m.group(2)], var(name))
    m = re.fullmatch(r"--slate-color-bsr-([a-z]+)-(\d+)", name)
    if m:
        put(SPEC["core"], ["color", "bsr", m.group(1), m.group(2)], var(name))
    m = re.fullmatch(r"--slate-color-transparent-grey-(\d+)", name)
    if m:
        put(SPEC["core"], ["color", "transparent", "grey", m.group(1)], var(name))

# ------------------------------------------------------ semantic roles ----
pale = re.compile(r"^--slate-color-(?:%s|bsr|transparent)-" % "|".join(PALETTES))
for name in sorted(R):
    if not name.startswith("--slate-color-") or pale.match(name):
        continue
    rest = name[len("--slate-color-"):]
    put(SPEC["light"], ["color"] + [camel(p) for p in rest.split("-")], var(name))

# legacy fs aliases of the same roles
for name in sorted(R):
    if name.startswith("--color-fs-"):
        rest = name[len("--color-fs-"):]
        put(SPEC["light"], ["color", "fs"] + [camel(p) for p in rest.split("-")], var(name))

# --------------------------------------------------- on-surface scope ----
# .fs-mode-on-surface remaps the same semantic names for controls painted on
# dark media. The scope is not resolved in the probe (it reads :root only), so
# each var() reference is followed here and the resolved value recorded with
# the chain in the source string.
def resolve_chain(raw):
    """Follow var(--a, var(--b, fallback)) through the :root declarations."""
    seen = []
    cur = raw.strip()
    while True:
        m = re.match(r"var\(\s*(--[a-zA-Z0-9_-]+)\s*(?:,\s*(.*))?\)$", cur, re.S)
        if not m:
            return cur if cur in R.values() or cur else None, seen
        name, fallback = m.group(1), m.group(2)
        seen.append(name)
        if name in R:
            return R[name], seen
        cur = (fallback or "").strip()
        if not cur:
            return None, seen


onsurface = None
for rules in (V.get("theme", []), V.get("app", [])):
    for r in rules:
        if "fs-mode-on-surface" in r.get("selector", ""):
            onsurface = r["properties"]
            break
    if onsurface:
        break
if onsurface:
    for name, raw in sorted(onsurface.items()):
        if not name.startswith("--slate-color-"):
            continue
        resolved, chain = resolve_chain(raw)
        if resolved is None:
            continue
        rest = name[len("--slate-color-"):]
        put(
            SPEC["light"],
            ["color", "onSurface"] + [camel(p) for p in rest.split("-")],
            val(resolved, "color",
                f"css-var {name} declared under .fs-mode-on-surface = {raw}"
                + (f" (resolves via {', '.join(chain)})" if chain else "")),
        )

# --------------------------------------------------------- typography ----
TYPEMAP = [
    ("family", "face", "fontFamily"),
    ("weight", "weight", "fontWeight"),
    ("font-size", "size", "dimension"),
    ("line-height", "lineHeight", "dimension"),
    ("letter-spacing", "letterSpacing", "dimension"),
]
for name in sorted(R):
    m = re.fullmatch(r"--slate-typography-([a-z-]+)-(\w+)", name)
    if m:
        for varpart, tokpart, ty in TYPEMAP:
            if m.group(1) == varpart:
                put(SPEC["core"], ["font", tokpart, m.group(2)], var(name, ty))
# family tokens are bare names (sans -> "Graphik_fix"); the full stacks ride
# the --font-family-* vars
put(SPEC["core"], ["font", "family", "sans"], var("--font-family-sans", "fontFamily",
    description="The Graphik_fix sans stack the UI type ramp uses."))
put(SPEC["core"], ["font", "family", "serif"], var("--font-family-serif", "fontFamily",
    description="The Nantes_fix serif stack the display roles use."))
put(SPEC["core"], ["font", "family", "legacySans"], var("--f_t_font_family_sans", "fontFamily",
    description="The older f_t ramp's sans stack (graphik,helvetica,sans-serif)."))
put(SPEC["core"], ["font", "family", "legacySerif"], var("--f_t_font_family_serif", "fontFamily",
    description="The older f_t ramp's serif stack (nantes,georgia,serif)."))

# extra faces the live pages paint outside the two declared stacks (measured)
def st(comp, state="default"):
    return C[comp]["states"][state]["style"]


def text(comp, state="default"):
    return C[comp]["states"][state].get("textStyle", {})


put(SPEC["core"], ["font", "family", "gtStandard"],
    val(st("cta-primary")["fontFamily"], "fontFamily",
        "measured fontFamily on the hero primary button (cta-primary default, raw/components-computed.json)",
        description="GT Standard — the sans face the large marketing buttons paint."))
put(SPEC["core"], ["font", "family", "gtCanon"],
    val(st("cat-h1")["fontFamily"], "fontFamily",
        "measured fontFamily on the category masthead (cat-h1 default, raw/components-computed.json)",
        description="GT Canon — the serif face the category masthead and auth dialog titles paint."))
put(SPEC["core"], ["font", "weight", "normal"], var("--font-weight-normal", "fontWeight"))
put(SPEC["core"], ["font", "weight", "medium"], var("--font-weight-medium", "fontWeight"))
put(SPEC["core"], ["font", "weight", "semibold"], var("--font-weight-semibold", "fontWeight"))

# the older f_t ramp (still resolved on the page)
for name in sorted(R):
    m = re.fullmatch(r"--f_t_font_size_(\d+)", name)
    if m:
        put(SPEC["core"], ["font", "legacySize", m.group(1)], var(name, "dimension"))
    m = re.fullmatch(r"--f_t_line_height_(\d+)", name)
    if m:
        put(SPEC["core"], ["font", "legacyLineHeight", m.group(1)], var(name, "dimension"))
    m = re.fullmatch(r"--f_t_font_weight_(\d+)", name)
    if m:
        put(SPEC["core"], ["font", "legacyWeight", m.group(1)], var(name, "fontWeight"))
    m = re.fullmatch(r"--f_t_letter_spacing_(\w+)", name)
    if m:
        put(SPEC["core"], ["font", "legacyLetterSpacing", m.group(1)], var(name, "dimension"))

# Tailwind utility ramp that ships in the same bundle
for name in sorted(R):
    m = re.fullmatch(r"--text-(\w[\w-]*)--line-height", name)
    if m:
        put(SPEC["core"], ["font", "utilityLineHeight", m.group(1)], var(name, "number"))
        continue
    m = re.fullmatch(r"--text-(\w[\w-]*)", name)
    if m:
        put(SPEC["core"], ["font", "utilitySize", m.group(1)], var(name, "dimension"))
    m = re.fullmatch(r"--leading-(\w+)", name)
    if m:
        put(SPEC["core"], ["font", "leading", m.group(1)], var(name, "number"))
    m = re.fullmatch(r"--tracking-(\w+)", name)
    if m:
        put(SPEC["core"], ["font", "tracking", m.group(1)], var(name, "other"))

# composite typography roles — measured on the live pages (the fs type-* and
# f_t_* classes), emitted as DTCG typography leaves
def typo(comp, state="default", use_text=False):
    s = text(comp, state) if use_text else st(comp, state)
    return {
        "$type": "typography",
        "$value": {
            "fontFamily": s["fontFamily"],
            "fontSize": s["fontSize"],
            "fontWeight": int(s["fontWeight"]),
            "lineHeight": s["lineHeight"],
            "letterSpacing": s.get("letterSpacing") or "normal",
        },
        "$extensions": {"source": f"measured {comp} {state} (raw/components-computed.json)"},
    }


put(SPEC["core"], ["typography", "display"], typo("hero-h1"))
SPEC["core"]["typography"]["display"]["$description"] = \
    "The type-fs-display marketing masthead (Nantes serif, 52/64) — 'Find your next bestseller'."
put(SPEC["core"], ["typography", "displayCanon"], typo("cat-h1"))
SPEC["core"]["typography"]["displayCanon"]["$description"] = \
    "The category-masthead serif (GT Canon, 38/50) painted over hero media — also the auth-dialog title face at 30/38."
put(SPEC["core"], ["typography", "dialogHeading"], typo("signin-dialog", use_text=True))
SPEC["core"]["typography"]["dialogHeading"]["$description"] = \
    "The fs-modal title style (GT Canon, 30/38) — 'Sign in to Faire'."
put(SPEC["core"], ["typography", "formHeading"], typo("apply-heading"))
SPEC["core"]["typography"]["formHeading"]["$description"] = \
    "The /apply step heading (nantes, 30/38) — 'Welcome! Sign up to sell on Faire.'"
put(SPEC["core"], ["typography", "paragraph"], typo("cta-plain"))
SPEC["core"]["typography"]["paragraph"]["$description"] = \
    "The type-fs-paragraph body style (Graphik_fix, 14/20, +0.15px tracking)."
put(SPEC["core"], ["typography", "caption"], typo("categories-panel", use_text=True))
SPEC["core"]["typography"]["caption"]["$description"] = \
    "The 12/16 fine-print style inside the categories menu (graphik legacy stack, +0.15px tracking)."

# ------------------------------------------------------------- scales ----
put(SPEC["core"], ["space", "base"], var("--spacing", "dimension",
    description="The 4px base every spacing utility multiplies."))
for name in sorted(R):
    m = re.fullmatch(r"--slate-spacing-([a-z]+)-(.*)", name)
    if m:
        put(SPEC["core"], ["space", m.group(1)] + [camel(p) for p in m.group(2).split("-")],
            var(name, "dimension"))
    m = re.fullmatch(r"--slate-dimensions-(\d+)", name)
    if m:
        put(SPEC["core"], ["dimension", m.group(1)], var(name, "dimension"))
    m = re.fullmatch(r"--slate-radius-(.*)", name)
    if m:
        put(SPEC["core"], ["radius", "component"] + [camel(p) for p in m.group(1).split("-")],
            var(name, "dimension"))
    m = re.fullmatch(r"--radius-(.*)", name)
    if m:
        put(SPEC["core"], ["radius"] + [camel(p) for p in m.group(1).split("-")],
            var(name, "dimension"))
    m = re.fullmatch(r"--container-(.*)", name)
    if m:
        put(SPEC["core"], ["container", camel(m.group(1))], var(name, "dimension"))
    m = re.fullmatch(r"--blur-(.*)", name)
    if m:
        put(SPEC["core"], ["blur", camel(m.group(1))], var(name, "dimension"))

put(SPEC["core"], ["elevation", "low"], var("--slate-elevation-low", "other",
    description="The low card/dropdown shadow."))
put(SPEC["core"], ["elevation", "medium"], var("--slate-elevation-medium", "other",
    description="The medium overlay shadow."))
put(SPEC["core"], ["elevation", "sm"], var("--drop-shadow-sm", "other"))
put(SPEC["core"], ["elevation", "md"], var("--drop-shadow-md", "other"))
put(SPEC["core"], ["ease", "in"], var("--ease-in", "cubicBezier"))
put(SPEC["core"], ["ease", "out"], var("--ease-out", "cubicBezier"))
put(SPEC["core"], ["ease", "inOut"], var("--ease-in-out", "cubicBezier"))
put(SPEC["core"], ["motion", "duration", "default"], var("--default-transition-duration", "duration"))
put(SPEC["core"], ["motion", "duration", "glow"], var("--glow-duration", "duration"))
put(SPEC["core"], ["motion", "duration", "headerGlow"], var("--header-glow-duration", "duration"))
put(SPEC["core"], ["motion", "easing", "default"], var("--default-transition-timing-function", "cubicBezier"))
put(SPEC["core"], ["motion", "animation", "spin"], var("--animate-spin", "other"))
put(SPEC["core"], ["motion", "animation", "pulse"], var("--animate-pulse", "other"))
put(SPEC["core"], ["motion", "animation", "bounce"], var("--animate-bounce", "other"))
put(SPEC["core"], ["aspect", "video"], var("--aspect-video", "other"))

# ----------------------------------------------------- measured geometry --
def px(v):
    return str(v)


def rd(comp, prop, ty, state="default", note=""):
    """A computed style read on comp in raw/components-computed.json; raises when the
    component, state or property is missing, so a recapture that loses it fails the build."""
    v = C[comp]["states"][state]["style"].get(prop)
    if v in (None, ""):
        raise KeyError(f"{comp} {state}: no {prop} reading")
    return val(v, ty, f"computed {prop} of {comp} {state} (raw/components-computed.json){note}")


def anc(comp, key, ty, note, state="default"):
    """A value recorded on the first ancestor that paints it (styleOf's `ancestors`)."""
    for a in C[comp]["states"][state].get("ancestors") or []:
        if a.get(key):
            return val(a[key], ty, f"painted {key} of {a['node']}, the ancestor of {comp} {state} (raw/components-computed.json){note}")
    raise KeyError(f"{comp} {state}: no ancestor paints {key}")


HAND = "Reconstruction — entered by hand at capture time, no raw reading behind it"

comp = SPEC["component"]
put(comp, ["button", "height", "small"], rd("nav-signup-buy", "height", "dimension", note="; the header fs-button--primary small"))
put(comp, ["button", "height", "medium"], rd("cta-primary", "height", "dimension", note="; next-btn matches"))
put(comp, ["button", "paddingX", "small"], rd("nav-signup-buy", "paddingLeft", "dimension"))
put(comp, ["button", "paddingX", "medium"], rd("cta-primary", "paddingLeft", "dimension"))
put(comp, ["button", "radius"], rd("cta-primary", "borderTopLeftRadius", "dimension",
    note="; nav-signup-buy matches; matches --slate-radius-component-default"))
put(comp, ["radius", "filter"], rd("cat-filter-btn", "borderTopLeftRadius", "dimension",
    note="; the All-filters pill; matches --slate-radius-component-filter"))
put(comp, ["field", "inputHeight"], rd("field-email", "height", "dimension",
    note="; the text input inside the boxed apply field (signin-email matches)"))
# The text inputs measure borderTopWidth 0px and their fs-form-field box records no border, so the
# 1px field border was typed in at capture time.
put(comp, ["field", "borderWidth"], val("1px", "dimension",
    HAND + " (field-firstname measures borderTopWidth 0px, and its fs-form-field box records no border)"))
put(comp, ["checkbox", "size"], rd("checkbox-terms", "width", "dimension"))
put(comp, ["checkbox", "radius"], anc("checkbox-terms", "radius", "dimension",
    "; the input itself measures 0px; matches --slate-radius-component-checkbox"))
put(comp, ["dialog", "width", "signIn"], rd("signin-dialog", "width", "dimension", note="; the Sign in to Faire fs-modal"))
put(comp, ["dialog", "width", "signUp"], rd("signup-dialog", "width", "dimension", note="; the Unlock wholesale pricing fs-modal"))
put(comp, ["navDrawer", "width"], rd("m-drawer", "width", "dimension", note="; the mobile nav drawer"))
put(comp, ["avatar", "brand"], rd("brand-avatar", "width", "dimension", note="; the circular fs-avatar on the brand storefront"))
put(comp, ["categoriesPanel", "height"], rd("categories-panel", "height", "dimension", note="; the All categories dropdown at 1440x900"))
put(comp, ["header", "height", "desktop"], rd("mkt-header", "height", "dimension", note="; header incl. promo strip and category nav"))
put(comp, ["header", "height", "mobile"], rd("m-topbar", "height", "dimension", note="; the phone top bar"))
put(comp, ["focusRing", "width"], rd("cta-primary", "outlineWidth", "dimension", state="focus-visible",
    note="; nav-signup-buy and next-btn match"))
put(comp, ["focusRing", "offset"], rd("cta-primary", "outlineOffset", "dimension", state="focus-visible", note="; next-btn matches"))
put(comp, ["focusRing", "color"], rd("cta-primary", "outlineColor", "color", state="focus-visible",
    note="; next-btn matches; the blue action-border-focus_ring role"))

def count(d):
    return sum(count(v) for v in d.values()) if isinstance(d, dict) and "$value" not in d and "var" not in d and "value" not in d else 1


if __name__ == "__main__":
    (RAW / "component-tokens.json").write_text(
        json.dumps(SPEC, indent=2, ensure_ascii=False) + "\n")
    print({k: count(v) for k, v in SPEC.items() if not k.startswith("_")})
