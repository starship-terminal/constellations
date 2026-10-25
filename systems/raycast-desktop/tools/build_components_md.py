#!/usr/bin/env python3
"""Write components.md from the inventory below, tokens.json and components/crops/ (native kit).

Adapted from systems/grokbot: NAME, INVENTORY and GAPS are Raycast's.

    python3 tools/build_components_md.py

Every value in an entry is a token path; the builder refuses a path tokens.json lacks and a crop
that is not on disk, so the page cannot drift from the package. Standard library only, deterministic.
"""
import json
import pathlib

PKG = pathlib.Path(__file__).resolve().parent.parent
TOK = json.loads((PKG / "tokens.json").read_text())
CROPS = PKG / "components" / "crops"
THEMES_OF = {}
for _c in json.loads((PKG / "tools" / "crops.json").read_text())["crops"]:
    THEMES_OF.setdefault(_c["name"], set()).update(_c["themes"])


def paths(node, pre=()):
    if isinstance(node, dict) and "$value" in node:
        yield ".".join(pre)
        return
    if isinstance(node, dict):
        for k, v in node.items():
            if not k.startswith("$"):
                yield from paths(v, pre + (k,))


KNOWN = set(paths(TOK["core"])) | set(paths(TOK["dark"]))

NAME = "Raycast"

