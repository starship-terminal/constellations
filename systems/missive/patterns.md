# Patterns

How the public Missive pages are built. Screenshots are in [screenshots/](screenshots).

## Marketing frame

[home-light-default](screenshots/home-light-default.png) is the signed-out home at 1440. A white navbar, 61px tall, holds the wordmark, Product, Pricing, Customers, Resources, Log in, Book a demo, and a filled Try for free. The page ground is white. The hero is Tiempos Headline at 56px, "Inbox collaboration for teams that run on email", with Inter body at 20px in neutral 500. Under that sit Try for free and Watch demo, then a product screenshot that is a public demo, not a signed-in inbox.

The phone home is [mobile-home-light-default](screenshots/mobile-home-light-default.png) at 390. The wordmark, Log in, Sign up and a menu icon replace the desktop nav. The privacy sheet ("Your Privacy Choices", I understand) was hidden and never clicked.

## Pricing

[pricing-light-default](screenshots/pricing-light-default.png). "Pay-for-what-you-use pricing". A yearly switch sits above three columns: Starter $14, Productive $24, Business $36, each per user per month, billed yearly. A 20% off chip sits beside the switch. Try for free and Talk to sales sit under the cards. Neither was clicked. No card number was entered.

## Features, customers, download, security, blog

[features-light-default](screenshots/features-light-default.png) is a category chip row (Collaboration, Email and Communication, Tasks, Automations, Security, AI, Integrations) over feature cards. [customers-light-default](screenshots/customers-light-default.png) is a story grid. [download-light-default](screenshots/download-light-default.png) lists macOS, Windows, Web app, iOS and iPadOS, and Android. No store link was followed. [security-light-default](screenshots/security-light-default.png) is a prose page. It publishes security@missiveapp.com as the product's own address. [blog-light-default](screenshots/blog-light-default.png) is a category list and article cards. No article was opened.

## Auth

[login-light-default](screenshots/login-light-default.png) is mail.missiveapp.com/#login. A white form column on the left, a quote and a product demo on the right. Continue with Google, Continue with Apple, and Single sign-on are outline buttons. Work email and Password sit under an OR rule. Log in is filled brand blue. Create an account links to signup. Nothing was submitted.

[login-dark-default](screenshots/login-dark-default.png) is the same screen after `data-theme="dark"` on the document. The page goes to rgb(29, 30, 31). The brand fill stays #2266ed. Marketing pages have no dark theme.

[signup-light-default](screenshots/signup-light-default.png) adds an agreement checkbox and a Sign up button that stays disabled until the fields are filled. The form was not filled. [signup-dark-default](screenshots/signup-dark-default.png) shows a Cloudflare "Verify you are human" widget on the dark signup. It was not checked.

[sso-light-default](screenshots/sso-light-default.png) asks for an organization login keyword. It was not submitted.

The phone login is [mobile-login-light-default](screenshots/mobile-login-light-default.png). The quote column drops away. The form is the whole width.

## What the product demo shows

The inbox paintings on the marketing pages and on the auth quote column are published demos. Names in them (Sarah Johnson, Rafael, Orphelia) are the product's sample content. They are not a signed-in workspace.
