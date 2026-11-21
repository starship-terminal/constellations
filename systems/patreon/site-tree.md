# Patreon public site tree

Mapped on 2026-11-20 from `https://www.patreon.com/` in headless Chromium before any package screenshots. Desktop probe 1440×900. Phone probe 390×844 opened the same logged-out app home and its navigation sheet.

A fresh context sometimes lands on the logged-out app (`Home | Patreon`) and sometimes on the marketing homepage (`Where Creator Communities Thrive — Patreon`). Both are public. The tree below records which control opens which page, menu, dialog, or wall. Branches that open a login or signup wall were recorded and not followed.

No password, code, email, or phone was typed. No form was submitted. Google, Apple, and Facebook controls were not clicked. Cookie banners were not accepted or rejected.

## Logged-out app home

URL: `https://www.patreon.com/` when the title is `Home | Patreon`.

Visible chrome: Skip navigation, logo (Go to home page), Home, Explore, Chats, Notifications, Create on Patreon, Account menu. The feed shows public posts, interest chips, and per-post Join, Play, Like, comments, Reshare, and Share.

| Control | Opens | Followed |
|---|---|---|
| Logo / Home | `https://www.patreon.com/` | yes |
| Explore | `https://www.patreon.com/explore` | yes |
| Chats | Login wall over the same URL. Email and password fields appear. | stopped |
| Notifications | Same login wall. | stopped |
| Create on Patreon | `https://www.patreon.com/create` (title `Sign up \| Patreon`). Password field, Continue with Apple, Continue with Facebook. | stopped |
| Account menu | Dialog labelled "Your account". | yes, dialog only |
| Account menu → Sign up | `https://www.patreon.com/login` | stopped |
| Account menu → Log in | `https://www.patreon.com/login` | stopped |
| Account menu → Light / Dark / System | Appearance on the current page. Dark was opened once, then System restored. | yes |
| Account menu → Support | `https://support.patreon.com/hc/en-us` | yes |
| Account menu → Terms of Use | `https://www.patreon.com/policy/legal` | yes |
| Account menu → Privacy Policy | `https://privacy.patreon.com/policies` | yes |
| Account menu → Community Policies | `https://www.patreon.com/policy` | yes |
| Share on a public post | Menu: Copy link, Share on X, Share on Facebook. Social share links were not opened. | menu only |
| Join on a post | Login wall (email and password) over the home URL. | stopped |
| Like, comments, Reshare | Not opened. These actions belong to a signed-in member. | not captured |
| Get the app (in the phone sheet) | `https://www.patreon.com/?display_app_qr=1` | yes |
| Creator name or "Link to creator's page" | `https://www.patreon.com/<vanity>` or `/cw/<vanity>` | one public creator |
| Post title or timestamp | `https://www.patreon.com/<vanity>/posts/<id>` | one public post |
| Interest chip (Filmmaking & analysis, Fantasy fiction, Fan fiction, TTRPG, Digital art, Anime & manga, Financial analysis, Simulation games, International relations, Self improvement) | `https://www.patreon.com/index-v2/interests/<slug>` | yes. A desktop load of these URLs often redirects to the marketing homepage. A mobile load of Digital art stayed on the interest feed. |

### Phone sheet

`Open navigation` (aria-expanded false until opened) opens a sheet. Close dismisses it. The sheet lists Home, Explore, Chats, Notifications, Create on Patreon, then Resources (Support, Features, Pricing, Patreon for Creators), Company (About, Press, Careers, Terms of Use, Privacy Policy, Community Policies), Get the app, and "Log in or create an account" (`https://www.patreon.com/login`, stopped). Log in and Sign up buttons in that sheet were not clicked.

## Explore

URL: `https://www.patreon.com/explore`. Title: Explore creators on Patreon.

| Control | Opens |
|---|---|
| Search field | Stays on `/explore`. Typing the public word "podcast" filters creators and posts. Nothing was submitted as a form. |
| Topic buttons (All, Pop culture, Comedy, Role playing games, True crime, Art tutorials, and the rest of the chip row) | Local filter on `/explore`. Art tutorials showed "More in Art tutorials". |
| Previous / Next | Carousel on the same page. |
| Creator card | Public creator page. |

## Public creator

Sample used for the tree: `https://www.patreon.com/cw/GlamorousTrash` (also reachable as `/GlamorousTrash`). Published creator content. Tabs:

| Tab | URL | Loaded |
|---|---|---|
| Home | `/cw/GlamorousTrash` | yes |
| Posts | `/cw/GlamorousTrash/posts` | yes |
| Quips | `/cw/GlamorousTrash/quips` | yes |
| Collections | `/cw/GlamorousTrash/collections` | yes |
| Shop | `/cw/GlamorousTrash/shop` | yes |
| Membership | `/cw/GlamorousTrash/membership` | yes |
| Recommendations | `/cw/GlamorousTrash/recommendations` | yes |
| Chats | `/cw/GlamorousTrash/chats` | yes, public page titled Chats. Joining a chat was not attempted. |

