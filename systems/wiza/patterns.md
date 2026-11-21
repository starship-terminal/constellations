# Wiza patterns

How the public pages combine the measured components. Screenshots from the 2026-11-21 refresh are in [screenshots/](screenshots/). The site tree is [site-tree.md](site-tree.md).

## Marketing shell

The home, pricing, enterprise, customers, privacy, and 404 pages share one Webflow nav. Logo, Solutions, Resources, Enterprise, Pricing, then white "Log in" and "Sign up" buttons. The bar is a white pill. Solutions and Resources open hover panels ([solutions](screenshots/home-light-solutions-menu.png), [resources](screenshots/home-light-resources-menu.png)). At 390px the links collapse to a menu button that opens a full-screen drawer ([shot](screenshots/mobile-home-light-menu.png)). Page backgrounds are transparent over a lavender hero gradient.

The footer is the same on those pages: "The future of prospecting", `hello@wiza.co`, and link columns in `#312749` / muted `#615e6e`.

## Home

A Britti Sans h1 at 64px / 64px, weight 500, on a purple animated heading (`#231645` plus a purple radial gradient). The h1's own computed color is transparent because the colour is painted by the animation wrap. Body copy is 16px Inter. Two buttons sit under it: filled "Get started for free" and white "Get a demo". Get started opens the signup wall. Get a demo opens a form that was not submitted. The home shot is [home-light-default](screenshots/home-light-default.png). The footer is [home-light-footer](screenshots/home-light-footer.png).

Below that, a video frame at 28px radius, then rounded section bands (56px) with gradient fills, problem cards, and a work-email field near the bottom. The field is not a signup form by itself. It was not filled.

## Pricing

Eyebrow "Transparent pricing", h1 "Individual Plans" at the h2 step (56px). A pill toggle defaults to "Bill annually" with an "Unlimited" tag. On the 2026-11-21 annual load the cards were Free `$0`, Starter, Email `$83` per month (billed `$990` per year), and Email + Phone `$166` (billed `$1,990` per year). Monthly was opened and repainted Free `$0`, Starter `$49`, Email `$99`, Email + Phone `$199` ([monthly](screenshots/pricing-light-monthly.png)). Get started was not followed. Checkout was not opened. The annual page is [pricing-light-default](screenshots/pricing-light-default.png). Phone pricing is [mobile-pricing-light-default](screenshots/mobile-pricing-light-default.png).

## Enterprise

A dark hero. The h1 is white, 64px Britti Sans, "Empower your team with world-class contact data." The nav "Log in" and "Sign up" buttons on this page are filled `#7e43ff` with white text, unlike the white buttons on the home nav. "Get started" and "Explore options" were not followed. No form was on the page.

## Customers

A story grid. Tiles are `#f6f8fa`, 8px radius. "Read story" was not followed, so story detail pages are a gap.

## Privacy and 404

Privacy is long prose: h1 at 56px, body 16px / 24px Inter in `#26114a`, links `#7e43ff` underlined. The page is about 16591px tall. The 404 says "404" at 56px Britti Sans and "This page could not be found." with "Return home".

## Blog

`/blog/` is a separate WordPress theme (`wizapress`). Body font is Work Sans, not Britti Sans or the marketing Inter. The Blog Home chip is `#ffacac`. WordPress preset colours are present and are not the marketing swatches. Treat the blog as a different surface.

## Login

`/auth/login` is the product app, not the marketing site. Inter var, a white card, one empty email field, a purple "Log in" button (`#7e43ff`, 6px radius, 32px tall), "Log in via Google", and a "Get started" link. Nothing was typed or submitted. Google was not clicked. The empty wall is [login-light-default](screenshots/login-light-default.png). Signup is the same card with "Get started for free." and an empty work-email field ([signup-light-default](screenshots/signup-light-default.png)). `login-extracted` stays not-started.

## Gaps

- No full-page screenshots.
- Phone menu not opened. Only the closed 390px home was measured.
- Monthly pricing state not opened.
- Story detail, blog post, book-a-demo, and contact-sales pages not opened.
- No loading, empty, or error state of a form. The 404 is the only error page.
