# Deel public site tree

Mapped from [https://www.deel.com/](https://www.deel.com/) on 2026-11-21 in headless Chrome (Playwright, `channel: chrome`), signed out, English locale. Desktop viewport 1440×900 (`innerWidth` 1440, `innerHeight` 900, `devicePixelRatio` 1 on the page shots). Phone checks used 390×844 (`innerWidth` 390, `devicePixelRatio` 2, PNG 780×1688). Nothing was typed. No form was submitted. Google, Apple, the Deel app, SSO, and every other OAuth control were not clicked. Cookiebot was hidden after the arrival shot, never answered. Newsletter and demo fields were not filled.

Each control is one of: **page** (navigation), **menu** (stays on the page), **overlay** (drawer or dialog that stays on the page), **dialog**, or **login wall** (branch stopped).

## Header (every public marketing page)

| Control | Opens | Where |
|---|---|---|
| Wordmark | page | `/` |
| Solutions | menu | Mega-menu on the same URL. See Solutions menu. |
| Use cases | menu | Mega-menu on the same URL. See Use cases menu. |
| Who we serve | menu | Mega-menu on the same URL. See Who we serve menu. |
| Resources | menu | Mega-menu on the same URL. See Resources menu. |
| Pricing | page | `/pricing/` |
| Select language (visible text EN) | menu | Locale list on the same URL. Not changed. See Language menu. |
| Log in | login wall | `https://app.deel.com/login?lang=en`. Branch stopped. |
| Book a demo (header) | dialog | Same URL with `?form=` query. "Experience Deel with a live demo". Not filled. The no-JS target is the page `/request-a-demo/`. |
| Claim offer (promo bar) | page | `/plp/peo/` |
| Close banner | menu | Hides the promo bar on the same URL. Not clicked for the default shots (the bar stayed). |

Phone header (390): wordmark, Book a demo, and Open menu (`aria-label="Open menu"`). Solutions, Use cases, Who we serve, Resources, Pricing, Log in, and EN move into the menu drawer.

## Solutions menu

Stays on the page until a child link is chosen. Each child is a page. Footer of the panel: Book a demo (dialog), Compare Deel (page `/deel-vs-competitors/`), Help center (page `https://help.letsdeel.com/hc/en-gb`, off marketing host, not walked), Close.

| Link | Opens |
|---|---|
| Find your solution in seconds | page `/solutions/discover/` |
| Deel Payroll | page `/solutions/payroll/` |
| Deel HR | page `/solutions/hr/` |
| Deel IT | page `/solutions/it/` |
| Deel Benefits | page `/solutions/benefits/` |
| Deel Hire | page `/solutions/hire/` |
| Deel Mobility | page `/solutions/mobility/` |
| Deel Embedded | page `/solutions/embedded/` |
| Deel's PEO | page `/solutions/payroll/peo/` |
| Employer of Record | page `/solutions/payroll/eor/` |
| Hire Contractors | page `/solutions/payroll/contractors/` |
| Deel Payroll Overview | page `/solutions/payroll/` |
| Deel Security (panel card) | page `/solutions/security` |
| Deel API (panel card) | page `/solutions/open-api/` |

## Use cases menu

| Link | Opens |
|---|---|
| Hire anywhere | page `/use-cases/hire-anywhere` |
| Run payroll globally | page `/use-cases/run-global-payroll/` |
| Run payroll locally | page `/use-cases/run-local-payroll/` |
| Manage a global team | page `/use-cases/manage-global-teams/` |
| Elevate team performance | page `/use-cases/team-performance/` |
| Manage benefits across borders | page `/use-cases/global-benefits/` |
| Ship devices | page `/use-cases/device-shipping/` |
| Run global IT operations | page `/use-cases/global-it-operations/` |
| Set up & manage entity | page `/use-cases/entity-setup` |
| Improve worker experience | page `/use-cases/worker-experience/` |
| Relocate talent | page `/use-cases/relocate-global-workforce/` |
| Customer Stories | page `/case-studies/` |

## Who we serve menu

| Link | Opens |
|---|---|
| Startups | page `/segments/startups/` |
| Mid-Market | page `/segments/mid-market/` |
| Enterprise | page `/segments/enterprise/` |
| HR teams | page `/teams/hr` |
| Finance teams | page `/teams/finance` |
| Legal teams | page `/teams/legal` |
| IT teams | page `/teams/it` |
| Founders | page `/solutions/mobility/immigration/` |
| Crypto | page `/industries/crypto/` |
| Fintech | page `/industries/fintech/` |
| Advertising | page `/industries/advertising/` |
| AI | page `/industries/ai-data-labeling/` |
| BPO | page `/industries/bpo/` |
| Gaming | page `/industries/gaming/` |
| IT | page `/industries/it-services/` |
| Oil & Gas | page `/industries/oil-and-gas/` |
| All industries | page `/industries/` |
| Venture Capital | page `/partner/venture-capital/` |
| Private Equity | page `/partner/private-equity/` |
| Benefit Brokers | page `/partner/brokers/` |
| Accounting | page `/partner/accounting/` |
| Technology | page `/partner/technology/` |
| System Integrators | page `/partner/system-integrators/` |
| Professional Services | page `/partner/professional-services/` |
| Affiliates | page `/partner/affiliates/` |
| Book a demo | dialog (same as header) |
| Compare Deel | page `/deel-vs-competitors/` |
| Help center | page `https://help.letsdeel.com/hc/en-gb` (not walked) |

## Resources menu

| Link | Opens |
|---|---|
| Blog | page `/blog/` |
| Deel Resource Hub | page `/blog/?type=checklist&type=course&type=guide&type=playbook&type=template` |
| Events and webinars | page `/events/` |
| Global hiring guides | page `/hiring/` |
| Help center | page `https://help.letsdeel.com/` (not walked) |
| Partner program | page `/partner/` |
| Careers | page `/careers/` |
| Deel Works | page `/deel-works/` |
| Deel Academy | page `/deel-academy/` |
| Press | page `/press/` |
| Compare Deel | page `/deel-vs-competitors/` |
| Unmatched security | page `/security/` |
| Continuous Compliance | page `/compliance/` (final URL `/solutions/compliance/`) |
| Customer stories | page `/case-studies/` |
| Owned infrastructure | page `/solutions/payroll-engine/` |
| Job description templates | page `/job-description-templates/` |
| Global Hiring Toolkit | page `/global-hiring-toolkit` |
| Global work glossary | page `/glossary/` |
| Misclassification Quiz | page `/misclassification-assessment/` |
| Global Employment Comparison | page `/employment-comparison/` |
| All tools | page `/global-hiring-toolkit/` |

## Language menu

Stays on the page. Not changed. Each child is a locale page of the same marketing site.

| Link | Opens |
|---|---|
| United States - English | page `/` (current) |
| United Kingdom - English | page `/en-gb/` |
| France - Français | page `/fr/` |
| Deutschland - Deutsch | page `/de/` |
| América Latina - Español | page `/es/` |
| España - Español | page `/es-es/` |
| Brasil - Português | page `/pt-br/` (href prefix seen; locale mirrors not walked) |
| Portugal - Português | page `/pt/` |
| Nederland - Nederlands | page `/nl/` |
| Italia - Italiano | page `/it/` |
| 日本 - 日本語 | page `/ja/` |
| 대한민국 - 한국어 | page `/ko/` |
| 中国 - 简体中文 | page `/zh/` |
| 台灣 - 繁體中文 | locale page (not walked) |
| Sverige - Svenska | page `/sv/` |
| Danmark - Dansk | page `/da/` |

Locale mirrors were not walked. The English US tree is the capture.

## Phone menu drawer

Opened by Open menu on `/` at 390. Stays on the page. Close menu closes it.

| Control | Opens |
|---|---|
| Solutions, Use cases, Who we serve, Resources | menu (nested row, chevron). Not expanded in the shot. Children match the desktop menus. |
| Pricing | page `/pricing/` |
| Log in | login wall `https://app.deel.com/login?lang=en` |
| Book a demo | page `/request-a-demo/` (phone bar) or dialog (in-page button) |
| Compare Deel | page `/deel-vs-competitors/` |
| Help center | page `https://help.letsdeel.com/hc/en-gb` (not walked) |
| EN | menu (language list). Not changed. |

## Home page controls

| Control | Opens |
|---|---|
| Hire anywhere, Run payroll, Secure visas, Manage HR & people, Ship equipment | menu (intent chips on the hero). They stay on `/`. Not used to start a flow. |
| Book a demo (hero and lower) | dialog. Not filled. |
| 175 STORIES | page `/case-studies/` |
| Product cards (Payroll, HR, IT, Benefits, Hire, Mobility) | page, the matching `/solutions/` URL |
| Deel Payroll / Deel HR / Deel IT / Deel Hire (speed section) | menu (tabs on the same URL) |
| Get your AI readiness score | login wall `https://lead.akai.run/login`. Off-site. Branch stopped. Not typed. |
| Learn more about payroll | page `/use-cases/run-global-payroll/` |
| Learn more about Deel AI | page `/hr-platform/ai/` |
| Learn more Deel's Payroll Engine | page `/solutions/payroll-engine/` |
| Play video | dialog or media on the same URL. Not played. |
| Read case study | page `/case-studies/<slug>` (carousel). Listing confirmed 200. Individual stories not treated as a second system. |
| Go to item 1–8 | menu (carousel dots) |
| Previous slide / Next slide | menu |
| Footer Email subscribe | text field. Not typed. Not submitted. |

## Pricing page

`/pricing/` (200).

| Control | Opens |
|---|---|
| Hire, Manage, Pay, Equip, Bundle | menu (tabs on the same URL). Hire is selected on arrival. |
| Book a demo | dialog. Not filled. |
| Plan cards and MOST POPULAR badge | stay on the page. Get started / Book a demo on a plan opens the demo dialog or the login wall. Not followed into the app. |

## Demo page and demo dialog

`/request-a-demo/` is a public page (200). Header Book a demo opens a dialog on the current URL (`?form=`). Both show work email, first name, and last name. Not filled. Continue and Choose a date & time were not pressed.

## Login wall

`https://app.deel.com/login` (and `?lang=en` from the marketing Log in link). Branch stopped.

| Control | Opens |
|---|---|
| Deel app (desktop) | not clicked. Would leave the page for the app. |
| SSO | not clicked. |
| Google | not clicked. |
| Email, Password | fields present. Not typed. |
| Log in (submit) | not pressed. |
| Create account | `https://app.deel.com/signup`. Not opened. |
| Forgot password, Having trouble logging in | not followed. |
| Need help? | not followed. |
| En (login locale) | menu. Not changed. |

Phone login wall at 390 shows SSO, Google, Email, Password, Log in, and Create account. Deel app was not in the phone viewport shot. None of those controls were used.

## Footer (marketing pages)

| Link | Opens |
|---|---|
| About us | page `/about/` |
| Leadership team | page `/leadership-team/` |
| Careers | page `/careers/` |
| Pricing | page `/pricing/` |
| Find your solution | page `/solutions/discover/` |
| AI at Deel | page `/solutions/ai` |
| Deel Payroll, HR, IT, Benefits, Hire, Mobility | page, matching `/solutions/` URL |
| Deel Security | page `/solutions/security` |
| Deel Embedded | page `/solutions/embedded/` |
| Deel Services | page `/solutions/services/` |
| EOR | page `/solutions/payroll/eor/` |
| PEO | page `/solutions/payroll/peo/` |
| HR Platform | page `/hr-platform/` |
| White Label | page `/hr-platform/white-label/` |
| Deel API | page `/solutions/open-api/` |
| Integrations | page `/integrations/` |
| Workflows | page `/hr-platform/workflows/` |
| Akai | page `https://www.akai.run/` (off-site, not walked) |
| Platform Status | page `https://status.deel.com/` (not walked) |
| Built on in-house infrastructure | page `/solutions/payroll-engine/` |
| Customer stories | page `/case-studies/` |
| Compare Deel | page `/deel-vs-competitors/` |
| Security | page `/security/` |
| Trust Center | page `https://trust.deel.com/` (not walked) |
| Become a partner | page `/partner/` |
| Become an affiliate | page `/partner/affiliates/` |
| G2 customer reviews | page `https://www.g2.com/products/deel/reviews` (off-site, not walked) |
| Blog | page `/blog/` |
| Templates And Guides | page `/blog/?type=template&type=guide` |
| Global Hiring Guides | page `/hiring/` |
| Webinars & Events | page `/events/` |
| Global Work Glossary | page `/glossary/` |
| Deel Impact | page `/deel-impact/` |
| Job Description Templates | page `/job-description-templates/` |
| Free HR tools | page `/global-hiring-toolkit` |
| API Documentation | page `https://developer.deel.com/home` (not walked) |
| Help Center | page `https://help.letsdeel.com/hc/en-gb` (not walked) |
| Press | page `/press/` |
| Social (X, LinkedIn, Facebook, Instagram) | off-site. Not walked. |
| Email subscribe | field. Not submitted. |
| Privacy, Disclaimer, Cookie Settings, Legal Hub, Whistleblower, Disclosures, Licenses | page under `/legal/` or `/privacy/`. Cookie Settings reopens Cookiebot. Not answered. |

## Confirmed public pages (200)

The crawl loaded 86 marketing URLs and stopped at login or app hosts. Representative paths, all 200:

`/`, `/pricing/`, `/request-a-demo/`, `/plp/peo/`, `/about/`, `/leadership-team/`, `/careers/`, `/press/`, `/blog/`, `/events/`, `/hiring/`, `/glossary/`, `/case-studies/`, `/deel-vs-competitors/`, `/deel-works/`, `/deel-academy/`, `/deel-impact/`, `/security/`, `/compliance/` (lands on `/solutions/compliance/`), `/solutions/discover/`, `/solutions/payroll/`, `/solutions/hr/`, `/solutions/it/`, `/solutions/benefits/`, `/solutions/hire/`, `/solutions/mobility/`, `/solutions/embedded/`, `/solutions/payroll/peo/`, `/solutions/payroll/eor/`, `/solutions/payroll/contractors/`, `/solutions/payroll-engine/`, `/solutions/ai`, `/solutions/security`, `/solutions/services/`, `/solutions/open-api/`, `/solutions/mobility/immigration/`, `/use-cases/hire-anywhere`, `/use-cases/run-global-payroll/`, `/use-cases/run-local-payroll/`, `/use-cases/manage-global-teams/`, `/use-cases/team-performance/`, `/use-cases/global-benefits/`, `/use-cases/device-shipping/`, `/use-cases/global-it-operations/`, `/use-cases/entity-setup`, `/use-cases/worker-experience/`, `/use-cases/relocate-global-workforce/`, `/segments/startups/`, `/segments/mid-market/`, `/segments/enterprise/`, `/teams/hr`, `/teams/finance`, `/teams/legal`, `/teams/it`, `/industries/`, `/industries/crypto/`, `/industries/fintech/`, `/industries/advertising/`, `/industries/ai-data-labeling/`, `/industries/bpo/`, `/industries/gaming/`, `/industries/it-services/`, `/industries/oil-and-gas/`, `/partner/`, `/partner/venture-capital/`, `/partner/private-equity/`, `/partner/brokers/`, `/partner/accounting/`, `/partner/technology/`, `/partner/system-integrators/`, `/partner/professional-services/`, `/partner/affiliates/`, `/hr-platform/`, `/hr-platform/white-label/`, `/hr-platform/workflows/`, `/hr-platform/ai/`, `/integrations/`, `/job-description-templates/`, `/global-hiring-toolkit`, `/misclassification-assessment/`, `/employment-comparison/`, `/legal/`, `/legal/privacy-policy/`, `/legal/disclaimer/`, `/legal/whistleblower-policy/`, `/privacy/`.

Blog posts, glossary entries, individual case studies, and country hiring guides are further public pages of the same shell. They were not each screenshotted. A later queue of about 227 same-host URLs was left after the 86-page pass, mostly those deep listings.

## Login walls and hosts not walked

| URL | Why the branch stopped |
|---|---|
| `https://app.deel.com/login` | Login wall. Email and password visible. Not typed. |
| `https://app.deel.com/login?lang=en` | Same wall, from the marketing Log in link. |
| `https://app.deel.com/signup` | Create account. Not opened. |
| `https://app.deel.com/` and other `app.deel.com` paths (`/start/hire`, `/it/public_catalog`, `/help/messages`, `/deel-academy`, `/mobility/self-serve/chat`) | App host. Not entered. |
| `https://app.demo.deel.com/` | Demo app host. Not entered. |
| `https://lead.akai.run/login` | AI readiness score. Login wall. Not typed. |
| `https://marketplace.deel.com/` and app listing URLs | Separate host. Integrations page on www.deel.com was loaded (search field, not submitted). Marketplace host not walked. |
| `https://developer.deel.com/home` | Docs host. Not walked. |
| `https://help.letsdeel.com/` | Help host. Not walked. |
| `https://status.deel.com/`, `https://trust.deel.com/`, `https://events.deel.com/`, `https://lab.deel.com/` | Other Deel hosts. Not walked. |
| Social, G2, Akai marketing (`www.akai.run`) | Off-site. Not walked. |
