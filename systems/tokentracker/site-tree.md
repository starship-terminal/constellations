# Token Tracker public site tree

Mapped on 2026-11-22 from `https://www.tokentracker.cc/` in a signed-out browser, then photographed in headless Chromium. The homepage returned 200. The title was "Token Tracker — AI Token Usage & Cost Tracker for Coding CLIs". The visible heading was "TRACK EVERY AI TOKEN". This is a live marketing site, not a parked domain.

The existing package slug is `tokentracker`. origin/main already had `systems/tokentracker/`. This pass refreshes that package with the public site. It does not add a second package.

`https://tokentracker.app` answers 301 to `https://ivan.dev` and is not this product. `https://tokens.studio` is Tokens Studio, a different product. The live URL used here is `https://www.tokentracker.cc/`. The catalog entry on origin/main names `https://github.com/xiufengsun/TokenTracker` and the local CLI dashboard. catalog.json was left alone.

The painted marketing field is dark. `html` has class `dark`. `color-scheme` is `dark`. The page surface resolves `--lv3-bg` to `#050507`. There is no theme switch on the homepage. The Cloud shell has a Theme menu (Light, Dark, System). That menu was opened and closed. The theme was not changed.

Nothing was typed. No password was typed. No email was typed. No phone number was typed. No address was typed. No form was submitted. GitHub and Google were not clicked. No captcha was solved. The signed-in dashboard was not entered. `login-extracted` stays `not-started`.

The public leaderboard lists other people's names, photos, and GitHub profiles. It was mapped and not photographed. Status (`https://tokentracker.statuspage.io/`) is off product and was not captured.

## Homepage

`https://www.tokentracker.cc/` is the marketing page. Status 200.

Desktop nav: wordmark "TOKEN TRACKER", a Star link, Cloud, Leaderboard, and an empty dark control in the top right (no visible label at 1440). Phone width (390) keeps the wordmark and a Sign in button. Cloud and Leaderboard hide.

| Control | Opens | Stop? |
|---|---|---|
| Wordmark "TOKEN TRACKER" | `/login` | Yes. Login wall. Photographed empty. |
| Star (count) | `https://github.com/xiufengsun/TokenTracker` | Off product. Not captured. |
| Cloud | `/cloud` | No. Public pricing. |
| Leaderboard | `/leaderboard` | No. Public table. Names and photos, so not photographed. |
| Sign in (phone, and on `/landing`) | Dialog on the same page: Continue with GitHub, Continue with Google, Continue with Email | Yes. Empty wall. Identity providers not clicked. |
| Copy command | Stays on the page. Copies `npx --yes tokentracker-cli`. | No. Hover only. Not a form. |
| Download for macOS | GitHub release `TokenTrackerBar.dmg` | Off product. Not opened. |
| Windows | GitHub release `TokenTracker-Setup.exe` | Off product. Not opened. |
| GitHub | `https://github.com/xiufengsun/TokenTracker` | Off product. Not captured. |
| Footer Cloud | `/cloud` | No. |
| Footer Status | `https://tokentracker.statuspage.io/` | Off product. Not captured. |
| Footer GitHub | `https://github.com/xiufengsun/TokenTracker` | Off product. Not captured. |
| Footer Cloud pricing | `/pricing.html` | No. Public. |
| Footer Terms of Service | `/terms.html` | No. Public. |
| Footer Privacy | `/privacy.html` | No. Public. |
| Footer Support | `mailto:rynnsun0509@gmail.com` | Not opened. |

The page continues below the hero: how it works, an install command, supported tools, FAQ, and a resource list. Those sections are in the full-page shot. No menu, drawer, or dialog sits on the desktop homepage.

## Landing

`https://www.tokentracker.cc/landing` is the same marketing page with a fuller nav: Cloud, Leaderboard, Dashboard, Sign in. `#download` is the install block on that page.

| Control | Opens | Stop? |
|---|---|---|
| Dashboard | `/dashboard`, which redirects to `/login` | Yes. Login wall. |
| Sign in | Dialog on the same page | Yes. Empty. Photographed. Escape closes it. |

## Cloud

`https://www.tokentracker.cc/cloud` is public. Heading "Choose your plan". Local free and TokenTracker Cloud ($4.99 / month, $39.99 / year). Signed-out shell with a sidebar.

