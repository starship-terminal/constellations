#!/usr/bin/env python3
"""Build tokens.json (W3C DTCG, Tokens Studio multi-set layout) from the raw readings.

    python3 tools/build_tokens.py

Sources, read live from Devin 3.11.216 for macOS on 2026-10-25 over the remote-debugging port
(tools/capture/electron/):
  raw/css-vars.<theme>.json      every semantic custom property the Agents view's stylesheets declare
                                 (--bg-*, --text-*, --border-*, --tint-*, --shadow-*, the hues, diff and
                                 chart colours), by sheet, selector and condition, and each name as it
                                 computes and paints on .devin-app-root
  raw/css-vars.ide-<theme>.json  the same for the IDE view (--vscode-*), on .monaco-workbench
  raw/utilities.<theme>.json     the Tailwind utility classes on screen across the captured screens, with
                                 their declarations (font sizes, radii, spacing, durations, focus ring)
  raw/components.<theme>.json    computed styles of the captured parts, per shot and state (shots.mjs)

How Devin's colours work, and so how this file is laid out. The Agents view is a Tailwind v3 app whose
theme is a list of colour channels declared per theme on .devin-app-root.dark and .light (index.css):
`--text-secondary: 255 255 255 / 0.52`, painted as rgb(var(--text-secondary)). So every neutral is
white (dark) or near-black (light) at a fixed alpha, and the hues are a handful of flat colours. Each
semantic set holds those values (bg, text, border, tint, the hues, diff, chart), the shadows, the IDE
view's VS Code colours (which Devin's theme maps onto the same values), the checklist roles (role.*)
and measured component values (component.*). Tailwind's scales are not custom properties, so the core
set comes from the utility classes the screens use. Every token carries $extensions.source =
{evidence, from}. Deterministic: same inputs, same bytes.
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

SCOPE = ".devin-app-root"
THEME_NAME = {"light": "Devin Light", "dark": "Devin Dark"}
THEME_SEL = {"light": ".devin-app-root.devin-app-root.light", "dark": ".devin-app-root.devin-app-root.dark"}
# Colour groups, by the name's first word: --bg-page -> bg.page. The six hues are one name each.
GROUPS = ["bg", "text", "border", "tint", "chart", "diff", "word-diff"]
HUES = ["red", "orange", "yellow", "green", "blue", "purple"]
SHADOW_COLOR = "--shadow-shadow-"           # colour channels behind Tailwind's shadow-* colours
SHADOWS = ["L1", "L2", "L2-border", "L3", "L4", "L4-wax", "inner"]
IDE_NAMES = ["editor-background", "editor-foreground", "editorLineNumber-foreground", "editorLineNumber-activeForeground",
             "sideBar-background", "sideBar-foreground", "activityBar-background", "statusBar-background", "statusBar-foreground",
             "titleBar-activeBackground", "titleBar-activeForeground", "tab-activeBackground", "tab-activeForeground",
             "tab-inactiveBackground", "tab-inactiveForeground", "editorGroupHeader-tabsBackground", "panel-background", "panel-border",
             "focusBorder", "list-hoverBackground", "list-activeSelectionBackground", "quickInput-background",
             "quickInputList-focusBackground", "input-background", "input-border", "input-foreground", "button-background",
             "button-foreground", "button-hoverBackground", "button-secondaryBackground", "button-secondaryForeground",
             "keybindingLabel-background", "keybindingLabel-foreground", "editorWidget-background", "dropdown-background",
             "menu-background", "menu-selectionBackground", "scrollbarSlider-background", "errorForeground", "textLink-foreground",
             "banner-background", "banner-foreground", "notifications-background", "notifications-foreground",
             "notificationsErrorIcon-foreground", "terminal-background", "terminal-foreground", "statusBarItem-warningBackground"]


def load(name):
    return json.loads((RAW / name).read_text())


V = {t: load(f"css-vars.{t}.json") for t in THEMES}
IDE = {t: load(f"css-vars.ide-{t}.json") for t in THEMES}
U = {t: load(f"utilities.{t}.json") for t in THEMES}
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


def decl(t, name):
    """The declaration that sets `name` for this theme on the Agents view's root, and where it is."""
    for d in V[t]["decls"]:
        if d["name"] == name and d["condition"] == "" and d["selector"].startswith(THEME_SEL[t]) and "high-contrast" not in d["selector"]:
            return d
    for d in V[t]["decls"]:
        if d["name"] == name and d["condition"] == "" and d["sheet"] == "index.css" and "high-contrast" not in d["selector"]:
            return d
    return None


