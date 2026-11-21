# Runey public site tree

Mapped on 2026-11-21 from https://runey.app/ in headless Chromium (Playwright), signed out, desktop 1440×900. Phone 390×844 was checked for the home nav only. No form was submitted. No password, code, or account field was typed.

A control that opens https://runey.app/auth (email and password, or Google) stops that branch. Password was not submitted.

## Walls (stop)

| Control or URL | Lands on | What is on the wall |
|---|---|---|
| Header "Log in", footer "Login", "Sign up" | https://runey.app/auth | Email, password, Continue with Google |
| "Start for free", "Start 14-day free trial", "Create your first invoice" | https://runey.app/auth | Same wall |
| https://runey.app/pricing | https://runey.app/auth?redirect=%2Fpricing | Same wall. Public pricing is the home `#pricing` section, not this path |
| https://runey.app/blog | https://runey.app/auth?redirect=%2Fblog | Same wall |
| https://runey.app/about | https://runey.app/auth?redirect=%2Fabout | Same wall |
| https://runey.app/privacy | https://runey.app/auth?redirect=%2Fprivacy | Same wall. Public privacy page is https://runey.app/policy |
| https://runey.app/changelog | https://runey.app/auth?redirect=%2Fchangelog | Same wall. Public changelog is https://runey.app/updates |
| https://runey.app/features | https://runey.app/auth?redirect=%2Ffeatures | Same wall. Feature pages are `/features/<slug>` |
| https://runey.app/legal | https://runey.app/auth?redirect=%2Flegal | Same wall |
| https://runey.app/login | https://runey.app/auth?redirect=%2Flogin | Same wall |
| https://runey.app/signup | https://runey.app/auth?redirect=%2Fsignup | Same wall |

`robots.txt` disallows `/dashboard`, `/invoices`, `/projects`, `/customers`, `/expenses`, `/proposals`, `/settings`, `/profile`, `/billing`, and `/auth`. Those app paths were not opened.

## Home (https://runey.app/)

| Control | Opens |
|---|---|
| Logo | https://runey.app/ |
| Features (header button) | Menu on the same page. Items: Invoicing `/features/invoices`, Projects & Tasks `/features/projects`, Customers `/features/customers`, Dashboard `/features/dashboard`, Expenses `/features/expenses`, Proposals `/features/proposals` |
| FAQ | `/#faq` |
| Pricing | `/#pricing` |
| Updates | `/updates` |
| Log in | Wall: `/auth` |
| Start for free | Wall: `/auth` |
| See features | `#features` |
| Request demo | `/contact` |
| Previous / Next | Hero carousel on the same page (invoices, quotes, proposals, projects) |
| Invoicing, Projects & Tasks, Time Tracker, Customers, Dashboard, Expenses, Proposals, Automations, Integrations | Feature tabs on the same page. They swap the panel. They do not navigate |
| Monthly, Yearly, Lifetime | Pricing period toggle on `#pricing`. Same page |
| Start 14-day free trial | Wall: `/auth` |
| Get in touch | `/contact` |
| FAQ questions (buttons) | Accordion on `#faq`. "More questions" goes to `/faq` |
| Cookie banner: Accept all, Reject all | Dismisses the banner. Not clicked during mapping, so consent was not posted |
| Cookie banner: Customize | Opens the preference panel on the same page: Essential (required switch, on) and Analytics (off). Save preferences and Reject all sit in that panel. Not submitted |
| Phone: 36×36 header button | Mobile menu. Features is not a visible header button at 390 until that control opens |

Home section ids: `features`, `invoices`, `pricing`, `faq`.

Footer, repeated on public pages:

| Control | Opens |
|---|---|
| Home | `/` |
| Features | `/#features` |
| FAQ | `/faq` |
| Help & Docs | `/help` |
| Updates | `/updates` |
| Request demo | `/contact` |
| Sign up, Login | Wall: `/auth` |
| Dashboard | `/#dashboard` |
| Invoices | `/#invoices` |
| Projects | `/#projects` |
| Clients | `/#clients` |
| Expenses | `/features/expenses` |
| Proposals | `/#proposals` |
| Contact | `/contact` |
| Terms of Use | `/terms` |
| Privacy Policy | `/policy` |
| Cookie Policy | `/cookies` |

External badge links in the footer (not followed for capture): findly.tools, startupfa.me, twelve.tools, wired.business, turbo0.com, foundrlist.com, tooldisk.com, indiehunt.io, tinylaunchpad.com.

## Feature pages

Each is a marketing page. "See …" links across them. "Create your first invoice" and "Start for free" are the auth wall.

| Page | URL |
|---|---|
| Invoicing | https://runey.app/features/invoices |
| Projects & Tasks | https://runey.app/features/projects |
| Customers | https://runey.app/features/customers |
| Dashboard | https://runey.app/features/dashboard |
| Expenses | https://runey.app/features/expenses |
| Proposals | https://runey.app/features/proposals |

