# Shopify public site tree

Mapped from the live public site on 2026-11-21, before screenshots, in headless Chromium at 1440x900. The bare URL `https://www.shopify.com/` redirects to a geo locale (this machine landed on `https://www.shopify.com/sg`). The tree below is the US English storefront at `https://www.shopify.com/?country=us&lang=en`, which stays on the US host. The same chrome exists on `/sg`.

Account: signed out. No form was submitted. No email was typed.

## How the header works

The header is one `header` bar, 72px tall. Desktop items:

| Control | Opens |
|---|---|
| Logo (`a` to `/`) | Home |
| Why Shopify (`label` for hidden checkbox `#bk-nav-Why Shopify`) | Mega menu, not a new page. Hover or the label opens it. Escape or moving away closes it. |
| Products (`label` for `#bk-nav-Products`) | Mega menu, same mechanism |
| Pricing (`a` to `/pricing`) | Pricing page |
| Enterprise (`a` to `/enterprise`) | Enterprise page |
| Fall '26 Edition (`a` to `/editions/fall2026`) | Editions page. Label text is hidden under 1300px; the mark stays. |
| Log in (`a` to `/login?ui_locales=en`) | Leaves the marketing site. Recorded as a wall. Branch stopped. |
| Start for free (`a` to `admin.shopify.com/signup`) | Signup wall. Branch stopped. Not clicked during capture. |

Phone (390): the level-1 list is off-screen until the hamburger `label` (three bars, no text) checks `#bk-nav-hamburger`. That drawer holds Why Shopify, Products, Pricing, Enterprise, Fall '26 Edition, and Log in. Start for free stays in the bar.

## Why Shopify menu

| Item | Opens |
|---|---|
| Get started fast | `/start` |
| Switch to Shopify | `/sell` |
| Trusted by enterprise brands | `/enterprise` |
| World's best checkout | `/checkout` |
| Sidekick | `/sidekick` |

## Products menu

Column labels are headings, not links.

BUILD YOUR WEBSITE

| Item | Opens |
|---|---|
| Website Builder | `/website/builder` |
| Themes | `https://themes.shopify.com/` (public theme store) |
| Domains | `/domains` |
| Customer Accounts | `/customer-accounts` |
| Sidekick | `/sidekick` |

SELL ANYWHERE

| Item | Opens |
|---|---|
| Online | `/online` |
| AI Chats | `/agentic-storefronts` |
| Catalog | `/catalog` |
| Point of Sale | `/pos` |
| Shop App | `/shop` |
| Social & Marketplaces | `/channels` |
| Global | `/international` |
| B2B | `/solutions/b2b` |
| Across Markets | `/markets` |

MARKETING & ANALYTICS

| Item | Opens |
|---|---|
| Advertising & Campaigns | `/marketing` |
| Email & Customer Chat | `/marketing-automation-tools` |
| Discounts | `/discounts` |
| Analytics | `/analytics` |
| Test & Launch | `/test-and-launch` |

RUN YOUR BUSINESS

| Item | Opens |
|---|---|
| Orders & Inventory | `/orders` |
| Shipping | `/shipping` |
| Finances & Funding | `/finance` |
| Workflow Automation | `/flow` |
| Mobile | `/mobile` |

GET PAID

| Item | Opens |
|---|---|
| Checkout | `/checkout` |
| Payments | `/payments` |
| Taxes | `/tax` |

CUSTOMIZE & EXTEND SHOPIFY (belt, opens a new host)

| Item | Opens |
|---|---|
| Build shopping anywhere | `https://shop.dev/` |
| Shopify App Store | `https://apps.shopify.com/` |
| Shopify.dev | `https://shopify.dev/` |

NON-STOP INNOVATION

| Item | Opens |
|---|---|
| Shopify Editions | `/editions/fall2026` |
| Shopify Protect | `/editions/fall2026#fraud-prevention-with-shopify-protect` |
| Shop.dev | `/editions/fall2026#shop-dev-for-builders` |
| Canvas | `/editions/fall2026#online-store-canvas` |

## Home page interactions

| Control | Opens |
|---|---|
| Start for free (hero and closing band) | `admin.shopify.com/signup`. Wall. Not followed. |
| "Start with your agent" copy button | Copies a prompt to the clipboard. No navigation. Not a form. |
| Play testimonial video | In-page video dialog. |
| Merchant name links (Steve Madden, Glossier, and the rest of the logo rail) | External merchant stores. Not Shopify UI. Not followed. |
| Section links (Agentic Storefronts, online store, payments, fulfillment, retail, channels, Markets, shipping, pricing, Sidekick, UCP, checkout, Shop Pay, Capital) | The matching marketing page in the tables above, plus `/ucp`, `/shop-pay`, `/capital` |
| 21,000+ commerce apps | `https://apps.shopify.com/` |
| Hydrogen, storefronts, agents, apps, shopify.dev | `shopify.dev` and `hydrogen.shopify.dev`. Public docs. |
| Hell Babes | External merchant store. Not followed. |

## Footer

Three columns, then a legal row. Region control is a button, not a link.

Shopify

| Item | Opens |
|---|---|
| What is Shopify? | `/blog/what-is-shopify` |
| Shopify Editions | `/editions` |
| Careers | `/careers` |
| Investors | `/investors` |
| Newsroom | `/news` |
| Sustainability | `/climate` |

Ecosystem

| Item | Opens |
|---|---|
| Developer Docs | `https://shopify.dev/docs` |
| Theme Store | `https://themes.shopify.com/` |
| App Store | `https://apps.shopify.com/` |
| Partners | `/partners` |
| Affiliates | `/affiliates` |

Resources

| Item | Opens |
|---|---|
| Blog | `/blog` |
| Compare Shopify | `/compare` |
| Guides | `/blog/topics/guides` |
| Free Tools | `/tools` |
| Changelog | `https://changelog.shopify.com/` |

Support

| Item | Opens |
|---|---|
| Shopify Help Center | `https://help.shopify.com/en` |
| Community Forum | `https://community.shopify.com/` |
| Hire a Partner | `/partners/directory` |
| Service Status | `https://shopifystatus.com/` |

Legal row: Terms of Service (`/legal/terms`), Legal (`/legal`), Privacy Policy (`/legal/privacy`), Sitemap (`/sitemap`), Your Privacy Choices (`https://privacy.shopify.com/en`).

Social icons (Facebook, Twitter, YouTube, Instagram, TikTok, LinkedIn, Pinterest) leave the site. Not followed. Facebook is in the do-not-click list.

## Region dialog

Button label "USA | English", `aria-controls="language-selector-popover"`. Opens a dialog titled "Choose a region & language". A country list and a language list. Confirm stays on the current locale (`/?country=us&lang=en`). Close modal dismisses it. Other locales are the same marketing site in another language. They were not captured as separate packages.

## Walls (branch stopped)

| Control | URL observed |
|---|---|
| Log in | `https://www.shopify.com/login` redirects to `https://accounts.shopify.com/lookup` (email, password, passkey, Google, Apple, Facebook, WhatsApp). Password not submitted. |
| Start for free | `https://admin.shopify.com/signup?...` Account creation. Not opened for a form. |

Admin, checkout of a store, and any page that asks for an email stay out of the capture.
