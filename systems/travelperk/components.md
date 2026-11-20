# Components

Public marketing chrome on perk.com, plus the signed-out login page at app.perk.com/login. Values are computed styles from 19 November 2026. Crops were not saved: the preview browser returned "The browser is not producing screenshot frames", so this file has no images.

## Button

Primary "Book a demo" is 40px tall and 131px wide at the homepage read. Background `rgb(190, 255, 80)`, label `rgb(20, 20, 15)`, OTSono 400 at 16/24, padding `16px 12px 16px 16px`, radius 26px, 1px transparent border, no shadow. The class is `transition-all duration-200 ease-in-out`.

Secondary "Explore our product" uses the same height and radius with a transparent face and a 1px `rgb(20, 20, 15)` border.

At innerWidth 390 on `/platform/`, "Book a demo" is 48px tall and 324px wide. Radius stays 26px.

Login "Sign in" is a different control: 44px, radius 8px, background `rgb(20, 20, 15)`, white Perk Sans 500 at 16px, width 384px. "Sign in with SSO" is the outline version, 1px off-black border, transparent face. Neither was clicked.

Hover, pressed, disabled and loading were not captured. The stylesheet declares `.hover:bg-brand-perk:hover` and a primary hover of `#2c2c27` on the app token `--color-button-background-primary-hover`. Those states were not painted.

## Link

Nav "Customers" is OTSono 400, 16/24, `rgb(20, 20, 15)`, no underline. Footer links were not isolated from the page text.

## Text field

The marketing pages that were opened have a currency text input and a language input. Their painted boxes were not the visible control. The login page has one email input, name `email_address`, placeholder "someone@company.com", 16px Perk Sans. The container is 384 by 44, radius 8px, padding `0px 8px 0px 10px`, 2px solid `rgb(20, 20, 15)`. It was left empty.

The app token `--color-input-border-base` is `#838377`. The painted border was off-black, so the token and the painted field disagree. The token is recorded as a gap in the login field role.

## Text area, select, checkbox, radio, switch

A "Show differences only" checkbox exists on pricing. Its input box computed to 0 by 0. The label is a 9999px pill with an 8px 16px pad and a 1px `rgb(145, 145, 131)` border, also at height 0 in the read. Text area, select, radio and switch were not present as painted controls.

## Tabs

Pricing region and product switches are `role="tab"`. "North America" and "Travel and Spend" were `aria-selected="true"`. Each tab is 16px, transparent, radius 0, height 20. No indicator was painted on `::before` or `::after`. The tab list is 86px tall with padding `20px 0 14px`.

## Menu

The product menu links were in the DOM at height 0. The open menu panel was not captured.

## Tooltip

Not present on the pages that were read.

## Dialog

No cookie dialog was painted. A US/Canada banner sat in the page ("Located in US or Canada?") as a rounded card, not a modal. It was not dismissed.

## Toast

Not present.

## Card

Homepage proof and feature cards are `rgb(245, 245, 235)`, radius 28px, no border and no shadow. The pricing plan card is the same fill, padding 32px, 527 by 711 at the 1169 read. A media card on pricing used `rgb(250, 250, 245)`.

## List row, table, avatar, badge

FAQ rows are 73px tall with a 1px `rgb(145, 145, 131)` border and 24px vertical padding. Plan feature lists were not measured as a separate component. Table, avatar and badge were not painted.

## Gaps

Hover, focus-visible, pressed, disabled and loading were not captured. The login error "An unexpected error occurred. Please try again." was already on the page in `rgb(210, 15, 70)` at 16px, before any field was filled. Dark theme tokens exist as `[data-theme="dark"]` focus colour only. No dark marketing theme was painted.
