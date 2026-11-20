# Patterns

Signed-out pages only. Screenshots are viewport captures at the CSS size named in the file's `.capture.json`, not full-page scrolls.

## Marketing shell

[home-light-default.png](screenshots/home-light-default.png) at 1440 by 900 CSS pixels, device pixel ratio 2.

A 40px announcement strip sits above a 64px header. The header inner row measured 1040px wide inside the 1440 viewport, starting 40px below the viewport top. On the home page the header is transparent over a photograph, with a 5px backdrop blur on the bar. Nav labels are Geist 14px weight 500 at 80% white. Contact Sales is a quiet button. Start now is a white square.

The same shell on a light page is in [pricing-light-default.png](screenshots/pricing-light-default.png) and [contact-light-default.png](screenshots/contact-light-default.png). There the Start now button is ink, #0c0a09, on the stone page #f7f6f4.

[home-light-phone.png](screenshots/home-light-phone.png) is the same home URL at 390 by 844 CSS pixels. The nav collapses to a wordmark and a menu button. Contact Sales and Start now sit over the photograph as a pair of square buttons.

## Hero

The home hero is a photograph with a Season Mix display line at 56px, weight 420, line-height 67.2px, letter-spacing -1.12px, colour #0c0a09. A quote in the same face at 18px sits above it, in white at 90% opacity. Two square buttons sit under the line. This is a public marketing hero, not the signed-in product.

[platform-light-default.png](screenshots/platform-light-default.png) is the platform page hero: a two-line Season Mix title on the stone page, then Contact Sales (ink) and Start now (paper).

## Pricing

Three columns: Individual at $100 a month, Teams at $255 a month for the team, Enterprise as "Contact us". Prices are Season Mix 42px weight 420, colour #1c1917. The plan button is charcoal, #403f3e, with a white Geist 16px weight 500 label. A second column's button computed to #828282. No card field is on this page. Enterprise points at contact sales.

## Contact form

[contact-light-default.png](screenshots/contact-light-default.png) shows the top of /contact. The form itself starts below the fold. Crops of the fields are in [components.md](components.md). The form asks for work email, first name, last name, company, phone number, a "how did you hear about us" select, and a message. It was not submitted. The phone field is why.

The form card is #fafafa, padding 40px, shadow 0 2px 9px 1px rgba(0, 0, 0, 0.05), 640px wide.

## Login

Start now and the footer Login both open `https://run.rox.com/api/auth/login`, which redirects to `roxai.us.auth0.com`. Signup (`screen_hint=signup`) and login use the same card. The page says "Business email", then "Continue with Google" and "Continue with Microsoft". No email was entered. No SSO button was clicked. There is no screenshot of this page: the preview browser was not producing frames, and a login page is outside the headless-Playwright allowance.

## Not captured

Signed-in app shell, empty, loading and error states of the product, destructive confirmation, search, tables, onboarding. The home page has no dark theme. The photograph behind the hero is not a dark palette.
