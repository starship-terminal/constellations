# Coursera design reference

A token set and component reference for Coursera's web product, for rebuilding our course list and course detail pages in the style of a real course platform. It was read from coursera.org on 2026-09-29: the public catalogue pages headless (home, search, browse, course, specialization, certificate and the Explore topic page with its compact course cards, chip rows and scrolling card rows), and the signed-in learner pages from one learner's account with one enrolled course, all at 1440 wide and (for public pages) 390 wide.

The earlier references (Duolingo, Brilliant, NotebookLM) are learning apps. Coursera is the one built around courses: a catalogue of product cards, a course landing page with modules and outcomes, and a course home where a learner works through modules, lessons and items with deadlines and grades. Those last screens map onto our `/courses` and course pages most directly.

| File | What it is |
|---|---|
| [tokens.json](tokens.json) | W3C DTCG tokens (every length is a single px or rem `dimension`, shorthands are split per side, an em letter-spacing is a `number` of ems, shadows are `shadow` layers) in Tokens Studio's multi-set layout: `core` (401: seven 15-step colour ramps plus ink and paper alpha ramps, one font family, 28 type styles with their breakpoint sizes, spacing, radius, breakpoints, motion, layout grids, component sizes, the focus ring) and `light` and `dark` (101 and 95: the semantic colour roles, elevation and component colours), plus `$themes`. Every token carries `$extensions.source`. |
| [style-guide.html](style-guide.html) | One self-contained page that renders every token and the course components with the real values, each state side by side, in both themes (toggle top right, defaults to the system theme). |
| [components.md](components.md) | The discovery list of every page and view, one entry per component with crops of the real product, the icon index, and the Gaps. |
| [components/crops/](components/crops) | 742 element screenshots: 352 from the public pages and 390 from the signed-in pages (`signed-in/`). |
| [icons/](icons) | 58 SVGs lifted from the public pages, named by role in [icons/INDEX.tsv](icons/INDEX.tsv). Coursera's property, kept for reference only. |
| [screenshots/](screenshots) | 90 `{page}-{theme}-{state}.png` captures. `learn-*` and `my-learning-*` are the signed-in pages, `mobile-*` are 390 wide. Viewport shots are 2x, `*-full` shots 1x. |
| [raw/](raw) | The unprocessed readings: every `--cds-*` variable by selector and media query with its computed value at four widths and both schemes (`css-vars.json`), per-component computed styles for the public pages (`measurements.md`, `components-computed.json`) and the signed-in pages (`measurements-signed-in.md`, `components-signed-in.json`), the component values the token file takes (`component-tokens.json`), per-page layout notes (`pages.md`), and the redacted DOM snapshots of the signed-in pages (`snapshots/`). |
| [tools/](tools) | The three builders and the capture kit. See Rebuild. |

## How the values were read

Coursera styles its product with CDS, the Coursera Design System, on Emotion. CDS writes its tokens onto `:root` as 386 custom properties (`--cds-color-interactive-primary`, `--cds-spacing-200`, `--cds-border-radius-100`, `--cds-typography-title-large`), and the signed-in course pages use exactly the same 386. So the palette, semantic colours, spacing, radii, type scale and elevation in the token file all trace to a named variable. The larger type styles shrink below 1024 and 600 wide through media-query overrides; each type token records its desktop size and those smaller sizes.

Every colour is a `light-dark(<light>, <dark>)` pair, and the ramps flip in the dark scheme: `blue.800` paints as `blue.300` does in light. `core.palette` holds each ramp's light values, and the light and dark sets alias the step each role paints in that scheme. Coursera does not offer learners a dark theme on any page captured (it ignores `prefers-color-scheme`); the dark set and the dark screenshots come from forcing the scheme on the page, so treat them as what CDS defines, not as a shipped design.

Component values are computed styles read per state with Playwright. Hover used the pointer, focus-visible used a real keyboard Tab, and pressed was either held with the mouse (signed-in) or forced through DevTools (public), so no button was ever clicked for real. Where CDS draws its focus ring from a class its own script adds on keyboard focus, the measurement adds that class and labels the state `focus-visible-cds`.

