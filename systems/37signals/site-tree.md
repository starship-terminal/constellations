# 37signals public site tree

Mapped on 2026-11-21 from the live public site, signed out. Official domain confirmed as `https://37signals.com/` (wordmark "37signals", a catalog of numbered signals). Nothing was typed. No identity provider was clicked. No form was submitted.

There is no login or signup wall on this domain. `/login`, `/sign-in`, `/signup`, and `/account` are the same "Page not found" page. The only email field is the jobs notify form. It was photographed empty and not submitted.

`theme.js` picks one of twelve `--rgb-theme-*` colours at random on each visit and writes it to `--rgb-theme` and `sessionStorage`. There is no dark theme and no theme toggle. Screenshots in this package pin `--rgb-theme-3` (`139, 119, 255`) so the set shares one page colour. The live site will not.

Basecamp, HEY, Fizzy, and ONCE are other products. Their links leave `37signals.com`. They are not this package.

## Header

Fixed. On a desktop pointer (min-width 64em, hover, fine pointer) it shows product links. Below that width those links hide and a "Menu" label opens the drawer.

| Control | Opens | Stays on 37signals.com |
|---|---|---|
| 37signals wordmark | `/` | yes |
| Signals | `/` | yes |
| Basecamp | `https://basecamp.com/` | no |
| HEY | `https://www.hey.com/` | no |
| Fizzy | `https://www.fizzy.do/` | no |
| ONCE | `https://once.com/` | no |

Hover and focus on a desktop header link add an underline. The colour does not change.

## Footer

Fixed, same breakpoint as the header.

| Control | Opens | Stays on 37signals.com |
|---|---|---|
| 1999 | `https://1999.37signals.com/` | subdomain, not captured |
| Books | `/books` | yes |
| Thoughts | `/thoughts` | yes |
| Jobs | `/jobs` | yes |
| Updates | `https://updates.37signals.com/` | subdomain, not captured |
| Podcast | `/podcast` | yes. Different visual system |
| Supply | `https://supply.37signals.com/` | subdomain, not captured |
| Dev | `https://dev.37signals.com/` | subdomain, not captured |
| Policies | `/policies` | yes |

## Phone menu

`#nav-active` is a hidden checkbox. The "Menu" label toggles it. When checked, `.nav` paints white and lists the header links, then the footer links. A scrim (`.nav-underlay`, theme colour at 80% opacity) sits behind it. Desktop CSS hides this drawer even if the checkbox is checked.

## Homepage (`/`)

A list of 38 signals, `00` through `37`. Each row is a link to `/00` … `/37`. A white circle at the bottom right (`.controller a`) goes to the next signal (`/00` from the homepage). It is a link, not a dialog. It can be dragged. A click that is held is cancelled. Not dragged here.

## Signal page (`/00` and the same shell for `/01` … `/37`)

Title, essay, and links out to books and other products. The same next-signal circle advances. Left and right arrow keys, and a horizontal swipe, also advance, via `navigate.js`. Those keys were not pressed during capture.

## Pages on this domain

| Path | What it is |
|---|---|
| `/` | Signal index |
| `/00` … `/37` | One essay each. `/00` and `/37` were opened |
| `/books` | Book list. Buy links leave the domain |
| `/thoughts` | Long-form index |
| `/seven-shipping-principles`, `/how-we-make-decisions`, `/why-we-choose-profit`, `/what-influenced-us`, `/how-we-communicate`, `/group-chat-problems` | Essays linked from Thoughts |
| `/jobs` | Empty openings, plus a notify form |
| `/feed/jobs.xml` | RSS. Not a page |
| `/policies` | Policy index |
| `/policies/trust`, `/policies/terms`, `/policies/privacy`, `/policies/privacy/regulations/ccpa`, `/policies/privacy/regulations/ferpa`, `/policies/cancellation`, `/policies/refund`, `/policies/security`, `/policies/accessibility`, `/policies/until-the-end-of-the-internet`, `/policies/taxes`, `/policies/ownership` | Policy documents. Privacy and ownership were opened |
| `/privacy-updates` | Policy changelog |
| `/podcast` and `/podcast/<slug>` | REWORK podcast. White page, Jost and Crimson Pro, not the Lab Grotesque theme |
| `/signup`, `/login`, `/sign-in`, `/account`, `/sitemap.xml` | Page not found. Pink-or-theme field, "Go home" pill |

## Jobs notify form

The only form on the marketing site. It posts to `basecamp.us2.list-manage.com`. Not submitted.

| Control | What it is |
|---|---|
| Email field | Empty. Placeholder `julie.young@hey.com`, the product's own example. Not typed |
| Sign up | Submit button. Not clicked |
| grab the RSS feed | `/feed/jobs.xml` |

## What was not opened

Subdomains (`1999`, `updates`, `supply`, `dev`), Basecamp, HEY, Fizzy, ONCE, Amazon, Bookshop, and the podcast subscribe badges (Apple, Spotify, Overcast, Pocket Casts, Radio Public). Those are other sites.
