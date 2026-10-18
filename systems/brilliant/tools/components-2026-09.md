<!-- Input to build_components_md.py: the 2026-09-25 discovery list and component inventory, kept as written then (headings demoted one level). -->
### Discovery list

Every page, view and overlay found, with what was captured. D is dark, L is light, M is the 390x844 mobile width. Screenshot names are in [screenshots/](screenshots).

#### Public pages (headless Chromium, 1440x900 and 390x844)

| Surface | URL | Themes | Captured | Screenshots |
|---|---|---|---|---|
| Landing | `/` | L only (ignores dark) | desktop, M | `landing-light-default`, `mobile-landing-light-default` |
| Sign up | `/signup` → `/welcome/` | L only | desktop, M | `signup-light-default`, `mobile-signup-light-default` |
| Log in | `/login/` | L, D | desktop, M | `login-{light,dark}-default`, `mobile-login-*` |
| Course catalog (public) | `/courses/` | L, D | desktop, M | `courses-public-*`, `mobile-courses-public-*` |
| Course page (public) | `/courses/<slug>/` | L, D | desktop, M | `course-public-*`, `mobile-course-public-*` |
| Pricing | `/subscribe/` | L, D | viewport, full page, M | `pricing-{light,dark}-{default,fullpage}`, `mobile-pricing-*` |
| 404 (legacy Django) | any bad path | L only | desktop, M | `notfound-light-404`, `mobile-notfound-light-404` |

#### Signed-in app (Chrome, 1384x797; 31 screenshots at 2x, 18 at 1x)

| Surface | Where | Captured | Screenshots |
|---|---|---|---|
| Onboarding: intro, voice choice, Koji demo, subject, level list, placement intro and question, result | `/welcome/…` | D; hover and selected card states | `onboarding-dark-*` (11) |
| Returning-learner promo | `/welcome/recommendations` | D | `promo-dark-returning-learner-offer` |
| "Creating your learning plan" loader | onboarding | D | `plan-dark-creating-plan-loading` |
| Learning plan intro | `#llp-preview-intro` | D | `plan-dark-learning-plan-intro` |
| Learning path | `#learning-path` | D | `plan-dark-learning-path` |
| In-app paywall | onboarding | not saved, see Gaps | covered by `pricing-*-fullpage` |
| Home | `/home/` | D, L | `home-dark-default`, `home-light-default` |
| Koji prompt (home) | `/home/` ask pill | D | `home-dark-koji-prompt-open` |
| Course catalog | `/courses/` | D, L; tile hover | `courses-dark-default`, `courses-dark-course-tile-hover`, `courses-light-default` |
| Course page | `/courses/<slug>/` | D, L | `course-dark-default`, `course-light-default` |
| Lesson player | `/courses/<course>/<chapter>/<lesson>/` | D: idle, answer placed, correct, retry. L: idle | `lesson-dark-*`, `lesson-light-default` |
| Koji tutor chat | lesson, "Get help" | D: open, typing, board highlight | `lesson-dark-tutor-*` |
| Quit dialog | lesson, close button | D: default, danger hover | `lesson-dark-quit-confirm-*` |
| You (progress) | `/you/` | D, L; chart tooltip | `you-dark-default`, `you-dark-chart-tooltip`, `you-light-default` |
| Settings: account | `/settings/account/` | D, L; input focus plus button hover | `settings-dark-account`, `settings-dark-input-focus-button-hover`, `settings-light-account` |
| Settings: preferences | `/settings/preferences/` | D, L; switches off | `settings-dark-preferences`, `settings-dark-preferences-switches-off`, `settings-light-preferences` |
| Legacy account page | `/account/` (Django) | L only | `legacy-light-account-settings` |

#### Overlays and transient states

