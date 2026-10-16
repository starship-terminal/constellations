# Duolingo: focus states, measured live

Captured on 2026-10-17 in the signed-in web app (free account) by pressing the Tab key in the built-in browser pane and reading the focused element's computed styles after each press, against the same element at rest ([tools/capture/live-measure.js](../tools/capture/live-measure.js), data in [raw/2026-10/live-measurements.json](../raw/2026-10/live-measurements.json)).

Duolingo draws no focus ring. Its stylesheets set `outline:none` on every element (`*,:after,:before,button,button:focus,input,textarea`) and on every web-ui button (`._7jW2t:not(._1ZhE5)`), and none of the 20 chunks the app loaded has a `:focus-visible` rule ([raw/2026-10/css-evidence.json](../raw/2026-10/css-evidence.json)). Every control below matched `:focus-visible`; only text fields change visibly, by turning their 2px border `border.focus`. Menu rows in the courses dropdown get a `surface.subtle` (polar) fill on `:focus` and `:focus-within`, from CSS only (the menu was not opened by keyboard). `core.focusRing.width` is 0px for that reason.

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

33 Tab presses. Not reached by keyboard: tabs (Characters, Profile), the MORE and courses menus, dialog buttons other than the friend-streak dialog's SEE INVITES (Tab-focused live in light: it matched `:focus-visible` and kept its face and lip, with no ring; that press was read before the log started, so it has no row) and the quit dialog (its buttons were focused by script, which does not set `:focus-visible`), checkboxes in the lesson report form (native inputs, global `outline:none`).
