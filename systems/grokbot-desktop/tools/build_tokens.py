#!/usr/bin/env python3
"""Build tokens.json (W3C DTCG, Tokens Studio multi-set layout) from the raw readings.

    python3 tools/build_tokens.py

Sources, read live from Grok Bot 0.75.5 for macOS on 2026-10-25 over the remote-debugging port
(tools/capture/electron/):
  raw/css-vars.<theme>.json      every --sand-*, --cursor-*, --ui-* (and a few product) custom properties the
                                 window's stylesheets declare, by sheet, selector and condition, and each name
                                 as it computes and paints on :root
  raw/components.<theme>.json    computed styles of the captured parts, per shot and state (shots.mjs)

How Grok Bot's colours work, and so how this file is laid out. Grok Bot (bundle id com.anysphere.sand)
has two layers. Its own, sand, is a flat list of literal colours per theme, written on :root by the
sand-cursor-theme style element: backgrounds (pane, chrome, sidebar, elevated, the scrim, primary and
secondary fills with hover and disabled steps, and twelve hues at bright, primary and secondary),
borders, text and icon tiers, bubble fills, specular highlights and a dataviz palette. Under it sits the
anysphere-ui kit Cursor is built on (--cursor-*), whose seeds the same element writes and whose
neutrals are mostly re-pointed at sand (--cursor-bg-elevated: var(--sand-bg-elevated)). So the
semantic sets hold sand's groups at the top level (bg, border, text, icon, fill, specular, dataviz,
transcript, prompt), the kit under kit.* (aliased to a sand token wherever its formula is a plain var()
of one that paints the same), shadows, the checklist roles (role.*) and measured component values
(component.*). Scales that do not change with the theme are the core set.

Every token carries $extensions.source = {evidence, from}. Deterministic: same inputs, same bytes.
"""
import json
import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from colour import color, is_color, ms, px, shadow  # noqa: E402

PKG = pathlib.Path(__file__).resolve().parent.parent
RAW = PKG / "raw"
THEMES = ["light", "dark"]
DATE = "2026-10-25"

# ---------------------------------------------------------------- PRODUCT (adapt): what the readings are

THEME_SHEET = "sand-cursor-theme"
THEME_NAME = {"light": "Light", "dark": "Dark"}
SCOPE = ":root"
# sand groups kept as colour tokens, by the name's second word (--sand-<group>-...)
SAND_GROUPS = ["bg", "border", "text", "icon", "fill", "specular", "dataviz", "transcript", "prompt", "activity", "shadow"]
# kit groups kept, by the name's second word (--cursor-<group>-...); one-word names are the kit's seeds
KIT_GROUPS = ["bg", "text", "stroke", "icon", "button", "control", "accent", "blue", "brown", "cyan", "danger", "green", "magenta",
              "orange", "purple", "red", "success", "warn", "yellow", "diff", "added", "modified", "removed", "untracked", "focus",
              "input", "progress", "syntax", "on", "border"]
KIT_SKIP = re.compile(r"^--cursor-(spacing|radius|height|font|line-height|letter-spacing|duration|easing|elevation|scrollbar|focus-ring|"
                      r"box-shadow|shadow|editor|terminal|titlebar|toolbar|command|specular)")
SHADOWS = ["--sand-shadow-inline", "--sand-shadow-popover", "--sand-shadow-modal", "--sand-shadow-window", "--ui-tooltip-box-shadow"]


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


def computed(t):
    return V[t]["computed"][V[t]["scope"]]


def effective(t, name):
    """The declaration that wins on :root: the last unconditioned one whose selector names :root, in
    document order (the theme element comes last). Returns (value, sheet) or (None, None)."""
    hit = (None, None)
    for d in V[t]["decls"]:
        if d["name"] == name and d["condition"] == "" and ":root" in d["selector"] and "not(" not in d["selector"]:
            hit = (d["value"], d["sheet"])
    return hit


