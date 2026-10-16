#!/usr/bin/env python3
"""Build tokens/linear.tokens.json, tokens/tokens-studio.json and tokens/linear.css.

Sources:
  raw/css-vars.json               the signed-in app's CSS variables, read on <main> (inside Linear's
                                  theme provider) in a dark and a light page copy, plus the bundle's
                                  @media, z-index, motion and font faces, the status icon colours
                                  and the overlay z-index stacks (tools/capture/vars.mjs, 2026-10-17)
  raw/components-computed.json    computed styles of the app's components per state and theme
                                  (tools/capture/signed-in/measure.mjs, 2026-10-17)
  the WEB and BRAND tables below  the public website's computed CSS and the brand page, read on
                                  2026-09-23 (evidence/styles/*-styles.json, https://linear.app/brand)

Sets: `core` (type, radii, sizes, borders, focus ring, motion, breakpoints, z-index, and the
spacing scale, which is a reconstruction), `dark` and `light` (the app's colour roles and shadows),
`web` and `brand` (the public site and the brand page, unchanged from the 2026-09-23 capture).

Every token carries `$extensions.source` (where it was read) and `$extensions.evidence` (the label
from docs/EVIDENCE.md). Linear computes its palette in lch(); colours are converted to sRGB hex
here with the CSS Color 4 formulas (lab D50 -> XYZ -> D65 -> sRGB), so a channel can differ by one
from a hex Linear declares elsewhere. A component colour that equals a theme variable names that
variable in its source. Deterministic: same inputs, same bytes. The builder refuses a token without
a source, a dimension that is not one px or rem length, and a colour it cannot convert.
"""
import json, math, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
V = json.loads((RAW / "css-vars.json").read_text())
C = json.loads((RAW / "components-computed.json").read_text())["components"]
THEMES = ("dark", "light")
COPY = {"dark": "issue-dark", "light": "issue-light"}

# ---------------------------------------------------------------- colour


def gam(x):
    return 12.92 * x if x <= 0.0031308 else 1.055 * x ** (1 / 2.4) - 0.055


def lab_rgb(L, a, b):
    fy = (L + 16) / 116
    fx, fz = fy + a / 500, fy - b / 200
    e, k = 216 / 24389, 24389 / 27
    finv = lambda t: t ** 3 if t ** 3 > e else (116 * t - 16) / k
    X, Y, Z = finv(fx) * 0.3457 / 0.3585, (fy ** 3 if L > k * e else L / k), finv(fz) * (1 - 0.3457 - 0.3585) / 0.3585
    x = 0.955473421488075 * X - 0.02309845494876471 * Y + 0.06325924320057072 * Z
    y = -0.0283697093338637 * X + 1.0099953980813041 * Y + 0.021041441191917323 * Z
    z = 0.012314014864481998 * X - 0.020507649298898964 * Y + 1.330365926242124 * Z
    rgb = [3.2409699419 * x - 1.5373831776 * y - 0.4986107603 * z, -0.9692436363 * x + 1.8759675015 * y + 0.0415550574 * z,
           0.0556300797 * x - 0.2039769589 * y + 1.0569715142 * z]
    return [round(min(1, max(0, gam(v))) * 255) for v in rgb]


def fmt(rgb, a=1):
    a = round(float(a), 3)
    return "#%02x%02x%02x" % tuple(rgb) if a >= 1 else "rgba(%d, %d, %d, %s)" % (*rgb, "%g" % a)


