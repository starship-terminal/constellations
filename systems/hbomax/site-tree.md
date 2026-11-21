# HBO Max public site tree

Mapped on 2026-11-21 from the signed-out homepage, before screenshots. `https://www.hbomax.com/` geo-redirected to `https://www.hbomax.com/sg/en` (title: "HBO Max | Watch Better"). One painted theme (`data-theme="max"`, page ground `rgb(18, 12, 29)`). A Cookie Preferences dialog is up on arrival. Stopped at sign-in, subscribe, and create-account.

## Header

| Control | Opens |
|---|---|
| Logo | `/sg/en` (this page) |
| Sign In | `https://auth.hbomax.com/login`. Wall. Not entered. |
| Subscribe Now | `https://auth.hbomax.com/product`. Wall. Not entered. |
| Skip To Content | Skips to the main content on this page |

## Cookie Preferences

Dialog on this page, labelled "PRIVACY Modal". Not accepted. Not saved.

| Control | Opens |
|---|---|
| Affiliates | `https://hbomax.com/affiliates` |
| Privacy Policy | `https://hbomax.com/privacy` |
| Accept All | Closes the dialog. Not clicked. |
| Manage Cookies | Second step of the same dialog: "Manage Cookie Preferences", one checkbox "Third-Party Targeting Cookies", and Save Preferences. Not ticked. Not saved. |

## Hero

| Control | Opens |
|---|---|
| GET HBO MAX | `https://auth.hbomax.com/product`. Wall. Not entered. |

## Plans

Stays on `/sg/en` until Select Plan.

| Control | Opens |
|---|---|
| Bundle | Billing period on this page |
| Monthly | Billing period on this page |
| Yearly Save up to 25% | Billing period on this page |
| Select Plan | `https://auth.hbomax.com/create-account` with a price plan id. Wall. Not entered. |

## Body rails

Title cards stay on `www.hbomax.com`. Carousel arrows stay on this page.

| Control | Opens |
|---|---|
| What's New cards | `/sg/en/movie/<id>` or `/sg/en/show/<id>` |
| Discover The Best Of, Previous / Next Carousel Slide | Scrolls the rail on this page (`/#`) |
| Groundbreaking Series, Blockbuster Movies, Iconic Hits, Real-life Stories, Family Favorites | `/sg/en/show/<id>` or `/sg/en/movie/<id>` |
| GET THE BUNDLE | `https://www.hbomax.com/bundle/viu`, which redirects to `/sg/en/bundle/viu` and returned 404 on 2026-11-21. Not photographed. |
| FAQ questions (What is the HBO Max & Viu Bundle?, and six more) | Accordion on this page. Not submitted. |

## Footer

| Control | Opens |
|---|---|
| English | Listbox on this page: English, Bahasa Melayu, 简体中文. A language was not chosen. |
| Explore What's On | `/sg/en/sitemap` |
| Movies | `/sg/en/movies` |
| TV Shows | `/sg/en/shows`, which redirects to `/sg/en/series` |
| Brands | `/sg/en/channel` |
| Kids and Family | `/sg/en/collections/genre/kids-family` |
| Accessibility | `/accessibility-statement` |
| Privacy Policy | `/privacy`, which redirects to `https://www.wbdprivacy.com/policycenter/b2c/` |
| Children's Privacy Policy | `/privacy/children` |
| Terms of Use | `/terms-of-use` |
| Manage Cookies | Same cookie dialog as the header (`/#`). Not saved. |
| Join the Team | `https://careers.wbd.com/global/en`. Left the product. Not followed. |
| Corporate Information | `/sg/en/corp-info` |
| Help | `https://help.hbomax.com/`. Left the product. Not followed. |

## Phone (390)

Sign In and Subscribe only in the header. Subscribe is the short label for the same `auth.hbomax.com/product` wall. No hamburger.

## Pages photographed from this tree

Public, no login: home (default, cookie dialog, manage-cookies step, language list, yearly plan), `/sg/en/movies`, `/sg/en/series` (the TV Shows link), `/sg/en/channel`, one public title card, `/sg/en/sitemap`, `/sg/en/corp-info`, the privacy redirect. Desktop 1440 and phone 390 for home.

Not entered: Sign In, Subscribe Now, GET HBO MAX, Select Plan, Accept All, Save Preferences, language choice, careers.wbd.com, help.hbomax.com, Google, Apple, any identity provider, any form. `/sg/en/bundle/viu` returned 404 and was not kept. The FAQ click opened, then the cookie dialog covered the answer, so the 2026-11-17 FAQ shot stays.
