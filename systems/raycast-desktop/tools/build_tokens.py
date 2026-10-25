#!/usr/bin/env python3
"""Build tokens.json (W3C DTCG, Tokens Studio multi-set layout) and raw/pixel-check.json.

    python3 tools/build_tokens.py

Adapted from the native kit (systems/grokbot). Raycast 2.9's windows are web views, and the app
ships the stylesheets and theme definitions they use. tools/capture/read_bundle.py copied the
declarations out of the installed bundle into raw/, and every colour, size and type value here
comes from them unless it says otherwise:

  bundled-themes.json   Raycast Dark and Raycast Light: 13 base colours each (`theme.*`). Measured:
                        the product's own declared values, in the shipped frontend chunk.
  css-tokens.json       The token stylesheet: radii, spacing, font sizes and weights, icon sizes,
                        blur, easing, focus ring, window sizes, and the semantic colour roles, each a
                        base colour at an alpha (`--color-text-secondary: var(--fg-60)` and
                        `--fg-60: rgb(from var(--fg) r g b / 60%)`). The alpha steps are worked out
                        here as #RRGGBBAA (Derived from the declaration, which names both inputs).
  text-styles.json      The Text component's named styles (core.typography).
  components-css.json   Component rules: heights, paddings, radii, state colours (component.*).
  readings.json         Pixel readings (tools/measure.py): the painted window fills, which the
                        declarations cannot give (the window is translucent over the macOS window
                        material), the list row height (set inline by script), and the pixel check.

The pixel check: each translucent role is composited over the fill it sits on in the capture and
compared with the pixel. raw/pixel-check.json lists both; the build fails if any differs by more
than 2 per channel, so a bundle that no longer matches the captures cannot be committed silently.

The builder refuses a token without a source, an alias that points at nothing, a colour that is not
#RRGGBB(AA), a dimension that is not one px length, and a light and dark set whose keys differ.
Standard library only. Deterministic: the same inputs give the same bytes.
"""
import json
import pathlib
import re

PKG = pathlib.Path(__file__).resolve().parent.parent
RAW = PKG / "raw"


def _load(name):
    p = RAW / name
    return json.loads(p.read_text()) if p.exists() else None


READ = _load("readings.json") or {}  # empty in the kit copy, for its tests
THEMES_FILE = _load("bundled-themes.json")
CSS = _load("css-tokens.json")
TEXT = _load("text-styles.json")
COMPONENTS = _load("components-css.json")
MEASURED = f"raw/{PKG.name}-measured.md"
NAMES = {"dark": "Raycast Dark", "light": "Raycast Light"}
INTER_CAP = 0.727   # Inter's cap height / em, the assumption behind a size Derived from a capital


class Missing(Exception):
    pass


def rd(rid, theme="dark"):
    try:
        return READ[rid][theme]
    except KeyError:
        raise Missing(f"no reading {rid} for {theme}")


def tok(value, typ, desc, evidence, capture, **more):
    src = {"evidence": evidence, "capture": capture}
    src.update(more)
    return {"$value": value, "$type": typ, "$description": desc, "$extensions": {"source": src}}


def px(v):
    return f"{v:g}px"


def pt_of(rid, theme="dark", index=0):
    v = rd(rid, theme)["value"].rstrip("pt")
    return float(v.split("x")[index])


def alias(path, typ, desc, capture="raw/css-tokens.json"):
    return tok("{" + path + "}", typ, desc, "Derived", capture)


# ---------------------------------------------------------------- the declarations

def decl(name, selector=":root", media=""):
    """The value of one custom property in the token stylesheet, under one selector."""
    hits = [d for d in CSS["declarations"] if d["name"] == name and d["selector"] == selector and d["media"] == media]
    if len(hits) != 1:
        raise Missing(f"{name} on {selector!r} ({media!r}): {len(hits)} declarations")
    return hits[0]["value"]


def css(name, desc, typ="dimension", selector=":root", media="", value=None):
    """A token whose value is a declaration in the token stylesheet (Measured)."""
    raw = decl(name, selector, media)
    return tok(value if value is not None else raw, typ, f"{desc} Declared `{name}: {raw}` on `{selector}`" + (f" in `{media}`" if media else "") + ".",
               "Measured", "raw/css-tokens.json", file=CSS["file"], declaration=name)


def scaled(name, desc, selector=".scaled-tokens"):
    """A `round(calc(N * var(--spx)), 1px)` declaration: N px at the owner's zoom of 1."""
    raw = decl(name, selector)
    m = re.fullmatch(r"round\(calc\((\d+(?:\.\d+)?) \* var\(--spx\)\), 1px\)", raw) or re.fullmatch(r"var\(--space-(\d+)\)", raw)
    if not m:
        raise Missing(f"{name}: not a scaled length ({raw})")
    return css(name, desc + " At the interface size the owner uses, --zoom is 1, so --spx is 1px (the launcher measures 750 pt wide, "
               "as `--main-window-width` gives at zoom 1).", selector=selector, value=px(float(m.group(1))))


def comp(value, typ, desc, module, evidence="Measured"):
    return tok(value, typ, desc, evidence, "raw/components-css.json", module=module)


def theme_obj(theme):
    return next(t for t in THEMES_FILE["themes"] if t["name"] == NAMES[theme])


def hexa(rgb, alpha=1.0):
    r, g, b = (round(c) for c in rgb)
    a = round(alpha * 255)
    return "#{:02X}{:02X}{:02X}".format(r, g, b) + ("" if a == 255 else "{:02X}".format(a))


def rgb_of(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4)), (int(h[6:8], 16) / 255 if len(h) == 8 else 1.0)


def over(top, below):
    (t, a), (b, _) = rgb_of(top), rgb_of(below)
    return hexa(tuple(t[i] * a + b[i] * (1 - a) for i in range(3)))


def mix_white(h, share):
    """color-mix(in srgb, h, white share)."""
    (c, _) = rgb_of(h)
    return hexa(tuple(c[i] * (1 - share) + 255 * share for i in range(3)))


# ---------------------------------------------------------------- core

