# Components

Public marketing components, measured 2026-11-19. Crops are from the headless 1440 capture at device pixel ratio 2.

## Button

The primary action is "Start for free". The visible control is an inner pill, `border-radius: 100px`, padding `14px 25px 15px`, height 51px. Its fill is a vertical gradient. Computed stops are `color(display-p3 0.772358 0.137098 0.050813)` at the bottom and `color(display-p3 0.97561 0.379986 0.256739)` at the top. Sampled pixels from [button-primary-default.png](components/crops/button-primary-default.png) are about `rgb(255, 80, 47)` at the top and `rgb(220, 0, 0)` at the bottom. The label is Haffer XH SemiBold, 18px, computed weight 400, letter-spacing -0.18px, white. Shadow: `rgba(0, 0, 0, 0.1) 0px 1px 1px 0px, rgba(0, 0, 0, 0.05) 0px 2px 4px 0px`, plus a white inset hairline.

Hover scaled the pill to about 1.05. The gradient string did not change. See [button-primary-hover.png](components/crops/button-primary-hover.png). Pressed, disabled, and loading were not on the page.

The nav "Sign up" uses the same gradient, padding 10px, height 40px, 16px label.

## Link

"See how it works" is Inter 15px, weight 600, `rgb(24, 24, 37)`, no underline. Footer links are Inter 14px, `rgb(142, 141, 160)`. Links transition colour over 0.2s with `cubic-bezier(0.44, 0, 0.56, 1)`.

## Tabs

Pricing billing is two chips. "Yearly – 20%" is selected: background `rgb(240, 238, 234)`, radius 24px, padding `12px 20px`, Inter 16px weight 600. "Monthly" has a transparent background and the same type. Crops: [tab-selected.png](components/crops/tab-selected.png), [tab-default.png](components/crops/tab-default.png).

## Card

Plan cards are 336px wide, padding 24px, radius 20px, background `rgb(240, 238, 234)`, no shadow. Names are Haffer XH SemiBold 32px. Prices are Inter 48px weight 600. Crop: [card-plan-default.png](components/crops/card-plan-default.png).

## Text field

The marketing pages have no text field. The signed-out app shows an email field after "Continue with email". Its painted styles were not readable. The Flutter semantics input computed as the browser default: Arial 13.3px, white, inset border. That is not stored as a product token.

## Not present on these pages

Text area, select, checkbox, radio, switch, menu, tooltip, dialog, toast, avatar, badge, icon button as its own component. The header menu button exists at the phone width. Its open panel was not captured.

## Gaps

See [raw/GAPS.md](raw/GAPS.md).
