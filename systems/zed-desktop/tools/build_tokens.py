#!/usr/bin/env python3
"""Build tokens.json (W3C DTCG, Tokens Studio multi-set layout) and raw/pixel-check.json.

    python3 tools/build_tokens.py

Adapted from the native kit (systems/grokbot). Three inputs, all in raw/:

  one.json            Zed's own theme file, assets/themes/one/one.json at the v1.25.2 commit
                      (MIT, GitHub Inc.; one.LICENSE beside it). Every colour comes from here:
                      `theme.*`, `syntax.*`, `player.*` copy each key of "One Dark" and "One Light",
                      and `role.*` and `component.*` alias them. Evidence: Measured (the product's
                      declared value), with the file, commit and key as the source.
  settings-fonts.json The font settings the capture ran with (tools/capture/read_settings.py).
  readings.json       Sizes, radii, insets, type and the pixel samples (tools/measure.py).

The pixel check: each `px.<key>` reading is compared with the theme key it names (composited over
the surface under it when the key has alpha), and raw/pixel-check.json lists both values and the
difference. The build fails if any differs by more than 2 per channel, so a theme file that no
longer matches the captures cannot be committed silently.

The builder refuses a token without a source, an alias that points at nothing, a colour that is not
#RRGGBB(AA), a dimension that is not one px length, and a light and dark set whose keys differ.
Standard library only. Deterministic: the same inputs give the same bytes.
"""
import json
import pathlib
import re

PKG = pathlib.Path(__file__).resolve().parent.parent
RAW = PKG / "raw"
_R = RAW / "readings.json"
READ = json.loads(_R.read_text()) if _R.exists() else {}
THEME_FILE = json.loads((RAW / "one.json").read_text()) if (RAW / "one.json").exists() else None
FONTS = json.loads((RAW / "settings-fonts.json").read_text()) if (RAW / "settings-fonts.json").exists() else None
MEASURED = f"raw/{PKG.name}-measured.md"
COMMIT = "d25fa01ccd788d812f236810b71af4feff6b2e38"
UPSTREAM = "zed-industries/zed assets/themes/one/one.json @ v1.25.2 (" + COMMIT[:12] + ")"
THEMES = {"dark": "One Dark", "light": "One Light"}
CAP_PLEX = 0.698   # IBM Plex Sans cap height / em, the assumption behind the Derived UI sizes
CAP_MENLO = 8 / 11  # calibrated: Menlo at the owner's 11 pt reads an 8 pt capital (cap.buffer)


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


def derived(value, typ, desc, capture=MEASURED):
    return tok(value, typ, desc, "Derived", capture)


def alias(path, typ, desc):
    return tok("{" + path + "}", typ, desc, "Derived", "raw/one.json")


def px(v):
    return f"{v:g}px"


def pt(rid, theme="dark", index=0):
    return float(rd(rid, theme)["value"].rstrip("pt").split("x")[index])


def sampled(rid, desc, theme="dark", index=0, rounder=None):
    v = pt(rid, theme, index)
    v = rounder(v) if rounder else v
    return tok(px(v), "dimension", desc + f" Reading `{rid}`: {rd(rid, theme)['value']} ({theme}).", "Sampled", rd(rid, theme)["capture"])


# ---------------------------------------------------------------- the theme file

def style(theme):
    return next(t for t in THEME_FILE["themes"] if t["name"] == THEMES[theme])["style"]


def colour(v):
    v = v.upper()
    return v[:7] if len(v) == 9 and v.endswith("FF") else v


def key_paths(keys):
    """Theme keys are dotted ('border', 'border.variant'). A key that is also the prefix of another
    becomes '<key>.default', so DTCG can hold both."""
    keys = sorted(keys)
    out = {}
    for k in keys:
        parts = k.split(".")
        if any(o.startswith(k + ".") for o in keys):
            parts.append("default")
        out[k] = parts
    return out


def put(tree, parts, value):
    for p in parts[:-1]:
        tree = tree.setdefault(p, {})
    tree[parts[-1]] = value


SKIP = {"version_control.conflict_marker.ours", "version_control.conflict_marker.theirs"}  # One Dark only