def color(c):
    """A colour string the browser computes or a stylesheet declares -> '#rrggbb' or 'rgba(...)'."""
    c = c.strip()
    m = re.fullmatch(r"lch\(([-\d.e]+)%? ([-\d.e]+) ([-\d.e]+)(?: / ([\d.]+%?))?\)", c)
    if m:
        L, Ch, H = (float(m.group(i)) for i in (1, 2, 3))
        a = m.group(4) or "1"
        a = float(a[:-1]) / 100 if a.endswith("%") else float(a)
        return fmt(lab_rgb(L, Ch * math.cos(math.radians(H)), Ch * math.sin(math.radians(H))), a)
    m = re.fullmatch(r"#([0-9a-fA-F]{3,8})", c)
    if m:
        h = m.group(1)
        if len(h) in (3, 4):
            h = "".join(ch * 2 for ch in h)
        return fmt([int(h[i:i + 2], 16) for i in (0, 2, 4)], int(h[6:8], 16) / 255 if len(h) == 8 else 1)
    m = re.fullmatch(r"rgba?\((\d+),\s*(\d+),\s*(\d+)(?:,\s*([\d.]+))?\)", c)
    if m:
        return fmt([int(m.group(i)) for i in (1, 2, 3)], m.group(4) or 1)
    raise ValueError("colour not understood: " + c)


def split_top(s):
    out, depth, cur = [], 0, ""
    for ch in s:
        depth += ch == "("
        depth -= ch == ")"
        if ch == "," and depth == 0:
            out.append(cur)
            cur = ""
        else:
            cur += ch
    out.append(cur)
    return [x.strip() for x in out if x.strip()]


COLOR_RE = r"(#[0-9a-fA-F]{3,8}|(?:rgba?|lch)\([^)]*\))"


def px(v):
    m = re.fullmatch(r"(-?\d*\.?\d+)px", str(v).strip())
    if not m:
        raise ValueError("not a px length: %r" % v)
    return ("%g" % round(float(m.group(1)), 3)) + "px"


def rem(v):
    m = re.fullmatch(r"(\d*\.?\d+)rem", v.strip())
    return px("%gpx" % (float(m.group(1)) * 16))


def shadow(v):
    layers = []
    for part in split_top(v):
        inset = bool(re.search(r"\binset\b", part))
        part = re.sub(r"\binset\b", "", part).strip()
        m = re.search(COLOR_RE, part)
        nums = (part[:m.start()] + " " + part[m.end():]).split()
        nums = [n if n.endswith("px") else n + "px" for n in nums] + ["0px"] * (4 - len(nums))
        layers.append({"color": color(m.group(1)), "offsetX": px(nums[0]), "offsetY": px(nums[1]), "blur": px(nums[2]), "spread": px(nums[3]), "inset": inset})
    return layers


def seconds_ms(v):
    m = re.fullmatch(r"(\d*\.?\d+)(m?s)", v.strip())
    return ("%g" % round(float(m.group(1)) * (1 if m.group(2) == "ms" else 1000), 3)) + "ms"


def bezier(v):
    m = re.fullmatch(r"cubic-bezier\(([^)]*)\)", v.strip())
    if m:
        return [float("%g" % float(x)) for x in m.group(1).split(",")]
    return {"ease": [0.25, 0.1, 0.25, 1], "ease-out": [0, 0, 0.58, 1], "ease-in-out": [0.42, 0, 0.58, 1], "linear": [0, 0, 1, 1]}[v.strip()]


# ---------------------------------------------------------------- readers


def tok(value, ty, source, evidence="Measured", **ext):
    t = {"$value": value, "$type": ty, "$extensions": {"source": source, "evidence": evidence}}
    t["$extensions"].update(ext)
    return t


def put(tree, path, t):
    node = tree
    for k in path.split(".")[:-1]:
        node = node.setdefault(k, {})
    node[path.split(".")[-1]] = t


def var(name, theme):
    v = V["theme"][theme].get(name)
    if not v:
        raise KeyError(f"{name} not read in {theme}")
    return v


# Readable names Linear's own bundle gives a hashed variable (`--dp-control-primary: var(--sx-n8xqcl)`).
ALIAS = {}
for name, targets in V["aliases"].items():
    for sx in targets:
        ALIAS.setdefault(sx, []).append(name)


def var_note(name):
    names = sorted(ALIAS.get(name, []))[:3]
    return f"css-var {name}" + (f" (named {', '.join(names)} in Linear's bundle)" if names else "")


def css(name, theme):
    return color(var(name, theme)), f"{var_note(name)}, getComputedStyle on <main> in the {theme} copy {COPY[theme]}"


