# Linktree components

The discovery list of every page and view captured, then one entry per component with crops of the real product, and the Gaps. Captured from linktr.ee on 2026-11-18, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running page. Nothing was signed into, claimed, sent or purchased.

The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) (33 components, 79 states).

How to read an entry:

- A colour is its value followed by the palette token in [tokens.json](tokens.json) with the same value, when there is one. Text is written family size/line-height weight, then its colour, for example `Inter 14/21 500, #111827`, and is read from the first text node inside the component.
- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example "default (same: focus-visible)". When the root paints nothing, "Child layers" names the first nodes inside it that do.
- Crops are images of the component read from the live page, in [components/crops/](components/crops) (78 files, named `{component}-{state}.png`, at 2x). Screenshots are in [screenshots/](screenshots).

## Discovery list

Screenshots are named `{page}-light-{state}.png`: the site paints one light theme. Desktop shots are 1440 x 900 at 1x; `-full` shots are whole pages (1x on desktop, 2x on mobile); mobile shots are `mobile-{page}-light-{state}.png`, 780 wide (390 at 2x).

| Surface | URL | Screenshots |
|---|---|---|
| Home | `/` | [default](screenshots/home-light-default.png), [solutions menu](screenshots/home-light-solutions-menu.png), [claim focused](screenshots/home-light-claim-focused.png), [FAQ open](screenshots/home-light-faq-open.png). The full-page shot was not committed: it shows public profile usernames. |
| About | `/about` | [default](screenshots/about-light-default.png), [full](screenshots/about-light-full.png) |
| Features | `/features` | [default](screenshots/features-light-default.png), [full](screenshots/features-light-full.png) |
| Pricing | `/s/pricing` | [default](screenshots/pricing-light-default.png), [full](screenshots/pricing-light-full.png) |
| Public profile | `/linktr.ee` | [default](screenshots/profile-light-default.png), [full](screenshots/profile-light-full.png) |
| Home, phone | `/` | [default](screenshots/mobile-home-light-default.png), [menu-open](screenshots/mobile-home-light-menu-open.png). The full-page shot was not committed: it shows public profile usernames. |
| Pricing, phone | `/s/pricing` | [default](screenshots/mobile-pricing-light-default.png), [full](screenshots/mobile-pricing-light-full.png) |
| Profile, phone | `/linktr.ee` | [default](screenshots/mobile-profile-light-default.png), [full](screenshots/mobile-profile-light-full.png) |

### Overlays and transient states

The desktop Solutions menu and the mobile menu were opened and closed. Consent overlays were hidden, never clicked. The login wall was measured and not submitted. No share sheet was sent.

## Shared values

Values that apply across entries, from the measurement files.

