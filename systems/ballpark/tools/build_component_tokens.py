#!/usr/bin/env python3
"""Write raw/component-tokens.json, the token spec build_tokens.py reads.

ballparkhq.com is a Framer site; its bundle declares on `body`
(raw/css-vars.json, read by tools/capture/vars.mjs):

  --token-<uuid>   the project's palette, 213 entries. 191 of them are the
                   Tailwind v3 default palette under Framer's uuid names
                   (#f5f5f5 = neutral.100, ...), emitted here under their
                   Tailwind names -> core.color.<family>.<step>. The rest are
                   the product's own colours: an 11-step coral/flame ramp
                   (the "NEW" chip and CTA colour), two brand blues, a dark
                   teal, and six translucent greys for hairlines and scrims
                   -> core.color.brand.* / core.color.gray-alpha.*
  --framer-*       Framer's own layout/effect internals, not a design scale;
                   recorded in css-vars.json but not tokenised

A leaf is {"var": "--name"} (resolved by build_tokens.py) or {"value": ...,
"source": "..."} for a measured value. The readable token name is decided
here, so build_tokens.py's spec carries names like color.flame.500 while the
"var" still points at the real --token-<uuid> declaration.
"""
import json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
V = json.loads((RAW / "css-vars.json").read_text())
RL = V["resolved"]["light"]
C = json.loads((RAW / "components-computed.json").read_text())["components"]
R = {n: v.get("value", v.get("raw")) for n, v in RL.items()}

# Tailwind v3 default palette: 20 hues at steps 50-950 plus black/white.
TW = {
'slate':'#f8fafc #f1f5f9 #e2e8f0 #cbd5e1 #94a3b8 #64748b #475569 #334155 #1e293b #0f172a',
'gray':'#f9fafb #f3f4f6 #e5e7eb #d1d5db #9ca3af #6b7280 #4b5563 #374151 #1f2937 #111827',
'zinc':'#fafafa #f4f4f5 #e4e4e7 #d4d4d8 #a1a1aa #71717a #52525b #3f3f46 #27272a #18181b',
'neutral':'#fafafa #f5f5f5 #e5e5e5 #d4d4d4 #a3a3a3 #737373 #525252 #404040 #262626 #171717',
'stone':'#fafaf9 #f5f5f4 #e7e5e4 #d6d3d1 #a8a29e #78716c #57534e #44403c #292524 #1c1917',
'red':'#fef2f2 #fee2e2 #fecaca #fca5a5 #f87171 #ef4444 #dc2626 #b91c1c #991b1b #7f1d1d',
'orange':'#fff7ed #ffedd5 #fed7aa #fdba74 #fb923c #f97316 #ea580c #c2410c #9a3412 #7c2d12',
'amber':'#fffbeb #fef3c7 #fde68a #fcd34d #fbbf24 #f59e0b #d97706 #b45309 #92400e #78350f',
'yellow':'#fefce8 #fef9c3 #fef08a #fde047 #facc15 #eab308 #ca8a04 #a16207 #854d0e #713f12',
'lime':'#f7fee7 #ecfccb #d9f99d #bef264 #a3e635 #84cc16 #65a30d #4d7c0f #3f6212 #365314',
'green':'#f0fdf4 #dcfce7 #bbf7d0 #86efac #4ade80 #22c55e #16a34a #15803d #166534 #14532d',
'emerald':'#ecfdf5 #d1fae5 #a7f3d0 #6ee7b7 #34d399 #10b981 #059669 #047857 #065f46 #064e3b',
'teal':'#f0fdfa #ccfbf1 #99f6e4 #5eead4 #2dd4bf #14b8a6 #0d9488 #0f766e #115e59 #134e4a',
'cyan':'#ecfeff #cffafe #a5f3fc #67e8f9 #22d3ee #06b6d4 #0891b2 #0e7490 #155e75 #164e63',
'sky':'#f0f9ff #e0f2fe #bae6fd #7dd3fc #38bdf8 #0ea5e9 #0284c7 #0369a1 #075985 #0c4a6e',
'blue':'#eff6ff #dbeafe #bfdbfe #93c5fd #60a5fa #3b82f6 #2563eb #1d4ed8 #1e40af #1e3a8a',
'indigo':'#eef2ff #e0e7ff #c7d2fe #a5b4fc #818cf8 #6366f1 #4f46e5 #4338ca #3730a3 #312e81',
'violet':'#f5f3ff #ede9fe #ddd6fe #c4b5fd #a78bfa #8b5cf6 #7c3aed #6d28d9 #5b21b6 #4c1d95',
'purple':'#faf5ff #f3e8ff #e9d5ff #d8b4fe #c084fc #a855f7 #9333ea #7e22ce #6b21a8 #581c87',
'fuchsia':'#fdf4ff #fae8ff #f5d0fe #f0abfc #e879f9 #d946ef #c026d3 #a21caf #86198f #701a75',
'pink':'#fdf2f8 #fce7f3 #fbcfe8 #f9a8d4 #f472b6 #ec4899 #db2777 #be185d #9d174d #831843',
'rose':'#fff1f2 #ffe4e6 #fecdd3 #fda4af #fb7185 #f43f5e #e11d48 #be123c #9f1239 #881337',
}
STEPS = [50, 100, 200, 300, 400, 500, 600, 700, 800, 900]
LOOKUP = {}
for fam, cols in TW.items():
    for step, hx in zip(STEPS, cols.split()):
        LOOKUP[hx] = f"{fam}.{step}"
