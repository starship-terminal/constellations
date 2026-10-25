#!/usr/bin/env python3
"""Write components.md from the inventory below, tokens.json and components/crops/.

    python3 tools/build_components_md.py

Adapted from the native kit (systems/grokbot). Every value in an entry is a token path; the builder
refuses a path tokens.json lacks and a crop that is not on disk, so the page cannot drift from the
package. Standard library only, deterministic.
"""
import json
import pathlib

PKG = pathlib.Path(__file__).resolve().parent.parent
TOK = json.loads((PKG / "tokens.json").read_text())
CROPS = PKG / "components" / "crops"


def paths(node, pre=()):
    if isinstance(node, dict) and "$value" in node:
        yield ".".join(pre)
        return
    if isinstance(node, dict):
        for k, v in node.items():
            if not k.startswith("$"):
                yield from paths(v, pre + (k,))


KNOWN = set(paths(TOK["core"])) | set(paths(TOK["dark"]))
NAME = "Zed"

# (component, checklist item, what it is, [(property, token path)], [(state, crop stem)], notes)
INVENTORY = [
    ("Button", "button", "Small bordered or ghost buttons: 'Restart to Update' in the title bar, 'Edit in settings.json' and 'Fix in settings.json' in Settings, Install and Uninstall on extension cards.",
     [("fill", "component.button.bg"), ("label", "component.button.text"), ("border", "role.border.default"), ("height", "size.button"), ("corner", "radius.sm"), ("hover fill", "role.control.ghostHover"), ("label type", "typography.label")],
     [("default", "button-default"), ("hover", "button-hover"), ("in Settings", "button-edit-json")],
     "No button is filled with the accent; Zed's buttons are ghost or bordered and change fill on hover. The pointer was over 'Restart to Update' in button-hover, but the capture shows no visible change, so its hover may be subtler than one quantised step."),
    ("Icon button", "icon button", "Ghost icon buttons in the tab bar (new, split, zoom), the status bar (panels) and the agent panel header.",
     [("hover fill", "role.control.ghostHover"), ("icon", "theme.icon.default"), ("active icon", "theme.icon.accent"), ("corner", "radius.sm")],
     [("default", "icon-button-default"), ("hover", "icon-button-hover")],
     "Hover fills a rounded square behind the glyph with `ghost_element.hover`. In the status bar the toggled panel's icon turns accent blue (terminal-panel)."),
    ("Link", "link", "Links in agent replies and the Markdown preview: accent text, underlined.",
     [("colour", "role.text.link"), ("type", "typography.body")],
     [("in a reply", "agent-result"), ("in Markdown", "markdown-preview")], ""),
    ("Text field", "text field", "The settings search field, the palette and picker query fields, the buffer search bar.",
     [("fill", "component.input.bg"), ("border", "role.border.default"), ("focus border", "role.border.focus"), ("placeholder", "role.text.placeholder"), ("height", "size.control"), ("palette query height", "size.paletteQuery"), ("corner", "radius.sm")],
     [("settings search, typed", "search-settings-typed"), ("buffer search", "buffer-search-bar"), ("palette, empty", "palette-empty"), ("palette, typed", "palette-typed")],
     "Query fields inside the palette have no border of their own; a divider separates them from the list."),
    ("Text area", "text area", "The agent composer: a multi-line field in the buffer font, with mode, model, effort and profile selectors and a send button under it.",
     [("fill", "component.input.bg"), ("placeholder", "role.text.placeholder"), ("send button", "size.sendButton"), ("text type", "typography.code")],
     [("empty", "composer-empty"), ("typed", "composer-typed")], ""),
    ("Select", "select", "Settings selects ('Platform Default'), with a chevron pair; the agent model and mode pickers open a searchable list.",
     [("fill", "component.select.bg"), ("border", "role.border.subtle"), ("height", "size.control"), ("corner", "radius.sm"), ("selected row", "role.accent.selected")],
     [("default", "select-default"), ("agent model, open", "select-agent-model")], ""),
    ("Stepper", "select", "A number with minus and plus buttons (Menu Delay, font sizes, panel widths).",
     [("fill", "role.control.default"), ("border", "role.border.subtle"), ("corner", "radius.sm")],
     [("default", "stepper-default")], ""),
    ("Checkbox", "checkbox", "The git panel's stage boxes (one per file and group).",
     [("border", "role.border.default")],
     [("unchecked", "git-panel")], "Only unchecked boxes were captured; no file was staged."),
    ("Radio and segmented control", "radio", "Segmented buttons: Light, Dark, System and the keymap grid on the onboarding page; All, Installed, Not Installed on the extensions page.",
     [("selected fill", "role.accent.selected"), ("border", "role.border.default"), ("corner", "radius.sm")],
     [("onboarding", "onboarding-panel"), ("extensions filter", "segmented-tabs-extensions")], ""),
    ("Switch", "switch", "Settings switches: a pill track with a round thumb.",
     [("width", "size.switch.width"), ("height", "size.switch.height"), ("thumb", "size.switch.thumb"), ("off track", "role.control.default"), ("on track", "role.control.switchOn"), ("corner", "radius.full")],
     [("off", "switch-off"), ("on", "switch-on")],
     "The on colour is a muted accent that no single theme key gives (README What to distrust)."),
    ("Tabs", "tabs", "Editor tabs in the tab bar, and small tab strips in pickers (Branches, Stashes) and the git panel (Changes, History).",
     [("bar fill", "component.tab.bg"), ("active fill", "component.tab.activeBg"), ("inactive label", "component.tab.text"), ("height", "component.tab.height"), ("label inset", "spacing.6"), ("width", "size.tab")],
     [("two tabs", "tab-bar-default"), ("hover", "tab-hover"), ("picker tabs", "branch-picker-tabs")],
     "The active tab takes the editor's fill and drops the line under it, so it joins the buffer. A modified file's tab label is drawn in the git `modified` colour."),
    ("Menu", "menu", "Context menus on files, the editor and tabs; the user menu; agent menus (mode, effort, profile, attach, new thread, options).",
     [("fill", "component.menu.bg"), ("item", "component.menu.text"), ("disabled item", "role.text.disabled"), ("border", "role.border.subtle"), ("corner", "component.menu.radius"), ("width", "size.menuWidth"), ("item inset", "spacing.3")],
     [("file", "menu-file"), ("editor", "menu-editor"), ("tab", "menu-tab"), ("user", "menu-user"), ("agent mode", "menu-agent-mode"), ("agent effort", "menu-agent-effort"), ("agent profile", "menu-agent-profile"), ("agent attach", "menu-agent-attach"), ("new thread", "menu-agent-new-thread"), ("agent options", "menu-agent-options")],
     "Key bindings sit right-aligned in muted text; separators are a 1 pt `border.variant` line."),
    ("Command palette and pickers", "menu", "The command palette, file finder, theme selector and outline picker share one shape: a query field, a list with one selected row, and a footer of actions.",
     [("fill", "component.palette.bg"), ("selected row", "role.accent.selected"), ("width", "size.paletteWidth"), ("row", "size.paletteRow"), ("corner", "radius.lg"), ("match highlight", "role.text.link")],
     [("palette", "palette-empty"), ("palette, selected", "palette-selected"), ("file finder", "file-finder-empty"), ("file finder, typed", "file-finder-typed"), ("theme selector", "theme-selector"), ("outline", "outline-picker"), ("branch picker", "branch-picker-tabs")], ""),
    ("Tooltip", "tooltip", "A label with its key binding, on hover; long paths in the file tree get one too.",
     [("fill", "component.tooltip.bg"), ("text", "component.tooltip.text"), ("binding", "role.text.secondary"), ("height", "size.tooltip"), ("corner", "radius.lg")],
     [("status bar", "tooltip-default"), ("path", "tooltip-path")], ""),
    ("Dialog", "dialog", "Confirmations use the macOS system prompt (the owner's 'Use System Prompts' is on), so they are drawn by AppKit, not by Zed's theme.",
     [],
     [("trash confirmation", "dialog-confirm-trash")], "Cancel was pressed; the file was kept. The prompt's blue is the system accent, not `text.accent`, and the dimming behind it is the system's; no scrim value was read."),
    ("Banner", "toast", "Inline notices: 'Your settings are out of date' in Settings, on the warning fill.",
     [("fill", "role.status.warningBg"), ("icon", "role.status.warning"), ("text", "role.text.primary")],
     [("warning", "banner-warning")], "No toast appeared during the capture; the title bar's 'Restart to Update' button is how Zed announced the pending update."),
    ("Card", "card", "Extension cards; terminal and file-write cards in agent replies.",
     [("fill", "role.surface"), ("border", "role.border.subtle"), ("corner", "radius.md"), ("card header", "size.toolCardHeader")],
     [("extension", "card-extension"), ("tool card, running", "tool-card-running"), ("file write", "agent-edit-result")], ""),
    ("List row", "list row", "File-tree rows, settings rows (label, description, control), keymap rows.",
     [("height", "size.treeRow"), ("selected", "role.accent.selected"), ("hover", "role.control.ghostHover"), ("label type", "typography.label"), ("description type", "typography.labelSmall")],
     [("file tree", "file-tree-default"), ("settings row", "list-row-settings"), ("hover", "list-row-hover"), ("settings nav, selected", "settings-nav-selected")],
     "Git status colours the file name (modified yellow, untracked green) and a letter at the row's end."),
    ("Table", "table", "The keymap editor: Action, Arguments, Keystrokes, Context, Source columns with zebra rows.",
     [("row fill", "role.page"), ("alternate row", "role.surface"), ("text", "role.text.primary"), ("context", "role.text.secondary")],
     [("keymap editor", "table-keymap")], "Agent replies render Markdown tables too (agent-result, dark)."),
    ("Avatar", "avatar", "The owner's round profile picture at the title bar's right edge.",
     [],
     [("title bar", "button-default")], "Its size was not measured; it sits in the 34 pt title bar beside the 24 pt button."),
    ("Badge", "badge", "Count and status marks: the diagnostics count, the git letters in the tree, the 'Free' plan tag in the user menu, extension category tags.",
     [("error", "role.status.danger"), ("modified", "theme.modified.default"), ("created", "theme.created.default")],
     [("tree letters", "file-tree-default"), ("plan tag", "menu-user"), ("category tags", "card-extension")], ""),
    ("Editor", "pattern", "The buffer: line numbers, the git gutter, indent guides, the active line, inline blame, diagnostics, multi-cursor selections.",
     [("fill", "role.page"), ("active line", "theme.editor.active_line.background"), ("line number", "theme.editor.line_number"), ("added", "role.git.added"), ("modified", "role.git.modified"), ("selection", "role.selection"), ("cursor", "role.cursor"), ("type", "typography.code"), ("line", "size.bufferLine")],
     [("gutter and syntax", "editor-gutter-git"), ("multi-cursor", "editor-multi-cursor"), ("diagnostic hover", "diagnostic-hover"), ("completions", "completions-menu")], ""),
    ("Diff, diagnostics and search", "pattern", "The project diff (split), the diagnostics view and project search: multibuffers of excerpts with headers.",
     [("added", "theme.version_control.added"), ("deleted", "theme.version_control.deleted"), ("match", "role.search.match"), ("subheader", "theme.editor.subheader.background")],
     [("diff", "diff-split"), ("diagnostics", "diagnostics-panel"), ("project search", "project-search")], ""),
    ("Panels and bars", "pattern", "Title bar, breadcrumb toolbar, status bar, the terminal panel and the git panel.",
     [("title bar", "size.titleBar"), ("toolbar", "size.toolbar"), ("status bar", "size.statusBar"), ("panel fill", "role.surface"), ("chrome fill", "role.chrome"), ("terminal", "theme.terminal.background")],
     [("title bar", "title-bar-default"), ("toolbar", "breadcrumb-toolbar"), ("status bar", "status-bar-default"), ("terminal", "terminal-panel"), ("git panel", "git-panel")], ""),
    ("Agent thread", "pattern", "The agent panel: a user message box, a running state with a stop button, tool cards, and rendered Markdown replies.",
     [("message fill", "component.userMessage.bg"), ("message corner", "component.userMessage.radius"), ("message padding", "component.userMessage.padding"), ("reply type", "typography.body"), ("heading", "typography.heading"), ("stop", "role.status.danger")],
     [("loading", "agent-loading"), ("running", "agent-running"), ("result", "agent-result"), ("tool running", "tool-card-running"), ("file written", "agent-edit-result")], ""),
]

