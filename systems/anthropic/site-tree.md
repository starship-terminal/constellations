# Anthropic public site tree

Mapped from https://www.anthropic.com/ on 2026-11-21, signed out, before any new package screenshot. The page is a live product site (title "Home \\ Anthropic"), not a parked domain or a captcha wall. Desktop width is 1440. Phone width is 390. This package stays on anthropic.com. claude.ai, platform.claude.com, and claude.com are named where a control points at them, and those branches stop. Nothing was typed. No form was submitted. No identity provider was clicked.

The header is a pill. Left of the wordmark: News (a link), then Research, Policy, and Commitments (buttons, `aria-haspopup="menu"`). Right of the wordmark: Company and Try Claude (the same kind of button), Search (a link to `/search`), and, at 390, Open menu (`aria-haspopup="dialog"`). A click on a header menu button sets `aria-expanded="true"` and shows one `[role=menu]`. Escape closes it. The menus do not navigate by themselves.

## Header menus (desktop)

| Control | Opens |
|---|---|
| News | https://www.anthropic.com/news |
| Wordmark | https://www.anthropic.com/ |
| Search | https://www.anthropic.com/search |
| Research | Menu: Overview, Alignment, Interpretability, Engineering, Science, The Anthropic Institute, Economics, Frontier Red Team, Societal Impacts |
| Policy | Menu: Overview, Policy on the AI Exponential |
| Commitments | Menu: Claude's Constitution, Beneficial Deployments, Responsible Scaling Policy, Frontier Safety Roadmap, Transparency, Threat Intelligence |
| Company | Menu: About us, Leadership, Public benefit report, Customers, Careers, Events, Claude Corps, Economic Futures |
| Try Claude | Menu: Claude AI, Console. Both leave anthropic.com. **Wall. Stop.** |

### Research menu

| Item | Opens |
|---|---|
| Overview | https://www.anthropic.com/research |
| Alignment | https://www.anthropic.com/research/team/alignment |
| Interpretability | https://www.anthropic.com/research/team/interpretability |
| Engineering | https://www.anthropic.com/engineering |
| Science | https://www.anthropic.com/science |
| The Anthropic Institute | https://www.anthropic.com/institute |
| Economics | https://www.anthropic.com/research/team/economics |
| Frontier Red Team | https://www.anthropic.com/research/team/frontier-red-team |
| Societal Impacts | https://www.anthropic.com/research/team/societal-impacts |

### Policy menu

| Item | Opens |
|---|---|
| Overview | https://www.anthropic.com/policy |
| Policy on the AI Exponential | https://www.anthropic.com/policy-on-the-ai-exponential |

### Commitments menu

| Item | Opens |
|---|---|
| Claude's Constitution | https://www.anthropic.com/constitution |
| Beneficial Deployments | https://www.anthropic.com/beneficial-deployments |
| Responsible Scaling Policy | https://www.anthropic.com/responsible-scaling-policy |
| Frontier Safety Roadmap | https://www.anthropic.com/responsible-scaling-policy/roadmap |
| Transparency | https://www.anthropic.com/transparency |
| Threat Intelligence | https://www.anthropic.com/threat-intelligence |

### Company menu

| Item | Opens |
|---|---|
The open menu also shows three column labels that are not links: Who we are, Join us, Programs. The footer Company list measured earlier omitted Who we are. The screenshot is the source for the items below.

| Item | Opens |
|---|---|
| About us | https://www.anthropic.com/company |
| Leadership | https://www.anthropic.com/company/leadership |
| Public benefit report | https://www.anthropic.com/public-benefit-report |
| Customers | https://claude.com/customers (off this host; not captured as Anthropic) |
| Careers | https://www.anthropic.com/careers |
| Events | https://www.anthropic.com/events |
| Claude Corps | https://www.anthropic.com/claude-corps |
| Economic Futures | https://www.anthropic.com/economic-futures |

### Try Claude menu (stop)

| Item | Opens |
|---|---|
| Claude AI | https://claude.ai/ **Wall. Stop.** Not captured. |
| Console | https://platform.claude.com/login **Wall. Stop.** Not captured. |

