# ResearchRabbit patterns

How ResearchRabbit's components work together on its recurring jobs, written from the
2026-10-04 and 2026-10-17 captures. Each pattern says when the product uses it, which
components it combines (they link to [components.md](components.md)), how it is laid out,
and the screenshots that show it. Where the capture could not reach part of a pattern, the
pattern says so instead of guessing what the product would do.

| Pattern | Seen | Main screens |
|---|---|---|
| [App shell and navigation](#app-shell-and-navigation) | Captured | [home-light-default](screenshots/home-light-default.png), [search-split-light-default](screenshots/search-split-light-default.png) |
| [Forms and validation](#forms-and-validation) | Form captured; no validation error reached | [account-light-edit-profile-dialog](screenshots/account-light-edit-profile-dialog.png) |
| [Empty, loading and error states](#empty-loading-and-error-states) | Empty and loading captured; no error reached | [library-reading-light-empty](screenshots/library-reading-light-empty.png), [search-list-light-loading](screenshots/search-list-light-loading.png) |
| [Destructive confirmation](#destructive-confirmation) | Captured, cancelled | [account-light-delete-confirm](screenshots/account-light-delete-confirm.png) |
| [Feedback after an action](#feedback-after-an-action) | Inline feedback captured; no toast appeared | [search-list-light-selected](screenshots/search-list-light-selected.png) |
| [Search and filtering](#search-and-filtering) | Captured | [search-list-light-settings-drawer](screenshots/search-list-light-settings-drawer.png) |
| [Data display](#data-display) | Captured | [library-table-light-default](screenshots/library-table-light-default.png), [search-list-light-keyword-results](screenshots/search-list-light-keyword-results.png) |
| [Onboarding and first run](#onboarding-and-first-run) | Only the hints an existing account sees | [search-split-light-default](screenshots/search-split-light-default.png) |

## App shell and navigation

**When.** Every signed-in page.

**Components.** [Top bar](components.md#top-bar) with the wordmark, the [Search and Library tabs](components.md#search-and-library-tabs), the [Upgrade pill](components.md#upgrade-pill), the [workspace menu button](components.md#workspace-menu-button) and the [account button](components.md#account-button); the [search session bar](components.md#search-session-bar); the [main card](components.md#main-card) and the [right panel](components.md#right-panel); the [workspace menu](components.md#menu) and the [account menu](components.md#account-menu).

**Layout.** A pastel gradient ground fills the window. The 64px top bar paints nothing of its own. Under it, search pages add a grey session bar (close, back, forward, the rabbit trail). The body is a half-white main card on the left and a 290 to 390px panel on the right (Next Search, an article's details, or layout settings). Home and the library use the same top bar with their own body: the home page centres a 1400px column of three cards; the library adds a sidebar of lists and collections. Account settings open as a dialog over whatever page is current, and the URL gains `?account=<tab>`.

**Widths.** At 640px or less every page is covered by a Screen too small notice ([library-mobile-light-screen-too-small](screenshots/library-mobile-light-screen-too-small.png)). Continue anyway shows the desktop layout clipped at the right edge ([library-mobile-light-continue](screenshots/library-mobile-light-continue.png)). There is no phone or tablet layout.

**Screens.** [home-light-default](screenshots/home-light-default.png), [search-split-light-default](screenshots/search-split-light-default.png), [library-list-light-default](screenshots/library-list-light-default.png), [home-light-workspace-menu](screenshots/home-light-workspace-menu.png), [home-light-account-menu](screenshots/home-light-account-menu.png).

## Forms and validation

**When.** Account details only: Update profile, Change email, Change password. Search has no form beyond its fields; settings apply as they change.

**Components.** [Dialog](components.md#dialog) with a [text field](components.md#text-field) per value under a 14px 500 label, then a text-only [Cancel](components.md#secondary-button) beside a black [Done](components.md#primary-button), both 56px tall and centred. Preferences uses a [checkbox](components.md#checkbox) with its sentence beside it and applies at once.

**Layout.** A form opens as a second dialog over Account Settings, 500px wide, 16px padding, 16px between fields. The scrim stacks, so the page behind darkens twice ([account-light-edit-profile-dialog](screenshots/account-light-edit-profile-dialog.png)).

**Validation.** Not captured. The only forms edit the account, and the capture did not empty or submit them, so where an error message appears and how it looks are unknown. The one gate seen is in the destructive confirmation below, where the action stays disabled until the typed phrase matches.

## Empty, loading and error states

**Empty.** Each empty place has its own copy, sized to where it sits:

| Where | What shows | Screen |
|---|---|---|
| Next Search, nothing selected | 24px "Pick where to start", an italic sentence, a carrot illustration and an underlined "Find out how it works" link | [search-split-light-default](screenshots/search-split-light-default.png) |
| Reading List | A 400px line illustration, "A clean slate - enjoy!", a sentence, and a black "Search for Articles" button | [library-reading-light-empty](screenshots/library-reading-light-empty.png) |
| An article's Notes tab | An illustration, a 600 heading "Turn reading into understanding", a sentence, and the note composer below | [library-all-light-notes-empty](screenshots/library-all-light-notes-empty.png) |
| A settings tab with nothing in it | One line of 14px text at the top left ("You have no active subscriptions") | [account-light-subscription-empty](screenshots/account-light-subscription-empty.png) |

The filter pills above the Reading List still show with zero counts (All 0, To Read 0, Read 0), and the selection actions stay disabled.

**Loading.** Two forms, both a 16px [spinner](components.md#spinner) turning every 1.1s:

- Paging a result list clears the list and centres the spinner in it ([search-list-light-loading](screenshots/search-list-light-loading.png)). The search bar, view toggle and right panel stay.
- Running a search again opens the loading [dialog](components.md#dialog): "Updating search..." over the spinner, on the usual scrim ([search-list-light-updating-dialog](screenshots/search-list-light-updating-dialog.png)).

The graph has its own entrance (nodes grow from dots), described in [graph.md](graph.md).

**Error.** Not captured. No request failed during the capture, and nothing was forced to fail.

## Destructive confirmation

**When.** Delete Account. In lists, Delete sits in the selection bar and stays disabled until an article is selected; the capture did not press it.

**Components.** A second [dialog](components.md#destructive-confirmation) over Account Settings: a title, two short sentences ("Are you really, **really** sure? This cannot be undone."), a pale yellow [typed-phrase box](components.md#typed-phrase-box) asking for "Delete my account", then a peach [danger button](components.md#danger-button) and a text-only Cancel.

**Behaviour seen.** The danger button is disabled while the phrase box is empty. Cancel closes the dialog and returns to Account Settings. The phrase was never typed, so the enabled danger button was not seen.

**Screen.** [account-light-delete-confirm](screenshots/account-light-delete-confirm.png).

## Feedback after an action

**Inline, in place.** Selecting an article fills its [selection circle](components.md#selection-circle) black with a white tick and draws a 1px black ring round the card. The right panel lists the paper under "1 selected" with an underlined [Clear](components.md#clear-link), and the drawer's summary changes to "Find related articles of 1 article" ([search-list-light-selected](screenshots/search-list-light-selected.png)). In the library the same selection enables Reading, Delete, Save, Export and Search ([library-all-light-selected](screenshots/library-all-light-selected.png)).

**On a setting.** Checking a filter on the drawer tints its whole row and adds a remove cross; because the filter is a paid one, the drawer's Search button gains a lock badge ([search-list-light-settings-checked](screenshots/search-list-light-settings-checked.png)).

**Toasts.** Not captured. A toast container is mounted on every page (z-index 2) but stayed empty: none of the actions taken (selecting, clearing, checking a filter, paging, searching) raised one.

## Search and filtering

**Start.** The home hero and the Search start page share one field: a black 53px pill with a magnifier, white placeholder text and a lavender Search button inside it, with Browse Library beside it ([home-light-search-typed](screenshots/home-light-search-typed.png), [search-start-light-recent](screenshots/search-start-light-recent.png)). The start page adds a BibTeX drop zone and the recent searches.

**Results.** A search opens a session: the query in a grey field at the top of the main card, a three-way view toggle (split, list, map), the results below, and Next Search at the right ([search-list-light-keyword-results](screenshots/search-list-light-keyword-results.png)).

**Refining.** The black Search Settings drawer at the foot of the right panel holds the controls ([search-list-light-settings-drawer](screenshots/search-list-light-settings-drawer.png)): [single-choice pills](components.md#single-choice-pills) for what to look for and how many results, then advanced filters marked by a green [Upgrade badge](components.md#upgrade-badge) and a [notice](components.md#notice-banner): a keyword field, two [range sliders](components.md#range-slider) with number fields, [multi-choice chips](components.md#multi-choice-chips), a [checkbox](components.md#checkbox) and a [select](components.md#select-in-the-drawer). In the graph, the filter popover filters by keyword ([search-map-light-filter-popover](screenshots/search-map-light-filter-popover.png)). In the library, a filter bar holds a sort select, a filter button, a Find in list field and the view buttons; the Reading List adds All, To Read and Read [filter pills](components.md#filter-toggle-pills).

## Data display

**List.** The default: one white [result card](components.md#result-card) per paper (author and year, title, journal in italics, a rule, then the abstract), with a selection circle at the top right. A [pager](components.md#list-pager) at the foot reads "1 - 10 of 6,020,000" between two chevrons.

**Table.** In the library the view buttons add a [table](components.md#article-table): a 600 header row (Label, Year, Title, Refs, Cites) with a sort chevron on the sorted column, 29px rows split by 1px grey rules, a grey row on hover, and a selection circle per row ([library-table-light-default](screenshots/library-table-light-default.png)).

**Graph.** The map and split views draw the same results as a citation graph; [graph.md](graph.md) covers it.

**Recent searches.** On the Search start page, each past search is a white row with its inputs as chips, its date in 12px grey, and a remove cross ([search-start-light-recent](screenshots/search-start-light-recent.png)).

## Onboarding and first run

**Not captured.** The account is not new, so the first-run flow did not appear, and Reset Tutorials in Preferences is disabled, so the tutorials could not be replayed. Opening a new account would mean creating one, which the capture does not do.

**What an existing account still sees.** A dismissible turquoise tip at the top of Next Search ("Select articles to help your next search find more accurate results"), the "Find out how it works" link in its empty state, and the What's New cards on the home page, which link to short guide videos ([home-light-default](screenshots/home-light-default.png)).
