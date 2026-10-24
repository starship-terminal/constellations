#!/usr/bin/env python3
"""Build tokens.json (W3C DTCG, Tokens Studio multi-set layout) from the raw readings.

    python3 tools/build_tokens.py

Sources, read live from Orca 1.4.237 for macOS on 2026-10-25 over the remote-debugging port
(tools/capture/electron/):
  raw/css-vars.<theme>.json      every custom property the window's stylesheets declare (Tailwind's
                                 --tw-* utility plumbing left out), by sheet, selector and condition,
                                 and each name as it computes and paints on <body>
  raw/components.<theme>.json    computed styles of the captured parts, per shot and state (shots.mjs)

How Orca's colours work, and so how this file is laid out. Orca is built with Tailwind CSS 4 and
shadcn/ui on its neutral base. Tailwind's palette (--color-<hue>-<step>, declared as hex with a
display-p3 and a lab copy under @supports) is the same in both themes and goes to core as color.*.
The theme is shadcn's: about thirty hex values on :root (light) and .dark (background, foreground,
card, popover, primary, secondary, muted, accent, destructive, border, input, ring, the two sidebars)
plus Orca's own groups (chat, status, agent, git, diff, terminal pane titles). Many of Orca's names
are a var() of another name or of a palette step (--agent-working: var(--color-yellow-500)), and the
chat colours are color-mix() of the foreground into the canvas at a per-theme percentage. So each
semantic set holds the declared hex values as values and the rest as aliases, or as the painted
value with the formula beside it. role.* maps the checklist roles onto those tokens, and
component.* holds measured component values, aliased to a token whenever the painted value matches.

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

SHEET = "client-"                       # the app stylesheet (client-<hash>.css)
THEME_SELECTOR = {"light": ":root", "dark": ".dark"}
THEME_NAME = {"light": "Light (html.light, System theme with prefers-color-scheme: light)",
              "dark": "Dark (html.dark, System theme with prefers-color-scheme: dark)"}
# name prefix -> token group; names without one go to `base` (shadcn's own names).
GROUPS = [("--color-", None), ("--worktree-sidebar-", "worktreeSidebar"), ("--worktree-sidebar", "worktreeSidebar"),
          ("--sidebar-", "sidebar"), ("--sidebar", "sidebar"), ("--chat-", "chat"), ("--status-", "status"),
          ("--agent-", "agent"), ("--workspace-status-", "workspaceStatus"), ("--chart-", "chart"), ("--callout-", "callout"),
          ("--git-decoration-", "git"), ("--git-graph-", "gitGraph"), ("--diff-", "diff"),
          ("--terminal-pane-title-", "terminalPaneTitle"), ("--orca-pane-title-", "paneTitle"), ("--terminal-", "terminal"),
          ("--orca-security-", "security"), ("--jira-priority-", "jiraPriority"), ("--markdown-", "markdown"),
          ("--tab-group-", "tabGroup"), ("--", "base")]
SKIP = re.compile(r"^--(tw-|lightningcss|m-|mp-|epr-|feature-|linear-|toast|normal|contextual|lift|divider|pdf|vscode|"
                  r"app-|font-|default-|text-|leading-|tracking-|radius|spacing|container|blur|ease|animate|shadow|drop-shadow|"
                  r"mac-|window-|workspace-sidebar|ui-zoom|orca-terminal-link|chat-.*-mix$|chat-content|chat-.*-base$|"
                  r"orca-pane-title-height|annotation|jira|editor-surface$)")
KEEP_ALSO = {"--annotation-highlight", "--editor-surface"}


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
    if t == "dark" and not any(d["selector"].split(",")[0].strip() == ".dark" or ".dark" in [s.strip() for s in d["selector"].split(",")] for d in own):
        own += [d for d in out if d["selector"].split(",")[0].strip() == ":root"]
    if t == "light":
        own = [d for d in own if d["selector"].split(",")[0].strip() in (":root", ":root:not(.dark)")]
    return own


def formula(t, name):
    ds = decls(t, name)
    applied = [d for d in ds if d["condition"] and "color-mix" in d["condition"]]
    return (applied or [d for d in ds if not d["condition"]] or ds or [{"value": None}])[0]["value"]


def path_of(name):
    for pre, group in GROUPS:
        if name.startswith(pre):
            rest = name[len(pre):]
            if group is None:          # --color-red-500 -> core color.red.500
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
    if not n.startswith("--color-") or n in ("--color-background",):
        continue
    if V["dark"]["colors"].get(n) != V["light"]["colors"].get(n):
        raise ValueError(f"{n} differs by theme")
    if not is_color(V["dark"]["colors"].get(n, "")):
        continue
    hexes = [d["value"] for d in V["dark"]["decls"] if d["name"] == n and d["value"].startswith("#")]
    put(CORE, path_of(n), tok(color(V["dark"]["colors"][n]), "color", "Measured",
        f"{n} as painted (Tailwind's palette; both themes), {DATE}", declared=hexes[0] if hexes else None))


def core_dim(group, key, name, conv=rem, ty="dimension", **ext):
    v = dark_comp[name]
    if light_comp.get(name) != v:
        raise ValueError(f"{name} differs by theme")
    put(CORE, (group, key), tok(conv(v), ty, "Measured", f"{name} on <body>, both themes, {DATE}", css=v, **ext))


# radius: --radius and Tailwind's steps derived from it; lg is --radius itself (radius-lg: var(--radius))
core_dim("radius", "xs", "--radius-xs")
core_dim("radius", "sm", "--radius-sm")
core_dim("radius", "md", "--radius-md")
core_dim("radius", "lg", "--radius")
core_dim("radius", "xl", "--radius-xl")
put(CORE, ("radius", "full"), tok("9999px", "dimension", "Measured", f"rounded-full on switches, badges and the send button (computed 9999px or 50%), {DATE}"))
# spacing: Tailwind's one step; every p-*, gap-* and m-* class is a multiple of it
core_dim("spacing", "unit", "--spacing")
for n in (0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 5, 6, 8, 10, 12, 16):
    put(CORE, ("spacing", ("%g" % n).replace(".", "-")), tok(px("%gpx" % (4 * n)), "dimension", "Derived",
        f"calc(var(--spacing) * {n:g}), Tailwind's spacing class {n:g}", formula=f"calc(var(--spacing) * {n:g})"))
# type
for key in ("3xs", "2xs", "xs", "sm", "base", "lg", "xl", "2xl", "3xl", "4xl", "chat-code"):
    core_dim("fontSize", key, f"--text-{key}")
    lh = dark_comp[f"--text-{key}--line-height"]
    m = re.fullmatch(r"calc\(\s*([\d.]+)\s*/\s*([\d.]+)\s*\)", lh)
    put(CORE, ("lineHeight", key), tok(px("%gpx" % (float(m.group(1)) * 16)), "dimension", "Measured",
        f"--text-{key}--line-height on <body> ({lh}, a ratio to the size), {DATE}", css=lh))
for key in ("light", "normal", "medium", "semibold", "bold"):
    core_dim("fontWeight", key, f"--font-weight-{key}", conv=int, ty="fontWeight")
for key in ("tight", "snug", "normal", "relaxed"):
    core_dim("leading", key, f"--leading-{key}", conv=float, ty="number")
for key in ("tight", "normal", "wide", "wider"):
    core_dim("letterSpacing", key, f"--tracking-{key}", conv=lambda v: v.replace("-.", "-0.").replace("+.", "0.") if v.startswith("-") else (("0" + v) if v.startswith(".") else v))
for key, n in (("sans", "--font-sans"), ("mono", "--font-mono")):
    stack = [f.strip().strip("'\"") for f in dark_comp[n].split(",")]
    put(CORE, ("fontFamily", key), tok(stack, "fontFamily", "Measured", f"{n} on <body> ({'from --app-font-family, the owner' + chr(39) + 's IDE Font setting Geist' if key == 'sans' else 'the stylesheet'}), {DATE}"))
# motion
put(CORE, ("duration", "default"), tok(ms(dark_comp["--default-transition-duration"]), "duration", "Measured", f"--default-transition-duration on <body>, {DATE}"))
for key, n in (("default", "--default-transition-timing-function"), ("in-out", "--ease-in-out"), ("out", "--ease-out")):
    put(CORE, ("easing", key), tok(bezier(dark_comp[n]), "cubicBezier", "Measured", f"{n} on <body>, {DATE}", css=dark_comp[n]))
for key in ("sm", "md", "xl", "2xl"):
    core_dim("blur", key, f"--blur-{key}")
for key in ("xs", "sm", "md", "lg", "xl", "2xl", "3xl", "4xl", "5xl", "6xl"):
    core_dim("container", key, f"--container-{key}")
core_dim("layout", "chat-content", "--chat-content-max-width")
core_dim("layout", "pane-title-height", "--orca-pane-title-height")
put(CORE, ("shadow", "floating"), tok(shadow(V["dark"]["shadows"]["--shadow-floating"]), "shadow", "Measured",
    f"--shadow-floating as painted, both themes, {DATE}", css=dark_comp["--shadow-floating"]))
put(CORE, ("shadow", "drop-sm"), tok(shadow(V["dark"]["shadows"]["--drop-shadow-sm"]), "shadow", "Measured",
    f"--drop-shadow-sm as painted (a filter drop shadow), both themes, {DATE}", css=dark_comp["--drop-shadow-sm"]))

# ---------------------------------------------------------------- semantic sets


def semantic(t):
    tree, comp, painted = {}, computed(t), V[t]["colors"]
    names = sorted(n for n in comp if (not SKIP.match(n) or n in KEEP_ALSO) and not n.startswith("--color-"))
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
        elif f and re.fullmatch(r"#[0-9a-fA-F]{3,8}", f):
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
ROLES = [("display", "page-title", "Settings page titles (h1)"),
         ("heading", "card-title", "Settings group titles"),
         ("body", "field-label", "Settings row labels, menu items, list text"),
         ("body-secondary", "page-description", "Page descriptions and row descriptions (muted-foreground)"),
         ("label", "button-outline", "Button labels"),
         ("caption", "workspace-badge", "Badges (the primary badge on a workspace)"),
         ("small", "status-chip", "Status bar chips and shortcut hints"),
         ("prompt", "composer-editor", "Text typed in the chat composer"),
         ("message", "assistant-message", "Agent replies in the chat")]
for role, part, use in ROLES:
    shot, s = style("dark", part)
    if not s:
        continue
    fam = "{fontFamily.mono}" if role in ("code", "terminal") else "{fontFamily.sans}"
    lh = s["line-height"]
    val = {"fontFamily": fam, "fontSize": px(s["font-size"]), "fontWeight": int(s["font-weight"]),
           "lineHeight": px(lh) if lh.endswith("px") else "normal",
           "letterSpacing": px(s["letter-spacing"]) if s["letter-spacing"].endswith("px") else "0px"}
    note = None
    if val["lineHeight"] == "normal":
        val["lineHeight"] = px("%gpx" % round(float(s["font-size"][:-2]) * 1.2, 1))
        note = "computed line-height is normal; 1.2 x the size is used here"
    put(CORE, ("typography", role), tok(val, "typography", "Measured", f"computed style of {part} in {shot}, dark, {DATE}; {use}", note=note))


put(CORE, ("typography", "code"), tok({"fontFamily": "{fontFamily.mono}", "fontSize": "{fontSize.chat-code}", "fontWeight": 400,
    "lineHeight": "{lineHeight.chat-code}", "letterSpacing": "0px"}, "typography", "Derived",
    f"the chat code block's text-chat-code class: --text-chat-code (12px) and its line height on <pre data-native-chat-code-content>, {DATE}"))
put(CORE, ("typography", "terminal"), tok({"fontFamily": "{fontFamily.mono}", "fontSize": "14px", "fontWeight": 500, "lineHeight": "14px",
    "letterSpacing": "0px"}, "typography", "Measured",
    f"the owner's terminal settings as Orca stores them (terminalFontFamily SF Mono, terminalFontSize 14, terminalFontWeight 500, terminalLineHeight 1); xterm draws the terminal itself, so no computed style holds them, {DATE}"))


def dim_of(part, prop, state="default", t="dark"):
    shot, s = style(t, part, state)
    return (shot, s[prop]) if s and s.get(prop, "").endswith("px") else (None, None)


SIZES = [("controlHeight.default", "select", "height", "Selects, inputs and default buttons (h-9)"),
         ("controlHeight.sm", "button-ghost", "height", "Small buttons (h-8)"),
         ("controlHeight.xs", "button-xs", "height", "Extra-small buttons (h-7)"),
         ("controlHeight.input", "settings-search", "height", "Text inputs"),
         ("size.control.icon-button", "icon-button", "height", "Sidebar icon buttons"),
         ("size.control.send", "send-button", "height", "The chat send button"),
         ("size.control.tab", "tab", "height", "Workspace tabs"),
         ("size.control.nav-row", "nav-row", "height", "Sidebar navigation rows"),
         ("size.control.settings-nav", "settings-nav", "height", "Settings navigation rows"),
         ("size.control.menu-item", "menu-item", "height", "Menu items"),
         ("size.control.switch-width", "switch-on", "width", "Switch"),
         ("size.control.switch-height", "switch-on", "height", "Switch"),
         ("size.control.toggle-item", "toggle-item", "height", "Segmented toggle items"),
         ("size.control.badge", "workspace-badge", "height", "Badges"),
         ("layout.sidebar", "sidebar", "width", "Left sidebar (the owner's 280px)"),
         ("layout.composer", "composer", "width", "Chat composer"),
         ("layout.settings-card", "card", "width", "Settings content column"),
         ("layout.dialog", "dialog", "width", "Add Quick Command dialog"),
         ("layout.confirm-dialog", "confirm-dialog", "width", "Remove Project confirmation"),
         ("layout.palette", "palette", "width", "Search palette"),
         ("layout.menu", "menu", "width", "Menus"),
         ("layout.status-bar-height", "status-bar", "height", "Status bar"),
         ("layout.toast", "toast", "width", "Update card")]
for path, part, prop, use in SIZES:
    shot, v = dim_of(part, prop)
    if v:
        put(CORE, tuple(path.split(".")), tok(px("%gpx" % round(float(v[:-2]))), "dimension", "Measured",
            f"computed {prop} of {part} in {shot}, dark, {DATE} ({use}); {v} before rounding"))
WINDOW = C["dark"]["chat-empty"]["viewport"]
put(CORE, ("layout", "window-width"), tok(f"{WINDOW['css'][0]}px", "dimension", "Measured",
    f"the window's viewport, {WINDOW['css'][0]} x {WINDOW['css'][1]} CSS px at devicePixelRatio {WINDOW['dpr']} (UI Zoom 100%), {DATE}"))
put(CORE, ("layout", "window-height"), tok(f"{WINDOW['css'][1]}px", "dimension", "Measured", f"the window's viewport height, {DATE}"))
put(CORE, ("layout", "right-sidebar"), tok("350px", "dimension", "Measured", f"ui.rightSidebarWidth in the profile (350), and the explorer pane's width on screen, {DATE}"))
for key, part in (("overlay", "overlay"), ("dialog", "dialog"), ("menu", "menu"), ("tooltip", "tooltip"), ("toast", "toast")):
    shot, s = style("dark", part)
    if s and s["z-index"] not in ("auto", ""):
        put(CORE, ("zIndex", key), tok(int(s["z-index"]), "number", "Measured", f"computed z-index of {part} in {shot}, {DATE}"))
put(CORE, ("borderWidth", "default"), tok("1px", "dimension", "Measured", f"border-top-width of cards, inputs, dialogs and the composer, {DATE}"))
# focus ring: shadcn's focus-visible:ring-[3px] ring-ring/50 plus border-ring, read on a focused part
for part in ("button-outline", "select", "switch-off", "input"):
    shot, s = style("dark", part, "focus-visible")
    if s and s["box-shadow"] != "none":
        layers = shadow(s["box-shadow"])
        ring = max(layers, key=lambda l: float(l["spread"][:-2]))
        put(CORE, ("focusRing", "width"), tok(ring["spread"], "dimension", "Measured",
            f"spread of the focus box-shadow of {part} in {shot}, dark, {DATE} (focus-visible:ring-[3px])", css=s["box-shadow"]))
        put(CORE, ("focusRing", "offset"), tok("0px", "dimension", "Measured", f"the ring is a box-shadow drawn outside the border, no offset ({shot}), {DATE}"))
        break
put(CORE, ("borderWidth", "focus"), tok("{focusRing.width}", "dimension", "Derived", "the focus ring is a box-shadow of focusRing.width"))

cond = V["dark"]["conditions"]
rm = {k: v["rules"] for k, v in cond.items() if "reduced-motion" in k}
CORE.setdefault("duration", {})["$extensions"] = {"reducedMotion": {"rules": rm,
    "how": "Tailwind's motion-safe: and motion-reduce: variants under (prefers-reduced-motion): spinners and enter animations stop; no duration token changes"}}
bp = sorted({k for k in cond if re.search(r"width", k)})
CORE.setdefault("layout", {})["$extensions"] = {"breakpointsInCss": bp,
    "note": "Tailwind's sm 40rem, md 48rem, lg 64rem, xl 80rem, 2xl 96rem; the window is resizable and few views use them"}

# ---------------------------------------------------------------- roles and components, per theme

ROLE = {
    "page": ("{base.background}", "the workspace, chat and settings content"),
    "surface": ("{worktreeSidebar.default}", "the left sidebar"),
    "raised": ("{base.popover}", "menus, dialogs, popovers; cards use base.card"),
    "overlay": (None, "palette", "the search palette"),
    "scrim": (None, "overlay", "the dialog overlay"),
    "text.primary": ("{base.foreground}", ""), "text.secondary": ("{base.muted-foreground}", ""),
    "text.on-accent": ("{base.primary-foreground}", ""), "text.link": ("{callout.note}", "links in markdown and the release notes link use the foreground with an underline; callout.note is the blue Orca uses for notes and unread"),
    "border.default": ("{base.border}", "cards, dialogs, separators"), "border.input": ("{base.input}", "inputs, selects, outline buttons"),
    "border.focus": ("{base.ring}", "the focus border; the ring is the same colour at 50%"),
    "accent.default": ("{base.primary}", "Orca's primary is ink, not a hue: near-black in light, near-white in dark"),
    "accent.subtle": ("{base.accent}", "shadcn's accent: the hover and highlight wash"),
    "brand": ("{sidebar.primary}", "the one saturated blue in the dark theme (sidebar-primary); light keeps it ink"),
}
ROLE["status.success.fill"] = ("{status.success}", "")
ROLE["status.success.text"] = ("{status.success}", "")
ROLE["status.warning.fill"] = ("{status.warning}", "")
ROLE["status.warning.text"] = ("{status.warning}", "")
ROLE["status.danger.fill"] = ("{base.destructive}", "")
ROLE["status.danger.text"] = ("{base.destructive}", "")
ROLE["status.danger.on"] = ("{base.destructive-foreground}", "")
ROLE["status.info.fill"] = ("{callout.note}", "Orca has no info status; callout.note is its blue")
ROLE["status.info.text"] = ("{callout.note}", "")

COMPONENTS = [
    ("button-default", "button-default", {"bg": "background-color", "text": "color", "radius": "border-top-left-radius", "height": "height", "padding": "padding-right"}),
    ("button-outline", "button-outline", {"bg": "background-color", "border": "border-top-color", "text": "color", "radius": "border-top-left-radius", "height": "height", "padding": "padding-right"}),
    ("button-destructive", "button-destructive", {"bg": "background-color", "text": "color", "radius": "border-top-left-radius", "height": "height"}),
    ("button-ghost", "button-ghost", {"text": "color", "radius": "border-top-left-radius", "height": "height"}),
    ("icon-button", "icon-button", {"text": "color", "radius": "border-top-left-radius", "size": "height"}),
    ("send-button", "send-button", {"bg": "background-color", "text": "color", "radius": "border-top-left-radius", "size": "height"}),
    ("composer", "composer", {"bg": "background-color", "border": "border-top-color", "radius": "border-top-left-radius"}),
    ("menu", "menu", {"bg": "background-color", "border": "border-top-color", "text": "color", "radius": "border-top-left-radius"}),
    ("menu-item", "menu-item", {"text": "color", "radius": "border-top-left-radius", "height": "height", "padding": "padding-left"}),
    ("dialog", "dialog", {"bg": "background-color", "border": "border-top-color", "radius": "border-top-left-radius"}),
    ("palette", "palette", {"bg": "background-color", "border": "border-top-color", "radius": "border-top-left-radius"}),
    ("scrim", "overlay", {"bg": "background-color"}),
    ("tooltip", "tooltip", {"bg": "background-color", "text": "color", "radius": "border-top-left-radius"}),
    ("toast", "toast", {"bg": "background-color", "border": "border-top-color", "radius": "border-top-left-radius"}),
    ("tab", "tab", {"bg": "background-color", "text": "color", "height": "height"}),
    ("tab-active", "tab-active", {"bg": "background-color", "text": "color"}),
    ("toggle-item", "toggle-item", {"text": "color", "radius": "border-top-left-radius", "height": "height"}),
    ("toggle-item-on", "toggle-item-on", {"bg": "background-color", "text": "color"}),
    ("input", "settings-search", {"bg": "background-color", "border": "border-top-color", "text": "color", "radius": "border-top-left-radius", "height": "height"}),
    ("select", "select", {"bg": "background-color", "border": "border-top-color", "text": "color", "radius": "border-top-left-radius", "height": "height"}),
    ("switch-on", "switch-on", {"bg": "background-color", "radius": "border-top-left-radius"}),
    ("switch-off", "switch-off", {"bg": "background-color"}),
    ("badge", "workspace-badge", {"bg": "background-color", "border": "border-top-color", "text": "color", "radius": "border-top-left-radius", "height": "height"}),
    ("card", "card", {"bg": "background-color", "border": "border-top-color", "radius": "border-top-left-radius", "padding": "padding-top"}),
    ("nav-row", "nav-row", {"text": "color", "radius": "border-top-left-radius", "height": "height"}),
    ("workspace-row", "workspace-row", {"bg": "background-color", "border": "border-top-color", "radius": "border-top-left-radius"}),
    ("settings-nav", "settings-nav", {"text": "color", "radius": "border-top-left-radius", "height": "height"}),
    ("settings-nav-selected", "settings-nav-selected", {"bg": "background-color", "text": "color"}),
    ("user-message", "user-message", {"bg": "background-color", "border": "border-top-color", "text": "color", "radius": "border-top-left-radius"}),
    ("code-block", "code-block", {"bg": "background-color", "border": "border-top-color", "radius": "border-top-left-radius"}),
    ("status-bar", "status-bar", {"bg": "background-color", "border": "border-top-color", "text": "color"}),
]
STATES = [("hover", "bg-hover", "background-color"), ("hover", "text-hover", "color"), ("pressed", "bg-pressed", "background-color"),
          ("focus-visible", "border-focus", "border-top-color")]
CORE_NAMES = re.compile(r"^base\.(background|foreground|card|popover|primary|primary-foreground|secondary|muted|muted-foreground|accent|accent-foreground|border|input|ring|destructive)$")
PREFER = ["role", "base", "sidebar", "worktreeSidebar", "chat", "status", "callout", "color"]


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
                # A text colour prefers a *-foreground name, a fill or edge one that is not.
                fits = [x for x in idx[v] if ("foreground" in x) == (prop == "color") and not x.startswith("role.")]
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
            if ss and ss[prop] != s[prop] and is_color(ss[prop]) and color(ss[prop]) != "rgba(0, 0, 0, 0)":
                put(tree, ("component", name, key), value_for(part, sh, prop, ss[prop]))
        layers = visible_shadow(s["box-shadow"])
        if layers:
            put(tree, ("shadow", name), tok(layers, "shadow", "Measured",
                f"computed box-shadow of {part} in {shot}, {THEME_NAME[t]}, {DATE}, without the transparent ring placeholders Tailwind adds"))
    # Roles that are states of a component or an opacity rule rather than a declared colour.
    for key, (comp_path, why) in {"accent.hover": ("component.button-default.bg-hover", "hover:bg-primary/90 on the default button"),
                                  "accent.pressed": ("component.button-default.bg-pressed", "shadcn has no :active style; pressed paints the hover fill")}.items():
        hit = get(tree, comp_path) or get(tree, "component.button-default.bg")
        put(tree, ("role",) + tuple(key.split(".")), tok(hit["$value"], "color", "Measured", hit["$extensions"]["source"]["from"] + f"; {why}"))
    fg = resolve(t, "{base.foreground}")
    r, g, b = (int(fg[i:i + 2], 16) for i in (1, 3, 5))
    put(tree, ("role", "text", "disabled"), tok(f"rgba({r}, {g}, {b}, 0.5)", "color", "Derived",
        "base.foreground at the 50% opacity shadcn applies to disabled controls (disabled:opacity-50)", formula="disabled:opacity-50"))
    put(tree, ("role", "border", "strong"), tok("{base.input}", "color", "Derived", "the checklist role, mapped to base.input (the edge of inputs and outline buttons)"))
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
         "$description": "Settings > Appearance > Theme: System with a light OS appearance, or Light (html.light)"},
        {"id": "dark", "name": "Dark", "selectedTokenSets": {"core": "source", "dark": "enabled"},
         "$description": "Settings > Appearance > Theme: System with a dark OS appearance, or Dark (html.dark)"},
    ],
    "$metadata": {"tokenSetOrder": ["core", "light", "dark"]},
}
(PKG / "tokens.json").write_text(json.dumps(tokens, indent=2, ensure_ascii=False) + "\n")


def count(d):
    return sum(1 for _ in tokens_of(d))


print({k: count(tokens[k]) for k in ("core", "light", "dark")}, "component values aliased:",
      {t: SETS[t]["$extensions"]["componentValues"] for t in THEMES})
