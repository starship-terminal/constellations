# Ballpark public site tree

Mapped from [https://ballparkhq.com/](https://ballparkhq.com/) on 2026-11-21, signed out, in headless Chromium (Playwright). Desktop viewport 1440×900 at 1x (`window.innerWidth` 1440, `devicePixelRatio` 1). Phone viewport 390×844 at 2x (`window.innerWidth` 390, `devicePixelRatio` 2, PNG 780×1688). Light theme only. No email, password, or provider button was used. No form was submitted.

The English sitemap index (`/sitemap_en-GB.xml`) lists 439 URLs. This tree records the controls on the homepage and the pages those controls open. Repeated article, glossary, template, and changelog URLs are named as families, with one photographed example each.

## Homepage controls

| Control | What it opens | Capture |
|---|---|---|
| Logo "Ballpark" | `/` | [home-light-default](screenshots/home-light-default.png) |
| Announcement "Ballpark is now available in Claude" | `https://claude.ai/directory/ballpark` (external). Not followed. | visible on the home shot |
| Platform (hover) | Mega menu, and the link itself goes to `/features` | [home-light-platform-menu](screenshots/home-light-platform-menu.png) |
| Solutions (hover, no href) | Flyout only. It does not navigate. | [home-light-solutions-menu](screenshots/home-light-solutions-menu.png) |
| Templates | `/templates` | [templates-light-default](screenshots/templates-light-default.png) |
| Pricing | `/pricing` | [pricing-light-default](screenshots/pricing-light-default.png) |
| Sign in | `/sign-in` email and password wall, plus Google and SSO. Branch stopped. | [sign-in-light-default](screenshots/sign-in-light-default.png) |
| Book a demo | `/contact/sales` | [contact-sales-light-default](screenshots/contact-sales-light-default.png) |
| Phone menu button (390) | Full-height sheet: Platform, Solutions, Use cases, Pricing, Templates | [mobile-home-light-menu-open](screenshots/mobile-home-light-menu-open.png) |
| Intercom launcher | Third-party chat. Not opened. | blue bubble on the home shot |
| Carousel dots | In-page story scroller. Not a new page. | measured in the earlier component crops |

## Platform menu

Hover on Platform. Each row is a page.

| Label | Path |
|---|---|
| AI Interviews | `/features/ai-interviewer` |
| Surveys | `/features/surveys` |
| Video Responses | `/features/video` |
| Figma Prototypes | `/features/figma-prototype-testing` |
| Copy Testing | `/features/copy-testing` |
| Live Interviews (beta) | `/features/live-interviews` |
| Participant Panel | `/features/recruitment` |
| Screeners | `/features/screeners` |
| AI Insights | `/features/ai-insights-report` |
| AI Agent | `/coach` |
| Developer API | `/developers` |
| ChatGPT | `/integrations/chatgpt` |
| Claude | `/integrations/claude` |
| User Interviews | `/integrations/user-interviews` |
| Figma | `/integrations/figma` |
| Rally | `/integrations/rally` |

The phone sheet lists the same features plus Website testing (`/features/website-testing`), Preference test (`/features/image-preference-test`), First click test (`/features/first-click-test`), Five second test (`/features/5-second-test`), Data tables (`/features/data-tables`), Card sorting (`/features/card-sorting`), and AI study creator (`/ai-research-study-creator`).

## Solutions menu

Hover on Solutions. No destination of its own.

| Group | Label | Path |
|---|---|---|
| Teams | Brand Teams | `/solutions/teams/brand` |
| Teams | Insights Teams | `/solutions/teams/insight` |
| Teams | Marketing Teams | `/solutions/teams/marketing` |
| Solutions | Concept Testing | `/solutions/concept-testing` |
| Solutions | Wireframe Testing | `/solutions/wireframe-testing` |
| Solutions | Design Survey | `/solutions/design-surveys` |
| Solutions | Video Surveys | `/solutions/video-surveys` |
| Roles | Product Managers | `/roles/product-managers` |
| Roles | User Researchers | `/roles/user-researchers` |
| Roles | Design Leadership | `/roles/design-leadership` |
| Roles | Product Designers | `/roles/product-designers` |

## Footer, from the homepage

| Group | Control | Opens |
|---|---|---|
| Product | AI interviewer, Video, Figma prototype testing, Website testing, Copy testing, Screeners, Image preference test, First click test, Five second test, Data tables, Card sorting, Live interviews, Recruitment, AI insights report | the feature paths above |
| Product | AI agent | `/coach` |
| Product | Enterprise | `/enterprise` |
| Product | Integrations | `/integrations` |
| Product | AI study creator | `/ai-research-study-creator` |
| Product | Developers (API/MCP) | `/developers` |
| Company | Security | `/security` |
| Company | Product updates | `/product-updates` |
| Company | Careers | `https://apply.workable.com/ballpark` (external). Not followed. |
| Company | Blog | `/blog` |
| Company | Crowd | `/crowd` |
| Company | Research services | `/research-services` |
| Company | Research glossary | `/research-glossary` |
| Company | Participant panel | `/participant-panel` |
| Legal | Privacy Policy, AI Policy, Participant Terms, Terms / MSA | `/privacy-policy`, `/ai-policy`, `/participant-terms`, `/terms-msa` |
| Resources | The User Testing Field Guide | `/field-guide` |
| Resources | calculators | `/resources/ab-testing-significance-calculator`, `/resources/ai-question-generator`, `/resources/margin-of-error-calculator`, `/resources/nps-calculator`, `/resources/recruitment-cost-calculator`, `/resources/sample-size-calculator` |
| Customers | NordVPN, Soldo, Vodafone, Coventry Building Society | `/customers/nordvpn`, `/customers/soldo`, `/customers/vodafone`, `/customers/coventry-building-society` |
| Compare | Maze, Dscout, UserZoom, UserTesting | `/compare/maze-alternative`, `/compare/dscout-alternative`, `/compare/userzoom-alternative`, `/compare/usertesting-alternative` |
| Support | Contact us | `/contact` |
| Support | Help center | `https://help.ballparkhq.com/` (external). Not followed. |
| Support | Trust center | `https://trust.ballparkhq.com/` (external). Not followed. |
| Support | Status | `https://status.ballparkhq.com/` (external). Not followed. |
| Social | Twitter, YouTube, LinkedIn, G2 | external. Not followed. |

## Auth walls (photographed, then stopped)

| Path | What it asks | Capture |
|---|---|---|
| `/sign-in` | Email, password, Continue with Google, Continue with SSO. Forgot password links to `/forgot-password`. | [sign-in-light-default](screenshots/sign-in-light-default.png), [mobile-sign-in-light-default](screenshots/mobile-sign-in-light-default.png) |
| `/sso` | Enterprise domain, then Continue with SSO. | [sso-light-default](screenshots/sso-light-default.png) |
| `/forgot-password` | Email, then Reset password. Not submitted. | [forgot-password-light-default](screenshots/forgot-password-light-default.png) |
| `/sign-up` | Redirects to `/contact/sales`. No account form. | not stored (it is the sales page) |
| `/reset-password` | Sitemap only. Not opened. | not captured |

## Families not walked one by one

| Family | Count in the English sitemap | Example photographed |
|---|---|---|
| `/blog/<post>` | posts under `/blog` plus category indexes | [blog-introducing-open-closed-and-hybrid-card-sorting-light-default](screenshots/blog-introducing-open-closed-and-hybrid-card-sorting-light-default.png). Category index `/blog/inside-ballpark` renders an empty list. |
| `/templates/<slug>` | 13 template URLs plus category filters (`/templates/popular`, `/templates/basics`, …) | [templates-popular-light-default](screenshots/templates-popular-light-default.png) |
| `/research-glossary/<term>` | 176 | [research-glossary-a-b-test-light-default](screenshots/research-glossary-a-b-test-light-default.png) |
| `/product-updates/<slug>` | 77 | index only: [product-updates-light-default](screenshots/product-updates-light-default.png) |
| `/developers/<slug>` | 22 | index only: [developers-light-default](screenshots/developers-light-default.png) |
| `/participant-panel/<slug>` | 22 | index only: [participant-panel-light-default](screenshots/participant-panel-light-default.png) |
| `/customers/<slug>` | 5 | NordVPN and Soldo photographed |
| `/contact/<campaign>` | 8, including `/contact/sales` | sales and `/contact` photographed. Campaign variants not walked. |
| Locale sitemaps | es, de, fr, pt, ja, it | not captured. The live site served English. |

`/template` (singular) returns the public 404 page. It is not a template index.

## Phone

The same public paths were photographed at 390×844. Files are `mobile-<slug>-light-default.png`. The only extra overlay at this width is the menu sheet above. Platform and Solutions do not open as separate flyouts on the phone. They are sections of that sheet.
