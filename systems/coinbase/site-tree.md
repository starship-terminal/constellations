# Coinbase public site tree

Mapped 2026-11-21 from https://www.coinbase.com/ in headed Chromium (channel Chrome), desktop 1440×900 and phone 390×844. The bare domain redirects to `/en-sg` (Singapore, English). Controls were expanded or read. No form was submitted. No email was typed. Passkey, Google, and Apple were not clicked. Cookie banners were hidden, never accepted or rejected.

The English sitemap is a catalog of assets, learn articles, blog posts, and legal revisions. This tree records the controls on the homepage, the menus, the footer, and the phone drawer, the page each one opens, and where a branch stops.

## Homepage header (desktop)

Sticky white bar under a promo strip. Promo text on this pass: "Sign up as an Accredited Investor and get S$300 Bitcoin on your first crypto".

| Control | Opens |
|---|---|
| Skip to content | In-page `#skip-nav-content` |
| Skip to site index | In-page `#footer-site-index` |
| Promo strip | `/en-sg/partner/ai-signup-offer` (signup offer page, public) |
| Wordmark | `/en-sg` |
| Crypto | `/en-sg/explore` |
| Individuals (`aria-controls=global-nav-dropdown-individuals`, `aria-expanded`) | Mega menu, not a page. Links below. |
| Businesses (`aria-controls=global-nav-dropdown-businesses`) | Mega menu. Panel id is `global-nav-dropdown-business` (the control id drops the final s). |
| Institutions (`aria-controls=global-nav-dropdown-institutions`) | Mega menu. Links below. |
| Developers (`aria-controls=global-nav-dropdown-developers`) | Mega menu. Links below. |
| Agents | `/en-sg/agents` |
| Company (`aria-controls=global-nav-dropdown-company`) | Mega menu. Links below. |
| Search (`button[aria-label=search]`, `data-testid=toggled-search-button`) | In-page search overlay. Does not navigate until a result is chosen. See Search. |
| Language (`button[aria-label="open language selector"]`) | Language dialog. See Region and language. |
| Sign in | `/signin?locale=en-sg`, which redirects to `https://login.coinbase.com/signin`. Auth wall. Stop. |
| Sign up | `/signup?type=picker`. Signup shell. Stop before submit. |

### Individuals menu

Opened 2026-11-21. Panel id `global-nav-dropdown-individuals`.

| Label | Opens |
|---|---|
| Crypto | `/en-sg/explore` |
| Token sales | `/en-sg/token-sales` |
| Advanced | `/en-sg/advanced-trade` |
| Coinbase One | `/en-sg/one` |
| USDC rewards | `/en-sg/usdc` |
| Coinbase Wallet | `https://wallet.coinbase.com` — other host. Stop. |
| Download app | `/en-sg/campaigns/download`. App-store links not followed. |

### Businesses menu

Opened 2026-11-21. Panel id `global-nav-dropdown-business`.

| Label | Opens |
|---|---|
| Business | `/en-sg/business` |
| Asset Listings | `/en-sg/listings` |
| Token Manager | `/en-sg/tokenmanager` |
| Coinbase Business (promo) | `/en-sg/business` |

### Institutions menu

Opened 2026-11-21. Panel id `global-nav-dropdown-institutions`.

| Label | Opens |
|---|---|
| Prime | `/en-sg/prime` |
| Trading and Financing | `/en-sg/prime/financing` |
| Custody | `/en-sg/prime/custody` |
| Staking | `/en-sg/staking` |
| Onchain Wallet | `/en-sg/prime/onchain-wallet` |
| Exchange | `/en-sg/exchange` |
| International Exchange | `/en-sg/international-exchange` |
| Derivatives Exchange | `/derivatives` (locale prefix dropped) |
| Verified Pools | `/en-sg/verified-pools` |
| Our clients | `/en-sg/institutional/clients/government` |

### Developers menu

