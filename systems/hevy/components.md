# Hevy components

Public web, 2026-11-21, is a separate surface from the iOS inventory below. Sign Up is a blue pill, 100×48, radius 11.3213px, fill rgb(38, 127, 232), white label. Log in is the same blue as text, weight 500, 17px. Product and Articles open a white menu, 225px wide, radius 10px, shadow rgba(0, 0, 0, 0.25) 0px 0px 6px 0px. The exercise search field is 50px tall. See [screenshots/public/](screenshots/public) and the `public-web` set in [tokens.json](tokens.json).

One entry per component in the measured reference ([raw/hevy-style-measured.md](raw/hevy-style-measured.md)), with size, radius, fill, states and the capture that shows it. Captured from Hevy 3.1.16 on iOS 26, free account, 2026-10-10, through iPhone Mirroring, at 390 x 844 pt (1 px = 1 pt, screen offset (8, 38) inside each PNG).

How to read an entry:

- Fills and text colours are token names from [tokens.json](tokens.json) (`color.accent.default`). Values are in the `light` and `dark` sets; sizes and radii are in `core` (`size.button.primary`, `radius.button`).
- Sizes are width x height in points. A bare number with no token has no token because it was read once and is not reused.
- Radii are estimates (plus or minus 2 pt). Sizes read off pixel edges are exact to the point. See "How the values were read" in [README.md](README.md).
- Layout, sizes and radii are the same in both themes. Only colour changes. Two things flip: cards (white with a 1 pt border in light, a filled `color.surface.card` with no border in dark) and settings (white rows on pale bands in light, raised rows on black in dark).
- Every capture is a link into [screenshots/](screenshots). `d` files are dark, `p` and `t` files are the detail pages (dark), the numbered files are light. The full screen list is in [page-tree.md](page-tree.md).

## Buttons

### Primary button
- Size: 358 x 40 (`size.content.width` x `size.button.primary`; the doc reads 39 to 40).
- Radius: `radius.button`.
- Fill: `color.accent.default`, label `color.text.onAccent`, `typography.body` at medium weight.
- States: default only in the captures. No pressed state was captured.
- Capture: [02-workout.png](screenshots/light/02-workout.png), dark [d10-workout.png](screenshots/dark/d10-workout.png).

### Secondary button, tall
- Size: 358 x 48 or 171 x 48 (`size.button.tall`; the 171 form sits in the two-up grid, `size.twoUp.width`).
- Radius: `radius.button`.
- Fill: `color.surface.raised`, dark label `color.text.body`, leading icon. Inside a dialog or the timer bar the fill is `color.surface.raised2`.
- States: the "Discard Workout" form keeps the neutral fill and turns the label `color.state.destructive`.
- Capture: [02-workout.png](screenshots/light/02-workout.png), red label in [14-empty-workout.png](screenshots/light/14-empty-workout.png).

### Secondary button, short ("Add Set")
- Size: 358 x 41 (`size.button.short`).
- Radius: `radius.button`.
- Fill: `color.surface.raised`.
- Capture: [03-log-workout.png](screenshots/light/03-log-workout.png).

### Floating count button ("Add 2 exercises")
- Size: 356 x 38 (`size.floatingButton.height`), pinned above the home indicator.
- Radius: `radius.control`.
- Fill: `color.accent.default`, label `color.text.onAccent`.
- States: appears only once a row is selected.
- Capture: [09-exercise-picker-selected.png](screenshots/light/09-exercise-picker-selected.png), dark [d12-exercise-picker-selected.png](screenshots/dark/d12-exercise-picker-selected.png).

### Small action ("Unlock")
- Size: 96 x 28.
- Radius: `radius.control`.
- Fill: `color.accent.default`.
- Capture: [13-settings.png](screenshots/light/13-settings.png).

### Dialog button
- Size: 294 x 40 (`size.dialogButton.width` x `size.dialogButton.height`).
- Radius: `radius.button`.
- Fill: `color.surface.raised2` in dark, `color.surface.raised` in light. The destructive label uses `color.state.destructive`.
- Capture: [06-discard-dialog.png](screenshots/light/06-discard-dialog.png), dark [d15-discard-dialog.png](screenshots/dark/d15-discard-dialog.png).

### Active filter button
- Fill: `color.accent.default`, white label with a clear (x).
- States: the neutral filter button (171 x 36, `size.control`, `color.surface.raised`) becomes this once a filter is on.
- Capture: [p12-filter-active.png](screenshots/pages/p12-filter-active.png).