def theme_tokens(theme):
    s = style(theme)
    flat = {k: v for k, v in s.items() if isinstance(v, str) and k not in SKIP}
    out = {}
    for k, parts in key_paths(flat).items():
        put(out, parts, tok(colour(flat[k]), "color", f"Theme key `{k}` in {THEMES[theme]}.", "Measured", "raw/one.json",
                            file=UPSTREAM, key=f"{THEMES[theme]}/{k}"))
    syn = {}
    for k, parts in key_paths(s["syntax"]).items():
        v = s["syntax"][k]
        extra = "".join(f" {n} {v[n]}." for n in ("font_style", "font_weight") if v.get(n) is not None)
        put(syn, parts, tok(colour(v["color"]), "color", f"Syntax key `{k}` in {THEMES[theme]}.{extra}", "Measured", "raw/one.json",
                            file=UPSTREAM, key=f"{THEMES[theme]}/syntax/{k}"))
    players = {str(i): {n: tok(colour(p[n]), "color", f"Player {i} {n} (player 0 is the local cursor and selection).", "Measured",
                               "raw/one.json", file=UPSTREAM, key=f"{THEMES[theme]}/players/{i}/{n}") for n in ("cursor", "background", "selection")}
               for i, p in enumerate(s["players"])}
    return out, syn, players


def path_of(key):
    keys = [k for k in style("dark") if isinstance(style("dark")[k], str) and k not in SKIP]
    return "theme." + ".".join(key_paths(keys)[key])


# ---------------------------------------------------------------- pixel check

def rgba(h):
    h = h.lstrip("#")
    if len(h) == 6:
        h += "ff"
    return [int(h[i:i + 2], 16) for i in (0, 2, 4, 6)]


def over(top, base):
    a = top[3] / 255
    return [round(top[i] * a + base[i] * (1 - a)) for i in range(3)]


# reading id -> (theme key, key of the surface under it when the key has alpha)
PX = {
    "px.title_bar.background": ("title_bar.background", None), "px.border": ("border", None),
    "px.tab_bar.background": ("tab_bar.background", None), "px.tab.active_background": ("tab.active_background", None),
    "px.panel.background": ("panel.background", None), "px.editor.background": ("editor.background", None),
    "px.editor.gutter.background": ("editor.gutter.background", None),
    "px.editor.active_line.background": ("editor.active_line.background", "editor.background"),
    "px.toolbar.background": ("toolbar.background", None), "px.status_bar.background": ("status_bar.background", None),
    "px.border.variant": ("border.variant", None), "px.elevated_surface.background": ("elevated_surface.background", None),
    "px.element.selected": ("element.selected", None), "px.terminal.background": ("terminal.background", None),
    "px.version_control.modified": ("version_control.modified", None), "px.version_control.added": ("version_control.added", None),
    "px.switch.off": ("element.background", None),
    "px.text": ("text", None), "px.text.status": ("text", None),
}


def pixel_check():
    rows = []
    for rid, (key, base) in PX.items():
        for theme in ("dark", "light"):
            r = rd(rid, theme)
            s = style(theme)
            want = rgba(s[key])
            exp = over(want, rgba(s[base])) if want[3] < 255 else want[:3]
            got = rgba(r["value"])[:3]
            diff = max(abs(a - b) for a, b in zip(exp, got))
            rows.append({"reading": rid, "theme": theme, "key": key, "declared": colour(s[key]),
                         "expected": "#%02X%02X%02X" % tuple(exp), "pixel": r["value"], "maxChannelDiff": diff,
                         "composited": f"over {base} {colour(s[base])}" if want[3] < 255 else None,
                         "method": r["op"], "capture": r["capture"]})
    bad = [r for r in rows if r["maxChannelDiff"] > 2]
    assert not bad, f"pixel and theme file disagree: {bad}"
    (RAW / "pixel-check.json").write_text(json.dumps(rows, indent=1) + "\n")
    return rows


# ---------------------------------------------------------------- core

def font(where, key):
    d = FONTS[where]["keys"][key]
    return d["value"] if where == "defaults" else d


def settings_src(where, key):
    if where == "owner":
        return {"evidence": "Measured", "capture": "raw/settings-fonts.json", "key": f"owner settings.json `{key}`"}
    d = FONTS["defaults"]["keys"][key]
    return {"evidence": "Measured", "capture": "raw/settings-fonts.json", "key": f"default.json line {d['line']} `{key}`", "file": UPSTREAM.replace("themes/one/one.json", "settings/default.json")}