def where(t, name, d=None, extra=""):
    at = f" ({d['sheet']}: {d['selector'][:60]})" if d else ""
    return f"{name} on {SCOPE}, Agents view, {THEME_NAME[t]}, {DATE}{at}{extra}"


def path_of(name):
    """--text-secondary -> ('text', 'secondary'); --word-diff-added-bg -> ('word-diff', 'added-bg'); --red -> ('hue', 'red')."""
    rest = name[2:]
    if rest in HUES:
        return ("hue", rest)
    for g in sorted(GROUPS, key=len, reverse=True):
        if rest.startswith(g + "-"):
            return (g, rest[len(g) + 1:])
    return None


# ---------------------------------------------------------------- semantic sets


def semantic(t):
    tree, comp, painted = {}, computed(t), V[t]["colors"]
    channels = set(V[t].get("channels", []))
    names = sorted(n for n in comp if path_of(n) and n in painted and is_color(painted[n]))
    paths = {n: path_of(n) for n in names}
    for n in names:
        p, d = paths[n], decl(t, n)
        value = color(painted[n])
        raw = (d or {}).get("value", comp[n])
        m = re.fullmatch(r"(?:rgb\()?var\((--[\w-]+)\)\)?", raw)
        if m and m.group(1) in paths and color(painted[m.group(1)]) == value:
            put(tree, p, tok("{%s}" % ".".join(paths[m.group(1)]), "color", "Measured", where(t, n, d), formula=raw))
            continue
        put(tree, p, tok(value, "color", "Measured", where(t, n, d), declared=raw,
                         painted="rgb(var(%s))" % n if n in channels else None))
    for n in sorted(comp):
        if n.startswith(SHADOW_COLOR) and n in painted and is_color(painted[n]):
            put(tree, ("shadow-color", n[len(SHADOW_COLOR):]), tok(color(painted[n]), "color", "Measured", where(t, n, decl(t, n)),
                declared=comp[n], painted=f"rgb(var({n}))"))
    for key in SHADOWS:
        n = f"--shadow-{key}"
        s = V[t]["shadows"].get(n)
        if s and s != "none":
            put(tree, ("shadow", key), tok(shadow(s), "shadow", "Measured", where(t, n, decl(t, n), "; box-shadow as painted"), formula=comp.get(n)))
    ide_painted = IDE[t]["colors"]
    for k in IDE_NAMES:
        n = "--vscode-" + k
        if n in ide_painted and is_color(ide_painted[n]):
            put(tree, ("ide", k), tok(color(ide_painted[n]), "color", "Measured", f"{n} on .monaco-workbench, IDE view, {THEME_NAME[t]}, {DATE}"))
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
            out.setdefault((part, d["state"]), (shot, v["style"]))
    return out


P = {t: parts(t) for t in THEMES}


def style(t, part, state="default"):
    hit = P[t].get((part, state))
    return hit if hit else (None, None)


# ---------------------------------------------------------------- core: the utility classes in use

CORE = {}
UT = U["dark"]["classes"]
SCREENS = len(U["dark"].get("screens", []))


def rem_px(v, scale=1.0):
    """'calc(.8125rem * var(--text-scale,1))' or '0.375rem' or '6px' -> '13px'; None if not a length."""
    v = v.strip()
    m = re.fullmatch(r"calc\(\s*(-?[\d.]+)rem\s*\*\s*var\(--text-scale,\s*1\)\)", v)
    if m:
        return "%gpx" % round(float(m.group(1)) * 16 * scale, 2)
    m = re.fullmatch(r"calc\((-?[\d.]+)px \+ ([\d.]+)rem\)", v)
    if m:
        return "%gpx" % round(float(m.group(1)) + float(m.group(2)) * 16, 2)
    m = re.fullmatch(r"(-?[\d.]+)rem", v)
    if m:
        return "%gpx" % round(float(m.group(1)) * 16, 2)
    m = re.fullmatch(r"(-?[\d.]+)px", v)
    if m:
        return "%gpx" % round(float(m.group(1)), 2)
    if v == "0":
        return "0px"
    return None


def usrc(cls, extra=""):
    c = UT[cls]
    decls = "; ".join(f"{k}: {v}" for k, v in c["props"].items())
    return f".{cls} {{ {decls} }} ({c['sheet']}), on {c['used']} elements across the {SCREENS} captured screens, dark, {DATE}{extra}"


