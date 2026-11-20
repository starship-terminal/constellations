# Elektron patterns

How the measured components combine on elektron.se's public surface, read
from the screenshots and the component entries in [components.md](components.md).
The site paints one dark theme; all values are from the dark set unless noted.

## The shell

A 56px transparent header over the `#151515` page
([home-dark-default](screenshots/home-dark-default.png)): text links
Catalog / Shop / Kulture left with small icons, the Elektron wordmark
centre, Support / Account / Cart right — all 14px Neue Haas Grotesk Text
at 400 in `#eeeef2` ([nav-link](components/crops/nav-link-default.png),
[header](components/crops/header-default.png)). At 390px the bar is 63px
with a 35px burger that expands the header into a fullscreen menu — a
2px-bordered search row, then 24px Display links
([m-menu-open](components/crops/m-menu-open-opened.png),
[mobile-home-dark-menu](screenshots/mobile-home-dark-menu.png)). Two
drawers hang off the header: Search drops a full-width 40.5px field in
Analog One V2 ([search-field](components/crops/search-field-default.png),
[home-dark-search](screenshots/home-dark-search.png)); Account slides a
420px `#212121` right panel over a 50% scrim with the magic-login card
([account-modal](components/crops/account-modal-opened.png),
[home-dark-account](screenshots/home-dark-account.png)).

## The outline action

The one button recipe repeats on every route: a 46px block-button with a
2px `#eeeef2` stroke, transparent fill and a digi one v2 14px caps label —
transparent -> paper on hover and pressed, the label flipping paper ->
`#151515` ([pdp-explore](components/crops/pdp-explore-default.png) vs
[pdp-explore-hover](components/crops/pdp-explore-hover.png),
[add-to-cart](components/crops/add-to-cart-default.png),
[submit-button](components/crops/submit-button-default.png),
[cart-continue](components/crops/cart-continue-default.png)). The quiet
variant is the 42px `#cccccc` secondary fill with a `#151515` label that
inverts to `#151515`/`#cccccc` on hover ([magic-send](components/crops/magic-send-default.png),
[login-create](components/crops/login-create-default.png)). Corners are
square everywhere; keyboard focus wraps any of them in the double ring —
2px white spread + 2px black outline
([submit-button-focus-visible](components/crops/submit-button-focus-visible.png)).

## The underline-sweep

Text links carry no `text-decoration`: each paints a
`linear-gradient(#333333,#333333)` layer under its text, grown from zero
width on hover by a 0.4s `background-size` ease — the site's signature
micro-motion, on nav labels, footer links, explore rows and accordion
heads ([nav-link](components/crops/nav-link-hover.png),
[footer-link](components/crops/footer-link-hover.png),
[explore-link](components/crops/explore-link-hover.png)).

## Shop and product

/shop is a single column of product rows on the ground: an 18px Neue Haas
Text name, a 14px one-line descriptor and the price in $
([product-card](components/crops/product-card-default.png),
[shop-dark-default](screenshots/shop-dark-default.png)). The product page
keeps the same 18px name + price block, adds a 24px Display "Key
Features" accordion row ([accordion](components/crops/accordion-opened.png),
[product-digitakt-dark-features](screenshots/product-digitakt-dark-features.png))
and stacks the outline actions full-width ([product-digitakt-dark-full](screenshots/product-digitakt-dark-full.png)).
Page titles are 64px Display at 500 with a hanging bullet indent
([support-title](components/crops/support-title-default.png)); the
/explore index drops to 44.4px Display rows
([explore-title](components/crops/explore-title-default.png),
[explore-dark-full](screenshots/explore-dark-full.png)).

## Forms and drawers

Forms are light slabs on the dark ground: 42px `#eeeef2` block-inputs
with `#151515` text and `#757575` placeholders — text, select and the
126px textarea share the recipe
([text-field](components/crops/text-field-default.png),
[select-field](components/crops/select-field-default.png),
[textarea-field](components/crops/textarea-field-default.png)). Inside
the drawers the same fields invert: `#eeeef2` at rest, `#151515` on
focus ([magic-email](components/crops/magic-email-default.png) vs
[magic-email-focused](components/crops/magic-email-focused.png)). The
cart is an empty right drawer over the page — "Your cart is empty." plus
the outline CONTINUE SHOPPING
([cart-drawer](components/crops/cart-drawer-default.png),
[cart-dark-default](screenshots/cart-dark-default.png)) — and /my-account
shows the same magic-login card as the header drawer, signed out
([my-account-dark-default](screenshots/my-account-dark-default.png)).

## Footer

A closing block over the same ground: the 213px wordmark, four columns of
24px Display links at 450 ([footer-link](components/crops/footer-link-default.png)),
18px social glyphs ([social-icon](components/crops/social-icon-default.png))
and the legal row — the footer layer reads `#151515` at 10% over the page
([footer](components/crops/footer-default.png),
[home-dark-full](screenshots/home-dark-full.png)).
