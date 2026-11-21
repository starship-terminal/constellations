# Lulu and Georgia public site tree

Mapped from https://www.luluandgeorgia.com/ on 2026-11-21, signed out, before the screenshot pass. The homepage returned 200. The title was "Lulu and Georgia". This is a live Shopify furniture store, not a parked domain.

There is no theme switch. `color-scheme` on the root was `normal`. No email was typed. No password was typed. No phone number was typed. No address was typed. No form was submitted. No identity provider was clicked. Add to cart was not clicked. Checkout was not opened. `login-extracted` stays `not-started`.

The homepage URL gained a `?ffe=` query after load. That query is a campaign flag, not a session. Screenshots do not record it.

## Consent and overlays

A DataGrail banner (`.dg-consent-banner`) sits at the bottom of the page. A Klaviyo newsletter embed asks for an email and offers Subscribe. A Gladly chat bubble sits at the bottom right. A Swym wishlist consent popup exists in the DOM and was hidden.

| Control | What it does | Stop? |
|---|---|---|
| DataGrail banner | Cookie consent | Not clicked. Hidden in screenshots so it would not cover the page |
| Klaviyo Subscribe | Submits an email | Stop. Not typed, not submitted |
| Gladly chat | Opens a chat widget | Not opened. Hidden in screenshots |
| Swym consent | Wishlist consent dialog | Not clicked |

## Announcement bar

| Control | Opens | Stop? |
|---|---|---|
| EARLY ACCESS: BLACK FRIDAY SALE | `/collections/bestsellers` | |
| Close | Dismisses the bar | Not clicked |

## Header

The wordmark, search field, and four icon controls sit in the top row. A second row holds text links. A third row holds category links. Category links with a mega-menu use hover. The text links are pages, not flyouts.

| Control | Opens | Stop? |
|---|---|---|
| Lulu and Georgia (wordmark) | `/` | |
| Search field | Focuses the field. Submitting goes to `/search` | Focused empty. Not submitted from the header |
| Sign In | Account drawer on the same page | Drawer only. Sign In / Create Account was not followed |
| Showroom | `/pages/showroom` | |
| Wishlist | `#swym-wishlist` drawer | Not opened as a signed-in list |
| Bag | Empty bag drawer, also linked to `/cart` | Drawer only. Continue to Checkout was not clicked |
| Bestsellers | `/collections/bestsellers` | |
| Collaborations | `/collections/designer-collections` | |
| Inspiration | `/pages/shop-by-room` | |
| Trade Program | `/pages/trade` | |
| Contract Program | `/pages/contract` | |
| Complimentary Design Services | `/pages/design-services` | |
| Registry | `/pages/registry` | |

## Category row

Hover opens a mega-menu. The link itself opens the collection. The furniture menu was opened and closed. Apply inside a filter drawer was not pressed.

| Control | Opens | Mega-menu? |
|---|---|---|
| NEW | `/collections/new` | Yes |
| HOLIDAY | `/collections/holiday` | Yes |
| FURNITURE | `/collections/furniture` | Yes. Living room, bedroom, dining, outdoor, office |
| RUGS | `/collections/rugs` | Yes |
| LIGHTING | `/collections/lighting` | Yes |
| DÉCOR + TABLETOP | `/collections/decor` | Yes |
| WALLS | `/collections/walls` | Yes |
| PILLOWS + THROWS | `/collections/pillows-throws` | Yes |
| BED + BATH | `/collections/bed-bath` | Yes |
| OUTDOOR | `/collections/outdoor` | Yes |
| SALE | `/collections/sale` | Yes. Sale is the red link |

## Account drawer

Opened from the header Sign In icon. It is a local drawer, not the Shop wall.

| Control | Opens | Stop? |
|---|---|---|
| Sign In / Create Account | `/account/login`, which redirects to a Shop sign-in on shopify.com | Stop. Empty wall only |
| Trade Login | A Shopify customer-account URL | Stop. Not opened |
| Showroom | `/pages/showroom` | |
| My Registry | `/pages/registry` | |
| My Wishlist | `/#swym-list` | |
| Close | Closes the drawer | |

