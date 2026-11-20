#!/usr/bin/env python3
"""Write raw/component-tokens.json — the token spec build_tokens.py turns
into tokens.json.

excalidraw.com declares its design-token layer as custom properties on the
app root: ~170 names on `.excalidraw` (the --color-* palette and semantic
roles, --button-*/*island*/*sidebar*/*popup*/*input*/field/RadioGroup/Switch
component vars, --shadow-* elevations, the --zIndex-* stack, font and size
scales) and ~80 overrides under `.excalidraw.theme--dark`. vars.mjs resolved
every name per theme into raw/css-vars.json; this file groups them into the
DTCG tree.

Leaves either name a resolved variable ("var") or carry a measured value with
its provenance ("source"). Where the stylesheet itself declares a var as an
alias of another var (--button-hover-bg = var(--color-surface-high)), the
token keeps the alias — it is the declaration, not a guess.

  light   the .excalidraw declarations as they resolve in light
  dark    the .excalidraw.theme--dark overrides as they resolve in dark
  core    theme-invariant values: the gray ramp, the --shadow-* elevations,
          the --zIndex-* stack, font families, radii, sizes, spacing
  component   measured geometry from raw/components-computed.json (toolbar
          and island sizes, panel widths, the mobile bar)

Deterministic; no network. Re-run after vars.mjs or measure.mjs.
"""
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
V = json.loads((RAW / "css-vars.json").read_text())
# Required: without the readings every measured token would vanish and the build would still pass.
C = json.loads((RAW / "components-computed.json").read_text())
RL = V["resolved"]["light"]
RD = V["resolved"]["dark"]


def has(var, theme="light"):
    return var in (RL if theme == "light" else RD)


def L(var, ty="color", desc=None):
    """A leaf bound to a resolved variable."""
    if not has(var):
        raise KeyError(f"{var} not resolved")
    return {"type": ty, "var": var, **({"description": desc} if desc else {})}


def declared(var, theme):
    """The stylesheet's own declaration of var in a theme: the .excalidraw.theme--dark rule for
    dark when it overrides var, else the .excalidraw rule (raw/css-vars.json "theme")."""
    rules = {}
    for r in V["theme"]:
        if r["selector"] in (".excalidraw", ".excalidraw.theme--dark") and not r["context"] and var in r["properties"]:
            rules[r["selector"]] = r["properties"][var].strip()
    return rules.get(".excalidraw.theme--dark") if theme == "dark" and ".excalidraw.theme--dark" in rules else rules.get(".excalidraw")


def A(target, target_var, var, theme, desc=None):
    """A leaf that keeps the stylesheet's own var() alias, but only where this theme's declaration
    of var is var(target_var); otherwise the leaf names the resolved variable."""
    if declared(var, theme) != f"var({target_var})":
        return L(var, desc=desc)
    return {"type": "color", "value": "{" + target + "}", "source": f"css-var {var} (declared as var({target_var}) and kept as an alias)", **({"description": desc} if desc else {})}


def M(value, source, ty, desc=None):
    return {"type": ty, "value": value, "source": source, **({"description": desc} if desc else {})}


def px(comp, state="default"):
    st = C["components"].get(comp, {}).get("states", {}).get(state, {})
    return st.get("rect", {})


def style(comp, prop, state="default"):
    return C["components"].get(comp, {}).get("states", {}).get(state, {}).get("style", {}).get(prop)


def measured_dim(value, comp, prop="rect.w", desc=None):
    return {"type": "dimension", "value": f"{value:g}px" if isinstance(value, (int, float)) else value,
            "source": f"measured {comp} {prop} (raw/components-computed.json)", **({"description": desc} if desc else {})}


# ---------------------------------------------------------------- core
core = {"color": {}, "font": {"family": {}, "size": {}, "weight": {}, "lineHeight": {}},
        "radius": {}, "space": {}, "size": {}, "shadow": {}, "zindex": {}, "duration": {}}

# The gray ramp is declared once on .excalidraw and never overridden by
# .theme--dark — it is the shared substrate every themed role picks from.
for s in (10, 20, 30, 40, 50, 60, 70, 80, 85, 90, 100):
    n = f"--color-gray-{s}"
    if has(n):
        core["color"].setdefault("gray", {})[str(s)] = L(n, desc="The neutral ramp (10 near-white to 100 near-black); theme-invariant — dark rebinds the roles that point into it.")