# Type: Devin's own text-NN classes (size, line height and tracking together), scaled by --text-scale (1).
scale = float(computed("dark").get("--text-scale", "1") or 1)
for cls in sorted((c for c in UT if re.fullmatch(r"text-\d+", c)), key=lambda c: int(c[5:])):
    pr = UT[cls]["props"]
    size, lh = rem_px(pr.get("font-size", ""), scale), rem_px(pr.get("line-height", ""), scale)
    if not size:
        continue
    key = cls[5:]
    put(CORE, ("fontSize", key), tok(size, "dimension", "Measured", usrc(cls)))
    if lh:
        put(CORE, ("lineHeight", key), tok(lh, "dimension", "Measured", usrc(cls)))
    ls = pr.get("letter-spacing")
    if ls:
        em = float(ls[:-2])
        put(CORE, ("letterSpacing", key), tok("%gpx" % round(em * float(size[:-2]), 3), "dimension", "Derived",
            usrc(cls, f"; {ls} x {size}"), em=ls))
for cls, key in (("font-normal", "normal"), ("font-medium", "medium"), ("font-semibold", "semibold"), ("font-bold", "bold")):
    if cls in UT:
        put(CORE, ("fontWeight", key), tok(int(UT[cls]["props"]["font-weight"]), "fontWeight", "Measured", usrc(cls)))
if "fontWeight" not in CORE or "normal" not in CORE["fontWeight"]:
    put(CORE, ("fontWeight", "normal"), tok(400, "fontWeight", "Measured", f"computed font-weight of body text (13px/18px/400 on {U['dark']['sizes'].get('13px/18px/400', 0)} text nodes), dark, {DATE}"))

# Families: font-sans and font-mono read --font-ui and --font-code, which Settings > Preferences >
# Interface font (Inter) and Code font (Devin Mono) set; the stylesheet fallbacks follow.
for key, cls in (("sans", "font-sans"), ("mono", "font-mono")):
    fam = UT[cls]["props"]["font-family"]
    m = re.match(r"var\(--font-(?:ui|code),\s*([^)]+)\),\s*(.*)", fam)
    stack = [m.group(1).strip()] + [f.strip().strip("'\"") for f in m.group(2).split(",")]
    put(CORE, ("fontFamily", key), tok(stack, "fontFamily", "Measured", usrc(cls),
        note="The first family is the owner's choice under Settings > Preferences (Interface font Inter, Code font Devin Mono), passed as --font-ui / --font-code; both are also the defaults"))

# Radius: every border-radius the screens use, named by its size.
radii = {}
for cls, c in UT.items():
    v = c["props"].get("border-top-left-radius")
    if not v or ":" in cls or cls.startswith(("first", "last", "!")):
        continue
    pxv = "9999px" if v == "9999px" else rem_px(v)
    if pxv and pxv != "0px":
        radii.setdefault(pxv, []).append(cls)
for pxv, classes in sorted(radii.items(), key=lambda kv: float(kv[0][:-2])):
    key = "full" if pxv == "9999px" else pxv[:-2].replace(".", "-")
    best = max(classes, key=lambda c: UT[c]["used"])
    put(CORE, ("radius", key), tok(pxv, "dimension", "Measured", usrc(best), classes=sorted(classes), used=sum(UT[c]["used"] for c in classes)))

# Spacing: Tailwind's 4px scale, every step used by a padding or gap class, named by the step.
steps = {}
for cls, c in UT.items():
    m = re.fullmatch(r"-?(?:p[xytrbl]?|gap(?:-[xy])?|m[xytrbl]?|space-[xy])-(px|\d+(?:\.\d+)?)", cls)
    if not m:
        continue
    v = next((rem_px(x) for x in c["props"].values() if rem_px(x)), None)
    if v:
        steps.setdefault(m.group(1), (v, []))[1].append(cls)
for step, (v, classes) in sorted(steps.items(), key=lambda kv: float(kv[1][0][:-2])):
    best = max(classes, key=lambda c: UT[c]["used"])
    put(CORE, ("spacing", step.replace(".", "-")), tok(v, "dimension", "Measured", usrc(best), used=sum(UT[c]["used"] for c in classes)))
arbitrary = sorted({rem_px(v) for cls, c in UT.items() if re.fullmatch(r"(p[xytrbl]?|gap)-\[\d+px\]", cls) for v in c["props"].values() if rem_px(v)},
                   key=lambda v: float(v[:-2]))
