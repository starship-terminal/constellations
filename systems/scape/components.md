# Components

Public signed-out UI on www.scape.com, measured 19 November 2026. Crops are viewport slices from the 1440x900 captures, except the mobile menu. Values are token names where a token exists.

## Button

Primary is an outline pill. Secondary is a filled black pill. On a photo header, Find a room uses the light secondary fill (`#fef5f0` on `#000`).

| State | Crop | Values |
|---|---|---|
| Primary, default | [button-primary-default.png](components/crops/button-primary-default.png) | `light.button.primary.*`, radius `core.radius.pill`, padding 10px 14px, type `core.typography.button`, uppercase |
| Secondary, default | [button-secondary-default.png](components/crops/button-secondary-default.png) | `light.button.secondary.*`, radius `core.radius.pill` |
| Hover | not cropped | `--button-primary-border-color-hover` is `rgba(0,0,0,.5)`. `--button-secondary-background-hover` is `rgba(0,0,0,.8)`. |
| Active | not cropped | `--button-secondary-background-active` matches hover. |
| Focus-visible | not cropped | Input focus is `1px solid #c1b1a0`. Button focus ring was not isolated. |
| Disabled, loading | gap | Not on the public pages that were opened. |

## Icon button

Heart and profile sit in the header as 24px circles. The chat launcher is a black circle, fixed at the corner.

[icon-button-default.png](components/crops/icon-button-default.png)

## Link

Header links are 16px Visuelt, weight 400, colour `#fef5f0` on the transparent header and `#000` on the solid header.

[link-default.png](components/crops/link-default.png)

## Text field

The contact modal is a HubSpot iframe. The shell was measured: modal background `#fef5f0`, radius 8px, overlay `rgba(0,0,0,.8)`. Declared field tokens: padding `12px 20px`, radius 4px, text `#000`, border `1px solid rgba(0,0,0,.2)`, focus border `#000`.

The form asks for first name, last name, email and phone. Nothing was typed.

[text-field-default.png](components/crops/text-field-default.png)

Text area, select: the location `<select>` on the contact page (Select a location) uses the pill button chrome. A free-standing textarea was not on the pages opened.

## Checkbox

Room filters use a 16px box, radius 2px, border `rgba(0,0,0,.2)`. The checked state is an inline SVG tick. CookieYes switches are a separate widget (24px, radius 50px, fill `#ede8de`) and were not submitted.

## Radio

Not present on the pages opened.

## Switch

CookieYes category switches exist inside the consent dialog. They were not opened after Reject All.

## Tabs

FAQ categories (All, Contracts and pricing, Bookings, Living with us, Check in and check out, Cancellation and fees) are 16px text links. All is underlined. Room stay types are a segmented pill: selected is black fill, the group has a 1px `rgba(0,0,0,.2)` border and a fully rounded track.

[tabs-default.png](components/crops/tabs-default.png)

## Menu

Sort by opens a white panel listing Price (low to high), Price (high to low), Location (asc), Location (desc). The mobile header opens a full-screen cream drawer with the same nav, Favourites, Profile, and a black Find a room pill.

[menu-open.png](components/crops/menu-open.png)

## Tooltip

Not present.

## Dialog

Contact form modal, 912px wide at 1440, padding `56px 12px 0`, radius 8px, page colour fill, overlay `rgba(0,0,0,.8)`. Closed without typing.

[dialog-default.png](components/crops/dialog-default.png)

Cookie consent is a CookieYes centre popup, radius 6px. Dismissed with Reject All. Its buttons are 14px / weight 500 / radius 2px, not the product pill.

## Toast

Not present.

## Card

City cards use `--scape-card-bg` `#fefaf7` and `--scape-card-shadow`. Search hits are flat: image radius 0, title 20px Visuelt, location and price in `rgba(0,0,0,.5)`.

[card-default.png](components/crops/card-default.png)

## List row

FAQ accordion rows: trigger padding `32px 0`, 1px top border `rgba(0,0,0,.2)`, label 16px Visuelt. Open panel is 16px / 24px, colour `rgb(33, 37, 41)`.

[accordion-open.png](components/crops/accordion-open.png)

## Table

A `.Table_table__QTCkj` rule exists (even rows `--light-grey`). No table was on the pages opened.

## Avatar

Not present. Profile is an icon that leads toward an account, and that flow was not entered.

## Badge

STANDARD is `rgba(0,0,0,.08)` fill, 10px / 500, padding 4px, radius 4px. PLUS uses `--scape-bright-yellow` `#feff55`.

[badge-default.png](components/crops/badge-default.png)

## Banner

Announcement bar is `--scape-pink` `#ec6ce7`, computed height 41px, type 16px, colour `rgb(33, 37, 41)`.

[banner-default.png](components/crops/banner-default.png)

## Gaps

- Disabled, error, loading and pressed states were not on the public pages.
- Radio, tooltip, toast, avatar and table were not on the pages opened.
- The contact form's inner field paint sits in a cross-origin HubSpot frame, so those pixels were not measured. The declared `--form-input-*` tokens were.
- Booking, payment, phone entry and email signup were not entered.
