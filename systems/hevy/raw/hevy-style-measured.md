# Hevy: measured style reference

Captured 10 October 2026 from the shipped Hevy iOS app, version 3.1.16 (free account, light and dark mode), through iPhone Mirroring.
Device screen is 390 × 844 pt and the captures are 1 px = 1 pt, so sizes below are in points.

This is a record of what Hevy looks like, for reference while designing Alke. It contains no Hevy artwork or code.

## How to read the numbers

| Evidence level | Meaning |
|---|---|
| measured | Read straight from the PNG pixels. Surfaces are exact. |
| measured (text) | Text colour from the darkest anti-aliased pixel. True value is the same or slightly darker. |
| estimated | Derived (corner radius from the diagonal inset, font size from letter height). Treat as ±1 pt for size, ±2 pt for radius. |
| unknown | Not determinable from pixels. |

## Captures

All in [screenshots/light/](../screenshots/light/). Screen area is offset by (8, 38) px inside each PNG.

| File | Screen | Shows |
|---|---|---|
| [01-home.png](../screenshots/light/01-home.png) | Home feed | Workout summary card, stat row, social actions. Other users blurred. |
| [02-workout.png](../screenshots/light/02-workout.png) | Workout tab | Large title, secondary buttons, tip banner, routine cards |
| [03-log-workout.png](../screenshots/light/03-log-workout.png) | Logging a workout | Set table, warm-up rows, inputs, check boxes, glass Finish button |
| [04-log-workout-scrolled.png](../screenshots/light/04-log-workout-scrolled.png) | Same, scrolled | Collapsed header, second exercise |
| [05-workout-in-progress-bar.png](../screenshots/light/05-workout-in-progress-bar.png) | Workout tab | Minimised in-progress bar with discard icon |
| [06-discard-dialog.png](../screenshots/light/06-discard-dialog.png) | Confirm dialog | Destructive action, scrim |
| [07-new-routine-empty.png](../screenshots/light/07-new-routine-empty.png) | New routine | Empty state, disabled Save |
| [08-exercise-picker.png](../screenshots/light/08-exercise-picker.png) | Add exercise | Search, filters, two-line list rows |
| [09-exercise-picker-selected.png](../screenshots/light/09-exercise-picker-selected.png) | Add exercise | Selected rows, floating count button |
| [10-routine-editor.png](../screenshots/light/10-routine-editor.png) | Routine editor | Enabled Save, empty set inputs |
| [11-profile.png](../screenshots/light/11-profile.png) | Profile | Chips, dashboard tiles, empty chart |
| [12-explore.png](../screenshots/light/12-explore.png) | Explore | Program cards, filter pills |
| [13-settings.png](../screenshots/light/13-settings.png) | Settings | Grouped list, section headers |
| [14-empty-workout.png](../screenshots/light/14-empty-workout.png) | Empty workout | Empty state, secondary button with red label |
| [15-sets-completed-rest-timer.png](../screenshots/light/15-sets-completed-rest-timer.png) | Logging, sets ticked | Completed rows, rest timer bar, progress lines |
| [16-keyboard-input.png](../screenshots/light/16-keyboard-input.png) | Logging, field focused | Focus ring on weight input |
| [17-workout-settings-toggles.png](../screenshots/light/17-workout-settings-toggles.png) | Workout settings | Switches on/off, value + chevron rows, Pro badge in a row |

Dark mode captures are in [screenshots/dark/](../screenshots/dark/):

