#!/usr/bin/env python3
"""Build tokens.json for TokenTracker from the readings in raw/.

Inputs:
  raw/css-vars.json             custom properties from the dashboard's CSS bundle (vars.mjs)
  raw/components-computed.json  computed styles per component, state and theme (public/measure.mjs)
  raw/census.json               every rendered value counted per page and theme, plus the stylesheet's
                                breakpoints, reduced-motion rules and colour utilities (public/census.mjs)

Output: tokens.json, W3C DTCG in Tokens Studio's multi-set layout: `core`, `light`, `dark` and
`$themes`. Every token carries `$extensions.source`, starting with its evidence label from
docs/EVIDENCE.md (Measured or Derived) and naming the reading it came from.

TokenTracker renders its neutrals from Tailwind classes whose oai-gray-* values are plain hex in
tailwind.config.cjs (#fafafa ... #0a0a0a). styles.css also declares green-tinted --oai-gray-*
custom properties, but the components do not use them, so the palette here is the computed one
and the declared ramp is listed under notTokenised.

Deterministic: same inputs, byte-identical output.
"""
import json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
V = json.loads((RAW / "css-vars.json").read_text())
J = json.loads((RAW / "components-computed.json").read_text())
C = J["components"]
K = json.loads((RAW / "census.json").read_text())
RES = V["resolved"]
READ = J["_meta"]["read"]


# ---------------------------------------------------------------- helpers

def hexa(c):
    """rgb()/rgba() -> #rrggbb or #rrggbbaa (alpha kept when below 1)."""
    m = re.match(r"rgba?\(([\d.]+),\s*([\d.]+),\s*([\d.]+)(?:,\s*([\d.]+))?\)", c or "")
    if not m:
        raise ValueError(f"not a colour: {c!r}")
    rgb = "#" + "".join("%02x" % round(float(x)) for x in m.groups()[:3])
    a = m.group(4)
    if a is None or float(a) >= 1:
        return rgb
    return rgb + "%02x" % round(float(a) * 255)


def ckey(key, theme):
    return key if theme == "dark" else f"{key}.light"


def reading(key, theme, state="default"):
    comp = C[ckey(key, theme)]
    if comp.get("missing"):
        raise KeyError(f"{ckey(key, theme)} was not found at capture time")
    return comp["states"][state]


def meas(key, prop, theme="dark", state="default"):
    """A computed property and its source string."""
    v = reading(key, theme, state)["style"][prop]
    k = ckey(key, theme)
    return v, f"Measured: computed {prop} of {k} {state} ({C[k]['selector']}), raw/components-computed.json, {READ}"


def var(name, theme="light"):
    r = RES[theme][name]
    return r["value"], f"Measured: {name} resolved on :root{'.dark' if theme == 'dark' else ''}, raw/css-vars.json"


def tok(value, ty, source, desc=None, **ext):
    t = {"$value": value, "$type": ty}
    if desc:
        t["$description"] = desc
    t["$extensions"] = {"source": source, **ext}
    return t


def put(tree, path, t):
    node = tree
    parts = path.split(".")
    for p in parts[:-1]:
        node = node.setdefault(p, {})
    node[parts[-1]] = t


def color(key, prop, theme="dark", state="default", desc=None):
    v, s = meas(key, prop, theme, state)
    return tok(hexa(v), "color", s, desc)


def dim(key, prop, theme="dark", state="default", desc=None):
    v, s = meas(key, prop, theme, state)
    return tok(v, "dimension", s, desc)


def shadow_layers(v):
    """A computed box-shadow -> DTCG shadow layers, dropping the transparent placeholders Tailwind adds."""
    found = re.findall(r"(rgba?\([^)]*\)) (-?[\d.]+px) (-?[\d.]+px) (-?[\d.]+px) (-?[\d.]+px)( inset)?", v)
    out = []
    for c, x, y, b, sp, inset in found:
        if c.startswith("rgba") and float(c.rstrip(")").split(",")[-1]) == 0:
            continue
        if b == "0px" and sp == "0px" and x == "0px" and y == "0px":
            continue
        layer = {"offsetX": x, "offsetY": y, "blur": b, "spread": sp, "color": hexa(c)}
        if inset:
            layer["inset"] = True
        out.append(layer)
    return out


