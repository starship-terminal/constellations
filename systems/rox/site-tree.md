# Rox public site tree

Mapped on 2026-11-21 from the live homepage at `https://www.rox.com/` (which redirects to `https://www.rox.com/`) before any package screenshots. The site is a Framer marketing site plus a public docs shell. `https://www.rox.com/sitemap.xml` lists 781 URLs. Every same-site link below was reached from the homepage chrome, a menu that chrome opens, the footer, or a page that chrome links. Article and docs leaves that share one template are grouped. Nothing was typed into a field. No form was submitted.

## Walls (stop)

| Control | Opens | What happened |
|---|---|---|
| Header and footer "Start now", footer "Login" | `https://run.rox.com/api/auth/login?screen_hint=signup` and `https://run.rox.com/api/auth/signup` | Auth wall. Branch stopped. No email typed, no form submitted. |
| Known wall `https://rox.com/login` | `https://roxai.us.auth0.com/u/login/identifier?...` | Auth0 "Log in to continue to Rox". Visible ask: business email, then Continue, plus Continue with Google and Continue with Microsoft. Password field is in the DOM and was not used. No email typed. No button pressed. |
| Docs header "Login" | same Auth0 / `run.rox.com` login host | Recorded as a wall. Not followed into a session. |
| Platform menu "iOS" | `https://apps.apple.com/bw/app/rox-ai/id6740219278` | External store. Not the web app. |
| Platform menu "MCP" | `https://openai.com/index/codex-for-every-role-tool-workflow/` | External page. Not a Rox control. |
| Company menu "Careers", footer "Careers" | `https://jobs.ashbyhq.com/Rox-Data-Corp` | External job board. |
| Footer "Trust Center" | `https://trust.rox.com/` | Public trust center (loaded, title "Trust Center"). Separate host. |
| Footer "Status" | `https://status.rox.com/posts/dashboard` | Public status page. Separate host. |
| Footer "Subprocessor List" | a published Google Doc | External. |
| Footer security contact | `mailto:` link in the footer | Published contact. The address is not copied into this package. |

`run.rox.com` also exposes `/settings` from some in-app links. That path is behind the same login wall. Not opened.

## Header (desktop 1440)

A 40px announcement bar sits above a 64px nav. The bar is one link. The nav items are links. Hovering Platform, Resources, or Company opens a menu panel. Research, Pricing, and Customers do not open a menu. They navigate.

| Control | Opens |
|---|---|
| Announcement "Rox Raises Series B at 1.3B Valuation" | `/articles/announcing-rox-s-series-b-at-a-1.3b-valuation` |
| Logo | `/` |
| Platform (hover) | Menu, below. The link itself goes to `/platform`. |
| Research | `/research` |
| Pricing | `/pricing` |
| Customers | `/customers` |
| Resources (hover) | Menu, below. The link itself goes to `/resources`. |
| Company (hover) | Menu, below. The link itself goes to `/company`. |
| Contact Sales | `/contact` (sales form). Not submitted. |
| Start now | Auth wall. Stop. |

### Platform menu

Left column categories, middle column capabilities (several labels share `/platform` as their href in the live DOM), right column "Also on".

| Label | Opens |
|---|---|
| Rox Revenue Agent Platform / View platform demo | `/platform` |
| Agentic Workflows | `/platform-categories/agentic-workflows` |
| Sales Engagement | `/platform-categories/sales-engagement` |
| Revenue Action Orchestration | `/platform-categories/revenue-action-orchestration` |
| CRM | `/platform-categories/crm` |
| GTM Data Application | `/platform-categories/gtm-data-applications` |
| Outbound, Dialer, Account Plans, Opportunity Management, People Search, Workflows, Multi-channel Sequences | `/platform` (labels in the menu; dedicated pages also exist under `/featured-agent-capabilities/` and `/platform/`) |
| Custom Apps, CRM Writeback, Native Enrichment, Deep Research & Monitoring, Deal Execution, Artifact Generation, Forecasting | `/platform` in this menu |
| Chat | `/docs/user-guide/chat` |
| Governance | `/docs/admin-guide/governance` |
| Integration | `/docs/admin-guide/integrations` |
| API | `/docs/admin-guide/developer-tools-api-access` |
| MCP | external OpenAI URL (wall of a different product; not followed as a Rox page) |
| WebApp | `/docs/user-guide/getting-started` |
| macOS | `/docs/user-guide/rox-for-mac` |
| iOS | App Store (external) |

### Resources menu

| Label | Opens |
|---|---|
| Resource Hub | `/resources` |
| Demo Library | `/rox-academy` |
| Download for Mac | `/downloads` |
| Blog | `/articles` |
| Docs | `/docs/about-rox/readme` |

### Company menu

| Label | Opens |
|---|---|
| Team | `/company` |
| Careers | Ashby (external) |
| Security | `/security` |

## Phone header (390)

The announcement bar and logo stay. A 33px icon button at the right (`framer-dkldq9`) opens the nav drawer. The drawer lists Platform, Research, Pricing, Customers, Resources, Company, Contact Sales, and Start now. Platform, Resources, and Company are expandable rows in that drawer (their `href` is null until expanded). Start now is the same auth wall.

## Homepage interactions