Opened 2026-11-21. Panel id `global-nav-dropdown-developers`.

| Label | Opens |
|---|---|
| Coinbase Developer Platform | `/en-sg/developer-platform` |
| Payments | `/en-sg/payments` |
| Trading | `/en-sg/developer-platform/trading` |
| Wallets | `/en-sg/developer-platform/wallets` |
| Stablecoins | `/en-sg/developer-platform/products/stablecoin-as-a-service` |
| Banks & Brokerages | `/en-sg/developer-platform/banks` |
| Payment Firms | `/en-sg/developer-platform/paymentfirms` |
| Startups | `/en-sg/developer-platform/startups` |
| Learn more | `/en-sg/developer-platform` |

### Company menu

Opened 2026-11-21. Panel id `global-nav-dropdown-company`.

| Label | Opens |
|---|---|
| About | `/en-sg/about` |
| Careers | `/en-sg/careers` |
| Affiliates | `/en-sg/affiliates` |
| Support | `https://help.coinbase.com` — other host. Stop. |
| Blog | `/en-sg/blog` |
| Security | `/en-sg/security` |
| Create your account | `/en-sg/signup`. Signup shell. Stop. |

## Search

`button[aria-label=search]` opens an overlay on the same URL. Backdrop `data-testid=search-backdrop`. Field is `input[role=searchbox]` (`data-testid=search-input`, placeholder "Search"). Results mount in `data-testid=search-dropdown-results` without typing and without submitting.

Tabs in the overlay (role `tablist`, in-page, not a navigation): Top, Crypto, Stocks, Predictions, Perpetuals, Futures.

Default rows are not anchors. A Bitcoin row click on 2026-11-21 navigated to `/price/bitcoin` (the locale prefix dropped). Apple and the other stock rows are the same pattern toward `/stock/<ticker>`. No query was typed. Escape closes the overlay and stays on `/en-sg`.

## Region and language

No page-level theme control is public. The only appearance control is locale.

| Control | Result |
|---|---|
| Header globe (`button[aria-label="open language selector"]`) | Same dialog as the footer English button. |
| Footer button "English" | Dialog titled Language. Options: English, 中文. Buttons, no href. Not switched (would leave the mapped locale). Close control dismisses it. |
| Footer button "Singapore" | Dialog titled Country / region, with a search field inside the dialog (not submitted). Options read 2026-11-21: United States, Germany, United Kingdom, France, Canada, Spain, Brazil, Portugal, Australia, Singapore (current), Italy, Netherlands, Argentina, India, Mexico, Global. Buttons, no href. Not switched. |

## Homepage body (visible without opening a menu)

| Control | Opens |
|---|---|
| Sign up with Singpass | `http://coinbase.com/signup`. Signup shell. Stop. |
| Trade Options | `/en-sg/advanced-trade/options` |
| Learn more (XSGD) | `/en-sg/xsgd` |
| Learn more (Coinbase One) | `/en-sg/one` |
| See more assets | `/en-sg/explore` |
| Bitcoin price row | `/en-sg/price/bitcoin` |
| Ethereum price row | `/en-sg/price/ethereum` |
| Tether price row | `/en-sg/price/tether` |
| BNB price row | `/en-sg/price/bnb` |
| USDC price row | `/en-sg/price/usdc` |
| XRP price row | `/en-sg/price/xrp` |
| Try it now | `/en-sg/signup`. Signup shell. Stop. |
| What is Bitcoin? | `/en-sg/learn/crypto-basics/what-is-bitcoin` |
| When is the best time to invest in crypto? | `/en-sg/learn/tips-and-tutorials/dollar-cost-averaging` |
| How to keep your crypto secure? | `/en-sg/learn/crypto-basics/how-to-secure-crypto` |

Price rows are a live list. The six above were on screen on 2026-11-21. Each opens `/en-sg/price/<slug>`.

## Phone bar and drawer (390)

