# Components

Signed-out controls measured on 2026-11-19. Token names point at [tokens.json](tokens.json). Crops exist only where a screenshot was saved.

## Button

The brand action is `{color.fill-brand}` (`#17d5ff`) with black or near-black text.

| Variant | Where | Height | Radius | Face |
|---|---|---|---|---|
| Email submit | Auth dialog, Continue with email | 48px | 16px | `{light.component.button-brand.background}` |
| Marketing primary | Start for free, header Join | 48px | 12px | same cyan, text `#141a20` |
| App primary | Watch header Join | 40px | 12px | `{light.button.primary}` / `{light.text.inverted}` |
| Secondary | Watch header Log in | 40px | 12px | `{light.button.secondary}` |
| Social | Continue with Google, Facebook, Apple | 48px | 10px | white, 1px `{light.border.stroke}` |

Crop: [components/crops/button-primary-default.png](components/crops/button-primary-default.png), [components/crops/button-join-default.png](components/crops/button-join-default.png).

Hover, pressed, and disabled were not captured. A focused marketing Join link drew `outline: rgb(0, 129, 158) auto 1px` with `outline-offset: 1px`.

## Link

Terms and Privacy in the auth dialog are `{light.text.link}` (`#00aacf`), 12px, weight 500, no underline.

## Text field

The email field and the watch search input are 40px tall, radius 12px, face `{light.background.input}`, outline `rgba(41, 81, 128, 0.24)`. The floating label is `{light.text.secondary}`. Error and filled states were not captured. The email was not submitted.

## Dialog

Log in on the watch page opens a `role=dialog` panel, 592 by 525 at the 1169 viewport, radius 20px, white, shadow matching `--vimeo-shadows-lg`. Title is 20px ABC Repro Medium. The same form is the whole page at `https://vimeo.com/log_in` at 390px. No screenshot: preview frames failed.

## Switch

The pricing billing toggle is a Chakra switch, 50 by 28, track `{color.gray-900}`, thumb `{color.text-button-inverted}`, radius 48px. It was checked (yearly) when read.

## Badge

"Save 40%" is `{color.status-positive-primary}` (`#58a628`) on black text, radius 6px.

## Card

Plan surfaces on `/upgrade-plan` are white with a computed radius of 36.8px. The recommended banner is `#8a5ee8`, white text, top radius 20px. Video cards on the watch feed were not measured individually.

## Navigation

The watch sidebar selected row (Explore) is 40px tall, radius 12px, face `{light.button.secondary}`. At 390 the sidebar is closed and an `open-sidenav` control sits at the top left. The marketing header is fixed, 84px, background `#fafcfd`.

## Gaps

Icon button, text area, select, checkbox, radio, tabs, menu, tooltip, toast, list row, table, and avatar were not on the signed-out pages that were opened. Hover, pressed, disabled, loading, and error were not forced. Dark theme was not in the DOM. Signed-in library, upload, and checkout were not entered.
