# Components

Public marketing chrome only. Measured 2026-11-22 on `https://www.conductor.build/` and on the empty login wall at `https://app.conductor.build/users/log_in`. States that need a signed-in app were not reached.

## Button

The header Download button is 32px tall, 6px radius, fill `#eae8e6`, label `#141110`, 14px weight 500, sans. Get Conductor is the same fill at 40px tall, weight 600, and stretches to the content width on the phone. Hover, pressed, disabled, and loading were not measured.

[screenshots/home-dark-desktop.png](screenshots/home-dark-desktop.png)

## Link

Header links are 14px sans, weight 400, colour `oklab(0.931899 0.00135055 0.00321984 / 0.7)` on the dark page. Footer links repeat the same quiet treatment. Focus-visible was not measured.

## Text field

Not present on the public marketing pages. The login and signup walls show identity-provider buttons, not an email field. Not captured: the field lives behind Other sign-in options, which was not clicked.

## Menu

At 390, Open menu expands the header. The panel is navigation named Mobile. It lists Changelog, Docs, Sign in, and Download. Close menu collapses it.

[screenshots/site-tree/phone-menu.png](screenshots/site-tree/phone-menu.png)

## Dialog

Download opens a dialog titled "Download Conductor". Close dismisses it. The Apple silicon download, the Intel dmg link, and the Windows/Linux waitlist were not followed.

[screenshots/site-tree/desktop-download-dialog.png](screenshots/site-tree/desktop-download-dialog.png)

## Card

Changelog entries on the homepage are three cards in a row at 1440, a horizontal strip at 390. Each card shows a version, a date, and a title.

[screenshots/changelog-entry-dark-desktop.png](screenshots/changelog-entry-dark-desktop.png)

## Badge

Version labels such as 0.98.0 sit beside the date on changelog cards. No separate badge component was measured.

## Not present on the public site

Checkbox, radio, switch, select, text area, toast, table, tabs, tooltip as a component, avatar as an account control. The homepage demo of the product shows a fake sidebar and a fake changes panel. That demo is a marketing illustration, not the signed-in app.

## Icon button

Open menu and Close menu are 36px square icon buttons in the phone header. The download dialog Close is a 28px icon button.