def state(comp, st, theme):
    key = st if theme == "dark" else ("light" if st == "default" else f"light-{st}")
    s = C[comp]["states"].get(key)
    if not s or "style" not in s:
        raise KeyError(f"{comp} {key} not measured")
    return s


def matching_var(value, theme):
    """The theme variables whose colour equals this one, Linear's readable names first."""
    hits = []
    for k, v in V["theme"][theme].items():
        if not re.match(r"(lch|#|rgb)", v):
            continue
        try:
            if color(v) == value:
                hits.append(k)
        except ValueError:
            pass
    hits.sort(key=lambda k: (k.startswith("--sx-"), k))
    return hits[:2]


def comp(comp_key, st, theme, prop="backgroundColor", where="element"):
    s = state(comp_key, st, theme)
    if where == "text":
        raw = s["textStyle"]["color"]
    elif where == "paint":
        raw = next(p["bg"] for p in s["paint"] if p.get("bg"))
    else:
        raw = s["style"][prop]
    value = color(raw)
    hits = matching_var(value, theme)
    title = C[comp_key]["title"]
    src = f"computed {prop if where == 'element' else where + ' colour'} of {title}, state {st}, copy {s['snapshot']}"
    if hits:
        src += f"; equals {', '.join(hits)}"
    return value, src


# ---------------------------------------------------------------- themed sets

themed = {}
not_tok = {t: [] for t in THEMES}
for theme in THEMES:
    T = {}
    def c(path, pair, evidence="Measured"):
        put(T, path, tok(pair[0], "color", pair[1], evidence))
    c("color.bg.page", css("--content-bg-color", theme))
    c("color.bg.panel", css("--color-bg-primary", theme))
    c("color.bg.raised", comp("card", "default", theme))
    c("color.bg.control", comp("tab", "default", theme))
    c("color.bg.control-hover", comp("tab", "hover", theme))
    c("color.bg.selected", comp("tab", "selected", theme))
    c("color.bg.overlay", comp("toast", "default", theme))
    c("color.bg.overlay-strong", comp("select", "open", theme))
    c("color.bg.highlight", comp("menu", "option-highlighted", theme))
    c("color.bg.scrim", comp("dialog-scrim", "default", theme))
    c("color.text.primary", css("--color-text-primary", theme))
    c("color.text.secondary", css("--color-text-secondary", theme))
    c("color.text.tertiary", css("--color-text-tertiary", theme))
    c("color.text.quaternary", css("--color-text-quaternary", theme))
    c("color.text.link", css("--sx-1xaoi8i", theme))
    c("color.text.on-accent", comp("button-primary", "default", theme, "color"))
    c("color.border.primary", css("--color-border-primary", theme))
    c("color.border.secondary", css("--color-border-secondary", theme))
    c("color.border.tertiary", css("--color-border-tertiary", theme))
    c("color.border.field", comp("text-field", "default", theme, "borderTopColor"))
    c("color.border.field-hover", comp("text-field", "hover", theme, "borderTopColor"))
    c("color.border.focus", css("--focus-ring-color", theme))
    c("color.accent.default", comp("button-primary", "default", theme))
    c("color.accent.hover", comp("button-primary", "hover", theme))
    c("color.accent.pressed", comp("button-primary", "pressed", theme))
    c("color.feedback.danger", comp("button-danger", "default", theme, where="text"))
    c("color.feedback.danger-hover-bg", comp("button-danger", "hover", theme, where="paint"))
    c("color.feedback.success", comp("presence-online", "default", theme))
    c("color.feedback.warning", comp("health-at-risk", "default", theme, "color"))
    c("color.feedback.on-track", comp("health-on-track", "default", theme, "color"))
    for label, value in V["statusColors"][theme].items():
        slug = label.lower().replace(" ", "-")
        put(T, f"color.status.{slug}", tok(color(value), "color", f"computed stroke or fill of the {label} icon in the status menu, copy issue-{theme}-menu"))
    for name, v, where in (("low", "--sx-10lzhmx", "buttons, tabs and cards"), ("medium", "--sx-1dhg814", "menus, toasts and select lists"), ("high", "--sx-1k7v50d", "the composer dialog"), ("inset", "--sx-umgfby", "pressed and inset wells")):
        put(T, f"shadow.{name}", tok(shadow(var(v, theme)), "shadow", f"{var_note(v)}, getComputedStyle on <main> in the {theme} copy {COPY[theme]}; matches the computed box-shadow of {where}" if name != "inset" else f"{var_note(v)}, getComputedStyle on <main> in the {theme} copy {COPY[theme]}"))
    card = state("card", "default", theme)["style"]["boxShadow"]
    put(T, "shadow.card", tok(shadow(card), "shadow", f"computed box-shadow of a board card, copy issues-board-{theme} (a 0.5px ring plus the low shadow)"))
    not_tok[theme].append({"role": "color.feedback.info", "reason": "Not captured: no info banner or info-coloured message appeared on the screens reached"})
    themed[theme] = T

