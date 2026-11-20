# SoundCloud public site tree

Mapped on 2026-11-21 from `https://soundcloud.com/` with headless Playwright (desktop 1440×900) before screenshots. A control is recorded only when it was opened or its `href` was read. Branches that land on a sign-in or sign-up wall stop there. No form was submitted. No password, code, Google, Facebook, or Apple control was used.

The signed-out desktop player is dark (`body` background `rgb(18, 18, 18)`, text `rgb(255, 255, 255)`). At 390×844 the same host redirects to `https://m.soundcloud.com/`, a light shell with a white page and a bottom tab bar. The auth iframe query includes `theme=dark`. No public theme switch was found on the desktop player. OneTrust cookie UI is present on every player page (`I accept`, `Reject all`, `Manage preferences`). It was not clicked. Capture hides the overlay in CSS.

## Header (player shell)

Present on `soundcloud.com` player pages (home, discover, search, profile, legal, upload marketing).

| Control | Opens |
|---|---|
| SoundCloud wordmark | `https://soundcloud.com/` (signed-out marketing home) |
| Home | `https://soundcloud.com/discover` |
| Feed | Sign-in wall: `https://soundcloud.com/signin?redirect_url=/feed` (HTTP 401). Stop. |
| Library | Sign-in wall: `https://soundcloud.com/signin?redirect_url=/you/library` (HTTP 401). Stop. |
| Search button | Focuses the header search field. Submitting a query (not a form POST of personal data) goes to `https://soundcloud.com/search?q=…` |
| Sign in (button, class `loginButton`) | Auth modal over the current page. Visible iframe `https://secure.soundcloud.com/web-auth?…&theme=dark&…&start_view=sign_in`. Page URL stays put. Stop. Known probe: email Continue on that host said something unexpected happened and did not advance. |
| Create account (button, class `signupButton`) | Same auth modal, sign-up view. Stop. Not opened past the wall. |
| Upload | `https://soundcloud.com/upload` (public marketing). The drop target says "After you sign in, your upload will start." |
| Settings and more (`aria` button) | Header dropdown menu, not a new page. Items below. |

### Settings and more menu

Opened on `/discover`. Closes with Escape.

| Item | Opens |
|---|---|
| About us | `https://soundcloud.com/company/home` (company site) |
| Legal | `https://soundcloud.com/terms-of-use` |
| Copyright | `https://soundcloud.com/pages/copyright` |
| Mobile apps | `https://soundcloud.com/download` |
| Artist Membership | Sign-in wall: `https://soundcloud.com/signin?redirect_url=/pages/membership` (HTTP 401). Stop. |
| Newsroom | `https://soundcloud.com/company/newsroom` |
| Jobs | Redirects to `https://soundcloud.com/company/careers/` |
| Developers | `https://developers.soundcloud.com/` |
| SoundCloud Store | `https://store.soundcloud.com/` (external shop; not captured as product UI) |
| Support | `https://help.soundcloud.com/hc` |
| Keyboard shortcuts | Dialog on the current page (play, volume, seek, like, search). Not a navigation. |
| Pro plans | `https://checkout.soundcloud.com/artist?ref=t132` (checkout). Buy controls not used. |

## Signed-out home (`/`)

Marketing page plus a trending-track strip. Header as above.

| Control | Opens |
|---|---|
| Promo banner Close | Dismisses the Artist Pro banner on the page. |
| Learn More (banner) | `https://checkout.soundcloud.com/artist?ref=t375#planPicker` |
| Get started | Auth / sign-up wall. Stop. |
| Featured artist name (example: DC the Don) | Public profile `https://soundcloud.com/dcthedon` |
| Explore Artist Pro | `https://checkout.soundcloud.com/artist?ref=t10552` |
| Explore Go+ | `https://checkout.soundcloud.com/go?ref=t1033` |
| For artists | Sign-in wall: `https://soundcloud.com/signin?redirect_url=/artists` (HTTP 401). Stop. |
| Upload your own | `https://soundcloud.com/upload` |
| Hear what's trending / a track title | Public track page, for example `https://soundcloud.com/akamersad/vay` |
| Artist name under a track | Public profile |
| Play / Like / Follow / More on a track card | Play starts audio in the bottom bar (public). Like, Follow, and More open the sign-in wall. Stop those branches. |
| Directory (footer area on the marketing home) | Same cluster as the player footer, listed below. |

## Discover (`/discover`)

