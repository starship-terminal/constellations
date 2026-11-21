# Patterns

Public signed-out Slab. Computed styles at 1169 by 731, devicePixelRatio 2. Marketing screenshots at 1440 and 390.

## Marketing home

https://slab.com/ uses a plum nav and hero, `#42022e`, with white text. The nav is 132px tall at this width and lists Product, Resources, Library, Pricing and Log In. The hero headline is Sentinel 42px / 52px, letter-spacing -0.75px: "Build a culture of knowledge-sharing today." Under it, a Google button, an "or" rule, a Work Email field and a coral Get Started button. A product illustration sits on the right. [screenshots/home-light-default.png](screenshots/home-light-default.png).

At 390 the same hero stacks, the nav collapses to a Menu button, and the Google button goes full width. [screenshots/home-light-mobile.png](screenshots/home-light-mobile.png). Computed styles were not re-read at 390.

## Pricing

https://slab.com/pricing/ switches the nav to white with slate text. The h1 is Sentinel 56px / 300, colour `#2f4050`: "Plans that scale with your team." A billing pill selects Annually. Four columns: Free (`#2f4050` button), Startup (`#fcb415`), Business (`#50c5dc`), Enterprise (plum column, maroon Contact Sales). The page says no credit card is required. No checkout was opened. [screenshots/pricing-light-default.png](screenshots/pricing-light-default.png).

## Login

https://slab.com/login/ is a signed-out account card on `#fcf9f8`. The card is white, 430px wide, padding 48px, radius 4px. Heading "Welcome back!" is Untitled Sans 25px / 500. The form asks for a subdomain, then Continue (`#7e0048`). A link offers "Sign up for Slab". The subdomain was empty. Continue was not clicked. [screenshots/login-wall-desktop.png](screenshots/login-wall-desktop.png) and [screenshots/login-wall-phone.png](screenshots/login-wall-phone.png).

## Register

https://slab.com/register/ uses the same account page colour. It asks for email, full name and password, plus "Sign up with Google" and "Create my account". That is not an email-only form, so it was not filled. Google was not clicked. [screenshots/signup-wall-desktop.png](screenshots/signup-wall-desktop.png) and [screenshots/signup-wall-phone.png](screenshots/signup-wall-phone.png).

## Public pages, 2026-11-22

Header and footer destinations are listed in [site-tree.md](site-tree.md). Each photographed page is a viewport shot in [screenshots/](screenshots/), named `public-<page>-desktop.png`. Home, pricing, and library also have phone shots. Plan buttons, Contact Sales, Contact Support, and download buttons were not clicked.

## Help center

https://help.slab.com/en/ is a separate help shell: system-ui, page `#ffffff`, text `#1a1a1a`. It was opened and not treated as the marketing system.

## Not captured

Signed-in wiki, company SSO, payment, phone and KYC. Hover, menu and dialog states. A 390 computed-style pass.
