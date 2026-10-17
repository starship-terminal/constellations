# Brilliant patterns

How Brilliant's components combine for the jobs every app has, written from what the captures show: the 2026-09-25 capture (onboarding, lessons, course pages) and the 2026-10-17 recapture (settings, You, Topics, Koji, Help Center search, phone width). Every claim links the screenshot it was read from; values are tokens in [tokens.json](tokens.json) and specs in [components.md](components.md). Where the product does something only once, the entry says so rather than generalising.

Screenshots under `screenshots/app-2026-10/` exist in dark and light (`-dark-` and `-light-` in the name); older ones carry the theme they were taken in.

## App shell and navigation

**When:** every signed-in page except the lesson player and onboarding.

| Part | Desktop (1440) | Phone (390) |
|---|---|---|
| App bar | Sticky, `size.appBar` (64px plus a 1px `border.primary` bottom edge), `bg.elevated`, `shadow.subtle`, stacked at `zIndex.app-bar` | Same bar, no logo: four icon tabs (Home, Topics, Koji, You) then the league, key and streak pills |
| Primary nav | Three text tabs with 16px icons (Home, Topics, You); selected is `text.primary` with a 2px underline, others `text.secondary` | Icon tabs, selected underlined |
| Right side | "Go Premium" pill, key and streak stat pills (each opens a popover), menu button (Settings, About, Help, Log out) | Stat pills stay; the menu moves off the bar's right edge |
| Content | One column of `layout.container` (1216px) centred, 112px side margins | One column between `layout.gutter-phone` (24px) gutters |
| Page grids | Home `layout.grid-home` (a 384px leagues card beside a 592px course card, 24px gap); Settings `layout.grid-settings` (side menu, 592px form, balancing column) | Everything stacks into one column (`layout.grid-phone`) |

Full-screen tasks drop the shell: the lesson player shows only a close button, the lesson progress bar, XP and streak, and onboarding shows a back chevron and a progress bar.

Evidence: [home-dark-default](screenshots/app-2026-10/home-dark-default.png), [settings-light-preferences](screenshots/app-2026-10/settings-light-preferences.png), [mobile-home-dark-default](screenshots/app-2026-10/mobile-home-dark-default.png), [mobile-courses-light-default](screenshots/app-2026-10/mobile-courses-light-default.png), [home-dark-menu-keyboard](screenshots/app-2026-10/home-dark-menu-keyboard.png), [lesson-light-default](screenshots/lesson-light-default.png), [raw/layout.json](raw/layout.json).

## Forms and validation

**When:** settings (personal info, email addresses) and sign-in.

- Labels sit above fields (`field-label`, `typography.body.sm`); fields are `size.control-lg` (52px) with a 2px `border.primary` edge and `radius.md`. Focus thickens the edge to `border.active` with an inset 1px ring (`shadow.input-focus`), with no outer glow. See [text-field crops](components/crops/2026-10/text-field-dark-focus-visible.png).
- The submit button is full width and disabled (`bg.disabled`, `text.disabled`) until the form has a change to save: "Update personal info" in settings, "Sign in" on login, Check in a lesson, Continue in onboarding. It fills in place rather than appearing. See [settings-dark-account](screenshots/app-2026-10/settings-dark-account.png) and [login-light-default](screenshots/login-light-default.png).
- Secondary form actions are outline buttons at `size.control-sm` inside the row they act on ("Send verification" beside an unverified address), and status sits in badges on the same row (UNVERIFIED in yellow, PRIMARY in blue). See [settings-light-account](screenshots/app-2026-10/settings-light-account.png).
- Errors: the product leaves format checks to the browser. An invalid address in Settings > Add another email stops at Chrome's native bubble ("Please include an '@' in the email address") and the field keeps its default `border.primary` edge, so nothing on the page itself turns red. See [settings-dark-email-invalid](screenshots/app-2026-10/settings-dark-email-invalid.png) and [raw/live-readings.json](raw/live-readings.json). The stylesheet also has invalid rules (`border.danger-primary` outline, `text.danger-primary` message, [raw/css-rules.json](raw/css-rules.json)) that this field never showed.
- Informational notes sit above the form as an info alert (`feedback.info`: `bg.blue-secondary`, `text.primary`, no border, `radius.lg`), for example the no-password notice in Settings > Account. See [alert-info crop](components/crops/2026-10/alert-info-dark-default.png).

