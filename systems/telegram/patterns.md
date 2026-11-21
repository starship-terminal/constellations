# Telegram patterns

How the components in [components.md](components.md) combine into Telegram's screens. Token paths are in
[tokens.json](tokens.json); the captures named here are in [screenshots/](screenshots).

## App shell and navigation

A floating glass tab bar holds four tabs: Contacts, Calls, Chats and Settings. The selected tab sits in a lighter
pill and turns the accent; everything scrolls under the bar. Chats opens on the chat list: glass Edit at the top
left, the title with the account avatar in the middle, a story camera and the accent compose button at the top
right, then the folder chip bar and the rows. See [02 dark](screenshots/dark/02-chat-list-folders-tabbar.png) and
[02 light](screenshots/light/02-chat-list-stories-archive-folders-tabbar.png). The light capture also shows the
stories strip, the search field and the archive row, which sit above the chips when the list is pulled down.

| Layer | What sits there | Tokens |
|---|---|---|
| List page | Chats, Calls, Contacts, search results | `color.bg.chats`, pinned rows on `color.bg.pinned` |
| Grouped page | Settings and its pushed pages | `color.bg.grouped` with `color.surface.card`; Chat Folders uses `color.bg.groupedAlt` with `color.surface.cardAlt` |
| Thread | A chat over its wallpaper | `color.surface.bubbleIn`, `color.surface.bubbleOut`, `color.surface.service` |
| Glass | Nav buttons, chip bar, tab bar, segmented control, composer | `color.surface.glass`, `color.surface.chipBar`, `color.surface.tabBar` |
| Sheet | New Message, the attachment picker | `color.bg.sheet`, `radius.sheet` |
| Menu | Long-press and pull-down menus | `color.surface.menu` over a blurred page |

A pushed page has a round glass back button at the top left and the title centred
([10](screenshots/dark/10-settings-notifications-switches-on-off.png)); a sheet has a round close button instead
([21](screenshots/dark/21-new-message-sheet-index.png)). There is no bar background behind either.

## Conversation

A thread shows its wallpaper edge to edge: the owner's photo in dark, Telegram's doodle pattern in light. The nav
floats over it: back, a glass title pill with the chat's name and member count, and more. A forum group adds a
glass bar of topics and the pinned message under it. Outgoing bubbles sit on the right in the theme's bubble colour
(a violet-to-blue gradient in dark, `#E1FFC7` green in light) with the time and ticks inside their bottom right.
A link gets a preview card inside the bubble with a coloured bar on its left. Service messages (a topic created,
a topic link) are small translucent pills centred in the thread. See
[03 dark](screenshots/dark/03-chat-topics-pinned-link-preview.png),
[03 light](screenshots/light/03-chat-topics-pinned-link-preview.png) and the theme preview in
[25](screenshots/dark/25-appearance-theme-cards-disabled-switch.png), the only capture with an incoming bubble.

The composer floats at the bottom: a round glass paperclip, a glass capsule field with a sticker or emoji button
inside it, and a microphone that becomes an accent send pill once there is text
([04](screenshots/dark/04-composer-typed-send-button.png)). The paperclip opens the attachment sheet, which has its
own glass tab bar: Gallery, File, Location, Poll, Checklist ([22](screenshots/dark/22-attachment-sheet-tab-bar.png),
one hostname in a thumbnail masked).

## Lists and data display

Chat rows are dense: a 60 pt avatar, a semibold title with mute and status marks, two preview lines in secondary
grey, the time at the top right with read ticks, and a pin under it for pinned chats. Pinned chats sit on a grey
band at the top. Calls and contacts are plainer rows with smaller avatars; a missed call's name turns red, and
online contacts show "online" in the accent ([14](screenshots/dark/14-calls-segmented-all.png),
[15](screenshots/dark/15-calls-segmented-missed-red.png), [16](screenshots/dark/16-contacts-list-search.png)).
A long alphabetical list gets accent index letters down its right edge ([21](screenshots/dark/21-new-message-sheet-index.png)).

Settings is grouped cards. Rows lead with a 30 pt gradient icon tile, end with a grey value and a chevron, and
take a subtitle when they need one; upper-case section headers sit above cards and grey footnotes under them
([10](screenshots/dark/10-settings-notifications-switches-on-off.png),
[11](screenshots/dark/11-settings-privacy-grouped-values.png)). Top-level settings pages that explain themselves
open with a sticker or illustration and a centred line ([12](screenshots/dark/12-checklist-with-sticker-header.png),
[13](screenshots/dark/13-chat-folders-add-pill-buttons.png), [24](screenshots/dark/24-devices-primary-button-destructive-row.png)).

## Forms and choices

Telegram has no forms with a submit button in the captures; settings apply as you change them. Booleans are
switches; a disabled one dims its track, thumb and label together
([25](screenshots/dark/25-appearance-theme-cards-disabled-switch.png)). A single choice is a card of rows with an
accent tick on the chosen one ([12](screenshots/dark/12-checklist-with-sticker-header.png),
[12 light](screenshots/light/12-checklist-auto-night-mode.png)). Two-way filters are a glass segmented control in
the nav bar ([14](screenshots/dark/14-calls-segmented-all.png)). No validation error appeared.

## Empty, loading and error states

In-chat search with no match leaves the thread as it is and says "No Results" in the bottom glass bar
([08](screenshots/dark/08-chat-search-no-results.png)). No loading or error state was captured: the app was
already synced, and cutting the network also cuts iPhone Mirroring.

## Destructive actions

Destructive actions are red text, never a red fill: Delete at the end of a message's context menu and a chat's
long-press menu, Terminate all other sessions as a card row with a red glyph
([05](screenshots/dark/05-message-context-menu-reactions.png), [19](screenshots/dark/19-chat-longpress-preview-menu.png),
[24](screenshots/dark/24-devices-primary-button-destructive-row.png)). None was tapped, so the confirmation that
follows is not captured.

## Feedback

Read state is ticks beside the time (blue in dark, green in light) and inside outgoing bubbles. Counts sit in
muted grey capsules on folder chips and the archive row ([02 light](screenshots/light/02-chat-list-stories-archive-folders-tabbar.png)).
A long press lifts the message or chat over a blurred page with a reaction bar and a menu
([05](screenshots/dark/05-message-context-menu-reactions.png), [19](screenshots/dark/19-chat-longpress-preview-menu.png)).
No toast appeared.

## Search and filtering

Search fields are glass capsules with a centred magnifier. Typing into the global search turns the field into a
left-aligned capsule with a clear button and a round close button, and lists matches under an upper-case header
([18](screenshots/dark/18-search-typed-global-results.png)). In a chat, search replaces the nav with the field and
puts date and member filters in the bottom bar ([07](screenshots/dark/07-chat-search-focused-file-bubble.png)).
The chat list filters by folder chips, and Contacts sorts with a pull-down menu
([23](screenshots/dark/23-folder-chip-selected-os.png), [17](screenshots/dark/17-contacts-sort-menu.png)).

## Editing a list

Edit turns the chat list into a selection: circles at the left, reorder handles at the right, remove crosses on
the folder chips, and a bottom toolbar (Read All, Archive, Delete) that stays disabled until a chat is chosen
([20](screenshots/dark/20-chat-list-edit-mode-disabled-actions.png)).

## Public site

The public website is a separate surface from the iOS app. [site-tree.md](site-tree.md) maps the homepage header, footer, and the pages those controls open. The marketing pages are white with blue links. Telegram Web is the login wall: a dark card titled "Log in by QR Code", with phone and passkey left unused. Shots live in [screenshots/public/](screenshots/public/).
