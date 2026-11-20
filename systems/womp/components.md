# Components

Values are token names. Crops are from the 1440px captures.

## Button

Solid, outline, ghost and soft, all pill-shaped.

| State | Crop | Values |
|---|---|---|
| Solid, size 3 | [button-solid.png](components/crops/button-solid.png) | `light.accent.solid` on `light.text.on-accent`, height `core.control.height-3`, radius `core.radius.control-3`, type `core.typography.button`, shadow `core.shadow.control-chrome` |
| Outline | [button-outline.png](components/crops/button-outline.png) | Transparent face, inset ring `core.shadow.outline`, same height and radius |
| Ghost | [button-ghost.png](components/crops/button-ghost.png) | Transparent face, `light.text.primary`, no shadow |
| Focus | Measured, not cropped | 2px solid `light.accent.focus`, offset `core.focus.outline-offset` |

Size 2 (Order, auth Continue) is 32px tall and 16px radius. Size 4 (hero Get started) is 48px tall, 24px radius, 18px type. Hover, pressed and disabled were not measured.

## Nav link

[nav-link.png](components/crops/nav-link.png). `core.typography.nav`, transparent, no radius. Focus outline is `light.accent.nav-focus` at 2px with a 4px offset.

## Text field

Home prompt sits in a soft card, 16px radius, 16px padding, 18px Inter, no border on the textarea. Contact fields are outline, 40px tall, 20px radius, inset `rgb(217, 217, 217)` ring. Focus adds a 2px `rgb(187, 187, 187)` outline on the wrapper. Auth email field is a 32px soft pill (`color(display-p3 0.939 0.939 0.939)`), full width of a 384px column. Placeholder on the home prompt is 50% ink.

## Text area

Contact message box is 144px tall, 20px radius, 12px padding, placeholder "Type your message…". Not submitted.

## Select

Contact topic trigger matches the outline field: 40px, 20px radius, inset ring, label "Select one…". The list was not opened.

## Radio

Company size is a row of `choice-card` labels, 40px tall, 16px radius, padding 8px 12px, inset `rgba(0,0,0,0.15)` ring. The checked card thickens the ring to 2px `rgb(141, 141, 141)`.

## Segmented control

Monthly / Annual on pricing. Track is `light.background.soft`, 40px, 20px radius. Annual starts selected. The indicator element computed a transparent background, so the selected fill is not recorded as a token.

## Chip

Soft chip, 24px, 14px radius, padding 4px 8px, 12px / 500. "Save 25%" and "Most popular" use green and blue tints that were not tokenised. See Gaps.

## Card

Template cards and plan cards are 16px radius, 16px padding. The Pro card is raised: `rgba(0,0,0,0.1) 0 1px 2px, rgba(0,0,0,0.11) 0 24px 64px -12px`. The screenshot also shows a blue outline on that card. That outline was not in the computed `box-shadow` or `border` of `.kui-variant-raised`, so it is a gap.

## Table

Comparison table, 47 rows. Header and section cells use `color(display-p3 0 0 0 / 0.024)` and an inset top hairline of `color(display-p3 0 0 0 / 0.122)`. Cell padding is 12px 16px.

## Menu

The 3D Printing menu drops a three-column grid under the header. Section labels are 16px Inter. Titles are Inter Tight 18px / 26px, tracking -0.09px. [screenshots/home-light-menu.png](screenshots/home-light-menu.png)

## Avatar

Quote block uses a 48px circular avatar. Not cropped.

## Gaps

- Hover, pressed, disabled, loading and error styles were not forced.
- Checkbox and switch were not on these pages.
- Tooltip, toast and dialog were not on these pages.
- The editor shell is behind auth. Google, SSO, the email form and the contact form were not submitted.
- "Save 25%" and "Most popular" chip colours, and the blue Pro-card outline, were seen and not tokenised.
- The selected segment fill computed as transparent.
- Reduced motion was not emulated. Video and the template marquee are not CSS transitions.
- Dark mode is the footer only. No separate dark marketing page was found.