## Empty, loading and error states

**Empty.** A new account's You page keeps every module in place and fills it with zeros rather than hiding it: the Weekly summary card carries Koji's line "No practice yet this week. Visit Home or Courses to pick a lesson, and I'll help you get started.", the stat cards read 0 and 0.0%, the bar chart draws a 2px stub for each zero day, and "No course progress yet." stands under Your learning progress. The next-period arrow is disabled (`text.disabled`) on the current week. See [you-dark-empty](screenshots/app-2026-10/you-dark-empty.png), [you-light-empty](screenshots/app-2026-10/you-light-empty.png), [mobile-you-light-empty](screenshots/app-2026-10/mobile-you-light-empty.png).

**Search with no result.** The Help Center says so inside the results panel, quoting the query ("No results found for …"), and leaves the topic lists below it. See [help-light-search-empty](screenshots/app-2026-10/help-light-search-empty.png).

**Loading.** Text that depends on account data renders inside skeleton slots (`data-slot=skeleton`, pulsing between `component.skeleton.from` and `to` over `duration.skeleton`); the You page holds its chart's place with one large rounded skeleton block while it loads ([you-dark-loading](screenshots/app-2026-10/you-dark-loading.png), [you-light-loading](screenshots/app-2026-10/you-light-loading.png)). Buttons that wait show a 16px spinner in their own label colour, and plan creation gets a full-screen Koji loader. See [plan-dark-creating-plan-loading](screenshots/plan-dark-creating-plan-loading.png).

**Error.** A missing page is a plain page with a heading and a "Go home" button; no in-app error banner was reached. See [notfound-light-404](screenshots/notfound-light-404.png).

## Destructive confirmation

**When:** leaving a lesson part-way, and deactivating the account.

A centred dialog (`modal-content`, `shadow.md`, `radius.2xl`, max `size.modal-max`) over `special.overlay.default` asks "Are you sure?" and states the cost in one line ("If you quit, you will lose your progress and XP."). The safe choice is the filled full-width button3d ("Keep learning"); the destructive one is a red text button below it ("Quit", `feedback.danger.text`), which only gains a tint on hover (`bg.red-tertiary`) or press. See [lesson-dark-quit-dialog](screenshots/app-2026-10/lesson-dark-quit-dialog.png), [lesson-light-quit-dialog](screenshots/app-2026-10/lesson-light-quit-dialog.png) and the [Quit crops](components/crops/2026-10/button-danger-text-dark-hover.png).

Deactivating the account is a full page behind a plain "Deactivate or delete your account" link in Settings. It asks why, as a list of checkboxes ("Other" opens a bordered text area), and its solid red "Deactivate account" button (`size.control-md`, pill radius) stays disabled in a dark red tint until a reason is checked. Nothing was submitted. See [deactivate-dark-default](screenshots/app-2026-10/deactivate-dark-default.png), [deactivate-light-other-checked](screenshots/app-2026-10/deactivate-light-other-checked.png) and the [danger button crops](components/crops/2026-10/button-danger-disabled-dark-default.png).

## Feedback after an action

