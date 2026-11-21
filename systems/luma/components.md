# Luma components

The discovery list of every page and view captured, then one entry per component with crops of the real product, and the Gaps. Captured from luma.com on 2026-11-21, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running page. Marketing pages paint html.theme-root.light. The public event page paints html.theme-root.dark on its own. Nothing was signed into, registered or submitted. Follow, Create, Get Luma Plus and the sign-in actions were measured and never followed.

The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) (36 components, 91 states). The page layouts are described in [patterns.md](patterns.md).

How to read an entry:

- A colour is its value followed by the palette token in [tokens.json](tokens.json) with the same value, when there is one. Text is written family size/line-height weight, then its colour, for example `SF Pro 14/21 500, #21252e`, and is read from the first text node inside the component.
- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example "default (same: focus-visible)". When the root paints nothing, "Child layers" names the first nodes inside it that do.
- Crops are images of the component read from the live page, in [components/crops/](components/crops) (91 files, named `{component}-{state}.png`, at 2x). Screenshots are in [screenshots/](screenshots).

## Discovery list

Screenshots are named `{page}-{theme}-state.png`. Marketing pages paint `light`. The public event page paints `dark` on its own. Desktop shots are 1440 x 900 at 1x; `-full` shots are whole pages at 1x; mobile shots are `mobile-{page}-{theme}-{state}.png`, 780 wide (390 at 2x). `pricing-light-monthly` is the Monthly segment toggled locally.

| Surface | URL | Screenshots |
|---|---|---|
| Home | `https://luma.com/` | [city-menu](screenshots/home-light-city-menu.png), [default](screenshots/home-light-default.png), [full](screenshots/home-light-full.png) |
| Pricing | `https://luma.com/pricing` | [default](screenshots/pricing-light-default.png), [full](screenshots/pricing-light-full.png), [monthly](screenshots/pricing-light-monthly.png) |
| Discover | `https://luma.com/discover` | [default](screenshots/discover-light-default.png), [full](screenshots/discover-light-full.png) |
| Public event | `https://luma.com/july4-brooklyn` | [default](screenshots/event-dark-default.png), [full](screenshots/event-dark-full.png) |
| Sign in | `https://luma.com/signin` | [default](screenshots/signin-light-default.png) |
| Home, phone | `https://luma.com/` | [default](screenshots/mobile-home-light-default.png), [full](screenshots/mobile-home-light-full.png) |
| Public event, phone | `https://luma.com/july4-brooklyn` |  |
| Sign in, phone | `https://luma.com/signin` | [default](screenshots/mobile-signin-light-default.png) |

### Overlays and transient states

| State | Where | How it was reached | Captured |
|---|---|---|---|
| Monthly billing segment | /pricing | the Monthly segment's own toggle; Annual is selected at rest | [pricing-light-monthly](screenshots/pricing-light-monthly.png), [billing-monthly](#monthly-segment) |
| Consent overlays | every page | hidden in CSS if present, never answered (no consent button was ever clicked, no consent POST sent) | none painted on these pages |
| Sign-in dialog on /create | /create | not opened; the landing Create pill links there and was never followed | gap; see Gaps |
| Host dashboard, guest list, checkout | behind sign-in | never reached | boundary; see Gaps |

## Shared values

Values that apply across entries, from the measurement files.

