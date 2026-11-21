# Luma site tree

Mapped 2026-11-21 from the public homepage at https://lu.ma/ before screenshots. lu.ma redirects to https://luma.com/. Signed out. `html.theme-root.light`. `theme-color` `#ffffff`. The public event page paints `theme-root.dark` on its own. No theme switch was found on the marketing shell.

No cookie dialog was on the page. No password, email, or code was typed. No form was submitted. Google and Passkey were not clicked. The clock in the product nav reads the machine's timezone. That chrome is not an account.

This is Luma the events product. luma.ai and lumalabs.ai are different products and were not opened.

## Shell (desktop, 1440)

The landing header is a bar with the spark logo and Sign In. The logo is an SVG, not a link. Discover, Pricing, and App are not in this bar. They sit in the footer, and on inner pages they sit in a product nav.

| Control | Opens |
|---|---|
| Spark logo | nothing. It is not a link. |
| Sign In (`a.landing-signin[href="/signin?next=%2Fhome"]`) | page https://luma.com/signin?next=%2Fhome. Login wall. Branch stopped. |

## Home https://luma.com/

| Control | Opens |
|---|---|
| Skip to Content | same page, `#main-content` |
| run clubs | page https://luma.com/jlnifjub. Public event. |
| launch parties | page https://luma.com/5.5. Public event. |
| firework shows | page https://luma.com/july4-brooklyn. Public event. The page paints dark. |
| Create Your First Event | page https://luma.com/create. Create form with a sign-in card. Branch stopped. Not submitted. |
| Discover Events (hero) | page https://luma.com/discover |
| City name under "Popular Events in" (`button.lux-menu-trigger-wrapper`) | menu on the same page (`.lux-overlay.modal` plus `.city-menu`). A city click stays on `/` and sets `?city=`. |
| Event cards in Popular Events | public event pages such as `/65anjsk3`. One public example was photographed. |
| Upcoming Major Events cards | public calendar pages such as `/binance-blockchain-week?k=c` |
| Explore Global Communities cards | public calendar pages such as `/readingrhythms-global?k=c` |
| Category tiles (Family, Books, Games, Tech, Food & Drink, AI, Running, Arts & Culture, Climate, Fitness, Wellness, Crypto) | pages `/family?k=t`, `/books?k=t`, `/games?k=t`, `/tech?k=t`, `/food?k=t`, `/ai?k=t`, `/running?k=t`, `/arts?k=t`, `/climate?k=t`, `/fitness?k=t`, `/wellness?k=t`, `/crypto?k=t` |
| Discover Events (lower) | page https://luma.com/discover |
| Get the App | page https://luma.com/app |

### City menu (click, same page)

Region buttons filter the city list. City buttons stay on the homepage.

| Control | Opens |
|---|---|
| Asia & Pacific, Africa, Europe, North America, South America | same menu, filtered city list |
| Auckland, Bangkok, Bengaluru, Dubai, Hong Kong, Honolulu, Jakarta, Kuala Lumpur, Manila, Melbourne, Mumbai, New Delhi, Seoul, Singapore, Sydney, Taipei, Tel Aviv-Yafo, Tokyo | same page, `/?city=<slug>`. Tokyo was opened and the menu closed. |

## Footer (every marketing page)

Discover `/discover`, Pricing `/pricing`, App `/app`, Terms `/terms`, Privacy `/privacy-policy`, Security `/security`, DMCA `/dmca`.

Leaves the site, not opened as product surfaces: Help (https://help.luma.com), Luma on Instagram, Luma on X, Contact Us (`mailto:support@luma.com`).

## Product nav (inner pages, not the landing header)

| Control | Opens |
|---|---|
| Luma Home | page https://luma.com/ |
| Discover Events | page https://luma.com/discover |
| Sign In | page https://luma.com/signin?next=<current path>. Login wall. |

## Phone (390)

The landing header is the same spark and Sign In. There is no Open menu button. Footer links wrap under the page.

| Control | Opens |
|---|---|
| Sign In | page https://luma.com/signin?next=%2Fhome. Login wall. |
| City name | the same city menu as desktop. |

## Login and create walls (recorded, not entered)

| Control or URL | What loaded |
|---|---|
| Sign In, `/signin` | Page "Sign In · Luma". "Welcome to Luma. Please sign in or sign up below." Empty email field (`you@email.com`), Use Phone Number, Continue with Email, Sign in with Google, Sign in with Passkey. Branch stopped. Google was not clicked. Email was not typed. Phone was not opened. |
| Create Your First Event, `/create` | Page "Create Event · Luma". A public create form (theme, calendar, dates, location, ticket price, capacity) and the same sign-in card. Create Event was not clicked. The form was not submitted. |
| Get Started on `/pricing` | `/signin`. Login wall. Not entered past the empty card. |
| Get Luma Plus on `/pricing` | `/calendar/manage/plus?cadence=yearly&source=pricing`. Not opened. Checkout was not started. |
| Follow, Contact the Host, Report Event on a public event | not clicked. They ask for an account or send a message. |

## Public pages the footer and hero open

| Control | Opens |
|---|---|
| Discover | page https://luma.com/discover. Light. Category and calendar links. |
| Pricing | page https://luma.com/pricing. Light. Monthly and Annual are buttons on the same page. |
| App | page https://luma.com/app. Light. A QR code and "open lu.ma/app on your phone". |
| Terms | page https://luma.com/terms. Light. |
| firework shows | page https://luma.com/july4-brooklyn. Dark public event. |
