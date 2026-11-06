# Gauth components

The discovery list of every page and view captured, then one entry per component with crops of the real product, the icon index and the Gaps. Captured from www.gauth.com on 2026-10-17, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running page. Nothing was signed into, created, sent or uploaded.

The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) (199 components, 389 states). The page layouts are described in [raw/pages.md](raw/pages.md).

How to read an entry:

- Every value is written as the token in [tokens.json](tokens.json) that holds it: a colour as the role token for what it paints (a fill as `action.*` or `background.*`, text as `text.*`, a border or outline as `border.*`) or, failing that, its palette token; a radius, padding, border width, focus ring, shadow, duration or press scale as its core or elevation token; text as its typography token, then its colour. A value no token holds is written raw (a text style as family size/line-height weight, for example `SF Pro 14/21 500`). 1379 of 1570 values in the entries (88%) are written as tokens. The other 191 are marked †: a value used by one component only (a one-off padding, colour or text style), a `50%` circle radius, or a line height of `normal`, none of which a DTCG token in this file holds; every other value used by two or more components has a token. Each entry ends with the list of tokens it uses. Sizes are the element's measured box and stay in px.
- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example "default (same: focus-visible)". When the root paints nothing, "Child layers" names the first nodes inside it that do.
- Crops are images of the component read from the live page, in [components/crops/](components/crops) (369 files, named `{component}-{state}.png`, at 2x). Screenshots are in [screenshots/](screenshots).

## Discovery list

Screenshots are named `{page}-light-{state}.png` (Gauth has one theme). Desktop shots are 1440 x 900 at 1x; `-full` shots are whole pages at 1x; mobile shots are `mobile-{page}-light-{state}.png`, 780 wide (390 at 2x).

| Surface | URL | Screenshots |
|---|---|---|
| Homework home. Serif hero, question field, upload panel, subject chips, then the Atlas, AI solution and live tutor bands, comments and the footer. The promo dialog, the field focused and the folded sidebar captured. | `/` | [default](screenshots/home-light-default.png), [full](screenshots/home-light-full.png), [promo](screenshots/home-light-promo.png), [question-focused](screenshots/home-light-question-focused.png), [sidebar-folded](screenshots/home-light-sidebar-folded.png) |
| Academy, Science Labs. Title, Create Course, tabs, course sections of lesson cards. | `/course/science` | [default](screenshots/academy-science-light-default.png), [full](screenshots/academy-science-light-full.png) |
| Academy, Math Curriculum. Unit cards, six per course, and Show more expanded (the toolbar sticks with Create Course in it). | `/course/math` | [default](screenshots/academy-math-light-default.png), [show-more](screenshots/academy-math-light-show-more.png) |
| Academy, History Signature. Illustrated lesson cards. | `/course/history` | [default](screenshots/academy-history-light-default.png) |
| Academy, My Course. The signed-out empty state, and the Create a Course dialog. | `/course/my` | [create-dialog](screenshots/academy-my-light-create-dialog.png), [default](screenshots/academy-my-light-default.png) |
| Unit page (Algebra 1). Banner, unit rail, topic path, Start panel; scrolled down the path; Unit 2 chosen in the rail. | `/course/math/algebra-1?unit=real-numbers-and-sets` | [default](screenshots/unit-light-default.png), [path](screenshots/unit-light-path.png), [unit-2](screenshots/unit-light-unit-2.png) |
| Science lesson. The audio dialog, the first chapter, Settings open, the Playback speed menu, a tooltip, Ask Tutor opened, a figure with its callout and list, a quiz, and the quiz answered (its result card). | `/course/science/how-things-work-1/learn` | [ask-tutor](screenshots/lesson-science-light-ask-tutor.png), [audio-dialog](screenshots/lesson-science-light-audio-dialog.png), [default](screenshots/lesson-science-light-default.png), [figure](screenshots/lesson-science-light-figure.png), [quiz-answered](screenshots/lesson-science-light-quiz-answered.png), [quiz](screenshots/lesson-science-light-quiz.png), [settings](screenshots/lesson-science-light-settings.png), [speed-menu](screenshots/lesson-science-light-speed-menu.png), [tooltip](screenshots/lesson-science-light-tooltip.png) |
| Math lesson. The audio gate, the playing slide with the tutor column, the chapters panel. | `/course/math/algebra-1/fundamentals-of-set-theory/learn` | [audio-gate](screenshots/lesson-math-light-audio-gate.png), [chapters](screenshots/lesson-math-light-chapters.png), [default](screenshots/lesson-math-light-default.png) |
| History lesson. The opening scene, the chapter panel. | `/course/history/crossing-the-ocean-wall/learn` | [chapters](screenshots/lesson-history-light-chapters.png), [default](screenshots/lesson-history-light-default.png) |
| Atlas. Landing, prompt box, chips, Popular Stories, FAQ; a story card's video preview; the Apollo 11 story page, and its Video Settings popover. | `/atlas` | [default](screenshots/atlas-light-default.png), [full](screenshots/atlas-light-full.png), [story-preview](screenshots/atlas-light-story-preview.png), [story-video-settings](screenshots/atlas-light-story-video-settings.png), [story](screenshots/atlas-light-story.png) |
| Insights. Breadcrumb, News and Blog tabs, featured article, article rows. | `/news` | [default](screenshots/news-light-default.png), [full](screenshots/news-light-full.png) |
| Blog. The article list and its pagination. | `/blog` | [default](screenshots/blog-light-default.png), [pagination](screenshots/blog-light-pagination.png) |
| Sign in dialog, opened from the top bar. | `/` | [dialog](screenshots/signin-light-dialog.png), [filled](screenshots/signin-light-filled.png), [signup-focused](screenshots/signin-light-signup-focused.png) |
| Gauth PLUS dialog, opened from the sidebar card's Start Free Trial. | `/` | [default](screenshots/plus-dialog-light-default.png) |
| Plans page. Two plan cards and the features-by-plan table. | `/plus` | [default](screenshots/plus-light-default.png), [full](screenshots/plus-light-full.png) |
| Footer language select, opened. | `/` | [language-open](screenshots/footer-light-language-open.png) |
| Homework home at 390: the promo dialog, the hero, the full page with the app banner. | `/` | [default](screenshots/mobile-home-light-default.png), [full](screenshots/mobile-home-light-full.png), [promo](screenshots/mobile-home-light-promo.png) |
| Academy at 390: Math Curriculum (Science Labs is not offered on a phone). | `/course/math` | [default](screenshots/mobile-academy-light-default.png), [full](screenshots/mobile-academy-light-full.png) |
| Unit page at 390, and scrolled down the path. | `/course/math/algebra-1?unit=real-numbers-and-sets` | [default](screenshots/mobile-unit-light-default.png), [path](screenshots/mobile-unit-light-path.png) |
| Math lesson at 390: the audio gate and the slide. | `/course/math/algebra-1/fundamentals-of-set-theory/learn` | [audio-gate](screenshots/mobile-lesson-math-light-audio-gate.png), [default](screenshots/mobile-lesson-math-light-default.png) |
| Atlas at 390, and a story page (Artemis II). | `/atlas` | [default](screenshots/mobile-atlas-light-default.png), [story](screenshots/mobile-atlas-light-story.png) |

### Overlays and transient states