### Filter button ("All Equipment")
- Size: 171 x 36 (`size.twoUp.width` x `size.searchField`).
- Radius: `radius.control`.
- Fill: `color.surface.raised`.
- Capture: [08-exercise-picker.png](screenshots/light/08-exercise-picker.png).

### Text button
- Fill: none. Blue "Connect" uses `color.accent.default`, red "Disconnect" uses `color.state.destructive`.
- Capture: [p31-apple-health-connect.png](screenshots/pages/p31-apple-health-connect.png), [p32-integrations-connected-states.png](screenshots/pages/p32-integrations-connected-states.png).

### Glass nav pills (iOS 26)
- Cancel: accent text on glass. Save: `color.accent.default` fill when enabled, `color.button.disabledGlass` when disabled. Finish: `color.accent.glass`.
- These are system glass; use standard SwiftUI components on iOS 26 rather than drawing them.
- Capture: disabled Save in [07-new-routine-empty.png](screenshots/light/07-new-routine-empty.png), enabled in [10-routine-editor.png](screenshots/light/10-routine-editor.png), Finish in [03-log-workout.png](screenshots/light/03-log-workout.png).

## Inputs and controls

### Search field
- Size: 358 x 36 (`size.content.width` x `size.searchField`).
- Radius: `radius.control`.
- Fill: `color.surface.raised`, placeholder `color.text.tertiary`, leading magnifier.
- Capture: [08-exercise-picker.png](screenshots/light/08-exercise-picker.png).

### Weight and reps input
- Size: 73 x 33 (`size.input.width` x `size.input.height`).
- Radius: `radius.control`.
- Fill: `color.surface.card` with a 1 pt `color.border.input` border, placeholder "-" in `color.text.tertiary`.
- States: focused (below), completed (values bold in `color.text.heading`, border gone).
- Capture: [03-log-workout.png](screenshots/light/03-log-workout.png).

### Focused input
- Size: 73 x 33.
- Border: `color.accent.focus`, about 1.5 pt (`border.width.focus`). The placeholder stays grey.
- Capture: [16-keyboard-input.png](screenshots/light/16-keyboard-input.png), dark [d14-sets-completed-timer-focus.png](screenshots/dark/d14-sets-completed-timer-focus.png).

### Set number chip
- Size: 36 x 36 (`size.control`).
- Radius: `radius.control`.
- Fill: `color.surface.raised`, bold number. Warm-up shows an orange "W" in `color.set.warmup`.
- States: on a ticked row the fill becomes `color.state.successChip`.
- Capture: [03-log-workout.png](screenshots/light/03-log-workout.png), [15-sets-completed-rest-timer.png](screenshots/light/15-sets-completed-rest-timer.png).

### Set check box
- Size: 36 x 36 (`size.control`).
- Radius: `radius.control`.
- Fill: `color.surface.raised` with a tick in `color.text.tertiary`.
- States: completed fills `color.state.success` with a white tick.
- Capture: [03-log-workout.png](screenshots/light/03-log-workout.png), [15-sets-completed-rest-timer.png](screenshots/light/15-sets-completed-rest-timer.png).

### Set row
- Size: 47 pt pitch (`size.setRow`: 36 pt controls plus an 11 pt gap), full width.
- Columns: set chip, previous value, weight input, reps input, check box. Column headers use `typography.columnHeader`.
- States: normal; completed (whole row `color.state.successRowTint`, values bold and dark); set types (see "Set type colours").
- Capture: [03-log-workout.png](screenshots/light/03-log-workout.png), [15-sets-completed-rest-timer.png](screenshots/light/15-sets-completed-rest-timer.png), [p17-set-types-in-table.png](screenshots/pages/p17-set-types-in-table.png).

### Switch
- Size: about 62 x 26 (`size.switch.width` x `size.switch.height`), pill.
- Fill: on `color.accent.default`, off `color.switch.offTrack`.
- Capture: [17-workout-settings-toggles.png](screenshots/light/17-workout-settings-toggles.png), off in dark [d06-privacy-switches-off.png](screenshots/dark/d06-privacy-switches-off.png), on in dark [d05-notifications-switches.png](screenshots/dark/d05-notifications-switches.png).

