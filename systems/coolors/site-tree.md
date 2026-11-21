# Coolors site tree

Mapped on 2026-11-21 from the public homepage [https://coolors.co](https://coolors.co), signed out, light theme, viewport 1440 × 900. `body` class was `route-homepage has-header-ad`, not `is-logged`. Each row is a control that was opened or followed from that page. Login, signup, and identity-provider buttons were not submitted and not clicked.

The public header is a 60px white bar: wordmark, Tools, Go Pro, Sign in, Sign up. No cookie banner was on screen.

## Header

| Control | Opens |
|---|---|
| Wordmark (`#header_logo`, href `/?home`) | Homepage |
| Tools (`#header_tools-btn`) | `#megamenu` overlay. Escape leaves the menu in the DOM. Shot: [home-light-tools-menu.png](screenshots/home-light-tools-menu.png) |
| Go Pro (`.header_go-pro-btn`) | `#modal-pro` (not opened). "Learn more" and "And more..." in that modal both go to `/pricing`. |
| Sign in (`header .header_signin-btn`) | `#fullscreen-access` overlay, intro panel. Not a navigation. Shot: [home-light-signin-wall.png](screenshots/home-light-signin-wall.png). Closed with `#fullscreen-access_close-btn`. |
| Sign up (`.header_signup-btn`) | Same overlay, signup panel (Full Name, Email, Password, "Create your free account"). Not opened. |

## Tools menu

| Control | Opens |
|---|---|
| Palette Generator | `/generate` |
| Explore Palettes | `/palettes` (redirects to `/palettes/trending`) |
| Image Picker | `/image-picker` (not opened) |
| Contrast Checker | `/contrast-checker` (redirects to a pair URL) |
| Palette Visualizer | `/visualizer` (not opened) |
| Color Picker | `/color-picker` (not opened) |
| Tailwind Colors | `/tailwind` (not opened) |
| Color Bot | `/color-bot` (not opened) |
| List of Colors | `/colors` (not opened) |
| List of Gradients | `/gradients` (not opened) |
| Gradient Maker | `/gradient-maker` (not opened) |
| Gradient Palette | `/gradient-palette` (not opened) |
| Image Converter | `/image-converter` (not opened) |
| Photo Editor | `/photo-editor` (not opened) |
| SVG Recolor | `/image-recolor` (not opened) |
| Collage Maker | `/collage-maker` (not opened) |
| Free Fonts | `/fonts` (not opened) |
| iOS APP | `https://apps.apple.com/app/coolors/id956480678` (not opened) |
| Figma Plugin | Figma community plugin (not opened) |
| Adobe Extension | Empty `href`, `target=_blank`. Not followed. |
| Chrome Extension | Chrome Web Store (not opened) |
| Pricing | `/pricing` (page opened; currency was local, so no shot is committed) |
| Help Center | `https://help.coolors.co` (not opened) |
| Features Request | `https://coolors.supahub.com` (not opened) |
| Affiliate | `/account/affiliation` (account wall, not followed) |

## Sign-in overlay

Opened from Sign in. Not submitted.

| Control | Opens |
|---|---|
| Continue with Google (`#fullscreen-access_google`) | Identity provider. Not clicked. |
| Continue with Apple (`#fullscreen-access_apple`) | Identity provider. Not clicked. |
| Continue with email (`#fullscreen-access_email`) | Email panel. Not clicked. |
| Close (`#fullscreen-access_close-btn`) | Dismisses the overlay. Verified: display none. |
| Terms of Service | `/terms-of-service` (link in the overlay, not followed) |
| Privacy Policy | `/privacy-policy` (link in the overlay, not followed) |

The signup panel and the reset-password panel sit in the same overlay and were not opened.

## Homepage body

| Control | Opens |
|---|---|
| Start the Generator | `/generate`, then a palette URL. A tutorial modal ("Let's go!") was closed with `.modal_close-btn`, not "Let's go". Shot: [generate-light-desktop.png](screenshots/generate-light-desktop.png) |
| Explore 10M+ Palettes | `/palettes/trending`. Shot: [palettes-light-default.png](screenshots/palettes-light-default.png) |
| Color of the day (`#homepage_color-of-the-day`) | `/add8e6` (`#ADD8E6` Light Blue). Not visited. |
| Tool cards | Same destinations as the Tools menu: `/generate`, `/palettes`, `/image-picker`, `/contrast-checker`, `/visualizer`, `/color-picker`, `/tailwind`, `/color-bot`, `/colors`, `/fonts`, `/collage-maker`, `/photo-editor`, `/gradients`, `/gradient-palette`. Contrast checker was opened. Shot: [contrast-light-default.png](screenshots/contrast-light-default.png) |

## Footer

Footer links repeat the tool destinations, plus `/license`, `/terms-of-service`, `/privacy-policy`, `/cookie-policy`, `/advertise`, `/contact` (a form, not submitted), and `/account/affiliation` (not followed). Manage cookies (`iubenda-cs-preferences-link`) was not clicked. `#footer_language-selector` opened a list: English, Italiano. No language was selected. Social links (X, Pinterest, Instagram, Product Hunt) and `http://fabrizio.io` were not opened.

## Phone

At 390px the header collapses to a menu button (`#mobile-header_menu-btn`) and the wordmark. `#mobile-menu` was in the DOM (`display: none`) and was not opened. Its signed-out list repeats the tools plus Sign in, Sign up, and Go Pro. Shot of the homepage only: [home-light-mobile.png](screenshots/home-light-mobile.png).
