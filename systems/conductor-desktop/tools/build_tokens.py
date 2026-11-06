#!/usr/bin/env python3
"""Build tokens.json (W3C DTCG, Tokens Studio multi-set layout) from the raw readings.

    python3 tools/build_tokens.py

Sources, read live from Conductor 0.91.2 for macOS on 2026-10-25 through Safari's Web Inspector on the
app's WKWebView (tools/capture/inspector/):
  raw/css-vars.<theme>.json      every custom property the page's stylesheets declare, by sheet, selector
                                 and condition, each name as it computes and paints on <body>, the inline
                                 custom properties the app writes on <html> (fonts, code colours), the
                                 stylesheets' @media conditions and the loaded font faces
  raw/components.<theme>.json    computed styles and boxes of the captured parts, per shot and state

How Conductor's colours work, and so how this file is laid out. Conductor's web view is React with
Tailwind CSS 4 and Base UI. Tailwind's theme (`:root, :host` in @layer theme) carries a palette that is
the same in both themes: Tailwind's hues as oklch, and Conductor's own warm grey ramp (--color-gray-0 to
-900, hex), which goes to core as color.*. The theme is shadcn-shaped names declared as hex on
`:root, .light` and `.dark` (background, foreground, card, popover, primary, secondary, muted, accent,
destructive, border, input, ring), plus Conductor's own groups (sidebar, git, status, terminal, tip,
todo, warning, highlight, link). The app writes the code-highlighting colours and the font stacks inline
on <html> from the Code theme and font settings. role.* maps the checklist roles onto those tokens, and
component.* holds measured component values, aliased to a token whenever the painted value matches.

Every token carries $extensions.source = {evidence, from}. Deterministic: same inputs, same bytes.
"""
import json
import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from colour import bezier, color, is_color, ms, px, shadow  # noqa: E402
from prefer import skip  # noqa: E402

PKG = pathlib.Path(__file__).resolve().parent.parent
RAW = PKG / "raw"
THEMES = ["light", "dark"]
DATE = "2026-10-25"

# ---------------------------------------------------------------- PRODUCT (adapt): what the readings are

THEME_SELECTOR = {"light": ":root, .light", "dark": ".dark"}
THEME_NAME = {"light": "Light (html.light, Settings > Appearance > Theme: Light)",
              "dark": "Dark (html.dark, Settings > Appearance > Theme: Dark, the owner's setting)"}
# name prefix -> token group; names without one go to `base` (the shadcn-shaped names).
GROUPS = [("--color-", None), ("--sidebar-", "sidebar"), ("--git-", "git"), ("--status-", "status"), ("--terminal-", "terminal"),
          ("--tip-", "tip"), ("--todo-", "todo"), ("--warning-", "warning"), ("--warning", "warning"), ("--highlight-", "highlight"),
          ("--highlight", "highlight"), ("--link-", "link"), ("--link", "link"), ("--code-", "code"), ("--checks-", "checks"),
          ("--", "base")]
LOW_CONTRAST = "html.dark.low-contrast-dark"


def load(name):
    return json.loads((RAW / name).read_text())


V = {t: load(f"css-vars.{t}.json") for t in THEMES}
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


def get(tree, path):
    node = tree
    for k in path.split("."):
        if not isinstance(node, dict) or k not in node:
            return None
        node = node[k]
    return node


def computed(t):
    return V[t]["computed"][V[t]["scope"]]


def rem(v):
    """A Tailwind length (rem, px, calc(<rem> - <px>)) -> px string."""
    v = v.strip()
    m = re.fullmatch(r"calc\(\s*([\d.]+)rem\s*-\s*([\d.]+)px\s*\)", v)
    if m:
        return px("%gpx" % (float(m.group(1)) * 16 - float(m.group(2))))
    m = re.fullmatch(r"(-?[\d.]+)rem", v)
    if m:
        return px("%gpx" % (float(m.group(1)) * 16))
    if re.fullmatch(r"-?[\d.]+em", v):
        return ("0" + v) if v.startswith(".") else v.replace("-.", "-0.")
    return px(v)


def theme_decl(t, name):
    """The value `name` is declared with in theme t's own selector, or None."""
    for d in V[t]["decls"]:
        if d["name"] == name and d["selector"] == THEME_SELECTOR[t] and not d["condition"]:
            return d["value"]
    return None


def path_of(name):
    for pre, group in GROUPS:
        if name.startswith(pre):
            rest = name[len(pre):]
            if group is None:          # --color-gray-500 -> core color.gray.500
                hue, _, step = rest.rpartition("-")
                return ("color", hue, step) if hue else ("color", rest)
            return (group, rest or "default")
    raise KeyError(name)


def where(t, name, extra=""):
    return f"{name} as painted on <body>, {THEME_NAME[t]}, {DATE}{extra}"