| Overlay | Trigger | Captured |
|---|---|---|
| Header dropdown menu | ☰ in the app header | D (item hover), L (`settings-light-header-menu-open`) |
| Keys popover | keys stat pill | D, L |
| Streak popover | streak stat pill | D, L |
| Tooltip | You page, bar chart and strength chip | D |
| Modal | quit a lesson | D |
| Koji prompt overlay | home ask pill | D |
| Tutor chat panel | lesson "Get help" | D |
| Lesson feedback (correct, retry) | Check button | D |
| Empty state | You page, "No course progress yet." | D, L (in the page captures) |
| Error state | 404 page | L; invalid input read from CSS only |
| Toast (Sonner) | never fired in this session | not captured, see Gaps |
| Command palette | none exists in the product | n/a |
| Cookie banner | OneTrust, third party | hidden during capture, not documented |

### Core components

The 2026-09 entries for components the 2026-10 specs above do not cover, rewritten in token names (`size.*`, `spacing.*`, `radius.*`, `borderWidth.*` are paths in `core`). Flat button, text input, switch, segmented control, tabs, badge, dropdown menu, tooltip, modal and card were superseded by the specs above; their 2026-09 crops stay listed under More crops.

#### Button3d colour variants

Face and lip per variant (`component.button3d.*`, both themes): primary `primary-face` over `primary-lip`; secondary `secondary-face` over `secondary-lip`; green, blue, yellow (with `yellow-text`), red, purple, orange, teal, pink, pear, papaya and mint each pair a 500-step face with its `*-lip`. Disabled is `disabled-face` with `disabled-text` and no lift; the button keeps `opacity.disabled-button3d`. The lift is `size.button3d-lift`, and pressing removes it over `duration.instant` with `easing.ease-out`. Premium is flat: `gradient.iridescent-frame` face, `text.iridescent-primary` label, `component.button3d.premium-inset` inner edge, `opacity.hover-premium` on hover.

![button3d primary, dark](components/crops/button3d-primary-dark.png)
![lesson footer: secondary and green button3d](components/crops/lesson-footer-correct-dark.png)
![lesson footer: secondary and yellow button3d](components/crops/lesson-footer-retry-dark.png)
![premium variant in the keys popover, light](components/crops/popover-keys-light.png)

#### Hue-shift pill

`data-slot=hue-shift-button`, for quick answers (No / Maybe / Yes): `size.button-height-pill` high, at least `spacing.24` wide, padding `spacing.4` `spacing.6`, `radius.full`, `typography.ui.actions.base`, fill `gradient.hue-shift-action-gray`. A hidden loading layer holds a spinner.

![hue-shift pills, dark](components/crops/hue-shift-pills-dark.png)

#### Glass button

`data-slot=glass-button` on the lesson rail: `size.icon-button` square, `radius.button`, `borderWidth.hairline` transparent edge, backdrop `blur.glass` (saturate 1.8), icon in `text.disabled`. The Koji dock joins two into a split pill whose halves round only their outer ends.

![lesson top bar with close icon button, dark](components/crops/lesson-topbar-dark.png)
![Koji dock with split glass pill, dark](components/crops/lesson-koji-dock-dark.png)

#### Chat input and ask pill

Tutor chat input: `radius.home-card`, fill `autoflip.black.100`, `borderWidth.hairline` `autoflip.black.200`, an auto-growing text area and a `size.icon-button-xs` round send button that is transparent when empty and fills with `gradient.koji-send-button` once there is text. Keycaps under it use `radius.tile` with a `borderWidth.thin` edge and a `borderWidth.default` bottom.

Ask pill on Home: the same frosted pill as the Koji prompt (`text-area-pill` above): `radius.3xl`, `borderWidth.default` `border.secondary`, `shadow.base`, `opacity.ask-pill-idle` until focused, then `blur.ask-pill` and full opacity over `duration.fast`.

![tutor input with text, dark](components/crops/tutor-input-filled-dark.png)
![ask pill, light](components/crops/home-ask-pill-light.png)
![ask pill, dark](components/crops/home-ask-pill-dark.png)