## Bag drawer

| Control | Opens | Stop? |
|---|---|---|
| Close | Closes the drawer | |
| Keep shopping | Closes the empty drawer | |
| View Bag | `/cart` | Not followed into checkout |
| Continue to Checkout | Checkout | Stop. Not clicked |

The empty state reads "Your bag is empty."

## Mobile drawer

At 390 wide the category row collapses. The hamburger opens a drawer. Each category row has a chevron for a nested list. The nested list was not expanded.

| Control | Opens | Stop? |
|---|---|---|
| Open menu | Drawer with NEW, HOLIDAY, FURNITURE, RUGS, LIGHTING, DÉCOR + TABLETOP, WALLS, PILLOWS + THROWS, BED + BATH, OUTDOOR, SALE, then Bestsellers | |
| Category chevron | Nested links for that category | Not expanded |
| Account icon | Account drawer | |
| Bag icon | Bag drawer | |

## Homepage sections

| Control | Opens | Stop? |
|---|---|---|
| Shop the sale | Sale collection | |
| Shop this bedroom, Shop this living room, Shop this dining room | Room collections | |
| Shop all looks | Looks collection | |
| Product cards | `/products/<slug>` | One product page was opened. Add to cart was not clicked |

## Collection page

`/collections/furniture` is a public category page. Chips (Bedroom, Beds, Sofas, In-Stock) filter in place. All filters opens a left drawer.

| Control | Opens | Stop? |
|---|---|---|
| Chip | Refines the grid | Not applied as a submitted filter |
| All filters | Filter drawer: product type, collection, color, material, width, price, height, features | Opened. Apply was not pressed. Clear filters was not pressed |
| Sort (Relevance) | Sort menu | Not changed |
| Product card | Product page | |

## Product page

`/products/sachs-dining-table` is public.

| Control | Opens | Stop? |
|---|---|---|
| Add to cart | Would add the table | Stop. Not clicked |
| Quantity minus and plus | Changes the quantity field | Not used |
| Wishlist heart | Wishlist | Not clicked |
| Order swatch | Swatch request | Not clicked |
| Add to registry | Registry | Stop |
| Save with our Trade Program | Trade page | |
| Get design help | Design services | |
| Shipping and returns | Expands a details block on the same page | Opened |
| Visit us | Showroom | |

## Search

`/search?q=rug&type=product` returns a public product grid. A nonsense query still returned suggested products, so the site has no empty search results page on this visit. The header field was focused and left empty.

## Footer

The footer is a public link list. Headless Chromium collapsed `.site-footer` to 0px until display was set on the element. The links were read from the live DOM and from that shot.

| Group | Items |
|---|---|
| Programs strip | Trade Program, Contract Program, Design Services, Showroom, Registry |
| Customer Support | FAQs (`/pages/top-questions`), Help Center (Zendesk), Shipping & Returns, Start a Return (`/apps/returns`), Catalog Unsubscribe |
| The Company | Careers, About Us, Sustainability, Accessibility Statement, Influencer Program |
| Ways to Shop | Complimentary Design Services, Trade Program, Contract Program, Showroom, View Online Catalogs, Registry, Current Offers, Gift Cards |
| Social | Instagram, TikTok, Facebook, Pinterest. Off-site. Not opened |
| Legal | Privacy Policy, Terms and Conditions, Site Index (`/collections`), Do Not Sell or Share My Information (`https://privacy.luluandgeorgia.com`) |

Start a Return and the privacy opt-out were not opened. Gift cards is a product page and was not entered as a purchase.

## Login and signup walls

`/account/login` and `/account/register` both redirect to the same Shop sign-in on shopify.com. The page title is "Sign in - Lulu and Georgia". The form is empty except for a pre-checked "Email me with news and offers" box. That box was not toggled.

| Control | What it does | Stop? |
|---|---|---|
| Continue with shop | Identity provider | Stop. Not clicked |
| Email field | Empty | Not typed |
| Email submit arrow | Would submit the email | Stop. Not clicked |
| Terms of service, Privacy policy | Legal buttons on the Shop page | Not opened |

There is no separate signup form. Create account is the same wall.
