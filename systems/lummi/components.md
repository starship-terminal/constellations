# Lummi components

Measured on the public site on 2026-11-18, light theme, 1440 CSS pixels. A colour is the computed value, with the token that holds the same role.

## Navigation

**Photos** is the selected tab. 14px / 500, rgb(24, 24, 27) `light.text`, 40px tall, 2px bottom border in the primary ink. Illustrations and 3D are the same size in rgb(113, 113, 122) `light.textMuted`. Focus-visible draws a 2px solid outline. Pressed was forced and matches focus.

**Log in** is a text link, 14px / 500, ink. Hover moves the ink to rgb(24, 24, 27). It points at `/auth/login`. It was followed only as a page load of `/login`, never submitted.

**Icon button** is the header menu control, 40×40, 4px radius. Hover fills rgb(244, 244, 245) `light.surfaceMuted`.

## Button

**Try Pro for free** is 40px tall, 12px inline padding, 4px radius, black fill, white label, 14px / 500. Hover and pressed fill rgb(63, 63, 70). The word Pro is yellow. The button did not navigate in this session. The pricing page is `/pro`. Its checkout link was not pressed.

**Download** on the image page matches the black fill, 40px, 4px radius on the left. Hover fills rgba(24, 24, 27, 0.8). It was not pressed. [hover shot](screenshots/photo-light-download-hover.png).

**Continue** on the login wall is 48px tall, 16px padding, 4px radius, rgb(24, 24, 27) fill, rgb(250, 250, 250) label, 14px / 600. Hover fills rgb(63, 63, 70). It was not pressed.

**Continue with Google** is a white 48px button with a 1px border. It starts OAuth and was not pressed.

## Field

**Email** and **password** are 48px, 16px padding, 4px radius, white fill, 1px border. Focus-visible is a 2px outline. The email field was filled with `not-submitted@example.com` and cleared. Enter was not pressed. [focused](screenshots/login-light-email-focused.png).

**Search** is a 38px input inside a pill, placeholder "Search or create anything!". Clicking it opens the command palette. Nothing was submitted.

## Menu

**Tools** opens a white menu: Duotone, a Video switch, Following, Number of people, Lighting style, Orientation, Multi-select. [shot](screenshots/home-light-tools-menu.png). Items were not followed.

**Daily picks** opens a short menu (Popular, New). [shot](screenshots/home-light-daily-picks.png).

## Dialog

The search palette is a white dialog, 6px radius, over an 80% black scrim. It lists Create image, Create video, suggested tags, creators and explore cards. [shot](screenshots/home-light-search-palette.png). Create image and Create video were not pressed.

## Type

**Display** is the home h1, Inter 600, 141.12px / 144px at 1440, tracking tight, ink. **Explore** is 64px / 70.4px. **Search title** is 104px. **Lede** is 20px / 28px, weight 400.

## Badge

Tag pills on the image page are 12px / 500, 24px tall, pill radius, fill rgb(244, 244, 245).

## Card

Image tiles in the masonry, and the photo detail with creator, title, tags and Download. [photo](screenshots/photo-light-default.png).

## Gaps

Text area, select, checkbox, radio, tooltip, toast, table, a validation error, a destructive confirm, and onboarding were not on the captured public pages. The Tools Video switch was seen and not measured as its own computed style. The hamburger dialog stayed closed under a scrim.
