# Zellerfeld site tree

Mapped on 2026-11-21 from the public homepage at `https://www.zellerfeld.com/`
in headed Chrome (Playwright, `channel: chrome`). curl alone is stopped by a
Vercel Security Checkpoint; the headed browser loads the storefront. This file
was written before screenshots. A control that opens a login or signup wall
is recorded here and that branch stops. No form is submitted. Cookie Accept
and Decline are not clicked. Continue with Google is not clicked.

One light theme. `color-scheme` is `normal`. No theme switch was found.

## Shell (every storefront page)

| Control | Opens |
|---|---|
| Wordmark "Zellerfeld" / "Home" | `/` |
| Grid button `aria-label="Open navigation"` | Left drawer (Radix dialog, max 528px on desktop). Close with `aria-label="Close navigation"` or Escape. |
| Search combobox, placeholder "What are you looking for?" | Search overlay on the current page. Typing a query (not submitted as a form) opens suggestions, collection links, a creator link and product results. `/search?q=` is a styled 404. |
| "CREATE" | `https://studio.zellerfeld.com/` (public studio landing: sidebar Home, Products, Orders, Sales & Analytics, Payments, guest "NOT LOGGED IN", file drop). "LOG IN" is a wall; stop. `/dashboard` is the same wall. |
| "SIGN IN" | Clerk dialog on the same page: "Welcome back! Please sign in to continue", Continue with Google, email, Use phone, password, Continue, Use passkey, Sign up. Stop. Do not click Continue with Google. |
| Cookie banner (Accept all, Decline, Cookie settings) | Banner only. Cookie settings is a preferences dialog. Not submitted. Hidden for later shots, never accepted or declined. |
| "Notice: Perfect Fit Guarantee" (pages after the first) | Dialog with Close and "Continue shopping". Close only; it does not submit. |

## Navigation drawer

| Control | Opens |
|---|---|
| Search field inside the drawer | Same search overlay. |
| Sneakers | `/collections/sneakers` |
| Boots | `/collections/boots` |
| Slides | `/collections/slides` |
| Barefoot | `/collections/barefoot` |
| Top creators | `/creators` |
| Stria Sport (preview card) | `/products/surge` |
| Heron Preston | `/creators/heron-preston` |
| All sneakers | `/collections/sneakers` |
| Product cards in the drawer | That product's `/products/<handle>` |

## Homepage sections

| Control | Opens |
|---|---|
| Hero product cards (Zama Zama Ninjaz, PDF Bol Sneaker, Top Toe Mule, Question 96/26) | `/products/<handle>` |
| "Start onboarding" | `/onboarding` (public first step: "Welcome to Zellerfeld", Go back, Let's go). Further steps ask for profile and preferences. Stop. Do not fill. |
| "Today's top shoes" / "Selected for you" / "All time favourites" | In-page rails. Cards go to `/products/<handle>`. |
| "All top sneakers" / "All top boots" / "All top slides" | `/collections/sneakers`, `/collections/boots`, `/collections/slides` |
| Creator names under cards | `/creators/<handle>` |
| "Top 30" | `/creators` |
| "Play short: …" | In-page short video. Public demo, not a signed-in surface. |
| "Read more customer reviews" | `/pages/customer-reviews` |
| Slider previous / next | Moves the hero or a rail. No new page. |

## Collection (`/collections/<handle>`)

Sort chips stay on the page: Trending, All time, New in. Product cards go to
`/products/<handle>`. Search suggestions also name `/collections/nike` and
`/collections/nike-us`.

## Product (`/products/<handle>`)

| Control | Opens |
|---|---|
| Return | Previous page. |
| Show image 1–n | Gallery index on the same page. |
| Colour names (Black, Oat, Lilac, Stone) | Sibling product URLs. |
| Creator name | `/creators/<handle>` |
| "Click to read our reviews" | `/pages/customer-reviews` |
| "Add to wishlist" | Same Clerk sign-in dialog. Stop. |
| "Buy now" | Fit Profile dialog: usual size (US-M, US-W, UK, EU) and "Proceed to payment". Size list is a profile field. Stop. Do not pick a size or proceed. |
| Show more | Expands the description on the page. |
| Related product cards | `/products/<handle>` |
| Previous / next slide | Related rail. |

## Creators

| Control | Opens |
|---|---|
| `/creators` cards | `/creators/<handle>` |
| Previous / next | Creator rail. |
| Creator page "Top creators" | `/creators` |
| Creator page Show more | Expands the bio. |
| Creator page Trending / All time / New in | Sorts that creator's products on the page. |

## Content pages (footer)

| Control | Opens |
|---|---|
| Careers | `/pages/careers`. "All job openings" goes to `https://ats.rippling.com/zellerfeld/jobs` (external). |
| Open letter | `/pages/why-zellerfeld` |
| Gift cards | `/collections/gift-cards` |
| Customer reviews | `/pages/customer-reviews`. "Load more" appends public reviews. |
| Privacy policy | `/policies/privacy-policy` |
| Privacy choices | `/pages/data-sharing-opt-out` |
| Affiliate | `https://zellerfeld.refr.cc/join/zellerfriends` (external join). Stop. |
| Help center | `https://help.zellerfeld.com/hc/en-us` (public Zendesk). Sign in and Submit a request are walls or forms. Stop those branches. |
| Contact | `https://help.zellerfeld.com/hc/en-us/requests/new` (request form). Do not fill. |
| Newsletter | `/pages/newsletter` (email field and submit). Do not fill or submit. |
| Shipping | `/policies/shipping-policy` |
| FAQ | `/pages/faq`. Each question is a `<summary>` accordion. |
| Scan your feet | `/pages/how-to-scan-your-feet`. Links to `/fit-profiles` and `/pages/have-you-ever`. |
| Have you ever | `/pages/have-you-ever` (public explainer). |
| See your order / My orders | `https://account.zellerfeld.com/orders`, which redirects to `/sign-in?redirect_url=…`. Stop. |
| Become a creator / Start with Studio | `https://studio.zellerfeld.com/dashboard`. Login wall. Stop. |
| Terms of service | `/policies/terms-of-service` |
| Footer privacy link `/privacy-policy` | Styled 404: "Hey, this is 404." with Homepage and My orders. |
| Instagram, Discord, LinkedIn, X | External social. Not captured as product UI. |

## Auth and profile walls (recorded, not entered)

| URL or control | What it is |
|---|---|
| Sign in button, wishlist, account | Clerk dialog, then `/sign-in` and `/sign-up` virtual routes. Continue with Google, phone, password, passkey, signup. Stop. |
| `/fit-profiles` | Redirects to `/sign-in?redirect_url=https://www.zellerfeld.com/fit-profiles`. Stop. |
| `/onboarding` after Let's go | Profile and preference fields. Stop. |
| `/cart` | Redirects to `/`. No public cart page. Buy now opens the fit dialog, not a cart. |
| Cookie Accept / Decline | Consent actions. Not clicked. Banner hidden in CSS for shots. |

## Not present on the public surface

Dark theme, cart drawer, toast, data table, switch, radio group, checkbox
group, tooltip, destructive confirmation, signed-in account, checkout.