#### Search field (2026-09 catalog)

A button styled as a field that opens Koji: `size.control-lg` high, `radius.full`, `borderWidth.default` `border.primary`, a `size.icon-sm` search icon and a trailing "Ask" pill. Hover `border.hover`; focus `border.active` plus `shadow.outline`. The 2026-10 Topics page shows the same field.

![search field, light](components/crops/courses-search-light.png)
![search field, dark](components/crops/courses-search-dark.png)

#### Choice card

A card that acts as a radio (onboarding voice, subject and level): `size.choice-card-height` high, `radius.xl`, padding `spacing.8` `spacing.6` `spacing.6`, fill `gradient.hue-shift-action-gray`, label `typography.ui.actions.base` in `text.secondary`.

| State | Change |
|---|---|
| Hover | fill `bg.hover`, gradient removed |
| Selected (`data-checked`) | label `text.primary`; a hue-shift gradient (`gradient.hue-shift-color-teal-primary` or `-blue-primary`) paints over it; subject cards add `shadow.outline` |

![choice cards, default](components/crops/choice-card-states-dark.png)
![choice card hover](components/crops/choice-card-hover-dark.png)
![choice card selected](components/crops/choice-card-selected-dark.png)
![subject card selected](components/crops/subject-card-selected-dark.png)
![level option cards](components/crops/level-option-cards-dark.png)

#### Progress

`.panda-progress`: track `radius.full`, indicator `bg.green-primary`. Heights `size.progress-sm`, `size.progress-default` (onboarding, indicator width animates over `duration.normal`) and `size.progress-lg` (lesson top bar, followed by upcoming-section dots). The learning-plan intro splits the bar into three segments with `spacing.1` gaps.

![onboarding progress](components/crops/progress-onboarding-dark.png)
![segmented progress and eyebrow](components/crops/segmented-progress-eyebrow-dark.png)
![lesson top bar, light](components/crops/lesson-topbar-light.png)

#### Spinner

`data-slot=spinner`: `size.icon-sm` square, `borderWidth.default`, the top edge in currentColor and the others at 25%, spinning over `duration.spinner` linear. Seen inside hue-shift pills and the plan loader (`plan-dark-creating-plan-loading.png`).

#### Popover

`data-slot=popover-content` (keys and streak): `bg.elevated`, `radius.md`, `shadow.base`, an arrow in `bg.elevated`, and the menu's scale-and-fade over `duration.fast` with `easing.ease-in-out`.

![keys popover, dark](components/crops/popover-keys-dark.png)
![streak popover, light](components/crops/popover-streak-light.png)
![streak popover, dark](components/crops/popover-streak-dark.png)

#### More crops (2026-09)

![button3d disabled, dark](components/crops/button3d-disabled-dark.png)
![primary button hover and outline "Send verification", dark](components/crops/button-primary-hover-dark.png)
![email row with outline button, light](components/crops/settings-email-badges-light.png)
![quit dialog: danger ghost button on hover](components/crops/modal-quit-danger-hover-dark.png)
![input focus, dark](components/crops/input-focus-dark.png)
![settings inputs, light](components/crops/settings-inputs-light.png)
![settings inputs, dark](components/crops/settings-inputs-dark.png)
![preferences switches off](components/crops/preferences-switches-off-dark.png)
![switch in onboarding](components/crops/switch-onboarding-dark.png)
![segmented control and stats, light](components/crops/segmented-and-stats-light.png)
![segmented switch in preferences](components/crops/preferences-segmented-switch-dark.png)
![app header, light](components/crops/app-header-light.png)
![app header, dark](components/crops/app-header-dark.png)
![settings side menu, light](components/crops/settings-sidenav-light.png)
![settings side menu, dark](components/crops/settings-sidenav-dark.png)
![badges in the email row, dark](components/crops/settings-email-badges-dark.png)
![dropdown menu, light](components/crops/dropdown-menu-light.png)
![dropdown menu with item hover, dark](components/crops/dropdown-menu-dark.png)
![bar chart with tooltip, dark](components/crops/bar-chart-and-tooltip-dark.png)
![quit dialog, dark](components/crops/modal-quit-dark.png)
![course hero card, light](components/crops/course-hero-card-light.png)
![course hero card, dark](components/crops/course-hero-card-dark.png)
![figure card, dark](components/crops/figure-card-dark.png)
![login form, light](components/crops/login-form-light.png)
![preferences, light](components/crops/preferences-light.png)
![RECOMMENDED badge, light](components/crops/home-recommended-card-light.png)
![premium badge over a display headline](components/crops/promo-badge-headline-dark.png)

