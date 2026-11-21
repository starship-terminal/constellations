# On Marathon public site tree

Mapped from https://onmarathon.com/ on 2026-11-21 in headless Chromium before any package screenshots. The live site is an archive of the former Marathon product (Figma comment management). The banner says the product is archived and points at Never Before Seen.

No password, code, captcha, Google or Apple button, profile, birthday, plan, survey, onboarding or newsletter field was filled. No form was submitted.

## What loads

| Requested URL | Lands on | What is there |
|---|---|---|
| https://onmarathon.com/ | same, HTTP 200 | Archive homepage. Header, banner, product story, feature sections, footer |
| https://onmarathon.com/for-agencies | same, HTTP 200 | Agency marketing page |
| https://onmarathon.com/pricing | same, HTTP 200 | Three plan cards and a Pay Annually / Pay Monthly toggle |
| https://onmarathon.com/demo | same, HTTP 200 | "Book A Demo" heading and an embedded SavvyCal iframe. No public booking form in the page itself |
| https://onmarathon.com/curated | same, HTTP 200 | "Curated by Marathon" and one published video |
| https://onmarathon.com/sign-in | redirects to https://onmarathon.com/ | No login form. Branch stopped |
| https://onmarathon.com/register | redirects to https://onmarathon.com/ | No signup form. Branch stopped |
| https://onmarathon.com/privacy | redirects to https://neverbeforeseen.co/privacy | Off-site legal page. Not captured as a Marathon surface |
| https://onmarathon.com/terms | redirects to https://neverbeforeseen.co/terms | Off-site legal page. Not captured as a Marathon surface |

These paths return the on-site 404 page (heading "404"): `/changelog`, `/blog`, `/login`, `/signup`, `/app`, `/legal`, `/features`, `/about`, `/careers`, `/docs`, `/help`, `/sitemap.xml`, `/robots.txt`. The 404 page is public and is captured once. It is not linked from the homepage.

`html` carries class `light`. A `.dark` rule exists in the CSS and changes `--background` when the class is forced in a probe. No public control switches the theme, so dark is not a live theme.

## Header

Desktop (1440): a row of links. Phone (390): the wordmark, then an "Open menu" button.

| Control | Opens |
|---|---|
| Wordmark "Marathon" | https://onmarathon.com/ |
| Product | https://onmarathon.com/ (same page; hover opens no menu) |
| For Agencies | https://onmarathon.com/for-agencies |
| Pricing | https://onmarathon.com/pricing |
| Sign In | https://onmarathon.com/sign-in, which redirects to the archive homepage. No login form. Stopped |
| Get Started | https://onmarathon.com/register, which redirects to the archive homepage. No signup form. Stopped |
| Open menu (phone only, hidden at 1440) | In-page nav panel: Product, For Agencies, Pricing, Sign In, Get Started. Close control is labelled "Close menu" |

The desktop header has no Product dropdown, no account menu, and no theme switch.

## Banner

| Control | Opens |
|---|---|
| "You're looking at the Marathon archive. See what we're building now at Never Before Seen." | https://neverbeforeseen.group/?ref=marathon-classic (external). Not followed |

## Homepage sections

In-page content. No dialogs, menus, or forms.

| Control | Opens |
|---|---|
| Never Before Seen | https://neverbeforeseen.group/?ref=marathon (external). Not followed |
| Get Started (repeated in sections) | https://onmarathon.com/register, then the archive homepage. Stopped |
| YouTube link ("See how we ran a global, asynchronous design agency on Marathon") | https://www.youtube.com/watch?v=RsiPizbzMEQ (external). Not followed |

## For Agencies

Same header, banner and footer as the homepage.

| Control | Opens |
|---|---|
| Get Started | https://onmarathon.com/register, then the archive homepage. Stopped |
| Watch Now / YouTube link | https://www.youtube.com/watch?v=RsiPizbzMEQ (external). Not followed |

## Pricing

| Control | Opens |
|---|---|
| Pay Annually | Local toggle. Selected on load. Prices read $0 (Free) and $49 (Pro, "per user per month billed annually") |
| Pay Monthly | Local toggle. After click, visible prices include $0 and $59. No navigation, no form |
| Get Started on a plan | https://onmarathon.com/register, then the archive homepage. Stopped |

No FAQ accordion, no checkout, no card fields.

## Demo

| Control | Opens |
|---|---|
| SavvyCal iframe (`savvycal.com/nbs/...`, title "Book A Demo") | A third-party scheduler embedded on the page. It is a booking form. Not filled, not submitted. An empty `role="dialog"` node inside the embed is opacity 0 and has no text |

## Curated

| Control | Opens |
|---|---|
| Video `/marketing/videos/001-transcode.webm` | A published loop labelled in the page as "Marathon in action". Playback is a media control, not a form |

No gallery of outbound design links was present on 2026-11-21.

## Footer (every captured page)

"More" is a column heading, not a button. Clicking the word does not open a menu.

| Control | Opens |
|---|---|
| neverbeforeseen.group | https://neverbeforeseen.group/?ref=marathonfooter (external). Not followed |
| Product | https://onmarathon.com/ |
| For Agencies | https://onmarathon.com/for-agencies |
| Pricing | https://onmarathon.com/pricing |
| Demo | https://onmarathon.com/demo |
| Curated | https://onmarathon.com/curated |
| Careers | https://neverbeforeseen.group/careers (external). Not followed |
| Privacy | https://www.neverbeforeseen.group/privacy (external). Not followed |
| Terms | https://www.neverbeforeseen.group/terms (external). Not followed |

The footer also prints a studio line. That line is not a control. It is not copied into the package.

## Stopped branches

| Control | URL | Why stopped |
|---|---|---|
| Sign In | https://onmarathon.com/sign-in | Redirects to the archive homepage. No login form |
| Get Started / Register | https://onmarathon.com/register | Redirects to the archive homepage. No signup form |
| SavvyCal embed | https://onmarathon.com/demo | Booking form. Not filled |
| External legal, careers, studio, YouTube | listed above | Off-site. Not a Marathon surface |
