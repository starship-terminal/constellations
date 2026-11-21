# Asana public site tree

Mapped 2026-11-21 from https://asana.com/ in headless Chromium (1440×900) before screenshots. Controls were expanded or read. No form was submitted. No email was typed. Google and Microsoft were not clicked.

The English sitemap lists 2,861 paths. Most are catalog items (resources, app directory, blog posts, templates, case studies, legal revisions). This tree records the controls on the homepage and footer, the page each one opens, and where a branch stops.

## Homepage header

| Control | Opens |
|---|---|
| Wordmark | `/` |
| Products (button, `aria-controls=product-tab-panel`) | Mega menu, not a page. Links below. |
| Solutions (button, `aria-controls=solutions-tab-panel`) | Mega menu, not a page. Links below. |
| Learning and support (button, `aria-controls=resources-tab-panel`) | Mega menu, not a page. Links below. |
| Pricing | `/pricing` |
| Log in | `https://app.asana.com/-/login` — auth wall. Stop. |
| Contact sales | `/sales` (visible once Products or Solutions is open) |
| Get started | `/create-account` — public signup shell. Stop before submit. |

### Products menu

| Label | Opens |
|---|---|
| Agentic Work Management | `/product/ai` |
| Asana Service Management | `/product/service-management` |
| Asana Client Management | `/product/client-management` |
| Command by Asana | `/product/command` |
| StackAI by Asana | `https://www.stackai.com/` — external. Stop. |
| AI Teammates | `/product/ai/ai-teammates` |
| AI Studio | `/product/ai/ai-studio` |
| Asana Dash | `/product/ai/dash` |
| Admin and security | `/features/admin-security/` |
| App integrations | `/apps` |
| Developer | `/developers` |
| Latest feature release | `/whats-new` |

### Solutions menu

| Label | Opens |
|---|---|
| Enterprise | `/enterprise` |
| Small business | `/small-business` |
| Nonprofit | `/industry/nonprofit` |
| Agencies | `/agencies` |
| Operations | `/teams/operations` |
| Marketing | `/teams/marketing` |
| IT | `/teams/it` |
| Leaders | `/teams/leaders` |
| Government | `/industry/government-solutions` |
| Healthcare | `/industry/healthcare` |
| Retail | `/industry/retail` |
| Financial services | `/industry/financial-services` |
| Education | `/industry/education` |
| Manufacturing | `/industry/manufacturing` |
| Media and entertainment | `/industry/media-entertainment` |
| Goal management | `/uses/goal-management` |
| Organizational planning | `/uses/organizational-planning` |
| Project intake | `/uses/project-intake` |
| Resource planning | `/uses/resource-planning` |
| Product launches | `/uses/product-launch` |
| View all use cases | `/uses` |

### Learning and support menu

Opened 2026-11-21. Panel id `resources-tab-panel`.

| Label | Opens |
|---|---|
| Blog | `/inside-asana` |
| Events and webinars | `/events` |
| Customer stories | `/customers` |
| Resource center | `/resources` |
| Asana Academy | `https://academy.asana.com/` — other host. Stop. |
| Certifications | `/certifications` |
| Trainings | recorded in the menu text. Destination not separately captured this pass. |
| Help Center | `https://help.asana.com/s/` — other host. Stop. |
| Community | `https://forum.asana.com/` — other host. Stop. |
| Templates | `/templates` |
| Customer Success | `/customer-success` |
| Find a partner | `/partners` |
| Become a partner | `/partners` (same public partners page unless a later control says otherwise) |

## Homepage body (visible without opening a menu)

| Control | Opens |
|---|---|
| Enterprise governance (accordion, `aria-expanded=false`) | In-page panel. Not a navigation. |
| Quality Coordinator card | `https://app.asana.com/0/ai-teammate/new?preset=issues_intake_specialist` — app host. Auth wall. Stop. |
| Discover resources | `/resources` |
| Start with a template | `/templates` |
| Product overview | `/product` |
| Creative production | `/uses/creative-production` |
| Product (team card) | `/teams/product-managers` |

## Footer (same shell on public pages)

