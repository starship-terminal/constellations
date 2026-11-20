# Hume AI components

The discovery list of every page and view captured, then one entry per component with crops of the real product, and the Gaps. Read from hume.ai's signed-out surfaces on 2026-11-18, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running page. Later recaptures merge into the same file, so every entry names the date its own states were read; a state a re-read missed keeps its earlier date and says so. Nothing was signed into, bought, typed, searched or submitted; the only presses were local UI toggles the product's own chrome provides — the docs header's Theme menu (the only real theme control on any surface), the home player's transport (a scripted sample-call player, a media control), the benchmark category tabs, the blog filters and the mobile 'Open menu' drawer — and nothing was sent anywhere: the contact form, newsletter Subscribe, log-in button and the docs API playground's Send were measured, never used.

**Where this was read.** Four public origins carry the system: www.hume.ai — the marketing and product pages (home, /emotion-science, the /products/* and /solutions/* pages, /benchmark, /blog, /publications, /about, /careers, /contact-form, the legal pages, the Speech Prosody explorer, the not-found page); dev.hume.ai — the Audio Decisions docs (the one surface with a theme control); demo.hume.ai — the Audio Decision Model playground's invitation gate (the playground itself is a documented boundary); and app.hume.ai/log-in — the platform's sign-in surface, never entered. EVI and Octave TTS have no public surface after the pivot to the Audio Decision Model line; demo.hume.ai/evi answers 404 — all documented as boundaries under Gaps, not captures.

The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) (48 components, 86 states). The page layouts are described in [patterns.md](patterns.md).

How to read an entry:

- A colour is its value followed by the token in [tokens.json](tokens.json) with the same value, when there is one (the `light.*` roles first — the painted surface; `dark.*` holds only the docs' painted dark). Text is written family size/line-height weight, then its colour, for example `Inter 16/26 400, #1b1918`, and is read from the first text node inside the component.
- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example "default (same: focus-visible)". When the root paints nothing, "Child layers" names the first nodes inside it that do.
- Crops are images of the component read from the live page, in [components/crops/](components/crops) (86 files, named `{component}-{state}.png`, at 2x). Screenshots are in [screenshots/](screenshots).

## Discovery list

Screenshots are named `{page}-{theme}-{state}.png` where `{theme}` is the theme the page painted at capture: www.hume.ai, demo.hume.ai and app.hume.ai paint one light theme with no control, so their shots are all `{page}-light-*`; the dev.hume.ai docs carry the one real theme control — the header Theme button's own Light / Dark / System menu repaints html.dark — so `docs-{page}-dark-*` shots were painted through it, verified by the painted surface and switched back to Light after. Desktop shots are 1440 x 900 at 1x; `-full` shots are the whole page at 1x, bounded at eight chunks with the boundary recorded in the shot's `.capture.json` sidecar; mobile shots are `mobile-{page}-{theme}-{state}.png`, 780 wide (390 at 2x). `notfound-*` is a stray-path probe — www.hume.ai's real not-found page.

| Surface | URL | Screenshots |
|---|---|---|
| Home | `www.hume.ai/` | [benchmark-tab](screenshots/home-light-benchmark-tab.png), [default](screenshots/home-light-default.png), [full](screenshots/home-light-full.png), [playing](screenshots/home-light-playing.png) |
| Emotion science | `www.hume.ai/emotion-science` | [default](screenshots/emotion-science-light-default.png), [full](screenshots/emotion-science-light-full.png) |
| Audio Decision Model | `www.hume.ai/products/decision-model-api` | [default](screenshots/decision-model-light-default.png), [full](screenshots/decision-model-light-full.png) |
| Expression APIs | `www.hume.ai/products/expression-apis` | [default](screenshots/expression-apis-light-default.png), [full](screenshots/expression-apis-light-full.png) |
| Human Feedback | `www.hume.ai/products/human-feedback` | [default](screenshots/human-feedback-light-default.png), [full](screenshots/human-feedback-light-full.png) |
| User Testing | `www.hume.ai/products/user-testing` | [default](screenshots/user-testing-light-default.png), [full](screenshots/user-testing-light-full.png) |
| Speech Data | `www.hume.ai/products/speech-data` | [default](screenshots/speech-data-light-default.png), [full](screenshots/speech-data-light-full.png) |
| Prism | `www.hume.ai/products/prism` | [default](screenshots/prism-light-default.png), [full](screenshots/prism-light-full.png) |
| VoiceEQ platform | `www.hume.ai/products/voiceeq-platform` | [default](screenshots/voiceeq-light-default.png), [full](screenshots/voiceeq-light-full.png) |
| Develop voice models | `www.hume.ai/solutions/develop-voice-models` | [default](screenshots/develop-models-light-default.png), [full](screenshots/develop-models-light-full.png) |
| Deploy voice agents | `www.hume.ai/solutions/deploy-voice-agents` | [default](screenshots/deploy-agents-light-default.png), [full](screenshots/deploy-agents-light-full.png) |
| Benchmark | `www.hume.ai/benchmark` | [category-tab](screenshots/benchmark-light-category-tab.png), [default](screenshots/benchmark-light-default.png), [full](screenshots/benchmark-light-full.png) |
| Blog index | `www.hume.ai/blog` | [category-filter](screenshots/blog-light-category-filter.png), [default](screenshots/blog-light-default.png), [full](screenshots/blog-light-full.png) |
| Benchmark post | `www.hume.ai/blog/hume-audio-decision-benchmarks` | [default](screenshots/blog-post-light-default.png), [full](screenshots/blog-post-light-full.png) |
| Publications | `www.hume.ai/publications` | [default](screenshots/publications-light-default.png), [full](screenshots/publications-light-full.png) |
| About | `www.hume.ai/about` | [default](screenshots/about-light-default.png), [full](screenshots/about-light-full.png) |
| Careers | `www.hume.ai/careers` | [default](screenshots/careers-light-default.png), [full](screenshots/careers-light-full.png) |
| Contact form | `www.hume.ai/contact-form` | [default](screenshots/contact-form-light-default.png), [field-focused](screenshots/contact-form-light-field-focused.png), [full](screenshots/contact-form-light-full.png) |
| Privacy | `www.hume.ai/privacy-policy` | [default](screenshots/privacy-policy-light-default.png), [full](screenshots/privacy-policy-light-full.png) |
| Terms | `www.hume.ai/terms-of-use` | [default](screenshots/terms-of-use-light-default.png), [full](screenshots/terms-of-use-light-full.png) |
| Speech Prosody explorer | `www.hume.ai/explore/speech-prosody-model` | [default](screenshots/explore-light-default.png), [full](screenshots/explore-light-full.png) |
| 404 page (stray-path probe) | `www.hume.ai/this-page-does-not-exist` | [default](screenshots/notfound-light-default.png), [full](screenshots/notfound-light-full.png) |
| Docs overview | `dev.hume.ai/audio-decisions/docs/overview` | [default](screenshots/docs-overview-dark-default.png), [default](screenshots/docs-overview-light-default.png), [full](screenshots/docs-overview-light-full.png) |
| Docs quickstart | `dev.hume.ai/audio-decisions/docs/quickstart/python` | [default](screenshots/docs-quickstart-dark-default.png), [default](screenshots/docs-quickstart-light-default.png), [full](screenshots/docs-quickstart-light-full.png) |
| Docs API reference | `dev.hume.ai/audio-decisions/reference/decisions/create` | [default](screenshots/docs-reference-dark-default.png), [full](screenshots/docs-reference-dark-full.png), [default](screenshots/docs-reference-light-default.png), [full](screenshots/docs-reference-light-full.png) |
| Docs changelog | `dev.hume.ai/audio-decisions/changelog` | [default](screenshots/docs-changelog-dark-default.png), [default](screenshots/docs-changelog-light-default.png), [full](screenshots/docs-changelog-light-full.png) |
| Demo invitation gate | `demo.hume.ai/decision-model/file` | [default](screenshots/demo-gate-light-default.png), [full](screenshots/demo-gate-light-full.png) |
| Log-in | `app.hume.ai/log-in` | [default](screenshots/login-light-default.png), [field-focused](screenshots/login-light-field-focused.png), [full](screenshots/login-light-full.png) |
| Home, phone | `www.hume.ai/` | [default](screenshots/mobile-home-light-default.png), [drawer](screenshots/mobile-home-light-drawer.png), [full](screenshots/mobile-home-light-full.png) |
| Benchmark, phone | `www.hume.ai/benchmark` | [default](screenshots/mobile-benchmark-light-default.png), [full](screenshots/mobile-benchmark-light-full.png) |
| Blog index, phone | `www.hume.ai/blog` | [default](screenshots/mobile-blog-light-default.png), [full](screenshots/mobile-blog-light-full.png) |
| Contact form, phone | `www.hume.ai/contact-form` | [default](screenshots/mobile-contact-form-light-default.png), [full](screenshots/mobile-contact-form-light-full.png) |
| Docs overview, phone | `dev.hume.ai/audio-decisions/docs/overview` | [default](screenshots/mobile-docs-overview-light-default.png), [drawer](screenshots/mobile-docs-overview-light-drawer.png), [full](screenshots/mobile-docs-overview-light-full.png) |
| Demo gate, phone | `demo.hume.ai/decision-model/file` | [default](screenshots/mobile-demo-gate-light-default.png) |
| Log-in, phone | `app.hume.ai/log-in` | [default](screenshots/mobile-login-light-default.png) |

### Overlays and transient states

| State | Where | How it was reached | Captured |
|---|---|---|---|
| Docs Theme menu | the dev.hume.ai header | the Theme button's own press — its Light / Dark / System menu opened; Dark pressed for the dark shots, the painted surface verified, Light restored | [docs-overview-dark-default](screenshots/docs-overview-dark-default.png), [docs-overview-light-default](screenshots/docs-overview-light-default.png) |
| Customer-call player | the home hero | the player's own Play press — the scripted sample call running; Stop ended it (a media control, not a submission) | [home-light-playing](screenshots/home-light-playing.png) |
| Benchmark category tabs | the home and /benchmark tables | a category tab's own activation — a local UI toggle | [benchmark-light-category-tab](screenshots/benchmark-light-category-tab.png) |
| Blog category filters | /blog | the 'Research' filter's own activation — a local UI toggle; 'All' restored after | [blog-light-category-filter](screenshots/blog-light-category-filter.png) |
| Contact form | www.hume.ai/contact-form | a field clicked into for the focus look — nothing typed, the form never submitted | [contact-form-light-field-focused](screenshots/contact-form-light-field-focused.png) |
| Docs Search / 'Ask AI' | the docs header | the Search dialog was opened for its UI and closed with Escape — never queried; 'Ask AI' never pressed | see icons; no query run |
| Docs API playground | dev.hume.ai/reference | the request editor measured at rest — Send never pressed (issuing a request is a network side effect) | [docs-reference-light-full](screenshots/docs-reference-light-full.png) |
| Demo playground | demo.hume.ai | gated on an invitation email link — the gate is captured, the playground was never entered | [demo-gate-light-default](screenshots/demo-gate-light-default.png) |
| Sign-in / the platform | app.hume.ai | /log-in captured at rest and with a field focused — never submitted; nothing past it was entered | [login-light-default](screenshots/login-light-default.png) |
| EVI / Octave TTS | the retired product line | no public surface exists after the pivot to the Audio Decision Model line — demo.hume.ai/evi answers 404 | boundary; see Gaps |

## Shared values

Values that apply across entries, from the measurement files.

**Focus.** 3 components were given a real keyboard focus. 3 draw an outline ring: `nav-menu-button` (1px auto #101010 `core.component.focus.outline.color`, offset 0px), `nav-cta` (1px auto #101010 `core.component.focus.outline.color`, offset 0px), `product-cta` (1px auto #101010 `core.component.focus.outline.color`, offset 1px).

**Pressed.** Forced with DevTools (`CSS.forcePseudoState` :active:hover). Nothing a real press would submit was ever pressed.

**Motion.** Transitions measured on the components, by duration.

| Duration | Easing | Property | Where |
|---|---|---|---|
| 0.15s | `cubic-bezier(0.4, 0, 0.2, 1)` | --tw-gradient-from, --tw-gradient-to, --tw-gradient-via, -webkit-backdrop-filter, backdrop-filter, background, background-color, border-color, box-shadow, color, content-visibility, display, fill, filter, opacity, outline-color, overlay, pointer-events, rotate, scale, stroke, text-decoration-color, transform, translate | benchmark-tab, blog-filter, demo-gate-cta, docs-cta, docs-search-button, docs-side-link, docs-theme-button, login-oauth and more |
| 0.15s | `ease-in-out` | border-color, box-shadow | contact-field, contact-textarea |
| 0.2s | `cubic-bezier(0.4, 0, 0.2, 1)` | background-color, transform | player-transport |
| 0.2s | `ease` | all | contact-submit |
| 0.25s | `cubic-bezier(0.4, 0, 0.2, 1)` | opacity | nav-menu-button |

**Card shapes.** Default-state values; the entries hold the states.

| Card | Size | Border | Radius | Background | Shadow | Padding |
|---|---|---|---|---|---|---|
| ["See a Demo" button](#see-a-demo-button) | 149 x 40 | - | 3.35544e+07px | #ffffff `light.docs.color.background` | rgba(0, 0, 0, 0.05) 0px 1px 2px 1px, rgba(0, 0, 0, 0.35) 0px 0px 1px 0px | 0px 24px |
| [Customer-call player](#customer-call-player) | 546 x 154 | - | - | transparent | none | 28px 16px |
| [Newsletter email input](#newsletter-email-input) | 159 x 40 | - | - | transparent | none | 0 |
| [Post preview card](#post-preview-card) | 1152 x 500 | - | 8px | transparent | none | 0 |
| [Contact form field](#contact-form-field) | 214 x 38 | - | 8px | transparent | #353535 0px 0px 0px 0px | 6px 12px |
| [Docs code block](#docs-code-block) | 704 x 410.75 | - | 0px 0px 4px 4px | transparent | none | 0 |
| [Docs "Search /" button](#docs-search--button) | 552.34 x 36 | - | 8px | transparent | #e7e5e4 0px 0px 0px 1px inset | 8px |
| [Invitation gate card](#invitation-gate-card) | 1440 x 855 | - | - | transparent | none | 0 |
| [Log-in card](#log-in-card) | 511 x 608 | - | - | transparent | none | 40px |
| [Email field](#email-field) | 421 x 30 | - | - | transparent | none | 4px |
| ["LOG IN" button](#log-in-button) | 431 x 36 | 1px solid #000000 `light.app.background.button` | 3.35544e+07px | #000000 `light.app.background.button` | none | 0px 14px |

## Components

### Site chrome

The frame every www.hume.ai page carries: the top nav (the wordmark, Emotion Science, the Products / Solutions / Benchmarks / Resources menu buttons, the solid 'See a Demo' action) and the footer with its link columns, newsletter form and social links. The surface has no theme control.

#### Site navigation bar
The top nav on www.hume.ai: the wordmark, Emotion Science, the Products / Solutions / Benchmarks / Resources menu buttons and the "See a Demo" action. Read as `site-nav` on the home page.
Read on 2026-11-17T16:34:16.757Z.

**Values (default).** size 585 x 56; background transparent; text Inter 14/20 400, transparent; icon 16 x 16, rgba(255, 255, 255, 0.65); layers span.bg-linear-to-r.from-violet-100 110.0x20.0.

Child layers that carry the look: span 110x20 image linear-gradient(to right, #ede9fe 0%, #ddd6ff 100%).

![Site navigation bar default](components/crops/site-nav-default.png)

#### Nav menu button ("Products")
A top-level nav menu button — the product/solution picker. Read as `nav-menu-button` on the home page.
States read on 2026-11-17T16:34:18.252Z (default); 2026-11-17T16:34:21.525Z (hover); 2026-11-17T16:34:23.630Z (focus-visible).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 105 x 32; padding 0px 10px; background transparent; text Inter 14/20 400, #fdfdfc `light.bg.default`; transition opacity 0.25s cubic-bezier(0.4, 0, 0.2, 1); icon 16 x 16, rgba(255, 255, 255, 0.65) |
| focus-visible | outline 1px auto #101010 `core.component.focus.outline.color`, offset 0px; layers button.group.gap-2.5 105.0x32.0 1px auto #101010 offset 0px |

![Nav menu button ("Products") default](components/crops/nav-menu-button-default.png) ![Nav menu button ("Products") hover](components/crops/nav-menu-button-hover.png) ![Nav menu button ("Products") focus-visible](components/crops/nav-menu-button-focus-visible.png)

#### "See a Demo" button
The solid primary button in the nav — measured, never followed. Read as `nav-cta` on the home page.
States read on 2026-11-17T16:34:26.072Z (default); 2026-11-17T16:34:28.939Z (hover); 2026-11-17T16:34:30.932Z (focus-visible); 2026-11-17T16:34:33.210Z (pressed).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 149 x 40; padding 0px 24px; radius 3.35544e+07px; background #ffffff `light.docs.color.background`; shadow rgba(0, 0, 0, 0.05) 0px 1px 2px 1px, rgba(0, 0, 0, 0.35) 0px 0px 1px 0px; text Inter 17/20 500, #1b1918 `light.ink.default`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1), opacity 0.15s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1), transform 0.15s cubic-bezier(0.4, 0, 0.2, 1), translate 0.15s cubic-bezier(0.4, 0, 0.2, 1), scale 0.15s cubic-bezier(0.4, 0, 0.2, 1), rotate 0.15s cubic-bezier(0.4, 0, 0.2, 1), filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), -webkit-backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), display 0.15s cubic-bezier(0.4, 0, 0.2, 1), content-visibility 0.15s cubic-bezier(0.4, 0, 0.2, 1), overlay 0.15s cubic-bezier(0.4, 0, 0.2, 1), pointer-events 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | background #f0efed `core.palette.pf0efed` |
| focus-visible | outline 1px auto #101010 `core.component.focus.outline.color`, offset 0px |

!["See a Demo" button default](components/crops/nav-cta-default.png) !["See a Demo" button hover](components/crops/nav-cta-hover.png) !["See a Demo" button focus-visible](components/crops/nav-cta-focus-visible.png) !["See a Demo" button pressed](components/crops/nav-cta-pressed.png)

#### Site footer
The page footer: link columns, the newsletter form, the social links. Read as `site-footer` on the home page.
Read on 2026-11-17T16:34:35.127Z.

**Values (default).** size 1440 x 501; background #191917; text Martina Plantijn 24/30 300, rgba(253, 253, 252, 0.65).

![Site footer default](components/crops/site-footer-default.png)

#### Social link
A footer social link ("X/Twitter") — measured, never followed. Read as `social-link` on the home page.
States read on 2026-11-17T16:34:36.961Z (default); 2026-11-17T16:34:40.569Z (hover).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 24 x 24; padding 4px; background transparent; text Inter 16/24 400, rgba(255, 255, 255, 0.5) `light.docs.white.a7`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 16 x 16, rgba(255, 255, 255, 0.5) `light.docs.white.a7` |
| hover | text Inter 16/24 400, #ffffff `light.docs.color.background`; icon 16 x 16, #ffffff `light.docs.color.background` |

![Social link default](components/crops/social-link-default.png) ![Social link hover](components/crops/social-link-hover.png)

### Home

The home surface: the 'Measure and improve real-world voice AI performance' hero, the scripted sample-call player ('Live answers from the call' — its transport was pressed for the playing state, a media control, never a submission), the audio-pipeline diagram, the benchmark table's category tabs and the newsletter form (the email field was clicked into for the focus look, never typed or submitted).

#### Hero headline
The home hero h1 — the product's largest display style. Read as `hero-headline` on the home page.
Read on 2026-11-17T16:34:45.707Z.

**Values (default).** size 669 x 133.38; background transparent; text Martina Plantijn 58/66.7 300, #ffffff `light.docs.color.background`.

![Hero headline default](components/crops/hero-headline-default.png)

#### Customer-call player
The scripted sample-call player on the home hero ("Live answers from the call"): transport, emotion labels, the audio-pipeline diagram. Read as `player-card` on the home page.
States read on 2026-11-17T16:34:53.515Z (default); 2026-11-17T16:34:57.277Z (playing).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: playing) | size 546 x 154; padding 28px 16px; background transparent; text PP Fraktion Mono 12/16 400, #6b6b66 `core.palette.p6b6b66`; layers span.grid.place-items-center 18.0x18.0 3.35544e+07px; span.rounded-full.border 12.0x12.0 #ffffff T:1px solid / R:1px solid / B:1px solid / L:1px solid 3.35544e+07px |

Child layers that carry the look: span 18x18 image conic-gradient(from 180deg, rgba(118, 53, 252, 0.35) -23%, rgba(110, 80, 170, 0.35) 17%, r radius 3.35544e+07px; span 12x12 background #ffffff `light.docs.color.background` border 1px solid radius 3.35544e+07px.

![Customer-call player default](components/crops/player-card-default.png) ![Customer-call player playing](components/crops/player-card-playing.png)

#### Player transport button
The player's Play button — pressed for the playing state, stopped after; a media control, not a submission. Read as `player-transport` on the home page.
States read on 2026-11-17T16:34:59.022Z (default); 2026-11-17T16:35:02.417Z (hover).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 30 x 30; radius 3.35544e+07px; background #ffffff `light.docs.color.background`; shadow rgba(0, 0, 0, 0.05) 0px 1px 2px 1px, rgba(0, 0, 0, 0.35) 0px 0px 1px 0px; text Inter 16/24 400, #1a1a1a; transition background-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), transform 0.2s cubic-bezier(0.4, 0, 0.2, 1); icon 12 x 12, #1a1a1a |

![Player transport button default](components/crops/player-transport-default.png) ![Player transport button hover](components/crops/player-transport-hover.png)

#### Player scenario button
A "Show …" scenario chip inside the call player — its own press swaps the scripted scene. Read as `scenario-button` on the home page.
States read on 2026-11-17T16:35:04.740Z (default); 2026-11-17T16:35:07.006Z (hover).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 148 x 461; radius 8px; background transparent; text Inter 16/24 400, #1b1918 `light.ink.default` |

![Player scenario button default](components/crops/scenario-button-default.png) ![Player scenario button hover](components/crops/scenario-button-hover.png)

#### Benchmark category tab
A benchmark category control ("Voice naturalness") — "selected" is its own activation. Read as `benchmark-tab` on the home page.
States read on 2026-11-17T16:35:09.365Z (default); 2026-11-17T16:35:11.397Z (hover); 2026-11-17T16:35:14.441Z (selected).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 155 x 32; padding 0px 14px; radius 3.35544e+07px; background transparent; text Inter 14/20 500, #6b6b66 `core.palette.p6b6b66`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | text Inter 14/20 500, #1b1918 `light.ink.default` |
| selected | background #ffffff `light.docs.color.background`; shadow rgba(0, 0, 0, 0.05) 0px 1px 2px 1px, rgba(0, 0, 0, 0.35) 0px 0px 1px 0px; text Inter 14/20 500, #1b1918 `light.ink.default` |

![Benchmark category tab default](components/crops/benchmark-tab-default.png) ![Benchmark category tab hover](components/crops/benchmark-tab-hover.png) ![Benchmark category tab selected](components/crops/benchmark-tab-selected.png)

#### Newsletter email input
The "Email address" field of the footer newsletter form. "focused" is the field clicked into — nothing is typed, the form is never submitted. Read as `newsletter-input` on the home page.
States read on 2026-11-17T16:35:16.458Z (default); 2026-11-17T16:35:22.058Z (focused).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focused) | size 159 x 40; background transparent; text Inter 14/20 400, #ffffff `light.docs.color.background`; placeholder rgba(255, 255, 255, 0.65) |

![Newsletter email input default](components/crops/newsletter-input-default.png) ![Newsletter email input focused](components/crops/newsletter-input-focused.png)

#### Newsletter "Subscribe" button
The newsletter form's submit — measured, never pressed. Read as `newsletter-button` on the home page.
States read on 2026-11-17T16:35:23.934Z (default); 2026-11-17T16:35:26.633Z (hover).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 98 x 32; padding 0px 14px; radius 3.35544e+07px; background #ffffff `light.docs.color.background`; shadow rgba(0, 0, 0, 0.05) 0px 1px 2px 1px, rgba(0, 0, 0, 0.35) 0px 0px 1px 0px; text Inter 14/20 500, #1b1918 `light.ink.default`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1), opacity 0.15s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1), transform 0.15s cubic-bezier(0.4, 0, 0.2, 1), translate 0.15s cubic-bezier(0.4, 0, 0.2, 1), scale 0.15s cubic-bezier(0.4, 0, 0.2, 1), rotate 0.15s cubic-bezier(0.4, 0, 0.2, 1), filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), -webkit-backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), display 0.15s cubic-bezier(0.4, 0, 0.2, 1), content-visibility 0.15s cubic-bezier(0.4, 0, 0.2, 1), overlay 0.15s cubic-bezier(0.4, 0, 0.2, 1), pointer-events 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | background #f0efed `core.palette.pf0efed` |

![Newsletter "Subscribe" button default](components/crops/newsletter-button-default.png) ![Newsletter "Subscribe" button hover](components/crops/newsletter-button-hover.png)

#### Section heading
A home section heading (an h2). Read as `section-heading` on the home page.
Read on 2026-11-17T16:35:27.838Z.

**Values (default).** size 242 x 73.59; background transparent; text Martina Plantijn 32/36.8 300, #1b1918 `light.ink.default`.

![Section heading default](components/crops/section-heading-default.png)

### Product pages

The product surfaces: the hero headline, the 'Contact sales' action — measured, never followed — and a feature card.

#### Product hero headline
The product page h1 — the display face at its working size. Read as `product-hero` on the Audio Decision Model page.
Read on 2026-11-17T16:36:00.854Z.

**Values (default).** size 387 x 133.38; background transparent; text Martina Plantijn 58/66.7 300, #ffffff `light.docs.color.background`.

![Product hero headline default](components/crops/product-hero-default.png)

#### Product "Contact sales" button
The product page's primary action — measured, never followed. Read as `product-cta` on the Audio Decision Model page.
States read on 2026-11-17T16:36:04.862Z (default); 2026-11-17T16:36:07.202Z (hover); 2026-11-17T16:36:12.528Z (focus-visible).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 120 x 32; padding 0px 14px; radius 3.35544e+07px; background #ffffff `light.docs.color.background`; shadow rgba(0, 0, 0, 0.05) 0px 1px 2px 1px, rgba(0, 0, 0, 0.35) 0px 0px 1px 0px; text Inter 14/20 500, #1b1918 `light.ink.default`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1), opacity 0.15s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1), transform 0.15s cubic-bezier(0.4, 0, 0.2, 1), translate 0.15s cubic-bezier(0.4, 0, 0.2, 1), scale 0.15s cubic-bezier(0.4, 0, 0.2, 1), rotate 0.15s cubic-bezier(0.4, 0, 0.2, 1), filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), -webkit-backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), display 0.15s cubic-bezier(0.4, 0, 0.2, 1), content-visibility 0.15s cubic-bezier(0.4, 0, 0.2, 1), overlay 0.15s cubic-bezier(0.4, 0, 0.2, 1), pointer-events 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | background #f0efed `core.palette.pf0efed` |
| focus-visible | outline 1px auto #101010 `core.component.focus.outline.color`, offset 1px |

![Product "Contact sales" button default](components/crops/product-cta-default.png) ![Product "Contact sales" button hover](components/crops/product-cta-hover.png) ![Product "Contact sales" button focus-visible](components/crops/product-cta-focus-visible.png)

#### Decision demo tab control
The Audio Fact / Listener Judgment / Interaction Decisions segmented tablist in the product page's decision demo. Read as `product-card` on the Audio Decision Model page.
Read on 2026-11-17T16:36:13.711Z.

**Values (default).** size 447.83 x 40; padding 4px; radius 3.35544e+07px; background #f6f4f1; text Inter 14/20 500, #1b1918 `light.ink.default`.

![Decision demo tab control default](components/crops/product-card-default.png)

### Blog

The /blog index: post preview cards, title links and the category filters — 'selected' is a filter's own activation, links were measured, never followed.

#### Post preview card
A blog index post card: title, excerpt, meta. Read as `post-card` on the blog index page.
States read on 2026-11-17T16:27:49.888Z (default); 2026-11-17T16:27:56.318Z (hover).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 1152 x 500; radius 8px; background transparent; text PP Fraktion Mono 12/16 400, #474644; icon 24 x 24, #1b1918 `light.ink.default`; layers div.flex.flex-col 576.0x500.0 #ffffff; div.w-full.h-full 40.0x40.0 #f9f9f9 transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, rgba(30, 30, 29, 0.1) 0px 0px 0px 1.67px inset, transparent 0px 0px 0px 0px 3.35544e+07px; p.@container.absolute 576.0x500.0 rgba(25, 25, 23, 0.12) |

Child layers that carry the look: div 576x500 background #ffffff `light.docs.color.background`; div 40x40 background #f9f9f9 `light.docs.accent.2` radius 3.35544e+07px shadow transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, rgba(30, 30, 29, 0.1) `core.palette.pab1123xx` 0px 0px 0px 1.67px inset, transparent 0px 0px 0px 0px; p 576x500 background rgba(25, 25, 23, 0.12).

![Post preview card default](components/crops/post-card-default.png) ![Post preview card hover](components/crops/post-card-hover.png)

#### Post title link
The post's title link inside an index card. Read as `post-title-link` on the blog index page.
States read on 2026-11-17T16:27:57.561Z (default); 2026-11-17T16:27:59.934Z (hover).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 403 x 133.38; background transparent; text Martina Plantijn 38/43.7 300, #1b1918 `light.ink.default`; layers ::after transparent 0px none 1 |

![Post title link default](components/crops/post-title-link-default.png) ![Post title link hover](components/crops/post-title-link-hover.png)

#### Blog category filter
A blog category chip ("Research"). "selected" is its own activation; the All filter restores. Read as `blog-filter` on the blog index page.
States read on 2026-11-17T16:28:01.139Z (default); 2026-11-17T16:28:04.156Z (hover); 2026-11-17T16:28:12.615Z (selected).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 94 x 32; padding 0px 14px; radius 3.35544e+07px; background transparent; text Inter 14/32 500, #6b6b66 `core.palette.p6b6b66`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | text Inter 14/32 500, #1b1918 `light.ink.default` |
| selected | background #ffffff `light.docs.color.background`; shadow rgba(0, 0, 0, 0.05) 0px 1px 2px 1px, rgba(0, 0, 0, 0.35) 0px 0px 1px 0px; text Inter 14/32 500, #1b1918 `light.ink.default` |

![Blog category filter default](components/crops/blog-filter-default.png) ![Blog category filter hover](components/crops/blog-filter-hover.png) ![Blog category filter selected](components/crops/blog-filter-selected.png)

### Prose

The blog article layer: the title h1, body paragraphs and links, inline code, fenced blocks and the benchmark result table.

#### Article title (h1)
The blog post title. Read as `prose-h1` on the benchmark post page.
Read on 2026-11-17T16:28:29.770Z.

**Values (default).** size 790 x 43.69; background transparent; text Martina Plantijn 38/43.7 300, #1b1918 `light.ink.default`.

![Article title (h1) default](components/crops/prose-h1-default.png)

#### Body paragraph
A paragraph of article prose. Read as `prose-p` on the benchmark post page.
Read on 2026-11-17T16:28:30.863Z.

**Values (default).** size 582 x 115.94; background transparent; text Inter 16/23.2 400, #474644.

![Body paragraph default](components/crops/prose-p-default.png)

#### Prose link
A body-text link inside the article. Read as `prose-link` on the benchmark post page.
States read on 2026-11-17T16:28:32.186Z (default); 2026-11-17T16:28:34.612Z (hover).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 160 x 18; padding 0px 0px 0px 14px; border L: 1px solid #1e1e1d; background transparent; text Inter 14/18 400, #1b1918 `light.ink.default`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1); layers a.-ml-px.block 160.0x18.0 L:1px solid |

Child layers that carry the look: a 160x18 border 1px solid.

![Prose link default](components/crops/prose-link-default.png) ![Prose link hover](components/crops/prose-link-hover.png)

#### Inline code
An inline code span in prose. Read as `prose-code` on the benchmark post page.

Not on the page when it was captured.

#### Code block
A fenced code block in the article. Read as `prose-pre` on the benchmark post page.

Not on the page when it was captured.

#### Prose table
A data table in the article (the benchmark post tabulates results). Read as `prose-table` on the benchmark post page.
Read on 2026-11-17T16:28:40.031Z.

**Values (default).** size 239 x 194.08; background transparent; text Inter 14/20.3 700, #474644.

![Prose table default](components/crops/prose-table-default.png)

### Contact form

The 'Talk to Hume' form: its fields were clicked into for the focus look — nothing was typed, and the submit button was never pressed.

#### Contact form field
A text field of the "Talk to Hume" form — clicked into for the focus look, never typed. Read as `contact-field` on the contact form page.
States read on 2026-11-17T16:28:52.494Z (default); 2026-11-17T16:28:54.541Z (focused).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focused) | size 214 x 38; padding 6px 12px; radius 8px; background transparent; shadow #353535 0px 0px 0px 0px; text Inter 14/normal 500, #ffffff `light.docs.color.background`; transition border-color 0.15s ease-in-out, box-shadow 0.15s ease-in-out; placeholder rgba(255, 255, 255, 0.5) `light.docs.white.a7`; layers input.css-14aefq 214.0x38.0 #353535 0px 0px 0px 0px 8px |

![Contact form field default](components/crops/contact-field-default.png) ![Contact form field focused](components/crops/contact-field-focused.png)

#### Contact form textarea
The message textarea, if the form carries one. Read as `contact-textarea` on the contact form page.
States read on 2026-11-17T16:28:55.563Z (default); 2026-11-17T16:28:56.902Z (focused).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 448 x 120; padding 8px 12px; radius 8px; background transparent; shadow #353535 0px 0px 0px 0px; text Inter 14/normal 500, transparent; transition border-color 0.15s ease-in-out, box-shadow 0.15s ease-in-out; placeholder transparent; layers textarea.css-1px7gbw 448.0x120.0 #353535 0px 0px 0px 0px 8px |
| focused | text Inter 14/normal 500, #ffffff `light.docs.color.background`; placeholder rgba(255, 255, 255, 0.5) `light.docs.white.a7`; layers textarea.css-1xfrjtn 448.0x120.0 #353535 0px 0px 0px 0px 8px |

![Contact form textarea default](components/crops/contact-textarea-default.png) ![Contact form textarea focused](components/crops/contact-textarea-focused.png)

#### Contact interest select
The interest/topic select or radio group the form carries — its menu never opened. Read as `contact-select` on the contact form page.
Read on 2026-11-17T16:28:57.763Z.

**Values (default).** size 4 x 17; background transparent; text Inter 14/normal 500, #333333 `core.palette.p333333`; placeholder #333333 `core.palette.p333333`.

![Contact interest select default](components/crops/contact-select-default.png)

#### Contact submit button
The form's submit — measured at rest and hover only, never pressed. Read as `contact-submit` on the contact form page.
States read on 2026-11-17T16:28:58.646Z (default); 2026-11-17T16:29:00.470Z (hover).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 448 x 40; padding 0px 10px; radius 30px; background #ffffff `light.docs.color.background`; shadow #353535 0px 0px 0px 0px; text Inter 17/normal 500, #1e1e1e; transition all 0.2s ease |
| hover | background #e8e8e8 `light.docs.accent.4` |

![Contact submit button default](components/crops/contact-submit-default.png) ![Contact submit button hover](components/crops/contact-submit-hover.png)

### Docs

The dev.hume.ai docs surface (a Fern docs build): the left nav, the 'Search /' field button (never queried), the header's Theme button — the only real theme control on any captured surface, whose own Light / Dark / System menu repainted html.dark for the dark states — the 'Get access' action, code blocks, the 'On this page' rail and the language tabs.

#### Docs sidebar
The left navigation rail on dev.hume.ai (a Fern docs shell). Read as `docs-nav` on the docs overview page.
States read on 2026-11-17T16:29:15.212Z (default); 2026-11-17T16:29:20.833Z (dark).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 272 x 6350.52; background transparent; text Fellix 16/24 350, #000000 `light.app.background.button` |
| dark | text Fellix 16/24 350, #ffffff `light.docs.color.background` |

![Docs sidebar default](components/crops/docs-nav-default.png) ![Docs sidebar dark](components/crops/docs-nav-dark.png)

#### Docs nav section link
A section link in the docs left nav ("Authentication"). Read as `docs-side-link` on the docs overview page.
States read on 2026-11-17T16:29:24.450Z (default); 2026-11-17T16:29:26.592Z (hover).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 222 x 20; background transparent; text Fellix 14/20 350, #000000 `light.app.background.button`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | transition none 0.15s cubic-bezier(0.4, 0, 0.2, 1) |

![Docs nav section link default](components/crops/docs-side-link-default.png) ![Docs nav section link hover](components/crops/docs-side-link-hover.png)

#### Docs "Search /" button
The header search field button — its dialog was never queried. Read as `docs-search-button` on the docs overview page.
States read on 2026-11-17T16:29:28.355Z (default); 2026-11-17T16:29:30.354Z (hover).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 552.34 x 36; padding 8px; radius 8px; background transparent; shadow #e7e5e4 0px 0px 0px 1px inset; text Fellix 14/20 500, #79716b `light.app.color.borderInputFocus`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 16 x 16, #79716b `light.app.color.borderInputFocus`; layers button.focus-visible:ring-(color:--accent).rounded-2 552.3x36.0 transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, #e7e5e4 0px 0px 0px 1px inset, transparent 0px 0px 0px 0px 8px; kbd.fern-kbd 21.0x22.0 rgba(255, 255, 255, 0.8) T:1px solid / R:1px solid / B:1px solid / L:1px solid 6px |
| hover | transition none 0.15s cubic-bezier(0.4, 0, 0.2, 1) |

![Docs "Search /" button default](components/crops/docs-search-button-default.png) ![Docs "Search /" button hover](components/crops/docs-search-button-hover.png)

#### Docs Theme button
The header's Theme button — the only real theme control on any captured surface. "opened" is its own press painting the Light / Dark / System menu. Read as `docs-theme-button` on the docs overview page.
States read on 2026-11-17T16:29:31.576Z (default); 2026-11-17T16:29:33.438Z (hover); 2026-11-17T16:29:35.570Z (opened).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 36 x 36; radius 8px; background transparent; text Fellix 14/20 500, #79716b `light.app.color.borderInputFocus`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 16 x 16, #79716b `light.app.color.borderInputFocus` |
| hover | background rgba(0, 0, 0, 0.063) `light.docs.accent.a3`; text Fellix 14/20 500, #000000 `light.app.background.button`; transition none 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 16 x 16, #000000 `light.app.background.button` |
| opened | size 118 x 96; border 1px solid #e7e5e4 `light.app.color.backgroundSelected`; background #ffffff `light.docs.color.background`; shadow rgba(0, 0, 0, 0.1) 0px 20px 25px -5px, rgba(0, 0, 0, 0.1) 0px 8px 10px -6px; text Fellix 14/20 350, #000000 `light.app.background.button`; transition none; icon 16 x 16, #000000 `light.app.background.button` |

![Docs Theme button default](components/crops/docs-theme-button-default.png) ![Docs Theme button hover](components/crops/docs-theme-button-hover.png) ![Docs Theme button opened](components/crops/docs-theme-button-opened.png)

#### Docs "Get access" button
The header's primary action — measured, never followed. Read as `docs-cta` on the docs overview page.
States read on 2026-11-17T16:29:36.601Z (default); 2026-11-17T16:29:38.572Z (hover).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 113 x 32; padding 4px 12px; radius 9999px; background transparent; shadow #e7e5e4 0px 0px 0px 1px inset; text Fellix 14/20 500, #2a2a2a `light.docs.color.body`; transition box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1), background 0.15s cubic-bezier(0.4, 0, 0.2, 1); layers a.group.cursor-pointer 113.0x32.0 transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, #e7e5e4 0px 0px 0px 1px inset, transparent 0px 0px 0px 0px 9999px |
| hover | background rgba(32, 16, 0, 0.063) `light.docs.grayscale.a3`; transition none 0.15s cubic-bezier(0.4, 0, 0.2, 1); layers none |

![Docs "Get access" button default](components/crops/docs-cta-default.png) ![Docs "Get access" button hover](components/crops/docs-cta-hover.png)

#### Docs code block
A fenced code block in the docs article — the surface the docs' --code-background and syntax palette paint. Read as `docs-code-block` on the docs overview page.
States read on 2026-11-17T16:29:40.151Z (default); 2026-11-17T16:29:44.571Z (dark).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 704 x 410.75; radius 0px 0px 4px 4px; background transparent; text Fraktion 14/22.75 350, #6f42c1 `core.palette.p6f42c1` |
| dark | text Fraktion 14/22.75 350, #ffcb6b |

![Docs code block default](components/crops/docs-code-block-default.png) ![Docs code block dark](components/crops/docs-code-block-dark.png)

#### Docs inline code
An inline code span inside the docs article. Read as `docs-inline-code` on the docs overview page.
Read on 2026-11-17T16:29:48.262Z.

**Values (default).** size 160 x 21; padding 2px 4px; radius 6px; background rgba(32, 16, 0, 0.063) `light.docs.grayscale.a3`; text Fraktion 14/24.5 400, #000000 `light.app.background.button`.

![Docs inline code default](components/crops/docs-inline-code-default.png)

#### Docs "On this page" rail
The right-rail table of contents. Read as `docs-toc` on the docs overview page.
States read on 2026-11-17T16:29:49.383Z (default); 2026-11-17T16:29:53.109Z (dark).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 272 x 390.14; background transparent; text Fraktion 12/17.14 500, #79716b `light.app.color.borderInputFocus`; icon 16 x 16, #79716b `light.app.color.borderInputFocus`; layers ul.toc-root.not-prose 236.0x216.0 L:2px solid; span.toc-track 2.0x28.0 rgba(31, 24, 0, 0.13) 1px 1px 0px 0px; span.toc-fill 2.0x28.0 #000000; span.toc-track 2.0x28.0 rgba(31, 24, 0, 0.13); span.toc-fill 2.0x28.0 #000000; span.toc-track 2.0x28.0 rgba(31, 24, 0, 0.13) |
| dark | text Fraktion 12/17.14 500, #e7e5e4 `light.app.color.backgroundSelected`; icon 16 x 16, #e7e5e4 `light.app.color.backgroundSelected`; layers ul.toc-root.not-prose 236.0x216.0 L:2px solid; span.toc-track 2.0x28.0 rgba(251, 251, 235, 0.137) 1px 1px 0px 0px; span.toc-fill 2.0x28.0 #ffffff; span.toc-track 2.0x28.0 rgba(251, 251, 235, 0.137); span.toc-fill 2.0x28.0 #ffffff; span.toc-track 2.0x28.0 rgba(251, 251, 235, 0.137) |

Child layers that carry the look: ul 236x216 border 2px solid; span 2x28 background rgba(31, 24, 0, 0.13) `light.docs.grayscale.a5` radius 1px 1px 0px 0px; span 2x28 background #000000 `light.app.background.button`.

![Docs "On this page" rail default](components/crops/docs-toc-default.png) ![Docs "On this page" rail dark](components/crops/docs-toc-dark.png)

#### Docs language tab
A code-sample language tab ("Python"). "selected" is its own activation. Read as `docs-lang-tab` on the docs overview page.
States read on 2026-11-17T16:29:56.772Z (default); 2026-11-17T16:29:58.640Z (hover); 2026-11-17T16:30:00.382Z (selected).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 58 x 34; padding 2px 10px; radius 3px; background transparent; text Fellix 12/20 500, #79716b `light.app.color.borderInputFocus` |
| hover | text Fellix 12/20 500, #000000 `light.app.background.button` |
| selected | background rgba(31, 21, 0, 0.098) `light.docs.grayscale.a4`; text Fellix 12/20 500, #000000 `light.app.background.button` |

![Docs language tab default](components/crops/docs-lang-tab-default.png) ![Docs language tab hover](components/crops/docs-lang-tab-hover.png) ![Docs language tab selected](components/crops/docs-lang-tab-selected.png)

### Demo gate

The demo.hume.ai invitation gate: 'Start from your invitation — the Audio Decision Model playground opens from the link in your invitation email'. The playground itself is a documented boundary; the gate is the honest signed-out evidence.

#### Invitation gate card
The demo.hume.ai gate: "Start from your invitation — the Audio Decision Model playground opens from the link in your invitation email". The playground itself is a documented boundary. Read as `demo-gate-card` on the invitation gate page.
Read on 2026-11-17T16:30:13.752Z.

**Values (default).** size 1440 x 855; background transparent; text fellix 24/32 350, #000000 `light.app.background.button`; icon 22.34 x 22.34, #ffffff `light.docs.color.background`; layers a.box-border.inline-flex 123.0x36.0 #000000 T:1px solid / R:1px solid / B:1px solid / L:1px solid 3.35544e+07px.

Child layers that carry the look: a 123x36 background #000000 `light.app.background.button` border 1px solid radius 3.35544e+07px.

![Invitation gate card default](components/crops/demo-gate-card-default.png)

#### Gate "Contact sales" link
The gate's only action — measured, never followed. Read as `demo-gate-cta` on the invitation gate page.
States read on 2026-11-17T16:30:14.602Z (default); 2026-11-17T16:30:16.433Z (hover).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 123 x 36; padding 0px 14px; border 1px solid #000000 `light.app.background.button`; radius 3.35544e+07px; background #000000 `light.app.background.button`; text fellix 14/20 500, #ffffff `light.docs.color.background`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 21.15 x 21.15, #ffffff `light.docs.color.background` |
| hover | background rgba(0, 0, 0, 0.9) `light.docs.black.a11`; icon 17.53 x 17.53, #ffffff `light.docs.color.background` |

![Gate "Contact sales" link default](components/crops/demo-gate-cta-default.png) ![Gate "Contact sales" link hover](components/crops/demo-gate-cta-hover.png)

### Log-in

The app.hume.ai sign-in card: the platform's public boundary page. Fields were clicked into for the focus look — nothing was typed and the LOG IN button was never pressed.

#### Log-in card
The app.hume.ai sign-in card — the platform's public boundary page; nothing past it was entered. Read as `login-card` on the log-in page.
Read on 2026-11-17T16:36:29.303Z.

**Values (default).** size 511 x 608; padding 40px; background transparent; text Fellix 20/28 500, #000000 `light.app.background.button`; layers button.box-border.inline-flex 431.0x36.0 T:1px solid / R:1px solid / B:1px solid / L:1px solid 3.35544e+07px; button.box-border.inline-flex 431.0x36.0 T:1px solid / R:1px solid / B:1px solid / L:1px solid 3.35544e+07px; hr.grow.border-border 128.0x1.0 T:1px solid; hr.grow.border-border 128.0x1.0 T:1px solid; div.[&_input]:text-inherit.h-10 431.0x40.0 #ffffff T:1px solid / R:1px solid / B:1px solid.

Child layers that carry the look: button 431x36 border 1px solid radius 3.35544e+07px; button 431x36 border 1px solid radius 3.35544e+07px; hr 128x1 border 1px solid.

![Log-in card default](components/crops/login-card-default.png)

#### Email field
The log-in Email field — clicked into for the focus look, never typed. Read as `login-email-field` on the log-in page.
States read on 2026-11-17T16:36:30.164Z (default); 2026-11-17T16:36:32.182Z (focused).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focused) | size 421 x 30; padding 4px; background transparent; text Fellix 16/24 400, #000000 `light.app.background.button`; placeholder #000000 `light.app.background.button` |

![Email field default](components/crops/login-email-field-default.png) ![Email field focused](components/crops/login-email-field-focused.png)

#### Password field
The log-in Password field — clicked into, never typed. Read as `login-password-field` on the log-in page.
States read on 2026-11-17T16:36:34.219Z (default); 2026-11-17T16:36:38.422Z (focused).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focused) | size 389 x 30; padding 4px; background transparent; text Fellix 16/24 400, #000000 `light.app.background.button`; placeholder #000000 `light.app.background.button` |

![Password field default](components/crops/login-password-field-default.png) ![Password field focused](components/crops/login-password-field-focused.png)

#### "LOG IN" button
The sign-in submit — measured at rest and hover only, never pressed (no credentials exist to submit). Read as `login-submit` on the log-in page.
States read on 2026-11-17T16:36:42.386Z (default); 2026-11-17T16:36:44.521Z (hover).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 431 x 36; padding 0px 14px; border 1px solid #000000 `light.app.background.button`; radius 3.35544e+07px; background #000000 `light.app.background.button`; text PP Fraktion Mono 14/20 400, #ffffff `light.docs.color.background`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 18.9 x 18.9, #ffffff `light.docs.color.background` |
| hover | background rgba(0, 0, 0, 0.9) `light.docs.black.a11`; icon 17.48 x 17.48, #ffffff `light.docs.color.background` |

!["LOG IN" button default](components/crops/login-submit-default.png) !["LOG IN" button hover](components/crops/login-submit-hover.png)

#### "SIGN IN WITH GOOGLE" button
An OAuth button — measured, never pressed. Read as `login-oauth` on the log-in page.
States read on 2026-11-17T16:36:45.375Z (default); 2026-11-17T16:36:47.209Z (hover).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 431 x 36; padding 0px 14px; border 1px solid rgba(0, 0, 0, 0.1) `light.docs.black.a2`; radius 3.35544e+07px; background transparent; text PP Fraktion Mono 14/20 400, #000000 `light.app.background.button`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 21.9 x 21.9, #000000 `light.app.background.button` |
| hover | background rgba(0, 0, 0, 0.05) `light.docs.black.a1`; icon 16.13 x 16.13, #000000 `light.app.background.button` |

!["SIGN IN WITH GOOGLE" button default](components/crops/login-oauth-default.png) !["SIGN IN WITH GOOGLE" button hover](components/crops/login-oauth-hover.png)

#### "Show password" toggle
The password visibility toggle — measured; its own press would reveal a (never-typed) field. Read as `login-show-password` on the log-in page.
States read on 2026-11-17T16:36:48.138Z (default); 2026-11-17T16:36:50.010Z (hover).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 32 x 30; padding 0px 8px; radius 12px; background transparent; text Fellix 16/24 400, #000000 `light.app.background.button`; icon 16 x 16, #000000 `light.app.background.button` |

!["Show password" toggle default](components/crops/login-show-password-default.png) !["Show password" toggle hover](components/crops/login-show-password-hover.png)

### Site chrome (mobile)

The 390px surface: the collapsed nav and the 'Open menu' drawer, opened and closed by its own button.

#### Mobile nav
The sticky header bar at 390px — the desktop nav links hide behind "Open menu". Read as `m-nav` on the home page.
Read on 2026-11-17T16:37:02.167Z.

**Values (default).** size 390 x 56; background #1e1e1d; text Inter 16/24 400, #ffffff `light.docs.color.background`; icon 106 x 24, #ffffff `light.docs.color.background`.

![Mobile nav default](components/crops/m-nav-default.png)

#### "Open menu" button
The mobile menu trigger. "opened" is its own press painting the drawer; Escape closes it. Read as `m-menu-button` on the home page.
States read on 2026-11-17T16:37:03.439Z (default); 2026-11-17T16:37:06.690Z (opened).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 36 x 36; background transparent; text Inter 16/24 400, rgba(255, 255, 255, 0.65); transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 20 x 20, rgba(255, 255, 255, 0.65) |
| opened | size 390 x 329; border T: 1px solid rgba(255, 255, 255, 0.05) `light.docs.white.a1`; background #1e1e1d; text Inter 16/24 400, transparent; transition none; icon 16 x 16, rgba(255, 255, 255, 0.65) |

!["Open menu" button default](components/crops/m-menu-button-default.png) !["Open menu" button opened](components/crops/m-menu-button-opened.png)

## Icons

114 distinct inline-SVG icons were collected from the live pages into [icons/](icons) by `tools/capture/icons.mjs`, indexed in [icons/INDEX.tsv](icons/INDEX.tsv): a file is named from `tools/capture/icon-names.tsv` where its geometry hash is listed, else the label or class of the control it sits in, else `icon-<hash>`; colour is kept as `currentColor` wherever it matched the text colour, so each icon recolours from CSS `color` the way it does on the site. The icons are the product's artwork — borrow the set's grammar (sizes, stroke-vs-fill, naming roles), never the artwork itself.

| Icon | Rendered sizes | View box | Style | Seen on | Next to |
|---|---|---|---|---|---|
| [icon-4f0f75d5](icons/icon-4f0f75d5.svg) | 11x11 12x12 16x16 | 0 0 24 24 | stroke | home; decision-model; emotion-science; benchmark; blog; blog-post; about; docs; docs-reference; docs search dialog; docs theme menu; docs dark; mobile | NEW Introducing the Hume Audio Decisions / Next / Next: For  |
| [discord](icons/discord.svg) | 16x16 | 0 0 256 199 | fill | home; decision-model; emotion-science; benchmark; blog; blog-post; about; mobile | Discord |
| [x-twitter](icons/x-twitter.svg) | 12x12 16x16 | 0 0 24 24 | fill | home; decision-model; emotion-science; benchmark; blog; blog-post; about; mobile | X/Twitter / Share on X |
| [github](icons/github.svg) | 16x16 | 0 0 1024 1024 | fill | home; decision-model; emotion-science; benchmark; blog; blog-post; about; mobile | GitHub |
| [youtube](icons/youtube.svg) | 16x16 | 0 0 24 24 | fill | home; decision-model; emotion-science; benchmark; blog; blog-post; about; mobile | YouTube |
| [linkedin](icons/linkedin.svg) | 16x16 | 0 0 256 256 | fill | home; decision-model; emotion-science; benchmark; blog; blog-post; about; mobile | LinkedIn |
| [products](icons/products.svg) | 16x16 | 0 0 24 24 | stroke | home; decision-model; emotion-science; benchmark; blog; blog-post; about | Products / Solutions / Benchmarks |
| [copy-page](icons/copy-page.svg) | 16x16 | 0 0 24 24 | stroke | docs; docs-reference; docs search dialog; docs theme menu; docs dark | Copy page / Copy to clipboard |
| [api-reference](icons/api-reference.svg) | 14x14 | 0 0 384 512 | fill | docs; docs-reference; docs search dialog; docs theme menu; docs dark | API Reference |
| [search](icons/search.svg) | 16x16 | 0 0 24 24 | stroke | docs; docs-reference; docs search dialog; docs theme menu; docs dark | Search |
| [support](icons/support.svg) | 14x14 | 0 0 512 512 | fill | docs; docs-reference; docs search dialog; docs theme menu; docs dark | Support |
| [icon-8af3f8cd](icons/icon-8af3f8cd.svg) | 12x12 16x16 | 0 0 24 24 | stroke | home; emotion-science; benchmark; blog-post; mobile | Learn more about User Testing API / Learn more about Express |
| [yes](icons/yes.svg) | 16x16 | 0 0 24 24 | stroke | docs; docs-reference; docs search dialog; docs theme menu; docs dark | Yes |
| [expand-code](icons/expand-code.svg) | 16x16 | 0 0 24 24 | stroke | docs; docs-reference; docs search dialog; docs theme menu; docs dark | Expand code |
| [no](icons/no.svg) | 16x16 | 0 0 24 24 | stroke | docs; docs-reference; docs search dialog; docs theme menu; docs dark | No |
| [changelog](icons/changelog.svg) | 14x14 | 0 0 512 512 | fill | docs; docs-reference; docs search dialog; docs theme menu; docs dark | Changelog |
| [cookbooks](icons/cookbooks.svg) | 14x14 | 0 0 448 512 | fill | docs; docs-reference; docs search dialog; docs theme menu; docs dark | Cookbooks |
| [audio-decisions](icons/audio-decisions.svg) | 12x12 16x16 | 0 0 24 24 | stroke | docs; docs-reference; docs search dialog; docs theme menu; docs dark | Audio Decisions / Voice agent QA / cURL |
| [documentation](icons/documentation.svg) | 14x14 | 0 0 512 512 | fill | docs; docs-reference; docs search dialog; docs theme menu; docs dark | Documentation |
| [icon-09329f69](icons/icon-09329f69.svg) | 32x32 | 0 0 512 512 | fill | docs; docs search dialog; docs theme menu; docs dark | Interpreting answers Learn how to read e |
| [icon-302c2bf8](icons/icon-302c2bf8.svg) | 32x32 | 0 0 512 512 | fill | docs; docs search dialog; docs theme menu; docs dark | Introducing the Audio Decisions API Why  |
| [scroll-to-top](icons/scroll-to-top.svg) | 16x16 | 0 0 24 24 | stroke | docs; docs search dialog; docs theme menu; docs dark | Scroll to top |
| [icon-546ab3a4](icons/icon-546ab3a4.svg) | 32x32 | 0 0 576 512 | fill | docs; docs search dialog; docs theme menu; docs dark | Runs Look up the status and request of p |
| [terms-of-use](icons/terms-of-use.svg) | 16x16 | 0 0 24 24 | stroke | docs; docs search dialog; docs theme menu; docs dark | Terms of use / Privacy policy / Status |
| [icon-5a311be7](icons/icon-5a311be7.svg) | 32x32 | 0 0 512 512 | fill | docs; docs search dialog; docs theme menu; docs dark | Primitives Learn what each question type |
| [icon-5d184e9a](icons/icon-5d184e9a.svg) | 32x32 | 0 0 448 512 | fill | docs; docs search dialog; docs theme menu; docs dark | TypeScript quickstart Act on answers in  |
| [icon-7341d5c6](icons/icon-7341d5c6.svg) | 32x32 | 0 0 384 512 | fill | docs; docs search dialog; docs theme menu; docs dark | API reference Every parameter and field  |
| [icon-766c46b6](icons/icon-766c46b6.svg) | 32x32 | 0 0 448 512 | fill | docs; docs search dialog; docs theme menu; docs dark | Python quickstart Score text-to-speech o |
| [built-with](icons/built-with-aff1e95e.svg) | 52x14 | 0 0 604 164 | fill | docs; docs-reference; docs search dialog; docs theme menu | Built with |
| [icon-b79621ff](icons/icon-b79621ff.svg) | 32x32 | 0 0 448 512 | fill | docs; docs search dialog; docs theme menu; docs dark | Build with a coding agent Point your cod |
| [ask-ai](icons/ask-ai-bcf801d6.svg) | 17x17 | 0 0 512 512 | fill | docs; docs-reference; docs search dialog; docs theme menu | Ask AI |
| [report-incorrect-code](icons/report-incorrect-code.svg) | 16x16 | 0 0 24 24 | stroke | docs; docs search dialog; docs theme menu; docs dark | Report incorrect code |
| [icon-e09864c9](icons/icon-e09864c9.svg) | 32x32 | 0 0 384 512 | fill | docs; docs search dialog; docs theme menu; docs dark | Use cases Learn which decisions the API  |
| [icon-e720274b](icons/icon-e720274b.svg) | 32x32 | 0 0 512 512 | fill | docs; docs search dialog; docs theme menu; docs dark | Writing questions Learn how to write que |
| [theme](icons/theme.svg) | 16x16 | 0 0 24 24 | stroke | docs; docs-reference; docs search dialog; docs theme menu | Theme / System |
| [add-question](icons/add-question-4ee09870.svg) | 11x11 12x12 16x16 | 0 0 24 24 | stroke | home; decision-model; mobile | Add question |
| [icon-70e6626c](icons/icon-70e6626c.svg) | 16x16 | 0 0 24 24 | stroke | emotion-science; benchmark; about | Read the study (opens in a new tab) / Explore the research ( |
| [play](icons/play.svg) | 10x10 11x11 12x12 14x14 18x18 | 0 0 24 24 | fill | home; decision-model; mobile | Play / Watch Video |
| [dark](icons/dark.svg) | 16x16 | 0 0 24 24 | stroke | docs theme menu; docs dark | Dark / Theme |
| [icon-15b0e8af](icons/icon-15b0e8af.svg) | 11x11 12x12 | 0 0 24 24 | fill | home; mobile |  |
| [ask-ai](icons/ask-ai-1b87bb98.svg) | 16x16 | 0 0 512 512 | fill | docs-reference; docs search dialog | Ask AI |
| [pick-one](icons/pick-one.svg) | 12x12 | 0 0 24 24 | stroke | home; mobile | Pick One / Yes/No / Scale |
| [add-question](icons/add-question-3979c7e1.svg) | 16x16 | 0 0 24 24 | stroke | home; mobile | Add question |
| [icon-42c79811](icons/icon-42c79811.svg) | 12x12 20x20 28x28 | 0 0 24 24 | stroke | decision-model; docs-reference | What is Hume’s audio decision model? / What is a decision mo |
| [icon-43ee084b](icons/icon-43ee084b.svg) | 10x10 14x14 18x18 | 0 0 14 14 | fill | home; mobile | Hume Audio Decision Model |
| [stop](icons/stop-70d7f08a.svg) | 11x11 12x12 | 0 0 24 24 | fill | home; mobile | Stop |
| [pause](icons/pause-91aa4dca.svg) | 11x11 12x12 | 0 0 24 24 | fill | home; mobile | Pause |
| [icon-d171201e](icons/icon-d171201e.svg) | 41x41 48x48 55x55 56x56 59x59 | 0 0 56 56 | stroke | home; mobile |  |
| [copy-link](icons/copy-link.svg) | 14x14 | 0 0 24 24 | stroke | blog-post | Copy link |
| [system](icons/system.svg) | 16x16 | 0 0 24 24 | stroke | docs theme menu | System |
| [scenarios](icons/scenarios-103e567a.svg) | 17x17 | 0 0 24 24 | stroke | home | Scenarios |
| [model](icons/model.svg) | 12x12 | 0 0 24 24 | stroke | blog-post | Model / AES / NISQA |
| [icon-199377de](icons/icon-199377de.svg) | 19x14 | 0 0 22.5 15 | fill | decision-model |  |
| [overall](icons/overall.svg) | 12x12 | 0 0 24 24 | stroke | blog-post | Overall |
| [svg-size-3-75](icons/svg-size-3-75-19d4b6ad.svg) | 15x15 | 0 0 24 24 | stroke | home |  |
| [add-question](icons/add-question-1ea3b0ce.svg) | 10x10 | 0 0 24 24 | stroke | decision-model | Add Question |
| [icon-2a386c64](icons/icon-2a386c64.svg) | 28x28 | 0 0 24 24 | stroke | benchmark | Your criteria Tailored to the modality a |
| [sign-in-with-google](icons/sign-in-with-google-2a6d6a3b.svg) | 16x16 | -24 0 310 262 | fill | login | SIGN IN WITH GOOGLE |
| [icon-2da37a5e](icons/icon-2da37a5e.svg) | 12x12 | 0 0 24 24 | fill | home |  |
| [icon-2e1a848b](icons/icon-2e1a848b.svg) | 24x24 | 0 0 24.5 25 | fill | blog |  |
| [hide-2-properties](icons/hide-2-properties.svg) | 12x12 | 0 0 24 24 | stroke | docs-reference | Hide 2 properties / Hide 4 variants / Hide 1 property |
| [share-on-bluesky](icons/share-on-bluesky.svg) | 14x14 | 0 0 24 24 | fill | blog-post | Share on Bluesky |
| [contact-sales](icons/contact-sales.svg) | 20x20 22x22 | 0 0 256 256 | fill | demo-gate | Contact sales |
| [icon-40305905](icons/icon-40305905.svg) | 16x16 | 0 0 24 24 | stroke | decision-model | Stop Telehealth consultation 0:08 / 0:56 / Stop Telehealth c |
| [decisions](icons/decisions.svg) | 16x16 | 0 0 24 24 | stroke | docs-reference | DECISIONS / RUNS |
| [02-listening-rubrics](icons/02-listening-rubrics.svg) | 16x16 | 0 0 24 24 | stroke | emotion-science | 02 Listening rubrics / 03 Scoring methods / TTS 3.1 TTS 4.0 |
| [start](icons/start.svg) | 14x14 | 0 0 24 24 | stroke | home | Start |
| [scenarios](icons/scenarios-5001a3b3.svg) | 17x17 | 0 0 24 24 | stroke | home | Scenarios |
| [icon-53f21a8e](icons/icon-53f21a8e.svg) | 28x28 | 0 0 24 24 | stroke | benchmark | Checkpoint comparison Internal checkpoin |
| [icon-57022824](icons/icon-57022824.svg) | 10x10 | 0 0 24 24 | stroke | home |  |
| [icon-58c2303a](icons/icon-58c2303a.svg) | 19x14 | 0 0 513 342 | fill | decision-model |  |
| [svg-size-3-75](icons/svg-size-3-75-5ac670b7.svg) | 15x15 | 0 0 24 24 | stroke | home |  |
| [yes-no](icons/yes-no.svg) | 12x12 | 0 0 24 24 | stroke | decision-model | Yes/No / Pick One / Scale |
| [microphone](icons/microphone.svg) | 16x16 | 0 0 24 24 | stroke | decision-model | Microphone |
| [4-7-avg](icons/4-7-avg.svg) | 10x10 | 0 0 24 24 | fill | home | 4.7 avg |
| [svg-size-3-75](icons/svg-size-3-75-62d17fe0.svg) | 15x15 | 0 0 24 24 | stroke | home |  |
| [icon-677dc649](icons/icon-677dc649.svg) | 17x17 19x19 20x20 21x21 22x22 | 0 0 24 24 | stroke | decision-model |  |
| [ask-ai](icons/ask-ai-6831a086.svg) | 17x17 | 0 0 512 512 | fill | docs dark | Ask AI |
| [show-password](icons/show-password.svg) | 16x16 | 0 0 24 24 | stroke | login | Show password |
| [original-map](icons/original-map.svg) | 14x14 | 0 0 24 24 | stroke | emotion-science | ORIGINAL MAP |
| [light](icons/light.svg) | 16x16 | 0 0 24 24 | stroke | docs theme menu | Light |
| [icon-759ec148](icons/icon-759ec148.svg) | 28x28 | 0 0 24 24 | stroke | benchmark | Reusable regression A held-out suite to  |
| [pause](icons/pause-7979e1f8.svg) | 12x12 | 0 0 12 12 | fill | blog-post | Pause |
| [open-menu](icons/open-menu.svg) | 20x20 | 0 0 24 24 | stroke | mobile | Open menu |
| [sign-in-with-apple](icons/sign-in-with-apple.svg) | 16x16 | 0 0 209 257 | fill | login | SIGN IN WITH APPLE |
| [sign-in-with-google](icons/sign-in-with-google-7ec67e85.svg) | 20x20 21x21 22x22 23x23 | 0 0 256 256 | fill | login | SIGN IN WITH GOOGLE / SIGN IN WITH APPLE / LOGGING IN... LOG |
| [sort-newest](icons/sort-newest.svg) | 16x16 | 0 0 24 24 | stroke | blog | Sort: Newest |
| [sample-call](icons/sample-call.svg) | 16x16 | 0 0 24 24 | stroke | decision-model | Sample call |
| [stop](icons/stop-93d8405b.svg) | 16x16 | 0 0 24 24 | stroke | decision-model | Stop |
| [built-with](icons/built-with-961810c6.svg) | 52x14 | 0 0 604 164 | fill | docs dark | Built with |
| [icon-96bf2687](icons/icon-96bf2687.svg) | 28x28 | 0 0 24 24 | stroke | benchmark | Your results, private Condition-level an |
| [share-on-linkedin](icons/share-on-linkedin.svg) | 14x14 | 0 0 24 24 | fill | blog-post | Share on LinkedIn |
| [svg-size-3-75](icons/svg-size-3-75-a3c44221.svg) | 15x15 | 0 0 24 24 | stroke | home |  |
| [icon-a4bd5bc6](icons/icon-a4bd5bc6.svg) | 24x24 | 0 0 24 24 | stroke | benchmark | 02 Automated graders Defined criteria At |
| [svg-size-3-75](icons/svg-size-3-75-ac71e1b2.svg) | 15x15 | 0 0 24 24 | stroke | home |  |
| [icon-afb1a00c](icons/icon-afb1a00c.svg) | 16x16 | 0 0 24 24 | stroke | blog |  |
| [scenarios](icons/scenarios-b41738f6.svg) | 16x16 | 0 0 24 24 | stroke | home | Scenarios |
| [close-search](icons/close-search.svg) | 16x16 | 0 0 24 24 | stroke | docs search dialog | Close search |
| [icon-bb6b5afb](icons/icon-bb6b5afb.svg) | 20x16 | 0 85.333 512 341.333 | fill | decision-model |  |
| [icon-c4afaf7a](icons/icon-c4afaf7a.svg) | 21x17 | 0 0 513 342 | fill | decision-model |  |
| [try-it](icons/try-it.svg) | 12x12 | 0 0 24 24 | fill | docs-reference | Try it |
| [curl](icons/curl.svg) | 16x16 | 0 0 512 512 | fill | docs-reference | cURL |
| [next-page](icons/next-page.svg) | 16x16 | 0 0 24 24 | stroke | blog | Next page |
| [upload-files](icons/upload-files.svg) | 16x16 | 0 0 24 24 | stroke | decision-model | Upload files |
| [icon-d5ea7cec](icons/icon-d5ea7cec.svg) | 24x24 | 0 0 24 24 | stroke | benchmark | 03 Human raters Naturalness Expression C |
| [icon-d8430450](icons/icon-d8430450.svg) | 21x18 | 0 0 513 342 | fill | decision-model |  |
| [icon-dad70c93](icons/icon-dad70c93.svg) | 20x16 | 0 0 513 342 | fill | decision-model |  |
| [show-property-path](icons/show-property-path.svg) | 14x14 | 0 0 24 24 | stroke | docs-reference | Show property path |
| [icon-e93f695c](icons/icon-e93f695c.svg) | 28x28 | 0 0 24 24 | stroke | benchmark | Your system Model, agent, endpoint, or c |
| [icon-f6d31953](icons/icon-f6d31953.svg) | 28x28 | 0 0 24 24 | stroke | benchmark | Your conditions Scenarios, speakers, and |
| [icon-fb137c44](icons/icon-fb137c44.svg) | 24x24 | 0 0 24 24 | stroke | benchmark | 01 Objective measures Accuracy Timing Ac |
| [share-on-threads](icons/share-on-threads.svg) | 14x14 | 0 0 192 192 | fill | blog-post | Share on Threads |
| [icon-fd4c7d16](icons/icon-fd4c7d16.svg) | 24x24 | 0 0 24 24 | stroke | decision-model | Searching for frustrated customer calls. / Sear |
| [blogs](icons/blogs.svg) | 12x12 | 0 0 24 24 | stroke | blog-post | Blogs |

## Gaps

### The blocked product surfaces

The signed-in product was never entered: **app.hume.ai past /log-in** — the platform's sign-in card is captured at rest and with a field focused, but no account exists and nothing was typed, submitted or entered. The **demo.hume.ai playground** is gated on an invitation email link — the gate page is captured; the Audio Decision Model playground behind it was never opened. The **EVI / Octave TTS line** has no public surface after the pivot to the Audio Decision Model / VoiceEQ line — demo.hume.ai/evi answers 404, so no EVI demo state exists to capture (the old EVI microphone-permission boundary is moot). The docs' **'Ask AI' and Search** were never queried, and the API reference's **Send** was never pressed — issuing a request is a network side effect. All are documented as boundaries, never faked.

### Pages

- **Sign-in / account surfaces** — the platform dashboard, API keys, projects and billing behind app.hume.ai/log-in: the product's own boundary, never entered.
- **demo.hume.ai playground** — gated on an invitation email link; the 'Start from your invitation' gate is the honest signed-out evidence.
- **EVI / Octave TTS** — no public surface exists post-pivot; demo.hume.ai/evi answers 404.
- **The /explore/speech-prosody-model canvas** — the explorer renders its visualisation into a canvas; the painted bitmap is captured in the screenshots but its internal structure is not a DOM and no DOM values are invented for it.
- **External links** — social links, the publications' arXiv/journal PDFs and the careers ATS links lead off-site; external surfaces, out of scope.
- **Long pages** — every `-full` shot is bounded at eight chunks; any boundary the bound hit is recorded in the shot's `.capture.json` sidecar and the capture log.

### States

- **Pressed** was forced with DevTools on the controls that carry it, so a state a script adds on mousedown (if any) is missing.
- **The docs Search and 'Ask AI' were never queried** — the dialog was opened for its UI and closed with Escape; no query was run, so result lists are uncaptured.
- **The contact form, newsletter and log-in fields were never typed into or submitted** — clicked into for the focus look only.
- **Send on the docs API playground was never pressed** — issuing a request is a network side effect, so the request editor's resting surface is the honest signed-out evidence.
- **The home player's Play was pressed** — it drives a scripted sample call (a media control, not a submission); Stop ended it after the playing state was captured.

### Themes

www.hume.ai, demo.hume.ai and app.hume.ai paint a single light theme and have no theme control at all — a `.dark` class and a dark colour-scheme emulation both leave the painted surface unchanged, and no dark marketing shots or tokens are invented. The dev.hume.ai docs carry the one real theme control: the header Theme button's own Light / Dark / System menu repaints `html.dark`, verified by the painted surface (html class, color-scheme, the computed background), and Light was restored afterwards. The `dark` token set holds only the docs' painted dark — `light.docs.*` the same declarations under html.light.

### Fonts

- **The brand faces are proprietary and never shipped**: 'Martina Plantijn' (the www display serif), 'PP Fraktion Mono'/'Fraktion' (the code faces), 'Fellix' (the docs/app body face) and 'M PLUS 1' (Japanese) are licensed assets, declared and measured by name only. 'Inter' is open-licensed. The style guide falls back to system faces.

### Screenshots

- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files.
- The rendered brand strings on the captured pages (the wordmark and copy) are the product's published content.
- Public author names, handles, headshots and company logos on the about, careers, blog and testimonial surfaces are published content and are kept; nothing private was captured.

### Content left out

- Article copy, publication text and testimonial quotes are the product's published content; only frames and components were measured.
