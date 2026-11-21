# Acctual site tree

Mapped 2026-11-21 from the public homepage `https://www.acctual.com/` (also `https://acctual.com/`, same page, HTTP 200) in headless Chromium, before screenshots. Controls were identified by reading the DOM. The only control pressed while mapping was the phone menu trigger, a local disclosure. No form was submitted. No password, code, or profile field was typed. Login and signup links were recorded and not followed.

The published sitemap (`https://www.acctual.com/sitemap.xml`, 89 URLs) is listed at the end. The tree below is the reachable public graph from the homepage, not the sitemap dump.

## Auth walls (recorded, not entered)

| Control | URL | What the page asks | Action |
|---|---|---|---|
| Nav "Log in" (desktop) | `https://app.acctual.com/` | Redirects into the product app | Stop. Not opened for capture. |
| Phone menu "Log in" | `https://app.acctual.com/login` | Same product app | Stop. Not opened. |
| Known probe | `https://app.acctual.com/sign-in` | HTTP 200. Title "Acctual". Body: "Welcome back", "Continue with Google", email address, password, "Continue", "Sign up". Inputs: `identifier` (email) and `password`. | Stop. Nothing typed. Google not clicked. |
| "Sign up for free", "Send my first invoice", "Create an invoice", "Get paid with Acctual", "Send Invoice with Acctual" | `https://app.acctual.com/signup` | Signup | Stop. Not opened. |
| Invoice templates, empty signup card | `https://app.acctual.com/sign-up` | Signup (hyphenated path) | Stop. Not opened. |
| Altitude page "Get started on Altitude" | `https://app.altitude.xyz/signup` (query `acctual`, referral campaign) | Another product's signup | Stop. Not opened. |

## Shell (every marketing page)

Desktop nav, `data-framer-name="Navigation/Topbar"`, is a row of links. It does not open a menu or dialog.

| Control | Opens |
|---|---|
| Wordmark (`data-framer-name="Inactive"`) | `/` |
| Freelancer | `/freelancer-invoicing` |
| Agency | `/agency-invoicing` |
| Pricing | `/pricing` |
| Blog | `/blog` |
| Log in | Auth wall, `https://app.acctual.com/` |
| Sign up for free | Auth wall, `https://app.acctual.com/signup` |
| Announcement strip "Acctual is joining Altitude" | `/altitude` |

Phone (390): the same top bar shows the wordmark and a 24px icon, `data-framer-name="Group 1171277804"`, at the right. Clicking it opens a full-viewport overlay named `Phone - Open` (local disclosure, stays on `/`). That overlay holds:

| Control | Opens |
|---|---|
| Freelancer | `/freelancer-invoicing` |
| Agency | `/agency-invoicing` |
| Pricing | `/pricing` |
| Blog | `/blog` |
| Log in | Auth wall, `https://app.acctual.com/login` |
| Sign up for free | Auth wall, `https://app.acctual.com/signup` |
| Announcement strip | `/altitude` |

Footer columns, shared by the marketing pages, are links, not menus:

| Label | Opens |
|---|---|
| Guides | External help centre `https://support.altitude.xyz/en/` |
| Privacy | `/privacy` |
| Terms | `/terms` |
| Invoice templates | `/invoice-templates` |
| Agency invoicing | `/agency-invoicing` |
| Freelancer invoicing | `/freelancer-invoicing` |
| Video production invoicing | `/blog/video-film-production-invoices` |
| Graphic design invoicing | `/blog/graphic-design-invoice` |
| Web design invoicing | `/blog/web-design-development-invoice` |
| Recurring invoicing | `/blog/how-to-set-up-recurring-invoices` |
| FreshBooks alternative | `/freshbooks-alternative` |
| PayPal invoice fees | `/blog/paypal-invoice-fees-are-they-worth-it` |
| Upwork alternatives | `/blog/best-upwork-alternatives-12-platforms-to-find-better-work-in-2026` |
| Consulting taxes | `/blog/how-to-set-up-recurring-invoices` (footer label points at the recurring-invoices post, not the consulting-taxes post) |
| Past due vs overdue | `/blog/past-due-vs-overdue-invoices` |
| Send money to UK from US | `/locations/us-to-uk` |
| Send money to US from UK | `/locations/uk-to-us` |
| Send money to US from Germany | `/locations/germany-to-us` |
| Send money to Germany from US | `/locations/us-to-germany` |
| Send money to US from Canada | `/locations/canada-to-us` |
| Send money to Canada from US | `/locations/us-to-canada` |
| Send money to Australia from US | `/locations/us-to-australia` |
| Send money to US from Australia | `/locations/australia-to-us` |
| Unlabelled brand-kit link | File download `https://framerusercontent.com/assets/EQixAHPVnB0mJWUEWcmeLJqBKOs.zip` (not a page) |
| Get paid with Acctual | Auth wall, `https://app.acctual.com/signup` |

