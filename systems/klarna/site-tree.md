# Klarna public site tree

Mapped from https://klarna.com on 2026-11-21, signed out, before the screenshot pass. The request redirected to https://www.klarna.com/international/. That page is the country picker ("Klarna International"). The design surface is the US market at https://www.klarna.com/us/. This is a live marketing site, not a parked domain and not a captcha wall.

Headless Chromium received "403 Access Denied" on www.klarna.com. Headed Chromium loaded the public pages. The T3 preview tab also loaded `/international/` (`title` "Klarna International | Safe & easy-to-use payment solutions") but could not take screenshots: "The browser is not producing screenshot frames."

There is no theme switch on the public marketing pages. A dark Klarna UI sheet is declared in CSS and is not painted here. The only region control is the header button "EN" (`aria-label` "Select language"). It opens a dialog of market links. Confirm was not submitted. No email was typed. No password was typed. No phone was typed. No form was submitted. No identity provider was clicked.

Sign up points at app.klarna.com. Sign in points at app.klarna.com/login. Both opened the same empty wall, "Select your main country of residence". No country was chosen. The query strings are not stored. Login extraction is not started.

## Utility strip

Sits above the header on `/us/`.

| Control | Opens | Stop? |
|---|---|---|
| Phishing warning | Text plus a link to `/us/phishing-and-scams/` | |
| close announcement | Closes the strip on the same page. Does not navigate. | |

## Header (US, 1440)

The wordmark is a link labelled "Klarna". Category labels are links. At 1440 the hamburger is in the DOM and not visible. Search is an input in the header, placeholder "Search for any product or brand".

| Control | Opens | Stop? |
|---|---|---|
| Klarna | `/us/` | |
| Discover Klarna | `/us/what-is-klarna/` | |
| Shop | `/us/shopping/` | |
| App | `/us/klarna-app/` | |
| Help | `/us/help/` | |
| For shoppers | `/us/` | |
| For business | `/international/enterprise/` | |
| Search field | Suggestion menu on the same page: Clothing, Nike, Shoes, Apple. Does not navigate until a row is chosen. Nothing was typed. Nothing was submitted. | |
| Select language (shows "EN") | Dialog "Choose your region and language". Region and Language are selects. Confirm was not submitted. | |
| Sign up | `https://app.klarna.com/` | yes, account wall |
| Sign in | `https://app.klarna.com/login` | yes, account wall |

## Phone header (390)

| Control | Opens | Stop? |
|---|---|---|
| Open navigation menu (pink) | Drawer on the same page. | |
| Klarna | `/us/` | |
| Search | Search overlay. Not submitted. | |
| Account | `https://app.klarna.com/login` | yes |

## Navigation drawer (390)

| Item | Opens | Stop? |
|---|---|---|
| Discover Klarna | `/us/what-is-klarna/` | |
| Shop | `/us/shopping/` | |
| App | `/us/klarna-app/` | |
| Help | `/us/help/` | |
| For business | `/international/enterprise/` | |
| English | Same region dialog as Select language. Confirm was not submitted. | |

## Search menu

Focusing the header search opens a menu. Rows seen, not followed: Clothing (category), Nike (brand), Shoes (category), Apple (brand). The field was left empty.

## Language dialog

Title: "Choose your region and language". Buttons: close, Confirm. Confirm was not clicked. Region shows United States. Language shows English. The closed page also lists market links. A sample:

| Item | Opens |
|---|---|
| English (en-US) | `/us/` |
| Español (es-US) | `/us/es/` |
| English (en-GB) | `/` |
| English (en-CA) | `/ca/` |
| Deutsch (de-DE) | `/de/` |
| English (en-AU) | `/au/` |

The full list also includes AT, BE, CZ, DK, FI, FR, GR, HU, IE, IT, NL, NO, PL, PT, RO, SK, ES, SE, CH, MX, CN, JP, NZ, KR, and the second language of several of those markets. Choosing one would change the market. None was chosen.

## Homepage sections

These are in-page links on `/us/`, not a second nav.

| Control | Opens | Stop? |
|---|---|---|
| Get the app | `/us/klarna-app/` | |
| Shop now | `/us/shopping/` | |
| Shop deals | `/us/shopping/c/black-friday/` | |
| Learn more (campaign) | `/us/campaign-app/` | |
| Pay at checkout | `/us/payments/` | |
| See Klarna Cards | `/us/all-cards/` | |
| Explore memberships | `/us/memberships/` | |
| Learn more (account) | `/us/personal-account/` | |
| Explore savings | `/us/savings-account/` | |
| Explore cashback | `/us/cashback/` | |
| Sign up (mobile plan) | `/us/mobile-plan/` | marketing page, not the app wall |
| How Apple Pay works | `/us/klarna-apple-pay/` | |
| buyer protection | `/us/buyer-protection/` | |
| Learn more about security | `/us/security/` | |
| 634,429 reviews | trustpilot.com/review/klarna.com | external, not followed |

## Footer

The footer is an ink band at the bottom of `/us/`. Three columns, then a wordmark, then legal lines. PDFs on cdn.klarna.com were not downloaded. Business log in (`portal.klarna.com`) was not opened.

| Item | Opens | Stop? |
|---|---|---|
| About us | `/us/about-us/` | |
| Careers | `/careers/` | |
| Black Friday | `/us/shopping/c/black-friday/` | |
| Legal | `/us/legal/` | |
| Press | `/international/press/` | |
| Security | `/us/security/` | |
| Privacy | `/us/privacy/` | |
| Sustainability | `/international/sustainability/` | |
| Resell | `/us/resell/` | |
| Accessibility | `/us/accessibility/` | |
| Contact | `/us/about-us/contact/` | |
| Store Directory | `/us/store/` | |
| Buyer Protection Policy | `/us/buyer-protection/` | |
| Complaints | `/us/complaints/` | |
| Merchant support | `/international/enterprise/merchant-support/` | |
| Business log in | `https://portal.klarna.com/` | yes, account wall |
| Sell with Klarna | `/international/enterprise/` | |
| Developers portal | `https://docs.klarna.com/` | external, not followed |
| Operational status | `https://status.klarna.com/` | external, not followed |
| Terms | `/us/terms-of-use/` | |
| Cookies | `/us/cookies/` | not opened |
| Auto-Track, cashback, account disclosures | cdn.klarna.com legal PDFs | not downloaded |

## International header

https://klarna.com lands on `/international/`. That header is a different tree.

| Control | Opens | Stop? |
|---|---|---|
| Open navigation menu | Drawer of the same links | |
| Klarna | `/international/` | |
| Investor relations | investors.klarna.com | external, not followed |
| Corporate governance | investors.klarna.com | external, not followed |
| ESG | investors.klarna.com | external, not followed |
| Sustainability | `/international/sustainability/` | |
| News | `/international/press/` | |
| Careers | `/international/careers/` | |
| About us | `/international/about-us/` | |
| Continue in app | `https://app.klarna.com/login` | yes, account wall |
| Market rows (Australia, Österreich, and the rest) | That market's home, such as `/au/` or `/at/` | not followed |

## Help

`/us/help/` is public. Topic links include `/us/help/klarna-card/`. Search on help was not submitted.

## Where this capture stops

Sign in, Sign up, and Continue in app are the account wall. They were opened only to photograph the empty wall. Nothing was typed. No identity provider was clicked. No form was submitted. Cookie settings were not opened. The OneTrust banner was hidden with CSS and never answered.
