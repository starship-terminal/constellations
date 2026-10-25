#!/usr/bin/env python3
"""Build tokens.json (W3C DTCG, Tokens Studio multi-set layout) from the raw readings.

    python3 tools/build_tokens.py

Sources, read live from Codex 26.1013 for macOS (Codex 2.app) on 2026-10-25 over the remote-debugging
port (tools/capture/electron/):
  raw/css-vars.<theme>.json      every custom property the window's stylesheets declare (Tailwind's
                                 --tw-* plumbing left out), by sheet, selector and condition, and each
                                 name as it computes and paints on <html>
  raw/components.<theme>.json    computed styles of the captured parts, per shot and state (shots.mjs)
  raw/theme-defaults.json        Codex's built-in default chrome theme, read from the app bundle

How Codex's colours work, and so how this file is laid out. Codex is React with Tailwind CSS 4 and
OpenAI's own component kit. A theme is four seeds that a <style data-codex-app-themes> element writes per
[data-theme] from Settings > Appearance: --codex-base-surface (the window colour), --codex-base-ink (the
text colour), --codex-base-accent and --codex-base-contrast (a number). Everything else is a formula over
those seeds and a light-dark grey ramp: the ink at fixed alphas (--alpha-*), color-mix() of the ink into
the surface, and Lightning CSS's light-dark polyfill (var(--lightningcss-light, A)var(--lightningcss-dark, B))
choosing between two primitives. The hue palettes (--blue-*, --red-*, ...) are the same in both themes and
go to core as color.*; the grey ramp (--gray-*) flips per theme and stays in each semantic set. Each
semantic set holds, per name, the painted colour, or an alias when its formula is a plain var() of another
token that paints the same. role.* maps the checklist roles onto those tokens; component.* holds measured
component values, aliased to a token whenever the painted value matches.

The owner's themes are not Codex's default: dark is the Absolutely preset (surface #2d2d2b, ink #f9f9f7,
accent #cc7d5e, contrast 50) and light the Catppuccin preset (surface #eff1f5, ink #4c4f69, accent #8839ef,
contrast 40), with the UI font set to Garamond. Codex's own default (surface #181818 / #ffffff, ink
#ffffff / #1a1c1f, accent #339cff) is kept under $extensions.codexDefault on core.seed, read from the bundle.

Every token carries $extensions.source = {evidence, from}. Deterministic: same inputs, same bytes.
"""
import ast
import json
import operator
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

THEME_NAME = {"light": "Light (Settings > Appearance > Mode: Light, the owner's Catppuccin theme)",
              "dark": "Dark (Mode: System with macOS dark, the owner's Absolutely theme)"}
# name prefix -> token group, in order; the first match wins.
GROUPS = [("--color-background-", "bg"), ("--color-text-", "text"), ("--color-border-", "border"), ("--color-ring-", "ring"),
          ("--color-codex-", "codex"), ("--color-token-", "token"), ("--app-color-", "app"), ("--color-chat-", "chat"),
          ("--color-content-", "content"), ("--color-chart-", "chart"), ("--color-surface-", "surface"), ("--color-surface", "surface"), ("--color-gray-", "neutral"),
          ("--gray-fixed-", "grayFixed"), ("--gray-", "gray"), ("--alpha-", "alpha"), ("--codex-base-", "seed"),
          ("--color-", "misc"), ("--", "kit")]
HUES = ["blue", "green", "orange", "pink", "purple", "red", "yellow"]
# Colour names left out: illustration, onboarding and media colours no screen captured here uses.
SKIP = re.compile(r"^--(tw-|lightningcss|color-(file|avatar|media|artifact|device|image|learning|slate|amber|brand|alpha|black|white|dialog|control)-?|"
                  r"startup|popcorn|daybreak|chatgpt|brand-|wb-|codeblock-syntax|toast|loading|shimmer|particle|learning|"
                  r"viewer-|dil-|oai-|vscode)")


def load(name):
    return json.loads((RAW / name).read_text())


V = {t: load(f"css-vars.{t}.json") for t in THEMES}
C = {t: load(f"components.{t}.json") for t in THEMES}
DEFAULTS = load("theme-defaults.json")

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


_OPS = {ast.Add: operator.add, ast.Sub: operator.sub, ast.Mult: operator.mul, ast.Div: operator.truediv, ast.USub: operator.neg}


def _ev(node):
    if isinstance(node, ast.Expression):
        return _ev(node.body)
    if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
        return node.value
    if isinstance(node, ast.BinOp) and type(node.op) in _OPS:
        return _OPS[type(node.op)](_ev(node.left), _ev(node.right))
    if isinstance(node, ast.UnaryOp) and type(node.op) in _OPS:
        return _OPS[type(node.op)](_ev(node.operand))
    raise ValueError("not arithmetic")


