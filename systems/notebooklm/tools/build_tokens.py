#!/usr/bin/env python3
"""Build tokens.json from the 2026-10-17 readings in raw/.

    python3 tools/build_tokens.py

Inputs (all written by tools/capture/):
  raw/css-vars.json            every --nlm-*, --nb-*, --mat-sys-* variable, resolved on <body> in dark and light
  raw/css-facts.json           media queries, reduced-motion rules, transitions, z-index, grids, fonts, usage counts
  raw/components-computed.json computed styles per component and state, both themes
  raw/brand.json               theme-color meta tags and the web manifest

Output: tokens.json in Tokens Studio's multi-set layout (core, light, dark, $themes). Every token
carries $extensions.source with an evidence label from docs/EVIDENCE.md:
  Measured  read from a declared custom property or a computed style
  Derived   worked out from measured values (a state layer composited over its fill, a ramp ordered
            by lightness, a rem converted to px)
The build fails if a token has no source or if light and dark do not hold the same keys.
"""
import colorsys, json, math, pathlib, re, sys

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
VARS = json.loads((RAW / "css-vars.json").read_text())["vars"]
FACTS = json.loads((RAW / "css-facts.json").read_text())
COMP = json.loads((RAW / "components-computed.json").read_text())["components"]
DATE = "2026-10-17"

# ---------------------------------------------------------------------------------------- helpers

def hexa(c):
    """rgb()/rgba()/color(srgb ...) -> #rrggbb or rgba(r,g,b,a)."""
    if c is None:
        return None
    c = c.strip()
    m = re.match(r"rgba?\(([\d.]+),\s*([\d.]+),\s*([\d.]+)(?:,\s*([\d.]+))?\)", c)
    if m:
        r, g, b = (round(float(x)) for x in m.groups()[:3])
        a = m.group(4)
    else:
        m = re.match(r"color\(srgb ([\d.]+) ([\d.]+) ([\d.]+)(?: / ([\d.]+))?\)", c)
        if not m:
            return c
        r, g, b = (round(float(x) * 255) for x in m.groups()[:3])
        a = m.group(4)
    if a is None or float(a) >= 1:
        return "#%02x%02x%02x" % (r, g, b)
    return "rgba(%d,%d,%d,%s)" % (r, g, b, ("%.2f" % float(a)).rstrip("0").rstrip("."))

def rgb_of(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))

def lab_l(h):
    """CIELAB L* of an sRGB hex, used only to order and name ramp steps."""
    def lin(c):
        c /= 255
        return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4
    r, g, b = (lin(x) for x in rgb_of(h))
    y = 0.2126 * r + 0.7152 * g + 0.0722 * b
    f = y ** (1 / 3) if y > 216 / 24389 else (24389 / 27 * y + 16) / 116
    return 116 * f - 16

def blend(base, layer, alpha):
    """A state layer of colour `layer` at `alpha` painted over the opaque `base`."""
    b, l = rgb_of(base), rgb_of(layer)
    return "#%02x%02x%02x" % tuple(round(l[i] * alpha + b[i] * (1 - alpha)) for i in range(3))

def var(name, theme="dark"):
    v = VARS.get(name, {}).get(theme)
    if not v:
        sys.exit(f"missing variable {name} ({theme})")
    return hexa(v["color"]) if "color" in v else v["raw"]

def comp(key, state="default"):
    s = COMP[key]["states"].get(state)
    if not s or "style" not in s:
        sys.exit(f"missing measurement {key}:{state}")
    return s

def cstyle(key, state, prop):
    return comp(key, state)["style"][prop]

def paint(key, state, node_pat, field):
    for p in comp(key, state).get("paint", []):
        if re.search(node_pat, p["node"]) and p.get(field):
            return p[field]
    sys.exit(f"no paint {node_pat}.{field} on {key}:{state}")

def px(v):
    """'1.25rem' -> '20px'; '12px' -> '12px'."""
    v = str(v).strip()
    m = re.match(r"^(-?[\d.]+)rem$", v)
    if m:
        n = float(m.group(1)) * 16
        return f"{int(n) if n == int(n) else round(n, 2)}px"
    return v

def T(value, type_, source, desc=None, **ext):
    t = {"$value": value, "$type": type_}
    if desc:
        t["$description"] = desc
    t["$extensions"] = {"source": source, **ext}
    return t

def M(src):
    return f"Measured: {src}"

def D(src):
    return f"Derived: {src}"

ST = lambda theme: "default" if theme == "dark" else "light"
SS = lambda theme, s: s if theme == "dark" else f"light-{s}"

# ------------------------------------------------------------------------------------- core: palettes

core = {"palette": {}}

def declared_ramp(prefix, steps):
    out = {}
    for s in steps:
        n = f"{prefix}-{s}"
        raw = VARS.get(n, {}).get("dark", {})
        if "color" not in raw:
            continue
        out[str(s)] = T(hexa(raw["color"]), "color", M(f"css-var {n}"))
    return out

core["palette"]["grey"] = declared_ramp("--nlm-grey", [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 95, 98, 100])
core["palette"]["blue"] = declared_ramp("--nlm-blue", [2, 5, 10, 20, 30, 40, 50, 60, 70, 80, 90, 95, 98, 100])
core["palette"]["green"] = declared_ramp("--nlm-green", [50, 60, 70, 80, 100])
for t in core["palette"]["green"].values():
    t["$description"] = "--nlm-green-0 to -40 and -90 to -99 are declared with the value `undefined` in the product's CSS, so only these steps exist. The step names are not tones (-50 is tone 83); the green hue's full ramp is palette.green-status."

def assembled(name, members, desc):
    """A ramp per hue from every value the product declares for that hue, ordered by L*.
    Steps are named by rounded CIELAB L* (0 black to 100 white); the first declaration wins a name."""
    seen, out = {}, {}
    for var_name, theme in members:
        h = var(var_name, theme)
        if not h or not h.startswith("#"):
            continue
        step = str(round(lab_l(h)))
        if step in out or h in seen:
            continue
        seen[h] = step
        out[step] = T(h, "color", M(f"css-var {var_name} ({theme})") + "; " + D("ramp step named by CIELAB L*"), desc)
    return dict(sorted(out.items(), key=lambda kv: int(kv[0])))

