# Claude for iOS patterns

How the components in [components.md](components.md) combine into the app's screens. Token paths are in
[tokens.json](tokens.json); the captures named here are in [screenshots/](screenshots).

## App shell and navigation

There is no tab bar. The app opens on a new chat: a round glass sidebar button at the top left, a round glass
incognito button at the top right, the spark and a serif greeting in the middle, and the composer at the bottom
([01-new-chat-greeting-composer](screenshots/dark/01-new-chat-greeting-composer.png),
[01 light](screenshots/light/01-new-chat-greeting-composer.png)). The sidebar slides in from the left over the
page and is the only top-level navigation: Chats, Projects, Code, Artifacts, Dispatch and Cowork, then Pinned and
Recents chats, the account avatar at the bottom left and a New chat pill
([06-sidebar-nav-pinned-recents](screenshots/dark/06-sidebar-nav-pinned-recents.png),
[23-sidebar-selected-row](screenshots/dark/23-sidebar-selected-row.png)).

Everything else sits in one of these layers:

| Layer | What sits there | Tokens |
|---|---|---|
| Chat page | New chat, threads | `color.bg.page` |
| List page | Chats, Projects, Artifacts, Code, Time & focus | `color.bg.list` (darker than the chat page in dark only) |
| Sidebar | Navigation, pinned and recent chats | `color.bg.sidebar` |
| Bottom sheet | Select model, Effort, Add to Chat, tool-step timeline, the gift promo, Settings | `color.bg.sheet`, `radius.sheet`, the page behind dims to `color.bg.scrim` |
| Glass | Nav buttons, the composer, the search bar, menus, the Add device pill | `color.surface.navGlass`, `color.surface.glass`, `color.surface.menu` |
| Context menu | Long press on a message: the message lifts over the dimmed thread | `color.surface.menu` |

Settings is a full-height sheet with a round close (x) at the top left; its pages push inside it with a round
back button ([13-settings-sheet-grouped](screenshots/dark/13-settings-sheet-grouped.png),
[15-capabilities-switches-on-disabled](screenshots/dark/15-capabilities-switches-on-disabled.png)). A scrolled
sheet blurs the content passing under its title
([16-capabilities-scrolled-blur-header](screenshots/dark/16-capabilities-scrolled-blur-header.png)).

## Conversation

The owner's messages sit in a grey bubble on the right (`color.surface.userBubble`). Claude's replies have no
bubble: a tool-step row ("Checking whether ...") that opens a timeline sheet, then serif paragraphs on the page
(`typography.response`), a row of outline action icons (copy, share, read aloud, thumbs, retry) and a disclaimer
in small tertiary text ([07-chat-thread-user-bubble-response-actions](screenshots/dark/07-chat-thread-user-bubble-response-actions.png),
[10-tool-steps-summary-sheet](screenshots/dark/10-tool-steps-summary-sheet.png)). While the thread scrolls, the
first message's action icons show in the top bar beside the sidebar button.

The composer is one glass block of two rows: the input line, then +, the model and effort pill, a microphone and
the black or white Talk pill. Typing swaps Talk for the round orange send button
([02-composer-typed-send-enabled](screenshots/dark/02-composer-typed-send-enabled.png)). The model pill opens the
Select model sheet, which pushes to Effort
([03-model-picker-sheet](screenshots/dark/03-model-picker-sheet.png), [04-effort-sheet-badges](screenshots/dark/04-effort-sheet-badges.png));
+ opens Add to Chat with photos, files, a project and switches for tools
([05-add-to-chat-sheet-switch](screenshots/dark/05-add-to-chat-sheet-switch.png)).

## Forms and validation

Settings are grouped cards of rows: an outline icon, the label, a tertiary value or chevron, or a switch. A
setting with an explanation puts a tertiary subtitle under its title
([15-capabilities-switches-on-disabled](screenshots/dark/15-capabilities-switches-on-disabled.png)). A setting
that another one requires stays on but locked: dimmed title and switch, grey thumb in dark. Time & focus uses
rimmed pop-up selects and round day toggles
([14-time-focus-selects-day-toggles](screenshots/dark/14-time-focus-selects-day-toggles.png)). Validation was not
seen: no form was submitted, and the composer simply has no send button until there is text.

## Empty, loading and error states

Empty states are an outline icon in a grey circle over a centred tertiary line, with an explanation under it when
there is a way out ([19-archived-empty-state-accent-icon](screenshots/dark/19-archived-empty-state-accent-icon.png),
[21-code-empty-sessions-secondary-pill](screenshots/dark/21-code-empty-sessions-secondary-pill.png)). Loading and
streaming were not captured: no message was sent. No error state was captured; cutting the network also ends
iPhone Mirroring.

## Destructive actions

Delete is red text with a red icon at the bottom of the chat's more menu, below a divider
([08-chat-menu-destructive](screenshots/dark/08-chat-menu-destructive.png)). It was not tapped, so the
confirmation it leads to is not captured.

## Feedback

Selection is blue: a tick on the chosen model and effort, a ring and blue label on the chosen Appearance tile, blue
switches ([03-model-picker-sheet](screenshots/dark/03-model-picker-sheet.png),
[24-settings-app-appearance-cards](screenshots/dark/24-settings-app-appearance-cards.png)). Cost is amber: the
Max effort carries a "5.5x or more usage" badge ([04-effort-sheet-badges](screenshots/dark/04-effort-sheet-badges.png)).
An active list filter fills its glass button orange
([19-archived-empty-state-accent-icon](screenshots/dark/19-archived-empty-state-accent-icon.png)). No toast
appeared.

## Search and filtering

Lists carry a floating glass search capsule at the bottom (Chats, Artifacts) or a round search button (Projects,
Code). Typing turns the capsule into a field with a clear button and a round close button beside it
([11-chats-list-search-new-chat](screenshots/dark/11-chats-list-search-new-chat.png),
[12-chats-search-typed-results](screenshots/dark/12-chats-search-typed-results.png)). A filter button at the top
right opens a menu (Yours, Archived) on Projects, Artifacts and Code.

## Data display

Lists of chats and projects are icon rows with a title and a subtitle and no dividers
([11-chats-list-search-new-chat](screenshots/dark/11-chats-list-search-new-chat.png),
[18-projects-list-new-project-pill](screenshots/dark/18-projects-list-new-project-pill.png)). Artifacts are cards
drawn as a rim on the page, with a thumbnail, a sharing line and a date
([20-artifacts-list-cards](screenshots/dark/20-artifacts-list-cards.png)). Usage is cards of thin blue meters with
the share used at the right and the reset time under each
([17-usage-progress-meters-switch-off](screenshots/dark/17-usage-progress-meters-switch-off.png)).

## Promotion

The gift sheet is the one place with an illustration: a hand-drawn gift over a serif display title, a short body,
a ticket counter and a full-width primary Share button
([22-gift-sheet-illustration-primary](screenshots/dark/22-gift-sheet-illustration-primary.png)).

## Onboarding

Not captured. The account was already signed in.
