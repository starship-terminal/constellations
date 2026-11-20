# Leonardo.Ai components

The discovery list of every page and view captured, then one entry per component with crops of the real product, and the Gaps. Captured from leonardo.ai, app.leonardo.ai and docs.leonardo.ai on 2026-11-18, signed out, in headless Chromium at 1440 x 900 (the Phone group at 390 x 844), with computed styles read from the running page. Nothing was signed into, generated, purchased or submitted. Log in, Start now, Subscribe, Generate and the OAuth buttons were measured where they painted, never followed. Marketing, the signed-out app and the public docs page paint one dark theme.

The full per-state readings are in [raw/components-computed.json](raw/components-computed.json) (34 components, 55 states). The page layouts are described in [patterns.md](patterns.md).

How to read an entry:

- A colour is its value followed by the palette token in [tokens.json](tokens.json) with the same value, when there is one. Text is written family size/line-height weight, then its colour, for example `SF Pro 14/21 500, #21252e`, and is read from the first text node inside the component.
- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example "default (same: focus-visible)". When the root paints nothing, "Child layers" names the first nodes inside it that do.
- Crops are images of the component read from the live page, in [components/crops/](components/crops) (54 files, named `{component}-{state}.png`, at 2x). Screenshots are in [screenshots/](screenshots).

## Discovery list

Screenshots are named `{page}-dark-{state}.png`. Desktop shots are 1440 x 900 at 1x; phone shots are 780 wide (390 at 2x).

| Surface | URL | Screenshots |
|---|---|---|
| Home | `https://leonardo.ai/` | [dark-default](screenshots/home-dark-default.png), [dark-full](screenshots/home-dark-full.png) |
| Pricing | `https://leonardo.ai/pricing` | [dark-default](screenshots/pricing-dark-default.png), [dark-full](screenshots/pricing-dark-full.png) |
| API | `https://leonardo.ai/api` | [dark-default](screenshots/api-dark-default.png), [dark-full](screenshots/api-dark-full.png) |
| Learn | `https://leonardo.ai/learn` | [dark-default](screenshots/learn-dark-default.png), [dark-full](screenshots/learn-dark-full.png) |
| Contact | `https://leonardo.ai/contact-us` | [dark-default](screenshots/contact-dark-default.png) |
| Image generator | `https://leonardo.ai/ai-image-generator` | [dark-default](screenshots/imagegen-dark-default.png), [dark-full](screenshots/imagegen-dark-full.png) |
| 404 | `https://leonardo.ai/this-page-does-not-exist` | [dark-default](screenshots/notfound-dark-default.png) |
| App shell | `https://app.leonardo.ai/` | [dark-default](screenshots/app-dark-default.png), [dark-full](screenshots/app-dark-full.png) |
| Blueprints | `https://app.leonardo.ai/blueprints/platform` | [dark-default](screenshots/blueprints-dark-default.png), [dark-full](screenshots/blueprints-dark-full.png) |
| Login | `https://app.leonardo.ai/auth/login` | [dark-default](screenshots/login-dark-default.png) |
| Docs | `https://docs.leonardo.ai/docs/getting-started` | [dark-default](screenshots/docs-dark-default.png), [dark-full](screenshots/docs-dark-full.png) |
| Home, phone | `https://leonardo.ai/` | [dark-default](screenshots/mobile-home-dark-default.png), [dark-drawer](screenshots/mobile-home-dark-drawer.png), [dark-full](screenshots/mobile-home-dark-full.png) |
| App, phone | `https://app.leonardo.ai/` | [dark-default](screenshots/mobile-app-dark-default.png), [dark-full](screenshots/mobile-app-dark-full.png) |
| Login, phone | `https://app.leonardo.ai/auth/login` | [dark-default](screenshots/mobile-login-dark-default.png) |

### Overlays and transient states

