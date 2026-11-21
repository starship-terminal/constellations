# Lummi site tree

Mapped 2026-11-21 from the signed-out homepage `https://www.lummi.ai/` in headless Chromium (1440x900), then by opening each control. Sitemap index `https://www.lummi.ai/sitemap.xml` lists six sitemaps. Login and signup walls were recorded and not entered. No form was submitted. Support is a `mailto:` link; the address is not written here.

Theme: the public site declares light tokens on `:root` and a parallel `*-dark` set. No public theme switch was found. `color-scheme` on the homepage was `normal`, page background `rgb(255, 255, 255)`.

## Shell (every browse page)

| Control | Opens |
|---|---|
| Logo | `/` |
| Photos | `/` (photo grid) |
| Illustrations | `/illustration` |
| 3D | `/3d` |
| Search icon (button beside 3D) | Search command dialog (same as focusing the search field or pressing Command-K) |
| Search field, placeholder "Search or create anything!" | Search command dialog |
| Try Pro for free | Pricing dialog on the current page (Monthly / Yearly, Pro Plan, Max Plan, Compare plans, Close). "Start your 7 day Pro trial" goes to a signup login wall, then Stripe checkout. Stop that branch. |
| Log in | `https://www.lummi.ai/login` (the nav href is `/auth/login?returnTo=/auth/close?platform=website`, which redirects to `/login`). Email, password, Continue, Continue with Google, Sign up, Forgot password. **Wall. Stop.** |
| Overflow button (`aria-label` footer-dropdown) | Overflow dialog (`aria-label` overflow-menu). See below. |
| What's new card Close | Dismisses the homepage "What's new" card. Does not navigate. |

Cookie preference center is in the DOM (OneTrust) but was not visible on first paint. Overflow "Cookies" opens it. Not submitted.

## Overflow menu

Opened from the header overflow button.

| Group | Control | Opens |
|---|---|---|
| Product | What's new | `/updates` (button, same destination) |
| Product | Pricing | `/pro` |
| Product | Become a contributor | `/contribute` |
| Product | Developers / API / MCP | `/developers` |
| Resources | Blog | `/blog` |
| Resources | Trends | `/trends` |
| Resources | Events | `/events` |
| Resources | Style references | `/sref-codes` |
| Resources | Help docs | `https://docs.lummi.ai/` (external host, public) |
| Plugins | Figma | `/apps/figma` |
| Plugins | Framer | `/apps/framer` |
| Plugins | Canva | `/apps/canva` |
| Plugins | Webflow | `/apps/webflow` |
| Plugins | Adobe Express | `/apps/adobe-express` |
| Company | About | `/about` |
| Company | Support | `mailto:` (no page). Not opened. |
| Company | Advertise with us | `/advertise` |
| Company | Wall of love | `/love-corner` |
| Company | Instagram | `https://www.instagram.com/lummipics` (external). Not captured. |
| Company | X | `https://x.com/lummipics` (external). Not captured. |
| Legal | Privacy Policy | `/privacy` |
| Legal | Terms of Use | `/terms` |
| Legal | License | `/license` |
| Legal | Cookies | OneTrust preference center dialog. Not submitted. |

Marketing pages (about, blog, pro, apps, and the rest of that family) also show a quieter footer: Blog, Trends, About, Style References, Advertise, Get Pro, Creators, Terms, Privacy.

## Homepage controls under the header

| Control | Opens |
|---|---|
| Tools | Tools menu (`role=menu`). Items: Effects (Reframe, Restyle, Background removal, Duotone), Filters (Video, Following, Number of people, Lighting style, Orientation), Misc (Multi-select), plus a "Sorted by: Daily picks" row. Filter rows are local UI. Duotone, Following, and several effect rows route toward a login wall when they need an account. Record and stop that branch. |
| Reframe | Tool mode on the grid (same family as Tools > Reframe). Applying it to an image hits the login wall. |
| Restyle | Tool mode on the grid. Same wall. |
| Background removal | Tool mode. Also linked as `/?bgremove=true`, `/illustration?bgremove=true`, `/3d?bgremove=true`. Applying it hits the login wall. |
| Daily picks | Sort dialog: Daily picks, Popular, New. Local sort. Does not navigate. |
| Image card | `/photo/<slug>`, `/illustration/<slug>`, or `/3d/<slug>` |
| Creator name on a card | `/creator/<slug>` |
| "+N Shots" | `/shoot/<id>/<slug>` (a published shoot) |
| Download image | Button on a card (`data-id=download-image-button`). A force-click from the probe did not open a dialog and did not leave `/`. Treated as an account action. Not retried into a download. |
| Create image / Create video (search dialog) | Generation UI. Submitting a prompt is a form. Not submitted. `/?create-video=1` is the video entry linked from What's new. |
| Search suggestion chips | `/s/photo/<term>` (and the illustration/3d equivalents when that tab is active) |
| View all (creators in search) | `/creators` |
| Creator avatars in search | `/creator/<slug>` |
| Create AI video / Create AI image | Generation entry. Not submitted. |
| All daily collections | `/daily/photo` |
| Explore all | `/explore` |