def census(theme, kind, where):
    """The census entry of this kind whose element sample names `where`, and its source string."""
    for v, x in K["totals"][theme][kind].items():
        if any(where in w for w in x["where"]):
            return v, (f"Measured: computed {kind} counted on {x['n']} rendered element(s) such as {where} "
                       f"({', '.join(sorted(set(x['pages'])))}, {theme}), raw/census.json")
    raise KeyError(f"census: no {kind} on {where} in {theme}")


# ---------------------------------------------------------------- core

core = {}

# Neutral palette: the hex steps the components render (Tailwind oai-gray-* classes). Each step
# is read from one component that shows it; the step names follow Tailwind's.
NEUTRAL = [
    ("50", "segmented", "backgroundColor", "light", "default"),
    ("100", "period-tab-selected", "backgroundColor", "light", "default"),
    ("200", "card", "borderTopColor", "light", "default"),
    ("300", "select", "borderTopColor", "light", "hover"),
    ("400", "nav-item", "color", "dark", "default"),
    ("500", "page-subtitle", "color", "light", "default"),
    ("600", "nav-item", "color", "light", "default"),
    ("700", "provider-tile", "borderTopColor", "dark", "default"),
    ("800", "card", "borderTopColor", "dark", "default"),
    ("900", "card", "backgroundColor", "dark", "default"),
    ("950", "dialog", "backgroundColor", "dark", "open"),
]
for step, key, prop, theme, st in NEUTRAL:
    put(core, f"color.neutral.{step}", color(key, prop, theme, st))
put(core, "color.neutral.white", color("card", "backgroundColor", "light", desc="Pure white: light cards, dialogs, fields."))

for step in ["50", "100", "200", "300", "400", "500", "600", "700", "800", "900", "950"]:
    v, s = var(f"--brand-{step}")
    put(core, f"color.brand.{step}", tok(v, "color", s))

# Ramps for every other hue the interface uses, with the steps the stylesheet actually ships (the
# Tailwind utility rules in the bundle). Hues with fewer than five steps are listed, not tokenised.
UTIL = K["sheet"]["utilities"]
RAMPS = {"red": "Danger: the toast, the danger button, error text.", "amber": "Warning: cached-limit notices.",
         "orange": "Claude's share in charts and the pace marker.", "sky": "Charts and the one sky ring.",
         "blue": "Charts and provider marks."}
for hue, desc in RAMPS.items():
    for step in sorted(UTIL[hue], key=int):
        u = UTIL[hue][step]
        put(core, f"color.{hue}.{step}", tok(u["value"], "color",
            f"Measured: the {', '.join(u['uses'])} utility rule(s) for {hue}-{step} in the dashboard stylesheet, raw/census.json sheet.utilities",
            desc if step == sorted(UTIL[hue], key=int)[0] else None))

for name in ["success", "warning", "error"]:
    for theme in ["light", "dark"]:
        v, s = var(f"--oai-{name}", theme)
        put(core, f"color.status.{name}.{theme}", tok(v, "color", s))

# Heatmap: five steps per theme, empty first, read off every rendered cell.
for theme in ["dark", "light"]:
    for i, c in enumerate(J["_meta"]["heatmap"][theme]):
        put(core, f"color.heatmap.{theme}.{i}", tok(hexa(c), "color",
            f"Measured: the distinct computed fills of the 12px heatmap cells on /dashboard ({theme}), empty first, raw/components-computed.json _meta.heatmap"))

# Type
v, s = var("--oai-font-sans")
put(core, "font.family.sans", tok(v, "fontFamily", s, "One family carries everything: the OS system font, so SF Pro on macOS."))
v, s = var("--oai-font-mono")
put(core, "font.family.mono", tok(v, "fontFamily", s, "Code blocks and terminal-style copy."))

