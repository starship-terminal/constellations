# Duolingo: focus states, measured live

Captured on 2026-10-17 in the signed-in web app (free account) by pressing the Tab key in the built-in browser pane and reading the focused element's computed styles after each press, against the same element at rest ([tools/capture/live-measure.js](../tools/capture/live-measure.js), data in [raw/2026-10/live-measurements.json](../raw/2026-10/live-measurements.json)).

Duolingo draws no focus ring on its controls. Its stylesheets set `outline:none` on every element (`*,:after,:before,button,button:focus,input,textarea`) and on every web-ui button (`._7jW2t:not(._1ZhE5)`), and none of the 20 chunks the learn page loaded has a `:focus-visible` rule; the one that does, `pathSections`, rings the Math course's section-group rows (second pass, below) ([raw/2026-10/css-evidence.json](../raw/2026-10/css-evidence.json)). Every control below matched `:focus-visible`; only text fields change visibly, by turning their 2px border `border.focus`, plus the one ring below. The one other visible keyboard state is the courses dropdown: its rows get a `surface.subtle` (polar) fill on `:focus` and `:focus-within`, read in CSS and confirmed live in the second pass (arrow keys move focus between rows). `core.focusRing.width` is 0px for that reason.

| # | Page | Control | `:focus-visible` | What changed on focus |
| --- | --- | --- | --- | --- |
| 1 | learn-light | Logo link | yes | outline-offset 1px with outline-style none (no ring drawn) |
| 2 | learn-light | Sidebar nav item (link) | yes | outline-offset 1px with outline-style none (no ring drawn) |
| 3 | learn-light | Sidebar nav item (link) | yes | outline-offset 1px with outline-style none (no ring drawn) |
| 4 | learn-light | Sidebar nav item (link) | yes | outline-offset 1px with outline-style none (no ring drawn) |
| 5 | learn-light | Sidebar nav item (link) | yes | outline-offset 1px with outline-style none (no ring drawn) |
| 6 | learn-light | Sidebar nav item (link) | yes | outline-offset 1px with outline-style none (no ring drawn) |
| 7 | learn-light | Sidebar nav item (link) | yes | outline-offset 1px with outline-style none (no ring drawn) |
| 8 | learn-light | Sidebar nav item (link) | yes | outline-offset 1px with outline-style none (no ring drawn) |
| 9 | learn-light | Sidebar MORE item | yes | no computed change |
| 10 | learn-light | Link button (TRY CHESS) | yes | outline-offset 1px with outline-style none (no ring drawn) |
| 11 | settings-profile-dark | Icon button (avatar edit) | yes | outline-offset 1px with outline-style none (no ring drawn) |
| 12 | settings-profile-dark | Text field (text) | yes | input unchanged; its wrapper was not read in this first pass (the second pass on the same page reads it) |
| 13 | settings-profile-dark | Text field (text) | yes | input unchanged; its wrapper was not read in this first pass (the second pass on the same page reads it) |
| 14 | settings-profile-dark | Text field (text) | yes | input unchanged; its wrapper was not read in this first pass (the second pass on the same page reads it) |
| 15 | settings-profile-dark | Text field (text) | yes | input unchanged; its wrapper was not read in this first pass (the second pass on the same page reads it) |
| 16 | settings-profile-dark | Text field (text) | yes | input unchanged; its wrapper was not read in this first pass (the second pass on the same page reads it) |
| 17 | settings-profile-dark | Text link | yes | outline-offset 1px with outline-style none (no ring drawn) |
| 18 | settings-profile-dark | Text link | yes | outline-offset 1px with outline-style none (no ring drawn) |
| 19 | settings-profile-dark | Text field (text) | yes | wrapper border -> `border.focus` (rgb(73, 192, 248)) |
| 20 | settings-profile-dark | Text field (password) | yes | wrapper border -> `border.focus` (rgb(73, 192, 248)) |
| 21 | settings-profile-dark | Text field (password) | yes | wrapper border -> `border.focus` (rgb(73, 192, 248)) |
| 22 | settings-account-dark | Switch | yes | no computed change |
| 23 | settings-account-dark | Switch | yes | no computed change |
| 24 | settings-account-dark | Select (theme) | yes | no computed change |
| 25 | settings-account-dark | Switch | yes | no computed change |
| 26 | settings-account-dark | Radio card | yes | no computed change |
| 27 | settings-account-dark | Switch | yes | no computed change |
| 28 | lesson-dark | Icon button (speaker) | yes | no computed change |
| 29 | lesson-dark | Hint token (opens the word tooltip) | yes | no computed change |
| 30 | lesson-dark | Hint token (opens the word tooltip) | yes | no computed change |
| 31 | lesson-dark | Word-bank tile (outline button) | yes | no computed change |
| 32 | lesson-dark | Word-bank tile (outline button) | yes | no computed change |
| 33 | lesson-dark | Outline button (SKIP) | yes | no computed change |