LITERAL = re.compile(r"^(#[0-9a-fA-F]{3,8}|oklch\([^)]*\)|rgba?\([^)]*\)|color\([^)]*\)|transparent)$")


def where(t, name, extra=""):
    return f"{name} on :root, {THEME_NAME[t]} theme, {DATE}{extra}"


def sand_path(name):
    """--sand-bg-pane -> ('bg', 'pane'); --sand-fill-bubble-user -> ('fill', 'bubble-user')."""
    head, _, tail = name[len("--sand-"):].partition("-")
    return (head, tail or "default")


def kit_path(name):
    """--cursor-bg-elevated -> ('kit', 'bg', 'elevated'); --cursor-base -> ('kit', 'seed', 'base')."""
    head, _, tail = name[len("--cursor-"):].partition("-")
    return ("kit", "seed", head) if not tail else ("kit", head, tail)


# ---------------------------------------------------------------- semantic sets


def semantic(t):
    tree, comp, painted = {}, computed(t), V[t]["colors"]
    paths = {}
    sand = sorted(n for n in comp if n.startswith("--sand-") and sand_path(n)[0] in SAND_GROUPS and n in painted and is_color(painted[n])
                  and not re.search(r"(radius|padding|height|gap|width|blur|size)", n))
    kit = sorted(n for n in comp if n.startswith("--cursor-") and not KIT_SKIP.match(n) and n in painted and is_color(painted[n])
                 and (kit_path(n)[1] in KIT_GROUPS or kit_path(n)[1] == "seed"))
    for n in sand:
        paths[n] = sand_path(n)
    for n in kit:
        paths[n] = kit_path(n)
    for n in sand + kit:
        p = paths[n]
        value = color(painted[n])
        decl, sheet = effective(t, n)
        if decl and LITERAL.match(decl.strip()):
            put(tree, p, tok(value, "color", "Measured", f"{n} = {decl} on :root ({sheet}), {THEME_NAME[t]} theme, {DATE}"))
            continue
        m = re.fullmatch(r"var\((--(?:sand|cursor)-[\w-]+)\)", (decl or "").strip())
        if m and m.group(1) in paths and is_color(painted.get(m.group(1), "none")) and color(painted[m.group(1)]) == value:
            put(tree, p, tok("{%s}" % ".".join(paths[m.group(1)]), "color", "Measured", where(t, n), formula=decl))
        else:
            put(tree, p, tok(value, "color", "Measured", where(t, n), formula=decl or comp[n]))
    # Focus: Grok Bot paints its focus tokens transparent until a Tab press sets [data-sand-keyboard-nav]
    # on the root (`:root:not([data-sand-keyboard-nav]) { --sand-border-focus-primary: transparent !important; ... }`).
    # Every name that rule hides gets the value it switches to: the theme's own declaration, resolved
    # in order so a var() of a restored name follows it (a literal, a var(), or a color-mix with transparent).
    hidden = sorted({d["name"] for d in V[t]["decls"] if d["selector"].startswith(":root:not([data-sand-keyboard-nav])")})
    keyboard = {}
    for _ in range(3):
        for n in hidden:
            if n not in paths:
                continue
            decl, sheet = effective(t, n)
            decl = (decl or "").strip()
            src = f"{n} = {decl} on :root ({sheet}), {THEME_NAME[t]} theme, {DATE}; painted only while [data-sand-keyboard-nav] is set"
            ref = re.fullmatch(r"var\((--[\w-]+)\)", decl)
            mix = re.fullmatch(r"color-mix\(in srgb, var\((--[\w-]+)\) ([\d.]+)%, transparent\)", decl)
            if LITERAL.match(decl):
                keyboard[n] = color(decl)
                put(tree, paths[n], tok(keyboard[n], "color", "Measured", src))
            elif ref and ref.group(1) in paths:
                keyboard[n] = keyboard.get(ref.group(1)) or color(painted[ref.group(1)])
                put(tree, paths[n], tok("{%s}" % ".".join(paths[ref.group(1)]), "color", "Measured", src, formula=decl))
            elif mix and mix.group(1) in paths:
                base = keyboard.get(mix.group(1)) or color(painted[mix.group(1)])
                m = re.fullmatch(r"#([0-9a-f]{2})([0-9a-f]{2})([0-9a-f]{2})|rgba\((\d+), (\d+), (\d+), ([\d.]+)\)", base)
                rgb = [int(x, 16) for x in m.groups()[:3]] if m.group(1) else [int(x) for x in m.groups()[3:6]]
                alpha = (1 if m.group(1) else float(m.group(7))) * float(mix.group(2)) / 100
                keyboard[n] = "rgba(%d, %d, %d, %s)" % (rgb[0], rgb[1], rgb[2], "%g" % round(alpha, 3))
                put(tree, paths[n], tok(keyboard[n], "color", "Derived", src + "; mixed here from the restored colour", formula=decl))
    for n in SHADOWS:
        if n in V[t]["shadows"]:
            key = n.replace("--sand-shadow-", "").replace("--ui-", "").replace("-box-shadow", "")
            layers = [l for l in shadow(V[t]["shadows"][n]) if not l["color"].endswith(", 0)")]
            put(tree, ("shadow", key), tok(layers, "shadow", "Measured", where(t, n, "; box-shadow as painted, fully transparent layers dropped"),
                formula=comp.get(n)))
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


