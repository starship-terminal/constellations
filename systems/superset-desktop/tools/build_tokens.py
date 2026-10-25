#!/usr/bin/env python3
"""Build tokens.json (W3C DTCG, Tokens Studio multi-set layout) from the raw readings.

    python3 tools/build_tokens.py

Sources, read live from Superset 1.39.0 for macOS on 2026-10-25 over the remote-debugging port
(tools/capture/electron/):
  raw/css-vars.<theme>.json    every custom property the window's stylesheets declare (Tailwind 4's
                               theme layer, shadcn's :root and :root.light fallbacks, highlight.js,
                               Sonner), by sheet, selector and condition, and each name as it computes
                               and paints on body
  raw/theme.<theme>.json       what Superset's theme engine writes: the 46 `ui` colours as inline custom
                               properties on <html>, and the terminal palette it hands to xterm.js
  raw/components.<theme>.json  computed styles of the captured parts, per shot and state (shots.mjs)

How Superset's colours work, and so how this file is laid out. A theme is a JSON object (`ui`,
`terminal`, `editor`); the built-in Dark and Light themes ship in the renderer bundle, and
applyUIColors() writes `ui` onto <html> as shadcn's custom properties (--background, --card,
--primary, --muted-foreground, ...), overriding the stylesheet's :root and :root.light fallbacks. So
each semantic set holds those 46 as `ui.*` (Measured: the inline value, painted), the two fills the
stylesheet mixes from them (`ui.fill-hover`, `ui.fill-selected`), the link and syntax colours that only
the stylesheet sets, the terminal palette, and the Tailwind palette steps the interface uses for status
(running, added, removed). Scales that do not change with the theme (Tailwind's spacing unit, type
sizes, radius, motion) and measured sizes are the core set. role.* maps the checklist roles onto
these, and component.* holds measured component values, aliased to a token when the painted value
matches one.

Every token carries $extensions.source = {evidence, from}. Deterministic: same inputs, same bytes.
"""
import json
import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from colour import bezier, color, is_color, ms, px, shadow  # noqa: E402

PKG = pathlib.Path(__file__).resolve().parent.parent
RAW = PKG / "raw"
THEMES = ["light", "dark"]
DATE = "2026-10-25"

# ---------------------------------------------------------------- PRODUCT (adapt): what the readings are

THEME_NAME = {"light": "Superset Light", "dark": "Superset Dark"}
SHEET = "index-OKFLt8Wb.css"            # the renderer's one Tailwind stylesheet
SCOPE = "body"
# Stylesheet-only colour names (no theme-engine counterpart): group they go to.
CSS_ONLY = [(re.compile(r"^--link(-hover)?$"), "link"), (re.compile(r"^--hljs-"), "syntax")]
# The Tailwind palette steps the interface uses (status dots, diff counts), same in both themes.
PALETTE = re.compile(r"^--color-(amber|emerald|green|red|yellow|orange|blue|sky|purple|violet|rose|pink|neutral|slate|gray|zinc)-\d+$|^--color-(black|white)$")


def load(name):
    return json.loads((RAW / name).read_text())


V = {t: load(f"css-vars.{t}.json") for t in THEMES}
TH = {t: load(f"theme.{t}.json") for t in THEMES}
C = {t: load(f"components.{t}.json") for t in THEMES}

# ---------------------------------------------------------------- helpers


def tok(value, ty, evidence, where, **ext):
    t = {"$value": value, "$type": ty, "$extensions": {"source": {"evidence": evidence, "from": where}}}
    t["$extensions"].update({k: v for k, v in ext.items() if v is not None})
    return t


def put(tree, path, t):
    node = tree
    for k in path[:-1]:
        node = node.setdefault(k, {})
    node[path[-1]] = t


def computed(t):
    return V[t]["computed"][SCOPE]


def decl(t, name, sel=None, cond=""):
    for d in V[t]["decls"]:
        if d["name"] == name and (sel is None or d["selector"] == sel) and d["condition"] == cond:
            return d
    return None


def rem(v):
    """'.75rem' -> '12px' (Superset's root font size is 16px)."""
    m = re.fullmatch(r"(-?\d*\.?\d+)rem", v.strip())
    return px("%gpx" % (float(m.group(1)) * 16)) if m else None


# ---------------------------------------------------------------- semantic sets


