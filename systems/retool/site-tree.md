# Retool public site tree

Mapped from the live homepage https://retool.com/ on 2026-11-21. The page
returned HTTP 200 with the title "Build internal software better, with AI. |
Retool". `html` class included `dark`. Desktop nav buttons expose
`aria-controls` panels that are already in the DOM. The published HTML sitemap
at https://retool.com/sitemap-page still lists the same nav destinations.

This tree records which control opens which page, menu, dialog or stopped
branch. A control that leaves the marketing origin, or that opens a login or
signup wall, stops that branch. No form was submitted. No email, password,
code, phone or address was typed. No identity provider was clicked.

## Shell

| Control | Opens |
|---|---|
| Logo "Retool" | Page `/` |
| Banner "Get early access" | Page `/agents-waitlist` |
| Button "Solution" | Desktop menu `#global-nav-menu-desktop-7dce14f92e3c`. Painted at 1440. |
| Button "Audience" | Present in the DOM (`#global-nav-menu-desktop-faaab62ecd3f`) but `display: none` at 1440. Painted only inside the mobile drawer and the footer. |
| Button "Resources" | Desktop menu `#global-nav-menu-desktop-a61efda0b862c09dd492ea6cd41520a7`. Painted at 1440. The first Discover item is Integrations. App gallery is a top-level link, not a menu row. |
| Link "Use cases" | Page `/use-cases` |
| Link "App gallery" | Page `/app-gallery`. Top-level at 1440 on 2026-11-21. |
| Link "Pricing" | Page `/pricing` |
| Button "Ask AI" | In-page search dialog. A result can leave for `https://docs.retool.com`. The dialog was opened empty and closed. No query was typed. |
| Link "Sign in" | Login wall `https://login.retool.com/auth/login?source=navbarcta`. Stop. |
| Link "Book a demo" | Page `/demo?meeting_page_source=navbarcta` (form; not submitted) |
| Link "Start for free" | Signup wall `https://login.retool.com/auth/signup?source=navbarcta`. Stop. |
| Button "Open navigation" | Mobile drawer (visible at 390). Same three groups as the desktop menus. |
| Button "Pause background video" | Toggles the hero background video. No navigation. |
| Button "Pause scrolling logos" / "Pause illustration" | Pauses a marquee or illustration. No navigation. |

## Desktop menu: Solution

Button "Solution" sets `aria-expanded=true` and shows
`#global-nav-menu-desktop-7dce14f92e3c`. Escape closes it.

| Group | Control | Opens |
|---|---|---|
| Featured | AI app security | Page `/secure-vibe-coding` |
| PLATFORM | Build | Page `/build-enterprise-apps` |
| PLATFORM | Launch | Page `/launch-enterprise-apps` |
| PLATFORM | Scale | Page `/scale-enterprise-apps` |
| PLATFORM | Govern | Page `/govern-enterprise-apps` |
| CAPABILITIES | Agents | Page `/build-enterprise-apps/agents` |
| CAPABILITIES | App builder | Page `/build-enterprise-apps/apps` |
| CAPABILITIES | AI primitives | Page `/ai` |
| CAPABILITIES | Workflows | Page `/build-enterprise-apps/workflows` |
| CAPABILITIES | Database | Page `/build-enterprise-apps/database` |
| CAPABILITIES | External apps | Page `/launch-enterprise-apps/external` |
| CAPABILITIES | Mobile apps | Page `/launch-enterprise-apps/mobile` |
| CAPABILITIES | Self-hosting | Page `/govern-enterprise-apps/self-hosted` |

## Audience menu

The desktop Audience button is in the DOM and `display: none` at 1440 on
2026-11-21. The same destinations are painted in the mobile drawer
(`#global-nav-menu-mobile-faaab62ecd3f`) and in the footer. The panel id
that the hidden desktop button controls is
`#global-nav-menu-desktop-faaab62ecd3f`.

| Group | Control | Opens |
|---|---|---|
| TEAM | Data | Page `/for/data-teams` |
| TEAM | Engineering | Page `/for/engineering-teams` |
| TEAM | Operations | Page `/for/operations-teams` |
| INDUSTRY | Financial services | Page `/for/financial-services` |
| INDUSTRY | Manufacturing | Page `/for/manufacturing` |
| TYPE | Enterprise | Page `/enterprise` |
| TYPE | Startups | Page `/startups` |

## Desktop menu: Resources

Button "Resources" opens `#global-nav-menu-desktop-a61efda0b862c09dd492ea6cd41520a7`.