Bar, top to bottom of the chrome: promo strip, wordmark (`/en-sg`), search (`button[aria-label=search]`, same overlay), Sign up (`/signup`, stop), menu (`button[aria-label="open navigation menu"]`, `aria-expanded`).

Opened 2026-11-21. The drawer lists Crypto (`/explore`, locale prefix dropped), Individuals, Businesses, Institutions, Developers, Agents (`/agents`), Company, the language globe, and Sign in (`/signin?locale=en-sg`, auth wall, stop).

Each named section is `button[data-testid=mobile-menu-<id>-item]` and expands `aria-controls=global-nav-mobile-sublinks`. The expanded panel covers the next section button, so the next section is opened from script after the first collapses. Sublinks match the desktop menus, minus the desktop promo tiles (Download app, Coinbase Business promo, Our clients, developer Learn more, Create your account).

| Section | Phone sublinks |
|---|---|
| Individuals | `/en-sg/explore`, `/en-sg/token-sales`, `/en-sg/advanced-trade`, `/en-sg/one`, `/en-sg/usdc`, `https://wallet.coinbase.com` (other host, stop) |
| Businesses | `/en-sg/business`, `/en-sg/listings`, `/en-sg/tokenmanager` |
| Institutions | `/en-sg/prime`, `/en-sg/prime/financing`, `/en-sg/prime/custody`, `/en-sg/staking`, `/en-sg/prime/onchain-wallet`, `/en-sg/exchange`, `/en-sg/international-exchange`, `/derivatives`, `/en-sg/verified-pools` |
| Developers | `/en-sg/developer-platform`, `/en-sg/payments`, `/en-sg/developer-platform/trading`, `/en-sg/developer-platform/wallets`, `/en-sg/developer-platform/products/stablecoin-as-a-service`, `/en-sg/developer-platform/banks`, `/en-sg/developer-platform/paymentfirms`, `/en-sg/developer-platform/startups` |
| Company | `/en-sg/about`, `/en-sg/careers`, `/en-sg/affiliates`, `https://help.coinbase.com` (other host, stop), `/en-sg/blog`, `/en-sg/security` |

The language globe in the drawer is the same `button[aria-label="open language selector"]`. On this pass a cookie dialog sat on top of the first click, so the language dialog was confirmed from the desktop footer control instead. Cookie controls were not accepted.

## Footer (same shell on public pages)

No heading elements. Groups read from link order on 2026-11-21.

