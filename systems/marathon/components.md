# Components

Measured on https://onmarathon.com, 2026-11-18, signed out, desktop 1440 unless a row says phone. Colour names a token from [tokens.json](tokens.json). The crop is the evidence. Pressed crops are a forced `:active` and did not fire the control.

## Banner

The archive strip sits above the header. Fill is `light.accent` (`#d7fd51`). Type is `light.textOnAccent` (`#21240c`), caption size 13.2px / 500 / 17.6. Height is `core.size.banner` (44px). Radius is 0. Hover does not change the fill. [crop](components/crops/banner-link-default.png).

## Navigation

Nav links are `core.typography.label` (15.4px / 500) in `light.textMuted` (`#717171`). Hover sets `light.text` (`#0b0b0b`) over 150ms. The wordmark is an image plus the word Marathon at 17.6px / 400. [default](components/crops/nav-link-default.png), [hover](components/crops/nav-link-hover.png).

Sign In is the same muted link. It points at `/sign-in`, which redirects to `/`. The form was not submitted.

## Button

The filled action is ink, not lime.

| Variant | Fill | Type | Height | Radius |
|---|---|---|---|---|
| Header Get Started | `light.ink` `#0b0b0b` | `light.onInk` `#ffffff` | `core.size.controlSm` 39.6px | `core.radius.full` |
| Large Get Started | `light.ink` | `light.onInk` | `core.size.controlMd` 48.4px | `core.radius.full` |
| Secondary | `light.secondary` `#f2f2f2` | `light.secondaryText` `#161616` | 48.4px | `core.radius.full` |

Header padding-inline is `core.space.3` (13.2px). The large button uses `core.space.8` (31.68px). Hover on the ink button is `light.inkHover` (`#404040`), measured. The declared `light.accentHover` (`#c8ee3a`) is the lime hover and the filled button does not use it. Secondary hover is `light.secondaryHover` (`#e4e4e4`).

[default](components/crops/primary-button-default.png), [hover](components/crops/primary-button-hover.png), [secondary](components/crops/secondary-button-default.png).

Get Started is a link to `/register`. It was not used as checkout. No purchase was made.

## Segment

Pay Annually / Pay Monthly is a pill group. The selected face is `light.ink` with `light.onInk`, height 39.6px, radius 9999px. The unselected label is `light.textMuted`. The toggle changes the price copy. It is not checkout. [selected](components/crops/segment-selected-default.png), [monthly shot](screenshots/pricing-light-monthly.png).

## Badge

Popular is an ink pill on the Pro card. Fill `light.ink`, type `light.onInk`, caption 13.2px / 500, height `core.size.badge` (22px), radius 9999px. [crop](components/crops/badge-default.png).

## Type

| Role | Token | Size | Weight |
|---|---|---|---|
| Display | `core.typography.display` | 81.4px / 81.4px | 500 |
| Heading | `core.typography.heading` | 46.2px / 46.2px | 500 |
| Price | `core.typography.price` | 66px / 99px | 500 |
| Body | `core.typography.body` | 15px / 22.5px | 400 |
| Label | `core.typography.label` | 15.4px / 22px | 500 |
| Caption | `core.typography.caption` | 13.2px / 17.6px | 500 |

Body colour on the letter is `light.textMuted`. Eyebrows such as "For Agencies" use `light.textOnAccent` (`#707a00` as `--primary-text`). [heading](components/crops/section-heading-default.png), [price](components/crops/price-default.png).

## Focus

Focus-visible is a 1px auto outline, colour `light.focus` (`#005fcc`), offset 1px on links and buttons. That is the browser default, not a Marathon custom property. [crop](components/crops/nav-link-focus-visible.png).

## Phone menu

The menu button is a 39.6px circle, radius 9999px. The open sheet is a solid panel, not a scrim. Links are Product, For Agencies, Pricing, Sign In, and a full-width Get Started. [shot](screenshots/mobile-home-light-menu.png). The menu-open crop is a partial text stack. Use the screenshot.

## Not on the public surface

Text field, text area, select, checkbox, radio, switch, tabs, tooltip, dialog, toast and table were not painted signed out. Sign-in and register were not submitted, so no field error, loading button or disabled control was reached. The demo page embeds a SavvyCal iframe (12px radius, 1px ring). The form was not submitted.
