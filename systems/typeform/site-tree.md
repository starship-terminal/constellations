# Typeform public site tree

Mapped on 2026-11-21 from [https://www.typeform.com/](https://www.typeform.com/) in headless Chromium at 1440x900, before screenshots. The page is a Webflow marketing site. OneTrust mounts a cookie dialog on load. That dialog was hidden, never answered. No form was submitted. Login, signup, Google, Microsoft, Apple, Facebook and SSO were not clicked.

Theme: the marketing site paints one light theme. `color-scheme` on `html` is `normal`. There is no `data-theme` switch and no dark class on the public pages.

## Home chrome

| Control | Opens |
|---|---|
| Announcement banner "Try it now" | [https://www.typeform.com/mcp](https://www.typeform.com/mcp) |
| Close announcement banner | Dismisses the banner. Local only. |
| Logo "Back to home" | [https://www.typeform.com/](https://www.typeform.com/) |
| Platform (hover, `aria-label="open products dropdown menu"`) | Menu. See Platform menu. A click toggles it shut. |
| Solutions (hover, `aria-label="open solutions dropdown menu"`) | Menu. See Solutions menu. |
| Resources (hover, `aria-label="open resource dropdown menu"`) | Menu. See Resources menu. |
| Pricing | [https://www.typeform.com/pricing](https://www.typeform.com/pricing) |
| Log in | Auth wall. [https://admin.typeform.com/login](https://admin.typeform.com/login). Branch stopped. |
| Contact sales | Hosted Typeform. [https://tfsales.typeform.com/to/PxcVKQGb](https://tfsales.typeform.com/to/PxcVKQGb?source=website&source2=navigation). Not submitted. |
| Sign up | Auth wall. [https://admin.typeform.com/signup](https://admin.typeform.com/signup). Branch stopped. |
| Phone menu (`aria-label="open mobile navigation menu"`, 390 only) | Full-screen nav with the same links. |
| Hero carousel dots "Go to slide 1" through "Go to slide 9" | Switches the customer-story slider. Local. |
| Hero video play | Plays the homepage animation. Local. |
| Cookie settings | OneTrust preference centre. Not opened (consent POST). Recorded as present, hidden. |

A hidden account dropdown (`w-dropdown-list-3`) sits in the DOM for a signed-in visitor: My forms, Refer friends, Log out, all on `admin.typeform.com`. It is not visible signed out. Not followed.

## Platform menu

| Item | Opens |
|---|---|
| Platform overview | [https://www.typeform.com/platform-overview](https://www.typeform.com/platform-overview) |
| Typeform AI | [https://www.typeform.com/ai](https://www.typeform.com/ai) |
| Typeform MCP | [https://www.typeform.com/mcp](https://www.typeform.com/mcp) |
| Growth Flow | [https://www.typeform.com/growth](https://www.typeform.com/growth) |
| Research Flow | [https://www.typeform.com/research-flow](https://www.typeform.com/research-flow) |
| Contacts and Automations | [https://www.typeform.com/contacts-and-automations](https://www.typeform.com/contacts-and-automations) |
| Video engagement | [https://www.typeform.com/video](https://www.typeform.com/video) |
| Analytics and reporting | [https://www.typeform.com/reporting](https://www.typeform.com/reporting) |
| Integrations | [https://www.typeform.com/connect](https://www.typeform.com/connect) |
| Form, survey, quiz, test, poll, application, landing page, NPS, registration, short form builders | `/forms`, `/surveys`, `/quizzes`, `/test-maker`, `/poll-builder`, `/application-form-builder`, `/landing-page-builder`, `/nps-form-builder`, `/registration-form-builder`, `/short-form-builder` |
| Choose one | [https://www.typeform.com/templates](https://www.typeform.com/templates) |

## Solutions menu

| Item | Opens |
|---|---|
| Marketing | [https://www.typeform.com/roles/b2b-marketing](https://www.typeform.com/roles/b2b-marketing) |
| Product | [https://www.typeform.com/templates-category/product](https://www.typeform.com/templates-category/product) |
| Human resources | [https://www.typeform.com/roles/hr](https://www.typeform.com/roles/hr) |
| Customer success | [https://www.typeform.com/templates-category/customer-success](https://www.typeform.com/templates-category/customer-success) |
| Lead generation, employee onboarding, employee satisfaction, employee engagement, customer feedback | `/use-case/lead-generation`, `/use-case/employee-onboarding`, `/use-case/employee-satisfaction`, `/use-case/employee-engagement`, `/use-case/customer-feedback` |
| View all use cases | [https://www.typeform.com/use-case-gallery](https://www.typeform.com/use-case-gallery) |
| Core / Growth / Research Flow / Talent / Enterprise plans | `/pricing`, `/growth`, `/research-flow`, `/pricing/talent`, `/enterprise` |

## Resources menu

| Item | Opens |
|---|---|
| Help center | [https://help.typeform.com/hc/en-us](https://help.typeform.com/hc/en-us) |
| Community | [https://community.typeform.com/](https://community.typeform.com/) |
| Contact us | [https://help.typeform.com/hc/en-us/requests/new](https://help.typeform.com/hc/en-us/requests/new). Support request form. Not submitted. |
| Partners | [https://www.typeform.com/partners](https://www.typeform.com/partners) |
| Careers | [https://www.typeform.com/careers](https://www.typeform.com/careers) |
| Webinars | [https://www.typeform.com/webinars](https://www.typeform.com/webinars) |
| Browse blog | [https://www.typeform.com/blog](https://www.typeform.com/blog) |

## Footer

Repeated on marketing pages. Dropdowns open a short list, then a page.

| Control | Opens |
|---|---|
| Enterprise | `/enterprise`, `/enterprise/healthcare` |
| Popular templates / Recent templates | Ten template pages under `/templates/` |
| Popular categories / Recent categories | Template category indexes under `/templates-sub-category/` and `/templates-category/education` |
| Popular integration apps / More integration apps | `/connect/slack`, `mailchimp`, `klaviyo`, `wordpress`, `pipedrive`, `google-calendar`, `zoho-crm`, `office-365`, `zendesk` |
| Popular app categories / More app categories | `/connect-category/` analytics, sales, payments, scheduling, email, support, automation, documents, rewards, collaboration |
| Why Typeform? | `/blog/typeform-vs-jotform`, `/blog/typeform-vs-formstack` |
| Partners | `/partners/agencies`, `/partners/technology`, `/agencies`, `/partners/startups` (redirects to `/typeform-startups`) |
| English | Footer language list. The visible items on the homepage probe resolved to `#`. Not a theme switch. |
| Pricing, Blog, Guides, Help center, Community, Tutorials, FAQs, Referral program, System status, Developers / API, AI Info, About us, Careers, Contact sales, Legal, Newsletter, Cookie policy, Report abuse | Matching public pages listed below |
| Facebook, X, Instagram, YouTube, LinkedIn | External social profiles. Not followed. |

## Pages reached from the home tree

Each row is a public page that loaded at HTTP 200. Controls are the ones that are not the shared header and footer.

| Page | What its own controls do |
|---|---|
| `/` | Banner, three nav menus, story slider, video play, CTAs into signup (stopped) and product pages |
| `/pricing` | Monthly / Yearly billing toggle (local). Plan info buttons open tooltips. Plan CTAs go to signup (stopped). A select is present and was not submitted. |
| `/forms`, `/surveys`, `/quizzes`, `/test-maker` | Step tabs (Build / Share / Learn) and FAQ accordions. Local. |
| `/ai`, `/mcp`, `/growth`, `/research-flow`, `/contacts-and-automations`, `/video`, `/reporting`, `/platform-overview` | Product marketing. FAQ accordions and, on some, a Play control for an embedded demo. Local. |
| `/poll-builder`, `/application-form-builder`, `/landing-page-builder`, `/nps-form-builder`, `/registration-form-builder`, `/short-form-builder` | Same marketing pattern. Some repeat the Monthly / Yearly toggle. |
| `/templates` and category indexes | Forms / Surveys / Quizzes tabs and a search field. Search was focused, never submitted. |
| `/templates/<slug>` (ten samples from the footer menus) | "Open template preview" opens a preview dialog. "Close template preview modal" closes it. Use-this CTAs go to signup (stopped). |
| `/connect` and `/connect/<app>` and `/connect-category/<slug>` | Integration directory. Search field present. Connect CTAs go to signup (stopped). |
| `/enterprise`, `/enterprise/healthcare` | Enterprise marketing. Contact sales opens the hosted sales form (not submitted). |
| `/blog`, `/blog-category/customer`, `/guides`, two comparison posts | Article indexes and posts. Posts have "Scroll back to top" and a closeable CTA banner. |
| `/about-us`, `/careers`, `/legal`, `/legal/cookie-policy`, `/ai-info`, `/refer-a-friend`, `/developers/` | Static marketing and legal pages. Careers has value tabs (local). |
| `/partners/agencies`, `/partners/technology`, `/agencies`, `/typeform-startups` | Partner and startup pages. Agency directory has sort and pagination (local). |
| `help.typeform.com` home, Videos, FAQ, Report Abuse | Zendesk help center. Language menu and article helpfulness buttons. Not submitted. |
| `community.typeform.com` | Public community home. "Log in" and "Create a post" are auth walls. Stopped. |
| `status.typeform.com` | Status page. Component toggles are local. "Subscribe to updates" is a form. Not submitted. |
| `tfsales.typeform.com/to/PxcVKQGb` | Hosted sales form. First question is visible. Not answered, not submitted. |
| `tfproductops.typeform.com/to/f9ErlyGj` | Newsletter signup form. Not filled, not submitted. Accept all / Reject all cookies not clicked. |

## Auth walls (branch stopped)

| Control | URL | What was on screen | What was not done |
|---|---|---|---|
| Log in | [https://admin.typeform.com/login](https://admin.typeform.com/login) | Continue with Google, Continue with Microsoft, Continue with email, Log in with SSO, Sign up | Google was not clicked. The email form was not submitted. |
| Sign up | [https://admin.typeform.com/signup](https://admin.typeform.com/signup) | Account creation | Not filled. |
| Get started, plan CTAs, Use this template, Connect | `admin.typeform.com` signup or login | Same wall | Not followed past the URL. |
| Hidden account menu | `admin.typeform.com`, `admin.typeform.com/login/logout` | Not visible signed out | Not followed. |

## Not in this tree

The sitemap lists thousands of blog posts, templates and help articles. This tree is the controls reachable from the homepage, its menus and its footer, plus one sample of each repeated family (one template, one integration, one blog post, one help article). The form builder, results, contacts and automations product are behind the login wall and were not captured.

## Capture coverage against this tree

Shot at 1440x900 and 390x844: home (desktop menus open; phone menu open with sections closed), pricing monthly and yearly, forms, AI, MCP, growth, research flow, templates (search focused, not submitted), one template preview dialog, connect, enterprise, blog, one blog post, legal, about, developers, help home, status, login wall, signup wall.

Mapped in this file and not individually shot: the rest of the Platform and Solutions product pages, role and use-case pages, the other nine footer templates, integration app pages, partner pages, careers, webinars, community home, newsletter and sales hosted forms (seen, not submitted), cookie preference centre (hidden, not opened), FAQ accordions, story slider, and the language lists. Phone captures of those mapped pages are the same gap.
