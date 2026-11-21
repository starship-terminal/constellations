# Stocktwits public site tree

Mapped from https://stocktwits.com/ on 2026-11-21, signed out, before the screenshot pass. Playwright, headless Chromium, desktop 1440x900. Consent is a OneTrust dialog ("We Care About Your Privacy"). It was hidden for mapping, never accepted or rejected, because those buttons POST.

The product paints one theme. `html` carries `class="light"` and `data-theme="light"` even when the browser prefers dark. No public theme control was found.

A control that opens `/signin` or `/signup` is a wall. That URL is recorded and the branch stops. No email, username, password, or other form field was typed. No form was submitted. Apple, Google, Facebook, and X sign-in buttons were not clicked.

## Shell

| Control | Opens |
|---|---|
| Logo (home) | `/` stream |
| Chevron beside the logo | "Choose Your Experience" dialog: stocktwits (standard app) and cryptotwits (crypto-first). Escape closes it. Neither Google nor Apple is in this dialog. |
| Left rail, always visible | Continue with Google (not clicked), Continue with Apple (not clicked), Create Account (`/signup?next=/`), Log in to existing account (`/signin?next=/`) |
| Search field "Search stocks, crypto, and people" | Listbox of trending symbols. Clicking a row opens that symbol or coin. Typing was not used. Escape closes it. |
| AI Agent | External https://ai.stocktwits.com/connect. Left as a link, not captured. |
| Trending | `/sentiment` |
| News | `/news-articles` |
| Earnings (live-calls badge) | `/sentiment/calendar` |
| Ticker "All" | Filter menu on the marquee (Stocks, Crypto, and related sets). Selecting a set filters the ticker in place. |
| Ticker symbol pill | `/symbol/{TICKER}` or `/coins/{slug}` |
| Pause trending ticker animation | Pauses the marquee. Same control resumes it. |
| Fire icon | `/sentiment/trending` |
| For You | Home stream, in place. Default. |
| Following | Same URL. Signed-out stream stays on the public feed; no following list. |
| Log In | `/signin` wall. Stop. |
| Sign Up | `/signup` wall. Stop. |
| Use App | External `stocktwits.onelink.me` app install. Not captured. |
| Remove ads | `/subscriptions` |
| ChatGPT / Claude links in the rail | External. Not captured. |
| Your Privacy Choices (footer) | OneTrust preference dialog. Not opened (consent POST). |
| Report a problem | Opens a report control. Not submitted. |

## Home stream

| Control | Opens |
|---|---|
| Watchlist row (AAPL, MSFT, NVDA, QQQ, SPY, TSLA) | `/symbol/{TICKER}` |
| Watchlist row (BTC) | `/coins/bitcoin` |
| Customize Watchlist | `/signup?next=/` wall. Stop. |
| Trending card | `/symbol/{TICKER}` |
| View all trending tickers | `/sentiment` |
| Message author | `/{handle}` public profile |
| Message timestamp | `/{handle}/message/{id}` |
| Cashtag in a message | `/symbol/{TICKER}` |
| Reply, Reshare, Like, Share | `/signin` wall. Stop. Not submitted. |
| Discussion card | `/discussions/{slug}/{id}` |
| News card in the rail | `/news-articles/markets/.../{id}` |
| Footer About, Best Practices, Disclaimer, Privacy, Rules, Terms, Disclosures, Enterprise, Subscriptions, Widgets, Advertise, Newsletters, Symbols Directory, Coins Directory, Beehiiv Network, About Newsroom | The matching public page below |
| Footer Careers, Shop, Help | External (`about.stocktwits.com`, `shop.stocktwits.com`, `help.stocktwits.com`). Not captured. |
| Footer X, Instagram, Facebook, YouTube | External. Not clicked. |

## Symbol `/symbol/AAPL`

