# Vivid Money public site tree

Mapped 2026-11-22 from [https://vivid.money/en-eu/](https://vivid.money/en-eu/) while signed out. The host redirects [https://vivid.money](https://vivid.money) to the Europe English marketing site. The page title is "Business accounts, expenses and cash management | Vivid Europe". Desktop shots are 1440×900 CSS pixels at 2x (2880×1800 PNG). Phone shots are 390×844 CSS pixels at 2x (780×1688 PNG).

A control that opens a login, signup, or identity-provider wall stops that branch. Nothing was typed. No form was submitted. No identity provider was clicked. Cookie Accept, Reject non-essential, and Customize were not pressed. The cookie dialog (`.popup-overlay` plus `#popup-1`) was hidden with CSS so the page underneath could be photographed.

`html` carried `data-theme="light"`. No public page exposed a dark theme switch.

## Header

Present on the homepage. Products, Solutions, Pricing, and Resources are buttons with `aria-controls` pointing at a mega-menu. Customers is a link. At 390 the same header stays in one row and the later items fall off the right edge. There is no hamburger and no drawer.

| Control | Kind | Opens | Shot |
|---|---|---|---|
| Wordmark | Link | https://vivid.money/en-eu/ | |
| Products | Button | Mega-menu `#mega-menu-business_products` | [desktop](screenshots/site-tree/desktop-menu-products.png) |
| Solutions | Button | Mega-menu `#mega-menu-business_solutions_header` | [desktop](screenshots/site-tree/desktop-menu-solutions.png) |
| Pricing | Button | Mega-menu `#mega-menu-pricing` | [desktop](screenshots/site-tree/desktop-menu-pricing.png) |
| Customers | Link | https://vivid.money/en-eu/customers/ | [desktop](screenshots/customers-light-desktop.png) |
| Resources | Button | Mega-menu `#mega-menu-company` | [desktop](screenshots/site-tree/desktop-menu-resources.png) |
| EN | Button, `aria-haspopup="listbox"` | Country and language panel. Apply was not pressed. | [desktop](screenshots/site-tree/desktop-menu-language.png) |
| Login | Link | https://business.vivid.money/en/login wall. Query string on the marketing link was not followed. Stopped. | [desktop](screenshots/login-wall-light-desktop.png), [phone](screenshots/login-wall-light-phone.png) |
| Get started | Button | `#open-account` on the homepage. Stopped. | [desktop](screenshots/signup-wall-light-desktop.png) |

## Products menu

Three columns of product links, then Platform and Personal accounts.

| Group | Label | Opens |
|---|---|---|
| Expense management | Corporate cards | https://vivid.money/en-eu/business/cards/ | [desktop](screenshots/cards-light-desktop.png) |
| Expense management | Budgets | https://vivid.money/en-eu/enterprise/budgets/ |
| Expense management | Custom roles | https://vivid.money/en-eu/enterprise/custom-roles/ |
| Expense management | Payment approvals | https://vivid.money/en-eu/enterprise/approval-rules/ |
| Expense management | Bookkeeping and receipts | https://vivid.money/en-eu/business/bookkeeping/ |
| Expense management | Business travel | https://vivid.money/en-eu/business/travel/ |
| Cash management | Cash overview | https://vivid.money/en-eu/business/cash-management/ |
| Cash management | Fixed interest | https://vivid.money/en-eu/business/interest/ |
| Cash management | Model portfolios | https://vivid.money/en-eu/business/strategies/ |
| Cash management | Business brokerage | https://vivid.money/en-eu/business/treasury/ |
| Cash management | Institutional cash management | https://vivid.money/en-eu/enterprise/cash-management/ |
| Cash management | Transfer rules | https://vivid.money/en-eu/enterprise/transfer-rules/ |
| Business account | Accounts and IBANs | https://vivid.money/en-eu/business/ | [desktop](screenshots/business-light-desktop.png) |
| Business account | Transfers | https://vivid.money/en-eu/business/international-payments/ |
| Business account | Currency exchange | https://vivid.money/en-eu/business/currency-exchange/ |
| Business account | Invoicing | https://vivid.money/en-eu/business/invoicing/ |
| Business account | Online payments | https://vivid.money/en-eu/business/acquiring/ |
| Business account | POS terminals | https://vivid.money/en-eu/business/terminals/ |
| Platform | Digital employees | https://vivid.money/en-eu/business/digital-employees/ |
| Platform | API | https://vivid.money/en-eu/business/api/ |
| Platform | Integrations | https://vivid.money/en-eu/business/open-banking/ |
| Platform | Tax filing | https://vivid.money/en-eu/business/tax/ |
| Personal accounts | Accounts | https://vivid.money/en-eu/personal/ | [desktop](screenshots/personal-light-desktop.png) |
| Personal accounts | Payments | https://vivid.money/en-eu/personal/#payments |
| Personal accounts | Cards | https://vivid.money/en-eu/personal/cards/ |
| Personal accounts | Stocks and ETFs | https://vivid.money/en-eu/personal/investments/stocks/ |
| Personal accounts | Crypto | https://vivid.money/en-eu/personal/investments/crypto/ |
| Personal accounts | Interest rate | https://vivid.money/en-eu/personal/interest-rate-pocket/ |
| Personal accounts | Rewards | https://vivid.money/en-eu/personal/cashback/ |
| Personal accounts | Prime | https://vivid.money/en-eu/personal/#prime |
| Personal accounts | Pricing | https://vivid.money/en-eu/personal/plans/ |

## Solutions menu

| Group | Label | Opens |
|---|---|---|
| By business type | Startups | https://vivid.money/en-eu/business/startups/ |
| By business type | Partnerships | https://vivid.money/en-eu/business/partnerships/ |
| By business type | Non-profits and associations | https://vivid.money/en-eu/business/non-profits/ |
| By business type | Companies in formation | https://vivid.money/en-eu/business/creation/ |
| By business type | Freelancers | https://vivid.money/en-eu/business/freelancers/ | [desktop](screenshots/freelancers-light-desktop.png) |
| By industry | Wholesalers | https://vivid.money/en-eu/business/account/wholesalers/ |
| By industry | E-commerce | https://vivid.money/en-eu/business/account/ecommerce/ |
| By industry | IT and software | https://vivid.money/en-eu/business/account/it-software/ |
| By industry | Construction | https://vivid.money/en-eu/business/account/construction/ |
| By industry | Logistics | https://vivid.money/en-eu/business/account/logistics/ |
| By industry | Marketing | https://vivid.money/en-eu/business/account/marketing-agencies/ |
| By industry | Solar and electrical | https://vivid.money/en-eu/business/account/solar-electrical/ |
| By industry | Travel | https://vivid.money/en-eu/business/account/travel-agencies/ |

## Pricing menu

Each card links to the plans page. The photographed page is the Companies tab.

| Label | Opens |
|---|---|
| Companies | https://vivid.money/en-eu/business/plans/?activeTab=companies | [desktop](screenshots/pricing-light-desktop.png), [phone](screenshots/pricing-light-phone.png) |
| Enterprises | https://vivid.money/en-eu/business/plans/?activeTab=enterprises |
| Freelancers | https://vivid.money/en-eu/business/plans/?activeTab=freelancers |

On the plans page, Companies, Enterprises, and Freelancers are tabs. Monthly and Annual is a switch. Get started on a plan opens the same account wall. That branch was not continued.

## Resources menu

| Group | Label | Opens |
|---|---|---|
| Learn | Events and webinars | https://vivid.money/en-eu/events/ |
| Learn | Affiliate program | https://vivid.money/en-eu/affiliate/partners/ |
| Company | About Vivid | https://vivid.money/en-eu/about-us/ | [desktop](screenshots/about-light-desktop.png) |
| Company | Press | https://press.vivid.money/en-eu/home |
| Company | Careers | https://careers.vivid.money/ |
| Help | Help Centre Business | https://help-business.vivid.money/en/ |
| Help | Help Centre Personal | https://support.vivid.money/en/ |
| Help | Contact us | https://vivid.money/en-eu/support/ |
| Help | Status | https://vivid.money/en-eu/status/ |

Press, Careers, and both help centres leave the marketing host. They were not opened.

## Country and language

The EN button opens a panel labelled Country and language. It shows Country set to Europe and Language set to English, plus a disabled Apply button. The dropdowns were not opened. Apply was not pressed.

## Signup wall

Get started sets the hash to `#open-account` and shows a section titled "Open a business account". The site prefilled Country (Germany), Business type (Registered Company), Legal entity type (GmbH), and the phone prefix (+49). Company name and the rest of the phone number were empty. Nothing was typed. Open a business account was not pressed.

## Login wall

Login leaves the marketing host for `https://business.vivid.money/en/login`. The page is titled "Log in to Vivid Business". It asks for a phone number, with Phone and Email as a segment, a country prefix the site filled in, and Continue. Language chips (English, De, It, Fr, Es, Nl) sit above the form. Nothing was typed. Continue was not pressed. No identity provider is on the page. The personal help centre was not used as a second login.

## Footer

The footer repeats the product, solution, pricing, company, and help links, plus legal documents, imprint, privacy notice, and social profiles. Social profiles and legal PDFs were not opened. Contact us and Speak Up are forms. They were not opened and not submitted.

## Phone

At 390 the homepage and the plans page keep the desktop header and crop it. Login, Get started, Customers, and Resources are off-screen. There is no menu button to open a drawer. Shots: [home](screenshots/home-light-phone.png), [pricing](screenshots/pricing-light-phone.png), [login](screenshots/login-wall-light-phone.png).
