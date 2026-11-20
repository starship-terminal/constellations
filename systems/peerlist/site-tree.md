# Peerlist site tree

Mapped from https://peerlist.io/ on 2026-11-21 with headed Playwright (Chromium), signed out. Desktop viewport requested 1440×900. A direct navigation often returns Cloudflare "Just a moment..." (HTTP 403) until the challenge clears; after it clears, the same URL returns 200. This map records the page that loaded after the challenge, not the interstitial.

Login and signup are walls. Opening one stops that branch. Nothing was typed into an email, password, phone, username, profile, survey, or newsletter field. No form was submitted. Google was not clicked.

## Shell

Marketing pages (`/`, `/ads`) use a top bar: logo to `/`, Scroll, Jobs, Launchpad, Log in, Create Profile. A hamburger (`button`, no label, `lg:hidden`) is the phone menu; it is not visible at 1440.

App pages (`/scroll`, `/jobs`, `/launchpad`, `/search`, `/blog`, `/github-recap`, `/job-hunt-ai`, `/layoffs-tracker`, a public profile, a company page) use a left rail:

| Control | Opens |
|---|---|
| Scroll | `/scroll` |
| Launchpad (current week link, seen as `/launchpad/2026/week/47`) | that week's launch board |
| Jobs | `/jobs` |
| Search | `/search` |
| Blog | `/blog` |
| Logo / Peerlist | `/` |
| Ads | `/ads` |
| Legal | `https://help.peerlist.io/legal` (off this origin) |
| Log in | `/login` wall |
| Create Profile / signup links | `/signup` wall |
| Change System theme (`aria-label`) | Cycles the `html` class. First click from a light session set `html` class to `dark` and `color-scheme` to `dark`. No menu of Light / Dark / System was mounted in the DOM after the click. |

Footer on the marketing home: Search People (`/search`), Peerlist Blog (`/blog`), GitHub Recap (`/github-recap`), Layoffs Tracker (`/layoffs-tracker`), Project Spotlight (`/project-spotlight`, redirects to `/launchpad`), Job Hunt AI (`/job-hunt-ai`), Privacy (`/legal/privacy-policy`, 404 on this origin), Code of Conduct (`/legal/code-of-conduct`, 404), TnC (`/legal/terms-and-conditions`, 404). The working legal index is `https://help.peerlist.io/legal`.

## Home `/`

| Control | Opens |
|---|---|
| Scroll, Jobs, Launchpad, Log in, Create Profile | those routes (login and signup are walls) |
| Introducing Peerlist Ads | `/ads?utm_source=landing_page` |
| Hero words "Showcase your work,", "launch projects,", "find jobs," | in-page section jumps (buttons, no navigation) |
| Username field + Submit | A claim-username form. Not used. Submitting would start signup. |
| Play | Reveals a YouTube embed (`youtube.com/embed/TRN-jJmiRJg`) in a dialog. Escape closes it. |
| Profile screenshot buttons (`cursor-zoom-in`) | Image zoom. A `dialog` (class includes `modal-scale-in-content`, about 988px wide) was already in the DOM; the click timed out because the control sits below the fold. |
| Avatar marquee links | Public profiles, `/{handle}` (published pages) |
| Download the app! | Stayed on `/`. No dialog text was mounted. Store links were not followed. |
| FAQ questions | In-page disclosure. The first question is not a `button` role Playwright could click by name; answers are in the page text. |
| Create Profile (repeated) | `/signup` wall |

## Scroll `/scroll`

Public feed of posts. Infinite scroll: capture is truncated.

| Control | Opens |
|---|---|
| TRENDING | `/scroll/trending` |
| #show | `/scroll/show` |
| Post | Login dialog on the same URL: "Log in", Continue with Google, email, password, Forgot Password, Create One. Wall. Not submitted. |
| Upvote, comment, follow-style icon buttons | Not clicked after Post proved the auth dialog. Treated as the same wall. |
| Visit | External project URL. Not followed (leaves the product). |
| Author name / avatar | `/{handle}` public profile |
| Project card | `/{handle}/project/{slug}` public project |
| Launch week chip | `/launchpad/2026/week/47` |

## Jobs `/jobs`

| Control | Opens |
|---|---|
| Job row | `/company/{slug}/careers/{role}/{id}` public job post |
| Remote jobs and role chips | `/jobs/role/{role}` (remote, software-engineer, and the other role slugs linked from the page) |
| AI Job Search | `/job-hunt-ai` |
| Search | `/search` |
| Username + Submit (footer claim) | Not used |
| Prev | Pager control. Not submitted. |

