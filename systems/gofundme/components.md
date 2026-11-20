# GoFundMe components

The discovery list of every page and view captured, then one entry per component with crops of the real product, and the Gaps. Captured from gofundme.com on 2026-11-16, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running page. Nothing was signed into, donated or submitted; the wizard's postcode field was typed into then cleared and never sent; 'Donate now', 'Share', 'Continue' and every CTA was measured, never followed.

The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) (63 components, 153 states). The page layouts are described in [patterns.md](patterns.md).

How to read an entry:

- A colour is its value followed by the palette token in [tokens.json](tokens.json) with the same value, when there is one. Text is written family size/line-height weight, then its colour, for example `Inter 16/19.2 500, #ffffff`, and is read from the first text node inside the component.
- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example "default (same: focus-visible)". When the root paints nothing, "Child layers" names the first nodes inside it that do.
- Crops are images of the component read from the live page, in [components/crops/](components/crops) (147 files, named `{component}-{state}.png`, at 2x). Screenshots are in [screenshots/](screenshots).

## Discovery list

Screenshots are named `{page}-{theme}-state.png` where `{theme}` is the mode the page painted at capture: `light` for every page — the consumer site paints the :root-declared `--hrt-*` consumer theme and ships no theme switcher; the /c/* content stack paints light too. Desktop shots are 1440 x 900 at 1x; `-full` shots are whole pages bounded at eight chunks; mobile shots are `mobile-{page}-{theme}-{state}.png`, 780 wide (390 at 2x).

| Surface | URL | Screenshots |
|---|---|---|
| Home | `/` | [default](screenshots/home-light-default.png), [full](screenshots/home-light-full.png), [menu-about](screenshots/home-light-menu-about.png), [menu-donate](screenshots/home-light-menu-donate.png), [menu-fundraise](screenshots/home-light-menu-fundraise.png) |
| Discover | `/discover` | [default](screenshots/discover-light-default.png), [full](screenshots/discover-light-full.png) |
| Search results | `/s?q=medical` | [default](screenshots/search-light-default.png), [full](screenshots/search-light-full.png) |
| Fundraiser page | `/f/<slug>` | [default](screenshots/fundraiser-light-default.png), [full](screenshots/fundraiser-light-full.png) |
| How it works | `/c/how-it-works` | [default](screenshots/how-it-works-light-default.png), [full](screenshots/how-it-works-light-full.png) |
| Pricing and fees | `/c/pricing` | [default](screenshots/pricing-light-default.png), [full](screenshots/pricing-light-full.png) |
| Why GoFundMe | `/c/why-gofundme` | [default](screenshots/why-gofundme-light-default.png), [full](screenshots/why-gofundme-light-full.png) |
| Crowdfunding | `/c/crowdfunding` | [default](screenshots/crowdfunding-light-default.png), [full](screenshots/crowdfunding-light-full.png) |
| Fundraising ideas | `/c/fundraising-ideas` | [default](screenshots/fundraising-ideas-light-default.png), [full](screenshots/fundraising-ideas-light-full.png) |
| Charity fundraising | `/c/charity-fundraising` | [default](screenshots/charity-fundraising-light-default.png), [full](screenshots/charity-fundraising-light-full.png) |
| Start a fundraiser (content) | `/c/start` | [default](screenshots/start-light-default.png), [full](screenshots/start-light-full.png) |
| About us | `/c/about-us` | [default](screenshots/about-light-default.png), [full](screenshots/about-light-full.png) |
| Careers | `/c/careers` | [default](screenshots/careers-light-default.png), [full](screenshots/careers-light-full.png) |
| Blog | `/c/blog` | [default](screenshots/blog-light-default.png), [full](screenshots/blog-light-full.png) |
| Trust and safety | `/c/safety` | [default](screenshots/safety-light-default.png), [full](screenshots/safety-light-full.png) |
| Sign in (auth shell) | `/sign-in` | [default](screenshots/sign-in-light-default.png), [full](screenshots/sign-in-light-full.png) |
| Start a fundraiser (wizard) | `/create/fundraiser/category` | [default](screenshots/create-light-default.png), [full](screenshots/create-light-full.png) |
| Home, phone | `/` | [default](screenshots/mobile-home-light-default.png), [drawer](screenshots/mobile-home-light-drawer.png), [full](screenshots/mobile-home-light-full.png) |
| Discover, phone | `/discover` | [default](screenshots/mobile-discover-light-default.png), [full](screenshots/mobile-discover-light-full.png) |
| Fundraiser page, phone | `/f/<slug>` | [default](screenshots/mobile-fundraiser-light-default.png), [full](screenshots/mobile-fundraiser-light-full.png) |
| Sign in, phone | `/sign-in` | [default](screenshots/mobile-sign-in-light-default.png), [full](screenshots/mobile-sign-in-light-full.png) |

### Overlays and transient states

| State | Where | How it was reached | Captured |
|---|---|---|---|
| Cookie consent | every page | the Transcend 'Privacy Information' banner is hidden before every shot and reading — 'Okay' was never clicked | hidden, never answered |
| Donate dropdown | every consumer page header | hovered the 'Donate' trigger — the dropdown opens on pointer hover (closed panels stay mounted hidden); its links were never followed | [home-light-menu-donate](screenshots/home-light-menu-donate.png), [nav-panel](#header-dropdown-panel) |
| Fundraise / About dropdowns | every consumer page header | the same hover on 'Fundraise' and 'About' | [home-light-menu-fundraise](screenshots/home-light-menu-fundraise.png), [home-light-menu-about](screenshots/home-light-menu-about.png) |
| Mobile nav overlay | home page, phone width | the header nav toggle's own activation | [mobile-home-light-drawer](screenshots/mobile-home-light-drawer.png), [m-drawer](#mobile-nav-overlay) |
| Wizard field | /create/fundraiser/category | typed into then cleared — nothing sent | [create-zip](#postcode-field) |
| Donation actions | a fundraiser page | 'Donate now', 'Share' and 'Message' were measured in every state, never pressed — no donation was started | [f-donate](#donate-button) |
| Signed-in product | a GoFundMe account | the dashboard and every post-login surface needs an account; the donation checkout needs a payment | boundary; see Gaps |

## Shared values

Values that apply across entries, from the measurement files.

**Focus.** 27 components were given a real keyboard focus. 26 draw an outline ring: `nav-search` (1px auto #101010 `light.measured.color.border.focusRing`, offset 1px), `nav-donate-dd` (1px auto #101010 `light.measured.color.border.focusRing`, offset 0px), `nav-about-dd` (1px auto #101010 `light.measured.color.border.focusRing`, offset 0px), `nav-signin` (1px auto #101010 `light.measured.color.border.focusRing`, offset 1px), `nav-start` (1px auto #101010 `light.measured.color.border.focusRing`, offset 1px), `hero-cta` (1px auto #101010 `light.measured.color.border.focusRing`, offset 1px), `collection-btn` (1px auto #101010 `light.measured.color.border.focusRing`, offset 0px), `pause-motion-btn` (1px auto #101010 `light.measured.color.border.focusRing`, offset 0px), `carousel-btn` (1px auto #101010 `light.measured.color.border.focusRing`, offset 0px), `footer-link` (1px auto #101010 `light.measured.color.border.focusRing`, offset 1px), `footer-more` (1px auto #101010 `light.measured.color.border.focusRing`, offset 0px), `locale-btn` (1px auto #101010 `light.measured.color.border.focusRing`, offset 0px), `disc-cat-btn` (1px auto #101010 `light.measured.color.border.focusRing`, offset 0px), `f-donate` (1px auto #101010 `light.measured.color.border.focusRing`, offset 1px), `f-share` (1px auto #101010 `light.measured.color.border.focusRing`, offset 0px), `f-message` (1px auto #101010 `light.measured.color.border.focusRing`, offset 0px), `f-readmore` (1px auto #101010 `light.measured.color.border.focusRing`, offset 0px), `f-media-nav` (1px auto #101010 `light.measured.color.border.focusRing`, offset 0px), `f-report` (1px auto #101010 `light.measured.color.border.focusRing`, offset 1px), `f-collection` (1px auto #101010 `light.measured.color.border.focusRing`, offset 0px), `price-toggle` (on a child: 1px auto rgb(16, 16, 16) offset 2px), `wp-locale` (1px auto #101010 `light.measured.color.border.focusRing`, offset 0px), `create-pill` (on a child: 1px auto rgb(16, 16, 16) offset 2px), `m-menu-btn` (1px auto #e59700, offset 0px), `m-hero-cta` (1px auto #e59700, offset 1px), `wp-button` (1px auto #101010 `light.measured.color.border.focusRing`, offset 1px). The other 1 show no measured change: `create-country`.

**Pressed.** Forced with DevTools (`CSS.forcePseudoState` :active:hover). Nothing a real press would submit was ever pressed.

**Motion.** Transitions measured on the components, by duration.

| Duration | Easing | Property | Where |
|---|---|---|---|
| 0.15s | `ease-in-out` | opacity, visibility | nav-panel |
| 0.15s | `linear` | top | nav-panel |
| 0.2s | `cubic-bezier(0.3, 0.01, 0, 1)` | background-color, box-shadow | m-header, mkt-header |
| 0.25s | `ease-in-out` | border-color | wp-locale |
| 0.5s | `cubic-bezier(0.3, 0.01, 0, 1)` | background-color, border-color, box-shadow, color, opacity, transform | carousel-btn, collection-btn, cookie-btn, create-continue, disc-cat-btn, f-collection, f-donate, f-media-nav and more |

**Card shapes.** Default-state values; the entries hold the states.

| Card | Size | Border | Radius | Background | Shadow | Padding |
|---|---|---|---|---|---|---|
| [Header dropdown panel](#header-dropdown-panel) | 632 x 236 | - | 8px | #ffffff `light.color.surface.default.default` | rgba(35, 35, 35, 0.1) 0px 6px 14px 0px | 16px |
| [Fundraiser card](#fundraiser-card) | 354.66 x 339.78 | - | 12px | #ffffff `light.color.surface.default.default` | none | 8px |
| [Featured merch card](#featured-merch-card) | 1104 x 311 | - | 16px | #fafafa `light.color.surface.default.hover` | none | 0 |
| [Sign-in card](#sign-in-card) | 1440 x 900 | - | - | #ffffff `light.color.surface.default.default` | none | 0 |
| [Mobile nav overlay](#mobile-nav-overlay) | 390 x 844 | - | - | transparent | none | 0 |

## Components

### Site chrome

The chrome on every consumer page: the 'Kind 50' promo banner (hrt-global-promo-banner), the white sticky header with the GoFundMe mark, Search and the Donate/Fundraise/About dropdown triggers (a button whose panel opens on hover), 'Sign in' and the pill 'Start a GoFundMe'; the dropdown panel opens under the trigger.

#### Global promo banner
The dismissal strip above the header ("Introducing the Kind 50…"); its close icon-button was never pressed. Read as `mkt-promo` on the home page.

**Values (default).** size 1440 x 64; padding 16px 40px; background #ccf88e `light.color.button.primary.surface.strong.default`; text GoFundMe Sans 16/24 100, #274a34 `light.color.button.primary.surface.default`; icon 24 x 24, #232323 `light.color.text.default`.

![Global promo banner default](components/crops/mkt-promo-default.png)

#### Site header
The sticky bar on every consumer page: the GoFundMe mark, Donate/Fundraise/About dropdown triggers, Search, "Sign in" and "Start a GoFundMe". Read as `mkt-header` on the home page.

**Values (default).** size 1440 x 80; padding 16px 0px; background transparent; text GoFundMe Sans 16/19.2 100, #232323 `light.color.text.default`; transition box-shadow 0.2s cubic-bezier(0.3, 0.01, 0, 1), background-color 0.2s cubic-bezier(0.3, 0.01, 0, 1); layers a.hrt-header-skip.hrt-show-on-focus 16.0x34.0 rgb(255, 255, 255) 9999px; div.hrt-header-dropdown-caret 8.0x5.0 T:5px rgb(35, 35, 35) / R:4px rgba(0, 0, 0, 0) / L:4px rgba(0, 0, 0, 0); div.hrt-header-dropdown-content.hrt-header-dropdown-content--left 632.0x236.0 rgb(255, 255, 255) rgba(35, 35, 35, 0.1) 0px 6px 14px 0px 8px; div.hrt-spot-icon.hrt-spot-icon--neutral-subtle 40.0x40.0 rgb(245, 245, 245.

Child layers that carry the look: a 16x34 background #ffffff `light.color.surface.default.default` radius 9999px; div 8x5 border 5px #232323 `light.color.text.default`; div 632x236 background #ffffff `light.color.surface.default.default` radius 8px shadow rgba(35, 35, 35, 0.1) 0px 6px 14px 0px.

![Site header default](components/crops/mkt-header-default.png)

#### Logo
The GoFundMe mark in the header, linking home. Read as `mkt-logo` on the home page.

**Values (default).** size 105 x 36; background transparent; text GoFundMe Sans 16/24 100, #232323 `light.color.text.default`; icon 105 x 36, #232323 `light.color.text.default`.

![Logo default](components/crops/mkt-logo-default.png)

#### Nav search button
The "Search" header button (search-field styling) to /s; measured, never followed. Read as `nav-search` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 91 x 34; padding 2px 8px; radius 9999px; background transparent; text GoFundMe Sans 16/19.2 100, #232323 `light.color.text.default`; transition background-color 0.5s cubic-bezier(0.3, 0.01, 0, 1), box-shadow 0.5s cubic-bezier(0.3, 0.01, 0, 1), color 0.5s cubic-bezier(0.3, 0.01, 0, 1), opacity 0.5s cubic-bezier(0.3, 0.01, 0, 1), transform 0.5s cubic-bezier(0.3, 0.01, 0, 1); icon 16 x 16, #232323 `light.color.text.default` |
| hover | background rgba(35, 35, 35, 0.05) `light.measured.color.action.ctaHover` |
| focus-visible | outline 1px auto #101010 `light.measured.color.border.focusRing`, offset 1px; layers a.default-header_search-button.hrt-hide-max-md 91.0x34.0 1px auto rgb(16, 16, 16) offset 1px 9999px |
| pressed | background rgba(35, 35, 35, 0.1) |

![Nav search button default](components/crops/nav-search-default.png) ![Nav search button hover](components/crops/nav-search-hover.png) ![Nav search button focus-visible](components/crops/nav-search-focus-visible.png) ![Nav search button pressed](components/crops/nav-search-pressed.png)

#### Nav dropdown trigger
The "Donate" header item whose dropdown opens on hover (panel measured next; links never followed). Read as `nav-donate-dd` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 87 x 34; padding 2px 8px; radius 9999px; background transparent; text GoFundMe Sans 16/19.2 100, #232323 `light.color.text.default`; transition background-color 0.5s cubic-bezier(0.3, 0.01, 0, 1), box-shadow 0.5s cubic-bezier(0.3, 0.01, 0, 1), color 0.5s cubic-bezier(0.3, 0.01, 0, 1), opacity 0.5s cubic-bezier(0.3, 0.01, 0, 1), transform 0.5s cubic-bezier(0.3, 0.01, 0, 1); layers div.hrt-header-dropdown-caret 8.0x5.0 T:5px rgb(35, 35, 35) / R:4px rgba(0, 0, 0, 0) / L:4px rgba(0, 0, 0, 0) |
| hover | background rgba(35, 35, 35, 0.05) `light.measured.color.action.ctaHover`; layers none |
| focus-visible | outline 1px auto #101010 `light.measured.color.border.focusRing`, offset 0px; layers button.hrt-ml-1.hrt-header-dropdown-button 87.0x34.0 1px auto rgb(16, 16, 16) offset 0px 9999px; div.hrt-header-dropdown-caret 8.0x5.0 T:5px rgb(35, 35, 35) / R:4px rgba(0, 0, 0, 0) / L:4px rgba(0, 0, 0, 0) |
| pressed | background rgba(35, 35, 35, 0.1); layers none |

Child layers that carry the look: div 8x5 border 5px #232323 `light.color.text.default`.

![Nav dropdown trigger default](components/crops/nav-donate-dd-default.png) ![Nav dropdown trigger hover](components/crops/nav-donate-dd-hover.png) ![Nav dropdown trigger focus-visible](components/crops/nav-donate-dd-focus-visible.png) ![Nav dropdown trigger pressed](components/crops/nav-donate-dd-pressed.png)

#### Header dropdown panel
The mega-dropdown panel under "Donate" (multi-column link groups); opened by hovering the trigger, its links never followed. Read as `nav-panel` on the home page.

**Values (default).** size 632 x 236; padding 16px; radius 8px; background #ffffff `light.color.surface.default.default`; shadow rgba(35, 35, 35, 0.1) 0px 6px 14px 0px; text GoFundMe Sans 20/22 100, #232323 `light.color.text.default`; transition opacity 0.15s ease-in-out, top 0.15s linear, visibility 0.15s ease-in-out; icon 24 x 24, #424242 `light.color.text.neutral.strong`; layers ::before rgba(0, 0, 0, 0) 0px none 1; ::after rgba(0, 0, 0, 0) 0px none 1.

![Header dropdown panel default](components/crops/nav-panel-default.png)

#### About dropdown trigger
The "About" header item — the right-aligned dropdown trigger; its panel was never opened beyond the one menu reading. Read as `nav-about-dd` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 75 x 34; padding 2px 8px; radius 9999px; background transparent; text GoFundMe Sans 16/19.2 100, #232323 `light.color.text.default`; transition background-color 0.5s cubic-bezier(0.3, 0.01, 0, 1), box-shadow 0.5s cubic-bezier(0.3, 0.01, 0, 1), color 0.5s cubic-bezier(0.3, 0.01, 0, 1), opacity 0.5s cubic-bezier(0.3, 0.01, 0, 1), transform 0.5s cubic-bezier(0.3, 0.01, 0, 1); layers div.hrt-header-dropdown-caret 8.0x5.0 T:5px rgb(35, 35, 35) / R:4px rgba(0, 0, 0, 0) / L:4px rgba(0, 0, 0, 0) |
| hover | background rgba(35, 35, 35, 0.05) `light.measured.color.action.ctaHover`; layers none |
| focus-visible | outline 1px auto #101010 `light.measured.color.border.focusRing`, offset 0px; layers button.hrt-header-dropdown-button.hrt-button 75.0x34.0 1px auto rgb(16, 16, 16) offset 0px 9999px; div.hrt-header-dropdown-caret 8.0x5.0 T:5px rgb(35, 35, 35) / R:4px rgba(0, 0, 0, 0) / L:4px rgba(0, 0, 0, 0) |
| pressed | background rgba(35, 35, 35, 0.1); layers none |

Child layers that carry the look: div 8x5 border 5px #232323 `light.color.text.default`.

![About dropdown trigger default](components/crops/nav-about-dd-default.png) ![About dropdown trigger hover](components/crops/nav-about-dd-hover.png) ![About dropdown trigger focus-visible](components/crops/nav-about-dd-focus-visible.png) ![About dropdown trigger pressed](components/crops/nav-about-dd-pressed.png)

#### Sign in link
The "Sign in" header link (tertiary button styling) to /sign-in; measured, never followed. Read as `nav-signin` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 64 x 34; padding 2px 8px; radius 9999px; background transparent; text GoFundMe Sans 16/19.2 100, #232323 `light.color.text.default`; transition background-color 0.5s cubic-bezier(0.3, 0.01, 0, 1), box-shadow 0.5s cubic-bezier(0.3, 0.01, 0, 1), color 0.5s cubic-bezier(0.3, 0.01, 0, 1), opacity 0.5s cubic-bezier(0.3, 0.01, 0, 1), transform 0.5s cubic-bezier(0.3, 0.01, 0, 1) |
| hover | background rgba(35, 35, 35, 0.05) `light.measured.color.action.ctaHover` |
| focus-visible | outline 1px auto #101010 `light.measured.color.border.focusRing`, offset 1px; layers a.hrt-ml-1.hrt-button 64.0x34.0 1px auto rgb(16, 16, 16) offset 1px 9999px |
| pressed | background rgba(35, 35, 35, 0.1) |

![Sign in link default](components/crops/nav-signin-default.png) ![Sign in link hover](components/crops/nav-signin-hover.png) ![Sign in link focus-visible](components/crops/nav-signin-focus-visible.png) ![Sign in link pressed](components/crops/nav-signin-pressed.png)

#### Header CTA
The pill "Start a GoFundMe" header button (secondary hierarchy); links to the wizard, measured never followed. Read as `nav-start` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 161 x 32; padding 4px 16px; radius 9999px; background rgba(255, 255, 255, 0) `light.measured.color.action.ctaFill`; shadow #b7b7b6 0px 0px 0px 1px inset; text GoFundMe Sans 14/20 175, #232323 `light.color.text.default`; transition background-color 0.5s cubic-bezier(0.3, 0.01, 0, 1), box-shadow 0.5s cubic-bezier(0.3, 0.01, 0, 1), color 0.5s cubic-bezier(0.3, 0.01, 0, 1), opacity 0.5s cubic-bezier(0.3, 0.01, 0, 1), transform 0.5s cubic-bezier(0.3, 0.01, 0, 1) |
| hover | background rgba(35, 35, 35, 0.05) `light.measured.color.action.ctaHover`; shadow #585858 0px 0px 0px 1px inset |
| focus-visible | outline 1px auto #101010 `light.measured.color.border.focusRing`, offset 1px |
| pressed | background rgba(35, 35, 35, 0.1); shadow #595959 0px 0px 0px 1px inset |

![Header CTA default](components/crops/nav-start-default.png) ![Header CTA hover](components/crops/nav-start-hover.png) ![Header CTA focus-visible](components/crops/nav-start-focus-visible.png) ![Header CTA pressed](components/crops/nav-start-pressed.png)

### Home

The home hero: the 'Where successful fundraisers start' masthead over the primary 'Start a GoFundMe' button, the collection selector pills, the fundraiser rails with media tags and carousel arrows, and the pause-motion control.

#### Hero headline
"Where successful fundraisers start" — the home hero display heading. Read as `hero-h1` on the home page.

**Values (default).** size 770 x 180.38; background transparent; text GoFundMe Sans 82/90.2 175, #232323 `light.color.text.default`.

![Hero headline default](components/crops/hero-h1-default.png)

#### Hero CTA
The primary "Start a GoFundMe" button in the hero; links to the wizard, measured never followed. Read as `hero-cta` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 190 x 56; padding 2px 24px; radius 9999px; background #274a34 `light.color.button.primary.surface.default`; text GoFundMe Sans 16/20 175, #ccf88e `light.color.button.primary.surface.strong.default`; transition background-color 0.5s cubic-bezier(0.3, 0.01, 0, 1), box-shadow 0.5s cubic-bezier(0.3, 0.01, 0, 1), color 0.5s cubic-bezier(0.3, 0.01, 0, 1), opacity 0.5s cubic-bezier(0.3, 0.01, 0, 1), transform 0.5s cubic-bezier(0.3, 0.01, 0, 1) |
| hover | background #2d6339 `light.color.button.primary.surface.hover` |
| focus-visible | outline 1px auto #101010 `light.measured.color.border.focusRing`, offset 1px |
| pressed | background #2d6339 `light.color.button.primary.surface.hover`; shadow rgba(53, 125, 58, 0.25) 0px 0px 0px 1440px inset |

![Hero CTA default](components/crops/hero-cta-default.png) ![Hero CTA hover](components/crops/hero-cta-hover.png) ![Hero CTA focus-visible](components/crops/hero-cta-focus-visible.png) ![Hero CTA pressed](components/crops/hero-cta-pressed.png)

#### Section heading
A marketing section heading further down the home page. Read as `section-h2` on the home page.

**Values (default).** size 880 x 140.78; background transparent; text GoFundMe Sans 64/70.4 175, #232323 `light.color.text.default`.

![Section heading default](components/crops/section-h2-default.png)

#### Collection selector
A "Happening worldwide"-style collection filter pill; measured at rest, never toggled (toggling would re-filter the rail). Read as `collection-btn` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 247 x 40; padding 2px 24px; radius 24px; background rgba(255, 255, 255, 0) `light.measured.color.action.ctaFill`; shadow #b7b7b6 0px 0px 0px 1px inset; text GoFundMe Sans 16/20 175, #232323 `light.color.text.default`; transition background-color 0.5s cubic-bezier(0.3, 0.01, 0, 1), box-shadow 0.5s cubic-bezier(0.3, 0.01, 0, 1), color 0.5s cubic-bezier(0.3, 0.01, 0, 1), opacity 0.5s cubic-bezier(0.3, 0.01, 0, 1), transform 0.5s cubic-bezier(0.3, 0.01, 0, 1); icon 16 x 16, #232323 `light.color.text.default` |
| hover | background rgba(35, 35, 35, 0.05) `light.measured.color.action.ctaHover`; shadow #585858 0px 0px 0px 1px inset |
| focus-visible | outline 1px auto #101010 `light.measured.color.border.focusRing`, offset 0px |
| pressed | background rgba(35, 35, 35, 0.1); shadow #595959 0px 0px 0px 1px inset |

![Collection selector hover](components/crops/collection-btn-hover.png) ![Collection selector focus-visible](components/crops/collection-btn-focus-visible.png) ![Collection selector pressed](components/crops/collection-btn-pressed.png)

#### Media tag
A location tag chip overlaid on a fundraiser card image ("Blaine, Minnesota" and neighbours). Read as `card-media-tag` on the home page.

**Values (default).** size 207 x 24; padding 0px 8px; border 1px solid transparent; radius 4px; background #ccf88e `light.color.button.primary.surface.strong.default`; text GoFundMe Sans 14/14 175, #274a34 `light.color.button.primary.surface.default`.

![Media tag default](components/crops/card-media-tag-default.png)

#### Pause-motion icon button
The reduced-motion control on the how-it-works steps; an icon-only button, measured never pressed. Read as `pause-motion-btn` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 32 x 32; radius 9999px; background rgba(255, 255, 255, 0.8) `light.color.surface.hover.on.strong`; shadow rgba(35, 35, 35, 0.1) 0px 1px 2px 0px; text GoFundMe Sans 16/24 100, #232323 `light.color.text.default`; transition background-color 0.5s cubic-bezier(0.3, 0.01, 0, 1), box-shadow 0.5s cubic-bezier(0.3, 0.01, 0, 1), color 0.5s cubic-bezier(0.3, 0.01, 0, 1), opacity 0.5s cubic-bezier(0.3, 0.01, 0, 1), transform 0.5s cubic-bezier(0.3, 0.01, 0, 1); icon 16 x 16, #232323 `light.color.text.default` |
| hover | background rgba(255, 255, 255, 0.7) `light.color.surface.on.media.hover`; shadow rgba(35, 35, 35, 0.1) 0px 1.99646px 5.98582px 0px |
| focus-visible | outline 1px auto #101010 `light.measured.color.border.focusRing`, offset 0px |
| pressed | shadow rgba(35, 35, 35, 0.1) 0px 1.97868px 5.91473px 0px |

![Pause-motion icon button default](components/crops/pause-motion-btn-default.png) ![Pause-motion icon button hover](components/crops/pause-motion-btn-hover.png) ![Pause-motion icon button focus-visible](components/crops/pause-motion-btn-focus-visible.png) ![Pause-motion icon button pressed](components/crops/pause-motion-btn-pressed.png)

#### Carousel arrow
A forward arrow icon-button on a fundraiser rail; measured never pressed (it would scroll the rail). Read as `carousel-btn` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 32 x 32; border 1px solid #b7b7b6 `light.color.surface.neutral.subtle.pressed`; radius 9999px; background rgba(255, 255, 255, 0) `light.measured.color.action.ctaFill`; text GoFundMe Sans 16/24 100, #232323 `light.color.text.default`; transition background-color 0.5s cubic-bezier(0.3, 0.01, 0, 1), box-shadow 0.5s cubic-bezier(0.3, 0.01, 0, 1), color 0.5s cubic-bezier(0.3, 0.01, 0, 1), opacity 0.5s cubic-bezier(0.3, 0.01, 0, 1), transform 0.5s cubic-bezier(0.3, 0.01, 0, 1); icon 16 x 16, #232323 `light.color.text.default` |
| hover | background rgba(35, 35, 35, 0.05) `light.measured.color.action.ctaHover` |
| focus-visible | outline 1px auto #101010 `light.measured.color.border.focusRing`, offset 0px |
| pressed | background rgba(35, 35, 35, 0.1) |

![Carousel arrow default](components/crops/carousel-btn-default.png) ![Carousel arrow hover](components/crops/carousel-btn-hover.png) ![Carousel arrow focus-visible](components/crops/carousel-btn-focus-visible.png) ![Carousel arrow pressed](components/crops/carousel-btn-pressed.png)

#### Featured merch card
A featured-topic merch card link (large image card); measured at rest and on hover, never followed. Read as `merch-card` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 1104 x 311; radius 16px; background #fafafa `light.color.surface.default.hover`; text GoFundMe Sans 14/14 175, #642878 `light.color.surface.accent.purple.strong.on.medium`; transition background-color 0.5s cubic-bezier(0.3, 0.01, 0, 1), box-shadow 0.5s cubic-bezier(0.3, 0.01, 0, 1), color 0.5s cubic-bezier(0.3, 0.01, 0, 1), opacity 0.5s cubic-bezier(0.3, 0.01, 0, 1), transform 0.5s cubic-bezier(0.3, 0.01, 0, 1); icon 12 x 12, #232323 `light.color.text.default` |

![Featured merch card default](components/crops/merch-card-default.png) ![Featured merch card hover](components/crops/merch-card-hover.png)

### Discover

/discover — the public browse grid: fundraiser cards (image, location tag, title, raised line, hrt-goal-bar) under the category chips and the 'Show more categories' expander.

#### Discover headline
The /discover masthead ("Fundraisers" and the result count). Read as `disc-h1` on the discover page.

**Values (default).** size 714.66 x 180.38; background transparent; text GoFundMe Sans 82/90.2 175, #232323 `light.color.text.default`.

![Discover headline default](components/crops/disc-h1-default.png)

#### Category expander
The "Show more categories" button under the category chips; measured at rest, never toggled. Read as `disc-cat-btn` on the discover page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 225 x 48; padding 2px 24px; radius 9999px; background rgba(255, 255, 255, 0) `light.measured.color.action.ctaFill`; shadow #b7b7b6 0px 0px 0px 1px inset; text GoFundMe Sans 16/20 175, #232323 `light.color.text.default`; transition background-color 0.5s cubic-bezier(0.3, 0.01, 0, 1), box-shadow 0.5s cubic-bezier(0.3, 0.01, 0, 1), color 0.5s cubic-bezier(0.3, 0.01, 0, 1), opacity 0.5s cubic-bezier(0.3, 0.01, 0, 1), transform 0.5s cubic-bezier(0.3, 0.01, 0, 1) |
| hover | background rgba(35, 35, 35, 0.05) `light.measured.color.action.ctaHover`; shadow #585858 0px 0px 0px 1px inset |
| focus-visible | outline 1px auto #101010 `light.measured.color.border.focusRing`, offset 0px |
| pressed | background rgba(35, 35, 35, 0.1); shadow #595959 0px 0px 0px 1px inset |

![Category expander default](components/crops/disc-cat-btn-default.png) ![Category expander hover](components/crops/disc-cat-btn-hover.png) ![Category expander focus-visible](components/crops/disc-cat-btn-focus-visible.png) ![Category expander pressed](components/crops/disc-cat-btn-pressed.png)

#### Fundraiser card
A discover-grid fundraiser card (image, location tag, title, raised line, progress bar); measured at rest and on hover, never followed. Read as `fundraiser-card` on the discover page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 354.66 x 339.78; padding 8px; radius 12px; background #ffffff `light.color.surface.default.default`; text GoFundMe Sans 14/24 175, #ffffff `light.color.surface.default.default`; transition background-color 0.5s cubic-bezier(0.3, 0.01, 0, 1) |
| hover | background #fafafa `light.color.surface.default.hover` |

![Fundraiser card default](components/crops/fundraiser-card-default.png) ![Fundraiser card hover](components/crops/fundraiser-card-hover.png)

#### Card title
The fundraiser title inside a discover card. Read as `card-title` on the discover page.

**Values (default).** size 306.66 x 32; background transparent; text GoFundMe Sans 16/16 175, #232323 `light.color.text.default`.

![Card title default](components/crops/card-title-default.png)

#### Goal bar (card)
The progress element inside a discover card. Read as `card-goal-bar` on the discover page.

**Values (default).** size 306.66 x 50; background transparent; text GoFundMe Sans 14/20 175, #232323 `light.color.text.default`; layers progress.fundraiser-card_progressBar.hrt-goal-bar 306.7x8.0 rgba(35, 35, 35, 0.05) 9999px.

Child layers that carry the look: progress 306.7x8 background rgba(35, 35, 35, 0.05) `light.measured.color.action.ctaHover` radius 9999px.

![Goal bar (card) default](components/crops/card-goal-bar-default.png)

#### Card location tag
The location tag chip overlaid on a card image. Read as `card-location` on the discover page.

**Values (default).** size 145 x 26; padding 0px 8px; border 1px solid transparent; radius 4px; background rgba(0, 0, 0, 0.55) `light.color.surface.on.overlay.default`; text GoFundMe Sans 14/24 175, #ffffff `light.color.surface.default.default`.

![Card location tag default](components/crops/card-location-default.png)

### Search

/s?q=medical — the results grid: the same fundraiser cards with organiser avatars.

#### Search headline
The /s results masthead. Read as `s-h1` on the search page.

Not on the page when it was captured.

#### Search result card
A fundraiser card in the /s?q=medical results grid; measured, never followed. Read as `s-card` on the search page.

**Values (default).** size 270 x 335; padding 16px; border 1px solid #d8d8d8 `light.color.surface.disabled.default`; radius 20px; background transparent; text GoFundMe Sans 20/22 175, #232323 `light.color.text.default`; transition background-color 0.5s cubic-bezier(0.3, 0.01, 0, 1), border-color 0.5s cubic-bezier(0.3, 0.01, 0, 1), box-shadow 0.5s cubic-bezier(0.3, 0.01, 0, 1).

![Search result card default](components/crops/s-card-default.png)

#### Avatar
An hrt-avatar on a search result (the organiser image). Read as `s-avatar` on the search page.

**Values (default).** size 96 x 96; radius 9999px; background #f5f5f5 `light.color.surface.neutral.medium.hover`; text GoFundMe Sans 24/36 175, #232323 `light.color.text.default`.

![Avatar default](components/crops/s-avatar-default.png)

### Fundraiser page

A public /f/<slug> campaign page: the title, the '$ raised of $ goal' line and goal bar, the 'Donate now'/'Share'/'Message' row (measured, never pressed), the media viewer arrows, the organiser avatar, 'Read more', the donations list heading and 'Report fundraiser'.

#### Fundraiser title
The campaign title h1 on a public /f/<slug> page. Read as `f-title` on the fundraiser page.

**Values (default).** size 1104 x 48; background transparent; text GoFundMe Sans 40/48 175, #232323 `light.color.text.default`.

![Fundraiser title default](components/crops/f-title-default.png)

#### Raised amount
The "$X raised of $Y goal" line. Read as `f-raised` on the fundraiser page.

**Values (default).** size 228.16 x 57.59; background transparent; text GoFundMe Sans 24/28.8 175, #232323 `light.color.text.default`.

![Raised amount default](components/crops/f-raised-default.png)

#### Goal bar (fundraiser)
The progress element beside the raised line (a progress-meter on the campaign pages). Read as `f-goal-bar` on the fundraiser page.

**Values (default).** size 308.16 x 77.59; background transparent; text GoFundMe Sans 14/21 175, #232323 `light.color.text.default`; icon 64 x 64, #232323 `light.color.text.default`.

![Goal bar (fundraiser) default](components/crops/f-goal-bar-default.png)

#### Donate button
The primary "Donate now" button; all four states measured, the button never pressed — no donation was ever started. Read as `f-donate` on the fundraiser page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 308.16 x 48; padding 2px 24px; radius 9999px; background #ccf88e `light.color.button.primary.surface.strong.default`; text GoFundMe Sans 16/20 175, #274a34 `light.color.button.primary.surface.default`; transition background-color 0.5s cubic-bezier(0.3, 0.01, 0, 1), box-shadow 0.5s cubic-bezier(0.3, 0.01, 0, 1), color 0.5s cubic-bezier(0.3, 0.01, 0, 1), opacity 0.5s cubic-bezier(0.3, 0.01, 0, 1), transform 0.5s cubic-bezier(0.3, 0.01, 0, 1) |
| hover | background #e9fcce `light.color.button.primary.surface.strong.hover` |
| focus-visible | outline 1px auto #101010 `light.measured.color.border.focusRing`, offset 1px |
| pressed | background #e9fccd; shadow rgba(53, 125, 58, 0.247) 0px 0px 0px 1440px inset |

![Donate button default](components/crops/f-donate-default.png) ![Donate button hover](components/crops/f-donate-hover.png) ![Donate button focus-visible](components/crops/f-donate-focus-visible.png) ![Donate button pressed](components/crops/f-donate-pressed.png)

#### Share button
The secondary "Share" button; states measured, never pressed. Read as `f-share` on the fundraiser page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 308.16 x 48; padding 2px 24px; radius 9999px; background #274a34 `light.color.button.primary.surface.default`; text GoFundMe Sans 16/20 175, #ccf88e `light.color.button.primary.surface.strong.default`; transition background-color 0.5s cubic-bezier(0.3, 0.01, 0, 1), box-shadow 0.5s cubic-bezier(0.3, 0.01, 0, 1), color 0.5s cubic-bezier(0.3, 0.01, 0, 1), opacity 0.5s cubic-bezier(0.3, 0.01, 0, 1), transform 0.5s cubic-bezier(0.3, 0.01, 0, 1) |
| hover | background #2d6339 `light.color.button.primary.surface.hover` |
| focus-visible | outline 1px auto #101010 `light.measured.color.border.focusRing`, offset 0px |
| pressed | background #2d6339 `light.color.button.primary.surface.hover`; shadow rgba(53, 125, 58, 0.247) 0px 0px 0px 1440px inset |

![Share button default](components/crops/f-share-default.png) ![Share button hover](components/crops/f-share-hover.png) ![Share button focus-visible](components/crops/f-share-focus-visible.png) ![Share button pressed](components/crops/f-share-pressed.png)

#### Message button
The "Message" button beside Share; states measured, never pressed. Read as `f-message` on the fundraiser page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 117 x 40; padding 2px 24px; radius 9999px; background rgba(255, 255, 255, 0) `light.measured.color.action.ctaFill`; shadow #b7b7b6 0px 0px 0px 1px inset; text GoFundMe Sans 16/20 175, #232323 `light.color.text.default`; transition background-color 0.5s cubic-bezier(0.3, 0.01, 0, 1), box-shadow 0.5s cubic-bezier(0.3, 0.01, 0, 1), color 0.5s cubic-bezier(0.3, 0.01, 0, 1), opacity 0.5s cubic-bezier(0.3, 0.01, 0, 1), transform 0.5s cubic-bezier(0.3, 0.01, 0, 1) |
| hover | background rgba(35, 35, 35, 0.05) `light.measured.color.action.ctaHover`; shadow #585858 0px 0px 0px 1px inset |
| focus-visible | outline 1px auto #101010 `light.measured.color.border.focusRing`, offset 0px |
| pressed | background rgba(35, 35, 35, 0.1); shadow #595959 0px 0px 0px 1px inset |

![Message button default](components/crops/f-message-default.png) ![Message button hover](components/crops/f-message-hover.png) ![Message button focus-visible](components/crops/f-message-focus-visible.png) ![Message button pressed](components/crops/f-message-pressed.png)

#### Read more
The text-button expanding the campaign story; measured at rest, never toggled. Read as `f-readmore` on the fundraiser page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 83 x 24; background transparent; text GoFundMe Sans 16/24 100, #232323 `light.color.text.default` |
| focus-visible | outline 1px auto #101010 `light.measured.color.border.focusRing`, offset 0px; layers button.hrt-text-button.hrt-text-button--underlined 83.0x24.0 1px auto rgb(16, 16, 16) offset 0px |

![Read more default](components/crops/f-readmore-default.png) ![Read more hover](components/crops/f-readmore-hover.png) ![Read more focus-visible](components/crops/f-readmore-focus-visible.png) ![Read more pressed](components/crops/f-readmore-pressed.png)

#### Organiser avatar
The organiser avatar in the campaign meta row. Read as `f-avatar` on the fundraiser page.

**Values (default).** size 40 x 40; radius 9999px; background #f5f5f5 `light.color.surface.neutral.medium.hover`; text GoFundMe Sans 16/24 175, #232323 `light.color.text.default`.

![Organiser avatar default](components/crops/f-avatar-default.png)

#### Media viewer arrow
An arrow icon-button on the fundraiser media viewer; measured never pressed. Read as `f-media-nav` on the fundraiser page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 32 x 32; radius 9999px; background rgba(0, 0, 0, 0.55) `light.color.surface.on.overlay.default`; shadow rgba(35, 35, 35, 0.1) 0px 1px 2px 0px; text GoFundMe Sans 16/24 100, #ffffff `light.color.surface.default.default`; transition background-color 0.5s cubic-bezier(0.3, 0.01, 0, 1), box-shadow 0.5s cubic-bezier(0.3, 0.01, 0, 1), color 0.5s cubic-bezier(0.3, 0.01, 0, 1), opacity 0.5s cubic-bezier(0.3, 0.01, 0, 1), transform 0.5s cubic-bezier(0.3, 0.01, 0, 1); icon 16 x 16, #ffffff `light.color.surface.default.default` |
| hover | border 1px solid #ffffff `light.color.surface.default.default`; background rgba(0, 0, 0, 0.25); shadow rgba(35, 35, 35, 0.1) 0px 1.99645px 5.98582px 0px |
| focus-visible | outline 1px auto #101010 `light.measured.color.border.focusRing`, offset 0px |
| pressed | border 1px solid #ffffff `light.color.surface.default.default`; background rgba(0, 0, 0, 0.255); shadow rgba(35, 35, 35, 0.1) 0px 1.98476px 5.93903px 0px |

![Media viewer arrow default](components/crops/f-media-nav-default.png) ![Media viewer arrow hover](components/crops/f-media-nav-hover.png) ![Media viewer arrow focus-visible](components/crops/f-media-nav-focus-visible.png) ![Media viewer arrow pressed](components/crops/f-media-nav-pressed.png)

#### Report link
The "Report fundraiser" text-button; measured, never pressed. Read as `f-report` on the fundraiser page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 171 x 40; padding 2px 8px; radius 9999px; background transparent; text GoFundMe Sans 16/20 100, #232323 `light.color.text.default`; transition background-color 0.5s cubic-bezier(0.3, 0.01, 0, 1), box-shadow 0.5s cubic-bezier(0.3, 0.01, 0, 1), color 0.5s cubic-bezier(0.3, 0.01, 0, 1), opacity 0.5s cubic-bezier(0.3, 0.01, 0, 1), transform 0.5s cubic-bezier(0.3, 0.01, 0, 1); icon 16 x 16, #232323 `light.color.text.default` |
| hover | background rgba(35, 35, 35, 0.05) `light.measured.color.action.ctaHover` |
| focus-visible | outline 1px auto #101010 `light.measured.color.border.focusRing`, offset 1px; layers a.hrt-px-1.hrt-gap-half 171.0x40.0 1px auto rgb(16, 16, 16) offset 1px 9999px |
| pressed | background rgba(35, 35, 35, 0.098) |

![Report link default](components/crops/f-report-default.png) ![Report link hover](components/crops/f-report-hover.png) ![Report link focus-visible](components/crops/f-report-focus-visible.png) ![Report link pressed](components/crops/f-report-pressed.png)

#### Collection pill (page)
The "Nearby"-style collection filter pill on the related-fundraisers rail; measured at rest, never toggled. Read as `f-collection` on the fundraiser page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 247 x 40; padding 2px 24px; radius 24px; background rgba(0, 0, 0, 0.1) `light.color.surface.implied.on.strong.default`; shadow #ffffff 0px 0px 0px 1px inset; text GoFundMe Sans 16/20 175, #ffffff `light.color.surface.default.default`; transition background-color 0.5s cubic-bezier(0.3, 0.01, 0, 1), box-shadow 0.5s cubic-bezier(0.3, 0.01, 0, 1), color 0.5s cubic-bezier(0.3, 0.01, 0, 1), opacity 0.5s cubic-bezier(0.3, 0.01, 0, 1), transform 0.5s cubic-bezier(0.3, 0.01, 0, 1); icon 16 x 16, #ffffff `light.color.surface.default.default` |
| hover | background rgba(254, 254, 254, 0.1) |
| focus-visible | outline 1px auto #101010 `light.measured.color.border.focusRing`, offset 0px |
| pressed | background rgba(253, 253, 253, 0.2) |

![Collection pill (page) default](components/crops/f-collection-default.png) ![Collection pill (page) hover](components/crops/f-collection-hover.png) ![Collection pill (page) focus-visible](components/crops/f-collection-focus-visible.png) ![Collection pill (page) pressed](components/crops/f-collection-pressed.png)

#### Donations heading
The "Donations (N)" section heading above the supporter list. Read as `f-donations-h2` on the fundraiser page.

Not on the page when it was captured.

### Pricing (content stack)

/c/pricing — the WordPress content stack, an older hrt-base-*/wp-* layer that does not share the consumer app's hrt button hierarchy: the masthead, the audience segment toggles, the CSS-disclosure FAQ rows, wp-block CTAs and the language switcher.