BASE_STATES = ["default", "selected", "hover"]


def style(t, part, state="default"):
    """A part's reading in a state. For "default", a part never read at rest (a selected row, a tooltip
    that only exists under the pointer) falls back to its base state: selected, then hover."""
    hit = P[t].get((part, state))
    if not hit and state == "default":
        hit = next((P[t][(part, s)] for s in BASE_STATES if (part, s) in P[t]), None)
    return hit if hit else (None, None)


# ---------------------------------------------------------------- core

CORE = {}
dark_comp, light_comp = computed("dark"), computed("light")

CORE_SCALES = [("--cursor-radius-", "radius"), ("--cursor-spacing-", "spacing"), ("--cursor-height-", "controlHeight"),
               ("--sand-font-size-", "fontSize"), ("--sand-line-height-", "lineHeight"), ("--cursor-duration-", "duration"),
               ("--cursor-font-size-", "kit.fontSize"), ("--cursor-line-height-", "kit.lineHeight"), ("--cursor-letter-spacing-", "kit.letterSpacing")]
SAND_METRICS = [("--sand-menu-", "menu"), ("--sand-search-menu-", "searchMenu"), ("--sand-command-palette-", "palette"),
                ("--sand-new-chat-menu-", "newChatMenu"), ("--sand-agent-item-", "botItem"), ("--sand-transcript-prose-", "transcript"),
                ("--ui-tooltip-", "tooltip")]


def core_scales():
    for n in sorted(dark_comp):
        if "-ne-" in n or "shadow" in n:
            continue
        for pre, group in CORE_SCALES + SAND_METRICS:
            if not n.startswith(pre):
                continue
            v = dark_comp[n]
            if light_comp.get(n) != v:
                raise ValueError(f"{n} differs by theme: {v} / {light_comp.get(n)}")
            key = n[len(pre):].replace(".", "-")
            src = f"{n} on :root, both themes, {DATE}"
            path = tuple(group.split(".")) + (key,)
            if group == "duration":
                put(CORE, path, tok(ms(v), "duration", "Measured", src))
            elif re.fullmatch(r"-?[\d.]+px", v):
                put(CORE, path, tok(px(v), "dimension", "Measured", src))
            elif re.fullmatch(r"-?[\d.]*em", v) and group == "tooltip":
                put(CORE, path, tok("0px", "dimension", "Measured", src + f" ({v})"))
            elif re.fullmatch(r"\d+", v):
                put(CORE, path, tok(int(v), "number", "Measured", src))
            break