def core():
    weights = {"regular": "--font-weight-400", "medium": "--font-weight-500", "semibold": "--font-weight-600", "bold": "--font-weight-700"}
    font_weight = {k: css(v, f"Font weight {k}.", "fontWeight", value=int(decl(v))) for k, v in weights.items()}
    font_size = {str(n): scaled(f"--font-size-{n}", f"Font size {n}.") for n in (8, 11, 13, 16, 18, 24)}
    spacing = {str(n): scaled(f"--space-{n}", f"Spacing step {n}.") for n in (2, 4, 6, 8, 12, 16, 24, 32, 40, 48, 56)}
    radius = {str(n): css(f"--radius-{n}", f"Radius {n}.") for n in (2, 4, 6, 8, 10, 12, 16, 18, 20, 26)}
    radius["full"] = css("--radius-full", "Pill and circle radius (switches, badges, the action-bar pills, alert buttons).")
    radius["window"] = css("--radius-window-macos-26", "The window corner on macOS 26, the version this Mac runs (`[macos=\"26\"]:root{--radius-window:var(--radius-window-macos-26)}`; macOS 27 uses 20).")
    radius["listItem"] = tok("10px", "dimension", "List row corner on macOS: the List item passes `{windows:6, macOS: size === 'large' ? 12 : 10}` to its radius helper "
                             "(standard-list-item.namespace-*.js). The corner fit on the selected root row reads "
                             f"{rd('radius.row')['value']} (reading `radius.row`).", "Measured", "raw/readings.json",
                             file="standard-list-item.namespace-*.js")
    icon = {str(n): scaled(f"--icon-{n}", f"Icon size {n}.") for n in (12, 16, 22, 32)}
    blur = {str(i): css(f"--blur-{i}", f"Backdrop blur step {i} (macOS).") for i in (1, 2, 3, 4)}

    def ease(name, desc):
        raw = decl(name)
        nums = [float(x) for x in re.findall(r"-?\d*\.?\d+", raw)]
        return css(name, desc, "cubicBezier", value=nums)

    easing = {"easeOutExpo": ease("--easing-ease-out-expo", "Ease-out expo."),
              "easeOutBack": ease("--easing-ease-out-back", "Ease-out back (overshoots; the macOS 27 glass button press)."),
              "switchThumb": comp([0.16, -0.12, 0.29, 1.31], "cubicBezier", "The switch thumb's slide on macOS (`--switch-thumb-transition: transform .366s cubic-bezier(.16, -.12, .29, 1.31)`).", "switch")}
    duration = {
        "control": comp("150ms", "duration", "Button background and opacity change (`.base-button__root{transition:background-color .15s ease-out,opacity .15s ease-out}`).", "base-button"),
        "switchTrack": comp("216ms", "duration", "Switch track colour on macOS (`--switch-transition: background-color .216s ease-out`).", "switch"),
        "switchThumb": comp("366ms", "duration", "Switch thumb slide on macOS, with easing.switchThumb.", "switch"),
        "toastHoverIn": comp("100ms", "duration", "Toast hover in (`--toast-hover-in-duration:.1s`).", "toast"),
        "toastHoverOut": comp("350ms", "duration", "Toast hover out (`--toast-hover-out-duration:.35s`).", "toast"),
        "reducedMotion": tok("0ms", "duration", f"Under `prefers-reduced-motion: reduce`, {len(CSS['reducedMotion'])} rules across the stylesheets set `transition:none` or "
                             "`animation:none` (spinners, progress bars, the dictation HUD, cloud-sync status, composer panels); there is no global switch, so "
                             "the list, switch and button transitions above still run. Separately, `:root:not(.transitions-ready) *{transition:none!important}` "
                             "keeps a window from animating while it first paints.", "Measured", "raw/css-tokens.json", file="every frontend stylesheet", declaration="reducedMotion"),
        "hotkeyHint": comp("150ms", "duration", "The number-key hint that slides into a list row (`--item-number-hotkey-hint-duration:.15s`, after a .4s delay).", "list"),
    }
    size = {
        "mainWindow": {
            "width": scaled("--main-window-width", "Launcher width.", ":root"),
            "expandedHeight": scaled("--main-window-expanded-height", "Launcher height when expanded (the owner's Window Mode).", ":root"),
            "header": scaled("--main-window-header-height", "Launcher search header on macOS (the selected row's top sits at 64 pt, reading `box.row`).", "[macos]:root"),
            "footer": scaled("--default-window-footer-height", "Window footer (action bar) on macOS.", "[macos]:root"),
        },
        "windowHeader": scaled("--default-window-header-height", "Default window header (Settings, AI Chat, Notes).", ":root"),
        "listRow": tok(px(pt_of("size.row")), "dimension", "Root search row height. Set inline by script (`--list-item-height`), so read from pixels: "
                       f"reading `size.row` {rd('size.row')['value']} in both themes.", "Sampled", rd("size.row")["capture"]),
        "listInset": tok(px((750 - pt_of("box.row", index=0)) / 2), "dimension",
                         f"Gap between the window edge and a row's fill: the selected row is {rd('box.row')['value']} in the 750 pt window (reading `box.row`).",
                         "Sampled", rd("box.row")["capture"]),
        "settingsSidebar": tok(px(pt_of("size.sidebar")), "dimension", "Settings window sidebar: an inset panel 9 pt in from the window edge, "
                               f"reading `size.sidebar` {rd('size.sidebar')['value']}.", "Sampled", rd("size.sidebar")["capture"]),
        "settingsWindow": tok(px(pt_of("size.window.settings")), "dimension", f"Settings window width as it opened (reading `size.window.settings` {rd('size.window.settings')['value']}).",
                              "Sampled", rd("size.window.settings")["capture"]),
        "settingsRow": comp("46px", "dimension", "Settings card row (`.settings-ui__row{min-height:round(calc(46 * var(--spx)), 1px)}`); reading `size.settings.row` "
                            f"{rd('size.settings.row')['value']}.", "settings-ui"),
        "actionBarPill": comp("36px", "dimension", "Action bar pills on macOS (`--action-bar-macos-pill-height`).", "action-bar-ui"),
        "focusRing": css("--focus-ring-width", "Focus ring width on macOS (`--focus-ring: var(--focus-ring-width) solid var(--color-border-focus-ring)`)."),
        "focusRingOffset": comp("2px", "dimension", "Focus ring offset on a switch (`.switch__root:focus-visible{outline-offset:2px}`); text fields and dropdowns draw the ring at 0.", "switch"),
        "hairline": css("--half-pixel", "Hairline on a 2x display (`@media (resolution>=2x){:root{--half-pixel:.5px}}`).", media="@media (resolution>=2x)", value="0.5px"),
        "icon": icon,
        "control": {
            "mini": comp("16px", "dimension", "Mini button (`.base-button__root[data-size=mini]{height:var(--space-16)}`).", "base-button"),
            "small": comp("24px", "dimension", "Small button, text field, dropdown and medium token (`height:var(--space-24)`).", "base-button"),
            "medium": comp("32px", "dimension", "Medium button and default text field and dropdown (`height:var(--space-32)`); the settings sidebar search and selected row measure 32 pt (readings `size.sidebarSearch.h`, `size.sidebar.selected`).", "base-button"),
            "large": comp("40px", "dimension", "Large button (`height:var(--space-40)`).", "base-button"),
            "actionButton": comp("28px", "dimension", "Action bar button on macOS (`[macos] .action-button__button{height:round(calc(28 * var(--spx)), 1px)}`).", "action-button"),
            "kbdSmall": comp("18px", "dimension", "Small key cap.", "shortcut"),
            "kbdMedium": comp("20px", "dimension", "Medium key cap.", "shortcut"),
        },
    }
    fonts = {
        "ui": css("--font-feature-settings-base", "UI face on macOS: `[macos]:root{font-family:InterVariable,system-ui,sans-serif}`; InterVariable is bundled with the app "
                  "(`@font-face{font-family:InterVariable;src:url(./InterVariable.woff2)}`). Font features liga, calt, kern and ss03 are on.",
                  "fontFamily", value=["InterVariable", "Inter", "system-ui", "sans-serif"]),
        "mono": comp(["JetBrainsMono", "JetBrains Mono", "monospace"], "fontFamily", "Monospace face (`.text__font-mono{font-family:JetBrainsMono,monospace}`), bundled as JetBrainsMono-Regular.woff2.", "text"),
    }

    def spacing_of(size_, weight):
        hit = [s for s in TEXT["letterSpacing"] if s["size"] == size_ and s["weight"] == weight]
        if not hit:
            return "0px"
        v = hit[0]["letterSpacing"]
        if v == "0":
            return "0px"
        return px(float(re.fullmatch(r"calc\((-?\.?\d*\.?\d+) \* var\(--spx\)\)", v).group(1)))

    names = {"weight": {400: "regular", 500: "medium", 600: "semibold", 700: "bold"}}
    camel = lambda s: re.sub(r"-(\w)", lambda m: m.group(1).upper(), s)
    typography = {}
    for name, st in TEXT["styles"].items():
        value = {"fontFamily": "{fontFamily.ui}" if st["font"] == "inter" else "{fontFamily.mono}",
                 "fontSize": "{fontSize." + str(st["size"]) + "}",
                 "fontWeight": "{fontWeight." + names["weight"][st["weight"]] + "}",
                 "letterSpacing": spacing_of(st["size"], st["weight"]) if st["font"] == "inter" else "0px"}
        note = {"text": " List row titles and subtitles (line height 1.8 in a row), settings labels, buttons. Reading `cap.rowTitle` "
                        f"{rd('cap.rowTitle')['value']} implies {pt_of('cap.rowTitle') / INTER_CAP:.1f} px at Inter's {INTER_CAP} cap height.",
                "small-text": " Section headers (`List.SectionHeaderTitle` uses small-text, secondary colour), descriptions, badges, key caps. "
                              f"Reading `cap.sectionHeader` {rd('cap.sectionHeader')['value']} implies {pt_of('cap.sectionHeader') / INTER_CAP:.1f} px.",
                "extra-large-text": " The root search field reads this size: reading `cap.input` "
                                    f"{rd('cap.input')['value']} implies {pt_of('cap.input') / INTER_CAP:.1f} px (Derived; the field's own class is not in the Text table)."}.get(name, "")
        typography[camel(name)] = tok(value, "typography", f"Text style `{name}` ({st['font']}, {st['size']}, {st['weight']}), with the letter spacing the "
                                      f"`text` CSS module sets for that size and weight.{note}", "Measured", "raw/text-styles.json", file=TEXT["file"], style=name)
    shadow = {"panel": css("--shadow-panel-shadow", "Panel shadow on macOS (popovers, the action panel): five stacked soft layers.", "shadow",
                           selector="[macos]:root", value=[
                               {"color": "#0000000D", "offsetX": "0px", "offsetY": "1px", "blur": "1px", "spread": "-1px", "inset": False},
                               {"color": "#0000000D", "offsetX": "0px", "offsetY": "4px", "blur": "2px", "spread": "-3px", "inset": False},
                               {"color": "#0000000D", "offsetX": "0px", "offsetY": "8px", "blur": "4px", "spread": "-6px", "inset": False},
                               {"color": "#0000001A", "offsetX": "0px", "offsetY": "12px", "blur": "40px", "spread": "-12px", "inset": False},
                               {"color": "#00000033", "offsetX": "0px", "offsetY": "24px", "blur": "64px", "spread": "-24px", "inset": False}])}
    return {"fontFamily": fonts, "fontWeight": font_weight, "fontSize": font_size, "typography": typography,
            "spacing": spacing, "radius": radius, "size": size, "borderWidth": {"default": comp("1px", "dimension", "Borders and separators (`.list__separator`, `.settings-ui__separator{height:1px}`, `box-shadow:0 0 0 1px` rings).", "settings-ui")},
            "blur": blur, "easing": easing, "duration": duration, "shadow": shadow}


