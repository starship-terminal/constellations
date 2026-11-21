# IKEA Singapore site tree

Mapped from the public homepage `https://www.ikea.com/sg/en/` on 2026-11-21 in headless Chromium at 1440×900, before screenshots. Controls were opened and closed. No form was submitted. Country and store were not changed. Login and signup branches stop at the wall.

The storefront is the Inter IKEA public site for Singapore, English. One light theme. No dark theme switch on the public pages.

## Header (every page)

| Control | Opens |
|---|---|
| Skip to main content | In-page `#hnf-content` |
| Promo link ("365 days to change your mind" / "Get your items delivered from $10") | `/sg/en/customer-service/returns-claims/return-policy/` or `/sg/en/customer-service/services/delivery/` |
| `SG English` button (`aria-haspopup=dialog`) | Sheet dialog: "You're in the Singapore online store". Change country/region empties the cart. Closed without changing country. |
| Select store (`aria-haspopup=dialog`) | Dialog listing Alexandra, IKEA Jurong @ JEM, Tampines, plus a location search. Closed without selecting a store. Street text in that dialog is store-published; the package does not copy it. |
| IKEA logotype | `/sg/en/` |
| Products (`aria-expanded`, mega menu) | Dropdown, then `/sg/en/cat/products-products/` if followed |
| Rooms | Dropdown, then `/sg/en/rooms/` |
| Offers | Dropdown, then `/sg/en/offers/` |
| Ideas & guides | Dropdown, then `/sg/en/ideas/` |
| Services | Dropdown, then `/sg/en/customer-service/services/` |
| Search field `#ikea-search-input` | Suggestion panel (focus) and typed suggestions. Enter goes to `/sg/en/search/?q=` |
| Hej! Log in or sign up | `/sg/en/profile/` which asks for email and password. Known probe: `https://www.ikea.com/sg/en/profile/login/`. Branch stops. |
| Track order | `/sg/en/customer-service/track-manage-order/` (order lookup form; not submitted) |
| Shopping list | `/sg/en/favourites/` |
| Shopping cart | `/sg/en/cart/` |
| Menu (phone, `aria-label=Menu`) | Full-screen navigation drawer |

## Products menu

| Control | Opens |
|---|---|
| Discover what's NEW | `/sg/en/new/` |
| Coming soon to IKEA | `/sg/en/campaigns/discover-whats-coming-soon-to-ikea-singapore-pub7afdaa00/` |
| Join in-store activities | `/sg/en/stores/whats-happening-at-ikea-store-pub396226a0` |
| Discover IKEA Family | `/sg/en/ikea-family/` (member join is a wall; page itself is public) |
| New products | `/sg/en/new/new-products/?sort=NEWEST` |
| Seasonal collections | `/sg/en/rooms/ikea-collections-pub88817721/` |
| Top sellers | `/sg/en/cat/best-sellers/` |
| Swedish Restaurant | `/sg/en/stores/restaurant/` |
| Swedish Bistro | `/sg/en/stores/restaurant/swedish-bistro-pub3f432030/` |
| Swedish Food Market | `/sg/en/stores/restaurant/swedish-food-market-pubf2000510/` |
| Christmas campaign card | `/sg/en/campaigns/christmas/` |

Homepage category rail (same Products surface): Offers & promos, Storage & organisation (`/cat/storage-organisation-st001/`), Small storage, Sofas & armchairs (`/cat/sofas-armchairs-700640/`), Beds & mattresses, Baby & children, Tables & dining, Study & office, Kitchen cabinets, Kitchenware, Outdoor, Bathroom, Textiles, Curtains, Home decoration, Plants, Lighting, Home electronics, Laundry, Home improvement, Food & beverages, Christmas.

## Rooms menu

Living room, Bedroom, Kitchen, Dining room, Children's room, Home office, Study room, Bathroom, Storeroom, Garden & Balcony, Main entrance, Service yard. Each is `/sg/en/rooms/<slug>/`.

## Offers menu

Shop all offers (`/sg/en/offers/`), IKEA Family offers (`/sg/en/offers/family-offers/`), Our lowest prices (`/sg/en/cat/lowest-price/`), In-store multibuy deals, Everyday essentials under $5, Top sellers campaign, IKEA Family food offers, sustainability offers, NEW for IKEA Family members (`/sg/en/ikea-family/`).

## Ideas & guides menu

Ideas hub (`/sg/en/ideas/`), Home design service, IKEA in Real Homes, My First Home, heat guide, storage tips (`/sg/en/ideas/storage/`), storage campaign, kitchen storage how-to, child safety (`/sg/en/safety-at-home/child/`), sleep guide, cooking guide, sustainable products, more how-tos, one featured home story.

## Services menu

Explore all services, Delivery, Assembly, FAQ, Delivery tracking, Finance options, Home design service, Curtains installation, Furniture removal, Kitchen consultation, Spare parts, 365-day return, Guarantees, Shopping app, In-store planning, Room Space planner (addon-app), PAX / BESTÅ / BILLY planners (addon-app), All planning tools (`/sg/en/planners`), IKEA Stores, IKEA for Business, Gift cards, Home design campaign card.

## Homepage body

| Control | Opens |
|---|---|
| Explore the Christmas shop | `/sg/en/campaigns/christmas/` |
| Product cards | `/sg/en/p/<name>-<article>/` |
| Pause video / View transcript | In-page video controls and transcript |
| Load 6 more | Expands the inspiration list on the same page |
| Campaign and room story cards | Campaign, room, or ideas URLs already listed |

## Footer

Join IKEA Family (`/sg/en/ikea-family/`), IKEA for Business, Offers, New products, Planning tools, Stores, Restaurant menu, Shopping app, FAQ, Delivery, Return policy, Track order, Guarantees, Services, Feedback form (not submitted), Spare parts, About us, Kids' Club (external `family.ikea.com.sg`, not followed as a login), Sustainable everyday, Work with us, Newsroom, Product recalls, Secure it or Return it, Media resources, Disclaimer, social links (external, not captured), payment-method links back to finance options, Cookie settings (opens consent UI; not clicked, overlay hidden).

## Login wall (stop)

| Control | Opens | Stop |
|---|---|---|
| Hej! Log in or sign up | `/sg/en/profile/` then `/sg/en/profile/login/` | Email and password fields. Not typed. Not submitted. |
| Create account / sign up on that page | Signup form | Not filled. |
| Google or Apple | SSO | Not clicked. |

## Not opened

Country change, store selection, newsletter, cookie accept or reject, any purchase, any planner that asks for a plan, surveys, onboarding, birthday, and every external social host.

The cookie card is a shadow-root `section.banner.panel` injected by `www.ikea.com/sg/en/cookieconsent/`. It was hidden, not clicked. The store button on later pages already read "Store" from a site preference, so the store sheet was not opened and no address was captured.
