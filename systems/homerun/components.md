# Homerun components

The discovery list of every page and view captured, then one entry per component with crops of the real product, the icon index and the Gaps. Captured from www.homerun.co, jobs.homerun.co, app.homerun.co/login and app.homerun.hr/Account/Logon on 2026-11-17, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running page. Nothing was signed into, created, sent, uploaded or submitted.

The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) (83 components, 172 states). The layout geometry is in [raw/layout.json](raw/layout.json).

How to read an entry:

- A colour is its value followed by the palette token in [tokens.json](tokens.json) with the same value, when there is one. Text is written family size/line-height weight, then its colour, for example `GT America 16/24 400, #4a3e3e`, and is read from the first text node inside the component.
- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example "default (same: focus-visible)". When the root paints nothing, "Child layers" names the first nodes inside it that do.
- Crops are images of the component read from the live page, in [components/crops/](components/crops) (159 files, named `{component}-{state}.png`, at 2x). Screenshots are in [screenshots/](screenshots).

## Discovery list

Screenshots are named `{page}-light-{state}.png` (Homerun shows one light theme). Desktop shots are 1440 x 900 at 1x; `-full` shots are whole pages at 1x stitched from `.partN` tiles when the page is taller than one GPU texture; mobile shots are `mobile-{page}-light-{state}.png`, 780 wide (390 at 2x).

| Surface | URL | Screenshots |
|---|---|---|
| Home. Hero, rating row, feature accordions, testimonials, logo marquee, dark CTA band, footer. The two hover-open nav dropdowns captured. | `/` | [default](screenshots/home-light-default.png), [full](screenshots/home-light-full.png), [nav-login-open](screenshots/home-light-nav-login-open.png), [nav-resources-open](screenshots/home-light-nav-resources-open.png) |
| ATS product page. Hero, feature tabs, integration cards. | `/ats` | [default](screenshots/ats-light-default.png), [full](screenshots/ats-light-full.png) |
| HR product page. | `/hr` | [default](screenshots/hr-light-default.png), [full](screenshots/hr-light-full.png) |
| Product features page. | `/product/features` | [default](screenshots/features-light-default.png), [full](screenshots/features-light-full.png) |
| Pricing. Plan cards, feature table, FAQ (one item opened), CTA. | `/pricing` | [default](screenshots/pricing-light-default.png), [faq-open](screenshots/pricing-light-faq-open.png), [full](screenshots/pricing-light-full.png) |
| Customers page. | `/customers` | [default](screenshots/customers-light-default.png), [full](screenshots/customers-light-full.png) |
| About page. | `/about` | [default](screenshots/about-light-default.png), [full](screenshots/about-light-full.png) |
| Contact page. | `/contact` | [default](screenshots/contact-light-default.png), [full](screenshots/contact-light-full.png) |
| Blog index. | `/blog` | [default](screenshots/blog-light-default.png), [full](screenshots/blog-light-full.png) |
| Job-template library. | `/templates` | [default](screenshots/templates-light-default.png), [full](screenshots/templates-light-full.png) |
| Integrations directory. | `/integrations` | [default](screenshots/integrations-light-default.png), [full](screenshots/integrations-light-full.png) |
| Guides index. | `/guides` | [default](screenshots/guides-light-default.png), [full](screenshots/guides-light-full.png) |
| Product updates index. | `/updates/` | [default](screenshots/updates-light-default.png), [full](screenshots/updates-light-full.png) |
| Start-free-trial page. | `/trial` | [default](screenshots/trial-light-default.png), [full](screenshots/trial-light-full.png) |
| Privacy statement. | `/privacy-statement` | [default](screenshots/privacy-light-default.png), [full](screenshots/privacy-light-full.png) |
| Careers site root (jobs.homerun.co): header, job list, cookie banner hidden. | `https://jobs.homerun.co/` | [default](screenshots/careers-light-default.png), [full](screenshots/careers-light-full.png) |
| A job ad on the careers site: title, Apply button, description prose, share and back. | `https://jobs.homerun.co/open/en` | [default](screenshots/job-light-default.png), [full](screenshots/job-light-full.png) |
| The public application form: steps strip, fields, upload and checkbox, Back/Next. At rest; nothing typed, uploaded or submitted. | `https://jobs.homerun.co/open/en/apply` | [default](screenshots/apply-light-default.png) |
| ATS sign-in at app.homerun.co/login. SSO buttons, email/password, Log in. At rest; never submitted. | `https://app.homerun.co/login` | [default](screenshots/signin-light-default.png) |
| HR sign-in at app.homerun.hr/Account/Logon. Email/password, green Log in. At rest; never submitted. | `https://app.homerun.hr/Account/Logon` | [default](screenshots/signinhr-light-default.png) |
| Home at 390: bar, hero, full page, and the hamburger's open menu sheet. | `/` | [default](screenshots/mobile-home-light-default.png), [full](screenshots/mobile-home-light-full.png), [menu-open](screenshots/mobile-home-light-menu-open.png) |
| Pricing at 390. | `/pricing` | [default](screenshots/mobile-pricing-light-default.png), [full](screenshots/mobile-pricing-light-full.png) |
| ATS product page at 390. | `/ats` | [default](screenshots/mobile-ats-light-default.png), [full](screenshots/mobile-ats-light-full.png) |
| Careers site at 390. | `https://jobs.homerun.co/` | [default](screenshots/mobile-careers-light-default.png), [full](screenshots/mobile-careers-light-full.png) |
| Application form at 390. | `https://jobs.homerun.co/open/en/apply` | [default](screenshots/mobile-apply-light-default.png) |

### Overlays and transient states