| File | Screen |
|---|---|
| [d01-theme-setting.png](../screenshots/dark/d01-theme-setting.png) | Theme setting (Dark) |
| [d02-settings-top.png](../screenshots/dark/d02-settings-top.png), [d03-settings-mid.png](../screenshots/dark/d03-settings-mid.png) | Settings list, top and lower half |
| [d04-units-segmented.png](../screenshots/dark/d04-units-segmented.png) | Units: segmented controls |
| [d05-notifications-switches.png](../screenshots/dark/d05-notifications-switches.png) | Notifications: grouped switches with helper text |
| [d06-privacy-switches-off.png](../screenshots/dark/d06-privacy-switches-off.png) | Privacy: switches off, value row |
| [d07-profile.png](../screenshots/dark/d07-profile.png) | Profile |
| [d08-statistics.png](../screenshots/dark/d08-statistics.png) | Statistics: body graph, Pro-locked row |
| [d09-muscle-distribution-chart.png](../screenshots/dark/d09-muscle-distribution-chart.png) | Radar chart and 2 × 2 stat cards (empty data) |
| [d10-workout.png](../screenshots/dark/d10-workout.png) | Workout tab |
| [d11-empty-workout.png](../screenshots/dark/d11-empty-workout.png) | Empty workout |
| [d12-exercise-picker-selected.png](../screenshots/dark/d12-exercise-picker-selected.png) | Exercise picker, one selected |
| [d13-log-workout.png](../screenshots/dark/d13-log-workout.png) | Logging, nothing ticked |
| [d14-sets-completed-timer-focus.png](../screenshots/dark/d14-sets-completed-timer-focus.png) | Completed sets, focus ring, rest timer |
| [d15-discard-dialog.png](../screenshots/dark/d15-discard-dialog.png) | Discard dialog |
| [d16-explore.png](../screenshots/dark/d16-explore.png) | Explore |
| [d17-home.png](../screenshots/dark/d17-home.png) | Home feed (other users blurred) |

Detail pages, sheets and menus (dark mode) are in [screenshots/pages/](../screenshots/pages/):

