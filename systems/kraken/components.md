# Kraken components

Public marketing site only, signed out, 2026-11-21. Values are computed styles or declared `--colors-ds-*` tokens. Crops were not cut: the screenshots in [screenshots/](screenshots/) show the controls in place.

## Button

The header Sign up link is the primary button. Computed on the homepage: background `#7132f5` (`light.accent`), text `#ffffff` (`light.onAccent`), radius 12px (`core.radius.5`), height 36px, padding 8px 12px, Kraken-Product 14px weight 500.

Hover is declared as `--colors-ds-semantic-action-primary-background-hover` `#5b1ecf`. Pressed, disabled, and loading were not captured: no disabled primary was on the public header, and a press would start signup.

Secondary actions (Log in) are text links, not filled buttons.

## Link

Nav items (Kraken, Pro, Wallet, Prime, VIP) are text links that also open menus. Footer links are quiet text. The brand link colour is `light.link` `#7132f5`.

## Text field

The homepage hero has an email field with placeholder `satoshi@email.com`. It was not filled. The sign-in wall has Email or username and Password. The sign-up wall has Email and Invite Code. None were typed into. Focus, error, and disabled field states were not captured.

## Search

The header Search button opens an overlay with placeholder "Find your next trade" and a list of markets. See [screenshots/home-light-search.png](screenshots/home-light-search.png). A query was not typed.

## Menu

Header menus open on hover. Kraken, Pro, Wallet, Prime, Markets, and About are recorded in [site-tree.md](site-tree.md). Screenshots: `home-light-menu-kraken.png`, `home-light-menu-pro.png`, `home-light-menu-markets.png`.

## Dialog

The language control opens "Change language and country/region" with Language and Country comboboxes and Continue. Continue was not clicked. Screenshot: [screenshots/home-light-language.png](screenshots/home-light-language.png).

The cookie banner is a OneTrust dialog. It was hidden, not accepted.

## Tabs

The homepage market block has tabs: Crypto, Spot / Margin, Futures, xStocks. They filter the public price table. Selected state was not measured separately.

## Table

`/prices` is a public price table (asset, price, 24h change, market cap). Screenshot: [screenshots/prices-light-default.png](screenshots/prices-light-default.png).

## Card

Homepage product cards link to Pro, the Kraken app, Wallet, and Krak. They are marketing cards, not app list rows.

## Badge

Price rows show a signed percent change. Positive text is `light.success` `#08844f`. Negative text is `light.danger` `#d11d45`.

## Gaps

| Component | Status |
|---|---|
| Icon button | Search is an icon button. Other icon buttons were not inventoried |
| Text area | Not present on the public pages opened |
| Select | Language and Country comboboxes on the language overlay. Options were not opened |
| Checkbox, radio, switch | Declared in `--spacing-ds-checkbox-*` and `--spacing-ds-radio-*`. Not shown on the pages opened |
| Tooltip | Not captured |
| Toast | Not present on the public pages opened |
| List row | Price rows stand in. No app list |
| Avatar | Not present signed out |
| Button pressed, disabled, loading | Not captured |
| Field error | Not captured. Submitting a form was out of scope |
