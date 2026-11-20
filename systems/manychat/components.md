# ManyChat components

The discovery list of every page and view captured, then one entry per component with crops of the real product, and the Gaps. Captured from manychat.com on 2026-11-18, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running page. Nothing was signed into, submitted or purchased. Product, the billing labels and the FAQ are local toggles. Log in, Get started and Start for free were measured, never followed. The Usercentrics privacy layer was hidden, never answered. app.manychat.com was never entered.

The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) (31 components, 63 states). The page layouts are described in [patterns.md](patterns.md).

How to read an entry:

- A colour is its value followed by the palette token in [tokens.json](tokens.json) with the same value, when there is one. Text is written family size/line-height weight, then its colour, for example `SF Pro 14/21 500, #21252e`, and is read from the first text node inside the component.
- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example "default (same: focus-visible)". When the root paints nothing, "Child layers" names the first nodes inside it that do.
- Crops are images of the component read from the live page, in [components/crops/](components/crops) (60 files, named `{component}-{state}.png`). Desktop crops are 1x; phone crops are 2x. Screenshots are in [screenshots/](screenshots).

## Discovery list

Screenshots are named `{page}-{theme}-state.png`: every page paints `light`. Desktop shots are 1440 x 900 at 1x. `-full` shots are whole pages at CSS scale. Phone viewport shots are 780 wide (2x). The pricing phone pass measured innerWidth 390. The home phone pass measured innerWidth 392 (visualViewport 390). The shipped phone full pages are 390 wide.

| Surface | URL | Screenshots |
|---|---|---|
| Home | `/` | [default](screenshots/home-light-default.png), [full](screenshots/home-light-full.png), [menu](screenshots/home-light-menu.png) |
| Pricing | `/pricing` | [default](screenshots/pricing-light-default.png), [full](screenshots/pricing-light-full.png), [monthly](screenshots/pricing-light-monthly.png) |
| Instagram | `/product/instagram` | [default](screenshots/instagram-light-default.png), [full](screenshots/instagram-light-full.png) |
| How to | `/resources/how-to` | [default](screenshots/how-to-light-default.png), [full](screenshots/how-to-light-full.png) |
| Home, phone | `/` | [default](screenshots/mobile-home-light-default.png), [full](screenshots/mobile-home-light-full.png) |
| Pricing, phone | `/pricing` | [default](screenshots/mobile-pricing-light-default.png), [full](screenshots/mobile-pricing-light-full.png) |

### Overlays and transient states

