# Jace AI patterns

How the public surfaces combine, read on 2026-11-18, signed out. Marketing pages are a light cream site. The product theme shows up on the sign-in card and the signup funnel.

## Marketing shell

A sticky header holds the wordmark, a white Log In pill, and a dark Get started pill. The page ground is sand (`#fffefd`). Body type is Geist Sans at `#2d2d2d`. Display type is Gelica, light weight, large on the home hero (88px / 300 on desktop). Pills use a 9999px radius. The header search-like chip is a white 9999px field with a `#d1d5dc` border.

See [home-light-default](screenshots/home-light-default.png) and [header-default](components/crops/header-default.png).

At 390 the same bar keeps Log In and Get started. There is no hamburger and no overlay menu.

See [mobile-home-light-default](screenshots/mobile-home-light-default.png).

## Home

The hero is a Gelica headline, a dark Get started pill, and a row of demo chips. Below that, integration pills (Gmail, Outlook) and feature cards sit on the cream ground. The inbox in the hero is a public demo image, not the signed-in product.

See [home-light-full](screenshots/home-light-full.png) and [hero-cta-default](components/crops/hero-cta-default.png).

## Pricing

A title, a yearly/monthly toggle (both states measured at rest), plan cards, a primary plan CTA and a secondary CTA, then an FAQ accordion. Opening one FAQ row is a public toggle, not a submission.

See [pricing-light-default](screenshots/pricing-light-default.png), [pricing-light-faq-open](screenshots/pricing-light-faq-open.png) and [price-card-default](components/crops/price-card-default.png).

Get Started for Free, Try Pro and Start your free trial leave for `app.jace.ai/signup`. Those links were measured and not followed.

## Blog, docs, brand, legal

Blog is a title, a nav row and cards. Docs is a title plus a sidebar of links, starting at `/docs/guides-getting-started`. Brand, about, changelog, press, lawyers, terms and privacy are long editorial pages captured as screenshots. `/features` returns the site's own 404.

See [blog-light-default](screenshots/blog-light-default.png), [docs-light-default](screenshots/docs-light-default.png), [brand-light-full](screenshots/brand-light-full.png) and [notfound-light-default](screenshots/notfound-light-default.png).

The sitemap lists 134 URLs (more blog posts, docs, persona pages, Slack and Outlook integrations, templates). Those were not shot one by one.

## Sales form (boundary)

`/contact/sales` shows a title, text fields, three selects and a Send a request button. The page ships with sample placeholders in the name and email fields. The committed screenshot clears those placeholders so the form reads empty. Nothing was submitted, so a posted error was not captured. The message control is a select, not a textarea.

See [contact-light-default](screenshots/contact-light-default.png) and [text-field-focused](components/crops/text-field-focused.png).

## Sign-in (boundary)

`app.jace.ai/signin` is the dark product surface: `#333437` ground, `#fff2e7` body text, Inter Variable in the product tokens. The card offers Continue with Google, Continue with Outlook, Launch the SSO portal, and Sign up. There is no email field on this page. Buttons were hovered and focus-tested. Pressed states were forced in DevTools. No OAuth or SSO flow was followed.

See [signin-light-default](screenshots/signin-light-default.png) and [signin-oauth-default](components/crops/signin-oauth-default.png).

The filename says light because the capture route names the marketing theme. The paint is the product dark theme (bare `:root`). The product light theme (`html.light`) is declared and measured from the stylesheet. It is not what this page paints.

## Signup (boundary)

`app.jace.ai/signup` is the same dark product paint. Three screens, in order:

1. Landing: a review carousel, "Join +10,000 people using Jace in their everyday work", a gradient Continue pill. See [signup-light-default](screenshots/signup-light-default.png) and [signup-continue-default](components/crops/signup-continue-default.png).
2. Privacy: "Your privacy matters", two copy blocks, a gradient Continue to signup pill. This is a product notice, not a cookie banner. See [signup-light-privacy](screenshots/signup-light-privacy.png).
3. OAuth card: "Sign up with your work email", Continue with Google, Continue with Outlook. There is no email field and no password field. Google and Outlook were measured, never pressed. See [signup-light-oauth](screenshots/signup-light-oauth.png).

Phone 390 keeps the same three screens. See [mobile-signup-light-oauth](screenshots/mobile-signup-light-oauth.png).

The inbox, drafts, labels, Flows and settings sit behind those OAuth buttons and were not reached.

## What is not on the public surface

Checkbox, radio, switch, select, toast, dialog, tooltip and table do not mount signed out. Empty, loading and error states of the inbox, destructive confirmation, search, settings and checkout sit behind sign-in. Reduced motion is ignored on the marketing home and pricing pages (62 and 41 moving elements kept). The sign-in page is partial (6 of 9 moving elements removed).