| State | Where | How it was reached | Captured |
|---|---|---|---|
| Dark theme | marketing, app shell, docs | the live public paint is dark on every captured surface; docs data-color-mode=light is a declared alternate, not a captured page | [app-h1](#app-display-heading) |
| Login / OAuth | app.leonardo.ai/auth/login | Canva, Apple, Google, Microsoft and email were measured at rest, never followed or submitted | [li-canva](#continue-with-canva) |
| Generate | signed-out prompt composer | the button and prompt were measured; generation was not submitted | [app-generate](#generate-button) |
| Subscribe / checkout | leonardo.ai/pricing | Subscribe links into the app; checkout was not entered | boundary; see Gaps |

## Shared values

Values that apply across entries, from the measurement files.

**Focus.** 8 components were given a real keyboard focus. 2 draw an outline ring: `api-docs` (1px auto rgba(161, 161, 161, 0.5), offset 1px), `li-help` (1px auto #005fcc, offset 1px). 6 draw a focus ring as a shadow instead: `app-ratio`, `bp-chip`, `li-canva`, `li-google`, `li-email`, `docs-search`.

**Pressed.** Forced with DevTools (`CSS.forcePseudoState` :active:hover). Nothing a real press would submit was ever pressed.

**Motion.** Transitions measured on the components, by duration.

| Duration | Easing | Property | Where |
|---|---|---|---|
| 0.15s | `cubic-bezier(0.16, 1, 0.3, 1)` | -webkit-box-shadow, background-color, border, box-shadow | docs-nav, docs-search |
| 0.15s | `cubic-bezier(0.4, 0, 0.2, 1)` | --tw-gradient-from, --tw-gradient-to, --tw-gradient-via, all, background-color, border-color, color, fill, outline-color, stroke, text-decoration-color | app-generate, app-ratio, bp-chip, li-canva, li-email, li-google |

**Card shapes.** Default-state values; the entries hold the states.

| Card | Size | Border | Radius | Background | Shadow | Padding |
|---|---|---|---|---|---|---|
| [Learn card](#learn-card) | 590.39 x 598.11 | - | - | transparent | none | 0 |
| [Continue with Canva](#continue-with-canva) | 240.5 x 32.5 | - | 9.75px | rgba(255, 255, 255, 0.1) `color.docs.border.base` | none | 6.5px 13px |
| [Generate button](#generate-button) | 97.28 x 32.5 | - | 13000px | #262626 `color.raised` | none | 6.5px 19.5px |

## Components

### Marketing chrome

The marketing nav and footer on leonardo.ai: Create, Industry, Business, Learn, Pricing, Contact, Tutorial and Log in. The header is a nav, not a header element. Log in points at app.leonardo.ai and was measured, never followed.

#### Marketing header
The signed-out marketing header: Create, Industry, Business, Learn, Pricing, Contact, Tutorial, Log in. Read as `mkt-header` on the home page.

Not on the page when it was captured.

#### Pricing nav link
A header text link. Hover and focus measured; the link was not followed during measurement. Read as `mkt-nav-pricing` on the home page.

Not on the page when it was captured.

#### Log in link
The header Log in control. Measured at rest. It opens the app, which then gates on an account. Never followed from this measurement. Read as `mkt-login` on the home page.

Not on the page when it was captured.

#### Create menu
A header disclosure. Opened locally. No destination was followed. Read as `mkt-menu` on the home page.

Not on the page when it was captured.

#### Marketing footer
The sitemap footer: product, company, legal and social links. Read as `mkt-footer` on the home page.

**Values (default).** size 1440 x 838.13; padding 84.375px 33.75px 13.5px 33.75px; background #000000 `color.black`; text canvaSans 10.39/12.99 400, #ffffff `color.text.on.accent`; icon 16.88 x 16.88, #ffffff `color.text.on.accent`.

![Marketing footer default](components/crops/mkt-footer-default.png)

#### View documentation link
A link to the public docs. Measured, not followed from this page. Read as `api-docs` on the API page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 200.86 x 48.27; background transparent; text canvaSans 16/21.28 500, #000000 `color.black`; layers button.group/gooey.relative 200.9x48.3 #ffffff `color.text.on.accent` 3.35544e+07px |
| focus-visible | outline 1px auto rgba(161, 161, 161, 0.5), offset 1px; layers a 200.9x48.3 1px auto rgba(161, 161, 161, 0.5) offset 1px; button.group/gooey.relative 200.9x48.3 #ffffff `color.text.on.accent` 3.35544e+07px |

Child layers that carry the look: button 200.9x48.3 background #ffffff `color.text.on.accent` radius 3.35544e+07px.

![View documentation link default](components/crops/api-docs-default.png) ![View documentation link hover](components/crops/api-docs-hover.png) ![View documentation link focus-visible](components/crops/api-docs-focus-visible.png) ![View documentation link pressed](components/crops/api-docs-pressed.png)

#### Contact heading
The public contact page heading. The form itself is a submission boundary and was not filled or sent. Read as `ct-h1` on the contact page.

**Values (default).** size 507.09 x 27.22; background transparent; text leoSans 29.59/27.23 400, #ffffff `color.text.on.accent`.

![Contact heading default](components/crops/ct-h1-default.png)

### Marketing hero

Display type on the black marketing canvas: the home wordmark line, the API hero, the Learn heading and the Learn card.

#### Hero display
The marketing display heading on the black canvas. Read as `mkt-h1` on the home page.

**Values (default).** size 440.31 x 65.66; background transparent; text leoSans 34.42/32.01 800, #ffffff `color.text.on.accent`.

![Hero display default](components/crops/mkt-h1-default.png)

#### Start now button
The primary marketing CTA. States measured. Never followed. It lands on the signed-out app, then an account. Read as `mkt-cta` on the home page.

Not on the page when it was captured.

#### API hero
The public API marketing heading. Read as `api-h1` on the API page.

**Values (default).** size 1188.34 x 174.14; background transparent; text leoSans 64.5/58.05 900, #6e60ee `color.accent.base`.

![API hero default](components/crops/api-h1-default.png)

#### Learn heading
The public Learn page heading. Read as `learn-h1` on the learn page.

**Values (default).** size 901.69 x 78; background transparent; text leoSans 97.5/78 700, #ffffff `color.text.on.accent`.

![Learn heading default](components/crops/learn-h1-default.png)

#### Learn card
A published article or tutorial card. Hover measured. Not opened. Read as `learn-card` on the learn page.

**Values (default).** size 590.39 x 598.11; background transparent; text canvaSans 8.91/11.13 400, #ededed `color.leo.white`; icon 13.5 x 13.5, #ededed `color.leo.white`; layers span.text-12.text-leo-white 56.9x20.3 3.35544e+07px; span.pointer-events-none.absolute 56.9x20.3 3.35544e+07px; span.rounded-full.px-2 51.1x17.9 #03e65b `color.green` 3.35544e+07px.

Child layers that carry the look: span 56.9x20.3 image linear-gradient(#0a0a0a `color.page` 0%, rgba(37, 37, 37, 0.65) 100%) radius 3.35544e+07px; span 56.9x20.3 image linear-gradient(156.2deg, rgba(255, 255, 255, 0.4) -4.87%, rgba(61, 61, 61, 0.3) 14.18%, r radius 3.35544e+07px; span 51.1x17.9 background #03e65b `color.green` radius 3.35544e+07px.

![Learn card default](components/crops/learn-card-default.png)

### App shell

The signed-out app.leonardo.ai shell: YOURS TO CREATE, the prompt composer, Generate, aspect chips, and the public Blueprints search. Generate was measured, never submitted.

#### App sidebar
The signed-out app nav: Create, Library, Agent, Upscaler, Blueprints and the rest. Library and other account routes redirect to login. Read as `app-sidebar` on the signed-out app page.

Not on the page when it was captured.

#### Create nav link
The Create item. Measured. Generate itself is a submission boundary. Read as `app-nav-create` on the signed-out app page.

Not on the page when it was captured.

#### Sign up button
The signed-out Sign up control. Measured, never followed. Read as `app-signup` on the signed-out app page.

Not on the page when it was captured.

#### Sign in button
The signed-out Sign in control. Measured, never followed. Read as `app-signin` on the signed-out app page.

Not on the page when it was captured.

#### App display heading
The signed-out generate shell heading. Read as `app-h1` on the signed-out app page.

**Values (default).** size 667.95 x 81.25; background transparent; text leoRenaisans 73.12/81.25 700, #fafafa `color.foreground`.

![App display heading default](components/crops/app-h1-default.png)

#### Prompt field
The public prompt field. Sample text was typed and cleared. Generate was never pressed. Read as `app-prompt` on the signed-out app page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 667.88 x 18; background transparent; text canvaSans 13/17.55 400, #ffffff `color.text.on.accent`; placeholder #a1a1a1 |
| focused, filled | size 820.63 x 18 |

![Prompt field default](components/crops/app-prompt-default.png) ![Prompt field focused](components/crops/app-prompt-focused.png) ![Prompt field filled](components/crops/app-prompt-filled.png)

#### Generate button
The Generate control. States forced through CDP. Never clicked, so no generation ran. Read as `app-generate` on the signed-out app page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 97.28 x 32.5; padding 6.5px 19.5px; radius 13000px; background #262626 `color.raised`; text canvaSans 13/19.5 500, #737373 `color.text.muted`; transition all 0.15s cubic-bezier(0.4, 0, 0.2, 1); opacity 0.5 |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

![Generate button default](components/crops/app-generate-default.png) ![Generate button hover](components/crops/app-generate-hover.png) ![Generate button pressed](components/crops/app-generate-pressed.png)

#### Aspect chip
An aspect-ratio chip on the signed-out composer. Measured at rest. Not selected, so no generation settings were submitted. Read as `app-ratio` on the signed-out app page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 66.03 x 32.5; padding 6.5px 13px; radius 13000px; background rgba(255, 255, 255, 0.1) `color.docs.border.base`; text canvaSans 13/19.5 500, #d4d4d4 `color.text.secondary`; transition all 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 16.25 x 16.25, #d4d4d4 `color.text.secondary` |
| hover | background rgba(255, 255, 255, 0.2) `color.docs.border.strong` |
| focus-visible | shadow rgba(110, 96, 238, 0.5) 0px 0px 0px 3px |
| pressed | background rgba(23, 23, 23, 0.8) |

![Aspect chip default](components/crops/app-ratio-default.png) ![Aspect chip hover](components/crops/app-ratio-hover.png) ![Aspect chip focus-visible](components/crops/app-ratio-focus-visible.png) ![Aspect chip pressed](components/crops/app-ratio-pressed.png)

#### Featured model card
A published model card on the signed-out home. Hover measured. Not opened. Read as `app-card` on the signed-out app page.

Not on the page when it was captured.

#### Blueprints heading
The public blueprint catalog heading. Read as `bp-h1` on the blueprints page.

Not on the page when it was captured.

#### Blueprint search
The catalog search field. Typed and cleared. Not submitted. Read as `bp-search` on the blueprints page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focused) | size 474.5 x 19.5; background transparent; text canvaSans 13/19.5 400, #fafafa `color.foreground`; placeholder #a1a1a1 |
| filled | size 438.75 x 19.5 |

![Blueprint search default](components/crops/bp-search-default.png) ![Blueprint search focused](components/crops/bp-search-focused.png) ![Blueprint search filled](components/crops/bp-search-filled.png)

#### Category chip
A blueprint category chip. Measured at rest. Read as `bp-chip` on the blueprints page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 52 x 31.25; padding 6.5px 13px; border 1px solid #7c71f7 `color.text.link`; radius 13000px; background rgba(110, 96, 238, 0.15); text canvaSans 11.37/16.25 500, #fafafa `color.foreground`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| focus-visible | shadow #ffffff 0px 0px 0px 0px, rgba(110, 96, 238, 0.5) 0px 0px 0px 4px |

![Category chip default](components/crops/bp-chip-default.png) ![Category chip hover](components/crops/bp-chip-hover.png) ![Category chip focus-visible](components/crops/bp-chip-focus-visible.png) ![Category chip pressed](components/crops/bp-chip-pressed.png)

### Login boundary

The OAuth card at app.leonardo.ai/auth/login. Canva, Apple, Google, Microsoft and Continue with Email were measured at rest. No provider was followed and the email form was not submitted.

#### Login heading
The sign-up or login card. The boundary of the signed-out capture. Read as `li-h1` on the login page.

**Values (default).** size 131.25 x 19.5; background transparent; text canvaSans 13/19.5 500, #fafafa `color.foreground`.

![Login heading default](components/crops/li-h1-default.png)

#### Continue with Canva
An OAuth button. Measured at rest. Never followed. Read as `li-canva` on the login page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 240.5 x 32.5; padding 6.5px 13px; radius 9.75px; background rgba(255, 255, 255, 0.1) `color.docs.border.base`; text canvaSans 13/19.5 500, #d4d4d4 `color.text.secondary`; transition all 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 16.25 x 16.25, #ffffff `color.text.on.accent` |
| hover | background rgba(255, 255, 255, 0.2) `color.docs.border.strong` |
| focus-visible | shadow rgba(110, 96, 238, 0.5) 0px 0px 0px 3px |
| pressed | background rgba(23, 23, 23, 0.8) |

![Continue with Canva default](components/crops/li-canva-default.png) ![Continue with Canva hover](components/crops/li-canva-hover.png) ![Continue with Canva focus-visible](components/crops/li-canva-focus-visible.png) ![Continue with Canva pressed](components/crops/li-canva-pressed.png)

#### Continue with Google
An OAuth button. Measured at rest. Never followed. Read as `li-google` on the login page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 240.5 x 32.5; padding 6.5px 13px; radius 9.75px; background rgba(255, 255, 255, 0.1) `color.docs.border.base`; text canvaSans 13/19.5 500, #d4d4d4 `color.text.secondary`; transition all 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 16.25 x 16.25, #d4d4d4 `color.text.secondary` |
| hover | background rgba(255, 255, 255, 0.2) `color.docs.border.strong` |
| focus-visible | shadow rgba(110, 96, 238, 0.5) 0px 0px 0px 3px |
| pressed | background rgba(23, 23, 23, 0.8) |

![Continue with Google default](components/crops/li-google-default.png) ![Continue with Google hover](components/crops/li-google-hover.png) ![Continue with Google focus-visible](components/crops/li-google-focus-visible.png) ![Continue with Google pressed](components/crops/li-google-pressed.png)

#### Continue with Email
The email path control. Measured. Not clicked, so the email form was not submitted. A Turnstile widget is present and was not solved. Read as `li-email` on the login page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 240.5 x 32.5; padding 6.5px 13px; radius 9.75px; background rgba(255, 255, 255, 0.1) `color.docs.border.base`; text canvaSans 13/19.5 500, #d4d4d4 `color.text.secondary`; transition all 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 16.25 x 16.25, #d4d4d4 `color.text.secondary` |
| hover | background rgba(255, 255, 255, 0.2) `color.docs.border.strong` |
| focus-visible | shadow rgba(110, 96, 238, 0.5) 0px 0px 0px 3px |
| pressed | background rgba(23, 23, 23, 0.8) |

![Continue with Email default](components/crops/li-email-default.png) ![Continue with Email hover](components/crops/li-email-hover.png) ![Continue with Email focus-visible](components/crops/li-email-focus-visible.png) ![Continue with Email pressed](components/crops/li-email-pressed.png)

#### Need help link
The public login FAQ link. Measured, not followed. Read as `li-help` on the login page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 70.86 x 18; background transparent; text canvaSans 13/19.5 500, #7c71f7 `color.text.link` |
| focus-visible | outline 1px auto #005fcc, offset 1px; layers a.text-highlight-foreground.text-sm 70.9x18.0 1px auto #005fcc offset 1px |

![Need help link default](components/crops/li-help-default.png) ![Need help link hover](components/crops/li-help-hover.png) ![Need help link focus-visible](components/crops/li-help-focus-visible.png) ![Need help link pressed](components/crops/li-help-pressed.png)

### Docs

docs.leonardo.ai getting-started, painted dark. Search and a nav link were measured. The docs color-mode light set is declared, not the live public paint.

#### Docs heading
The Quick Start heading on the public ReadMe docs. Read as `docs-h1` on the docs page.

**Values (default).** size 800 x 39.84; background transparent; text Twemoji Country Flags 31/39.85 600, #ffffff `color.text.on.accent`.

![Docs heading default](components/crops/docs-h1-default.png)

#### Docs search
The docs search control. Measured at rest. The search dialog was not opened, so no query was sent. Read as `docs-search` on the docs page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 150 x 32; padding 0px 8px; radius 6px; background rgba(0, 0, 0, 0.5); shadow rgba(255, 255, 255, 0.1) 0px 0px 0px 1px; text Twemoji Country Flags 14/32 400, #aeb2bd `color.docs.text.minimum`; transition box-shadow 0.15s cubic-bezier(0.16, 1, 0.3, 1), -webkit-box-shadow 0.15s cubic-bezier(0.16, 1, 0.3, 1) |
| focus-visible | shadow rgba(255, 255, 255, 0.75) 0px 0px 0px 1px, rgba(255, 255, 255, 0.25) 0px 0px 0px 4px |

![Docs search default](components/crops/docs-search-default.png) ![Docs search hover](components/crops/docs-search-hover.png) ![Docs search focus-visible](components/crops/docs-search-focus-visible.png) ![Docs search pressed](components/crops/docs-search-pressed.png)

#### Docs nav link
A sidebar documentation link. Hover measured. Not followed. Read as `docs-nav` on the docs page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 91.06 x 32; padding 10px; border 1px solid transparent; radius 6px; background rgba(255, 255, 255, 0.1) `color.docs.border.base`; text Twemoji Country Flags 14/normal 500, #ffffff `color.text.on.accent`; transition background-color 0.15s cubic-bezier(0.16, 1, 0.3, 1), border 0.15s cubic-bezier(0.16, 1, 0.3, 1) |
| hover | border 1px solid rgba(255, 255, 255, 0.1) `color.docs.border.base` |

![Docs nav link default](components/crops/docs-nav-default.png) ![Docs nav link hover](components/crops/docs-nav-hover.png)

### Phone

The 390-wide signed-out app: the prompt field. The marketing phone drawer is a screenshot, not a measured component.

#### Phone app chrome
The signed-out app chrome at 390px. Read as `m-app-bar` on the phone app page.

Not on the page when it was captured.

#### Phone prompt
The prompt field at 390px, at rest. Read as `m-app-prompt` on the phone app page.

**Values (default).** size 298 x 43; background transparent; text canvaSans 16/21.63 400, #ffffff `color.text.on.accent`; placeholder #a1a1a1.

![Phone prompt default](components/crops/m-app-prompt-default.png)

## Icons

No standalone SVG icon set was lifted on this pass. The Leonardo wordmark, nav glyphs and OAuth marks are visible in the crops and screenshots. Declared under layoutGaps in the catalog entry.

| Icon | Rendered sizes | View box | Style | Seen on | Next to |
|---|---|---|---|---|---|

## Gaps

### The signed-in product

Account, generation, library, checkout and API keys need a Leonardo account. Library and other account routes redirect to https://app.leonardo.ai/auth/login. Generate, Subscribe, Start now and the OAuth buttons were measured where they painted, never followed or submitted. What is public signed out: the marketing pages, the signed-out app shell, public Blueprints, the login card and the docs getting-started page.

### Pages

- **Library, account, API keys and checkout.** These sit behind https://app.leonardo.ai/auth/login or a Subscribe handoff into the app. Recorded, not captured.
- **Marketing nav controls.** The home header, Pricing link, Log in, Create menu and Start now were not boxed on the measurement pass (Cloudflare on the retry). The pages themselves are in screenshots/.
- **App sidebar, Sign up, Sign in and featured cards.** Visible on the app screenshot, not boxed as components.

### States

- **Pressed** was forced with DevTools on every control, so a state a script adds on mousedown (if any) is missing.
- **Disabled, error and loading states** were not seen on the public surface.

### Themes

Marketing and the signed-out app paint one dark theme. No public theme toggle was found. The docs stylesheets declare data-color-mode light and dark; the public docs page paints dark. light.color.docs.* is that declared alternate. light.color.page and the other product roles match the dark paint, because those names do not switch.

### Fonts

- **canvaSans** is the UI face, **ufficioDisplay** the marketing wordmark, **leoSans** the marketing display, **leoRenaisans** the app display. They are served from Leonardo's own CDN and not redistributed. The style guide falls back to system fonts.

### Screenshots

- Full-page shots are single document captures; the marketing pages' animated hero fields are motion media, frozen at capture time.
- Product names, taglines, imagery and prices are the site's published content; screenshots are 256-colour PNGs, read exact colours from the tokens or the raw files.

### Content left out

- Product names, taglines, imagery and prices are the site's published content; only frames and components were measured.
