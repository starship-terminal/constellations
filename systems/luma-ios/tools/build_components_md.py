#!/usr/bin/env python3
"""Write components.md from the inventory below, tokens.json and components/crops/ (native kit).

Copied from tools/kit/native (Grok Bot's). Adapt NAME, INVENTORY and GAPS (PRODUCT (adapt)).

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

NAME = "Luma"  # PRODUCT (adapt)

# PRODUCT (adapt): (component, checklist item, what it is, [(property, token path)], [(state, crop stem)], notes)
INVENTORY = [
    ("Tab bar", "tabs", "A floating glass capsule with three tabs (Home, Discover, Chat), icon over label, centred above the home indicator.",
     [("height", "size.tabBar.height"), ("width", "size.tabBar.width"), ("selected pill width", "size.tabBar.selected"), ("fill", "color.surface.glass"),
      ("selected pill", "color.surface.selected"), ("label", "color.text.tab"), ("selected label", "color.text.tabSelected"), ("label type", "typography.tab"),
      ("unread count", "color.danger.emphasis"), ("count size", "size.countBadge"), ("icon", "size.icon.tab")],
     [("Home selected", "tab-bar-home-selected"), ("Chat selected", "tab-bar-chat-selected"), ("unread count", "count-badge-tab")],
     "The selected tab sits in a pill darker than the bar in both themes, and its label takes the ink, not a brand colour. The bar stays the same on every screen, sheets and menus included."),
    ("Navigation bar", "navigation bar", "No bar fill: round glass buttons float at the top corners. Tab roots show the account avatar and a title; pushed pages a back button and a centred title.",
     [("button", "size.navButton"), ("button fill", "color.surface.glass"), ("title type", "typography.navTitle"), ("root title type", "typography.title2"),
      ("avatar", "size.avatar.header")],
     [("tab root", "nav-bar-tab-root"), ("pushed", "nav-bar-pushed"), ("event, compact title", "nav-bar-compact-event"), ("scrolled, blurred", "header-scrolled-blur")],
     "Two actions on a tab root share one glass capsule (+ and the bell). Scrolled content blurs under the header rather than meeting a bar edge."),
    ("Event row", "list row", "The app's main list item: a square cover thumbnail, then host line, title (up to two lines) and meta lines with small icons, and a pill at the top right.",
     [("thumbnail", "size.thumb"), ("thumbnail corner", "radius.thumb"), ("gap", "space.md"), ("host", "color.text.secondary"), ("host type", "typography.subhead"),
      ("title", "color.text.primary"), ("title type", "typography.headline"), ("meta", "color.text.secondary"), ("meta type", "typography.callout"), ("meta icon", "size.icon.meta"),
      ("divider", "color.border.divider"), ("divider width", "border.width.hairline")],
     [("invited, priced", "event-row-invited-price"), ("sold out", "event-row-sold-out"), ("date section", "date-section")],
     "Rows group under date sections: the date in the ink, then '/ weekday' in text.tertiary. The divider starts at the text, not the screen edge."),
    ("Badge", "badge", "'Invited' on a thumbnail: a purple capsule straddling the thumbnail's lower edge, ringed in the page colour.",
     [("height", "size.badge"), ("fill", "color.accent.subtle"), ("label", "color.accent.fg"), ("label type", "typography.caption"), ("corner", "radius.capsule")],
     [("Invited", "badge-invited")], ""),
    ("Status pill", "badge", "A small capsule at the top right of an event row: the price, or the event's state.",
     [("height", "size.pill"), ("type", "typography.pill"), ("price fill", "color.success.subtle"), ("price label", "color.success.fg"),
      ("sold out fill", "color.danger.subtle"), ("sold out label", "color.danger.fg"), ("near capacity fill", "color.warning.subtle"),
      ("near capacity label", "color.warning.fg"), ("waitlist fill", "color.info.subtle"), ("waitlist label", "color.info.fg")],
     [("price", "pill-price"), ("Sold Out", "pill-sold-out"), ("Near Capacity", "pill-near-capacity"), ("Waitlist Open", "pill-waitlist-open")],
     "The fills are faint washes of the label colour (about 6 to 8% over the page), so the label carries the meaning."),
    ("Search field", "text field", "A glass capsule beside the back button, with a leading magnifier and a clear button once typed.",
     [("height", "size.searchField"), ("fill", "color.surface.glass"), ("caret", "color.focus.caret"), ("corner", "radius.capsule")],
     [("focused, empty, with chips", "search-field-focused-chips"), ("typed", "search-field-typed")],
     "Focus shows only as the caret; there is no ring."),
    ("Filter chip", "button", "Glass capsules under the search field (Near you, Any Date), icon then label; each opens a menu or sheet.",
     [("height", "size.chip"), ("fill", "color.surface.glass"), ("label type", "typography.callout"), ("gap", "space.sm")],
     [("default", "chip-filter")], ""),
    ("Category chip", "button", "Outlined capsules with a coloured line icon (Family, Tech, Food & Drink) on Discover, in two scrolling rows.",
     [("height", "size.categoryChip"), ("outline", "color.border.chip"), ("outline width", "border.width.outline"), ("label type", "typography.callout")],
     [("default", "chip-category")],
     "The only outlined control in the app. Each category's icon has its own colour; those are artwork, not tokens."),
    ("Segmented control", "radio or segmented control", "Upcoming and Past on Your Events: a glass capsule with a darker selected pill.",
     [("height", "size.segmented.height"), ("pill height", "size.segmented.pill"), ("fill", "color.surface.glass"), ("selected pill", "color.surface.selected"),
      ("label type", "typography.callout")],
     [("Upcoming", "segmented-upcoming"), ("Past", "segmented-past")], ""),
    ("Primary button", "button", "A full-width capsule in the theme's ink at the bottom of a sheet (Confirm).",
     [("height", "size.button"), ("fill", "color.button.primary.bg"), ("label", "color.button.primary.text"), ("corner", "radius.capsule")],
     [("default", "button-primary-confirm")],
     "White in dark and near-black in light. The enabled check on Create Event is the same ink in a circle."),
    ("Accent button", "button", "Subscribe on a category page: a purple capsule with a white label, beside a round glass map button.",
     [("height", "size.buttonCompact"), ("fill", "color.button.accent.bg"), ("label", "color.button.accent.text")],
     [("Subscribe", "button-subscribe"), ("Following (glass, opens a menu)", "button-following")],
     "After subscribing the button becomes a glass 'Following' capsule with a chevron."),
    ("Event action tiles", "button", "Register, Contact and More on an event page: three equal tiles, icon over label.",
     [("height", "size.actionTile"), ("corner", "radius.control"), ("tile on the tinted page", "color.coverExample.eventButton"), ("label type", "typography.caption")],
     [("default", "event-action-tiles")],
     "Register is white in both themes; Contact and More are a lighter wash of the page's cover tint."),
    ("Cover-tinted page", "pattern", "Event pages and the Create Event sheet take their background, buttons and fields from the cover image, in both themes.",
     [("event page (one cover)", "color.coverExample.eventPage"), ("Create Event sheet (one cover)", "color.coverExample.createPage"),
      ("field on the sheet", "color.coverExample.createField"), ("title type", "typography.title2")],
     [("event page", "event-page-cover-title"), ("location, map, weather", "event-location-map-weather"), ("hosts, About Event", "event-hosts-about"),
      ("Create Event form", "form-create-event")],
     "The coverExample tokens are one cover's readings, kept as evidence; build the tint from the cover at run time. The light theme changes little here beyond the map tiles."),
    ("Menu", "menu", "Glass pull-down and pop-up menus: a tick on the current choice, line icons, separators between groups, destructive items in red.",
     [("fill", "color.surface.menu"), ("item type", "typography.body"), ("destructive item", "color.danger.fg")],
     [("pull-down with icons", "menu-pull-down-icons"), ("pop-up, location", "menu-popup-location"), ("pop-up, Nearby", "menu-popup-nearby"),
      ("destructive item, Report Event", "menu-destructive-report"), ("single destructive item, Unfollow", "menu-destructive-unfollow")], ""),
    ("Sheet", "sheet", "The Date Range sheet: glass, with an icon, title, explanation, a From/To card, a month calendar and a Confirm button.",
     [("fill", "color.surface.sheet"), ("scrim behind", "color.bg.scrim"), ("link", "color.text.link"), ("past days", "color.text.disabled"), ("button", "color.button.primary.bg")],
     [("Date Range", "sheet-date-range")], ""),
    ("Grouped card", "card", "Settings and its pages: rows in rounded cards on the grouped page, coloured icon tiles at the start, chevrons or values at the end.",
     [("page", "color.bg.grouped"), ("card", "color.surface.card"), ("corner", "radius.card"), ("row", "size.row"), ("padding", "space.cardPadding"),
      ("row divider", "color.border.cardDivider"), ("icon tile", "size.settingsIcon"), ("icon corner", "radius.icon"), ("row type", "typography.body"),
      ("section header", "color.text.tertiary")],
     [("profile", "settings-card-profile"), ("rows with icons", "settings-rows-icons"), ("section header", "settings-section-header"),
      ("pop-up values", "popup-value-rows"), ("social handles", "list-row-social-handles")], ""),
    ("Banner", "toast or banner", "Push Notifications Disabled at the top of Notification settings: a card with an icon, title, body and a text link.",
     [("fill", "color.surface.card"), ("corner", "radius.card"), ("link", "color.text.link")],
     [("default", "banner-push-disabled")], ""),
    ("Text field", "text field", "Name on Edit Profile: a capsule with a grey label on the left and the value after it.",
     [("height", "size.field"), ("fill", "color.surface.card"), ("label", "color.text.tertiary")],
     [("filled", "text-field-name"), ("Create Event name, typed", "text-field-event-name-typed")], ""),
    ("Text area", "text area", "Bio on Edit Profile: a rounded field with a grey placeholder.",
     [("corner", "radius.textArea"), ("fill", "color.surface.card"), ("placeholder", "color.text.placeholder")],
     [("empty", "text-area-bio-placeholder")], ""),
    ("Switch", "switch", "Require Approval on Create Event, off.",
     [("width", "size.switch.width"), ("height", "size.switch.height"), ("thumb", "size.switch.thumb"), ("off track", "color.switch.off"),
      ("thumb fill", "color.switch.thumb")],
     [("off, over the cover tint", "switch-off-tinted")],
     "Only seen off and over the tinted sheet, so the off track carries the cover's colour. No on state was captured."),
    ("Option cards", "radio or segmented control", "Colour Scheme on Appearance: three cards (System, Light, Dark); the selected one has an ink outline.",
     [("outline", "color.border.control"), ("selected outline", "color.border.selected"), ("selected width", "border.width.selected")],
     [("System selected (dark), Light selected (light)", "option-cards-colour-scheme"), ("app icon grid", "app-icon-grid")], ""),
    ("Destructive row", "dialog or alert", "Delete Account: a single-row card with a red label, under a footnote.",
     [("label", "color.danger.fg"), ("card", "color.surface.card"), ("footnote type", "typography.caption")],
     [("default", "destructive-row-delete-account")], "Not tapped, so the confirmation it leads to was not captured."),
    ("Chat list and thread", "list row", "Chat rows with the event cover, title, preview and date; a thread with grey bubbles and a glass composer.",
     [("row title", "typography.navTitle"), ("date", "color.text.tertiary"), ("unread dot", "color.danger.emphasis"), ("dot size", "size.dot"),
      ("bubble", "color.surface.bubble"), ("composer", "size.composer"), ("send", "color.info.emphasis"), ("send size", "size.send")],
     [("unread row", "chat-row-unread"), ("list", "chat-list"), ("image bubble", "bubble-image"), ("text bubble", "bubble-text"),
      ("composer, empty", "composer-empty"), ("composer, typed", "composer-typed-send")],
     "The send button turns blue once there is text; empty, it is a faint glass circle."),
    ("Notification row", "list row", "An avatar with a small role badge, bold names in the sentence, a grey age, and the event cover at the end.",
     [("text", "color.text.primary"), ("age", "color.text.tertiary"), ("type", "typography.callout")],
     [("default", "notification-rows")], ""),
    ("Calendar and category headers", "card", "A calendar page opens with its banner, an avatar tile and Following; a category page with an icon disc, title, counts and Subscribe.",
     [("title type", "typography.title1"), ("disc", "color.accent.tile"), ("tile", "size.calendarTile"), ("tile corner", "radius.thumb")],
     [("calendar page", "calendar-page-header"), ("category page", "category-page-header"), ("Your Calendars tiles", "calendar-tiles"),
      ("city cards", "city-cards"), ("map with event clusters", "map-event-clusters")], ""),
]

# PRODUCT (adapt)
GAPS = [
    ("Dialog or alert", "Not captured. Only Delete Account, Sign Out and Unfollow lead to one, and none was tapped."),
    ("Toast", "Not seen in any capture."),
    ("Checkbox", "Not present: booleans are switches, choices are menus with a tick."),
    ("Switch on", "Not captured: the only switch (Require Approval) was left off."),
    ("Empty state", "Not captured: search matches loosely, so even nonsense text returned events."),
    ("Loading", "Not captured: the chat list loaded before the capture ran."),
    ("Register or RSVP flow", "Not captured: registering is an action on a real event."),
    ("Pressed states and motion", "Not captured: stills made with clicks."),
    ("Keyboard", "iPhone Mirroring types from the Mac keyboard, so the software keyboard never shows."),
    ("Tooltip", "Not present."),
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