core_scales()

# Letter spacing is declared in em per size step (--sand-letter-spacing-xl: -.008em); DTCG dimensions are
# px or rem, so each is written in px at its own step's font size, with the em value kept.
for n in sorted(dark_comp):
    if n.startswith("--sand-letter-spacing-"):
        step = n[len("--sand-letter-spacing-"):]
        em = float(dark_comp[n].replace("em", "") or 0)
        size = float(dark_comp[f"--sand-font-size-{step}"][:-2])
        put(CORE, ("letterSpacing", step), tok(px("%gpx" % round(em * size, 3)), "dimension", "Derived",
            f"{n} = {dark_comp[n]} on :root x --sand-font-size-{step} ({size:g}px), {DATE}", em=dark_comp[n]))
for key, n in (("regular", "--sand-font-weight-regular"), ("medium", "--sand-font-weight-medium"), ("semibold", "--sand-font-weight-semibold"),
               ("bold", "--cursor-font-weight-bold"), ("code", "--cursor-font-weight-normal-code")):
    put(CORE, ("fontWeight", key), tok(int(dark_comp[n]), "fontWeight", "Measured", f"{n} on :root, {DATE}",
        note="set inline on the root by the app (420 for regular text, not 400)" if key == "regular" else None))
for key, n in (("sans", "--cursor-font-family-sans"), ("mono", "--cursor-font-family-mono")):
    stack = [f.strip().strip("'\"") for f in dark_comp[n].split(",")]
    put(CORE, ("fontFamily", key), tok(stack, "fontFamily", "Measured", f"{n} on :root, {DATE}"))
put(CORE, ("focusRing", "width"), tok(px(dark_comp["--cursor-focus-ring-width"]), "dimension", "Measured", f"--cursor-focus-ring-width on :root, {DATE}"))
put(CORE, ("focusRing", "offset"), tok(px(dark_comp["--cursor-focus-ring-offset"]), "dimension", "Measured", f"--cursor-focus-ring-offset on :root, {DATE}"))
put(CORE, ("blur", "background"), tok(px(dark_comp["--sand-blur-background"]), "dimension", "Measured", f"--sand-blur-background on :root, {DATE}"))
put(CORE, ("press", "scale"), tok(float(dark_comp["--ui-press-scale"]), "number", "Measured", f"--ui-press-scale on :root, {DATE}"))
put(CORE, ("zoom", "factor"), tok(float(dark_comp["--sand-zoom-factor"]), "number", "Measured",
    f"--sand-zoom-factor on :root (inline), {DATE}: the window renders at 1.1 x, a devicePixelRatio of 2.2 on a 2x display",
    note="Every px value here is the CSS px the stylesheets declare, before this zoom"))

# Type roles, measured on real elements (computed style; both themes agree).
# Only parts whose own computed style is their text: a container (a settings row, a tile) reports the
# inherited size of the box, not of the label in it, so those are left to the size scale.
ROLES = [("body", "message-prose", "Agent replies in the conversation"),
         ("prompt", "prompt-field", "Text typed in the composer"),
         ("list", "section-header", "Sidebar group headers"),
         ("button", "button-secondary", "Button labels"),
         ("caption", "time-separator", "Time separators in the transcript"),
         ("code", "inline-code", "Inline code in replies (0.93em of the reply)")]
for role, part, use in ROLES:
    shot, s = style("dark", part)
    if not s:
        continue
    # the element's own text style: a container part reports the inherited values of its text
    fam = "{fontFamily.mono}" if role == "code" else "{fontFamily.sans}"
    lh = s["line-height"]
    val = {"fontFamily": fam, "fontSize": px(s["font-size"]), "fontWeight": int(float(s["font-weight"])),
           "lineHeight": px(lh) if lh.endswith("px") else px("%gpx" % round(float(s["font-size"][:-2]) * 1.2, 1)),
           "letterSpacing": px(s["letter-spacing"]) if s["letter-spacing"].endswith("px") else "0px"}
    put(CORE, ("typography", role), tok(val, "typography", "Measured", f"computed style of {part} in {shot}, dark, {DATE}; {use}",
        note=None if lh.endswith("px") else "computed line-height is normal; 1.2 x the size is used here"))


