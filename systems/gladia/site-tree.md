# Gladia public site tree

Walked on 2026-11-21 in headless Chromium, signed out. Start was `https://www.gladia.io/` (HTTP 200, title "Gladia | AI Audio Infrastructure for Voice Products"). No Cloudflare, DataDome, or Akamai block. The Axeptio cookie card ("We value your privacy") was hidden, never accepted or rejected. No form was typed into or submitted. Google was not clicked.

Measured viewports: desktop `innerWidth` 1440, `innerHeight` 900, `devicePixelRatio` 1. Phone `innerWidth` 390, `innerHeight` 844, `devicePixelRatio` 2.

Marketing pages share one header and one footer unless a row says otherwise. `:root` paints dark (`--bg-primary` `#000000`). `body.light-mode` paints light. The marketing header has no theme switch and no locale switch.

## Header (desktop, 1440)

The floating `nav.navbar` inside `header.site-nav`. Logo "Gladia" goes to `/`.

| Control | What it opens |
|---|---|
| Product (`button[data-menu="product"]`, `aria-controls="mega-panel-product"`) | Hover or click sets `aria-expanded="true"` and shows the Product panel. Escape closes it. Links below. |
| Solutions (`data-menu="solutions"`) | Same, panel `mega-panel-solutions`. |
| Pricing (`a`, `/pricing`) | Page `https://www.gladia.io/pricing`. |
| Developers (`data-menu="developers"`) | Panel `mega-panel-developers`. |
| Resources (`data-menu="resources"`) | Panel `mega-panel-resources`. |
| Company (`data-menu="company"`) | Panel `mega-panel-company`. |
| Request a demo | Page `/demo-request`. |
| Sign up | Login wall `https://app.gladia.io/signup`. Stopped that branch. Empty form photographed. |

### Product panel

Opened. Eleven links.

| Link | Destination |
|---|---|
| Speech-to-text API | `/product/speech-to-text-api` |
| Real-time speech-to-text | `/product/speech-to-text-api/real-time` |
| Async speech-to-text | `/product/speech-to-text-api/async` |
| Audio intelligence | `/product/audio-intelligence` |
| GladiaFlow | `/gladiaflow` |
| Compare STT | `/speech-to-text-api-comparison` |
| STT API Benchmarks | `/competitors/benchmarks` |
| Gladia vs Deepgram | `/competitors/gladia-vs-deepgram` |
| Gladia vs AssemblyAI | `/competitors/gladia-vs-assemblyai` |
| Gladia vs ElevenLabs | `/competitors/gladia-vs-elevenlabs` |
| Startup Studio | `/start-up-studio` |

### Solutions panel

Opened. Six links.

| Link | Destination |
|---|---|
| Meeting assistants | `/use-cases/meeting-assistants` |
| CCaaS | `/use-cases/ccaas` |
| Voice agents | `/use-cases/voice-agents` |
| Content & media | `/use-cases/media` |
| Voices that shape our story | `/testimonials` |
| Blind test: compare STT models | `/speech-to-text-api-comparison` |

### Developers panel

Opened. Nine links.

| Link | Destination |
|---|---|
| Playground | `https://app.gladia.io/signup` (signup wall; not entered) |
| Documentation | `https://docs.gladia.io/` which redirects to `/chapters/introduction` |
| Changelog | `/changelog` |
| Status | `https://status.gladia.io/` (HTTP 200, "Gladia Status") |
| Integration | `https://docs.gladia.io/chapters/integrations` |
| Discord | `https://discord.com/invite/UUd79ckzz9` (external; not followed) |
| GitHub | `https://github.com/gladiaio` (external; not followed) |
| Build with us on GitHub | `https://github.com/gladiaio` |
| Blind test card | `/speech-to-text-api-comparison` |

### Resources panel

Opened. Eleven links.

| Link | Destination |
|---|---|
| Blog | `/blog` |
| Library | `/library` |
| Benchmark Checker | `/benchmark-reliability-checker` |
| TCO Calculator | `/build-vs-buy-whisper` |
| Compliance Hub | `/compliance-hub` |
| AI note-taker guide | `/content/ai-note-takers-guide` |
| Contact center guide | `/content/ccaas-async-speech-ai-guide` |
| Startup Studio | `/start-up-studio` |
| Creator Program | `/creator-program` |
| 2026 Meeting Assistant Market Map | `/meeting-assistant-market-map` |
| Blind test card | `/speech-to-text-api-comparison` |

### Company panel

Opened. Seven links.

| Link | Destination |
|---|---|
| About us | `/about-us` |
| Careers | `https://www.welcometothejungle.com/fr/companies/gladia` (external; not followed) |
| Press | A Google Drive folder (external; not followed) |
| Partners | `/partners` |
| Testimonials | `/testimonials` |
| Compliance Hub | `/compliance-hub` |
| Blind test card | `/speech-to-text-api-comparison` |

## Header (phone, 390)