| State | Where | How it was reached | Captured |
|---|---|---|---|
| Promo dialog ("Introducing Gauth Academy") | every page, on load | at rest; then dismissed with its own close button for every other capture | [home-light-promo](screenshots/home-light-promo.png), [promo-dialog](#promo-dialog) |
| Create a Course dialog | Academy | Create Course pressed (opens the dialog); a prompt typed and deleted, no suggestion pressed | [academy-my-light-create-dialog](screenshots/academy-my-light-create-dialog.png), [create-a-course-dialog](#create-a-course-dialog) |
| Enable audio dialog | science lesson | on load; Not now pressed, Enable audio never pressed | [lesson-science-light-audio-dialog](screenshots/lesson-science-light-audio-dialog.png) |
| Audio gate | math lesson | on load; Continue pressed to start playback | [lesson-math-light-audio-gate](screenshots/lesson-math-light-audio-gate.png) |
| Settings popover | science lesson | the lesson's Settings button | [lesson-science-light-settings](screenshots/lesson-science-light-settings.png) |
| Ask Tutor, opened | science lesson | clicked into the bar; sample text typed and deleted, nothing sent | [lesson-science-light-ask-tutor](screenshots/lesson-science-light-ask-tutor.png) |
| Quiz | science lesson | reached by letting the lesson play about three minutes | [lesson-science-light-quiz](screenshots/lesson-science-light-quiz.png) |
| Quiz answered | science lesson | the last option of the practice check-in picked; the check-in comes back as a result card in the notes | [lesson-science-light-quiz-answered](screenshots/lesson-science-light-quiz-answered.png), [quiz-result-card](#quiz-result-card) |
| Playback speed menu | science lesson | Settings, then its Speed row; no speed chosen | [lesson-science-light-speed-menu](screenshots/lesson-science-light-speed-menu.png), [playback-speed-menu](#playback-speed-menu) |
| Tooltip | science lesson | hovering a header control | [lesson-science-light-tooltip](screenshots/lesson-science-light-tooltip.png), [tooltip](#tooltip) |
| Sign in dialog | every page with the top bar | the top bar's Sign in; a throwaway string typed into the email field and deleted, nothing submitted | [signin-light-dialog](screenshots/signin-light-dialog.png), [sign-in-dialog](#sign-in-dialog) |
| Sign in, enabled | Sign in dialog | name@example.com typed so the brand-red button enables; never pressed | [signin-light-filled](screenshots/signin-light-filled.png), [primary-button-brand-red-sign-in](#primary-button-brand-red-sign-in) |
| Sign-up view | Sign in dialog | its Sign up link; the password field focused (never typed into) to show its rule line | [signin-light-signup-focused](screenshots/signin-light-signup-focused.png), [field-helper-text](#field-helper-text) |
| Field error (forced) | Sign in dialog | Gauth's own form_error class added to the email field in DevTools; its error shows only after a submit | [text-field-error-forced](#text-field-error-forced) |
| Quiz answered right | science lesson | a second visit, the option naming lift, thrust and climb cost picked | [quiz-result-card-right-answer](#quiz-result-card-right-answer) |
| Gauth PLUS dialog | every page with the sidebar | the sidebar card's Start Free Trial; nothing chosen, typed or bought | [plus-dialog-light-default](screenshots/plus-dialog-light-default.png), [gauth-plus-dialog](#gauth-plus-dialog) |
| Language list | footer | the footer's language select; no language chosen | [footer-light-language-open](screenshots/footer-light-language-open.png), [select-list-language](#select-list-language) |
| Chapters panel | math and history lessons | the chapters button | [lesson-math-light-chapters](screenshots/lesson-math-light-chapters.png), [lesson-history-light-chapters](screenshots/lesson-history-light-chapters.png) |
| Show more | Math Curriculum | the Show 14 more button | [academy-math-light-show-more](screenshots/academy-math-light-show-more.png) |
| Folded sidebar | Homework home | the sidebar's collapse button | [home-light-sidebar-folded](screenshots/home-light-sidebar-folded.png) |
| Story preview | Atlas | a story card pressed (opens a video preview) | [atlas-light-story-preview](screenshots/atlas-light-story-preview.png) |
| Story page | Atlas | Explore in the preview (opens the published story) | [atlas-light-story](screenshots/atlas-light-story.png), [mobile-atlas-light-story](screenshots/mobile-atlas-light-story.png) |
| Video Settings popover | Atlas story | hovering Generate Video; nothing in it pressed | [atlas-light-story-video-settings](screenshots/atlas-light-story-video-settings.png) |

## Checklist coverage

The 19 components of the library's checklist ([docs/DESIGN-SYSTEM.md](../../docs/DESIGN-SYSTEM.md)), each with the entries below that show it and the states captured across them. 17 of 19 are captured.

| Component | Entries | States captured |
|---|---|---|
| Button | [Start button](#start-button), [Create button (empty state)](#create-button-empty-state), [Primary button, brand red (Sign in)](#primary-button-brand-red-sign-in), [Secondary button (Not now)](#secondary-button-not-now), [Secondary button (Start for free)](#secondary-button-start-for-free), [Join Gauth PLUS button](#join-gauth-plus-button), [Primary button, disabled (Sign in)](#primary-button-disabled-sign-in) | default, hover, focus-visible, pressed, disabled |
| Icon button | [Transport and view buttons](#transport-and-view-buttons), [Exit button](#exit-button), [Header round button](#header-round-button), [Page arrow button](#page-arrow-button), [Dialog close button (Gauth)](#dialog-close-button-gauth) | default, hover, focus-visible, pressed |
| Link | [Inline link (Learn More)](#inline-link-learn-more), [Footer link](#footer-link), [Inline link (Terms of Service)](#inline-link-terms-of-service), [Inline link (Sign up)](#inline-link-sign-up), [Back link](#back-link) | default, hover, focus-visible |
| Text field | [Email field](#email-field), [Text field, focused (sign-up password)](#text-field-focused-sign-up-password), [Text field, error (forced)](#text-field-error-forced), [Field helper text](#field-helper-text), [Question field](#question-field), [Topic search field](#topic-search-field), [Top bar question field](#top-bar-question-field), [Ask gauth field](#ask-gauth-field) | default, hover, focused, filled, error |
| Text area | [Text area (Atlas prompt)](#text-area-atlas-prompt), [Atlas prompt box](#atlas-prompt-box), [Course prompt field](#course-prompt-field) | default, focus-visible, filled, hover, focused |
| Select | [Select (language)](#select-language), [Select list (language)](#select-list-language), [Select option, current](#select-option-current), [Select option](#select-option) | default, hover, focus-visible, opened, selected |
| Checkbox | not captured: not present on any public page; no public form has one | - |
| Radio | [Quiz option](#quiz-option), [Plan card (single choice)](#plan-card-single-choice), [Plan card, selected](#plan-card-selected) | default, hover, focus-visible, pressed, selected |
| Switch | [Switch](#switch), [Search toggle pill](#search-toggle-pill) | default, hover, focus-visible |
| Tabs | [Category tab](#category-tab), [Category tab, current](#category-tab-current), [Pill tab](#pill-tab), [Pill tab, current](#pill-tab-current) | default, hover, focus-visible, pressed |
| Menu | [Settings popover](#settings-popover), [Playback speed menu](#playback-speed-menu), [Menu item](#menu-item), [Menu item, current](#menu-item-current) | opened, default, hover, focus-visible, selected |
| Tooltip | [Tooltip](#tooltip) | opened |
| Dialog | [Sign in dialog](#sign-in-dialog), [Gauth PLUS dialog](#gauth-plus-dialog), [Create a Course dialog](#create-a-course-dialog), [Enable audio dialog](#enable-audio-dialog), [Promo dialog](#promo-dialog) | default |
| Toast | not captured: not seen: no toast appeared after any action the capture took signed out | - |
| Card | [Lesson card (Science Labs, History Signature)](#lesson-card-science-labs-history-signature), [Unit card (Math Curriculum)](#unit-card-math-curriculum), [Story card](#story-card), [Plan card (plans page)](#plan-card-plans-page), [Review card](#review-card) | default, hover, focus-visible, pressed |
| List row | [Article row](#article-row), [Chapter row](#chapter-row), [Chapter panel row](#chapter-panel-row), [Unit rail item](#unit-rail-item), [Table row (benefits)](#table-row-benefits) | default, hover, focus-visible, pressed |
| Table | [Table (features by plan)](#table-features-by-plan), [Table row](#table-row), [Table (benefits)](#table-benefits) | default, hover |
| Avatar | [Avatar (review)](#avatar-review) | default |
| Badge | [New badge](#new-badge), [Badge (plan tag)](#badge-plan-tag) | default |

## Shared values

Values that apply across entries, from the measurement files.

**Focus.** 57 components were given a real keyboard focus. 15 show a visible change (an outline on the element, a child or a parent, a shadow ring, a border or a fill): `canvas-exit` (outline `focus.width` solid `border.focus`, offset `focus.offset-astryx`), `canvas-control` (outline `focus.width` solid `border.focus`, offset `focus.offset-astryx`), `outline-item` (outline `focus.width` solid `border.focus`, offset `focus.offset-astryx`), `ask-tutor-mic` (outline `focus.width` solid `palette.ink.black`, offset `focus.offset`), `switch` (outline `focus.width` solid `palette.blue.focus-2`, offset `focus.offset-inset`; fill `background.hover`), `quiz-option` (outline `focus.width` solid `border.focus`, offset `focus.offset-astryx`), `chapter-option` (fill `background.selected`), `chapter-panel-item` (fill `palette.ink.a04`), `search-toggle` (outline `focus.width` solid rgba(23, 20, 16, 0.18)†, offset `focus.offset`), `pill-tab-active` (outline `focus.width` solid `palette.brand.focus`, offset `focus.offset`), `pill-tab` (outline `focus.width` solid `palette.brand.focus`, offset `focus.offset`), `featured-article` (outline `focus.width` solid `action.accent-hover`, offset 4px†), `language-select` (shadow ring 0px 0px 0px 2px rgba(5, 145, 255, 0.1)†; border `borderWidth.hairline` solid #1677ff†), `pagination-item` (outline on a: 3px solid #91caff† offset 1px), `menu-item` (outline `focus.width` solid `palette.blue.focus-2`, offset `focus.offset-inset`; fill `background.hover`). The other 42 change nothing, so a keyboard user sees no focus: `promo-confirm`, `promo-close`, `side-menu-link`, `side-menu-collapse`, `question-input`, `subject-chip`, `atlas-cta`, `create-course-button`, `category-tab-active`, `category-tab`, `lesson-card`, `unit-card`, `show-more`, `unit-row`, `create-button`, `create-suggestion`, `create-close`, `back-link`, `unit-button-active`, `topic-node-current`, `topic-node`, `start-button`, `audio-not-now`, `audio-enable`, `page-nav`, `header-round-button`, `chapter-pill`, `play-button`, `new-topic`, `recommendation-chip`, `story-card`, `explore-button`, `share-button`, `generate-video-button`, `rail-item`, `continue-button`, `terms-link`, `plan-card`, `start-free-button`, `inline-link`, `footer-link`, `atlas-textarea`. The Upgrade and Sign in buttons in the top bar are a `div` and a `span` and cannot take focus at all.

**Pressed.** Gauth's own button component, the brand-red primary in the Sign in dialog, darkens when pressed (`action.accent` `#ff013e`, hover `#f00039`, pressed `#d80033`). The learning pages' buttons shrink instead of changing colour much: Create, Start, Create Course and the Astryx buttons scale to 0.98, the math player's round buttons to 0.94, the promo button to 0.99. Cards deepen their shadow on hover and keep it when pressed.

**Motion.** Transitions measured on the components, by duration.

| Duration | Easing | Property | Where |
|---|---|---|---|
| 0.12s | `ease` | background-color, color, transform | chapter-pill, chapter-pill-active, continue-button, header-round-button, page-nav, play-button, search-toggle, speed-button |
| 0.125s | `cubic-bezier(0.24, 1, 0.4, 1)` | background-color, background-image, border-color, box-shadow, color, opacity, transform | audio-enable, audio-not-now, canvas-control, canvas-exit, outline-item, outline-item-active, quiz-option |
| 0.15s | `ease` | background, border-color, box-shadow, color | search-toggle |
| 0.16s | `ease` | background, background-color, box-shadow, opacity, transform | continue-button, explore-button, header-round-button, history-card, lesson-card, m-unit-card, page-nav, promo-close and more |
| 0.18s | `ease` | background, background-color, border-color, box-shadow, color, opacity, transform | chapter-panel, generate-video-button, player-frame, rail-item, recommendation-chip, send-button |
| 0.2s | `ease` | all, background, border-color, box-shadow | atlas-composer, pagination-item, pagination-prev |
| 0.25s | `ease` | border-color, box-shadow, opacity, transform | story-card, video-settings |
| 0.26s | `cubic-bezier(0.22, 1, 0.36, 1)` | width | ask-tutor, ask-tutor-open |
| 0.26s | `ease` | opacity | side-menu-link |
| 0.3s | `cubic-bezier(0.34, 1.56, 0.64, 1)` | transform | video-settings |
| 0.3s | `ease` | all, background-color | atlas-textarea, language-option, language-option-selected, language-select, m-question-box |
| 0.5s | `ease-in-out` | margin-left, max-width, width | side-menu, side-menu-link, side-menu-warm |

**Layout grid.** Read on each page at each width ([raw/layout.json](raw/layout.json)).

| Page | 1440 | 1920 | 1024 | 390 |
|---|---|---|---|---|
| home | content x 220, 1220 wide; grid 228 228 228 228 gap 16px | content x 220, 1700 wide; grid 228 228 228 228 gap 16px | content x 220, 804 wide; grid 173 173 173 173 gap 16px | content x 0, 390 wide |
| academy-science | content x 220, 1220 wide; grid 325.6 325.6 325.6 gap 24px | content x 220, 1700 wide; grid 325.6 325.6 325.6 gap 24px | content x 220, 804 wide; grid 358 358 gap 24px | content x 0, 390 wide; grid 72 217 12 gap 16px |
| academy-math | content x 220, 1220 wide; grid 325.6 325.6 325.6 gap 24px | content x 220, 1700 wide; grid 325.6 325.6 325.6 gap 24px | content x 220, 804 wide; grid 358 358 gap 24px | content x 0, 390 wide; grid 72 217 12 gap 16px |
| unit | content x 220, 1220 wide; grid 310 683 gap 32px | content x 220, 1700 wide; grid 310 683 gap 32px | content x 220, 804 wide; grid 248 460 gap 32px | content x 0, 390 wide |
| lesson-math | content x 360, 1080 wide; grid 360 1080 gap normal | content x 360, 1560 wide; grid 360 1560 gap normal | content x 300, 724 wide; grid 300 724 gap normal | content x 0, 390 wide |
| atlas | content full width; grid 338.6 338.6 338.6 gap 32px | content full width; grid 338.6 338.6 338.6 gap 32px | content full width; grid 480 480 gap 24px | content x 0, 390 wide; grid 20 302 20 gap normal |

**Card shapes.** Default-state values; the entries hold the states.

| Card | Size | Border | Radius | Background | Shadow | Padding |
|---|---|---|---|---|---|---|
| [Lesson card (Science Labs, History Signature)](#lesson-card-science-labs-history-signature) | 325.66 x 294.09 | `borderWidth.hairline` solid `border.card` | `radius.16` | `background.card` | `elevation.level-1` | `spacing.8` `spacing.8` `spacing.16` `spacing.8` |
| [Unit card (Math Curriculum)](#unit-card-math-curriculum) | 325.66 x 178 | `borderWidth.hairline` solid `border.card` | `radius.16` | `background.card` | `elevation.level-1` | `spacing.20` |
| [Story card](#story-card) | 338.66 x 313.5 | `borderWidth.hairline` solid `border.card` | `radius.16` | `background.card` | `elevation.story-card` | `spacing-offgrid.14` `spacing-offgrid.14` `spacing-offgrid.18` `spacing-offgrid.14` |
| [Feature card](#feature-card) | 228 x 150 | `borderWidth.hairline` solid `border.control` | `radius.32` | `background.card` | none | `spacing.20` `spacing.20` `spacing-offgrid.18` `spacing.20` |
| [Solution option row](#solution-option-row) | 369.81 x 102 | - | `radius.20` | `action.accent` | 0px 7px 14px 0px rgba(168, 0, 0, 0.1)† | `spacing.16` `spacing.24` `spacing.16` `spacing.20` |
| [Course suggestion chip](#course-suggestion-chip) | 310 x 54 | `borderWidth.hairline` solid `palette.paper.line-light` | `radius.16` | `background.card` | none | `spacing-offgrid.14` `spacing.20` |
| [Quiz card](#quiz-card) | 560 x 296 | `borderWidth.hairline` solid `component.quiz.border` | `radius.20` | `background.card` | `elevation.quiz` | `spacing.20` |
| [Quiz option](#quiz-option) | 518 x 44 | `borderWidth.hairline` solid `component.quiz.option-border` | `radius.10` | `background.card` | none | 0px `spacing.12` |
| [Start panel](#start-panel) | 460 x 145.8 | `borderWidth.hairline` solid `border.control` | `radius.28` | `background.card` | `elevation.start-panel` | `spacing-offgrid.26` `spacing.24` `spacing-offgrid.22` `spacing.24` |
| [Settings popover](#settings-popover) | 298 x 246 | `borderWidth.hairline` solid `palette.astryx.popover-line` | `radius.24` | `background.card` | `elevation.level-3` | 0 |
| [Chapters panel](#chapters-panel) | 320 x 460 | - | `radius.16` | `background.card` | `elevation.panel` | `spacing.12` `spacing.8` |
| [Video Settings popover](#video-settings-popover) | 314.88 x 365.04 | `borderWidth.hairline` solid `palette.paper.line-light` | `radius.16` | `background.card` | 0px 10px 40px 0px rgba(0, 0, 0, 0.12)† | 0 |
| [View and Details rail](#view-and-details-rail) | 70 x 132 | `borderWidth.hairline` solid `palette.paper.line-light` | `radius.16` | `background.card` | 0px 4px 20px 0px rgba(0, 0, 0, 0.06)† | `spacing-offgrid.6` |
| [Unit card (mobile)](#unit-card-mobile) | 358 x 112 | `borderWidth.hairline` solid `border.card` | `radius.20` | `background.card` | `elevation.level-1` | `spacing-offgrid.11` `spacing.12` `spacing.12` `spacing-offgrid.11` |

## Components

### Shell and navigation

The app shell shared by Homework, Academy and Insights: a fixed 220px sidebar and a 60px top bar over the content. The sidebar is white with a cool grey current item on Homework and Insights, and takes the warm `#faf9f5` ground with a beige current item on Academy. Atlas and the lesson players have shells of their own (their groups below).

#### Top bar
The 60px bar over the content column: white with a 1px bottom rule on Homework and Insights, transparent on Academy. Holds the question field on inner pages, Upgrade and Sign in. Read as `header` on the Homework home page.

**Values (default).** size 1440 x 60; border B: `borderWidth.hairline` solid `border.field`; background `background.card`; text `typography.nav-strong`, `component.upgrade.text`; icon 24 x 24, `palette.ink.black`.

**Tokens.** `background.card`, `border.field`, `borderWidth.hairline`, `component.upgrade.text`, `palette.ink.black`, `typography.nav-strong`.

![Top bar default](components/crops/header-default.png)

#### Upgrade button
The gold Upgrade pill: a warm gradient fill with brown text and a bolt icon. A div, so it takes no keyboard focus. Measured, never pressed. Read as `upgrade-button` on the Homework home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 90.28 x 31; padding `spacing-offgrid.5` `spacing.8`; radius `radius.8`; background transparent; image linear-gradient(90deg, `palette.gold.start`, `palette.gold.end`); text `typography.nav-strong`, `component.upgrade.text`; icon 14 x 15, `component.upgrade.text` |
| hover | background `component.upgrade.hover`; image none |
| pressed | background `component.upgrade.pressed`; image none |

**Tokens.** `component.upgrade.hover`, `component.upgrade.pressed`, `component.upgrade.text`, `palette.gold.end`, `palette.gold.start`, `radius.8`, `spacing-offgrid.5`, `spacing.8`, `typography.nav-strong`.

![Upgrade button default](components/crops/upgrade-button-default.png) ![Upgrade button hover](components/crops/upgrade-button-hover.png) ![Upgrade button pressed](components/crops/upgrade-button-pressed.png)

#### Sign in button
The near-black primary button in the top bar. A span in a div, so it takes no keyboard focus. Measured, never pressed. Read as `sign-in-button` on the Homework home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 70 x 30; padding 0px `spacing-offgrid.6`; radius `radius.10`; background `action.primary`; text -apple-system 14/normal 600†, `text.inverse` |
| hover, pressed | background `palette.ink.800` |

**Tokens.** `action.primary`, `palette.ink.800`, `radius.10`, `spacing-offgrid.6`, `text.inverse`.

![Sign in button default](components/crops/sign-in-button-default.png) ![Sign in button hover](components/crops/sign-in-button-hover.png) ![Sign in button pressed](components/crops/sign-in-button-pressed.png)

#### Sidebar
The 220px left rail: logo and collapse button, the four destinations, a rule, App, and the Gauth PLUS card pinned to the bottom. Read as `side-menu` on the Homework home page.

**Values (default).** size 220 x 900; padding `spacing.24` `spacing.16` 0px `spacing.16`; border R: `borderWidth.hairline` solid `border.sidebar`; background `background.card`; text `typography.nav-strong`, `text.primary`; transition width `duration.sidebar` `easing.ease-in-out`; icon 24 x 24, `palette.ink.black`.

**Tokens.** `background.card`, `border.sidebar`, `borderWidth.hairline`, `duration.sidebar`, `easing.ease-in-out`, `palette.ink.black`, `spacing.16`, `spacing.24`, `text.primary`, `typography.nav-strong`.

![Sidebar default](components/crops/side-menu-default.png)

#### Sidebar item, current (cool)
The current destination on Homework and Insights: a #f5f5f7 pill with the label in 600. Read as `side-menu-item-active` on the Homework home page.

**Values (default).** size 187 x 40; padding `spacing.8` `spacing.12`; radius `radius.10`; background `background.selected`; text `typography.nav-strong`, `text.primary`; icon 24 x 25, `palette.ink.black`.

**Tokens.** `background.selected`, `palette.ink.black`, `radius.10`, `spacing.12`, `spacing.8`, `text.primary`, `typography.nav-strong`.

![Sidebar item, current (cool) default](components/crops/side-menu-item-active-default.png)

#### Sidebar item
A destination row: 40px tall, radius 10, 20px icon, 14/21 label. Read as `side-menu-item` on the Homework home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 187 x 40; padding `spacing.8` `spacing.12`; radius `radius.10`; background transparent; text `typography.nav`, `text.primary`; icon 24 x 24, `palette.ink.black` |
| hover, pressed | background `background.selected` |

**Tokens.** `background.selected`, `palette.ink.black`, `radius.10`, `spacing.12`, `spacing.8`, `text.primary`, `typography.nav`.

![Sidebar item default](components/crops/side-menu-item-default.png) ![Sidebar item hover](components/crops/side-menu-item-hover.png) ![Sidebar item pressed](components/crops/side-menu-item-pressed.png)

#### Sidebar link, keyboard focus
The link inside a sidebar row, which is what takes keyboard focus. Read as `side-menu-link` on the Homework home page.

**Values (focus-visible).** size 31.95 x 21; background transparent; text `typography.nav`, `text.primary`; transition opacity `duration.ask-tutor` `easing.ease`, max-width `duration.sidebar` `easing.ease-in-out`, margin-left `duration.sidebar` `easing.ease-in-out`.

**Tokens.** `duration.ask-tutor`, `duration.sidebar`, `easing.ease`, `easing.ease-in-out`, `text.primary`, `typography.nav`.

![Sidebar link, keyboard focus focus-visible](components/crops/side-menu-link-focus-visible.png)

#### Sidebar collapse button
Read as `side-menu-collapse` on the Homework home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 24 x 24; background transparent; text Arial 13.33/normal 400†, `text.primary`; opacity 0.4; icon 24 x 24, `text.primary` |
| hover | opacity none |
| pressed | opacity 0.7 |

**Tokens.** `text.primary`.

![Sidebar collapse button default](components/crops/side-menu-collapse-default.png) ![Sidebar collapse button hover](components/crops/side-menu-collapse-hover.png) ![Sidebar collapse button focus-visible](components/crops/side-menu-collapse-focus-visible.png) ![Sidebar collapse button pressed](components/crops/side-menu-collapse-pressed.png)

#### Gauth PLUS card
The upsell card at the foot of the sidebar: cream fill, radius 12, a gold rule under the title and a gold "Start Free Trial" button. Read as `plus-card` on the Homework home page.

**Values (default).** size 174 x 153; padding `spacing-offgrid.10` `spacing.12` `spacing.12` `spacing.12`; radius `radius.12`; background `component.plus-card.background`; text -apple-system 18/26 700†, `text.primary`; icon 44 x 19, `text.primary`.

**Tokens.** `component.plus-card.background`, `radius.12`, `spacing-offgrid.10`, `spacing.12`, `text.primary`.

![Gauth PLUS card default](components/crops/plus-card-default.png)

#### Gauth PLUS card button
Measured, never pressed. Read as `plus-card-button` on the Homework home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 150 x 32; radius `radius.10`; background `component.plus-card.button`; text -apple-system 12/18 600†, `component.plus-card.button-text`; icon 15 x 15, `component.plus-card.button-text` |
| hover | background `component.plus-card.button-hover` |
| pressed | background rgba(255, 196, 106, 0.8)† |

**Tokens.** `component.plus-card.button`, `component.plus-card.button-hover`, `component.plus-card.button-text`, `radius.10`.

![Gauth PLUS card button default](components/crops/plus-card-button-default.png) ![Gauth PLUS card button hover](components/crops/plus-card-button-hover.png) ![Gauth PLUS card button pressed](components/crops/plus-card-button-pressed.png)

#### Logo
Read as `logo` on the Homework home page.

**Values (default).** size 90 x 24; background transparent; icon 24 x 24, `palette.ink.black`.

**Tokens.** `palette.ink.black`.

![Logo default](components/crops/logo-default.png)

#### Sidebar, warm
On Academy the sidebar takes the page ground and the current item turns beige. Read as `side-menu-warm` on the Academy (Science Labs) page.

**Values (default).** size 220 x 900; padding `spacing.24` `spacing.16` 0px `spacing.16`; border R: `borderWidth.hairline` solid `border.sidebar`; background `background.academy`; text `typography.nav`, `text.primary`; transition width `duration.sidebar` `easing.ease-in-out`; icon 24 x 24, #0000ee†.

**Tokens.** `background.academy`, `border.sidebar`, `borderWidth.hairline`, `duration.sidebar`, `easing.ease-in-out`, `spacing.16`, `spacing.24`, `text.primary`, `typography.nav`.

![Sidebar, warm default](components/crops/side-menu-warm-default.png)

#### Sidebar item, current (warm)
The current destination on Academy: a #f4ebe5 pill (--lesson-primary-fill-2). Read as `side-menu-item-warm-active` on the Academy (Science Labs) page.

**Values (default).** size 187 x 40; padding `spacing.8` `spacing.12`; radius `radius.10`; background `background.selected-warm`; text `typography.nav-strong`, `text.primary`; icon 24 x 24, `palette.ink.black`.

**Tokens.** `background.selected-warm`, `palette.ink.black`, `radius.10`, `spacing.12`, `spacing.8`, `text.primary`, `typography.nav-strong`.

![Sidebar item, current (warm) default](components/crops/side-menu-item-warm-active-default.png)

#### Top bar question field
On inner pages the question field moves into the top bar: 640 x 40, white at 84%, a 1px #e4e6eb border, radius 30, image and send buttons. Sample text was typed and deleted. Read as `header-question` on the Insights page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, focused, filled) | size 640 x 40; background transparent; text `typography.field-lg`, `palette.indigo.upload-text`; icon 24 x 24, #333333† |

Child layers that carry the look: div 640x40 background rgba(255, 255, 255, 0.84)† border `borderWidth.hairline` solid `border.field` radius 30px†; div 1x14 background #c7c7cc†; div 30x30 background `background.selected` radius 15px†.

**Tokens.** `background.selected`, `border.field`, `borderWidth.hairline`, `palette.indigo.upload-text`, `typography.field-lg`.

![Top bar question field default](components/crops/header-question-default.png) ![Top bar question field hover](components/crops/header-question-hover.png) ![Top bar question field focused](components/crops/header-question-focused.png) ![Top bar question field filled](components/crops/header-question-filled.png)

### Homework home

The question-first home page: a serif hero over a lilac gradient, the question field, an upload panel and subject chips, then marketing sections. Nothing was ever sent or uploaded.

#### Homework hero
The first band of the home page: a pale lilac gradient ground, the two-line serif title, the question field, the upload panel and the subject chips. Read as `home-hero` on the Homework home page.

**Values (default).** size 1220 x 673; padding 0px 0px 70px† 0px; background transparent; image linear-gradient(0deg, rgba(245, 246, 255, 0)† -13.47%, `background.home` 0px); text `typography.hero`, `text.primary`; icon 29 x 28, `palette.ink.black`.

**Tokens.** `background.home`, `palette.ink.black`, `text.primary`, `typography.hero`.

![Homework hero default](components/crops/home-hero-default.png)

#### Hero title
"Your AI Study Helper / Gauth it, Ace it!" in Gauth Home Libre Baskerville; the second line is filled with a gradient through background-clip. Read as `home-title` on the Homework home page.

**Values (default).** size 680 x 104; background `action.primary`; image an image (data URI); text `typography.hero`, `text.primary`.

**Tokens.** `action.primary`, `text.primary`, `typography.hero`.

![Hero title default](components/crops/home-title-default.png)

#### Question field
The 680 x 64 pill the home page is built around: a faint indigo tint, a 2px indigo-alpha border, radius 38, a round white submit button at the right end. Text was typed and deleted; nothing was sent. Read as `question-box` on the Homework home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 680 x 64; padding `spacing-offgrid.10` `spacing.12` `spacing-offgrid.10` `spacing-offgrid.30`; border `borderWidth.strong` solid `component.question-field.border`; radius `radius.38`; background `component.question-field.background`; icon 29 x 28, `palette.ink.black` |
| hover, focused, filled | border `borderWidth.strong` solid `component.question-field.border-hover` |

**Tokens.** `borderWidth.strong`, `component.question-field.background`, `component.question-field.border`, `component.question-field.border-hover`, `palette.ink.black`, `radius.38`, `spacing-offgrid.10`, `spacing-offgrid.30`, `spacing.12`.

![Question field default](components/crops/question-box-default.png) ![Question field hover](components/crops/question-box-hover.png) ![Question field focused](components/crops/question-box-focused.png) ![Question field filled](components/crops/question-box-filled.png)

#### Question field input
Read as `question-input` on the Homework home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 562 x 48; radius `radius.12`; background transparent; text -apple-system 20/26 400†, `text.primary`; placeholder `component.question-field.placeholder` |

**Tokens.** `component.question-field.placeholder`, `radius.12`, `text.primary`.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Question submit button
The round white arrow button; measured, never pressed. Read as `question-submit` on the Homework home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 44 x 44; radius `radius.24`; background `action.secondary`; icon 29 x 28, `palette.ink.black` |
| hover | background `palette.indigo.tint-hover` |

**Tokens.** `action.secondary`, `palette.indigo.tint-hover`, `palette.ink.black`, `radius.24`.

![Question submit button default](components/crops/question-submit-default.png) ![Question submit button hover](components/crops/question-submit-hover.png)

#### Upload panel
The dashed drop zone under the field. Hovered only; no file was chosen. Read as `upload-panel` on the Homework home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 680 x 207; border `borderWidth.strong` dashed `component.question-field.border`; radius `radius.24`; background rgba(255, 255, 255, 0.4)†; text `typography.field-lg`, `palette.indigo.upload-text`; icon 30 x 30, `palette.ink.black` |
| hover | border `borderWidth.strong` dashed `palette.indigo.line-strong` |

**Tokens.** `borderWidth.strong`, `component.question-field.border`, `palette.indigo.line-strong`, `palette.indigo.upload-text`, `palette.ink.black`, `radius.24`, `typography.field-lg`.

![Upload panel default](components/crops/upload-panel-default.png) ![Upload panel hover](components/crops/upload-panel-hover.png)

#### Subject chip
Icon over label, 87 x 72, radius 10, in a muted grey-violet. Read as `subject-chip` on the Homework home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 87.25 x 72; radius `radius.10`; background transparent; text `typography.chip-label`, `component.subject-chip.text`; icon 29 x 29, `palette.ink.black` |
| hover | background `component.subject-chip.hover`; text `typography.chip-label`, `component.subject-chip.text-hover` |
| pressed | background `palette.indigo.chip-pressed`; text `typography.chip-label`, `component.subject-chip.text-hover` |

**Tokens.** `component.subject-chip.hover`, `component.subject-chip.text`, `component.subject-chip.text-hover`, `palette.indigo.chip-pressed`, `palette.ink.black`, `radius.10`, `typography.chip-label`.

![Subject chip default](components/crops/subject-chip-default.png) ![Subject chip hover](components/crops/subject-chip-hover.png) ![Subject chip focus-visible](components/crops/subject-chip-focus-visible.png) ![Subject chip pressed](components/crops/subject-chip-pressed.png)

#### More subjects chip
The "MORE" pill at the end of the chip row. Read as `subject-more` on the Homework home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 84.47 x 35; padding `spacing-offgrid.9` `spacing.12` `spacing-offgrid.9` `spacing.16`; radius `radius.18`; background `palette.indigo.more`; text -apple-system 14/normal 500†, `palette.indigo.more-text`; icon 12 x 12, `palette.ink.black` |
| hover | background #ececf5†; icon 12 x 12, #5c627f† |
| pressed | background #e6e7f2†; icon 12 x 12, #5c627f† |

**Tokens.** `palette.indigo.more`, `palette.indigo.more-text`, `palette.ink.black`, `radius.18`, `spacing-offgrid.9`, `spacing.12`, `spacing.16`.

![More subjects chip default](components/crops/subject-more-default.png) ![More subjects chip hover](components/crops/subject-more-hover.png) ![More subjects chip pressed](components/crops/subject-more-pressed.png)

#### Section headline
The marketing sections below the fold open with a 32/41.6 700 headline and a 16/24 500 grey line; a word can carry a gradient shine. Read as `atlas-band-title` on the Homework home page.

**Values (default).** size 960 x 115.59; padding 0px 0px `spacing.40` 0px; background transparent; text `typography.marketing-heading`, `text.primary`.

Child layers that carry the look: span 254x41.6 image linear-gradient(90deg, #8a6024†, #ff8d1f† 18%, #ff6404† 34%, rgb(.

**Tokens.** `spacing.40`, `text.primary`, `typography.marketing-heading`.

![Section headline default](components/crops/atlas-band-title-default.png)

#### Atlas showcase
A radius-48 panel with soft radial colour washes holding the copy, a CTA and a demo video. Read as `atlas-showcase` on the Homework home page.

**Values (default).** size 960 x 341; padding `spacing.28` `spacing.28` `spacing.28` 47px†; radius `radius.48`; background #fbf9ff†; image radial-gradient(420px 260px at 6% 92%, rgba(181, 197, 255, 0.76)†, transparent 72%), radial-gradient(360px 280px at 94% 5%, rgba(208, 222, 255, 0.88)†, transparent 72%), radial-gradient(440px ; text `typography.showcase-title`, `text.primary`; icon 20 x 20, `text.primary`.

**Tokens.** `radius.48`, `spacing.28`, `text.primary`, `typography.showcase-title`.

![Atlas showcase default](components/crops/atlas-showcase-default.png)

#### Start Exploring button
A dark radius-14 link button. Measured, never followed. Read as `atlas-cta` on the Homework home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 160 x 44; radius `radius.14`; background `action.primary`; text `typography.nav-strong`, `text.inverse`; icon 16 x 16, `text.inverse` |
| hover, pressed | background `palette.ink.hover-2` |

**Tokens.** `action.primary`, `palette.ink.hover-2`, `radius.14`, `text.inverse`, `typography.nav-strong`.

![Start Exploring button default](components/crops/atlas-cta-default.png) ![Start Exploring button hover](components/crops/atlas-cta-hover.png) ![Start Exploring button focus-visible](components/crops/atlas-cta-focus-visible.png) ![Start Exploring button pressed](components/crops/atlas-cta-pressed.png)

#### Feature card
White, 1px #5058651a border, radius 32: icon, 16/24 600 title, 14/21 grey line. Read as `feature-card` on the Homework home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 228 x 150; padding `spacing.20` `spacing.20` `spacing-offgrid.18` `spacing.20`; border `borderWidth.hairline` solid `border.control`; radius `radius.32`; background `background.card`; text `typography.card-title`, `text.primary`; icon 32 x 36, `text.primary` |

**Tokens.** `background.card`, `border.control`, `borderWidth.hairline`, `radius.32`, `spacing-offgrid.18`, `spacing.20`, `text.primary`, `typography.card-title`.

![Feature card default](components/crops/feature-card-default.png) ![Feature card hover](components/crops/feature-card-hover.png)

#### Solution option row
A radius-20 row with an icon, a 16/22 600 title and a 14/22 description. The rows take turns being the active one, which turns Gauth red (#ff013e) with white text and a red-tinted shadow; the measured row was active. Read as `solution-option` on the Homework home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 369.81 x 102; padding `spacing.16` `spacing.24` `spacing.16` `spacing.20`; radius `radius.20`; background `action.accent`; shadow 0px 7px 14px 0px rgba(168, 0, 0, 0.1)†; text -apple-system 16/22 600†, `text.inverse`; icon 24 x 24, `palette.ink.black` |

**Tokens.** `action.accent`, `palette.ink.black`, `radius.20`, `spacing.16`, `spacing.20`, `spacing.24`, `text.inverse`.

![Solution option row default](components/crops/solution-option-default.png) ![Solution option row hover](components/crops/solution-option-hover.png)

#### Live tutor band
A pink block with one oversized corner radius (54 54 200 54). Read as `live-tutor-band` on the Homework home page.

**Values (default).** size 960 x 349.2; radius 54px† 200px† 54px† 54px†; background `palette.brand.pink-band`; text `typography.dialog-display`, `palette.indigo.heading`; icon 13 x 10, `palette.indigo.heading`.

**Tokens.** `palette.brand.pink-band`, `palette.indigo.heading`, `typography.dialog-display`.

![Live tutor band default](components/crops/live-tutor-band-default.png)

#### Footer
White with a 1px #f5f5f7 top rule: brand line, email, socials and a language select, then Company, Legal and Download App columns. Read as `footer` on the Homework home page.

**Values (default).** size 1220 x 244; border T: `borderWidth.hairline` solid `component.progress.track`; background `background.card`; text -apple-system 20/26 600†, `text.primary`; icon 24 x 24, `text.primary`.

**Tokens.** `background.card`, `borderWidth.hairline`, `component.progress.track`, `text.primary`.

![Footer default](components/crops/footer-default.png)

#### Select (language)
The footer's language picker: an Ant Design select drawn as a blue underlined value and a chevron after a grey "Language" label. Read as `language-select` on the Homework home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 61.56 x 40; padding `spacing.4` `spacing-offgrid.11`; border `borderWidth.hairline` solid #d9d9d9†; radius `radius.6`; background `background.card`; text -apple-system 14/22 400†, `palette.antd.text`; transition all `duration.popover` `easing.ease`; icon 14 x 14, `palette.antd.disabled` |
| hover | border `borderWidth.hairline` solid #4096ff† |
| focus-visible | border `borderWidth.hairline` solid #1677ff†; shadow 0px 0px 0px 2px rgba(5, 145, 255, 0.1)† |

**Tokens.** `background.card`, `borderWidth.hairline`, `duration.popover`, `easing.ease`, `palette.antd.disabled`, `palette.antd.text`, `radius.6`, `spacing-offgrid.11`, `spacing.4`.

![Select (language) default](components/crops/language-select-default.png) ![Select (language) hover](components/crops/language-select-hover.png) ![Select (language) focus-visible](components/crops/language-select-focus-visible.png)

#### Select list (language)
The list the select opens upward: a 182px white popup, radius 8, a soft three-layer shadow, 16px rows, the current one on a grey fill. Opened and closed; no language chosen. Read as `language-list` on the Homework home page.

**Values (opened).** size 182 x 638; padding `spacing.4`; radius `radius.12`; background `background.card`; shadow 0px 6px 16px 0px rgba(0, 0, 0, 0.08), 0px 3px 6px -4px rgba(0, 0, 0, 0.12), 0px 9px 28px 8px rgba(0, 0, 0, 0.05)†; text `typography.select-option`, `palette.antd.text`.

**Tokens.** `background.card`, `palette.antd.text`, `radius.12`, `spacing.4`, `typography.select-option`.

![Select list (language) opened](components/crops/language-list-opened.png)

#### Select option, current
Read as `language-option-selected` on the Homework home page.

**Values (selected).** size 174 x 40; padding `spacing-offgrid.5` `spacing.12`; radius `radius.8`; background `palette.slate.divider`; text `typography.select-option`, `palette.antd.text`; transition background-color `duration.popover` `easing.ease`.

**Tokens.** `duration.popover`, `easing.ease`, `palette.antd.text`, `palette.slate.divider`, `radius.8`, `spacing-offgrid.5`, `spacing.12`, `typography.select-option`.

![Select option, current selected](components/crops/language-option-selected-selected.png)

#### Select option
Hovered only. Read as `language-option` on the Homework home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 174 x 40; padding `spacing-offgrid.5` `spacing.12`; radius `radius.8`; background transparent; text -apple-system 14/40 400†, `palette.antd.text`; transition background-color `duration.popover` `easing.ease` |
| hover | background `palette.paper.hairline` |

**Tokens.** `duration.popover`, `easing.ease`, `palette.antd.text`, `palette.paper.hairline`, `radius.8`, `spacing-offgrid.5`, `spacing.12`.

![Select option default](components/crops/language-option-default.png) ![Select option hover](components/crops/language-option-hover.png)

#### Inline link (Learn More)
The blue link closing the honor-code line above the footer. Hovered and focused, never followed. Read as `inline-link` on the Homework home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 82.53 x 18; background transparent; text `typography.body`, `text.link` |
| hover | text `typography.body`, `text.meta` |

**Tokens.** `text.link`, `text.meta`, `typography.body`.

![Inline link (Learn More) default](components/crops/inline-link-default.png) ![Inline link (Learn More) hover](components/crops/inline-link-hover.png) ![Inline link (Learn More) focus-visible](components/crops/inline-link-focus-visible.png)

#### Footer link
Read as `footer-link` on the Homework home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 113.22 x 21; background transparent; text -apple-system 14/21 400, letter spacing 0.09px†, `text.primary` |
| hover | text -apple-system 14/21 400, letter spacing 0.09px†, `text.link` |

**Tokens.** `text.link`, `text.primary`.

![Footer link default](components/crops/footer-link-default.png) ![Footer link hover](components/crops/footer-link-hover.png) ![Footer link focus-visible](components/crops/footer-link-focus-visible.png)

#### Avatar (review)
A reviewer's 40px picture beside their name and star rating; Gauth uses mascot illustrations, square, with no radius or ring. Read as `review-avatar` on the Homework home page.

**Values (default).** size 40 x 40; background transparent.

![Avatar (review) default](components/crops/review-avatar-default.png)

#### Review card
A 392 x 320 tinted card at radius 32 (pale lilac, the active slide pale pink) with the avatar, name, a 5.0 star row and the quote. Read as `review-card` on the Homework home page.

**Values (default).** size 392 x 320; padding 44px† 44px† 31px† 44px†; radius `radius.32`; background #f8f9ff†; text -apple-system 16/24 500†, rgba(31, 37, 86, 0.6)†; icon 16 x 16, rgba(31, 37, 86, 0.6)†.

**Tokens.** `radius.32`.

![Review card default](components/crops/review-card-default.png)

### Academy catalogue

The course catalogue: the Playfair title and Create Course, four category tabs, then course sections of card grids. Science Labs and History Signature use cover cards with a progress track; Math Curriculum uses unit cards with an 80px cover tile.

#### Academy page
The catalogue page: #faf9f5 ground under a transparent top bar, the warm sidebar, a 1025px column. Read as `academy-ground` on the Academy (Science Labs) page.

**Values (default).** size 1220 x 2094.38; background `background.academy`; text `typography.label`, `text.primary`; icon 20 x 20, `text.primary`.

**Tokens.** `background.academy`, `text.primary`, `typography.label`.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Academy title
"Gauth Academy" in Playfair Display 700 at 36px. Read as `academy-title` on the Academy (Science Labs) page.

**Values (default).** size 259.25 x 48; background transparent; text Playfair Display 36/normal 700†, `text.primary`.

**Tokens.** `text.primary`.

![Academy title default](components/crops/academy-title-default.png)

#### Create Course button
A pale blue pill: an image fill of a soft blue-to-cream gradient, a 1px #d5e3f4 border, radius 12, a sparkle icon and SF Pro 14/21 500. Read as `create-course-button` on the Academy (Science Labs) page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 140.83 x 37; padding 0px `spacing-offgrid.10`; border `borderWidth.hairline` solid `component.create-course.border`; radius `radius.12`; background `component.create-course.background`; image an image (data URI); text `typography.label`, `text.primary`; icon 20 x 20, `text.primary` |
| hover | border `borderWidth.hairline` solid `component.create-course.border-hover` |
| pressed | size 138.01 x 36.26; border `borderWidth.hairline` solid `component.create-course.border-hover`; transform scale `scale.press`; icon 19.6 x 19.6, `text.primary` |

**Tokens.** `borderWidth.hairline`, `component.create-course.background`, `component.create-course.border`, `component.create-course.border-hover`, `radius.12`, `scale.press`, `spacing-offgrid.10`, `text.primary`, `typography.label`.

![Create Course button default](components/crops/create-course-button-default.png) ![Create Course button hover](components/crops/create-course-button-hover.png) ![Create Course button focus-visible](components/crops/create-course-button-focus-visible.png) ![Create Course button pressed](components/crops/create-course-button-pressed.png)

#### Category tab, current
The current catalogue tab: #f4ebe5 fill, transparent border, 700 label. Read as `category-tab-active` on the Academy (Science Labs) page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 122.98 x 36; padding 0px `spacing-offgrid.15`; border `borderWidth.hairline` solid transparent; radius `radius.12`; background `component.category-tab.current`; text `typography.tab-strong`, `text.primary` |

**Tokens.** `borderWidth.hairline`, `component.category-tab.current`, `radius.12`, `spacing-offgrid.15`, `text.primary`, `typography.tab-strong`.

![Category tab, current default](components/crops/category-tab-active-default.png) ![Category tab, current focus-visible](components/crops/category-tab-active-focus-visible.png)

#### Category tab
A 36px tab with a 1px #5058651a border, radius 12, 14/19.6 grey label. Read as `category-tab` on the Academy (Science Labs) page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 139.19 x 36; padding 0px `spacing-offgrid.15`; border `borderWidth.hairline` solid `component.category-tab.border`; radius `radius.12`; background transparent; text `typography.tab`, `component.category-tab.text` |
| hover, pressed | background `component.category-tab.hover`; text `typography.tab`, `text.primary` |

**Tokens.** `borderWidth.hairline`, `component.category-tab.border`, `component.category-tab.hover`, `component.category-tab.text`, `radius.12`, `spacing-offgrid.15`, `text.primary`, `typography.tab`.

![Category tab default](components/crops/category-tab-default.png) ![Category tab hover](components/crops/category-tab-hover.png) ![Category tab focus-visible](components/crops/category-tab-focus-visible.png) ![Category tab pressed](components/crops/category-tab-pressed.png)

#### Course section heading
An 80px rounded cover beside a 22/28.6 600 title and a 16/22.4 grey line. Read as `section-heading` on the Academy (Science Labs) page.

**Values (default).** size 1025 x 80; background transparent; text `typography.section-heading`, `text.primary`.

**Tokens.** `text.primary`, `typography.section-heading`.

![Course section heading default](components/crops/section-heading-default.png)

#### Course section
One course: its heading and a three-column card grid, closed by a 1px #e7e6e3 rule. Read as `course-section` on the Academy (Science Labs) page.

**Values (default).** size 1025 x 464.09; padding `spacing-offgrid.29` 0px `spacing.36` 0px; border B: `borderWidth.hairline` solid `border.rule`; background transparent; text `typography.section-heading`, `text.primary`.

Child layers that carry the look: section 1025x464.1 border `borderWidth.hairline` solid `border.rule`; a 325.7x294.1 background `background.card` border `borderWidth.hairline` solid `border.card` radius `radius.16` shadow `elevation.level-1`; div 283.7x6 background `background.selected` radius `radius.4`.

**Tokens.** `background.card`, `background.selected`, `border.card`, `border.rule`, `borderWidth.hairline`, `elevation.level-1`, `radius.16`, `radius.4`, `spacing-offgrid.29`, `spacing.36`, `text.primary`, `typography.section-heading`.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Lesson card (Science Labs, History Signature)
A white card, 1px rgba(0,0,0,.08) border, radius 16, a 0 4 7 shadow at 4%: a 147px cover inset 9px at radius 12, a 700 category label, a 16/24 600 title, a 12/16.8 subtitle and a 6px progress track. Read as `lesson-card` on the Academy (Science Labs) page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 325.66 x 294.09; padding `spacing.8` `spacing.8` `spacing.16` `spacing.8`; border `borderWidth.hairline` solid `border.card`; radius `radius.16`; background `background.card`; shadow `elevation.level-1`; text `typography.caption-strong`, `text.meta`; transition box-shadow `duration.fast` `easing.ease` |
| hover | shadow `elevation.level-2` |
| pressed | border `borderWidth.hairline` solid `palette.slate.pressed-line`; shadow `elevation.level-2` |

**Tokens.** `background.card`, `border.card`, `borderWidth.hairline`, `duration.fast`, `easing.ease`, `elevation.level-1`, `elevation.level-2`, `palette.slate.pressed-line`, `radius.16`, `spacing.16`, `spacing.8`, `text.meta`, `typography.caption-strong`.

![Lesson card (Science Labs, History Signature) default](components/crops/lesson-card-default.png) ![Lesson card (Science Labs, History Signature) hover](components/crops/lesson-card-hover.png) ![Lesson card (Science Labs, History Signature) focus-visible](components/crops/lesson-card-focus-visible.png) ![Lesson card (Science Labs, History Signature) pressed](components/crops/lesson-card-pressed.png)

#### Lesson card category
Read as `lesson-card-category` on the Academy (Science Labs) page.

**Values (default).** size 283.66 x 16.8; background transparent; text `typography.caption-strong`, `text.meta`.

**Tokens.** `text.meta`, `typography.caption-strong`.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Lesson card title
Read as `lesson-card-title` on the Academy (Science Labs) page.

**Values (default).** size 283.66 x 24; background transparent; text `typography.card-title`, `text.primary`.

**Tokens.** `text.primary`, `typography.card-title`.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Lesson card subtitle
Read as `lesson-card-subtitle` on the Academy (Science Labs) page.

**Values (default).** size 283.66 x 16.8; background transparent; text `typography.caption`, `text.meta`.

**Tokens.** `text.meta`, `typography.caption`.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Lesson card progress track
Read as `lesson-card-progress` on the Academy (Science Labs) page.

**Values (default).** size 283.66 x 6; radius `radius.4`; background `background.selected`.

**Tokens.** `background.selected`, `radius.4`.

![Lesson card progress track default](components/crops/lesson-card-progress-default.png)

#### Unit card (Math Curriculum)
A white card 326 x 178: an 80px cover tile at radius 12 beside an Inter 17/23.8 600 title, a "Unit 1 | 42 Topics" meta line and a 6px pill track. Read as `unit-card` on the Academy (Math Curriculum) page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 325.66 x 178; padding `spacing.20`; border `borderWidth.hairline` solid `border.card`; radius `radius.16`; background `background.card`; shadow `elevation.level-1`; text `typography.unit-card-title`, `text.primary`; transition box-shadow `duration.fast` `easing.ease` |
| hover, pressed | shadow `elevation.level-2` |

**Tokens.** `background.card`, `border.card`, `borderWidth.hairline`, `duration.fast`, `easing.ease`, `elevation.level-1`, `elevation.level-2`, `radius.16`, `spacing.20`, `text.primary`, `typography.unit-card-title`.

![Unit card (Math Curriculum) default](components/crops/unit-card-default.png) ![Unit card (Math Curriculum) hover](components/crops/unit-card-hover.png) ![Unit card (Math Curriculum) focus-visible](components/crops/unit-card-focus-visible.png) ![Unit card (Math Curriculum) pressed](components/crops/unit-card-pressed.png)

#### Unit card title
Read as `unit-card-title` on the Academy (Math Curriculum) page.

**Values (default).** size 187.66 x 47.59; background transparent; text `typography.unit-card-title`, `text.primary`.

**Tokens.** `text.primary`, `typography.unit-card-title`.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Unit card meta line
Read as `unit-card-meta` on the Academy (Math Curriculum) page.

**Values (default).** size 283.66 x 20; background transparent; text `typography.meta`, `text.meta`.

Child layers that carry the look: span::before 1pxx12px background `palette.slate.meta-rule`.

**Tokens.** `palette.slate.meta-rule`, `text.meta`, `typography.meta`.

![Unit card meta line default](components/crops/unit-card-meta-default.png)

#### Unit card progress track
Read as `unit-card-progress` on the Academy (Math Curriculum) page.

**Values (default).** size 283.66 x 6; radius `radius.999`; background `component.progress.track-unit`.

**Tokens.** `component.progress.track-unit`, `radius.999`.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Show more button
"Show 14 more" with a chevron: 1px #e0e3e8 border, radius 12, 14/19.6 grey. Pressing it lists the remaining units as compact rows. Read as `show-more` on the Academy (Math Curriculum) page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 145.28 x 40; padding 0px `spacing.16`; border `borderWidth.hairline` solid `component.show-more.border`; radius `radius.12`; background transparent; text Arial 14/19.6 400†, `text.meta`; icon 14 x 14, `text.meta` |
| hover | border `borderWidth.hairline` solid `component.show-more.border-hover`; background `component.show-more.hover`; text Arial 14/19.6 400†, `text.primary`; icon 14 x 14, `text.primary` |
| pressed | border `borderWidth.hairline` solid `component.show-more.border-hover`; background `component.show-more.pressed`; text Arial 14/19.6 400†, `text.primary`; icon 14 x 14, `text.primary` |
| expanded | size 118.81 x 40 |

**Tokens.** `borderWidth.hairline`, `component.show-more.border`, `component.show-more.border-hover`, `component.show-more.hover`, `component.show-more.pressed`, `radius.12`, `spacing.16`, `text.meta`, `text.primary`.

![Show more button default](components/crops/show-more-default.png) ![Show more button hover](components/crops/show-more-hover.png) ![Show more button focus-visible](components/crops/show-more-focus-visible.png) ![Show more button pressed](components/crops/show-more-pressed.png) ![Show more button expanded](components/crops/show-more-expanded.png)

#### Unit card revealed by Show more
Show more reveals the units past the sixth as the same cards. Read as `unit-row` on the Academy (Math Curriculum) page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 325.66 x 178; padding `spacing.20`; border `borderWidth.hairline` solid `border.card`; radius `radius.16`; background `background.card`; shadow `elevation.level-1`; text `typography.unit-card-title`, `text.primary`; transition box-shadow `duration.fast` `easing.ease` |
| hover | shadow `elevation.level-2` |

**Tokens.** `background.card`, `border.card`, `borderWidth.hairline`, `duration.fast`, `easing.ease`, `elevation.level-1`, `elevation.level-2`, `radius.16`, `spacing.20`, `text.primary`, `typography.unit-card-title`.

![Unit card revealed by Show more default](components/crops/unit-row-default.png) ![Unit card revealed by Show more hover](components/crops/unit-row-hover.png) ![Unit card revealed by Show more focus-visible](components/crops/unit-row-focus-visible.png)

#### History lesson card
The same card as Science Labs with a full-bleed illustrated cover. Read as `history-card` on the Academy (History Signature) page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 325.66 x 264.25; padding `spacing.8` `spacing.8` `spacing.16` `spacing.8`; border `borderWidth.hairline` solid `border.card`; radius `radius.16`; background `background.card`; shadow `elevation.level-1`; text `typography.caption-strong`, `text.meta`; transition box-shadow `duration.fast` `easing.ease` |
| hover | shadow `elevation.level-2` |

**Tokens.** `background.card`, `border.card`, `borderWidth.hairline`, `duration.fast`, `easing.ease`, `elevation.level-1`, `elevation.level-2`, `radius.16`, `spacing.16`, `spacing.8`, `text.meta`, `typography.caption-strong`.

![History lesson card default](components/crops/history-card-default.png) ![History lesson card hover](components/crops/history-card-hover.png)

#### My Course empty state
A fan of three course cards, a 20px 600 title, a grey line and a dark Create button. Read as `my-empty` on the Academy (My Course) page.

**Values (default).** size 1025 x 557; padding `spacing.36` 0px; background transparent; text `typography.empty-title`, `palette.ink.black`.

Child layers that carry the look: button 120x44 background `action.primary` radius `radius.12`.

**Tokens.** `action.primary`, `palette.ink.black`, `radius.12`, `spacing.36`, `typography.empty-title`.

![My Course empty state default](components/crops/my-empty-default.png)

#### Create button (empty state)
The dark primary button: #21252e, radius 12, 44px, white 16/22.4 500. Hover lightens it to #333943; pressed also scales it to 0.98. Measured, never pressed. Read as `create-button` on the Academy (My Course) page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 120 x 44; padding 0px `spacing-offgrid.18`; radius `radius.12`; background `action.primary`; text Arial 16/22.4 500†, `text.inverse` |
| hover | background `action.primary-hover` |
| pressed | size 117.6 x 43.12; background `action.primary-hover`; transform scale `scale.press` |

**Tokens.** `action.primary`, `action.primary-hover`, `radius.12`, `scale.press`, `spacing-offgrid.18`, `text.inverse`.

![Create button (empty state) default](components/crops/create-button-default.png) ![Create button (empty state) hover](components/crops/create-button-hover.png) ![Create button (empty state) focus-visible](components/crops/create-button-focus-visible.png) ![Create button (empty state) pressed](components/crops/create-button-pressed.png)

### Unit page

A math course's page: a back link, a tinted course banner, the unit rail at the left and the topic path at the right, with a floating Start panel.

#### Back link
An arrow and the catalogue tab name, SF Pro 16/22.4 in #646a77. Read as `back-link` on the unit page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, focus-visible) | size 148.05 x 22.39; background transparent; text SF Pro 20/20 400†, `text.meta` |

**Tokens.** `text.meta`.

![Back link default](components/crops/back-link-default.png) ![Back link hover](components/crops/back-link-hover.png) ![Back link focus-visible](components/crops/back-link-focus-visible.png)

#### Course banner
A radius-20 band tinted with the course colour (Algebra 1 is green #ecf4e5): an SF Pro 22/28.6 700 course title, a lessons and topics count, a 7px progress bar and the percent. Read as `course-banner` on the unit page.

**Values (default).** size 1025 x 89; padding `spacing.16` `spacing.20` `spacing.16` `spacing.28`; radius `radius.20`; background `component.unit.banner`; text `typography.course-title`, `text.primary`.

**Tokens.** `component.unit.banner`, `radius.20`, `spacing.16`, `spacing.20`, `spacing.28`, `text.primary`, `typography.course-title`.

![Course banner default](components/crops/course-banner-default.png)

#### Unit rail
The 310px list of units: a 1px rgba(0,0,0,.04) border, radius 16; the current unit is marked by a 5px green bar on its ::before and green #3c6b26 text. Read as `unit-rail` on the unit page.

**Values (default).** size 310 x 632; padding `spacing.4` `spacing.4` `spacing.4` 0px; border `borderWidth.hairline` solid `border.hairline`; radius `radius.16`; background transparent; text `typography.rail-meta`, `component.unit.current`.

**Tokens.** `border.hairline`, `borderWidth.hairline`, `component.unit.current`, `radius.16`, `spacing.4`, `typography.rail-meta`.

![Unit rail default](components/crops/unit-rail-default.png)

#### Unit rail item, current
Read as `unit-button-active` on the unit page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 304 x 62; padding `spacing-offgrid.10` `spacing.16`; radius `radius.12`; background transparent; text `typography.rail-meta`, `component.unit.current` |

Child layers that carry the look: button::before 5pxx42px background `component.unit.current`.

**Tokens.** `component.unit.current`, `radius.12`, `spacing-offgrid.10`, `spacing.16`, `typography.rail-meta`.

![Unit rail item, current default](components/crops/unit-button-active-default.png) ![Unit rail item, current focus-visible](components/crops/unit-button-active-focus-visible.png)

#### Unit rail item
A 62px row: 12/16.8 "Unit n" over a 14/21 700 title. Read as `unit-button` on the unit page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 304 x 62; padding `spacing-offgrid.10` `spacing.16`; radius `radius.12`; background transparent; text `typography.rail-meta`, `text.meta` |
| hover | background `component.unit.row-hover` |
| pressed | background `component.unit.row-pressed` |

**Tokens.** `component.unit.row-hover`, `component.unit.row-pressed`, `radius.12`, `spacing-offgrid.10`, `spacing.16`, `text.meta`, `typography.rail-meta`.

![Unit rail item default](components/crops/unit-button-default.png) ![Unit rail item hover](components/crops/unit-button-hover.png) ![Unit rail item pressed](components/crops/unit-button-pressed.png)

#### Unit header
A white-on-ground header card with radius 20 over the topic path. Read as `unit-header` on the unit page.

**Values (default).** size 683 x 84; padding `spacing-offgrid.18` 38px† `spacing.12` 38px†; border `borderWidth.hairline` solid `border.hairline`; radius `radius.20`; background transparent; text SF Pro 12/18 500†, `text.meta`.

**Tokens.** `border.hairline`, `borderWidth.hairline`, `radius.20`, `spacing-offgrid.18`, `spacing.12`, `text.meta`.

![Unit header default](components/crops/unit-header-default.png)

#### Topic path
Topics as round coin buttons on a winding dotted connector, the label to the right; the current topic has a halo ring. Read as `topic-path` on the unit page.

**Values (default).** size 457 x 553; background transparent; text `typography.topic`, `text.primary`.

**Tokens.** `text.primary`, `typography.topic`.

![Topic path default](components/crops/topic-path-default.png)

#### Topic node, current
Read as `topic-node-current` on the unit page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, focus-visible) | size 316 x 105; background transparent; text `typography.topic`, `text.primary`; icon 108 x 105, `text.primary` |

**Tokens.** `text.primary`, `typography.topic`.

![Topic node, current default](components/crops/topic-node-current-default.png) ![Topic node, current hover](components/crops/topic-node-current-hover.png) ![Topic node, current focus-visible](components/crops/topic-node-current-focus-visible.png)

#### Topic node, not started
A pale coin with a star and a grey label. Read as `topic-node` on the unit page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 332 x 108; padding `spacing-offgrid.10`; background transparent; text SF Pro 15/21 500†, `text.tertiary`; icon 96 x 88, `text.tertiary` |
| hover | text SF Pro 15/21 500†, `text.meta`; icon 96 x 88, `text.meta` |
| pressed | text SF Pro 15/21 500†, `text.meta`; icon 94.08 x 86.24, `text.meta` |

**Tokens.** `spacing-offgrid.10`, `text.meta`, `text.tertiary`.

![Topic node, not started default](components/crops/topic-node-default.png) ![Topic node, not started hover](components/crops/topic-node-hover.png) ![Topic node, not started focus-visible](components/crops/topic-node-focus-visible.png) ![Topic node, not started pressed](components/crops/topic-node-pressed.png)

#### Start panel
The floating card under the current topic: white, a 1px #5058651a border, radius 28, a 0 12 14 shadow tinted navy at 14%, a 17/23.8 700 topic title and a full-width dark Start button. Read as `learning-panel` on the unit page.

**Values (default).** size 460 x 145.8; padding `spacing-offgrid.26` `spacing.24` `spacing-offgrid.22` `spacing.24`; border `borderWidth.hairline` solid `border.control`; radius `radius.28`; background `background.card`; shadow `elevation.start-panel`; text `typography.panel-title`, `text.primary`.

**Tokens.** `background.card`, `border.control`, `borderWidth.hairline`, `elevation.start-panel`, `radius.28`, `spacing-offgrid.22`, `spacing-offgrid.26`, `spacing.24`, `text.primary`, `typography.panel-title`.

![Start panel default](components/crops/learning-panel-default.png)

#### Start button
The primary button: #21252e, radius 12, 48px, white 16/24 700, with a moving light sheen drawn on ::after. Pressed scales it to 0.98. Read as `start-button` on the unit page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, focus-visible) | size 410 x 48; radius `radius.12`; background `action.primary`; text `typography.button-lg`, `text.inverse` |
| pressed | size 401.8 x 47.04; transform scale `scale.press` |

**Tokens.** `action.primary`, `radius.12`, `scale.press`, `text.inverse`, `typography.button-lg`.

![Start button default](components/crops/start-button-default.png) ![Start button hover](components/crops/start-button-hover.png) ![Start button focus-visible](components/crops/start-button-focus-visible.png) ![Start button pressed](components/crops/start-button-pressed.png)

### Lesson player: science canvas

The science player is built in Astryx, a separate design system (`astryx-*` classes, StyleX variables, the "stone" theme): a narrated canvas that pans by itself, a section rail, transport controls and a docked Ask Tutor bar. Its focus ring is the only blue one on the site.

#### Lesson header
Exit button and the lesson title in Playfair Display 16/21 600 at the left; the transport (previous, play or pause, next), Reset view and Settings at the right, all 32px round ghost buttons. Read as `canvas-header` on the science lesson page.

**Values (default).** size 1396 x 40; background transparent; text `typography.lesson-title`, `text.primary`; icon 40 x 40, `component.section-rail.indicator`.

Child layers that carry the look: div 0x0 background `component.section-rail.indicator` radius `radius.12`; div 0x0 background `component.section-rail.indicator` radius `radius.12`; div 0x0 background `component.section-rail.indicator` radius `radius.12`.

**Tokens.** `component.section-rail.indicator`, `radius.12`, `text.primary`, `typography.lesson-title`.

![Lesson header default](components/crops/canvas-header-default.png)

#### Exit button
Read as `canvas-exit` on the science lesson page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 40 x 40; radius `radius.pill`; background transparent; text `typography.callout`, `component.section-rail.indicator`; transition background-image `duration.astryx` `easing.astryx`, background-color `duration.astryx` `easing.astryx`, color `duration.astryx` `easing.astryx`, opacity `duration.astryx` `easing.astryx`, transform `duration.astryx` `easing.astryx`; icon 40 x 40, `component.section-rail.indicator` |
| hover | image linear-gradient(`action.ghost-hover`, `action.ghost-hover`) |
| focus-visible | outline `focus.width` solid `border.focus`, offset `focus.offset-astryx` |
| pressed | size 39.2 x 39.2; image linear-gradient(`action.ghost-pressed`, `action.ghost-pressed`); transform scale `scale.press`; icon 39.2 x 39.2, `component.section-rail.indicator` |

**Tokens.** `action.ghost-hover`, `action.ghost-pressed`, `border.focus`, `component.section-rail.indicator`, `duration.astryx`, `easing.astryx`, `focus.offset-astryx`, `focus.width`, `radius.pill`, `scale.press`, `typography.callout`.

![Exit button default](components/crops/canvas-exit-default.png) ![Exit button hover](components/crops/canvas-exit-hover.png) ![Exit button focus-visible](components/crops/canvas-exit-focus-visible.png) ![Exit button pressed](components/crops/canvas-exit-pressed.png)

#### Transport and view buttons
A 32px round ghost button holding a 32px icon. Hover lays a 5% ink film over it, pressed 10% and a 0.98 scale; keyboard focus draws Astryx's 2px #0064e0 ring 3px out. Read as `canvas-control` on the science lesson page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 32 x 32; radius `radius.pill`; background transparent; text `typography.callout`, `component.section-rail.indicator`; transition background-image `duration.astryx` `easing.astryx`, background-color `duration.astryx` `easing.astryx`, color `duration.astryx` `easing.astryx`, opacity `duration.astryx` `easing.astryx`, transform `duration.astryx` `easing.astryx`; icon 32 x 32, `component.section-rail.indicator` |
| hover | image linear-gradient(`action.ghost-hover`, `action.ghost-hover`) |
| focus-visible | outline `focus.width` solid `border.focus`, offset `focus.offset-astryx` |
| pressed | size 31.36 x 31.36; image linear-gradient(`action.ghost-pressed`, `action.ghost-pressed`); transform scale `scale.press`; icon 31.36 x 31.36, `component.section-rail.indicator` |

**Tokens.** `action.ghost-hover`, `action.ghost-pressed`, `border.focus`, `component.section-rail.indicator`, `duration.astryx`, `easing.astryx`, `focus.offset-astryx`, `focus.width`, `radius.pill`, `scale.press`, `typography.callout`.

![Transport and view buttons default](components/crops/canvas-control-default.png) ![Transport and view buttons hover](components/crops/canvas-control-hover.png) ![Transport and view buttons focus-visible](components/crops/canvas-control-focus-visible.png) ![Transport and view buttons pressed](components/crops/canvas-control-pressed.png)

#### Section rail
The right-hand outline: right-aligned 14/20 section names beside a 2px track whose dark segment marks the current section. Read as `canvas-outline` on the science lesson page.

**Values (default).** size 240 x 118; background transparent; text `typography.rail-current`, `component.section-rail.indicator`; transform translate(0px, -59px).

Child layers that carry the look: span 2x118 background `component.section-rail.track` radius `radius.pill`; span 2x28 background `component.section-rail.indicator` radius `radius.pill`.

**Tokens.** `component.section-rail.indicator`, `component.section-rail.track`, `radius.pill`, `typography.rail-current`.

![Section rail default](components/crops/canvas-outline-default.png)

#### Section rail item, current
Read as `outline-item-active` on the science lesson page.

**Values (default).** size 236 x 28; padding `spacing.4` `spacing.12` `spacing.4` `spacing.8`; radius `radius.8`; background transparent; text `typography.rail-current`, `component.section-rail.indicator`; transition background-color `duration.astryx` `easing.astryx`, color `duration.astryx` `easing.astryx`.

**Tokens.** `component.section-rail.indicator`, `duration.astryx`, `easing.astryx`, `radius.8`, `spacing.12`, `spacing.4`, `spacing.8`, `typography.rail-current`.

![Section rail item, current default](components/crops/outline-item-active-default.png)

#### Section rail item
Read as `outline-item` on the science lesson page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 236 x 28; padding `spacing.4` `spacing.12` `spacing.4` `spacing.8`; radius `radius.8`; background transparent; text `typography.rail`, `component.section-rail.text`; transition background-color `duration.astryx` `easing.astryx`, color `duration.astryx` `easing.astryx` |
| hover | background `action.ghost-hover`; text `typography.rail`, `component.section-rail.indicator` |
| focus-visible | outline `focus.width` solid `border.focus`, offset `focus.offset-astryx` |

**Tokens.** `action.ghost-hover`, `border.focus`, `component.section-rail.indicator`, `component.section-rail.text`, `duration.astryx`, `easing.astryx`, `focus.offset-astryx`, `focus.width`, `radius.8`, `spacing.12`, `spacing.4`, `spacing.8`, `typography.rail`.

![Section rail item default](components/crops/outline-item-default.png) ![Section rail item hover](components/crops/outline-item-hover.png) ![Section rail item focus-visible](components/crops/outline-item-focus-visible.png)

#### Ask Tutor bar
The compact pill docked at the bottom centre: white, 1px #e2e2e8 border, radius 9999, a two-layer soft shadow, the Gauth mascot, an "Ask Tutor" placeholder and a microphone button. It widens to 820px when opened (0.26s). Read as `ask-tutor` on the science lesson page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 820 x 52; border `borderWidth.hairline` solid `component.ask-tutor.border`; radius `radius.pill`; background `background.card`; shadow `elevation.ask-tutor`; text `typography.field`, `component.ask-tutor.placeholder`; transition width `duration.ask-tutor` `easing.ask-tutor`; icon 40 x 40, `palette.ink.black` |

**Tokens.** `background.card`, `borderWidth.hairline`, `component.ask-tutor.border`, `component.ask-tutor.placeholder`, `duration.ask-tutor`, `easing.ask-tutor`, `elevation.ask-tutor`, `palette.ink.black`, `radius.pill`, `typography.field`.

![Ask Tutor bar default](components/crops/ask-tutor-default.png) ![Ask Tutor bar hover](components/crops/ask-tutor-hover.png)

#### Ask Tutor microphone button
Measured, never pressed. Read as `ask-tutor-mic` on the science lesson page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 40 x 40; radius 50%†; background transparent; text Arial 13.33/normal 400†, `palette.ink.black`; icon 40 x 40, `palette.ink.black` |
| focus-visible | outline `focus.width` solid `palette.ink.black`, offset `focus.offset` |

**Tokens.** `focus.offset`, `focus.width`, `palette.ink.black`.

![Ask Tutor microphone button default](components/crops/ask-tutor-mic-default.png) ![Ask Tutor microphone button hover](components/crops/ask-tutor-mic-hover.png) ![Ask Tutor microphone button focus-visible](components/crops/ask-tutor-mic-focus-visible.png)

#### Ask Tutor bar, opened
Clicking the bar widens it into a text field. Sample text was typed and deleted; no message was sent. Read as `ask-tutor-open` on the science lesson page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| opened | size 820 x 52; border `borderWidth.hairline` solid `component.ask-tutor.border`; radius `radius.pill`; background `background.card`; shadow `elevation.ask-tutor`; text `typography.field`, `component.ask-tutor.placeholder`; transition width `duration.ask-tutor` `easing.ask-tutor`; icon 40 x 40, `palette.ink.black` |
| filled | text `typography.field`, `palette.ink.story` |

**Tokens.** `background.card`, `borderWidth.hairline`, `component.ask-tutor.border`, `component.ask-tutor.placeholder`, `duration.ask-tutor`, `easing.ask-tutor`, `elevation.ask-tutor`, `palette.ink.black`, `palette.ink.story`, `radius.pill`, `typography.field`.

![Ask Tutor bar, opened opened](components/crops/ask-tutor-open-opened.png) ![Ask Tutor bar, opened filled](components/crops/ask-tutor-open-filled.png)

#### Settings popover
Speed, Narration and Captions switches, a Zoom stepper and Export PDF (not pressed): a white card with a 1px #f2f2f2 border, radius 24 and a 0 8 14 shadow at 9%. Read as `settings-popover` on the science lesson page.

**Values (opened).** size 298 x 246; radius `radius.24`; background transparent; text `typography.menu`, `palette.astryx.menu-ink`; icon 20 x 20, `palette.astryx.menu-ink`.

Child layers that carry the look: section 298x246 background `background.card` border `borderWidth.hairline` solid `palette.astryx.popover-line` radius `radius.24` shadow `elevation.level-3`; button 119x32 background `palette.astryx.menu-fill` radius `radius.pill`.

**Tokens.** `background.card`, `borderWidth.hairline`, `elevation.level-3`, `palette.astryx.menu-fill`, `palette.astryx.menu-ink`, `palette.astryx.popover-line`, `radius.24`, `radius.pill`, `typography.menu`.

![Settings popover opened](components/crops/settings-popover-opened.png)

#### Switch
A Settings row holding the Narration toggle, off: 44px, radius 12; hover fills it #f3f3f3 and keyboard focus draws a 2px #307aff ring inside. Not toggled. Read as `switch` on the science lesson page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 264 x 44; padding 0px `spacing.8`; radius `radius.12`; background transparent; text `typography.menu`, `palette.astryx.menu-ink`; icon 36 x 36, `palette.astryx.menu-ink` |
| hover | background `background.hover` |
| focus-visible | background `background.hover`; outline `focus.width` solid `palette.blue.focus-2`, offset `focus.offset-inset` |

**Tokens.** `background.hover`, `focus.offset-inset`, `focus.width`, `palette.astryx.menu-ink`, `palette.blue.focus-2`, `radius.12`, `spacing.8`, `typography.menu`.

![Switch default](components/crops/switch-default.png) ![Switch hover](components/crops/switch-hover.png) ![Switch focus-visible](components/crops/switch-focus-visible.png)

#### Chapter title
"Canvas Chapter", which is Libre Baskerville Bold, 24/30. Read as `chapter-title` on the science lesson page.

**Values (default).** size 470 x 57; padding 27px† `spacing-offgrid.26` 0px `spacing.32`; background transparent; text `typography.chapter-title`, `palette.astryx.chapter-ink`.

**Tokens.** `palette.astryx.chapter-ink`, `spacing-offgrid.26`, `spacing.32`, `typography.chapter-title`.

![Chapter title default](components/crops/chapter-title-default.png)

#### Note heading
"Canvas Heading" (Satoshi Medium) 18/26 600; the note being read is blue #2e70ed. Read as `note-heading` on the science lesson page.

**Values (default).** size 416 x 26; background transparent; text Canvas Heading 18/26 600†, `text.note`.

**Tokens.** `text.note`.

![Note heading default](components/crops/note-heading-default.png)

#### Note body text
"Canvas Print" (Satoshi) 16/28 in a warm grey #45433f. Read as `note-text` on the science lesson page.

**Values (default).** size 416 x 84; background transparent; text `typography.note-body`, `palette.astryx.print-ink`.

**Tokens.** `palette.astryx.print-ink`, `typography.note-body`.

![Note body text default](components/crops/note-text-default.png)

#### Canvas ground
A #fcfcfc board with a dot grid, panned and zoomed by drag and Ctrl/Cmd + scroll. Read as `canvas-ground` on the science lesson page.

**Values (default).** size 1440 x 900; background `background.canvas`; text `typography.chapter-title`, `palette.astryx.chapter-ink`.

**Tokens.** `background.canvas`, `palette.astryx.chapter-ink`, `typography.chapter-title`.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Figure card
An animated diagram in a white radius-20 frame. Read as `figure-card` on the science lesson page.

**Values (default).** size 416 x 257.83; radius `radius.20`; background `background.card`.

**Tokens.** `background.card`, `radius.20`.

![Figure card default](components/crops/figure-card-default.png)

#### Takeaway callout
A #e8fbef radius-14 box with a bulb icon for the one-line takeaway. Read as `callout` on the science lesson page.

**Values (default).** size 416 x 88; padding `spacing-offgrid.14` `spacing-offgrid.10`; radius `radius.14`; background `component.callout.background`; text `typography.callout`, #202522†; icon 24 x 24, #202522†.

**Tokens.** `component.callout.background`, `radius.14`, `spacing-offgrid.10`, `spacing-offgrid.14`, `typography.callout`.

![Takeaway callout default](components/crops/callout-default.png)

#### Numbered list
Points with a small number in a pale blue disc and 16/24 text. Read as `numbered-list` on the science lesson page.

**Values (default).** size 416 x 240; background transparent; text Canvas Print 12/20 700†, `palette.blue.marker`.

Child layers that carry the look: span 20x20 background `palette.blue.marker-fill` radius 50%†; span 20x20 background `palette.blue.marker-fill` radius 50%†; span 20x20 background `palette.blue.marker-fill` radius 50%†.

**Tokens.** `palette.blue.marker`, `palette.blue.marker-fill`.

![Numbered list default](components/crops/numbered-list-default.png)

#### Quiz card
A check-in question docked over the canvas: white, 1px #e3e3e3 border, radius 20, a 0 6 24 shadow at 7%, an Inter 16/24 600 question, four outlined options and a small close button. No option was chosen. Read as `quiz-card` on the science lesson page.

**Values (default).** size 560 x 296; padding `spacing.20`; border `borderWidth.hairline` solid `component.quiz.border`; radius `radius.20`; background `background.card`; shadow `elevation.quiz`; text Inter 16/24 600†, #20242d†; icon 16 x 16, #737373†.

**Tokens.** `background.card`, `borderWidth.hairline`, `component.quiz.border`, `elevation.quiz`, `radius.20`, `spacing.20`.

![Quiz card default](components/crops/quiz-card-default.png)

#### Quiz option
A 44px option, 1px #e6e6e7 border, radius 10, SF Pro 14/20, over a visually hidden radio. Hover fills it #f3f3f3; keyboard focus draws Astryx's 2px #0064e0 ring 3px out. Read as `quiz-option` on the science lesson page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 518 x 44; padding 0px `spacing.12`; border `borderWidth.hairline` solid `component.quiz.option-border`; radius `radius.10`; background `action.secondary`; text SF Pro 14/20 400†, #2c323d†; transition box-shadow `duration.astryx` `easing.astryx`, border-color `duration.astryx` `easing.astryx` |
| hover | background `component.quiz.option-hover` |
| focus-visible | outline `focus.width` solid `border.focus`, offset `focus.offset-astryx` |

**Tokens.** `action.secondary`, `border.focus`, `borderWidth.hairline`, `component.quiz.option-border`, `component.quiz.option-hover`, `duration.astryx`, `easing.astryx`, `focus.offset-astryx`, `focus.width`, `radius.10`, `spacing.12`.

![Quiz option default](components/crops/quiz-option-default.png) ![Quiz option hover](components/crops/quiz-option-hover.png) ![Quiz option focus-visible](components/crops/quiz-option-focus-visible.png)

#### Playback speed menu
The Speed row swaps the Settings popover for a submenu: a back row on a #f3f3f3 fill, then one 44px row per speed, the current one marked with a check. Opened only; no speed was chosen. Read as `speed-menu` on the science lesson page.

**Values (opened).** size 298 x 290; radius `radius.24`; background transparent; text `typography.menu`, `palette.astryx.menu-ink`; icon 16 x 16, `palette.astryx.menu-ink`.

Child layers that carry the look: section 298x290 background `background.card` border `borderWidth.hairline` solid `palette.astryx.popover-line` radius `radius.24` shadow `elevation.level-3`; button 264x44 background `background.hover` radius `radius.12`; button 119x32 background `palette.astryx.menu-fill` radius `radius.pill`.

**Tokens.** `background.card`, `background.hover`, `borderWidth.hairline`, `elevation.level-3`, `palette.astryx.menu-fill`, `palette.astryx.menu-ink`, `palette.astryx.popover-line`, `radius.12`, `radius.24`, `radius.pill`, `typography.menu`.

![Playback speed menu opened](components/crops/speed-menu-opened.png)

#### Menu item, current
The current speed: the same row with a check at the right. Read as `menu-item-selected` on the science lesson page.

**Values (selected).** size 264 x 44; padding 0px `spacing.12` 0px `spacing.8`; radius `radius.12`; background transparent; text `typography.menu`, `palette.astryx.menu-ink`; icon 20 x 20, `palette.astryx.menu-ink`.

**Tokens.** `palette.astryx.menu-ink`, `radius.12`, `spacing.12`, `spacing.8`, `typography.menu`.

![Menu item, current selected](components/crops/menu-item-selected-selected.png)

#### Menu item
A 44px submenu row, radius 12; hovered and focused only, never chosen. Read as `menu-item` on the science lesson page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 264 x 44; padding 0px `spacing.12` 0px `spacing.8`; radius `radius.12`; background transparent; text `typography.menu`, `palette.astryx.menu-ink` |
| hover | background `background.hover` |
| focus-visible | background `background.hover`; outline `focus.width` solid `palette.blue.focus-2`, offset `focus.offset-inset` |

**Tokens.** `background.hover`, `focus.offset-inset`, `focus.width`, `palette.astryx.menu-ink`, `palette.blue.focus-2`, `radius.12`, `spacing.12`, `spacing.8`, `typography.menu`.

![Menu item default](components/crops/menu-item-default.png) ![Menu item hover](components/crops/menu-item-hover.png) ![Menu item focus-visible](components/crops/menu-item-focus-visible.png)

#### Tooltip
Hovering a header control shows Astryx's tooltip: a small dark label under the button. Read as `tooltip` on the science lesson page.

**Values (opened).** size 74.06 x 28; radius `radius.12`; background `component.section-rail.indicator`; text Figtree 14/20.00 400†, `text.inverse`.

**Tokens.** `component.section-rail.indicator`, `radius.12`, `text.inverse`.

![Tooltip opened](components/crops/tooltip-opened.png)

#### Quiz result card
After an option is picked the check-in leaves the dock and comes back as a card in the notes: a status line with an icon ("Quick check · Needs review" when wrong), the question, Your answer beside Correct answer, and why the answer missed. Wrong answers paint it in the lesson's wrong colours. Read as `quiz-result` on the science lesson page.

**Values (answered-wrong).** size 416 x 405; padding `spacing.16` `spacing-offgrid.18` `spacing-offgrid.18` `spacing.24`; border `borderWidth.hairline` solid `status.danger.border`; radius `radius.20`; background `status.danger.fill`; shadow 0px 8px 24px 0px rgba(0, 0, 0, 0.05)†; text `typography.overline`, `status.danger.text`; icon 20 x 20, `status.danger.text`.

**Tokens.** `borderWidth.hairline`, `radius.20`, `spacing-offgrid.18`, `spacing.16`, `spacing.24`, `status.danger.border`, `status.danger.fill`, `status.danger.text`, `typography.overline`.

![Quiz result card answered-wrong](components/crops/quiz-result-answered-wrong.png)

#### Quiz result status line
Read as `quiz-result-label` on the science lesson page.

**Values (answered-wrong).** size 187.11 x 18; background transparent; text `typography.overline`, `status.danger.text`.

**Tokens.** `status.danger.text`, `typography.overline`.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Quiz result card, right answer
The check-in answered correctly comes back as the same result card in the lesson's right-answer colours. Read as `quiz-result-correct` on the science lesson page.

**Values (answered-correct).** size 416 x 403.5; padding 19px† `spacing.20` 21px† `spacing-offgrid.26`; border `borderWidth.hairline` solid `status.success.border`; radius `radius.20`; background `status.success.fill`; shadow 0px 8px 24px 0px rgba(0, 0, 0, 0.06)†; text `typography.overline-lg`, `status.success.accent`; icon 20 x 20, `status.success.accent`.

**Tokens.** `borderWidth.hairline`, `radius.20`, `spacing-offgrid.26`, `spacing.20`, `status.success.accent`, `status.success.border`, `status.success.fill`, `typography.overline-lg`.

![Quiz result card, right answer answered-correct](components/crops/quiz-result-correct-answered-correct.png)

#### Quiz result status line, right answer
Read as `quiz-result-correct-label` on the science lesson page.

**Values (answered-correct).** size 168.64 x 20; background transparent; text `typography.overline-lg`, `status.success.accent`.

**Tokens.** `status.success.accent`, `typography.overline-lg`.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

### Lesson player: math

The math player puts a tutor column at the left and the slide in a white frame at the right, on the warm ground.

#### Math lesson page
Two columns on #faf9f5: a 360px tutor column at the left and the slide in a white radius-32 frame at the right, under a 66px header with the progress bar. Read as `math-lesson-page` on the math lesson page.

**Values (default).** size 1440 x 900; background `background.academy`; text `typography.nav`, `text.secondary`; icon 40 x 40, `text.primary`.

**Tokens.** `background.academy`, `text.primary`, `text.secondary`, `typography.nav`.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Tutor column
The mascot, a status line ("Explaining ...") with a shimmer, the running transcript and the "Ask gauth" field at the foot. Read as `tutor-panel` on the math lesson page.

**Values (default).** size 360 x 900; background `background.academy`; text `typography.nav`, `text.secondary`; icon 12.72 x 13.55, `text.secondary`.

**Tokens.** `background.academy`, `text.secondary`, `typography.nav`.

![Tutor column default](components/crops/tutor-panel-default.png)

#### Tutor status line
Read as `tutor-status` on the math lesson page.

**Values (default).** size 296 x 42; background transparent; text `typography.nav`, `text.secondary`; icon 12.72 x 13.55, `text.secondary`.

Child layers that carry the look: span 276x42 image linear-gradient(100deg, `palette.ink.shimmer-1` 0px, `palette.ink.shimmer-1` 38%, `palette.ink.shimmer-2`.

**Tokens.** `palette.ink.shimmer-1`, `palette.ink.shimmer-2`, `text.secondary`, `typography.nav`.

![Tutor status line default](components/crops/tutor-status-default.png)

#### Ask gauth field
White, 1px #e4e6eb border, radius 16, 48px, Inter 16, a microphone at the right; it grows with the text. Sample text was typed and deleted; nothing was sent. Read as `tutor-input` on the math lesson page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, focused) | size 296 x 48; padding `spacing-offgrid.9` `spacing.12`; border `borderWidth.hairline` solid `border.field`; radius `radius.16`; background `background.card`; icon 30 x 30, `text.primary` |
| filled | size 296 x 71; padding `spacing.12`; text Inter 16/22.4 400†, `text.primary`; icon 10.19 x 10.19, `palette.ink.black` |

**Tokens.** `background.card`, `border.field`, `borderWidth.hairline`, `palette.ink.black`, `radius.16`, `spacing-offgrid.9`, `spacing.12`, `text.primary`.

![Ask gauth field default](components/crops/tutor-input-default.png) ![Ask gauth field hover](components/crops/tutor-input-hover.png) ![Ask gauth field focused](components/crops/tutor-input-focused.png) ![Ask gauth field filled](components/crops/tutor-input-filled.png)

#### Lesson progress
Previous and next page arrows around an 8px track (#edeade fill, #27220c value) and one 20px dot per later chapter. Read as `progress-bar` on the math lesson page.

**Values (default).** size 718 x 40; background transparent; text -apple-system 16/normal 400†, `text.primary`; icon 40 x 40, `text.secondary`.

Child layers that carry the look: div 532x8 background `component.progress.track-lesson` radius `radius.100`; span 22.2x8 background `component.progress.value-lesson` radius `radius.100`; span 20x8 background `component.progress.track-lesson` radius `radius.100`.

**Tokens.** `component.progress.track-lesson`, `component.progress.value-lesson`, `radius.100`, `text.primary`, `text.secondary`.

![Lesson progress default](components/crops/progress-bar-default.png)

#### Page arrow button
Read as `page-nav` on the math lesson page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 40 x 40; radius 50%†; background transparent; text Arial 13.33/normal 400†, `text.secondary`; transition background `duration.fast` `easing.ease`, opacity `duration.fast` `easing.ease`, transform `duration.press` `easing.ease`; icon 40 x 40, `text.secondary` |
| hover | background `palette.lesson-math.film` |
| pressed | size 37.6 x 37.6; background `palette.lesson-math.film`; transform scale `scale.press-round`; icon 37.6 x 37.6, `text.secondary` |

**Tokens.** `duration.fast`, `duration.press`, `easing.ease`, `palette.lesson-math.film`, `scale.press-round`, `text.secondary`.

![Page arrow button default](components/crops/page-nav-default.png) ![Page arrow button hover](components/crops/page-nav-hover.png) ![Page arrow button focus-visible](components/crops/page-nav-focus-visible.png) ![Page arrow button pressed](components/crops/page-nav-pressed.png)

#### Header round button
Pause, speed ("1x") and chapters: 40px round ghost buttons. Read as `header-round-button` on the math lesson page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 40 x 40; radius 50%†; background transparent; text -apple-system 15/normal 600†, `text.primary`; transition background `duration.fast` `easing.ease`, transform `duration.press` `easing.ease`; icon 26.81 x 26.81, `text.primary` |
| hover | background `palette.lesson-math.film` |
| pressed | size 37.6 x 37.6; background `palette.lesson-math.film`; transform scale `scale.press-round`; icon 25.2 x 25.2, `text.primary` |

**Tokens.** `duration.fast`, `duration.press`, `easing.ease`, `palette.lesson-math.film`, `scale.press-round`, `text.primary`.

![Header round button default](components/crops/header-round-button-default.png) ![Header round button hover](components/crops/header-round-button-hover.png) ![Header round button focus-visible](components/crops/header-round-button-focus-visible.png) ![Header round button pressed](components/crops/header-round-button-pressed.png)

#### Speed button
Read as `speed-button` on the math lesson page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 40 x 40; radius 50%†; background transparent; text -apple-system 15/normal 600†, `text.primary`; transition background `duration.fast` `easing.ease`, transform `duration.press` `easing.ease` |
| hover | background `palette.lesson-math.film` |

**Tokens.** `duration.fast`, `duration.press`, `easing.ease`, `palette.lesson-math.film`, `text.primary`.

![Speed button default](components/crops/speed-button-default.png) ![Speed button hover](components/crops/speed-button-hover.png)

#### Slide frame
The white radius-32 frame the slide plays in, title in Playfair Display. Read as `player-frame` on the math lesson page.

**Values (default).** size 1048 x 820; border `borderWidth.hairline` solid transparent; radius `radius.32`; background `background.card`; transition border-color `duration.atlas` `easing.ease`.

**Tokens.** `background.card`, `borderWidth.hairline`, `duration.atlas`, `easing.ease`, `radius.32`.

![Slide frame default](components/crops/player-frame-default.png)

#### Chapters panel
Opened from the list button at the top right: a white panel of chapter rows, the current one tinted. Read as `chapters-panel` on the math lesson page.

**Values (opened).** size 320 x 460; padding `spacing.12` `spacing.8`; radius `radius.16`; background `background.card`; shadow `elevation.panel`; text -apple-system 16/normal 700†, `text.primary`.

**Tokens.** `background.card`, `elevation.panel`, `radius.16`, `spacing.12`, `spacing.8`, `text.primary`.

![Chapters panel opened](components/crops/chapters-panel-opened.png)

#### Chapter row, current
Read as `chapter-option-active` on the math lesson page.

**Values (default).** size 304 x 37; padding `spacing.8` `spacing.12`; radius `radius.10`; background `background.selected`; text -apple-system 14/normal 600†, `text.primary`.

**Tokens.** `background.selected`, `radius.10`, `spacing.12`, `spacing.8`, `text.primary`.

![Chapter row, current default](components/crops/chapter-option-active-default.png)

#### Chapter row
A 37px row. Hovered and focused only. Read as `chapter-option` on the math lesson page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 304 x 37; padding `spacing.8` `spacing.12`; radius `radius.10`; background transparent; text -apple-system 14/normal 400†, `text.primary` |
| hover, focus-visible | background `background.selected` |

**Tokens.** `background.selected`, `radius.10`, `spacing.12`, `spacing.8`, `text.primary`.

![Chapter row default](components/crops/chapter-option-default.png) ![Chapter row hover](components/crops/chapter-option-hover.png) ![Chapter row focus-visible](components/crops/chapter-option-focus-visible.png)

#### Tutor transcript
The column under the mascot. While the tutor narrates it holds the status line with a shimmer; no transcript text appeared in 25 seconds of playback. Read as `tutor-transcript` on the math lesson page.

**Values (default).** size 296 x 748; padding 73px† 0px `spacing.20` 0px; background transparent; text `typography.nav`, `text.secondary`; icon 12.72 x 13.55, `text.secondary`.

Child layers that carry the look: span 230.7x21 image linear-gradient(100deg, `palette.ink.shimmer-1` 0px, `palette.ink.shimmer-1` 38%, `palette.ink.shimmer-2`.

**Tokens.** `palette.ink.shimmer-1`, `palette.ink.shimmer-2`, `spacing.20`, `text.secondary`, `typography.nav`.

![Tutor transcript default](components/crops/tutor-transcript-default.png)

### Lesson player: history

The history player is immersive: chapter pills at the top, the scene in the middle, a play disc and a caption line.

#### History lesson page
An immersive player on #faf9f5: chapter pills centred in the header, the scene in the middle, a round play button and a caption line at the foot. Read as `history-lesson-page` on the history lesson page.

**Values (default).** size 1440 x 900; background `background.academy`; text `typography.label`, `text.primary`; icon 40 x 40, `text.primary`.

**Tokens.** `background.academy`, `text.primary`, `typography.label`.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Chapter pills
The current chapter as a grey pill with an icon and its name; later chapters as numbered pills joined by dashed lines; a chapters list button at the end. Read as `chapter-pills` on the history lesson page.

**Values (default).** size 382.92 x 44; padding 0px `spacing-offgrid.6`; radius 22px†; background transparent; image linear-gradient(#f7f9fa†, `background.canvas`); text `typography.label`, `text.primary`; icon 14 x 14, `text.primary`.

**Tokens.** `background.canvas`, `spacing-offgrid.6`, `text.primary`, `typography.label`.

![Chapter pills default](components/crops/chapter-pills-default.png)

#### Chapter pill, current
Read as `chapter-pill-active` on the history lesson page.

**Values (default).** size 122.19 x 32; padding `spacing.8` `spacing-offgrid.14`; radius `radius.999`; background `palette.ink.a07`; text `typography.label`, `text.primary`; transition background-color `duration.press` `easing.ease`, color `duration.press` `easing.ease`; icon 14 x 14, `text.primary`.

**Tokens.** `duration.press`, `easing.ease`, `palette.ink.a07`, `radius.999`, `spacing-offgrid.14`, `spacing.8`, `text.primary`, `typography.label`.

![Chapter pill, current default](components/crops/chapter-pill-active-default.png)

#### Chapter pill, upcoming
An upcoming chapter: a 32px pill at 4% ink with its number at 25% ink; hover doubles both. Read as `chapter-pill` on the history lesson page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 50.56 x 32; padding 0px `spacing.12`; radius `radius.999`; background `palette.ink.a04`; text SF Pro 16/22.4 500†, `palette.ink.a25`; transition background-color `duration.press` `easing.ease`, color `duration.press` `easing.ease`; icon 14 x 14, `palette.ink.a25` |
| hover | background rgba(33, 37, 46, 0.08)†; text SF Pro 16/22.4 500†, rgba(33, 37, 46, 0.48)†; icon 14 x 14, rgba(33, 37, 46, 0.48)† |

**Tokens.** `duration.press`, `easing.ease`, `palette.ink.a04`, `palette.ink.a25`, `radius.999`, `spacing.12`.

![Chapter pill, upcoming default](components/crops/chapter-pill-default.png) ![Chapter pill, upcoming hover](components/crops/chapter-pill-hover.png) ![Chapter pill, upcoming focus-visible](components/crops/chapter-pill-focus-visible.png)

#### Play button
A 60px disc, white at 82%, with a 0 8 28 navy shadow and a black play glyph. Not pressed. Read as `play-button` on the history lesson page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, focus-visible) | size 60 x 60; radius 50%†; background `palette.paper.glass`; shadow `elevation.play`; text SF Pro 16/normal 400†, #161823†; transition transform `duration.press` `easing.ease`; icon 26 x 26, #161823† |

**Tokens.** `duration.press`, `easing.ease`, `elevation.play`, `palette.paper.glass`.

![Play button default](components/crops/play-button-default.png) ![Play button hover](components/crops/play-button-hover.png) ![Play button focus-visible](components/crops/play-button-focus-visible.png)

#### Chapter panel
A 400px white panel from the right edge, radius 28 on the leading corners, a -8 0 40 shadow: each chapter with a number, a 600 name and a two-line description; the current chapter is pink #fff0f3 with red text. Read as `chapter-panel` on the history lesson page.

**Values (opened).** size 400 x 900; padding `spacing.8` `spacing.16`; radius `radius.28` 0px 0px `radius.28`; background `background.card`; shadow `elevation.side-panel`; text SF Pro 16/22.4 700†, `text.primary`; transition opacity `duration.atlas` `easing.ease`, transform `duration.atlas` `easing.ease`; icon 24 x 24, `text.primary`.

**Tokens.** `background.card`, `duration.atlas`, `easing.ease`, `elevation.side-panel`, `radius.28`, `spacing.16`, `spacing.8`, `text.primary`.

![Chapter panel opened](components/crops/chapter-panel-opened.png)

#### Chapter panel row
Read as `chapter-panel-item` on the history lesson page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 368 x 94; padding `spacing.16` `spacing.4`; radius `radius.16`; background transparent; text SF Pro 16/normal 700†, `text.primary` |
| hover, focus-visible | background `palette.ink.a04` |

**Tokens.** `palette.ink.a04`, `radius.16`, `spacing.16`, `spacing.4`, `text.primary`.

![Chapter panel row default](components/crops/chapter-panel-item-default.png) ![Chapter panel row hover](components/crops/chapter-panel-item-hover.png) ![Chapter panel row focus-visible](components/crops/chapter-panel-item-focus-visible.png)

#### Caption line
The narration as one centred grey line under the scene. Read as `caption` on the history lesson page.

**Values (default).** size 284.52 x 22.41; background transparent; text SF Pro 20/22.4 400†, `text.meta`.

**Tokens.** `text.meta`.

![Caption line default](components/crops/caption-default.png)

### Atlas

Atlas has its own shell (a 56px header and a 230px drawer), a prompt box, recommendation chips and a grid of story cards. A story opens as a video preview, then a story page.

#### Atlas top bar
Atlas has its own 56px shell: logo and a menu button at the left, Sign in at the right. Read as `atlas-header` on the Atlas page.

**Values (default).** size 1440 x 56; padding 0px `spacing.20`; background `background.card`; text -apple-system 14/normal 600†, `text.inverse`; icon 24 x 24, `palette.indigo.heading`.

**Tokens.** `background.card`, `palette.indigo.heading`, `spacing.20`, `text.inverse`.

![Atlas top bar default](components/crops/atlas-header-default.png)

#### Atlas sidebar
A 230px white drawer: New Topic, a search field and the topic list (empty when signed out). Read as `atlas-drawer` on the Atlas page.

**Values (default).** size 230 x 844; padding 0px `spacing.12` `spacing.20` `spacing.12`; background `background.card`; text Rubik 12/normal 400†, `palette.atlas.drawer-ink`; icon 20 x 20, `palette.atlas.drawer-ink`.

**Tokens.** `background.card`, `palette.atlas.drawer-ink`, `spacing.12`, `spacing.20`.

![Atlas sidebar default](components/crops/atlas-drawer-default.png)

#### New Topic button
A 44px row, radius 12, plus icon and Rubik 12px label. Read as `new-topic` on the Atlas page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 206 x 44; padding 0px `spacing-offgrid.10`; radius `radius.12`; background transparent; text Rubik 12/normal 400†, `palette.atlas.drawer-ink`; icon 20 x 20, `palette.atlas.drawer-ink` |
| hover, pressed | background `palette.paper.hover-2` |

**Tokens.** `palette.atlas.drawer-ink`, `palette.paper.hover-2`, `radius.12`, `spacing-offgrid.10`.

![New Topic button default](components/crops/new-topic-default.png) ![New Topic button hover](components/crops/new-topic-hover.png) ![New Topic button focus-visible](components/crops/new-topic-focus-visible.png) ![New Topic button pressed](components/crops/new-topic-pressed.png)

#### Topic search field
Read as `atlas-search` on the Atlas page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 206 x 44; padding 0px `spacing-offgrid.10` 0px `spacing.40`; radius `radius.12`; background transparent; icon 20 x 20, `palette.ink.black` |
| hover, focused, filled | background `palette.paper.hover-2` |

**Tokens.** `palette.ink.black`, `palette.paper.hover-2`, `radius.12`, `spacing-offgrid.10`, `spacing.40`.

![Topic search field default](components/crops/atlas-search-default.png) ![Topic search field hover](components/crops/atlas-search-hover.png) ![Topic search field focused](components/crops/atlas-search-focused.png) ![Topic search field filled](components/crops/atlas-search-filled.png)

#### Atlas title
"Turn any topic into a visual story" in Libre Baskerville 40/48 700, the first letter filled with a red gradient. Read as `atlas-title` on the Atlas page.

**Values (default).** size 682.92 x 48; background `action.primary`; image an image (data URI); text Libre Baskerville 40/48 700, letter spacing -0.4px†, `palette.ink.black`.

**Tokens.** `action.primary`, `palette.ink.black`.

![Atlas title default](components/crops/atlas-title-default.png)

#### Atlas prompt box
A 920 x 148 white box, 1px #e4e6eb border, radius 20, a peach glow (0 6 20 rgba(255,215,199,.4)) that deepens on focus, a Search toggle pill and a round send button. Sample text was typed and deleted; nothing was sent. Read as `atlas-composer` on the Atlas page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 920 x 148; padding `spacing.12` `spacing.12` `spacing-offgrid.10` `spacing.12`; border `borderWidth.hairline` solid `border.field`; radius `radius.20`; background `background.card`; shadow `elevation.composer`; text SF Pro 15/22 400†, `text.tertiary`; transition border-color `duration.composer` `easing.ease`, box-shadow `duration.composer` `easing.ease`, background `duration.composer` `easing.ease`; icon 13 x 13, `text.inverse` |
| focused | border `borderWidth.hairline` solid `palette.atlas.line-focus`; shadow `elevation.composer-focus` |
| filled | border `borderWidth.hairline` solid `palette.atlas.line-focus`; shadow `elevation.composer-focus`; text `typography.composer`, `text.primary` |

**Tokens.** `background.card`, `border.field`, `borderWidth.hairline`, `duration.composer`, `easing.ease`, `elevation.composer`, `elevation.composer-focus`, `palette.atlas.line-focus`, `radius.20`, `spacing-offgrid.10`, `spacing.12`, `text.inverse`, `text.primary`, `text.tertiary`, `typography.composer`.

![Atlas prompt box default](components/crops/atlas-composer-default.png) ![Atlas prompt box hover](components/crops/atlas-composer-hover.png) ![Atlas prompt box focused](components/crops/atlas-composer-focused.png) ![Atlas prompt box filled](components/crops/atlas-composer-filled.png)

#### Search toggle pill
The web-search switch, on: a near-black #171410 pill, radius 20, with a 0 5 12 shadow; hover lightens it to #2a2d34. Not toggled. Read as `search-toggle` on the Atlas page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 85.17 x 30; padding 0px `spacing.12`; border `borderWidth.hairline` solid `component.atlas.toggle`; radius `radius.20`; background `component.atlas.toggle`; shadow `elevation.toggle`; text -apple-system 12/12 600†, `text.inverse`; transition background 0.15s† `easing.ease`, border-color 0.15s† `easing.ease`, color 0.15s† `easing.ease`, box-shadow 0.15s† `easing.ease`, transform `duration.press` `easing.ease`; icon 13 x 13, `text.inverse` |
| hover | border `borderWidth.hairline` solid `palette.atlas.toggle-hover`; background `palette.atlas.toggle-hover`; shadow 0px 6px 14px 0px rgba(17, 20, 16, 0.18)† |
| focus-visible | outline `focus.width` solid rgba(23, 20, 16, 0.18)†, offset `focus.offset` |

**Tokens.** `borderWidth.hairline`, `component.atlas.toggle`, `duration.press`, `easing.ease`, `elevation.toggle`, `focus.offset`, `focus.width`, `palette.atlas.toggle-hover`, `radius.20`, `spacing.12`, `text.inverse`.

![Search toggle pill default](components/crops/search-toggle-default.png) ![Search toggle pill hover](components/crops/search-toggle-hover.png) ![Search toggle pill focus-visible](components/crops/search-toggle-focus-visible.png)

#### Send button
Grey #eef0f3 disc while the box is empty, when it carries the disabled attribute; typing into the box enables it. Never pressed. Read as `send-button` on the Atlas page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, disabled) | size 36 x 36; radius 50%†; background `component.atlas.send`; text Arial 13.33/normal 400†, `text.tertiary`; transition background `duration.atlas` `easing.ease`, color `duration.atlas` `easing.ease`, transform `duration.atlas` `easing.ease`; icon 18 x 18, `text.tertiary` |
| enabled | background `component.atlas.toggle`; text Arial 13.33/normal 400†, `text.inverse`; icon 18 x 18, `text.inverse` |

**Tokens.** `component.atlas.send`, `component.atlas.toggle`, `duration.atlas`, `easing.ease`, `text.inverse`, `text.tertiary`.

![Send button default](components/crops/send-button-default.png) ![Send button hover](components/crops/send-button-hover.png) ![Send button disabled](components/crops/send-button-disabled.png) ![Send button enabled](components/crops/send-button-enabled.png)

#### Recommendation chip
A white chip, 1px #dcdcdc border, radius 10, SF Pro 13/19.5 black; hover lifts it 1px onto #f5f5f7 with a soft shadow. Pressing one would start a story, so it was only hovered, focused and forced. Read as `recommendation-chip` on the Atlas page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 170.5 x 41.5; padding `spacing-offgrid.10` `spacing.16`; border `borderWidth.hairline` solid `component.atlas.chip-border`; radius `radius.10`; background `action.secondary`; text `typography.chip`, `palette.ink.black`; transition box-shadow `duration.atlas` `easing.ease`, transform `duration.atlas` `easing.ease`, border-color `duration.atlas` `easing.ease` |
| hover, pressed | border `borderWidth.hairline` solid `palette.atlas.chip-line-hover`; background `background.selected`; shadow 0px 4px 14px 0px rgba(0, 0, 0, 0.04)†; transform translate(0px, -1px) |

**Tokens.** `action.secondary`, `background.selected`, `borderWidth.hairline`, `component.atlas.chip-border`, `duration.atlas`, `easing.ease`, `palette.atlas.chip-line-hover`, `palette.ink.black`, `radius.10`, `spacing-offgrid.10`, `spacing.16`, `typography.chip`.

![Recommendation chip default](components/crops/recommendation-chip-default.png) ![Recommendation chip hover](components/crops/recommendation-chip-hover.png) ![Recommendation chip focus-visible](components/crops/recommendation-chip-focus-visible.png) ![Recommendation chip pressed](components/crops/recommendation-chip-pressed.png)

#### Popular Stories heading
Read as `stories-title` on the Atlas page.

**Values (default).** size 1080 x 24; background transparent; text `typography.stories-title`, `palette.ink.black`.

**Tokens.** `palette.ink.black`, `typography.stories-title`.

![Popular Stories heading default](components/crops/stories-title-default.png)

#### Story card
A 339px white card, 1px rgba(0,0,0,.08) border, radius 16, a 0 6 18 shadow at 4%: a radius-12 thumbnail (video or image) and a 16/24 600 title. Hover lifts it 4px with a 0 18 42 shadow at 10%. Read as `story-card` on the Atlas page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 338.66 x 313.5; padding `spacing-offgrid.14` `spacing-offgrid.14` `spacing-offgrid.18` `spacing-offgrid.14`; border `borderWidth.hairline` solid `border.card`; radius `radius.16`; background `background.card`; shadow `elevation.story-card`; text `typography.atlas-card-title`, `text.inverse`; transition transform `duration.story-card` `easing.ease`, box-shadow `duration.story-card` `easing.ease`, border-color `duration.story-card` `easing.ease` |
| hover, pressed | border `borderWidth.hairline` solid rgba(0, 0, 0, 0.12)†; shadow `elevation.story-card-hover`; transform translate(0px, -4px) |

**Tokens.** `background.card`, `border.card`, `borderWidth.hairline`, `duration.story-card`, `easing.ease`, `elevation.story-card`, `elevation.story-card-hover`, `radius.16`, `spacing-offgrid.14`, `spacing-offgrid.18`, `text.inverse`, `typography.atlas-card-title`.

![Story card default](components/crops/story-card-default.png) ![Story card hover](components/crops/story-card-hover.png) ![Story card focus-visible](components/crops/story-card-focus-visible.png) ![Story card pressed](components/crops/story-card-pressed.png)

#### Video badge
A dark translucent radius-8 label over the thumbnail. Read as `video-badge` on the Atlas page.

Not on the page when it was captured.

#### New badge
A red #ff013e radius-8 label. Read as `new-badge` on the Atlas page.

**Values (default).** size 40.8 x 20; radius `radius.8`; background `action.accent`; text `typography.atlas-card-title`, `text.inverse`; transform scale(0.8†).

**Tokens.** `action.accent`, `radius.8`, `text.inverse`, `typography.atlas-card-title`.

![New badge default](components/crops/new-badge-default.png)

#### Play disc
A 48px white-alpha disc over a video thumbnail. Read as `play-icon` on the Atlas page.

Not on the page when it was captured.

#### Story canvas
The story image in a radius-20 frame, hotspot rings over places in it, a "Content generated by AI" note under it. Read as `story-stage` on the Atlas story page.

**Values (default).** size 1034 x 581.63; background transparent; text Libre Baskerville 12/normal 400†, rgba(156, 162, 172, 0.5)†; icon 18 x 18, `palette.ink.black`.

Child layers that carry the look: span 18x18 background `palette.atlas.hotspot` border `borderWidth.strong` solid rgba(255, 255, 255, 0.94)† radius `radius.999` shadow 0px 0px 0px 5px rgba(122, 92, 255, 0.16), 0px 8px 18px 0px rgba(80, 41, 255, 0.2)†; span 18x18 background `palette.atlas.hotspot` border `borderWidth.strong` solid rgba(255, 255, 255, 0.94)† radius `radius.999` shadow 0px 0px 0px 5px rgba(122, 92, 255, 0.16), 0px 8px 18px 0px rgba(80, 41, 255, 0.2)†; span 18x18 background `palette.atlas.hotspot` border `borderWidth.strong` solid rgba(255, 255, 255, 0.94)† radius `radius.999` shadow 0px 0px 0px 5px rgba(122, 92, 255, 0.16), 0px 8px 18px 0px rgba(80, 41, 255, 0.2)†.

**Tokens.** `borderWidth.strong`, `palette.atlas.hotspot`, `palette.ink.black`, `radius.999`.

![Story canvas default](components/crops/story-stage-default.png)

#### Share button
The dark #21252e radius-8 button, Rubik 12/20 600. It shows no hover, focus or pressed change. Measured, never pressed. Read as `share-button` on the Atlas story page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, focus-visible, pressed) | size 70 x 30; padding 0px `spacing-offgrid.6`; border `borderWidth.hairline` solid `action.primary`; radius `radius.8`; background `action.primary`; text `typography.atlas-label`, `text.inverse` |

**Tokens.** `action.primary`, `borderWidth.hairline`, `radius.8`, `spacing-offgrid.6`, `text.inverse`, `typography.atlas-label`.

![Share button default](components/crops/share-button-default.png) ![Share button hover](components/crops/share-button-hover.png) ![Share button focus-visible](components/crops/share-button-focus-visible.png) ![Share button pressed](components/crops/share-button-pressed.png)

#### Generate Video button
A white button, 1px #dfe3ea border, radius 8, Rubik 12/20 600, a red guide dot; hover greys it to #f9fafb. Never pressed. Read as `generate-video-button` on the Atlas story page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 141.83 x 34; padding 0px `spacing-offgrid.14`; border `borderWidth.hairline` solid `palette.atlas.button-line`; radius `radius.8`; background `action.secondary`; shadow 0px 1px 2px 0px rgba(16, 24, 40, 0.02)†; text `typography.atlas-label`, `palette.atlas.button-ink`; transition border-color `duration.atlas` `easing.ease`, background-color `duration.atlas` `easing.ease`, color `duration.atlas` `easing.ease`, box-shadow `duration.atlas` `easing.ease`; icon 16 x 16, `palette.atlas.button-ink` |
| hover | border `borderWidth.hairline` solid #cbd5e1†; background #f9fafb†; text `typography.atlas-label`, `palette.atlas.ink-strong`; icon 16 x 16, `palette.atlas.ink-strong` |

**Tokens.** `action.secondary`, `borderWidth.hairline`, `duration.atlas`, `easing.ease`, `palette.atlas.button-ink`, `palette.atlas.button-line`, `palette.atlas.ink-strong`, `radius.8`, `spacing-offgrid.14`, `typography.atlas-label`.

![Generate Video button default](components/crops/generate-video-button-default.png) ![Generate Video button hover](components/crops/generate-video-button-hover.png) ![Generate Video button focus-visible](components/crops/generate-video-button-focus-visible.png)

#### Video Settings popover
Source image tiles, a language select and a dark Generate Video button with an estimate line, in a white radius-16 popover with a 0 10 40 shadow that springs in (cubic-bezier(0.34, 1.56, 0.64, 1)). Nothing in it was pressed. Read as `video-settings` on the Atlas story page.

**Values (opened).** size 314.88 x 365.04; border `borderWidth.hairline` solid `palette.paper.line-light`; radius `radius.16`; background `background.card`; shadow 0px 10px 40px 0px rgba(0, 0, 0, 0.12)†; text Rubik 12/18 700†, `palette.atlas.ink-strong`; transition opacity `duration.story-card` `easing.ease`, transform `duration.popover` `easing.spring`; transform matrix(0.96, 0, 0, 0.96, 0, -8); opacity 0; icon 19.2 x 19.2, `palette.ink.black`.

**Tokens.** `background.card`, `borderWidth.hairline`, `duration.popover`, `duration.story-card`, `easing.ease`, `easing.spring`, `palette.atlas.ink-strong`, `palette.ink.black`, `palette.paper.line-light`, `radius.16`.

![Video Settings popover opened](components/crops/video-settings-opened.png)

#### View and Details rail
A floating white radius-16 rail at the right edge of the canvas, 1px #eeeeee border, with View (current, a 3px black bar) and Details. Read as `view-rail` on the Atlas story page.

**Values (default).** size 70 x 132; padding `spacing-offgrid.6`; border `borderWidth.hairline` solid `palette.paper.line-light`; radius `radius.16`; background `background.card`; shadow 0px 4px 20px 0px rgba(0, 0, 0, 0.06)†; text `typography.atlas-rail`, `palette.ink.black`; transform translate(0px, -66px); icon 18 x 18, `palette.ink.black`.

**Tokens.** `background.card`, `borderWidth.hairline`, `palette.ink.black`, `palette.paper.line-light`, `radius.16`, `spacing-offgrid.6`, `typography.atlas-rail`.

![View and Details rail default](components/crops/view-rail-default.png)

#### Rail item
Read as `rail-item` on the Atlas story page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 56 x 56; radius `radius.12`; background transparent; text `typography.atlas-rail`, `palette.atlas.rail-ink`; transition background-color `duration.atlas` `easing.ease`, color `duration.atlas` `easing.ease`; icon 18 x 18, `palette.atlas.rail-ink` |
| hover | text `typography.atlas-rail`, `palette.atlas.rail-ink-hover`; icon 18 x 18, `palette.atlas.rail-ink-hover` |

**Tokens.** `duration.atlas`, `easing.ease`, `palette.atlas.rail-ink`, `palette.atlas.rail-ink-hover`, `radius.12`, `typography.atlas-rail`.

![Rail item default](components/crops/rail-item-default.png) ![Rail item hover](components/crops/rail-item-hover.png) ![Rail item focus-visible](components/crops/rail-item-focus-visible.png)

#### Story strip item
The current story under the canvas: thumbnail and a 600 title on a #f5f6f9 radius-12 tile. Read as `story-strip-item` on the Atlas story page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 289 x 62; padding `spacing.8`; radius 11px†; background `palette.atlas.strip`; text Rubik 12/15.6 510, letter spacing -0.12px†, `palette.ink.story` |

**Tokens.** `palette.atlas.strip`, `palette.ink.story`, `spacing.8`.

![Story strip item default](components/crops/story-strip-item-default.png) ![Story strip item hover](components/crops/story-strip-item-hover.png)

#### Text area (Atlas prompt)
The multi-line field inside the prompt box: an Ant Design textarea with no border of its own; the box around it draws the frame. Sample text was typed and deleted. Read as `atlas-textarea` on the Atlas page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible, filled) | size 894 x 78; padding `spacing.4` 58px† `spacing.4` `spacing.8`; radius `radius.6`; background transparent; text `typography.composer`, `text.primary`; transition all `duration.popover` `easing.ease`; placeholder `text.primary` |

**Tokens.** `duration.popover`, `easing.ease`, `radius.6`, `spacing.4`, `spacing.8`, `text.primary`, `typography.composer`.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

### Insights

The news and blog list in the app shell, and the blog's pagination.

#### Breadcrumb
Read as `breadcrumb` on the Insights page.

**Values (default).** size 720 x 82; padding 35px† 0px `spacing-offgrid.29` 0px; background transparent; text `typography.chip-label`, `text.tertiary`; icon 12 x 13, `text.tertiary`.

**Tokens.** `spacing-offgrid.29`, `text.tertiary`, `typography.chip-label`.

![Breadcrumb default](components/crops/breadcrumb-default.png)

#### Pill tab, current
News: pink #fff0f3 fill, 1px #ffe5ec border, red #f00039 label, radius 100. Keyboard focus draws a 2px red ring 2px out. Read as `pill-tab-active` on the Insights page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 70.52 x 37; padding 0px `spacing.16`; border `borderWidth.hairline` solid `component.news-tab.current-border`; radius `radius.100`; background `component.news-tab.current`; text `typography.label-system`, `text.brand` |
| focus-visible | outline `focus.width` solid `palette.brand.focus`, offset `focus.offset` |

**Tokens.** `borderWidth.hairline`, `component.news-tab.current`, `component.news-tab.current-border`, `focus.offset`, `focus.width`, `palette.brand.focus`, `radius.100`, `spacing.16`, `text.brand`, `typography.label-system`.

![Pill tab, current default](components/crops/pill-tab-active-default.png) ![Pill tab, current focus-visible](components/crops/pill-tab-active-focus-visible.png)

#### Pill tab
White, 1px #e4e6eb border, radius 100, 14/21 500; pressed fills it #f5f5f7. Read as `pill-tab` on the Insights page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 63.63 x 37; padding 0px `spacing.16`; border `borderWidth.hairline` solid `border.field`; radius `radius.100`; background `action.secondary`; text `typography.label-system`, `text.primary` |
| focus-visible | outline `focus.width` solid `palette.brand.focus`, offset `focus.offset` |
| pressed | background `background.selected`; opacity 0.8 |

**Tokens.** `action.secondary`, `background.selected`, `border.field`, `borderWidth.hairline`, `focus.offset`, `focus.width`, `palette.brand.focus`, `radius.100`, `spacing.16`, `text.primary`, `typography.label-system`.

![Pill tab default](components/crops/pill-tab-default.png) ![Pill tab hover](components/crops/pill-tab-hover.png) ![Pill tab focus-visible](components/crops/pill-tab-focus-visible.png) ![Pill tab pressed](components/crops/pill-tab-pressed.png)

#### Featured article
A 26/36 700 title and a 16/24 description beside a 333 x 200 radius-12 image. Read as `featured-article` on the Insights page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 720 x 200; background transparent; text `typography.featured-title`, `text.primary` |
| focus-visible | radius `radius.12`; outline `focus.width` solid `action.accent-hover`, offset 4px† |

Child layers that carry the look: span::after 333pxx200px background `palette.lesson-math.film`.

**Tokens.** `action.accent-hover`, `focus.width`, `palette.lesson-math.film`, `radius.12`, `text.primary`, `typography.featured-title`.

![Featured article default](components/crops/featured-article-default.png) ![Featured article hover](components/crops/featured-article-hover.png) ![Featured article focus-visible](components/crops/featured-article-focus-visible.png)

#### Article row
A 171 x 96 radius-8 image beside an 18px title and a two-line grey summary, rows split by a 1px rule. Read as `article-row` on the Insights page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 720 x 128; background transparent; text `typography.article-title`, `text.primary` |

Child layers that carry the look: li::after 720pxx1px background `background.selected`; span::after 170.656pxx96px background `palette.lesson-math.film`.

**Tokens.** `background.selected`, `palette.lesson-math.film`, `text.primary`, `typography.article-title`.

![Article row default](components/crops/article-row-default.png) ![Article row hover](components/crops/article-row-hover.png)

#### Pagination
Ant Design pagination under the blog list: 32px square page items at radius 6. Read as `pagination` on the Blog page.

**Values (default).** size 752 x 36; background transparent; text `typography.pagination`, `text.inverse`; icon 16 x 17, `palette.antd.disabled`.

Child layers that carry the look: li 36x36 background `background.selected` border `borderWidth.hairline` solid `border.field` radius `radius.18`; button 34x34 border `borderWidth.hairline` solid transparent radius `radius.16`; li 36x36 background `action.primary` border `borderWidth.hairline` solid `action.primary` radius `radius.18`.

**Tokens.** `action.primary`, `background.selected`, `border.field`, `borderWidth.hairline`, `palette.antd.disabled`, `radius.16`, `radius.18`, `text.inverse`, `typography.pagination`.

![Pagination default](components/crops/pagination-default.png)

#### Pagination arrow, disabled
Previous on the first page. Read as `pagination-prev` on the Blog page.

**Values (disabled).** size 36 x 36; border `borderWidth.hairline` solid `border.field`; radius `radius.18`; background `background.selected`; transition all `duration.composer` `easing.ease`; icon 16 x 17, `palette.antd.disabled`.

**Tokens.** `background.selected`, `border.field`, `borderWidth.hairline`, `duration.composer`, `easing.ease`, `palette.antd.disabled`, `radius.18`.

![Pagination arrow, disabled disabled](components/crops/pagination-prev-disabled.png)

#### Pagination item, current
Read as `pagination-item-active` on the Blog page.

**Values (selected).** size 36 x 36; border `borderWidth.hairline` solid `action.primary`; radius `radius.18`; background `action.primary`; text `typography.pagination`, `text.inverse`.

**Tokens.** `action.primary`, `borderWidth.hairline`, `radius.18`, `text.inverse`, `typography.pagination`.

![Pagination item, current selected](components/crops/pagination-item-active-selected.png)

#### Pagination item
Hovered and focused, never followed. Read as `pagination-item` on the Blog page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 36 x 36; border `borderWidth.hairline` solid `border.field`; radius `radius.18`; background `action.secondary`; text -apple-system 14/32 400†, `palette.antd.text` |
| hover | background rgba(0, 0, 0, 0.06)†; transition all `duration.composer` `easing.ease` |
| focus-visible | outline on a: 3px solid #91caff† offset 1px |

**Tokens.** `action.secondary`, `border.field`, `borderWidth.hairline`, `duration.composer`, `easing.ease`, `palette.antd.text`, `radius.18`.

![Pagination item default](components/crops/pagination-item-default.png) ![Pagination item hover](components/crops/pagination-item-hover.png) ![Pagination item focus-visible](components/crops/pagination-item-focus-visible.png)

### Plans page

`/plus`, the plans page the top bar's Upgrade opens: two plan cards and a real `<table>` comparing them. Read only; no button on it was pressed.

#### Table (features by plan)
A real <table> in a white card, 1px border, radius 24: a header row with the two plans and their buttons, then label, Free and PLUS cells, the PLUS column tinted cream. Read as `plan-table` on the Gauth PLUS plans page.

**Values (default).** size 1000 x 485; border `borderWidth.strong` solid `palette.paper.table-line`; radius `radius.32`; background transparent; text `typography.table-heading`, `palette.ink.800`; icon 118 x 28, `text.primary`.

**Tokens.** `borderWidth.strong`, `palette.ink.800`, `palette.paper.table-line`, `radius.32`, `text.primary`, `typography.table-heading`.

![Table (features by plan) default](components/crops/plan-table-default.png)

#### Table header cell
Read as `plan-table-header` on the Gauth PLUS plans page.

**Values (default).** size 378.5 x 154; padding 0px 0px 0px `spacing.40`; border B: `borderWidth.strong` solid `palette.paper.table-line`; background transparent; text `typography.table-heading`, `palette.ink.800`.

Child layers that carry the look: td 378.5x154 border `borderWidth.strong` solid `palette.paper.table-line`.

**Tokens.** `borderWidth.strong`, `palette.ink.800`, `palette.paper.table-line`, `spacing.40`, `typography.table-heading`.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Table row
Read as `plan-table-row` on the Gauth PLUS plans page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 996 x 52; background transparent; text `typography.label-system`, `text.tab`; icon 21 x 21, `text.tab` |

Child layers that carry the look: td 378.5x52 background `action.secondary`; td 308.8x52 background `action.secondary` border `borderWidth.strong` solid `palette.paper.table-line`; td 308.8x52 background #fef9ee† border `borderWidth.strong` solid `palette.paper.table-line`.

**Tokens.** `action.secondary`, `borderWidth.strong`, `palette.paper.table-line`, `text.tab`, `typography.label-system`.

![Table row default](components/crops/plan-table-row-default.png) ![Table row hover](components/crops/plan-table-row-hover.png)

#### Table cell
Read as `plan-table-cell` on the Gauth PLUS plans page.

**Values (default).** size 308.75 x 72; padding 33px† `spacing.40` `spacing-offgrid.13` `spacing.40`; border L: `borderWidth.strong` solid `palette.paper.table-line`; background `action.secondary`; text `typography.label-system`, `text.tab`.

**Tokens.** `action.secondary`, `borderWidth.strong`, `palette.paper.table-line`, `spacing-offgrid.13`, `spacing.40`, `text.tab`, `typography.label-system`.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Plan card (plans page)
A white radius-24 card: plan name, price, a full-width button and a benefits list with green checks. Read as `plan-box` on the Gauth PLUS plans page.

**Values (default).** size 312.5 x 409; padding `spacing.28` `spacing.32` `spacing.24` `spacing.32`; radius `radius.24`; background `background.card`; text -apple-system 24/34 600†, `palette.ink.800`; icon 21 x 21, `palette.ink.black`.

**Tokens.** `background.card`, `palette.ink.800`, `palette.ink.black`, `radius.24`, `spacing.24`, `spacing.28`, `spacing.32`.

![Plan card (plans page) default](components/crops/plan-box-default.png)

#### Secondary button (Start for free)
A pale periwinkle 56px button at radius 16. Never pressed. Read as `start-free-button` on the Gauth PLUS plans page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 248.5 x 58; radius `radius.14`; background #d5dffe†; text -apple-system 20/48 600†, `text.primary` |
| hover | background #c8d5ff† |

**Tokens.** `radius.14`, `text.primary`.

![Secondary button (Start for free) default](components/crops/start-free-button-default.png) ![Secondary button (Start for free) hover](components/crops/start-free-button-hover.png) ![Secondary button (Start for free) focus-visible](components/crops/start-free-button-focus-visible.png)

### Dialogs and overlays

The promo dialog every page opens with, the Sign in dialog, the Gauth PLUS dialog, the Create a Course dialog, the science player's audio dialog, the math player's audio gate and the Atlas story preview. The promo's overlay is `rgba(15, 17, 20, 0.45)`; Gauth's own dialogs sit on `rgba(31, 35, 43, 0.7)`. Dialogs were opened and closed again: nothing in them was submitted, chosen or bought.

#### Promo dialog
The announcement every page opens with ("Introducing Gauth Academy"): a 600px white card at radius 24 with a 0 8 20 shadow, a Playfair Display 24/31.2 800 title, a 14/19.6 grey subtitle, a media panel, a full-width black button and a round close button. Read as `promo-dialog` on the Homework home page.

**Values (default).** size 600 x 542.14; radius `radius.24`; background `background.card`; shadow `elevation.promo`; text `typography.promo-title`, `text.primary`.

**Tokens.** `background.card`, `elevation.promo`, `radius.24`, `text.primary`, `typography.promo-title`.

![Promo dialog default](components/crops/promo-dialog-default.png)

#### Promo dialog title
Read as `promo-title` on the Homework home page.

**Values (default).** size 540 x 31.2; background transparent; text `typography.promo-title`, `text.primary`.

**Tokens.** `text.primary`, `typography.promo-title`.

![Promo dialog title default](components/crops/promo-title-default.png)

#### Promo dialog subtitle
Read as `promo-subtitle` on the Homework home page.

**Values (default).** size 540 x 39.19; background transparent; text Playfair Display 14/19.6 400†, `text.secondary`.

**Tokens.** `text.secondary`.

![Promo dialog subtitle default](components/crops/promo-subtitle-default.png)

#### Promo dialog button
"Explore now": black, radius 14, 48px tall, Playfair Display 18/27 600. Hover turns it #21252e; pressed scales it to 0.99. Measured, never pressed. Read as `promo-confirm` on the Homework home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 540 x 48; padding 10.5px† `spacing.16`; radius `radius.14`; background `palette.ink.black`; text Playfair Display 18/27 600†, `text.inverse`; transition background-color `duration.fast` `easing.ease`, transform `duration.fast` `easing.ease` |
| hover | background `action.primary` |
| pressed | size 534.6 x 47.52; background `action.primary`; transform scale `scale.press-promo` |

**Tokens.** `action.primary`, `duration.fast`, `easing.ease`, `palette.ink.black`, `radius.14`, `scale.press-promo`, `spacing.16`, `text.inverse`.

![Promo dialog button default](components/crops/promo-confirm-default.png) ![Promo dialog button hover](components/crops/promo-confirm-hover.png) ![Promo dialog button focus-visible](components/crops/promo-confirm-focus-visible.png) ![Promo dialog button pressed](components/crops/promo-confirm-pressed.png)

#### Promo dialog close button
Read as `promo-close` on the Homework home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 28 x 28; radius `radius.999`; background transparent; text Arial 13.33/normal 400†, `palette.ink.black`; transition opacity `duration.fast` `easing.ease`; icon 28 x 28, `palette.ink.black` |
| hover, pressed | opacity 0.85 |

**Tokens.** `duration.fast`, `easing.ease`, `palette.ink.black`, `radius.999`.

![Promo dialog close button default](components/crops/promo-close-default.png) ![Promo dialog close button hover](components/crops/promo-close-hover.png) ![Promo dialog close button focus-visible](components/crops/promo-close-focus-visible.png) ![Promo dialog close button pressed](components/crops/promo-close-pressed.png)

#### Create a Course dialog
Opened from Create Course: a #faf9f5 sheet with radius 24, a greeting, three suggestion chips, Shuffle, and a prompt field over a blue-to-lilac glow. Nothing was typed into the prompt but sample text, then deleted; no suggestion was pressed. Read as `create-dialog` on the Academy (My Course) page.

**Values (default).** size 720 x 611; radius `radius.24`; background `background.academy`; shadow `elevation.create-dialog`; text `typography.unit-title`, `text.primary`.

**Tokens.** `background.academy`, `elevation.create-dialog`, `radius.24`, `text.primary`, `typography.unit-title`.

![Create a Course dialog default](components/crops/create-dialog-default.png)

#### Course suggestion chip
A white chip with a 600 label and an arrow; pressing one would start a course, so it was only hovered and focused. Read as `create-suggestion` on the Academy (My Course) page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 310 x 54; padding `spacing-offgrid.14` `spacing.20`; border `borderWidth.hairline` solid `palette.paper.line-light`; radius `radius.16`; background `action.secondary`; text `typography.nav-strong`, `text.primary`; icon 13 x 12, `text.primary` |
| hover | border `borderWidth.hairline` solid #d9ddd9†; background #fcfdfc† |

**Tokens.** `action.secondary`, `borderWidth.hairline`, `palette.paper.line-light`, `radius.16`, `spacing-offgrid.14`, `spacing.20`, `text.primary`, `typography.nav-strong`.

![Course suggestion chip default](components/crops/create-suggestion-default.png) ![Course suggestion chip hover](components/crops/create-suggestion-hover.png) ![Course suggestion chip focus-visible](components/crops/create-suggestion-focus-visible.png)

#### Course prompt field
The white radius-16 prompt field at the foot of the dialog with a round send button that stays grey until there is text. Read as `create-prompt` on the Academy (My Course) page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focused) | size 648 x 60; padding `spacing-offgrid.13` `spacing-offgrid.10` `spacing-offgrid.13` `spacing.16`; border `borderWidth.hairline` solid `border.field`; radius `radius.16`; background `background.card`; icon 20 x 20, `text.inverse` |
| filled | text `typography.field`, `text.primary` |

**Tokens.** `background.card`, `border.field`, `borderWidth.hairline`, `radius.16`, `spacing-offgrid.10`, `spacing-offgrid.13`, `spacing.16`, `text.inverse`, `text.primary`, `typography.field`.

![Course prompt field default](components/crops/create-prompt-default.png) ![Course prompt field focused](components/crops/create-prompt-focused.png) ![Course prompt field filled](components/crops/create-prompt-filled.png)

#### Dialog close button
Read as `create-close` on the Academy (My Course) page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 32 x 32; radius `radius.10`; background transparent; text Arial 13.33/normal 400†, `palette.ink.black`; icon 16 x 16, `palette.ink.black` |
| hover | background `palette.ink.a06` |

**Tokens.** `palette.ink.a06`, `palette.ink.black`, `radius.10`.

![Dialog close button default](components/crops/create-close-default.png) ![Dialog close button hover](components/crops/create-close-hover.png) ![Dialog close button focus-visible](components/crops/create-close-focus-visible.png)

#### Enable audio dialog
Shown when a science lesson opens: a 400px white Astryx dialog at radius 20 with a 0 12 32 shadow at 16%, an Inter 24/32 600 title, a 14/20 grey line and two 48px buttons at radius 16. Read as `audio-dialog` on the science lesson page.

**Values (default).** size 400 x 238; radius `radius.20`; background `background.card`; shadow `elevation.level-4`; text `typography.dialog-title`, `palette.astryx.dialog-ink`.

**Tokens.** `background.card`, `elevation.level-4`, `palette.astryx.dialog-ink`, `radius.20`, `typography.dialog-title`.

![Enable audio dialog default](components/crops/audio-dialog-default.png)

#### Secondary button (Not now)
White, 1px #d0d5dd border, radius 16, Inter 15/20 500. Pressed scales it to 0.98. Its focus ring is Astryx's 2px #0064e0 outline. Read as `audio-not-now` on the science lesson page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, focus-visible) | size 165 x 48; border `borderWidth.hairline` solid `action.secondary-border`; radius `radius.16`; background `action.secondary`; text `typography.button`, `palette.astryx.dialog-ink`; transition background-image `duration.astryx` `easing.astryx`, background-color `duration.astryx` `easing.astryx`, color `duration.astryx` `easing.astryx`, opacity `duration.astryx` `easing.astryx`, transform `duration.astryx` `easing.astryx` |
| pressed | size 161.7 x 47.04; transform scale `scale.press` |

**Tokens.** `action.secondary`, `action.secondary-border`, `borderWidth.hairline`, `duration.astryx`, `easing.astryx`, `palette.astryx.dialog-ink`, `radius.16`, `scale.press`, `typography.button`.

![Secondary button (Not now) default](components/crops/audio-not-now-default.png) ![Secondary button (Not now) hover](components/crops/audio-not-now-hover.png) ![Secondary button (Not now) focus-visible](components/crops/audio-not-now-focus-visible.png) ![Secondary button (Not now) pressed](components/crops/audio-not-now-pressed.png)

#### Primary button (Enable audio)
Near-black #1f232b, radius 16, white Inter 15/20 500. Measured, never pressed. Read as `audio-enable` on the science lesson page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, focus-visible) | size 163 x 48; radius `radius.16`; background `palette.astryx.dialog-ink`; text `typography.button`, `text.inverse`; transition background-image `duration.astryx` `easing.astryx`, background-color `duration.astryx` `easing.astryx`, color `duration.astryx` `easing.astryx`, opacity `duration.astryx` `easing.astryx`, transform `duration.astryx` `easing.astryx` |
| pressed | size 159.74 x 47.04; transform scale `scale.press` |

**Tokens.** `duration.astryx`, `easing.astryx`, `palette.astryx.dialog-ink`, `radius.16`, `scale.press`, `text.inverse`, `typography.button`.

![Primary button (Enable audio) default](components/crops/audio-enable-default.png) ![Primary button (Enable audio) hover](components/crops/audio-enable-hover.png) ![Primary button (Enable audio) focus-visible](components/crops/audio-enable-focus-visible.png) ![Primary button (Enable audio) pressed](components/crops/audio-enable-pressed.png)

#### Story preview
A story card opens a video preview over a dark scrim, with a white Explore pill under it. Read as `story-preview` on the Atlas page.

**Values (default).** size 960 x 620; background transparent; text -apple-system 20/30 600†, `text.inverse`; icon 32 x 32, `palette.ink.black`.

Child layers that carry the look: div 960x540 background `palette.ink.black` radius `radius.18` shadow 0px 28px 80px 0px rgba(0, 0, 0, 0.48)†; div 960x540 background `palette.ink.black`; video 960x540 background `palette.ink.black`.

**Tokens.** `palette.ink.black`, `radius.18`, `text.inverse`.

![Story preview default](components/crops/story-preview-default.png)

#### Explore button
Read as `explore-button` on the Atlas page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 116 x 44; padding 0px `spacing.20`; radius `radius.999`; background `action.secondary`; shadow 0px 10px 28px 0px rgba(255, 255, 255, 0.08)†; text Arial 14/44 700†, `palette.ink.black`; transition transform `duration.fast` `easing.ease`, background `duration.fast` `easing.ease` |
| hover | background #f4f4f4†; transform translate(0px, -1px) |

**Tokens.** `action.secondary`, `duration.fast`, `easing.ease`, `palette.ink.black`, `radius.999`, `spacing.20`.

![Explore button default](components/crops/explore-button-default.png) ![Explore button hover](components/crops/explore-button-hover.png) ![Explore button focus-visible](components/crops/explore-button-focus-visible.png)

#### Audio gate
The math player asks for a tap instead of a dialog: a line of text and a dark Continue button over the blurred slide. Read as `audio-gate` on the math lesson page.

**Values (default).** size 1046 x 818; padding `spacing.32`; background `palette.paper.glass`; text `typography.body`, `text.primary`.

**Tokens.** `palette.paper.glass`, `spacing.32`, `text.primary`, `typography.body`.

![Audio gate default](components/crops/audio-gate-default.png)

#### Continue button
Read as `continue-button` on the math lesson page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 180 x 48; padding 0px `spacing.24`; radius `radius.16`; background `action.primary`; text -apple-system 16/normal 700†, `text.inverse`; transition transform `duration.press` `easing.ease`, background `duration.fast` `easing.ease` |
| hover | background #343943† |
| pressed | size 176.4 x 47.04; background #343943†; transform scale `scale.press` |

**Tokens.** `action.primary`, `duration.fast`, `duration.press`, `easing.ease`, `radius.16`, `scale.press`, `spacing.24`, `text.inverse`.

![Continue button default](components/crops/continue-button-default.png) ![Continue button hover](components/crops/continue-button-hover.png) ![Continue button focus-visible](components/crops/continue-button-focus-visible.png) ![Continue button pressed](components/crops/continue-button-pressed.png)

#### Sign in dialog
A 460px white sheet over a dark scrim: a 36px bold "Welcome", a grey line with a red Sign up link, three outlined social buttons, an OR rule, an email field and a full-width Sign in button in the brand red, pale while disabled. Opened and closed; nothing was submitted. Read as `signin-dialog` on the Homework home page.

**Values (default).** size 460 x 559.8; radius `radius.24`; background `background.card`; text `typography.dialog-display`, `palette.ink.black`; icon 28 x 28, `text.primary`.

**Tokens.** `background.card`, `palette.ink.black`, `radius.24`, `text.primary`, `typography.dialog-display`.

![Sign in dialog default](components/crops/signin-dialog-default.png)

#### Dialog scrim
The full-window layer behind Gauth's own dialogs. Read as `signin-scrim` on the Homework home page.

**Values (default).** size 1440 x 900; background `background.scrim-dialog`; text `typography.dialog-display`, `palette.ink.black`; icon 28 x 28, `text.primary`.

**Tokens.** `background.scrim-dialog`, `palette.ink.black`, `text.primary`, `typography.dialog-display`.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Social sign-in button
A 400 x 54 outlined pill: 1px border, radius 9999, a brand mark and a 16px label. Hovered only. Read as `signin-social` on the Homework home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 400 x 40; border `borderWidth.hairline` solid #dadce0†; radius `radius.20`; background transparent; text `typography.label-system`, `palette.ink.black`; icon 20 x 20, `palette.ink.black` |
| hover | border `borderWidth.hairline` solid #d2e3fc†; background rgba(66, 133, 244, 0.04)† |

**Tokens.** `borderWidth.hairline`, `palette.ink.black`, `radius.20`, `typography.label-system`.

![Social sign-in button default](components/crops/signin-social-default.png) ![Social sign-in button hover](components/crops/signin-social-hover.png)

#### Email field
A 400 x 48 grey field, radius 12, a mail icon and a clear button once text is typed. A throwaway string was typed and deleted; Gauth shows no inline error on blur, it only keeps Sign in disabled. Read as `signin-email` on the Homework home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 400 x 48; border `borderWidth.hairline` solid `border.sidebar`; radius `radius.12`; background `background.selected`; icon 24 x 25, `palette.ink.black` |
| focused, filled | border `borderWidth.hairline` solid `component.field.border-focus` |

**Tokens.** `background.selected`, `border.sidebar`, `borderWidth.hairline`, `component.field.border-focus`, `palette.ink.black`, `radius.12`.

![Email field default](components/crops/signin-email-default.png) ![Email field hover](components/crops/signin-email-hover.png) ![Email field focused](components/crops/signin-email-focused.png) ![Email field filled](components/crops/signin-email-filled.png)

#### Primary button, disabled (Sign in)
The dialog's Sign in button while the email field is empty: Gauth's button_btn-primary in its disabled skin (button_btn-disabled). Never pressed. Read as `signin-submit` on the Homework home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| disabled (same: hover) | size 400 x 54; border `borderWidth.hairline` solid transparent; radius `radius.14`; background `action.accent-disabled`; text `typography.button-xl`, `text.inverse` |

**Tokens.** `action.accent-disabled`, `borderWidth.hairline`, `radius.14`, `text.inverse`, `typography.button-xl`.

![Primary button, disabled (Sign in) disabled](components/crops/signin-submit-disabled.png) ![Primary button, disabled (Sign in) hover](components/crops/signin-submit-hover.png)

#### Inline link (Sign up)
A red text link inside a grey line. Hovered only. Read as `signup-link` on the Homework home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 49.69 x 17; background transparent; text `typography.label-system`, `text.brand` |

**Tokens.** `text.brand`, `typography.label-system`.

![Inline link (Sign up) default](components/crops/signup-link-default.png) ![Inline link (Sign up) hover](components/crops/signup-link-hover.png)

#### Inline link (Terms of Service)
A darker, medium-weight link inside the 14px grey terms line. Read as `terms-link` on the Homework home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 97.09 x 15; background transparent; text -apple-system 12/18 500†, `text.secondary` |
| hover | text -apple-system 12/18 500†, `text.link` |

**Tokens.** `text.link`, `text.secondary`.

![Inline link (Terms of Service) default](components/crops/terms-link-default.png) ![Inline link (Terms of Service) hover](components/crops/terms-link-hover.png) ![Inline link (Terms of Service) focus-visible](components/crops/terms-link-focus-visible.png)

#### Dialog close button (Gauth)
Read as `modal-close` on the Homework home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 28 x 28; background transparent; icon 28 x 28, `text.primary` |

**Tokens.** `text.primary`.

![Dialog close button (Gauth) default](components/crops/modal-close-default.png) ![Dialog close button (Gauth) hover](components/crops/modal-close-hover.png)

#### Gauth PLUS dialog
A 1060 x 580 two-panel dialog: a warm gradient panel with an italic title and the benefits table at the left, the email field, three plan cards and a dark Join button at the right. Opened and closed; nothing chosen or bought. Read as `plus-dialog` on the Homework home page.

**Values (default).** size 1060 x 580; radius `radius.20`; background `background.card`; text -apple-system 30/39 900†, `component.plus-card.button-text`; icon 119 x 196, `text.primary`.

**Tokens.** `background.card`, `component.plus-card.button-text`, `radius.20`, `text.primary`.

![Gauth PLUS dialog default](components/crops/plus-dialog-default.png)

#### Table (benefits)
A three-column comparison inside a 2px gold-bordered card at radius 24: a 600 header row (All Benefits, Gauth PLUS in gold, Free), then 24px rows split into label, a green check or value, and a grey dash. Read as `benefits-table` on the Homework home page.

**Values (default).** size 460 x 347; padding `spacing-offgrid.22` `spacing.20`; border `borderWidth.strong` solid #ffb94d†; radius `radius.20`; background transparent; image linear-gradient(107.49deg, rgba(255, 196, 106, 0.3)† -2.04%, rgba(255, 196, 106, 0.15)† 69.72%); text `typography.button-lg`, `text.primary`; icon 41 x 35, `text.primary`.

**Tokens.** `borderWidth.strong`, `radius.20`, `spacing-offgrid.22`, `spacing.20`, `text.primary`, `typography.button-lg`.

![Table (benefits) default](components/crops/benefits-table-default.png)

#### Table row (benefits)
Read as `benefits-row` on the Homework home page.

**Values (default).** size 416 x 24; background transparent; text SF Pro 16/24 500†, #3d2b09†; icon 18 x 18, #3d2b09†.

![Table row (benefits) default](components/crops/benefits-row-default.png)

#### Plan card (single choice)
One of three 147 x 160 cards that behave as a single-choice group: 2px border, radius 16, a grey 20px period, a bold price. Hovered, focused and pressed by DevTools only, so the choice never changed. Read as `plan-card` on the Homework home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 146.67 x 160; padding `spacing-offgrid.30` `spacing.12` `spacing.16` `spacing.12`; border `borderWidth.choice` solid `border.field`; radius `radius.16`; background `background.card`; text Arial 18/25.2 590†, `text.meta` |
| hover, pressed | border `borderWidth.choice` solid #d7dbe3† |

**Tokens.** `background.card`, `border.field`, `borderWidth.choice`, `radius.16`, `spacing-offgrid.30`, `spacing.12`, `spacing.16`, `text.meta`.

![Plan card (single choice) default](components/crops/plan-card-default.png) ![Plan card (single choice) hover](components/crops/plan-card-hover.png) ![Plan card (single choice) focus-visible](components/crops/plan-card-focus-visible.png) ![Plan card (single choice) pressed](components/crops/plan-card-pressed.png)

#### Plan card, selected
The preselected 12 Months card: a gold border and a gold corner tag. Read as `plan-card-selected` on the Homework home page.

**Values (selected).** size 146.67 x 160; padding `spacing-offgrid.30` `spacing.12` `spacing.16` `spacing.12`; border `borderWidth.choice` solid `palette.gold.plan`; radius `radius.16`; background `background.card`; text `typography.plan-tag`, `text.inverse`.

**Tokens.** `background.card`, `borderWidth.choice`, `palette.gold.plan`, `radius.16`, `spacing-offgrid.30`, `spacing.12`, `spacing.16`, `text.inverse`, `typography.plan-tag`.

![Plan card, selected selected](components/crops/plan-card-selected-selected.png)

#### Badge (plan tag)
The gold tag on a plan card's top edge. Read as `plan-tag` on the Homework home page.

**Values (default).** size 50 x 21; padding `spacing-offgrid.2` `spacing.8`; radius 0px `radius.16` 0px `radius.10`; background `palette.gold.plan`; text `typography.plan-tag`, `text.inverse`.

**Tokens.** `palette.gold.plan`, `radius.10`, `radius.16`, `spacing-offgrid.2`, `spacing.8`, `text.inverse`, `typography.plan-tag`.

![Badge (plan tag) default](components/crops/plan-tag-default.png)

#### Join Gauth PLUS button
A dark brown full-width pill with gold text and an arrow. Hovered only; never pressed. Read as `join-button` on the Homework home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 460 x 48; radius `radius.14`; background `component.plus-card.button-text`; text -apple-system 16/22.4 590†, `component.plus-card.rule`; icon 18 x 18, `component.plus-card.rule` |

**Tokens.** `component.plus-card.button-text`, `component.plus-card.rule`, `radius.14`.

![Join Gauth PLUS button default](components/crops/join-button-default.png) ![Join Gauth PLUS button hover](components/crops/join-button-hover.png)

#### Email field (PLUS dialog)
Not typed into. Read as `plus-email` on the Homework home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 420 x 48; padding `spacing.12` `spacing-offgrid.10` `spacing.12` `spacing.16`; radius `radius.16`; background `background.selected`; shadow 0px 0px 0px 1px #edeef1 inset†; icon 24 x 24, `text.tertiary` |

**Tokens.** `background.selected`, `radius.16`, `spacing-offgrid.10`, `spacing.12`, `spacing.16`, `text.tertiary`.

![Email field (PLUS dialog) default](components/crops/plus-email-default.png) ![Email field (PLUS dialog) hover](components/crops/plus-email-hover.png)

#### Primary button, brand red (Sign in)
Gauth's own button component (button_btn-primary) in the Sign in dialog, enabled once the field holds an address: brand red #ff013e, hover #f00039, pressed #d80033 (its :active rule). name@example.com was typed and deleted; the button was never pressed. Read as `accent-button` on the Homework home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 400 x 54; border `borderWidth.hairline` solid transparent; radius `radius.14`; background `action.accent`; text `typography.button-xl`, `text.inverse` |
| hover | background `action.accent-hover` |
| pressed | background `action.accent-pressed` |

**Tokens.** `action.accent`, `action.accent-hover`, `action.accent-pressed`, `borderWidth.hairline`, `radius.14`, `text.inverse`, `typography.button-xl`.

![Primary button, brand red (Sign in) default](components/crops/accent-button-default.png) ![Primary button, brand red (Sign in) hover](components/crops/accent-button-hover.png) ![Primary button, brand red (Sign in) pressed](components/crops/accent-button-pressed.png)

#### Text field, error (forced)
The email field with Gauth's own error classes added in DevTools: form_error on the field turns it #fff2f2 with a #f00039 border, and input_email-error on its input wrapper turns the typed text and the mail icon red. Gauth shows them after a submit, which the capture never made, so the classes were forced to read the rules. Read as `field-error` on the Homework home page.

**Values (error).** size 400 x 48; border `borderWidth.hairline` solid `component.field.error-border`; radius `radius.12`; background `component.field.error-background`; field typed text `component.field.error-text` on `component.field.error-background`, icon `component.field.error-border`; icon 24 x 25, `palette.ink.black`.

**Tokens.** `borderWidth.hairline`, `component.field.error-background`, `component.field.error-border`, `component.field.error-text`, `palette.ink.black`, `radius.12`.

![Text field, error (forced) error](components/crops/field-error-error.png)

#### Text field, focused (sign-up password)
Focusing a sign-up field gives it Gauth's form_active border (#8e8e93) and shows the rule line under the password field. Focused only; nothing typed. Read as `field-focused` on the Homework home page.

**Values (focused).** size 400 x 48; border `borderWidth.hairline` solid `component.field.border-focus`; radius `radius.12`; background `component.field.background`; icon 24 x 25, `palette.ink.black`.

**Tokens.** `borderWidth.hairline`, `component.field.background`, `component.field.border-focus`, `palette.ink.black`, `radius.12`.

![Text field, focused (sign-up password) focused](components/crops/field-focused-focused.png)

#### Field helper text
The rule line Gauth shows under the password field while it has focus: "Use 6-20 characters from at least 2 categories". Read as `field-helper` on the Homework home page.

**Values (focused).** size 400 x 36; background transparent; text `typography.chip-label`, `component.field.helper-text`.

**Tokens.** `component.field.helper-text`, `typography.chip-label`.

![Field helper text focused](components/crops/field-helper-focused.png)

### Mobile (390 wide)

A few components as a phone draws them, at 390 x 844 with an iPhone user agent.

#### Promo dialog (mobile)
Read as `m-promo-dialog` on the Homework home page at 390 wide.

**Values (default).** size 358 x 437.22; radius `radius.24`; background `background.card`; shadow `elevation.promo`; text `typography.promo-title`, `text.primary`.

**Tokens.** `background.card`, `elevation.promo`, `radius.24`, `text.primary`, `typography.promo-title`.

![Promo dialog (mobile) default](components/crops/m-promo-dialog-default.png)

#### Mobile top bar
Logo and a menu button; the sidebar becomes a drawer. Read as `m-header` on the Homework home page at 390 wide.

**Values (default).** size 390 x 60; background transparent; icon 24 x 24, `text.primary`.

**Tokens.** `text.primary`.

![Mobile top bar default](components/crops/m-header-default.png)

#### Mobile menu button
Read as `m-menu-button` on the Homework home page at 390 wide.

**Values (default).** size 44 x 27; background transparent; icon 24 x 24, `palette.ink.black`.

**Tokens.** `palette.ink.black`.

![Mobile menu button default](components/crops/m-menu-button-default.png)

#### Mobile question field
Read as `m-question-box` on the Homework home page at 390 wide.

**Values (default).** size 322 x 36; radius `radius.6`; background transparent; text -apple-system 13/18 400, letter spacing 0.13px†, `palette.antd.text`; transition all `duration.popover` `easing.ease`; placeholder `text.tertiary`.

**Tokens.** `duration.popover`, `easing.ease`, `palette.antd.text`, `radius.6`, `text.tertiary`.

![Mobile question field default](components/crops/m-question-box-default.png)

#### App banner (mobile)
A bottom banner with the app icon, rating and an Open pill. Open was not pressed. Read as `m-app-banner` on the Homework home page at 390 wide.

**Values (default).** size 390 x 64; padding `spacing-offgrid.14` `spacing.12` `spacing-offgrid.14` `spacing-offgrid.14`; radius `radius.16` `radius.16` 0px 0px; background `background.card`; shadow 0px -4px 16px 0px rgba(0, 0, 0, 0.12)†; text -apple-system 14/19.6 600†, `text.primary`; icon 12 x 13, `text.inverse`.

**Tokens.** `background.card`, `radius.16`, `spacing-offgrid.14`, `spacing.12`, `text.inverse`, `text.primary`.

![App banner (mobile) default](components/crops/m-app-banner-default.png)

#### Unit card (mobile)
On a phone the unit card is a 112px row card at radius 20 with a 4px track. Read as `m-unit-card` on the Academy (Math Curriculum) page at 390 wide.

**Values (default).** size 358 x 112; padding `spacing-offgrid.11` `spacing.12` `spacing.12` `spacing-offgrid.11`; border `borderWidth.hairline` solid `border.card`; radius `radius.20`; background `background.card`; shadow `elevation.level-1`; text Inter 15/21 600†, `text.primary`; transition box-shadow `duration.fast` `easing.ease`.

**Tokens.** `background.card`, `border.card`, `borderWidth.hairline`, `duration.fast`, `easing.ease`, `elevation.level-1`, `radius.20`, `spacing-offgrid.11`, `spacing.12`, `text.primary`.

![Unit card (mobile) default](components/crops/m-unit-card-default.png)

#### Category tab (mobile)
Read as `m-category-tab` on the Academy (Math Curriculum) page at 390 wide.

**Values (default).** size 147.28 x 36; padding 0px `spacing-offgrid.15`; border `borderWidth.hairline` solid transparent; radius `radius.12`; background `background.selected-warm`; text `typography.tab-strong`, `text.primary`.

**Tokens.** `background.selected-warm`, `borderWidth.hairline`, `radius.12`, `spacing-offgrid.15`, `text.primary`, `typography.tab-strong`.

![Category tab (mobile) default](components/crops/m-category-tab-default.png)

#### Create button (mobile)
On a phone Create Course shrinks to "+ Create" on a #f4f2e6 pill. Read as `m-create-button` on the Academy (Math Curriculum) page at 390 wide.

**Values (default).** size 82 x 32; padding 0px 7px†; radius `radius.12`; background `palette.sand.create-mobile`; text `typography.label`, `text.primary`; icon 16 x 16, `text.primary`.

**Tokens.** `palette.sand.create-mobile`, `radius.12`, `text.primary`, `typography.label`.

![Create button (mobile) default](components/crops/m-create-button-default.png)

## Icons

99 SVGs were lifted from the pages into [icons/](icons), named by role, with the source table in [icons/INDEX.tsv](icons/INDEX.tsv). Colour is `currentColor` wherever the icon took its colour from the text, so each recolours from CSS `color`. Lesson content (the canvas, slides and formulas) was left out; these are the interface icons. The SVGs are Gauth's property, kept for reference only.

| Icon | Rendered sizes | View box | Style | Seen on | Next to |
|---|---|---|---|---|---|
| [gauth-mark](icons/gauth-mark.svg) | 24x24 | 0 0 24 24 | fill | home; academy; news; unit; atlas; atlas story |  |
| [nav-atlas](icons/nav-atlas.svg) | 24x24 | 0 0 24 24 | fill | home; academy; news; unit | Atlas |
| [gauth-wordmark](icons/gauth-wordmark.svg) | 58x15 | 0 0 69.9824 17.7508 | fill | home; academy; news; unit |  |
| [collapse-sidebar](icons/collapse-sidebar.svg) | 24x24 | 0 0 24 24 | stroke | home; academy; news; unit | Collapse sidebar |
| [nav-app](icons/nav-app.svg) | 24x24 | 0 0 24 24 | fill | home; academy; news; unit | App |
| [nav-insights](icons/nav-insights.svg) | 24x25 | 0 0 24 25 | stroke | home; academy; unit | Insights |
| [exit-lesson](icons/exit-lesson.svg) | 40x40 | 0 0 40 40 | fill | lesson-math; lesson-history | Exit lesson |
| [chevron-down-select](icons/chevron-down-select.svg) | 11x11 | 0 0 11 11 | stroke | home; news; atlas | English English |
| [exit-lesson-canvas](icons/exit-lesson-canvas.svg) | 40x40 | 0 0 40 40 | fill | lesson-science | Exit lesson |
| [next-block](icons/next-block.svg) | 32x32 | 0 0 32 32 | fill | lesson-science | Next block |
| [social-tiktok](icons/social-tiktok.svg) | 24x24 | 0 0 25 24 | fill | home; news; atlas |  |
| [social-facebook](icons/social-facebook.svg) | 24x24 | 0 0 25 24 | fill | home; news; atlas |  |
| [social-youtube](icons/social-youtube.svg) | 24x24 | 0 0 25 24 | fill | home; news; atlas |  |
| [reset-view](icons/reset-view.svg) | 32x32 | 0 0 32 32 | fill | lesson-science | Reset view |
| [previous-block](icons/previous-block.svg) | 32x32 | 0 0 32 32 | fill | lesson-science | Previous block |
| [nav-homework](icons/nav-homework.svg) | 24x25 | 0 0 24 25 | stroke | academy; news; unit | Homework |
| [settings](icons/settings.svg) | 32x32 | 0 0 32 32 | fill | lesson-science | Settings |
| [social-instagram](icons/social-instagram.svg) | 24x24 | 0 0 24 24 | fill | home; news; atlas |  |
| [microphone](icons/microphone.svg) | 40x40 | 0 0 40 40 | fill | lesson-science | Ask by voice |
| [chevron-down-small](icons/chevron-down-small.svg) | 14x14 | 0 0 14 14 | fill | home; news |  |
| [nav-academy](icons/nav-academy.svg) | 24x24 | 0 0 24 24 | fill | home; news | Academy |
| [key-v](icons/key-v.svg) | 18x19 | 0 0 18 19 | fill | home; news | Drag Image orClick Hereto upload Command |
| [bolt](icons/bolt.svg) | 14x15 | 0 0 14 15 | fill | home; news | Upgrade |
| [key-command](icons/key-command.svg) | 18x19 | 0 0 18 19 | fill | home; news | Drag Image orClick Hereto upload Command |
| [plus-badge](icons/plus-badge.svg) | 44x19 | 0 0 44 19 | fill | home; news | Gauth |
| [upload-image](icons/upload-image.svg) | 30x30 | 0 0 34 34 | fill | home; news | Drag Image orClick Hereto upload Command |
| [nav-academy-active](icons/nav-academy-active.svg) | 24x24 | 0 0 24 24 | fill | academy; unit | Academy |
| [check-badge](icons/check-badge.svg) | 12x12 | 0 0 12 12 | fill | home; news | Unlimited Answers / Gauth AI Pro |
| [arrow-right-bold](icons/arrow-right-bold.svg) | 15x15 | 0 0 15 15 | stroke | home; news | Start Free Trial |
| [nav-homework-active](icons/nav-homework-active.svg) | 24x25 | 0 0 24 25 | fill | home | Homework |
| [chapters-list-math](icons/chapters-list-math.svg) | 18x18 | 0 0 18.2 18.2 | fill | lesson-math | Open lesson chapters |
| [question-submit](icons/question-submit.svg) | 29x28 | 0 0 29 28 | stroke | home |  |
| [chevron-left](icons/chevron-left.svg) | 40x40 | 0 0 40 40 | fill | lesson-math | Previous lesson page / Next lesson page |
| [rating-star](icons/rating-star.svg) | 14x14 | 0 0 10 10 | fill | home | 4.8 (1.9M) |
| [solution-steps](icons/solution-steps.svg) | 24x24 | 0 0 24 24 | fill | home |  |
| [app-store](icons/app-store.svg) | 20x20 | 0 0 20 20 | fill | home | App Store |
| [tutor-explaining](icons/tutor-explaining.svg) | 13x14 | 0 0 12.732 13.558 | fill | lesson-math |  |
| [atlas-feature-1](icons/atlas-feature-1.svg) | 32x36 | 0 0 32 35.556 | fill | home |  |
| [arrow-right-grey](icons/arrow-right-grey.svg) | 18x18 | 0 0 19 18 | stroke | home; news |  |
| [carousel-previous](icons/carousel-previous.svg) | 48x48 | 0 0 48 48 | fill | home |  |
| [atlas-feature-2](icons/atlas-feature-2.svg) | 32x36 | 0 0 32 35.556 | stroke | home |  |
| [subject-biology](icons/subject-biology.svg) | 29x29 | 0 0 29 29 | fill | home | Biology |
| [subject-calculus](icons/subject-calculus.svg) | 29x29 | 0 0 29 29 | stroke | home | Calculus |
| [sparkle](icons/sparkle.svg) | 20x20 | 0 0 32 32 | fill | academy | Create Course |
| [pause-thin](icons/pause-thin.svg) | 27x27 | 0 0 26.819 26.819 | fill | lesson-math | Pause lesson |
| [check](icons/check.svg) | 13x10 | 0 0 13 10 | fill | home | 50k verified expert / 98.5% satisfaction rate / Solves the t |
| [chapter-video](icons/chapter-video.svg) | 14x14 | 0 0 14 14 | fill | lesson-history | 2 / 3 / 4 |
| [atlas-feature-3](icons/atlas-feature-3.svg) | 32x36 | 0 0 32 35.556 | fill | home |  |
| [chapters-list](icons/chapters-list.svg) | 20x20 24x24 | 0 0 20 20 | fill | lesson-history | Open chapters / Crossing the Ocean Wall / Close chapters |
| [chapter-playing](icons/chapter-playing.svg) | 14x14 | 0 0 14 14 | stroke | lesson-history | Technology / 1 Technology The borrowed global technol |
| [carousel-next](icons/carousel-next.svg) | 48x48 | 0 0 48 48 | fill | home |  |
| [subject-math](icons/subject-math.svg) | 29x29 | 0 0 29 29 | fill | home | Math |
| [solution-fast](icons/solution-fast.svg) | 24x24 | 0 0 24 24 | fill | home |  |
| [pause](icons/pause.svg) | 32x32 | 0 0 32 32 | fill | lesson-science | Pause |
| [upload-image-small](icons/upload-image-small.svg) | 24x24 | 0 0 30 30 | stroke | home; news |  |
| [play-circle](icons/play-circle.svg) | 20x20 | 0 0 20 20 | stroke | home | Watch Demo |
| [play-large](icons/play-large.svg) | 26x26 | 0 0 26 26 | fill | lesson-history | Play |
| [close](icons/close.svg) | 22x22 | 0 0 24 24 | stroke | lesson-history | Close chapters |
| [play](icons/play.svg) | 32x32 | 0 0 32 32 | fill | lesson-science | Play |
| [sound-off](icons/sound-off.svg) | 20x20 | 0 0 16 16 | fill | home | Unmute preview video |
| [plus](icons/plus.svg) | 20x20 | 0 0 20 20 | fill | atlas; atlas story | New Topic |
| [microphone-small](icons/microphone-small.svg) | 30x30 | 0 0 30 30 | fill | lesson-math | Record a question |
| [atlas-feature-4](icons/atlas-feature-4.svg) | 32x36 | 0 0 32 35.556 | stroke | home |  |
| [gauth-ai-sparkle](icons/gauth-ai-sparkle.svg) | 28x28 | 0 0 24 24 | fill | home | Gauth AI |
| [search](icons/search.svg) | 20x20 | 0 0 20 20 | stroke | atlas; atlas story |  |
| [arrow-right](icons/arrow-right.svg) | 16x16 | 0 0 16 16 | stroke | home | Start Exploring |
| [star](icons/star.svg) | 16x16 | 0 0 20 21 | fill | home |  |
| [subject-business](icons/subject-business.svg) | 29x29 | 0 0 29 29 | fill | home | Business |
| [subject-social-science](icons/subject-social-science.svg) | 28x28 | 0 0 28 28 | fill | home | Social Science |
| [chevron-right-small](icons/chevron-right-small.svg) | 12x12 | 0 0 12 12 | stroke | home | MORE |
| [subject-chemistry](icons/subject-chemistry.svg) | 29x29 | 0 0 29 29 | fill | home | Chemistry |
| [solution-explanations](icons/solution-explanations.svg) | 24x24 | 0 0 24 24 | fill | home |  |
| [google-play](icons/google-play.svg) | 28x28 | 0 0 28 28 | fill | home | Google Play |
| [menu](icons/menu.svg) | 20x24 | 0 0 24 24 | stroke | atlas; atlas story | Toggle atlas session drawer |
| [export-pdf](icons/export-pdf.svg) | 15x17 | 0 0 14.582 16.377 | stroke | lesson-science | Export PDF |
| [zoom-in](icons/zoom-in.svg) | 20x20 | 0 0 20 20 | stroke | lesson-science | Zoom in |
| [send-disabled](icons/send-disabled.svg) | 20x20 | 0 0 17.778 17.778 | stroke | academy | Send |
| [zoom-out](icons/zoom-out.svg) | 20x20 | 0 0 20 20 | stroke | lesson-science | Zoom out |
| [send-up](icons/send-up.svg) | 40x40 | 0 0 40 40 | fill | lesson-science | Send question |
| [speed](icons/speed.svg) | 20x20 | 0 0 20 20 | stroke | lesson-science | Speed 1x |
| [shuffle](icons/shuffle.svg) | 20x20 | 0 0 18.001 18.001 | fill | academy | Shuffle |
| [captions](icons/captions.svg) | 24x24 | 0 0 24 24 | stroke | lesson-science | Captions |
| [narration](icons/narration.svg) | 36x36 | 0 0 36 36 | fill | lesson-science | Narration |
| [solution-4](icons/solution-4.svg) | 24x24 | 0 0 24 24 | fill | home |  |
| [chevron-down](icons/chevron-down.svg) | 14x14 | 0 0 16 16 | stroke | academy | Show 14 more / Show 15 more |
| [view-eye](icons/view-eye.svg) | 18x18 | 0 0 24 24 | stroke | atlas story | View |
| [chevron-right](icons/chevron-right.svg) | 16x16 | 0 0 16 16 | stroke | lesson-science | Speed 1x |
| [arrow-right-thin](icons/arrow-right-thin.svg) | 18x18 | 0 0 18 18 | stroke | atlas | Send atlas prompt |
| [zoom](icons/zoom.svg) | 20x20 | 0 0 20 20 | stroke | lesson-science |  |
| [switch-off](icons/switch-off.svg) | 36x21 | 0 0 36 21 | fill | lesson-science | Narration / Captions |
| [close-round](icons/close-round.svg) | 28x28 | 0 0 28 28 | fill | home | Close |
| [globe](icons/globe.svg) | 13x13 | 0 0 16 16 | stroke | atlas | Search |
| [details-help](icons/details-help.svg) | 18x18 | 0 0 24 24 | fill | atlas story | Details |
| [breadcrumb-separator](icons/breadcrumb-separator.svg) | 12x13 | 0 0 12 13 | fill | news |  |
| [nav-insights-active](icons/nav-insights-active.svg) | 24x25 | 0 0 24 25 | fill | news | Insights |
| [close-small](icons/close-small.svg) | 16x16 | 0 0 16 16 | fill | academy | Close |
| [chevron-down-tiny](icons/chevron-down-tiny.svg) | 14x14 | 0 0 14 14 | fill | atlas |  |
| [generate-video](icons/generate-video.svg) | 16x16 19x19 | 0 0 18 18 | fill | atlas story | Generate Atlas video / Video Settings |
| [arrow-right-small](icons/arrow-right-small.svg) | 13x12 | 0 0 12.738 11.14 | stroke | academy | Perimeter and Area of Rectangles / Rocks, Minerals and the R |

## Gaps

### Pages

- **Signed-in pages.** Nothing behind sign-in was captured: a learner's own My Course list, course progress, history, the homework answer page, Atlas topics a learner made, account settings and the subscription checkout. The kit never signs in.
- **Anything that sends or creates.** No homework question was submitted (so the answer and step-by-step pages are missing), no course was generated from Create a Course, no tutor message or voice question was sent, no Atlas story was generated, no file was uploaded, and no dialog was submitted. The answers given are to the science lesson's practice check-in, once wrong and once right on two visits, which a signed-out visitor answers as part of the lesson.
- **Toast and checkbox.** Neither was seen. No toast appeared after any action the capture took, and no public form has a checkbox; the Sign in dialog states its terms in a line of text instead.
- **Study Resources.** `/study-resources/*` redirects to gauthmath.com, which answers a headless browser with Access Denied.
- **The science lesson's Completed screen** (a cover, a laurel "Completed" title, Share and View Canvas) was seen while exploring, after a lesson played to its end, but the kit does not wait the several minutes it takes, so there is no crop or measurement.
- **Mobile science lessons.** A phone is redirected from `/course/science` to `/course/math`; Science Labs is not offered on a phone.
- **Other lesson kinds.** Math lessons carry interactive steps (matching, drag, number lines, flashcards, graphs; their CSS is in the stylesheets) that only appear as a lesson plays on; the capture saw the first slides only.

### States

- **Pressed** was forced with DevTools on every control except toggles, so a state a script adds on mousedown (if any) is missing.
- **Hover on the feature cards, the article rows, the Share button and the play disc** changed nothing measurable; their entries read 'same'.
- **The tutor transcript** held only the status line during the 25 seconds of playback the kit waits; transcript text was not captured.
- **Disabled states** were found on three controls: the Sign in dialog's Sign in button (brand red at low strength), the Atlas Send button while the box is empty (it turns dark, enabled, once text is typed), and the blog's Previous arrow on page 1. Gauth shows no inline error while typing: the Sign in dialog keeps its button disabled instead. Its CSS declares the error state a submit would show (`form_error`: a `#fff2f2` field with a `#f00039` border, a red 14/20 message); the capture forced that class in DevTools to read it ([text-field-error-forced](#text-field-error-forced)).
- **Loading states.** The pages render on the server, so the skeletons in Gauth's CSS (`catalog_mathSkeleton*`, `math-course-detail_detailSkeletonBanner`) never showed, even with the data request held back. The nearest to a loading state is the math tutor's status line, which shimmers while it narrates; it was read at rest, as its default state ([tutor-status-line](#tutor-status-line)).

### Themes

Gauth shows one light theme. Its stylesheets do declare dark values: TikTok's TUX theme under `[data-theme="dark"]` and `.twv-container` with `prefers-color-scheme: dark`, the lesson palette under `[data-lesson-style="dark"]`, and Astryx's stone theme as `light-dark()` pairs. None of them is applied on any page captured: no page sets a dark attribute, the science player pins `data-theme="light"`, and every page painted the same under `prefers-color-scheme: dark` (`themeChecks` in [raw/css-vars.json](raw/css-vars.json)). There is no theme switch in the sidebar, the lesson Settings or the footer. The token file therefore ships no dark set, and the dark declarations stay in the raw file for reference.

### Fonts

- **SF Pro** is Apple's system face; Gauth declares an "SF Pro" family over `local()` only, so it renders as SF Pro on Apple devices and falls back elsewhere.
- **Satoshi** (the science canvas's "Canvas Print" and "Canvas Heading") is from Fontshare and is not on Google Fonts; the style guide falls back to the system font.
- **Rubik**, named on small Atlas labels, has no `@font-face` on the page and rendered as a fallback in the capture.

### Screenshots

- Covers, illustrations, videos and story images are Gauth's content and appear only inside screenshots and crops. The lesson canvas and the Atlas story keep moving, so two captures of the same view can differ in what the narration has drawn.
- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files.

### Content left out

- Lesson content (slides, canvas drawings, formulas, narration) was not transcribed; only the frames around it were measured.
- No personal data was captured: the pages were read signed out, and the Atlas drawer was empty.
