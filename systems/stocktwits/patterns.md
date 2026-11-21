# Patterns

Public Stocktwits, signed out, light, 2026-11-21. Screenshots are in [screenshots/](screenshots). The control map is [site-tree.md](site-tree.md).

## App shell

Desktop is three columns. A left rail holds Google and Apple (not clicked), Create Account, a login link, a sample watchlist, and the footer. The centre is the stream. The right rail is news. The top bar is search, Trending, News, and Earnings. Phone drops the rail into a menu and adds a tab bar: Home, Watchlist, Trending, News, Explore, Profile. Watchlist and Profile are login walls.

Shown in [screenshots/home-light-default.png](screenshots/home-light-default.png) and [screenshots/mobile-home-light-default.png](screenshots/mobile-home-light-default.png).

## Stream

For You is the default. Following stays on the same public feed when signed out. Messages show a handle, a time, cashtags, and Reply, Reshare, Like, Share. Those actions open `/signin`. The branch stops there.

## Symbol

`/symbol/AAPL` is a quote header, a chart that expands in place, Bullish and Bearish chips, and tabs for Feed, News, Sentiment, Earnings, Futures, Fundamentals, and Info. Shown in [screenshots/symbol-light-default.png](screenshots/symbol-light-default.png) and [screenshots/symbol-light-chart.png](screenshots/symbol-light-chart.png).

## Table

`/sentiment` is a ranked table with Equities and Crypto filters and chips for Trending, Most Active, Watchers, Most Bullish, Most Bearish, Top Gainers, and Top Losers. A fade and a Sign Up / Log In pair sit under the first rows. Shown in [screenshots/sentiment-light-default.png](screenshots/sentiment-light-default.png).

## Plans

`/subscriptions` is three cards on a dark band: Ad Free, Edge, Enterprise. Subscribe and Get In Touch were not clicked. Shown in [screenshots/subscriptions-light-default.png](screenshots/subscriptions-light-default.png).

## Auth wall

`/signin` is a split page: black panel, white form, Email or Username, Password, a disabled Log In, Forgot your password, Sign up, and Continue with Google and Continue with Apple. Nothing was typed. Shown in [screenshots/signin-light-default.png](screenshots/signin-light-default.png).

## Empty, loading, error, destructive, onboarding

Empty and loading states of the signed-in app were not reached. No destructive confirm was public. Onboarding starts at signup and was not entered. Cloudflare challenges on a second navigation in one session are recorded as a capture gap, not as a product error state.