### Segmented control (Units)
- Size: container 358 x 50, selected segment 173 x 40.
- Radius: `radius.button`.
- Fill: container `color.bg.page` with a 1 pt `color.border.input`; selected segment `color.accent.default` with a `color.text.onAccent` label.
- The same control appears in the Clock sheet. Measured in dark.
- Capture: [d04-units-segmented.png](screenshots/dark/d04-units-segmented.png), [p20-clock-timer-ring.png](screenshots/pages/p20-clock-timer-ring.png).

### Wheel picker
- System wheel inside a sheet (`color.surface.sheetFilter` in dark). Selected band `color.surface.wheelBand`, accent Done button below.
- Capture: [p18-rest-timer-wheel-picker.png](screenshots/pages/p18-rest-timer-wheel-picker.png), [t70-date-time-wheel-sheet.png](screenshots/pages/t70-date-time-wheel-sheet.png).

### Form row
- Label on the left, value or a blue "Select" (`color.accent.default`) below or at the right, chevron. Rows are separated by `color.divider`.
- Capture: [p14-create-exercise-form.png](screenshots/pages/p14-create-exercise-form.png), [p27-edit-profile-form.png](screenshots/pages/p27-edit-profile-form.png).

## Chips, badges and banners

### Chip and segmented pill
- Size: auto x 28 (`size.chip`).
- Radius: `radius.full`.
- Fill: selected `color.accent.default` with `color.text.onAccent`; unselected `color.surface.raised` with `color.text.body`.
- Capture: [11-profile.png](screenshots/light/11-profile.png).

### Tag chip
- Small grey rounded tag ("Reps", "Kg", "Time"), `color.surface.raised` with `color.text.secondary`.
- Capture: [p15-exercise-type-list-tags.png](screenshots/pages/p15-exercise-type-list-tags.png).

### Selection badge
- Size: 16 x 16 circle (`size.badge.selection`), top right of a row image.
- Fill: `color.accent.default` with a white tick.
- Capture: [09-exercise-picker-selected.png](screenshots/light/09-exercise-picker-selected.png).

### Pro badge
- Size: 40 x 18 (`size.proBadge.width` x `size.proBadge.height`), `radius.full`.
- Fill: `color.badge.pro`, dark "PRO". The same in both themes.
- Capture: [17-workout-settings-toggles.png](screenshots/light/17-workout-settings-toggles.png).

### Tip banner
- Size: 356 x 38, `radius.control`.
- Fill: `color.banner.tip`, dark text, close icon on the right. The same in both themes.
- States: dismissible.
- Capture: [02-workout.png](screenshots/light/02-workout.png).

### Underline tabs
- Text tabs across the top. Active in `color.text.heading` with a `color.accent.default` underline, inactive `color.text.secondary`.
- Capture: [p01-search.png](screenshots/pages/p01-search.png), [p06-exercise-summary.png](screenshots/pages/p06-exercise-summary.png).

### Rank medals
- Filled circles: `color.medal.gold`, `color.medal.silver`, `color.medal.bronze`, then plain numbers. The current user's row sits on a raised fill and is pinned at the bottom.
- Capture: [p09-exercise-leaderboard.png](screenshots/pages/p09-exercise-leaderboard.png), [t73-leaderboard-bottom-sticky-you.png](screenshots/pages/t73-leaderboard-bottom-sticky-you.png).

### Set type colours
- Warm-up "W" `color.set.warmup`, Failure "F" `color.set.failure`, Drop "D" `color.set.drop` (a cyan, separate from the accent), Normal numbered in `color.text.heading`.
- Capture: [p16-set-type-sheet.png](screenshots/pages/p16-set-type-sheet.png), [p17-set-types-in-table.png](screenshots/pages/p17-set-types-in-table.png).

## Rows and lists

### Exercise picker row
- Size: 80 tall, full bleed (`size.row.picker`). Image in a 56 pt white circle at x 16 (`size.avatar.picker`).
- Two lines: name in `typography.cardTitle` style, muscle group in `color.text.secondary`.
- States: selected row tinted `color.tint.selectedRow` with a selection badge.
- Capture: [08-exercise-picker.png](screenshots/light/08-exercise-picker.png), [09-exercise-picker-selected.png](screenshots/light/09-exercise-picker-selected.png).

### Settings row
- Size: 60 tall (`size.row.settings`), leading icon, label, chevron at the right.
- Fill: white on `color.bg.grouped` bands in light, `color.surface.card` on black in dark. Dividers `color.divider`.
- Capture: [13-settings.png](screenshots/light/13-settings.png), dark [d02-settings-top.png](screenshots/dark/d02-settings-top.png).