# Fonts: --ui-font is the declared interface stack; the canvas families come
# from the served @font-face rules and the computed fontFamily of canvas text
# (the welcome logo is the hand-drawn face).
core["font"]["family"]["ui"] = {**L("--ui-font", "fontFamily", "The declared UI stack — Assistant over the system sanses."), "source": "css-var --ui-font"}
display = style("welcome-logo", "fontFamily")
if not display:
    raise SystemExit("welcome-logo default has no computed fontFamily in raw/components-computed.json; recapture it")
core["font"]["family"]["display"] = M(display,
                                      "computed fontFamily of welcome-logo default (raw/components-computed.json)",
                                      "fontFamily", "The hand-drawn face: welcome logo and default canvas handwriting.")
# No reading holds a monospace stack: no measured element computes Cascadia and raw/css-vars.json
# has no @font-face for it. The value was entered by hand at capture time.
core["font"]["family"]["mono"] = M('"Cascadia", ui-monospace, monospace',
                                    "Reconstruction: entered by hand at capture time; no measured element or @font-face in raw/ holds it",
                                    "fontFamily", "The monospace face for code elements and keybindings.")

# Measured type scale: sizes read off the real controls.
sizes = {}
for tok, comp, prop, desc in [
    ("logo", "welcome-logo", "fontSize", "The 36px hand-drawn welcome wordmark."),
    ("heading", "welcome-heading", "fontSize", "The 18px welcome heading."),
    ("body", "menu-item", "fontSize", "Menu row text."),
    ("hint", "welcome-panel", "fontSize", "Small UI text (hints, footers)."),
    ("label", "prop-label", "fontSize", "The 12px sidebar property labels and small buttons."),
    ("keyhint", "keycap", "fontSize", "Shortcut keycap text."),
]:
    v = style(comp, prop)
    if v:
        sizes[tok] = measured_dim(v, comp, "fontSize", desc)
core["font"]["size"] = sizes
wt = style("export-png", "fontWeight")
if wt:
    core["font"]["weight"]["button"] = M(int(float(wt)), "measured export-png fontWeight", "fontWeight", "Control label weight.")
lh = style("cmdk-input", "lineHeight")
if lh:
    core["font"]["lineHeight"]["control"] = measured_dim(lh, "cmdk-input", "lineHeight", "The 16px/24px input line height (menu rows compute 'normal').")

# Radii and spacing: the declared --border-radius-* and --space-factor grid.
for tok, var in [("md", "--border-radius-md"), ("lg", "--border-radius-lg")]:
    if has(var):
        core["radius"][tok] = L(var, "dimension", "The declared corner radii — 6px controls, 8px cards/islands.")
r = px("tool-island")
for tok, val, comp, prop, desc in [
    ("toolbar", style("tool-rect", "borderTopLeftRadius"), "tool-rect", "borderRadius", "Tool-button corner inside the island."),
]:
    if val:
        core["radius"].setdefault("control", measured_dim(val, comp, prop, desc))
for tok, var in [("factor", "--space-factor"), ("container-x", "--container-padding-x"),
                 ("container-y", "--container-padding-y"), ("editor-pad", "--editor-container-padding"),
                 ("safe-top", "--sat"), ("safe-right", "--sar"), ("safe-bottom", "--sab"), ("safe-left", "--sal"),
                 ("userlist-pad", "--userList-padding"), ("avatarlist-gap", "--avatarList-gap")]:
    if has(var):
        core["space"][tok] = L(var, "dimension", "Declared spacing — the 4px factor and the shell paddings.")

# Declared control sizes.
for tok, var, desc in [
    ("button", "--default-button-size", "Standard square tool/icon button (32px)."),
    ("button-lg", "--lg-button-size", "Large button — the 36px toolbar controls."),
    ("icon", "--default-icon-size", "Standard inline icon."),
    ("icon-lg", "--lg-icon-size", "Large toolbar icon."),
    ("avatar", "--avatar-size", "Collaborator avatar."),
    ("mobile-action", "--mobile-action-button-size", "Phone-size action button."),
    ("slider-thumb", "--slider-thumb-size", "Range-thumb diameter."),
]:
    if has(var):
        core["size"][tok] = L(var, "dimension", desc)

