# Replo patterns

How the public marketing pages combine the components. Screenshots are in [screenshots/](screenshots). The control map is [site-tree.md](site-tree.md).

## Marketing shell

Every captured page uses the same header: Product, Solutions, and Resources as menus, Customers and Pricing as links, then Log in, Start for free, and Book a demo. The page background is black. Body and headings are the cream ink. Start for free is the only cream-filled pill. Book a demo is a black pill with a cream hairline.

See [home-dark-default](screenshots/home-dark-default.png).

## Menus

Product, Solutions, and Resources each open a panel of links over the page. Escape closes the panel. The phone width uses one "Open menu" button for the same links.

See [home-dark-product-menu](screenshots/home-dark-product-menu.png), [home-dark-solutions-menu](screenshots/home-dark-solutions-menu.png), [home-dark-resources-menu](screenshots/home-dark-resources-menu.png), and [mobile-home-dark-menu](screenshots/mobile-home-dark-menu.png).

## Hero

A 56px Archivo heading, a short lede, and the cream Start for free pill. Prompt chips sit under the hero and fill a prompt. That prompt was not submitted.

## Pricing and contact

Pricing is a long dark page of plan cards. Contact is the demo request page. Neither form was submitted.

See [pricing-dark-default](screenshots/pricing-dark-default.png) and [contact-dark-default](screenshots/contact-dark-default.png).

## Auth boundary

Log in and Start for free leave the marketing host. The dashboard shows an email and password wall, or Google. That is the end of the public tree. The marketing `/login` path is a 404 that still wears the marketing chrome.

See [notfound-dark-default](screenshots/notfound-dark-default.png) and [login-dark-wall](screenshots/login-dark-wall.png).