### Product components

#### Promo banner

Under the app header: min-h 48, centred `body.sm` → `body.base` 500 with an underlined link, over a 25% blue → pink → yellow wash (80% `bg.primary` on top). Visible in every signed-in page crop of the header.

#### Premium header button and stat pills

"Go Premium" (`data-slot=premium-button`): `size.premium-button` high, padding `spacing.2` `spacing.4`, `radius.full`, a `borderWidth.default` iridescent border (`gradient.iridescent-frame` via `padding-box`/`border-box`), 14/21 500 in `text.iridescent-secondary`.

Stat pills (keys, streak): 47px high (no token), `radius.button`, `borderWidth.default` `border.primary`, `typography.ui.actions.base`, `size.icon-lg` icon. They open the keys and streak popovers.

![header right side](components/crops/app-header-light.png)

#### Course tile

`data-inner-course-card`: `size.course-tile` square at 2xl (152 to 218 by breakpoint), padding 22.72%, `radius.2xl`, `borderWidth.default` `border.solid`, lifted `size.button3d-lift` over a `border.solid` lip (`shadow.tile3d`). Hover changes the border and lip to `border.hover`; transform and lip move over `duration.instant` `easing.ease-out`, the border over `duration.normal`. Grade badge top-left, "NEW" badge top-right, label below. Tiles on a shelf (`bg.secondary`, `radius.lg`) are joined by `borderWidth.default` connectors. The 2026-10 Topics cards are the 150px `card-course` spec above.

![course shelf, light](components/crops/courses-shelf-light.png)
![course tile hover, dark](components/crops/course-tile-hover-dark.png)
![public course tiles, light](components/crops/course-tiles-light.png)

#### Learning-path tile and "START HERE" tag

Onboarding path: 176x174 artwork well, radius 36, padding 36; current tiles get `gradient.hue-shift-color-blue-primary`, locked tiles are `bg.primary` with a 2px `border.secondary` and `text.disabled` label. "START HERE" is a `gray.900` pill with gradient-clipped `ui.actions.sm` text, sitting on the tile's top edge.

![learning path tiles](components/crops/learning-path-tiles-dark.png)
![fixed bottom action bar](components/crops/bottom-action-bar-dark.png)

#### Course path (level header and nodes)

Level header: 456x64 button, radius 18, over a 3D lip in the level colour (blue.700 for Level 1); presses 4px on active. Eyebrow `ui.actions.sm` in the level colour. Path nodes are 3D discs with a label to the right; the current node glows blue with Koji on top, locked nodes are grey with `text.tertiary` labels. A fixed footer card holds a full-width blue button3d.

![course path, light](components/crops/course-path-light-app.png)
![course path, dark](components/crops/course-path-dark.png)

#### Home cards

Gamification card (streak, leagues, premium footer with an iridescent "Explore" pill) and recommended course card (badge, art, title, `LEVEL 1` eyebrow, lesson rows, blue button3d).

![gamification card, light](components/crops/home-gamification-card-light.png)
![gamification card, dark](components/crops/home-gamification-card-dark.png)
![recommended card, dark](components/crops/home-recommended-card-dark.png)