def stok(value, typ, desc, where, key):
    s = settings_src(where, key)
    return tok(value, typ, desc, s.pop("evidence"), s.pop("capture"), **s)


def core():
    c = {}
    sans = FONTS["defaults"]["comments"]["ZedSans"]["value"]
    mono = FONTS["defaults"]["comments"]["ZedMono"]["value"]
    c["fontFamily"] = {
        "ui": stok(f"{sans}, -apple-system, system-ui, sans-serif", "fontFamily",
                   f"UI font. The owner leaves `ui_font_family` unset, so Zed uses its default `.ZedSans`, which default.json (line {FONTS['defaults']['comments']['ZedSans']['line']}) says currently aliases to {sans}; Zed bundles it. The fallbacks are for a page built from these tokens.",
                   "defaults", "ui_font_family"),
        "buffer": stok(f"{font('owner', 'buffer_font_family')}, ui-monospace, SF Mono, monospace", "fontFamily",
                       "Editor (buffer) font, set by the owner. Agent-panel user messages and the terminal use the buffer font when theirs is unset.",
                       "owner", "buffer_font_family"),
        "bufferDefault": stok(f"{mono}, ui-monospace, monospace", "fontFamily",
                              f"Zed's default buffer font, `.ZedMono`, which default.json (line {FONTS['defaults']['comments']['ZedMono']['line']}) says currently aliases to {mono}. Not used in these captures: the owner sets Menlo.",
                              "defaults", "buffer_font_family"),
    }
    c["fontSize"] = {
        "uiBase": stok(px(font("owner", "ui_font_size")), "dimension", "`ui_font_size`: the rem base the UI scales from (the owner's value equals Zed's default of 16). Labels render smaller; see `typography`.", "owner", "ui_font_size"),
        "buffer": stok(px(font("owner", "buffer_font_size")), "dimension", "`buffer_font_size`, set by the owner (Zed's default is 15). The pixels agree: an 8 pt capital (cap.buffer) is 11 pt Menlo.", "owner", "buffer_font_size"),
        "agentUi": stok(px(font("owner", "agent_ui_font_size")), "dimension", "`agent_ui_font_size`, set by the owner. Agent replies measure smaller (cap.agentBody gives about 14), so the panel scales from this base as the UI does.", "owner", "agent_ui_font_size"),
        "agentBuffer": stok(px(font("defaults", "agent_buffer_font_size")), "dimension", "`agent_buffer_font_size` default: user messages in the agent panel, in the buffer font.", "defaults", "agent_buffer_font_size"),
        "markdownPreview": stok(px(font("owner", "markdown_preview_font_size")), "dimension", "`markdown_preview_font_size`, set by the owner.", "owner", "markdown_preview_font_size"),
        "terminal": derived("10px", "dimension", "Terminal font size as the Settings window shows it (Terminal > Font Size 10.00, marked as changed from the default); read as text off screenshots/dark/36-settings-terminal.png.", "screenshots/dark/36-settings-terminal.png"),
    }
    c["fontWeight"] = {
        "regular": stok(font("defaults", "ui_font_weight"), "fontWeight", "`ui_font_weight` default 400; `buffer_font_weight` is 400 too (owner).", "defaults", "ui_font_weight"),
        "semibold": derived(600, "fontWeight", "Headings in agent replies and Markdown, judged by stroke width; Zed's theme file sets no UI weights.", rd("cap.agentHeading")["capture"]),
    }
    std = FONTS["defaults"]["comments"]["standard"]
    c["lineHeight"] = {
        "buffer": tok(float(std["value"]), "number", f"`buffer_line_height` is \"{font('owner', 'buffer_line_height')}\" (owner), which default.json (line {std['line']}) defines as {std['value']}. The pixels agree: a buffer line is {rd('size.gutterLine')['value']} at 11 pt (size.gutterLine).",
                      "Measured", "raw/settings-fonts.json", key="owner settings.json `buffer_line_height`"),
        "bufferComfortable": tok(float(FONTS["defaults"]["comments"]["comfortable"]["value"]), "number", "Zed's default `buffer_line_height` (\"comfortable\"). Not used in these captures.", "Measured", "raw/settings-fonts.json", key=f"default.json line {FONTS['defaults']['comments']['comfortable']['line']}"),
    }

    def size_of(cap_rid, theme="dark", ratio=CAP_PLEX):
        return round(pt(cap_rid, theme) / ratio)

    def ty(name, family, cap_rid, weight, desc, lh=None, theme="dark", also=()):
        size = size_of(cap_rid, theme)
        caps = ", ".join(f"{r} {rd(r, t)['value']}" for r, t in ((cap_rid, theme),) + tuple(also))
        v = {"fontFamily": "{fontFamily.%s}" % family, "fontWeight": "{fontWeight.%s}" % weight, "fontSize": px(size)}
        if lh:
            v["lineHeight"] = lh
        return tok(v, "typography", desc + f" Size Derived from capital heights ({caps}) at IBM Plex Sans's cap height of {CAP_PLEX} em, plus or minus 1 pt.", "Derived", rd(cap_rid, theme)["capture"])

    buffer_size = round(pt("cap.buffer") / CAP_MENLO)
    c["typography"] = {
        "label": ty("label", "ui", "cap.tree", "regular", "Default UI label: file tree rows, tabs, menu and palette items, settings row titles, status bar.", also=(("cap.settingsRow", "dark"), ("cap.treeL", "light"))),
        "labelSmall": ty("labelSmall", "ui", "cap.settingsDesc", "regular", "Secondary text: settings descriptions, inline hints. Dark reads 8.5 pt, light 9 pt (12 to 13 px).", theme="light", also=(("cap.settingsDesc", "dark"),)),
        "title": ty("title", "ui", "cap.settingsTitle", "regular", "Page title in the Settings window ('General').", also=(("cap.settingsTitle", "light"),)),
        "body": ty("body", "ui", "cap.agentBody", "regular", "Agent replies and Markdown preview paragraphs.", also=(("cap.mdBody", "dark"),)),
        "heading": ty("heading", "ui", "cap.agentHeading", "semibold", "Headings inside agent replies ('Done', 'Follow-ups'): the body size, heavier."),
        "markdownH1": ty("markdownH1", "ui", "cap.mdH1", "semibold", "H1 in the Markdown preview."),
        "code": tok({"fontFamily": "{fontFamily.buffer}", "fontWeight": "{fontWeight.regular}", "fontSize": px(buffer_size), "lineHeight": "{lineHeight.buffer}"},
                    "typography", f"The editor, terminal output in tool cards and code in replies: Menlo at the owner's 11 pt; cap.buffer reads {rd('cap.buffer')['value']}, which is 11 pt at Menlo's measured cap ratio.",
                    "Measured", "raw/settings-fonts.json", key="owner settings.json `buffer_font_size`"),
    }
    c["radius"] = {
        "sm": derived("4px", "dimension", f"Buttons, selects, the settings search field and nav rows: {rd('radius.button')['value']} (button), {rd('radius.select')['value']} (select), {rd('radius.navRow')['value']} (nav row), dark. Fitted to the corner's outline, plus or minus 0.5 pt."),
        "md": derived("6px", "dimension", f"Context menus and the agent's user message box: {rd('radius.menu')['value']} (menu), {rd('radius.userMessage')['value']} (message), dark."),
        "lg": derived("8px", "dimension", f"The command palette, pickers and tooltips: {rd('radius.palette')['value']} (palette), {rd('radius.tooltip')['value']} (tooltip), dark. Light readings come out lower ({rd('radius.palette', 'light')['value']}, {rd('radius.tooltip', 'light')['value']}) because the light border barely differs from the surface and the shadow."),
        "full": derived("999px", "dimension", f"Switch tracks are pills: a {rd('radius.switch')['value']} fit on an 18 pt track."),
    }
    c["spacing"] = {
        "1": derived("4px", "dimension", f"Palette border to the selected row's fill ({rd('inset.paletteRowMargin')['value']})."),
        "2": derived("8px", "dimension", f"Window edge to a file-tree icon ({rd('inset.treeIcon')['value']}, icon side bearing included)."),
        "3": derived("12px", "dimension", f"Padding inside the agent's user message box ({rd('inset.userMessage')['value']}) and palette rows ({rd('inset.paletteRowText')['value']} to the first ink)."),
        "6": derived("24px", "dimension", f"Tab edge to its label ({rd('inset.tabLabel')['value']}): the close-button slot sits on the left (the owner's `tabs.close_position`)."),
        "8": derived("32px", "dimension", f"Settings sidebar to the page content ({rd('inset.settingsPage')['value']})."),
    }
    c["size"] = {
        "titleBar": sampled("size.titleBar", "Title bar height (project, branch, update button, avatar)."),
        "tabBar": sampled("size.tabBar", "Tab bar height."),
        "toolbar": sampled("size.toolbar", "Breadcrumb toolbar under the tabs."),
        "statusBar": sampled("size.statusBar", "Status bar height."),
        "projectPanel": derived("240px", "dimension", f"Project panel width: {rd('size.projectPanel')['value']} of fill plus a 1 pt border; the Settings window lists Project Panel Default Width 240 (35-settings-panels)."),
        "tab": sampled("size.activeTab", "Width of the 'inventory.py' tab; tabs size to their label."),
        "treeRow": sampled("size.treeRow", "File-tree row pitch.", theme="light"),
        "bufferLine": sampled("size.gutterLine", "One editor line at Menlo 11 pt, standard line height."),
        "control": sampled("size.select.h", "Selects, the settings search field and nav rows, border to border (search and nav row read the same)."),
        "button": sampled("size.button.h", "Small bordered button in the title bar ('Restart to Update'), border to border."),
        "paletteWidth": derived("610px", "dimension", f"Command palette and file finder: {rd('size.palette.w')['value']} inside a 1 pt border on each side."),
        "paletteQuery": sampled("size.palette.query", "The palette's query field."),
        "paletteRow": derived("32px", "dimension", f"Palette and picker rows: the selected row's fill reads {rd('size.palette.row')['value']}."),
        "menuWidth": sampled("size.menu.w", "File context menu, border to border; menus size to their longest item."),
        "tooltip": derived("32px", "dimension", f"Tooltip height: {rd('size.tooltip.h')['value']} border to border in dark, {rd('size.tooltip.h', 'light')['value']} in light (the dark shadow reads as border)."),
        "switch": {
            "width": sampled("size.switch.w", "Switch track, border to border."),
            "height": sampled("size.switch.h", "Switch track, border to border."),
            "thumb": sampled("size.switch.thumb", "Switch thumb."),
        },
        "sendButton": sampled("size.sendButton", "Agent composer send button, width (height 22).", index=0),
        "userMessage": sampled("size.userMessage.h", "A one-line user message box in the agent panel, border to border."),
        "toolCardHeader": sampled("size.toolCardHeader", "Header of a terminal tool card (label and command)."),
        "settingsSidebar": sampled("size.settingsSidebar", "Settings window sidebar, border excluded."),
    }
    c["border"] = {"width": {"default": derived("1px", "dimension", "Every divider and control border is 2 px in the 2x captures (px.border, px.border.variant)." )}}
    c["$extensions"] = {"notTokenised": [
        "Motion and durations: stills only",
        "Shadows: popovers and menus cast a soft shadow (visible below the palette); its blur and offset were not measured",
        "Icon sizes: Zed's icons are its own (Lucide-derived) set and are not kept here",
        "Theme keys declared null in One Dark and One Light (`pane.focused_border`, `panel.focused_border`)",
        "`version_control.conflict_marker.ours` and `.theirs`: declared in One Dark only, so left out of both sets",
    ]}
    return c