| Control | Opens | Stop? |
|---|---|---|
| Sign in | Dialog on the same page | Yes. Empty. Photographed. Not submitted. |
| Collapse sidebar | Stays on the page. Sidebar folds. | No. Photographed. |
| Theme | Menu: Light, Dark, System | Opened and closed. Theme not changed. |
| Monthly / Yearly | Stays on the page. Switches the Cloud price. | No. Both photographed. |
| Try free for 7 days | Would start a Cloud trial. | Yes. Not clicked. |
| Use the free app | `/landing#download` | No. Marketing install block. |
| FAQ summaries (What does Cloud include?, and five more) | Expand on the same page | One opened and photographed. |
| Read deployment guidance | `/self-host` | No. Public. |
| Tokens | `/dashboard` | Yes. Redirects to login. |
| Sessions | `/sessions` | Yes. Login wall. |
| Limits | `/limits` | Yes. Login wall. |
| Leaderboard | `/leaderboard` | Public table. Not photographed. |
| Achievements | `/achievements` | Yes. Login wall. |
| Menu Bar & Widgets | `/widgets` | Yes. Login wall. |
| Pet | `/pet-settings` | Yes. Login wall. |
| Skills | `/skills` | Yes. Login wall. |
| Claude IP Check | `/ip-check` | Yes. Login wall. |
| Service Status | `/service-status` | Yes. Login wall. |
| Settings | `/settings` | Yes. Login wall. |
| Star | GitHub | Off product. Not captured. |

On a 390-wide viewport the sidebar hides. A hamburger sits in the top bar. The plan cards stack. The hamburger was not used to enter a signed-in page.

## Self-host

`https://www.tokentracker.cc/self-host` is public. "Back to Cloud plans" returns to `/cloud`. Body is a technical preview of a private InsForge deploy. Same signed-out shell as Cloud. Sidebar links stop at the same walls.

## Pricing, terms, privacy

| URL | What it is |
|---|---|
| `/pricing.html` | "TokenTracker Cloud pricing". Free local use, Cloud description, a price table (Monthly Cloud USD 4.99, Annual Cloud USD 39.99). Wordmark returns to `/`. |
| `/terms.html` | Terms of Service. Version 1.0, effective 8 October 2026. |
| `/privacy.html` | Privacy Policy. Last updated 2026-10-08. |

These three are static documents. They have no menus or dialogs.

## Share

`https://www.tokentracker.cc/share` with no share id renders the same marketing page as `/landing`, including Sign in and Dashboard. It is not an empty share state. A share id was not requested.

## Leaderboard

`https://www.tokentracker.cc/leaderboard` is public. Heading "AI coding token usage leaderboard". Week, Month, and All stay on the page. A sign-in dialog opens on load and from "Sign In". Escape closes it. The dialog is the same empty wall as login (GitHub, Google, Email). It was photographed with the table behind it, then discarded: the table shows other people's names and photos. Rows-per-page and pagination stay on the page. A row's GitHub link leaves the product. Not clicked.

## Login wall

`https://www.tokentracker.cc/login` is the wall. "Back to home" returns to `/`.

| Control | Opens | Stop? |
|---|---|---|
| Continue with GitHub | Identity provider | Yes. Not clicked. |
| Continue with Google | Identity provider | Yes. Not clicked. |
| Continue with Email | Reveals empty Email and Password fields, plus Forgot password? | Fields left empty. Photographed. |
| Sign in / Create account | Switches the empty email form. Create account adds an empty Display name field ("Optional"). | Photographed empty. Create account was not submitted. |
| Forgot password? | Would start a reset. | Not followed into a submitted reset. |
| Sign in with email / Create account (submit) | Would submit the form. | Yes. Not clicked. |

`/signup`, `/sign-up`, `/register`, and `/forgot-password` do not have their own walls. Each returns the marketing homepage. Account creation lives on the login card after Continue with Email.

## App routes that stop

These URLs return 200 and then the client sends a signed-out browser to `/login`. The wall was photographed once. The routes were not entered.

`/dashboard`, `/sessions`, `/limits`, `/achievements`, `/widgets`, `/pet-settings`, `/skills`, `/ip-check`, `/service-status`, `/settings`.
