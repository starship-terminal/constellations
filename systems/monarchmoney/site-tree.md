# Monarch Money public site tree

Mapped on 2026-11-21 from the homepage before any package screenshot, in headless Chromium at 1440 x 900. The brief URL `https://www.monarchmoney.com/` returns HTTP 301 to `https://www.monarch.com/`. The live marketing host is `www.monarch.com`. The signed-in product lives on `app.monarch.com` and was not entered.

Cookie banner: an Osano dialog ("This site uses technologies such as cookies…") is present on first paint. Close is a button (`aria-label="Close this consent banner"`) that is not inside a `<form>`. Accept All, Reject Non-Essential, and Save are also buttons, not form submits. This capture hides the banner with CSS and does not click Accept, Reject, or Save. Cookie Preferences reopens the same dialog. Storage Preferences is an in-page anchor.

No dark theme switch exists on the public site. `color-scheme` on the document is `normal`. Body paints cream `rgb(253, 248, 237)` with text `rgb(34, 32, 29)` in ABC Oracle.

## Header (every marketing page)

| Control | Opens |
|---|---|
| Logo (Home) | `/` |
| Features (button, Radix menu, `aria-expanded`) | Mega menu, not a new page. Cards link to `/features/tracking`, `/features/budgeting`, `/features/planning`. Close with Escape. |
| For Couples | `/for-couples` |
| For Professionals | `/for-professionals` |
| Pricing | `/pricing` |
| Download | `/download` |
| Sign in | `https://app.monarch.com/login` (login wall: password field). Branch stops. |
| Sign up | `https://app.monarch.com/signup` or `https://app.monarch.com/quiz/onboarding` (signup / onboarding wall). Branch stops. |
| Open menu (phone, `aria-label="Open menu"`) | Mobile nav drawer with the same destinations. |

## Features menu

| Card | Opens |
|---|---|
| Tracking | `/features/tracking` |
| Budgeting | `/features/budgeting` |
| Planning | `/features/planning` |

## Homepage `/`

| Control | Opens |
|---|---|
| Promo strip "Get 30% OFF…" | Text only. Code is published on `/promo-codes`. Not a form. |
| Unlock better money habits, Get started today | Signup wall (`app.monarch.com/quiz/onboarding`). Stop. |
| Track, Budget, Collaborate, Plan | In-page tab buttons. They swap the feature panel. They do not navigate. |
| Learn more (tracking, budgeting, planning) | `/features/tracking`, `/features/budgeting`, `/features/planning` |
| Learn more (collaborate) | `/for-couples` |
| Press logos (WSJ, ZDNet, Elite Daily, Forbes, The Cut, USA Today) | External articles. Not captured. |
| r/monarchmoney, Read now | External Reddit, or `/blog` |
| View pricing | `/pricing` |
| App Store, Google Play | External store listings. Not captured. |

## Feature, audience, and pricing pages

| Page | In-page controls | Walls |
|---|---|---|
| `/features/tracking` | FAQ accordions (How is my net worth calculated?, How do I customize my dashboard?, How does Monarch define what shows up on my Recurring page?) | Get started links go to signup. Stop. |
| `/features/budgeting` | Flex Budgeting / Category Budgeting tabs. FAQ accordions. | Signup wall. |
| `/features/planning` | FAQ accordions. | Signup wall. |
| `/for-couples` | FAQ accordions. | Signup wall. |
| `/for-professionals` | Audience tabs: Financial Advisors, Money Coaches, Tax Professionals, Estate Planning Attorneys. How can we help? FAQ. Let's go. | Let's go and sign-up CTAs go to `/for-professionals/sign-up` (public form). Not submitted. |
| `/for-professionals/sign-up` | Professional signup form (profile fields). | Not filled. Not submitted. Recorded as a wall for profile fields. |
| `/pricing` | Comparison rows are buttons that expand category copy (Tracking, Budgeting, Planning & forecasting, Small business tracking, Guidance & insights, Connectivity & integrations, Access & collaboration). FAQ accordions. | Try Monarch free for 7 days and Sign up go to `app.monarch.com/signup`. Stop. |
| `/download` | Store badges. | External stores. No account form. |
| `/canada` | Marketing page. | Signup wall on CTAs. |
| `/promo-codes` | Published promo copy. | Signup wall on CTAs. |
| `/compare/mint-alternative` | FAQ accordions. | Signup wall. Same pattern on `/compare/ynab-alternative`, `/compare/simplifi-alternative`, `/compare/credit-karma-alternative`. |
| `/for-employers` | Redirects to `/` (200 after redirect). Dead nav target. | None beyond the homepage. |

## Tools and directories

