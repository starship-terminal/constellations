#!/usr/bin/env python3
"""Build tokens.json (W3C DTCG, Tokens Studio multi-set layout) from the raw readings.

    python3 tools/build_tokens.py

Sources, read live from OpenCode 2.1.4 for macOS on 2026-10-25 over the remote-debugging port
(tools/capture/electron/):
  raw/css-vars.<theme>.json      every custom property the window's stylesheets declare (Tailwind's own
                                 --tw-* left out), by sheet, selector and condition, and each name as it
                                 computes and paints on :root
  raw/components.<theme>.json    computed styles of the captured parts, per shot and state (shots.mjs)

How OpenCode's colours work, and so how this file is laid out. The theme engine writes one style
element, `oc-theme`, on :root from the chosen theme (OpenCode, the default) and the colour scheme. It
holds two layers. The newer one, v2, is a set of ramps (grey in 13 steps, eight hues in 12 steps; the
same in both schemes) under semantic names that point at them with var(): --v2-background-bg-*,
--v2-text-text-*, --v2-border-border-*, --v2-icon-icon-*, --v2-overlay-*, --v2-state-*, --v2-agent-*,
--v2-avatar-*, --v2-elevation-* (shadows). Translucent white and black steps (--v2-alpha-light-*,
--v2-alpha-dark-*) come from the main stylesheet. The older layer (--background-*, --surface-*,
--text-*, --border-*, --icon-*, --syntax-*, --markdown-*, ...) is written as literals beside it; the
newer components use v2 classes, the code and markdown colours still come from the older names.
So the core set holds the ramps and alpha steps (theme-independent), the semantic sets hold the v2
roles at the top level (bg, text, border, icon, overlay, state, agent, avatar, illustration), syntax
and markdown, the older layer under legacy.*, shadows, the checklist roles (role.*) and measured
component values (component.*).

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

THEME_SHEET = "oc-theme"
THEME_NAME = {"light": "Light", "dark": "Dark"}
SCOPE = ":root"
RAMPS = ["grey", "red", "orange", "yellow", "green", "cyan", "blue", "purple", "pink"]
# v2 semantic groups: --v2-<group>-... -> (path, ...) by these rules
V2_GROUPS = {
    "background": lambda r: ("bg", r.removeprefix("bg-")),
    "text": lambda r: ("text", r.removeprefix("text-")),
    "border": lambda r: ("border", r.removeprefix("border-")),
    "icon": lambda r: ("icon", r.removeprefix("icon-")),
    "overlay": lambda r: ("overlay", re.sub(r"^(simple|gradient-depth)-(overlay-)?", "", r)),
    "state": lambda r: ("state",) + tuple(reversed(r.split("-", 1))),        # bg-success -> state.success.bg
    "agent": lambda r: ("agent",) + tuple(r.split("-", 1)),                  # plan-solid -> agent.plan.solid
    "avatar": lambda r: ("avatar", r),
    "illustration": lambda r: ("illustration", r.removeprefix("illustration-")),
}
# older layer: --<group>-... kept under legacy.<group>, except syntax and markdown, which stay top level
LEGACY = ["background", "surface", "text", "border", "icon", "input", "button", "avatar", "base", "base2", "base3"]
TOP_LEGACY = ["syntax", "markdown"]
SHADOW_NAMES = re.compile(r"^--(v2-elevation-[\w-]+|shadow-(xxs-border|xs|md|lg|xs-border[\w-]*|lg-border-base))$")


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
    """The declaration that wins on :root: the last unconditioned one whose selector is :root (the
    oc-theme element comes last). Falls back to the last :root declaration under the stylesheet's
    @layer theme. Returns (value, sheet) or (None, None)."""
    hit, layered = (None, None), (None, None)
    for d in V[t]["decls"]:
        if d["name"] != name or d["selector"] not in (":root", ":root, :host"):
            continue
        if d["condition"] == "":
            hit = (d["value"], d["sheet"])
        elif d["condition"] == "@layer theme":
            layered = (d["value"], d["sheet"])
    return hit if hit[0] is not None else layered


LITERAL = re.compile(r"^(#[0-9a-fA-F]{3,8}|oklch\([^)]*\)|rgba?\([^)]*\)|color\([^)]*\)|transparent)$")


def where(t, name, extra=""):
    return f"{name} on :root, {THEME_NAME[t]} theme, {DATE}{extra}"


def path_of(name):
    """The token path for a colour custom property, or None when it is not kept."""
    m = re.fullmatch(r"--v2-(%s)-(\d+)" % "|".join(RAMPS), name)
    if m:
        return ("color", m.group(1), m.group(2))                             # core
    m = re.fullmatch(r"--v2-alpha-(light|dark)-(\d+)", name)
    if m:
        return ("color", "alpha", m.group(1), m.group(2))                     # core
    m = re.fullmatch(r"--v2-([a-z]+)-([\w-]+)", name)
    if m:
        return V2_GROUPS[m.group(1)](m.group(2)) if m.group(1) in V2_GROUPS else None
    head, _, tail = name[2:].partition("-")
    if head in TOP_LEGACY:
        return (head, tail)
    if head in LEGACY:
        return ("legacy", head, tail) if tail else ("legacy", "seed", head)
    return None


def is_core(path):
    return path[0] == "color"


# ---------------------------------------------------------------- core

CORE = {}
dark_comp, light_comp = computed("dark"), computed("light")
PATHS = {}


def core_colours():
    """The ramps and alpha steps: identical in both schemes, so core."""
    for n in sorted(dark_comp):
        p = path_of(n)
        if not p or not is_core(p) or n not in V["dark"]["colors"]:
            continue
        a, b = V["dark"]["colors"][n], V["light"]["colors"][n]
        if color(a) != color(b):
            raise ValueError(f"{n} differs by scheme: {a} / {b}")
        decl, sheet = effective("dark", n)
        PATHS[n] = p
        put(CORE, p, tok(color(a), "color", "Measured", f"{n} = {decl} on :root ({sheet}), both schemes, {DATE}"))


core_colours()

# ---------------------------------------------------------------- semantic sets


def semantic(t):
    tree, comp, painted = {}, computed(t), V[t]["colors"]
    names = sorted(n for n in comp if n not in PATHS and path_of(n) and n in painted and is_color(painted[n]) and not SHADOW_NAMES.match(n))
    paths = dict(PATHS)
    for n in names:
        paths[n] = path_of(n)
    for n in names:
        p = paths[n]
        value = color(painted[n])
        decl, sheet = effective(t, n)
        decl = (decl or "").strip()
        if LITERAL.match(decl):
            put(tree, p, tok(value, "color", "Measured", f"{n} = {decl} on :root ({sheet}), {THEME_NAME[t]} theme, {DATE}"))
            continue
        m = re.fullmatch(r"var\((--[\w-]+)\)", decl)
        if m and m.group(1) in paths and is_color(painted.get(m.group(1), "none")) and color(painted[m.group(1)]) == value:
            put(tree, p, tok("{%s}" % ".".join(paths[m.group(1)]), "color", "Measured", where(t, n, f" ({sheet})"), formula=decl))
        else:
            put(tree, p, tok(value, "color", "Measured", where(t, n), formula=decl or comp[n]))
    # Shadows: the older layer's --shadow-* as painted (a probe's box-shadow); the v2 elevations have no
    # "shadow" in their names, so vars.mjs did not paint them, and their computed value (var()s already
    # substituted, colours as hex) is read instead.
    for n in sorted(comp):
        if not SHADOW_NAMES.match(n):
            continue
        key = n.replace("--v2-elevation-", "").replace("--shadow-", "legacy-")
        painted_as = V[t]["shadows"].get(n)
        layers = [l for l in shadow(painted_as or comp[n]) if not l["color"].endswith(", 0)")]
        decl, _ = effective(t, n)
        how = "box-shadow as painted" if painted_as else "computed value"
        put(tree, ("shadow", key), tok(layers, "shadow", "Measured", where(t, n, f"; {how}, fully transparent layers dropped"),
            formula=decl or comp.get(n)))
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
BASE_STATES = ["default", "selected", "hover", "empty"]


def style(t, part, state="default"):
    """A part's reading in a state. For "default", a part never read at rest (a tooltip that only
    exists under the pointer) falls back to its base state."""
    hit = P[t].get((part, state))
    if not hit and state == "default":
        hit = next((P[t][(part, s)] for s in BASE_STATES if (part, s) in P[t]), None)
    return hit if hit else (None, None)


# ---------------------------------------------------------------- core scales

def rem_px(v):
    return px("%gpx" % (float(v.replace("rem", "")) * 16))


for pre, group in (("--radius-", "radius"), ("--breakpoint-", "breakpoint"), ("--container-", "container")):
    for n in sorted(dark_comp):
        if not n.startswith(pre):
            continue
        v = dark_comp[n]
        if light_comp.get(n) != v:
            raise ValueError(f"{n} differs by theme")
        key = n[len(pre):]
        if v.endswith("rem"):
            put(CORE, (group, key), tok(rem_px(v), "dimension", "Derived", f"{n} = {v} on :root, both themes, {DATE}; 1rem = 16px", rem=v))
        elif v.endswith("px"):
            put(CORE, (group, key), tok(px(v), "dimension", "Measured", f"{n} on :root, both themes, {DATE}"))
# OpenCode's controls are drawn with Tailwind's arbitrary radii more than with the scale; the ones the
# captured parts compute are kept as steps of their own, with the parts that use them.
used_r = {}
for (part, state), (shot, s) in sorted(P["dark"].items()):
    r = s["border-top-left-radius"]
    if state == "default" and re.fullmatch(r"\d+px", r) and r != "0px" and int(r[:-2]) < 100:
        used_r.setdefault(r, set()).add(part)
for r, users in sorted(used_r.items(), key=lambda x: int(x[0][:-2])):
    put(CORE, ("radius", "measured-" + r[:-2]), tok(px(r), "dimension", "Measured",
        f"computed border-radius of {', '.join(sorted(users)[:8])}{' and others' if len(users) > 8 else ''}, dark, {DATE}"))

SPACING = dark_comp["--spacing"]
base = float(SPACING.replace("rem", "")) * 16
put(CORE, ("spacing", "base"), tok(px("%gpx" % base), "dimension", "Measured", f"--spacing = {SPACING} on :root (Tailwind's spacing unit), {DATE}"))
for n in (0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 5, 6, 7, 8, 10, 12, 16, 20):
    put(CORE, ("spacing", ("%g" % n).replace(".", "-")), tok(px("%gpx" % (base * n)), "dimension", "Derived",
        f"Tailwind's spacing scale, calc(var(--spacing) * {n:g}), with --spacing = {SPACING}"))

for key, n in (("sans", "--font-family-sans"), ("mono", "--font-family-mono")):
    stack = [f.strip().strip("'\"") for f in dark_comp[n].split(",")]
    put(CORE, ("fontFamily", key), tok(stack, "fontFamily", "Measured", f"{n} on :root (set inline on <html> by the app from Settings > Appearance), {DATE}"))
for key, n in (("small", "--font-size-small"), ("base", "--font-size-base"), ("large", "--font-size-large"), ("x-large", "--font-size-x-large")):
    put(CORE, ("fontSize", key), tok(px(dark_comp[n]), "dimension", "Measured", f"{n} on :root, {DATE}"))
for key, n in (("regular", "--font-weight-regular"), ("medium", "--font-weight-medium"), ("bold", "--font-weight-bold")):
    put(CORE, ("fontWeight", key), tok(int(dark_comp[n]), "fontWeight", "Measured", f"{n} on :root, {DATE}"))
put(CORE, ("fontWeight", "ui"), tok(440, "fontWeight", "Measured",
    f"the body's font-[440] class and the computed font-weight of most measured parts, {DATE}", note="OpenCode's interface text is 440, not 400"))
put(CORE, ("fontWeight", "label"), tok(530, "fontWeight", "Measured", f"computed font-weight of buttons, menu group labels, the session title and tooltips, {DATE}"))
put(CORE, ("fontWeight", "heading"), tok(640, "fontWeight", "Measured", f"computed font-weight of Settings section titles, {DATE}"))
for key, n in (("tight", "--line-height-tight"), ("compact", "--line-height-compact"), ("base", "--line-height-base")):
    put(CORE, ("lineHeight", key), tok(px(dark_comp[n]), "dimension", "Measured", f"{n} on :root, {DATE}"))
for key, n in (("normal", "--line-height-normal"), ("large", "--line-height-large"), ("x-large", "--line-height-x-large"), ("2x-large", "--line-height-2x-large")):
    put(CORE, ("lineHeight", key), tok(round(float(dark_comp[n][:-1]) / 100, 3), "number", "Measured", f"{n} = {dark_comp[n]} on :root, {DATE}"))
for key, n in (("normal", "--letter-spacing-normal"), ("tight", "--letter-spacing-tight"), ("tightest", "--letter-spacing-tightest")):
    put(CORE, ("letterSpacing", key), tok(px("%gpx" % float(dark_comp[n])), "dimension", "Derived",
        f"{n} = {dark_comp[n]} on :root, {DATE}; declared without a unit, read here as px", declared=dark_comp[n]))

# Type roles, measured on real elements (computed style; both themes agree). Only parts whose own
# computed style is their text.
ROLES = [("body", "markdown", "Agent replies in the conversation"),
         ("message", "user-message", "The owner's prompt in the conversation"),
         ("prompt", "prompt-field", "Text typed in the composer"),
         ("ui", "project-row", "Rows, menus and most interface text"),
         ("label", "button-neutral", "Button labels"),
         ("title", "session-title", "The session title in the header"),
         ("heading", "section-title", "Settings section titles"),
         ("caption", "tooltip", "Tooltips and menu group labels (11px, 530)"),
         ("tool", "tool-group", "Tool-call summaries (Used 1 Shell)"),
         ("code", "inline-code", "Inline code in replies")]
for role, part, use in ROLES:
    shot, s = style("dark", part)
    if not s:
        continue
    fam = "{fontFamily.mono}" if role == "code" else "{fontFamily.sans}"
    lh = s["line-height"]
    val = {"fontFamily": fam, "fontSize": px(s["font-size"]), "fontWeight": int(float(s["font-weight"])),
           "lineHeight": px("%gpx" % round(float(lh[:-2]), 1)) if lh.endswith("px") else px("%gpx" % round(float(s["font-size"][:-2]) * 1.2, 1)),
           "letterSpacing": px(s["letter-spacing"]) if s["letter-spacing"].endswith("px") else "0px"}
    put(CORE, ("typography", role), tok(val, "typography", "Measured", f"computed style of {part} in {shot}, dark, {DATE}; {use}",
        note=None if lh.endswith("px") else "computed line-height is normal; 1.2 x the size is used here"))


def dim_of(part, prop, state="default", t="dark"):
    shot, s = style(t, part, state)
    return (shot, s[prop]) if s and s.get(prop, "").endswith("px") else (None, None)


SIZES = [("size.control.icon-button", "icon-button", "height", "Icon buttons (Add project, Toggle review)"),
         ("size.control.icon-button-small", "copy-button", "height", "Message actions (Copy, Revert)"),
         ("size.control.tab-close", "tab-close", "height", "A tab's close button"),
         ("size.control.button", "button-neutral", "height", "Text buttons"),
         ("size.control.select", "select", "height", "Select triggers in Settings"),
         ("size.control.menu-row", "menu-row", "height", "Menu rows"),
         ("size.control.palette-row", "palette-row", "height", "Command palette rows"),
         ("size.control.settings-nav", "settings-nav", "height", "Settings navigation rows"),
         ("size.control.project-row", "project-row", "height", "Home's project rows"),
         ("size.control.session-row", "session-row", "height", "Home's session rows"),
         ("size.control.session-tab", "session-tab", "height", "Session tabs in the title bar"),
         ("size.control.search-field", "search-field", "height", "Home's session search"),
         ("size.control.palette-input", "palette-input", "height", "The palette's search field"),
         ("size.control.switch-width", "switch", "width", "Switch"),
         ("size.control.switch-height", "switch", "height", "Switch"),
         ("size.control.avatar", "project-avatar", "height", "Project avatar"),
         ("size.control.tag", "tag-free", "height", "Tags (Free)"),
         ("size.control.composer", "composer", "height", "The composer, empty"),
         ("layout.tab", "session-tab", "width", "A session tab"),
         ("layout.project-list", "project-row", "width", "Home's project column"),
         ("layout.session-list", "session-row", "width", "Home's session column"),
         ("layout.composer", "composer", "width", "Composer in a session"),
         ("layout.transcript", "text-part", "width", "Conversation column"),
         ("layout.settings-nav", "settings-nav", "width", "Settings navigation"),
         ("layout.settings-list", "settings-list", "width", "Settings group"),
         ("layout.confirm-dialog", "confirm-dialog", "width", "Delete confirmation"),
         ("layout.palette", "palette", "width", "Command palette"),
         ("layout.menu", "model-menu", "width", "Model menu"),
         ("layout.review-pane", "pane", "width", "Review and context pane")]
for path, part, prop, use in SIZES:
    shot, v = dim_of(part, prop)
    if v:
        put(CORE, tuple(path.split(".")), tok(px("%gpx" % round(float(v[:-2]))), "dimension", "Measured",
            f"computed {prop} of {part} in {shot}, dark, {DATE} ({use}); {v} before rounding"))
WINDOW = C["dark"]["home-default"]["viewport"]
put(CORE, ("layout", "window-width"), tok("%dpx" % WINDOW["css"][0], "dimension", "Measured",
    f"window {WINDOW['css'][0]} x {WINDOW['css'][1]} pt at devicePixelRatio {WINDOW['dpr']:g}, no zoom, {DATE}"))
put(CORE, ("layout", "window-height"), tok("%dpx" % WINDOW["css"][1], "dimension", "Measured", f"window height, pt, {DATE}"))

Z = [("tab-close", "tab-close"), ("search", "search-field"), ("dialog", "dialog-overlay"), ("menu", "model-menu"), ("tooltip", "tooltip")]
for key, part in Z:
    shot, s = style("dark", part)
    if s and s["z-index"] not in ("auto", ""):
        put(CORE, ("zIndex", key), tok(int(s["z-index"]), "number", "Measured", f"computed z-index of {part} in {shot}, {DATE}"))

# Border widths: OpenCode draws most edges as a 0.5px box-shadow ring (inset 0 0 0 0.5px), and its
# tags as a 0.5px border.
put(CORE, ("borderWidth", "hairline"), tok("0.5px", "dimension", "Measured",
    f"border-top-width of tag-free and the 0.5px spread of the inset ring on settings-list and focused rows, {DATE}"))
# Focus: an outline, read on buttons in their focus-visible shots.
shot, s = style("dark", "button-neutral", "focus-visible")
put(CORE, ("focusRing", "width"), tok(px(s["outline-width"]), "dimension", "Measured", f"outline-width of button-neutral in {shot}, {DATE}"))
put(CORE, ("focusRing", "offset"), tok(px(s["outline-offset"]), "dimension", "Measured", f"outline-offset of button-neutral in {shot}, {DATE}"))
put(CORE, ("borderWidth", "focus"), tok("{focusRing.width}", "dimension", "Derived", "the focus ring is an outline of focusRing.width"))

# Motion: no duration or easing tokens are declared; these are the transitions the measured parts compute.
durs, eases = {}, {}
for (part, state), (shot, s) in sorted(P["dark"].items()):
    if state != "default":
        continue
    for d in {x.strip() for x in s["transition-duration"].split(",")} - {"0s"}:
        durs.setdefault(d, set()).add(part)
    if s["transition-duration"] != "0s":
        for e in {x.strip() for x in s["transition-timing-function"].split(",")}:
            eases.setdefault(e, set()).add(part)
for d, users in sorted(durs.items(), key=lambda x: ms(x[0])):
    put(CORE, ("duration", ms(d).replace("ms", "")), tok(ms(d), "duration", "Measured",
        f"computed transition-duration of {', '.join(sorted(users))}, dark, {DATE}"))
EASE = {"ease": [0.25, 0.1, 0.25, 1], "ease-in-out": [0.42, 0, 0.58, 1], "ease-out": [0, 0, 0.58, 1], "ease-in": [0.42, 0, 1, 1], "linear": [0, 0, 1, 1]}
for e, users in sorted(eases.items()):
    if e in EASE:
        put(CORE, ("easing", e), tok(EASE[e], "cubicBezier", "Measured", f"computed transition-timing-function of {', '.join(sorted(users))}, dark, {DATE} ({e})"))
cond = V["dark"]["conditions"]
rm = {k: v["rules"] for k, v in cond.items() if "reduced-motion" in k}
CORE.setdefault("duration", {})["$extensions"] = {"reducedMotion": {
    "rules": rm, "how": "(prefers-reduced-motion: reduce) rules and motion-reduce: utilities drop the animations"}}
bp = sorted({k for k in cond if re.search(r"width", k)})
CORE.setdefault("layout", {})["$extensions"] = {"breakpointsInCss": bp,
    "note": "The window is resizable; these are every width condition the stylesheets use, media and container queries both"}

# ---------------------------------------------------------------- roles and components, per theme

ROLE = {
    "page": ("{bg.base}", "the main panel: Home, the session, Settings"),
    "surface": ("{bg.deep}", "the window behind the panel: the title bar and its tabs"),
    "raised": ("{bg.layer-01}", "settings groups, the composer (dark), tags' panes"),
    "overlay": ("{bg.layer-01}", "menus, tooltips and the command palette"),
    "scrim": ("{overlay.scrim}", "dialog backdrop"),
    "text.primary": ("{text.base}", ""), "text.secondary": ("{text.muted}", ""),
    "text.tertiary": ("{text.faint}", ""), "text.disabled": ("{text.faint}", "OpenCode has no disabled text tier; the faint tier is the lightest"),
    "text.on-accent": ("{text.contrast}", "text on the accent and contrast fills"), "text.link": ("{text.accent}", ""),
    "border.default": ("{border.base}", ""), "border.strong": ("{border.strong}", ""),
    "border.subtle": ("{border.muted}", "the 0.5px rings on settings groups and rows"), "border.focus": ("{border.focus}", "the focus outline"),
    "accent.default": ("{bg.accent}", "blue-600; links, focus and the owner's prompt use the blue ramp, while the primary action (Send) is the contrast fill"),
    "accent.hover": ("{text.accent-hover}", "OpenCode has no accent fill hover; the accent text's hover step is used"),
    "accent.pressed": ("{text.accent-hover}", "OpenCode has no pressed accent step"),
    "accent.subtle": ("{state.info.bg}", "the faint blue behind the owner's prompt and info states"),
    "contrast": ("{bg.icon-button-contrast}", "the Send button: the primary action is an ink fill, not the accent"),
    "brand": ("{legacy.surface.brand-base}", "the older layer's brand orange; not used in the v2 chrome"),
}
for s_ in ("success", "warning", "danger", "info"):
    ROLE[f"status.{s_}.fill"] = ("{state.%s.fg}" % s_, "OpenCode's state colours are fg, bg and border; the solid is fg")
    ROLE[f"status.{s_}.subtle"] = ("{state.%s.bg}" % s_, "")
    ROLE[f"status.{s_}.text"] = ("{state.%s.fg}" % s_, "")
    ROLE[f"status.{s_}.border"] = ("{state.%s.border}" % s_, "")

COMPONENTS = [
    ("button-neutral", "button-neutral", {"bg": "background-color", "text": "color", "radius": "border-top-left-radius", "height": "height", "padding": "padding-left"}),
    ("button-secondary", "button-secondary", {"bg": "background-color", "text": "color", "radius": "border-top-left-radius", "height": "height", "padding": "padding-left"}),
    ("button-danger", "button-danger", {"bg": "background-color", "text": "color", "radius": "border-top-left-radius", "height": "height", "padding": "padding-left"}),
    ("send-button", "send-button", {"bg": "background-color", "text": "color", "radius": "border-top-left-radius", "size": "height"}),
    ("icon-button", "icon-button", {"bg": "background-color", "text": "color", "radius": "border-top-left-radius", "size": "height"}),
    ("icon-button-selected", "icon-button-home", {"bg": "background-color", "text": "color"}),
    ("model-button", "model-button", {"text": "color", "radius": "border-top-left-radius", "height": "height"}),
    ("composer", "composer", {"bg": "background-color", "radius": "border-top-left-radius", "width": "width"}),
    ("menu", "model-menu", {"bg": "background-color", "radius": "border-top-left-radius", "width": "width"}),
    ("menu-row", "menu-row", {"text": "color", "radius": "border-top-left-radius", "height": "height", "padding": "padding-left"}),
    ("menu-group-label", "menu-group-label", {"text": "color"}),
    ("tooltip", "tooltip", {"bg": "background-color", "text": "color", "radius": "border-top-left-radius", "height": "height"}),
    ("tag", "tag-free", {"bg": "background-color", "text": "color", "border": "border-top-color", "radius": "border-top-left-radius", "height": "height"}),
    ("scrim", "dialog-overlay", {"bg": "background-color"}),
    ("confirm-dialog", "confirm-dialog", {"bg": "background-color", "radius": "border-top-left-radius", "width": "width"}),
    ("palette", "palette", {"bg": "background-color", "radius": "border-top-left-radius", "width": "width"}),
    ("palette-row", "palette-row", {"text": "color", "radius": "border-top-left-radius", "height": "height"}),
    ("palette-row-active", "palette-row-active", {"bg": "background-color", "text": "color"}),
    ("project-row", "project-row", {"text": "color", "radius": "border-top-left-radius", "height": "height", "padding": "padding-left"}),
    ("project-row-selected", "project-row-selected", {"bg": "background-color", "text": "color"}),
    ("session-row", "session-row", {"text": "color", "radius": "border-top-left-radius", "height": "height"}),
    ("session-tab", "session-tab", {"bg": "background-color", "height": "height", "width": "width"}),
    ("session-tab-selected", "session-tab-selected", {"bg": "background-color"}),
    ("search-field", "search-field", {"bg": "background-color", "radius": "border-top-left-radius", "height": "height"}),
    ("settings-search", "settings-search", {"bg": "background-color", "radius": "border-top-left-radius", "height": "height"}),
    ("settings-nav", "settings-nav", {"text": "color", "radius": "border-top-left-radius", "height": "height"}),
    ("settings-nav-selected", "settings-nav-selected", {"bg": "background-color", "text": "color"}),
    ("settings-list", "settings-list", {"bg": "background-color", "radius": "border-top-left-radius", "padding": "padding-left"}),
    ("select", "select", {"bg": "background-color", "radius": "border-top-left-radius", "height": "height"}),
    ("switch", "switch", {"bg": "background-color", "height": "height", "width": "width"}),
    ("user-message", "user-message", {"bg": "background-color", "text": "color"}),
    ("markdown", "markdown", {"text": "color"}),
    ("inline-code", "inline-code", {"bg": "background-color", "text": "color", "radius": "border-top-left-radius"}),
    ("code-block", "code-block", {"bg": "background-color", "text": "color", "radius": "border-top-left-radius"}),
    ("tool-group", "tool-group", {"text": "color"}),
]
STATES = [("hover", "bg-hover", "background-color"), ("hover", "text-hover", "color"), ("pressed", "bg-pressed", "background-color"),
          ("focus-visible", "outline-focus", "outline-color"), ("focus-visible", "bg-focus", "background-color"), ("filled", "bg-filled", "background-color")]
CORE_NAMES = re.compile(r"^(text|bg|border|icon)\.(base|muted|faint|inverse|contrast|accent|deep|layer-0\d|strong|focus)$")
PREFER = ["text", "bg", "border", "icon", "overlay", "state", "color", "legacy", "syntax", "markdown", "agent", "avatar", "role"]


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
        target = spec[0][1:-1]
        if get(tree, target) is None and get(CORE, target) is None:
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
                pre = {"background-color": ("bg.", "overlay."), "color": ("text.",), "border-top-color": ("border.",), "outline-color": ("border.",)}[prop]
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
            if prop == "border-top-left-radius" and raw == "0px":
                continue
            put(tree, ("component", name, key), value_for(part, shot, prop, raw))
        for state, key, prop in STATES:
            sh, ss = style(t, part, state)
            if ss and ss[prop] != s[prop] and color(ss[prop]) != "rgba(0, 0, 0, 0)" and not (prop == "outline-color" and ss.get("outline-style") == "none"):
                put(tree, ("component", name, key), value_for(part, sh, prop, ss[prop]))
    tree["$extensions"] = {"componentValues": {"measured": measured_n, "aliased": aliased_n}}


for t in THEMES:
    build_roles_and_components(t)


def _norm(layers):
    """Shadow layers compared at two decimals of alpha: a token's #0000004d reads 0.302 and the same
    colour painted on an element reads 0.3."""
    def c(v):
        m = re.fullmatch(r"rgba\((\d+), (\d+), (\d+), ([\d.]+)\)", v)
        return (m.group(1), m.group(2), m.group(3), round(float(m.group(4)), 2)) if m else v
    return [dict(l, color=c(l["color"])) for l in layers if not l["color"].endswith(", 0)")]


def shadow_uses(t):
    """Name, on each shadow token, the captured parts whose computed box-shadow is exactly it."""
    for key, tokn in SETS[t].get("shadow", {}).items():
        if not isinstance(tokn, dict) or tokn.get("$type") != "shadow":
            continue
        uses = sorted({part for (part, state), (shot, s) in P[t].items() if state == "default" and s["box-shadow"] != "none"
                       and _norm(shadow(s["box-shadow"])) == _norm(tokn["$value"])})
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
         "$description": "Settings > Appearance > Color scheme: System with prefers-color-scheme light, or Light; Theme: OpenCode (html[data-color-scheme=light])"},
        {"id": "dark", "name": "Dark", "selectedTokenSets": {"core": "source", "dark": "enabled"},
         "$description": "Settings > Appearance > Color scheme: System with prefers-color-scheme dark, or Dark; Theme: OpenCode (html[data-color-scheme=dark])"},
    ],
    "$metadata": {"tokenSetOrder": ["core", "light", "dark"]},
}
(PKG / "tokens.json").write_text(json.dumps(tokens, indent=2, ensure_ascii=False) + "\n")


def count(d):
    return sum(1 for _ in tokens_of(d))


print({k: count(tokens[k]) for k in ("core", "light", "dark")}, "component values aliased:",
      {t: SETS[t]["$extensions"]["componentValues"] for t in THEMES})
