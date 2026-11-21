# Lemon Squeezy public site tree

Mapped on 2026-11-21 from https://www.lemonsqueezy.com/ in headless Chromium, signed out. Every control below was opened or its destination was read from the live DOM. The signed-in app, checkout, and identity providers were not entered.

The marketing site is a shutdown page. A yellow banner on every page says new sign-ups are closed and the product shuts down on March 31, 2027. The homepage headline is "Sell digital products globally, now on Stripe". There is no product menu, no dark-theme switch, and no cookie banner.

`robots.txt` allows every agent except `/backups/` and points at the sitemap. The sitemap lists 21 URLs. Four category URLs redirect to `/`.

## Shared chrome

Present on every `www.lemonsqueezy.com` page that was opened.

| Control | Opens |
|---|---|
| Yellow banner, "Learn more" | Page: `/blog/saying-goodbye-to-lemon-squeezy` |
| Logo, aria-label "home" | Page: `/` |
| Docs | Page: `https://docs.lemonsqueezy.com/` (docs host, same visual shell) |
| Help | Page: `/help` |
| Sign in | Login wall: `https://app.lemonsqueezy.com/login` redirects to `https://auth.lemonsqueezy.com/login`. Stop. See [login-review.json](login-review.json). |
| Start with Managed Payments (desktop) / Get started (phone) | External page: `https://dashboard.stripe.com/register/managed_payments`. Stripe account registration. Not submitted. |
| Privacy | Page: `/privacy` |
| Terms | Page: `/terms` |
| DPA | Page: `/dpa` |
| Stripe wordmark in the footer | External page: `https://stripe.com/` |

Phone width (390): Docs, Help and Sign in hide. A hamburger (`aria-label` "menu", `aria-controls` the nav overlay) opens an overlay menu with Docs, Help and Sign in. The primary button label changes from "Start with Managed Payments" to "Get started" and still opens the Stripe registration URL. Closing the menu is the same hamburger.

No consent banner appeared. Nothing was accepted.

## Homepage `/`

Title: "Payments, tax & subscriptions for software companies • Lemon Squeezy". No buttons besides the shared chrome. Category URLs `/category/growth`, `/category/hacks`, `/category/juice-bar` and `/category/lemon-drops` land here (HTTP 200, final URL `/`, same headline and same links).

| Control | Opens |
|---|---|
| Explore Managed Payments | External page: `https://stripe.com/managed-payments` |
| Learn more (already using Lemon Squeezy) | Page: `https://docs.lemonsqueezy.com/migration` |
| Learn more (Managed Payments) | External page: `https://stripe.com/managed-payments` |
| "here" in the eligibility sentence | External page: `https://docs.stripe.com/payments/managed-payments/eligibility#supported-business-locations` |
| "learn more" in the migration sentence | Page: `https://docs.lemonsqueezy.com/migration` |
| "transition" | Page: `https://docs.lemonsqueezy.com/migration#moving-to-another-provider` |
| migration planning guide | Page: `https://docs.lemonsqueezy.com/migration` |
| export your data | Page: `https://docs.lemonsqueezy.com/help/orders/exporting-orders` |
| Stripe Atlas | External page: `https://stripe.com/atlas` |
| "docs" in the body | Page: `https://docs.lemonsqueezy.com/migration` |
| Help Center | Page: `/help` |
| stripe.com/managed-payments | External page: `https://stripe.com/managed-payments` |

## Pricing `/pricing`

Headline: "Whether you're just starting out or selling like hotcakes, we've got your back". The fee card reads 5% + 50¢. The email card has a subscriber slider and an Annual discount switch.

