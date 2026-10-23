# Substack patterns

How the components in [components.md](components.md) combine into Substack's screens. Token paths are in
[tokens.json](tokens.json); the captures named here are in [screenshots/](screenshots).

## App shell and navigation

Five tabs sit in a floating glass capsule at the bottom: Home, Read, Podcasts, Chat and Activity, with the
selected one on a pill and an orange dot on Chat for unread messages. Each tab screen has a large bold title at
the top left and a glass capsule at the top right holding search and the account avatar; Home shows the Substack
mark in a round glass button instead of a title. Under the title, Read, Podcasts, Chat and Activity have a row of
text tabs with the selected one on a glass pill. Content scrolls under the tab bar and the top controls. See
[02-home](screenshots/dark/02-home-feed-notes-stories-fab-tabbar.png),
[03-read](screenshots/dark/03-read-tabs-featured-card-inbox-unread.png) and
[04-saved light](screenshots/light/04-saved-tab-progress-rows.png).

Everything else is pushed or presented over it:

| Layer | What sits there | Tokens |
|---|---|---|
| Page | Tab screens, the post reader, search, the profile | `color.bg.page` |
| Grouped sheet | Settings and its pushed pages (Payments, Engagement, Appearance) | `color.bg.grouped`, cards in `color.surface.card`, `radius.sheet` |
| Sheet | Post and note options, Display Settings, the notifications pre-prompt | `color.surface.sheet`, `radius.sheet`, the page behind dims to `color.bg.scrim` |
| Glass | Tab bar, nav buttons, top-tab pill, search fields, the floating action bar | `color.surface.glass`, `color.surface.tabBar` |
| Floating button | The orange compose button over Home, the profile and Chat | `color.accent.brandFab`, `size.fab` |

A pushed page has a round glass back button ([15-payments](screenshots/dark/15-payments-empty-state-link-button.png));
the Settings sheet has a round close (x) instead ([14-settings](screenshots/dark/14-settings-sheet-grouped-icons.png)).
In dark the grouped sheet is lighter than its cards, the reverse of iOS's own grouped style.

## Reading

Home is a feed of notes: avatar, name, date and an orange Subscribe link, the note text, then like, comment,
restack and share counts, with hairlines between notes. A row of publication avatars (rounded squares, an orange
dot when there is something new) sits above it ([02-home](screenshots/dark/02-home-feed-notes-stories-fab-tabbar.png)).
Read opens on a featured card, then "Your inbox": rows with the publication, a title, read time and counts, a
square thumbnail, and an orange dot at the leading edge when unread
([03-read](screenshots/dark/03-read-tabs-featured-card-inbox-unread.png)). Saved adds a grey reading-progress bar
and an orange bookmark ([04-saved](screenshots/dark/04-saved-tab-progress-rows.png)).

The reader has a glass back button, the publication's Subscribe pill and a more button. The post opens with an
upper-case kicker, a heavy title, a grey subtitle, the authors' avatars with a Listen pill, and the byline. The body
is serif (`typography.reader`), with the publication's colour on its Subscribe button. A glass bar with like,
comment, restack and share floats above the tab bar
([05-post](screenshots/dark/05-post-reader-serif-subscribe-action-bar.png)). Display Settings, from the options
sheet, picks the article font and text size ([07-display-settings](screenshots/dark/07-display-settings-option-buttons-selected.png)).

## Forms and settings

Settings are grouped cards of 54.5 pt rows: an icon on a rounded tile, the label, and a chevron or a control. Upper-case
section headers sit above cards and helper text below them
([14-settings](screenshots/dark/14-settings-sheet-grouped-icons.png),
[15-payments](screenshots/dark/15-payments-empty-state-link-button.png)). Booleans are blue switches, single
choices are rows with a blue tick ([17-appearance](screenshots/dark/17-appearance-switches-checklists.png)), and a
matrix of choices is a grid of checkboxes under column headers
([16-engagement](screenshots/dark/16-notification-checkbox-grid-destructive-button.png)). No editable form or
validation message was captured.

## Empty, loading and error states

Empty states are a bold line and a tertiary line centred in a card ("No subscriptions yet",
[15-payments](screenshots/dark/15-payments-empty-state-link-button.png)). Search with no results shows the query as
a suggestion row and a "Find people you know" card rather than a message
([10-search-no-results](screenshots/dark/10-search-no-results-find-people.png)). No loading or error state was
captured: cutting the network also cuts iPhone Mirroring.

## Destructive actions

Destructive items are red text with a red outline icon, last in an options sheet after a hairline: Report on a
post, Mute, Block and Report on a note ([06-post-options](screenshots/dark/06-post-options-sheet-destructive.png),
[19-note-options](screenshots/dark/19-note-longpress-options-destructive-group.png)). In Settings, Disable all is red
text alone in its own card ([16-engagement](screenshots/dark/16-notification-checkbox-grid-destructive-button.png)).
None was tapped, so whether they ask for confirmation is not known.

## Feedback

Unread state is an orange dot: on publication avatars, at the leading edge of inbox and chat rows, and on the Chat
tab. A liked post shows a filled red heart with a red count ([04-saved](screenshots/dark/04-saved-tab-progress-rows.png)).
When notifications are off, Chat shows a banner card with a warning icon, Later and Turn on
([18-chat](screenshots/dark/18-chat-list-warning-banner-unread.png)). No toast appeared.

## Search and filtering

Search pushes a page with a glass back button and a glass search field. Focused, it shows topic chips (the selected
one filled with the theme's ink), suggested people and trending searches
([08-search-focused](screenshots/dark/08-search-focused-chips-trending.png)). Typed, the chips turn into related
topics and results list publications and authors with the matched word highlighted in blue
([09-search-typed](screenshots/dark/09-search-typed-highlighted-results.png)). Chat has its own search field above
the list ([18-chat](screenshots/dark/18-chat-list-warning-banner-unread.png)).

## Data display

Podcasts uses horizontal cards whose lower half takes the artwork's colour, with a glass play pill showing the
duration, and square show tiles ([11-podcasts](screenshots/dark/11-podcasts-cards-play-pills.png)). Activity lists
subscribes and notes with a tinted icon circle, the avatar and an orange Subscribe back or an outlined Message button
([12-activity](screenshots/dark/12-activity-feed-primary-secondary-buttons.png)). The profile stacks the name,
handle, bio, a recommendation chip, the subscriber count, Share and Edit, a Creator stats card and tabs over the
owner's notes ([13-profile](screenshots/dark/13-profile-share-edit-tabs-note.png)).

## Onboarding

Partly. The notifications pre-prompt is a sheet with an illustration, a title, two lines of text and an
orange-tinted "Enable notifications" button ([01-notification-preprompt-sheet](screenshots/dark/01-notification-preprompt-sheet.png));
it was dismissed by tapping outside. The account was already signed in, so sign-up did not show.