LOOKUP["#ffffff"] = "white"
LOOKUP["#000000"] = "black"

# The product's own colours among the --token-* declarations, named by hand
# after what the site paints them as (checked against the screenshots):
#   flame  the coral ramp of the NEW chip, hero underline and CTAs
#   navy   the deep blue accents
#   pine   the dark teal used on badges
#   grey-alpha  translucent greys for hairlines and the header scrim
BRAND = {
    "#fff3f1": "brand.flame.50", "#ffe5e0": "brand.flame.100", "#ffcec6": "brand.flame.200",
    "#ffac9e": "brand.flame.300", "#ff7e67": "brand.flame.400", "#fc4a2b": "brand.flame.500",
    "#ea3718": "brand.flame.600", "#c52b10": "brand.flame.700", "#a32711": "brand.flame.800",
    "#872615": "brand.flame.900", "#4a0f05": "brand.flame.950",
    "#0954a5": "brand.navy.700", "#0a4481": "brand.navy.900",
    "#114e59": "brand.pine.900",
    "rgba(75, 85, 99, 0.1)": "gray-alpha.10", "rgba(75, 85, 99, 0.2)": "gray-alpha.20",
    "rgba(75, 85, 99, 0.3)": "gray-alpha.30", "rgba(75, 85, 99, 0.4)": "gray-alpha.40",
    "rgba(156, 163, 175, 0.25)": "gray-alpha.25", "rgba(229, 231, 235, 0.5)": "gray-alpha.50",
    "rgba(243, 244, 246, 0.8)": "gray-alpha.80",
}


def descend(root, parts):
    node = root
    for p in parts[:-1]:
        node = node.setdefault(p, {})
    node[parts[-1]] = None
    return node, parts[-1]


SPEC = {"_about": (
    "The token tree build_tokens.py turns into tokens.json. ballparkhq.com is a "
    "Framer build: its --token-<uuid> palette is the Tailwind v3 ramp set "
    "(emitted under the Tailwind names) plus the product's own flame, navy, "
    "pine and grey-alpha colours. \"var\" leaves resolve through the live "
    "document; \"value\" leaves are measured."),
    "core": {}, "light": {}, "component": {}}

unmatched = []
for name in sorted(n for n in R if n.startswith("--token-")):
    v = R[name]
    path = LOOKUP.get(v) or BRAND.get(v)
    if not path:
        unmatched.append((name, v))
        continue
    node, last = descend(SPEC["core"].setdefault("color", {}), path.split("."))
    node[last] = {"var": name, "type": "color"}
if unmatched:
    raise SystemExit("unmapped --token colours: " + "; ".join(f"{v} {n}" for n, v in unmatched))

