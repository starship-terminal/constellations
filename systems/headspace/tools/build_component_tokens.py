#!/usr/bin/env python3
"""Write raw/component-tokens.json: the token tree spec for headspace.com.

headspace.com ships no usable custom-property token layer (raw/css-vars.json
keeps the stylesheets' declarations verbatim to show that), so every leaf here
is a *measured* reading from raw/components-computed.json / raw/layout.json /
raw/motion.json, each carrying its own provenance string.

Sets:
  core     theme-independent scales: font families, type scale, radii,
           spacing readings, breakpoints, motion
  light    the semantic palette the light pages paint (there is no dark set:
           no control, no attribute, no dark media rules applied)

Deterministic: same inputs, byte-identical output. This file is generated;
edit the raw inputs, never the output.
"""
import json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
C = json.loads((RAW / "components-computed.json").read_text())["components"]
LAYOUT = json.loads((RAW / "layout.json").read_text())
MOTION = json.loads((RAW / "motion.json").read_text())
SPEC = {"core": {}, "light": {}}


def st(comp, state):
    return C[comp]["states"][state]["style"]


def ts(comp, state, prop):
    """The first text node's reading when recorded — the wrapper's own
    fontSize can be the container's, not the text's."""
    try:
        c = C[comp]["states"][state]
        t = c.get("textStyle") or {}
        return t.get(prop) or c["style"].get(prop)
    except KeyError:
        return None


def parse_float(v):
    m = re.match(r"([\d.]+)", str(v))
    return float(m.group(1)) if m else 0.0


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


# Components whose one key was measured on several pages: measure.mjs kept the
# last page's reading and dropped the rest (fixed in the script, not rerun).
# Their tokens say which page the value is from.
OVERWRITTEN = {
    "hero-h1": "the /share page's headline: measure.mjs read hero-h1 on 16 pages under one key and kept the last, so the home headline was not kept; recapture needed",
    "auth-card": "the /signup card (\"Create your account\"): measured under one key on /login and /signup, the /signup reading was kept and the /login one lost; recapture needed",
}


def caveat(comp):
    return f"; {OVERWRITTEN[comp]}" if comp in OVERWRITTEN else ""


def put(bag, key, comp, state, prop, ty, desc, transform=None):
    """Emit a measured leaf when the reading exists."""
    try:
        if prop == "paint":
            v = None
            c = C[comp]["states"][state]
            for n in (c.get("paint") or []) + (c.get("ancestors") or []):
                if n.get("bg"):
                    v = n["bg"]
                    break
        elif prop == "textStyle-color":
            v = C[comp]["states"][state].get("textStyle", {}).get("color")
        elif prop.startswith("text-"):
            v = ts(comp, state, prop[5:])
        else:
            v = st(comp, state).get(prop, "")
        v = (v or "").strip()
        if not v or v == "transparent" or v == "none":
            return
        if transform:
            v = transform(v)
            if not v:
                return
        if ty == "color":
            v = norm_color(v)
        bag[key] = {"value": v, "type": ty,
                    "source": f"computed {prop} of {comp} {state} (raw/components-computed.json)" + caveat(comp),
                    "description": desc}
    except KeyError:
        pass


def put_ancestor(bag, key, comp, state, desc, ty="color"):
    """Emit the first painted ancestor's fill."""
    try:
        c = C[comp]["states"][state]
        v = None
        for n in (c.get("ancestors") or []):
            if n.get("bg"):
                v = n["bg"]
                break
        if not v:
            return
        bag[key] = {"value": norm_color(v), "type": ty,
                    "source": f"computed ancestor paint of {comp} {state} (raw/components-computed.json)",
                    "description": desc}
    except KeyError:
        pass


def put_paint_node(bag, key, comp, state, needle, desc, ty="color"):
    """Emit the fill of a specific painted child whose node label contains needle."""
    try:
        c = C[comp]["states"][state]
        for n in (c.get("paint") or []):
            if needle in (n.get("node") or "") and n.get("bg"):
                bag[key] = {"value": norm_color(n["bg"]), "type": ty,
                            "source": f"computed paint of {n['node']} inside {comp} {state} (raw/components-computed.json)" + caveat(comp),
                            "description": desc}
                return
    except KeyError:
        pass


