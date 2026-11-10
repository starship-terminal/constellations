# [untitled] components

The discovery list of every page and view captured, then one entry per component with crops of the real product and the Gaps. Captured from untitled.stream on 2026-11-10, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running page. Nothing was bought, downloaded, signed into, sent or submitted.

The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) (51 components, 101 states).

How to read an entry:

- A colour is its value followed by the palette token in [tokens.json](tokens.json) with the same value, when there is one. Text is written family size/line-height weight, then its colour, for example `Untitled Sans 15/20 500, #191919`, and is read from the first text node inside the component.
- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example "default (same: focus-visible)". When the root paints nothing, "Child layers" names the first nodes inside it that do.
- Crops are images of the component read from the live page, in [components/crops/](components/crops) (99 files, named `{component}-{state}.png`, at 2x). Screenshots are in [screenshots/](screenshots).

## Discovery list

Screenshots are named `{page}-light-{state}.png` (the marketing site paints its light theme). Desktop shots are 1440 x 900 at 1x; `-full` shots are whole pages at 1x; mobile shots are `mobile-{page}-light-{state}.png`, 780 wide (390 at 2x). /terms, /privacy and /cookie-policy stayed inside Cloudflare's waiting room headless and are listed as blocked, not captured.

| Surface | URL | Screenshots |
|---|---|---|
| Home. Tagline, disc strip, bottom pill bar; consent card and full page. | `/` | [default](screenshots/home-light-default.png), [full](screenshots/home-light-full.png) |
| Pricing. Title, billing rail, plan cards; full page. | `/pricing` | [default](screenshots/pricing-light-default.png), [full](screenshots/pricing-light-full.png) |
| Trust & Security. The numbered-practices text column; full page. | `/trust` | [default](screenshots/trust-light-default.png), [full](screenshots/trust-light-full.png) |
| Sign-in. Icon, OAuth pills, phone link; captured when Cloudflare cleared. | `/login` | [default](screenshots/login-light-default.png), [full](screenshots/login-light-full.png) |
| Home at 390: hero title, App Store badge, the giant disc; full page. | `/` | [default](screenshots/mobile-home-light-default.png), [full](screenshots/mobile-home-light-full.png) |
| Pricing at 390; full page. | `/pricing` | [default](screenshots/mobile-pricing-light-default.png), [full](screenshots/mobile-pricing-light-full.png) |
| Trust at 390; full page. | `/trust` | [default](screenshots/mobile-trust-light-default.png), [full](screenshots/mobile-trust-light-full.png) |

### Overlays and transient states

