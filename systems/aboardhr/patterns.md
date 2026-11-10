# Aboard HR patterns

How the measured components combine into aboardhr.com's marketing pages. Every value below is a token in [tokens.json](tokens.json); the crops and screenshots named are the evidence.

## The fixed translucent band

Every page opens under the same 90px header (64px at 390): the Aboard wordmark left, muted 15px nav links (`light.muted`, ink at 70%) that wash `rgba(112,112,121,0.08)` on hover, and on the right a Sign-in link plus the light-blue "Book a demo" pill (`component.button-secondary-bg` fill, `accent-ink` text). The band paints a 0-offset shadow declaration that draws nothing; the page is flat. At 390 it collapses to logo plus the hamburger trigger, opening a full-width menu sheet.

- Components: [nav-bar](components.md#top-navigation-bar), [nav-link](components.md#nav-link), [nav-cta](components.md#nav-cta), [m-nav-bar](components.md#mobile-top-bar), [m-menu-trigger](components.md#mobile-menu-trigger), [m-nav-panel](components.md#mobile-menu-open)
- Screens: [home-light-default](screenshots/home-light-default.png), [mobile-home-light-menu-open](screenshots/mobile-home-light-menu-open.png)

## The centred hero with the animated demo

The home hero centres a 768px column: the 64px display headline (`core.typography.display`, semibold, tracked -0.6px), the muted 20/32 lead, then the CTA pair — a blue `component.button-primary-bg` pill and a tint `button-secondary-bg` pill, both 48px tall, 18px semibold. The hero carries the animated co-pilot demo: a chat mock with the "Ask me anything" prompt inside a `tint-blue` panel. It is a marketing animation, not a live product.

- Components: [hero-title](components.md#hero-title), [hero-sub](components.md#hero-subtitle), [cta-demo](components.md#primary-cta), [cta-try](components.md#secondary-cta), [copilot-demo](components.md#co-pilot-demo-panel)
- Screens: [home-light-default](screenshots/home-light-default.png), [home-light-copilot](screenshots/home-light-copilot.png), [mobile-home-light-default](screenshots/mobile-home-light-default.png)

## The pastel product-card bands

Sections alternate the flat `#fafafa` ground with pastel bands; inside them, cards are 24px-radius flat panels (`card-blue`, `card-teal`, `card-pink`) with a 44px semibold headline, medium-weight feature rows, and a CTA. Two cards grid at 330px columns with a 20px gap inside a 680px column. No borders, no shadows — the tint does all the separation. The product pages repeat the pattern per product (Everyday HR mint, Growth & feedback, Team culture pink).

- Components: [feature-card](components.md#feature-card), [feature-item](components.md#feature-list-item), [everyday-hr-card](components.md#feature-card-2), [team-culture-card](components.md#feature-card-3), [learn-more](components.md#learn-more-link)
- Screens: [home-light-full](screenshots/home-light-full.png), [everyday-hr-light-default](screenshots/everyday-hr-light-default.png), [team-culture-light-default](screenshots/team-culture-light-default.png)

## The single plan card

Pricing is one white 24px-radius card on the flat ground: the 64px price figure ("80 kr") with a muted "/ user / month" suffix, feature rows, and a tint CTA. No billing toggle, no comparison table — the product sells one plan.

- Components: [price-card](components.md#plan-card), [price-amount](components.md#plan-price), [plan-cta](components.md#plan-cta)
- Screens: [pricing-light-default](screenshots/pricing-light-default.png), [mobile-pricing-light-full](screenshots/mobile-pricing-light-full.png)

## The quiet demo form

Book-a-demo is Framer's own form: Inter 12px labels at #888 over 40px controls filled `component.field-bg` (ink at 5%) with 12px radius — text inputs and selects with a drawn #999 arrow. The submit inverts the usual pattern: a white control drawing a 2px `component.submit-ring` (ink at 10%) instead of a fill. Measured at rest and at focus only; never submitted.

- Components: [demo-form](components.md#demo-form), [demo-field](components.md#demo-field), [demo-submit](components.md#demo-submit)
- Screens: [book-demo-light-default](screenshots/book-demo-light-default.png)

## The changelog and legal columns

What's new is a plain index of dated release rows (muted date, semibold title) on hairlines; each detail page is a single reading column with a back link. The legal pages are the same column with running copy. Nothing else on these pages deviates from the shared type and colour rules.

- Components: [release-row](components.md#release-row), [release-title](components.md#release-title), [release-back](components.md#back-link), [release-post](components.md#release-body), [terms-body](components.md#body-text-2)
- Screens: [whats-new-light-default](screenshots/whats-new-light-default.png), [release-light-default](screenshots/release-light-default.png), [terms-light-default](screenshots/terms-light-default.png)

## The light footer

The footer stays on the `#fafafa` ground: the "Smooth sailing." sign-off heading, link columns in `palette.grey-link` (#777, hover #555), and the Teamtailor credit row. No dark band, no coloured fill — the site's one loud surface is the hero's blue pill.

- Components: [footer](components.md#footer), [footer-heading](components.md#footer-heading), [footer-link](components.md#footer-link)
- Screens: any `-full` screenshot's bottom band

## The mobile fold

At 390 every page reflows single-column with a 16px gutter: the display step drops to 48px (`core.typography.display-mobile`), cards stack full-width, the header collapses to a 64px band with the trigger, and the CTA pills keep their 48px height. The menu opens as a full-width sheet under the band.

- Screens: [mobile-home-light-default](screenshots/mobile-home-light-default.png), [mobile-home-light-full](screenshots/mobile-home-light-full.png), [mobile-everyday-hr-light-full](screenshots/mobile-everyday-hr-light-full.png)
