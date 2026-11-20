# Headspace components

The discovery list of every page and view captured, then one entry per component with crops of the real product, the icon index and the Gaps. Captured from www.headspace.com, organizations.headspace.com, checkout.headspace.com and auth.headspace.com on 2026-11-17, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running page. Nothing was signed into, bought, redeemed, sent or submitted.

The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) (46 components, 66 states). The page layouts are described in [raw/layout.json](raw/layout.json).

How to read an entry:

- A colour is its value followed by the palette token in [tokens.json](tokens.json) with the same value, when there is one. Text is written family size/line-height weight, then its colour, for example `SF Pro 14/21 500, #21252e`, and is read from the first text node inside the component.
- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example "default (same: focus-visible)". When the root paints nothing, "Child layers" names the first nodes inside it that do.
- Crops are images of the component read from the live page, in [components/crops/](components/crops) (64 files, named `{component}-{state}.png`, at 2x). Screenshots are in [screenshots/](screenshots).

## Discovery list

Screenshots are named `{page}-light-{state}.png` (headspace.com has one theme). Desktop shots are 1440 x 900 at 1x; `-full` shots are whole pages at 1x; mobile shots are `mobile-{page}-light-{state}.png`, 780 wide (390 at 2x).

| Surface | URL | Screenshots |
|---|---|---|
| Marketing home: hero, the 50%-off strip and CTA, feature and testimonial sections, the open mega-menu and the footer. | `/` | [default](screenshots/home-light-default.png), [full](screenshots/home-light-full.png), [menu](screenshots/home-light-menu.png) |
| The /app product overview: the numbered feature tabs and app benefits. | `/app` | [default](screenshots/app-light-default.png), [full](screenshots/app-light-full.png) |
| The meditation topic page. | `/meditation` | [default](screenshots/meditation-light-default.png), [full](screenshots/meditation-light-full.png) |
| The mindfulness topic page. | `/mindfulness` | [default](screenshots/mindfulness-light-default.png), [full](screenshots/mindfulness-light-full.png) |
| The sleep topic page. | `/sleep` | [default](screenshots/sleep-light-default.png), [full](screenshots/sleep-light-full.png) |
| The online-therapy product page. | `/online-therapy` | [default](screenshots/therapy-light-default.png), [full](screenshots/therapy-light-full.png) |
| The mental-health coaching page. | `/coaching` | [default](screenshots/coaching-light-default.png), [full](screenshots/coaching-light-full.png) |
| Ebb, the AI mental-health companion page. | `/ai-mental-health-companion` | [default](screenshots/ebb-light-default.png), [full](screenshots/ebb-light-full.png) |
| The mental-health hub page. | `/mental-health` | [default](screenshots/mental-health-light-default.png), [full](screenshots/mental-health-light-full.png) |
| The anxiety topic page. | `/mental-health/anxiety` | [default](screenshots/anxiety-light-default.png), [full](screenshots/anxiety-light-full.png) |
| The research/science page. | `/science` | [default](screenshots/science-light-default.png), [full](screenshots/science-light-full.png) |
| The about page. | `/about-us` | [default](screenshots/about-light-default.png), [full](screenshots/about-light-full.png) |
| The articles hub. | `/articles` | [default](screenshots/articles-light-default.png), [full](screenshots/articles-light-full.png) |
| One published article. | `/articles/can-you-use-hsa-or-fsa-for-mental-health` | [default](screenshots/article-light-default.png), [full](screenshots/article-light-full.png) |
| The free-preview content library. | `/content` | [default](screenshots/content-light-default.png), [full](screenshots/content-light-full.png) |
| A content topic page (New and Popular). | `/content/topics/100` | [default](screenshots/topic-light-default.png), [full](screenshots/topic-light-full.png) |
| The plans page: plan cards, billing switch, seat slider. | `/subscriptions` | [default](screenshots/subscriptions-light-default.png), [full](screenshots/subscriptions-light-full.png) |
| The family-plan page. | `/family-plan` | [default](screenshots/family-light-default.png), [full](screenshots/family-light-full.png) |
| The gift page. | `/buy/gift` | [default](screenshots/gift-light-default.png), [full](screenshots/gift-light-full.png) |
| The 30-day guest-pass page. | `/share-headspace` | [default](screenshots/share-light-default.png), [full](screenshots/share-light-full.png) |
| The redeem-a-code form. | `/code` | [default](screenshots/redeem-light-default.png), [full](screenshots/redeem-light-full.png) |
| The mindful-families page. | `/app/mindful-families` | [default](screenshots/mindful-families-light-default.png), [full](screenshots/mindful-families-light-full.png) |
| The B2B marketing home. | `organizations.headspace.com/` | [default](screenshots/org-home-light-default.png), [full](screenshots/org-home-light-full.png) |
| The B2B employers page. | `organizations.headspace.com/employers` | [default](screenshots/org-employers-light-default.png), [full](screenshots/org-employers-light-full.png) |
| The self-serve checkout shell, viewed only. | `checkout.headspace.com/checkout` | [default](screenshots/checkout-light-default.png), [full](screenshots/checkout-light-full.png) |
| The universal login (reached through /login). | `/login -> auth.headspace.com` | [default](screenshots/login-light-default.png), [full](screenshots/login-light-full.png) |
| The universal signup (reached through /signup). | `/signup -> auth.headspace.com` | [default](screenshots/signup-light-default.png), [full](screenshots/signup-light-full.png) |
| Home at 390: hero, the open nav sheet, the full page. | `/` | [default](screenshots/mobile-home-light-default.png), [drawer](screenshots/mobile-home-light-drawer.png), [full](screenshots/mobile-home-light-full.png) |
| Plans at 390. | `/subscriptions` | [default](screenshots/mobile-subscriptions-light-default.png), [full](screenshots/mobile-subscriptions-light-full.png) |
| The meditation page at 390. | `/meditation` | [default](screenshots/mobile-meditation-light-default.png), [full](screenshots/mobile-meditation-light-full.png) |
| The content library at 390. | `/content` | [default](screenshots/mobile-content-light-default.png), [full](screenshots/mobile-content-light-full.png) |