# ---------------------------------------------------------------- core: the palette and the scales

CORE = {}
dark_comp, light_comp = computed("dark"), computed("light")
for n in sorted(dark_comp):
    if not n.startswith("--color-"):
        continue
    decl = [d["value"] for d in V["dark"]["decls"] if d["name"] == n and d["selector"] == ":root, :host"]
    if not decl or decl[0].startswith("var("):
        continue                       # --color-background: var(--background) and the like are the theme's names
    pc, pl = V["dark"]["colors"].get(n), V["light"]["colors"].get(n)
    if not pc or not is_color(pc) or color(pc) != color(pl):
        raise ValueError(f"{n} differs by theme or is not a colour")
    put(CORE, path_of(n), tok(color(pc), "color", "Measured",
        f"{n} as painted ({'Conductor' + chr(39) + 's warm grey ramp' if '-gray-' in n else 'Tailwind' + chr(39) + 's palette as Conductor loads it'}; both themes), {DATE}",
        declared=decl[0]))


def core_dim(group, key, name, conv=rem, ty="dimension", **ext):
    v = dark_comp[name]
    if light_comp.get(name) != v:
        raise ValueError(f"{name} differs by theme")
    put(CORE, (group, key), tok(conv(v), ty, "Measured", f"{name} on <body>, both themes, {DATE}", css=v, **ext))


for key, n in (("xs", "--radius-xs"), ("md", "--radius-md"), ("lg", "--radius"), ("xl", "--radius-xl"), ("2xl", "--radius-2xl"), ("3xl", "--radius-3xl")):
    core_dim("radius", key, n)
put(CORE, ("radius", "sm"), tok("4px", "dimension", "Measured", f"computed border-radius of rounded-sm parts (the repository icon tile, the tool argument chip), {DATE}"))
put(CORE, ("radius", "full"), tok("9999px", "dimension", "Measured", f"rounded-full on switches, the focus hint and the send button (computed 9999px or 50%), {DATE}"))
core_dim("spacing", "unit", "--spacing")
for n in (0.5, 1, 1.5, 2, 2.5, 3, 4, 5, 6, 8, 10, 12, 16):
    put(CORE, ("spacing", ("%g" % n).replace(".", "-")), tok(px("%gpx" % (4 * n)), "dimension", "Derived",
        f"calc(var(--spacing) * {n:g}), Tailwind's spacing class {n:g}", formula=f"calc(var(--spacing) * {n:g})"))
SIZES = ("3xs", "2xs", "xs", "sm", "md", "base", "lg", "xl", "2xl", "3xl", "4xl", "5xl")
for key in SIZES:
    core_dim("fontSize", key, f"--text-{key}")
    lh = dark_comp[f"--text-{key}--line-height"]
    lhpx = rem(lh) if lh.endswith("rem") else px("%gpx" % (float(lh) * float(rem(dark_comp[f'--text-{key}'])[:-2])))
    put(CORE, ("lineHeight", key), tok(lhpx, "dimension", "Measured", f"--text-{key}--line-height on <body> ({lh}), {DATE}", css=lh))
    ls = dark_comp.get(f"--text-{key}--letter-spacing")
    if ls:
        put(CORE, ("letterSpacing", key), tok(rem(ls), "dimension", "Measured", f"--text-{key}--letter-spacing on <body>, {DATE}", css=ls))
for key in ("extralight", "normal", "450", "medium", "semibold", "bold"):
    core_dim("fontWeight", key, f"--font-weight-{key}", conv=int, ty="fontWeight")
for key in ("tight", "snug", "normal", "relaxed"):
    core_dim("leading", key, f"--leading-{key}", conv=float, ty="number")
for key in ("tight", "normal", "wide", "wider", "widest"):
    core_dim("tracking", key, f"--tracking-{key}")
for key, n in (("sans", "--font-sans"), ("mono", "--font-mono")):
    stack = [f.strip().strip("'\"") for f in dark_comp[n].split(",")]
    put(CORE, ("fontFamily", key), tok(stack, "fontFamily", "Measured",
        f"{n} on <body>, written inline on <html> by the app (the stylesheet's own default is "
        f"{'SF Pro' if key == 'sans' else 'Geist Mono'}); Geist and Geist Mono are loaded as web fonts, {DATE}"))