# ---------------------------------------------------------------- semantic sets

BASES = ["bg", "bg-secondary", "fg", "accent", "selection", "loader", "red", "orange", "yellow", "green", "blue", "purple", "magenta"]
KEY = {"bg": "background", "bg-secondary": "backgroundSecondary", "fg": "foreground", "accent": "accent", "selection": "selection",
       "loader": "loader"}
STEPS = (5, 10, 20, 40, 60, 80)


def base_tokens(theme):
    t = theme_obj(theme)
    out = {}
    for b in BASES:
        k = KEY.get(b, b)
        out[k] = tok(t[k].upper(), "color", f"`{k}` of {NAMES[theme]} (custom property `--{'theme-accent' if b == 'accent' else b}`).", "Measured",
                     "raw/bundled-themes.json", file=THEMES_FILE["file"], key=f"{t['id']}/{k}")
    return out


def alpha_tokens(theme):
    t = theme_obj(theme)
    out = {}
    for b in BASES:
        if b == "loader":
            continue
        k = KEY.get(b, b)
        steps = {}
        for s in STEPS:
            name = f"--{b}-{s}"
            raw = decl(name, ".theme-root")
            assert raw == f"rgb(from var(--{b}) r g b / {s}%)", (name, raw)
            steps[str(s)] = tok(hexa(rgb_of(t[k])[0], s / 100), "color", f"`{name}: {raw}`, worked out for {NAMES[theme]}.", "Derived",
                                "raw/css-tokens.json", file=CSS["file"], declaration=name)
        out[k] = steps
    return out