def length(v):
    """A computed CSS length (px, rem, or calc() arithmetic over them) -> px string; None if it is not one."""
    v = v.strip()
    if v in ("0", "0px"):
        return "0px"
    expr = v.replace("calc", "")
    if re.search(r"[a-df-oq-z%]", expr.replace("rem", "").replace("px", "")):
        return None
    expr = re.sub(r"(-?[\d.]+)rem", lambda m: "(%s*16)" % m.group(1), expr)
    expr = re.sub(r"(-?[\d.]+)px", r"(\1)", expr)
    expr = re.sub(r"(?<![\d.])\.(\d)", r"0.\1", expr)
    try:
        return px("%gpx" % round(_ev(ast.parse(expr, mode="eval")), 3))
    except (ValueError, SyntaxError, ZeroDivisionError):
        return None


def em(v):
    v = v.strip()
    m = re.fullmatch(r"(-?)\.(\d+)(em|px|rem)", v)
    if m:
        v = f"{m.group(1)}0.{m.group(2)}{m.group(3)}"
    if v.endswith("rem"):
        return length(v)
    return v if re.fullmatch(r"-?\d*\.?\d+(em|px)", v) else None


def branch(value, t):
    """Lightning CSS writes light-dark() as var(--lightningcss-light,A)var(--lightningcss-dark,B); keep this theme's side."""
    m = re.match(r"^var\(--lightningcss-light,", value or "")
    if not m:
        return value
    depth, i, parts, start = 0, 0, [], None
    while i < len(value):
        ch = value[i]
        if value.startswith("var(--lightningcss-", i) and depth == 0:
            start = value.index(",", i) + 1
        if ch == "(":
            depth += 1
        elif ch == ")":
            depth -= 1
            if depth == 0 and start is not None:
                parts.append(value[start:i]); start = None
        i += 1
    return parts[0 if t == "light" else 1] if len(parts) == 2 else value


def applies(d, t):
    """A declaration that applies to the Electron window in theme t (not the extension, browser or other theme's rules)."""
    sel = d["selector"]
    if re.search(r'window-type="(extension|browser|chrome-extension)"\]', sel) and "not([data-codex-window-type" not in sel:
        return False
    if 'data-theme="%s"' % ("dark" if t == "light" else "light") in sel and 'data-theme="%s"' % t not in sel:
        return False
    if d["condition"] and not re.search(r"color-mix|@layer|supports|^$", d["condition"]):
        return False
    return True


def formula(t, name):
    """The declaration of `name` that wins on <html> in theme t: of the declarations that apply to the Electron
    window, the one whose value (this theme's branch) paints the captured colour; failing that, a theme-named
    rule, then the last declaration in sheet order, which is the one the cascade keeps among equal selectors."""
    ds = [d for d in V[t]["decls"] if d["name"] == name and applies(d, t)]
    if not ds:
        return None
    painted = V[t]["colors"].get(name)
    if painted and is_color(painted):
        want = color(painted)
        for d in reversed(ds):
            v = (branch(d["value"], t) or "").strip()
            m = re.fullmatch(r"var\((--[\w-]+)(?:,[^()]*)?\)", v)
            ref = V[t]["colors"].get(m.group(1)) if m else (v if is_color(v) else None)
            if ref and is_color(ref) and color(ref) == want:
                return v
    own = [d for d in ds if 'data-theme="%s"' % t in d["selector"]]
    return branch((own or ds)[-1]["value"], t)


def path_of(name):
    for pre, group in GROUPS:
        if name.startswith(pre):
            rest = name[len(pre):] or "default"
            return (group, rest)
    raise KeyError(name)


def where(t, name, extra=""):
    return f"{name} as painted on <html>, {THEME_NAME[t]}, {DATE}{extra}"


# ---------------------------------------------------------------- core: the hue palettes and the scales

CORE = {}
dark_comp, light_comp = computed("dark"), computed("light")
for n in sorted(dark_comp):
    m = re.fullmatch(r"--(%s)-(a?\d+)" % "|".join(HUES), n)
    if not m or not is_color(V["dark"]["colors"].get(n, "")):
        continue
    if color(V["dark"]["colors"][n]) != color(V["light"]["colors"].get(n, "")):
        continue                       # a hue step that flips per theme stays in the semantic sets
    hexes = [d["value"] for d in V["dark"]["decls"] if d["name"] == n and d["value"].startswith("#")]
    put(CORE, ("color", m.group(1), m.group(2)), tok(color(V["dark"]["colors"][n]), "color", "Measured",
        f"{n} as painted (the same in both themes), {DATE}", declared=hexes[0] if hexes else None))


def core_dim(group, key, name, conv=length, ty="dimension", **ext):
    v = dark_comp[name]
    if light_comp.get(name) != v:
        raise ValueError(f"{name} differs by theme")
    out = conv(v)
    if out is None:
        raise ValueError(f"{name}: {v!r}")
    put(CORE, (group,) + (key if isinstance(key, tuple) else (key,)), tok(out, ty, "Measured", f"{name} on <html>, both themes, {DATE}", css=v, **ext))


