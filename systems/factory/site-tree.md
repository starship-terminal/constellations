# Factory public site tree

Walked signed out on 2026-11-21 from [https://factory.ai/](https://factory.ai/) (HTTP 200). That origin redirects to [https://factory.com/](https://factory.com/). Desktop viewport 1440. Phone viewport 390. No consent banner was offered. No page-level theme switch was found on the marketing site. Marketing pages paint light (`html[data-theme="light"]`). [https://docs.factory.com/](https://docs.factory.com/) paints light by default and has Light, Dark, and System switches. Dark was opened and photographed.

Opened means the control was used and the result was photographed or the destination loaded. Linked means the href was read and the page was not opened in this pass. Query strings are stripped.

A control that opens a login or signup wall is recorded and that branch stops. Nothing was typed. No identity provider was clicked. No form was submitted.

## Header, desktop

The logo links to `/`. Photographed in [home-light-default.png](screenshots/home-light-default.png).

| Control | Opens |
|---|---|
| Product | Menu on `/`. See below. |
| Enterprise | Menu on `/`. See below. |
| Pricing | `/pricing` |
| News | `/news` |
| Company | Menu on `/`. See below. |
| Docs | `https://docs.factory.com/` |
| Globe | `/ja` (aria-label 日本語に切り替える). Linked, not opened as a second language pass beyond confirming HTTP 200. |
| Sign in | `https://app.factory.ai/`, which redirects to `https://auth.factory.ai/`. Wall. Branch stopped. Photographed empty in [login-dark-empty.png](screenshots/login-dark-empty.png). |
| Contact sales | `/contact` |
| Download | `https://app.factory.ai/api/desktop`. File download. Not saved. |

### Product menu

Button, `aria-expanded`. Click keeps the URL on `/`. Photographed in [home-light-menu-product.png](screenshots/home-light-menu-product.png).

| Group | Control | Opens |
|---|---|---|
| Surfaces | Factory App | `/product/desktop` |
| Surfaces | Droid CLI | `/product/cli` |
| Surfaces | Droid Exec | `https://docs.factory.com/droid-exec/overview` |
| Surfaces | Droid SDK | `https://docs.factory.com/sdk/python` |
| Surfaces | Delegations | `https://docs.factory.com/delegations` |
| Surfaces | IDE Integrations | `/product/ide` |
| Surfaces | Factory API | `https://docs.factory.com/api-reference` |
| Automations | Custom Automations | `/product/automations` |
| Automations | Triage | `https://docs.factory.com/automations/triage` |
| Automations | Automated QA | `https://docs.factory.com/automations/automated-qa` |
| Automations | Security Review | `https://docs.factory.com/automations/security-review` |
| Automations | Code Review | `https://docs.factory.com/automations/code-review-ci` |
| Automations | Incident Response | `https://docs.factory.com/automations/incident-response` |
| Automations | AutoWiki | `https://docs.factory.com/automations/wiki/overview` |
| Platform | Software Factory | `/product/software-factory` |
| Platform | Security Factory | `/product/security-factory` |
| Platform | Connectors | `/product/connectors` |
| Platform | Missions | `/product/missions` |
| Platform | Cloud Agents | `/product/cloud-agents` |
| Platform | Droid Computers | `/product/droid-computers` |
| Platform | Agent Effectiveness | `/product/agent-effectiveness` |
| Platform | Agent Readiness | `/agent-readiness` |
| Platform | Model Routing | `/product/router` |

Product pages that were opened (HTTP 200): `/product/analytics`, `/product/desktop` was linked from the menu and not opened as a second shot, `/product/cli`, `/product/ide`, `/product/automations`, `/product/software-factory`, `/product/security-factory`, `/product/connectors`, `/product/missions`, `/product/cloud-agents`, `/product/droid-computers`, `/product/agent-effectiveness`, `/product/router`, `/agent-readiness`. Docs destinations were linked, not each opened.

### Enterprise menu

Button. Click keeps the URL on `/`.

| Group | Control | Opens |
|---|---|---|
| Industries | Defense & NatSec | `/industries/defense` |
| Industries | Federal | `/industries/federal` |
| Industries | Financial Services | `/industries/financial-services` |
| Industries | Healthcare | `/industries/healthcare` |
| Industries | Technology | `/industries/technology` |
| Industries | Telecom | `/industries/telecom` |
| Deployment | Managed | `/deployment/factory-managed` |
| Deployment | Private | `/deployment/factory-private` |

Each of those eight pages loaded HTTP 200 in this pass.

### Company menu

Button. Click keeps the URL on `/`.

| Control | Opens |
|---|---|
| About | `/company` |
| Events | `/events` |
| Careers | `/company#careers` |

## Header, phone (390)

The island collapses to the logo, a globe, and Open menu. Opened in [mobile-home-light-menu.png](screenshots/mobile-home-light-menu.png) with Product expanded.

Product, Enterprise, and Company are buttons in the drawer. Product expands the same Surfaces, Automations, and Platform links as the desktop menu. Sign in, Contact sales, and Download sit at the bottom of the drawer. Sign in is the same auth wall. Download on this width links to `/product/desktop`, not the file endpoint.

## Homepage body

URL stays `/` unless noted. Photographed in [home-light-default.png](screenshots/home-light-default.png).

| Control | Result |
|---|---|
| Download for Mac | `https://app.factory.ai/api/desktop`. File download. Not saved. |
| Other downloads | Menu on `/`. Apple Silicon and Intel link to `https://app.factory.ai/api/desktop` with a platform query (stripped, not followed). Windows x64 and ARM64 do the same. Linux links to `https://docs.factory.com/factory-app/linux`. Photographed in [home-light-downloads.png](screenshots/home-light-downloads.png). |
| Book demo | `/contact` |
| Copy code | Copies the CLI install command. URL stays `/`. Not a navigation. |
| Get started | `https://app.factory.ai/`. Wall. Branch stopped. |
| Start building | `https://app.factory.ai/`. Wall. Not followed a second time. |
| Analytics card | `/product/analytics` |
| Droid Computers card | `/product/droid-computers` |
| Agent Readiness card | `/product/agent-readiness` |
| Mission Control card | `/product/missions` |
| Automations card | `https://docs.factory.com/web/automations` |
| Model Routing card | `/product/router` |
| Code Review card | `https://docs.factory.com/guides/droid-exec/code-review` |
| AutoWiki card | `https://docs.factory.com/cli/features/wiki/overview` |

## Footer

Shared on marketing pages.

| Control | Opens |
|---|---|
| Events | `/events` |
| Case Studies | `/news` |
| Contact Sales | `/contact` |
| Open Source | `/oss` |
| Factory for Science | `/science` |
| Careers | `/company` |
| Security | `/security` |
| Trust Center | `https://trust.factory.com/` (HTTP 200, public trust site) |
| Partners | `/partners` |
| The Guild | `/ambassador` |
| Privacy Policy | `/privacy-policy` |
| Terms of Service | `/legal/terms-individual` |
| SLA | `/sla` |
| DPA | `/data-processing-agreement` |
| X | `https://x.com/factory` |
| LinkedIn | `https://www.linkedin.com/company/factory-hq/` |
| GitHub | `https://github.com/Factory-AI` |
| 日本語 | `/ja` |

External social links were not followed.

## Pricing

`/pricing` loaded HTTP 200. Photographed in [pricing-light-default.png](screenshots/pricing-light-default.png).

Plans visible: Free, Pro, Teams, Business, Enterprise. Pro has a segment of Pro, Plus, and Max. Clicking Plus keeps the URL on `/pricing`. Photographed in [pricing-light-plus.png](screenshots/pricing-light-plus.png). Max was clicked the same way.

| Control | Opens |
|---|---|
| Get Pro | `https://app.factory.ai/` with a plan query. Wall. Branch stopped. |
| Get Teams | `https://app.factory.ai/` with a plan query. Wall. Not followed a second time. |
| Contact Sales | `/contact` |

FAQ items are buttons (`aria-expanded`). A click aimed at the first expanded-false button landed on the header Product control and did not open an answer. The titles were not each opened. The URL stays `/pricing`.

## News

`/news` loaded HTTP 200. Photographed in [news-light-default.png](screenshots/news-light-default.png).

Search is a text field, placeholder Search, aria-label Search news. Nothing was typed into it in the photographed pass. The URL stayed `/news`.

Filter news by category is a button. Its menu did not paint in this pass (the control was not visible to a click). Category links were read from the page: Research links to `/news?category=research` (query stripped). Article cards link to `/news/<slug>`. One example read: `/news/databricks-partnership`. Articles were linked, not each opened.

View more stays on `/news` and reveals more cards. Not followed into a new page.

## Company

`/company` loaded HTTP 200. Photographed in [company-light-default.png](screenshots/company-light-default.png).

See openings links to `#careers`. Start building links to `https://app.factory.ai/` with a sign-up hint. Wall. Branch stopped.

All departments and All locations are buttons. A later click did not leave a photograph of an open menu. Search roles is a search field. Nothing was typed into it. Role cards link to `/careers/<slug>`. Examples read and not opened: member-of-deployed-staff, software-engineer-ai, software-engineer-data, software-engineer-federal, software-engineer-fullstack, software-engineer-mobile. Previous page and Next page stay on `/company`.

## Contact

`/contact` loaded HTTP 200. Empty form photographed in [contact-light-empty.png](screenshots/contact-light-empty.png).

Fields seen and left empty: First Name, Last Name, Company, Work Email, How did you find us (Select one...), How can we help. Submit was not clicked. A captcha response field was present and was not solved.

How did you find us opens a list on the same URL. Photographed in [contact-light-how.png](screenshots/contact-light-how.png). Options seen, none chosen: LinkedIn, X, Event, Podcast, Google, Billboard, Referral/word of mouth, An existing customer, Other.

## Docs

`https://docs.factory.com/` loaded HTTP 200. Light photographed in [docs-light-default.png](screenshots/docs-light-default.png). Dark photographed in [docs-dark-default.png](screenshots/docs-dark-default.png) after Switch to Dark theme. The switch was set back toward light after the shot.

| Control | Opens |
|---|---|
| Documentation | `/` on the docs host |
| API Reference | `/api-reference` |
| Changelog | `/changelog` |
| Search | Dialog on the same URL. Placeholder "Search the docs". Photographed in [docs-light-search.png](screenshots/docs-light-search.png). Nothing typed. Escape closes it. |
| Switch to Dark theme | In-page. URL stays. |
| Switch to Light theme | In-page. URL stays. |
| Switch to System theme | In-page. URL stays. |
| Sign in | `https://app.factory.ai/`. Wall. Branch stopped. |
| Download | `https://app.factory.ai/api/desktop`. Not saved. |
| Create an account | `https://app.factory.ai/` with a sign-up hint, which redirects to `https://auth.factory.ai/sign-up`. Wall. Photographed empty in [signup-dark-empty.png](screenshots/signup-dark-empty.png). |
| Quickstart guide | `/droid-cli/quickstart` |
| Sidebar groups | Buttons that expand on the same URL: Welcome, Plans & Pricing, Product surfaces, Automations, Platform capabilities, and further groups. Welcome was already expanded. |

Sidebar destinations were linked, not each opened. Examples: `/docs/support`, `/models`, `/missions/overview`, `/enterprise`, `/harness/agents-md`, `/factory-app/linux`.

## Other public pages opened

Each loaded HTTP 200 unless noted.

| Page | Notes |
|---|---|
| `/enterprise` | Customer-study pager stays on the page. Contact sales goes to `/contact`. |
| `/events` | Event cards link to `/events/<slug>`. Linked, not each opened. |
| `/oss` | Public open-source page. |
| `/science` | Public science page. A form was present and not submitted. |
| `/security` | Photographed in [security-light-default.png](screenshots/security-light-default.png). |
| `/partners` | Partner network. |
| `/ambassador` | Join the Guild stays on `#ambassador-apply`. Existing member links to `/guild/login`. Wall. Branch stopped. |
| `/privacy-policy`, `/legal/terms-individual`, `/sla`, `/data-processing-agreement` | Legal pages. |
| `/ja` | Japanese home. Same header structure. |
| `https://trust.factory.com/` | Trust center. HTTP 200. |

Case studies (`/case-studies/<slug>`), articles (`/articles/<slug>`), news posts, careers posts, and agent-readiness repo pages were linked from these pages and not each opened. They are public marketing pages, not a signed-in app.

## Login and signup walls

| URL | How it was reached | Stopped |
|---|---|---|
| `https://factory.com/login` | `https://factory.ai/login` redirects here. HTTP 404. Title Login – Vercel. | Empty email field and Continue with Email, Google, GitHub, ChatGPT, SAML SSO, and Passkey were read. Stylesheet did not paint. Photographed unstyled in [vercel-login-unstyled.png](screenshots/vercel-login-unstyled.png). Not typed. Not pressed. |
| `https://auth.factory.ai/` | Sign in, and `https://app.factory.ai/`. | Empty email. Continue with email and Continue with Google not used. |
| `https://auth.factory.ai/sign-up` | Sign up, and sign-up hints. | Empty email. Continue and Continue with Google not used. |
| `https://factory.com/guild/login` | Existing member on the Guild page. | Empty email (placeholder only). Send link and Continue with Google not used. |

No signed-in package was invented. The app behind auth.factory.ai was not entered.