# ------------------------------------------------------------- light roles
#
# The bundle declares no semantic role names of its own; these roles are
# measured on the painted chrome (header, hero, footer) and point at palette
# tokens where the value matches.
def st(comp, state):
    c = C[comp]
    if c.get("missing") or c.get("recaptureMissed"):
        raise KeyError(comp)
    return c["states"][state]["style"]


def stprop(comp, state, prop):
    """prop may be `styleProp`, `textStyle.prop`, `::after.prop` or the special
    `ringShadow`: resolve the dotted path inside the measured state (the
    anchors keep UA-default colour, so painted text/border lives on the text
    child or a pseudo). `ringShadow` returns the colour of the `0 0 0 Npx`
    ring layer in the element's own boxShadow — the hairline many Framer
    controls paint instead of a real border."""
    d = C[comp]["states"][state]
    if prop == "ringShadow":
        sh = d.get("style", {}).get("boxShadow", "") or ""
        for layer in re.split(r",(?![^(]*\))", sh):
            if re.search(r"0px 0px 0px\s+(?:0\.[5-9]|[1-9])[\d.]*px", layer):
                m = re.search(r"rgba?\([^)]*\)|#[0-9a-fA-F]{3,8}", layer)
                if m:
                    return m.group(0)
        return ""
    if "." in prop:
        head, tail = prop.split(".", 1)
        node = d.get(head)
        if not isinstance(node, dict):
            return ""
        return node.get(tail, "")
    return d.get("style", {}).get(prop, "")


def norm_color(v):
    v = (v or "").strip()
    m = re.fullmatch(r"#([0-9a-fA-F]{3,8})", v)
    if m:
        h = m.group(1).lower()
        if len(h) in (3, 4):
            h = "".join(c * 2 for c in h)
        return "#" + h
    m = re.fullmatch(r"rgba?\(([\d.]+),\s*([\d.]+),\s*([\d.]+)(?:,\s*([\d.]+))?\)", v)
    if m:
        r, g, b, a = m.groups()
        if a is None or float(a) >= 1:
            return "#%02x%02x%02x" % (int(float(r)), int(float(g)), int(float(b)))
        return f"rgba({int(float(r))}, {int(float(g))}, {int(float(b))}, {'%g' % float(a)})"
    m = re.fullmatch(r"oklab\(\s*([\d.]+)\s+(-?[\d.]+)\s+(-?[\d.]+)(?:\s*/\s*([\d.]+%?))?\s*\)", v)
    if m:
        # Framer paints some alpha greys as oklab(); convert to sRGB.
        L, A, B = (float(m.group(i)) for i in (1, 2, 3))
        l_ = (L + 0.3963377774 * A + 0.2158037573 * B) ** 3
        m_ = (L - 0.1055613458 * A - 0.0638541729 * B) ** 3
        s_ = (L - 0.0894841775 * A - 1.2914855480 * B) ** 3
        R_ = +4.0767416621 * l_ - 3.3077115913 * m_ + 0.2309699292 * s_
        G_ = -1.2684380046 * l_ + 2.6097574011 * m_ - 0.3413193965 * s_
        B_ = -0.0041960863 * l_ - 0.7034186147 * m_ + 1.7076147010 * s_
        gam = lambda x: max(0, min(255, round((12.92 * x if x <= 0.0031308 else 1.055 * x ** (1 / 2.4) - 0.055) * 255)))
        a = m.group(4)
        a = float(a[:-1]) / 100 if a and a.endswith("%") else float(a) if a else 1
        if a >= 1:
            return "#%02x%02x%02x" % (gam(R_), gam(G_), gam(B_))
        return f"rgba({gam(R_)}, {gam(G_)}, {gam(B_)}, {'%g' % a})"
    return v


BY_VALUE = {}
def collect(node, prefix=""):
    for k, v in node.items():
        if isinstance(v, dict) and "var" in v:
            val = norm_color(R[v["var"]])
            BY_VALUE.setdefault(val, prefix + k)
        elif isinstance(v, dict):
            collect(v, prefix + k + ".")
