# TokenTracker patterns

How TokenTracker v1.4.3's dashboard combines its components for the jobs every page repeats, read from the captures on 2026-10-17. Each entry says when the pattern is used, which components and tokens it is made of, the layout, and the screenshots that show it. Component names are entries in [components.md](components.md); token names are in [tokens.json](tokens.json).

These are observed patterns: what the product does, not rules its team wrote down. Where a state could not be reached, the entry says so.

## App shell and navigation

**When.** Every page.

**Made of.** `sidebar`, `nav-item`, `nav-item-active`, `sidebar-group-label`, `sidebar-toggle`, `account-control`, `theme-toggle`, `star-pill`, `content-panel`.

**Layout.** A 220px sidebar with no fill or border sits on the page wash (`bg.wash`). It holds the account control at the top, three labelled groups (General, Tools, Account) and two footer pills. The content panel starts at the sidebar's edge, 8px from the top and 12px from the right and bottom, with a 16px radius (`radius.2xl`), a hairline border and the only resting shadow (`shadow.sm`). The chevron collapses the sidebar to 72px of icons. Below `breakpoint.lg` (1024px) the sidebar becomes a drawer opened from a menu button. The current page is a filled row (`bg.navActive`); hover is a lighter wash (`bg.hover`) and changes nothing else.

**Screens.** [dashboard-dark-default](screenshots/dashboard-dark-default.png), [dashboard-light-sidebar-collapsed](screenshots/dashboard-light-sidebar-collapsed.png), [mobile-dashboard-dark-menu-open](screenshots/mobile-dashboard-dark-menu-open.png).

## Page header

**When.** Every page but Tokens, which leads with its period tabs instead.

**Made of.** `page-title` (`typography.pageTitle`, 36/40 semibold), `page-subtitle` (`typography.body` in `text.secondary`), and actions as 36px `icon-button`s at the top right (Refresh).

**Layout.** Title and one-line subtitle, left aligned, inside a centred `layout.contentWidth.page` (1152px) column. No breadcrumb, no tabs under the title.

**Screens.** [sessions-dark-default](screenshots/sessions-dark-default.png), [limits-light-default](screenshots/limits-light-default.png).

## Forms and validation

**When.** Settings is the only form surface. Every setting is a row: label and a one-line description on the left, the control on the right.

**Made of.** `settings-card`, `setting-label`, `setting-description`, `segmented` and `segment`, `select`, `text-field`, `field-error`, `primary-button` (Save), `share-button`-style outlined button (Test connection).

**Validation.** Fields are not checked as you type or on leaving them. The check runs when Test connection or Save is pressed. A failed field keeps its border (`text-field-error` reads the same as `text-field`); its hint line under the label is replaced by the error, in the same grey caption style (`field-error`), not in red. So the error sits where the help text was, and recovery is to edit the field and press the button again.

**Screens.** [settings-light-network](screenshots/settings-light-network.png), [settings-light-network-error](screenshots/settings-light-network-error.png), [settings-dark-network-error](screenshots/settings-dark-network-error.png). The proxy section's Manual mode was chosen in the capture browser to show the fields and was never saved.

## Empty, loading and error states

**When.** Every list and card that loads data. Sessions shows all three.

**Made of.** `empty-state`, `loading-state`, `error-state`, `retry-button`.

**Layout.** All three take the list's place inside the same bordered block and keep the page header, filters and summary strip in place, so nothing jumps when data arrives.

- **Loading** is one quiet line with a small spinner: "Loading sessions…". The summary reads "0 of 0". No skeletons.
- **Empty after a search** is a centred title ("No matching sessions") over a one-line hint ("Try a different search, or widen the date range."), with a "Clear filters" link beside the count. No illustration.
- **Error** is a centred title ("Could not load sessions"), the reason in secondary text ("Failed to fetch") and a small outlined Try again button.
- **Cards with no data** show dashes in place of numbers and an empty heatmap, rather than hiding (see Onboarding).

**Screens.** [sessions-loading-light-default](screenshots/sessions-loading-light-default.png), [sessions-dark-empty](screenshots/sessions-dark-empty.png), [sessions-error-dark-default](screenshots/sessions-error-dark-default.png). Loading and error were produced by holding back or aborting the sessions request in the capture browser.

## Confirming destructive actions

**When.** Removing skills, one or many (the source has the same confirmation for deleting a subscription). Only the Skills bulk remove was reached.

