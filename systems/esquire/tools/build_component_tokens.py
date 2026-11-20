#!/usr/bin/env python3
"""Write raw/component-tokens.json, the token spec build_tokens.py reads.

esquire.com is Hearst's FRE design-token site: its /api/styles.css bundle
declares ~4,300 custom properties — the --_palette/--_size/--_font
primitives, the --color-* semantic layer (palette ramps plus per-component
roles), the --type-* type styles, the --dim-* space/layout scale and a large
--comp-* component layer. Most leaves below are var references resolved on
the live probe in raw/css-vars.json; component dimensions and state tracks
are measured computed styles from raw/components-computed.json.

What was measured (desktop 1440x900 unless noted):

  #ff3a30   the brand red — the utility strip, the Subscribe pill, the Join
            and Sign Up buttons, badge/chip accents
  #121212   the ink on every heading, nav label and body text
  #3b3b3b   the muted meta/byline/readtime text
  #575757   the subtler secondary text (deks, form placeholders, excluded
            list items)
  #ffffff   the page field — every captured surface paints white
  #f5f6f8   the pale panel behind newsletter blocks and meta boxes
  #bdbdbd   the hairline divider; #ededed the softer meta border

  Typography: Lausanne everywhere for UI (nav 16px, headings 32px, card
  titles 18-40px), PlayFair for serif display (hero/section titles to 64px),
  Lora for article body (18px), "SF Pro" as the mac-default secondary
  (offers headings 32px/700), Charter and Inter declared in the family
  stacks.

The page paints ONE theme: white editorial surfaces with the red accent.
There is no dark class/theme switch; the export keeps `dark` empty.
"""
import json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
V = json.loads((RAW / "css-vars.json").read_text())
RL = V.get("resolved", {}).get("light", {})
C = json.loads((RAW / "components-computed.json").read_text())["components"]
R = {n: (v.get("value", v.get("raw")) if isinstance(v, dict) else v) for n, v in RL.items()}


def var(name, ty="color", **kw):
    d = {"var": name, "type": ty}
    d.update(kw)
    return d


SPEC = {"_about": (
    "The token tree build_tokens.py turns into tokens.json. "
    "esquire.com is a single-theme Hearst magazine on the FRE design-token "
    "layer: a white editorial field with the #ff3a30 brand red (utility "
    "strip, Subscribe pill, Join/Sign-Up buttons) over Lausanne UI, "
    "PlayFair display and Lora body. Design values are the resolved FRE "
    "custom properties (--_palette/--_size/--_font primitives, --color-* "
    "semantics, --type-* styles, --dim-* scale); component dimensions and "
    "state tracks are measured computed styles."),
    "core": {}, "light": {}, "dark": {}, "component": {}}


def st(comp, state):
    return C[comp]["states"][state]["style"]


def rc(comp, state, key):
    return C[comp]["states"][state]["rect"][key]


def ts(comp, state, prop):
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


def lit(value, ty, src, desc):
    return {"value": norm_color(value) if ty == "color" else value, "type": ty, "source": src, "description": desc}


def has(n):
    return n in R


def ref(name, ty, desc, **kw):
    """A var leaf only when the resolved probe actually holds the name."""
    if not has(name):
        return None
    return var(name, ty, source=f"css-var {name} resolved (raw/css-vars.json)", description=desc, **kw)


def put(tree, path, leaf):
    """Place a leaf; a second leaf at the same path stops the build instead of silently replacing
    the first (two rows naming one token would otherwise lose one reading without a trace)."""
    if leaf is None:
        return
    node = tree
    for k in path[:-1]:
        node = node.setdefault(k, {})
    if path[-1] in node:
        raise SystemExit(f"{'.'.join(path)}: two rows write this token; give one of them its own path")
    node[path[-1]] = leaf


# ------------------------------------------------------------------- fonts

fam = SPEC["core"].setdefault("font", {}).setdefault("family", {})
put(fam, ("sans",), ref("--type-font-family-primary", "fontFamily",
    "Lausanne — every UI string, button, label, nav, headings and card titles."))
