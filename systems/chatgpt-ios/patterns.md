# ChatGPT for iOS patterns

How the components in [components.md](components.md) combine into ChatGPT's iOS screens. Token paths are in
[tokens.json](tokens.json); the captures named here are in [screenshots/](screenshots).

## App shell and navigation

There is no tab bar. A new chat is an empty `color.bg.page` with three glass controls at the top (the sidebar
button, the Chat / Work control, a new-chat button), suggestion rows low on the screen, and the composer at the
bottom ([02](screenshots/dark/02-chat-mode-suggestions-composer.png), [02 light](screenshots/light/02-chat-mode-suggestions-composer.png)).
Work mode drops the new-chat button and puts a model pill in the composer
([15](screenshots/dark/15-work-mode-suggestions-model-pill.png)).

The sidebar slides in from the left and pushes the page aside, which stays visible at the right edge. It holds
the ChatGPT title and a search button, outline-icon nav items 48 pt apart (Your dot, Scheduled, Space, Customize,
Codex, Explore, more when expanded), a rule, the recent chats with an unread dot, See all, and at the bottom an
accent Chat pill and a round briefcase button ([05](screenshots/dark/05-sidebar-nav-recents-unread-dot.png),
[17](screenshots/dark/17-sidebar-expanded-more.png)).

| Layer | What sits there | Tokens |
|---|---|---|
| Page | New chat, threads, sidebar, search, Scheduled | `color.bg.page` |
| Grouped page | Settings, General, Personalization, Usage | `color.bg.grouped`, cards in `color.surface.card` |
| Glass | Round buttons, the Chat / Work control, the composer, the search field, the slider | `color.surface.glass`, `color.surface.composer`, `color.surface.segmentTrack` |
| Menu | Plus menu, chat menu, pop-up selects | `color.surface.menu`, `radius.menuLarge`, `radius.menu` |
| Alert | Error alert over a scrim | `color.surface.dialog`, `color.bg.scrim` |

Settings opens with a round close (x) at the top right ([09](screenshots/dark/09-settings-grouped-popup-values.png));
pages pushed from it have a round back button and a centred title ([11](screenshots/dark/11-general-switches-on-popup-rows.png)).

## Conversation

The owner's message is a right-aligned block in `color.surface.userBubble` with `color.text.onUserBubble`,
22 pt corners and no tail. The reply is not in a bubble: it runs the full text width in `color.text.reply`, with
bold lines, rendered maths in a serif italic and display equations centred, then an action row (copy, share, more).
The thread's date line is centred above it in muted text. See [06](screenshots/dark/06-chat-thread-blue-bubble-math.png),
[08](screenshots/dark/08-find-in-chat-no-results.png) and [06 light](screenshots/light/06-chat-thread-blue-bubble-math.png).

In a thread the top controls are the sidebar button on the left and one glass capsule on the right holding new chat
and more. The composer floats at the bottom as a capsule: +, the placeholder, a microphone and the voice circle.
On a new chat it is a two-row card: the field on top, and +, the speed or model pill, the microphone and the voice or
send circle below ([01](screenshots/dark/01-work-mode-segmented-composer-focused.png), [03](screenshots/dark/03-composer-typed-send.png)).
The plus menu rises from the composer's corner with Camera, Photos, Files, Plugins and the selected tool (Think
harder) in the accent with a tick ([04](screenshots/dark/04-plus-menu-selected-item.png)). In Work mode the model pill
opens an effort slider over a blurred page ([16](screenshots/dark/16-effort-slider-stepped.png)).

## Forms and settings

Settings are iOS grouped cards on `color.bg.grouped`: section headers above, helper text below, 52 pt rows with an
outline icon, the label, and a grey value with a chevron or up-down pop-up arrows. Booleans are green switches.
Pop-up rows open a glass menu with a tick on the current value (Accent color lists the ten options)
([09](screenshots/dark/09-settings-grouped-popup-values.png), [10](screenshots/dark/10-accent-color-popup-menu.png),
[11](screenshots/dark/11-general-switches-on-popup-rows.png)). Free text is a card holding a placeholder (Custom
instructions, [13](screenshots/dark/13-personalization-popups-text-field-empty.png)). No form was submitted, so no
validation message was seen.

## Empty, loading and error states

Search's no-results state is centred: a magnifier on a grey tile, a title, a muted line and an ink New chat pill
([19](screenshots/dark/19-search-no-results-empty-state.png)). Before typing, search shows a magnifier and one prompt
line ([20](screenshots/dark/20-search-focused-empty-prompt.png)). An empty tab is one muted line in the middle of the
page ([22](screenshots/dark/22-scheduled-paused-empty-tab-selected.png)).

Errors come as an alert: a glass card over a scrim with a title, a grey body and two equal glass buttons (Cancel,
Retry). It appeared on its own when Personalization could not load a photo
([12](screenshots/dark/12-error-dialog-cancel-retry.png), [12 light](screenshots/light/12-error-dialog-cancel-retry.png)).
No loading state was captured: the two captures planned for it (18) show the resolved screens.

## Destructive actions

Delete is the last item of the chat's glass menu, red text with a red outline icon, after Share, Pin, Add to
project, Plugins, Uploaded files, Find in chat and Archive ([07](screenshots/dark/07-chat-menu-destructive-glass.png)).
It was not tapped, so its confirmation is not known.

## Feedback

Unread chats carry a system-blue dot in the recents, and the sidebar button carries one while any chat is unread
([05](screenshots/dark/05-sidebar-nav-recents-unread-dot.png), [15](screenshots/dark/15-work-mode-suggestions-model-pill.png)).
In light, a white glass banner (Share Message, a line of the reply and a chevron) slid over the top of the thread
([06 light](screenshots/light/06-chat-thread-blue-bubble-math.png)). No toast was seen.

## Search and filtering

Search puts the field at the bottom, a glass capsule beside a round close button, with filter tabs at the top (a
filter button, then All, Chats, Pages, Image) once there is a query ([20](screenshots/dark/20-search-focused-empty-prompt.png),
[19](screenshots/dark/19-search-no-results-empty-state.png)). Find in chat replaces the top controls with a glass bar
holding the query, a result count, previous, next and close ([08](screenshots/dark/08-find-in-chat-no-results.png)).
Scheduled filters with tabs (Active, Paused, Completed), the selected one on a glass pill
([21](screenshots/dark/21-scheduled-tabs-cards-primary-pill.png)).

## Data display

Lists are rows with no dividers on the page (sidebar, recents, suggestions) or inside grouped cards (settings).
Scheduled shows recommended tasks as cards with an emoji, a title and a three-line description inside a dashed rim,
with an accent New task pill floating at the bottom right ([21](screenshots/dark/21-scheduled-tabs-cards-primary-pill.png),
[21 light](screenshots/light/21-scheduled-tabs-cards-primary-pill.png)). Usage is a card with a thin meter in a
lighter blue, the remaining share at the right and the reset time under it
([14](screenshots/dark/14-usage-progress-bar.png)).

## Onboarding

Not captured. The account was already signed in.