No Google, Apple, or other identity provider is on the anthropic.com homepage. Those buttons, if any, sit on the hosts above and were not opened.

## Phone menu

Control: header button "Open menu" (`aria-haspopup="dialog"`). Hidden as a primary control at 1440. At 390, a click opens a dialog titled by the same control. Close is the "Close menu" button inside the dialog.

The dialog lists Home, News, and the same Research, Policy, Commitments, and Company buttons as the desktop menus. Below those, a horizontal strip of recent articles with Previous article and Next article. Then Products, Models, Solutions, Help and security, and Terms and policies (the footer groups, collapsed). Then Try Claude, Contact Sales, and Download app.

| Control in the dialog | Opens |
|---|---|
| Home | https://www.anthropic.com/ |
| News | https://www.anthropic.com/news |
| Research, Policy, Commitments, Company | The same menus as desktop, inside the sheet |
| Try Claude | The same two off-host links. **Wall. Stop.** |
| Contact Sales | https://claude.com/contact-sales (off this host) |
| Download app | https://claude.com/download (off this host) |
| Article cards | Individual news and research URLs on anthropic.com |

## Homepage body

The hero is a film. Play film and Pause motion toggle that film. They do not open a page.

Announcement cards link to a topic chip, a model page, a system card, and the announcement itself. A "Related to …" button sits on each card. It expands related links on the page. It does not navigate.

| Control | Opens |
|---|---|
| Announcements chip | https://www.anthropic.com/news/announcements |
| Introducing Fable 5.2 and Mythos 5.2 | https://www.anthropic.com/claude-fable-and-mythos-5-2 |
| Fable / Mythos / Opus / Sonnet chips | https://www.anthropic.com/claude/fable, /claude/mythos, /claude/opus, /claude/sonnet |
| System card "View" | /claude-fable-5-2-mythos-5-2-system-card, /document/claude-opus-5-5-system-card, /document/claude-sonnet-5-5-system-card |
| Institute topic | https://www.anthropic.com/search?topic=institute |
| The Anthropic Institute card | https://www.anthropic.com/institute |
| Alignment chip and Constitution card | /research/team/alignment and /constitution |
| Responsible Scaling Policy chip and card | /search?topic=responsible-scaling-policy and /responsible-scaling-policy |
| Policy chip and "Core views on AI safety" | /news/policy and /news/core-views-on-ai-safety |
| Previous slide / Next slide | Moves the lower carousel. No new URL. |

## Footer

Column titles are buttons. On desktop the columns are already listed. On phone they expand. Privacy choices is a button in the footer. It was not opened. Opening it is a consent choice.

| Column | Opens |
|---|---|
| Research | The same nine Research destinations as the header menu |
| Policy | The same two Policy destinations |
| Commitments | The same six Commitments destinations |
| Company | The same eight Company destinations, including the claude.com Customers link |
| Products | claude.com product, pricing, and platform pages. Off this host. Not captured as Anthropic. |
| Models | /claude/mythos, /claude/fable, /claude/opus, /claude/sonnet, /claude/haiku |
| Solutions | claude.com/solutions and one platform.claude.com agents page. Off this host. |
| Help and security | /legal/supported-regions stays on anthropic.com. The rest are claude.com, status.claude.com, support.claude.com, and trust.anthropic.com. |
| Terms and policies | /legal, /legal/privacy, /responsible-disclosure-policy, /legal/commercial-terms, /legal/consumer-terms, /legal/k12-terms, /legal/consumer-health-data-privacy-policy, /legal/aup |
| Log in | Claude.ai (https://claude.ai/) and Claude console (https://platform.claude.com/). **Wall. Stop.** |
| Privacy choices | Consent dialog. Not opened. Not submitted. |
| Social icons | YouTube, X, LinkedIn. Off-site. Not captured. |

Our mission is footer copy. It has no link.

## What this capture photographs

Public anthropic.com pages and the menus that open on this host: home, news, research, engineering, policy, constitution, company, careers, search, one model page, the phone menu, and one header menu. Claude product, pricing, docs, console, and claude.ai stay out of this refresh. They are a different product surface, and the login branches stop.