def semantic(t):
    tree, painted = {}, V[t]["colors"]
    inline = TH[t]["inline"]
    # 1. the theme engine's ui colours, written inline on <html>
    for n in sorted(inline):
        if n in painted and is_color(painted[n]):
            put(tree, ("ui", n[2:]), tok(color(painted[n]), "color", "Measured",
                f"{n} = {inline[n]} on <html> (inline, written by Superset's theme engine for the {THEME_NAME[t].split()[1]} theme), {DATE}"))
    # 2. the two fills the stylesheet mixes from the foreground
    for n in ("--fill-hover", "--fill-selected"):
        sel = ":root.light" if t == "light" else ":root"
        d = decl(t, n, sel, "(color: color-mix(in lab, red, red))")
        put(tree, ("ui", n[2:]), tok(color(painted[n]), "color", "Measured",
            f"{n} on {SCOPE}, painted, {THEME_NAME[t]}, {DATE}", formula=d["value"] if d else computed(t)[n]))
    # 3. stylesheet-only colours: links and highlight.js syntax
    for n in sorted(painted):
        for pat, group in CSS_ONLY:
            if pat.match(n) and is_color(painted[n]):
                key = n[2:].replace("hljs-", "") if group == "syntax" else ("default" if n == "--link" else "hover")
                sel = {"link": ":root.light" if t == "light" else ":root", "syntax": ".light" if t == "light" else ":root"}[group]
                d = decl(t, n, sel)
                put(tree, (group, key), tok(color(painted[n]), "color", "Measured",
                    f"{n} = {d['value'] if d else computed(t)[n]} ({sel} in {SHEET}), painted on {SCOPE}, {THEME_NAME[t]}, {DATE}"))
    # 4. the terminal palette (xterm.js paints it on a canvas; no CSS holds it)
    for k in sorted(TH[t]["terminal"]):
        v = TH[t]["terminal"][k]
        if isinstance(v, str) and is_color(v):
            put(tree, ("terminal", re.sub(r"([A-Z])", lambda m: "-" + m.group(1).lower(), k)), tok(color(v), "color", "Measured",
                f"terminal.{k} = {v} in localStorage['theme-terminal'] (the active theme's terminal palette), {THEME_NAME[t]}, {DATE}"))
    # 5. Tailwind palette steps the interface uses
    for n in sorted(painted):
        if PALETTE.match(n) and is_color(painted[n]):
            d = decl(t, n, ":root, :host", "@layer theme")
            put(tree, ("palette", n[len("--color-"):]), tok(color(painted[n]), "color", "Measured",
                f"{n} = {d['value'] if d else '?'} (Tailwind 4 theme layer in {SHEET}), painted, {DATE}"))
    return tree


SETS = {t: semantic(t) for t in THEMES}


def get(tree, path):
    node = tree
    for k in path.split("."):
        if not isinstance(node, dict) or k not in node:
            return None
        node = node[k]
    return node


def resolve(t, value, depth=0):
    m = re.fullmatch(r"\{([^{}]+)\}", value) if isinstance(value, str) else None
    if not m:
        return value
    node = get(SETS[t], m.group(1)) or get(CORE, m.group(1))
    return resolve(t, node["$value"], depth + 1)


# ---------------------------------------------------------------- measured components

def parts(t):
    """{(part, state): (shot, style)} from the first shot that measured it."""
    out = {}
    for shot, d in C[t].items():
        for part, v in d["parts"].items():
            out.setdefault((part, d["state"]), (shot, v["style"]))
    return out


P = {t: parts(t) for t in THEMES}


def style(t, part, state="default"):
    hit = P[t].get((part, state))
    return hit if hit else (None, None)


def need(t, part, state="default"):
    shot, s = style(t, part, state)
    if not s:
        raise KeyError(f"{part} ({state}) was not measured in {t}")
    return shot, s


# ---------------------------------------------------------------- core

CORE = {}
dark_comp = computed("dark")
src_theme = f"Tailwind 4 theme layer (:root, :host) in {SHEET}, both themes, {DATE}"


def declared(n):
    d = decl("dark", n, ":root, :host", "@layer theme")
    if not d:
        raise KeyError(n)
    if computed("light").get(n) != computed("dark").get(n):
        raise ValueError(f"{n} differs by theme")
    return d["value"]


# Spacing: Tailwind's one unit, and the steps the captured parts use (padding and gap).
unit = rem(declared("--spacing"))
put(CORE, ("spacing", "unit"), tok(unit, "dimension", "Measured", f"--spacing = {declared('--spacing')} ({src_theme}); every p-*, m-*, gap-* is calc(var(--spacing) * n)"))
steps = {}
for t in THEMES:
    for (part, state), (shot, s) in P[t].items():
        for prop in ("padding-left", "padding-right", "padding-top", "gap"):
            v = s.get(prop, "")
            if re.fullmatch(r"\d+px", v) and v != "0px":
                steps.setdefault(int(v[:-2]), set()).add(part)
