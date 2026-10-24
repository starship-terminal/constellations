#!/usr/bin/env python3
"""Build tokens.json (W3C DTCG, Tokens Studio multi-set layout) from the raw readings.

    python3 tools/build_tokens.py

Sources, read live from Cursor 3.27.6 for macOS on 2026-10-25 over the remote-debugging port
(tools/capture/electron/):
  raw/css-vars.<theme>.json      every --cursor-*, --glass-* and --ui-* custom property the Agents
                                 window's stylesheets declare, by sheet, selector and condition, and
                                 each name as it computes and paints on [data-component="root"]
  raw/css-vars.ide-<theme>.json  the same for the IDE window (--vscode-* and --cursor-*), on .monaco-workbench
  raw/components.<theme>.json    computed styles of the captured parts, per shot and state (shots.mjs)

How Cursor's colours work, and so how this file is laid out. A theme is a short list of seed colours
(base, chrome, pane, sidebar, elevated, accent, brand, nine hues, status and git colours, written as
hex on body[data-cursor-glass-mode="true"] by the glass-cursor-theme-variables style element). Every
other colour token is either a plain var() of another token or a color-mix() of a seed with
transparent: text.secondary is base at 74%, bg.primary base at 20%, stroke.secondary base at 12%.
So each semantic set holds the seeds as values and the rest as aliases ({seed.base}) or as the
painted value with the formula in $extensions.formula. Scales that do not change with the theme
(radius, spacing, type, control heights, motion) are the core set. role.* maps the checklist roles
(page, surface, raised, ...) onto Cursor's own tokens, and component.* holds measured component
values, aliased to a token whenever the painted value matches one.

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

PREFIX = "--cursor-"
SEED_SHEET, SEED_SEL = "glass-cursor-theme-variables", 'body[data-cursor-glass-mode="true"]'
FORMULA_SHEET, FORMULA_SEL = "glass-cursor-theme-variables", "CSSNestedDeclarations"
THEME_NAME = {"light": "Cursor Light", "dark": "Cursor Dark"}
# Names that are scales, not colours: they go to core under these groups.
CORE_SCALES = [("radius-", "radius"), ("spacing-", "spacing"), ("height-", "controlHeight"), ("line-height-", "lineHeight"),
               ("letter-spacing-", "letterSpacing"), ("font-size-", "fontSize"), ("font-weight-", "fontWeight"),
               ("duration-", "duration"), ("easing-", "easing"), ("scrollbar-horizontal-size", "scrollbar"),
               ("scrollbar-vertical-size", "scrollbar"), ("elevation-", "elevation")]
SKIP = re.compile(r"^--cursor-(spacing-ne-|spinner|font-smoothing|font-family|focus-ring-(width|offset)|field-focus)")
GROUPS = ["bg", "text", "stroke", "icon", "button", "control", "command", "diff", "editor", "terminal", "scrollbar",
          "shadow", "specular", "input", "titlebar", "toolbar", "progress", "syntax", "focus", "box", "on"]
IDE_NAMES = ["editor-background", "editor-foreground", "editorLineNumber-foreground", "editorLineNumber-activeForeground",
             "sideBar-background", "sideBar-foreground", "sideBarSectionHeader-foreground", "activityBar-background",
             "activityBar-foreground", "statusBar-background", "statusBar-foreground", "titleBar-activeBackground",
             "titleBar-activeForeground", "tab-activeBackground", "tab-activeForeground", "tab-inactiveBackground",
             "tab-inactiveForeground", "panel-background", "panel-border", "focusBorder", "list-hoverBackground",
             "list-activeSelectionBackground", "list-inactiveSelectionBackground", "quickInput-background",
             "quickInputList-focusBackground", "input-background", "input-border", "input-foreground", "button-background",
             "button-foreground", "button-hoverBackground", "widget-shadow", "keybindingLabel-background",
             "keybindingLabel-foreground", "editorWidget-background", "dropdown-background", "menu-background",
             "menu-selectionBackground", "scrollbarSlider-background", "errorForeground", "textLink-foreground"]


def load(name):
    return json.loads((RAW / name).read_text())


V = {t: load(f"css-vars.{t}.json") for t in THEMES}
IDE = {t: load(f"css-vars.ide-{t}.json") for t in THEMES}
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
    return V[t]["computed"][V[t]["scope"]]


def decl(t, name, sheet, sel):
    for d in V[t]["decls"]:
        if d["name"] == name and d["sheet"] == sheet and d["selector"].startswith(sel) and d["condition"] == "":
            return d["value"]
    return None


def path_of(name):
    """--cursor-bg-accent-primary -> ('bg', 'accent-primary'); --cursor-blue-fill -> ('blue', 'fill');
    --cursor-base -> ('seed', 'base')."""
    rest = name[len(PREFIX):]
    head, _, tail = rest.partition("-")
    if not tail:
        return ("seed", head)
    return (head, tail)


def where(t, name, extra=""):
    return f"{name} on [data-component=\"root\"], Agents window, {THEME_NAME[t]}, {DATE}{extra}"


# ---------------------------------------------------------------- semantic sets


def semantic(t):
    tree, comp, painted, shadows = {}, computed(t), V[t]["colors"], V[t]["shadows"]
    names = sorted(n for n in comp if n.startswith(PREFIX) and not SKIP.match(n)
                   and not any(n[len(PREFIX):].startswith(p) for p, _ in CORE_SCALES))
    paths = {n: path_of(n) for n in names}
    for n in names:
        p = paths[n]
        seed = decl(t, n, SEED_SHEET, SEED_SEL)
        formula = decl(t, n, FORMULA_SHEET, FORMULA_SEL)
        if "shadow" in n and n in shadows and shadows[n] != "none" and n.startswith("--cursor-box-shadow"):
            put(tree, ("shadow", p[1].replace("shadow-", "")), tok(shadow(shadows[n]), "shadow", "Measured",
                where(t, n, "; box-shadow as painted"), formula=comp[n]))
            continue
        if n not in painted or not is_color(painted[n]):
            continue
        value = color(painted[n])
        if seed:
            put(tree, p, tok(value, "color", "Measured", f"{n} = {seed} on {SEED_SEL} ({SEED_SHEET}), {THEME_NAME[t]}, {DATE}"))
            continue
        m = re.fullmatch(r"var\((--cursor-[\w-]+)\)", formula or "")
        if m and m.group(1) in paths and color(painted.get(m.group(1), "none") if is_color(painted.get(m.group(1), "none")) else "none") == value:
            put(tree, p, tok("{%s}" % ".".join(paths[m.group(1)]), "color", "Measured", where(t, n), formula=formula))
        else:
            put(tree, p, tok(value, "color", "Measured", where(t, n), formula=formula or comp[n]))
    # --glass-* surfaces and the ui tool-call card
    for n in sorted(comp):
        if (n.startswith("--glass-") or n.startswith("--ui-")) and n in painted and is_color(painted[n]) and not re.search(r"(width|height|gap|padding|spacer|opacity|scale)", n):
            key = n[2:].split("-", 1)
            put(tree, (key[0], key[1]), tok(color(painted[n]), "color", "Measured", where(t, n), formula=comp[n]))
    # IDE window colours
    ide_painted = IDE[t]["colors"]
    for k in IDE_NAMES:
        n = "--vscode-" + k
        if n in ide_painted and is_color(ide_painted[n]):
            put(tree, ("ide", k), tok(color(ide_painted[n]), "color", "Measured",
                f"{n} on .monaco-workbench, IDE window, {THEME_NAME[t]}, {DATE}"))
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
    """{(part, state): style} from the first shot that measured it."""
    out = {}
    for shot, d in C[t].items():
        for part, v in d["parts"].items():
            out.setdefault((part, d["state"]), (shot, v["style"]))
    return out


P = {t: parts(t) for t in THEMES}


def style(t, part, state="default"):
    hit = P[t].get((part, state))
    return hit if hit else (None, None)


# ---------------------------------------------------------------- core

CORE = {}
dark_comp, light_comp = computed("dark"), computed("light")


def core_scales():
    for n in sorted(dark_comp):
        if not n.startswith(PREFIX) or SKIP.match(n):
            continue
        rest = n[len(PREFIX):]
        for pre, group in CORE_SCALES:
            if rest.startswith(pre):
                v = dark_comp[n]
                if light_comp.get(n) != v:
                    raise ValueError(f"{n} differs by theme: {v} / {light_comp.get(n)}")
                key = rest[len(pre):] if pre.endswith("-") else rest.replace("scrollbar-", "")
                src = f"{n} on [data-component=\"root\"], both themes, {DATE}"
                if group == "fontWeight":
                    t = tok(int(v), "fontWeight", "Measured", src)
                elif group == "duration":
                    t = tok(ms(v), "duration", "Measured", src)
                elif group == "easing":
                    t = tok(bezier(v), "cubicBezier", "Measured", src, css=v)
                elif group == "elevation":
                    t = tok(int(v), "number", "Measured", src)
                else:
                    t = tok(px(v), "dimension", "Measured", src)
                put(CORE, (group, key.replace(".", "-")), t)
                break


core_scales()

# Families: the root's inline style (written from Settings > Appearance > UI Font Family "System font"
# and Code Font Family "System monospace") overrides the stylesheet stacks.
for key, n in (("sans", "--cursor-font-family-sans"), ("mono", "--cursor-font-family-mono")):
    stack = [f.strip().strip("'\"") for f in dark_comp[n].split(",")]
    sheet = decl("dark", n, "anysphere-ui-tokens", ":root") or decl("dark", n, "anysphere-ui-styles", ":root")
    put(CORE, ("fontFamily", key), tok(stack, "fontFamily", "Measured",
        f"{n} on [data-component=\"root\"] (inline, from the owner's font-family settings), {DATE}", stylesheetDefault=sheet))
put(CORE, ("fontWeight", "normal-ui"), tok(int(dark_comp["--cursor-font-weight-normal"]), "fontWeight", "Measured",
    f"--cursor-font-weight-normal on [data-component=\"root\"] (inline): the regular weight the Agents window renders text at, {DATE}",
    note="The stylesheet's --cursor-font-weight-normal is 400; the root overrides it to 418 under body.glass-typography-refresh"))

# Focus ring: the Agents window's own (on [data-component=root][data-focus-ring]) and the default.
FR = {"--glass-focus-ring-width": ("width", "Measured"), "--cursor-focus-ring-offset": ("offset-default", "Measured"),
      "--cursor-focus-ring-width": ("width-default", "Measured")}
for n, (key, ev) in FR.items():
    v = dark_comp.get(n) if n.startswith("--glass") else V["dark"]["computed"]["body"].get(n)
    put(CORE, ("focusRing", key), tok(px(v), "dimension", ev, f"{n}, {'[data-component=root]' if n.startswith('--glass') else 'body'}, {DATE}"))
put(CORE, ("focusRing", "offset"), tok("-1px", "dimension", "Measured",
    f"calc(var(--glass-focus-ring-width) * -1) on [data-component=\"root\"][data-focus-ring], {DATE}"))

# Type roles, measured on real elements (computed style, both themes agree).
ROLES = [("heading", "page-title", "Settings and Automations page titles"),
         ("body", "field-label", "Settings row labels, list text, menu items"),
         ("body-secondary", "field-description", "Settings row descriptions (text.secondary)"),
         ("label", "button-primary", "Button labels"),
         ("caption", "palette-section-heading", "Section headings in menus and the palette"),
         ("small", "ide-button", "The IDE button and other 11px chrome"),
         ("prompt", "composer-editor", "Text typed in the composer"),
         ("message", "assistant-message", "Agent replies in the conversation"),
         ("code", "editor", "Code in the IDE editor")]
for role, part, use in ROLES:
    shot, s = style("dark", part)
    if not s:
        continue
    fam = "{fontFamily.mono}" if role == "code" else "{fontFamily.sans}"
    lh = s["line-height"]
    val = {"fontFamily": fam, "fontSize": px(s["font-size"]), "fontWeight": int(s["font-weight"]),
           "lineHeight": px(lh) if lh.endswith("px") else "normal",
           "letterSpacing": px(s["letter-spacing"]) if s["letter-spacing"].endswith("px") else "0px"}
    if val["lineHeight"] == "normal":
        val["lineHeight"] = px("%gpx" % round(float(s["font-size"][:-2]) * 1.2, 1))
        note = "computed line-height is normal; 1.2 x the size is used here"
    else:
        note = None
    put(CORE, ("typography", role), tok(val, "typography", "Measured", f"computed style of {part} in {shot}, dark, {DATE}; {use}", note=note))

# Sizes, layout, layers: measured boxes and computed widths.
def dim_of(part, prop, shot_state="default", t="dark"):
    shot, s = style(t, part, shot_state)
    return (shot, s[prop]) if s and s.get(prop, "").endswith("px") else (None, None)


SIZES = [("size.control.icon-button", "icon-button", "height", "Icon buttons (24 x 24)"),
         ("size.control.button", "button-primary", "height", "Text buttons"),
         ("size.control.pill", "pill", "height", "Pills (Plan New Idea)"),
         ("size.control.menu-row", "menu-row", "height", "Menu and select rows"),
         ("size.control.sidebar-row", "sidebar-row", "height", "Sidebar rows"),
         ("size.control.table-row", "table-row", "height", "Table rows (Automations)"),
         ("size.control.switch-width", "switch-on", "width", "Switch, medium"),
         ("size.control.switch-height", "switch-on", "height", "Switch, medium"),
         ("size.control.switch-sm-width", "switch-sm", "width", "Switch, small (in menus)"),
         ("size.control.switch-sm-height", "switch-sm", "height", "Switch, small (in menus)"),
         ("size.control.avatar", "avatar", "height", "Account avatar"),
         ("size.control.progress", "progress", "height", "Usage progress bar"),
         ("layout.sidebar", "sidebar", "width", "Agents window sidebar"),
         ("layout.composer", "composer", "width", "Composer on the empty New Chat page"),
         ("layout.settings-content", "field-group", "width", "Settings content column"),
         ("layout.automations-content", "table", "width", "Automations content column"),
         ("layout.conversation", "user-message", "width", "Conversation column (user bubble)"),
         ("layout.palette", "palette", "width", "Search palette"),
         ("layout.dialog", "dialog", "width", "Create Project dialog"),
         ("layout.confirm-dialog", "confirm-dialog", "width", "Delete confirmation"),
         ("layout.menu", "context-menu", "width", "Context and action menus"),
         ("layout.menu-wide", "menu", "width", "Model menu"),
         ("layout.select-popover", "select-popover", "width", "Environment select"),
         ("layout.ide-sidebar", "side-bar", "width", "IDE primary sidebar"),
         ("layout.ide-agent-pane", "agent-pane", "width", "IDE agent pane"),
         ("layout.ide-titlebar-height", "titlebar", "height", "IDE title bar"),
         ("layout.ide-statusbar-height", "status-bar", "height", "IDE status bar")]
for path, part, prop, use in SIZES:
    shot, v = dim_of(part, prop)
    if v:
        put(CORE, tuple(path.split(".")), tok(px("%gpx" % round(float(v[:-2]))), "dimension", "Measured",
            f"computed {prop} of {part} in {shot}, dark, {DATE} ({use}); {v} before rounding"))
for n, key in (("--glass-chrome-bar-height", "titlebar-height"), ("--ui-sidebar-top-bar-height", "sidebar-top-bar-height")):
    if n in dark_comp:
        put(CORE, ("layout", key), tok(px(dark_comp[n]), "dimension", "Measured", f"{n} on [data-component=\"root\"], {DATE}"))
WINDOW = C["dark"]["home-default"]["viewport"]
put(CORE, ("layout", "window-width"), tok("1280px", "dimension", "Measured",
    f"window 1280 x 800 pt; the Agents window's viewport is {WINDOW['css'][0]} x {WINDOW['css'][1]} CSS px at devicePixelRatio {WINDOW['dpr']:.2f} (2 x the --zoom-factor 0.84 the owner's UI Font Size 11 sets), {DATE}"))
put(CORE, ("layout", "window-height"), tok("800px", "dimension", "Measured", f"window height, pt, {DATE}"))
put(CORE, ("layout", "chat-width"), tok("780px", "dimension", "Measured",
    f"Settings > Appearance > Chat Width, shown as 780px (the owner's value), {DATE}"))

Z = [("backdrop", "backdrop"), ("menu", "menu"), ("submenu", "submenu"), ("dialog", "dialog"), ("ide-quick-input", "quick-input")]
for key, part in Z:
    shot, s = style("dark", part)
    if s and s["z-index"] not in ("auto", ""):
        put(CORE, ("zIndex", key), tok(int(s["z-index"]), "number", "Measured", f"computed z-index of {part} in {shot}, {DATE}"))

shot, s = style("dark", "composer")
put(CORE, ("borderWidth", "hairline"), tok("1px", "dimension", "Measured",
    f"border-top-width of composer, pill, dialog and banners; computed {s['border-top-width']} = one device pixel at the 1.68 pixel ratio, declared 1px, {DATE}"))
put(CORE, ("borderWidth", "focus"), tok("{focusRing.width}", "dimension", "Derived", "the focus ring is an outline of focusRing.width"))
put(CORE, ("press", "scale"), tok(float(dark_comp.get("--ui-press-scale", "1")), "number", "Measured",
    f"--ui-press-scale on [data-component=\"root\"], {DATE}"))
put(CORE, ("blur", "palette"), tok("16px", "dimension", "Measured", f"backdrop-filter of the search palette ({style('dark', 'palette')[1]['backdrop-filter']}), {DATE}"))
put(CORE, ("blur", "user-message"), tok("10px", "dimension", "Measured", f"backdrop-filter of the user message bubble ({style('dark', 'user-message')[1]['backdrop-filter']}), {DATE}"))

# reduced motion and breakpoints, summarised from the stylesheets' conditions
cond = V["dark"]["conditions"]
rm = {k: v["rules"] for k, v in cond.items() if "reduced-motion" in k}
CORE.setdefault("duration", {})["$extensions"] = {"reducedMotion": {
    "rules": rm, "how": "Settings > Appearance > Reduce Motion (System follows the OS) sets --ui-reduced-motion: reduce; "
    "style(--ui-reduced-motion: reduce) container queries then drop animation-name, durations and delays; "
    "(prefers-reduced-motion: reduce) rules do the same for transitions"}}
bp = sorted({k for k in cond if re.search(r"width", k)})
CORE.setdefault("layout", {})["$extensions"] = {"breakpointsInCss": bp,
    "note": "The window is resizable and Cursor has no breakpoint scale of its own; these are every width condition its stylesheets use"}

# ---------------------------------------------------------------- roles and components, per theme

ROLE = {
    "page": ("{seed.chrome}", "Agents window main panel (sampled #141414 in dark home-default as a check)"),
    "surface": ("{bg.sidebar}", "the sidebar and the IDE pane"),
    "raised": ("{seed.elevated}", "composer, menus, dialogs, tables, cards"),
    "overlay": (None, "palette", "the search palette: translucent, with backdrop blur 16px"),
    "scrim": (None, "backdrop", "dialog and palette backdrop"),
    "text.primary": ("{text.primary}", ""), "text.secondary": ("{text.secondary}", ""),
    "text.tertiary": ("{text.tertiary}", ""), "text.disabled": ("{text.quaternary}", "the quaternary tier is the faintest text"),
    "text.on-accent": ("{text.on-primary}", ""), "text.link": ("{text.link}", ""),
    "border.default": ("{stroke.secondary}", "composer, dialogs, fields"), "border.strong": ("{stroke.primary}", ""),
    "border.subtle": ("{stroke.tertiary}", "tables, menu footers, separators"), "border.focus": ("{stroke.focus-ring}", ""),
    "accent.default": ("{bg.accent-primary}", ""), "accent.hover": ("{bg.accent-primary-hover}", ""),
    "accent.pressed": ("{bg.accent-primary-pressed}", ""), "accent.subtle": ("{bg.accent-tertiary}", ""),
    "brand": ("{seed.brand}", "Cursor's orange; not used in the interface chrome captured"),
}
for s_, words in (("success", "success"), ("warning", "warning"), ("danger", "danger")):
    hue = {"success": "green", "warning": "yellow", "danger": "red"}[s_]
    ROLE[f"status.{s_}.fill"] = ("{bg.%s-primary}" % words, "")
    ROLE[f"status.{s_}.subtle"] = ("{bg.%s-tertiary}" % words, "")
    ROLE[f"status.{s_}.text"] = ("{text.%s-primary}" % words, "")
    ROLE[f"status.{s_}.border"] = ("{stroke.%s-secondary}" % hue, f"no stroke.{words}-*; the {hue} hue's stroke tier")
ROLE["status.info.fill"] = ("{bg.blue-primary}", "Cursor has no info status; blue is used for it (the info banner uses the accent)")
ROLE["status.info.subtle"] = ("{bg.blue-tertiary}", "")
ROLE["status.info.text"] = ("{text.blue-primary}", "")
ROLE["status.info.border"] = ("{stroke.blue-secondary}", "")

# component tokens: (name, part, state, {key: css property}); value aliased when it equals a token
COMPONENTS = [
    ("button-primary", "button-primary", {"bg": "background-color", "text": "color", "radius": "border-top-left-radius", "height": "height", "padding": "padding-right"}),
    ("button-inverse", "button-primary-inverse", {"bg": "background-color", "text": "color", "radius": "border-top-left-radius", "height": "height", "padding": "padding-right"}),
    ("button-update", "button-update", {"bg": "background-color", "text": "color", "radius": "border-top-left-radius", "height": "height"}),
    ("button-outline", "button-outline", {"border": "border-top-color", "text": "color", "radius": "border-top-left-radius"}),
    ("icon-button", "icon-button", {"text": "color", "radius": "border-top-left-radius", "size": "height"}),
    ("pill", "pill", {"border": "border-top-color", "text": "color", "radius": "border-top-left-radius", "height": "height", "padding": "padding-right"}),
    ("composer", "composer", {"bg": "background-color", "border": "border-top-color", "radius": "border-top-left-radius"}),
    ("menu", "menu", {"bg": "background-color", "text": "color", "radius": "border-top-left-radius"}),
    ("menu-row", "menu-row", {"text": "color", "height": "height", "padding": "padding-left"}),
    ("dialog", "dialog", {"bg": "background-color", "border": "border-top-color", "radius": "border-top-left-radius"}),
    ("palette", "palette", {"bg": "background-color", "radius": "border-top-left-radius"}),
    ("scrim", "backdrop", {"bg": "background-color"}),
    ("tab", "tab", {"text": "color", "radius": "border-top-left-radius", "height": "height", "padding": "padding-left"}),
    ("tab-selected", "tab-selected", {"bg": "background-color", "text": "color"}),
    ("text-field", "settings-search", {"bg": "background-color", "border": "border-top-color", "text": "color", "radius": "border-top-left-radius", "height": "height"}),
    ("badge", "badge", {"bg": "background-color", "text": "color", "radius": "border-top-left-radius", "height": "height"}),
    ("status-badge", "status-badge", {"bg": "background-color", "text": "color"}),
    ("table", "table", {"bg": "background-color", "border": "border-top-color", "radius": "border-top-left-radius"}),
    ("card", "template-card", {"bg": "background-color", "radius": "border-top-left-radius", "padding": "padding-top"}),
    ("banner-info", "info-banner", {"bg": "background-color", "border": "border-top-color", "radius": "border-top-left-radius"}),
    ("sidebar-row", "sidebar-row", {"text": "color", "radius": "border-top-left-radius", "height": "height"}),
    ("sidebar-row-selected", "sidebar-row-selected", {"text": "color"}),
    ("user-message", "user-message", {"bg": "background-color", "border": "border-top-color", "radius": "border-top-left-radius"}),
    ("code-block", "code-block", {"bg": "background-color", "border": "border-top-color", "radius": "border-top-left-radius"}),
    ("tooltip", "tooltip", {"bg": "background-color", "text": "color", "radius": "border-top-left-radius"}),
    ("link", "text-link", {"text": "color"}),
]
STATES = [("hover", "bg-hover", "background-color"), ("hover", "text-hover", "color"), ("pressed", "bg-pressed", "background-color"),
          ("focus-visible", "outline-focus", "outline-color")]
CORE_NAMES = re.compile(r"^(text|bg|stroke|icon)\.(primary|secondary|tertiary|quaternary|quinary|on-primary|link|elevated|chrome|sidebar|card|accent-primary(-hover|-pressed)?|focus-ring)$")
PREFER = ["role", "text", "bg", "stroke", "seed", "icon", "button", "control", "glass"]


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
    for vals in idx.values():
        vals.sort(key=lambda p: (not CORE_NAMES.match(p), PREFER.index(p.split(".")[0]) if p.split(".")[0] in PREFER else 99, len(p), p))
    return idx


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
                pre = {"background-color": "bg.", "color": "text.", "border-top-color": "stroke.", "outline-color": "stroke."}[prop]
                best = next((x for x in idx[v] if x.startswith(pre)), idx[v][0])
                return tok("{%s}" % best, "color", "Measured", src, painted=v)
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
            put(tree, ("component", name, key), value_for(part, shot, prop, raw))
        for state, key, prop in STATES:
            sh, ss = style(t, part, state)
            if ss and ss[prop] != s[prop] and color(ss[prop]) != "rgba(0, 0, 0, 0)":
                put(tree, ("component", name, key), value_for(part, sh, prop, ss[prop]))
    tree["$extensions"] = {"componentValues": {"measured": measured_n, "aliased": aliased_n}}


for t in THEMES:
    build_roles_and_components(t)


def shadow_uses(t):
    """Name, on each shadow token, the captured parts whose computed box-shadow is exactly it."""
    for key, tokn in SETS[t].get("shadow", {}).items():
        if not isinstance(tokn, dict) or tokn.get("$type") != "shadow":
            continue
        uses = sorted({part for (part, state), (shot, s) in P[t].items() if state == "default"
                       and s["box-shadow"] != "none" and shadow(s["box-shadow"]) == tokn["$value"]})
        tokn["$extensions"]["usedBy"] = uses or "no captured part paints exactly this shadow"


for t in THEMES:
    shadow_uses(t)

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
    a, b = {n for n, _ in tokens_of(SETS["light"])}, {n for n, _ in tokens_of(SETS["dark"])}
    if a != b:
        raise ValueError(f"light and dark differ: only light {sorted(a - b)[:5]}, only dark {sorted(b - a)[:5]}")


def reconcile():
    """A name set by script on only one theme's root (seen once) is not a theme token: move it out."""
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
                {"name": n, "value": v["$value"], "why": f"present on the root only while capturing {t}; not in the other theme"})


reconcile()
check()
tokens = {
    "core": CORE, "light": SETS["light"], "dark": SETS["dark"],
    "$themes": [
        {"id": "light", "name": "Light", "selectedTokenSets": {"core": "source", "light": "enabled"},
         "$description": "Settings > Appearance > Theme: Cursor Light (body.cursor-light)"},
        {"id": "dark", "name": "Dark", "selectedTokenSets": {"core": "source", "dark": "enabled"},
         "$description": "Settings > Appearance > Theme: Cursor Dark (body.cursor-dark); System follows macOS"},
    ],
    "$metadata": {"tokenSetOrder": ["core", "light", "dark"]},
}
(PKG / "tokens.json").write_text(json.dumps(tokens, indent=2, ensure_ascii=False) + "\n")


def count(d):
    return sum(1 for _ in tokens_of(d))


print({k: count(tokens[k]) for k in ("core", "light", "dark")}, "component values aliased:",
      {t: SETS[t]["$extensions"]["componentValues"] for t in THEMES})
