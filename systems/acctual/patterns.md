# Acctual patterns

The control map for these screens is [site-tree.md](site-tree.md). Auth walls (`app.acctual.com`, including `/sign-in`) are recorded there and were not entered.

How Acctual's components combine to do the recurring jobs on its public marketing pages, written from the captures of 2026-11-10 and the public recapture of 2026-11-21 (signed out, 1440x900 and 390x844). Each pattern says when the site uses it, the components it is built from (entries in [components.md](components.md), values in [tokens.json](tokens.json)), the layout, and the screens that show it. These are observations of what the site does, not Acctual's own guidance.

| Pattern | Captured | Example screen |
|---|---|---|
| [Shell and navigation](#shell-and-navigation) | yes | [home-light-default](screenshots/home-light-default.png) |
| [Centred-hero marketing page](#centred-hero-marketing-page) | yes | [home-light-full](screenshots/home-light-full.png) |
| [Fee comparison](#fee-comparison) | yes | [pricing-light-default](screenshots/pricing-light-default.png) |
| [Programmatic landing page](#programmatic-landing-page) | yes | [stablecoin-invoicing-light-full](screenshots/stablecoin-invoicing-light-full.png) |
| [Legal text page](#legal-text-page) | yes | [terms-light-default](screenshots/terms-light-default.png) |
| [Disclosure accordions and menus](#disclosure-accordions-and-menus) | yes | [mobile-home-light-menu-open](screenshots/mobile-home-light-menu-open.png) |
| [Mobile fold](#mobile-fold) | yes | [mobile-home-light-default](screenshots/mobile-home-light-default.png) |

## Shell and navigation

**When.** Every public page: home, pricing, company, blog, landing and legal pages all sit inside the same shell.

**Components.** [Top navigation bar](components.md#top-navigation-bar), [Logo](components.md#logo), [Nav link](components.md#nav-link), [Nav CTA](components.md#nav-cta), [Log-in link](components.md#log-in-link), [Announcement banner](components.md#announcement-banner), and the footer set: [Footer](components.md#footer), [Footer heading](components.md#footer-heading), [Footer link](components.md#footer-link).

**Layout.** The blue announcement strip (`light.accent`, Inter 14/24) sits above an 80px floating pill (`layout.nav-height`): `rgba(245,245,245,0.6)` frost over `blur(10px)`, a 0 1px 2px drop at 10% black, 20px bottom corners, spanning 1034px inside the 1072px container. It holds the wordmark, section links in 16px medium ink-70 (hover to black), a dimmer Log-in at ink-60 and the dark capsule CTA. The footer is a plain band on the page ground: the 20px semibold sign-off, link columns in muted (hover black-90) and the same capsule again. No hairlines, no shadows on the ground; sections separate by whitespace.

**Screens.** [home-light-default](screenshots/home-light-default.png), [pricing-light-default](screenshots/pricing-light-default.png), [blog-light-default](screenshots/blog-light-default.png).

## Centred-hero marketing page

**When.** The home page, and the template the other marketing pages echo: a centred hero over a long single column of bands.

**Components.** [Hero title](components.md#hero-title), [Invoice demo](components.md#invoice-demo), [Section title](components.md#section-title), [Fee item](components.md#fee-item), [Persona card](components.md#persona-card), [Security item](components.md#security-item), [FAQ item](components.md#faq-item).

**Layout.** A centred ~768px hero: the 64/72 semibold display with -1.92px tracking (`typography.display`), a `badge` pill (accent text on accent-tint) above and one dark capsule CTA below; blue check bullets quote the fees. The interactive invoice mock — white cards on hairlines with 12px labels — hangs off the hero's edge. Below, 40/48 section titles introduce bands on the same `#fafafa` ground: `#fafafa` persona cards (16px radius, 24px inset), the security trust rows, the FAQ accordion. The column centres at 1024px inside 1072px.

**Screens.** [home-light-default](screenshots/home-light-default.png), [home-light-invoice-demo](screenshots/home-light-invoice-demo.png), [home-light-full](screenshots/home-light-full.png).

## Fee comparison

**When.** The pricing page and the home hero's fee bullets: the product argues on cost with a simple comparison table.

**Components.** [Page title](components.md#pricing-title), [Fee comparison row](components.md#fee-comparison-row), [Page CTA](components.md#page-cta).

**Layout.** The comparison table alternates white cells on `row` (#f0f0f0 at 95%) separated by `#dbdbdb` hairlines, 64px rows across the 1024px column; a 48/56 page title tops the page and the dark capsule CTA closes it. The same fee numbers appear on the home hero as blue check bullets — the accent is the only colour in the argument.

**Screens.** [pricing-light-default](screenshots/pricing-light-default.png), [pricing-light-full](screenshots/pricing-light-full.png), [home-light-default](screenshots/home-light-default.png).

## Programmatic landing page

**When.** The templated acquisition pages: persona pages (freelancer-invoicing), product pages (stablecoin-invoicing) and ~30 /locations/* corridors (us-to-japan captured).

**Components.** Page title and Page CTA per template ([freelancer-invoicing](components.md#freelancer-invoicing-title), [stablecoin-invoicing](components.md#stablecoin-invoicing-title), [location](components.md#location-title)), [Section title](components.md#stablecoin-invoicing-section).

**Layout.** The product and corridor pages swap Open Runde for Selecta: dark hero panels run the Medium face at 72/72 (stablecoin) or 64/64 (location, white text on `#0d111b`-class dark fills), interior sections at 56/56. The freelancer persona page keeps the marketing fonts: Open Runde 48/56 on its title and 40/48 on sections. The shell and the dark capsule CTA are unchanged across all of them; body copy sits darker at black-90 on the product pages. One template serves every corridor and persona — capture one, and the rest differ only in copy and imagery.

**Screens.** [stablecoin-invoicing-light-default](screenshots/stablecoin-invoicing-light-default.png), [freelancer-invoicing-light-full](screenshots/freelancer-invoicing-light-full.png), [location-light-full](screenshots/location-light-full.png).

## Legal text page

**When.** Terms and privacy: the same shell carrying a heading and long grey body copy.

**Components.** [Page title](components.md#terms-title), [Body text](components.md#terms-body).

**Layout.** A 64px semibold title (terms, privacy) over Selecta Regular 18/28 body in `#666`, running the full length of the column; nothing else on the page but the shell. These pages are the longest captures (terms is ~24,400px at 1440) and tile under the 8-chunk cap.

**Screens.** [terms-light-default](screenshots/terms-light-default.png), [privacy-light-default](screenshots/privacy-light-default.png).

## Disclosure accordions and menus

**When.** The FAQ accordion on home and the mobile nav: the only controls on the site that open anything, both local disclosures pressed during capture.

**Components.** [FAQ item](components.md#faq-item) (default and open), [Mobile menu trigger](components.md#mobile-menu-trigger), [Mobile menu](components.md#mobile-menu-open).

**Layout.** FAQ rows sit at 1024px: a 16/24 medium question line with a plus mark; opened, the row grows to ~120px and the answer runs below in grey. At 390 the nav trigger (a 24px icon box at the right of the collapsed bar) opens a full-screen white menu: logo and close mark on top, section links stacked large, a white Log-in capsule over the dark Sign-up capsule. Neither control navigates; both are pure UI state.

**Screens.** [mobile-home-light-menu-open](screenshots/mobile-home-light-menu-open.png), [home-light-full](screenshots/home-light-full.png) (FAQ near the bottom).

## Mobile fold

**When.** Every page at 390: the same content single-columned.

**Components.** [Mobile top bar](components.md#mobile-top-bar), [Mobile menu trigger](components.md#mobile-menu-trigger), [Mobile menu](components.md#mobile-menu-open), [Mobile hero title](components.md#mobile-hero-title).

**Layout.** The floating pill collapses to a 48px bar (logo left, trigger right, same frost); the display drops to 40/48; the 1024px column becomes a 16px-gutter single rail; cards, fee rows and the accordion stack full-width. The desktop's centred hero stays centred.

**Screens.** [mobile-home-light-default](screenshots/mobile-home-light-default.png), [mobile-home-light-full](screenshots/mobile-home-light-full.png), [mobile-pricing-light-full](screenshots/mobile-pricing-light-full.png).