put(CORE, ("duration", "default"), tok(ms(dark_comp["--default-transition-duration"]), "duration", "Measured", f"--default-transition-duration on <body>, {DATE}"))
put(CORE, ("duration", "fast"), tok("150ms", "duration", "Measured", f"transition-duration of buttons, rows and tabs (duration-150), {DATE}"))
put(CORE, ("duration", "overlay"), tok("200ms", "duration", "Measured", f"the dialog backdrop's transition-opacity duration-200, {DATE}"))
for key, n in (("default", "--default-transition-timing-function"), ("in", "--ease-in"), ("out", "--ease-out"), ("in-out", "--ease-in-out")):
    put(CORE, ("easing", key), tok(bezier(dark_comp[n]), "cubicBezier", "Measured", f"{n} on <body>, {DATE}", css=dark_comp[n]))
for key in ("xs", "sm", "md", "xl"):
    core_dim("blur", key, f"--blur-{key}")
for key in ("xs", "sm", "md", "lg", "xl", "2xl", "3xl", "4xl", "5xl", "6xl", "7xl"):
    core_dim("container", key, f"--container-{key}")

# ---------------------------------------------------------------- semantic sets


def theme_names(t):
    names = {d["name"] for d in V[t]["decls"] if d["selector"] == THEME_SELECTOR[t] and not d["condition"]}
    names |= {n for n in V[t]["htmlInline"] if n.startswith("--code-")}
    return sorted(names - {"--radius"})


def semantic(t):
    tree, painted = {}, V[t]["colors"]
    for n in theme_names(t):
        if n not in painted or not is_color(painted[n]):
            continue
        value = color(painted[n])
        f = theme_decl(t, n) or V[t]["htmlInline"].get(n)
        m = re.fullmatch(r"var\((--[\w-]+)\)", f or "")
        if m and m.group(1) in painted and color(painted[m.group(1)]) == value:
            put(tree, path_of(n), tok("{%s}" % ".".join(path_of(m.group(1))), "color", "Measured", where(t, n), formula=f))
        elif n in V[t]["htmlInline"]:
            put(tree, path_of(n), tok(value, "color", "Measured", f"{n} written inline on <html> by the app for the Code theme Default, {THEME_NAME[t]}, {DATE}"))
        elif f and re.fullmatch(r"#[0-9a-fA-F]{3,8}", f):
            put(tree, path_of(n), tok(value, "color", "Measured", where(t, n, f"; declared {f}")))
        else:
            put(tree, path_of(n), tok(value, "color", "Measured", where(t, n), formula=f))
    return tree


SETS = {t: semantic(t) for t in THEMES}
# Names declared in one theme only (git-selection is light-only) are not theme tokens.
for t in THEMES:
    o = "dark" if t == "light" else "light"
    for g, node in list(SETS[t].items()):
        for k in list(node):
            if (g not in SETS[o]) or (k not in SETS[o][g]):
                v = node.pop(k)
                SETS[t].setdefault("$extensions", {}).setdefault("notTokenised", []).append(
                    {"name": f"{g}.{k}", "value": v["$value"], "why": f"declared in {t} only"})
SETS["dark"]["$extensions"] = SETS["dark"].get("$extensions", {})
SETS["dark"]["$extensions"]["lowContrastDark"] = {
    "selector": LOW_CONTRAST, "how": "Settings > Appearance > Low-contrast dark mode (off for the owner) adds .low-contrast-dark to <html> and overrides these names",
    "values": {d["name"]: d["value"] for d in V["dark"]["decls"] if d["selector"] == LOW_CONTRAST}}


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
            if not skip(shot, part, d["state"]):
                out.setdefault((part, d["state"]), (shot, v["style"]))
    return out


P = {t: parts(t) for t in THEMES}


INTERACTION = ("hover", "focus-visible", "focus", "pressed", "active")


def style(t, part, state="default"):
    if ":" in part:                    # "<shot>:<part>": that shot's reading, for a part name two components share
        shot, part = part.split(":")
        d = C[t].get(shot)
        if d and part in d["parts"] and (state == "default" or d["state"] == state):
            return shot, d["parts"][part]["style"]
        if state != "default":
            return None, None
    hit = P[t].get((part, state))
    if not hit and state == "default":
        # A part read only in a content state (composer-text exists once text is typed) takes that reading;
        # never a hover, focus or pressed one, whose values are the state's, not the part's.
        hit = next((v for (p, s), v in sorted(P[t].items()) if p == part and s not in INTERACTION), None)
    return hit if hit else (None, None)


# Type roles, measured on real elements.
ROLES = [("display", "markdown-h1", "Markdown h1 in the file viewer"),
         ("title", "settings-title", "Settings page titles (h2, text-2xl)"),
         ("heading", "assistant-heading", "Headings in agent replies"),
         ("dialog-title", "dialog-title", "Dialog titles (text-lg)"),
         ("body", "assistant-text", "Agent replies, body text"),
         ("ui", "settings-row-title", "Settings row labels, menu items, list rows (text-sm)"),
         ("body-secondary", "settings-row-description", "Row and page descriptions (muted-foreground)"),
         ("label", "button-outline", "Button labels"),
         ("caption", "panel-tab", "Panel tabs and small controls (text-xs)"),
         ("section", "sidebar-section-label", "Sidebar section labels (text-xs semibold, muted at 70%)"),
         ("prompt", "composer-text", "Text typed in the composer"),
         ("code", "tool-arg", "Mono chips: tool arguments, branch names (Geist Mono, text-xs)"),
         ("file", "tree-label", "File tree labels (Geist Mono, text-xs)"),
         ("diff", "diff-code", "Diff and code views (Geist Mono 13px)")]
