# Acuity Scheduling components

The discovery list of every page and state captured, then one entry per component with crops of the real site, the shared values and the Gaps. Captured from acuityscheduling.com on 2026-11-09 and 2026-11-10, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running page. Nothing was submitted, bought or signed into; the only presses were local UI toggles (the nav mega-menu, the pricing FAQ accordion, the mobile hamburger, the gate's MORE OPTIONS). Consent SDKs were aborted at request level, so no consent button was ever mounted or pressed — a hide, not a consent.

The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) (58 components, 143 states).

How to read an entry:

- A colour is its value followed by the token in [tokens.json](tokens.json) whose value is the same, when there is one. Text is written family size/line-height weight, then its colour, for example `Clarkson 14/22 500, #0e0e0e`, and is read from the first text node inside the component.
- The first state of each entry lists every value; later states list only what changed. A state identical to the first is named in its label, for example "default (same: focus-visible)". When the root paints nothing, "Child layers" names the first nodes inside it that do.
- Crops are images of the component in [components/crops/](components/crops) (143 files, named `{component}-{state}.png`, at 2x). Screenshots are in [screenshots/](screenshots).

## Discovery list

Screenshots are named `{page}-light-{state}.png`. Desktop shots are 1440 x 900 at 1x; `-full` shots are whole pages at the same width; mobile shots are `mobile-{page}-light-{state}.png`, 390 x 844 at 2x. Only light exists — the marketing site and the gate have no dark theme.

| Surface | URL | Screenshots |
|---|---|---|
| Home. The gradient hero, industry cards, feature card, testimonial carousel, support card and footer. Captured at rest, with the Solutions mega-menu open, and full-page. | `/` | [default (light)](screenshots/home-light-default.png), [dropdown (light)](screenshots/home-light-dropdown.png), [full (light)](screenshots/home-light-full.png) |
| Pricing. The plan cards, segment toggle and navy FAQ. Captured at rest, with the first FAQ open, and full-page. | `/pricing` | [default (light)](screenshots/pricing-light-default.png), [faq-open (light)](screenshots/pricing-light-faq-open.png), [full (light)](screenshots/pricing-light-full.png) |
| How Acuity works. | `/features/how-acuity-works` | [default (light)](screenshots/how-it-works-light-default.png), [full (light)](screenshots/how-it-works-light-full.png) |
| The features index. | `/features` | [default (light)](screenshots/features-light-default.png), [full (light)](screenshots/features-light-full.png) |
| The solutions index. | `/solutions` | [default (light)](screenshots/solutions-light-default.png), [full (light)](screenshots/solutions-light-full.png) |
| An industry page (Beauty). | `/solutions/beauty` | [default (light)](screenshots/beauty-light-default.png), [full (light)](screenshots/beauty-light-full.png) |
| The about page. | `/about` | [default (light)](screenshots/about-light-default.png), [full (light)](screenshots/about-light-full.png) |
| The Learn resources page. | `/learn` | [default (light)](screenshots/learn-light-default.png), [full (light)](screenshots/learn-light-full.png) |
| Get started, which lands on Squarespace's public 'Create your account' gate. Captured at rest and with MORE OPTIONS open. | `/get-started?type=professional` | [default (light)](screenshots/get-started-light-default.png), [full (light)](screenshots/get-started-light-full.png), [more-options (light)](screenshots/get-started-light-more-options.png) |
| Log in, which redirects to Squarespace's public sign-in page. Captured at rest only. | `https://secure.acuityscheduling.com/login?nav=1` | [default (light)](screenshots/login-light-default.png), [full (light)](screenshots/login-light-full.png) |
| Home at 390: collapsed bar, the hamburger menu open, and full-page. | `/` | [default (light)](screenshots/mobile-home-light-default.png), [full (light)](screenshots/mobile-home-light-full.png), [menu (light)](screenshots/mobile-home-light-menu.png) |
| Pricing at 390. | `/pricing` | [default (light)](screenshots/mobile-pricing-light-default.png), [full (light)](screenshots/mobile-pricing-light-full.png) |

### Overlays and transient states

