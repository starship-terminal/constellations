# West Elm components

Inventory of controls measured on the public pages that loaded on 2026-11-21. Shop, product, cart and favorites pages returned HTTP 403, so catalogue cards, filters, swatches and add-to-cart were not measured. Crops were not cut. The screenshots named here are the evidence.

## Button

Primary fill is ink `rgb(33, 33, 33)` with a white label, 1px ink border, 0 radius, padding 12px 24px, about 43px tall. Label is GT Eesti Text 14px, weight 375, letter-spacing 1.4px, uppercase. Seen as SHOP NOW on the home page and CONTINUE WITH EMAIL on [login-light-default](screenshots/login-light-default.png). Hover, pressed, disabled and loading were not measured.

Secondary social buttons (Continue with Google, Continue with Apple) sit beside the primary on the login page. They were not clicked. Their resting fill was not isolated from the screenshot.

## Link

Primary nav links are 12px / 300 / 40px line-height, letter-spacing 0.96px, uppercase, ink on white. SALE is a red label, sampled `#bf4759` from the raw home screenshot. Secondary nav links are 14px / 300, colour `rgb(100, 100, 100)`. Footer links are 12px / 300, the same muted colour, on the footer fill. [home-light-default](screenshots/home-light-default.png).

## Text field

Search is a 400x36 input, 1px border `rgb(200, 200, 200)`, padding 6px 35px 6px 16px, 14px type, 0 radius. Login email is 59px tall, 16px type, padding 28px 16px 8px, white fill. On focus the outline is 2px `rgb(37, 99, 235)` and the border becomes ink. [login-light-email-focus](screenshots/login-light-email-focus.png). No value was typed. Error and disabled states were not reached.

## Menu

Desktop category hover opens a white multi-column flyout under the primary nav. [home-light-nav-furniture](screenshots/home-light-nav-furniture.png). ACCOUNT hover opens a short list: Sign In / Create Account, B2B Member Sign In, View My Rewards, Key Rewards, West Elm Credit Card, Registry. [home-light-account](screenshots/home-light-account.png).

Phone width: the hamburger (`#menu-icon`, aria-label "show site navigation") opens a left drawer of the same categories, with Favorites, Registry, Track Order and My Store as a row above them. A marketing overlay covered the button until it was removed from the DOM. [mobile-home-light-menu](screenshots/mobile-home-light-menu.png).

## Dialog

An email signup dialog (`#join-email-campaign`) opens on the homepage. It was removed so the nav could be read, and it was not submitted. [home-light-signup](screenshots/home-light-signup.png). A phone marketing overlay also covered the drawer button. [mobile-home-light-overlay](screenshots/mobile-home-light-overlay.png).

## Card

Home tiles are edge-to-edge photographs with a small caption and a text link ("SOFAS & SECTIONALS"). No product detail page loaded, so price, swatch and add-to-cart treatments are only visible as captions on the home tiles. [home-light-default](screenshots/home-light-default.png).

## Not present on the loaded pages

Text area, checkbox (except an unchecked "keep me signed in" on the track-order page, not measured), radio, switch, tabs, tooltip, toast, table, avatar, badge as a component, select (store locator has selects; not measured as a component state set).

## Gaps

- Hover, pressed, disabled and loading were not measured. A registry CTA hover shot was not taken after the account locator hung.
- No component crops. Values are computed styles and two sampled pixels, named in [tokens.json](tokens.json).
- Catalogue, product, cart and favorites controls are behind the 403 and are Not captured.
