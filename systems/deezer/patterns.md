# Deezer patterns

Public, signed-out, captured 2026-11-21.

## App shell

Two shells.

Marketing pages use a black header (logo, Plans, Features, Music, Log in, Sign up) over a white page, then a black footer with plan, feature, catalogue and legal columns. On a 390px phone the header keeps the logo, a Sign up pill and a burger. The burger opens a full-screen dark drawer. See [home-desktop-default.png](screenshots/home-desktop-default.png) and [home-phone-menu-open.png](screenshots/home-phone-menu-open.png).

The channel player is a dark app shell: left nav (Home, Explore, a playlist prompt), a search field, a channel grid, a pale signup banner, and a bottom player. Phone collapses the nav into the marketing burger and stacks category cards. See [explore-desktop-default.png](screenshots/explore-desktop-default.png) and [explore-phone-default.png](screenshots/explore-phone-default.png).

## Form

The login wall is a centered form on black: email field, password field with a show-password icon button, a full-width purple submit, then Facebook, Google and Apple icon buttons. It was not submitted. See [login-wall-desktop-default.png](screenshots/login-wall-desktop-default.png).

The cookie notice is a light dialog over the homepage. Accept, Refuse and Preferences were not clicked. The dialog was hidden in the DOM for later shots. See [home-desktop-cookie.png](screenshots/home-desktop-cookie.png).

## Empty, loading, error

Not captured. The signed-out player shows a "Create your first playlist" prompt instead of an empty library. No error or loading state was held.

## Destructive confirmation

Not present on the public surface.

## Feedback

Not captured. No form was submitted, so no success or error toast was shown. Tempo still declares success, warning and danger fills.

## Search and filtering

The player search field focuses in place. No query was typed, so suggestions were not captured. Channel pages are the public browse surface. See [explore-desktop-search-focus.png](screenshots/explore-desktop-search-focus.png).

## List or table

Channel tiles are the public list. Charts repeats the same card grid. The open-source report page is a long text list, not a data table.

## Onboarding

Not captured. Sign up, gift codes and account creation stop at the login or signup wall.
