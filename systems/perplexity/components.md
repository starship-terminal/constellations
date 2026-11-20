# Components

Crops are from the 2026-11-19 public capture. Values are token names where a token exists.

## Button

The marketing header uses a filled pill and an outline pill. Get started on pricing is the filled pill. Select is the outline pill.

![Get started](components/crops/button-solid-marketing.png)

![Select](components/crops/button-outline-default.png)

The sign-in dialog uses the same filled pill for Continue with Google.

![Continue with Google](components/crops/button-solid-default.png)

| State | Value |
|---|---|
| Filled height | `light.component.button.pill.heightSm` (36px) on the header, `heightMd` (40px) on pricing |
| Radius | `core.radius.full` |
| Filled fill | `light.component.button.solidNeutral.backgroundColor` |
| Outline border | `light.component.button.outline.borderColor` |
| Hover | Not isolated. A hover read of See a demo on the hub hero did not change its computed background. |
| Focus, pressed, disabled, loading | Not captured. |

## Icon button

The dialog close control and the product sidebar icons are visible in [dialog-default.png](components/crops/dialog-default.png) and [sidebar-default.png](components/crops/sidebar-default.png). Their computed size was not read as its own measurement.

## Link

Terms of Service and Privacy Notice sit in the product footer and in the dialog.

![Footer links](components/crops/link-default.png)

Link colour tokens are `light.color.link.accent.fg.idle` (`#016a71`) and the alert pair. The footer links in the light product shot read as muted, not the accent. That pairing was not isolated.

## Text field

The product composer is a 20px-radius white shell. The dialog email field is a separate outlined input. Placeholder copy is "Ask anything..." and "Enter your email". Nothing was typed.

![Composer](components/crops/text-field-default.png)

![Email](components/crops/text-field-email.png)

| Part | Value |
|---|---|
| Composer radius | `light.component.composer.radius` (20px) |
| Composer fill | `light.component.composer.backgroundColor` |
| Email radius, height, focus ring | Not captured as their own computed values. |

## Text area

Not present as a separate control. The composer is a contenteditable, not a textarea.

## Select

Not present on the captured pages. Model is a button, not a native select. Its menu was not opened.

## Checkbox, radio, switch

Not present on the captured pages.

## Tabs

Individual and Enterprise on pricing are a two-label switch. Computed styles were read for Individual (34px, 14px, weight 600, pill radius, transparent fill). The Enterprise selected state was not opened.

## Menu

Products, Business, and Resources are header buttons. Their menus were not opened. Model was not opened.

## Tooltip

Not captured. No hover produced a tooltip in the reads that were taken.

## Dialog

Sign In opens a dialog. It offers Google, Apple, an email field, Continue with email, and Single sign-on. None of those was submitted.

![Sign-in dialog](components/crops/dialog-default.png)

Dialog radius and scrim were not read as their own computed values. The page backdrop token is `light.color.bg.backdrop`.

## Toast

Not captured. No action was submitted, so no toast appeared.

## Card

Pricing plans are three cards. The featured card has a teal border and a Popular badge.

![Featured plan](components/crops/card-featured-default.png)

| Part | Value |
|---|---|
| Featured fill | `light.component.planCard.backgroundColor` (`#fdfbfa`) |
| Featured radius | `light.component.planCard.radius` (10px) |
| Featured border | `light.component.planCard.borderColor` |
| Popular badge | `light.component.badge.popular.backgroundColor` / `textColor` |

## List row

The product sidebar lists New, Computer, Automations, Artifacts, and Plugins. Empty copy is "No projects" and "No recent sessions".

![Sidebar](components/crops/sidebar-default.png)

Painted width is `light.component.sidebar.width` (240px). `--sidebar-width` computed to 220px.

## Table

The pricing comparison (Computer, Platform, and the rows under them) is in [pricing-light-plans.png](screenshots/pricing-light-plans.png). Row height and cell padding were not measured.

## Avatar

The signed-out sidebar uses a generic person glyph beside Sign In. No account avatar was available.

## Badge

Popular is the only badge whose computed style was read: 24px tall, 6px radius, `#c6e2e3` on `#016a71`.

## Gaps

- Hover, focus-visible, pressed, disabled, loading, and error were not forced on controls.
- Checkbox, radio, switch, select, toast, tooltip, and menu panels were not on the page.
- The email field's own radius, height, and focus ring were not measured.
- The dialog's own radius and scrim colour were not measured.
- Dark marketing chrome was not captured. The hub stayed light under a dark preference.
- Signed-in product states, Pro checkout, SSO, and phone entry were not entered.