for n in sorted(steps):
    if n % 2 == 0 and n <= 48 and len(steps[n]) >= 2:
        put(CORE, ("spacing", "%g" % (n / 4)), tok(f"{n}px", "dimension", "Measured",
            f"{n / 4:g} x the 4px unit; padding or gap of {len(steps[n])} captured parts (e.g. {', '.join(sorted(steps[n])[:3])}), {DATE}"))

# Radius: --radius (shadcn's base, 10px) and Tailwind's declared steps, with the radii the parts paint.
radii = {}
for t in THEMES:
    for (part, state), (shot, s) in P[t].items():
        v = s.get("border-top-left-radius", "")
        if re.fullmatch(r"[\d.e+]+px", v) and v != "0px":
            radii.setdefault(px(v), set()).add(part)
RADIUS = [("xs", "2px", "--radius-xs"), ("sm", "4px", None), ("md", "6px", None), ("base", "8px", None), ("lg", "10px", "--radius"),
          ("2xl", "16px", "--radius-2xl"), ("full", "9999px", None)]
for key, v, name in RADIUS:
    used = sorted(radii.get(v, set()))
    if name == "--radius":
        why = f"--radius = .625rem on :root ({SHEET}), shadcn's base radius; painted by {', '.join(used[:4])}"
    elif name:
        why = f"{name} = {declared(name)} ({src_theme}); painted by {', '.join(used[:4]) or 'no captured part'}"
    else:
        why = f"border-radius painted by {len(used)} captured parts ({', '.join(used[:4])}); Tailwind's rounded-*, shadcn's calc(var(--radius) - n) steps inlined in the utilities"
    if not used and not name:
        continue
    put(CORE, ("radius", key), tok(v, "dimension", "Measured", why + f", {DATE}"))

# Type: families, the declared size scale with its line heights, weights, tracking, leading, and
# the 10, 11 and 13px sizes the chrome uses as arbitrary values (text-[13px]).
for key, n in (("sans", "--font-sans"), ("mono", "--font-mono")):
    stack = [f.strip().strip("'\"") for f in declared(n).split(",")]
    put(CORE, ("fontFamily", key), tok(stack, "fontFamily", "Measured", f"{n} ({src_theme})"))
shot, s = need("dark", "terminal")
put(CORE, ("fontFamily", "terminal"), tok([f.strip().strip("'\"") for f in s["font-family"].split(",")], "fontFamily", "Measured",
    f"computed font-family of .xterm in {shot}: Settings > Appearance > Terminal typography (the default, not changed by the owner), {DATE}"))
for n in sorted(dark_comp):
    m = re.fullmatch(r"--text-(\w+)", n)
    if m:
        size = rem(declared(n))
        put(CORE, ("fontSize", m.group(1)), tok(size, "dimension", "Derived", f"{n} = {declared(n)} ({src_theme}) x 16px"))
        lh = declared(n + "--line-height")
        a, b = re.fullmatch(r"calc\(([\d.]+) / ([\d.]+)\)", lh).groups()
        put(CORE, ("lineHeight", m.group(1)), tok(px("%gpx" % (float(a) * 16)), "dimension", "Derived", f"{n}--line-height = {lh} ({src_theme}), x {size}"))
for key, v, part in (("2xs", "10px", "section-label"), ("xs-ui", "11px", "agent-select"), ("ui", "13px", "sidebar-row")):
    shot, s = need("dark", part)
    assert s["font-size"] == v, (part, s["font-size"])
    put(CORE, ("fontSize", key), tok(v, "dimension", "Measured", f"computed font-size of {part} in {shot} (an arbitrary text-[{v}] value), {DATE}"))
for n in sorted(dark_comp):
    m = re.fullmatch(r"--font-weight-(\w+)", n)
    if m:
        put(CORE, ("fontWeight", m.group(1)), tok(int(declared(n)), "fontWeight", "Measured", f"{n} ({src_theme})"))
    m = re.fullmatch(r"--tracking-(\w+)", n)
    if m:
        put(CORE, ("letterSpacing", m.group(1)), tok(float(declared(n).replace("em", "")), "number", "Measured", f"{n} = {declared(n)} ({src_theme})", unit="em"))
    m = re.fullmatch(r"--leading-(\w+)", n)
    if m:
        put(CORE, ("leading", m.group(1)), tok(float(declared(n)), "number", "Measured", f"{n} = {declared(n)} ({src_theme}), a multiple of the font size"))

# Type roles, measured on real elements (computed style, dark).
ROLES = [("display", "heading", "the New Workspace page's heading (What should we build next?)"),
         ("page-title", "page-title", "page titles (Pages, Plugins, Settings panes)"),
         ("title", "title-select", "the Workspaces board title (This device)"),
         ("body", "menu-row", "menu rows, options, list text"),
         ("ui", "sidebar-row", "sidebar rows and settings navigation"),
         ("label", "field-label", "form labels and small buttons"),
         ("button", "button-primary", "button labels"),
         ("caption", "agent-select", "composer chips and footer selects"),
         ("overline", "section-label", "sidebar section labels (SESSIONS, PROJECTS), uppercase"),
         ("code", "text-field-mono", "monospace fields (paths)")]