def ref(b, s=None):
    k = KEY.get(b, b)
    return f"alpha.{k}.{s}" if s else f"theme.{k}"


def role_of(theme, name, selector=".theme-root"):
    """An alias token for a role declared as var(--x) or var(--x-N)."""
    raw = decl(name, selector)
    m = re.fullmatch(r"var\(--([a-z-]+?)(?:-(\d+))?\)", raw)
    if not m or m.group(1) not in BASES:
        raise Missing(f"{name}: {raw} is not a base or alpha step")
    return alias(ref(m.group(1), m.group(2)), "color", f"`{name}: {raw}`.")


def literal(theme, name, selector=".theme-root", desc=""):
    """A role declared as a hex literal (or white/black)."""
    raw = decl(name, selector)
    h = {"white": "ffffff", "black": "000000"}.get(raw, raw.lstrip("#"))
    if len(h) in (3, 4):
        h = "".join(c * 2 for c in h)
    assert re.fullmatch(r"[0-9a-fA-F]{6}([0-9a-fA-F]{2})?", h), (name, raw)
    h = h.upper()
    if len(h) == 8 and h.endswith("FF"):
        h = h[:6]
    return tok("#" + h, "color", f"{desc}`{name}: {raw}` on `{selector}`.", "Measured", "raw/css-tokens.json", file=CSS["file"], declaration=name)


def pct(theme, base, p, desc):
    t = theme_obj(theme)
    return tok(hexa(rgb_of(t[KEY.get(base, base)])[0], p / 100), "color", desc, "Derived", "raw/components-css.json")


def sampled(rid, theme, desc):
    r = rd(rid, theme)
    return tok(r["value"], "color", desc + f" Reading `{rid}`.", r["evidence"], r["capture"])


