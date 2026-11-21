# Frame.io components

The discovery list of every page and view captured, then one entry per component with crops of the real product, and the Gaps. Captured from frame.io on 2026-11-16, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running page. Nothing was signed into, bought or submitted; the contact form and the sign-in field were never sent; every link and CTA was measured, never followed.

The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) (52 components, 127 states). The page layouts are described in [patterns.md](patterns.md).

How to read an entry:

- A colour is its value followed by the palette token in [tokens.json](tokens.json) with the same value, when there is one. Text is written family size/line-height weight, then its colour, for example `Inter 16/20.8 400, #fcfcfc`, and is read from the first text node inside the component.
- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example "default (same: focus-visible)". When the root paints nothing, "Child layers" names the first nodes inside it that do.
- Crops are images of the component read from the live page, in [components/crops/](components/crops) (122 files, named `{component}-{state}.png`, shot at 2x device scale; a crop over about 1.2 megapixels is halved to 1x by the quantize step, so check a file's own dimensions before reading pixels off it). Screenshots are in [screenshots/](screenshots).

## Discovery list

Screenshots are named `{page}-{theme}-state.png` where `{theme}` is the mode the page painted at capture: `dark` for every frame.io page — the site ships no theme switch, so the dark theme is the only painted surface (the `dark` token set) — and `light` for accounts.frame.io/welcome, the sign-in surface on a different stack. Desktop shots are 1440 x 900 at 1x; `-full` shots are whole pages bounded at eight chunks; mobile shots are `mobile-{page}-{theme}-{state}.png` — the `-default` viewports are 780 wide (390 at 2x), the `-full` pages are captured at css scale and are 390 wide.

| Surface | URL | Screenshots |
|---|---|---|
| Home | `/` | [default](screenshots/home-dark-default.png), [full](screenshots/home-dark-full.png), [locale-open](screenshots/home-dark-locale-open.png), [menu-enterprise](screenshots/home-dark-menu-enterprise.png), [menu-features](screenshots/home-dark-menu-features.png), [menu-resources](screenshots/home-dark-menu-resources.png), [mobile-drawer](screenshots/home-dark-mobile-drawer.png) |
| Workflow Management | `/features/workflow-management` | [default](screenshots/features-workflow-dark-default.png), [full](screenshots/features-workflow-dark-full.png) |
| Review & Approval | `/features/review-and-approval` | [default](screenshots/features-review-dark-default.png), [full](screenshots/features-review-dark-full.png) |
| Camera to Cloud | `/features/c2c` | [default](screenshots/features-c2c-dark-default.png), [full](screenshots/features-c2c-dark-full.png) |
| Pricing | `/pricing` | [annual](screenshots/pricing-dark-annual.png), [default](screenshots/pricing-dark-default.png), [full](screenshots/pricing-dark-full.png) |
| Enterprise | `/enterprise` | [default](screenshots/enterprise-dark-default.png), [full](screenshots/enterprise-dark-full.png) |
| Media & Entertainment | `/enterprise/media-and-entertainment` | [default](screenshots/enterprise-me-dark-default.png), [full](screenshots/enterprise-me-dark-full.png) |
| Customers | `/customers` | [default](screenshots/customers-dark-default.png), [full](screenshots/customers-dark-full.png) |
| Case study (Ford) | `/case-studies/ford` | [default](screenshots/case-study-dark-default.png), [full](screenshots/case-study-dark-full.png) |
| Integrations | `/integrations` | [default](screenshots/integrations-dark-default.png), [full](screenshots/integrations-dark-full.png) |
| Resource hub | `/resources` | [default](screenshots/resources-dark-default.png), [full](screenshots/resources-dark-full.png) |
| What's new | `/whats-new` | [default](screenshots/whats-new-dark-default.png), [full](screenshots/whats-new-dark-full.png) |
| Contact | `/contact` | [default](screenshots/contact-dark-default.png), [full](screenshots/contact-dark-full.png) |
| Contact form | `/contact/form` | [default](screenshots/contact-form-dark-default.png), [full](screenshots/contact-form-dark-full.png) |
| Security | `/security` | [default](screenshots/security-dark-default.png), [full](screenshots/security-dark-full.png) |
| AI | `/ai` | [default](screenshots/ai-dark-default.png), [full](screenshots/ai-dark-full.png) |
| Frame.io Drive | `/drive` | [default](screenshots/drive-dark-default.png), [full](screenshots/drive-dark-full.png) |
| Transfer | `/transfer` | [default](screenshots/transfer-dark-default.png), [full](screenshots/transfer-dark-full.png) |
| Sign in (accounts.frame.io) | `accounts.frame.io/welcome` | [default](screenshots/welcome-light-default.png), [empty-desktop](screenshots/welcome-light-empty-desktop.png), [empty-phone](screenshots/welcome-light-empty-phone.png), [full](screenshots/welcome-light-full.png) |
| Home, phone | `/` | [default](screenshots/mobile-home-dark-default.png), [drawer](screenshots/mobile-home-dark-drawer.png), [full](screenshots/mobile-home-dark-full.png) |
| Pricing, phone | `/pricing` | [default](screenshots/mobile-pricing-dark-default.png), [full](screenshots/mobile-pricing-dark-full.png) |
| Contact form, phone | `/contact/form` | [default](screenshots/mobile-contact-form-dark-default.png), [full](screenshots/mobile-contact-form-dark-full.png) |
| Sign in, phone | `accounts.frame.io/welcome` | [default](screenshots/mobile-welcome-light-default.png), [full](screenshots/mobile-welcome-light-full.png) |

### Overlays and transient states

| State | Where | How it was reached | Captured |
|---|---|---|---|
| Announcement banner | every page | real chrome — left in every shot and reading; its close button was never pressed | captured as chrome |
| Geo-redirect language notice | some pages, non-US locales | did not appear for the en-US capture; the footer's 'English (US)' trigger was measured at rest, never opened | not seen while captured |
| Features mega-menu | every page header | clicked the 'Features' trigger — a local UI toggle (hover does not open it; keyboard Enter is the fallback) | [home-dark-menu-features](screenshots/home-dark-menu-features.png), [nav-panel](#mega-menu-panel), [nav-menu-item](#mega-menu-item) |
| Enterprise mega-menu | every page header | the same activation on 'Enterprise' | [home-dark-menu-enterprise](screenshots/home-dark-menu-enterprise.png) |
| Resources mega-menu | every page header | the same activation on 'Resources' | [home-dark-menu-resources](screenshots/home-dark-menu-resources.png) |
| Mobile nav overlay | home page, phone width | the 'Toggle mobile navigation' button's own toggle | [mobile-home-dark-drawer](screenshots/mobile-home-dark-drawer.png), [m-drawer](#mobile-nav-overlay) |
| Billing toggle | /pricing | the Monthly/Annually switch was measured at rest — flipping re-prices the grid, so it was never switched | [price-toggle](#billing-toggle), [price-toggle-alt](#billing-toggle-annual) |
| Comparison accordions | /pricing | clicked one comparison-row category — a local UI toggle | [ptable-acc](#feature-comparison-accordion) — the accordion-open screenshot was not captured this run (the accordion trigger did not open) |
| Pricing FAQ | /pricing | clicked one FAQ row — a local UI toggle | [faq-acc](#faq-accordion) |
| Contact form fields | /contact/form | empty — nothing typed; Submit was never pressed | [form-name](#name-field), [form-email](#email-field), [form-message](#message-field) |
| Sign-in field | accounts.frame.io/welcome | empty — nothing typed; 'Let's go' was never pressed | [login-email](#email-field-sign-in) |
| Schedule a Meeting | /contact | it mounts a Calendly scheduler — a vendor widget; the button was measured, never pressed | [schedule-btn](#schedule-a-meeting) |
| Signed-in product | a Frame.io account | the app and every post-login surface needs an account | boundary; see Gaps |

## Shared values

Values that apply across entries, from the measurement files.

**Focus.** 19 components were given a real keyboard focus. 18 draw an outline ring: `nav-trigger` (1px dotted #fcfcfc `dark.theme.fg.declared`, offset 0px), `nav-pricing` (1px dotted #fcfcfc `dark.theme.fg.declared`, offset 1px), `nav-contact` (1px dotted #fcfcfc `dark.theme.fg.declared`, offset 1px), `nav-signin` (1px dotted #fcfcfc `dark.theme.fg.declared`, offset 1px), `nav-cta` (1px dotted #fcfcfc `dark.theme.fg.declared`, offset 1px), `hero-cta` (1px dotted #fcfcfc `dark.theme.fg.declared`, offset 1px), `hero-tour` (1px dotted #fcfcfc `dark.theme.fg.declared`, offset 1px), `locale-btn` (2px solid #5b53ff `core.color.brand.cobalt.default`, offset 2px), `cookie-prefs` (1px dotted #fcfcfc `dark.theme.fg.declared`, offset 0px), `price-toggle` (1px dotted #fcfcfc `dark.theme.fg.declared`, offset 0px), `price-toggle-alt` (1px dotted #fcfcfc `dark.theme.fg.declared`, offset 0px), `plan-signup` (1px dotted #fcfcfc `dark.theme.fg.declared`, offset 1px), `plan-trial` (1px dotted #fcfcfc `dark.theme.fg.declared`, offset 1px), `plan-meeting` (1px dotted #fcfcfc `dark.theme.fg.declared`, offset 0px), `schedule-btn` (1px dotted #fcfcfc `dark.theme.fg.declared`, offset 0px), `sales-link` (1px dotted #fcfcfc `dark.theme.fg.declared`, offset 0px), `m-menu-btn` (1px dotted #fcfcfc `dark.theme.fg.declared`, offset 0px), `m-hero-cta` (1px dotted #fcfcfc `dark.theme.fg.declared`, offset 1px). 1 draw a focus ring as a shadow instead: `login-submit`.

**Pressed.** Forced with DevTools (`CSS.forcePseudoState` :active:hover). Nothing a real press would submit was ever pressed.

**Motion.** Transitions measured on the components, by duration.

| Duration | Easing | Property | Where |
|---|---|---|---|
| 0.0002s | `ease` | opacity | login-submit |
| 0.2s | `cubic-bezier(0.25, 0.1, 0.25, 1)` | background-color, color | locale-btn |
| 0.2s | `ease` | background-color, box-shadow, color | login-submit |
| 0.3s | `cubic-bezier(0, 0.44, 0.6, 1)` | color | form-submit, hero-cta, hero-tour, m-cta, m-hero-cta, nav-cta, plan-meeting, plan-signup and more |
| 0.3s | `cubic-bezier(0.25, 0.1, 0.25, 1)` | border-color | form-email, form-message, form-name |
| 0.3s | `cubic-bezier(0.28, 0.44, 0.49, 1)` | color | footer-link, nav-contact, nav-pricing, nav-signin, nav-trigger, sales-link |
| 0.3s | `ease` | background-color | login-email |
| 0.5s | `cubic-bezier(0, 0.44, 0.6, 1)` | background-color, border-color | int-card |
| 0.5s | `cubic-bezier(0.42, 0, 0.28, 0.99)` | transform | m-topbar |
| 0.6s | `cubic-bezier(0.28, 0.44, 0.49, 1)` | color | nav-menu-item |

**Card shapes.** Default-state values; the entries hold the states.

| Card | Size | Border | Radius | Background | Shadow | Padding |
|---|---|---|---|---|---|---|
| [Mega-menu panel](#mega-menu-panel) | 1440 x 604.5 | - | - | transparent | none | 176px 0px 106px 0px |
| [Plan card](#plan-card) | 252 x 796.59 | 1px solid rgba(157, 157, 255, 0.1) | 10px | rgba(16, 16, 23, 0.5) `dark.theme.surface.card` | #181826 12px 12px 50px 0px inset, rgba(0, 0, 0, 0.31) 84.68px 149.711px 80px 0px, rgba(0, 0, 0, 0.26) 54.885px 97.035px 46.852px 0px, rgba(0, 0, 0, 0.23) 32.618px 57.666px 25.481px 0px, rgba(0, 0, 0, 0.2) 16.936px 29.942px 13px 0px, rgba(0, 0, 0, 0.18) 6.9px 12.199px 6.519px 0px, rgba(0, 0, 0, 0.2) 1.568px 2.772px 3.148px 0px | 24px |
| [Contact form card](#contact-form-card) | 1440 x 1543.47 | - | - | transparent | none | 0 |
| [Sign-in panel](#sign-in-panel) | 346 x 345.84 | - | - | transparent | none | 0 |
| [Mobile nav overlay](#mobile-nav-overlay) | 342 x 210 | - | - | transparent | none | 0 |
| [Customer card](#customer-card) | 1080 x 220 | - | - | transparent | none | 0 |

## Components

### Site chrome (header, announcement, nav, footer)

The chrome on every public page: the cobalt announcement banner, the fixed 8rem header (the Frame.io waveform mark, the Features/Enterprise/Resources mega-menu triggers — click opens the full-width panel, hover does not — Pricing, Contact Us, Sign In and the white 'Start Free Trial' pill), and the dark footer with 'Cookie preferences' and the 'English (US)' language trigger.

#### Site header
The fixed top bar on every public page (header is a 0-height sentinel; the painted bar is nav.mainNavigation, 80px under the 36px announcement strip): the Frame.io mark, the Features/Enterprise/Resources mega-menu triggers, Pricing, Contact Us, Sign In and the "Start Free Trial" pill. Read as `mkt-header` on the home page.

**Values (default).** size 1440 x 80; background transparent; text FrameGothic 14/13.44 600, #fcfcfc `dark.theme.fg.declared`; icon 30 x 34, #fcfcfc `dark.theme.fg.declared`; layers a::before.Button_white__XYP1F.Button_base__1G9eD 155.25pxx37.75px rgb(245, 245, 248) T:1px solid rgb(193, 194, 217) / R:1px solid rgb(193, 194, 217) / B:1px solid rgb(193, 194, 217) / L:1px solid rgb(193, 194, 217) 100px; figure.Navigation_backdrop__xQNG2 1440.0x80.0 rgba(13, 13, 24, 0.3).

Child layers that carry the look: a::before 155.25pxx37.75px background #f5f5f8 `dark.theme.accent` border 1px solid #c1c2d9 `core.color.grey.80` radius 100px; figure 1440x80 background rgba(13, 13, 24, 0.3) `core.color.alpha.dark.30`.

![Site header default](components/crops/mkt-header-default.png)

#### Page field
The near-black field the whole public site paints (the html background layer; body is transparent over it). Read as `page-field` on the home page.

**Values (default).** size 1440 x 11936.91; background #000000 `core.color.alpha.black.100`; text FrameGothic 12/12 600, #fcfcfc `dark.theme.fg.declared`; icon 24 x 24, #fcfcfc `dark.theme.fg.declared`.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Logo
The Frame.io waveform mark in the header, linking home. Read as `mkt-logo` on the home page.

**Values (default).** size 30 x 34; background transparent; text Times New Roman 10/10 400, #fcfcfc `dark.theme.fg.declared`; icon 30 x 34, #fcfcfc `dark.theme.fg.declared`.

![Logo default](components/crops/mkt-logo-default.png)

#### Announcement banner
The site-wide promo strip above the header ("Put your creative context to work with new AI-powered capabilities →") — real chrome, never hidden. Read as `announcement` on the home page.

**Values (default).** size 1440 x 36; padding 12px 24px; background #5b53ff `core.color.brand.cobalt.default`; image linear-gradient(355deg, rgba(255, 255, 255, 0.15) 4.03%, rgba(255, 255, 255, 0) 95.81%), none; text FrameGothic 12/12 600, #fcfcfc `dark.theme.fg.declared`; icon 24 x 24, #fcfcfc `dark.theme.fg.declared`.

![Announcement banner default](components/crops/announcement-default.png)

#### Mega-menu trigger
The "Features" header button — click opens the mega-menu (the group gains NavGroup_open__ and the nav Navigation_subNavOpen__; hovering does not open it). The opened state was measured after its own toggle click. Read as `nav-trigger` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 83.92 x 80; background transparent; text FrameGothic 14/13.44 600, #fcfcfc `dark.theme.fg.declared`; transition color 0.3s cubic-bezier(0.28, 0.44, 0.49, 1); icon 9.8 x 9.8, #fcfcfc `dark.theme.fg.declared`; layers ::before rgba(0, 0, 0, 0) 0px none 1 |
| focus-visible | outline 1px dotted #fcfcfc `dark.theme.fg.declared`, offset 0px; layers ::before rgba(0, 0, 0, 0) 0px none 1; button.Navigation_navigationMainItem__pIZar.typography_navigation__70PKN 83.9x80.0 1px dotted rgb(252, 252, 252) offset 0px |
| opened | icon 12.94 x 12.94, #fcfcfc `dark.theme.fg.declared` |

![Mega-menu trigger default](components/crops/nav-trigger-default.png) ![Mega-menu trigger hover](components/crops/nav-trigger-hover.png) ![Mega-menu trigger focus-visible](components/crops/nav-trigger-focus-visible.png) ![Mega-menu trigger pressed](components/crops/nav-trigger-pressed.png) ![Mega-menu trigger opened](components/crops/nav-trigger-opened.png)

#### Mega-menu panel
The Features mega-menu opened by its trigger (Workflow Management, File Management, Share & Present, Review & Approvals, Camera to Cloud, Integrations, Mounted Storage, Frame.io Drive); its links were never followed. Read as `nav-panel` on the home page.

**Values (default).** size 1440 x 604.5; padding 176px 0px 106px 0px; background transparent; text FrameGothic 48/48.96 600, #fcfcfc `dark.theme.fg.declared`.

![Mega-menu panel default](components/crops/nav-panel-default.png)

#### Mega-menu item
A destination row inside the opened mega-menu; measured, never followed. Read as `nav-menu-item` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 360 x 49.19; background transparent; text FrameGothic 24/31.2 400, #fcfcfc `dark.theme.fg.declared`; transition color 0.6s cubic-bezier(0.28, 0.44, 0.49, 1); layers ::before rgba(0, 0, 0, 0) 0px none 1 |
| hover | transition color 0.3s cubic-bezier(0.28, 0.44, 0.49, 1) |

![Mega-menu item default](components/crops/nav-menu-item-default.png) ![Mega-menu item hover](components/crops/nav-menu-item-hover.png)

#### Nav link
The "Pricing" header link; measured, never followed. Read as `nav-pricing` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 48.98 x 80; background transparent; text FrameGothic 14/13.44 600, #fcfcfc `dark.theme.fg.declared`; transition color 0.3s cubic-bezier(0.28, 0.44, 0.49, 1); layers ::before rgba(0, 0, 0, 0) 0px none 1 |
| focus-visible | outline 1px dotted #fcfcfc `dark.theme.fg.declared`, offset 1px; layers ::before rgba(0, 0, 0, 0) 0px none 1; a.Navigation_navigationMainItem__pIZar.typography_navigation__70PKN 49.0x80.0 1px dotted rgb(252, 252, 252) offset 1px |

![Nav link default](components/crops/nav-pricing-default.png) ![Nav link hover](components/crops/nav-pricing-hover.png) ![Nav link focus-visible](components/crops/nav-pricing-focus-visible.png) ![Nav link pressed](components/crops/nav-pricing-pressed.png)

#### Contact Us link
The "Contact Us" header link; measured, never followed. Read as `nav-contact` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 81 x 13.44; background transparent; text FrameGothic 14/13.44 600, #fcfcfc `dark.theme.fg.declared`; transition color 0.3s cubic-bezier(0.28, 0.44, 0.49, 1); layers ::before rgba(0, 0, 0, 0) 0px none 1 |
| focus-visible | outline 1px dotted #fcfcfc `dark.theme.fg.declared`, offset 1px; layers ::before rgba(0, 0, 0, 0) 0px none 1; a.NavItem_isReducedNavNavItem__kqUAm.typography_reducedNavigation__4_qzl 81.0x13.4 1px dotted rgb(252, 252, 252) offset 1px |

![Contact Us link default](components/crops/nav-contact-default.png) ![Contact Us link hover](components/crops/nav-contact-hover.png) ![Contact Us link focus-visible](components/crops/nav-contact-focus-visible.png) ![Contact Us link pressed](components/crops/nav-contact-pressed.png)

#### Sign In link
The "Sign In" header link to app.frame.io (which redirects to the accounts.frame.io/welcome sign-in surface); measured, never followed. Read as `nav-signin` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 44.98 x 13.44; background transparent; text FrameGothic 14/13.44 600, #fcfcfc `dark.theme.fg.declared`; transition color 0.3s cubic-bezier(0.28, 0.44, 0.49, 1); layers ::before rgba(0, 0, 0, 0) 0px none 1 |
| focus-visible | outline 1px dotted #fcfcfc `dark.theme.fg.declared`, offset 1px; layers ::before rgba(0, 0, 0, 0) 0px none 1; a.Navigation_navigationMainItem__pIZar.typography_navigation__70PKN 45.0x13.4 1px dotted rgb(252, 252, 252) offset 1px |

![Sign In link default](components/crops/nav-signin-default.png) ![Sign In link hover](components/crops/nav-signin-hover.png) ![Sign In link focus-visible](components/crops/nav-signin-focus-visible.png) ![Sign In link pressed](components/crops/nav-signin-pressed.png)

#### Header CTA
The white "Start Free Trial" header pill; links to the trial sign-up, measured never followed. Read as `nav-cta` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 157.25 x 39.75; padding 0px 24px; radius 100px; background transparent; text FrameGothic 14/13.44 600, #000000 `core.color.alpha.black.100`; transition color 0.3s cubic-bezier(0, 0.44, 0.6, 1); layers ::before rgb(245, 245, 248) 1px none 1; ::after rgba(0, 0, 0, 0) 0px rgb(193, 194, 217) 0px 0px 0px 2px inset 0; a::before.Button_white__XYP1F.Button_base__1G9eD 155.25pxx37.75px rgb(245, 245, 248) T:1px solid rgb(193, 194, 217) / R:1px solid rgb(193, 194, 217) / B:1px solid rgb(193, 194, 217) / L:1px solid rgb(193, 194, 217) 100px |
| hover | layers ::before rgba(233, 233, 255, 0.7) 1px none 1; ::after rgba(0, 0, 0, 0) 0px rgb(252, 252, 252) 0px 0px 0px 2px inset 1; a::before.Button_white__XYP1F.Button_base__1G9eD 155.25pxx37.75px rgba(233, 233, 255, 0.7) T:1px solid rgb(193, 194, 217) / R:1px solid rgb(193, 194, 217) / B:1px solid rgb(193, 194, 217) / L:1px solid rgb(193, 194, 217) 100px; a::after.Button_white__XYP1F.Button_base__1G9eD 157.2 |
| focus-visible | outline 1px dotted #fcfcfc `dark.theme.fg.declared`, offset 1px; layers ::before rgba(233, 233, 255, 0.7) 1px none 1; ::after rgba(0, 0, 0, 0) 0px rgb(193, 194, 217) 0px 0px 0px 2px inset 0; a.Button_white__XYP1F.Button_base__1G9eD 157.3x39.8 1px dotted rgb(252, 252, 252) offset 1px 100px; a::before.Button_white__XYP1F.Button_base__1G9eD 155.25pxx37.75px rgba(233, 233, 255, 0.7) T:1px solid rgb(193, 194, 217) / R:1px solid rgb(193, 194, 217) / B:1px solid rgb(193, 194 |
| pressed | text FrameGothic 14/13.44 600, #fcfcfc `dark.theme.fg.declared`; layers ::before rgba(0, 0, 0, 0) 0px none 1; ::after rgba(0, 0, 0, 0) 0px rgba(209, 209, 251, 0.2) 0px 0px 0px 4px inset 1; a::after.Button_white__XYP1F.Button_base__1G9eD 157.25pxx39.75px rgba(209, 209, 251, 0.2) 0px 0px 0px 4px inset 100px |

Child layers that carry the look: a::before 155.25pxx37.75px background #f5f5f8 `dark.theme.accent` border 1px solid #c1c2d9 `core.color.grey.80` radius 100px.

![Header CTA default](components/crops/nav-cta-default.png) ![Header CTA hover](components/crops/nav-cta-hover.png) ![Header CTA focus-visible](components/crops/nav-cta-focus-visible.png) ![Header CTA pressed](components/crops/nav-cta-pressed.png)

#### Site footer
The dark footer on every public page: link columns, legal row, "Cookie preferences" and the language selector. Read as `footer` on the home page.

**Values (default).** size 1440 x 838.39; padding 96px 0px 48px 0px; background transparent; text NeueMachinaInktrap 12/10.8 400, rgba(233, 233, 255, 0.7) `core.color.alpha.light.70`; transform translate(0px, -14.598px); icon 30 x 34, #fcfcfc `dark.theme.fg.declared`; layers div::before.Footer_rowSecondary__dHZWA.global_grid__4e_JW 1080pxx2px rgba(189, 189, 244, 0.1) 2px; div.Footer_backdrop__Asw9G 1440.0x838.4 rgba(13, 13, 24, 0.8).

Child layers that carry the look: div::before 1080pxx2px background rgba(189, 189, 244, 0.1) `core.color.alpha.light.10` radius 2px; div 1440x838.4 background rgba(13, 13, 24, 0.8) `core.color.alpha.dark.80`.

![Site footer default](components/crops/footer-default.png)

#### Footer link
A legal/support link in the footer; measured, never followed. Read as `footer-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 87 x 36; padding 0px 24px 16px 0px; background transparent; text FrameGothic 16/20 400, #fcfcfc `dark.theme.fg.declared`; transition color 0.3s cubic-bezier(0.28, 0.44, 0.49, 1) |

![Footer link default](components/crops/footer-link-default.png) ![Footer link hover](components/crops/footer-link-hover.png)

#### Language selector
The "English (US)" footer trigger (LanguageSelector_trigger); measured at rest, never opened. Read as `locale-btn` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 120 x 32; padding 4px 8px; radius 5px; background transparent; text FrameGothic 10/normal 400, #6a6b83 `core.color.grey.50`; transition color 0.2s cubic-bezier(0.25, 0.1, 0.25, 1), background-color 0.2s cubic-bezier(0.25, 0.1, 0.25, 1); icon 16 x 16, #6a6b83 `core.color.grey.50` |
| hover | background rgba(157, 157, 255, 0.05) `core.color.alpha.light.5`; text FrameGothic 10/normal 400, #fcfcfc `dark.theme.fg.declared`; icon 16 x 16, #fcfcfc `dark.theme.fg.declared` |
| focus-visible | outline 2px solid #5b53ff `core.color.brand.cobalt.default`, offset 2px; layers button.LanguageSelector_trigger__IwXGd.typography_footnote__h8r_U 120.0x32.0 2px solid rgb(91, 83, 255) offset 2px 5px |
| pressed | background rgba(157, 157, 255, 0.05) `core.color.alpha.light.5`; text FrameGothic 10/normal 400, #fcfcfc `dark.theme.fg.declared`; icon 16 x 16, #fcfcfc `dark.theme.fg.declared` |

![Language selector default](components/crops/locale-btn-default.png) ![Language selector hover](components/crops/locale-btn-hover.png) ![Language selector focus-visible](components/crops/locale-btn-focus-visible.png) ![Language selector pressed](components/crops/locale-btn-pressed.png)

#### Cookie preferences
The footer "Cookie preferences" button, which mounts the consent manager on demand; measured at rest, never pressed. Read as `cookie-prefs` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 93 x 12; background transparent; text FrameGothic 10/normal 400, #fcfcfc `dark.theme.fg.declared` |
| focus-visible | outline 1px dotted #fcfcfc `dark.theme.fg.declared`, offset 0px; layers button.Footer_bottomLeftItem__EmEaX.typography_footnote__h8r_U 93.0x12.0 1px dotted rgb(252, 252, 252) offset 0px |

![Cookie preferences default](components/crops/cookie-prefs-default.png) ![Cookie preferences hover](components/crops/cookie-prefs-hover.png) ![Cookie preferences focus-visible](components/crops/cookie-prefs-focus-visible.png) ![Cookie preferences pressed](components/crops/cookie-prefs-pressed.png)

### Home

The home hero: the centred FrameGothic display masthead, the paired Start-Free-Trial pill / Take-a-Product-Tour ghost, and section headings.

#### Hero headline
"One platform for all your creative work." — the frame.io hero display heading in FrameGothic 80px. Read as `hero-h1` on the home page.

**Values (default).** size 504 x 249.56; background transparent; text FrameGothic 80/83.2 600, #fcfcfc `dark.theme.fg.declared`.

![Hero headline default](components/crops/hero-h1-default.png)

#### Hero CTA
The hero "Start Free Trial" button; measured, never followed. Read as `hero-cta` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 157.25 x 39.75; padding 0px 24px; radius 100px; background transparent; text FrameGothic 14/13.44 600, #000000 `core.color.alpha.black.100`; transition color 0.3s cubic-bezier(0, 0.44, 0.6, 1); layers ::before rgb(245, 245, 248) 1px none 1; ::after rgba(0, 0, 0, 0) 0px rgb(193, 194, 217) 0px 0px 0px 2px inset 0; a::before.Button_white__XYP1F.Button_base__1G9eD 155.25pxx37.75px rgb(245, 245, 248) T:1px solid rgb(193, 194, 217) / R:1px solid rgb(193, 194, 217) / B:1px solid rgb(193, 194, 217) / L:1px solid rgb(193, 194, 217) 100px |
| hover | layers ::before rgba(233, 233, 255, 0.7) 1px none 1; ::after rgba(0, 0, 0, 0) 0px rgb(252, 252, 252) 0px 0px 0px 2px inset 1; a::before.Button_white__XYP1F.Button_base__1G9eD 155.25pxx37.75px rgba(233, 233, 255, 0.7) T:1px solid rgb(193, 194, 217) / R:1px solid rgb(193, 194, 217) / B:1px solid rgb(193, 194, 217) / L:1px solid rgb(193, 194, 217) 100px; a::after.Button_white__XYP1F.Button_base__1G9eD 157.2 |
| focus-visible | outline 1px dotted #fcfcfc `dark.theme.fg.declared`, offset 1px; layers ::before rgba(233, 233, 255, 0.7) 1px none 1; ::after rgba(0, 0, 0, 0) 0px rgb(193, 194, 217) 0px 0px 0px 2px inset 0; a.Button_white__XYP1F.Button_base__1G9eD 157.3x39.8 1px dotted rgb(252, 252, 252) offset 1px 100px; a::before.Button_white__XYP1F.Button_base__1G9eD 155.25pxx37.75px rgba(233, 233, 255, 0.7) T:1px solid rgb(193, 194, 217) / R:1px solid rgb(193, 194, 217) / B:1px solid rgb(193, 194 |
| pressed | text FrameGothic 14/13.44 600, #fcfcfc `dark.theme.fg.declared`; layers ::before rgba(0, 0, 0, 0) 0px none 1; ::after rgba(0, 0, 0, 0) 0px rgba(209, 209, 251, 0.2) 0px 0px 0px 4px inset 1; a::after.Button_white__XYP1F.Button_base__1G9eD 157.25pxx39.75px rgba(209, 209, 251, 0.2) 0px 0px 0px 4px inset 100px |

Child layers that carry the look: a::before 155.25pxx37.75px background #f5f5f8 `dark.theme.accent` border 1px solid #c1c2d9 `core.color.grey.80` radius 100px.

![Hero CTA default](components/crops/hero-cta-default.png) ![Hero CTA hover](components/crops/hero-cta-hover.png) ![Hero CTA focus-visible](components/crops/hero-cta-focus-visible.png) ![Hero CTA pressed](components/crops/hero-cta-pressed.png)

#### Hero secondary action
The hero "Take a Product Tour" ghost button; measured, never followed. Read as `hero-tour` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 208.67 x 39.75; padding 0px 24px; radius 100px; background transparent; text FrameGothic 14/13.44 600, #fcfcfc `dark.theme.fg.declared`; transition color 0.3s cubic-bezier(0, 0.44, 0.6, 1); icon 4.44 x 7.5, #fcfcfc `dark.theme.fg.declared`; layers ::before rgba(209, 209, 251, 0.2) 0px none 1; ::after rgba(0, 0, 0, 0) 0px rgba(157, 157, 255, 0.05) 0px 0px 0px 1px inset 1; a::before.Button_glass__B8SwH.Button_base__1G9eD 208.672pxx39.75px rgba(209, 209, 251, 0.2) 100px; a::after.Button_glass__B8SwH.Button_base__1G9eD 208.672pxx39.75px rgba(157, 157, 255, 0.05) 0px 0px 0px 1px inset 100px; span::after.AnimatedSvgArrow_cssTail__yibfW 20pxx1.656 |
| hover | layers ::before rgba(220, 220, 255, 0.3) 0px none 1; ::after rgba(0, 0, 0, 0) 0px rgba(189, 189, 244, 0.1) 0px 0px 0px 2px inset 1; a::before.Button_glass__B8SwH.Button_base__1G9eD 208.672pxx39.75px rgba(220, 220, 255, 0.3) 100px; a::after.Button_glass__B8SwH.Button_base__1G9eD 208.672pxx39.75px rgba(189, 189, 244, 0.1) 0px 0px 0px 2px inset 100px; span::after.AnimatedSvgArrow_cssTail__yibfW 20pxx1.65625 |
| focus-visible | outline 1px dotted #fcfcfc `dark.theme.fg.declared`, offset 1px; layers ::before rgba(220, 220, 255, 0.298) 0px none 1; ::after rgba(0, 0, 0, 0) 0px rgba(157, 157, 255, 0.05) 0px 0px 0px 1px inset 1; a.Button_glass__B8SwH.Button_base__1G9eD 208.7x39.8 1px dotted rgb(252, 252, 252) offset 1px 100px; a::before.Button_glass__B8SwH.Button_base__1G9eD 208.672pxx39.75px rgba(220, 220, 255, 0.298) 100px; a::after.Button_glass__B8SwH.Button_base__1G9eD 208.672pxx39.75px rgba( |
| pressed | layers ::before rgba(0, 0, 0, 0) 0px none 1; ::after rgba(0, 0, 0, 0) 0px rgba(209, 209, 251, 0.2) 0px 0px 0px 4px inset 1; a::after.Button_glass__B8SwH.Button_base__1G9eD 208.672pxx39.75px rgba(209, 209, 251, 0.2) 0px 0px 0px 4px inset 100px; span::after.AnimatedSvgArrow_cssTail__yibfW 20pxx1.65625px rgb(245, 245, 248) 1px |

Child layers that carry the look: a::before 208.672pxx39.75px background rgba(209, 209, 251, 0.2) `core.color.alpha.hawkes.20` radius 100px; a::after 208.672pxx39.75px radius 100px shadow rgba(157, 157, 255, 0.05) `core.color.alpha.light.5` 0px 0px 0px 1px inset; span::after 20pxx1.65625px background #f5f5f8 `dark.theme.accent` radius 1px.

![Hero secondary action default](components/crops/hero-tour-default.png) ![Hero secondary action hover](components/crops/hero-tour-hover.png) ![Hero secondary action focus-visible](components/crops/hero-tour-focus-visible.png) ![Hero secondary action pressed](components/crops/hero-tour-pressed.png)

#### Section headline
A section heading on the home page; first visible h2. Read as `section-h2` on the home page.

**Values (default).** size 896 x 97.91; background transparent; text FrameGothic 48/48.96 600, rgba(234, 234, 255, 0.5) `core.color.alpha.light.50`.

![Section headline default](components/crops/section-h2-default.png)

### Pricing

The /pricing grid: the Monthly/Annually billing switch (Annually carries a 'SAVE 13%' badge), the plan columns at $0/$15/$25 and their CTAs, the feature-comparison category accordions and the pricing FAQ.

#### Pricing headline
The /pricing masthead. Read as `price-h1` on the pricing page.

**Values (default).** size 804 x 166.38; background transparent; text FrameGothic 80/83.2 600, #fcfcfc `dark.theme.fg.declared`.

![Pricing headline default](components/crops/price-h1-default.png)

#### Billing toggle
The "Monthly" side of the Monthly/Annually billing switch — a pair of round radio controls (a 24px circle ringed grey-60, a 10px turquoise-triumph dot on the selected side), not a segmented pill; a local UI toggle, measured at rest — the alternate price state was not toggled. Read as `price-toggle` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 91.98 x 24; background transparent; text FrameGothic 14/13.44 600, #fcfcfc `dark.theme.fg.declared`; layers figure.RadioButtons_radioButtonIcon__ih70y 24.0x24.0 T:1px solid rgb(129, 133, 159) / R:1px solid rgb(129, 133, 159) / B:1px solid rgb(129, 133, 159) / L:1px solid rgb(129, 133, 159) 12px; figure::after.RadioButtons_radioButtonIcon__ih70y 10pxx10px rgb(97, 153, 246) 5px |
| focus-visible | outline 1px dotted #fcfcfc `dark.theme.fg.declared`, offset 0px; layers button.RadioButtons_radioButtonInner__TrHlG 92.0x24.0 1px dotted rgb(252, 252, 252) offset 0px; figure.RadioButtons_radioButtonIcon__ih70y 24.0x24.0 T:1px solid rgb(129, 133, 159) / R:1px solid rgb(129, 133, 159) / B:1px solid rgb(129, 133, 159) / L:1px solid rgb(129, 133, 159) 12px; figure::after.RadioButtons_radioButtonIcon__ih70y 10pxx10px rgb(97, 153, 246) 5px |

Child layers that carry the look: figure 24x24 border 1px solid #81859f `core.color.grey.60` radius 12px; figure::after 10pxx10px background #6199f6 `core.color.turquoiseTriumph` radius 5px.

![Billing toggle default](components/crops/price-toggle-default.png) ![Billing toggle hover](components/crops/price-toggle-hover.png) ![Billing toggle focus-visible](components/crops/price-toggle-focus-visible.png) ![Billing toggle pressed](components/crops/price-toggle-pressed.png)

#### Billing toggle (annual)
The "Annually — SAVE 13%" side of the billing switch — the same round radio control, measured at rest, never toggled. Read as `price-toggle-alt` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 174.86 x 24; background transparent; text FrameGothic 14/13.44 600, #fcfcfc `dark.theme.fg.declared`; layers figure.RadioButtons_radioButtonIcon__ih70y 24.0x24.0 T:1px solid rgb(129, 133, 159) / R:1px solid rgb(129, 133, 159) / B:1px solid rgb(129, 133, 159) / L:1px solid rgb(129, 133, 159) 12px; span.RadioButtons_radioButtonSubtitle__g5iTZ.typography_button__Uyx6e 72.7x14.6 rgb(97, 153, 246) T:1px solid rgb(97, 153, 246) / R:1px solid rgb(97, 153, 246) / B:1px solid rgb(97, 153, 246) / L:1px solid rgb(9 |
| focus-visible | outline 1px dotted #fcfcfc `dark.theme.fg.declared`, offset 0px; layers button.RadioButtons_radioButtonInner__TrHlG 174.9x24.0 1px dotted rgb(252, 252, 252) offset 0px; figure.RadioButtons_radioButtonIcon__ih70y 24.0x24.0 T:1px solid rgb(129, 133, 159) / R:1px solid rgb(129, 133, 159) / B:1px solid rgb(129, 133, 159) / L:1px solid rgb(129, 133, 159) 12px; span.RadioButtons_radioButtonSubtitle__g5iTZ.typography_button__Uyx6e 72.7x14.6 rgb(97, 153, 246) T:1px solid rgb( |

Child layers that carry the look: figure 24x24 border 1px solid #81859f `core.color.grey.60` radius 12px; span 72.7x14.6 background #6199f6 `core.color.turquoiseTriumph` border 1px solid #6199f6 `core.color.turquoiseTriumph` radius 100px.

![Billing toggle (annual) default](components/crops/price-toggle-alt-default.png) ![Billing toggle (annual) hover](components/crops/price-toggle-alt-hover.png) ![Billing toggle (annual) focus-visible](components/crops/price-toggle-alt-focus-visible.png) ![Billing toggle (annual) pressed](components/crops/price-toggle-alt-pressed.png)

#### Plan card
A pricing plan card (Free / Pro / Team / Enterprise, $0–$25 monthly); the card wrapping a "Sign Up Now" CTA. Read as `plan-card` on the pricing page.

**Values (default).** size 252 x 796.59; padding 24px; border 1px solid rgba(157, 157, 255, 0.1); radius 10px; background rgba(16, 16, 23, 0.5) `dark.theme.surface.card`; shadow #181826 12px 12px 50px 0px inset, rgba(0, 0, 0, 0.31) 84.68px 149.711px 80px 0px, rgba(0, 0, 0, 0.26) 54.885px 97.035px 46.852px 0px, rgba(0, 0, 0, 0.23) 32.618px 57.666px 25.481px 0px, rgba(0, 0, 0, 0.2) 16.936px 29.942px 13px 0px, rgba(0, 0, 0, 0.18) 6.9px 12.199px 6.519px 0px, rgba(0, 0, 0, 0.2) 1.568px 2.772px 3.148px 0px; text NeueMachinaInktrap 12/10.8 400, #6199f6 `core.color.turquoiseTriumph`; icon 16 x 17, #fcfcfc `dark.theme.fg.declared`.

![Plan card default](components/crops/plan-card-default.png)

#### Plan CTA
A plan card's "Sign Up Now" button; measured, never followed or clicked (it begins account creation). Read as `plan-signup` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 202 x 39.75; padding 0px 24px; radius 100px; background transparent; text FrameGothic 14/13.44 600, #000000 `core.color.alpha.black.100`; transition color 0.3s cubic-bezier(0, 0.44, 0.6, 1); layers ::before rgb(245, 245, 248) 1px none 1; ::after rgba(0, 0, 0, 0) 0px rgb(193, 194, 217) 0px 0px 0px 2px inset 0; a::before.Button_white__XYP1F.Button_base__1G9eD 200pxx37.75px rgb(245, 245, 248) T:1px solid rgb(193, 194, 217) / R:1px solid rgb(193, 194, 217) / B:1px solid rgb(193, 194, 217) / L:1px solid rgb(193, 194, 217) 100px |
| hover | layers ::before rgb(245, 245, 248) 1px none 1; ::after rgba(0, 0, 0, 0) 0px rgb(252, 252, 252) 0px 0px 0px 2px inset 0; a::before.Button_white__XYP1F.Button_base__1G9eD 200pxx37.75px rgb(245, 245, 248) T:1px solid rgb(193, 194, 217) / R:1px solid rgb(193, 194, 217) / B:1px solid rgb(193, 194, 217) / L:1px solid rgb(193, 194, 217) 100px |
| focus-visible | outline 1px dotted #fcfcfc `dark.theme.fg.declared`, offset 1px; layers ::before rgba(233, 233, 255, 0.706) 1px none 1; ::after rgba(0, 0, 0, 0) 0px rgb(193, 194, 217) 0px 0px 0px 2px inset 0; a.Button_white__XYP1F.Button_base__1G9eD 202.0x39.8 1px dotted rgb(252, 252, 252) offset 1px 100px; a::before.Button_white__XYP1F.Button_base__1G9eD 200pxx37.75px rgba(233, 233, 255, 0.706) T:1px solid rgb(193, 194, 217) / R:1px solid rgb(193, 194, 217) / B:1px solid rgb(193, 19 |
| pressed | text FrameGothic 14/13.44 600, #a3a3a3; layers ::before rgba(245, 245, 248, 0.353) 0px none 1; ::after rgba(0, 0, 0, 0) 0px rgba(209, 209, 251, 0.2) 0px 0px 0px 4px inset 0.648422; a::before.Button_white__XYP1F.Button_base__1G9eD 202pxx39.75px rgba(245, 245, 248, 0.353) 100px; a::after.Button_white__XYP1F.Button_base__1G9eD 202pxx39.75px rgba(209, 209, 251, 0.2) 0px 0px 0px 4px inset 100px |

Child layers that carry the look: a::before 200pxx37.75px background #f5f5f8 `dark.theme.accent` border 1px solid #c1c2d9 `core.color.grey.80` radius 100px.

![Plan CTA default](components/crops/plan-signup-default.png) ![Plan CTA hover](components/crops/plan-signup-hover.png) ![Plan CTA focus-visible](components/crops/plan-signup-focus-visible.png) ![Plan CTA pressed](components/crops/plan-signup-pressed.png)

#### Plan trial CTA
A plan card's "Start Free Trial" button; measured, never followed. Read as `plan-trial` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 202 x 39.75; padding 0px 24px; radius 100px; background transparent; text FrameGothic 14/13.44 600, #000000 `core.color.alpha.black.100`; transition color 0.3s cubic-bezier(0, 0.44, 0.6, 1); layers ::before rgb(245, 245, 248) 1px none 1; ::after rgba(0, 0, 0, 0) 0px rgb(193, 194, 217) 0px 0px 0px 2px inset 0; a::before.Button_white__XYP1F.Button_base__1G9eD 200pxx37.75px rgb(245, 245, 248) T:1px solid rgb(193, 194, 217) / R:1px solid rgb(193, 194, 217) / B:1px solid rgb(193, 194, 217) / L:1px solid rgb(193, 194, 217) 100px |
| hover | layers ::before rgba(233, 233, 255, 0.7) 1px none 1; ::after rgba(0, 0, 0, 0) 0px rgb(252, 252, 252) 0px 0px 0px 2px inset 1; a::before.Button_white__XYP1F.Button_base__1G9eD 200pxx37.75px rgba(233, 233, 255, 0.7) T:1px solid rgb(193, 194, 217) / R:1px solid rgb(193, 194, 217) / B:1px solid rgb(193, 194, 217) / L:1px solid rgb(193, 194, 217) 100px; a::after.Button_white__XYP1F.Button_base__1G9eD 202pxx39 |
| focus-visible | outline 1px dotted #fcfcfc `dark.theme.fg.declared`, offset 1px; layers ::before rgba(240, 240, 251, 0.843) 1px none 1; ::after rgba(0, 0, 0, 0) 0px rgb(193, 194, 217) 0px 0px 0px 2px inset 0; a.Button_white__XYP1F.Button_base__1G9eD 202.0x39.8 1px dotted rgb(252, 252, 252) offset 1px 100px; a::before.Button_white__XYP1F.Button_base__1G9eD 200pxx37.75px rgba(240, 240, 251, 0.843) T:1px solid rgb(193, 194, 217) / R:1px solid rgb(193, 194, 217) / B:1px solid rgb(193, 19 |
| pressed | text FrameGothic 14/13.44 600, #fcfcfc `dark.theme.fg.declared`; layers ::before rgba(0, 0, 0, 0) 0px none 1; ::after rgba(0, 0, 0, 0) 0px rgba(209, 209, 251, 0.2) 0px 0px 0px 4px inset 1; a::after.Button_white__XYP1F.Button_base__1G9eD 202pxx39.75px rgba(209, 209, 251, 0.2) 0px 0px 0px 4px inset 100px |

Child layers that carry the look: a::before 200pxx37.75px background #f5f5f8 `dark.theme.accent` border 1px solid #c1c2d9 `core.color.grey.80` radius 100px.

![Plan trial CTA default](components/crops/plan-trial-default.png) ![Plan trial CTA hover](components/crops/plan-trial-hover.png) ![Plan trial CTA focus-visible](components/crops/plan-trial-focus-visible.png) ![Plan trial CTA pressed](components/crops/plan-trial-pressed.png)

#### Plan meeting CTA
The Enterprise card's "Book a Meeting" button; measured, never followed. Read as `plan-meeting` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 202 x 39.75; padding 0px 24px; radius 100px; background transparent; text FrameGothic 14/13.44 600, #000000 `core.color.alpha.black.100`; transition color 0.3s cubic-bezier(0, 0.44, 0.6, 1); layers ::before rgb(245, 245, 248) 1px none 1; ::after rgba(0, 0, 0, 0) 0px rgb(193, 194, 217) 0px 0px 0px 2px inset 0; button::before.Button_white__XYP1F.Button_base__1G9eD 200pxx37.75px rgb(245, 245, 248) T:1px solid rgb(193, 194, 217) / R:1px solid rgb(193, 194, 217) / B:1px solid rgb(193, 194, 217) / L:1px solid rgb(193, 194, 217) 100px |
| hover | layers ::before rgba(233, 233, 255, 0.7) 1px none 1; ::after rgba(0, 0, 0, 0) 0px rgb(252, 252, 252) 0px 0px 0px 2px inset 1; button::before.Button_white__XYP1F.Button_base__1G9eD 200pxx37.75px rgba(233, 233, 255, 0.7) T:1px solid rgb(193, 194, 217) / R:1px solid rgb(193, 194, 217) / B:1px solid rgb(193, 194, 217) / L:1px solid rgb(193, 194, 217) 100px; button::after.Button_white__XYP1F.Button_base__1G9e |
| focus-visible | outline 1px dotted #fcfcfc `dark.theme.fg.declared`, offset 0px; layers ::before rgba(237, 237, 253, 0.776) 1px none 1; ::after rgba(0, 0, 0, 0) 0px rgb(193, 194, 217) 0px 0px 0px 2px inset 0; button.Button_white__XYP1F.Button_base__1G9eD 202.0x39.8 1px dotted rgb(252, 252, 252) offset 0px 100px; button::before.Button_white__XYP1F.Button_base__1G9eD 200pxx37.75px rgba(237, 237, 253, 0.776) T:1px solid rgb(193, 194, 217) / R:1px solid rgb(193, 194, 217) / B:1px solid r |
| pressed | text FrameGothic 14/13.44 600, #eaeaea; layers ::before rgba(245, 245, 248, 0.07) 0px none 1; ::after rgba(0, 0, 0, 0) 0px rgba(209, 209, 251, 0.2) 0px 0px 0px 4px inset 0.929097; button::before.Button_white__XYP1F.Button_base__1G9eD 202pxx39.75px rgba(245, 245, 248, 0.07) 100px; button::after.Button_white__XYP1F.Button_base__1G9eD 202pxx39.75px rgba(209, 209, 251, 0.2) 0px 0px 0px 4px inset 100px |

Child layers that carry the look: button::before 200pxx37.75px background #f5f5f8 `dark.theme.accent` border 1px solid #c1c2d9 `core.color.grey.80` radius 100px.

![Plan meeting CTA default](components/crops/plan-meeting-default.png) ![Plan meeting CTA hover](components/crops/plan-meeting-hover.png) ![Plan meeting CTA focus-visible](components/crops/plan-meeting-focus-visible.png) ![Plan meeting CTA pressed](components/crops/plan-meeting-pressed.png)

#### Feature-comparison accordion
A category row in the feature-comparison table (Users, Storage, Projects & workspaces, Feedback & collaboration, … — the rows mount expanded); the closed state was measured after clicking the row — a local UI toggle. Read as `ptable-acc` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: closed) | size 1080 x 36.09; padding 0px 0px 10px 0px; background transparent; text FrameGothic 18/26.1 400, #fcfcfc `dark.theme.fg.declared`; icon 10 x 10, #fcfcfc `dark.theme.fg.declared` |

![Feature-comparison accordion default](components/crops/ptable-acc-default.png) ![Feature-comparison accordion closed](components/crops/ptable-acc-closed.png)

#### FAQ accordion
A question row in the pricing FAQ; the opened state was measured after clicking it — a local UI toggle. Read as `faq-acc` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: opened) | size 1080 x 19.5; background transparent; text FrameGothic 15/19.5 500, #fcfcfc `dark.theme.fg.declared`; icon 16 x 16, #fcfcfc `dark.theme.fg.declared` |

![FAQ accordion default](components/crops/faq-acc-default.png) ![FAQ accordion opened](components/crops/faq-acc-opened.png)

### Contact

The /contact hub — 'Hello, how can we help you?' — with the white 'Schedule a Meeting' button (it mounts a Calendly scheduler — a vendor widget, never opened) and the 'Talk with Sales' text link.

#### Contact headline
"Hello, how can we help you?" — the /contact hub. Read as `contact-h1` on the contact page.

**Values (default).** size 712 x 166.38; background transparent; text FrameGothic 80/83.2 600, #fcfcfc `dark.theme.fg.declared`.

![Contact headline default](components/crops/contact-h1-default.png)

#### Schedule a Meeting
The white "Schedule a Meeting" button on /contact (it mounts a Calendly scheduler — a vendor widget, never opened); measured, never pressed. Read as `schedule-btn` on the contact page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 186.53 x 39.75; padding 0px 24px; radius 100px; background transparent; text FrameGothic 14/13.44 600, #000000 `core.color.alpha.black.100`; transition color 0.3s cubic-bezier(0, 0.44, 0.6, 1); layers ::before rgb(245, 245, 248) 1px none 1; ::after rgba(0, 0, 0, 0) 0px rgb(193, 194, 217) 0px 0px 0px 2px inset 0; button::before.Button_white__XYP1F.Button_base__1G9eD 184.531pxx37.75px rgb(245, 245, 248) T:1px solid rgb(193, 194, 217) / R:1px solid rgb(193, 194, 217) / B:1px solid rgb(193, 194, 217) / L:1px solid rgb(193, 194, 217) 100px |
| hover | layers ::before rgba(233, 233, 255, 0.7) 1px none 1; ::after rgba(0, 0, 0, 0) 0px rgb(252, 252, 252) 0px 0px 0px 2px inset 1; button::before.Button_white__XYP1F.Button_base__1G9eD 184.531pxx37.75px rgba(233, 233, 255, 0.7) T:1px solid rgb(193, 194, 217) / R:1px solid rgb(193, 194, 217) / B:1px solid rgb(193, 194, 217) / L:1px solid rgb(193, 194, 217) 100px; button::after.Button_white__XYP1F.Button_base__ |
| focus-visible | outline 1px dotted #fcfcfc `dark.theme.fg.declared`, offset 0px; layers ::before rgba(233, 233, 255, 0.7) 1px none 1; ::after rgba(0, 0, 0, 0) 0px rgb(193, 194, 217) 0px 0px 0px 2px inset 0; button.Button_white__XYP1F.Button_base__1G9eD 186.5x39.8 1px dotted rgb(252, 252, 252) offset 0px 100px; button::before.Button_white__XYP1F.Button_base__1G9eD 184.531pxx37.75px rgba(233, 233, 255, 0.7) T:1px solid rgb(193, 194, 217) / R:1px solid rgb(193, 194, 217) / B:1px solid r |
| pressed | text FrameGothic 14/13.44 600, #fcfcfc `dark.theme.fg.declared`; layers ::before rgba(0, 0, 0, 0) 0px none 1; ::after rgba(0, 0, 0, 0) 0px rgba(209, 209, 251, 0.2) 0px 0px 0px 4px inset 1; button::after.Button_white__XYP1F.Button_base__1G9eD 186.531pxx39.75px rgba(209, 209, 251, 0.2) 0px 0px 0px 4px inset 100px |

Child layers that carry the look: button::before 184.531pxx37.75px background #f5f5f8 `dark.theme.accent` border 1px solid #c1c2d9 `core.color.grey.80` radius 100px.

![Schedule a Meeting default](components/crops/schedule-btn-default.png) ![Schedule a Meeting hover](components/crops/schedule-btn-hover.png) ![Schedule a Meeting focus-visible](components/crops/schedule-btn-focus-visible.png) ![Schedule a Meeting pressed](components/crops/schedule-btn-pressed.png)

#### Talk with Sales
The "Talk with Sales" text-link button on /contact (leads to /contact/form); measured, never followed. Read as `sales-link` on the contact page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 132 x 32; padding 0px 24px 16px 0px; background transparent; text FrameGothic 16/16 400, #f5f5f8 `dark.theme.accent`; transition color 0.3s cubic-bezier(0.28, 0.44, 0.49, 1); layers ::before rgba(0, 0, 0, 0) 0px none 1 |
| hover | text FrameGothic 16/16 400, #fcfcfc `dark.theme.fg.declared` |
| focus-visible | outline 1px dotted #fcfcfc `dark.theme.fg.declared`, offset 0px; layers ::before rgba(0, 0, 0, 0) 0px none 1; button.Button_textLink__A_4Vq.Button_base__1G9eD 132.0x32.0 1px dotted rgb(252, 252, 252) offset 0px |
| pressed | text FrameGothic 16/16 400, #fcfcfc `dark.theme.fg.declared` |

![Talk with Sales default](components/crops/sales-link-default.png) ![Talk with Sales hover](components/crops/sales-link-hover.png) ![Talk with Sales focus-visible](components/crops/sales-link-focus-visible.png) ![Talk with Sales pressed](components/crops/sales-link-pressed.png)

### Contact form

The /contact/form card: 'Enter your info below. We'll get back to you shortly.' with underlined Name/Email/Message fields and the Submit pill — photographed empty, never typed into, never submitted.

#### Contact form card
The dark form card on /contact/form — "Enter your info below. We'll get back to you shortly." with Name/Email/Message fields and a Submit pill; never submitted. Read as `form-panel` on the contact form page.

**Values (default).** size 1440 x 1543.47; background transparent; text FrameGothic 80/83.2 600, #fcfcfc `dark.theme.fg.declared`; layers div.PageSection_pageSection__8v9It.PageSection_isNextSectionSameLevel__ujiEc 1440.0x1543.5 rgb(0, 0, 0); div.Form_inner__RZlVF.global_subgrid__ZRhT6 1080.0x545.8 rgba(13, 13, 24, 0.5) T:1px solid rgba(189, 189, 244, 0.1) / R:1px solid rgba(189, 189, 244, 0.1) / B:1px solid rgba(189, 189, 244, 0.1) / L:1px solid rgba(189, 189, 244, 0.1) 5px; input.TextInput_textInput__d8dTK.typography_body__vVxn5 4.

Child layers that carry the look: div 1440x1543.5 background #000000 `core.color.alpha.black.100`; div 1080x545.8 background rgba(13, 13, 24, 0.5) `core.color.alpha.cinder.50` border 1px solid rgba(189, 189, 244, 0.1) `core.color.alpha.light.10` radius 5px; input 431x48 border 1px solid #2e2f40 `core.color.grey.20`.

![Contact form card default](components/crops/form-panel-default.png)

#### Name field
The underlined "Name" input; photographed empty; focus lands in the field; nothing is typed. Read as `form-name` on the contact form page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 431 x 48; padding 1px 2px; border B: 1px solid #2e2f40 `core.color.grey.20`; background transparent; text FrameGothic 15/21.75 400, #dedfee `core.color.grey.90`; transition border-color 0.3s cubic-bezier(0.25, 0.1, 0.25, 1); placeholder #dedfee `core.color.grey.90`; layers input.TextInput_textInput__d8dTK.typography_body__vVxn5 431.0x48.0 B:1px solid rgb(46, 47, 64) |
| focused | border B: 1px solid #fcfcfc `dark.theme.fg.declared`; layers input.TextInput_textInput__d8dTK.typography_body__vVxn5 431.0x48.0 B:1px solid rgb(252, 252, 252) |

Child layers that carry the look: input 431x48 border 1px solid #2e2f40 `core.color.grey.20`.

![Name field default](components/crops/form-name-default.png) ![Name field focused](components/crops/form-name-focused.png)

#### Email field
The underlined "Email" input; photographed empty; focus lands in the field; nothing is typed. Read as `form-email` on the contact form page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 431 x 48; padding 1px 2px; border B: 1px solid #2e2f40 `core.color.grey.20`; background transparent; text FrameGothic 15/21.75 400, #dedfee `core.color.grey.90`; transition border-color 0.3s cubic-bezier(0.25, 0.1, 0.25, 1); placeholder #dedfee `core.color.grey.90`; layers input.TextInput_textInput__d8dTK.typography_body__vVxn5 431.0x48.0 B:1px solid rgb(46, 47, 64) |
| focused | border B: 1px solid #fcfcfc `dark.theme.fg.declared`; layers input.TextInput_textInput__d8dTK.typography_body__vVxn5 431.0x48.0 B:1px solid rgb(252, 252, 252) |

Child layers that carry the look: input 431x48 border 1px solid #2e2f40 `core.color.grey.20`.

![Email field default](components/crops/form-email-default.png) ![Email field focused](components/crops/form-email-focused.png)

#### Message field
The underlined "Message" input; photographed empty; focus lands in the field; nothing is typed. Read as `form-message` on the contact form page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 886 x 48; padding 1px 2px; border B: 1px solid #2e2f40 `core.color.grey.20`; background transparent; text FrameGothic 15/21.75 400, #dedfee `core.color.grey.90`; transition border-color 0.3s cubic-bezier(0.25, 0.1, 0.25, 1); placeholder #dedfee `core.color.grey.90`; layers input.TextInput_textInput__d8dTK.typography_body__vVxn5 886.0x48.0 B:1px solid rgb(46, 47, 64) |
| focused | border B: 1px solid #fcfcfc `dark.theme.fg.declared`; layers input.TextInput_textInput__d8dTK.typography_body__vVxn5 886.0x48.0 B:1px solid rgb(252, 252, 252) |

Child layers that carry the look: input 886x48 border 1px solid #2e2f40 `core.color.grey.20`.

![Message field default](components/crops/form-message-default.png) ![Message field focused](components/crops/form-message-focused.png)

#### Submit
The form's pill "Submit" button; its states were measured but the button was never clicked — nothing was sent. Read as `form-submit` on the contact form page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 97.84 x 39.75; padding 0px 24px; radius 100px; background transparent; text FrameGothic 14/13.44 600, #4f5167 `core.color.grey.40`; transition color 0.3s cubic-bezier(0, 0.44, 0.6, 1); layers ::before rgba(189, 189, 244, 0.1) 1px none 1; ::after rgba(0, 0, 0, 0) 0px rgb(193, 194, 217) 0px 0px 0px 2px inset 0; button::before.Button_white__XYP1F.Button_base__1G9eD 95.8438pxx37.75px rgba(189, 189, 244, 0.1) T:1px solid rgb(193, 194, 217) / R:1px solid rgb(193, 194, 217) / B:1px solid rgb(193, 194, 217) / L:1px solid rgb(193, 194, 217) 100px; div::after.SubmitButtonAnimation_dot__vO6gD 2.5 |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

Child layers that carry the look: button::before 95.8438pxx37.75px background rgba(189, 189, 244, 0.1) `core.color.alpha.light.10` border 1px solid #c1c2d9 `core.color.grey.80` radius 100px; div::after 2.5pxx2.5px background #fcfcfc `dark.theme.fg.declared` radius 50%.

![Submit default](components/crops/form-submit-default.png) ![Submit hover](components/crops/form-submit-hover.png) ![Submit pressed](components/crops/form-submit-pressed.png)

### Sign-in surface (accounts.frame.io — a different stack)

accounts.frame.io/welcome — where 'Sign In' lands — the light styled-components sign-in card: 'Welcome / Enter your email to get started.', one e-mail field and the cobalt 'Let's go' submit. A different stack that does not share the marketing --* layer; measured as a form, never submitted.

#### Sign-in panel
The accounts.frame.io/welcome sign-in card — the Frame.io mark, "Welcome / Enter your email to get started.", an e-mail field and a "Let's go" submit on a light page (styled-components — a different stack from the marketing site); never submitted. Read as `login-panel` on the sign-in page.

**Values (default).** size 346 x 345.84; background transparent; text Avenir Next 24/normal 700, #000000 `core.color.alpha.black.100`; icon 56 x 64, #000000 `core.color.alpha.black.100`; layers input.TextInput__Input-a3o9vm-1.irdNuq 346.0x40.0 rgb(255, 255, 255) T:1px solid rgb(224, 71, 95) / R:1px solid rgb(224, 71, 95) / B:1px solid rgb(224, 71, 95) / L:1px solid rgb(224, 71, 95) 4px; button.Button__StyledButton-tzx5l-0.fmdBhl 346.0x40.0 rgb(91, 83, 255) rgba(0, 0, 0, 0) 0px 0px 0px 0px inset 6px.

Child layers that carry the look: input 346x40 background #ffffff `core.component.productShell.login-field-bg` border 1px solid #e0475f radius 4px; button 346x40 background #5b53ff `core.color.brand.cobalt.default` radius 6px shadow transparent 0px 0px 0px 0px inset.

![Sign-in panel default](components/crops/login-panel-default.png)

#### Email field (sign-in)
The "Email" input with placeholder "you@example.com"; photographed empty; focus lands in the field; nothing is typed. Read as `login-email` on the sign-in page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 346 x 40; padding 12px; border 1px solid #e0475f; radius 4px; background #ffffff `core.component.productShell.login-field-bg`; text Avenir Next 14/21 400, #20222b; transition background-color 0.3s ease; placeholder #7d829c |
| focused | border 1px solid #5b53ff `core.color.brand.cobalt.default`; shadow rgba(91, 83, 255, 0.1) 0px 0px 8px 0px |

![Email field (sign-in) default](components/crops/login-email-default.png) ![Email field (sign-in) focused](components/crops/login-email-focused.png)

#### Let's go submit
The cobalt "Let's go" submit; its states were measured but the button was never clicked — nothing was submitted. Read as `login-submit` on the sign-in page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 346 x 40; padding 0px 12px; radius 6px; background #5b53ff `core.color.brand.cobalt.default`; text Avenir Next 14/14 700, #ffffff `core.component.productShell.login-field-bg`; transition background-color 0.2s ease, color 0.2s ease, box-shadow 0.2s ease, opacity 0.0002s ease |
| hover | background #564ef2 |
| focus-visible | shadow #53afff 0px 0px 0px 1px inset, #53afff 0px 0px 4px 1px |
| pressed | background #514ae5 |

![Let's go submit default](components/crops/login-submit-default.png) ![Let's go submit hover](components/crops/login-submit-hover.png) ![Let's go submit focus-visible](components/crops/login-submit-focus-visible.png) ![Let's go submit pressed](components/crops/login-submit-pressed.png)

### Customers, case study, integrations, what's new

The gallery surfaces: the /customers index and a published case study (Ford), the /integrations cards and the /whats-new release index — published marketing content, measured at rest, never followed.

#### Customers headline
The /customers masthead. Read as `cust-h1` on the customers page.

**Values (default).** size 528 x 166.38; background transparent; text FrameGothic 80/83.2 600, #fcfcfc `dark.theme.fg.declared`.

![Customers headline default](components/crops/cust-h1-default.png)

#### Customer card
A customer-story card on /customers; measured, never followed. Read as `cust-card` on the customers page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 1080 x 220; background transparent; text FrameGothic 80/57.6 500, #fcfcfc `dark.theme.fg.declared`; layers div.StatsCard_statsCard__U67L3.global_cardHover__VD7I6 344.0x220.0 10px; div::after.StatsCard_statsCard__U67L3.global_cardHover__VD7I6 342pxx218px T:1px solid rgba(157, 157, 255, 0.05) / R:1px solid rgba(157, 157, 255, 0.05) / B:1px solid rgba(157, 157, 255, 0.05) / L:1px solid rgba(157, 157, 255, 0.05) 5px; div.StatsCard_statsCard__U67L3.global_cardHover__VD7I6 344.0x220.0 10px; div::after.StatsC |

Child layers that carry the look: div 344x220 image linear-gradient(140deg, #1b1b26 -41.97%, #09090d 77.06%) radius 10px; div::after 342pxx218px border 1px solid rgba(157, 157, 255, 0.05) `core.color.alpha.light.5` radius 5px; div 344x220 image linear-gradient(140deg, #1b1b26 -41.97%, #09090d 77.06%) radius 10px.

![Customer card default](components/crops/cust-card-default.png) ![Customer card hover](components/crops/cust-card-hover.png)

#### Case-study headline
The masthead of a published case study (Ford); published editorial content, measured at rest. Read as `cs-h1` on the case study page.

**Values (default).** size 712 x 83.19; background transparent; text FrameGothic 80/83.2 600, #fcfcfc `dark.theme.fg.declared`.

![Case-study headline default](components/crops/cs-h1-default.png)

#### Integrations headline
The /integrations masthead. Read as `int-h1` on the integrations page.

**Values (default).** size 712 x 166.38; background transparent; text FrameGothic 80/83.2 600, #fcfcfc `dark.theme.fg.declared`.

![Integrations headline default](components/crops/int-h1-default.png)

#### Integration card
An integration card on /integrations; measured, never followed. Read as `int-card` on the integrations page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 252 x 82; padding 26px 28px 28px 28px; border 1px solid rgba(157, 157, 255, 0.05) `core.color.alpha.light.5`; radius 5px; background #12131d `core.color.grey.08`; text FrameGothic 11/13.75 500, #a3a4bf `core.color.grey.70`; transition background-color 0.5s cubic-bezier(0, 0.44, 0.6, 1), border-color 0.5s cubic-bezier(0, 0.44, 0.6, 1); icon 26 x 21, #fcfcfc `dark.theme.fg.declared` |
| hover | border 1px solid rgba(37, 39, 54, 0.996); background rgba(18, 19, 29, 0.004) |

![Integration card default](components/crops/int-card-default.png) ![Integration card hover](components/crops/int-card-hover.png)

#### What's New headline
The /whats-new release-notes index masthead. Read as `wn-h1` on the what's new page.

**Values (default).** size 1080 x 166.38; background transparent; text FrameGothic 80/83.2 600, #fcfcfc `dark.theme.fg.declared`.

![What's New headline default](components/crops/wn-h1-default.png)

#### Release card
A release-note card on /whats-new; measured, never followed. Read as `wn-card` on the what's new page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 528 x 466.2; background transparent; text FrameGothic 20/24.6 600, #fcfcfc `dark.theme.fg.declared`; icon 4.44 x 7.5, #f5f5f8 `dark.theme.accent`; layers span::after.AnimatedSvgArrow_cssTail__yibfW 20pxx1.65625px rgb(245, 245, 248) 1px |

Child layers that carry the look: span::after 20pxx1.65625px background #f5f5f8 `dark.theme.accent` radius 1px.

![Release card default](components/crops/wn-card-default.png) ![Release card hover](components/crops/wn-card-hover.png)

### Mobile (390 wide)

The phone surface at 390 wide: the header with the nav button and 'Start Free Trial' pill, the full-viewport nav overlay opened by 'Toggle mobile navigation', the hero and CTA.

#### Mobile top bar
The phone header at 390 wide: the Frame.io mark, "Start Free Trial" and the nav button. Read as `m-topbar` on the home page at 390 wide.

**Values (default).** size 390 x 120; background transparent; text FrameGothic 12/12 600, #fcfcfc `dark.theme.fg.declared`; transition transform 0.5s cubic-bezier(0.42, 0, 0.28, 0.99); icon 24 x 24, #fcfcfc `dark.theme.fg.declared`; layers div.AnnouncementBanner_announcementBanner__g9QLM.Navigation_navigationBannerEl__zSvOh 390.0x48.0 rgb(91, 83, 255); span.ToggleButton_navMobileButtonLineEl__IvuHL 5.7x5.7 rgb(240, 240, 247) 9.33333px; span.ToggleButton_navMobileButtonLineEl__IvuHL 5.7x5.7 rgb(240, 240, 247) 9.33333px; span.ToggleButton_navMobileButtonLineEl__IvuHL 5.7x5.7 rgb(240, 240, 247) 9.33333px; span.ToggleButton_navMobileBut.

Child layers that carry the look: div 390x48 background #5b53ff `core.color.brand.cobalt.default` image linear-gradient(355deg, rgba(255, 255, 255, 0.15) 4.03%, rgba(255, 255, 255, 0) 95.81%), n; span 5.7x5.7 background #f0f0f7 `core.color.grey.95` radius 9.33333px; span 5.7x5.7 background #f0f0f7 `core.color.grey.95` radius 9.33333px.

![Mobile top bar default](components/crops/m-topbar-default.png)

#### Drawer CTA
The nav overlay's white "Start Free Trial" pill at 390 wide — the closed top bar carries none (mark, Sign In and the menu button only); measured with the drawer open, never followed. Read as `m-cta` on the home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 165 x 37.75; padding 0px 24px; radius 100px; background transparent; text FrameGothic 14/13.44 600, #000000 `core.color.alpha.black.100`; transition color 0.3s cubic-bezier(0, 0.44, 0.6, 1); layers ::before rgb(245, 245, 248) 1px none 1; ::after rgba(0, 0, 0, 0) 0px rgb(193, 194, 217) 0px 0px 0px 2px inset 0 |
| pressed | text FrameGothic 14/13.44 600, #fcfcfc `dark.theme.fg.declared`; layers ::before rgba(0, 0, 0, 0) 0px none 1; ::after rgba(0, 0, 0, 0) 0px rgba(209, 209, 251, 0.2) 0px 0px 0px 4px inset 1 |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Mobile menu button
The "Toggle mobile navigation" button — a local UI toggle; the opened state was measured after activating it. Read as `m-menu-btn` on the home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 25 x 20; background transparent; text Arial 13.33/normal 400, #fcfcfc `dark.theme.fg.declared`; transform matrix(0, -1, 1, 0, 0, 0); layers span.ToggleButton_navMobileButtonLineEl__IvuHL 5.7x5.7 rgb(240, 240, 247) 9.33333px; span.ToggleButton_navMobileButtonLineEl__IvuHL 5.7x5.7 rgb(240, 240, 247) 9.33333px; span.ToggleButton_navMobileButtonLineEl__IvuHL 5.7x5.7 rgb(240, 240, 247) 9.33333px; span.ToggleButton_navMobileButtonLineEl__IvuHL 5.7x5.7 rgb(240, 240, 247) 9.33333px |
| focus-visible | outline 1px dotted #fcfcfc `dark.theme.fg.declared`, offset 0px; layers button.ToggleButton_navMobileButton__WW3qe 25.0x20.0 1px dotted rgb(252, 252, 252) offset 0px; span.ToggleButton_navMobileButtonLineEl__IvuHL 5.7x5.7 rgb(240, 240, 247) 9.33333px; span.ToggleButton_navMobileButtonLineEl__IvuHL 5.7x5.7 rgb(240, 240, 247) 9.33333px; span.ToggleButton_navMobileButtonLineEl__IvuHL 5.7x5.7 rgb(240, 240, 247) 9.33333px; span.ToggleButton_navMobileButtonLineEl__IvuHL 5.7 |
| opened | size 20.15 x 23.77; transform matrix(0.849411, -0.126644, 0.126644, 0.849411, 0, 0); layers span.ToggleButton_navMobileButtonLineEl__IvuHL 9.3x7.5 rgb(240, 240, 247) 9.33333px; span.ToggleButton_navMobileButtonLineEl__IvuHL 7.5x9.3 rgb(240, 240, 247) 9.33333px; span.ToggleButton_navMobileButtonLineEl__IvuHL 9.3x7.5 rgb(240, 240, 247) 9.33333px; span.ToggleButton_navMobileButtonLineEl__IvuHL 7.5x9.3 rgb(240, 240, 247) 9.33333px |

Child layers that carry the look: span 5.7x5.7 background #f0f0f7 `core.color.grey.95` radius 9.33333px; span 5.7x5.7 background #f0f0f7 `core.color.grey.95` radius 9.33333px; span 5.7x5.7 background #f0f0f7 `core.color.grey.95` radius 9.33333px.

![Mobile menu button default](components/crops/m-menu-btn-default.png) ![Mobile menu button hover](components/crops/m-menu-btn-hover.png) ![Mobile menu button focus-visible](components/crops/m-menu-btn-focus-visible.png) ![Mobile menu button pressed](components/crops/m-menu-btn-pressed.png) ![Mobile menu button opened](components/crops/m-menu-btn-opened.png)

#### Mobile nav overlay
The nav list inside the overlay opened by the menu button; its links were never followed. Read as `m-drawer` on the home page at 390 wide.

**Values (default).** size 342 x 210; background transparent; text FrameGothic 30/34.5 600, #fcfcfc `dark.theme.fg.declared`; icon 30 x 15, #fcfcfc `dark.theme.fg.declared`.

![Mobile nav overlay default](components/crops/m-drawer-default.png)

#### Mobile hero headline
The masthead at 390 wide. Read as `m-hero-h1` on the home page at 390 wide.

**Values (default).** size 342 x 145.17; background transparent; text FrameGothic 44/48.4 600, #fcfcfc `dark.theme.fg.declared`.

![Mobile hero headline default](components/crops/m-hero-h1-default.png)

#### Mobile hero CTA
The hero "Start Free Trial" button at 390 wide; measured never followed. Read as `m-hero-cta` on the home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 342 x 37.75; padding 0px 24px; radius 100px; background transparent; text FrameGothic 14/13.44 600, #000000 `core.color.alpha.black.100`; transition color 0.3s cubic-bezier(0, 0.44, 0.6, 1); layers ::before rgb(245, 245, 248) 1px none 1; ::after rgba(0, 0, 0, 0) 0px rgb(193, 194, 217) 0px 0px 0px 2px inset 0; a::before.Button_white__XYP1F.Button_base__1G9eD 340pxx35.75px rgb(245, 245, 248) T:1px solid rgb(193, 194, 217) / R:1px solid rgb(193, 194, 217) / B:1px solid rgb(193, 194, 217) / L:1px solid rgb(193, 194, 217) 100px |
| focus-visible | outline 1px dotted #fcfcfc `dark.theme.fg.declared`, offset 1px; layers ::before rgb(245, 245, 248) 1px none 1; ::after rgba(0, 0, 0, 0) 0px rgb(193, 194, 217) 0px 0px 0px 2px inset 0; a.Button_white__XYP1F.Button_base__1G9eD 342.0x37.8 1px dotted rgb(252, 252, 252) offset 1px 100px; a::before.Button_white__XYP1F.Button_base__1G9eD 340pxx35.75px rgb(245, 245, 248) T:1px solid rgb(193, 194, 217) / R:1px solid rgb(193, 194, 217) / B:1px solid rgb(193, 194, 217) / L:1px  |
| pressed | text FrameGothic 14/13.44 600, #fcfcfc `dark.theme.fg.declared`; layers ::before rgba(0, 0, 0, 0) 0px none 1; ::after rgba(0, 0, 0, 0) 0px rgba(209, 209, 251, 0.2) 0px 0px 0px 4px inset 1; a::after.Button_white__XYP1F.Button_base__1G9eD 342pxx37.75px rgba(209, 209, 251, 0.2) 0px 0px 0px 4px inset 100px |

Child layers that carry the look: a::before 340pxx35.75px background #f5f5f8 `dark.theme.accent` border 1px solid #c1c2d9 `core.color.grey.80` radius 100px.

![Mobile hero CTA default](components/crops/m-hero-cta-default.png) ![Mobile hero CTA hover](components/crops/m-hero-cta-hover.png) ![Mobile hero CTA focus-visible](components/crops/m-hero-cta-focus-visible.png) ![Mobile hero CTA pressed](components/crops/m-hero-cta-pressed.png)

## Icons

No standalone SVG icon set was lifted on this pass; the icons in the crops and screenshots (the Frame.io waveform mark, the mega-menu glyphs, integration logos, social glyphs) are the product's artwork. Declared under layoutGaps in the catalog entry.

| Icon | Rendered sizes | View box | Style | Seen on | Next to |
|---|---|---|---|---|---|

## Gaps

### The signed-in product

Frame.io's product is the review-and-approval app: projects, the commenting player, Camera to Cloud uploads, Drive, Transfer deliveries — every surface after 'Sign In' needs an account and was never reached. accounts.frame.io/welcome is the only app-adjacent surface a signed-out visitor sees, and it was measured as a form, never submitted. The product demos embedded in the marketing pages are videos and mocks, not the product.

### Pages

- **The account.** The app and every post-login surface (projects, the player, uploads, admin, billing) was never reached; the accounts.frame.io/welcome sign-in was measured as a form and never submitted.
- **Forms.** The /contact/form fields and the welcome email field were photographed empty — nothing was typed or sent; what a submission returns is unverified.
- **The /lp/* campaign landings and the remaining sitemap routes** are the same templates with different copy; a representative set was captured, not all 60+ public URLs.
- **Case studies, release notes, integration pages and blog posts** are index-level captures plus one case study; individual articles are the same templates, unmeasured.
- **Schedule a Meeting** mounts a Calendly scheduler — a third-party widget; the button was measured at rest and never pressed, so the scheduler frame is uncaptured.
- **Cookie preferences** opens the consent manager on demand; it was measured at rest and never pressed — no consent layer appeared for the en-US signed-out visitor otherwise.

### States

- **Pressed** was forced with DevTools on every control, so a state a script adds on mousedown (if any) is missing.
- **Disabled, error, loading and validation states** were not seen on the public surface — the forms were never submitted.
- **The Monthly/Annually billing switch** on /pricing re-prices the grid when flipped; it was measured at rest and never switched, so the annual price state is uncaptured.
- **Mega-menu items' focus/hover** is partially covered: the panel closes on blur, so a real keyboard focus inside it could not always be held.
- **The language selector** was measured at rest, never opened, so the locale list is uncaptured.

### Themes

Every public frame.io page paints the one dark theme — the near-black field with #fcfcfc ink resolved on `:root`; the site ships no `[data-theme]` scope and no toggle control, so `dark` is the package's only token set. accounts.frame.io/welcome is the lone light-painted public surface — a different stack, kept as measured component tokens, not a theme.

### Fonts

- **FrameGothic** (a 400-600 variable face, `--font-main`) carries every display heading, **NeueMachinaInktrap** (`--font-secondary`) the labels and kickers, and **Inter** (a 100-900 variable face, `--font-tertiary`) the UI and body copy — each with an Arial-metric fallback, self-hosted as woff/woff2 and declared on the Next.js font-variable classes. The style guide falls back to system sans.

### Screenshots

- The product demos, video frames, community thumbnails and photography in the screenshots are the product's published content.
- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files.

### Content left out

- Marketing copy, plan prices, job titles, plugin names and community author names are the product's content; only frames and components were measured.
