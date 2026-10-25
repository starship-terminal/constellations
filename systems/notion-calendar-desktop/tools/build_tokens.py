#!/usr/bin/env python3
"""Build tokens.json (W3C DTCG, Tokens Studio multi-set layout) from the raw readings.

    python3 tools/build_tokens.py

Sources, read live from Notion Calendar 1.142.0 for macOS on 2026-10-25 over the remote-debugging port
(tools/capture/electron/):
  raw/css-vars.<theme>.json      every custom property the window's stylesheets declare, by sheet, selector
                                 and condition, and each name as it computes and paints on <html>
  raw/components.<theme>.json    computed styles of the captured parts, per shot and state (shots.mjs)

How Notion Calendar's colours work, and so how this file is laid out. The window loads the web app from
calendar.notion.so: React with styled-components on Notion's design system custom properties (--nds-*).
One inline sheet declares every name twice, on :root (light) and :root.dark (dark), and the theme is the
`dark` class on <html> (Settings > General > Theme). The --nds-* names come in roles (text, icon, surface,
fill, tint, state, stroke, shadow) and twelve hue ramps; every role also has a -contr- twin that holds the
dark value in both themes, which the always-dark parts (menus, tooltips) use. Older Cron names (--public-*,
--object-*, --layout-*, --calendar-*, --kbs) sit beside them, mostly as var() of an --nds-* name. Each
semantic set holds, per name, the painted colour, or an alias when its declaration is a plain var() of
another kept name that paints the same. The fixed grey scale (--gray10 .. --gray900) is the same in both
themes and goes to core. role.* maps the checklist roles onto those tokens; component.* holds measured
component values, aliased to a token whenever the painted value matches.

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

THEME_NAME = {"light": "Light (Settings > General > Theme: Light mode)",
              "dark": "Dark (Settings > General > Theme: Dark mode, the owner's setting)"}
# name prefix -> token group, in order; the first match wins.
GROUPS = [("--nds-text-", "text"), ("--nds-icon-", "icon"), ("--nds-surface-", "surface"), ("--nds-fill-", "fill"),
          ("--nds-tint-", "tint"), ("--nds-state-", "state"), ("--nds-stroke-", "stroke"), ("--nds-pageGlass-", "glass.page"),
          ("--nds-washGlass-", "glass.wash"), ("--nds-", "palette"), ("--public-", "public"), ("--layout-", "layout"),
          ("--calendar-", "calendar"), ("--object-", "object"), ("--text-", "appText"), ("--material-", "material"),
          ("--", "app")]
HUES = ["gray", "transparentGray", "translucentGray", "uiBlue", "blue", "brown", "green", "orange", "pink", "purple", "red", "yellow"]


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


def length(v):
    """A computed CSS length (px or 0) -> px string; None if it is not one."""
    v = v.strip()
    if v in ("0", "0px"):
        return "0px"
    return px(v) if re.fullmatch(r"-?\d*\.?\d+px", v) else None


def em(v):
    v = v.strip()
    m = re.fullmatch(r"(-?)\.(\d+)(em|px)", v)
    if m:
        v = f"{m.group(1)}0.{m.group(2)}{m.group(3)}"
    return v if re.fullmatch(r"-?\d*\.?\d+(em|px)", v) else None


def applies(d, t):
    """A declaration on <html> in theme t: :root, and :root.dark in dark; not the free-busy overlay or a component class."""
    return not d["condition"] and d["selector"] in ((":root", ":root.dark") if t == "dark" else (":root",))


def formula(t, name):
    """The declaration of `name` that wins on <html> in theme t (the dark rule over the root one in dark)."""
    ds = [d for d in V[t]["decls"] if d["name"] == name and applies(d, t)]
    if not ds:
        return None
    own = [d for d in ds if d["selector"] == ":root.dark"] if t == "dark" else []
    return (own or ds)[-1]["value"].strip()


def path_of(name):
    for pre, group in GROUPS:
        if name.startswith(pre):
            rest = name[len(pre):] or "default"
            if group == "palette":
                m = re.fullmatch(r"(%s)-(\d+)" % "|".join(HUES), rest)
                if m:
                    return (group, m.group(1), m.group(2))
            return tuple(group.split(".")) + (rest,)
    raise KeyError(name)


def where(t, name, extra=""):
    return f"{name} as painted on <html>, {THEME_NAME[t]}, {DATE}{extra}"


# ---------------------------------------------------------------- core: fixed colours and the scales

CORE = {}
dark_comp, light_comp = computed("dark"), computed("light")
for n in sorted(dark_comp, key=lambda n: (len(n), n)):
    m = re.fullmatch(r"--gray(\d+)", n)
    if m and is_color(V["dark"]["colors"].get(n, "")) and color(V["dark"]["colors"][n]) == color(V["light"]["colors"].get(n, "")):
        put(CORE, ("color", "gray", m.group(1)), tok(color(V["dark"]["colors"][n]), "color", "Measured",
            f"{n} as painted (the same in both themes), {DATE}", declared=formula("dark", n)))
for n in ("--white", "--black"):
    put(CORE, ("color", n[2:]), tok(color(V["dark"]["colors"][n]), "color", "Measured", f"{n} as painted (both themes), {DATE}"))


def core_dim(group, key, name, conv=length, ty="dimension", **ext):
    v = dark_comp[name]
    if light_comp.get(name) != v:
        raise ValueError(f"{name} differs by theme")
    out = conv(v)
    if out is None:
        raise ValueError(f"{name}: {v!r}")
    put(CORE, (group,) + (key if isinstance(key, tuple) else (key,)), tok(out, ty, "Measured", f"{name} on <html>, both themes, {DATE}", css=v, **ext))


def shorthand(name, i):
    """The i-th length of a padding shorthand such as `0px 12px` (top/bottom, left/right)."""
    parts = dark_comp[name].split()
    return px(parts[min(i, len(parts) - 1)])


# Radius
for key, n in (("s", "--radius-s"), ("m", "--radius-m"), ("l", "--radius-l"), ("xl", "--radius-xl")):
    core_dim("radius", key, n)
# Spacing: Notion Calendar declares no numbered scale; these are its named spacings.
put(CORE, ("spacing", "button-x"), tok(shorthand("--button-padding", 1), "dimension", "Measured", f"--button-padding ({dark_comp['--button-padding']}) on <html>, {DATE}: horizontal padding of a button"))
put(CORE, ("spacing", "button-x-condensed"), tok(shorthand("--button-padding-condensed", 1), "dimension", "Measured", f"--button-padding-condensed ({dark_comp['--button-padding-condensed']}), {DATE}"))
core_dim("spacing", "button-keys", "--button-padding-keys")
put(CORE, ("spacing", "chip-left"), tok(shorthand("--chip-padding", 3), "dimension", "Measured", f"--chip-padding ({dark_comp['--chip-padding']}), the event chip's left padding (room for the colour ribbon), {DATE}"))
put(CORE, ("spacing", "chip-right"), tok(shorthand("--chip-padding", 1), "dimension", "Measured", f"--chip-padding ({dark_comp['--chip-padding']}), the event chip's right padding, {DATE}"))
for key, n in (("chip-y", "--chip-padding-top"), ("chip-gap-bottom", "--chip-margin-bottom"), ("chip-gap-right", "--chip-margin-right"),
               ("chip-ribbon-gap", "--chip-ribbon-gap"), ("chip-time-top", "--chip-time-margin-top"), ("input-detail", "--input-detail-margin"),
               ("notification-gap", "--notification-spacing"), ("notification-window", "--notifications-window-padding"),
               ("time-column-right", "--time-column-padding-right"), ("db-property-left", "--db-property-values-margin-left")):
    core_dim("spacing", key, n)
# Type
for key, n, note in (("sans", "--nds-font-sans", "Notion's UI stack; resolves to SF Pro on the Mac"),
                     ("sans-app", "--sans-serif-font", "the stack <body> and most of the calendar use"),
                     ("serif", "--nds-font-serif", "Lyon Text is Notion's own face, not loaded by the calendar"),
                     ("mono", "--nds-font-mono", "iA Writer Mono and Nitti are Notion's own faces, not loaded by the calendar"),
                     ("mono-app", "--monospace-font", None),
                     ("compact", "--compact-font", "SF Compact, used for keyboard-shortcut keys")):
    stack = [f.strip().strip("'\"") for f in dark_comp[n].split(",")]
    put(CORE, ("fontFamily", key), tok(stack, "fontFamily", "Measured", f"{n} on <html>, {DATE}", note=note))
for key, n in (("button", "--button-font-size"), ("input", "--input-font-size"), ("chip-title", "--chip-title-font-size"), ("chip-time", "--chip-time-font-size")):
    core_dim("fontSize", key, n)
for key, n in (("button", "--button-line-height"), ("input", "--input-line-height"), ("chip-title", "--chip-title-line-height"), ("chip-time", "--chip-time-line-height")):
    core_dim("lineHeight", key, n)
for key, n in (("button", "--button-letter-spacing"), ("input", "--input-letter-spacing"), ("compact", "--compact-font-letter-spacing")):
    core_dim("letterSpacing", key, n, conv=em)
core_dim("fontWeight", "button", "--button-font-weight", conv=int, ty="fontWeight")
for key in ("button", "input"):
    put(CORE, ("typography", key), tok({"fontFamily": "{fontFamily.sans}", "fontSize": "{fontSize.%s}" % key,
        "fontWeight": int(dark_comp["--button-font-weight"]) if key == "button" else 400, "lineHeight": "{lineHeight.%s}" % key,
        "letterSpacing": "{letterSpacing.%s}" % key}, "typography", "Measured", f"--{key}-font-size, -line-height and -letter-spacing on <html>, {DATE}"))
for key in ("chip-title", "chip-time"):
    put(CORE, ("typography", key), tok({"fontFamily": "{fontFamily.sans-app}", "fontSize": "{fontSize.%s}" % key, "fontWeight": 500 if key == "chip-title" else 400,
        "lineHeight": "{lineHeight.%s}" % key, "letterSpacing": "0px"}, "typography", "Measured",
        f"--{key}-font-size and -line-height on <html>, {DATE}; the weight is the event chip's as rendered"))
# Motion
for key in ("fast", "default", "long", "xlong", "context-panel", "pulsate", "toast-fade-out", "card-flash", "date-flash"):
    n = f"--animation-duration-{key}"
    put(CORE, ("duration", key), tok(ms(dark_comp[n]), "duration", "Measured", f"{n} on <html>, {DATE}", css=dark_comp[n]))
put(CORE, ("duration", "delay-default"), tok(ms(dark_comp["--animation-delay-default"]), "duration", "Measured", f"--animation-delay-default on <html>, {DATE}"))
put(CORE, ("duration", "notification-dismiss"), tok(ms(dark_comp["--notification-dismiss-duration-safe"]), "duration", "Measured", f"--notification-dismiss-duration-safe on <html>, {DATE}"))
for n in sorted(k for k in dark_comp if k.startswith("--ease-")):
    put(CORE, ("easing", n[len("--ease-"):]), tok(bezier(dark_comp[n]), "cubicBezier", "Measured", f"{n} on <html>, {DATE}", css=dark_comp[n]))
put(CORE, ("easing", "default"), tok("{easing.out-quad}", "cubicBezier", "Measured", f"--animation-easing-default = var(--ease-out-quad) on <html>, {DATE}"))
for key, n in (("enter", "--animation-scale-initial-default"), ("exit", "--animation-scale-exit-default")):
    put(CORE, ("scale", key), tok(float(dark_comp[n]), "number", "Measured", f"{n} on <html>, {DATE}: menus and popovers grow from this scale"))
# Opacity
for key, n in (("ghost", "--ghost-opacity"), ("hidden", "--hidden-opacity"), ("dimmed", "--dimmed-opacity"), ("disabled", "--disabled-opacity"),
               ("disabled-destructive", "--disabled-destructive-opacity"), ("icon-secondary", "--icon-secondary-opacity"),
               ("grid-selection-fill", "--grid-selection-fill-opacity"), ("grid-selection-border", "--grid-selection-border-opacity"),
               ("flash", "--card-flash-indicator-opacity")):
    put(CORE, ("opacity", key), tok(float(dark_comp[n]), "number", "Measured", f"{n} on <html>, {DATE}"))
# Sizes
for key, n in (("row", "--base-row-height"), ("button", "--button-height"), ("button-condensed", "--button-height-condensed"),
               ("icon-button", "--icon-button-size"), ("icon-button-md", "--icon-button-size-md"), ("icon-button-sm", "--icon-button-size-sm"),
               ("input-icon", "--input-icon-size"), ("input-icon-box", "--input-icon-container-size"), ("chip-min", "--chip-min-height"),
               ("chip-ribbon", "--chip-ribbon-width"), ("db-compact-property", "--db-compact-property-height")):
    core_dim("size", key, n)
# Layout
for key, n in (("sidebar", "--sidebar-width-default"), ("sidebar-pane", "--sidebar-pane-width-default"), ("context-panel", "--context-panel-width"),
               ("menu-max", "--menu-max-width"), ("notification", "--notification-width"), ("time-column-gutter", "--time-column-left-gutter-width"),
               ("notification-window-fudge", "--notifications-window-outer-fudge-factor-macos")):
    core_dim("layout", key, n)
for n in sorted(k for k in dark_comp if k.startswith("--z-index-")):
    put(CORE, ("zIndex", n[len("--z-index-"):]), tok(int(dark_comp[n]), "number", "Measured", f"{n} on <html>, {DATE}"))
put(CORE, ("blur", "wax"), tok("12px", "dimension", "Measured",
    f"--nds-wax-effect on <html>, {DATE}: blur(12px) behind translucent panels; dark adds brightness(120%)",
    css={"light": light_comp["--nds-wax-effect"], "dark": dark_comp["--nds-wax-effect"]}))
put(CORE, ("borderWidth", "default"), tok("1px", "dimension", "Measured", f"border-top-width of menus, dialogs and panels (computed), {DATE}"))
put(CORE, ("borderWidth", "hairline"), tok("1px", "dimension", "Measured",
    f"the spread of --input-border and --nds-shadow-2xs (inset 0 0 0 1px), the edge every button, field and sidebar draws, {DATE}"))

# ---------------------------------------------------------------- semantic sets

SKIP = re.compile(r"^--(tw-|rdp-)")


def keep(n, painted):
    if SKIP.match(n) or n not in painted or not is_color(painted[n]):
        return False
    if get(CORE, ".".join(("color", "gray", n[6:]))) is not None and re.fullmatch(r"--gray\d+", n):
        return False
    return n not in ("--white", "--black")


def core_ref(n):
    m = re.fullmatch(r"--gray(\d+)", n or "")
    if m:
        return ("color", "gray", m.group(1))
    if n in ("--white", "--black"):
        return ("color", n[2:])
    return None


def semantic(t):
    """Each kept name as its painted colour, or as an alias when its declaration is a plain var() of a kept name
    (or of a core colour) that paints the same."""
    tree, comp, painted = {}, computed(t), V[t]["colors"]
    kept = {n for n in comp if keep(n, painted)}
    paths = {}
    for n in sorted(kept):          # two names must never land on one token path
        if path_of(n) in paths:
            raise ValueError(f"{n} and {paths[path_of(n)]} both map to {'.'.join(path_of(n))}")
        paths[path_of(n)] = n
    for n in sorted(kept):
        value = color(painted[n])
        f = formula(t, n)
        m = re.fullmatch(r"var\(\s*(--[\w-]+)\s*(?:,[^()]*)?\)", (f or "").strip())
        target = m.group(1) if m else None
        tpath = path_of(target) if target in kept else core_ref(target)
        if tpath and target != n and is_color(painted.get(target, "")) and color(painted[target]) == value:
            put(tree, path_of(n), tok("{%s}" % ".".join(tpath), "color", "Measured", where(t, n), formula=f))
        else:
            put(tree, path_of(n), tok(value, "color", "Measured", where(t, n), formula=f if f and f.lower() != value else None))
    return tree


SETS = {t: semantic(t) for t in THEMES}


def resolve(t, value, depth=0):
    m = re.fullmatch(r"\{([^{}]+)\}", value) if isinstance(value, str) else None
    if not m or depth > 20:
        return value
    node = get(SETS[t], m.group(1)) or get(CORE, m.group(1))
    if node is None:
        raise KeyError(f"{t}: {value} points at nothing")
    return resolve(t, node["$value"], depth + 1)


# Gradients per theme: Notion's buttons and segmented controls paint a faint top-to-bottom fill (--neutral-gradient-bg).
GRADIENTS = {"--neutral-gradient-bg": "neutral", "--neutral-gradient-contr-bg": "neutral-contr",
             "--neutral-gradient-contr-elevated-bg": "neutral-contr-elevated", "--object-gradient-bg": "object"}


def gradient(css):
    """`linear-gradient(#a,#b)` (top to bottom, two stops) -> DTCG gradient stops; None for anything else."""
    import re as _re
    m = _re.fullmatch(r"linear-gradient\(\s*([^,()]+(?:\([^()]*\))?)\s*,\s*([^,()]+(?:\([^()]*\))?)\s*\)", css.strip())
    if not m or not (is_color(m.group(1)) and is_color(m.group(2))):
        return None
    return [{"color": color(m.group(1)), "position": 0}, {"color": color(m.group(2)), "position": 1}]


for t in THEMES:
    for n, key in GRADIENTS.items():
        g = gradient(computed(t)[n])
        if g:
            put(SETS[t], ("gradient", key), tok(g, "gradient", "Measured", f"{n} as computed on <html> (top to bottom), {THEME_NAME[t]}, {DATE}", css=computed(t)[n]))

# Shadows per theme, from the computed value on <html> (custom properties compute with their var()s replaced).
SHADOWS = ["--nds-shadow-2xs", "--nds-shadow-xs", "--nds-shadow-sm", "--nds-shadow-md", "--nds-shadow-lg",
           "--nds-shadow-contr-2xs", "--nds-shadow-contr-xs", "--nds-shadow-contr-sm", "--nds-shadow-contr-md", "--nds-shadow-contr-lg",
           "--elevation-low", "--elevation-middle", "--elevation-high", "--elevation-low-material-border-inside",
           "--elevation-middle-material-border-inside", "--elevation-high-material-border-inside", "--highlight-focus",
           "--highlight-contr-focus", "--highlight-light", "--highlight-cursor", "--input-border", "--input-highlight-border",
           "--input-error-border", "--public-elevation-low", "--public-elevation-high"]
for t in THEMES:
    for n in SHADOWS:
        css = computed(t).get(n)
        if not css or css == "none":
            continue
        key = n.replace("--nds-shadow-", "").replace("--", "")
        put(SETS[t], ("shadow", key), tok(shadow(css), "shadow", "Measured", f"{n} as computed on <html>, {THEME_NAME[t]}, {DATE}", css=css))

# ---------------------------------------------------------------- measured components


def parts(t):
    """{(part, state): (shot, style)} from the first shot that measured it."""
    out = {}
    for shot, d in C[t].items():
        for part, v in d["parts"].items():
            if "style" in v and not skip(shot, part, d["state"]):
                out.setdefault((part, d["state"]), (shot, v["style"]))
    return out


P = {t: parts(t) for t in THEMES}


def style(t, part, state="default"):
    hit = P[t].get((part, state))
    if not hit and state == "default":
        hit = next((v for (p, s), v in sorted(P[t].items()) if p == part), None)
    return hit if hit else (None, None)


# Type roles, measured on real elements.
ROLES = [("display", "month-title", "The month and year over the grid (October 2026)"),
         ("heading", "settings-heading", "Settings section titles (Calendar view)"),
         ("command", "command-input", "Text typed in the command menu"),
         ("row", "command-row", "Command menu rows"),
         ("body", "settings-text", "Settings descriptions and panel rows"),
         ("label", "today-button", "Button labels (Today, Week)"),
         ("day-header", "day-header", "Day headers over the grid (Tue 20)"),
         ("caption", "week-label", "The week number beside the month (Week 43)"),
         ("section-label", "command-heading", "Group headings in menus and settings navigation (Navigation, Account)"),
         ("tooltip", "tooltip", "Tooltips"),
         ("micro", "mini-weekday", "Mini calendar weekdays and time-zone labels (Mo, SF)"),
         ("kbd", "kbd", "Keyboard-shortcut keys")]
for role, part, use in ROLES:
    shot, s = style("dark", part)
    if not s:
        continue
    fam = "{fontFamily.compact}" if role == "kbd" else "{fontFamily.sans}"
    lh = s["line-height"]
    val = {"fontFamily": fam, "fontSize": px(s["font-size"]), "fontWeight": int(s["font-weight"]),
           "lineHeight": px(lh) if lh.endswith("px") else px("%gpx" % round(float(s["font-size"][:-2]) * 1.2, 1)),
           "letterSpacing": px(s["letter-spacing"]) if s["letter-spacing"].endswith("px") else "0px"}
    put(CORE, ("typography", role), tok(val, "typography", "Measured", f"computed style of {part} in {shot}, dark, {DATE}; {use}",
        note=None if lh.endswith("px") else "computed line-height is normal; 1.2 x the size is used here"))


def dim_of(part, prop, state="default", t="dark"):
    shot, s = style(t, part, state)
    return (shot, s[prop]) if s and s.get(prop, "").endswith("px") else (None, None)


SIZES = [("size.control.button", "today-button", "height", "Header buttons (Today, Week)"),
         ("size.control.icon-button", "nav-arrow", "height", "Header and sidebar icon buttons"),
         ("size.control.calendar-row", "calendar-row", "height", "Sidebar calendar rows"),
         ("size.control.menu-row", "menu-row", "height", "Menu rows"),
         ("size.control.command-row", "command-row", "height", "Command menu rows"),
         ("size.control.mini-day", "mini-day", "height", "Mini calendar days"),
         ("size.control.select", "select", "height", "Settings selects"),
         ("size.control.text-field", "text-field", "height", "Settings text fields"),
         ("size.control.switch-width", "switch-on", "width", "Switch track"),
         ("size.control.switch-height", "switch-on", "height", "Switch track"),
         ("size.control.kbd", "kbd", "height", "Keyboard-shortcut keys"),
         ("size.control.avatar", "avatar", "height", "The profile avatar"),
         ("size.control.now-badge", "now-badge", "height", "The current-time badge in the time column"),
         ("size.hour", None, None, None),
         ("layout.sidebar-measured", "sidebar", "width", "Sidebar"),
         ("layout.menu", "menu", "width", "The view menu"),
         ("layout.command-menu", "command-menu", "width", "The command menu"),
         ("layout.dialog", "dialog", "width", "The settings dialog"),
         ("layout.panel", "panel", "width", "The event popover (floating context panel)"),
         ("layout.scheduling-pane", "pane", "width", "The scheduling pane")]
for path, part, prop, use in SIZES:
    if part is None:
        continue
    shot, v = dim_of(part, prop)
    if v:
        put(CORE, tuple(path.split(".")), tok(px(v), "dimension", "Measured", f"computed {prop} of {part} in {shot}, dark, {DATE} ({use})"))
shot, s = style("dark", "time-column")
put(CORE, ("size", "hour"), tok(px("%gpx" % round(float(s["height"][:-2]) / 24, 2)), "dimension", "Measured",
    f"the time column's height ({s['height']}) over 24 hours in {shot}, {DATE}: one hour of the week grid"))
WINDOW = C["dark"]["week-default"]["viewport"]
put(CORE, ("layout", "window-width"), tok(f"{WINDOW['css'][0]}px", "dimension", "Measured",
    f"the window's viewport, {WINDOW['css'][0]} x {WINDOW['css'][1]} CSS px at devicePixelRatio {WINDOW['dpr']}, {DATE}"))
put(CORE, ("layout", "window-height"), tok(f"{WINDOW['css'][1]}px", "dimension", "Measured", f"the window's viewport height, {DATE}"))
# Component radii, measured.
for key, part in (("control", "today-button"), ("menu", "menu"), ("dialog", "dialog"), ("panel", "panel"), ("chip", "event-chip"),
                  ("switch", "switch-on"), ("kbd", "kbd"), ("badge", "now-badge"), ("card", "settings-card")):
    shot, v = dim_of(part, "border-top-left-radius")
    if v:
        put(CORE, ("radius", key), tok(px(v), "dimension", "Measured", f"computed border-top-left-radius of {part} in {shot}, dark, {DATE}"))
put(CORE, ("radius", "full"), tok("9999px", "dimension", "Measured", f"the avatar's 50% radius (computed) in week-default, {DATE}"))
# Focus ring: a box-shadow, read on a focused control: a 1px accent ring and a 4px tinted halo (--highlight-focus).
shot, s = style("dark", "today-button", "focus-visible")
layers = shadow(s["box-shadow"])
put(CORE, ("focusRing", "width"), tok(layers[0]["spread"], "dimension", "Measured", f"spread of the first focus box-shadow layer of today-button in {shot}, dark, {DATE}", css=s["box-shadow"]))
put(CORE, ("focusRing", "halo"), tok(layers[1]["spread"], "dimension", "Measured", f"spread of the second, tinted layer of the same focus shadow, {DATE}"))
put(CORE, ("focusRing", "offset"), tok("0px", "dimension", "Measured", f"the ring is a box-shadow on the control's edge ({shot}), {DATE}"))
put(CORE, ("borderWidth", "focus"), tok("{focusRing.width}", "dimension", "Derived", "the focus ring's width"))
rm = {k: v["rules"] for k, v in V["dark"]["conditions"].items() if "reduced-motion" in k}
CORE["duration"]["$extensions"] = {"reducedMotion": {"rules": rm,
    "how": "a prefers-reduced-motion: reduce rule in the app sheet; no duration token changes and the app has no setting of its own"}}

# ---------------------------------------------------------------- roles and components, per theme

ROLE = {
    "page": ("{surface.page}", "the week grid, the scheduling pane and the main area"),
    "surface": ("{surface.wash}", "the sidebar"),
    "raised": ("{surface.elevated}", "the settings dialog, the context panel when docked"),
    "overlay": ("{surface.elevated-wax}", "translucent floating panels: the event popover, the command menu, the shortcuts panel (with the wax blur)"),
    "scrim": ("{material.dim}", "the tint behind the settings dialog and the command menu"),
    "text.primary": ("{text.primary}", ""), "text.secondary": ("{text.secondary}", ""), "text.disabled": ("{text.tertiary}", "also the dimmed section labels"),
    "text.on-accent": ("{text.contrastPrimary}", "opaque white, as the primary button's label paints in both themes"),
    "text.link": ("{text.uiBluePrimary}", "Notion's link blue; settings links are underlined secondary text instead"),
    "border.default": ("{stroke.secondary}", "the hairline every button, field, menu and the sidebar draw (an inset 1px shadow)"),
    "border.strong": ("{stroke.primary}", "the hovered or highlighted field edge (--input-highlight-border)"),
    "border.focus": ("{stroke.uiBluePrimary}", "the focus ring colour"),
    "accent.default": ("{fill.uiBlue}", "the primary button, the on switch, the selected scheduling action"),
    "accent.subtle": ("{fill.uiBlueSecondary}", "the accent at a low alpha"),
}
for s_, fill, text, sub, border in (("success", "fill.greenPrimary", "text.greenSecondary", "fill.greenTertiary", "stroke.greenPrimary"),
                                    ("warning", "fill.yellowPrimary", "text.uiYellowPrimary", "fill.yellowTertiary", "stroke.yellowPrimary"),
                                    ("danger", "fill.uiRed", "text.uiRedPrimary", "fill.uiRedSecondary", "stroke.uiRedPrimary"),
                                    ("info", "fill.uiBlue", "text.uiBluePrimary", "fill.uiBlueSecondary", "stroke.uiBluePrimary")):
    ROLE[f"status.{s_}.fill"] = ("{%s}" % fill, "")
    ROLE[f"status.{s_}.text"] = ("{%s}" % text, "")
    ROLE[f"status.{s_}.subtle"] = ("{%s}" % sub, "")
    ROLE[f"status.{s_}.border"] = ("{%s}" % border, "")

COMPONENTS = [
    ("button-primary", "button-primary", {"bg": "background-color", "text": "color", "radius": "border-top-left-radius", "height": "height", "padding": "padding-left"}),
    ("button-secondary", "today-button", {"text": "color", "radius": "border-top-left-radius", "height": "height", "padding": "padding-left"}),
    ("button-danger", "button-danger", {"text": "color", "radius": "border-top-left-radius", "height": "height"}),
    ("icon-button", "nav-arrow", {"text": "color", "radius": "border-top-left-radius", "size": "height"}),
    ("sidebar", "sidebar", {"bg": "background-color", "text": "color", "width": "width"}),
    ("calendar-row", "calendar-row", {"text": "color", "radius": "border-top-left-radius", "height": "height"}),
    ("account-header", "account-header", {"text": "color", "radius": "border-top-left-radius", "height": "height"}),
    ("scheduling-row-selected", "scheduling-row-selected", {"bg": "background-color", "text": "color", "radius": "border-top-left-radius"}),
    ("mini-day", "mini-day", {"text": "color", "size": "height"}),
    ("mini-day-today", "mini-day-today", {"bg": "background-color", "text": "color"}),
    ("mini-weekday", "mini-weekday", {"text": "color"}),
    ("month-title", "month-title", {"text": "color"}),
    ("week-label", "week-label", {"text": "color"}),
    ("day-header", "day-header", {"text": "color"}),
    ("day-header-today", "day-header-today", {"text": "color"}),
    ("now-badge", "now-badge", {"bg": "background-color", "text": "color", "radius": "border-top-left-radius", "height": "height"}),
    ("event-chip", "event-chip", {"radius": "border-top-left-radius", "padding": "padding-left"}),
    ("menu", "menu", {"bg": "background-color", "border": "border-top-color", "text": "color", "radius": "border-top-left-radius", "width": "width"}),
    ("menu-row", "menu-row", {"text": "color", "radius": "border-top-left-radius", "height": "height", "padding": "padding-left"}),
    ("menu-row-danger", "menu-row-danger", {"text": "color"}),
    ("tooltip", "tooltip", {"bg": "background-color", "border": "border-top-color", "text": "color", "radius": "border-top-left-radius", "height": "height"}),
    ("panel", "panel", {"bg": "background-color", "border": "border-top-color", "text": "color", "radius": "border-top-left-radius", "width": "width"}),
    ("command-menu", "command-menu", {"bg": "background-color", "border": "border-top-color", "radius": "border-top-left-radius", "width": "width"}),
    ("command-row-selected", "command-row-selected", {"bg": "background-color", "text": "color", "radius": "border-top-left-radius", "height": "height"}),
    ("command-heading", "command-heading", {"text": "color"}),
    ("dialog", "dialog", {"bg": "background-color", "border": "border-top-color", "text": "color", "radius": "border-top-left-radius"}),
    ("settings-nav-selected", "settings-nav-selected", {"bg": "background-color", "text": "color", "radius": "border-top-left-radius", "height": "height"}),
    ("settings-section-label", "settings-section-label", {"text": "color"}),
    ("select", "select", {"text": "color", "radius": "border-top-left-radius", "height": "height", "padding": "padding-left"}),
    ("text-field", "text-field", {"text": "color", "radius": "border-top-left-radius", "height": "height"}),
    ("switch-on", "switch-on", {"bg": "background-color", "radius": "border-top-left-radius", "width": "width", "height": "height"}),
    ("kbd", "kbd", {"bg": "background-color", "text": "color", "radius": "border-top-left-radius"}),
    ("pane", "pane", {"bg": "background-color", "width": "width"}),
    ("settings-card", "settings-card", {"radius": "border-top-left-radius"}),
]
STATES = [("hover", "bg-hover", "background-color"), ("hover", "text-hover", "color"), ("pressed", "bg-pressed", "background-color"),
          ("focus-visible", "bg-focus", "background-color")]
CORE_NAMES = re.compile(r"^(surface\.(page|wash|elevated|elevated-wax)|text\.(primary|secondary|tertiary|contr-primary)|stroke\.(primary|secondary)|state\.(hover|pressed)|fill\.uiBlue)$")
AWKWARD = re.compile(r"Elevated|contr-contrast|lightGray|public|object|appText|kbs|bg-selected|palette|layout|tint|glass")
PREFER = ["role", "surface", "text", "state", "stroke", "fill", "tint", "icon", "material", "object", "appText", "app", "layout", "calendar", "public", "glass", "palette", "color"]


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
        vals.sort(key=lambda p: (not CORE_NAMES.match(p), bool(AWKWARD.search(p)), PREFER.index(p.split(".")[0]) if p.split(".")[0] in PREFER else 99, len(p), p))
    return idx


def build_roles_and_components(t):
    tree = SETS[t]
    for key, spec in ROLE.items():
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
                kinds = {"color": ("text", "icon", "object", "appText", "app", "calendar", "color", "stroke"),
                         "background-color": ("surface", "fill", "state", "tint", "material", "app", "color", "calendar", "object", "palette"),
                         "border-top-color": ("stroke", "object", "tint", "fill"), "outline-color": ("stroke", "text")}[prop]
                fits = [x for x in idx[v] if x.split(".")[0] in kinds]
                if fits:
                    aliased_n += 1
                    first = {"color": "text", "background-color": "surface", "border-top-color": "stroke", "outline-color": "stroke"}[prop]
                    pref = [x for x in fits if x.split(".")[0] == first]
                    return tok("{%s}" % (pref or fits)[0], "color", "Measured", src, painted=v)
            return tok(v, "color", "Measured", src)
        return tok(px(raw) if raw.endswith("px") else raw, "dimension", "Measured", src)
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
            # Notion's buttons paint hover and pressed as a gradient over the fill (background-image).
            if ss and prop == "background-color" and ss.get("background-image", "none") != s.get("background-image", "none"):
                m = re.search(r"linear-gradient\([^,]+,\s*(rgba?\([^)]+\))", ss["background-image"])
                if m:
                    put(tree, ("component", name, key), value_for(part, sh, prop, m.group(1)))
    # A button whose rest fill is a gradient: name the gradient token it paints.
    for name, part in (("button-secondary", "today-button"),):
        shot, s = style(t, part)
        g = gradient(s.get("background-image", "")) if s else None
        for key, tk in (tree.get("gradient") or {}).items():
            if g and tk["$value"] == g:
                put(tree, ("component", name, "bg-gradient"), tok("{gradient.%s}" % key, "gradient", "Measured",
                    f"computed background-image of {part} in {shot}, {THEME_NAME[t]}, {DATE}", css=s["background-image"]))
                break
    for key, comp_path, why in (("accent.hover", "component.switch-on.bg-hover", "the on switch under the pointer"),
                                ("accent.pressed", "component.switch-on.bg-pressed", "the on switch while pressed")):
        hit = get(tree, comp_path)
        if not hit:
            raise KeyError(f"{t}: {comp_path} missing for role.{key}")
        put(tree, ("role",) + tuple(key.split(".")), tok(hit["$value"], "color", "Measured", hit["$extensions"]["source"]["from"] + f"; {why}"))
    tree["$extensions"] = {"componentValues": {"measured": measured_n, "aliased": aliased_n}}


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
    """A name present in only one theme is not a theme token: move it out (an alias to it becomes its value)."""
    for _ in range(5):
        names = {t: {n for n, _ in tokens_of(SETS[t])} for t in THEMES}
        moved = False
        for t in THEMES:
            other = names["dark" if t == "light" else "light"]
            for n in sorted(names[t] - other):
                path = n.split(".")
                node = SETS[t]
                for k in path[:-1]:
                    node = node[k]
                v = node.pop(path[-1])
                SETS[t].setdefault("$extensions", {}).setdefault("notTokenised", []).append(
                    {"name": n, "value": v["$value"], "why": f"present only while capturing {t}; not in the other theme"})
                moved = True
            for n, v in list(tokens_of(SETS[t])):
                for a in aliases(v["$value"]):
                    if get(SETS[t], a) is None and get(CORE, a) is None:
                        v["$extensions"]["aliasOf"] = a
                        v["$value"] = v["$extensions"].get("painted") or resolve_removed(t, a)
        if not moved:
            break


def resolve_removed(t, a):
    for item in SETS[t].get("$extensions", {}).get("notTokenised", []):
        if item["name"] == a:
            return resolve(t, item["value"]) if isinstance(item["value"], str) else item["value"]
    raise KeyError(a)


reconcile()
for t in THEMES:   # empty groups left by reconcile
    def prune(node):
        for k in [k for k, v in node.items() if isinstance(v, dict) and "$value" not in v and not k.startswith("$")]:
            prune(node[k])
            if not [x for x in node[k] if not x.startswith("$")]:
                del node[k]
    prune(SETS[t])
check()
tokens = {
    "core": CORE, "light": SETS["light"], "dark": SETS["dark"],
    "$themes": [
        {"id": "light", "name": "Light", "selectedTokenSets": {"core": "source", "light": "enabled"},
         "$description": "Settings > General > Theme: Light mode (no class on <html>)"},
        {"id": "dark", "name": "Dark", "selectedTokenSets": {"core": "source", "dark": "enabled"},
         "$description": "Settings > General > Theme: Dark mode, the owner's setting (html.dark)"},
    ],
    "$metadata": {"tokenSetOrder": ["core", "light", "dark"]},
}
(PKG / "tokens.json").write_text(json.dumps(tokens, indent=2, ensure_ascii=False) + "\n")


def count(d):
    return sum(1 for _ in tokens_of(d))


print({k: count(tokens[k]) for k in ("core", "light", "dark")}, "component values aliased:",
      {t: SETS[t]["$extensions"]["componentValues"] for t in THEMES})