both = lambda names: [(n, th) for n in names for th in ("light", "dark")]
core["palette"]["neutral"] = assembled("neutral", both([
    "--nb-sys-color--white", "--nb-sys-color--surface-background", "--nb-sys-color--surface", "--nb-sys-color--surface-dim",
    "--nb-sys-color--on-surface", "--nlm-grey-95", "--nlm-grey-90", "--nlm-grey-80", "--nlm-grey-70", "--nlm-grey-60",
    "--nlm-grey-50", "--nlm-grey-40", "--nlm-grey-30", "--nlm-grey-20", "--nb-sys-color--surface-bright", "--nlm-grey-10",
    "--nb-sys-color--black"]), "Neutral used by the luminous UI: the nb-sys surface and text greys merged with the --nlm-grey ramp.")
# The other hues have no declared ramp, only role colours on Material 3 tones. Each ramp is the
# Material tonal palette of a measured seed (tools/capture/tonal-ramps.mjs, raw/tonal-ramps.json):
# steps the product paints keep the measured value, the rest are the generated tone.
TONAL = json.loads((HERE / "raw" / "tonal-ramps.json").read_text())
def tonal(name):
    r = TONAL["ramps"][name]
    seed = r["seed"]
    out = {}
    for step, st in r["steps"].items():
        if st.get("extra"):
            src = M(f"css-var {st['var']} ({st['theme']})") + f"; extra step at its own Material tone {step}, between the standard tones"
        elif st["source"] == "measured":
            src = M(f"css-var {st['var']} ({st['theme']})") + f"; on Material tone {step} (generated {st['generated']}, RGB distance {st['rgbDistance']})"
        else:
            src = D(f"Material tonal palette tone {step} of the seed {seed['var']} {seed['hex']}, built with material-color-utilities; the product declares no colour at this tone")
        out[step] = T(st["hex"], "color", src, r["description"])
    return out
for name in ("red", "orange", "amber", "yellow", "green-status", "cyan", "sky", "info", "purple", "pink"):
    core["palette"][name] = tonal(name)
core["palette"]["brand"] = {k: T(var(f"--nlm-brand-{k}"), "color", M(f"css-var --nlm-brand-{k}")) for k in ("black", "white", "green", "blue", "dark-blue")}
core["palette"]["icon"] = {k: T(var(f"--nlm-icons-{v}"), "color", M(f"css-var --nlm-icons-{v}")) for k, v in
                           (("blue", "blue"), ("yellow", "yellow"), ("red", "red"), ("pink", "pink"), ("green", "green"), ("youtube", "youtube"))}

# -------------------------------------------------------------------------------------- core: type

stack_sans = [s.strip().strip('"') for s in var("--nlm-font-family-sans").split(",")]
stack_text = [s.strip().strip('"') for s in var("--mat-sys-body-medium-font").split(",")]
code_stack = [s.strip().strip('"') for s in re.split(r",\s*", comp("type-code")["style"]["fontFamily"])]
icon_stack = [s.strip().strip('"') for s in re.split(r",\s*", comp("menu")["iconStyle"]["fontFamily"])]
core["fontFamily"] = {
    "display": T(stack_sans, "fontFamily", M("css-var --nlm-font-family-sans"), "Google Sans Flex, a variable font (wght 100-1000, wdth, opsz, ROND axes), loaded from fonts.gstatic.com. The stack is the product's own."),
    "text": T(stack_text, "fontFamily", M("css-var --mat-sys-body-medium-font"), "Material's text roles name Google Sans Text second."),
    "code": T(code_stack, "fontFamily", M("computed font-family of inline code in a chat answer (code.code)"), "Google Sans Code from Google Fonts."),
    "icon": T(icon_stack, "fontFamily", M("computed font-family of a mat-icon in the card menu"), "Luminous Symbols first, then Google Symbols and Material Symbols Outlined, all ligature icon fonts."),
    "math": T(["KaTeX_Main", "Times New Roman", "serif"], "fontFamily", M("@font-face KaTeX_* from www.gstatic.com; serif fallback is KaTeX's own"), "Formulae in answers."),
}

SCALE = "--nb-sys-typography-type-scale--"
weights = set()
def role(r, family="display", base=SCALE, desc=None):
    size = px(var(f"{base}{r}-font-size"))
    lh = px(var(f"{base}{r}-line-height"))
    w = int(var(f"{base}{r}-font-weight"))
    tr = px(var(f"{base}{r}-font-tracking"))
    weights.add(w)
    # The captured settings are already CSS ("wdth" 100), so they are joined as they are.
    axes = [var(f"{base}{r}-{axis}") for axis in ("font-width", "opsz", "font-rond") if f"{base}{r}-{axis}" in VARS]
    return T({"fontFamily": "{fontFamily.%s}" % family, "fontSize": size, "fontWeight": w, "lineHeight": lh,
              "letterSpacing": tr if tr not in ("0", "0rem") else "0px"}, "typography",
             M(f"css-vars {base}{r}-font-size/-line-height/-font-weight/-font-tracking"), desc,
             fontVariationSettings=", ".join(axes) or None)

typo = {}
for name, r in (("display-large", "display-l"), ("display-medium", "display-m"), ("display-small", "display-s"),
                ("headline-large", "headline-l"), ("headline-medium", "headline-m"), ("headline-small", "headline-s"),
                ("title-large", "title-l"), ("title-medium", "title-m"), ("title-small", "title-s"),
                ("body-large", "body-l"), ("body-medium", "body-m"), ("body-small", "body-s"),
                ("label-large", "label-l"), ("label-medium", "label-m"), ("label-small", "label-s")):
    typo[name] = role(r)