def dim_of(part, prop, state="default", t="dark"):
    shot, s = style(t, part, state)
    return (shot, s[prop]) if s and s.get(prop, "").endswith("px") else (None, None)


SIZES = [("size.control.icon-button", "icon-button", "height", "Sidebar icon buttons (Search, New Bot)"),
         ("size.control.composer-button", "attach-button", "height", "Composer icon buttons"),
         ("size.control.button", "button-secondary", "height", "Text buttons"),
         ("size.control.select", "select", "height", "Select triggers in Settings"),
         ("size.control.menu-row", "menu-row", "height", "Menu rows"),
         ("size.control.settings-nav", "settings-nav", "height", "Settings navigation rows"),
         ("size.control.section-header", "section-header", "height", "Sidebar group headers"),
         ("size.control.list-row", "list-row-selected", "height", "Sidebar Bot rows"),
         ("size.control.pinned-tile", "pinned-tile", "height", "Pinned Bot tiles"),
         ("size.control.switch-width", "switch-on", "width", "Switch"),
         ("size.control.switch-height", "switch-on", "height", "Switch"),
         ("size.control.avatar", "avatar", "height", "Account avatar"),
         ("size.control.text-field", "text-field", "height", "Text field (New Bot name)"),
         ("layout.sidebar", "sidebar", "width", "Sidebar"),
         ("layout.composer", "composer", "width", "Composer"),
         ("layout.settings-dialog", "settings-dialog", "width", "Settings dialog"),
         ("layout.dialog", "dialog", "width", "New Bot dialog"),
         ("layout.confirm-dialog", "confirm-dialog", "width", "Delete confirmation"),
         ("layout.palette", "palette", "width", "Search palette"),
         ("layout.menu", "menu", "width", "Account and composer menus"),
         ("layout.context-menu", "context-menu", "width", "Context menu"),
         ("layout.inspector", "inspector", "width", "Inspector pane")]
for path, part, prop, use in SIZES:
    shot, v = dim_of(part, prop)
    if v:
        put(CORE, tuple(path.split(".")), tok(px("%gpx" % round(float(v[:-2]))), "dimension", "Measured",
            f"computed {prop} of {part} in {shot}, dark, {DATE} ({use}); {v} before rounding"))
WINDOW = C["dark"]["home-default"]["viewport"]
put(CORE, ("layout", "window-width"), tok("1120px", "dimension", "Measured",
    f"window 1120 x 760 pt; the page's viewport is {WINDOW['css'][0]} x {WINDOW['css'][1]} CSS px at devicePixelRatio {WINDOW['dpr']:.1f} (2 x the 1.1 zoom), {DATE}"))
put(CORE, ("layout", "window-height"), tok("760px", "dimension", "Measured", f"window height, pt, {DATE}"))

Z = [("backdrop", "backdrop"), ("menu", "menu"), ("dialog", "dialog"), ("tooltip", "tooltip")]
for key, part in Z:
    shot, s = style("dark", part)
    if s and s["z-index"] not in ("auto", ""):
        put(CORE, ("zIndex", key), tok(int(s["z-index"]), "number", "Measured", f"computed z-index of {part} in {shot}, {DATE}"))
# Two border widths compute: 0.4545px (one device pixel at the 2.2 ratio, declared 0.5px) and 0.9091px
# (two device pixels, declared 1px).
for key, part, declared in (("hairline", "composer", "0.5px"), ("default", "select", "1px")):
    shot, s = style("dark", part)
    users = sorted({p for (p, st), (sh, x) in P["dark"].items() if st == "default" and x["border-top-width"] == s["border-top-width"]})
    put(CORE, ("borderWidth", key), tok(declared, "dimension", "Measured",
        f"border-top-width of {', '.join(users)}; computed {s['border-top-width']} at devicePixelRatio 2.2, {DATE}"))