`button[aria-label="Open menu"]` opens the mobile nav (`aria-expanded="true"`, body class `mobile-nav-open`). `Close menu` closes it. The drawer repeats Product, Solutions, Pricing, Developers, Resources, Company, Request a demo, and Sign up. Product inside the drawer starts expanded and lists Speech-to-text API, Real-time speech-to-text, Async speech-to-text, Audio intelligence, GladiaFlow, and Compare STT. Sign up still goes to the signup wall.

## Announcement bar

`#announceBar`, label "2026 Meeting Assistant Market Map I Fall Edition". "See the report" goes to `/meeting-assistant-market-map`. "Close announcement" is a local dismiss. Not a theme or locale switch.

## Home page controls

URL `https://www.gladia.io/`. H1 "Turn audio into your most valuable dataset". Body class `homepage-v3`. Background `rgb(0, 0, 0)`.

| Control | What it does |
|---|---|
| Get started | A hero control. Its `href` was empty in the DOM read, so it was not followed. |
| Expand (five buttons, `aria-label="Expand"`) | Present. The first click did not set `aria-expanded` on a named control. Not a page change. |
| Show all features | Click set `aria-expanded` from `false` to `true`. A local disclosure on the home feature list. |
| Live hours counter | Display only. Not a control. |
| No carousel | No `carousel`, `swiper`, or next/previous control on the home page. |

## Footer

Present on the marketing pages. Groups and where each link goes:

Product: Real-time STT `/product/speech-to-text-api/real-time`, Batch STT `/product/speech-to-text-api/async`, Audio Intelligence `/product/audio-intelligence`, Pricing `/pricing`.

Solutions: Meeting assistants, CCaaS, Voice agents, Content & media (the four `/use-cases/*` pages).

Resources: Blog, Library, AI note-takers guide, Contact center guide, API benchmarks, Benchmark Checker, Whisper TCO calculator, Compliance hub, Meeting assistant map, Gladia vs AssemblyAI, Gladia vs Deepgram, Gladia vs ElevenLabs.

Developers: Documentation `https://docs.gladia.io/`, Playground `https://app.gladia.io/` (redirects to the sign-in wall), Status `https://status.gladia.io/`, Discord (external).

Legal: Privacy notice `/privacy-notice`, Legal notice `/legal-notice`, Data processing agreement `/data-process-agreement`, Terms of use Gladia Inc. `/general-terms-of-use-gladia-inc`, Terms of use Gladia SAS `/general-terms-of-use-gladia-sas`, Terms & conditions Gladia Inc. `/terms-conditions-gladia-inc`, Terms & conditions Gladia SAS `/terms-conditions`, Security `/security`, Bug bounty `/bug-bounty`. GDPR, HIPAA, SOC Type 2, and ISO 27001 badges all go to `/compliance-hub`.

No "Cookie preferences" control was in the footer DOM on this walk. The Axeptio card mentioned one; it was not opened.

## Pages opened from the home tree

Each row is a page this walk loaded. Status 200 unless noted. "Stopped" means the URL is a login or signup wall.

| Page | URL | What else is on it |
|---|---|---|
| Pricing | `/pricing` | Async (`aria-pressed` true at rest) and Real-time toggle. Clicking Real-time set `aria-pressed` true. Restored to Async. "See more" disclosure (`aria-expanded` false). Twelve FAQ buttons, all `aria-expanded="false"` at rest. Opened "Can I try Gladia for free?" (`false` to `true`). Calculator inputs exist (`#calc-hours`, a range, checkboxes). Not typed, not dragged, not toggled. Plan CTAs point at signup or demo. |
| Speech-to-text API | `/product/speech-to-text-api` | Shared header. H1 "Speech-to-text API". |
| Real-time STT | `/product/speech-to-text-api/real-time` | Async/Real-time toggle, Real-time pressed. Nine FAQ buttons, closed. |
| Async STT | `/product/speech-to-text-api/async` | Same toggle, Async pressed. Ten FAQ buttons, closed. |
| Audio intelligence | `/product/audio-intelligence` | Shared header. |
| GladiaFlow | `/gladiaflow` | Body `page-flow-v3`. |
| Compare STT | `/speech-to-text-api-comparison` | H1 "Which speech-to-text API is the most accurate?". Upload/vote UI is a form-like flow. Not used. |
| Benchmarks | `/competitors/benchmarks` | H1 "Open speech-to-text API benchmarks". |
| vs Deepgram | `/competitors/gladia-vs-deepgram` | `body.light-mode`. Background white. |
| vs AssemblyAI | `/competitors/gladia-vs-assemblyai` | `body.light-mode`. |
| vs ElevenLabs | `/competitors/gladia-vs-elevenlabs` | `body.light-mode`. |
| Startup Studio | `/start-up-studio` | Application form (name, email, selects, radios, consent). Not typed. Not submitted. |
| Meeting assistants | `/use-cases/meeting-assistants` | Shared header. |
| CCaaS | `/use-cases/ccaas` | Shared header. |
| Voice agents | `/use-cases/voice-agents` | Shared header. |
| Content & media | `/use-cases/media` | Older Webflow stack (no shared header in the DOM). TypeScript / Python code tabs. Newsletter form `#sign-up`. Not typed. |
| Testimonials | `/testimonials` | Shared header. |
| Changelog | `/changelog` | Shared header. |
| Blog | `/blog` | Webflow, light, no shared header. Search form `action="/search"` with `input[name="query"]`. Not typed, so no results page. Category radios. Newsletter form. Not submitted. |
| Library | `/library` | `body.light-mode`. Filter buttons ALL, CASE STUDIES, EBOOKS, WEBINARS, TUTORIALS. "Load more" is a local button. Filters were not clicked on this walk. |
| Benchmark checker | `/benchmark-reliability-checker` | "Take the test" button. Not clicked (it starts a scored flow). |
| TCO calculator | `/build-vs-buy-whisper` | Three volume buttons (Early stage, Growth phase, Scale-up). "Get the calculator" reveals `#gated-content-form` (name, company, email). Not typed. Not submitted. |
| Compliance hub | `/compliance-hub` | Four FAQ buttons, all closed. Not opened on this walk. |
| AI note-taker guide | `/content/ai-note-takers-guide` | `body.light-mode`. Five FAQ buttons. |
| Contact center guide | `/content/ccaas-async-speech-ai-guide` | `body.light-mode`. Five FAQ buttons. |
| Creator program | `/creator-program` | `#cp-apply-form` (name, email, channel checkboxes, text areas, audience select). Not typed. Five FAQ buttons, closed. |
| Market map | `/meeting-assistant-market-map` | Section jumps (Executive summary, Magique Quadrants, Q&A, Methodology). Email form `#sv-email`. Not typed. |
| About | `/about-us` | Shared header. |
| Partners | `/partners` | Shared header. |
| Demo request | `/demo-request` | `#demo-request-form`: email, name, company, three selects, hours, two checkboxes, Submit. Not typed. Not submitted. Nine FAQ buttons, closed. |
| Solaria-3 | `/solaria-3` | Video controls: Enable sound, Play video, Replay video, Unmute video (`aria-pressed` true). Not played. |
| Security | `/security` | Shared header. |
| Bug bounty | `/bug-bounty` | Shared header. |
| Privacy notice | `/privacy-notice` | Shared header. |
| Legal notice | `/legal-notice` | Shared header. |