**Focus.** 17 components were given a real keyboard focus. 17 draw an outline ring: `nav-discover` (2px solid rgba(255, 255, 255, 0.5), offset 4px), `nav-signin` (2px solid rgba(21, 21, 21, 0.64), offset 2px), `cta-create` (1px auto #005fcc, offset 1px), `cta-discover` (2px solid #959595 `color.gray.60`, offset 6px), `billing-monthly` (on a child: 2px solid rgb(21, 21, 21) offset 0px), `billing-annual` (on a child: 2px solid rgb(21, 21, 21) offset 0px), `plan-cta` (2px solid #353535 `color.gray.90`, offset 2px), `plan-cta-brand` (2px solid #f31a7c `color.status.brand`, offset 2px), `follow-button` (2px solid rgba(21, 21, 21, 0.64), offset 2px), `event-signin` (2px solid rgba(255, 255, 255, 0.64), offset 2px), `host-follow` (2px solid rgba(255, 255, 255, 0.64), offset 2px), `phone-toggle` (2px solid #959595 `color.gray.60`, offset 6px), `continue-btn` (2px solid #353535 `color.gray.90`, offset 2px), `google-btn` (2px solid rgba(21, 21, 21, 0.64), offset 2px), `passkey-btn` (2px solid rgba(21, 21, 21, 0.64), offset 2px), `footer-link` (1px auto #005fcc, offset 1px), `m-signin` (2px solid rgba(21, 21, 21, 0.64), offset 2px).

**Pressed.** Forced with DevTools (`CSS.forcePseudoState` :active:hover). Nothing a real press would submit was ever pressed.

**Motion.** Transitions measured on the components, by duration.

| Duration | Easing | Property | Where |
|---|---|---|---|
| 0.2s | `cubic-bezier(0.4, 0, 0.2, 1)` | color | cta-discover |
| 0.3s | `cubic-bezier(0.4, 0, 0.2, 1)` | all, border-color, box-shadow | billing-annual, billing-monthly, category-card, continue-btn, cta-create, email-field, event-card, event-meta and more |

**Card shapes.** Default-state values; the entries hold the states.

| Card | Size | Border | Radius | Background | Shadow | Padding |
|---|---|---|---|---|---|---|
| [Event row](#event-row) | 146.66 x 225.27 | - | - | transparent | none | 0 |
| [Free plan card](#free-plan-card) | 448 x 845 | 1px solid #ffffff `color.white` | 24px | rgba(255, 255, 255, 0.8) | rgba(0, 0, 0, 0.01) 0px 0.7px 2.7px 0px, rgba(0, 0, 0, 0.016) 0px 1.7px 6.9px 0px, rgba(0, 0, 0, 0.02) 0px 3.5px 14.2px 0px, rgba(0, 0, 0, 0.024) 0px 7.3px 29.2px 0px | 18px 20px |
| [Plus plan card](#plus-plan-card) | 448 x 845 | 1px solid #ffffff `color.white` | 24px | rgba(255, 255, 255, 0.8) | rgba(0, 0, 0, 0.01) 0px 0.7px 2.7px 0px, rgba(0, 0, 0, 0.016) 0px 1.7px 6.9px 0px, rgba(0, 0, 0, 0.02) 0px 3.5px 14.2px 0px, rgba(0, 0, 0, 0.024) 0px 7.3px 29.2px 0px | 18px 20px |
| [Category card](#category-card) | 252 x 66 | 1px solid #ffffff `color.white` | 24px | rgba(255, 255, 255, 0.8) | none | 8px 16px 8px 4px |
| [Host card](#host-card) | 330 x 125.59 | - | - | transparent | none | 0 |

## Components

### Shell and navigation

The marketing landing header on the white field: a four-point spark and the light Sign In pill. The wordmark and Discover Events live on inner pages and are listed with the public event.

#### Landing header
The marketing landing header: a spark mark and the Sign In pill. Inner pages add the wordmark and Discover Events. Read as `header` on the home page.

**Values (default).** size 1440 x 58; padding 14px 18px; background transparent; text -apple-system 14/14 500, rgba(21, 21, 21, 0.64); icon 20 x 20, rgba(21, 21, 21, 0.36); layers a.btn.lux-button 67.0x30.0 rgba(21, 21, 21, 0.04) T:1px solid rgba(0, 0, 0, 0) / R:1px solid rgba(0, 0, 0, 0) / B:1px solid rgba(0, 0, 0, 0) / L:1px solid rgba(0, 0, 0, 0) 2px solid rgba(0, 0, 0, 0) offset 2px 15px.

Child layers that carry the look: a 67x30 background rgba(21, 21, 21, 0.04) border 1px solid transparent radius 15px.

![Landing header default](components/crops/header-default.png)

#### Sign In pill
The landing Sign In pill (light, round). It links to /signin; measured, never followed. Read as `nav-signin` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 66.95 x 30; padding 7px 10px; border 1px solid transparent; radius 15px; background rgba(21, 21, 21, 0.04); outline 2px solid transparent, offset 2px; text -apple-system 14/14 500, rgba(21, 21, 21, 0.64); transition all 0.3s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | border 1px solid rgba(21, 21, 21, 0); background rgba(21, 21, 21, 0.64); text -apple-system 14/14 500, #ffffff `color.white` |
| focus-visible | outline 2px solid rgba(21, 21, 21, 0.64), offset 2px |
| pressed | border 1px solid rgba(21, 21, 21, 0); background rgba(21, 21, 21, 0.64); text -apple-system 14/14 500, #ffffff `color.white` |

![Sign In pill default](components/crops/nav-signin-default.png) ![Sign In pill hover](components/crops/nav-signin-hover.png) ![Sign In pill focus-visible](components/crops/nav-signin-focus-visible.png) ![Sign In pill pressed](components/crops/nav-signin-pressed.png)

#### Spark mark
The four-point spark in the landing header. It is not a link. Read as `spark` on the home page.

**Values (default).** size 20 x 20; background transparent; text -apple-system 16/24 400, rgba(21, 21, 21, 0.36); icon 20 x 20, rgba(21, 21, 21, 0.36).

![Spark mark default](components/crops/spark-default.png)

### Home hero

The 80px system-stack landing title and the two acquisition actions: a black Create Your First Event pill and a text Discover Events link.

#### Hero title
The 80px landing title, "Delightful events start here". A second painted copy ("Stellar") sits in a dark island and is not this atom. Read as `hero-title` on the home page.

**Values (default).** size 365.25 x 273.94; background transparent; text -apple-system 80/73.6 500, #151515 `color.ink`; icon 80 x 29.16, rgba(21, 21, 21, 0.36); layers span.gradient-text 343.5x118.0.

Child layers that carry the look: span 343.5x118 image radial-gradient(circle at 0.15em 0.15em, #ab46dd 0%, #f31a7c `color.status.brand` 36%, #f8.

![Hero title default](components/crops/hero-title-default.png)

#### Hero lede
The sentence under the landing title. Read as `hero-lede` on the home page.

**Values (default).** size 450 x 60; background transparent; text -apple-system 20/30 400, rgba(21, 21, 21, 0.36).

![Hero lede default](components/crops/hero-lede-default.png)

#### Create event button
The black Create Your First Event pill. It links to /create, which opens a sign-in dialog; measured, never followed. Read as `cta-create` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 223.78 x 45; padding 10px 16px; border 2px solid transparent; radius 100px; background #151515 `color.ink`; shadow rgba(0, 0, 0, 0.03) 0px 3px 3px 0px, rgba(0, 0, 0, 0.04) 0px 8px 7px 0px, rgba(0, 0, 0, 0.05) 0px 17px 14px 0px, rgba(0, 0, 0, 0.06) 0px 35px 29px 0px, rgba(0, 0, 0, 0.07) 0px 96px 80px 0px; text -apple-system 18/27 500, #ffffff `color.white`; transition all 0.3s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | border 2px solid rgba(255, 255, 255, 0.16); background rgba(255, 255, 255, 0.16); shadow none |
| focus-visible | outline 1px auto #005fcc, offset 1px |
| pressed | border 2px solid rgba(255, 255, 255, 0.16); background rgba(255, 255, 255, 0.16); shadow none |

![Create event button default](components/crops/cta-create-default.png) ![Create event button hover](components/crops/cta-create-hover.png) ![Create event button focus-visible](components/crops/cta-create-focus-visible.png) ![Create event button pressed](components/crops/cta-create-pressed.png)

#### Discover Events button
The secondary Discover Events action under the hero. Read as `cta-discover` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 141.02 x 16; background transparent; outline 2px solid transparent, offset 6px; text -apple-system 16/16 500, rgba(21, 21, 21, 0.36); transition color 0.2s cubic-bezier(0.4, 0, 0.2, 1); icon 14.53 x 14.53, rgba(21, 21, 21, 0.36); layers a.btn.lux-button 141.0x16.0 2px solid rgba(0, 0, 0, 0) offset 6px |
| hover | text -apple-system 16/16 500, rgba(21, 21, 21, 0.64); icon 14.53 x 14.53, rgba(21, 21, 21, 0.64) |
| focus-visible | outline 2px solid #959595 `color.gray.60`, offset 6px; layers a.btn.lux-button 141.0x16.0 2px solid rgb(149, 149, 149) offset 6px |
| pressed | text -apple-system 16/16 500, rgba(21, 21, 21, 0.64); icon 14.53 x 14.53, rgba(21, 21, 21, 0.64) |

Child layers that carry the look: a 141x16.

![Discover Events button default](components/crops/cta-discover-default.png) ![Discover Events button hover](components/crops/cta-discover-hover.png) ![Discover Events button focus-visible](components/crops/cta-discover-focus-visible.png) ![Discover Events button pressed](components/crops/cta-discover-pressed.png)

### Home

A public event card on the landing page. The card links to an event; it was measured, never followed into a registration.

#### Event row
A popular-events row on the home page. The row was measured, never opened. Read as `event-card` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 146.66 x 225.27; background transparent; text -apple-system 16/20.8 500, #151515 `color.ink`; transition all 0.3s cubic-bezier(0.4, 0, 0.2, 1); layers div.jsx-1092221a26d8459c.cover 146.7x146.7 rgba(21, 21, 21, 0.04) 24px; div.jsx-bf40f23d3e10e809.img-aspect-ratio 146.7x146.7 rgba(21, 21, 21, 0.04) 16px |
| hover | text -apple-system 16/20.8 500, #6f802b; layers div.jsx-1092221a26d8459c.cover 150.3x150.3 rgba(21, 21, 21, 0.04) 24px; div.jsx-bf40f23d3e10e809.img-aspect-ratio 150.3x150.3 rgba(21, 21, 21, 0.04) 16px |

Child layers that carry the look: div 146.7x146.7 background rgba(21, 21, 21, 0.04) radius 24px; div 146.7x146.7 background rgba(21, 21, 21, 0.04) radius 16px.

![Event row default](components/crops/event-card-default.png) ![Event row hover](components/crops/event-card-hover.png)

### Pricing

The pricing surface: a 60px title, Monthly and Annual segments, white plan cards, a dark Get Started pill and a pink Get Luma Plus pill.

#### Pricing title
The 60px Pricing heading. Read as `pricing-title` on the pricing page.

**Values (default).** size 186.36 x 72; background transparent; text -apple-system 60/72 600, #151515 `color.ink`.

![Pricing title default](components/crops/pricing-title-default.png)

#### Monthly segment
The Monthly half of the billing segment. Toggled as local UI; nothing was purchased. Read as `billing-monthly` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 86.13 x 34; padding 4px 12px; border 1px solid transparent; background transparent; text -apple-system 16/24 500, rgba(21, 21, 21, 0.36); transition all 0.3s cubic-bezier(0.4, 0, 0.2, 1); layers ::after rgba(0, 0, 0, 0) 0px none 1 |
| hover, pressed | text -apple-system 16/24 500, #151515 `color.ink` |

![Monthly segment default](components/crops/billing-monthly-default.png) ![Monthly segment hover](components/crops/billing-monthly-hover.png) ![Monthly segment focus-visible](components/crops/billing-monthly-focus-visible.png) ![Monthly segment pressed](components/crops/billing-monthly-pressed.png)

#### Annual segment
The Annual half of the billing segment, selected at rest on this load. Read as `billing-annual` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, focus-visible, pressed) | size 86.13 x 34; padding 4px 12px; border 1px solid transparent; background transparent; text -apple-system 16/24 500, #151515 `color.ink`; transition all 0.3s cubic-bezier(0.4, 0, 0.2, 1); layers ::before rgba(0, 0, 0, 0) 0px none 0; ::after rgba(0, 0, 0, 0) 0px none 1 |

![Annual segment default](components/crops/billing-annual-default.png) ![Annual segment hover](components/crops/billing-annual-hover.png) ![Annual segment focus-visible](components/crops/billing-annual-focus-visible.png) ![Annual segment pressed](components/crops/billing-annual-pressed.png)

#### Free plan card
The free plan card: 24px radius, white surface. Read as `plan-card` on the pricing page.

**Values (default).** size 448 x 845; padding 18px 20px; border 1px solid #ffffff `color.white`; radius 24px; background rgba(255, 255, 255, 0.8); shadow rgba(0, 0, 0, 0.01) 0px 0.7px 2.7px 0px, rgba(0, 0, 0, 0.016) 0px 1.7px 6.9px 0px, rgba(0, 0, 0, 0.02) 0px 3.5px 14.2px 0px, rgba(0, 0, 0, 0.024) 0px 7.3px 29.2px 0px; text -apple-system 18/27 600, #151515 `color.ink`; icon 16 x 16, #151515 `color.ink`.

![Free plan card default](components/crops/plan-card-default.png)

#### Plus plan card
The Luma Plus plan card. Get Luma Plus was measured, never followed (it is a sign-in checkout). Read as `plan-card-plus` on the pricing page.

**Values (default).** size 448 x 845; padding 18px 20px; border 1px solid #ffffff `color.white`; radius 24px; background rgba(255, 255, 255, 0.8); shadow rgba(0, 0, 0, 0.01) 0px 0.7px 2.7px 0px, rgba(0, 0, 0, 0.016) 0px 1.7px 6.9px 0px, rgba(0, 0, 0, 0.02) 0px 3.5px 14.2px 0px, rgba(0, 0, 0, 0.024) 0px 7.3px 29.2px 0px; text -apple-system 18/27 600, #f31a7c `color.status.brand`; icon 16 x 16, #151515 `color.ink`.

![Plus plan card default](components/crops/plan-card-plus-default.png)

#### Get Started button
The primary plan button (near-black fill, 16px radius). It links to sign-in; measured, never followed. Read as `plan-cta` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 406 x 38; padding 10px 14px; border 1px solid #353535 `color.gray.90`; radius 16px; background #353535 `color.gray.90`; outline 2px solid transparent, offset 2px; text -apple-system 16/16 500, #ffffff `color.white`; transition all 0.3s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | border 1px solid #555555 `color.gray.80`; background #555555 `color.gray.80` |
| focus-visible | outline 2px solid #353535 `color.gray.90`, offset 2px |
| pressed | border 1px solid #555555 `color.gray.80`; background #555555 `color.gray.80` |

![Get Started button default](components/crops/plan-cta-default.png) ![Get Started button hover](components/crops/plan-cta-hover.png) ![Get Started button focus-visible](components/crops/plan-cta-focus-visible.png) ![Get Started button pressed](components/crops/plan-cta-pressed.png)

#### Get Luma Plus button
The brand button (#f31a7c, 16px radius). It links to calendar checkout; measured, never followed. Read as `plan-cta-brand` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 406 x 38; padding 10px 14px; border 1px solid #f31a7c `color.status.brand`; radius 16px; background #f31a7c `color.status.brand`; outline 2px solid transparent, offset 2px; text -apple-system 16/16 500, #ffffff `color.white`; transition all 0.3s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | border 1px solid #d5176d `color.status.brand-active`; background #d5176d `color.status.brand-active` |
| focus-visible | outline 2px solid #f31a7c `color.status.brand`, offset 2px |
| pressed | border 1px solid #d5176d `color.status.brand-active`; background #d5176d `color.status.brand-active` |

![Get Luma Plus button default](components/crops/plan-cta-brand-default.png) ![Get Luma Plus button hover](components/crops/plan-cta-brand-hover.png) ![Get Luma Plus button focus-visible](components/crops/plan-cta-brand-focus-visible.png) ![Get Luma Plus button pressed](components/crops/plan-cta-brand-pressed.png)

### Discover

The public Discover directory: a title, category cards and event rows with a Follow pill that was measured and never pressed.

#### Discover title
The Discover Events heading. Read as `discover-title` on the discover page.

**Values (default).** size 788 x 33.59; background transparent; text -apple-system 28/33.6 600, #151515 `color.ink`.

![Discover title default](components/crops/discover-title-default.png)

#### Category card
A browse-by-category card (Family, Books, …). Measured, never followed. Read as `category-card` on the discover page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 252 x 66; padding 8px 16px 8px 4px; border 1px solid #ffffff `color.white`; radius 24px; background rgba(255, 255, 255, 0.8); text -apple-system 16/24 500, #151515 `color.ink`; transition border-color 0.3s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.3s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | border 1px solid rgba(21, 21, 21, 0.16); shadow rgba(0, 0, 0, 0.004) 0px 28px 17px 0px, rgba(0, 0, 0, 0.01) 0px 12px 12px 0px, rgba(0, 0, 0, 0.01) 0px 3px 7px 0px, rgba(0, 0, 0, 0.01) 0px 0px 0px 0px |

![Category card default](components/crops/category-card-default.png) ![Category card hover](components/crops/category-card-hover.png)

#### Follow button
A calendar Follow button. Measured, never pressed (pressing asks for sign-in). Read as `follow-button` on the discover page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 64.42 x 30; padding 7px 10px; border 1px solid transparent; radius 15px; background rgba(21, 21, 21, 0.04); outline 2px solid transparent, offset 2px; text -apple-system 14/14 500, rgba(21, 21, 21, 0.64); transition all 0.3s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | border 1px solid rgba(21, 21, 21, 0); background rgba(21, 21, 21, 0.64); text -apple-system 14/14 500, #ffffff `color.white` |
| focus-visible | outline 2px solid rgba(21, 21, 21, 0.64), offset 2px |
| pressed | border 1px solid rgba(21, 21, 21, 0); background rgba(21, 21, 21, 0.64); text -apple-system 14/14 500, #ffffff `color.white` |

![Follow button default](components/crops/follow-button-default.png) ![Follow button hover](components/crops/follow-button-hover.png) ![Follow button focus-visible](components/crops/follow-button-focus-visible.png) ![Follow button pressed](components/crops/follow-button-pressed.png)

### Public event

One public event page, which paints theme-root.dark on its own: wordmark, Discover Events, a Sign In button, the Google Sans Flex title, a host card and the location row.

#### Discover link
The Discover Events link in the inner-page header. Measured, never followed. Read as `nav-discover` on the public event page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 105.52 x 17; radius 100px; background transparent; text -apple-system 14/21 500, rgba(255, 255, 255, 0.5); transition all 0.3s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | text -apple-system 14/21 500, #ffffff `color.white` |
| focus-visible | outline 2px solid rgba(255, 255, 255, 0.5), offset 4px; layers a.min-width-0.text-ellipses 105.5x17.0 2px solid rgba(255, 255, 255, 0.5) offset 4px 100px |
| pressed | text -apple-system 14/21 500, #ffffff `color.white` |

![Discover link default](components/crops/nav-discover-default.png) ![Discover link hover](components/crops/nav-discover-hover.png) ![Discover link focus-visible](components/crops/nav-discover-focus-visible.png) ![Discover link pressed](components/crops/nav-discover-pressed.png)

#### Event title
The event page title. The page paints theme-root.dark on its own. Read as `event-title` on the public event page.

**Values (default).** size 566 x 87.38; background transparent; text Google Sans Flex 38/43.7 575, #ffffff `color.white`.

![Event title default](components/crops/event-title-default.png)

#### Event Sign In
The header Sign In control on the dark event page. Measured, never pressed. Read as `event-signin` on the public event page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 66.95 x 30; padding 7px 10px; border 1px solid transparent; radius 15px; background rgba(255, 255, 255, 0.08); outline 2px solid transparent, offset 2px; text -apple-system 14/14 500, rgba(255, 255, 255, 0.64); transition all 0.3s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | border 1px solid rgba(255, 255, 255, 0); background rgba(255, 255, 255, 0.64); text -apple-system 14/14 500, #151515 `color.ink` |
| focus-visible | outline 2px solid rgba(255, 255, 255, 0.64), offset 2px |
| pressed | border 1px solid rgba(255, 255, 255, 0); background rgba(255, 255, 255, 0.64); text -apple-system 14/14 500, #151515 `color.ink` |

![Event Sign In default](components/crops/event-signin-default.png) ![Event Sign In hover](components/crops/event-signin-hover.png) ![Event Sign In focus-visible](components/crops/event-signin-focus-visible.png) ![Event Sign In pressed](components/crops/event-signin-pressed.png)

#### Host card
The presented-by host block beside the event title. Read as `host-card` on the public event page.

**Values (default).** size 330 x 125.59; background transparent; text -apple-system 12/15.6 400, rgba(255, 255, 255, 0.79); icon 16 x 16, rgba(255, 255, 255, 0.5); layers img.square.rounded 32.0x32.0 T:1px solid rgba(255, 255, 255, 0.08) / R:1px solid rgba(255, 255, 255, 0.08) / B:1px solid rgba(255, 255, 255, 0.08) / L:1px solid rgba(255, 255, 255, 0.08) 8px; button.btn.lux-button 64.4x30.0 rgba(255, 255, 255, 0.08) T:1px solid rgba(0, 0, 0, 0) / R:1px solid rgba(0, 0, 0, 0) / B:1px solid rgba(0, 0, 0, 0) / L:1px solid rgba(0, 0, 0, 0) 2px solid rgba(0, 0, 0, 0) o.

Child layers that carry the look: img 32x32 border 1px solid rgba(255, 255, 255, 0.08) radius 8px; button 64.4x30 background rgba(255, 255, 255, 0.08) border 1px solid transparent radius 15px.

![Host card default](components/crops/host-card-default.png)

#### Host Follow
The host Follow button. Measured, never pressed (it asks for sign-in). Read as `host-follow` on the public event page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 64.42 x 30; padding 7px 10px; border 1px solid transparent; radius 15px; background rgba(255, 255, 255, 0.08); outline 2px solid transparent, offset 2px; text -apple-system 14/14 500, rgba(255, 255, 255, 0.64); transition all 0.3s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | border 1px solid rgba(255, 255, 255, 0); background rgba(255, 255, 255, 0.64); text -apple-system 14/14 500, #011036 |
| focus-visible | outline 2px solid rgba(255, 255, 255, 0.64), offset 2px |
| pressed | border 1px solid rgba(255, 255, 255, 0); background rgba(255, 255, 255, 0.64); text -apple-system 14/14 500, #011036 |

![Host Follow default](components/crops/host-follow-default.png) ![Host Follow hover](components/crops/host-follow-hover.png) ![Host Follow focus-visible](components/crops/host-follow-focus-visible.png) ![Host Follow pressed](components/crops/host-follow-pressed.png)

#### Location row
The place row. It links out to a map; measured, never followed. Read as `event-meta` on the public event page.

**Values (default).** size 233.31 x 46; background transparent; text Google Sans Flex 16/24 475, #ffffff `color.white`; transition all 0.3s cubic-bezier(0.4, 0, 0.2, 1); icon 20 x 20, rgba(255, 255, 255, 0.79); layers div.jsx-100837539.icon-container 40.0x40.0 T:1px solid rgba(255, 255, 255, 0.08) / R:1px solid rgba(255, 255, 255, 0.08) / B:1px solid rgba(255, 255, 255, 0.08) / L:1px solid rgba(255, 255, 255, 0.08) 8px.

Child layers that carry the look: div 40x40 border 1px solid rgba(255, 255, 255, 0.08) radius 8px.

![Location row default](components/crops/event-meta-default.png)

#### Wordmark
The luma wordmark on an inner page. It links home; measured, never followed. Read as `wordmark` on the public event page.

**Values (default).** size 43.88 x 28; radius 8px; background transparent; text -apple-system 16/24 400, #f98dbe; transition all 0.3s cubic-bezier(0.4, 0, 0.2, 1); icon 43.88 x 16, rgba(255, 255, 255, 0.5).

![Wordmark default](components/crops/wordmark-default.png)

### Sign in

The sign-in card, measured and never submitted: title, email field, phone toggle, Continue with Email, Google and Passkey.

#### Sign-in title
The Welcome to Luma heading on the sign-in card. Nothing was submitted. Read as `signin-title` on the sign in page.

**Values (default).** size 320 x 24; background transparent; text -apple-system 20/24 600, #151515 `color.ink`.

![Sign-in title default](components/crops/signin-title-default.png)

#### Email field
The email input (8px radius). Sample text was typed and deleted. Continue was never pressed. Read as `email-field` on the sign in page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 320 x 38; padding 10px 14px; border 1px solid rgba(21, 21, 21, 0.08); radius 8px; background #ffffff `color.white`; image -webkit-linear-gradient(top, rgba(255, 255, 255, 0), rgba(255, 255, 255, 0)); text -apple-system 16/16 400, #151515 `color.ink`; transition all 0.3s cubic-bezier(0.4, 0, 0.2, 1); placeholder rgba(21, 21, 21, 0.32) |
| focused, filled | border 1px solid #151515 `color.ink` |

![Email field default](components/crops/email-field-default.png) ![Email field focused](components/crops/email-field-focused.png) ![Email field filled](components/crops/email-field-filled.png)

#### Use Phone Number
The link-styled toggle that swaps the email field for a phone field. Measured, never pressed. Read as `phone-toggle` on the sign in page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 146.34 x 14; background transparent; outline 2px solid transparent, offset 6px; text -apple-system 14/14 500, rgba(21, 21, 21, 0.36); transition all 0.3s cubic-bezier(0.4, 0, 0.2, 1); icon 12.72 x 12.72, rgba(21, 21, 21, 0.36); layers button.btn.lux-button 146.3x14.0 2px solid rgba(0, 0, 0, 0) offset 6px |
| hover | text -apple-system 14/14 500, rgba(21, 21, 21, 0.64); icon 12.72 x 12.72, rgba(21, 21, 21, 0.64) |
| focus-visible | outline 2px solid #959595 `color.gray.60`, offset 6px; layers button.btn.lux-button 146.3x14.0 2px solid rgb(149, 149, 149) offset 6px |
| pressed | text -apple-system 14/14 500, rgba(21, 21, 21, 0.64); icon 12.72 x 12.72, rgba(21, 21, 21, 0.64) |

Child layers that carry the look: button 146.3x14.

![Use Phone Number default](components/crops/phone-toggle-default.png) ![Use Phone Number hover](components/crops/phone-toggle-hover.png) ![Use Phone Number focus-visible](components/crops/phone-toggle-focus-visible.png) ![Use Phone Number pressed](components/crops/phone-toggle-pressed.png)

#### Continue with Email
The primary submit. Measured with CDP :active only, so the form was never submitted. Read as `continue-btn` on the sign in page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 320 x 38; padding 10px 14px; border 1px solid #353535 `color.gray.90`; radius 16px; background #353535 `color.gray.90`; outline 2px solid transparent, offset 2px; text -apple-system 16/16 500, #ffffff `color.white`; transition all 0.3s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | border 1px solid #555555 `color.gray.80`; background #555555 `color.gray.80` |
| focus-visible | outline 2px solid #353535 `color.gray.90`, offset 2px |
| pressed | border 1px solid #555555 `color.gray.80`; background #555555 `color.gray.80` |

![Continue with Email default](components/crops/continue-btn-default.png) ![Continue with Email hover](components/crops/continue-btn-hover.png) ![Continue with Email focus-visible](components/crops/continue-btn-focus-visible.png) ![Continue with Email pressed](components/crops/continue-btn-pressed.png)

#### Sign in with Google
The Google button. Measured, never pressed. Read as `google-btn` on the sign in page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 320 x 38; padding 10px 14px; border 1px solid transparent; radius 16px; background rgba(21, 21, 21, 0.04); outline 2px solid transparent, offset 2px; text -apple-system 16/16 500, rgba(21, 21, 21, 0.64); transition all 0.3s cubic-bezier(0.4, 0, 0.2, 1); icon 16 x 16, rgba(21, 21, 21, 0.64) |
| hover | border 1px solid rgba(21, 21, 21, 0); background rgba(21, 21, 21, 0.64); text -apple-system 16/16 500, #ffffff `color.white`; icon 16 x 16, #ffffff `color.white` |
| focus-visible | outline 2px solid rgba(21, 21, 21, 0.64), offset 2px |
| pressed | border 1px solid rgba(21, 21, 21, 0); background rgba(21, 21, 21, 0.64); text -apple-system 16/16 500, #ffffff `color.white`; icon 16 x 16, #ffffff `color.white` |

![Sign in with Google default](components/crops/google-btn-default.png) ![Sign in with Google hover](components/crops/google-btn-hover.png) ![Sign in with Google focus-visible](components/crops/google-btn-focus-visible.png) ![Sign in with Google pressed](components/crops/google-btn-pressed.png)

#### Sign in with Passkey
The passkey button. Measured, never pressed. Read as `passkey-btn` on the sign in page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 320 x 38; padding 10px 14px; border 1px solid transparent; radius 16px; background rgba(21, 21, 21, 0.04); outline 2px solid transparent, offset 2px; text -apple-system 16/16 500, rgba(21, 21, 21, 0.64); transition all 0.3s cubic-bezier(0.4, 0, 0.2, 1); icon 16 x 16, rgba(21, 21, 21, 0.64) |
| hover | border 1px solid rgba(21, 21, 21, 0); background rgba(21, 21, 21, 0.64); text -apple-system 16/16 500, #ffffff `color.white`; icon 16 x 16, #ffffff `color.white` |
| focus-visible | outline 2px solid rgba(21, 21, 21, 0.64), offset 2px |
| pressed | border 1px solid rgba(21, 21, 21, 0); background rgba(21, 21, 21, 0.64); text -apple-system 16/16 500, #ffffff `color.white`; icon 16 x 16, #ffffff `color.white` |

![Sign in with Passkey default](components/crops/passkey-btn-default.png) ![Sign in with Passkey hover](components/crops/passkey-btn-hover.png) ![Sign in with Passkey focus-visible](components/crops/passkey-btn-focus-visible.png) ![Sign in with Passkey pressed](components/crops/passkey-btn-pressed.png)

### Footer

The marketing footer and one of its links.

#### Footer
The page footer: Discover, Pricing, App, Help, Terms, Privacy. Read as `footer` on the home page.

**Values (default).** size 1440 x 185.5; background transparent; text -apple-system 14/21 400, rgba(21, 21, 21, 0.64); icon 43.88 x 16, rgba(21, 21, 21, 0.64); layers div.jsx-1656054359.flex-start 928.0x54.0 T:1px solid rgba(21, 21, 21, 0.08).

Child layers that carry the look: div 928x54 border 1px solid rgba(21, 21, 21, 0.08).

![Footer default](components/crops/footer-default.png)

#### Footer link
A footer text link. Read as `footer-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 60.63 x 37; padding 8px; background transparent; text -apple-system 14/21 400, rgba(21, 21, 21, 0.64); transition all 0.3s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | text -apple-system 14/21 400, #151515 `color.ink` |
| focus-visible | outline 1px auto #005fcc, offset 1px; layers a 60.6x37.0 1px auto rgb(0, 95, 204) offset 1px |
| pressed | text -apple-system 14/21 400, #151515 `color.ink` |

![Footer link default](components/crops/footer-link-default.png) ![Footer link hover](components/crops/footer-link-hover.png) ![Footer link focus-visible](components/crops/footer-link-focus-visible.png) ![Footer link pressed](components/crops/footer-link-pressed.png)

### Mobile (390 wide)

The landing surface at phone width: spark and Sign In, no hamburger, and the stacked hero.

#### Mobile header
The 390px header: wordmark and Sign In. There is no hamburger. Read as `m-header` on the home page at 390 wide.

**Values (default).** size 390 x 58; padding 14px 18px; background transparent; text -apple-system 14/14 500, rgba(21, 21, 21, 0.64); icon 20 x 20, rgba(21, 21, 21, 0.36); layers a.btn.lux-button 67.0x30.0 rgba(21, 21, 21, 0.04) T:1px solid rgba(0, 0, 0, 0) / R:1px solid rgba(0, 0, 0, 0) / B:1px solid rgba(0, 0, 0, 0) / L:1px solid rgba(0, 0, 0, 0) 2px solid rgba(0, 0, 0, 0) offset 2px 15px.

Child layers that carry the look: a 67x30 background rgba(21, 21, 21, 0.04) border 1px solid transparent radius 15px.

![Mobile header default](components/crops/m-header-default.png)

#### Mobile Sign In
The header Sign In pill at 390. Measured, never followed. Read as `m-signin` on the home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 66.95 x 30; padding 7px 10px; border 1px solid transparent; radius 15px; background rgba(21, 21, 21, 0.04); outline 2px solid transparent, offset 2px; text -apple-system 14/14 500, rgba(21, 21, 21, 0.64); transition all 0.3s cubic-bezier(0.4, 0, 0.2, 1) |
| focus-visible | outline 2px solid rgba(21, 21, 21, 0.64), offset 2px |

![Mobile Sign In default](components/crops/m-signin-default.png) ![Mobile Sign In hover](components/crops/m-signin-hover.png) ![Mobile Sign In focus-visible](components/crops/m-signin-focus-visible.png) ![Mobile Sign In pressed](components/crops/m-signin-pressed.png)

#### Mobile headline
The landing title at 390. Read as `m-hero` on the home page at 390 wide.

**Values (default).** size 206.34 x 154.02; background transparent; text -apple-system 40/39.2 500, #151515 `color.ink`; icon 56 x 20.41, rgba(21, 21, 21, 0.36); layers span.gradient-text 175.5x59.0.

Child layers that carry the look: span 175.5x59 image radial-gradient(circle at 0.15em 0.15em, #ab46dd 0%, #f31a7c `color.status.brand` 36%, #f8.

![Mobile headline default](components/crops/m-hero-default.png)

## Icons

No standalone SVG icon set was lifted on this pass. The spark, the luma wordmark and the Google mark are visible in the crops and screenshots. Declared under layoutGaps in the catalog entry.

| Icon | Rendered sizes | View box | Style | Seen on | Next to |
|---|---|---|---|---|---|

## Gaps

### The signed-in product

Luma's host product sits behind sign-in and was not entered on 2026-11-21: the host dashboard, the event editor, the guest list, check-in, blasts, billing and Luma Plus checkout. /create paints a sign-in card over the composer. That card was photographed and not submitted. Registration, ticket purchase and access-code entry were not submitted. Follow was measured and never pressed. Get Luma Plus links to /calendar/manage/plus, which is checkout and was never opened.

### Pages

- **The host workspace.** Dashboard, editor, guest list, check-in, blasts and billing need an account and were never reached.
- **Sign-in.** /signin was captured as a card and never submitted. Continue with Email, Google and Passkey were measured, never pressed.
- **Create.** The landing Create Your First Event pill links to /create. The page paints a composer and a sign-in card. The card was photographed and not submitted.
- **Checkout.** Get Luma Plus links to /calendar/manage/plus?cadence=yearly. That checkout was never opened.
- **Registration.** The public event page has no public tickets. Access-code entry was not submitted. Follow and Contact the Host were not pressed.

### States

- **Pressed** was forced with DevTools (`CSS.forcePseudoState`), so a state a script adds on mousedown is missing. Nothing a real press would submit was ever pressed.
- **Disabled, error and loading states** were not seen on the captured surfaces.
- **Annual** is selected at rest. Monthly was toggled locally for one screenshot and is not a second component state beyond the segment's own hover, focus and press.

### Themes

Marketing pages paint html.theme-root.light. The public event page paints html.theme-root.dark on its own, so the dark set is a live theme, not a reconstruction. There is no theme toggle on the captured pages.

### Fonts

- The UI stack is the system face with Inter in the fallback list. Event titles paint Google Sans Flex, a served woff2 face, via --title-font. Neither face is distributed with this package.

### Screenshots

- Event photography, the spark, the luma wordmark and host names in the screenshots are the product's published content. The event location is a public venue (Brooklyn Bridge Park).
- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files.
- Discover's popular events are localized to the capture egress. Treat those titles as sample content, not a fixed catalog.

### Content left out

- Marketing copy and the public event's description are the product's content; only frames and components were measured.
