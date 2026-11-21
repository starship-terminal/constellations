# Dock public site tree

Walked signed out on 2026-11-21 from [https://dock.us](https://dock.us), which redirects to [https://www.dock.us/](https://www.dock.us/) (title: Dock | AI Revenue Enablement that Sellers & Buyers Love). Written from the homepage before screenshots. Desktop viewport requested at 1440. Phone viewport requested at 390. One light theme. No page-level theme switch. The header and footer are custom elements (`dock-site-header`, `dock-site-footer`) with closed-looking shadow roots. Query strings are stripped. The footer support control is a mailto link. The address is not copied into this file.

Opened means the control was used and the destination loaded, or the in-page result was photographed. Linked means the href was read and the page was not opened in this pass. Wall means the destination is a login, signup, or identity-provider page. Those branches stop. No password, email, or code was typed. Google, Apple, and any identity provider were not clicked. No form was submitted. No captcha was solved.

## Header, desktop

The bar lives in `dock-site-header`. Logo (`a`, accessible name "Dock home") links to `/`. Skip to content links to `#main`.

Product and Resources are `summary.nav-trigger` controls with no href. Each opens a mega-menu on `/`. Pricing, Customers, and Log in are direct links.

| Control | Opens |
|---|---|
| Product | Mega-menu on `/`. Groups below. |
| Product / Sales / Sales Deal Rooms | `/solutions/sales` |
| Product / Sales / Sales Order Forms | `/product/order-forms` |
| Product / Customer success / Customer Onboarding | `/solutions/customer-onboarding` |
| Product / Customer success / Client Portals | `/solutions/client-portal` |
| Product / Content / Content Management | `/product/content-management` |
| Product / Content / Slides | `/product/slides` |
| Product / Learning / Learning Management | `/product/learning-management` |
| Product / Learning / Playbooks | `/product/learning-playbooks` |
| Product / Learning / Roleplay | `/product/ai-roleplay` |
| Product / Learning / Tutors | `/product/ai-tutor` |
| Product / AI / Dock AI | `/product/dock-ai` |
| Product / AI / AI Agents | `/product/ai-enablement-agent` |
| Product / AI / Buyer AI Chat | `/features/ai-chat` |
| Product / AI / Dock MCP | `/features/dock-mcp` |
| Product / Integrations / Salesforce | `/features/salesforce` |
| Product / Integrations / HubSpot | `/features/hubspot` |
| Product / Integrations / Chrome Extension | `/features/chrome-extension` |
| Product / Integrations / API | `https://developers.dock.us/introduction`. Opens in a new tab. Linked. |
| Product / Integrations / All integrations | `/product/integrations` |
| Pricing | `/pricing` |
| Customers | `/customers` |
| Resources | Mega-menu on `/`. Groups below. |
| Resources / Dock / Product Updates | `/product-updates` |
| Resources / Dock / Templates | `/templates` |
| Resources / Grow & Tell / Podcast | `/grow-and-tell` |
| Resources / Grow & Tell / Newsletter | `/category/grow-and-tell` |
| Resources / Learn / The Revenue Lab Blog | `/library` |
| Resources / Learn / Webinars & Events | `/events` |
| Resources / Learn / The Revenue Archives | `/revenue-archives` |
| Resources / Topics / Sales | `/category/sales` |
| Resources / Topics / Customer Success | `/category/customer-success` |
| Resources / Topics / Marketing | `/category/marketing` |
| Resources / Topics / Enablement | `/category/sales-enablement` |
| Log in | `https://auth.dock.us/login`. Wall. Branch stopped. |
| Request demo | `/demo` |
| Start for free | `https://auth.dock.us/sign-up`. Wall. Branch stopped. |

No locale switch. No theme switch. No search field in the header.

## Header, phone (390)

The bar collapses to the logo and a Menu button (`button.navigation-toggle`, accessible name "Menu"). The same Product and Resources groups are `summary.menu-group-toggle` rows inside the drawer. Log in, Request demo, and Start for free sit in the drawer and point at the same destinations. Start for free and Log in were not followed from the phone.

## Homepage body

URL stays `/` unless noted.

| Control | Result |
|---|---|
| Request demo | `/demo` |
| Start for free | `https://auth.dock.us/sign-up`. Wall. Not followed from the body. |
| Train, Organize, Collaborate | Buttons. No href. They switch the hero product demo on `/`. |
| Intro, Meet Acme, Next steps | Anchors to `#overview-intro`, `#overview-meet-acme`, `#overview-next-steps`. URL stays `/`. |
| Publish changes | Button inside the product demo. Not pressed. A press can start a demo action. |
| Sales Training, Content Library, Sales Room, Roleplay, Presentations, Agents | Buttons. They switch the "Meet Dock" panel on `/`. |
| Show Sales Training, Show Content Library, Show Sales Room, Show Roleplay, Show Presentations, Show Agents | Buttons. Same panel switch. |
| Lattice +25% win rate | `/library/customer-story-lattice` |
| BrightHire +22% deals closed | `/library/customer-story-brighthire` |
| Nectar +31% close rate | `/library/customer-story-nectar` |
| Explore learning management, Learn more about Pathways | `/product/learning-management` |
| Explore content management, Learn more about Keep content in one place | `/product/content-management` |
| Explore sales rooms, Learn more about Repeat what works | `/solutions/sales` |
| Explore Dock AI | `/product/dock-ai` |
| Play testimonial (Ingrid Murra, Andrew Hollis, Stephen Ruff, Victoria Bush, Noah Massucci, Rachel Jennings-Keane, Bill Tillman, Seth Kramer, Brittany Soinski, Todd Busler, Jules Aldag, Joyce Golden) | `https://dock-3.wistia.com/medias/<id>`. Linked. Not opened. |
| Copy prompt | Button. Copies a prompt chip. Not pressed. |
| Build a sales room for my next deal, Find the best content for my buyer, Turn deal activity into next steps | Buttons. Prompt chips. Not pressed. Nothing was submitted. |
| All Dock love, Sales, Enablement, Customer Success, GTM teams, Reps, Your customers, More love | Buttons. They filter the love wall on `/`. |
| View all stories | In-page control. URL stays `/` unless a later click follows a story link. |
| Close video | Button. Closes an in-page video. Not pressed. |
| Request Demo (pre-footer) | `/demo` |

No homepage search. No form on `/`.

## Footer

The footer lives in `dock-site-footer`. Columns: Revenue Enablement, Customer Success, Sales, AI & Integrations, Templates, Resources, General, Support, Terms & Privacy. Tagline: Build high-performing sales teams. Badges: SOC 2 TYPE II, GDPR, CCPA. Copyright: 2026 Dock Labs, Inc.

| Control | Opens |
|---|---|
| Sales Enablement | `/solutions/sales-enablement` |
| Sales Content Management | `/product/content-management` |
| Learning Management | `/product/learning-management` |
| Learning Playbooks | `/product/learning-playbooks` |
| AI Enablement Agent | `/product/ai-enablement-agent` |
| AI Documents | `/product/ai-documents` |
| Customer Onboarding | `/solutions/customer-onboarding` |
| Client Portals | `/solutions/client-portal` |
| White-Label Client Portals | `/solutions/white-label-client-portal` |
| Client Project Plans | `/product/project-plans` |
| Client Project Management | `/solutions/project-management-client-portal` |
| Sales Rooms | `/solutions/sales` |
| Mutual Action Plans | `/features/mutual-action-plan` |
| Sales Portals | `/solutions/sales-portal` |
| Price Quotes & Order Forms | `/product/order-forms` |
| Buyer Enablement | `/solutions/buyer-enablement` |
| Dock AI | `/product/dock-ai` |
| Buyer AI Chat | `/features/ai-chat` |
| Dock MCP | `/features/dock-mcp` |
| Integrations | `/product/integrations` |
| HubSpot | `/features/hubspot` |
| Salesforce | `/features/salesforce` |
| Chrome Extension | `/features/chrome-extension` |
| Sales Room Template | `/templates/digital-sales-room` |
| Customer Onboarding Plan | `/templates/customer-onboarding` |
| Client Portal Template | `/templates/client-portal-template` |
| Mutual Action Plan | `/templates/mutual-action-plan` |
| Pricing Proposal Template | `/templates/pricing-proposal-template` |
| Implementation Plan | `/templates/implementation-plan` |
| Dock Templates | `/templates` |
| Product Updates | `/product-updates` |
| Webinars & Events | `/events` |
| Sales Collateral Examples | `/revenue-archives` |
| Blog | `/library` |
| Newsletter | `/category/grow-and-tell` |
| Podcast | `/grow-and-tell` |
| About Us | `/about-us` |
| Case Studies | `/customers` |
| Careers | `https://dock.rippling-ats.com/`. Linked. Not opened. |
| Request Demo | `/demo` |
| LinkedIn | `https://www.linkedin.com/company/dock-us/`. Linked. |
| YouTube | `https://www.youtube.com/@dock_us`. Linked. |
| Help Center | `https://help.dock.us/`. Linked. |
| API Documentation | `https://developers.dock.us/api-reference/introduction`. Linked. |
| Status | `https://status.dock.us/`. Linked. |
| Support mail | A mailto link in the Support column. Linked. Not opened. The address is not recorded. |
| Trust Center | `https://app.vanta.com/dock.us/trust/qb4850pc9t0glmc1df43q`. Linked. The trust path token is not copied into a screenshot. |
| Privacy Policy | `/legal/privacy` |
| Terms of Service | `/legal/terms` |

## Public pages opened from the tree

Each loaded signed out on 2026-11-21 in headless Chromium. Desktop viewport 1440×900. Phone viewport 390×844. Screenshot names are in [login-review.json](login-review.json).

| Path | Result |
|---|---|
| `/` | HTTP 200. Product menu and Resources menu opened in place. Phone Menu opened in place. |
| `/pricing` | HTTP 200. Plan CTAs that point at signup were not followed. |
| `/customers` | HTTP 200. |
| `/library` | HTTP 200. Post links were linked, not opened one by one. |
| `/templates` | HTTP 200. |
| `/product/dock-ai` | HTTP 200. |
| `/product/learning-management` | HTTP 200. |
| `/product/content-management` | HTTP 200. |
| `/product/integrations` | HTTP 200. |
| `/solutions/sales` | HTTP 200. |
| `/solutions/client-portal` | HTTP 200. |
| `/product-updates` | HTTP 200. |
| `/events` | HTTP 200. |
| `/about-us` | HTTP 200. Saved as `about-light-2026-11-21.png` because the 2026-11-13 filenames were index-skipped. |
| `/demo` | HTTP 200. Fields left empty. Nothing typed. Submit and the captcha were not used. |
| `/legal/privacy` | HTTP 200. Photographed, then the file was deleted. The page prints a street address. Linked. Not committed. |
| `/legal/terms` | Linked. Not photographed. |

Remaining product, feature, template, and category paths in the tables above were read from the homepage and footer. They were not each photographed. They share the same marketing shell.

## Walls, stopped

`https://auth.dock.us/login` is the destination of Log in. `https://auth.dock.us/sign-up` is the destination of Start for free. Both were opened once from a direct load so the empty wall could be photographed. No email, password, or code was typed. Google, Apple, and any other identity provider were not clicked. No form was submitted. The branch stopped there.

`/demo` is a public request page. Its fields were left empty. Nothing was typed. Submit and any captcha were not used.