| Control | Opens |
|---|---|
| Feed | `/symbol/AAPL` |
| News | `/symbol/AAPL/news` |
| Sentiment | `/symbol/AAPL/sentiment` |
| Earnings | `/symbol/AAPL/earnings` |
| Futures | `/symbol/AAPL/futures` |
| Fundamentals | `/symbol/AAPL/fundamentals` |
| Info | `/symbol/AAPL/about` |
| Expand full chart / Full Chart | Chart dialog on the same page. Escape closes it. |
| Show more about AAPL | Expands the about blurb in place. |
| View watcher stats | Stats popover. Signed-out. |
| Remove from watchlist / Watch | `/signup` wall. Stop. |
| Breadcrumb Home, Symbol | `/`, `/symbol` |

## Other public pages

| Page | How it is reached | Notes |
|---|---|---|
| `/sentiment` | Trending nav, or View all trending tickers | Ranked symbols. A row opens `/symbol/{TICKER}`. |
| `/sentiment/trending` | Fire icon | Trending list. |
| `/sentiment/calendar` | Earnings nav | Calendar of calls. A row opens a symbol. |
| `/news-articles` | News nav | Article list. A card opens `/news-articles/.../{id}`. |
| `/news-articles/markets/equity/{slug}/{id}` | A news card | Public article. |
| `/discussions` | Home discussion cards and footer-adjacent links | Discussion index. |
| `/discussions/{slug}/{id}` | A discussion card | Public thread. Reply is a wall. |
| `/symbol` | Footer Symbols Directory, symbol breadcrumb | A–Z directory. A letter filters in place. A row opens a symbol. |
| `/coins` | Footer Coins Directory | Coin index. A row opens `/coins/{slug}`. |
| `/coins/bitcoin` | Watchlist BTC, coin index | Coin page. Same tab pattern as a symbol where the product shows it. |
| `/{handle}` | A message author | Public profile. Follow is a wall. |
| `/{handle}/message/{id}` | A message timestamp | Single message. Reply is a wall. |
| `/about` | Footer | Marketing page. |
| `/about/best-practices` | Footer | Static. |
| `/about/rules` | Footer | Static. |
| `/about/legal/disclaimer` | Footer | Static. |
| `/about/legal/privacy` | Footer | Static. |
| `/about/legal/terms` | Footer | Static. |
| `/about/legal/disclosures/` | Footer | Static. |
| `/about/contact/` | Footer Advertise | Contact form. Not filled. Not submitted. |
| `/enterprise` | Footer | Sales form (name, job, work email, company). Not filled. Not submitted. |
| `/subscriptions` | Footer, Remove ads | Plan cards. Checkout not started. |
| `/widgets` | Footer | Widget embed preview. No form submit. |
| `/newsletters` | Footer | Newsletter list. Subscribe not clicked (would collect an address). |
| `/newsletters/beehiiv` | Footer Beehiiv Network | Partner page. No signup. |
| `/about-newsroom` | Footer | Newsroom index. |
| `/signin` | Log In | Wall. Fields: Email or Username, Password. Forgot password links to `/reset-password` (not opened as a form). Continue with Apple not clicked. Turnstile present. Nothing typed. |
| `/signup` | Sign Up, Create Account | Wall. Email field visible. Nothing typed. Continue with Apple not clicked. |
| `/reset-password` | Forgot your password? | Wall. Not opened beyond recording the link. |

## Phone 390x844

| Control | Opens |
|---|---|
| Menu (hamburger) | Full-screen drawer: Continue with Google (not clicked), Continue with Apple (not clicked), Create Account (`/signup`), Log in to existing account (`/signin`), Explore links (Trending, Earnings, Newsletters, News, Symbols Directory, Coins Directory, Widgets, Enterprise), Learn more (House Rules, Best Practices, About). Close returns to the stream. |
| Search icon | Search field. Not typed into. |
| Use App | External install link. Not captured. |
| Chevron beside the logo | Same Choose Your Experience dialog as desktop. |
| Tab bar Home | `/` |
| Tab bar Watchlist | `/signup` wall. Stop. |
| Tab bar Trending | `/sentiment` |
| Tab bar News | `/news-articles` |
| Tab bar Explore | Search / explore. Not typed into. |
| Tab bar Profile | `/signin` wall. Stop. |

## Not in this capture

Signed-in watchlists, Following as a personal feed, compose, reply, like, reshare, settings, theme (none public), checkout, newsletter subscribe, and every OAuth button.
