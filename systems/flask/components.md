# Flask components

The discovery list of every page and view captured, then one entry per component with crops of the real product, and the Gaps. Captured from flask.do on 2026-11-15, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running page. Nothing was signed into, bought or submitted; the login form was never sent; every link, CTA, scheduler and the external 'Add to Cursor' MCP-install link was measured, never followed.

The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) (45 components, 128 states). The page layouts are described in [patterns.md](patterns.md).

How to read an entry:

- A colour is its value followed by the palette token in [tokens.json](tokens.json) with the same value, when there is one. Text is written family size/line-height weight, then its colour, for example `ui-sans-serif 16/24 400, #fafafa`, and is read from the first text node inside the component.
- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example "default (same: focus-visible)". When the root paints nothing, "Child layers" names the first nodes inside it that do.
- Crops are images of the component read from the live page, in [components/crops/](components/crops) (122 files, named `{component}-{state}.png`, at 2x). Screenshots are in [screenshots/](screenshots).

## Discovery list

Screenshots are named `{page}-{theme}-state.png` where `{theme}` is the mode the page painted at capture: `dark` for every public page — the only --ds-* layer the bundle declares is the dark `default` theme and the site ships no light variant or toggle. Desktop shots are 1440 x 900 at 1x; `-full` shots are whole pages bounded at eight chunks; mobile shots are `mobile-{page}-{theme}-{state}.png`, 780 wide (390 at 2x).

| Surface | URL | Screenshots |
|---|---|---|
| Home (with the embedded product demo) | `/` | [default](screenshots/home-dark-default.png), [demo-asset-2](screenshots/home-dark-demo-asset-2.png), [full](screenshots/home-dark-full.png) |
| Pricing | `/pricing` | [billed-quarterly](screenshots/pricing-dark-billed-quarterly.png), [default](screenshots/pricing-dark-default.png), [faq-open](screenshots/pricing-dark-faq-open.png), [full](screenshots/pricing-dark-full.png) |
| Flask MCP Server docs | `/mcp` | [default](screenshots/mcp-dark-default.png), [full](screenshots/mcp-dark-full.png) |
| About | `/about` | [default](screenshots/about-dark-default.png), [full](screenshots/about-dark-full.png) |
| Security | `/security` | [default](screenshots/security-dark-default.png), [full](screenshots/security-dark-full.png) |
| Video collaboration | `/video-collaboration` | [default](screenshots/video-collaboration-dark-default.png), [full](screenshots/video-collaboration-dark-full.png) |
| Frame.io alternative | `/frame-io-alternative` | [default](screenshots/frame-io-alternative-dark-default.png), [full](screenshots/frame-io-alternative-dark-full.png) |
| Privacy policy | `/privacy-policy` | [default](screenshots/privacy-policy-dark-default.png), [full](screenshots/privacy-policy-dark-full.png) |
| Terms of service | `/terms-of-service` | [default](screenshots/terms-of-service-dark-default.png), [full](screenshots/terms-of-service-dark-full.png) |
| Sign in (signed-out) | `/login` | [default](screenshots/login-dark-default.png), [full](screenshots/login-dark-full.png) |
| Home, phone | `/` | [default](screenshots/mobile-home-dark-default.png), [full](screenshots/mobile-home-dark-full.png), [menu](screenshots/mobile-home-dark-menu.png) |
| Pricing, phone | `/pricing` | [default](screenshots/mobile-pricing-dark-default.png), [full](screenshots/mobile-pricing-dark-full.png) |
| Sign in, phone | `/login` | [default](screenshots/mobile-login-dark-default.png), [full](screenshots/mobile-login-dark-full.png) |

### Overlays and transient states

