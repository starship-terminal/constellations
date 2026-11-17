# Column components

The discovery list of every page and view captured, then one entry per component with crops of the real product, and the Gaps. Captured from column.com on 2026-11-17, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running page. Nothing was signed into, paid for or submitted.

The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) (30 components, 58 states).

How to read an entry:

- A colour is its value followed by the palette token in [tokens.json](tokens.json) with the same value, when there is one. Text is written family size/line-height weight, then its colour, for example `SuisseIntl 16/24 400, #575a64`, and is read from the first text node inside the component.
- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example "default (same: focus-visible)". When the root paints nothing, "Child layers" names the first nodes inside it that do.
- Crops are images of the component read from the live page, in [components/crops/](components/crops) (42 files, named `{component}-{state}.png`, at 2x). Screenshots are in [screenshots/](screenshots).

## Discovery list

Screenshots are named `{page}-{theme}-{state}.png`; every public route paints the same light theme. Desktop shots are 1440 x 900 at 1x; `-full` shots are whole pages (1x on desktop, 2x on mobile); mobile shots are `mobile-{page}-{theme}-{state}.png`, 780 wide (390 at 2x).

| Surface | URL | Screenshots |
|---|---|---|
| Home | `/` | [default](screenshots/home-light-default.png), [full](screenshots/home-light-full.png) |
| ACH | `/ach/` | [default](screenshots/ach-light-default.png), [full](screenshots/ach-light-full.png) |
| Bank accounts | `/bank-accounts/` | [default](screenshots/bankaccounts-light-default.png), [full](screenshots/bankaccounts-light-full.png) |
| Book transfers | `/book-transfers/` | [default](screenshots/booktransfers-light-default.png), [full](screenshots/booktransfers-light-full.png) |
| Card programs | `/card-programs/` | [default](screenshots/cardprograms-light-default.png), [full](screenshots/cardprograms-light-full.png) |
| Checks | `/checks/` | [default](screenshots/checks-light-default.png), [full](screenshots/checks-light-full.png) |
| Global banking | `/global-banking/` | [default](screenshots/globalbanking-light-default.png), [full](screenshots/globalbanking-light-full.png) |
| International wires | `/international-wires/` | [default](screenshots/intlwires-light-default.png), [full](screenshots/intlwires-light-full.png) |
| Loan origination | `/loan-origination/` | [default](screenshots/loanorig-light-default.png), [full](screenshots/loanorig-light-full.png) |
| Multicurrency | `/multicurrency/` | [default](screenshots/multicurrency-light-default.png), [full](screenshots/multicurrency-light-full.png) |
| Real-time payments | `/realtime/` | [default](screenshots/realtime-light-default.png), [full](screenshots/realtime-light-full.png) |
| Stablecoins | `/stablecoins/` | [default](screenshots/stablecoins-light-default.png), [full](screenshots/stablecoins-light-full.png) |
| Wire transfers | `/wire/` | [default](screenshots/wire-light-default.png), [full](screenshots/wire-light-full.png) |
| Company | `/company/` | [default](screenshots/company-light-default.png), [full](screenshots/company-light-full.png) |
| Careers | `/careers/` | [default](screenshots/careers-light-default.png), [full](screenshots/careers-light-full.png) |
| Blog | `/blog/` | [default](screenshots/blog-light-default.png), [full](screenshots/blog-light-full.png) |
| Security | `/security/` | [default](screenshots/security-light-default.png), [full](screenshots/security-light-full.png) |
| Contact | `/contact/` | [default](screenshots/contact-light-default.png), [full](screenshots/contact-light-full.png) |
| Privacy | `/legal/privacy-notice/` | [default](screenshots/privacy-light-default.png), [full](screenshots/privacy-light-full.png) |
| Sign-in (boundary) | `dashboard.column.com/login` | [default](screenshots/signin-light-default.png) |
| Home, phone | `/` | [default](screenshots/mobile-home-light-default.png), [full](screenshots/mobile-home-light-full.png), [menu-open](screenshots/mobile-home-light-menu-open.png) |
| ACH, phone | `/ach/` | [default](screenshots/mobile-ach-light-default.png), [full](screenshots/mobile-ach-light-full.png) |
| Card programs, phone | `/card-programs/` | [default](screenshots/mobile-cardprograms-light-default.png), [full](screenshots/mobile-cardprograms-light-full.png) |
| Blog, phone | `/blog/` | [default](screenshots/mobile-blog-light-default.png), [full](screenshots/mobile-blog-light-full.png) |

### Overlays and transient states

| State | Where | How it was reached | Captured |
|---|---|---|---|
| Mobile menu, open | bar, phone | the hamburger's own press | [mobile-home-light-menu-open](screenshots/mobile-home-light-menu-open.png), [m-menu-open](#m-menu-open) |

