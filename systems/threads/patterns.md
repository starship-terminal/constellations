# Patterns

How the signed-out controls combine. Screenshots are headless Chromium after the same URLs loaded in the T3 preview tab without a Cloudflare challenge.

## Signed-out home

A public feed sits in a 640 px column (`size.column`) with a 24 px bottom radius and a soft column shadow. A login card floats at the top right. A modal, "Say more with Threads", covers the centre. The scrim is `color.background.scrim`.

Dark, live class: [screenshots/home-dark-default.png](screenshots/home-dark-default.png).

Light, class-forced `__fb-light-mode`: [screenshots/home-light-default.png](screenshots/home-light-default.png).

The feed itself is public. The capture did not open a post, follow a profile, or search.

## Login page

`/login` is a centred column: a 16 px heading ("Log in with your Instagram account"), two empty fields, a white or black Log in button, a muted "Forgot password?" link, an "or" divider, the Instagram button, and a "Scan to get the app" caption at 13 px. Nothing was typed. Log in was not pressed.

Dark: [screenshots/login-dark-default.png](screenshots/login-dark-default.png).

Light, class-forced: [screenshots/login-light-default.png](screenshots/login-light-default.png).

The QR in those shots is the app-download code the page paints. It is not a session credential.

## Phone width

At 390 CSS pixels the dark home shows a top banner (Log in, Open app), the feed, and a "Thread on Threads" sheet with Open Threads and Continue with Instagram. `/login` at the same width is the full-screen "Say more with Threads" dialog plus a legal toast. Neither sheet was submitted.

[screenshots/mobile-home-dark-default.png](screenshots/mobile-home-dark-default.png)

[screenshots/mobile-login-dark-default.png](screenshots/mobile-login-dark-default.png)

Phone light was not captured.

## Help center

Threads Terms and the privacy supplemental live on help.instagram.com, not on the app's token set. The help page is light, 24 px titles, 12 px body. Recorded only so the legal links on the Threads footer have a destination. Do not restyle Threads with these values.

[screenshots/terms-light-default.png](screenshots/terms-light-default.png)

[screenshots/privacy-light-default.png](screenshots/privacy-light-default.png)

Cookies policy (https://help.instagram.com/1896641480634370/) was not shot.