# (component, checklist item, what it is, [(property, token path)], [(state, crop stem)], notes)
INVENTORY = [
    ("Search field", "text field", "The launcher's header: one borderless field across the top of the window, the Raycast mark to its left. It filters everything below it as you type.",
     [("header height", "size.mainWindow.header"), ("text", "text.primary"), ("placeholder", "text.placeholder"), ("type", "typography.extraLargeText")],
     [("empty", "search-field-empty"), ("typed", "search-field-typed")],
     "No box, no border and no focus ring: the caret is the only focus cue. The type size is Derived from a capital (see typography.extraLargeText)."),
    ("List row", "list row", "Every launcher result: a 22 pt icon, a title, a dimmer subtitle, and accessories (type, keyword, badges) pushed to the right.",
     [("height", "component.list.row.height"), ("corner", "component.list.row.radius"), ("inset", "size.listInset"), ("hover fill", "component.list.row.hoverBg"),
      ("selected fill", "component.list.row.selectedBg"), ("title", "component.list.row.title"), ("subtitle", "component.list.row.subtitle"), ("type", "typography.text"),
      ("icon", "size.icon.22")],
     [("default", "list-row-default"), ("selected", "list-row-selected"), ("hover", "list-row-hover"), ("selection moved with arrow keys", "list-row-selected-moved")],
     "Selection and hover are the same white (dark) or black (light) at 10% and 5%. Disabled rows drop to 30% opacity (declared, not seen)."),
    ("Section header", "list row", "Small secondary label over each group of results (Suggestions, Commands, Results, Files).",
     [("text", "component.list.sectionHeader.text"), ("type", "typography.smallText")],
     [("Suggestions", "list-section-header")], ""),
    ("Action bar", "toolbar", "The footer: a round menu button on the left, and a glass pill on the right naming the primary action and Actions with their key caps.",
     [("height", "component.actionBar.height"), ("pill height", "component.actionBar.pillHeight"), ("pill corner", "component.actionBar.pillRadius"), ("pill fill", "surfaceFill.actionBar")],
     [("root", "action-bar-default")],
     "On macOS 26 the pills are system glass, so their painted fill varies; the declared fill is white at 5%."),
    ("Key cap", "badge", "Shortcut keys drawn as outlined caps beside actions (return, command, K).",
     [("height", "component.kbd.height"), ("border", "component.kbd.border"), ("label", "component.kbd.text")],
     [("in the action panel", "menu-actions")], ""),
    ("Action panel", "menu", "Command-K opens a floating panel of the selected item's actions, with key caps and a search field at the bottom.",
     [("row fill, selected", "component.list.row.selectedBg"), ("separator", "border.separator"), ("shadow", "shadow.panel"), ("type", "typography.text")],
     [("open", "menu-actions"), ("filtered", "menu-actions-typed")],
     "Typing filters the actions in place; the panel shrinks to the matches."),
    ("App menu", "menu", "The round footer button opens Raycast's own menu (feedback, manual, changelog, about, settings) in the same panel shape.",
     [("shadow", "shadow.panel"), ("separator", "border.separator")],
     [("open", "menu-app")], ""),
    ("Badge", "badge", "Pills after a title (Pro) and in the Settings sidebar.",
     [("gray fill", "component.badge.bg"), ("gray text", "component.badge.text"), ("corner", "component.badge.radius"), ("blue fill", "alpha.blue.10"), ("blue text", "theme.blue"),
      ("type", "typography.smallText")],
     [("Pro", "badge-pro")], "The Pro badge is the blue variant: the hue at 10% behind the hue."),
    ("Calculator card", "card", "Typing arithmetic turns the top of the results into a two-cell card: expression, arrow, answer, each with a caption chip.",
     [("fill", "component.list.row.selectedBg")],
     [("12*7+2", "calculator-card")], ""),
    ("Grid", "card", "Emoji & Symbols lays results out as square tiles under section headers, with a category dropdown in the header.",
     [("tile fill", "component.grid.itemBg"), ("selected ring", "component.grid.selectedRing")],
     [("default", "grid-default"), ("filtered", "grid-typed")], "The selected tile gets a 2 pt inner ring rather than a fill change."),
    ("Fallback list", "pattern", "A query with no matches shows 'Use \"query\" with...' and the fallback commands, never an empty pane.",
     [("text", "text.secondary")],
     [("no matches", "list-fallback-empty")], ""),
    ("Settings card", "card", "Settings rows grouped in a faintly lighter rounded card, with hairlines between rows.",
     [("fill", "component.settings.cardBg"), ("row height", "component.settings.rowHeight"), ("separator", "component.settings.separator"), ("padding", "component.settings.padding"),
      ("corner", "radius.10")],
     [("General", "settings-card"), ("pricing", "card-pricing")], ""),
    ("Switch", "checkbox or toggle / switch", "macOS-style switch with a pill thumb.",
     [("width", "component.switch.width"), ("height", "component.switch.height"), ("thumb width", "component.switch.thumbWidth"), ("off", "component.switch.offBg"),
      ("on", "component.switch.onBg"), ("thumb", "component.switch.thumb"), ("motion", "duration.switchThumb")],
     [("on and off", "switch-on-off")], "On is the theme accent; when the window is not key the on track turns grey (fg at 30%)."),
    ("Checkbox", "checkbox or toggle / switch", "14 pt outlined square with a drawn tick; enables commands in an extension's table.",
     [("size", "component.checkbox.size"), ("border", "component.checkbox.border"), ("tick", "component.checkbox.check")],
     [("checked", "checkbox-checked"), ("unchecked", "checkbox-unchecked")], ""),
    ("Dropdown", "select or picker", "A labelled button with a chevron; opens a searchable list grouped by section.",
     [("height", "component.dropdown.height"), ("fill", "component.dropdown.bg"), ("border", "component.dropdown.border"), ("open fill", "component.dropdown.openBg")],
     [("default", "select-default"), ("open", "select-open")], "The open list has its own search field at the top and groups light and dark themes."),
    ("Button", "button", "Pill buttons in Settings (Upgrade to Pro, Check now, Reset).",
     [("height", "component.button.height"), ("fill", "component.button.bg"), ("label", "component.button.text"), ("padding", "component.button.padding"),
      ("ghost hover", "component.button.ghostHoverBg"), ("destructive fill", "component.button.destructiveBg")],
     [("default", "button-default")], "Destructive buttons are red at 20% with red text (declared, not seen)."),
    ("Segmented control", "radio or segmented control", "Interface Size: three Aa options, the chosen one on a filled tile.",
     [("selected fill", "surfaceFill.control")],
     [("Small chosen", "segmented-interface-size")], ""),
    ("Sidebar", "navigation", "Settings navigation: a search field, the account, then General to About, then every extension with its icon.",
     [("fill", "sidebar"), ("selected fill", "surfaceFill.listSelection")],
     [("selected row", "sidebar-row-selected"), ("search empty", "sidebar-search-empty"), ("search focused", "sidebar-search-focused"), ("search typed", "sidebar-search-typed")],
     "Search results highlight the matched words with the text selection colour."),
    ("Text field", "text field", "Bordered fields in forms and Settings (Alias, Export Passphrase).",
     [("height", "component.input.height"), ("fill", "component.input.bg"), ("border", "component.input.border"), ("focus ring", "component.input.focusRing"),
      ("error border", "component.input.errorBorder"), ("padding", "component.input.padding")],
     [("in the commands table", "table-commands")], "The error border and red focus ring are declared; no form was submitted, so no error was seen."),
    ("Table", "table", "An extension's commands: icon and name, Alias, Hotkey, and an enable checkbox per row, with hairlines between rows.",
     [("separator", "border.tertiary"), ("disabled text", "text.tertiary")],
     [("Raycast's commands", "table-commands")], "Disabled commands dim the whole row."),
    ("Avatar", "avatar", "The account's round photo in the sidebar and on the Account page.",
     [("name type", "typography.largeTextStrong")],
     [("Account page", "avatar-account")], ""),
    ("Link", "link", "About's links: an icon, a label and an outward arrow per row.",
     [("label", "text.primary"), ("separator", "border.tertiary")],
     [("About links", "link-list")], ""),
]

