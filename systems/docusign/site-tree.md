# DocuSign public site tree

Mapped from https://www.docusign.com/ on 2026-11-21, signed out, in headless Playwright (Chromium). Desktop viewport 1440 x 900. Phone viewport 390 x 844. Cookie banners were hidden and never accepted. No email, password, code, or SSO control was used.

The crawl opened 68 desktop URLs and 18 phone URLs, all HTTP 200. It recorded 531 controls. Branches that leave for a login, signup, account, or checkout host were recorded and stopped.

## Utility bar

The bar sits above the main header. It is published sales contact chrome. This package does not copy the phone number into text or into a committed screenshot.

| Control | Opens | Kind |
|---|---|---|
| Promo link, "Leader in 2026 IDC MarketScape" | https://www.docusign.com/blog/docusign-named-a-leader-in-the-idc-marketscape-integrated-signing-workflows | public page |
| Sales phone link | a `tel:` link | not opened |
| Search | in-page search panel | interaction, query not typed |
| Support | https://support.docusign.com/s/?language=en_US | sibling host, not followed |
| Access Documents | https://apps.docusign.com/sign/access | login wall, branch stopped |
| Log In | https://apps.docusign.com/send, which redirects to https://account.docusign.com/oauth/auth | login wall, branch stopped |

Log In was opened once to confirm the wall. The page is "Log in to Docusign" with an empty email field, Next, and Sign Up for Free. Nothing was typed. Google, Apple, Microsoft, and SSO were not on that first screen and were not clicked.

## Main header

| Control | Opens | Kind |
|---|---|---|
| Logo | https://www.docusign.com/ | public page |
| Products | mega-menu panel, `aria-expanded` | interaction |
| Solutions | mega-menu panel, `aria-expanded` | interaction |
| Resources | mega-menu panel, `aria-expanded` | interaction |
| Enterprise | https://www.docusign.com/solutions/enterprise | public page |
| Plans & Pricing | https://ecom.docusign.com/plans-and-pricing/esignature | checkout wall, branch stopped |
| Contact sales | https://www.docusign.com/contact-sales | public form, not submitted |
| Buy now | https://ecom.docusign.com/plans-and-pricing/esignature | checkout wall, branch stopped |
| Try for free | https://trial.docusign.com/ | signup wall, branch stopped |

A second press on Products, Solutions, or Resources closes the panel. Escape closes it too.

## Products menu

The Products button does not navigate. Each row is a link.

| Label | URL | Followed |
|---|---|---|
| Intelligent Agreement Management | https://www.docusign.com/intelligent-agreement-management | yes |
| Contract Lifecycle Management | https://www.docusign.com/products/clm | yes |
| Iris | https://www.docusign.com/products/platform/ai | yes |
| Agreement Preparation | https://www.docusign.com/products/agreement-preparation | yes |
| Agreement Manager | https://www.docusign.com/products/platform/agreement-manager | yes |
| eSignature | https://www.docusign.com/products/electronic-signature | yes |
| Agents | https://www.docusign.com/products/agents | yes |
| Electronic Notarization | https://www.docusign.com/products/notary | yes |
| Workflow Builder | https://www.docusign.com/products/platform/workflow-builder | yes |
| Web Forms | https://www.docusign.com/products/web-forms | yes |
| App Center | https://www.docusign.com/products/platform/app-center | yes |
| Integrations | https://www.docusign.com/integrations | yes, index |
| MCP Connectors | https://www.docusign.com/products/mcp | yes |
| APIs | https://www.docusign.com/products/apis | yes |
| Explore All Products | https://www.docusign.com/products | yes |

Footer-only product links, not in the menu panel:

| Label | URL | Followed |
|---|---|---|
| Identify | https://www.docusign.com/products/identify | yes |
| Special offers | https://www.docusign.com/products/special-offers | yes |
| Signers | https://www.docusign.com/products/electronic-signature/signers | yes |

## Solutions menu