#### Pricing headline
"Simple pricing, powerful fundraising" — the /c/pricing masthead on the WordPress content stack. Read as `price-h1` on the pricing page.

**Values (default).** size 890 x 180.38; background transparent; text GoFundMeSans 82/90.2 700, #232323 `light.color.text.default`.

![Pricing headline default](components/crops/price-h1-default.png)

#### Audience toggle
An "Individual or business / Certified nonprofit" segment toggle on the fee section; measured at rest, never switched (switching would re-tab the fees). Read as `price-toggle` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 772 x 65; border B: 1px solid #d8d8d8 `light.color.surface.disabled.default`; background transparent; text GoFundMeSans 24/30 700, #333333; icon 32 x 32, #333333; layers div.group 772.0x65.0 B:1px rgb(216, 216, 216) |
| focus-visible | layers div.group 772.0x65.0 B:1px rgb(216, 216, 216); input.toggle 13.0x13.0 1px auto rgb(16, 16, 16) offset 2px |

Child layers that carry the look: div 772x65 border 1px #d8d8d8 `light.color.surface.disabled.default`.

![Audience toggle default](components/crops/price-toggle-default.png) ![Audience toggle hover](components/crops/price-toggle-hover.png) ![Audience toggle focus-visible](components/crops/price-toggle-focus-visible.png) ![Audience toggle pressed](components/crops/price-toggle-pressed.png)

