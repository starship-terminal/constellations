# Wealthsimple public site tree

Mapped 2026-11-21 from https://www.wealthsimple.com/ (redirects to `/en-ca`) in headless Chromium, before screenshots. English Canada only. French (`/fr-ca`) is the same tree in another language and was not walked.

A control that opens `my.wealthsimple.com`, `app.wealthsimple.com`, or a signup/login path is a wall. That URL is recorded and the branch stops. No email, password, code, or form was submitted.

## Shell controls on every marketing page

| Control | Opens |
|---|---|
| Banner link "Wealthsimple Presents" | Page `/en-ca/presents/something-good` |
| Banner button "Close banner" | Dismisses the top banner. No navigation. |
| Logo | Page `/en-ca` |
| Skip to main content | In-page `#main` |
| Nav button Chequing | Mega menu (hover and click). Links below. |
| Nav button Trade | Mega menu. |
| Nav link Credit card | Page `/en-ca/credit-card` (no menu) |
| Nav button Borrow | Mega menu. |
| Nav button Accounts | Mega menu. |
| Nav button Business | Mega menu. |
| Nav button Offers | Mega menu. |
| Log in | Wall `https://my.wealthsimple.com/app/login?locale=en-ca`. Known probe: email and password fields. No Google button. Email was not typed. Password was not submitted. |
| Get started | Wall `https://my.wealthsimple.com/app/signup?locale=en-ca`. Branch stops. |
| Open search | Search dialog. Placeholder "I'm looking for...". Typing a query is a search, not a form submit of profile data. Escape closes it. |
| Menu (phone) | Full-screen nav drawer with the same groups as accordions. |
| Open chat | Support chat widget. Not submitted. |
| Pause motion / Pause video | Toggles motion on the page. No navigation. |
| Language / FR links in footer | `/fr-ca` mirror. Not walked. |

## Mega menus (desktop header)

Each menu button expands a panel of product links. The same links are repeated in the footer and in the phone drawer.

Invest is a footer and in-page product group, not a header button on the 2026-11-21 home capture.

### Chequing

- Chequing account opens page `/en-ca/chequing`
- Kids and teens opens page `/en-ca/chequing/kids-teens`
- Savings opens page `/en-ca/savings`
- USD account opens page `/en-ca/accounts/usd`

### Trade

- Stocks & ETFs opens page `/en-ca/trade`
- Wealthsimple Pro opens page `/en-ca/trade/pro`
- Options opens page `/en-ca/trade/options`
- Margin opens page `/en-ca/trade/margin`
- Futures opens page `/en-ca/trade/futures`
- IPO access opens page `/en-ca/trade/ipo-access`
- Prediction markets opens page `/en-ca/predict`
- Gold opens page `/en-ca/trade/gold`
- Crypto opens page `/en-ca/trade/crypto`

### Borrow

- Portfolio line of credit opens page `/en-ca/portfolio-line-of-credit`
- Mortgages opens page `/en-ca/mortgages`

### Accounts

- TFSA opens page `/en-ca/accounts/tfsa`
- RRSP opens page `/en-ca/accounts/rrsp`
- Spousal RRSP opens page `/en-ca/accounts/spousal-rrsp`
- Non-registered opens page `/en-ca/accounts/non-registered`
- FHSA opens page `/en-ca/accounts/fhsa`
- RESP opens page `/en-ca/accounts/resp`
- RRIF opens page `/en-ca/accounts/rrif`
- LIRA opens page `/en-ca/accounts/lira`
- All accounts opens page `/en-ca/accounts`

### Business

- Business chequing opens page `/en-ca/business/chequing`
- Business investing opens page `/en-ca/business/investing`
- Group savings opens page `/en-ca/business/group-savings`
- All business opens page `/en-ca/business`

### Offers

- Monthly Millionaire opens page `/en-ca/monthly-millionaire`
- 1% Transfer match opens page `/en-ca/one-percent-match`
- 5% Welcome offer opens page `/en-ca/5-percent-welcome-offer`
- All offers opens page `/en-ca/promotions`

Invest group (footer and in-page):

- Automated Investing opens page `/en-ca/automated-investing`
- Classic portfolios opens page `/en-ca/invest/classic-portfolios`
- Summit portfolios opens page `/en-ca/invest/summit-portfolios`
- Income portfolios opens page `/en-ca/invest/income-portfolios`
- Private Market fund opens page `/en-ca/invest/private-market-fund`
- Work with an advisor opens page `/en-ca/invest/advice`
- All portfolios opens page `/en-ca/invest`

## Home page interactions that are not navigation

| Control | What it does |
|---|---|
| Email field + Register now (Monthly Millionaire) | Newsletter / contest signup. Not filled. Not submitted. |
| Terms of Use | Page `/en-ca/legal/terms` |
| Privacy Policy | Page `/en-ca/legal/privacy` |
| Product tiles (Chequing, Trade, Invest, Advice, Business) | Same product pages as the menus |
| Pricing / plan comparison links | Page `/en-ca/pricing` |
| Chat launcher | Support widget. Not a page. Not submitted. |