| Label | URL | Followed |
|---|---|---|
| IAM Core | https://www.docusign.com/solutions/iam-core | yes |
| Sales | https://www.docusign.com/solutions/departments/sales | yes |
| Customer Experience | https://www.docusign.com/solutions/departments/customer-experience | yes |
| Human Resources | https://www.docusign.com/solutions/departments/human-resources | yes |
| Legal | https://www.docusign.com/solutions/departments/legal | yes |
| Procurement | https://www.docusign.com/solutions/departments/procurement | yes |
| View All Departments | https://www.docusign.com/solutions | yes |
| Financial Services | https://www.docusign.com/solutions/industries/financial-services | yes |
| Insurance | https://www.docusign.com/solutions/industries/insurance | yes |
| Real Estate | https://www.docusign.com/solutions/industries/real-estate | yes |
| Government | https://www.docusign.com/solutions/industries/government | yes |
| Healthcare | https://www.docusign.com/solutions/industries/healthcare | yes |
| Life Sciences | https://www.docusign.com/solutions/industries/life-sciences | yes |
| View All Industries | https://www.docusign.com/solutions | yes, same index |

Footer-only solution links:

| Label | URL | Followed |
|---|---|---|
| Small and medium-sized businesses | https://www.docusign.com/solutions/small-and-medium-sized-businesses | yes |
| Why Docusign | https://www.docusign.com/why-docusign | yes |

## Resources menu

| Label | URL | Kind |
|---|---|---|
| Blog | https://www.docusign.com/blog | public index, opened |
| Customer Stories | https://www.docusign.com/customer-stories | public index, opened |
| Resource Center | https://www.docusign.com/resources | public index, opened |
| Legality Guide | https://www.docusign.com/products/electronic-signature/legality | public page, opened |
| Product Releases | https://www.docusign.com/releases | public page, opened |
| Roadmap | https://www.docusign.com/releases/roadmap | public page, opened |
| Learn Hub | https://www.docusign.com/learn | public index, opened |
| Support Center | https://support.docusign.com/s/?language=en_US | sibling, not followed |
| Customer Success | https://www.docusign.com/customer-success | public page, opened |
| Docusign University | https://dsucustomers.docusign.com/ | sibling, not followed |
| Trust Center | https://www.docusign.com/trust | public page, opened |
| Safety Center | https://www.docusign.com/safety | public page, opened |

## Walls

Opened once to confirm the gate, then stopped. Nothing was typed.

| Control | Lands on | What the page asks |
|---|---|---|
| Log In, Access Documents | https://account.docusign.com/oauth/auth | email, then Next. No password on the first screen. No code sent |
| Try for free | https://trial.docusign.com/ | email and Get Started. Not filled |
| Buy now, Plans & Pricing | https://ecom.docusign.com/plans-and-pricing/esignature | plan picker. No checkout step was taken |
| Partner Portal (footer) | https://partners.docusign.com/s/login/ | login wall, not opened past the record |
| Free developer account | https://www.docusign.com/developers/sandbox | public page that offers an account. No account was created |
| Send a sample agreement (footer) | https://apps.docusign.com/send/prepare | login wall, not opened |

Known probe, not repeated: https://account.docusign.com/ accepted an email and then asked for a password. No code was sent. This capture did not type an email.

IAM Plans, eSignature Plans, Real Estate Plans, and API Plans in the footer point at ecom.docusign.com. Same checkout wall. Branch stopped.

## In-page interactions

| Page | Control | What it does |
|---|---|---|
| Home | Products, Solutions, Resources | Opens a mega-menu. A second press or Escape closes it |
| Home | Search | Opens a search field. No query was typed |
| Home at 390 | Open Menu | Opens a drawer: Products, Solutions, Resources, Enterprise, Plans & Pricing, plus search and close |
| Product and solution pages | FAQ button with `aria-expanded=false` | Opens one accordion item |
| Home hero | Get Started | Sits on a form. Not clicked. The form was not filled |
| Home hero | Country/region select | Native select. Not changed |
| Home hero | Marketing consent checkbox | Not checked |
| Trial wall | Help | Menu. Not opened, because the branch had already stopped |
| Login wall | Sign Up for Free | Would continue the account flow. Not clicked |
| Login wall | Next | Would submit the email. Not clicked |
| Cookie dialog | Accept All Cookies, Cookies Settings | Hidden or left unanswered. Never accepted |
| Footer | Region links (`/en-ca`, `/fr-fr`, and the other locale homes) | Same marketing site in another locale. Not photographed |
| Footer | App store badges | Store listings. Not opened. No app was downloaded |
| Several pages | Docusign Assistant | A chat launcher. Not opened |

## Pages opened

Desktop, 1440. Shot names are the crawl files. Committed screenshots are a cropped subset in [screenshots/](screenshots).