# The theme seeds, and Codex's own default theme from the bundle.
put(CORE, ("seed", "contrast", "dark"), tok(int(dark_comp["--codex-base-contrast"]), "number", "Measured",
    f"--codex-base-contrast on <html>, {THEME_NAME['dark']}, {DATE} (Settings > Appearance > Advanced > Contrast)"))
put(CORE, ("seed", "contrast", "light"), tok(int(light_comp["--codex-base-contrast"]), "number", "Measured",
    f"--codex-base-contrast on <html>, {THEME_NAME['light']}, {DATE}"))
CORE["seed"]["$extensions"] = {"codexDefault": {"source": {"evidence": "Measured", "from": DEFAULTS["from"] + ", " + DEFAULTS["read"]},
    "value": DEFAULTS["source"], "note": DEFAULTS["note"]}}
put(CORE, ("cornerScale",), tok(float(dark_comp["--corner-radius-scale"]), "number", "Measured",
    f"--corner-radius-scale on <html> ({DATE}): every radius is its -base value times this; 1.25 is Codex's default"))
for key in ("2xs", "xs", "sm", "md", "lg", "xl", "2xl", "3xl", "4xl", "full"):
    core_dim("radius", key, f"--radius-{key}")
for key, n in (("menu", "--menu-radius"), ("menu-item", "--menu-item-radius"), ("dialog", "--dialog-radius"), ("popover", "--popover-radius"),
               ("tooltip", "--tooltip-border-radius"), ("row", "--radius-token-row"), ("composer-single-line", "--radius-token-composer-single-line"),
               ("form-dialog", "--radius-form-dialog"), ("unread-badge", "--radius-unread-badge")):
    core_dim("radius", key, n)
put(CORE, ("radius", "$extensions"), {"cornerShape": dark_comp["--codex-corner-shape"],
    "note": "Codex draws corners with Chromium's corner-shape: superellipse(1.5) (a squircle) where the window supports it, so a radius renders softer than a circular one of the same size"})
core_dim("spacing", "unit", "--spacing")
for n in (0.5, 1, 1.5, 2, 2.5, 3, 4, 5, 6, 8, 10, 12):
    put(CORE, ("spacing", ("%g" % n).replace(".", "-")), tok(px("%gpx" % (4 * n)), "dimension", "Derived",
        f"calc(var(--spacing) * {n:g}), Tailwind's spacing class {n:g}", formula=f"calc(var(--spacing) * {n:g})"))
for n in sorted(k for k in dark_comp if k.startswith("--spacing-") and length(dark_comp[k])):
    core_dim("spacing", n[len("--spacing-"):], n)
# Type: Codex's kit declares each text and heading style as size, line height, tracking and weight.
for kind in ("text", "heading"):
    for key in sorted({re.match(rf"--font-{kind}-([\w]+)-size$", n).group(1) for n in dark_comp if re.match(rf"--font-{kind}-[\w]+-size$", n)}):
        b = f"--font-{kind}-{key}"
        for prop, grp, conv, ty in (("size", "fontSize", length, "dimension"), ("line-height", "lineHeight", length, "dimension"),
                                    ("tracking", "letterSpacing", em, "dimension")):
            core_dim(grp, f"{kind}-{key}", f"{b}-{prop}", conv=conv, ty=ty)
        put(CORE, ("typography", f"{kind}-{key}"), tok({"fontFamily": "{fontFamily.sans}", "fontSize": "{fontSize.%s-%s}" % (kind, key),
            "fontWeight": int(dark_comp[f"{b}-weight"]), "lineHeight": "{lineHeight.%s-%s}" % (kind, key),
            "letterSpacing": "{letterSpacing.%s-%s}" % (kind, key)}, "typography", "Measured",
            f"{b}-size, -line-height, -tracking and -weight on <html>, both themes, {DATE}"))
for key in ("xs", "sm", "base", "lg", "xl", "2xl", "3xl", "4xl"):
    core_dim("fontSize", key, f"--text-{key}", note="Tailwind's text-* size as Codex sets it inline on <html> from the UI font size (14px)")
for key in ("light", "normal", "medium", "semibold", "bold"):
    core_dim("fontWeight", key, f"--font-weight-{key}", conv=int, ty="fontWeight")
core_dim("fontWeight", "ui", "--font-ui-weight", conv=int, ty="fontWeight")
core_dim("fontSize", "ui", "--font-ui-size")
core_dim("fontSize", "code", "--font-code-size")
core_dim("fontSize", "chat", "--codex-chat-font-size")
core_dim("fontSize", "chat-code", "--codex-chat-code-font-size")
core_dim("fontSize", "menu", "--menu-font-size")
core_dim("fontSize", "tooltip", "--tooltip-font-size")
for key in ("tight", "snug", "normal", "relaxed"):
    core_dim("leading", key, f"--leading-{key}", conv=float, ty="number")
