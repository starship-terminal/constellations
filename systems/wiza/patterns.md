# Wiza patterns

How the public pages combine the measured components. Screenshots were not saved because the preview browser did not produce frames.

## Marketing shell

The home, pricing, enterprise, customers, privacy, and 404 pages share one Webflow nav. Logo, Solutions, Resources, Enterprise, Pricing, then white "Log in" and "Sign up" buttons. At 390px the links collapse to a 40 by 37 menu button. The nav itself is transparent. Page backgrounds are transparent over a lavender hero gradient (`radial-gradient` plus `linear-gradient(rgb(239, 239, 255), ...)`).

The footer is the same on those pages: "The future of prospecting", `hello@wiza.co`, and link columns in `#312749` / muted `#615e6e`.

## Home

A Britti Sans h1 at 64px / 64px, weight 500, on a purple animated heading (`#231645` plus a purple radial gradient). The h1's own computed color is transparent because the colour is painted by the animation wrap. Body copy is 16px Inter. Two buttons sit under it: filled "Get started for free" and white "Get a demo". Both go to signup or book-a-demo and were not followed.

Below that, a video frame at 28px radius, then rounded section bands (56px) with gradient fills, problem cards, and a work-email field near the bottom. The field is not a signup form by itself. It was not filled.

## Pricing

Eyebrow "Transparent pricing", h1 "Individual Plans" at the h2 step (56px). A pill toggle defaults to "Bill annually" with an "Unlimited" tag. Three cards: Free `$0`, Email `$83` per month (billed `$990` per year), Email + Phone `$166` (billed `$1,990` per year). A Team Plan band says "Custom pricing" and "Contact sales". CTAs were not followed. Checkout was not opened.

## Enterprise

A dark hero. The h1 is white, 64px Britti Sans, "Empower your team with world-class contact data." The nav "Log in" and "Sign up" buttons on this page are filled `#7e43ff` with white text, unlike the white buttons on the home nav. "Get started" and "Explore options" were not followed. No form was on the page.

## Customers

A story grid. Tiles are `#f6f8fa`, 8px radius. "Read story" was not followed, so story detail pages are a gap.

## Privacy and 404

Privacy is long prose: h1 at 56px, body 16px / 24px Inter in `#26114a`, links `#7e43ff` underlined. The page is about 16591px tall. The 404 says "404" at 56px Britti Sans and "This page could not be found." with "Return home".

## Blog

`/blog/` is a separate WordPress theme (`wizapress`). Body font is Work Sans, not Britti Sans or the marketing Inter. The Blog Home chip is `#ffacac`. WordPress preset colours are present and are not the marketing swatches. Treat the blog as a different surface.

## Login

`/auth/login` is the product app, not the marketing site. Inter var, a white card at 12px radius, one email field, a purple "Log in" button, "Log in via Google", and a "Get started" link. Nothing was typed or submitted. Google SSO was not entered. Signup hit Cloudflare and was not measured.

## Gaps

- No full-page screenshots.
- Phone menu not opened. Only the closed 390px home was measured.
- Monthly pricing state not opened.
- Story detail, blog post, book-a-demo, and contact-sales pages not opened.
- No loading, empty, or error state of a form. The 404 is the only error page.
