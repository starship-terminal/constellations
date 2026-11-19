# Rivian components

Public signed-out surfaces on rivian.com, 2026-11-19. Crops are cut from the 1440 x 900 viewport screenshots. Nothing was reserved, configured, booked, or signed in.

## Button

Demo drive is the brand action in the header. Computed fill `#ffaa00` (`light.accent`), label `#000000`, height 32px, padding 8px 16px, radius 9999px, Adventure 14px / 600. Focus-visible computed a 2px `#ffaa00` outline. The class list names hover and pressed as `bg-brand-accent` (`#ffbd2e`) and `bg-brand-accent/85`. A synthetic mouseover did not change the computed fill, so those two fills are declared, not a held state.

![Demo drive](components/crops/button-demo-default.png)

Reserve on the R2 page is a black pill: fill `#000000`, label `#ffffff`, height 56px, padding 16px 40px, Adventure 16px / 600. Design yours beside it uses the same yellow as Demo drive. Neither was clicked.

![Reserve and Design yours](components/crops/button-reserve-default.png)

Home hero Design yours is a white pill, height 56px, radius 40px, 14px / 500, sitting on the photograph. Book a drive is a transparent pill with a light outline.

![Hero pills](components/crops/button-hero-default.png)

The Vehicles menu uses a black Design yours pill on the vehicle card.

![Menu Design yours](components/crops/button-design-menu.png)

Sign in on the login page is a black pill, height 56px, width 448px, 16px / 600. It was not clicked.

## Icon button

The header chat and account marks sit to the right of Demo drive. The account control was not opened. Chat was not opened. Icon size token `--navbar-icon-size` is 24px. No separate hover or pressed crop.

## Link

Vehicles, Charging, Technology, Discover, and Gear Shop are 14px / 600 pills with a transparent rest fill. Opening Vehicles sets the fill to `rgba(0, 0, 0, 0.1)`. Legal links on General Terms are underlined black text.

![Nav](components/crops/nav-default.png)

Explore in the vehicle card is underlined black text, 16px / 400.

## Text field

Login email and password are 56px tall, radius 12px, fill `oklch(0.961 0 0)` (the same stone as `--input`, `#f2f2f2`), 16px Adventure, padding 23px 12px 8px 16px. Nothing was typed.

Support search is a white MUI field, wrapper border 1px `#cbcbcb`, height 57px, placeholder "How can we help?". No query was submitted.

![Support search](components/crops/field-support-default.png)

Charging route fields (from, to) are 112px tall, radius 12px, 32px type, fill `oklch(0.973 0 0)`. They sit below the loader. No route was searched.

The home email field computed fill `#212121`, radius 4px, height 56px. It was below the fold in the viewport shot. Subscribe computed a grey disabled fill and height 0. Neither was submitted.

## Text area

One textarea exists in the home DOM. Computed height was 0. Not captured as a visible control.

## Select

Not present on the pages opened. R2 Standard, Premium, and Performance are pill buttons, not a native select. Standard was selected on load (fill `#000000`). The others were not clicked.

## Checkbox

Login has one checkbox, "Remember my device for 30 days", 24px, transparent fill. It was not checked.

## Radio

Not present.

## Switch

Not present.

## Tabs

R2 lineup pills (Standard, Premium, Performance) act as a tab. Selected fill is `#000000`, rest is transparent, height 55px. The home carousel dots are 8px pills, selected `#000000`, rest `#cbcbcb`. No product tab component with a panel was opened.

## Menu

Clicking Vehicles opens a panel of three vehicle cards (R1S, R1T, R2) and a link list (Compare models, Demo drive, Trade-in, Current offers, Inventory, Pre-owned, Purchasing, Financing, Insurance, R3, Fleet). Card fill `oklch(0.96 0 0)`, radius 12px, height 413px, shadow none. Design yours and Explore inside the card were not followed.

![R1S card](components/crops/card-vehicle-default.png)

The full panel is [home-light-menu](screenshots/home-light-menu.png).

## Tooltip

Not captured. No tooltip was opened.

## Dialog

A cookie dialog ("We respect your privacy") was on the first load. Reject All was clicked so the page could be read. Accept All and Manage Preferences were not used. The dialog was gone after Reject All, so it has no crop.

## Toast

Not present.

## Card

Vehicle cards in the Vehicles menu, as above. Radius 12px.

## List row

The Vehicles panel link list is 16px / 400, height 36px, transparent fill. Not a separate component file.

## Table

Not present.

## Avatar

Not present. The header account mark is an icon, not a photo.

## Badge

Not present as a labelled chip. The charging loader uses a green bolt on a pill track. That green was not read as a computed style on an element. Recorded as a gap.

## Logo

The header wordmark is an inline SVG, `currentColor`, from the Home link. The site icon is the compass mark in [icon.png](icon.png).

![Wordmark](components/crops/logo-default.png)

## Loading

The charging page paints a full-viewport loader before the map: "Charging is easier than you think" and a green bolt on a grey pill. The screenshot is that state. The loader colour was not read from CSS.

![Charging loader](components/crops/loading-charging.png)

## Gaps

Hover and pressed fills for Demo drive are class names (`bg-brand-accent`, `bg-brand-accent/85`), not a computed state. Reduced-motion emulation was not run. 27 `prefers-reduced-motion` rules were declared, mostly `no-preference`. Dark theme was not found (`color-scheme: normal`). The vehicle builder, reserve, demo-drive booking, trade-in, inventory checkout, and Gear Shop were not entered. Sign in was not submitted. No phone number, card, or account was created.
