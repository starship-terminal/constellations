# Components

Signed-out TIDAL chrome, measured on 2026-11-19. Values are token names. The preview browser did not paint screenshots, so this inventory has no crops.

## Button

The player uses a 32px pill. Create a free account is white with `dark.color.button.primaryText` (`#101010`), weight 600, 16px inline padding, radius `core.radius.full`. Log in and Download TIDAL are `dark.color.button.secondaryBg` (`rgba(40, 40, 40, 0.75)`) with white text, the same size, and `backdrop-filter: blur(20px) saturate(1.8)`.

Get started on the transfer card is 40px tall, `dark.color.bg.quietButton` (`rgba(255, 255, 255, 0.08)`), same pill radius and type.

Hover on Log in moved the background from `rgba(40, 40, 40, 0.75)` to `color(srgb 0.244564 0.244564 0.244564 / 0.769098)`. Text stayed white. Focus-visible is declared as a 3px solid `--wave-color-solid-contrast-fill` outline, offset 3px, on `._marketButton_1d16h_1:focus-visible`. That state was not forced.

Pressed, disabled and loading were not on the player chrome.

## Login button

On `login.tidal.com/authorize`, Continue is 50px tall, 459px wide in the 1169px viewport, radius 12px, white face, black text, weight 600, 20px inline padding. It was disabled at opacity 0.4. Continue with Passkey, Continue with Google and Continue with Apple share that face. They were not clicked.

## Link

Sidebar links are 40px tall, 208px wide inside a 240px aside, 8px padding, 12px radius, 14px medium. Selected (Music, then Explore) uses `dark.color.bg.selected` and white text. Unselected text is `dark.color.text.secondary`.

View all is 14px medium white, no underline in the computed style. A playlist title link computed `text-decoration-line: underline`.

## Text field

The authorize email field's wrapper is 54px tall, 459px wide, radius 16px, transparent fill, inset 1px white stroke. The input itself has no border, 16px semibold Nationale, white caret, placeholder "Enter your email or login name". Placeholder colour is declared as `var(--ts-color-form-text-alt, rgba(var(--ts-color-text-rgb), .4))`. No value was typed.

## Text area, select, checkbox, radio, switch

Not present on the signed-out surfaces that were opened.

## Tabs

Home uses a text tab row: For you is white, 14px medium, 4px top padding and 10px bottom padding. Staff Picks is the secondary text colour. No tab indicator rule was measured.

Explore section titles (Featured, Genres) are 20px weight 600 Square Sans Text, line-height 24px.

## Menu, tooltip, toast

Not opened. A sorting and filter control was named in the player, and was not opened.

## Dialog

Log in does not open a dialog on tidal.com. It navigates to `login.tidal.com/authorize`, an OAuth authorize page (`response_type=code`, `scope=r_usr w_usr`). The page background is black. The form sits in a centred column. No modal chrome was measured around it.

The OneTrust cookie banner was in the DOM. Its Accept and Reject buttons computed 34px tall, radius 1000px, 12px type, weight 600, background `rgb(60, 60, 60)`. Their box sat at the bottom edge of the 731px viewport and was not treated as a measured layout. The banner was not accepted or rejected.

## Card

Artwork images on Explore computed 4px radius. The transfer card title is 12px medium white. Its body is 12px regular at `rgba(255, 255, 255, 0.55)`, line-height 18px. The card container's own padding was not isolated from the sidebar inset.

## List row, table, avatar, badge

A track row, table, avatar and badge were not measured as components. Playlist tiles and artwork were on the home page. Their layout was not cropped.

## Icon button

Back and Next are 32px circles. In the resting state their colour was `rgba(255, 255, 255, 0.15)`. The wordmark button is 24px.

## Gaps

- No screenshots or crops. The preview browser did not produce screenshot frames, and headless Playwright was blocked.
- Hover is one colour reading, not a crop.
- Focus-visible, pressed, disabled (player), loading and error were not forced.
- Light theme was not on the public chrome.
- Signed-in player, search results, menus, toasts and form errors were not entered.
- OAuth continue buttons were not clicked, so no account session exists.