### Settings section header
- Size: 54 tall band (`size.row.settingsHeader`), label in `color.text.secondary`.
- Capture: [13-settings.png](screenshots/light/13-settings.png).

### Settings row with value
- Size: 60 tall. Label at the left, grey value (`color.text.secondary`) and chevron at the right.
- Capture: [17-workout-settings-toggles.png](screenshots/light/17-workout-settings-toggles.png).

### Single-choice list
- Rows with an accent checkmark on the chosen one.
- Capture: [p29-language-single-choice.png](screenshots/pages/p29-language-single-choice.png).

### Card list (FAQ)
- Each item its own rounded `color.surface.card` card with a chevron and gaps between cards (measured in dark).
- Capture: [p34-faq-card-list.png](screenshots/pages/p34-faq-card-list.png).

## Cards

### Routine card
- Size: full width minus the 16 pt margins. Padding `space.cardPadding` (18).
- Radius: `radius.card`.
- Fill: `color.surface.card` with a 1 pt `color.border.card` (no border in dark). Title in `typography.cardTitle`, grey exercise list, "..." menu, a primary button inside.
- Capture: [02-workout.png](screenshots/light/02-workout.png), dark [d10-workout.png](screenshots/dark/d10-workout.png).

### Dashboard tile
- Size: 171 x 48 (`size.twoUp.width` x `size.tile.height`).
- Radius: `radius.card`.
- Fill: `color.surface.raised`, icon and label.
- Capture: [11-profile.png](screenshots/light/11-profile.png).

### Stat card (muscle distribution)
- 2 x 2 grid, about 171 wide, `radius.card`. `color.surface.card` with a thin border, label, bold value, small trend line. Observed in dark with empty data.
- Capture: [d09-muscle-distribution-chart.png](screenshots/dark/d09-muscle-distribution-chart.png).

### Plan card (paywall)
- Three cards side by side. The selected one has an accent border and an accent "Save 33%" tab on top.
- Capture: [p28-paywall.png](screenshots/pages/p28-paywall.png), [t18-paywall-contextual.png](screenshots/pages/t18-paywall-contextual.png).

### Post card (feed)
- Author row, workout summary, stat row, social actions. Other users are blurred in the capture.
- Capture: [01-home.png](screenshots/light/01-home.png), dark [d17-home.png](screenshots/dark/d17-home.png).

## Timer and progress

### Rest timer bar
- Size: 390 x 91, docked at the bottom (`size.timerBar`), no radius.
- Fill: `color.surface.card`. A 3 pt `color.accent.default` progress line on the top edge (`size.progressLine.timer`) that shrinks as the time runs down.
- Row: "-15" (70 x 38, `color.surface.raised2`), mm:ss digits in `typography.timerDigits` and `color.text.heading`, "+15", then Skip (68 x 36, `color.accent.default`).
- Capture: [15-sets-completed-rest-timer.png](screenshots/light/15-sets-completed-rest-timer.png), dark [d14-sets-completed-timer-focus.png](screenshots/dark/d14-sets-completed-timer-focus.png).

### Workout progress line
- 1 pt full-width `color.accent.default` line under the nav bar (`size.progressLine.workout`).
- Capture: [15-sets-completed-rest-timer.png](screenshots/light/15-sets-completed-rest-timer.png).

### Minimised workout bar
- Sits above the tab bar: a `color.state.live` dot, elapsed time, current exercise, a `color.state.destructive` trash icon.
- Capture: [05-workout-in-progress-bar.png](screenshots/light/05-workout-in-progress-bar.png).

### Circular timer
- Large thin accent ring with big digits inside, small "-15s" and "+15s" accent text on either side.
- Capture: [p20-clock-timer-ring.png](screenshots/pages/p20-clock-timer-ring.png), [p21-clock-stopwatch.png](screenshots/pages/p21-clock-stopwatch.png).

## Sheets, dialogs and feedback

### Bottom sheet
- Fill: `color.surface.sheet`, grabber at the top, centred title, dims the page with `color.scrim`. Filter sheets use `color.surface.sheetFilter`.
- Capture: [p16-set-type-sheet.png](screenshots/pages/p16-set-type-sheet.png), [p10-filter-sheet-equipment.png](screenshots/pages/p10-filter-sheet-equipment.png).

### Action sheet item
- Leading icon and label. Destructive items (Delete, Remove) use `color.state.destructive` for label and icon.
- Capture: [p05-action-sheet.png](screenshots/pages/p05-action-sheet.png), [p19-exercise-menu-sheet.png](screenshots/pages/p19-exercise-menu-sheet.png).

