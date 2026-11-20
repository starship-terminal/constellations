# Components

Measured on the public signed-out pages. Token names point at [tokens.json](tokens.json). No crops: the preview browser produced no screenshot frames.

## Button

The marketing primary is `wds-Button--large wds-Button--primary`. Height `core.size.control` (48px), padding 12px 16px, radius `core.radius.pill`, label `core.typography.button-large`. Face is `light.color.accent` with `light.color.on-accent`.

The nav Sign up is the medium size: height `core.size.nav` (32px), padding 8px 12px, same green and forest. On the pricing page the nav Sign up inverts: forest face, green label.

On a green plate the same primary class paints `light.color.forest` with `light.color.on-forest`. The calculator Send money button uses the green face at weight 400, not 600.

Secondary-neutral is a 48px pill, fill `light.color.neutral-fill`, label `light.color.text`.

Hover, pressed, disabled, and loading were not forced. Declared hover tokens exist (`--color-interactive-accent-hover` #80E142, `--color-interactive-primary-hover` #0D1F00) and were not confirmed on a hovered element, so they are not component tokens.

## Link

The login "Sign up" link is 14px, weight 600, underline, colour `light.color.link`. Nav links are the tertiary button: transparent, 18px, weight 600, forest text.

## Text field

The login email and password fields are 48px, padding `12px 16px`, radius `core.radius.input`, type Inter 16px / 24px, letter-spacing -0.176px. The ring is an inset shadow, `light.shadow.input`, not a CSS border. Focusing the empty email field did not change that ring. Both fields were left empty.

The home calculator amount fields are a different control (Wise Sans, transparent, no radius). They were not filled.

## Select

Currency pickers are `role="combobox"` buttons, 40px (and a second pair at 72px), radius pill, fill `light.color.calculator-fill`. The menu was not opened.

## Alert

The login page already showed "Something went wrong." The banner is radius 16px, padding 16px, fill `light.color.neutral-fill`, text `light.color.muted`. The icon circle is `light.color.negative-strong` with a glyph in `light.color.negative-on`. Nothing was submitted to produce it.

## Card

Pricing segment cards are 374px wide, radius 10px, border 1px solid rgba(22, 51, 0, 0.12), content padding 16px. Title is `core.typography.display-card`.

## Gaps

| Component | Status |
|---|---|
| Icon button | Close on login is 48px, pill, transparent. Not cropped |
| Text area, checkbox, radio, switch | Not present on these pages |
| Tabs | Not isolated. Personal, Business, and Platform are nav links |
| Menu, tooltip, dialog, toast | Not opened |
| Table | Not present on the pricing page that loaded |
| Avatar, badge | Not present |
| Hover, pressed, disabled, loading | Not captured |
| Focus ring change | Not observed. The email inset ring stayed #868685 |
| Crops | Not captured. Preview frames never arrived |