## Page types reached from the shell

Each row is a distinct public template. Asset, creator, collection, search, category, blog, trend, and sref pages repeat by the tens of thousands. One of each template is captured, not every URL.

| Path | What it is | Notes |
|---|---|---|
| `/` | Photo grid | Default browse. Infinite scroll. Capture is truncated. |
| `/illustration` | Illustration grid | Same shell as photos. |
| `/3d` | 3D grid | Same shell. |
| `/photo/<slug>` | Photo detail | Representative: first public card from the homepage. |
| `/illustration/<slug>` | Illustration detail | Representative from `/illustration`. |
| `/3d/<slug>` | 3D detail | Representative from `/3d`. Query `?3d=true` is the same detail with the 3D viewer hinted. |
| `/creator/<slug>` | Creator profile | Public gallery. Follow is an account action. Stop that branch. |
| `/creators` | Creator index | |
| `/shoot/<id>/<slug>` | Shoot (a set of shots) | Public. |
| `/collection/<id>/<slug>` | Collection | Public. Linked from daily and sref. |
| `/s/photo/<term>` | Photo search results | Public. `/s/illustration/` and `/s/3d/` are the same template on the other tabs. |
| `/explore` | Category explorer | Links into `/category/<slug>`. |
| `/category/<slug>` | Category grid | Representative from Explore. |
| `/daily/photo` | Daily collections index | |
| `/pro` | Pricing marketing page | "Get Pro" / checkout links go to `/api/stripe/checkout` via the login wall. Stop. |
| `/contribute` | Contributor marketing | Apply / upload is behind an account. `/upload` is disallowed in robots.txt. Stop. |
| `/developers` | API marketing | Apply now goes to `/developers/api`. Docs link `/developers/api-reference`. |
| `/developers/api` | API request form | Public page says "Please sign in to fill out the form." Fields were not filled. Form not submitted. |
| `/developers/api-reference` | API reference | Public docs page if it loads signed out. |
| `/blog` | Blog index | |
| `/blog/articles` | All articles | |
| `/blog/<slug>` | Article | One representative. |
| `/trends` | Trends index | |
| `/trends/<slug>` | Trend detail | One representative. |
| `/events` | Events index | "Get in touch" is mailto. Not opened. |
| `/sref-codes` | Style references index | |
| `/sref-codes/<category>` | Style reference category | One representative (`/sref-codes/cinematic`). |
| `/about` | About | Links Custom (`/custom`), which is a generation surface. Not submitted. |
| `/custom` | Not a distinct page | Loads the photo homepage. Not a separate template. |
| `/advertise` | Advertise | Contact is mailto. Not opened. |
| `/love-corner` | Wall of love | Published testimonials. |
| `/privacy` | Privacy | |
| `/terms` | Terms | |
| `/license` | License | |
| `/updates` | What's new | |
| `/apps` | Plugin index | |
| `/apps/figma`, `/apps/framer`, `/apps/canva`, `/apps/webflow`, `/apps/adobe-express` | Plugin landing pages | Same template. Capture the index and one detail (Figma). |
| `/image-prompt-generator` | Prompt inspiration | Shuffle is local. Not a submitted form. |
| `https://docs.lummi.ai/` | Help docs | Public. Sidebar: Getting Started, Plugins, Paid Plans, Advanced Features, FAQ, creator docs, license, collections. One home capture. |
| `/es` | Not a page | Sitemap lists it. The URL returns the site's own "couldn't find this page" screen. Not captured. |

## Walls and branches that stop

| URL or control | Why it stops |
|---|---|
| `https://www.lummi.ai/login` | Email, password, Continue, Continue with Google, Sign up, Forgot password. |
| `/auth/login` and `screen_hint=signup` | Same login wall, including the Pro trial and Stripe return path. |
| Continue with Google / Apple | OAuth. Not clicked. |
| Forgot password, Sign up | Account flows. Not opened past the login page record. |
| `/api/stripe/checkout` | Payment. Not opened. |
| Download, Follow, Duotone, generation submit, contributor apply, newsletter, profile, plan, survey, onboarding | Account, payment, or a form. Not submitted. |
| `/upload`, `/s/custom/` | robots.txt Disallow. Not opened. |
| Instagram, X, Udemy privacy, OneTrust product site | Off-site. Not captured. |

## Sitemap scale (not a shot list)

| Sitemap | Count | Path prefix |
|---|---|---|
| `/sitemap/0.xml` | 57 | Marketing, apps, a few collections, `/es` |
| `/sitemap/1.xml` | 64 | `/s/` search URLs |
| `/sitemap/2.xml` | 57 | `/category/` |
| `/sitemap/3.xml` | 184 | `/creator/` |
| `/sitemap/4.xml` | 50000 | `/photo/`, `/illustration/`, `/3d/` |
| `/sitemap/5.xml` | 50000 | same asset prefixes |

Asset, creator, and search URLs are the same templates as the representatives above.