put(fam, ("display",), ref("--type-font-family-serif-primary", "fontFamily",
    "PlayFair — the serif display face: cover headlines, plan names, section titles."))
put(fam, ("content",), ref("--type-font-family-serif-secondary", "fontFamily",
    "Lora — the article body face."))
put(fam, ("secondary",), ref("--type-font-family-sans-serif-secondary", "fontFamily",
    '"SF Pro" mac-default stack — offers-page headings and utility copy.'))
put(fam, ("windows",), ref("--_font-family-windows", "fontFamily",
    '"Segoe UI" fallback stack declared for Windows clients.'))

weights = SPEC["core"].setdefault("font", {}).setdefault("weight", {})
for n in sorted(R):
    if n.startswith("--_font-weight-"):
        put(weights, (n[len("--_font-weight-"):].replace("_", "-"),),
            ref(n, "fontWeight", f"FRE weight step {n}."))

# ---------------------------------------------------------- primitive ramps

pal = SPEC["core"].setdefault("palette", {})
for n in sorted(R):
    if n.startswith("--_palette-"):
        leaf = n[len("--_palette-"):]
        hue, _, step = leaf.partition("-")
        put(pal, (hue, step), ref(n, "color", f"FRE palette primitive {n}."))

size = SPEC["core"].setdefault("size", {})
for n in sorted(R):
    if n.startswith("--_size-"):
        put(size, (n[len("--_size-"):].replace("_", "-"),),
            ref(n, "dimension", f"FRE sizing primitive {n}."))

fs = SPEC["core"].setdefault("font", {}).setdefault("size", {})
for n in sorted(R):
    if n.startswith("--_font-size-"):
        put(fs, (n[len("--_font-size-"):].replace("_", "-"),),
            ref(n, "dimension", f"FRE type-size step {n}."))

lh = SPEC["core"].setdefault("font", {}).setdefault("lineHeight", {})
for n in sorted(R):
    if n.startswith("--_font-line-height-"):
        put(lh, (n[len("--_font-line-height-"):].replace("_", "-"),),
            ref(n, "dimension", f"FRE line-height step {n}."))

sp = SPEC["core"].setdefault("space", {})
put(sp, ("base",), ref("--spacing", "dimension",
    "The 4px Tailwind base unit the --dim-space scale multiplies."))
for n in sorted(R):
    if n.startswith("--dim-space-"):
        put(sp, (n[len("--dim-space-"):],), ref(n, "dimension", f"FRE space step {n}."))

lay = SPEC["core"].setdefault("layout", {})
for n in sorted(R):
    if n.startswith("--dim-layout-") and re.fullmatch(r"--dim-layout-(\dx?l|\dx?s|xl|lg|md|sm|xs)", n):
        put(lay, ("breakpoint", n[len("--dim-layout-"):]), ref(n, "dimension", f"FRE layout step {n}."))
    if n.startswith("--dim-layout-elevation-"):
        # The z-stacking roles go under layout.z with the --_z-level-* ladder;
        # the name must not contain "elevation" or the DESIGN.md shadow table
        # would list stacking levels (e.g. 8000000) as box-shadows.
        put(lay, ("z", n[len("--dim-layout-elevation-"):]), ref(n, "number", f"FRE stacking level {n}."))
    if n.startswith("--dim-layout-grid-gap-"):
        put(lay, ("grid-gap", n[len("--dim-layout-grid-gap-"):]), ref(n, "dimension", f"FRE grid gap {n}."))

for n in sorted(R):
    if n.startswith("--_z-"):
        put(lay, ("z", n[len("--_z-"):]), ref(n, "number", f"FRE z-level {n}."))

bw = SPEC["core"].setdefault("borderWidth", {})
for n in sorted(R):
    if n.startswith("--_border-width-"):
        put(bw, (n[len("--_border-width-"):],), ref(n, "dimension", f"FRE border width {n}."))

