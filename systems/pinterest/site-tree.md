# Pinterest public site tree

Mapped on 2026-11-21 from [https://www.pinterest.com/](https://www.pinterest.com/) in Chromium, signed out, before the screenshot pass. Rechecked the same day: the homepage still paints the signed-out marketing page (title Pinterest, HTTP 200). Nothing was typed. No form was submitted. Google, Apple, Facebook, QR login, and account creation were not clicked.

The product surface is `www.pinterest.com`. Header links to About, Businesses, Create, and News leave that host. Policy links leave to `policy.pinterest.com`. Help leaves to `help.pinterest.com`. App-store links leave to Apple and Google. Those stores are recorded as exits, not as Pinterest UI.

## Homepage (`https://www.pinterest.com/`)

Signed-out marketing page. Title: Pinterest. A signup form is mounted in the page (email, password, birthdate) and is not filled. Search is a combobox and is not typed into.

| Control | Opens |
|---|---|
| Pinterest home (logo) | [https://www.pinterest.com/](https://www.pinterest.com/) |
| Explore | [https://www.pinterest.com/ideas/](https://www.pinterest.com/ideas/) |
| Search combobox, focused, nothing typed | Stays on `/`. A dialog named `modal` mounts. Copy: Welcome to Pinterest, email, password, Forgot password?, Continue with Google, Continue with QR code. **Wall. Branch stopped. Nothing typed. Google and QR not clicked.** Submitting a query is not done. |
| About (new tab) | [https://about.pinterest.com/](https://about.pinterest.com/) via `/_/_/about/` |
| Businesses (new tab) | [https://business.pinterest.com/](https://business.pinterest.com/) via `/_/_/business/` |
| Create (new tab) | [https://create.pinterest.com/en-sg/](https://create.pinterest.com/en-sg/) via `/_/_/create/` (geo path from this network) |
| News (new tab) | [https://newsroom.pinterest.com/en-sg/](https://newsroom.pinterest.com/en-sg/) via `/_/_/blog/` |
| Log in (header button) | Dialog on `/`, URL stays `/`. Copy: Welcome to Pinterest, log in, email, password, Forgot your password?, Continue with Google. Recheck also shows "Or, log in instantly by scanning code with your phone". **Wall. Branch stopped. Nothing typed.** Same wall as [https://www.pinterest.com/login/](https://www.pinterest.com/login/). |
| Sign up (header button) | Dialog on `/`. Copy: Join Pinterest for free, email, password, birthday. **Wall. Branch stopped.** |
| Join Pinterest for free (hero) | Same signup dialog. **Wall. Branch stopped.** |
| I already have an account (hero) | Login dialog, plus Continue with QR code. **Wall. Branch stopped. QR not opened.** |
| Scroll up / Scroll down | In-page scroll of the holiday carousel. No new URL. |
| Pause carousel | Pauses the hero carousel. No new URL. |
| View Previous / View Next | Moves the board carousel. No new URL. |
| See more boards / See more | [https://www.pinterest.com/pinterest/your-ultimate-holiday-starter-pack/](https://www.pinterest.com/pinterest/your-ultimate-holiday-starter-pack/) |
| Holiday mocktails everyone will love | [https://www.pinterest.com/food/holiday-mocktails-everyone-will-love/](https://www.pinterest.com/food/holiday-mocktails-everyone-will-love/) |
| Cookies to bake this holiday season | [https://www.pinterest.com/food/cookies-to-bake-this-holiday-season/](https://www.pinterest.com/food/cookies-to-bake-this-holiday-season/) |
| Easy appetizers and snacks for holiday hosting | [https://www.pinterest.com/food/easy-appetizers-and-snacks-for-holiday-hosting/](https://www.pinterest.com/food/easy-appetizers-and-snacks-for-holiday-hosting/) |
| Sleek holiday hair and makeup inspo | [https://www.pinterest.com/beauty/sleek-holiday-hair-and-makeup-inspo/](https://www.pinterest.com/beauty/sleek-holiday-hair-and-makeup-inspo/) |
| See what's new | Clicked. URL stayed `/`. No dialog text. Treated as in-page. |
| Footer Log in | [https://www.pinterest.com/login/](https://www.pinterest.com/login/) **Wall. Branch stopped.** Title: Pinterest Login. |
| Get started here | `#` on the same page. Not followed as a new page. |
| Footer Join Pinterest, Continue creating your Pinterest account, About password requirements, Show password, Open birthdate picker | Signup form controls. **Not used. No fields filled. No form submitted.** |
| Continue with Google | OAuth. **Not clicked.** |
| Terms of Service | [https://policy.pinterest.com/en/terms-of-service](https://policy.pinterest.com/en/terms-of-service) |
| Privacy Policy | [https://policy.pinterest.com/en/privacy-policy](https://policy.pinterest.com/en/privacy-policy) |
| Notice at collection | [https://policy.pinterest.com/en/notice-at-collection](https://policy.pinterest.com/en/notice-at-collection) |
| iOS | Apple App Store. Exit. Not a Pinterest surface. |
| Android | Google Play. Exit. Not a Pinterest surface. |
| Footer Explore | [https://www.pinterest.com/ideas/](https://www.pinterest.com/ideas/) |
| Shop | [https://www.pinterest.com/shopping/](https://www.pinterest.com/shopping/) |
| Help Center | [https://help.pinterest.com/en](https://help.pinterest.com/en) |
| Non-user notice | [https://policy.pinterest.com/en/non-user-notice](https://policy.pinterest.com/en/non-user-notice) |

## Explore (`https://www.pinterest.com/ideas/`)

Public. Title: Explore the best of Pinterest. A login dialog is already mounted (email and password fields present). It is not filled.

| Control | Opens |
|---|---|
| Category tabs: All, Art, Womens Fashion, Beauty, Home Decor, Food And Drink, Quotes, Diy And Crafts, Animals, Design, Weddings, Travel, Mens Fashion, Tattoos | Public idea hubs, for example [https://www.pinterest.com/ideas/art/961238559656/](https://www.pinterest.com/ideas/art/961238559656/). One hub (Art) is captured as the category state. The rest are the same shell. |
| Featured board cards | Public board pages under `/pinterest/<slug>/`. One extra board is captured. |
| Setting | Not opened. Name is an icon control; treated as a settings affordance that may lead to an account wall. |
| Log in / Sign up / Continue with Google / QR code login | **Wall. Not followed.** |
| Forgot password? | [https://www.pinterest.com/password/reset/](https://www.pinterest.com/password/reset/) **Wall. Not opened for typing.** |

## Shop (`https://www.pinterest.com/shopping/`)

Public. Title: Discover shopping inspiration. Category chips link to the same `/ideas/<topic>/<id>/` hubs as Explore. No checkout is reachable signed out.

## Official board and idea pages

These loaded signed out. Each mounts a signup or login dialog. The dialog is recorded and not filled. Save, share-to-account, and pin close-ups that require an account are walls.

| Page | Notes |
|---|---|
| [https://www.pinterest.com/pinterest/your-ultimate-holiday-starter-pack/](https://www.pinterest.com/pinterest/your-ultimate-holiday-starter-pack/) | Official board. Title: Christmas 2026 inspiration. Profile link `/pinterest/`. Share and Close Bottom Right Upsell are on-page controls. Continue with email / Google / QR are walls. |
| [https://www.pinterest.com/food/holiday-mocktails-everyone-will-love/](https://www.pinterest.com/food/holiday-mocktails-everyone-will-love/) | Idea page. Profile link `/food/`. Representative of the other three homepage idea cards (cookies, appetizers, hair and makeup), which use the same shell. |
| [https://www.pinterest.com/pinterest/](https://www.pinterest.com/pinterest/) | Official profile, linked from the board. Public if it loads; account actions stop. |

## About (`https://about.pinterest.com/`)

Public marketing site, a different visual system from the app. Header: Visit Pinterest, Business, Creators, Newsroom, Careers, Investors, Impact, Help Center, Policies, Teen safety, Brand safety, Advertise on Pinterest, Pinterest Academy, Trends tool. Log in and Sign up go to `www.pinterest.com/login/` with campaign query strings. **Those login URLs are walls. Not opened for typing.**

Child marketing hosts recorded, not walked as the product UI: `business.pinterest.com`, `create.pinterest.com`, `newsroom.pinterest.com`, `www.pinterestcareers.com`, `investor.pinterestinc.com`, `ads.pinterest.com`, `www.pinterestacademy.com`, `trends.pinterest.com`, `inspiredinternet.org`.

## Business, Create, Newsroom

| URL | What loaded |
|---|---|
| [https://business.pinterest.com/](https://business.pinterest.com/) | Marketing on Pinterest. Public. |
| [https://create.pinterest.com/en-sg/](https://create.pinterest.com/en-sg/) | Pinterest Create. Public. Geo path `en-sg`. |
| [https://newsroom.pinterest.com/en-sg/](https://newsroom.pinterest.com/en-sg/) | Pinterest Newsroom. Public. Geo path `en-sg`. |

## Help (`https://help.pinterest.com/en`)

Public help home. Article links visible without a search submit: Add a Pinterest widget, Facebook login is going away, Download a Pin as an image, Create a Pinterest account, Create a collage. One article is opened. Search is not submitted.

## Policy (`https://policy.pinterest.com/`)

Public legal pages. Terms of service, privacy policy, notice at collection, non-user notice. Not the product UI. One page (terms) is captured so the footer destination is evidenced.

## Walls (recorded, branch stopped)

| URL or control | Why stopped |
|---|---|
| [https://www.pinterest.com/login/](https://www.pinterest.com/login/) | Asks for email and password. Nothing typed. |
| Header Log in, Sign up, Join, I already have an account | Same email/password/birthday dialogs, sometimes with Google or QR. Nothing typed. Google, Apple, Facebook, QR not clicked. |
| [https://www.pinterest.com/password/reset/](https://www.pinterest.com/password/reset/) | Password reset. Not opened for typing. |
| Continue with Google / Continue with email / QR code login | Account creation or login. Not clicked. |
| Home feed, pin close-up save, boards of a signed-in user, messages, settings, ads manager | Not reachable without an account. Not inferred. |

## Phone width

The same URLs are captured at 390×844. At that width the header keeps Explore (a dropdown), Log in, and a clipped Sign up. Explore's dropdown was not opened: the same control on desktop is a link to `/ideas/`, and the phone Log in and Sign up are the login wall. If a control opens the login or signup dialog, the URL is recorded and that branch stops.

## Refresh note (2026-11-21, same day)

Homepage rechecked signed out. Title still Pinterest. Search focus now mounts the login dialog (email, password, Continue with Google, Continue with QR code), not an empty search modal. Header Log in does the same and also offers a phone scan. `/login/` paints a scannable QR code; that image is not in the package. Google, Apple, Facebook, and QR were not clicked. No field was filled. No form was submitted.