# ---------------------------------------------------------------- core

core = {}
d = "dark"
put(core, "font.family.ui", tok([f.strip().strip('"') for f in split_top(var("--font-regular", d))], "fontFamily", "css-var --font-regular, getComputedStyle on <main>, copy issue-dark"))
put(core, "font.family.mono", tok([f.strip().strip('"') for f in split_top(var("--font-monospace", d))], "fontFamily", "css-var --font-monospace, getComputedStyle on <main>, copy issue-dark"))
put(core, "font.family.emoji", tok([f.strip().strip('"') for f in split_top(var("--font-emoji", d))], "fontFamily", "css-var --font-emoji, getComputedStyle on <main>, copy issue-dark"))
put(core, "font.family.editorial", tok(["Tiempos Headline", "Georgia", "serif"], "fontFamily", "public site computed font-family of the Linear Method heading, evidence/styles/method-styles.json, 2026-09-23; Georgia and serif are this package's fallbacks", "Measured (public site)"))
for name in ("micro", "mini", "small", "regular", "large", "title3", "title2", "title1"):
    raw = var(f"--font-size-{name}", d)
    m = re.fullmatch(r"round\(up, (\d*\.?\d+)rem, (\d+)px\)", raw)
    if m:
        # CSS round(up, 0.6875rem, 2px): 11px rounded up to the next 2px step.
        value = px("%gpx" % (math.ceil(float(m.group(1)) * 16 / int(m.group(2))) * int(m.group(2))))
        put(core, f"font.size.{name}", tok(value, "dimension", f"css-var --font-size-{name} ({raw}), worked out at 16px", "Derived"))
    else:
        put(core, f"font.size.{name}", tok(rem(raw), "dimension", f"css-var --font-size-{name} ({raw} at 16px), copy issue-dark"))
for name in ("light", "normal", "medium", "semibold", "bold"):
    put(core, f"font.weight.{name}", tok(int(var(f"--font-weight-{name}", d)), "fontWeight", f"css-var --font-weight-{name}, copy issue-dark"))
put(core, "font.lineHeight.editor", tok(float(var("--editor-line-height", d)), "number", "css-var --editor-line-height, copy issue-dark"))


def typo(path, comp_key, use_text, note):
    s = state(comp_key, "default", "dark")
    t = s["textStyle"] if use_text and s.get("textStyle") else s["style"]
    lh = t["lineHeight"]
    first = [f.strip().strip('"') for f in split_top(t["fontFamily"])][0]
    val = {"fontFamily": [first, "monospace" if "Mono" in first else "sans-serif"], "fontSize": px(t["fontSize"]), "fontWeight": int(t["fontWeight"])}
    if lh != "normal" and lh != "0px":
        val["lineHeight"] = round(float(lh[:-2]) / float(t["fontSize"][:-2]), 3)
    if t.get("letterSpacing") and t["letterSpacing"] != "normal":
        val["letterSpacing"] = px(t["letterSpacing"])
    put(core, path, tok(val, "typography", f"computed {'text node' if use_text else 'element'} style of {C[comp_key]['title']}, copy {s['snapshot']}; {note}"))