TYPE = [
    ("display", "hero-metric", "The one giant number (total tokens). Tabular figures."),
    ("pageTitle", "page-title", "h1 on every page but Tokens."),
    ("sectionTitle", "section-title", "Settings section heading."),
    ("figure", "hero-cost", "Cost under the hero, set in the brand green."),
    ("body", "page-subtitle", "Page subtitles and body copy."),
    ("bodySmall", "setting-label", "Setting labels, table cells, field text."),
    ("rowTitle", "list-row-title", "A list row's name."),
    ("subnav", "subnav-item", "Settings sub-navigation."),
    ("nav", "nav-item", "Sidebar items; the current item steps up to 500."),
    ("control", "period-tab", "Tabs, segments, buttons."),
    ("caption", "setting-description", "Descriptions, summary labels, column headers."),
    ("eyebrow", "hero-label", "Uppercase label above the hero number. See Do and don't."),
    ("cardTitleLegacy", "card-title", "Uppercase card title on the older cards. See Do and don't."),
    ("groupLabel", "sidebar-group-label", "Sidebar group label, uppercase. See Do and don't."),
    ("badge", "badge", "Neutral pill on a skill row."),
    ("code", "code-block", "Code blocks and terminal copy (Limits, the first-run install command)."),
    ("tableHeader", "table-header", "Daily Breakdown column headers."),
]
for role, key, desc in TYPE:
    r = reading(key, "dark")
    st = r.get("textStyle") or r["style"]
    src = f"Measured: computed font of {key} default (dark){' (its label ' + st['node'] + ')' if r.get('textStyle') else ''}, raw/components-computed.json, {READ}"
    put(core, f"font.size.{role}", tok(st["fontSize"], "dimension", src))
    put(core, f"font.weight.{role}", tok(int(st["fontWeight"]), "fontWeight", src))
    put(core, f"font.lineHeight.{role}", tok(st["lineHeight"], "dimension", src))
    put(core, f"font.letterSpacing.{role}", tok("0px" if st["letterSpacing"] == "normal" else st["letterSpacing"], "dimension", src))
    put(core, f"typography.{role}", tok({
        "fontFamily": "{font.family.mono}" if role == "code" else "{font.family.sans}", "fontSize": f"{{font.size.{role}}}", "fontWeight": f"{{font.weight.{role}}}",
        "lineHeight": f"{{font.lineHeight.{role}}}", "letterSpacing": f"{{font.letterSpacing.{role}}}",
    }, "typography", src, desc, textTransform=st["textTransform"]))

# The type scale as rendered: every size / line height / weight that at least 10 text elements use
# across the ten pages (dark), beyond the named roles above. Named by size and weight.
named = {(core["font"]["size"][r]["$value"], core["font"]["lineHeight"][r]["$value"], core["font"]["weight"][r]["$value"]) for r, *_ in TYPE}
for v, x in K["totals"]["dark"]["type"].items():
    m = re.fullmatch(r"([\d.]+px)/([\d.]+px) (\d+)", v)
    if not m or x["n"] < 10 or (m.group(1), m.group(2), int(m.group(3))) in named:
        continue
    size, lh, w = m.group(1), m.group(2), int(m.group(3))
    name = f"text{size[:-2].replace('.', '_')}w{w}"
    if name in core.get("typography", {}):
        name += f"lh{lh[:-2].replace('.', '_')}"
    put(core, f"typography.{name}", tok({"fontFamily": "{font.family.sans}", "fontSize": size, "fontWeight": w, "lineHeight": lh, "letterSpacing": "0px"},
        "typography", f"Measured: computed font of {x['n']} rendered text elements such as {x['where'][0]} ({', '.join(sorted(set(x['pages']))[:4])}, dark), raw/census.json totals.dark.type"))

# The size scale: every font size that at least 10 rendered text elements use (dark, all pages).
from collections import Counter
sizes = Counter()
for v, x in K["totals"]["dark"]["type"].items():
    sizes[v.split("/")[0]] += x["n"]
for i, (size, n) in enumerate(sorted(((sz, n) for sz, n in sizes.items() if n >= 10), key=lambda kv: float(kv[0][:-2]))):
    put(core, f"font.scale.{size[:-2]}", tok(size, "dimension",
        f"Measured: font size of {n} rendered text elements across the ten pages (dark), raw/census.json totals.dark.type"))

# Radii, each from the component that shows it
RADII = [
    ("xs", "heatmap-cell", "Heatmap cells."),
    ("sm", "table-tab", "Table tabs, badges, code blocks."),
    ("md", "select", "Selects."),
    ("lg", "nav-item", "Nav items, buttons, tabs, fields, segments."),
    ("xl", "provider-tile", "Tiles, stat chips, segmented tracks, icon buttons, menu options."),
    ("2xl", "card", "Cards, the content panel, dialogs, status rows."),
    ("full", "usage-track", "Usage tracks, the footer pills."),
]
for name, key, desc in RADII:
    put(core, f"radius.{name}", dim(key, "borderTopLeftRadius", desc=desc))