for role, part, use in ROLES:
    shot, s = need("dark", part)
    fam = "{fontFamily.mono}" if role == "code" else "{fontFamily.sans}"
    val = {"fontFamily": fam, "fontSize": px(s["font-size"]), "fontWeight": int(s["font-weight"]),
           "lineHeight": px(s["line-height"]), "letterSpacing": px(s["letter-spacing"]) if s["letter-spacing"].endswith("px") else "0px"}
    put(CORE, ("typography", role), tok(val, "typography", "Measured", f"computed style of {part} in {shot}, dark, {DATE}; {use}",
        textTransform=s["text-transform"] if s["text-transform"] != "none" else None))

# Motion
put(CORE, ("duration", "default"), tok(ms(declared("--default-transition-duration")), "duration", "Measured", f"--default-transition-duration ({src_theme})"))
durs = {}
for (part, state), (shot, s) in P["dark"].items():
    for v in s.get("transition-duration", "").split(","):
        v = v.strip()
        if v and v != "0s":
            durs.setdefault(ms(v), set()).add(part)
for v in sorted(durs, key=lambda x: float(x[:-2])):
    if v != "150ms":
        put(CORE, ("duration", v.replace("ms", "")), tok(v, "duration", "Measured", f"transition-duration of {', '.join(sorted(durs[v])[:3])} (computed), {DATE}"))
put(CORE, ("easing", "default"), tok(bezier(declared("--default-transition-timing-function")), "cubicBezier", "Measured",
    f"--default-transition-timing-function ({src_theme})", css=declared("--default-transition-timing-function")))
for key in ("out", "in-out"):
    n = f"--ease-{key}"
    put(CORE, ("easing", key), tok(bezier(declared(n)), "cubicBezier", "Measured", f"{n} ({src_theme})", css=declared(n)))

# Focus ring: shadcn's 3px box-shadow ring in --ring at 50%, measured on a focused button.
shot, s = need("dark", "button-primary", "focus-visible")
ring = [l for l in shadow(s["box-shadow"]) if l["spread"] != "0px" and not l["color"].endswith(", 0)")][0]
put(CORE, ("focusRing", "width"), tok(ring["spread"], "dimension", "Measured", f"box-shadow spread of button-primary in {shot} (ring-[3px]), {DATE}"))
put(CORE, ("focusRing", "offset"), tok("0px", "dimension", "Measured", f"the ring is a box-shadow at offset 0 ({shot}), {DATE}"))

# Sizes, layout, layers: measured boxes.
def dim_of(part, prop, state="default", t="dark"):
    shot, s = style(t, part, state)
    return (shot, s[prop]) if s and s.get(prop, "").endswith("px") else (None, None)


SIZES = [("controlHeight.xs", "agent-select", "height", "composer chips (agent, model, effort)"),
         ("controlHeight.sm", "icon-button", "height", "icon buttons, preset buttons, run button"),
         ("controlHeight.md", "sidebar-row", "height", "sidebar rows, small buttons, menu-adjacent controls"),
         ("controlHeight.base", "select-trigger", "height", "selects, search fields, toolbar buttons"),
         ("controlHeight.lg", "text-field", "height", "text fields and dialog buttons"),
         ("size.control.menu-row", "menu-row", "height", "menu and option rows"),
         ("size.control.palette-row", "palette-row", "height", "search palette rows"),
         ("size.control.table-row", "table-row", "height", "table rows (Organization members)"),
         ("size.control.switch-width", "switch-on", "width", "switch"),
         ("size.control.switch-height", "switch-on", "height", "switch"),
         ("size.control.tab-height", "tab", "height", "workspace tab strip"),
         ("size.control.pane-header", "pane-header", "height", "pane header in a workspace"),
         ("layout.sidebar", "sidebar", "width", "main sidebar"),
         ("layout.composer", "composer", "width", "composer on the New Workspace page"),
         ("layout.dialog", "dialog", "width", "Create a new project dialog"),
         ("layout.confirm-dialog", "confirm-dialog", "width", "delete confirmation"),
         ("layout.palette", "palette", "width", "search palette"),
         ("layout.board-column", "board-column", "width", "Workspaces board column"),
         ("layout.setup-card", "setup-card", "width", "sidebar setup card")]