## Updates

https://runey.app/updates lists posts. Each title opens one post. No dialog.

| Date | URL |
|---|---|
| Sep 21, 2026 | `/updates/proposal-template-library-23-ready-made-templates` |
| Jun 21, 2026 | `/updates/customer-project-stages` |
| May 27, 2026 | `/updates/invoice-from-time-tracking` |
| May 21, 2026 | `/updates/slack-integration-is-now-available-in-runey` |
| May 20, 2026 | `/updates/pages-in-runey` |
| May 19, 2026 | `/updates/proposal-quote-signatures` |
| May 18, 2026 | `/updates/data-import-is-now-available-in-runey` |
| May 16, 2026 | `/updates/runey-for-macos` |
| May 8, 2026 | `/updates/team-collaboration-is-now-live-in-runey` |
| May 7, 2026 | `/updates/new-task-modal-kanban-board-in-runey` |
| May 5, 2026 | `/updates/new-navigation-dashboard-and-powerful-invoicing-improvements` |
| Apr 24, 2026 | `/updates/schedule-invoices` |
| Apr 21, 2026 | `/updates/payment-templates` |
| Apr 15, 2026 | `/updates/save-your-own-templates-for-invoices-proposals` |
| Apr 14, 2026 | `/updates/attach-files-to-your-documents` |
| Apr 14, 2026 | `/updates/chat-for-invoices-proposals` |
| Apr 8, 2026 | `/updates/monthly-reports` |
| Apr 8, 2026 | `/updates/share-projects-with-your-clients` |
| Apr 6, 2026 | `/updates/time-tracking-and-automatic-invoice-generation-from-projects` |
| Apr 2, 2026 | `/updates/password-protection-and-expiring-public-invoice-links` |
| Apr 2, 2026 | `/updates/zapier-integration-and-webhooks-are-now-available` |
| Apr 2, 2026 | `/updates/create-beautiful-proposals-and-win-more-projects` |
| Apr 2, 2026 | `/updates/receipts-and-partial-payments-are-now-available` |
| Apr 2, 2026 | `/updates/stripe-payments-payment-links-and-qr-codes` |
| Apr 2, 2026 | `/updates/runey-is-live-your-invoicing-and-project-management-app` |

## Help

https://runey.app/help is a docs shell. Topic buttons navigate. Article names inside a section stay on that section URL (in-page), they do not each have their own path.

| Control | URL | Heading seen |
|---|---|---|
| Getting Started, and its articles (Welcome to Runey, First Steps, Onboarding Checklist, Dark & Light Mode, Understanding Your Dashboard, Quick Actions, Global Search, Notification Center, Reports) | `/help/getting-started` | Welcome to Runey |
| Settings & Account | `/help/settings` | Branding & Themes |
| Customers | `/help/customers` | Managing Customers |
| Projects | `/help/projects` | Managing Projects |
| Invoices & Quotes | `/help/invoices` | Creating Invoices |
| Proposals | `/help/proposals` | Creating Proposals |
| Expenses | `/help/expenses` | Tracking Expenses |
| Integrations | `/help/integrations` | Connecting Stripe |
| Next First Steps | `/help/getting-started` | Welcome to Runey |

Help describes a signed-in Dark & Light Mode. The public site did not follow `prefers-color-scheme: dark` (page background stayed `rgb(250, 250, 250)`). No public theme switch was found.

## Other public pages

| Page | URL | Interaction |
|---|---|---|
| FAQ | https://runey.app/faq | Question buttons expand answers on the page |
| Contact | https://runey.app/contact | Marketing page. No public form fields were in the DOM. "Request demo" is this page |
| Feedback & Roadmap | https://runey.app/feedback | "Send Feedback" is a button. No name, email, or message field was filled. Not submitted |
| Terms of Service | https://runey.app/terms | Document. Last updated May 20, 2026 |
| Privacy Policy | https://runey.app/policy | Document. Last updated May 20, 2026. Links out to stripe.com and slack.com legal pages |
| Cookie Policy | https://runey.app/cookies | Document. "Manage cookie preferences" opens the same preference panel as Customize |

## Sample invoices linked from the home demo

Home carousel cards link to `/invoice/<id>` (nine ids seen). Opening `https://runey.app/invoice/d277b3a0715b4c55` returned the marketing shell (title "Runey — Invoices, Projects & Clients in One Place"), not a document viewer. Treated as a demo link that does not expose a public invoice. Not captured as an app screen.

## Theme

One public theme: light. `color-scheme` on the home page was `normal`. No `data-theme` and no theme class. Dark mode is documented as an in-app setting and was not reached.