| State | Where | How it was reached | Captured |
|---|---|---|---|
| Resources dropdown | marketing nav | hovering the Resources toggle (Webflow data-hover) | [home-light-nav-resources-open](screenshots/home-light-nav-resources-open.png), [nav-resources-panel](#resources-panel) |
| Log in dropdown | marketing nav | hovering the Log in toggle | [home-light-nav-login-open](screenshots/home-light-nav-login-open.png), [nav-login-panel](#log-in-panel) |
| Pricing FAQ, opened | pricing | the question's own toggle | [pricing-light-faq-open](screenshots/pricing-light-faq-open.png), [faq-item](#faq-item) |
| Mobile menu, opened | home at 390 | the hamburger's own press (an in-page click; the tap layer never reaches it) | [mobile-home-light-menu-open](screenshots/mobile-home-light-menu-open.png), [m-menu-open](#m-menu-open) |
| Cookie consent | careers site | present on load; hidden for every capture, never accepted or declined | [cookie-banner](#cookie-banner) |

## Shared values

Values that apply across entries, from the measurement files.

**Focus.** 21 components were given a real keyboard focus. 12 draw a ring: `nav-link` (1px auto #101010, offset 1px), `nav-product-pill` (1px auto #101010, offset 1px), `nav-demo` (1px auto #101010, offset 1px), `nav-trial` (1px auto #101010, offset 1px), `hero-cta` (1px auto #101010, offset 1px), `hero-demo` (1px auto #101010, offset 1px), `footer-link` (1px auto #101010, offset 1px), `plan-button` (1px auto #101010, offset 1px), `pricing-cta` (1px auto #101010, offset 1px), `signin-sso` (5px auto #101010, offset 0px), `hr-button` (2px solid #00b16b `secondary.green`, offset 2px), `hr-link` (1px auto #101010, offset 1px). The other 9 draw none, so a keyboard user sees no change: `careers-filter`, `careers-job-card`, `job-apply`, `job-share`, `apply-back`, `signin-button`, `signin-link`, `m-menu-link`, `job-back`.
Focus could not be captured on 2: keyboard focus never reached them (or they took focus without matching :focus-visible), so their focus look is unknown, not absent: `careers-share`, `careers-all-jobs`.

**Pressed.** The blue controls darken on press to blue-600 `#254cda` (the hero CTA, the nav trial button and the ATS sign-in button all read the same value); the dark buttons lighten toward brown-300 `#4a3e3e`; the HR button darkens toward `#128053`. The careers and apply buttons hold their fill. What changed is in each entry's state row.

**Motion.** Transitions measured on the components, by duration.

| Duration | Easing | Property | Where |
|---|---|---|---|
| 0.1s | `cubic-bezier(0.455, 0.03, 0.515, 0.955)` | all | apply-next |
| 0.15s | `cubic-bezier(0.4, 0, 0.2, 1)` | all | hr-button |
| 0.15s | `cubic-bezier(0.455, 0.03, 0.515, 0.955)` | all | careers-carousel |
| 0.18s | `cubic-bezier(0.55, 0.025, 0.455, 0.98)` | all | careers-all-jobs, careers-job-card, careers-logo, careers-share, job-apply |
| 0.2s | `ease` | all, background-color, color | apply-back, ats-integrate-card, faq-item, feature-accordion, footer-link, hero-cta, job-back, newsletter-button and more |
| 0.2s | `ease-out` | all | apply-email, apply-field |
| 0.3s | `ease` | all, background-color | hero-demo, m-menu-link, nav-demo, nav-link, nav-login, nav-login-link, nav-product-pill, nav-resources-link and more |
| 0.3s | `ease-out` | all, background, border-color, box-shadow, color | careers-filter, signin-button, signin-email, signin-link, signin-password |
| 0.4s | `ease` | all, transform | careers-header, m-menu-open |

**Layout grid.** Read on each page at each width ([raw/layout.json](raw/layout.json)).

| Page | 1440 | 1920 | 1024 | 390 |
|---|---|---|---|---|
| home | content x 0, 1440 wide; grid 208 208 208 gap 8px | content x 0, 1920 wide; grid 208 208 208 gap 8px | content x 0, 1024 wide; grid 204.6 204.6 204.6 gap 8px | content x 0, 390 wide |
| pricing | content x 0, 1440 wide; grid 652 652 gap 16px | content x 0, 1920 wide; grid 672 672 gap 16px | content x 0, 1024 wide; grid 444 444 gap 16px | content x 0, 390 wide; grid 171 171 gap 16px |
| ats | content x 0, 1440 wide; grid 203.3 203.3 203.3 203.3 203.3 203.3 gap 8px | content x 0, 1920 wide; grid 203.3 203.3 203.3 203.3 203.3 203.3 gap 8px | content x 0, 1024 wide; grid 144 144 144 144 144 144 gap 8px | content x 0, 390 wide; grid 175 175 gap 8px |
| careers | content x 0, 1440 wide; grid 628 628 gap 24px | content x 0, 1920 wide; grid 628 628 gap 24px | content x 0, 1024 wide; grid 460 460 gap 24px | content x 0, 390 wide |
| job | content x 0, 1440 wide | - | - | - |
| signin | content x 0, 1440 wide | - | - | - |

**Card shapes.** Default-state values; the entries hold the states.

| Card | Size | Border | Radius | Background | Shadow | Padding |
|---|---|---|---|---|---|---|
| [Plan card](#plan-card) | 652 x 442 | 1px solid #e3e1dd `beige.700` | 32px | #ffffff `white` | none | 48px |
| [Testimonial card](#testimonial-card) | 400 x 354.38 | - | 20px | #f5f1ec | #d386de 0px 4px 5px 0px | 60px 50px |
| [ATS card](#ats-card) | 1260 x 997.98 | - | 40px | #faf9f7 `beige.400` | none | 48px 64px |
| [Integration card](#integration-card) | 356 x 209.19 | - | 20px | #ffffff `white` | #e3e1dd 0px 2px 0px 0px | 24px |
| [Job card](#job-card) | 1080 x 54 | - | 8px 8px 0px 0px | #ffffff `white` | none | 14px 20px |
| [Sign-in card](#sign-in-card) | 1440 x 900 | - | 20px 20px 0px 0px | #ffffff `white` | none | 0 |
| [HR sign-in card](#hr-sign-in-card) | 382 x 278 | - | 10px | #f5f3ef `beige.500` | none | 0 |
| [Cookie banner](#cookie-banner) | 775 x 104 | - | 5px | #ffffff `white` | rgba(33, 43, 54, 0.15) 0px 2px 5px 0px | 30px |
| [FAQ item](#faq-item) | 677.64 x 56 | - | 10px | #ffffff `white` | none | 0 |
| [Feature accordion](#feature-accordion) | 548 x 56 | - | 10px | #ffffff `white` | none | 0 |
| [Resources panel](#resources-panel) | 436 x 240 | - | 28px | #ffffff `white` | rgba(67, 65, 61, 0.15) 0px 5px 20px 0px | 0 |
| [Log-in panel](#log-in-panel) | 234 x 138 | - | 20px | #ffffff `white` | rgba(67, 65, 61, 0.15) 0px 5px 20px 0px | 0 |
| [Mobile menu, open](#mobile-menu-open) | 358 x 451 | 1px solid #edebe7 `beige.600` | 20px | #ffffff `white` | rgba(67, 65, 61, 0.15) 0px 5px 20px 0px | 0px 0px 64px 0px |
| [Next-step button](#next-step-button) | 538 x 80 | - | 0px 0px 5px 5px | #4f75fe `blue.500` | none | 0 |

## Components

### Shell and navigation

The sticky top bar of the marketing site: logo, product pill, the Resources and Log in dropdowns (both open on hover), the dark Book-a-demo button and the blue Start-free-trial button.

#### Nav bar
The sticky 1440 top nav (position:sticky): logo, product pills, dropdown menus, Log-in/Book-a-demo/Start-free-trial actions. Read as `header` on the home page.

**Values (default).** size 1440 x 104; background #ffffff `white`; text GT America 16/22 400, #4a3e3e `brown.300`; icon 42 x 28, #4a3e3e `brown.300`.

![Nav bar default](components/crops/header-default.png)

#### Logo
The HOMERUN logotype anchor (wordmark image). Read as `logo` on the home page.

**Values (default).** size 126 x 26; background transparent; text GT America 14/20 400, #333333.

![Logo default](components/crops/logo-default.png)

#### Nav link
A text nav link (Pricing) in the top bar. Read as `nav-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 74 x 58; padding 12px; radius 10px; background transparent; text GT America 16/22 400, #4a3e3e `brown.300`; transition background-color 0.3s ease |
| hover | background #f5f3ef `beige.500` |
| focus-visible | outline 1px auto #101010, offset 1px |
| pressed | background #f5f3ef `beige.500` |

![Nav link default](components/crops/nav-link-default.png) ![Nav link hover](components/crops/nav-link-hover.png) ![Nav link focus-visible](components/crops/nav-link-focus-visible.png) ![Nav link pressed](components/crops/nav-link-pressed.png)

#### Nav product pill
The "ATS Organise your hiring" pill — an icon-bearing product link that tints its icon on hover. Read as `nav-product-pill` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 221 x 58; padding 12px; radius 10px; background transparent; text GT America 16/22 400, #4a3e3e `brown.300`; transition background-color 0.3s ease; icon 42 x 28, #4a3e3e `brown.300` |
| hover | background #f5f3ef `beige.500`; icon 42 x 28, #4f75fe `blue.500` |
| focus-visible | outline 1px auto #101010, offset 1px |
| pressed | background #f5f3ef `beige.500`; icon 42 x 28, #4f75fe `blue.500` |

![Nav product pill default](components/crops/nav-product-pill-default.png) ![Nav product pill hover](components/crops/nav-product-pill-hover.png) ![Nav product pill focus-visible](components/crops/nav-product-pill-focus-visible.png) ![Nav product pill pressed](components/crops/nav-product-pill-pressed.png)

#### Resources dropdown
The Resources nav dropdown trigger — a hover-open w-dropdown whose panel links Blog/Guides/Templates/Integrations/Help center and Product updates/Careers/Refer/About. Read as `nav-resources` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: opened) | size 121 x 58; padding 0px 12px 0px 0px; radius 10px; background transparent; text GT America 16/22 400, #4a3e3e `brown.300`; icon 12 x 13, #8a7878 `named.coffee-600` |
| hover | background #f5f3ef `beige.500` |

![Resources dropdown default](components/crops/nav-resources-default.png) ![Resources dropdown hover](components/crops/nav-resources-hover.png) ![Resources dropdown opened](components/crops/nav-resources-opened.png)

#### Resources panel
The open Resources mega-panel (nav_resources-update): two link columns, rounded + shadowed card. Read as `nav-resources-panel` on the home page.

**Values (default).** size 436 x 240; background rgba(221, 221, 221, 0); text GT America 16/18 400, #131313 `brown.700`; transform translate(-281.6px, 0px); icon 24 x 24, #4f75fe `blue.500`.

![Resources panel default](components/crops/nav-resources-panel-default.png)

#### Resources link
A link row inside the open Resources panel; focus/pressed are unreachable while the panel is hover-held. Read as `nav-resources-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 186 x 40; padding 8px; background transparent; text GT America 16/18 400, #131313 `brown.700`; transition all 0.3s ease; icon 24 x 24, #4f75fe `blue.500` |
| hover | radius 12px; background #f5f3ef `beige.500` |

![Resources link default](components/crops/nav-resources-link-default.png) ![Resources link hover](components/crops/nav-resources-link-hover.png)

#### Log-in dropdown
The "Log in" ghost-button dropdown — opens the ATS/HR sign-in menu on hover. Read as `nav-login` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: opened) | size 78 x 42; padding 4px 16px; border 1px solid #edebe7 `beige.600`; radius 12px; background transparent; text GT America 16/32 400, #4a3e3e `brown.300`; transition background-color 0.3s ease |
| hover | background #e8e5de `named.sky` |

![Log-in dropdown default](components/crops/nav-login-default.png) ![Log-in dropdown hover](components/crops/nav-login-hover.png) ![Log-in dropdown opened](components/crops/nav-login-opened.png)

#### Log-in panel
The open Log-in menu: "ATS Organise your hiring" and "HR Manage your team" sign-in links, measured never followed. Read as `nav-login-panel` on the home page.

**Values (default).** size 234 x 138; background transparent; text GT America 16/22 400, #2d2323 `brown.500`; icon 43.74 x 30.12, #4f75fe `blue.500`.

Child layers that carry the look: div 234x130 background #ffffff `white` radius 20px shadow rgba(67, 65, 61, 0.15) 0px 5px 20px 0px; a 218x57 background #f5f3ef `beige.500` radius 10px.

![Log-in panel default](components/crops/nav-login-panel-default.png)

#### Log-in menu link
A sign-in link inside the open Log-in menu (to app.homerun.co/login); measured never followed. Read as `nav-login-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 218 x 57; padding 14px 8px; radius 10px; background #f5f3ef `beige.500`; text GT America 16/22 400, #2d2323 `brown.500`; transition background-color 0.3s ease; icon 43.74 x 30.12, #4f75fe `blue.500` |

![Log-in menu link default](components/crops/nav-login-link-default.png) ![Log-in menu link hover](components/crops/nav-login-link-hover.png)

#### Book-a-demo button
The dark "Book a demo" button in the top bar; links to a HubSpot meeting page, never followed. Read as `nav-demo` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 126.91 x 72; padding 4px 16px; radius 12px; background #2d2323 `brown.500`; text GT America 16/32 400, #ffffff `white`; transition background-color 0.3s ease |
| hover | background #4a3e3e `brown.300` |
| focus-visible | outline 1px auto #101010, offset 1px |
| pressed | background #4a3e3e `brown.300` |

![Book-a-demo button default](components/crops/nav-demo-default.png) ![Book-a-demo button hover](components/crops/nav-demo-hover.png) ![Book-a-demo button focus-visible](components/crops/nav-demo-focus-visible.png) ![Book-a-demo button pressed](components/crops/nav-demo-pressed.png)

#### Start-trial button
The blue "Start free trial" button in the top bar; links to /trial, never followed. Read as `nav-trial` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 135.89 x 72; padding 4px 16px; radius 12px; background #4f75fe `blue.500`; text GT America 16/32 400, #ffffff `white`; transition background-color 0.3s ease |
| hover | background #254cda `blue.600` |
| focus-visible | outline 1px auto #101010, offset 1px |
| pressed | background #254cda `blue.600` |

![Start-trial button default](components/crops/nav-trial-default.png) ![Start-trial button hover](components/crops/nav-trial-hover.png) ![Start-trial button focus-visible](components/crops/nav-trial-focus-visible.png) ![Start-trial button pressed](components/crops/nav-trial-pressed.png)

### Home

The home page: GT Walsheim hero headline over the white ground, a blue primary CTA next to a dark secondary one, the rating row, feature accordions, testimonial cards on the beige band, the logo marquee and the closing dark CTA band.

#### Hero title
"Beautiful HR tools for modern teams." — the hero display headline. Read as `hero-title` on the home page.

**Values (default).** size 576 x 192; background transparent; text GT Walsheim 64/64 900, #382d2d `brown.400`.

![Hero title default](components/crops/hero-title-default.png)

#### Hero subline
The hero supporting paragraph under the headline. Read as `hero-sub` on the home page.

**Values (default).** size 640 x 92.39; background transparent; text GT America 22/30.8 400, #4a3e3e `brown.300`.

![Hero subline default](components/crops/hero-sub-default.png)

#### Hero CTA
"Try free for 15 days" — the large primary button with an arrow icon under the hero copy; links to /trial, never followed. Read as `hero-cta` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 234 x 52; padding 12px 16px 12px 20px; radius 12px; background #4f75fe `blue.500`; text GT America 20/28 400, #ffffff `white`; transition color 0.2s ease; icon 24 x 25, #ffffff `white` |
| hover | background #254cda `blue.600` |
| focus-visible | outline 1px auto #101010, offset 1px |
| pressed | background #254cda `blue.600` |

![Hero CTA default](components/crops/hero-cta-default.png) ![Hero CTA hover](components/crops/hero-cta-hover.png) ![Hero CTA focus-visible](components/crops/hero-cta-focus-visible.png) ![Hero CTA pressed](components/crops/hero-cta-pressed.png)

#### Hero secondary
The "Book a demo" bordered button beside the hero CTA. Read as `hero-demo` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 160 x 54; padding 12px 20px; border 1px solid #edebe7 `beige.600`; radius 12px; background #382d2d `brown.400`; text GT America 20/28 400, #ffffff `white`; transition background-color 0.3s ease |
| hover | background #4a3e3e `brown.300` |
| focus-visible | outline 1px auto #101010, offset 1px |
| pressed | background #4a3e3e `brown.300` |

![Hero secondary default](components/crops/hero-demo-default.png) ![Hero secondary hover](components/crops/hero-demo-hover.png) ![Hero secondary focus-visible](components/crops/hero-demo-focus-visible.png) ![Hero secondary pressed](components/crops/hero-demo-pressed.png)

#### Rating row
The social-proof row under the hero CTAs (Capterra rating, satisfaction, team count). Read as `rating-row` on the home page.

**Values (default).** size 640 x 50; background transparent; text GT America 13/15.6 500, #382d2d `brown.400`.

![Rating row default](components/crops/rating-row-default.png)

#### Section title
The first section heading under the hero. Read as `section-h2` on the home page.

**Values (default).** size 548 x 48; background transparent; text GT Walsheim 48/48 900, #1e1818.

![Section title default](components/crops/section-h2-default.png)

#### Feature accordion
A feature accordion row (h-new_features-item w-dropdown): summary bar + expanding body; opened with its own toggle. Read as `feature-accordion` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 548 x 56; radius 10px; background #ffffff `white`; text GT America 20/28 400, #4a3e3e `brown.300`; transition background-color 0.2s ease; icon 17 x 17, #4a3e3e `brown.300` |
| opened | size 548 x 153.72 |

![Feature accordion default](components/crops/feature-accordion-default.png) ![Feature accordion opened](components/crops/feature-accordion-opened.png)

#### Accordion body
The body text region of an opened feature accordion. Read as `feature-accordion-body` on the home page.

**Values (default).** size 548 x 97.72; padding 0px 20px 20px 24px; background transparent; text GT America 18/25.92 400, #736b6b `brown.200`.

![Accordion body default](components/crops/feature-accordion-body-default.png)

#### Testimonial card
A customer testimonial card (land-new_testi-item): quote, avatar, name, role. Read as `testimonial-card` on the home page.

**Values (default).** size 400 x 354.38; padding 60px 50px; radius 20px; background #f5f1ec; shadow #d386de 0px 4px 5px 0px; text GT America 28/33.6 400, #4a3e3e `brown.300`.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Logo marquee item
A company logo cell in the scrolling customer marquee (CSS marquee animation). Read as `marquee-item` on the home page.

**Values (default).** size 128 x 96; background transparent; text GT America 14/20 400, #4a3e3e `brown.300`.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### CTA band
The closing call-to-action band before the footer (h-new_cta: label, headline, demo + trial buttons). Read as `cta-band` on the home page.

**Values (default).** size 1260 x 461.19; padding 64px; radius 40px; background #2d2323 `brown.500`; text GT Walsheim 48/48 900, #ffffff `white`; icon 24 x 24, #dbd9d5 `beige.800`.

![CTA band default](components/crops/cta-band-default.png)

#### Page ground
The body element's painted fill — the page ground. Read as `page-ground` on the home page.

**Values (default).** size 1440 x 5961.27; background #ffffff `white`; text GT America 16/22 400, #4a3e3e `brown.300`; icon 42 x 28, #4a3e3e `brown.300`.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

### Pricing

The pricing page: three plan cards with the job-slot stepper, a feature table, the FAQ accordion and the closing CTA.

#### Pricing title
"Choose the right plan for your team." — the pricing headline. Read as `pricing-title` on the pricing page.

**Values (default).** size 1120 x 180; background transparent; text GT Walsheim 100/90 900, #1f1818 `brown.600`.

![Pricing title default](components/crops/pricing-title-default.png)

#### Plan card
A plan card (new-pricing_plan-card): plan name, description, price, job-slot stepper and feature list. Read as `plan-card` on the pricing page.

**Values (default).** size 652 x 442; padding 48px; border 1px solid #e3e1dd `beige.700`; radius 32px; background #ffffff `white`; text GT Walsheim 48/48 900, #1f1818 `brown.600`.

![Plan card default](components/crops/plan-card-default.png)

#### Job-slot stepper
The plus icon in a plan card's job-slot stepper — a local stepper that changes the quoted price; measured, and the minus side paints .disabled. Read as `plan-stepper-plus` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 26 x 32; background transparent; text GT America 14/20 400, #1f1818 `brown.600`; transition color 0.2s ease; icon 26 x 26, #1f1818 `brown.600` |
| hover, pressed | text GT America 14/20 400, #736b6b `brown.200`; icon 26 x 26, #736b6b `brown.200` |

![Job-slot stepper default](components/crops/plan-stepper-plus-default.png) ![Job-slot stepper hover](components/crops/plan-stepper-plus-hover.png) ![Job-slot stepper pressed](components/crops/plan-stepper-plus-pressed.png)

#### Job-slot minus (disabled)
The minus icon at the stepper's floor — painted with a .disabled class. Read as `plan-stepper-minus` on the pricing page.

**Values (default).** size 26 x 32; background transparent; text GT America 14/20 400, #f5f3ef `beige.500`; transition color 0.2s ease; icon 26 x 26, #f5f3ef `beige.500`.

![Job-slot minus (disabled) default](components/crops/plan-stepper-minus-default.png)

#### Plan CTA
A "Start free trial" button inside a plan card; links to /trial, never followed. Read as `plan-button` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 150 x 52; padding 12px 16px; radius 10px; background #1f1818 `brown.600`; text GT America 20/28 400, #ffffff `white`; transition all 0.2s ease |
| hover | background #382d2d `brown.400` |
| focus-visible | outline 1px auto #101010, offset 1px |
| pressed | background #382d2d `brown.400` |

![Plan CTA default](components/crops/plan-button-default.png) ![Plan CTA hover](components/crops/plan-button-hover.png) ![Plan CTA focus-visible](components/crops/plan-button-focus-visible.png) ![Plan CTA pressed](components/crops/plan-button-pressed.png)

#### Plan feature row
A feature row inside a plan card (icon + text). Read as `plan-feature` on the pricing page.

**Values (default).** size 360 x 56; background transparent; text GT America 18/32 400, #1f1818 `brown.600`.

![Plan feature row default](components/crops/plan-feature-default.png)

#### Comparison table
The plan comparison table lives in .section_compare.is-hide — the public page paints the section hidden, so nothing is measured. Read as `pricing-table` on the pricing page.

**Values (default).** size 0 x 0; background transparent; text Oliver 16/20 400, #a3a2a2 `brown.100`.

Child layers that carry the look: div 0x0 background #2d2323 `brown.500` radius 14px; a 0x0 background rgba(221, 221, 221, 0); a 0x0 background rgba(221, 221, 221, 0).

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Table header cell
A header cell in the comparison table — unreachable while the section is hidden. Read as `pricing-table-head` on the pricing page.

**Values (default).** size 0 x 0; background transparent; text GT Walsheim 24/36 900, #e3e1dd `beige.700`.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Table row
A feature row in the comparison table — unreachable while the section is hidden. Read as `pricing-table-row` on the pricing page.

**Values (default).** size 0 x 0; padding 24px 0px; border B: 1px solid #4a3e3e `brown.300`; background transparent; text GT America 18/20 400, #e3e1dd `beige.700`.

Child layers that carry the look: div 0x0 border 1px solid #4a3e3e `brown.300`; div 0x0 background #0d0d12 radius 8px.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### FAQ item
A pricing FAQ accordion item; opened with its own toggle. Read as `faq-item` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 677.64 x 56; radius 10px; background #ffffff `white`; text GT America 20/28 400, #4a3e3e `brown.300`; transition background-color 0.2s ease; icon 17 x 17, #4a3e3e `brown.300` |
| opened | size 677.64 x 227.53 |

![FAQ item default](components/crops/faq-item-default.png) ![FAQ item opened](components/crops/faq-item-opened.png)

#### FAQ answer
The rich-text body of an opened FAQ item. Read as `faq-answer` on the pricing page.

**Values (default).** size 633.64 x 151.53; background transparent; text GT America 18/25.92 400, #736b6b `brown.200`.

![FAQ answer default](components/crops/faq-answer-default.png)

#### Pricing CTA
The closing trial CTA on the pricing page. Read as `pricing-cta` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 130 x 54; padding 12px 16px; radius 10px; background #ffffff `white`; text GT America 20/30 400, #2d2323 `brown.500` |
| focus-visible | outline 1px auto #101010, offset 1px |

![Pricing CTA default](components/crops/pricing-cta-default.png) ![Pricing CTA hover](components/crops/pricing-cta-hover.png) ![Pricing CTA focus-visible](components/crops/pricing-cta-focus-visible.png) ![Pricing CTA pressed](components/crops/pricing-cta-pressed.png)

### ATS page

The ATS product page: hero, feature tabs, integration cards.

#### ATS title
The /ats product page headline. Read as `ats-title` on the ATS product page.

**Values (default).** size 640 x 192; background transparent; text GT Walsheim 64/64 900, #382d2d `brown.400`.

![ATS title default](components/crops/ats-title-default.png)

#### Feature item
A feature row on the ATS product page (new-ats_feature-item). Read as `ats-feature-item` on the ATS product page.

**Values (default).** size 189 x 54; padding 12px 16px; border 1px solid #edebe7 `beige.600`; radius 10px; background transparent; text GT America 18/25.2 400, #4a3e3e `brown.300`.

![Feature item default](components/crops/ats-feature-item-default.png)

#### ATS feature link
A feature-item link inside the ATS features body; the tab script paints the inactive copies display:none. Read as `ats-tab` on the ATS product page.

**Values (default).** size 0 x 0; padding 12px 16px; border 1px solid #edebe7 `beige.600`; radius 10px; background #4f75fe `blue.500`; text GT America 18/25.2 400, #4a3e3e `brown.300`.

![ATS feature link default](components/crops/ats-tab-default.png)

#### ATS card
A product card on the ATS page (new-ats_card: heading, image, bottom text). Read as `ats-card` on the ATS product page.

**Values (default).** size 1260 x 997.98; padding 48px 64px; radius 40px; background #faf9f7 `beige.400`; text Oliver 22/30.8 400, #4f75fe `blue.500`.

![ATS card default](components/crops/ats-card-default.png)

#### Integration card
An integrations card on the ATS page (new-ats_integrate-card). Read as `ats-integrate-card` on the ATS product page.

**Values (default).** size 356 x 209.19; padding 24px; radius 20px; background #ffffff `white`; shadow #e3e1dd 0px 2px 0px 0px; text GT Walsheim 24/31.92 900, #000000; transition all 0.2s ease.

![Integration card default](components/crops/ats-integrate-card-default.png)

### Careers site (jobs.homerun.co)

Homerun's own employer careers site, a separate client-rendered app on the same palette: header, job list, the cookie banner (hidden, never answered), a job ad and the share/back chrome.

#### Cookie banner
The careers site's consent banner (CookieBanner), measured at rest then hidden for every other reading — never answered. Read as `cookie-banner` on the careers (jobs.homerun.co) page.

**Values (default).** size 775 x 104; padding 30px; radius 5px; background #ffffff `white`; shadow rgba(33, 43, 54, 0.15) 0px 2px 5px 0px; text Inter 16/22 400, #454f5b `named.dim-grey`.

![Cookie banner default](components/crops/cookie-banner-default.png)

#### Careers header
The careers site header block (job-blocks career-site-header): company intro and share links. Read as `careers-header` on the careers (jobs.homerun.co) page.

**Values (default).** size 1440 x 60; background #ffffff `white`; shadow rgba(0, 0, 0, 0.1) 0px 1px 1px 0px; text Inter 14/32 400, rgba(0, 0, 0, 0.7); transition all 0.4s ease; opacity 0.

![Careers header default](components/crops/careers-header-default.png)

#### Careers logo
The company logo link at the top of the careers site. Read as `careers-logo` on the careers (jobs.homerun.co) page.

**Values (default).** size 220 x 40; background transparent; text GTAmerica-Regular 32/140 400, #466af6; transition all 0.18s cubic-bezier(0.55, 0.025, 0.455, 0.98).

![Careers logo default](components/crops/careers-logo-default.png)

#### Share button
A share-this-site social icon button in the careers header; measured never pressed. Read as `careers-share` on the careers (jobs.homerun.co) page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 175 x 40; padding 0px 10px 0px 37px; background transparent; text Inter 15/40 400, #736b6b `brown.200`; transition all 0.18s cubic-bezier(0.55, 0.025, 0.455, 0.98) |

![Share button pressed](components/crops/careers-share-pressed.png)

#### See-all-jobs button
The "See all jobs" button — scrolls to the job list. Read as `careers-all-jobs` on the careers (jobs.homerun.co) page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 179 x 59; border B: 1px solid #466af6; radius 12px; background #466af6; text GTAmerica-Regular 22/34 400, #ffffff `white`; transition all 0.18s cubic-bezier(0.55, 0.025, 0.455, 0.98) |

![See-all-jobs button default](components/crops/careers-all-jobs-default.png) ![See-all-jobs button hover](components/crops/careers-all-jobs-hover.png) ![See-all-jobs button pressed](components/crops/careers-all-jobs-pressed.png)

#### Filter button
A job-list filter pill (Department/Location/Job type) — opens a filter popover. Read as `careers-filter` on the careers (jobs.homerun.co) page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 110 x 36; padding 6px 12px; border 1px solid rgba(0, 0, 0, 0.1); radius 8px; background transparent; text Inter 15/22 400, rgba(0, 0, 0, 0.7); transition all 0.3s ease-out |
| hover, pressed | border 1px solid transparent; background rgba(0, 0, 0, 0.7); text Inter 15/22 400, #ffffff `white` |

![Filter button default](components/crops/careers-filter-default.png) ![Filter button hover](components/crops/careers-filter-hover.png) ![Filter button focus-visible](components/crops/careers-filter-focus-visible.png) ![Filter button pressed](components/crops/careers-filter-pressed.png)

#### Job card
A job listing row (title + location + department); links to the job page, never followed. Read as `careers-job-card` on the careers (jobs.homerun.co) page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 1080 x 54; padding 14px 20px; radius 8px 8px 0px 0px; background #ffffff `white`; text GT-Walsheim-Ultra-Bold 18/26 400, #131313 `brown.700`; transition all 0.18s cubic-bezier(0.55, 0.025, 0.455, 0.98) |
| hover, pressed | background rgba(0, 0, 0, 0.7); text GT-Walsheim-Ultra-Bold 18/26 400, #ffffff `white` |

![Job card default](components/crops/careers-job-card-default.png) ![Job card hover](components/crops/careers-job-card-hover.png) ![Job card focus-visible](components/crops/careers-job-card-focus-visible.png) ![Job card pressed](components/crops/careers-job-card-pressed.png)

#### Carousel control
The next-arrow of the careers photo carousel (local UI control). Read as `careers-carousel` on the careers (jobs.homerun.co) page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 60 x 120; padding 1px 6px; radius 4px; background rgba(0, 0, 0, 0.2); text GTAmerica-Regular 22/34 400, #000000; transition all 0.15s cubic-bezier(0.455, 0.03, 0.515, 0.955) |
| hover | background rgba(0, 0, 0, 0.4) |

![Carousel control default](components/crops/careers-carousel-default.png) ![Carousel control hover](components/crops/careers-carousel-hover.png)

#### Job title
The open-application page heading (jobs.homerun.co/open/en). Read as `job-title` on the job ad page.

**Values (default).** size 160 x 58; background transparent; text Inter 20/58 400, #333333.

![Job title default](components/crops/job-title-default.png)

#### Apply button
The "Apply now" button on a job page; links to the application form, measured never followed. Read as `job-apply` on the job ad page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, focus-visible, pressed) | size 130 x 60; background #466af6; text Inter 18/38 400, #ffffff `white`; transition all 0.18s cubic-bezier(0.55, 0.025, 0.455, 0.98) |

![Apply button default](components/crops/job-apply-default.png) ![Apply button hover](components/crops/job-apply-hover.png) ![Apply button focus-visible](components/crops/job-apply-focus-visible.png) ![Apply button pressed](components/crops/job-apply-pressed.png)

#### Job body
The job description prose block (vacancy-text). Read as `job-prose` on the job ad page.

**Values (default).** size 1440 x 531; padding 0px 0px 60px 0px; background transparent; text GTAmerica-Regular 22/32 400, #ffffff `white`.

Child layers that carry the look: a 147x55 background #466af6 border 1px solid #466af6 radius 4px.

![Job body default](components/crops/job-prose-default.png)

#### Share link
A share-this-job link (X/LinkedIn); measured never followed. Read as `job-share` on the job ad page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 16 x 16; background #736b6b `brown.200`; text Inter 14/20 400, #333333 |
| hover, focus-visible, pressed | background transparent; text Inter 14/20 400, #a3a2a2 `brown.100` |

![Share link default](components/crops/job-share-default.png) ![Share link hover](components/crops/job-share-hover.png) ![Share link focus-visible](components/crops/job-share-focus-visible.png) ![Share link pressed](components/crops/job-share-pressed.png)

#### Back link
The back-to-career-site link at the job page top; measured never followed. Read as `job-back` on the job ad page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 60 x 60; background transparent; text GT-America 14/60 400, #333333; transition background-color 0.2s ease |
| hover, pressed | background #e3e1dd `beige.700` |

![Back link default](components/crops/job-back-default.png) ![Back link hover](components/crops/job-back-hover.png) ![Back link focus-visible](components/crops/job-back-focus-visible.png) ![Back link pressed](components/crops/job-back-pressed.png)

### Application form

The public application wizard a job ad links to: steps strip, fields, file upload and checkbox, Back/Next. Measured at rest; nothing was typed, uploaded or submitted.

#### Form steps
The 4-step indicator (Your details / Questions / Preview / Submit). Read as `apply-steps` on the application form page.

**Values (default).** size 1440 x 40; background transparent; text Inter 18/40 400, #ffffff `white`.

Child layers that carry the look: span 1440x40 background rgba(0, 0, 0, 0.3); i 0x40 background #4f75fe `blue.500`; ul 1440x41 border 1px solid rgba(0, 0, 0, 0.3).

![Form steps default](components/crops/apply-steps-default.png)

#### Text field
A text input in the application form; focused locally, never submitted. Read as `apply-field` on the application form page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 235 x 40; padding 0px 10px; border 1px solid #e8e8e8; radius 2px; background #fafafa; text Inter 17/24.28 400, #333333; transition all 0.2s ease-out; placeholder #333333 |
| focused | border 1px solid #cccccc |

![Text field default](components/crops/apply-field-default.png) ![Text field focused](components/crops/apply-field-focused.png)

#### Email field
The email input in the application form; focused locally, never submitted. Read as `apply-email` on the application form page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 480 x 40; padding 0px 10px; border 1px solid #e8e8e8; radius 2px; background #fafafa; text Inter 17/24.28 400, #333333; transition all 0.2s ease-out; placeholder #333333 |
| focused | border 1px solid #cccccc |

![Email field default](components/crops/apply-email-default.png) ![Email field focused](components/crops/apply-email-focused.png)

#### File dropzone
The resume upload dropzone (.file-drop wraps the hidden native file input); measured at rest, nothing uploaded. Read as `apply-file` on the application form page.

**Values (default).** size 0 x 0; padding 50px; border 1px solid #e8e8e8; radius 3px; background #fafafa; text Inter 17/28 400, #ffffff `white`.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Consent checkbox
A data-consent checkbox row (label.checkbox-container paints the custom box around the hidden input); never ticked. Read as `apply-checkbox` on the application form page.

**Values (default).** size 0 x 0; padding 20px 0px 0px 0px; background transparent; text Inter 18/25.71 400, #333333.

Child layers that carry the look: i 0x0 border 2px solid #e5e5e5 radius 3px.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Next-step button
The "Next: Questions" control — measured never pressed (it advances the wizard; the final Submit is never reached). Read as `apply-next` on the application form page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 538 x 80; radius 0px 0px 5px 5px; background #4f75fe `blue.500`; text Inter 24/80 400, #ffffff `white`; transition all 0.1s cubic-bezier(0.455, 0.03, 0.515, 0.955) |

![Next-step button default](components/crops/apply-next-default.png) ![Next-step button hover](components/crops/apply-next-hover.png)

#### Back link
The back-to-job link in the application bar; measured never followed. Read as `apply-back` on the application form page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 61 x 40; border R: 1px solid rgba(0, 0, 0, 0.1); background transparent; text Inter 0/0 400, #22a9e5; transition all 0.2s ease |
| hover | background rgba(255, 255, 255, 0.15); text Inter 0/0 400, #333333 |
| focus-visible | background rgba(255, 255, 255, 0.15); text Inter 0/0 400, #3277b2 |
| pressed | background rgba(255, 255, 255, 0.15); text Inter 0/0 400, #333333 |

Child layers that carry the look: a 61x40 border 1px solid rgba(0, 0, 0, 0.1); a::after 7pxx7px border 2px solid #ffffff `white`.

![Back link default](components/crops/apply-back-default.png) ![Back link hover](components/crops/apply-back-hover.png) ![Back link focus-visible](components/crops/apply-back-focus-visible.png) ![Back link pressed](components/crops/apply-back-pressed.png)

### ATS sign-in (boundary)

app.homerun.co/login, the Angular sign-in card: SSO buttons, email/password fields, Log in. Measured at rest; nothing was typed or submitted.

#### Sign-in card
The app.homerun.co login card the Angular SPA paints (ATS/HR variant tabs, SSO buttons, email/password). Measured at rest, never submitted. Read as `signin-card` on the ATS sign-in page.

**Values (default).** size 1440 x 900; background transparent; text GT-America 16/22 400, #4f75fe `blue.500`; icon 24 x 24, #4a3e3e `brown.300`.

Child layers that carry the look: div 1440x900 background #f5f3ef `beige.500`; a 231x64 background #ffffff `white` radius 20px 20px 0px 0px; a 231x64 background #edebe7 `beige.600` radius 20px 20px 0px 0px.

![Sign-in card default](components/crops/signin-card-default.png)

#### Product tab
The ATS/HR product tab at the card top (the HR variant links to app.homerun.hr; measured never followed). Read as `signin-tab` on the ATS sign-in page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 231 x 64; radius 20px 20px 0px 0px; background #ffffff `white`; text GT-America 16/22 400, #4a3e3e `brown.300` |

![Product tab default](components/crops/signin-tab-default.png) ![Product tab hover](components/crops/signin-tab-hover.png)

#### SSO button
"Log in with Google" — an SSO button on the card; measured never pressed. Read as `signin-sso` on the ATS sign-in page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 382 x 44; padding 0px 20px; border 1px solid rgba(102, 87, 87, 0.2); radius 10px; background transparent; shadow #e3e1dd 0px 2px 0px 0px; text GT-America 16/22 400, #4a3e3e `brown.300`; icon 24 x 24, #4a3e3e `brown.300` |
| hover | background #f5f3ef `beige.500` |
| focus-visible | outline 5px auto #101010, offset 0px |
| pressed | background #f5f3ef `beige.500` |

![SSO button default](components/crops/signin-sso-default.png) ![SSO button hover](components/crops/signin-sso-hover.png) ![SSO button focus-visible](components/crops/signin-sso-focus-visible.png) ![SSO button pressed](components/crops/signin-sso-pressed.png)

#### Email field
The email input on the sign-in card; focused locally, never submitted. Read as `signin-email` on the ATS sign-in page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focused) | size 382 x 44; padding 0px 15px; radius 10px; background #f5f3ef `beige.500`; text GT-America 16/22 400, #2d2323 `brown.500`; transition border-color 0.3s ease-out, box-shadow 0.3s ease-out; placeholder #2d2323 `brown.500` |

![Email field default](components/crops/signin-email-default.png) ![Email field focused](components/crops/signin-email-focused.png)

#### Password field
The password input; measured at rest, never typed. Read as `signin-password` on the ATS sign-in page.

**Values (default).** size 382 x 44; padding 0px 15px; radius 10px; background #f5f3ef `beige.500`; text GT-America 16/22 400, #2d2323 `brown.500`; transition border-color 0.3s ease-out, box-shadow 0.3s ease-out; placeholder #2d2323 `brown.500`.

![Password field default](components/crops/signin-password-default.png)

#### Log-in button
The "Log in" submit-style button (h-button-secondary); measured never pressed. Read as `signin-button` on the ATS sign-in page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 382 x 44; padding 4px 14px; radius 10px; background #4f75fe `blue.500`; text GT-America 16/22 400, #ffffff `white`; transition background 0.3s ease-out, color 0.3s ease-out |
| hover | background #254cda `blue.600` |
| focus-visible | shadow #ffffff 0px 0px 0px 1px, #c9d5fd 0px 0px 2px 2px |
| pressed | background #254cda `blue.600` |

![Log-in button default](components/crops/signin-button-default.png) ![Log-in button hover](components/crops/signin-button-hover.png) ![Log-in button focus-visible](components/crops/signin-button-focus-visible.png) ![Log-in button pressed](components/crops/signin-button-pressed.png)

#### Account link
"I don't have an account" / "Forgot your password?" — link-styled controls; measured never followed. Read as `signin-link` on the ATS sign-in page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 170 x 22; background transparent; text GT-America 16/22 400, #4f75fe `blue.500`; transition color 0.3s ease-out |
| hover | text GT-America 16/22 400, #254cda `blue.600` |
| focus-visible | shadow #ffffff 0px 0px 0px 1px, #c9d5fd 0px 0px 2px 2px |
| pressed | text GT-America 16/22 400, #254cda `blue.600` |

![Account link default](components/crops/signin-link-default.png) ![Account link hover](components/crops/signin-link-hover.png) ![Account link focus-visible](components/crops/signin-link-focus-visible.png) ![Account link pressed](components/crops/signin-link-pressed.png)

### HR sign-in (boundary)

app.homerun.hr/Account/Logon, the .NET HR sign-in card on the Tailwind UI stack, its button in the HR green. Measured at rest; nothing was typed or submitted.

#### HR sign-in card
The app.homerun.hr logon card (the outermost form container). Measured at rest, never submitted. Read as `hr-card` on the HR sign-in page.

**Values (default).** size 382 x 278; background transparent; text GT-America 16/24 300, #4a3e3e `brown.300`.

Child layers that carry the look: input 382x44 background #f5f3ef `beige.500` radius 10px; input 382x44 background #f5f3ef `beige.500` radius 10px; button 382x44 background #00b16b `secondary.green` radius 10px shadow transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, rgba(0, 0, 0, 0.05) 0px 1px 2px 0px.

![HR sign-in card default](components/crops/hr-card-default.png)

#### HR email field
The email input (public-form__input); focused locally, never submitted. Read as `hr-field` on the HR sign-in page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 382 x 44; padding 2px 12px; radius 10px; background #f5f3ef `beige.500`; text GT-America 16/40 400, #4a3e3e `brown.300`; placeholder #4a3e3e `brown.300` |
| focused | shadow #ffffff 0px 0px 0px 0px, #2563eb 0px 0px 0px 0px; outline 2px solid transparent, offset 2px |

![HR email field default](components/crops/hr-field-default.png) ![HR email field focused](components/crops/hr-field-focused.png)

#### HR password field
The password input; measured at rest, never typed. Read as `hr-password` on the HR sign-in page.

**Values (default).** size 382 x 44; padding 2px 12px; radius 10px; background #f5f3ef `beige.500`; text GT-America 16/40 400, #4a3e3e `brown.300`; placeholder #4a3e3e `brown.300`.

![HR password field default](components/crops/hr-password-default.png)

#### HR log-in button
The "Log in" button (public-form__button); measured never pressed. Read as `hr-button` on the HR sign-in page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 382 x 44; padding 11px 16px; radius 10px; background #00b16b `secondary.green`; shadow rgba(0, 0, 0, 0.05) 0px 1px 2px 0px; text GT-America 16/22 300, #ffffff `white`; transition all 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | background #128053 |
| focus-visible | outline 2px solid #00b16b `secondary.green`, offset 2px |
| pressed | background #128053 |

![HR log-in button default](components/crops/hr-button-default.png) ![HR log-in button hover](components/crops/hr-button-hover.png) ![HR log-in button focus-visible](components/crops/hr-button-focus-visible.png) ![HR log-in button pressed](components/crops/hr-button-pressed.png)

#### HR account link
"I don't have an account" / "Forgot your password?" — measured never followed. Read as `hr-link` on the HR sign-in page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 170 x 24; background transparent; text GT-America 16/24 400, #00b16b `secondary.green` |
| focus-visible | outline 1px auto #101010, offset 1px |

![HR account link default](components/crops/hr-link-default.png) ![HR account link hover](components/crops/hr-link-hover.png) ![HR account link focus-visible](components/crops/hr-link-focus-visible.png) ![HR account link pressed](components/crops/hr-link-pressed.png)

### Mobile (390 wide)

The marketing nav and hero as a phone draws them, at 390 x 844 with an iPhone user agent, and the hamburger's opened menu sheet.

#### Mobile bar
The 390 mobile nav bar: logo + hamburger + trial button. Read as `m-header` on the home page at 390 wide.

**Values (default).** size 390 x 72; background #ffffff `white`; text GT America 16/32 400, #ffffff `white`.

![Mobile bar default](components/crops/m-header-default.png)

#### Menu button
The hamburger (the painted w-nav-button copy); its own press opens the menu sheet. Read as `m-menu-button` on the home page at 390 wide.

**Values (default).** size 39.19 x 40; padding 0px 10px; radius 8px; background rgba(255, 255, 255, 0); image linear-gradient(#ffffff `white`, #ffffff `white`); text GT America 18/20 400, #4e101f `named.maroon`.

![Menu button default](components/crops/m-menu-button-default.png)

#### Mobile menu, open
The opened mobile menu sheet after the hamburger press. Read as `m-menu-open` on the home page at 390 wide.

**Values (default).** size 358 x 451; padding 0px 0px 64px 0px; border 1px solid #edebe7 `beige.600`; radius 20px; background #ffffff `white`; shadow rgba(67, 65, 61, 0.15) 0px 5px 20px 0px; text GT America 16/22 400, #4a3e3e `brown.300`; transition transform 0.4s ease; icon 42 x 28, #4a3e3e `brown.300`.

![Mobile menu, open default](components/crops/m-menu-open-default.png)

#### Menu link
A link row inside the open mobile menu. Read as `m-menu-link` on the home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 324 x 60; padding 16px 12px; radius 10px; background transparent; text GT America 16/22 400, #4a3e3e `brown.300`; transition background-color 0.3s ease; icon 42 x 28, #4a3e3e `brown.300` |
| hover, focus-visible, pressed | background #f5f3ef `beige.500`; icon 42 x 28, #4f75fe `blue.500` |

![Menu link default](components/crops/m-menu-link-default.png) ![Menu link hover](components/crops/m-menu-link-hover.png) ![Menu link focus-visible](components/crops/m-menu-link-focus-visible.png) ![Menu link pressed](components/crops/m-menu-link-pressed.png)

#### Mobile headline
The hero headline at 390. Read as `m-hero` on the home page at 390 wide.

**Values (default).** size 322.19 x 160; background transparent; text GT Walsheim 40/40 900, #382d2d `brown.400`.

![Mobile headline default](components/crops/m-hero-default.png)

### Footer



#### Footer
The footer band: link columns, newsletter form, social icons and legal subfooter. Read as `footer` on the home page.

**Values (default).** size 1340 x 622.17; padding 30px 0px 0px 0px; background transparent; text GT Walsheim 20/20 900, #2d2323 `brown.500`.

Child layers that carry the look: input 217x50 background rgba(45, 35, 35, 0.1) radius 30px 0px 0px 30px; input 96x50 background #2d2323 `brown.500` radius 0px 30px 30px 0px; div 0x0 background #ffdede.

![Footer default](components/crops/footer-default.png)

#### Footer link
A link in a footer link column. Read as `footer-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 41 x 25; background transparent; text GT America 20/24 400, #736b6b `brown.200`; transition all 0.2s ease |
| hover | text GT America 20/24 400, #2d2323 `brown.500` |
| focus-visible | outline 1px auto #101010, offset 1px |
| pressed | text GT America 20/24 400, #2d2323 `brown.500` |

![Footer link default](components/crops/footer-link-default.png) ![Footer link hover](components/crops/footer-link-hover.png) ![Footer link focus-visible](components/crops/footer-link-focus-visible.png) ![Footer link pressed](components/crops/footer-link-pressed.png)

#### Footer heading
A column heading in the footer. Read as `footer-heading` on the home page.

**Values (default).** size 303 x 20; background transparent; text GT Walsheim 20/20 900, #2d2323 `brown.500`.

![Footer heading default](components/crops/footer-heading-default.png)

#### Newsletter field
The footer newsletter email input; focused locally, never submitted. Read as `newsletter-field` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 217 x 50; padding 8px 12px 8px 20px; radius 30px 0px 0px 30px; background rgba(45, 35, 35, 0.1); text GT America 18/25.71 400, #2d2323 `brown.500`; transition all 0.2s ease; placeholder rgba(45, 35, 35, 0.7) |
| focused | background rgba(45, 35, 35, 0.2) |

![Newsletter field default](components/crops/newsletter-field-default.png) ![Newsletter field focused](components/crops/newsletter-field-focused.png)

#### Newsletter button
The newsletter subscribe submit; measured never pressed (a submit control). Read as `newsletter-button` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 96 x 50; padding 9px 20px 9px 15px; radius 0px 30px 30px 0px; background #2d2323 `brown.500`; text GT America 18/20 400, #ffffff `white`; transition background-color 0.2s ease; placeholder #ffffff `white` |

![Newsletter button default](components/crops/newsletter-button-default.png) ![Newsletter button hover](components/crops/newsletter-button-hover.png)

## Icons

25 SVGs were lifted from the pages into [icons/](icons), named by role, with the source table in [icons/INDEX.tsv](icons/INDEX.tsv). Colour is `currentColor` wherever the icon took its colour from the text, so each recolours from CSS `color`. Product screenshots, mockups and the logo-marquee artwork were left out; these are the interface icons. The SVGs are Homerun's property, kept for reference only.

| Icon | Rendered sizes | View box | Style | Seen on | Next to |
|---|---|---|---|---|---|
| [resources](icons/resources.svg) | 12x13 | 0 0 13 13 | fill | home; ats; hr; pricing; customers; features; blog; templates; integrations; about; contact | Resources |
| [manage-your-team](icons/manage-your-team-77cc6ec7.svg) | 43x29 | 0 0 43 29 | fill | home; ats; hr; pricing; customers; features; blog; templates; integrations; about; contact | Manage your team |
| [organise-your-hiring](icons/organise-your-hiring-d2c548f6.svg) | 42x28 | 0 0 42 28 | fill | home; ats; hr; pricing; customers; features; blog; templates; integrations; about; contact | Organise your hiring |
| [try-free-for-15-days](icons/try-free-for-15-days.svg) | 24x25 | 0 0 24 25 | fill | home; ats; pricing; trial | Try free for 15 days / Explore Homerun ATS / Explore Homerun |
| [new](icons/new-10fb26e7.svg) | 17x17 | 0 0 17 17 | fill | home; pricing; about | Get an overview of your hiring process / Save time with auto |
| [icon-bfc7d286](icons/icon-bfc7d286.svg) | 24x24 32x32 | 0 0 32 32 | fill | features; templates; integrations; trial |  |
| [new](icons/new-d3be1709.svg) | 24x24 | 0 0 32 32 | fill | home; pricing; trial |  |
| [new](icons/new-9b2b6c6d.svg) | 24x24 | 0 0 32 32 | fill | home; pricing |  |
| [icon-eb072ccb](icons/icon-eb072ccb.svg) | 32x32 | 0 0 32 32 | fill | features; templates; integrations |  |
| [start-a-15-day-trial](icons/start-a-15-day-trial.svg) | 32x32 | 0 0 33 32 | fill | customers; blog | Start a 15-day trial |
| [details-icon](icons/details-icon.svg) | 16x16 | 0 0 16 16 | fill | customers; blog |  |
| [card-icon](icons/card-icon.svg) | 40x40 | 0 0 41 40 | fill | home |  |
| [open-intercom-messenger](icons/open-intercom-messenger.svg) | 24x24 | 0 0 28 32 | fill | templates; about | Open Intercom Messenger |
| [log-in-with-google](icons/log-in-with-google.svg) | 24x24 | 0 0 28 28 | fill | signin | Log in with Google |
| [next-page](icons/next-page.svg) | 32x32 | 0 0 33 32 | fill | blog | Next Page |
| [manage-your-team](icons/manage-your-team-256843dc.svg) | 43x29 | 0 0 43 29 | fill | home | Manage your team |
| [organise-your-hiring](icons/organise-your-hiring-46f9eadf.svg) | 43x29 | 0 0 43 29 | fill | home | Organise your hiring |
| [new](icons/new-5e9d2115.svg) | 24x24 | 0 0 32 32 | fill | ats |  |
| [new](icons/new-6335a094.svg) | 24x24 | 0 0 32 32 | fill | ats |  |
| [faq-icon](icons/faq-icon-7dc6855f.svg) | 48x49 | 0 0 48 49 | fill | pricing |  |
| [plan-selector-embed](icons/plan-selector-embed-a9fe3363.svg) | 26x26 | 0 0 26 27 | fill | pricing |  |
| [log-in-with-microsoft](icons/log-in-with-microsoft.svg) | 24x24 | 0 0 28 28 | fill | signin | Log in with Microsoft |
| [plan-selector-embed](icons/plan-selector-embed-ceb38656.svg) | 26x26 | 0 0 26 27 | fill | pricing |  |
| [cta-icon](icons/cta-icon.svg) | 40x40 | 0 0 40 40 | fill | pricing |  |
| [faq-icon](icons/faq-icon-e22f943d.svg) | 48x49 | 0 0 48 49 | fill | pricing |  |

## Gaps

### Pages

- **Signed-in pages.** Nothing behind sign-in was captured: the ATS dashboard, pipelines, job editor, candidate profiles and the HR admin. Both sign-in cards were measured at rest and never submitted; no credentials exist in this capture.
- **Anything that converts or sends.** The trial and demo forms were not filled or sent (the /trial page was captured as marketing, not signed up through), the application wizard was never advanced past its first step, no file was uploaded, no newsletter or contact form was submitted.
- **Article and entry pages.** Blog posts, guide entries, update notes, template detail pages and customer stories are linked lists only — the index pages were captured, individual articles were not opened.
- **The careers cookie banner** was hidden for every capture, never answered, so a consent-accepted render is not in this set.

### States

- **Pressed** was forced with DevTools on every control, so a state a script adds on mousedown (if any) is missing.
- **pricing-table, pricing-table-head and pricing-table-row** kept their earlier readings (the feature table was below the lazy-load line on the recapture pass); their entries carry `recaptureMissed` provenance in the JSON.
- **ats-tab** read 0 x 0: the feature tabs render their labels through a script that had not painted them at measure time.
- **apply-file and apply-checkbox** read 0 x 0: the wizard hides its file input and checkbox inputs visually (custom controls paint them).
- **Disabled states** were not seen on any public control.

### Themes

Homerun shows one light theme on every captured surface. The marketing pages paint dark content bands inside that theme (the closing CTA band, `.dark`/`.darkbg` classes on sections) and the careers, ATS and HR surfaces are all light; no dark switch or `prefers-color-scheme` variant was found (`themeChecks` in [raw/css-vars.json](raw/css-vars.json)). The token file therefore ships one `light` set, and the dark bands are captured as `light.surface.dark`, not as a theme.

### Fonts

- **GT America** (UI text, buttons, nav) and **GT Walsheim** (display headlines, weight 900) are Grilli Type faces served from Homerun's CDN; they are commercial fonts, so the style guide falls back to a system sans where they are not installed.
- The careers site paints `GTAmerica-Regular` and the application wizard paints **Inter**; the app sign-in bundle names the same family `GT-America`; the HR card paints the `ui-sans-serif` stack.

### Screenshots

- Customer logos, product mockups and team photos are Homerun's content and appear only inside screenshots and crops.
- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files.

### Content left out

- Job-ad prose, plan pricing copy and article text were not transcribed; only the frames around them were measured.
- No personal data was captured: the pages were read signed out, the sign-in fields stayed empty and the application form was never filled.