Also linked from the footer and loaded only as destinations, not as extra interaction walks: `/data-process-agreement`, `/general-terms-of-use-gladia-inc`, `/general-terms-of-use-gladia-sas`, `/terms-conditions-gladia-inc`, `/terms-conditions`.

## Docs

`https://docs.gladia.io/` redirects to `https://docs.gladia.io/chapters/introduction`. Title "Welcome to Gladia - Gladia". Default class `light`, `data-theme-preference` `system`, color scheme light.

| Control | What it opens |
|---|---|
| Open search | Search dialog. Placeholder "Search...". Closed with Escape. Nothing typed. |
| Switch to dark theme | Sets `html.dark` and `data-theme-preference="dark"`. Photographed. |
| Switch to light theme | Restored after the dark shot. |
| Switch to system theme | Present. Not left on system. |
| Support | `https://support.gladia.io/` (linked; not walked as an app). |
| Community | Discord invite. Not followed. |
| Blog | `https://www.gladia.io/blog` |
| Signup | `https://app.gladia.io/` with documentation UTM params. That host redirects to the sign-in wall. Not entered. |
| Documentation / API Reference | `/chapters/introduction` and `/api-reference` |
| Sidebar links | Getting started, Models, SDK, Playground, CLI, Gladia MCP (GitHub), Benchmarking, GladiaFlow, Pre-recorded Transcription (disclosure), Quickstart, and further chapters. Playground in docs is a docs page, not the app. |
| Ask the docs | A docs assistant launcher. Not opened. Sending a message would be a submission. |
| More actions | Present in the DOM, not visible at 1440, so it was not opened. |

## Status

`https://status.gladia.io/` returned 200, title "Gladia Status", text "We're fully operational". Subscribe-to-updates was not used.

## Login and signup walls

These branches stop here. Nothing was typed. Google was not clicked.

| Control that leads here | URL | What the empty wall shows |
|---|---|---|
| Header Sign up, Developers Playground, several plan CTAs | `https://app.gladia.io/signup` | "Create an account". First name, last name, work email, password, two checkboxes, Sign up, Sign up with Google, Sign in. |
| Footer Playground, docs Signup, `https://app.gladia.io/` | `https://app.gladia.io/signin` (redirect) | "Sign in to your account". Email, password, Forgot password, Sign in, Sign in with Google, Sign up. |
| Forgot password on the sign-in wall | `https://app.gladia.io/passwordReset` | "Forgot password?". Empty email field, "Send reset link". Not sent. |

No signed-in navigation, settings, or create flow was entered.
## Theme and locale

| Surface | Switch |
|---|---|
| Marketing `www.gladia.io` | No theme control. Dark `:root` is the default. Light is `body.light-mode` on `/library`, the three competitor pages, and the two guides. |
| Docs | System, light, and dark buttons. Dark was opened and photographed, then light was restored. |
| App auth walls | No theme control. Dark paint. |
| Locale | None on the public header, footer, docs, or auth walls. |