def semantic(theme):
    t = theme_obj(theme)
    sel = f".theme-root[{theme}]"
    accent = t["accent"].upper()
    roles = {
        "page": sampled("px.window.main", theme, "The launcher window as painted: `--color-window-bg: var(--bg-40)` with a vertical gradient to "
                        "`--color-window-bg-secondary` over the macOS window material, so no declaration gives it. Use this as the page colour."),
        "settingsPage": sampled("px.window.settings", theme, "The Settings window as painted, behind its cards."),
        "surface": pct(theme, "fg", 2.5, "Settings card fill: `.settings-ui__sectionContent{background-color:rgb(from var(--fg) r g b / 2.5%)}`."),
        "sidebar": sampled("px.sidebar", theme, "The Settings sidebar as painted."),
        "dialog": tok(hexa((26, 26, 26)) if theme == "dark" else hexa((242, 242, 242)), "color",
                      "Dialog panel: `[dark]{--dialog-panel-bg-color:hsl(from var(--bg) h s 10%)}`, `[light]{... 95%}`, worked out from the theme's black or white "
                      "background. It equals the painted launcher window (role.page).", "Derived", "raw/components-css.json", module="dialog-primitive"),
        "scrim": comp("#0000004D", "color", "Dialog overlay (`.dialog-primitive__overlay{background-color:#0000004d}`); the alert overlay is #00000066.", "dialog-primitive"),
        "windowBase": literal(theme, "--color-window-base", sel, "Declared window base colour; not what the window paints (see page). "),
        "panelBackdrop": literal(theme, "--color-panel-backdrop", sel),
        "panelOverlay": literal(theme, "--color-panel-overlay", ".theme-root"),
        "text": {
            "primary": role_of(theme, "--color-text-primary"),
            "secondary": role_of(theme, "--color-text-secondary"),
            "tertiary": role_of(theme, "--color-text-tertiary"),
            "quaternary": role_of(theme, "--color-text-quaternary"),
            "disabled": role_of(theme, "--color-text-disabled"),
            "placeholder": role_of(theme, "--color-text-placeholder"),
            "selection": role_of(theme, "--color-text-selection"),
            "link": role_of(theme, "--color-text-link"),
        },
        "border": {
            "primary": role_of(theme, "--color-border-primary"),
            "secondary": role_of(theme, "--color-border-secondary"),
            "tertiary": role_of(theme, "--color-border-tertiary"),
            "separator": role_of(theme, "--color-border-separator"),
            "field": role_of(theme, "--color-border-field"),
            "token": role_of(theme, "--color-border-token"),
            "tokenSelected": role_of(theme, "--color-border-token-selected"),
            "focus": tok(hexa(rgb_of(t["foreground"])[0], 0.3), "color", "Focus ring colour on macOS: `--color-border-focus-ring: rgb(from var(--fg) r g b / 30%)`, drawn "
                         "2 px wide (core.size.focusRing).", "Derived", "raw/css-tokens.json", file=CSS["file"], declaration="--color-border-focus-ring"),
        },
        "surfaceFill": {
            "token": role_of(theme, "--color-surface-token"),
            "listHover": role_of(theme, "--color-surface-list-hover"),
            "listSelection": role_of(theme, "--color-surface-list-selection"),
            "control": role_of(theme, "--color-surface-control"),
            "innerPanel": literal(theme, "--color-surface-inner-panel"),
            "inputField": literal(theme, "--color-surface-input-field", desc="White at 5% in both themes. "),
            "actionBar": literal(theme, "--color-surface-action-bar"),
        },
        "accent": {
            "default": tok(accent, "color", f"`--accent: var(--color-system-accent, var(--theme-accent))`: the theme's accent unless macOS supplies one. The switch "
                           f"track paints {rd('px.switch.on', theme)['value']} (reading `px.switch.on`), so on this Mac the theme accent is in use.",
                           "Measured", "raw/bundled-themes.json", file=THEMES_FILE["file"], key=f"{t['id']}/accent"),
            "pressed": tok(mix_white(accent, 0.1), "color", "Pressed switch track: `color-mix(in srgb, var(--accent), white 10%)`, worked out.", "Derived", "raw/components-css.json", module="switch"),
            "subtle": alias("alpha.accent.10", "color", "`--accent-transparent: var(--accent-10)`: tinted backgrounds."),
        },
        "status": {
            "danger": alias("theme.red", "color", "Errors, destructive buttons (`.base-button[data-variant=destructive]` on red-20), invalid fields (red-40 border)."),
            "warning": alias("theme.yellow", "color", "Warnings (`.settings-ui__warningPanel` border yellow-40, icon yellow)."),
            "success": alias("theme.green", "color", "Success (valid fields green-40, success toasts)."),
            "info": alias("theme.blue", "color", "Info and blue badges."),
        },
        "brand": literal(theme, "--color-brand", ".theme-root", "Raycast's red, the same in every theme. "),
    }
    component = {
        "list": {
            "row": {
                "height": tok("{size.listRow}", "dimension", "Row height.", "Derived", MEASURED),
                "radius": tok("{radius.listItem}", "dimension", "Row corner.", "Derived", MEASURED),
                "hoverBg": comp("{alpha.selection.5}", "color", "`.list__item{--list-item-hover-background-color:var(--selection-5)}`.", "list"),
                "selectedBg": comp("{alpha.selection.10}", "color", "`.list__item:where([data-state=selected]){background-color:var(--selection-10)}`.", "list"),
                "title": alias("text.primary", "color", "Row title, text style `text`."),
                "subtitle": alias("text.secondary", "color", "Row subtitle and accessory, text style `text`."),
            },
            "sectionHeader": {"text": alias("text.secondary", "color", "`List.SectionHeaderTitle`: small-text, secondary.", "raw/components-css.json")},
            "separator": {"bg": alias("border.separator", "color", "`.list__separator:before{background-color:var(--color-border-separator)}`.")},
        },
        "switch": {
            "width": comp("36px", "dimension", "Medium switch on macOS (`--switch-width: round(calc(36 * var(--spx)), 1px)`); reading `size.switch` "
                          f"{rd('size.switch')['value']}.", "switch"),
            "height": comp("16px", "dimension", "Medium switch on macOS (`--switch-height: var(--space-16)`).", "switch"),
            "thumbWidth": comp("21px", "dimension", "Medium switch thumb on macOS (`--switch-thumb-width`); 13 px tall (16 less 1.5 px padding each side at 2x).", "switch"),
            "offBg": comp("{alpha.foreground.20}", "color", "`.switch__root{background-color:var(--fg-20)}`.", "switch"),
            "onBg": comp("{accent.default}", "color", "`.switch__root[aria-checked=true]{background-color:var(--accent)}`; fg at 30% when the window is not key.", "switch"),
            "thumb": comp("#FFFFFFE6", "color", "`.switch__thumb{background-color:#ffffffe6}`; #fffffff2 when on.", "switch"),
        },
        "button": {
            "height": tok("{size.control.medium}", "dimension", "Medium button; mini, small and large are core.size.control.*.", "Derived", "raw/components-css.json"),
            "bg": comp("{surfaceFill.control}", "color", "Default button (`[data-variant=default]{background-color:var(--color-surface-control)}`).", "base-button"),
            "text": alias("text.primary", "color", "Default button label.", "raw/components-css.json"),
            "ghostHoverBg": comp("{alpha.foreground.5}", "color", "Ghost button on hover (`var(--fg-5)`).", "base-button"),
            "destructiveBg": comp("{alpha.red.20}", "color", "Destructive button (`background-color:var(--red-20)`, label red-on-tint-20).", "base-button"),
            "padding": comp("16px", "dimension", "Medium button inline padding (`.button-primitive__root[data-size=medium]{padding-inline:var(--space-16)}`; 12 beside an icon).", "button-primitive"),
        },
        "input": {
            "height": tok("{size.control.medium}", "dimension", "Default text field (`[data-size=default]{height:var(--space-32)}`); small is size.control.small.", "Derived", "raw/components-css.json"),
            "bg": comp("{surfaceFill.inputField}", "color", "`.input-field-primitive__background{background-color:var(--color-surface-input-field)}`.", "input-field-primitive"),
            "border": comp("{border.secondary}", "color", "`--input-field-border-color:var(--color-border-secondary)`, drawn as a 1 px ring; transparent while focused.", "input-field-primitive"),
            "focusRing": comp("{border.focus}", "color", "Focus ring (`outline:var(--focus-ring-width) solid var(--input-field-focus-ring-color)`).", "input-field-primitive"),
            "errorBorder": comp("{alpha.red.40}", "color", "`[data-variant=error]{--input-field-border-color:var(--red-40)}`; its focus ring is red-60.", "input-field-primitive"),
            "padding": comp("12px", "dimension", "Inline padding (`--input-field-padding-x:var(--space-12)`).", "input-field-primitive"),
        },
        "dropdown": {
            "height": tok("{size.control.medium}", "dimension", "Default dropdown button (`height:var(--space-32)`); small is size.control.small.", "Derived", "raw/components-css.json"),
            "bg": comp("{surfaceFill.inputField}", "color", "`[data-variant=default]{background-color:var(--color-surface-input-field)}`.", "dropdown-button"),
            "border": comp("{border.secondary}", "color", "`--dropdown-button-border-color:var(--color-border-secondary)`.", "dropdown-button"),
            "openBg": comp("{alpha.foreground.10}", "color", "Ghost dropdown while open (`[data-state=open]{background-color:var(--fg-10)}`).", "dropdown-button"),
        },
        "checkbox": {
            "size": comp("14px", "dimension", "`.checkbox__checkbox{width:round(calc(14 * var(--spx)), 1px)}`.", "checkbox"),
            "border": comp("{alpha.foreground.20}", "color", "`box-shadow:0 0 0 1px var(--fg-20)`.", "checkbox"),
            "check": comp("{alpha.foreground.80}", "color", "`.checkbox__checkmark{stroke:var(--fg-80)}`, 1.8 px stroke; fg-40 when disabled.", "checkbox"),
        },
        "kbd": {
            "height": tok("{size.control.kbdMedium}", "dimension", "Medium key cap (`[data-size=medium]{height:round(calc(20 * var(--spx)), 1px)}`).", "Derived", "raw/components-css.json"),
            "border": comp("{border.token}", "color", "`[data-variant=default]{box-shadow:inset 0 0 0 1px var(--color-border-token)}`.", "shortcut"),
            "text": comp("{text.secondary}", "color", "Default key cap label.", "shortcut"),
        },
        "badge": {
            "bg": comp("{surfaceFill.token}", "color", "Gray badge (`[data-color=gray]{background-color:var(--color-surface-token)}`); coloured badges use the hue at 10% (`--blue-transparent`).", "base-badge"),
            "text": comp("{text.secondary}", "color", "Gray badge label.", "base-badge"),
            "radius": comp("{radius.full}", "dimension", "`border-radius:var(--radius-full)`.", "base-badge"),
        },
        "settings": {
            "rowHeight": tok("{size.settingsRow}", "dimension", "Card row.", "Derived", "raw/components-css.json"),
            "cardBg": alias("surface", "color", "Card fill.", "raw/components-css.json"),
            "separator": comp("{border.tertiary}", "color", "`.settings-ui__separator{background-color:var(--color-border-tertiary)}`.", "settings-ui"),
            "padding": comp("12px", "dimension", "Row padding (`padding:var(--space-12)`).", "settings-ui"),
            "radius": comp("8px", "dimension", "Interactive row corner (`border-radius:var(--space-8)`). The card corner fits "
                           f"{rd('radius.settings.card')['value']} (reading `radius.settings.card`, dark), so cards are about 10.", "settings-ui"),
        },
        "actionBar": {
            "height": tok("{size.mainWindow.footer}", "dimension", "Footer height.", "Derived", "raw/css-tokens.json"),
            "pillHeight": tok("{size.actionBarPill}", "dimension", "Pill height.", "Derived", "raw/components-css.json"),
            "pillRadius": comp("{radius.full}", "dimension", "`[macos] .action-bar-ui__right{border-radius:var(--radius-full)}`.", "action-bar-ui"),
        },
        "dialog": {
            "width": comp("400px", "dimension", "`.dialog-primitive__panel{width:round(calc(400 * var(--spx)), 1px)}`.", "dialog-primitive"),
            "bg": alias("dialog", "color", "Dialog panel.", "raw/components-css.json"),
            "headerHeight": comp("64px", "dimension", "`.dialog-primitive__header{height:round(calc(64 * var(--spx)), 1px)}`.", "dialog-primitive"),
            "footerHeight": comp("56px", "dimension", "`.dialog-primitive__footer{height:var(--space-56)}`.", "dialog-primitive"),
        },
        "grid": {
            "itemBg": comp("{alpha.foreground.5}", "color", "`.grid__itemContent{background-color:var(--fg-5)}`; selected draws a 2 px ring of selection-80 inside a 3 px ring of bg-80.", "grid"),
            "selectedRing": comp("{alpha.selection.80}", "color", "Selected grid item ring.", "grid"),
        },
        "toast": {
            "padding": comp("12px", "dimension", "`.toast__root{padding-inline:var(--space-12);padding-block:var(--space-8)}`.", "toast"),
            "successGlow": pct(theme, "green", 26, "Success toast glow (`--gradient-base-color:rgb(from var(--green) r g b / 26%)`), worked out."),
            "failureGlow": pct(theme, "red", 26, "Failure toast glow (red at 26%), worked out."),
        },
    }
    return {"theme": base_tokens(theme), "alpha": alpha_tokens(theme), **roles, "component": component}