| File | Screen | Pattern |
|---|---|---|
| [p01-search.png](../screenshots/pages/p01-search.png) | Search | Underline tabs, user rows with Follow buttons (others blurred) |
| [p02-notifications-empty.png](../screenshots/pages/p02-notifications-empty.png) | Notifications | Empty state with icon, bold title, grey line |
| [p03-workout-detail.png](../screenshots/pages/p03-workout-detail.png) | Workout detail | Horizontal bar chart (Muscle Split), stat row (author blurred) |
| [p04-routine-detail.png](../screenshots/pages/p04-routine-detail.png) | Routine detail | Read-only set table with alternating row shading |
| [p05-action-sheet.png](../screenshots/pages/p05-action-sheet.png) | Routine menu | Bottom action sheet, destructive item in red |
| [p06-exercise-summary.png](../screenshots/pages/p06-exercise-summary.png) | Exercise: Summary | Underline tabs, hero image, metric chips |
| [p07-exercise-history.png](../screenshots/pages/p07-exercise-history.png) | Exercise: History | Past sessions as cards with set tables |
| [p08-exercise-howto.png](../screenshots/pages/p08-exercise-howto.png) | Exercise: How to | Numbered instruction list |
| [p09-exercise-leaderboard.png](../screenshots/pages/p09-exercise-leaderboard.png) | Exercise: Leaderboard | Rank medals, highlighted "You" row (others blurred) |
| [p10-filter-sheet-equipment.png](../screenshots/pages/p10-filter-sheet-equipment.png) | Equipment filter | Sheet with 2-column icon tile grid, footer buttons |
| [p11-filter-tile-selected.png](../screenshots/pages/p11-filter-tile-selected.png) | Equipment filter | Selected tile, live result count |
| [p12-filter-active.png](../screenshots/pages/p12-filter-active.png) | Picker, filtered | Active filter button in accent with clear (x) |
| [p13-filter-sheet-muscles.png](../screenshots/pages/p13-filter-sheet-muscles.png) | Muscle filter | Same grid with section label |
| [p14-create-exercise-form.png](../screenshots/pages/p14-create-exercise-form.png) | Create exercise | Form: photo circle, name field, rows with blue "Select" |
| [p15-exercise-type-list-tags.png](../screenshots/pages/p15-exercise-type-list-tags.png) | Exercise type | Option rows with small tag chips |
| [p16-set-type-sheet.png](../screenshots/pages/p16-set-type-sheet.png) | Set type | Sheet listing W / 1 / F / D with colours, red Remove |
| [p17-set-types-in-table.png](../screenshots/pages/p17-set-types-in-table.png) | Logging | All four set types in the table |
| [p18-rest-timer-wheel-picker.png](../screenshots/pages/p18-rest-timer-wheel-picker.png) | Rest timer | Wheel picker sheet with Done button |
| [p19-exercise-menu-sheet.png](../screenshots/pages/p19-exercise-menu-sheet.png) | Exercise menu | Action sheet with icons, red Remove |
| [p20-clock-timer-ring.png](../screenshots/pages/p20-clock-timer-ring.png) | Clock: Timer | Segmented control in a sheet, circular progress ring |
| [p21-clock-stopwatch.png](../screenshots/pages/p21-clock-stopwatch.png) | Clock: Stopwatch | Large digits, primary Start |
| [p22-program-detail.png](../screenshots/pages/p22-program-detail.png) | Program | Cover image, primary Save, icon attribute grid |
| [p23-level-sheet.png](../screenshots/pages/p23-level-sheet.png) | Level filter | Sheet with 3 icon tiles |
| [p24-calendar-month.png](../screenshots/pages/p24-calendar-month.png) | Calendar | Month grid, streak and rest-day pills, today in accent |
| [p25-measurements.png](../screenshots/pages/p25-measurements.png) | Measurements | Chart card, history list (values blurred) |
| [p26-exercise-library.png](../screenshots/pages/p26-exercise-library.png) | Exercises | Picker layout with chevrons |
| [p27-edit-profile-form.png](../screenshots/pages/p27-edit-profile-form.png) | Edit profile | Label/value form rows, section labels (private values blurred) |
| [p28-paywall.png](../screenshots/pages/p28-paywall.png) | Paywall | Feature list, 3 plan cards, selected plan with "Save" tab |
| [p29-language-single-choice.png](../screenshots/pages/p29-language-single-choice.png) | Language | Single-choice list with accent checkmark |
| [p30-sounds-value-rows.png](../screenshots/pages/p30-sounds-value-rows.png) | Sounds | Section labels, value + chevron rows |
| [p31-apple-health-connect.png](../screenshots/pages/p31-apple-health-connect.png) | Apple Health | Integration row with blue "Connect" text button |
| [p32-integrations-connected-states.png](../screenshots/pages/p32-integrations-connected-states.png) | Integrations | Connected (red "Disconnect") vs not connected (blue "Connect") |
| [p33-guide-article.png](../screenshots/pages/p33-guide-article.png) | Guide | Article with inline screenshots |
| [p34-faq-card-list.png](../screenshots/pages/p34-faq-card-list.png) | FAQ | Search field, list of separate rounded cards |
| [p35-about.png](../screenshots/pages/p35-about.png) | About | Centred logo, link list, version |

## Colour

