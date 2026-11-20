#!/usr/bin/env python3
"""Write components.md from the inventory below, tokens.json and components/crops/ (native kit).

Copied from systems/grokbot. Adapt NAME, INVENTORY and GAPS (PRODUCT (adapt)).

    python3 tools/build_components_md.py

Every value in an entry is a token path; the builder refuses a path tokens.json lacks and a crop
that is not on disk, so the page cannot drift from the package. Standard library only, deterministic.
"""
import json
import os
import pathlib

# PRODUCT (adapt): name the product here once every part marked PRODUCT (adapt) is rewritten
# for it. While this is None the script stops: the kit's copy is Grok Bot's example and
# would write Grok Bot's values. KIT_EXAMPLE=1 runs the example as it is.
ADAPTED_FOR = None
if ADAPTED_FOR is None and not os.environ.get("KIT_EXAMPLE"):
    raise SystemExit("build_components_md.py is the kit's Grok Bot example, not adapted: rewrite the parts marked PRODUCT (adapt), then set ADAPTED_FOR")

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


KNOWN = set().union(*(paths(TOK[s]) for s in ("core", "light", "dark") if s in TOK))   # a one-theme app has one set

NAME = "Grok Bot"  # PRODUCT (adapt)

# PRODUCT (adapt): (component, checklist item, what it is, [(property, token path)], [(state, crop stem)], notes)
INVENTORY = [
    ("Primary button", "button", "Full-width capsule at the bottom of a sheet (Create, Send Feedback). One per screen.",
     [("height", "size.button"), ("corner", "radius.capsule"), ("fill", "color.button.primary.bg"), ("label", "color.button.primary.text"),
      ("label type", "typography.button"), ("disabled fill", "color.button.primaryDisabled.bg"), ("disabled label", "color.button.primaryDisabled.text")],
     [("default", "button-primary-default"), ("disabled", "button-primary-disabled")],
     "The enabled fill is the theme's ink (white in dark, near-black in light), not the blue accent. Disabled turns it to a grey glass. It enables as soon as the required field has text."),
    ("Inline secondary button", "button", "Small capsule at the end of a list row (Add, Added).",
     [("height", "size.secondaryButton"), ("corner", "radius.capsule"), ("fill", "color.button.secondary.bg"), ("label", "color.button.secondary.text"),
      ("disabled label", "color.text.disabled"), ("label type", "typography.subheadline")],
     [("enabled and disabled", "button-secondary-add")],
     "Disabled keeps the fill and dims the label (Added)."),
    ("Icon button", "icon button", "Round glass buttons for back, close and more, and the composer's + button.",
     [("size", "size.navButton"), ("composer +", "size.composerButton"), ("fill", "color.surface.glass"), ("glyph", "color.text.primary")],
     [("back", "icon-button-back")],
     "Each is a circle of iOS 26 glass; the fill token is its centre reading."),
    ("Link", "link", "Inline link inside a bubble, coloured and preceded by a small object icon.",
     [("colour", "color.text.link"), ("type", "typography.body")],
     [("in a bubble", "bubble-link")], ""),
    ("Text field", "text field", "Single-line field, centred placeholder (Create New Bot), or left-aligned with a label above (Edit Bot).",
     [("height", "size.field"), ("corner", "radius.field"), ("fill", "color.surface.field"), ("rim", "color.border.card"),
      ("placeholder", "color.text.placeholder"), ("text", "color.text.primary"), ("large text type", "typography.fieldLarge"), ("caret", "color.focus.caret")],
     [("empty", "text-field-empty"), ("focused", "text-field-focused"), ("typed", "text-field-typed")],
     "Focus shows only the blue caret: no ring, no border change."),
    ("Text area", "text area", "Multi-line field with helper text under it (Send Feedback).",
     [("corner", "radius.field"), ("fill", "color.surface.card"), ("placeholder", "color.text.placeholder"), ("helper", "color.text.tertiary")],
     [("focused", "text-area-focused")], ""),
    ("Composer", "text field", "The chat input: a round + button, then a glass capsule field holding a microphone and a send or voice pill.",
     [("height", "size.composer"), ("corner", "radius.capsule"), ("fill", "color.surface.glass"), ("placeholder", "color.text.placeholder"),
      ("send pill", "size.sendButton.width"), ("send fill", "color.button.send.bg"), ("send glyph", "color.button.send.glyph"), ("type", "typography.callout")],
     [("default", "composer-default"), ("focused", "composer-focused"), ("typed", "composer-typed")],
     "With text the voice pill becomes a send arrow and the microphone hides. The placeholder names the bot ('Ask [Tutor] Hardware')."),
    ("Pop-up select", "select or picker", "A row value with up-down chevrons opens a glass menu with a tick on the current choice (Voice, Speed, Language).",
     [("menu fill", "color.surface.menu"), ("menu corner", "radius.menu"), ("item type", "typography.callout")],
     [("open", "select-open")], ""),
    ("Switch", "checkbox or toggle / switch", "iOS 26 switch with a pill thumb.",
     [("width", "size.switch.width"), ("height", "size.switch.height"), ("on", "color.switch.on"), ("on, bot pages", "color.switch.onBot"),
      ("off", "color.switch.off"), ("thumb", "color.switch.thumb")],
     [("on and off, settings", "switch-settings"), ("on, bot colour", "switch-bot-color")],
     "App settings use a neutral grey for on; a bot's own pages tint it with the bot's colour."),
    ("Selection tiles", "radio or segmented control", "Appearance picks one tile per row: the chosen tile fills, its label turns primary.",
     [("selected fill", "color.surface.card"), ("unselected label", "color.text.tertiary"), ("corner", "radius.card")],
     [("Follow System and Bot color chosen", "segmented-appearance")], ""),
    ("Navigation bar", "navigation bar", "Floating glass controls over the content: a round back button, a glass title pill with the bot's avatar, a round more button.",
     [("button", "size.navButton"), ("title type", "typography.rowTitle"), ("fill", "color.surface.glass")],
     [("thread", "nav-bar-thread")],
     "No bar background: content scrolls under the glass."),
    ("Menu", "menu or action sheet", "iOS 26 glass pull-down and context menus. Destructive items are red text with a red icon.",
     [("width", "size.menuWidth"), ("corner", "radius.menu"), ("fill", "color.surface.menu"), ("item type", "typography.callout"), ("destructive", "color.text.danger"),
      ("scrim (context)", "color.bg.scrim")],
     [("+ menu", "menu-plus"), ("more, with Delete", "menu-more-destructive"), ("attach", "menu-attach"), ("long-press context", "menu-context"), ("search filter", "menu-filter")],
     "A long press lifts the bot with a preview of its last message over a dimmed home."),
    ("Sheet", "sheet", "Settings and Create New Bot open as sheets with a close button at the top left.",
     [("fill", "color.bg.sheet"), ("corner", "radius.sheet"), ("behind", "color.bg.scrim")],
     [("Create New Bot", "sheet-new-bot")], ""),
    ("Update banner", "toast or banner", "A card in Settings with a blue dot, a title, the version change and an outward arrow.",
     [("fill", "color.surface.card"), ("dot", "color.accent.default"), ("subtitle", "color.text.secondary")],
     [("update available", "banner-update")], "No toast appeared in any capture."),
    ("Grouped card", "card", "Rows grouped in a rounded card with hairline dividers inset to the text.",
     [("fill", "color.surface.card"), ("rim", "color.border.card"), ("corner", "radius.card"), ("divider", "color.border.divider"), ("row", "size.row")],
     [("bot profile", "card-grouped"), ("account", "card-account")], ""),
    ("Message bubble", "card", "Bot replies in grey bubbles on the left; the owner's in the bot's colour on the right. Runs from one sender join with tighter corners.",
     [("bot fill", "color.surface.bubble"), ("one-to-one fill", "color.surface.bubbleDirect"), ("own fill", "color.surface.ownBubble"), ("own text", "color.text.onOwnBubble"),
      ("corner", "radius.bubble"), ("joined corner", "radius.bubbleJoined"), ("max width", "size.bubbleMaxWidth"), ("text", "typography.body"), ("sender label", "typography.caption")],
     [("bot, group", "bubble-bot-group"), ("own", "bubble-own")], ""),
    ("Code block", "card", "Monospace block inside a bot bubble with a copy button.",
     [("fill", "color.surface.code"), ("text", "color.text.code"), ("corner", "radius.code")],
     [("in a bubble", "bubble-code-block")], ""),
    ("List row", "list row", "Home chat rows (avatar, title, preview, time, unread dot), search results, routines, connected apps.",
     [("title", "typography.rowTitle"), ("preview", "typography.preview"), ("time", "typography.footnote"), ("secondary", "color.text.secondary"), ("tertiary", "color.text.tertiary")],
     [("home", "list-row-home"), ("search", "list-row-search"), ("routine", "list-row-routine"), ("connected app", "list-row-connect-app")], ""),
    ("Avatar", "avatar", "Each bot is a coloured blob with two eyes, cut out of the page colour; groups stack three with a +N; the account is initials on glass.",
     [("grid size", "size.avatarGrid"), ("colours", "color.avatar.orange"), ("eye", "color.avatar.eye"), ("picker swatch", "size.swatch")],
     [("home grid", "avatar-grid"), ("account initials", "avatar-initials"), ("picker", "avatar-picker")],
     "The blob shapes are Grok Bot's artwork: borrow the system (one colour per bot, cut-out eyes), not the drawings."),
    ("Badge", "badge", "Blue unread dots after a name, an amber star on a pinned bot, a floating 'N unread' pill, account chips with a green tick.",
     [("dot", "color.accent.default"), ("star", "color.badge.star"), ("pill", "color.accent.pill"), ("pill label", "color.text.onAccent"), ("chip", "size.chip"), ("tick", "color.text.success")],
     [("star and unread dot", "badge-star-unread"), ("unread pill", "badge-unread-pill"), ("chips", "chip-account")], ""),
    ("Search bar", "text field", "Glass capsule at the bottom of home; focused it rises into a sheet with a close button and a filter menu.",
     [("height", "size.searchBar"), ("fill", "color.surface.glass"), ("placeholder", "color.text.secondary")],
     [("default", "search-bar-default"), ("focused", "search-bar-focused")], ""),
    ("Empty state", "pattern", "One centred line of tertiary text, with a magnifier above it for search.",
     [("text", "color.text.secondary"), ("type", "typography.body")],
     [("Coding", "empty-state-coding"), ("no search matches", "empty-state-search")], ""),
    ("Loading", "pattern", "A system spinner, with a label when the wait is long (Connecting...).",
     [("label", "color.text.primary")],
     [("computer", "loading-computer"), ("list", "loading-list")], ""),
    ("Usage meter", "pattern", "A full-width track in a card with the percentage under it.",
     [("track", "color.surface.secondary"), ("card", "color.surface.card")],
     [("0%", "progress-usage")], ""),
]