# ---------------------------------------------------------------- semantic sets

ROLES = [  # role path, theme key, what it is
    ("page", "editor.background", "The editor, the largest surface; tabs' active fill and the terminal match it."),
    ("surface", "panel.background", "Panels (project, git, agent), the tab bar and inactive tabs."),
    ("raised", "elevated_surface.background", "The command palette, pickers, menus and tooltips."),
    ("chrome", "title_bar.background", "Title bar and status bar (`background` and `status_bar.background` are the same value)."),
    ("text.primary", "text", "Labels and UI text."),
    ("text.secondary", "text.muted", "Muted labels: breadcrumbs, descriptions, file-tree folders."),
    ("text.placeholder", "text.placeholder", "Placeholders in the palette, composer and search fields."),
    ("text.disabled", "text.disabled", "Disabled labels (menu items such as Paste with an empty clipboard)."),
    ("text.link", "text.accent", "Links in agent replies and the Markdown preview, and accented labels."),
    ("text.code", "editor.foreground", "Plain text in the buffer."),
    ("border.default", "border", "Dividers between bars and panels; control borders."),
    ("border.subtle", "border.variant", "Borders of popovers, menus and the palette; lines inside the editor chrome."),
    ("border.focus", "border.focused", "The focused element's outline (the Cancel button in the system prompt shows the OS ring, not this)."),
    ("border.selected", "border.selected", "Selected element border."),
    ("accent.default", "text.accent", "The one hue: links, the active status-bar icon, accent icons, the cursor (player 0)."),
    ("accent.hover", "element.hover", "Controls on hover: Zed shifts a control's fill to `element.hover`, not an accent shade."),
    ("accent.pressed", "element.active", "Controls while pressed."),
    ("accent.selected", "element.selected", "The selected row in the palette, pickers and lists."),
    ("control.default", "element.background", "Filled controls (selects, steppers, the switch track when off)."),
    ("control.ghostHover", "ghost_element.hover", "Ghost buttons (icon buttons, tabs, list rows) on hover."),
    ("status.success", "success", "Success text and icons."),
    ("status.warning", "warning", "Warnings."),
    ("status.danger", "error", "Errors: diagnostics, squiggles, the error count."),
    ("status.info", "info", "Information."),
    ("status.successBg", "success.background", "Success fill."),
    ("status.warningBg", "warning.background", "Warning fill (the 'settings are out of date' banner)."),
    ("status.dangerBg", "error.background", "Error fill (diagnostic blocks)."),
    ("status.infoBg", "info.background", "Information fill."),
    ("git.added", "version_control.added", "Gutter bar and diff for added lines."),
    ("git.modified", "version_control.modified", "Gutter bar for modified lines."),
    ("git.deleted", "version_control.deleted", "Gutter marker and diff for deleted lines."),
    ("search.match", "search.match_background", "Search matches in the buffer (translucent)."),
]


