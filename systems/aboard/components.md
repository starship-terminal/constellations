# Aboard components

The discovery list of every page and view captured, then one entry per component with crops of the real site, the icon index and the Gaps. Captured from aboard.com on 2026-11-09, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running page. Nothing was sent or submitted: the newsletter signup was measured at rest and focus only, and the cookie consent was never answered (it was hidden for the clean captures, which is not a consent).

The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) (84 components, 126 states). The page layouts at four widths are in [raw/layout.json](raw/layout.json).

How to read an entry:

- A colour is its value followed by the palette token in [tokens.json](tokens.json) with the same value, when there is one. Text is written family size/line-height weight, then its colour, for example `Tobias 64/68 400, #232a20`, and is read from the first text node inside the component.
- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example "default (same: focus-visible)". When the root paints nothing, "Child layers" names the first nodes inside it that do.
- Crops are images of the component read from the live page, in [components/crops/](components/crops) (125 files, named `{component}-{state}.png`, at 2x). Screenshots are in [screenshots/](screenshots).

## Discovery list

Screenshots are named `{page}-light-{state}.png` (Aboard has one theme). Desktop shots are 1440 x 900 at 1x; `-full` shots are whole pages at 1x; mobile shots are `mobile-{page}-light-{state}.png`, 390 wide.

| Surface | URL | Screenshots |
|---|---|---|
| Home. Display hero, media carousel, feed rows, contact section with the signup iframe, citrus footer. The cookie strip captured as a separate state. | `/` | [contact](screenshots/home-light-contact.png), [cookie-banner](screenshots/home-light-cookie-banner.png), [default](screenshots/home-light-default.png), [full](screenshots/home-light-full.png) |
| How We Work. The process page and its step row. | `/how-we-work/` | [default](screenshots/how-we-work-light-default.png), [full](screenshots/how-we-work-light-full.png) |
| Case studies index. Featured card and the card grid. | `/case-studies/` | [default](screenshots/case-studies-light-default.png), [full](screenshots/case-studies-light-full.png) |
| Case study detail. City of Boston scheduling app. | `/case-studies/city-of-boston-scheduling-app/` | [default](screenshots/case-study-light-default.png), [full](screenshots/case-study-light-full.png) |
| Foundry. The self-built products page. | `/foundry/` | [default](screenshots/foundry-light-default.png), [full](screenshots/foundry-light-full.png) |
| Perspectives index. | `/perspectives/` | [default](screenshots/perspectives-light-default.png), [full](screenshots/perspectives-light-full.png) |
| Newsletter. Latest issue, index rows and the dark signup form. | `/newsletter/` | [default](screenshots/newsletter-light-default.png), [full](screenshots/newsletter-light-full.png) |
| Podcast index. Episode rows on dark green, dock player. | `/podcast/` | [default](screenshots/podcast-light-default.png), [full](screenshots/podcast-light-full.png) |
| Podcast episode detail. | `/podcast/jason-goldman-from-vc-pitches-to-ai-kill-switches/` | [default](screenshots/podcast-episode-light-default.png), [full](screenshots/podcast-episode-light-full.png) |
| Events index. | `/events/` | [default](screenshots/events-light-default.png), [full](screenshots/events-light-full.png) |
| Media index. | `/media/` | [default](screenshots/media-light-default.png), [full](screenshots/media-light-full.png) |
| About. Team and company page. | `/about/` | [default](screenshots/about-light-default.png), [full](screenshots/about-light-full.png) |
| FAQ. Accordion of questions. | `/faq/` | [default](screenshots/faq-light-default.png), [full](screenshots/faq-light-full.png) |
| Careers. Openings list. | `/careers/` | [default](screenshots/careers-light-default.png), [full](screenshots/careers-light-full.png) |
| Security. Posture and practices text. | `/security/` | [default](screenshots/security-light-default.png), [full](screenshots/security-light-full.png) |
| Newsletter article. Meet Aboard Sign, with the share rail. | `/meet-aboard-sign/` | [default](screenshots/aboard-sign-light-default.png), [full](screenshots/aboard-sign-light-full.png) |
| Home at 390: collapsed header, the opened menu, feed rows single-column. | `/` | [default](screenshots/mobile-home-light-default.png), [full](screenshots/mobile-home-light-full.png), [menu-open](screenshots/mobile-home-light-menu-open.png) |
| How We Work at 390. | `/how-we-work/` | [default](screenshots/mobile-how-we-work-light-default.png), [full](screenshots/mobile-how-we-work-light-full.png) |
| Case studies at 390. | `/case-studies/` | [default](screenshots/mobile-case-studies-light-default.png), [full](screenshots/mobile-case-studies-light-full.png) |

### Overlays and transient states