## Homepage interactions (`/`)

| Control | What it does |
|---|---|
| Hero "Send my first invoice" | Auth wall, `https://app.acctual.com/signup` |
| Persona cards (Freelancers, Agencies, Consultants, Contractors, eCommerce, Cross border) | `href` is `/`. They do not navigate. |
| Invoice mock, `data-framer-name="Dropdown"` / `InputContainer` / `chevron-down-small` | Marketing artwork inside the hero. Labels read "PAYMENT METHOD", "Bank", "Card", "Crypto", "USD", "ACH", "USDC via ETH/Solana". A click on the first dropdown did not open a menu and did not navigate. Not a form. Not submitted. |
| FAQ items, `data-framer-name="Closed"` under `FAQ · Stablecoin` | Local accordion. Twelve questions, including "Is Acctual really free invoicing software?" Opening one does not navigate. |
| Security rows (PCI, SSL) | Static. No control. |
| Mid-page "Create an invoice" | Auth wall, signup. |

## Page graph from the homepage

Each row is a public page a control on the homepage, the shared nav, or the shared footer opens. Capture both widths unless noted.

| Page | How it is reached |
|---|---|
| `/` | Wordmark, start |
| `/freelancer-invoicing` | Nav Freelancer, footer |
| `/agency-invoicing` | Nav Agency, footer |
| `/pricing` | Nav Pricing |
| `/blog` | Nav Blog, footer Blog |
| `/altitude` | Announcement strip |
| `/privacy` | Footer |
| `/terms` | Footer |
| `/invoice-templates` | Footer |
| `/freshbooks-alternative` | Footer |
| `/locations/us-to-uk` | Footer |
| `/locations/uk-to-us` | Footer |
| `/locations/germany-to-us` | Footer |
| `/locations/us-to-germany` | Footer |
| `/locations/canada-to-us` | Footer |
| `/locations/us-to-canada` | Footer |
| `/locations/us-to-australia` | Footer |
| `/locations/australia-to-us` | Footer |
| `/blog/video-film-production-invoices` | Footer |
| `/blog/graphic-design-invoice` | Footer |
| `/blog/web-design-development-invoice` | Footer |
| `/blog/how-to-set-up-recurring-invoices` | Footer (also the "Consulting taxes" label) |
| `/blog/paypal-invoice-fees-are-they-worth-it` | Footer |
| `/blog/best-upwork-alternatives-12-platforms-to-find-better-work-in-2026` | Footer |
| `/blog/past-due-vs-overdue-invoices` | Footer |

### Pages one more click in

| Page | How it is reached |
|---|---|
| `/blog/<slug>` | Each card on `/blog` |
| `/usdc-invoicing`, `/usdt-invoicing`, `/stablecoin-invoicing`, `/exporters` | Footer column labels on the homepage named "USDC invoicing", "USDT invoicing", "Stablecoin Invoicing", "Transfer USDC to Bank", "Transfer USDT to Bank" in `data-framer-name` (confirm hrefs during capture; if a label is not an anchor, record it as static) |
| Persona template links on `/invoice-templates` | Freelance writers and consultants and contractors go to `/freelancer-invoicing`; agencies to `/agency-invoicing`; graphic design, web design, video, influencer posts as in the footer graph |
| Template file links on `/invoice-templates` | `.docx`, `.xlsx`, `.pdf` downloads on `framerusercontent.com`, plus two `docs.google.com` copy links. Not pages. Not submitted. |
| `/altitude` legal links | External: `https://altitude.xyz/legal/terms-of-service` ("Welcome Offer Terms"), `https://altitude.xyz/legal/cashback-terms` ("Cashback Terms"). Recorded, not captured as Acctual pages. |

