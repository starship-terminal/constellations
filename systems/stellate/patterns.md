# Patterns

Public signed-out Stellate, 2026-11-19, CSS viewport 1169 by 731. No screenshots: preview frames failed.

## Marketing shell

https://stellate.co/ uses a header 72px tall, padding 20px 0, transparent, TT Commons. Nav links are 15px / 550, `#3b4c6a`. "Get started for free" is the gray 8px-radius button. The page colour is `#3b4c6a` on a grey page. `meta theme-color` is `#F8FAFC`. A dark band uses `#283448` with `#f8fafc` headings. The hero `h1` is 48px / 650 / 52.8px, `#283448`. Section `h2`s are 38px / 57px. The content column uses `max-w-7xl` at 1280px and `px-6`.

https://stellate.co/graphql-edge-caching stays on the same grey page when the system colour scheme is dark. Its `h1` is 64px / 550 / 76.8px.

## Pricing

https://stellate.co/pricing opens with a 48px `h1`, "Pricing that scales". Three plan cards sit in a row at this width: Free, Business (blue), Enterprise (neutral). Business is the wide card. Buttons are "Get Started", "Start free trial" and "Contact us". No card form was opened.

## Auth

https://stellate.co/login is a column on `#f8fafc`, max width about 464px for the heading. The `h1` is 40px / 450 / 60px, "Welcome back!". GitHub and GitLab buttons are 320px, then an "or" divider, then one email field and "Continue with Email". Legal copy says Stellate stores email, name and avatar.

https://stellate.co/signup matches that column. The `h1` is "Get started in minutes". The lede says it is free for developers and that no credit card is required. The email was submitted. The next page, https://stellate.co/login/submitted, says "Magic login link sent to" and prints the address in 16px uppercase at 50 percent opacity, letter-spacing wider. The magic link was not opened.

## Docs

https://stellate.co/docs is a Nextra shell, not the marketing theme. With `prefers-color-scheme: dark`, `html` is `dark`, the page is `#18181b`, and the `h1` is 40px / 700, canvas `#f1f5f9`. With light, `html` is `light`, the page is `#fafafa`, the `h1` is canvas `#0f172b`, and links are `#006be6`. The navbar is 64px (`--nextra-navbar-height`). Search is a kbd reading ⌘K. A mobile nav is in the DOM at 0 height. https://stellate.co/docs/quickstart has three `pre` blocks. https://stellate.co/docs/graphql-edge-cache/getting-started is a 404.

## Email

The magic-link message uses Gotham, page `#F1F5F8`, heading `#3B4C6A` at 24px, and a button with background `#DFE4EA`, padding 14px 17px, radius 6px. Those are declared inline styles in the message, not a live page reading.

## What was not entered

The magic link, GitHub, GitLab, a card, a phone number, and the signed-in dashboard were not opened.
