# Lovable components

Every measured component from lovable.dev and docs.lovable.dev on 2026-11-18, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844). Nothing was signed into, submitted or purchased.

The machine-readable copy is [raw/components-computed.json](raw/components-computed.json) (29 components, 77 states).

How to read an entry:

- Colours are the computed values the browser returned (oklch on lovable.dev, rgb on docs). Tokens live in [tokens.json](tokens.json). Text is family size/line-height weight, then colour.
- The state table's first row lists every value. Later rows list only what changes. A state with the same values as the first is named in the first row's label.
- Crops are in [components/crops/](components/crops) (76 files, named `{component}-{state}.png`). Screenshots are in [screenshots/](screenshots).

## Discovery list

Desktop shots are 1440 x 900 at 1x. `-full` shots are whole pages. Phone shots are 780 wide (390 at 2x). Phone full-page shots were not kept: the page height and the screenshot height disagreed.

| Surface | URL | Screenshots |
|---|---|---|
| Home | `https://lovable.dev/` | [default](screenshots/home-light-default.png), [full](screenshots/home-light-full.png), [solutions-menu](screenshots/home-light-solutions-menu.png) |
| Pricing | `https://lovable.dev/pricing` | [default](screenshots/pricing-light-default.png), [faq-open](screenshots/pricing-light-faq-open.png), [full](screenshots/pricing-light-full.png), [yearly](screenshots/pricing-light-yearly.png) |
| Blog | `https://lovable.dev/blog` | [default](screenshots/blog-light-default.png), [full](screenshots/blog-light-full.png) |
| Security | `https://lovable.dev/security` | [default](screenshots/security-light-default.png) |
| Templates | `https://lovable.dev/templates` | [default](screenshots/templates-light-default.png) |
| Enterprise landing | `https://lovable.dev/enterprise` | [default](screenshots/enterprise-landing-light-default.png) |
| Enterprise form (dark) | `https://lovable.dev/enterprise-form` | [default](screenshots/enterprise-form-dark-default.png) |
| Log in | `https://lovable.dev/login` | [default](screenshots/login-light-default.png) |
| Docs welcome | `https://docs.lovable.dev/introduction/welcome` | [default](screenshots/docs-light-default.png), [search-open](screenshots/docs-light-search-open.png) |
| Docs plans | `https://docs.lovable.dev/introduction/plans-and-credits` | [default](screenshots/docs-plans-light-default.png) |
| Home, phone | `https://lovable.dev/` | [default](screenshots/mobile-home-light-default.png), [menu-open](screenshots/mobile-home-light-menu-open.png) |
| Pricing, phone | `https://lovable.dev/pricing` | [default](screenshots/mobile-pricing-light-default.png) |
| Log in, phone | `https://lovable.dev/login` | [default](screenshots/mobile-login-light-default.png) |
| Docs, phone | `https://docs.lovable.dev/introduction/welcome` | [default](screenshots/mobile-docs-light-default.png) |

### Overlays and transient states

| State | Where | How it was reached | Captured |
|---|---|---|---|
| Solutions menu, open | header, home | the nav button's own press | [home-light-solutions-menu](screenshots/home-light-solutions-menu.png) |
| Yearly billing | pricing | the segment's own press | [pricing-light-yearly](screenshots/pricing-light-yearly.png) |
| FAQ item, expanded | pricing | the question row's own press | [pricing-light-faq-open](screenshots/pricing-light-faq-open.png) |
| Docs search, open | docs | the Search button's own press | [docs-light-search-open](screenshots/docs-light-search-open.png) |
| Mobile menu, open | header, phone | the menu trigger's own press | [mobile-home-light-menu-open](screenshots/mobile-home-light-menu-open.png) |

## Shared values

**Focus.** 15 components were given a real keyboard focus. 15 show a visible focus state: `nav-link` (2px solid oklch(0.60 0.21 267.53)), `nav-menu` (2px solid oklch(0.60 0.21 267.53)), `nav-login` (2px solid oklch(0.60 0.21 267.53)), `nav-cta` (2px solid oklch(0.60 0.21 267.53)), `billing-monthly` (visible change in boxShadow), `billing-yearly` (visible change in boxShadow), `plan-cta` (2px solid oklch(0.52 0.23 264.41)), `credit-select` (2px solid oklch(0.52 0.23 264.41)), `faq-item` (2px solid oklch(0.52 0.23 264.41)), `oauth-google` (2px solid oklch(0.52 0.23 264.41)), `login-continue` (2px solid oklch(0.52 0.23 264.41)), `login-signup-link` (1px auto rgb(0, 95, 204)), `docs-search` (1px auto rgb(0, 149, 255)), `docs-nav` (1px auto rgb(0, 149, 255)), `docs-theme` (1px auto rgb(0, 149, 255)). Focus could not be captured on 2 more (keyboard focus never landed on them, so their readings are left out): `prompt-build`, `icon-button`.

