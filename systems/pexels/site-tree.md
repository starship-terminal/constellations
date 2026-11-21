# Pexels site tree

Mapped from the public homepage at https://www.pexels.com/ on 2026-11-21, before screenshots, in headless Chromium (Playwright, system Chrome channel). Desktop viewport requested 1440x900. Cookie banner was hidden in the DOM and never clicked: Reject All, Accept All Cookies, Cookies Settings and Continue without Accepting can POST. No form was submitted. No email was typed. Google and Apple were not clicked.

A control that opens `/login/` or `/join-contributor/` is a wall. The URL is recorded and that branch stops.

## Shell (every public page)

| Control | Opens |
|---|---|
| Logo | `/` home |
| Explore (link, also a hover disclosure) | `/discover/` |
| Explore hover: Wallpapers | `/discover/wallpapers/` |
| Explore hover: Leaderboard | `/leaderboard/` |
| Explore hover: Challenges | `/challenges/` |
| Explore hover: Winners Wall | `/winners-wall/` |
| Explore hover: Photography Series | `/the-level-up/` |
| Explore hover: Become a Hero | `/hero/` |
| Explore hover: Free Videos | `/videos/` |
| License | `/license/` |
| More (`#more` icon button, unlabeled) | Dropdown menu, stays on the page |
| More: Log in | `/login/` wall. Also offers Apple and Facebook, plus a Cloudflare "Verify you are human" checkbox. Stop. |
| More: Image & Video API | `/api/` |
| More: Apps & Plugins | `/pro/` |
| More: Help Center | `https://help.pexels.com/hc/en-us` (Zendesk, off the product shell) |
| More: Report Content | `/report/` |
| More: Partnerships | `/become-a-partner/` |
| More: Imprint & Terms | `/imprint/` |
| More: Change Language | Language list in the same menu. Not a navigation. |
| More: social icons | Instagram, Threads, Pinterest, YouTube, TikTok. External. Not followed. |
| Join (header button) | Intent dialog, stays on the page |
| Join dialog: Download content | Continues the join flow toward an account. Not followed. |
| Join dialog: Share photos and videos | `/join-contributor/` wall. Stop. |
| Join dialog: close | Closes the dialog |
| Search field (`#search`, type=search) | Focus shows suggestion list after typing. Enter would submit a search. Not submitted from the mapper. |
| Search: Photos / Videos type button | Content-type menu (Photos, Videos) |
| Search submit (magnifier) | `/search/<query>/` or `/search/videos/<query>/` |
| Cookie banner: Cookie Policy | `/cookies/` |
| Cookie banner: Reject All, Accept All Cookies, Cookies Settings, Continue without Accepting | Consent actions. Not clicked. |

License, API, Pro, imprint and similar pages also show a secondary nav: About Us (`/about/`), License, Help Center, Legal (`/imprint/`).

## Home `/`

| Control | Opens |
|---|---|
| Challenge card (Close to Home) | `/challenges/close-to-home/` |
| Challenge card Join | Same challenge, or the join wall if the action requires an account. Not followed as a submit. |
| Subnav: Home | `/` |
| Subnav: Videos | `/videos/` |
| Subnav: Leaderboard | `/leaderboard/` |
| Subnav: Challenges | `/challenges/` |
| Subnav: Winners Wall | `/winners-wall/` |
| Subnav: Photography Series | `/the-level-up/` |
| Trending / New toggle | Listbox: Trending, New. Stays on the page. |
| Around the world | Dialog of trending searches by country. A chip opens `/search/<term>/`. |
| Trending chips | `/search/<term>/` |
| See more (popular, trending) | `/popular-searches/` |
| Photo tile | `/photo/<slug>/` |
| Video tile | `/video/<slug>/` |
| Photographer name on a tile | `/@<handle>/` public profile |
| Canva promo on a tile | `canva.com` (external editor). Not followed. |

## Search `/search/ocean/` and `/search/videos/ocean/`

Reached by the search submit and by trending chips. Representative query `ocean` (a public topic word, not a person).

| Control | Opens |
|---|---|
| Photos / Videos type | Switches `/search/` and `/search/videos/` |
| Filter chips: orientation, people count, age, size, color, recency, duration, fps, resolution | Filter menus on the results page. Color includes a hex field and a color input. Not submitted as a search form beyond opening the menu. |
| Pagination 1–6, Next | `/search/ocean/?page=N` (and the video equivalent) |
| Result tile | Photo or video detail |

## Videos home `/videos/`

Same shell and subnav as home, with a video search field and video tiles.

## Discover `/discover/`

Editorial collections. Cards open collection or wallpaper paths such as `/discover/wallpapers/`. Page is very tall (about 23800px). Capture is truncated at the kit's 8-chunk boundary.

## Photo detail `/photo/icelandic-geothermal-landscape-with-mountains-32577944/`

A published photo linked from the homepage.

| Control | Opens |
|---|---|
| Photographer name | `/@<handle>/` public profile |
| Crop, Remove Background, Edit | canva.com. External. Not followed. |
| Like count button | Requires an account. Not clicked (would be an action, and may open the login wall). |
| Free download | Direct image file on `images.pexels.com`. A file download, not a page. Not saved as an asset. |
| Download size menu (chevron beside Free download) | Size menu. The capture click missed the chevron and opened the search type menu instead. Size menu not captured. |
| Related photos | Other `/photo/` pages. One representative only. |

## Video detail `/video/fresh-kumquats-in-wooden-bowl-indoors-39458084/`

| Control | Opens |
|---|---|
| Add Text, Convert to GIF, Edit | canva.com. External. Not followed. |
| Free download | `/download/video/<id>/` file response. Not saved. |
| Related videos | Other `/video/` pages. One representative only. |

## Challenges `/challenges/` and `/challenges/close-to-home/`

Challenge cards open `/challenges/<slug>/`. Join on a challenge is the contributor wall if it asks for an account. Stop that branch.

## Leaderboard `/leaderboard/`

| Control | Opens |
|---|---|
| Most Viewed, Most Active, Recent | Tabs on the same page |
| A member row | `/@<handle>/` public profile. One representative. |

## Other public pages

| Path | What it is |
|---|---|
| `/winners-wall/` | Challenge winners editorial |
| `/popular-searches/` | Search directory |
| `/cookies/` | Cookie policy |
| `/api/` | API marketing |
| `/pro/` | Apps and plugins |
| `/imprint/` | Imprint and terms |
| `/report/` | Report content. If it is a form, it is not submitted. |
| `/become-a-partner/` | Partnerships. Form not submitted. |
| `/about/` | About, linked from the license secondary nav |
| `/hero/` | Heroes program. Apply / join stops at the account wall if that control opens one. |
| `/the-level-up/` | Photography series |
| `/this-page-does-not-exist-capture/` | Styled 404 |

## Walls (stop)

| URL | What it asks | How it was reached |
|---|---|---|
| `https://www.pexels.com/login/` | Email, password, Google, Apple, or Facebook. A Cloudflare checkbox sits above Log in. Language button and Join stay in the header. | More menu Log in. Upload redirects here (`/login/?redirect_to=/upload/`). |
| `https://www.pexels.com/join-contributor/` | First name, last name, email, password, or Google. | Join dialog, Share photos and videos. |

Not typed, not clicked: the email field, the password field, name fields, Google, Apple, Facebook, Forgot your password.

## Not a product page

Help Center (`help.pexels.com`) is Zendesk. Canva links leave the site. Both are recorded and not captured as Pexels screens.