put(CORE, ("borderWidth", "focus"), tok("{focusRing.width}", "dimension", "Derived", "the focus ring is an outline of focusRing.width"))

cond = V["dark"]["conditions"]
rm = {k: v["rules"] for k, v in cond.items() if "reduced-motion" in k}
CORE.setdefault("duration", {})["$extensions"] = {"reducedMotion": {
    "rules": rm, "how": "--ui-reduced-motion follows the OS (no-preference here); style(--ui-reduced-motion: reduce) container queries "
    "drop animations and transitions, and (prefers-reduced-motion: reduce) rules do the same"}}
bp = sorted({k for k in cond if re.search(r"width", k)})
CORE.setdefault("layout", {})["$extensions"] = {"breakpointsInCss": bp,
    "note": "The window is resizable; these are every width condition the stylesheets use, media and container queries both"}

# ---------------------------------------------------------------- roles and components, per theme

ROLE = {
    "page": ("{bg.pane}", "the conversation pane"),
    "surface": ("{bg.sidebar}", "the sidebar"),
    "raised": ("{bg.elevated}", "composer, menus, dialogs, settings groups, message bubbles' cards"),
    "overlay": (None, "palette", "the search palette"),
    "scrim": ("{bg.scrim}", "dialog backdrop"),
    "text.primary": ("{text.primary}", ""), "text.secondary": ("{text.secondary}", ""),
    "text.tertiary": ("{text.tertiary}", ""), "text.disabled": ("{text.quaternary}", "the quaternary tier is the faintest text"),
    "text.on-accent": ("{text.on-primary}", "text on the accent and danger fills (the Update button, the switch, Delete); the ink primary button uses text.inverted"), "text.link": ("{text.accent-primary}", ""),
    "border.default": ("{border.secondary-translucent}", "composer, dialogs, fields"), "border.strong": ("{border.primary-translucent}", ""),
    "border.subtle": ("{border.tertiary-translucent}", "separators"), "border.focus": ("{border.focus-primary}", "drawn only after a Tab press"),
    "accent.default": ("{bg.accent-primary}", "the Accent setting's default blue; with Accent set to Bot color the open Bot's hue replaces it"),
    "accent.hover": ("{bg.accent-primary-hover}", ""),
    "accent.pressed": ("{bg.accent-primary-hover}", "Grok Bot has no pressed accent step; pressing scales the control to core.press.scale"),
    "accent.subtle": ("{bg.accent-secondary}", ""),
    "brand": ("{kit.seed.brand}", "the kit's orange; not used in Grok Bot's chrome"),
}
for s_, hue in (("success", "success"), ("warning", "warn"), ("danger", "danger")):
    ROLE[f"status.{s_}.fill"] = ("{bg.%s-primary}" % hue, "")
    ROLE[f"status.{s_}.subtle"] = ("{bg.%s-secondary}" % hue, "")
    ROLE[f"status.{s_}.text"] = ("{text.%s-primary}" % hue, "")
    ROLE[f"status.{s_}.border"] = ("{border.%s-primary}" % hue, "")
ROLE["status.info.fill"] = ("{bg.blue-primary}", "Grok Bot has no info status; the blue hue is used for it")
ROLE["status.info.subtle"] = ("{bg.blue-secondary}", "")
ROLE["status.info.text"] = ("{text.blue-primary}", "")
ROLE["status.info.border"] = ("{border.blue-primary}", "")

