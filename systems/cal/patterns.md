# Cal.com patterns

Public pages only. The signed-in scheduler is a recorded boundary.

## App shell

Every marketing page shares a sticky 64px bar: wordmark, five menu triggers (Products, Use cases, AI, Features, Resources), Enterprise, Pricing, Talk to sales, Sign in, and a Get started pill. The footer repeats product, industry, tool, developer, company and legal columns.

Screenshot: [screenshots/home-light-default.png](screenshots/home-light-default.png).

## Mega-menu

Hover or click on a nav trigger opens a panel. Products lists Cal Desktop, the companion app, Scheduling Links, Event planning and Discover. Use cases lists industries and a healthcare drill-in. AI lists Cal.ai, Agent, Assistant, MCP, Grok Bot and Cal Desktop. Features lists event, team, payments and platform links. Resources lists docs, stories, company and legal links.

| Trigger | Screenshot |
|---|---|
| Products | [screenshots/home-light-menu-products.png](screenshots/home-light-menu-products.png) |
| Use cases | [screenshots/home-light-menu-use-cases.png](screenshots/home-light-menu-use-cases.png) |
| AI | [screenshots/home-light-menu-ai.png](screenshots/home-light-menu-ai.png) |
| Features | [screenshots/home-light-menu-features.png](screenshots/home-light-menu-features.png) |
| Resources | [screenshots/home-light-menu-resources.png](screenshots/home-light-menu-resources.png) |

The phone control labelled Open menu opens a drawer: [screenshots/mobile-home-light-menu.png](screenshots/mobile-home-light-menu.png).

## Hero

A large Cal Sans headline (80px on the home page), a muted subline, and a signup row that offers Google, Microsoft and email. Those three controls navigate to `app.cal.com` and were not clicked. The row is visible in the home screenshot.

## Pricing

Plan cards on [screenshots/pricing-light-default.png](screenshots/pricing-light-default.png). A billing toggle, when present, is [screenshots/pricing-light-billing-toggle.png](screenshots/pricing-light-billing-toggle.png).

## Auth wall

Sign in and Get started leave the marketing host.

| Control | Opens | What was done |
|---|---|---|
| Sign in | https://app.cal.com/auth/login | Photographed. Email and password left empty. Google, Microsoft and SAML not clicked. |
| Get started | https://app.cal.com/signup | Photographed. No account created. |

Screenshots: [screenshots/login-wall-light-auth-wall.png](screenshots/login-wall-light-auth-wall.png), [screenshots/signup-wall-light-auth-wall.png](screenshots/signup-wall-light-auth-wall.png).

## FAQ

The home page FAQ is a disclosure list. One item was opened: [screenshots/home-light-faq-open.png](screenshots/home-light-faq-open.png).

## Feature and industry pages

Feature pages (`/features/*`, `/scheduling/*`) reuse the same shell, a display headline and a long marketing column. One of each family is in screenshots: scheduling, round-robin, healthcare, sales, workflows, routing, teams.

## Docs and help

`/docs` and `/help` are public documentation. They use a different shell from the marketing home. Screenshots: [screenshots/docs-light-default.png](screenshots/docs-light-default.png), [screenshots/help-light-default.png](screenshots/help-light-default.png).

## Empty, loading, error, destructive confirmation

Not present on the public marketing pages. The scheduler's empty states sit behind the login wall and were not captured.

## Onboarding and search

Not present without an account. Discover (`/discover`) is a public directory, not the signed-in search.