| Control | Opens |
|---|---|
| Previous / Next (story carousel) | Local carousel. No navigation. |
| "Open story" cards | A customer page, for example `/customers/times-of-india`, `/customers/mongodb`, `/customers/wsp`, `/customers/ramp`, `/customers/together-ai`, `/customers/cloud-software-group`, `/customers/xbow`, `/customers/logicmonitor`, `/customers/pallet`, `/customers/puma-energy`, `/customers/upwind`, `/customers/bynder`, `/customers/axon-911`, `/customers/codat`, `/customers/rev.io`, `/customers/couchbase` |
| Capability chips (Outbound, Automations, Custom Apps, Artifact Generation) | `/featured-agent-capabilities/outbound`, `/featured-agent-capabilities/agent-workflows`, `/featured-agent-capabilities/custom-apps`, `/featured-agent-capabilities/artifact-generation`, and the cross-sell card to `/featured-agent-capabilities/cross-sell-upsell` |
| "Download report" | `/reports/gartner-magic-quadrant` |
| Investor logos | External: General Catalyst, Sequoia, GV. Not followed. |
| Research cards | Mix of `/articles/...` and external `x.com/rox_ai` posts. External not followed. |
| Contact Sales / Start now (repeated in the page) | `/contact` or the auth wall |

No dialog, toast, or theme switch is mounted on the homepage. `color-scheme: dark` does not restyle the page. Body stays `rgb(247, 246, 244)`.

## Footer (every marketing page)

| Group | Controls |
|---|---|
| Explore | Platform `/platform`, Research `/` (href is home in the live footer), Customers `/customers`, Manifesto `/manifesto`, Pricing `/pricing` |
| Resources | Resource Hub `/resources`, Demo Library `/rox-academy`, Download for Mac `/downloads`, Blog `/articles`, Events `/` (href is home), Docs `/docs/about-rox/readme` |
| Company | Team `/company`, Careers (Ashby), Contact `/contact`, Get started `/contact`, Login (auth wall), Talk to sales `/contact`, Security `/security` |
| Trust | Trust Center, Status |
| Legal | `/legal`, extension terms, privacy, terms, vulnerability disclosure, subprocessor list (Google Doc) |
| Social | LinkedIn, X, YouTube. External. |

## Marketing pages linked from chrome

These loaded with HTTP 200 on 2026-11-21. Representative pages are captured. Same-template leaves are listed, not all screenshotted.

| Path | What it is |
|---|---|
| `/` | Home |
| `/platform` | Product |
| `/platform/outbound-agent`, `/platform/agent-workflows`, `/platform/sales-intelligence`, `/platform/sales-engagement`, `/platform/conversation-intelligence`, `/platform/revenue-intelligence`, `/platform/account-intelligence` | Platform leaves (sitemap) |
| `/platform-categories/agentic-workflows`, `sales-engagement`, `revenue-action-orchestration`, `crm`, `gtm-data-applications` | Category pages from the Platform menu |
| `/featured-agent-capabilities/` (15 slugs in the sitemap) | Capability pages |
| `/research`, `/publications`, `/manifesto`, `/careers` | Editorial / company |
| `/pricing` | Three plan cards (Individual, Teams, and a third). No billing toggle. "Start for free" / "Try for free" go to the auth wall. |
| `/customers` and 26 `/customers/<slug>` stories | Story index and stories |
| `/resources`, `/resources/build-vs-buy`, `/resources/stack-consolidation-map`, `/resources/maturity-assessment`, `/resources/assessment`, `/resources/assessment-request` | Resource pages. Assessment request is a form. Not submitted. |
| `/company`, `/teams`, `/security`, `/downloads`, `/rox-academy` | Company, security, Mac download, academy |
| `/contact`, `/contact/success` | Sales form (email, first, last, company, phone, "how did you hear" select, message) and the success URL. Form not filled, not submitted. |
| `/legal` and four policy pages | Legal index and policies |
| `/articles` and 525 article URLs | Blog index and posts. One post captured as the template. |
| `/reports/gartner`, `/reports/gartner-magic-quadrant` | Report landing |
| `/workflow`, `/startups/`, `/startups/gc/`, `/partners/rox-leadiq`, `/rox-for-leadiq`, `/rox-for-cios`, `/rox-for-microsoft-copilot` | Campaign landings in the sitemap |
| `/50-cios-redefining-ai-leadership-in-2026`, `/50-cros`, `/cio-summit-of-san-francisco`, `/cro-summit-of-new-york`, `/flagship-events/ainative` | Event landings |
| `/llms.txt` | Plain text, not a page |

## Docs

`/docs/about-rox/readme` is the docs home. The shell has a left nav (About Rox, Architecture, User Guide, Admin Guide, Security, Release Notes), a search field, and Login.

| Control | Opens |
|---|---|
| Search, or Control+K / Command+K | A dialog: "Type at least two letters to search all docs pages." Not submitted. Escape closes it. |
| Login | Auth wall. Stop. |
| Nav sections | 162 docs URLs: admin-guide 56, user-guide 83, blogs 11, architecture 5, about-rox 4, security 2, release-notes 1 |

Docs pages that describe login with Google or email are public documentation. They are not the login wall, and they were not used to sign in.

## What is not on the public site

The signed-in product (agent workspace, sequences, dialer, settings) lives on `run.rox.com` behind Auth0. Those screens are not in this tree. No dark theme toggle exists on the marketing site.
