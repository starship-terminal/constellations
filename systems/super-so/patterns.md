# Super patterns

How the public marketing site combines the components in [components.md](components.md). Screenshots are 256-colour. Read colours from [tokens.json](tokens.json).

## Marketing shell

Every `super.so` page hangs the same bar over Notion content. Logo left, six links, a white Sign in pill, a yellow Get started free pill. The bar is 80px and translucent white. The page ground is light.page. There is no sidebar.

Desktop: [home-light-default.png](screenshots/home-light-default.png). Phone: logo, the same yellow pill, and a hamburger that opens a white drawer. [mobile-home-light-menu.png](screenshots/mobile-home-light-menu.png).

Use cases and Features open in place. [home-light-use-cases-menu.png](screenshots/home-light-use-cases-menu.png), [home-light-features-menu.png](screenshots/home-light-features-menu.png). On the phone they are chevrons in the drawer. [mobile-home-light-menu-use-cases.png](screenshots/mobile-home-light-menu-use-cases.png).

Sign in and Get started free leave the marketing host for the app wall. The branch stops there.

## Home

A yellow announcement pill, a 56px heading with a yellow highlight on one word, a grey paragraph, a yellow pill button, then a video. Below that, a chip row, steps, a logo row, and a gallery with Load more. [home-light-default.png](screenshots/home-light-default.png), [home-light-cta-hover.png](screenshots/home-light-cta-hover.png), [home-light-full.png](screenshots/home-light-full.png).

The full-page shot stops at the 8-chunk cap (20020px on desktop). The page continues past that.

## Pricing

A 57.6px heading, a three-way billing control (Monthly, Yearly, Multi-pack), then three plan cards. The middle card is outlined and labelled most popular. Plan buttons read "Start for free" and were not measured. [pricing-light-default.png](screenshots/pricing-light-default.png), [pricing-monthly-light-default.png](screenshots/pricing-monthly-light-default.png). Phone: [mobile-pricing-light-default.png](screenshots/mobile-pricing-light-default.png).

## Templates

A grey eyebrow, a large heading, two inline filters ("any site", "anyone"), a search field, a category list, and a card grid with a Free badge on some cards. Filters stay on `/templates`. Search was filled with the word portfolio and cleared. [templates-light-default.png](screenshots/templates-light-default.png), [templates-light-filter-menu.png](screenshots/templates-light-filter-menu.png), [templates-light-search-filled.png](screenshots/templates-light-search-filled.png), [templates-light-category.png](screenshots/templates-light-category.png).

## Feature and use case

Feature pages put a yellow wash behind an icon, a small label, a 57.6px heading, and an 18px grey paragraph. [feature-ai-light-default.png](screenshots/feature-ai-light-default.png). The feature index is [features-light-default.png](screenshots/features-light-default.png).

A use-case page is a heading, a yellow "Start with this website" link (signup wall), an "Open the demo" link to a `*.super.site` (not followed), and Original / Green / Blue / Mono chips that recolour the demo in place. [usecase-light-default.png](screenshots/usecase-light-default.png), [usecase-light-mono.png](screenshots/usecase-light-mono.png).

## Lists

Showcase, blog, guides, icons and themes are Notion collection pages under the same shell. One index shot each: [showcase-light-default.png](screenshots/showcase-light-default.png), [blog-light-default.png](screenshots/blog-light-default.png), [guides-light-default.png](screenshots/guides-light-default.png), [icons-light-default.png](screenshots/icons-light-default.png), [themes-light-default.png](screenshots/themes-light-default.png). Load more on the blog reveals more cards on the same URL. [blog-light-load-more.png](screenshots/blog-light-load-more.png).

## Login wall

A centred column on a light ground: mark, "Log into Super", empty email and password fields, a yellow Log in button, then Google, Apple and a passkey. Nothing was typed. Those three buttons were not clicked. [login-light-wall.png](screenshots/login-light-wall.png).

## Off-site hosts

Docs, changelog, status and the feedback board loaded and are not the marketing shell. One viewport each: [docs-light-default.png](screenshots/docs-light-default.png), [changelog-light-default.png](screenshots/changelog-light-default.png), [status-light-default.png](screenshots/status-light-default.png), [feedback-light-default.png](screenshots/feedback-light-default.png).

## Not on this surface

No form validation, empty dashboard, loading dashboard, destructive confirm, toast, or onboarding. Those sit behind the login wall. Customer sites on `*.super.site` are not Super's chrome and were not captured.
