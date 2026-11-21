# ElevenMusic components

Public surface only, measured 2026-11-21. Signed-in studio, library, composer, and chat were not entered.

## Button

Sign in is a quiet pill. Start free is the inverted pill. Continue with Google and Continue with Apple are taller provider pills inside the login dialog.

| State | Evidence |
|---|---|
| default | [screenshots/home-dark-default.png](screenshots/home-dark-default.png), [screenshots/home-light-default.png](screenshots/home-light-default.png) |
| disabled | Continue with Email stays disabled while the email field is empty. [screenshots/login-dialog-email-dark.png](screenshots/login-dialog-email-dark.png) |
| hover, focus-visible, pressed, loading | Not captured. |

Dark Sign in is 32px tall, 14px Inter, `#222222` on `#fafafa` text, pill radius. Start free inverts that. Light swaps the pair.

## Icon button

Close sidebar, Search, Attach, and the prompt submit arrow are icon buttons. Search opens the login dialog. Attach opens a menu.

## Link

Nav links (Explore, Pricing) and footer links are 16px Inter in the text colour. Terms and Privacy inside the login wall are underlined links.

## Text field

The home prompt is a 15px Inter input, 36px tall, transparent, inside a rounded bar. The login email field appears only after Show other options, with placeholder "Enter email address". It was left empty.

Text area, select, checkbox (beyond the unread terms checkbox), radio, and switch are not present on the public chrome. The terms checkbox was not checked.

## Tabs

Tools uses Featured, Studio, and All. Home uses Songs and Sounds, and Featured, Trending, and New. Blog uses All, Guides, Product, and Industry.

## Menu

Resources, Attach, language, Instrument, and Genre open menus. See [site-tree.md](site-tree.md).

## Dialog

Log in or sign up, Log in to upload, Log in to download, Share, and Tempo. The login dialog is recorded in [login-review.json](login-review.json).

## Tooltip, toast, table

Not present on the public pages that were opened.

## Card

Track cards, sound packs, tool cards, and plan cards. Plan cards sit on [screenshots/pricing-dark-default.png](screenshots/pricing-dark-default.png).

## List row

Playlist rows in the sidebar, track rows on charts, and artist rows.

## Avatar

Artist and playlist art on cards. No account avatar was shown.

## Badge

Featured on the sidebar playlists, and v2.5 on track cards.

## Gaps

Hover, focus-visible, pressed, and loading were not held. Error and validation states were not triggered, because no form was submitted. Signed-in components are not in this package.