### Blog index cards (from `/blog`, 2026-11-21)

The index lists these posts. Footer already reaches seven of them. The rest are reached from the index:

- `/blog/acctual-joins-altitude`
- `/blog/how-to-set-up-recurring-invoices`
- `/blog/what-is-contra-the-commission-free-freelance-platform-explained`
- `/blog/best-upwork-alternatives-12-platforms-to-find-better-work-in-2026`
- `/blog/how-to-accept-international-payments`
- `/blog/how-to-receive-money-from-abroad`
- `/blog/best-fiverr-alternatives-12-platforms-to-earn-more-in-2026`
- `/blog/consulting-taxes-how-to-do-taxes-as-an-independent-contractor`
- `/blog/paypal-invoice-fees-are-they-worth-it`
- `/blog/influencer-invoicing-how-to-get-paid-on-time`
- `/blog/stablecoin-directory`
- `/blog/payoneer-alternatives`
- `/blog/past-due-vs-overdue-invoices`
- `/blog/why-do-bank-transfers-take-so-long`
- `/blog/payment-methods-for-international-trade`
- `/blog/what-s-the-difference-between-an-invoice-vs-a-statement`
- `/blog/how-to-transfer-usdc-to-a-bank-account`
- `/blog/advantages-and-disadvantages-of-offshore-banking`
- `/blog/transferring-large-sums-of-money-internationally`
- `/blog/revolut-alternatives`
- `/blog/how-to-pay-an-invoice`
- `/blog/video-film-production-invoices`
- `/blog/how-to-transfer-usdt-to-a-bank-account`
- `/blog/how-to-send-usdt`
- `/blog/freelance-writer-invoicing`
- `/blog/graphic-design-invoice`
- `/blog/web-design-development-invoice`
- `/blog/how-to-send-usdc`
- `/blog/crypto-payroll-guide`
- `/blog/paying-freelancers-overseas`
- `/blog/stablecoin-tax-guide`
- `/blog/paying-international-contractors`
- `/blog/crypto-treasury-management-track-and-secure-digital-assets`
- `/blog/cross-border-b2b-payments`
- `/blog/what-is-otc-crypto`
- `/blog/best-payment-options-for-freelancers`
- `/blog/wise-alternatives`
- `/blog/get-paid-upwork-receive-stablecoins-crypto`
- `/blog/get-paid-same-day`
- further cards below the fold on `/blog` (the index is long; the sitemap lists the same set through `/blog/introducing-acctual-ap-ar-for-both-fiat-and-digital-assets`)

Posts share one article template. Capture the index, one representative post at both widths, and the footer-linked posts that are distinct entry points. Remaining posts are the same template, recorded in this tree.

## Help centre, reached from blog and location pages

A crawl on 2026-11-21 followed public links off the homepage graph and found a second public host. Blog posts and location pages link to it. It is not behind the sign-in wall. `help.acctual.com` returned HTTP 403 ("CNAME Cross-User Banned | Cloudflare") and was not captured.

| Control | Opens |
|---|---|
| In-article links on `/blog/revolut-alternatives`, `/blog/wise-alternatives`, `/blog/paypal-invoice-fees-are-they-worth-it`, and location pages | `https://guides.acctual.com/guide/getting-started` and the pages below |
| Help links on location pages and stablecoin landings | `https://help.acctual.com/` and article URLs. HTTP 403 from this client. Stop. |

Guide pages that loaded (HTTP 200), each linking the others:

| URL | Title |
|---|---|
| `https://guides.acctual.com/guide` | Guide index |
| `https://guides.acctual.com/guide/overview` | Overview |
| `https://guides.acctual.com/guide/getting-started` | Getting started |
| `https://guides.acctual.com/guide/send-an-invoice/create-send-an-invoice` | Create and send an invoice |
| `https://guides.acctual.com/guide/send-an-invoice/manage-invoices` | Manage invoices |
| `https://guides.acctual.com/guide/pay-a-bill/pay-a-bill-from-wallet` | Pay a bill from wallet |
| `https://guides.acctual.com/guide/pay-a-bill/pay-bills-from-a-safe` | Pay bills from a Safe |
| `https://guides.acctual.com/guide/pay-a-bill/pay-bills-in-batch` | Pay bills in batch |
| `https://guides.acctual.com/guide/pay-a-bill/pay-bills-off-platform` | Pay bills off-platform |
| `https://guides.acctual.com/guide/pay-a-bill/approvals` | Approvals |
| `https://guides.acctual.com/guide/pay-a-bill/internal-transfers` | Internal transfers |
| `https://guides.acctual.com/guide/payments/transfer-funds` | Transfer funds |
| `https://guides.acctual.com/guide/payments/create-flexible-payment-options` | Create flexible payment options |
| `https://guides.acctual.com/guide/add-a-team-member` | Add a team member |
| `https://guides.acctual.com/guide/manage-contacts` | Manage contacts |
| `https://guides.acctual.com/guide/resources/account-verification` | Account verification |
| `https://guides.acctual.com/guide/resources/faqs` | FAQs |
| `https://guides.acctual.com/guide/resources/rates-fees` | Rates and fees |

These are public documentation of the product, not the signed-in app. Capture the index, getting started, one invoice page, one pay-a-bill page, and rates and fees, at both widths. The rest share that docs template.

Also reached from the graph, not in the first homepage pass: `/free-invoice-software` (HTTP 200, same title as `/about`), `/about`, `/teams`, `/old-home`. `/blog/crypto-to-fiat` returned 404.

## Sitemap URLs not linked from the homepage

These exist in `sitemap.xml`. They are public. They are not opened by a control on the homepage, nav, or footer. Capture them if a later page links them; otherwise record them as sitemap-only.

| URL | Note |
|---|---|
| `/old-home` | Retired homepage |
| `/blog-old` | Retired blog index |
| `/404` | Error page |
| `/teams` | Team plan page. Not in the current nav (nav Agency goes to `/agency-invoicing`). |
| `/about` | Company page. Not in the current nav. |
| `/usdt-invoicing`, `/usdc-invoicing`, `/stablecoin-invoicing`, `/exporters` | Product landings. Confirm whether a homepage `data-framer-name` is an anchor. |
| `/locations/us-to-japan`, `/locations/japan-to-us`, `/locations/us-to-hong-kong`, `/locations/hong-kong-to-us`, `/locations/singapore-to-us`, `/locations/us-to-singapore`, `/locations/uae-to-us`, `/locations/us-to-uae`, `/locations/uae-to-uk`, `/locations/uk-to-uae`, `/locations/germany-to-uk`, `/locations/uk-to-germany` | Corridor template. Footer links eight other corridors, not these. |

## States to capture on the pages above

| State | Where | Notes |
|---|---|---|
| Default and full page | Every captured route | Desktop 1440x900 and phone 390x844 |
| Phone menu open | `/` at 390 | `Phone - Open` overlay |
| FAQ open | `/` | One accordion item |
| Invoice demo in view | `/` | Marketing mock, not the app |
| Hover, focus-visible, pressed | Nav links, capsule CTAs, footer links, announcement | Pressed via forced `:active`, not a real navigation into an auth wall |
| Dark theme | Not present | One light theme on the public site |

No cookie banner rendered on 2026-11-21. No dialog, toast, tooltip, select, checkbox, radio, switch, or text field exists on the public marketing surface. The invoice mock's fields are artwork.
