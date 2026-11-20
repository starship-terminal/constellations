# Mesh components

The discovery list of every page and view captured, then one entry per component with crops of the real product, and the Gaps. Captured from me.sh on 2026-11-16 — clay.earth 301s there; the Clay product rebranded to Mesh — signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running page. Nothing was signed into, paid for or submitted.

The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) (39 components, 94 states).

How to read an entry:

- A colour is its value followed by the palette token in [tokens.json](tokens.json) with the same value, when there is one. Text is written family size/line-height weight, then its colour, for example `Verlag 14/14 700, #fff`, and is read from the first text node inside the component.
- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example "default (same: focus-visible)". When the root paints nothing, "Child layers" names the first nodes inside it that do.
- Crops are images of the component read from the live page, in [components/crops/](components/crops) (85 files, named `{component}-{state}.png`, at 2x). Screenshots are in [screenshots/](screenshots).

## Discovery list

Screenshots are named `{page}-{theme}-{state}.png`: the marketing site paints a dark theme on / and a warm light theme on /pricing and the sign-in card — the suffix is the theme the page actually paints. Desktop shots are 1440 x 900 at 1x; `-full` shots are whole pages (1x on desktop, 2x on mobile); mobile shots are `mobile-{page}-{theme}-{state}.png`, 780 wide (390 at 2x).

| Surface | URL | Screenshots |
|---|---|---|
| Home | `/` | [default](screenshots/home-dark-default.png), [full](screenshots/home-dark-full.png), [menu](screenshots/home-dark-menu.png) |
| Pricing | `/pricing` | [default](screenshots/pricing-light-default.png), [full](screenshots/pricing-light-full.png) |
| Integrations | `/integrations` | [default](screenshots/integrations-dark-default.png), [full](screenshots/integrations-dark-full.png) |
| Nexus | `/nexus` | [default](screenshots/nexus-dark-default.png), [full](screenshots/nexus-dark-full.png) |
| Teams | `/teams` | [default](screenshots/teams-dark-default.png), [full](screenshots/teams-dark-full.png) |
| Get started | `/start` | [default](screenshots/start-dark-default.png), [full](screenshots/start-dark-full.png) |
| Stories | `/stories` | [default](screenshots/stories-dark-default.png), [full](screenshots/stories-dark-full.png) |
| Serendipity | `/serendipity` | [default](screenshots/serendipity-dark-default.png), [full](screenshots/serendipity-dark-full.png) |
| Mesh for Notion | `/notion` | [default](screenshots/notion-dark-default.png), [full](screenshots/notion-dark-full.png) |
| Our origins | `/story` | [default](screenshots/story-dark-default.png), [full](screenshots/story-dark-full.png) |
| Careers | `/careers` | [default](screenshots/careers-dark-default.png), [full](screenshots/careers-dark-full.png) |
| Apple Vision Pro | `/apple-vision-pro` | [default](screenshots/vision-dark-default.png), [full](screenshots/vision-dark-full.png) |
| About | `/about` | [default](screenshots/about-dark-default.png), [full](screenshots/about-dark-full.png) |
| Contact | `/contact` | [default](screenshots/contact-dark-default.png), [full](screenshots/contact-dark-full.png) |
| Sign-in (boundary) | `app.me.sh/login?signin` | [default](screenshots/signin-light-default.png) |
| Home, phone | `/` | [default](screenshots/mobile-home-dark-default.png), [full](screenshots/mobile-home-dark-full.png), [menu-open](screenshots/mobile-home-dark-menu-open.png) |
| Pricing, phone | `/pricing` | [default](screenshots/mobile-pricing-light-default.png), [full](screenshots/mobile-pricing-light-full.png) |

### Overlays and transient states

| State | Where | How it was reached | Captured |
|---|---|---|---|
| Nav menu, open | nav pill, desktop | the dropdown trigger's own press | [home-dark-menu](screenshots/home-dark-menu.png), [menu-panel](#nav-menu) |
| Mobile menu, open | bar, phone | the hamburger's own press | [mobile-home-dark-menu-open](screenshots/mobile-home-dark-menu-open.png), [m-menu-open](#mobile-menu-open) |

## Shared values

Values that apply across entries, from the measurement files.

