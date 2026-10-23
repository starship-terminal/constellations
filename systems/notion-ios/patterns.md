# Notion patterns

How the components in [components.md](components.md) combine into Notion's iOS screens. Token paths are in
[tokens.json](tokens.json); the captures named here are in [screenshots/](screenshots).

## App shell and navigation

Notion for iOS has no bottom tab bar. Four tabs sit across the top beside the account button: Home (the sidebar
tree), Chats (Notion AI), Meetings and Inbox. Unselected tabs are glass circles holding an icon; the selected one
widens into a pill with its label (`size.tab`, `color.surface.tab`, `color.surface.tabSelected`). The bottom is
floating glass: a round search button, an 'Ask AI' pill and a round compose button. Content scrolls under both.
See [01-home-sidebar-tree](screenshots/dark/01-home-sidebar-tree.png), [02-chats-tab-list](screenshots/dark/02-chats-tab-list.png),
[04-inbox-tab](screenshots/dark/04-inbox-tab.png) and [01 light](screenshots/light/01-home-sidebar-tree.png).

Two greys carry the structure. The navigation screens (Home, Chats, Inbox, Settings) sit on `color.bg.sidebar`; the
content they open (a page, search, the AI chat) sits on the darker, or in light the whiter, `color.bg.page`.

| Layer | What sits there | Tokens |
|---|---|---|
| Navigation | Home tree, Chats, Meetings, Inbox, Settings | `color.bg.sidebar` |
| Content | Pages, search results, the AI chat | `color.bg.page` |
| Pushed card | The AI chat opens as a card over the dimmed tab behind it | `color.bg.page`, `color.bg.scrim` |
| Small sheet | Search Filters, Sort | `color.bg.sheet`, `radius.sheet`, `color.bg.scrim` |
| Large sheet | Page and row Actions, Views, filter properties, Theme | `color.bg.sheetGrouped`, `color.surface.card` |
| Glass | Tabs, bottom bar, nav buttons, composer, menus | `color.surface.glass`, `color.surface.composer`, `color.surface.menu` |

A page has no bar either: back, share and more float at the top, and a compact title with 'Private' under it
appears once the page scrolls ([17-page-headings-table](screenshots/dark/17-page-headings-table.png),
[18-page-scrolled-compact-header-table](screenshots/dark/18-page-scrolled-compact-header-table.png)). On a page the
bottom bar's search button becomes a menu button. A page with a cover puts the buttons on solid circles over the
image ([20-database-cover-inline-view](screenshots/dark/20-database-cover-inline-view.png)).

## Documents

A page is text on the canvas at a 27 pt margin, wider than the sidebar's 21 pt: a bold title (`typography.pageTitle`),
bold headings (`heading1`, `heading2`), body on a 24 pt line, inline code as red monospace on a tinted chip, and
tables with a tinted header row and hairline cells ([17-page-headings-table](screenshots/dark/17-page-headings-table.png),
[18-page-scrolled-compact-header-table](screenshots/dark/18-page-scrolled-compact-header-table.png)). The Actions sheet
lets the owner switch the page's font between Default, Serif and Mono ([19-page-actions-sheet](screenshots/dark/19-page-actions-sheet.png)).

## Conversation (Notion AI)

The AI chat opens as a card over the tab behind it. The AI's face sits at the top centre over a glass title pill,
with history and new-chat buttons in the corners. Only the owner's messages are bubbles (`color.surface.bubble`,
right-aligned, grey in both themes). The AI answers in plain text on the canvas, prefixed by a collapsible 'N steps'
line, followed by an outlined card listing the pages it touched and copy, thumbs and retry icons
([16-ai-chat-thread-bubbles](screenshots/dark/16-ai-chat-thread-bubbles.png)). Chat text uses `color.text.prose`, a
softer ink than the sidebar's `color.text.primary` in dark.

The composer is a capsule with + and a mic when idle ([14-ai-composer-unfocused](screenshots/dark/14-ai-composer-unfocused.png)).
Focused, it grows into a two-row glass card with the model name ('Auto') and a shield for access; typing turns the mic
into a blue send button ([11-ai-chat-empty-composer](screenshots/dark/11-ai-chat-empty-composer.png),
[12-ai-composer-typed-send-enabled](screenshots/dark/12-ai-composer-typed-send-enabled.png)). Tapping the model name
opens a glass menu of models with a tick on the current one ([13-model-picker-menu](screenshots/dark/13-model-picker-menu.png)).