# ------------------------------------------------------------------- fonts
fam = SPEC["core"].setdefault("font", {}).setdefault("family", {})
for key, comp, desc in [
    ("display", "hero-h1", "The Headspace Apercu stack on the hero headline — the single family the whole marketing surface ships, weights 200/400/600/700."),
    ("body", "hero-lede", "The Headspace Apercu stack on body copy."),
    ("nav", "nav-category", "The stack on the top-nav labels."),
]:
    v = ts(comp, "default", "fontFamily")
    if v:
        fam[key] = {"value": v, "type": "fontFamily",
                    "source": f"computed fontFamily of {comp} default (raw/components-computed.json)" + caveat(comp),
                    "description": desc}
# Apercu Pro Mono if a mono reading exists anywhere (it is in the served @font-face list)
for comp, state in (("redeem-field", "default"), ("auth-email", "default"), ("checkout-field", "default")):
    v = ts(comp, state, "fontFamily")
    if v and "mono" in v.lower():
        fam["mono"] = {"value": v, "type": "fontFamily",
                       "source": f"computed fontFamily of {comp} {state} (raw/components-computed.json)",
                       "description": "Apercu Pro Mono, the monospace face in the site's font stack."}
        break

# ------------------------------------------------------------- type scale
scale = SPEC["core"].setdefault("font", {}).setdefault("size", {})
for key, comp, state, prop, desc in [
    ("display", "hero-h1", "default", "text-fontSize", "The hero headline."),
    ("h1-b2b", "org-h1", "default", "text-fontSize", "The B2B hero headline (a second large size if it differs)."),
    ("h2", "prose-h2", "default", "text-fontSize", "A marketing section heading."),
    ("h3", "prose-h3", "default", "text-fontSize", "A card heading."),
    ("body-lg", "hero-lede", "default", "text-fontSize", "The lede under the hero headline."),
    ("body", "prose-body", "default", "text-fontSize", "Running body text."),
    ("body-sm", "testimonial", "default", "text-fontSize", "Quote / smaller body text."),
    ("caption", "footer-link", "default", "text-fontSize", "Footer links and small print."),
    ("button", "nav-cta", "default", "text-fontSize", "Button labels."),
    ("nav", "nav-category", "default", "text-fontSize", "The top-nav category labels."),
]:
    put(scale, key, comp, state, prop, "dimension", desc)

weight = SPEC["core"].setdefault("font", {}).setdefault("weight", {})
for key, comp, state, desc in [
    ("display", "hero-h1", "default", "The headline weight (the family ships 200/400/600/700)."),
    ("body", "prose-body", "default", "Body text weight."),
    # keyed by role, not by an assumed weight: the card heading measures 400
    ("cardHeading", "prose-h3", "default", "The card-heading weight."),
    ("button", "nav-cta", "default", "Button-label weight."),
]:
    put(weight, key, comp, state, "text-fontWeight", "number", desc)

lh = SPEC["core"].setdefault("font", {}).setdefault("lineHeight", {})
for key, comp, state, desc in [
    ("display", "hero-h1", "default", "The hero headline line height."),
    ("heading", "prose-h2", "default", "The section-heading line height."),
    ("body", "prose-body", "default", "The body line height."),
]:
    put(lh, key, comp, state, "text-lineHeight", "dimension", desc)

# ------------------------------------------------------------- light palette
ink = SPEC["light"].setdefault("color", {}).setdefault("ink", {})
for key, comp, state, prop, desc in [
    ("primary", "hero-h1", "default", "color", "The near-black text of headings and body on the light ground."),
    ("muted", "hero-lede", "default", "color", "The secondary text colour under the hero."),
    ("nav", "nav-category", "default", "color", "The warm near-black of nav labels and links."),
    ("footer", "footer-link", "default", "color", "Footer link colour."),
]:
    put(ink, key, comp, state, prop, "color", desc)

surf = SPEC["light"].setdefault("color", {}).setdefault("surface", {})
for key, comp, state, prop, desc in [
    ("header", "nav-header", "default", "backgroundColor", "The header's ground."),
    ("field", "newsletter-field", "default", "backgroundColor", "An input field's ground."),
]:
    put(surf, key, comp, state, prop, "color", desc)