GAPS = [
    ("Toast", "Not seen: no action in the capture raised one."),
    ("Pressed state", "Not captured: stills only. The theme declares it (`element.active`, `ghost_element.active`)."),
    ("Focus ring", "Zed draws focus as `border.focused` on some elements; no keyboard-focus ring was captured on a control."),
    ("Disabled controls", "Disabled menu items (Paste, Undo, Redo, Close Right) were captured; no disabled button or switch."),
    ("Error state in a form", "Not present in Settings; validation errors were not seen."),
    ("Approval prompt in the agent panel", "Not captured: the Claude Agent ran in its Auto mode, which approved both harmless actions inside the scratch folder without asking."),
    ("Radio button", "Not present as a round radio; Zed uses segmented buttons."),
    ("Motion", "Not captured: stills only."),
]


def main():
    out = [f"# {NAME} components", "",
           "Generated by `tools/build_components_md.py` from its inventory, [tokens.json](tokens.json) and [components/crops/](components/crops). "
           "Colour paths are in the `light` and `dark` sets (they alias Zed's own theme keys under `theme.*`); other paths are in `core`. "
           "Crops are cut from the 256-colour screenshots by `tools/crops.py`, so they show layout and state, never exact colour.", ""]
    for name, item, what, props, states, notes in INVENTORY:
        for _, path in props:
            if path not in KNOWN:
                raise SystemExit(f"{name}: unknown token {path}")
        out += [f"## {name}", "", f"Checklist item: {item}. {what}", "", "| Property | Token |", "|---|---|"]
        out += [f"| {p} | `{path}` |" for p, path in props]
        out.append("")
        cells = []
        for state, stem in states:
            for suffix, theme in (("", "dark"), ("-light", "light")):
                f = CROPS / f"{stem}{suffix}.png"
                if f.exists():
                    cells.append(f"[{state} ({theme})](components/crops/{f.name})")
                elif not suffix:
                    raise SystemExit(f"{name}: no crop {f.name}")
        out += ["Crops: " + ", ".join(cells) + ".", ""]
        if notes:
            out += [notes, ""]
    out += ["## Gaps", "", "| Item | Status |", "|---|---|"] + [f"| {a} | {b} |" for a, b in GAPS] + [""]
    (PKG / "components.md").write_text("\n".join(out))
    print("components.md:", len(INVENTORY), "components")


if __name__ == "__main__":
    main()