typo["body-medium-strong"] = role("body-m", base="--nb-sys-typography-type-scale-emphasized--", desc="Emphasised body, used for <b> in answers.")
typo["caption"] = role("caption", family="code", base="--nb-sys-typography-type-scale-extended--", desc="The extended scale's caption is Google Sans Code italic. The card meta line uses body-small instead (see type-caption in components.md).")
typo["code-inline"] = role("code", family="code", base="--nb-sys-typography-type-scale-extended--", desc="Inline and block code in answers.")
typo["answer-heading"] = role("h-3", base="--nb-sys-typography-markdown-type-scale--", desc="Markdown h3 in a chat answer (measured on .paragraph.heading3).")
ph = comp("type-panel-header")["style"]
typo["panel-header"] = T({"fontFamily": "{fontFamily.display}", "fontSize": ph["fontSize"], "fontWeight": int(float(ph["fontWeight"])), "lineHeight": ph["lineHeight"], "letterSpacing": "0px" if ph["letterSpacing"] == "normal" else ph["letterSpacing"]},
                         "typography", M("computed style of the Sources panel header"), "Panel titles (Sources, Chat, Studio).")
weights.add(int(float(ph["fontWeight"])))
core["typography"] = typo
core["fontWeight"] = {str(w): T(w, "fontWeight", M("the --nb-sys-typography-* weights; the font is variable, so any weight renders")) for w in sorted(weights)}
sizes = sorted({float(t["$value"]["fontSize"].rstrip("px")) for t in typo.values()})
core["fontSize"] = {(str(int(s)) if s == int(s) else str(s)): T(f"{int(s) if s == int(s) else s}px", "dimension", D("the distinct sizes of the typography roles, converted from rem")) for s in sizes}

# ------------------------------------------------------------------------------- core: shape, space, size

SH = "--nb-sys-shape--corner-"
core["radius"] = {k: T(px(var(SH + v)), "dimension", M(f"css-var {SH}{v}")) for k, v in (
    ("none", "none"), ("xs", "extra-small"), ("sm", "small"), ("md", "medium"), ("lg", "large"), ("lg-increased", "large-increased"),
    ("lg-max", "large-max"), ("xl", "extra-large"), ("xl-increased", "extra-large-increased"), ("xl-max", "extra-large-max"),
    ("xxl", "extra-extra-large"), ("xxl-increased", "extra-extra-large-increased"), ("full", "full"))}
core["radius"]["button"] = T(cstyle("button-accent", "default", "borderTopLeftRadius"), "dimension", M("computed border-radius of nb-buttons (New notebook, Add sources, Create notebook)"), "Every nb-button is a pill.")
core["radius"]["card"] = T(cstyle("card", "default", "borderTopLeftRadius"), "dimension", M("computed border-radius of the notebook card"))
core["radius"]["panel"] = T(cstyle("panel-sources", "default", "borderTopLeftRadius"), "dimension", M("computed border-radius of the Sources panel"))
core["radius"]["dialog"] = T(cstyle("dialog", "default", "borderTopLeftRadius"), "dimension", M("computed border-radius of .mat-mdc-dialog-surface"))
core["radius"]["menu"] = T(cstyle("menu", "default", "borderTopLeftRadius"), "dimension", M("computed border-radius of .mat-mdc-menu-panel"))
core["radius"]["menu-item"] = T(cstyle("menu", "item-hover", "borderTopLeftRadius"), "dimension", M("computed border-radius of a hovered menu item"))
core["radius"]["tooltip"] = T(cstyle("tooltip", "default", "borderTopLeftRadius"), "dimension", M("computed border-radius of the tooltip surface"))
core["radius"]["toast"] = T(cstyle("toast", "default", "borderTopLeftRadius"), "dimension", M("computed border-radius of the snackbar surface"))
core["radius"]["chat-bubble"] = T(cstyle("chat-bubble", "default", "borderTopLeftRadius"), "dimension", M("computed border-radius of the user chat bubble"))
core["radius"]["list-row"] = T(cstyle("list-row", "default", "borderTopLeftRadius"), "dimension", M("computed border-radius of a source row"))
core["radius"]["dialog-button"] = T(cstyle("button-dialog-primary", "default", "borderTopLeftRadius"), "dimension", M("computed border-radius of the mdc buttons in dialogs (Save, Insert): Material's 6rem container shape"))
core["radius"]["circle"] = T("50%", "dimension", M("computed border-radius of avatars, checkbox and radio touch targets"))
core["radius"]["composer"] = T(cstyle("text-area", "default", "borderTopLeftRadius"), "dimension", M("computed border-radius of the chat composer"))

core["borderWidth"] = {
    "hairline": T(cstyle("button-outlined", "default", "borderTopWidth"), "dimension", M("computed border of the outlined button and the empty-state panel")),
    "field": T("1px", "dimension", M("computed outline of the outlined text area at rest and in error (.mdc-notched-outline)")),
    "field-focus": T("2px", "dimension", M("computed outline of the outlined text area and text field with keyboard focus")),
    "focus-ring": T(cstyle("button-accent", "focus-visible", "outlineWidth"), "dimension", M("computed outline of nb-buttons with keyboard focus")),
}
SP = "--nb-sys-spacing--"
core["spacing"] = {}
for k in ("xxs", "xs", "s", "m", "l", "xl", "xxl", "xxxl"):
    v = px(var(SP + k))
    core["spacing"][v.rstrip("px")] = T(v, "dimension", M(f"css-var {SP}{k}"), f"nb-sys spacing {k}.")
for k in ("container-padding-small", "container-padding-medium", "container-padding-large", "widget-gap", "space-above"):
    v = px(var(SP + k))
    core["spacing"][k] = T(v, "dimension", M(f"css-var {SP}{k}"))

def h(key, st="default"):
    return f'{round(comp(key, st)["rect"]["h"])}px'
def w(key, st="default"):
    return f'{round(comp(key, st)["rect"]["w"])}px'