CORE["spacing"]["$extensions"] = {"arbitraryValuesInUse": arbitrary,
    "note": "Besides the 4px steps, these exact px values are written as arbitrary Tailwind values (p-[6px], gap-[14px]) in the captured screens"}

# Motion: durations and easings the screens use (motion-safe: variants, so reduced motion drops them).
durs = {}
for cls, c in UT.items():
    v = c["props"].get("transition-duration") or c["props"].get("animation-duration")
    if v and re.fullmatch(r"[\d.]+m?s", v.split(",")[0].strip()):
        d = ms(v.split(",")[0])
        durs.setdefault(d, []).append(cls)
for d, classes in sorted(durs.items(), key=lambda kv: float(kv[0][:-2])):
    best = max(classes, key=lambda c: UT[c]["used"])
    put(CORE, ("duration", d[:-2]), tok(d, "duration", "Measured", usrc(best), classes=sorted(classes)[:8]))
eases = {}
for cls, c in UT.items():
    v = c["props"].get("transition-timing-function")
    if v and v.startswith("cubic-bezier"):
        eases.setdefault(v, []).append(cls)
EASE_NAMES = {"cubic-bezier(0.4, 0, 0.2, 1)": "standard", "cubic-bezier(0, 0, 0.2, 1)": "out", "cubic-bezier(0.4, 0, 1, 1)": "in",
              "cubic-bezier(0.25, 1, 0.5, 1)": "out-quart",
              "cubic-bezier(0.87, 0, 0.13, 1)": "in-out-expo", "cubic-bezier(0.76, 0, 0.24, 1)": "in-out-quart"}
for v, classes in sorted(eases.items()):
    if not bezier(v):
        continue
    key = EASE_NAMES.get(v, "e" + str(len(CORE.get("easing", {}))))
    best = max(classes, key=lambda c: UT[c]["used"])
    put(CORE, ("easing", key), tok(bezier(v), "cubicBezier", "Measured", usrc(best), css=v))
cond = V["dark"]["conditions"]
CORE["duration"]["$extensions"] = {"reducedMotion": {
    "rules": {k: v["rules"] for k, v in cond.items() if "reduced-motion" in k},
    "how": "Devin's transitions are written as motion-safe: variants, so under (prefers-reduced-motion: reduce) they do not apply; "
           "(prefers-reduced-motion: reduce) rules also stop the workbench's spinners and the chat's fade animations"}}

# Focus ring: the .focus-ring utility (1px outline, accent colour) on most controls; .focus-ring-inset
# draws it inside (-1px offset) on rows and links.
fr = UT.get("focus-ring:focus-visible", {}).get("props", {})
fri = UT.get("focus-ring-inset:focus-visible", {}).get("props", {})
put(CORE, ("focusRing", "width"), tok(px(fr.get("outline-width", "1px")), "dimension", "Measured", usrc("focus-ring:focus-visible")))
put(CORE, ("focusRing", "offset-inset"), tok(px(fri.get("outline-offset", "-1px")), "dimension", "Measured", usrc("focus-ring-inset:focus-visible")))
fs = next(((sh, s) for (part, state), (sh, s) in P["dark"].items() if state == "focus-visible" and s.get("outline-style") == "solid"), (None, None))
if fs[1]:
    put(CORE, ("focusRing", "offset"), tok(px(fs[1]["outline-offset"]) if fs[1]["outline-offset"].endswith("px") else "0px", "dimension", "Measured",
        f"computed outline-offset of a focused control in {fs[0]}, dark, {DATE}"))

# Type roles, measured on real elements (computed style).
ROLES = [("title", "page-title", "Settings and page titles"),
         ("section", "section-title", "Settings section headings"),
         ("body", "menu-row", "Menu rows, settings rows, list text, session titles (13/18)"),
         ("label", "button-primary-inverse", "Button labels (13/18, medium)"),
         ("caption", "sidebar-group-label", "Group labels in the sidebar and menus (12/16, medium)"),
         ("prompt", "composer-editor", "Text typed in the composer (14/20)"),
         ("message", "hook-error", "A reply paragraph in the transcript (14/20)"),
         ("status", "status-line", "Status lines under a turn (Devin is awaiting instructions)"),
         ("code", "inline-code", "Inline code in replies (Devin Mono)")]
