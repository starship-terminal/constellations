# Patterns

Public pages on savee.com, measured 2026-11-19 at CSS viewport 1169 by 731. No page screenshots. Preview frames failed.

## Marketing shell, light

Home, features and pricing ship `html` class `theme-light`. The page background is `#fdfdfd`. The home shell under the nav is `#f3f3f3` from the class `bg-[#F3F3F3]`.

The nav is fixed, 64px tall, full width. A scrim behind it is `oklab` near-white at 80 percent with `backdrop-filter: blur(24px)` and a 1px bottom border of `#dadada`. Links are Features, Teams, Pricing. Actions are Log in and Join for free. `--nav-height` is 100px. The rendered bar is 64px.

The hero is one line of saveeFont at 77.74px, weight 500, `#0a0a0a`, tight tracking. The lede under it is 21px `#404040`. Actions are a black pill and a `#dadada` pill.

Save tiles are 320px tall, 16px radius, `#e4e4e4`, in a loose masonry. They link to `/join/`.

The footer is "Made for visual minds" with 16px links in `#464646`.

## Marketing shell, dark

FAQ, contact and team ship `html` class `theme-dark` without a toggle on the page. Body background is `#0e0e0e`. Body text is `#d4d4d4`. The nav links change to Features, Marketplace, MCP. Join for free flips to a white pill with `#0e0e0e` text.

`prefers-color-scheme` was dark while home stayed `theme-light`. The class on `html` decides the theme, not the system preference.

## Login

https://savee.com/login/ stays light. Title "Let's get you inside." at 35.07px medium. Lede "Log in or sign up, no password needed." is `#a3a3a3`. Google and Apple sit above an underline email field. Copy under the field says a link will be emailed. The form was filled and cleared. It was not submitted.

## Pricing

Three plan cards in a row: Pro, Portfolio, Team. Prices read were `$9`, `$15` and `$12` per seat, yearly. A Popular badge sits on Pro. Billing is a pill toggle. Monthly was not selected, and no checkout was opened.

## FAQ

A three-column grid of questions, not an accordion. Clicking the first question revealed its answer in the same cell. No dialog.

## Contact

A short dark form: name, email, message, a white Contact us pill, and a reCAPTCHA iframe. Not submitted.

## Team

https://savee.com/team/ redirected to https://savee.com/team/create/. Dark marketing for "Create your team", with a white pill. Creating a team was not started.