# PRODUCT (adapt)
GAPS = [
    ("Tab bar", "Not present. Home is one screen; the bottom holds a grid button (Connect apps) and the search bar."),
    ("Dialog or alert", "Not captured. The one destructive action seen (Delete in the chat's more menu) was not tapped, because it might delete the bot without a confirmation."),
    ("Toast", "Not seen in any capture."),
    ("Pressed states and motion", "Not captured: stills made with clicks."),
    ("Keyboard", "iPhone Mirroring types from the Mac keyboard, so the software keyboard never shows."),
    ("Light-theme detail pages", "Light was captured for 21 of the 58 screens; the rest are dark only."),
    ("Warning colour", "No warning state appeared."),
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
            found = 0
            for suffix, theme in (("", "dark"), ("-light", "light")):
                f = CROPS / f"{stem}{suffix}.png"
                if f.exists():
                    cells.append(f"[{state} ({theme})](components/crops/{f.name})")
                    found += 1
            if not found:   # a light-only app has only the -light crop
                raise SystemExit(f"{name}: no crop {stem}.png or {stem}-light.png")
        out += ["Crops: " + ", ".join(cells) + ".", ""]
        if notes:
            out += [notes, ""]
    out += ["## Gaps", "", "| Item | Status |", "|---|---|"] + [f"| {a} | {b} |" for a, b in GAPS] + [""]
    (PKG / "components.md").write_text("\n".join(out))
    print("components.md:", len(INVENTORY), "components")


if __name__ == "__main__":
    main()