#### FAQ row
A CSS-disclosure FAQ row (checkbox + label) in the pricing FAQ; measured at rest, never opened. Read as `price-faq` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 772 x 65; border B: 1px solid #d8d8d8 `light.color.surface.disabled.default`; background transparent; text GoFundMeSans 24/30 700, #333333; icon 32 x 32, #333333; layers div.group 772.0x65.0 B:1px rgb(216, 216, 216) |

Child layers that carry the look: div 772x65 border 1px #d8d8d8 `light.color.surface.disabled.default`.

![FAQ row default](components/crops/price-faq-default.png) ![FAQ row hover](components/crops/price-faq-hover.png)

#### Locale select (content stack)
The WordPress language switcher in the content-stack footer; measured, never changed. Read as `wp-locale` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 238 x 35; padding 0px 32px 0px 16px; border 1px solid #c0bdb8; radius 12px; background #ffffff `light.color.surface.default.default`; image an image (data URI); text GoFundMeSans 16/24 400, #232323 `light.color.text.default`; transition border-color 0.25s ease-in-out |
| focus-visible | outline 1px auto #101010 `light.measured.color.border.focusRing`, offset 0px |

![Locale select (content stack) default](components/crops/wp-locale-default.png) ![Locale select (content stack) hover](components/crops/wp-locale-hover.png) ![Locale select (content stack) focus-visible](components/crops/wp-locale-focus-visible.png) ![Locale select (content stack) pressed](components/crops/wp-locale-pressed.png)

