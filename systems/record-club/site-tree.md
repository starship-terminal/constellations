# Record Club site tree

Public signed-out map of [record.club](https://record.club/), read on 2026-11-21 in a T3 preview tab, incognito. `data-theme` on `<html>` was `system`. The homepage and the about page painted light. Browse, the album page, lists, search, help, supporter, the 404, and both auth walls painted dark. No account setting was changed.

Nothing was typed. Apple and Google were not clicked. No form was submitted. The signed-in app was not entered.

## Header (desktop, 1440)

Logged-out header, 76px. Left nav, centred wordmark, right actions.

| Control | Opens |
|---|---|
| Browse | page `https://record.club/browse` |
| Community | page `https://record.club/community` |
| Search | page `https://record.club/search` |
| Show more (ellipsis, `aria-haspopup`) | menu on the same page: Blog, About, Become a supporter, Changelog |
| Wordmark | page `https://record.club/` |
| Log in | page `https://record.club/login`. Wall. Branch stopped. |
| Join for free | page `https://record.club/register`. Wall. Branch stopped. |

Show more links:

| Label | Page |
|---|---|
| Blog | `https://record.club/blog` |
| About | `https://record.club/about` |
| Become a supporter | `https://record.club/supporter` |
| Changelog | `https://record.club/changelog` |

The hamburger (`.toggle-slide-out-navigation`) is in the header markup and is `display: none` at 1440.

## Phone (390)

The category row collapses. The header keeps the wordmark and a hamburger. The hamburger opens a drawer on the same URL. A grey scrim covers the page behind it. Close returns to the same page.

| Drawer control | Opens |
|---|---|
| Browse | `https://record.club/browse` |
| Community | `https://record.club/community` |
| About | `https://record.club/about` |
| Help | `https://record.club/help` |
| Blog | `https://record.club/blog` |
| Contact support | `https://record.club/about/contact` |
| Become a supporter | `https://record.club/supporter` |
| Register | `https://record.club/register`. Wall. Branch stopped. |
| Log in | `https://record.club/login`. Wall. Branch stopped. |
| Instagram, Bluesky, Threads, Twitter, Discord | external |

## Home `https://record.club/`

| Control | Opens |
|---|---|
| Create free account | `https://record.club/register`. Wall. Branch stopped. |
| Get the app | `https://record.club/download` |
| Log in (under the hero) | `https://record.club/login`. Wall. Branch stopped. |
| Album artwork in the primer | a public release page, for example `https://record.club/releases/albums/2hollis-pirouette` |
| retrospective | `https://record.club/2025` |

## Browse `https://record.club/browse`

Heading "Explore all music on Record Club". Signed out. Four cards and carousel rows.

| Control | Opens |
|---|---|
| Releases | `https://record.club/releases` |
| Artists | `https://record.club/artists` |
| Labels | `https://record.club/labels` |
| Genres | `https://record.club/genres` |
| See all (trending) | `https://record.club/releases?sortBy=popularity-week` |
| Release tile | a public album page |
| Previous slide, Next slide | the same carousel. No new URL. |

## Album `https://record.club/releases/albums/2hollis-pirouette`

Public. Title "Pirouette (2026) by 2hollis". Track list, ratings, and public reviews load without an account.

| Control | Opens |
|---|---|
| Overview, Reviews, Lists, Comments, Versions, Press, Users | tabs on the same release. Counts were visible (Reviews 35, Lists 49, Users 164). |
| 2hollis | `https://record.club/artists/2hollis` |
| Listened, Rotation, Queue, stars, Like, Submit rating | in-page controls. Not submitted. |
| Review or log…, Add to lists…, Add tags…, Add notes…, Set cover art…, Recommend to user…, Share release… | an actions panel on the same page. Not submitted. Notes and cover art are marked upgrade. |
| More options (per track) | not opened. |
| Preview | not pressed. |

## Community `https://record.club/community`

Heading "Explore the community". Users, Reviews, and Lists cards. A trending-users carousel shows public display names and a Follow control on each card. Follow was not clicked.

| Control | Opens |
|---|---|
| Users | `https://record.club/users` |
| Reviews | `https://record.club/reviews` |
| Lists | `https://record.club/lists` |
| A user name | a public profile, for example `https://record.club/nathyboy04` |

## Lists `https://record.club/lists`

Public. Heading "Lists". Filters: Everyone, Following, Liked by friends, and a Year select. "Showing 1–50 of 13,859 lists". Public list titles and public display names. Following was not opened as a signed-in view.

## Search `https://record.club/search`

Public. Empty field, placeholder "Search Record Club". Filters: Releases, Artists, Labels, Users, Lists, Reviews. The empty state shows trending releases and a genre row. Nothing was typed.

## About, help, blog, supporter

| URL | What loaded |
|---|---|
| `https://record.club/about` | Heading "Microphone check – one, two, what is this?". Help, contact, and social links. |
| `https://record.club/help` | Heading "How can we help?". Topic cards (General, Features, Cover art, Contributing data, Reviews, Supporter, Account and privacy, Importing, Exporting). Search not submitted. |
| `https://record.club/blog` | Heading "Liner Notes". Public posts, including track ratings, essential releases, and "Easier sign in with Apple and Google". |
| `https://record.club/supporter` | Heading "Become a supporter.". Monthly and Yearly. Standard is Free. Supporter is "$4 per month". Checkout was not opened. |
| `https://record.club/download` | linked from the hero. Not photographed. |
| `https://record.club/changelog` | linked from Show more. Not photographed. |
| `https://record.club/community` | Heading "Explore the community". Read. Not photographed. |
| `https://record.club/releases/albums/2hollis-pirouette` at 390 | Photographed as [album-dark-mobile.png](screenshots/album-dark-mobile.png). |

## Footer (every marketing page)

Browse: Releases, Artists, Labels, Genres.

Community: Users, Reviews, Lists.

Information: About, Help, Blog, Changelog, Supporter, Contact (`/about/contact`).

Follow: Instagram, Bluesky, Threads, Twitter, Discord. External.

Download: App Store and Google Play. External.

Legal: Terms of Service (`/terms`), Privacy Policy (`/privacy`), Acceptable Use (`/fair-use`), Community Guidelines (`/community-guidelines`).

The copyright line reads "© 2026 Okay Nice AB."

## Login walls (recorded, not entered)

| URL or control | What loaded |
|---|---|
| Log in, `/login` | HTTP 200. Heading "Welcome back." Continue with Apple, Continue with Google, an empty email field, Continue disabled. Password field exists in the DOM and is not shown. Nothing typed. Identity providers not clicked. |
| Join for free, Create free account, `/register` | HTTP 200. Heading "Join the community." Same Apple, Google, and empty email field. Continue not clicked. |
| Phone drawer, Register and Log in | same walls. Branch stopped. |

`login-extracted` stays `not-started`.

## Other public pages

| URL | What loaded |
|---|---|
| `https://record.club/this-page-is-not-real` | Title "Page not found". Heading "Page not found". Copy: "Oh no! We can't find the page you've requested." Back to the front page, plus the footer. |