| State | Where | How it was reached | Captured |
|---|---|---|---|
| Solutions mega-menu | home | hover on the Solutions nav trigger (a local disclosure) | [home-light-dropdown](screenshots/home-light-dropdown.png), [nav-dropdown](#nav-dropdown), [dropdown-item](#dropdown-item) |
| Pricing FAQ, first answer open | pricing | the accordion row's own toggle | [pricing-light-faq-open](screenshots/pricing-light-faq-open.png), [accordion-title-open](#accordion-title-open), [accordion-panel](#accordion-panel) |
| Mobile menu sheet | home at 390 | the hamburger button | [mobile-home-light-menu](screenshots/mobile-home-light-menu.png), [m-menu](#m-menu), [m-menu-link](#m-menu-link) |
| MORE OPTIONS, open | get-started | the caps toggle on the account gate | [get-started-light-more-options](screenshots/get-started-light-more-options.png), [more-options-open](#more-options-open) |
| Form focus and fill | the login card | tabbed into and typed (sample text, deleted; nothing sent) | [login-email](#login-email), [login-password](#login-password) |

## Shared values

Values that apply across entries, tallied from the measurement file.

**Radius.** 12px (16), 16px (6), 50% (4), 8px (2), 22px (1), 24px (1), 6px (1). The 12px step is the signature: nav pill, hero CTAs, plan buttons, the bottom CTA and the plan cards share it.

**Hover.** no change on the element (26), transparent to #f2f2f2 `palette.fog` (1), #283849 `surface-inverse` to #3e5772 `palette.ink-hover` (1), transparent to #f0f0f0 `palette.fog-deep` (1), #283849 `surface-inverse` to #1e2d3a `palette.ink-pressed` (1). Links fade to 50% opacity or gain an underline rather than recolouring; the ink fills split — the header pill lightens to #3e5772 `palette.ink-hover` while the plan button darkens to #1e2d3a `palette.ink-pressed`.

**Focus.** Of 27 elements given a real keyboard focus: 1px auto #005fcc `palette.focus-blue` offset 1px (10), 2px solid transparent offset 2px (6), no ring on the element (4), 1px auto #005fcc `palette.focus-blue` offset 0px (3), 2px auto #000000 `border-strong` offset 4px (1), 2px solid #283849 `palette.ink` offset 2px (1). Links and accordions take Chromium's 1px #005fcc `palette.focus-blue` auto ring; the mobile menu's controls draw #e59700 `palette.focus-amber` amber; the gate's buttons paint a double box-shadow ring (2px white, 4px black); plan-cta draws a 2px solid #283849 `palette.ink` ring offset 2px.

**Motion.** 0.05s ease (41), 0.15s ease-in (4), 0.2s ease (4), 0.15s ease (4), 0.25s ease-in-out (3), 0.2s ease-out (1). The blanket step is 50ms ease on links and gate rows; the header pill takes 150ms ease-in; the mega-menu opens over 250ms ease-in-out.

**Layout.** The desktop bar is an 80px rail (55px at 390; the open mobile menu's header block 104px). Controls come in four heights: the 42.8px nav pill, 46px plan buttons, 55px gate/OAuth rows and the 56px hero CTAs (the bottom CTA stretches to 72px). The mega-menu panel pads 44px at a 22px radius; the FAQ column is 640px; plan cards are ~449px across on 1px #e4e4e4 hairlines.

**Accent.** Navy ink #283849 does all the work: every primary button fill, the serif headlines' colour, the hero ghost CTAs' 1px rules, the FAQ band and the support card. There is no bright accent at all — the loudest secondary is the pale-blue #e0ebf4 bottom band and the lavender #d6d0ed testimonial card.

## Components

### Shell and navigation

The 80px white bar every marketing page shares (55px at 390): the acuity:scheduling wordmark left, How It Works / Solutions / Product / Resources (the last three open mega-menu panels) / Pricing centre, Log in and the ink Get started pill right. Links are Clarkson 14/18.76; hover fades them to 50% opacity.

#### Header

<a id="header"></a>`header`, on home. The fixed top bar at 80px: the Acuity wordmark left; How It Works plus the Solutions / Product / Resources dropdown triggers, Pricing and Log in; the Get started CTA right. Transparent over the hero, opaque after scroll.

<img src="components/crops/header-default.png" alt="Header, default" height="80"> 

| State | Values |
|---|---|
| default | size 1440 x 80; padding 18px 20px 18px 40px; background transparent; text Clarkson 14/18.76 400, #000000 `text-strong`; transition background 0.25s ease-in-out |

#### Wordmark

<a id="logo"></a>`logo`, on home. The Acuity logotype in the header, an SVG lockup that links home.

<img src="components/crops/logo-default.png" alt="Wordmark, default" height="24"> 

| State | Values |
|---|---|
| default | size 168 x 24; background transparent |

#### Nav link

<a id="nav-link"></a>`nav-link`, on home. A direct header link (How It Works, Pricing).

<img src="components/crops/nav-link-default.png" alt="Nav link, default" height="24"> <img src="components/crops/nav-link-hover.png" alt="Nav link, hover" height="24"> <img src="components/crops/nav-link-focus-visible.png" alt="Nav link, focus-visible" height="24"> <img src="components/crops/nav-link-pressed.png" alt="Nav link, pressed" height="24"> 

| State | Values |
|---|---|
| default | size 85.39 x 18.77; background transparent; text Clarkson 14/18.76 400, #000000 `text-strong` |
| hover | opacity 0.5 |
| focus-visible | outline 1px auto #005fcc `palette.focus-blue`, offset 1px |
| pressed | opacity 0.5 |

#### Nav dropdown trigger

<a id="nav-trigger"></a>`nav-trigger`, on home. A hoverable dropdown trigger (Solutions, Product, Resources): a nav item that opens a mega-menu of industry / feature links.

<img src="components/crops/nav-trigger-default.png" alt="Nav dropdown trigger, default" height="24"> <img src="components/crops/nav-trigger-hover.png" alt="Nav dropdown trigger, hover" height="24"> <img src="components/crops/nav-trigger-focus-visible.png" alt="Nav dropdown trigger, focus-visible" height="24"> <img src="components/crops/nav-trigger-pressed.png" alt="Nav dropdown trigger, pressed" height="24"> 

| State | Values |
|---|---|
| default | size 80.86 x 18.77; background transparent; text Clarkson 14/18.76 400, #000000 `text-strong` |
| hover | opacity 0.5 |
| focus-visible | outline 1px auto #005fcc `palette.focus-blue`, offset 0px |
| pressed | opacity 0.5 |

#### Nav dropdown

<a id="nav-dropdown"></a>`nav-dropdown`, on home. The Solutions mega-menu under the header: a padded card grid of industry links (Beauty, Business Services, Wellness, Fitness, Visual and Performing Arts, Education).

<img src="components/crops/nav-dropdown-default.png" alt="Nav dropdown, default" height="120"> 

| State | Values |
|---|---|
| default | size 788 x 347; padding 44px; radius 22px; background #ffffff `surface`; shadow rgba(0, 0, 0, 0.05) 0px 4px 4px 2px; text Clarkson 14/22 400, #000000 `text-strong`; transition opacity 0.25s ease-in-out |

#### Dropdown item

<a id="dropdown-item"></a>`dropdown-item`, on home. An industry link inside the mega-menu: a bold name with a grey one-line description.

<img src="components/crops/dropdown-item-default.png" alt="Dropdown item, default" height="65"> <img src="components/crops/dropdown-item-hover.png" alt="Dropdown item, hover" height="65"> <img src="components/crops/dropdown-item-focus-visible.png" alt="Dropdown item, focus-visible" height="65"> <img src="components/crops/dropdown-item-pressed.png" alt="Dropdown item, pressed" height="65"> 

| State | Values |
|---|---|
| default | size 353 x 65; padding 11px; border B: 1px solid #f2f2f2 `palette.fog`; background transparent; text Clarkson 14/22 400, #000000 `text-strong` |
| hover | radius 8px; background #f2f2f2 `palette.fog` |
| focus-visible | outline 1px auto #005fcc `palette.focus-blue`, offset 1px |
| pressed | radius 8px; background #f2f2f2 `palette.fog` |

Child layers: a 353x65 border 1px solid #f2f2f2 `palette.fog`

#### Log in link

<a id="login-link"></a>`login-link`, on home. The Log in entry in the header, an <a> to the Squarespace sign-in gate. Hovered and focused, never followed.

<img src="components/crops/login-link-default.png" alt="Log in link, default" height="24"> <img src="components/crops/login-link-hover.png" alt="Log in link, hover" height="24"> <img src="components/crops/login-link-focus-visible.png" alt="Log in link, focus-visible" height="24"> <img src="components/crops/login-link-pressed.png" alt="Log in link, pressed" height="24"> 

| State | Values |
|---|---|
| default | size 40.27 x 18; background transparent; text Clarkson 14/18.76 400, #000000 `text-strong` |
| hover | opacity 0.5 |
| focus-visible | outline 1px auto #005fcc `palette.focus-blue`, offset 1px |
| pressed | opacity 0.5 |

#### Nav CTA

<a id="nav-cta"></a>`nav-cta`, on home. The Get started button in the header: the signup CTA.

<img src="components/crops/nav-cta-default.png" alt="Nav CTA, default" height="43"> <img src="components/crops/nav-cta-hover.png" alt="Nav CTA, hover" height="43"> <img src="components/crops/nav-cta-focus-visible.png" alt="Nav CTA, focus-visible" height="43"> <img src="components/crops/nav-cta-pressed.png" alt="Nav CTA, pressed" height="43"> 

| State | Values |
|---|---|
| default | size 121.48 x 42.77; padding 12px 24px; radius 12px; background #283849 `surface-inverse`; text Clarkson 14/18.76 400, #ffffff `text-inverse`; transition all 0.15s ease-in |
| hover | background #3e5772 `palette.ink-hover` |
| focus-visible | background #3e5772 `palette.ink-hover`; outline 2px auto #000000 `border-strong`, offset 4px |
| pressed | background #3e5772 `palette.ink-hover` |

### Home

The home page: a pastel gradient hero (nine declared variants rotate; the capture shows one) with a serif headline and two ghost signup CTAs, the cream industry cards, a grey feature card with an ink CTA, the auto-playing lavender testimonial carousel, and the pale-blue bottom band holding the navy support card and a tall ink CTA.

#### Hero

<a id="hero"></a>`hero`, on home. The opening band: the 40px "Scheduling software to power exceptional client experiences" headline, the signup pair and a product booking-page mock. Measured at rest.

<img src="components/crops/hero-default.png" alt="Hero, default" height="120"> 

| State | Values |
|---|---|
| default | size 1440 x 1317.33; background transparent; text Clarkson Serif 40/48 500, #283849 `accent` |

Child layers: div 1440x1317.3 image linear-gradient(66deg, #f0ece1 `palette.hero-c1` 0px, #f9f6ea `palette.hero-c2` 75%, #f6f3ed `palette.hero-c3` 100%); div::after 1440pxx395.188px image linear-gradient(transparent, #ffffff `surface`); a 0x0 background #283849 `surface-inverse` radius 12px

#### Hero title

<a id="hero-title"></a>`hero-title`, on home. The 40px Clarkson headline.

<img src="components/crops/hero-title-default.png" alt="Hero title, default" height="96"> 

| State | Values |
|---|---|
| default | size 572 x 96; background transparent; text Clarkson Serif 40/48 500, #283849 `accent` |

#### Hero sub

<a id="hero-sub"></a>`hero-sub`, on home. The supporting line under the title ("Book appointments, take payments, and automate the busywork…").

<img src="components/crops/hero-sub-default.png" alt="Hero sub, default" height="51"> 

| State | Values |
|---|---|
| default | size 572 x 51.19; background transparent; text Clarkson 16/25.6 400, #283849 `accent` |

#### Sign up with email

<a id="hero-cta-email"></a>`hero-cta-email`, on home. The hero signup button: a 56px 12px-radius control, followed to the account gate only in captures — never pressed here.

<img src="components/crops/hero-cta-email-default.png" alt="Sign up with email, default" height="56"> <img src="components/crops/hero-cta-email-hover.png" alt="Sign up with email, hover" height="56"> <img src="components/crops/hero-cta-email-focus-visible.png" alt="Sign up with email, focus-visible" height="56"> <img src="components/crops/hero-cta-email-pressed.png" alt="Sign up with email, pressed" height="56"> 

| State | Values |
|---|---|
| default | size 220.06 x 56; padding 16px 33px; border 1px solid #283849 `palette.ink`; radius 12px; background transparent; text Clarkson 14/22 400, #283849 `accent` |
| hover | opacity 0.8 |
| focus-visible | outline 1px auto #005fcc `palette.focus-blue`, offset 1px |
| pressed | opacity 0.8 |

#### Sign up with Google

<a id="hero-cta-google"></a>`hero-cta-google`, on home. The Google signup button beside the email one, with the G glyph.

<img src="components/crops/hero-cta-google-default.png" alt="Sign up with Google, default" height="56"> <img src="components/crops/hero-cta-google-hover.png" alt="Sign up with Google, hover" height="56"> <img src="components/crops/hero-cta-google-focus-visible.png" alt="Sign up with Google, focus-visible" height="56"> <img src="components/crops/hero-cta-google-pressed.png" alt="Sign up with Google, pressed" height="56"> 

| State | Values |
|---|---|
| default | size 211.98 x 56; padding 16px 25px; border 1px solid #283849 `palette.ink`; radius 12px; background transparent; text Clarkson 14/22 400, #283849 `accent` |
| hover | opacity 0.8 |
| focus-visible | outline 1px auto #005fcc `palette.focus-blue`, offset 1px |
| pressed | opacity 0.8 |

#### Signup legal line

<a id="hero-terms"></a>`hero-terms`, on home. The "By creating an account, you agree to our Terms of Service…" line under the buttons.

<img src="components/crops/hero-terms-default.png" alt="Signup legal line, default" height="32"> 

| State | Values |
|---|---|
| default | size 273 x 32; background transparent; text Clarkson 10/16 400, #283849 `accent` |

#### Industry card

<a id="vertical-card"></a>`vertical-card`, on home. A tile in "Acuity is for anyone in the business of time" (Beauty, Business Services, Wellness, Fitness, Visual and Performing Arts, Education): a named card with an image and a one-line descriptor, linking the industry page.

<img src="components/crops/vertical-card-default.png" alt="Industry card, default" height="120"> <img src="components/crops/vertical-card-hover.png" alt="Industry card, hover" height="120"> <img src="components/crops/vertical-card-focus-visible.png" alt="Industry card, focus-visible" height="120"> <img src="components/crops/vertical-card-pressed.png" alt="Industry card, pressed" height="120"> 

| State | Values |
|---|---|
| default (same: hover, pressed) | size 458.89 x 150; padding 10px; radius 16px; background #fdf9f7 `surface-warm`; shadow rgba(0, 0, 0, 0.08) 0px 0px 0.5px 0px, rgba(0, 0, 0, 0.12) 0px 16px 32px 0px; text Clarkson 16/19.44 500, #000000 `text-strong` |
| focus-visible | outline 1px auto #005fcc `palette.focus-blue`, offset 1px |

#### Industries CTA

<a id="vertical-cta"></a>`vertical-cta`, on home. "Explore all industries" under the grid.

<img src="components/crops/vertical-cta-default.png" alt="Industries CTA, default" height="24"> <img src="components/crops/vertical-cta-hover.png" alt="Industries CTA, hover" height="24"> <img src="components/crops/vertical-cta-focus-visible.png" alt="Industries CTA, focus-visible" height="24"> <img src="components/crops/vertical-cta-pressed.png" alt="Industries CTA, pressed" height="24"> 

| State | Values |
|---|---|
| default (same: hover, pressed) | size 155.73 x 22; background transparent; text Clarkson 16/22 400, #0e0e0e `text-soft` |
| focus-visible | outline 1px auto #005fcc `palette.focus-blue`, offset 1px |

#### Feature card

<a id="feature-card"></a>`feature-card`, on home. A card in "Everything you need to run your business" (Book beautifully 24/7, Reduce no-shows, Automate your day, Boost your earnings): an image, a 24px header and body text.

<img src="components/crops/feature-card-default.png" alt="Feature card, default" height="120"> <img src="components/crops/feature-card-hover.png" alt="Feature card, hover" height="120"> 

| State | Values |
|---|---|
| default (same: hover) | size 928 x 333.73; padding 40px; radius 16px; background #f4f4f4 `surface-mist`; text Clarkson Serif 24/28 500, #283849 `accent` |

#### Feature card title

<a id="feature-card-title"></a>`feature-card-title`, on home. A 24px feature card header.

<img src="components/crops/feature-card-title-default.png" alt="Feature card title, default" height="28"> 

| State | Values |
|---|---|
| default | size 414 x 28; background transparent; text Clarkson Serif 24/28 500, #283849 `accent` |

#### Testimonial card

<a id="testimonial-card"></a>`testimonial-card`, on home. A quote card in "Real results from professionals just like you".

<img src="components/crops/testimonial-card-default.png" alt="Testimonial card, default" height="120"> 

| State | Values |
|---|---|
| default | size 787.95 x 444.55; radius 24px; background transparent; shadow rgba(0, 0, 0, 0.12) 0px 2px 8px 0px, rgba(0, 0, 0, 0.08) 0px 0px 1px 0px; text Clarkson 20/32 500, #162427 |

#### Carousel arrow

<a id="carousel-nav"></a>`carousel-nav`, on home. A prev/next control on the testimonials carousel.

*Not found on the captured pages — an honest miss, kept so the gap is visible.*

#### Integration logo

<a id="integration-logo"></a>`integration-logo`, on home. A partner mark in "Connect your calendar and so much more" (Google, Outlook, Stripe…).

<img src="components/crops/integration-logo-default.png" alt="Integration logo, default" height="55"> 

| State | Values |
|---|---|
| default | size 151.42 x 55; background transparent; text Clarkson 16/22 500, #0e0e0e `text-soft` |

#### Bottom CTA

<a id="bottom-cta"></a>`bottom-cta`, on home. The closing "Get started for free" band before the footer.

<img src="components/crops/bottom-cta-default.png" alt="Bottom CTA, default" height="120"> 

| State | Values |
|---|---|
| default | size 1440 x 599; padding 204px 20px 195px 20px; background transparent; text Clarkson Serif 40/48 500, #283849 `accent` |

Child layers: a 230x72 background #283849 `surface-inverse` radius 12px

#### Carousel dots

<a id="carousel-dots"></a>`carousel-dots`, on home. The testimonials carousel has no arrows: a .testimonial-card__dots row of thin dash indicators (the active one wider) marks position while slides auto-play.

<img src="components/crops/carousel-dots-default.png" alt="Carousel dots, default" height="24"> 

| State | Values |
|---|---|
| default | size 68 x 3.4; background transparent |

Child layers: span 27.2x3.4 background #574f8a `palette.grape` radius 2px; span 3.4x3.4 background rgba(22, 36, 39, 0.25) radius 50%; span 3.4x3.4 background rgba(22, 36, 39, 0.25) radius 50%

### Footer

The white page foot: 'Get Started' link columns in Clarkson 16/18.4 titles and 12px links, the social icon circles, then the legal row under a hairline. Footer links underline on hover.

#### Footer

<a id="footer"></a>`footer`, on home. The page foot: a Squarespace logo mark, link columns under collapsible headings (Get Started, Features, Solutions, Resources), social icons and legal links.

<img src="components/crops/footer-default.png" alt="Footer, default" height="120"> 

| State | Values |
|---|---|
| default | size 1440 x 641.19; padding 40px 0px 20px 0px; background #ffffff `surface`; text Clarkson 12/19.2 600, #0e0e0e `text-soft` |

#### Footer column title

<a id="footer-col-title"></a>`footer-col-title`, on home. A footer column heading (Get Started, Features, Solutions, Resources): a button that expands the column on narrow screens.

<img src="components/crops/footer-col-title-default.png" alt="Footer column title, default" height="41"> <img src="components/crops/footer-col-title-hover.png" alt="Footer column title, hover" height="41"> <img src="components/crops/footer-col-title-focus-visible.png" alt="Footer column title, focus-visible" height="41"> <img src="components/crops/footer-col-title-pressed.png" alt="Footer column title, pressed" height="41"> 

| State | Values |
|---|---|
| default (same: hover, pressed) | size 203.59 x 41.19; background transparent; text Clarkson 12/19.2 600, #0e0e0e `text-soft` |
| focus-visible | outline 1px auto #005fcc `palette.focus-blue`, offset 0px |

#### Footer link

<a id="footer-link"></a>`footer-link`, on home. A footer column link (Home, About Us, Pricing, Online Booking).

<img src="components/crops/footer-link-default.png" alt="Footer link, default" height="37"> <img src="components/crops/footer-link-hover.png" alt="Footer link, hover" height="37"> <img src="components/crops/footer-link-focus-visible.png" alt="Footer link, focus-visible" height="37"> <img src="components/crops/footer-link-pressed.png" alt="Footer link, pressed" height="37"> 

| State | Values |
|---|---|
| default (same: hover, pressed) | size 203.59 x 37; padding 11px 0px; background transparent; text Clarkson 12/normal 400, #0e0e0e `text-soft` |
| focus-visible | outline 1px auto #005fcc `palette.focus-blue`, offset 1px |

#### Social link

<a id="social-link"></a>`social-link`, on home. A social icon link in the footer (Instagram, Pinterest, Facebook, LinkedIn, YouTube): the mark is painted as a background image, not an inline SVG.

<img src="components/crops/social-link-default.png" alt="Social link, default" height="32"> <img src="components/crops/social-link-hover.png" alt="Social link, hover" height="32"> <img src="components/crops/social-link-focus-visible.png" alt="Social link, focus-visible" height="32"> <img src="components/crops/social-link-pressed.png" alt="Social link, pressed" height="32"> 

| State | Values |
|---|---|
| default | size 32 x 32; radius 50%; background transparent; text Clarkson 16/16 400, #0000ee; transition background-color 0.2s ease |
| hover | background #f0f0f0 `palette.fog-deep` |
| focus-visible | outline 1px auto #005fcc `palette.focus-blue`, offset 1px |
| pressed | background #f0f0f0 `palette.fog-deep`; text Clarkson 16/16 400, #ff0000 |

#### Legal link

<a id="footer-legal"></a>`footer-legal`, on home. A legal foot link (Terms of Service, Privacy Policy).

<img src="components/crops/footer-legal-default.png" alt="Legal link, default" height="24"> <img src="components/crops/footer-legal-hover.png" alt="Legal link, hover" height="24"> <img src="components/crops/footer-legal-focus-visible.png" alt="Legal link, focus-visible" height="24"> <img src="components/crops/footer-legal-pressed.png" alt="Legal link, pressed" height="24"> 

| State | Values |
|---|---|
| default (same: hover, pressed) | size 40.52 x 15; background transparent; text Clarkson 12/normal 400, #0e0e0e `text-soft` |
| focus-visible | outline 1px auto #005fcc `palette.focus-blue`, offset 1px |

### Pricing

The pricing page: a photographic hero band (a background image, not a flat fill) with the serif headline and the white-pill annual/monthly segment, three white plan cards on 1px hairlines with ink Start-free-trial buttons, then the navy FAQ accordion with white rows.

#### Pricing plans block

<a id="pricing-hero"></a>`pricing-hero`, on pricing. The plan cards row: three or four tiers each with a name, blurb, monthly price, feature list and a CTA.

<img src="components/crops/pricing-hero-default.png" alt="Pricing plans block, default" height="120"> 

| State | Values |
|---|---|
| default | size 1440 x 1395; background transparent; image url(…); text Clarkson Serif 48/48 500, #ffffff `text-inverse` |

#### Plan card

<a id="plan-card"></a>`plan-card`, on pricing. A pricing tier card (~447x436): name, price, feature list with tooltip markers, Start free trial CTA.

<img src="components/crops/plan-card-default.png" alt="Plan card, default" height="120"> <img src="components/crops/plan-card-hover.png" alt="Plan card, hover" height="120"> 

| State | Values |
|---|---|
| default (same: hover) | size 446.67 x 436; background transparent; text Clarkson Serif 32/40 500, #0e0e0e `text-soft` |

Child layers: a 0x0 background #283849 `surface-inverse` radius 12px; a 138.7x46 background #283849 `surface-inverse` radius 12px; div 402.7x1 background #e7e7e7 `palette.line-divider`

#### Plan name

<a id="plan-name"></a>`plan-name`, on pricing. The tier name on a plan card (Starter, Emerging, Growing, Powerhouse), a .phase2-plan-title div.

<img src="components/crops/plan-name-default.png" alt="Plan name, default" height="40"> 

| State | Values |
|---|---|
| default | size 85.3 x 40; background transparent; text Clarkson Serif 32/40 500, #0e0e0e `text-soft` |

#### Plan price

<a id="plan-price"></a>`plan-price`, on pricing. The monthly price figure on a tier card.

<img src="components/crops/plan-price-default.png" alt="Plan price, default" height="27"> 

| State | Values |
|---|---|
| default | size 100.09 x 27; background transparent; text Clarkson 18/27 500, #0e0e0e `text-soft` |

#### Plan CTA

<a id="plan-cta"></a>`plan-cta`, on pricing. The "Start free trial" button on a tier card: measured and state-forced, never followed.

<img src="components/crops/plan-cta-default.png" alt="Plan CTA, default" height="46"> <img src="components/crops/plan-cta-hover.png" alt="Plan CTA, hover" height="46"> <img src="components/crops/plan-cta-focus-visible.png" alt="Plan CTA, focus-visible" height="46"> <img src="components/crops/plan-cta-pressed.png" alt="Plan CTA, pressed" height="41"> 

| State | Values |
|---|---|
| default | size 138.66 x 46; padding 12px 24px; radius 12px; background #283849 `surface-inverse`; text Clarkson 14/22 500, #ffffff `text-inverse`; transition all 0.15s ease |
| hover | background #1e2d3a `palette.ink-pressed` |
| focus-visible | background #1e2d3a `palette.ink-pressed`; outline 2px solid #283849 `palette.ink`, offset 2px |
| pressed | size 124.79 x 41.4; background #1e2d3a `palette.ink-pressed`; transform scale(0.9) |

#### Plan feature row

<a id="plan-feature"></a>`plan-feature`, on pricing. A feature line in a plan card; the marker holds a tooltip on hover.

<img src="components/crops/plan-feature-default.png" alt="Plan feature row, default" height="24"> <img src="components/crops/plan-feature-hover.png" alt="Plan feature row, hover" height="24"> 

| State | Values |
|---|---|
| default (same: hover) | size 402.67 x 22; background transparent; text Clarkson 14/22 500, #0e0e0e `text-soft` |

Child layers: span 67.6x20 image linear-gradient(90deg, #b7b7b7 `palette.gray` 1px, transparent 0px); div 250x88 background #0e0e0e `palette.ink-0e` radius 4px shadow rgba(0, 0, 0, 0.08) 0px 0px 1px 0px, rgba(0, 0, 0, 0.12) 0px 8px 32px 0px

#### FAQ accordion

<a id="faq-accordion"></a>`faq-accordion`, on pricing. The pricing FAQ: button.accordion-title questions expanding .accordion-panel answers.

<img src="components/crops/faq-accordion-default.png" alt="FAQ accordion, default" height="120"> 

| State | Values |
|---|---|
| default | size 640 x 1007.72; background transparent; text Clarkson Serif 24/27.6 500, #ffffff `text-inverse` |

Child layers: button 640x92.6 border 1px solid rgba(255, 255, 255, 0.1) `border-on-dark`; button 640x92.6 border 1px solid rgba(255, 255, 255, 0.1) `border-on-dark`; button 640x92.6 border 1px solid rgba(255, 255, 255, 0.1) `border-on-dark`

#### FAQ question

<a id="accordion-title"></a>`accordion-title`, on pricing. An accordion question row; pressing it is a local toggle that reveals the answer.

<img src="components/crops/accordion-title-default.png" alt="FAQ question, default" height="93"> <img src="components/crops/accordion-title-hover.png" alt="FAQ question, hover" height="93"> <img src="components/crops/accordion-title-focus-visible.png" alt="FAQ question, focus-visible" height="93"> <img src="components/crops/accordion-title-pressed.png" alt="FAQ question, pressed" height="93"> 

| State | Values |
|---|---|
| default (same: hover, pressed) | size 640 x 92.59; padding 32px 0px; border B: 1px solid rgba(255, 255, 255, 0.1) `border-on-dark`; background transparent; text Clarkson Serif 24/27.6 500, #ffffff `text-inverse` |
| focus-visible | outline 1px auto #005fcc `palette.focus-blue`, offset 0px |

Child layers: button 640x92.6 border 1px solid rgba(255, 255, 255, 0.1) `border-on-dark`

#### FAQ answer

<a id="accordion-panel"></a>`accordion-panel`, on pricing. An expanded accordion answer, opened through its own question toggle.

<img src="components/crops/accordion-panel-default.png" alt="FAQ answer, default" height="120"> 

| State | Values |
|---|---|
| default | size 640 x 145; border B: 1px solid rgba(255, 255, 255, 0.1) `border-on-dark`; background transparent; text Clarkson 16/26 400, #ffffff `text-inverse`; transition max-height 0.2s ease-out |

Child layers: div 640x145 border 1px solid rgba(255, 255, 255, 0.1) `border-on-dark`

#### FAQ question, open

<a id="accordion-title-open"></a>`accordion-title-open`, on pricing. The question in its expanded state (accordion-active / aria-expanded).

<img src="components/crops/accordion-title-open-default.png" alt="FAQ question, open, default" height="92"> 

| State | Values |
|---|---|
| default | size 640 x 91.59; padding 32px 0px; background transparent; text Clarkson Serif 24/27.6 500, #ffffff `text-inverse` |

### Auth gate (Squarespace)

Squarespace's shared account surface: /get-started lands on a white 'Create your account' dialog (Continue with Google/Apple/Email rows on 1px black rules, MORE OPTIONS caps toggle) and secure.acuityscheduling.com/login on the sign-in card with underlined fields, a greyed LOG IN and the same OAuth rows. Measured and state-forced, never submitted.

#### Create-account card

<a id="gate-card"></a>`gate-card`, on getstarted. The Squarespace account gate "Create your account": a centred ~540px card with provider buttons and legal links — the start of the signup flow, never submitted.

<img src="components/crops/gate-card-default.png" alt="Create-account card, default" height="120"> 

| State | Values |
|---|---|
| default | size 540 x 572; radius 6px; background #ffffff `surface`; shadow rgba(0, 0, 0, 0.12) 0px 16px 64px 0px, rgba(0, 0, 0, 0.08) 0px 0px 1px 0px; text Clarkson 20/28 600, #0e0e0e `text-soft` |

#### Continue with Google

<a id="gate-google"></a>`gate-google`, on getstarted. The Google OAuth row on the create-account card. Measured, never pressed.

<img src="components/crops/gate-google-default.png" alt="Continue with Google, default" height="55"> <img src="components/crops/gate-google-hover.png" alt="Continue with Google, hover" height="55"> <img src="components/crops/gate-google-focus-visible.png" alt="Continue with Google, focus-visible" height="55"> <img src="components/crops/gate-google-pressed.png" alt="Continue with Google, pressed" height="55"> 

| State | Values |
|---|---|
| default (same: hover, pressed) | size 452 x 55; padding 0px 22px; border 1px solid #000000 `border-strong`; background transparent; text Clarkson 14/22 500, #000000 `text-strong`; transition transform 0.05s ease |
| focus-visible | shadow #ffffff 0px 0px 0px 2px, #000000 0px 0px 0px 4px; outline 2px solid transparent, offset 2px |

#### Continue with Apple

<a id="gate-apple"></a>`gate-apple`, on getstarted. The Apple OAuth row. Measured, never pressed.

<img src="components/crops/gate-apple-default.png" alt="Continue with Apple, default" height="55"> <img src="components/crops/gate-apple-hover.png" alt="Continue with Apple, hover" height="55"> <img src="components/crops/gate-apple-focus-visible.png" alt="Continue with Apple, focus-visible" height="55"> <img src="components/crops/gate-apple-pressed.png" alt="Continue with Apple, pressed" height="55"> 

| State | Values |
|---|---|
| default (same: hover, pressed) | size 452 x 55; padding 0px 22px; border 1px solid #000000 `border-strong`; background transparent; text Clarkson 14/22 500, #000000 `text-strong`; transition transform 0.05s ease |
| focus-visible | shadow #ffffff 0px 0px 0px 2px, #000000 0px 0px 0px 4px; outline 2px solid transparent, offset 2px |

#### Continue with Email

<a id="gate-email"></a>`gate-email`, on getstarted. The email signup row — leads to an email field on the next step, which is not reached.

<img src="components/crops/gate-email-default.png" alt="Continue with Email, default" height="55"> <img src="components/crops/gate-email-hover.png" alt="Continue with Email, hover" height="55"> <img src="components/crops/gate-email-focus-visible.png" alt="Continue with Email, focus-visible" height="55"> <img src="components/crops/gate-email-pressed.png" alt="Continue with Email, pressed" height="55"> 

| State | Values |
|---|---|
| default (same: hover, pressed) | size 452 x 55; padding 0px 22px; border 1px solid #000000 `border-strong`; background transparent; text Clarkson 14/22 500, #000000 `text-strong`; transition transform 0.05s ease |
| focus-visible | shadow #ffffff 0px 0px 0px 2px, #000000 0px 0px 0px 4px; outline 2px solid transparent, offset 2px |

#### More options expander

<a id="more-options"></a>`more-options`, on getstarted. The "MORE OPTIONS" text expander revealing further providers — a local toggle.

<img src="components/crops/more-options-default.png" alt="More options expander, default" height="55"> <img src="components/crops/more-options-hover.png" alt="More options expander, hover" height="55"> <img src="components/crops/more-options-focus-visible.png" alt="More options expander, focus-visible" height="55"> <img src="components/crops/more-options-pressed.png" alt="More options expander, pressed" height="55"> 

| State | Values |
|---|---|
| default (same: hover, focus-visible, pressed) | size 98.59 x 55; background transparent; text Clarkson 12/22 500, #0e0e0e `text-soft`; transition transform 0.05s ease |

Child layers: div 0x2 border 2px solid #0e0e0e `palette.ink-0e`

#### Extra provider, revealed

<a id="more-options-open"></a>`more-options-open`, on getstarted. A provider row revealed by MORE OPTIONS.

<img src="components/crops/more-options-open-default.png" alt="Extra provider, revealed, default" height="55"> 

| State | Values |
|---|---|
| default | size 452 x 55; padding 0px 22px; border 1px solid #000000 `border-strong`; background transparent; text Clarkson 14/22 500, #000000 `text-strong`; transition transform 0.05s ease |

#### Sign-in card

<a id="login-card"></a>`login-card`, on login. The Squarespace "Log into Acuity Scheduling with your Squarespace account" card (styled-components css-* classes): email and password fields, LOG IN, OR divider, OAuth rows — the gate for the app, never submitted.

*Not found on the captured pages — an honest miss, kept so the gap is visible.*

#### Email field

<a id="login-email"></a>`login-email`, on login. The EMAIL ADDRESS field; typed and deleted, never submitted.

<img src="components/crops/login-email-default.png" alt="Email field, default" height="24"> <img src="components/crops/login-email-focused.png" alt="Email field, focused" height="24"> <img src="components/crops/login-email-filled.png" alt="Email field, filled" height="24"> 

| State | Values |
|---|---|
| default (same: focused, filled) | size 326.63 x 22; background transparent; text Clarkson 14/22 400, #0e0e0e `text-soft`; placeholder #949494 `muted` |

#### Password field

<a id="login-password"></a>`login-password`, on login. The PASSWORD field; focused only, never typed.

<img src="components/crops/login-password-default.png" alt="Password field, default" height="24"> <img src="components/crops/login-password-focused.png" alt="Password field, focused" height="24"> 

| State | Values |
|---|---|
| default (same: focused) | size 326.63 x 22; background transparent; text Clarkson 14/22 500, #0e0e0e `text-soft`; placeholder #949494 `muted` |

#### Log in button

<a id="login-submit"></a>`login-submit`, on login. The LOG IN submit. Measured, never pressed.

<img src="components/crops/login-submit-default.png" alt="Log in button, default" height="44"> <img src="components/crops/login-submit-hover.png" alt="Log in button, hover" height="44"> <img src="components/crops/login-submit-focus-visible.png" alt="Log in button, focus-visible" height="44"> <img src="components/crops/login-submit-pressed.png" alt="Log in button, pressed" height="44"> 

| State | Values |
|---|---|
| default (same: hover, focus-visible, pressed) | size 326.63 x 44; padding 0px 16px; background #f2f2f2 `palette.fog`; text Clarkson 12/22 500, #b7b7b7 `disabled-text`; transition transform 0.05s ease |

#### OAuth Google

<a id="oauth-google"></a>`oauth-google`, on login. The Google OAuth row on the sign-in card. Measured, never pressed.

<img src="components/crops/oauth-google-default.png" alt="OAuth Google, default" height="55"> <img src="components/crops/oauth-google-hover.png" alt="OAuth Google, hover" height="55"> <img src="components/crops/oauth-google-focus-visible.png" alt="OAuth Google, focus-visible" height="55"> <img src="components/crops/oauth-google-pressed.png" alt="OAuth Google, pressed" height="55"> 

| State | Values |
|---|---|
| default (same: hover, pressed) | size 326.63 x 55; padding 0px 22px; border 1px solid #000000 `border-strong`; background transparent; text Clarkson 14/22 500, #000000 `text-strong`; transition transform 0.05s ease |
| focus-visible | shadow #ffffff 0px 0px 0px 2px, #000000 0px 0px 0px 4px; outline 2px solid transparent, offset 2px |

#### OAuth Apple

<a id="oauth-apple"></a>`oauth-apple`, on login. The Apple OAuth row.

<img src="components/crops/oauth-apple-default.png" alt="OAuth Apple, default" height="55"> <img src="components/crops/oauth-apple-hover.png" alt="OAuth Apple, hover" height="55"> <img src="components/crops/oauth-apple-focus-visible.png" alt="OAuth Apple, focus-visible" height="55"> <img src="components/crops/oauth-apple-pressed.png" alt="OAuth Apple, pressed" height="55"> 

| State | Values |
|---|---|
| default (same: hover, pressed) | size 326.63 x 55; padding 0px 22px; border 1px solid #000000 `border-strong`; background transparent; text Clarkson 14/22 500, #000000 `text-strong`; transition transform 0.05s ease |
| focus-visible | shadow #ffffff 0px 0px 0px 2px, #000000 0px 0px 0px 4px; outline 2px solid transparent, offset 2px |

#### OAuth Facebook

<a id="oauth-facebook"></a>`oauth-facebook`, on login. The Facebook OAuth row.

<img src="components/crops/oauth-facebook-default.png" alt="OAuth Facebook, default" height="55"> <img src="components/crops/oauth-facebook-hover.png" alt="OAuth Facebook, hover" height="55"> <img src="components/crops/oauth-facebook-focus-visible.png" alt="OAuth Facebook, focus-visible" height="55"> <img src="components/crops/oauth-facebook-pressed.png" alt="OAuth Facebook, pressed" height="55"> 

| State | Values |
|---|---|
| default (same: hover, pressed) | size 326.63 x 55; padding 0px 22px; border 1px solid #000000 `border-strong`; background transparent; text Clarkson 14/22 500, #000000 `text-strong`; transition transform 0.05s ease |
| focus-visible | shadow #ffffff 0px 0px 0px 2px, #000000 0px 0px 0px 4px; outline 2px solid transparent, offset 2px |

#### Can't log in link

<a id="cant-login"></a>`cant-login`, on login. The recovery link under the OAuth rows.

<img src="components/crops/cant-login-default.png" alt="Can't log in link, default" height="36"> <img src="components/crops/cant-login-hover.png" alt="Can't log in link, hover" height="36"> <img src="components/crops/cant-login-focus-visible.png" alt="Can't log in link, focus-visible" height="36"> <img src="components/crops/cant-login-pressed.png" alt="Can't log in link, pressed" height="36"> 

| State | Values |
|---|---|
| default (same: hover, focus-visible, pressed) | size 93.05 x 36; background transparent; text Clarkson 12/22 500, #0e0e0e `text-soft`; transition transform 0.05s ease |

Child layers: div 0x2 border 2px solid #0e0e0e `palette.ink-0e`

#### Create account link

<a id="create-account-link"></a>`create-account-link`, on login. The CREATE ACCOUNT tab beside LOG IN on the gate.

<img src="components/crops/create-account-link-default.png" alt="Create account link, default" height="36"> <img src="components/crops/create-account-link-hover.png" alt="Create account link, hover" height="36"> <img src="components/crops/create-account-link-focus-visible.png" alt="Create account link, focus-visible" height="36"> <img src="components/crops/create-account-link-pressed.png" alt="Create account link, pressed" height="36"> 

| State | Values |
|---|---|
| default (same: hover, focus-visible, pressed) | size 116.27 x 36; background transparent; text Clarkson 12/22 500, #0e0e0e `text-soft`; transition transform 0.05s ease |

Child layers: div 0x2 border 2px solid #0e0e0e `palette.ink-0e`

### Mobile (390 wide)

The same site at 390: the bar collapses to wordmark plus hamburger, which opens a full-height white sheet over a 50% scrim — 28px Clarkson links on hairline rows, an ink Get started bar and a Log in. Focus inside the sheet is an amber ring.

#### Mobile header

<a id="m-header"></a>`m-header`, on mobile. The bar at 390: 55px, wordmark and a hamburger.

<img src="components/crops/m-header-default.png" alt="Mobile header, default" height="55"> 

| State | Values |
|---|---|
| default | size 390 x 55; padding 16px 20px; background transparent; transition background 0.25s ease-in-out |

#### Hamburger button

<a id="m-hamburger"></a>`m-hamburger`, on mobile. The menu trigger; opens the full-screen menu.

<img src="components/crops/m-hamburger-default.png" alt="Hamburger button, default" height="24"> <img src="components/crops/m-hamburger-hover.png" alt="Hamburger button, hover" height="24"> <img src="components/crops/m-hamburger-focus-visible.png" alt="Hamburger button, focus-visible" height="24"> <img src="components/crops/m-hamburger-pressed.png" alt="Hamburger button, pressed" height="24"> 

| State | Values |
|---|---|
| default (same: hover, pressed) | size 25 x 16; background transparent; text Clarkson 16/16 400, #222222 `text` |
| focus-visible | outline 1px auto #e59700 `palette.focus-amber`, offset 0px |

#### Mobile menu

<a id="m-menu"></a>`m-menu`, on mobile. The full-height menu the hamburger opens (.mobile-menu-container): primary links stacked.

<img src="components/crops/m-menu-default.png" alt="Mobile menu, default" height="120"> 

| State | Values |
|---|---|
| default | size 390 x 844; background rgba(0, 0, 0, 0.5) `palette.scrim`; text Clarkson 28/37.52 400, #2d2d2d `palette.ink-2d`; transition background 0.3s ease-in |

#### Mobile menu link

<a id="m-menu-link"></a>`m-menu-link`, on mobile. A primary link in the mobile menu.

<img src="components/crops/m-menu-link-default.png" alt="Mobile menu link, default" height="38"> <img src="components/crops/m-menu-link-hover.png" alt="Mobile menu link, hover" height="38"> <img src="components/crops/m-menu-link-focus-visible.png" alt="Mobile menu link, focus-visible" height="38"> <img src="components/crops/m-menu-link-pressed.png" alt="Mobile menu link, pressed" height="38"> 

| State | Values |
|---|---|
| default (same: hover, pressed) | size 350 x 37.52; background transparent; text Clarkson 28/37.52 400, #2d2d2d `palette.ink-2d` |
| focus-visible | outline 1px auto #e59700 `palette.focus-amber`, offset 1px |

#### Mobile hero

<a id="m-hero"></a>`m-hero`, on mobile. The hero at 390.

<img src="components/crops/m-hero-default.png" alt="Mobile hero, default" height="120"> 

| State | Values |
|---|---|
| default | size 390 x 1192.78; background transparent; text Clarkson Serif 32/38.4 500, #283849 `accent` |

Child layers: div 390x1192.8 image linear-gradient(66deg, #ebddda 0px, #ebdadb 75%, #f5eff6 100%); div::after 390pxx357.828px image linear-gradient(transparent, #ffffff `surface`); a 0x0 background #283849 `surface-inverse` radius 12px

## Gaps

- `carousel-nav` and `login-card` are honest misses: the testimonials carousel has no arrow buttons (a dotted indicator row only, see `carousel-dots`), and the login card's own wrapper element could not be isolated — its children (fields, submit, OAuth rows) are measured instead.
- Everything behind the sign-in is out of bounds: the scheduling app itself, account creation, checkout, the OAuth redirects. The gate and login card were measured and state-forced but never submitted, and no account exists to continue into.
- `social-link` and `m-menu-link`'s pressed rows show `rgb(255, 0, 0)`: those anchors carry no `color` of their own (default link blue `rgb(0, 0, 238)` at rest), so the forced `:active` falls back to the UA stylesheet's red. It is a measurement artifact of unstyled anchors, not a design value.
- The pricing hero's dark band is a background photograph (`pricing-background.webp`), not a flat fill — its sampled pixels (~#334e53) are image content. Likewise the home hero repaints one of nine declared pastel gradient variants per load (raw/css-vars.json); the tokens record the variant live during the capture.
- `plan-card` itself paints transparent: the white card with the hairline border and 12px radius is its `.plan-wrapper` sibling, which the paint layers record.
- The testimonials carousel auto-plays, so `testimonial-card` is measured on its first slide only and two captures of the same section can differ.
- Consent SDKs (OneTrust/Cookiebot) were aborted at the network layer before any banner mounted, so no consent UI was captured or measured — there was nothing to hide after the fact.
- Disabled, error, loading and selected states barely exist on the public surface: the disabled LOG IN (`field-disabled-bg`) is the only disabled control captured; error and loading states live behind submitted forms and were never reached.