for key, n in (("tight", "--tracking-tight"), ("normal", "--tracking-normal"), ("wide", "--tracking-wide"), ("tooltip", "--tracking-tooltip")):
    core_dim("letterSpacing", key, n, conv=em)
for key, n in (("sans", "--font-sans"), ("sans-default", "--font-sans-default"), ("mono", "--font-mono"), ("mono-default", "--font-mono-default")):
    stack = [f.strip().strip("'\"") for f in dark_comp[n].split(",")]
    note = {"sans": "the owner's Font setting (Garamond) in front of Codex's system stack; Garamond is not installed on this Mac, so the UI renders in the system font",
            "mono": "the owner's code font (Menlo) in front of Codex's mono stack"}.get(key)
    put(CORE, ("fontFamily", key), tok(stack, "fontFamily", "Measured", f"{n} on <html>, {DATE}", note=note))
# Motion
for key, n in (("basic", "--transition-duration-basic"), ("moderate", "--transition-duration-moderate"), ("relaxed", "--transition-duration-relaxed"),
               ("default", "--default-transition-duration"), ("streaming-text", "--animation-duration-streaming-text")):
    put(CORE, ("duration", key), tok(ms(dark_comp[n]), "duration", "Measured", f"{n} on <html>, {DATE}", css=dark_comp[n]))
for key, n in (("default", "--default-transition-timing-function"), ("in-out", "--ease-in-out"), ("out", "--ease-out"), ("enter", "--ease-enter"),
               ("enter-snappy", "--ease-enter-snappy"), ("exit", "--cubic-exit"), ("exit-snappy", "--cubic-exit-snappy"), ("move", "--cubic-move")):
    put(CORE, ("easing", key), tok(bezier(dark_comp[n]), "cubicBezier", "Measured", f"{n} on <html>, {DATE}", css=dark_comp[n]))
CORE["easing"]["$extensions"] = {"notTokenised": [{"name": "--ease-spring-snappy", "value": dark_comp["--ease-spring-snappy"][:80] + "...",
    "why": "a linear() spring curve; DTCG has no type for it"}]}
# Sizes
for key in ("4xs", "3xs", "2xs", "xs", "sm", "md", "lg", "xl", "2xl", "3xl"):
    core_dim("controlHeight", key, f"--control-size-{key}")
for key in ("2xs", "xs", "sm", "md", "lg", "xl"):
    core_dim("controlGutter", key, f"--control-gutter-{key}")
for key, n in (("row", "--height-token-row"), ("nav-row", "--height-token-nav-row"), ("message", "--height-token-message"),
               ("settings-row", "--height-token-settings-row"), ("titlebar", "--height-titlebar"), ("toolbar", "--height-toolbar"),
               ("toolbar-pane", "--height-toolbar-pane"), ("toolbar-sm", "--height-toolbar-sm"), ("page-search", "--height-page-search"),
               ("switch-track", "--switch-track-height"), ("switch-thumb", "--switch-thumb-size"), ("menu-radio", "--menu-radio-indicator-size"),
               ("menu-checkbox", "--menu-checkbox-indicator-size")):
    core_dim("size", key, n)
core_dim("size", "switch-track-width", "--switch-track-width")
for key in ("xs", "sm", "md", "lg", "xl", "2xl"):
    core_dim("breakpoint", key, f"--breakpoint-{key}")
for key in ("3xs", "xs", "sm", "md", "lg", "xl", "2xl", "3xl", "4xl", "5xl", "6xl", "7xl"):
    core_dim("container", key, f"--container-{key}")
for key in ("xs", "sm", "md", "lg", "xl", "2xl", "3xl"):
    core_dim("blur", key, f"--blur-{key}")
core_dim("layout", "sidebar", "--codex-sidebar-preferred-width", note="the owner's sidebar width (Codex's default range is 240 to 520px)")
core_dim("layout", "dialog-max", "--dialog-max-width")
core_dim("layout", "dialog-min", "--dialog-min-width")
core_dim("layout", "dialog-padding", "--dialog-container-inner-padding")
core_dim("borderWidth", "hairline", "--border-width-hairline")
put(CORE, ("borderWidth", "default"), tok("1px", "dimension", "Measured", f"border-top-width of the composer, cards and inputs (computed), {DATE}"))
put(CORE, ("zoom",), tok(float(dark_comp["--codex-window-zoom"]), "number", "Measured", f"--codex-window-zoom on <html> (unzoomed), {DATE}"))

# ---------------------------------------------------------------- semantic sets


