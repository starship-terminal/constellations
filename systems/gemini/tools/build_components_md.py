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

NAME = "Gemini"  # PRODUCT (adapt)

# PRODUCT (adapt): (component, checklist item, what it is, [(property, token path)], [(state, crop stem)], notes)
INVENTORY = [
    ("Primary button", "button", "Full-width near-black capsule over the glow at the bottom of a screen or sheet (Get started, Try it).",
     [("height", "size.button"), ("corner", "radius.capsule"), ("fill", "color.button.primary.bg"), ("label", "color.button.primary.text"), ("label type", "typography.body")],
     [("onboarding", "button-primary-default"), ("in a glass sheet", "button-primary-sheet")],
     "Captured in dark only (onboarding and the Create images sheet); the light tokens are Derived. The label is regular weight, not bold."),
    ("Filled tonal button", "button", "Capsule with a leading + icon (Add, on Memory), in Google's Material primary.",
     [("height", "size.buttonTonal"), ("corner", "radius.capsule"), ("fill", "color.button.tonal.bg"), ("label", "color.button.tonal.text"), ("label type", "typography.body")],
     [("default", "button-tonal-add")],
     "Light blue with a navy label in dark, deep blue with a white label in light: the Material 3 primary pair."),
    ("Text button", "button", "Blue text with no container in a sheet header (Done).",
     [("colour", "color.text.action"), ("type", "typography.body")],
     [("default", "text-button-done")], ""),
    ("Google sign-in button", "button", "Light-blue rounded rectangle inside the Google account sheet at onboarding (Continue as ...).",
     [("height", "size.buttonSignIn"), ("fill", "color.button.signIn.bg"), ("label", "color.button.signIn.text"), ("sheet", "color.surface.signIn")],
     [("onboarding", "button-sign-in")],
     "Google's account sign-in surface, styled unlike the rest of the app (a rectangle, not a capsule). Dark only."),
    ("Icon button", "icon button", "Round glass buttons: menu, new chat, close, back, share, filter. The account avatar sits in the same 44 pt circle.",
     [("size", "size.navButton"), ("fill", "color.surface.glass"), ("glyph", "color.text.onGlass")],
     [("menu", "icon-button-glass")],
     "iOS 26 glass; the fill token is its centre reading. Pairs of actions share one glass capsule (share and compass on Memory, new chat and more in a thread)."),
    ("Send and voice buttons", "icon button", "Circles at the right end of the composer: a blue-tinted voice (Live) button while empty, a blue send arrow once text is typed.",
     [("size", "size.sendButton"), ("send fill", "color.button.send.bg"), ("send glyph", "color.button.send.glyph"), ("voice fill", "color.button.voice.bg"), ("voice, Task mode", "color.button.voice.bgTask"), ("voice glyph", "color.button.voice.glyph")],
     [("send", "button-send"), ("voice", "button-voice")],
     "The voice button takes the mode's colour: blue in Chat, purple in Task."),
    ("Link", "link", "Inline bright-blue text at the end of a paragraph (Learn more); elsewhere links are primary text with a dotted underline (Memory, Scheduled, onboarding).",
     [("colour", "color.text.link"), ("type", "typography.subheadline")],
     [("in a paragraph", "link-inline")], ""),
    ("Composer", "text field", "A floating glass capsule over the glow: +, the placeholder, a microphone, then the voice or send circle. It widens to the screen margins once text is typed.",
     [("height", "size.composer.height"), ("width, empty", "size.composer.width"), ("width, typed", "size.composer.widthTyped"), ("corner", "radius.capsule"), ("fill", "color.surface.composer"),
      ("placeholder", "color.text.placeholder"), ("text type", "typography.body"), ("caret", "color.focus.caret")],
     [("empty", "composer-default"), ("typed", "composer-typed"), ("Task mode", "composer-task")],
     "The placeholder names the mode ('Ask Gemini', 'Describe task'). The software keyboard never shows in these captures."),
    ("Search field", "text field", "Glass capsule at the bottom of the chat search, with a separate round close button; typed text adds a clear button.",
     [("fill", "color.surface.glass"), ("placeholder", "color.text.placeholderSearch"), ("caret", "color.focus.caret")],
     [("focused", "search-field-focused"), ("typed", "search-field-typed")], ""),
    ("Segmented toggle", "radio or segmented control", "Chat / Task above the composer: the selected label sits in a pill, the other is bare text.",
     [("pill width", "size.segment.width"), ("pill height", "size.segment.height"), ("pill fill", "color.surface.segment"), ("label", "color.text.onGlass"), ("type", "typography.caption")],
     [("Chat selected", "segmented-chat-selected"), ("Task selected", "segmented-task-selected")],
     "Choosing Task turns the glow and the voice button purple and swaps the greeting and suggestions."),
    ("Pop-up select", "select or picker", "A settings row value with up-down chevrons opens a glass menu with a tick on the current choice and an icon per option (Theme).",
     [("menu fill", "color.surface.menuPopup"), ("corner", "radius.menu"), ("item type", "typography.callout"), ("value", "color.text.secondary")],
     [("open", "select-theme-open")], ""),
    ("Switch", "checkbox or toggle / switch", "Two styles: a Material switch with a tick on its thumb (Memory) and the iOS switch (Voice settings).",
     [("Material width", "size.switch.width"), ("Material height", "size.switch.height"), ("Material on", "color.switch.on"), ("Material thumb", "color.switch.thumb"), ("tick", "color.switch.tick"),
      ("iOS width", "size.switchSystem.width"), ("iOS height", "size.switchSystem.height"), ("iOS on", "color.switch.onSystem"), ("iOS thumb", "color.switch.thumbSystem")],
     [("Material, on", "switch-material-on"), ("iOS, on", "switch-system-on")],
     "Both were captured on only. No off switch appeared."),
    ("Navigation bar", "navigation bar", "No bar: glass circles float at the corners over the content, with the title as plain text (Gemini and the model name on home, a centred title in sheets).",
     [("button", "size.navButton"), ("fill", "color.surface.glass"), ("title type", "typography.title"), ("model name", "color.text.secondary"), ("new-model dot", "color.accent.dot")],
     [("home", "nav-bar-home"), ("sheet page", "nav-bar-sheet"), ("Scheduled", "nav-bar-scheduled")],
     "On home the title is a button: 'Gemini' then the model in secondary text and a chevron opens the model picker."),
    ("Menu", "menu or action sheet", "iOS 26 glass pull-down menus: the model picker (two-line items, a tick, a divider, a submenu row) and the chat menu with a red Delete last.",
     [("width", "size.menuWidth"), ("row", "size.menuRow"), ("corner", "radius.menu"), ("fill", "color.surface.menu"), ("item", "color.text.onGlass"), ("item type", "typography.callout"),
      ("description", "color.text.onMenuSecondary"), ("description type", "typography.caption2"), ("destructive", "color.text.danger")],
     [("model picker", "menu-model-picker"), ("chat, with Delete", "menu-chat-destructive")], ""),
    ("Sheet", "sheet", "Settings and Usage open as full-height sheets with a grabber and a round close button; the + sheet and the Create images intro are glass sheets over the page; the account sheet is tinted grey with a Done button.",
     [("fill", "color.bg.sheet"), ("account sheet", "color.bg.sheetAccount"), ("+ sheet", "color.surface.sheetPlus"), ("corner", "radius.sheet"), ("grabber", "size.grabber.width"), ("behind", "color.bg.scrim"), ("large title", "typography.titleLarge")],
     [("Settings header", "sheet-settings-header"), ("+ sheet", "sheet-plus"), ("Create images intro", "sheet-images-intro"), ("account", "sheet-account")],
     "The + sheet holds three large tiles (Photos, Camera, Avatar) above a list of tools, each with an icon, a title and a description."),
    ("Dialog", "dialog or alert", "The iOS permission alert (notifications), drawn by the system.",
     [("message", "color.text.secondary")],
     [("open", "dialog-permission")],
     "System UI, not Gemini's; it shows how the app looks behind an alert. Its values are in raw/readings.json (surface.alert, radius.alert) and are not tokenised."),
    ("Grouped card", "card", "Rows grouped in a rounded card with hairline dividers inset to the row text, under a section header. Each row has a line icon, a title, and a chevron, a value or a switch.",
     [("fill", "color.surface.card"), ("corner", "radius.card"), ("divider", "color.border.divider"), ("row", "size.row"), ("two-line row", "size.rowTwoLine"), ("header", "color.text.tertiary"), ("subtitle", "color.text.secondary")],
     [("Voice", "card-grouped"), ("Account section", "card-grouped-section")],
     "Cards have no rim; in light they are white on the warm off-white sheet."),
    ("Suggestion card", "card", "A title and a two-line description in a rounded card, stacked 12 pt apart (Scheduled); the study-notebook card adds a text button at the bottom right.",
     [("fill", "color.surface.raised"), ("corner", "radius.cardSuggestion"), ("height", "size.suggestionCard"), ("padding", "space.xl"), ("title type", "typography.body"), ("description", "color.text.secondary")],
     [("Scheduled", "card-suggestion"), ("empty notebook", "card-notebook-empty")], ""),
    ("Feature and template cards", "card", "Image cards in a horizontal scroller with a caption under them (Students) or a label over the image (image templates).",
     [("caption type", "typography.body"), ("caption", "color.text.primary")],
     [("Students", "card-feature"), ("image templates", "card-template")],
     "The images are Google's published artwork and sample photos; borrow the layout, not the pictures."),
    ("Usage card", "card", "Two stacked container cards with a title, a value at the right, a progress track and a reset line.",
     [("fill", "color.surface.container"), ("track", "color.surface.track"), ("title type", "typography.subheadline"), ("helper", "color.text.tertiary")],
     [("0% and 9% used", "card-usage-progress")], "Only the empty (0%) track was seen, so no fill colour is known."),
    ("Message bubble", "card", "The owner's messages sit in a container-coloured bubble at the right; Gemini's replies are plain text on the page with an action row (share, like, dislike, more) under them.",
     [("fill", "color.surface.container"), ("text", "color.text.primary"), ("corner", "radius.bubble"), ("padding", "space.xxl"), ("text type", "typography.body"), ("disclaimer", "typography.footnote")],
     [("own", "bubble-own"), ("reply and actions", "reply-actions")], ""),
    ("Media card", "card", "A generated video inline in the thread, with large rounded corners, a play button and a share button over it.",
     [("width", "size.mediaCard")],
     [("video", "media-card-video")], ""),
    ("List row", "list row", "Sidebar rows (icon, label; the current one in a capsule), notebook rows, the account row, and search results (bubble icon, title, age).",
     [("sidebar row", "size.sidebarRow"), ("selected", "color.surface.selected"), ("search row", "size.searchRow"), ("type", "typography.body"), ("age", "color.text.tertiary"), ("section header", "color.text.tertiary")],
     [("sidebar", "list-row-sidebar"), ("notebooks", "list-row-notebooks"), ("account", "list-row-account"), ("search", "list-row-search")], ""),
    ("Avatar", "avatar", "The account photo in a circle with a blue ring (sidebar, account sheet), plain in the nav bar.",
     [("ring", "color.accent.ring"), ("nav size", "size.navButton")],
     [("account sheet, with edit", "avatar-ring")], ""),
    ("Badge", "badge", "PRO as grey text on a container chip beside the Usage limits title; Pro as a glassy blue chip under the account name.",
     [("fill", "color.surface.container"), ("label", "color.text.badge"), ("type", "typography.subheadline")],
     [("PRO", "badge-pro"), ("Pro on the account", "badge-pro-account")], ""),
    ("Empty state", "pattern", "A centred magnifier, a medium title and a secondary line (search); one centred secondary line (Memory).",
     [("title", "typography.bodyStrong"), ("line", "typography.subheadline"), ("line colour", "color.text.secondary")],
     [("no search results", "empty-state-search"), ("Memory", "empty-state-memory")], ""),
]

# PRODUCT (adapt)
GAPS = [
    ("Tab bar", "Not present. Navigation is a sidebar opened from the menu button."),
    ("Loading and streaming", "Not captured: it needs a prompt sent, and the capture sent none."),
    ("Live (voice) mode", "Not captured: it asks for the microphone."),
    ("Off and disabled states", "No switch was off and no control was disabled in any capture."),
    ("Pressed states and motion", "Not captured: stills made with clicks."),
    ("Toast or snackbar", "None appeared."),
    ("Error state and destructive confirmation", "Delete was not tapped, and no error appeared."),
    ("Keyboard", "iPhone Mirroring types from the Mac keyboard, so the software keyboard never shows."),
    ("Light onboarding", "Onboarding (sign-in, terms, the permission alert), the Create images intro and the sidebar's New chat row were captured in dark only."),
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
