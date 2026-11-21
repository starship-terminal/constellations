# Sentry public site tree

Mapped on 2026-11-21 from the live public site before screenshots.
Official domain confirmed as `https://sentry.io/` (title "Application
Performance Monitoring & Error Tracking Software | Sentry", h1 "Code
breaks, fix it faster"). `https://sentry.io/` redirects to
`https://sentry.io/welcome/`. Headless Chromium, signed out, after T3
preview screenshots failed twice. Nothing was typed into a field.
Nothing was submitted. Google, GitHub and Azure were not clicked.

The marketing site paints dark (`html` class `dark`, page background
`rgb(31, 22, 51)`). `prefers-color-scheme: light` does not flip the
marketing page. There is no marketing theme toggle. A "Marketing Mode"
switch on the homepage stays on and was not switched. Docs at
`https://docs.sentry.io/` follows the browser color scheme: dark under
`prefers-color-scheme: dark`, light under light. A "Toggle theme"
button is in the docs header. Opening it did not reveal a labelled
light or dark menu item in this pass, so the docs theme was recorded
from the color-scheme emulation and then left.

Auth walls, recorded and not entered:

| Control | Opens | Action |
|---|---|---|
| Header "Sign in", footer has no separate sign-in, phone drawer "Sign in" | `https://sentry.io/auth/login/` | Stopped. Empty email and password. Did not click Google, GitHub, Azure, Organization SSO, or Forgot password. Did not submit. |
| Header "Get started", hero "Get started", product "Try Sentry for free", pricing "Start trial" | `https://sentry.io/signup/` | Stopped. Empty name, organization, email and password. Did not open the location select. Did not click Google, GitHub or Azure DevOps. Did not submit Get set up. |
| Header "Get demo", pricing Enterprise "Contact sales" (`/demo`) | `https://sentry.io/demo/` | Photographed the empty request form. Did not type a name, email, company or note. Did not submit. |
| Promo code "Redeem" on signup | stays on the signup page | Not clicked. |

## Shell

Desktop header (sticky, 1440): logo to `/welcome/`, then three buttons
that open dropdowns, then links.

| Control | Kind | Opens |
|---|---|---|
| Logo, "Welcome Page" | link | `/welcome/` |
| Platform | button, `aria-controls="dropdown-platform"` | dropdown, not a page |
| Solutions | button, `aria-controls="dropdown-solutions"` | dropdown, not a page |
| Resources | button, `aria-controls="dropdown-resources"` | dropdown, not a page |
| Docs | link | `https://docs.sentry.io/` |
| Pricing | link | `/pricing/` |
| Sign in | link | `/auth/login/` (auth wall) |
| Get demo | link | `/demo/` (request form, not submitted) |
| Get started | link | `/signup/` (auth wall) |

Hover opens a dropdown. Click also opens it if hover did not. Escape
and moving the pointer away closes it. No dialog.

Phone header (390): logo to `/welcome/`, and a button labelled "Menu"
(`aria-controls="mobileMenu"`). That button opens a full-height sheet
over the hero. The sheet lists Platform, Solutions and Resources as
buttons with chevrons, then Docs, Pricing, Sign in, Get demo and Get
started. Platform inside the sheet expands the same product links as
the desktop dropdown. Sign in, Get demo and Get started are the same
walls as desktop.

A promo pill, "Sentry MCP: fix production issues right from your LLM",
links to `https://mcp.sentry.dev`. It is not an auth wall.

## Desktop dropdowns

### Platform button

Three columns: Products, AI Debugging, Integrations.

| Item | Opens |
|---|---|
| Error Monitoring | `/product/error-monitoring/` |
| Logs | `/product/logs/` |
| Session Replay | `/product/session-replay/` |
| Metrics | `/product/metrics/` |
| Tracing | `/product/tracing/` |
| Agent Tracing | `/product/tracing/ai-agent/` |
| Profiling | `/product/profiling/` |
| Size Analysis | `/product/size-analysis/` |
| Cron Monitoring | `/product/cron-monitoring/` |
| Uptime Monitoring | `/product/uptime-monitoring/` |
| Labs | `https://labs.sentry.dev/` (external) |
| Seer | `/product/seer/` |
| Agent | `/product/seer/agent/` |
| Autofix | `/product/seer/autofix/` |
| Github | `/integrations/github/` |
| Slack | `/integrations/slack/` |
| Sentry CLI | `https://cli.sentry.dev/` (external) |
| Sentry MCP | `https://mcp.sentry.dev/` (external) |
| All Integrations | `/integrations/` |

### Solutions button

| Item | Opens |
|---|---|
| Web / Full Stack Development | `/for/full-stack/` |
| Mobile Crash Reporting | `/solutions/mobile-developers/` |
| Game Crash Reporting | `/solutions/game-developers/` |
| AI Observability | `/solutions/ai-observability/` |
| Application Performance Monitoring | `/solutions/application-performance-monitoring/` |
| Application Observability | `/solutions/application-observability/` |
| Real User Monitoring | `/solutions/real-user-monitoring-rum/` |
| Ecommerce | `/solutions/ecommerce/` |
| OpenTelemetry | `/solutions/opentelemetry/` |
| Enterprise | `/for/enterprise/` |
| Startups | `/for/startups/` |
| All SDKs | `/platforms/` |

### Resources button

Groups: Learn, Support, Hang out with us, plus a card "Automated
Debugging Hub" that links to `/resources/automated-debugging/`.

| Item | Opens |
|---|---|
| Blog | `https://blog.sentry.io/` (external) |
| Changelog | `/changelog/` |
| Sandbox | `https://sandbox.sentry.io/` (public demo host, not entered as an org) |
| Resources | `/resources/` |
| Syntax | `https://syntax.fm/` (external) |
| Customers | `/customers/` |
| Cookbook | `/cookbook/` |
| Contact us | `/contact/enterprise/` (sales form, not submitted) |
| Help Center | `https://help.sentry.io/` (external) |
| Status | `https://status.sentry.io/` (external) |
| Community | `/community/` |
| Events | `/events/` |
| Merch | `https://sentry.shop/` (external shop, not entered) |

## Home page interactions (not navigation)

The home page is a long marketing page. Embedded Errors, Replays, Logs,
Traces and Seer panels are illustrations, not a signed-in org. The home
page has no form to submit.

| Control | What it does |
|---|---|
| Marketing Mode switch | Sits on the right of the hero. Left on. Not switched. |
| Hero "Get started" | Same signup wall as the header. |
| Hero "Get demo" | Same demo request form as the header. |
| Promo pill | Leaves the site for `https://mcp.sentry.dev`. |

## Pricing

`/pricing/` is public. Heading: "Pricing plans for dev teams of all
sizes". A switch labelled "Toggle billing frequency, currently Annual"
flips Monthly and Annual. Plan cards: Developer (Free), Team, Business,
Enterprise. "Start trial" links go to `/signup/` with a plan query
(auth wall, not followed as a submit). Enterprise "Contact sales" goes
to `/demo`. Quota rows (Errors, Logs, Replays, Spans, and the rest) are
on-page controls, not separate routes.

## Docs

`https://docs.sentry.io/` is public. Landing heading: "Get started with
Sentry". Header links: Get Started, SDKs, Product, AI, Concepts,
API, Manage, Search Docs, Ask AI, Go to Sentry. "Go to Sentry" returns
to the marketing site, not a signed-in org. Search Docs and Ask AI
were not submitted. The page has a theme toggle. This pass did not
walk the full docs tree.

## Footer

Footer columns on the marketing pages: company (About, Blog, Careers,
Contact us, Trust), products, solutions, and resources (Docs, Help
Center, Status, Cookbook, Dev resources, Terms, Security and
compliance, Privacy). Social links leave the site: X, GitHub, LinkedIn,
Discord. External links were not captured as pages of this product.

## Pages photographed

Desktop 1440 CSS px, phone 390 CSS px. Marketing shots are dark
because the site paints dark. Login is light because that wall paints
light. Docs was shot in both color schemes.

| Page | File |
|---|---|
| Home | `screenshots/public-2026-11-21/home-dark-desktop.png` |
| Home, full page | `screenshots/public-2026-11-21/home-dark-desktop-full.png` |
| Home, phone | `screenshots/public-2026-11-21/home-dark-mobile.png` |
| Platform menu | `screenshots/public-2026-11-21/home-dark-platform-menu.png` |
| Solutions menu | `screenshots/public-2026-11-21/home-dark-solutions-menu.png` |
| Resources menu | `screenshots/public-2026-11-21/home-dark-resources-menu.png` |
| Phone menu | `screenshots/public-2026-11-21/home-dark-mobile-menu.png` |
| Phone Platform expansion | `screenshots/public-2026-11-21/home-dark-mobile-platform.png` |
| Pricing | `screenshots/public-2026-11-21/pricing-dark-desktop.png` |
| Pricing, phone | `screenshots/public-2026-11-21/pricing-dark-mobile.png` |
| Error Monitoring | `screenshots/public-2026-11-21/product-error-dark-desktop.png` |
| Tracing | `screenshots/public-2026-11-21/product-tracing-dark-desktop.png` |
| Integrations | `screenshots/public-2026-11-21/integrations-dark-desktop.png` |
| Customers | `screenshots/public-2026-11-21/customers-dark-desktop.png` |
| About | `screenshots/public-2026-11-21/about-dark-desktop.png` |
| Changelog | `screenshots/public-2026-11-21/changelog-dark-desktop.png` |
| Platforms | `screenshots/public-2026-11-21/platforms-dark-desktop.png` |
| Docs, dark | `screenshots/public-2026-11-21/docs-dark-desktop.png` |
| Docs, light | `screenshots/public-2026-11-21/docs-light-desktop.png` |
| Login wall, empty | `screenshots/public-2026-11-21/login-light-desktop.png` |
| Login wall, phone, empty | `screenshots/public-2026-11-21/login-light-mobile.png` |
| Signup wall, empty | `screenshots/public-2026-11-21/signup-light-desktop.png` |
| Signup wall, phone, empty | `screenshots/public-2026-11-21/signup-light-mobile.png` |
| Demo request, empty | `screenshots/public-2026-11-21/demo-dark-desktop.png` |
