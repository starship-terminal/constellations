# Wealthsimple patterns

Public site only. The signed-in app at `my.wealthsimple.com` was not entered.

## App shell

Every marketing page shares a floating header: wordmark, six product groups (Chequing, Trade, Borrow, Accounts, Business, Offers), a Credit card link, search, Log in, and Get started. A promo banner can sit above it. Phone collapses the groups into a Menu drawer. See [screenshots/home-light-banner-closed.png](screenshots/home-light-banner-closed.png) and [screenshots/mobile-home-light-default.png](screenshots/mobile-home-light-default.png).

The map of which control opens which page is [site-tree.md](site-tree.md).

## Navigation menus

Desktop groups open a two-column menu. Trade lists self-directed products on the left and managed portfolios on the right. [screenshots/home-light-menu-trade.png](screenshots/home-light-menu-trade.png). Phone opens a full-screen drawer from the button labelled Open navigation. [screenshots/mobile-home-light-menu.png](screenshots/mobile-home-light-menu.png). Trade inside that drawer is a second list. [screenshots/mobile-home-light-menu-trade.png](screenshots/mobile-home-light-menu-trade.png).

## Search

Open search drops a pill field under the header. Typing filters without a form submit of profile data. [screenshots/home-light-search-typed.png](screenshots/home-light-search-typed.png). The query TFSA painted suggested public results. Nothing was submitted.

## Product page

Product URLs (chequing, trade, credit card, accounts) share a long-scroll marketing template: a large headline, a primary pill, feature bands, and disclosures. Screenshots are named `{page}-light-default.png` and `{page}-light-full.png`.

## Pricing

[screenshots/pricing-light-default.png](screenshots/pricing-light-default.png) compares Core, Premium, and Generation. It is a public page. Choosing a plan that continues into signup is a wall and was not followed.

## Forms

Get in touch and newsletter fields are visible. They were not filled with an email, phone, birthday, or plan, and nothing was submitted. A validation error was therefore not captured.

## Empty, loading, error

A missing path was requested at `/en-ca/this-page-does-not-exist`. See `not-found-light-default.png` when that shot landed. Loading skeletons were not held. No toast followed an action, because no action was submitted.

## Login wall

Log in opens https://my.wealthsimple.com/app/login?locale=en-ca. The known probe showed email and password. There is no Google button. Nothing was typed. The branch stops. See `login-wall-light-default.png` when that shot landed.

## Onboarding

Get started opens https://my.wealthsimple.com/app/signup. Not entered.
