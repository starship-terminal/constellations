# Endless Tools components

The discovery list of every page and view captured, then one entry per component with crops of the real product and the Gaps. Captured from endlesstools.io and app.endlesstools.io on 2026-11-13, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running page. Nothing was signed into, created, sent or submitted.

The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) (54 components, 117 states).

How to read an entry:

- A colour is its value followed by the palette token in [tokens.json](tokens.json) with the same value, when there is one. Text is written family size/line-height weight, then its colour, for example `Inter 12/14 500, #959595`, and is read from the first text node inside the component.
- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example "default (same: focus-visible)". When the root paints nothing, "Child layers" names the first nodes inside it that do.
- Crops are images of the component read from the live page, in [components/crops/](components/crops) (116 files, named `{component}-{state}.png`). Screenshots are in [screenshots/](screenshots).

## Discovery list

Screenshots are named `{page}-dark-{state}.png` (every surface paints one dark theme). Desktop shots are 1440 x 900 at 1x; `-full` shots are whole pages at 1x; mobile shots are `mobile-{page}-dark-{state}.png`, 780 wide (390 at 2x).

| Surface | URL | Screenshots |
|---|---|---|
| Marketing one-pager. Header, hero, asset strip, statement sections, pricing, testimonials, newsletter, footer. Default, the Monthly billing toggle and the full page. | `https://endlesstools.io/` | [default](screenshots/home-dark-default.png), [full](screenshots/home-dark-full.png), [monthly](screenshots/home-dark-monthly.png) |
| App-host login card. OTP email form default and the password form behind 'Log in with password'. | `https://app.endlesstools.io/login` | [default](screenshots/login-dark-default.png), [password](screenshots/login-dark-password.png) |
| Privacy policy document page. Header and the full page. | `https://app.endlesstools.io/legal/privacy_policy` | [default](screenshots/privacy-dark-default.png), [full](screenshots/privacy-dark-full.png) |
| Terms & conditions document page. Header and the full page. | `https://app.endlesstools.io/legal/terms_of_use` | [default](screenshots/terms-dark-default.png), [full](screenshots/terms-dark-full.png) |
| Marketing page at 390: hero, asset cards, plan cards, the full page. | `https://endlesstools.io/` | [default](screenshots/mobile-home-dark-default.png), [full](screenshots/mobile-home-dark-full.png) |
| Login card at 390. | `https://app.endlesstools.io/login` | [default](screenshots/mobile-login-dark-default.png) |

### Overlays and transient states