op = SPEC["core"].setdefault("opacity", {})
for n in sorted(R):
    if n.startswith("--_opacity-"):
        put(op, (n[len("--_opacity-"):],), ref(n, "number", f"FRE opacity step {n}."))

rad = SPEC["core"].setdefault("radius", {})
for n, key, desc in [
    ("--comp-btn-dim-radius-square", "square", "The 0px square radius."),
    ("--comp-btn-dim-radius-sm", "sm", "The 4px small radius (form fields, FAQ rows)."),
    ("--comp-btn-dim-radius-default", "pill", "The 1024px pill radius on every button (Subscribe, Join, Sign Up, See More)."),
]:
    put(rad, (key,), ref(n, "dimension", desc))
for n in sorted(R):
    if re.fullmatch(r"--comp-(input|card|badge|chip|collapsible|modal|popover).*radius.*", n):
        leaf = re.sub(r"^--comp-|-mobile$|-desktop$|-tablet$|-laptop$", "", n).strip("-")
        put(rad, ("component", leaf), ref(n, "dimension", f"FRE component radius {n}."))

# ------------------------------------------------------------- typography

# FRE declares each style as --type-<stem>-<prop>-<bp>: size, line-height and
# letter-spacing per breakpoint (mobile is the base; desktop, and for a few
# styles laptop/tablet), while family, weight, style and txt-case are declared
# only at the base (mobile) breakpoint. The export composes the parts into
# DTCG typography tokens — one composite per stem per declared breakpoint —
# under core.typography, the layout the DESIGN.md exporter reads.
typegrp = SPEC["core"].setdefault("typography", {})
TYPE_PROP = {"size": "fontSize", "line-height": "lineHeight", "letter-spacing": "letterSpacing",
             "family": "fontFamily", "weight": "fontWeight", "style": "fontStyle", "txt-case": "textTransform"}
TYPE_DESC = {
    "nav-header-xs": "The 13px utility-strip/nav meta style.",
    "nav-linktxt-md": "The 16px category-nav link style.",
    "body": "The Lora article body style.",
    "body-blockquote": "The blockquote body style.",
    "desc-lede": "The 20px lede/standfirst style.",
    "title-standard": "The standard card title style.",
    "headline-prominent": "The 24px prominent headline.",
    "headline-hero": "The 48px hero headline.",
    "headline-lede": "The 56px lede headline (negative tracking).",
    "header-hero-topic": "The 64px hero topic display.",
    "headline-body-h2": "The 36px in-article h2.",
    "headline-body-h3": "The 30px in-article h3.",
    "header-standard": "The section-front header style.",
    "eyebrow-standard": "The small uppercase eyebrow.",
    "meta-author": "The byline/meta style.",
    "meta-readtime": "The read-time meta style.",
    "meta-timestamp-md": "The timestamp meta style.",
    "legal-fine-print": "The footer legal style.",
    "legal-terms": "The legal terms style.",
    "offer-price-current": "The plan-card current price style.",
    "offer-price-duration": "The plan-card price duration style.",
    "offer-price-strikethrough": "The plan-card struck list-price style.",
    "list-item": "The plan-card perk list style.",
    "form-label": "The form label style.",
    "pagination": "The pagination number style.",
}
# stem -> breakpoint -> {prop -> var name}, discovered from the resolved vars.
TYPE_STEMS = {}
for n in sorted(R):
    m = re.fullmatch(r"--type-(.+)-(size|line-height|letter-spacing|family|weight|style|txt-case)-(desktop|mobile|tablet|laptop)", n)
    if m:
        TYPE_STEMS.setdefault(m.group(1), {}).setdefault(m.group(3), {})[m.group(2)] = n