def keep(n, painted):
    if SKIP.match(n) or n not in painted or not is_color(painted[n]):
        return False
    if re.fullmatch(r"--(%s)-a?\d+" % "|".join(HUES), n) and get(CORE, "color." + n[2:].replace("-", ".", 1)):
        return False                   # a theme-independent hue step, already in core
    if path_of(n)[0] == "kit" and not re.match(r"--(input|tooltip|switch|radio|menu|segmented|dialog|modal|link|user|scrollbar|button|composer|chat|codex|app)-", n):
        return False
    return True


def semantic(t):
    """Each kept name as its painted colour, or as an alias when its formula is a plain var() of a kept name
    (or of a core hue step) that paints the same."""
    tree, comp, painted = {}, computed(t), V[t]["colors"]
    kept = {n for n in comp if keep(n, painted)}
    for n in sorted(kept):
        value = color(painted[n])
        f = formula(t, n)
        m = re.fullmatch(r"var\((--[\w-]+)(?:,[^()]*)?\)", (f or "").strip())
        target = m.group(1) if m else None
        hue = re.fullmatch(r"--(%s)-(a?\d+)" % "|".join(HUES), target or "")
        tpath = path_of(target) if target in kept else (("color", hue.group(1), hue.group(2)) if hue and get(CORE, "color.%s.%s" % hue.groups()) else None)
        if tpath and target != n and is_color(painted.get(target, "")) and color(painted[target]) == value:
            put(tree, path_of(n), tok("{%s}" % ".".join(tpath), "color", "Measured", where(t, n), formula=f))
        else:
            put(tree, path_of(n), tok(value, "color", "Measured", where(t, n), formula=f if f and f != value else None))
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


# Shadows per theme: the elevation steps and the named shadows, as painted.
SHADOWS = ["--shadow-100", "--shadow-200", "--shadow-300", "--shadow-400", "--shadow-sm", "--shadow-md", "--shadow-lg", "--shadow-xl", "--shadow-2xl",
           "--shadow-card", "--shadow-hairline", "--shadow-dropdown-overlay", "--shadow-popover-overlay", "--shadow-tooltip", "--menu-box-shadow",
           "--dialog-backdrop-fade-shadow", "--switch-thumb-shadow", "--elevation-composer", "--elevation-prominent"]
for t in THEMES:
    for n in SHADOWS:
        css = V[t]["shadows"].get(n)
        if not css or css == "none":
            continue
        key = n.replace("--shadow-", "").replace("--", "")
        put(SETS[t], ("shadow", key), tok(shadow(css), "shadow", "Measured", f"{n} as painted (box-shadow on a probe), {THEME_NAME[t]}, {DATE}", css=computed(t).get(n)))

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
ROLES = [("display", "home-heading", "The new-chat heading (What should we work on in ...)"),
         ("title", "page-title", "Settings page titles (h1)"),
         ("heading", "section-title", "Settings section titles"),
         ("body", "assistant-message", "Agent replies"),
         ("prompt", "composer-editor", "Text typed in the composer"),
         ("label", "project-row", "Sidebar rows"),
         ("menu", "menu-row", "Menu items"),
         ("caption", "tooltip", "Tooltips"),
         ("button", "button-primary", "Button labels"),
         ("code", "inline-code", "Inline code in replies")]
for role, part, use in ROLES:
    shot, s = style("dark", part)
    if not s:
        continue
    fam = "{fontFamily.mono}" if role == "code" else "{fontFamily.sans}"
    lh = s["line-height"]
    val = {"fontFamily": fam, "fontSize": px(s["font-size"]), "fontWeight": int(s["font-weight"]),
           "lineHeight": px(lh) if lh.endswith("px") else px("%gpx" % round(float(s["font-size"][:-2]) * 1.2, 1)),
           "letterSpacing": px(s["letter-spacing"]) if s["letter-spacing"].endswith("px") else "0px"}
    put(CORE, ("typography", role), tok(val, "typography", "Measured", f"computed style of {part} in {shot}, dark, {DATE}; {use}",
        note=None if lh.endswith("px") else "computed line-height is normal; 1.2 x the size is used here"))


def dim_of(part, prop, state="default", t="dark"):
    shot, s = style(t, part, state)
    return (shot, s[prop]) if s and s.get(prop, "").endswith("px") else (None, None)