for role, part, use in ROLES:
    shot, s = style("dark", part)
    if not s:
        continue
    mono = role == "code"
    lh = s["line-height"]
    val = {"fontFamily": "{fontFamily.mono}" if mono else "{fontFamily.sans}", "fontSize": px(s["font-size"]), "fontWeight": int(s["font-weight"]),
           "lineHeight": px(lh) if lh.endswith("px") else px("%gpx" % round(float(s["font-size"][:-2]) * 1.2, 1)),
           "letterSpacing": px(s["letter-spacing"]) if s["letter-spacing"].endswith("px") else "0px"}
    put(CORE, ("typography", role), tok(val, "typography", "Measured", f"computed style of {part} in {shot}, dark, {DATE}; {use}",
        note=None if lh.endswith("px") else "computed line-height is normal; 1.2 x the size is used here"))

# Sizes, layout, layers: measured boxes and computed widths.
def dim_of(part, prop, state="default", t="dark"):
    shot, s = style(t, part, state)
    return (shot, s[prop]) if s and s.get(prop, "").endswith("px") else (None, None)


SIZES = [("controlHeight.sm", "button-inverse-sm", "height", "Small buttons (Generate, Go to Customize, Add wiki)"),
         ("controlHeight.base", "composer-tool", "height", "Composer tools, icon buttons, selects, page buttons (Create automation)"),
         ("controlHeight.lg", "button-primary", "height", "The workbench dialog's buttons"),
         ("size.control.menu-row", "menu-row", "height", "Menu rows"),
         ("size.control.sidebar-row", "sidebar-row", "height", "Sidebar navigation rows"),
         ("size.control.session-row", "session-row", "height", "Two-line session rows"),
         ("size.control.palette-row", "palette-row", "height", "Command palette rows"),
         ("size.control.select", "select", "height", "Settings selects"),
         ("size.control.switch-width", "switch-on", "width", "Switch"), ("size.control.switch-height", "switch-on", "height", "Switch"),
         ("size.control.switch-sm-width", "switch-sm-on", "width", "Switch, small (in menus)"),
         ("size.control.switch-sm-height", "switch-sm-on", "height", "Switch, small (in menus)"),
         ("size.control.checkbox", "checkbox", "height", "Checkbox"),
         ("size.control.segment", "segment-selected", "height", "Segmented control (Cloud / Local)"),
         ("size.control.avatar", "avatar", "height", "Account avatar in the sidebar"),
         ("size.control.send", "send-button", "height", "Send button"),
         ("layout.sidebar", "sidebar", "width", "Agents view sidebar"),
         ("layout.composer", "composer", "width", "Composer on the empty New session page"),
         ("layout.settings-content", "settings-card", "width", "Settings content column"),
         ("layout.palette", "palette", "width", "Command palette"),
         ("layout.menu", "menu", "width", "Menus"),
         ("layout.dialog", "dialog", "width", "Workbench dialog (trust)"),
         ("layout.toast", "toast", "width", "Workbench notification toast"),
         ("layout.ide-sidebar", "side-bar", "width", "IDE primary sidebar"),
         ("layout.ide-agent-pane", "agent-pane", "width", "IDE agent pane"),
         ("layout.ide-titlebar-height", "titlebar", "height", "IDE title bar"),
         ("layout.ide-statusbar-height", "status-bar", "height", "IDE status bar")]
for path, part, prop, use in SIZES:
    shot, v = dim_of(part, prop)
    if v:
        put(CORE, tuple(path.split(".")), tok(px("%gpx" % round(float(v[:-2]))), "dimension", "Measured",
            f"computed {prop} of {part} in {shot}, dark, {DATE} ({use}); {v} before rounding"))
WINDOW = C["dark"]["home-default"]["viewport"]
put(CORE, ("layout", "window-width"), tok(f"{WINDOW['css'][0]}px", "dimension", "Measured",
    f"window {WINDOW['css'][0]} x {WINDOW['css'][1]} pt (CSS px, devicePixelRatio {WINDOW['dpr']}), the size the owner's window was in, {DATE}"))
put(CORE, ("layout", "window-height"), tok(f"{WINDOW['css'][1]}px", "dimension", "Measured", f"window height, {DATE}"))
side = computed("dark").get("--sidebar-width")
put(CORE, ("layout", "header-height"), tok("44px", "dimension", "Measured",
    f"h-[var(--window-header-height,44px)] on the page headers ({UT.get('h-[var(--window-header-height,44px)]', {}).get('used', 0)} elements), {DATE}"))

Z = [("popup", "menu"), ("tooltip", "tooltip"), ("palette", "palette")]
for key, part in Z:
    shot, s = style("dark", part)
    if s and s["z-index"] not in ("auto", ""):
        put(CORE, ("zIndex", key), tok(int(s["z-index"]), "number", "Measured", f"computed z-index of {part} in {shot}, {DATE}"))