| Role | Hex | Evidence | Where |
|---|---|---|---|
| Accent | `#0082F9` | measured | Primary buttons, selected chip, Unlock, check badge, links, active tab |
| Accent on glass | `#0090EE` | measured | Finish pill (system glass tints it) |
| Selected row tint | `#EBF6FF` | measured | Exercise picker selected rows |
| Neutral fill | `#F0F3F7` | measured | Secondary buttons, search field, filter buttons, unselected chips, tiles, set-number chip, check box |
| Grouped background | `#F5F9FA` | measured | Settings section bands and top area |
| Page | `#FFFFFF` | measured | All main screens |
| Card border | `#EAE9EA` | measured (text) | Routine cards, empty chart card (1 pt) |
| Row divider | `#F9F9F9` or lighter | measured (text) | List rows. Barely visible. |
| Text primary (headings) | `#000D1C` | measured (text) | Large titles. A navy-black, not pure black. |
| Text primary (body) | `#121A29` | measured (text) | Row titles, card titles, settings labels |
| Text secondary | `#7E8388` | measured (text) | Section labels, subtitles, column headers |
| Text tertiary | `#AAAFB2` to `#B7BABC` | measured (text) | Placeholders, "previous" values, empty-state icon |
| Warm-up | `#F1A232` | measured (text) | "W" set type |
| Success | `#00C457` | measured | Completed set check box |
| Completed row tint | `#E8F8E0` | measured | Background of a ticked set row |
| Completed set chip | `#DFEFD7` | measured | Set-number chip on a ticked row |
| Live indicator | `#35B433` | measured (text) | "Live Sync Active" dot |
| Destructive | `#EC574C` | measured (text) | Discard button text, trash icon |
| Tip banner | `#FFEB94` | measured | Inline hint ("Press and hold a routine to reorder") |
| Pro badge | `#FFD836` | measured | "PRO" pill |
| Scrim | black at about 70% | estimated | Behind dialogs (`#434343` over white) |

## Colour: dark mode

Layout, sizes and radii are identical to light mode. Only colour changes.

| Role | Light | Dark | Evidence (dark) |
|---|---|---|---|
| Page | `#FFFFFF` | `#000000` | measured |
| Raised surface (cards, neutral buttons, tiles, search, set chip, settings rows, dialog, timer bar) | `#F0F3F7` (white for cards) | `#1A1A1C` | measured |
| Raised surface, second level (buttons inside a dialog or timer bar) | `#F0F3F7` | `#272729` | measured |
| Grouped background (settings section bands) | `#F5F9FA` | `#000000` | measured |
| Input / container border | `#EAE9EA` | about `#1E1E1E` | measured (text) |
| Accent | `#0082F9` | `#0082F9` (unchanged) | measured |
| Focus ring | accent | about `#0077E4` | measured (text) |
| Selected row tint | `#EBF6FF` | `#001828` | measured |
| Success (completed check) | `#00C457` | `#36B434` | measured |
| Completed row tint | `#E8F8E0` | `#122A10` | measured |
| Completed set chip | `#DFEFD7` | `#11250D` | measured |
| Text primary | `#000D1C` / `#121A29` | `#FEFEFE` / `#F0F0F1` | measured (text) |
| Text secondary | `#7E8388` | about `#64666A` to `#696B6F` | measured (text) |
| Text tertiary | `#AAAFB2` to `#B7BABC` | about `#4A4A4A` to `#626468` | measured (text) |
| Destructive | `#EC574C` | about `#DE3F34` | measured (text) |
| Warm-up | `#F1A232` | about `#E59929` | measured (text) |
| Tip banner | `#FFEB94` | `#FFEB94` (unchanged) | measured |
| Pro badge | `#FFD836` | `#FFD836` (unchanged) | measured |

Two things flip between modes:

1. Cards change how they separate from the page. Light mode uses white cards with a 1 pt border on white. Dark mode drops the border and fills the card with `#1A1A1C` on black.
2. Settings change which layer is raised. Light mode has white rows on pale grey section bands. Dark mode has `#1A1A1C` rows on black bands.

Success green, destructive red and warm-up orange get slightly different values in dark rather than reusing the light hex.

## Typography

| Use | Size | Weight | Evidence |
|---|---|---|---|
| Large title ("Workout", "Home") | about 26 pt | bold | estimated |
| Nav bar title ("Settings", "Explore") | about 17 pt | regular/medium | estimated |
| Card and exercise titles | about 17 pt | semibold | estimated |
| Exercise name link (blue) | about 16 pt | semibold | estimated |
| Body, row titles, button labels | about 15 to 16 pt | regular/medium | estimated |
| Secondary lines (muscle group, exercise list in card) | about 15 pt | regular | estimated |
| Small labels ("Duration", "SET", "KG") | about 12 to 13 pt | regular, caps for column headers | estimated |

