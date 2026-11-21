# ClassPass public site tree

Mapped from https://classpass.com/ on 2026-11-21, signed out, in headless Chromium at 1440 x 900 and 390 x 844. Each row is a control that was opened, or a link that was followed, and where it went. Auth walls were recorded and not entered. No email, password, or SSO button was used.

Cookie banner: a dialog titled "This site uses cookies and similar technologies" with OK and Cookie Preferences. It was hidden in CSS for later shots. Neither button was clicked, because a consent button can POST.

## Home, desktop

| Control | Opens |
|---|---|
| Logo (aria-label home) | `/` |
| Search | `/search` |
| Plans | `/plans` |
| How it works (button, aria-haspopup menu) | Menu with How ClassPass works (`/how-classpass-works`) and How credits work (`/features`) |
| Gifts | `/gifts` |
| List my business | `/partners` |
| Corporate wellness | `https://corporate-wellness.classpass.com/` (the path `/corporate-wellness` on the apex host redirects there) |
| Log in | `/login` (email and password, Sign in with Apple, Sign in with Google). Stop. |
| Get 14 days free (header pill and yellow banner) | `/walkthrough`, which redirects to `/walkthrough/getclasspass` |
| Banner Close | Dismisses the yellow trial banner. Not a page. |
| Learn more about ClassPass | `/walkthrough/edusignup` |
| fees apply | `https://help.classpass.com/hc/en-us/articles/207942743-What-is-the-reservation-cancellation-policy` (help centre, off the marketing host) |
| Footer Company: About us, About Playlist, Why studio fitness, Gifts, Careers, Press, How credits work, Reviews | `/about`, `//playlist.com`, `/fitness`, `/gifts`, `/about/careers`, `/press-room`, `/features`, `/try/reviews` |
| Footer Corporate wellness: Our program, How it works, Refer your company, BeneFit blog, Resource center | `/corporate-wellness`, `/corporate-wellness/explainer`, `/corporate-wellness/refer-your-company`, `/corporate-wellness/blog`, `/corporate-wellness/resources` (these four leave the apex host for `corporate-wellness.classpass.com`) |
| Footer Support: Contact us, Help center, language button | `/contact`, `https://help.classpass.com/hc/en-us`, and a menu titled Select your language (Bokmål, Dansk, Deutsch, English (United States), Español, Français, Nederlands, Português, Português (Brasil), Svenska, 日本語). English stayed selected. |
| Footer Partners: Partners, Earnings calculator, Integration API docs, After Class blog, Resource center | `/partners`, `/partners/revenue-calculator`, `https://developers.classpass.com/specInfo`, `/afterclass` (redirects to `/partners/blog`), `/partners/resources` |
| Footer Community: Refer a friend, Become an affiliate, Blog, Activities, Popular studios, Explore gym access | `/try/referral-program`, `/try/affiliate-program`, `/blog`, `/search-index`, `/brands`, `/gym` |
| App Store, Google Play, social icons | Apple, Google, Facebook, X, Instagram, Pinterest. External. Not opened as product UI. |
| Terms of use, Privacy policy, Cookies & ads, Accessibility, Cookie Settings | `/terms` (redirects to `/terms/sgp`), `/privacy` (redirects to `/privacy/sgp`), cookies link, `/about/accessibility`, cookie settings control |

## Home, phone

The header is a logo and a hamburger. The hamburger opens a full-screen drawer: Search, Plans, How ClassPass works, How credits work, Gifts, List my business, Corporate wellness, Log in, and a blue Get 14 days free pill. Close is the X. Same destinations as the desktop nav.

## Pages that loaded

| Path | What it is |
|---|---|
| `/` | Marketing home. Rotating word (fitness, wellness, beauty, gyms) over photo tiles. |
| `/plans` | Plan picker. Credit cards and a monthly price in the currency the site chose. Change location is `/location`. |
| `/how-classpass-works` | How ClassPass works. Trial CTA goes to `/walkthrough/getclasspass`. |
| `/features` | How credits work. |
| `/gifts` | Gift cards. |
| `/about`, `/about/careers`, `/about/accessibility` | About, careers, accessibility statement. |
| `/fitness` | Why studio fitness. Learn more goes to `/walkthrough/edusignup`. Claim trial goes to `/member-signup/getclasspass`. |
| `/try/reviews` | Reviews. |
| `/try/referral-program`, `/try/affiliate-program`, `/try/brand-partnerships` | Referral, affiliate, brand partnership. |
| `/contact` | Contact. "Have an account? Log in" points at `/login`. The page itself is public. |
| `/blog` and `/blog/what-is-somatic-yoga/` | Blog index and one post. Categories: Fitness, Wellness & recovery, Spa & beauty. |
| `/search-index` and `/search-index/amsterdam` | City index, then activities in one city. `/search-index/new-york` 404s without the slug the index uses. |
| `/brands` and `/brands/soulcycle` | Brand index and one brand page. |
| `/gym` | Gym explainer. The copy that loaded was the Germany gym page. |
| `/press-room` | Press room. |
| `/partners` and its children | Partner marketing: how it works, revenue calculator, booking integrations, resources, blog, FAQs, contact. Partner contact is a form. It was not filled. |
| `/location` | "Where are you located?" with a submit control. The field was not filled and the form was not submitted. |
| `/terms/sgp`, `/privacy/sgp` | Legal pages. The site redirected `/terms` and `/privacy` to the `sgp` copies. |
| `/walkthrough/getclasspass`, `/walkthrough/edusignup` | Public trial explainers with Next slides. Skip straight to sign up goes to `/member-signup/...`. |
| `/member-signup/getclasspass` | Sign-up wall: Get started, Sign up with Apple, Get started with Google. Stop. Not submitted. |
| `/login` | Welcome back. Email, password, Apple, Google, Forgot your password, Partner Dashboard login. Stop. |
| `/reset-password` | Email field and Submit. Stop. Not filled. |

## Search and studio

`/search` is a public studio list with Fitness, Activities, Amenities and Distance menus. The headless browser was placed in a city by the site. Those shots, and the studio page they linked, show a street address and a map pin, so they are not in `screenshots/`. The filters were opened during mapping: Fitness lists All categories, Fitness, Wellness, Beauty.

## Stopped branches

| Control | URL | Why it stopped |
|---|---|---|
| Log in | `/login` | Email, password, Apple, Google |
| Get 14 days free, Skip straight to sign up | `/member-signup/getclasspass` and `/member-signup/edusignup` | Apple, Google, account creation |
| Forgot your password | `/reset-password` | Email form |
| Partner Dashboard login | not followed | Auth |
| Sign in with Apple, Sign in with Google, Sign up with Apple, Get started with Google | SSO | Not clicked |
| Location submit, partner contact, gift purchase, newsletter | forms | Not filled |

## Not a dark theme

No theme switch was found on the public pages. `color-scheme` on the home page was `normal`. Captures are light only.
