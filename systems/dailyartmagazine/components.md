# Components

Measured on the public magazine, 2026-11-21, signed out. States that were not on the page are marked not present or not captured.

## Button

Primary is a black fill, white Basier 14/600, 3px radius, about 40px tall. Search in the header is the same face with a white keyline on the ink bar. Donate is a translucent crimson fill. Amount buttons inside the donate dialog are the black primary.

| State | Where |
|---|---|
| Default | [home](screenshots/home-light-default.png) Search; [contact](screenshots/contact-light-default.png) |
| Hover | Not captured as a separate crop. Header Stories was hovered; the button hover was not held. |
| Focus-visible | Not captured on a button. |
| Pressed | Not captured. Pressing Search navigates. |
| Disabled | Not present on the public pages. |
| Loading | Not present. |

## Icon button

`#hamburger` is a 20 by 15px mark in the header. It toggles the menu. No other icon button is part of the chrome. Social icons are image links.

## Link

Header links are white Basier 14/600. Footer and byline links are crimson `#c6002f`, no underline. Article body links use the same crimson.

## Text field

Search field on `/?s=`: white, 1px `#c9cfdf` border, 0 radius, 48px tall, Basier 14. Placeholder "Search articles, artist, museums or art stuff". Focus paints no ring (`outline: none`). Newsletter field: white, 3px radius, 40px tall. Not filled.

## Text area

Contact page, Contact Form 7. White, 1px `#989da7` border, 2px radius, about 202px tall. Placeholder "Your message". Not filled.

## Select

Not present on the photographed pages. The theme CSS includes Select2 rules. No select was on screen.

## Checkbox

Newsletter consent checkbox, 13px, unchecked. Not toggled. Contact form has a terms checkbox. Not toggled.

## Radio

Not present.

## Switch

Not present.

## Tabs

Not present. The menu columns are links, not tabs.

## Menu

The hamburger opens `nav.fixed-nav.navigation.open`: a white panel of crimson links in five columns, then the site pages. See [site-tree.md](site-tree.md). Shot: [home-light-menu-open](screenshots/home-light-menu-open.png) and [mobile-home-light-menu-open](screenshots/mobile-home-light-menu-open.png).

## Tooltip

Not present.

## Dialog

Donate opens `.modal-r--show` on a `rgba(0,0,0,0.9)` scrim. The panel is a crimson illustration with white Roslindale display type and black amount buttons. Close is `.modal-close-r`. Shot: [home-light-donate-modal](screenshots/home-light-donate-modal.png). The panel sits in document flow below the fold, so the viewport shot shows the scrim and the top of the page more than the panel. The panel's colours were read from computed style.

## Toast

Not present.

## Card

Story card: image, crimson category badge, Roslindale title, slate excerpt, crimson author. On the home featured band the card sits on `#19191c` with white type.

## List row

Category archives and Latest are a grid of cards, not rows.

## Table

Not present.

## Avatar

Not present. Authors are a name link.

## Badge

`.category` is crimson fill, white Basier 10/700, 3px radius, 4px padding, 20px tall, uppercase. Example: RENAISSANCE.

## Gaps

- No dark theme.
- No focus ring paints on the search field.
- Pressed, disabled, loading, and error states of buttons were not on the public pages.
- Validation error of the contact form was not triggered (the form was not submitted).
- Icons are not extracted (docs/RIGHTS.md).