#### Content CTA
A wp-block button on the content stack; measured, never followed. Read as `wp-button` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 191 x 48; padding 8px 24px; border 1px solid transparent; radius 9999px; background #ccf88e `light.color.button.primary.surface.strong.default`; text GoFundMeSans 16/20 700, #274a34 `light.color.button.primary.surface.default`; transition background-color 0.5s cubic-bezier(0.3, 0.01, 0, 1), box-shadow 0.5s cubic-bezier(0.3, 0.01, 0, 1), color 0.5s cubic-bezier(0.3, 0.01, 0, 1), border-color 0.5s cubic-bezier(0.3, 0.01, 0, 1), opacity 0.5s cubic-bezier(0.3, 0.01, 0, 1), transform 0.5s cubic-bezier(0.3, 0.01, 0, 1) |
| hover | background #e9fcce `light.color.button.primary.surface.strong.hover` |
| focus-visible | outline 1px auto #101010 `light.measured.color.border.focusRing`, offset 1px; text GoFundMeSans 16/20 700, #026c3b |
| pressed | background #e8fccd |

![Content CTA default](components/crops/wp-button-default.png) ![Content CTA hover](components/crops/wp-button-hover.png) ![Content CTA focus-visible](components/crops/wp-button-focus-visible.png) ![Content CTA pressed](components/crops/wp-button-pressed.png)