33 Tab presses. The friend-streak dialog's SEE INVITES was also Tab-focused live in light (it matched `:focus-visible` and kept its face and lip, with no ring); that press was read before the log started, so it has no row.

## Second pass: menus, profile, lesson footer, dialogs

Same method, dark theme, 1440x900 ([tools/capture/tab-pass.js](../tools/capture/tab-pass.js), data in [raw/2026-10/live-measurements-2.json](../raw/2026-10/live-measurements-2.json)). Reads taken after a script `focus()` call are left out, so every row is a key press.

| # | Page | Key | Control | `:focus-visible` | What changed on focus |
| --- | --- | --- | --- | --- | --- |
| 1 | characters-dark | Tab | Link button (outline) | yes | outline-offset 1px with outline-style none (no ring drawn) |
| 2 | characters-dark | Tab | Link button (filled) | yes | outline-offset 1px with outline-style none (no ring drawn) |
| 3 | characters-dark | Tab | Outline button | yes | no computed change |
| 4 | characters-dark | Tab | Text link | yes | outline-offset 1px with outline-style none (no ring drawn) |
| 5 | characters-dark | Tab | Text link | yes | outline-offset 1px with outline-style none (no ring drawn) |
| 6 | profile-dark | Tab | Text link | yes | outline-offset 1px with outline-style none (no ring drawn) |
| 7 | profile-dark | Tab | Text link | yes | outline-offset 1px with outline-style none (no ring drawn) |
| 8 | profile-dark | Tab | Tooltip trigger (div with tabindex) | yes | no computed change |
| 9 | profile-dark | Tab | Outline button | yes | no computed change |
| 10 | profile-dark | Tab | Text link | yes | outline-offset 1px with outline-style none (no ring drawn) |
| 11 | profile-dark | Tab | Text link | yes | outline-offset 1px with outline-style none (no ring drawn) |
| 12 | profile-dark | Tab | Tooltip trigger (div with tabindex) | yes | no computed change |
| 13 | profile-dark | Tab | Outline button | yes | no computed change |
| 14 | learn-dark-more-menu | Tab | MORE menu row (link) | yes | no computed change |
| 15 | learn-dark-more-menu | Tab | MORE menu row (button) | yes | no computed change |
| 16 | learn-dark-more-menu | Tab | MORE menu row (button) | yes | no computed change |
| 17 | learn-dark-more-menu | Tab | MORE menu row (button) | yes | no computed change |
| 18 | learn-dark-top-bar | Tab | Top-bar stat button (streak / gems / hearts) | yes | no computed change |
| 19 | learn-dark-top-bar | Tab | Top-bar stat button (streak / gems / hearts) | yes | no computed change |
| 20 | learn-dark-top-bar | Tab | Top-bar stat button (streak / gems / hearts) | yes | no computed change |
| 21 | learn-dark-courses-menu | Tab | Courses menu row (menuitem) | yes | no computed change |
| 22 | learn-dark-courses-menu | ArrowDown | Courses menu row (menuitem) | yes | fill rgba(0, 0, 0, 0) -> rgb(32, 47, 54) (`surface.subtle`, dark polar) |
| 23 | learn-dark-courses-menu | ArrowDown | Courses menu row (menuitem) | yes | fill rgba(0, 0, 0, 0) -> rgb(32, 47, 54) (`surface.subtle`, dark polar) |
| 24 | lesson-dark | Tab | Icon button (speaker) | yes | no computed change |
| 25 | lesson-dark | Tab | Hint token (opens the word tooltip) | yes | no computed change |
| 26 | lesson-dark | Tab | Hint token (opens the word tooltip) | yes | no computed change |
| 27 | lesson-dark | Tab | Word-bank tile (outline button) | yes | no computed change |
| 28 | lesson-dark | Tab | Word-bank tile (outline button) | yes | no computed change |
| 29 | lesson-dark | Tab | Word-bank tile (outline button) | yes | no computed change |
| 30 | lesson-dark | Tab | Word-bank tile (outline button) | yes | no computed change |
| 31 | lesson-dark | Tab | Word-bank tile (outline button) | yes | no computed change |
| 32 | lesson-dark | Tab | Outline button (SKIP) | yes | no computed change |
| 33 | lesson-dark | Tab | Filled button (CHECK / CONTINUE) | yes | no computed change |
| 34 | lesson-dark-footer-correct | Tab | Footer feedback button (Too easy / Too difficult) | yes | no computed change |
| 35 | lesson-dark-footer-correct | Tab | Footer feedback button (Report) | yes | no computed change |
| 36 | lesson-dark-footer-correct | Tab | Filled button (CHECK / CONTINUE) | yes | no computed change |
| 37 | lesson-dark-quit-dialog | Tab | Filled button | yes | control unchanged; the dialog's fade-in (ancestor opacity 0 -> 1) ended between the rest read and the press |
| 38 | lesson-dark-quit-dialog | Tab | Text button (END SESSION) | yes | control unchanged; the dialog's fade-in (ancestor opacity 0 -> 1) ended between the rest read and the press |
| 39 | lesson-dark-quit-dialog | Tab | Filled button | yes | control unchanged; the dialog's fade-in (ancestor opacity 0 -> 1) ended between the rest read and the press |
| 40 | lesson-dark-footer-correct | Tab | Icon button (quit X) | yes | no computed change |
| 41 | lesson-dark-footer-correct | Tab | Icon button (lesson settings gear) | yes | no computed change |
| 42 | lesson-dark-footer-correct | Tab | Footer feedback button (Too easy / Too difficult) | yes | no computed change |
| 43 | lesson-dark-footer-correct | Tab | Footer feedback button (Too easy / Too difficult) | yes | no computed change |
| 44 | lesson-dark-report-form | Tab | Checkbox (native input) | yes | outline-offset 1px with outline-style none (no ring drawn) |
| 45 | lesson-dark-report-form | Tab | Checkbox (native input) | yes | outline-offset 1px with outline-style none (no ring drawn) |
| 46 | sections-math-dark | Tab | Segmented tab (Grades / Topics) | yes | no computed change |
| 47 | sections-math-dark | Tab | Segmented tab (Grades / Topics) | yes | no computed change |
| 48 | sections-math-dark | Tab | Section-group row (Math section picker, role=button) | yes | 2px solid outline in rgb(73, 192, 248) (`border.focus`, macaw), offset -2px (drawn inside the row) |
| 49 | sections-math-dark | Tab | Section-group row (Math section picker, role=button) | yes | 2px solid outline in rgb(73, 192, 248) (`border.focus`, macaw), offset -2px (drawn inside the row) |
| 50 | sections-math-light | Tab | Section-group row (Math section picker, role=button) | yes | 2px solid outline in rgb(28, 176, 246) (`border.focus`, macaw), offset -2px (drawn inside the row) |
| 51 | sections-math-light | Tab | Section-group row (Math section picker, role=button) | yes | 2px solid outline in rgb(28, 176, 246) (`border.focus`, macaw), offset -2px (drawn inside the row) |