| Page | Controls | Stop rule |
|---|---|---|
| `/calculators` | Index cards to the three calculators. | None. |
| `/calculators/financial-health-calculator` | Previous / Next steps through a quiz. | No account fields. Steps are public interactions. |
| `/calculators/debt-payoff-calculator` | Loan fields, Add a loan, strategy menu (Avalanche), Calculate. | Local calculator. Not submitted to a server. Fields left empty. Strategy menu opened. |
| `/calculators/mortgage-calculator` | Term control (30-year fixed), Advanced disclosure. | Local calculator. Fields left empty. Advanced opened. |
| `/professional-directory` | Filter chips: All, Featured, Financial Planner, Investment Advisor, Money Coach, Tax Professional, CFP. Read more expands a listing. Fee buttons (`aria-haspopup="dialog"`): Project-based, Hourly, Ongoing. | Listings are published. No search field filled. Dialogs opened and closed. |
| `/personal-finance-term-glossary` | Category chips (All, Budgeting, Credit, Loans & Debt, Banking, Investing, Retirement, Student Loans, Taxes, Insurance, Real Estate, Planning, Monarch). Read more expands a definition. | Public. |
| `/connection-status` | Public bank-connection status page. | No login. |
| `/whats-new` | Previous Page / Next Page. | Public changelog. |
| `/blog` | Previous Page / Next Page. Article cards. | One article captured as the article pattern. Remaining sitemap posts are the same template. |

## Company and legal

| Page | Notes |
|---|---|
| `/about` | Team filter chips: All, Operations, Design, Engineering, Customer Success, People, Advice & Planning, Data, Marketing, Finance. |
| `/careers` | Filter menus: All departments, All locations, All employment types. Job links leave to the applicant host. Those hosts are recorded and not filled. |
| `/press` | Press page. External coverage links not followed. |
| `/security` | FAQ accordions. Trust Center link is external. |
| `/privacy`, `/terms`, `/copyright`, `/referralprogramterms`, `/giftprogramterms`, `/policy-dec-2025`, `/AI-connector-privacy`, `/privacy-opt-out` | Legal documents. Same shell. Privacy and terms captured as the legal pattern. |
| `/opt-out-request-form` | Form: first name, last name, email, checkbox, Submit. Profile and contact fields. Not filled. Not submitted. |

## Footer (every marketing page)

| Link | Opens |
|---|---|
| Tracking, Budgeting, Planning | Feature pages above |
| vs. YNAB, vs. Simplifi, vs. Credit Karma, vs. Mint | `/compare/ynab-alternative`, `/compare/simplifi-alternative`, `/compare/credit-karma-alternative`, `/compare/mint-alternative` |
| Financial Health Calculator, Debt Payoff Calculator, Mortgage Calculator | Calculator pages above |
| What's New, Bank Connections, Professional Directory, Monarch in Canada | Pages above |
| Terms of Use, Privacy Policy, Promo Codes, Blog, About, Careers, Press | Pages above |
| Partnerships | `https://monarchmoney.qualtrics.com/jfe/form/SV_3FbqJ9e4CBRDd5Q` (survey). Stop. Not filled. |
| Privacy and Security | `/security` |
| Help Center | `https://help.monarch.com/hc/en-us` (external help). Not captured as product UI. |
| System Health | `https://status.monarch.com/` (external status). Not captured. |
| Contact | A mailto link to the published support contact. Not opened. The address is not written in this package. |
| Cookie Preferences | Reopens the Osano dialog. Closed without saving. |
| Do Not Sell or Share My Personal Information | `/opt-out-request-form` |
| App Store, Google Play, X, Reddit, YouTube, LinkedIn, Instagram | External. Not captured. |

## Login and signup walls (branch stops)

| URL | What it asks | Action |
|---|---|---|
| `https://app.monarch.com/login` | Password (known wall). | Recorded. Not entered. |
| `https://app.monarch.com/signup` | Account creation. | Recorded. Not entered. |
| `https://app.monarch.com/quiz/onboarding` | Onboarding quiz. | Recorded. Not entered. |
| `/for-professionals/sign-up` | Professional profile form. | Page recorded. Fields not filled. Not submitted. |
| `/opt-out-request-form` | Name, email, checkbox. | Page recorded. Fields not filled. Not submitted. |
| Qualtrics partnerships form | Survey. | Recorded. Not opened for entry. |

## Sitemap posts not walked as unique screens

`https://www.monarch.com/sitemap.xml` lists 198 URLs (fetched 2026-11-21). About 150 are `/blog/<slug>` posts on the same article template. One post is captured. The rest are the same pattern, listed in `raw/sitemap-paths.txt`, not re-shot.