## Forms and settings

Settings is one long scrolling list on `color.bg.sidebar`, without grouped cards: a bold section title, then rows of a
title, a grey two-line subtitle and a control at the right, with inset hairlines between them. Controls are switches,
outlined selects with a chevron and outlined buttons (Connect, Change password), all 28 pt tall with 4 pt corners
([25-settings-notifications-switches-off](screenshots/dark/25-settings-notifications-switches-off.png),
[26-settings-select-and-secondary-button](screenshots/dark/26-settings-select-and-secondary-button.png),
[28-settings-preferences-theme-select](screenshots/dark/28-settings-preferences-theme-select.png)). A select opens a
list under itself with a tick ([27-select-dropdown-open](screenshots/dark/27-select-dropdown-open.png)); the Theme
select opens a sheet with Done instead ([29-theme-choice-sheet](screenshots/dark/29-theme-choice-sheet.png)). No form
with a validation error was reached.

## Empty, loading and error states

The one empty state is search with no matches: a page outline, 'No pages found' and a hint about deleted pages, centred
in secondary grey ([08-search-no-results-empty](screenshots/dark/08-search-no-results-empty.png)). Loading and error
states were not captured: every screen loaded before a capture could run, and cutting the network ends iPhone Mirroring.

## Destructive actions

Move to Bin is the last row of an Actions card, in red text with a red bin icon, never a red fill
([19-page-actions-sheet](screenshots/dark/19-page-actions-sheet.png), [23-row-longpress-actions](screenshots/dark/23-row-longpress-actions.png)).
It was not tapped, so its confirmation is not known.

## Feedback

Unread activity is a dot on the account button ([01-home-sidebar-tree](screenshots/dark/01-home-sidebar-tree.png)).
Inbox lists what happened (access requests, imports, comments) with the status line under each ('The request was
approved') ([04-inbox-tab](screenshots/dark/04-inbox-tab.png)). An active filter or sort shows as blue: the filter icon
on a database, and 'Sort' and the filtered property in the filter sheet
([20-database-cover-inline-view](screenshots/dark/20-database-cover-inline-view.png),
[22-filter-sheet-properties](screenshots/dark/22-filter-sheet-properties.png)). No toast appeared.

## Search and filtering

The bottom search button turns the screen into search: an 'Ask AI anything' row at the top, recent pages grouped by
day, and the glass search bar at the bottom with a filter button and a round close button
([06-search-focused-recents](screenshots/dark/06-search-focused-recents.png), [07-search-typed-results](screenshots/dark/07-search-typed-results.png)).
Results are two-line rows: icon, title, location, and an excerpt with the matched words in bold. Filters open as a small
sheet (Sort, Title only, Created by), and Sort pushes a radio list inside the same sheet with a round back button
([09-search-filters-sheet-switch-off](screenshots/dark/09-search-filters-sheet-switch-off.png),
[10-sort-radio-list](screenshots/dark/10-sort-radio-list.png)). Inbox has its own filter menu
([05-inbox-filter-menu](screenshots/dark/05-inbox-filter-menu.png)).

## Data display

An inline database sits in a rimmed frame with a view chip, search, filter, properties and a blue + split button, then
rows grouped by colour: each group's rows sit on its own tinted fill (`color.group.*`), 40 pt tall with 2 pt gaps
([20-database-cover-inline-view](screenshots/dark/20-database-cover-inline-view.png), [20 light](screenshots/light/20-database-cover-inline-view.png)).
Its Views sheet lists views and offers New view and New data source ([21-views-sheet](screenshots/dark/21-views-sheet.png)).
A long press on a row opens the row's Actions sheet, ending with who last edited it and a word count
([23-row-longpress-actions](screenshots/dark/23-row-longpress-actions.png)). Board, calendar and gallery views were not
captured: the database has only a list view.

## Onboarding

Not captured. The account was already signed in.