51 key presses.

The one ring Duolingo draws: the section-group rows of the Math course's section picker (`._3DGr8:focus-visible{outline:2px solid rgb(var(--color-macaw));outline-offset:-2px}`, the only `:focus-visible` rule in the app's CSS), focused by Tab in both themes:

| Dark | Light |
| --- | --- |
| ![Math section-group row focused, dark](crops/focus-section-row-dark.png) | ![Math section-group row focused, light](crops/focus-section-row-light.png) |

The crops are from the browser pane at its own scale (not 2x).

## Reachability

What the keyboard can and cannot reach, from the two passes:

- characters-dark: Hiragana / Katakana / Kanji underline tabs are divs with no tabindex: focus() leaves document.activeElement on body, so Tab never reaches them.
- profile-dark: Following and Followers tabs are li elements with no tabindex, so Tab never reaches them.
- lesson-dark-footer-correct: Enter with Report focused advanced to the next challenge: the lesson binds Enter to Continue globally, so the report form cannot be opened by Enter.
- lesson-dark-quit-dialog: focus trap: Tab cycles Keep learning and End session only; focus starts on body.
- lesson-dark-report-form: native checkbox; Tab stays on it while Submit is disabled (focus trap inside the report popover); popover closes when focus leaves.
- sections-math: Math course section picker: the section rows inside an open grade group (div.g62F5) have no tabindex, so Tab moves from one grade header to the next.
- MORE menu (sidebar): Enter on the trigger opens it; Tab then walks its four rows (Duolingo English Test, Settings, Help, Log out) with no visible change on any of them.
- Courses menu (top bar): opens on hover. Enter on its trigger did not open it, and the next Tab presses moved on to the stat buttons. With the menu open, Tab lands on the current course row (the only row with tabindex 0) and ArrowDown moves between rows (roving tabindex).
- Quit dialog: opens only once the lesson has progress (with none, the X leaves at once).
