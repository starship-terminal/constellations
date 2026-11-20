# Zellerfeld patterns

Public storefront only, captured 2026-11-21. The map of which control opens
which page is [site-tree.md](site-tree.md).

## Shell

A black bar. Left: a grid icon that opens the navigation drawer. Center: the
wordmark, a home mark, and a search field. Right: Create (ember outline) and
Sign in. On a phone the same jobs move to a bottom bar: Home, and a Menu
button that opens a full-screen drawer with search at the top.

![Home](screenshots/home-light-default.png)

![Phone home](screenshots/mobile-home-light-default.png)

## Navigation

The drawer is a left sheet on desktop and a full screen on the phone. Shoes
are Sneakers, Boots, Slides and Barefoot. Explore holds creator cards.

![Desktop nav](screenshots/home-light-nav.png)

![Phone nav](screenshots/mobile-home-light-nav.png)

## Search

Typing in the field (not submitted as a form) opens suggestions, a creator
hit and a product grid on the same page. `/search?q=` is a 404.

![Search](screenshots/home-light-search.png)

## Catalogue

A collection is a heading plus three sort chips (Trending, All time, New in)
and a product grid. Cards carry a sold-out badge, a name, a creator and a price.

![Sneakers](screenshots/sneakers-light-default.png)

![Sneakers, New in](screenshots/sneakers-light-new-in.png)

## Product

Gallery thumbs, colour links, a creator link, a reviews link, a wishlist
heart and Buy now. Wishlist opens the sign-in dialog and stops. Buy now
opens a Fit Profile dialog (usual size, then Proceed to payment). That
dialog is a profile step. It was opened and closed. No size was chosen and
payment was not started.

![Product](screenshots/product-light-default.png)

![Fit dialog](screenshots/product-light-fit-dialog.png)

## Content

FAQ questions are disclosures. Reviews are a public wall with Load more.
Careers, the open letter, shipping, privacy, terms and privacy choices are
long text pages. The newsletter page has an email field that was not filled
and not submitted. A missing path renders "Hey, this is 404."

![FAQ open](screenshots/faq-light-open.png)

![404](screenshots/notfound-light-default.png)

## Onboarding and sign-in (walls)

Start onboarding opens a welcome step with Let's go. Further steps ask for
a profile. Stopped on the welcome. Sign in is a Clerk dialog: Continue with
Google, email, phone, password, passkey, sign up. Not entered. Continue
with Google was not clicked.

![Onboarding welcome](screenshots/onboarding-light-default.png)

![Sign-in dialog](screenshots/home-light-signin.png)

## Studio and help

Create opens the public Studio landing (guest, not logged in). Log in on
that host is a wall. The help center is a public Zendesk home. Its sign-in
and request form were not used.

![Studio](screenshots/studio-light-default.png)

## Empty, loading, error, confirmation

The styled 404 is the error page. Sold-out badges are the empty-purchase
state on a product card. No toast, no destructive confirmation, and no
validation error: no form was submitted. Loading was not held.
