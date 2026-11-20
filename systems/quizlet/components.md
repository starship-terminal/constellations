# Components

Measured on quizlet.com on 19 November 2026, signed out, in the T3 preview browser. The viewport was 1169 by 731 CSS pixels at devicePixelRatio 2. `preview_snapshot` failed with "The browser is not producing screenshot frames", so this package has no crops. States that were read from a stylesheet rule, and not painted, say so.

## Button

Quizlet calls the control `AssemblyButtonBase`.

| State | What was read |
|---|---|
| Primary, medium | Computed on "Log in": background rgb(66, 85, 255), text rgb(255, 255, 255), height 40px, padding 10px 16px, radius 200px, weight 600, 14px / 20px, border 2px transparent |
| Primary, large | Computed on "Sign up for free": height 48px, padding 12px 24px, 16px / 24px |
| Primary, xlarge | Computed on "Stay on track": height 56px, padding 16px 32px |
| Secondary | Computed on "Teachers": background rgb(237, 239, 255), text rgb(66, 85, 255), height 40px, radius 200px |
| Tertiary | Computed on "Log in with Google": background rgb(246, 247, 251), text rgb(88, 99, 128), height 56px, radius 200px |
| Hover | Stylesheet `.a1v8mkuk:hover` sets background `var(--twilight600-twilight600)` (#423ed8). Not hovered live |
| Pressed | Stylesheet `.a1v8mkuk:active` sets background `var(--twilight700-twilight700)` (#1f1c8b). Not pressed live |
| Focus | Stylesheet `.b1cnxow2:focus` sets border-color #a8b1ff. A script focus on "Log in" did not paint that border. The search field did: computed border rgb(168, 177, 255) |
| Disabled | Stylesheet sets color `var(--gray400-gray600)` and background `var(--gray200-gray700)`. No disabled button was on the page |
| Icon | Computed carousel buttons 56px circle, background rgb(246, 247, 251), icon rgb(88, 99, 128). Close button 40px circle |

Transition on `.b1cnxow2`: all 120ms cubic-bezier(0.47, 0, 0.745, 0.715). Under `prefers-reduced-motion: reduce` the same rule sets the duration to 1ms.

## Link

`AssemblyLink`. Create computed color rgb(66, 85, 255), 14px / 20px, weight 600, radius 4px. Footer title links computed color rgb(40, 46, 62). Terms links computed 12px, weight 600, color rgb(88, 99, 128). Hover rule `.aa6yb24:hover` sets color `var(--twilight-600-twilight-500)`. Focus-visible rule sets border-color #a8b1ff.

## Text field

`AssemblyTextInput`. Header search computed height 40px, padding 8px 16px, radius 8px, background rgb(246, 247, 251), border 2px transparent. Placeholder computed rgb(147, 155, 180), weight 600. Login email and password fields computed height 56px, same fill and radius. Focus-within computed border rgb(168, 177, 255). Inline custom properties resolved to height 3.5rem, fill #f6f7fb, text #282e3e, focus #a8b1ff.

## Select

The footer language `select` computed color rgb(88, 99, 128), 14px, weight 600, radius 4px. Signup birthday selects sit in pill wrappers: background rgb(246, 247, 251), radius 200px, height 48px. Open menu, hover and error were not captured.

## Checkbox

The signup terms checkbox is a native input, computed 13 by 13. No custom painted box was measured. Checked, focus and error were not captured.

## Tabs

Signup and Log in are `role=tab`, 24px / weight 700. Selected computed color rgb(46, 56, 86). Idle computed color rgb(88, 99, 128). No underline was painted.

## Dialog

The magic-link dialog is a `ReactModal`. Computed background rgb(255, 255, 255), radius 16px, shadow rgba(40, 46, 62, 0.1) 0px 4px 16px 0px, width 800px. Heading computed 32px / 40px / 700. Overlay rule targets `--scrim300-scrim300` (#0101108f). The overlay's computed background was still transparent. The entrance animation had not painted, and the preview pane was not producing frames.

## Card

Mission article cards computed background rgb(255, 255, 255), radius 24px, shadow rgba(40, 46, 62, 0.1) 0px 2px 4px 0px, 304 by 384. Homepage feature tiles computed radius 24px. Fills: rgb(66, 85, 255), rgb(217, 255, 204), rgb(18, 193, 203), rgb(217, 221, 232). The green and teal fills are not named scale steps.

## Navigation

Header computed sticky, height 64px, background rgb(255, 255, 255), padding 12px 16px, z-index 1098. Promo bar computed height 48px, background rgb(31, 28, 139), link rgb(199, 247, 230).

## Gaps

- No screenshots and no crops. `preview_snapshot` returned "The browser is not producing screenshot frames" twice.
- Viewport was 1169, not 1440, and phone width was not captured.
- Night theme rules were read. `body.theme-night` was not painted. `prefers-color-scheme: dark` was true and the page stayed `theme-default`.
- Hover, pressed and disabled were read from rules, not from a painted control.
- Checkbox, radio, switch, tooltip, toast, table, avatar and badge were not on the signed-out pages.
- Text area was not on the pages that loaded.
- Menu open state, search suggestions and validation errors were not opened.
- `/features/flashcards` returned a PerimeterX press-and-hold challenge. It was not completed.
- Signed-in study, Quizlet Plus, payment, phone and birthday submission were not entered.