| Control | Opens |
|---|---|
| About | `/en-sg/about` |
| Careers | `/en-sg/careers` |
| Affiliates | `/en-sg/affiliates` |
| Blog | `/en-sg/blog` |
| Press | `/en-sg/press` |
| Security | `/en-sg/security` |
| Investors | `https://investor.coinbase.com/` — other host. Stop. |
| Vendors | `/en-sg/vendors/vendors-at-coinbase` |
| Legal & privacy | `/en-sg/legal` |
| Cookie policy | `/en-sg/legal/cookie` |
| Cookie preferences | `/en-sg#` — in-page consent manager. Not opened (would be a consent POST if accepted). |
| Digital Asset Disclosures | `/en-sg/legal/digital-asset-disclosures` |
| Explore crypto | `/en-sg/explore` |
| Explore stocks | `/en-sg/stock/explore` |
| Market statistics | `/en-sg/market-stats` |
| Coinbase Bytes newsletter | `/en-sg/bytes`. Newsletter page. Not subscribed. |
| Crypto basics | `/en-sg/learn/crypto-basics` |
| Tips & tutorials | `/en-sg/learn/tips-and-tutorials` |
| Crypto glossary | `/en-sg/learn/crypto-glossary` |
| Market updates | `/en-sg/learn/market-updates` |
| What is Bitcoin? | `/en-sg/learn/crypto-basics/what-is-bitcoin` |
| What is crypto? | `/en-sg/learn/crypto-basics/what-is-cryptocurrency` |
| What is a blockchain? | `/en-sg/learn/crypto-basics/what-is-a-blockchain` |
| How to set up a crypto wallet? | `/en-sg/learn/tips-and-tutorials/how-to-set-up-a-crypto-wallet` |
| How to send crypto? | `/en-sg/learn/tips-and-tutorials/how-to-send-crypto` |
| Taxes | `/en-sg/learn/crypto-basics/understanding-crypto-taxes` |
| Buy & sell | `/en-sg/explore` |
| Coinbase Wallet | `https://base.app` — other host. Stop. |
| Coinbase One | `/en-sg/one` |
| Debit Card | `/en-sg/card` |
| Token Sales | `/en-sg/token-sales` |
| Asset Listings | `/en-sg/listings` |
| Payments | `/en-sg/payments` |
| Token Manager | `/en-sg/tokenmanager` |
| Prime | `/en-sg/prime` |
| Staking | `/en-sg/staking` |
| Exchange | `/en-sg/exchange` |
| International Exchange | `/en-sg/international-exchange` |
| Derivatives Exchange | `/derivatives` |
| Verified Pools | `/en-sg/verified-pools` |
| Developer Platform | `/en-sg/developer-platform` |
| Base | `https://base.org` — other host. Stop. |
| Server Wallets | `/en-sg/developer-platform/products/wallets` |
| Embedded Wallets | `/en-sg/developer-platform/products/embeddedwallets` |
| Base Accounts (Smart Wallets) | `https://www.base.org/build/base-account` — other host. Stop. |
| Onramp & Offramp | `/en-sg/developer-platform/products/onramp` |
| x402 | `https://www.x402.org` — other host. Stop. |
| Trade API | `/en-sg/developer-platform/products/trade-api` |
| Paymaster | `/en-sg/developer-platform/products/paymaster` |
| OnchainKit | `https://www.base.org/build/onchainkit` — other host. Stop. |
| Data API | `/en-sg/developer-platform/products/data-api` |
| Verifications | `/en-sg/developer-platform/products/verifications` |
| Node | `/en-sg/developer-platform/products/node` |
| AgentKit | `/en-sg/developer-platform/products/agentkit` |
| Staking (developer) | `/en-sg/developer-platform/products/staking` |
| Faucet | `/en-sg/developer-platform/products/faucet` |
| Exchange API | `/en-sg/developer-platform/products/exchange-api` |
| International Exchange API | `https://docs.cdp.coinbase.com/international-exchange/introduction/welcome` — docs host. Stop. |
| Prime API | `https://docs.cdp.coinbase.com/prime/introduction/welcome` — docs host. Stop. |
| Derivatives API | `https://docs.cdp.coinbase.com/derivatives/introduction/welcome` — docs host. Stop. |
| Help center | `https://help.coinbase.com` — other host. Stop. |
| Contact us | `https://help.coinbase.com/contact-us/` — other host. Stop. |
| Create account | `https://help.coinbase.com/coinbase/getting-started/getting-started-with-coinbase/create-a-coinbase-account/` — help host. Stop. |
| ID verification | `https://help.coinbase.com/coinbase/managing-my-account#identity-verification/` — help host. Stop. |
| Account information | `https://help.coinbase.com/coinbase/managing-my-account/` — help host. Stop. |
| Payment methods | `https://help.coinbase.com/coinbase/getting-started#add-a-payment-method/` — help host. Stop. |
| Account access | `https://help.coinbase.com/coinbase/managing-my-account/` — help host. Stop. |
| Supported crypto | `https://help.coinbase.com/supported-crypto.html` — help host. Stop. |
| Status | `https://status.coinbase.com` — other host. Stop. |
| Bitcoin price | `/en-sg/price/bitcoin` |
| Ethereum price | `/en-sg/price/ethereum` |
| Solana price | `/en-sg/price/solana` |
| XRP price | `/en-sg/price/xrp` |
| NVIDIA price | `/en-sg/stock/nvda` |
| Apple price | `/en-sg/stock/aapl` |
| Microsoft price | `/en-sg/stock/msft` |
| Amazon price | `/en-sg/stock/amzn` |
| Coinbase X account | `https://x.com/coinbase` — external. Stop. Not clicked. |
| Coinbase LinkedIn page | `https://www.linkedin.com/company/coinbase` — external. Stop. Not clicked. |
| Coinbase Instagram page | `https://www.instagram.com/coinbase/` — external. Stop. Not clicked. |
| Coinbase Tiktok page | `https://www.tiktok.com/@coinbase` — external. Stop. |
| Privacy | `/legal/privacy` |
| Terms & Conditions | `/legal/user_agreement` |
| Singapore (button) | Country / region dialog. See Region and language. |
| English (button) | Language dialog. See Region and language. |