**Made of.** `checkbox`, the bulk action bar, `confirm-dialog`, `cancel-button`, `danger-button`, `confirm-scrim`.

**Layout.** Ticking a row shows a bar with the count ("1 selected") and the bulk actions. Remove opens a small centred dialog (448px wide, `bg.overlay`, `elevation.confirm`) over a 40% black scrim (`bg.scrim` family, `zIndex.scrim`). The title is a question with the count ("Remove 1 skills?"); one sentence says what will happen ("This unsyncs each skill from every agent and deletes its local copy."). Cancel is a quiet outlined button; the confirm button is the only red fill in the product (`button.danger.bg`), on the right. Escape cancels.

**Screens.** [skills-dark-selected](screenshots/skills-dark-selected.png), [skills-light-confirm](screenshots/skills-light-confirm.png), [skills-dark-confirm](screenshots/skills-dark-confirm.png). The dialog was cancelled with Escape; the confirm button was never pressed.

## Feedback after an action

**When.** After an action that finishes out of sight: copying or saving a share image, installing, syncing or removing skills, resetting a limit.

**Made of.** `toast`.

**Layout.** A small pill toast near the bottom centre of the window (`radius.full`, `shadow.md`, 12px text). A failure toast is filled red (`status.danger.fill`) with white text: "Couldn't generate image". Actions that finish in place report in place instead: the install command's Copy button reports "Copied to clipboard", and the proxy section prints "Proxy settings saved." under its buttons (seen in the source, not captured).

**Screens.** [dashboard-dark-toast](screenshots/dashboard-dark-toast.png), [dashboard-light-share-open](screenshots/dashboard-light-share-open.png). Only the failure toast was reached: a headless browser has no clipboard to copy the image to.

## Search and filtering

**When.** Sessions and Skills.

**Made of.** `search-field`, `search-input`, `select` and `select-menu` (tools, time, projects, models), the sort selects (By date, Recent), `summary-strip`.

**Layout.** One row: a wide search field, then four equal selects with a leading icon. Under it, a bordered summary strip of four figures (matching sessions, tokens, cost, speed) that updates with every filter, then the count ("756 root sessions") with the sort selects on the right. Filters apply at once; there is no Apply button. When a filter hides everything, a Clear filters link appears beside the count.

**Screens.** [sessions-dark-default](screenshots/sessions-dark-default.png), [sessions-light-search-focused](screenshots/sessions-light-search-focused.png), [sessions-light-select-open](screenshots/sessions-light-select-open.png), [sessions-dark-empty](screenshots/sessions-dark-empty.png).

## Data display

**When.** Usage by day, sessions, models, limits.

**Made of.** `table-tab`, `table-header`, `table-row`, `table-cell`, `list-header`, `list-row`, `list-row-title`, `provider-tile`, `stat-chip`, `usage-row`, `usage-track`, `tooltip`.

**Layout.** Tables are borderless rows split by hairlines (`border.default`) with a sticky header (`zIndex.sticky`), numbers right of the label column in tabular figures, and a row hover wash. Two tables share a card through small tabs (Daily Breakdown, Project Usage). Sessions is a list grouped under date headings, each row a title over a dotted metadata line, with tokens, cost and speed right aligned. Big figures lead (`typography.display`); money is the one green thing (`accent.default`). Limits are thin tracks with a percentage and time left. Hovering a heatmap cell or a pill opens a tooltip (`shadow.xl`).

**Screens.** [dashboard-dark-full](screenshots/dashboard-dark-full.png), [sessions-light-row-hover](screenshots/sessions-light-row-hover.png), [limits-dark-full](screenshots/limits-dark-full.png).

## Onboarding and first run

**When.** A machine with no usage recorded yet.

**Layout.** There is no welcome screen or tour. The Tokens page renders as usual with zeros and dashes, and the first card is replaced by the one step to take: "Install Node.js 18+ then run:" over a code block (`typography.code`, `bg.code`) holding `npx --yes tokentracker-cli init`, with a Copy button. The heatmap draws its empty grid and the table lists the dates with dashes.

**Screens.** [onboarding-dark-default](screenshots/onboarding-dark-default.png), [onboarding-light-full](screenshots/onboarding-light-full.png). Captured from a second TokenTracker started with an empty home folder, so nothing was stubbed.
