# Components

Measured in the attached T3 preview browser on 2026-11-18, signed in as `kaichen@agentmail.to`. Desktop CSS viewport 1169x731. Values are computed styles, recorded in [raw/measured.json](raw/measured.json).

| Component | State | Evidence |
|---|---|---|
| Button, primary | default | `a.btn.btn--primary.btn--m`. Fill `#2563eb`, label `#ffffff`, 16px weight 600, height 46, radius 10px, padding 0 21px. Text "Start the Generator" on the homepage. The same fill paints "I accept" and "Let's go!". |
| Button, gray | default | `a.btn.btn--gray.btn--m`. Fill `rgba(0, 0, 0, 0.06)`, label `#000000`, same size as primary. Text "Explore 10M+ Palettes". |
| Button, header | default | `a.btn.btn--s.btn--transparent`. Height 36, radius 8px, 15px weight 500, label `#000000`. Text "Tools". |
| Button, Go Pro | default | `a.btn.btn--accent-transparent.btn--s`. Same size as header. Label `#ec4899`. |
| Icon button | default | Generator toolbar icons are 36px square `a.btn.btn--s.btn--icon.btn--transparent`, 14px weight 500. |
| Avatar | signed in | Header swaps Sign in and Sign up for a 36px circle with the initial K after email confirmation. |
| Text field | confirm | `#passcode_code`, placeholder "Enter the code", height 46, width 332 in the confirm modal. Signup fields are `#modal-signup_name`, `#modal-signup_email`, `#modal-signup_password`. |
| Search field | explore | Placeholder "Search with colors, topics, styles or hex values...", 16px, height 39, at 390px. |
| Dialog | terms, hello | `.modal_element` is white, radius 14px, ring `rgba(0, 0, 0, 0.07) 0 0 0 1px`. Primary action is the 46px blue button. |
| Generator column | default | `.generator_color` is 234 by 615 at 1169px. Hex is `.generator_color_hex`, 30px weight 600, letter-spacing 0.9px. Name is `.generator_color_color-info`, 11.2px weight 600, letter-spacing 0.448px. Ink is white or black against the column. |
| Palette card | explore, 390px | `.palette-card` about 330 by 150, side inset 30. Swatch row is 104px tall. Title sits under the swatches with a like count. |
| Tooltip | hover | "View color info" appears on a generator column control. Black pill, white label. Not measured beyond the screenshot. |

## Gaps

- Pro checkout, saved palettes and account settings were not entered.
- No dark theme was on screen.
- Crops were not cut. The page screenshots are the evidence.
- Focus, disabled, error and loading states were not measured.
