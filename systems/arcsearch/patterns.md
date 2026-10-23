# Arc Search patterns

How the components in [components.md](components.md) combine into Arc Search's screens. Token paths are in
[tokens.json](tokens.json); the captures named here are in [screenshots/](screenshots).

## App shell and navigation

Arc Search has no tab bar and no address bar on the page. A web page fills the screen, and a glass toolbar runs
along the bottom (`color.glass.toolbar`): the stack of open tabs at the left, a + capsule for a new search in the
middle (`size.plus`, `size.plusWidth`), and a round chevron at the right that opens the page menu. See
[03-page-bottom-toolbar](screenshots/dark/03-page-bottom-toolbar.png) and
[11-page-youtube-tab light](screenshots/light/11-page-youtube-tab.png).

Everything else opens over the page as a layer. Each is iOS 26 glass or a sheet, never a pushed full-screen page:

| Layer | What sits there | Tokens |
|---|---|---|
| Page | The website, edge to edge | none: the site's own colours |
| Toolbar | Tabs, +, page menu | `color.glass.toolbar`, `color.glass.plus` |
| Launcher | Search field, pinned sites, suggestions | `color.glass.launcher`, `color.glass.searchField` |
| Page menu | Address bar, actions, display options, notice | `color.glass.menu`, `color.glass.panel`, `radius.panel` |
| Find bar | Replaces the toolbar while finding | `color.glass.findField`, `size.findField` |
| Sheet | Settings and its sub-pages over the dimmed page | `color.bg.sheet`, `radius.sheet`, `color.bg.dimmed` behind |
| Second sheet | App Icon over Settings | `color.surface.sheet`, `size.closeButton` |
| Full-screen page | The Archive and its search | `color.bg.page`, `color.surface.card` |
| Menus | Pop-up (a choice), context (long press), edit (Archive) | `color.glass.popup`, `color.destructive.text` |
| Space sheet | A space's tabs over its gradient | `color.space.top`, `color.space.bottom` |

Long-pressing the tab button opens the current space ([17-space-sheet-gradient](screenshots/dark/17-space-sheet-gradient.png)),
a sheet in the space's own colour with its name at the top and a close button. Tapping the tab stack opens the
switcher, overlapping cards with a site chip over each ([04-tab-switcher-cards](screenshots/dark/04-tab-switcher-cards.png)).

## Searching

The + button, and a new launch, raise the launcher: a glass sheet whose search field sits at the top of the
lower half, focused, with a microphone and the Browse for Me glasses inside it
([01-launch-search-focused-pinned](screenshots/dark/01-launch-search-focused-pinned.png)). Pinned and favourite
sites list under it as plain rows with a pin glyph (`size.rowLauncher`), no dividers. Typing turns the rows into
suggestions: a magnifier, the suggestion with the typed part in `color.text.secondary` and the completion in
`color.text.primary`, and a Browse for Me button at the end of each
([02-search-typed-suggestions](screenshots/dark/02-search-typed-suggestions.png)). The launcher's glass takes its
colour from the page under it: brown over the dark Google page, pink over the light YouTube page.

Find on Page swaps the toolbar for the find bar: a round close button, the field with the query and a match
count, and a capsule of previous and next chevrons ([15-find-bar-typed-match](screenshots/dark/15-find-bar-typed-match.png)).
No match shows a 0 ([16-find-bar-no-results](screenshots/dark/16-find-bar-no-results.png)).

## The page menu

The chevron in the toolbar opens one glass sheet that holds every page action
([12-page-menu-address-actions](screenshots/dark/12-page-menu-address-actions.png)):

1. An address bar capsule with back and forward at the left, the host in the middle, copy link and reload at the right (`size.addressBar`).
2. Four square glass buttons with labels under them: Find on Page, Summarize, Pin, Share (`size.tileButton`, `radius.tileButton`).
3. A list panel (`radius.panel`, `size.rowMenu`): Display Options with a disclosure chevron, Translate, Reader Mode, Page Zoom with a minus and plus stepper, Request Desktop Site.
4. Site Settings on its own panel.
5. A notice panel: how many ads and trackers Arc removed, and a second line that offers to restore the page.

Display Options collapses the list panel to one row ([13-page-menu-collapsed](screenshots/dark/13-page-menu-collapsed.png)).

## Settings and forms

Settings is a sheet over the dimmed page ([05-settings-sheet](screenshots/dark/05-settings-sheet.png)): a centred
title with a glass Done capsule, two grey capsule buttons (Downloads, Archive), then inset groups of rows. Each
row is a coloured icon tile, a label and a value, a chevron or a switch (`size.row`, `size.tile`, `color.tile.*`).
Groups sit `space.groupGap` apart and separators are inset to start at the label. In dark the groups are lighter
than the sheet; in light they are darker than it, so the sheet always reads as the background.

Rows push sub-pages with a round glass back button and keep Done
([08-settings-search-engine-checklist](screenshots/dark/08-settings-search-engine-checklist.png),
[09-site-settings-switches](screenshots/dark/09-site-settings-switches.png)). A choice list marks the current row
with an accent tick and ends with an accent text action. A short helper paragraph can sit over a group in
`color.text.secondary`. A row whose value is a short choice opens a glass pop-up menu over it rather than a page
([07-popup-menu-archive-tabs](screenshots/dark/07-popup-menu-archive-tabs.png)). Content scrolled under the nav bar
blurs out behind it ([06-settings-scrolled-header-blur](screenshots/dark/06-settings-scrolled-header-blur.png)).

No form with validation exists in the captured screens.

## The Archive and history

The Archive is the one full-screen page: the iOS grouped background, an Edit capsule and the title at the top, a
round accent confirm button at the top right, then day headers over cards of history rows (favicon, title, URL)
([20-archive-history-list](screenshots/dark/20-archive-history-list.png)). A glass search field floats at the
bottom; focused, it gains a round close button and filters the list in place
([22-archive-search-typed](screenshots/dark/22-archive-search-typed.png)). Edit turns into a capsule that holds a
red Clear All ([21-edit-menu-destructive-item](screenshots/dark/21-edit-menu-destructive-item.png)).

## Destructive actions

Destructive items are red text with a red glyph inside a glass menu or capsule, never a red button: Remove
Favorite in the long-press menu ([19-longpress-favorite-menu](screenshots/dark/19-longpress-favorite-menu.png)),
Clear All in the Archive. Their confirmations were not captured.

## Feedback, empty, loading and error states

- **Empty.** An Archive search with no results leaves a blank page ([23-archive-search-no-results-blank](screenshots/dark/23-archive-search-no-results-blank.png)); a find with no match shows 0. Neither has a message.
- **Loading.** The Google tab behind the launcher was loading in [01](screenshots/dark/01-launch-search-focused-pinned.png); the dots are the page's, not Arc's.
- **Feedback.** The page menu's notice reports the ads and trackers removed. No toast was raised.
- **Error.** Not captured.
