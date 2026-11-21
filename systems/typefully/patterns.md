# Typefully patterns

How the public pages combine. Screenshots are quantised sRGB PNGs. Read colours from [tokens.json](tokens.json), not from the PNGs.

## Marketing page

A quiet white page, Inter, black headlines, muted secondary copy, and one blue accent. The header sits on the page, not in a bar with a border. The CTA is a short pill. Plan cards and tool cards use a hairline and a small radius, not a heavy shadow.

Shown in [screenshots/pricing-light-default.png](screenshots/pricing-light-default.png) and [screenshots/ai-light-default.png](screenshots/ai-light-default.png).

## Homepage modal

`/` is a long marketing page drawn inside a dialog over a product-shell illustration. The shell looks like the app (Write, Plan, Analyze, queue) and does not receive clicks. Log in and Sign up open a second dialog on the same URL.

Shown in [screenshots/home-light-default.png](screenshots/home-light-default.png) and [screenshots/home-light-login-dialog.png](screenshots/home-light-login-dialog.png).

## Auth wall

Every "Get started", "Try Typefully now", and "Create profile" control returns to that wall. The dialog offers four providers and a switch between log in and sign up. Email reveals a field and a Turnstile widget. That branch stops there.

## Pricing

Three plans in a row: Free, Creator, Business. Copy says annual billing. There is no monthly toggle. A social-set control opens a menu. Feature rows expand in place. On a phone the comparison uses plan tabs.

Shown in [screenshots/pricing-light-full.png](screenshots/pricing-light-full.png) and [screenshots/mobile-pricing-light-default.png](screenshots/mobile-pricing-light-default.png).

## Editorial index

Blog, changelog, announcements, and the glossary share a list of titles on the same white page, with the same header and footer. One sample of each template was captured. The sitemap has many more slugs of the same template.

Shown in [screenshots/blog-light-default.png](screenshots/blog-light-default.png) and [screenshots/changelog-light-default.png](screenshots/changelog-light-default.png).

## Tool page

The fake-tweet composer is a local form: name, handle, textarea, advanced options. It was not submitted. The glossary search was focused and not submitted.

Shown in [screenshots/fake-tweet-light-default.png](screenshots/fake-tweet-light-default.png) and [screenshots/glossary-light-search-focused.png](screenshots/glossary-light-search-focused.png).

## Docs

`/docs/api` is a Scalar reference: a left rail of groups, method rows, and a client panel. It is a different chrome from the marketing pages. The token field stays empty.

Shown in [screenshots/docs-light-default.png](screenshots/docs-light-default.png).

## Phone

390px CSS width, captured at 2x. Marketing pages keep the logo and the pill CTA. On jobs, a menu icon appears. Pricing, Blog, Changelog, Jobs, and Help stay in the footer when they leave the top bar. The jobs phone menu was not opened.

Shown in [screenshots/mobile-home-light-default.png](screenshots/mobile-home-light-default.png) and [screenshots/mobile-jobs-light-default.png](screenshots/mobile-jobs-light-default.png).