Signed-out home of the player. Sections observed: Tracks and Playlists, Artists to watch out for, Buzzing (Mexico, Electronic, Hip Hop & Rap, Pop, R&B), Curated by SoundCloud.

| Control | Opens |
|---|---|
| A playlist or track card | Public track or set URL under `soundcloud.com/<user>/…` |
| An artist card | Public profile |
| forward (carousel) | Scrolls the shelf. Stays on `/discover`. |
| Play on a card | Bottom play bar. Public. |
| Like, Follow, More | Sign-in wall. Stop. |

## Search

| Control | Opens |
|---|---|
| Empty search | `https://soundcloud.com/search` |
| Query `techno` (typed, not a personal form) | `https://soundcloud.com/search?q=techno` with heading Search results |
| Everything | `https://soundcloud.com/search?q=techno` |
| Tracks | `https://soundcloud.com/search/sounds?q=techno` |
| People | `https://soundcloud.com/search/people?q=techno` |
| Albums | `https://soundcloud.com/search/albums?q=techno` |
| Playlists | `https://soundcloud.com/search/sets?q=techno` |
| Follow / Share / Copy Link / Add to Next up / More on a result | Share and Copy Link are public menus. Follow and More hit the sign-in wall. Stop those. |

## Public profile and track

Reached from the home trending strip (published catalogue, not a private account).

| Control | Opens |
|---|---|
| Profile tabs (All, and further tabs the profile shows) | Stay on `https://soundcloud.com/<user>` with a query or hash, or a subpath the profile links |
| Follow, Share, More | Share is a public menu. Follow and More hit the sign-in wall. Stop. |
| A track row Play | Bottom play bar |
| Like, Repost, More on a row | Sign-in wall. Stop. |

## Upload (`/upload`)

Public marketing. "Upload your first track" and the drop target both require sign-in before an upload starts. Stop at that wall. No file was dropped.

## Charts

| Control | Opens |
|---|---|
| Footer Charts | `https://soundcloud.com/charts/top` |
| `/charts` | Same charts view (HTTP 404 on the bare path, page still renders the player shell and chart rows) |
| A chart row | Public track or playlist |
| Like, Follow, More | Sign-in wall. Stop. |

## Player footer

| Control | Opens |
|---|---|
| Legal | `https://soundcloud.com/terms-of-use` |
| Privacy | `https://soundcloud.com/pages/privacy` |
| Cookie Policy | `https://soundcloud.com/pages/cookies` |
| Cookie Manager | In-page hash (`#`). OneTrust preference center. Not submitted. |
| Imprint | `https://soundcloud.com/imprint` |
| Artist Resources | `https://soundcloud.com/getstarted/getheard` |
| Newsroom | `https://soundcloud.com/company/newsroom` |
| Topics | `https://soundcloud.com/topic` |
| Charts | `https://soundcloud.com/charts/top` |
| Transparency Reports | `https://soundcloud.com/transparency-reports` |
| Language: English (US) | Dialog titled "Select your language". Items: Deutsch, English (US), Español, Français, Italiano, Nederlands, Polski, Português, Svenska, Cancel. A language was not selected. |

## Bottom play bar (player pages)

| Control | Opens |
|---|---|
| Play / pause, seek, volume, next, previous | Transport on the current page. Public. |
| Hide queue | Collapses the queue. Stays on the page. |
| Like, repost, follow on the playing track | Sign-in wall. Stop. |

## Company site (`/company/…`)

Different chrome: Company, Services, Newsroom, Careers, Available Plans. No player header.

| Control | Opens |
|---|---|
| Company (button) | Company menu. Items include the homepage and contact. |
| Services (button) | Services menu. Opened on the company home. |
| Hamburger (phone) | Opens the same columns: COMPANY, SERVICES, FOR BUSINESS, RESOURCES. |
| Newsroom | `https://soundcloud.com/company/newsroom/` |
| Careers | `https://soundcloud.com/company/careers/` |
| Available Plans | `https://soundcloud.com/company/plans/` |
| Listen now (company home) | `https://soundcloud.com/discover/` |
| A newsroom story | `https://soundcloud.com/playbook-articles/<slug>/` |
| Previous slide / Next slide | Carousel on the newsroom. Stays on the page. |
| Contact (pages/contact redirects) | `https://soundcloud.com/company/contact-us/` |
| Visit our Help Center | `https://help.soundcloud.com/hc/en-us` |
| Get in touch / press | `mailto:` links. Not opened. Addresses are not written into the package. |

