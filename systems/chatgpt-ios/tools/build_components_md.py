#!/usr/bin/env python3
"""Write components.md from the inventory below, tokens.json and components/crops/ (native kit).

Copied from the native kit (systems/grokbot). NAME, INVENTORY and GAPS are ChatGPT for iOS's
(PRODUCT (adapt)); a state captured in one theme only links that theme's crop.

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

NAME = "ChatGPT for iOS"  # PRODUCT (adapt)

# PRODUCT (adapt): (component, checklist item, what it is, [(property, token path)], [(state, crop stem)], notes)
INVENTORY = [
    ("Accent pill button", "button", "The primary action as a filled capsule in the accent: Chat (new chat) at the bottom of the sidebar, New task on Scheduled.",
     [("height", "size.pill"), ("corner", "radius.capsule"), ("fill", "color.accent.pill"), ("label", "color.text.onAccent"), ("label type", "typography.body")],
     [("Chat, sidebar", "button-chat-pill"), ("New task", "button-new-task")],
     "Both float over the page at the bottom of the screen. The label is white in both themes."),
    ("Ink pill button", "button", "A smaller capsule in the theme's ink, used inside an empty state (New chat).",
     [("height", "size.inkButton"), ("corner", "radius.capsule"), ("fill", "color.button.ink.bg"), ("label", "color.button.ink.text"), ("label type", "typography.body")],
     [("default", "button-new-chat")],
     "White with a black label in dark, near-black with a white label in light."),
    ("Icon button", "icon button", "Round glass buttons: sidebar, close, back and new chat at the top; the send and voice circles in the composer are accent-filled.",
     [("size", "size.navButton"), ("fill", "color.surface.glass"), ("glyph", "color.text.primary"), ("send size", "size.sendButton"), ("send fill", "color.accent.default"),
      ("send glyph", "color.text.onAccent"), ("unread dot", "color.accent.unread")],
     [("sidebar, with unread dot", "icon-button-sidebar-unread"), ("close", "icon-button-close"), ("back", "icon-button-back")],
     "The sidebar button carries a blue dot while a chat is unread."),
    ("Segmented control", "radio or segmented control", "Chat / Work at the top of a new chat: a glass capsule with a thumb behind the selected half.",
     [("width", "size.segmented.width"), ("height", "size.segmented.height"), ("thumb", "size.segmented.thumb"), ("track", "color.surface.segmentTrack"),
      ("thumb fill", "color.surface.segmentThumb"), ("label type", "typography.callout")],
     [("Chat selected", "segmented-chat"), ("Work selected", "segmented-work")],
     "In dark the thumb is darker than the track; in light it is a grey on a white track."),
    ("Tabs", "tabs", "Filter tabs as text with a glass pill behind the selected one (Scheduled: Active, Paused, Completed; search: All, Chats, Pages, Image).",
     [("height", "size.tab"), ("selected fill", "color.surface.tabSelected"), ("unselected label", "color.text.muted"), ("selected label", "color.text.primary"), ("type", "typography.body")],
     [("Active", "tabs-scheduled-active"), ("Paused", "tabs-scheduled-paused"), ("search filter", "tabs-search-filter")], ""),
    ("Navigation bar", "navigation bar", "A centred title with a round glass back or sidebar button; no bar background.",
     [("button", "size.navButton"), ("title type", "typography.headline"), ("title", "color.text.primary")],
     [("General", "nav-bar-title")], "Content scrolls under the glass button."),
    ("Composer", "text field", "The chat input: a two-row glass card. The field on top; + on the left of the tool row, then the model pill (Work) or speed icon (Chat), microphone and the send or voice circle.",
     [("width", "size.composer.width"), ("height", "size.composer.height"), ("corner", "radius.composer"), ("fill", "color.surface.composer"),
      ("placeholder", "color.text.placeholder"), ("type", "typography.body"), ("caret", "color.focus.caret"), ("send", "color.accent.default")],
     [("empty, Chat", "composer-empty"), ("focused, Work", "composer-focused-work"), ("typed", "composer-typed"), ("model pill", "composer-model-pill")],
     "With text the voice circle becomes a send arrow. The placeholder names the mode ('Ask ChatGPT', 'Work with ChatGPT')."),
    ("Text field", "text field", "Custom instructions in Personalization: a grouped card holding only a placeholder.",
     [("fill", "color.surface.card"), ("corner", "radius.card"), ("placeholder", "color.text.placeholder"), ("header", "color.text.sectionHeader")],
     [("empty", "text-field-empty")], "Not typed into, because the field may save as it is edited."),
    ("Search field", "text field", "Glass capsule at the bottom of search with a magnifier, a clear button and a round close button beside it.",
     [("height", "size.searchBar"), ("fill", "color.surface.searchField"), ("placeholder", "color.text.placeholder"), ("caret", "color.focus.caret")],
     [("empty", "search-field-empty"), ("typed", "search-field-typed")], ""),
    ("Find in chat", "text field", "A glass search bar replaces the top controls, with a result count and up, down and close buttons.",
     [("fill", "color.surface.glass"), ("count", "color.text.muted")],
     [("no results", "find-in-chat-no-results")], ""),
    ("Pop-up select", "select or picker", "A row value with up-down chevrons opens a glass menu with a tick on the current choice (Appearance, Accent color, Start screen, Model).",
     [("value", "color.text.secondary"), ("chevrons", "color.text.chevron"), ("menu fill", "color.surface.menu"), ("item type", "typography.body")],
     [("closed values", "select-row-values"), ("Accent color open", "select-accent-open")],
     "The Accent color menu lists the nine `color.accent.*` swatches and `color.accent.inkOption`."),
    ("Switch", "checkbox or toggle / switch", "iOS 26 switch with a pill thumb, iOS system green when on.",
     [("width", "size.switch.width"), ("height", "size.switch.height"), ("thumb", "size.switch.thumb"), ("on", "color.switch.on"), ("thumb fill", "color.switch.thumb")],
     [("on", "switch-on")], "Every switch captured was on; the off track is not captured."),
    ("Slider", "slider", "The effort slider: a glass capsule with six steps, an accent fill up to a white thumb, grey dots beyond.",
     [("height", "size.slider.height"), ("thumb", "size.slider.thumb"), ("fill", "color.accent.default"), ("track", "color.surface.sliderTrack"),
      ("thumb fill", "color.slider.thumb"), ("step", "color.slider.step")],
     [("Medium", "slider-effort")], "The model and effort name sit above it ('6.1 Sol Medium')."),
    ("Progress bar", "progress", "The usage meter: a thin capsule in a card, the fill a lighter blue than the accent, the track the same blue faded.",
     [("height", "size.progress"), ("fill", "color.accent.meter"), ("track", "color.surface.progressTrack"), ("card", "color.surface.card")],
     [("67% remaining", "progress-usage")], ""),
    ("Menu", "menu or action sheet", "iOS 26 glass menus. The plus menu has large items with round icon wells and a tick on the selected tool; the chat menu has a header, chevrons for submenus and a red Delete.",
     [("plus width", "size.menuWidth"), ("plus corner", "radius.menuLarge"), ("chat corner", "radius.menu"), ("fill", "color.surface.menu"), ("icon well", "size.menuIcon"),
      ("icon well fill", "color.surface.menuIcon"), ("plus item type", "typography.menuLarge"), ("item type", "typography.body"), ("selected", "color.text.accent"),
      ("destructive", "color.text.danger"), ("header", "color.text.menuHeader")],
     [("plus, Think harder selected", "menu-plus-selected"), ("chat, with Delete", "menu-chat-destructive")],
     "The glass takes the colour of what is behind it: the chat menu turns blue over the owner's bubble (`color.surface.menuTinted`)."),
    ("Dialog", "dialog or alert", "An alert card in glass over a scrim, a title, grey body and two equal capsule buttons.",
     [("width", "size.dialog.width"), ("corner", "radius.dialog"), ("fill", "color.surface.dialog"), ("button fill", "color.surface.dialogButton"),
      ("button height", "size.dialog.button"), ("button label", "color.button.dialog.text"), ("title type", "typography.headline"), ("body", "color.text.dialogBody"),
      ("body type", "typography.subheadline"), ("scrim", "color.bg.scrim")],
     [("error, Cancel and Retry", "dialog-error")],
     "It appeared on its own when a photo failed to load. Neither button is tinted; Retry is not drawn as the primary."),
    ("Banner", "toast or banner", "A white glass card that slid over the top of a thread: a bold title, one line of body and a chevron (Share Message).",
     [("fill", "color.surface.banner"), ("title", "color.text.bannerTitle"), ("body", "color.text.bannerBody")],
     [("Share Message", "banner-share-message")], "Seen in light only (06 and 08); its dark tokens are Derived."),
    ("Grouped card", "card", "Settings rows grouped in a card with an icon, a label, a value or chevron, and hairline dividers inset to the label.",
     [("fill", "color.surface.card"), ("corner", "radius.card"), ("divider", "color.border.divider"), ("row", "size.row"), ("header", "color.text.sectionHeader"),
      ("helper text", "color.text.footnote"), ("page", "color.bg.grouped")],
     [("Customize ChatGPT", "card-grouped")], ""),
    ("Task card", "card", "A recommended Scheduled task: emoji, title, three lines of description, inside a dashed rim.",
     [("fill", "color.surface.taskCard"), ("rim", "color.border.dashed"), ("rim width", "border.width.dashed"), ("title type", "typography.body"),
      ("description", "color.text.muted"), ("description type", "typography.footnote")],
     [("recommended", "card-task")], "In light the card is white on a near-white page, so the dashed rim is all that separates it."),
    ("Message bubble", "card", "Only the owner's messages are in a bubble: right-aligned, tinted by the accent. Replies sit on the page as plain text with maths, bold runs and an action row (copy, share, more).",
     [("fill", "color.surface.userBubble"), ("text", "color.text.onUserBubble"), ("corner", "radius.bubble"), ("max width", "size.bubbleMaxWidth"), ("bubble type", "typography.bubble"),
      ("reply text", "color.text.reply"), ("reply type", "typography.body"), ("bold", "typography.headline"), ("maths", "fontFamily.math")],
     [("owner's bubble", "bubble-user"), ("reply with maths and actions", "reply-math-actions")], ""),
    ("List row", "list row", "Grouped settings rows with values, sidebar nav items with outline icons, recent chats with an unread dot, suggestion rows above the composer.",
     [("row", "size.row"), ("label", "color.text.primary"), ("value", "color.text.secondary"), ("suggestion", "color.text.suggestion"), ("see all", "color.text.muted"),
      ("unread dot", "color.accent.unread"), ("rule", "color.border.sidebar"), ("type", "typography.body"), ("sidebar title", "typography.titleLarge")],
     [("settings values", "list-row-values"), ("sidebar nav", "sidebar-nav"), ("recents, unread", "sidebar-recents-unread"), ("sidebar expanded", "sidebar-expanded"), ("suggestions", "suggestions")],
     "Sidebar and suggestion rows have no dividers; they sit 48 pt and 47 pt apart."),
    ("Badge", "badge", "A system-blue unread dot after a recent chat and on the sidebar button.",
     [("dot", "color.accent.unread")],
     [("on the sidebar button", "icon-button-sidebar-unread"), ("in recents", "sidebar-recents-unread")], ""),
    ("Empty state", "pattern", "Centred: a magnifier on a grey tile, a title, muted body, and an ink pill (no results); or a magnifier and one line (search prompt); or one muted line (no paused tasks).",
     [("tile", "color.surface.searchTile"), ("tile size", "size.searchTile"), ("title", "color.text.primary"), ("body", "color.text.muted"), ("body type", "typography.callout")],
     [("no results", "empty-state-search"), ("search prompt", "empty-state-search-prompt"), ("no paused tasks", "empty-state-paused")], ""),
]

# PRODUCT (adapt)
GAPS = [
    ("Tab bar", "Not present. Navigation is the sidebar, opened from the round button at the top left."),
    ("Loading state", "Not captured. Both 18 captures were planned as loading skeletons, but the skeletons had resolved: dark/18 matches 19 (no results) and light/18 matches 21 (Scheduled) except for the clock and caret."),
    ("Switch off", "Not captured: every switch on the captured pages was on, and none was changed."),
    ("Message long-press menu", "Not captured: a long press on a bubble opened nothing through iPhone Mirroring."),
    ("Voice mode", "Not captured: it would raise a microphone permission prompt."),
    ("Toast", "No toast seen; the only transient surface is the light Share Message banner."),
    ("Pressed states and motion", "Not captured: stills made with clicks."),
    ("Keyboard", "iPhone Mirroring types from the Mac keyboard, so the software keyboard never shows."),
    ("Other accents", "Only Blue was applied; the other nine options were seen only as swatches."),
    ("Warning and success colours", "No such state appeared."),
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
            found = [(theme, CROPS / f"{stem}{suffix}.png") for suffix, theme in (("", "dark"), ("-light", "light"))]
            found = [(theme, f) for theme, f in found if f.exists()]
            if not found:   # a state seen in one theme has only that theme's crop
                raise SystemExit(f"{name}: no crop {stem}.png or {stem}-light.png")
            cells += [f"[{state} ({theme})](components/crops/{f.name})" for theme, f in found]
        out += ["Crops: " + ", ".join(cells) + ".", ""]
        if notes:
            out += [notes, ""]
    out += ["## Gaps", "", "| Item | Status |", "|---|---|"] + [f"| {a} | {b} |" for a, b in GAPS] + [""]
    (PKG / "components.md").write_text("\n".join(out))
    print("components.md:", len(INVENTORY), "components")


if __name__ == "__main__":
    main()