for cls in sorted(c for c in UT if re.fullmatch(r"z-(\d+|\[\d+\])", c)):
    v = UT[cls]["props"].get("z-index")
    if v:
        put(CORE, ("zIndex", cls[2:].strip("[]")), tok(int(v), "number", "Measured", usrc(cls)))

put(CORE, ("borderWidth", "hairline"), tok("1px", "dimension", "Measured",
    f"border-top-width of the composer, settings cards, menus and selects (computed {style('dark', 'composer')[1]['border-top-width']}), {DATE}"))
put(CORE, ("borderWidth", "focus"), tok("{focusRing.width}", "dimension", "Derived", "the focus ring is an outline of focusRing.width"))
for cls in ("backdrop-blur-sm", "backdrop-blur"):
    if cls in UT:
        b = re.search(r"blur\(([\d.]+px)\)", UT[cls]["props"].get("--tw-backdrop-blur", ""))
        if b:
            put(CORE, ("blur", cls.replace("backdrop-blur", "backdrop").replace("[8px]", "8").strip("-") or "backdrop"),
                tok(b.group(1), "dimension", "Measured", usrc(cls)))

# ---------------------------------------------------------------- roles and components, per theme

ROLE = {
    "page": ("{bg.page}", "the Agents view's page and sidebar, the IDE editor"),
    "surface": ("{bg.wash}", "the IDE's title, side and status bars; a step off the page"),
    "raised": ("{bg.elevated}", "the composer, settings cards, the palette"),
    "overlay": ("{bg.elevated-wax}", "menus and popovers (the elevated fill at 94%)"),
    "scrim": ("{bg.scrim}", "behind dialogs"),
    "text.primary": ("{text.primary}", ""), "text.secondary": ("{text.secondary}", ""),
    "text.tertiary": ("{text.tertiary}", ""), "text.disabled": ("{text.disabled}", ""),
    "text.on-accent": ("{text.always-white}", "white on the accent blue (the workbench's primary button)"),
    "text.link": ("{text.link}", ""),
    "border.default": ("{border.primary}", "composer, menus, cards"), "border.subtle": ("{border.secondary}", "settings cards, selects, rows"),
    "border.strong": ("{border.primary-strong}", ""), "border.focus": ("{border.accent-primary}", "the focus ring"),
    "accent.default": ("{bg.accent-primary}", ""), "accent.hover": ("{ide.button-hoverBackground}", "Devin has no hover tier of its own; the workbench's primary button darkens to this"),
    "accent.pressed": ("{ide.button-hoverBackground}", "no pressed tier; the hover fill is kept"),
    "accent.subtle": ("{bg.accent-secondary}", ""), "accent.text": ("{text.accent-primary}", ""),
    "inverse.bg": ("{bg.accent-neutral}", "the ink-filled page buttons (Create automation, Add wiki)"),
    "inverse.text": ("{text.primary-inverse}", ""),
    "brand": ("{hue.orange}", "Devin's persona mark is drawn in the orange hue (data-slot=devin-persona, text-orange)"),
    "status.success.fill": ("{text.green}", ""), "status.success.subtle": ("{bg.green}", ""), "status.success.text": ("{text.green}", ""),
    "status.success.border": ("{text.green}", "no border tier; the hue itself"),
    "status.warning.fill": ("{text.orange}", "warnings use the orange hue (the Restricted Mode banner)"), "status.warning.subtle": ("{bg.orange}", ""),
    "status.warning.text": ("{text.orange}", ""), "status.warning.border": ("{text.orange}", "no border tier; the hue itself"),
    "status.danger.fill": ("{bg.destructive}", ""), "status.danger.subtle": ("{bg.red}", ""), "status.danger.text": ("{text.destructive}", ""),
    "status.danger.border": ("{text.red}", "no border tier; the hue itself"),
    "status.info.fill": ("{text.blue}", "no info status; the blue hue"), "status.info.subtle": ("{bg.blue}", ""), "status.info.text": ("{text.blue}", ""),
    "status.info.border": ("{text.blue}", "no border tier; the hue itself"),
}