Join for free, and any checkout or pledge control, is the login wall. Search posts is a local field. It was focused. It was not submitted.

A sample public post, `https://www.patreon.com/GlamorousTrash/posts/175733850`, loads without a password. Locked posts and paid media were not opened.

## Marketing homepage

URL: `https://www.patreon.com/` when the title is `Where Creator Communities Thrive — Patreon`. H1 observed: Where podcasts grow.

Desktop header: Creators, Features, Pricing, Resources, Updates, logo, Find a Creator search, Log in, Get Started. Open menu is the phone control (0×0 on desktop).

| Control | Opens | Followed |
|---|---|---|
| Creators (hover) | Menu: Podcasters, Video creators, Musicians, Artists, Game devs, plus in-page anchors on those pages | menu mapped; destination pages loaded |
| Features (button) | On one click, navigated to `/product/create`. The mounted menu also lists the product pages below. | destinations loaded |
| Pricing (button) | `https://www.patreon.com/pricing` | yes |
| Resources | Mounted links include Patreon for Creators and resource collections. Hover did not reliably open a distinct panel in this run. | destinations loaded from the DOM links |
| Updates | `https://www.patreon.com/collection/700928?view=condensed` | yes |
| Find a Creator | Search field, placeholder "Find a Creator". Not submitted. | field only |
| Log in | `https://www.patreon.com/login` | stopped |
| Get Started | `https://www.patreon.com/create` signup wall | stopped |
| Creator story cards (Rachel Maksy, Tim Chantarangsu, and the other named cards) | Public creator vanity URLs | one sample creator captured, not every card |
| App Store / Google Play badges | External store listings | not captured (off-site) |
| Scroll down to next section | Same page, next section | interaction, not a new page |

Creators menu destinations:

- `https://www.patreon.com/creators/podcasts`
- `https://www.patreon.com/creators/video`
- `https://www.patreon.com/creators/music`
- `https://www.patreon.com/creators/visualartists`
- `https://www.patreon.com/creators/gaming`

Features menu destinations:

- `https://www.patreon.com/product/create`
- `https://www.patreon.com/product/online-community`
- `https://www.patreon.com/product/grow`
- `https://www.patreon.com/product/newsletter`
- `https://www.patreon.com/product/manage-business`
- `https://www.patreon.com/product/digital-products`
- `https://www.patreon.com/product/paid-membership`

Footer and company links (also in the phone sheet):

| Label | URL | Loaded |
|---|---|---|
| About | `https://www.patreon.com/about` | yes |
| Press | `https://www.patreon.com/press` | yes |
| Careers | `https://www.patreon.com/careers` | yes |
| Brand | `https://www.patreon.com/brand` | yes |
| App directory | `https://www.patreon.com/apps` | yes |
| News | `https://news.patreon.com/` | yes |
| Patreon for Creators | `https://www.patreon.com/cw/PatreonforCreators` | yes |
| Policy | `https://www.patreon.com/policy` | yes |
| Terms of Use | `https://www.patreon.com/policy/legal` (nav also names `/legal`, which redirects here) | yes |
| Accessibility | `https://www.patreon.com/policy/accessibility` | yes |
| Privacy | `https://privacy.patreon.com/policies` | yes |
| Help Center | `https://support.patreon.com/hc/en-us` | yes |
| Top articles | `https://support.patreon.com/hc/en-us/p/top-articles` | yes |
| Contact Us | `https://support.patreon.com/hc/p/contact-us` | not opened (contact form) |
| Help Center Log in | `https://www.patreon.com/login?ru=%2Fzendesk-sso-start` | stopped |

Help Center search accepts a query. The word "payout" was typed and not submitted. The language button opens a locale list (Deutsch, English (United Kingdom), Español, Français, Italiano). Locales were not switched.

Resource collections linked from the marketing footer, loaded as pages:

- `https://www.patreon.com/collection/1489797`
- `https://www.patreon.com/collection/1334102`

## Walls (branch stopped)

| URL | What is on the page |
|---|---|
| `https://www.patreon.com/login` | Title `Log in or sign up`. Email and password. Apple and Facebook. |
| `https://www.patreon.com/create` | Title `Sign up`. Password field. Continue with Apple. Continue with Facebook. |
| Chats, Notifications, Join, and More on the logged-out app | Same email and password wall, often without changing the URL. |

Signed-in home, messages, settings, checkout, pledges, and creator dashboard were not reached.