SIZES = [("size.control.icon-button", "icon-button", "height", "Sidebar icon buttons (Search, View activity)"),
         ("size.control.rail-button", "rail-button", "height", "Navigation rail buttons"),
         ("size.control.composer-tool", "composer-tool", "height", "Composer icon buttons (add, dictate)"),
         ("size.control.voice", "voice-button", "height", "The composer's round voice / send button"),
         ("size.control.chip", "permissions-button", "height", "Composer chips (permissions, model)"),
         ("size.control.row", "project-row", "height", "Sidebar rows"),
         ("size.control.settings-nav", "settings-nav", "height", "Settings navigation rows"),
         ("size.control.menu-row", "menu-row", "height", "Menu rows"),
         ("size.control.select", "select", "height", "Settings selects"),
         ("size.control.button", "button-primary", "height", "Dialog buttons"),
         ("size.control.switch-width", "switch-track-on", "width", "Switch track"),
         ("size.control.switch-height", "switch-track-on", "height", "Switch track"),
         ("layout.rail", "rail", "width", "Navigation rail"),
         ("layout.sidebar-measured", "sidebar", "width", "Sidebar (the owner's 290px less the rail)"),
         ("layout.composer", "composer", "width", "Composer on the new-chat page"),
         ("layout.menu", "menu", "width", "Menus"),
         ("layout.palette", "palette", "width", "Search palette"),
         ("layout.dialog", "dialog", "width", "Remove project confirmation"),
         ("layout.settings-card", "settings-card", "width", "Settings content column")]
for path, part, prop, use in SIZES:
    shot, v = dim_of(part, prop)
    if v:
        put(CORE, tuple(path.split(".")), tok(px(v), "dimension", "Measured",
            f"computed {prop} of {part} in {shot}, dark, {DATE} ({use})"))
WINDOW = C["dark"]["home-default"]["viewport"]
put(CORE, ("layout", "window-width"), tok(f"{WINDOW['css'][0]}px", "dimension", "Measured",
    f"the window's viewport, {WINDOW['css'][0]} x {WINDOW['css'][1]} CSS px at devicePixelRatio {WINDOW['dpr']} (unzoomed), {DATE}"))
put(CORE, ("layout", "window-height"), tok(f"{WINDOW['css'][1]}px", "dimension", "Measured", f"the window's viewport height, {DATE}"))
for key, part in (("menu", "menu"), ("dialog", "dialog"), ("tooltip", "tooltip"), ("palette", "palette")):
    shot, s = style("dark", part)
    if s and s["z-index"] not in ("auto", ""):
        put(CORE, ("zIndex", key), tok(int(s["z-index"]), "number", "Measured", f"computed z-index of {part} in {shot}, {DATE}"))
# Focus ring: read on a focused control.
for part in ("select", "button-secondary", "switch-off", "settings-nav", "icon-button", "composer-tool"):
    shot, s = style("dark", part, "focus-visible")
    if not s:
        continue
    if s["outline-style"] != "none" and s["outline-width"] not in ("0px", ""):
        put(CORE, ("focusRing", "width"), tok(px(s["outline-width"]), "dimension", "Measured", f"outline-width of {part} in {shot}, dark, {DATE}", css=f"{s['outline-width']} {s['outline-style']} {s['outline-color']}"))
        put(CORE, ("focusRing", "offset"), tok(px(s["outline-offset"]), "dimension", "Measured", f"outline-offset of {part} in {shot}, dark, {DATE}"))
        break
    layers = [l for l in shadow(s["box-shadow"]) if not l["color"].endswith(", 0)")]
    if layers:
        ring = max(layers, key=lambda l: float(l["spread"][:-2]))
        put(CORE, ("focusRing", "width"), tok(ring["spread"], "dimension", "Measured", f"spread of the focus box-shadow of {part} in {shot}, dark, {DATE}", css=s["box-shadow"]))
        put(CORE, ("focusRing", "offset"), tok("0px", "dimension", "Measured", f"the ring is a box-shadow outside the edge ({shot}), {DATE}"))
        break
put(CORE, ("borderWidth", "focus"), tok("{focusRing.width}", "dimension", "Derived", "the focus ring's width"))

cond = V["dark"]["conditions"]
rm = {k: v["rules"] for k, v in cond.items() if "reduced-motion" in k}
CORE["duration"]["$extensions"] = {"reducedMotion": {"rules": rm,
    "how": "Codex sets data-reduced-motion on <html> from Settings (System by default) and Tailwind's motion-safe:/motion-reduce: variants stop spinners, shimmers and enter animations; no duration token changes"}}

# ---------------------------------------------------------------- roles and components, per theme