| Control | Opens |
|---|---|
| Annual discount switch (`input[type=checkbox]`, name `checkbox`) | Interaction on the same page. Off by default. Turning it on changes the email price label to an annual figure (`$0/m` at the default 500 subscribers). Not a navigation. |
| Subscriber slider (`input[type=range]`, min 0, max 52, step 1, value 0) | Interaction on the same page. The thumb sits at "500 subscribers". Dragging it changes the subscriber count and the email price. Not dragged past the default during capture, so intermediate prices are not recorded as tokens. |
| "fees" | Page: `https://docs.lemonsqueezy.com/help/getting-started/fees` |
| Learn more (getting paid) | Page: `https://docs.lemonsqueezy.com/help/getting-started/getting-paid` |
| Learn more (merchant of record) | Page: `https://docs.lemonsqueezy.com/help/payments/merchant-of-record` |
| Learn more (currencies) | Page: `https://docs.lemonsqueezy.com/help/payments/currencies` |
| Learn more (video) | External page: `https://www.youtube.com/watch?v=Xb9hqA7uStE` |
| Learn more (email), two cards | Page: `https://docs.lemonsqueezy.com/help/email` |
| Learn more (API) | Page: `https://docs.lemonsqueezy.com/api` |
| "help center" and "Help center" (`href="#"`) | Interaction: in-page jump. The link sits inside an accordion card. A pointer click was intercepted by `.accordion_item-box-2` and the sticky nav. Destination is the same page. |
| Documentation | Page: `https://docs.lemonsqueezy.com/help` |
| API documentation | Page: `https://docs.lemonsqueezy.com/api` |
| FAQ row 01, "Can I cancel anytime?" | Interaction: accordion. The first row is open on load and shows the answer. A click on `.accordion_item` keeps it open. |
| FAQ rows 02 to 12 | Interaction: accordion, closed on load. Each row is a disclosure on the same page (plus icon). Questions: Can I sell subscriptions? How and when do I get paid? Are you the merchant of record? Can I sell in other countries? What if I already have a website? What can I sell with Lemon Squeezy? Can I send emails? How does my email plan work? Do you have an API or developer resources? Can you help if I get stuck? Could fees ever exceed 5% + 50¢ per transaction? |

## About `/about`

| Control | Opens |
|---|---|
| 01 Our mission (`href="#"`) | Interaction: in-page scroll. Click moved the page down the mission section. URL stays `/about`. |
| 02 Our values (`href="#"`) | Interaction: same pattern, in-page jump to the values section. |
| 03 Our goals (`href="#"`) | Interaction: same pattern, in-page jump to the goals section. |
| @jrfarr | External page: `https://twitter.com/jrfarr` |
| @gilbitron | External page: `https://twitter.com/gilbitron` |
| @ormanclark | External page: `https://twitter.com/ormanclark` |
| Help center | Page: `/help` |
| Documentation | Page: `https://docs.lemonsqueezy.com/help` |
| API documentation | Page: `https://docs.lemonsqueezy.com/api` |

## Help `/help`

| Control | Opens |
|---|---|
| View the docs | Page: `https://docs.lemonsqueezy.com/help` |
| View API reference | Page: `https://docs.lemonsqueezy.com/api` |
| View Guides | Page: `https://docs.lemonsqueezy.com/guides` |
| Message us (`href="#"`) | Overlay: "Contact support" dialog on the same page. Fields: Name, Email (required), Additional details. Buttons: close (x), Cancel, Submit. The form was not filled and not submitted. Cancel and the close control dismiss it. |

## Creators guide `/creators-guide`

| Control | Opens |
|---|---|
| Download now for free | Checkout overlay URL: `https://makelemonade.lemonsqueezy.com/checkout/buy/0929c351-abb3-49f7-a671-ba15406517dd?embed=1`. Not opened. A checkout is an account and payment branch. Stop. |
| Download free guide | Same checkout URL. Not opened. |

## Legal and buyer pages

These pages add no controls beyond the shared chrome and the in-body links below.