for role, part, use in ROLES:
    shot, s = style("dark", part)
    if not s:
        continue
    fam = "{fontFamily.mono}" if "Mono" in s["font-family"] else "{fontFamily.sans}"
    lh = s["line-height"]
    val = {"fontFamily": fam, "fontSize": px(s["font-size"]), "fontWeight": int(s["font-weight"]),
           "lineHeight": px(lh) if lh.endswith("px") else "normal",
           "letterSpacing": px(s["letter-spacing"]) if s["letter-spacing"].endswith("px") else "0px"}
    note = None
    if val["lineHeight"] == "normal":
        val["lineHeight"] = px("%gpx" % round(float(s["font-size"][:-2]) * 1.2, 1))
        note = "computed line-height is normal; 1.2 x the size is used here"
    put(CORE, ("typography", role), tok(val, "typography", "Measured", f"computed style of {part} in {shot}, dark, {DATE}; {use}", note=note))


def dim_of(part, prop, state="default", t="dark"):
    shot, s = style(t, part, state)
    return (shot, s[prop]) if s and s.get(prop, "").endswith("px") else (None, None)


SIZES_M = [("controlHeight.default", "select", "height", "Selects and outline buttons in Settings (h-8)"),
           ("controlHeight.sm", "suggestion-chip", "height", "Suggestion chips and small buttons (h-7)"),
           ("controlHeight.xs", "breadcrumb", "height", "Header controls (h-6)"),
           ("controlHeight.input", "settings-search", "height", "The Settings search field (h-7)"),
           ("size.control.icon-button", "composer-add", "height", "Ghost icon buttons"),
           ("size.control.send", "send-button", "height", "The composer's send button"),
           ("size.control.chat-tab", "chat-tab-selected", "height", "Chat tabs"),
           ("size.control.panel-tab", "panel-tab", "height", "Right panel tabs"),
           ("size.control.nav-row", "sidebar-nav-item", "height", "Sidebar navigation rows"),
           ("size.control.workspace-row", "workspace-row-selected", "height", "Workspace rows"),
           ("size.control.settings-nav", "settings-nav-item", "height", "Settings navigation rows"),
           ("size.control.menu-item", "menu-item", "height", "Menu items"),
           ("size.control.palette-item", "palette-item", "height", "Command palette rows"),
           ("size.control.switch-width", "switch-on", "width", "Switch"),
           ("size.control.switch-height", "switch-on", "height", "Switch"),
           ("size.control.tree-row", "tree-row", "height", "File tree rows"),
           ("layout.sidebar", "sidebar", "width", "Left sidebar"),
           ("layout.composer", "composer", "width", "Composer"),
           ("layout.dialog", "dialog", "width", "Dialogs (max-w-lg)"),
           ("layout.palette", "search-palette:dialog", "width", "Command palette"),
           ("layout.toast", "toast", "width", "Update toast"),
           ("layout.menu", "menu", "width", "Menus")]
for path, part, prop, use in SIZES_M:
    shot, v = dim_of(part, prop)
    if v:
        put(CORE, tuple(path.split(".")), tok(px("%gpx" % round(float(v[:-2]))), "dimension", "Measured",
            f"computed {prop} of {part} in {shot}, dark, {DATE} ({use}); {v} before rounding"))
WINDOW = C["dark"]["workspace"]["viewport"]
put(CORE, ("layout", "window-width"), tok(f"{WINDOW['css'][0]}px", "dimension", "Measured",
    f"the web view's viewport, {WINDOW['css'][0]} x {WINDOW['css'][1]} CSS px at devicePixelRatio {WINDOW['dpr']} (App zoom 100%), {DATE}"))
put(CORE, ("layout", "window-height"), tok(f"{WINDOW['css'][1]}px", "dimension", "Measured", f"the web view's viewport height, {DATE}"))
shot, hb = style("dark", "resize-handle")
if hb:
    left = float(hb["_box"][0]) + float(hb["_box"][2]) / 2
    put(CORE, ("layout", "right-panel"), tok(px("%gpx" % round(WINDOW["css"][0] - left)), "dimension", "Derived",
        f"the window width less the centre of the right panel's resize handle in {shot} ({hb['_box']}), dark, {DATE}: the right panel (files, changes, scripts) as the owner had it; it is resizable"))
