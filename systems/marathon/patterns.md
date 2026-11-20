# Patterns

Public pages on https://onmarathon.com, read 2026-11-18, signed out. The product is an archive. Account, dashboard and checkout sit behind sign-in and were not entered.

## Archive frame

Every captured page shares one frame.

1. A lime banner: "You're looking at the Marathon archive." The arrow leaves toward Never Before Seen. That off-site link was not followed as a product surface.
2. A sticky header: logomark, Product, For Agencies, Pricing, Sign In, Get Started.
3. A light page field. The token `light.page` is `#ffffff`. The painted field reads slightly gray.
4. A footer with links to neverbeforeseen.group (careers, privacy, terms) and YouTube. Those leave the site and were not followed.

[home](screenshots/home-light-default.png), [full](screenshots/home-light-full.png).

## Letter

`/` is a letter, not a product tour. The heading is "Thanks for everything." at `core.typography.heading`. Body is a narrow column at `core.typography.body` in `light.textMuted`. The sign-off is Jeremy Blaze, Never Before Seen. There is no app shell on this page.

## Pricing

Two cards. Free is a white surface with `$0`. Pro is a lime card (`light.accent`) with a Popular badge and `$49` per user per month billed annually. The segment switches the billing copy. Both Get Started links point at `/register`, which redirects home. No checkout, payment or billing portal was opened.

[annual](screenshots/pricing-light-default.png), [monthly](screenshots/pricing-light-monthly.png).

## Agencies page

`/for-agencies` is marketing. It includes a public demo of a shared board. Treat that board as a public demo, captured as it rendered, not as the signed-in dashboard or account. The share host was not followed into the app.

[shot](screenshots/agencies-light-default.png).

## Demo

`/demo` offers Book A Demo. The page embeds a SavvyCal iframe. At capture the embed showed a spinner. The form was not submitted. No booking was made.

[shot](screenshots/demo-light-default.png).

## Curated

`/curated` is a public marketing page. It loads signed out. [shot](screenshots/curated-light-default.png).

## Phone

The same frame collapses to a menu button. The open menu is a solid sheet with the nav links, Sign In, and a full-width Get Started. [menu](screenshots/mobile-home-light-menu.png).

## Gates

| Surface | What happened |
|---|---|
| `/sign-in` | Redirects to `/`. Sign-in form was not submitted. No fields painted. [shot](screenshots/signin-light-redirect.png) |
| `/register` | Redirects to `/`. Registration was not submitted. [shot](screenshots/register-light-redirect.png) |
| Get Started | Link to `/register`. Not used as checkout. No purchase. |
| Book A Demo | Embed was not submitted. |
| app.onmarathon.com | Account, dashboard and workspace are behind sign-in. Not entered. |
| Cookie banner | None appeared. The hide path was not a click. |

Dark theme is declared in CSS and was not painted. There is no dark screenshot.