typo("typography.issue-title", "type-issue-title", True, "the issue detail title")
typo("typography.heading", "type-heading", True, "an h2 in an issue description")
typo("typography.body", "type-body", True, "a description paragraph (--editor-font-size, --editor-line-height)")
typo("typography.page-title", "type-page-title", True, "a settings page title")
typo("typography.label", "nav-item", True, "sidebar item label")
typo("typography.control", "tab", True, "view tab and small control label")
typo("typography.caption", "type-caption", False, "card meta line")
typo("typography.section-label", "type-section-label", False, "sidebar section label")
typo("typography.code", "type-code", True, "inline code in a description")

for name, v, note in (("control", "--control-border-radius", "control radius"), ("settings-group", "--settings-list-view-item-radius", "settings list group"), ("editor-block", "--editor-block-radius", "editor blocks"), ("pill", "--radius-rounded", "pills, tabs, buttons")):
    put(core, f"radius.{name}", tok(px(var(v, d)), "dimension", f"css-var {v} ({note}), copy issue-dark"))
for name, comp_key, note in (("card", "card", "board card"), ("menu", "toast", "toast, menu and select surfaces (12px on each)"), ("dialog", "dialog", "composer dialog"), ("badge", "badge", "Admin badge"), ("kbd", "kbd", "keyboard key in a tooltip")):
    s = state(comp_key, "default", "dark")
    put(core, f"radius.{name}", tok(px(s["style"]["borderTopLeftRadius"]), "dimension", f"computed border-radius of the {note}, copy {s['snapshot']}"))

SPACE = {"1": 4, "2": 8, "3": 12, "4": 16, "6": 24, "8": 32, "12": 48, "16": 64}
for k, v in SPACE.items():
    put(core, f"space.{k}", tok(f"{v}px", "dimension", "4px-step scale chosen for this package in 2026-09; Linear declares no spacing scale and its stylex classes carry literal paddings", "Reconstruction"))

for name, comp_key, prop, note in (("control", "button-primary", "height", "primary button, tabs and icon buttons"), ("control-large", "text-field", "height", "text fields, search and page-header buttons"),
                                   ("sidebar-item", "nav-item", "height", "sidebar items"), ("menu-option", "menu", "option", "menu and select options"), ("list-row", "list-row", "height", "sub-issue rows"),
                                   ("table-row", "table-row", "height", "projects table rows"), ("avatar", "avatar", "width", "avatars in tables"), ("switch-width", "switch", "width", "switch track"), ("switch-height", "switch", "height", "switch track")):
    if prop == "option":
        s = state("menu", "option", "dark")
        value = px("%gpx" % s["rect"]["h"])
    else:
        s = state(comp_key, "default", "dark")
        value = px("%gpx" % s["rect"]["h" if prop == "height" else "w"])
    put(core, f"size.{name}", tok(value, "dimension", f"measured {prop if prop != 'option' else 'height'} of the {note}, copy {s['snapshot']}"))
put(core, "size.icon", tok(px("%gpx" % state("icon-button", "default", "dark")["icon"]["w"]), "dimension", "measured icon width inside the icon button, copy issue-dark"))
for name, v in (("sidebar-width", "--sidebar-width"), ("header-height", "--header-height"), ("desktop-tabs-height", "--desktop-tabs-height")):
    put(core, f"layout.{name}", tok(px(var(v, d)), "dimension", f"css-var {v}, copy issue-dark"))
put(core, "layout.content-inset", tok(px("%gpx" % state("app-shell-main", "default", "dark")["rect"]["y"]), "dimension", "measured gap between the window edge and the inset main panel, copy issues-board-dark"))

put(core, "borderWidth.default", tok(px(state("text-field", "default", "dark")["style"]["borderTopWidth"]), "dimension", "computed border width of a text field, copy settings-workspace-dark"))
put(core, "borderWidth.hairline", tok(px(var("--editor-hairline", d)), "dimension", "css-var --editor-hairline; the 0.5px rings in Linear's surface shadows use the same width"))
put(core, "focusRing.width", tok(px(var("--focus-ring-width", d)), "dimension", "css-var --focus-ring-width, and the measured outline width on every focus-visible state"))
for name, comp_key in (("offset-button", "button-primary"), ("offset-field", "text-field"), ("offset-icon", "icon-button"), ("offset-link", "link")):
    s = state(comp_key, "focus-visible", "dark")
    put(core, f"focusRing.{name}", tok(px(s["style"]["outlineOffset"]), "dimension", f"computed outline-offset of {C[comp_key]['title']} at focus-visible (real keyboard focus), copy {s['snapshot']}"))