put(CORE, ("layout", "traffic-lights-clearance"), tok("66px", "dimension", "Measured", f"--traffic-lights-clearance on <body> (calc(66px / var(--webview-zoom))), the gap left for the macOS window buttons, {DATE}"))
for key, part in (("overlay", "backdrop"), ("dialog", "dialog"), ("menu", "menu"), ("toast", "toast")):
    shot, s = style("dark", part)
    if s and s["z-index"] not in ("auto", ""):
        put(CORE, ("zIndex", key), tok(int(s["z-index"]), "number", "Measured", f"computed z-index of {part} in {shot}, {DATE}"))
put(CORE, ("borderWidth", "default"), tok("1px", "dimension", "Measured", f"border-top-width of cards, inputs, dialogs and the composer, {DATE}"))
# focus ring: focus-visible:ring-2 ring-ring (Tailwind's ring is a box-shadow), read on a focused part
for part in ("switch-on", "chat-tab-selected", "button-outline", "select"):
    shot, s = style("dark", part, "focus-visible")
    if s and s["box-shadow"] != "none":
        layers = [l for l in shadow(s["box-shadow"]) if not l["color"].endswith(", 0)")]
        if not layers:
            continue
        ring = max(layers, key=lambda l: float(l["spread"][:-2]))
        offset = [l for l in layers if l is not ring]
        put(CORE, ("focusRing", "width"), tok(px("%gpx" % (float(ring["spread"][:-2]) - (float(offset[0]["spread"][:-2]) if offset else 0))), "dimension", "Measured",
            f"spread of the focus box-shadow of {part} in {shot}, dark, {DATE}, less the offset layer", css=s["box-shadow"]))
        put(CORE, ("focusRing", "offset"), tok(offset[0]["spread"] if offset else "0px", "dimension", "Measured",
            f"the ring-offset layer of the same box-shadow ({shot}), {DATE}", css=s["box-shadow"]))
        break
put(CORE, ("borderWidth", "focus"), tok("{focusRing.width}", "dimension", "Derived", "the focus ring is a box-shadow of focusRing.width"))

cond = V["dark"]["conditions"]
rm = {k: v["rules"] for k, v in cond.items() if "reduced-motion" in k}
CORE.setdefault("duration", {})["$extensions"] = {"reducedMotion": {"rules": rm,
    "how": "Tailwind's motion-safe: and motion-reduce: variants under (prefers-reduced-motion); no duration token changes"}}
bp = sorted({k for k in cond if re.search(r"width", k)})
CORE.setdefault("layout", {})["$extensions"] = {"breakpointsInCss": bp,
    "note": "Tailwind's sm 40rem to 2xl 96rem plus container queries; the window is resizable and few views use them"}

# ---------------------------------------------------------------- roles and components, per theme

ROLE = {
    "page": ("{base.background}", "the conversation, settings and home content"),
    "surface": ("{sidebar.background}", "the left sidebar and the settings sidebar"),
    "raised": ("{base.popover}", "menus, popovers, the palette; cards use base.card"),
    "sheet": ("{base.sheet-surface}", "sheets"),
    "overlay": (None, "search-palette:dialog", "the command palette"),
    "text.primary": ("{base.foreground}", ""), "text.secondary": ("{base.muted-foreground}", ""),
    "text.faint": ("{base.faint}", "hints such as the composer's focus shortcut"),
    "text.on-accent": ("{base.background}", "the primary button's text is the page colour (white in light, #141110 in dark); --primary-foreground goes with the unpainted --primary"),
    "text.link": ("{link.foreground}", "file links in agent replies and the README link colour: the warm tan, not blue"),
    "border.default": ("{base.border}", "cards, dialogs, separators"), "border.input": ("{base.input-border}", "inputs, selects, outline buttons"),
    "border.strong": ("{base.prose-border}", "the stronger edge used in rendered markdown"),
    "border.focus": ("{base.ring}", "the focus ring"),
    "accent.default": ("{base.foreground}", "the primary button and the on switch paint the foreground (ink): warm near-black in light, near-white in dark. --primary (#413030 light, #f3f2f1 dark) is declared but the captured primary buttons do not paint it"),
    "accent.subtle": ("{base.accent}", "the hover and highlight wash"),
    "brand": ("{base.special}", "the warm tan (#cca694) on the Done status, unread markers and highlights"),
}
for s_, fill, fg in (("success", "{base.success}", "{base.success-foreground}"), ("danger", "{base.destructive}", "{base.destructive-foreground}"),
                     ("info", "{base.info}", "{base.info-foreground}")):
    ROLE[f"status.{s_}.fill"] = (fill, "")
    ROLE[f"status.{s_}.text"] = (fill, "")
    ROLE[f"status.{s_}.on"] = (fg, "")