**Focus.** 11 components were given a real keyboard focus (a further 1 could not be driven: `login-continue`). 11 show a visible focus state: `nav-link` (visible change in backgroundColor), `nav-login` (visible change in boxShadow), `nav-signup` (visible change in boxShadow), `nav-menu` (visible change in backgroundColor), `hero-cta` (visible change in boxShadow), `claim-submit` (visible change in boxShadow), `footer-link` (1px auto #005fcc, offset 1px), `plan-select` (1px auto #005fcc, offset 1px), `profile-share` (1px auto #005fcc, offset 0px), `profile-tab` (1px auto #005fcc, offset 0px), `m-menu` (1px auto #e59700, offset 0px).

**Pressed.** Forced with DevTools (`CSS.forcePseudoState` :active:hover). Nothing a real press would submit, follow or purchase was ever pressed.

**Motion.** Transitions measured on the components, by duration.

| Duration | Easing | Property | Where |
|---|---|---|---|
| 0.075s | `cubic-bezier(0, 0, 0.2, 1)` | -webkit-backdrop-filter, backdrop-filter, background-color, border-color, box-shadow, color, fill, filter, opacity, stroke, text-decoration-color, transform | login-field |
| 0.15s | `cubic-bezier(0, 0, 0.2, 1)` | background-color, box-shadow, filter, transform | claim-submit, hero-cta, m-signup, nav-login, nav-signup |
| 0.15s | `cubic-bezier(0.4, 0, 0.2, 1)` | --tw-gradient-from, --tw-gradient-to, --tw-gradient-via, -webkit-backdrop-filter, all, backdrop-filter, background-color, border-color, box-shadow, color, fill, filter, opacity, outline-color, stroke, text-decoration-color, transform | claim-field, claim-wrap, footer-link, login-continue, login-google, login-signup, m-menu-panel, nav-link and more |
| 0.2s | `cubic-bezier(0.4, 0, 0.2, 1)` | --tw-gradient-from, --tw-gradient-to, --tw-gradient-via, background-color, border-color, color, fill, outline-color, stroke, text-decoration-color | m-menu |
| 0.3s | `cubic-bezier(0, 0, 0.2, 1)` | rotate, scale, transform, translate | m-navbar, navbar |

**Card shapes.** Default-state values; the entries hold the states.

| Card | Size | Border | Radius | Background | Shadow | Padding |
|---|---|---|---|---|---|---|
| [Sign up free pill](#sign-up-free-pill) | 152.08 x 62 | - | 9999px | #1e2330 `color.shade` | none | 0px 26px |
| [Get started for free](#get-started-for-free) | 300 x 60 | - | 9999px | #254f1a `color.forest` | none | 0px 36px |
| [Try free for 7 days](#try-free-for-7-days) | 336 x 48 | - | 9999px | #7f22fe | none | 0px 24px |
| [Profile link card](#profile-link-card) | 394.86 x 64 | - | - | transparent | none | 0 |
| [Claim field shell](#claim-field-shell) | 290.39 x 60 | - | 8px | #ffffff `color.white` | none | 8px 16px |

## Components

### Shell and navigation

The marketing nav: text links, the Sign up free pill, and the Solutions disclosure.

#### Top navigation
The marketing nav: Solutions, Features, Integrations, Resources, Pricing, Log in, and the Sign up free pill. Read as `navbar` on the home page.

**Values (default).** size 1440 x 138; background transparent; text Linksans 16/20.8 400, #1e2330 `color.shade`; transition transform 0.3s cubic-bezier(0, 0, 0.2, 1), translate 0.3s cubic-bezier(0, 0, 0.2, 1), scale 0.3s cubic-bezier(0, 0, 0.2, 1), rotate 0.3s cubic-bezier(0, 0, 0.2, 1); icon 118 x 28, #000000 `color.black`.

Child layers that carry the look: div 1296x90 background #ffffff `color.white` border 1px solid rgba(0, 0, 0, 0.08) radius 9999px; div 1294x2 background #ffffff `color.white` border 1px solid rgba(0, 0, 0, 0.04) radius 36px shadow transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, rgba(0, 0, 0, 0.08) 0px 24px 60px 0px; li 0x0 background #eff0ec radius 16px.

![Top navigation default](components/crops/navbar-default.png)

#### Nav link
The Pricing text link in the bar. Measured, never followed. Read as `nav-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 86.16 x 48; padding 0px 16px; radius 16px; background transparent; text Linksans 16/20.8 400, #1e2330 `color.shade`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| focus-visible | background #eff0ec |

![Nav link default](components/crops/nav-link-default.png) ![Nav link hover](components/crops/nav-link-hover.png) ![Nav link focus-visible](components/crops/nav-link-focus-visible.png) ![Nav link pressed](components/crops/nav-link-pressed.png)

#### Log in link
The quiet Log in link. Measured, never followed. The login wall itself is a separate signed-out page. Read as `nav-login` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 101.53 x 62; padding 0px 26px; radius 16px; background transparent; text Linksans 16/24 400, #1e2330 `color.shade`; transition background-color 0.15s cubic-bezier(0, 0, 0.2, 1), transform 0.15s cubic-bezier(0, 0, 0.2, 1) |
| hover | background #eff0ec |
| focus-visible | shadow #ffffff 0px 0px 0px 2px, #1e2330 0px 0px 0px 4px |
| pressed | background #eff0ec |

![Log in link default](components/crops/nav-login-default.png) ![Log in link hover](components/crops/nav-login-hover.png) ![Log in link focus-visible](components/crops/nav-login-focus-visible.png) ![Log in link pressed](components/crops/nav-login-pressed.png)

#### Sign up free pill
The ink pill in the bar. Measured, never followed. Read as `nav-signup` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 152.08 x 62; padding 0px 26px; radius 9999px; background #1e2330 `color.shade`; text Linksans 16/24 400, #ffffff `color.white`; transition background-color 0.15s cubic-bezier(0, 0, 0.2, 1), transform 0.15s cubic-bezier(0, 0, 0.2, 1) |
| hover | background #262d3e |
| focus-visible | shadow #ffffff 0px 0px 0px 2px, #1e2330 0px 0px 0px 4px |
| pressed | background #262d3e |

![Sign up free pill default](components/crops/nav-signup-default.png) ![Sign up free pill hover](components/crops/nav-signup-hover.png) ![Sign up free pill focus-visible](components/crops/nav-signup-focus-visible.png) ![Sign up free pill pressed](components/crops/nav-signup-pressed.png)

#### Nav menu button
The Solutions disclosure. Opened only to record the menu panel; nothing inside was followed. Read as `nav-menu` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 106.11 x 48; padding 0px 16px; radius 16px; background transparent; text Linksans 16/20.8 400, #1e2330 `color.shade`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| focus-visible | background #eff0ec |

![Nav menu button default](components/crops/nav-menu-default.png) ![Nav menu button hover](components/crops/nav-menu-hover.png) ![Nav menu button focus-visible](components/crops/nav-menu-focus-visible.png) ![Nav menu button pressed](components/crops/nav-menu-pressed.png)

#### Nav menu item
A Solutions menu item, captured after the disclosure is opened. The item has no box until the menu opens. Measured, never followed. Read as `nav-menu-panel` on the home page.

**Values (opened).** size 319 x 48; radius 16px; background transparent; text Linksans 16/20.8 400, #1e2330 `color.shade`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 24 x 24, #1e2330 `color.shade`.

![Nav menu item opened](components/crops/nav-menu-panel-opened.png)

### Home

The hero, the claim field, and the footer.

#### Hero title
"A link in bio built for you." in Linksans. Read as `hero-title` on the home page.

**Values (default).** size 616 x 171.19; background transparent; text Linksans 80/85.6 800, #254f1a `color.forest`.

![Hero title default](components/crops/hero-title-default.png)

#### Get started for free
The hero claim CTA. Measured, never followed and never submitted. Read as `hero-cta` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 300 x 60; padding 0px 36px; radius 9999px; background #254f1a `color.forest`; text Linksans 16/24 500, #f3f3f1 `color.marble`; transition background-color 0.15s cubic-bezier(0, 0, 0.2, 1), transform 0.15s cubic-bezier(0, 0, 0.2, 1), filter 0.15s cubic-bezier(0, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0, 0, 0.2, 1) |
| focus-visible | shadow #ffffff 0px 0px 0px 2px, #1e2330 0px 0px 0px 4px |
| pressed | size 291 x 58.2; transition background-color 0.08s cubic-bezier(0, 0, 0.2, 1), transform 0.08s cubic-bezier(0, 0, 0.2, 1), filter 0.08s cubic-bezier(0, 0, 0.2, 1), box-shadow 0.08s cubic-bezier(0, 0, 0.2, 1) |

![Get started for free default](components/crops/hero-cta-default.png) ![Get started for free hover](components/crops/hero-cta-hover.png) ![Get started for free focus-visible](components/crops/hero-cta-focus-visible.png) ![Get started for free pressed](components/crops/hero-cta-pressed.png)

#### Claim username field
The linktr.ee/yourname field on the marketing page. A throwaway string was typed and deleted. The form was not submitted. Read as `claim-field` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 290.39 x 60; padding 8px 16px; radius 8px; background #ffffff `color.white`; text Linksans 16/24 500, #757575; transition all 0.15s cubic-bezier(0.4, 0, 0.2, 1); placeholder oklab(0.562378 0.0000257194 0.0000112355 / 0.5) |
| focused, filled | outline 2px solid #ffffff `color.white`, offset 2px |

![Claim username field default](components/crops/claim-field-default.png) ![Claim username field focused](components/crops/claim-field-focused.png) ![Claim username field filled](components/crops/claim-field-filled.png)

#### Claim field shell
The painted shell around the claim field. Read as `claim-wrap` on the home page.

**Values (default).** size 290.39 x 60; padding 8px 16px; radius 8px; background #ffffff `color.white`; text Linksans 16/24 500, #757575; transition all 0.15s cubic-bezier(0.4, 0, 0.2, 1); placeholder oklab(0.562378 0.0000257194 0.0000112355 / 0.5).

![Claim field shell default](components/crops/claim-wrap-default.png)

#### Claim your Linktree
The claim button beside the field. Measured, never pressed for real. Read as `claim-submit` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 300 x 60; padding 0px 36px; radius 9999px; background #d2e823 `color.chartreuse`; text Linksans 16/24 500, #1e2330 `color.shade`; transition background-color 0.15s cubic-bezier(0, 0, 0.2, 1), transform 0.15s cubic-bezier(0, 0, 0.2, 1), filter 0.15s cubic-bezier(0, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0, 0, 0.2, 1) |
| focus-visible | shadow #ffffff 0px 0px 0px 2px, #1e2330 0px 0px 0px 4px |
| pressed | size 291 x 58.2; transition background-color 0.08s cubic-bezier(0, 0, 0.2, 1), transform 0.08s cubic-bezier(0, 0, 0.2, 1), filter 0.08s cubic-bezier(0, 0, 0.2, 1), box-shadow 0.08s cubic-bezier(0, 0, 0.2, 1) |

![Claim your Linktree default](components/crops/claim-submit-default.png) ![Claim your Linktree hover](components/crops/claim-submit-hover.png) ![Claim your Linktree focus-visible](components/crops/claim-submit-focus-visible.png) ![Claim your Linktree pressed](components/crops/claim-submit-pressed.png)

#### Footer
The purple footer band with the claim field repeated and the product columns. Read as `footer` on the home page.

**Values (default).** size 1440 x 1667.45; padding 250px 0px 32px 0px; background #502274 `color.dahlia`; text Linksans 56/59.36 700, #e9c0e9 `color.lavender`; icon 36 x 26, #1e2330 `color.shade`.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Footer link
A company-column link. Measured, never followed. Read as `footer-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 39.14 x 19.5; background transparent; text Linksans 13/19.5 400, #676b5f; transition opacity 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | opacity 0.7 |
| focus-visible | outline 1px auto #005fcc, offset 1px |
| pressed | opacity 0.7 |

![Footer link default](components/crops/footer-link-default.png) ![Footer link hover](components/crops/footer-link-hover.png) ![Footer link focus-visible](components/crops/footer-link-focus-visible.png) ![Footer link pressed](components/crops/footer-link-pressed.png)

### Pricing

Public plan names and Select buttons. Nothing was added to a cart.

#### Pricing title
Read as `pricing-title` on the pricing page.

**Values (default).** size 706.42 x 52.8; background transparent; text Linksans 48/52.8 800, #000000 `color.black`.

![Pricing title default](components/crops/pricing-title-default.png)

#### Plan name
The Pro plan heading on the public pricing page. Selecting a plan was never clicked. Read as `plan-card` on the pricing page.

**Values (default).** size 64.66 x 36; background transparent; wrapper div.relative.flex: shadow rgba(0, 0, 0, 0.12) 0px 16px 32px 4px; text Linksans 36/36 800, #7008e7.

![Plan name default](components/crops/plan-card-default.png)

#### Try free for 7 days
The Pro plan link. Measured, never followed. Checkout was not opened. Read as `plan-select` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 336 x 48; padding 0px 24px; radius 9999px; background #7f22fe; wrapper div.relative.flex: shadow rgba(0, 0, 0, 0.12) 0px 16px 32px 4px; text Linksans 16/16 400, #ffffff `color.white`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | background #7008e7 |
| focus-visible | outline 1px auto #005fcc, offset 1px |
| pressed | background #7008e7 |

![Try free for 7 days default](components/crops/plan-select-default.png) ![Try free for 7 days hover](components/crops/plan-select-hover.png) ![Try free for 7 days focus-visible](components/crops/plan-select-focus-visible.png) ![Try free for 7 days pressed](components/crops/plan-select-pressed.png)

#### Get started
The free-plan link on the pricing page. Measured, never followed. Read as `plan-free` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 336 x 48; padding 0px 24px; border 1px solid rgba(4, 4, 3, 0.14); radius 9999px; background #ffffff `color.white`; wrapper div.relative.flex: shadow rgba(0, 0, 0, 0.02) 0px 0px 0px 1px, rgba(0, 0, 0, 0.02) 0px 1px 2px 0px, rgba(0, 0, 0, 0.05) 0px 8px 32px 0px; text Linksans 16/16 400, rgba(4, 4, 3, 0.9); transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | background #f7f7f7 |

![Get started default](components/crops/plan-free-default.png) ![Get started hover](components/crops/plan-free-hover.png)

### Public profile

The official linktr.ee profile, loaded signed out.

#### Profile name
The public Linktree profile title (the official linktr.ee page). Read as `profile-title` on the the public profile page.

**Values (default).** size 95.25 x 33; background transparent; text Link Sans Product 24/28.8 600, #040212.

![Profile name default](components/crops/profile-title-default.png)

#### Share profile
The share icon button on a public profile. Its name is an aria-label. Measured, never pressed, so no share sheet was sent. Read as `profile-share` on the the public profile page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 40 x 40; padding 0px 10px; background transparent; wrapper div.relative.flex: outline 1px solid rgba(255, 255, 255, 0.4); text Link Sans Product 16/16 400, #000000 `color.black`; icon 20 x 20, #000000 `color.black` |
| focus-visible | outline 1px auto #005fcc, offset 0px |

![Share profile default](components/crops/profile-share-default.png) ![Share profile hover](components/crops/profile-share-hover.png) ![Share profile focus-visible](components/crops/profile-share-focus-visible.png) ![Share profile pressed](components/crops/profile-share-pressed.png)

#### Profile tab
The Links tab on the public profile. Read as `profile-tab` on the the public profile page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 93.86 x 48; radius 64px; background transparent; text Link Sans Product 16/24 500, #000000 `color.black`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), opacity 0.15s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1), transform 0.15s cubic-bezier(0.4, 0, 0.2, 1), filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), -webkit-backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| focus-visible | outline 1px auto #005fcc, offset 0px |

![Profile tab default](components/crops/profile-tab-default.png) ![Profile tab hover](components/crops/profile-tab-hover.png) ![Profile tab focus-visible](components/crops/profile-tab-focus-visible.png) ![Profile tab pressed](components/crops/profile-tab-pressed.png)

#### Shop tab
The unselected Shop tab. Not selected, so the page content was not swapped. Read as `profile-tab-shop` on the the public profile page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 94.16 x 48; radius 64px; background transparent; text Link Sans Product 16/24 500, #ffffff `color.white`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), opacity 0.15s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1), transform 0.15s cubic-bezier(0.4, 0, 0.2, 1), filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), -webkit-backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1) |

![Shop tab default](components/crops/profile-tab-shop-default.png) ![Shop tab hover](components/crops/profile-tab-shop-hover.png) ![Shop tab pressed](components/crops/profile-tab-shop-pressed.png)

#### Social icon button
A social icon on the public profile. Measured, never followed. Read as `profile-social` on the the public profile page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 48 x 48; padding 8px; background rgba(255, 255, 255, 0); text Link Sans Product 16/16 400, #000000 `color.black`; transition transform 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 32 x 32, #040212 |
| hover | size 51.6 x 51.6; transform scale(1.075); icon 34.4 x 34.4, #040212 |

![Social icon button default](components/crops/profile-social-default.png) ![Social icon button hover](components/crops/profile-social-hover.png)

#### Profile link card
A published link card on the official profile. Measured, never followed. Read as `profile-link` on the the public profile page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 394.86 x 64; background transparent; wrapper div.LinkContainer_LinkContainer__Kk5IQ.grid: shadow #000000 3px 4px 0px 0px; text Link Sans Product 16/16 400, #14160e |
| hover | wrapper div.LinkContainer_LinkContainer__Kk5IQ.grid: shadow #000000 4px 5px 0px 0px |

![Profile link card default](components/crops/profile-link-default.png) ![Profile link card hover](components/crops/profile-link-hover.png)

#### Verified badge
The verified badge on the official profile. Read as `profile-badge` on the the public profile page.

**Values (default).** size 62.2 x 24; background transparent; text Link Sans Product 12/18 400, rgba(0, 0, 0, 0.75).

![Verified badge default](components/crops/profile-badge-default.png)

### Sign-in wall (not submitted)

The login page as a signed-out wall. The form was not submitted.

#### Login title
The signed-out login wall. Nothing was submitted. Read as `login-title` on the the signed-out login wall page.

**Values (default).** size 720 x 36; background transparent; text Link Sans Display 32/36 800, #000000 `color.black`.

![Login title default](components/crops/login-title-default.png)

#### Login field
The email or username field. Focused only. Nothing was typed and the form was not submitted. Read as `login-field` on the the signed-out login wall page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 478 x 54.84; padding 24px 16px 8px 16px; background transparent; outline 2px solid transparent, offset 2px; text Link Sans Product 16/22.85 400, rgba(4, 4, 3, 0.898); transition color 0.075s cubic-bezier(0, 0, 0.2, 1), background-color 0.075s cubic-bezier(0, 0, 0.2, 1), border-color 0.075s cubic-bezier(0, 0, 0.2, 1), text-decoration-color 0.075s cubic-bezier(0, 0, 0.2, 1), fill 0.075s cubic-bezier(0, 0, 0.2, 1), stroke 0.075s cubic-bezier(0, 0, 0.2, 1), opacity 0.075s cubic-bezier(0, 0, 0.2, 1), box-shadow 0.075s cubic-bezier(0, 0, 0.2, 1), transform 0.075s cubic-bezier(0, 0, 0.2, 1), filter 0.075s cubic-bezier(0, 0, 0.2, 1), -webkit-backdrop-filter 0.075s cubic-bezier(0, 0, 0.2, 1), backdrop-filter 0.075s cubic-bezier(0, 0, 0.2, 1); placeholder transparent |
| focused | wrapper div.group/field.relative: shadow #fbfaf9 0px 0px 0px 0px, rgba(4, 4, 3, 0.898) 0px 0px 0px 2px |

Child layers that carry the look: input 478x54.8.

![Login field default](components/crops/login-field-default.png) ![Login field focused](components/crops/login-field-focused.png)

#### Continue
The primary continue button. Measured, never pressed. Read as `login-continue` on the the signed-out login wall page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 480 x 56; padding 0px 20px; radius 9999px; background #e5e4e1; text Link Sans Product 16/24 500, rgba(4, 4, 3, 0.18); transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| pressed | size 470.4 x 54.88; transform scale(0.98) |

Focus could not be captured: keyboard focus never landed on this element, so `focus-visible` is the element at rest and is left out of the table.

![Continue default](components/crops/login-continue-default.png) ![Continue hover](components/crops/login-continue-hover.png) ![Continue pressed](components/crops/login-continue-pressed.png)

#### Continue with Google
The Google button on the signed-out wall. Measured, never pressed. Read as `login-google` on the the signed-out login wall page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 480 x 56; padding 0px 20px; border 1px solid rgba(4, 4, 3, 0.14); radius 9999px; background transparent; text Link Sans Product 16/24 500, rgba(4, 4, 3, 0.898); transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 24 x 24, rgba(4, 4, 3, 0.898) |
| hover | background rgba(4, 4, 3, 0.05) |

![Continue with Google default](components/crops/login-google-default.png) ![Continue with Google hover](components/crops/login-google-hover.png)

#### Sign up link
The sign-up link on the login wall. Measured, never followed. Read as `login-signup` on the the signed-out login wall page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 51.69 x 19.98; background transparent; text Link Sans Product 14/20 400, #7008e7; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1) |

![Sign up link default](components/crops/login-signup-default.png) ![Sign up link hover](components/crops/login-signup-hover.png)

### Mobile (390 wide)

The marketing nav at 390 wide, including the opened menu.

#### Mobile nav
The marketing nav at 390 wide, with the menu toggle. Read as `m-navbar` on the home page at 390 wide.

**Values (default).** size 390 x 89.22; background transparent; text Linksans 11.7/17.55 400, #1e2330 `color.shade`; transition transform 0.3s cubic-bezier(0, 0, 0.2, 1), translate 0.3s cubic-bezier(0, 0, 0.2, 1), scale 0.3s cubic-bezier(0, 0, 0.2, 1), rotate 0.3s cubic-bezier(0, 0, 0.2, 1).

Child layers that carry the look: div 362.7x65.8 background #ffffff `color.white` border 1px solid rgba(0, 0, 0, 0.08) radius 9999px; div 0x0 background #ffffff `color.white` border 1px solid rgba(0, 0, 0, 0.04) radius 9.75px shadow transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, rgba(0, 0, 0, 0.08) 0px 24px 60px 0px; a 73.3x46.4 background #eff0ec radius 7.8px.

![Mobile nav default](components/crops/m-navbar-default.png)

#### Menu toggle
The mobile menu button. Its name is an aria-label. Opened once for the menu link. Read as `m-menu` on the home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 48.23 x 48.23; radius 9999px; background transparent; text Linksans 16/24 400, #1e2330 `color.shade`; transition color 0.2s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), fill 0.2s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.2s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.2s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.2s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.2s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | background #eff0ec |
| focus-visible | outline 1px auto #e59700, offset 0px |
| pressed | background #eff0ec |

Child layers that carry the look: span 16x1.5 background #1e2330 `color.shade` radius 3.35544e+07px; span 16x1.5 background #1e2330 `color.shade` radius 3.35544e+07px; span 16x1.5 background #1e2330 `color.shade` radius 3.35544e+07px.

![Menu toggle default](components/crops/m-menu-default.png) ![Menu toggle hover](components/crops/m-menu-hover.png) ![Menu toggle focus-visible](components/crops/m-menu-focus-visible.png) ![Menu toggle pressed](components/crops/m-menu-pressed.png)

#### Mobile signup
The signup control at 390 wide. Measured, never followed. Read as `m-signup` on the home page at 390 wide.

**Values (default).** size 110.22 x 46.39; padding 13.689px 18.525px 15.171px 18.525px; radius 9999px; background #1e2330 `color.shade`; text Linksans 11.7/17.55 400, #ffffff `color.white`; transition background-color 0.15s cubic-bezier(0, 0, 0.2, 1), transform 0.15s cubic-bezier(0, 0, 0.2, 1).

![Mobile signup default](components/crops/m-signup-default.png)

#### Mobile menu link
A link inside the opened mobile menu. Measured, never followed. Read as `m-menu-panel` on the home page at 390 wide.

**Values (opened).** size 390 x 64; padding 20px 16px; background transparent; text Linksans 20/24 500, #1e2330 `color.shade`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 16 x 16, #a8a29e.

![Mobile menu link opened](components/crops/m-menu-panel-opened.png)

## Icons

No standalone SVG icon set was lifted on this pass. Social glyphs and the wordmark stay in the crops and screenshots. Declared under layoutGaps in the catalog entry.

| Icon | Rendered sizes | View box | Style | Seen on | Next to |
|---|---|---|---|---|---|

## Gaps

### Pages

- **Admin and analytics sit behind sign-in.** The editor, dashboard, analytics and billing were never reached. The login wall was measured and not submitted.
- **Nothing was claimed or purchased.** The claim field was filled with a throwaway string and cleared. Select plan, Continue, and share were measured, never pressed for real.

### States

- **Pressed** was forced with DevTools, so a state a script adds only on a real mousedown is missing.
- **Disabled, error and loading states** were not seen on the public surface. A validation error would require submitting a form, which this capture does not do.

### Themes

The captured public routes paint one light theme. A dark class on a probe document does not change the resolved Tailwind palette, and no theme switch was used.

### Fonts

- **Linksans** is the measured family on the marketing type. The font files are not committed.
- The wordmark and illustrations in the screenshots are Linktree's property.

### Screenshots

- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files.

### Content left out

- Profile photography and published link titles on the official profile are Linktree's public content. Private account titles were not captured.