for stem in sorted(TYPE_STEMS):
    bps = TYPE_STEMS[stem]
    desc = TYPE_DESC.get(stem, f"The --type-{stem} style.")
    for bp in sorted(bps):
        val, used = {}, []
        for prop in ("size", "line-height", "letter-spacing"):
            n = bps[bp].get(prop)
            if n:
                val[TYPE_PROP[prop]] = R[n]
                used.append(n)
        # family/weight/style/case live on the base (mobile) declaration only.
        base = bps.get("mobile", {})
        for prop in ("family", "weight", "style", "txt-case"):
            n = bps[bp].get(prop) or base.get(prop)
            if n:
                v = R[n]
                val[TYPE_PROP[prop]] = int(v) if prop == "weight" and re.fullmatch(r"\d+", str(v)) else v
                used.append(n)
        if not val:
            continue
        put(typegrp, (stem, bp), {
            "$value": val, "$type": "typography",
            "$extensions": {"source": "; ".join(f"css-var {n}" for n in used) + " resolved (raw/css-vars.json)"},
            "$description": desc + (f" ({bp} breakpoint; family/weight from the base mobile declaration)" if bp != "mobile" else " (mobile base breakpoint)"),
        })

# ----------------------------------------------------- semantic light roles

sem = SPEC["light"]

def grab(group, key, names, desc):
    for n in names:
        if has(n):
            put(sem, (group, key), ref(n, "color", desc))
            return n
    return None

# brand + text
grab("brand", "red", ["--color-btn-primary-solid-bg", "--color-badge-bg-primary"],
     "The #ff3a30 brand red — utility strip, Subscribe pill, Join and Sign-Up buttons, badges.")
grab("brand", "red-border", ["--color-btn-primary-outlined-border"],
     "The #ff3a30 border on the outlined/ghost actions (See More, gift CTA).")
grab("text", "ink", ["--color-article-body-txt", "--color-nav-header-txt"],
     "The #121212 ink on every heading and body string.")
grab("text", "muted", ["--color-meta-author-txt"],
     "The #3b3b3b muted meta/byline/readtime text.")
grab("text", "subtle", ["--color-form-field-message-txt", "--color-list-item-txt-excluded"],
     "The #575757 secondary text (deks, placeholders, excluded perks).")
grab("text", "disabled", ["--color-form-input-txt-placeholder", "--color-form-input-icon-placeholder"],
     "The #757575 placeholder/quiet icon grey.")
grab("text", "inverse", ["--color-btn-primary-solid-txt", "--color-nav-utility-txt"],
     "White text on the red fills.")
grab("text", "on-dark-hover", ["--color-btn-neutral-inverse-solid-txt"],
     "Text the inverse buttons paint.")

# backgrounds
grab("background", "page", ["--color-nav-megamenu-bg", "--color-modal-bg-primary"],
     "The #fff page field — body paints the default canvas white; verified against the megamenu, modal and footer surfaces.")
grab("background", "panel", ["--color-meta-bg", "--color-nwsltr-bg"],
     "The #f5f6f8 pale panel behind newsletter blocks and meta boxes.")
grab("background", "footer", ["--color-nav-footer-bg"],
     "The white footer field.")
grab("background", "scrim", ["--color-overlay-bg"],
     "The rgba(18,18,18,.72) overlay behind modal/drawer surfaces.")
grab("background", "error-field", ["--color-form-input-bg-error"],
     "The #feecec error wash on a form field.")

# borders
grab("border", "divider", ["--color-divider-border"],
     "The #bdbdbd hairline divider.")
grab("border", "soft", ["--color-meta-border"],
     "The #ededed soft border around meta boxes.")
grab("border", "field", ["--color-form-input-search-border-placeholder"],
     "The #d6d6d6 resting field border.")
grab("border", "field-focus", ["--color-form-input-border-active", "--color-form-input-search-border-value"],
     "The #121212 active field border.")
grab("border", "field-rest", ["--color-form-input-border-placeholder"],
     "The #757575 resting non-search field border.")
grab("border", "error", ["--color-form-input-border-error"],
     "The #a81a1f error field border.")
grab("border", "megamenu", ["--color-nav-megamenu-border"],
     "The #ffaca8 underline the megamenu paints; #3b3b3b on hover.")

# nav
grab("nav", "utility-txt", ["--color-nav-utility-txt", "--color-header-list-txt"],
     "The utility-strip text colour.")