ROLE["status.success.subtle"] = ("{base.positive-muted}", "the positive tint")
ROLE["status.warning.fill"] = ("{status.in-progress}", "Conductor's warning colour is the in-progress yellow; base.warning is a tan callout, not a yellow")
ROLE["status.warning.text"] = ("{checks.pending}", "pending checks")
ROLE["status.warning.subtle"] = ("{warning.default}", "the warning callout fill")
ROLE["status.warning.border"] = ("{warning.border}", "the warning callout edge")

COMPONENTS = [
    ("button-primary", "button-primary", {"bg": "background-color", "text": "color", "radius": "border-top-left-radius", "height": "height", "padding": "padding-right"}),
    ("button-outline", "button-outline", {"bg": "background-color", "border": "border-top-color", "text": "color", "radius": "border-top-left-radius", "height": "height", "padding": "padding-right"}),
    ("button-secondary", "button-secondary", {"bg": "background-color", "text": "color", "radius": "border-top-left-radius", "height": "height"}),
    ("button-destructive", "button-destructive", {"bg": "background-color", "text": "color", "radius": "border-top-left-radius", "height": "height"}),
    ("suggestion-chip", "suggestion-chip", {"bg": "background-color", "border": "border-top-color", "text": "color", "radius": "border-top-left-radius", "height": "height"}),
    ("icon-button", "composer-add", {"text": "color", "radius": "border-top-left-radius", "size": "height"}),
    ("send-button", "send-button", {"bg": "background-color", "text": "color", "radius": "border-top-left-radius", "size": "height"}),
    ("composer", "composer", {"bg": "background-color", "border": "border-top-color", "radius": "border-top-left-radius"}),
    ("model-button", "model-button", {"text": "color", "radius": "border-top-left-radius", "height": "height"}),
    ("menu", "menu", {"bg": "background-color", "text": "color", "radius": "border-top-left-radius"}),
    ("menu-item", "menu-item", {"text": "color", "radius": "border-top-left-radius", "height": "height", "padding": "padding-left"}),
    ("menu-item-highlighted", "menu-item-highlighted", {"bg": "background-color", "text": "color"}),
    ("dialog", "dialog", {"bg": "background-color", "border": "border-top-color", "radius": "border-top-left-radius", "padding": "padding-top"}),
    ("palette", "search-palette:dialog", {"bg": "background-color", "border": "border-top-color", "radius": "border-top-left-radius"}),
    ("palette-item-highlighted", "palette-item-highlighted", {"bg": "background-color", "text": "color", "radius": "border-top-left-radius"}),
    ("tooltip", "tooltip", {"bg": "background-color", "text": "color", "radius": "border-top-left-radius"}),
    ("toast", "toast", {"bg": "background-color", "border": "border-top-color", "text": "color", "radius": "border-top-left-radius"}),
    ("chat-tab", "chat-tab-selected", {"text": "color", "height": "height"}),
    ("panel-tab", "panel-tab", {"text": "color", "radius": "border-top-left-radius", "height": "height"}),
    ("panel-tab-selected", "panel-tab-selected", {"bg": "background-color", "text": "color"}),
    ("bottom-tab-selected", "bottom-tab-selected", {"text": "color"}),
    ("input", "settings-search", {"bg": "background-color", "border": "border-top-color", "text": "color", "radius": "border-top-left-radius", "height": "height"}),
    ("text-field", "text-field", {"bg": "background-color", "border": "border-top-color", "text": "color", "radius": "border-top-left-radius", "height": "height"}),
    ("select", "select", {"bg": "background-color", "border": "border-top-color", "text": "color", "radius": "border-top-left-radius", "height": "height"}),
    ("switch-on", "switch-on", {"bg": "background-color", "radius": "border-top-left-radius"}),
    ("switch-off", "switch-off", {"bg": "background-color"}),
    ("badge", "plan-badge", {"border": "border-top-color", "text": "color", "radius": "border-top-left-radius"}),
    ("home-card", "home-card", {"bg": "background-color", "border": "border-top-color", "radius": "border-top-left-radius"}),
    ("system-card", "system-card", {"bg": "background-color", "text": "color", "radius": "border-top-left-radius"}),
    ("empty-card", "empty-card", {"border": "border-top-color", "radius": "border-top-left-radius"}),
    ("nav-row", "sidebar-nav-item", {"text": "color", "radius": "border-top-left-radius", "height": "height"}),
    ("workspace-row", "workspace-row-selected", {"bg": "background-color", "text": "color", "radius": "border-top-left-radius"}),
    ("settings-nav", "settings-nav-item", {"text": "color", "radius": "border-top-left-radius", "height": "height"}),
    ("settings-nav-selected", "settings-nav-selected", {"bg": "background-color", "text": "color"}),
    ("tree-row", "tree-row", {"text": "color", "height": "height"}),
    ("user-message", "user-message", {"bg": "background-color", "text": "color", "radius": "border-top-left-radius"}),
    ("tool-arg", "tool-arg", {"bg": "background-color", "text": "color", "radius": "border-top-left-radius"}),
    ("inline-code", "inline-code", {"bg": "background-color", "border": "border-top-color", "text": "color", "radius": "border-top-left-radius"}),
    ("file-link", "file-link", {"text": "color"}),
    ("diff-chip", "diff-chip", {"bg": "background-color", "border": "border-top-color", "radius": "border-top-left-radius"}),
    ("diff-line-added", "diff-line-added", {"bg": "background-color"}),
    ("diff-gutter-added", "diff-gutter-added", {"bg": "background-color", "text": "color"}),
    ("list-row", "list-row", {"text": "color", "height": "height"}),
]
STATES = [("hover", "bg-hover", "background-color"), ("hover", "text-hover", "color"), ("pressed", "bg-pressed", "background-color"),
          ("focus-visible", "border-focus", "border-top-color")]