# ---------------------------------------------------------------- pixel check

def resolve(doc, theme, path):
    node = doc[theme]
    for p in path.split("."):
        node = node[p]
    v = node["$value"]
    while isinstance(v, str) and v.startswith("{"):
        v = resolve(doc, theme, v[1:-1])
    return v


CHECKS = [  # (reading, token path, composited over: a reading, a token path, or None)
    ("px.list.selected", "component.list.row.selectedBg", "px.window.main"),
    ("px.list.hover", "component.list.row.hoverBg", "px.window.main"),
    ("px.text.primary", "text.primary", "px.window.main"),
    ("px.text.secondary", "text.secondary", "px.window.main"),
    ("px.text.sectionHeader", "component.list.sectionHeader.text", "px.window.main"),
    ("px.text.placeholder", "text.placeholder", "px.window.main"),
    ("px.settings.card", "surface", "px.window.settings"),
    ("px.settings.separator", "border.tertiary", "@px.settings.card"),
    ("px.sidebar.selected", "surfaceFill.listSelection", "px.sidebar"),
    ("px.switch.on", "component.switch.onBg", None),
    ("px.switch.off", "component.switch.offBg", "@px.settings.card"),
]


def pixel_check(doc):
    rows, worst = [], 0
    for theme in ("dark", "light"):
        for rid, path, under in CHECKS:
            declared = resolve(doc, theme, path)
            if under is None:
                expect = declared
            else:
                base = rd(under.lstrip("@"), theme)["value"]
                expect = over(declared, base)
            got = rd(rid, theme)["value"]
            diff = max(abs(a - b) for a, b in zip(rgb_of(expect)[0], rgb_of(got)[0]))
            worst = max(worst, diff)
            rows.append({"theme": theme, "reading": rid, "token": f"{theme}.{path}", "declared": declared,
                         "over": None if under is None else f"{under.lstrip('@')} {rd(under.lstrip('@'), theme)['value']}",
                         "expected": expect, "pixel": got, "maxChannelDiff": diff, "capture": rd(rid, theme)["capture"]})
    assert worst <= 2, f"pixel check: a declared colour differs from its pixel by {worst} per channel"
    return {"note": "Each translucent token composited over the painted fill under it, against the pixel. A text reading is the glyph pixel "
                    "furthest from the fill, so it matches only where a glyph has a fully covered pixel.", "worst": worst, "rows": rows}