### Start-a-fundraiser wizard

/create/fundraiser/category — the first wizard step, captured at rest: the country select, the postcode field (typed into then cleared), the category radio pills and 'Continue' — never submitted.

#### Wizard headline
"Let's begin your fundraising journey" — the /create/fundraiser/category masthead, captured at rest before any step was submitted. Read as `create-h1` on the create-fundraiser page.

**Values (default).** size 377.59 x 246; padding 158px 0px 0px 0px; background transparent; text GoFundMe Sans 40/44 100, #232323 `light.color.text.default`.

![Wizard headline default](components/crops/create-h1-default.png)

#### Country select
The "Select your country" select; measured at rest, never changed (changing would re-price the currency). Read as `create-country` on the create-fundraiser page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, focus-visible, pressed) | size 245.19 x 24; background transparent; text GoFundMe Sans 16/24 100, #232323 `light.color.text.default` |

![Country select default](components/crops/create-country-default.png) ![Country select hover](components/crops/create-country-hover.png) ![Country select focus-visible](components/crops/create-country-focus-visible.png) ![Country select pressed](components/crops/create-country-pressed.png)

#### Postcode field
The postcode text field; focused and typed into then cleared — the step was never submitted. Read as `create-zip` on the create-fundraiser page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focused, filled) | size 269.2 x 24; background transparent; text GoFundMe Sans 16/24 100, #232323 `light.color.text.default`; placeholder #6f6f6f `light.color.text.helper` |

