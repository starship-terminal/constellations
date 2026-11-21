# Kitchen.co public site tree

Mapped from https://kitchen.co/ on 2026-11-21 in an incognito T3 preview tab, signed out, before screenshots. The official product is https://kitchen.co (Client Portal Software for Agencies). This is not Kitchen Stories (kitchenstories.com).

The homepage stays on `/`. Title: "Client Portal Software for Agencies | Kitchen.co". One light theme. `colorScheme` is `normal`. Body font is Graphik. Page background is white. No dark toggle on the public pages.

No email, password, phone, or code was typed. No form was submitted. No identity provider was clicked. No captcha was solved.

The preview pane did not produce screenshot frames ("The browser is not producing screenshot frames"). The tree below is from the live DOM in that tab. Photographs are taken separately with the package's headless capture.

## Promo bar

Present above the header on the homepage.

| Control | Opens |
|---|---|
| Black Friday Month: 20% OFF Lifetime Plans with code BF20 | https://kitchen.co/buy (public lifetime pricing). Not a checkout submit. |

## Header

Present on the homepage. Desktop nav is in `.header__nav`. The phone control is `a.header__nav-mobile` ("Menu").

| Control | Opens |
|---|---|
| Wordmark (Kitchen.co) | https://kitchen.co/ |
| Features | https://kitchen.co/features |
| Solutions | a dropdown on the same page (`.has-dropdown` / `.dropdown`). It is a menu, not a new route. |
| Pricing | https://kitchen.co/pricing |
| Tutorials | https://kitchen.co/tutorials |
| Affiliate Program | https://kitchen.co/affiliate-program |
| Log in | https://kitchen.co/login. Stop. |
| Try it FREE | https://kitchen.co/get-started. Stop at the signup wall. |
| Menu | the phone drawer on the same page. Desktop header hides this control. |

## Solutions menu

Opened by hovering Solutions. Four links, each with a title and a one-line description.

| Control | Opens |
|---|---|
| Creative Agencies ("Work better with clients") | https://kitchen.co/for-creative-agencies |
| Accounting and Bookkeeping ("Dazzle clients with your process") | https://kitchen.co/for-accounting-agencies |
| Law Firms ("Get clients the results they want") | https://kitchen.co/for-law-firms |
| Freelancers ("Become a master multi tasker") | https://kitchen.co/for-freelancers |

## Homepage

https://kitchen.co/

| Control | Opens |
|---|---|
| Get Started—it's FREE | https://kitchen.co/get-started. Stop. The same label repeats in the body. |
| Folders, Conversations, Boards, Docs, Files, Invoicing & Payments, Embed URL, File Feedback, White-label | switches the hero preview tab on the same page (`#hero-preview-*`). Folders starts selected. No dialog. |
| Creative Agencies, Accounting and Bookkeeping, Freelancers, Law Firms | switches the "Built for service businesses" panel on the same page (`#solution-*`). Creative Agencies starts selected. The same four names also appear as footer links to the `/for-*` pages. |
| Learn more about integrations | https://kitchen.co/integrations |

Integration marks on the homepage (Zapier, GoogleDrive, Dropbox, OneDrive, Stripe, PayPal, Square, Razorpay) are figures, not links.

## Cookie dialog

A `role="dialog"` banner (`.cookie-banner`) sits on the homepage. It is not a login wall.

| Control | Opens |
|---|---|
| Accept all | stores the cookie choice. Not clicked. |
| Reject all | stores the necessary-only choice. Not clicked in this walk. The headless capture hides the banner with CSS and does not click it. |
| More options » | the settings view of the same dialog: Strictly Necessary (disabled, always on), Functional, Analytics, Marketing, Done, « Simpler choices. |
| See the Cookie Policy for details | https://kitchen.co/legal/cookie-policy |

## Blog header

https://kitchen.co/blog uses a different header from the marketing homepage: Features, Solutions, Pricing, About, Get a Demo, Log in, Try it FREE. Under that: Blog, Insights, and a search icon (`a.form-search__btn`). The sticky header covers that icon, so a click did not open a visible field. No search screenshot was kept. The field was not submitted.

## Footer

The footer columns are not labelled in the DOM. Links, in order:

| Control | Opens |
|---|---|
| Wordmark | https://kitchen.co/ |
| Features | https://kitchen.co/features |
| Pricing | https://kitchen.co/pricing |
| Tutorials | https://kitchen.co/tutorials |
| How it Works | https://kitchen.co/how-it-works |
| Benefits | https://kitchen.co/benefits |
| Get a Demo | https://kitchen.co/get-demo. Stop. Demo request form. Not submitted. |
| Get Started | https://kitchen.co/get-started. Stop. |
| Reviews | https://kitchen.co/reviews |
| API Docs | https://developer.kitchen.co/ (other host; not captured) |
| Login | https://kitchen.co/login. Stop. |
| Find your workspace | https://kitchen.co/login/find. Stop. Same login family. |
| Creative Agencies, Accounting and Bookkeeping, Law Firms, Freelancers | the matching `/for-*` page |
| About us | https://kitchen.co/about |
| Our story | https://kitchen.co/our-story |
| Blog | https://kitchen.co/blog |
| Email Us | mailto:team@kitchen.co. Not opened. |
| Feedback | mailto:team@kitchen.co?subject=Feedback. Not opened. |
| Affiliate Program | https://kitchen.co/affiliate-program |
| 2create.io | https://2create.io/ (other host; not captured) |
| Terms | https://kitchen.co/legal/terms |
| Privacy | https://kitchen.co/legal/privacy |
| DPA | https://kitchen.co/legal/dpa |
| Cookie Policy | https://kitchen.co/legal/cookie-policy |
| Cookie Settings | reopens the cookie dialog on the same page |
| Facebook | https://facebook.com/kitchendotco (other host; not captured). Not an identity provider. |
| YouTube | https://www.youtube.com/@kitchendotco/videos (other host; not captured) |

## Pages this walk treats as public

Reached from the homepage controls above, and photographed when the headless capture can load them: `/`, `/features`, `/pricing`, `/buy`, `/for-creative-agencies`, `/for-accounting-agencies`, `/for-law-firms`, `/for-freelancers`, `/tutorials`, `/affiliate-program`, `/integrations`, `/how-it-works`, `/benefits`, `/reviews`, `/about`, `/our-story`, `/blog`, `/legal/cookie-policy`, `/legal/terms`, `/legal/privacy`, `/legal/dpa`.

## Stop

| Control | Why |
|---|---|
| Log in, Login | https://kitchen.co/login redirects to https://kitchen.co/login/workspace. Title: "Login to your workspace". One text field (placeholder "your-workspace"), Continue (submit), Find your workspace, Sign up—it's free. No Google, Apple, or other identity provider. Photographed at rest. Nothing typed. Continue not clicked. |
| Find your workspace | https://kitchen.co/login/find. Title: "Find your workspace". Email field (placeholder "name@work-email.com") and Continue with Email, which sends a magic code. Stop. Photographed at rest. Nothing typed. |
| Try it FREE, Get Started | https://kitchen.co/get-started. Title: "Get Started Today". Email field (placeholder "Enter your email to begin") and Continue. Stop. Photographed at rest. Not submitted. |
| Get a Demo | https://kitchen.co/get-demo. Title: "See if Kitchen.co's Right For You | Get a Demo". Fields: first name, last name, company, email, a Cloudflare Turnstile captcha, and Request a demo. Stop. Photographed at rest. Not submitted. Captcha not solved. |
