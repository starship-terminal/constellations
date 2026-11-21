# Slack public site tree

Mapped from the live homepage with Playwright on 2026-11-21, before screenshots. The browser landed on `https://slack.com/intl/en-sg/` (Singapore English). `https://slack.com/` and `https://slack.com/intl/en-us/` both redirected there. The product app was not entered.

Nothing in this file is a private string. No email, phone or location was typed. Cookie banners were hidden, never accepted. No form was submitted.

## How the homepage opens other surfaces

Desktop header at 1440x900. Phone header at 390x844 collapses the same links into a Menu button.

| Control | What it opens |
|---|---|
| Logo | `/` (this locale: `/intl/en-sg/`) |
| Product (button) | Mega menu, overlay, not a page. Escape closes it |
| Solutions (button) | Mega menu, overlay |
| Enterprise | `/enterprise` |
| Resources (button) | Mega menu, overlay |
| Pricing | `/pricing` |
| Search (`#nav_search_btn`) | In-header search field, placeholder "Find anything (ie. channels, emoji, or reset password)", plus a Search button. Not submitted |
| Sign in | `https://slack.com/signin` — sign-in wall. Stop |
| Request a demo | `/contact-sales` |
| Get started (header, hero, menus, footer) | `https://slack.com/get-started` or `/intl/en-sg/get-started` — get-started wall. Stop |
| Find your subscription | `/pricing` |
| Change region (footer button) | Dialog "Change region". Region links switch locale. Not followed |
| Cookie banner | OneTrust dialog. Hidden, never accepted or rejected |
| Pause animation / slide dots | Hero carousel states on the same page |
| Phone Menu (`#nav_menu_btn`) | Full-screen nav: Product, Solutions, Enterprise, Resources, Pricing, Request a demo, Get started, Sign in, Close |
| Phone Product / Solutions / Resources | Nested lists of the same mega-menu links |

## Product menu

| Label | Opens |
|---|---|
| Channels | `/features/channels` |
| Slack Connect | `/connect` |
| Meetings & video | `/features/huddles` |
| Canvas | `/features/canvas` |
| Lists | `/features/task-list` |
| Slackbot | `/features/slackbot` |
| Slack Code | `/features/code-channels` |
| Native AI | `/features/ai` |
| Agentforce | `/ai-agents` |
| Apps & integrations | `/integrations` |
| Native CRM | `/crm` |
| Salesforce in Slack | `/features/crm` |
| Enterprise search | `/features/enterprise-search` |
| Agentic platform | `/features/agentic-platform` |
| Workflow Builder | `/features/workflow-automation` |
| Trust & security | `/trust` |
| What's new | `/whats-new` |
| Slack Marketplace | `/marketplace` |
| Watch demo | `/demo` |
| Download Slack | `/downloads` |
| See all features | `/features` |

## Solutions menu

| Label | Opens |
|---|---|
| Frontline | `/enterprise/frontline` |
| Engineering | `/solutions/engineering` |
| IT | `/solutions/information-technology` |
| Customer service | `/solutions/customer-service` |
| Sales | `/solutions/sales` |
| Project management | `/solutions/project-management` |
| Marketing | `/solutions/marketing` |
| Human Resources | `/solutions/human-resources` |
| Security | `/solutions/security` |
| Manufacturing, auto and energy | `/solutions/manufacturing` |
| Technology | `/solutions/technology` |
| Media | `/solutions/media` |
| Small business | `/solutions/small-business` |
| Financial services | `/solutions/financial-services` |
| Retail | `/solutions/retail` |
| Public sector | `/solutions/public-sector` |
| Education | `/solutions/education` |
| Health and life sciences | `/solutions/healthcare` |
| Manage projects | `/solutions/use-cases/efficient-project-management` |
| Client collaboration | `/solutions/use-cases/collaborating-with-external-partners` |
| Run effective meetings | `/solutions/use-cases/running-effective-meetings` |
| Pipeline management | `/solutions/use-cases/manage-sales-pipeline` |
| Internal communications | `/solutions/use-cases/improve-internal-communication` |
| Project tracking | `/solutions/use-cases/project-tracking` |
| Lead management | `/solutions/use-cases/manage-leads` |
| Team productivity | `/solutions/use-cases/boost-team-productivity` |
| Employee onboarding | `/solutions/use-cases/onboard-new-employees` |
| Time tracking | `/solutions/use-cases/time-tracking` |
| Find answers faster | `/solutions/use-cases/find-company-knowledge-faster` |
| Template gallery | `/templates/gallery` |
| See all solutions | `/solutions` |
| Watch demo / Download Slack | `/demo`, `/downloads` |

