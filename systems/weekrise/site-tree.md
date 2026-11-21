# Weekrise public site tree

Mapped from https://weekrise.com/ on 2026-11-21 in headless Chromium, signed out. Viewport 1440 x 900, then 390 x 844 for the phone menu. `sitemap.xml` returned 404. `robots.txt` returned 200 and states content signals. It does not list a disallow path for `/`.

The public site is one marketing page plus Academy, three legal pages, and an external imprint. Pricing is a section on the homepage, not its own URL. A control that opens a login or signup wall is recorded and that branch stops. No email, name, password, or code was typed. Google was not clicked. No form was submitted.

## Header

Present on every public page. At 1440 the links sit in the bar. At 390 they move into the menu button.

| Control | Opens |
|---|---|
| Weekrise wordmark | https://weekrise.com/ |
| Pricing | Same page. Scrolls to the Pricing section. URL stays https://weekrise.com/. See Pricing. |
| Academy | https://weekrise.com/academy |
| Login | https://weekrise.com/auth/login. Empty email wall. Branch stops. See [login-review.json](login-review.json). |
| Signup | https://weekrise.com/auth/signup. Empty name and email wall. Branch stops. |
| Open Navigation (390) | In-page overlay. See Phone menu. |

## Homepage controls

The homepage is one long page, about 11466 px at 1440. These controls stay on the page except where the table says otherwise.

| Control | Opens |
|---|---|
| Get Started (hero) | https://weekrise.com/auth/signup. Branch stops. |
| Learn more | Same page. Scrolls to the section "Task management, designed for people, not robots." |
| Start Timer | Same page. Scrolls to the Pomodoro demo. The 70 x 70 control has no accessible name. The demo shows a play button and "25 : 00". It was not started. |
| Sign up (Free card) | https://weekrise.com/auth/signup. Branch stops. |
| Get Started (Pro card) | https://weekrise.com/auth/signup. Branch stops. |
| Get Started (Team card) | https://weekrise.com/auth/signup. Branch stops. |
| Get started for free (closing band) | https://weekrise.com/auth/signup. Branch stops. |

The product frames under the hero are marketing illustrations. They are not the signed-in planner.

## Pricing

Reached by the Pricing control. The URL does not change.

| Card | Price shown | Action |
|---|---|---|
| Free | $0 /month | Sign up, then https://weekrise.com/auth/signup. Branch stops. |
| Pro | $4 /month | Get Started, then https://weekrise.com/auth/signup. Branch stops. |
| Team | $12 /month (flat rate) | Get Started, then https://weekrise.com/auth/signup. Branch stops. |

No billing switch. Checkout was not opened. See [screenshots/home-light-pricing.png](screenshots/home-light-pricing.png).

## Phone menu

At 390 the bar shows the wordmark and a button labelled Open Navigation. Opening it shows Close Navigation, Pricing, Academy, Login, and Signup. Login and Signup are the same walls as the desktop chips. The branch stops at those URLs. See [screenshots/home-light-phone-menu.png](screenshots/home-light-phone-menu.png).

## Footer

Shared on the public pages.

| Control | Opens |
|---|---|
| Tobias Herber | https://twitter.com/tobiasherber_ |
| Weekrise | https://weekrise.com/ |
| Privacy Policy | https://weekrise.com/privacy |
| Terms of Service | https://weekrise.com/terms |
| Payment Policy | https://weekrise.com/payments |
| Imprint | The footer href is https://herber.space/imprint. Following it landed on https://tobiasnotes.com/imprint. External page. Not photographed. |

The footer does not print a street address.

## Academy

https://weekrise.com/academy uses the same header and footer. The topic list and the essay sit on one page. Each topic is also its own URL. The index opens on the Academy welcome. Selecting a topic swaps the essay and changes the URL.

| Topic | Opens |
|---|---|
| Teamwork | https://weekrise.com/academy/team |
| Pomodoro | https://weekrise.com/academy/pomodoro |
| Command Menu | https://weekrise.com/academy/command-menu |
| Google Calendar | https://weekrise.com/academy/google-calendar |
| Daily Digest | https://weekrise.com/academy/digest |
| Tags and Filters | https://weekrise.com/academy/tags |
| Customize Weekrise | https://weekrise.com/academy/customize |
| Bulk Editing | https://weekrise.com/academy/bulk |
| Tips and Tricks | https://weekrise.com/academy/tips |

The photographed article is Pomodoro. The others use the same chrome and the same topic list. See [screenshots/academy-light-default.png](screenshots/academy-light-default.png) and [screenshots/academy-article-light-default.png](screenshots/academy-article-light-default.png).

## Legal pages

| Page | URL | Controls beyond the chrome |
|---|---|---|
| Privacy Policy | https://weekrise.com/privacy | Links to Vercel, Hetzner, Cloudflare, Namecheap, Crisp, and Paddle privacy pages. External. Not followed. |
| Terms of Service | https://weekrise.com/terms | A table of contents of 30 anchors on the same page (`#agreement` through `#contact`). Also links to the privacy page, https://ec.europa.eu/consumers/odr, and Termly. External links were not followed. |
| Refund and Payment Policy | https://weekrise.com/payments | Links to https://paddle.net/ and Paddle's checkout buyer terms. External. Not followed. |

## Auth walls

Recorded and not passed.

| Control | URL | What the empty wall asks for |
|---|---|---|
| Login, and Sign up instead on the signup wall | https://weekrise.com/auth/login | Email, Continue, Sign in with Google. See [login-review.json](login-review.json). |
| Signup, Get Started, Sign up, Get started for free, and Log in instead's pair | https://weekrise.com/auth/signup | Name, Email, Continue, Sign in with Google. |

Login's "Sign up instead" points at `/auth/signup`. Signup's "Log in instead" points at `/auth/login`. Each href also carries a `next` query. That value is a return path, not a credential, and it is not copied here. Neither wall was submitted. Google was not clicked.