for path, part, prop, use in SIZES:
    shot, v = dim_of(part, prop)
    if v:
        put(CORE, tuple(path.split(".")), tok(px("%gpx" % round(float(v[:-2]))), "dimension", "Measured",
            f"computed {prop} of {part} in {shot}, dark, {DATE} ({use}); {v} before rounding"))
shot, s = need("dark", "panel-tab-selected")
WINDOW = C["dark"]["home-default"]["viewport"]
put(CORE, ("layout", "window-width"), tok(f"{WINDOW['css'][0]}px", "dimension", "Measured",
    f"the window's viewport, {WINDOW['css'][0]} x {WINDOW['css'][1]} CSS px at devicePixelRatio {WINDOW['dpr']} (the window maximised on the built-in display), {DATE}"))
put(CORE, ("layout", "window-height"), tok(f"{WINDOW['css'][1]}px", "dimension", "Measured", f"the window's viewport height, {DATE}"))
shot, s = need("dark", "panel-tab-selected")
put(CORE, ("layout", "right-panel"), tok("340px", "dimension", "Measured",
    f"the workspace's right panel (Files, Changes, Review), 339 to 340px from the boxes of its tabs in {shot}, {DATE}"))
shot, s = need("dark", "menu")
put(CORE, ("zIndex", "overlay"), tok(int(s["z-index"]), "number", "Measured", f"computed z-index of menus, popovers, dialogs (z-50), e.g. menu in {shot}, {DATE}"))
put(CORE, ("borderWidth", "hairline"), tok("1px", "dimension", "Measured", f"border-top-width of menus, dialogs, fields and cards, {DATE}"))
shot, s = need("dark", "agent-select")
put(CORE, ("borderWidth", "chip"), tok(px(s["border-top-width"]), "dimension", "Measured", f"border-top-width of agent-select in {shot}: a half-pixel edge on the composer's chips, {DATE}"))
put(CORE, ("blur", "sm"), tok(px(declared("--blur-sm")), "dimension", "Measured", f"--blur-sm ({src_theme})"))

# reduced motion and breakpoints, summarised from the stylesheets' conditions
cond = V["dark"]["conditions"]
CORE["duration"]["$extensions"] = {"reducedMotion": {
    "rules": {k: v["rules"] for k, v in cond.items() if "reduced-motion" in k},
    "how": "Tailwind's motion-reduce / motion-safe variants under (prefers-reduced-motion); Superset has no setting of its own"}}
CORE["layout"]["$extensions"] = {"breakpointsInCss": sorted({k for k in cond if re.search(r"width", k)}),
    "note": "Tailwind's sm/md/lg/xl/2xl (40, 48, 64, 80, 96rem) and container queries on panes (pane-header, strip, detail, topbar); the window is resizable and the layout is fixed panes, not a breakpoint grid"}

# ---------------------------------------------------------------- roles and components, per theme

ROLE = {
    "page": ("{ui.background}", "the main pane and the workspace's panes"),
    "surface": ("{ui.sidebar}", "the sidebar"),
    "raised": ("{ui.card}", "the composer, setup card, menus"),
    "overlay": ("{ui.popover}", "menus, popovers and listboxes"),
    "scrim": (None, "scrim", "dialog overlay"),
    "text.primary": ("{ui.foreground}", ""), "text.secondary": ("{ui.muted-foreground}", ""),
    "text.on-accent": ("{ui.primary-foreground}", ""), "text.link": ("{link.default}", ""),
    "border.default": ("{ui.border}", "menus, dialogs, fields, cards"), "border.strong": ("{ui.ring}", "Superset has no stronger edge than --ring"),
    "border.focus": ("{ui.ring}", "the 3px focus ring is --ring at 50%"),
    "accent.default": ("{ui.primary}", "the ink button: Superset's primary action is the foreground colour, not a hue"),
    "accent.subtle": ("{ui.accent}", ""),
    "brand": ("{ui.highlight}", "the ember orange (search matches, the running cursor in the terminal)"),
    "status.success.fill": ("{ui.success}", ""), "status.success.text": ("{ui.success}", ""),
    "status.warning.fill": ("{ui.warning}", ""), "status.warning.text": ("{ui.warning-foreground}", "text on the warning fill"),
    "status.danger.fill": ("{ui.destructive}", ""), "status.danger.text": ("{ui.destructive-foreground}", "text on the destructive fill"),
    "status.info.fill": ("{link.default}", "Superset has no info status; the link blue is used for it"),
    "status.info.text": ("{link.default}", ""),
    "status.running": ("{palette.amber-500}", "the dot on a tab whose agent is working"),
}


