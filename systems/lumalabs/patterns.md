# Luma AI patterns

How the measured components combine on each captured surface. Values are in [tokens.json](tokens.json). Components are in [components.md](components.md). Full-page evidence is in [screenshots/](screenshots).

## Home hero

https://lumalabs.ai/ paints a dark video hero under a light announcement strip. The nav is a wordmark, uppercase PRODUCT / PRICING / API / ENTERPRISE / MCP / NEWS / JOIN US labels, and a 32px white Sign In pill (`nav-signin`, 69 x 32). The heading (`hero-h1`, 576 x 125, 52px / 500) reads "Luma is your creative partner". Try for free (`hero-cta`, 155 x 48) is a white pill. Both link toward the app host. They were measured and never followed. See [home-dark-default](screenshots/home-dark-default.png).

Below the fold, a prompt composer (`prompt`, 510 x 76, 12px radius) sits on a dark card. Sample text was typed and deleted. Submit prompt (`prompt-submit`) was hovered and never clicked. Idea chips (`idea-chip`, 149 x 32) are local suggestions. See [home-dark-prompt-filled](screenshots/home-dark-prompt-filled.png).

## Pricing

https://lumalabs.ai/pricing paints the light page: white field, black heading (`price-h1`, 338 x 62), a Monthly / Yearly pill toggle (`price-monthly`, `price-yearly`). Plus and Ultra sit on the subtle surface. Pro inverts to black. Start Now (`price-cta`, 350 x 40) was measured and never followed. Following it is a sign-in and a checkout. See [pricing-light-default](screenshots/pricing-light-default.png) and [pricing-light-yearly](screenshots/pricing-light-yearly.png).

## API, about, news, enterprise

https://lumalabs.ai/api is a light page with Use the API (`api-cta`, 98 x 32, black pill) and Explore docs (`api-docs`). Use the API was never followed. The Uni-1.1 tab (`api-tab`) is a local toggle. See [api-light-default](screenshots/api-light-default.png).

https://lumalabs.ai/about is a light editorial page. The heading (`about-h1`) is a long Graphik sentence. See [about-light-default](screenshots/about-light-default.png).

https://lumalabs.ai/news is a light index with All / Company / Product / Engineering / Guides chips (`news-filter`) and article cards (`news-card`). Subscribe was not clicked. See [news-light-default](screenshots/news-light-default.png).

https://lumalabs.ai/enterprise opens on a dark photograph and a Talk to our team control. The form field (`ent-field`, 400 x 36) was focused and not filled. Submit (`ent-submit`) was hovered and never clicked. See [enterprise-light-default](screenshots/enterprise-light-default.png).

## Ray

https://lumalabs.ai/ray paints a dark cinematic page: white type on a generated still, Try in Luma and Build with API. Those CTAs were not followed. See [ray-dark-default](screenshots/ray-dark-default.png).

## Docs

https://docs.lumalabs.ai/docs/welcome is a public ReadMe hub (Guides, API Reference). Its sheets were harvested apart and are not in the marketing tokens. See [docs-light-default](screenshots/docs-light-default.png).

## Phone (390 x 844)

The home collapses to a wordmark, a 32px Sign In pill (`m-signin`) and a menu button (`m-menu`, 20 x 20). Opening the menu shows PRODUCT through JOIN US. Sign In inside it was not followed. See [mobile-home-dark-default](screenshots/mobile-home-dark-default.png) and [mobile-home-dark-nav](screenshots/mobile-home-dark-nav.png). Pricing at 390 stacks the plan cards. See [mobile-pricing-light-default](screenshots/mobile-pricing-light-default.png).

## What does not paint signed out

The app at https://app.lumalabs.ai redirects to a WorkOS sign-up host. Generation, account, billing, API keys and checkout were not entered. There is no public user gallery. A missing path on lumalabs.ai is a Vercel "Invalid slug" page, not a Luma 404, and was not kept.