# Elevations: the declared --shadow-* set is theme-invariant.
for tok, var, desc in [
    ("island", "--shadow-island", "The floating-toolbar card shadow — hairline + soft lift."),
    ("island-stronger", "--shadow-island-stronger", "The stronger island variant."),
    ("modal", "--modal-shadow", "The dialog drop shadow — also the sidebar's."),
    ("sidebar", "--sidebar-shadow", "The library/properties panel elevation."),
    ("library-dropdown", "--library-dropdown-shadow", "The library overflow menu shadow."),
    ("chat-msg", "--chat-msg-shadow", "The collaboration chat bubble shadow."),
]:
    if has(var):
        v = RL[var].get("value", RL[var]["raw"])
        if isinstance(v, str) and v != "none":
            layers = []
            for part in re.split(r",\s*(?=rgba?|#)", v):
                m = re.match(r"(.+?)\s+(-?[\d.]+)px\s+(-?[\d.]+)px\s+(-?[\d.]+)px(?:\s+(-?[\d.]+)px)?\s*$", part.strip())
                if m:
                    layers.append({"color": m.group(1), "offsetX": m.group(2) + "px", "offsetY": m.group(3) + "px",
                                   "blur": m.group(4) + "px", "spread": (m.group(5) or "0") + "px"})
            if layers:
                core["shadow"][tok] = {"type": "shadow", "value": layers, "source": f"css-var {var} (parsed)", **({"description": desc} if desc else {})}
            else:
                core["shadow"][tok] = L(var, "shadow", desc)

# The paint-order scale.
for n in sorted(set(k for k in RL if k.startswith("--zIndex-"))):
    tok = n[len("--zIndex-"):]
    core["zindex"][re.sub(r"[^a-zA-Z0-9-]", "-", tok)] = L(n, "number", "The declared stacking order — canvas 1, UI layers, menus 110, modal 1000, toast 999999.")

# Motion: transitions measured on the real controls (no --duration vars exist).
dur = style("tool-rect", "transitionDuration") or style("menu-item", "transitionDuration")
if dur:
    core["duration"]["control"] = M(dur.split(",")[0].strip(), "measured tool-rect transitionDuration", "duration", "The control-state transition.")

