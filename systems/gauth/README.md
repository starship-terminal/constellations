# Gauth design reference

A token set and component reference for Gauth's web product, for building self-learn's courses, lessons and tutor in the style of a real AI learning app. It was read from www.gauth.com on 2026-10-04, signed out, in headless Chromium at 1440 wide and 390 wide: the Homework home, the Gauth Academy catalogue (Science Labs, Math Curriculum, History Signature, My Course and the Create a Course dialog), a math unit page, three lesson players (a science canvas, a math lesson and a history lesson), Atlas with a story page, and Insights. It was refreshed on 2026-10-17, again signed out, to close the gaps in the library's scorecard: the Sign in and Gauth PLUS dialogs, the plans page and its table, the footer's language select, the blog's pagination, the science lesson's tooltip, Playback speed menu and answered check-in, disabled states, z-index layers, reduced motion, and the patterns in [patterns.md](patterns.md). The science lesson, the Atlas landing and the new pages were measured again on that date; the rest keeps its 2026-10-04 readings.

The earlier references (Duolingo, Brilliant, NotebookLM, Coursera) each cover part of what self-learn does. Gauth covers most of it in one product: a course catalogue with an AI course builder, unit pages with a path of topics, narrated lessons with a tutor beside them, AI-generated visual stories, and a question-first home.

| File | What it is |
|---|---|
| [tokens.json](tokens.json) | W3C DTCG tokens (every length is a single px `dimension`, gradients are `gradient` stops with the angle in `$extensions`, shadows are `shadow` layers, a press scale, z-index or column count is a `number`) in Tokens Studio's multi-set layout: `core` (381: Gauth's named colours and the literal ones it paints, grouped by where they belong, nine font families, the `--lesson-font-size-*` scale, 56 composite type styles, a 4px spacing scale with the off-grid values kept apart, radius, border widths, sizes, layout widths, grid columns, breakpoints, z-index layers, durations including the reduced-motion one, easings, press scales, focus) and `light` (161: background, text, border, action (near-black primary and brand-red accent) and status roles, gradients, four elevation levels over the per-component shadows, and component colours), plus `$themes`. There is no dark set; see How the values were read. Every token carries `$extensions.source`. |
| [style-guide.html](style-guide.html) | One self-contained page that renders every token and the main components (sidebar, top bar buttons, Academy catalogue, unit page, the three lesson players, dialogs, Homework home, Atlas, Insights tabs) with the real values, states side by side. |
| [components.md](components.md) | The discovery list of every page and view, the 19 checklist components mapped to entries (17 captured), one entry per component (199) written in tokens with crops of the real product, the shared values (focus, pressed, motion, layout grid, card shapes), the icon index, and the Gaps. |
| [patterns.md](patterns.md) | How the components combine: app shell, forms and validation, empty, loading and error states, feedback, search and filtering, data display, onboarding and the upsell, each with its components, layout and screens; destructive confirmation is not present signed out. |
| [components/crops/](components/crops) | 369 element screenshots, `{component}-{state}.png`, at 2x (large ones halved). |
| [icons/](icons) | 99 SVGs lifted from the pages, named by role in [icons/INDEX.tsv](icons/INDEX.tsv). Gauth's property, kept for reference only. |
| [screenshots/](screenshots) | 56 `{page}-light-{state}.png` captures. Desktop shots are 1440 x 900 at 1x, `-full` shots whole pages at 1x, `mobile-*` shots 390 x 844 at 2x. |
| [raw/](raw) | The unprocessed readings: every custom property the pages declare, sorted by owner, with font faces, loaded fonts and the dark-theme checks (`css-vars.json`); per-component computed styles (`components-computed.json`, and `measurements.md` built from it); the token tree the builder reads (`component-tokens.json`); page geometry at four widths (`layout.json`) and the layout notes written from it (`pages.md`); the reduced-motion rules and what they change, the z-index layers and the brand colour evidence (`foundations.json`). |
| [tools/](tools) | The three builders and the capture kit. See Rebuild. |

## How the values were read

Gauth's pages are React with CSS modules: a class reads `catalog_card__Xyz12`, so the kit selects by the stable `catalog_card` part. The stylesheets come from a CDN, which the CSSOM will not read cross-origin, so [vars.mjs](tools/capture/vars.mjs) keeps every stylesheet response and parses it in the page with a constructed `CSSStyleSheet`. The pages declare about 3,700 custom properties, and most are not Gauth's: 2,211 are Ant Design's CSS-variable theme (`--ant-*`, including its stock `#1677ff` primary that Gauth never paints), 244 are TikTok's TUX theme (`--Primary: #fe2c55` and friends, under `:root, [data-theme="light"]`), and the science lesson brings Astryx, a separate design system with its own "stone" theme. All of these are recorded in [raw/css-vars.json](raw/css-vars.json) by owner and none is promoted unless Gauth paints it.