grab("nav", "header-txt", ["--color-header-list-txt"],
     "The nav header list text.")
grab("nav", "dropdown-badge", ["--color-nav-dropdown-badge-txt"],
     "The #a80800 dropdown badge text.")
grab("nav", "footer-icon", ["--color-nav-footer-social-icon"],
     "The footer social icon colour.")
grab("nav", "footer-icon-hover", ["--color-nav-footer-social-icon-hover"],
     "The #3b3b3b footer icon hover.")

# buttons — the whole state triplet where declared
btn = sem.setdefault("button", {})
for kind, prefix, desc in [
    ("primary", "--color-btn-primary-solid-", "The filled red primary (Subscribe, Join, Sign Up)."),
    ("primary-outlined", "--color-btn-primary-outlined-", "The red ghost/outline button (See More, gift CTA)."),
    ("secondary", "--color-btn-secondary-solid-", "The secondary solid button."),
    ("neutral", "--color-btn-neutral-solid-", "The neutral solid button."),
    ("neutral-inverse", "--color-btn-neutral-inverse-solid-", "The inverse neutral button (white on dark)."),
]:
    for role in ("bg", "border", "txt", "icon"):
        for st_ in ("", "-hover", "-active"):
            n = f"{prefix}{role}{st_}"
            key = role + ("_" + st_.strip("-") if st_ else "")
            put(btn, (kind, key), ref(n, "color", f"{desc} ({key})."))

# links, badges, chips, meta, offers, forms, list states
grab("link", "txt", ["--color-link-txt"], "The #121212 inline link; #3b3b3b on hover.")
grab("link", "hover", ["--color-link-txt-hover"], "The #3b3b3b link hover.")
grab("badge", "primary-bg", ["--color-badge-bg-primary"], "The #ff3a30 badge fill.")
grab("badge", "primary-border", ["--color-badge-border-primary"], "The #ff3a30 badge border.")
grab("chip", "primary-border", ["--color-chip-border-primary"], "The #ff3a30 chip border.")
grab("chip", "primary-selected-bg", ["--color-chip-bg-primary-selected"], "The selected chip fill.")
grab("eyebrow", "txt", ["--color-eyebrow-txt"], "The #121212 eyebrow text.")
grab("meta", "timestamp", ["--color-meta-timestamp-txt"], "The #3b3b3b timestamp/readtime text.")
grab("offer", "price", ["--color-offer-price-current"], "The current plan price.")
grab("offer", "strikethrough", ["--color-offer-price-strikethrough"], "The #cc2828 struck-through list price.")
grab("list", "included", ["--color-list-item-icon-included"], "The #088153 green check on included perks.")
grab("list", "included-txt", ["--color-list-item-txt-included"], "The #121212 included perk text.")
grab("list", "excluded", ["--color-list-item-icon-excluded", "--color-list-item-txt-excluded"], "The #575757 excluded perk text/icon.")
grab("pullquote", "txt", ["--color-pullquote-txt"], "The pull-quote text.")
grab("hr", "bg", ["--color-hr-bg"], "The #121212 horizontal rule.")
grab("accordion", "txt", ["--color-accordion-header-txt", "--color-accordion-txt"], "The FAQ accordion header text.")

# ------------------------------------------------------------- elevation

# FRE splits each elevation level into --dim-elevation-shadow-<level>-{position-x,
# position-y, blur, spread, color}; exporting the parts as separate leaves made
# DESIGN.md list lone lengths (4px) as complete shadows. The export composes the
# parts into DTCG shadow tokens, one layer each, so the shadow table reads a
# whole box-shadow. The none and card levels are all-zero over a transparent
# colour: card is kept as "none" so the tokens record that cards paint no
# shadow, and none is dropped as a no-op declaration.
def _px(v):
    v = str(v if v is not None else "0").strip()
    return v + "px" if re.fullmatch(r"-?\d+(\.\d+)?", v) else v

