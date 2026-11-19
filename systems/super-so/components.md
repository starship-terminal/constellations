# Components

Measured on 2026-11-19 from a T3 preview tab at 1169 by 731, devicePixelRatio 2. No crops: `preview_snapshot` returned "The browser is not producing screenshot frames".

## Button

Nav CTA "Get started free" on https://super.so/: background `#ffbe3c`, text `#111111`, 16px Beausite weight 500, padding `10px 16px`, radius `8px`, height 42px, no shadow.

Hero CTA "Get started for free": same colours, padding `13px 16px 14px`, radius `8px`, height 53px, line-height 25.6px, shadow `rgba(18, 18, 32, 0.05) 0px 12px 40px -3px`.

Pricing "Start for free" on the Free card: white background, text `#4d545c`, border `1px solid #f2f4f5`, radius `8px`, padding `13px 16px 14px`, height 53px, weight 500.

Pricing "Start for free" on Personal and Pro: background `#fff8eb`, text `#262a2e`, border `1px solid #ffbe3d`, radius `6px`, same padding and height.

"Get started today for free": background `#111111`, text `#ffffff`, radius `8px`, height 53px, weight 500.

Login "Log in": background `#ffb224`, text `#1b1b18`, border `1px solid #ffb224`, radius `8px`, height 44px, padding `0 16px`, 14px weight 400, width 320px.

Login "Sign in with Google" and "Sign in with Apple": background `#151514`, text `#eeeeed`, border `1px solid #2d2d2a`, radius `8px`, height 44px. Passkey uses background `#1a1a19` and the same border.

Hover, pressed, loading and disabled were not shown.

## Link

Nav item: 16px weight 400, colour `#262a2e`, padding `16px 12px`, radius `8px`, gap 4px, height 80px inside the bar.

Sign in: background `#ffffff`, text `#4d545c`, border `1px solid #f2f4f5`, radius `8px`, padding `10px 16px`, weight 500, height 44px.

Footer list link: white at opacity 0.7, 200ms ease-in-out opacity, hover opacity 0.85 (declared, not hovered).

Auth "Sign up" and "Forgot password?": `#7e7d77`, 14px weight 300 and 12px weight 300.

## Text field

Login email and password sit in `.input.input-focus-within.h-11.px-4`: background `#151514`, border `1px solid #2d2d2a`, radius `8px`, height 44px, padding `0 16px`, width 320px on login and 380px on signup. Input text `#eeeeed`, 14px weight 400. Placeholder `#727169`.

Declared focus, not forced on a live element: `.input-focus-within:focus-within:is(.dark *)` sets border `rgb(255, 178, 36)` and ring `#4d2e00`. The light rule sets border `rgb(255, 190, 61)` and ring `#ffe0b3`.

Error, disabled and filled states were not shown. The fields were left empty.

## Checkbox

Signup "Agree to terms of service" is a native checkbox, 18 by 18, background `#ffffff`, border `1px solid #6b7280`. It was not checked. Marketing pages had no checkbox.

## Card

Pricing plan cards are 304px wide, radius 16px, white, shadow `rgba(0, 0, 0, 0.1) 0px 0px 26px -3px`. The inner block pads 24px. Personal adds border `1px solid #ffbe3d` and ring `rgba(254, 189, 60, 0.16) 0px 0px 0px 4px`.

Quote cards on pricing: background `#fdfdfc`, border `1px solid #f2f1f1`, radius 16px, padding `20px 24px 24px`.

Home gallery cards: background `#33383d`, text white, radius 8px, about 278 by 319.

## Badge

Home gallery pill "Directory": background `#262a2e`, text `#ccd1d6`, padding `4px 8px`, radius 30px, height 26px. The stylesheet also declares `.notion-pill` at radius 3px and 0.875rem. The painted pill used 30px.

## Billing track

Three links inside a callout: background `#ededed`, border `1px solid #e5e5e5`, radius 12px, shadow `rgba(0, 0, 0, 0.1) 0px 0px 26px -3px`. Each link pads `8px 12px`, radius 8px. Monthly is painted white. Yearly and Multi-pack are transparent with text `#66707a`.

## Gaps

- Hover, pressed, loading, disabled and error were not shown.
- Text area, select, radio, switch, tabs, menu, tooltip, dialog, toast and avatar were not on the pages opened.
- The compare-plans table was visible. Its cells were not measured one by one.
- Signed-in app chrome was not entered.
- No crops. Screenshot frames failed.