The signed-in pages were captured without handing the account to a headless browser. In the signed-in tab, [snapshot.js](tools/capture/signed-in/snapshot.js) copied each page's DOM with every stylesheet inlined from the CSSOM (Emotion inserts rules with `insertRule`, so the `<style>` tags alone are empty), stripped the scripts, kept the current video frame, cut every presigned URL back to its path (a reading's narration audio is served from S3 with a credential in the query), and replaced the learner's name, avatar initials, institution and programme with "Learner", "L", "Example University" and "Example Program". A later pass (2026-10-11) scrubbed what that missed, in the snapshots and in every file measured from them: the career goal and weekly commitment, the other enrolled and completed courses (now "Example Course 1" to "9", "Another Course", "Completed Course A" to "C", with their partners and slugs), start, submission, due and completion dates, the time zone, certificate ids, signed thumbnail URLs and ad-tracking ids. The crops and screenshots were not retaken. On 2026-10-11 the career goal, weekly commitment, enrolled course titles, dates and due times were painted out of them with solid fills (`python3 tools/redact_images.py apply systems/coursera --rules tools/redact-rules/coursera.json --patterns ~/.design-systems/cleanup-redact.json`), and the 17 crops that showed only a goal, the calendar, a completed-course card or the enrolled course list were deleted, so [components.md](components.md) says no crop was saved for those entries. Grades-table due dates and the one enrolled public course title in the `learn-*` shots stay. The values to replace come from a redaction file kept outside the repository (`~/.self-learn/coursera-redact.json` by default, shaped like [redact.example.json](tools/capture/signed-in/redact.example.json)), since the file itself names the learner. [unsnap.py](tools/capture/signed-in/unsnap.py) refuses a snapshot in which any redacted string or signing parameter survived. The snapshots were then rendered and measured headless at 2x; CSS hover and focus rules still apply to a static copy, but anything that needs JavaScript (menus, the AI chat panel, toggling an accordion) could only be measured in the state it was captured in. The discussion forums, messages and notes pages were not captured, since they hold other people's posts or the learner's own notes.

Screenshots are stored as 256-colour PNGs to keep the repo small. Flat UI colours are exact; read values from the tokens, not the images.

## Fonts

| Family | Weights | Used for |
|---|---|---|
| Source Sans Pro | 400, 600, 700, with italics | Every UI string. Coursera serves Source Sans 3 under this family name |
| Boutros Coursera | | Arabic script only |

Source Sans 3 is open source, so the style guide loads it from Google Fonts and needs no local font folder. Letter-spacing is 0 on the type tokens CDS uses today; the older `title*` and `display*` styles carry -0.1px and -0.2px, and the tracking some components add is in `core.tracking`.

## Do and don't