# ---------------------------------------------------------------- component declarations behind each token

# Every token whose value was transcribed from a component rule names that rule here, as (module,
# a substring of its selector, property, a substring of its value). verify_rules() fails the build
# when a rule is gone or its value no longer matches, so a re-read bundle cannot leave a stale token.
RULES = {
    "easing.switchThumb": ("switch", ".switch__root", "--switch-thumb-transition", "cubic-bezier(.16, -.12, .29, 1.31)"),
    "duration.control": ("base-button", ".base-button__root", "transition", "background-color .15s ease-out"),
    "duration.switchTrack": ("switch", "[macos] .switch__root", "--switch-transition", "background-color .216s ease-out"),
    "duration.switchThumb": ("switch", "[macos] .switch__root", "--switch-thumb-transition", "transform .366s"),
    "duration.toastHoverIn": ("toast", ".toast__root", "--toast-hover-in-duration", ".1s"),
    "duration.toastHoverOut": ("toast", ".toast__root", "--toast-hover-out-duration", ".35s"),
    "duration.hotkeyHint": ("list", ".list__item", "--item-number-hotkey-hint-duration", ".15s"),
    "size.settingsRow": ("settings-ui", ".settings-ui__row", "min-height", "round(calc(46 * var(--spx)), 1px)"),
    "size.actionBarPill": ("action-bar-ui", ".action-bar-ui__root", "--action-bar-macos-pill-height", "round(calc(36 * var(--spx)), 1px)"),
    "size.focusRingOffset": ("switch", ".switch__root:focus-visible", "outline-offset", "2px"),
    "size.control.mini": ("base-button", "[data-size=mini])", "height", "var(--space-16)"),
    "size.control.small": ("base-button", "[data-size=small])", "height", "var(--space-24)"),
    "size.control.medium": ("base-button", "[data-size=medium])", "height", "var(--space-32)"),
    "size.control.large": ("base-button", "[data-size=large])", "height", "var(--space-40)"),
    "size.control.actionButton": ("action-button", "[macos] .action-button__button", "height", "round(calc(28 * var(--spx)), 1px)"),
    "size.control.kbdSmall": ("shortcut", "[data-size=small]", "height", "round(calc(18 * var(--spx)), 1px)"),
    "size.control.kbdMedium": ("shortcut", "[data-size=medium]", "height", "round(calc(20 * var(--spx)), 1px)"),
    "fontFamily.mono": ("text", ".text__font-mono", "font-family", "JetBrainsMono,monospace"),
    "borderWidth.default": ("settings-ui", ".settings-ui__separator", "height", "1px"),
    "scrim": ("dialog-primitive", ".dialog-primitive__overlay", "background-color", "#0000004d"),
    "surface": ("settings-ui", ".settings-ui__sectionContent", "background-color", "rgb(from var(--fg) r g b / 2.5%)"),
    "dialog": ("dialog-primitive", ".dialog-primitive__panelWeb", "--dialog-panel-bg-color", "hsl(from var(--bg) h s "),
    "accent.pressed": ("switch", ".switch__root[aria-checked=true]:not(:disabled):active", "background-color", "color-mix(in srgb, var(--accent), white 10%)"),
    "component.list.row.hoverBg": ("list", ".list__item", "--list-item-hover-background-color", "var(--selection-5)"),
    "component.list.row.selectedBg": ("list", ".list__item:where([data-state=selected])", "background-color", "var(--selection-10)"),
    "component.switch.width": ("switch", "[data-size=medium]:is([macos] .switch__root)", "--switch-width", "round(calc(36 * var(--spx)), 1px)"),
    "component.switch.height": ("switch", "[data-size=medium]:is([macos] .switch__root)", "--switch-height", "var(--space-16)"),
    "component.switch.thumbWidth": ("switch", "[data-size=medium]:is([macos] .switch__root)", "--switch-thumb-width", "round(calc(21 * var(--spx)), 1px)"),
    "component.switch.offBg": ("switch", ".switch__root", "background-color", "var(--fg-20)"),
    "component.switch.onBg": ("switch", ".switch__root[aria-checked=true]", "background-color", "var(--accent)"),
    "component.switch.thumb": ("switch", ".switch__thumb", "background-color", "#ffffffe6"),
    "component.button.bg": ("base-button", "[data-variant=default])", "background-color", "var(--color-surface-control)"),
    "component.button.ghostHoverBg": ("base-button", "[data-variant=ghost])", "background-color", "var(--fg-5)"),
    "component.button.destructiveBg": ("base-button", "[data-variant=destructive])", "background-color", "var(--red-20)"),
    "component.button.padding": ("button-primitive", "[data-size=medium])", "padding-inline", "var(--space-16)"),
    "component.input.bg": ("input-field-primitive", ".input-field-primitive__background", "background-color", "var(--color-surface-input-field)"),
    "component.input.border": ("input-field-primitive", ".input-field-primitive__root", "--input-field-border-color", "var(--color-border-secondary)"),
    "component.input.focusRing": ("input-field-primitive", "[data-state=focus]", "outline", "var(--focus-ring-width) solid var(--input-field-focus-ring-color)"),
    "component.input.errorBorder": ("input-field-primitive", "[data-variant=error]", "--input-field-border-color", "var(--red-40)"),
    "component.input.padding": ("input-field-primitive", "[data-size=default]", "--input-field-padding-x", "var(--space-12)"),
    "component.dropdown.bg": ("dropdown-button", "[data-variant=default])", "background-color", "var(--color-surface-input-field)"),
    "component.dropdown.border": ("dropdown-button", "[data-variant=default])", "--dropdown-button-border-color", "var(--color-border-secondary)"),
    "component.dropdown.openBg": ("dropdown-button", "[data-state=open])", "background-color", "var(--fg-10)"),
    "component.checkbox.size": ("checkbox", ".checkbox__checkbox", "width", "round(calc(14 * var(--spx)), 1px)"),
    "component.checkbox.border": ("checkbox", ".checkbox__checkbox", "box-shadow", "0 0 0 1px var(--fg-20)"),
    "component.checkbox.check": ("checkbox", ".checkbox__checkmark", "stroke", "var(--fg-80)"),
    "component.kbd.border": ("shortcut", "[data-variant=default]", "box-shadow", "var(--color-border-token)"),
    "component.kbd.text": ("shortcut", "[data-variant=default]", "color", "var(--color-text-secondary)"),
    "component.badge.bg": ("base-badge", "[data-color=gray])", "background-color", "var(--color-surface-token)"),
    "component.badge.text": ("base-badge", "[data-color=gray])", "color", "var(--color-text-secondary)"),
    "component.badge.radius": ("base-badge", ".base-badge__root", "border-radius", "var(--radius-full)"),
    "component.settings.separator": ("settings-ui", ".settings-ui__separator", "background-color", "var(--color-border-tertiary)"),
    "component.settings.padding": ("settings-ui", ".settings-ui__row", "padding-top", "var(--space-12)"),
    "component.settings.radius": ("settings-ui", ".settings-ui__row", "border-radius", "var(--space-8)"),
    "component.actionBar.pillRadius": ("action-bar-ui", ".action-bar-ui__right", "border-radius", "var(--radius-full)"),
    "component.dialog.width": ("dialog-primitive", ".dialog-primitive__panel", "width", "round(calc(400 * var(--spx)), 1px)"),
    "component.dialog.headerHeight": ("dialog-primitive", ".dialog-primitive__header", "height", "round(calc(64 * var(--spx)), 1px)"),
    "component.dialog.footerHeight": ("dialog-primitive", ".dialog-primitive__footer", "height", "var(--space-56)"),
    "component.grid.itemBg": ("grid", ".grid__itemContent", "background-color", "var(--fg-5)"),
    "component.grid.selectedRing": ("grid", "[data-state=selected]", "--item-box-shadow-color1", "var(--selection-80)"),
    "component.toast.padding": ("toast", ".toast__root", "padding-inline", "var(--space-12)"),
    "component.toast.successGlow": ("toast", "[data-variant=success]", "--gradient-base-color", "rgb(from var(--green) r g b / 26%)"),
    "component.toast.failureGlow": ("toast", "[data-variant=failure]", "--gradient-base-color", "rgb(from var(--red) r g b / 26%)"),
}


