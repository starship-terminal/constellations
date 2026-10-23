#!/usr/bin/env python3
"""Write components.md from the inventory below, tokens.json and components/crops/ (native kit).

Copied from the native kit (systems/grokbot). Adapt NAME, INVENTORY and GAPS (PRODUCT (adapt)).

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

NAME = "Claude for iOS"  # PRODUCT (adapt)

# PRODUCT (adapt): (component, checklist item, what it is, [(property, token path)], [(state, crop stem)], notes)
INVENTORY = [
    ("Primary pill", "button", "The inverse capsule that carries a screen's main action: Talk in the composer, New chat, New project and New session floating at the bottom right, Share at the foot of a promo sheet.",
     [("height", "size.pill"), ("full-width height", "size.button"), ("Talk", "size.talk.width"), ("corner", "radius.capsule"), ("fill", "color.button.primary.bg"),
      ("label", "color.button.primary.text"), ("label type", "typography.callout")],
     [("New chat over the sidebar", "button-primary-pill"), ("full width (Share)", "button-primary-full")],
     "Near-white in dark, near-black in light. No button is filled orange or blue; orange is kept for send."),
    ("Secondary pill", "button", "A glass capsule with a + and a label (Add device).",
     [("height", "size.pillSecondary"), ("corner", "radius.capsule"), ("fill", "color.surface.glass"), ("label", "color.text.primary")],
     [("default", "button-secondary-glass")], ""),
    ("Icon button", "icon button", "Round iOS 26 glass buttons for the sidebar, close, back, more, filter and search; two can join into one glass capsule (new chat and more in a thread).",
     [("size", "size.navButton"), ("fill", "color.surface.navGlass"), ("glyph", "color.text.primary"), ("active filter", "color.accent.filter")],
     [("new chat", "icon-button-glass"), ("active filter (Archived)", "icon-button-accent")],
     "An active filter fills the glass with the brand orange."),
    ("Link", "link", "Action text in a card (Add account, Give the gift of Claude) and underlined 'Learn more' inside subtitles.",
     [("colour", "color.text.link"), ("type", "typography.body")],
     [("in the account card", "card-account")], ""),
    ("Composer", "text field", "Two rows in one glass block: the input line over a row of controls (+, model and effort pill, microphone, then Talk or send).",
     [("height", "size.composer.height"), ("width", "size.composer.width"), ("corner", "radius.composer"), ("fill", "color.surface.glass"), ("placeholder", "color.text.placeholder"),
      ("control", "size.control"), ("control fill", "color.button.control.bg"), ("send", "size.send"), ("send fill", "color.button.send.bg"), ("caret", "color.focus.caret"), ("type", "typography.body")],
     [("new chat", "composer-new-chat"), ("typed", "composer-typed"), ("thread", "composer-thread")],
     "With text, the Talk pill turns into the round orange send button. The placeholder changes with context (Chat with Claude, Reply to Claude or hold to talk)."),
    ("Search field", "text field", "A glass capsule floating at the bottom of a list; typing turns it into a field with a clear button and a round close button beside it.",
     [("height", "size.searchField"), ("fill", "color.surface.glass"), ("typed fill", "color.surface.search"), ("placeholder", "color.text.placeholder")],
     [("default", "search-bar-glass"), ("typed", "search-field-typed")], ""),
    ("Pop-up select", "select or picker", "A rimmed field with a value and a down chevron (Break reminders).",
     [("height", "size.select"), ("corner", "radius.field"), ("fill", "color.surface.field"), ("rim", "color.border.field"), ("chevron", "color.text.tertiary")],
     [("default", "select-field")], "Its open state was not captured."),
    ("Switch", "checkbox or toggle / switch", "iOS 26 switch with a pill thumb, in the interactive blue.",
     [("width", "size.switch.width"), ("height", "size.switch.height"), ("thumb", "size.switch.thumb"), ("on", "color.switch.on"), ("on, locked", "color.switch.onDisabled"),
      ("off", "color.switch.off"), ("thumb colour", "color.switch.thumb"), ("locked thumb", "color.switch.thumbDisabled")],
     [("locked and on", "switch-on-disabled"), ("off (Usage credits)", "switch-off"), ("off (Research, in a sheet)", "switch-research-off")],
     "A setting another one requires (Artifacts) shows its switch on but dimmed, with a grey thumb in dark."),
    ("Day toggles", "radio or segmented control", "Seven round toggles, one per weekday (Quiet hours).",
     [("size", "size.dayToggle"), ("fill", "color.surface.dayToggle"), ("letter", "color.text.tertiary")],
     [("all off", "day-toggles")], "Only the off state was captured."),
    ("Appearance tiles", "radio or segmented control", "Three preview tiles (Light, Dark, System); the chosen one gets a blue ring and a blue label.",
     [("chosen label", "color.text.selected"), ("ring", "color.accent.default"), ("label type", "typography.callout"), ("card", "color.surface.card")],
     [("System chosen (dark), Light chosen (light)", "segmented-appearance")], ""),
    ("Navigation bar", "navigation bar", "No bar: glass buttons float over the content at the top, with a centred title on list pages and sheets. A scrolled sheet blurs what passes under its title.",
     [("button", "size.navButton"), ("title type", "typography.headline"), ("fill", "color.surface.navGlass")],
     [("thread", "nav-bar-thread"), ("sheet", "nav-bar-sheet"), ("scrolled, blurred", "nav-bar-scrolled-blur")], ""),
    ("Sidebar", "navigation bar", "The app's main navigation slides in from the left over a dimmed page: a serif wordmark, six destinations with outline icons, then Pinned and Recents chats, the account avatar and a New chat pill.",
     [("fill", "color.bg.sidebar"), ("wordmark", "typography.titleSerif"), ("item type", "typography.bodyLarge"), ("row", "size.rowSidebar"),
      ("selected fill", "color.surface.selected"), ("selected corner", "radius.row"), ("section header", "color.text.secondary")],
     [("open", "sidebar-nav"), ("selected row", "sidebar-selected-row")],
     "There is no tab bar: the sidebar is the only top-level navigation."),
    ("Menu", "menu or action sheet", "iOS 26 glass pull-down (chat more) and context menu (long press on a message). Destructive items are red text with a red icon below a divider.",
     [("corner", "radius.menu"), ("fill", "color.surface.menu"), ("item type", "typography.body"), ("destructive", "color.text.danger"), ("divider", "color.border.divider")],
     [("chat more, with Delete", "menu-chat-destructive"), ("long press on a message", "menu-context-message")],
     "The pull-down does not dim the page; the long-press menu dims the thread and lifts the message."),
    ("Bottom sheet", "sheet", "Sheets rise from the bottom over a dimmed page, with a grabber, a round glass close or back button and a centred title; they hold grouped cards.",
     [("fill", "color.bg.sheet"), ("corner", "radius.sheet"), ("behind", "color.bg.scrim"), ("grabber", "color.border.grabber"), ("grabber size", "size.grabber.width"),
      ("card corner", "radius.cardSheet"), ("tick", "color.accent.check"), ("title", "typography.headline")],
     [("Select model", "sheet-model-picker"), ("Effort, pushed inside the sheet", "sheet-effort"), ("Add to Chat", "sheet-add-to-chat"), ("tool-step timeline", "sheet-timeline"), ("promo", "sheet-promo")],
     "Effort pushes inside the model sheet and swaps the close button for a back button."),
    ("Grouped card", "card", "Rows grouped in a rounded card with hairline dividers inset to the row text; an icon leads each settings row and a chevron or value ends it.",
     [("fill", "color.surface.card"), ("corner", "radius.card"), ("divider", "color.border.divider"), ("row", "size.row"), ("two-line row", "size.rowTwoLine"),
      ("padding", "space.cardPadding"), ("value", "color.text.tertiary"), ("chevron", "color.text.chevron")],
     [("account", "card-account"), ("settings rows", "card-settings-rows")], "Cards carry no rim and no shadow."),
    ("Artifact card", "card", "A list card that is only a rim on the page: a thumbnail on the left, a title, a sharing line and a date.",
     [("rim", "color.border.card"), ("title", "typography.callout"), ("meta", "typography.subheadline")],
     [("default", "card-artifact")], "The thumbnails are the owner's artifacts; take the layout, not the images."),
    ("Message bubble", "card", "The owner's messages sit in a grey bubble on the right. Claude's replies have no bubble: serif text straight on the page.",
     [("fill", "color.surface.userBubble"), ("text", "color.text.primary"), ("corner", "radius.bubble"), ("max width", "size.bubbleMaxWidth"), ("type", "typography.body")],
     [("owner", "bubble-user")], ""),
    ("Response", "pattern", "Claude's reply: a tool-step summary row, serif paragraphs, a row of outline action icons and a disclaimer.",
     [("text", "color.text.response"), ("type", "typography.response"), ("tool step", "color.text.tertiary"), ("tool step type", "typography.callout"),
      ("actions", "color.text.tertiary"), ("disclaimer", "color.text.footnote")],
     [("tool step", "tool-step-row"), ("serif text", "response-serif"), ("actions and disclaimer", "response-actions")],
     "The tool-step row opens a timeline sheet of the steps."),
    ("Greeting", "pattern", "A new chat shows the orange spark over one serif line that changes with the time of day.",
     [("spark", "color.accent.brand"), ("text", "color.text.greeting"), ("type", "typography.titleSerif")],
     [("new chat", "greeting")], "The spark is Anthropic's mark: keep the layout, draw your own mark."),
    ("List row", "list row", "Chats and Projects rows: an outline icon, a one-line title and a subtitle (time or description), no dividers.",
     [("title", "typography.body"), ("subtitle", "typography.callout"), ("subtitle colour", "color.text.footnote"), ("row", "size.rowList")],
     [("chat", "list-row-chat"), ("project", "list-row-project")], ""),
    ("Badge", "badge", "Small capsules after a label: neutral (Recommended, Beta) or amber for a cost warning ('5.5x or more usage').",
     [("height", "size.badge"), ("fill", "color.badge.bg"), ("label", "color.badge.text"), ("warning fill", "color.badge.warningBg"), ("warning label", "color.badge.warningText"),
      ("type", "typography.caption")],
     [("Recommended", "badge-recommended"), ("usage warning", "badge-usage-warning"), ("Beta", "badge-beta")], ""),
    ("Usage meter", "pattern", "A thin rounded track in a card, with the share used at the right of the title and the reset time under it.",
     [("height", "size.progress"), ("fill", "color.progress.fill"), ("track", "color.progress.track"), ("card", "color.surface.card")],
     [("current session", "progress-usage")], ""),
    ("Empty state", "pattern", "An outline icon in a grey circle over one centred line of tertiary text, sometimes with an explanation under it.",
     [("circle", "size.emptyIcon"), ("circle fill", "color.surface.emptyIcon"), ("text", "color.text.tertiary"), ("type", "typography.body")],
     [("no archived projects", "empty-state-archived"), ("no sessions", "empty-state-sessions")], ""),
]

# PRODUCT (adapt)
GAPS = [
    ("Tab bar", "Not present. The sidebar is the app's navigation."),
    ("Dialog or alert", "Not captured. Delete was not tapped, the only action that leads to one."),
    ("Toast", "Not seen in any capture."),
    ("Streaming and loading", "Not captured: no message was sent."),
    ("Voice and Talk mode", "Not captured: it would raise a microphone prompt and start a session."),
    ("Pop-up select, open", "Not captured; the projects filter menu was opened but not captured."),
    ("Pressed states and motion", "Not captured: stills made with clicks."),
    ("Keyboard", "iPhone Mirroring types from the Mac keyboard, so the software keyboard never shows."),
    ("Light-theme detail", "Light was captured for 12 of the 36 screens; effort, tool steps, lists, empty states, artifacts and the promo sheet are dark only."),
    ("Success colour", "No success state appeared."),
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
