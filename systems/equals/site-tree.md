# Equals public site tree

Walked on 2026-11-21 from [https://equals.com/](https://equals.com/) in Playwright. Desktop shots are 1440×900 at 2x, except the open Use cases menu, which is 1600×1000 so the panel fits. Phone shots are 390×844 at 2x. Signed out. No form was submitted. No email, name, password, or code was typed. No identity provider was clicked.

`https://equals.app/` redirects to `https://equals.com/` (200, title "Trusted AI analytics | Equals"). Screenshot: [equals-app-redirect-light-default.png](screenshots/equals-app-redirect-light-default.png).

The marketing site is one public site. Header and footer repeat. Search is not on the marketing pages. Docs search is a separate host, recorded below and not submitted.

## Auth wall

These controls leave the public site. The walk recorded the URL and stopped. Nothing was typed. Continue was not pressed. Request a demo was not clicked.

| Control | Where | Opens |
|---|---|---|
| Sign in | Desktop header | `https://go.equals.com/`, which redirects to `https://go.equals.com/auth/new` |
| Continue | Sign-in wall | Same page. Not pressed. |
| Request a demo | Sign-in wall | `https://equals.com` (href only; not clicked) |

`https://equals.app/login` redirects to `https://equals.com/login` and returns 404, title "Page not found", body "Page not found". Screenshot: [login-404-light-default.png](screenshots/login-404-light-default.png).

The wall that painted is [signin-wall-light-default.png](screenshots/signin-wall-light-default.png) and [mobile-signin-wall-light-default.png](screenshots/mobile-signin-wall-light-default.png). Fields and the stop are in [login-review.json](login-review.json).

There is no Google, Apple, or other identity-provider button on the empty wall.

## Cookie control

No cookie banner painted. Nothing was accepted.

## Desktop header (1440×900)

Present on the marketing pages. Screenshot: [home-light-default.png](screenshots/home-light-default.png).

On `/pricing/`, `/about/`, `/customers/`, `/launches/`, and `/use-cases/` the Use cases item is still in the header. The home shot is the one that shows every desktop header control together.

| Control | Opens |
|---|---|
| Logo (Equals home) | `/` |
| Use cases | Hover menu. Screenshot: [home-light-menu.png](screenshots/home-light-menu.png) at 1600×1000 |
| Pricing | `/pricing/` |
| About | `/about/` |
| Sign in | Auth wall. Stop. |
| Enter email + Get a demo | A form. Not typed. Not submitted. |

### Use cases menu

Three groups. Each item is a public page. One representative, ARR Dashboard, was opened. The other 22 were not each photographed. Phone lists the same links at `/use-cases/`.

| Group | Item | Opens |
|---|---|---|
| Revenue and Retention | ARR Daily Pulse | `/use-cases/arr-daily-pulse/` |
| Revenue and Retention | ARR Dashboard | `/use-cases/arr-dashboard/` |
| Revenue and Retention | ARR Spreadsheet | `/use-cases/arr-spreadsheet/` |
| Revenue and Retention | Average Contract Value | `/use-cases/acv/` |
| Revenue and Retention | Customer Dashboard | `/use-cases/customer-dashboard/` |
| Revenue and Retention | Customer Retention Cohorts | `/use-cases/customer-retention-cohorts/` |
| Revenue and Retention | Net Revenue Retention | `/use-cases/nrr/` |
| Revenue and Retention | Operating Model Dashboard | `/use-cases/operating-model-dashboard/` |
| Revenue and Retention | Retention Dashboard | `/use-cases/retention-dashboard/` |
| Sales Pipeline and Funnel | Deal Size and Velocity | `/use-cases/deal-size-and-velocity/` |
| Sales Pipeline and Funnel | Paid Campaign Performance | `/use-cases/paid-campaign-performance/` |
| Sales Pipeline and Funnel | Pipeline Creation | `/use-cases/pipeline-creation/` |
| Sales Pipeline and Funnel | Pipeline Movement Waterfall | `/use-cases/pipeline-movement-waterfall/` |
| Sales Pipeline and Funnel | Sales Conversion Rates | `/use-cases/sales-conversion-rates/` |
| Sales Pipeline and Funnel | Sales Daily Pulse | `/use-cases/sales-daily-pulse/` |
| Sales Pipeline and Funnel | Sales Pacing vs Historicals | `/use-cases/pacing-vs-historicals/` |
| Sales Pipeline and Funnel | Sales Pipeline Dashboard | `/use-cases/sales-pipeline-dashboard/` |
| Sales Pipeline and Funnel | Website Traffic Dashboard | `/use-cases/website-traffic-dashboard/` |
| Team and Customer Management | Customer Health Score | `/use-cases/customer-health-score/` |
| Team and Customer Management | Sales Commission Calculator | `/use-cases/sales-commission-calculator/` |
| Team and Customer Management | Sales Forecast Dashboard | `/use-cases/sales-forecast-attainment/` |
| Team and Customer Management | Sales Rep Performance | `/use-cases/sales-rep-performance/` |
| Team and Customer Management | Upcoming Renewals | `/use-cases/upcoming-renewals/` |

## Phone header (390×844)

Closed: logo and a menu control. Screenshot: [mobile-home-light-default.png](screenshots/mobile-home-light-default.png).

Open drawer. Screenshot: [mobile-home-light-drawer.png](screenshots/mobile-home-light-drawer.png).

| Control | Opens |
|---|---|
| Close (×) | Closes the drawer |
| Home | `/` |
| Use cases | `/use-cases/` |
| Pricing | `/pricing/` |
| About | `/about/` |
| Enter your work email + Get a demo | A form. Not typed. Not submitted. |

Sign in is not in the phone drawer. It is a desktop header link.

## Footer

Same on the marketing pages. LinkedIn, X, and Status are external and were not walked.

| Column | Control | Opens |
|---|---|---|
| Guides | The Ultimate Guide to ARR | `/guides/arr/` |
| Guides | The Guide to SaaS Metrics | `/guides/saas-metrics/` |
| Product | Customers | `/customers/` |
| Product | Launches | `/launches/` |
| Product | Pricing | `/pricing/` |
| Product | Use cases | `/use-cases/` |
| Company | About | `/about/` |
| Company | Help docs | `https://docs.equals.com` |
| Company | LinkedIn | `https://www.linkedin.com/company/equalshq/` (not walked) |
| Company | X | `http://twitter.com/heyequals` (not walked) |
| Legal | Privacy Policy | `/policies/privacy-policy.pdf` (not opened) |
| Legal | Terms & Conditions | `/policies/equals-online-terms-and-conditions-GP-april-11-22.pdf` (not opened) |
| Legal | Status | `https://status.equals.com` (not walked) |

## Pages opened

Each marketing index returned 200. `/login` returned 404. The sitemap lists 179 URLs on equals.com: 118 launch notes, 50 guides, 6 customer stories, plus the index pages. Individual launch notes, guide chapters, and customer stories were not each photographed.

| Path | In-page controls | Package shot |
|---|---|---|
| `/` | Hero email field and Get a demo. Not submitted. Logo row is not a set of links. | home, mobile-home |
| `/pricing/` | Three plan cards (Essential, Business, Enterprise), each with an email field and Get a demo. Not submitted. | pricing, mobile-pricing |
| `/about/` | Body links, including an external "a bicycle of the mind" link. Not followed. | about |
| `/customers/` | Read case study links to customer stories. Index only. | customers |
| `/launches/` | Cards such as "Improvements and fixes" under October 2026. Index only. | launches |
| `/use-cases/` | The same 23 use-case links as the menu. | usecases, mobile-usecases |
| `/use-cases/arr-dashboard/` | See all use cases returns to `/use-cases/`. Connector chips (Stripe, Sequence, Salesforce, HubSpot) are labels on a public demo, not the app. Email field and Get a demo not submitted. | usecase |
| `/guides/arr/` | Start reading scrolls the guide. Created by Equals returns home. Not submitted. | guide-arr |
| `/guides/saas-metrics/` | Same splash shape as the ARR guide. | guide |
| `https://docs.equals.com/` | Search and Ask Assistant are on the page. Neither was typed into or submitted. The analyst panel is a public demo. | docs |
| `https://equals.com/login` | 404. No form. | login-404 |
| `https://go.equals.com/auth/new` | Auth wall. Stop. | signin-wall, mobile-signin-wall |

## Not captured

- Signed-in workbook, dashboards, settings, and onboarding. The wall stops at an email field.
- Signup does not have its own wall on the empty sign-in page. Request a demo points at `https://equals.com` and was not clicked.
- Dark theme on marketing and sign-in. Docs can flip theme; this pass did not click the theme control, so a fresh dark docs shot was not taken.
- The other 22 use-case pages, launch notes, guide chapters, and customer stories share the header, footer, and a demo email field. They were mapped, not each photographed.
- Token values that this pass did not read stay Not captured. Older readings in `tokens.json` are from 2026-11-13.