put(core, "border.width.default", dim("card", "borderTopWidth", desc="Every border is one hairline."))

# Sizes
SIZES = [
    ("sidebar.width", "sidebar", "w", "Expanded sidebar."),
    ("navItem.height", "nav-item", "h", None),
    ("control.sm", "period-tab", "h", "Tabs, segments, small buttons."),
    ("control.md", "share-button", "h", "Outlined buttons."),
    ("control.field", "search-input", "h", "Fields and selects."),
    ("iconButton", "icon-button", "w", "Square icon buttons."),
    ("usageTrack.height", "usage-track", "h", None),
    ("heatmapCell", "heatmap-cell", "w", None),
]
for path, key, axis, desc in SIZES:
    put(core, f"size.{path}", tok(f"{reading(key, 'dark')['rect'][axis]:g}px", "dimension",
        f"Measured: rendered {'width' if axis == 'w' else 'height'} of {key} default (dark), raw/components-computed.json", desc))
put(core, "size.icon.nav", tok(f"{reading('nav-icon', 'dark')['icon']['w']:g}px", "dimension",
    "Measured: rendered size of the Lucide icon in a[href=/sessions], raw/components-computed.json", "Lucide, default stroke 2."))
put(core, "size.icon.control", tok(f"{reading('icon-button', 'dark')['icon']['w']:g}px", "dimension",
    "Measured: rendered size of the icon in the Refresh icon button, raw/components-computed.json"))
put(core, "size.icon.small", tok(f"{reading('share-button', 'dark')['icon']['w']:g}px", "dimension",
    "Measured: rendered size of the icon in the Share button, raw/components-computed.json", "Icons inside buttons, selects and the theme toggle."))
put(core, "size.sidebar.collapsedWidth", tok("72px", "dimension",
    "Derived: read from the dashboard source (the collapsed sidebar's w-[72px]); not rendered at capture time"))

# Spacing: paddings as measured
PADS = [
    ("navItem.y", "nav-item", "paddingTop"), ("navItem.x", "nav-item", "paddingLeft"),
    ("control.y", "period-tab", "paddingTop"), ("control.x", "period-tab", "paddingLeft"),
    ("tile", "provider-tile", "paddingTop"), ("card", "card", "paddingTop"),
    ("statusRow", "status-row", "paddingTop"), ("listRow.y", "list-row", "paddingTop"),
    ("tableCell.y", "table-cell", "paddingTop"), ("tableCell.x", "table-cell", "paddingLeft"),
    ("subnav.y", "subnav-item", "paddingTop"), ("subnav.x", "subnav-item", "paddingLeft"),
]
for path, key, prop in PADS:
    put(core, f"space.{path}", dim(key, prop))
# The spacing scale: every padding and gap rendered on the ten pages, in px, kept when it sits on the
# 2px half-step of Tailwind's 4px base and is used on more than one element. Step names are px / 4.
for v, x in sorted(K["totals"]["dark"]["space"].items(), key=lambda kv: float(kv[0][:-2])):
    px = float(v[:-2])
    if px != int(px) or int(px) % 2 or x["n"] < 2 or px > 64:
        continue
    step = f"{px / 4:g}".replace(".", "_")
    put(core, f"space.scale.{step}", tok(v, "dimension",
        f"Measured: padding or gap of {x['n']} rendered elements across {len(set(x['pages']))} pages (dark), raw/census.json totals.dark.space"))
pr = reading("content-panel", "dark")["rect"]
put(core, "space.panelInset", tok(f"{pr['y']:g}px", "dimension",
    "Measured: the content panel's top offset from the window at 1440 x 900, raw/components-computed.json", "Gap between the window edge and the content panel."))

# Elevation and motion
v, s = meas("content-panel", "boxShadow")
put(core, "shadow.sm", tok([{"offsetX": "0px", "offsetY": "1px", "blur": "2px", "spread": "0px", "color": "#0000000d"}], "shadow", s,
    "The only resting shadow: the content panel and the selected segment."))
