# Rise components

Public marketing controls, measured 2026-11-19. Crops are 2x element screenshots from the live pages. Values are token names.

## Button

Primary, on [pricing](screenshots/pricing-light-default.png). Background `{color.primary}`, text `{color.system-white}`, radius 4px, padding 8px 16px, 14px medium, height 34px. Hover is primary at 80%.

![Primary](components/crops/button-primary-default.png)

![Primary hover](components/crops/button-primary-hover.png)

Secondary. White face, 1px `{color.border}`, foreground text. Hover fills `{color.input}` and drops the text to foreground at 90%.

![Secondary](components/crops/button-secondary-default.png)

![Secondary hover](components/crops/button-secondary-hover.png)

The comparison page uses the same primary face at 18px, padding 8px 24px, height 46px.

Focus-visible is declared as a 2px ring with a 2px offset. The class names `ring-ring`, and the stylesheet does not define `--ring`. A programmatic focus did not paint a ring. See Gaps.

![Secondary focus](components/crops/button-secondary-focus.png)

Pressed, disabled and loading were not on the public pages.

## Link

Inline article links are primary, semibold, no underline at rest. Hover adds an underline and primary at 80%.

![Link](components/crops/link-default.png)

![Link hover](components/crops/link-hover.png)

Blog titles are foreground, bold, and shift 4px right on hover (`.hover:translate-x-1`). The featured title also drops to foreground at 60%.

## Badge

Eyebrow. 10px semibold, uppercase, letter-spacing 0.5px, padding 2px 8px, 1px border, radius 4px, offset-dark text.

![Eyebrow](components/crops/badge-eyebrow.png)

Soft accent chip. Primary text on primary at 10%, 12px medium, radius 2px.

![Soft chip](components/crops/badge-default.png)

Discount chip. Foreground text on `{color.surface}`, radius 2px, padding 2px 4px.

![Discount](components/crops/badge-discount.png)

## Switch

Annual billing, off. Track 32 by 16px, radius full, offset-dark at 60%, padding 2px. Thumb 12px, white.

![Switch off](components/crops/switch-off.png)

On. Track becomes `{color.primary}`. Thumb translates 16px.

![Switch on](components/crops/switch-on.png)

## Card

Quiet plan card. `{color.background}`, border at 50%, radius 6px, padding 36px, width 480px at 1440.

![Quiet card](components/crops/card-quiet.png)

Raised plan card. White, full border, shadow `0 1px 2px rgba(0,0,0,0.05)`.

![Raised card](components/crops/card-raised.png)

## List row

Pricing features are a `ul` of rows: 14px, padding-block 12px, label in offset-dark, value in medium foreground, a 1px border under the first row.

## Logo

Wordmark, 76 by 24. The mark is two linear gradients. Bottom stops `#767df9`, `#7161ec`, `#5730e3`. Top stops `#ff7557`, `#ffaf66`. The word is black.

![Wordmark](components/crops/logo-wordmark.png)

## Gaps

Not on the public pages, so not captured: text field, text area, select, checkbox, radio, icon button, tabs, menu, tooltip, dialog, toast, table, avatar. The signed-in app that held them shut down on 31 March 2025. Login and signup URLs now 404. No email form was shown, so no account was created.

Not present as a second theme: dark. `:root` is the only colour block. `prefers-color-scheme` is not in the stylesheet.

Not captured: focus ring colour. The utility names `--ring` and the file does not set it. Pressed, disabled and loading button states were not reachable. Reduced motion is not authored. `--sidebar` is declared and unused on these pages.