def index(t):
    idx = {}

    def walk(node, path):
        for k, v in node.items():
            if k.startswith("$"):
                continue
            if isinstance(v, dict) and "$value" in v:
                if v["$type"] == "color":
                    idx.setdefault(resolve(t, v["$value"]), []).append(".".join(path + [k]))
            elif isinstance(v, dict):
                walk(v, path + [k])
    walk(SETS[t], [])
    PREFER = ["ui", "link", "palette", "role", "terminal", "syntax"]
    for vals in idx.values():
        vals.sort(key=lambda p: (PREFER.index(p.split(".")[0]) if p.split(".")[0] in PREFER else 99, len(p), p))
    return idx


# component tokens: (name, part, {key: css property}); value aliased when it equals a token
COMPONENTS = [
    ("button-primary", "button-primary", {"bg": "background-color", "text": "color", "radius": "border-top-left-radius", "height": "height", "padding": "padding-left"}),
    ("button-primary-sm", "button-primary-sm", {"bg": "background-color", "text": "color", "height": "height", "padding": "padding-left"}),
    ("button-secondary", "button-secondary", {"bg": "background-color", "border": "border-top-color", "text": "color", "radius": "border-top-left-radius", "height": "height"}),
    ("button-ghost", "button-ghost", {"text": "color", "radius": "border-top-left-radius", "height": "height", "padding": "padding-left"}),
    ("button-destructive", "button-destructive", {"bg": "background-color", "text": "color", "radius": "border-top-left-radius", "height": "height"}),
    ("icon-button", "icon-button", {"text": "color", "radius": "border-top-left-radius", "size": "height"}),
    ("sidebar-row", "sidebar-row", {"text": "color", "radius": "border-top-left-radius", "height": "height", "padding": "padding-left"}),
    ("sidebar-row-selected", "sidebar-row-selected", {"bg": "background-color", "text": "color"}),
    ("workspace-row-selected", "workspace-row-selected", {"bg": "background-color", "text": "color"}),
    ("composer", "composer", {"bg": "background-color", "radius": "border-top-left-radius", "width": "width"}),
    ("chip", "agent-select", {"bg": "background-color", "border": "border-top-color", "text": "color", "radius": "border-top-left-radius", "height": "height"}),
    ("menu", "menu", {"bg": "background-color", "border": "border-top-color", "text": "color", "radius": "border-top-left-radius", "padding": "padding-left"}),
    ("menu-row", "menu-row", {"text": "color", "radius": "border-top-left-radius", "height": "height", "padding": "padding-left"}),
    ("option-selected", "option-selected", {"bg": "background-color", "text": "color"}),
    ("dialog", "dialog", {"bg": "background-color", "border": "border-top-color", "radius": "border-top-left-radius", "padding": "padding-left", "width": "width"}),
    ("palette", "palette", {"bg": "background-color", "border": "border-top-color", "radius": "border-top-left-radius"}),
    ("palette-row-selected", "palette-row-selected", {"bg": "background-color", "text": "color"}),
    ("scrim", "scrim", {"bg": "background-color"}),
    ("text-field", "text-field", {"border": "border-top-color", "text": "color", "radius": "border-top-left-radius", "height": "height", "padding": "padding-left"}),
    ("search-field", "settings-search", {"bg": "background-color", "text": "color", "radius": "border-top-left-radius", "height": "height"}),
    ("select", "select-trigger", {"border": "border-top-color", "text": "color", "radius": "border-top-left-radius", "height": "height"}),
    ("switch-on", "switch-on", {"bg": "background-color", "width": "width"}),
    ("switch-off", "switch-off", {"bg": "background-color"}),
    ("segmented", "segmented", {"bg": "background-color", "radius": "border-top-left-radius", "padding": "padding-left"}),
    ("segment-selected", "segment-selected", {"bg": "background-color", "text": "color", "radius": "border-top-left-radius"}),
    ("tab", "tab", {"text": "color", "radius": "border-top-left-radius", "height": "height"}),
    ("panel-tab-selected", "panel-tab-selected", {"bg": "background-color", "text": "color"}),
    ("pane-header", "pane-header", {"bg": "background-color", "height": "height"}),
    ("card", "setup-card", {"bg": "background-color", "border": "border-top-color", "radius": "border-top-left-radius", "padding": "padding-left"}),
    ("badge", "badge", {"border": "border-top-color", "text": "color", "radius": "border-top-left-radius", "height": "height"}),
    ("badge-solid", "badge-pro", {"bg": "background-color", "text": "color", "height": "height"}),
    ("tooltip", "tooltip", {"bg": "background-color", "text": "color", "radius": "border-top-left-radius"}),
    ("toast", "toast", {"bg": "background-color", "border": "border-top-color", "text": "color", "radius": "border-top-left-radius"}),
    ("table-row", "table-row", {"height": "height"}),
]
# When one painted colour is several tokens, the name a reader expects for that property wins.
PREF_BY_PROP = {
    "color": ["ui.foreground", "ui.muted-foreground", "ui.primary-foreground", "ui.destructive-foreground", "palette.white"],
    "background-color": ["ui.background", "ui.card", "ui.popover", "ui.accent", "ui.muted", "ui.secondary", "ui.primary", "ui.fill-hover", "ui.fill-selected"],
    "border-top-color": ["ui.border", "ui.input", "ui.ring"],
}
STATES = [("hover", "bg-hover", "background-color"), ("hover", "text-hover", "color"), ("pressed", "bg-pressed", "background-color")]