**Focus.** 10 components were given a real keyboard focus (a further 7 could not be driven: `nav-cta`, `cta`, `cta-bottom`, `plan-cta`, `signin-email-btn`, `m-cta`, `plan-cta-filled`). 4 show a visible focus state: `nav-signin` (1px auto #101010, offset 1px), `filter-button` (1px auto #101010, offset 0px), `footer-link` (1px auto #101010, offset 1px), `footer-social` (1px auto #101010, offset 1px). The other 6 show no change a keyboard user can see: `nav-item`, `nav-dropdown`, `signin-apple`, `signin-google`, `signin-toggle`, `m-menu-link`.

**Pressed.** Forced with DevTools (`CSS.forcePseudoState` :active:hover): the controls hold their hover state through press — the filled plan CTA stays #fb7232, the Google button stays at 87% blue, the nav Sign-In keeps its 8% wash, and the white CTA pills shrink ~1% (205x54 -> 203x53.5). Nothing a real press would submit or navigate was ever pressed.

**Motion.** Transitions measured on the components, by duration.

| Duration | Easing | Property | Where |
|---|---|---|---|
| 0.1s | `ease-in-out` | color, opacity | m-menu-link, menu-card, nav-dropdown, nav-item |
| 0.15s | `ease-in-out` | background-color, border-color, color, filter, opacity | cta-bottom, filter-button, footer-link, footer-social, logo, menu-panel, plan-cta, plan-cta-filled and more |
| 0.2s | `ease` | background-color | nav-signin |
| 0.24s | `ease` | color | nav-dropdown, nav-item, nav-signin |
| 0.35s | `ease` | transform | cta |

**Card shapes.** Default-state values; the entries hold the states.

| Card | Size | Border | Radius | Background | Shadow | Padding |
|---|---|---|---|---|---|---|
| [Plan card](#plan-card) | 288 x 196 | 1px solid #eceae8 | 16px | linear-gradient(#ffffff `color.paper.100`, rgba(255, 255, 255, 0.5)) | none | 22px 24px 24px 24px |
| [Popular plan card](#popular-plan-card) | 288 x 196 | 1px solid #fb7232 `color.orange.500` | 16px | linear-gradient(#ffffff `color.paper.100`, rgba(255, 255, 255, 0.5)) | rgba(251, 114, 50, 0.24) 0px 0px 0px 3px | 22px 24px 24px 24px |
| [Nav menu](#nav-menu) | 556 x 154 | - | - | transparent | none | 0px 24px |
| [Billing toggle](#billing-toggle) | 226 x 40 | - | 12px | rgba(31, 31, 31, 0.06) `color.ink-alpha.6` | none | 0px 6px |

## Components

### Shell and navigation

The floating glass nav pill on the black ground, its dropdowns and the Sign-In and Get-Started actions.

#### Nav pill
The floating top nav: wordmark, the Releases/Resources/Company dropdowns, Pricing link and Sign In. Read as `header` on the home page.

**Values (default).** size 388 x 48; padding 0px 24px; radius 16px; background transparent; text Verlag 12/27 700, #ffffff `color.paper.100`; transform translate(-194px, 0px); icon 40 x 40, #ffffff `color.paper.100`.

Child layers that carry the look: div::before 388pxx48px background rgba(255, 255, 255, 0.03) `color.white-alpha.3` image linear-gradient(rgba(255, 255, 255, 0.12) 10%, rgba(255, 255, 255, 0) 86%) radius 16px shadow rgba(0, 0, 0, 0.06) 0px 0px 0px 0.5px, rgba(0, 0, 0, 0.1) 0px 2px 4px -2px, rgba(0, 0, 0, 0.06) 0px 8px 16px -8px, rgba(255, 255, 255, 0.03) `color.white-alpha.3` 0px 1px 0px 0px inset, rgba(255, 255, 255, 0.03) `color.white-alpha.3` 0px -1px 0px 0px inset, rgba(255, 255, 255, 0.03) `color.white-alpha.3` 0px -5px 6px 0px inset, rgba(255, 255, 255, 0.03) `color.white-alpha.3` 0px -8px 24px 0px inset; div::after 388pxx48px image linear-gradient(#272727, #111111) radius 16px shadow rgba(0, 0, 0, 0.08) 0px 2px 4px -2px, rgba(0, 0, 0, 0.03) 0px 8px 16px -8px, rgba(255, 255, 255, 0.03) `color.white-alpha.3` 0px 1px 0px 0px inset, rgba(255, 255, 255, 0.03) `color.white-alpha.3` 0px -1px 0px 0px inset, rgba(255, 255, 255, 0.03) `color.white-alpha.3` 0px -5px 6px 0px inset, rgba(255, 255, 255, 0.03) `color.white-alpha.3` 0px -8px 24px 0px inset; a 254x214.4 background rgba(255, 255, 255, 0.12) border 1px solid rgba(255, 255, 255, 0.06) `color.white-alpha.6` radius 12px.

![Nav pill default](components/crops/header-default.png)

#### Logo
The Mesh wordmark anchor. Read as `logo` on the home page.

**Values (default).** size 40 x 24; background transparent; text Verlag 18/27 400, #f2b98b `color.tan.300`; transition color 0.15s ease-in-out; icon 114 x 26, #f2b98b `color.tan.300`.

![Logo default](components/crops/logo-default.png)

#### Nav link
A plain nav link (Pricing). Read as `nav-item` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 57 x 27; background transparent; text Verlag 12/27 700, #ffffff `color.paper.100`; transition opacity 0.1s ease-in-out, color 0.24s ease; opacity 0.64 |
| hover, pressed | opacity none |

![Nav link default](components/crops/nav-item-default.png) ![Nav link hover](components/crops/nav-item-hover.png) ![Nav link focus-visible](components/crops/nav-item-focus-visible.png) ![Nav link pressed](components/crops/nav-item-pressed.png)

#### Nav dropdown
A nav dropdown trigger (the Releases/Resources/Company buttons); its own press opens the link menu (opened state). Read as `nav-dropdown` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 64 x 27; background transparent; text Verlag 12/27 700, #ffffff `color.paper.100`; transition opacity 0.1s ease-in-out, color 0.24s ease; opacity 0.64 |
| hover, pressed, opened | opacity none |

![Nav dropdown default](components/crops/nav-dropdown-default.png) ![Nav dropdown hover](components/crops/nav-dropdown-hover.png) ![Nav dropdown focus-visible](components/crops/nav-dropdown-focus-visible.png) ![Nav dropdown pressed](components/crops/nav-dropdown-pressed.png) ![Nav dropdown opened](components/crops/nav-dropdown-opened.png)

#### Nav menu
The opened nav dropdown panel, held open by the trigger toggle. Read as `menu-panel` on the home page.

**Values (default).** size 556 x 154; padding 0px 24px; background transparent; text Verlag 14/14 700, #ffffff `color.paper.100`; transition opacity 0.15s ease-in-out; transform translate(-278px, 0px); opacity 0.

![Nav menu default](components/crops/menu-panel-default.png)

#### Menu item
A link row inside the open nav menu. Read as `menu-card` on the home page.

**Values (default).** size 238 x 14; background transparent; text Verlag 14/14 700, #ffffff `color.paper.100`; transition color 0.1s ease-in-out.

![Menu item default](components/crops/menu-card-default.png)

#### Nav CTA
The "Get Started" action inside the nav pill; links to /start, measured never followed. Read as `nav-cta` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 123 x 32.03; background transparent; text Verlag 12/12 600, #ffffff `color.paper.100` |
| hover | child paint div.eoWgla_cta.y0DxmG_cta: background rgba(255, 255, 255, 0.04) |

Child layers that carry the look: div 123x32 radius 8px shadow rgba(255, 255, 255, 0.24) `color.white-alpha.24` 0px 0px 0px 1px inset; div::after calc(100% + 36px)xcalc(100% + 12px) image linear-gradient(225deg, #32c5ff 0%, #b620e0 51%, #f7b500 100%) radius 100%; div::before calc(100% + 36px)xcalc(100% + 12px) image linear-gradient(225deg, #32c5ff 0%, #b620e0 51%, #f7b500 100%).

![Nav CTA default](components/crops/nav-cta-default.png) ![Nav CTA hover](components/crops/nav-cta-hover.png) ![Nav CTA pressed](components/crops/nav-cta-pressed.png)

#### Sign-in link
The "Sign In" action in the nav pill; links to app.me.sh/login, measured never followed. Read as `nav-signin` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 83 x 34; padding 0px 16px; radius 8px; background transparent; text Verlag 12/0 700, rgba(255, 255, 255, 0.64) `color.white-alpha.64`; transition background-color 0.2s ease, color 0.24s ease |
| hover | background rgba(255, 255, 255, 0.08) `color.white-alpha.8`; text Verlag 12/0 700, #ffffff `color.paper.100`; child paint a.y0DxmG_signInBtn: size 83.0x34.0; background rgba(255, 255, 255, 0.08) `color.white-alpha.8`; radius 8px |
| focus-visible | outline 1px auto #101010, offset 1px; child paint a.y0DxmG_signInBtn: size 83.0x34.0; radius 8px; outline 1px auto rgb(16, 16, 16) offset 1px |
| pressed | background rgba(255, 255, 255, 0.08) `color.white-alpha.8`; text Verlag 12/0 700, rgba(255, 255, 255, 0.976); child paint a.y0DxmG_signInBtn: size 83.0x34.0; background rgba(255, 255, 255, 0.08) `color.white-alpha.8`; radius 8px |

![Sign-in link default](components/crops/nav-signin-default.png) ![Sign-in link hover](components/crops/nav-signin-hover.png) ![Sign-in link focus-visible](components/crops/nav-signin-focus-visible.png) ![Sign-in link pressed](components/crops/nav-signin-pressed.png)

### Home

The rotating-word hero in VerlagCondensed, the animated relationship counter, the white CTA pills and the feature filter pills.

#### Hero title
"Every relationship, organized." — the VerlagCondensed display headline. Read as `hero-title` on the home page.

**Values (default).** size 1232 x 64; background transparent; text VerlagCondensed 64/64 700, #fefef7 `color.cream.0`.

![Hero title default](components/crops/hero-title-default.png)

#### Section title
"Never miss what matters." — the first section heading (Verlag, 480x48); the hero carries no lede, only the display h1 and an animated stat counter. Read as `section-title` on the home page.

**Values (default).** size 480 x 48; background transparent; text VerlagCondensed 48/48 900, #1d1d1f `color.ink.700`.

![Section title default](components/crops/section-title-default.png)

#### Stat counter
One digit of the animated relationship-count ticker beside the hero (the digits cycle). Read as `stat-counter` on the home page.

**Values (default).** size 8 x 18; background transparent; text Verlag 18/18 700, #ffffff `color.paper.100`.

![Stat counter default](components/crops/stat-counter-default.png)

#### Hero CTA
The "Get Mesh Free" pill — the painted 205x54 off-white inner of the hero CTA; the anchor links to /start, never followed. Read as `cta` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 205 x 54; padding 0px 27px; radius 14px; background #fdfcfa `color.paper.0`; shadow rgba(255, 255, 255, 0.98) 0px 0px 4px 1px; text Verlag 18/18 600, #000000 `color.ink.950`; transition transform 0.35s ease |
| hover | size 202.95 x 53.46; transform scale(0.99); child paint div.eoWgla_ctaInner: size 202.9x53.5 |

![Hero CTA default](components/crops/cta-default.png) ![Hero CTA hover](components/crops/cta-hover.png) ![Hero CTA pressed](components/crops/cta-pressed.png)

#### Bottom CTA
The "Get Mesh Free" pill closing the page — a white 185x52 button on the #0f0f10 bottom band; never followed. Read as `cta-bottom` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 185 x 52; radius 16px; background #ffffff `color.paper.100`; text Verlag 16/16 600, #000000 `color.ink.950`; transition background-color 0.15s ease-in-out |
| hover | size 181.3 x 50.96; child paint div.eoWgla_cta.JzsFla_ctaButton: size 181.3x51.0 |

![Bottom CTA default](components/crops/cta-bottom-default.png) ![Bottom CTA hover](components/crops/cta-bottom-hover.png) ![Bottom CTA pressed](components/crops/cta-bottom-pressed.png)

#### Feature pill
A feature filter pill (Birthdays/Events/News/…); its press swaps the demo panel — a local toggle. Read as `filter-button` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 480 x 48; background transparent; text Verlag 20/27 400, #1d1d1f `color.ink.700`; transition opacity 0.15s ease-in-out; opacity 0.6; icon 24 x 24, #1d1d1f `color.ink.700` |
| hover | opacity none |
| focus-visible | outline 1px auto #101010, offset 0px; child paint button._9nEsHa_filterButton_Birthdays: size 480.0x48.0; outline 1px auto rgb(16, 16, 16) offset 0px |
| pressed | opacity none |

Child layers that carry the look: button::after 492pxx48px image linear-gradient(90deg, rgba(29, 29, 31, 0.06) 0%, rgba(29, 29, 31, 0.03) 100%) radius 16px.

![Feature pill default](components/crops/filter-button-default.png) ![Feature pill hover](components/crops/filter-button-hover.png) ![Feature pill focus-visible](components/crops/filter-button-focus-visible.png) ![Feature pill pressed](components/crops/filter-button-pressed.png)

#### Page ground
The html element's own painted fill — the black ground under every section (body itself is transparent). Read as `page-ground` on the home page.

**Values (default).** size 1440 x 8016.98; background #000000 `color.ink.950`; text Verlag 12/27 700, #1f1f1f `color.ink.800`; icon 114 x 26, #f2b98b `color.tan.300`.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Hero subcopy
"Mesh brings together everyone you've ever met…" — the serif lede under the display headline. Read as `hero-sub` on the home page.

**Values (default).** size 480 x 112; background transparent; text Verlag 20/28 400, #86868b `color.gray.400`.

![Hero subcopy default](components/crops/hero-sub-default.png)

### Pricing

The warm-cream pricing route: the billing toggle, the four plan cards and the orange popular ring.

#### Pricing title
"Invest in better relationships" — the pricing page display heading. Read as `pricing-h1` on the pricing page.

**Values (default).** size 590 x 56; background transparent; text VerlagCondensed 48/56 700, #1f1f1f `color.ink.800`.

![Pricing title default](components/crops/pricing-h1-default.png)

#### Plan card
A plan card (the Personal column); translucent gray fill on black. Read as `plan-card` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 288 x 196; padding 22px 24px 24px 24px; border 1px solid #eceae8; radius 16px; background rgba(149, 149, 149, 0.06) `color.gray-alpha.6`; image linear-gradient(#ffffff `color.paper.100`, rgba(255, 255, 255, 0.5)); text Verlag 14/14 600, #fb7232 `color.orange.500` |

![Plan card default](components/crops/plan-card-default.png) ![Plan card hover](components/crops/plan-card-hover.png)

#### Popular plan card
The Team plan card with the Popular tag. Read as `plan-card-popular` on the pricing page.

**Values (default).** size 288 x 196; padding 22px 24px 24px 24px; border 1px solid #fb7232 `color.orange.500`; radius 16px; background rgba(149, 149, 149, 0.06) `color.gray-alpha.6`; image linear-gradient(#ffffff `color.paper.100`, rgba(255, 255, 255, 0.5)); shadow rgba(251, 114, 50, 0.24) 0px 0px 0px 3px; text Verlag 14/14 600, #fb7232 `color.orange.500`.

![Popular plan card default](components/crops/plan-card-popular-default.png)

#### Plan price
The "Free"/"$10/ month" price line inside a plan card. Read as `plan-price` on the pricing page.

**Values (default).** size 238 x 56; padding 0px 0px 0px 4px; background transparent; text ChronicleCondensed 56/56 400, #1f1f1f `color.ink.800`.

![Plan price default](components/crops/plan-price-default.png)

#### Plan CTA
The "Get Started" outline action inside the Personal plan card (a button-styled div, 238x44); measured in all non-submitting states, never followed. Read as `plan-cta` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 238 x 44; border 1px solid rgba(31, 31, 31, 0.4) `color.ink-alpha.40`; radius 10px; background transparent; text Verlag 14/27 600, #1f1f1f `color.ink.800`; transition background-color 0.15s ease-in-out, color 0.15s ease-in-out, border-color 0.15s ease-in-out |
| hover, pressed | border 1px solid transparent; background #fb7232 `color.orange.500`; text Verlag 14/27 600, #ffffff `color.paper.100`; child paint div.htJ5kW_button: background #fb7232 `color.orange.500`; border 1px solid transparent |

![Plan CTA default](components/crops/plan-cta-default.png) ![Plan CTA hover](components/crops/plan-cta-hover.png) ![Plan CTA pressed](components/crops/plan-cta-pressed.png)

#### Plan CTA, filled
The filled orange "Try it free" action inside the popular Team card; never pressed for real. Read as `plan-cta-filled` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 238 x 44; border 1px solid transparent; radius 10px; background #fb7232 `color.orange.500`; wrapper div._3K18mq_card._3K18mq_popular: shadow rgba(251, 114, 50, 0.24) 0px 0px 0px 3px; text Verlag 14/27 600, #ffffff `color.paper.100`; transition background-color 0.15s ease-in-out, color 0.15s ease-in-out, border-color 0.15s ease-in-out |

![Plan CTA, filled default](components/crops/plan-cta-filled-default.png) ![Plan CTA, filled hover](components/crops/plan-cta-filled-hover.png) ![Plan CTA, filled pressed](components/crops/plan-cta-filled-pressed.png)

#### Billing toggle
The "Pay monthly / Pay annually" switcher above the plan cards (226x40, gray-chip fill); a local toggle, never flipped. Read as `billing-toggle` on the pricing page.

**Values (default).** size 226 x 40; padding 0px 6px; radius 12px; background rgba(31, 31, 31, 0.06) `color.ink-alpha.6`; text Verlag 10/27 600, rgba(31, 31, 31, 0.5).

![Billing toggle default](components/crops/billing-toggle-default.png)

#### Plan label
The PERSONAL/PRO/TEAM eyebrow label on a plan card. Read as `plan-name` on the pricing page.

**Values (default).** size 238 x 14; padding 0px 0px 0px 6px; background transparent; text Verlag 14/14 600, #fb7232 `color.orange.500`.

![Plan label default](components/crops/plan-name-default.png)

#### Pricing ground
The pricing page's warm-cream main surface (#f9f8f6) — pricing is a light route on the otherwise-dark site. Read as `pricing-ground` on the pricing page.

**Values (default).** size 1440 x 2386; padding 60px 0px 0px 0px; background #f9f8f6 `color.paper.50`; image url(…); text Verlag 12/27 700, #1f1f1f `color.ink.800`; icon 114 x 26, #f2b98b `color.tan.300`.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

### Sign-in page (boundary)

app.me.sh/login's public sign-in card — a light sibling surface on a different stack: fields were focused and filled with placeholder text only; nothing was submitted.

#### Sign-in title
"Sign in to Mesh" — the 32px headline on the app.me.sh sign-in card, a LIGHT sibling surface (#fcfcfc), a different stack from the dark marketing site. Read as `signin-title` on the sign-in page.

**Values (default).** size 272 x 30; background transparent; wrapper div._box_z86qt_27: shadow rgba(0, 0, 0, 0.08) 0px 2px 4px -2px, rgba(0, 0, 0, 0.03) 0px 8px 16px -8px, rgba(255, 255, 255, 0.5) 0px -10px 24px 0px inset, rgba(255, 255, 255, 0.24) 0px -16px 48px 0px inset; text ChronicleDisplayCondensed 32/21 400, #48494a `color.gray.500`.

![Sign-in title default](components/crops/signin-title-default.png)

#### E-mail field
The "Enter your email" field; filled with the documented test address then deleted, Sign in with email never pressed. Read as `signin-input` on the sign-in page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 272 x 40; padding 0px 12px; border 1px solid rgba(72, 73, 74, 0.1) `color.ink-alpha.10`; radius 6px; background rgba(72, 73, 74, 0.04) `color.ink-alpha.4`; text SFProText 14/21 400, #48494a `color.gray.500`; transition border-color 0.15s ease-in-out, background-color 0.15s ease-in-out; placeholder #48494a `color.gray.500` |
| focused, filled | border 1px solid #2686be; child paint input._textInput_5plfs_1: border 1px solid #2686be |

![E-mail field default](components/crops/signin-input-default.png) ![E-mail field focused](components/crops/signin-input-focused.png) ![E-mail field filled](components/crops/signin-input-filled.png)

#### E-mail sign-in
The orange "Sign in with email" button — the brand accent on this light surface; never pressed. Read as `signin-email-btn` on the sign-in page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 272 x 40; radius 12px; background #ff6821 `color.orange-app.500`; text SF Pro Text 14/21 400, rgba(255, 255, 255, 0.6) `color.white-alpha.60`; transition background-color 0.15s ease-in-out, color 0.15s ease-in-out |

![E-mail sign-in default](components/crops/signin-email-btn-default.png) ![E-mail sign-in hover](components/crops/signin-email-btn-hover.png) ![E-mail sign-in pressed](components/crops/signin-email-btn-pressed.png)

#### Apple sign-in
The "Sign in with Apple" OAuth button; never followed. Read as `signin-apple` on the sign-in page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 272 x 44; radius 12px; background #1f1f1e `color.ink.750`; text SF Pro Text 14/21 400, #ffffff `color.paper.100`; transition background-color 0.15s ease-in-out, color 0.15s ease-in-out; icon 18 x 21, #ffffff `color.paper.100` |
| hover, pressed | background rgba(31, 31, 30, 0.85); child paint button._loginBtn_1ii7i_42._button_ykqwo_1: background rgba(31, 31, 30, 0.85) |

![Apple sign-in default](components/crops/signin-apple-default.png) ![Apple sign-in hover](components/crops/signin-apple-hover.png) ![Apple sign-in focus-visible](components/crops/signin-apple-focus-visible.png) ![Apple sign-in pressed](components/crops/signin-apple-pressed.png)

#### Google sign-in
The "Sign in with Google" OAuth button (Google blue); never followed. Read as `signin-google` on the sign-in page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 272 x 44; radius 12px; background #5383ec `color.google.500`; text SF Pro Text 14/21 400, #ffffff `color.paper.100`; transition background-color 0.15s ease-in-out, color 0.15s ease-in-out; icon 18 x 18, #ffffff `color.paper.100` |
| hover, pressed | background rgba(83, 131, 236, 0.87) `color.google.600`; child paint button._loginBtn_1ii7i_42._button_ykqwo_1: background rgba(83, 131, 236, 0.87) `color.google.600` |

![Google sign-in default](components/crops/signin-google-default.png) ![Google sign-in hover](components/crops/signin-google-hover.png) ![Google sign-in focus-visible](components/crops/signin-google-focus-visible.png) ![Google sign-in pressed](components/crops/signin-google-pressed.png)

#### Create-account toggle
The "Create account" switcher on the sign-in card; a local toggle measured never pressed. Read as `signin-toggle` on the sign-in page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, focus-visible, pressed) | size 91 x 12; background transparent; text SFProText 12/12 400, #48494a `color.gray.500`; transition filter 0.15s ease-in-out |

![Create-account toggle default](components/crops/signin-toggle-default.png) ![Create-account toggle hover](components/crops/signin-toggle-hover.png) ![Create-account toggle focus-visible](components/crops/signin-toggle-focus-visible.png) ![Create-account toggle pressed](components/crops/signin-toggle-pressed.png)

### Footer

The #0f0f10 footer band, its link columns and social icons.

#### Footer
The #0f0f10 footer band: link columns, app links, the legal subfooter. Read as `footer` on the home page.

**Values (default).** size 1440 x 335; padding 150px 0px 0px 0px; background #0f0f10 `color.ink.900`; text Verlag 12/12 600, #ffffff `color.paper.100`; icon 16 x 16, #f2b98b `color.tan.300`.

![Footer default](components/crops/footer-default.png)

#### Footer link
Read as `footer-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 88 x 12; background transparent; text Verlag 12/12 700, rgba(255, 255, 255, 0.4) `color.white-alpha.40`; transition color 0.15s ease-in-out |
| hover | text Verlag 12/12 700, #efab74 `color.tan.400` |
| focus-visible | outline 1px auto #101010, offset 1px; child paint a.pNqdxq_navigationLink: size 88.0x12.0; outline 1px auto rgb(16, 16, 16) offset 1px |
| pressed | text Verlag 12/12 700, #ed9d5d |

![Footer link default](components/crops/footer-link-default.png) ![Footer link hover](components/crops/footer-link-hover.png) ![Footer link focus-visible](components/crops/footer-link-focus-visible.png) ![Footer link pressed](components/crops/footer-link-pressed.png)

#### Social link
A footer social icon link (X). Read as `footer-social` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 16 x 16; radius 4px; background rgba(255, 255, 255, 0.14); text Verlag 18/24 400, #f2b98b `color.tan.300`; transition background-color 0.15s ease-in-out; icon 16 x 16, #f2b98b `color.tan.300` |
| hover | background transparent; text Verlag 18/24 400, #efab74 `color.tan.400`; icon 16 x 16, #efab74 `color.tan.400` |
| focus-visible | outline 1px auto #101010, offset 1px; child paint a.pNqdxq_socialLink.pNqdxq_xLink: outline 1px auto rgb(16, 16, 16) offset 1px |
| pressed | background transparent; text Verlag 18/24 400, #ed9d5d; icon 16 x 16, #ed9d5d |

![Social link default](components/crops/footer-social-default.png) ![Social link hover](components/crops/footer-social-hover.png) ![Social link focus-visible](components/crops/footer-social-focus-visible.png) ![Social link pressed](components/crops/footer-social-pressed.png)

### Mobile (390 wide)

The same surface at phone width: the fixed bar pieces and the slide-in drawer.

#### Menu button
The 44x32 hamburger at the bar edge (an icon div, no label); its own press slides the nav drawer in. Read as `m-menu-button` on the home page at 390 wide.

**Values (default).** size 44 x 32; radius 8px; background rgba(255, 255, 255, 0.06) `color.white-alpha.6`; image linear-gradient(179deg, rgba(255, 255, 255, 0.1) 7%, rgba(255, 255, 255, 0) 92%); shadow rgba(0, 0, 0, 0.08) 0px 2px 4px -2px, rgba(0, 0, 0, 0.03) 0px 8px 16px -8px, rgba(255, 255, 255, 0.1) 0px -2px 3px 0px inset, rgba(255, 255, 255, 0.06) 0px -4px 12px 0px inset; text Verlag 18/27 400, rgba(255, 255, 255, 0.7) `color.white-alpha.70`; icon 44 x 26, rgba(255, 255, 255, 0.7) `color.white-alpha.70`.

![Menu button default](components/crops/m-menu-button-default.png)

#### Mobile menu, open
The nav drawer after the hamburger press (fixed, 374x762; it is transparent and translated -187px off-canvas while closed). Read as `m-menu-open` on the home page at 390 wide.

**Values (default).** size 374 x 762; radius 12px; background transparent; text Verlag 12/12 700, #ffffff `color.paper.100`; transform translate(-187px, 0px); icon 40 x 40, #ffffff `color.paper.100`.

Child layers that carry the look: ul 374x549.9 background rgba(31, 31, 30, 0.06) `measured.drawer-fill` image linear-gradient(rgba(31, 31, 30, 0.8) 2%, rgba(31, 31, 30, 0) 100%) radius 12px; li 342x282.9 border 1px solid rgba(255, 255, 255, 0.06) `color.white-alpha.6`; a 171x174.9 background rgba(255, 255, 255, 0.12) border 1px solid rgba(255, 255, 255, 0.06) `color.white-alpha.6` radius 12px.

![Mobile menu, open default](components/crops/m-menu-open-default.png)

#### Menu link
A link row inside the open mobile drawer. Read as `m-menu-link` on the home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 171 x 14; background transparent; text Verlag 14/14 700, #ffffff `color.paper.100`; transition color 0.1s ease-in-out |
| hover, pressed | text Verlag 14/14 700, #fb7232 `color.orange.500` |

![Menu link default](components/crops/m-menu-link-default.png) ![Menu link hover](components/crops/m-menu-link-hover.png) ![Menu link focus-visible](components/crops/m-menu-link-focus-visible.png) ![Menu link pressed](components/crops/m-menu-link-pressed.png)

#### Mobile headline
The hero headline at 390 — the final word rotates (organized / searchable / up to date). Read as `m-hero` on the home page at 390 wide.

**Values (default).** size 332 x 96; background transparent; text VerlagCondensed 48/48 700, #fefef7 `color.cream.0`.

![Mobile headline default](components/crops/m-hero-default.png)

#### Mobile CTA
The fixed "Get Started" pill in the mobile bar; links to /start, never followed. Read as `m-cta` on the home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 123 x 32.03; background transparent; text Verlag 12/12 600, #1f1f1e `color.ink.750` |
| pressed | child paint a.y0DxmG_signInBtn: size 0.0x0.0; background rgba(255, 255, 255, 0.08) `color.white-alpha.8`; radius 8px |

Child layers that carry the look: div 123x32 background #ffffff `color.paper.100` radius 8px; div::after calc(100% + 36px)xcalc(100% + 12px) image linear-gradient(225deg, #32c5ff 0%, #b620e0 51%, #f7b500 100%) radius 100%; div::before calc(100% + 36px)xcalc(100% + 12px) image linear-gradient(225deg, #32c5ff 0%, #b620e0 51%, #f7b500 100%).

![Mobile CTA default](components/crops/m-cta-default.png) ![Mobile CTA hover](components/crops/m-cta-hover.png) ![Mobile CTA pressed](components/crops/m-cta-pressed.png)

## Icons

No standalone SVG icon set was lifted on this pass; the icons in the crops and screenshots are Mesh's artwork. Declared under layoutGaps in the catalog entry.

| Icon | Rendered sizes | View box | Style | Seen on | Next to |
|---|---|---|---|---|---|

## Gaps

### Pages

- **The product itself.** Mesh's app — the network, contacts and settings — lives behind app.me.sh sign-in; the sign-in card was measured but never submitted. /start's download links and the paid plan checkouts were never followed.
- **library.me.sh.** The documentation host (where /terms and /privacy redirect) sits behind a 'Confirm you are human' verification gate — it was not captured.
- **/press/kit** redirects to a public Notion page (clayearth.notion.site) — an external surface, not captured.
- **clay.earth** 301s to me.sh. The capture is entirely of the Mesh site; the redirect is provenance, recorded in the catalog.

### States

- **Pressed** was forced with DevTools on every control, so a state a script adds on mousedown (if any) is missing.
- **Disabled, error and loading states** were not seen on the public surface.

### Themes

Two page themes exist on different routes, not a toggle: / and the dark routes paint black; /pricing and the app.me.sh sign-in card paint warm light surfaces. tokens.json carries both sets (`dark`, `light`).

### Fonts

- **The UI fonts** are webfonts the site declares (9 @font-face entries — Verlag, VerlagCondensed, ChronicleTextG1Roman, ChronicleCondensed; `fonts` in [raw/css-vars.json](raw/css-vars.json)); the font files themselves are not committed. SF Pro Text on the sign-in card is a system font.
- Photography, testimonial imagery and wordmark artwork in the screenshots are Mesh's property.

### Screenshots

- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files.

### Content left out

- The photography, testimonial avatars, integration logos and the wordmark are Mesh's content; only the frames and components were measured.