Font family: unknown. It is a geometric sans with circular "o" and a two-storey "a", and it isn't SF Pro.
The Behance concept board used Poppins, which is a similar shape, but that is the concept author's choice and not confirmed for the shipped app.

## Layout and spacing

| Thing | Value | Evidence |
|---|---|---|
| Screen side margin | 16 pt | measured |
| Two-up grid | 171 + 16 gap + 171 | measured |
| Full-width control width | 358 pt | measured |
| Card inner padding | about 18 pt (card at x 16, button inside at x 34) | measured |
| Exercise picker row | 80 pt tall, full bleed, image in a 56 pt white circle at x 16 | measured |
| Settings row | 60 pt tall, leading icon, label, chevron right | measured |
| Settings section header band | 54 pt tall | measured |
| Set table row | 47 pt pitch (36 pt controls + 11 pt gap) | measured |

## Components

| Component | Size (w × h) | Radius | Fill | Evidence |
|---|---|---|---|---|
| Primary button (full width) | 358 × 39 to 40 | about 10 | Accent, white label | measured, radius estimated |
| Secondary button, tall | 358 × 48 or 171 × 48 | about 10 | Neutral fill, dark label, leading icon | measured |
| Secondary button, short ("Add Set") | 358 × 41 | about 10 | Neutral fill | measured |
| Floating count button ("Add 2 exercises") | 356 × 38 | about 8 | Accent, pinned above home indicator | measured |
| Search field | 358 × 36 | about 8 | Neutral fill, grey placeholder, leading magnifier | measured |
| Filter button ("All Equipment") | 171 × 36 | about 8 | Neutral fill | measured |
| Chip / segmented pill | auto × 28 | full (14) | Selected: accent + white. Unselected: neutral fill + dark | measured |
| Small action ("Unlock") | 96 × 28 | about 8 | Accent | measured |
| Tip banner | 356 × 38 | about 8 | `#FFEB94`, close icon on right | measured |
| Pro badge | 40 × 18 | full | `#FFD836`, dark "PRO" | measured |
| Routine card | full width minus margins | about 10 | White with 1 pt `#EAE9EA` border, title, grey exercise list, "..." menu, primary button | measured |
| Set number chip | 36 × 36 | about 8 | Neutral fill, bold number (or orange "W") | measured |
| Weight / reps input | 73 × 33 | about 8 | White with light border, grey placeholder "-" | measured |
| Set check box | 36 × 36 | about 8 | Neutral fill, grey tick until done | measured |
| Selection badge | 16 × 16 circle | full | Accent with white tick, top right of row image | measured |
| Dialog buttons | 294 × 40 | about 10 | Neutral fill. Destructive label in red. | measured |
| Dashboard tile | 171 × 48 | about 10 | Neutral fill, icon + label | measured |
| Completed check box | 36 × 36 | about 8 | Success green, white tick | measured |
| Focused input | 73 × 33 | about 8 | White, accent border (about 1.5 pt) | measured |
| Rest timer bar | 390 × 91, docked at bottom | none | White. 3 pt accent progress line on top edge. Row of -15 (70 × 38, neutral), mm:ss digits (about 28 pt, heading colour), +15 (neutral), Skip (68 × 36, accent) | measured |
| Workout progress line | full width × 1 pt under nav bar | none | Accent | measured |
| Switch | about 62 × 26 | full | On: accent. Off: light grey track. | measured |
| Settings row with value | 60 pt tall | none | Label left, grey value + chevron right | measured |
| Segmented control (Units) | 358 × 50 container, 173 × 40 selected segment | about 10 | Container: page fill with 1 pt border. Selected: accent with white label. | measured (dark) |
| Stat card (Muscle distribution) | 2 × 2 grid, about 171 wide | about 10 | Raised surface with thin border, label, bold value, small trend line | observed (dark) |
| Radar chart | about 6 axes (Back, Chest, Core, Shoulders, Arms, Legs) | n/a | Grey hexagon grid, accent for current, grey for previous, legend below | observed (dark) |