def build_roles_and_components(t):
    tree = SETS[t]
    for key, spec in ROLE.items():
        if spec[0] is None:
            state = "error" if spec[1] == "toast" else "default"
            shot, s = need(t, spec[1], state)
            put(tree, ("role",) + tuple(key.split(".")), tok(color(s["background-color"]), "color", "Measured",
                f"background-color of {spec[1]} in {shot}, {THEME_NAME[t]}, {DATE}; {spec[2]}"))
            continue
        target = spec[0][1:-1]
        if get(tree, target) is None:
            raise KeyError(f"role.{key}: {target} missing in {t}")
        put(tree, ("role",) + tuple(key.split(".")), tok(spec[0], "color", "Derived", f"the checklist role, mapped to {target}" + (f"; {spec[1]}" if spec[1] else "")))
    # Accent hover and pressed: the ink button's own fill under the pointer and pressed (bg-primary/90).
    for key, state in (("hover", "hover"), ("pressed", "pressed")):
        shot, s = need(t, "button-primary", state)
        put(tree, ("role", "accent", key), tok(color(s["background-color"]), "color", "Measured",
            f"background-color of button-primary in {shot} ({state}), {THEME_NAME[t]}, {DATE}; bg-primary/90"))
    # Disabled text: disabled controls are drawn at opacity 0.5 (disabled:opacity-50).
    shot, s = need(t, "textarea")
    fg = resolve(t, "{ui.foreground}")
    r, g, b = (int(fg[i:i + 2], 16) for i in (1, 3, 5))
    put(tree, ("role", "text", "disabled"), tok(f"rgba({r}, {g}, {b}, 0.5)", "color", "Derived",
        f"ui.foreground at the opacity 0.5 disabled controls are drawn at (computed opacity of the disabled textarea in {shot}; disabled:opacity-50), {THEME_NAME[t]}"))
    # Focus ring colour as painted.
    shot, s = need(t, "button-primary", "focus-visible")
    ring = [l for l in shadow(s["box-shadow"]) if l["spread"] != "0px" and not l["color"].endswith(", 0)")][0]
    put(tree, ("focus", "ring"), tok(ring["color"], "color", "Measured", f"box-shadow colour of button-primary in {shot} (ring-ring/50), {THEME_NAME[t]}, {DATE}"))
    idx = index(t)
    measured_n = aliased_n = 0

    def value_for(part, shot, prop, raw):
        nonlocal measured_n, aliased_n
        src = f"computed {prop} of {part} in {shot}, {THEME_NAME[t]}, {DATE}"
        if prop in ("background-color", "color", "border-top-color"):
            v = color(raw)
            measured_n += 1
            if v in idx:
                aliased_n += 1
                rank = PREF_BY_PROP[prop]
                best = sorted(idx[v], key=lambda x: rank.index(x) if x in rank else len(rank))[0]
                return tok("{%s}" % best, "color", "Measured", src, painted=v)
            return tok(v, "color", "Measured", src)
        v = px(raw) if raw.endswith("px") else raw
        if re.fullmatch(r"[\d.]+px", v):
            v = px("%gpx" % round(float(v[:-2])))
        return tok(v, "dimension", "Measured", src + f" ({raw})")
    for name, part, props in COMPONENTS:
        state = "error" if part == "toast" else "hover" if part == "tooltip" else "default"
        shot, s = style(t, part, state)
        if not s:
            continue
        for key, prop in props.items():
            raw = s[prop]
            if prop in ("background-color", "border-top-color") and color(raw) == "rgba(0, 0, 0, 0)":
                continue
            put(tree, ("component", name, key), value_for(part, shot, prop, raw))
        for st, key, prop in STATES:
            sh, ss = style(t, part, st)
            if ss and ss[prop] != s[prop] and color(ss[prop]) != "rgba(0, 0, 0, 0)":
                put(tree, ("component", name, key), value_for(part, sh, prop, ss[prop]))
    tree["$extensions"] = {"componentValues": {"measured": measured_n, "aliased": aliased_n}}


