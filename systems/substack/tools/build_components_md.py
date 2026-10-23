#!/usr/bin/env python3
"""Write components.md from the inventory below, tokens.json and components/crops/ (native kit).

Adapted from the native kit (from systems/grokbot): NAME, INVENTORY and GAPS (PRODUCT (adapt)) are Substack's.

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

NAME = "Substack"  # PRODUCT (adapt)

# PRODUCT (adapt): (component, checklist item, what it is, [(property, token path)], [(state, crop stem)], notes)
INVENTORY = [
    ("Primary button", "button", "Orange filled button for Substack's own actions (Turn on, Subscribe back, Share on the owner's profile).",
     [("fill", "color.accent.brand"), ("Share fill", "color.accent.brandShare"), ("label", "color.text.onBrand"), ("label type", "typography.headline"),
      ("height", "size.button"), ("banner height", "size.buttonBanner"), ("small height", "size.buttonSmall"), ("corner", "radius.button"), ("small corner", "radius.small")],
     [("Share and Edit", "button-share-edit"), ("Subscribe back", "button-subscribe-back"), ("banner pair", "banner-notifications-off")],
     "Corners are rounded rectangles (12 pt), not capsules. Share reads a lighter orange than Turn on; both sit beside a grey secondary button of the same size."),
    ("Secondary button", "button", "Grey filled or outlined button beside a primary (Edit, Later, Message).",
     [("fill", "color.surface.secondary"), ("label", "color.text.primary"), ("outline", "color.border.outline"), ("corner", "radius.button")],
     [("Message (outlined)", "button-outline-message"), ("Edit", "button-share-edit")], ""),
    ("Publication Subscribe button", "button", "A post's Subscribe buttons take the publication's own colour: a filled button in the body and a glass pill in the nav bar.",
     [("fill", "color.accent.publication"), ("nav pill", "color.accent.publicationGlass"), ("label", "color.text.onPublication"), ("height", "size.buttonPublication"),
      ("nav pill height", "size.navPill"), ("corner", "radius.publicationButton")],
     [("in the post", "button-publication-subscribe"), ("nav bar", "nav-bar-reader")],
     "Only one publication was read (#538BFA). Another publication shows its own colour here."),
    ("Link button", "link", "Blue text set alone in a grouped card (Restore in-app purchases), or inline in helper text (Learn more).",
     [("colour", "color.text.link"), ("type", "typography.link")],
     [("in a card", "button-link-restore"), ("inline", "empty-state-payments")], ""),
    ("Destructive button", "button", "Red text centred in its own grouped card (Disable all).",
     [("label", "color.text.danger"), ("fill", "color.surface.card"), ("corner", "radius.card")],
     [("Disable all", "button-danger-disable-all")], "Never a red fill."),
    ("Icon button", "icon button", "Round glass buttons for back, close and more; the orange compose button floats over feeds.",
     [("size", "size.navButton"), ("fill", "color.surface.glass"), ("compose size", "size.fab"), ("compose fill", "color.accent.brandFab"), ("glyph", "color.text.onBrand")],
     [("back", "icon-button-back"), ("compose", "fab-compose")], ""),
    ("Navigation bar", "navigation bar", "No bar background: a glass back button, an optional pill (Subscribe, the publication name) and a glass more button float over the content.",
     [("button", "size.navButton"), ("fill", "color.surface.glass"), ("title type", "typography.headline")],
     [("post reader", "nav-bar-reader")], ""),
    ("Tab bar", "tabs", "Floating iOS 26 glass capsule with five items (Home, Read, Podcasts, Chat, Activity); the selected item sits on a pill.",
     [("height", "size.tabBar.height"), ("width", "size.tabBar.width"), ("item pill", "size.tabBar.item"), ("fill", "color.surface.tabBar"), ("selected pill", "color.surface.tabBarSelected"),
      ("label", "color.text.tabBar"), ("selected label", "color.text.tabBarSelected"), ("badge", "color.accent.dot"), ("label type", "typography.caption")],
     [("Read selected", "tab-bar-read"), ("Chat badge", "tab-bar-chat-badge")], ""),
    ("Top tabs", "tabs", "A scrolling row of text tabs under a screen title; the selected one sits on a glass pill.",
     [("height", "size.tab"), ("selected pill", "color.surface.tabSelected"), ("selected label", "color.text.tabActive"), ("label", "color.text.tertiary"), ("type", "typography.subheadline")],
     [("For you", "tabs-top-for-you"), ("Saved", "tabs-top-saved")], ""),
    ("Search field", "text field", "Glass capsule with a magnifier; focused it shows a caret, typed it gains a clear button.",
     [("height", "size.searchField"), ("fill", "color.surface.glass"), ("placeholder", "color.text.placeholder"), ("caret", "color.focus.caret"), ("corner", "radius.capsule")],
     [("focused", "search-field-focused"), ("typed", "search-field-typed"), ("Chat, empty", "search-field-chat")],
     "Focus shows only the caret, in the text colour."),
    ("Chip", "chip", "Topic chips under search: the selected one is filled with the theme's ink, the rest are outlined tiles.",
     [("height", "size.chip"), ("fill", "color.surface.tile"), ("rim", "color.border.raised"), ("type", "typography.subheadline"), ("corner", "radius.capsule")],
     [("Suggested selected", "chips-suggested"), ("suggestions while typing", "chips-typed")], ""),
    ("Switch", "checkbox or toggle / switch", "iOS switch, tinted the system blue.",
     [("width", "size.switch.width"), ("height", "size.switch.height"), ("on", "color.control.switchOn"), ("thumb", "color.control.switchThumb")],
     [("on", "switch-on")], "Only the on state was seen."),
    ("Checkbox", "checkbox or toggle / switch", "Square checkboxes in a grid of email and push columns (Engagement).",
     [("size", "size.checkbox"), ("corner", "radius.small"), ("checked fill", "color.control.checkbox"), ("tick", "color.control.checkboxTick")],
     [("checked", "checkbox-grid")], "The checked fill is the theme's ink (white in dark, near-black in light), not an accent. No unchecked box was seen."),
    ("Checklist", "radio or segmented control", "Single choice in a grouped card: a blue tick on the chosen row (Theme, Default tab).",
     [("tick", "color.control.check"), ("row", "size.row"), ("icon tile", "color.surface.iconTile")],
     [("System chosen", "checklist-theme")], ""),
    ("Option buttons", "radio or segmented control", "Display Settings picks a font and a size from outlined buttons; the chosen one gets a thick blue rim, a blue tint and a blue label.",
     [("height", "size.option"), ("corner", "radius.option"), ("rim", "color.border.option"), ("selected rim", "color.control.optionRim"), ("selected fill", "color.surface.optionSelected"),
      ("selected label", "color.text.selected"), ("label", "color.text.tertiary"), ("rim width", "border.width.option"), ("selected rim width", "border.width.optionSelected")],
     [("New York and Default selected", "option-buttons")], "Font options are set in their own typeface."),
    ("Sheet", "sheet", "Options, Display Settings and the notifications pre-prompt rise as sheets with a grabber, a title, a subtitle and a round close button.",
     [("fill", "color.surface.sheet"), ("corner", "radius.sheet"), ("scrim", "color.bg.scrim"), ("divider", "color.border.sheet"), ("title type", "typography.headline")],
     [("Display Settings", "sheet-display-settings"), ("notifications pre-prompt", "sheet-notifications-prompt")], ""),
    ("Action sheet menu", "menu or action sheet", "Post and note options as icon rows in a sheet, grouped by hairlines; destructive items come last in red.",
     [("fill", "color.surface.sheet"), ("item type", "typography.headline"), ("destructive", "color.text.danger"), ("divider", "color.border.sheet")],
     [("post options", "sheet-options-destructive"), ("note options", "menu-note-destructive")], "No context menu (iOS pull-down) appeared; long-press on a note opens this sheet."),
    ("Banner", "toast or banner", "A raised card at the top of Chat with a warning icon, a title, a subtitle, a close button and two buttons.",
     [("fill", "color.surface.banner"), ("rim", "color.border.raised"), ("corner", "radius.card"), ("subtitle", "color.text.tertiary")],
     [("notifications off", "banner-notifications-off")], "In light the card has a soft shadow; in dark only a rim. No toast appeared."),
    ("Grouped card", "card", "Settings rows grouped in a card on bg.grouped, each with a rounded icon tile and a chevron.",
     [("fill", "color.surface.card"), ("behind", "color.bg.grouped"), ("corner", "radius.card"), ("divider", "color.border.grouped"), ("row", "size.row"), ("icon tile", "color.surface.iconTile")],
     [("Saved, Archive, Downloads", "card-grouped-settings"), ("account", "card-account")], ""),
    ("Featured card", "card", "A large card at the top of Read: the post's image fades into a dark panel with the publication, title, subtitle, meta and a save button.",
     [("title type", "typography.headline"), ("meta type", "typography.footnote")],
     [("For you", "card-featured")], "The panel takes its colour from the post image, so it has no token."),
    ("Podcast card", "card", "Episode cards whose lower half takes the artwork's colour, with a glass play pill showing the duration.",
     [("title type", "typography.headline"), ("meta type", "typography.footnote")],
     [("Next up", "card-podcast")], "Colours come from each episode's artwork."),
    ("Raised row", "card", "A full-width row on a page with a rim ('View saved notes', 'Find people you know').",
     [("fill", "color.surface.raised"), ("rim", "color.border.raised"), ("height", "size.raisedRow"), ("corner", "radius.card")],
     [("View saved notes", "card-raised-row"), ("Find people", "card-find-people")], ""),
    ("List row", "list row", "Inbox, saved, search, trending, activity and chat rows: publication or person, title, meta line, optional thumbnail, unread dot at the left edge.",
     [("title", "typography.headline"), ("meta", "typography.footnote"), ("meta colour", "color.text.tertiary"), ("divider", "color.border.divider"), ("thumbnail", "size.thumbnail"), ("unread dot", "color.accent.dot")],
     [("inbox, unread", "list-row-inbox-unread"), ("saved, progress", "list-row-saved-progress"), ("search result", "list-row-search-result"), ("trending", "list-row-trending"),
      ("activity", "list-row-activity"), ("chat, unread", "list-row-chat-unread")], ""),
    ("Note", "card", "A note in the feed: avatar, name, date and orange Subscribe link, the text, then like, comment, restack and share counts.",
     [("text", "typography.body"), ("subscribe link", "color.text.brand"), ("actions", "color.text.secondary"), ("divider", "color.border.divider")],
     [("in the feed", "note-feed")], ""),
    ("Post reader", "pattern", "Kicker, heavy title, subtitle, byline with avatars and a Listen pill, then the serif body; a glass action bar floats above the tab bar.",
     [("kicker", "typography.kicker"), ("title", "typography.postTitle"), ("subtitle", "typography.postSubtitle"), ("body", "typography.reader"), ("body colour", "color.text.reader"), ("Listen pill", "color.surface.tile")],
     [("header", "reader-header"), ("body", "reader-body-serif"), ("action bar", "action-bar-floating")], ""),
    ("Avatar", "avatar", "Publications show as rounded squares of their artwork in the top row of Home; people show as circles.",
     [("publication", "size.avatarStory"), ("unread dot", "color.accent.dot")],
     [("publication row", "avatar-story-row"), ("profile", "avatar-profile")], "Artwork is each publication's own."),
    ("Badge", "badge", "Orange dots for unread: on publication avatars, at the start of inbox and chat rows, and on the Chat tab.",
     [("dot", "color.accent.dot")],
     [("Chat tab", "tab-bar-chat-badge"), ("inbox row", "list-row-inbox-unread")], ""),
    ("Progress bar", "progress", "A short grey reading-progress bar on saved posts.",
     [("track", "color.control.progressTrack"), ("fill", "color.control.progressFill"), ("width", "size.progress")],
     [("14m left", "progress-reading")], "Grey, not an accent."),
    ("Search highlight", "pattern", "Matched words in search results are blue on a pale blue highlight.",
     [("text", "color.text.highlight"), ("fill", "color.surface.highlight")],
     [("design", "highlight-search")], ""),
    ("Empty state", "pattern", "A bold line and a tertiary line centred in a card (Payments), or a single suggestion row (search, no results).",
     [("title type", "typography.link"), ("text", "color.text.tertiary"), ("card", "color.surface.card")],
     [("Payments", "empty-state-payments"), ("search, no results", "empty-state-search")], ""),
    ("Profile header", "pattern", "Name, handle, bio, recommendation chip, subscriber count, Share and Edit, Creator stats, then tabs.",
     [("bio", "typography.body"), ("handle", "color.text.secondary"), ("chip", "color.surface.tile")],
     [("own profile", "profile-header")], ""),
]

# PRODUCT (adapt)
GAPS = [
    ("Dialog or alert", "Not captured. The only actions that might confirm (Block, Disable all) are destructive and were not tapped."),
    ("Chat thread", "Not captured: every chat showed an unread dot, and opening one would mark it read."),
    ("Compose", "Not captured: opening the compose button risked posting a draft."),
    ("Text area and form validation", "Not captured: no editable form was opened."),
    ("Toast", "Not seen in any capture."),
    ("Switch off, unchecked checkbox", "Not seen: every switch and checkbox was on as found, and none was changed."),
    ("Pressed states and motion", "Not captured: stills made with clicks."),
    ("Keyboard", "iPhone Mirroring types from the Mac keyboard, so the software keyboard never shows."),
    ("Loading and error states", "Not seen; cutting the network ends the mirroring session."),
    ("Light theme", "16 of 19 screens. The pre-prompt, search with no results and the note options sheet are dark only."),
    ("Success and warning colours", "No success state appeared; the warning banner draws its icon in the text colour."),
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