![Postcode field default](components/crops/create-zip-default.png) ![Postcode field focused](components/crops/create-zip-focused.png) ![Postcode field filled](components/crops/create-zip-filled.png)

#### Category pill
A category radio pill (Animals, Business, Community…); measured at rest, never selected — selecting would be a wizard choice. Read as `create-pill` on the create-fundraiser page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 90 x 42; padding 8px 16px; border 1px solid #b7b7b6 `light.color.surface.neutral.subtle.pressed`; radius 20px; background transparent; text GoFundMe Sans 16/24 100, #232323 `light.color.text.default` |
| hover, pressed | background rgba(39, 74, 52, 0.1) `light.color.surface.implied.brand.hover` |

![Category pill default](components/crops/create-pill-default.png) ![Category pill hover](components/crops/create-pill-hover.png) ![Category pill focus-visible](components/crops/create-pill-focus-visible.png) ![Category pill pressed](components/crops/create-pill-pressed.png)

#### Continue button
The wizard "Continue" button; states measured, never clicked — no wizard step was ever submitted. Read as `create-continue` on the create-fundraiser page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 150 x 56; padding 2px 24px; radius 9999px; background #274a34 `light.color.button.primary.surface.default`; text GoFundMe Sans 16/20 175, #ccf88e `light.color.button.primary.surface.strong.default`; transition background-color 0.5s cubic-bezier(0.3, 0.01, 0, 1), box-shadow 0.5s cubic-bezier(0.3, 0.01, 0, 1), color 0.5s cubic-bezier(0.3, 0.01, 0, 1), opacity 0.5s cubic-bezier(0.3, 0.01, 0, 1), transform 0.5s cubic-bezier(0.3, 0.01, 0, 1); opacity 0.4 |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

