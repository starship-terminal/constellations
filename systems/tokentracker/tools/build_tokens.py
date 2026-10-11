#!/usr/bin/env python3
"""Build tokens.json for TokenTracker from the readings in raw/.

Inputs:
  raw/css-vars.json             custom properties from the dashboard's CSS bundle (vars.mjs)
  raw/components-computed.json  computed styles per component, state and theme (public/measure.mjs)

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
    ("badge", "beta-badge", "Tiny uppercase badge, drawn at scale 0.9."),
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
        "fontFamily": "{font.family.sans}", "fontSize": f"{{font.size.{role}}}", "fontWeight": f"{{font.weight.{role}}}",
        "lineHeight": f"{{font.lineHeight.{role}}}", "letterSpacing": f"{{font.letterSpacing.{role}}}",
    }, "typography", src, desc, textTransform=st["textTransform"]))

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

v, s = meas("nav-item", "transitionDuration")
put(core, "motion.duration.fast", tok("150ms", "duration", s, "Colour and background changes on hover."))
v, s = meas("share-button", "transitionDuration")
put(core, "motion.duration.base", tok("200ms", "duration", s, "Buttons, tiles, the sidebar width."))
v, s = meas("dialog", "transitionDuration", "dark", "open")
put(core, "motion.duration.dialog", tok("260ms", "duration", s, "Dialog transform; opacity takes 220ms."))
v, s = meas("nav-item", "transitionTimingFunction")
put(core, "motion.easing.standard", tok([0.4, 0, 0.2, 1], "cubicBezier", s))
v, s = meas("dialog", "transitionTimingFunction", "dark", "open")
put(core, "motion.easing.emphasized", tok([0.16, 1, 0.3, 1], "cubicBezier", s, "Dialogs ease out hard."))

core["$extensions"] = {"notTokenised": {
    "declaredGreenTintedGrays": {k: RES["light"][k]["value"] for k in sorted(RES["light"]) if k.startswith("--oai-gray-")},
    "note": "styles.css declares these green-tinted --oai-gray-* properties (oklch hue 145), but the components render the plain hex Tailwind oai-gray-* steps above. TokenTracker's own DESIGN.md describes the tinted ramp; the rendered UI is neutral.",
    "focusRing": "None. styles.css removes every Tailwind focus ring, so focus-visible looks the same as default on every component measured.",
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
    P("border.default", color("card", "borderTopColor", theme))
    P("border.strong", color("share-button", "borderTopColor", theme, desc="Outlined buttons."))
    P("border.hover", color("select", "borderTopColor", theme, "hover"))
    P("accent.default", color("hero-cost", "color", theme, desc="Cost figures, links, the brand."))
    P("accent.hover", color("cost-button", "color", theme, "hover"))
    P("accent.fill", color("usage-fill", "backgroundColor", theme, desc="Usage bar fill."))
    P("button.primary.bg", color("primary-button", "backgroundColor", theme, desc="Inverted: near-black in light, near-white in dark."))
    P("button.primary.fg", color("primary-button", "color", theme))
    P("button.secondary.bg", color("share-button", "backgroundColor", theme))
    P("button.secondary.border", color("share-button", "borderTopColor", theme))
    P("button.secondary.hoverFg", color("share-button", "color", theme, "hover"))
    P("usage.track", color("usage-track", "backgroundColor", theme))
    for k in ["success", "warning", "error"]:
        P(f"status.{k}", tok(f"{{color.status.{k}.{theme}}}", "color", f"Derived: alias of color.status.{k}.{theme}"))
    for i in range(5):
        P(f"heatmap.{i}", tok(f"{{color.heatmap.{theme}.{i}}}", "color", f"Derived: alias of color.heatmap.{theme}.{i}"))
    P("elevation.dialog", tok(f"{{shadow.dialog.{theme}}}", "shadow", f"Derived: alias of shadow.dialog.{theme}"))
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
