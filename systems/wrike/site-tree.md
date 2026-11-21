# Wrike public site tree

Mapped from https://www.wrike.com/ on 2026-11-21 in headless Chromium at 1440×900, plus the phone header at 390×844. Every control below was seen. A link that opens a public page was followed once to confirm it loads. A control that opens a login or signup wall is recorded and that branch stops. Nothing was submitted. Identity providers were not clicked.

The header menus are full-width panels, not small dropdowns. Opening one hides the hero. Screenshots: [home-light-products-menu.png](screenshots/home-light-products-menu.png), [home-light-solutions-menu.png](screenshots/home-light-solutions-menu.png), [home-light-resources-menu.png](screenshots/home-light-resources-menu.png), [home-light-language.png](screenshots/home-light-language.png), [mobile-home-light-menu.png](screenshots/mobile-home-light-menu.png).

## Top banner

| Control | Opens |
|---|---|
| Read the report | https://www.wrike.com/gartner-report-collaborative-work-management/ |

## Header (desktop)

| Control | Opens |
|---|---|
| Wrike wordmark | https://www.wrike.com/ |
| Products (button, aria-controls `header-desktop-submenu-content-products`) | Products mega menu, below |
| Solutions | Solutions mega menu, below |
| Resources | Resources mega menu, below |
| Pricing | https://www.wrike.com/price/ |
| Enterprise | https://www.wrike.com/enterprise/ |
| Contact Sales | https://www.wrike.com/contact-sales/ (form present; not submitted) |
| EN | Language panel, below |
| Log in | https://login.wrike.com/login/ — auth wall. See [login-review.json](login-review.json). Branch stopped. |
| Try Wrike for free | Trial / signup wall. Not followed. Branch stopped. |

## Products menu

Promo column "Get more with Wrike AI":

| Control | Opens |
|---|---|
| AI overview | https://www.wrike.com/ai/ |
| AI agents | https://www.wrike.com/ai/agents/ |
| Wrike Copilot | https://www.wrike.com/ai/copilot/ |
| AI features | https://www.wrike.com/ai/features/ |

Platform:

| Control | Opens |
|---|---|
| Platform overview | https://www.wrike.com/tour/ |
| Integrations | https://www.wrike.com/apps/ |
| Wrike Work Intelligence | https://www.wrike.com/features/work-intelligence/ |
| Mobile & desktop apps | https://www.wrike.com/apps/mobile-and-desktop/ |
| Security & governance | https://www.wrike.com/security/ |
| Templates | https://www.wrike.com/templates/ |
| Book a demo | https://www.wrike.com/demo/ (video / demo page; form not submitted) |

Features:

| Control | Opens |
|---|---|
| Dashboards | https://www.wrike.com/features/dashboards/ |
| Wrike Whiteboard | https://www.wrike.com/features/whiteboard/ |
| Automation | https://www.wrike.com/features/workflow-automation/ |
| Gantt charts | https://www.wrike.com/features/gantt-chart/ |
| Resource management | https://www.wrike.com/use-cases/resource-management/ |
| Dynamic request forms | https://www.wrike.com/features/custom-request-forms/ |
| See all features | https://www.wrike.com/features/ |

Sticky bar inside the open menu:

| Control | Opens |
|---|---|
| Try Wrike for free | Signup wall. Not followed. |
| Contact Sales | https://www.wrike.com/contact-sales/ |

## Solutions menu

Teams:

| Control | Opens |
|---|---|
| Marketing | https://www.wrike.com/marketing/ |
| Product | https://www.wrike.com/teams/product-management/ |
| PMO | https://www.wrike.com/project-management-office/ |
| Operations | https://www.wrike.com/teams/business-operations/ |
| Creative & design | https://www.wrike.com/teams/creative-project-management/ |
| IT | https://www.wrike.com/teams/it-project-management/ |
| See all teams | https://www.wrike.com/solutions/ with team-solution filter |

Workflows:

| Control | Opens |
|---|---|
| Project management | https://www.wrike.com/use-cases/project-management/ |
| Campaign management | https://www.wrike.com/use-cases/campaign-management/ |
| Client service delivery | https://www.wrike.com/use-cases/client-management/ |
| Project portfolio management | https://www.wrike.com/use-cases/project-portfolio-management/ |
| Product lifecycle | https://www.wrike.com/use-cases/product-lifecycle/ (one visit returned 429; the link is real) |
| Creative production | https://www.wrike.com/use-cases/creative-content-production/ |
| See all workflows | https://www.wrike.com/solutions/ with workflow filter |

Industries:

| Control | Opens |
|---|---|
| Manufacturing | https://www.wrike.com/industries/manufacturing/ |
| Professional services | https://www.wrike.com/professional-services-management/ |
| Agencies | https://www.wrike.com/use-cases/agency-management/ |
| Construction | https://www.wrike.com/industries/construction/ |
| Technology | https://www.wrike.com/industries/technology/ |
| Finance | https://www.wrike.com/industries/financial-services/ |
| See all industries | https://www.wrike.com/solutions/ with industry filter |

Side cards:

| Control | Opens |
|---|---|
| Book a demo | https://www.wrike.com/demo/ |
| Try our templates | https://www.wrike.com/templates/ |
| Read case studies | https://www.wrike.com/customer-stories/ |

## Resources menu