CORE_NAMES = re.compile(r"^base\.(background|foreground|card|popover|primary|primary-foreground|secondary|muted|muted-foreground|accent|accent-foreground|border|input|ring|destructive)$")
PREFER = ["role", "base", "sidebar", "link", "git", "status", "highlight", "tip", "warning", "todo", "terminal", "code", "checks", "color"]


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
    walk(CORE.get("color", {}), ["color"])
    for vals in idx.values():
        vals.sort(key=lambda p: (not CORE_NAMES.match(p), PREFER.index(p.split(".")[0]) if p.split(".")[0] in PREFER else 99, len(p), p))
    return idx


def visible_shadow(css):
    """Tailwind writes every box-shadow as ring, ring-offset and shadow layers; the unused ones are transparent zeros."""
    return [l for l in shadow(css) if not l["color"].endswith(", 0)")]


def build_roles_and_components(t):
    tree = SETS[t]
    for key, spec in ROLE.items():
        if spec[0] is None:
            shot, s = style(t, spec[1])
            put(tree, ("role",) + tuple(key.split(".")), tok(color(s["background-color"]), "color", "Measured",
                f"background-color of {spec[1]} in {shot}, {THEME_NAME[t]}, {DATE}; {spec[2]}"))
            continue
        target = spec[0][1:-1]
        if get(tree, target) is None:
            raise KeyError(f"role.{key}: {target} missing in {t}")
        put(tree, ("role",) + tuple(key.split(".")), tok(spec[0], "color", "Derived", f"the checklist role, mapped to {target}" + (f"; {spec[1]}" if spec[1] else "")))
    # The backdrop's own element was not the one measured (a portal wrapper with no fill was), so the scrim is
    # read off the screenshots: over the flat page, light #ffffff shows as #808080 and dark #151110 as #0a0808,
    # both black at 50% (bg-overlay is --overlay, #000, at /50), under a backdrop-blur-xs.
    put(tree, ("role", "scrim"), tok("rgba(0, 0, 0, 0.5)", "color", "Sampled",
        f"remove-confirm.png against settings-repo-misc.png, 200 x 150 px of flat page at (2400, 1300), {THEME_NAME[t]}, {DATE}: "
        "black at 50% over the page; the class is bg-overlay (--overlay, #000) with backdrop-blur-xs", formula="var(--overlay) at 50%"))
    idx = index(t)
    measured_n = aliased_n = 0

    def value_for(part, shot, prop, raw):
        nonlocal measured_n, aliased_n
        src = f"computed {prop} of {part} in {shot}, {THEME_NAME[t]}, {DATE}"
        if prop in ("background-color", "color", "border-top-color", "outline-color"):
            v = color(raw)
            measured_n += 1
            if v in idx:
                aliased_n += 1
                fits = [x for x in idx[v] if ("foreground" in x) == (prop == "color") and not x.startswith("role.")]
                return tok("{%s}" % (fits or [x for x in idx[v] if not x.startswith("role.")] or idx[v])[0], "color", "Measured", src, painted=v)
            return tok(v, "color", "Measured", src)
        v = px(raw) if raw.endswith("px") else raw
        if re.fullmatch(r"[\d.]+px", v):
            v = px("%gpx" % round(float(v[:-2])))
        return tok(v, "dimension", "Measured", src + f" ({raw})")
    for name, part, props in COMPONENTS:
        shot, s = style(t, part)
        if not s:
            continue
        for key, prop in props.items():
            raw = s[prop]
            if prop in ("background-color", "border-top-color") and color(raw) == "rgba(0, 0, 0, 0)":
                continue
            if prop == "border-top-color" and s.get("border-top-width") in ("0px", ""):
                continue
            if prop == "border-top-left-radius" and raw.endswith("%"):
                raw = "9999px"
            if not (raw.endswith("px") or is_color(raw)):
                continue
            put(tree, ("component", name, key), value_for(part, shot, prop, raw))
        for state, key, prop in STATES:
            sh, ss = style(t, part, state)
            if ss and ss[prop] != s[prop] and is_color(ss[prop]) and color(ss[prop]) != "rgba(0, 0, 0, 0)":
                put(tree, ("component", name, key), value_for(part, sh, prop, ss[prop]))
        layers = visible_shadow(s["box-shadow"])
        if layers:
            put(tree, ("shadow", name), tok(layers, "shadow", "Measured",
                f"computed box-shadow of {part} in {shot}, {THEME_NAME[t]}, {DATE}, without the transparent ring placeholders Tailwind adds"))
    # Roles that are states of a component rather than a declared colour.
    hov = get(tree, "component.button-primary.bg-hover")
    base_btn = get(tree, "component.button-primary.bg")
    hit = hov or base_btn
    put(tree, ("role", "accent", "hover"), tok(hit["$value"], "color", "Measured", hit["$extensions"]["source"]["from"] + "; hover:bg-primary/90 on the primary button" if hov else
        hit["$extensions"]["source"]["from"] + "; the primary button's hover did not change its fill"))
    put(tree, ("role", "accent", "pressed"), tok("{role.accent.default}", "color", "Derived",
        "pressed keeps the fill and darkens it with an inset shadow (active:inset-shadow-[0_0_0_999px_rgb(0_0_0/0.1)]) and a 1px drop (active:translate-y-px)",
        overlay="inset 0 0 0 999px rgba(0, 0, 0, 0.1)"))
    fg = color(resolve(t, "{base.foreground}"))
    if not re.fullmatch(r"#[0-9a-f]{6}", fg):
        raise SystemExit(f"base.foreground is {fg} in {t}, not an opaque colour: role.text.disabled cannot be derived from it")
    r, g, b = (int(fg[i:i + 2], 16) for i in (1, 3, 5))
    put(tree, ("role", "text", "disabled"), tok(f"rgba({r}, {g}, {b}, 0.5)", "color", "Derived",
        "base.foreground at the 50% opacity disabled controls take (disabled:opacity-50)", formula="disabled:opacity-50"))
    tree["$extensions"] = {**tree.get("$extensions", {}), "componentValues": {"measured": measured_n, "aliased": aliased_n}}


