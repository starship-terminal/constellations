# Nothing patterns

How the public storefront combines the controls. Screenshots are in [screenshots/](screenshots). The site tree is [site-tree.md](site-tree.md).

## Header island

A white bar under a yellow promo strip. Wordmark on the left, AUDIO PHONES WATCHES CMF COMMUNITY in the centre, cart and account on the right. AUDIO and PHONES open a white mega menu over a dimmed page. WATCHES, CMF and COMMUNITY navigate. See [home-light-default.png](screenshots/home-light-default.png), [home-light-menu-audio.png](screenshots/home-light-menu-audio.png), [home-light-menu-phones.png](screenshots/home-light-menu-phones.png).

## Promo bar

One line, centred, black on yellow. It rotates between the sale line and the student line. The sale line goes to `/collections/sale`. The student line leaves the site. Not followed.

## Collection grid

Dot-matrix title, a category strip (ALL, AUDIO, HEADPHONES, and the rest), FILTER & SORT on the right, then three-up product cards on `#f4f4f4`. Card titles use the same dot face as the page title. Prices sit under the name. A struck price marks a sale. See [phones-light-default.png](screenshots/phones-light-default.png).

## Product page

Headphone (1) Pro paints `html.dark`: a dark canvas, a gallery, a yellow SAVE badge, a black ADD TO BAG control, and overview/specs. This is a painted page state. The CSS variable sheet does not change between light and dark probes. See [product-light-default.png](screenshots/product-light-default.png).

## Empty cart

A centred dialog: CART, "Your cart is empty", a black CONTINUE SHOPPING button, then text links for All products, Audio, Headphones, Phones, Earbuds, Speakers. See [home-light-cart.png](screenshots/home-light-cart.png).

## Error

`/login` is a 404. A white card on the dotted page says Page Not Found, with a black BACK TO HOME button. See [notfound-light-default.png](screenshots/notfound-light-default.png).

## Phone width

The header collapses to a Menu button. The drawer lists AUDIO and PHONES with chevrons, then WATCHES, CMF, COMMUNITY. See [mobile-home-light-menu.png](screenshots/mobile-home-light-menu.png).

## Account wall

The account icon leaves the store for `https://account.nothing.tech/v2/login/` and asks for email and password. That branch stops. Nothing was typed.