put_paint_node(surf, "page", "nav-header", "default", "css-15t8m5e", "The warm-grey wash the page/menu wrapper paints (the same #f9f4f2 the auth ground and the declared --2ndary-warm-grey-100/--grey-for-bg-adjacent tokens carry).")
put_paint_node(surf, "auth-card", "auth-card", "default", "bg-card", "The white the universal-login card paints.")
put_paint_node(surf, "footer-panel", "footer", "default", "css-1v3qhkq", "The dark panel band inside the footer.")

brand = SPEC["light"].setdefault("color", {}).setdefault("brand", {})
for key, comp, state, prop, desc in [
    ("blue", "hero-cta", "default", "backgroundColor", "The bright blue every primary CTA paints (the declared --secondary-blue)."),
    ("blue-hover", "hero-cta", "hover", "backgroundColor", "The deeper blue primary CTAs shift to on hover (the declared --primary-blue)."),
    ("on-blue", "hero-cta", "default", "color", "Text on the blue CTA."),
    ("orange", "org-cta", "hover", "backgroundColor", "Headspace's signature orange — it surfaces as the B2B CTA's hover fill (the declared --orange)."),
    ("yellow", "org-card", "default", "backgroundColor", "The Headspace yellow a B2B highlight card paints (the declared --yellow)."),
]:
    put(brand, key, comp, state, prop, "color", desc)

action = SPEC["light"].setdefault("color", {}).setdefault("action", {})
for key, comp, state, prop, desc in [
    ("secondary", "subscribe-button", "default", "backgroundColor", "The dark pill secondary CTAs paint (Subscribe, and the declared --primary-warm-grey-700)."),
    ("secondary-hover", "subscribe-button", "hover", "backgroundColor", "The near-black the dark pill shifts to on hover."),
    ("secondary-ink", "subscribe-button", "default", "color", "Text on the dark pill."),
    ("tertiary", "auth-sso", "default", "backgroundColor", "The quiet warm-grey button ground (the SSO button)."),
    ("tertiary-hover", "auth-sso", "hover", "backgroundColor", "The SSO button's hover ground."),
    ("link", "prose-link", "default", "color", "Inline link colour (dark, underlined on hover)."),
    ("link-hover", "footer-link", "hover", "color", "A link on hover."),
]:
    put(action, key, comp, state, prop, "color", desc)

accent = SPEC["light"].setdefault("color", {}).setdefault("accent", {})
for key, comp, state, prop, desc in [
    ("promo-ink", "nav-promo-strip", "default", "textStyle-color", "Text on the offer strip."),
    ("focus", "nav-category", "focus-visible", "outlineColor", "The 1px near-black keyboard focus ring the site's controls draw."),
]:
    put(accent, key, comp, state, prop, "color", desc)

hair = SPEC["light"].setdefault("color", {}).setdefault("line", {})
for key, comp, state, prop, desc in [
    ("field", "newsletter-field", "default", "borderTopColor", "An input's border."),
    ("redeem-field", "redeem-field", "default", "borderTopColor", "The redeem field's dark border."),
]:
    try:
        if st(comp, state).get("borderTopWidth", "0px") != "0px":
            put(hair, key, comp, state, prop, "color", desc)
    except KeyError:
        pass

# ------------------------------------------------------------- radii / shape
radii = SPEC["core"].setdefault("radius", {})
for key, comp, state, desc in [
    ("button", "hero-cta", "default", "The CTA pill radius (32px on the marketing pills)."),
    ("pill", "org-cta", "default", "The fully-round pill the B2B CTA draws (800px)."),
    ("field", "newsletter-field", "default", "An input's corner radius."),
    ("field-sm", "redeem-field", "default", "The redeem field's smaller radius."),
]:
    put(radii, key, comp, state, "borderTopLeftRadius", "dimension", desc)

# ------------------------------------------------------------- shadows
shadow = SPEC["core"].setdefault("shadow", {})
for key, comp, state, desc in [
    ("button", "hero-cta", "default", "The 2px soft drop every pill button carries."),
]:
    put(shadow, key, comp, state, "boxShadow", "shadow", desc)