for t in THEMES:
    build_roles_and_components(t)

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
            if t["$type"] == "dimension" and not aliases(t["$value"]) and not re.fullmatch(r"-?\d*\.?\d+(px|rem|em)", t["$value"]):
                raise ValueError(f"{setname}.{n}: dimension {t['$value']!r}")
            if t["$type"] == "color" and not aliases(t["$value"]) and not re.fullmatch(r"#[0-9a-f]{6}|rgba\(\d+, \d+, \d+, [\d.]+\)", t["$value"]):
                raise ValueError(f"{setname}.{n}: colour {t['$value']!r}")
    a, b = {n for n, _ in tokens_of(SETS["light"])}, {n for n, _ in tokens_of(SETS["dark"])}
    if a != b:
        raise ValueError(f"light and dark differ: only light {sorted(a - b)[:5]}, only dark {sorted(b - a)[:5]}")


def reconcile():
    """A name measured in only one theme (a part that rendered in one pass only) is not a theme token: move it out."""
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
                {"name": n, "value": v["$value"], "why": f"measured only while capturing {t}; not in the other theme"})


reconcile()
check()
tokens = {
    "core": CORE, "light": SETS["light"], "dark": SETS["dark"],
    "$themes": [
        {"id": "light", "name": "Light", "selectedTokenSets": {"core": "source", "light": "enabled"},
         "$description": "Settings > Appearance > Theme: Light, or System with a light macOS appearance (html.light)"},
        {"id": "dark", "name": "Dark", "selectedTokenSets": {"core": "source", "dark": "enabled"},
         "$description": "Settings > Appearance > Theme: Dark (the default), or System with a dark macOS appearance (html.dark)"},
    ],
    "$metadata": {"tokenSetOrder": ["core", "light", "dark"]},
}
(PKG / "tokens.json").write_text(json.dumps(tokens, indent=2, ensure_ascii=False) + "\n")


def count(d):
    return sum(1 for _ in tokens_of(d))


print({k: count(tokens[k]) for k in ("core", "light", "dark")}, "component values aliased:",
      {t: SETS[t]["$extensions"]["componentValues"] for t in THEMES})