## More components (from the detail pages, dark mode)

| Component | Detail | Evidence |
|---|---|---|
| Bottom sheet | Fill `#1A1A1C` (filter sheets slightly darker, `#161617`), grabber at top, centred title, dims the page | measured |
| Action sheet item | Leading icon, label. Destructive items (Delete, Remove) red with red icon. | observed |
| Filter tile | `#272729` on the sheet, round icon on the left, label. Selected: accent border. | measured |
| Sheet footer | Two buttons: neutral "Clear Filters" and accent "Show N results" with a live count | observed |
| Active filter button | Accent fill with white label and a clear (x) | observed |
| Wheel picker | System wheel, selected band `#232326`, accent Done button below | measured |
| Underline tabs | Text tabs across the top, active one in white with an accent underline, inactive grey | observed |
| Segmented control in sheet | Same as Units: accent selected segment | observed |
| Circular timer | Large thin accent ring with big digits inside, small "-15s"/"+15s" accent text either side | observed |
| Set type colours | Warm-up W orange, Failure F `#E13F34`, Drop D `#03B0F7` (a cyan, separate from the accent), Normal numbered in white | measured (text) |
| Horizontal bar chart | Accent bars of varying length with the percentage at the bar end, label above each | observed |
| Rank medals | Filled circles: gold `#F8C734`, silver `#A4A9AD`, bronze `#B05F2D`, then plain numbers | measured |
| Highlighted own row | Current user's row on a raised fill | observed |
| Calendar month | 7-column grid, weekday header, month title, today's date in accent, summary pills (week streak with flame, rest days with moon) | observed |
| Form row | Label left, value or blue "Select" below or right, chevron | observed |
| Tag chip | Small grey rounded tag ("Reps", "Kg", "Time") | observed |
| Plan card (paywall) | Three cards side by side, selected one with accent border and an accent "Save 33%" tab on top | observed |
| Text button | Blue "Connect", red "Disconnect", no background | observed |
| Card list (FAQ) | Each item its own rounded `#1A1A1C` card with chevron, gaps between cards | measured |

## Feedback, loading and growth patterns (from the full page tree)

The complete list of screens is in [page-tree.md](../page-tree.md). These are the patterns it added.