def semantic(theme):
    th, syn, players = theme_tokens(theme)
    s = {"theme": th, "syntax": syn, "player": players}
    role = {}
    for path, key, desc in ROLES:
        put(role, path.split("."), alias(path_of(key), "color", f"{desc} Alias of theme key `{key}`."))
    put(role, ["selection"], alias("player.0.selection", "color", "Text selection: player 0's selection colour (translucent)."))
    put(role, ["cursor"], alias("player.0.cursor", "color", "The local cursor (player 0)."))
    switch_on = rd("px.switch.on", theme)
    put(role, ["control", "switchOn"], tok(switch_on["value"], "color",
        f"Switch track when on. No theme key gives this value directly (it is not `text.accent` or `border.focused`); the reading's dominant colour covers {round(switch_on['share'] * 100)}% of its box.",
        "Sampled" if switch_on["share"] >= 0.9 else "Derived", switch_on["capture"]))
    s["role"] = role
    a = lambda key: "{" + path_of(key) + "}"
    s["component"] = {
        "tab": {"bg": alias(path_of("tab.inactive_background"), "color", "Inactive tab fill."),
                "activeBg": alias(path_of("tab.active_background"), "color", "Active tab fill: the editor's colour, so the tab joins the buffer."),
                "text": alias(path_of("text.muted"), "color", "Inactive tab label (a modified file's label takes `modified`, the owner's `tabs.git_status`)."),
                "height": alias("size.tabBar", "dimension", "Tab height: the tab bar.")},
        "palette": {"bg": alias(path_of("elevated_surface.background"), "color", "Palette fill."),
                    "text": alias(path_of("text"), "color", "Palette items."),
                    "radius": alias("radius.lg", "dimension", "Palette corners."),
                    "width": alias("size.paletteWidth", "dimension", "Palette width.")},
        "menu": {"bg": alias(path_of("elevated_surface.background"), "color", "Menu fill."),
                 "text": alias(path_of("text"), "color", "Menu items."),
                 "radius": alias("radius.md", "dimension", "Menu corners.")},
        "tooltip": {"bg": alias(path_of("elevated_surface.background"), "color", "Tooltip fill."),
                    "text": alias(path_of("text"), "color", "Tooltip label; the key binding beside it is muted."),
                    "radius": alias("radius.lg", "dimension", "Tooltip corners."),
                    "height": alias("size.tooltip", "dimension", "Tooltip height.")},
        "button": {"bg": alias(path_of("ghost_element.background"), "color", "Ghost button fill: transparent until hover."),
                   "text": alias(path_of("text"), "color", "Button label."),
                   "radius": alias("radius.sm", "dimension", "Button corners."),
                   "height": alias("size.button", "dimension", "Small button height.")},
        "input": {"bg": alias(path_of("editor.background"), "color", "Text fields (settings search, the agent composer) take the editor's colour."),
                  "text": alias(path_of("text"), "color", "Typed text."),
                  "radius": alias("radius.sm", "dimension", "Field corners."),
                  "height": alias("size.control", "dimension", "Field height.")},
        "select": {"bg": alias(path_of("element.background"), "color", "Select fill."),
                   "text": alias(path_of("text"), "color", "Select value."),
                   "radius": alias("radius.sm", "dimension", "Select corners."),
                   "height": alias("size.control", "dimension", "Select height.")},
        "statusBar": {"bg": alias(path_of("status_bar.background"), "color", "Status bar fill."),
                      "height": alias("size.statusBar", "dimension", "Status bar height.")},
        "userMessage": {"bg": alias(path_of("editor.background"), "color", "The agent panel's user message box: the editor colour inside a `border`-coloured outline, on the panel surface."),
                        "radius": alias("radius.md", "dimension", "Message corners."),
                        "padding": alias("spacing.3", "dimension", "Message padding.")},
    }
    s["$extensions"] = {"themeFile": UPSTREAM, "theme": THEMES[theme]}
    return s


