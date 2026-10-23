# Cursor for iOS patterns

How the components in [components.md](components.md) combine into Cursor's iOS screens. Token paths are in
[tokens.json](tokens.json); the captures named here are in [screenshots/](screenshots).

## App shell and navigation

There is no tab bar. Inbox is the root, on `color.bg.page`: the account avatar in a glass circle at the top
left, search and a folder-plus (Add Workspace) at the top right, a large title, a two-by-two grid of tiles (All
Agents, Needs Attention, Working, In Review), then Projects and Workspaces as single-line rows. A glass composer
capsule floats at the bottom of Inbox, every agent list and every thread, and the content scrolls under it. See
[02-inbox](screenshots/dark/02-inbox-tiles-projects-workspaces.png) and its
[light twin](screenshots/light/02-inbox-tiles-projects-workspaces.png).

Everything else is pushed or presented over it:

| Layer | What sits there | Tokens |
|---|---|---|
| Page | Inbox, agent lists, repo lists, the agent thread | `color.bg.page` |
| Glass | Nav circles, the composer, the '7 PRs' capsule, search fields, menus | `color.surface.glass`, `color.surface.glassField`, `color.surface.menu` |
| Full-height sheet | Customize, Search, Profile, Add Workspace, Changes | `color.bg.sheet` (Changes: `color.bg.sheetGrouped`), `radius.sheet`; a grey strip of the dimmed page shows above it |
| Half-height sheet | Model, Context, agent details, Pull Requests | `color.bg.sheet`, `radius.sheet`, inset from the screen edges, the page behind dims to `color.bg.scrim` |
| Pop-up and pull-down menus | Group by, the thread's more menu | `color.surface.popup`, `color.surface.menu`, `radius.menu` |

A pushed list has a round glass back button ([01-repo-agents-list](screenshots/dark/01-repo-agents-list-composer.png),
[03-all-agents](screenshots/dark/03-all-agents-grouped-status-dots.png)); a sheet has a grabber and a round close
(x) instead ([04-customize](screenshots/dark/04-customize-sheet-switches-popups.png)).

## Agent lists

Agents are two-line rows grouped under collapsible secondary headers (Pinned, Needs Attention, Open PR, Read).
A blue dot marks an unread agent and a grey one a read agent. The second line holds the branch state with its
icon (Merged in violet, Draft in grey), a diffstat in green and pink-red, and the repo in tertiary, separated by
middle dots. See [03-all-agents](screenshots/dark/03-all-agents-grouped-status-dots.png) and
[01-repo-agents-list](screenshots/dark/01-repo-agents-list-composer.png). The filter button opens Customize.

## Conversation

An agent thread has no bubbles: replies are plain `typography.body` text on the page, with numbered lists in
secondary, semibold runs, and inline code on a `color.surface.code` chip. A reply that changed files ends
in a Changes card listing each file with its diffstat; tapping it opens the Changes sheet, where each file is a
disclosure row that expands into its diff. A glass '7 PRs' capsule floats above the composer and opens the Pull
Requests sheet. See [06-agent-thread](screenshots/dark/06-agent-thread-changes-card-diffstat.png),
[07-changes-sheet](screenshots/dark/07-changes-sheet-disclosure-empty-diff.png) and
[19-pull-requests](screenshots/light/19-pull-requests-sheet-segmented.png) (light only).

The composer reads 'Plan, ask, build...' on lists and 'Follow up...' in a thread. Typing grows it into a panel
with a grabber, the text, and a bottom bar: +, the model picker ('Claude Opus 5.5 1M High'), a microphone and a
round send button in the theme's inverse. See [08-composer](screenshots/dark/08-composer-expanded-typed-model-send.png).
The + opens the Context sheet (photo access, Plan or Draft mode); the model name opens the Model sheet.

## Forms and validation

There are no forms beyond the composer and search fields. Customize is a settings sheet: rows with a pop-up
select (Group by), rows that push a value (Repo, Status, Git, Source), and switches. Nothing validates; the send
button stays a plain inverse circle. See [04-customize](screenshots/dark/04-customize-sheet-switches-popups.png)
and [05-group-by](screenshots/dark/05-group-by-popup-menu.png).

## Empty, loading and error states

Empty states are centred secondary text: a title and a sentence in Search
([14-search-no-matches](screenshots/dark/14-search-no-matches-empty.png)), one line in the Model sheet
([10-model-search-no-match](screenshots/dark/10-model-search-no-match.png)). An expanded file row with no diff
shows 'Diff not available' in an inset band ([07](screenshots/dark/07-changes-sheet-disclosure-empty-diff.png)).
Loading and errors were not captured: Working held no agents, and starting one was out of scope.

## Destructive actions

Archive is the only destructive action seen. It sits in the thread's more menu, drawn like every other item:
no red, no separate group colour ([11-agent-menu](screenshots/dark/11-agent-menu-pulldown.png)). Sign out on the
profile is an ordinary row ([20-profile-bottom](screenshots/light/20-profile-bottom-streak-heatmap-support.png)).
Neither was tapped, so any confirmation is Not captured.

## Feedback

State is shown in place rather than with toasts: unread dots, tile counts, the branch state and diffstat on each
row, the 'N PRs' capsule. The Context sheet asks for photo access with a grey banner card and a Continue capsule
([18-context](screenshots/dark/18-context-sheet-mode-options.png)).

## Search and filtering

Search is a full-height sheet: a glass search field with a blue caret, a scrolling row of chips (the selected one
in a grey capsule, the rest plain text), then agent rows ([13-search](screenshots/dark/13-search-sheet-focused-chips-rows.png)).
Typed, the field gains a clear button ([14](screenshots/dark/14-search-no-matches-empty.png)). The Model sheet
has its own search with a round cancel beside it ([09](screenshots/dark/09-model-sheet-search-field.png),
[10](screenshots/dark/10-model-search-no-match.png)). Lists filter through Customize's Show rows.

## Data display

The profile sheet holds the account (initial avatar, name, handle, company and join date), then stat pairs
(label in secondary, big number in `typography.statValue`) over bar charts in `color.chart.bar` with a monospace
axis, then the current and longest streak and a year heatmap in four orange steps
(`core.color.orange`), then Support and More rows and the version in monospace capitals. See
[15-profile](screenshots/dark/15-profile-sheet-bar-charts.png), [16-profile-scrolled](screenshots/dark/16-profile-scrolled-two-charts-stats.png)
and [20-profile-bottom](screenshots/light/20-profile-bottom-streak-heatmap-support.png) (light only).

## Onboarding

Not captured: the account was already signed in.