![Continue button default](components/crops/create-continue-default.png) ![Continue button hover](components/crops/create-continue-hover.png) ![Continue button pressed](components/crops/create-continue-pressed.png)

#### Wizard sign-in link
The "Sign in" link above the wizard; measured, never followed. Read as `create-signin` on the create-fundraiser page.

Not on the page when it was captured.

### Sign-in boundary

/sign-in — the auth shell. In headless the auth island hydrates to a card ('Welcome', Google and Apple SSO, an e-mail field and 'Continue') or stays an empty form; the form was never submitted.

#### Sign-in card
The /sign-in document: the Welcome card a signed-out visitor gets — Google/Apple buttons, an email field and Continue. Never submitted. Read as `signin-shell` on the sign-in page.

**Values (default).** size 1440 x 900; background #ffffff `light.color.surface.default.default`; text GoFundMe Sans 16/24 100, #232323 `light.color.text.default`.

![Sign-in card default](components/crops/signin-shell-default.png)

#### Email field
The "Email Address" field on the sign-in card; focused, typed into and cleared — never submitted. Read as `signin-email` on the sign-in page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focused, filled) | size 385 x 25.11; padding 0px 7px; background transparent; text GoFundMeSans-Regular 16/normal 400, #333333; placeholder #333333 |

![Email field default](components/crops/signin-email-default.png) ![Email field focused](components/crops/signin-email-focused.png) ![Email field filled](components/crops/signin-email-filled.png)

#### Continue button
The sign-in card's primary "Continue" button; all four states measured with hover/focus/forced-active only — it was never clicked. Read as `signin-continue` on the sign-in page.

Not on the page when it was captured.

#### Google button
The "Sign in with Google" button; measured at rest and on hover/focus, never pressed (a press would start OAuth). Read as `signin-google` on the sign-in page.

Not on the page when it was captured.

### Mobile (390 wide)

The phone surface at 390 wide: the header with the nav toggle, the nav overlay, the hero and CTA.

#### Mobile header
The phone header at 390 wide: the mark, the menu toggle and the start CTA. Read as `m-header` on the home page at 390 wide.

**Values (default).** size 390 x 56; background transparent; text GoFundMe Sans 16/19.2 100, #232323 `light.color.text.default`; transition box-shadow 0.2s cubic-bezier(0.3, 0.01, 0, 1), background-color 0.2s cubic-bezier(0.3, 0.01, 0, 1); icon 24 x 24, #232323 `light.color.text.default`; layers a.hrt-header-skip.hrt-show-on-focus 16.0x34.0 rgb(255, 255, 255) 9999px; div.hrt-header-dropdown-caret 0.0x0.0 T:5px rgb(35, 35, 35) / R:4px rgba(0, 0, 0, 0) / L:4px rgba(0, 0, 0, 0); div.hrt-header-dropdown-content.hrt-header-dropdown-content--left 0.0x0.0 rgb(255, 255, 255) rgba(35, 35, 35, 0.1) 0px 6px 14px 0px 8px; div.hrt-spot-icon.hrt-spot-icon--neutral-subtle 0.0x0.0 rgb(245, 245, 245) 9999.

Child layers that carry the look: a 16x34 background #ffffff `light.color.surface.default.default` radius 9999px; div 0x0 border 5px #232323 `light.color.text.default`; div 0x0 background #ffffff `light.color.surface.default.default` radius 8px shadow rgba(35, 35, 35, 0.1) 0px 6px 14px 0px.

![Mobile header default](components/crops/m-header-default.png)

#### Mobile menu button
The header nav toggle at 390 wide — a local UI toggle; the opened state was measured after activating it. Read as `m-menu-btn` on the home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, opened) | size 40 x 40; radius 9999px; background transparent; text GoFundMe Sans 16/24 100, #232323 `light.color.text.default`; transition background-color 0.5s cubic-bezier(0.3, 0.01, 0, 1), box-shadow 0.5s cubic-bezier(0.3, 0.01, 0, 1), color 0.5s cubic-bezier(0.3, 0.01, 0, 1), opacity 0.5s cubic-bezier(0.3, 0.01, 0, 1), transform 0.5s cubic-bezier(0.3, 0.01, 0, 1); icon 24 x 24, #232323 `light.color.text.default` |
| focus-visible | outline 1px auto #e59700, offset 0px; layers button.hrt-icon-button.hrt-icon-button--hierarchy-tertiary 40.0x40.0 1px auto rgb(229, 151, 0) offset 0px 9999px |
| pressed | background rgba(35, 35, 35, 0.1) |

![Mobile menu button default](components/crops/m-menu-btn-default.png) ![Mobile menu button hover](components/crops/m-menu-btn-hover.png) ![Mobile menu button focus-visible](components/crops/m-menu-btn-focus-visible.png) ![Mobile menu button pressed](components/crops/m-menu-btn-pressed.png) ![Mobile menu button opened](components/crops/m-menu-btn-opened.png)

#### Mobile nav overlay
The nav overlay opened by the menu button; its links were never followed. Read as `m-drawer` on the home page at 390 wide.

**Values (default).** size 390 x 844; background transparent; text GoFundMe Sans 20/22 100, #232323 `light.color.text.default`; icon 24 x 24, #232323 `light.color.text.default`; layers div.hrt-rounded-0.hrt-side-modal 330.0x844.0 rgb(255, 255, 255) rgba(35, 35, 35, 0.1) 0px 6px 14px 0px; div.hrt-modal-header 330.0x56.0 rgb(255, 255, 255); div.hrt-modal-body 330.0x594.0 T:1px rgba(0, 0, 0, 0) / B:1px rgba(0, 0, 0, 0); a.hrt-base-list-item--heading-size.hrt-base-list-item 282.0x96.0 rgb(255, 255, 255) 12px; button.hrt-base-list-item--heading-size.hrt-base-list-item 282.0x96.0 rgb(.

Child layers that carry the look: div 330x844 background #ffffff `light.color.surface.default.default` shadow rgba(35, 35, 35, 0.1) 0px 6px 14px 0px; div 330x56 background #ffffff `light.color.surface.default.default`; div 330x594 border 1px transparent.

![Mobile nav overlay default](components/crops/m-drawer-default.png)

#### Mobile hero headline
The masthead at 390 wide. Read as `m-hero-h1` on the home page at 390 wide.

**Values (default).** size 330 x 88.75; background transparent; text GoFundMe Sans 40.33/44.37 175, #232323 `light.color.text.default`.

![Mobile hero headline default](components/crops/m-hero-h1-default.png)

#### Mobile hero CTA
The hero "Start a GoFundMe" button at 390 wide; measured never followed. Read as `m-hero-cta` on the home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 190 x 56; padding 2px 24px; radius 9999px; background #274a34 `light.color.button.primary.surface.default`; text GoFundMe Sans 16/20 175, #ccf88e `light.color.button.primary.surface.strong.default`; transition background-color 0.5s cubic-bezier(0.3, 0.01, 0, 1), box-shadow 0.5s cubic-bezier(0.3, 0.01, 0, 1), color 0.5s cubic-bezier(0.3, 0.01, 0, 1), opacity 0.5s cubic-bezier(0.3, 0.01, 0, 1), transform 0.5s cubic-bezier(0.3, 0.01, 0, 1) |
| focus-visible | outline 1px auto #e59700, offset 1px |
| pressed | background #2d6339 `light.color.button.primary.surface.hover`; shadow rgba(53, 125, 58, 0.247) 0px 0px 0px 844px inset |

![Mobile hero CTA default](components/crops/m-hero-cta-default.png) ![Mobile hero CTA hover](components/crops/m-hero-cta-hover.png) ![Mobile hero CTA focus-visible](components/crops/m-hero-cta-focus-visible.png) ![Mobile hero CTA pressed](components/crops/m-hero-cta-pressed.png)

