# Epidemic Sound public site tree

Captured 2026-11-21, signed out, from [https://www.epidemicsound.com/](https://www.epidemicsound.com/). Cookie banner `#es-cookie-banner` was hidden. Accept was not clicked. Login, signup, checkout, and identity providers were not opened.

Machine-readable copy: [raw/site-tree.json](raw/site-tree.json).

## Header

The desktop bar is a white pill. The logo (accessible name Home) goes to `/`.

| Control | Opens |
|---|---|
| Music | Dropdown `#top-nav-panel-music` |
| Sound effects | Dropdown `#top-nav-panel-sound-effects` |
| Tools | Dropdown `#top-nav-panel-tools` |
| License | Dropdown `#top-nav-panel-license` |
| Resources | Dropdown `#top-nav-panel-resources` |
| For business | Dropdown `#top-nav-panel-for-business` |
| Pricing | Page `/pricing/` |
| Log in | Stopped. `/login/` redirects toward `login.epidemicsound.com`. Not opened. |
| Create free account | Stopped. `/oauth_registration/`. Not opened. |
| Show navigation menu (390) | Drawer `#top-nav-menu`. Close is Hide navigation menu. |

Music panel links: Explore all music `/music/`, Genres `/music/genres/`, Moods `/music/moods/`, Themes `/music/themes/`, All artists `/artists/`, plus featured artists and playlists (Christmas, Podcast Hooks, Beats).

Sound effects panel: All sound effects `/sound-effects/`, Ambience, Rain, Wind category pages.

Tools panel: `/tools/`, Studio, Assistant, Voiceovers `/voices/`, Adapt, Labs, MCP, API, Adobe plugin, DaVinci plugin, Mac, Windows, iOS, Android app pages.

License panel: How it works, YouTube, Filmmaking, Advertising, and the copyright-claim link back to How it works.

Resources panel: Blog, Help center (`www.epidemicsoundhelp.com`, external), Refer a friend, For artists, About us, and a blog post about the API.

For business panel: Business hub, brands, broadcasters, production companies, publishers, developers (`developers.epidemicsound.com`, external, not crawled), agencies, Enterprise, Business plan, In-store, Customer stories, Reseller, Soundproof.

## Pages visited

Each row is a public page that returned 200. Catalog pages (genres, artists, tracks) repeat the same templates. Individual tracks and artists after the samples were not all opened. The queue still held thousands of artist, genre, and locale URLs when the crawl stopped.

| Path | Heading |
|---|---|
| `/` | You bring the idea. We bring the sound. |
| `/music/` | Discover our royalty-free music for videos |
| `/music/genres/` | Browse our music by genre |
| `/music/moods/` | Browse our music by mood |
| `/music/themes/` | Music Themes and playlists |
| `/music/genres/christmas/` | Christmas music |
| `/music/genres/beats/` | Beats music |
| `/music/themes/podcast/podcast-hooks/` | Podcast hooks |
| `/music/tracks/6c0178b7-7c04-42d6-915e-0809526bc168/` | Glory Bound |
| `/music/tracks/111230ad-d08e-4d49-af44-1df611181e6c/` | EAST WEST/WEST EAST |
| `/artists/` | Meet our artists |
| `/artists/christoffer-moe-ditlevsen/` | Christoffer Moe Ditlevsen |
| `/artists/adelyn-paik/` | Adelyn Paik |
| `/artists/ooyy/` | Ooyy |
| `/artists/roy-williams/` | Roy Williams |
| `/sound-effects/` | Sound Effects |
| `/sound-effects/categories/ambience/` | Ambience |
| `/sound-effects/categories/rain/` | Rain |
| `/sound-effects/categories/wind/` | Wind |
| `/tools/` | Your soundtrack toolbox |
| `/tools/studio/` | Studio |
| `/tools/assistant/` | Assistant |
| `/tools/adapt/` | Adapt |
| `/tools/labs/` | Labs |
| `/tools/mcp/` | MCP |
| `/tools/api/` | API |
| `/voices/` | Voiceovers |
| `/plugins/adobe/` | Adobe plugin |
| `/plugins/davinci-resolve-studio/` | DaVinci plugin |
| `/app/macos/` `/app/windows/` `/app/ios/` `/app/android/` | App marketing pages |
| `/how-it-works/` | How it works |
| `/youtube/` | For YouTube |
| `/filmmaking/` | For filmmaking |
| `/pricing/` | Our subscriptions |
| `/our-plans/business-plan/` | Business plan |
| `/business/` and brand, broadcaster, production, publisher, agency, advertising, soundproof pages | Business marketing |
| `/enterprise/` `/enterprise/success-stories/` `/enterprise/become-a-reseller/` | Enterprise marketing |
| `/instore/instore-music/` | In-store music |
| `/about-us/` | About |
| `/blog/` and `/blog/free-api/` | Blog index and one post |
| `/community-program/` | Community |
| `/for-artists/` | For artists |

## Same-page controls

| Control | What it does |
|---|---|
| Play on a home card | Starts an inline preview. Does not leave the page. |
| Individuals / Businesses on pricing | Switches the plan set on the same page. |
| Monthly / Yearly switch | Changes the billed period on the same page. Not a form submit. |
| Search on `/music/` | A text field. "calm" was typed and not submitted. |
| Get 30 days free | Link to `/subscription/create`. Stopped. Checkout was not opened. |
| Contact sales | Link to `https://go.epidemicsound.com/custom-license`. Not submitted. |
| Footer language links (`/es`, `/fr`, `/de`, and others) | Locale copies of the marketing site. Recorded, not photographed. |

## Stopped

| URL | Why |
|---|---|
| `/login/` | Login. Known to open a Keycloak form. Not opened. No email, password, Google, Apple, or SSO. |
| `/oauth_registration/` | Signup. Not opened. |
| `/signup` | Signup alias. Not opened. |
| `/subscription/create` | Checkout. Not opened. |

Help center, developers, press (`corporate.epidemicsound.com`), and the sales form are other hosts. They are linked from the tree and were not crawled.
