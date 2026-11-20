# Patterns

## Marketing shell

Sticky header, 57px, padding 18px inline, transparent at rest, bottom border transparent, 200ms colour transition. Links: Features, Teams, Pricing. Actions: Log in (secondary pill) and Sign up (primary pill). Page background `#FDFDFD`. Type is ABC Oracle at -0.02em.

Shown in [screenshots/home-light-default.png](screenshots/home-light-default.png) at 1440 by 900, and [screenshots/home-light-phone.png](screenshots/home-light-phone.png) at 390 by 844. The phone width keeps Log in, Sign up and a menu button. The menu was not opened.

## Hero

H1 at 32px, weight 400, line-height 1.2, tracking -0.64px, colour `#0C0A09`. The subtitle is the same size at black 50%. Get started is the primary body button. Under it, a 32px-radius frame holds a demo: Long form, Short form, Product demos, Video messages. That demo is a public marketing animation, not the signed-in editor.

The full page is [screenshots/home-light-full.png](screenshots/home-light-full.png). Photographs in that file are banded because the PNG is 256-colour. Read colour from the tokens.

## Pricing

Three articles in a grid (two columns from 700px, three from 1050px), gap 12px. Pro, Premium, Enterprise. Annual is the default switch state, with a 50% off badge. A users stepper sits beside it. Buy now and Contact sales stay on the page. Buy now was not clicked, because that continues into payment.

Shown in [screenshots/pricing-light-default.png](screenshots/pricing-light-default.png).

## Sign in

`https://www.tella.tv/api/login` redirects to `https://authkit.tella.tv/` (WorkOS AuthKit). The card is 440px, 16px radius, 48px padding, inset ring. Heading "Sign in to Tella" at 24px semibold. Email field, Continue with email, then Google and Apple. A sign-up link sits under the card. No screenshot of this page is in the package: the preview browser could not produce frames, and a headless session was not started against the login host.

The email was not submitted. Google, Apple and company SSO were not opened.

## Theme

`html` on the marketing site carries the class `dark`, and the stylesheet declares a `.dark` token set (`--background: #1E2025`, foreground `#ECEEF4`). The marketing shell does not use those variables. It paints `#FDFDFD` and slate-950. No theme control was on the pages that were read. The dark tokens are the declaration, not a captured screen.