core["size"] = {
    "control-compact": T(h("tab"), "dimension", M("computed height of the header nb-buttons (nb-button-size-compact-36)")),
    "control-small": T(h("button-accent"), "dimension", M("computed height of nb-button-size-small (New notebook, Add sources)")),
    "control-dialog": T(h("button-dialog-primary"), "dimension", M("computed height of mdc buttons in dialogs (Save, Upload files)")),
    "control-medium": T(h("button-confirm-delete"), "dimension", M("computed height of nb-button-size-medium (Cancel, Delete)")),
    "icon-button": T(h("icon-button"), "dimension", M("computed size of the header icon buttons")),
    "icon-button-small": T(h("icon-button-small"), "dimension", M("computed size of the card actions button")),
    "field": T(h("text-field"), "dimension", M("computed height of the outlined text field (Add people and groups)")),
    "composer": T(h("text-area"), "dimension", M("computed height of the chat composer at one line")),
    "list-row": T(h("list-row"), "dimension", M("computed height of a source row")),
    "list-row-output": T(h("list-row-output"), "dimension", M("computed height of a Studio output row")),
    "table-row": T(h("table-row"), "dimension", M("computed height of a notebook list-view row")),
    "menu-item": T(h("menu", "item-hover"), "dimension", M("computed height of a menu item")),
    "tab-mobile": T(h("mobile-tab"), "dimension", M("computed height of a panel tab at 390")),
    "studio-tile": T(h("studio-tile"), "dimension", M("computed height of a Studio tile")),
    "card-width": T(w("card"), "dimension", M("computed width of a notebook card at 1440 (five columns)")),
    "card-height": T(h("card"), "dimension", M("computed height of a notebook card")),
    "header-height": T(h("header"), "dimension", M("computed height of the page header")),
    "checkbox-target": T(h("checkbox"), "dimension", M("computed size of mat-checkbox's touch box")),
    "switch-width": T(w("switch"), "dimension", M("computed width of the switch")),
    "switch-height": T(h("switch"), "dimension", M("computed height of the switch")),
    "avatar": T(h("avatar"), "dimension", M("computed size of the account avatar link")),
}
IC = "--nb-sys-icon-scale--"
for k in ("s", "m", "l", "xl", "xxl"):
    core["size"][f"icon-{k}"] = T(px(var(f"{IC}{k}-font-size")), "dimension", M(f"css-var {IC}{k}-font-size"))

fr = comp("button-accent", "focus-visible")["style"]
core["focusRing"] = {
    "width": T(fr["outlineWidth"], "dimension", M("computed outline-width on nb-buttons with keyboard focus (New notebook, Create notebook, Settings)")),
    "offset": T(fr["outlineOffset"], "dimension", M("computed outline-offset on the same buttons"), "Outside the control; the ring follows the control's radius."),
    "style": T(fr["outlineStyle"], "other", M("computed outline-style")),
    "field-width": T("2px", "dimension", M("computed outline of a focused outlined field; the field's own outline thickens from 1px to 2px, no separate ring")),
    "checkbox-width": T("3px", "dimension", M("computed border of mat-checkbox's focus indicator (span.mat-focus-indicator::before)")),
}

# ---------------------------------------------------------------------------- core: layout, z, motion

media = FACTS["media"]
def mq(cond):
    return media.get(cond, 0)
core["breakpoint"] = {
    "xs-max": T("359.98px", "dimension", M(f"@media (max-width: 359.98px), {mq('@media (max-width: 359.98px)')} rules")),
    "mobile-max": T("599.98px", "dimension", M(f"@media (max-width: 599.98px), {mq('@media (max-width: 599.98px)')} rules; the most used breakpoint")),
    "tablet": T("600px", "dimension", M("@media (min-width: 600px) and (max-width: 959.98px)")),
    "tablet-max": T("959.98px", "dimension", M("@media (min-width: 600px) and (max-width: 959.98px)")),
    "desktop-min": T("1024px", "dimension", M(f"@media (min-width: 1024px), {mq('@media (min-width: 1024px)')} rules")),
    "wide-max": T("1280px", "dimension", M("@media (max-width: 1280px)")),
}
g = FACTS["grids"]
grid_rule = next(r for r in g["rules"] if "project-buttons-flow" in r["selector"])
core["layout"] = {
    "grid-notebooks": T(grid_rule["value"].replace(",", ", "), "other", M(f"grid-template-columns on {grid_rule['selector'].split('[')[0]}"),
                        "Auto-fill columns of at least --project-card-min-width."),
    "grid-columns-1440": T(g["1440"]["columnsInFirstRow"], "number", M("cards in the first row of the notebook grid at 1440")),
    "grid-columns-1024": T(g["1024"]["columnsInFirstRow"], "number", M("cards in the first row at 1024")),
    "grid-columns-800": T(g["800"]["columnsInFirstRow"], "number", M("cards in the first row at 800")),
    "grid-columns-390": T(g["390"]["columnsInFirstRow"], "number", M("cards in the first row at 390")),
    "panel-sources-width": T(w("panel-sources"), "dimension", M("computed width of the Sources panel at 1440")),
    "panel-chat-width": T(w("panel-chat"), "dimension", M("computed width of the Chat column at 1440")),
    "panel-gutter": T(px(var("--nb-sys-spacing--l")), "dimension", M("css-var --nb-sys-spacing--l, the gap between the three panels")),
    "content-width-home": T(w("table-row"), "dimension", M("computed width of the notebook table at 1440 (page padding 24px each side)")),
    "dialog-width-small": T(w("dialog"), "dimension", M("computed width of the Delete confirmation dialog")),
    "dialog-width-large": T(w("dialog-large"), "dimension", M("computed width of the Configure Chat dialog")),
    "menu-max-width": T(cstyle("menu", "default", "maxWidth"), "dimension", M("computed max-width of .mat-mdc-menu-panel")),
}
zc = FACTS["zIndexComputed"]
core["zIndex"] = {
    "card-actions": T(10, "number", M("z-index on .project-button-box-right (the card's actions above its link)")),
    "google-bar": T(int(zc[".boqOnegoogleliteOgbOneGoogleBar"]), "number", M("computed z-index of the Google account bar")),
    "overlay": T(int(zc[".cdk-overlay-container"]), "number", M("computed z-index of .cdk-overlay-container"), "Dialogs, menus, select panels, tooltips and toasts all mount in this one container and stack by DOM order."),
    "picker": T(1004, "number", M("z-index on .google-picker.modal-dialog (the Drive picker)")),
}
dur = FACTS["motion"]["durations"]
def ms(v):
    return f"{round(float(v[:-2]))}ms" if v.endswith("ms") else f"{round(float(v[:-1]) * 1000)}ms"
