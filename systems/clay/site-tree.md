# Clay public site tree

Mapped on 2026-11-22 from the live public site, signed out. Official domain confirmed as `https://www.clay.com/` (wordmark "clay", hero "Build systems to grow revenue"). `https://clay.com` 301s there. This is the GTM data platform, not the personal CRM at clay.earth (that product 301s to me.sh and already lives in [systems/clay-earth](../clay-earth)). clay.global and clay.so are different products and were not captured.

Nothing was typed. No identity provider was clicked. No form was submitted. No captcha was solved. `login-extracted` stays `not-started`.

The marketing site is Webflow plus a custom nav (`clay-webflow-dev.vercel.app/nav.css`). It paints one light theme. `color-scheme` on the root was `normal`. There is no theme control. Login and signup are a separate app at `app.clay.com`.

## Auth walls

Photographed empty. Stopped there.

| Control | Opens | Action |
|---|---|---|
| Header "Log in" | `https://app.clay.com/` | Empty email field. "Welcome back!" Sign in with Google. Continue. Not typed. Google not clicked. Continue not clicked. |
| Header "Start free trial", hero "Start free trial", phone drawer "Start free trial" | `https://app.clay.com/signup` | "Welcome to Clay!" Empty full-name and email fields. Sign up with Google. Continue. Not typed. Google not clicked. Continue not clicked. The nav link carries a `su` query. The committed URL is the path only. |
| Signup "Log in" | The login wall | Not followed from the signup card. |
| Login "Sign up" | The signup wall | Not followed from the login card. |
| "Get a demo" | `https://www.clay.com/demo` | Not opened. A demo request form. Not typed. Not submitted. |
| Contact "What do you need help with?" | A select on `/contact` | Not opened. Not submitted. The page tells you to log in or email support. The email was not opened. |

## Homepage header (`https://www.clay.com/`)

Desktop, left to right: logo to `/`, Product (hover menu), Solutions (hover menu), Resources (hover menu), Company (hover menu), Pricing (`/pricing`). Right side: command-K search, Log in, Get a demo, Start free trial. The bar is a white pill.

| Control | Opens |
|---|---|
| Product | A white panel. Data infrastructure: Audiences (`/audiences`), Data marketplace (`/integrations`), Signals and intent (`/signals`), Waterfall enrichment (`/waterfall-enrichment`). Agents: Clay's global agent (`/agent`), Account agents (`/account-agents`), Claygents (`/claygent`), Inbound SDR agent (`/inbound-sdr`). Orchestration: Workflows (`/workflows`), CLI/API (`/agent-plugin`), Functions (`/functions`). Activation: Ads (`/ads`), Sequencer (`/sequencer`), MCP for reps (`/mcp`). A feature card links to `/agent`. |
| Solutions | A white panel. Data foundations: CRM enrichment, TAM sourcing, Territory planning, Reverse ETL (all under `/use-cases/`). Pipeline generation: Outbound, Automated inbound, PLG assist, ABM. Rep productivity: Rep prospecting, Account research, Rep assist. Department: GTM Ops (`/clay-for-gtm-ops`), Marketing, Sales, Enterprise (`/enterprise`), Startup (`/clay-for-startups`). |
| Resources | A white panel. Case studies (`/customers`). Learn: University (`https://university.clay.com/`), Skills library (`https://marketplace.clay.com/`), Livestreams (`/livestreams`), GTM guides (`/guides`), Cohort live classes (`https://university.clay.com/cohorts`). Connect: Clay community (`https://community.clay.com/`), Slack (`/slack-community`), Live events (luma.com), Startup program, Campus ambassadors, Find Clay experts (`/experts`), GTM Engineer job board (`/job-board`), partner links, Private Equity. A dated livestream card. University, marketplace, community, and Luma were not captured as product pages. |
| Company | A white panel. About (`/about`), Careers (`/careers`), Open roles (`/jobs`), Blog (`/blog`), Contact (`/contact`), Press (`/press`). Social: LinkedIn, YouTube, X. Not opened. A New York Times card. Not followed. |
| Pricing | `https://www.clay.com/pricing` |
| Command-K | A search dialog over a blurred page. Empty field, placeholder "Search for anything...". Search and Ask AI tabs. Ask AI row, "Start conversation". Nothing typed. Ask AI was not started. Escape closes it. On a 390 width the same control opens a full-screen empty search ("All (0)"). |
| Log in | Login wall. |
| Get a demo | Demo page. Not opened. |
| Start free trial | Signup wall. |

Phone (390): logo, Get a demo, and a menu toggle (`.nav__menu--toggle`). The open drawer lists Product, Solutions, Resources, Company, Pricing, then Log in and Start free trial. The drawer was photographed. No row was followed.

## Footer

On the homepage, after the page. Columns from the live footer links:

- Trial and demo: Start free trial, Get a demo.
- Use cases: Automated inbound, Account research, ABM, PLG assist, Rep assist, Reverse ETL, Outbound, CRM Enrichment, TAM Sourcing.
- Product: Claygent AI, Account Agents, Ads, Sequencer, Multi-provider data enrichment, Audiences, Signals, Workflows, Functions, Integrations, Pricing, Changelog.
- Learn: three blog posts, Series C, a University lesson, University, Use case templates, Partner programs, Community, FAQ.
- Company: Contact us, About, Careers, Jobs, Integrate with Clay, Status (`https://status.clay.com/`).
- Customers: OpenAI, Vanta, Verkada, Sendoso, Anthropic, Coverflex, Rippling, Case studies.
- Legal: Privacy policy (`https://privacy.clay.com/`), Terms of service (`/legal/terms-of-service`), Make a privacy request (`https://app.clay.com/privacy/request`). The privacy request was not opened.
- Social: LinkedIn, YouTube, X, Slack. Not opened.
- Credit: Hudson. Not followed.

Status, University, Community, privacy.clay.com, and the social hosts are other hosts. They were not captured as product pages.

## Pages opened

| Page | What it is |
|---|---|
| `https://www.clay.com/` | Marketing home. Claymation hero. Green band. White and chartreuse CTAs. |
| `https://www.clay.com/pricing` | Free, Launch, Growth, Enterprise. Monthly and Annual (save 10%). Annual is the painted default in the first viewport. Monthly was not switched. Checkout was not entered. |
| `https://www.clay.com/integrations` | Data marketplace index. |
| `https://www.clay.com/customers` | Customer stories. |
| `https://www.clay.com/about` | About. |
| `https://www.clay.com/faq` | FAQ. |
| `https://www.clay.com/blog` | Blog index. |
| `https://www.clay.com/changelog` | Changelog. |
| `https://www.clay.com/enterprise` | Enterprise product page. |
| `https://www.clay.com/contact` | Contact. A select, not submitted. |
| `https://www.clay.com/legal/terms-of-service` | Terms. |
| `https://www.clay.com/this-page-does-not-exist-capture-2026` | 404. "Uh-oh! We dropped this one on the wheel." Go back home and Customer stories. |
| `https://app.clay.com/` | Login wall. Empty. |
| `https://app.clay.com/signup` | Signup wall. Empty. |

Blog and changelog pages are very long (about 45,000 and 52,000 CSS px). The package keeps the first viewport of each, not the full sheet.