# ---------------------------------------------------------------- themes
# The shared semantic map: every --color-*/role var resolved per theme.
# (token path, var name, alias target or None, description)
THEMED = [
    # brand ramp — the violet primary flips to a lighter tint in dark
    ("color.brand.default", "--color-primary", None, "The signature violet — accent, selection, active radio fills."),
    ("color.brand.hover", "--color-brand-hover", None, None),
    ("color.brand.active", "--color-brand-active", None, None),
    ("color.brand.darker", "--color-primary-darker", None, None),
    ("color.brand.darkest", "--color-primary-darkest", None, None),
    ("color.brand.light", "--color-primary-light", None, "The soft violet wash behind selected swatches."),
    ("color.brand.light-darker", "--color-primary-light-darker", None, None),
    ("color.brand.contrast-offset", "--color-primary-contrast-offset", None, None),
    ("color.brand.selection", "--color-selection", None, "Canvas selection / highlight accent."),
    ("color.brand.on-primary-container", "--color-on-primary-container", None, "Ink on the primary-container fill."),
    ("color.brand.primary-container", "--color-surface-primary-container", None, "The primary container fill."),
    ("color.brand.promo", "--color-promo", "color.brand.default", "The Excalidraw+ promo accent (declared = primary)."),
    # surfaces — the stepped UI grounds
    ("color.surface.lowest", "--color-surface-lowest", None, "The deepest surface — the page ground and on-brand ink."),
    ("color.surface.low", "--color-surface-low", None, "Field background (ExcTextField, RadioGroup off)."),
    ("color.surface.mid", "--color-surface-mid", None, "The mid-step surface."),
    ("color.surface.high", "--color-surface-high", None, "Hover/active fills, hairline borders."),
    # ink
    ("color.text.primary", "--color-on-surface", None, "Primary ink — also --text-primary-color and --icon-fill-color."),
    ("color.text.warning", "--color-text-warning", None, "Ink on the warning fill."),
    # borders
    ("color.border.default", "--default-border-color", "color.surface.high", "The default control border (declared = surface-high)."),
    ("color.border.subtle", "--color-outline", None, "The faint hairline (gray-20 light / gray-80 dark)."),
    ("color.border.dialog", "--dialog-border-color", None, "Dialog edge."),
    ("color.border.list", "--list-border-color", None, "List row hairline."),
    ("color.border.outline", "--color-border-outline", None, "The stronger outline."),
    ("color.border.outline-variant", "--color-border-outline-variant", None, "The softer outline."),
    ("color.border.input", "--input-border-color", None, "Field border."),
    # icons
    ("color.icon.fill", "--icon-fill-color", "color.text.primary", "Icon ink (declared = on-surface)."),
    ("color.icon.white", "--color-icon-white", None, "The 'white' icon — inverts to near-black in dark."),
    ("color.icon.green", "--icon-green-fill-color", None, "The success-green icon fill."),
    # links
    ("color.link.default", "--link-color", None, "Inline link blue."),
    ("color.link.hover", "--link-color-hover", None, None),
    ("color.link.active", "--link-color-active", None, None),
    # logo
    ("color.logo.icon", "--color-logo-icon", "color.brand.default", "The logo glyph (declared = primary)."),
    ("color.logo.text", "--color-logo-text", None, "The logo wordmark ink."),
    # muted family
    ("color.muted.default", "--color-muted", None, "Muted gray fill — gray-30 light / gray-80 dark."),
    ("color.muted.darker", "--color-muted-darker", None, None),
    ("color.muted.darkest", "--color-muted-darkest", None, None),
    ("color.muted.background", "--color-muted-background", None, None),
    ("color.muted.background-darker", "--color-muted-background-darker", None, None),
    # status
    ("color.success.default", "--color-success", None, "The green success fill."),
    ("color.success.contrast", "--color-success-contrast", None, None),
    ("color.success.contrast-hover", "--color-success-contrast-hover", None, None),
    ("color.success.contrast-active", "--color-success-contrast-active", None, None),
    ("color.success.darker", "--color-success-darker", None, None),
    ("color.success.darkest", "--color-success-darkest", None, None),
    ("color.success.text", "--color-success-text", None, None),
    ("color.warning.default", "--color-warning", None, "The amber warning fill."),
    ("color.warning.dark", "--color-warning-dark", None, None),
    ("color.warning.darker", "--color-warning-darker", None, None),
    ("color.warning.darkest", "--color-warning-darkest", None, None),
    ("color.warning.color", "--color-warning-color", None, "Ink on warning (primary text light / gray-80 dark)."),
    ("color.warning.icon-background", "--color-warning-icon-background", None, None),
    ("color.warning.icon-color", "--color-warning-icon-color", None, None),
    ("color.danger.default", "--color-danger", None, "The red danger accent."),
    ("color.danger.dark", "--color-danger-dark", None, None),
    ("color.danger.darker", "--color-danger-darker", None, None),
    ("color.danger.darkest", "--color-danger-darkest", None, None),
    ("color.danger.background", "--color-danger-background", None, "The pink danger wash."),
    ("color.danger.color", "--color-danger-color", None, "Danger text."),
    ("color.danger.icon-background", "--color-danger-icon-background", None, None),
    ("color.danger.icon-color", "--color-danger-icon-color", None, None),
    ("color.badge.bg", "--background-color-badge", None, "The green badge pill fill."),
    ("color.badge.text", "--color-badge", None, "Badge ink."),
    ("color.disabled", "--color-disabled", None, "Disabled ink/icon (gray-40 light / gray-70 dark)."),
    ("color.slider.track", "--color-slider-track", None, "The range track."),
    ("color.slider.thumb", "--color-slider-thumb", None, "The range thumb (gray-80 both themes)."),
    ("color.select.highlight", "--select-highlight-color", None, "The blue selection highlight."),
    ("color.focus.highlight", "--focus-highlight-color", None, "The focus-highlight wash — sky light / blue dark."),
    ("color.canvas.default-bg", "--default-bg-color", None, "The canvas default background — white / near-black."),
    ("color.overlay.bg", "--overlay-bg-color", None, "The modal scrim — 35% ink light, 65% dark."),
    ("color.popup.bg", "--popup-bg-color", None, "Popover surface (= island bg)."),
    ("color.popup.bg-secondary", "--popup-secondary-bg-color", None, "Secondary popover surface."),
    ("color.popup.text", "--popup-text-color", None, None),
    ("color.popup.text-inverted", "--popup-text-inverted-color", None, None),
    ("color.mobile-action.bg", "--mobile-action-button-bg", None, "Translucent phone action fill."),
    ("color.keybinding", "--keybinding-color", None, "The shortcut-hint gray (gray-40 light / gray-60 dark)."),
    # controls
    ("control.button.hover-bg", "--button-hover-bg", "color.surface.high", "Button hover fill (declared = surface-high)."),
    ("control.button.active-bg", "--button-active-bg", "color.surface.high", "Button pressed fill."),
    ("control.button.active-border", "--button-active-border", "color.brand.active", "Pressed button edge (= brand-active)."),
    ("control.button.destructive-bg", "--button-destructive-bg-color", None, "Destructive hover wash."),
    ("control.button.destructive-color", "--button-destructive-color", None, "Destructive ink."),
    ("control.button.special-active-bg", "--button-special-active-bg-color", None, "The green 'special' active fill (e.g. theme choice)."),
    ("control.button.gray-1", "--button-gray-1", None, "Neutral button step 1 — flips dark in dark theme."),
    ("control.button.gray-2", "--button-gray-2", None, None),
    ("control.button.gray-3", "--button-gray-3", None, None),
    ("control.island.bg", "--island-bg-color", None, "The floating-toolbar/popover card surface."),
    ("control.island.bg-alt", "--island-bg-color-alt", None, "The alternate island surface."),
    ("control.sidebar.bg", "--sidebar-bg-color", None, "Panel surface (= island bg)."),
    ("control.sidebar.border", "--sidebar-border-color", "color.surface.high", "Panel hairline (= surface-high)."),
    ("control.field.bg", "--ExcTextField--background", "color.surface.low", "ExcTextField fill (= surface-low)."),
    ("control.field.border", "--ExcTextField--border", None, "Field border."),
    ("control.field.border-hover", "--ExcTextField--border-hover", "color.brand.hover", "Field hover border (= brand-hover)."),
    ("control.field.border-active", "--ExcTextField--border-active", "color.brand.active", "Field focus border (= brand-active)."),
    ("control.field.text", "--ExcTextField--color", "color.text.primary", "Field ink (= on-surface)."),
    ("control.field.label", "--ExcTextField--label-color", "color.text.primary", "Field label ink."),
    ("control.field.placeholder", "--ExcTextField--placeholder", None, "Placeholder gray."),
    ("control.field.readonly-bg", "--ExcTextField--readonly--background", "color.surface.high", "Read-only field fill."),
    ("control.field.readonly-border", "--ExcTextField--readonly--border", None, None),
    ("control.field.readonly-text", "--ExcTextField--readonly--color", "color.text.primary", None),
    ("control.input.bg", "--input-bg-color", None, "Native input fill."),
    ("control.input.hover-bg", "--input-hover-bg-color", None, None),
    ("control.input.label", "--input-label-color", None, None),
    ("control.radio.bg", "--RadioGroup-background", None, "Segmented-control track (= island bg)."),
    ("control.radio.border", "--RadioGroup-border", None, "Track hairline (= surface-high)."),
    ("control.radio.choice-on-bg", "--RadioGroup-choice-background-on", None, "Selected segment fill (= primary)."),
    ("control.radio.choice-on-bg-hover", "--RadioGroup-choice-background-on-hover", "color.brand.hover", None),
    ("control.radio.choice-on-bg-active", "--RadioGroup-choice-background-on-active", "color.brand.active", None),
    ("control.radio.choice-off-bg", "--RadioGroup-choice-background-off", None, None),
    ("control.radio.choice-off-bg-active", "--RadioGroup-choice-background-off-active", "color.surface.high", None),
    ("control.radio.choice-on-text", "--RadioGroup-choice-color-on", None, "Ink on the selected segment."),
    ("control.radio.choice-off-text", "--RadioGroup-choice-color-off", "color.brand.default", "Unselected segment ink (= primary)."),
    ("control.radio.choice-off-text-hover", "--RadioGroup-choice-color-off-hover", "color.brand.hover", None),
    ("control.switch.track", "--Switch-track-background", None, "Switch track (= island bg)."),
    ("control.switch.thumb", "--Switch-thumb-background", "color.text.primary", "Switch thumb (= on-surface)."),
    ("control.switch.hover", "--Switch-hover-background", "color.brand.hover", None),
    ("control.switch.active", "--Switch-active-background", "color.brand.active", None),
    ("control.switch.disabled", "--Switch-disabled-color", "color.border.outline", None),
    ("control.switch.disabled-border", "--Switch-disabled-border", "color.border.outline-variant", None),
    ("control.switch.disabled-toggled", "--Switch-disabled-toggled-background", "color.border.outline-variant", None),
    ("control.scrollbar.thumb", "--scrollbar-thumb", "control.button.gray-2", "Scrollbar thumb (light declares it as button-gray-2; dark declares its own value)."),
    ("control.scrollbar.thumb-hover", "--scrollbar-thumb-hover", "control.button.gray-3", None),
    ("control.export.preview-border", "--ImageExportModal-preview-border", None, "The export preview pane edge."),
    ("control.userlist.hint-bg", "--userlist-hint-bg-color", None, "Collaborator list hint surface."),
    ("control.userlist.hint-heading", "--userlist-hint-heading-color", None, None),
    ("control.userlist.hint-text", "--userlist-hint-text-color", None, None),
    ("control.userlist.collaborators-border", "--userlist-collaborators-border-color", None, None),
    ("control.avatar.border", "--avatar-border-color", None, "Avatar ring."),
]


