# GitHub Mobile patterns

How the components in [components.md](components.md) combine into GitHub Mobile's screens. Token paths are in
[tokens.json](tokens.json); the captures named here are in [screenshots/](screenshots).

## App shell and navigation

A floating glass tab bar holds four tabs: Home, Inbox, Explore and Copilot. The selected tab sits in its own
darker (dark) or greyer (light) pill and turns blue (`color.surface.tabSelected`, `color.text.tabSelected`). Every
tab root opens with a 34 pt bold large title (Inbox, Explore, Copilot) or, on Home, with the account avatar at the
top left and a glass capsule of + and search at the top right. Content scrolls under the tab bar and under the
blurred header ([02-home-scrolled](screenshots/dark/02-home-scrolled-blur-header-fab.png)). See
[01-home](screenshots/dark/01-home-my-work-favorites-empty-shortcuts.png),
[03-inbox](screenshots/dark/03-inbox-chips-banner-unread-rows.png) and
[01-home light](screenshots/light/01-home-my-work-favorites-empty-shortcuts.png).

Pushed pages keep the tab bar. Their nav bar is a round glass back button, a centred title (an issue or PR page
puts the repository under it) and a glass capsule of actions ([11-repo-page](screenshots/dark/11-repo-page-archived-banner-star-button-rows.png),
[17-pr-page](screenshots/dark/17-pr-page-draft-branch-pills-diffstat.png)).

Pages come in two backgrounds:

| Layer | What sits there | Tokens |
|---|---|---|
| Page with cards | Home, Explore, Copilot, Settings, Appearance, the Filters sheet | `color.bg.page` under `color.surface.card` |
| Full-bleed list | Inbox, search scopes, Issues, Pull Requests, repository, issue and PR pages | `color.bg.list` (the card colour), rows divided by `color.border.divider` |
| System grouped table | Code Options | `color.bg.grouped` under `color.surface.card` |
| Glass | Tab bar, nav buttons, search field, filter chips, menus, the dark New Session button | `color.surface.glass`, `color.surface.menu` |
| Sheet | Inbox Filters | `color.bg.page` with a round confirm button |

On an issue or PR page the header (repository line, title, badges, author) sits on `color.bg.list`, and the
sections under it (Changes, Status) drop to `color.bg.page` with full-width rows
([17-pr-page](screenshots/dark/17-pr-page-draft-branch-pills-diffstat.png)).

## Lists and data display

Grouped cards hold rows that lead with a coloured 32 pt icon tile, then a title, an optional count and a chevron
(57 pt rows: [01-home](screenshots/dark/01-home-my-work-favorites-empty-shortcuts.png),
[11-repo-page](screenshots/dark/11-repo-page-archived-banner-star-button-rows.png),
[20-profile](screenshots/dark/20-profile-status-achievements-rows.png)). Each kind of object keeps its tile colour
everywhere: Issues green, Pull Requests blue, Discussions purple, Starred yellow, Organizations orange. Settings
rows have no tile: a label, a grey value and a chevron in 53 pt rows
([21-settings](screenshots/dark/21-settings-grouped-values-new-badge.png)).

Lists of work are full-bleed. An Inbox row is a state icon and an unread dot in a left column, the repository and
number in grey, the title in up to three lines, a grey preview line, the age and a blue unread count at the right
([03-inbox](screenshots/dark/03-inbox-chips-banner-unread-rows.png)). Issue and PR rows put the state icon at the
left, labels and review chips under the title, and the age at the right
([13-issues](screenshots/dark/13-issues-list-filter-chips-labels.png),
[16-pull-requests](screenshots/dark/16-pull-requests-list-draft-icons.png)). A draft PR's icon is grey; an open
one green.

An issue or PR page stacks the repository line, a 22 pt bold title, state badges and branch pills, then the
comment, then grouped sections ([15-issue-page](screenshots/dark/15-issue-page-open-locked-badges-comment.png),
[17-pr-page](screenshots/dark/17-pr-page-draft-branch-pills-diffstat.png)). Files Changed is a diff with a line
number gutter, red and green line fills and syntax colours
([18-files-changed](screenshots/dark/18-files-changed-diff-view.png)).

## Forms and validation

Settings is grouped cards with values and chevrons; booleans are switches with the blue accent for on
([21-settings](screenshots/dark/21-settings-grouped-values-new-badge.png),
[22-code-options](screenshots/dark/22-code-options-preview-switches-on-off.png)). Appearance is a choice list with
a filled blue tick ([23-appearance](screenshots/dark/23-appearance-choice-list.png)). Code Options previews its
effect live in a code card above the switches. No text form, validation message or error was captured: the
comment composer was not opened.

## Empty, loading and error states

Empty states are a centred bold line, with a grey explanation under it when there is one
([19-search-no-repositories](screenshots/dark/19-search-no-repositories-empty.png),
[07-search-focused](screenshots/dark/07-search-focused-empty-qualifier-chips.png)). On Home an empty section keeps
its card and fills it with a sentence and a neutral button (Add Favorites, Get started)
([01-home](screenshots/dark/01-home-my-work-favorites-empty-shortcuts.png)). Loading and error states were not
captured: [09](screenshots/dark/09-repo-results-loading-spinner.png) shows the results already loaded.

## Destructive actions

Not captured. No destructive item appeared in the menus that were opened (the repository menu holds Share via,
Report and Add to favorites: [12-repo-overflow-menu](screenshots/dark/12-repo-overflow-menu.png)).

## Feedback

Unread notifications carry a blue dot and a blue count ([03-inbox](screenshots/dark/03-inbox-chips-banner-unread-rows.png)).
A prompt card at the top of Inbox asks to set up notifications, with a dismiss button and a Configure button. A
setting that needs attention gets a blue New badge and the value Setup Needed
([21-settings](screenshots/dark/21-settings-grouped-values-new-badge.png)). An archived repository shows a yellow
banner under the nav bar ([11-repo-page](screenshots/dark/11-repo-page-archived-banner-star-button-rows.png)).
Agent sessions show Completed or Failed chips with a green tick or red warning icon
([06-copilot](screenshots/dark/06-copilot-promo-card-status-badges.png)). No toast appeared.

## Search and filtering

Search opens from the glass capsule on Home: a glass search field at the top, a close button beside it, and a
glass bar of qualifiers (org, user, repo, path) where the tab bar was
([07-search-focused](screenshots/dark/07-search-focused-empty-qualifier-chips.png)). Typing turns the page into scope
rows (Code, Repositories, Issues, Pull Requests, People, Organizations, Jump to)
([08-search-typed](screenshots/dark/08-search-typed-scope-rows.png)). Lists filter with glass chips under the title;
a chip with a chevron opens a pop-up menu with a tick on the current value
([13-issues](screenshots/dark/13-issues-list-filter-chips-labels.png),
[14-state-filter-popup-menu](screenshots/dark/14-state-filter-popup-menu.png)), and Inbox's first chip opens a
Filters sheet ([04-inbox-filters](screenshots/dark/04-inbox-filters-sheet-checked.png)).

## Onboarding

Not captured. The account was already signed in.
