# Substack public site tree

Mapped on 2026-11-21 from the live public site, signed out, in an incognito preview tab and then in headless Playwright. Official domain confirmed as `https://substack.com/` (wordmark "substack", hero "Where independent creators publish"). Nothing was typed. No identity provider was clicked. No form was submitted. No subscribe control was followed into an account.

`html` carries `class="dark-mode"` on the logged-out home, Explore, and the sign-in page. About, a publication post, and Privacy paint light. There is no public theme toggle on these pages.

## Auth walls

Photographed empty. Stopped there.

| Control | Opens | Action |
|---|---|---|
| Home "Sign in" | A dialog on `https://substack.com/`, titled "Sign in to Substack" | Empty email field, placeholder "Your email". Continue, and "Sign in with password". No Google, Apple, or other identity button. Not typed. Not submitted. |
| "Create account" inside that dialog | The same dialog's signup copy, then `https://substack.com/onboarding?flow=creator_signup` from "Start your Substack" | Photographed empty. |
| Home "Start your Substack", About "Start publishing", About "Start your Substack" | `https://substack.com/onboarding?flow=creator_signup` | "Create your account". Empty email. Terms checkbox unchecked. Continue is disabled. Not typed. Checkbox not clicked. Not submitted. |
| Signup "Sign in", and `https://substack.com/account/login` | Redirects to `https://substack.com/sign-in?redirect=%2F&change_user=false` | Full-page wall. Empty email. "Sign in with password" is a `#` link, not followed. Continue not clicked. App Store and Google Play badges were not clicked. |
| Explore sidebar Home, Subscriptions, Chat, Activity, Profile | Stay on the Explore shell and show a "Log in or sign up" card | Not entered. |
| Publication "Subscribe" | A subscribe prompt on the post, then an account wall | Closed with Escape. Not subscribed. |
| Leaderboard "+" | Would follow a publication | Not clicked. |

## Logged-out home (`https://substack.com/`)

Desktop header: logo to `/`, then "Sign in" (dialog) and "Start your Substack" (signup wall). A second copy of those two buttons sits at the right of the category row.

Category nav is a horizontal list of links. "All" is `/`. Each other chip is `/?category=<slug>` (culture, technology, business, us-politics, finance, food, sports, art, world-politics, health-politics, fashion, news, music, faith, climate, science, literature, fiction, health, design, travel, parenting, philosophy, comics, international, crypto, history, humor, education, film-and-tv, home-garden, games, beauty, photography). "More categories" scrolls that list. It does not open a page.

Hero link "Start a newsletter, podcast, or video show worth paying for" goes to `/onboarding?flow=creator_signup` (signup wall).

Note cards link to `https://substack.com/note/c-<id>`. Some cards link to a publication post on a `*.substack.com` host or a custom domain. "Load more" appends more public cards. It was not used as a submit.

There is no footer on the logged-out home.

Phone (390): logo, "Sign in", "Get the app". No hamburger. Category chips scroll sideways. "Get the app" opens `/app`.

## Marketing header (About, Privacy, Discover)

Used on `/about`, `/privacy`, `/app`, and the discover page an unknown path falls through to.

| Control | Opens |
|---|---|
| Logo | `/` |
| Resources (click menu) | `/get-started`, `/going-paid-guide`, `/resources`, `/community-and-programs`, `/sponsorships`, Help center on `support.substack.com`, `/brand` |
| Creators (click menu) | `/switch`, `/going-paid`, `/growthfeatures`, a live-video page on `pages.substack.com`, `/video`, `/podcasts`, `/for-bloggers`, `/investing-and-business`, `/book`, `/food-writers`, `/local-news`, `/startups` |
| Explore (click menu) | `/app`, `/explore`, Featured on `on.substack.com/s/stories`, `/globe` |
| Search field | Stays on the page. Not typed. |
| Start publishing | `/onboarding?flow=creator_signup` (signup wall) |
| Sign in | Sign-in dialog or `/sign-in` (auth wall) |

## Footer (About, App, Privacy)

Columns linked from `/app` and repeated on the marketing pages:

- Discover: Explore (`/explore`), Get the app (`/app`), Substack Reader (`reader.substack.com`), Top podcasts and Top in culture, food, finance, sports, politics, technology, faith, business (`/leaderboard/<topic>/paid`), Topics (`/topics`).
- Creators: Switch (`/switch`), Get started (`/get-started`), Go paid (`/going-paid`), Sponsorships, For video, For podcasts, For bloggers, For finance writers, For authors, For food writers, For local news, For media founders.
- Company: About (`/about`), Help (`support.substack.com`), Jobs (`/jobs`), Blog (`on.substack.com`), Vulnerability Policy (`/vulnerability-disclosure`).
- More: Contact, Sitemap, Resource center, Guide to going paid, Help center, Community and programs, Brand assets, Features, comparison pages (`/substack-vs-patreon` and the same pattern for other products).
- Legal: Privacy (`/privacy`), Terms (`/tos`), Collection notice (`/ccpa`).

External and not treated as pages of this product: App Store and Google Play badges, Help Center on `support.substack.com`.

## Pages opened

| Page | What it is |
|---|---|
| `/` | Logged-out discovery home. Dark. |
| `/?category=technology` | Same home, Technology chip selected. |
| `/about` | Creator marketing. Light. Hero in Cahuenga. Earnings estimator is two native selects, not submitted. |
| `/app` | App marketing. A download dialog offers "Send link". Closed. The phone field was not typed. |
| `/explore` | Reader shell, signed out. A login card sits in the rail. |
| `/search` | Redirects to `/explore`. |
| `/leaderboard/technology/paid` | Public bestseller list. "+" not clicked. |
| `/discover` | Redirects to `/explore`. |
| A public post, `https://www.oneusefulthing.org/p/fable-52-and-jagged-agi` | Loads without an account. Subscribe prompt closed. |
| `/privacy` | Privacy policy, light, with a documents list. |
| `/sign-in` | Login wall. Empty. |
| `/onboarding?flow=creator_signup` | Signup wall. Empty. Continue disabled. |
| An unknown path | Falls through to a public "Discover world class culture" page, not a 404. |

## Phone

390 x 844. Homepage and About. About's header uses a menu button (three lines) plus "Start publishing" and "Sign in". The homepage does not.
