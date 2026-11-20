# Components

Values are token names. The readings behind them are in [raw/computed.json](raw/computed.json). Crops are missing because the preview browser returned no screenshot frames.

## Button

The marketing call to action is `#homepage-weave-cta` on [wandb.ai/site](https://wandb.ai/site). Fill is a gradient from `core.color.gradientStart` to `core.color.gradientEnd`. Text is `dark.color.text.onAccent`. Radius is `core.radius.md`. Desktop padding is 21px by 35px. Type is `core.typography.button`, set in uppercase.

The Forge primary button (Log in, Sign up) uses `light.color.action.primary` and `light.color.text.onAccent`, radius `core.radius.sm`, height `core.spacing.field`. Focus outline is `light.color.focus` at 1px auto.

A ghost button (Forgot your password) has no fill. Text is `light.color.text.ghost`. Same radius and height as the primary button.

Hover on the Weave CTA was not a separate computed change. The header LOG IN hover rule sets color to `core.color.amber`. Nav item hover sets color to `core.color.accent`.

## Link

Docs and Pricing are `dark.color.text.accent` at `core.typography.nav`. CONTACT and SIGN UP are white, 16px, letter-spacing 6%, uppercase. LOG IN is `core.color.amber` at rest. Focus on LOG IN drew a 3px auto white outline.

## Text field

The Forge email field is the only text field that was on screen. Background `light.color.bg.surface`, border `light.color.border.default`, radius `core.radius.sm`, padding 4px 8px, height 32px. Focusing it cleared the outline (`outline: none`) and did not change the border. Error, disabled, and filled states were not produced. Nothing was typed.

## Social button

Continue with Google, GitHub, and Microsoft on the login page, and Google, GitHub, and Microsoft on signup. Background `light.color.bg.social`, border `light.color.border.social`, radius `core.radius.md`, padding 10px 16px, height 46px, weight 500. Not pressed.

## Card

Pricing plan titles are Source Serif 4 at 26px, white. The Personal price text read `$0/mo` at 20px. GET STARTED and CONTACT US are 16px weight 600, uppercase, letter-spacing 0.96px, padding 16px 36px, radius 8px, color rgb(250, 250, 250). Their background computed as transparent, so a card fill was not read. A home card computed radius `12px 12px 0px 0px`.

The home code panel background is `dark.color.bg.code`, bottom radius 8px. The `pre` is `core.typography.code` in `dark.color.text.code`.

## Navigation

The header is 96px tall and starts 60px down the page. The logo is 245 by 48. There is no filled header bar. A `.wb-banner` exists with background rgb(220, 38, 38) and `display: none`.

At 390px the header links had no box, and no hamburger button was in the accessibility set that was queried. The phone menu was not opened.

## Cookie banner

OneTrust is on the Forge login and signup pages. Manage My Cookies Settings uses the same cobalt fill as the primary button, radius 4px, padding 0 32px, height 32px. The preference center was in the DOM. It was not submitted.

## Gaps

| Component | Status |
|---|---|
| Button default, focus | Captured on the Forge primary button and the Weave CTA. No screenshot. |
| Button hover, pressed, disabled, loading | Not captured. Hover rules exist for nav and LOG IN. Pressed, disabled, and loading were not on the page. |
| Icon button | Social circles on pricing are 42px, radius 50%, fill rgb(54, 54, 54). No crop. |
| Link | Captured as computed styles. |
| Text field default, focus | Captured. Focus cleared the outline. |
| Text area, select | Not present on the pages that loaded. |
| Checkbox, radio, switch | Present only inside the OneTrust preference center. Not measured as product controls. |
| Tabs | Not present. |
| Menu | Header dropdowns were not opened. |
| Tooltip | Not present. |
| Dialog | The Forge cookie preference center was in the DOM and was not opened as a measured state. |
| Toast | Not present. |
| Card | Plan titles and the code panel were measured. Card fill was transparent. |
| List row, table | Not present on the marketing and login pages. |
| Avatar, badge | Not present. |
| Screenshots and crops | Not captured. `preview_snapshot` returned "The browser is not producing screenshot frames". |