| Path | Title |
|---|---|
| / | Docusign, electronic signature and agreement management |
| /intelligent-agreement-management | IAM |
| /why-docusign | Why Docusign |
| /products | Products and capabilities |
| /products/clm | Contract lifecycle management |
| /products/platform/ai | Iris |
| /products/agreement-preparation | Agreement preparation |
| /products/platform/agreement-manager | Agreement manager |
| /products/electronic-signature | eSignature |
| /products/electronic-signature/legality | Legality, United States |
| /products/electronic-signature/signers | Sign documents |
| /products/agents | Iris agents |
| /products/notary | Online notary |
| /products/platform/workflow-builder | Workflow builder |
| /products/web-forms | Web forms |
| /products/platform/app-center | App center |
| /products/mcp | MCP connectors |
| /products/apis | API |
| /products/identify | ID verification |
| /products/special-offers | Coupons and promos |
| /integrations | Integrations index |
| /solutions | Solutions index |
| /solutions/iam-core | IAM Core |
| /solutions/enterprise | Enterprise |
| /solutions/small-and-medium-sized-businesses | Small business |
| /solutions/departments/sales | Sales |
| /solutions/departments/customer-experience | Customer experience |
| /solutions/departments/human-resources | Human resources |
| /solutions/departments/legal | Legal |
| /solutions/departments/procurement | Procurement |
| /solutions/industries/financial-services | Financial services |
| /solutions/industries/insurance | Insurance |
| /solutions/industries/real-estate | Real estate |
| /solutions/industries/government | Government |
| /solutions/industries/healthcare | Healthcare |
| /solutions/industries/life-sciences | Life sciences |
| /blog | Blog index |
| /blog/{post} | One post photographed as the template. Sitemap lists about 2,183 English posts |
| /customer-stories | Stories index |
| /customer-stories/{story} | Four stories opened as the template |
| /resources | Resource center |
| /learn | Learn hub |
| /templates | Templates index |
| /releases | Product releases |
| /releases/roadmap | Roadmap |
| /customer-success | Customer success |
| /trust | Trust center |
| /trust/trust-portal | Trust portal |
| /safety | Safety center |
| /partners | Partner ecosystem |
| /partners/isv-embed | Embedded eSignature for ISVs |
| /contact-sales | Talk to sales. Form not submitted |
| /company | About |
| /company/leadership | Leadership |
| /company/news-center | News index |
| /company/contact-us | Contact |
| /legal/terms-and-conditions | Terms |
| /privacy | Privacy notice |
| /invoice-generator | Invoice generator. Not used |
| /signature-generator | Signature generator. Not used |
| /developers/sandbox | Developer account offer. No account created |

Phone, 390: home, mobile menu, blog index, solutions index, products index, and the same product URLs the desktop pass opened first (CLM, Iris, agreement preparation, agreement manager, eSignature, agents, notary, workflow builder, web forms, app center, MCP, APIs, IAM, IAM Core, one blog post). Login and pricing walls were also shot at 390 and not entered.

## Sitemap, not all opened

`sitemap.xml` is an index. English `main-sitemap.xml` has 1,747 URLs. English blog sitemap has about 2,183. Locale copies (en-gb, fr-fr, ja-jp, and the rest of the index) were not crawled.

| First path segment | Indexed URLs | What was opened |
|---|---|---|
| /trust | 533 | index and trust portal. Alerts are one template |
| /company | 332 | about, leadership, news index, contact. News items are one template |
| /legal | 206 | terms. Other legal docs are one template |
| /products | 169 | every menu product, plus identify, signers, legality, special offers |
| /customer-stories | 138 | index and four stories |
| /resources | 102 | index |
| /templates | 60 | index. Individual templates are one template |
| /learn | 55 | index |
| /integrations | 38 | index. Individual integrations are one template |
| /solutions | 24 | every menu department and industry, plus enterprise and small business |
| /releases | 14 | index and roadmap |

Templates treated as one page for screenshots: `/blog/{post}`, `/customer-stories/{story}`, `/trust/alerts/{alert}`, `/company/news-center/{item}`, `/legal/{group}/{doc}`, `/templates/{template}`, `/integrations/{integration}`, `/resources/{group}/{item}`, `/learn/{group}/{item}`, `/lp/{campaign}`.
