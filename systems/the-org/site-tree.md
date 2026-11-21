# The Org site tree

Mapped from https://theorg.com/ on 2026-11-21 in headless Chromium before any package screenshot. Public marketing and directory pages returned HTTP 200. Login, signup, and account branches were recorded and not followed. Pages that expose an email address were mapped and not screenshotted.

Nothing was typed. No password, email, code, or form was submitted. Google, Apple, and Microsoft were not clicked. Continue with Google was not used.

## Header (desktop 1440)

| Control | Opens |
|---|---|
| Logo | https://theorg.com/ |
| Platform (button, `aria-expanded`) | Dialog: For Companies, For Candidates, For Professionals |
| Enrich (button, `aria-expanded`) | Dialog: Browser Extension, CRM Enrichment, MCP Connectors, Developer Portal |
| Pricing | https://theorg.com/pricing |
| Log in | https://theorg.com/login (wall; stop) |
| Sign up | https://theorg.com/signup (wall; stop) |

Platform dialog links:

| Link | Page |
|---|---|
| For Companies | https://theorg.com/for-companies |
| For Candidates | https://theorg.com/for-candidates |
| For Professionals | https://theorg.com/for-professionals |

Enrich dialog links:

| Link | Page |
|---|---|
| Browser Extension | https://theorg.com/browser-extension |
| CRM Enrichment | https://theorg.com/crm-enrichment |
| MCP Connectors | https://theorg.com/mcp-connectors |
| Developer Portal | https://theorg.com/developer-portal |

## Header (phone 390)

Platform, Enrich, Pricing, Log in, and Sign up are in the DOM with zero box size. A 32 by 32 button in the header (no accessible name) is the phone menu trigger. Opening it reveals the same Platform and Enrich destinations plus Pricing, Log in, and Sign up. Log in and Sign up stop the branch.

## Home

https://theorg.com/

| Control | Opens |
|---|---|
| Start for free | https://theorg.com/signup (wall; stop) |
| Learn more | https://theorg.com/learn-more |
| Company card (trending) | https://theorg.com/org/{slug} (public org chart; offices checked before screenshot) |
| Industry chip | https://theorg.com/explore/industries/{slug} |
| City, country chip | https://theorg.com/explore/countries/{slug} |
| Employee-range chip | https://theorg.com/explore/employee-ranges/{slug} |
| Extra-industry `+N` button | Popover of more industry links (same explore pattern) |
| Explore more | https://theorg.com/explore |
| Article card | https://theorg.com/iterate/{slug} |
| View more | https://theorg.com/iterate |

No search field on the home page. No theme switch. Painted theme is light (`color-scheme: normal`, page background `rgb(253, 252, 252)`).

## Marketing pages (public)

| Path | What it is |
|---|---|
| /learn-more | Product overview; links onward to the three Platform pages |
| /for-companies | Audience page. Get Started goes to signup (wall; stop) |
| /for-candidates | Audience page. Get Started goes to signup (wall; stop) |
| /for-professionals | Audience page. Get Started goes to signup (wall; stop) |
| /browser-extension | Chrome and Edge install links (external stores; not followed) |
| /crm-enrichment | HubSpot and Salesforce install links (external; not followed) |
| /mcp-connectors | Connect to ChatGPT / Connect to Claude (external connector flows; not followed) |
| /developer-portal | Developer marketing. Portal login not entered |
| /employer-branding | Solution page |
| /professional-networking | Solution page |
| /job-discovery | Solution page |
| /solutions | Data product page. Free Trial goes to signup (wall). Contact sales opens a sales form (not filled, not submitted, not screenshotted) |
| /about | Mission page. Named staff link to `/org/theorg/person/{slug}` (person pages are a stopped branch) and investor orgs |
| /trust | Trust Center. No form |
| /pricing | Plan cards. Yearly / Monthly is a billing toggle (local, no submit). Get started goes to signup (wall). Contact sales opens a form with first name, last name, company, work email, job title, and message (not filled, not submitted, not screenshotted) |

## Directory and content (public)

| Path | What it is |
|---|---|
| /explore | Hub: countries, industries, employee ranges |
| /explore/countries | Index plus a search field (typed nothing) |
| /explore/industries | Index plus a search field (typed nothing) |
| /explore/employee-ranges | Index plus a search field (typed nothing) |
| /explore/countries/united-states | Filtered company list (representative country) |
| /explore/industries/information-technology | Filtered company list (representative industry) |
| /explore/employee-ranges/10-50 | Filtered company list (representative range) |
| /companies | A to Z index (`/companies/a-1` and siblings) |
| /companies/a-1 | Letter page of company links (representative) |
| /people-directory | A to Z index (`/people-directory/a-1` and siblings). Person targets are a stopped branch |
| /iterate | Blog index and category links |
| /iterate/categories/executive-moves | Category index (representative) |
| /iterate/executive-moves-you-should-know-about-february-18-2026 | One article (representative) |
| /org/five-blocks | Public org chart (representative small company). Tabs: Org chart, Teams, Offices. Offices text had no email, phone, or street match, so the page is in the shot list. Follow did not navigate and opened no dialog |
| /org/google | Public org chart (representative large company). Same tab pattern |

Company card links such as Follow, and any control whose `href` is `/login` or `/signup`, are walls. `/prospect/people` and `/prospect/jobs` redirect to https://theorg.com/login. Stop.

## Footer

| Link | Destination |
|---|---|
| About | /about |
| Contact | /contact (emails on the page; mapped, not screenshotted) |
| Blog | https://blog.theorg.com/ (separate host; not captured) |
| Solutions | /solutions |
| Trust | /trust |
| Pricing | /pricing |
| Companies | /companies |
| People | /people-directory |
| Employer Branding | /employer-branding |
| Professional Networking | /professional-networking |
| Job Discovery | /job-discovery |
| Terms | /terms |
| Privacy | /privacy |
| Do not sell my info | /do-not-sell (email on the page; mapped, not screenshotted) |
| X, LinkedIn, Facebook, Instagram | External profiles; not followed |

## Stopped branches

| URL | Why the branch stops |
|---|---|
| https://theorg.com/login | Email and password fields, plus Google, Microsoft, passkey, and SSO. Known probe confirmed. Password was not submitted |
| https://theorg.com/signup | Work email field and Google / Microsoft. Email was not typed |
| https://theorg.com/forgot-password | Email field. Not typed |
| https://theorg.com/login/sso | Email field. Not typed |
| https://theorg.com/prospect/people | Redirects to /login |
| https://theorg.com/prospect/jobs | Same login wall pattern as people search |
| https://theorg.com/contact | Published sales and press email addresses on the page. FAQ accordion is public, but the page is not screenshotted |
| https://theorg.com/do-not-sell | Email address on the page. Not screenshotted |
| https://theorg.com/org/{slug}/person/{slug} | Headless Chromium stayed on "Verify to continue / Confirm you are a person to view this profile." Not a captcha solve. Not screenshotted. Treated as a person page that must not be captured |
| Contact sales form on /pricing and /solutions | Name, company, work email, job title, message. Not filled, not submitted, not screenshotted |
| External store, CRM, and chatbot connect buttons | Leave theorg.com. Not followed |

## Not present on the public surface

- Dark theme toggle
- Toast, checkbox, radio, switch, select, or text area on the pages that were opened
- Signed-in app shell, credits, seats, or org-chart editing