| Control | Opens |
|---|---|
| Starter plan | `/plan/starter` |
| Advanced plan | `/plan/advanced` |
| All features | `/features` |
| All teams | `/teams` |
| Help Center | `https://help.asana.com/s/` — other host. Recorded, not walked. |
| Get support | `https://help.asana.com/s/#chat` — chat wall. Stop. |
| Asana Academy | `https://academy.asana.com/` — other host. Stop. |
| Forum | `https://forum.asana.com/` — other host. Stop. |
| Resource center | `/resources/category/all` |
| Events and webinars | `/events` |
| Customer Success | `/customer-success` |
| Developers and API | `https://developers.asana.com/docs/` — other host. Stop. |
| Partners | `/partners` |
| Sitemap | `/site-map` |
| About us | `/company` |
| Leadership | `/leadership` |
| Customers | `/customers` |
| Careers | `/jobs` |
| Blog | `/inside-asana` |
| Culture | `/culture-and-belonging` |
| Press | `/press` |
| Investor relations | `https://investors.asana.com/` — other host. Stop. |
| Trust and security | `/trust` |
| Privacy | `/privacy` |
| Supplier responsibility | `/terms/modern-slavery-statement` |
| Sustainability and ESG | `https://investors.asana.com/sustainability` — other host. Stop. |
| Language switcher (`#i18n`) | Locale links (`/de`, `/es`, `/fr`, `/ja`, and the rest). Not walked. English only. |
| Social icons | x.com, linkedin.com, instagram.com, facebook.com, youtube.com. External. Stop. |
| Terms | `/terms` |
| Privacy statement | `/terms/privacy-statement` |
| App Store / Play Store | itunes.apple.com, play.google.com. External. Stop. |

## Auth and signup walls (stop)

| URL | Why the branch stops |
|---|---|
| `https://app.asana.com/-/login` | Loaded 2026-11-21 as a public login shell: Google, Microsoft, or email, plus reCAPTCHA. Branch stopped. No email typed. Google and Microsoft not clicked. A prior probe had accepted an email and then stuck on Signing Up. |
| `https://app.asana.com/0/ai-teammate/new` | App host. Same wall. |
| `/create-account`, `/create-account-mobile`, `/create-account-signup` | Public shells only. Fields may be focused. Never submitted. |
| `/sso-redirect`, `/logged-in`, `/invite`, `/invite-confirmation`, `/join-guided-trial` | Session or invite gates. Not followed. |

## In-page interactions on captured pages

| Page | Control | Result |
|---|---|---|
| `/` desktop | Products or Solutions | Mega menu (flyout) |
| `/` phone | Menu button | Full-screen nav |
| `/pricing` | FAQ question (`aria-expanded`) | Accordion panel |
| `/pricing` | Billing period control, if present | In-page toggle. Not a submit. |
| `/sales` | Selects and fields | Focus only. Not submitted. |
| Any page | Cookie / location dialog | Hidden, never accepted or rejected. |

## Catalog depth not walked page by page

These indexes are reachable from the tree above. Their children share one template. One index plus one child stands in for the set.

| Index | Sitemap count (English) | Child example |
|---|---|---|
| `/resources` | 782 | first article linked from the index |
| `/apps` | 647 | `/apps/slack` |
| `/inside-asana` | 585 | first post linked from the index |
| `/templates` | 265 | first template linked from the index |
| `/case-study` | (under customers) | first story linked from `/customers` |
| `/terms` | 70 | `/terms` and `/terms/privacy-statement` |
| `/uses` | 54 | the five Solutions-menu use cases |
| `/features` | 30 | `/features` and `/features/admin-security` |
| `/jobs` | 21 | `/jobs` index only. Applications not opened. |
| `/compare` | 11 | first compare link from a product page, if one is on screen |

## Not a public design surface

`/-/tracking`, `/error`, `/inactive-link`, `/go/*`, `/campaign/*`, `/demo/*`, `/plan` checkout variants beyond the two footer plan pages, and locale mirrors. Recorded here so a later pass does not treat a miss as a forgotten control.
