# Variant public site tree

Mapped on 2026-11-22 from the live public site, signed out, in an incognito preview tab. Official domain confirmed as `https://variant.com/` (wordmark "variant", title "Variant – Endless designs for your ideas, just scroll", legal name Variant Design, Inc.). The page loaded. It is not a parked domain and not a captcha wall.

Nothing was typed. No identity provider was clicked. No form was submitted. No captcha was solved. The signed-in app was not opened. `login-extracted` stays `not-started`.

origin/main already had `systems/variant/`. This file refreshes that package. The slug did not change.

The public product is one dark app shell, not a marketing site with a nav and a footer. `/` is a left column (headline, two chips, a composer) beside a scrolling grid of public design widgets. There is no header menu, no footer, and no theme control. Forcing a light colour scheme on 2026-11-19 left the page on `rgb(34, 34, 34)`.

The grid cards are public demos (a weather card, a bike-battery card, a radio, and others from `/homepage-widgets/manifest.json`). Copy inside them is the site's sample copy.

## Homepage controls (`https://variant.com/`)

Desktop column is 408px wide inside a 1440 CSS viewport. Phone (390) uses the same column at full width. There is no menu button at 390.

| Control | Opens | Action |
|---|---|---|
| Wordmark | Stays on `/` | Not a link on the homepage. On `/authentication` the same mark is a Home link to `/`. |
| Sign up / Sign in | `https://variant.com/authentication` | One wall for login and signup. See Auth wall. |
| Surprise me | `https://variant.com/authentication?prompt=Create+something+that+will+surprise+me` | Same wall, with a prompt query. Not followed. The chip was not clicked, so the prompt was not submitted. |
| Composer, placeholder "See endless designs for..." | Would push `/authentication?prompt=...` | Left empty. Submit stays disabled. Not typed. Not submitted. |
| Add image | A hidden file input (`accept="image/*"`) | Not clicked. No file was chosen. |
| Select style | No menu, dialog, or popover | Clicked. The button took focus. Nothing opened. The style modal is signed-in chrome and was not entered. |
| Submit | Disabled while the composer is empty | Not clicked. |

A click on Sign up / Sign in is the only homepage control that changes the page.

## Auth wall

Photographed empty. Stopped there. Login and signup are the same card. There is no separate signup URL.

| Control | Opens | Action |
|---|---|---|
| Continue with Google | Identity provider | Not clicked. |
| Email address | An empty field, placeholder "Email address" | Not typed. |
| Continue with Email | Would start the email flow, then a code step | Disabled while the field is empty. Not clicked. |
| Terms of Service | `https://variant.com/terms-and-privacy` | Opened. |
| Privacy Policy | `https://variant.com/terms-and-privacy` | Same page. The Privacy Policy tab was not selected. |
| Home | `/` | Present on the wall. Not needed to leave. |

The email flow's later steps (a code field, Resend, Verify, Back) are in the page script. They were not opened, because opening them means submitting the form.

## Legal page (`https://variant.com/terms-and-privacy`)

Public. Two tabs in one page: Terms of Service (selected on load) and Privacy Policy. No other nav. The article is long. A crop of the tabs and the heading was kept. The rest of the article was not committed: it prints a public contact email, a street address, and a phone line.

A link inside the terms points at `/privacy-policy`. That path 307s to `/authentication?next=%2Fprivacy-policy` and was not followed.

## Pages that are not public

A direct request for these paths 307s to `/authentication?next=<path>`. None was opened, because the next step is the auth wall or the signed-in app.

`/pricing`, `/about`, `/blog`, `/careers`, `/login`, `/signup`, `/sign-in`, `/sign-up`, `/community`, `/docs`, `/changelog`, `/security`, `/privacy`, `/terms`, `/privacy-policy`.

There is no public pricing page. Plan names (Free, Pro, Monthly, Yearly) live in the signed-in billing script. That screen was not opened.

`robots.txt` disallows `/design/`, `/images/`, `/profile/`, `/collections/`, `/assets/`, and `/shared/`. Those were not requested.

## Signed-in shell, not entered

The layout script names Community, Projects, Saved, Boards, Account settings, and billing dialogs (Upgrade, Manage plan, Confirm upgrade). A session check on `/` would send a signed-in browser to `/community`. This tab was signed out. Those routes were not opened.

## Phone

390 by 844, devicePixelRatio 2. PNG width 780.

| Page | What it shows |
|---|---|
| `/` | The same column, full width. A grid card overlaps the copy. No drawer. |
| `/authentication` | The same empty wall. The card is 400px wide, so it overflows the 390 frame. |