| State | Where | How it was reached | Captured |
|---|---|---|---|
| Consent card | first visit, any page | mounts fixed bottom-left; measured, then hidden (never clicked — the buttons POST a Remix action to /settings/cookies that Cloudflare 403s headless, which replaces the page with the router error boundary) | [consent-card](#consent-card), [consent-accept](#accept-all-button), [consent-reject](#reject-all-button) |
| Monthly billing | pricing | the Monthly segment pressed (client-side state, nothing sent) | [billing-monthly-on](#monthly-option-selected), [plan-price-monthly](#monthly-price) |
| Feature videos | home sections | auto-playing demo videos down the page | measured as element boxes only; streams not introspected |
| Signed-in onboarding | the app | a window screenshot from the user's own signed-in browser session | dark "Welcome / Choose a disc" screen — evidence of the app theme only, not introspected |

## Shared values

Values that apply across entries, from the measurement files.

**Focus.** 16 components were given a real keyboard focus. 0 draw a ring: none. The other 16 draw none, so a keyboard user sees no change: `logo`, `nav-membership`, `cta-enter-app`, `pill-social`, `cta-hiring`, `pill-learn-more`, `pill-platform`, `read-more`, `footer-link`, `cookie-settings`, `cta-subscribe`, `trust-link`, `oauth-google`, `oauth-apple`, `phone-signin`, `legal-link`.

**Pressed.** untitled's pills hold flat under :active (the interactions are opacity hovers, not colour steps) — see the per-component state rows.

**Motion.** Transitions measured on the components, by duration.

| Duration | Easing | Property | Where |
|---|---|---|---|
| 0.15s | `cubic-bezier(0.4, 0, 0.2, 1)` | opacity | cta-enter-app, cta-subscribe, legal-link, nav-membership, read-more |
| 0.2s | `cubic-bezier(0.4, 0, 0.2, 1)` | opacity | pill-platform, trust-link |
| 0.3s | `cubic-bezier(0.4, 0, 0.2, 1)` | all, opacity | billing-monthly, billing-monthly-on, billing-yearly, consent-accept, consent-customize, consent-reject, cookie-settings, cta-hiring and more |

**Card shapes.** Default-state values; the entries hold the states. The Painted child column names the first node inside a transparent root that carries the paint — it is the child's radius and fill, not the container's, and its size is the child's own.

| Card | Size | Border | Radius | Background | Shadow | Padding | Painted child |
|---|---|---|---|---|---|---|---|
| [Header](#header) | 1312 x 88 | - | - | transparent | none | 0 | a.clean-btn.inline-flex 150x44, radius 3.35544e+07px, shadow transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0p |
| [Pricing header](#pricing-header) | 1440 x 108 | - | - | transparent | none | 32px 64px | a.clean-btn.inline-flex 150x44, rgba(26, 26, 26, 0.05) `shading.DEFAULT`, radius 3.35544e+07px |
| [Cookie consent card](#cookie-consent-card) | 500 x 224 | - | 16px | rgba(38, 38, 38, 0.9) `surface-frost` | rgba(0, 0, 0, 0.2) 0px 4px 10px 0px | 0 | - |
| [Plan card (starter)](#plan-card-starter) | 350 x 536 | - | 20px | #eeeeee | none | 32px 24px | - |
| [Plan card (membership)](#plan-card-membership) | 350 x 536 | - | - | #eeeeee | none | 32px 24px 32px 0px | div.bg-secondary-background-dark.relative 350x536, #eeeeee |
| [Sign-in card](#sign-in-card) | 1440 x 762 | - | - | transparent | none | 32px 0px 128px 0px | div.absolute.inset-[7%] 189.2x189.2, oklab(0 none none / 0.1), radius 3.35544e+07px |
| [Bottom pill bar](#bottom-pill-bar) | 1440 x 92 | - | - | transparent | none | 24px 64px | div.sm:bg-shading.flex 342.4x44, rgba(26, 26, 26, 0.05) `shading.DEFAULT`, radius 3.35544e+07px |
| [Billing toggle](#billing-toggle) | 121.95 x 536 | - | - | transparent | none | 0 | span.bg-shading.rounded-20 91.1x44, rgba(26, 26, 26, 0.05) `shading.DEFAULT`, radius 20px |
| [Disc carousel](#disc-carousel) | 1440 x 900 | - | - | transparent | none | 0 | div.bg-shading.rounded-full 818.6x818.6, rgba(26, 26, 26, 0.05) `shading.DEFAULT`, radius 3.35544e+07px |
| [Feature section](#feature-section) | 319 x 72 | - | - | transparent | none | 0 | - |
| [Feature video](#feature-video) | 450 x 345.94 | - | - | rgba(26, 26, 26, 0.05) `shading.DEFAULT` | none | 0 | video.opacity-0.shadow-device 450x345.9, rgba(26, 26, 26, 0.05) `shading.DEFAULT` |
| [Trust bullet list](#trust-bullet-list) | 528 x 86 | - | - | transparent | none | 0px 24px | - |

## Components

### Shell and navigation

The chrome on the public pages: a transparent top band (the [untitled] wordmark link on sub-pages, [membership] and the black Enter App pill on the right), and the legal row at the foot. Home's header swaps the wordmark for the super-title tagline.

#### Header
The transparent top band: [untitled] wordmark and the super-title tagline on the left, [membership] text link and the black Enter App pill on the right. Read as `header` on the home page.

**Values (default).** size 1312 x 88; background transparent; text Untitled Sans 26/32 500, #191919 `black`.

Child layers that carry the look: a 150x44 image linear-gradient(#242424 0%, #101010 100%) radius 3.35544e+07px shadow transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, rgba(0, 0, 0, 0.15) 0px 4px 15px 0px.

![Header default](components/crops/header-default.png)

#### Wordmark
The [untitled] mark, a text link rendered with bracket styling; only rendered on the sub-pages, not on home. Read as `logo` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 112.28 x 32; background transparent; text Untitled Sans 26/32 500, #191919 `black`; transition opacity 0.3s cubic-bezier(0.4, 0, 0.2, 1) |
| hover, pressed | opacity 0.8 |

![Wordmark default](components/crops/logo-default.png) ![Wordmark hover](components/crops/logo-hover.png) ![Wordmark focus-visible](components/crops/logo-focus-visible.png) ![Wordmark pressed](components/crops/logo-pressed.png)

#### Membership nav link
The [membership] text link in the header; scrolls to the membership pitch. Read as `nav-membership` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 99.3 x 20; background transparent; text Untitled Sans 15/20 500, #191919 `black`; transition opacity 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover, pressed | opacity 0.8 |

![Membership nav link default](components/crops/nav-membership-default.png) ![Membership nav link hover](components/crops/nav-membership-hover.png) ![Membership nav link focus-visible](components/crops/nav-membership-focus-visible.png) ![Membership nav link pressed](components/crops/nav-membership-pressed.png)

#### Enter App CTA
The black pill at the header's far right; links to /login. Read as `cta-enter-app` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 150 x 44; padding 0px 16px; radius 3.35544e+07px; background transparent; image linear-gradient(#242424 0%, #101010 100%); shadow rgba(0, 0, 0, 0.15) 0px 4px 15px 0px; text Untitled Sans 13/16 500, #ffffff `white`; transition opacity 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover, pressed | opacity 0.8 |

![Enter App CTA default](components/crops/cta-enter-app-default.png) ![Enter App CTA hover](components/crops/cta-enter-app-hover.png) ![Enter App CTA focus-visible](components/crops/cta-enter-app-focus-visible.png) ![Enter App CTA pressed](components/crops/cta-enter-app-pressed.png)

#### Footer
The legal row at the foot: Terms, Privacy, Cookie Policy, Contact Us and a Cookie Settings button, plus the Made in Brooklyn, NY mark. Read as `footer` on the home page.

**Values (default).** size 436.64 x 16; background transparent; text Untitled Sans 13/16 400, #7e7e7e `gray`.

![Footer default](components/crops/footer-default.png)

#### Footer legal link
Read as `footer-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 36.58 x 16; background transparent; text Untitled Sans 13/16 400, #7e7e7e `gray`; transition opacity 0.3s cubic-bezier(0.4, 0, 0.2, 1) |
| hover, pressed | opacity 0.8 |

![Footer legal link default](components/crops/footer-link-default.png) ![Footer legal link hover](components/crops/footer-link-hover.png) ![Footer legal link focus-visible](components/crops/footer-link-focus-visible.png) ![Footer legal link pressed](components/crops/footer-link-pressed.png)

#### Cookie settings button
The footer control that re-opens the consent card. Focused and hovered only — pressing it reposts the gated consent flow. Read as `cookie-settings` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 90.13 x 16; background transparent; text Untitled Sans 13/16 400, #7e7e7e `gray`; transition opacity 0.3s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | opacity 0.8 |

![Cookie settings button default](components/crops/cookie-settings-default.png) ![Cookie settings button hover](components/crops/cookie-settings-hover.png) ![Cookie settings button focus-visible](components/crops/cookie-settings-focus-visible.png)

#### Pricing header
Same top band as home, here with the [untitled] wordmark link at the left and Enter app (ghost) + Subscribe (black) pills on the right. Read as `pricing-header` on the pricing page.

**Values (default).** size 1440 x 108; padding 32px 64px; background transparent; text Untitled Sans 26/32 500, #191919 `black`.

Child layers that carry the look: div 2592x108 image linear-gradient(in oklab, #ffffff `white` 0%, #ffffff `white` 80%, transparent 100%); a 150x44 background rgba(26, 26, 26, 0.05) `shading.DEFAULT` radius 3.35544e+07px; a 150x44 image linear-gradient(#242424 0%, #101010 100%) radius 3.35544e+07px shadow transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, rgba(0, 0, 0, 0.15) 0px 4px 15px 0px.

![Pricing header default](components/crops/pricing-header-default.png)

#### Subscribe CTA
The black Subscribe pill in the header. Read as `cta-subscribe` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 150 x 44; padding 0px 16px; radius 3.35544e+07px; background transparent; image linear-gradient(#242424 0%, #101010 100%); shadow rgba(0, 0, 0, 0.15) 0px 4px 15px 0px; text Untitled Sans 13/16 500, #ffffff `white`; transition opacity 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover, pressed | opacity 0.8 |

![Subscribe CTA default](components/crops/cta-subscribe-default.png) ![Subscribe CTA hover](components/crops/cta-subscribe-hover.png) ![Subscribe CTA focus-visible](components/crops/cta-subscribe-focus-visible.png) ![Subscribe CTA pressed](components/crops/cta-subscribe-pressed.png)

### Home

The landing page: the super-title tagline, the auto-scrolling strip of oversized iridescent CD renders, the floating pill bar pinned to the viewport bottom, and product-feature sections with demo videos down ~4800px.

#### Hero title
The visible display copy "A sacred place for your work-in-progress music" (p.super-title); the actual h1 is sr-only. Read as `hero-title` on the home page.

**Values (default).** size 360 x 64; background transparent; text Untitled Sans 26/32 500, #191919 `black`.

![Hero title default](components/crops/hero-title-default.png)

#### Disc carousel
The signature element: a strip of oversized iridescent CD renders (div.rounded-full with webp background-image art) filling the hero. Read as `disc-carousel` on the home page.

**Values (default).** size 1440 x 900; background transparent; text Untitled Sans 15/20 400, #191919 `black`.

Child layers that carry the look: div 818.6x818.6 background rgba(26, 26, 26, 0.05) `shading.DEFAULT` radius 3.35544e+07px; div 771.3x771.3 background rgba(26, 26, 26, 0.05) `shading.DEFAULT` radius 3.35544e+07px; div 791x791 background rgba(26, 26, 26, 0.05) `shading.DEFAULT` radius 3.35544e+07px.

![Disc carousel default](components/crops/disc-carousel-default.png)

#### Disc
One iridescent CD render: a rounded-full div whose background-image is a webp disc artwork. Read as `disc` on the home page.

**Values (default).** size 802.64 x 802.64; radius 3.35544e+07px; background rgba(26, 26, 26, 0.05) `shading.DEFAULT`; image url(…); text Untitled Sans 15/20 400, #191919 `black`; transform matrix(-0.439488, 0.898249, -0.898249, -0.439488, 0, 0).

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Bottom pill bar
The floating bar pinned to the viewport bottom: social pills (Texting Interviews, IG, X), the black We're hiring pill, Learn more, and the iOS / Android / MacOS platform pills. Read as `pill-bar` on the home page.

**Values (default).** size 1440 x 92; padding 24px 64px; background transparent; text Untitled Sans 15/20 500, #191919 `black`; icon 20 x 20, #191919 `black`.

Child layers that carry the look: div 342.4x44 background rgba(26, 26, 26, 0.05) `shading.DEFAULT` radius 3.35544e+07px; a 130.7x44 background #191919 `black` radius 3.35544e+07px; button 148.7x44 background rgba(26, 26, 26, 0.05) `shading.DEFAULT` radius 3.35544e+07px.

![Bottom pill bar default](components/crops/pill-bar-default.png)

#### Social pill
A frosted pill in the bottom bar holding the social links (a campaign link — "[untitled broadcast network]", earlier "Texting Interviews" — then IG, X). Read as `pill-social` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 220.91 x 20; padding 0px 12px; background transparent; text Untitled Sans 15/20 500, #191919 `black` |
| hover, pressed | opacity 0.8 |

![Social pill default](components/crops/pill-social-default.png) ![Social pill hover](components/crops/pill-social-hover.png) ![Social pill focus-visible](components/crops/pill-social-focus-visible.png) ![Social pill pressed](components/crops/pill-social-pressed.png)

#### Hiring pill
The inverted (black) "We're hiring" pill in the bottom bar; links to jobs.untitled.stream. Read as `cta-hiring` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 130.72 x 44; padding 12px 24px; radius 3.35544e+07px; background #191919 `black`; text Untitled Sans 15/20 500, #ffffff `white`; transition opacity 0.3s cubic-bezier(0.4, 0, 0.2, 1) |
| hover, pressed | opacity 0.8 |

![Hiring pill default](components/crops/cta-hiring-default.png) ![Hiring pill hover](components/crops/cta-hiring-hover.png) ![Hiring pill focus-visible](components/crops/cta-hiring-focus-visible.png) ![Hiring pill pressed](components/crops/cta-hiring-pressed.png)

#### Learn more pill
The frosted pill that scrolls the page to the product sections. It fades to opacity 0 as soon as the page scrolls and back at the top — these states are measured at scrollY 0. Read as `pill-learn-more` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, focus-visible, pressed) | size 148.67 x 44; padding 12px; radius 3.35544e+07px; background rgba(26, 26, 26, 0.05) `shading.DEFAULT`; text Untitled Sans 15/20 500, #191919 `black`; transition opacity 0.3s cubic-bezier(0.4, 0, 0.2, 1); icon 20 x 20, #191919 `black` |

![Learn more pill default](components/crops/pill-learn-more-default.png) ![Learn more pill hover](components/crops/pill-learn-more-hover.png) ![Learn more pill focus-visible](components/crops/pill-learn-more-focus-visible.png) ![Learn more pill pressed](components/crops/pill-learn-more-pressed.png)

#### Platform pill
One of the iOS / Android / MacOS download pills in the bottom bar, each with a platform icon. Read as `pill-platform` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 96.39 x 44; padding 12px 20px; radius 3.35544e+07px; background rgba(26, 26, 26, 0.05) `shading.DEFAULT`; text Untitled Sans 15/20 500, #191919 `black`; transition opacity 0.2s cubic-bezier(0.4, 0, 0.2, 1); icon 20 x 20, #191919 `black` |
| hover, pressed | opacity 0.8 |

![Platform pill default](components/crops/pill-platform-default.png) ![Platform pill hover](components/crops/pill-platform-hover.png) ![Platform pill focus-visible](components/crops/pill-platform-focus-visible.png) ![Platform pill pressed](components/crops/pill-platform-pressed.png)

#### Feature title
An h3.body-semibold heading a product section down the page ("Organize your music the way you want"). Read as `feature-title` on the home page.

**Values (default).** size 319 x 20; background transparent; text Untitled Sans 15/20 500, #191919 `black`.

![Feature title default](components/crops/feature-title-default.png)

#### Feature section
A product-feature block down the landing page: heading, copy and media. Read as `feature-section` on the home page.

**Values (default).** size 319 x 72; background transparent; text Untitled Sans 15/20 500, #191919 `black`.

![Feature section default](components/crops/feature-section-default.png)

#### Read more link
A text link expanding a product story section. Read as `read-more` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 65.88 x 16; background transparent; text Untitled Sans 13/16 400, #191919 `black`; transition opacity 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover, pressed | opacity 0.8 |

![Read more link default](components/crops/read-more-default.png) ![Read more link hover](components/crops/read-more-hover.png) ![Read more link focus-visible](components/crops/read-more-focus-visible.png) ![Read more link pressed](components/crops/read-more-pressed.png)

#### Feature video
A product-demo video embedded in a feature section; measured as the element, its stream is not introspected. Read as `feature-video` on the home page.

**Values (default).** size 450 x 345.94; background rgba(26, 26, 26, 0.05) `shading.DEFAULT`; text Untitled Sans 15/20 400, #191919 `black`; opacity 0.

![Feature video default](components/crops/feature-video-default.png)

### Pricing

The pricing page: the display title, the Yearly/Monthly segment rail, and the [starter] (free) and [membership] ($49.99/yr) plan cards flanking a disc collage.

#### Pricing title
"Take your creative process to the next level" — a .super-title block, same display style as the home hero. Read as `pricing-title` on the pricing page.

**Values (default).** size 1312 x 32; background transparent; text Untitled Sans 26/32 500, #191919 `black`.

![Pricing title default](components/crops/pricing-title-default.png)

#### Billing toggle
The Yearly / Monthly segment rail at the left of the plan grid: the buttons are its direct children, and the column stretches to the plan cards' full height. Read as `billing-toggle` on the pricing page.

**Values (default).** size 121.95 x 536; background transparent; text Untitled Sans 15/20 500, #191919 `black`.

Child layers that carry the look: span 91.1x44 background rgba(26, 26, 26, 0.05) `shading.DEFAULT` radius 20px.

![Billing toggle default](components/crops/billing-toggle-default.png)

#### Yearly option
The selected segment (default plan is yearly). Read as `billing-yearly` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 91.08 x 44; padding 12px 24px; radius 3.35544e+07px; background transparent; text Untitled Sans 15/20 500, #191919 `black`; transition all 0.3s cubic-bezier(0.4, 0, 0.2, 1) |
| hover, pressed | opacity 0.8 |

Child layers that carry the look: span 91.1x44 background rgba(26, 26, 26, 0.05) `shading.DEFAULT` radius 20px.

![Yearly option default](components/crops/billing-yearly-default.png) ![Yearly option hover](components/crops/billing-yearly-hover.png) ![Yearly option pressed](components/crops/billing-yearly-pressed.png)

#### Monthly option
Read as `billing-monthly` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 105 x 44; padding 12px 24px; radius 3.35544e+07px; background transparent; text Untitled Sans 15/20 500, #191919 `black`; transition all 0.3s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | opacity 0.8 |

![Monthly option default](components/crops/billing-monthly-default.png) ![Monthly option hover](components/crops/billing-monthly-hover.png)

#### Monthly option (selected)
The Monthly segment after pressing it: client-side state switch, no data posted. Read as `billing-monthly-on` on the pricing page.

**Values (open).** size 105 x 44; padding 12px 24px; radius 3.35544e+07px; background transparent; text Untitled Sans 15/20 500, #191919 `black`; transition all 0.3s cubic-bezier(0.4, 0, 0.2, 1); opacity 0.996676.

Child layers that carry the look: span 105x44 background rgba(26, 26, 26, 0.05) `shading.DEFAULT` radius 20px.

![Monthly option (selected) open](components/crops/billing-monthly-on-open.png)

#### Monthly price
The membership price after switching to Monthly. Read as `plan-price-monthly` on the pricing page.

**Values (open).** size 278 x 20; background transparent; text Untitled Sans 15/20 500, #191919 `black`.

![Monthly price open](components/crops/plan-price-monthly-open.png)

#### Plan card (starter)
The [starter] free tier card: plan name, price, feature list with icons. Read as `plan-card` on the pricing page.

**Values (default).** size 350 x 536; padding 32px 24px; radius 20px; background #eeeeee; text Untitled Sans 26/32 500, #191919 `black`; icon 32 x 32, #191919 `black`.

![Plan card (starter) default](components/crops/plan-card-default.png)

#### Plan card (membership)
The [membership] card: $49.99 / year, feature list with icons. Read as `plan-card-paid` on the pricing page.

**Values (default).** size 350 x 536; padding 32px 24px 32px 0px; background #eeeeee; text Untitled Sans 26/32 500, #191919 `black`; icon 32 x 32, #191919 `black`.

![Plan card (membership) default](components/crops/plan-card-paid-default.png)

#### Plan name
A bracketed plan name ([starter], [membership]). Read as `plan-name` on the pricing page.

**Values (default).** size 254 x 32; background transparent; text Untitled Sans 26/32 500, #191919 `black`.

![Plan name default](components/crops/plan-name-default.png)

#### Plan price
Read as `plan-price` on the pricing page.

**Values (default).** size 254 x 20; background transparent; text Untitled Sans 15/20 500, #191919 `black`.

![Plan price default](components/crops/plan-price-default.png)

#### Feature row
A plan feature line: icon + h3.body-semibold name + sub copy ("Unlimited listening"). Read as `feature-row` on the pricing page.

**Values (default).** size 254 x 52; background transparent; text Untitled Sans 15/20 500, #191919 `black`; icon 32 x 32, #191919 `black`.

![Feature row default](components/crops/feature-row-default.png)

### Trust and security

The Trust & Security page: a single text column of numbered practices (passwordless sign-in, encryption, Face ID).

#### Trust title
"Trust & Security" — the page is a single long-text column. Read as `trust-title` on the trust page.

**Values (default).** size 536 x 32; background transparent; text Untitled Sans 26/32 500, #191919 `black`.

![Trust title default](components/crops/trust-title-default.png)

#### Trust section title
A numbered practice heading ("[1] Passwordless sign-in"). Read as `trust-section-title` on the trust page.

**Values (default).** size 536 x 22; background transparent; text Untitled Sans 18/22 500, #191919 `black`.

![Trust section title default](components/crops/trust-section-title-default.png)

#### Trust bullet list
The encryption-standards bullet list (TLS in transit, AES-256 at rest). Read as `trust-list` on the trust page.

**Values (default).** size 528 x 86; padding 0px 24px; background transparent; text Untitled Sans 15/20 500, #191919 `black`.

![Trust bullet list default](components/crops/trust-list-default.png)

#### Trust link
The untitled-blue outbound link inside the practices column (the Latacora link). Read as `trust-link` on the trust page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 58.69 x 19; background transparent; text Untitled Sans 15/20 400, #191919 `black`; transition opacity 0.2s cubic-bezier(0.4, 0, 0.2, 1) |
| hover, pressed | opacity 0.8 |

![Trust link default](components/crops/trust-link-default.png) ![Trust link hover](components/crops/trust-link-hover.png) ![Trust link focus-visible](components/crops/trust-link-focus-visible.png) ![Trust link pressed](components/crops/trust-link-pressed.png)

### Dialogs and overlays

The one overlay the site raises signed out: the "We value privacy" consent card. It was measured, then hidden — its buttons were never pressed (see Gaps).

#### Cookie consent card
The "We value privacy" card, fixed bottom-left on first load (frosted surface). Its Customize / Reject all / Accept all buttons were measured but never pressed: the consent form posts a Remix action to /settings/cookies, which Cloudflare 403s headless, replacing the page with the router error boundary. Read as `consent-card` on the home page.

**Values (default).** size 500 x 224; radius 16px; background rgba(38, 38, 38, 0.9) `surface-frost`; image linear-gradient(0deg, #808080 0%, #808080 100%), none; shadow rgba(0, 0, 0, 0.2) 0px 4px 10px 0px; text Untitled Sans 15/20 500, #ffffff `white`.

![Cookie consent card default](components/crops/consent-card-default.png)

#### Accept all button
The solid white pill in the consent card. Not pressed. Read as `consent-accept` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 85.63 x 40; padding 12px 16px; radius 3.35544e+07px; background #ffffff `white`; text Untitled Sans 12/16 500, #000000; transition opacity 0.3s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | opacity 0.8 |

![Accept all button default](components/crops/consent-accept-default.png) ![Accept all button hover](components/crops/consent-accept-hover.png)

#### Reject all button
The bg-white/5 ghost pill beside Accept all. Not pressed. Read as `consent-reject` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 81.2 x 40; padding 12px 16px; radius 3.35544e+07px; background rgba(255, 255, 255, 0.05); text Untitled Sans 12/16 500, #ffffff `white`; transition opacity 0.3s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | opacity 0.8 |

![Reject all button default](components/crops/consent-reject-default.png) ![Reject all button hover](components/crops/consent-reject-hover.png)

#### Customize link
The text-only option in the consent card. Not pressed. Read as `consent-customize` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 58.45 x 16; background transparent; text Untitled Sans 12/16 500, #ffffff `white`; transition opacity 0.3s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | opacity 0.8 |

![Customize link default](components/crops/consent-customize-default.png) ![Customize link hover](components/crops/consent-customize-hover.png)

### Mobile (390 wide)

The same pages as a phone draws them, at 390 x 844 with an iPhone user agent: the hero title, the App Store badge and one oversized disc.

#### Mobile hero title
Read as `m-hero-title` on the home page at 390 wide.

**Values (default).** size 294 x 88; padding 0px 0px 20px 0px; background transparent; text Untitled Sans 28/34 500, #191919 `black`.

![Mobile hero title default](components/crops/m-hero-title-default.png)

#### App Store badge
The Download on the App Store badge under the mobile hero title. Read as `m-appstore` on the home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 150 x 50; background transparent; text Untitled Sans 17/22 500, #191919 `black`; transition opacity 0.3s cubic-bezier(0.4, 0, 0.2, 1) |
| pressed | opacity 0.8 |

![App Store badge default](components/crops/m-appstore-default.png) ![App Store badge pressed](components/crops/m-appstore-pressed.png)

#### Mobile disc
The oversized iridescent disc filling the lower half of the mobile hero. Read as `m-disc` on the home page at 390 wide.

**Values (default).** size 772.52 x 772.52; radius 3.35544e+07px; background rgba(26, 26, 26, 0.05) `shading.DEFAULT`; image url(…); text Untitled Sans 17/22 400, #191919 `black`; transform matrix(-0.35126, 0.936278, -0.936278, -0.35126, 0, 0).

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Mobile nav link
Read as `m-membership` on the home page at 390 wide.

Not on the page when it was captured.

### Sign-in boundary

The /login card: app icon, tagline, and Continue with Google / Apple / phone. The buttons were measured at rest only — OAuth leaves the site and the phone flow starts a session, so nothing was pressed. The signed-in app beyond it is out of scope.

#### Sign-in card
The centred sign-in column: app icon, the tagline, and three choices — Continue with Google, Continue with Apple, Sign in with phone. OAuth and phone sign-in were measured at rest only; nothing was pressed or sent. Read as `login-card` on the login page.

**Values (default).** size 1440 x 762; padding 32px 0px 128px 0px; background transparent; text Untitled Sans 26/32 500, #191919 `black`; icon 21 x 20, #191919 `black`.

Child layers that carry the look: div 220x220 image linear-gradient(#eeeeee, #d0d0d0); div 189.2x189.2 background oklab(0 none none / 0.1) radius 3.35544e+07px; div 167.2x167.2 background oklab(0 none none / 0.1) radius 3.35544e+07px.

![Sign-in card default](components/crops/login-card-default.png)

#### App icon
The iridescent-disc app icon at the top of the sign-in card (the 220 px amulet mask, not its inner ring). Read as `login-icon` on the login page.

**Values (default).** size 220 x 220; background transparent; image linear-gradient(#eeeeee, #d0d0d0); text Untitled Sans 15/20 400, #191919 `black`.

![App icon default](components/crops/login-icon-default.png)

#### Sign-in title
Read as `login-title` on the login page.

**Values (default).** size 300 x 64; background transparent; text Untitled Sans 26/32 500, #191919 `black`.

![Sign-in title default](components/crops/login-title-default.png)

#### Continue with Google
The frosted OAuth pill. Hovered and focused only — pressing it leaves for accounts.google.com. Read as `oauth-google` on the login page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 342 x 52; padding 16px 20px; radius 3.35544e+07px; background rgba(26, 26, 26, 0.05) `shading.DEFAULT`; text Untitled Sans 15/20 500, #191919 `black`; transition opacity 0.3s cubic-bezier(0.4, 0, 0.2, 1); icon 21 x 20, #191919 `black` |
| hover | opacity 0.8 |

![Continue with Google default](components/crops/oauth-google-default.png) ![Continue with Google hover](components/crops/oauth-google-hover.png) ![Continue with Google focus-visible](components/crops/oauth-google-focus-visible.png)

#### Continue with Apple
The matching Apple OAuth pill. Hovered and focused only. Read as `oauth-apple` on the login page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 342 x 54; padding 16px 20px; radius 3.35544e+07px; background rgba(26, 26, 26, 0.05) `shading.DEFAULT`; text Untitled Sans 15/20 500, #191919 `black`; transition opacity 0.3s cubic-bezier(0.4, 0, 0.2, 1); icon 18 x 22, #191919 `black` |
| hover | opacity 0.8 |

![Continue with Apple default](components/crops/oauth-apple-default.png) ![Continue with Apple hover](components/crops/oauth-apple-hover.png) ![Continue with Apple focus-visible](components/crops/oauth-apple-focus-visible.png)

#### Phone sign-in link
The text option under the OAuth pills; leads to the passwordless SMS flow. Read as `phone-signin` on the login page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 342 x 52; padding 16px 0px; radius 3.35544e+07px; background transparent; text Untitled Sans 15/20 500, #191919 `black`; transition opacity 0.3s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | opacity 0.8 |

![Phone sign-in link default](components/crops/phone-signin-default.png) ![Phone sign-in link hover](components/crops/phone-signin-hover.png) ![Phone sign-in link focus-visible](components/crops/phone-signin-focus-visible.png)

#### Legal link
The Terms / Privacy Policy links under the sign-in choices. Read as `legal-link` on the login page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 33.81 x 15; background transparent; text Untitled Sans 12/16 400, #7e7e7e `gray`; transition opacity 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover, pressed | opacity 0.8 |

![Legal link default](components/crops/legal-link-default.png) ![Legal link hover](components/crops/legal-link-hover.png) ![Legal link focus-visible](components/crops/legal-link-focus-visible.png) ![Legal link pressed](components/crops/legal-link-pressed.png)
## Gaps

### Pages

- **The app and everything behind sign-in.** The product itself is account-gated (Google / Apple OAuth or passwordless SMS): app views, the library, upload and collaboration were never reached. The sign-in card at /login was captured when Cloudflare's challenge happened to clear; the signed-in onboarding was seen once — a dark "Welcome to [untitled] / Choose a disc" screen — in a window screenshot from the user's own signed-in browser, held as provenance for the app's dark theme only, not introspected.
- **/terms, /privacy and /cookie-policy** stay inside Cloudflare's managed-challenge waiting room headless ("Performing security verification") and were never reached; they are recorded as blocked, not captured.
- **The consent card's own actions.** Its buttons were measured but never pressed: the form posts a Remix action to /settings/cookies, which Cloudflare 403s headless, and the router's error boundary then replaces the whole page with "Something went wrong". The card is hidden before other captures instead of being dismissed.
- **Anything that sends.** No form was submitted, nothing bought, nothing downloaded; the OAuth pills and the phone sign-in were measured at rest only.

### States

- **Pressed** was forced with DevTools (`CSS.forcePseudoState` :active:hover), so a state a script adds on mousedown (if any) is missing.
- **The feature videos** down the home page stream their own content; the elements' boxes are measured but the frames inside are not introspected.
- **Monthly billing** was reached by pressing the Monthly segment (client-side state, nothing posted); Yearly was restored after.

### Themes

The marketing site paints its light theme; the stylesheet also ships a complete `[data-theme="dark"]` remap — the app's theme, seen on the signed-in onboarding's dark surface. The token file carries both sets, dark sourced from the stylesheet's own overrides.

### Fonts

- **Untitled Sans** and **IBM Plex Mono** are the site's faces, served as woff/woff2 from `/assets/` (`fonts` in [raw/css-vars.json](raw/css-vars.json)). Untitled Sans is the product's own brand face; the style guide falls back to the system sans/mono for them.

### Screenshots

- Screens and product imagery are untitled.stream's content and appear only inside screenshots and crops.
- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files.

### Content left out

- No personal data was captured: every page was read signed out with an empty session, and the only presses were the Monthly billing toggle; no text was ever typed into a form.
