#!/usr/bin/env python3
"""Write components.md from the inventory below, tokens.json and components/crops/ (native kit).

Copied from systems/grokbot. Adapt NAME, INVENTORY and GAPS (PRODUCT (adapt)).

    python3 tools/build_components_md.py

Every value in an entry is a token path; the builder refuses a path tokens.json lacks and a crop
that is not on disk, so the page cannot drift from the package. Standard library only, deterministic.
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

NAME = "Notion"  # PRODUCT (adapt)

# PRODUCT (adapt): (component, checklist item, what it is, [(property, token path)], [(state, crop stem)], notes)
INVENTORY = [
    ("Top tabs", "tabs", "Four tabs across the top beside the account button: Home, Chats, Meetings, Inbox. Unselected tabs are glass circles with an icon; the selected one widens into a pill with its label.",
     [("height", "size.tab"), ("corner", "radius.capsule"), ("unselected fill", "color.surface.tab"), ("selected fill", "color.surface.tabSelected"),
      ("unselected icon", "color.text.iconMuted"), ("selected label", "color.text.primary"), ("label type", "typography.callout"), ("gap", "space.sm")],
     [("Home", "tabs-home"), ("Chats", "tabs-chats"), ("Meetings", "tabs-meetings"), ("Inbox", "tabs-inbox")],
     "This replaces a bottom tab bar: the bottom of the screen holds search, Ask AI and compose instead."),
    ("Bottom bar", "navigation bar", "Floating glass at the bottom of every main screen: a round search button, an 'Ask AI' pill with the AI face, a round compose button. On a page the search button becomes a menu button.",
     [("button", "size.barButton"), ("pill height", "size.barPill"), ("fill", "color.surface.glass"), ("label", "color.text.secondary"), ("glyph", "color.text.iconMuted")],
     [("Home", "bottom-bar"), ("on a page", "bottom-bar-page")],
     "Content scrolls under the glass; no bar background is drawn."),
    ("Icon button", "icon button", "Round glass buttons with a line glyph: history and new chat on the AI chat, search and compose in the bottom bar, close on sheets, back in the Sort sheet.",
     [("size", "size.navButton"), ("bar size", "size.barButton"), ("corner", "radius.capsule"), ("fill", "color.surface.glass"), ("glyph", "color.text.icon")],
     [("AI chat history", "icon-button-glass")], ""),
    ("Link", "link", "Links inside text are underlined and keep the text's own colour (a settings subtitle).",
     [("colour", "color.text.secondary"), ("type", "typography.footnote")],
     [("in a subtitle", "link-underlined")], "No coloured link was seen; blue is kept for controls."),
    ("Unread dot", "badge", "A dot on the account button for unread activity. No count badge was seen.",
     [("fill", "color.status.unread")],
     [("on the account button", "badge-unread-dot")], ""),
    ("Account button", "avatar", "The workspace icon in a glass circle at the top left, with a dot for unread activity. It opens the workspace menu.",
     [("size", "size.avatarButton"), ("fill", "color.surface.glass")],
     [("with dot", "avatar-account")],
     "Inbox rows use people's profile pictures or a letter on a coloured circle; neither was read as a token."),
    ("Sidebar row", "list row", "The Home tree: section headers (Recents, Favourites, Private, Teamspaces) with a chevron, then rows of an emoji or icon and a page title. No dividers, no cards.",
     [("row", "size.row"), ("title", "typography.bodyLarge"), ("title colour", "color.text.primary"), ("header", "typography.subheadline"),
      ("header colour", "color.text.secondary"), ("margin", "space.screenMargin"), ("icon tile", "color.surface.iconTile")],
     [("Home", "list-row-sidebar")], ""),
    ("Chat and meeting rows", "list row", "Chats lists agents, then past chats under a month header, one line each. Meetings lists events with a time, and meeting notes.",
     [("row", "size.row"), ("title", "typography.bodyLarge"), ("header colour", "color.text.secondary"), ("time", "color.text.secondary")],
     [("Chats", "list-row-chats"), ("Meetings", "list-row-meetings")], ""),
    ("Inbox row", "list row", "A notification: avatar, a sentence with the actor and the page in bold, a date at the right, a muted status line, a hairline between items.",
     [("body", "color.text.prose"), ("date", "color.text.tertiary"), ("date type", "typography.subheadline"), ("status", "color.text.secondary")],
     [("Older", "list-row-inbox")], ""),
    ("Search result", "list row", "A page icon, the title, and the page's location under it; matched words in an excerpt are bold. Hairlines between results.",
     [("row", "size.rowSearch"), ("title", "typography.bodyLarge"), ("location", "typography.caption"), ("location colour", "color.text.secondary"), ("canvas", "color.bg.page")],
     [("recents", "list-row-search"), ("typed", "list-row-search-typed")], ""),
    ("Search bar", "text field", "Glass capsule at the bottom with a magnifier, a clear button once typed, a filter button, and a round close button beside it. An 'Ask AI' row sits at the top of the results.",
     [("fill", "color.surface.glass"), ("placeholder", "color.text.placeholder"), ("caret", "color.focus.caret"), ("close", "size.navButton")],
     [("focused", "search-bar-focused"), ("typed", "search-bar-typed"), ("no results", "search-bar-no-results")],
     "Focus shows only the caret."),
    ("Empty state", "pattern", "A page outline icon, a title and a hint, all in secondary grey, centred on the canvas.",
     [("text", "color.text.secondary"), ("type", "typography.subheadline")],
     [("no search results", "empty-state-search")], ""),
    ("Composer", "text area", "The Ask AI field. Focused it is a two-row glass card: text on top, then + (attach), a shield (access), the model name and the mic or a blue send button. Unfocused it collapses to one capsule row.",
     [("focused height", "size.composer"), ("compact height", "size.composerCompact"), ("corner", "radius.composer"), ("fill", "color.surface.composer"),
      ("placeholder", "color.text.placeholder"), ("type", "typography.callout"), ("send", "size.sendButton"), ("send fill", "color.accent.default"), ("caret", "color.focus.caret")],
     [("focused, empty", "composer-focused"), ("typed", "composer-typed"), ("unfocused", "composer-unfocused")],
     "The mic turns into the send arrow once there is text. Nothing was sent."),
    ("Navigation bar", "navigation bar", "No bar: round glass buttons float at the corners. The AI chat centres the AI face over a glass title pill; a page shows back, share and more, and gains a compact title with 'Private' under it once scrolled.",
     [("button", "size.navButton"), ("fill", "color.surface.glass"), ("title", "typography.bodyLarge")],
     [("AI chat", "nav-bar-ai-chat"), ("page, scrolled", "nav-bar-page-compact")], ""),
    ("Primary button", "button", "The blue floating capsule (+ Chat) in the Chats sheet. The only filled button seen.",
     [("height", "size.button"), ("corner", "radius.capsule"), ("fill", "color.button.primary.bg"), ("label", "color.button.primary.text"), ("label type", "typography.button")],
     [("default", "button-primary")], ""),
    ("Secondary button", "button", "Outlined button in Settings (Connect, Manage settings, Change password): no fill, a hairline rim, primary text.",
     [("height", "size.control"), ("corner", "radius.control"), ("rim", "color.button.secondary.border"), ("label", "color.button.secondary.text"), ("type", "typography.subheadline")],
     [("default", "button-secondary")], ""),
    ("Select", "select or picker", "Settings selects look like the outlined button with a chevron (Off, Use system setting). Open, a dark list drops below with a tick on the current value; the Theme select opens a sheet instead.",
     [("height", "size.control"), ("wide height", "size.controlLarge"), ("corner", "radius.control"), ("rim", "color.border.control")],
     [("closed", "select-closed"), ("wide", "select-wide"), ("open", "select-open"), ("sheet", "sheet-theme")],
     "The open list in Settings is drawn by Notion (square, dark, rimmed), not the system menu."),
    ("Switch", "checkbox or toggle / switch", "iOS 26 switch with a pill thumb. Every switch seen was off.",
     [("width", "size.switch.width"), ("height", "size.switch.height"), ("thumb", "size.switch.thumb"), ("off, sheets", "color.switch.off"),
      ("off, Settings", "color.switch.offSettings"), ("thumb colour", "color.switch.thumb")],
     [("off, Filters sheet", "switch-off-sheet"), ("off, Actions sheet", "switch-off-actions"), ("off, Settings", "switch-off-settings")],
     "No switch was on, so the on colour is Not captured."),
    ("Radio list", "radio or segmented control", "The Sort sheet: one choice per row in a system inset list, a blue ring on the chosen row, grey rings on the rest.",
     [("size", "size.radio"), ("on", "color.radio.on"), ("off", "color.radio.off"), ("list fill", "color.surface.list"), ("list corner", "radius.list")],
     [("Best matches chosen", "radio-sort")], ""),
    ("Segmented picker", "radio or segmented control", "Page font: three 'Ag' specimens (Default, Serif, Mono) in a card; the chosen one turns blue.",
     [("selected", "color.text.accent"), ("label", "color.text.secondary"), ("label type", "typography.footnote"), ("card", "color.surface.card")],
     [("Default chosen", "segmented-font")], ""),
    ("Menu", "menu or action sheet", "iOS 26 glass pop-up menus: Inbox filter, the AI model picker (with descriptions), the workspace menu. Items take the system's own ink, not Notion's warm one.",
     [("corner", "radius.menu"), ("fill", "color.surface.menu"), ("item", "color.text.menu"), ("description", "color.text.menuSecondary"), ("item type", "typography.bodyLarge"), ("header type", "typography.caption")],
     [("Inbox filter", "menu-filter"), ("model picker", "menu-model-picker"), ("workspace", "menu-workspace")], ""),
    ("Action sheet", "menu or action sheet", "A page's or a row's Actions open as a large sheet of grouped cards; the destructive row (Move to Bin) is red text with a red icon at the end of its card.",
     [("sheet", "color.bg.sheetGrouped"), ("card", "color.surface.card"), ("corner", "radius.card"), ("row", "size.rowSheet"), ("divider", "color.border.divider"),
      ("icon", "color.text.icon"), ("destructive", "color.text.danger")],
     [("page Actions", "menu-actions-destructive"), ("row long press", "menu-row-actions")], ""),
    ("Sheet", "sheet", "Two kinds: small sheets in the page colour over a dimmed screen (Filters, Sort) and large sheets in the sidebar colour holding grouped cards (Actions, Views, Theme, filter properties). Both have a grabber; Done is blue text.",
     [("small", "color.bg.sheet"), ("large", "color.bg.sheetGrouped"), ("corner", "radius.sheet"), ("scrim", "color.bg.scrim"), ("grabber", "color.surface.grabber"), ("Done", "color.text.accent")],
     [("Filters", "sheet-filters"), ("Chats", "sheet-chats"), ("Views", "sheet-views"), ("filter properties", "sheet-filter-properties"), ("Theme", "sheet-theme")], ""),
    ("Message bubble", "card", "In an AI chat only the owner's messages are bubbles: a quiet grey, right-aligned. The AI answers in plain text on the canvas, with an outlined card listing the pages it changed and copy, thumbs and retry icons under it.",
     [("fill", "color.surface.bubble"), ("corner", "radius.bubble"), ("text", "color.text.prose"), ("type", "typography.bodyLarge"),
      ("result card rim", "color.border.card"), ("result card corner", "radius.card"), ("inline code", "color.surface.code"), ("code text", "color.text.code")],
     [("own", "bubble-own"), ("AI answer", "ai-answer")], ""),
    ("Page content", "pattern", "A page: title, headings and body on the canvas at a wider margin than the sidebar, inline code in red, tables with a tinted header row and hairline cells.",
     [("title", "typography.pageTitle"), ("heading 1", "typography.heading1"), ("heading 2", "typography.heading2"), ("body", "typography.body"),
      ("margin", "space.page"), ("table rim", "color.border.table"), ("table header", "color.surface.tableHeader"), ("table text", "typography.caption")],
     [("headings", "page-headings"), ("table", "page-table")], ""),
    ("Database view", "table", "An inline database in a rimmed frame: a view chip, search, filter (blue while a filter is on), properties and a blue + split button, then rows grouped by colour.",
     [("frame rim", "color.border.frame"), ("frame corner", "radius.frame"), ("chip", "size.chip"), ("chip fill", "color.surface.chip"), ("+ button", "size.splitButton"),
      ("+ fill", "color.accent.default"), ("row", "size.rowDatabase"), ("blue group", "color.group.blue"), ("green group", "color.group.green"), ("pink group", "color.group.pink"), ("orange group", "color.group.orange")],
     [("groups", "database-groups"), ("toolbar", "database-toolbar")], ""),
    ("Settings row", "list row", "Settings is one long scroll: a bold section title, then rows of a title, a two-line grey subtitle and a control at the right, separated by inset hairlines.",
     [("section title", "typography.title"), ("row title", "typography.subheadline"), ("subtitle", "typography.footnote"), ("subtitle colour", "color.text.secondary"), ("separator", "color.border.separator"), ("canvas", "color.bg.sidebar")],
     [("Notifications", "settings-rows")], ""),
]

# PRODUCT (adapt)
GAPS = [
    ("Loading", "Not captured: every screen loaded before a capture could run."),
    ("Dialog or alert", "Not captured: only Move to Bin leads to one, and it was not tapped."),
    ("Board, calendar and gallery views", "Not captured: the database has only one (list) view."),
    ("Switch on", "Not captured: every switch was off and none was changed."),
    ("Text field (single line, labelled)", "Not captured outside search and the composer."),
    ("Checkbox, tooltip, toast", "Not seen in any capture."),
    ("Pressed states and motion", "Not captured: stills made with clicks."),
    ("Keyboard", "iPhone Mirroring types from the Mac keyboard, so the software keyboard never shows."),
    ("Light theme", "17 of the 29 screens; the Sort list, radios, menus over content, Views and the row Actions sheet are dark only."),
    ("Success and warning colours", "No such state appeared."),
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