core["duration"] = {}
for k, v in (("short", "0.15s"), ("short2", "0.2s"), ("medium", "0.25s"), ("medium2", "280ms"), ("medium3", "0.3s"), ("medium4", "365ms"),
             ("long", "0.4s"), ("long2", "0.5s"), ("spinner", "1333ms"), ("shimmer", "1.4s"), ("spinner-cycle", "5332ms")):
    core["duration"][k] = T(ms(v), "duration", M(f"transition/animation durations in the stylesheets, {dur.get(v, 0)} declarations"))
core["duration"]["reduced-motion"] = T("1ms", "duration", M("@media (prefers-reduced-motion) .cdk-overlay-backdrop { transition-duration: 1ms }"), "What overlays fade in under reduced motion.")
eas = FACTS["motion"]["easings"]
core["easing"] = {}
for k, v in (("standard", "cubic-bezier(0.4, 0, 0.2, 1)"), ("decelerate", "cubic-bezier(0, 0, 0.2, 1)"), ("accelerate", "cubic-bezier(0.4, 0, 0.6, 1)"),
             ("emphasized-decelerate", "cubic-bezier(0.05, 0.7, 0.1, 1)"), ("emphasized-accelerate", "cubic-bezier(0.3, 0, 0.8, 0.15)"),
             ("expand", "cubic-bezier(0.2, 0, 0, 1)"), ("backdrop", "cubic-bezier(0.25, 0.8, 0.25, 1)")):
    nums = [float(x) for x in re.findall(r"[\d.]+", v)]
    core["easing"][k] = T(nums, "cubicBezier", M(f"{v} in the stylesheets, {eas.get(v, 0)} declarations"))
core["easing"]["ease"] = T([0.25, 0.1, 0.25, 1], "cubicBezier", M(f"the keyword `ease`, {eas.get('ease', 0)} declarations"), "CSS `ease` written as its curve.")
core["reducedMotion"] = {}
for r in FACTS["reduced"]:
    sel = re.sub(r"\[_ng[\w-]+\]", "", r["selector"]).split(",")[0].strip()
    if not r["css"]:
        continue
    key = re.sub(r"[^a-z0-9]+", "-", sel.lower()).strip("-")[:40]
    core["reducedMotion"][key] = T(r["css"].replace("auto ease 0s 1 normal none running none", "none"), "other",
                                   M(f"{r['media']} {sel}"), "What this element does instead when the system asks for reduced motion.")
core["opacity"] = {
    "hover": T(float(var("--mat-sys-hover-state-layer-opacity")), "number", M("css-var --mat-sys-hover-state-layer-opacity; the button ripple ::before reads 0.08 on hover")),
    "focus": T(float(var("--mat-sys-focus-state-layer-opacity")), "number", M("css-var --mat-sys-focus-state-layer-opacity")),
    "pressed": T(float(var("--mat-sys-pressed-state-layer-opacity")), "number", M("css-var --mat-sys-pressed-state-layer-opacity; the ripple ::before reads 0.12 when held")),
    "dragged": T(float(var("--mat-sys-dragged-state-layer-opacity")), "number", M("css-var --mat-sys-dragged-state-layer-opacity")),
    "disabled-container": T(0.12, "number", M("css-var --nb-sys-color-states--disabled-on-surface (on-surface at 12%)")),
    "disabled-content": T(0.38, "number", M("css-var --nb-sys-color-states--disabled-label-on-surface (on-surface at 38%)")),
    "secondary-text": T(0.55, "number", M("css-var --nb-sys-color--on-surface-variant (on-surface at 55%)")),
}
core["blur"] = {"panel-glass": T("14px", "dimension", M("backdrop-filter: blur(0.875rem) on translucent panels (2026-09-25 read, still declared)"))}

# Shadows are theme-dependent in the luminous UI (the nb level colour is .04 in light, .28 in dark),
# so the shadow levels live in the theme sets; Material's fixed levels stay in core.
def shadow_parts(s):
    parts = []
    for m in re.finditer(r"(rgba?\([^)]*\)) (-?[\d.]+px) (-?[\d.]+px) (-?[\d.]+px)(?: (-?[\d.]+px))?( inset)?", s):
        col, x, y, b, sp, ins = m.groups()
        p = {"color": hexa(col), "offsetX": x, "offsetY": y, "blur": b, "spread": sp or "0px"}
        if ins:
            p["type"] = "innerShadow"
        parts.append(p)
    return parts
for i in range(1, 6):
    raw = var(f"--mat-sys-level{i}")
    parts = []
    for m in re.finditer(r"(-?[\d.]+px) (-?[\d.]+px) (-?[\d.]+px) (-?[\d.]+px) (rgba\([^)]*\))", raw):
        x, y, b, sp, col = m.groups()
        parts.append({"color": hexa(col.replace(",", ", ")), "offsetX": x, "offsetY": y, "blur": b, "spread": sp})
    core.setdefault("shadow", {})[f"m3-level{i}"] = T(parts, "shadow", M(f"css-var --mat-sys-level{i}"))

# ------------------------------------------------------------------------------------- semantic sets

