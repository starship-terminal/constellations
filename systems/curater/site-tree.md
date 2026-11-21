# Site tree

Start: https://curater.org/

Captured 2026-11-21, signed out, desktop 1440 x 900 and phone 390 x 844. A control that opens Google is recorded and that branch stops. Google was not clicked. No email, password, code, or form was submitted.

## Shell

The same shell wraps every public page except the login page, which drops the rail.

| Control | Kind | Opens |
|---|---|---|
| Logo | link | https://curater.org/ |
| Home (house icon, title Home) | link | https://curater.org/home |
| Feed (grid icon, title Home in the DOM, href /feed) | link | https://curater.org/feed |
| Taste Profile | link | https://curater.org/taste, which redirects to https://curater.org/taste/soon |
| Notifications | button | Sign-in dialog on the current URL. Stops at Continue with Google |
| Profile | button | Same sign-in dialog |
| Create | button | Same sign-in dialog |
| Settings | button | Settings menu |
| Privacy | footer link | https://curater.org/privacy |
| Terms | footer link | https://curater.org/terms |

Phone header, 390 wide:

| Control | Kind | Opens |
|---|---|---|
| Logo | link | https://curater.org/ |
| Feed | link | https://curater.org/feed |
| Taste Profile | link | https://curater.org/taste/soon |
| Search | button | Search overlay on the current page. Placeholder "Type anything". Submit is a filled Search button. Not submitted |
| Menu | button | Sheet: Settings, Privacy, Terms, About, Sign in. Close is the X that replaces Menu |

## Settings menu

Opened by the gear. Desktop items:

| Item | Opens |
|---|---|
| Settings | https://curater.org/auth/login. Login wall. Branch stops |
| Extension | https://curater.org/extension |
| Privacy | https://curater.org/privacy |
| Terms | https://curater.org/terms |
| About | https://curater.org/about |
| Sign in | https://curater.org/auth/login. Login wall. Branch stops |

Phone sheet has Settings, Privacy, Terms, About, Sign in. Extension is not in the phone sheet.

## Home

https://curater.org/ and https://curater.org/home render the same digest.

| Control | Opens |
|---|---|
| Sign in or create account | Leaves the site for Google sign-in. Curater's redirect host is auth.curater.org. Branch stops |
| Curation card image or title | https://curater.org/curation/<id> |
| Curated by | https://curater.org/<handle> |
| Privacy, Terms | legal pages |

Cards seen on the first paint included `/curation/sVWPDcCJ`, `/curation/vk2At56d`, `/curation/ytJC9YL2`, and the handle `/glauber`. The digest is a live list, so later visits can show other ids.

## Feed

https://curater.org/feed

| Control | Opens |
|---|---|
| Featured | Stays on /feed. Default list |
| For You | Stays on /feed. Swaps the list. Signed out, the list still renders public cards |
| More | Menu |
| Search | Expands a field, placeholder "Search curations...". Not submitted |
| Log in or sign up | https://curater.org/auth/login. Login wall |
| Card | https://curater.org/curation/<id> |
| Curator name | https://curater.org/<handle> |
| Category label | https://curater.org/feed?categoryId=<id> |
| Tag chip, from a curation page | https://curater.org/feed?tag=<id> |
| Add to my taste | On a card, opens the sign-in path. On a curation page the button is disabled and Continue with Google sits beside it. Not clicked through to Google |
| Browse by themes, Visual Identity | https://curater.org/collection/visual-identity |
| Street Photography | https://curater.org/collection/street-photography |
| Summer Tracks | https://curater.org/collection/summer-tracks |

More menu:

| Item | Opens |
|---|---|
| Subscriptions | Stays on https://curater.org/feed and replaces the grid with a login wall: "Sign in to subscribe to curators". Continue with Google. Branch stops |
| Contributors | https://curater.org/feed?authors=contributors |
| Art & Design | https://curater.org/feed?categoryId=bd44ee5f-734f-4db6-abf4-090d0fbfe9c0 |
| Photography & Cinema | https://curater.org/feed?categoryId=6049193e-6f65-4191-80f4-7f0d1c2f7dff |
| Music & Sounds | https://curater.org/feed?categoryId=8756cffb-e1f7-4860-8dc5-933771c11126 |
| Architecture & Interiors | https://curater.org/feed?categoryId=441e9d5b-6fa3-4f67-bb2d-63eab5c0284b |
| Fashion & Style | https://curater.org/feed?categoryId=5cb35cee-d4c2-40c1-a455-a299ac63289e |
| Industrial Design | https://curater.org/feed?categoryId=19680323-1e6f-456f-86a6-1a4ff0cba220 |
| Sensorial | https://curater.org/feed?categoryId=84c7cf6d-6b96-4d92-bdf3-3f40c9b64539 |

Category ids were read from the public `GET /api/v1/categories` response while the feed loaded. Photography through Sensorial were not each clicked after Subscriptions hid the More button; the ids match the menu labels in that response.

## Curation

https://curater.org/curation/<id>

Example captured: https://curater.org/curation/sVWPDcCJ

| Control | Opens |
|---|---|
| Back / feed mark | https://curater.org/feed |
| Category | https://curater.org/feed?categoryId=<id> |
| Curated by | https://curater.org/<handle> |
| Add to my taste | Disabled. Login wall copy sits beside it |
| Continue with Google | Google sign-in. Not clicked |
| Hide pins | Toggles to Show pins on the same page |
| A pin row | Expands that pin's note. Stays on the page |
| A tag | https://curater.org/feed?tag=<id> |
| Listen links | External music pages. Not followed |
| Related curation | another `/curation/<id>` |

Related ids reached from the first cards: `ETNg4L3b`, `jGxXVSfV`, `jJsMzwGn`, `4vDCjVxN`, `U6kTqX8J`, `HzzpHHxx`. They share the same page pattern.

## Profile

https://curater.org/glauber

| Control | Opens |
|---|---|
| TasteScope button | Stays on the profile. The section is already on the page |
| Learn more | In-page link on the taste line |
| A curation in the grid | https://curater.org/curation/<id> |
| Social marks | External profiles. Not followed |

## Collection

https://curater.org/collection/<slug>

Reached from Browse by themes: `visual-identity`, `street-photography`, `summer-tracks`. Each is a public grid of curations. Cards open `/curation/<id>`.

## Taste

https://curater.org/taste redirects to https://curater.org/taste/soon.

No form. Copy says full access is coming soon and is available only to curators. No further control.

## Extension

https://curater.org/extension

| Control | Opens |
|---|---|
| Add to Chrome | https://curater.org/extension/chrome, which redirects to the Chrome Web Store page for the extension. Not clicked. Branch stops at the store URL |

The page shows a static draft picker (New draft, an example draft, Cancel, Save). Those controls are a demo of the extension. Save was not clicked.

## About, privacy, terms

| Page | Notes |
|---|---|
| https://curater.org/about | Links to `/glauber` and to an external social profile. The social link was not followed |
| https://curater.org/privacy | Long policy. External analytics policy links were not followed |
| https://curater.org/terms | Long terms. No extra in-app routes |

## Login wall routes

| Request | Result |
|---|---|
| https://curater.org/auth/login | Login page. Continue with Google. Not clicked |
| https://curater.org/signin | Redirects to /auth/login |
| https://curater.org/auth/callback | Redirects to /auth/login |
| https://curater.org/onboarding | Redirects to /auth/login. Not filled |

## Not pages

These returned the site's 404 shell (one link, no app chrome): `/pricing`, `/blog`, `/explore`, `/discover`, `/search`, `/login`, `/auth`, `/settings`, `/notifications`, `/profile`, `/create`, `/account`.

`/robots.txt` allows all user agents and names several AI crawlers. `/sitemap.xml` did not return a URL list in this session.

## Widths

Desktop 1440 x 900 shows the icon rail, the feed masonry, and the settings menu as a popover.

Phone 390 x 844 shows the header, the digest as a single column, the menu as a sheet, and search as an overlay. Login is a single column with the sample card above the Google button.