COMPONENTS = [
    ("button-primary", "button-primary", {"bg": "background-color", "text": "color", "radius": "border-top-left-radius", "height": "height", "padding": "padding-right"}),
    ("button-secondary", "button-secondary", {"bg": "background-color", "text": "color", "border": "border-top-color", "radius": "border-top-left-radius", "height": "height", "padding": "padding-right"}),
    ("button-danger", "button-danger", {"bg": "background-color", "text": "color", "radius": "border-top-left-radius", "height": "height"}),
    ("button-tonal", "button-tonal", {"bg": "background-color", "text": "color", "radius": "border-top-left-radius", "height": "height"}),
    ("icon-button", "icon-button", {"bg": "background-color", "text": "color", "radius": "border-top-left-radius", "size": "height"}),
    ("composer-button", "attach-button", {"text": "color", "radius": "border-top-left-radius", "size": "height"}),
    ("composer", "composer", {"bg": "background-color", "border": "border-top-color", "radius": "border-top-left-radius"}),
    ("menu", "menu", {"bg": "background-color", "border": "border-top-color", "radius": "border-top-left-radius"}),
    ("menu-row", "menu-row", {"text": "color", "radius": "border-top-left-radius", "height": "height", "padding": "padding-left"}),
    ("dialog", "dialog", {"bg": "background-color", "border": "border-top-color", "radius": "border-top-left-radius"}),
    ("confirm-dialog", "confirm-dialog", {"bg": "background-color", "radius": "border-top-left-radius"}),
    ("palette", "palette", {"bg": "background-color", "radius": "border-top-left-radius"}),
    ("scrim", "backdrop", {"bg": "background-color"}),
    ("text-field", "text-field", {"bg": "background-color", "border": "border-top-color", "text": "color", "radius": "border-top-left-radius", "height": "height"}),
    ("select", "select", {"bg": "background-color", "border": "border-top-color", "text": "color", "radius": "border-top-left-radius", "height": "height"}),
    ("switch-on", "switch-on", {"bg": "background-color", "radius": "border-top-left-radius"}),
    ("switch-off", "switch-off", {"bg": "background-color"}),
    ("tab", "tab", {"text": "color", "radius": "border-top-left-radius", "height": "height"}),
    ("tab-selected", "tab-selected", {"bg": "background-color", "text": "color"}),
    ("settings-nav", "settings-nav", {"text": "color", "radius": "border-top-left-radius", "height": "height"}),
    ("settings-nav-selected", "settings-nav-selected", {"bg": "background-color", "text": "color"}),
    ("pinned-tile", "pinned-tile", {"text": "color", "radius": "border-top-left-radius", "height": "height"}),
    ("list-row", "list-row-selected", {"bg": "background-color", "text": "color", "radius": "border-top-left-radius", "height": "height"}),
    ("section-header", "section-header", {"text": "color", "radius": "border-top-left-radius", "height": "height"}),
    ("agent-message", "agent-message", {"bg": "background-color", "radius": "border-top-left-radius"}),
    ("question-card", "question-card", {"bg": "background-color", "radius": "border-top-left-radius"}),
    ("chat-header", "chat-header", {"bg": "background-color", "text": "color", "radius": "border-top-left-radius", "height": "height"}),
    ("tooltip", "tooltip", {"bg": "background-color", "text": "color", "radius": "border-top-left-radius"}),
    ("avatar", "avatar", {"bg": "background-color", "text": "color"}),
    ("filter-pill", "filter-pill", {"bg": "background-color", "text": "color", "radius": "border-top-left-radius", "height": "height"}),
    ("filter-pill-selected", "filter-pill-selected", {"bg": "background-color", "text": "color"}),
]
STATES = [("hover", "bg-hover", "background-color"), ("hover", "text-hover", "color"), ("pressed", "bg-pressed", "background-color"),
          ("focus-visible", "outline-focus", "outline-color"), ("filled", "bg-filled", "background-color")]
CORE_NAMES = re.compile(r"^(text|bg|border|icon)\.(primary|secondary|tertiary|quaternary|on-primary|accent-primary(-hover)?|pane|chrome|sidebar|elevated|scrim|"
                        r"(primary|secondary|tertiary|quaternary)-translucent)$")
