# Zendesk public site tree

Mapped 2026-11-21 from [https://www.zendesk.com/](https://www.zendesk.com/) while signed out. The host returns the Singapore marketing site at [https://www.zendesk.com/sg/](https://www.zendesk.com/sg/). The page title is "Transform Customer & Employee Service with AI Agents | Zendesk Singapore". Desktop shots are 1440×900. Phone shots are 390×844 CSS pixels at 2x (780×1688 PNG).

A control that opens a login, signup, demo form, or identity-provider wall stops that branch. Nothing was typed. No form was submitted. No identity provider was clicked. Cookie Accept all, Reject all, and Cookie settings were not pressed.

The OneTrust dialog covers the first paint. Shots of opened states live in [screenshots/site-tree/](screenshots/site-tree/). Desktop menus did not open from a pointer hover in this pass (the cookie dialog intercepts the pointer, and a script click left `aria-expanded` false). The panels are in the DOM. The desktop menu shots set `aria-expanded` and, where the stylesheet still kept the panel at `display: none`, forced that panel visible so the links could be photographed. The phone drawer opened from a real tap on "Toggle mobile menu".

## Promo strip

A black bar sits above the header on a fresh visit.

| Control | Kind | Opens |
|---|---|---|
| CX Trends 2027 | Text | Not a link |
| Download now | Link | https://www.zendesk.com/au/cxtrends/ (campaign query stripped in the sidecar) |
| Close | Button | Dismisses the bar. Not pressed. |

On the login page the same bar reads "AI Masterclass 2026" and "Watch now", which leaves the marketing host for a virtual-events page. Not followed.

## Secondary bar

Present above the primary menu at 1440. Hidden at 390 until the drawer opens.

| Control | Kind | Opens |
|---|---|---|
| Sign in | Link | https://www.zendesk.com/sg/login/ wall. Stopped. | [desktop](screenshots/login-light-default.png), [phone](screenshots/mobile-login-light-default.png) |
| Contact us | Link | https://www.zendesk.com/sg/contact/ form. Stopped. Not submitted. | [desktop](screenshots/contact-light-default.png) |
| Language | Menuitem | Locale list. Escape is the close path on a real hover. Shot forced open. | [desktop](screenshots/site-tree/desktop-menu-language.png) |

## Primary menu

Present on the homepage. Platform, Products, Solutions, and Resources are menuitems (`aria-haspopup`, `aria-controls` ending in `-menu`). Pricing is a link. At 390 the same items sit in a drawer opened by "Toggle mobile menu".

| Control | Kind | Opens | Shot |
|---|---|---|---|
| Wordmark | Link | https://www.zendesk.com/sg/ | |
| Platform | Menuitem | Mega-menu, listed below | [desktop](screenshots/site-tree/desktop-menu-platform.png), [phone](screenshots/site-tree/phone-nav-platform.png) |
| Products | Menuitem | Mega-menu, listed below | [desktop](screenshots/site-tree/desktop-menu-products.png) |
| Solutions | Menuitem | Mega-menu, listed below | [desktop](screenshots/site-tree/desktop-menu-solutions.png) |
| Resources | Menuitem | Mega-menu, listed below | [desktop](screenshots/site-tree/desktop-menu-resources.png) |
| Pricing | Link | https://www.zendesk.com/sg/pricing/ | [desktop](screenshots/pricing-light-default.png), [phone](screenshots/mobile-pricing-light-default.png) |
| Try it for free | Link | https://www.zendesk.com/sg/register/ wall. Stopped. | |
| View demo | Link | https://www.zendesk.com/sg/demo/ wall. Stopped. | [desktop](screenshots/demo-light-default.png) |

Phone: the header collapses to the wordmark, View demo, and "Toggle mobile menu". The drawer lists Platform, Products, Solutions, Resources, Pricing, Sign in, and Language, plus View demo and Contact us. Shot: [phone-nav-drawer.png](screenshots/site-tree/phone-nav-drawer.png).

## Platform menu

| Label | Opens |
|---|---|
| Zendesk Resolution Platform | https://www.zendesk.com/sg/platform/ | [desktop](screenshots/platform-light-default.png) |
| Zendesk AI | https://www.zendesk.com/sg/service/ai/ |
| Zendesk Bridge | https://www.zendesk.com/sg/service/ai/ai-agents/zendesk-bridge/ |
| Reporting and analytics | https://www.zendesk.com/sg/service/analytics/ |
| Marketplace | https://www.zendesk.com/sg/marketplace/ |
| Actions and integrations | https://www.zendesk.com/sg/service/ai/ai-agents/any-platform/ |
| Security and trust | https://www.zendesk.com/sg/trust-center/ |

## Products menu

| Label | Opens |
|---|---|
| Customer Service | https://www.zendesk.com/sg/service/ | [desktop](screenshots/service-light-default.png) |
| Employee Service | https://www.zendesk.com/sg/employee-service/ |
| Contact Centre | https://www.zendesk.com/sg/service/contact-center/ |
| AI agents | https://www.zendesk.com/sg/service/ai/ai-agents/ | [desktop](screenshots/ai-agents-light-default.png) |
| Copilot | https://www.zendesk.com/sg/service/ai/copilot/ |
| Quality assurance | https://www.zendesk.com/sg/service/quality-assurance/ |
| Workforce Management | https://www.zendesk.com/sg/service/workforce-management/ |

## Solutions menu

Two groups: Common use cases, and By business type.

| Group | Label | Opens |
|---|---|---|
| Common use cases | Messaging and live chat | https://www.zendesk.com/sg/service/messaging/ |
| Common use cases | Ticketing | https://www.zendesk.com/sg/service/ticketing-system/ |
| Common use cases | IT service management | https://www.zendesk.com/sg/employee-service/itsm/ |
| Common use cases | Knowledge base | https://www.zendesk.com/sg/service/knowledge/ |
| Common use cases | Voice | https://www.zendesk.com/sg/service/voice/ |
| By business type | Startups | https://www.zendesk.com/sg/business/startups/ |
| By business type | Retail | https://www.zendesk.com/sg/industries/retail/ |
| By business type | Financial services | https://www.zendesk.com/sg/industries/financial-services/ |
| By business type | Technology | https://www.zendesk.com/sg/industries/technology/ |
| By business type | Media & Entertainment | https://www.zendesk.com/sg/industries/media/ |
| By business type | View all business types | https://www.zendesk.com/sg/industries/ |

## Resources menu

Four groups: Learn, Support, Company, and a Latest news promo.

| Group | Label | Opens |
|---|---|---|
| Learn | Customer stories | https://www.zendesk.com/sg/customer/ |
| Learn | Blog | https://www.zendesk.com/sg/blog/ |
| Learn | Events | https://www.zendesk.com/sg/company/events/ |
| Learn | CX Trends | https://www.zendesk.com/sg/cxtrends/ |
| Support | Help centre | https://support.zendesk.com/hc/en-us/ | [desktop](screenshots/help-light-default.png) |
| Support | Community | https://www.zendesk.com/sg/programs/zendesk-community/ |
| Support | Partners | https://www.zendesk.com/sg/partner/ |
| Support | What's new | https://support.zendesk.com/hc/en-us/sections/4405298877338-What-s-New-in-Zendesk/ |
| Company | About us | https://www.zendesk.com/sg/company/ |
| Company | Why Zendesk | https://www.zendesk.com/sg/why-zendesk/ |
| Company | Newsroom | https://www.zendesk.com/sg/newsroom/ |
| Company | Careers | https://www.zendesk.com/sg/company/careers/ |
| Latest news | Watch now | https://www.zendesk.com/au/company/events/ai-summit-2026/ (leaves the /sg/ tree) |

## Language menu

Opened by the Language menuitem. Each row is a locale home. English (Singapore) is the current host.

| Label | Opens |
|---|---|
| English (US) | https://www.zendesk.com/ |
| English (UK) | https://www.zendesk.co.uk/ |
| Español | https://www.zendesk.es/ |
| Español (LATAM) | https://www.zendesk.com.mx/ |
| Português | https://www.zendesk.com.br/ |
| Français | https://www.zendesk.fr/ |
| Deutsch | https://www.zendesk.de/ |
| Italiano | https://www.zendesk.com/it/ |
| Nederlands | https://www.zendesk.nl/ |
| English (Denmark) | https://www.zendesk.com/dk/ |
| English (Sweden) | https://www.zendesk.com/se/ |
| English (Australia) | https://www.zendesk.com/au/ |
| English (India) | https://www.zendesk.com/in/ |
| English (Singapore) | https://www.zendesk.com/sg/ |
| 日本語 | https://www.zendesk.co.jp/ |
| 한국어 | https://www.zendesk.kr/ |
| 繁體中文 (台灣) | https://www.zendesk.tw/ |
| 繁體中文 (香港特區) | https://www.zendesk.hk/ |

## Homepage body

Controls that are not the header or the footer. "Try it for free" and the hero email stop at the trial wall. The email was not typed. "View demo" and "Watch now" stop at a demo or events wall.

| Control | Kind | Opens |
|---|---|---|
| Enter work email | Field | Empty. Not typed. |
| Try it for free | Button | Trial wall. Not submitted. |
| Zendesk Privacy Notice | Link | https://www.zendesk.com/sg/company/agreements-and-terms/privacy-notice/ |
| Explore Zendesk Bridge | Link | https://www.zendesk.com/sg/service/ai/ai-agents/zendesk-bridge/ |
| Explore Specialized AI agents | Link | https://www.zendesk.com/sg/service/ai/ai-agents/specialized-agents/ |
| Explore Agentic Analytics | Link | https://www.zendesk.com/sg/service/analytics/ |
| Explore the platform | Link | https://www.zendesk.com/sg/platform/ |
| Watch now | Link | AI summit events page. Stopped. |

## Cookie dialog

Opened by the site on first visit. Dialog id `onetrust-banner-sdk`. Title is the cookie notice. None of the buttons were pressed.

| Control | Kind | Opens |
|---|---|---|
| Accept all | Button | Consent. Not pressed. |
| Reject all | Button | Consent. Not pressed. |
| Cookie settings | Button | Preference center. Not pressed. |
| Cookie Notice | Link | https://www.zendesk.com/sg/company/agreements-and-terms/cookie-notice/ |

Shot: [desktop-cookie-dialog.png](screenshots/site-tree/desktop-cookie-dialog.png). The homepage copy is [home-light-cookie.png](screenshots/home-light-cookie.png).

## Footer

Dark band under the page. Shot: [desktop-footer.png](screenshots/site-tree/desktop-footer.png). Columns repeat product, audience, and company links, plus Compare (Zendesk vs. Intercom, Salesforce, Freshdesk) and a software-keyword column. "How can we help? Contact us" goes to the contact form. Social marks for X, Facebook, LinkedIn, YouTube, Instagram, and TikTok leave the site. The legal row is Terms of use, Privacy notice, Cookie notice, Cookie settings, Trust Centre, and the copyright line.

## Walls

Sign in asks for a subdomain and stops. The field was empty and was not typed. Sign in, Forgot your subdomain, and the Chat, Sell, and Sunshine Conversations links were not followed. Try it for free and View demo open a first step and stop. The register page paints a sample agent workspace behind the trial dialog, with placeholder names. That shot was discarded and is not in this package. Contact us is an empty sales form. It was not submitted. The public sales phone on that page is Zendesk's published number.

A missing path returns the older 404 template. Shot: [notfound-light-default.png](screenshots/notfound-light-default.png). That template is not the current marketing system.
