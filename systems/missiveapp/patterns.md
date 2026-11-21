# Missive patterns

How the measured components compose into missiveapp.com's public pages. Values are in [components.md](components.md) and [tokens.json](tokens.json). The screenshots named below are in [screenshots/](screenshots). Which control opens which page is in [site-tree.md](site-tree.md).

## The shell

A white bar, 61px tall, with the wordmark on the left and a compact link set on the right: Product, Pricing, Customers, Resources, then Log in, Book a demo, and a blue Try for free. ([home-light-default](screenshots/home-light-default.png), `header`, `nav-link`, `nav-cta`)

Hovering Product opens a mega menu on the same page: Collaborate, Coordinate, Connect, then Explore and Industries. ([home-light-product-menu](screenshots/home-light-product-menu.png)) Hovering Resources opens Help, Download and Blog. ([home-light-resources-menu](screenshots/home-light-resources-menu.png))

At 390 the links collapse behind a 40px menu button. The open list covers the page and includes Log in, a blue Sign up, and the same groups. ([mobile-home-light-menu](screenshots/mobile-home-light-menu.png)) Log in and Sign up go to the login wall and were not followed.

## The hero

A Tiempos Headline line, 56px, over a short supporting line, then a blue Try for free and a grey Watch demo. The page behind them is white. ([home-light-default](screenshots/home-light-default.png), `hero-title`, `hero-cta`, `hero-secondary`)

Watch demo opens a lightbox on the same URL. The Try for Free link inside it goes to the signup wall and was not followed. ([home-light-demo](screenshots/home-light-demo.png))

## Pricing

`/pricing` is three plan columns: Starter, Productive, Business. Each card is about 401 x 422, with a 16px radius on the left corners and a 1px `#e4e6e9` border. Plan CTAs go to the signup wall and were not followed. FAQ questions sit below as 800 x 60 accordions. ([pricing-light-default](screenshots/pricing-light-default.png), [pricing-light-faq](screenshots/pricing-light-faq.png), `plan-card`, `faq-question`)

## Feature, docs and story pages

Pillar pages (`/collaborate`, `/coordinate`, `/connect`), `/features`, `/integrations`, `/ai-assistant` and `/customers` repeat the same nav and the same hero rhythm. Customer stories, blog posts, changelog posts, integrations, partners and compare pages share one template each. ([features-light-default](screenshots/features-light-default.png), [customers-light-default](screenshots/customers-light-default.png))

`/docs` is the public help center: a search field, 338 x 37 at rest and wider when focused, plus a chat field that was not measured. Neither was submitted. ([docs-light-default](screenshots/docs-light-default.png), `docs-search`)

## The footer

A dark band, ink `#050607`, with white headings and `#cdd0d4` links in columns: Product, Learn, Company, pillars, use cases, solutions, compare, legal, and a language switch to `/fr`. ([home-light-full](screenshots/home-light-full.png), `footer`, `footer-link`)

## What these pages do not compose

No public page shows a checkbox, radio, switch, toast, table, or a destructive confirmation. No page shows a disabled, error, loading, or selected control. The signed-in inbox is behind https://mail.missiveapp.com/#login and is not part of these patterns.
