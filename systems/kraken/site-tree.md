# Kraken public site tree

Mapped from [https://www.kraken.com/](https://www.kraken.com/) on 2026-11-21 with Playwright, signed out. Desktop viewport 1440 by 900. The OneTrust cookie banner was hidden in CSS. Accept All Cookies was not clicked.

`signed_in` is false. The sign-in and sign-up walls were opened only far enough to see what they ask for. Nothing was typed. Google, Apple, and passkey were not clicked. No form was submitted.

Prices in the Markets menu and the search overlay are live quotes from that session. They are not design tokens.

## Header

| Control | Opens |
|---|---|
| Logo (home) | Page `/` |
| Kraken | Menu. The link itself goes to `/app` |
| Pro | Menu. The link itself goes to `/pro` |
| Wallet | Menu. The link itself goes to `/wallet` |
| Prime | Menu. The link itself goes to `/prime` |
| VIP | Page `/vip`. No menu |
| Markets | Menu |
| About | Menu |
| Search | Overlay. Placeholder "Find your next trade". Lists popular markets, newly listed crypto, and categories. Escape closes it |
| EN | Overlay "Change language and country/region", with Language and Country comboboxes and Continue. Continue was not clicked |
| Log in | Page `https://id.kraken.com/sign-in` (also `/sign-in` on www). See [login-review.json](login-review.json) |
| Sign up | Page `/sign-up`. See [login-review.json](login-review.json) |

## Kraken menu

| Item | Opens |
|---|---|
| Log in | Sign-in wall, `preferTheme=light` |
| Sign up | `/sign-up` |
| Kraken brand header | `/app` |
| xStocks | `/app/xstocks` |
| Borrow | `/app/borrow` |
| Onchain | `/app/onchain` |
| Auto earn | `/app/auto-earn` |
| Perpetual futures | `/app/perpetual-futures` |
| Kraken+ | `/app/kraken-plus` |
| Dollar Cost Averaging | `/app/dollar-cost-averaging` |
| Crypto card | `/app/crypto-card` |
| Buy crypto | `/buy` |
| Buy xStocks | `/xstocks` |
| Command-center promo | `https://pro.kraken.com/app/home` (signed-in app, not entered) |

## Pro menu

| Item | Opens |
|---|---|
| Log in | Sign-in wall, `rfr=pro-web`, `preferTheme=dark`. Not followed |
| Get a free account | `/sign-up` |
| Pro brand header | `/pro` |
| Explore the app | `https://pro.kraken.com` (app host, not entered) |
| Crypto spot | `/pro/spot` |
| Margin | `/pro/margin` |
| Perps | `/pro/perps` |
| xStocks | `/pro/xstocks` |
| Options | `/pro/options` |
| Staking | `/pro/staking` |
| Pro fees | `/pro/fees` |
| Liquidity providers | `/pro/liquidity-provider-program` |
| Prop funding | `/pro/prop` |
| Desktop app | `/pro/desktop` |
| TradingView | `/pro/tradingview` |
| CLI trading | `/kraken-cli` |
| Trade markets | `https://pro.kraken.com/app/trade` (not entered) |
| OTC | `https://pro.kraken.com/app/otc/quote` (not entered) |
| Rewards hub | `https://pro.kraken.com/app/promos/overview` (not entered) |

## Wallet menu

| Item | Opens |
|---|---|
| Wallet brand header | `/wallet` |
| Explore the app | `https://wallet.kraken.com` (not entered) |
| Portfolio, earn, swap | `/wallet#features` |
| Your keys | `/wallet#custody` |
| Multi-chain | `/wallet#networks` |
| FAQs | `/wallet#faq` |

## Prime menu

| Item | Opens |
|---|---|
| Log in | Sign-in wall, Pro theme query. Not followed |
| Get in touch | `/prime#contact` |
| Prime brand header | `/prime` |
| OTC | `/prime#otc` |
| Custody | `/prime#custody` |
| Staking | `/prime#staking` |
| Prime eligibility | `/prime#who-we-serve` |

## Markets menu

| Item | Opens |
|---|---|
| Browse crypto prices | `/prices` |
| AAPL, MSFT, GOOGL quotes | `/stocks/aapl`, `/stocks/msft`, `/stocks/googl` |
| Learn more | `/stocks` |
| BTC, ETH, XRP quotes | `https://pro.kraken.com/app/trade/...` (not entered) |
| Crypto in app | `https://pro.kraken.com/app/markets/spot/crypto` (not entered) |
| BTC, ETH, SOL perpetual quotes | `https://pro.kraken.com/app/trade/futures-...` (not entered) |
| Futures in app | `https://pro.kraken.com/app/markets/futures` (not entered) |

## About menu

| Item | Opens |
|---|---|
| Payward.com | `https://payward.com` |
| Why Kraken | `/why-kraken` |
| Leading security | `/features/security` |
| Deep liquidity | `/features/liquidity` |
| Proof of reserves | `/proof-of-reserves` |
| Affiliates | `/affiliate` |
| Learn | `/learn` |
| Support | `https://support.kraken.com` |
| Payward newsroom | `https://payward.com/newsroom` |

## Homepage body

| Control | Opens |
|---|---|
| Email field, placeholder `satoshi@email.com` | Text field on the hero. Not filled |
| Try Kraken | Same hero signup block. Not submitted |
| Sign in with Apple | Identity provider. Not clicked |
| Sign in with Google | Identity provider. Not clicked |
| Sign up now | Signup wall. Not submitted |
| Product cards (Pro, Kraken app, Wallet, Krak) | Marketing pages or app-download links |
| Market tabs (Crypto, Spot / Margin, Futures, xStocks) | In-page table filter |
| Asset rows | Price pages such as `/prices/bitcoin`, or Pro trade URLs |
| View all crypto | `/prices` |
| Accept All Cookies | OneTrust consent. Not clicked. Banner hidden |
| Manage Cookie Settings | OneTrust preference center. Not opened |

## Footer

Footer columns link to public pages. Social icons leave the site (Instagram, Facebook, LinkedIn, X, YouTube, TikTok, Reddit) and were not followed.

| Column | Opens |
|---|---|
| Features | `/features`, `/buy`, `/sell`, `/features/margin-trading`, Pro perpetuals, `/prime`, `/features/api-trading`, `/features/staking`, `/features/dollar-cost-averaging`, `/features/borrow`, `/features/funded` |
| About | `/why-kraken`, `/features/security`, `/careers`, `https://blog.kraken.com`, `https://docs.kraken.com/api`, `/affiliate`, `/listings`, `https://status.kraken.com/`, Support Center, complaints article |
| Prices | `/prices` and per-asset pages (`/prices/bitcoin`, `/prices/ethereum`, and others) |
| Convert | `/convert` and pairs such as `/convert/btc/usd` |
| Buy crypto | `/buy` and `/buy/btc`, `/buy/eth`, and others |
| Buy stocks | `/stocks` and `/stocks/nvda`, `/stocks/tsla`, and others |
| Tokenized equities | `/xstocks` and `/xstocks/nvdax`, and others |
| Learn | `/learn` and articles such as `/learn/what-is-cryptocurrency` |
| Legal | `/privacy-hub`, `/legal/privacy`, `/legal/cookies`, `/compliance`, `/legal`, trading rules, disclosures |

## Pages opened

Each of these returned a public marketing page (HTTP 200) with its own headline. Signed-in hosts (`pro.kraken.com`, `wallet.kraken.com`, `id.kraken.com` past the wall) were not entered.

`/`, `/app`, `/pro`, `/wallet`, `/prime`, `/vip`, `/why-kraken`, `/features`, `/features/security`, `/features/liquidity`, `/features/margin-trading`, `/proof-of-reserves`, `/affiliate`, `/learn`, `/buy`, `/sell`, `/prices`, `/prices/bitcoin`, `/prices/ethereum`, `/prices/tether`, `/prices/bnb`, `/prices/usdc`, `/prices/xrp`, `/xstocks`, `/kraken-cli`, `/kraken-app`, `/krak`, `/legal`, `/legal/equities`, `/app/xstocks`, `/app/borrow`, `/app/onchain`, `/app/auto-earn`, `/app/perpetual-futures`, `/app/kraken-plus`, `/app/dollar-cost-averaging`, `/app/crypto-card`, `/pro/spot`, `/pro/margin`, `/pro/perps`, `/pro/xstocks`, `/pro/options`, `/pro/staking`, `/pro/fees`, `/pro/liquidity-provider-program`, `/pro/prop`, `/pro/desktop`, `/pro/tradingview`, `/sign-in`, `/sign-up`.

## Phone width

At 390 wide the header collapses. Visible controls: logo, Sign up, Search, a menu button, and Get the app (an app-download link). The menu button opens a navigation sheet. Apple and Google buttons on the hero were not clicked.