# ------------------------------------------------------------- spacing readings
spacing = SPEC["core"].setdefault("spacing", {})
for key, comp, state, prop, desc in [
    ("button-x", "hero-cta", "default", "paddingLeft", "A pill button's horizontal padding."),
    ("button-y", "hero-cta", "default", "paddingTop", "A pill button's vertical padding."),
    ("header-x", "nav-header", "default", "paddingLeft", "The header's horizontal padding."),
    ("field-y", "newsletter-field", "default", "paddingTop", "An input's vertical padding."),
    ("field-x", "newsletter-field", "default", "paddingLeft", "An input's horizontal padding."),
    ("auth-card", "auth-card", "default", "paddingLeft", "The auth card's padding."),
]:
    put(spacing, key, comp, state, prop, "dimension", desc)

# ------------------------------------------------------------- layout readings
lay = SPEC["core"].setdefault("layout", {})
for page in ("home", "subscriptions", "meditation"):
    rec = LAYOUT.get(f"{page}@1440") or {}
    wides = [m for m in (rec.get("maxWidths") or []) if m.get("max")]
    if wides:
        wides.sort(key=lambda m: -parse_float(m["max"]))
        cont = wides[0]
        lay.setdefault("container", {"value": cont["max"], "type": "dimension",
                                     "source": f"widest constrained container on {page}@1440 (raw/layout.json)",
                                     "description": "The marketing content column's max width."})
        break
for w in ("1440", "390"):
    rec = LAYOUT.get(f"home@{w}") or {}
    hd = rec.get("header") or {}
    if hd.get("h"):
        lay[f"header-height-{w}"] = {"value": f"{hd['h']}px", "type": "dimension",
                                     "source": f"header bounding box on home@{w} (raw/layout.json)",
                                     "description": f"The header's painted height at {w}px wide."}

# ------------------------------------------------------------- motion
# raw/motion.json: pages -> each {groups: [{node, base:{transitions,animations},
# reduced:{...}}], summary}, plus a merged summary.behaviour.
mot = SPEC["core"].setdefault("motion", {})
durs, eases = [], []
for pg in (MOTION.get("pages") or {}).values():
    for g in pg.get("groups") or []:
        base = g.get("base") or {}
        for t in base.get("transitions") or []:
            if t.get("durationMs"):
                durs.append(t["durationMs"])
            if t.get("easing") and t["easing"] not in ("linear", "ease"):
                eases.append(t["easing"])
        for a in base.get("animations") or []:
            if a.get("durationMs"):
                durs.append(a["durationMs"])
if durs:
    for i, d in enumerate(sorted(set(durs))[:4]):
        mot[f"duration-{i+1}"] = {"value": f"{d}ms", "type": "duration",
                                  "source": "transition/animation duration measured on live components (raw/motion.json)",
                                  "description": "A motion duration the site uses."}
if eases:
    top = sorted(set(eases), key=lambda e: (-eases.count(e), e))[0]  # a tie goes to the first by name
    bez = re.fullmatch(r"cubic-bezier\(\s*([-\d.]+)\s*,\s*([-\d.]+)\s*,\s*([-\d.]+)\s*,\s*([-\d.]+)\s*\)", top)
    # DTCG cubicBezier values are the four numeric points, not the CSS string.
    mot["easing"] = {"value": [float(x) for x in bez.groups()] if bez else top,
                     "type": "cubicBezier" if bez else "other",
                     "source": "transition-timing-function measured on live components (raw/motion.json)",
                     "description": "The easing curve most components transition with."}
behaviour = (MOTION.get("summary") or {}).get("behaviour")
mot["reduced"] = {"value": behaviour or "not observed",
                  "type": "other",
                  "source": "prefers-reduced-motion probe (raw/motion.json)",
                  "description": "What the site changes under prefers-reduced-motion: reduce, as measured by the probe."}

if __name__ == "__main__":
  (RAW / "component-tokens.json").write_text(json.dumps(SPEC, indent=2) + "\n")
n = sum(len(v) for s in SPEC.values() for v in s.values()) if all(isinstance(v, dict) for s in SPEC.values() for v in s.values()) else 0
count = 0
def walk(o):
    global count
    for k, v in o.items():
        if isinstance(v, dict):
            if "value" in v: count += 1
            else: walk(v)
walk(SPEC)
print("component-tokens.json:", count, "leaves")