def theme_set(theme):
    st = ST(theme)
    o = {}
    vt = lambda n: var(n, theme)
    o["bg"] = {
        "page": T(hexa(cstyle("header", st, "backgroundColor")), "color", M("computed background of the page header and the Chat column (= --nb-sys-color--surface)")),
        "background": T(vt("--nb-sys-color--surface-background"), "color", M("css-var --nb-sys-color--surface-background")),
        "scrim": T(hexa(cstyle("scrim", st, "backgroundColor")), "color", M("computed background of .cdk-overlay-dark-backdrop behind a dialog"), "--nlm-fills-scrim still declares .6 in dark; the live backdrop is .32 in both themes."),
    }
    o["surface"] = {
        "panel": T(hexa(cstyle("panel-sources", st, "backgroundColor")), "color", M("computed background of the Sources and Studio panels (= --nb-sys-color--surface-bright)")),
        "card": T(hexa(cstyle("card", st, "backgroundColor")), "color", M("computed background of a notebook card (= --nb-sys-color--surface-dim)")),
        "raised": T(hexa(paint("dialog", st, r"^div\.dialog-container", "bg")), "color", M("computed background of div.dialog-container inside .mat-mdc-dialog-surface (= --nb-sys-color--surface-bright)")),
        "dialog": T(hexa(cstyle("dialog", st, "backgroundColor")), "color", M("computed background of .mat-mdc-dialog-surface")),
        "overlay": T(hexa(cstyle("menu", st, "backgroundColor")), "color", M("computed background of .mat-mdc-menu-panel"), "Menus and the select panel."),
        "selected": T(hexa(cstyle("tab", SS(theme, "selected"), "backgroundColor")), "color", M("computed background of the selected header tab (tonal nb-button)"), "Selection is a quiet grey fill, not the accent."),
        "hover": T(hexa(cstyle("list-row", SS(theme, "hover"), "backgroundColor")), "color", M("computed background of a hovered source row")),
        "inverse": T(hexa(cstyle("tooltip", st, "backgroundColor")), "color", M("computed background of the tooltip")),
        "toast": T(hexa(cstyle("toast", st, "backgroundColor")), "color", M("computed background of the snackbar")),
        "empty": T(hexa(cstyle("empty-state", st, "backgroundColor")), "color", M("computed background of the No notebooks found panel")),
        "badge": T(hexa(cstyle("badge-pro", st, "backgroundColor")), "color", M("computed background of the PRO and New! badges")),
        "accent": T(vt("--nb-sys-color--surface-accent"), "color", M("css-var --nb-sys-color--surface-accent")),
        "legacy-panel": T(vt("--nlm-fills-surface-panel"), "color", M("css-var --nlm-fills-surface-panel"), "The 2026-09 panel fill; still declared, no longer painted by the luminous shell."),
        "legacy-page": T(vt("--nlm-fills-surface-page"), "color", M("css-var --nlm-fills-surface-page"), "The 2026-09 lavender page; still declared, no longer painted."),
    }
    o["text"] = {
        "primary": T(vt("--nb-sys-color--on-surface"), "color", M("css-var --nb-sys-color--on-surface; computed colour of button and menu labels")),
        "secondary": T(vt("--nb-sys-color--on-surface-variant"), "color", M("css-var --nb-sys-color--on-surface-variant; computed colour of card meta lines and inactive segments")),
        "title": T(vt("--nlm-text-titles-and-labels"), "color", M("css-var --nlm-text-titles-and-labels; computed colour of the header title")),
        "body": T(vt("--nlm-text-body-text"), "color", M("css-var --nlm-text-body-text; computed colour of answer text and card titles")),
        "disabled": T(vt("--nb-sys-color-states--disabled-label-on-surface"), "color", M("css-var --nb-sys-color-states--disabled-label-on-surface")),
        "disabled-button": T(hexa(cstyle("button-dialog-primary", SS(theme, "disabled"), "color")), "color", M("computed colour of the disabled Save label")),
        "on-accent": T(hexa(cstyle("button-accent", st, "color")), "color", M("computed label colour of the New notebook button")),
        "on-brand": T(hexa(cstyle("button-dialog-primary", st, "color")), "color", M("computed label colour of the blue dialog Save button")),
        "link": T(hexa(cstyle("link", st, "color")), "color", M("computed colour of the Learn more link"), "The same #4259ff in both themes."),
        "inverse": T(hexa(cstyle("tooltip", st, "color")), "color", M("computed text colour of the tooltip")),
        "on-toast": T(hexa(comp("toast", st)["textStyle"]["color"]), "color", M("computed text colour of the snackbar label")),
        "ghost": T(vt("--nlm-text-ghost-text"), "color", M("css-var --nlm-text-ghost-text")),
        "warning": T(vt("--nlm-text-warning"), "color", M("css-var --nlm-text-warning")),
        "error": T(hexa(cstyle("error-text", st, "color")), "color", M("computed colour of the field error message")),
        "placeholder": T(hexa(comp("text-area", st)["textStyle"]["color"]), "color", M("computed colour of the composer's source-count label, the same as its placeholder (= --nlm-text-secondary-text)")),
    }
    o["border"] = {
        "default": T(hexa(cstyle("button-outlined", st, "borderTopColor")), "color", M("computed border of the outlined button (= --nb-sys-color--on-surface-low)")),
        "divider": T(re.search(r"rgb\([^)]*\)", paint("table-row", st, "td|tr", "border")).group(0) and hexa(re.search(r"rgb\([^)]*\)", paint("table-row", st, "td|tr", "border")).group(0)), "color", M("computed bottom border of list-view table cells")),
        "strong": T(vt("--nlm-stroke-focus"), "color", M("css-var --nlm-stroke-focus")),
        "subtle": T(vt("--nlm-stroke-default"), "color", M("css-var --nlm-stroke-default; computed border of the empty-state panel")),
        "field": T(hexa(re.search(r"rgb\([^)]*\)", paint("text-area-outlined", SS(theme, "focus-visible"), "notch|outline|div|span", "border")).group(0)), "color", M("computed outline of the outlined text area on hover (1px) and with keyboard focus (2px); at rest it is border.subtle")),
        "focus": T(hexa(cstyle("button-accent", SS(theme, "focus-visible"), "outlineColor")), "color", M("computed outline colour of nb-buttons with keyboard focus (on-surface)")),
        "focus-strong": T(vt("--nlm-strong-focus-indicator"), "color", M("css-var --nlm-strong-focus-indicator; the computed focus ring of checkboxes, links and Material toggles"), "The second focus colour: lavender in dark, brand blue in light."),
        "error": T(hexa(re.search(r"rgb\([^)]*\)", paint("text-area-outlined", SS(theme, "error"), "notch|outline|div|span", "border")).group(0)), "color", M("computed outline of the URL text area in its error state")),
        "divider-material": T(vt("--mat-sys-surface-variant"), "color", M("css-var --mat-sys-surface-variant; computed colour of mat-divider in dialogs")),
    }
    acc = hexa(cstyle("button-accent", st, "backgroundColor"))
    layer = hexa(paint("button-accent", st, "ripple", "bg"))
    brand = hexa(cstyle("button-dialog-primary", st, "backgroundColor"))
    blayer = hexa(paint("button-dialog-primary", st, "ripple|before", "bg"))
    o["accent"] = {
        "default": T(acc, "color", M("computed background of the New notebook button (= --nb-sys-color-acc-color--accent)")),
        "hover": T(blend(acc, layer, 0.08), "color", D(f"the button's state layer ({layer}) at the measured hover opacity 0.08 over {acc}")),
        "pressed": T(blend(acc, layer, 0.12), "color", D(f"the same layer at the measured pressed opacity 0.12")),
        "on-accent": T(hexa(cstyle("button-accent", st, "color")), "color", M("computed label colour of the New notebook button")),
        "container": T(vt("--nb-sys-color-acc-color--accent-container"), "color", M("css-var --nb-sys-color-acc-color--accent-container")),
        "fixed": T(vt("--nb-sys-color-acc-color--accent-fixed"), "color", M("css-var --nb-sys-color-acc-color--accent-fixed")),
        "brand": T(brand, "color", M("computed background of the blue Save button in dialogs (= --nlm-ctas-buttons-primary)"), "The 2026-09 brand blue, kept for dialog confirm buttons and links."),
        "brand-hover": T(blend(brand, blayer, 0.08), "color", D(f"the Save button's state layer ({blayer}) at 0.08 over {brand}")),
        "brand-pressed": T(blend(brand, blayer, 0.12), "color", D(f"the same layer at 0.12")),
        "chip-selected": T(hexa(comp("radio", SS(theme, "selected"))["ancestors"][0]["bg"]), "color", M("computed background of the checked mat-button-toggle (Configure Chat)")),
    }
    hov = vt("--nb-sys-color-states--hover-on-surface")
    o["state"] = {
        "hover-on-surface": T(hov, "color", M("css-var --nb-sys-color-states--hover-on-surface; computed fill of a hovered menu item")),
        "focus-on-surface": T(vt("--nb-sys-color-states--focus-on-surface"), "color", M("css-var --nb-sys-color-states--focus-on-surface")),
        "pressed-on-surface": T(vt("--nb-sys-color-states--pressed-on-surface"), "color", M("css-var --nb-sys-color-states--pressed-on-surface")),
        "disabled-container": T(hexa(cstyle("button-dialog-primary", SS(theme, "disabled"), "backgroundColor")), "color", M("computed background of the disabled Save button")),
        "disabled-content": T(hexa(cstyle("button-dialog-primary", SS(theme, "disabled"), "color")), "color", M("computed label of the disabled Save button")),
        "drag-over": T(vt("--nlm-states-drag-over"), "color", M("css-var --nlm-states-drag-over")),
        "brand-layer": T(hexa(paint("button-dialog-primary", st, "ripple|before", "bg")), "color", M("computed state-layer colour of the blue dialog button (= --mat-sys-on-primary)")),
    }
    chip_bg = hexa(cstyle("status-chip", st, "backgroundColor"))
    chip_fg = hexa(cstyle("status-chip", st, "color"))
    o["status"] = {
        "danger": {
            "fill": T(chip_bg, "color", M("computed background of the Blocked by browser chip (Notifications dialog)")),
            "text": T(chip_fg, "color", M("computed text colour of the same chip")),
            "border": T(hexa(re.search(r"rgb\([^)]*\)", paint("text-area-outlined", SS(theme, "error"), "notch|outline|div|span", "border")).group(0)), "color", M("computed outline of the URL field in its error state (= --mat-sys-error)")),
            "solid": T(vt("--nb-sys-color--error"), "color", M("css-var --nb-sys-color--error")),
        },
        "success": {
            "fill": T(vt("--nb-sys-color--positive-container"), "color", M("css-var --nb-sys-color--positive-container"), "Declared; no success message appeared in the capture."),
            "text": T(vt("--nb-sys-color--on-positive-container"), "color", M("css-var --nb-sys-color--on-positive-container")),
            "border": T(vt("--nb-sys-color--positive"), "color", M("css-var --nb-sys-color--positive (the solid role, used here as the border)")),
        },
        "warning": {
            "fill": T(vt("--nlm-fills-ui-caution-subtle"), "color", M("css-var --nlm-fills-ui-caution-subtle"), "Declared; no warning appeared in the capture."),
            "text": T(vt("--nlm-text-warning"), "color", M("css-var --nlm-text-warning")),
            "border": T(vt("--mat-sys-warning"), "color", M("css-var --mat-sys-warning (the solid role, used here as the border)")),
        },
        "info": {
            "fill": T(vt("--mat-sys-info-container"), "color", M("css-var --mat-sys-info-container"), "Declared; no info message appeared in the capture."),
            "text": T(vt("--mat-sys-on-info-container"), "color", M("css-var --mat-sys-on-info-container")),
            "border": T(vt("--mat-sys-info"), "color", M("css-var --mat-sys-info (the solid role, used here as the border)")),
        },
    }
    o["tile"] = {}
    for c in ("blue", "green", "yellow", "orange", "pink", "cyan", "grey"):
        o["tile"][c] = {"bg": T(vt(f"--nlm-tiles-{c}"), "color", M(f"css-var --nlm-tiles-{c}")),
                        "fg": T(vt(f"--nlm-tiles-on-{c}"), "color", M(f"css-var --nlm-tiles-on-{c}")),
                        "hover": T(vt(f"--nlm-tiles-on-{c}-hover"), "color", M(f"css-var --nlm-tiles-on-{c}-hover"))}
    o["pastel"] = {c: T(vt(f"--nlm-pastel-{c}"), "color", M(f"css-var --nlm-pastel-{c}")) for c in ("purple", "green", "yellow", "orange", "pink", "blue")}
    o["dataviz"] = {}
    for c in ("blue", "red", "yellow", "green", "orange", "pink", "purple", "cyan", "grey"):
        o["dataviz"][c] = T(vt(f"--mat-sys-{c}"), "color", M(f"css-var --mat-sys-{c}"))
        o["dataviz"][f"{c}-container"] = T(vt(f"--mat-sys-{c}-container"), "color", M(f"css-var --mat-sys-{c}-container"))
    o["skeleton"] = {
        "base": T(vt("--nlm-skeleton-shimmer-base"), "color", M("css-var --nlm-skeleton-shimmer-base")),
        "highlight": T(vt("--nlm-skeleton-shimmer-highlight"), "color", M("css-var --nlm-skeleton-shimmer-highlight")),
        "loading-highlight": T(vt("--nlm-loading-shimmer-highlight"), "color", M("css-var --nlm-loading-shimmer-highlight")),
    }
    o["icon"] = {
        "default": T(vt("--nb-sys-color--on-surface"), "color", M("computed colour of header and menu icons (on-surface)")),
        "secondary": T(vt("--nb-sys-color--on-surface-variant"), "color", M("computed colour of inactive segmented-control icons")),
        "source-pdf": T(hexa(comp("list-row", st)["iconStyle"]["color"]), "color", M("computed colour of the PDF icon in a source row (= --nlm-icons-red)")),
    }
    o["studio"] = {c: T(vt(f"--nb-studio-accent-{c}"), "color", M(f"css-var --nb-studio-accent-{c}"), "Icon colour of one Studio output type (the tile and its list row).") for c in ("blue", "green", "pink", "purple", "teal", "warm")}
    o["studio"]["new-dot"] = T(vt("--nb-studio-new-dot"), "color", M("css-var --nb-studio-new-dot"))
    o["code"] = {k: T(vt(f"--nb-sys-color--code-{v}"), "color", M(f"css-var --nb-sys-color--code-{v}")) for k, v in (
        ("background", "background"), ("text", "primary-text"), ("blue", "blue-text"), ("green", "green-text"), ("pink", "pink-text"),
        ("purple", "purple-text"), ("red", "red-text"), ("yellow", "yellow-text"), ("grey", "grey-text"))}
    # Elevation: each level is tied to the components measured with it.
    lv1 = vt("--nb-sys-elevation--level1")
    lv2 = vt("--nb-sys-elevation--level2")
    o["shadow"] = {
        "none": T([{"color": "rgba(0,0,0,0)", "offsetX": "0px", "offsetY": "0px", "blur": "0px", "spread": "0px"}], "shadow",
                  M("computed box-shadow none on notebook cards, panels and dialog surfaces"), "Level 0: cards, panels and dialogs separate by fill, not shadow."),
        "level1": T(shadow_parts(cstyle("menu", st, "boxShadow")), "shadow", M(f"computed box-shadow of .mat-mdc-menu-panel, the chat composer and the Studio banner (= --nb-sys-elevation--level1: {lv1})"),
                    "Floating surfaces: menus, the composer, banners."),
        "level2": T([{"color": hexa(m.group(1)), "offsetX": "0px", "offsetY": "0px", "blur": "20px", "spread": "0px"} for m in [re.search(r"(rgba\([^)]*\))", lv2.replace(",", ", "))]], "shadow",
                    M(f"css-var --nb-sys-elevation--level2 ({lv2})"), "Declared; no captured component used it."),
        "select": T(shadow_parts(cstyle("select", SS(theme, "open"), "boxShadow")), "shadow", M("computed box-shadow of the open select panel (Material level 3 tones)")),
        "toast": T(shadow_parts(cstyle("toast", st, "boxShadow")), "shadow", M("computed box-shadow of the snackbar (= --mat-sys-level3)")),
    }
    o["gradient"] = {"live-badge": T(vt("--nlm-gradients-live-updates-badge") if "color" not in VARS["--nlm-gradients-live-updates-badge"][theme] else VARS["--nlm-gradients-live-updates-badge"][theme]["raw"], "gradient", M("css-var --nlm-gradients-live-updates-badge"))}
    return o

