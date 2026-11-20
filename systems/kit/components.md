# Kit components

The discovery list of every page and view captured, then one entry per component with crops of the real product, and the Gaps. Captured from kit.com on 2026-11-18, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running page. Nothing was signed into, bought or submitted. The log-in form was typed into and cleared. Every link and call to action was measured, never followed.

The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) (32 components, 81 states). The page layouts are described in [patterns.md](patterns.md).

How to read an entry:

- A colour is its value followed by the palette token in [tokens.json](tokens.json) with the same value, when there is one. Text is written family size/line-height weight, then its colour, for example `Inter 15/22.5 600, #23252b`, and is read from the first text node inside the component.
- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example "default (same: focus-visible)". When the root paints nothing, "Child layers" names the first nodes inside it that do.
- Crops are images of the component read from the live page, in [components/crops/](components/crops) (77 files, named `{component}-{state}.png`, at 2x). Screenshots are in [screenshots/](screenshots).

## Discovery list

Screenshots are named `{page}-light-{state}.png`. Every surface paints light. Desktop shots are 1440 x 900 at 1x. `-full` shots are whole pages at 1x. Mobile shots are `mobile-{page}-light-{state}.png`, 780 wide (390 at 2x).

| Surface | URL | Screenshots |
|---|---|---|
| Home | `/` | [default](screenshots/home-light-default.png), [full](screenshots/home-light-full.png), [menu-features](screenshots/home-light-menu-features.png), [menu-use-cases](screenshots/home-light-menu-use-cases.png) |
| Pricing | `/pricing` | [default](screenshots/pricing-light-default.png), [faq-open](screenshots/pricing-light-faq-open.png), [full](screenshots/pricing-light-full.png) |
| Features | `/features` | [default](screenshots/features-light-default.png), [full](screenshots/features-light-full.png), [search-focused](screenshots/features-light-search-focused.png) |
| Email marketing | `/features/email-marketing` | [default](screenshots/features-email-light-default.png), [full](screenshots/features-email-light-full.png) |
| Request a demo | `/request-demo` | [default](screenshots/request-demo-light-default.png), [full](screenshots/request-demo-light-full.png) |
| Compare | `/compare/mailchimp` | [default](screenshots/compare-light-default.png), [full](screenshots/compare-light-full.png) |
| Migrations | `/migrations` |  |
| Brand | `/brand` | [default](screenshots/brand-light-default.png), [full](screenshots/brand-light-full.png) |
| About | `/about` | [default](screenshots/about-light-default.png), [full](screenshots/about-light-full.png) |
| Privacy | `/privacy` | [default](screenshots/privacy-light-default.png) |
| Log in | `app.kit.com/users/login` | [default](screenshots/login-light-default.png) |
| Home, phone | `/` | [default](screenshots/mobile-home-light-default.png), [drawer](screenshots/mobile-home-light-drawer.png), [full](screenshots/mobile-home-light-full.png) |
| Pricing, phone | `/pricing` | [default](screenshots/mobile-pricing-light-default.png), [full](screenshots/mobile-pricing-light-full.png) |
| Features, phone | `/features` | [default](screenshots/mobile-features-light-default.png), [full](screenshots/mobile-features-light-full.png) |
| Log in, phone | `app.kit.com/users/login` | [default](screenshots/mobile-login-light-default.png) |

### Overlays and transient states