# component tokens: (name, part, {key: css property}); value aliased when it equals a token
COMPONENTS = [
    ("button-primary", "button-primary", {"bg": "background-color", "text": "color", "radius": "border-top-left-radius", "height": "height", "padding": "padding-right"}),
    ("button-inverse", "button-primary-inverse", {"bg": "background-color", "text": "color", "radius": "border-top-left-radius", "height": "height", "padding": "padding-right"}),
    ("button-inverse-sm", "button-inverse-sm", {"bg": "background-color", "text": "color", "radius": "border-top-left-radius", "height": "height"}),
    ("button-secondary", "button-secondary", {"bg": "background-color", "border": "border-top-color", "text": "color", "radius": "border-top-left-radius", "height": "height"}),
    ("button-outline", "button-outline", {"border": "border-top-color", "text": "color", "radius": "border-top-left-radius", "height": "height"}),
    ("button-danger", "button-danger-outline", {"border": "border-top-color", "text": "color", "radius": "border-top-left-radius"}),
    ("icon-button", "icon-button", {"text": "color", "radius": "border-top-left-radius", "size": "height"}),
    ("send-button", "send-button", {"bg": "background-color", "text": "color", "radius": "border-top-left-radius", "size": "height"}),
    ("segmented", "segmented", {"bg": "background-color", "radius": "border-top-left-radius"}),
    ("segment", "segment", {"text": "color", "radius": "border-top-left-radius", "height": "height"}),
    ("segment-selected", "segment-selected", {"bg": "background-color", "border": "border-top-color", "text": "color"}),
    ("composer", "composer", {"bg": "background-color", "border": "border-top-color", "radius": "border-top-left-radius"}),
    ("menu", "menu", {"bg": "background-color", "text": "color", "radius": "border-top-left-radius", "outline": "outline-color", "shadow": "box-shadow"}),
    ("menu-row", "menu-row", {"text": "color", "radius": "border-top-left-radius", "height": "height", "padding": "padding-left"}),
    ("palette", "palette", {"bg": "background-color", "border": "border-top-color", "radius": "border-top-left-radius"}),
    ("palette-row-selected", "palette-row-selected", {"bg": "background-color", "text": "color", "radius": "border-top-left-radius"}),
    ("tooltip", "tooltip", {"bg": "background-color", "text": "color", "border": "border-top-color", "radius": "border-top-left-radius", "shadow": "box-shadow"}),
    ("diff-added", "diff-line-added", {"layer": "background-image"}),
    ("diff-removed", "diff-line-removed", {"layer": "background-image"}),
    ("dialog", "dialog", {"bg": "background-color", "text": "color", "border": "border-top-color", "radius": "border-top-left-radius"}),
    ("toast", "toast", {"bg": "background-color", "text": "color", "radius": "border-top-left-radius"}),
    ("select", "select", {"border": "border-top-color", "text": "color", "radius": "border-top-left-radius", "height": "height"}),
    ("text-field", "settings-search", {"bg": "background-color", "border": "border-top-color", "text": "color", "radius": "border-top-left-radius", "height": "height"}),
    ("switch-on", "switch-on", {"bg": "background-color", "radius": "border-top-left-radius"}),
    ("switch-off", "switch-off", {"bg": "background-color"}),
    ("checkbox", "checkbox", {"bg": "background-color", "border": "border-top-color", "radius": "border-top-left-radius"}),
    ("settings-card", "settings-card", {"bg": "background-color", "border": "border-top-color", "radius": "border-top-left-radius"}),
    ("card", "card", {"bg": "background-color", "border": "border-top-color", "radius": "border-top-left-radius"}),
    ("banner-warning", "banner-warning", {"bg": "background-color", "text": "color", "radius": "border-top-left-radius"}),
    ("banner-info", "banner-info", {"bg": "background-color", "border": "border-top-color", "radius": "border-top-left-radius"}),
    ("sidebar-row", "sidebar-row", {"text": "color", "radius": "border-top-left-radius", "height": "height"}),
    ("sidebar-row-selected", "sidebar-row-selected", {"bg": "background-color", "text": "color"}),
    ("filter-chip-selected", "filter-chip-selected", {"bg": "background-color", "border": "border-top-color", "text": "color"}),
    ("badge-merged", "badge-merged", {"bg": "background-color", "text": "color", "radius": "border-top-left-radius"}),
    ("inline-code", "inline-code", {"bg": "background-color", "radius": "border-top-left-radius"}),
    ("link", "link", {"text": "color"}),
    ("kbd", "kbd", {"text": "color"}),
]
STATES = [("hover", "bg-hover", "background-color"), ("hover", "layer-hover", "background-image"), ("hover", "text-hover", "color"),
          ("pressed", "bg-pressed", "background-color"), ("pressed", "layer-pressed", "background-image"),
          ("focus-visible", "outline-focus", "outline-color")]