## Launchpad `/launchpad`

| Control | Opens |
|---|---|
| Week list | `/launchpad/{year}/week/{n}` (archive from 2024 week 14 onward was linked) |
| Category | `/launchpad/category` and `/launchpad/category/{slug}` |
| Launch | Login dialog on the same URL (same copy as Scroll's Post). Wall. |
| Follow | Not clicked. Same auth dialog expected. |
| Project / builder links | public project or profile |
| Username + Submit | Not used |

`/project-spotlight` redirects to `/launchpad`.

## Search `/search`

Tabs are buttons on the same URL: People (default), Projects, Jobs, Posts. People shows a search input (placeholder "Search people") and filters: Skills and Tools, Match with all the tags, Location, Roles, Company, Clear.

Clicking Projects, Jobs, or Posts did not change the placeholder and left a login dialog mounted ("Continue with Google", Email, Password, Login). Those three tabs are a wall for a signed-out visitor. The search field was not typed into. Location was not opened.

## Ads `/ads`

| Control | Opens |
|---|---|
| See All Placements | In-page. No dialog text after the click. |
| Preview | In-page placement preview. No dialog role with text. |
| Book — from $29 / Book — $199/wk / Book — $149/wk / Book — $99/wk / Book — $129/wk / Book Ad Pro — $404/wk | Booking controls. Not clicked, so a checkout or signup wall was not opened. Recorded as not captured. |

## Blog `/blog`

Index of public posts. A post link opens `/blog/{section}/{slug}` (engineering, commentary, design, jobs-and-interviews, help, changelog). One post was opened: `/blog/engineering/best-email-verification-tools-for-developers-in-2026`. Its page also mounts a Create Profile dialog (Google, password visibility, Create Profile). That dialog is a wall; it was not submitted.

`/blog/design/designing-peerlist-darkmode` and `/blog/engineering/developing-peerlist-dark-mode` are the product's own notes on dark mode. They are articles, not a component spec.

## Tools

| Path | What it is |
|---|---|
| `/github-recap` | Public tool page. Username field + Submit. Not used. |
| `/job-hunt-ai` | Public tool. Prompt field (placeholder is a job-search example) and example chips. Not typed. Chips would run a search; not clicked, to avoid a generated query. |
| `/layoffs-tracker` | Public tracker. Search companies field. Not typed. Year control "2026". |

## Profiles, companies, jobs

| Path | What it is |
|---|---|
| `/{handle}` | Public profile. Home links dozens. One sample, `/kaiser`, is in the capture set. Follow / message, if present, are auth walls and are not submitted. |
| `/{handle}/project/{slug}` | Public project. Linked from Scroll. |
| `/company/{slug}` | Public company page. |
| `/company/{slug}/careers/{role}/{id}` | Public job post. |

## Walls (stop)

| URL | What it asks |
|---|---|
| `/login` | Email, password, Continue with Google, Login, Forgot Password (`/forgot-password`) |
| `/signup` | Email (placeholder is an example address), password, Continue with Google, Create Profile |
| Login dialog on `/scroll` (Post), `/launchpad` (Launch), `/search` (Projects / Jobs / Posts tabs) | Same email / password / Google wall, stays on the page |
| `/forgot-password` | Linked from login. Not opened beyond the link. Password reset is a wall. |

## Not on this origin

| Path | Result |
|---|---|
| `/legal`, `/legal/privacy-policy`, `/legal/code-of-conduct`, `/legal/terms-and-conditions` | 404 on peerlist.io. Footer still links them. Working copy is `https://help.peerlist.io/legal`. |
| `/help`, `/about`, `/pricing`, `/faq`, `/careers`, `/changelog`, `/docs`, `/individuals`, `/companies`, `/bootcamps`, `/people`, `/projects` | 404, or not linked from the home page. Refero lists `/individuals`, `/companies`, `/bootcamps`; those URLs 404 on 2026-11-21. |
| App Store / Play Store | "Download the app!" did not navigate. Store pages were not captured. |

## Themes and widths

Light is the default (`html` class `light`). Dark exists: the theme button sets `html` class `dark`, and `:root` / `.dark` both declare the gray ramp, border, and shadows. Both themes are captured on the app shell pages. Marketing home has no theme button in the header that was measured.

Widths: desktop 1440×900 and phone 390×844, both requested. Sidecars record the measured viewport.