Learn: Resource hub https://www.wrike.com/resources/, Blog https://www.wrike.com/blog/, Guides https://www.wrike.com/guides/, Webinars https://www.wrike.com/webinars/, Trainings & certification https://www.wrike.com/discover/.

Community: Customer stories https://www.wrike.com/customer-stories/, Wrike Community https://community.wrike.com/, Partners https://www.wrike.com/partners/, Developers https://developers.wrike.com/.

Support: Help Center https://help.wrike.com/hc/en-us/, Premium Support Packages https://www.wrike.com/support-packages/, Professional services https://www.wrike.com/professional-services/, Templates https://www.wrike.com/templates/.

Side card: Read the report opens the Gartner report page above.

## Language panel

English `/`, Dansk `/da/`, Deutsch `/de/`, Español `/es/`, Français `/fr/`, Bahasa Indonesia `/id/`, Italiano `/it/`, Bahasa Melayu `/ms/`, Nederlands `/nl/`, Norsk `/no/`, Polski `/pl/`, Português (BR) `/pt-br/`, Svenska `/sv/`, Русский `/ru/`, 日本語 `/ja/`, 한국어 `/ko/`, 中文 (简体) `/zh-cn/`, 中文 (繁體) `/zh-tw/`. The first six locales loaded. The rest were recorded from the panel and not each opened.

## Home page controls

| Control | Opens |
|---|---|
| Try Wrike for free (hero) | Signup wall. Not followed. |
| Wrike in 3 minutes | In-page video control. Clicked. It did not navigate and did not open a dialog in this capture. Screenshot [home-light-video.png](screenshots/home-light-video.png). |
| Workflow tabs Ideate, Plan, Deliver, Report, Evolve | In-page tab state. Plan was selected. No navigation. |
| Previous slide / Next slide | Logo-row carousel. In-page. |
| Playback buttons on animated screenshots | In-page video play/pause. |
| Kate chat (Speak now, Contact Sales, Ask Kate a question) | Embedded sales chat. Not opened. Not typed into. |
| See all Wrike AI features | https://www.wrike.com/ai/ |

## Phone header (390)

| Control | Opens |
|---|---|
| Wordmark | https://www.wrike.com/ |
| Try for free | Signup wall. Not followed. |
| Toggle mobile navigation (`button.header-nav-button`) | Full-screen menu: Products, Solutions, Resources (each expands in place), Pricing, Enterprise, a business-email field (not filled), Try Wrike for free (signup wall, not followed), Log in (auth wall, not followed again), Contact Sales, EN. Screenshot [mobile-home-light-menu.png](screenshots/mobile-home-light-menu.png). |

## Footer

Product: Product tour `/tour/`, Pricing `/price/`, Wrike AI `/ai/`, Templates `/templates/`, Apps & Integrations `/apps/`, Ease of use `/features/ease-of-use/`, Gantt Chart Tool `/features/gantt-chart/`, Security `/security/`, Wrike API https://developers.wrike.com/, Compare `/compare/`, Features `/features/`.

Solutions: Enterprise `/enterprise/`, Marketing `/marketing/`, Creative `/teams/creative-project-management/`, Project Management `/project-management-office/`, Product Development `/teams/product-management/`, Business Operations `/teams/business-operations/`, Professional Services `/professional-services-management/`, IT Management `/teams/it-project-management/`, Students `/use-cases/collaboration-tool-for-students/`, All solutions `/solutions/`.

Resources: Help Center https://help.wrike.com/hc/en-us/, Community https://community.wrike.com/, Blog `/blog/`, Webinars `/webinars/`, Interactive Training `/discover/`, Support Packages `/support-packages/`, Wrike Status https://status.wrike.com/, Find a Reseller `/partners/reseller-locator/`, Google Project Management Tools `/google-apps/`, CA Notice at Collection `/security/privacy/#details-for-california-residents`.

Company: About Us `/company/`, Leadership `/newsroom/executive-bios/`, Careers `/jobs/`, Our Customers `/customer-stories/`, Events `/events/`, Newsroom `/newsroom/`, Partner Program `/partners/`, Collaborate `/collaborate/conference/`, Klaxoon by Wrike https://klaxoon.com/ (external), Contact Us `/contact-us/`.

Guides: Project Management, Professional Services, Workflow, Kanban, Agile, Scrum, Marketing Project Management, Collaborative Work Management, Digital Marketing, Go-to-Market, Remote Work, Return to Work, Product Management, Goal Setting. Each is `https://www.wrike.com/<name>-guide/`.

Legal: Privacy Policy `/security/privacy/`, Terms of Service `/security/terms/`, Your Privacy Choices `/security/privacy-choices/`.

Social (external, not opened as identity providers): X, Facebook, LinkedIn, YouTube, Instagram, plus App Store and Google Play store listings. These are publisher profile links in the footer, not sign-in buttons.

## Stopped branches

| Control | URL | Why stopped |
|---|---|---|
| Log in | https://login.wrike.com/login/ | Asks for email or corporate ID, then Next. Password step not reached. |
| Try Wrike for free / Try for free | Signup wall (header, hero, menu bar, phone menu) | Account creation. Not followed. |
| Google, Apple, Office on the login card | Identity providers | Not clicked. |
| Contact Sales, demo, and trial email fields | Public forms | Fields measured where visible. Not filled. Not submitted. |
| Kate chat | Overlay on the home page | Not typed into. |
