# Hume AI public site tree

Mapped from https://www.hume.ai/ on 2026-11-21, signed out, in headless Chromium, before this note was written. `https://hume.ai/` redirects to `https://www.hume.ai/`. The marketing site is a Next.js app on Vercel. The signed-in product is a different host (`app.hume.ai`) and was not entered.

The package already on main (captured 2026-11-17/18, [PR 659](https://github.com/starship-terminal/constellations/pull/659)) holds the screenshots, tokens, and component states for the pages this tree names. This file records which control opens which page, menu, dialog, or interaction. The 2026-11-21 menu probe re-read the four desktop menus and confirmed the destinations below. It did not replace those captures.

Nothing in the probe was submitted. CookieYes "Accept", the newsletter Subscribe button, the contact form, and the See a Demo email form were not submitted. Google and Apple on the log-in wall were not clicked.

## Chrome

| Control | Opens | Notes |
|---|---|---|
| Announcement bar "Introducing the Hume Audio Decisions API" | Page `/products/decision-model-api` | Link. Shot as [decision-model](screenshots/decision-model-light-default.png). |
| Logo "Hume home" | Page `/` | Link. |
| Emotion Science | Page `/emotion-science` | Top-level nav link, no menu. |
| Products (hover) | Menu | Desktop popup. Click toggles it closed. |
| Solutions (hover) | Menu | Desktop popup. |
| Benchmarks (hover) | Menu | Desktop popup. |
| Resources (hover) | Menu | Desktop popup. |
| Talk to Hume | Page `/contact-form` | Pill button in the header. |
| Open menu (phone) | Dialog | `aria-label="Open menu"`. Hidden at 1440 (`lg` breakpoint). |
| Close menu | Closes the phone menu | Same sheet. |
| See a Demo | Dialog | Feathery form: "We'll email you a personal link". Email field. Not submitted. |
| CookieYes banner | Overlay | "Your privacy choices". Close, Do Not Sell (opens `#ckyPreferenceCenter` dialog). Not accepted. |
| Cookie settings (footer) | Same CookieYes preference dialog | Not submitted. |
| Footer Subscribe | Would submit the newsletter email | Not filled, not submitted. |

## Products menu

Confirmed by hover on 2026-11-21.

| Item | Opens |
|---|---|
| Audio Decision API | Page `/products/decision-model-api` |
| Expression APIs | Page `/products/expression-apis` |
| Human Feedback API | Page `/products/human-feedback` |
| User Testing API | Page `/products/user-testing` |
| Speech Data | Page `/products/speech-data` |

VoiceEQ Platform (`/products/voiceeq-platform`) and Prism (`/products/prism`) are in the sitemap and load publicly. They are not in this menu. The package already has [voiceeq](screenshots/voiceeq-light-default.png) and [prism](screenshots/prism-light-default.png).

## Solutions menu

| Item | Opens |
|---|---|
| Model Builders | Page `/solutions/develop-voice-models` |
| Speech Generation (TTS) | Anchor `/solutions/develop-voice-models#team-tts` |
| Speech-to-Text (ASR) | Anchor `#team-asr` |
| Cascaded Voice Systems | Anchor `#team-cascaded` |
| Speech-to-Speech | Anchor `#team-sts` |
| Agent Builders | Page `/solutions/deploy-voice-agents` |
| Healthcare | Anchor `#industry-healthcare` |
| Financial Services | Anchor `#industry-financial-services` |
| Travel & Hospitality | Anchor `#industry-travel-hospitality` |
| Insurance | Anchor `#industry-insurance` |
| Customer Support | Anchor `#industry-customer-support` |
| Telecom | Anchor `#industry-telecom` |

## Benchmarks menu

| Item | Opens |
|---|---|
| RW-VEQ Bench | Page `/benchmark` |
| TTS, STS, ASR, Speech Understanding, SLM Judge, Voice Creation, Voice Cloning | Same page with `?tab=` (`tts`, `sts`, `asr`, `understanding`, `judge`, `creation`, `cloning`) |
| Technical report | External `https://arxiv.org/abs/2607.14846` (new tab). Not captured as a Hume page. |

On the benchmark page the same tabs are in-page controls. The package captures the opened tab states.

## Resources menu

| Item | Opens |
|---|---|
| API Docs | External `https://dev.hume.ai` (public docs). The package has overview, quickstart, API reference, and changelog, light and dark. |
| Blog | Page `/blog` |
| Research & Insights | Page `/emotion-science` |
| Publications | Page `/publications` |
| About | Page `/about` |
| Careers | Page `/careers` |
| All posts | Page `/blog` |
| Latest post | Page `/blog/hume-asr-entity-dataset` |

## Footer

Repeats Products, Solutions (including the industry anchors), Benchmark, Emotion Science, API Docs, Blog, Publications, About, Careers, Privacy Policy (`/privacy-policy`), Terms of Service (`/terms-of-use`). Social links leave the site: X, LinkedIn, GitHub, Discord, YouTube. Not captured.

Also linked from legal pages and already in the package's coverage notes where captured: `/api-data-usage-policy`, `/subprocessors`, `/acceptable-use-policy`. `/contact` is a public "Say Hello" page. The form that Talk to Hume opens is `/contact-form`. `/pricing` redirects to `/`.

## Homepage interactions (not navigation)

| Control | What it does |
|---|---|
| Customer Calls Next | Advances the public demo card on the page. Local. |
| Play / Pause / Stop | Controls the hero audio demo. Local. The package's playing state is this control. |
| Scene buttons (smiling on a call, smiling at phone, relaxing, headphones) | Swap the public demo image. Local. |
| Develop Model / Deploy Agent | Tabs, `aria-controls="platform-panel-0"` and `platform-panel-1`. Local. |
| Emotion Alignment, Voice naturalness, Acting / Role-fit, Reliability | Tabs into `benchmarks-panel`. Local. |

## Phone menu (390)

Open menu opens a dark sheet. Visible links: Emotion Science, Talk to Hume. Accordions: Products, Solutions, Benchmarks, Resources (same destinations as the desktop menus). See a Demo is also on the sheet and opens the same email dialog. The package has mobile shots of home, benchmark, blog, contact-form, docs overview, the demo gate, and log-in.

## Other public origins already in the package

These are not in the www header, but the 2026-11-17/18 capture reached them and stopped at the wall.

| Control or URL | Opens | Branch |
|---|---|---|
| API Docs | `https://dev.hume.ai` | Public. Theme menu paints `html.dark`. Search and Ask AI were opened and not queried. |
| Demo invitation | `https://demo.hume.ai` | Invitation gate. Not entered. |
| Explore speech-prosody | `/explore/speech-prosody-model` | Public canvas page. Internals are not DOM. |
| Not found | A missing www path | Public 404. |

## Walls (recorded, then stopped)

| URL | What it asks | Branch |
|---|---|---|
| `https://app.hume.ai/log-in` | Email and password, or "Sign in with Google", or "Sign in with Apple" | Stopped. No typing, no OAuth click. |
| `https://platform.hume.ai` | Redirects to `https://app.hume.ai/log-in` | Stopped. |
| See a Demo dialog | Email for a personal demo link | Dialog recorded as a wall. Form not submitted. The readable dialog crop is a gap: the 2026-11-21 probe saw a 0-height dialog box over a dimmed page. |
| `/contact` and `/contact-form` | Contact / talk-to-Hume forms | Pages in the package. Fields not filled. Newsletter not subscribed. |

## Sitemap not walked page by page

`/blog/` has a long post list and `/explore/` has several model pages. The index, one post, and the speech-prosody explorer that the nav or sitemap reaches are in the package. The other posts and explore model pages share those templates and are not each screenshotted.

## Theme

No theme toggle on the public marketing site. The header is a dark bar. The page background in the package is `light.bg.default` `#fdfdfc`. `prefers-color-scheme` dark does not change www painted colours. Dark evidence exists only on docs, painted by the docs Theme menu. A dark marketing theme is not invented.