for theme in ["dark", "light"]:
    v, s = meas("dialog", "boxShadow", theme, "open")
    found = re.findall(r"(rgba?\([^)]*\)) (-?[\d.]+px) (-?[\d.]+px) (-?[\d.]+px) (-?[\d.]+px)", v)
    layers = [{"offsetX": x, "offsetY": y, "blur": b, "spread": sp, "color": hexa(c)} for c, x, y, b, sp in found if not (b == "0px" and sp == "0px")]
    put(core, f"shadow.dialog.{theme}", tok(layers, "shadow", s, "A 1px ring in the border colour plus one deep, soft drop."))

v, s = meas("toast", "boxShadow", "dark", "open")
put(core, "shadow.md", tok(shadow_layers(v), "shadow", s, "Toasts and small floating chips (Tailwind shadow-md)."))
anc = reading("select-menu", "dark", "open")["ancestors"][0]
put(core, "shadow.lg", tok(shadow_layers(anc["shadow"]), "shadow",
    f"Measured: computed box-shadow of the select menu's popup ({anc['node']}), the parent of select-menu open (dark), raw/components-computed.json",
    "Menus and the small hint tooltip: a 1px ring plus Tailwind shadow-lg."))
v, s = meas("hint-tooltip", "boxShadow", "dark", "open")
put(core, "shadow.lgBare", tok(shadow_layers(v), "shadow", s, "Tailwind shadow-lg without the ring: the hint tooltip on Limits."))
v, s = meas("tooltip", "boxShadow", "dark", "open")
put(core, "shadow.xl", tok(shadow_layers(v), "shadow", s, "The heatmap tooltip (Tailwind shadow-xl)."))
for theme in ["dark", "light"]:
    v, src = census(theme, "shadow", "span.inline-flex.shrink-0.rounded-full")
    put(core, f"shadow.ring.{theme}", tok(shadow_layers(v), "shadow", src, "A 1px ring drawn as a shadow: provider and agent marks, pills." if theme == "dark" else None))
v, s = meas("confirm-dialog", "boxShadow", "dark", "open")
put(core, "shadow.confirm.dark", tok(shadow_layers(v), "shadow", s, "Confirmation dialogs: a 1px ring and a deep drop."))
v, s = meas("confirm-dialog", "boxShadow", "light", "open")
put(core, "shadow.confirm.light", tok(shadow_layers(v), "shadow", s))

# Focus ring: the few controls that keep one draw a 2px solid outline 2px out.
v, s = meas("theme-toggle", "outlineWidth", "dark", "focus-visible")
put(core, "focusRing.width", tok(v, "dimension", s, "Theme toggle, star pill, sidebar chevron and the Cloud page's controls. Every other control draws none."))
v, s = meas("theme-toggle", "outlineOffset", "dark", "focus-visible")
put(core, "focusRing.offset", tok(v, "dimension", s))

# Layers: the z-index each kind of layer renders at.
LAYERS = [("sticky", "census", "thead.sticky.top-0.z-10", "Sticky table headers and page headers."),
          ("tooltip", "hint-tooltip", "open", "Hint tooltips."),
          ("scrim", "dialog-scrim", "open", "The dim layer behind a dialog."),
          ("shareSheet", "share-dialog", "open", "The full-window share sheet and its toasts.")]
for name, key, st, desc in LAYERS:
    if key == "census":
        v, src = census("dark", "z", st)
        v = v.split()[0]
    else:
        v, src = meas(key, "zIndex", "dark", st)
        if v == "auto":
            raise SystemExit(f"{key} has no z-index of its own")
    put(core, f"zIndex.{name}", tok(int(v), "number", src, desc))
dl = [l for l in J["_meta"]["layers"]["dialog.dark"] if l["position"] == "fixed" and "101" in l["cls"]]
put(core, "zIndex.dialog", tok(dl[0]["z"], "number",
    "Measured: computed z-index of the fixed layer holding the open cost dialog, raw/components-computed.json _meta.layers[\"dialog.dark\"]", "Dialogs, one above their scrim."))

# Breakpoints: the min-width media queries in the stylesheet, with how many rules each carries.
BP = {"640px": "sm", "768px": "md", "1024px": "lg", "1280px": "xl", "1536px": "2xl"}
for q, n in K["sheet"]["media"].items():
    m = re.fullmatch(r"\(min-width: (\d+px)\)", q)
    if m and m.group(1) in BP:
        put(core, f"breakpoint.{BP[m.group(1)]}", tok(m.group(1), "dimension",
            f"Measured: @media {q} in the dashboard stylesheet ({n} rules), raw/census.json sheet.media",
            "The sidebar shows from lg; below it the sidebar is a drawer." if BP[m.group(1)] == "lg" else None))
