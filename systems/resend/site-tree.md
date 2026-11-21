# Resend public site tree

Mapped on 2026-11-21 from the live public site, then refreshed the same day. Official
domain confirmed as `https://resend.com/` (title "Resend · Email for
developers", h1 "Email for developers"). Headless Playwright, signed out.
Nothing was typed, submitted, or clicked on Google or GitHub.

Default theme on the marketing site is dark (`html` class includes `dark`,
`color-scheme: dark`). Docs has an explicit theme switch (system, light,
dark). There is no marketing-site theme toggle.

Auth walls, recorded and not entered:

| Control | Opens | Action |
|---|---|---|
| Header "Get started", footer "Get started", pricing plan "Get started" | `https://resend.com/signup` | Photographed empty on 2026-11-21. Did not type. Did not click Google or GitHub. Did not submit. |
| Header "Log in" | `https://resend.com/login` | Photographed empty. Page shows email, "Log in with Google", "Log in with GitHub", and "Log In". Did not type. Did not click Google or GitHub. Did not submit. |
| `https://resend.com/get-started` | redirects to `https://resend.com/signup` | Stopped. |
| `https://resend.com/settings/usage` (linked from a public page) | redirects to `https://resend.com/login` | Stopped. |

## Shell

Desktop header (sticky, 1440): logo to `/home`, then hover menus, then
Pricing (`/pricing`, a link, not a menu), then Log in (`/login`, auth wall)
and Get started (`/signup`, auth wall).

Phone header (390): logo to `/home`, and a button labelled "Open main menu"
(`aria-label="menu"`). That button opens a full-screen sheet. The sheet
lists Get started (`/signup`, auth wall), Log in (`/login`, auth wall),
the same six section buttons as desktop, Pricing (`/pricing`), a Forward
promo (`/forward`), Get started again, and Documentation (`/docs`).

A persistent banner link, "What you missed at Resend Forward", goes to
`/forward`. It stays visible under the hover menus.

Footer columns (same on the mapped marketing pages): Product, Company,
Resources, legal. External links (not followed as pages of this product):
GitHub (`https://github.com/resend`), LinkedIn, X, YouTube, and
`https://react.email/docs` ("Check the docs" on the home code sample).

## Desktop hover menus

Each menu opens on pointer hover over the header button. Click did not
open them. Escape and moving the pointer away closes them. No dialog.

### Features button

| Item | Opens |
|---|---|
| Email API | `/features/email-api` |
| SMTP | `/features/smtp-service` |
| Inbound | `/features/inbound` |
| Audiences | `/features/audiences` |
| Broadcasts | `/features/broadcasts` |
| Automations | `/features/automations` |
| Templates | `/features/templates` |
| CLI | `/features/cli` |
| Webhooks | `/features/webhooks` |
| Dedicated IPs | `/features/dedicated-ips` |
| Inbox | `/products/inboxes` |
| Transactional emails | `/products/transactional-emails` |
| Marketing emails | `/products/marketing-emails` |

### Company button

| Item | Opens |
|---|---|
| About | `/about` |
| Blog | `/blog` |
| Careers | `/careers` |
| Customers | `/customers` |
| Humans | `/humans` |
| Handbook, "How we work" | `/handbook` |
| Philosophy, "What we value" | `/philosophy` |

### Enterprise button

| Item | Opens |
|---|---|
| Talk to sales | `/enterprise` |
| Customers | `/customers` |
| Security | `/security` |
| SOC 2 | `/security/soc-2` |
| GDPR | `/security/gdpr` |
| Your next billion emails | `/enterprise` |

### Help button

| Item | Opens |
|---|---|
| Support | `/support` |
| Status | `/status` (redirects to `https://resend-status.com/`) |
| Migrate | `/migrate` |
| Knowledge base | `/docs/knowledge-base/introduction` |

### Docs button

| Item | Opens |
|---|---|
| Getting started | `/docs/introduction` |
| API reference | `/docs/api-reference` |
| Integrations | `/docs/integrations` |
| Changelog | `/changelog` |
| SDKs | `/docs/sdks` |
| Language marks (no visible label in the hover panel) | `/nodejs`, `/nextjs`, `/nuxt`, `/remix`, `/python`, `/ruby`, `/php`, `/laravel`, `/supabase`, `/convex`, `/go`, `/java`, `/elixir`, `/rust`, `/aws-lambda`, `/fastapi` |

### AI button

| Item | Opens |
|---|---|
| Cursor | `/cursor` |
| Claude | `/claude` |
| Claude Code | `/claude-code` |
| Codex | `/codex` |
| GitHub Copilot | `/github-copilot` |
| Gemini | `/gemini` |
| v0 | `/v0` |
| Bolt | `/bolt` |
| Lovable | `/lovable` |
| Replit | `/replit` |
| Agents | `/agents` |
| MCP | `/mcp` |
| Skills | `/agent-skills` |

## Home page interactions (not navigation)

The home page is a long marketing page. These controls stay on the page.
None of them submit a form. The home page has no `<form>`.

| Control | What it does |
|---|---|
| Language tabs: Node.js, Serverless, Ruby, Python, PHP, CLI, Go, Rust, Java, Elixir, .NET, REST, SMTP | Swap the hero code sample. Local tab state. |
| Framework tabs under the sample: Node.js, Next.js, Remix, Nuxt, Express, Hono, Redwood, Bun, Astro | Swap the framework example. Local tab state. |
| "Copy to clipboard" | Copies the visible sample. No navigation. |
| "Select test mode" listbox | Opens a listbox of demo delivery states. Public demo, not a signed-in inbox. |
| "Send test email" | Public demo control on the animated dashboard. Not submitted as a real send. |
| Template names (`user-welcome.tsx`, `reset-password.tsx`, `user-invite.tsx`, `weekly-digest.tsx`) | Swap the template preview. Local state. |
| Deliverability glossary buttons (DNSBLs, Spamhaus, BIMI, VMC, CAN-SPAM Act, DKIM, SPF, DMARC) | Open a definition popover on the page. |
| Feature cards (Intuitive analytics, Full visibility, Domain authentication) | In-page sections, not separate routes. |

## Pricing

`/pricing` has two tabs: "Transactional emails" (default) and "Marketing
emails". Plan cards link "Get started" to `/signup` (auth wall, not
followed) and "Contact us" to `/enterprise`. A link "Are you an AI agent?
See pricing" opens `/pricing.md` (plain markdown, no chrome).