collect(SPEC["core"].setdefault("color", {}), "color.")


def role(path, comp, state, prop, desc):
    v = norm_color(stprop(comp, state, prop))
    if not v or v == "transparent":
        return
    target = BY_VALUE.get(v)
    leaf = {"type": "color", "description": desc}
    if target:
        leaf["value"] = "{%s}" % target
        leaf["source"] = f"computed {prop} of {comp} {state} (raw/components-computed.json); same value as core.{target}"
    else:
        leaf["value"] = v
        leaf["source"] = f"computed {prop} of {comp} {state} (raw/components-computed.json)"
    node = SPEC["light"]
    parts = path.split(".")
    for p in parts[:-1]:
        node = node.setdefault(p, {})
    node[parts[-1]] = leaf


for path, comp, state, prop, desc in [
    ("page", "header", "default", "backgroundColor", "The page ground behind the header."),
    ("foreground", "hero-title", "default", "color", "The ink of display type."),
    ("muted", "hero-sub", "default", "textStyle.color", "Secondary text under the hero, painted on the inner span."),
    ("accent", "nav-cta", "default", "backgroundColor", "The black CTA fill."),
    ("accentText", "nav-cta", "default", "textStyle.color", "Text painted on the black CTA (the anchor itself keeps the UA link colour)."),
    ("accentHover", "nav-cta", "hover", "backgroundColor", "The CTA fill on hover."),
    ("link", "footer-legal", "default", "color", "The muted legal/footer link colour."),
    ("border", "nav-signin", "default", "ringShadow", "The bordered pill's hairline, painted as a 1px ring shadow on the anchor (its ::after draws no border)."),
    ("chip", "announcement-bar", "default", "backgroundColor", "The announcement strip's ground."),
    ("focus", "nav-cta", "focus-visible", "outlineColor", "The keyboard-focus ring where one is drawn."),
]:
    try:
        role(path, comp, state, prop, desc)
    except KeyError:
        pass

# -------------------------------------------------- measured extras (no var)

meas = SPEC["core"].setdefault("measured", {})
for comp, state, key, prop, desc in [
    ("nav-cta", "focus-visible", "focus-outline", "outlineColor", "The keyboard-focus ring on the nav CTA."),
    ("contact-submit", "hover", "submit-hover", "backgroundColor", "The form submit on hover."),
    ("signin-field", "default", "field-border", "borderTopColor", "The sign-in field's edge."),
    ("contact-field", "default", "field-bg", "backgroundColor", "The sales field's fill."),
]:
    try:
        v = norm_color(st(comp, state).get(prop, ""))
        if v and v != "transparent":
            meas[key] = {"value": v, "type": "color",
                         "source": f"computed {prop} of {comp} {state} (raw/components-computed.json)",
                         "description": desc}
    except KeyError:
        pass

# ------------------------------------------------------------------ component

comp = SPEC["component"]
for key, cname, state, prop, desc in [
    ("control.heightNav", "nav-link", "default", "height", "Nav controls are 36px."),
    ("control.heightCta", "nav-cta", "default", "height", "The Book a demo pill height."),
    ("control.fieldHeight", "signin-field", "default", "height", "The sign-in field height."),
    ("control.fieldHeightSales", "contact-field", "default", "height", "The sales field height."),
    ("control.heightSubmit", "contact-submit", "default", "height", "The sales submit height."),
    ("control.radiusPill", "nav-cta", "default", "borderTopLeftRadius", "The CTA's corner."),
    ("control.radiusField", "signin-field", "default", "borderTopLeftRadius", "The sign-in field's corner."),
    ("control.radiusCard", "feature-card", "default", "borderTopLeftRadius", "The feature card's corner."),
    ("header.height", "header", "default", "height", "The full header block at 1440px."),
    ("footer.height", "footer", "default", "height", "The footer block at 1440px."),
]:
    try:
        node = comp
        parts = key.split(".")
        for p in parts[:-1]:
            node = node.setdefault(p, {})
        node[parts[-1]] = {"type": "dimension", "value": st(cname, state)[prop],
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
