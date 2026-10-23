# Gemini patterns

How the components in [components.md](components.md) combine into Gemini's screens. Token paths are in
[tokens.json](tokens.json); the captures named here are in [screenshots/](screenshots).

## App shell and navigation

There is no tab bar. Home is a near-empty page on `color.bg.page` (pure black in dark, a warm off-white in
light) with a glow rising from the bottom edge (`color.bg.glow`). Three glass circles float at the top: the
menu button at the left, new chat and the account avatar at the right, and between them the title, "Gemini"
followed by the model name in secondary text and a chevron that opens the model picker. The greeting sits in
the middle in `typography.display`; the Chat / Task toggle and the composer float at the bottom. See
[04-home dark](screenshots/dark/04-home-greeting-chat-task-toggle-composer.png) and
[04-home light](screenshots/light/04-home-greeting-chat-task-toggle-composer.png).

The menu button opens a full-screen sidebar on the page colour: Gemini and round search and close buttons,
the main destinations (New chat in a `color.surface.selected` capsule, Library, Images, Scheduled, Students,
More), a Notebooks section, recent chats, and the account row with its ringed avatar and a settings gear. See
[09-sidebar](screenshots/dark/09-sidebar-nav-notebooks-account.png).

| Layer | What sits there | Tokens |
|---|---|---|
| Page | Home, threads, the sidebar, search, Scheduled, Students, Images | `color.bg.page`, `color.bg.glow` |
| Sheet | Settings, Usage limits, Memory, Voice | `color.bg.sheet`, `radius.sheet`, a grabber, the page behind dims to `color.bg.scrim` |
| Tinted sheet | The account sheet | `color.bg.sheetAccount`, with `color.surface.rowCard` capsules |
| Glass sheet | The + sheet, the Create images intro | `color.surface.sheetPlus` |
| Glass | Nav circles, the composer, menus, the search field | `color.surface.glass`, `color.surface.composer`, `color.surface.menu` |

Pages inside a sheet use a round back button and a centred title ([14-memory](screenshots/dark/14-memory-switch-on-tonal-button-empty.png),
[15-voice](screenshots/dark/15-voice-settings-switch-on.png)); the sheet's root has a round close button and a
large title ([12-settings](screenshots/dark/12-settings-sheet-grouped.png)).

## Modes

The Chat / Task toggle changes more than the input. In Task the glow and the voice button turn purple
(`color.bg.glowTask`, `color.button.voice.bgTask`), the greeting becomes a two-line question, the placeholder
reads "Describe task", and three suggestion rows with line icons appear above the toggle. See
[08-task](screenshots/dark/08-task-mode-suggestions-purple.png) and
[08-task light](screenshots/light/08-task-mode-suggestions-purple.png).

## Conversation

Gemini's replies are plain text on the page in `typography.body`, full width, with an action row under each
(share, like, dislike, more) and no avatar. The owner's messages sit at the right in a `color.surface.container`
bubble with large corners (`radius.bubble`). Generated media appear inline as rounded cards with a play button
and a share button over them. A disclaimer line in `color.text.tertiary` ends the thread above the composer.
See [10-thread](screenshots/dark/10-chat-thread-media-bubble-actions.png) and
[10-thread light](screenshots/light/10-chat-thread-media-bubble-actions.png).

The composer floats over the glow: + (the + sheet), the placeholder, a microphone, and a round voice button.
Once text is typed it widens from `size.composer.width` to `size.composer.widthTyped` and the voice button
becomes a blue send arrow ([05-typed](screenshots/dark/05-composer-typed-send.png)).

## Forms and settings

Settings are grouped cards under small section headers: each row has a line icon, a title, and a chevron, a
value with up-down chevrons (a pop-up select), or a switch. Rows with a subtitle run two lines in
`color.text.secondary`. Gemini's own pages use a Material switch and a Material filled button
(`color.accent.primary`); pages built on iOS controls use the system switch (`color.switch.onSystem`). See
[12-settings](screenshots/dark/12-settings-sheet-grouped.png), [14-memory](screenshots/dark/14-memory-switch-on-tonal-button-empty.png),
[15-voice](screenshots/dark/15-voice-settings-switch-on.png) and [16-theme](screenshots/dark/16-theme-popup-menu-not-changed.png).

No form with a validation error was captured.

## Empty and loading states

Empty states are centred text: a magnifier, a medium title and a secondary line for search
([18-no-results](screenshots/dark/18-search-no-results-empty.png)); one secondary line for Memory
([14-memory](screenshots/dark/14-memory-switch-on-tonal-button-empty.png)). The empty study-notebook card on
Students explains the feature and offers a "+ New notebook" text button
([19-students](screenshots/dark/19-students-cards-empty-notebook-card.png)). No loading or streaming state was
captured, since no prompt was sent.

## Destructive actions

Delete is the last item in the chat's more menu, in red text with a red outline icon and no fill
([11-chat-menu](screenshots/dark/11-chat-menu-destructive.png)). It was not tapped, so any confirmation is
unseen.

## Feedback

Usage limits show two container cards with a percentage and a progress track
([13-usage](screenshots/dark/13-usage-limits-badge-progress.png)). The dot after the model name flags a new
model. The system's notification permission alert appears after onboarding
([03-alert](screenshots/dark/03-system-notification-permission-alert.png)). No toast appeared.

## Search and filtering

Search opens on the page with a "Recent" list of past chats (bubble icon, title, age) and the field at the
bottom: a glass capsule with a magnifier and a separate round close button. Typing adds a clear button; no
match shows the empty state. See [17-search](screenshots/dark/17-search-focused-recent-list.png) and
[18-no-results](screenshots/dark/18-search-no-results-empty.png). Scheduled has a filter button at the top
right; its menu was not opened.

## Data display

Cards carry the content pages: suggestion cards stacked 12 pt apart (Scheduled,
[20-scheduled](screenshots/dark/20-scheduled-suggestion-cards.png)), image cards in horizontal scrollers with
captions (Students) or labels over the image (image templates,
[22-images](screenshots/dark/22-images-template-grid.png)). There are no tables.

## Onboarding

Onboarding is two dark screens on the glow: a Google account sheet with "Continue as ..." under a large
centred welcome ([01-sign-in](screenshots/dark/01-onboarding-sign-in-gate.png)), then the terms with three
icon rows, a fine-print paragraph with dotted links and a full-width Get started button
([02-terms](screenshots/dark/02-onboarding-get-started-terms.png)). Feature intros use a glass sheet with a
collage, a title, three icon rows and a Try it button
([21-images-intro](screenshots/dark/21-images-intro-sheet-glass.png)).
