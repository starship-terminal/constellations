# Rive public site tree

Mapped from https://rive.app/ in headless Chromium on 2026-11-21, before screenshots. Desktop viewport 1440×900. Phone viewport 390×844. No form was submitted. No password, code, or account field was typed.

The marketing site paints one dark theme (`body` background `rgb(0, 0, 0)`, Framer `--token-*` on `body`). Docs paint `html.dark` and expose a "Change theme preference" control. That control was not used to invent a light theme; a click that only opens a preference UI is recorded below.

## Header (desktop)

Fixed bar. Logo link "Rive home" opens `/`.

| Control | Opens |
|---|---|
| PRODUCTS (`button.rn-top`, `aria-controls="rive-nav-panel-0"`) | Mega menu, not a page. Escape or a click outside closes it. |
| USE CASES (`button.rn-top`, `aria-controls="rive-nav-panel-1"`) | Mega menu. |
| RESOURCES (`button.rn-top`, `aria-controls="rive-nav-panel-2"`) | Mega menu. |
| PRICING | `/pricing` |
| DOWNLOADS | `/downloads` |
| DOCS | `https://rive.app/docs/getting-started/introduction` |
| GET STARTED | `https://editor.rive.app` (editor app host; not the marketing page `/editor`) |

### PRODUCTS menu

| Link | Destination |
|---|---|
| Rive Editor | `/editor` |
| Rive CLI | `/agents` |
| Game Engine | `/games` |
| Downloads | `/downloads` |
| Runtimes | `/runtimes` |
| Renderer | `/renderer` |
| The .riv Format | `/blog/a-new-graphics-format-for-the-interactive-era` |
| All Features | `/features` |
| AnimaScript | `https://rive.app/rasc/index.html` |
| Marketplace | `https://rive.app/marketplace/` |
| Promo card | `/agents` |

### USE CASES menu

| Link | Destination |
|---|---|
| Apps | `/use-cases/mobile-apps` |
| Websites | `/use-cases/websites` |
| Product Design | `/use-cases/product-design` |
| Games | `/games` |
| Game UI | `/game-ui` |
| Characters | `/use-cases/character-animation` |
| Vehicles | `/use-cases/automotive` |
| Broadcast | `/use-cases/broadcast` |
| Film & TV | `/use-cases/film-tv` |
| All Use Cases | `/use-cases` |
| Spotify | `/blog/spotify-used-rive-for-spotify-wrapped-2025` |
| Duolingo | `/blog/duolingo-s-ai-powered-video-call-brings-lily-to-life` |
| LinkedIn | `/blog/linkedin-year-in-review-2025-built-with-rive` |
| Figma | `/blog/figma-s-new-homepage-is-full-of-rive-animations` |
| Intercom | `/blog/intercom-s-product-animation-evolution-embracing-rive` |
| Pocketwatch Games | `/blog/pocketwatch` |
| All Case Studies | `/blog/case-studies` |
| Rive vs HTML | `/rive-vs-html` |
| Rive vs Lottie | `/blog/rive-as-a-lottie-alternative` |
| Rive vs After Effects | `/blog/rive-vs-after-effects` |
| Rive vs Animate | `/blog/adobe-animate-alternative-rive-is-what-flash-should-have-become` |
| Rive vs Spine | `/rive-vs-spine` |
| Figma to Rive | `/figma-to-rive` |
| Promo card | `/games` |

### RESOURCES menu

| Link | Destination |
|---|---|
| Documentation | `https://rive.app/docs/getting-started/introduction` |
| Blog | `/blog` |
| Changelog | `https://community.rive.app/c/announcements/` (community host) |
| Video Tutorials | YouTube channel (external) |
| Community | `https://community.rive.app/` |
| Discord | `https://discord.gg/rive-app` (external) |
| Experts | `/experts` |
| Feature Requests | `https://community.rive.app/c/feature-requests/` |
| Bug Reports | `https://community.rive.app/c/bug-reports/` |
| Support | `https://community.rive.app/c/support/` |
| Voyager Support | `https://community.rive.app/c/voyager-support/` |
| Enterprise | `/enterprise` |
| Contact | `/contact` |
| Careers | `/careers` |
| Press | `/blog/press` |
| Newsletter | `/newsletter` |
| Promo card | `/newsletter` |

## Header (phone)

`button[aria-label="Open menu"]` (32×32, class `rn-mob`) opens a sheet. The sheet shows:

| Control | Opens |
|---|---|
| Close menu | Closes the sheet. |
| PRODUCTS | Expands the products list inside the sheet (same destinations as the desktop menu). |
| USE CASES | Expands the use-cases list. |
| RESOURCES | Expands the resources list. |
| PRICING | `/pricing` |
| DOWNLOADS | `/downloads` |
| DOCS | `https://rive.app/docs/getting-started/introduction` |
| GET STARTED | `https://editor.rive.app` |

## Home page interactions (`/`)

