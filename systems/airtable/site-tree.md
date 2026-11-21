# Airtable public site tree

Mapped from https://www.airtable.com/ on 2026-11-21, signed out, desktop 1440×900, before screenshots. The page title was "Airtable: Build Enterprise-ready AI Workflows, Apps & Agents | Airtable". The h1 was "All your teams, all their workflows—connected in one workspace". The site is a live marketing product, not a parked domain.

The product app (bases, interfaces, automations) sits behind Log in and Sign up. This tree stops at those walls. Identity-provider buttons were recorded and not clicked. No email, password, or code was typed. No form was submitted.

## Chrome

A promo bar sits above the header. "Try it now" opens https://www.airtable.com/lp/claude-airtable. "Close promo banner" dismisses the bar on this page only.

The wordmark ("Airtable home or view your bases") opens https://www.airtable.com/.

| Control | Opens |
|---|---|
| Platform (button, `aria-haspopup`, `aria-expanded`) | Slide-in nav drawer, Platform panel |
| Solutions (button, `aria-haspopup`) | Same drawer, Solutions panel |
| Resources (button, `aria-haspopup`) | Same drawer, Resources panel |
| Enterprise (link) | https://www.airtable.com/solutions/enterprise |
| Pricing (link) | https://airtable.com/pricing |
| What's new (link) | https://airtable.com/whatsnew |
| Book Demo (link) | https://www.airtable.com/contact-sales |
| Sign up for free (link) | https://airtable.com/signup (account wall; not followed) |
| Log in (link) | https://airtable.com/login (account wall; photographed, not submitted) |

Escape and "Close menu" close the drawer. A nested panel has "Go back to previous menu options".

A Transcend consent host (`#transcend-shadow-root`) can cover drawer clicks. It was hidden, not accepted or rejected.

## Platform drawer

Clicking Platform opens the drawer. Primary links:

| Label | Opens |
|---|---|
| Airtable Platform | https://www.airtable.com/platform |
| AI App Building | https://www.airtable.com/platform/app-building |
| AI Agents | https://www.airtable.com/platform/ai-agents |
| MCP | https://www.airtable.com/platform/mcp |
| Scale | https://www.airtable.com/platform/hyperdb |
| Download | https://www.airtable.com/downloads |
| Explore the platform | https://www.airtable.com/platform |

"Platform Features" is a nested toggle inside the same drawer. It lists:

| Label | Opens |
|---|---|
| What's New | https://www.airtable.com/whatsnew |
| Automations | https://www.airtable.com/platform/automations |
| Governance & Security | https://www.airtable.com/platform/governance |
| Portals | https://www.airtable.com/platform/portals |
| Airtable AI | https://www.airtable.com/platform/ai |
| Databases | https://www.airtable.com/platform/connected-data |
| Interfaces | https://www.airtable.com/platform/interface-designer |
| Reporting | https://www.airtable.com/platform/reporting |

"Integrations" is a nested toggle in the same drawer. It lists:

| Label | Opens |
|---|---|
| Slack | https://www.airtable.com/integrations/slack |
| Google Drive | https://www.airtable.com/integrations/google-drive |
| Salesforce | https://www.airtable.com/integrations/salesforce |
| Jira | https://www.airtable.com/integrations/jira |
| Zendesk | https://www.airtable.com/integrations/zendesk |
| See all integrations | https://www.airtable.com/integrations |

## Solutions drawer

Clicking Solutions replaces the drawer panel. No nested toggle on this panel.

| Label | Opens |
|---|---|
| Use Cases | https://www.airtable.com/use-cases |
| Product | https://www.airtable.com/solutions/product |
| Marketing | https://www.airtable.com/solutions/marketing |
| Project Management | https://www.airtable.com/solutions/project-management |
| Operations | https://www.airtable.com/solutions/operations |
| Sales | https://www.airtable.com/solutions/sales |
| Design & Creative | https://www.airtable.com/solutions/design-creative-project-management |
| Human Resources | https://www.airtable.com/solutions/hr |
| Finance | https://www.airtable.com/solutions/finance |
| Learn more (story card) | https://www.airtable.com/customer-stories/code-and-theory |

The header Enterprise link and the footer Enterprise link are different pages. The header goes to `/solutions/enterprise`. The footer column labelled Enterprise goes to https://www.airtable.com/services.

## Resources drawer

Clicking Resources opens four nested toggles plus a link list.

Top links: AI Plays (`/ai-plays`), Blog (`/articles`), Customer Stories (`/customer-stories`), Videos (`/videos`), Events (`/events-webinars`), Airtable Academy (`https://academy.airtable.com/`), Airtable Community (`https://community.airtable.com/`), How-to guides (`/guides`), Explore all resources (`/lp/resources`).

Resources Hub (nested) opens filter pages on the hub: Reports, eBooks, Webinars, Quick Reads, Demos (`/lp/resources?filter=…`), and See all resources.

Templates (nested) opens individual template pages under `/templates/…` and See all templates (`https://www.airtable.com/templates`).

Developers Docs (nested) opens Dev Community (`https://community.airtable.com/t5/development-apis/bd-p/development`), API Docs (`https://airtable.com/developers/web/api/introduction`), Custom Extensions (`https://airtable.com/developers/apps`), Scripting (`https://airtable.com/developers/scripting`).

Support (nested) opens Help center (`https://support.airtable.com/`) and Contact Support (`https://support.airtable.com/docs/contacting-airtable-support`).

## Homepage body

| Control | Opens |
|---|---|
| Get started for free | https://airtable.com/signup (account wall; not followed) |
| Book demo | https://www.airtable.com/contact-sales |
| Feature tabs 01–04 (AI app building, Agents at Scale, Meet Omni, Enterprise capabilities) | In-page panels, not a new route |
| Learn more (app building) | https://www.airtable.com/platform/app-building |
| Learn more (agents) | https://www.airtable.com/platform/ai-agents |
| See AI plays, and the four play prompts | https://www.airtable.com/ai-plays |
| Builders & Breakthroughs | https://www.airtable.com/breakthroughs |
| The 2026 AI guide for marketers | https://www.airtable.com/lp/resources/ebooks/ultimate-ai-guide-for-marketers |
| In action: Airtable ProductCentral | https://www.airtable.com/lp/resources/demos/airtable-productcentral-demo |
| Explore all customer stories | https://www.airtable.com/customer-stories |
| Pause video | Pauses the in-page demo video. Public demo, not the signed-in product. |

## Footer

Column headings (Platform, Solutions, Resources, Learn, Company) are accordion buttons at phone width and static headings at desktop. "See more" / "Show less" toggles extra links in a column. "Cookie Preferences" is an in-page hash control for the consent manager and was not submitted.

Company and legal links include About (`/about`), Careers (`/careers`), Pricing, Contact sales (`/contact-sales`), Contact support, Status (`https://status.airtable.com/`), Newsroom (`/newsroom`), Security (`/company/trust-and-security`), API, Privacy, Terms, Do Not Sell/Share My Info (`/company/privacy-choices`), Accessibility (`/company/accessibility`). Try Airtable for free goes to `/signup` and was not followed.

## Account walls (not entered)

https://airtable.com/login (title "Sign in - Airtable") shows "Welcome to Airtable", an email field, Continue, Continue with Single Sign On, Continue with Google, Continue with Apple ID, and Continue with ChatGPT. None of those were used.

https://airtable.com/signup shows the same wall with "Work email", Continue, SSO, Google, Apple, and ChatGPT. Not followed from the homepage, and not submitted.
