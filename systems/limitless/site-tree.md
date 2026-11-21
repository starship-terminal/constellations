# Limitless public site tree

Mapped from https://www.limitless.ai/ on 2026-11-21, signed out. `https://limitless.ai` returns 308 to `https://www.limitless.ai/`. The homepage returned 200. The title was "Limitless". The first heading was "Limitless has been acquired by Meta". This is a live marketing site, not a parked domain.

There is no theme switch. `color-scheme` on the root was `normal`. No email was typed. No password was typed. No phone number was typed. No address was typed. No form was submitted. No identity provider was clicked. `login-extracted` stays `not-started`.

## Consent banner

An Enzuzo banner sits over the page. It is not a page. It was hidden with CSS for screenshots. None of its controls were clicked.

| Control | What it does | Stop? |
|---|---|---|
| Privacy Policy | Opens `/privacy-policy` | |
| Terms of Service | Opens `/terms` | |
| Decline | Records a consent choice | Not clicked |
| Allow All | Records a consent choice | Not clicked |
| Save & Accept | Records a consent choice | Not clicked |
| Manage Cookies | Opens the preference dialog on the same page | Not clicked |
| Close | Dismisses the banner | Not clicked |

## Header

The wordmark, five items, and Sign In sit in the top bar. Home, Privacy, Developers, and About are links. Solutions is a menu button (`aria-haspopup="menu"`).

| Control | Opens | Stop? |
|---|---|---|
| Limitless (wordmark) | `/` | |
| Home | `/` | |
| Solutions | A menu on the same page. It is not a route | |
| Privacy | `/privacy` | |
| Developers | `/developers` | |
| About | `/about` | |
| Sign In | `https://app.limitless.ai/`, which redirects to `/signin` | Stop. Empty wall only |

On a 390-wide viewport the text links hide. A hamburger opens a drawer.

## Solutions menu

Opened from the header button. Groups are labels, not links.

| Group | Item | Opens |
|---|---|---|
| By use case | Voice Recorder | `/for/voice-recorder` |
| By use case | Life Coach | `/for/life-coach` |
| By use case | Personalized AI | `/for/personalized-ai` |
| By role | Parents | `/for/parents` |
| By role | Patients | `/for/patients` |
| By role | Students | `/for/students` |
| By job | Executives | `/for/executives` |
| By job | Journalists | `/for/journalists` |
| By condition | ADHD | `/for/adhd` |
| By condition | Dementia | `/for/dementia` |
| By condition | Alzheimer's | `/for/alzheimers` |

Escape closes the menu. Each item is a public marketing page.

## Mobile drawer

| Control | Opens | Stop? |
|---|---|---|
| Home | `/` | |
| Privacy | `/privacy` | |
| Developers | `/developers` | |
| About | `/about` | |
| Sign In | `https://app.limitless.ai/` | Stop |

## Homepage

The page is an acquisition letter from Dan Siroker. In-page links:

| Control | Opens | Stop? |
|---|---|---|
| export all of your data | `https://help.limitless.ai/en/articles/13004987-how-to-download-your-limitless-transcripts-and-account-info` | Public help article. Not opened in this pass |
| delete all of your data | `https://help.limitless.ai/en/articles/13005203-how-to-delete-your-limitless-account-and-data` | Public help article. Not opened. Account deletion was not started |
| Sign in | `https://app.limitless.ai/` | Stop |

## Footer

| Group | Items |
|---|---|
| Product | Home (`/`), Developers (`/developers`) |
| Company | About (`/about`), Careers (`/careers`), Privacy (`/privacy`) |
| Resources and support | Help Center (`https://help.limitless.ai/`), Support (`/support`), Community (`/community`) |
| Social | X, YouTube, LinkedIn, TikTok, Instagram. Off-site. Not opened |
| Apps | App Store and Google Play badges. Off-site. Not opened |
| Legal | Terms (`/terms`), Privacy Policy (`/privacy-policy`), Cookie Policy (`/privacy`), Manage Cookies |

`/community` redirects to a Slack invite. The invite said the link is no longer active. It was not followed into account creation.

Careers has "View open roles". That link leaves the site for Ashby. It was not followed.

## Pricing

`/pricing` returns 404. The page title is "404: This page could not be found." There is no public pricing page.

## Login wall

Sign In lands on `https://app.limitless.ai/signin`. The title is "Limitless". The form is empty.

| Control | What it is | Stop? |
|---|---|---|
| Continue with Google | Identity provider button | Not clicked |
| Continue with your email | Empty email field | Focused only. Nothing typed |
| Privacy Policy | `/privacy-policy` | |

`https://app.limitless.ai/` redirects to the same wall.

## Signup wall

There is no separate signup form. `https://app.limitless.ai/signup` returns a public "Page not found" with a Home link. `/signup`, `/login`, and `/signin` on `www.limitless.ai` are marketing 404s. Nothing was typed. Nothing was submitted.

## Help

`https://help.limitless.ai/en/` returned 200. Title: "Home | Limitless Help Center".

| Control | Opens | Stop? |
|---|---|---|
| Search for articles | Empty search field | Not submitted |
| Getting Started, Pendant, and other collections | Public help collections | Not opened in this pass |
