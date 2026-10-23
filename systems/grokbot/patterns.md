# Grok Bot patterns

How the components in [components.md](components.md) combine into Grok Bot's screens. Token paths are in
[tokens.json](tokens.json); the captures named here are in [screenshots/](screenshots).

## App shell and navigation

There is no tab bar. Home is one scrolling page on `color.bg.page`: an account avatar (initials on glass) at the
top left, a round glass + at the top right, a three-column grid of pinned bots and groups, then folders that
expand in place into chat rows. The bottom holds a round glass grid button (Connect apps) and a glass search
capsule. Content scrolls under every glass control. See [01-home](screenshots/dark/01-home.png),
[31-folder](screenshots/dark/31-folder.png) and [01-home light](screenshots/light/01-home.png).

Everything else is pushed or presented over it:

| Layer | What sits there | Tokens |
|---|---|---|
| Page | Home, chat threads, search results | `color.bg.page` |
| Pushed page | Bot profile, Routines, Library, Coding, Usage | `color.bg.sheet` |
| Sheet | Settings, Create New Bot, Connect apps, search | `color.bg.sheet`, `radius.sheet`, the page behind dims to `color.bg.scrim` |
| Glass | Nav buttons and title pill, composer, search bar, menus | `color.surface.glass`, `color.surface.menu` |
| Context menu | Long-press preview and actions | `color.bg.scrim` over the page |

A pushed page has the same round back button as a thread ([13-routines](screenshots/dark/13-routines.png)); a
sheet has a round close (x) instead ([19-account-menu](screenshots/dark/19-account-menu.png)).

## Conversation

A thread is bubbles on `color.bg.page` with a floating glass nav: back, a title pill with the bot's avatar
and name, and more. Bot replies sit on the left in `color.surface.bubble` (`color.surface.bubbleDirect` one to
one); the owner's sit on the right in the bot's own colour darkened (`color.surface.ownBubble`). Consecutive
bubbles from one sender stack 8 pt apart with tighter joined corners (`radius.bubbleJoined`). In a group each run
gets a sender label and a small avatar at its bottom left. Replies can hold lists, links with an object icon,
inline code and code blocks with a copy button. Times and system lines ("Messaged Chief of Staff") are centred
in tertiary or secondary text. See [35-tutor-chat](screenshots/dark/35-tutor-chat.png),
[37-own-bubble](screenshots/dark/37-own-bubble.png), [30-group-chat](screenshots/dark/30-group-chat.png) and
[06-chat](screenshots/dark/06-chat.png).

The composer floats at the bottom: + (Photo or Video, Take Photo, Choose File), a glass capsule with the bot's
name as placeholder, a microphone, and a voice pill that becomes a send arrow once there is text
([08-attach-menu](screenshots/dark/08-attach-menu.png), [10-composer-typed](screenshots/dark/10-composer-typed.png)).

## Forms and validation

Forms are grouped cards with small tertiary labels above fields (Name, Title, Appearance, Voice Calls) and
pop-up rows for choices ([17-edit-bot](screenshots/dark/17-edit-bot.png), [18-select-menu](screenshots/dark/18-select-menu.png)).
Validation is a disabled primary action, not an error message: Create stays grey glass until the name has text,
then turns the theme's ink ([03-new-bot](screenshots/dark/03-new-bot.png),
[05-new-bot-typed](screenshots/dark/05-new-bot-typed.png)). Edit Bot's Done is disabled until something changes. No
inline error message appeared.

## Empty, loading and error states

Empty states are one centred line, with a magnifier above it for search ([16-coding](screenshots/dark/16-coding.png),
[28-search-no-results](screenshots/dark/28-search-no-results.png)). Loading is the system spinner, alone in a list
([24-connect-apps-loading](screenshots/dark/24-connect-apps-loading.png), [27-search-loading](screenshots/dark/27-search-loading.png))
or with a label when the wait is long ([14-computer](screenshots/dark/14-computer.png)). No error state was captured:
cutting the network also cuts iPhone Mirroring.

## Destructive actions

Destructive items are red text with a red outline icon inside an ordinary menu or card: Delete in a chat's more
menu, Hide in the long-press menu, Sign Out at the bottom of Settings
([11-chat-more-menu](screenshots/dark/11-chat-more-menu.png), [33-bot-context-menu](screenshots/dark/33-bot-context-menu.png),
[22-settings-bottom](screenshots/dark/22-settings-bottom.png)). None was tapped, so whether Delete asks for
confirmation is not known.

## Feedback

Unread state is a blue dot after a name and a floating "N unread" pill above the list
([01-home](screenshots/dark/01-home.png)). An available update shows as a card at the top of Settings with a blue dot
and the version change ([19-account-menu](screenshots/dark/19-account-menu.png)). Connected accounts carry a green tick
in their chip ([25-connect-apps](screenshots/dark/25-connect-apps.png)). No toast appeared.

## Search and filtering

The bottom search capsule opens a sheet with a close button, the field and a filter menu (All, Messages, Bots,
Group Chats, Files, Routines). Results are rows with a type label at the right (Group Chat, Bot)
([26-search-focus](screenshots/dark/26-search-focus.png), [29-search-filter-menu](screenshots/dark/29-search-filter-menu.png)).
Connect apps has its own search field and filter button ([25-connect-apps](screenshots/dark/25-connect-apps.png)).

## Data display

Settings and bot pages are grouped cards of 50 pt rows: a line icon, the label, a secondary value and a chevron,
with switches for booleans and helper text under the card ([12-bot-profile](screenshots/dark/12-bot-profile.png),
[20-settings-mid](screenshots/dark/20-settings-mid.png)). Lists of things (Library links, routines, connected apps)
are rows inside one card, with two-line rows for a title and a detail
([15-library](screenshots/dark/15-library.png), [13-routines](screenshots/dark/13-routines.png),
[32-connect-apps-add](screenshots/dark/32-connect-apps-add.png)). Usage is a meter track with the percentage under it
([34-usage](screenshots/dark/34-usage.png)).

## Onboarding

Not captured. The account was already signed in, so the first-run tour and first-bot setup did not show.