sh = SPEC["core"].setdefault("shadow", {})
for lvl in ("sm", "md", "lg"):
    part = {p: R.get(f"--dim-elevation-shadow-{lvl}-{p}")
            for p in ("position-x", "position-y", "blur", "spread", "color")}
    if not all(v is not None for v in part.values()):
        continue
    layer = {"offsetX": _px(part["position-x"]), "offsetY": _px(part["position-y"]),
             "blur": _px(part["blur"]), "spread": _px(part["spread"]), "color": str(part["color"])}
    put(sh, (lvl,), {
        "$value": [layer], "$type": "shadow",
        "$extensions": {"source": f"css-var --dim-elevation-shadow-{lvl}-position-x/-position-y/-blur/-spread/-color resolved (raw/css-vars.json)"},
        "$description": f"The {lvl} elevation shadow ({layer['offsetX']} {layer['offsetY']} {layer['blur']} {layer['spread']} {layer['color']}) from FRE's --dim-elevation-shadow-{lvl}-* parts."})
put(sh, ("card",), lit("none", "other", "css-var --comp-card-dim-shadow-* resolved (raw/css-vars.json)",
    "FRE declares the card shadow at 0 offsets over a transparent colour: cards paint no shadow."))

# ------------------------------------------------------------------ motion

mo = SPEC["core"].setdefault("motion", {})
put(mo, ("duration",), ref("--default-transition-duration", "duration", "The 150ms default transition duration."))
put(mo, ("ease-in-out",), ref("--ease-in-out", "cubicBezier", "cubic-bezier(.4,0,.2,1)."))
put(mo, ("ease-out",), ref("--ease-out", "cubicBezier", "cubic-bezier(0,0,.2,1)."))

# ------------------------------------------------------------- components

comp = SPEC["component"]
COMP_DIMS = [
    ("nav-height", "nav", "default", "h", "The ~155px desktop top chrome (utility strip + main bar + category strip)."),
    ("nav-utility-height", "nav-utility", "default", "h", "The 32px red utility strip."),
    ("megamenu-height", "megamenu", "default", "h", "The ~53px category strip."),
    ("logo-width", "nav-logo", "default", "w", "The ~296px Esquire wordmark."),
    ("search-input-width", "nav-search", "default", "w", "The ~211px header search input."),
    ("search-input-height", "nav-search", "default", "h", "The ~26px header search input."),
    ("signin-width", "nav-signin", "default", "w", "The Sign In link box."),
    ("subscribe-height", "nav-subscribe", "default", "h", "The Subscribe pill height."),
    ("more-width", "more-btn", "default", "w", "The ~87px More toggle."),
    ("search-field-width", "search-field", "default", "w", "The ~1115px results-page search field."),
    ("search-field-height", "search-field", "default", "h", "The 48px results-page search field."),
    ("search-btn-size", "search-btn", "default", "w", "The ~46px round search submit."),
    ("see-more-height", "search-more", "default", "h", "The ~38px See More ghost button."),
    ("story-thumb-width", "story-thumb", "default", "w", "The story-list thumbnail width."),
    ("section-h2-size", "section-h2", "default", "h", "The 41px-tall section heading box (32px Lausanne)."),
    ("hero-headline-width", "hero-story", "default", "w", "The ~628px cover-hero headline box."),
    ("newsletter-width", "newsletter-block", "default", "w", "The ~846px newsletter band."),
    ("newsletter-input-width", "newsletter-input", "default", "w", "The newsletter email field."),
    ("signup-width", "newsletter-signup", "default", "w", "The ~255px Sign Up button."),
    ("footer-height", "footer", "default", "h", "The footer block height."),
    ("pagination-width", "pagination", "default", "w", "The ~192px pagination strip."),
    ("article-h1-width", "art-h1", "default", "w", "The article headline measure."),
    ("article-para-width", "art-para", "default", "w", "The article text column (~628-680px)."),
    ("plan-card-width", "plan-card", "default", "w", "The ~390px plan card."),
    ("plan-join-width", "plan-join", "default", "w", "The ~318px Join button."),
    ("faq-row-height", "faq-header", "default", "h", "The 56px FAQ accordion row."),
    ("faq-row-width", "faq-header", "default", "w", "The ~1200px FAQ row."),
    ("gift-width", "gift-cta", "default", "w", "The ~322px gift-subscription CTA."),
    ("m-nav-height", "m-nav", "default", "h", "The ~154px phone top chrome."),
    ("m-logo-width", "m-logo", "default", "w", "The phone wordmark."),
    ("m-hamburger-size", "m-hamburger", "default", "w", "The hamburger hit box."),
    ("m-drawer-width", "m-drawer", "default", "w", "The phone side-panel width."),
]
for name, cname, state, prop, desc in COMP_DIMS:
    try:
        s_ = C[cname]["states"][state]
        v = s_["rect"][prop] if prop in ("w", "h") else s_["style"][prop]
        if v and v not in ("0px", "auto", "rgba(0, 0, 0, 0)", 0):
            comp[name] = lit(("%gpx" % v) if isinstance(v, (int, float)) else v, "dimension",
                f"computed {prop} of {cname} {state} (raw/components-computed.json)", desc)
    except KeyError:
        pass