### Footer

The page footer: sitemap columns, social icons, the 'United States · English' locale control and the Transcend 'Manage Cookie Preferences' link.

#### Footer
The page footer: column links, social icons, the locale selector and the Transcend consent link. Read as `footer` on the home page.

**Values (default).** size 1440 x 686; background transparent; text GoFundMe Sans 16/24 175, #232323 `light.color.text.default`; icon 16 x 16, #232323 `light.color.text.default`; layers div.hrt-mt-0.hrt-mb-0 1440.0x1.0 T:1px rgb(216, 216, 216); a.hrt-base-list-item--condensed-size.hrt-base-list-item 268.0x40.0 rgb(255, 255, 255) 12px; a.hrt-base-list-item--condensed-size.hrt-base-list-item 268.0x40.0 rgb(255, 255, 255) 12px; a.hrt-base-list-item--condensed-size.hrt-base-list-item 268.0x40.0 rgb(255, 255, 255) 12px; a.hrt-base-list-item--condensed-size.hrt-base-list-item 268.0x40..

Child layers that carry the look: div 1440x1 border 1px #d8d8d8 `light.color.surface.disabled.default`; a 268x40 background #ffffff `light.color.surface.default.default` radius 12px; a 268x40 background #ffffff `light.color.surface.default.default` radius 12px.

![Footer default](components/crops/footer-default.png)

#### Footer link
A footer sitemap link; measured, never followed. Read as `footer-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 268 x 40; padding 8px; radius 12px; background #ffffff `light.color.surface.default.default`; text GoFundMe Sans 16/24 100, #232323 `light.color.text.default` |
| hover | background #fafafa `light.color.surface.default.hover` |
| focus-visible | outline 1px auto #101010 `light.measured.color.border.focusRing`, offset 1px |
| pressed | background #fafafa `light.color.surface.default.hover` |

![Footer link default](components/crops/footer-link-default.png) ![Footer link hover](components/crops/footer-link-hover.png) ![Footer link focus-visible](components/crops/footer-link-focus-visible.png) ![Footer link pressed](components/crops/footer-link-pressed.png)

#### Footer accordion
A footer accordion button ("More resources"); measured at rest, never toggled. Read as `footer-more` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 158 x 40; padding 2px 8px; radius 9999px; background transparent; text GoFundMe Sans 16/20 100, #232323 `light.color.text.default`; transition background-color 0.5s cubic-bezier(0.3, 0.01, 0, 1), box-shadow 0.5s cubic-bezier(0.3, 0.01, 0, 1), color 0.5s cubic-bezier(0.3, 0.01, 0, 1), opacity 0.5s cubic-bezier(0.3, 0.01, 0, 1), transform 0.5s cubic-bezier(0.3, 0.01, 0, 1); icon 16 x 16, #232323 `light.color.text.default` |
| hover | background rgba(35, 35, 35, 0.05) `light.measured.color.action.ctaHover` |
| focus-visible | outline 1px auto #101010 `light.measured.color.border.focusRing`, offset 0px; layers button.hrt-footer-resources-button.hrt-button 158.0x40.0 1px auto rgb(16, 16, 16) offset 0px 9999px |
| pressed | background rgba(35, 35, 35, 0.1) |

![Footer accordion default](components/crops/footer-more-default.png) ![Footer accordion hover](components/crops/footer-more-hover.png) ![Footer accordion focus-visible](components/crops/footer-more-focus-visible.png) ![Footer accordion pressed](components/crops/footer-more-pressed.png)

#### Locale selector
The "United States · English" locale control in the footer; measured, never opened (opening would offer a locale switch). Read as `locale-btn` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 187 x 36; padding 8px; radius 12px; background rgba(255, 255, 255, 0) `light.measured.color.action.ctaFill`; shadow #b7b7b6 0px 0px 0px 1px inset; text GoFundMe Sans 14/20 100, #232323 `light.color.text.default`; transition background-color 0.5s cubic-bezier(0.3, 0.01, 0, 1), box-shadow 0.5s cubic-bezier(0.3, 0.01, 0, 1), color 0.5s cubic-bezier(0.3, 0.01, 0, 1), opacity 0.5s cubic-bezier(0.3, 0.01, 0, 1), transform 0.5s cubic-bezier(0.3, 0.01, 0, 1); icon 16 x 16, #232323 `light.color.text.default` |
| hover | background rgba(35, 35, 35, 0.05) `light.measured.color.action.ctaHover`; shadow #585858 0px 0px 0px 1px inset |
| focus-visible | outline 1px auto #101010 `light.measured.color.border.focusRing`, offset 0px |
| pressed | background rgba(35, 35, 35, 0.1); shadow #595959 0px 0px 0px 1px inset |

![Locale selector default](components/crops/locale-btn-default.png) ![Locale selector hover](components/crops/locale-btn-hover.png) ![Locale selector focus-visible](components/crops/locale-btn-focus-visible.png) ![Locale selector pressed](components/crops/locale-btn-pressed.png)

#### Cookie preferences link
The "Manage Cookie Preferences" Transcend footer control; measured, never pressed (it would open the consent manager). Read as `cookie-btn` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 0 x 0; padding 2px 8px; radius 9999px; background transparent; text GoFundMe Sans 16/20 100, #232323 `light.color.text.default`; transition background-color 0.5s cubic-bezier(0.3, 0.01, 0, 1), box-shadow 0.5s cubic-bezier(0.3, 0.01, 0, 1), color 0.5s cubic-bezier(0.3, 0.01, 0, 1), opacity 0.5s cubic-bezier(0.3, 0.01, 0, 1), transform 0.5s cubic-bezier(0.3, 0.01, 0, 1) |
| pressed | background rgba(35, 35, 35, 0.1) |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

## Icons

No standalone SVG icon set was lifted on this pass; the icons in the crops and screenshots (the GoFundMe mark, the dropdown carets, carousel arrows, social glyphs, card photography) are the product's artwork. Declared under layoutGaps in the catalog entry.

| Icon | Rendered sizes | View box | Style | Seen on | Next to |
|---|---|---|---|---|---|

## Gaps

### The signed-in product

GoFundMe's product is the fundraiser dashboard and the donation checkout: campaign management, donor lists, updates, withdrawals and every surface after `Sign in` needs an account and was never reached; starting a donation means payment details and was never begun. /sign-in is the only auth surface a signed-out visitor sees, and it was measured as a form, never submitted. The /create/fundraiser wizard's first step is public — it was captured at rest and never submitted.

### Pages

- **The account.** The fundraiser dashboard and every post-login surface (campaign management, donor lists, updates, withdrawals) was never reached; the /sign-in form was measured as a form and never submitted; 'Sign in with Google' and 'Continue with Apple' were never followed.
- **The donation checkout.** 'Donate now', 'Share' and 'Message' on a fundraiser page were measured in every state and never pressed — no tip, payment or donation flow was ever begun; the checkout's own design is uncaptured.
- **Forms.** The wizard's postcode field was measured at rest and typed into then cleared — nothing was sent; what a submission returns is unverified. Later wizard steps sit behind the first Continue and were never reached.
- **Blog posts and help articles** are index-level captures only; individual articles are the same templates, unmeasured.

### States

- **Pressed** was forced with DevTools on every control, so a state a script adds on mousedown (if any) is missing.
- **Disabled, error, loading and validation states** were not seen on the public surface — the forms were never submitted.
- **The audience toggles on /c/pricing** switch the fee table between 'Individual or business' and 'Certified nonprofit'; they were measured at rest and never switched, so the nonprofit fee column is uncaptured.
- **The header dropdown panels' focus/hover** is partially covered: the panels open on hover and close on blur, so a real keyboard focus inside one could not be held.

### Themes

Every consumer page paints one surface — the light palette the `:root`-declared `--hrt-*` colour roles resolve to; no theme switcher or alternate layer exists on the consumer site. The sheets do declare a `[data-theme="pro"]` layer for GoFundMe Pro — it is kept in raw/css-vars.json as declared evidence but never paints on the captured surfaces. The /c/* pages are the WordPress content stack, an older hrt-base-*/wp-* layer whose values are component tokens, not the consumer theme. There is no painted dark variant of the consumer site.

### Fonts

- The consumer pages set the hrt typefaces declared in `--hrt-font-family-*`/`--hrt-typeface` (the @font-face list is in raw/css-vars.json); the measured face on each component is in its entry. The /c/* content stack sets its own faces. The style guide falls back to system sans.

### Screenshots

- The fundraiser photos, campaign titles, organiser names and beneficiary locations in the screenshots and card crops are public published content — real campaigns the product itself surfaces on /discover.
- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files.

### Content left out

- Marketing copy, fee figures, campaign text, organiser names and supporter names are the product's content; only frames and components were measured.