# Shadows: Tailwind's shadow-xs, sm, md, lg and Sonner's toast shadow, each read off a part that paints it
# (the transparent ring layers Tailwind stacks in front are dropped).
SHADOWS = [("xs", "text-field", "default", "fields, outline buttons, switches (shadow-xs)"),
           ("sm", "segment-selected", "default", "the selected segment, tooltips (shadow-sm)"),
           ("md", "menu", "default", "menus, popovers, listboxes (shadow-md)"),
           ("lg", "dialog", "default", "dialogs and the search palette (shadow-lg)"),
           ("toast", "toast", "error", "toasts (Sonner)")]


def build_shadows(t):
    for key, part, state, use in SHADOWS:
        shot, s = need(t, part, state)
        layers = [l for l in shadow(s["box-shadow"]) if not l["color"].endswith(", 0)")]
        uses = sorted({p for (p, st), (sh, ss) in P[t].items() if st == "default" and
                       [l for l in shadow(ss["box-shadow"]) if not l["color"].endswith(", 0)")] == layers})
        put(SETS[t], ("shadow", key), tok(layers, "shadow", "Measured", f"box-shadow of {part} in {shot}, {THEME_NAME[t]}, {DATE}; {use}",
            usedBy=uses or [part]))


for t in THEMES:
    build_roles_and_components(t)
    build_shadows(t)

# ---------------------------------------------------------------- checks


def tokens_of(tree, prefix=""):
    for k, v in tree.items():
        if k.startswith("$"):
            continue
        if isinstance(v, dict) and "$value" in v:
            yield prefix + k, v
        elif isinstance(v, dict):
            yield from tokens_of(v, prefix + k + ".")


def aliases(v):
    if isinstance(v, str):
        return re.findall(r"\{([^{}]+)\}", v)
    if isinstance(v, dict):
        return [a for x in v.values() for a in aliases(x)]
    if isinstance(v, list):
        return [a for x in v for a in aliases(x)]
    return []


def check():
    core_names = dict(tokens_of(CORE))
    for setname, tree in [("core", CORE)] + [(t, SETS[t]) for t in THEMES]:
        names = dict(core_names)
        names.update(dict(tokens_of(tree)))
        for n, t in tokens_of(tree):
            if not (t.get("$extensions") or {}).get("source"):
                raise ValueError(f"{setname}.{n}: no source")
            for a in aliases(t["$value"]):
                if a not in names:
                    raise KeyError(f"{setname}.{n}: alias {{{a}}} points at nothing")
                if t["$type"] in ("color", "dimension") and names[a]["$type"] != t["$type"]:
                    raise TypeError(f"{setname}.{n}: alias {{{a}}} is a {names[a]['$type']}")
            if t["$type"] == "dimension" and not aliases(t["$value"]) and not re.fullmatch(r"-?\d*\.?\d+(px|rem)", t["$value"]):
                raise ValueError(f"{setname}.{n}: dimension {t['$value']!r}")
            if t["$type"] == "color" and not aliases(t["$value"]) and not re.fullmatch(r"#[0-9a-f]{6}|rgba\(\d+, \d+, \d+, [\d.]+\)", t["$value"]):
                raise ValueError(f"{setname}.{n}: colour {t['$value']!r}")


def reconcile():
    """A name present in only one theme's readings is not a theme token: move it out."""
    names = {t: {n for n, _ in tokens_of(SETS[t])} for t in THEMES}
    for t in THEMES:
        other = names["dark" if t == "light" else "light"]
        for n in sorted(names[t] - other):
            path = n.split(".")
            node = SETS[t]
            for k in path[:-1]:
                node = node[k]
            v = node.pop(path[-1])
            SETS[t].setdefault("$extensions", {}).setdefault("notTokenised", []).append(
                {"name": n, "value": v["$value"], "why": f"read only while capturing {t}; not in the other theme"})


reconcile()
check()
tokens = {
    "core": CORE, "light": SETS["light"], "dark": SETS["dark"],
    "$themes": [
        {"id": "light", "name": "Light", "selectedTokenSets": {"core": "source", "light": "enabled"},
         "$description": "Settings > Appearance > Theme: Light (html.light; the built-in `light` theme)"},
        {"id": "dark", "name": "Dark", "selectedTokenSets": {"core": "source", "dark": "enabled"},
         "$description": "Settings > Appearance > Theme: Dark (html.dark; the built-in `dark` theme, Superset's default)"},
    ],
    "$metadata": {"tokenSetOrder": ["core", "light", "dark"]},
}
(PKG / "tokens.json").write_text(json.dumps(tokens, indent=2, ensure_ascii=False) + "\n")


def count(d):
    return sum(1 for _ in tokens_of(d))


print({k: count(tokens[k]) for k in ("core", "light", "dark")}, "component values aliased:",
      {t: SETS[t]["$extensions"]["componentValues"] for t in THEMES})
