# LottieFiles public site tree

Mapped from https://lottiefiles.com/ on 2026-11-21, signed out, in headless Chromium at 1440x900 before any package screenshot. Phone header notes are from a 390x844 context. No form was submitted. No password, code, or profile field was typed.

The marketing site is one light theme (`color-scheme: normal`, page background `oklch(1 0 0)`). No theme switch was found in the public header, footer, or pricing page. Cookie copy is a banner ("We use cookies... Privacy Policy / Got It"). The capture hides that banner. It does not click Got It.

## Auth walls (stop)

| Control | What it opens | Stop |
|---|---|---|
| Header **Log in** | Modal iframe `https://login.lottiefiles.com/login?origin=https%3A%2F%2Flottiefiles.com%2F&mode=modal&return_to_url=https%3A%2F%2Fapp.lottiefiles.com...` | Yes. Do not type. |
| Header **Sign up** | Modal iframe `https://login.lottiefiles.com/register?origin=https%3A%2F%2Flottiefiles.com%2F&mode=modal&return_to_url=https%3A%2F%2Fapp.lottiefiles.com...` | Yes. Do not type. |
| Direct `https://lottiefiles.com/login` | 404 "Oh snap! We couldn't find th..." | Recorded. Not a form. |
| Direct `https://accounts.lottiefiles.com/login` | 200 "Log in with your organization's email" plus email and password fields | Stop. Do not type. |
| Direct `https://login.lottiefiles.com/login` | 200 "Log in / Log in with Google / Continue with enterprise log in" | Stop. Do not click Google. Do not type. |
| Direct `https://login.lottiefiles.com/register` | 200 "Create an account / Sign up with Google" | Stop. Do not click Google. Do not type. |
| **Get started for free**, **Premium Lottie Animations** | `http://app.lottiefiles.com/` or `https://app.lottiefiles.com/premium-animations` | App host. If it asks for login, stop that branch. |
| Animation **Save animation**, **Download**, **Edit**, **Edit with AI** | Signed-in actions on a public animation page | Do not click through a login wall. |

## Header (desktop)

The bar is a Radix navigation menu. Products, Tools, and Customers open on click. Integrations and Learn open on hover (a click left `data-state` closed in the probe). Escape closes them.

| Control | Opens |
|---|---|
| Logo | https://lottiefiles.com/ |
| **Products** menu | Platform, Lottie Creator, Creator MCP, After Effects plugin, Figma plugin, dotLottie, Motion System, DAM, State Machines, Motion Tokens, AI Tools, Free animations, Premium (app host), Motion Templates, Marketplace, Hire animators, Publish to community |
| **Integrations** menu (hover) | Developer docs (docs.lottiefiles.com), dotLottie Runtimes, ThorVG (github.com), Figma, After Effects, Canva, Webflow, Framer, Explore all integrations, GitHub players (web, iOS, Android, Flutter) |
| **Tools** menu | Preview, Web Player, Accessibility Analyzer, All tools, Prompt to Vector, Raster to Vector, AEP to Lottie, Design to SVG, SVG to Lottie, Video to Lottie, Animation to Lottie, Lottie Editor, JSON Editor, Optimizer, Lottie to dotLottie, Lottie to GIF/MP4/WebM/MOV |
| **Customers** menu | All case studies, Wise, Robinhood, Duolingo, Canva, Uber, CNN Create, State of Motion, Motion Maturity, Use Cases, Built with Lottie |
| **Learn** menu (hover) | Certifications (creator, AE, Figma, Webflow, all), Docs, Education, Blog, Enterprise community course, Community, Evangelists, Challenges, recent tutorials and blog posts |
| **Pricing** link | https://lottiefiles.com/pricing |
| **Search animations** / **Search animations... ⌘ K** | In-page search dialog, placeholder "Search for animations...". Typing a query is a search interaction, not a form submit. |
| **En** menu | English, Español, Português, 한국어, 日本語, Français, Deutsch. Locale switch, not a new page. Capture stays on English. |
| **Log in** / **Sign up** | Auth walls above. |
| **Publish animation** (below the fold on home) | Auth-gated publish flow. Stop if it opens login. |

## Home interactions (not navigation)

| Control | Interaction |
|---|---|
| Dismiss (aria-label) | Closes the "Your ideas, in motion" promo strip. |
| Hero feature buttons | Tiny file format, Motion Tokens, Interactive, Dev ready. In-page feature switch. |
| Product tabs | Lottie AI, Creator MCP, Lottie Creator, LottieFiles for Figma, LottieFiles for After Effects. |
| Workflow tabs | Figma, After Effects, Canva, Webflow, Framer, Premier Pro. |
| AI feature cards | Motion Copilot, Prompt to Vector, Raster to Vector in Figma, Prompt to Themes. |
| Logo carousel | Scroll left / Scroll right. |
| Animation filters | Free & Premium, interactivity, theming, loading, success, confetti, ai, arrow, login, error, check, money, 404. Filter chips on the public library strip. |
| Animation cards | One public detail page, for example `/free-animation/loader-cat-dWUie0iIVk`. |
| Cookie **Got It** | Consent. Hidden, never clicked. |

## Phone (390)

The desktop nav buttons are not in the top 180px. The top bar is the logo link. A dismiss control sits on the promo. The full nav is reached by scrolling to the footer links, or by opening a page directly. Capture records the phone header as it paints and opens the same public URLs.

## Public pages captured as representatives

One page per pattern, plus the nav destinations that show a distinct component. Infinite animation grids are truncated.

| Page | URL | Why |
|---|---|---|
| Home | `/` | Shell, promo, tabs, search, cookie banner |
| Pricing | `/pricing` | Plan cards, billing comparison |
| Platform | `/platform` | Product marketing |
| Lottie Creator | `/lottie-creator` | Product marketing |
| Integrations index | `/integrations` | Plugin grid |
| Figma plugin | `/plugins/figma` | Plugin detail |
| Tools index | `/tools` | Tool grid |
| Preview | `/preview` | Tool with a file field (not submitted) |
| Free animations | `/featured-free-animations` | Filterable catalog |
| Animation detail | `/free-animation/loader-cat-dWUie0iIVk` | Player, download menu (opened, not downloaded) |
| Marketplace | `/marketplace` | Marketplace listing |
| Case studies | `/case-studies` | Card list |
| One case study | `/case-studies/wise` | Article |
| Blog | `/blog` | Article list |
| What is Lottie | `/what-is-lottie` | Editorial |
| Education | `/education` | Learning index |
| Contact sales | `/contact-sales` | Form present, not filled, not submitted |
| 404 | `/login` | Known missing route |
| Privacy | `/page/privacy-policy` | Long legal page, truncated |

External hosts (docs, help, forum, feedback, GitHub, lottie.ai, lottie.community, app.lottiefiles.com) are named in this tree and not captured as the design system of lottiefiles.com.

## Not present on the public site

Dark theme. Signed-in app shell, workspace, toast after a real save, destructive confirmation, onboarding, account settings. Those rows stay "not captured" or "not present" in the package coverage table.