## Resources menu

| Label | Opens |
|---|---|
| What's new | `/whats-new` |
| Resources library | `/resources` |
| Customer stories | `/customer-stories` |
| Events | `/events` |
| Blog | `/blog` |
| Product tour | `https://slackdemo.com/` (external demo host) |
| Help Centre | `/help` |
| Slack vs Teams | `/compare/slack-vs-teams` |
| Developers | `https://api.slack.com/` then `https://docs.slack.dev/` |
| Slack Community | `/community` |
| Partner programme | `/partners` |
| Partner offers | `/partner-offers` |
| AI era of work | `/resources/why-use-slack/rethinking-email-ai-conversations-work` |

## Footer (same locale)

Why Slack: `/features`, `/features/channels`, `/connect`, `/features/ai`, `/trust`, `/trust/security`, `/enterprise-key-management`, `/accessibility`, `/innovations`, `/changelog`, `https://slack-status.com/`.

Product links also include `/features/clips`, `/features/document-sharing`, `/features/team-chat`, `/features/atlas`, `/integrations`, `/ai-agents`, `/scale`, `/engage-users`, `/compare/slack-vs-email`, `/compare/slack-vs-teams`.

Solutions repeats the department and industry pages above, plus `/solutions/task-management` and `/solutions/distance-learning`.

Resources: `/resources`, `/help`, `/customer-stories`, `/events`, `/blog`, `/community`, `/partners`, `/partner-offers`, `/marketplace`, `https://api.slack.com/`.

Company: `/about`, `/blog/news`, `/media-kit`, `https://brand.slackhq.com/`, `/careers`, `/legal`, `/trust/privacy/privacy-policy`.

Other hosts named in the footer, not captured as the product UI: `slack.design`, `slack.engineering`, `slackcertified.com`, Salesforce store and privacy pages, social profiles.

## Auth walls (stop)

These loaded in headed Chrome. Headless Chromium got HTTP 403 "browser is not supported" on the same URLs. No field was filled. Google, Apple and Microsoft were not clicked. No code was requested.

| Control | URL that loaded | What stopped the branch |
|---|---|---|
| Sign in | `https://slack.com/signin#/signin` | "Enter your email to sign in", email field, Sign In With Email, Google, Apple, workspace-URL link |
| Get started, Create an account | `https://slack.com/get-started#/createnew` and `https://app.slack.com/get-started#/createnew` | "First, enter your email", Continue, Google, Apple |
| Known probe | those two get-started URLs, Continue | Prior run: Continue stayed on loading and did not send a code. This run did not press Continue |

`/intl/en-sg/get-started` in headless Chromium showed "This browser is no longer supported" and was not treated as a successful wall.

## Capture set

Representative public pages, both widths, plus the menus, search, region dialog, phone menu, and the two walls (screenshot only, no submit):

`/`, `/pricing`, `/features`, `/enterprise`, `/solutions`, `/resources`, `/customer-stories`, `/blog`, `/help`, `/whats-new`, `/marketplace`, `/trust`, `/demo`, `/downloads` (desktop only; phone returned HTTP 429), `/contact-sales`, `/legal`, `/accessibility`, `/about`, `/templates/gallery`, `/events`, one feature page (`/features/channels`), one solution page (`/solutions/engineering`), `https://slack.design/`, `https://docs.slack.dev/`.

The remaining feature, solution, use-case, blog, story and help article URLs are the same chrome. They are listed above and not each given a full-page capture.

## Not captured

| Surface | Why |
|---|---|
| Signed-in workspace, channels, DMs, settings | Behind the sign-in wall |
| Account creation, email code, SSO | Behind the get-started wall. Google, Apple and Microsoft not clicked |
| Contact-sales and partner forms | Public pages may show fields. Nothing is typed or submitted |
| Cookie consent result | Banner hidden, never posted |
| Dark marketing theme | Not observed on the public pages |
| `slackdemo.com` product tour | External host, not the marketing system |
