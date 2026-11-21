# Asana patterns

How the measured components compose into asana.com's public pages.
Values are in [components.md](components.md) and [tokens.json](tokens.json);
the screenshots named below are in [screenshots/](screenshots).

## The shell

A top nav with the Asana wordmark left and a compact link set right:
Products, Solutions, Pricing, then Log in and the near-black Get started pill
([home-light-default](screenshots/home-light-default.png),
`header`, `nav-link`, `nav-cta`). Opening Products shows a wide panel over the hero
([home-light-flyout](screenshots/home-light-flyout.png), `flyout-open`).
The control map is [site-tree.md](site-tree.md).
At 390 the links collapse behind a menu button opening a full-width panel
([mobile-home-light-menu](screenshots/mobile-home-light-menu.png),
`m-menu-open`).

## The hero

The landing is a large TWK Lausanne h1 over a supporting line and a CTA pair —
a near-black primary and a ghost secondary — sitting on `#f3f3f3` or white
panels with `#cfcfcf` hairlines ([home-light-default](screenshots/home-light-default.png),
`hero-title`, `hero-cta`, `eyebrow`, `section-heading`, `card`).

## Pricing

/pricing is a grid of plan columns — Personal / Starter / Advanced /
Enterprise — each with a name, a price line and a CTA, followed by
hairline FAQ accordions that open one at a time
([pricing-light-default](screenshots/pricing-light-default.png),
[pricing-light-faq](screenshots/pricing-light-faq.png),
`plan-card`, `plan-cta`, `faq-open`).

## Product and feature pages

/product/ai and /features repeat the same rhythm: caps eyebrow labels,
large headings, near-black CTAs, linked cards on white
([product-ai-light-default](screenshots/product-ai-light-default.png),
[features-light-default](screenshots/features-light-default.png)).
/resources is the same surface again with article cards
([resources-light-default](screenshots/resources-light-default.png)).

## The gates

/create-account is a centred sign-up gate: email field, a near-black
continue button and SSO options, 50px fields with 3px radii — measured,
never submitted ([create-account-light-default](screenshots/create-account-light-default.png),
`gate-field`, `gate-cta`, `gate-sso`). /sales is a contact form — 50px
text fields and dropdown selects under a heading — also measured, never
submitted ([sales-light-default](screenshots/sales-light-default.png),
`sales-title`, `sales-field`, `sales-select`).

## The footer

A multi-column link block: grouped headings, dense link lists and legal,
on the near-black `#0d0d0d` surface the footer actually paints (white text) ([home-light-full](screenshots/home-light-full.png),
`footer`).