Gauth's own 750 declarations are mostly the lesson system: the lesson palette (`--lesson-primary-*`, `--lesson-gray-*`, `--lesson-blue-*`, `--lesson-right-*`, `--lesson-wrong-*`, which the Academy pages also paint), the lesson type scale (`--lesson-font-size-*`, `--ugc-lesson-*`), a few layout widths, Atlas's `--aw-*` and the math player's `--gauth-*`. The token file uses these wherever one matches what a page paints, and otherwise takes the computed style of the real element, citing the component entry it was read from. So the palette is grouped by place (ink, paper, sand, slate, blue, green, gold, indigo for Homework, astryx for the science lesson, atlas) rather than as ramps, because Gauth has no ramps.

Component values are computed styles read per state with Playwright ([measure.mjs](tools/capture/measure.mjs)). Hover used the pointer, focus-visible a real keyboard Tab, and pressed was forced through DevTools (`CSS.forcePseudoState`), so no button was clicked for real. Text fields were typed into and cleared again, and Enter was never pressed. The only presses were dismissals (the promo dialog's close button, the audio dialog's Not now), the math player's Continue (which starts playback), tabs, Show more, the lesson's own Pause, Settings and chapters buttons, Create Course (which opens a dialog), and a story card's Explore (which opens a published story). Nothing was signed into, created, sent or uploaded.

A second pass the same day closed four more gaps: the brand-red Sign in measured enabled (with `name@example.com` typed, never submitted), a field's error state forced from Gauth's own `form_error` class, the sign-up password field focused (never typed into), the check-in answered right on a second visit, warning resolved from Astryx in the science player, and the code role and the Atlas delete dialog read from Gauth's stylesheets. The 2026-10-17 refresh added three readings. [foundations.mjs](tools/capture/foundations.mjs) parses every rule Gauth's stylesheets put under `prefers-reduced-motion: reduce` (about 60, in the lesson players, the course pages and Astryx) and compares what the components paint with reduced motion emulated and without: the lesson controls' transitions go from 125ms to none, entrance animations, skeleton pulses and loading dots stop, and the lesson-complete confetti is hidden, while the shell and Academy transitions do not change (`core.duration.reduced`). The same script reads the z-index of every layer on each page and with each dialog open (`core.zIndex`), and the brand colour evidence: one `<meta name="theme-color" content="#ffffff">`, no mask icon and no web manifest, so the brand red is confirmed only by where it is painted. The new components were reached by opening the Sign in dialog, the Gauth PLUS dialog and the footer's language select and closing them again; a throwaway string was typed into the Sign in email field and deleted, no plan card was chosen and no button in a dialog was pressed. To see the lesson's feedback colours, the last option of the science lesson's practice check-in was picked once; that is the only answer the capture gave.

Gauth paints one light theme. Its stylesheets declare dark values (TUX under `[data-theme="dark"]`, the lesson palette under `[data-lesson-style="dark"]`, Astryx as `light-dark()` pairs), but no page captured applies any of them, no control offers a switch, and every page painted the same with `prefers-color-scheme: dark` emulated. So the token file has a light set only, and the dark declarations stay in the raw file.

Screenshots are stored as 256-colour PNGs to keep the folder small. Flat UI colours are exact; read values from the tokens, not the images.

## What to distrust

