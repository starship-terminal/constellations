# Components

Signed-out chrome measured on pi.ai on 19 November 2026, plus the public marketing controls on hey.pi.ai. States that were not on screen are listed under Gaps. No crops were saved: the preview browser did not produce screenshot frames.

## Button

The filled action is a pill. On the light chat at 1440×900, header Log in is 128×48, radius 48px, padding-inline 16px, background `#1A4631` (`light.background.action`), text `#FCFAF7`, DM Sans 16px weight 400. The sidebar Log in is 247×56 with the same fill. Sign up for free is the outline pill: 160×48, 1px border `#E1D3C0`, fill `#FAF3EA`, text `#655E55`.

On the dark chat at 1169×731 the same pills use `#289A62` with text `#242322`. Sign up for free uses a 1px border `#504A42` and text `#B4AFA7`.

Submit name is a 40×40 circle, radius 9999px. Light fill `#038247`, dark fill `#43A774`, icon colour `#FCFAF7` in light and `#242322` in dark.

The marketing Try Pi control on hey.pi.ai is a separate pill: nav 96×40, radius 40px, fill `#131212`, label Grenette 14px white. The hero button is 160×56, radius 40px, fill `#000000`, label Grenette 18px white, padding-inline 48px.

Hover, pressed, disabled and loading were not on screen. The stylesheet declares `hover:bg-fill-hover`, `active:bg-fill-tap` and `disabled:opacity` on the button class. Those declarations were not forced.

## Icon button

Sidebar toggle, chat options and the close-sidebar control are 40×40, padding 6px, radius 10px, transparent fill, 1px transparent border, icon colour `#655E55` in light and `#B4AFA7` in dark. Email and Phone on the login page are 56×56 circles, radius 9999px, 1px border `#E1D3C0` in light and `#504A42` in dark.

## Link

Terms and Privacy Policy in the chat footer are DM Sans 14px weight 500, colour `#038247` in light and `#43A774` in dark, class `text-tertiary-default`. On the login page the same words are 16px `#038247` in light and `#33C782` in dark. Marketing nav links (Get the app, Help) are Grenette 15px, line-height 30px, letter-spacing -0.15px, colour `#131212`.

## Text field

The signed-out greeting asks for a name. The field is 528×40 at 1440, radius 10px, padding-inline 16px, 1px border. Light surface `#FCFAF7`, border `#D9C9B4`, text `#131212`, DM Sans 16px weight 500, letter-spacing -0.16px, line-height 22.4px. Dark surface `#2C2A28`, border `#504A42`, text `#D8D4CE`. Placeholder colour is the `--color-placeholder` token, `#BEB09D` light and `#AAA6A1` dark. The field was left empty.

## Text area, select, checkbox, radio, switch, tabs

Not present on the signed-out chat, the login page, or the marketing home.

## Menu

Chat options is an icon button. The menu it would open was not opened. Declared menu tokens exist (`--color-menu-background`, `--color-menu-stroke`, `--shadow-menu-shadow`) and are in `tokens.json`. They were not seen painted.

## Tooltip, toast, dialog

Not opened. Login is a full page at `/onboarding/login`, not a dialog. Declared modal and toast shadows are in the token file. A toast was not shown.

## Card

No card was painted on the signed-out surfaces. `.rounded-card` is declared at 28px and kept as `core.radius.card`. The marketing feature bands are full-bleed sections, not cards. Feature 2 and Feature 4 use `#F7EFE4`.

## List row

The sidebar shows one chat row, "Greetings from Pi", and a Help and feedback row. Help and feedback is 255×40, radius 8px, padding-inline 12px, gap 12px, text `#655E55` in light and `#B4AFA7` in dark. The chat title's own metrics were not separated from the row.

## Table, avatar, badge

Not present on the captured surfaces. The sidebar has no avatar while signed out.

## Marketing type

hey.pi.ai h1 at 1440 is Grenette 64px, line-height 60.8px, letter-spacing -3px, colour `#131212`. At 390 the same heading is 40px, line-height 38px, letter-spacing -3px, width 342px. Section headings are Grenette 52px, line-height 49.4px, letter-spacing -2.08px. Body under the hero is Grenette 20px, line-height 28px, letter-spacing -0.4px.

## Gaps

- Hover, focus-visible, pressed, disabled, loading and error were not captured as painted states. Focusing Log in drew a Tailwind ring: 1px white offset and 2px `rgb(59 130 246 / 0.5)`. That blue is the Tailwind default `--tw-ring-color`, not a Pi colour token, so it is not in `tokens.json`.
- No component crops. `preview_snapshot` returned "The browser is not producing screenshot frames" on every attempt.
- OAuth buttons were measured and not clicked. Email and Phone were measured and not clicked.
- The name field was not filled and not submitted.
- Checkbox, radio, switch, select, tabs, tooltip, toast, dialog, table, avatar and badge were not on these pages.
