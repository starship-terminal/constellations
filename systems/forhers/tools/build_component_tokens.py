#!/usr/bin/env python3
"""Write raw/component-tokens.json, the token spec build_tokens.py reads.

forhers.com exposes almost no named token layer: the marketing stack's
styled-components sheets inline every value and keep custom properties only
for the fluid-type machinery (--base-font-size, --scale, the breakpoint
redeclarations), while the /shop stack's archived bundle declares the
--unit-u*, --spacing-s*, --grid-*, --*Height and --promoHeight* scales this
file exports under core.space and core.layout. Everything else is measured:
the palette is harvested from the archived inline sheets' literal colours,
the type styles and component dimensions are computed styles in
raw/components-computed.json.

www.forhers.com answers every automated request from this network with a
Cloudflare managed challenge, so every value is resolved from the Wayback
snapshots served locally; the sheet census cites declaration counts across
those archived inline sheets (the sheets index in raw/css-vars.json).

What the capture shows (desktop 1440x900 unless noted):

  rgba(0,0,0,.89)   the near-black ink — body copy, nav, footer
  rgba(0,0,0,.65)   secondary text — prose body, privacy notes
  rgba(0,0,0,.44)   the muted step — bylines and meta
  rgba(0,0,0,.37)   the faint step — "Read more"
  rgba(0,0,0,.12/.06) hairlines and hover wells (Log in hover, topic chips,
                    footer social wells, the disabled button)
  #ffffff           the page field
  #e8eae8           the footer slab; #f0f0f0/#efefef the wash surfaces
  #e4eee6/#f2f9f4/#f5faf6  the sage surfaces; #faf8f2/#f4f1e6 the cream
  #338585           the Hers teal (103 declarations across the sheets) with
                    a full ramp #13262e .. #9cccbc
  #d5ff5d           the promo lime; #c5ed82/#b6dd64 the softer limes (the
                    BMI Calculate submit paints #b6dd64)
  #000000           the primary action pill (mobile sticky CTA)
  #0077ab           the text-link blue (drug index links)
  #8a3a34/#451310/#ff7350 the clay/terracotta ramp; #ff7350 the alert
  Type: 'CareSans' display serif-feel (fluid headings, letter-spacing
  -0.0625em) and 'sofia-pro/SofiaProWeb' UI sans; IvarSoft faces are
  declared but no SSR rule applies them.

The page paints ONE theme — light surfaces, near-black ink, teal and lime
accents. There is no dark hook, so the export keeps `dark` empty.
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
    "The token tree build_tokens.py turns into tokens.json. forhers.com has no named token layer "
    "on the marketing stack: core.space and core.layout export the /shop bundle's --unit-u*/"
    "--spacing-s*/--grid-*/--*Height scales, core.palette harvests the literal colours the "
    "archived inline sheets declare (ink on white, sage and cream surfaces, the #338585 teal "
    "ramp, lime and clay accents), core.typography and light.component are computed styles "
    "measured on the same archived pages. core.font names the measured faces: sofia-pro/"
    "SofiaProWeb UI sans and the CareSans display face."),
    "core": {}, "light": {}, "dark": {}, "component": {}}


def st(comp, state):
    return C[comp]["states"][state]["style"]


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
        if len(h) == 8:
            a = int(h[6:8], 16) / 255
            return "#" + h[:6] if a == 1 else f"rgba({int(h[0:2], 16)}, {int(h[2:4], 16)}, {int(h[4:6], 16)}, {'%g' % a})"
        return "#" + h[:6]
    m = re.fullmatch(r"rgba?\(([\d.]+),\s*([\d.]+),\s*([\d.]+)(?:,\s*([\d.]+))?\)", v)
    if m:
        r, g, b, a = m.groups()
        if a is None or float(a) >= 1:
            return "#%02x%02x%02x" % (int(float(r)), int(float(g)), int(float(b)))
        return f"rgba({int(float(r))}, {int(float(g))}, {int(float(b))}, {'%g' % float(a)})"
    return v


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
    if leaf is None:
        return
    node = tree
    for k in path[:-1]:
        node = node.setdefault(k, {})
    node[path[-1]] = leaf


# ------------------------------------------------------------------- fonts
# Measured fontFamily stacks (raw/components-computed.json). IvarSoft is
# @font-face-declared (Regular + Italic, unicode-range subsets, font-display:
# swap) but no SSR rule applies it — recorded as declared-only.

fam = SPEC["core"].setdefault("font", {}).setdefault("family", {})
def computed_text(comp, prop, state="default"):
    """A computed style off comp in raw/components-computed.json (the element's own style);
    raises when it is missing."""
    v = (C[comp]["states"][state].get("style") or {}).get(prop)
    if not v:
        raise KeyError(f"{comp} {state}: no {prop} reading")
    return v


put(fam, ("sans",), lit(computed_text("article-card", "fontFamily"), "fontFamily",
    "computed fontFamily of article-card default (raw/components-computed.json); blog-topic and the other "
    "blog/prose components match (nav-link and footer measure CareSans)",
    "The UI sans — nav, footer, blog/prose, forms and the /shop stack."))
put(fam, ("display",), lit("CareSans, Helvetica, Arial, sans-serif", "fontFamily",
    "computed fontFamily of hero-heading (raw/components-computed.json)",
    "The marketing display face (the soft-serif brand face): hero and card headlines, "
    "CTAs and prices. Fluid-sized via --scale, letter-spacing -0.0625em."))
put(fam, ("serif",), lit("IvarSoft", "fontFamily",
    "@font-face declarations in the archived inline sheets (raw/css-vars.json fonts)",
    "Declared faces only: Regular and Italic, unicode-range subsets, font-display: swap. "
    "No SSR rule applies it — the marketing display face is CareSans."))

# ------------------------------------------------------------- typography
# One composite per measured role (raw/components-computed.json textStyle,
# desktop 1440). The marketing faces are fluid: font-size = base * --scale
# where --scale is a media-query staircase between 360px and 1392px wide, so
# the px values are the 1440 readings.

typegrp = SPEC["core"].setdefault("typography", {})


def type_tok(comp, state="default"):
    s = C[comp]["states"][state]
    t = s.get("textStyle") or {}
    st_ = s.get("style") or {}
    def g(p):
        return t.get(p) or st_.get(p)
    return {
        "fontFamily": g("fontFamily"),
        "fontSize": g("fontSize"),
        "lineHeight": g("lineHeight"),
        "fontWeight": int(round(float(g("fontWeight") or 400))),
        **({"letterSpacing": g("letterSpacing")} if g("letterSpacing") and g("letterSpacing") != "normal" else {}),
    }


for key, comp, desc in [
    ("display", "hero-heading",
     "The home hero headline — CareSans at its fluid max (57px at 1440, weight 410, "
     "letter-spacing -0.0625em, line-height 1). Base size 40 scaled by --scale."),
    ("display-page", "page-heading",
     "The category-page H1 (weight-loss, hair-loss, …) — CareSans, about 53px at 1440, weight 410."),
    ("title", "article-title",
     "The editorial title — blog article H1 and the lead-capture headline, sofia-pro 62px."),
    ("card-title", "product-card",
     "Card and product names — CareSans 28px/31.5 at weight 460."),
    ("dek", "page-dek",
     "The CareSans dek under a page heading — 18.5px."),
    ("body", "prose-body",
     "The default reading size — sofia-pro 20px/28. The article paragraph reading was the wrong element and is not published."),
    ("body-comfortable", "prose-body",
     "The wider-measure prose body — sofia-pro 20px/28 at the muted ink."),
    ("small", "disclaimer",
     "The small print — disclaimers and helper text, sofia-pro 14px/20."),
    ("micro", "byline",
     "Bylines, captions and footer fine print — sofia-pro 12px."),
    ("label", "login-button",
     "Compact UI labels (Log in, menu) — sofia-pro 12px/12 at weight 600."),
    ("button", "region-cta",
     "Button labels — sofia-pro 16px at weight 500."),
    ("chip", "blog-topic",
     "Topic chip labels — sofia-pro 14px/19.6 at weight 500."),
    ("drug-index", "drug-link",
     "The A-Z drug index links — sofia-pro 29px, link blue."),
]:
    try:
        val = type_tok(comp)
    except KeyError:
        continue
    put(typegrp, (key,), {
        "$value": val, "$type": "typography",
        "$extensions": {"source": f"computed text style of {comp} default (raw/components-computed.json)"},
        "$description": desc})

# --------------------------------------------------------------- spacing
# The /shop bundle's scales (raw/css-vars.json resolved): --unit-u* is the
# 18-step element scale (3..78px), --spacing-s* the 4-step section rhythm.

sp = SPEC["core"].setdefault("space", {})
usp = sp.setdefault("unit", {})
for n in sorted(R):
    if re.fullmatch(r"--unit-u\d+", n):
        put(usp, (n[len("--unit-"):],), ref(n, "dimension", f"Element spacing step {n}."))
ssp = sp.setdefault("section", {})
for n in sorted(R):
    if re.fullmatch(r"--spacing-s\d+", n):
        put(ssp, (n[len("--spacing-"):],), ref(n, "dimension", f"Section spacing step {n} — vertical rhythm between modules."))

# ----------------------------------------------------------------- layout
# The /shop grid variables plus the chrome heights both stacks declare.
# --column-margin/--grid-max-width/--grid-column-width are declared as calc()
# expressions; the value here is the arithmetic resolved at the captured width.

lay = SPEC["core"].setdefault("layout", {})
grid = lay.setdefault("grid", {})
put(grid, ("column-count",), ref("--grid-column-count", "number", "The 12-column content grid."))
put(grid, ("gap",), ref("--grid-gap", "dimension", "The grid gutter (declared as the unitless 14; px)."))
put(grid, ("max-width",), lit("1251px", "dimension",
    "css-var --grid-max-width declared calc(1266 - 15), resolved arithmetically (raw/css-vars.json)",
    "The grid's max width — the 1266 page shell minus the 15px scrollbar."))
put(grid, ("column-width",), lit("86.75px", "dimension",
    "css-var --grid-column-width declared calc(((1266 - 15) - (14 * 11) - (14 * 4)) / 12), resolved arithmetically (raw/css-vars.json)",
    "One of the 12 columns at max width: (1251 - 154 - 56) / 12."))
put(grid, ("column-margin",), lit("56px", "dimension",
    "css-var --column-margin declared calc(14 * 4), resolved arithmetically (raw/css-vars.json)",
    "The 4-gap margin inside the 1266 shell."))
put(grid, ("content-max-width",), ref("--grid-content-max-width", "dimension", "The 1195px text column inside the grid."))
put(grid, ("marketing-column",), ref("--gridColumn", "dimension",
    "The marketing stack's column unit at the captured width (calc(100vw / 24) = 60px at 1440)."))
chrome = lay.setdefault("chrome", {})
put(chrome, ("header-height",), ref("--headerHeight", "dimension", "The 56px sticky header."))
put(chrome, ("global-nav-row-height",), ref("--global-nav-header-row-height", "dimension", "The 48px global-nav row."))
put(chrome, ("product-nav-height",), ref("--productNavHeight", "dimension", "The 56px product nav."))
put(chrome, ("promo-height",), ref("--promoHeight", "dimension", "The 44px promo bar."))
put(chrome, ("promo-offset",), ref("--promoHeightOffset", "dimension", "The 44px offset under the promo bar."))
put(chrome, ("header-offset",), ref("--headerOffset", "dimension", "The 100px combined promo+header offset."))
put(chrome, ("scrollbar-width",), ref("--scrollbar-width", "number", "The 15px scrollbar the shell subtracts."))
bp = lay.setdefault("breakpoint", {})
BPS = set()
for r in V.get("global", []) + V.get("component", []):
    for c in r.get("context", []):
        for m in re.finditer(r"@media \(min-width: ?(\d+(?:\.\d+)?)px\)", c):
            BPS.add(float(m.group(1)))
for px in sorted(BPS):
    put(bp, ("%d" % px,), lit("%dpx" % px, "dimension",
        "@media (min-width: %dpx) context in the archived sheets (raw/css-vars.json)" % px,
        "A fluid-type/responsive breakpoint the sheets gate on."))

# ----------------------------------------------------------------- radius
# Measured border radii — the shapes are pills, circles and rounded cards.

rad = SPEC["core"].setdefault("radius", {})
RADII = [
    ("round-48", "login-button", "default",
     "The 48px circle — icon buttons (Log in, menu, social wells) and the lime submit."),
    ("pill", "region-cta", "default",
     "The 9999px pill — CTAs and the region dialog's button."),
    ("chip", "blog-topic", "default",
     "The 100px pill the topic chips paint."),
    ("card", "tile-card", "default",
     "The 24px card radius (category tiles, price cards)."),
    ("dialog", "region-dialog", "default",
     "The 16px dialog radius (the region card)."),
    ("field", "text-field", "default",
     "The 11px input radius."),
    ("circle", "disabled-button", "default",
     "The 100% circle the disabled control paints."),
]
for name, comp, state, desc in RADII:
    try:
        v = st(comp, state)["borderTopLeftRadius"]
    except KeyError:
        continue
    if v and v != "0px":
        ty = "dimension" if v.endswith("px") else "other"
        put(rad, (name,), lit(v, ty,
            f"computed borderTopLeftRadius of {comp} {state} (raw/components-computed.json)", desc))

# --------------------------------------------------------------- palette
# forhers publishes no colour scale — these are the literal colours the
# archived inline sheets declare, counted across the capture (the sheets are
# indexed in raw/css-vars.json). Ramps are named by role, not by a product
# token name the site never gave them.

pal = SPEC["core"].setdefault("palette", {})


def census():
    out = {}
    for r in V.get("global", []) + V.get("component", []):
        for val in (r.get("properties") or {}).values():
            for m in re.finditer(r"#[0-9a-fA-F]{6}\b|rgba?\([\d\s.,]+\)", str(val)):
                k = norm_color(re.sub(r"\s+", " ", m.group(0)))
                out[k] = out.get(k, 0) + 1
    return out


CENSUS = census()
# Colours that only appear in full rule bodies (the census above counts the
# custom-property declarations css-vars.json keeps). These counts were taken by
# hand at capture time across the archived inline sheets, which are not
# committed, so the sources say so and nothing recounts them.
SHEET_COUNTS = {
    "#ffffff": 234, "#338585": 103, "#000000": 62, "#3f676d": 34, "#c5ed82": 34,
    "#6498a0": 30, "#76b2a7": 29, "#78b3a8": 29, "#9cccbc": 29, "#757575": 28,
    "#e8eae8": 25, "#e4eee6": 24, "#f2f9f4": 24, "#90ad72": 23, "#bff8b1": 22,
    "#f4f1e6": 20, "#faf8f2": 20, "#9abdb1": 20, "#f0f0f0": 18, "#efefef": 18,
    "#fdffa7": 15, "#f1f1f1": 12, "#235b5b": 12, "#2a6868": 12, "#7b8967": 10,
    "#eaf3ed": 10, "#13262e": 10, "#f2ede5": 10, "#729693": 10, "#384429": 8,
    "#194737": 8, "#3b5b50": 8, "#e7e7e7": 7, "#b0d563": 7, "#343c2b": 6,
    "#1e3944": 4, "#f1f4f2": 4, "#941f18": 4, "#5e1e1a": 4, "#451310": 4,
    "#e4ff8b": 4, "#5d62c8": 3, "#5e91d6": 3, "#6cc2d6": 3, "#8fdfc5": 3,
    "#e5e5e5": 3, "#e8e8e2": 3, "#f7f7f7": 2, "#e4eae6": 2, "#3e4f49": 2,
    "#5d2f24": 2, "#87a299": 2, "#8a3a34": 2, "#b4cdc4": 2, "#384b4a": 2,
    "#263a1e": 2, "#486635": 2, "#162511": 2, "#2d4021": 2, "#a3b58d": 2,
    "#c1d4a3": 2, "#c3ec82": 2, "#7b9e92": 2, "#ff7350": 2, "#334b43": 2,
    "#1a6966": 2, "#9fb089": 2, "#7d8f66": 2, "#536240": 2, "#2d3421": 2,
    "#9dbd67": 2, "#a6fb89": 2, "#225c5c": 2, "#8f8f8f": 2, "#0077ab": 1,
    "#8db0ca": 1, "#d2d2d2": 1, "#f5faf6": 1, "#b7d7a3": 1, "#178052": 1,
    "#162a13": 1, "#223c47": 1, "#313631": 1, "#b6dd64": 1, "#d5ff5d": 1,
    "#ccddb7": 1,
}


def swatch(group, name, value, desc):
    n = CENSUS.get(norm_color(value), 0)
    hand_n = SHEET_COUNTS.get(norm_color(value), 0)
    if n:
        src = (f"stylesheet literal, {n} custom-property declaration{'s' if n != 1 else ''} in "
               "raw/css-vars.json")
    elif hand_n:
        src = (f"stylesheet literal, {hand_n} declaration{'s' if hand_n != 1 else ''} counted by hand at capture "
               "time in the archived inline sheets (not committed; raw/css-vars.json keeps the sheet index)")
    else:
        src = "stylesheet literal in the archived inline sheets (raw/css-vars.json sheet index)"
    put(pal, (group, name), lit(value, "color", src, desc))


# ink — near-black text and its alpha steps (measured + declared)
swatch("ink", "base", "#000000", "The ink every ramp step derives from.")
RAW_TEXT = {f.name: f.read_text() for f in (RAW / "components-computed.json", RAW / "css-vars.json")}


def ink_source(v):
    """Where an ink step was read: the first computed reading that paints it (text colour first,
    then fills, then any property, then a layer inside a composite such as a box-shadow), else a
    declaration in raw/css-vars.json, else None (typed in at capture time)."""
    order = ("color", "backgroundColor")
    found = {}

    def strings(node, key=None):
        """(property, value) for every string under a state: style, textStyle, and the paint and
        ancestor layers the kit records."""
        if isinstance(node, dict):
            for kk, vv in node.items():
                yield from strings(vv, kk)
        elif isinstance(node, list):
            for vv in node:
                yield from strings(vv, key)
        elif isinstance(node, str):
            yield key, node

    for k, c in C.items():
        for state, st in c.get("states", {}).items():
            if True:
                for prop, val in strings(st):
                    rank = order.index(prop) if prop in order else len(order)
                    try:
                        whole = norm_color(val) == v
                    except ValueError:
                        whole = False
                    if whole:
                        what = "painted fill (a paint layer)" if prop == "bg" else f"computed {prop}"
                        found.setdefault(rank, f"{what} of {k} {state} (raw/components-computed.json)")
                    elif v in val:
                        found.setdefault(9, f"a layer of computed {prop} of {k} {state} (raw/components-computed.json)")
    if found:
        return found[min(found)]
    compact = v.replace(" ", "").replace("(0,0,0,0.", "(0,0,0,.")
    if v in RAW_TEXT["css-vars.json"] or compact in RAW_TEXT["css-vars.json"]:
        return "declared in an archived inline sheet (raw/css-vars.json)"
    return None


for name, v, d in [
    ("a89", "rgba(0, 0, 0, 0.89)", "Primary text — nav, body, footer."),
    ("a74", "rgba(0, 0, 0, 0.74)", "A mid emphasis step."),
    ("a65", "rgba(0, 0, 0, 0.65)", "Secondary text — prose body, privacy notes."),
    ("a54", "rgba(0, 0, 0, 0.54)", "The muted step."),
    ("a50", "rgba(0, 0, 0, 0.5)", "The page dek's reading."),
    ("a44", "rgba(0, 0, 0, 0.44)", "Subtle text — bylines and meta."),
    ("a37", "rgba(0, 0, 0, 0.37)", "The faint step — 'Read more'."),
    ("a33", "rgba(0, 0, 0, 0.33)", "Placeholder/disabled-adjacent text."),
    ("a30", "rgba(16, 16, 16, 0.3)", "Disabled control text."),
    ("a12", "rgba(0, 0, 0, 0.12)", "Hairlines and card borders."),
    ("a08", "rgba(0, 0, 0, 0.08)", "The soft divider wash."),
    ("a06", "rgba(0, 0, 0, 0.06)", "Hover wells — Log in hover, chips, social wells, disabled fill."),
    ("a05", "rgba(0, 0, 0, 0.05)", "The lightest wash."),
    ("a03", "rgba(0, 0, 0, 0.03)", "The faintest surface tint."),
]:
    v = norm_color(v)
    src = ink_source(v) or ("Reconstruction — entered by hand at capture time, no raw reading behind it "
                            "(no computed style or declaration holds this step)")
    put(pal, ("ink", name), lit(v, "color", src, d))

# paper — whites and greys
for name, v, d in [
    ("white", "#ffffff", "The page field."),
    ("snow", "#f7f7f7", "A soft panel."),
    ("wash", "#f0f0f0", "The wash surface."),
    ("wash-2", "#f1f1f1", "A wash variant."),
    ("grey", "#efefef", "The tertiary button surface and carousel arrow base."),
    ("grey-2", "#e7e7e7", "A grey step."),
    ("grey-3", "#e5e5e5", "A grey step."),
    ("footer", "#e8eae8", "The footer slab — measured on the footer."),
    ("warm-grey", "#e8e8e2", "The warm grey surface."),
    ("silver", "#d2d2d2", "A mid grey."),
    ("mid", "#8f8f8f", "A mid grey."),
    ("muted", "#757575", "The muted grey — accordion labels."),
]:
    swatch("paper", name, v, d)

# sage + cream surfaces
for name, v, d in [
    ("sage-050", "#f5faf6", "The lightest sage surface."),
    ("sage-100", "#f2f9f4", "The sage surface."),
    ("sage-200", "#eaf3ed", "A mid sage."),
    ("sage-300", "#e4eee6", "The deep sage surface."),
    ("sage-400", "#f1f4f2", "A sage-grey."),
    ("cream-100", "#faf8f2", "The light cream."),
    ("cream-200", "#f4f1e6", "The cream surface."),
    ("cream-300", "#f2ede5", "The deep cream."),
]:
    swatch("surface", name, v, d)

# teal — the Hers brand ramp
for name, v, d in [
    ("950", "#13262e", "The deepest teal — dark hero surfaces."),
    ("900", "#1e3944", "A deep teal."),
    ("850", "#223c47", "A deep teal."),
    ("800", "#235b5b", "Deep teal."),
    ("750", "#2a6868", "Deep teal."),
    ("700", "#338585", "The Hers teal — 103 declarations: badges, quality seals, accents."),
    ("650", "#3f676d", "A dark teal-grey."),
    ("600", "#6498a0", "The mid teal."),
    ("550", "#729693", "A mid teal."),
    ("500", "#76b2a7", "The soft teal."),
    ("450", "#78b3a8", "The soft teal variant."),
    ("400", "#87a299", "A sage-teal."),
    ("350", "#7b9e92", "A sage-teal."),
    ("300", "#9cccbc", "The pale teal."),
    ("250", "#9abdb1", "The pale sage-teal."),
    ("200", "#b4cdc4", "The lightest teal."),
]:
    swatch("teal", name, v, d)

# forest — the dark greens
for name, v, d in [
    ("950", "#162511", "The deepest green."),
    ("900", "#162a13", "A deep green."),
    ("850", "#194737", "A deep green-teal."),
    ("800", "#263a1e", "A dark green."),
    ("750", "#2d4021", "A dark green."),
    ("700", "#2d3421", "A dark olive."),
    ("650", "#313631", "A dark neutral green."),
    ("600", "#343c2b", "A dark olive."),
    ("550", "#384429", "A mid olive."),
    ("500", "#3e4f49", "A green-grey."),
    ("450", "#334b43", "A deep green-grey."),
    ("400", "#486635", "A mid green."),
    ("350", "#536240", "A mid olive."),
]:
    swatch("forest", name, v, d)

# sage-green ramp
for name, v, d in [
    ("700", "#7d8f66", "A deep sage green."),
    ("650", "#7b8967", "A deep sage green."),
    ("600", "#90ad72", "A mid sage green."),
    ("550", "#9fb089", "A mid sage green."),
    ("500", "#9dbd67", "The mid sage green."),
    ("450", "#a3b58d", "A soft sage green."),
    ("300", "#b7d7a3", "A pale sage green."),
    ("200", "#c1d4a3", "A pale sage green."),
    ("100", "#ccddb7", "The palest sage green."),
]:
    swatch("sage-green", name, v, d)

# lime — the promo/highlight ramp
for name, v, d in [
    ("600", "#b0d563", "A mid lime."),
    ("550", "#b6dd64", "The BMI Calculate submit's fill — measured."),
    ("500", "#c3ec82", "A soft lime."),
    ("450", "#c5ed82", "The soft lime — 34 declarations."),
    ("400", "#d5ff5d", "The promo lime — the promo bar's highlight."),
    ("350", "#e4ff8b", "A pale lime."),
    ("300", "#a6fb89", "A green-leaning lime."),
    ("200", "#bff8b1", "The pale lime."),
    ("100", "#fdffa7", "The palest yellow-lime."),
]:
    swatch("lime", name, v, d)

# clay — terracotta/alert ramp
for name, v, d in [
    ("900", "#451310", "The deepest clay."),
    ("800", "#5d2f24", "A dark clay."),
    ("700", "#5e1e1a", "A dark clay."),
    ("600", "#8a3a34", "The terracotta."),
    ("500", "#941f18", "The alert red."),
    ("accent", "#ff7350", "The coral accent."),
]:
    swatch("clay", name, v, d)

# accent — links and one-off accents
for name, v, d in [
    ("link", "#0077ab", "The text-link blue — measured on the drug index links."),
    ("green", "#178052", "A success green."),
    ("teal", "#1a6966", "A bright teal."),
    ("deep-teal", "#225c5c", "A deep teal accent."),
    ("mint", "#8fdfc5", "A mint accent."),
    ("violet", "#5d62c8", "A violet accent."),
    ("blue", "#5e91d6", "A blue accent."),
    ("sky", "#6cc2d6", "A sky accent."),
    ("steel", "#8db0ca", "A steel blue."),
]:
    swatch("accent", name, v, d)

# ------------------------------------------------------- semantic (light)

light = SPEC["light"]
SEM = [
    (("bg", "page"), "{palette.paper.white}", "The page field every surface sits on."),
    (("bg", "wash"), "{palette.paper.wash}", "The light wash surface."),
    (("bg", "grey"), "{palette.paper.grey}", "The tertiary button / carousel arrow base."),
    (("bg", "footer"), "{palette.paper.footer}", "The footer slab."),
    (("bg", "sage"), "{palette.surface.sage-100}", "The sage section surface."),
    (("bg", "sage-deep"), "{palette.surface.sage-300}", "The deeper sage surface."),
    (("bg", "cream"), "{palette.surface.cream-100}", "The cream section surface."),
    (("bg", "ink"), "{palette.ink.base}", "The dark surface — the black CTA pill and dark modules."),
    (("text", "primary"), "{palette.ink.a89}", "Primary text."),
    (("text", "secondary"), "{palette.ink.a65}", "Secondary text — prose body, notes."),
    (("text", "muted"), "{palette.ink.a54}", "Muted text."),
    (("text", "subtle"), "{palette.ink.a44}", "Subtle text — bylines, meta."),
    (("text", "faint"), "{palette.ink.a37}", "Faint text — 'Read more'."),
    (("text", "disabled"), "{palette.ink.a30}", "Disabled control text."),
    (("text", "on-dark"), "{palette.paper.white}", "Text on dark surfaces and the black CTA."),
    (("action", "primary-bg"), "{palette.ink.base}", "The primary action fill — the black pill."),
    (("action", "primary-ink"), "{palette.paper.white}", "Label on the primary action."),
    (("action", "lime-bg"), "{palette.lime.550}", "The lime submit fill (BMI Calculate)."),
    (("action", "lime-ink"), "{palette.ink.base}", "Label on the lime submit."),
    (("action", "tertiary-bg"), "{palette.paper.grey}", "The tertiary button fill."),
    (("action", "hover-wash"), "{palette.ink.a06}", "The 6% ink wash ghost buttons paint on hover/pressed."),
    (("action", "disabled-bg"), "{palette.ink.a06}", "The disabled fill."),
    (("action", "disabled-ink"), "{palette.ink.a30}", "The disabled label."),
    (("accent", "teal"), "{palette.teal.700}", "The Hers teal — badges, quality seals."),
    (("accent", "link"), "{palette.accent.link}", "The text-link blue."),
    (("accent", "lime"), "{palette.lime.400}", "The promo lime."),
    (("accent", "clay"), "{palette.clay.600}", "The terracotta accent."),
    (("accent", "alert"), "{palette.clay.500}", "The alert red."),
    (("promo", "bg"), "{palette.lime.400}", "The promo bar highlight."),
    (("border", "hairline"), "{palette.ink.a12}", "The 12% hairline."),
    (("border", "wash"), "{palette.ink.a06}", "The 6% border wash (dialog edge)."),
    (("focus", "ring"), "#101010", "The painted focus indicator — outline: auto 1px rgb(16,16,16)."),
]
FOCUS_SRC = ink_source("#101010")
if not FOCUS_SRC:
    raise KeyError("no reading paints the #101010 focus outline")
for path, val, desc in SEM:
    ty = "color"
    src = ("alias over core.palette; the palette leaf cites its measurement or declaration" if val.startswith("{")
           else FOCUS_SRC + "; a literal, not an alias (no palette step holds it)")
    put(light, path, {"value": val, "type": ty, "source": src, "description": desc})

# ------------------------------------------------------------- components

comp = SPEC["component"]
COMP_DIMS = [
    ("promo-bar-height", "promo-bar", "default", "h", "The promo strip (~55px painted; the --promoHeight var names 44)."),
    ("logo-width", "logo", "default", "w", "The ~71px 'hers' wordmark."),
    ("logo-height", "logo", "default", "h", "The wordmark's 56px row."),
    ("icon-button-size", "login-button", "default", "w", "The 48px circular icon button (Log in, menu)."),
    ("hero-heading-width", "hero-heading", "default", "w", "The hero headline measure at 1440."),
    ("product-card-width", "product-card", "default", "w", "The 320px product card."),
    ("product-card-height", "product-card", "default", "h", "The 389px product card."),
    ("treatment-card-width", "treatment-card", "default", "w", "The ~282px treatment card."),
    ("treatment-card-height", "treatment-card", "default", "h", "The 468px treatment card."),
    ("testimonial-card-width", "testimonial", "default", "w", "The 546px testimonial card."),
    ("tile-card-width", "tile-card", "default", "w", "The 337px category tile."),
    ("fda-badge-size", "fda-badge", "default", "w", "The 56px FDA badge."),
    ("article-card-width", "article-card", "default", "w", "The ~692px editorial card."),
    ("region-dialog-width", "region-dialog", "default", "w", "The 388px region redirect card."),
    ("region-cta-width", "region-cta", "default", "w", "The 338px region dialog button."),
    ("text-field-width", "text-field", "default", "w", "The 316px BMI text field."),
    ("text-field-height", "text-field", "default", "h", "The 54px field height."),
    ("email-field-width", "email-field", "default", "w", "The 358px email field."),
    ("form-submit-height", "form-submit", "default", "h", "The 48px lime submit."),
    ("blog-topic-chip-width", "blog-topic", "default", "w", "The ~139px topic chip."),
    ("drug-link-width", "drug-link", "default", "w", "A 455px A-Z drug index link."),
    ("m-header-height", "m-header", "default", "h", "The mobile header block at 390 wide."),
    ("m-bento-card-width", "m-bento-card", "default", "w", "The 374px mobile bento card."),
    ("m-cta-primary-width", "m-cta-primary", "default", "w", "The 346px mobile primary CTA."),
    ("m-cta-primary-height", "m-cta-primary", "default", "h", "The 48px mobile primary CTA."),
    ("m-text-field-width", "m-text-field", "default", "w", "The ~161px mobile field."),
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

# measured state moves on the interactive controls — only components whose
# states actually paint on the archived pages (the hydration-owned states are
# gaps by construction)
for name, cname, desc in [
    ("login-button-track", "login-button",
     "Log in icon button: transparent at rest; hover and pressed paint the 6% ink wash."),
    ("menu-toggle-track", "menu-toggle",
     "Menu icon button: the same 6% ink wash on hover and pressed."),
    ("cta-tertiary-track", "cta-tertiary",
     "The tertiary action: rest is a near-transparent fill with dark text; hover paints a 65% ink fill and white text, and pressed darkens the fill further."),
    ("accordion-toggle-track", "accordion-toggle",
     "Accordion row: #757575 grey at rest; hover lifts the label to the .65 ink."),
    ("blog-topic-track", "blog-topic",
     "Topic chip: a 100px pill on the 6% ink wash."),
    ("carousel-arrow-track", "carousel-arrow",
     "Carousel arrow: 30% grey fill with a 2px 30% grey ring."),
    ("form-submit-track", "form-submit",
     "BMI Calculate: the #b6dd64 lime fill with black label; a white border paints on the pressed pass."),
    ("m-cta-primary-track", "m-cta-primary",
     "Mobile primary CTA: the black 9999px pill with white label."),
    ("footer-social-track", "footer-social",
     "Social icon wells: 48px circles on the 6% ink wash."),
    ("drug-link-track", "drug-link",
     "A-Z drug index link: the #0077ab blue."),
]:
    try:
        states = {s2: {p: C[cname]["states"][s2]["style"][p] for p in ("backgroundColor", "color", "transform", "outlineStyle", "outlineColor", "outlineWidth", "outlineOffset", "borderTopColor", "borderColor") if C[cname]["states"][s2]["style"].get(p)}
                  for s2 in ("default", "hover", "pressed", "focus-visible", "focused", "filled")
                  if s2 in C[cname]["states"] and C[cname]["states"][s2].get("style")}
        if states:
            comp.setdefault("state-track", {})[name] = {
                "type": "other",
                "value": states,
                "source": f"computed styles of {cname} across states (raw/components-computed.json)",
                "description": desc}
    except KeyError:
        pass

# the shared focus outline
for cname in ("nav-link", "cta-primary", "cta-tertiary", "read-more", "login-button"):
    try:
        s = st(cname, "focus-visible")
        if s.get("outlineStyle") and s["outlineStyle"] != "none":
            comp["focus-ring"] = lit(
                f"{s['outlineWidth']} {s['outlineStyle']} {s['outlineColor']} offset {s.get('outlineOffset','')}".strip(),
                "other",
                f"computed outline of {cname} focus-visible (raw/components-computed.json)",
                "The painted focus indicator — a 1px solid ring around the control.")
            break
    except KeyError:
        continue

def count(d):
    if not isinstance(d, dict):
        return 1
    if "var" in d or "value" in d or "$value" in d:
        return 1
    return sum(count(v) for v in d.values())


if __name__ == "__main__":
    (RAW / "component-tokens.json").write_text(json.dumps(SPEC, indent=1, ensure_ascii=False) + "\n")
    print("component-tokens.json:", {k: count(v) for k, v in SPEC.items() if isinstance(v, dict)})