- **Status colours.** `status.danger` and `status.success` are painted (the check-in's result card, answered wrong and right). `status.info` is Gauth's declared `--gauth-semantic-blue-*`, and `status.warning` is Astryx's yellow as the science player resolves it; neither was seen painted, and Gauth's own CSS has no warning. Gauth also declares a danger and a success trio (`--lesson-wrong-*`, `--lesson-right-*`) that differ from the painted ones.
- **Forced and declared states.** The field error is Gauth's `form_error` class added in DevTools; the error message text, the code role and the delete dialog are read from Gauth's CSS and never seen on a page.
- **The spacing scale is a reading, not Gauth's.** Gauth declares no spacing scale. `core.spacing` lists the measured values on a 4px grid, which 63% of the 1,020 measured paddings and gaps fall on; `core.spacing-offgrid` keeps the rest (10px alone is used 131 times).
- **The elevation levels are a grouping.** `elevation.level-1` to `level-4` point at measured shadows chosen by use (resting card, hovered card, popover, dialog); Gauth itself paints 17 different shadows, all kept under `light.elevation`.
- **Three background roles share a value.** `background.surface`, `.raised` and `.overlay` are all white: Gauth separates them by shadow, not by fill.
- **Disabled text** (`text.disabled`, `#9ca2ac`) is read from one control, the Atlas Send button's icon while the box is empty. The Sign in button's disabled state is a pale fill with white text instead (`action.primary-disabled`).
- **Pressed** was forced with DevTools, so `action.primary-pressed` is the hover fill held under `:active:hover`; Gauth sets no separate pressed colour.
- **Third-party controls.** The language select and the blog pagination are Ant Design and keep Ant's own colours (`rgba(0, 0, 0, 0.88)` text, `#1677ff` focus); they are measured as Gauth shows them but are not Gauth's palette.
- **The Atlas Video badge and play disc** were not on the landing page on 2026-10-17; their entries keep the 2026-10-04 readings.

## Coverage

Against the library's checklist ([docs/DESIGN-SYSTEM.md](../../docs/DESIGN-SYSTEM.md)), as of 2026-10-17. The last column says why a row the scorecard marks short cannot be closed by a recapture.

| Item | Status | Where, or why not |
|---|---|---|
| Colour ramps | not present | Gauth declares no ramps: its own variables are named roles (`--lesson-gray-text-1`, `--lesson-primary-fill-2`), and the palette is grouped by place. A recapture cannot add a ramp the product does not have; ordering the painted greys by lightness would invent one. |
| Background roles | captured | `light.background.page`, `.surface`, `.raised`, `.overlay`, `.scrim` and `.scrim-dialog` |
| Text roles | captured | `light.text.primary`, `.secondary`, `.disabled`, `.on-accent`, `.link` |
| Border roles | captured | `light.border.default`, `.strong`, `.focus` |
| Accent states | captured | `light.action.accent`, `.accent-hover`, `.accent-pressed`, `.accent-disabled`: Gauth's own button component, the brand-red Sign in (`#ff013e`, hover `#f00039`, pressed `#d80033`), measured with an example address in the field. The near-black primary of the learning pages (`light.action.primary`, `.primary-hover`) has no pressed colour of its own: pressed keeps the hover fill and scales to `scale.press`. |
| Status colours | captured | `light.status`, each with fill, text and border: danger and success painted (the lesson's result card, answered wrong and right), info declared by Gauth (`--gauth-semantic-blue-*`), warning from Astryx, the science player's design system, resolved in the player (`--color-*-yellow`). Gauth's own CSS declares no warning; neither info nor warning was seen painted. |
| Theme parity | not present | Gauth ships one light theme; its dark declarations are applied on no page (`themeChecks` in [raw/css-vars.json](raw/css-vars.json)) |
| Type | captured | nine families with stacks, the `--lesson-font-size-*` scale, weights, line heights and 56 composite styles (`core.typography`), with display, heading, body, label and caption roles and `typography.code` from Gauth's markdown styles (code keeps the text face on a grey fill; declared, not seen painted, since no page captured shows code). |
| Spacing | captured | `core.spacing` on a 4px base (`core.spacing.base`), off-grid values in `core.spacing-offgrid`; see What to distrust |
| Shape | captured | `core.radius`, `core.borderWidth` |
| Sizing | captured | `core.size` (control heights 30 to 48, icons 20 and 24, the 32px lesson control), `core.focus` |
| Elevation | captured | `light.elevation.level-1` to `level-4`, each with its use, over the 17 measured shadows |
| Motion | captured | `core.duration`, `core.easing`, `core.scale`, and `core.duration.reduced` with what reduced motion changes ([raw/foundations.json](raw/foundations.json)) |
| Layout | captured | `core.breakpoint`, `core.layout`, `core.grid` (column counts and gaps), `core.zIndex` |
| Button, icon button, link, text field, text area, select, radio, switch, tabs, menu, tooltip, dialog, card, list row, table, avatar, badge | captured | 17 of 19; [components.md, Checklist coverage](components.md#checklist-coverage) maps each to its entries and states |
| Checkbox | not present | no public page or form has one; the Sign in dialog states its terms as text |
| Toast | not captured | none appeared after any action the capture took signed out |
| States | captured | hover, focus-visible, pressed (forced), selected, opened, disabled (Sign in, Atlas Send, pagination), error (the answered check-in, and a field's `form_error` state forced from Gauth's own class) and success (the check-in answered right). Loading only as the math tutor's shimmering status line, read at rest: the pages render on the server, so the skeletons Gauth's CSS declares never showed. The switch was not toggled on. |
| Focus | partly | all 57 keyboard-focused controls record what focus changes, but only 15 show any visible change (an outline, a shadow ring or a fill), the product's own gap ([components.md, Shared values](components.md#shared-values)) |
| App shell and navigation, forms and validation, empty, loading and error states, feedback, search and filtering, data display, onboarding | captured | [patterns.md](patterns.md) |
| Destructive confirmation | declared | the Atlas delete-topic dialog, written from Gauth's own CSS in [patterns.md](patterns.md#destructive-confirmation) and `light.component.delete-dialog`; it is behind sign-in, so not seen |
| Signed-in pages | not captured | the capture never signs in (a learner's own courses, history, settings, checkout) |
| Light theme, 1440 and 390 | captured | [screenshots/](screenshots); dialogs, the plans page and the lesson are desktop only |
| Dark theme | not present | see Theme parity |
| Icons and fonts | captured | [icons/INDEX.tsv](icons/INDEX.tsv) by role; Fonts below, with licences and fallbacks |

## Fonts

| Family | Weights | Used for |
|---|---|---|
| Playfair Display | 600, 700, 800 | "Gauth Academy", lesson titles, the promo dialog, the math slide titles |
| Libre Baskerville | 400, 700 | The Homework hero (served as "Gauth Home Libre Baskerville"), the Atlas title, the science canvas's chapter titles (served as "Canvas Chapter") |
| SF Pro | 400, 590, 700 | Academy controls, the unit page, Atlas; Gauth declares it over `local()` only, so it is Apple's system face |
| System stack | | Everything the CSS modules inherit: `-apple-system, "system-ui", "Google Sans", Roboto, Arial` |
| Inter | 400, 500, 600 | Math unit cards, the Ask gauth field, Astryx dialogs |
| Satoshi | 500 | The science canvas's text and headings (served as "Canvas Print" and "Canvas Heading") |
| Shantell Sans | 500, 600 | The canvas tutor's handwriting (served as "Canvas Tutor") |
| KaTeX | | Maths |

Playfair Display, Libre Baskerville, Inter and Shantell Sans are open source, so the style guide loads them from Google Fonts. SF Pro is Apple's and Satoshi is from Fontshare, so the guide falls back to the system font for both, and no font file is committed or needed.

## Do and don't

1. **Do keep the near-black fill for Sign in and the one action that moves the learner on.** Start, Create and Share are `#21252e`; tabs, Show more and Generate Video are outlined on the ground or on white, and Create Course, the AI entry point, is the pale blue gradient button. See [unit-light-default](screenshots/unit-light-default.png), [academy-my-light-default](screenshots/academy-my-light-default.png), [atlas-light-story](screenshots/atlas-light-story.png) and [academy-math-light-default](screenshots/academy-math-light-default.png).
2. **Do let each course bring its own colour and keep the chrome neutral.** Physics covers are pale blue, Biology green, Chemistry violet and Algebra 2 terracotta; on the unit page Algebra 1's green tints the banner (`#ecf4e5`), the current unit's 5px bar and text (`#3c6b26`) and the topic coins, while the sidebar, tabs and buttons stay warm grey. See [academy-science-light-full](screenshots/academy-science-light-full.png), [unit-light-default](screenshots/unit-light-default.png) and [course-banner-default](components/crops/course-banner-default.png).
3. **Don't carry the brand red into the learning pages.** `#ff013e` paints the marketing home (the gradient headline words, the Step-by-step row) and the Insights tab, but in the Academy, the unit page and the lessons it appears only in the logo and the mascot. See [home-light-full](screenshots/home-light-full.png), [news-light-default](screenshots/news-light-default.png) and [academy-math-light-default](screenshots/academy-math-light-default.png).
4. **Do keep the serif for titles.** The page title, the lesson title and the chapter titles are Playfair Display or Libre Baskerville; section headings, card titles, body text and every control are sans. See [academy-science-light-default](screenshots/academy-science-light-default.png), [lesson-science-light-quiz](screenshots/lesson-science-light-quiz.png) and [lesson-math-light-default](screenshots/lesson-math-light-default.png).
5. **Do drop the app shell inside a lesson.** The players have no sidebar or top bar: an exit cross at the top left, transport controls as 32px ghost icons, and in the science and math players the tutor field stays docked on screen (the Ask Tutor pill at the bottom, the Ask gauth field in the 360px column). See [lesson-science-light-default](screenshots/lesson-science-light-default.png), [lesson-math-light-default](screenshots/lesson-math-light-default.png) and [lesson-history-light-default](screenshots/lesson-history-light-default.png).
6. **Don't copy the missing focus ring.** 42 of the 57 controls given keyboard focus show no change, Create Course and Start among them; use the 2px `#0064e0` ring 3px out that the science lesson's own controls draw. See [create-course-button-focus-visible](components/crops/create-course-button-focus-visible.png), [start-button-focus-visible](components/crops/start-button-focus-visible.png) and [quiz-option-focus-visible](components/crops/quiz-option-focus-visible.png).

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

`build_tokens.py` reads `raw/css-vars.json` and `raw/component-tokens.json` and writes `tokens.json`; it refuses a value that is not the DTCG type it claims and an alias that points at nothing. `build_style_guide.py` renders `style-guide.html` from `tokens.json` and `tools/style-guide.template.html`, turning every token into a CSS variable so the page cannot drift from the file. `build_components_md.py` writes `components.md` from `raw/components-computed.json`, `raw/layout.json`, `tokens.json`, the screenshots and `icons/INDEX.tsv`. All three are deterministic: re-running them on this commit reproduces their files byte for byte. Edit the raw inputs or the builders, never the generated files.

`tools/capture/` holds the kit the captures came from. The Playwright scripts take `PLAYWRIGHT` as the path to a Playwright install's `index.mjs` when `playwright` is not resolvable from where they run.

```bash
PLAYWRIGHT=/path/to/playwright/index.mjs node tools/capture/measure.mjs academy unit
```

`measure.mjs` takes page names (`promo home academy create unit science math history atlas story news mobile signin trial plus footer blog`) and merges into `raw/components-computed.json`, dropping the entries a re-run page no longer produces; then `node tools/capture/build-measurements.mjs` rewrites `raw/measurements.md`. `public.mjs` takes the screenshot names to re-take (`RAW=<scratch dir> node tools/capture/public.mjs academy-math,mobile-atlas`), and `python3 tools/capture/quantize.py <scratch dir>` stores them. `vars.mjs`, `foundations.mjs`, `icons.mjs` (with `icon-names.tsv` naming icons by geometry hash) and `layout.mjs` rewrite their raw files whole. The science lesson takes about four minutes to reach its quiz, so `measure.mjs science` is slow. `lib.mjs` holds the shared helpers.

## Use in Figma

Import `tokens.json` with Tokens Studio and choose the Light theme. Set the display fonts to Playfair Display and Libre Baskerville and the UI font to SF Pro (or Inter where SF Pro is not installed).

## Gauth's surfaces and self-learn's

| Gauth | Layout | self-learn |
|---|---|---|
| Academy catalogue (`/course/<tab>`) | A Playfair title and Create Course over category tabs, then course sections, each a heading row and a three-column card grid | `/courses` |
| Unit page (`/course/math/<course>?unit=`) | A course banner, a sticky unit rail at the left, a path of topic coins at the right, a floating Start panel | the course page, `/courses/[slug]` |
| Lesson player and Ask Tutor (`/course/<subject>/<lesson>/learn`) | Full screen, no shell. Science: a narrated canvas, a section rail at the right, an Ask Tutor pill docked at the bottom. Math: a 360px tutor column with an Ask gauth field beside the slide | `/learn/<concept>` |
| Atlas (`/atlas`) | A prompt box that turns a topic into an illustrated story, recommendation chips, a grid of story cards with Video badges, and a story page | the studio, `/studio` |
| Homework home (`/`) | A serif hero, one large question field, an upload panel and subject chips, then marketing bands | Home, `/home` (formerly `/today`) |
| Create a Course dialog | A warm sheet with suggested topics and a single prompt field | the studio's chat, and making a course |

## The screen to get right

The Academy catalogue is the screen to get right. It sits on a warm `#faf9f5` ground (`--lesson-gray-bg`) that the 220px sidebar shares, with the current sidebar item and the current tab in beige `#f4ebe5` (`--lesson-primary-fill-2`) at radius 10 and 12. "Gauth Academy" is Playfair Display 700 at 36px; Create Course is a 37px pale blue button with a 1px `#d5e3f4` border at radius 12. The column is 1025 wide, and each course section is a 22/28.6 600 heading beside an 80px cover over three 326px cards, 24 apart. Cards are white with a 1px `rgba(0, 0, 0, 0.08)` border, radius 16 and a `0 4px 7px rgba(0, 0, 0, 0.04)` shadow that deepens to `0 8px 10px rgba(0, 0, 0, 0.08)` on hover in 160ms; text is `#21252e` with `#757c88` meta. The primary button is `#21252e` at radius 12, lightens to `#333943` on hover and scales to 0.98 when pressed. Most of Gauth's own controls draw no focus ring, which a rebuild should not copy. Everything the capture could not reach is listed under Gaps in [components.md](components.md#gaps).
