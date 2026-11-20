# Ripple public site tree

Mapped from [https://ripple.com/](https://ripple.com/) on 2026-11-21 in headless Chromium before any package screenshot. The homepage returned HTTP 200 and painted "The new standard for modern finance". Nav menus were opened with their own buttons. Same-origin links came from those menus, the footer, and the public sitemap index at [https://ripple.com/sitemap.xml](https://ripple.com/sitemap.xml) (`page.xml` 88 URLs, `casestudy.xml` 15, `press-release.xml` 250, `post.xml` 646).

No password, code, captcha, Google or Apple control, account form, profile field, birthday, plan, survey, onboarding, or newsletter field was filled. No form was submitted.

## Shell

The desktop header is the same on every `ripple.com` marketing page.

| Control | Opens |
|---|---|
| Logo | [https://ripple.com/](https://ripple.com/) |
| Products (button, `aria-expanded`) | Mega menu. See Products. |
| Solutions (button) | Mega menu. See Solutions. |
| Customers (button) | Mega menu. See Customers. |
| Developers (button) | Mega menu. See Developers. |
| Resources (button) | Mega menu. See Resources. |
| Company (button) | Mega menu. See Company. |
| Contact Sales | [https://ripple.com/contact/sales/](https://ripple.com/contact/sales/) (sales form; not submitted) |
| Open search | Search dialog with an input labelled "Search through ripple.com content", placeholder "Search ripple.com". No query was typed. |
| Change language | Menu: English ([https://ripple.com/](https://ripple.com/)), Português ([https://ripple.com/pt-br/](https://ripple.com/pt-br/)) |
| Cookie banner "Close this consent banner" | Dismisses the OneTrust-style banner. Copy says closing continues with essential cookies only. |
| Cookie banner "Deny Non-Essential Cookies" | Consent choice. Not used for the capture: the banner was hidden, never clicked, so no consent POST ran. |
| Cookie banner "Accept All Cookies" / "Save Preferences" | Consent choices. Not clicked. |
| Cookie banner toggles (Targeted Advertising, Personalization, Analytics) | Preference switches inside the banner. Not toggled. |
| Storage Preferences | In-banner anchor. Not followed as a separate page. |
| Your Privacy Choices / Do Not Sell My Information | Footer controls that reopen cookie preferences. Not clicked. |
| Explore Our Solutions | Same-page anchor `#solutions` |
| Carousel "Go to slide 1" through "Go to slide 4" | Customer quote slides on the homepage. Local state. |
| Back to top | Scrolls the current page. |

Phone width (390) replaces the six nav buttons with a menu button. That menu is captured as a local interaction, not a new URL.

## Products menu

| Control | Opens |
|---|---|
| Payments | [https://ripple.com/products/cross-border-payments/](https://ripple.com/products/cross-border-payments/) |
| Custody | [https://ripple.com/products/custody/](https://ripple.com/products/custody/) |
| Stablecoin | [https://ripple.com/products/stablecoin/](https://ripple.com/products/stablecoin/) |
| Prime Brokerage | [https://ripple.com/products/prime-brokerage/](https://ripple.com/products/prime-brokerage/) |
| Treasury Management | [https://ripple.com/products/treasury-management/](https://ripple.com/products/treasury-management/) |
| Report, "The Functional Evolution of Digital Assets" | [https://ripple.com/lp/functional-evolution-of-digital-assets/](https://ripple.com/lp/functional-evolution-of-digital-assets/) (gated download form; not submitted) |
| Global Payout Network | [https://ripple.com/products/cross-border-payments/payout-network/](https://ripple.com/products/cross-border-payments/payout-network/) |

Homepage solution cards repeat Payments, Custody, Stablecoin, Prime Brokerage, Treasury, and Tokenization ([https://ripple.com/products/tokenization/](https://ripple.com/products/tokenization/)). Tokenization is on the homepage cards, not in the Products menu.

Sitemap children not in the menu, same template:

- [https://ripple.com/products/custody/features/](https://ripple.com/products/custody/features/)
- [https://ripple.com/products/custody/institutional/](https://ripple.com/products/custody/institutional/)
- [https://ripple.com/products/custody/wallets/](https://ripple.com/products/custody/wallets/)
- [https://ripple.com/products/payments/features/](https://ripple.com/products/payments/features/)
- [https://ripple.com/products/stablecoin/advisory-board/](https://ripple.com/products/stablecoin/advisory-board/)
- [https://ripple.com/products/stablecoin/availability/](https://ripple.com/products/stablecoin/availability/)
- [https://ripple.com/products/stablecoin/features/](https://ripple.com/products/stablecoin/features/)
- [https://ripple.com/products/stablecoin/transparency/](https://ripple.com/products/stablecoin/transparency/)

## Solutions menu

| Control | Opens |
|---|---|
| Accept stablecoin payments | [https://ripple.com/use-case/accept-stablecoin-payments/](https://ripple.com/use-case/accept-stablecoin-payments/) |
| Pay out in stablecoins or fiat globally | [https://ripple.com/use-case/global-payouts/](https://ripple.com/use-case/global-payouts/) |
| Secure and govern digital assets | [https://ripple.com/use-case/secure-digital-assets/](https://ripple.com/use-case/secure-digital-assets/) |
| Issue and manage tokenized assets | [https://ripple.com/use-case/issue-tokenized-assets/](https://ripple.com/use-case/issue-tokenized-assets/) |
| Execute OTC crypto trades at scale | [https://ripple.com/use-case/otc/](https://ripple.com/use-case/otc/) |
| Banking | [https://ripple.com/industry/banking/](https://ripple.com/industry/banking/) |
| Fintech | [https://ripple.com/industry/fintech/](https://ripple.com/industry/fintech/) |
| Fintech Guide card | [https://ripple.com/lp/the-fintech-checklist-for-stablecoin-payments/](https://ripple.com/lp/the-fintech-checklist-for-stablecoin-payments/) (gated download form; not submitted) |

## Customers menu

| Control | Opens |
|---|---|
| Customers | [https://ripple.com/customers/](https://ripple.com/customers/) |
| Case Studies | [https://ripple.com/customer-case-study/](https://ripple.com/customer-case-study/) |
| Regulated Worldwide card | [https://ripple.com/use-case/global-payouts/](https://ripple.com/use-case/global-payouts/) |
| DZ Bank case study card | [https://ripple.com/customer-case-study/dz-bank/](https://ripple.com/customer-case-study/dz-bank/) |
| i-payout case study card | [https://ripple.com/customer-case-study/i-payout/](https://ripple.com/customer-case-study/i-payout/) |

The case-study index lists further public studies (sitemap, 15 total): bdacs, bitso, flash-payments, hai-ha-money-transfer, instarem, moneymatch, nium, sbi-remit, scb, sentbe, tranglo, travelex-bank, unicambio. Each is the same article template. The index plus two articles stand for the template.

## Developers menu

| Control | Opens | Stop |
|---|---|---|
| Technical Documentation | [https://docs.ripple.com/](https://docs.ripple.com/) | Separate docs product. Public. Recorded as a boundary, not the marketing system. |
| XRP Ledger Documentation | [https://xrpl.org/docs](https://xrpl.org/docs) | Separate site. Public. Boundary. |
| Talk to a solutions engineer | [https://ripple.com/contact/sales/](https://ripple.com/contact/sales/) | Sales form. Not submitted. |
| Explore Payments API | [https://docs.ripple.com/products/payments-direct-2/api-docs/payments-direct-api/payments-direct-2-api](https://docs.ripple.com/products/payments-direct-2/api-docs/payments-direct-api/payments-direct-2-api) | Docs boundary. |
| Explore Custody API | [https://docs.ripple.com/products/custody/reference/api/openapi](https://docs.ripple.com/products/custody/reference/api/openapi) | Docs boundary. |
| Wallets Docs card | [https://docs.ripple.com/products/wallet](https://docs.ripple.com/products/wallet) | Docs boundary. |
| Payments Docs card | [https://docs.ripple.com/products/payments-direct-2](https://docs.ripple.com/products/payments-direct-2) | Docs boundary. |

Sitemap also lists [https://ripple.com/developer-resources/](https://ripple.com/developer-resources/) and [https://ripple.com/institutional-defi-portal/](https://ripple.com/institutional-defi-portal/).

## Resources menu

| Control | Opens |
|---|---|
| Content Library | [https://ripple.com/content-library/](https://ripple.com/content-library/) |
| Blog | [https://ripple.com/insights/](https://ripple.com/insights/) |
| Events | [https://ripple.com/events/](https://ripple.com/events/) |
| FAQs | [https://ripple.com/faq/](https://ripple.com/faq/) |
| Fraud Prevention | [https://ripple.com/how-to-identify-crypto-scams/](https://ripple.com/how-to-identify-crypto-scams/) |
| Stablecoin landscape report card | [https://ripple.com/lp/the-definitive-stablecoin-landscape-series-north-america/](https://ripple.com/lp/the-definitive-stablecoin-landscape-series-north-america/) (gated form; not submitted) |
| BCG custody report card | [https://ripple.com/lp/bcg-report-2026/](https://ripple.com/lp/bcg-report-2026/) (gated form; not submitted) |

`post.xml` holds 646 insight articles under `/insights/<slug>/`. The index stands for that template. `page.xml` also lists 12 `/learn/` explainers (what is a stablecoin, wallets, remittance, and similar). The learn index stands for that template.

Events also has [https://ripple.com/events/all/](https://ripple.com/events/all/).

## Company menu

| Control | Opens |
|---|---|
| About Ripple | [https://ripple.com/company/](https://ripple.com/company/) |
| Careers | [https://ripple.com/careers/](https://ripple.com/careers/) |
| Public Policy | [https://ripple.com/public-policy/](https://ripple.com/public-policy/) |
| Leadership | [https://ripple.com/company/leadership/](https://ripple.com/company/leadership/) |
| Ripple Impact | [https://ripple.com/impact/](https://ripple.com/impact/) |
| About XRP | [https://ripple.com/xrp/](https://ripple.com/xrp/) |
| Open Roles card | [https://ripple.com/careers/all-jobs/](https://ripple.com/careers/all-jobs/) (public job list; no application form filled) |

Sitemap children of the same templates, not opened as separate captures:

- Careers: `/careers/early-careers/`, `/careers/engineering/`, `/careers/locations/`, `/careers/ripplelife/`
- Company: `/company/sbi-ripple-asia/`
- Impact: `/impact/sustainability/`, `/impact/ubri/`, `/impact/impact-report/`, `/impact/case-study/rlusd-mercy-corps-ventures/`, `/impact/case-study/rlusd-sidechain-pilot/`
- XRP: `/xrp/availability/`

## Footer

| Control | Opens |
|---|---|
| Payments, Custody, Stablecoin, Prime Brokerage, Treasury Management | Same product URLs as the Products menu |
| Accept stablecoin payments, Pay out, Secure and govern, Manage tokenized assets | Same use-case URLs as the Solutions menu |
| Banking, Fintech | Same industry URLs |
| Customers, Case Studies | Same customer URLs |
| Customer Login | [https://home.ripple.com/](https://home.ripple.com/). **Wall.** See below. |
| Technical Documentation, XRP Ledger Documentation | Docs boundaries above |
| Content Library, Blog, Events, FAQs, Fraud Prevention | Same resource URLs |
| Press Center | [https://ripple.com/press-releases/](https://ripple.com/press-releases/) (`press-release.xml` has 250 articles under `/ripple-press/<slug>/`; the index stands for the template) |
| About Ripple, Contact Us, Careers, Public Policy, Leadership, Ripple Impact, About XRP | Same company URLs |
| Investments | [https://ripple.com/investments/](https://ripple.com/investments/) |
| Facebook, X, YouTube, LinkedIn | External social profiles. Not captured. |
| Terms | [https://ripple.com/legal/terms-of-use/](https://ripple.com/legal/terms-of-use/) |
| Privacy | [https://ripple.com/legal/privacy-policy/](https://ripple.com/legal/privacy-policy/) |
| Licenses | [https://ripple.com/legal/money-transfer-license/](https://ripple.com/legal/money-transfer-license/) |
| Additional Terms | [https://legal.rail.io/](https://legal.rail.io/). Separate legal host. Boundary. |
| Ripple Prime Disclosures | [https://ripple.com/prime-brokerage-disclosures/](https://ripple.com/prime-brokerage-disclosures/) |
| Ripple Prime NL Disclosures | [https://ripple.com/prime-brokerage-disclosures/hrp-civ-nl-bv/](https://ripple.com/prime-brokerage-disclosures/hrp-civ-nl-bv/) |

Other legal pages in `page.xml`, same long-form template: applicant-privacy-notice, bug-bounty, complaints-dispute-resolution, compliance, cookie-policy, dpf-covered-entities, stablecoin.

Other sitemap pages not in the header menus: `/newsroom/`, `/media-kit/`, `/partners/`, `/security/`, `/ripplenet-committee/`, `/its-happening/`, `/contact/press/`, `/suppliers/`, `/suppliers/existing/`, `/suppliers/invoice/`, `/suppliers/onboarding/`. Supplier invoice and onboarding look like account flows; they were not filled.

## Login wall

Footer "Customer Login" goes to [https://home.ripple.com/](https://home.ripple.com/). The page title is "Ripple Payments". It immediately redirects to Auth0:

`https://ripplenet-prod-eu.eu.auth0.com/u/login`

The query string on that redirect holds a session token. It is not recorded here.

The wall shows "Sign in to your account.", an email field (`username`), a password field, "Show password", "Reset password", and "Continue". Password was not submitted. Reset password was not opened. No Google or Apple button was present on that screen. That branch stops here. The signed-in payments app was not reached.

## Forms recorded, never submitted

| Page | Fields visible | Action |
|---|---|---|
| [https://ripple.com/contact/](https://ripple.com/contact/) | Contact routing page ("How can we help?") | Not filled |
| [https://ripple.com/contact/sales/](https://ripple.com/contact/sales/) | Sales lead form | Not filled |
| `/lp/*` report pages | Download / lead forms | Not filled |
| Search dialog | Search field | Not typed |
| Cookie banner | Preference toggles | Hidden, not clicked |
| Job application links from `/careers/all-jobs/` | External application | Not followed into a form |

## Capture set

Desktop 1440×900 and phone 390×844, light only (no theme switch was found on the public site):

Home, one product page, one use-case page, customers, insights index, FAQ, company, contact (form not submitted), legal terms, Portuguese home, plus local states: Products mega menu, search dialog open and empty, language menu, phone menu, homepage carousel slide, FAQ item expanded if the control is a disclosure.

Article, press, learn, and remaining product children are the same templates. They are listed above and not shot one by one.