| State | Where | How it was reached | Captured |
|---|---|---|---|
| Monthly billing toggle | pricing section | the Monthly pill flipped and flipped back (a local UI toggle, nothing bought) | [home-dark-monthly](screenshots/home-dark-monthly.png), [billing-monthly](#billing-toggle), [billing-yearly](#billing-toggle) |
| Password login form | app /login | the 'Log in with password' switch (a local toggle; the form was never filled or sent) | [login-dark-password](screenshots/login-dark-password.png), [login-password-field](#password-field), [login-submit](#log-in-button) |
| Newsletter consent, selected | newsletter band | the consent checkbox ticked for measurement, then left as found; the form was never submitted | [news-consent](#consent-checkbox) selected crop |

## Shared values

Values that apply across entries, from the measurement files.

**Focus.** 18 controls were given a real keyboard focus. 12 show the browser's own ring, a 1px `auto` outline (Chrome reports its colour as #005fcc `accent.focus`, the UA default, which the product does not paint): `nav-login` (offset 1px), `nav-cta` (offset 1px), `hero-cta` (offset 1px), `billing-monthly` (offset 0px), `plan-cta` (offset 1px), `team-cta` (offset 1px), `edu-cta` (offset 1px), `carousel-prev` (offset 0px), `news-submit` (offset 0px), `footer-link` (offset 1px), `social-link` (offset 1px), `m-cta` (offset 0px). 6 keep Tailwind's preset `outline: 2px solid transparent` and show no measured change, so a keyboard user sees no ring: `send-code`, `login-switch`, `login-submit`, `login-forgot`, `legal-signin`, `legal-link`. Focus could not be captured on `billing-yearly` (keyboard focus did not reach the element), so its look is unknown, not absent.

**Pressed.** Pressed states were forced with DevTools (`:active:hover`), so no button was ever clicked through. Pressed paints the same colour as hover on every control — the page's own press cue is `active:scale-95` (a 0.95 shrink) declared in the sheets, which a forced pseudo-state does not show.

**Motion.** Transitions measured on the components, by duration.

| Duration | Easing | Property | Where |
|---|---|---|---|
| 0.15s | `cubic-bezier(0.4, 0, 0.2, 1)` | --tw-gradient-from, --tw-gradient-to, --tw-gradient-via, -webkit-backdrop-filter, backdrop-filter, background-color, border-color, box-shadow, color, fill, filter, opacity, outline-color, rotate, scale, stroke, text-decoration-color, transform, translate | billing-monthly, billing-yearly, carousel-prev, edu-cta, footer-link, hero-cta, legal-signin, login-field and more |

**Card shapes.** Default-state values; the entries hold the states.

| Card | Size | Border | Radius | Background | Shadow | Padding |
|---|---|---|---|---|---|---|
| [Plan card](#plan-card) | 356.66 x 562 | - | 33px | #121212 `neutral.card` | #222222 0px 0px 0px 1px inset | 15px |
| [Login card](#login-card) | 450 x 497 | - | 20px | rgba(239, 239, 239, 0.05) `neutral.alpha.veil-5` | none | 50px |
| [Floating promo card](#floating-promo-card) | 365.58 x 54 | - | 3.35544e+07px | - | transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, oklab(0.999994 0.0000455678 0.0000200868 / 0.1) 0px 0px 0px 1px, transparent 0px 0px 0px 0px | 0 |
| [Testimonial card](#testimonial-card) | 390 x 355.38 | - | 12px | #080808 `neutral.inset` | #373737 0px 0px 0px 1px inset | 15px |
| [Asset thumbnail](#asset-thumbnail) | 144 x 144 | 1px solid #343434 `neutral.thumb-border` | 16px | - | none | 0 |
| [Mobile plan card](#mobile-plan-card) | 331.5 x 576 | - | 33px | #121212 `neutral.card` | #222222 0px 0px 0px 1px inset | 15px |
| [Mobile asset title](#mobile-asset-title) | 135.05 x 26 | - | - | transparent | none | 0 |

## Components

### Shell and navigation

The 80px sticky header over the marketing one-pager: the Endless Tools wordmark, a translucent Log-in pill and a solid white Start-for-free pill, on the black veil gradient.

#### Header
The sticky top bar over a fade gradient: the logomark, the Log-in outline pill and the white Start-for-free pill. Read as `header` on the marketing home page.

**Values (default).** size 1440 x 80; background transparent; image linear-gradient(#000000 `neutral.page` 14.73%, rgba(0, 10, 10, 0) 100%); text Inter 12/14 500, #959595 `neutral.grey-4`.

![Header default](components/crops/header-default.png)

#### Logo
The Endless Tools dot-grid logomark anchor. Read as `logo` on the marketing home page.

**Values (default).** size 130 x 40; background transparent; text Inter 16/24 400, transparent.

![Logo default](components/crops/logo-default.png)

#### Log in link
The Log-in header action (secondary pill on a blurred #1e1e1e fill); measured never followed. Read as `nav-login` on the marketing home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 74.91 x 35; padding 0px 20px; radius 3.35544e+07px; background oklab(0.23503 0.0000106841 0.00000470877 / 0.8); shadow #959595 0px 0px 0px 1px inset; text Inter 12/14 500, #959595 `neutral.grey-4`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1), opacity 0.15s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1), transform 0.15s cubic-bezier(0.4, 0, 0.2, 1), translate 0.15s cubic-bezier(0.4, 0, 0.2, 1), scale 0.15s cubic-bezier(0.4, 0, 0.2, 1), rotate 0.15s cubic-bezier(0.4, 0, 0.2, 1), filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), -webkit-backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | background #1e1e1e `neutral.secondary`; shadow #ffffff 0px 0px 0px 1px inset; text Inter 12/14 500, #ffffff `neutral.white` |
| focus-visible | outline 1px auto #005fcc `accent.focus`, offset 1px |
| pressed | background #1e1e1e `neutral.secondary`; shadow #ffffff 0px 0px 0px 1px inset; text Inter 12/14 500, #ffffff `neutral.white` |

![Log in link default](components/crops/nav-login-default.png) ![Log in link hover](components/crops/nav-login-hover.png) ![Log in link focus-visible](components/crops/nav-login-focus-visible.png) ![Log in link pressed](components/crops/nav-login-pressed.png)

#### Nav CTA
The Start-for-free white pill; measured never followed (it opens the app host). Read as `nav-cta` on the marketing home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 113.22 x 35; padding 0px 20px; radius 3.35544e+07px; background #ffffff `neutral.white`; text Inter 12/14 500, #0a0a0a `neutral.black`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1), opacity 0.15s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1), transform 0.15s cubic-bezier(0.4, 0, 0.2, 1), translate 0.15s cubic-bezier(0.4, 0, 0.2, 1), scale 0.15s cubic-bezier(0.4, 0, 0.2, 1), rotate 0.15s cubic-bezier(0.4, 0, 0.2, 1), filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), -webkit-backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | background #373737 `neutral.grey-1`; text Inter 12/14 500, #ffffff `neutral.white` |
| focus-visible | outline 1px auto #005fcc `accent.focus`, offset 1px |
| pressed | background #373737 `neutral.grey-1`; text Inter 12/14 500, #ffffff `neutral.white` |

![Nav CTA default](components/crops/nav-cta-default.png) ![Nav CTA hover](components/crops/nav-cta-hover.png) ![Nav CTA focus-visible](components/crops/nav-cta-focus-visible.png) ![Nav CTA pressed](components/crops/nav-cta-pressed.png)

### Home hero

The centred hero: a 42px title with a hand-drawn ellipse annotation, the grey lede and the pink Start-creating pill.

#### Hero headline
The 42px title-primary headline; "exploration" and "graphic designers" carry hand-drawn circle/underline marks painted by masked white spans. Read as `hero-title` on the marketing home page.

**Values (default).** size 820 x 92; background transparent; text Inter 42/46 500, #ffffff `neutral.white`.

Child layers that carry the look: span 0x0 background #ffffff `neutral.white`; span 230x62.2 background #ffffff `neutral.white`; span 0x0 background #ffffff `neutral.white`.

![Hero headline default](components/crops/hero-title-default.png)

#### Annotation mark
One of the aria-hidden white spans behind the headline words, masked (via CSS mask-image) into the hand-drawn circle and underline — the signature annotation style repeated on every section heading. Read as `hero-mark` on the marketing home page.

**Values (default).** size 230 x 62.23; background #ffffff `neutral.white`; text Inter 42/46 500, #ffffff `neutral.white`.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Hero copy
The 14px grey-4 lede under the headline. Read as `hero-lede` on the marketing home page.

**Values (default).** size 350 x 36; background transparent; text Inter 14/18 400, #959595 `neutral.grey-4`.

![Hero copy default](components/crops/hero-lede-default.png)

#### Hero CTA
The Start-exploring pill — the only pink (#FF13B1) action on the site; measured never followed. Read as `hero-cta` on the marketing home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 124.41 x 36; padding 0px 20px; radius 3.35544e+07px; background #ff13b1 `accent.pink`; text Inter 12/14 500, #ffffff `neutral.white`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1), opacity 0.15s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1), transform 0.15s cubic-bezier(0.4, 0, 0.2, 1), translate 0.15s cubic-bezier(0.4, 0, 0.2, 1), scale 0.15s cubic-bezier(0.4, 0, 0.2, 1), rotate 0.15s cubic-bezier(0.4, 0, 0.2, 1), filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), -webkit-backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | background #ff4bc4 `accent.pink-hover` |
| focus-visible | outline 1px auto #005fcc `accent.focus`, offset 1px |
| pressed | background #ff4bc4 `accent.pink-hover` |

![Hero CTA default](components/crops/hero-cta-default.png) ![Hero CTA hover](components/crops/hero-cta-hover.png) ![Hero CTA focus-visible](components/crops/hero-cta-focus-visible.png) ![Hero CTA pressed](components/crops/hero-cta-pressed.png)

### Asset inputs

The 'Bring your own' strip: asset-type titles and rounded thumbnails the page drags between the statement sections.

#### Asset input title
An input-source heading (Use a library) inside a hand-drawn circle mark. Read as `asset-title` on the marketing home page.

**Values (default).** size 135.05 x 26; background transparent; text Inter 24/26 500, #ffffff `neutral.white`.

![Asset input title default](components/crops/asset-title-default.png)

#### Asset thumbnail
A floating asset tile: a looping muted video in a 16px-radius rounded box. Read as `asset-thumb` on the marketing home page.

**Values (default).** size 144 x 144; border 1px solid #343434 `neutral.thumb-border`; radius 16px; background transparent; text Inter 16/24 400, #ffffff `neutral.white`.

![Asset thumbnail default](components/crops/asset-thumb-default.png)

### Statement sections

The full-bleed statement titles and the editor screenshot the page sells the app with.

#### Section heading
A statement heading ("The hard part isn't making it.") — title-primary inside an underline mark. Read as `section-title` on the marketing home page.

**Values (default).** size 820 x 92; background transparent; text Inter 42/46 500, #ffffff `neutral.white`.

Child layers that carry the look: span 0x0 background #ffffff `neutral.white`; span 200x28.2 background #ffffff `neutral.white`.

![Section heading default](components/crops/section-title-default.png)

#### Product shot
The embedded product-workspace image/video in the "One workspace" band (marketing content, not the app). Read as `editor-shot` on the marketing home page.

**Values (default).** size 1300 x 700; radius 10px; background transparent; text Inter 16/24 400, #ffffff `neutral.white`.

![Product shot default](components/crops/editor-shot-default.png)

### Pricing

The Yearly/Monthly toggle (the only control flipped during capture), the pink save pill, and the plan cards with their chips, prices, feature lists and CTAs.

#### Billing toggle, yearly
The Yearly option of the billing toggle (selected by default — the chosen option renders disabled). Read as `billing-yearly` on the marketing home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 121.48 x 26; background transparent; text Inter 16/24 500, #ffffff `neutral.white`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured, not measured as absent.

Child layers that carry the look: span 71.8x25 background #ff3dae `accent.pill` radius 3.35544e+07px.

![Billing toggle, yearly default](components/crops/billing-yearly-default.png) ![Billing toggle, yearly hover](components/crops/billing-yearly-hover.png) ![Billing toggle, yearly pressed](components/crops/billing-yearly-pressed.png)

#### Billing toggle, monthly
The Monthly option; toggled for the monthly screenshot state, never checked out. Read as `billing-monthly` on the marketing home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 59.53 x 26; background transparent; text Inter 16/24 500, oklab(0.999994 0.0000455678 0.0000200868 / 0.3); transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | text Inter 16/24 500, oklab(0.999994 0.0000455678 0.0000200868 / 0.75) |
| focus-visible | outline 1px auto #005fcc `accent.focus`, offset 0px |
| pressed | text Inter 16/24 500, oklab(0.999994 0.0000455678 0.0000200868 / 0.75) |

![Billing toggle, monthly default](components/crops/billing-monthly-default.png) ![Billing toggle, monthly hover](components/crops/billing-monthly-hover.png) ![Billing toggle, monthly focus-visible](components/crops/billing-monthly-focus-visible.png) ![Billing toggle, monthly pressed](components/crops/billing-monthly-pressed.png)

#### Save badge
The pink "Save 17%" pill inside the Yearly option. Read as `save-pill` on the marketing home page.

**Values (default).** size 71.84 x 25; padding 0px 10px; radius 3.35544e+07px; background #ff3dae `accent.pill`; text Inter 12/25 500, #ffffff `neutral.white`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1).

![Save badge default](components/crops/save-pill-default.png)

#### Plan card
A pricing plan card: 33px radius, #121212 fill, 1px #222 ring, hover lifts to #1D1D1D. Read as `plan-card` on the marketing home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 356.66 x 562; padding 15px; radius 33px; background #121212 `neutral.card`; shadow #222222 0px 0px 0px 1px inset; text Inter 14/35 500, #ffffff `neutral.white`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1), opacity 0.15s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1), transform 0.15s cubic-bezier(0.4, 0, 0.2, 1), translate 0.15s cubic-bezier(0.4, 0, 0.2, 1), scale 0.15s cubic-bezier(0.4, 0, 0.2, 1), rotate 0.15s cubic-bezier(0.4, 0, 0.2, 1), filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), -webkit-backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | background #1d1d1d `neutral.card-hover` |

![Plan card default](components/crops/plan-card-default.png) ![Plan card hover](components/crops/plan-card-hover.png)

#### Plan chip
The FREE plan chip — a dark pill on the card header. Read as `plan-chip` on the marketing home page.

**Values (default).** size 64.22 x 35; padding 0px 15px; radius 3.35544e+07px; background #121212 `neutral.card`; shadow #222222 0px 0px 0px 1px; text Inter 14/35 500, #ffffff `neutral.white`.

![Plan chip default](components/crops/plan-chip-default.png)

#### Plan chip, PRO
The PRO chip — the inverted white pill. Read as `plan-chip-pro` on the marketing home page.

**Values (default).** size 58.8 x 35; padding 0px 15px; radius 3.35544e+07px; background #ffffff `neutral.white`; text Inter 14/35 500, #0a0a0a `neutral.black`.

![Plan chip, PRO default](components/crops/plan-chip-pro-default.png)

#### Plan chip, EDUCATION
The EDUCATION chip — the one blue element on the surface. Read as `plan-chip-edu` on the marketing home page.

**Values (default).** size 111.88 x 35; padding 0px 15px; radius 3.35544e+07px; background #2c5cff `accent.blue`; text Inter 14/35 500, #ffffff `neutral.white`.

![Plan chip, EDUCATION default](components/crops/plan-chip-edu-default.png)

#### Plan price
A plan price figure at title-primary size. Read as `plan-price` on the marketing home page.

**Values (default).** size 51.72 x 42; background transparent; text Inter 42/42 500, #ffffff `neutral.white`.

![Plan price default](components/crops/plan-price-default.png)

#### Plan feature row
A feature row on the PRO card: a 15px SVG glyph plus a bold white key and grey detail text. Read as `plan-feature` on the marketing home page.

**Values (default).** size 303.67 x 28; background transparent; text Inter 12/14 500, #ffffff `neutral.white`.

![Plan feature row default](components/crops/plan-feature-default.png)

#### Plan CTA
A plan card action (white pill); measured never followed. Read as `plan-cta` on the marketing home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 326.66 x 36; padding 0px 20px; radius 3.35544e+07px; background #ffffff `neutral.white`; text Inter 12/14 500, #0a0a0a `neutral.black`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1), opacity 0.15s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1), transform 0.15s cubic-bezier(0.4, 0, 0.2, 1), translate 0.15s cubic-bezier(0.4, 0, 0.2, 1), scale 0.15s cubic-bezier(0.4, 0, 0.2, 1), rotate 0.15s cubic-bezier(0.4, 0, 0.2, 1), filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), -webkit-backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | background #c4c4c4 `neutral.hover-white` |
| focus-visible | outline 1px auto #005fcc `accent.focus`, offset 1px |
| pressed | background #c4c4c4 `neutral.hover-white` |

![Plan CTA default](components/crops/plan-cta-default.png) ![Plan CTA hover](components/crops/plan-cta-hover.png) ![Plan CTA focus-visible](components/crops/plan-cta-focus-visible.png) ![Plan CTA pressed](components/crops/plan-cta-pressed.png)

### Team and education

The two secondary CTAs under pricing: a white team pill and the blue education pill.

#### Team CTA
The Create-team action under the shared-workspace section; measured never followed. Read as `team-cta` on the marketing home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 110 x 36; padding 0px 20px; radius 3.35544e+07px; background #ffffff `neutral.white`; text Inter 12/14 500, #0a0a0a `neutral.black`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1), opacity 0.15s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1), transform 0.15s cubic-bezier(0.4, 0, 0.2, 1), translate 0.15s cubic-bezier(0.4, 0, 0.2, 1), scale 0.15s cubic-bezier(0.4, 0, 0.2, 1), rotate 0.15s cubic-bezier(0.4, 0, 0.2, 1), filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), -webkit-backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | background #c4c4c4 `neutral.hover-white` |
| focus-visible | outline 1px auto #005fcc `accent.focus`, offset 1px |
| pressed | background #c4c4c4 `neutral.hover-white` |

![Team CTA default](components/crops/team-cta-default.png) ![Team CTA hover](components/crops/team-cta-hover.png) ![Team CTA focus-visible](components/crops/team-cta-focus-visible.png) ![Team CTA pressed](components/crops/team-cta-pressed.png)

#### Education CTA
The Request-Education-access mailto link; measured never followed. Read as `edu-cta` on the marketing home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 191.23 x 36; padding 0px 20px; radius 3.35544e+07px; background #2c5cff `accent.blue`; text Inter 12/14 500, #ffffff `neutral.white`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1), opacity 0.15s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1), transform 0.15s cubic-bezier(0.4, 0, 0.2, 1), translate 0.15s cubic-bezier(0.4, 0, 0.2, 1), scale 0.15s cubic-bezier(0.4, 0, 0.2, 1), rotate 0.15s cubic-bezier(0.4, 0, 0.2, 1), filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), -webkit-backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | background #5a65ff `accent.blue-hover` |
| focus-visible | outline 1px auto #005fcc `accent.focus`, offset 1px |
| pressed | background #5a65ff `accent.blue-hover` |

![Education CTA default](components/crops/edu-cta-default.png) ![Education CTA hover](components/crops/edu-cta-hover.png) ![Education CTA focus-visible](components/crops/edu-cta-focus-visible.png) ![Education CTA pressed](components/crops/edu-cta-pressed.png)

### Testimonials

The quote carousel: white serif quotes over the black field, round black/50 arrows, and the floating promo card.

#### Testimonial card
A "Created with Endless Tools" social post card in the carousel. Read as `social-card` on the marketing home page.

**Values (default).** size 390 x 355.38; padding 15px; radius 12px; background #080808 `neutral.inset`; shadow #373737 0px 0px 0px 1px inset; text Inter 12/14 500, #ffffff `neutral.white`.

![Testimonial card default](components/crops/social-card-default.png)

#### Carousel prev
The round 40px Previous arrow of the testimonial carousel. Read as `carousel-prev` on the marketing home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 40 x 40; radius 3.35544e+07px; background oklab(0.144787 0.00000661612 0.00000289828 / 0.5); shadow oklab(0.999994 0.0000455678 0.0000200868 / 0.15) 0px 0px 0px 1px; text Inter 16/24 400, #ffffff `neutral.white`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1), opacity 0.15s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1), transform 0.15s cubic-bezier(0.4, 0, 0.2, 1), translate 0.15s cubic-bezier(0.4, 0, 0.2, 1), scale 0.15s cubic-bezier(0.4, 0, 0.2, 1), rotate 0.15s cubic-bezier(0.4, 0, 0.2, 1), filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), -webkit-backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | background oklab(0.144787 0.00000661612 0.00000289828 / 0.8); shadow oklab(0.999994 0.0000455678 0.0000200868 / 0.4) 0px 0px 0px 1px |
| focus-visible | outline 1px auto #005fcc `accent.focus`, offset 0px |
| pressed | background oklab(0.144787 0.00000661612 0.00000289828 / 0.8); shadow oklab(0.999994 0.0000455678 0.0000200868 / 0.4) 0px 0px 0px 1px |

![Carousel prev default](components/crops/carousel-prev-default.png) ![Carousel prev hover](components/crops/carousel-prev-hover.png) ![Carousel prev focus-visible](components/crops/carousel-prev-focus-visible.png) ![Carousel prev pressed](components/crops/carousel-prev-pressed.png)

#### Floating promo card
The fixed bottom-centre testimonial pill ("Endless Tools great tool for designers by designers."). Read as `promo-card` on the marketing home page.

**Values (default).** size 365.58 x 54; background transparent; text Inter 14/20 400, #ffffff `neutral.white`.

Child layers that carry the look: div 365.6x54 radius 3.35544e+07px shadow transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, oklab(0.999994 0.0000455678 0.0000200868 / 0.1) 0px 0px 0px 1px, transparent 0px 0px 0px 0px; div 38x38 radius 3.35544e+07px shadow transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, #0a0a0a `neutral.black` 0px 0px 0px 2px, transparent 0px 0px 0px 0px.

![Floating promo card default](components/crops/promo-card-default.png)

### Newsletter

The footer signup: a pill email field, a bordered consent checkbox and a white submit pill. The form was never submitted.

#### Newsletter heading
The "Stay in the loop" heading. Read as `news-title` on the marketing home page.

**Values (default).** size 289.8 x 46; background transparent; text Inter 42/46 500, #ffffff `neutral.white`.

![Newsletter heading default](components/crops/news-title-default.png)

#### Newsletter field
The "Your email" input; sample text was typed and deleted, nothing sent. Read as `news-field` on the marketing home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focused, filled) | size 310 x 35; padding 0px 20px; radius 3.35544e+07px; background #1e1e1e `neutral.secondary`; shadow #373737 0px 0px 0px 1px; text Inter 12/14 500, #ffffff `neutral.white`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1), opacity 0.15s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1), transform 0.15s cubic-bezier(0.4, 0, 0.2, 1), translate 0.15s cubic-bezier(0.4, 0, 0.2, 1), scale 0.15s cubic-bezier(0.4, 0, 0.2, 1), rotate 0.15s cubic-bezier(0.4, 0, 0.2, 1), filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), -webkit-backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1); placeholder oklab(0.999994 0.0000455678 0.0000200868 / 0.5) |

![Newsletter field default](components/crops/news-field-default.png) ![Newsletter field focused](components/crops/news-field-focused.png) ![Newsletter field filled](components/crops/news-field-filled.png)

#### Consent checkbox
The "I agree to the Privacy Policy" checkbox (peer-checked swaps its fill white); checked as a local toggle — the form was never submitted. Read as `news-consent` on the marketing home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 18 x 18; border 1px solid #959595 `neutral.grey-4`; radius 3.35544e+07px; background transparent; text Inter 14/18 400, #959595 `neutral.grey-4`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1), opacity 0.15s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1), transform 0.15s cubic-bezier(0.4, 0, 0.2, 1), translate 0.15s cubic-bezier(0.4, 0, 0.2, 1), scale 0.15s cubic-bezier(0.4, 0, 0.2, 1), rotate 0.15s cubic-bezier(0.4, 0, 0.2, 1), filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), -webkit-backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| selected | background #ffffff `neutral.white` |

![Consent checkbox default](components/crops/news-consent-default.png) ![Consent checkbox selected](components/crops/news-consent-selected.png)

#### Newsletter submit
The "Stay updated" submit; measured, never pressed (a press would subscribe). Read as `news-submit` on the marketing home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 310 x 35; radius 3.35544e+07px; background #ffffff `neutral.white`; text Inter 12/14 500, #0a0a0a `neutral.black`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1), opacity 0.15s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1), transform 0.15s cubic-bezier(0.4, 0, 0.2, 1), translate 0.15s cubic-bezier(0.4, 0, 0.2, 1), scale 0.15s cubic-bezier(0.4, 0, 0.2, 1), rotate 0.15s cubic-bezier(0.4, 0, 0.2, 1), filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), -webkit-backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | background oklab(0.999994 0.0000455678 0.0000200868 / 0.85) |
| focus-visible | outline 1px auto #005fcc `accent.focus`, offset 0px |
| pressed | background oklab(0.999994 0.0000455678 0.0000200868 / 0.85) |

![Newsletter submit default](components/crops/news-submit-default.png) ![Newsletter submit hover](components/crops/news-submit-hover.png) ![Newsletter submit focus-visible](components/crops/news-submit-focus-visible.png) ![Newsletter submit pressed](components/crops/news-submit-pressed.png)

### Footer

The grey link columns and social links under the newsletter band.

#### Footer
The page footer: social links, legal links, contact mailto and the ©EndlessTools line. Read as `footer` on the marketing home page.

**Values (default).** size 1440 x 319; padding 150px 0px 75px 0px; background transparent; text Inter 14/18 400, #959595 `neutral.grey-4`.

![Footer default](components/crops/footer-default.png)

#### Footer link
A legal link in the footer. Read as `footer-link` on the marketing home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 92.28 x 18; background transparent; text Inter 14/18 400, #959595 `neutral.grey-4`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1), opacity 0.15s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1), transform 0.15s cubic-bezier(0.4, 0, 0.2, 1), translate 0.15s cubic-bezier(0.4, 0, 0.2, 1), scale 0.15s cubic-bezier(0.4, 0, 0.2, 1), rotate 0.15s cubic-bezier(0.4, 0, 0.2, 1), filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), -webkit-backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | text Inter 14/18 400, #ffffff `neutral.white` |
| focus-visible | outline 1px auto #005fcc `accent.focus`, offset 1px |
| pressed | text Inter 14/18 400, #ffffff `neutral.white` |

![Footer link default](components/crops/footer-link-default.png) ![Footer link hover](components/crops/footer-link-hover.png) ![Footer link focus-visible](components/crops/footer-link-focus-visible.png) ![Footer link pressed](components/crops/footer-link-pressed.png)

#### Social link
A social link in the footer Get-in-touch block; measured never followed. Read as `social-link` on the marketing home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 65.92 x 18; background transparent; text Inter 14/18 400, #959595 `neutral.grey-4`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1), opacity 0.15s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1), transform 0.15s cubic-bezier(0.4, 0, 0.2, 1), translate 0.15s cubic-bezier(0.4, 0, 0.2, 1), scale 0.15s cubic-bezier(0.4, 0, 0.2, 1), rotate 0.15s cubic-bezier(0.4, 0, 0.2, 1), filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), -webkit-backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | text Inter 14/18 400, #ffffff `neutral.white` |
| focus-visible | outline 1px auto #005fcc `accent.focus`, offset 1px |
| pressed | text Inter 14/18 400, #ffffff `neutral.white` |

![Social link default](components/crops/social-link-default.png) ![Social link hover](components/crops/social-link-hover.png) ![Social link focus-visible](components/crops/social-link-focus-visible.png) ![Social link pressed](components/crops/social-link-pressed.png)

### Log in (app host)

app.endlesstools.io/login: the 450px veil card with the OTP email flow (the 'Log in with password' switch was flipped, nothing was sent) and the password form behind it.

#### Login card
The centred 450px login card: a 5%-white fill at a 20px radius on the #0a0a0a field; never filled or submitted. Read as `login-card` on the app /login page.

**Values (default).** size 450 x 497; padding 50px; radius 20px; background rgba(239, 239, 239, 0.05) `neutral.alpha.veil-5`; text Inter 23/25 500, #efefef `neutral.ink`; icon 50 x 50, #efefef `neutral.ink`.

![Login card default](components/crops/login-card-default.png)

#### Login logo
The dot-grid Endless Tools mark above the card title (inline SVG, currentColor). Read as `login-logo` on the app /login page.

**Values (default).** size 50 x 50; background transparent; text Inter 16/24 400, #efefef `neutral.ink`; icon 50 x 50, #efefef `neutral.ink`.

![Login logo default](components/crops/login-logo-default.png)

#### Login title
"Welcome to Endless Tools!" plus the sign-in-or-create lede. Read as `login-title` on the app /login page.

**Values (default).** size 190 x 50; background transparent; text Inter 23/25 500, #efefef `neutral.ink`.

![Login title default](components/crops/login-title-default.png)

#### Email field
The email input (secondary fill, grey-2 border); sample text was typed and deleted, nothing sent. Read as `login-field` on the app /login page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 350 x 35; padding 0px 15px; border 1px solid #2a2a2a `neutral.grey-2`; radius 10px; background #1e1e1e `neutral.secondary`; text Inter 14/15 500, #efefef `neutral.ink`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), opacity 0.15s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1), transform 0.15s cubic-bezier(0.4, 0, 0.2, 1), filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1); placeholder #959595 `neutral.grey-4` |
| focused, filled | border 1px solid #373737 `neutral.grey-1`; outline 2px solid transparent, offset 2px |

![Email field default](components/crops/login-field-default.png) ![Email field focused](components/crops/login-field-focused.png) ![Email field filled](components/crops/login-field-filled.png)

#### Send Code button
The Send-Code submit (white fill); measured, never pressed (a press would send a login code). Read as `send-code` on the app /login page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 350 x 35; radius 10px; background #efefef `neutral.ink`; text Inter 14/15 500, #000000 `neutral.page`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), opacity 0.15s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1), transform 0.15s cubic-bezier(0.4, 0, 0.2, 1), filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | background rgba(239, 239, 239, 0.9) `neutral.alpha.ink-90` |
| focus-visible | outline 2px solid transparent, offset 2px |
| pressed | background rgba(239, 239, 239, 0.9) `neutral.alpha.ink-90` |

![Send Code button default](components/crops/send-code-default.png) ![Send Code button hover](components/crops/send-code-hover.png) ![Send Code button focus-visible](components/crops/send-code-focus-visible.png) ![Send Code button pressed](components/crops/send-code-pressed.png)

#### Password switch
The "Log in with password" ghost button that swaps the OTP form for the password form; toggled for the password-field reading. Read as `login-switch` on the app /login page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 184.98 x 35; padding 0px 25px; radius 10px; background transparent; text Inter 14/15 500, #efefef `neutral.ink`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), opacity 0.15s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1), transform 0.15s cubic-bezier(0.4, 0, 0.2, 1), filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | background #2a2a2a `neutral.grey-2` |
| focus-visible | outline 2px solid transparent, offset 2px |
| pressed | background #2a2a2a `neutral.grey-2` |

![Password switch default](components/crops/login-switch-default.png) ![Password switch hover](components/crops/login-switch-hover.png) ![Password switch focus-visible](components/crops/login-switch-focus-visible.png) ![Password switch pressed](components/crops/login-switch-pressed.png)

#### Password field
The password input on the password form (after the local switch); focused only, never filled or submitted. Read as `login-password-field` on the app /login page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 350 x 35; padding 0px 15px; border 1px solid #2a2a2a `neutral.grey-2`; radius 10px; background #1e1e1e `neutral.secondary`; text Inter 15/20 500, #efefef `neutral.ink`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), opacity 0.15s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1), transform 0.15s cubic-bezier(0.4, 0, 0.2, 1), filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1); placeholder #959595 `neutral.grey-4` |
| focused | border 1px solid #373737 `neutral.grey-1`; outline 2px solid transparent, offset 2px |

![Password field default](components/crops/login-password-field-default.png) ![Password field focused](components/crops/login-password-field-focused.png)

#### Log in button
The password form's Log-in submit; measured, never pressed. Read as `login-submit` on the app /login page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 350 x 35; radius 10px; background #efefef `neutral.ink`; text Inter 14/15 500, #000000 `neutral.page`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), opacity 0.15s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1), transform 0.15s cubic-bezier(0.4, 0, 0.2, 1), filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | background rgba(239, 239, 239, 0.9) `neutral.alpha.ink-90` |
| focus-visible | outline 2px solid transparent, offset 2px |
| pressed | background rgba(239, 239, 239, 0.9) `neutral.alpha.ink-90` |

![Log in button default](components/crops/login-submit-default.png) ![Log in button hover](components/crops/login-submit-hover.png) ![Log in button focus-visible](components/crops/login-submit-focus-visible.png) ![Log in button pressed](components/crops/login-submit-pressed.png)

#### Forgot password link
The "Forgot your password?" link; measured never followed. Read as `login-forgot` on the app /login page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 125.39 x 13; background transparent; text Inter 12/13 500, #959595 `neutral.grey-4`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), opacity 0.15s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1), transform 0.15s cubic-bezier(0.4, 0, 0.2, 1), filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | text Inter 12/13 500, #efefef `neutral.ink` |
| focus-visible | outline 2px solid transparent, offset 2px |
| pressed | text Inter 12/13 500, #efefef `neutral.ink` |

![Forgot password link default](components/crops/login-forgot-default.png) ![Forgot password link hover](components/crops/login-forgot-hover.png) ![Forgot password link focus-visible](components/crops/login-forgot-focus-visible.png) ![Forgot password link pressed](components/crops/login-forgot-pressed.png)

#### Legal line
The agree-to-terms line with its underlined Terms and Privacy links. Read as `login-legal` on the app /login page.

**Values (default).** size 350 x 26; background transparent; text Inter 12/13 400, #959595 `neutral.grey-4`.

![Legal line default](components/crops/login-legal-default.png)

### Legal documents (app host)

app.endlesstools.io/legal/*: the slim gradient header with the Sign-in pill and the long-form document text.

#### Legal header
The fixed top bar on the legal pages: logomark left, Sign-in pill right, over a nav gradient. Read as `legal-header` on the app /legal/privacy_policy page.

**Values (default).** size 1440 x 100; padding 0px 15px; background transparent; image linear-gradient(#0a0a0a `neutral.black`, rgba(10, 10, 10, 0)); text Inter 12/13 400, #efefef `neutral.ink`.

![Legal header default](components/crops/legal-header-default.png)

#### Sign in link
The Sign-in pill in the legal header; measured never followed. Read as `legal-signin` on the app /legal/privacy_policy page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 98.44 x 40; padding 0px 30px; radius 10px; background #2a2a2a `neutral.grey-2`; text Inter 12/13 400, #efefef `neutral.ink`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), opacity 0.15s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1), transform 0.15s cubic-bezier(0.4, 0, 0.2, 1), filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | text Inter 12/13 400, rgba(239, 239, 239, 0.75) `neutral.alpha.ink-75` |
| focus-visible | outline 2px solid transparent, offset 2px |
| pressed | text Inter 12/13 400, rgba(239, 239, 239, 0.75) `neutral.alpha.ink-75` |

![Sign in link default](components/crops/legal-signin-default.png) ![Sign in link hover](components/crops/legal-signin-hover.png) ![Sign in link focus-visible](components/crops/legal-signin-focus-visible.png) ![Sign in link pressed](components/crops/legal-signin-pressed.png)

#### Legal title
The document title ("Privacy Policy"). Read as `legal-title` on the app /legal/privacy_policy page.

**Values (default).** size 656.09 x 40; background transparent; text Inter 42/40 400, #efefef `neutral.ink`.

![Legal title default](components/crops/legal-title-default.png)

#### Legal content
The document body (the .et-content column): 14px grey-4 text with white emphasis spans. Read as `legal-content` on the app /legal/privacy_policy page.

Not on the page when it was captured.

#### Legal link
An inline document link (underlined); measured never followed. Read as `legal-link` on the app /legal/privacy_policy page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 171.05 x 20; background transparent; text Inter 16/24 500, rgba(239, 239, 239, 0.75) `neutral.alpha.ink-75` |
| focus-visible | outline 2px solid transparent, offset 2px |

![Legal link default](components/crops/legal-link-default.png) ![Legal link hover](components/crops/legal-link-hover.png) ![Legal link focus-visible](components/crops/legal-link-focus-visible.png) ![Legal link pressed](components/crops/legal-link-pressed.png)

### Mobile (390 wide)

The marketing page as a phone draws it, at 390 x 844 with an iPhone user agent.

#### Mobile header
The sticky bar at 390: logomark plus the white Start-for-free pill (the Log-in link hides at this width). Read as `m-header` on the marketing home at 390 page at 390 wide.

**Values (default).** size 390 x 78; background transparent; image linear-gradient(#000000 `neutral.page` 14.73%, rgba(0, 10, 10, 0) 100%); text Inter 12/14 500, #0a0a0a `neutral.black`.

![Mobile header default](components/crops/m-header-default.png)

#### Mobile nav CTA
The Start-for-free button at 390 (a button, not an anchor, at this width). Read as `m-cta` on the marketing home at 390 page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 113.22 x 38; padding 0px 20px; radius 3.35544e+07px; background #ffffff `neutral.white`; text Inter 12/14 500, #0a0a0a `neutral.black`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1), opacity 0.15s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1), transform 0.15s cubic-bezier(0.4, 0, 0.2, 1), translate 0.15s cubic-bezier(0.4, 0, 0.2, 1), scale 0.15s cubic-bezier(0.4, 0, 0.2, 1), rotate 0.15s cubic-bezier(0.4, 0, 0.2, 1), filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), -webkit-backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| focus-visible | outline 1px auto #005fcc `accent.focus`, offset 0px |

![Mobile nav CTA default](components/crops/m-cta-default.png) ![Mobile nav CTA hover](components/crops/m-cta-hover.png) ![Mobile nav CTA focus-visible](components/crops/m-cta-focus-visible.png) ![Mobile nav CTA pressed](components/crops/m-cta-pressed.png)

#### Mobile headline
The hero at 390: title-secondary size with the same circle/underline marks. Read as `m-hero` on the marketing home at 390 page at 390 wide.

**Values (default).** size 330 x 52; background transparent; text Inter 24/26 500, #ffffff `neutral.white`.

Child layers that carry the look: span 135x36.5 background #ffffff `neutral.white`; span 0x0 background #ffffff `neutral.white`; span 150x5.5 background #ffffff `neutral.white`.

![Mobile headline default](components/crops/m-hero-default.png)

#### Mobile asset title
An input-source heading in the stacked mobile layout. Read as `m-asset-card` on the marketing home at 390 page at 390 wide.

**Values (default).** size 135.05 x 26; background transparent; text Inter 24/26 500, #ffffff `neutral.white`.

![Mobile asset title default](components/crops/m-asset-card-default.png)

#### Mobile plan card
A plan card in the horizontally scrolling pricing row at 390. Read as `m-plan-card` on the marketing home at 390 page at 390 wide.

**Values (default).** size 331.5 x 576; padding 15px; radius 33px; background #121212 `neutral.card`; shadow #222222 0px 0px 0px 1px inset; text Inter 14/35 500, #ffffff `neutral.white`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1), opacity 0.15s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1), transform 0.15s cubic-bezier(0.4, 0, 0.2, 1), translate 0.15s cubic-bezier(0.4, 0, 0.2, 1), scale 0.15s cubic-bezier(0.4, 0, 0.2, 1), rotate 0.15s cubic-bezier(0.4, 0, 0.2, 1), filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), -webkit-backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1).

![Mobile plan card default](components/crops/m-plan-card-default.png)
## Gaps

### Pages

- **The product itself.** Endless Tools is a canvas editor for graphic designers; the editor, its toolbars, panels and canvas live behind sign-in on app.endlesstools.io and were never entered. Every component in this file is from the public marketing one-pager or the signed-out app shell (login card, legal documents).
- **Anything that sends or creates.** The newsletter form was never submitted, the OTP login never sent a code, the password form was never filled, and no checkout was opened — the plan CTAs only navigate to the app host.
- **Other app-host pages.** Only /login and the two legal documents paint signed out; signup and any other app route were not visited.
- **The consent checkbox's error state, toasts, dialogs and menus** do not exist on the public surfaces.

### States

- **Pressed** was forced with DevTools on every control, so a state a script adds on mousedown is missing; the page's own press cue is `active:scale-95`, which a forced pseudo-state does not show.
- **Hover on the asset thumbnails, plan chips, save pill and headers** changed nothing measurable; their entries read 'same'.
- **Disabled states** were not seen on any public control.
- **legal-content** (the .et-content document column) was listed but not found at capture time; the legal text is measured through legal-title and legal-link only.

### Themes

Both surfaces paint a single dark theme — the marketing body is `bg-[#000] text-white`, the app shell `bg-back` #0a0a0a — and neither offers a theme switch or a light sheet. The token file therefore ships a dark set only.

### Fonts

- **Inter** is the only family any measured text paints: the variable face (100-900) with next/font's Arial-metric 'Inter Fallback', subset woff2 on both hosts.
- **Flow Rounded** ships in the app bundle as `--font-skeleton` (a geometric placeholder face for skeleton/loading text); no public component paints it.

### Screenshots

- The hero canvas animates (orbiting shapes, gradient text), the testimonial card autoplaying quotes; two captures of the same view can differ in what the animation has drawn.
- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files.

### Content left out

- Testimonial names, plan copy and legal text are the product's published content and stay as captured.
- No personal data was captured: the pages were read signed out and no form was submitted.
