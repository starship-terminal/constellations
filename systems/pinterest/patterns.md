# Patterns

How the public pages combine the components. Screenshots are in [screenshots/](screenshots/).

## App shell

The signed-out header is 80px tall: the red wordmark, Explore, a pill search, then About, Businesses, Create, News, a red Log in and a gray Sign up. See [home-light-default](screenshots/home-light-default.png) and [header-default](components/crops/header-default.png).

On a 390px phone the header keeps the wordmark, Log in and Sign up, and drops Explore and the search pill. The hero becomes a full-width red button. See [mobile-home-light-default](screenshots/mobile-home-light-default.png).

## Marketing home

A large black headline, one red primary and one gray secondary, then a collage of rounded photos. Below that, a seasonal section and a horizontal board carousel. See [home-light-default](screenshots/home-light-default.png) and [home-light-carousel-next](screenshots/home-light-carousel-next.png).

## Explore

Category tabs with an underline on the selected one, a headline, a photo collage, then a row of board cards. See [ideas-light-page](screenshots/ideas-light-page.png). A topic hub uses the same shell: [ideas-art-light-page](screenshots/ideas-art-light-page.png).

## Board

Title, a featured-board line, a short description, an avatar row, a cover image with a share icon button, then a masonry of pins. See [board-light-page](screenshots/board-light-page.png). Saving a pin opens the login dialog. That dialog is [ideas-light-auth-dialog](screenshots/ideas-light-auth-dialog.png). Nothing was typed.

## Shop

A shopping landing with category chips that link to idea hubs. See [shopping-light-page](screenshots/shopping-light-page.png). No checkout exists signed out.

## Help

A separate help site: a search pill, three columns of article links, outline See more buttons. See [help-light-default](screenshots/help-light-default.png). One article: [help-article-light-default](screenshots/help-article-light-default.png). Search was focused and not submitted.

## Login wall

[https://www.pinterest.com/login/](https://www.pinterest.com/login/) and the header Log in button open an email and password form, plus Google and a QR code. The QR code is a credential and is not in the package. The dialog without the QR image is [dialog-login-default](components/crops/dialog-login-default.png). The branch stops there.

## Empty, loading, error, confirmation

Not captured. The public pages did not show an empty search, a skeleton, an error card, or a destructive confirmation. A loading spinner token exists in CSS (`--comp-spinner-motion-enter-duration`) and was not measured on an element.
