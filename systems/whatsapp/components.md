# WhatsApp components

Public marketing components measured on whatsapp.com, signed out, on 2026-11-19. Values are computed styles. Crops are cuts of those pages. A control that was not on the page is in Gaps.

## Button

The Download link is the primary control. At innerWidth 1440 it measured 145 x 45, padding 12px 20px, radius 50px, 1px solid `#1c1e21`, fill `#25d366`, label `#1c1e21` at 16px / 500. Hover left the fill at rgb(37, 211, 102). Focus drew a 1px `#005fcc` outline, offset 1px, and no box-shadow.

The Log in link is the secondary control: white fill, 1px solid `#111b21`, radius 50px, padding 14px 20px, 116 x 46.

See [button-download-default](components/crops/button-download-default.png), [button-download-hover](components/crops/button-download-hover.png), [button-download-focus](components/crops/button-download-focus.png) and [button-login-default](components/crops/button-login-default.png).

## Link

Nav labels (Privacy) compute to 16px / 500, `#1c1e21`, line-height 16px. Learn more is 16px / 400, transparent, no radius. Inline contact links on the contact page sample to `#0373e9`. That blue was read from pixels, not from a computed style.

See [link-learn-default](components/crops/link-learn-default.png).

## Menu

Features opens a white list: Calling, Messaging, Groups, Channels, Meta AI, Status, Security, Parental controls. Items compute to 16px / 500, `#1c1e21`, padding 10px 0, line-height 19.2px. The painted panel's radius and shadow were not measured: the DOM walk landed on a transparent wrapper.

See [menu-features-open](components/crops/menu-features-open.png) and [home-light-menu](screenshots/home-light-menu.png).

## Header

80px tall at innerWidth 1440, background `#fcf5eb`, padding 16px 60px. At innerWidth 390 it is 58px with padding 12px 24px, a menu glyph and a round download icon.

See [header-default](components/crops/header-default.png).

## Card

The Browser / WhatsApp Web card on the download page is a white surface on the `#fcf5eb` field. Its radius and shadow were not measured. The crop shows the card and the Log in pill inside it.

See [card-web-default](components/crops/card-web-default.png).

## Heading

Home h1 is 80px / 400, line-height 80px, `#ffffff`, at innerWidth 1440. The same h1 is 44px at innerWidth 390. Download h1 is 60px / 400. Home section h2s are 60px or 48px, weight 400.

See [heading-hero-default](components/crops/heading-hero-default.png).

## Footer

Background `#111b21`. Column labels compute to 12px / 400 `#ffffff`. Link rows compute to 18px / 400 `#ffffff`.

## Gaps

- Text field, text area, checkbox, radio, switch, toast, table, avatar, badge, tooltip, dialog: not present on the captured marketing pages. Contact is a list of links, not a form. No field was filled.
- Tabs: not present.
- Select: a language `select` is in the DOM (pill radius 50px, fill `#111b21`, label `#ffffff`) and `display: none` at 1440. The visible language control was not measured.
- Icon button: the phone download control is a round green icon. Its computed box was not cropped.
- Menu radius and shadow: not measured.
- Pressed and disabled: not shown. Hover on Download did not change the fill.
- web.whatsapp.com login, including any QR pairing surface: not opened.
- WhatsApp Business, the blog, the help center and the app stores: other domains, not captured.