| Group | Control | Opens |
|---|---|---|
| DISCOVER | Integrations | Page `/integrations` |
| DISCOVER | Templates | Page `/templates` |
| DISCOVER | Utilities | Page `/utilities` |
| DISCOVER | Blog | Page `/blog` |
| DISCOVER | Customer stories | Page `/customers` |
| DISCOVER | Videos | Page `/resources/videos` |
| DISCOVER | Resource hub | Page `/resources` |
| DEVELOPERS | Documentation | External `https://docs.retool.com/`. Stop. |
| DEVELOPERS | Community | External `https://community.retool.com/`. Stop. |
| DEVELOPERS | Retool University | External `https://university.retool.com/`. Stop. |
| DEVELOPERS | API reference | External `https://docs.retool.com/reference/api/v2`. Stop. |
| DEVELOPERS | CLI reference | External `https://docs.retool.com/build/apps/reference/cli`. Stop. |
| DEVELOPERS | MCP server | External `https://docs.retool.com/org-users/guides/mcp`. Stop. |
| COMPANY | About | Page `/about` |
| COMPANY | Careers | Page `/careers` |
| COMPANY | Partners | Page `/partners` |
| COMPANY | Support | External `https://docs.retool.com/support`. Stop. |
| COMPANY | Newsroom | Page `/newsroom` |

The mobile drawer repeats these three groups. At 390 the drawer button is
"Open navigation".

## Homepage interactions that stay on the page

| Control | Opens |
|---|---|
| "Starter prompts" (`aria-haspopup=dialog`) | Prompt-picker dialog. Not submitted. |
| "Import code" (`aria-haspopup=dialog`) | Import dialog (React / Lovable / Replit). Not uploaded, not submitted. |
| "Build with AI agents" (`aria-haspopup=dialog`) | Agent-builder dialog (Claude Code, Cursor, Codex, ChatGPT, Kiro CLI). Not submitted. |
| "Submit prompt" | Would send the hero prompt. Not clicked. |
| "See what's new. Watch the film" | Film overlay or player on the homepage. |
| Card links under the hero | Same-origin product pages, or external docs.retool.com paths. The docs origin stops the branch. |

## Footer

The footer repeats the Solution, Audience and Resources destinations, and adds
AppGen (`/ai-app-generation`). Community, API reference, CLI reference, MCP
server and Support stay in the Resources menu and are not repeated in the
footer column that was read on 2026-11-21.

| Control | Opens |
|---|---|
| Start for free | Signup wall `https://login.retool.com/auth/signup?source=footercta`. Stop. |
| Book a demo | Page `/demo?meeting_page_source=footercta` |
| Retool on LinkedIn | External `https://www.linkedin.com/company/tryretool/`. Stop. |
| Retool on Twitter/X | External `https://x.com/retool`. Stop. |
| Retool on Reddit | External `https://www.reddit.com/r/Retool/`. Stop. |
| Terms of use | External `https://docs.retool.com/legal`. Stop. |
| Privacy policy | External `https://docs.retool.com/legal/privacy-policy`. Stop. |
| Security | External `https://docs.retool.com/legal/security`. Stop. |
| Trust Center | External `https://trust.retool.com/`. Stop. |
| Report abuse | `mailto:` link. Not opened. The address is not written into this package. |
| Changelog | External `https://docs.retool.com/changelog`. Stop. |
| Status | External `https://retool.statuspage.io/`. Stop. |
| Site map | Page `/sitemap-page` |

## Pages captured from this tree

Desktop 1440 x 900, painted dark: homepage (default, full, Solution menu,
Resources menu, empty Ask AI, starter prompts), pricing, use cases and one
use-case detail, each Solution and Audience destination, app gallery,
integrations and one integration, templates and one template, utilities,
blog and one post (`/blog/ai-agent-governance-agent-org-chart`), customers and one story, videos, resource hub, about,
careers, partners, newsroom, demo (fields visible, not submitted), agents
waitlist (fields visible, not submitted), sitemap, AI app security, AppGen,
and one competitor page.

Phone 390 x 844: homepage (default, full, open drawer, Solution group) and
pricing (default, full).

Login and signup walls were photographed empty and the branch stopped.

## Stopped branches

| Control | Why the branch stops |
|---|---|
| Sign in | Login wall at login.retool.com. Email, password, Google and any login link are not used. |
| Start for free | Signup wall at login.retool.com. |
| Any control that redirects to login.retool.com | Record the URL and stop. |
| Google or any other identity provider | Not clicked. |
| Demo, waitlist, newsletter and contact forms | Opened only to see the empty fields. Never submitted. |
| docs.retool.com, community.retool.com, university.retool.com, trust.retool.com, statuspage.io, social networks | Different products or off-site. |
| Signed-in app | Not entered. `login-extracted` stays not-started. |