## Footer

| Control | Opens |
|---|---|
| About | `/en-ca/about` |
| Culture | `/en-ca/culture` |
| Careers | `/en-ca/careers` |
| Newsroom | `https://newsroom.wealthsimple.com/` (separate host) |
| Shop | `https://wealthsimple.com/shop` |
| Accessibility statement | `/en-ca/legal/accessibility/statement` |
| Security | `/en-ca/security` |
| Tax | `/en-ca/tax` |
| Households | `/en-ca/households` |
| Changelog | `/en-ca/changelog` |
| Contact | `/en-ca/contact` |
| Get in touch | `/en-ca/get-in-touch` (lead form; not submitted) |
| Help centre | `https://help.wealthsimple.com/hc/en-ca` |
| Referrals | `/en-ca/referrals` |
| Pricing | `/en-ca/pricing` |
| Learn | `/en-ca/learn` (article index; 100+ articles) |
| Legal disclaimers | `/en-ca/legal/legal-disclaimers` |
| File a complaint | `/en-ca/legal/file-complaint` |
| Français | `/fr-ca` |
| TLDR newsletter | `/en-ca/learn/tldr-newsletter-signup` (signup form; not filled) |

## Login and signup walls (branch stops)

| From | URL |
|---|---|
| Log in | `https://my.wealthsimple.com/app/login?locale=en-ca` |
| Get started | `https://my.wealthsimple.com/app/signup?locale=en-ca` |
| Deep links on product pages | `https://app.wealthsimple.com/74rd/...` (app store / onboarding handoff) |
| Pre-IPO and similar | `https://my.wealthsimple.com/app/pre-ipo` and other `/app/` paths |

Known probe of the login URL: the page showed email and password. There is no Google button. Nothing was typed.

## Public page inventory

Crawl of homepage seeds plus one more hop found these hosts. Marketing pages on `www.wealthsimple.com` returned 200 except two PDF downloads.

| Host | Paths found | Treatment |
|---|---|---|
| `www.wealthsimple.com` | 274 | see below |
| `help.wealthsimple.com` | 111 | see below |
| `app.wealthsimple.com` | 27 | see below |
| `www.cdn.wealthsimple.com` | 11 | see below |
| `wealthsimple.com` | 10 | see below |
| `my.wealthsimple.com` | 8 | see below |
| `newsroom.wealthsimple.com` | 4 | see below |
| `promotions.wealthsimple.com` | 4 | see below |
| `product-news.wealthsimple.com` | 3 | see below |
| `tldr-archive.wealthsimple.com` | 3 | see below |
| `engineering.wealthsimple.com` | 1 | see below |
| `start.wealthsimple.com` | 1 | see below |
| `insights.wealthsimple.com` | 1 | see below |
| `compliance-documents.cdn.wealthsimple.com` | 1 | see below |

Visited 90 URLs in the map pass. Two credit-card legal links start a file download and were not rendered: `/en-ca/credit-card/rewards-terms-conditions`, `/en-ca/credit-card/certificate-of-insurance-chubb`.

### www.wealthsimple.com product and company pages