for name in ("highlightFadeIn", "quickTransition", "highlightFadeOut", "regularTransition", "slowTransition"):
    put(core, f"duration.{name}", tok(seconds_ms(var(f"--speed-{name}", d)), "duration", f"css-var --speed-{name}, copy issue-dark"))
put(core, "duration.hover", tok("150ms", "duration", "the most common transition on measured components (border, background-color, color, opacity 0.15s ease; 29 states, raw/measurements.md)"))
for name in ("out-quad", "out-cubic", "in-out-cubic", "out-quart", "out-expo"):
    put(core, f"easing.{name}", tok(bezier(var(f"--ease-{name}", d)), "cubicBezier", f"css-var --ease-{name}, copy issue-dark"))
E = V["easings"]
put(core, "easing.default", tok(bezier("ease"), "cubicBezier", f"the CSS keyword ease, the timing function on {E.get('ease', 0)} rules in the bundle (raw/css-vars.json easings)"))
put(core, "easing.out", tok(bezier("ease-out"), "cubicBezier", f"the CSS keyword ease-out, on {E.get('ease-out', 0)} rules in the bundle"))

M = V["media"]
for name, q in (("phone-small", "(max-width: 375px)"), ("phone", "(max-width: 640px)"), ("tablet", "(max-width: 768px)"), ("laptop", "(max-width: 1024px)"), ("wide", "(min-width: 1400px)"), ("ultrawide", "(min-width: 1800px)")):
    width = re.search(r"(\d+)px", q).group(1)
    put(core, f"breakpoint.{name}", tok(f"{width}px", "dimension", f"@media {q} in the app bundle ({M.get(q, 0)} rules)"))

L = V["layers"]["dark"]
for name in ("dialog", "toast", "menu"):
    put(core, f"zIndex.{name}", tok(max(L[name]), "number", f"computed z-index of the {name}'s outermost stacking ancestor, copy {'composer-dark' if name == 'dialog' else 'issue-dark-' + name}; the same in light"))
not_core = [
    {"role": "zIndex.tooltip", "reason": "Not captured: no ancestor of the tooltip sets a z-index in the copy (it stacks by order in <body>)"},
    {"role": "font.letterSpacing.editor", "value": var("--editor-letter-spacing", d), "reason": "an em length; DTCG dimensions are px or rem"},
    {"role": "font.size.*Plus", "reason": "--font-size-microPlus ... --font-size-regularPlus equal their base sizes in this account's Default font size; left out"},
]

# ---------------------------------------------------------------- public site and brand (2026-09-23)

WEB = {"canvas": "#08090A", "surface": "#0F1011", "raised": "#161718", "border": "#24282C", "text": "#F7F8F8", "secondary": "#D0D6E0", "muted": "#8A8F98", "subtle": "#62666D", "primary": "#E5E5E6", "accent": "#5E6AD2"}
BRAND = {"mercury-white": "#F4F5F8", "nordic-gray": "#222326"}
web = {k: tok(v.lower(), "color", "public site computed CSS, evidence/styles/01-home-styles.json, read 2026-09-23", "Measured (public site)") for k, v in WEB.items()}
brand = {k: tok(v.lower(), "color", "https://linear.app/brand, displayed hex (Nordic Gray's RGB prose says 35, 35, 38; the displayed hex is kept)", "Measured (brand page)") for k, v in BRAND.items()}
core["$extensions"] = {"notTokenised": not_core}
for t in THEMES:
    themed[t]["$extensions"] = {"notTokenised": not_tok[t]}

# ---------------------------------------------------------------- checks


def tokens_of(tree, prefix=""):
    for k, v in tree.items():
        if k.startswith("$"):
            continue
        if isinstance(v, dict) and "$value" in v:
            yield prefix + k, v
        elif isinstance(v, dict):
            yield from tokens_of(v, prefix + k + ".")


