# Portrait public site tree

Mapped from https://portrait.so/ on 2026-11-21, signed out, in headless Chrome at 1440 by 900. The request returned 200. The page title was "Portrait – Your forever space for everything you are." This is a live marketing site, not a parked domain. The page paints light (`rgb(247, 247, 247)`, `data-mode="light"`).

No email was typed. No password was typed. No code was typed. No phone or address was typed. No form was submitted. Sign in with Portrait Wallet, Sign in with email, and Sign in with other wallet were not clicked. Apply for early access was not followed. The editor Login button was not clicked.

## Header

A sticky bar holds the wordmark, one announcement link, Log in, Sign up, and a Menu button. Menu is in the DOM at desktop width and stays `aria-expanded="false"` after a click at 1440. At 390 it opens a drawer.

| Control | Opens | Stop? |
|---|---|---|
| Portrait (wordmark) | `/` | |
| New / Introducing Portrait Wallet | `/#wallet` on home. On Wallet, Pay, Blog, Points and Hosting the same chip points at `/wallet` | |
| Log in | A dialog on the current page. Title "Sign in". The URL stays `/` | Stop. Empty wall only |
| Sign up | The same Sign in dialog. There is no separate signup form | Stop. Empty wall only |
| Menu | At 390, a drawer with Home and Introducing Portrait Wallet. Close is the same button, then labelled with an X | Opened on the phone homepage, then closed |

## Homepage

`/` is one long page, about 9938 px at 1440. Sample names in the hero carousel (david, marie, Rowan Blake, and the rest) are the site's own copy.

| Control | Opens | Stop? |
|---|---|---|
| Username field | Empty field, placeholder "username", label "Choose your username" | Nothing typed |
| Sign up (inside the username row) | The same Sign in dialog | Stop. Not followed |
| Already have a Portrait? Log in | The same Sign in dialog | Stop. Not followed |
| Portrait Wallet / Get early access now | `/#wallet` | |
| Apply for early access | Not followed. The button sits in the wallet section | Stop |
| Donate, Image, Video, Link, Text | Painted demo controls on the page. Not a signed-in editor | Not used as a form |
| FAQ questions | Same page. "What is Portrait?" and "How much does it cost?" were open. The cost answer says creating a Portrait is free, and Plus is $10/month | |
| Create your Portrait | Present in the page copy as a dark pill on inner sections. On this visit the homepage matcher landed on Apply for early access first | Not followed into `/editor` |

## Product pages

These share the same header and footer. Each returned 200.

| Control | Opens |
|---|---|
| Pages | `/pages`. Title "Portrait Pages". Example portraits (`/ryan`, `/naomi`, and the rest) are public profile links. Not opened |
| Wallet | `/wallet`. Title "Portrait Wallet". Apply for early access and "Already have access? Log in" sit on the page. Neither was followed |
| Pay | `/pay`. Title "Portrait Pay". "Log in to create links" was not clicked. The chat and the $25 request are painted demos |
| Hosting | `/hosting`. Title "Portrait – Hosting". Download hosting app points at GitHub. Not opened |
| Blog | `/blog`. Title "Portrait – Blog" |
| A blog post | `/blog/portrait-is-now-free-for-everyone`. Title "Portrait is now free for everyone \| Portrait Blog" |
| Points | `/points`. Title "Portrait – Points". Dashboard is the selected tab. Leaderboard is labelled "(soon)". Counts show 0. "Sign up or log in" was not clicked. Connect with X is locked |

## Footer

The footer is a link list, not a menu.

| Group | Items | Stop? |
|---|---|---|
| Product | Overview `/`, Pages `/pages`, Wallet `/wallet`, Pay `/pay` | |
| Support | Report abuse `mailto:abuse@portrait.so`, Report bug `mailto:bugs@portrait.so` | Mailto. Not opened |
| Resources | Blog `/blog`, Points `/points`, Open Internet Protocol `https://openinternetprotocol.com`, Brand Kit `https://github.com/portraitgg/portrait-brand-kit` | Off-site links not opened |
| Developers | GitHub `https://github.com/portraitgg/`, Docs `https://learn.portrait.so`, Smart Contracts `https://github.com/portraitgg/portrait-contracts-public` | Not opened |
| Hosting | Overview `/hosting`, Hosting for Mac and Hosting for Windows, both `https://github.com/portraitgg/portrait-hosting-app` | Not opened |
| Socials | X.com, Farcaster, Bluesky, Discord | Not opened |
| Legal | System status `https://status.portrait.so`, Privacy and Terms on `media.portrait.host` | Not opened |

## Login and signup walls

Log in and Sign up both open one dialog on the current page. It is 420 by 277 px, white, radius 16 px. The fields are empty. There is no email field until Sign in with email is clicked, and that button was not clicked.

| Control | What it is | Stop? |
|---|---|---|
| Close | Closes the dialog. Escape also closes it | Closed after the shot |
| Sign in with Portrait Wallet | Identity provider | Not clicked |
| Sign in with email | Opens an email step | Not clicked. Nothing typed |
| Sign in with other wallet | Identity provider | Not clicked |

`/login` returned the homepage and did not open the dialog by itself. `/signup` is treated as a username and shows the missing-user page ("Uh oh / This user does not exist."). `/pricing` and `/plus` show the same missing-user page. There is no public pricing URL. Plus is a section on the marketing pages, priced at $10/month in the FAQ.

`/editor` shows a signed-out wall: "You are not logged in" and a Login button. The button was not clicked.

## Mobile

At 390 the header keeps Log in and Sign up and replaces the announcement row with Menu. Menu opens a drawer with Home and Introducing Portrait Wallet. Wallet was also photographed at 390.

## Not entered

The editor, wallet connect, email code, Apply for early access, checkout, and any signed-in chrome. This pass stopped at the empty Sign in dialog and the empty editor wall. `login-extracted` stays `not-started`.
