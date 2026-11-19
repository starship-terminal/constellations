# Components

Signed-out Twitch, dark theme, 2026-11-19. Sizes are computed styles from the T3 preview tab (1169 by 731). Crops are from headless Chromium at 1440 by 900, device pixel ratio 2, after those URLs had loaded without a Cloudflare challenge.

## Button

Primary Sign Up is a pill. Fill `#9147ff`, text `#ffffff`, height 32, weight 600, radius `9000px`.

![Sign Up](components/crops/button-primary-default.png)

Hover and pressed were not held. The declared tokens are `#772ce8` and `#5c16c5`.

Secondary Log In uses `rgba(83, 83, 95, 0.38)` and the same 32px pill. The community banner paints a white Sign Up with black text, the overlay brand button.

Disabled Continue on `/signup` is `rgba(83, 83, 95, 0.55)`, height 36, width 488, and `disabled` is true until the email field is valid.

## Icon button

The search submit is 36 by 36, radius `0 8px 8px 0`, fill `rgba(83, 83, 95, 0.38)`. A separate Search control in the nav computed a 9000px radius and a 0 by 0 box, so it was not on screen.

## Link

"Use phone number instead" is `#bf94ff`, underlined, 14px, transparent background. The selected directory tab uses the same purple. Hover token is `#a970ff`. Hover was not held.

## Text field

Search is 36px tall, fill `#18181b`, radius `8px 0 0 8px`, padding `0 12px`. The signup email field is 32px tall, 488px wide, radius 8px, with an inset 1px ring `rgba(222, 222, 227, 0.95)`. Focus replaces that ring with a 2px `#a970ff` outer and inset shadow. No text was typed.

![Email field](components/crops/field-email-default.png)

![Search](components/crops/search-default.png)

## Text area

Not present on the signed-out pages.

## Select

Directory pages show a Language control and a "Recommended For You" sort control. Their open menus were not measured.

## Checkbox, radio, switch

Not present on the signed-out pages. The token set declares checkbox and toggle colours. Those controls were not on screen.

## Tabs

Directory uses Categories and Live Channels. The selected tab is `#bf94ff` at 14px. Category pages use Live Channels, Videos, and Clips. The underline weight was not isolated from the tab colour.

## Menu

The Browse overflow (the three-dot control) was not opened. No menu panel was measured.

## Tooltip

Not opened. `--color-background-tooltip` is `#ffffff` and `--color-text-tooltip` is `#0e0e10`.

## Dialog

`/signup` is a centered panel, form width 488. Title is Roobert 24px / 500. The page also offers phone signup and Google, Amazon, and Apple. None of those were followed.

![Signup panel](components/crops/dialog-signup-default.png)

The category page shows a "May Contain Labeled Content" notice with a purple Manage Settings pill. That notice was not measured control by control.

## Toast

Not present on the signed-out pages.

## Card

Channel preview thumbs on the directory computed 350 by 197 with radius 0. Category art is square. Tags under a card are 12px pills, fill `rgba(83, 83, 95, 0.38)`, height 20.

![Live card](components/crops/card-live-default.png)

![Category card](components/crops/card-category-default.png)

## List row

The left rail lists live channels with an avatar, a name, a category, and a red viewer count. Row padding was not measured as its own token.

![Sidebar](components/crops/sidebar-default.png)

## Table

Not present.

## Avatar

Side-nav avatars computed radius `9000px`. Sizes were not recorded as a scale.

## Badge

LIVE is `#eb0400` on white, radius 4px, padding `1px 5px`, 12px, height 19. A red count sits on the inbox icon in the nav. Its number is session chrome, not a design value.

## Gaps

- Light theme: adding `tw-root--theme-light` did not change computed colour tokens or the body background. No public theme toggle was found.
- Hover and pressed: declared button tokens only. Pointer states were not held.
- Signed-in shell, chat, settings, following, and subscriptions: not entered.
- Phone, Google, Amazon, and Apple signup: not entered. Signup is not email-only.
- Checkbox, radio, switch, text area, toast, table, open menu, open select, tooltip: not on the captured pages.
- Reduced motion: not probed. Durations are the three `--timing-*` custom properties.