# measured state moves on the interactive controls
for name, cname, desc in [
    ("subscribe-pill-track", "nav-subscribe",
     "Subscribe pill: #ff3a30 fill + #121212 text at rest; hover inverts to a white fill keeping the red border; pressed paints a #fff0f0 pale-red wash; focus shows the browser outline."),
    ("join-track", "plan-join",
     "Join button: #ff3a30 fill + black text at rest; hover and pressed invert to a white fill keeping the red border; focus shows a dotted outline."),
    ("signup-track", "newsletter-signup",
     "Newsletter Sign Up: #ff3a30 fill + #121212 text at rest; hover inverts to a white fill; pressed paints a #fff0f0 pale-red wash."),
    ("see-more-track", "search-more",
     "See More ghost: white fill, #ff3a30 text and a #121212 border at rest; hover/pressed paint a 4-8% dark grey wash — it never fills red."),
    ("nav-link-track", "nav-link",
     "Category link: #121212 in every state — no colour or decoration change on hover; focus shows the browser outline."),
    ("faq-track", "faq-header",
     "FAQ header: a transparent row over the white page in every state; the opened state was reached by its own toggle."),
    ("more-track", "more-btn",
     "More toggle: text button at rest, a 16% red wash on press; the opened state drops the overflow panel."),
]:
    try:
        states = {s2: {p: C[cname]["states"][s2]["style"][p] for p in ("backgroundColor", "color", "transform", "outlineStyle", "borderTopColor") if C[cname]["states"][s2]["style"].get(p)}
                  for s2 in ("default", "hover", "pressed", "focus-visible", "opened")
                  if s2 in C[cname]["states"] and C[cname]["states"][s2].get("style")}
        comp.setdefault("state-track", {})[name] = {
            "type": "other",
            "value": states,
            "source": f"computed styles of {cname} across states (raw/components-computed.json)",
            "description": desc}
    except KeyError:
        pass

# the shared focus outline
for cname in ("nav-link", "nav-subscribe", "plan-join", "faq-header"):
    try:
        s = st(cname, "focus-visible")
        if s.get("outlineStyle") and s["outlineStyle"] != "none":
            comp["focus-ring"] = lit(
                f"{s['outlineWidth']} {s['outlineStyle']} {s['outlineColor']} offset {s.get('outlineOffset','')}".strip(),
                "other",
                f"computed outline of {cname} focus-visible (raw/components-computed.json)",
                "The painted focus indicator.")
            break
    except KeyError:
        continue

(RAW / "component-tokens.json").write_text(json.dumps(SPEC, indent=1, ensure_ascii=False) + "\n")


def count(d):
    if not isinstance(d, dict):
        return 1
    if "var" in d or "value" in d or "$value" in d:
        return 1
    return sum(count(v) for v in d.values())


print("component-tokens.json:", {k: count(v) for k, v in SPEC.items() if isinstance(v, dict)})