# ---------------------------------------------------------------- build and checks

def walk(node, path=()):
    if isinstance(node, dict) and "$value" in node:
        yield path, node
        return
    if isinstance(node, dict):
        for k, v in node.items():
            if not k.startswith("$"):
                yield from walk(v, path + (k,))


def aliases(v):
    if isinstance(v, str):
        return re.findall(r"\{([^{}]+)\}", v)
    if isinstance(v, dict):
        return [a for x in v.values() for a in aliases(x)]
    return []


def check(doc):
    sets = [s for s in ("core", "light", "dark") if s in doc]
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
            elif t["$type"] in ("number", "fontWeight"):
                assert isinstance(v, (int, float)) and not isinstance(v, bool), f"{where}: {t['$type']} is not a number: {v!r}"
    keys = lambda s: sorted(".".join(p) for p, _ in walk(doc[s]))
    if "light" in doc and "dark" in doc:
        assert keys("light") == keys("dark"), "light and dark keys differ"


def build():
    pixel_check()
    doc = {
        "core": core(),
        "light": semantic("light"),
        "dark": semantic("dark"),
        "$themes": [
            {"id": "light", "name": "One Light", "selectedTokenSets": {"core": "source", "light": "enabled"},
             "$description": "Zed's One Light, the owner's light theme; theme.mode set to \"light\" for the capture and restored. Read from screenshots/light/."},
            {"id": "dark", "name": "One Dark", "selectedTokenSets": {"core": "source", "dark": "enabled"},
             "$description": "Zed's One Dark, the owner's dark theme; theme.mode set to \"dark\" for the capture and restored. Read from screenshots/dark/."},
        ],
        "$metadata": {"tokenSetOrder": ["core", "light", "dark"]},
    }
    check(doc)
    (PKG / "tokens.json").write_text(json.dumps(doc, indent=1, ensure_ascii=False) + "\n")
    n = sum(1 for s in ("core", "light", "dark") for _ in walk(doc[s]))
    print(f"tokens.json: {n} tokens; raw/pixel-check.json: {len(PX) * 2} comparisons")


if __name__ == "__main__":
    if not READ or not THEME_FILE or not FONTS:
        raise SystemExit("raw/readings.json, raw/one.json and raw/settings-fonts.json are needed")
    build()