light, dark = theme_set("light"), theme_set("dark")

# ------------------------------------------------------------------------------------------ checks

def flat(node, prefix=""):
    for k, v in node.items():
        if k.startswith("$"):
            continue
        if isinstance(v, dict) and "$value" in v:
            yield prefix + k, v
        elif isinstance(v, dict):
            yield from flat(v, prefix + k + ".")

lk, dk = {k for k, _ in flat(light)}, {k for k, _ in flat(dark)}
if lk != dk:
    sys.exit(f"theme key mismatch: {sorted(lk ^ dk)}")
for set_name, s in (("core", core), ("light", light), ("dark", dark)):
    for k, t in flat(s):
        if not t.get("$extensions", {}).get("source"):
            sys.exit(f"{set_name}.{k} has no source")
        if t["$value"] in (None, "", "undefined"):
            sys.exit(f"{set_name}.{k} has no value")
        for kk in [x for x, v in t["$extensions"].items() if v is None]:
            del t["$extensions"][kk]

out = {
    "core": core, "light": light, "dark": dark,
    "$themes": [{"id": "light", "name": "Light", "selectedTokenSets": {"core": "source", "light": "enabled"}},
                {"id": "dark", "name": "Dark", "selectedTokenSets": {"core": "source", "dark": "enabled"}}],
    "$metadata": {"tokenSetOrder": ["core", "light", "dark"], "captured": DATE,
                  "source": "notebook.google.com, signed in, luminous UI generation; see README.md"},
}
(HERE / "tokens.json").write_text(json.dumps(out, indent=2, ensure_ascii=False) + "\n")
n = sum(1 for _ in flat(core)) + len(lk) * 2
print(f"wrote tokens.json: {sum(1 for _ in flat(core))} core + {len(lk)} per theme = {n} tokens")