def find_rule(module, selector, prop, value):
    for r in COMPONENTS["modules"].get(module, []):
        if selector in r["selector"] and any(n == prop and value in v for n, v in r["decls"]):
            return r
    return None


def verify_rules(doc):
    """Every non-alias token sourced from raw/components-css.json has a RULES entry whose rule exists."""
    for name in ("core", "light", "dark"):
        for p, t in walk(doc[name]):
            path = ".".join(p)
            src = t["$extensions"]["source"]
            if src["capture"] != "raw/components-css.json":
                continue
            if isinstance(t["$value"], str) and t["$value"].startswith("{") and src["evidence"] == "Derived":
                continue          # a reference to another token, not a transcribed value
            assert path in RULES, f"{name}.{path}: transcribed from a component rule but names none in RULES"
            assert find_rule(*RULES[path]), f"{name}.{path}: no rule {RULES[path]} in raw/components-css.json"
    return len(RULES)


# ---------------------------------------------------------------- helpers, check, build

def walk(node, path=()):
    if isinstance(node, dict) and "$value" in node:
        yield path, node
        return
    if isinstance(node, dict):
        for k, v in node.items():
            if not k.startswith("$"):
                yield from walk(v, path + (k,))


def aliases(v):
    """Every {alias} in a value, including those inside a composite (a typography style)."""
    if isinstance(v, str):
        return re.findall(r"\{([^{}]+)\}", v)
    if isinstance(v, dict):
        return [a for x in v.values() for a in aliases(x)]
    return []


def check(doc):
    sets = [s for s in ("core", "light", "dark") if s in doc]  # a one-theme app has no light or no dark
    paths = {".".join(p) for name in sets for p, _ in walk(doc[name])}
    for name in sets:
        for p, t in walk(doc[name]):
            where = name + "." + ".".join(p)
            src = t.get("$extensions", {}).get("source", {})
            assert src.get("evidence") and src.get("capture"), f"{where}: no source"
            v = t["$value"]
            for a in aliases(v):
                assert a in paths, f"{where}: alias {{{a}}} points at nothing"
            if isinstance(v, str) and v.startswith("{"):
                continue
            elif t["$type"] == "color":
                assert re.fullmatch(r"#[0-9A-F]{6}([0-9A-F]{2})?", v), f"{where}: bad colour {v}"
            elif t["$type"] == "dimension":
                assert re.fullmatch(r"-?\d+(\.\d+)?px", v), f"{where}: bad dimension {v}"
    keys = lambda s: sorted(".".join(p) for p, _ in walk(doc[s]))
    if "light" in doc and "dark" in doc:
        assert keys("light") == keys("dark"), "light and dark keys differ"


def build():
    doc = {
        "core": core(),
        "light": semantic("light"),
        "dark": semantic("dark"),
        "$themes": [
            {"id": "light", "name": "Raycast Light", "selectedTokenSets": {"core": "source", "light": "enabled"},
             "$description": "Settings > General > Appearance: Follow System Appearance off and Theme set to Raycast Light for the capture, then put back. Read from screenshots/light/."},
            {"id": "dark", "name": "Raycast Dark", "selectedTokenSets": {"core": "source", "dark": "enabled"},
             "$description": "The owner's setting: Follow System Appearance on, Dark Theme Raycast Dark, with macOS in dark mode. Read from screenshots/dark/."},
        ],
        "$metadata": {"tokenSetOrder": ["core", "light", "dark"],
                      "source": f"Raycast {THEMES_FILE['version']} for macOS, {THEMES_FILE['bundle']}"},
    }
    check(doc)
    verify_rules(doc)
    pc = pixel_check(doc)
    (RAW / "pixel-check.json").write_text(json.dumps(pc, indent=1) + "\n")
    (PKG / "tokens.json").write_text(json.dumps(doc, indent=1, ensure_ascii=False) + "\n")
    n = sum(1 for s in ("core", "light", "dark") for _ in walk(doc[s]))
    print(f"tokens.json: {n} tokens; pixel check: {len(pc['rows'])} comparisons, worst {pc['worst']} per channel")


if __name__ == "__main__":
    if not READ:
        raise SystemExit("no raw/readings.json: run tools/measure.py first")
    build()
