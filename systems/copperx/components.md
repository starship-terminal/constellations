# Components

Measured on copperx.io, signed out, on 2026-11-18. Crops are 256-colour PNGs. Read colours from [tokens.json](tokens.json).

## Primary button

The black Get Started control in the header and the hero.

| State | Size | Fill | Text | Crop |
|---|---|---|---|---|
| default | 102.5 x 36 | rgb(0, 0, 0) | rgb(255, 255, 255) | [crop](components/crops/primary-button-default.png) |
| hover | 102.5 x 36 | rgb(30, 35, 46) | rgb(255, 255, 255) | [crop](components/crops/primary-button-hover.png) |
| focus-visible | 102.5 x 36 | rgb(43, 50, 64) | rgb(255, 255, 255) | [crop](components/crops/primary-button-focus-visible.png) |
| pressed | 102.5 x 36 | rgb(45, 52, 66) | rgb(255, 255, 255) | [crop](components/crops/primary-button-pressed.png) |

## Secondary button

The white Log in control. Opens the account-choice dialog. The dialog links were not followed.

| State | Size | Fill | Text | Crop |
|---|---|---|---|---|
| default | 63.8 x 36 | rgb(255, 255, 255) | rgb(19, 23, 31) | [crop](components/crops/login-button-default.png) |
| hover | 63.8 x 36 | rgb(247, 249, 252) | rgb(19, 23, 31) | [crop](components/crops/login-button-hover.png) |
| focus-visible | 63.8 x 36 | rgb(234, 238, 246) | rgb(19, 23, 31) | [crop](components/crops/login-button-focus-visible.png) |
| pressed | 63.8 x 36 | rgb(233, 237, 245) | rgb(19, 23, 31) | [crop](components/crops/login-button-pressed.png) |

## Sales button

Contact Sales, the same white control, linking out to a Google Form. The form was not filled.

| State | Size | Fill | Text | Crop |
|---|---|---|---|---|
| default | 118.3 x 36 | rgb(255, 255, 255) | rgb(19, 23, 31) | [crop](components/crops/sales-button-default.png) |
| hover | 118.3 x 36 | rgb(247, 249, 252) | rgb(19, 23, 31) | [crop](components/crops/sales-button-hover.png) |

## Link

Indigo menu links, Tailwind text-indigo-400.

| State | Size | Fill | Text | Crop |
|---|---|---|---|---|
| default | 312 x 20 | rgba(0, 0, 0, 0) | rgb(95, 118, 249) | [crop](components/crops/nav-link-default.png) |
| hover |  |  |  | not measured: locator.hover: Timeout 4000ms exceeded. |

## Display title

The home headline.

| State | Size | Fill | Text | Crop |
|---|---|---|---|---|
| default | 960 x 192 | rgba(0, 0, 0, 0) | rgb(30, 35, 46) | [crop](components/crops/hero-title-default.png) |

## Account choice

A row in the Log in dialog. The row's host is recorded. The host was not opened.

| State | Size | Fill | Text | Crop |
|---|---|---|---|---|
| default | 466 x 149 | rgba(0, 0, 0, 0) | rgb(0, 0, 0) | [crop](components/crops/account-choice-default.png) |

## Header

The sticky marketing header.

| State | Size | Fill | Text | Crop |
|---|---|---|---|---|
| default | 1440 x 85 | rgb(255, 255, 255) | rgb(0, 0, 0) |  |

## Pricing title

The pricing page headline.

| State | Size | Fill | Text | Crop |
|---|---|---|---|---|
| default | 327.2 x 186 | rgba(0, 0, 0, 0) | rgb(0, 0, 0) | [crop](components/crops/pricing-title-default.png) |

## Card page title

The corporate-card page headline.

| State | Size | Fill | Text | Crop |
|---|---|---|---|---|
| default | 820 x 252 | rgba(0, 0, 0, 0) | rgb(30, 35, 46) | [crop](components/crops/cards-title-default.png) |

## Gaps

Text area, select, checkbox, radio, switch, tabs, tooltip, toast, avatar and badge were not on the signed-out marketing pages.
The contact form is a Google Form iframe. It was not filled, so validation, disabled and error states were not measured.
dashboard.copperx.io and payout.copperx.io are the account hosts named by the Log in dialog. They were not opened.
The focus-visible and pressed rows of the Secondary and Primary buttons are not clean readings: the capture never reset between states, so focus-visible was read with the pointer still on the button (its fill is neither the rest nor the hover fill) and pressed with the focus ring still drawn (`outline: auto 1px`). They need a recapture; the default and hover rows are sound.