| State | Where | How it was reached | Captured |
|---|---|---|---|
| Cookie consent | every page | any consent overlay is hidden, never answered | hidden before every shot and reading |
| Nav menus | every marketing page | clicked the Features and Use Cases buttons | [home-light-menu-features](screenshots/home-light-menu-features.png) |
| FAQ disclosure | /pricing | opened a summary locally | [pricing-light-faq-open](screenshots/pricing-light-faq-open.png) |
| Mobile menu | home, phone width | clicked Toggle mobile menu | [mobile-home-light-drawer](screenshots/mobile-home-light-drawer.png) |
| Log-in fields | app.kit.com/users/login | typed into then cleared. Nothing sent | [login-email](#email-field) |
| Signed-in product | a Kit account | the creator app needs an account | boundary; see Gaps |

## Shared values

Values that apply across entries, from the measurement files.

**Focus.** 13 components were given a real keyboard focus. 5 draw an outline ring: `login-show` (2px solid #1e1e1e `color.soft.black`, offset 2px), `login-submit` (2px solid #1e1e1e `color.soft.black`, offset 2px), `login-forgot` (2px solid #1e1e1e `color.soft.black`, offset 2px), `login-create` (2px solid #1e1e1e `color.soft.black`, offset -2px), `m-menu` (1px auto #e59700, offset 0px). 8 draw a focus ring as a shadow instead: `nav-menu`, `nav-link`, `nav-login`, `nav-trial`, `hero-cta`, `footer-link`, `price-cta`, `price-free`.

**Pressed.** Forced with DevTools (`CSS.forcePseudoState` :active:hover). Nothing a real press would submit was ever pressed.

**Motion.** Transitions measured on the components, by duration.

| Duration | Easing | Property | Where |
|---|---|---|---|
| 0.1s | `cubic-bezier(0.4, 0, 0.2, 1)` | --tw-gradient-from, --tw-gradient-to, --tw-gradient-via, background-color, border-color, color, fill, outline-color, stroke, text-decoration-color | footer-link |
| 0.15s | `cubic-bezier(0.4, 0, 0.2, 1)` | --tw-gradient-from, --tw-gradient-to, --tw-gradient-via, -webkit-backdrop-filter, all, backdrop-filter, background-color, border-color, box-shadow, color, content-visibility, display, fill, filter, opacity, outline-color, overlay, pointer-events, rotate, scale, stroke, text-decoration-color, transform, translate | announce-bar, hero-cta, hero-secondary, login-email, login-forgot, login-show, login-submit, m-nav and more |

**Card shapes.** Default-state values; the entries hold the states.

| Card | Size | Border | Radius | Background | Shadow | Padding |
|---|---|---|---|---|---|---|
| [Nav menu panel](#nav-menu-panel) | 1440 x 287.91 | - | - | #ffffff `color.white` | rgba(0, 0, 0, 0.1) 0px 10px 15px -3px, rgba(0, 0, 0, 0.1) 0px 4px 6px -4px | 0 |

## Components

### Announcement bar

The blue announcement strip above the nav on marketing pages.

#### Announcement bar
The blue announcement strip above the nav ("See Kit’s newest features in action"). Measured, never followed. Read as `announce-bar` on the home page.

**Values (default).** size 1440 x 48; padding 8px 16px; background #44b1ff `color.blue.500`; text Libre Franklin 14/21 600, #1e1e1e `color.soft.black`; transition all 0.15s cubic-bezier(0.4, 0, 0.2, 1).

![Announcement bar default](components/crops/announce-bar-default.png)

### Site chrome

The fixed #mega-nav: wordmark, Features / Use Cases / Resources menus, Pricing, Log in, Request a demo, and the blue Start free trial pill.

#### Site nav
The fixed #mega-nav: wordmark, Features / Use Cases / Resources menus, Pricing, Log in, Request a demo, and the blue Start free trial pill. Read as `mega-nav` on the home page.

**Values (default).** size 1440 x 58; background transparent; text Libre Franklin 14/24.00 600, #f2efe9 `color.warm.white`; transition all 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 53 x 24.53, #1e1e1e `color.soft.black`; layers a.font-sans.transition-all 131.1x34.0 T:1px solid rgb(242, 239, 233) / R:1px solid rgb(242, 239, 233) / B:1px solid rgb(242, 239, 233) / L:1px solid rgb(242, 239, 233) 8px; a.font-sans.transition-all 115.8x32.0 rgb(68, 177, 255) 8px; span 0.0x0.0 rgb(255, 255, 255); span::before 100%x2px rgb(255, 255, 255) 999px; span::after 100%x2px rgb(255, 255, 255) 999px; span 0.0x0.0 rgb(255, 255, 255).

Child layers that carry the look: a 131.1x34 border 1px solid #f2efe9 `color.warm.white` radius 8px; a 115.8x32 background #44b1ff `color.blue.500` radius 8px; span 0x0 background #ffffff `color.white`.

![Site nav default](components/crops/mega-nav-default.png)

#### Wordmark
The Kit wordmark linking home. Read as `nav-logo` on the home page.

**Values (default).** size 53 x 24.53; background transparent; text Libre Franklin 16/24 400, #1e1e1e `color.soft.black`; icon 53 x 24.53, #1e1e1e `color.soft.black`.

![Wordmark default](components/crops/nav-logo-default.png)

#### Nav menu button
The Features button (aria-haspopup) that opens the mega menu. The opened state was measured after clicking it. Menu links were never followed. Read as `nav-menu` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 105.23 x 32; padding 4px 8px; radius 8px; background transparent; text Libre Franklin 14/24.00 600, #f2efe9 `color.warm.white`; transition all 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 20 x 20, #f2efe9 `color.warm.white` |
| hover | background oklab(0.952704 0.000861377 0.0086019 / 0.08) |
| focus-visible | background oklab(0.952704 0.000861377 0.0086019 / 0.08); shadow #44b1ff 0px 0px 0px 2px |
| pressed | background oklab(0.952704 0.000861377 0.0086019 / 0.08) |
| opened | background oklab(0.235024 0.0000107065 0.00000470877 / 0.08); text Libre Franklin 14/24.00 600, #1e1e1e `color.soft.black`; icon 20 x 20, #1e1e1e `color.soft.black` |

![Nav menu button default](components/crops/nav-menu-default.png) ![Nav menu button hover](components/crops/nav-menu-hover.png) ![Nav menu button focus-visible](components/crops/nav-menu-focus-visible.png) ![Nav menu button pressed](components/crops/nav-menu-pressed.png) ![Nav menu button opened](components/crops/nav-menu-opened.png)

#### Nav menu panel
The panel opened by Features. Its links were never followed. Read as `nav-panel` on the home page.

**Values (default).** size 1440 x 287.91; background #ffffff `color.white`; shadow rgba(0, 0, 0, 0.1) 0px 10px 15px -3px, rgba(0, 0, 0, 0.1) 0px 4px 6px -4px; text Libre Franklin 14/20 600, #1e1e1e `color.soft.black`; transition all 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 24 x 24, #1e1e1e `color.soft.black`.

![Nav menu panel default](components/crops/nav-panel-default.png)

#### Nav link
The Pricing link in the nav. Measured, never followed. Read as `nav-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 70.48 x 32; padding 4px 8px; radius 8px; background transparent; text Libre Franklin 14/24.00 600, #f2efe9 `color.warm.white`; transition all 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | background oklab(0.952704 0.000861377 0.0086019 / 0.08) |
| focus-visible | background oklab(0.952704 0.000861377 0.0086019 / 0.08); shadow #44b1ff 0px 0px 0px 2px |
| pressed | background oklab(0.952704 0.000861377 0.0086019 / 0.08) |

![Nav link default](components/crops/nav-link-default.png) ![Nav link hover](components/crops/nav-link-hover.png) ![Nav link focus-visible](components/crops/nav-link-focus-visible.png) ![Nav link pressed](components/crops/nav-link-pressed.png)

#### Log in link
The Log in link to app.kit.com. Measured, never followed. Read as `nav-login` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 63.38 x 32; padding 4px 8px; radius 8px; background transparent; text Libre Franklin 14/24.00 600, #f2efe9 `color.warm.white`; transition all 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | background oklab(0.952704 0.000861377 0.0086019 / 0.08) |
| focus-visible | background oklab(0.952704 0.000861377 0.0086019 / 0.08); shadow #44b1ff 0px 0px 0px 2px |
| pressed | background oklab(0.952704 0.000861377 0.0086019 / 0.08) |

![Log in link default](components/crops/nav-login-default.png) ![Log in link hover](components/crops/nav-login-hover.png) ![Log in link focus-visible](components/crops/nav-login-focus-visible.png) ![Log in link pressed](components/crops/nav-login-pressed.png)

#### Start free trial
The blue Start free trial pill. Measured, never followed. Read as `nav-trial` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 115.8 x 32; padding 4px 8px; radius 8px; background #44b1ff `color.blue.500`; text Libre Franklin 14/24.00 600, #1e1e1e `color.soft.black`; transition all 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | background #a2d1f1 `color.blue.200` |
| focus-visible | shadow #44b1ff 0px 0px 0px 2px |
| pressed | background #a2d1f1 `color.blue.200` |

![Start free trial default](components/crops/nav-trial-default.png) ![Start free trial hover](components/crops/nav-trial-hover.png) ![Start free trial focus-visible](components/crops/nav-trial-focus-visible.png) ![Start free trial pressed](components/crops/nav-trial-pressed.png)

### Home

The home hero on a soft-black band, KitSansFont headline, trial and demo buttons.

#### Hero headline
The home masthead, set in KitSansFont on the dark hero. Read as `hero-h1` on the home page.

**Values (default).** size 768 x 152; background transparent; text KitSansFont 80/76 500, #ffffff `color.white`.

![Hero headline default](components/crops/hero-h1-default.png)

#### Hero CTA
A Start free trial button. Measured, never followed. Read as `hero-cta` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 115.8 x 32; padding 4px 8px; radius 8px; background #44b1ff `color.blue.500`; text Libre Franklin 14/24.00 600, #1e1e1e `color.soft.black`; transition all 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | background #a2d1f1 `color.blue.200` |
| focus-visible | shadow #44b1ff 0px 0px 0px 2px |
| pressed | background #a2d1f1 `color.blue.200` |

![Hero CTA default](components/crops/hero-cta-default.png) ![Hero CTA hover](components/crops/hero-cta-hover.png) ![Hero CTA focus-visible](components/crops/hero-cta-focus-visible.png) ![Hero CTA pressed](components/crops/hero-cta-pressed.png)

#### Request demo button
The Request demo button. Measured, never followed. The demo form sits behind a Chili Piper embed and was not submitted. Read as `hero-secondary` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 118.61 x 32; padding 4px 8px; radius 8px; background #1e1e1e `color.soft.black`; text Libre Franklin 14/24.00 600, #f2efe9 `color.warm.white`; transition all 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| pressed | background #3d3d3d `color.gray.800` |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

![Request demo button default](components/crops/hero-secondary-default.png) ![Request demo button hover](components/crops/hero-secondary-hover.png) ![Request demo button pressed](components/crops/hero-secondary-pressed.png)

### Pricing

The /pricing page: masthead, plan trial links, and the FAQ disclosures.

#### Pricing headline
The /pricing masthead, "Pricing and plans". Read as `price-h1` on the pricing page.

**Values (default).** size 1312 x 64; background transparent; text KitSansFont 64/64 500, #1e1e1e `color.soft.black`.

![Pricing headline default](components/crops/price-h1-default.png)

#### Plan trial button
A plan card "Start 14-day free trial" link. Measured, never followed. Read as `price-cta` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 394.67 x 48; padding 16px; radius 12px; background oklab(0.235024 0.0000107065 0.00000470877 / 0.08); text Libre Franklin 16/16 600, #1e1e1e `color.soft.black`; transition all 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | background oklab(0.235024 0.0000107065 0.00000470877 / 0.16) |
| focus-visible | background oklab(0.235024 0.0000107065 0.00000470877 / 0.16); shadow #44b1ff 0px 0px 0px 2px |
| pressed | background oklab(0.235024 0.0000107065 0.00000470877 / 0.16) |

![Plan trial button default](components/crops/price-cta-default.png) ![Plan trial button hover](components/crops/price-cta-hover.png) ![Plan trial button focus-visible](components/crops/price-cta-focus-visible.png) ![Plan trial button pressed](components/crops/price-cta-pressed.png)

#### Sign up free
The Free plan Sign up free link. Measured, never followed. Read as `price-free` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 242.55 x 40; padding 0px 12px; radius 10px; background oklab(0.235024 0.0000107065 0.00000470877 / 0.08); text Libre Franklin 14/40.01 600, #1e1e1e `color.soft.black`; transition all 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | background oklab(0.235024 0.0000107065 0.00000470877 / 0.16) |
| focus-visible | background oklab(0.235024 0.0000107065 0.00000470877 / 0.16); shadow #44b1ff 0px 0px 0px 2px |
| pressed | background oklab(0.235024 0.0000107065 0.00000470877 / 0.16) |

![Sign up free default](components/crops/price-free-default.png) ![Sign up free hover](components/crops/price-free-hover.png) ![Sign up free focus-visible](components/crops/price-free-focus-visible.png) ![Sign up free pressed](components/crops/price-free-pressed.png)

#### FAQ summary
A pricing FAQ disclosure. Opened locally; nothing was submitted. Read as `faq-summary` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: opened) | size 752 x 83; padding 28px; background transparent; text Libre Franklin 18/27 600, #1e1e1e `color.soft.black`; icon 24 x 24, #1e1e1e `color.soft.black` |

![FAQ summary default](components/crops/faq-summary-default.png) ![FAQ summary opened](components/crops/faq-summary-opened.png)

### Features

The /features explorer, including the search field.

#### Features headline
The /features masthead. Read as `feat-h1` on the features page.

**Values (default).** size 748.42 x 64; background transparent; text KitSansFont 64/64 500, #ffffff `color.white`.

![Features headline default](components/crops/feat-h1-default.png)

#### Feature search
The feature explorer search field. Focused and typed into, then cleared. Nothing was submitted. Read as `feat-search` on the features page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 976 x 45; padding 8px 8px 8px 48px; border 1px solid #e3e3e3 `color.gray.200`; radius 8px; background #f7f7f7 `color.gray.50`; text Libre Franklin 18/27 400, #1e1e1e `color.soft.black`; placeholder #b8b8b8 `color.gray.500` |
| focused, filled | outline 1px auto #1e1e1e `color.soft.black`, offset 0px |

![Feature search default](components/crops/feat-search-default.png) ![Feature search focused](components/crops/feat-search-focused.png)

The filled crop was not stored. The field was typed into and cleared, and the crop was dropped with the log-in field crops so the package keeps only empty-field images.

### Compare

The Kit vs Mailchimp comparison table.

#### Compare headline
The Kit vs Mailchimp masthead. Read as `compare-h1` on the compare/mailchimp page.

**Values (default).** size 632 x 64; background transparent; text KitSansFont 64/64 500, #1e1e1e `color.soft.black`.

![Compare headline default](components/crops/compare-h1-default.png)

#### Comparison table
The feature comparison table on /compare/mailchimp. Read as `compare-table` on the compare/mailchimp page.

**Values (default).** size 1312 x 3567; background transparent; text Libre Franklin 20/25 700, #1e1e1e `color.soft.black`; icon 24 x 24, #1e1e1e `color.soft.black`; layers th.hidden.xs:block 437.3x74.0 rgb(255, 255, 255) B:1px solid rgb(212, 212, 212); th.sticky.top-12 437.3x74.0 rgb(255, 255, 255) B:1px solid rgb(212, 212, 212) / L:1px solid rgb(212, 212, 212); th.sticky.top-12 437.3x74.0 rgb(255, 255, 255) B:1px solid rgb(212, 212, 212) / L:1px solid rgb(212, 212, 212); td.col-span-full.border-b 1312.0x74.0 oklab(0.952704 0.000861377 0.0086019 / 0.5) B:1px solid r.

Child layers that carry the look: th 437.3x74 background #ffffff `color.white` border 1px solid #d4d4d4 `color.gray.300`; th 437.3x74 background #ffffff `color.white` border 1px solid #d4d4d4 `color.gray.300`; th 437.3x74 background #ffffff `color.white` border 1px solid #d4d4d4 `color.gray.300`.

![Comparison table default](components/crops/compare-table-default.png)

### App log-in

app.kit.com/users/login, a separate signed-out card. Measured, never submitted.

#### Log-in card
The signed-out log-in card on app.kit.com/users/login. A separate app from the marketing site. Nothing was submitted. Read as `login-panel` on the app log-in page.

Not on the page when it was captured.

#### Email field
The Email field. Focused and typed into with a placeholder address, then cleared. Nothing was submitted. Read as `login-email` on the app log-in page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 470 x 40; padding 8px 12px; radius 10px; background #ffffff `color.white`; shadow #d4d4d4 0px 0px 0px 1px inset; outline 2px solid transparent, offset 2px; text Inter 14/24 400, #1e1e1e `color.soft.black`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1), opacity 0.15s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1), transform 0.15s cubic-bezier(0.4, 0, 0.2, 1), translate 0.15s cubic-bezier(0.4, 0, 0.2, 1), scale 0.15s cubic-bezier(0.4, 0, 0.2, 1), rotate 0.15s cubic-bezier(0.4, 0, 0.2, 1), filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), -webkit-backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), display 0.15s cubic-bezier(0.4, 0, 0.2, 1), content-visibility 0.15s cubic-bezier(0.4, 0, 0.2, 1), overlay 0.15s cubic-bezier(0.4, 0, 0.2, 1), pointer-events 0.15s cubic-bezier(0.4, 0, 0.2, 1); placeholder #919191 `color.gray.600` |
| focused, filled | shadow #c4c4c4 0px 0px 0px 1px inset; outline 2px solid #1e1e1e `color.soft.black`, offset 2px |

![Email field default](components/crops/login-email-default.png)

Focused and filled crops were not stored. The empty field paints an email as a CSS placeholder, and the image scan treats any address as personal data. The stored page shot hides that placeholder. Measurements for focused and filled stay in [raw/measurements.md](raw/measurements.md).

#### Password field
The Password field. Focused and typed into, then cleared. Nothing was submitted. Read as `login-password` on the app log-in page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focused, filled) | size 414 x 40; padding 8px 0px; background transparent; text Inter 14/24 400, #1e1e1e `color.soft.black`; placeholder #919191 `color.gray.600` |

![Password field default](components/crops/login-password-default.png)

Focused and filled crops were not stored, for the same reason as the email field.

#### Show password
The Show password control. Measured, never used to reveal a real password. Read as `login-show` on the app log-in page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 32 x 32; padding 4px; radius 8px; background transparent; outline 2px solid transparent, offset 2px; text Inter 14/24 600, #1e1e1e `color.soft.black`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1), opacity 0.15s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1), transform 0.15s cubic-bezier(0.4, 0, 0.2, 1), translate 0.15s cubic-bezier(0.4, 0, 0.2, 1), scale 0.15s cubic-bezier(0.4, 0, 0.2, 1), rotate 0.15s cubic-bezier(0.4, 0, 0.2, 1), filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), -webkit-backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), display 0.15s cubic-bezier(0.4, 0, 0.2, 1), content-visibility 0.15s cubic-bezier(0.4, 0, 0.2, 1), overlay 0.15s cubic-bezier(0.4, 0, 0.2, 1), pointer-events 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 24 x 24, #3d3d3d `color.gray.800`; layers button.shrink-0.group/button 32.0x32.0 2px solid rgba(0, 0, 0, 0) offset 2px 8px |
| hover | background lab(11.2636 -0.00000745058 0.0000089407 / 0.06); layers none |
| focus-visible | outline 2px solid #1e1e1e `color.soft.black`, offset 2px; layers button.shrink-0.group/button 32.0x32.0 2px solid rgb(30, 30, 30) offset 2px 8px |
| pressed | background lab(11.2636 -0.00000745058 0.0000089407 / 0.06); layers none |

Child layers that carry the look: button 32x32 radius 8px.

![Show password default](components/crops/login-show-default.png) ![Show password hover](components/crops/login-show-hover.png) ![Show password focus-visible](components/crops/login-show-focus-visible.png) ![Show password pressed](components/crops/login-show-pressed.png)

#### Remember me
The Keep me logged in checkbox. Measured at rest, never toggled into a session. Read as `login-remember` on the app log-in page.

**Values (default).** size 1 x 1; background transparent; text Inter 14/normal 400, #3d3d3d `color.gray.800`; placeholder #3d3d3d `color.gray.800`.

![Remember me default](components/crops/login-remember-default.png)

#### Log in submit
The Log in submit. States were measured. The button was never clicked. Read as `login-submit` on the app log-in page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 470 x 48; padding 12px 20px; radius 12px; background #1e1e1e `color.soft.black`; outline 2px solid transparent, offset 2px; text Inter 14/24 600, #ffffff `color.white`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1), opacity 0.15s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1), transform 0.15s cubic-bezier(0.4, 0, 0.2, 1), translate 0.15s cubic-bezier(0.4, 0, 0.2, 1), scale 0.15s cubic-bezier(0.4, 0, 0.2, 1), rotate 0.15s cubic-bezier(0.4, 0, 0.2, 1), filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), -webkit-backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), display 0.15s cubic-bezier(0.4, 0, 0.2, 1), content-visibility 0.15s cubic-bezier(0.4, 0, 0.2, 1), overlay 0.15s cubic-bezier(0.4, 0, 0.2, 1), pointer-events 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | background #3d3d3d `color.gray.800` |
| focus-visible | outline 2px solid #1e1e1e `color.soft.black`, offset 2px |
| pressed | background #3d3d3d `color.gray.800` |

![Log in submit default](components/crops/login-submit-default.png) ![Log in submit hover](components/crops/login-submit-hover.png) ![Log in submit focus-visible](components/crops/login-submit-focus-visible.png) ![Log in submit pressed](components/crops/login-submit-pressed.png)

#### Forgot password
The I forgot my password link. Measured, never followed. Read as `login-forgot` on the app log-in page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 470 x 48; padding 12px 20px; radius 12px; background transparent; outline 2px solid transparent, offset 2px; text Inter 14/24 600, #1e1e1e `color.soft.black`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1), opacity 0.15s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1), transform 0.15s cubic-bezier(0.4, 0, 0.2, 1), translate 0.15s cubic-bezier(0.4, 0, 0.2, 1), scale 0.15s cubic-bezier(0.4, 0, 0.2, 1), rotate 0.15s cubic-bezier(0.4, 0, 0.2, 1), filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), -webkit-backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), display 0.15s cubic-bezier(0.4, 0, 0.2, 1), content-visibility 0.15s cubic-bezier(0.4, 0, 0.2, 1), overlay 0.15s cubic-bezier(0.4, 0, 0.2, 1), pointer-events 0.15s cubic-bezier(0.4, 0, 0.2, 1); layers a.shrink-0.group/button 470.0x48.0 2px solid rgba(0, 0, 0, 0) offset 2px 12px |
| hover | background lab(11.2636 -0.00000745058 0.0000089407 / 0.06); layers none |
| focus-visible | outline 2px solid #1e1e1e `color.soft.black`, offset 2px; layers a.shrink-0.group/button 470.0x48.0 2px solid rgb(30, 30, 30) offset 2px 12px |
| pressed | background lab(11.2636 -0.00000745058 0.0000089407 / 0.06); layers none |

Child layers that carry the look: a 470x48 radius 12px.

![Forgot password default](components/crops/login-forgot-default.png) ![Forgot password hover](components/crops/login-forgot-hover.png) ![Forgot password focus-visible](components/crops/login-forgot-focus-visible.png) ![Forgot password pressed](components/crops/login-forgot-pressed.png)

#### Create account
The Create account link. Signup is Cloudflare-gated and was not followed. Read as `login-create` on the app log-in page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 235 x 38; padding 8px 0px; border B: 1px solid #e3e3e3 `color.gray.200`; background transparent; outline 2px solid transparent, offset 0px; text Inter 14/20 400, #3d3d3d `color.gray.800`; layers a.hover:border-gray-500.hover:no-underline 235.0x38.0 B:1px solid rgb(227, 227, 227) 2px solid rgba(0, 0, 0, 0) offset 0px |
| hover | border B: 1px solid #b8b8b8 `color.gray.500`; layers a.hover:border-gray-500.hover:no-underline 235.0x38.0 B:1px solid rgb(184, 184, 184) 2px solid rgba(0, 0, 0, 0) offset 0px |
| focus-visible | outline 2px solid #1e1e1e `color.soft.black`, offset -2px; layers a.hover:border-gray-500.hover:no-underline 235.0x38.0 B:1px solid rgb(227, 227, 227) 2px solid rgb(30, 30, 30) offset -2px |
| pressed | border B: 1px solid #b8b8b8 `color.gray.500`; layers a.hover:border-gray-500.hover:no-underline 235.0x38.0 B:1px solid rgb(184, 184, 184) 2px solid rgba(0, 0, 0, 0) offset 0px |

Child layers that carry the look: a 235x38 border 1px solid #e3e3e3 `color.gray.200`.

![Create account default](components/crops/login-create-default.png) ![Create account hover](components/crops/login-create-hover.png) ![Create account focus-visible](components/crops/login-create-focus-visible.png) ![Create account pressed](components/crops/login-create-pressed.png)

### Mobile (390 wide)

The phone nav, menu button, and hero at 390 wide.

#### Mobile nav
The phone nav bar. Read as `m-nav` on the home page at 390 wide.

**Values (default).** size 390 x 60; background transparent; text Libre Franklin 14/24.00 600, #1e1e1e `color.soft.black`; transition all 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 53 x 24.53, #1e1e1e `color.soft.black`; layers a.font-sans.transition-all 0.0x0.0 T:1px solid rgb(242, 239, 233) / R:1px solid rgb(242, 239, 233) / B:1px solid rgb(242, 239, 233) / L:1px solid rgb(242, 239, 233) 8px; a.font-sans.transition-all 115.8x32.0 rgb(68, 177, 255) 8px; span 20.0x2.0 rgb(255, 255, 255); span::before 20pxx2px rgb(255, 255, 255) 999px; span::after 20pxx2px rgb(255, 255, 255) 999px; span 20.0x2.0 rgb(255, 255, 255).

Child layers that carry the look: a 0x0 border 1px solid #f2efe9 `color.warm.white` radius 8px; a 115.8x32 background #44b1ff `color.blue.500` radius 8px; span 20x2 background #ffffff `color.white`.

![Mobile nav default](components/crops/m-nav-default.png)

#### Mobile menu button
The icon-only Toggle mobile menu button. Opened locally. Links were never followed. Read as `m-menu` on the home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 36 x 36; padding 18px; background transparent; text Libre Franklin 0/0 400, #1e1e1e `color.soft.black`; layers span 20.0x2.0 rgb(255, 255, 255); span::before 20pxx2px rgb(255, 255, 255) 999px; span::after 20pxx2px rgb(255, 255, 255) 999px; span 20.0x2.0 rgb(255, 255, 255); span::before 20pxx2px rgb(255, 255, 255) 999px; span::after 20pxx2px rgb(255, 255, 255) 999px |
| focus-visible | outline 1px auto #e59700, offset 0px; layers button.MobileMenuToggle_MenuToggle__3DstI 36.0x36.0 1px auto rgb(229, 151, 0) offset 0px; span 20.0x2.0 rgb(255, 255, 255); span::before 20pxx2px rgb(255, 255, 255) 999px; span::after 20pxx2px rgb(255, 255, 255) 999px; span 20.0x2.0 rgb(255, 255, 255); span::before 20pxx2px rgb(255, 255, 255) 999px |
| opened | layers span::before 20pxx2px rgb(30, 30, 30) 999px; span::after 20pxx2px rgb(30, 30, 30) 999px; span::before 20pxx2px rgb(30, 30, 30) 999px; span::after 20pxx2px rgb(30, 30, 30) 999px; span::before 20pxx2px rgb(30, 30, 30) 999px; span::after 20pxx2px rgb(30, 30, 30) 999px |

Child layers that carry the look: span 20x2 background #ffffff `color.white`; span::before 20pxx2px background #ffffff `color.white` radius 999px; span::after 20pxx2px background #ffffff `color.white` radius 999px.

![Mobile menu button default](components/crops/m-menu-default.png) ![Mobile menu button hover](components/crops/m-menu-hover.png) ![Mobile menu button focus-visible](components/crops/m-menu-focus-visible.png) ![Mobile menu button pressed](components/crops/m-menu-pressed.png) ![Mobile menu button opened](components/crops/m-menu-opened.png)

#### Mobile hero
The home masthead at 390 wide. Read as `m-hero` on the home page at 390 wide.

**Values (default).** size 358 x 144; background transparent; text KitSansFont 48/48 500, #ffffff `color.white`.

![Mobile hero default](components/crops/m-hero-default.png)

### Footer

The page footer and a sitemap link.

#### Footer
The page footer: sitemap columns and legal links, including the published help@kit.com address. Read as `footer` on the home page.

**Values (default).** size 1440 x 1177; background transparent; text Libre Franklin 16/24 600, #ffffff `color.white`; icon 106 x 49.06, #ffffff `color.white`; layers section.relative.bg-soft-black 1440.0x1010.0 rgb(30, 30, 30); a.font-sans.transition-all 145.2x48.0 rgb(68, 177, 255) 12px; section.relative.bg-soft-black 1440.0x167.0 rgb(30, 30, 30).

Child layers that carry the look: section 1440x1010 background #1e1e1e `color.soft.black`; a 145.2x48 background #44b1ff `color.blue.500` radius 12px; section 1440x167 background #1e1e1e `color.soft.black`.

![Footer default](components/crops/footer-default.png)

#### Footer link
A footer sitemap link. Measured, never followed. Read as `footer-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 44.77 x 17; background transparent; text Libre Franklin 14/20 400, #ffffff `color.white`; transition color 0.1s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.1s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.1s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.1s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.1s cubic-bezier(0.4, 0, 0.2, 1), fill 0.1s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.1s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.1s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.1s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.1s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | text Libre Franklin 14/20 400, #6e6e6e `color.gray.700` |
| focus-visible | shadow #44b1ff 0px 0px 0px 2px; text Libre Franklin 14/20 400, #6e6e6e `color.gray.700`; layers a.relative.text-sm 44.8x17.0 rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgb(68, 177, 255) 0px 0px 0px 2px, rgba(0, 0, 0, 0) 0px 0px 0px 0px |
| pressed | text Libre Franklin 14/20 400, #6e6e6e `color.gray.700` |

![Footer link default](components/crops/footer-link-default.png) ![Footer link hover](components/crops/footer-link-hover.png) ![Footer link focus-visible](components/crops/footer-link-focus-visible.png) ![Footer link pressed](components/crops/footer-link-pressed.png)

## Icons

No standalone SVG icon set was lifted on this pass. The wordmark and menu glyphs in the crops are the product's artwork. Declared under layoutGaps in the catalog entry.

| Icon | Rendered sizes | View box | Style | Seen on | Next to |
|---|---|---|---|---|---|

## Gaps

### The signed-in product

Kit's product is the creator app at app.kit.com. The dashboard, email designer, automations, subscribers and commerce need an account and were never reached. The log-in card at https://app.kit.com/users/login was measured and never submitted. Signup at https://app.kit.com/users/signup?plan=1k stopped at a Cloudflare robot check. The request-a-demo form at https://kit.com/request-demo sits in a Chili Piper embed and was not submitted. help.kit.com, learn.kit.com and developers.kit.com are separate sites and were not captured.

### Pages

- **The account.** Every post-login surface was never reached. The log-in form was typed into and cleared. Log in was never clicked.
- **Signup.** https://app.kit.com/users/signup?plan=1k is behind a Cloudflare check and was not captured.
- **Request a demo.** https://kit.com/request-demo shows the marketing page. The embedded form was not submitted.
- **Migrations.** https://kit.com/migrations stopped at a Cloudflare security check and was not captured.
- **help.kit.com, learn.kit.com, developers.kit.com, updates.kit.com and newsletter.kit.com** are separate sites and were not captured.
- **Password reset.** https://app.kit.com/users/password/new is linked from the log-in card and was not followed.
- **Checkout and trial.** Plan links on https://kit.com/pricing point at signup with a plan query and were measured, never followed.

### States

- **Pressed** was forced with DevTools on controls, so a scripted mousedown state is missing.
- **Disabled, error, loading and validation** were not seen. Forms were never submitted.

### Themes

kit.com has no theme toggle. Every page paints light. The log-in card is also light, and it uses Inter rather than the marketing faces.

### Fonts

- **KitSansFont** draws display headlines. **Libre Franklin** draws UI and body on kit.com. **Inter** draws the log-in card. The style guide falls back to system sans.

### Screenshots

- The product screenshots, brand logos and blog imagery in the captures are the product's published content.
- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files.

### Content left out

- Article copy, integration names and the tool demos are the product's content; only frames and components were measured.
