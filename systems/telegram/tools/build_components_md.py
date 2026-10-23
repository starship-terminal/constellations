#!/usr/bin/env python3
"""Write components.md from the inventory below, tokens.json and components/crops/ (native kit).

Copied from the native kit (tools/kit/native, from systems/grokbot); NAME, INVENTORY and GAPS are Telegram's.

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

NAME = "Telegram"

# (component, checklist item, what it is, [(property, token path)], [(state, crop stem)], notes)
INVENTORY = [
    ("Accent button", "button", "Full-width capsule in the page's flow (Add Device), the only filled button in the captures.",
     [("height", "size.button"), ("corner", "radius.capsule"), ("fill", "color.accent.default"), ("label", "color.text.onAccent"), ("label type", "typography.navTitle")],
     [("default", "button-primary-default")],
     "The fill is the accent itself, a lighter blue in dark. No disabled or pressed state was captured."),
    ("Accent pill", "button", "Small capsule at the end of a row (ADD on a recommended folder).",
     [("height", "size.pill"), ("corner", "radius.capsule"), ("fill", "color.accent.pill"), ("label", "color.text.onAccent")],
     [("default", "button-pill-add")], "Upper-case label."),
    ("Text action row", "link", "An action written as accent text in a card row, often with an accent glyph (Change Profile Photo, Create a Folder, Start New Call, Invite Friends).",
     [("colour", "color.text.link"), ("type", "typography.body"), ("row", "size.row")],
     [("default", "list-row-accent")], "Telegram's secondary buttons are rows like this, not outlined buttons."),
    ("Glass nav button", "icon button", "Round glass buttons in the nav bar (back, compose, search, add) and glass capsules for text (Edit, Sort, Done).",
     [("size", "size.navButton"), ("fill", "color.surface.glass"), ("compose fill", "color.accent.compose"), ("glyph", "color.text.primary")],
     [("back", "icon-button-back"), ("compose", "button-compose")],
     "Compose is the one accent-tinted glass button."),
    ("Navigation bar", "navigation bar", "No bar: glass buttons float at each side and the title sits between them, over the content.",
     [("title", "color.text.primary"), ("title type", "typography.navTitle"), ("button", "size.navButton")],
     [("settings page", "nav-bar-settings"), ("chat list", "nav-bar-chats")],
     "The chat list title carries the account avatar and a lock (passcode on)."),
    ("Search field", "text field", "Capsule field with a centred magnifier and placeholder; typed, it gains a clear button and a round close button beside it.",
     [("height", "size.search"), ("corner", "radius.capsule"), ("fill", "color.surface.search"), ("placeholder", "color.text.placeholder"), ("caret", "color.focus.caret")],
     [("default", "search-field"), ("typed, global", "search-field-typed"), ("in a chat, focused", "search-chat-focused"), ("in a chat, typed", "search-chat-typed")],
     "Focus moves the placeholder to the left and shows the caret; there is no ring."),
    ("Composer", "text field", "Attach button, a glass capsule field with an emoji or sticker button, and a microphone that becomes a send pill once there is text.",
     [("send", "size.send.width"), ("send fill", "color.accent.send"), ("field", "color.surface.composer"), ("caret", "color.focus.caret"), ("type", "typography.body")],
     [("default", "composer-default"), ("typed", "composer-typed")],
     "The field is glass over the wallpaper, so its colour follows the wallpaper."),
    ("Switch", "checkbox or toggle / switch", "iOS 26 switch with a pill thumb.",
     [("width", "size.switch.width"), ("height", "size.switch.height"), ("thumb", "size.switch.thumb"), ("on", "color.switch.on"), ("off", "color.switch.off"),
      ("disabled", "color.switch.offDisabled"), ("disabled label", "color.text.disabled")],
     [("on and off", "switch-on-off"), ("disabled", "switch-disabled")],
     "Disabled dims the track, the thumb and the row label together."),
    ("Choice list", "radio or segmented control", "A card of rows where one carries an accent checkmark at its end (dark) or start (light's Auto-Night list).",
     [("check", "color.accent.check"), ("row", "size.row"), ("card", "color.surface.card")],
     [("one chosen", "checklist")], "The accent action row closes the list (Set Custom Time...)."),
    ("Segmented control", "radio or segmented control", "Glass capsule with two segments in the nav bar (Calls: All / Missed).",
     [("width", "size.segmented.width"), ("height", "size.segmented.height"), ("track", "color.surface.segmented"), ("selected", "color.surface.segmentedSelected"), ("label type", "typography.subheadline")],
     [("All", "segmented-all"), ("Missed", "segmented-missed")], ""),
    ("Folder chips", "tabs", "A glass bar of folder chips above the chat list; the selected chip is a lighter pill, counts sit in a muted badge, and edit mode adds a remove cross to each.",
     [("bar height", "size.chipBar"), ("chip height", "size.chip"), ("bar", "color.surface.chipBar"), ("selected", "color.surface.chipSelected"), ("count", "color.badge.muted"), ("type", "typography.subheadline")],
     [("All selected", "chip-bar-folders"), ("os selected", "chip-bar-selected-os"), ("edit mode", "chip-bar-edit-mode")], ""),
    ("Tab bar", "tabs", "Floating glass capsule with four tabs (Contacts, Calls, Chats, Settings); the selected tab sits in a pill and turns accent.",
     [("height", "size.tabBar.height"), ("width", "size.tabBar.width"), ("fill", "color.surface.tabBar"), ("selected pill", "color.surface.tabSelected"),
      ("label", "color.text.tab"), ("selected label", "color.text.tabSelected"), ("type", "typography.caption")],
     [("Chats selected", "tab-bar")], "Content scrolls under it."),
    ("Menu", "menu or action sheet", "iOS 26 glass menus: a context menu under a long-pressed message (with a reaction bar above it), the chat's pull-down, the Sort menu, and a chat preview's menu.",
     [("corner", "radius.menu"), ("fill", "color.surface.menu"), ("over a plain list", "color.surface.menuPlain"), ("reactions", "color.surface.reactions"),
      ("item type", "typography.body"), ("destructive", "color.text.dangerMenu")],
     [("message", "menu-context"), ("reactions", "reactions-bar"), ("chat more", "menu-chat-more"), ("sort", "menu-sort"), ("chat preview", "menu-chat-preview")],
     "A long press blurs everything behind; the item that matches the current choice has a tick."),
    ("Sheet", "sheet", "New Message and the attachment picker rise as sheets with a round close button at the top left.",
     [("fill", "color.bg.sheet"), ("corner", "radius.sheet")],
     [("New Message", "sheet-new-message"), ("attachment", "sheet-attachment")],
     "The attachment sheet ends in its own glass tab bar (Gallery, File, Location, Poll, Checklist). One thumbnail's hostname is masked."),
    ("Grouped card", "card", "Rows grouped in a rounded card with hairline dividers inset to the text; settings rows lead with a coloured icon tile.",
     [("fill", "color.surface.card"), ("corner", "radius.card"), ("divider", "color.border.divider"), ("row", "size.row"), ("two-line row", "size.rowTwoLine"),
      ("icon tile", "size.iconTile"), ("tile corner", "radius.iconTile"), ("section header", "color.text.sectionHeader"), ("footnote", "color.text.footnote")],
     [("one-line rows", "card-grouped"), ("two-line rows", "card-grouped-two-line"), ("on the grey page", "card-grouped-alt")], ""),
    ("Message bubble", "card", "Outgoing bubbles on the right in the theme's bubble colour; incoming on the left. Link previews sit inside as a tinted card with a bar.",
     [("outgoing", "color.surface.bubbleOut"), ("outgoing, end", "color.surface.bubbleOutEnd"), ("incoming", "color.surface.bubbleIn"), ("text", "color.text.onBubbleOut"),
      ("time", "color.text.bubbleMeta"), ("link", "color.text.bubbleLink"), ("preview card", "color.surface.quote"), ("preview title", "color.text.quoteTitle"),
      ("corner", "radius.bubble"), ("text type", "typography.bubble")],
     [("link preview", "bubble-out-link-preview"), ("file", "bubble-out-file"), ("theme preview", "bubble-in-out-preview")],
     "Dark's outgoing bubble is a violet-to-blue gradient; light's is a flat pale green."),
    ("Service message", "badge", "Small translucent pills centred in the thread for events (topic created, topic links).",
     [("fill", "color.surface.service"), ("text", "color.text.service")],
     [("in a thread", "service-message")], ""),
    ("Topics bar and pinned message", "tabs", "A forum group shows its topics as a scrolling glass bar, and the pinned message as a glass strip under it.",
     [("fill", "color.surface.chipBar"), ("text", "color.text.primary")],
     [("default", "topics-bar-pinned")], ""),
    ("Chat row", "list row", "60 pt avatar, a semibold title with mute and status marks, a two-line preview, time and read ticks, and a pin for pinned chats.",
     [("height", "size.rowChat"), ("avatar", "size.avatarChat"), ("title type", "typography.chatTitle"), ("preview type", "typography.subheadline"),
      ("preview", "color.text.preview"), ("time", "color.text.time"), ("ticks", "color.text.readMark"), ("pinned band", "color.bg.pinned"), ("divider", "color.border.list")],
     [("pinned", "list-row-chat-pinned"), ("edit mode", "list-row-chat-edit-mode")],
     "Edit mode adds selection circles and reorder handles and greys the bottom actions."),
    ("Call, contact and search rows", "list row", "Plain rows on the black or white list background with a smaller avatar.",
     [("call row", "size.rowCall"), ("contact row", "size.rowContact"), ("avatar", "size.avatarList"), ("online", "color.text.online"), ("missed", "color.text.missed"),
      ("username", "color.text.username"), ("info", "color.accent.default")],
     [("call", "list-row-call"), ("missed call", "list-row-call-missed"), ("contact", "list-row-contact"), ("search result", "list-row-search-result")],
     "A missed call's name turns red."),
    ("Destructive row", "list row", "A card row in red text with a red glyph (Terminate all other sessions).",
     [("text", "color.text.danger"), ("card", "color.surface.card")],
     [("default", "list-row-destructive")], "No red fill appears anywhere."),
    ("Avatar", "avatar", "Photos in circles; contacts without one get initials on a gradient from a fixed palette.",
     [("chat", "size.avatarChat"), ("list", "size.avatarList"), ("red", "color.avatar.red"), ("green", "color.avatar.green"), ("blue", "color.avatar.blue")],
     [("initials", "avatar-initials")], ""),
    ("Badge", "badge", "Muted grey count capsules on folder chips and the archive row. No accent unread badge appears: every chat in the captures was read.",
     [("muted", "color.badge.muted"), ("text", "color.text.onAccent")],
     [("chip count and archive count", "badge-muted")], ""),
    ("Index scrubber", "list row", "Accent letters down the right edge of a long contact list.",
     [("colour", "color.accent.default")],
     [("New Message", "index-scrubber")], ""),
    ("Theme picker", "radio or segmented control", "Appearance shows a live chat preview and a row of theme cards; the chosen card has an accent outline.",
     [("outline", "color.accent.default"), ("bubble in", "color.surface.bubbleIn"), ("bubble out", "color.surface.bubbleOut")],
     [("cards", "theme-picker")], ""),
    ("Empty state", "pattern", "In-chat search with no match says 'No Results' in the bottom glass bar instead of filling the thread.",
     [("text", "color.text.secondary")],
     [("no results", "empty-state-no-results")], ""),
    ("Bottom toolbar", "pattern", "Edit mode's actions (Read All, Archive, Delete) as glass capsules along the bottom, disabled until a chat is chosen.",
     [("label", "color.text.disabledAction")],
     [("disabled", "toolbar-disabled")], ""),
    ("Profile header", "pattern", "The Settings root opens with a large photo, the name, and the handle under it; the phone number beside the handle is masked.",
     [("name type", "typography.profileName"), ("handle", "color.text.secondary")],
     [("default", "profile-header")], ""),
]

GAPS = [
    ("Dialog or alert", "Not captured. The only dialogs on offer were destructive (Delete, Terminate sessions), and nothing was tapped."),
    ("Toast", "Not seen in any capture."),
    ("Accent unread badge", "Not captured: every chat was already read, so only muted counts show."),
    ("Passcode lock", "Not captured: the owner unlocked the app before the capture ran."),
    ("Pressed states and motion", "Not captured: stills made with clicks."),
    ("Keyboard", "iPhone Mirroring types from the Mac keyboard, so the software keyboard never shows."),
    ("Light-theme detail screens", "Light covers 15 of the 39 captures; search, sheets, edit mode, menus over lists and the contact screens beyond the list are dark only."),
    ("Warning colour", "No warning state appeared."),
    ("Form validation", "No form with an error appeared; Telegram's settings apply as you change them."),
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
