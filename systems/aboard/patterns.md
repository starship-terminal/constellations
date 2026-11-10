# Aboard patterns

How Aboard's components combine to do the recurring jobs on its public marketing pages, written from the captures of 2026-11-09 (signed out, 1440 and 390 wide). Each pattern says when the site uses it, the components it is built from (entries in [components.md](components.md), values in [tokens.json](tokens.json)), the layout, and the screens that show it. These are observations of what the site does, not Aboard's own guidance.

| Pattern | Captured | Example screen |
|---|---|---|
| [Shell and navigation](#shell-and-navigation) | yes | [home-light-default](screenshots/home-light-default.png) |
| [Editorial hero](#editorial-hero) | yes | [home-light-default](screenshots/home-light-default.png) |
| [Content feed pages](#content-feed-pages) | yes | [perspectives-light-full](screenshots/perspectives-light-full.png) |
| [Case-study cards](#case-study-cards) | yes | [case-studies-light-full](screenshots/case-studies-light-full.png) |
| [Dark content bands](#dark-content-bands) | yes | [newsletter-light-default](screenshots/newsletter-light-default.png) |
| [Signup forms](#signup-forms) | yes, at rest and focus only | [newsletter-light-default](screenshots/newsletter-light-default.png) |
| [Consent](#consent) | no, never rendered | [home-light-cookie-banner](screenshots/home-light-cookie-banner.png) |
| [Mobile fold](#mobile-fold) | yes | [mobile-home-light-menu-open](screenshots/mobile-home-light-menu-open.png) |

## Shell and navigation

**When.** Every public page: the marketing pages, the content indexes and the article page all sit inside the same shell.

**Components.** [Top navigation bar](components.md#top-navigation-bar), [Logo](components.md#logo), [Nav link](components.md#nav-link), [Get-in-touch CTA](components.md#get-in-touch-cta), [Skip link](components.md#skip-link), and the footer set: [Footer](components.md#footer), [Footer heading](components.md#footer-heading), [Footer link](components.md#footer-link), [Social link](components.md#social-link), [Contact iframe](components.md#contact-iframe).

**Layout.** The header is not a bar but a floating pill: `nav::before` paints a 1328 x 60 rounded pill in `#f0f1ef` at 84% alpha (`component.nav-pill-bg`), fixed at the top inside the 78px header (`layout.header-height`). It carries the wordmark, five Work Sans section links (15px, pill hover wash `component.nav-hover-bg`) and the citrus "Get in Touch" pill (`component.button-primary-bg` → `button-primary-active-bg` near-black on hover). The footer is the inverse: a full-bleed bright-citrus band (`light.accent`) with the Tobias "We Can Help" heading, the signup iframe, off-white link columns separated by `border.inverse` hairlines, and a giant clipped wordmark along the bottom edge.

**Screens.** [home-light-default](screenshots/home-light-default.png), [newsletter-light-full](screenshots/newsletter-light-full.png) (the footer), [about-light-default](screenshots/about-light-default.png).

## Editorial hero

**When.** The home page and every index page open the same way: a Tobias display headline on the cream ground, often under a small tracked eyebrow.

**Components.** [Hero title](components.md#hero-title), [Eyebrow label](components.md#eyebrow-label), [Section title](components.md#section-title), [Carousel tick](components.md#carousel-tick), [Carousel pause](components.md#carousel-pause).

**Layout.** Page heroes run `typography.display` (Tobias ~72-78px at ~1.02, tracked -2.5%) in `light.text` warm-black on `light.page`. On the home page the headline sits above a full-width media carousel (`cc-*` slides cross-fading over 900ms on `--rd-ease-io`) whose captions restyle per slide; `carousel-tick` marks progress with short 35px bars and `carousel-pause` toggles autoplay. Index pages swap the carousel for a simple headline block (`perspectives-title`, `newsletter-title`, `pod-title`, `cases-title` at up to 123.8px). Headline words reveal one at a time on scroll: 50ms stagger (`duration.stagger`) moving 48px over ~1.2s (`--rd-reveal-*`).

**Screens.** [home-light-default](screenshots/home-light-default.png), [case-studies-light-default](screenshots/case-studies-light-default.png), [newsletter-light-default](screenshots/newsletter-light-default.png).

## Content feed pages

**When.** Perspectives, Newsletter, Events and In Media: four indexes that share one row pattern — a small caps kind tag, a Tobias row title, and a date, on a hairline.

**Components.** [Index row](components.md#index-row) (per feed: [Perspectives](components.md#index-row), [Newsletter](components.md#index-row-1), [Events](components.md#index-row-2), [Media](components.md#index-row-3)), [Row title](components.md#row-title), [Feed row kind tag](components.md#feed-row-kind-tag), [Event kind tag](components.md#event-kind-tag), [Media show-more button](components.md#media-show-more-button).

**Layout.** Rows are a three-column grid — kind tag (`typography.tag`: Work Sans ~11px semibold, tracked +0.15em, `muted-warm`), Tobias title at `typography.card-title` (~29-37px, weight 300, tracked -2.5%), date — separated by `light.border-warm` hairlines and padded by the `core.spacing` scale. Thumbnails where present are `component.thumb-bg` blocks at `radius.card`. The home page reuses the same row for its "Perspectives" feed.

**Screens.** [perspectives-light-full](screenshots/perspectives-light-full.png), [newsletter-light-full](screenshots/newsletter-light-full.png), [events-light-full](screenshots/events-light-full.png), [media-light-full](screenshots/media-light-full.png).

## Case-study cards

**When.** The case-studies index and the home carousel link to client work through image cards.

**Components.** [Featured case card](components.md#featured-case-card), [Case card](components.md#case-card), [Case industry tag](components.md#case-industry-tag), [Case study title](components.md#case-study-title), [Case study body](components.md#case-study-body), [Case study meta](components.md#case-study-meta).

**Layout.** A card is a `radius.card` media figure over a warm hairline. The figure bases on `component.card-dark-bg` (`#1a110a`) and lifts at hover on `shadow.card` (`0 40px 80px -48px` black at ~0.54, easing in over ~300ms); a `component.live-dot` green dot marks recordings. Under it, an all-caps industry tag (`typography.tag`) and a Tobias title. The featured card spans full width (1328 x 703 measured); grid cards sit two-up (~632 wide). Inside a case study, `typography.page-title` (59px) opens the article and `cs-body` leads at ~23px (`typography.lead`).

**Screens.** [case-studies-light-default](screenshots/case-studies-light-default.png), [case-studies-light-full](screenshots/case-studies-light-full.png), [case-study-light-full](screenshots/case-study-light-full.png).

## Dark content bands

**When.** Sections that invert the palette without leaving the single theme: the newsletter page hero, the podcast index rows and dock, the events signup band, the foundry project panel.

**Components.** [Podcast title](components.md#podcast-title), [Episode row](components.md#episode-row), [Episode title](components.md#episode-title), [Player seek bar](components.md#player-seek-bar), [Player button](components.md#player-button), [Events email field](components.md#events-email-field), [Events submit button](components.md#events-submit-button), [Foundry product card](components.md#foundry-product-card).

**Layout.** Dark bands reuse the same palette tokens: cream `palette.cream`/`light.text-inverse` text on `palette.case-dark`-family fills (`#1a110a`, the `#00040f` podcast backdrop at 42%, `palette.pod-navy` on the play tile), hairlines at `border.inverse` (off-white at 30%), and translucent cream field fills (`component.field-bg-dark`, 8%). The podcast dock shows the small pattern language: a navy 10px-radius play tile, episode rows in Tobias 28.8px, and `tan-suit` meta text. Nothing dark inverts the page background — bands are bounded rectangles inside the light page.

**Screens.** [podcast-light-full](screenshots/podcast-light-full.png), [podcast-episode-light-full](screenshots/podcast-episode-light-full.png), [newsletter-light-default](screenshots/newsletter-light-default.png).

## Signup forms

**When.** The one public form, the newsletter signup, appears three ways: the dark variant on the newsletter page and in the citrus footer iframe, the light `is-card` variant on the article page, and the events band's ink submit.

**Components.** [Newsletter form](components.md#newsletter-form), [Newsletter email field](components.md#newsletter-email-field), [Subscribe button](components.md#subscribe-button), [Newsletter card form](components.md#newsletter-card-form), [Events email field](components.md#events-email-field), [Events submit button](components.md#events-submit-button), [Contact iframe](components.md#contact-iframe), [Newsletter card](components.md#newsletter-card).

**Layout.** The row form is a 50px pill field (`component.field-bg-dark` + `light.field-border` on dark; `component.field-bg-light` + `light.border` hairline on light) beside a 50px pill submit with a 40px frosted icon disc. Field focus swaps the border to `light.focus` orange-peel and adds `shadow.focus-ring` (3px halo at 25%); the submit's own focus ring is a 2px orange-peel outline offset 3px. Submit colours invert by band: citrus → dark-citrus on dark (`button-primary-*`), ink → citrus on light (`button-dark-*`/`ev-submit`). Pressed scales the button to 0.98. The form posts to `/wp-json/aboard/v1/newsletter-signups` — measured at rest and focus only, never submitted.

**Screens.** [newsletter-light-default](screenshots/newsletter-light-default.png), [aboard-sign-light-full](screenshots/aboard-sign-light-full.png) (the card variant), [home-light-contact](screenshots/home-light-contact.png).

## Consent

**When.** A CookieYes consent strip (`.cky-*`) is wired into every page through the CMP script.

**Components.** [Cookie consent strip](components.md#cookie-consent-strip), [Accept-all button](components.md#accept-all-button), [Customize button](components.md#customize-button), [Consent close button](components.md#consent-close-button) — all recorded `missing`.

**Layout.** Unknown: the strip never rendered in headless Chromium during the capture, so its colours and geometry are unmeasured. The capture kit hides `.cky-consent-container` for the clean screenshots (a hide, not a consent); `home-light-cookie-banner.png` records the page without it. The style guide holds a placeholder panel, not a measurement.

**Screens.** [home-light-cookie-banner](screenshots/home-light-cookie-banner.png).

## Mobile fold

**When.** Every page at 390: the floating pill collapses to a trigger, and feeds stack single-column.

**Components.** [Mobile top bar](components.md#mobile-top-bar), [Mobile menu trigger](components.md#mobile-menu-trigger), [Mobile menu (open)](components.md#mobile-menu-open), [Mobile hero title](components.md#mobile-hero-title), [Mobile feed row](components.md#mobile-feed-row).

**Layout.** At 390 the same frosted pill shrinks to a 44px hamburger trigger; opened, it grows a 350 x 643 sheet at `radius.menu` 28px (`m-nav-panel`), still `#f0f1ef` at 84%. Display type compresses fluidly — the hero drops from 77.76px to 44.8px (`font.size.m-display`) — and feed rows reflow to a single column. The menu trigger was the only real press in the mobile capture (a local disclosure).

**Screens.** [mobile-home-light-default](screenshots/mobile-home-light-default.png), [mobile-home-light-menu-open](screenshots/mobile-home-light-menu-open.png), [mobile-home-light-full](screenshots/mobile-home-light-full.png), [mobile-case-studies-light-full](screenshots/mobile-case-studies-light-full.png).