## Shared values

Values that apply across entries, from the measurement files.

**Focus.** 9 components were given a real keyboard focus. 8 show a visible focus state: `nav-item` (visible change in boxShadow), `nav-ghost` (visible change in boxShadow), `nav-cta` (visible change in boxShadow/backgroundColor), `hero-cta` (visible change in boxShadow), `cards-cta` (visible change in boxShadow), `signin-submit` (shadow change on button::after (child layer)), `footer-link` (1px auto #101010, offset 1px), `m-menu-link` (1px auto #e59700, offset 1px). The other 1 show no change a keyboard user can see: `signin-passkey`.

**Pressed.** Forced with DevTools (`CSS.forcePseudoState` :active:hover). On 6 of 9 measured controls pressed reads as the same painted step as hover; the rest differ — `nav-cta`, `hero-cta`, `cards-cta` (their rows show the diff). Nothing a real press would submit, navigate or write (the CTAs navigate onward, the sign-in OAuth and Log-in controls submit) was ever pressed.

**Motion.** Transitions measured on the components, by duration.

| Duration | Easing | Property | Where |
|---|---|---|---|
| 0.2s | `ease` | background, background-color, border-color, box-shadow, color, filter, opacity, transform | cards-cta, footer-link, hero-cta, nav-cta, promo-banner, signin-field, signin-passkey, signin-submit |
| 0.3s | `ease` | background, box-shadow, transform | header, m-header |
| 0.5s | `ease` | border-radius | dark-band, footer |

**Card shapes.** Default-state values; the entries hold the states.

| Card | Size | Border | Radius | Background | Shadow | Padding |
|---|---|---|---|---|---|---|
| [Section box](#section-box) | 1280 x 443 | - | 16px | rgba(255, 255, 255, 0.6) | rgba(0, 0, 0, 0.04) 0px 0px 0px 1px | 72px 0px |
| [Product screen](#product-screen) | 430 x 530.77 | - | 8px | #ffffff `color.white` | rgba(0, 0, 0, 0.05) 0px 0px 0px 1px, rgba(0, 0, 0, 0.02) 0px 40px 32px 0px, rgba(0, 0, 0, 0.03) 0px 22px 18px 0px, rgba(0, 0, 0, 0.03) 0px 12px 10px 0px, rgba(0, 0, 0, 0.04) 0px 7px 5px 0px, rgba(0, 0, 0, 0.07) 0px 3px 2px 0px | 0 |
| [Sign-in card](#sign-in-card) | 280 x 112 | - | - | transparent | none | 0 |
| [Nav CTA](#nav-cta) | 127 x 36 | - | 8px | rgba(255, 255, 255, 0.5) | rgba(255, 255, 255, 0) 0px 1px 1px 0px, rgba(87, 90, 100, 0.12) 0px 0px 0px 1px | 0px 16px |

## Components

### Shell and navigation

The launch announcement banner and the fixed site nav: the Column mark, the mega-menu nav triggers, the Sign-in link, the "Get started" ghost and the navy Sign-up button.

#### Promo banner
The launch announcement row at the top of the header (Header__LaunchBanner) — real chrome, kept. Read as `promo-banner` on the home page.

**Values (default).** size 1440 x 40; padding 0px 20px; background transparent; image linear-gradient(90deg, #3e5199 0%, #5568ad 100%); text SuisseIntl 14/15.4 500, #ffffff `color.white`; transition filter 0.2s ease; icon 16 x 16, #ffffff `color.white`.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Nav bar
The fixed site header (Header__SiteHeader): Column logo, nav triggers, Sign in, ghost CTAs and the navy Sign up button. Read as `header` on the home page.

**Values (default).** size 1440 x 62; padding 16px 0px; background transparent; text SuisseIntl 14/21 500, #12161e `color.gray.900`; transition transform 0.3s ease, box-shadow 0.3s ease, background 0.3s ease; icon 86.48 x 19, #12161e `color.gray.900`.

Child layers that carry the look: button 127x36 background rgba(255, 255, 255, 0.5) radius 8px shadow rgba(255, 255, 255, 0) 0px 1px 1px 0px, rgba(87, 90, 100, 0.12) 0px 0px 0px 1px; div 400x153.4 background #ffffff `color.white` radius 12px shadow rgba(0, 0, 0, 0.024) 0px 0px 0px 1px, rgba(0, 0, 0, 0.05) 0px 16px 32px 0px, rgba(0, 0, 0, 0.1) 0px 4px 8px 0px; a 188x137.4 border 1px solid transparent radius 8px.

![Nav bar default](components/crops/header-default.png)

#### Logo
The Column logo home anchor in the nav (Header__HeaderLogo). Read as `logo` on the home page.

**Values (default).** size 86.48 x 19; background transparent; text SuisseIntl 16/24 400, #12161e `color.gray.900`; icon 86.48 x 19, #12161e `color.gray.900`.

![Logo default](components/crops/logo-default.png)

#### Nav link
A nav trigger ("Products", Header__NavItemButton); its mega-menu renders eager in the DOM. Read as `nav-item` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 111 x 37; padding 8px 16px; radius 8px; background transparent; text SuisseIntl 14/21 500, #12161e `color.gray.900`; icon 16 x 16, #12161e `color.gray.900` |
| hover | background rgba(0, 0, 0, 0.02); shadow rgba(0, 0, 0, 0.25) 0px 0px 1px 0px; child paint button.Header__NavItemButton-sc-i83ruj-7.eAqYjN: size 111.0x37.0; background rgba(0, 0, 0, 0.02); radius 8px; shadow rgba(0, 0, 0, 0.25) 0px 0px 1px 0px |
| focus-visible | shadow #a2c1ed 0px 0px 0px 2px; child paint button.Header__NavItemButton-sc-i83ruj-7.eAqYjN: size 111.0x37.0; radius 8px; shadow rgb(162, 193, 237) 0px 0px 0px 2px |
| pressed | background rgba(0, 0, 0, 0.02); shadow rgba(0, 0, 0, 0.25) 0px 0px 1px 0px; child paint button.Header__NavItemButton-sc-i83ruj-7.eAqYjN: size 111.0x37.0; background rgba(0, 0, 0, 0.02); radius 8px; shadow rgba(0, 0, 0, 0.25) 0px 0px 1px 0px |

![Nav link default](components/crops/nav-item-default.png) ![Nav link focus-visible](components/crops/nav-item-focus-visible.png) ![Nav link pressed](components/crops/nav-item-pressed.png)

#### Nav sign-in link
The "Sign in" NavItem anchor (Header__NavItem) linking to dashboard.column.com/login; measured never followed. Read as `nav-ghost` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 77 x 38; padding 8px 16px; radius 8px; background transparent; text SuisseIntl 14/21 500, #12161e `color.gray.900` |
| hover | background rgba(0, 0, 0, 0.02); shadow rgba(0, 0, 0, 0.25) 0px 0px 1px 0px; child paint a.Header__NavItem-sc-i83ruj-6.kkIoGS: size 77.0x38.0; background rgba(0, 0, 0, 0.02); radius 8px; shadow rgba(0, 0, 0, 0.25) 0px 0px 1px 0px |
| focus-visible | shadow #a2c1ed 0px 0px 0px 2px; child paint a.Header__NavItem-sc-i83ruj-6.kkIoGS: size 77.0x38.0; radius 8px; shadow rgb(162, 193, 237) 0px 0px 0px 2px |
| pressed | background rgba(0, 0, 0, 0.02); shadow rgba(0, 0, 0, 0.25) 0px 0px 1px 0px; child paint a.Header__NavItem-sc-i83ruj-6.kkIoGS: size 77.0x38.0; background rgba(0, 0, 0, 0.02); radius 8px; shadow rgba(0, 0, 0, 0.25) 0px 0px 1px 0px |

![Nav sign-in link default](components/crops/nav-ghost-default.png) ![Nav sign-in link hover](components/crops/nav-ghost-hover.png) ![Nav sign-in link focus-visible](components/crops/nav-ghost-focus-visible.png) ![Nav sign-in link pressed](components/crops/nav-ghost-pressed.png)

#### Nav CTA
The "Get started" pill (Button__StyledButton / GetStartedMenu__Trigger, white-50% fill + border) — the nav's painted CTA; it opens the GetStartedMenu dropdown whose navy "Sign up" choice renders eager but hidden, so it is not measured at rest. Read as `nav-cta` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 127 x 36; padding 0px 16px; radius 8px; background rgba(255, 255, 255, 0.5); shadow rgba(255, 255, 255, 0) 0px 1px 1px 0px, rgba(87, 90, 100, 0.12) 0px 0px 0px 1px; text SuisseIntl 14/14 500, #232730 `color.gray.800`; transition box-shadow 0.2s ease, background-color 0.2s ease, border-color 0.2s ease; icon 16 x 16, #232730 `color.gray.800` |
| hover | background #ffffff `color.white`; shadow rgba(0, 0, 0, 0.15) 0px 1px 1px 0px, rgba(87, 90, 100, 0.2) 0px 0px 0px 1px; child paint button.Button__StyledButton-sc-fltzk0-1.dQTXBn: background #ffffff `color.white`; shadow rgba(0, 0, 0, 0.15) 0px 1px 1px 0px, rgba(87, 90, 100, 0.2) 0px 0px 0px 1px |
| focus-visible | background #ffffff `color.white`; shadow rgba(0, 0, 0, 0.2) 0px 1px 1px 0px, rgba(87, 90, 100, 0.2) 0px 0px 0px 1px, #f6f6f8 0px 0px 0px 4px; child paint button.Button__StyledButton-sc-fltzk0-1.dQTXBn: background #ffffff `color.white`; shadow rgba(0, 0, 0, 0.2) 0px 1px 1px 0px, rgba(87, 90, 100, 0.2) 0px 0px 0px 1px, rgb(246, 246, 248) 0px 0px 0px 4px |
| pressed | background #ffffff `color.white`; shadow rgba(0, 0, 0, 0.2) 0px 0px 0px 0px, rgba(87, 90, 100, 0.2) 0px 0px 0px 1px; child paint button.Button__StyledButton-sc-fltzk0-1.dQTXBn: background #ffffff `color.white`; shadow rgba(0, 0, 0, 0.2) 0px 0px 0px 0px, rgba(87, 90, 100, 0.2) 0px 0px 0px 1px |

![Nav CTA default](components/crops/nav-cta-default.png) ![Nav CTA hover](components/crops/nav-cta-hover.png) ![Nav CTA focus-visible](components/crops/nav-cta-focus-visible.png) ![Nav CTA pressed](components/crops/nav-cta-pressed.png)

### Home

The hero ("Move, hold, and lend the dollar at scale"), the stat figures, and the near-black navy infrastructure band inside the light page.

#### Hero title
"Move, hold, and lend the dollar at scale" — the hero headline (SuisseIntl 52px, deep navy). Read as `hero-title` on the home page.

**Values (default).** size 486 x 114.38; background transparent; text SuisseIntl 52/57.2 600, #111a4a `color.blue.800`.

![Hero title default](components/crops/hero-title-default.png)

#### Hero CTA
The first button under the hero copy (the "Get started"/contact pair); links onward, never followed. Read as `hero-cta` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 98 x 36; padding 0px 16px; radius 8px; background #111a4a `color.blue.800`; shadow #111a4a 0px 0px 0px 1px, rgba(0, 0, 0, 0.25) 0px 2px 4px 0px, rgba(0, 0, 0, 0.25) 0px 1px 2px 0px; text SuisseIntl 14/14 500, #ffffff `color.white`; transition box-shadow 0.2s ease, background-color 0.2s ease, border-color 0.2s ease; icon 16 x 16, #ffffff `color.white` |
| hover | shadow #111a4a 0px 0px 0px 1px, rgba(0, 0, 0, 0.25) 0px 2px 4px 0px; child paint a.Button__StyledOutboundLink-sc-fltzk0-2.bHvuWn: shadow rgb(17, 26, 74) 0px 0px 0px 1px, rgba(0, 0, 0, 0.25) 0px 2px 4px 0px; el::after: opacity 0.15 |
| focus-visible | shadow #111a4a 0px 0px 0px 1px, rgba(0, 0, 0, 0.15) 0px 1px 3px 0px, #d4e3f7 0px 0px 0px 4px; child paint a.Button__StyledOutboundLink-sc-fltzk0-2.bHvuWn: shadow rgb(17, 26, 74) 0px 0px 0px 1px, rgba(0, 0, 0, 0.15) 0px 1px 3px 0px, rgb(212, 227, 247) 0px 0px 0px 4px |
| pressed | shadow #111a4a 0px 0px 0px 1px, rgba(0, 0, 0, 0.15) 0px 1px 3px 0px, #d4e3f7 0px 0px 0px 0px; child paint a.Button__StyledOutboundLink-sc-fltzk0-2.bHvuWn: shadow rgb(17, 26, 74) 0px 0px 0px 1px, rgba(0, 0, 0, 0.15) 0px 1px 3px 0px, rgb(212, 227, 247) 0px 0px 0px 0px; el::after: opacity 0.05 |

![Hero CTA default](components/crops/hero-cta-default.png) ![Hero CTA hover](components/crops/hero-cta-hover.png) ![Hero CTA focus-visible](components/crops/hero-cta-focus-visible.png) ![Hero CTA pressed](components/crops/hero-cta-pressed.png)

#### Stat tile
A stat tile in the home stats row (_scale__StatsWrapper > Column — "$4.5T+ Annual transaction volume"). Read as `stat-figure` on the home page.

**Values (default).** size 253 x 56.77; background transparent; text SuisseIntl 24/26.4 500, #167e6c `color.seafoam.700`.

![Stat tile default](components/crops/stat-figure-default.png)

#### Dark band
The near-black navy infrastructure section ("The only bank built from the ground up for developers", #011821 ground). Read as `dark-band` on the home page.

**Values (default).** size 1416 x 3242; radius 12px; background #011821 `color.cyan.900`; image radial-gradient(circle, rgba(255, 255, 255, 0.075) 0px, rgba(255, 255, 255, 0.075) 1px, transparent 1px); text SuisseIntlMono 12/18 400, #88deeb `color.cyan.400`; transition border-radius 0.5s ease.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Dark band title
"Flexible building blocks built on USD" — the 48px heading inside the dark infrastructure band (white on #011821). Read as `dark-title` on the home page.

**Values (default).** size 426.66 x 105.59; background transparent; text SuisseIntl 48/52.8 500, #c1e8ef `color.cyan.200`.

![Dark band title default](components/crops/dark-title-default.png)

#### Section title
"Start building today" — the display section heading (SuisseIntl 60px). Read as `section-title` on the home page.

**Values (default).** size 1072 x 60; background transparent; text SuisseIntl 60/60 600, #111a4a `color.blue.800`.

![Section title default](components/crops/section-title-default.png)

#### Page ground
The body element painted fill — the page ground. Read as `page-ground` on the home page.

**Values (default).** size 1440 x 9980.73; background #ffffff `color.white`; text SuisseIntl 14/15.4 500, #ffffff `color.white`; icon 16 x 16, #ffffff `color.white`.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

### ACH page

The /ach product route: its headline, a SectionBox content card and the rendered product-UI mock (ProductScreen).

#### ACH title
"Ultimate control and simplicity" — the ACH product page headline. Read as `ach-title` on the ACH page.

**Values (default).** size 536 x 120; background transparent; text SuisseIntl 56/60 600, #12161e `color.gray.900`.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Section box
A SectionBox content card on the ACH page. Read as `section-box` on the ACH page.

**Values (default).** size 1280 x 443; padding 72px 0px; radius 16px; background rgba(255, 255, 255, 0.6); shadow rgba(0, 0, 0, 0.04) 0px 0px 0px 1px; text SuisseIntl 36/40 600, #12161e `color.gray.900`; icon 24 x 24, #000000 `color.black`.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Product screen
The product-UI mock on the ACH page (ProductScreen__Wrapper — a rendered app frame inside the marketing page). Read as `product-screen` on the ACH page.

**Values (default).** size 430 x 530.77; radius 8px; background transparent; text SuisseIntl 16/24 400, #000000 `color.black`.

Child layers that carry the look: div::before 438.594pxx541.359px image linear-gradient(132deg, #f7d8da `color.red.100` 12%, #7ea7e9 `color.blue.400` 97%), linear radius 0%; div::after 688pxx849.203px background #fbfcfd radius 0%; div 430x530.8 background #ffffff `color.white` radius 8px shadow rgba(0, 0, 0, 0.05) 0px 0px 0px 1px, rgba(0, 0, 0, 0.02) 0px 40px 32px 0px, rgba(0, 0, 0, 0.03) 0px 22px 18px 0px, rgba(0, 0, 0, 0.03) 0px 12px 10px 0px, rgba(0, 0, 0, 0.04) 0px 7px 5px 0px, rgba(0, 0, 0, 0.07) 0px 3px 2px 0px.

![Product screen default](components/crops/product-screen-default.png)

### Card programs page

The /card-programs product route: its headline and first CTA.

#### Cards title
The Card programs product page headline. Read as `cards-title` on the card programs page.

**Values (default).** size 625.33 x 120; background transparent; text SuisseIntl 56/60 600, #12161e `color.gray.900`.

![Cards title default](components/crops/cards-title-default.png)

#### Cards CTA
The first button CTA on the Card programs page; links onward, never followed. Read as `cards-cta` on the card programs page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 139 x 36; padding 0px 16px; radius 8px; background #111a4a `color.blue.800`; shadow #111a4a 0px 0px 0px 1px, rgba(0, 0, 0, 0.25) 0px 2px 4px 0px, rgba(0, 0, 0, 0.25) 0px 1px 2px 0px; text SuisseIntl 14/14 500, #ffffff `color.white`; transition box-shadow 0.2s ease, background-color 0.2s ease, border-color 0.2s ease; icon 16 x 16, #ffffff `color.white` |
| hover | shadow #111a4a 0px 0px 0px 1px, rgba(0, 0, 0, 0.25) 0px 2px 4px 0px; child paint a.Button__StyledOutboundLink-sc-fltzk0-2.bHvuWn: shadow rgb(17, 26, 74) 0px 0px 0px 1px, rgba(0, 0, 0, 0.25) 0px 2px 4px 0px; el::after: opacity 0.149716 |
| focus-visible | shadow #111a4a 0px 0px 0px 1px, rgba(0, 0, 0, 0.15) 0px 1px 3px 0px, #d4e3f7 0px 0px 0px 4px; child paint a.Button__StyledOutboundLink-sc-fltzk0-2.bHvuWn: shadow rgb(17, 26, 74) 0px 0px 0px 1px, rgba(0, 0, 0, 0.15) 0px 1px 3px 0px, rgb(212, 227, 247) 0px 0px 0px 4px |
| pressed | shadow #111a4a 0px 0px 0px 1px, rgba(0, 0, 0, 0.15) 0px 1px 3px 0px, #d4e3f7 0px 0px 0px 0px; child paint a.Button__StyledOutboundLink-sc-fltzk0-2.bHvuWn: shadow rgb(17, 26, 74) 0px 0px 0px 1px, rgba(0, 0, 0, 0.15) 0px 1px 3px 0px, rgb(212, 227, 247) 0px 0px 0px 0px; el::after: opacity 0.0516997 |

![Cards CTA default](components/crops/cards-cta-default.png) ![Cards CTA hover](components/crops/cards-cta-hover.png) ![Cards CTA focus-visible](components/crops/cards-cta-focus-visible.png) ![Cards CTA pressed](components/crops/cards-cta-pressed.png)

### App sign-in (boundary)

dashboard.column.com/login — the product's public login surface, measured at rest; nothing was typed, signed into or submitted.

#### Sign-in card
The dashboard.column.com login form — email field plus the Sign-in and passkey rows. Measured at rest, never submitted. Read as `signin-card` on the sign-in page.

**Values (default).** size 280 x 112; background transparent; text Inter 14/16 400, #575a64 `color.gray.600`; icon 16 x 16, #ffffff `color.white`.

Child layers that carry the look: label 280x40 background rgba(87, 90, 100, 0.04) radius 8px shadow rgba(43, 49, 67, 0.075) 0px 0px 0px 1px inset, transparent 0px 0px 0px 0px, rgba(0, 0, 0, 0.075) 0px 1px 1px 0px inset, rgba(0, 0, 0, 0.024) 0px 2px 4px 0px inset; button::after 280pxx32px background #4575cd `color.blue.500` radius 8px shadow rgba(43, 49, 67, 0.075) 0px 0px 0px 1px inset, rgba(69, 117, 205, 0.15) 0px 0px 0px 0px, rgba(0, 0, 0, 0.25) 0px -1px 0px 0px inset, rgba(0, 0, 0, 0.25) 0px 1px 1px 0px, rgba(0, 0, 0, 0.1) 0px 2px 4px 0px.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Email field
The sign-in email input — a focus reading only; nothing typed, nothing sent. Read as `signin-field` on the sign-in page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 248 x 16; background transparent; wrapper label.sc-2aaa72-0.kRmqPU: shadow rgba(43, 49, 67, 0.075) 0px 0px 0px 1px inset, rgba(0, 0, 0, 0.075) 0px 1px 1px 0px inset, rgba(0, 0, 0, 0.024) 0px 2px 4px 0px inset; text Inter 14/16 400, #575a64 `color.gray.600`; transition opacity 0.2s ease; placeholder #afb0b3 |
| focused | wrapper label.sc-2aaa72-0.hFoKE: shadow rgba(43, 49, 67, 0.075) 0px 0px 0px 1px inset, rgba(0, 0, 0, 0.075) 0px 1px 1px 0px inset, rgba(0, 0, 0, 0.024) 0px 2px 4px 0px inset |

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Sign-in button
The "Sign in"/"Continue" submit on the login form; measured never pressed — it would submit the form. Read as `signin-submit` on the sign-in page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 280 x 32; padding 8px 16px; background transparent; text Inter 14/16 500, #ffffff `color.white`; transition color 0.2s ease, transform 0.2s ease; icon 16 x 16, #ffffff `color.white` |
| focus-visible | child paint button::after.sc-a08sz3-0.dsdCvr: size 280pxx32px; background #4575cd `color.blue.500`; radius 8px; shadow rgba(43, 49, 67, 0.075) 0px 0px 0px 1px inset, rgba(69, 117, 205, 0.15) 0px 0px 0px 3px, rgba(0, 0, 0, 0.25) 0px -1px 0px 0px inset, rgba(0, 0, 0, 0.25) 0px 1px 1px 0px, rgba(0, 0, 0, 0.1) 0px 2px 4px 0px; el::after: shadow rgba(43, 49, 67, 0.075) 0px 0px 0px 1px inset, rgba(69, 117, 205, 0.15) 0px 0px 0px 3px, rgba(0, 0, 0, 0.25) 0px -1px 0px 0px inset, rgba(0, 0, 0, 0.25) 0px 1px 1px 0px, rgba(0, 0, 0, 0.1) 0px 2px 4px 0px |

Child layers that carry the look: button::after 280pxx32px background #4575cd `color.blue.500` radius 8px shadow rgba(43, 49, 67, 0.075) 0px 0px 0px 1px inset, rgba(69, 117, 205, 0.15) 0px 0px 0px 0px, rgba(0, 0, 0, 0.25) 0px -1px 0px 0px inset, rgba(0, 0, 0, 0.25) 0px 1px 1px 0px, rgba(0, 0, 0, 0.1) 0px 2px 4px 0px.

![Sign-in button hover](components/crops/signin-submit-hover.png) ![Sign-in button focus-visible](components/crops/signin-submit-focus-visible.png) ![Sign-in button pressed](components/crops/signin-submit-pressed.png)

#### Passkey button
The "Sign in with a passkey" row on the login form; measured never pressed. Read as `signin-passkey` on the sign-in page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 280 x 32; padding 8px 16px; background transparent; text Inter 14/16 500, #575a64 `color.gray.600`; transition color 0.2s ease, transform 0.2s ease; icon 12 x 12, #575a64 `color.gray.600` |
| focus-visible | child paint button::after.sc-a08sz3-0.bEKcVr: size 278pxx30px; background #ffffff `color.white`; radius 8px; shadow rgba(43, 49, 67, 0.075) 0px 0px 0px 1px, rgba(69, 117, 205, 0.15) 0px 0px 0px 0px, rgba(0, 0, 0, 0.1) 0px 1px 1px 0px, rgba(0, 0, 0, 0.075) 0px 2px 4px 0px |

Child layers that carry the look: button::after 278pxx30px background #ffffff `color.white` radius 8px shadow rgba(43, 49, 67, 0.075) 0px 0px 0px 1px, rgba(69, 117, 205, 0.15) 0px 0px 0px 0px, rgba(0, 0, 0, 0.1) 0px 1px 1px 0px, rgba(0, 0, 0, 0.075) 0px 2px 4px 0px.

![Passkey button default](components/crops/signin-passkey-default.png)

### Footer

The light-grey closer band at the page bottom: link columns, the Column logo block and legal copy.

#### Footer
The closer band at the page bottom (light grey, #eeeff2): link columns, the Column logo and legal copy. Read as `footer` on the home page.

**Values (default).** size 1416 x 1074.38; border 1px solid #e3e4e8 `color.gray.200`; radius 12px; background #eeeff2 `color.gray.100`; text SuisseIntl 60/60 600, #111a4a `color.blue.800`; transition border-radius 0.5s ease.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Footer card link
The closer band’s card link (_closer__CardLink — "Documentation / Get started" tiles, white-25% fill + 1px white ring). Read as `footer-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 344 x 208.98; padding 24px 32px 32px 32px; border 1px solid #ffffff `color.white`; radius 8px; background rgba(255, 255, 255, 0.25); shadow rgba(0, 0, 0, 0.1) 0px 1px 2px 0px; text SuisseIntl 16/17.6 600, #111a4a `color.blue.800`; transition background 0.2s ease |
| focus-visible | outline 1px auto #101010, offset 1px; child paint a._closer__CardLink-sc-jov7sq-4.czbWQZ: outline 1px auto rgb(16, 16, 16) offset 1px |

![Footer card link default](components/crops/footer-link-default.png) ![Footer card link hover](components/crops/footer-link-hover.png) ![Footer card link focus-visible](components/crops/footer-link-focus-visible.png)

#### Footer logo
The Column logo block inside the footer band (_footer__FooterLogoContainer). Read as `footer-logo` on the home page.

**Values (default).** size 125 x 28.63; background transparent; text SuisseIntl 16/0 400, #000000 `color.black`.

Child layers that carry the look: div 125x28.6 image linear-gradient(90deg, transparent 0%, rgba(148, 239, 183, 0.2) 25%, rgba(113, 210, 240, 0.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

### Mobile (390 wide)

The same surface at phone width: the collapsed bar and the open menu overlay.

#### Mobile bar
The 390 mobile nav bar (Header__SiteHeader): logo and the menu toggle, under the launch banner row. Read as `m-header` on the home page at 390 wide.

**Values (default).** size 390 x 45; padding 16px 0px; background transparent; text SuisseIntl 16/24 400, #12161e `color.gray.900`; transition transform 0.3s ease, box-shadow 0.3s ease, background 0.3s ease; icon 72.83 x 16, #12161e `color.gray.900`.

Child layers that carry the look: button 0x0 background rgba(255, 255, 255, 0.5) radius 8px shadow rgba(255, 255, 255, 0) 0px 1px 1px 0px, rgba(87, 90, 100, 0.12) 0px 0px 0px 1px; div 0x0 background #ffffff `color.white` radius 12px shadow rgba(0, 0, 0, 0.024) 0px 0px 0px 1px, rgba(0, 0, 0, 0.05) 0px 16px 32px 0px, rgba(0, 0, 0, 0.1) 0px 4px 8px 0px; a 0x0 border 1px solid transparent radius 8px.

![Mobile bar default](components/crops/m-header-default.png)

#### Menu button
The hamburger (Header__MobileNavToggle, aria-label "Open menu"); its own press opens the menu. Read as `m-menu-button` on the home page at 390 wide.

**Values (default).** size 16 x 18.42; background transparent; text SuisseIntl 12/18 500, #12161e `color.gray.900`; icon 16 x 16, #12161e `color.gray.900`.

![Menu button default](components/crops/m-menu-button-default.png)

#### Mobile menu, open
The menu overlay after the hamburger press. Read as `m-menu-open` on the home page at 390 wide.

**Values (default).** size 390 x 799; padding 4px 4px 0px 4px; background transparent; text SuisseIntl 14/20 500, #12161e `color.gray.900`; icon 16 x 16, #12161e `color.gray.900`.

Child layers that carry the look: div 382x759 background #ffffff `color.white` radius 12px shadow rgba(0, 0, 0, 0.024) 0px 0px 0px 1px, rgba(0, 0, 0, 0.05) 0px 16px 32px 0px, rgba(0, 0, 0, 0.1) 0px 4px 8px 0px; hr 342x1 border 1px solid #eeeff2 `color.gray.100`; hr 342x1 border 1px solid #eeeff2 `color.gray.100`.

![Mobile menu, open default](components/crops/m-menu-open-default.png)

#### Menu link
A link/accordion row inside the open mobile menu. Read as `m-menu-link` on the home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 342 x 42; padding 10px 0px; background transparent; wrapper div.MobileMenu__Panel-sc-1ksm2t0-0.hwMZyc: shadow rgba(0, 0, 0, 0.024) 0px 0px 0px 1px, rgba(0, 0, 0, 0.05) 0px 16px 32px 0px, rgba(0, 0, 0, 0.1) 0px 4px 8px 0px; text SuisseIntl 16/22 500, #12161e `color.gray.900`; icon 16 x 16, #12161e `color.gray.900` |
| focus-visible | outline 1px auto #e59700, offset 1px; child paint a.MobileMenu__Row-sc-1ksm2t0-4.jAtTwx: size 342.0x42.0; outline 1px auto rgb(229, 151, 0) offset 1px |

![Menu link default](components/crops/m-menu-link-default.png) ![Menu link hover](components/crops/m-menu-link-hover.png) ![Menu link focus-visible](components/crops/m-menu-link-focus-visible.png) ![Menu link pressed](components/crops/m-menu-link-pressed.png)

#### Mobile headline
The hero headline at 390. Read as `m-hero` on the home page at 390 wide.

**Values (default).** size 360 x 70.38; background transparent; text SuisseIntl 32/35.2 600, #111a4a `color.blue.800`.

![Mobile headline default](components/crops/m-hero-default.png)

## Icons

No standalone SVG icon set was lifted on this pass; the icons in the crops and screenshots are Column's artwork. Declared under layoutGaps in the catalog entry.

| Icon | Rendered sizes | View box | Style | Seen on | Next to |
|---|---|---|---|---|---|

## Gaps

### Pages

- **The product itself.** Column's platform — the dashboard, ledgers, transfers and account controls — lives behind dashboard.column.com sign-in; the public login surface was measured but never submitted, and no authenticated flow was ever entered.
- **The app itself is a different surface.** The marketing site is a Gatsby + styled-components build; the dashboard UI behind dashboard.column.com login is not reachable signed out and is not claimed here. docs.column.com (the API docs surface) was not captured.

### States

- **Pressed** was forced with DevTools on every control, so a state a script adds on mousedown (if any) is missing.
- **Disabled, error and loading states** were not seen on the public surface.

### Themes

One theme: the whole public surface paints light. Dark islands exist inside it (the near-black navy infrastructure band, which carries the `.color-palette-inverted` class), but no second theme is offered.

### Fonts

- **The UI fonts** are webfonts the site ships (SuisseIntl body, SuisseIntlMono code and Inter UI via the --font-* stacks; `fonts` in [raw/css-vars.json](raw/css-vars.json) holds the @font-face records); the font files themselves are not committed.
- Illustrations, photography, the product-UI mocks and the wordmark in the screenshots are Column's property; partner and certification marks are their owners' marks.

### Screenshots

- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files.

### Content left out

- The hero artwork, illustrations and the Column wordmark are Column's content; only the frames and components were measured. The product-UI mocks render the app's look inside marketing frames.