CORE_NAMES = re.compile(r"^(text|bg|border|tint)\.(primary|secondary|tertiary|disabled|page|wash|elevated|elevated-wax|accent-primary|accent-neutral|link|primary-inverse|always-white)$")
PREFER = ["role", "text", "bg", "border", "tint", "hue", "shadow-color", "ide"]


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


def visible_layers(layers):
    """Tailwind paints its ring and ring-offset layers (transparent, zero size) before the shadow; drop them."""
    return [l for l in layers if l["color"] != "rgba(0, 0, 0, 0)"]


def gradient_layers(v):
    """The colours of a background-image made only of flat linear-gradient(c, c) layers, top first; [] otherwise."""
    if not v or v == "none":
        return []
    layers = re.findall(r"linear-gradient\((rgba?\([^)]*\)), (rgba?\([^)]*\))\)", v)
    if not layers or any(a != b for a, b in layers) or len(layers) != v.count("linear-gradient("):
        return []
    return [a for a, _ in layers]


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
        if prop == "box-shadow":
            layers = visible_layers(shadow(raw))
            hit = next((k for k, tk in sorted(SETS[t].get("shadow", {}).items()) if isinstance(tk, dict) and "$value" in tk
                        and visible_layers(tk["$value"]) == layers), None)
            if hit:
                return tok("{shadow.%s}" % hit, "shadow", "Measured", src)
            return tok(layers, "shadow", "Measured", src)
        if prop == "background-image":
            # The top layer of a stack of flat linear-gradient() washes (Tailwind's hover and diff tints).
            raw = gradient_layers(raw)[0]
            prop = "background-color"
            src += " (top flat gradient layer)"
        if prop in ("background-color", "color", "border-top-color", "outline-color"):
            v = color(raw)
            measured_n += 1
            if v in idx:
                aliased_n += 1
                pre = {"background-color": ("bg.", "tint."), "color": ("text.",), "border-top-color": ("border.",), "outline-color": ("border.", "text.")}[prop]
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
            if prop == "background-image" and not gradient_layers(raw):
                continue
            if prop == "box-shadow" and not visible_layers(shadow(raw) if raw != "none" else []):
                continue
            if prop in ("background-color", "border-top-color", "outline-color") and color(raw) == "rgba(0, 0, 0, 0)":
                continue
            if prop == "border-top-color" and s.get("border-top-width") == "0px":
                continue
            if prop == "outline-color" and s.get("outline-style") in ("none", ""):
                continue
            put(tree, ("component", name, key), value_for(part, shot, prop, raw))
        for state, key, prop in STATES:
            sh, ss = style(t, part, state)
            if prop == "background-image" and not (ss and gradient_layers(ss[prop])):
                continue
            painted = gradient_layers(ss[prop])[0] if ss and prop == "background-image" else (ss or {}).get(prop)
            if ss and ss[prop] != s[prop] and color(painted) != "rgba(0, 0, 0, 0)" and not (prop == "outline-color" and ss.get("outline-style") == "none"):
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
                       and s["box-shadow"] != "none" and visible_layers(shadow(s["box-shadow"])) == visible_layers(tokn["$value"])})
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
    """A name present in only one theme's reading is not a theme token: move it out."""
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
                {"name": n, "value": v["$value"], "why": f"read only while capturing {t}; not in the other theme's readings"})


reconcile()
check()
tokens = {
    "core": CORE, "light": SETS["light"], "dark": SETS["dark"],
    "$themes": [
        {"id": "light", "name": "Light", "selectedTokenSets": {"core": "source", "light": "enabled"},
         "$description": "Settings > Preferences > Theme: Light (.devin-app-root.light; the workbench's Devin Light theme)"},
        {"id": "dark", "name": "Dark", "selectedTokenSets": {"core": "source", "dark": "enabled"},
         "$description": "Settings > Preferences > Theme: Dark (.devin-app-root.dark; Devin Dark); System follows macOS"},
    ],
    "$metadata": {"tokenSetOrder": ["core", "light", "dark"]},
}
(PKG / "tokens.json").write_text(json.dumps(tokens, indent=2, ensure_ascii=False) + "\n")


def count(d):
    return sum(1 for _ in tokens_of(d))


print({k: count(tokens[k]) for k in ("core", "light", "dark")}, "component values aliased:",
      {t: SETS[t]["$extensions"]["componentValues"] for t in THEMES})