### Filter tile
- `color.surface.raised2` on the sheet, round icon at the left, label. Selected: accent border.
- Capture: [p10-filter-sheet-equipment.png](screenshots/pages/p10-filter-sheet-equipment.png), [p11-filter-tile-selected.png](screenshots/pages/p11-filter-tile-selected.png).

### Sheet footer
- Two buttons: neutral "Clear Filters" and accent "Show N results" with a live count.
- Capture: [p11-filter-tile-selected.png](screenshots/pages/p11-filter-tile-selected.png).

### Confirm dialog (destructive)
- Centred card with a question, red "Discard Workout" and neutral "Cancel", over `color.scrim`.
- Capture: [06-discard-dialog.png](screenshots/light/06-discard-dialog.png), dark [d15-discard-dialog.png](screenshots/dark/d15-discard-dialog.png).

### Alert with one button
- Centred card, short message, full-width accent "Ok". Used for validation ("Add an exercise") and confirmations.
- Capture: [t75-finish-validation-alert.png](screenshots/pages/t75-finish-validation-alert.png), [t23-copy-link-alert.png](screenshots/pages/t23-copy-link-alert.png).

### Info dialog
- Optional bold title, body text, accent "Okay" or "Ok". Opened from "?" icons.
- Capture: [t19-info-dialog.png](screenshots/pages/t19-info-dialog.png), [t104-info-dialog-no-title.png](screenshots/pages/t104-info-dialog-no-title.png).

### Toast
- Small dark pill at the top, short text, disappears on its own. The only real toast is "Link Copied".
- Not in any capture. This description comes from the capture notes alone: [t93-toast-link-copied.png](screenshots/pages/t93-toast-link-copied.png) shows no toast and is the same as the share composer [t91](screenshots/pages/t91-share-workout-template-1.png) apart from the clock.

### Tooltip
- Light pill pointing at a row on first use ("Tap to select your gym").
- Capture: [t83-save-workout-tooltip.png](screenshots/pages/t83-save-workout-tooltip.png).

### Skeleton and spinner
- Skeleton: rounded grey placeholder cards while content loads. Spinner: small system spinner centred under the header.
- Not in any capture. This description comes from the capture notes alone: [t98-skeleton-loading-suggested.png](screenshots/pages/t98-skeleton-loading-suggested.png) shows the Suggested Athletes cards loaded, with their contents masked and blue Follow buttons, and [t24-contacts-loading-spinner.png](screenshots/pages/t24-contacts-loading-spinner.png) is the same as the empty state [t25](screenshots/pages/t25-contacts-empty.png) apart from the tab bar.

### Empty state
- Line icon (`color.text.tertiary`), bold title or grey sentence, optional primary button.
- Capture: [07-new-routine-empty.png](screenshots/light/07-new-routine-empty.png), [t25-contacts-empty.png](screenshots/pages/t25-contacts-empty.png), [t27-search-no-results.png](screenshots/pages/t27-search-no-results.png).

### Paywall and upsell
- Full-screen paywall with a generic version and feature-specific heroes over the same three plan cards. A short "Upgrade to HEVY PRO" bottom sheet with Continue and Not now for locked fields. A yellow PRO pill on rows and a lock icon on form fields.
- Capture: [p28-paywall.png](screenshots/pages/p28-paywall.png), [t113-upsell-bottom-sheet.png](screenshots/pages/t113-upsell-bottom-sheet.png), [t17-period-sheet-pro-locked.png](screenshots/pages/t17-period-sheet-pro-locked.png).

## Charts and data

### Horizontal bar chart
- `color.accent.default` bars of varying length with the percentage at the bar end, label above each.
- Capture: [p03-workout-detail.png](screenshots/pages/p03-workout-detail.png).

### Comparison bars
- Paired horizontal bars: accent for you, grey for the other person, a red down arrow with a percentage.
- Capture: [t16-compare-exercise.png](screenshots/pages/t16-compare-exercise.png).

### Radar chart
- About six axes (Back, Chest, Core, Shoulders, Arms, Legs). Grey hexagon grid, accent for current, grey for previous, legend below. Observed in dark with empty data.
- Capture: [d09-muscle-distribution-chart.png](screenshots/dark/d09-muscle-distribution-chart.png), [t102-monthly-report-bottom.png](screenshots/pages/t102-monthly-report-bottom.png).