#### Koji prompt

Opened from the ask pill. Cards slide out, "Hey, Learner! How can I help?" (`body.lg` 600) sits over Koji, and suggestion cards float around. The suggestion cards are drawn on a `<canvas>`, so their styling is estimated from screenshot: about 130x84, radius 12, 5% white fill, active card with a 1px blue.400 border and glow.

![Koji prompt, dark](components/crops/home-koji-prompt-dark.png)

#### Lesson frame and interactive

The lesson panel is inset `size.lesson-frame-radius-inset`, `radius.lesson-frame`, `bg.primary`, with a `borderWidth.default` border that turns to the evaluation colour (`component.lesson.frame-correct`, `frame-retry`). The interactive (`<custom-interactive>`, CoFo Semi Mono) has tappy tiles, wells, a tray, answer slots and algebra tiles; every colour is in `component.lesson.*` for both themes.

| Part | Token (resolves per theme) |
|---|---|
| Tile face / edge | `component.lesson.tile-face` / `tile-edge` |
| Stacked lip | `component.lesson.tile-stack` |
| Well / tray | `component.lesson.tile-well` / `tile-tray` |
| Empty slot | `component.lesson.tile-slot`, `borderWidth.default` dashed `tile-slot-dash` |
| Variable chip | `component.lesson.variable-chip`, border `variable-chip-border` |
| Algebra bar | `component.lesson.algebra-bar`; unit tiles `unit-tile-from` to `unit-tile-to` |

![lesson frame, light](components/crops/lesson-frame-light.png)
![interactive, light](components/crops/lesson-interactive-light.png)
![interactive with answer placed, dark](components/crops/lesson-interactive-dark.png)

#### Lesson feedback

| State | Panel | Tutor bubble | Footer |
|---|---|---|---|
| Correct | border green.700 plus `borderGlow` 1s | green.800, border green.700 | "Why?" secondary, "Continue" green button3d |
| Retry | border yellow.700, `shakeX .45s` | yellow.700 | "Get help" secondary, "Try again" yellow button3d |
| Neutral (tutor) | unchanged | `component.lesson.bubble-tutor` #172326e0, border #3e6a74 | n/a |

Tutor bubbles have radius 16 16 16 4 and padding 12 20, 16/24 500. The answer row gets a check or cross badge at its corner.

![correct badge](components/crops/lesson-answer-correct-badge-dark.png)
![retry badge](components/crops/lesson-answer-retry-badge-dark.png)

#### Koji tutor chat

A 400px column slides in from the left while the lesson panel moves right, using `--spring-smooth` over .833s. Messages: tutor (radius 16 16 16 4), user (right-aligned, `bg.tertiary`, 16 all round), and fading older messages at opacity .5. The board highlight is a pulsing `0 0 8px 0 rgba(255,255,255,.6)` glow.

![tutor chat panel](components/crops/tutor-chat-panel-dark.png)
![tutor board highlight](components/crops/tutor-highlight-dark.png)
![Koji question line](components/crops/koji-question-dark.png)

#### Weekly summary, stat cards and bar chart

Weekly summary: radius 20, 2px `border.primary`, `gradient` from `autoflip.green.100` to `autoflip.green.50`, Koji peeking bottom-left. Bar chart bars are plain divs in `bg.blue-primary`, radius 4 on top corners, a 2px bar for zero, with an accessible table underneath. Tokens: `component.chart.bar`.

Strength chip: h40, radius full, 1px border, delta pill `body.xs` 700 on `bg.green-secondary`.

![weekly summary, light](components/crops/weekly-summary-light.png)
![weekly summary, dark](components/crops/weekly-summary-dark.png)
![stat cards, dark](components/crops/segmented-and-stats-dark.png)

#### Pricing and Free vs Premium comparison