put(core, "layout.contentWidth.page", tok("1152px", "dimension",
    "Derived: the max-w-6xl container class seen on the page wrappers (raw/census.json) is 72rem in the dashboard's Tailwind theme; not read as a computed max-width",
    "Every page but Tokens, centred in the panel."))
put(core, "layout.contentWidth.settings", tok("1024px", "dimension",
    "Derived: Settings' max-w-5xl wrapper (64rem), read from the dashboard source; not read as a computed max-width"))
put(core, "layout.columns", tok(12, "number",
    "Derived: the Tokens page's lg:grid-cols-12 grid in the dashboard source; matches the 4 + 8 column split in the screenshots",
    "Tokens page: a 4-column card stack beside an 8-column overview."))

v, s = meas("nav-item", "transitionDuration")
put(core, "motion.duration.fast", tok("150ms", "duration", s, "Colour and background changes on hover."))
v, s = meas("share-button", "transitionDuration")
put(core, "motion.duration.base", tok("200ms", "duration", s, "Buttons, tiles, the sidebar width."))
v, s = meas("dialog", "transitionDuration", "dark", "open")
put(core, "motion.duration.dialog", tok("260ms", "duration", s, "Dialog transform; opacity takes 220ms."))
put(core, "motion.duration.fade", tok("220ms", "duration", s, "Dialog and toast opacity."))
v, s = meas("nav-item", "transitionTimingFunction")
put(core, "motion.easing.standard", tok([0.4, 0, 0.2, 1], "cubicBezier", s))
v, s = meas("dialog", "transitionTimingFunction", "dark", "open")
put(core, "motion.easing.emphasized", tok([0.16, 1, 0.3, 1], "cubicBezier", s, "Dialogs ease out hard."))

core["$extensions"] = {"notTokenised": {
    "declaredGreenTintedGrays": {k: RES["light"][k]["value"] for k in sorted(RES["light"]) if k.startswith("--oai-gray-")},
    "note": "styles.css declares these green-tinted --oai-gray-* properties (oklch hue 145), but the components render the plain hex Tailwind oai-gray-* steps above. TokenTracker's own DESIGN.md describes the tinted ramp; the rendered UI is neutral.",
    "focusRing": "Mostly none: styles.css sets `*:focus, *:focus-visible { outline: none !important }` and zeroes Tailwind's ring shadows. Only the sidebar's theme toggle, star pill and collapse chevron, and the Cloud page, override it with a 2px outline (core.focusRing). Light text fields turn their border emerald on focus (border.focus); dark ones do not change.",
    "reducedMotion": {
        "what changes": "Under prefers-reduced-motion: reduce, the fade and modal keyframe animations stop (animation: none), the Cloud page's action popup and backdrop drop their transitions and their entry transform, and the plan cards' hover glow stops transitioning. Spinners and the sidebar's width and position transitions run only under no-preference. Colour transitions on hover (150 to 200ms) are not changed.",
        "rules": [r["rule"] for r in K["sheet"]["reduced"]],
        "source": "Measured: every rule inside a prefers-reduced-motion media query, and the motion-safe/motion-reduce utilities, in the dashboard stylesheet, raw/census.json sheet.reduced",
    },
    "otherHues": {h: sorted(UTIL[h], key=int) for h in sorted(UTIL) if h not in RAMPS and h not in ("emerald", "oai-brand", "oai-gray")},
    "otherHuesNote": "Hues the stylesheet ships fewer steps of (mostly chart and provider colours). Listed with their steps; not tokenised.",
    "warningNotice": "The only rendered warning surface is a light-theme notice on Limits: amber-50 at 50% fill, amber-300 at 60% border (raw/census.json). Dark has none on screen, so no themed warning fill or border is tokenised.",
    "providerColors": "Per-provider colours (Claude orange, Codex blue, OpenCode purple) come from getProviderColor() in the dashboard source; data-viz only, not read as tokens.",
}}

# ---------------------------------------------------------------- themed sets