## Docs

`/docs/introduction` is the docs shell. Sidebar:

- Search button ("Search... ⌘K") opens a search dialog. Public. Not a form submit.
- "Toggle assistant panel" opens an assistant panel. Not submitted.
- Get started: Introduction, Create API key, Add domain, Email types, AI onboarding.
- Sending examples (collapsed button).
- Learn (collapsed groups): Domains, Sending, Receiving, plus Inboxes (`/docs/dashboard/inboxes/introduction`).
- Collapsed groups: Broadcasts, Contacts, Automations, Templates, Logs, Webhooks (`/docs/webhooks/introduction` is also linked from the home page).
- Resources: Resend Forge (`/docs/forge`), SDKs, CLI, MCP Server, Integrations, Examples.
- Theme buttons: "Switch to system theme", "Switch to light theme", "Switch to dark theme".

The docs sitemap lists 425 URLs. Representative pages are captured. The
full docs tree is not a separate screenshot per article.

## Footer and company pages reached from the home page

| Link | Page |
|---|---|
| Changelog | `/changelog` |
| Brand | `/brand` |
| Clubs | `/clubs` |
| Events | `/events` |
| Insiders | `/insiders` |
| Open source | `/open-source` |
| Wallpapers | `/wallpapers` |
| Legal policies | `/legal` |
| Security, SOC 2, GDPR | `/security`, `/security/soc-2`, `/security/gdpr` |
| Support | `/support` |
| Migrate | `/migrate` |
| Customers | `/customers` |
| Humans | `/humans` |
| Philosophy | `/philosophy` |
| About | `/about` |
| Blog | `/blog` |
| Careers | `/careers` |
| Forward | `/forward` and `/forward/agenda` |
| Status | `https://resend-status.com/` |

## Sitemap families not opened one by one

`sitemap.xml` is an index of 12 child sitemaps, 1065 unique URLs. Families
beyond the nav tree: `/blog` (187), `/changelog` (116), `/docs` (425),
`/handbook` (66), `/humans` (64), `/customers` (48), `/other` (132),
`/guides` (12), `/clubs` (7), `/legal` (8), `/launch-weeks` (7), plus
single partner and SDK landing pages (`/nodejs`, `/nextjs`, `/cursor`,
and the rest of the Docs and AI menus). Index pages of those families
are in the capture. Individual posts, humans, customers, handbook
chapters, and changelog entries are the same templates. They are not
each a separate state.

## Stopped branches

- Signup, login, Google, GitHub, get-started, settings/usage: auth walls, above.
- No newsletter field was filled. No contact form was submitted. The
  enterprise page is a public sales page; its form, if present, is
  photographed and not submitted.
