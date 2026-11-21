# Craft public site tree

Mapped on 2026-11-22 from the live public site, signed out. Official domain confirmed as `https://www.craft.do/` (wordmark CRAFT, hero "Your space for notes, tasks, and big ideas"). `https://craft.do` redirects there. This is the Craft Docs marketing site. `systems/craftwork` is a different product and was not edited. `systems/craft-docs` was not created, because origin/main already maps craft.do to `systems/craft`.

Nothing was typed. No identity provider was clicked. No form was submitted. No captcha was solved. `login-extracted` stays `not-started`.

The marketing site is Next.js with a Tailwind v4 semantic layer. It paints one light theme. `prefers-color-scheme: dark` left the body at `rgb(252, 249, 247)`. There is no theme control. Login and signup are the same wall at `https://docs.craft.do/`.

## Auth walls

Photographed empty. Stopped there.

| Control | Opens | Action |
|---|---|---|
| Header "Log in" | `https://docs.craft.do/` | The live link adds a `ref` and a PostHog distinct id. Those query parameters were stripped. Empty email field. "Welcome to Craft". continue with SSO, Continue, Continue with Google, Continue with Apple, Continue with Microsoft. Not typed. Providers not clicked. Continue not clicked. |
| Phone drawer "Log in" | The same wall | Photographed at 390. Same empty fields. |
| "continue with SSO" | A further step on the same host | Not pressed. |
| Continue, Google, Apple, Microsoft | Identity or email continuation | Not clicked. reCAPTCHA notice visible. Not solved. |
| Hero and header "Try Craft Free" | `/download` | Photographed. No installer was started. App Store, Play Store, and Microsoft store buttons were not followed. |
| Download page "Open" (Web) | The docs host | Not followed from that button. The empty wall was opened directly. |
| "Upgrade to Plus" and checkout links | The docs host with a checkout query | Not followed. |

There is no separate signup page. The empty wall is both login and signup.

## Homepage header (`https://www.craft.do/`)

Desktop, left to right: logo to `/`, Product (click menu), Imagine (`/imagine`), Community (click menu), Pricing (`/pricing`), Learn (`/learn`), Download (`/download`). Right side: Log in, Try Craft Free. The bar is a white pill, 52px tall, 26px radius. A black promo bar above it links to `/pricing`.

| Control | Opens |
|---|---|
| Product | A white panel on the same URL. Plan (`/plan`), Write (`/write`), Organize (`/organize`), Customize (`/customize`), What's New (`/whats-new`), Imagine (`/imagine`), Help and Support (`https://support.craft.do`, not followed), Blog (`/blog`). |
| Community | A white panel on the same URL. Reddit Community (`https://www.reddit.com/r/CraftDocs`, not followed), Slack (`https://craft.do/community`, not followed), X / Twitter (`https://x.com/craftdocsapp`, not followed). |
| Imagine | `/imagine` |
| Pricing | `/pricing` |
| Learn | `/learn` |
| Download | `/download` |
| Log in | Login wall. |
| Try Craft Free | `/download` |

Phone (390): promo bar, logo, Try Craft Free, and a menu button. The open drawer expands Product (Plan, Write, Organize, Customize, What's New, Imagine, Help and Support, Blog) and lists Imagine, Pricing, Learn, Download, and Community. Community was left collapsed. Download, Log in, and Try Craft Free sit at the bottom of the drawer. The drawer was photographed. No row was followed.

## Homepage body

URL stays `/` unless noted. Feature chips (Docs, Tasks, Calendar, Whiteboards, Daily Notes) are section labels, not routes.

| Control | Opens |
|---|---|
| Black Friday banner | `/pricing` |
| Try Craft Free, hero | `/download` |
| Learn more, writing | `/write` |
| Learn more, Imagine | `/imagine` |
| MCP client links | `/imagine/guide/mcp/...` (linked, not each opened) |
| API tool links | `/imagine/guide/api/...` (linked, not each opened) |
| Explore community templates | `/imagine#community` |
| Learn more, planning | `/plan` |
| Learn more, customize | `/customize` |

Accordion buttons (MCP Connections, API Integrations, Start Building, Community, Calendar, Tasks, Journal, Reminders) expand in place. They do not navigate. Two were already expanded on load. None submit a form.

## Footer

Black panel, 24px radius, ink `#030302`. Columns: Product, Community, Support, Company, Download. Social icons for Instagram, YouTube, X, and LinkedIn were not followed. Store and installer links were not followed. Contact Support is a mailto link and was not sent.

| Control | Opens |
|---|---|
| Product Releases | `/whats-new` |
| Write, Plan, Organize, Customize | Those product pages |
| Imagine With Craft | `/imagine` |
| Pricing | `/pricing` |
| Education Plan | `/education` (linked, not opened this pass) |
| Learn, Use Cases, Compare Craft, Getting Started Guide, Template Gallery | `/learn`, `/for`, `/compare`, `/getting-started`, `/templates` (linked, not each opened) |
| Help Center | `https://support.craft.do/` (not followed) |
| About us, Blog, Careers, Affiliate Program, Media | `/about`, `/blog`, `/careers`, `/affiliates`, `/media` |
| Terms, Privacy, Security, ESG, Responsible Disclosure | Those legal paths (linked, not each opened) |
| English | A button in the footer. Clicking it did not open a locale dialog in this capture. Locales were not followed. |

## Pages opened

| Page | What it is |
|---|---|
| `https://www.craft.do/` | Marketing home. Sky collage, serif headline, white pill nav. |
| `https://www.craft.do/pricing` | Starter, Plus, Family, Team, Enterprise. Yearly is the painted default. Prices in this region rendered SGD. Monthly was not switched. Checkout was not entered. |
| `https://www.craft.do/download` | Desktop and mobile download cards. No installer was started. |
| `https://www.craft.do/imagine` | Imagine product page. |
| `https://www.craft.do/learn` | Learn. |
| `https://www.craft.do/write` | Write. |
| `https://www.craft.do/plan` | Plan. |
| `https://www.craft.do/organize` | Organize. |
| `https://www.craft.do/customize` | Customize. |
| `https://www.craft.do/blog` | Blog index. |
| `https://www.craft.do/about` | About. |
| `https://www.craft.do/whats-new` | Product releases. The first viewport. |
| `https://www.craft.do/this-page-does-not-exist-capture-2026` | 404. "Page Not Found \| 404". Let us know was not clicked. |
| `https://docs.craft.do/` | Login and signup wall. Empty. |

Support, the app stores, Reddit, Slack, and X are other hosts. They were not captured as product pages.