### Overlays and transient states

| State | Where | How it was reached | Captured |
|---|---|---|---|
| Header mega-menu, open | home | a real pointer hover on the For You category link - the menu's links were never followed | [home-light-menu](screenshots/home-light-menu.png), [nav-mega-menu](#nav-mega-menu) |
| Mobile nav sheet, open | mobile home | the nav button's own press - the sheet's links were never followed | [mobile-home-light-drawer](screenshots/mobile-home-light-drawer.png) |
| OneTrust consent layer | every page, on load | hidden with display:none for every capture - never answered | (no capture; it is hidden, not a state) |
| Auth0 universal login | /login and /signup | the redirect each public route performs | [login-light-default](screenshots/login-light-default.png), [signup-light-default](screenshots/signup-light-default.png), [auth-card](#auth-card) |
| Checkout shell | checkout.headspace.com | the arrival state only - no voucher, no card, no submit | [checkout-light-default](screenshots/checkout-light-default.png) |
| Redeem-a-code field, focused | /code | a real click into the field; never filled, never redeemed | [redeem-field](#redeem-field) |

## Shared values

Values that apply across entries, from the measurement files.

**Focus.** 12 components were given a real keyboard focus. 12 draw a ring: `nav-logo` (1px auto #101010 `light.color.accent.focus`, offset 1px), `nav-category` (1px auto #101010 `light.color.accent.focus`, offset 1px), `nav-cta` (2px solid #0040ea `light.color.brand.blue-hover`, offset 1px), `nav-login` (2px solid #0040ea `light.color.brand.blue-hover`, offset 1px), `footer-link` (1px auto #101010 `light.color.accent.focus`, offset 1px), `hero-cta` (2px solid #0040ea `light.color.brand.blue-hover`, offset 1px), `prose-link` (1px auto #101010 `light.color.accent.focus`, offset 1px), `subscribe-button` (2px solid #0040ea `light.color.brand.blue-hover`, offset 0px), `redeem-field` (1px auto #101010 `light.color.accent.focus`, offset 0px), `redeem-button` (2px solid #0040ea `light.color.brand.blue-hover`, offset 0px), `auth-continue` (2px solid #0040ea `light.color.brand.blue-hover`, offset 2px), `org-cta` (1px solid #000000 `declared.black`, offset 5px). The other 0 draw none, so a keyboard user sees no change: .

**Pressed.** The pressed states below were forced with DevTools (`CSS.forcePseudoState` :active:hover), so no button was pressed. On the measured buttons the press keeps the resting fill (the blue pill stays `#0061ef`, the dark pill `#2d2c2b`) - Headspace answers the pointer with colour on hover instead.

**Motion.** Transitions measured on the components, by duration.

| Duration | Easing | Property | Where |
|---|---|---|---|
| 0.15s | `cubic-bezier(0.32, 0.94, 0.6, 1)` | background-color, border-color, box-shadow, color, transform | auth-continue, auth-sso, footer-link, hero-cta, m-hero-cta, m-nav-button, nav-cta, nav-login and more |
| 0.2s | `ease` | all | org-cta |

**Layout grid.** Read on each page at each width ([raw/layout.json](raw/layout.json)).

| Page | 1440 | 1920 | 1024 | 390 |
|---|---|---|---|---|
| home | content x 0, 1440 wide; grid 223.5 223.5 223.5 223.5 gap 16px | content x 0, 1920 wide; grid 329.1 329.1 329.1 329.1 gap 16px | content x 0, 1024 wide; grid 192 192 gap 40px | content x 0, 390 wide |
| subscriptions | content x 0, 1440 wide | content x 0, 1920 wide | content x 0, 1024 wide | content x 0, 390 wide |
| meditation | content x 0, 1440 wide; grid 223.5 223.5 223.5 223.5 gap 16px | content x 0, 1920 wide; grid 329.1 329.1 329.1 329.1 gap 16px | content x 0, 1024 wide; grid 192 192 gap 40px | content x 0, 390 wide |
| content | content x 0, 1440 wide; grid 223.5 223.5 223.5 223.5 gap 16px | content x 0, 1920 wide; grid 329.1 329.1 329.1 329.1 gap 16px | content x 0, 1024 wide; grid 192 192 gap 40px | content x 0, 390 wide |
| org-home | content x 0, 1440 wide; grid 628 628 gap 40px | content x 0, 1920 wide; grid 844 844 gap 40px | content x 0, 1024 wide; grid 445.4 445.4 gap 30.735px | content x 0, 390 wide; grid 12.2 278.9 gap 15.2552px |

**Card shapes.** Default-state values; the entries hold the states.

| Card | Size | Border | Radius | Background | Shadow | Padding |
|---|---|---|---|---|---|---|
| [Auth card](#auth-card) | 1440 x 870.39 | - | 32px | #ffffff `light.color.surface.header` | transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, rgba(0, 0, 0, 0.12) 0px 12px 40px 0px | 48px 40px |
| [B2B card](#b2b-card) | 340 x 430 | - | 8px | #ffce00 `light.color.brand.yellow` | none | 32px 40px |

## Components

### Marketing chrome

The header and footer shared by every marketing page: the wordmark and orange dot, the For You / For Business / For Providers / Our Plans / Resources / About categories whose hover opens one shared mega-menu, Log in, Help and the offer CTA, plus the promo strip above and the link columns, language selector and app badges below.

#### Promo strip
The banner over the header ("Feel your best for 50% off →"). Read as `nav-promo-strip` on the home page.

**Values (default).** size 1440 x 26; background transparent; text Headspace Apercu 18/26 500, #2d2c2b `light.color.ink.nav`.

![Promo strip default](components/crops/nav-promo-strip-default.png)

#### Header bar
The top bar: logo, the For You / For Business / For Providers / Our Plans / Resources / About categories, Log in, Help and the Get-50%-off CTA. Read as `nav-header` on the home page.

**Values (default).** size 1440 x 80; padding 0px 48px; background #ffffff `light.color.surface.header`; text Headspace Apercu 16/18.4 400, #2d2c2b `light.color.ink.nav`; icon 16 x 16, #2d2c2b `light.color.ink.nav`.

![Header bar default](components/crops/nav-header-default.png)

#### Logo link
The headspace wordmark image in the header. Read as `nav-logo` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 152 x 80; background transparent; text Headspace Apercu 16/18.4 400, #0000ee |
| focus-visible | outline 1px auto #101010 `light.color.accent.focus`, offset 1px |

![Logo link default](components/crops/nav-logo-default.png) ![Logo link hover](components/crops/nav-logo-hover.png) ![Logo link focus-visible](components/crops/nav-logo-focus-visible.png)

#### Nav category link
A top-level header link ("For You"): hovering it opens the mega-menu. Read as `nav-category` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 52 x 18.39; background transparent; text Headspace Apercu 16/18.4 400, #2d2c2b `light.color.ink.nav` |
| hover | size 56 x 18.39; text Headspace Apercu 16/18.4 700, #2d2c2b `light.color.ink.nav` |
| focus-visible | size 56 x 18.39; outline 1px auto #101010 `light.color.accent.focus`, offset 1px; text Headspace Apercu 16/18.4 700, #2d2c2b `light.color.ink.nav` |

![Nav category link default](components/crops/nav-category-default.png) ![Nav category link hover](components/crops/nav-category-hover.png) ![Nav category link focus-visible](components/crops/nav-category-focus-visible.png)

#### Mega-menu pane (open)
The dropdown pane of subcategory links under a hovered category. "opened" is a real pointer hover on the category link; the pane is read while the pointer rests inside it. Read as `nav-mega-menu` on the home page.

**Values (opened).** size 223.52 x 204.78; background transparent; text Headspace Apercu 16/20.8 400, #44423f `light.color.ink.muted`; icon 16 x 16, #2d2c2b `light.color.ink.nav`.

![Mega-menu pane (open) opened](components/crops/nav-mega-menu-opened.png)

#### Mega-menu link
One link inside the open mega-menu ("Meditation" under For You). Read as `nav-subcategory` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| opened (same: hover) | size 94 x 20.8; background transparent; text Headspace Apercu 16/20.8 400, #44423f `light.color.ink.muted`; icon 16 x 16, #2d2c2b `light.color.ink.nav` |

![Mega-menu link opened](components/crops/nav-subcategory-opened.png) ![Mega-menu link hover](components/crops/nav-subcategory-hover.png)

#### Header CTA ("Get 50% off")
The pill call-to-action in the header, measured, never followed. Read as `nav-cta` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 125 x 48; padding 14.3px 24px; border 2px solid transparent; radius 32px; background #0061ef `light.color.brand.blue`; shadow rgba(65, 61, 69, 0.2) 0px 2px 0px 0px; text Headspace Apercu 14/15.4 700, #ffffff `light.color.surface.header`; transition color 0.15s cubic-bezier(0.32, 0.94, 0.6, 1), background-color 0.15s cubic-bezier(0.32, 0.94, 0.6, 1), border-color 0.15s cubic-bezier(0.32, 0.94, 0.6, 1), box-shadow 0.15s cubic-bezier(0.32, 0.94, 0.6, 1), transform 0.15s cubic-bezier(0.32, 0.94, 0.6, 1) |
| hover | background #0040ea `light.color.brand.blue-hover` |
| focus-visible | background #0040ea `light.color.brand.blue-hover`; outline 2px solid #0040ea `light.color.brand.blue-hover`, offset 1px |

![Header CTA ("Get 50% off") default](components/crops/nav-cta-default.png) ![Header CTA ("Get 50% off") hover](components/crops/nav-cta-hover.png) ![Header CTA ("Get 50% off") focus-visible](components/crops/nav-cta-focus-visible.png) ![Header CTA ("Get 50% off") pressed](components/crops/nav-cta-pressed.png)

#### "Log in" link
The sign-in link in the header, measured, never followed. Read as `nav-login` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 46 x 48; border 2px solid transparent; radius 32px; background transparent; text Headspace Apercu 16/17.6 400, #2d2c2b `light.color.ink.nav`; transition color 0.15s cubic-bezier(0.32, 0.94, 0.6, 1), background-color 0.15s cubic-bezier(0.32, 0.94, 0.6, 1), border-color 0.15s cubic-bezier(0.32, 0.94, 0.6, 1), box-shadow 0.15s cubic-bezier(0.32, 0.94, 0.6, 1), transform 0.15s cubic-bezier(0.32, 0.94, 0.6, 1) |
| hover | size 48 x 48; text Headspace Apercu 16/17.6 700, #44423f `light.color.ink.muted` |
| focus-visible | outline 2px solid #0040ea `light.color.brand.blue-hover`, offset 1px; text Headspace Apercu 16/17.6 400, #44423f `light.color.ink.muted` |

!["Log in" link default](components/crops/nav-login-default.png) !["Log in" link hover](components/crops/nav-login-hover.png) !["Log in" link focus-visible](components/crops/nav-login-focus-visible.png)

#### Footer
The page footer: link columns, app-store badges, the language selector and legal links. Read as `footer` on the home page.

**Values (default).** size 1360 x 534.14; padding 0px 0px 40px 0px; background transparent; text Headspace Apercu 24/32 700, #4b4c4d `light.color.ink.primary`.

Child layers that carry the look: a 108x48 background #0061ef `light.color.brand.blue` border 2px solid transparent radius 32px shadow rgba(65, 61, 69, 0.2) 0px 2px 0px 0px; button 0x0 background #f9f4f2 `light.color.surface.page` border 2px solid #44423f `light.color.ink.muted` radius 32px; div 0x0 background #44423f `light.color.ink.muted` radius 8px shadow rgba(65, 61, 69, 0.2) 0px 2px 0px 0px.

![Footer default](components/crops/footer-default.png)

#### Footer link
A link in a footer column. Read as `footer-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 228.2 x 13.8; background transparent; text Headspace Apercu 12/13.8 500, #44423f `light.color.ink.muted`; transition color 0.15s cubic-bezier(0.32, 0.94, 0.6, 1), background-color 0.15s cubic-bezier(0.32, 0.94, 0.6, 1), border-color 0.15s cubic-bezier(0.32, 0.94, 0.6, 1), box-shadow 0.15s cubic-bezier(0.32, 0.94, 0.6, 1), transform 0.15s cubic-bezier(0.32, 0.94, 0.6, 1); opacity 0.7 |
| hover | opacity none |
| focus-visible | outline 1px auto #101010 `light.color.accent.focus`, offset 1px |

![Footer link default](components/crops/footer-link-default.png) ![Footer link hover](components/crops/footer-link-hover.png) ![Footer link focus-visible](components/crops/footer-link-focus-visible.png)

#### Language selector
The footer's locale button ("English"). Measured at rest — its option list was never opened. Read as `footer-language` on the home page.

Not on the page when it was captured.

#### App-store badge
The App Store / Google Play badge links in the footer. Read as `footer-app-badge` on the home page.

Not on the page when it was captured.

### Hero and type

The hero headline and lede on the captured pages, the section and card headings, body copy and the inline text link, all in Headspace Apercu.

#### Hero headline (h1)
The page's display headline in Headspace Apercu. Read as `hero-h1` on the guest pass page.

**Values (default).** size 429.13 x 72; background transparent; text Headspace Apercu 64/72 700, #4b4c4d `light.color.ink.primary`.

![Hero headline (h1) default](components/crops/hero-h1-default.png)

#### Hero lede
The paragraph under the hero headline. Read as `hero-lede` on the article page.

**Values (default).** size 308.42 x 38.41; background transparent; text Headspace Apercu 16/19.2 700, #44423f `light.color.ink.muted`.

![Hero lede default](components/crops/hero-lede-default.png)

#### Hero primary CTA
The pill call-to-action inside the hero ("Get 50% off" / "Get started"), measured, never followed. Read as `hero-cta` on the article page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 136 x 48; padding 13.2px 24px; border 2px solid transparent; radius 32px; background #0061ef `light.color.brand.blue`; shadow rgba(65, 61, 69, 0.2) 0px 2px 0px 0px; text Headspace Apercu 16/17.6 700, #ffffff `light.color.surface.header`; transition color 0.15s cubic-bezier(0.32, 0.94, 0.6, 1), background-color 0.15s cubic-bezier(0.32, 0.94, 0.6, 1), border-color 0.15s cubic-bezier(0.32, 0.94, 0.6, 1), box-shadow 0.15s cubic-bezier(0.32, 0.94, 0.6, 1), transform 0.15s cubic-bezier(0.32, 0.94, 0.6, 1) |
| hover | background #0040ea `light.color.brand.blue-hover` |
| focus-visible | background #0040ea `light.color.brand.blue-hover`; outline 2px solid #0040ea `light.color.brand.blue-hover`, offset 1px |

![Hero primary CTA default](components/crops/hero-cta-default.png) ![Hero primary CTA hover](components/crops/hero-cta-hover.png) ![Hero primary CTA focus-visible](components/crops/hero-cta-focus-visible.png) ![Hero primary CTA pressed](components/crops/hero-cta-pressed.png)

#### Section heading (h2)
A mid-page section headline. Read as `prose-h2` on the article page.

**Values (default).** size 780.86 x 38.41; background transparent; text Headspace Apercu 32/38.4 700, #4b4c4d `light.color.ink.primary`.

![Section heading (h2) default](components/crops/prose-h2-default.png)

#### Card heading (h3)
A card or feature heading. Read as `prose-h3` on the article page.

**Values (default).** size 301.31 x 27; background transparent; text Headspace Apercu 18/27 400, #141313 `light.color.action.secondary-hover`.

![Card heading (h3) default](components/crops/prose-h3-default.png)

#### Body copy
A body paragraph. Read as `prose-body` on the article page.

**Values (default).** size 1440 x 26; background transparent; text Headspace Apercu 18/26 500, #2d2c2b `light.color.ink.nav`.

![Body copy default](components/crops/prose-body-default.png)

#### Inline text link
A link inside body copy. Read as `prose-link` on the article page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 277 x 42; background transparent; text Headspace Apercu 14/24 400, #2d2c2b `light.color.ink.nav` |
| focus-visible | outline 1px auto #101010 `light.color.accent.focus`, offset 1px |

![Inline text link default](components/crops/prose-link-default.png) ![Inline text link hover](components/crops/prose-link-hover.png) ![Inline text link focus-visible](components/crops/prose-link-focus-visible.png)

### Marketing widgets

The cards and controls the marketing pages are built from: feature and testimonial cards, the /app feature tabs, the plan card, billing switch and seat slider on /subscriptions, the content preview tiles and Subscribe button on /content, and the FAQ accordion.

#### Feature/benefit card
A rounded card on the home page (benefit or content tile). Read as `feature-card` on the home page.

Not on the page when it was captured.

#### Testimonial/press quote
A quote or press-mention block on the home page. Read as `testimonial` on the home page.

Not on the page when it was captured.

#### Feature tab
A numbered feature tab on /app ("1 Guided meditations", "2 AI guidance", ...). Its own activation is a local UI toggle. Read as `app-tab` on the /app product overview page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 205 x 30; background transparent; text Headspace Apercu 18/26 700, #ffffff `light.color.surface.header` |

Child layers that carry the look: span 30x30 background #0061ef `light.color.brand.blue` radius 50%.

![Feature tab default](components/crops/app-tab-default.png) ![Feature tab hover](components/crops/app-tab-hover.png)

#### FAQ accordion row
A frequently-asked-questions row near the foot of a topic page (a details/summary or button accordion). Measured at rest and opened by its own toggle. Read as `faq-item` on the meditation page.

Not on the page when it was captured.

#### "Subscribe" button
The subscribe action on a plan/upsell card, measured, never pressed. Read as `subscribe-button` on the content library page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 151 x 57.8; padding 16px 32px; border 2px solid transparent; radius 32px; background #2d2c2b `light.color.ink.nav`; shadow rgba(65, 61, 69, 0.2) 0px 2px 0px 0px; text Headspace Apercu 18/19.8 700, #ffffff `light.color.surface.header`; transition color 0.15s cubic-bezier(0.32, 0.94, 0.6, 1), background-color 0.15s cubic-bezier(0.32, 0.94, 0.6, 1), border-color 0.15s cubic-bezier(0.32, 0.94, 0.6, 1), box-shadow 0.15s cubic-bezier(0.32, 0.94, 0.6, 1), transform 0.15s cubic-bezier(0.32, 0.94, 0.6, 1) |
| hover | background #141313 `light.color.action.secondary-hover` |
| focus-visible | background #141313 `light.color.action.secondary-hover`; outline 2px solid #0040ea `light.color.brand.blue-hover`, offset 0px |

!["Subscribe" button default](components/crops/subscribe-button-default.png) !["Subscribe" button hover](components/crops/subscribe-button-hover.png) !["Subscribe" button focus-visible](components/crops/subscribe-button-focus-visible.png)

#### Content preview tile
A meditation/music/sleep preview tile on /content. Never played. Read as `content-tile` on the content library page.

Not on the page when it was captured.

#### Preview play button
A play control on a preview tile or audio row. Never pressed — previews were not played. Read as `play-button` on the content library page.

Not on the page when it was captured.

#### Plan card
A subscription plan card on /subscriptions (radius 12, cream fill). Read as `plan-card` on the subscriptions page.

Not on the page when it was captured.

#### Billing switch
The monthly/annual switch control on /subscriptions (role switch or checkbox name="switch"), measured at rest — never toggled. Read as `plan-switch` on the subscriptions page.

Not on the page when it was captured.

#### Seat slider
A range input on the plans page (member-count slider), measured at rest — never dragged. Read as `plan-slider` on the subscriptions page.

**Values (default).** size 406.47 x 8; background #ffffff `light.color.surface.header`; text Headspace Apercu 16/18.4 400, #9d968e; opacity 0; placeholder #9d968e.

![Seat slider default](components/crops/plan-slider-default.png)

### Forms

The signed-out fields: the newsletter email input in the footer, and the redeem-a-code field and its button on /code. Fields were clicked into, never filled; buttons never pressed.

#### Newsletter email field
The footer's email input, clicked into — nothing typed. Read as `newsletter-field` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 281 x 58; padding 24px 16px 8px 16px; border 1px solid #d2d5de `light.color.line.field`; radius 8px; background #ffffff `light.color.surface.header`; text Headspace Apercu 16/24 400, #000000 `declared.black`; placeholder #000000 `declared.black` |
| focused | outline 1px auto #101010 `light.color.accent.focus`, offset 0px |

![Newsletter email field default](components/crops/newsletter-field-default.png) ![Newsletter email field focused](components/crops/newsletter-field-focused.png)

#### Redeem-code field
The "Enter your code" text input on /code, clicked into — nothing typed. Read as `redeem-field` on the redeem-a-code page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 344 x 50; padding 12px 32px 12px 12px; radius 4px; background #ffffff `light.color.surface.header`; text Headspace Apercu 18/26 500, #000000 `declared.black`; placeholder #757575 |
| focused, focus-visible | outline 1px auto #101010 `light.color.accent.focus`, offset 0px |

![Redeem-code field default](components/crops/redeem-field-default.png) ![Redeem-code field focused](components/crops/redeem-field-focused.png) ![Redeem-code field focus-visible](components/crops/redeem-field-focus-visible.png)

#### "Redeem code" button
The submit on /code, measured, never pressed. Read as `redeem-button` on the redeem-a-code page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 165 x 52; padding 14px 32px; radius 32px; background #0061ef `light.color.brand.blue`; shadow rgba(65, 61, 69, 0.2) 0px 2px 0px 0px; text Headspace Apercu 16/17.6 700, #ffffff `light.color.surface.header`; transition color 0.15s cubic-bezier(0.32, 0.94, 0.6, 1), background-color 0.15s cubic-bezier(0.32, 0.94, 0.6, 1), border-color 0.15s cubic-bezier(0.32, 0.94, 0.6, 1), box-shadow 0.15s cubic-bezier(0.32, 0.94, 0.6, 1), transform 0.15s cubic-bezier(0.32, 0.94, 0.6, 1) |
| hover | background #0040ea `light.color.brand.blue-hover` |
| focus-visible | background #0040ea `light.color.brand.blue-hover`; outline 2px solid #0040ea `light.color.brand.blue-hover`, offset 0px |

!["Redeem code" button default](components/crops/redeem-button-default.png) !["Redeem code" button hover](components/crops/redeem-button-hover.png) !["Redeem code" button focus-visible](components/crops/redeem-button-focus-visible.png)

### Auth surface

The Auth0 universal login on auth.headspace.com, reached through /login and /signup: the centred card, the email field and the Continue / Continue-with-SSO buttons, measured empty, never filled or submitted.

#### Auth card
The centred card on auth.headspace.com (the universal login). Read as `auth-card` on the universal signup (auth.headspace.com) page.

**Values (default).** size 1440 x 870.39; padding 48px 40px; background transparent; text Headspace Apercu 24/28.8 700, #1e212a; icon 16 x 16, #ffffff `light.color.surface.header`.

Child layers that carry the look: div 400x774.4 background #ffffff `light.color.surface.header` radius 32px shadow transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, rgba(0, 0, 0, 0.12) 0px 12px 40px 0px; div 336x56 background #ffffff `light.color.surface.header` border 2px solid #e2ded9 `declared.wary.grey.200` radius 12px; button 336x48 background #0061ef `light.color.brand.blue` border 2px solid transparent radius 32px.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Email field
The email input on the universal login, clicked into — nothing typed. Read as `auth-email` on the universal signup (auth.headspace.com) page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focused) | size 300 x 24; background transparent; text MyCustomFont 16/24 400, #2d2c2b `light.color.ink.nav`; placeholder #2d2c2b `light.color.ink.nav` |

![Email field default](components/crops/auth-email-default.png) ![Email field focused](components/crops/auth-email-focused.png)

#### "Continue" button
The primary submit on the universal login, measured, never pressed. Read as `auth-continue` on the universal login (auth.headspace.com) page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 336 x 48; padding 13.2px 24px; border 2px solid transparent; radius 32px; background #0061ef `light.color.brand.blue`; text MyCustomFont 16/17.6 700, #ffffff `light.color.surface.header`; transition color 0.15s cubic-bezier(0.32, 0.94, 0.6, 1), background-color 0.15s cubic-bezier(0.32, 0.94, 0.6, 1), border-color 0.15s cubic-bezier(0.32, 0.94, 0.6, 1), box-shadow 0.15s cubic-bezier(0.32, 0.94, 0.6, 1), transform 0.15s cubic-bezier(0.32, 0.94, 0.6, 1) |
| hover | background #0040ea `light.color.brand.blue-hover` |
| focus-visible | background #0040ea `light.color.brand.blue-hover`; outline 2px solid #0040ea `light.color.brand.blue-hover`, offset 2px |

!["Continue" button default](components/crops/auth-continue-default.png) !["Continue" button hover](components/crops/auth-continue-hover.png) !["Continue" button focus-visible](components/crops/auth-continue-focus-visible.png)

#### "Continue with SSO" button
The secondary SSO submit, measured, never pressed. Read as `auth-sso` on the universal login (auth.headspace.com) page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 336 x 48; padding 13.2px 24px; border 2px solid transparent; radius 32px; background #f9f4f2 `light.color.surface.page`; text MyCustomFont 16/17.6 700, #44423f `light.color.ink.muted`; transition color 0.15s cubic-bezier(0.32, 0.94, 0.6, 1), background-color 0.15s cubic-bezier(0.32, 0.94, 0.6, 1), border-color 0.15s cubic-bezier(0.32, 0.94, 0.6, 1), box-shadow 0.15s cubic-bezier(0.32, 0.94, 0.6, 1), transform 0.15s cubic-bezier(0.32, 0.94, 0.6, 1); icon 24 x 24, #44423f `light.color.ink.muted` |
| hover | background #e5e7ec `light.color.action.tertiary-hover` |

!["Continue with SSO" button default](components/crops/auth-sso-default.png) !["Continue with SSO" button hover](components/crops/auth-sso-hover.png)

### Checkout

The self-serve checkout on checkout.headspace.com as it paints on arrival, viewed only - nothing filled, nothing submitted.

#### Checkout panel
The self-serve checkout surface (plan picker or payment form) as it paints without a voucher — viewed only, nothing filled or submitted. Read as `checkout-form` on the checkout page.

Not on the page when it was captured.

#### Checkout field
An input on the checkout surface (email or plan option), measured at rest. Read as `checkout-field` on the checkout page.

Not on the page when it was captured.

#### Checkout button
The primary action on the checkout surface, measured, never pressed. Read as `checkout-button` on the checkout page.

Not on the page when it was captured.

### B2B surface

The organizations.headspace.com business marketing pages on the same stack: the hero headline, the white pill CTA that goes orange on hover, and a yellow highlight card.

#### B2B hero headline
The organizations.headspace.com hero h1. Read as `org-h1` on the B2B employers page.

**Values (default).** size 624 x 96; background transparent; text HS Apercu Bold 48/48 700, #ffffff `light.color.surface.header`.

![B2B hero headline default](components/crops/org-h1-default.png)

#### B2B CTA
The business-surface call-to-action ("Request a demo" / "Get started"), measured, never followed. Read as `org-cta` on the B2B employers page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 183 x 50.16; padding 14.08px 32px; border 1px solid #ffffff `light.color.surface.header`; radius 800px; background #ffffff `light.color.surface.header`; text HS Apercu Medium 16/20 500, #2d2c2b `light.color.ink.nav`; transition all 0.2s ease |
| hover | border 1px solid #ff7e1d `light.color.brand.orange`; background #ff7e1d `light.color.brand.orange`; text HS Apercu Medium 16/20 500, #ffffff `light.color.surface.header` |
| focus-visible | outline 1px solid #000000 `declared.black`, offset 5px |

![B2B CTA default](components/crops/org-cta-default.png) ![B2B CTA hover](components/crops/org-cta-hover.png) ![B2B CTA focus-visible](components/crops/org-cta-focus-visible.png)

#### B2B card
A card on the B2B surface (stat, benefit or customer logo tile). Read as `org-card` on the B2B home page.

**Values (default).** size 340 x 430; padding 32px 40px; radius 8px; background #ffce00 `light.color.brand.yellow`; text HS Apercu Bold 14/21 700, #2d2c2b `light.color.ink.nav`.

![B2B card default](components/crops/org-card-default.png)

### Marketing chrome (mobile)

The header and its nav sheet as a phone draws them, at 390 x 844.

#### Mobile header
The bar at 390px: logo and the nav button. Read as `m-nav-header` on the home page.

**Values (default).** size 390 x 64; padding 0px 24px; background #ffffff `light.color.surface.header`; text Headspace Apercu 14/15.4 700, #ffffff `light.color.surface.header`.

![Mobile header default](components/crops/m-nav-header-default.png)

#### Nav button
The button that opens the nav sheet. Read as `m-nav-button` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 28 x 28; border 2px solid transparent; background transparent; text Headspace Apercu 16/17.6 700, #44423f `light.color.ink.muted`; transition color 0.15s cubic-bezier(0.32, 0.94, 0.6, 1), background-color 0.15s cubic-bezier(0.32, 0.94, 0.6, 1), border-color 0.15s cubic-bezier(0.32, 0.94, 0.6, 1), box-shadow 0.15s cubic-bezier(0.32, 0.94, 0.6, 1), transform 0.15s cubic-bezier(0.32, 0.94, 0.6, 1); icon 24 x 24, #44423f `light.color.ink.muted` |

![Nav button default](components/crops/m-nav-button-default.png) ![Nav button hover](components/crops/m-nav-button-hover.png)

#### Nav sheet (open)
The opened navigation sheet. The nav button's own press happens in find(); the state itself is a no-op. Read as `m-nav-sheet` on the home page.

Not on the page when it was captured.

### Marketing widgets (mobile)

The hero CTA at 390 wide.

#### Mobile hero CTA
The hero call-to-action at 390px, measured, never followed. Read as `m-hero-cta` on the home page.

**Values (default).** size 125 x 32.59; padding 14.3px 24px; border 2px solid transparent; radius 32px; background #0061ef `light.color.brand.blue`; shadow rgba(65, 61, 69, 0.2) 0px 2px 0px 0px; text Headspace Apercu 14/15.4 700, #ffffff `light.color.surface.header`; transition color 0.15s cubic-bezier(0.32, 0.94, 0.6, 1), background-color 0.15s cubic-bezier(0.32, 0.94, 0.6, 1), border-color 0.15s cubic-bezier(0.32, 0.94, 0.6, 1), box-shadow 0.15s cubic-bezier(0.32, 0.94, 0.6, 1), transform 0.15s cubic-bezier(0.32, 0.94, 0.6, 1).

![Mobile hero CTA default](components/crops/m-hero-cta-default.png)

## Icons

36 SVGs were lifted from the pages into [icons/](icons), named by role where the markup named them, with the source table in [icons/INDEX.tsv](icons/INDEX.tsv). Colour is `currentColor` wherever the icon took its colour from the text, so each recolours from CSS `color`. Marketing illustrations, photos and the OneTrust consent SVGs were left out; these are the interface icons. The SVGs are Headspace's property, kept for reference only.

| Icon | Rendered sizes | View box | Style | Seen on | Next to |
|---|---|---|---|---|---|
| [open-headspace-facebook](icons/open-headspace-facebook.svg) | 16x16 | 0 0 24 24 | fill | home; app; meditation; mindfulness; sleep; therapy; coaching; ebb; mental-health; science; about; articles; article; content; subscriptions; gift; share; redeem; mindful-families; login; signup; header; nav | Open Headspace Facebook / facebook / Facebook |
| [icon-5897a300](icons/icon-5897a300.svg) | 32x32 | 0 0 24 24 | fill | home; app; meditation; mindfulness; sleep; therapy; coaching; ebb; mental-health; science; about; articles; article; content; topic; subscriptions; gift; share; redeem; mindful-families; header; nav | Scroll to the top of the page |
| [open-headspace-twitter](icons/open-headspace-twitter.svg) | 16x16 | 0 0 24 24 | fill | home; app; meditation; mindfulness; sleep; therapy; coaching; ebb; mental-health; science; about; articles; article; content; subscriptions; gift; share; redeem; mindful-families; header; nav | Open Headspace Twitter / twitter |
| [english](icons/english-4558bdc0.svg) | 16x16 24x24 | 0 0 24 24 | fill | home; app; meditation; mindfulness; sleep; therapy; coaching; ebb; mental-health; science; about; articles; article; content; subscriptions; gift; share; redeem; mindful-families; header; nav | English |
| [english](icons/english-4e503953.svg) | 24x24 |  | fill | home; app; meditation; mindfulness; sleep; therapy; coaching; ebb; mental-health; science; about; articles; article; content; subscriptions; gift; share; redeem; mindful-families; header; nav | English |
| [open-headspace-youtube](icons/open-headspace-youtube.svg) | 16x16 | 0 0 24 24 | fill | home; app; meditation; mindfulness; sleep; therapy; coaching; ebb; mental-health; science; about; articles; article; content; subscriptions; gift; share; redeem; mindful-families; header; nav | Open Headspace Youtube |
| [open-headspace-instagram](icons/open-headspace-instagram.svg) | 16x16 | 0 0 24 24 | fill | home; app; meditation; mindfulness; sleep; therapy; coaching; ebb; mental-health; science; about; articles; article; content; subscriptions; gift; share; redeem; mindful-families; header; nav | Open Headspace Instagram |
| [open-headspace-linkedin](icons/open-headspace-linkedin.svg) | 16x16 | 0 0 24 24 | fill | home; app; meditation; mindfulness; sleep; therapy; coaching; ebb; mental-health; science; about; articles; article; content; subscriptions; gift; share; redeem; mindful-families; header; nav | Open Headspace Linkedin |
| [stress-less](icons/stress-less-7b8b9412.svg) | 14x14 16x16 24x24 29x29 | 0 0 24 24 | fill | home; app; meditation; mindfulness; about; articles; article; content; topic; subscriptions; share; header; nav | Stress less / Sleep soundly / Manage anxiety |
| [play-pause-audio](icons/play-pause-audio.svg) | 24x24 40x40 | 0 0 32 32 | fill | home; app; meditation; mindfulness; sleep; coaching; ebb; mental-health; articles; topic; subscriptions; header; nav | Play / Pause audio / Play / Pause '20-minute guided meditati |
| [previous-slide](icons/previous-slide-54c11b46.svg) | 16x16 24x24 29x29 | 0 0 24 24 | fill | home; app; meditation; mindfulness; about; article; content; topic; subscriptions; share; header; nav | Previous slide / Move back / Previous |
| [what-is-headspace](icons/what-is-headspace.svg) | 16x16 | 0 0 24 24 | fill | home; app; therapy; coaching; ebb; content; gift; header; nav | What is Headspace? / What is Headspace’s mission? / How do I |
| [icon-903b86b7](icons/icon-903b86b7.svg) | 16x16 24x24 | 0 0 16 16 | fill | meditation; mindfulness; sleep; mental-health; science; article; content; subscriptions; gift | Access the full library of 500+ meditati / Put your mind to  |
| [apple](icons/apple.svg) | 16x16 | 0 0 24 24 | fill | login; signup | Apple |
| [practice-meditation](icons/practice-meditation.svg) | 58x58 | 0 0 58 58 | fill | home; app | Practice meditation |
| [previous-slide](icons/previous-slide-5499893d.svg) | 20x14 38x14 | 0 0 10 15 | stroke | org-home; org-employers | Previous slide / previous slide |
| [continue-with-sso](icons/continue-with-sso.svg) | 24x24 | 0 0 24 24 | fill | login; signup | Continue with SSO |
| [google](icons/google.svg) | 16x16 | 0 0 256 262 | fill | login; signup | Google |
| [next-slide](icons/next-slide-7aeaa161.svg) | 20x14 38x14 | 0 0 10 15 | stroke | org-home; org-employers | Next slide / next slide |
| [sleep-soundly](icons/sleep-soundly.svg) | 58x58 | 0 0 58 58 | fill | home; app | Sleep soundly |
| [stress-less](icons/stress-less-9195bb4a.svg) | 58x58 | 0 0 58 58 | fill | home; app | Stress less |
| [spotify](icons/spotify.svg) | 16x16 | 0 0 24 24 | fill | login; signup | Spotify |
| [source](icons/source.svg) | 16x16 | 0 0 24 24 | fill | about; header | Source / Get started with therapy |
| [manage-anxiety](icons/manage-anxiety.svg) | 58x58 | 0 0 58 58 | fill | home; app | Manage anxiety |
| [next-slide](icons/next-slide-0ee54682.svg) | 24x24 | 0 0 21 36 | stroke | org-home | Next slide |
| [pause](icons/pause.svg) | 27x27 | 0 0 32 32 | fill | content | pause |
| [icon-23f7f106](icons/icon-23f7f106.svg) | 16x16 | 0 0 16 16 | fill | topic | Breathe in Relaxation Mindful Activity • |
| [previous-slide](icons/previous-slide-492209bf.svg) | 24x24 | 0 0 22 35 | stroke | org-home | Previous slide |
| [icon-4bb1fa23](icons/icon-4bb1fa23.svg) | 24x24 | 0 0 24 24 | fill | share | Who can use the sharing feature? / Where can I find the abil |
| [icon-5b0a2d2e](icons/icon-5b0a2d2e.svg) | 24x24 | 0 0 24 24 | fill | family | Who is eligible to join Headspace Family |
| [icon-603f8c2d](icons/icon-603f8c2d.svg) | 28x28 | 0 0 24 24 | fill | nav |  |
| [back-to-explore](icons/back-to-explore.svg) | 16x16 | 0 0 24 24 | fill | topic | Back to explore |
| [icon-aefbd31f](icons/icon-aefbd31f.svg) | 16x16 | 0 0 18 18 | fill | article |  |
| [icon-b9fda43f](icons/icon-b9fda43f.svg) | 16x16 | 0 0 16 16 | fill | topic | Focus Timer: Mt. Fuji Session • 148 min  / Summer Jam Harves |
| [icon-d2d0a0c6](icons/icon-d2d0a0c6.svg) | 24x24 | 0 0 24 24 | fill | nav |  |
| [icon-e91dcd85](icons/icon-e91dcd85.svg) | 24x24 | 0 0 24 24 | fill | family | Can I join a Headspace Family Plan if I  / How does payment  |

## Gaps

### Pages

- **Signed-in pages.** Everything behind auth.headspace.com is out of scope: the member home, the meditation and sleep players, streaks and progress, account settings, the /app member experience. The kit never signs in.
- **Anything that sends or creates.** No form was submitted anywhere: no login or signup completed, no newsletter joined, no code redeemed on /code, no gift sent, no guest pass claimed, no plan bought on checkout, no trial started. Validation, error, loading and success states are absent rather than measured.
- **/pricing is a 404.** Headspace serves its own 'Whoops! Something's changed' page there; the plans live on /subscriptions. Recorded as an absence, not a capture.
- **The checkout's inner form.** checkout.headspace.com paints a plan summary and fields on arrival; its inputs were never focused, filled or submitted, and the checkout component specs read absent on this pass.
- **The OneTrust consent layer.** Its banner and preferences were set `display: none` for every capture; no consent state was chosen and the UI is intentionally absent.

### States

- **Pressed** was forced with DevTools, so a state a script adds on mousedown (if any) is missing.
- **The mobile nav sheet** did not match the measurement spec on the phone pass (the drawer was screenshot but the `m-nav-sheet` component read absent); its values come from the screenshot, not a table.
- **Thirteen component specs read absent** on this pass - the feature and testimonial cards, the FAQ accordion, the content tiles and play button, the plan card and billing switch, the checkout pieces, the footer language selector and app badges - recorded as missing, not measured.
- **Disabled states** were not seen on any public control.

### Themes

Headspace shows one light theme on every signed-out surface. There is no theme control, no dark attribute and no applied `prefers-color-scheme: dark` rule on any captured page; the motion probe's media checks found the same (`raw/css-vars.json`, `raw/motion.json`). The token file ships no dark set.

### Fonts

- **Headspace Apercu** (weights 200/400/600/700) and **Apercu Pro Mono** are licensed faces served from the site's own CDN; they are not shipped in the package, and the style guide falls back to system sans.

### Screenshots

- Illustrations, photos, device mocks and article art are Headspace's content and appear only inside screenshots and crops.
- `-full` screenshots capture the real scrollable area: where a page's content overflows horizontally the PNG is wider than the 1440 viewport (the home and topic pages reach ~6900px and ~8200px wide), and pages taller than 8 tiles truncate from the bottom. Sidecars record the document size.
- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files.

### Content left out

- Marketing copy, article text and session content were not transcribed; only the frames around them were measured.
- No personal data was captured: every page was read signed out with fields left empty.