| State | Where | How it was reached | Captured |
|---|---|---|---|
| Demo version chip | home demo mock | clicked the demo's own 'Version' chip — a local UI toggle inside the marketing demo | [home-dark-demo-asset-2](screenshots/home-dark-demo-asset-2.png), [demo-version-chip](#demo-version-chip) |
| Billing switch | /pricing | toggled to the 'Billed quarterly' view, then back to 'Billed yearly' — a local UI toggle | [pricing-dark-billed-quarterly](screenshots/pricing-dark-billed-quarterly.png), [billing-switch](#billing-switch) |
| FAQ accordion | /pricing | clicked one FAQ row — a local UI toggle; aria-expanded had to stay true | [pricing-dark-faq-open](screenshots/pricing-dark-faq-open.png), [faq-acc](#faq-accordion) |
| Mobile nav overlay | home page, phone width | the icon-only 'Open menu' hamburger's own toggle | [mobile-home-dark-menu](screenshots/mobile-home-dark-menu.png), [m-drawer](#mobile-nav-overlay) |
| Login field | /login | typed into then cleared — nothing sent; 'Continue with Google' and 'Continue with Email' were never pressed | [login-email](#email-field-login) |
| Demo controls | home demo mock | the mock's 'Open menu', share-scope and folder controls were pointer-tested; the mock's overlay intercepted the clicks, so their opened states are uncaptured | unreached; see Gaps |
| External actions | every page | 'Add to Cursor' (a base64 MCP-install URL), the Book Demo/Call schedulers, mailto and social links | measured, never followed |
| Signed-in product | a Flask account | the workspace and every post-login surface needs an account — /home redirects to /login | boundary; see Gaps |

## Shared values

Values that apply across entries, from the measurement files.

**Focus.** 17 components were given a real keyboard focus. 0 draw an outline ring: . 7 draw a focus ring as a shadow instead: `nav-cta`, `hero-cta`, `hero-copy-prompt`, `cta-book-demo`, `billing-switch`, `login-google`, `m-hero-cta`. The other 10 show no measured change: `nav-pricing`, `nav-features`, `plan-cta`, `book-call`, `faq-acc`, `docs-cursor`, `docs-anchor`, `about-link`, `seo-cta`, `m-menu-btn`.

**Pressed.** Forced with DevTools (`CSS.forcePseudoState` :active:hover). Nothing a real press would submit was ever pressed.

**Motion.** Transitions measured on the components, by duration.

| Duration | Easing | Property | Where |
|---|---|---|---|
| 0.15s | `cubic-bezier(0.23, 1, 0.32, 1)` | box-shadow, color, opacity, transform | book-call, demo-acme-btn, demo-close, demo-copy-link, demo-share-scope, demo-tab-context, demo-tab-feedback, demo-th and more |
| 0.15s | `cubic-bezier(0.4, 0, 0.2, 1)` | all, background-color, border-color, color, fill, stroke, text-decoration-color | about-link, billing-switch, docs-anchor, faq-acc, login-email, m-menu-btn, mkt-header |
| 0.2s | `cubic-bezier(0.4, 0, 0.2, 1)` | background-color, border-color, color, fill, opacity, stroke, text-decoration-color | cta-book-demo, demo-feedback-field, hero-cta, m-hero-cta |
| 0.28s | `cubic-bezier(0.23, 1, 0.32, 1)` | box-shadow, color | login-google, plan-cta, seo-cta |

**Card shapes.** Default-state values; the entries hold the states.

| Card | Size | Border | Radius | Background | Shadow | Padding |
|---|---|---|---|---|---|---|
| [Login panel](#login-panel) | 288 x 318 | - | - | transparent | none | 0 |
| [Mobile nav overlay](#mobile-nav-overlay) | 366 x 126 | T: 1px solid #2b2b2b `dark.line.edge`; R: 1px solid #282828 `dark.line.2`; B: 1px solid #282828 `dark.line.2`; L: 1px solid #282828 `dark.line.2` | 16px | #1f1f1f `dark.surface.3` | rgba(0, 0, 0, 0.4) 0px 2px 8px -2px, rgba(0, 0, 0, 0.5) 0px 16px 40px -8px | 4px 6px 8px 6px |

## Components

### Site chrome

The fixed header on every page: the Flask mark, the Pricing and Features links and the 'Sign Up' CTA. There is no Log in link — /login is reached through Sign Up.

#### Site header
The sticky top bar on every page (a div, not <header>): the Flask mark, the Pricing/Features nav links and the "Sign Up" CTA (which links to /home — the login boundary). Read as `mkt-header` on the home page.

**Values (default).** size 1440 x 56; background transparent; text ui-sans-serif 13/19.5 400, #a0a0a0 `dark.fg.2.default`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 48 x 16, #fafafa `dark.fg.1`; layers button.md:hidden.flex 0.0x0.0 2px solid rgba(0, 0, 0, 0) offset 2px; a.ds-focus:ring-2.ds-focus:ring-focus-ring 81.5x32.0 rgba(160, 160, 160, 0.063) rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(173, 173, 173, 0.07) 0px 0.5px 0px 0px inset, rgba(111, 111, 111, 0.255) 0px 0px 0px 0.5px inset, rgba(0, 0, 0, 0.18) 0px 1px 2px 0px, rgba(0, 0, 0, 0.18) 0px 2px 6px -2px 9999px; a::before.ds-focus:ring-2.ds-foc.

Child layers that carry the look: button 0x0; a 81.5x32 background rgba(160, 160, 160, 0.063) `dark.action.bookCallFill` radius 9999px shadow transparent 0px 0px 0px 0px, rgba(173, 173, 173, 0.07) 0px 0.5px 0px 0px inset, rgba(111, 111, 111, 0.255) 0px 0px 0px 0.5px inset, rgba(0, 0, 0, 0.18) `dark.shadow.color.raised` 0px 1px 2px 0px, rgba(0, 0, 0, 0.18) `dark.shadow.color.raised` 0px 2px 6px -2px; a::before 81.5156pxx32px image radial-gradient(90px at 50% 50%, rgba(250, 250, 250, 0.06) `dark.control.light.default`, t radius 9999px.

![Site header default](components/crops/mkt-header-default.png)

#### Logo
The Flask mark (aria-label="Flask") in the top bar, linking home. Read as `mkt-logo` on the home page.

**Values (default).** size 64 x 32; padding 0px 8px; radius 12px; background transparent; text ui-sans-serif 16/24 400, #fafafa `dark.fg.1`; transition transform 0.15s cubic-bezier(0.23, 1, 0.32, 1); icon 48 x 16, #fafafa `dark.fg.1`.

![Logo default](components/crops/mkt-logo-default.png)

#### Nav link
The "Pricing" header link; measured, never followed. Read as `nav-pricing` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 58.22 x 32; padding 0px 8px; radius 12px; background transparent; text ui-sans-serif 13/19.5 400, #a0a0a0 `dark.fg.2.default`; transition transform 0.15s cubic-bezier(0.23, 1, 0.32, 1) |
| hover | background rgba(250, 250, 250, 0.035); text ui-sans-serif 13/19.5 400, #fafafa `dark.fg.1` |
| pressed | size 56.47 x 31.04; background rgba(250, 250, 250, 0.035); text ui-sans-serif 13/19.5 400, #fafafa `dark.fg.1`; transform scale(0.97) |

![Nav link default](components/crops/nav-pricing-default.png) ![Nav link hover](components/crops/nav-pricing-hover.png) ![Nav link focus-visible](components/crops/nav-pricing-focus-visible.png) ![Nav link pressed](components/crops/nav-pricing-pressed.png)

#### Features nav link
The "Features" header link; measured, never followed. The header offers no Log in link — /login is reached through Sign Up. Read as `nav-features` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 68.78 x 32; padding 0px 8px; radius 12px; background transparent; text ui-sans-serif 13/19.5 400, #a0a0a0 `dark.fg.2.default`; transition transform 0.15s cubic-bezier(0.23, 1, 0.32, 1) |
| hover | background rgba(250, 250, 250, 0.035); text ui-sans-serif 13/19.5 400, #fafafa `dark.fg.1` |
| pressed | size 66.72 x 31.04; background rgba(250, 250, 250, 0.035); text ui-sans-serif 13/19.5 400, #fafafa `dark.fg.1`; transform scale(0.97) |

![Features nav link default](components/crops/nav-features-default.png) ![Features nav link hover](components/crops/nav-features-hover.png) ![Features nav link focus-visible](components/crops/nav-features-focus-visible.png) ![Features nav link pressed](components/crops/nav-features-pressed.png)

#### Header CTA
The "Sign Up" CTA in the top bar — it links to /home, which redirects to /login; measured, never followed. Read as `nav-cta` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 81.52 x 32; padding 0px 14px; radius 9999px; background rgba(160, 160, 160, 0.063) `dark.action.bookCallFill`; shadow rgba(173, 173, 173, 0.07) 0px 0.5px 0px 0px inset, rgba(111, 111, 111, 0.255) 0px 0px 0px 0.5px inset, rgba(0, 0, 0, 0.18) 0px 1px 2px 0px, rgba(0, 0, 0, 0.18) 0px 2px 6px -2px; text ui-sans-serif 13/19.5 500, rgba(250, 250, 250, 0.7) `dark.control.fg.default`; transition color 0.15s cubic-bezier(0.23, 1, 0.32, 1), transform 0.15s cubic-bezier(0.23, 1, 0.32, 1), opacity 0.15s cubic-bezier(0.23, 1, 0.32, 1), box-shadow 0.15s cubic-bezier(0.23, 1, 0.32, 1); icon 14 x 14, rgba(250, 250, 250, 0.7) `dark.control.fg.default`; layers ::before rgba(0, 0, 0, 0) 0px none 0 |
| hover | shadow rgba(173, 173, 173, 0.16) 0px 0.5px 0px 0px inset, rgba(111, 111, 111, 0.255) 0px 0px 0px 0.5px inset, rgba(0, 0, 0, 0.18) 0px 1px 2px 0px, rgba(0, 0, 0, 0.18) 0px 2px 6px -2px; text ui-sans-serif 13/19.5 500, rgba(250, 250, 250, 0.95) `dark.control.fg.hover`; icon 14 x 14, rgba(250, 250, 250, 0.95) `dark.control.fg.hover`; layers ::before rgba(0, 0, 0, 0) 0px none 1 |
| focus-visible | shadow #ffffff 0px 0px 0px 0px, rgba(173, 173, 173, 0.5) 0px 0px 0px 2px, rgba(0, 0, 0, 0.18) 0px 1px 2px 0px, rgba(0, 0, 0, 0.18) 0px 2px 6px -2px |
| pressed | shadow rgba(173, 173, 173, 0.16) 0px 0.5px 0px 0px inset, rgba(111, 111, 111, 0.255) 0px 0px 0px 0.5px inset, rgba(0, 0, 0, 0.18) 0px 1px 1px 0px; text ui-sans-serif 13/19.5 500, rgba(250, 250, 250, 0.95) `dark.control.fg.hover`; transform translate(0px, 1px); icon 14 x 14, rgba(250, 250, 250, 0.95) `dark.control.fg.hover`; layers ::before rgba(0, 0, 0, 0) 0px none 1 |

![Header CTA default](components/crops/nav-cta-default.png) ![Header CTA hover](components/crops/nav-cta-hover.png) ![Header CTA focus-visible](components/crops/nav-cta-focus-visible.png) ![Header CTA pressed](components/crops/nav-cta-pressed.png)

### Home and landing pages

The home hero ('The world's fastest way to review video.') with the Open Flask / Copy Prompt pills, the section headings, the 'Book a Demo' CTAs, and the SEO landing pages that share the shell (/video-collaboration, /frame-io-alternative).

#### Hero headline
"The world's fastest way to review video." — the flask.do hero display heading. Read as `hero-h1` on the home page.

**Values (default).** size 1200 x 138.22; background transparent; text ui-sans-serif 64/69.12 500, #fafafa `dark.fg.1`.

![Hero headline default](components/crops/hero-h1-default.png)

#### Hero CTA
The hero's "Open Flask" pill — the primary call to action; measured, never followed. Read as `hero-cta` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 127.84 x 40; padding 0px 12px 0px 16px; border 1px solid transparent; radius 9999px; background transparent; image linear-gradient(to top, #adadad `dark.brand.default` 20%, #cacaca `dark.brand.highlight` 80%); shadow rgba(255, 255, 255, 0.85) 0px 1px 0px 0px inset, rgba(0, 0, 0, 0.06) 0px -1px 0px 0px inset, rgba(0, 0, 0, 0.55) 0px 0px 0px 0.5px, rgba(0, 0, 0, 0.35) 0px 1px 2px 0px, rgba(0, 0, 0, 0.22) 0px 4px 12px 0px; text ui-sans-serif 15/22.5 500, #090909 `dark.brand.fg.default`; transition color 0.2s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), fill 0.2s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.2s cubic-bezier(0.4, 0, 0.2, 1); icon 16 x 16, #090909 `dark.brand.fg.default`; layers ::before rgba(0, 0, 0, 0) 0px rgba(255, 255, 255, 0.85) 0px 1px 0px 0px inset, rgba(0, 0, 0, 0.06) 0px -1px 0px 0px inset 0; ::after rgba(0, 0, 0, 0) 0px none 0 |
| hover | shadow rgba(255, 255, 255, 0.85) 0px 1px 0px 0px inset, rgba(0, 0, 0, 0.06) 0px -1px 0px 0px inset, rgba(0, 0, 0, 0.55) 0px 0px 0px 0.5px, rgba(0, 0, 0, 0.35) 0px 2px 4px 0px, rgba(0, 0, 0, 0.28) 0px 6px 16px 0px; text ui-sans-serif 15/22.5 500, #242424 `dark.brand.fg.hover`; icon 16 x 16, #242424 `dark.brand.fg.hover`; layers ::before rgba(0, 0, 0, 0) 0px rgba(255, 255, 255, 0.85) 0px 1px 0px 0px inset, rgba(0, 0, 0, 0.06) 0px -1px 0px 0px inset 1; ::after rgba(0, 0, 0, 0) 0px none 1 |
| focus-visible | shadow #ffffff 0px 0px 0px 0px, rgba(173, 173, 173, 0.5) 0px 0px 0px 2px |
| pressed | shadow rgba(255, 255, 255, 0.6) 0px 1px 0px 0px inset, rgba(0, 0, 0, 0.06) 0px -1px 0px 0px inset, rgba(0, 0, 0, 0.55) 0px 0px 0px 0.5px, rgba(0, 0, 0, 0.3) 0px 1px 1px 0px; text ui-sans-serif 15/22.5 500, #242424 `dark.brand.fg.hover`; transform translate(0px, 1px); icon 16 x 16, #242424 `dark.brand.fg.hover`; layers ::before rgba(0, 0, 0, 0) 0px rgba(255, 255, 255, 0.85) 0px 1px 0px 0px inset, rgba(0, 0, 0, 0.06) 0px -1px 0px 0px inset 1; ::after rgba(0, 0, 0, 0) 0px none 1 |

![Hero CTA default](components/crops/hero-cta-default.png) ![Hero CTA hover](components/crops/hero-cta-hover.png) ![Hero CTA focus-visible](components/crops/hero-cta-focus-visible.png) ![Hero CTA pressed](components/crops/hero-cta-pressed.png)

#### Hero "Copy Prompt" button
The hero's secondary "Copy Prompt" pill; measured, never pressed. Read as `hero-copy-prompt` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 145.75 x 40; padding 0px 14px 0px 16px; radius 9999px; background #121212 `dark.surface.1`; image linear-gradient(rgba(160, 160, 160, 0.063) `dark.action.bookCallFill`, rgba(160, 160, 160, 0.063) `dark.action.bookCallFill`), none; shadow rgba(173, 173, 173, 0.07) 0px 0.5px 0px 0px inset, rgba(111, 111, 111, 0.255) 0px 0px 0px 0.5px inset, rgba(0, 0, 0, 0.18) 0px 1px 2px 0px, rgba(0, 0, 0, 0.18) 0px 2px 6px -2px; text ui-sans-serif 15/22.5 500, rgba(250, 250, 250, 0.7) `dark.control.fg.default`; transition color 0.15s cubic-bezier(0.23, 1, 0.32, 1), transform 0.15s cubic-bezier(0.23, 1, 0.32, 1), opacity 0.15s cubic-bezier(0.23, 1, 0.32, 1), box-shadow 0.15s cubic-bezier(0.23, 1, 0.32, 1); icon 16 x 16, rgba(250, 250, 250, 0.7) `dark.control.fg.default`; layers ::before rgba(0, 0, 0, 0) 0px none 0 |
| hover | shadow rgba(173, 173, 173, 0.16) 0px 0.5px 0px 0px inset, rgba(111, 111, 111, 0.255) 0px 0px 0px 0.5px inset, rgba(0, 0, 0, 0.18) 0px 1px 2px 0px, rgba(0, 0, 0, 0.18) 0px 2px 6px -2px; text ui-sans-serif 15/22.5 500, rgba(250, 250, 250, 0.95) `dark.control.fg.hover`; icon 16 x 16, rgba(250, 250, 250, 0.95) `dark.control.fg.hover`; layers ::before rgba(0, 0, 0, 0) 0px none 1 |
| focus-visible | shadow #ffffff 0px 0px 0px 0px, rgba(173, 173, 173, 0.5) 0px 0px 0px 2px, rgba(0, 0, 0, 0.18) 0px 1px 2px 0px, rgba(0, 0, 0, 0.18) 0px 2px 6px -2px |
| pressed | shadow rgba(173, 173, 173, 0.16) 0px 0.5px 0px 0px inset, rgba(111, 111, 111, 0.255) 0px 0px 0px 0.5px inset, rgba(0, 0, 0, 0.18) 0px 1px 1px 0px; text ui-sans-serif 15/22.5 500, rgba(250, 250, 250, 0.95) `dark.control.fg.hover`; transform translate(0px, 1px); icon 16 x 16, rgba(250, 250, 250, 0.95) `dark.control.fg.hover`; layers ::before rgba(0, 0, 0, 0) 0px none 1 |

![Hero "Copy Prompt" button default](components/crops/hero-copy-prompt-default.png) ![Hero "Copy Prompt" button hover](components/crops/hero-copy-prompt-hover.png) ![Hero "Copy Prompt" button focus-visible](components/crops/hero-copy-prompt-focus-visible.png) ![Hero "Copy Prompt" button pressed](components/crops/hero-copy-prompt-pressed.png)

#### Section heading
A marketing section heading further down the home page ("Talk, Draw, Show", "Share, Organize and Compare", …). Read as `section-h2` on the home page.

**Values (default).** size 900 x 48.39; background transparent; text ui-sans-serif 44/48.4 500, #fafafa `dark.fg.1`.

![Section heading default](components/crops/section-h2-default.png)

#### Book a Demo CTA
A "Book a Demo" CTA in the marketing page body; measured, never followed. Read as `cta-book-demo` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 110.03 x 32; padding 0px 14px; radius 9999px; background rgba(160, 160, 160, 0.063) `dark.action.bookCallFill`; shadow rgba(173, 173, 173, 0.07) 0px 0.5px 0px 0px inset, rgba(111, 111, 111, 0.255) 0px 0px 0px 0.5px inset, rgba(0, 0, 0, 0.18) 0px 1px 2px 0px, rgba(0, 0, 0, 0.18) 0px 2px 6px -2px; text ui-sans-serif 13/19.5 500, rgba(250, 250, 250, 0.7) `dark.control.fg.default`; transition color 0.2s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), fill 0.2s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.2s cubic-bezier(0.4, 0, 0.2, 1); layers ::before rgba(0, 0, 0, 0) 0px rgba(255, 255, 255, 0.85) 0px 1px 0px 0px inset, rgba(0, 0, 0, 0.06) 0px -1px 0px 0px inset 0; ::after rgba(0, 0, 0, 0) 0px none 0 |
| hover | shadow rgba(255, 255, 255, 0.85) 0px 1px 0px 0px inset, rgba(0, 0, 0, 0.06) 0px -1px 0px 0px inset, rgba(0, 0, 0, 0.55) 0px 0px 0px 0.5px, rgba(0, 0, 0, 0.35) 0px 2px 4px 0px, rgba(0, 0, 0, 0.28) 0px 6px 16px 0px; text ui-sans-serif 13/19.5 500, rgba(250, 250, 250, 0.95) `dark.control.fg.hover`; layers ::before rgba(0, 0, 0, 0) 0px rgba(255, 255, 255, 0.85) 0px 1px 0px 0px inset, rgba(0, 0, 0, 0.06) 0px -1px 0px 0px inset 1; ::after rgba(0, 0, 0, 0) 0px none 1 |
| focus-visible | shadow #ffffff 0px 0px 0px 0px, rgba(173, 173, 173, 0.5) 0px 0px 0px 2px, rgba(0, 0, 0, 0.18) 0px 1px 2px 0px, rgba(0, 0, 0, 0.18) 0px 2px 6px -2px |
| pressed | shadow rgba(255, 255, 255, 0.6) 0px 1px 0px 0px inset, rgba(0, 0, 0, 0.06) 0px -1px 0px 0px inset, rgba(0, 0, 0, 0.55) 0px 0px 0px 0.5px, rgba(0, 0, 0, 0.3) 0px 1px 1px 0px; text ui-sans-serif 13/19.5 500, rgba(250, 250, 250, 0.95) `dark.control.fg.hover`; transform translate(0px, 1px); layers ::before rgba(0, 0, 0, 0) 0px rgba(255, 255, 255, 0.85) 0px 1px 0px 0px inset, rgba(0, 0, 0, 0.06) 0px -1px 0px 0px inset 1; ::after rgba(0, 0, 0, 0) 0px none 1 |

![Book a Demo CTA default](components/crops/cta-book-demo-default.png) ![Book a Demo CTA hover](components/crops/cta-book-demo-hover.png) ![Book a Demo CTA focus-visible](components/crops/cta-book-demo-focus-visible.png) ![Book a Demo CTA pressed](components/crops/cta-book-demo-pressed.png)

#### SEO page headline
The /video-collaboration landing-page masthead — one of the SEO/landing surfaces sharing the marketing shell. Read as `seo-h1` on the video-collaboration page.

**Values (default).** size 960 x 105.59; background transparent; text ui-sans-serif 48/52.8 500, #fafafa `dark.fg.1`.

![SEO page headline default](components/crops/seo-h1-default.png)

#### SEO page CTA
The landing page's CTA; measured, never followed. Read as `seo-cta` on the video-collaboration page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 138.77 x 46; padding 12px 24px; border 1px solid transparent; radius 12px; background transparent; image linear-gradient(to top, #adadad `dark.brand.default` 20%, #cacaca `dark.brand.highlight` 80%); shadow rgba(255, 255, 255, 0.85) 0px 1px 0px 0px inset, rgba(0, 0, 0, 0.06) 0px -1px 0px 0px inset, rgba(0, 0, 0, 0.55) 0px 0px 0px 0.5px, rgba(0, 0, 0, 0.35) 0px 1px 2px 0px, rgba(0, 0, 0, 0.22) 0px 4px 12px 0px; text ui-sans-serif 14/20 500, #090909 `dark.brand.fg.default`; transition color 0.28s cubic-bezier(0.23, 1, 0.32, 1), box-shadow 0.28s cubic-bezier(0.23, 1, 0.32, 1), transform 0.15s cubic-bezier(0.23, 1, 0.32, 1); layers ::before rgba(0, 0, 0, 0) 0px rgba(255, 255, 255, 0.85) 0px 1px 0px 0px inset, rgba(0, 0, 0, 0.06) 0px -1px 0px 0px inset 0; ::after rgba(0, 0, 0, 0) 0px none 0 |
| hover | shadow rgba(255, 255, 255, 0.85) 0px 1px 0px 0px inset, rgba(0, 0, 0, 0.06) 0px -1px 0px 0px inset, rgba(0, 0, 0, 0.55) 0px 0px 0px 0.5px, rgba(0, 0, 0, 0.35) 0px 2px 4px 0px, rgba(0, 0, 0, 0.28) 0px 6px 16px 0px; text ui-sans-serif 14/20 500, #242424 `dark.brand.fg.hover`; layers ::before rgba(0, 0, 0, 0) 0px rgba(255, 255, 255, 0.85) 0px 1px 0px 0px inset, rgba(0, 0, 0, 0.06) 0px -1px 0px 0px inset 1; ::after rgba(0, 0, 0, 0) 0px none 1 |
| pressed | shadow rgba(255, 255, 255, 0.6) 0px 1px 0px 0px inset, rgba(0, 0, 0, 0.06) 0px -1px 0px 0px inset, rgba(0, 0, 0, 0.55) 0px 0px 0px 0.5px, rgba(0, 0, 0, 0.3) 0px 1px 1px 0px; text ui-sans-serif 14/20 500, #242424 `dark.brand.fg.hover`; transform translate(0px, 1px); layers ::before rgba(0, 0, 0, 0) 0px rgba(255, 255, 255, 0.85) 0px 1px 0px 0px inset, rgba(0, 0, 0, 0.06) 0px -1px 0px 0px inset 1; ::after rgba(0, 0, 0, 0) 0px none 1 |

![SEO page CTA default](components/crops/seo-cta-default.png) ![SEO page CTA hover](components/crops/seo-cta-hover.png) ![SEO page CTA focus-visible](components/crops/seo-cta-focus-visible.png) ![SEO page CTA pressed](components/crops/seo-cta-pressed.png)

#### Alternative page headline
The /frame-io-alternative landing-page masthead. Read as `seo2-h1` on the frame-io-alternative page.

**Values (default).** size 960 x 105.59; background transparent; text ui-sans-serif 48/52.8 500, #fafafa `dark.fg.1`.

![Alternative page headline default](components/crops/seo2-h1-default.png)

### Marketing demo (pre-rendered product UI)

The interactive Flask workspace mock embedded in the home page — a pre-rendered marketing demo built from the same --ds-* component classes (sidebar 'Open menu', 'Copy Prompt'/'Copy Link' buttons, 'v2 | Context' and 'Feedback | 0' tabs, the 'Version' asset chip, the file list with 'Latest Activity'/'Collapse Group'/'ACME Studios' rows and the 'Anyone with Link' share control). Its controls were measured as painted; only the Version chip was toggled — pointer attempts on the overlay-guarded controls were intercepted and are recorded as unreached.

#### Demo breadcrumb chip
The demo mock's "ACME Studios" breadcrumb chip in the workspace bar; measured as painted. Read as `demo-breadcrumb` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 81.87 x 16.61; background transparent; text ui-sans-serif 14/17.5 400, #a0a0a0 `dark.fg.2.default` |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

![Demo breadcrumb chip default](components/crops/demo-breadcrumb-default.png) ![Demo breadcrumb chip hover](components/crops/demo-breadcrumb-hover.png) ![Demo breadcrumb chip pressed](components/crops/demo-breadcrumb-pressed.png)

#### Demo context tab
The demo's "v2 / Context" tab, painted as the active tab; measured as painted. Read as `demo-tab-context` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 103.97 x 30.38; padding 0px 12px; radius 9999px; background rgba(160, 160, 160, 0.063) `dark.action.bookCallFill`; shadow rgba(173, 173, 173, 0.07) 0px 0.5px 0px 0px inset, rgba(111, 111, 111, 0.255) 0px 0px 0px 0.5px inset, rgba(0, 0, 0, 0.18) 0px 1px 2px 0px, rgba(0, 0, 0, 0.18) 0px 2px 6px -2px; text ui-monospace 12/12 500, #a0a0a0 `dark.fg.2.default`; transition color 0.15s cubic-bezier(0.23, 1, 0.32, 1), transform 0.15s cubic-bezier(0.23, 1, 0.32, 1), opacity 0.15s cubic-bezier(0.23, 1, 0.32, 1), box-shadow 0.15s cubic-bezier(0.23, 1, 0.32, 1); opacity 0.5; layers ::before rgba(0, 0, 0, 0) 0px none 0 |
| pressed | size 71.31 x 30.38; shadow rgba(173, 173, 173, 0.16) 0px 0.5px 0px 0px inset, rgba(111, 111, 111, 0.255) 0px 0px 0px 0.5px inset, rgba(0, 0, 0, 0.18) 0px 1px 1px 0px; text ui-sans-serif 14/20 500, rgba(250, 250, 250, 0.95) `dark.control.fg.hover`; transform translate(0px, 1px); opacity none; layers ::before rgba(0, 0, 0, 0) 0px none 1 |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

![Demo context tab default](components/crops/demo-tab-context-default.png) ![Demo context tab hover](components/crops/demo-tab-context-hover.png) ![Demo context tab pressed](components/crops/demo-tab-context-pressed.png)

#### Demo feedback tab
The demo's "Feedback / 0" tab, painted as inactive; measured as painted. Read as `demo-tab-feedback` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 81.96 x 30.38; padding 0px 12px; radius 9999px; background rgba(160, 160, 160, 0.063) `dark.action.bookCallFill`; shadow rgba(173, 173, 173, 0.07) 0px 0.5px 0px 0px inset, rgba(111, 111, 111, 0.255) 0px 0px 0px 0.5px inset, rgba(0, 0, 0, 0.18) 0px 1px 2px 0px, rgba(0, 0, 0, 0.18) 0px 2px 6px -2px; text ui-sans-serif 14/20 500, #868686 `dark.chip.fg.unselected`; transition color 0.15s cubic-bezier(0.23, 1, 0.32, 1), transform 0.15s cubic-bezier(0.23, 1, 0.32, 1), opacity 0.15s cubic-bezier(0.23, 1, 0.32, 1), box-shadow 0.15s cubic-bezier(0.23, 1, 0.32, 1); layers ::before rgba(0, 0, 0, 0) 0px none 0 |
| pressed | shadow rgba(173, 173, 173, 0.16) 0px 0.5px 0px 0px inset, rgba(111, 111, 111, 0.255) 0px 0px 0px 0.5px inset, rgba(0, 0, 0, 0.18) 0px 1px 1px 0px; text ui-sans-serif 14/20 500, rgba(250, 250, 250, 0.95) `dark.control.fg.hover`; transform translate(0px, 1px); layers ::before rgba(0, 0, 0, 0) 0px none 1 |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

![Demo feedback tab default](components/crops/demo-tab-feedback-default.png) ![Demo feedback tab hover](components/crops/demo-tab-feedback-hover.png) ![Demo feedback tab pressed](components/crops/demo-tab-feedback-pressed.png)

#### Demo feedback composer
The demo's "00:00 / Leave Feedback.." composer field, painted with a timestamp chip; measured as painted. Read as `demo-feedback-field` on the home page.

**Values (default).** size 154.5 x 44.31; background transparent; text ui-sans-serif 14/20 400, #6f6f6f `dark.fg.3`; transition opacity 0.2s cubic-bezier(0.4, 0, 0.2, 1).

![Demo feedback composer default](components/crops/demo-feedback-field-default.png)

#### Demo version chip
The demo's "Version 3" chip — the mock asset switcher; measured as painted, toggled once during screenshot capture. Read as `demo-version-chip` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 93.9 x 30.38; padding 0px 6px 0px 12px; radius 9999px; background rgba(160, 160, 160, 0.063) `dark.action.bookCallFill`; shadow rgba(173, 173, 173, 0.07) 0px 0.5px 0px 0px inset, rgba(111, 111, 111, 0.255) 0px 0px 0px 0.5px inset, rgba(0, 0, 0, 0.18) 0px 1px 2px 0px, rgba(0, 0, 0, 0.18) 0px 2px 6px -2px; text ui-sans-serif 14/20 500, rgba(250, 250, 250, 0.7) `dark.control.fg.default`; transition color 0.15s cubic-bezier(0.23, 1, 0.32, 1), transform 0.15s cubic-bezier(0.23, 1, 0.32, 1), opacity 0.15s cubic-bezier(0.23, 1, 0.32, 1), box-shadow 0.15s cubic-bezier(0.23, 1, 0.32, 1); icon 15.19 x 15.19, #a0a0a0 `dark.fg.2.default`; layers ::before rgba(0, 0, 0, 0) 0px none 0 |
| pressed | shadow rgba(173, 173, 173, 0.16) 0px 0.5px 0px 0px inset, rgba(111, 111, 111, 0.255) 0px 0px 0px 0.5px inset, rgba(0, 0, 0, 0.18) 0px 1px 1px 0px; text ui-sans-serif 14/20 500, rgba(250, 250, 250, 0.95) `dark.control.fg.hover`; transform translate(0px, 1px); layers ::before rgba(0, 0, 0, 0) 0px none 1 |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

![Demo version chip default](components/crops/demo-version-chip-default.png) ![Demo version chip pressed](components/crops/demo-version-chip-pressed.png)

#### Demo "Copy Link" button
The demo's "Copy Link to Folder" / "Copy Link" control; measured, never pressed. Read as `demo-copy-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 103.97 x 30.38; padding 0px 12px; radius 20px 4px 4px 20px; background rgba(160, 160, 160, 0.063) `dark.action.bookCallFill`; shadow rgba(173, 173, 173, 0.07) 0px 0.5px 0px 0px inset, rgba(111, 111, 111, 0.255) 0px 0px 0px 0.5px inset, rgba(0, 0, 0, 0.18) 0px 1px 2px 0px, rgba(0, 0, 0, 0.18) 0px 2px 6px -2px; text ui-sans-serif 14/20 500, rgba(250, 250, 250, 0.7) `dark.control.fg.default`; transition color 0.15s cubic-bezier(0.23, 1, 0.32, 1), transform 0.15s cubic-bezier(0.23, 1, 0.32, 1), opacity 0.15s cubic-bezier(0.23, 1, 0.32, 1), box-shadow 0.15s cubic-bezier(0.23, 1, 0.32, 1); icon 15.19 x 15.19, rgba(250, 250, 250, 0.7) `dark.control.fg.default`; layers ::before rgba(0, 0, 0, 0) 0px none 0 |
| pressed | shadow rgba(173, 173, 173, 0.16) 0px 0.5px 0px 0px inset, rgba(111, 111, 111, 0.255) 0px 0px 0px 0.5px inset, rgba(0, 0, 0, 0.18) 0px 1px 1px 0px; text ui-sans-serif 14/20 500, rgba(250, 250, 250, 0.95) `dark.control.fg.hover`; transform translate(0px, 1px); icon 15.19 x 15.19, rgba(250, 250, 250, 0.95) `dark.control.fg.hover`; layers ::before rgba(0, 0, 0, 0) 0px none 1 |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

![Demo "Copy Link" button default](components/crops/demo-copy-link-default.png) ![Demo "Copy Link" button hover](components/crops/demo-copy-link-hover.png) ![Demo "Copy Link" button pressed](components/crops/demo-copy-link-pressed.png)

#### Demo table header
The demo file list's "Latest Activity" column header; measured as painted. Read as `demo-th` on the home page.

**Values (default).** size 137.95 x 38.45; padding 0px 12px; radius 9999px; background rgba(160, 160, 160, 0.063) `dark.action.bookCallFill`; shadow rgba(173, 173, 173, 0.07) 0px 0.5px 0px 0px inset, rgba(111, 111, 111, 0.255) 0px 0px 0px 0.5px inset, rgba(0, 0, 0, 0.18) 0px 1px 2px 0px, rgba(0, 0, 0, 0.18) 0px 2px 6px -2px; text ui-sans-serif 14/20 500, rgba(250, 250, 250, 0.7) `dark.control.fg.default`; transition color 0.15s cubic-bezier(0.23, 1, 0.32, 1), transform 0.15s cubic-bezier(0.23, 1, 0.32, 1), opacity 0.15s cubic-bezier(0.23, 1, 0.32, 1), box-shadow 0.15s cubic-bezier(0.23, 1, 0.32, 1); layers ::before rgba(0, 0, 0, 0) 0px none 0.

![Demo table header default](components/crops/demo-th-default.png)

#### Demo "ACME Studios" share button
The "ACME Studios" button in the demo's rendered share popover ("Who can edit"); measured, never pressed. Read as `demo-acme-btn` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 166.99 x 33.65; padding 0px 10px; radius 9999px; background rgba(160, 160, 160, 0.063) `dark.action.bookCallFill`; shadow rgba(173, 173, 173, 0.07) 0px 0.5px 0px 0px inset, rgba(111, 111, 111, 0.255) 0px 0px 0px 0.5px inset, rgba(0, 0, 0, 0.18) 0px 1px 2px 0px, rgba(0, 0, 0, 0.18) 0px 2px 6px -2px; text ui-sans-serif 13/19.5 400, rgba(250, 250, 250, 0.7) `dark.control.fg.default`; transition color 0.15s cubic-bezier(0.23, 1, 0.32, 1), transform 0.15s cubic-bezier(0.23, 1, 0.32, 1), opacity 0.15s cubic-bezier(0.23, 1, 0.32, 1), box-shadow 0.15s cubic-bezier(0.23, 1, 0.32, 1); icon 8.41 x 8.41, #a0a0a0 `dark.fg.2.default`; layers ::before rgba(0, 0, 0, 0) 0px none 0 |
| pressed | shadow rgba(173, 173, 173, 0.16) 0px 0.5px 0px 0px inset, rgba(111, 111, 111, 0.255) 0px 0px 0px 0.5px inset, rgba(0, 0, 0, 0.18) 0px 1px 1px 0px; text ui-sans-serif 13/19.5 400, rgba(250, 250, 250, 0.95) `dark.control.fg.hover`; transform translate(0px, 1px); layers ::before rgba(0, 0, 0, 0) 0px none 1 |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

![Demo "ACME Studios" share button default](components/crops/demo-acme-btn-default.png) ![Demo "ACME Studios" share button hover](components/crops/demo-acme-btn-hover.png) ![Demo "ACME Studios" share button pressed](components/crops/demo-acme-btn-pressed.png)

#### Demo share-scope control
The demo's "Anyone with Link" share-scope control; measured as painted, never opened (an earlier pointer attempt was intercepted by the mock overlay). Read as `demo-share-scope` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 191.55 x 33.65; padding 0px 10px; radius 9999px; background rgba(160, 160, 160, 0.063) `dark.action.bookCallFill`; shadow rgba(173, 173, 173, 0.07) 0px 0.5px 0px 0px inset, rgba(111, 111, 111, 0.255) 0px 0px 0px 0.5px inset, rgba(0, 0, 0, 0.18) 0px 1px 2px 0px, rgba(0, 0, 0, 0.18) 0px 2px 6px -2px; text ui-sans-serif 13/19.5 400, rgba(250, 250, 250, 0.7) `dark.control.fg.default`; transition color 0.15s cubic-bezier(0.23, 1, 0.32, 1), transform 0.15s cubic-bezier(0.23, 1, 0.32, 1), opacity 0.15s cubic-bezier(0.23, 1, 0.32, 1), box-shadow 0.15s cubic-bezier(0.23, 1, 0.32, 1); icon 19.23 x 19.23, #a0a0a0 `dark.fg.2.default`; layers ::before rgba(0, 0, 0, 0) 0px none 0 |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

![Demo share-scope control default](components/crops/demo-share-scope-default.png) ![Demo share-scope control hover](components/crops/demo-share-scope-hover.png)

#### Demo share popover
The demo mock's painted share popover (bg-surface-3, element-border, shadow-popover): "Who can view / Anyone with Link / Who can edit" — a painted mock state, measured as painted. Read as `demo-share-popover` on the home page.

**Values (default).** size 406.16 x 57.68; padding 10px 10px 10px 20px; background transparent; text ui-sans-serif 13/20 400, #fafafa `dark.fg.1`; icon 19.23 x 19.23, #a0a0a0 `dark.fg.2.default`; layers button.ds-focus:ring-2.ds-focus:ring-focus-ring 191.5x33.6 rgba(160, 160, 160, 0.063) rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(173, 173, 173, 0.07) 0px 0.5px 0px 0px inset, rgba(111, 111, 111, 0.255) 0px 0px 0px 0.5px inset, rgba(0, 0, 0, 0.18) 0px 1px 2px 0px, rgba(0, 0, 0, 0.18) 0px 2px 6px -2px 9999px; button::before.ds-focus:ring-2.ds-focus:ring-focus-ring 159.406pxx28px 9999px.

Child layers that carry the look: button 191.5x33.6 background rgba(160, 160, 160, 0.063) `dark.action.bookCallFill` radius 9999px shadow transparent 0px 0px 0px 0px, rgba(173, 173, 173, 0.07) 0px 0.5px 0px 0px inset, rgba(111, 111, 111, 0.255) 0px 0px 0px 0.5px inset, rgba(0, 0, 0, 0.18) `dark.shadow.color.raised` 0px 1px 2px 0px, rgba(0, 0, 0, 0.18) `dark.shadow.color.raised` 0px 2px 6px -2px; button::before 159.406pxx28px image radial-gradient(90px at 50% 50%, rgba(250, 250, 250, 0.06) `dark.control.light.default`, t radius 9999px.

![Demo share popover default](components/crops/demo-share-popover-default.png)

#### Demo "Close" button
A "Close" button in the demo mock's dialog surface; measured, never pressed. Read as `demo-close` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 62.09 x 22.71; padding 0px 10px; radius 9999px; background #121212 `dark.surface.1`; image linear-gradient(rgba(160, 160, 160, 0.063) `dark.action.bookCallFill`, rgba(160, 160, 160, 0.063) `dark.action.bookCallFill`), none; shadow rgba(173, 173, 173, 0.07) 0px 0.5px 0px 0px inset, rgba(111, 111, 111, 0.255) 0px 0px 0px 0.5px inset, rgba(0, 0, 0, 0.18) 0px 1px 2px 0px, rgba(0, 0, 0, 0.18) 0px 2px 6px -2px; text ui-sans-serif 14/20 400, rgba(250, 250, 250, 0.7) `dark.control.fg.default`; transition color 0.15s cubic-bezier(0.23, 1, 0.32, 1), transform 0.15s cubic-bezier(0.23, 1, 0.32, 1), opacity 0.15s cubic-bezier(0.23, 1, 0.32, 1), box-shadow 0.15s cubic-bezier(0.23, 1, 0.32, 1); icon 12.17 x 12.17, rgba(250, 250, 250, 0.7) `dark.control.fg.default`; layers ::before rgba(0, 0, 0, 0) 0px none 0 |
| pressed | shadow rgba(173, 173, 173, 0.16) 0px 0.5px 0px 0px inset, rgba(111, 111, 111, 0.255) 0px 0px 0px 0.5px inset, rgba(0, 0, 0, 0.18) 0px 1px 1px 0px; text ui-sans-serif 14/20 400, rgba(250, 250, 250, 0.95) `dark.control.fg.hover`; transform translate(0px, 1px); icon 12.17 x 12.17, rgba(250, 250, 250, 0.95) `dark.control.fg.hover`; layers ::before rgba(0, 0, 0, 0) 0px none 1 |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

![Demo "Close" button default](components/crops/demo-close-default.png) ![Demo "Close" button hover](components/crops/demo-close-hover.png) ![Demo "Close" button pressed](components/crops/demo-close-pressed.png)

### Pricing

The /pricing grid: Free, Pro and Organization plan cards with Get Started / Book Call, the billing switch ('Billed yearly' on, $15/member/mo — 'Billed quarterly' off, $35/member/mo), the Features table and the FAQs accordion. The switch and one FAQ row were toggled — local UI toggles — and the switch was toggled back.

#### Pricing headline
"Pricing" — the /pricing masthead. Read as `price-h1` on the pricing page.

**Values (default).** size 896 x 46; padding 0px 20px; background transparent; text ui-sans-serif 40/46 500, #fafafa `dark.fg.1`.

![Pricing headline default](components/crops/price-h1-default.png)

#### Billing switch
The plan billing switch beside the plan cards — labelled "Billed yearly" when on ($15/member/mo) and "Billed quarterly" when off ($35/member/mo); the off state was measured after toggling it — a local UI toggle — then toggled back. Read as `billing-switch` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 36 x 20; border 2px solid transparent; radius 9999px; background #fafafa `dark.fg.1`; text ui-sans-serif 14/20 400, #a0a0a0 `dark.fg.2.default`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| focus-visible | shadow #0c0c0c 0px 0px 0px 2px, #adadad 0px 0px 0px 4px |
| off | background rgba(250, 250, 250, 0.086) |

![Billing switch default](components/crops/billing-switch-default.png) ![Billing switch hover](components/crops/billing-switch-hover.png) ![Billing switch focus-visible](components/crops/billing-switch-focus-visible.png) ![Billing switch pressed](components/crops/billing-switch-pressed.png) ![Billing switch off](components/crops/billing-switch-off.png)

#### Get Started button
A plan card's "Get Started" button; measured, never followed (it would start a sign-up flow). Read as `plan-cta` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 248 x 40; padding 0px 16px; border 1px solid transparent; radius 9999px; background transparent; image linear-gradient(to top, #adadad `dark.brand.default` 20%, #cacaca `dark.brand.highlight` 80%); shadow rgba(255, 255, 255, 0.85) 0px 1px 0px 0px inset, rgba(0, 0, 0, 0.06) 0px -1px 0px 0px inset, rgba(0, 0, 0, 0.55) 0px 0px 0px 0.5px, rgba(0, 0, 0, 0.35) 0px 1px 2px 0px, rgba(0, 0, 0, 0.22) 0px 4px 12px 0px; text ui-sans-serif 14/20 500, #090909 `dark.brand.fg.default`; transition color 0.28s cubic-bezier(0.23, 1, 0.32, 1), box-shadow 0.28s cubic-bezier(0.23, 1, 0.32, 1), transform 0.15s cubic-bezier(0.23, 1, 0.32, 1); layers ::before rgba(0, 0, 0, 0) 0px rgba(255, 255, 255, 0.85) 0px 1px 0px 0px inset, rgba(0, 0, 0, 0.06) 0px -1px 0px 0px inset 0; ::after rgba(0, 0, 0, 0) 0px none 0 |
| hover | shadow rgba(255, 255, 255, 0.85) 0px 1px 0px 0px inset, rgba(0, 0, 0, 0.06) 0px -1px 0px 0px inset, rgba(0, 0, 0, 0.55) 0px 0px 0px 0.5px, rgba(0, 0, 0, 0.35) 0px 2px 4px 0px, rgba(0, 0, 0, 0.28) 0px 6px 16px 0px; text ui-sans-serif 14/20 500, #242424 `dark.brand.fg.hover`; layers ::before rgba(0, 0, 0, 0) 0px rgba(255, 255, 255, 0.85) 0px 1px 0px 0px inset, rgba(0, 0, 0, 0.06) 0px -1px 0px 0px inset 1; ::after rgba(0, 0, 0, 0) 0px none 1 |
| pressed | shadow rgba(255, 255, 255, 0.6) 0px 1px 0px 0px inset, rgba(0, 0, 0, 0.06) 0px -1px 0px 0px inset, rgba(0, 0, 0, 0.55) 0px 0px 0px 0.5px, rgba(0, 0, 0, 0.3) 0px 1px 1px 0px; text ui-sans-serif 14/20 500, #242424 `dark.brand.fg.hover`; transform translate(0px, 1px); layers ::before rgba(0, 0, 0, 0) 0px rgba(255, 255, 255, 0.85) 0px 1px 0px 0px inset, rgba(0, 0, 0, 0.06) 0px -1px 0px 0px inset 1; ::after rgba(0, 0, 0, 0) 0px none 1 |

![Get Started button default](components/crops/plan-cta-default.png) ![Get Started button hover](components/crops/plan-cta-hover.png) ![Get Started button focus-visible](components/crops/plan-cta-focus-visible.png) ![Get Started button pressed](components/crops/plan-cta-pressed.png)

#### Book Call button
A plan card's "Book Call" button; measured, never followed (external scheduler). Read as `book-call` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 248 x 40; padding 0px 16px; radius 9999px; background rgba(160, 160, 160, 0.063) `dark.action.bookCallFill`; shadow rgba(173, 173, 173, 0.07) 0px 0.5px 0px 0px inset, rgba(111, 111, 111, 0.255) 0px 0px 0px 0.5px inset, rgba(0, 0, 0, 0.18) 0px 1px 2px 0px, rgba(0, 0, 0, 0.18) 0px 2px 6px -2px; text ui-sans-serif 14/20 500, rgba(250, 250, 250, 0.7) `dark.control.fg.default`; transition color 0.15s cubic-bezier(0.23, 1, 0.32, 1), transform 0.15s cubic-bezier(0.23, 1, 0.32, 1), opacity 0.15s cubic-bezier(0.23, 1, 0.32, 1), box-shadow 0.15s cubic-bezier(0.23, 1, 0.32, 1); layers ::before rgba(0, 0, 0, 0) 0px none 0 |
| hover | shadow rgba(173, 173, 173, 0.16) 0px 0.5px 0px 0px inset, rgba(111, 111, 111, 0.255) 0px 0px 0px 0.5px inset, rgba(0, 0, 0, 0.18) 0px 1px 2px 0px, rgba(0, 0, 0, 0.18) 0px 2px 6px -2px; text ui-sans-serif 14/20 500, rgba(250, 250, 250, 0.95) `dark.control.fg.hover`; layers ::before rgba(0, 0, 0, 0) 0px none 1 |
| pressed | shadow rgba(173, 173, 173, 0.16) 0px 0.5px 0px 0px inset, rgba(111, 111, 111, 0.255) 0px 0px 0px 0.5px inset, rgba(0, 0, 0, 0.18) 0px 1px 1px 0px; text ui-sans-serif 14/20 500, rgba(250, 250, 250, 0.95) `dark.control.fg.hover`; transform translate(0px, 1px); layers ::before rgba(0, 0, 0, 0) 0px none 1 |

![Book Call button default](components/crops/book-call-default.png) ![Book Call button hover](components/crops/book-call-hover.png) ![Book Call button focus-visible](components/crops/book-call-focus-visible.png) ![Book Call button pressed](components/crops/book-call-pressed.png)

#### FAQ accordion
A question row in the /pricing FAQs accordion ("What is the storage limit and what are download windows?"); the opened state was measured after its own toggle — aria-expanded had to stay true. Read as `faq-acc` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, focus-visible, pressed, opened) | size 896 x 62.5; padding 20px 0px; background transparent; text ui-sans-serif 15/22.5 500, #fafafa `dark.fg.1`; transition all 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 16 x 16, #fafafa `dark.fg.1` |

![FAQ accordion default](components/crops/faq-acc-default.png) ![FAQ accordion hover](components/crops/faq-acc-hover.png) ![FAQ accordion focus-visible](components/crops/faq-acc-focus-visible.png) ![FAQ accordion pressed](components/crops/faq-acc-pressed.png) ![FAQ accordion opened](components/crops/faq-acc-opened.png)

### Docs and about

/mcp — the Flask MCP Server docs (Quick start, connect, tools, data handling) with code blocks and the external 'Add to Cursor' install link — and /about with its social/mailto links.

#### Docs headline
"Flask MCP Server" — the /mcp documentation masthead. Read as `docs-h1` on the mcp page.

**Values (default).** size 848 x 36; background transparent; text ui-sans-serif 30/36 700, #fafafa `dark.fg.1`.

![Docs headline default](components/crops/docs-h1-default.png)

#### Code block
A command/code block in the MCP docs (install and tool snippets); measured as painted, never run. Read as `docs-code` on the mcp page.

**Values (default).** size 172.83 x 18; background transparent; text ui-monospace 16/24 400, #a0a0a0 `dark.fg.2.default`.

![Code block default](components/crops/docs-code-default.png)

#### Add to Cursor link
The "Add to Cursor" MCP-install link; an external install URL, measured, never followed. Read as `docs-cursor` on the mcp page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, focus-visible, pressed) | size 104.25 x 22; background transparent; text ui-sans-serif 16/24 400, #fafafa `dark.fg.1` |

![Add to Cursor link default](components/crops/docs-cursor-default.png) ![Add to Cursor link hover](components/crops/docs-cursor-hover.png) ![Add to Cursor link focus-visible](components/crops/docs-cursor-focus-visible.png) ![Add to Cursor link pressed](components/crops/docs-cursor-pressed.png)

#### Docs anchor link
An in-page anchor link in the MCP docs; measured, never followed. Read as `docs-anchor` on the mcp page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 71.48 x 19; background transparent; text ui-sans-serif 14/20 400, #a0a0a0 `dark.fg.2.default`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover, pressed | text ui-sans-serif 14/20 400, #fafafa `dark.fg.1` |

![Docs anchor link default](components/crops/docs-anchor-default.png) ![Docs anchor link hover](components/crops/docs-anchor-hover.png) ![Docs anchor link focus-visible](components/crops/docs-anchor-focus-visible.png) ![Docs anchor link pressed](components/crops/docs-anchor-pressed.png)

#### About headline
"About" — the /about masthead. Read as `about-h1` on the about page.

**Values (default).** size 688 x 46; background transparent; text ui-sans-serif 40/46 500, #fafafa `dark.fg.1`.

![About headline default](components/crops/about-h1-default.png)

#### About link
An external/social link on /about (YouTube show, DMs, hello@flask.do); measured, never followed. Read as `about-link` on the about page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 118 x 33; background transparent; text Caveat 26/39 400, #fafafa `dark.fg.1`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover, pressed | text Caveat 26/39 400, #a0a0a0 `dark.fg.2.default` |

![About link default](components/crops/about-link-default.png) ![About link hover](components/crops/about-link-hover.png) ![About link focus-visible](components/crops/about-link-focus-visible.png) ![About link pressed](components/crops/about-link-pressed.png)

### Security and legal

/security ('Security: How Flask Protects Your Data'), plus the /privacy-policy and /terms-of-service pages captured as screenshots only.

#### Security headline
"Security" — the /security masthead ("Security: How Flask Protects Your Data"). Read as `sec-h1` on the security page.

**Values (default).** size 848 x 45; background transparent; text ui-sans-serif 36/45 700, #fafafa `dark.fg.1`.

![Security headline default](components/crops/sec-h1-default.png)

### Login (signed-out)

/login — the sign-in card ('Sign in to Flask') with Continue with Google, Continue with Email and the e-mail field. Measured and typed into then cleared, never submitted; /home redirects here, so every post-login surface is out of reach.

#### Login panel
The sign-in card on /login: "Sign in to Flask" with Continue with Google and Continue with Email plus the e-mail field. Nothing was submitted. Read as `login-panel` on the login page.

**Values (default).** size 288 x 318; background transparent; text ui-sans-serif 14/20 400, #a0a0a0 `dark.fg.2.default`; icon 72 x 24, #fafafa `dark.fg.1`; layers button.ds-focus:ring-2.ds-focus:ring-focus-ring 288.0x44.0 T:1px solid rgba(0, 0, 0, 0) / R:1px solid rgba(0, 0, 0, 0) / B:1px solid rgba(0, 0, 0, 0) / L:1px solid rgba(0, 0, 0, 0) rgba(255, 255, 255, 0.85) 0px 1px 0px 0px inset, rgba(0, 0, 0, 0.06) 0px -1px 0px 0px inset, rgba(0, 0, 0, 0.55) 0px 0px 0px 0.5px, rgba(0, 0, 0, 0.35) 0px 1px 2px 0px, rgba(0, 0, 0, 0.22) 0px 4px 12px 0px 9999px; butto.

Child layers that carry the look: button 288x44 image linear-gradient(to top, #adadad `dark.brand.default` 20%, #cacaca `dark.brand.highlight` 8 border 1px solid transparent radius 9999px shadow rgba(255, 255, 255, 0.85) `dark.primary.highlight.default` 0px 1px 0px 0px inset, rgba(0, 0, 0, 0.06) `dark.primary.shade` 0px -1px 0px 0px inset, rgba(0, 0, 0, 0.55) `dark.primary.ring` 0px 0px 0px 0.5px, rgba(0, 0, 0, 0.35) `dark.shadow.color.contact` 0px 1px 2px 0px, rgba(0, 0, 0, 0.22) `dark.shadow.color.ambient` 0px 4px 12px 0px; button::before 286pxx42px image radial-gradient(55% 40% at 28% 108%, rgba(209, 93, 255, 0.3) `dark.primary.glow.1`, transp radius 9999px shadow rgba(255, 255, 255, 0.85) `dark.primary.highlight.default` 0px 1px 0px 0px inset, rgba(0, 0, 0, 0.06) `dark.primary.shade` 0px -1px 0px 0px inset; button::after 286pxx42px image linear-gradient(90deg, #d15dff `dark.flair.1`, #f78264 `dark.flair.2` 55%, #efd7a4 `dark.f radius 9999px.

![Login panel default](components/crops/login-panel-default.png)

#### Google SSO button
The "Continue with Google" button; measured, never pressed (it would leave for Google SSO). Read as `login-google` on the login page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 288 x 44; padding 0px 16px; border 1px solid transparent; radius 9999px; background transparent; image linear-gradient(to top, #adadad `dark.brand.default` 20%, #cacaca `dark.brand.highlight` 80%); shadow rgba(255, 255, 255, 0.85) 0px 1px 0px 0px inset, rgba(0, 0, 0, 0.06) 0px -1px 0px 0px inset, rgba(0, 0, 0, 0.55) 0px 0px 0px 0.5px, rgba(0, 0, 0, 0.35) 0px 1px 2px 0px, rgba(0, 0, 0, 0.22) 0px 4px 12px 0px; text ui-sans-serif 14/20 500, #090909 `dark.brand.fg.default`; transition color 0.28s cubic-bezier(0.23, 1, 0.32, 1), box-shadow 0.28s cubic-bezier(0.23, 1, 0.32, 1), transform 0.15s cubic-bezier(0.23, 1, 0.32, 1); icon 16 x 16, #090909 `dark.brand.fg.default`; layers ::before rgba(0, 0, 0, 0) 0px rgba(255, 255, 255, 0.85) 0px 1px 0px 0px inset, rgba(0, 0, 0, 0.06) 0px -1px 0px 0px inset 0; ::after rgba(0, 0, 0, 0) 0px none 0 |
| hover | shadow rgba(255, 255, 255, 0.85) 0px 1px 0px 0px inset, rgba(0, 0, 0, 0.06) 0px -1px 0px 0px inset, rgba(0, 0, 0, 0.55) 0px 0px 0px 0.5px, rgba(0, 0, 0, 0.35) 0px 2px 4px 0px, rgba(0, 0, 0, 0.28) 0px 6px 16px 0px; text ui-sans-serif 14/20 500, #242424 `dark.brand.fg.hover`; icon 16 x 16, #242424 `dark.brand.fg.hover`; layers ::before rgba(0, 0, 0, 0) 0px rgba(255, 255, 255, 0.85) 0px 1px 0px 0px inset, rgba(0, 0, 0, 0.06) 0px -1px 0px 0px inset 1; ::after rgba(0, 0, 0, 0) 0px none 1 |
| focus-visible | shadow #ffffff 0px 0px 0px 0px, rgba(173, 173, 173, 0.5) 0px 0px 0px 2px |
| pressed | shadow rgba(255, 255, 255, 0.6) 0px 1px 0px 0px inset, rgba(0, 0, 0, 0.06) 0px -1px 0px 0px inset, rgba(0, 0, 0, 0.55) 0px 0px 0px 0.5px, rgba(0, 0, 0, 0.3) 0px 1px 1px 0px; text ui-sans-serif 14/20 500, #242424 `dark.brand.fg.hover`; transform translate(0px, 1px); icon 16 x 16, #242424 `dark.brand.fg.hover`; layers ::before rgba(0, 0, 0, 0) 0px rgba(255, 255, 255, 0.85) 0px 1px 0px 0px inset, rgba(0, 0, 0, 0.06) 0px -1px 0px 0px inset 1; ::after rgba(0, 0, 0, 0) 0px none 1 |

![Google SSO button default](components/crops/login-google-default.png) ![Google SSO button hover](components/crops/login-google-hover.png) ![Google SSO button focus-visible](components/crops/login-google-focus-visible.png) ![Google SSO button pressed](components/crops/login-google-pressed.png)

#### Continue with Email button
The "Continue with Email" submit button; its states were measured but the button was never clicked — nothing was submitted. Read as `login-email-btn` on the login page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 288 x 44; radius 9999px; background rgba(160, 160, 160, 0.063) `dark.action.bookCallFill`; shadow rgba(173, 173, 173, 0.07) 0px 0.5px 0px 0px inset, rgba(111, 111, 111, 0.255) 0px 0px 0px 0.5px inset, rgba(0, 0, 0, 0.18) 0px 1px 2px 0px, rgba(0, 0, 0, 0.18) 0px 2px 6px -2px; text ui-sans-serif 14/20 500, rgba(250, 250, 250, 0.7) `dark.control.fg.default`; transition color 0.15s cubic-bezier(0.23, 1, 0.32, 1), transform 0.15s cubic-bezier(0.23, 1, 0.32, 1), opacity 0.15s cubic-bezier(0.23, 1, 0.32, 1), box-shadow 0.15s cubic-bezier(0.23, 1, 0.32, 1); opacity 0.5; icon 16 x 16, rgba(250, 250, 250, 0.7) `dark.control.fg.default`; layers ::before rgba(0, 0, 0, 0) 0px none 0 |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

![Continue with Email button default](components/crops/login-email-btn-default.png) ![Continue with Email button hover](components/crops/login-email-btn-hover.png) ![Continue with Email button pressed](components/crops/login-email-btn-pressed.png)

#### Email field (login)
The e-mail input on the sign-in card (placeholder "han@solo.com"); focused and typed into then cleared — never submitted. Read as `login-email` on the login page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 288 x 44; padding 0px 16px; border 1px solid #282828 `dark.line.2`; radius 9999px; background rgba(250, 250, 250, 0.047) `dark.form.fieldBg`; outline 2px solid transparent, offset 2px; text ui-sans-serif 14/20 400, #fafafa `dark.fg.1`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1); placeholder #505050 `dark.fg.4` |
| focused, filled | border 1px solid #505050 `dark.fg.4`; outline none |

![Email field (login) default](components/crops/login-email-default.png) ![Email field (login) focused](components/crops/login-email-focused.png) ![Email field (login) filled](components/crops/login-email-filled.png)

### Mobile (390 wide)

The phone surface at 390 wide: the logo plus the icon-only 'Open menu' hamburger (no <header> element mounts at this width), its bottom-sheet nav overlay, the hero and CTA.

#### Mobile top chrome
The phone top chrome at 390 wide: the Flask logo link plus the hamburger — the page mounts no <header> element at this width. Read as `m-topbar` on the home page at 390 wide.

**Values (default).** size 64 x 32; padding 0px 8px; radius 12px; background transparent; text ui-sans-serif 16/24 400, #fafafa `dark.fg.1`; transition transform 0.15s cubic-bezier(0.23, 1, 0.32, 1); icon 48 x 16, #fafafa `dark.fg.1`.

![Mobile top chrome default](components/crops/m-topbar-default.png)

#### Mobile menu button
The icon-only "Open menu" hamburger (md:hidden — mobile only) — a local UI toggle; the opened state was measured after activating it. Read as `m-menu-btn` on the home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed, opened) | size 38 x 38; padding 8px; background transparent; outline 2px solid transparent, offset 2px; text ui-sans-serif 16/24 400, #a0a0a0 `dark.fg.2.default`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 22 x 22, #a0a0a0 `dark.fg.2.default`; layers button.md:hidden.flex 38.0x38.0 2px solid rgba(0, 0, 0, 0) offset 2px |
| focus-visible | outline none; layers none |

Child layers that carry the look: button 38x38.

![Mobile menu button default](components/crops/m-menu-btn-default.png) ![Mobile menu button hover](components/crops/m-menu-btn-hover.png) ![Mobile menu button focus-visible](components/crops/m-menu-btn-focus-visible.png) ![Mobile menu button pressed](components/crops/m-menu-btn-pressed.png) ![Mobile menu button opened](components/crops/m-menu-btn-opened.png)

#### Mobile nav overlay
The nav layer opened by the "Open menu" button; its links were never followed. Read as `m-drawer` on the home page at 390 wide.

**Values (default).** size 366 x 126; padding 4px 6px 8px 6px; border T: 1px solid #2b2b2b `dark.line.edge`; R: 1px solid #282828 `dark.line.2`; B: 1px solid #282828 `dark.line.2`; L: 1px solid #282828 `dark.line.2`; radius 16px; background #1f1f1f `dark.surface.3`; shadow rgba(0, 0, 0, 0.4) 0px 2px 8px -2px, rgba(0, 0, 0, 0.5) 0px 16px 40px -8px; text ui-sans-serif 15/22.5 400, #fafafa `dark.fg.1`.

![Mobile nav overlay default](components/crops/m-drawer-default.png)

#### Mobile hero headline
The masthead at 390 wide. Read as `m-hero-h1` on the home page at 390 wide.

**Values (default).** size 342 x 142.55; background transparent; text ui-sans-serif 44/47.52 500, #fafafa `dark.fg.1`.

![Mobile hero headline default](components/crops/m-hero-h1-default.png)

#### Mobile hero CTA
The hero CTA at 390 wide; measured, never followed. Read as `m-hero-cta` on the home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 127.84 x 40; padding 0px 12px 0px 16px; border 1px solid transparent; radius 9999px; background transparent; image linear-gradient(to top, #adadad `dark.brand.default` 20%, #cacaca `dark.brand.highlight` 80%); shadow rgba(255, 255, 255, 0.85) 0px 1px 0px 0px inset, rgba(0, 0, 0, 0.06) 0px -1px 0px 0px inset, rgba(0, 0, 0, 0.55) 0px 0px 0px 0.5px, rgba(0, 0, 0, 0.35) 0px 1px 2px 0px, rgba(0, 0, 0, 0.22) 0px 4px 12px 0px; text ui-sans-serif 15/22.5 500, #090909 `dark.brand.fg.default`; transition color 0.2s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), fill 0.2s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.2s cubic-bezier(0.4, 0, 0.2, 1); icon 16 x 16, #090909 `dark.brand.fg.default`; layers ::before rgba(0, 0, 0, 0) 0px rgba(255, 255, 255, 0.85) 0px 1px 0px 0px inset, rgba(0, 0, 0, 0.06) 0px -1px 0px 0px inset 0; ::after rgba(0, 0, 0, 0) 0px none 0 |
| hover | shadow rgba(255, 255, 255, 0.85) 0px 1px 0px 0px inset, rgba(0, 0, 0, 0.06) 0px -1px 0px 0px inset, rgba(0, 0, 0, 0.55) 0px 0px 0px 0.5px, rgba(0, 0, 0, 0.35) 0px 2px 4px 0px, rgba(0, 0, 0, 0.28) 0px 6px 16px 0px; text ui-sans-serif 15/22.5 500, #242424 `dark.brand.fg.hover`; icon 16 x 16, #242424 `dark.brand.fg.hover`; layers ::before rgba(0, 0, 0, 0) 0px rgba(255, 255, 255, 0.85) 0px 1px 0px 0px inset, rgba(0, 0, 0, 0.06) 0px -1px 0px 0px inset 1; ::after rgba(0, 0, 0, 0) 0px none 1 |
| focus-visible | shadow #ffffff 0px 0px 0px 0px, rgba(173, 173, 173, 0.5) 0px 0px 0px 2px |
| pressed | shadow rgba(255, 255, 255, 0.6) 0px 1px 0px 0px inset, rgba(0, 0, 0, 0.06) 0px -1px 0px 0px inset, rgba(0, 0, 0, 0.55) 0px 0px 0px 0.5px, rgba(0, 0, 0, 0.3) 0px 1px 1px 0px; text ui-sans-serif 15/22.5 500, #242424 `dark.brand.fg.hover`; transform translate(0px, 1px); icon 16 x 16, #242424 `dark.brand.fg.hover`; layers ::before rgba(0, 0, 0, 0) 0px rgba(255, 255, 255, 0.85) 0px 1px 0px 0px inset, rgba(0, 0, 0, 0.06) 0px -1px 0px 0px inset 1; ::after rgba(0, 0, 0, 0) 0px none 1 |

![Mobile hero CTA default](components/crops/m-hero-cta-default.png) ![Mobile hero CTA hover](components/crops/m-hero-cta-hover.png) ![Mobile hero CTA focus-visible](components/crops/m-hero-cta-focus-visible.png) ![Mobile hero CTA pressed](components/crops/m-hero-cta-pressed.png)

## Icons

No standalone SVG icon set was lifted on this pass; the icons in the crops and screenshots (the Flask mark, the demo mock's glyphs, social glyphs) are the product's artwork. Declared under layoutGaps in the catalog entry.

| Icon | Rendered sizes | View box | Style | Seen on | Next to |
|---|---|---|---|---|---|

## Gaps

### The signed-in product

Flask's product is the video review workspace: the canvas, upload, feedback threads, folders, versions and sharing — every surface after Sign Up needs an account and was never reached. /home redirects to /login?returnUrl=%2Fhome, so /login is the only app surface a signed-out visitor sees, and it was measured as a form, never submitted. The Flask workspace embedded in the home page is a pre-rendered marketing demo of the product, not the product itself.

### Pages

- **The account.** The workspace and every post-login surface (uploads, feedback threads, folders, versions, sharing, settings, MCP-authenticated routes) was never reached — /home redirects to /login; the /login form was measured as a form and never submitted; 'Continue with Google' and 'Continue with Email' were never pressed.
- **The demo mock's deeper states.** The home page's product demo is a pre-rendered marketing mock: pointer attempts on 'Open menu', 'Anyone with Link', 'ACME Studios' and related controls were intercepted by the mock's overlay or left no painted state, so their opened/menu states are uncaptured — only the 'Version' asset chip was toggled.
- **Forms.** The login e-mail field was measured at rest and typed into then cleared — nothing was sent; what a submission returns is unverified.
- **Legal/SEO pages.** /privacy-policy and /terms-of-service were screenshot-captured only (no component specs); the remaining SEO pages in the sitemap (/flask-vs-frame-io, /frame-io-vs-dropbox-replay, /best-video-review-software, /ai-video-feedback, /video-review-for-ai-agents, /remotion-hyperframes-video-review, /timestamped-video-feedback) are the same landing template, uncaptured.
- **External actions.** 'Add to Cursor' carries a base64 MCP configuration and would install into an editor; the Book Demo/Call buttons open external schedulers; mailto/social links leave the site — all were measured, never followed.

### States

- **Pressed** was forced with DevTools on every control, so a state a script adds on mousedown (if any) is missing.
- **Disabled, error, loading, validation and success states** were not seen on the public surface — the login form was never submitted, and no public surface displays them.
- **The billing switch** on /pricing was toggled to its 'Billed quarterly' view ($35/member/mo) and back; the quarterly view is captured, the yearly view is the resting state.
- **Hover and focus states** on the demo mock's overlay-guarded controls are partially covered where the overlay intercepted the pointer.

### Themes

Every public flask.do page paints the dark `default` theme — the only --ds-* layer the inline ds-theme stylesheet declares on `:root`, resolved with `color-scheme: dark`. The site ships no light variant and no theme toggle exists; tokens.json therefore carries a single `dark` set. Most --ds-* colours are declared as rgb channel lists ("250 250 250 / 0.18") — declared values — while the rgba() they paint is recorded on the measured tokens.

### Fonts

- **System sans.** --ds-font-sans is the ui-sans-serif/system-ui stack — the site loads no self-hosted display face, so the style guide and tokens carry the same system stack the browser paints.

### Screenshots

- The product demo frames, testimonial portraits and photography in the screenshots are the product's published content.
- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files.

### Content left out

- Marketing copy, plan prices, testimonial names and demo asset names are the product's content; only frames and components were measured.