**Pressed.** Forced with DevTools (`CSS.forcePseudoState` :active). Get started, Continue, OAuth and plan CTAs were never given a real press that would sign in or submit.

## Components

### Shell and navigation

The sticky 56px header: Solutions, Resources and Community menus, Log in, and the inverse Get started pill.

#### Header
The marketing bar: wordmark, Solutions and Resources menus, Community, Enterprise, Pricing, Security, Log in and Get started. Read as `header` on the home page.

**Values (default).** size pill x 56; background transparent; text Camera Plain Variable 14/21 400, oklab(0.300 -0.001 0.005).

![Header default](components/crops/header-default.png)

#### Nav link
Read as `nav-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 66.59 x 32; padding 0px 12px; radius 3.35e+07px; background transparent; text Camera Plain Variable 14/21 400, oklab(0.300 -0.001 0.005); transition --nav-item-hover-lmk 0.15s |
| hover | text Camera Plain Variable 14/21 400, oklab(0.222 0 0) |
| focus-visible | outline 2px solid oklch(0.60 0.21 267.53), offset 2px |
| pressed | text Camera Plain Variable 14/21 400, oklab(0.222 0 0) |

![Nav link default](components/crops/nav-link-default.png) ![Nav link hover](components/crops/nav-link-hover.png) ![Nav link focus-visible](components/crops/nav-link-focus-visible.png) ![Nav link pressed](components/crops/nav-link-pressed.png)

#### Solutions menu button
Read as `nav-menu` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 95.25 x 32; padding 0px 12px; radius 3.35e+07px; background transparent; text Camera Plain Variable 14/21 400, oklab(0.300 -0.001 0.005); transition --nav-item-hover-lmk 0.15s |
| hover | text Camera Plain Variable 14/21 400, oklab(0.222 0 0) |
| focus-visible | outline 2px solid oklch(0.60 0.21 267.53), offset 2px |
| pressed | text Camera Plain Variable 14/21 400, oklab(0.222 0 0) |

![Solutions menu button default](components/crops/nav-menu-default.png) ![Solutions menu button hover](components/crops/nav-menu-hover.png) ![Solutions menu button focus-visible](components/crops/nav-menu-focus-visible.png) ![Solutions menu button pressed](components/crops/nav-menu-pressed.png)

#### Solutions menu, open
The Solutions button after its own press. The menu is local; no destination was followed. Read as `nav-menu-open` on the home page.

**Values (opened).** size 95.25 x 32; padding 0px 12px; radius 3.35e+07px; background transparent; text Camera Plain Variable 14/21 400, oklab(0.222 0 0); transition --nav-item-hover-lmk 0.15s.

![Solutions menu, open opened](components/crops/nav-menu-open-opened.png)

#### Log in pill
The white pill in the header. Measured, never followed. Read as `nav-login` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 68.38 x 32; padding 0px 16px; radius 3.35e+07px; background oklch(1 0 0); text Camera Plain Variable 14/21 400, oklch(0.22 0 0); transition --button-overlay-lmk 0.15s |
| hover | transition none |
| focus-visible | outline 2px solid oklch(0.60 0.21 267.53), offset 2px; transition none |
| pressed | transition none |

![Log in pill default](components/crops/nav-login-default.png) ![Log in pill hover](components/crops/nav-login-hover.png) ![Log in pill focus-visible](components/crops/nav-login-focus-visible.png) ![Log in pill pressed](components/crops/nav-login-pressed.png)

#### Get started pill
The inverse pill in the header. Measured, never followed. Following it would open the sign-up page. Read as `nav-cta` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 101.45 x 32; padding 0px 16px; radius 3.35e+07px; background transparent; text Camera Plain Variable 14/21 400, oklch(0.98 0 0); transition --button-overlay-lmk 0.15s |
| hover | transition none |
| focus-visible | outline 2px solid oklch(0.60 0.21 267.53), offset 2px; transition none |
| pressed | transition none |

![Get started pill default](components/crops/nav-cta-default.png) ![Get started pill hover](components/crops/nav-cta-hover.png) ![Get started pill focus-visible](components/crops/nav-cta-focus-visible.png) ![Get started pill pressed](components/crops/nav-cta-pressed.png)

#### Build mode chip
The Build chip under the composer. Measured, never used to start a build. Read as `prompt-build` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 74.84 x 32; padding 6px 10px; radius 3.35e+07px; background transparent; outline 2px solid transparent, offset 2px; text Camera Plain Variable 14/21 400, oklch(0.1 0 0) |

![Build mode chip default](components/crops/prompt-build-default.png) ![Build mode chip hover](components/crops/prompt-build-hover.png) ![Build mode chip pressed](components/crops/prompt-build-pressed.png)

### Home

The hero kicker, the prompt composer and the Additional actions icon button. The composer was never submitted.

#### Hero title
The first heading on the home page, Camera Plain Variable. Read as `hero-title` on the home page.

**Values (default).** size 114.52 x 21.59; background transparent; text Camera Plain Variable 18/21.6 480, oklch(1 0 0 0.6).

No crop was saved for this entry.

#### Prompt field
The home composer. Focused only. Nothing was typed into a send path and nothing was submitted. Read as `prompt-field` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focused) | size 582 x 40; background transparent; shadow oklch(0.1 0 0) 0px 0px 0px 0px; text Camera Plain Variable 16/24 400, oklch(0.1 0 0) |

![Prompt field default](components/crops/prompt-field-default.png) ![Prompt field focused](components/crops/prompt-field-focused.png)

#### Additional actions
The icon button beside the composer. Its menu was not opened. Read as `icon-button` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 32 x 32; radius 3.35e+07px; background oklch(1 0 0 0.8); outline 2px solid transparent, offset 2px; text Camera Plain Variable 14/21 400, oklch(0.1 0 0) |

![Additional actions default](components/crops/icon-button-default.png) ![Additional actions hover](components/crops/icon-button-hover.png) ![Additional actions pressed](components/crops/icon-button-pressed.png)

### Pricing

The Monthly and Yearly segments, a plan CTA, the credit combobox and one expanded FAQ row. Nothing was purchased.

#### Pricing title
Read as `pricing-title` on the pricing page.

**Values (default).** size 138.58 x 45; background transparent; text Camera Plain Variable 30/45 480, oklch(0.1 0 0).

![Pricing title default](components/crops/pricing-title-default.png)

#### Monthly segment
Read as `billing-monthly` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 73.2 x 32; padding 0px 12px; radius 9999px; background transparent; text Camera Plain Variable 14/21 400, oklch(0.1 0 0); transition color 0.15s |
| hover | transition none |
| focus-visible | shadow oklch(0.52 0.23 264.41) 0px 0px 0px 2px; transition none |
| pressed | transition none |

![Monthly segment default](components/crops/billing-monthly-default.png) ![Monthly segment hover](components/crops/billing-monthly-hover.png) ![Monthly segment focus-visible](components/crops/billing-monthly-focus-visible.png) ![Monthly segment pressed](components/crops/billing-monthly-pressed.png)

#### Yearly segment
The unselected Yearly segment. Switching it is a local toggle, not a purchase. Read as `billing-yearly` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 157.58 x 32; padding 0px 12px; radius 9999px; background transparent; text Camera Plain Variable 14/21 400, oklch(0.5 0.00 107); transition color 0.15s |
| hover | text Camera Plain Variable 14/21 400, oklch(0.1 0 0); transition none |
| focus-visible | shadow oklch(0.52 0.23 264.41) 0px 0px 0px 2px; transition none |
| pressed | text Camera Plain Variable 14/21 400, oklch(0.1 0 0); transition none |

![Yearly segment default](components/crops/billing-yearly-default.png) ![Yearly segment hover](components/crops/billing-yearly-hover.png) ![Yearly segment focus-visible](components/crops/billing-yearly-focus-visible.png) ![Yearly segment pressed](components/crops/billing-yearly-pressed.png)

#### Plan CTA
A plan card Get started link. Measured, never followed. Following it would open sign-up. Read as `plan-cta` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 260 x 36; padding 6px 10px; radius 3.35e+07px; background transparent; outline 2px solid transparent, offset 2px; text Camera Plain Variable 14/21 400, oklch(0.1 0 0) |
| focus-visible | outline 2px solid oklch(0.52 0.23 264.41), offset 2px |

![Plan CTA default](components/crops/plan-cta-default.png) ![Plan CTA hover](components/crops/plan-cta-hover.png) ![Plan CTA focus-visible](components/crops/plan-cta-focus-visible.png) ![Plan CTA pressed](components/crops/plan-cta-pressed.png)

#### Credit amount select
The credit-tier combobox on a paid plan. Its list was not opened, so no checkout started. Read as `credit-select` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 260 x 32; padding 6px 8px 6px 10px; radius 8px; background oklch(1 0 0 0.8); outline 2px solid transparent, offset 2px; text Camera Plain Variable 14/21 400, oklch(0.1 0 0) |
| focus-visible | outline 2px solid oklch(0.52 0.23 264.41), offset 2px |

![Credit amount select default](components/crops/credit-select-default.png) ![Credit amount select hover](components/crops/credit-select-hover.png) ![Credit amount select focus-visible](components/crops/credit-select-focus-visible.png)

#### FAQ item
A pricing FAQ row. Expanded locally. Read as `faq-item` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, expanded) | size 896 x 62; padding 16px 0px; background transparent; text Camera Plain Variable 20/30 480, oklch(0.1 0 0); transition color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s |
| focus-visible | outline 2px solid oklch(0.52 0.23 264.41), offset 2px |

![FAQ item default](components/crops/faq-item-default.png) ![FAQ item hover](components/crops/faq-item-hover.png) ![FAQ item focus-visible](components/crops/faq-item-focus-visible.png) ![FAQ item expanded](components/crops/faq-item-expanded.png)

### Log in

OAuth buttons, the email field and Continue. The field was filled and cleared. Continue was never pressed.

#### Log in title
Read as `login-title` on the log in page.

**Values (default).** size 350 x 45; background transparent; text Camera Plain Variable 30/45 480, oklch(0.1 0 0).

![Log in title default](components/crops/login-title-default.png)

#### Continue with Google
OAuth button. Measured, never pressed. Pressing it would start a sign-in. Read as `oauth-google` on the log in page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 350 x 44; padding 10px 14px; radius 3.35e+07px; background transparent; outline 2px solid transparent, offset 2px; text Camera Plain Variable 16/24 480, oklch(0.1 0 0) |
| focus-visible | outline 2px solid oklch(0.52 0.23 264.41), offset 2px |

![Continue with Google default](components/crops/oauth-google-default.png) ![Continue with Google hover](components/crops/oauth-google-hover.png) ![Continue with Google focus-visible](components/crops/oauth-google-focus-visible.png) ![Continue with Google pressed](components/crops/oauth-google-pressed.png)

#### Continue with GitHub
OAuth button. Measured at rest, never pressed. Read as `oauth-github` on the log in page.

**Values (default).** size 350 x 44; padding 10px 14px; radius 3.35e+07px; background transparent; outline 2px solid transparent, offset 2px; text Camera Plain Variable 16/24 480, oklch(0.1 0 0).

![Continue with GitHub default](components/crops/oauth-github-default.png)

#### Email field
The log-in email field. Sample text was typed and deleted. Continue was never pressed, so no sign-in was submitted. Read as `login-field` on the log in page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 350 x 44; padding 0px 16px; radius 3.35e+07px; background transparent; shadow rgba(0, 0, 0, 0.04) 0px 2px 2px -1px inset, rgba(0, 0, 0, 0.02) 0px 4px 4px -2px inset, rgb(255, 255, 255) 0px 0.5px 0px 0px, oklch(0.55 0.00 107 0.4) 0px 0px 0px 0.5px inset; text Camera Plain Variable 16/24 400, oklch(0.1 0 0); transition box-shadow 0.15s; placeholder oklch(0.5 0.00 107) |
| focused, filled | shadow rgba(0, 0, 0, 0.04) 0px 2px 2px -1px inset, rgba(0, 0, 0, 0.02) 0px 4px 4px -2px inset, rgb(255, 255, 255) 0px 0.5px 0px 0px, oklch(0.52 0.23 264.41) 0px 0px 0px 0.5px inset; transition none |

![Email field default](components/crops/login-field-default.png) ![Email field focused](components/crops/login-field-focused.png) ![Email field filled](components/crops/login-field-filled.png)

#### Continue
The email continue button. Measured, never pressed. Pressing it would submit a sign-in. Read as `login-continue` on the log in page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 350 x 44; padding 10px 14px; radius 3.35e+07px; background oklch(0 0 0 0.88); outline 2px solid transparent, offset 2px; text Camera Plain Variable 16/24 480, oklch(0.98 0 89.88) |
| focus-visible | outline 2px solid oklch(0.52 0.23 264.41), offset 2px |

![Continue default](components/crops/login-continue-default.png) ![Continue hover](components/crops/login-continue-hover.png) ![Continue focus-visible](components/crops/login-continue-focus-visible.png) ![Continue pressed](components/crops/login-continue-pressed.png)

#### Create your account link
The link to sign-up. Measured, never followed. Read as `login-signup-link` on the log in page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 123.7 x 18; background transparent; text Camera Plain Variable 14/21 400, oklch(0.1 0 0) |
| focus-visible | outline 1px auto rgb(0, 95, 204), offset 1px |

![Create your account link default](components/crops/login-signup-link-default.png) ![Create your account link hover](components/crops/login-signup-link-hover.png) ![Create your account link focus-visible](components/crops/login-signup-link-focus-visible.png)

### Docs

docs.lovable.dev, a separate host. Inter, not Camera Plain Variable. Not in tokens.json.

#### Docs title
Read as `docs-title` on the docs page.

**Values (default).** size 334.73 x 40; background transparent; text Inter 36/40 600, rgb(22, 27, 30).

![Docs title default](components/crops/docs-title-default.png)

#### Search button
The docs search trigger. Its dialog was opened in the page capture, not submitted. Read as `docs-search` on the docs page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 269.56 x 36; padding 0px 12px 0px 14px; radius 12px; background rgb(255, 255, 255); shadow oklab(0.712 -0.004 -0.005 / 0.3) 0px 0px 0px 1px; text Inter 14/24 400, rgb(111, 116, 119) |
| hover | shadow oklab(0.442 -0.004 -0.006 / 0.3) 0px 0px 0px 1px |
| focus-visible | outline 1px auto rgb(0, 149, 255), offset 0px |
| pressed | shadow oklab(0.442 -0.004 -0.006 / 0.3) 0px 0px 0px 1px |

![Search button default](components/crops/docs-search-default.png) ![Search button hover](components/crops/docs-search-hover.png) ![Search button focus-visible](components/crops/docs-search-focus-visible.png) ![Search button pressed](components/crops/docs-search-pressed.png)

#### Docs nav row
The current sidebar row. Read as `docs-nav` on the docs page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 256 x 36; padding 6px 12px 6px 16px; radius 12px; background oklab(0.660 -0.063 -0.176 / 0.1); text Inter 14/24 400, rgb(0, 149, 255) |
| focus-visible | outline 1px auto rgb(0, 149, 255), offset -2px |

![Docs nav row default](components/crops/docs-nav-default.png) ![Docs nav row hover](components/crops/docs-nav-hover.png) ![Docs nav row focus-visible](components/crops/docs-nav-focus-visible.png)

#### Start building for free
The docs header CTA. Measured, never followed. Following it would open sign-up. Read as `docs-cta` on the docs page.

Not measured. The selector did not match a visible element.

#### Theme preference
The docs theme control. Its menu was not used to change the account, and the page was left on the theme it loaded in. Read as `docs-theme` on the docs page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 32 x 32; padding 8px; radius 8px; background transparent; text Inter 14/20 400, oklab(0.160 -0.004 -0.007 / 0.5) |
| focus-visible | outline 1px auto rgb(0, 149, 255), offset 0px |

![Theme preference default](components/crops/docs-theme-default.png) ![Theme preference hover](components/crops/docs-theme-hover.png) ![Theme preference focus-visible](components/crops/docs-theme-focus-visible.png)

### Mobile (390 wide)

The same marketing header at phone width. The menu-open screenshot exists; the sheet itself was not measured.

#### Mobile header
Read as `m-header` on the home page.

**Values (default).** size 390 x 56; background transparent; text Camera Plain Variable 14/21 400, oklch(0.98 0 0).

![Mobile header default](components/crops/m-header-default.png)

#### Mobile menu button
The phone nav button. Opened locally. Read as `m-menu` on the home page.

Not measured. The selector did not match a visible element.

## Icons

No standalone SVG icon set was lifted. The glyphs in the crops and screenshots are Lovable's artwork.

## Gaps

### Pages

- **The builder behind sign-in.** The product was never signed into. Log in, Get started and the docs signup link were measured, never followed.
- **Forms were not submitted.** The prompt composer, the log-in email field and the enterprise demo form were not submitted. Continue and the OAuth buttons were never pressed.
- **Checkout was not reached.** Plan CTAs were measured, never followed. The credit combobox list was not opened.

### States

- **Pressed** was forced with DevTools, so a handler that only runs on a real pointer event is missing.
- **Disabled, error and loading** were not seen on the public surface.
- **docs-cta** and **m-menu** selectors did not match. The mobile menu-open screenshot still exists.

### Themes

Marketing routes paint light (`html.light`). Dark is declared and painted on `/enterprise-form`. Docs has its own theme control; it was not changed.

### Fonts

- **Camera Plain Variable** and **Roboto Mono Variable** are webfonts in the lovable.dev bundle. The font files are not committed. Docs uses Inter.

### Screenshots

- Screenshots are 256-colour PNGs. Read exact colours from tokens.json or the raw JSON.
- Phone full-page shots were dropped. The screenshot height and the page height disagreed by more than one pixel.