1. **Do keep the filled blue button for the step that moves the learner on.** Resume, Go to next item, Try again, Enroll for free and Add to LinkedIn are `blue.800` (#0056d2) fills; the actions beside them are an outlined button, a ghost button or bold blue text (View submission, Help me practice, Save note, View certificate). Apart from the search submit, there is one such action per screen or per row, even where the page repeats it (the reading page shows Go to next item twice). See [learn-assignment-light-submitted](screenshots/learn-assignment-light-submitted.png), [learn-reading-light-default](screenshots/learn-reading-light-default.png) and [my-learning-light-completed](screenshots/my-learning-light-completed.png).
2. **Do separate learner panels by fill and catalogue cards by a hairline.** Course home, grades and the item pages set white 16-radius cards on the `grey.25` (#f2f5fa) ground with no border or shadow. Product and compact cards on search and Explore carry a 1px `grey.200` (#c1cbdb) border and gain a shadow only on hover; the stats card over the course hero is the one card that rests on a shadow (`0 8px 16px` at 20%). See [learn-home-light-module-in-progress](screenshots/learn-home-light-module-in-progress.png), [search-light-card-hover](screenshots/search-light-card-hover.png) and [course-light-default](screenshots/course-light-default.png).
3. **Do put an item's facts on one grey line joined by dots.** Item rows read "Video • 5 min" in 14/20 `grey.750` (#48546e) under the title, product cards read "4.9 (39K) · Beginner · Specialization · 1 - 3 Months" in 12/18 of the same grey, and module headers read "Week 1 • 7 hours to complete". See [learn-home-light-module-not-started](screenshots/learn-home-light-module-not-started.png), [search-light-default](screenshots/search-light-default.png) and [course-light-tab-modules](screenshots/course-light-tab-modules.png).
4. **Do mark the current item with a pale tint and a heavier label.** The current module, item and sidebar link sit on a `blue.25` (#f0f6ff) tint with the label at 600; the selected course tab is a `grey.25` tint with underlined blue text, and the selected My Learning tab is black 600 over a 4px black bar. The only filled selected state is the Explore chip, and it is near-black `grey.950` (#1c2026), not blue. See [item-row-current](components/crops/signed-in/item-row-current.png), [tab-selected](components/crops/tab-selected.png), [ml-tabs-default](components/crops/signed-in/ml-tabs-default.png) and [explore-chip-row-default](components/crops/explore-chip-row-default.png).
5. **Do keep green for finished work.** Green appears as the `green.750` (#197d12) check on completed items and courses, the "Completed" label beside Go to next item, and the "Right on schedule!" callout on `green.50` (#e0f4dc). Progress still under way is not green: the My Learning bar fills in `purple.750` (#6f29e5). See [learn-home-light-module-in-progress](screenshots/learn-home-light-module-in-progress.png), [learn-reading-light-default](screenshots/learn-reading-light-default.png) and [my-learning-light-default](screenshots/my-learning-light-default.png).
6. **Don't copy the mixed casing of button labels.** Title Case and sentence case sit on one screen: "Join for Free" above "Enroll for free" on the course page, "Purchase Certificate" a row below "View certificate" on My Learning. Use sentence case throughout. See [course-light-default](screenshots/course-light-default.png) and [my-learning-light-completed](screenshots/my-learning-light-completed.png).

## Rebuild

```bash
python3 tools/build_tokens.py
```

```bash
python3 tools/build_style_guide.py
```

```bash
python3 tools/build_components_md.py
```

`build_tokens.py` reads `raw/css-vars.json` and `raw/component-tokens.json` and writes `tokens.json`. `build_style_guide.py` renders `style-guide.html` from `tokens.json` and `tools/style-guide.template.html`, turning every token into a CSS variable so the page cannot drift from the file. `build_components_md.py` writes `components.md` from the measurement files. All three are deterministic: re-running them on this commit reproduces their files byte for byte. Edit the raw inputs or the builders, never the generated files.

`tools/capture/` holds the kit the captures came from, written for one session. `measure.mjs` takes page names, so `node tools/capture/measure.mjs explore` re-reads only the Explore page (it merges into `raw/components-computed.json`, then run `node tools/capture/build-measurements.mjs`), and `public.mjs light explore,mobile-explore` re-takes its three screenshots. The Playwright scripts take `PLAYWRIGHT` as the path to a Playwright install when `playwright` is not resolvable from where they run: `vars.mjs` (the variable dump), `public.mjs` and `layout.mjs` (public screenshots and grid measurements), `icons.mjs`, `measure.mjs` with `lib.mjs` and `build-measurements.mjs` (public components), and `quantize.py`. `tools/capture/signed-in/` holds the snapshot helper, `unsnap.py`, `render.mjs` and the signed-in `measure.mjs`.

## Use in Figma

Import `tokens.json` with Tokens Studio and choose the Light theme; Dark is available but is not a theme Coursera ships. Set the font to Source Sans 3.

The course home is the screen to get right. It sits on a `grey.25` (#f2f5fa) ground under a 64px bar, in three white cards with a 16 radius and no border or shadow: a 300px sidebar, a 716px module column and a 360px rail, 16 apart. An item row is 60 tall with a 20px status icon, a 16/24 title and a 14/20 grey meta line, and the current item carries a `blue.25` tint and a 36px primary Resume button. Buttons are 8-radius rectangles in `blue.800` (#0056d2) that go darker blue on hover and purple when pressed, with no transition. Catalogue cards have a 1px `grey.200` border, a 16 radius and gain a shadow on hover. Everything the capture could not reach is listed under Gaps in [components.md](components.md#gaps).
