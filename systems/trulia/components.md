# Trulia components

Public signed-out surface, measured 2026-11-21 in headed Chrome. Crops are the real controls. Values are token names from [tokens.json](tokens.json).

## Button

Login button `[data-testid=navbar-login-button]`. Height 42px (`core.sizing.control`), radius `core.radius.m` (8px), weight 700, 16px Figtree.

| State | Fill | Text |
|---|---|---|
| default | `light.color.page` | `light.color.text` |
| hover | grey.100 `#e8e9ea` (measured, not a named step that matches exactly; nearest declared step is `color.grey.100`) | `light.color.text` |
| focus-visible | page, plus the declared `--focus-shadow` | `light.color.text` |
| pressed | grey.600 `#6b7780` | white |

![default](components/crops/login-button-default.png) ![hover](components/crops/login-button-hover.png) ![focus](components/crops/login-button-focus-visible.png) ![pressed](components/crops/login-button-pressed.png)

Primary submit inside the login dialog: fill `light.color.accent` (`color.tarzana.700`), text white, radius 8px, height 42px. Not pressed (that would submit).

Search submit `[aria-label=submit search]`: 60×60, fill `light.color.search-submit` (`color.oakmore.500-a-a`), radius 0 8px 8px 0. Hover and pressed both paint `light.color.search-submit-hover`.

![search](components/crops/search-submit-default.png) ![search hover](components/crops/search-submit-hover.png)

## Icon button

Main Menu toggle is an icon button (hamburger). It opens a 320px drawer. No separate crop of the glyph alone.

## Link

Header links (Buy, Rent, Mortgage) are 16px Figtree, colour `light.color.text`. Mortgage hover opens a flyout of text links. Teal links on the newsroom cards use the accent.

## Text field

`#banner-search`, 60px tall, white, radius 8px, placeholder "Search for City, Neighborhood, Zip, County, School". Focus shrinks the field as the clear control appears (453px wide when focused). Not submitted.

![field](components/crops/search-field-default.png) ![focus](components/crops/search-field-focus.png)

Login dialog email field: 42px, 1px solid grey.500, radius 8px, placeholder "Enter email address". Not typed into.

Calculator fields (home price, down payment, rate, ZIP, loan-type select) are on the calculator page. That screenshot was dropped because a cleanup pass wiped the sample numbers. The field chrome was measured only as Observed on the first pass.

## Text area

Not present on the public pages that loaded.

## Select

Loan type on the calculator is a native select ("30-year fixed"). Observed on the first calculator pass. The kept screenshots do not include it.

## Checkbox, radio, switch

Not present on the pages that loaded.

## Tabs

Hero Buy / Rent / Sold. Selected Buy: white fill, text `color.tarzana.700`, radius 8px, 83×40. Idle Rent: transparent, white text. Hover on Rent: fill `color.tarzana.50`, text tarzana.700.

![selected](components/crops/tab-buy-selected.png) ![idle](components/crops/tab-rent-default.png) ![hover](components/crops/tab-rent-hover.png)

## Menu

Main Menu drawer: 320×900, fill `color.grey.900`, sections Buy, Rent, Mortgage, Local Info, Additional Resources. Close control aria-label "Close Menu".

Header Mortgage hover flyout lists eight links. Rent hover lists Post A Rental Listing. Buy hover has no extra links.

![menu page](screenshots/home-light-menu.png) ![flyout](screenshots/home-light-mortgage-flyout.png)

## Tooltip

Not captured. Info icons sit next to calculator labels; their popovers were not opened.

## Dialog

Sign up or Log in. Accessible name "Sign in or register". Panel 375×396, white, radius 8px. Overlay class paints `rgba(0, 0, 0, 0.3)`. Email, Submit, Continue with Google (iframe, not clicked), Continue with Apple (not clicked).

![login](screenshots/home-light-login.png)

## Toast

Not present.

## Card

City photo cards on the homepage rail, neighborhood photo cards, newsroom text cards (white, light border, radius about 8px). Mortgage tool cards are illustration plus an outline button.

## List row

Menu section rows and footer link groups. Footer "More" expands a group in place.

## Table

Not present on the pages that loaded.

## Avatar

Not present. The homepage hero is a photograph, not an avatar component.

## Badge

Not captured as a component. No pill badge was isolated.

## Gaps

| Item | Status |
|---|---|
| Dark theme | Not present. `color-scheme` on the document is `normal`. No dark custom properties. |
| Disabled, loading, error | Not captured. No public control painted them. |
| Text area, checkbox, radio, switch, tooltip, toast, table, avatar, badge | Not present or not reached on the loaded pages. |
| Select | Observed on the calculator, screenshot not kept. |
| Form validation | Not captured. No form was submitted. |
| Login password step | Not captured. Email was not submitted. https://www.trulia.com/login was not opened in this run. |
| Listing result pages | Mapped in [site-tree.md](site-tree.md), not screenshotted. |