### Calendar month
- 7-column grid, weekday header, month title, today's date in `color.accent.default`, summary pills (week streak with a flame, rest days with a moon).
- Capture: [p24-calendar-month.png](screenshots/pages/p24-calendar-month.png), [t110-calendar-month-workout-days.png](screenshots/pages/t110-calendar-month-workout-days.png).

### Activity heatmap
- Year and multi-year grids of small squares, accent for workout days.
- Capture: [t106-calendar-year-heatmap.png](screenshots/pages/t106-calendar-year-heatmap.png), [t107-calendar-multiyear-heatmap.png](screenshots/pages/t107-calendar-multiyear-heatmap.png).

## System chrome (iOS 26)

### Tab bar
- A floating glass capsule with three items (Home, Workout, Profile). The active item gets a lighter glass lozenge plus accent tint.
- Comes from the system in SwiftUI. Its size was not measured.
- Capture: [d10-workout.png](screenshots/dark/d10-workout.png), [17-workout-settings-toggles.png](screenshots/light/17-workout-settings-toggles.png).

### Large title and nav bar
- Large title `typography.largeTitle`, nav bar title `typography.navTitle`. The large title collapsing into the bar on scroll is not shown: [04-log-workout-scrolled.png](screenshots/light/04-log-workout-scrolled.png) is the Log Workout page, which has a nav bar title and no large title.
- Capture: [02-workout.png](screenshots/light/02-workout.png), [04-log-workout-scrolled.png](screenshots/light/04-log-workout-scrolled.png).

## Patterns that span components

### Share card composer
- Card preview on the page background, page dots for templates, round action buttons (Background, Stories, More, Send to, Download, Link). Variants for records, leaderboard, workout photo, monthly report and calendar.
- Capture: [t62-share-card-composer.png](screenshots/pages/t62-share-card-composer.png), [t91-share-workout-template-1.png](screenshots/pages/t91-share-workout-template-1.png), [t109-share-card-calendar.png](screenshots/pages/t109-share-card-calendar.png).

### Onboarding questionnaire
- Segmented progress bar, radio rows with an accent selected border, ruler picker, wheel picker, checkbox list, "Recommended" outlined tag, Continue disabled until answered.
- Capture: [t36-trainer-q1-radio.png](screenshots/pages/t36-trainer-q1-radio.png) to [t47-trainer-q10-bottom.png](screenshots/pages/t47-trainer-q10-bottom.png).

## Gaps

What was not captured, or is only a guess. Treat these as open.

| Gap | Why |
|---|---|
| Font family | Unknown. A geometric sans with circular "o" and a two-storey "a", not SF Pro. `fontFamily.base` is "system". Line heights were not measured |
| Light sheets and the light wheel band | The detail pages and sheets were captured in dark only. The light values of `surface.sheet`, `surface.sheetFilter` and `surface.wheelBand` are Derived (white or the neutral fill) |
| Dark `button.disabledGlass` | No disabled Save in dark was captured. Borrowed from `switch.offTrack` |
| Values read in one theme only | `set.failure`, `set.drop`, the three medals, `accent.glass` and `state.live` were read in one theme; the other is Derived |
| Pressed and hover-like states | iPhone Mirroring gives clicks only; no pressed, highlighted or long-press state was seen |
| Scrolled content | Scrolling inside iPhone Mirroring moves a few points at a time. 24 captures show a page below its top (`04-log-workout-scrolled`, `d03-settings-mid` and the tree-pass `mid` and `bottom` pages); the rest of a long page between those positions is unseen |
| Loading states and the toast | The pass names a spinner (t24), skeleton (t98), web view loading (t130) and a "Link Copied" toast (t93), but none of those captures shows one (README, What to distrust) |
| Swipe-only content | Image carousel page 2 and share card templates 2 to 8 cannot be reached by clicking |
| Software keyboard | iPhone Mirroring takes typing from the Mac keyboard and hides the keyboard |
| Network error state | Turning off the phone's connection would also cut Mirroring |
| Motion | Stills only. No durations or easings, no timer-ring animation, no sheet transitions |
| Tab bar and nav bar geometry | System glass; heights and insets were not measured |
| Dynamic Type, iPad, landscape | Only the default text size on a 390 x 844 screen was captured |
| Pages opened but not acted on | Every `[action]` and `[external]` leaf in [page-tree.md](page-tree.md) |
| Third-party views | The iOS share sheet, photo picker and the help-centre web view are system or web content, not Hevy components |
