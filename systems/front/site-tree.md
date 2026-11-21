# Front public site tree

Walked signed out on 2026-11-21 from [https://front.com/](https://front.com/) (HTTP 200). [https://www.front.com/](https://www.front.com/) redirects to that origin. Desktop viewport 1440. Phone viewport 390. OneTrust and cookielaw requests were blocked. The consent banner was hidden, not accepted. No locale switch was found. The marketing site has no page-level theme switch. Section themes alternate on one page.

Opened means the control was used and the result was photographed or the destination loaded. Linked means the href was read and the page was not opened in this pass. A prior capture (2026-11-16) already has screenshots for many of those destinations. This file records this pass.

## Header, desktop

The logo links to `/`. Pricing links to `/pricing` and was opened. Sign in links to `https://app.frontapp.com/signin` (query string stripped) and was opened. See the login wall below.

Hover keeps the URL on `/` and opens a mega menu.

Product, photographed in [home-light-menu-product.png](screenshots/home-light-menu-product.png):

| Control | Opens |
|---|---|
| See Front in Action | `/product-tour` |
| Platform Overview | `/product` |
| Recent Product Updates | `/whats-new` |
| Customer Service | `/customer-service` |
| Email Management | `/email-management` |
| Client Communication | `/client-communication` |
| Autopilot | `/product/autopilot-customer-service-automation` |
| Copilot | `/product/copilot-ai-assistant` |
| Compass | `/product/compass-AI-agent-performance-monitoring` |
| External Agents | `/product/external-agents-bring-your-own-agent` |
| Omnichannel | `/product/omnichannel-support-inbox` |
| Ticketing | `/product/ticketing-system` |
| Resolve | `/product/resolve-self-serve-ai-support` |
| Knowledge Base | `/product/knowledge-base` |
| Integrations & API | `/product/integrations-api` |

Solutions, photographed in [home-light-menu-solutions.png](screenshots/home-light-menu-solutions.png). Headings: Industries, Teams.

| Control | Opens |
|---|---|
| Tech | `/industries/b2b-tech` |
| Financial Services | `/industries/financial-services` |
| Logistics | `/industries/logistics` |
| Manufacturing | `/industries/manufacturing` |
| Professional Services | `/industries/professional-services` |
| Travel | `/industries/travel` |
| Customer Support | `/teams/customer-service-support` |
| Operations | `/teams/operations` |
| Inbound Sales | `/teams/inbound-sales` |
| Account Management | `/teams/account-management` |
| Customer Success | `/teams/customer-success` |

Resources, photographed in [home-light-menu-resources.png](screenshots/home-light-menu-resources.png):

| Control | Opens |
|---|---|
| Academy | `https://academy.front.com/app` |
| Community | `https://community.front.com/` |
| Help Center | `https://help.front.com/` |
| Developer Portal | `https://dev.frontapp.com/docs/welcome` |
| Blog | `/blog` |
| Integrations | `/integrations` |
| Guides & Webinars | `/resources` |
| Security | `/security` |
| Customer Stories | `/customer-stories` |
| Download App | `/download` |
| Front's Support Report | `/support-report` |
| Channel Partnerships | `/partners/channel` |
| Promo card | `https://front.registration.goldcast.io/series/f7a5a6e2-a125-4eff-90cc-ea68f93122c3` |

Request a demo is a button. It opens a dialog on `https://front.com/`, photographed empty in [home-light-demo-dialog.png](screenshots/home-light-demo-dialog.png). Fields seen and left empty: Work email, Full name, Phone number (country-code control, nothing typed), Company size, Job title, What are you looking to improve?, Submit. Stopped. Not typed. Not submitted.

Try for free is a button with no href. It opens a dialog titled "Try Front for free" on `https://front.com/`, photographed empty in [home-light-try-dialog.png](screenshots/home-light-try-dialog.png). Fields seen and left empty: Work email, First name, Last name, Company, Job title, Industry (select, "Select one"), Phone number (country-code control, nothing typed), Company size (select, "Select one"), Submit. Legal links in the dialog: General Terms, AI Supplemental Terms, Privacy Notice. Stopped. Not typed. Not submitted. This is a trial form on the marketing site, not the app sign-in wall.

## Header, phone (390)

Open menu (`button-mobile-menu-trigger`) opens a drawer. Photographed collapsed in [mobile-home-light-menu.png](screenshots/mobile-home-light-menu.png): Product, Solutions, Resources, Pricing, Sign in, Request a demo, Try for free, Close menu.

Product chevron opened the section. Photographed in [mobile-home-light-menu-product.png](screenshots/mobile-home-light-menu-product.png). Visible groups: Use Cases (Customer Service, Email Management, Client Communication), AI Platform (Autopilot, Copilot, Compass, External Agents), More Features (Omnichannel, Ticketing, Resolve, Knowledge Base, Integrations & API). Same paths as the desktop Product menu. None of those links were followed from the drawer.

Solutions chevron opened the section and collapsed Product. Photographed in [mobile-home-light-menu-solutions.png](screenshots/mobile-home-light-menu-solutions.png). Visible: Industries (Tech, Financial Services, Logistics, Manufacturing, Professional Services, Travel) and Teams (Customer Support, Operations, Inbound Sales, Account Management, Customer Success). Same paths as the desktop Solutions menu. None followed from the drawer.

The Resources phone section was not opened. Close menu was visible and not used as a separate shot.

## Homepage body

URL stays `/` unless noted. Photographed in [home-light-default.png](screenshots/home-light-default.png) and [mobile-home-light-default.png](screenshots/mobile-home-light-default.png).

Hellobar "Read it now" links to `/blog/ai-agents-teammates-launch`. Not followed this pass.

Feature buttons swap an in-page panel. No `aria-pressed`, `aria-expanded`, or `aria-selected`. URL stays `/`.

| Control | Result |
|---|---|
| Run complex work | in-page panel |
| Collaborate effortlessly | in-page panel |
| Power all your agents | in-page panel |
| Get full visibility | in-page panel |
| Stay in control | in-page panel, photographed in [home-light-feature-stay-in-control.png](screenshots/home-light-feature-stay-in-control.png) |

The first Explore more navigates to `https://front.com/teams/customer-service-support`. Five more Explore more buttons and Explore integrations were visible and not followed. Their destinations are not claimed.

Play did not open a dialog. Vendor iframes (Optimizely, DoubleClick, Qualified) were present. Not treated as a video dialog. The Qualified widget was hidden in this pass.

Homepage search: none. The only search field in the DOM was the hidden OneTrust cookie search.

No carousel control was opened. No theme switch. No locale switch.

## Pricing

`/pricing` loaded HTTP 200. Photographed in [pricing-light-default.png](screenshots/pricing-light-default.png).

Billing is a checkbox (id `22`), label "Billed Annually", default checked, with "SAVE 24%" when annual. Clicking it is a local toggle, not a form submit. Annual prices photographed in [pricing-light-billing.png](screenshots/pricing-light-billing.png): Starter $25 /seat/mo, Professional $65 /seat/mo, Enterprise $105 /seat/mo (MOST POPULAR). After uncheck, photographed in [pricing-light-billing-monthly.png](screenshots/pricing-light-billing-monthly.png): Starter $35 /seat/mo, Professional $85 /seat/mo, Enterprise "Only available on annual".

FAQ accordion: "How does Front's free trial work? Do I need a credit card?" was opened. Photographed in [pricing-light-faq.png](screenshots/pricing-light-faq.png). The answer describes a 14-day Professional trial and no card. Other FAQ titles were visible and not opened: seat, channel, channel maximum, AI providers, data processing, security, combining seats, bank payment, Success Services packages.

Plan CTAs on the cards (Try for Free, Request a Demo, Talk to sales) were not followed from this page. The header Request a demo and Try for free dialogs above are the ones that were opened.

## Integrations

`/integrations` loaded HTTP 200. Photographed in [integrations-light-default.png](screenshots/integrations-light-default.png).

Search placeholder "Search for an app..." was focused and not typed. Photographed in [integrations-light-search-focus.png](screenshots/integrations-light-search-focus.png).

Categories opens a filter panel. Photographed in [integrations-light-categories.png](screenshots/integrations-light-categories.png). Visible unchecked checkboxes: Bots & Workflow Automation, Voice & Telephony, Project Management & Issue Tracking. The rest of the list was below the fold and was not recorded. No checkbox was applied.

Explore + and Plans + were not opened. See all, Show all integrations, and Get started were linked and not followed.

## Customer stories

`/customer-stories` loaded HTTP 200. Search placeholder "Search by customer or phrase" was not typed.

Industry, Company size, and Topic were expanded by default. Labels seen: Industry (Education, Financial Services, Healthcare, Logistics, Manufacturing, Media), Company size (1-50, 51-200, 201-500, 501-1,000, 1,001-5,000, 5,000+), Topic (Boost Employee Satisfaction, Email Management, Improve Operational Efficiency, Increase Revenue, Shared Inbox). Checkboxes were left unchecked. "82 customer stories" and Show all on Industry were visible. Show all was not clicked.

Sort opens Most recent (default) and Alphabetical. Photographed in [customer-stories-light-sort.png](screenshots/customer-stories-light-sort.png). Alphabetical was not applied.

## Resources

`/resources` loaded HTTP 200. Types + opened a filter list. Photographed in [resources-light-types.png](screenshots/resources-light-types.png): Awards, Ebooks, Events, Guides, Regional Events, Reports, Research. None applied.

Teams +, Topics +, Industries +, and Show more (120) were visible and not opened.

## Jobs

`/jobs` loaded HTTP 200. Photographed in [jobs-light-default.png](screenshots/jobs-light-default.png).

"See our open positions" is a button. It scrolls on the same URL. It does not navigate. The hero is [jobs-light-default.png](screenshots/jobs-light-default.png).

Two selects sit above the listings: location (default "All locations") and department (default "All departments"). Neither was changed. The listings show published place names, so that frame was not committed. Option labels that name a place are omitted here.

## What's new

`/whats-new` loaded HTTP 200. Watch video is an external video link. The click did not open a dialog and the URL stayed `https://front.com/whats-new`. Photographed in [whats-new-light-watch.png](screenshots/whats-new-light-watch.png). The external id is not recorded.

## Footer

Collected from the homepage. 62 links. Not opened in this pass unless a row above already says opened. Headings include AI PLATFORM, USE CASES, and COMPARE. The heading dump also listed link labels as if they were headings. The table below is the link list.

| Label | Href |
|---|---|
| Front AI Overview | `/product/ai` |
| Autopilot | `/product/autopilot-customer-service-automation` |
| Copilot | `/product/copilot-ai-assistant` |
| External Agents | `/product/external-agents-bring-your-own-agent` |
| Compass | `/product/compass-AI-agent-performance-monitoring` |
| Smart QA | `/product/smart-qa-automated-quality-assurance` |
| Smart CSAT | `/product/smart-csat-ai-scoring` |
| Customer Service | `/customer-service` |
| Email Management | `/email-management` |
| Client Communication | `/client-communication` |
| Front vs. Zendesk | `/compare/front-vs-zendesk` |
| Front vs. Freshdesk | `/compare/front-vs-freshdesk` |
| Front vs. Intercom | `/compare/front-vs-intercom` |
| Front vs. Help Scout | `/compare/front-vs-help-scout` |
| Front vs. Salesforce | `/compare/front-vs-sfdc` |
| Front vs. Hiver | `/compare/front-vs-hiver` |
| Front vs. Missive | `/compare/front-vs-missive` |
| Front vs. Pylon | `/compare/front-vs-pylon` |
| About | `/about` |
| Careers | `/jobs` (page opened from the tree, not from this footer link) |
| Press Kit | `/about#front-media-assets` |
| Real-Time Metrics | `/support-report` |
| Become a Partner | `/partners/integration` |
| Customer Referral | `/customer-referral` |
| Contact Support | `https://help.front.com/en/contact-us` |
| Legal | `/legal` |
| Front Overview | `/product` |
| Help Desk | `/teams/customer-service-support` |
| Shared Inbox | `/product/omnichannel-support-inbox` |
| Ticketing | `/product/ticketing-system` |
| Knowledge base | `/product/knowledge-base` |
| Resolve | `/product/resolve-self-serve-ai-support` |
| Integrations & API | `/product/integrations-api` |
| Pricing | `/pricing` |
| Product Updates | `https://community.front.com/product-updates` |
| Download App | `/download` |
| Blog | `/blog` |
| Customer Stories | `/customer-stories` |
| The Coordination Tax | `https://research.front.com` |
| Help | `https://help.front.com/` |
| Academy | `https://academy.front.com/app` |
| Developers | `https://dev.frontapp.com/docs/welcome` |
| Integrations | `/integrations` |
| Glossary | `/glossary` |
| The State of Service Expectations | `/resources/state-of-service-expectations` |
| Customer Support Metrics Library | `/guides/top-customer-service-metrics` |
| Guide to 100% CSAT | `/blog/improve-csat` |
| Boost Agent Support Productivity | `/blog/customer-service-automation-ai` |
| Front's New AI Capabilities | `/blog/customer-service-agent-assistance-ai` |
| AI vs. Human Support Strategy | `/resources/ai-vs-human-why-you-dont-have-to-choose` |
| 5 Best Practices for Self-Service Support | `/resources/how-to-scale-delightful-customer-experiences-with-self-service-support` |
| Create AI-Friendly Help Center Articles | `/resources/creating-ai-friendly-help-center-articles` |
| Top Tips for Knowledge Base Articles | `/blog/how-to-write-knowledge-base-articles` |
| Support Message Templates | `/resources/5-tried-and-true-message-templates-to-improve-your-support-teams-csat` |
| Shared Inbox Management Tips | `/guides/shared-inbox-management` |
| Front Reviews | `/reviews` |
| Front AI Information | `/guides/ai-information` |
| SaaS Service Agreement | `/legal/saas-services-agreement` |
| Privacy Notice | `/legal/privacy-notice` |
| Cookie Policy | `/legal/cookie-policy` |
| Google User Data Privacy Notice | `/legal/front-products-and-services-privacy-notice` |
| Status | `https://www.frontstatus.com/` |

Social icon hrefs were not collected in this pass.

## Login and signup walls

Sign in in the header opens `https://app.frontapp.com/signin` (HTTP 200). Empty form photographed and the branch stopped. See [login-review.json](login-review.json).

| Shot | Theme | Width |
|---|---|---|
| [signin-light-empty.png](screenshots/signin-light-empty.png) | light (`data-theme=light`) | 1440 |
| [signin-dark-empty.png](screenshots/signin-dark-empty.png) | dark (`data-theme=dark`, `front-theme-preference=dark` before navigation) | 1440 |
| [mobile-signin-light-empty.png](screenshots/mobile-signin-light-empty.png) | light | 390 |
| [mobile-signin-dark-empty.png](screenshots/mobile-signin-dark-empty.png) | dark | 390 |

Wall offers: Email address, Password, Sign in, Forgot password?, Try for Free, Google, Office 365, SAML SSO, Privacy Notice, Google User Data Privacy Notice. Nothing was typed. No identity provider was clicked. Try for Free on this wall was not followed. Forgot password? was not followed.

## Not opened this pass

- Phone Resources drawer section.
- Integrations Explore + and Plans +.
- Customer-story filter apply, resources filter apply, jobs select change.
- Remaining homepage Explore more buttons and Explore integrations.
- Remaining pricing FAQ rows and plan-card CTAs.
- Watch video player (click did not open a dialog).
- Academy, Community, Help Center, Developer Portal, and the Goldcast registration card, from the Resources menu.
- Footer destinations not already named as opened above.
- Any signed-in workspace. Nav, settings, and create inside the app were not entered.