GAPS = [
    ("Raycast AI (AI Chat, Quick AI, AI commands)", "Not captured. The owner's account is on the free plan and its AI trial has ended (Settings > AI says 'Upgrade to continue using AI'); `raycast://ai-chat` opened nothing and Ask AI is not in root search. No test prompt was sent."),
    ("Extension Store", "Not captured. The Store command is turned off in the owner's Raycast extension settings and no deeplink opened it; turning it on would change a setting."),
    ("Dialog and destructive confirmation", "Not captured. The only confirmations found (Sign Out, Reset search history, uninstalling) sit behind actions that would change the account or delete data. The dialog's values are declared (component.dialog, scrim)."),
    ("Toast and HUD", "Not captured. Every action that raises one (copy, paste, run a command) is an action the capture did not take. The toast's paddings and glows are declared (component.toast)."),
    ("Form validation error", "Declared (component.input.errorBorder) but not seen: no form was submitted."),
    ("Loading", "Not captured. Results arrived before the first capture after typing; the spinner is declared in the search field (`.search-input__spinner`)."),
    ("Pressed and focus-visible states", "Declared (switch pressed, focus ring 2 pt at fg 30%) but not captured: clicks and keystrokes do not hold them for a still."),
    ("Clipboard History, Snippets, Notes, Calendar", "Left out on purpose: they show private content."),
    ("Onboarding and Theme Studio", "Not captured: onboarding was completed long ago, and Theme Studio needs Pro."),
]


def main():
    out = [f"# {NAME} components", "",
           "Generated by `tools/build_components_md.py` from its inventory, [tokens.json](tokens.json) and [components/crops/](components/crops). "
           "Values are token paths (in the `light` and `dark` sets for colours, `core` for the rest); take them from tokens.json. "
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
            listed = THEMES_OF.get(stem)
            if not listed:
                raise SystemExit(f"{name}: crop {stem} is not in tools/crops.json")
            for suffix, theme in (("", "dark"), ("-light", "light")):
                f = CROPS / f"{stem}{suffix}.png"
                if theme not in listed:
                    continue
                if not f.exists():   # every theme crops.json lists must be on disk, so a lost crop cannot drop a link silently
                    raise SystemExit(f"{name}: no crop {f.name}; run tools/crops.py")
                cells.append(f"[{state} ({theme})](components/crops/{f.name})")
        out += ["Crops: " + ", ".join(cells) + ".", ""]
        if notes:
            out += [notes, ""]
    out += ["## Gaps", "", "| Item | Status |", "|---|---|"] + [f"| {a} | {b} |" for a, b in GAPS] + [""]
    (PKG / "components.md").write_text("\n".join(out))
    print("components.md:", len(INVENTORY), "components")


if __name__ == "__main__":
    main()
