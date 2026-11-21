# Components

Measured on the signed-out chat and the login wall, 21 November 2026. Values are computed styles. Crops were not cut. The page screenshots are in [screenshots/](screenshots/).

## Button

Header Log in, light, 1440×900: 128×48 at x1120 y85, fill `#1A4631` (`--color-primary-default`), label `#FCFAF7`, radius 48px, DM Sans 16/24. Sidebar Log in is the same fill at 247×56. See [screenshots/home-light-default.png](screenshots/home-light-default.png).

Sign up for free: 160×48, fill `#FAF3EA`, label `#655E55`, border 1px `#E1D3C0`, radius 48px.

Dark header Log in uses `--color-button-accent-default` `#289A62`. See [screenshots/home-dark-default.png](screenshots/home-dark-default.png).

Hover, pressed, disabled and loading were not painted.

## Icon button

Submit name is a 40×40 circle, fill `#038247` (`--color-tertiary-default`), label `#FCFAF7`. It was not clicked.

Toggle sidebar is 40×40, radius 10px. Chat options is the same size and opens a menu.

## Link

Terms and Privacy Policy in the composer are `#038247`. Marketing nav links are Grenette 15px `#131212`. Try Pi in the marketing nav is a 96×40 pill, fill `#131212`, radius 40px.

## Text field

Preferred name, light: 528×40 at x572 y805, fill `#FCFAF7`, text `#131212`, DM Sans 16/22.4 weight 500, tracking -0.16px, radius 10px, border 1px `#E1D3C0`. Placeholder colour token is `--color-placeholder` `#BEB09D`. The field was left empty. The declared input border token is `--color-input-border` `#D9C9B4`. The painted border on this date matched the divider stroke `#E1D3C0`.

## Menu

Chat options opens a menu with one row, Auto-read. See [screenshots/home-light-chat-menu.png](screenshots/home-light-chat-menu.png).

## Login wall buttons

Continue with Google, Apple and Facebook, light: 353×56, fill `#FCFAF7`, label `#131212`, border 1.5px `#E1D3C0`, radius 48px. Email and Phone are 56×56 circles, border 1px `#E1D3C0`, label `#655E55`. None was clicked. See [screenshots/login-light-empty.png](screenshots/login-light-empty.png).

Dark OAuth buttons use the raised surface `#242322` and border `#504A42`. See [screenshots/signup-dark-empty.png](screenshots/signup-dark-empty.png).

## Not present on these surfaces

Select, checkbox, radio, switch, tabs, tooltip, toast, dialog, table, avatar, badge. The phone chat-history panel is a drawer, recorded in [patterns.md](patterns.md).