## Get started (`/getstarted/…`)

Artist marketing. Nav: Get Started, Get Heard, Get Paid, Why SoundCloud, Help, Sign in.

| Control | Opens |
|---|---|
| Get Started | `https://soundcloud.com/getstarted/home/` |
| Get Heard | `https://soundcloud.com/getstarted/getheard/` |
| Get Paid | `https://soundcloud.com/getstarted/getpaid/` |
| Why SoundCloud | `https://soundcloud.com/getstarted/whysoundcloud/` (linked from that nav; confirm on capture) |
| Help | `https://help.soundcloud.com/hc/en-us/categories/31283161425563-Creators-on-SoundCloud` |
| Sign in | `https://secure.soundcloud.com/web-auth?…` (artists redirect). Stop. |
| Get Artist Pro | `https://checkout.soundcloud.com/artist?ref=t10643`. Buy not used. |

## Checkout

| URL | What loaded |
|---|---|
| `https://checkout.soundcloud.com/go` | Public "Go+ not in your country" page with Start Listening back to `soundcloud.com`. No purchase. |
| `https://checkout.soundcloud.com/artist` | Public Artist Pro marketing. "Get Artist Pro" goes to `/artist/buy/artist-pro`. That buy page is a payment wall. Stop. |
| `https://checkout.soundcloud.com/artist?ref=t375#planPicker` | Plan picker. Not submitted. |

## Other public pages linked from the tree

| Page | URL | Notes |
|---|---|---|
| Download | `https://soundcloud.com/download` | iPhone and iPad, and further store links. Store badges not followed into Apple or Google. |
| Community guidelines | `https://soundcloud.com/community-guidelines` | Player chrome, long text. |
| Copyright | `https://soundcloud.com/pages/copyright` | In-page anchors. Report form not submitted. |
| Copyright report | `https://soundcloud.com/pages/copyright/report` | Form. Not submitted. |
| CCPA | `https://soundcloud.com/pages/ccpa` | Linked from privacy. |
| Transparency | `https://soundcloud.com/transparency-reports` | Links to moderation policies. |
| Topics index | `https://soundcloud.com/topic/` | Category cards. |
| Developers | `https://developers.soundcloud.com/` | HOME, BLOG, docs. YOUR APPS goes to `https://soundcloud.com/you/apps` (sign-in wall). Stop. |
| Help Center | `https://help.soundcloud.com/hc/en-us` | Zendesk. Categories for fans, creators, account, billing. Search not submitted with personal data. |
| Imprint, terms, privacy, cookies | player legal URLs above | Long text. Mailto links not opened and not copied into the package. |

## Walls (stop)

| From | Lands on |
|---|---|
| Feed | `https://soundcloud.com/signin?redirect_url=/feed` |
| Library | `https://soundcloud.com/signin?redirect_url=/you/library` |
| For artists | `https://soundcloud.com/signin?redirect_url=/artists` |
| Artist Membership | `https://soundcloud.com/signin?redirect_url=/pages/membership` |
| Sign in / Create account | `https://secure.soundcloud.com/web-auth?…` iframe, `start_view=sign_in` |
| Get started Sign in | `https://secure.soundcloud.com/web-auth?redirect_uri=…artists.soundcloud.com…` |
| Developers YOUR APPS | `https://soundcloud.com/you/apps` (sign-in) |
| Like, Follow, Repost, More, upload drop | Sign-in modal or the upload modal's "After you sign in" |
| Phone Feed and Discover | `https://m.soundcloud.com/feed` stays on the phone host (HTTP 200) and shows a sign-in sheet ("Sign in to SoundCloud", "No thanks"). Stop. The sheet was dismissed with No thanks after the overlay was hidden in CSS. Consent was not accepted or rejected. |

## Phone shell (`m.soundcloud.com`)

At 390×844, `soundcloud.com` redirects here. Tab bar: Home, Feed, Search, Library. Home and search results are public. Feed and Library open the sign-in sheet. A track page and a profile page load. The track more control opens Add to Next up, Add to Playlist, and Station. Add to Playlist was not followed (sign-in).

## Not in the public tree

Signed-in Feed, Library, upload progress, settings, messages, stats, and any plan, birthday, survey, or newsletter field. Dark is the only theme the signed-out player showed. No light theme control was found.