PREFER = ["role", "text", "bg", "border", "fill", "icon", "transcript", "prompt", "specular", "kit"]


def index(t):
    idx = {}

    def walk(node, path):
        for k, v in node.items():
            if k.startswith("$"):
                continue
            if isinstance(v, dict) and "$value" in v:
                if v["$type"] == "color" and path[:1] != ["component"]:
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
                f"background-color of {spec[1]} in {shot}, {THEME_NAME[t]} theme, {DATE}; {spec[2]}"))
            continue
        target = spec[0][1:-1]
        if get(tree, target) is None:
            raise KeyError(f"role.{key}: {target} missing in {t}")
        put(tree, ("role",) + tuple(key.split(".")), tok(spec[0], "color", "Derived", f"the checklist role, mapped to {target}" + (f"; {spec[1]}" if spec[1] else "")))
    idx = index(t)
    measured_n = aliased_n = 0

    def value_for(part, shot, prop, raw):
        nonlocal measured_n, aliased_n
        src = f"computed {prop} of {part} in {shot}, {THEME_NAME[t]} theme, {DATE}"
        if prop in ("background-color", "color", "border-top-color", "outline-color"):
            v = color(raw)
            measured_n += 1
            if v in idx:
                aliased_n += 1
                pre = {"background-color": "bg.", "color": "text.", "border-top-color": "border.", "outline-color": "border."}[prop]
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
            if prop == "border-top-color" and s.get("border-top-width") in ("0px", ""):
                continue
            put(tree, ("component", name, key), value_for(part, shot, prop, raw))
        for state, key, prop in STATES:
            sh, ss = style(t, part, state)
            if ss and ss[prop] != s[prop] and color(ss[prop]) != "rgba(0, 0, 0, 0)" and not (prop == "outline-color" and ss.get("outline-style") == "none"):
                put(tree, ("component", name, key), value_for(part, sh, prop, ss[prop]))
    tree["$extensions"] = {"componentValues": {"measured": measured_n, "aliased": aliased_n}}


for t in THEMES:
    build_roles_and_components(t)


def shadow_uses(t):
    """Name, on each shadow token, the captured parts whose computed box-shadow is exactly it."""
    for key, tokn in SETS[t].get("shadow", {}).items():
        if not isinstance(tokn, dict) or tokn.get("$type") != "shadow":
            continue
        uses = sorted({part for (part, state), (shot, s) in P[t].items() if state == "default" and s["box-shadow"] != "none"
                       and [l for l in shadow(s["box-shadow"]) if not l["color"].endswith(", 0)")] == tokn["$value"]})
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
    """A name present in only one theme (a part measured in one theme only, a shadow that is empty in
    one) is not a theme token: move it out, with its value, to $extensions.notTokenised."""
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
                {"name": n, "value": v["$value"], "why": f"present only in the {t} reading; not in the other theme"})


reconcile()
check()
tokens = {
    "core": CORE, "light": SETS["light"], "dark": SETS["dark"],
    "$themes": [
        {"id": "light", "name": "Light", "selectedTokenSets": {"core": "source", "light": "enabled"},
         "$description": "Settings > General > Theme: Light (html[data-theme=cursor-light])"},
        {"id": "dark", "name": "Dark", "selectedTokenSets": {"core": "source", "dark": "enabled"},
         "$description": "Settings > General > Theme: Dark, or Follow System with macOS dark (html[data-theme=cursor-dark])"},
    ],
    "$metadata": {"tokenSetOrder": ["core", "light", "dark"]},
}
(PKG / "tokens.json").write_text(json.dumps(tokens, indent=2, ensure_ascii=False) + "\n")


def count(d):
    return sum(1 for _ in tokens_of(d))


print({k: count(tokens[k]) for k in ("core", "light", "dark")}, "component values aliased:",
      {t: SETS[t]["$extensions"]["componentValues"] for t in THEMES})