def themed(theme):
    t = {}

    def P(path, tk):
        put(t, path, tk)

    pg = J["_meta"]["page"][theme]
    P("bg.wash", tok(hexa(pg["root"]), "color", f"Measured: computed background of the app root on /dashboard ({theme}), raw/components-computed.json _meta.page", "The window behind the sidebar and panel."))
    P("bg.panel", color("content-panel", "backgroundColor", theme, desc="The rounded content panel every page sits in."))
    P("bg.card", color("card", "backgroundColor", theme, desc="Cards, the limits card, status rows."))
    P("bg.field", color("search-input", "backgroundColor", theme))
    P("bg.dialog", color("dialog", "backgroundColor", theme, "open"))
    anc = reading("select-menu", theme, "open")["ancestors"][0]
    P("bg.raised", tok(hexa(anc["bg"]), "color",
        f"Measured: computed background of the select menu's popup ({anc['node']}), parent of {ckey('select-menu', theme)} open, raw/components-computed.json",
        "Menus and popovers."))
    P("bg.overlay", color("confirm-dialog", "backgroundColor", theme, "open", desc="Dialogs and confirmations."))
    P("bg.scrim", color("dialog-scrim", "backgroundColor", theme, "open", desc="Behind the cost dialog."))
    P("bg.subtle", color("stat-chip", "backgroundColor", theme, desc="Stat chips; quiet filled tiles."))
    P("bg.code", color("code-block", "backgroundColor", theme))
    P("bg.hover", color("nav-item", "backgroundColor", theme, "hover", desc="Hover wash on nav items and menu options."))
    P("bg.selected", color("period-tab-selected", "backgroundColor", theme, desc="Selected tab."))
    P("bg.navActive", color("nav-item-active", "backgroundColor", theme, desc="The current sidebar item."))
    P("bg.segmentTrack", color("segmented", "backgroundColor", theme))
    P("bg.segmentSelected", color("segment-selected", "backgroundColor", theme))
    P("bg.rowHover", color("table-row", "backgroundColor", theme, "hover"))
    P("text.primary", color("hero-metric", "color", theme))
    P("text.strong", color("page-title", "color", theme, desc="Titles; pure white in dark."))
    P("text.secondary", color("page-subtitle", "color", theme))
    P("text.nav", color("nav-item", "color", theme, desc="Sidebar items at rest."))
    P("text.muted", color("sidebar-group-label", "color", theme, desc="Group labels and footer links."))
    P("text.label", color("setting-label", "color", theme))
    P("text.onPrimary", color("primary-button", "color", theme))
    P("text.disabled", color("button-disabled", "color", theme, "disabled", desc="Disabled buttons: a muted grey on a filled neutral, no opacity."))
    P("text.link", color("link", "color", theme, desc="Text links are quiet: muted 12px text with a light underline (link.underline)."))
    P("text.linkHover", color("link", "color", theme, "hover", desc="Links brighten towards the primary text on hover; the underline stays."))
    P("link.underline", color("link", "textDecorationColor", theme, desc="The underline under a text link, lighter than its text."))
    P("border.default", color("card", "borderTopColor", theme))
    P("border.strong", color("share-button", "borderTopColor", theme, desc="Outlined buttons."))
    P("border.hover", color("select", "borderTopColor", theme, "hover"))
    P("border.focus", color("text-field", "borderTopColor", theme, "focused", desc="Text field focus: emerald in light; in dark the border does not change."))
    P("focus.ring", color("theme-toggle", "outlineColor", theme, "focus-visible", desc="The ink colour: the outline matches the strongest text."))
    P("accent.default", color("hero-cost", "color", theme, desc="Cost figures, links, the brand."))
    P("accent.hover", color("cost-button", "color", theme, "hover"))
    P("accent.pressed", color("cost-button", "color", theme, "pressed", desc="Pressed reads the same as hover."))
    P("accent.fill", color("usage-fill", "backgroundColor", theme, desc="Usage bar fill."))
    P("button.primary.bg", color("primary-button", "backgroundColor", theme, desc="Inverted: near-black in light, near-white in dark."))
    P("button.primary.fg", color("primary-button", "color", theme))
    P("button.primary.hover", color("primary-button", "backgroundColor", theme, "hover"))
    P("button.primary.pressed", color("primary-button", "backgroundColor", theme, "pressed"))
    P("button.danger.bg", color("danger-button", "backgroundColor", theme, desc="Destructive confirm only."))
    P("button.danger.hover", color("danger-button", "backgroundColor", theme, "hover"))
    P("button.danger.fg", color("danger-button", "color", theme))
    P("button.disabled.bg", color("button-disabled", "backgroundColor", theme, "disabled"))
    P("button.secondary.bg", color("share-button", "backgroundColor", theme))
    P("button.secondary.border", color("share-button", "borderTopColor", theme))
    P("button.secondary.hoverFg", color("share-button", "color", theme, "hover"))
    P("usage.track", color("usage-track", "backgroundColor", theme))
    for k in ["success", "warning", "error"]:
        P(f"status.{k}", tok(f"{{color.status.{k}.{theme}}}", "color", f"Derived: alias of color.status.{k}.{theme}"))
    v, src = census(theme, "text", "text-emerald-600")
    P("status.successText", tok(hexa(v), "color", src, "\"Operational\" on Service Status."))
    P("status.danger.fill", color("toast", "backgroundColor", theme, "open", desc="The error toast and the danger button."))
    P("status.danger.text", color("toast", "color", theme, "open", desc="Text on the danger fill."))
    P("control.switchOn", tok(hexa(reading("switch-on", theme, "disabled")["paint"][0]["bg"]), "color",
        f"Measured: computed fill of span.tt-toggle-track in {ckey('switch-on', theme)} (disabled, at 50% opacity as a whole), raw/components-computed.json"))
    P("control.switchOff", tok(hexa(reading("switch-off", theme, "disabled")["paint"][0]["bg"]), "color",
        f"Measured: computed fill of span.tt-toggle-track in {ckey('switch-off', theme)} (disabled), raw/components-computed.json"))
    for i in range(5):
        P(f"heatmap.{i}", tok(f"{{color.heatmap.{theme}.{i}}}", "color", f"Derived: alias of color.heatmap.{theme}.{i}"))
    P("elevation.dialog", tok(f"{{shadow.dialog.{theme}}}", "shadow", f"Derived: alias of shadow.dialog.{theme}"))
    P("elevation.ring", tok(f"{{shadow.ring.{theme}}}", "shadow", f"Derived: alias of shadow.ring.{theme}"))
    P("elevation.confirm", tok(f"{{shadow.confirm.{theme}}}", "shadow", f"Derived: alias of shadow.confirm.{theme}"))
    return t