| State | Where | How it was reached | Captured |
|---|---|---|---|
| Cookie consent strip | every page, on load | at rest; hidden by CSS for every clean capture, never answered | [home-light-cookie-banner](screenshots/home-light-cookie-banner.png), [cookie-bar](#cookie-bar) |
| Cookie preferences modal | in the DOM on every page | never opened (Customize was not pressed); the DOM node was measured where visible | [cookie-bar](#cookie-bar) |
| Mobile menu, open | home at 390 | the Open-menu trigger pressed (a local disclosure) | [mobile-home-light-menu-open](screenshots/mobile-home-light-menu-open.png), [m-nav-panel](#m-nav-panel) |
| FAQ answer, open | FAQ | the question heading pressed (a local accordion disclosure) | [faq-panel-open](#faq-panel-open) |
| Podcast dock player | podcast pages | measured at rest; transport controls were never pressed | [pod-seek](#pod-seek), [pod-play](#pod-play) |
| Form focus | newsletter signup | the email field tabbed or clicked into; nothing typed, nothing sent | [nl-field](#nl-field) |
| Contact / signup iframe | home contact section and footer | the same-origin embed was measured as a frame; its fields are the newsletter signup's | [contact-iframe](#contact-iframe) |

## Shared values

Values that apply across entries, from the measurement files.

**Focus.** 10 components were given a real keyboard focus. 9 draw a ring: `nav-logo` (2px solid #271503 `warm-black`, offset 2px), `nav-link` (2px solid #271503 `warm-black`, offset 2px), `nav-cta` (2px solid #271503 `warm-black`, offset 2px), `footer-link` (2px solid #fffefb `off-white`, offset 4px), `footer-social` (2px solid #fffefb `off-white`, offset 4px), `nl-submit` (2px solid #e67940 `orange-peel`, offset 3px), `m-menu-trigger` (2px solid #271503 `warm-black`, offset 2px), `ev-submit` (2px solid #de4c00 `bright-citrus`, offset 4px), `media-show` (2px solid #de4c00 `bright-citrus`, offset 4px). The other 1 draw none, so a keyboard user sees no change: `carousel-tick`.

**Pressed.** Forced `:active` was applied to the buttons and links above; the site changes very little under the finger (the nav CTA and consent buttons keep their fills). See each entry's Pressed row for what did move.

**Motion.** Transitions measured on the components, by duration.

| Duration | Easing | Property | Where |
|---|---|---|---|
| 0.2s | `ease` | color | footer-link, footer-social |
| 0.25s | `ease` | background | nav-link |
| 0.3s | `ease` | background, border-color, box-shadow, color, transform | carousel-pause, ev-field, media-show, nl-field, nl-submit, perspectives-row-title, pod-ep-title |
| 0.35s | `ease` | background | ev-submit |
| 0.4s | `ease` | color | job-row, media-row-title, newsletter-row-title, nl-latest-title |
| 0.5s | `cubic-bezier(0.65, 0, 0.35, 1)` | background, color | m-nav-panel, nav-cta |
| 0.6s | `cubic-bezier(0.32, 0.72, 0, 1)` | transform | feed-row, m-feed-row, perspectives-row |
| 0.7s | `cubic-bezier(0.65, 0, 0.35, 1)` | max-width, transform | m-nav-panel |
| 1s | `cubic-bezier(0.65, 0, 0.35, 1)` | opacity | pod-ep-row |
| 1.2s | `cubic-bezier(0.16, 1, 0.3, 1)` | transform | pod-ep-row |

**Layout grid.** Read on each page at each width ([raw/layout.json](raw/layout.json)).

| Page | 1440 | 1920 | 1024 | 390 |
|---|---|---|---|---|
| home | content x 0, 1440 wide; grid 81.6 81.6 81.6 81.6 81.6 81.6 81.6 81.6 81.6 81.6 81.6 81.6 gap 31.68px | content x 0, 1920 wide; grid 81.3 81.3 81.3 81.3 81.3 81.3 81.3 81.3 81.3 81.3 81.3 81.3 gap 32px | content x 0, 1024 wide; grid 57.8 57.8 57.8 57.8 57.8 57.8 57.8 57.8 57.8 57.8 57.8 57.8 gap 22.528px | content x 0, 390 wide; grid 14.5 14.5 14.5 14.5 14.5 14.5 14.5 14.5 14.5 14.5 14.5 14.5 gap 16px |
| how-we-work | content x 0, 1440 wide; grid 82.9 82.9 82.9 82.9 82.9 82.9 82.9 82.9 82.9 82.9 82.9 82.9 gap 31.68px | content x 0, 1920 wide; grid 82.6 82.6 82.6 82.6 82.6 82.6 82.6 82.6 82.6 82.6 82.6 82.6 gap 32px | content x 0, 1024 wide; grid 58.8 58.8 58.8 58.8 58.8 58.8 58.8 58.8 58.8 58.8 58.8 58.8 gap 22.528px | content x 0, 390 wide; grid 14.5 14.5 14.5 14.5 14.5 14.5 14.5 14.5 14.5 14.5 14.5 14.5 gap 16px |
| case-studies | content x 0, 1440 wide; grid 81.6 81.6 81.6 81.6 81.6 81.6 81.6 81.6 81.6 81.6 81.6 81.6 gap 31.68px | content x 0, 1920 wide; grid 81.3 81.3 81.3 81.3 81.3 81.3 81.3 81.3 81.3 81.3 81.3 81.3 gap 32px | content x 0, 1024 wide; grid 57.8 57.8 57.8 57.8 57.8 57.8 57.8 57.8 57.8 57.8 57.8 57.8 gap 22.528px | content x 0, 390 wide; grid 14.5 14.5 14.5 14.5 14.5 14.5 14.5 14.5 14.5 14.5 14.5 14.5 gap 16px |
| foundry | content x 0, 1440 wide; grid 82.9 82.9 82.9 82.9 82.9 82.9 82.9 82.9 82.9 82.9 82.9 82.9 gap 31.68px | content x 0, 1920 wide; grid 82.6 82.6 82.6 82.6 82.6 82.6 82.6 82.6 82.6 82.6 82.6 82.6 gap 32px | content x 0, 1024 wide; grid 58.8 58.8 58.8 58.8 58.8 58.8 58.8 58.8 58.8 58.8 58.8 58.8 gap 22.528px | content x 0, 390 wide; grid 14.5 14.5 14.5 14.5 14.5 14.5 14.5 14.5 14.5 14.5 14.5 14.5 gap 16px |
| newsletter | content x 0, 1440 wide; grid 82.9 82.9 82.9 82.9 82.9 82.9 82.9 82.9 82.9 82.9 82.9 82.9 gap 31.68px | content x 0, 1920 wide; grid 82.6 82.6 82.6 82.6 82.6 82.6 82.6 82.6 82.6 82.6 82.6 82.6 gap 32px | content x 0, 1024 wide; grid 58.8 58.8 58.8 58.8 58.8 58.8 58.8 58.8 58.8 58.8 58.8 58.8 gap 22.528px | content x 0, 390 wide; grid 14.5 14.5 14.5 14.5 14.5 14.5 14.5 14.5 14.5 14.5 14.5 14.5 gap 16px |
| podcast | content x 0, 1440 wide; grid 82.9 82.9 82.9 82.9 82.9 82.9 82.9 82.9 82.9 82.9 82.9 82.9 gap 31.68px | content x 0, 1920 wide; grid 82.6 82.6 82.6 82.6 82.6 82.6 82.6 82.6 82.6 82.6 82.6 82.6 gap 32px | content x 0, 1024 wide; grid 58.8 58.8 58.8 58.8 58.8 58.8 58.8 58.8 58.8 58.8 58.8 58.8 gap 22.528px | content x 0, 390 wide; grid 14.5 14.5 14.5 14.5 14.5 14.5 14.5 14.5 14.5 14.5 14.5 14.5 gap 16px |
| about | content x 0, 1440 wide; grid 82.9 82.9 82.9 82.9 82.9 82.9 82.9 82.9 82.9 82.9 82.9 82.9 gap 31.68px | content x 0, 1920 wide; grid 82.6 82.6 82.6 82.6 82.6 82.6 82.6 82.6 82.6 82.6 82.6 82.6 gap 32px | content x 0, 1024 wide; grid 58.8 58.8 58.8 58.8 58.8 58.8 58.8 58.8 58.8 58.8 58.8 58.8 gap 22.528px | content x 0, 390 wide; grid 14.5 14.5 14.5 14.5 14.5 14.5 14.5 14.5 14.5 14.5 14.5 14.5 gap 16px |
| faq | content x 0, 1440 wide; grid 82.9 82.9 82.9 82.9 82.9 82.9 82.9 82.9 82.9 82.9 82.9 82.9 gap 31.68px | content x 0, 1920 wide; grid 82.6 82.6 82.6 82.6 82.6 82.6 82.6 82.6 82.6 82.6 82.6 82.6 gap 32px | content x 0, 1024 wide; grid 58.8 58.8 58.8 58.8 58.8 58.8 58.8 58.8 58.8 58.8 58.8 58.8 gap 22.528px | content x 0, 390 wide; grid 14.5 14.5 14.5 14.5 14.5 14.5 14.5 14.5 14.5 14.5 14.5 14.5 gap 16px |

**Card shapes.** Default-state values; the entries hold the states.

| Card | Size | Border | Radius | Background | Shadow | Padding |
|---|---|---|---|---|---|---|
| [Featured case card](#featured-case-card) | 1328 x 703.02 | - | 12px | rgba(128, 128, 128, 0.12) | transparent 0px 40px 80px -48px | 30px 0px 0px 0px |
| [Case card](#case-card) | 632.31 x 599.17 | - | 12px | rgba(128, 128, 128, 0.12) | transparent 0px 40px 80px -48px | 30px 0px 0px 0px |
| [Foundry product card](#foundry-product-card) | 1440 x 6600.69 | - | 999px | #06070a `ink` | none | 0 |
| [Newsletter card](#newsletter-card) | 426.88 x 422.58 | - | 12px | #f5f4f1 `thumb-cool` | none | 0 |
| [Newsletter form](#newsletter-form) | 541.52 x 84.19 | 1px solid rgba(233, 222, 205, 0.28) `field-border` | 999px | rgba(251, 242, 234, 0.08) | none | 0 |
| [Newsletter card form](#newsletter-card-form) | 560 x 81.94 | 1px solid rgba(6, 7, 10, 0.1) `line` | 999px | #fffefb `off-white` | none | 0 |
| [Newsletter email field](#newsletter-email-field) | 379.33 x 50 | 1px solid rgba(233, 222, 205, 0.28) `field-border` | 999px | rgba(251, 242, 234, 0.08) | none | 0px 20px |
| [Feed row](#feed-row) | 1328 x 242.39 | - | 12px | #efe7db `thumb-warm` | none | 24px 0px |
| [Episode row](#episode-row) | 1344 x 197 | - | 10px | #0b2050 `pod-navy` | none | 26px 0px |

## Components

### Shell and navigation

The shell every page shares: a 78px fixed header with the Aboard wordmark, the section links (How We Work / Case Studies / Foundry / Perspectives / About) and the boxed "Get in Touch" CTA; and the bright-citrus footer with the "We Can Help" serif display heading, the newsletter-signup iframe, link columns and the legal row.

#### Top navigation bar
The fixed 78px header: the Aboard wordmark, the section links (How We Work / Case Studies / Foundry / Perspectives / About) and the boxed "Get in Touch" CTA. Read as `nav-bar` on the home page.

**Values (default).** size 1440 x 78; padding 18px 56px 0px 56px; background transparent; text Work Sans 15.04/24.06 400, #271503 `warm-black`; icon 107.05 x 26, #271503 `warm-black`.

Child layers that carry the look: nav::before 1328pxx60px background rgba(240, 241, 239, 0.84) radius 999px; a::after 9pxx9px background #271503 `warm-black`; ul 210x223.7 background rgba(250, 245, 239, 0.97) radius 14px shadow rgba(39, 21, 3, 0.18) 0px 14px 34px -22px.

![Top navigation bar default](components/crops/nav-bar-default.png)

#### Logo
The Aboard wordmark linking home. Read as `nav-logo` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 107.05 x 26; background transparent; text Work Sans 16/25.6 400, #271503 `warm-black`; icon 107.05 x 26, #271503 `warm-black` |
| focus-visible | radius 2px; outline 2px solid #271503 `warm-black`, offset 2px |

![Logo default](components/crops/nav-logo-default.png) ![Logo hover](components/crops/nav-logo-hover.png) ![Logo focus-visible](components/crops/nav-logo-focus-visible.png) ![Logo pressed](components/crops/nav-logo-pressed.png)

#### Nav link
A section link in the top bar. Read as `nav-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 129.73 x 42.06; padding 9px 14px; radius 999px; background transparent; text Work Sans 15.04/24.06 400, #271503 `warm-black`; transition background 0.25s ease |
| hover | background rgba(128, 128, 128, 0.16) |
| focus-visible | background rgba(128, 128, 128, 0.16); outline 2px solid #271503 `warm-black`, offset 2px |
| pressed | background rgba(128, 128, 128, 0.16) |

![Nav link default](components/crops/nav-link-default.png) ![Nav link hover](components/crops/nav-link-hover.png) ![Nav link focus-visible](components/crops/nav-link-focus-visible.png) ![Nav link pressed](components/crops/nav-link-pressed.png)

#### Get-in-touch CTA
The boxed "Get in Touch" button at the right of the nav; jumps to the contact section. Hovered and focused only. Read as `nav-cta` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 157.31 x 42; padding 5px 5px 5px 18px; radius 999px; background #de4c00 `bright-citrus`; text Work Sans 14.72/23.55 400, #fffefb `off-white`; transition background 0.5s cubic-bezier(0.65, 0, 0.35, 1), color 0.5s cubic-bezier(0.65, 0, 0.35, 1); icon 13 x 13, #fffefb `off-white` |
| hover | background #291503 `cta-hover` |
| focus-visible | outline 2px solid #271503 `warm-black`, offset 2px |
| pressed | background #2f1703 |

![Get-in-touch CTA default](components/crops/nav-cta-default.png) ![Get-in-touch CTA hover](components/crops/nav-cta-hover.png) ![Get-in-touch CTA focus-visible](components/crops/nav-cta-focus-visible.png) ![Get-in-touch CTA pressed](components/crops/nav-cta-pressed.png)

#### Skip link
The fixed "Skip to content" link, offscreen until focused. Read as `skip-link` on the home page.

**Values (default).** size 153.3 x 45.59; padding 10px 16px; background #271503 `warm-black`; text Work Sans 16/25.6 400, #ffffff `white`.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Footer
The bright-citrus footer: "We Can Help" display heading, the newsletter-signup iframe, link columns, the legal row and the social links. Read as `footer` on the home page.

**Values (default).** size 1440 x 1237.78; background #de4c00 `bright-citrus`; text Tobias 32/35.2 300, #fffefb `off-white`.

![Footer default](components/crops/footer-default.png)

#### Footer heading
"We Can Help" — the serif display heading of the citrus footer. Read as `footer-heading` on the home page.

**Values (default).** size 178.25 x 35.19; background transparent; text Tobias 32/35.2 300, #fffefb `off-white`.

![Footer heading default](components/crops/footer-heading-default.png)

#### Footer link
Read as `footer-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 101.47 x 18; background transparent; text Work Sans 15/24 400, #fffefb `off-white`; transition color 0.2s ease |
| hover | text Work Sans 15/24 400, #f3d9c8 `footer-hover` |
| focus-visible | radius 2px; outline 2px solid #fffefb `off-white`, offset 4px |
| pressed | text Work Sans 15/24 400, #f3d9c8 `footer-hover` |

![Footer link default](components/crops/footer-link-default.png) ![Footer link hover](components/crops/footer-link-hover.png) ![Footer link focus-visible](components/crops/footer-link-focus-visible.png) ![Footer link pressed](components/crops/footer-link-pressed.png)

#### Social link
A social link in the footer column (LinkedIn New York / Lebanon, YouTube, Instagram, Facebook, X). Read as `footer-social` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 149.5 x 18; background transparent; text Work Sans 15/24 400, #fffefb `off-white`; transition color 0.2s ease |
| hover | text Work Sans 15/24 400, #f3d9c8 `footer-hover` |
| focus-visible | radius 2px; outline 2px solid #fffefb `off-white`, offset 4px |
| pressed | text Work Sans 15/24 400, #f3d9c8 `footer-hover` |

![Social link default](components/crops/footer-social-default.png) ![Social link hover](components/crops/footer-social-hover.png) ![Social link focus-visible](components/crops/footer-social-focus-visible.png) ![Social link pressed](components/crops/footer-social-pressed.png)

### Home

The home page: the "Your partner for the big AI leap" display hero (words animate in one by one), the "Your roadmap, realized" section, a media carousel with tick pagination and a pause control, and the feed rows linking events, the newsletter and the podcast.

#### Hero title
"Your partner for the big AI leap" — the display headline, per-word animated (rd-words). Read as `hero-title` on the home page.

**Values (default).** size 933.11 x 155.53; background transparent; text Tobias 77.76/77.76 400, #271503 `warm-black`.

![Hero title default](components/crops/hero-title-default.png)

#### Eyebrow label
A small caps section label ("WHAT WE DO", "PERSPECTIVES"). Read as `eyebrow` on the home page.

**Values (default).** size 435.19 x 20.47; background transparent; text Work Sans 12.8/20.48 600, #766757 `warm-grey`.

![Eyebrow label default](components/crops/eyebrow-default.png)

#### Section title
A section heading ("Your roadmap, realized", "We've got opinions"). Read as `section-title` on the home page.

**Values (default).** size 421.55 x 229.08; background transparent; text Tobias 74.88/76.37 400, #271503 `warm-black`.

![Section title default](components/crops/section-title-default.png)

#### Feed row
A content row in the home feed: kind tag, title and date in a three-column grid (EVENT / NEWSLETTER / PODCAST). Read as `feed-row` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 1328 x 242.39; padding 24px 0px; background transparent; text Work Sans 11.52/18.43 600, #271503 `warm-black`; transition transform 0.6s cubic-bezier(0.32, 0.72, 0, 1); icon 13 x 13, #de4c00 `bright-citrus` |
| hover | transform translate(7.95329px, 0px) |

Child layers that carry the look: span 259.2x194.4 background #efe7db `thumb-warm` radius 12px.

![Feed row default](components/crops/feed-row-default.png) ![Feed row hover](components/crops/feed-row-hover.png)

#### Feed row kind tag
The small caps kind label on a feed row. Read as `feed-row-tag` on the home page.

**Values (default).** size 525.48 x 18.42; background transparent; text Work Sans 11.52/18.43 600, #271503 `warm-black`; icon 13 x 13, #de4c00 `bright-citrus`.

![Feed row kind tag default](components/crops/feed-row-tag-default.png)

#### Carousel tick
A pagination tick of the home media carousel (cc-*); is-on marks the current one. Read as `carousel-tick` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, focus-visible, pressed) | size 35 x 20; padding 9px 0px; background transparent; text Work Sans 16/25.6 400, #fffefb `off-white` |

Child layers that carry the look: i 35x2 background rgba(255, 254, 251, 0.3) `line-inverse` radius 2px; i::after 35pxx2px background #fffefb `off-white`.

![Carousel tick default](components/crops/carousel-tick-default.png) ![Carousel tick hover](components/crops/carousel-tick-hover.png) ![Carousel tick focus-visible](components/crops/carousel-tick-focus-visible.png) ![Carousel tick pressed](components/crops/carousel-tick-pressed.png)

#### Carousel pause
The carousel's pause control. Read as `carousel-pause` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 28 x 28; background transparent; text Work Sans 16/25.6 400, rgba(255, 254, 251, 0.85); transition color 0.3s ease; icon 14 x 14, rgba(255, 254, 251, 0.85) |
| hover | text Work Sans 16/25.6 400, #ffffff `white`; icon 14 x 14, #ffffff `white` |

![Carousel pause default](components/crops/carousel-pause-default.png) ![Carousel pause hover](components/crops/carousel-pause-hover.png)

#### Contact iframe
The embedded form frame in the contact section (same-origin newsletter signup). Measured as a frame; the fields inside live under Newsletter signup. Read as `contact-iframe` on the home page.

**Values (default).** size 1120 x 375; background transparent; text Work Sans 16/25.6 400, #fffefb `off-white`.

![Contact iframe default](components/crops/contact-iframe-default.png)

### Consent overlay

Aboard's cookie consent is CookieYes: a bottom strip with "We use cookies..." copy and Customize / Accept All buttons, plus a preferences modal that lives in the DOM. Captured as found; nothing was pressed (the capture hides the strip by CSS for the clean shots, which is a hide, not a consent).

#### Cookie consent strip
The CookieYes strip pinned at the bottom: "We use cookies..." copy with Customize and Accept All. Re-shown for the measurement, never answered. Read as `cookie-bar` on the home page.

Not on the page when it was captured.

#### Accept-all button
The "Accept All" button of the consent strip. Measured in every state — never pressed (it would post consent). Read as `cookie-accept` on the home page.

Not on the page when it was captured.

#### Customize button
The "Customize" button, which opens the preferences modal. Measured, never pressed. Read as `cookie-customize` on the home page.

Not on the page when it was captured.

#### Consent close button
The small close control of the consent strip. Measured, never pressed. Read as `cookie-close` on the home page.

Not on the page when it was captured.

### How We Work

The process page: the "95% of AI software initiatives fail" headline, the principle cards and the Landscape / Audit / Blueprint / Architecture / Migrate step row.

#### Page title
"95% of AI software initiatives fail. Why do ours ship?" — the interior display headline. Read as `hww-title` on the How We Work page.

**Values (default).** size 1000.08 x 372.56; background transparent; text Tobias 95.04/93.13 400, #06070a `ink`.

Child layers that carry the look: i 482.6x6.6 background #de4c00 `bright-citrus` radius 3.8016px.

![Page title default](components/crops/hww-title-default.png)

#### Principle card heading
A principle card heading ("We evolved the process"). Read as `hww-card` on the How We Work page.

**Values (default).** size 656.16 x 34.77; background transparent; text Tobias 30.24/34.77 400, #06070a `ink`.

![Principle card heading default](components/crops/hww-card-default.png)

#### Process step
A step of the Landscape → Audit → Blueprint → Architecture → Migrate process row. Read as `hww-step` on the How We Work page.

**Values (default).** size 541.52 x 51.2; background transparent; text Tobias 51.2/51.2 400, #06070a `ink`.

![Process step default](components/crops/hww-step-default.png)

#### Body text
Read as `hww-body` on the How We Work page.

**Values (default).** size 312.25 x 77.77; background transparent; text Work Sans 17.28/25.92 400, #3d3a36 `body`.

![Body text default](components/crops/hww-body-default.png)

### Case studies

The work index and one detail page (City of Boston scheduling app): a full-width featured card, then a grid of case cards with industry tags.

#### Page title
Read as `cases-title` on the case studies page.

**Values (default).** size 988.08 x 232.81; background transparent; text Tobias 123.84/116.41 400, #271503 `warm-black`.

![Page title default](components/crops/cases-title-default.png)

#### Featured case card
The lead case-study card (the full-width SageSure feature). Read as `case-card-feature` on the case studies page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 1328 x 703.02; padding 30px 0px 0px 0px; border T: 1px solid rgba(39, 21, 3, 0.114); background transparent; text Work Sans 11.52/12.67 400, #766757 `warm-grey` |
| hover | border T: 1px solid rgba(39, 21, 3, 0.1) `line-warm` |

![Featured case card default](components/crops/case-card-feature-default.png) ![Featured case card hover](components/crops/case-card-feature-hover.png)

#### Case card
A case-study card in the grid: industry tag, title, client. Read as `case-card` on the case studies page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 632.31 x 599.17; padding 30px 0px 0px 0px; border T: 1px solid rgba(39, 21, 3, 0.1) `line-warm`; background transparent; text Work Sans 11.52/12.67 400, #766757 `warm-grey`; icon 11.23 x 11.23, #2a2a33 |
| hover | icon 12.15 x 12.15, #2a2a33 |

![Case card default](components/crops/case-card-default.png) ![Case card hover](components/crops/case-card-hover.png)

#### Case industry tag
The small caps industry label on a case card. Read as `case-tag` on the case studies page.

**Values (default).** size 87.13 x 12.66; background transparent; text Work Sans 11.52/12.67 400, #766757 `warm-grey`.

![Case industry tag default](components/crops/case-tag-default.png)

#### Case study title
"City of Boston" detail page title. Read as `cs-title` on the case study page.

**Values (default).** size 988.09 x 120.44; background transparent; text Tobias 59.04/60.22 400, #271503 `warm-black`.

![Case study title default](components/crops/cs-title-default.png)

#### Case study body
Read as `cs-body` on the case study page.

**Values (default).** size 691.19 x 96.8; background transparent; text Work Sans 23.04/32.25 400, #271503 `warm-black`.

![Case study body default](components/crops/cs-body-default.png)

#### Case study meta
The detail page's fact labels (client, sector, platform). Read as `cs-meta` on the case study page.

**Values (default).** size 308.23 x 18.55; background transparent; text Work Sans 12.8/18.56 500, #766757 `warm-grey`.

![Case study meta default](components/crops/cs-meta-default.png)

### Foundry

The Foundry page: the products Aboard builds for itself (Aboard Sign, TinyLittleOffice) as cards in the same shell.

#### Page title
"Software we build for ourselves" — the Foundry page title. Read as `foundry-title` on the Foundry page.

**Values (default).** size 574.41 x 84.67; background transparent; text Tobias 86.4/84.67 400, #06070a `ink`.

![Page title default](components/crops/foundry-title-default.png)

#### Foundry product card
A Foundry product card (Aboard Sign, TinyLittleOffice). Read as `foundry-card` on the Foundry page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 1440 x 6600.69; background transparent; text Tobias 69.12/67.73 400, #06070a `ink`; icon 14 x 14, #ffffff `white` |

Child layers that carry the look: section 1440x1530.2 background #ffffff `white` border 1px solid rgba(6, 7, 10, 0.1) `line`; a 224.6x46.6 background #06070a `ink` radius 999px; ul 770.8x53.6 border 1px solid rgba(6, 7, 10, 0.1) `line`.

![Foundry product card default](components/crops/foundry-card-default.png) ![Foundry product card hover](components/crops/foundry-card-hover.png)

### Feeds: perspectives, newsletter, events, media

The content indexes share one row vocabulary: a kind tag or date, a serif title and a thumbnail. The newsletter page adds the dark signup form and the latest-issue card.

#### Page title
Read as `perspectives-title` on the Perspectives page.

**Values (default).** size 541.52 x 73.44; background transparent; text Tobias 72/73.44 400, #06070a `ink`.

![Page title default](components/crops/perspectives-title-default.png)

#### Index row
A content row/card on the index (date, title, thumbnail). Read as `perspectives-row` on the Perspectives page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 1344 x 242.39; padding 24px 0px; background transparent; text Work Sans 11.52/17.28 600, #06070a `ink`; transition transform 0.6s cubic-bezier(0.32, 0.72, 0, 1); icon 13 x 13, #de4c00 `bright-citrus` |
| hover | transform translate(7.9388px, 0px) |

Child layers that carry the look: span 259.2x194.4 background #efe7db `thumb-warm` radius 12px.

![Index row default](components/crops/perspectives-row-default.png) ![Index row hover](components/crops/perspectives-row-hover.png)

#### Row title
Read as `perspectives-row-title` on the Perspectives page.

**Values (default).** size 534.05 x 32.25; background transparent; text Tobias 28.8/32.25 400, #06070a `ink`; transition color 0.3s ease.

![Row title default](components/crops/perspectives-row-title-default.png)

#### Page title
Read as `newsletter-title` on the newsletter page.

**Values (default).** size 656.16 x 146.88; background transparent; text Tobias 72/73.44 400, #fbf3ec `cream`.

![Page title default](components/crops/newsletter-title-default.png)

#### Index row
A content row/card on the index (date, title, thumbnail). Read as `newsletter-row` on the newsletter page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 1344 x 267.52; padding 28px 0px; background transparent; text Work Sans 11.84/17.76 600, #6f6a63 `muted` |

Child layers that carry the look: span 317.3x211.5 background #f5f4f1 `thumb-cool` radius 10px.

![Index row default](components/crops/newsletter-row-default.png) ![Index row hover](components/crops/newsletter-row-hover.png)

#### Row title
Read as `newsletter-row-title` on the newsletter page.

**Values (default).** size 740.31 x 34.84; background transparent; text Tobias 31.68/34.84 300, #06070a `ink`; transition color 0.4s ease.

![Row title default](components/crops/newsletter-row-title-default.png)

#### Page title
Read as `events-title` on the events page.

**Values (default).** size 1000.08 x 73.44; background transparent; text Tobias 72/73.44 400, #06070a `ink`.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Index row
A content row/card on the index (date, title, thumbnail). Read as `events-row` on the events page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 1114.72 x 383.22; padding 36px 0px; border B: 1px solid rgba(6, 7, 10, 0.1) `line`; background transparent; text Work Sans 10.88/16.32 600, #06070a `ink`; icon 12 x 12, #de4c00 `bright-citrus` |

Child layers that carry the look: li 1114.7x383.2 border 1px solid rgba(6, 7, 10, 0.1) `line`; a 240x240 background #f5f4f1 `thumb-cool` radius 12px; span 118.9x24.3 background #fbf3ec `cream` radius 999px shadow rgba(39, 21, 3, 0.08) 0px 0px 0px 1px inset.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Row title
Read as `events-row-title` on the events page.

**Values (default).** size 543.22 x 39.67; background transparent; text Tobias 37.44/39.68 400, #06070a `ink`.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Page title
Read as `media-title` on the media page.

**Values (default).** size 1000.08 x 73.44; background transparent; text Tobias 72/73.44 400, #06070a `ink`.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Index row
A content row/card on the index (date, title, thumbnail). Read as `media-row` on the media page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 885.45 x 500.53; background transparent; text Work Sans 11.2/16.8 600, #06070a `ink`; icon 13 x 13, #fffefb `off-white` |

Child layers that carry the look: span 93x24.8 background #fbf3ec `cream` radius 9999px shadow transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, rgba(39, 21, 3, 0.08) 0px 0px 0px 1px inset; span 218.3x46 background #06070a `ink` radius 999px; span 36x36 background rgba(255, 255, 255, 0.16) radius 50%.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Row title
Read as `media-row-title` on the media page.

**Values (default).** size 459.42 x 143.72; background transparent; text Tobias 46.08/47.92 400, #06070a `ink`; transition color 0.4s ease.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Event kind tag
The "OFFICE HOURS" caps tag on an event card. Read as `ev-tag` on the events page.

**Values (default).** size 118.91 x 24.31; padding 4px 10px; radius 999px; background #fbf3ec `cream`; shadow rgba(39, 21, 3, 0.08) 0px 0px 0px 1px inset; text Work Sans 10.88/16.32 600, #06070a `ink`.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Media show-more button
A "show" toggle on a media row. Measured, not pressed. Read as `media-show` on the media page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 127.22 x 39.05; padding 12px 22px; radius 999px; background transparent; shadow rgba(39, 21, 3, 0.3) 0px 0px 0px 1px inset; text Work Sans 15.04/15.04 500, #06070a `ink`; transition background 0.3s ease |
| hover | background #fbf3ec `cream` |
| focus-visible | outline 2px solid #de4c00 `bright-citrus`, offset 4px |
| pressed | background #fbf3ec `cream` |

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

### Podcast

The podcast index (cream type on dark forest green) and one episode page: episode rows and the dock player's seek bar. Transport buttons were measured at rest, never pressed.

#### Podcast title
The latest-episode headline in cream on the dark podcast section. Read as `pod-title` on the podcast page.

**Values (default).** size 770.8 x 76.44; background transparent; text Tobias 72/73.44 400, #fbf3ec `cream`.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Episode title
An episode row title ("Allison Fine: Making AI-Driven Change Less Scary"). Read as `pod-ep-title` on the podcast page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 1084.91 x 32.25; background transparent; text Tobias 28.8/32.25 300, #fbf3ec `cream`; transition color 0.3s ease |

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Episode row
An episode row in the index. Read as `pod-ep-row` on the podcast page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 1344 x 197; padding 26px 0px; border B: 1px solid rgba(233, 222, 205, 0.16); background transparent; text Tobias 28.8/32.25 300, #fbf3ec `cream`; transition opacity 1s cubic-bezier(0.65, 0, 0.35, 1), transform 1.2s cubic-bezier(0.16, 1, 0.3, 1); icon 15 x 15, #fbf3ec `cream` |
| hover | text Tobias 28.8/32.25 300, #e67940 `orange-peel` |

Child layers that carry the look: li 1344x197 border 1px solid rgba(233, 222, 205, 0.16); button 144x144 background #0b2050 `pod-navy` radius 10px; button 46x46 border 1px solid rgba(233, 222, 205, 0.16) radius 50%.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Player seek bar
The range input of the podcast dock player. Measured at rest, never dragged. Read as `pod-seek` on the podcast page.

Not on the page when it was captured.

#### Player button
A player transport button. Measured, never pressed (it would play). Read as `pod-play` on the podcast page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 340 x 340; radius 10px; background #0b2050 `pod-navy`; text Work Sans 16/24 400, #eadfcf |

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Episode page title
Read as `pe-title` on the podcast episode page.

**Values (default).** size 656.16 x 220.31; background transparent; text Tobias 72/73.44 400, #fbf3ec `cream`.

![Episode page title default](components/crops/pe-title-default.png)

#### Episode body
Read as `pe-body` on the podcast episode page.

**Values (default).** size 217.05 x 36; background transparent; text Tobias 24/36 400, #fbf3ec `cream`.

![Episode body default](components/crops/pe-body-default.png)

### Article page

A long-form piece ("Meet Aboard Sign") in the centred article column with the SHARE rail and newsletter cards; a boxed variant of the signup form closes the page.

#### Article title
"Meet Aboard Sign…" — a long-form piece in the article layout. Read as `art-title` on the newsletter article page.

**Values (default).** size 1000.08 x 77.77; background transparent; text Tobias 77.76/77.76 400, #fbf3ec `cream`.

![Article title default](components/crops/art-title-default.png)

#### Article body
A paragraph in the article column (rd-article, centred at columns 4-11). Read as `art-body` on the newsletter article page.

**Values (default).** size 312.25 x 52.78; background transparent; text Work Sans 17.6/26.4 400, rgba(233, 222, 205, 0.82).

![Article body default](components/crops/art-body-default.png)

#### Share rail
The SHARE rail beside the article (copy-link, never pressed). Read as `art-share` on the newsletter article page.

**Values (default).** size 197.59 x 229.77; background transparent; text Work Sans 11.84/17.76 600, #6f6a63 `muted`; icon 18 x 18, #06070a `ink`.

Child layers that carry the look: button 42x42 border 1px solid rgba(6, 7, 10, 0.1) `line` radius 50%; span 62.2x28.7 background #06070a `ink` radius 999px; a 42x42 border 1px solid rgba(6, 7, 10, 0.1) `line` radius 50%.

![Share rail default](components/crops/art-share-default.png)

#### Newsletter card
A "More from the newsletter" card (date, title, thumbnail). Read as `art-nl-card` on the newsletter article page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 426.88 x 422.58; background transparent; text Work Sans 11.84/17.76 600, #6f6a63 `muted` |

Child layers that carry the look: span 426.9x284.6 background #f5f4f1 `thumb-cool` radius 12px.

![Newsletter card default](components/crops/art-nl-card-default.png) ![Newsletter card hover](components/crops/art-nl-card-hover.png)

### Newsletter signup (resting only)

The one real form on the site, rendered twice: inline on the newsletter page (dark variant) and boxed under articles (is-card variant), plus embedded in the footer through a same-origin iframe. It posts to /wp-json/aboard/v1/newsletter-signups. Fields were measured at rest and focused only: no address was typed and the form was never submitted.

#### Newsletter form
The "Email address + Subscribe" signup (dark variant on the newsletter page). Posts to /wp-json/aboard/v1/newsletter-signups — measured at rest, never submitted. Read as `nl-form` on the newsletter page.

**Values (default).** size 541.52 x 84.19; background transparent; text Work Sans 15.04/15.04 500, #fffefb `off-white`; icon 14 x 14, #fffefb `off-white`.

Child layers that carry the look: input 379.3x50 background rgba(251, 242, 234, 0.08) border 1px solid rgba(233, 222, 205, 0.28) `field-border` radius 999px; button 152.2x50 background #de4c00 `bright-citrus` radius 999px; span 40x40 background rgba(255, 255, 255, 0.16) radius 50%.

![Newsletter form default](components/crops/nl-form-default.png)

#### Newsletter email field
The email input. Clicked into for the focus style; nothing typed. Read as `nl-field` on the newsletter page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 379.33 x 50; padding 0px 20px; border 1px solid rgba(233, 222, 205, 0.28) `field-border`; radius 999px; background rgba(251, 242, 234, 0.08); text Work Sans 16/16 400, #fbf3ec `cream`; transition border-color 0.3s ease, box-shadow 0.3s ease; placeholder rgba(233, 222, 205, 0.6) |
| focused | border 1px solid #e67940 `orange-peel`; shadow rgba(230, 121, 64, 0.25) 0px 0px 0px 3px |

![Newsletter email field default](components/crops/nl-field-default.png) ![Newsletter email field focused](components/crops/nl-field-focused.png)

#### Subscribe button
The Subscribe submit. Measured in every state — never pressed. Read as `nl-submit` on the newsletter page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 152.19 x 50; padding 5px 5px 5px 22px; radius 999px; background #de4c00 `bright-citrus`; text Work Sans 15.04/15.04 500, #fffefb `off-white`; transition background 0.3s ease, transform 0.3s ease; icon 14 x 14, #fffefb `off-white` |
| hover | background #c44300 `dark-citrus` |
| focus-visible | outline 2px solid #e67940 `orange-peel`, offset 3px |
| pressed | size 149.14 x 49; background #c44300 `dark-citrus`; transform scale(0.98); icon 13.72 x 13.72, #fffefb `off-white` |

![Subscribe button default](components/crops/nl-submit-default.png) ![Subscribe button hover](components/crops/nl-submit-hover.png) ![Subscribe button focus-visible](components/crops/nl-submit-focus-visible.png) ![Subscribe button pressed](components/crops/nl-submit-pressed.png)

#### Latest issue title
"Meet Aboard Sign" — the latest-issue headline. Read as `nl-latest-title` on the newsletter page.

**Values (default).** size 412.61 x 57.27; background transparent; text Tobias 56.16/57.28 400, #06070a `ink`; transition color 0.4s ease.

![Latest issue title default](components/crops/nl-latest-title-default.png)

#### Newsletter card form
The boxed variant of the signup (is-card) under the article. Read as `nl-form-card` on the newsletter article page.

**Values (default).** size 560 x 81.94; background transparent; text Work Sans 15.04/15.04 500, #ffffff `white`; icon 14 x 14, #ffffff `white`.

Child layers that carry the look: input 397.8x50 background #fffefb `off-white` border 1px solid rgba(6, 7, 10, 0.1) `line` radius 999px; button 152.2x50 background #06070a `ink` radius 999px; span 40x40 background rgba(255, 255, 255, 0.16) radius 50%.

![Newsletter card form default](components/crops/nl-form-card-default.png)

#### Events email field
The email field of the events signup row; clicked into, nothing typed. Read as `ev-field` on the events page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 796.48 x 50; padding 0px 18px; border 1px solid rgba(6, 7, 10, 0.1) `line`; radius 999px; background #fffefb `off-white`; text Work Sans 16/16 400, #06070a `ink`; transition border-color 0.3s ease, box-shadow 0.3s ease; placeholder #6f6a63 `muted` |
| focused | border 1px solid #de4c00 `bright-citrus`; shadow rgba(222, 76, 0, 0.16) 0px 0px 0px 3px |

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Events submit button
The events signup submit. Measured in every state, never pressed. Read as `ev-submit` on the events page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 133.77 x 50; padding 5px 5px 5px 22px; radius 999px; background #06070a `ink`; text Work Sans 15.04/15.04 500, #fffefb `off-white`; transition background 0.35s ease; icon 14 x 14, #fffefb `off-white` |
| hover | background #de4c00 `bright-citrus` |
| focus-visible | outline 2px solid #de4c00 `bright-citrus`, offset 4px |
| pressed | background #de4c00 `bright-citrus` |

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

### About, careers, security

The company pages in the same shell: team photos on about, the openings list on careers, the security posture text.

#### About title
Read as `about-title` on the about page.

**Values (default).** size 1000.08 x 220.31; background transparent; text Tobias 72/73.44 400, #06070a `ink`.

![About title default](components/crops/about-title-default.png)

#### about body text
Read as `about-body` on the about page.

**Values (default).** size 770.8 x 263.56; background transparent; text Tobias 63.36/65.89 300, rgba(7, 7, 10, 0.875).

![about body text default](components/crops/about-body-default.png)

#### Team member
A person card/photo on the about page. Read as `about-person` on the about page.

**Values (default).** size 770.8 x 347.72; background transparent; text Tobias 63.36/65.89 300, #06070a `ink`.

Child layers that carry the look: figcaption 770.8x48.2 border 2px solid #de4c00 `bright-citrus`.

![Team member default](components/crops/about-person-default.png)

#### FAQ title
Read as `faq-title` on the FAQ page.

**Values (default).** size 1000.08 x 73.44; background transparent; text Tobias 72/73.44 400, #06070a `ink`.

![FAQ title default](components/crops/faq-title-default.png)

#### FAQ category
A category heading inside the FAQ ("AI consulting, strategy & managed services"). Read as `faq-cat` on the FAQ page.

**Values (default).** size 885.45 x 47.91; background transparent; text Tobias 46.08/47.92 400, #06070a `ink`.

![FAQ category default](components/crops/faq-cat-default.png)

#### FAQ question
A question row of the FAQ accordion. Read as `faq-q` on the FAQ page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 885.45 x 80; background transparent; text Tobias 24/28.8 300, #06070a `ink` |
| hover | text Tobias 24/28.8 300, #de4c00 `bright-citrus` |

Child layers that carry the look: span 36x36 border 1px solid rgba(6, 7, 10, 0.1) `line` radius 50%; span::before 12pxx1.5px background #06070a `ink` radius 1px; span::after 12pxx1.5px background #06070a `ink` radius 1px.

![FAQ question default](components/crops/faq-q-default.png) ![FAQ question hover](components/crops/faq-q-hover.png)

#### FAQ panel (open)
The answer panel after its question was pressed; a local disclosure, nothing sent. Read as `faq-panel-open` on the FAQ page.

**Values (open).** size 885.45 x 385.08; background transparent; text Work Sans 16/26.4 400, #3d3a36 `body`.

![FAQ panel (open) open](components/crops/faq-panel-open-open.png)

#### FAQ question (open)
The question row after being pressed once. Read as `faq-q-open` on the FAQ page.

**Values (open).** size 885.45 x 80; background transparent; text Tobias 24/28.8 300, #06070a `ink`.

Child layers that carry the look: span 50.9x50.9 background #06070a `ink` border 1px solid #06070a `ink` radius 50%; span::before 12pxx1.5px background #fffefb `off-white` radius 1px; span::after 12pxx1.5px background #fffefb `off-white` radius 1px.

![FAQ question (open) open](components/crops/faq-q-open-open.png)

#### Careers title
Read as `careers-title` on the careers page.

**Values (default).** size 1000.08 x 293.75; background transparent; text Tobias 72/73.44 400, #06070a `ink`.

![Careers title default](components/crops/careers-title-default.png)

#### careers body text
Read as `careers-body` on the careers page.

**Values (default).** size 312.25 x 51.84; background transparent; text Work Sans 17.28/25.92 400, #3d3a36 `body`.

![careers body text default](components/crops/careers-body-default.png)

#### Job row
An opening on the careers page. Read as `job-row` on the careers page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 713.45 x 38.02; background transparent; text Tobias 34.56/38.01 300, #06070a `ink`; transition color 0.4s ease |
| hover | size 699.19 x 38.02; text Tobias 34.56/38.01 300, #de4c00 `bright-citrus` |

![Job row default](components/crops/job-row-default.png) ![Job row hover](components/crops/job-row-hover.png)

#### Security title
Read as `security-title` on the security page.

**Values (default).** size 770.8 x 73.44; background transparent; text Tobias 72/73.44 400, #06070a `ink`.

![Security title default](components/crops/security-title-default.png)

#### security body text
Read as `security-body` on the security page.

**Values (default).** size 541.52 x 77.77; background transparent; text Work Sans 17.28/25.92 400, #3d3a36 `body`.

![security body text default](components/crops/security-body-default.png)

### Mobile (390 wide)

A few components as a phone draws them, at 390 x 844: the header with its Open-menu trigger, the opened nav panel, the hero title and a feed row.

#### Mobile top bar
The mobile header: wordmark left, menu trigger right. Read as `m-nav-bar` on the home page at 390 wide.

**Values (default).** size 390 x 72; padding 12px 12px 0px 12px; background transparent; text Work Sans 14.08/22.52 400, #fffefb `off-white`; icon 107.05 x 26, #271503 `warm-black`.

Child layers that carry the look: nav::before 350pxx60px background rgba(240, 241, 239, 0.84) radius 28px; a::after 9pxx9px background #271503 `warm-black`; ul 0x0 background rgba(250, 245, 239, 0.97) radius 14px shadow rgba(39, 21, 3, 0.18) 0px 14px 34px -22px.

![Mobile top bar default](components/crops/m-nav-bar-default.png)

#### Mobile menu trigger
The "Open menu" button. Pressed once below to open the menu; a local disclosure. Read as `m-menu-trigger` on the home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 44 x 44; background transparent; text Work Sans 16/25.6 400, #271503 `warm-black` |
| focus-visible | radius 2px; outline 2px solid #271503 `warm-black`, offset 2px |

Child layers that carry the look: span 20x1.5 background #271503 `warm-black`; span 20x1.5 background #271503 `warm-black`; span 20x1.5 background #271503 `warm-black`.

![Mobile menu trigger default](components/crops/m-menu-trigger-default.png) ![Mobile menu trigger hover](components/crops/m-menu-trigger-hover.png) ![Mobile menu trigger focus-visible](components/crops/m-menu-trigger-focus-visible.png) ![Mobile menu trigger pressed](components/crops/m-menu-trigger-pressed.png)

#### Mobile menu (open)
The opened mobile menu panel; pressed once, nothing navigated. Read as `m-nav-panel` on the home page at 390 wide.

**Values (open).** size 350 x 643.41; radius 28px; background transparent; text Work Sans 14.08/22.52 400, #fffefb `off-white`; transition color 0.5s cubic-bezier(0.65, 0, 0.35, 1), max-width 0.7s cubic-bezier(0.65, 0, 0.35, 1), transform 0.7s cubic-bezier(0.65, 0, 0.35, 1); icon 107.05 x 26, #271503 `warm-black`.

Child layers that carry the look: nav::before 350pxx643.406px background rgba(240, 241, 239, 0.84) radius 28px; a::after 9pxx9px background #271503 `warm-black`; ul 0x0 background rgba(250, 245, 239, 0.97) radius 14px shadow rgba(39, 21, 3, 0.18) 0px 14px 34px -22px.

![Mobile menu (open) open](components/crops/m-nav-panel-open.png)

#### Mobile hero title
Read as `m-hero-title` on the home page at 390 wide.

**Values (default).** size 350 x 89.59; background transparent; text Tobias 44.8/44.8 400, #271503 `warm-black`.

![Mobile hero title default](components/crops/m-hero-title-default.png)

#### Mobile feed row
Read as `m-feed-row` on the home page at 390 wide.

**Values (default).** size 350 x 232.81; padding 24px 0px; background transparent; text Work Sans 11.52/18.43 600, #271503 `warm-black`; transition transform 0.6s cubic-bezier(0.32, 0.72, 0, 1); icon 13 x 13, #de4c00 `bright-citrus`.

Child layers that carry the look: span 120x120 background #efe7db `thumb-warm` radius 12px.

![Mobile feed row default](components/crops/m-feed-row-default.png)

## Icons

28 SVGs were lifted from the pages into [icons/](icons), named by role, with the source table in [icons/INDEX.tsv](icons/INDEX.tsv). Colour is `currentColor` wherever the icon took its colour from the text, so each recolours from CSS `color`. Photography and artwork were left out; these are the interface icons (the wordmark, the menu trigger, the player controls, arrows). The SVGs are Aboard's property, kept for reference only.

| Icon | Rendered sizes | View box | Style | Seen on | Next to |
|---|---|---|---|---|---|
| [all](icons/all.svg) | 15x15 | 0 0 16 16 | stroke |  | All |
| [all-case-studies](icons/all-case-studies.svg) | 14x14 | 0 0 16 16 | stroke | how-we-work/ | All case studies |
| [chemistry-discovering-tomorrow-s-products-with-supercharged](icons/chemistry-discovering-tomorrow-s-products-with-supercharged.svg) | 11x11 | 0 0 24 24 | fill | case-studies/ | CHEMISTRY Discovering tomorrow’s products with supercharged  |
| [close-player](icons/close-player.svg) | 12x12 | 0 0 12 12 | stroke | podcast/ | Close player |
| [copied](icons/copied.svg) | 18x18 | 0 0 20 20 | stroke | meet-aboard-sign/ | Copied |
| [data-mapped](icons/data-mapped.svg) | 20x20 | 0 0 16 16 | stroke | how-we-work/ | Data mapped |
| [event-office-hours-can-ai-help-nonprofits-fundraise-12-n](icons/event-office-hours-can-ai-help-nonprofits-fundraise-12-n.svg) | 13x13 | 0 0 16 16 | stroke |  | EVENT Office Hours: Can AI Help Nonprofits Fundraise? ↗ 12 N |
| [events](icons/events.svg) | 15x15 | 0 0 16 16 | stroke |  | Events |
| [expected-outcome-62-average-year-0-5-c-past-1-c-recent-1-5](icons/expected-outcome-62-average-year-0-5-c-past-1-c-recent-1-5.svg) | 11x13 | 0 0 16 16 | stroke | ; case-studies/ | Expected outcome 62% average year 0.5°C Past 1°C Recent 1.5° |
| [get-in-touch](icons/get-in-touch.svg) | 13x13 | 0 0 16 16 | stroke | ; how-we-work/; case-studies/; newsletter/; podcast/; about/; faq/; meet-aboard-sign/ | Get in Touch |
| [in-media](icons/in-media.svg) | 15x15 | 0 0 16 16 | stroke |  | In Media |
| [in-media-the-open-secret-buried-in-anthropic-s-300-page-i-p](icons/in-media-the-open-secret-buried-in-anthropic-s-300-page-i-p.svg) | 13x13 | 0 0 16 16 | stroke |  | IN MEDIA The Open Secret Buried in Anthropic’s 300-Page I.P. |
| [learn-more-about-us](icons/learn-more-about-us.svg) | 20x20 | 0 0 16 16 | stroke |  | Learn more about us |
| [newsletter](icons/newsletter.svg) | 15x15 | 0 0 16 16 | stroke |  | Newsletter |
| [newsletter-meet-aboard-sign-5-nov-2026-sign-contracts-for](icons/newsletter-meet-aboard-sign-5-nov-2026-sign-contracts-for.svg) | 13x13 | 0 0 16 16 | stroke |  | NEWSLETTER Meet Aboard Sign ↗ 5 NOV 2026 Sign contracts for  |
| [next-case-study](icons/next-case-study.svg) | 29x29 | 0 0 24 24 | stroke |  | Next case study |
| [pause-case-studies](icons/pause-case-studies.svg) | 14x14 | 0 0 16 16 | fill |  | Pause case studies |
| [play-episode-anthony-ha-dispatches-from-a-techcrunch-ai-r](icons/play-episode-anthony-ha-dispatches-from-a-techcrunch-ai-r.svg) | 16x16 | 0 0 16 16 | fill | podcast/ | Play episode : Anthony Ha: Dispatches from a TechCrunch AI R |
| [podcast](icons/podcast.svg) | 15x15 | 0 0 16 16 | stroke |  | Podcast |
| [podcast-anthony-ha-dispatches-from-a-techcrunch-ai-reporter](icons/podcast-anthony-ha-dispatches-from-a-techcrunch-ai-reporter.svg) | 13x13 | 0 0 16 16 | stroke |  | PODCAST Anthony Ha: Dispatches from a TechCrunch AI Reporter |
| [previous-case-study](icons/previous-case-study.svg) | 29x29 | 0 0 24 24 | stroke |  | Previous case study |
| [rss](icons/rss.svg) | 22x22 | 0 0 20 20 | stroke | podcast/ | RSS |
| [share-by-email](icons/share-by-email.svg) | 18x18 | 0 0 20 20 | stroke | meet-aboard-sign/ | Share by email |
| [share-on-linkedin](icons/share-on-linkedin.svg) | 18x18 | 0 0 20 20 | fill | meet-aboard-sign/ | Share on LinkedIn |
| [share-on-x](icons/share-on-x.svg) | 18x18 | 0 0 20 20 | fill | meet-aboard-sign/ | Share on X |
| [the-aboard-newsletter](icons/the-aboard-newsletter.svg) | 14x14 | 0 0 16 16 | stroke | meet-aboard-sign/ | THE ABOARD NEWSLETTER |
| [unlocking-the-potential-of-hundreds-of-community-health-cent](icons/unlocking-the-potential-of-hundreds-of-community-health-cent.svg) | 15x15 | 0 0 24 24 | fill | ; case-studies/ | Unlocking the potential of hundreds of community health cent |
| [view-all-case-studies](icons/view-all-case-studies.svg) | 13x13 | 0 0 16 16 | stroke | ; newsletter/; podcast/; faq/; meet-aboard-sign/ | View all case studies |

## Gaps

### Pages

- **There is no account area.** aboard.com is a marketing site with one form (the newsletter signup); there is no login, dashboard, cart or checkout to be behind.
- **The contact path is the signup.** The "Get in Touch" CTA and the #contact section embed the same newsletter-signup iframe (`/contact-form/?iframe=contactForm`), a same-origin page that posts to a WordPress REST endpoint. It was measured as a frame and at rest; no address was typed and nothing was submitted.
- **Embedded media.** Podcast and article pages embed third-party players (YouTube iframes and the like); the embeds were screenshotted in place but not opened, played or probed.
- **External destinations.** The footer and cards link out to LinkedIn, YouTube, Instagram, Facebook and X; outbound pages were not visited.

### States

- **Pressed** was forced with DevTools (`:active`), so a state a script adds on mousedown is missing if one exists.
- **The consent states.** Customize / Accept All / the modal's preference toggles were measured but never clicked: the post-consent UI is uncaptured.
- **Audio playback.** The podcast dock's transport buttons were measured at rest; playback was never started, so playing/paused/buffering states are missing.
- **Carousel autoplay.** The home carousel's ticks and pause button were measured at rest; the pause toggle was not flipped.
- **Disabled states** were not seen on any public control.

### Themes

Aboard shows one theme. The page paints warm off-white (`--wp--preset--color--parchment` / `--rd-parchment`) with dark forest-green and bright-citrus sections inside the same paint; there is no `prefers-color-scheme` variant and no theme attribute, so the token file ships a single `light` set. Roughly 640 custom properties resolve from the WordPress theme sheets (see [raw/css-vars.json](raw/css-vars.json)); the token file aliases the --wp--preset--* and --rd-* names where the site declares them.

### Fonts

- **Work Sans** is the interface sans (headings, nav, buttons, body); **Tobias** is the serif used for display headings and card titles. Both are served same-origin by the theme; the @font-face rules are in [raw/css-vars.json](raw/css-vars.json).

### Screenshots

- Photography, project artwork and media frames are Aboard's content and appear only inside screenshots and crops.
- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files.

### Content left out

- Article body text, case-study copy and the FAQ answers were not transcribed; only the frames around them were measured.
- No personal data was captured: every page was read signed out, and the only form touched was the newsletter field measured and left empty.