| Pattern | Detail | Capture |
|---|---|---|
| Toast | Small dark pill at the top, short text ("Link Copied"), disappears on its own | [t93](../screenshots/pages/t93-toast-link-copied.png) |
| Alert with one button | Centred card, short message, full-width accent "Ok". Used for validation ("Add an exercise") and confirmations ("Link added to clipboard") | [t75](../screenshots/pages/t75-finish-validation-alert.png), [t23](../screenshots/pages/t23-copy-link-alert.png) |
| Info dialog | Optional bold title, body text, accent "Okay"/"Ok". Opened from "?" icons | [t19](../screenshots/pages/t19-info-dialog.png), [t104](../screenshots/pages/t104-info-dialog-no-title.png) |
| Tooltip | Light pill pointing at a row ("Tap to select your gym") on first use | [t83](../screenshots/pages/t83-save-workout-tooltip.png) |
| Skeleton loading | Rounded grey placeholder cards while content loads | [t98](../screenshots/pages/t98-skeleton-loading-suggested.png) |
| Spinner loading | Small system spinner centred under the header | [t24](../screenshots/pages/t24-contacts-loading-spinner.png) |
| Empty states | Line icon, bold title or grey sentence, optional primary button | [t25](../screenshots/pages/t25-contacts-empty.png), [t27](../screenshots/pages/t27-search-no-results.png), [t81](../screenshots/pages/t81-superset-sheet-empty.png) |
| Paywall, full screen | Generic version plus feature-specific heroes (Graph History, Advanced Statistics, Warm-up Calculator) over the same three plan cards | [t18](../screenshots/pages/t18-paywall-contextual.png), [t95](../screenshots/pages/t95-paywall-advanced-stats.png) |
| Paywall, bottom sheet | Short "Upgrade to HEVY PRO" sheet with Continue and Not now, for locked fields | [t113](../screenshots/pages/t113-upsell-bottom-sheet.png) |
| Pro lock | Yellow PRO pill on rows and options, lock icon on form fields | [t17](../screenshots/pages/t17-period-sheet-pro-locked.png), [t112](../screenshots/pages/t112-log-measurements-bottom-locked.png) |
| Share card composer | Card preview on the page background, page dots for templates, round action buttons (Background, Stories, More, Send to, Download, Link). Variants for records, leaderboard, workout photo, monthly report and calendar | [t62](../screenshots/pages/t62-share-card-composer.png), [t91](../screenshots/pages/t91-share-workout-template-1.png), [t109](../screenshots/pages/t109-share-card-calendar.png) |
| Activity heatmap | Year and multi-year grids of small squares, accent for workout days | [t106](../screenshots/pages/t106-calendar-year-heatmap.png), [t107](../screenshots/pages/t107-calendar-multiyear-heatmap.png) |
| Comparison bars | Paired horizontal bars, accent for you and grey for the other person, red down arrow with percentage | [t16](../screenshots/pages/t16-compare-exercise.png) |
| Onboarding questionnaire | Segmented progress bar, radio rows with accent selected border, ruler picker, wheel picker, checkbox list, "Recommended" outlined tag, Continue disabled until answered | [t36](../screenshots/pages/t36-trainer-q1-radio.png) to [t47](../screenshots/pages/t47-trainer-q10-bottom.png) |

## System chrome (iOS 26)

Hevy uses the iOS 26 glass look for chrome. The tab bar is a floating glass capsule with three items (Home, Workout, Profile), and the active item gets a lighter glass lozenge plus accent tint.
Nav bar buttons are glass pills: Cancel (accent text), Save (accent fill when enabled, grey `#B8BABE` glass when disabled), Finish (accent fill).
These come from the system in SwiftUI, so Alke gets them by using standard components on iOS 26.

## States captured

| State | Where |
|---|---|
| Empty | New routine ("Get started by adding an exercise to your routine."), profile chart ("No data in time period") |
| Disabled | Save button with no exercises |
| Selected | Exercise rows: tinted row, blue badge, floating "Add N exercises" |
| In progress | Minimised workout bar above tab bar: green dot, elapsed time, current exercise, red trash |
| Destructive confirm | Centred dialog: question, red "Discard Workout", neutral "Cancel" |
| Hint | Yellow tip banner, dismissible |
| Set types | Warm-up "W" in orange, working sets numbered |
| Completed set | Whole row tinted green, values turn bold and dark, check box fills green |
| Rest timer running | Bottom bar with countdown and -15 / +15 / Skip, thin accent progress line shrinking |
| Focus | Input gets an accent border, placeholder value stays grey |

Loading, validation and toast states were captured later in the tree pass (see "Feedback, loading and growth patterns" above). Still not captured: network error.

Pages not opened are listed, with reasons, at the end of [page-tree.md](../page-tree.md).
Scrolling inside iPhone Mirroring only moves a few points at a time, so long pages were captured from the top only.
The software keyboard can't be captured: iPhone Mirroring takes typing from the Mac keyboard and hides it.

## Patterns

- One accent colour does all the work. Everything else is navy-black text on white, with one pale grey-blue fill (`#F0F3F7`) for anything tappable that isn't primary.
- Borders are rare. Separation comes from the grey fill, 16 pt margins and pale dividers. Routine cards and inputs are the exceptions.
- Corners are small and consistent: about 8 for short controls, about 10 for buttons and cards, full round for chips and badges.
- Lists are dense: 80 pt for two-line rows with an image, 60 pt for settings.