out = {
    "core": core,
    "light": themed("light"),
    "dark": themed("dark"),
    "$themes": [
        {"id": "light", "name": "Light", "selectedTokenSets": {"core": "source", "light": "enabled"}},
        {"id": "dark", "name": "Dark", "selectedTokenSets": {"core": "source", "dark": "enabled"}},
    ],
    "$metadata": {"tokenSetOrder": ["core", "light", "dark"]},
}

# ---------------------------------------------------------------- checks

def leaves(node, prefix=""):
    for k, v in node.items():
        if k.startswith("$"):
            continue
        if isinstance(v, dict) and "$value" in v:
            yield prefix + k, v
        elif isinstance(v, dict):
            yield from leaves(v, prefix + k + ".")


def strings(v):
    if isinstance(v, str):
        yield v
    elif isinstance(v, dict):
        for x in v.values():
            yield from strings(x)
    elif isinstance(v, list):
        for x in v:
            yield from strings(x)


core_names = {n for n, _ in leaves(core)}
problems = []
for setname in ("core", "light", "dark"):
    for n, t in leaves(out[setname]):
        if not re.match(r"(Measured|Derived|Sampled|Observed|Not captured)", t["$extensions"].get("source", "")):
            problems.append(f"{setname}.{n}: source lacks an evidence label")
        for ref in (r for x in strings(t["$value"]) for r in re.findall(r"\{([^{}]+)\}", x)):
            if ref not in core_names:
                problems.append(f"{setname}.{n}: alias {ref} not in core")
if {n for n, _ in leaves(out["light"])} != {n for n, _ in leaves(out["dark"])}:
    problems.append("light and dark name different tokens")
if problems:
    raise SystemExit("\n".join(problems))

(HERE / "tokens.json").write_text(json.dumps(out, indent=2, ensure_ascii=False) + "\n")
print("tokens.json:", " + ".join(f"{sum(1 for _ in leaves(out[s]))} {s}" for s in ("core", "light", "dark")), "tokens; checks pass")