Hero: CoFo Robert 60/66 500 (`typography.display.5xl`) over `gradient.paywall-iridescent-bg-flipped`. Plan cards are a radio group (330x129), the checked one framed in `gradient.iridescent-frame` with a "MOST POPULAR" tab and Koji peeking over it (frame estimated from screenshot). The comparison table heading clips "Premium" to the iridescent gradient, and the Premium column is framed in the same gradient (about 4px, radius 16, estimated from screenshot).

![pricing hero, light](components/crops/pricing-hero-light.png)
![pricing hero, dark](components/crops/pricing-hero-dark.png)
![comparison, light](components/crops/premium-comparison-light.png)
![comparison, dark](components/crops/premium-comparison-dark.png)

#### Public header and landing CTAs

Public header: logo, nav, "Sign in" outline and "Sign up" green buttons. Landing CTAs are h60 pills, `ui.actions.lg` 20/25 500, `0 4px 7px 0 rgba(0,0,0,.05)`: green "I'm a learner" and white "I'm a parent or teacher".

![public header](components/crops/public-header-light.png)
![landing CTAs](components/crops/landing-ctas-light.png)

#### Legacy 404

The old Django UI, not part of the Panda system: h1 22/30.8 500 #333, body 15/24, "Go home" pill #f0f0f0. Kept for completeness.

![404](components/crops/notfound-legacy-light.png)

### Icons

App icons are a custom set of filled glyphs drawn at 16 (nav, menu), 24 (stats), 32 (XP) and 48 (lesson rail), all `fill="currentColor"` except the gold key. They were saved by hand from the signed-in pages into [icons/app/](icons/app), named by role and size.

| File | Where |
|---|---|
| `nav-home-16`, `nav-courses-16`, `nav-you-16` | app header tabs |
| `menu-16` | header menu trigger |
| `stat-key-24` (#f7c325), `stat-streak-bolt-24` | header stat pills |
| `xp-sparkle-32` | lesson XP counter |
| `lesson-report-flag-48`, `lesson-sound-48`, `lesson-chat-48`, `lesson-mic-18` | lesson rail and Koji dock |
| `play-16`, `close-16`, `arrow-up-16`, `arrow-down-16` | voice sample, close, strength deltas |

[icons/public/](icons/public) holds 32 SVGs pulled from the public pages by a script, named by content hash:

| Files | What | Size | Style |
|---|---|---|---|
| `91a27c79f8`, `35bbde23a3` | nav "Courses", "Next" chevron | 16, 12 | fill, currentColor black |
| `c29b0a1931`, `e950fc5c01` | course meta: lessons, exercises | 16 | fill |
| `93e06c447c`, `4fc06a14a3`, `38197ce722`, `197d4e7d65` | footer Facebook, Instagram, Twitter, LinkedIn | 20–22 | fill #999 |
| `f65ff86b03`, `9f2b7ed8f1` | Google and Apple login | 20, 17 | fill, brand colours |
| `b4ce175fcd`, `c6f4f6cb5b` | landing video pause and play | 16 | fill 30% black |
| `5ed2cd3d2e` | Koji peeking over the plan card | 40x26 | fill |
| `b7865a5607`, `6b48e24473`, `a38292d801`, `5baf88ce65`, `61a5187a65` | pricing feature list icons | 20–24 | fill with gradients |
| `13e7b9f445`, `2239dabbae`, `9d5342950c`, `f78cff109f` | pricing benefits | 32 | stroke 2.4px plus fills |
| `0cfb527962`, `f9abc0b2e7`, `c8b322698c`, `1c94002d26` | pricing tab icons | 20 | fill 60% black |
| `abefb23ce2`, `829a917deb`, `063a2fb769`, `0aa9540d2a`, `64e87ab675`, `b84ae4c3e9` | testimonial avatars (illustrated) | 28 | fill with stroke ring |

Course art, path nodes and Koji are raster or complex illustrations and are not included. All icons are Brilliant's property, kept for reference only.