| Page | Extra control | Opens |
|---|---|---|
| `/privacy` | none | Shared chrome only |
| `/terms` | none | Shared chrome only |
| `/affiliate-terms` | none | Shared chrome only |
| `/dpa` | privacy policy | Page: `/privacy` |
| `/dpa` | service agreement | Page: `/terms` |
| `/dmca` | website | External page: `https://www.copyright.gov/` |
| `/buyer-terms` | here | Page: `/privacy` |
| `/anti-spam-policy` | terms and conditions | External archive page: a 2022 Wayback copy of the terms. Not followed as a live product page. |
| `/why-did-lemon-squeeezy-charge-me` | my orders | Login wall: `https://app.lemonsqueezy.com/my-orders` redirects to `https://app.lemonsqueezy.com/my-orders/login`. Stop. See login-review. |
| `/why-did-lemon-squeeezy-charge-me` | Contact us | Page: `/help` |
| `/why-did-lemon-squeeezy-charge-me` | Learn more (merchant of record) | Page: `https://docs.lemonsqueezy.com/help/payments/merchant-of-record` |
| `/why-did-lemon-squeeezy-charge-me` | Learn more (home) | Page: `/` |
| `/why-did-lemon-squeeezy-charge-me` | Learn more (sales tax) | Page: `https://docs.lemonsqueezy.com/help/payments/sales-tax-vat` |

## Blog posts

Four posts are in the sitemap. Each has the shared chrome plus a share widget (Webflow dropdown, `aria-expanded` false) that reveals LinkedIn, Twitter and Facebook icon links. The icons are external share URLs. They were not followed.

| Post | Extra control | Opens |
|---|---|---|
| `/blog/saying-goodbye-to-lemon-squeezy` | Managed Payments | External page: Stripe docs for Managed Payments |
| `/blog/2026-update` | our last real update | Page: `/blog/stripe-lemon-squeezy-update-2025` |
| `/blog/2026-update` | new merchant of record product, Stripe Managed Payments | External page: Stripe docs for Managed Payments |
| `/blog/2026-update` | Stripe acquired Lemon Squeezy | Page: `/blog/stripe-acquires-lemon-squeezy` |
| `/blog/2026-update` | here (sign-up anchor) | External page: Stripe Managed Payments sign-up anchor. Not submitted. |
| `/blog/2026-update` | support merchants in 35+ countries | External page: Stripe docs, supported locations |
| `/blog/2026-update` | check out Atlas | External page: `https://stripe.com/atlas` |
| `/blog/2026-update` | migration settings | Login wall: `https://app.lemonsqueezy.com/settings/migration`. Not opened. Account settings. Stop. |
| `/blog/stripe-acquires-lemon-squeezy` | @stripe, @lmsqueezy | External pages: `https://twitter.com/stripe`, `https://twitter.com/lmsqueezy` |
| `/blog/stripe-lemon-squeezy-update-2025` | last year | Page: `/blog/stripe-acquires-lemon-squeezy` |
| `/blog/stripe-lemon-squeezy-update-2025` | official Stripe roundup | External page: `https://stripe.com/blog/top-product-updates-sessions-2025` |
| `/blog/stripe-lemon-squeezy-update-2025` | Stripe Managed Payments waitlist | External page: Stripe docs for Managed Payments |

## Docs host `https://docs.lemonsqueezy.com/`

Reached from the Docs nav item. Same banner and nav as the marketing site. Title: "Docs & Guides • Lemon Squeezy".

| Control | Opens |
|---|---|
| Logo | Page: `https://lemonsqueezy.com` |
| Docs (in the docs nav) | Page: `/` on the docs host |
| Documentation | Page: `/` on the docs host |
| Migration | Page: `/migration` |
| Docs (card) | Page: `/help` |
| API Reference | Page: `/api` |
| Guides | Page: `/guides` |
| LEMSQZY* Charge | Page: `https://www.lemonsqueezy.com/why-did-lemon-squeeezy-charge-me` |
| Open search | Interaction: search dialog on the docs host. A query was not typed. |
| Sidebar groups | Pages under `/help`, `/api` and `/guides` (Getting Started, Products, Payments, and the rest of the published docs tree). The sidebar is a page index, not an app. |

## Stopped branches

| Control | Why it stopped |
|---|---|
| Sign in, Sign up, Forgot your password, Customer Dashboard, My Orders, migration settings | Login, signup, password reset, or account page. Photographed only. No fields filled. No identity provider clicked. |
| Download now for free, Download free guide | Checkout URL. Not opened. |
| Start with Managed Payments, Get started, Stripe sign-up anchors | Stripe registration. Not submitted. |
| Google, Twitter | Identity providers. Not clicked. |
