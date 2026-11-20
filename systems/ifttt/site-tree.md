# IFTTT public site tree

Mapped 2026-11-21 with headless Playwright before any screenshot. `https://ifttt.com/` redirects to `https://ifttt.ai/` (HTTP 200, title "The easiest way to automate anything - IFTTT"). One light theme: `color-scheme: normal`, body background `rgb(255, 255, 255)`, no `data-theme`. `prefers-color-scheme: dark` does not switch the page. Desktop header links are always visible. At 390 wide the same links sit behind a hamburger (`button.closed`, `aria-expanded` flips to `true`, class becomes `open`).

No cookie or consent dialog appeared on the pages below. Search is a lookup overlay, not a submitted form. Login, signup, checkout, password reset, and sales contact are walls: the URL is recorded and that branch stops. Nothing was typed into a password, email, profile, newsletter, or survey field. Google, Apple, and Facebook buttons were not clicked.

## Global chrome (every public page)

| Control | Opens |
|---|---|
| Wordmark "The IFTTT.ai home page" | [https://ifttt.ai/](https://ifttt.ai/) |
| Explore | [https://ifttt.ai/explore](https://ifttt.ai/explore) (a page, not a menu; hover opens nothing) |
| Plans | [https://ifttt.ai/plans](https://ifttt.ai/plans) |
| Log in | [https://ifttt.ai/login](https://ifttt.ai/login) signup/login wall. Stop. |
| Get started | [https://ifttt.ai/join?source=site-header](https://ifttt.ai/join?source=site-header) signup wall. Stop. |
| Search (desktop: input already in the header, `#universal-search-input`, placeholder "Search for Applets, services, etc."; phone: `button[aria-label="Search"]` opens the same field) | In-page suggestion list. Typing "hue" listed public services (Philips Hue, Sengled, MagicHue, and others) plus "See all results". Escape closes it. Not submitted. |
| Close search | `button[aria-label="Close search"]`, phone only, hidden until search is open |
| Mobile menu (`button.closed` at 390) | Drawer: Explore, Plans, Log in, Get started. Close returns `aria-expanded=false`. |
| Footer Explore, Services, Stories, Applets, IFTTT.ai MCP, Help Center, Content Map, Search, Plans, Developer docs | Same destinations as the rows below |
| Footer Top Integrations | Pair pages such as `/connect/discord/instagram` |
| Footer Latest Stories | Story pages under `/explore/<slug>` |
| Footer Developers, Partner program, Careers, Contact, About, Privacy | Company and legal pages below |
| Footer app badges | Apple App Store and Google Play (external). Not followed. |
| Footer social | Facebook, LinkedIn, Instagram, YouTube, Twitter, TikTok, Reddit (external). Not followed. |

## Home (`/`)

| Control | Opens |
|---|---|
| Start building (hero button) | [https://ifttt.ai/join?source=homepage-hero](https://ifttt.ai/join?source=homepage-hero) signup wall. Stop. |
| Join today / Join today (animated demo) | `/join?source=how-it-works-module` and `?source=how-it-works-animation`. Signup wall. Stop. |
| Featured tabs (role=tab): Popular, Business, Productivity, AI-powered, Smart home, iOS and Android | Same page. Swaps the applet card row. No navigation. |
| Applet card | `/applets/<id>-<slug>` public applet page |
| Explore all Applets | `/explore?source=featured-module` |
| Service logos | `/<service>?source=homepage-services` (Slack, Gmail, Hue, and others) |
| See all services | `/explore/services?source=homepage-module` |
| AI pair cards | `/connect/<a>/<b>` |
| Explore AI services | `/explore/services/ai?source=ai-module` |
| AI Agent | `/ai_agent?source=ai-module` |
| Create | `/create?source=ai-module` redirects to signup with `return_to=/create`. Stop. |
| MCP | `/mcp?source=ai-module` |
| Solution cards | `/solutions/productivity`, `/solutions/smart-home`, `/solutions/customer-communications`, `/solutions/social-media` |
| Explore plans | `/plans?source=homepage-upsell` |
| Story spotlight tabs | Same page. Swaps the story card. |
| Story card | `/explore/<story-slug>` |
| See all stories | `/explore/stories?source=homepage-spotlight` |
| Homepage join CTA | `/join?source=homepage-join-cta`. Signup wall. Stop. |

## Explore (`/explore`, `/explore/applets`, `/explore/services`, `/explore/stories`)

Same shell. Tabs are links: All (`/explore`), Applets (`/explore/applets`), Services (`/explore/services`), Stories (`/explore/stories`).

| Control | Opens |
|---|---|
| Search automations (`#explore-search-input`) | Same lookup pattern as the header search. Not submitted. |
| Example prompt buttons ("If an RSS feed has a new item…", and two siblings) | `/join?return_to=/create&source=explore_prompt_hero`. Signup wall. Stop. |
| Start building | Signup wall (`return_to` create). Stop. |
| Category chips (All, New to IFTTT, Popular, AI, Business tools, Contacts, Developer tools, and further chips behind scroll buttons) | Filter the current tab. AI chip on Services navigates to `/explore/services/ai`. |
| Scroll categories backward / forward | Scrolls the chip row. No page. |
| Applet, service, connection, and story cards | `/applets/…`, `/<service>`, `/connections/…`, `/explore/<story>` |
| Create your own Applet | `/create`. Signup wall. Stop. |
| MCP promo | `/mcp` |

## Service page (example `/hue`, same shell as `/ai_agent` and other `/<service>`)

| Control | Opens |
|---|---|
| Back | `/explore` |
| Copy | Copies the page URL. No navigation. |
| Share (`button[aria-label="share"]`, class `modal-open`) | Dialog: "Share this using the options below" with Copy. Close control `modal-close`. |
| show more / show less | Expands the service description on the same page. |
| Load more Applets | Appends applet cards. No navigation. |
| All (11) / Triggers (0) / Queries (1) / Actions (10) | Filters the ingredient list on the same page. |
| Try it (on applet pages, same card pattern) | `/create?…` signup wall. Stop. |
| Connect / enable an applet | Not a public control on the sampled applet. The public CTAs are Log in, Get started, Get started for free, and Try it, all walls. |

## Applet page (example `/applets/yNvHX9VQ-set-your-android-wallpaper-to-nasa-s-image-of-the-day`)

Public. Back, Copy, Share (same dialog), ingredient filters, View more Applets (`/explore/applets`), related applet cards, Get started for free (`/join`). Stop at Get started and Try it.

## Connection page (example `/connect/google_calendar/slack`)

Public. Same Back / Copy / Share / Load more Applets / ingredient filters as a service page.

## Story page (example `/explore/welcome_to_ifttt`)

Public article. Back, Copy, Share. Body links to other public stories, services, and applets.

## Plans (`/plans`)

| Control | Opens |
|---|---|
| Monthly / Yearly switch (`role=switch`, name "Show yearly prices") | Same page. Yearly is the default (`aria-checked=true` on load, prices show "/ month" with an annual bill line and "SAVE 30%"). Turning it off shows monthly prices (Starter $2.99 / month). |
| About Credits, About AI in Applets, and the other "About …" buttons (`aria-expanded`) | Tooltip, role=tooltip. Credits text: "Credits power everything. Applet runs, MCP usage, and AI features all use credits from your monthly allowance." Escape closes. |
| Get started on Starter / Pro / Pro+ | `/subscriptions/<plan>?interval=year` redirects to `/join?return_to=…&source=subscriptions-checkout`. Signup wall. Stop. |
| Contact us | `/login?return_to=/plans`. Login wall. Stop. |
| FAQ summaries (Which payment methods can I use?, How does renewal work?, Can I switch plans?, What currency are prices in?, Can I use IFTTT for free?) | `<details>` on the same page. The summary click did not set `open` in headless; treat the open state as not yet verified and recapture it during screenshots. |

## MCP (`/mcp`)

Public. Client tabs (role=tab): Claude, Claude Code, ChatGPT, Cursor, Copilot, OpenClaw, Perplexity. Each swaps install steps and a Copy button on the same page. External "Add IFTTT to Claude / Cursor / ChatGPT / Copilot Studio" links leave the site. Not followed.

## Company, legal, help, docs

| Page | What it is | Controls that leave the public tree |
|---|---|---|
| `/about` | Public marketing | Get started is a signup wall |
| `/careers` | Public. "See open positions" goes to `https://careers.smartrecruiters.com/IFTTT` (external). Not followed. | |
| `/contact` | Public community page. Links to Twitter, Facebook (external) and `/help`. | |
| `/help` | "How can we help?" Links to `https://help.ifttt.com` (external Help Center), `/developers`, `/docs/api_reference`. | |
| `/developers` | Public. "Start building" is `/join?return_to=partners_signup`. Stop. "Service API" is `/docs/api_reference`. "Contact us" is `/contact_sales`. | |
| `/partners` | Public. "Start building", "Join for free", and "Join our partner program" are `/join?return_to=partners_signup`. Stop. "See documentation" is `/docs`. | |
| `/docs` | Public getting-started guide. In-page anchors (Overview, Plan, Build, Development, Testing, Submit for review). "My Services" is `/developer_sign_up/new` (not opened; treat as a signup wall until a capture confirms). Nav: Service API, Connect API, Example Services, FAQ. | |
| `/docs/api_reference` | Public reference. "Open the menu" / "Close the menu" toggles the in-page section nav (General API requirements, Service authentication, Triggers, Actions, Queries, and further anchors). Copy buttons copy code samples. | |
| `/docs/connect_api`, `/docs/example_services`, `/docs/faq` | Linked from the docs nav. Same docs shell. Capture as sibling pages. | |
| `/terms` | Trust page. In-page anchors: `#gdpr`, `#data`, `#privacy-policy`, `#eu-residents`, `#terms-of-use`, `#developer-license-agreement`. `/privacy` redirects here (`/terms#privacy-policy`). "export your IFTTT data" and "delete my account" point at `/settings#control-your-data`, which redirects to signup. Stop. Help request form is `https://help.ifttt.com/hc/en-us/requests/new` (external). Not followed. | |
| `/content_map` | Public index of the links above, plus `/explore/stories.rss`. | |
| `/contact_sales` | Public page ("Self-service not for you?") that asks for business details. Form fields are a survey/profile wall. Do not fill. Record the page and stop. | |
| `/billing`, `/settings`, `/create` | Redirect to `/join?return_to=<original>`. Signup wall. Stop. | |
| `/passwords/forgot` | "Forgot your password?" posts to `/passwords/send_reset_token`. Do not submit. Record and stop. | |
| `/login`, `/join` | Email or username and password, or Google, Apple, Facebook. Stop. Do not type, do not click the identity providers. | |
| Unknown path (`/not-a-real-page-xyz`) | Capture the live status during screenshots. If it is a styled error page, keep it. | |

## Solutions

`/solutions/productivity`, `/solutions/smart-home`, `/solutions/customer-communications`, `/solutions/social-media` are public marketing pages. "Try it now" and sibling CTAs that go to `/join` or `/create` are walls. Stop those branches.

## Not in this tree

Signed-in applet builder, my applets, service connections, billing portal, account settings, and onboarding. Each of those redirects to `/login` or `/join`. Dark theme is not present on the public site.
