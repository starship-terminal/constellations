# Playbook public site tree

Mapped from https://www.playbook.com/ on 2026-11-21, signed out, in headless Chromium at 1440×900. `https://playbook.com` redirects to `https://www.playbook.com/`. The homepage returned 200. The title was "Playbook | File infrastructure for every app and team". This is a live marketing site, not a parked domain.

No email, password, code, phone or address was typed. No form was submitted. Continue with Google and Continue with Apple were not clicked. The language control was not opened. `login-extracted` stays `not-started`.

The T3 preview tab loaded the homepage and could read the DOM. It could not produce screenshot frames (`The browser is not producing screenshot frames`). The shots below were taken in headless Chromium on pages that had already loaded with no challenge.

## Header

The home header is a dark bar: wordmark, MCP (with a New badge), Developers, Solutions, Resources, Pricing, a language button, Schedule a demo, and Get started. Solutions and Resources are hover menus, not routes. The language button (`aria-label="Change language"`) is in the DOM and was not opened.

| Control | Opens | Stop? |
|---|---|---|
| Wordmark | `/#marketing-home` | |
| MCP | `/mcp/` | |
| Developers | `https://dev.playbook.com/` in a new tab | public docs host, not entered past the link |
| Solutions | Hover menu on the same page | |
| Resources | Hover menu on the same page | |
| Pricing | `/pricing/` | |
| Language | A menu of locale routes (`/de/`, `/es/`, `/fr/`, `/hi/`, `/it/`, `/ja/`, `/ko/`, `/nl/`, `/no/`, `/pt-BR/`, `/pt-PT/`, `/vi/`, `/zh/`, `/zh-Hant/`, and `/` for English) | not opened |
| Schedule a demo | `/contact/` | empty form, not submitted |
| Get started | `/login/`, which redirects to `/sign-in` | yes, empty wall |

On a 390-wide viewport the text links hide. A hamburger opens a drawer. Schedule a demo is inside that drawer, not in the collapsed bar.

## Solutions menu

Opened by hovering Solutions. It is a panel titled "Use cases", not a route.

| Item | Opens |
|---|---|
| Enterprise Marketing | `/enterprise/` |
| Media & Entertainment | `/media-and-entertainment/` |
| Creative Agency | `/creative-agency/` |
| Consumer Brands | `/consumer-brands/` |
| Game Studios | `/games/` |

## Resources menu

Opened by hovering Resources. It is a panel titled "Resources".

| Item | Opens |
|---|---|
| Help center & tutorials | `/tutorial/` |
| Customer stories | `/customers/` |
| Portfolio showcase | `/s/community/portfolioshowcase` |
| Free giveaway | `/s/community/illustrations` |
| About us | `/p/about-us/` |
| Story of Playbook | `/the-story-of-playbook/` |
| Blog | `/blog/` |
| Privacy & ownership | `/blog/artist-privacy-and-ownership/` |
| Browse template gallery | `/s/community/template-gallery` |

The community and customer-story routes were mapped and not each photographed. One sample of the marketing template (`/customers/`, `/blog/`, `/about-us/`) was photographed.

## Phone drawer

At 390px the bar is the wordmark, Get started, and a hamburger. The drawer lists Schedule demo, Get started, MCP, Developers, Solutions, Resources, and Pricing. Solutions expands in place to Enterprise, Media & Entertainment, Creative agency, Consumer brands, and Game studios. Resources expands to the same items as the desktop menu. Escape is the close control (×).

## Home interactions that stay on `/`

| Control | Opens | Stop? |
|---|---|---|
| Prompt chips (Build a review portal, Tag Dropbox photos, Resize for the web, Add an uploader, Host a website) | Fill the prompt on the same page | not clicked, nothing typed |
| Send (arrow in the prompt) | Would start a prompt | not clicked |
| Read the docs | `https://dev.playbook.com/docs/getting_started` | not followed |
| Book a demo | `/contact/` | empty form, not submitted |

## Footer

The footer is on the home page. Groups are the labels as painted.

| Group | Items |
|---|---|
| Product | Digital asset management `/features/`, Playbook Intelligence `/launch/`, MCP for creative teams `/mcp/`, Developer API `https://dev.playbook.com/docs/getting_started/`, Tools and integrations `/integrations-all/`, Pricing `/pricing/` |
| Playbook for | Enterprise `/enterprise/`, Media and entertainment `/media-and-entertainment/`, Creative agencies `/creative-agency/`, Consumer brands `/consumer-brands/`, Game studios `/games/` |
| Resources | Blog `/blog/`, Customer stories `/customers/`, Help center `/tutorial/`, Discord community `https://discord.com/invite/MKpZvuvqg3`, For students `/school/` |
| Company | About us `/about-us/`, Story of Playbook `/the-story-of-playbook/`, Contact us `/contact/` |
| Comparisons | Playbook vs Plytix, vs Air, vs Tagbox, vs Dropbox, vs Google Drive (blog posts) |
| Legal | Terms `/terms/`, Privacy `/privacy/`, Consent Preferences (same-page control, not clicked), Platform Status `https://status.playbook.com/` |
| Social | Instagram, LinkedIn, X (`playbook_hq`) |

Inner pages such as `/blog/` and `/contact/` paint a different bar: Product, API/SDK, Solutions, Resources, Pricing, Schedule a demo, Get started for free. Product and API/SDK are menus on those pages. They were not opened. Get started for free goes to the same `/login/` wall.

## Auth walls

Photographed empty. Nothing was typed. Google and Apple were not clicked. Continue with email stayed disabled. The EN language control on the wall was not opened.

| Control | Opens | What it shows |
|---|---|---|
| Get started | `/login/` then `/sign-in` | "Log in or sign up". Google, Apple, an empty work-email field, Continue with email disabled. |
| `/sign-in` | Same page | Same wall. |
| `/sign-up` | `/sign-up` | Same wall, same heading. Signup is not a separate form. |
| `/signup` | `/signup/sign-in` | Same wall. |
| `/register` | Same wall | Same heading. |

The right half of the desktop wall is a published sample collage. It is marketing art, not an account.

## Contact

`/contact/` is a public demo form: work email, team size, location, what you are looking for, how you heard about Playbook, and a disabled Submit. Every field was empty. Nothing was typed. Submit was not clicked. Take a product tour and Read customer stories sit beside the form and were not followed.

## Phone

Home and pricing were photographed at 390×844. Login and signup were photographed at that width and left empty. The home drawer was opened and Solutions was expanded.

## Not entered

Signed-in app, identity providers, the language menu, community boards (`/s/community/…`), `dev.playbook.com`, Discord, status, social profiles, checkout, and any form submit.
