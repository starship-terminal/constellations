# Components

Public marketing components on ripple.com, measured 2026-11-19. Crops are 2x screenshots of the live controls. Values are computed styles, named as tokens.

## Button

Primary action. Class `button button-dark button1`. Height 40px, radius 40px, label 16px / 24px weight 500 in rippleFont, colour `#f1f2f3`. The fill is not a flat `background-color` (that computed to transparent). Twelve circle layers animate over `--color-blue-60` stops, with an inset shadow `rgba(0, 91, 204, 0.9) 0px 3px 12px` and `rgba(0, 91, 204, 0.8) 0px -3px 4px`. Hover, declared on `.button-dark:hover`, shifts those stops to `--color-blue-70` and `--color-blue-80`. Pressed, disabled and loading were not shown.

![Primary default](components/crops/button-primary-default.png)

![Primary hover](components/crops/button-primary-hover.png)

Secondary. The Contact Sales link is a 40px pill, radius 9999px, 2px transparent border, padding 6px 18px, rippleBdsFont 16px / 24px weight 400, colour `#000000`.

![Secondary default](components/crops/button-secondary-default.png)

![Secondary focus](components/crops/button-secondary-focus.png)

## Icon button

Open search and Change language. 40px circle, background `#f2f2f3` (`--bds-neutral-50`), transition `0.15s cubic-bezier(0.4, 0, 0.2, 1)` on colour and background. Hover is declared as `hover:bg-bds-neutral-100`.

![Search default](components/crops/icon-button-search-default.png)

![Search hover](components/crops/icon-button-search-hover.png)

## Link

Tertiary text actions (`button-tertiary`) are 16px weight 500, colour `#141a1f`, with a blue arrow (`--color-blue-55` on light bands). Inline legal links compute to `#008cff` (`--color-blue-50`), no underline, weight 500. Article links compute to `#005bcc` (`--color-blue-60`).

![Tertiary default](components/crops/link-tertiary-default.png)

![Tertiary hover](components/crops/link-tertiary-hover.png)

![Inline link](components/crops/link-inline-default.png)

## Text field

The only field on the public site is the search input. Placeholder "Search ripple.com". Height 40px, radius 4px, padding 8px 16px 8px 40px, background `#e4e5e7`, text `#586074`, weight 350. Focused box-shadow is `0 0 0 1px #ffffff, 0 0 0 3px #006aff`. The sales form at `/contact/sales/` is an iframe from go.ripple.com and was not filled.

![Search focus](components/crops/text-field-search-focus.png)

![Search filled](components/crops/text-field-search-filled.png)

## Menu

Desktop Products panel (`#nav-panel-0`) is a full-width white sheet under the 80px header, shadow `rgba(0, 0, 0, 0.05) 0px 10px 20px`. Row title is rippleBdsFont 16px weight 500 `#000000`. Description is 14px weight 400 `#707a8f`. Featured card is `#000b33` with radius 12px.

![Menu item](components/crops/menu-item-default.png)

![Menu item hover](components/crops/menu-item-hover.png)

Nav items in the header are 36px tall, radius 6px. The current section (Company on `/company/`) is `#006aff`.

![Nav item](components/crops/nav-item-default.png)

## Accordion

FAQ questions are buttons with background `#e5e7e8`, radius 8px, padding 32px at the xl breakpoint. The question is 22px / 32px weight 350. The open answer is 16px / 24px weight 350, colour `#141a1f`.

![Accordion closed](components/crops/accordion-default.png)

![Accordion open](components/crops/accordion-open.png)

## Card

Insight cards crop the title link. The image above it is 352x200 with radius 8px. Title is 19px / 28px weight 500.

![Insight card](components/crops/card-insight-default.png)

## Type

Home h1 at 1440 is 68px / 80px, weight 500, letter-spacing -1px, colour `#141a1f`. At 390 it is 42px / 56px.

![Display](components/crops/type-display.png)

## Gaps

Text area, select, checkbox, radio, switch, tabs, tooltip, toast, table, avatar and badge were not on the public pages measured. The FAQ is the accordion, not a tab set. Search is the only text field. No validation error, empty state, loading state or destructive confirm was reachable without submitting the sales form or creating an account. Dark theme is not present. Wallet connect, sign-in and KYC were not entered.