sets = {"core": core, "dark": themed["dark"], "light": themed["light"], "web": web, "brand": brand}
for sname, tree in sets.items():
    for n, t in tokens_of(tree):
        if not t["$extensions"].get("source") or not t["$extensions"].get("evidence"):
            raise ValueError(f"{sname}.{n} has no source")
        if t["$type"] == "dimension" and not re.fullmatch(r"-?\d*\.?\d+(px|rem)", t["$value"]):
            raise ValueError(f"{sname}.{n}: {t['$value']!r}")
        if t["$type"] == "color" and not re.fullmatch(r"#[0-9a-f]{6}|rgba\(\d+, \d+, \d+, [\d.]+\)", t["$value"]):
            raise ValueError(f"{sname}.{n}: {t['$value']!r}")
dark_names = {n for n, _ in tokens_of(themed["dark"])}
light_names = {n for n, _ in tokens_of(themed["light"])}
if dark_names != light_names:
    raise ValueError(f"themes differ: {sorted(dark_names ^ light_names)}")

tokens = {
    "core": core, "dark": themed["dark"], "light": themed["light"], "web": web, "brand": brand,
    "$themes": [
        {"id": "dark", "name": "Dark", "selectedTokenSets": {"core": "source", "dark": "enabled"}, "$description": "Settings > Preferences > Interface theme: Dark (the account's theme; every dark copy)"},
        {"id": "light", "name": "Light", "selectedTokenSets": {"core": "source", "light": "enabled"}, "$description": "Interface theme: Light, switched for the light copies on 2026-10-17 with the owner's agreement and set back to Dark"},
    ],
    "$metadata": {"tokenSetOrder": ["core", "dark", "light", "web", "brand"]},
}
out = HERE / "tokens"
(out / "linear.tokens.json").write_text(json.dumps(tokens, indent=2, ensure_ascii=False) + "\n")

# Tokens Studio: one set per group, plain values.


def studio(tree):
    o = {}
    for k, v in tree.items():
        if k.startswith("$"):
            continue
        if isinstance(v, dict) and "$value" in v:
            o[k] = {"type": v["$type"], "value": v["$value"], "description": v["$extensions"]["evidence"] + ": " + v["$extensions"]["source"]}
        else:
            o[k] = studio(v)
    return o


(out / "tokens-studio.json").write_text(json.dumps({**{k: studio(v) for k, v in sets.items()}, "$themes": tokens["$themes"], "$metadata": tokens["$metadata"]}, indent=2, ensure_ascii=False) + "\n")


def css_value(t):
    v, ty = t["$value"], t["$type"]
    if ty == "shadow":
        return ", ".join(("inset " if l["inset"] else "") + f"{l['offsetX']} {l['offsetY']} {l['blur']} {l['spread']} {l['color']}" for l in v)
    if ty == "fontFamily":
        return ", ".join(f'"{f}"' if " " in f else f for f in v)
    if ty == "cubicBezier":
        return "cubic-bezier(%s)" % ", ".join("%g" % x for x in v)
    if ty == "typography":
        return None
    return str(v)


def block(sel, tree, prefix):
    lines = [f"  --linear-{prefix}{n.replace('.', '-')}: {css_value(t)};" for n, t in tokens_of(tree) if css_value(t) is not None]
    return sel + " {\n" + "\n".join(lines) + "\n}\n"


(out / "linear.css").write_text("/* Generated by tools/build_tokens.py. Dark is the default; light under [data-theme=\"light\"]. */\n"
                                + block(":root", core, "") + "\n" + block(":root", themed["dark"], "") + "\n" + block('[data-theme="light"]', themed["light"], "")
                                + "\n" + block(":root", web, "web-") + "\n" + block(":root", brand, "brand-")
                                + 'body {font-family: var(--linear-font-family-ui); font-feature-settings: "cv01", "ss03";}\n')
print({k: len(list(tokens_of(v))) for k, v in sets.items()}, "not tokenised:", len(not_core) + len(not_tok["dark"]))
