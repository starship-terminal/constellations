# Retool public site tree

Mapped from the live homepage https://retool.com/ on 2026-11-20, before any
screenshot pass. Playwright loaded the page (HTTP 200, title "Build internal
software better, with AI. | Retool"). The desktop nav buttons expose
`aria-controls` panels that are already in the DOM. The published HTML sitemap
at https://retool.com/sitemap-page (227 links, 145 unique hrefs) lists the
same nav destinations plus the index samples below.

This tree records which control opens which page, menu, dialog or interaction.
A control that leaves the marketing origin, or that opens a login or signup
wall, stops that branch. No form is submitted. No email is typed. Google is
not clicked. The login-link request is not used.

## Shell

| Control | Opens |
|---|---|
| Logo "Retool" | Page `/` |
| Skip to main content | In-page `#main-content` |
| Banner "Get early access" | Page `/agents-waitlist` |
| Top link "Use cases" | Page `/use-cases` |
| Top link "Pricing" | Page `/pricing` |
| Button "Sign in" | Login wall `https://login.retool.com/auth/login?source=navbarcta`. Stop. Known probe: email and password, or Google, or a login link. Not typed, not clicked, not requested. |
| Button "Book a demo" | Page `/demo?meeting_page_source=navbarcta` (form; do not submit) |
| Button "Start for free" | Signup wall `https://login.retool.com/auth/signup?source=navbarcta`. Stop. |
| Button "Ask AI" (⌘K) | In-page search dialog. A result link "Go to docs" leaves for `https://docs.retool.com`. Do not submit a query that leaves the page. |
| Button "Open navigation" | Mobile drawer `#global-nav-mobile-menu` (visible at 390). Same three groups as the desktop menus. |
| Button "Play background video" / "Pause" | Toggles the hero background video. No navigation. |
| Button "Pause scrolling logos" / "Pause illustration" | Pauses a marquee or illustration. No navigation. |

## Desktop menu: Solution

Button "Solution" sets `aria-expanded=true` and shows
`#global-nav-menu-desktop-7dce14f92e3c` (about 734 by 372). Escape closes it.

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

## Desktop menu: Audience

Button "Audience" opens `#global-nav-menu-desktop-faaab62ecd3f`.

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
| DISCOVER | App gallery | Page `/app-gallery` |
| DISCOVER | Integrations | Page `/integrations` |
| DISCOVER | Templates | Page `/templates` |
| DISCOVER | Utilities | Page `/utilities` |
| DISCOVER | Blog | Page `/blog` |
| DISCOVER | Customer stories | Page `/customers` |
| DISCOVER | Videos | Page `/resources/videos` |
| DISCOVER | Resource hub | Page `/resources` |
| DEVELOPERS | Documentation | External `https://docs.retool.com/`. Separate product docs origin. |
| DEVELOPERS | Community | External `https://community.retool.com/`. |
| DEVELOPERS | Retool University | External `https://university.retool.com/`. |
| DEVELOPERS | API reference | External `https://docs.retool.com/reference/api/v2`. |
| DEVELOPERS | CLI reference | External `https://docs.retool.com/build/apps/reference/cli`. |
| DEVELOPERS | MCP server | External `https://docs.retool.com/org-users/guides/mcp`. |
| COMPANY | About | Page `/about` |
| COMPANY | Careers | Page `/careers` |
| COMPANY | Partners | Page `/partners` |
| COMPANY | Support | External `https://docs.retool.com/support`. |
| COMPANY | Newsroom | Page `/newsroom` |

The mobile drawer repeats these three groups under buttons that control
`#global-nav-menu-mobile-7dce14f92e3c`, `#global-nav-menu-mobile-faaab62ecd3f`
and `#global-nav-menu-mobile-a61efda0b862c09dd492ea6cd41520a7`.

## Homepage interactions that stay on the page

| Control | Opens |
|---|---|
| "Starter prompts" (`aria-haspopup=dialog`) | Prompt-picker dialog. Do not submit the prompt. |
| "Import code" (`aria-haspopup=dialog`) | Import dialog (React / Lovable / Replit). Do not upload or submit. |
| "Build with AI agents" (`aria-haspopup=dialog`) | Agent-builder dialog (Claude Code, Cursor, Codex, ChatGPT, Kiro CLI). Do not submit. |
| "Submit prompt" | Would send the hero prompt. Do not click. |
| "See what's new. Watch the film" | Film overlay or player on the homepage. |
| Card "Learn about the app builder" | Page `/build-enterprise-apps/apps` |
| Card links MCP / CLI / import docs | External docs.retool.com paths. Stop at the origin change. |
| "See the full list of integrations" | Page `/integrations` |
| "Learn about security and governance" | Page `/govern-enterprise-apps` |
| "View app gallery" | Page `/app-gallery` |
| App-gallery cards on the homepage | One page each under `/app-gallery/<slug>` (18 cards on the homepage). |
| Customer logo row | One page each under `/customers/<slug>` or a team page. |

## Footer

The footer repeats the Solution, Audience and Resources destinations, plus:

| Control | Opens |
|---|---|
| Start for free | Signup wall `https://login.retool.com/auth/signup?source=footercta`. Stop. |
| Book a demo | Page `/demo?meeting_page_source=footercta` |
| Retool on LinkedIn | External `https://www.linkedin.com/company/tryretool/`. Stop. |
| Retool on Twitter/X | External `https://x.com/retool`. Stop. |
| Retool on Reddit | External `https://www.reddit.com/r/Retool/`. Stop. |
| Terms of use | External `https://docs.retool.com/legal` |
| Privacy policy | External `https://docs.retool.com/legal/privacy-policy` |
| Security | External `https://docs.retool.com/legal/security` |
| Trust Center | External `https://trust.retool.com/` |
| Report abuse | `mailto:` link. Do not open. The address is not written into this package. |
| Changelog | External `https://docs.retool.com/changelog` |
| Status | External `https://retool.statuspage.io/` |
| Site map | Page `/sitemap-page` |

## Sitemap index samples

https://retool.com/sitemap-page groups further same-origin pages. Each item is
a page. "View all" returns to the parent index.

| Group | Sample pages |
|---|---|
| Customer stories | `/customers/doordash`, `/customers/ramp`, `/customers/snowflake`, `/customers/greenly`, `/customers/remitly`, `/customers/plaid`, `/customers/equipmentshare`, `/customers/westhill`, `/customers/orangetheory`, `/customers/holland-and-barrett` |
| Blog | `/blog/retool-launches-react-ai-app-builder`, `/blog/best-react-calendar-components`, `/blog/top-redis-guis`, `/blog/the-react-lifecycle-methods-and-hooks-explained`, `/blog/filtering-data-in-react-filter-map-and-for-loops`, `/blog/how-low-code-for-manufacturing-transforms-operations`, `/blog/how-to-make-your-react-native-apps-work-on-the-web`, `/blog/building-a-react-navbar`, `/blog/expo-cli-vs-react-native-cli`, `/blog/state-of-ai-h1-2024` |
| Use cases | `/use-case/react-components`, `/use-case/front-end-database`, `/use-case/admin-panels`, `/use-case/postgresql-gui`, `/use-case/mysql-gui`, `/use-case/sql-gui`, `/use-case/sql-front-end`, `/use-case/google-sheets-front-end`, `/use-case/openai-gui-frontend` |
| Templates | `/templates/business-intelligence-dashboard`, `/templates/snowflake-dashboard`, `/templates/data-visualization-dashboard`, `/templates/library-management-system`, `/templates/rest-api-dashboard`, `/templates/kpi-dashboard`, `/templates/postgresql-admin-panel`, `/templates/rest-api-admin-panel`, `/templates/firebase-admin-panel`, `/templates/google-sheets-dashboard` |
| Integrations | `/integrations/rest-api`, `/integrations/google-sheets`, `/integrations/postgresql`, `/integrations/mysql`, `/integrations/mongodb`, `/integrations/aws-s3`, `/integrations/firebase`, `/integrations/snowflake`, `/integrations/graphql`, `/integrations/aws-dynamodb` |
| Misc | `/vertical/manufacturing`, `/industry/financial-services`, `/ai-app-generation`, `/competitor/airtable`, `/competitor/lovable`, `/competitor/powerapps`, `/competitor/replit` |

Blog, customer, template, integration, use-case and gallery indexes paginate
or list more items than the sitemap samples. Those extra items are the same
page type. Capture records the index plus one representative detail page,
and names the rest as the same pattern.

## Stopped branches

| Control | Why the branch stops |
|---|---|
| Sign in | Login wall at login.retool.com. Email, password, Google and the login link are not used. |
| Start for free | Signup wall at login.retool.com. |
| Any control that redirects to login.retool.com or a signup form | Record the URL and stop. |
| Google sign-in | Not clicked. |
| Demo, waitlist, newsletter and contact forms | Opened only to see the fields. Never submitted. No email, phone, location, birthday, plan, survey or onboarding field is filled. |
| docs.retool.com, community.retool.com, university.retool.com, trust.retool.com, statuspage.io, social networks | Different products or off-site. Not part of the marketing-site capture. |