def insert(tree, path, leaf):
    node = tree
    parts = path.split(".")
    for p in parts[:-1]:
        node = node.setdefault(p, {})
    node[parts[-1]] = leaf


VAR_OF = {path: var for path, var, _, _ in THEMED}
light, dark = {}, {}
for path, var, alias, desc in THEMED:
    for tree, theme in ((light, "light"), (dark, "dark")):
        if not has(var, theme):
            continue
        leaf = A(alias, VAR_OF[alias], var, theme, desc) if alias else L(var, desc=desc)
        insert(tree, path, leaf)

# ---------------------------------------------------------------- component geometry
component = {}


def add_dim(path, comp, prop, val=None, desc=None):
    v = val if val is not None else style(comp, prop)
    if v is None:
        return
    # flex/grid gap and friends compute to keywords ('normal', 'normal 10px')
    # when unset — only a real length may become a dimension token.
    if isinstance(v, str) and not re.fullmatch(r"-?\d+(\.\d+)?(px|rem)", v.strip()):
        return
    insert(component, path, measured_dim(v, comp, prop, desc))


add_dim("toolbar.island-h", "tool-island", "rect.h", val=px("tool-island").get("h"), desc="The floating toolbar Island height — 44px of 36px buttons + padding.")
add_dim("toolbar.button", "tool-rect", "rect.w", val=px("tool-rect").get("w"), desc="Square tool button — 36px inside the 44px island.")
add_dim("toolbar.gap", "tool-island", "columnGap", val=style("tool-island", "columnGap"), desc="The tool-row gap (0px — the island packs its buttons with padding, not gap).")
add_dim("toolbar.pad", "tool-island", "paddingTop", val=style("tool-island", "paddingTop"), desc="Island padding around the buttons.")
add_dim("toolbar.radius", "tool-island", "borderTopLeftRadius", val=style("tool-island", "borderTopLeftRadius"), desc="The island's outer corner.")
add_dim("footer.zoom-h", "zoom-btn", "rect.h", val=px("zoom-btn").get("h"), desc="The zoom pill in the footer.")
add_dim("props.width", "props-panel", "rect.w", val=px("props-panel").get("w"), desc="The left properties sidebar width.")
add_dim("library.width", "lib-panel", "rect.w", val=px("lib-panel").get("w"), desc="The library panel width.")
add_dim("welcome.width", "welcome-panel", "rect.w", val=px("welcome-panel").get("w"), desc="The welcome sheet width on the canvas.")
add_dim("menu.item-h", "menu-item", "rect.h", val=px("menu-item").get("h"), desc="A dropdown menu row.")
add_dim("menu.item-radius", "menu-item", "borderTopLeftRadius", val=style("menu-item", "borderTopLeftRadius"), desc="Menu-row corner.")
add_dim("mobile.toolbar-h", "m-toolbar", "rect.h", val=px("m-toolbar").get("h"), desc="The phone toolbar height.")
add_dim("mobile.actions-h", "m-shape-actions", "rect.h", val=px("m-shape-actions").get("h"), desc="The phone compact-shape-actions bar.")

out = {"core": core, "light": light, "dark": dark, "component": component}
RAW.mkdir(exist_ok=True)
(RAW / "component-tokens.json").write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")


def count(d):
    return sum(count(v) for v in d.values()) if isinstance(d, dict) and "type" not in d else 1


print({k: count(v) for k, v in out.items()})