| State | Where | How it was reached | Captured |
|---|---|---|---|
| Product mega menu | the nav | the Product div clicked locally | [home-light-menu](screenshots/home-light-menu.png) |
| Monthly billing | pricing | the Monthly label clicked locally; checkout was never opened | [pricing-light-monthly](screenshots/pricing-light-monthly.png) |
| Promo strip | home | the Creator World link was measured, never followed | [promo-banner](#promo-banner) |
| Usercentrics consent | every page | the layer was hidden, never answered | boundary; see Gaps |
| Log in / app.manychat.com | the nav | the sign-in link was measured, never followed | boundary; see Gaps |

## Shared values

Values that apply across entries, from the measurement files.

**Focus.** 9 components were given a real keyboard focus. 9 show no measured change: `nav-plain-link`, `nav-login`, `nav-cta`, `hero-cta`, `faq-item`, `footer-link`, `price-cta`, `product-cta`, `m-cta`.

**Pressed.** Forced with DevTools (`CSS.forcePseudoState` :active:hover). Nothing a real press would submit was ever pressed.

**Motion.** Transitions measured on the components, by duration.

| Duration | Easing | Property | Where |
|---|---|---|---|
| 0.3s | `ease` | background, background-size, box-shadow, color, transform | footer-link, hero-cta, howto-card, m-cta, m-logo, nav-cta, nav-locale, nav-login and more |
| 0.45s | `cubic-bezier(0.43, 0.195, 0.02, 1)` | transform | header-nav, m-header, nav-link, nav-plain-link |
| 0.7s | `cubic-bezier(0.43, 0.195, 0.02, 1)` | opacity, transform | section-heading |

**Card shapes.** Default-state values; the entries hold the states.

| Card | Size | Border | Radius | Background | Shadow | Padding |
|---|---|---|---|---|---|---|
| [Price card](#price-card) | 368.53 x 661.53 | - | 24px | #ffffff `light.surface.primary` | none | 32px 32px 40px 32px |
| [FAQ accordion](#faq-accordion) | 841.33 x 62.39 | - | - | transparent | none | 0 |
| [Guide card](#guide-card) | 368 x 372.17 | 1px solid #f5f5f5 `light.background.secondary` | - | transparent | rgba(0, 0, 0, 0.08) 0px 4px 8px 0px | 0 |

## Components

### Shell and navigation

The sticky chrome: a 68px black Creator World strip on home, a 92px white nav (wordmark, Product/Solutions divs, Pricing, EN, Log in, Get started), and the footer.

#### Promo banner
The Creator World 27 strip above the nav. A marketing link; measured, never followed. Read as `promo-banner` on the home page.

**Values (default).** size 1440 x 68; background #0f0f0f `light.text.primary`; text CoFo Sans Mono 14/10 400, #0f0f0f `light.text.primary`; transition color 0.3s ease.

![Promo banner default](components/crops/promo-banner-default.png)

#### Header
The sticky nav: logo, Product/Solutions/Agencies/Pricing/Resources, locale, Log in, Get started. The site paints no <header> element. Read as `header-nav` on the home page.

**Values (default).** size 1440 x 92; background transparent; text CoFo Sans Mono 12/16.32 400, #ffffff `light.surface.primary`; transition transform 0.45s cubic-bezier(0.43, 0.195, 0.02, 1); layers div::before._4Y2iAa_menu 1400pxx900px rgb(237, 242, 237); a.p_y-s.p_x-l 150.0x48.0 rgb(250, 12, 247) 999px; a::before.p_y-s.p_x-l 149.953pxx48px T:1px solid rgba(0, 0, 0, 0) / R:1px solid rgba(0, 0, 0, 0) / B:1px solid rgba(0, 0, 0, 0) / L:1px solid rgba(0, 0, 0, 0) 999px; div.mb-0.4rem.flex 1336.0x48.3 rgb(255, 255, 255) 8px; span._4Y2iAa_underline_item.mc-text-label 51.3x16.3; span._4Y2iAa_under.

Child layers that carry the look: div::before 1400pxx900px background #edf2ed; a 150x48 background #fa0cf7 `core.color.brand.neon-pink` radius 999px; a::before 149.953pxx48px border 1px solid transparent radius 999px.

![Header default](components/crops/header-nav-default.png)

#### Logo
The Manychat wordmark in the nav. Read as `nav-logo` on the home page.

**Values (default).** size 151 x 28; background transparent; text Rooftop 15/19.5 400, #ffffff `light.surface.primary`; transition color 0.3s ease.

![Logo default](components/crops/nav-logo-default.png)

#### Nav item (dropdown)
"Product" is a div, not a button. It opens the channel mega-menu. A local toggle; its links were never followed. Read as `nav-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 51.25 x 18; background transparent; text CoFo Sans Mono 12/18 400, #ffffff `light.surface.primary`; transition transform 0.45s cubic-bezier(0.43, 0.195, 0.02, 1); layers span._4Y2iAa_underline_item 51.3x14.0; ancestors div._4Y2iAa_nav_item._4Y2iAa_underline bg transparent |
| hover, pressed, opened | text CoFo Sans Mono 12/18 400, #000000 |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

Child layers that carry the look: span 51.3x14 image linear-gradient(#ffffff `light.surface.primary`, #ffffff `light.surface.primary`).

![Nav item (dropdown) default](components/crops/nav-link-default.png) ![Nav item (dropdown) hover](components/crops/nav-link-hover.png) ![Nav item (dropdown) pressed](components/crops/nav-link-pressed.png) ![Nav item (dropdown) opened](components/crops/nav-link-opened.png)

#### Nav link
"Pricing" is a plain nav anchor. Measured, never followed from this shot. Read as `nav-plain-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, focus-visible, pressed) | size 51.25 x 18; background transparent; text CoFo Sans Mono 12/18 400, #000000; transition transform 0.45s cubic-bezier(0.43, 0.195, 0.02, 1); layers span._4Y2iAa_underline_item 51.3x14.0; ancestors div._4Y2iAa_nav_item._4Y2iAa_underline bg transparent |

Child layers that carry the look: span 51.3x14 image linear-gradient(#000000, #000000).

![Nav link default](components/crops/nav-plain-link-default.png) ![Nav link hover](components/crops/nav-plain-link-hover.png) ![Nav link focus-visible](components/crops/nav-plain-link-focus-visible.png) ![Nav link pressed](components/crops/nav-plain-link-pressed.png)

#### Locale switch
The EN language switch is a div. Measured; the locale was never changed. Read as `nav-locale` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 14.64 x 16.31; background transparent; image linear-gradient(#000000, #000000); shadow #000000 0px -1px 1px -1px inset, #000000 0px -1px 1px -1px inset; text CoFo Sans Mono 12/16.32 400, #000000; transition background-size 0.3s ease |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

![Locale switch default](components/crops/nav-locale-default.png) ![Locale switch hover](components/crops/nav-locale-hover.png) ![Locale switch pressed](components/crops/nav-locale-pressed.png)

#### Log in link
"Log in" points at app.manychat.com/signin. Measured, never followed. Sign-in boundary. Read as `nav-login` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, focus-visible, pressed) | size 99.92 x 44.31; padding 14px 20px; radius 999px; background transparent; text CoFo Sans Mono 12/16.32 400, #000000 (the element's computed colour; its first label span is a transparent copy); transition background 0.3s ease, transform 0.3s ease; layers ::before rgba(0, 0, 0, 0) 1px none 1; a::before.p_y-s.p_x-l 99.9219pxx44.3125px T:1px solid rgba(0, 0, 0, 0) / R:1px solid rgba(0, 0, 0, 0) / B:1px solid rgba(0, 0, 0, 0) / L:1px solid rgba(0, 0, 0, 0) 999px |

Child layers that carry the look: a::before 99.9219pxx44.3125px border 1px solid transparent radius 999px.

![Log in link default](components/crops/nav-login-default.png) ![Log in link hover](components/crops/nav-login-hover.png) ![Log in link focus-visible](components/crops/nav-login-focus-visible.png) ![Log in link pressed](components/crops/nav-login-pressed.png)

#### Get started pill
The nav "Get started" pill. It opens the sign-up flow. Measured, never followed. Read as `nav-cta` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, focus-visible, pressed) | size 136.53 x 44.31; padding 14px 20px; radius 999px; background #ffffff `light.surface.primary`; text CoFo Sans Mono 12/16.32 400, #ffffff `light.surface.primary` (measured white on a white fill, so the visible label's colour was not read); transition background 0.3s ease, transform 0.3s ease; layers ::before rgba(0, 0, 0, 0) 1px none 1 |

![Get started pill default](components/crops/nav-cta-default.png) ![Get started pill hover](components/crops/nav-cta-hover.png) ![Get started pill focus-visible](components/crops/nav-cta-focus-visible.png) ![Get started pill pressed](components/crops/nav-cta-pressed.png)

#### Mega-menu item
The closed Product menu keeps these links in the DOM at opacity 0. They are not a captured open state. A refresh must wait until a menu link paints before saving them. Read as `menu-item` on the home page.

Not on the page when it was captured.

#### Channel menu item
The closed Product menu keeps these links in the DOM at opacity 0. They are not a captured open state. A refresh must wait until a menu link paints before saving them. Read as `channel-card` on the home page.

Not on the page when it was captured.

#### Footer
The footer band: product, company and legal columns. Read as `footer` on the home page.

**Values (default).** size 1440 x 942.22; padding 40px 0px; border T: 1px solid oklab(0.999994 0.0000455678 0.0000200868 / 0.25); background #0f0f0f `light.text.primary`; text CoFo Sans Mono 12/16.32 400, #ffffff `light.surface.primary`.

![Footer default](components/crops/footer-default.png)

#### Footer link
"About" in the footer. Measured, never followed. Read as `footer-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, focus-visible, pressed) | size 37.67 x 14; background transparent; image linear-gradient(#ffffff `light.surface.primary`, #ffffff `light.surface.primary`); text Rooftop 12/16.32 400, #ffffff `light.surface.primary`; transition background-size 0.3s ease |

![Footer link default](components/crops/footer-link-default.png) ![Footer link hover](components/crops/footer-link-hover.png) ![Footer link focus-visible](components/crops/footer-link-focus-visible.png) ![Footer link pressed](components/crops/footer-link-pressed.png)

### Home

The landing: a ManyChatGravity hero, a neon-pink Get started pill, and an FAQ accordion.

#### Hero heading
"Social smarter, not harder." set in ManyChatGravity. Read as `hero-h1` on the home page.

**Values (default).** size 692 x 118.06; background transparent; text ManyChatGravity 72/59.04 400, #ffffff `light.surface.primary`.

![Hero heading default](components/crops/hero-h1-default.png)

#### Hero Get started
The neon-pink hero pill. It opens sign-up. Measured, never followed. Read as `hero-cta` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, focus-visible, pressed) | size 149.95 x 48; padding 14px 20px; radius 999px; background #fa0cf7 `core.color.brand.neon-pink`; text CoFo Sans Mono 14/20 400, #ffffff `light.surface.primary` (the element's computed colour; its first label span is a transparent copy); transition background 0.3s ease, transform 0.3s ease; layers ::before rgba(0, 0, 0, 0) 1px none 1 |

![Hero Get started default](components/crops/hero-cta-default.png) ![Hero Get started hover](components/crops/hero-cta-hover.png) ![Hero Get started focus-visible](components/crops/hero-cta-focus-visible.png) ![Hero Get started pressed](components/crops/hero-cta-pressed.png)

#### Section heading
A Rooftop section heading below the hero. Read as `section-heading` on the home page.

**Values (default).** size 930 x 118.06; background transparent; text ManyChatGravity 72/59.04 400, #0f0f0f `light.text.primary`; transition opacity 0.7s cubic-bezier(0.43, 0.195, 0.02, 1), transform 0.7s cubic-bezier(0.43, 0.195, 0.02, 1).

![Section heading default](components/crops/section-heading-default.png)

#### Creator quote
A published creator quote on the home page. Marketing copy, not an account. Read as `quote-card` on the home page.

Not on the page when it was captured.

#### FAQ accordion
A home FAQ summary. Opened by its own click. Nothing was submitted. Read as `faq-item` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: opened, focus-visible) | size 841.33 x 62.39; background transparent; text Rooftop 16/22.4 400, #ffffff `light.surface.primary` |

![FAQ accordion default](components/crops/faq-item-default.png) ![FAQ accordion opened](components/crops/faq-item-opened.png) ![FAQ accordion focus-visible](components/crops/faq-item-focus-visible.png)

### Pricing

The /pricing page: Plans that scale when you do, the Monthly/Annual labels, the Free card, Start for free.

#### Pricing heading
"Plans that scale when you do". Read as `price-h1` on the pricing page.

**Values (default).** size 1376 x 38.88; background transparent; text Rooftop 36/38.88 600, #0f0f0f `light.text.primary`.

![Pricing heading default](components/crops/price-h1-default.png)

#### Billing toggle
The Annual side of the Monthly/Annual switch. The control is a label, not a button. A local UI toggle. Checkout was never opened. Read as `billing-toggle` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 51.25 x 19.59; background transparent; text CoFo Sans Mono 14/19.6 400, #ffffff `light.surface.primary` |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

![Billing toggle default](components/crops/billing-toggle-default.png) ![Billing toggle hover](components/crops/billing-toggle-hover.png) ![Billing toggle pressed](components/crops/billing-toggle-pressed.png)

#### Price card
The Free plan card: $0, 25 active contacts, Start for free. Read as `price-card` on the pricing page.

**Values (default).** size 368.53 x 661.53; padding 32px 32px 40px 32px; radius 24px; background #ffffff `light.surface.primary`; text Rooftop 20/28 700, #0f0f0f `light.text.primary`; icon 16 x 16, oklab(0.168402 0.0000076443 0.00000336766 / 0.2).

![Price card default](components/crops/price-card-default.png)

#### Price CTA
"Start for free" on the Free card. It opens sign-up. Measured, never followed. Checkout was not submitted. Read as `price-cta` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, focus-visible, pressed) | size 304.53 x 48; padding 14px 20px; radius 999px; background #0f0f0f `light.text.primary`; text CoFo Sans Mono 12/20 400, #ffffff `light.surface.primary` (the element's computed colour; its first label span is a transparent copy); transition background 0.3s ease, transform 0.3s ease; layers ::before rgba(0, 0, 0, 0) 1px none 1; ancestors div.relative.h-full bg #ffffff `light.surface.primary` |

![Price CTA default](components/crops/price-cta-default.png) ![Price CTA hover](components/crops/price-cta-hover.png) ![Price CTA focus-visible](components/crops/price-cta-focus-visible.png) ![Price CTA pressed](components/crops/price-cta-pressed.png)

#### Pricing FAQ
A pricing FAQ summary, opened by its own click. Nothing was submitted. Read as `price-faq` on the pricing page.

Not on the page when it was captured.

### Instagram product

The /product/instagram page: Your Instagram just got smarter, and a Get started pill.

#### Product heading
"Your Instagram just got smarter". Read as `product-h1` on the instagram page.

**Values (default).** size 590 x 118.06; background transparent; text ManyChatGravity 72/59.04 400, #ffffff `light.surface.primary`.

![Product heading default](components/crops/product-h1-default.png)

#### Product CTA
A product-page Get started pill. Measured, never followed. Read as `product-cta` on the instagram page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, focus-visible, pressed) | size 136.53 x 44.31; padding 14px 20px; radius 999px; background #ffffff `light.surface.primary`; text CoFo Sans Mono 12/16.32 400, #ffffff `light.surface.primary` (measured white on a white fill, so the visible label's colour was not read); transition background 0.3s ease, transform 0.3s ease; layers ::before rgba(0, 0, 0, 0) 1px none 1 |

![Product CTA default](components/crops/product-cta-default.png) ![Product CTA hover](components/crops/product-cta-hover.png) ![Product CTA focus-visible](components/crops/product-cta-focus-visible.png) ![Product CTA pressed](components/crops/product-cta-pressed.png)

### How-to resources

The /resources/how-to page: How to Use Manychat, a public guide index. Not the in-app template library.

#### How-to heading
"How to Use Manychat". A public guide index, not the bot builder. Read as `howto-h1` on the how-to page.

**Values (default).** size 1041.31 x 72; background transparent; text ManyChatGravity 80/72 400, #0f0f0f `light.text.primary`.

![How-to heading default](components/crops/howto-h1-default.png)

#### Guide card
A public how-to card. Measured, never followed into a form. Read as `howto-card` on the how-to page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 368 x 372.17; border 1px solid #f5f5f5 `light.background.secondary`; background transparent; shadow rgba(0, 0, 0, 0.08) 0px 4px 8px 0px; text Rooftop 20/24 600, rgba(15, 15, 15, 0.4); transition transform 0.3s ease, box-shadow 0.3s ease |
| hover | shadow rgba(0, 0, 0, 0.08) 0px 8px 16px 10px; text Rooftop 20/24 600, #0f0f0f `light.text.primary`; transform translate(0px, -4px) |

![Guide card default](components/crops/howto-card-default.png) ![Guide card hover](components/crops/howto-card-hover.png)

### Mobile (390 wide)

Home at phone width: a 60px nav, the 44px hero, a Get started pill. The painted hamburger was not a selectable control.

#### Mobile header
The nav at phone width. The site paints no <header> element. Read as `m-header` on the home page at 390 wide.

**Values (default).** size 390 x 60; background transparent; text CoFo Sans Mono 12/16.32 400, #ffffff `light.surface.primary`; transition transform 0.45s cubic-bezier(0.43, 0.195, 0.02, 1); icon 107.84 x 20, #ffffff `light.surface.primary`; layers div::before._4Y2iAa_menu 390pxx844px rgb(237, 242, 237); a.p_y-s.p_x-l 150.0x48.0 rgb(250, 12, 247) 999px; a::before.p_y-s.p_x-l 149.953pxx48px T:1px solid rgba(0, 0, 0, 0) / R:1px solid rgba(0, 0, 0, 0) / B:1px solid rgba(0, 0, 0, 0) / L:1px solid rgba(0, 0, 0, 0) 999px; div.mb-0.4rem.flex 358.0x48.3 rgb(255, 255, 255) 8px; span._4Y2iAa_underline_item.mc-text-label 51.3x16.3; span._4Y2iAa_underli.

Child layers that carry the look: div::before 390pxx844px background #edf2ed; a 150x48 background #fa0cf7 `core.color.brand.neon-pink` radius 999px; a::before 149.953pxx48px border 1px solid transparent radius 999px.

![Mobile header default](components/crops/m-header-default.png)

#### Mobile logo
Read as `m-logo` on the home page at 390 wide.

**Values (default).** size 107.84 x 20; background transparent; text Rooftop 15/19.5 400, #ffffff `light.surface.primary`; transition color 0.3s ease; icon 107.84 x 20, #ffffff `light.surface.primary`.

![Mobile logo default](components/crops/m-logo-default.png)

#### Mobile menu button
The menu trigger at 390px. A local toggle. Read as `m-hamburger` on the home page at 390 wide.

Not on the page when it was captured.

#### Mobile hero heading
The hero h1 at 390px. Read as `m-h1` on the home page at 390 wide.

**Values (default).** size 358 x 72.16; background transparent; text ManyChatGravity 44/36.08 400, #ffffff `light.surface.primary`.

![Mobile hero heading default](components/crops/m-h1-default.png)

#### Mobile Get started
A Get started link at 390px. Measured, never followed. Read as `m-cta` on the home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, focus-visible, pressed) | size 128.53 x 32.31; padding 8px 16px; radius 32px; background #fa0cf7 `core.color.brand.neon-pink`; text CoFo Sans Mono 12/16.32 400, #ffffff `light.surface.primary` (the element's computed colour; its first label span is a transparent copy); transition background 0.3s ease, transform 0.3s ease; opacity 0; layers ::before rgba(0, 0, 0, 0) 1px none 1 |

![Mobile Get started default](components/crops/m-cta-default.png) ![Mobile Get started hover](components/crops/m-cta-hover.png) ![Mobile Get started focus-visible](components/crops/m-cta-focus-visible.png) ![Mobile Get started pressed](components/crops/m-cta-pressed.png)

## Icons

No standalone SVG icon set was lifted on this pass. The wordmark and channel marks are visible in the crops and screenshots. Declared under layoutGaps in the catalog entry.

| Icon | Rendered sizes | View box | Style | Seen on | Next to |
|---|---|---|---|---|---|

## Gaps

### Sign-in and checkout

The bot builder and the in-app template library sit behind sign-in at app.manychat.com. Log in, Get started and Start for free were measured, never followed. Checkout was not submitted. /templates and /template-gallery returned 404 signed out. The painted mobile hamburger was not a selectable control in this headless pass, so the drawer was not captured.

### Pages

- **Outbound links.** Log in (app.manychat.com/signin), Get started (app.manychat.com/signup) and Start for free were measured, never followed. Checkout was not submitted.
- **Public pages captured.** Home, /pricing, /product/instagram and /resources/how-to, plus a phone pass on home and pricing. Other product pages share the same chrome.
- **The Product menu** was opened locally and screenshot as home-light-menu. The Instagram item inside it was measured. Solutions, Agencies and Resources were not individually componentized.
- **The in-app template library** sits behind sign-in. /templates and /template-gallery returned 404 signed out.
- **The mobile drawer** was not captured. The hamburger is painted, but it was not a selectable control in this headless pass.
- **The promo strip** is a campaign. What was captured is what this IP was served.

### States

- **Pressed** was forced with DevTools on every control, so a state a script adds on mousedown (if any) is missing.
- **Product, the billing labels and the FAQ** were toggled locally. Nothing was typed into or submitted.
- **No public form was opened.** Sign-up and checkout sit behind the CTAs. Fields, validation, disabled and error states were not measured.

### Themes

One painted theme, no toggle: a white field, #0f0f0f ink, a #fa0cf7 neon-pink hero pill, and a black Creator World strip on home. tokens.json emits light only.

### Fonts

- **ManyChatGravity** (display), **Rooftop** (UI) and **CoFo Sans Mono** (nav labels and pill text) are served by the site. Font files are not shipped in this package. The site sets html font-size to 10px, so 1rem is 10px.

### Screenshots

- Creator quotes, pricing figures and the hero artwork are the product's published content; only frames and components were measured.
- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files.

### Content left out

- Testimonial copy, pricing figures and the artwork inside panels are the product's content; only frames and components were measured.