- **Inline, in place.** The lesson answers Check in the panel itself: the frame border turns `component.lesson.frame-correct` (with a 1s glow) or `frame-retry` (with a 0.45s shake when motion is allowed), Koji's bubble arrives in the same hue, and the footer swaps to a green "Continue" or yellow "Try again". See [lesson-dark-correct](screenshots/lesson-dark-correct.png) and [lesson-dark-retryable](screenshots/lesson-dark-retryable.png).
- **State change on the control.** Preferences has no save button: its switches and segments change on click and show their new state as the only feedback. See [settings-dark-preferences](screenshots/app-2026-10/settings-dark-preferences.png).
- **Toast.** Quick, reversible actions confirm with a Sonner toast at the bottom of the viewport (356px, `radius.lg`, `shadow.base`). Unstarring a topic shows a neutral toast ("Removed from your topics"); starring shows a green success-tinted one ("Added to your learning paths"). Neither has an undo button; the star itself undoes it. See [courses-dark-toast](screenshots/app-2026-10/courses-dark-toast.png), [courses-light-toast-added](screenshots/app-2026-10/courses-light-toast-added.png).

## Search and filtering

- **Ask, don't filter.** The Topics page has no filter: its search box reads "What do you want to learn?" with an Ask button that hands the query to Koji. Topics are grouped by learning path instead, and at phone width a sticky row of path tabs (Math, Basic Algebra, CS, Data) jumps between groups. See [courses-dark-default](screenshots/app-2026-10/courses-dark-default.png) and [mobile-courses-dark-default](screenshots/app-2026-10/mobile-courses-dark-default.png).
- **Live results.** The public Help Center search is a 52px pill (`radius` 32, 2px `border.primary`, white at 43% until focused) whose results drop into a panel under it as you type, each a title with a highlighted excerpt. See [help-light-search-results](screenshots/app-2026-10/help-light-search-results.png).
- **Period filter.** The You page filters its stats with a segmented control (All time, Week, Month, Year) plus previous and next arrows for the period. See [you-light-empty](screenshots/app-2026-10/you-light-empty.png).

## Data display

- **Stat cards and chart.** The You page pairs two stat cards (label `typography.body.sm`, value `typography.heading.xl`, an info tooltip on each) with a bar chart of plain blue bars (`component.chart.bar`). The chart carries a screen-reader-only data table (`data-slot=table` inside a visually hidden wrapper) with the same numbers. See [you-dark-tooltip](screenshots/app-2026-10/you-dark-tooltip.png) and [raw/components-computed.json](raw/components-computed.json).
- **Grid of cards.** Topics lists courses as 150px 3D cards (2px `border.solid` edge and a 4px lip, `radius.xl`), six to a shelf, with a grade badge and a NEW badge on the card. See [courses-light-default](screenshots/app-2026-10/courses-light-default.png).
- **Comparison table.** The only visible table is Free vs Premium on `/subscribe/`, with the Premium column framed in the iridescent gradient. See [premium-comparison-dark](components/crops/premium-comparison-dark.png).
- No sorting or pagination appears anywhere in the free app.

## Onboarding and first run

**When:** a new account's first session (2026-09 capture, dark).

One question per screen under a progress bar (`size.progress-default`): Koji introduces itself, then voice choice, subject, level and a short placement question, each answered by tapping a choice card (selected cards get the blue hue-shift fill and the `shadow.outline` ring). Continue stays disabled until a card is chosen. A full-screen loader builds the learning plan, which then opens on a path of course tiles with "START HERE" on the first and a fixed bottom bar holding one button3d. See [onboarding-dark-intro](screenshots/onboarding-dark-intro.png), [onboarding-dark-subject-selected](screenshots/onboarding-dark-subject-selected.png), [onboarding-dark-level-list](screenshots/onboarding-dark-level-list.png), [plan-dark-creating-plan-loading](screenshots/plan-dark-creating-plan-loading.png) and [plan-dark-learning-path](screenshots/plan-dark-learning-path.png).

First run on Home afterwards puts one course card front and centre with a single blue Start, and the Koji page greets the learner by first name over four suggestion cards. See [home-light-default](screenshots/app-2026-10/home-light-default.png) and [koji-dark-default](screenshots/app-2026-10/koji-dark-default.png).
