# VSCO public site tree

Mapped from [https://vsco.co/](https://vsco.co/) on 2026-11-21 in headless Chromium before any package screenshots. The home page redirects to `https://www.vsco.co/`. The marketing site is a Webflow site (`data-wf-site=64e27cdd42db7ecf119d5e61`). The signed-in app lives on `vsco.co` (no `www`) and stops at a login or signup wall. Nothing was submitted. Log in with Google and Continue with Google were not clicked.

The English sitemap at `https://www.vsco.co/sitemap.xml` lists 420 English URLs (684 including `pt-br` and `es-mx` alternates). Article families (`/learn/` 104, `/features/` 69, `/photographer-stories/` 49, `/effects/` 28, `/50/` 27) share the same chrome. This tree records the control that opens each kind of page, not a second copy of the sitemap.

One theme. Body computed style on the home page is `rgb(17, 17, 17)` page and `rgb(255, 255, 255)` text. No theme toggle.

## Chrome on every marketing page

| Control | Opens |
|---|---|
| Logo | [https://www.vsco.co/](https://www.vsco.co/) |
| PRODUCTS (desktop dropdown, `role=button`) | Menu. Destinations below. |
| SOLUTIONS (desktop dropdown) | Menu. Destinations below. |
| COMMUNITY (desktop dropdown) | Menu. Destinations below. |
| RESOURCES (desktop dropdown) | Menu. Destinations below. |
| PRICING | [https://www.vsco.co/subscribe/plans](https://www.vsco.co/subscribe/plans) |
| LOG IN | [https://vsco.co/user/login](https://vsco.co/user/login). Wall. Stop. |
| TRY FOR FREE | [https://www.vsco.co/subscribe/plans](https://www.vsco.co/subscribe/plans) |
| Top promo LEARN MORE | [https://www.vsco.co/studio-pro/desktop](https://www.vsco.co/studio-pro/desktop) |
| Phone menu (`aria-label=menu`) | Drawer: PRODUCTS, SOLUTIONS, COMMUNITY, RESOURCES, PRICING, GET THE APP, SIGN UP, LOG IN |
| Phone GET THE APP | [https://www.vsco.co/downloads](https://www.vsco.co/downloads) |
| Phone SIGN UP | [https://vsco.co/user/signup](https://vsco.co/user/signup). Wall. Stop. |
| Footer language "English" | Links to [https://www.vsco.co/](https://www.vsco.co/), [https://www.vsco.co/pt-br](https://www.vsco.co/pt-br), [https://www.vsco.co/es-mx](https://www.vsco.co/es-mx). Same marketing tree in another language. |
| Cookie banner CLOSE | Local hide of the OneTrust banner. Not clicked for capture (banner is hidden, never accepted). |
| YOUR PRIVACY CHOICES | OneTrust preference center (Allow All, Reject All, Confirm My Choices, vendor lists). Not clicked. |
| Footer legal links | About, careers, terms, privacy, community guidelines, Hub agreement, Workspace agreement |

## PRODUCTS menu

| Item | Opens |
|---|---|
| VSCO App | [https://www.vsco.co/features/photo-editor](https://www.vsco.co/features/photo-editor) |
| VSCO Studio Pro | [https://www.vsco.co/studio-pro](https://www.vsco.co/studio-pro) |
| VSCO Galleries | [https://www.vsco.co/galleries](https://www.vsco.co/galleries) |
| AI Lab | [https://www.vsco.co/ai-lab](https://www.vsco.co/ai-lab) |
| Feed + Profile | [https://vsco.co/feed](https://vsco.co/feed). Cloudflare challenge in this session. Signed-in community. Stop. |
| VSCO Spaces | [https://www.vsco.co/features/spaces](https://www.vsco.co/features/spaces) |
| VSCO Capture | [https://www.vsco.co/capture](https://www.vsco.co/capture) |
| VSCO Canvas | [https://www.vsco.co/features/canvas](https://www.vsco.co/features/canvas) |
| VSCO Workspace | [https://www.vsco.co/workspace](https://www.vsco.co/workspace) |
| VSCO Hub | [https://www.vsco.co/vsco-hub](https://www.vsco.co/vsco-hub) |
| VSCO Sites | [https://www.vsco.co/features/sites](https://www.vsco.co/features/sites) |
| The Freelance Photographer | [https://www.vsco.co/the-freelance-photographer](https://www.vsco.co/the-freelance-photographer) |
| Apps + Downloads, and each View | [https://www.vsco.co/downloads](https://www.vsco.co/downloads) plus anchors `#vsco-app`, `#vsco-studio-pro`, `#vsco-galleries`, `#vsco-capture`, `#tfp` |

## SOLUTIONS menu

| Item | Opens |
|---|---|
| VSCO Pro | [https://www.vsco.co/pro](https://www.vsco.co/pro) |
| VSCO One | [https://www.vsco.co/vsco-one](https://www.vsco.co/vsco-one) |
| Photo Editing | [https://www.vsco.co/features/photo-editor](https://www.vsco.co/features/photo-editor) |
| Video Editing | [https://www.vsco.co/features/video-editor](https://www.vsco.co/features/video-editor) |
| Color Grading | [https://www.vsco.co/solutions/color-grading](https://www.vsco.co/solutions/color-grading) |
| Digital Photography | [https://www.vsco.co/solutions/digital-photography](https://www.vsco.co/solutions/digital-photography) |
| Moodboarding | [https://www.vsco.co/solutions/moodboarding](https://www.vsco.co/solutions/moodboarding) |
| Studio Management | [https://www.vsco.co/solutions/studio-management](https://www.vsco.co/solutions/studio-management) |
| See all solutions | [https://www.vsco.co/solutions](https://www.vsco.co/solutions) |
| Photo Presets | [https://www.vsco.co/features/photo-filters](https://www.vsco.co/features/photo-filters) |
| Film Effects | [https://www.vsco.co/features/film-fx](https://www.vsco.co/features/film-fx) |
| Vintage Filters | [https://www.vsco.co/effects/vintage-filters](https://www.vsco.co/effects/vintage-filters) |
| Grain | [https://www.vsco.co/features/photo-grain](https://www.vsco.co/features/photo-grain) |
| Photo Effects | [https://www.vsco.co/effects](https://www.vsco.co/effects) |
| AI Editing | [https://www.vsco.co/ai-lab](https://www.vsco.co/ai-lab) |
| See all tools | [https://www.vsco.co/features](https://www.vsco.co/features) |
| Photographer, Videographer, Studio Manager, Wedding, Portrait, Content Creator | `/roles/<slug>` |
| See all roles | [https://www.vsco.co/roles](https://www.vsco.co/roles) |

## COMMUNITY menu

| Item | Opens |
|---|---|
| Live Events | [https://www.vsco.co/events](https://www.vsco.co/events) |
| Customer Stories | [https://www.vsco.co/try/with-vsco](https://www.vsco.co/try/with-vsco) |
| Feed | [https://vsco.co/feed](https://vsco.co/feed). Challenge. Stop. |
| Search | [https://vsco.co/search/people](https://vsco.co/search/people). Challenge. Stop. |

## RESOURCES menu

| Item | Opens |
|---|---|
| Learn the skills / Business Education | [https://www.vsco.co/vsco-one/education](https://www.vsco.co/vsco-one/education) |
| Photography Coaching | [https://www.vsco.co/the-freelance-photographer/photography-coaching](https://www.vsco.co/the-freelance-photographer/photography-coaching) |
| Portfolio Reviews, Workshops, Panels, Community, Toolkit | Anchors on [https://www.vsco.co/the-freelance-photographer](https://www.vsco.co/the-freelance-photographer) |
| See all TFP features | Same page |
| Photography Basics, Guides, Business | Index pages under those paths |
| Photographer Stories | [https://www.vsco.co/photographer-stories](https://www.vsco.co/photographer-stories) |
| Guides for Hiring | [https://www.vsco.co/hiring-guides](https://www.vsco.co/hiring-guides) |
| VSCO Blogs / What's New | [https://vsco.co/vsco/journal/p/1](https://vsco.co/vsco/journal/p/1). Challenge. Stop. |
| See all learning | [https://www.vsco.co/learn](https://www.vsco.co/learn) |
| Support Center | [https://support.vsco.co/en/](https://support.vsco.co/en/). Challenge. Stop. |
| Safety Center | [https://www.vsco.co/safety](https://www.vsco.co/safety) |
| Community Guidelines | [https://www.vsco.co/about/community-guidelines](https://www.vsco.co/about/community-guidelines) |

## Home page interactions

| Control | Opens |
|---|---|
| What's new, Create, Connect, Work tabs | Local panes on the same page. Cards link to product and story URLs (Joe Greer preset, Studio Pro desktop, The Fifty, plans, galleries, Canvas, events, messaging). |
| Previous slide / Next slide | Local carousels. No navigation. |
| Explore VSCO / Explore VSCO One / View all plans | Plans or product pages (`/vsco-one`, `/subscribe/plans`). |
| Explore creative tools / community tools / work solutions | `/features`, `/features/community`, `/features/business-tools` |
| FAQ rows on plans | Local accordion. Questions include plan differences and Workspace. |
| Copy code on the plans promo | Copies a published promo code. Not a form submit. Not clicked. |
| Select VSCO One / Select Pro | Checkout or signup path. Not clicked. Treated as a purchase wall. |
| Play video | Local or embedded player on product pages. Not a form. |

## Page families the home tree reaches

Each family is the same shell. Captures use one representative, named in the coverage table.

| Family | Example | What a control on it does |
|---|---|---|
| Product marketing | `/studio-pro`, `/galleries`, `/capture`, `/ai-lab`, `/workspace` | Same header. CTAs go to plans, downloads, or the app host. |
| Feature tool page | `/features/photo-editor`, `/features/photo-filters` | Same header. Sibling tools in the body. |
| Solution / role | `/solutions`, `/roles/photographers` | Same header. CTAs to plans or product pages. |
| Plans | `/subscribe/plans` | Accordions. Select buttons start a purchase. Not submitted. |
| Downloads | `/downloads` | Anchors for each app. Store badges leave the site. |
| Learn index and article | `/learn`, `/learn/how-to-edit-photos` | Article links. Same header and footer. |
| Stories and collections | `/photographer-stories`, `/photo-collections`, `/try/with-vsco` | Card links to one story. Same shell. |
| Effects index and effect | `/effects`, `/effects/vintage-filters` | Same shell. |
| The Fifty | `/50` and `/50/<state>` | State cards. Same shell. |
| About and legal | `/about`, `/about/careers`, `/about/terms-of-use`, `/about/privacy-policy` | Long text. Careers lists open roles. |
| Safety | `/safety`, `/safety/transparency-reports` | Same shell. |
| Hub marketing | `/vsco-hub`, `/vsco-hub/photographers` | Upgrade to Pro goes to plans. No public photographer directory form. |
| Release notes | `/release-notes` | Same shell. |
| Web Studio marketing | `/studio` | Marketing page. No file input. The editor is `studio.vsco.co`. |
| 404 | any unknown `www.vsco.co` path | Styled 404 inside the same chrome. |
| Locale home | `/pt-br`, `/es-mx` | Same tree, translated. |

## Walls (branch stops)

| URL | What loaded | Stopped because |
|---|---|---|
| [https://vsco.co/user/login](https://vsco.co/user/login) | 200. Title "Log in to VSCO". Visible fields: email (`identity`), password. Buttons: Log in, Forgot password, Log in with Google, Log in with Apple, Sign up. | Login wall. Password not typed. Google and Apple not clicked. |
| [https://vsco.co/user/signup](https://vsco.co/user/signup) | 200. Title "Signup for VSCO". Email field, Continue, Continue with Apple, Continue with Google. | Signup wall. Email not typed. Google and Apple not clicked. |
| [https://workspace.vsco.co/](https://workspace.vsco.co/) | Redirects to `https://vsco.co/user/login?app=workspace`. Same email and password fields. | Login wall. |
| [https://vsco.co/user/account](https://vsco.co/user/account) | Linked from the footer account cluster. | Account wall. Not opened. |
| [https://vsco.co/me](https://vsco.co/me) | Cloudflare "Just a moment" in this session. | Signed-in profile. Stop. |
| [https://vsco.co/feed](https://vsco.co/feed) | Cloudflare challenge. | Signed-in feed. Stop. |
| [https://vsco.co/search/people](https://vsco.co/search/people) | Cloudflare challenge. `www.vsco.co/search` redirects here. | People search. Stop. |
| [https://vsco.co/vsco/journal/p/1](https://vsco.co/vsco/journal/p/1) | Cloudflare challenge. | Journal. Stop. |
| [https://support.vsco.co/en/](https://support.vsco.co/en/) | Cloudflare challenge. | Support. Stop. |
| [https://studio.vsco.co/](https://studio.vsco.co/) | 200, title "VSCO Studio", empty body in headless. | Editor app, not the marketing system. |
| [https://canvas.vsco.co/](https://canvas.vsco.co/) | Sign up / log in gate plus a search field. | Account wall. Search not submitted. |
| [https://help.workspace.vsco.co/en/](https://help.workspace.vsco.co/en/) | Separate help center. | Out of the marketing tree. |

## Not present on the public marketing site

Dark theme toggle, toast, switch, radio group, data table, signed-in empty and loading states, destructive confirmation, onboarding, newsletter field (none on the home page). Plans FAQ is an accordion, not a separate dialog. Cookie preference center is a dialog and was not opened.