- `/en-ca`
- `/en-ca/5-percent-welcome-offer`
- `/en-ca/about`
- `/en-ca/accounts`
- `/en-ca/accounts/corporate`
- `/en-ca/accounts/fhsa`
- `/en-ca/accounts/lira`
- `/en-ca/accounts/non-registered`
- `/en-ca/accounts/registered-savings`
- `/en-ca/accounts/resp`
- `/en-ca/accounts/rrif`
- `/en-ca/accounts/rrsp`
- `/en-ca/accounts/spousal-rrsp`
- `/en-ca/accounts/tfsa`
- `/en-ca/accounts/usd`
- `/en-ca/advice`
- `/en-ca/automated-investing`
- `/en-ca/benefits`
- `/en-ca/business`
- `/en-ca/business-resources`
- `/en-ca/business/brokers-and-consultants`
- `/en-ca/business/chequing`
- `/en-ca/business/credit-card-notify-me`
- `/en-ca/business/get-in-touch`
- `/en-ca/business/group-savings`
- `/en-ca/business/group-savings/dpsp`
- `/en-ca/business/group-savings/group-fhsa`
- `/en-ca/business/group-savings/group-non-reg`
- `/en-ca/business/group-savings/group-rrsp`
- `/en-ca/business/group-savings/group-tfsa`
- `/en-ca/business/investing`
- `/en-ca/business/target-date-portfolios`
- `/en-ca/buying-a-house`
- `/en-ca/careers`
- `/en-ca/changelog`
- `/en-ca/chequing`
- `/en-ca/chequing/kids-teens`
- `/en-ca/contact`
- `/en-ca/credit-card`
- `/en-ca/credit-card/cardholder-agreement`
- `/en-ca/credit-card/cardholder-agreement-core`
- `/en-ca/credit-card/certificate-of-insurance-chubb`
- `/en-ca/credit-card/rewards-terms-conditions`
- `/en-ca/culture`
- `/en-ca/dex-trading`
- `/en-ca/direct-deposit`
- `/en-ca/financial-assistant-notify-me`
- `/en-ca/for-business`
- `/en-ca/fundamental-analysis`
- `/en-ca/futures-trading-resource-guide`
- `/en-ca/get-in-touch`
- `/en-ca/get-in-touch/active-trading`
- `/en-ca/get-in-touch/one-percent-match`
- `/en-ca/get-in-touch/super-referrer`
- `/en-ca/get-in-touch/voice-of-the-next-gen`
- `/en-ca/households`
- `/en-ca/invest`
- `/en-ca/invest/advice`
- `/en-ca/invest/advice-wm-estate-planning-webinar`
- `/en-ca/invest/classic-portfolios`
- `/en-ca/invest/income-portfolios`
- `/en-ca/invest/private-market-fund`
- `/en-ca/invest/summit-portfolios`
- `/en-ca/kids-teens-notify-me`
- `/en-ca/managed-investing`
- `/en-ca/margin-trading-resources`
- `/en-ca/monthly-millionaire`
- `/en-ca/mortgages`
- `/en-ca/mortgages/apply`
- `/en-ca/one-percent-match`
- `/en-ca/options-trading-education`
- `/en-ca/portfolio-line-of-credit`
- `/en-ca/predict`
- `/en-ca/prediction-trading-resources`
- `/en-ca/presents/something-good`
- `/en-ca/presents/something-good/live`
- `/en-ca/pricing`
- `/en-ca/promotions`
- `/en-ca/referrals`
- `/en-ca/retirement-planning`
- `/en-ca/savings`
- `/en-ca/security`
- `/en-ca/self-directed-investing/margin`
- `/en-ca/tax`
- `/en-ca/tax-information-canada`
- `/en-ca/teaching-kids-about-money`
- `/en-ca/technical-analysis`
- `/en-ca/the-trade-show`
- `/en-ca/trade`
- `/en-ca/trade/active-trading`
- `/en-ca/trade/crypto`
- `/en-ca/trade/futures`
- `/en-ca/trade/futures/perpetuals-notify-me`
- `/en-ca/trade/gold`
- `/en-ca/trade/ipo-access`
- `/en-ca/trade/legal/crypto-product-risk-disclosure`
- `/en-ca/trade/margin`
- `/en-ca/trade/options`
- `/en-ca/trade/pro`
- `/en-ca/transfer-bonus`
- `/en-ca/wealthsimple-app/predict-app-store`
- `/en-ca/wealthsimple-app/predict-google-play`
- `/en-ca/wealthsimple-visa-infinite-card`
- `/en-ca/wealthsimple-visa-infinite-privilege-card`

### Learn (`/en-ca/learn`)

105 article and index paths. The index is `/en-ca/learn`. Individual articles are the same article template. The capture records the index plus a sample article rather than every post.

### Legal (`/en-ca/legal`)

66 legal and disclaimer paths. Long-form policy pages. The capture records terms, privacy, accessibility statement, and the disclaimer index. Fee schedules and chart disclaimers are the same legal template.

### Other hosts

- `help.wealthsimple.com`: Zendesk help centre. Public articles. Capture the centre home, not every article.
- `newsroom.wealthsimple.com`: press index. Public.
- `promotions.wealthsimple.com`: promotion article host (Zendesk).
- `product-news.wealthsimple.com` and `engineering.wealthsimple.com`: blog hosts.
- `insights.wealthsimple.com`, `tldr-archive.wealthsimple.com`: content archives.
- `wealthsimple.com/shop`: shop. Public until a cart checkout.
- `www.cdn.wealthsimple.com` and `compliance-documents.cdn.wealthsimple.com`: PDF downloads. Not HTML states.
- `start.wealthsimple.com`: short redirect into an app flow. Treated as a wall if it lands on signup.

## Interactions recorded as states, not pages

| State | How it opens |
|---|---|
| Banner visible / banner closed | Close banner |
| Each mega menu open | Header button hover or click |
| Search dialog open, field focused, query typed (not submitted as a profile form) | Open search |
| Phone menu drawer | Button labelled Open navigation (visible text "Menu") |
| Phone menu accordion expanded | Group button inside the drawer |
| Chat panel open | Open chat, if it renders without a login wall |
| Button hover, focus-visible, pressed | Pointer and keyboard on a primary control |
| Link hover and focus-visible | Pointer and keyboard |
| Text field focused and filled | Type into a public field, do not submit |
| Pricing tier selected / comparison | `/en-ca/pricing` controls |
| FAQ accordion open | Product-page disclosure buttons |
| 404 | A missing path on the same host |

## Not captured on purpose

- Signed-in app at `my.wealthsimple.com` past the login wall.
- Account creation, onboarding, birthday, plan, survey, newsletter submit.
- French locale tree.
- Every Learn article and every Help Centre article (same templates; indexes captured).
- PDF downloads.

