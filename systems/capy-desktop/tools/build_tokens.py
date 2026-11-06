#!/usr/bin/env python3
"""Build tokens.json (W3C DTCG, Tokens Studio multi-set layout) from the raw readings.

    python3 tools/build_tokens.py

Sources, read live from Capy 0.4.7 for macOS on 2026-10-25 over the remote-debugging port
(tools/capture/electron/):
  raw/css-vars.<theme>.json      every custom property the window's stylesheets declare (Tailwind's
                                 --tw-* utility plumbing left out), by sheet, selector and condition,
                                 and each name as it computes and paints on <body>
  raw/components.<theme>.json    computed styles of the captured parts, per shot and state (shots.mjs)
  raw/run.dark.json              the agent run's kept frames (run.mjs, on Capy 0.5.0): the inspector's width

How Capy's colours work, and so how this file is laid out. Capy is built with Tailwind CSS 4 on Base UI.
Its theme is about forty oklch seeds on `:root, [data-theme-preview]` (light) and `.dark` in the app
stylesheet (styles-<hash>.css): the window (bg, chrome), the content panel, card, popover, input and
button fills, the ink (fg, text), the teal primary, destructive, warning, success, info and a few hues,
diff and chart colours. Everything else is a color-mix() of those, declared under
@supports (color: color-mix(in lab, red, red)) with a plain var() fallback: the muted text tiers are
the text mixed into the window colour at 62, 48 and 36% in light (68, 52, 38% in dark), the soft fills
are a seed at 18 to 30% over transparent, the link and the ring are the primary darkened with black.
Tailwind's `--color-*` names are all var() aliases of these seeds (no Tailwind palette is loaded beyond
black and white), so they are left out. Each semantic set holds the seeds as values and the mixes as
the painted value with the formula beside it. role.* maps the checklist roles onto those tokens, and
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

SHEET = "styles-"                       # the app stylesheet (styles-<hash>.css)
THEME_SELECTOR = {"light": ":root", "dark": ".dark"}
THEME_NAME = {"light": "Light (html.light, System theme with prefers-color-scheme: light)",
              "dark": "Dark (html.dark, System theme with prefers-color-scheme: dark)"}
# name prefix -> token group; names without one go to `base`.
GROUPS = [("--chart-", "chart"), ("--diff-", "diff"), ("--", "base")]
SKIP = re.compile(r"^--(tw-|lightningcss|_|color-|trees|diffs|ansi|shader-(?!ink)|gradient|toast|normal|success-|error|info-|warning-(?!fg|subtle)|"
                  r"gray|lift|mask|clamp|scroll|memory|capy|y-|default|font|text-(?!link)|leading|tracking|radius|spacing|container|blur|ease|animate|"
                  r"duration|shadow|sh-|z-|h-|icon-(?!muted)|responsive|safe|shell|right-panel|shimmer|aspect|table|tab-surface|border-width|focus|button-(?!hover))")
KEEP_ALSO = set()


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
    """A Tailwind length (rem, px, or calc(<rem> * n)) -> px string."""
    v = v.strip()
    m = re.fullmatch(r"calc\(\s*([\d.]+)rem\s*\*\s*([\d.]+)\s*\)", v)
    if m:
        return px("%gpx" % (float(m.group(1)) * 16 * float(m.group(2))))
    m = re.fullmatch(r"(-?[\d.]+)rem", v)
    if m:
        return px("%gpx" % (float(m.group(1)) * 16))
    m = re.fullmatch(r"(-?[\d.]+)em", v)
    if m:
        return v
    return px(v)


def decls(t, name):
    """The declarations of `name` in the app stylesheet that apply in theme t, unconditional ones first."""
    out = [d for d in V[t]["decls"] if d["name"] == name and d["sheet"].startswith(SHEET)]
    sel = THEME_SELECTOR[t]
    own = [d for d in out if any(s.strip() == sel or s.strip().startswith(sel + "[") for s in d["selector"].split(","))
           or d["selector"].startswith(":root, :host")]
    if t == "dark" and not any(d["selector"].split(",")[0].strip() == ".dark" for d in own):
        own += [d for d in out if d["selector"].split(",")[0].strip() == ":root"]
    if t == "dark":
        own = [d for d in own if not (d["selector"].split(",")[0].strip() == ":root" and any(x["selector"] == ".dark" for x in own))]
    if t == "light":
        own = [d for d in own if d["selector"].split(",")[0].strip() in (":root", ":root:not(.dark)")]
    return [d for d in own if not d["condition"] or "color-mix" in d["condition"] or d["condition"].startswith("@layer theme")]


def formula(t, name):
    ds = decls(t, name)
    applied = [d for d in ds if d["condition"] and "color-mix" in d["condition"]]
    return (applied or [d for d in ds if not d["condition"] or d["condition"].startswith("@layer")] or ds or [{"value": None}])[0]["value"]


def path_of(name):
    for pre, group in GROUPS:
        if name.startswith(pre):
            rest = name[len(pre):]
            return (group, rest or "default")
    raise KeyError(name)


def where(t, name, extra=""):
    return f"{name} as painted on <body>, {THEME_NAME[t]}, {DATE}{extra}"


# ---------------------------------------------------------------- core: the scales

CORE = {}
dark_comp, light_comp = computed("dark"), computed("light")
for n in ("--color-black", "--color-white"):
    put(CORE, ("color", n[8:]), tok(color(V["dark"]["colors"][n]), "color", "Measured",
        f"{n} as painted (Tailwind's black and white, the only palette steps Capy loads; both themes), {DATE}"))


def core_dim(group, key, name, conv=rem, ty="dimension", **ext):
    if name not in dark_comp:
        raise KeyError(f"{name} is not on <body> in the dark reading")
    v = dark_comp[name]
    if light_comp.get(name) != v:
        raise ValueError(f"{name} differs by theme")
    touch = [d["value"] for d in V["dark"]["decls"] if d["name"] == f"--responsive-{name[2:]}" and d["selector"].startswith(":root, [data-theme")]
    put(CORE, (group, key), tok(conv(v), ty, "Measured", f"{name} on <body>, both themes, {DATE}", css=v,
        touch=(conv(touch[0]) if touch else None), **ext))


# radius: Capy names its radii by use (button, card, overlay, panel, kbd, inner) beside Tailwind's steps
for key in ("xs", "sm", "md", "lg"):
    core_dim("radius", key, f"--radius-{key}")
for key in ("inner", "kbd", "button", "card", "overlay", "panel"):
    core_dim("radius", key, f"--radius-{key}")
core_dim("radius", "default", "--radius")
put(CORE, ("radius", "full"), tok("9999px", "dimension", "Measured", f"rounded-full on switches, badges and the count chip (computed 9999px or 50%), {DATE}"))
# spacing: Tailwind's one step; every p-*, gap-* and m-* class is a multiple of it
core_dim("spacing", "unit", "--spacing")
for n in (0.5, 1, 1.5, 2, 2.5, 3, 4, 5, 6, 8, 10, 12):
    put(CORE, ("spacing", ("%g" % n).replace(".", "-")), tok(px("%gpx" % (4 * n)), "dimension", "Derived",
        f"calc(var(--spacing) * {n:g}), Tailwind's spacing class {n:g}", formula=f"calc(var(--spacing) * {n:g})"))
core_dim("spacing", "page-padding", "--spacing-page-padding")
# control sizes: --h-* (desktop values; the --responsive-* copies under (pointer: coarse) are recorded as `touch`)
for key in ("xs", "sm", "base"):
    core_dim("controlHeight", key, f"--h-control-{key}")
core_dim("controlHeight", "menu-row", "--h-menu-row")
core_dim("controlHeight", "palette-row", "--h-palette-row")
for key in ("xs", "sm", "base", "count"):
    core_dim("badgeHeight", key, f"--h-badge-{key}")
for key in ("xs", "sm", "base", "lg"):
    core_dim("iconSize", key, f"--icon-{key}")
# type
for key in ("2xs", "xs", "sm", "base", "lg", "xl", "2xl", "3xl", "4xl", "5xl", "7xl", "markdown", "code-block", "count-chip", "plan-chip"):
    core_dim("fontSize", key, f"--text-{key}")
    lh = dark_comp.get(f"--text-{key}--line-height")
    if lh:
        m = re.fullmatch(r"calc\(\s*([\d.]+)\s*/\s*([\d.]+)\s*\)", lh)
        ratio = float(m.group(1)) / float(m.group(2)) if m else float(lh)
        size = float(rem(dark_comp[f"--text-{key}"])[:-2])
        put(CORE, ("lineHeight", key), tok(px("%gpx" % round(size * ratio, 2)), "dimension", "Measured",
            f"--text-{key}--line-height on <body> ({lh}, a ratio to the size), {DATE}", css=lh))
    ls = dark_comp.get(f"--text-{key}--letter-spacing")
    if ls:
        put(CORE, ("letterSpacing", key), tok(ls.replace("-.", "-0.") if ls.startswith("-.") else ("0" + ls if ls.startswith(".") else ls), "dimension", "Measured",
            f"--text-{key}--letter-spacing on <body>, {DATE}"))
for key in ("normal", "medium", "semibold", "bold"):
    core_dim("fontWeight", key, f"--font-weight-{key}", conv=int, ty="fontWeight")
for key in ("snug", "normal", "relaxed"):
    core_dim("leading", key, f"--leading-{key}", conv=float, ty="number")
core_dim("letterSpacing", "wider", "--tracking-wider", conv=lambda v: "0" + v if v.startswith(".") else v)
for key, n in (("sans", "--font-sans"), ("mono", "--font-mono"), ("terminal", "--font-terminal")):
    stack = [f.strip().strip("'\"") for f in dark_comp[n].split(",")]
    put(CORE, ("fontFamily", key), tok(stack, "fontFamily", "Measured", f"{n} on <body>, {DATE}"))
# motion
put(CORE, ("duration", "default"), tok(ms(dark_comp["--default-transition-duration"]), "duration", "Measured", f"--default-transition-duration on <body>, {DATE}"))
for key in ("fast", "base", "slow", "slower"):
    put(CORE, ("duration", key), tok(ms(dark_comp[f"--duration-{key}"]), "duration", "Measured", f"--duration-{key} on <body>, {DATE}"))
for key, n in (("default", "--default-transition-timing-function"), ("in-out", "--ease-in-out"), ("out", "--ease-out"), ("out-quint", "--ease-out-quint")):
    put(CORE, ("easing", key), tok(bezier(dark_comp[n]), "cubicBezier", "Measured", f"{n} on <body>, {DATE}", css=dark_comp[n]))
core_dim("blur", "xs", "--blur-xs")
for key in ("xs", "sm", "md", "lg", "xl", "2xl", "3xl", "4xl", "5xl", "6xl"):
    core_dim("container", key, f"--container-{key}")
core_dim("layout", "shell-top", "--shell-top")
for key in ("chat-row-lift", "table-lead", "top-bar", "sidebar", "drawer", "dialog", "overlay-content", "toast", "tooltip"):
    core_dim("zIndex", key, f"--z-{key}", conv=int, ty="number")

# ---------------------------------------------------------------- semantic sets


def semantic(t):
    tree, comp, painted = {}, computed(t), V[t]["colors"]
    names = sorted(n for n in comp if (not SKIP.match(n) or n in KEEP_ALSO))
    for n in names:
        if n not in painted or not is_color(painted[n]):
            continue
        p = path_of(n)
        value = color(painted[n])
        f = formula(t, n)
        m = re.fullmatch(r"var\((--[\w-]+)\)", f or "")
        if m and m.group(1) in painted and is_color(painted[m.group(1)]) and color(painted[m.group(1)]) == value and not SKIP.match(m.group(1)):
            target = path_of(m.group(1))
            put(tree, p, tok("{%s}" % ".".join(target), "color", "Measured", where(t, n), formula=f))
        elif f and re.fullmatch(r"(#[0-9a-fA-F]{3,8}|oklch\([^()]*\))", f):
            put(tree, p, tok(value, "color", "Measured", where(t, n, f"; declared {f}")))
        else:
            put(tree, p, tok(value, "color", "Measured", where(t, n), formula=f or comp[n]))
    return tree


SETS = {t: semantic(t) for t in THEMES}


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


def style(t, part, state="default"):
    hit = P[t].get((part, state))
    if not hit and state == "default":
        # A part only seen in one state (the tooltip appears on hover) is read there.
        hit = next((v for (p, s), v in sorted(P[t].items()) if p == part), None)
    return hit if hit else (None, None)


# Type roles, measured on real elements.
ROLES = [("heading", "page-title", "Page titles (h1 in Settings and the gallery, text-xl)"),
         ("heading-2", "markdown-h1", "Document titles in markdown (threads, plans)"),
         ("subheading", "section-title", "Settings section titles (h2)"),
         ("body", "row-label", "Settings row labels, menu items, list text"),
         ("body-secondary", "row-description", "Row descriptions (muted-foreground-2)"),
         ("label", "button-outline", "Button labels"),
         ("caption", "badge", "Badges"),
         ("small", "kbd", "Shortcut hints"),
         ("prompt", "composer-editor", "Text typed in the composer"),
         ("message", "message-text", "Agent replies in a thread (markdown, 13px)"),
         ("code", "code-block", "Code blocks in markdown")]
for role, part, use in ROLES:
    shot, s = style("dark", part)
    if not s:
        continue
    fam = "{fontFamily.mono}" if role in ("code", "terminal") else "{fontFamily.sans}"
    lh = s["line-height"]
    val = {"fontFamily": fam, "fontSize": px(s["font-size"]), "fontWeight": int(s["font-weight"]),
           "lineHeight": px(lh) if lh.endswith("px") else "normal",
           "letterSpacing": px(s["letter-spacing"]) if s["letter-spacing"].endswith("px") else "0px"}
    notes = []
    if val["lineHeight"] == "normal":
        val["lineHeight"] = px("%gpx" % round(float(s["font-size"][:-2]) * 1.2, 1))
        notes.append("computed line-height is normal; 1.2 x the size is used here")
    if not s["letter-spacing"].endswith("px"):
        # `normal` adds no tracking, so 0px stands for it; it is not a computed length, and the token says so.
        notes.append(f"computed letter-spacing is {s['letter-spacing']}; 0px is used here")
    note = "; ".join(notes) or None
    put(CORE, ("typography", role), tok(val, "typography", "Measured", f"computed style of {part} in {shot}, dark, {DATE}; {use}", note=note))


def dim_of(part, prop, state="default", t="dark"):
    shot, s = style(t, part, state)
    return (shot, s[prop]) if s and s.get(prop, "").endswith("px") else (None, None)


SIZES = [("size.control.icon-button", "icon-button", "height", "Sidebar icon buttons"),
         ("size.control.send", "send-button", "height", "The composer's Start button"),
         ("size.control.tab", "tab", "height", "Desktop tabs in the title bar"),
         ("size.control.tab-width", "tab", "width", "Desktop tabs in the title bar"),
         ("size.control.nav-row", "nav-row", "height", "Sidebar navigation rows"),
         ("size.control.thread-row", "thread-row", "height", "Sidebar thread rows (title over the project key)"),
         ("size.control.settings-nav", "settings-nav", "height", "Settings navigation rows"),
         ("size.control.settings-row", "settings-row", "height", "Settings rows"),
         ("size.control.menu-item", "menu-item", "height", "Menu items"),
         ("size.control.switch-width", "switch-on", "width", "Switch"),
         ("size.control.switch-height", "switch-on", "height", "Switch"),
         ("size.control.checkbox", "checkbox-on", "height", "Checkbox"),
         ("size.control.input", "input", "height", "Inputs in Settings rows (the sm size)"),
         ("size.control.settings-input", "settings-search", "height", "The Settings search field"),
         ("layout.sidebar", "sidebar", "width", "Left sidebar (the owner's 240px)"),
         ("layout.tab-strip-height", "tab-strip", "height", "The desktop tab strip, the window's title bar"),
         ("layout.composer", "composer", "width", "The new-thread composer"),
         ("layout.settings-card", "card", "width", "Settings content column"),
         ("layout.confirm-dialog", "confirm-dialog", "width", "Delete thread confirmation"),
         ("layout.palette", "palette", "width", "Search palette"),
         ("layout.menu", "menu", "width", "Menus (the user menu)"),
         ("layout.toast", "toast", "width", "Toasts")]
for path, part, prop, use in SIZES:
    shot, v = dim_of(part, prop)
    if v:
        put(CORE, tuple(path.split(".")), tok(px("%gpx" % round(float(v[:-2]))), "dimension", "Measured",
            f"computed {prop} of {part} in {shot}, dark, {DATE} ({use}); {v} before rounding"))
# The inspector (a thread's right pane: Overview, Diffs, Files, Shell) is only on screen inside a thread, so its
# width comes from the agent run's kept frame that opened it (raw/run.<theme>.json, run.mjs on Capy 0.5.0).
RUN = load("run.dark.json") if (RAW / "run.dark.json").exists() else {}
_pane = RUN.get("run-inspector", {}).get("parts", {}).get("right-panel", {}).get("style", {})
if _pane.get("width", "").endswith("px"):
    put(CORE, ("layout", "inspector"), tok(px("%gpx" % round(float(_pane["width"][:-2]))), "dimension", "Measured",
        f"computed width of right-panel in run-inspector (the thread's right pane, opened in the test run on Capy 0.5.0), dark, {DATE}; {_pane['width']} before rounding"))
WINDOW = C["dark"]["home"]["viewport"]
put(CORE, ("layout", "window-width"), tok(f"{WINDOW['css'][0]}px", "dimension", "Measured",
    f"the window's viewport, {WINDOW['css'][0]} x {WINDOW['css'][1]} CSS px at devicePixelRatio {WINDOW['dpr']}, {DATE}"))
put(CORE, ("layout", "window-height"), tok(f"{WINDOW['css'][1]}px", "dimension", "Measured", f"the window's viewport height, {DATE}"))
put(CORE, ("borderWidth", "hairline"), tok("0.5px", "dimension", "Measured", f"border-[0.5px] on cards, the panel, tabs, inputs and badges (computed 0.5px), {DATE}"))
# focus ring: Capy's focus-visible draws an outline or ring in --ring; read on a focused part
for part in ("button-outline", "button-accent", "select", "row-button", "input", "switch-off"):
    shot, s = style("dark", part, "focus-visible")
    if not s:
        continue
    if s["outline-style"] not in ("none", "") and s["outline-width"] not in ("0px", ""):
        put(CORE, ("focusRing", "width"), tok(px(s["outline-width"]), "dimension", "Measured",
            f"outline-width of {part} in {shot}, dark, {DATE}", css=f"{s['outline-width']} {s['outline-style']} {s['outline-color']}"))
        put(CORE, ("focusRing", "offset"), tok(px(s["outline-offset"]), "dimension", "Measured", f"outline-offset of {part} in {shot}, dark, {DATE}"))
        break
    layers = [l for l in shadow(s["box-shadow"]) if not l["color"].endswith(", 0)")] if s["box-shadow"] != "none" else []
    if layers:
        ring = max(layers, key=lambda l: float(l["spread"][:-2]))
        put(CORE, ("focusRing", "width"), tok(ring["spread"], "dimension", "Measured",
            f"spread of the focus box-shadow of {part} in {shot}, dark, {DATE}", css=s["box-shadow"]))
        put(CORE, ("focusRing", "offset"), tok("0px", "dimension", "Measured", f"the ring is a box-shadow drawn outside the border, no offset ({shot}), {DATE}"))
        break

cond = V["dark"]["conditions"]
rm = {k: v["rules"] for k, v in cond.items() if "reduced-motion" in k}
CORE.setdefault("duration", {})["$extensions"] = {"reducedMotion": {"rules": rm,
    "how": "Tailwind's motion-safe: and motion-reduce: variants under (prefers-reduced-motion): enter transitions and the dot-grid loaders stop; no duration token changes"}}
bp = sorted({k for k in cond if re.search(r"width", k)})
CORE.setdefault("layout", {})["$extensions"] = {"breakpointsInCss": bp[:40],
    "note": "Tailwind's md 768px splits the phone layout from the desktop one ((width >= 768px), (hover: hover) and (pointer: fine)); many views also use container queries (pull, list, composer, rail). The desktop window is resizable"}

# ---------------------------------------------------------------- roles and components, per theme

ROLE = {
    "page": ("{base.panel}", "the content panel every page sits in, a rounded inset on the window"),
    "surface": ("{base.chrome}", "the window: tab strip and sidebar (chrome is var(--bg))"),
    "raised": ("{base.popover}", "menus, the composer, dialogs, the active tab; cards use base.card"),
    "overlay": (None, "palette", "the search palette"),
    "scrim": ("{base.overlay}", "behind dialogs and the palette"),
    "text.primary": ("{base.fg}", ""), "text.secondary": ("{base.muted-foreground-1}", "the text mixed into the window colour"),
    "text.disabled": ("{base.muted-foreground-3}", "the lightest text tier: placeholders and disabled labels"),
    "text.on-accent": ("{base.primary-text}", ""), "text.link": ("{base.text-link}", "the primary darkened with black (light) or the primary (dark)"),
    "border.default": ("{base.border-1}", "cards, the panel, separators"), "border.strong": ("{base.border-3}", "the strongest hairline tier"),
    "border.focus": ("{base.ring}", "the focus outline"),
    "accent.default": ("{base.primary}", "Capy's teal"),
    "accent.subtle": ("{base.primary-soft}", "the primary at 20% (24% in dark): selected and soft fills"),
    "brand": ("{base.shader-ink}", "the dot-grid shader's ink on the home page"),
}
ROLE["status.success.fill"] = ("{base.success}", "")
ROLE["status.success.text"] = ("{base.success}", "Capy has one success colour")
ROLE["status.warning.fill"] = ("{base.warning}", "")
ROLE["status.warning.text"] = ("{base.warning-fg}", "")
ROLE["status.warning.subtle"] = ("{base.warning-subtle}", "the warning at 10%")
ROLE["status.danger.fill"] = ("{base.destructive}", "")
ROLE["status.danger.text"] = ("{base.destructive}", "")
ROLE["status.danger.subtle"] = ("{base.destructive-soft}", "the destructive at 18% (22% in dark)")
ROLE["status.danger.on"] = ("{base.destructive-text}", "")
ROLE["status.info.fill"] = ("{base.info}", "")
ROLE["status.info.text"] = ("{base.info}", "Capy has one info colour")

BTN = {"bg": "background-color", "text": "color", "radius": "border-top-left-radius", "height": "height", "padding": "padding-right"}
COMPONENTS = [
    ("button-accent", "button-accent", BTN),
    ("button-outline", "button-outline", {**BTN, "border": "border-top-color"}),
    ("button-soft", "button-soft", BTN),
    ("button-solid", "button-solid", {**BTN, "border": "border-top-color"}),
    ("button-ghost", "button-ghost", {"text": "color", "radius": "border-top-left-radius", "height": "height"}),
    ("button-selected", "button-selected", BTN),
    ("button-inverse", "button-inverse", BTN),
    ("button-danger", "button-danger", BTN),
    ("button-danger-text", "button-danger-text", {"text": "color"}),
    ("icon-button", "icon-button", {"text": "color", "radius": "border-top-left-radius", "size": "height"}),
    ("send-button", "send-button", {"bg": "background-color", "text": "color", "radius": "border-top-left-radius", "size": "height"}),
    ("composer", "composer", {"bg": "background-color", "border": "border-top-color", "radius": "border-top-left-radius", "padding": "padding-top"}),
    ("menu", "menu", {"bg": "background-color", "border": "border-top-color", "text": "color", "radius": "border-top-left-radius"}),
    ("menu-item", "menu-item", {"text": "color", "radius": "border-top-left-radius", "height": "height", "padding": "padding-left"}),
    ("confirm-dialog", "confirm-dialog", {"bg": "background-color", "border": "border-top-color", "radius": "border-top-left-radius"}),
    ("palette", "palette", {"bg": "background-color", "border": "border-top-color", "radius": "border-top-left-radius"}),
    ("palette-row", "palette-row", {"text": "color", "radius": "border-top-left-radius", "height": "height"}),
    ("scrim", "scrim", {"bg": "background-color"}),
    ("tooltip", "tooltip", {"bg": "background-color", "text": "color", "radius": "border-top-left-radius"}),
    ("toast", "toast", {"bg": "background-color", "border": "border-top-color", "text": "color", "radius": "border-top-left-radius"}),
    ("tab", "tab", {"bg": "background-color", "text": "color", "radius": "border-top-left-radius", "height": "height"}),
    ("tab-active", "tab-active", {"bg": "background-color", "border": "border-top-color", "text": "color"}),
    ("segmented-item", "segmented-item", {"text": "color", "radius": "border-top-left-radius", "height": "height"}),
    ("segmented-active", "segmented-active", {"bg": "background-color", "text": "color"}),
    ("input", "input", {"bg": "background-color", "border": "border-top-color", "text": "color", "radius": "border-top-left-radius", "height": "height"}),
    ("input-invalid", "input-invalid", {"border": "border-top-color"}),
    ("settings-search", "settings-search", {"bg": "background-color", "border": "border-top-color", "text": "color", "radius": "border-top-left-radius", "height": "height"}),
    ("select", "select", {"bg": "background-color", "border": "border-top-color", "text": "color", "radius": "border-top-left-radius", "height": "height"}),
    ("switch-on", "switch-on", {"bg": "background-color", "radius": "border-top-left-radius"}),
    ("switch-off", "switch-off", {"bg": "background-color", "border": "border-top-color"}),
    ("checkbox-on", "checkbox-on", {"bg": "background-color", "radius": "border-top-left-radius"}),
    ("checkbox-off", "checkbox-off", {"bg": "background-color", "border": "border-top-color"}),
    ("badge", "badge", {"bg": "background-color", "border": "border-top-color", "text": "color", "radius": "border-top-left-radius", "height": "height"}),
    ("badge-failed", "badge-failed", {"bg": "background-color", "text": "color"}),
    ("badge-passing", "badge-passing", {"bg": "background-color", "text": "color"}),
    ("badge-count", "badge-count", {"bg": "background-color", "text": "color", "height": "height"}),
    ("card", "card", {"bg": "background-color", "border": "border-top-color", "radius": "border-top-left-radius"}),
    ("panel", "panel", {"bg": "background-color", "border": "border-top-color", "radius": "border-top-left-radius"}),
    ("nav-row", "nav-row", {"text": "color", "radius": "border-top-left-radius", "height": "height"}),
    ("nav-row-selected", "nav-row-selected", {"bg": "background-color", "text": "color"}),
    ("thread-row", "thread-row", {"text": "color", "radius": "border-top-left-radius"}),
    ("settings-nav", "settings-nav", {"text": "color", "radius": "border-top-left-radius", "height": "height"}),
    ("settings-nav-selected", "settings-nav-selected", {"bg": "background-color", "text": "color"}),
    ("setup-card", "setup-card", {"bg": "background-color", "border": "border-top-color", "radius": "border-top-left-radius"}),
    ("user-message", "user-message", {"text": "color"}),
    ("code-block", "code-block", {"bg": "background-color", "border": "border-top-color", "radius": "border-top-left-radius"}),
    ("inline-code", "inline-code", {"bg": "background-color", "text": "color", "radius": "border-top-left-radius"}),
    ("alert", "alert", {"bg": "background-color", "border": "border-top-color", "radius": "border-top-left-radius"}),
    ("table-row", "table-row", {"text": "color", "height": "height"}),
    ("kbd", "kbd", {"bg": "background-color", "text": "color", "radius": "border-top-left-radius", "height": "height"}),
]
STATES = [("hover", "bg-hover", "background-color"), ("hover", "text-hover", "color"), ("pressed", "bg-pressed", "background-color"),
          ("focus-visible", "outline-focus", "outline-color")]
# The names a measured colour is written as first, in this order where two paint the same (the ring is the primary in dark).
CORE_ORDER = ["base.fg", "base.primary", "base.primary-text", "base.panel", "base.card", "base.popover", "base.bg", "base.chrome", "base.input", "base.button", "base.secondary", "base.muted", "base.border-1", "base.border-2", "base.border-3", "base.destructive", "base.overlay", "base.ring"]
PREFER = ["role", "base", "chart", "diff", "color"]


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
        vals.sort(key=lambda p: (CORE_ORDER.index(p) if p in CORE_ORDER else 99, PREFER.index(p.split(".")[0]) if p.split(".")[0] in PREFER else 99, len(p), p))
    return idx


def css_shadow(css):
    """A shadow as its custom property computes (the declared text: `0 1px 2px oklch(0% 0 0/.05)`) -> layers.
    vars.mjs paints only names containing `shadow`, so Capy's --sh-* levels are read from this text: the oklch
    channels are rewritten in the form colour.py reads, and bare decimals get their leading zero."""
    def ok(m):
        l, c, h, a = m.group(1), m.group(2), m.group(3), m.group(4)
        l = "%g" % (float(l[:-1]) / 100) if l.endswith("%") else l
        return f"oklch({l} {c} {h}" + (f" / {float(a):g})" if a else ")")
    css = re.sub(r"oklch\(\s*([\d.]+%?)\s+([\d.]+)\s+([\d.]+)\s*(?:/\s*([\d.]+))?\s*\)", ok, css)
    css = re.sub(r"(?<![\d.])\.(\d)", r"0.\1", css)
    return shadow(css)


def visible_shadow(css):
    """Tailwind writes every box-shadow as ring, ring-offset and shadow layers; the unused ones are transparent zeros."""
    return [l for l in shadow(css) if not l["color"].endswith(", 0)")]


SHADOWS = [("plate", "--sh-plate", "the switch thumb and small raised chips"), ("card", "--sh-card", "cards and the active tab: a hairline ring, no blur"),
           ("overlay", "--sh-overlay", "menus, popovers, tooltips and the palette"), ("composer", "--sh-composer", "the composer"),
           ("sheet", "--sh-sheet", "sheets and drawers; dialogs carry the overlay level")]


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
    # The five shadow levels, as painted, each with the parts measured carrying it.
    used = {}
    for (part, state), (shot, s) in sorted(P[t].items()):
        if state == "default" and s.get("box-shadow", "none") != "none":
            used.setdefault(json.dumps(visible_shadow(s["box-shadow"])), []).append(part)
    for key, name, use in SHADOWS:
        layers = [l for l in css_shadow(computed(t)[name]) if not l["color"].endswith(", 0)")]
        put(tree, ("shadow", key), tok(layers, "shadow", "Measured", f"{name} as it computes on <body> (oklch converted to sRGB), {THEME_NAME[t]}, {DATE}; {use}",
            css=computed(t)[name], usedBy=sorted(set(used.get(json.dumps(layers), []))) or None))

    def value_for(part, shot, prop, raw):
        nonlocal measured_n, aliased_n
        src = f"computed {prop} of {part} in {shot}, {THEME_NAME[t]}, {DATE}"
        if prop in ("background-color", "color", "border-top-color", "outline-color"):
            v = color(raw)
            measured_n += 1
            if v in idx:
                aliased_n += 1
                # A text colour prefers a foreground or text name, a fill or edge one that is not.
                textish = lambda x: any(w in x for w in ("fg", "foreground", "text"))
                fits = [x for x in idx[v] if textish(x) == (prop == "color") and not x.startswith("role.")]
                return tok("{%s}" % (fits or idx[v])[0], "color", "Measured", src, painted=v)
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
            if not ss or ss[prop] == s[prop] or not is_color(ss[prop]) or color(ss[prop]) == "rgba(0, 0, 0, 0)":
                continue
            if prop == "outline-color" and ss["outline-style"] in ("none", ""):
                continue
            put(tree, ("component", name, key), value_for(part, sh, prop, ss[prop]))
    # Roles that are states of a component rather than a declared colour.
    for key, (comp_path, why) in {"accent.hover": ("component.button-accent.bg-hover", "the accent button under the pointer"),
                                  "accent.pressed": ("component.button-accent.bg-pressed", "the accent button with :active forced")}.items():
        hit = get(tree, comp_path) or get(tree, "component.button-accent.bg")
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
         "$description": "Settings > Appearance > Theme: System with a light appearance, or Light (html.light), with the default Capy colour theme"},
        {"id": "dark", "name": "Dark", "selectedTokenSets": {"core": "source", "dark": "enabled"},
         "$description": "Settings > Appearance > Theme: System with a dark appearance, or Dark (html.dark), with the default Capy colour theme"},
    ],
    "$metadata": {"tokenSetOrder": ["core", "light", "dark"]},
}
(PKG / "tokens.json").write_text(json.dumps(tokens, indent=2, ensure_ascii=False) + "\n")


def count(d):
    return sum(1 for _ in tokens_of(d))


print({k: count(tokens[k]) for k in ("core", "light", "dark")}, "component values aliased:",
      {t: SETS[t]["$extensions"]["componentValues"] for t in THEMES})