| Control | What it does |
|---|---|
| Show Rive City, Show Sentinel, Show Dead End Drive, Show Rocket Squadron, Show RiveBox, Show Spotify Wrapped, Show Shoe configurator, Show Dashboard, Show Duolingo | Segmented demo switcher. Swaps the hero demo in place. Does not navigate. |
| PLAY IT LIVE | External demo host `https://rive-city-cr4bhd.rive.to/` (changes with the selected demo). |
| GET SOURCE | External GitHub repo for the selected demo. |
| COPY, COPY STARTER PROMPT | Copies a prompt to the clipboard. Does not navigate. Not a form submit. |
| Step anchors 01–05 | In-page `#step-1` … `#step-5`. |
| Feature cards (Rigging, State Machine, Data Binding, and the rest) | Docs URLs under `https://rive.app/docs/editor/…` or `https://rive.app/docs/scripting/…`. |
| orbit.as, bounce.as, closure.as | In-page script specimen switcher. |
| RESET, FORMAT | In-page code specimen controls. Not a form submit. |
| Footer SIGN UP (`button.rnf-btn`) | Sits on the newsletter email field. Not clicked. No form was submitted. |
| Your Privacy Choices | `/#cookie-settings` |
| Merch | `https://merch.rive.app` (external shop) |
| llms.txt | `https://rive.app/llms.txt` |
| Social links | YouTube, X, Instagram, GitHub, Dribbble, Discord. External. |

## Footer (same on marketing pages)

| Link | Destination |
|---|---|
| Terms | `https://rive.app/docs/legal/terms-of-service` |
| Privacy | `https://rive.app/docs/legal/privacy-policy` |
| Data Protection Addendum | `https://rive.app/docs/legal/data-protection-addendum` |
| Newsletter email + SIGN UP | Form with one email field, placeholder `email@rive.app`. Not submitted. |

## Other marketing controls

| Page | Control | Opens |
|---|---|---|
| `/pricing` | YEARLY / MONTHLY | In-page billing period toggle. Does not navigate. |
| `/pricing` | GET STARTED | `https://editor.rive.app` or signup redirect (wall). Not followed as a submit. |
| `/pricing` | GET IN TOUCH | `/contact` |
| `/pricing` | TELL YOUR CODING AGENT / COPY | Clipboard. |
| `/features` | Previous / Next | In-page feature carousel. |
| `/features` | CHANGELOG | Community announcements (external host). |
| `/newsletter` | VIEW PAST NEWSLETTERS | In-page or archive list. Email field not filled. |
| `/careers` | VIEW OPEN ROLES | In-page roles. |
| `/careers` | Story buttons | In-page story panels. |
| `/experts` | BROWSE EXPERTS | In-page list. |
| `/experts` | BECOME AN EXPERT | Application path. Not submitted. |
| `/marketplace/` | MARKETPLACE button | Marketplace nav. |
| `/marketplace/` | Search the Marketplace | Text field. Not submitted. |
| `/contact` | No public message form on first paint. Footer email field only. Not submitted. |  |

## Login and signup walls (stop)

Recorded, not entered.

| URL | What it shows | Stop |
|---|---|---|
| `https://rive.app/login/` | Title "Rive - Log in". CONTINUE WITH GOOGLE, email or username, password, SHOW, LOG IN, Forgot password (`/forgot/`), Use single sign-on (`/login/sso`), Create account (`/signup/`). | Password was not submitted. Google and SSO were not clicked. |
| `https://rive.app/signup/` | Title "Rive - Sign up". Account creation wall. | No account created. No profile, birthday, plan, survey, or newsletter field filled. |
| `https://editor.rive.app` | GET STARTED and OPEN THE EDITOR leave the marketing host. | Not captured as an app. If it asks for login, that branch stops. |
| Community, Discord, YouTube, merch | Other hosts. | Out of the rive.app public marketing capture. |

## Docs (`/docs/…`)

`/cli` redirects to `/docs/cli/getting-started`. The docs shell has a sidebar (Learn, Support, Get Rive, Home, Editor, Scripting, Runtimes, CLI), a search field ("Search... ⌘K"), and "Change theme preference". Docs are a second surface (Mintlify-style, `html.dark`). Captured as the public docs home plus the theme control if it opens without a login wall. Search was not submitted.

## Reachable public pages used for the capture

Marketing (Framer, one dark theme), both widths unless noted:

- `/` home
- `/pricing` (yearly default, monthly toggle)
- `/downloads`
- `/editor` (marketing page, not the editor app)
- `/agents`
- `/games`
- `/game-ui`
- `/runtimes`
- `/renderer`
- `/features`
- `/use-cases` and the eight use-case pages
- `/blog`, `/blog/case-studies`, `/blog/press`, one published case study
- comparison pages: `/rive-vs-html`, `/rive-vs-spine`, `/figma-to-rive`, plus the three comparison posts linked from the menu
- `/experts`, `/enterprise`, `/contact`, `/careers`, `/newsletter`
- `/marketplace/`
- `/rasc/index.html`
- docs introduction and one docs section

External hosts, login, signup, SSO, forgot-password, and the editor app are boundaries.