ROLE = {
    "page": ("{token.main-surface-primary}", "the main pane: the new-chat page, chats and settings"),
    "surface": ("{token.side-bar-background}", "the sidebar and the navigation rail"),
    "raised": ("{app.background-elevated-primary}", "menus, popovers, dialogs and the composer"),
    "overlay": ("{app.background-elevated-secondary}", "the second raised level (submenus, nested surfaces)"),
    "scrim": (None, "dialog", "the dialog backdrop draws no scrim; the dialog's own shadow separates it"),
    "text.primary": ("{text.primary}", ""), "text.secondary": ("{text.secondary}", ""), "text.disabled": ("{text.disabled}", ""),
    "text.on-accent": ("{text.accent-action}", "text on the accent fill"), "text.link": ("{token.text-link-foreground}", ""),
    "border.default": ("{misc.border}", "the ink at a low alpha (--color-border): cards, menus, the composer"), "border.strong": ("{border.strong}", ""),
    "border.focus": ("{token.focus-border}", "the focus ring colour"),
    "accent.default": ("{bg.accent-action}", "the theme's accent seed: the switch, links, file mentions, the permission chip's warning"),
    "accent.subtle": ("{bg.info-soft}", "the accent at a low alpha"),
}
for s_, src in (("success", "success"), ("warning", "warning"), ("danger", "danger"), ("info", "info")):
    ROLE[f"status.{s_}.fill"] = ("{bg.%s-solid}" % src, "")
    ROLE[f"status.{s_}.text"] = ("{text.%s}" % src, "")
    ROLE[f"status.{s_}.subtle"] = ("{bg.%s-soft}" % src, "")
    ROLE[f"status.{s_}.border"] = ("{border.%s-outline}" % src, "")

COMPONENTS = [
    ("button-primary", "button-primary", {"bg": "background-color", "text": "color", "radius": "border-top-left-radius", "height": "height", "padding": "padding-right"}),
    ("button-ghost", "button-ghost", {"text": "color", "radius": "border-top-left-radius", "height": "height"}),
    ("button-danger", "button-danger", {"bg": "background-color", "text": "color", "radius": "border-top-left-radius", "height": "height"}),
    ("button-secondary", "button-secondary", {"bg": "background-color", "border": "border-top-color", "text": "color", "radius": "border-top-left-radius", "height": "height"}),
    ("icon-button", "icon-button", {"text": "color", "radius": "border-top-left-radius", "size": "height"}),
    ("rail-button", "rail-button", {"text": "color", "radius": "border-top-left-radius", "size": "height"}),
    ("rail-button-selected", "rail-button-selected", {"bg": "background-color", "text": "color"}),
    ("voice-button", "voice-button", {"bg": "background-color", "text": "color", "radius": "border-top-left-radius", "size": "height"}),
    ("composer", "composer", {"bg": "background-color", "border": "border-top-color", "radius": "border-top-left-radius"}),
    ("composer-chip", "permissions-button", {"text": "color", "radius": "border-top-left-radius", "height": "height"}),
    ("model-button", "model-button", {"text": "color", "radius": "border-top-left-radius", "height": "height"}),
    ("utility-bar", "utility-bar", {"bg": "background-color", "radius": "border-top-left-radius"}),
    ("menu", "menu", {"bg": "background-color", "border": "border-top-color", "text": "color", "radius": "border-top-left-radius"}),
    ("menu-row", "menu-row", {"text": "color", "radius": "border-top-left-radius", "height": "height", "padding": "padding-left"}),
    ("composer-menu", "composer-menu", {"bg": "background-color", "border": "border-top-color", "radius": "border-top-left-radius"}),
    ("dialog", "dialog", {"bg": "background-color", "border": "border-top-color", "radius": "border-top-left-radius", "padding": "padding-top"}),
    ("palette", "palette", {"bg": "background-color", "border": "border-top-color", "radius": "border-top-left-radius"}),
    ("palette-row-selected", "palette-row-selected", {"bg": "background-color", "text": "color", "radius": "border-top-left-radius"}),
    ("tooltip", "tooltip", {"bg": "background-color", "text": "color", "radius": "border-top-left-radius"}),
    ("text-field", "text-field-focused", {"bg": "background-color", "border": "border-top-color", "radius": "border-top-left-radius", "height": "height"}),
    ("settings-search", "settings-search", {"bg": "background-color", "text": "color", "radius": "border-top-left-radius", "height": "height"}),
    ("select", "select", {"bg": "background-color", "border": "border-top-color", "text": "color", "radius": "border-top-left-radius", "height": "height"}),
    ("switch-on", "switch-track-on", {"bg": "background-color", "radius": "border-top-left-radius", "width": "width", "height": "height"}),
    ("switch-off", "switch-track-off", {"bg": "background-color"}),
    ("radio-thumb", "radio-thumb", {"radius": "border-top-left-radius", "width": "width"}),
    ("settings-card", "settings-card", {"bg": "background-color", "border": "border-top-color", "radius": "border-top-left-radius"}),
    ("settings-nav", "settings-nav", {"text": "color", "radius": "border-top-left-radius", "height": "height"}),
    ("settings-nav-selected", "settings-nav-selected", {"bg": "background-color", "text": "color"}),
    ("project-row", "project-row", {"text": "color", "radius": "border-top-left-radius", "height": "height"}),
    ("project-row-selected", "project-row-selected", {"bg": "background-color", "text": "color"}),
    ("thread-row", "thread-row", {"text": "color", "radius": "border-top-left-radius", "height": "height"}),
    ("user-message", "user-message", {"bg": "background-color", "text": "color", "radius": "border-top-left-radius", "padding": "padding-left"}),
    ("inline-code", "inline-code", {"bg": "background-color", "text": "color", "radius": "border-top-left-radius"}),
    ("file-mention", "file-mention", {"text": "color"}),
    ("summary-panel", "summary-panel", {"bg": "background-color", "border": "border-top-color", "radius": "border-top-left-radius"}),
    ("kbd", "kbd", {"bg": "background-color", "text": "color", "radius": "border-top-left-radius"}),
    ("tab", "tab", {"bg": "background-color", "text": "color", "radius": "border-top-left-radius", "height": "height"}),
]
STATES = [("hover", "bg-hover", "background-color"), ("hover", "text-hover", "color"), ("pressed", "bg-pressed", "background-color"),
          ("focus-visible", "outline-focus", "outline-color")]
