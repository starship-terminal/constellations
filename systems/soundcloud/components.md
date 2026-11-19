# Components

Signed-out controls measured on soundcloud.com and secure.soundcloud.com/web-auth on 2026-11-19. Crops are 256-colour.

## Button

Hero Sign in is a 36px pill, white `#ffffff` with black type, padding `0 18px`, radius `9999px`, Söhne 14/600. See [hero-signin-default.png](components/crops/hero-signin-default.png).

Hero Create account is the same height, black `#000000` with white type, width about 135px. See [hero-create-default.png](components/crops/hero-create-default.png).

Get started is 32px tall, fill `#f3f3f3`, ink `#121212`, 17px/600, letter-spacing 0.2px, padding `0 24px`. See [hero-get-started-default.png](components/crops/hero-get-started-default.png).

The app header also computes a 32px Sign in (fill `#121212`, white type) and a white Create account. That header has `overflow: hidden` and height 0 on the marketing home, so those buttons are not painted there.

Phone Sign in is 40px, radius 4px, transparent, ink `#121212`. Listen in app and Create a free account are `#121212` with white type, radius 4px, heights 40px and 48px.

Hover on the header pills did not change background, colour, or opacity. The transition is opacity over 200ms linear. A painted hover state was not observed.

## Link

Learn More and the play button use `#699fff`. Footer links use `#999999` at 14/400. Terms of Use on the light auth tab uses `#044dd2`. Focus on the logo link computed `outline: dotted 1px`.

## Text field

Header search is 36px, fill `#303030`, radius 3px, padding `8px 40px 8px 16px`, white type, 14/400. Focus sets the border to `1px solid rgba(153, 153, 153, 0.686)`.

Auth email is a 54px field, radius 4px. Dark iframe fill is `#303030`. Light standalone tab fill is `#f3f3f3`, and focus draws a `#666666` border. Placeholder: "Your email address or profile URL". Error and disabled were not shown. The form was not submitted.

## OAuth button

Continue with Facebook, Google, and Apple are 48px, radius 100px, 16/600, letter-spacing 0.16px. Dark iframe: transparent fill, border `1px solid rgba(255, 255, 255, 0.16)`, white type. Light tab: the same border at `rgba(18, 18, 18, 0.16)` and ink `#121212`.

Continue is the primary. Dark iframe: white fill, ink `#121212`, opacity 0.5 while disabled. Light tab: `#121212` fill, white type, opacity 0.5 while disabled. It was not clicked.

## Dialog

Sign in opens `.auth-modal` over `rgba(255, 255, 255, 0.4)`. The sheet is `.modal__modal`, 450px wide, radius 4px, padding 16px. The form lives in an iframe from secure.soundcloud.com. Close is a 32px circle, fill `#303030`, white type. See [auth-card-default.png](components/crops/auth-card-default.png).

## Card

The home hero is 1240 by 450px at 1440, radius 16px. Contact inquiry cards are 608px wide, radius 20px. Press is `#e76b9f`. Advertising is `#ab87e2`. Help Center's own fill was transparent in the reading. Those cards are the company site, not the listener chrome.

## Play button

`.playButton` is a 64px circle, white fill, icon `#699fff`. The progress bar is 2px, `#ff5500`. The player bar is 48px. Playback was not started.

## Gaps

Text area, select, checkbox, radio, switch, tabs, menu, tooltip, toast, table, avatar, and badge were not present on the pages that loaded, or they sit behind an account. No validation error was shown. No paid plan was opened. No email was submitted.
