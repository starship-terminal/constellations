# RevenueCat patterns

How the public pages combine the components. All captures are signed out, 2026-11-21. Desktop is 1440×900 at 1x. Phone is 390×844 at 2x (PNG width 780).

## Marketing shell

A 64px white header. Wordmark at the left, four menu buttons, Pricing, then Log in, an outline Contact sales pill, and a blue Sign up pill. Menus open over the page without a recorded scrim. Footer repeats the same destinations plus legal links.

[home-light-default](screenshots/home-light-default.png), [home-light-menu-solutions](screenshots/home-light-menu-solutions.png).

Phone replaces the bar with a wordmark, an Eng control, and a Menu button. The sheet pins Sign up, Contact sales and Log in to the bottom. [mobile-home-light-default](screenshots/mobile-home-light-default.png), [mobile-home-light-menu-open](screenshots/mobile-home-light-menu-open.png).

## Home

Left headline in Object Sans 60/500, a pill email field with a blue Start for free button inside it, three stat columns, and a product illustration on the right. The email field was not filled. The illustration is a public demo of the dashboard, not the signed-in app.

[home-light-default](screenshots/home-light-default.png), full page [home-light-full](screenshots/home-light-full.png).

## Pricing

One plan card ("Start for free", then 1% after $2,500 MTR) beside an "Everything's included" panel, then an enterprise strip. In-page text tabs switch Growth Tools, All features, Testimonials and FAQs.

[pricing-light-default](screenshots/pricing-light-default.png), [pricing-light-tab-faqs](screenshots/pricing-light-tab-faqs.png), phone [mobile-pricing-light-default](screenshots/mobile-pricing-light-default.png).

## Feature and audience pages

Same shell, a long marketing column, and a blue pill CTA that leaves for signup. Representatives: [paywalls-light-default](screenshots/paywalls-light-default.png), [for-developers-light-default](screenshots/for-developers-light-default.png), [why-revenuecat-light-default](screenshots/why-revenuecat-light-default.png).

## Stories and integrations

Index pages of cards. [testimonials-light-default](screenshots/testimonials-light-default.png), [integrations-light-default](screenshots/integrations-light-default.png), one story [customer-openai-light-default](screenshots/customer-openai-light-default.png), one integration [integrations-stripe-light-default](screenshots/integrations-stripe-light-default.png).

## Sales form

A public page with empty fields and a discussion select. Nothing was typed or submitted. [talk-to-sales-light-default](screenshots/talk-to-sales-light-default.png), phone [mobile-talk-to-sales-light-default](screenshots/mobile-talk-to-sales-light-default.png). Contact is the same pattern: [contact-light-default](screenshots/contact-light-default.png).

## Docs

A separate shell: top nav, search field, SDK cards, and a theme toggle. Search opens a dialog. Dark is a docs theme only.

[docs-light-default](screenshots/docs-light-default.png), [docs-light-search-open](screenshots/docs-light-search-open.png), [docs-light-dark](screenshots/docs-light-dark.png), sidebar [docs-overview-light-sidebar-open](screenshots/docs-overview-light-sidebar-open.png), phone [mobile-docs-light-default](screenshots/mobile-docs-light-default.png).

## Filters

Changelog chips and glossary letters filter the public index locally. [changelog-light-filter-sdk](screenshots/changelog-light-filter-sdk.png), [glossary-light-letter-p](screenshots/glossary-light-letter-p.png). Blog search did not open: the SEARCH button was not found, so that state is not captured. The newsletter field on the blog was left empty.

## Walls

Login and signup are the end of those branches. [login-wall-light-default](screenshots/login-wall-light-default.png), [signup-wall-light-default](screenshots/signup-wall-light-default.png). The signed-in dashboard was not captured.

## Not on the public surface

Empty, loading and error states, a destructive confirmation, feedback after an action, and onboarding all sit behind the login wall or never appeared. Status is a public board with a subscribe form that was not used: [status-light-default](screenshots/status-light-default.png).