CORE_NAMES = re.compile(r"^(token\.(main-surface-primary|side-bar-background|text-primary|text-secondary)|bg\.(elevated-primary|accent-action)|text\.(primary|secondary|tertiary)|border\.(default|heavy|light))$")
AWKWARD = re.compile(r"chart|tooltip|disabled|other-user|page-search|chatgpt|business|coachmark|header-upgrade|internal|activity|execution|viewer|mode-toggle|attribution|artifact")
PREFER = ["role", "token", "bg", "text", "border", "ring", "codex", "app", "chat", "alpha", "gray", "color"]


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
        # Names that only coincide in value (a tooltip fill, the disabled tint, the page search box) go last.
        vals.sort(key=lambda p: (not CORE_NAMES.match(p), bool(AWKWARD.search(p)), PREFER.index(p.split(".")[0]) if p.split(".")[0] in PREFER else 99, len(p), p))
    return idx


def build_roles_and_components(t):
    tree = SETS[t]
    for key, spec in ROLE.items():
        if spec[0] is None:
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
                # A fill aliases a fill-like token and a text colour a text-like one; a value that only matches
                # a token of another kind (a menu fill equal to a tooltip text colour) stays a value.
                kinds = {"color": ("text", "token", "app", "codex"), "background-color": ("bg", "token", "app", "codex", "surface", "alpha", "gray", "seed"),
                         "border-top-color": ("border", "token", "misc", "ring", "app"), "outline-color": ("ring", "token", "border", "bg")}[prop]
                fits = [x for x in idx[v] if x.split(".")[0] in kinds and not (prop != "color" and "text" in x.split(".")[0])]
                if fits:
                    aliased_n += 1
                    first = {"color": "text", "background-color": "bg", "border-top-color": "border", "outline-color": "ring"}[prop]
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
                if prop == "outline-color" and ss.get("outline-style") in ("none", ""):
                    continue
                put(tree, ("component", name, key), value_for(part, sh, prop, ss[prop]))
    # The scrim role: Codex's dialogs draw no backdrop colour.
    shot, s = style(t, "dialog")
    put(tree, ("role", "scrim"), tok("rgba(0, 0, 0, 0)", "color", "Measured",
        f"the dialog backdrop in {shot}, {THEME_NAME[t]}, {DATE}: Codex mounts no tinted overlay; the dialog sits on a 1px blur (--dialog-backdrop-fade-filter) with its own shadow (shadow.dialog-backdrop-fade-shadow)"))
    for key, (comp_path, why) in {"accent.hover": ("component.switch-on.bg-hover", "the switch's on fill under the pointer"),
                                  "accent.pressed": ("component.switch-on.bg-pressed", "the switch's on fill while pressed")}.items():
        hit = get(tree, comp_path)
        if hit:
            put(tree, ("role",) + tuple(key.split(".")), tok(hit["$value"], "color", "Measured", hit["$extensions"]["source"]["from"] + f"; {why}"))
        else:
            put(tree, ("role",) + tuple(key.split(".")), tok("{bg.accent-action}", "color", "Derived", f"Codex declares no hover or pressed accent; {why} paints the accent unchanged"))
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
            # an alias to a removed token takes the painted value
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
         "$description": "Settings > Appearance > Mode: Light, with the owner's Catppuccin theme ([data-theme=light])"},
        {"id": "dark", "name": "Dark", "selectedTokenSets": {"core": "source", "dark": "enabled"},
         "$description": "Settings > Appearance > Mode: System with a dark macOS appearance, or Dark, with the owner's Absolutely theme ([data-theme=dark])"},
    ],
    "$metadata": {"tokenSetOrder": ["core", "light", "dark"]},
}
(PKG / "tokens.json").write_text(json.dumps(tokens, indent=2, ensure_ascii=False) + "\n")


def count(d):
    return sum(1 for _ in tokens_of(d))


print({k: count(tokens[k]) for k in ("core", "light", "dark")}, "component values aliased:",
      {t: SETS[t]["$extensions"]["componentValues"] for t in THEMES})