## Auth and signup walls (stop)

| URL | Why the branch stops |
|---|---|
| `https://login.coinbase.com/signin` | Loaded 2026-11-21 from `/signin`. Title "Coinbase - Sign in". Email field, Continue, Sign in with passkey, Sign in with Google, Sign in with Apple, Sign up. Cookie policy links only. No email typed. Passkey, Google, and Apple not clicked. Continue not clicked. A prior probe (2026-11-17) had accepted an email and then asked for a password. This pass stopped before that. |
| `/signup`, `/en-sg/signup`, `http://coinbase.com/signup` | Signup shells, including Singpass. Not opened past the link. No account created. |
| `/en-sg/partner/ai-signup-offer` | Public offer page. Signup form on it not filled. |
| Help, status, investor, wallet, base, docs, x402 | Other hosts. Recorded, not walked. |

## In-page interactions on captured pages

| Page | Control | Result |
|---|---|---|
| `/en-sg` desktop | Individuals, Businesses, Institutions, Developers, Company | Mega menu |
| `/en-sg` desktop | Search | Overlay with tabs and default rows. Escape closes it. |
| `/en-sg` desktop | English / Singapore / globe | Language or region dialog. Not switched. |
| `/en-sg` phone | Menu button | Full-screen nav. Close returns `aria-expanded=false`. |
| `/en-sg` phone | Section button | Sublink list in `#global-nav-mobile-sublinks` |
| `/en-sg/explore` | Filter chips and sort | In-page. Not a navigation. |
| Any page | Cookie / consent dialog | Hidden, never accepted or rejected. |

## Catalog depth not walked page by page

These indexes are reachable from the tree above. Their children share one template. One index plus one child stands in for the set.

| Index | Child example |
|---|---|
| `/en-sg/explore` | `/en-sg/price/bitcoin` |
| `/en-sg/stock/explore` | `/en-sg/stock/aapl` |
| `/en-sg/learn` | `/en-sg/learn/crypto-basics/what-is-bitcoin` |
| `/en-sg/learn/crypto-basics` | the three basics links in the footer |
| `/en-sg/learn/tips-and-tutorials` | `/en-sg/learn/tips-and-tutorials/how-to-set-up-a-crypto-wallet` |
| `/en-sg/blog` | first post linked from the index, if one is on screen |
| `/en-sg/legal` | `/legal/privacy` and `/legal/user_agreement` |
| `/en-sg/developer-platform` | the product pages named in the Developers menu and the footer |
| `/en-sg/prime` | `/en-sg/prime/financing`, `/en-sg/prime/custody`, `/en-sg/prime/onchain-wallet` |
| `/en-sg/careers` | index only. Applications not opened. |

## Not a public design surface

`/signup` after the first screen, `login.coinbase.com` after the sign-in card, wallet connect, app-store badges, locale mirrors other than `/en-sg`, and social profiles. Recorded here so a later pass does not treat a miss as a forgotten control.
