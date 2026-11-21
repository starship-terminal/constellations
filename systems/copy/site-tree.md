# Copy.ai site tree

Mapped 2026-11-21 from [https://www.copy.ai/](https://www.copy.ai/) with headless Playwright (desktop 1440×900, then the phone menu at 390×844). Every row is a control that was present on the loaded homepage. Auth branches were opened once to confirm the wall, then not followed. No form was submitted. No identity provider was clicked. The HubSpot cookie script is present as a tag and did not paint a banner in this session, so it was not answered.

The same shell repeats on the public marketing pages: top announcement, header, footer. Those rows are written once.

## Shell (homepage, and the same header on public marketing pages)

| Control | Opens |
|---|---|
| Announcement "The 2026 Benchmarks Report is Finally Here!" | External page `https://www.fullcast.com/ebooks/2026-benchmarks-report-the-state-of-gtm-in-2026/`. Not followed. |
| Logo | Page `/` |
| Nav toggle Platform | Menu panel, not a navigation. Links below. |
| Nav toggle Use cases | Menu panel. Links below. |
| Nav toggle Resources | Menu panel. Links below. |
| Nav toggle GTM AI | Menu panel. Links below. |
| Nav link Pricing | Page `/prices` |
| Nav link Login | Auth wall `https://app.copy.ai/login` (redirects toward the login host). Branch stopped. |
| Nav link Get a Demo | Page `/request-a-demo` (demo request form). Not submitted. |
| Burger (`.mega--nav_burger_trigger`, phone) | Same four menus plus Pricing, Login and Get a Demo, as a full-screen menu. |
| Email field "What's your email?" plus submit | Form on the homepage (`#wf-form-formref`, method get). Not submitted. A Turnstile widget is in the form. Not solved. |

### Platform menu

| Control | Opens |
|---|---|
| How it Works | Page `/platform/how-it-works` |
| Platform Components | Page `/platform/platform-components` |
| Powering GTM AI | Page `/platform/powering-gtm-ai` |
| What are Workflows? | Page `/platform/what-are-workflows` |
| Building Workflows | Page `/platform/building-workflows` |
| Copy Agents | Page `/platform/copy-agents` |
| Tables | Page `/platform/tables` |
| Actions | Page `/platform/actions` |
| Brand Voice | Page `/platform/brand-voice` |
| The Power of "Actions" for GTM Teams | Page `/blog/the-power-of-actions-for-gtm-teams` |
| Introducing Tables | Page `/blog/introducing-tables` |
| What's the Difference Between LLMs? | Page `/blog/difference-between-llms` |

### Use cases menu

| Control | Opens |
|---|---|
| Prospecting Cockpit | Page `/use-cases/prospecting-cockpit` |
| Inbound Lead Processing | Page `/use-cases/inbound-lead-processing` |
| Deal Coaching & Forecasting | Page `/use-cases/deal-management-forecasting` |
| Account Based Marketing | Page `/use-cases/account-based-marketing` |
| Content Creation | Page `/use-cases/content-creation` |
| Translation & Localization | Page `/use-cases/localization-translation` |
| Lead + Account Intelligence | Page `/use-cases/lead-account-intelligence` |
| CRM Enrichment | Page `/use-cases/crm-enrichment` |
| GTM Systems Integrations | Page `/use-cases/gtm-systems-integrations` |
| Cold Email Best Practices Guide | Page `/blog/cold-email-best-practices-guide-2024-edition` |
| AI for Thought Leadership | Page `/blog/ai-for-thought-leadership` |
| How to Prospect for Sales in an AI-Driven World | Page `/blog/how-to-prospect-for-sales` |

### Resources menu

| Control | Opens |
|---|---|
| Marketing | Page `/resources/marketing` |
| Sales | Page `/resources/sales` |
| Operations | Page `/resources/operations` |
| Blog | Page `/blog` |
| For The Enterprise | Page `/enterprise` |
| Trust Center | External `https://trust.copy.ai/` |
| Webinars | Page `/webinars` |
| Help Center | External `https://support.fullcast.com/copy-ai` |
| Contact Support | Page `/contact-us` (header). Footer "Contact Support" is a mailto to the support address. Not sent. |
| Changelog | Page `/changelog` |
| The Power of "Actions" for GTM Teams | Page `/blog/the-power-of-actions-for-gtm-teams` |
| Introducing Tables | Page `/blog/introducing-tables` |
| How Automated Workflows and SOC 2 Compliance Protect Your Data | Page `/blog/how-automated-workflows-and-soc-2-compliance-protect-your-data` |

### GTM AI menu

| Control | Opens |
|---|---|
| Marketing | Page `/planning/marketing` |
| Sales | Page `/planning/sales` |
| Operations | Page `/planning/operations` |
| Sales Development | Page `/planning/sales-development` |
| Why GTM AI | Page `/gtm-ai` |
| Goodbye, Copilots | Page `/goodbye-copilots` |
| The Problem with AI SDRs | Page `/injured` |
| How to Go from GTM Bloat to Velocity | Page `/blog/introducing-gtm-ai` |
| GTM AI: A New Approach for Getting Rid of GTM Bloat | Page `/blog/gtm-ai` |
| AI Copilots & The Illusion of Progress | Page `/blog/the-illusion-of-progress-the-marginal-gains-from-ai-copilots` |

### Footer columns

| Control | Opens |
|---|---|
| Platform column (How it Works through Brand Voice, plus Infobase) | Same platform pages as the menu, plus `/features/infobase`. Actions and Chat are in the footer markup with class `hide`. |
| Use cases column | Same nine use-case pages as the menu. |
| Resources column | Marketing, Sales, Operations, Blog, Enterprise, Trust Center, Webinars, Help Center, Changelog. |
| Company column | Home `/`, Pricing `/prices`, GTM AI in-page `https://www.copy.ai#why-gtm-ai`, Careers external `https://jobs.lever.co/CopyAI`, Free Tools `/tools`, Podcasts `/podcasts`, Live Training `#` (no destination), Help Docs external support host, Community `#` (no destination). |
| Privacy Notice | Page `/privacy-notice` |
| Terms of Service | Page `/terms-of-service` |
| Status | External `https://status.copy.ai/` |
| LinkedIn, Facebook, Twitter icons | External social profiles. Not followed. |
| Marketing (archive) | Page `/archive/email-marketers-old` |
| Events | Page `/webinars` (footer markup class `hide`) |

## Home `/`

| Control | Opens |
|---|---|
| Get Demo on each playbook card | Page `/request-a-demo`. Not submitted. |
| Learn more, Prospecting Cockpit | Page `/use-cases/prospecting-cockpit` |
| Learn more, Content Creation | Page `/use-cases/content-creation` |
| Learn more, Inbound Lead Processing | Page `/use-cases/inbound-lead-processing` |
| Learn more, Account Based Marketing | Page `/use-cases/account-based-marketing` |
| Learn more, Translation & Localization | Page `/use-cases/localization-translation` |
| Learn more, Deal Coaching & Forecasting | Page `/use-cases/deal-management-forecasting` |
| Workflows card | Page `/platform/what-are-workflows` |
| Actions card | Page `/platform/actions` |
| Agents card | Page `/platform/copy-agents` |
| Tables card | Page `/platform/tables` |
| Chat card | Page `/chat` |
| Infobase card | Page `/features/infobase` |
| Brand Voice card | Page `/platform/brand-voice` |
| Blog slider cards | Posts `/blog/the-illusion-of-progress-the-marginal-gains-from-ai-copilots`, `/blog/the-worlds-first-gtm-ai-platform`, `/blog/gtm-ai`, `/blog/introducing-gtm-ai` |
| Get a demo (closing band) | Page `/request-a-demo`. Not submitted. |

No dialog, search field, settings control, or create-account control is on the homepage. Signup and the product sit behind Login.
