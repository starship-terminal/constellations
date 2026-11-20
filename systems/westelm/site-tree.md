# West Elm site tree

Mapped from the public homepage at https://www.westelm.com/ on 2026-11-21, desktop viewport 1440x900, headed Chrome (Playwright `channel: chrome`). Headless Chromium received HTTP 403 on every URL. The email-signup dialog (`#join-email-campaign`) was removed from the DOM so it would not intercept the nav. It was not submitted.

Williams-Sonoma Akamai returned HTTP 403 ("West Elm: 403 - Restricted Access") for `/shop/*`, `/pages/*`, `/products/*`, `/favorites/`, and `/shoppingcart/`, including clicks that started on the loaded homepage. Those branches are recorded as blocked. Login and account URLs loaded. No email was typed and no form was submitted.

## Shell

The desktop header is four rows.

| Control | Opens |
|---|---|
| Brand strip (west elm, west elm office, west elm kids, west elm business to business, and sibling Williams-Sonoma brands) | Sibling brand homepages, or a West Elm path. Office, kids, and business paths 403'd in this session. |
| Utility row: ACCOUNT | Account menu (links below). The ACCOUNT link itself goes to `/account/`, which loaded as the signed-out account page. |
| Utility row: TRACK ORDER | `/customer-service/order-shipment-tracking/` (loaded). The page also shows a sign-in form. Not submitted. |
| Utility row: MY STORE | Store flyout ("Select a Store" search). STORE LOCATOR goes to `/stores/` (loaded). |
| Utility row: FAVORITES | `/favorites/` (403 in this session). |
| Utility row: CART | `/shoppingcart/` (403 in this session). |
| Search icon | Search field (`input[name=words]`, placeholder Search). A query was not submitted. |
| Secondary row | Hover menus listed below. Collaborations was in the row's text but had no visible hit target at 1440. |
| Primary row | Hover menus listed below. The category link itself navigates to `/shop/<category>/`, which 403'd. |
| Email signup dialog | Opens on load. Buttons: SIGN UP NOW (submits email; not used), NO THANKS, close. Removed so the nav could be read. |
| Footer columns | Links listed below. Credit-card manage and pay-bill links leave the site for a bank sign-in. Not followed. |

Phone width uses the same header with a Navigation button (`aria-label="show site navigation"`) that opens the mobile drawer. The drawer contains the same primary categories. It was not opened as a separate capture pass beyond the 390 viewport shots of pages that loaded.

## Stopped branches

| Control | URL | Why the branch stopped |
|---|---|---|
| ACCOUNT, Sign In / Create Account | `/account/` and `/account/login.html` | Loaded. Login asks for an email, then CONTINUE WITH EMAIL. No email typed, no form submitted. |
| B2B Member Sign In | `/account/login.html` | Same login page. Stopped. |
| Continue with Apple | on the login page | Not clicked. |
| Favorites, Design Boards, My Design Projects, View My Rewards | `/favorites/`, `/my-boards/`, `/my-design-projects/`, `/account/keyrewards.html` | Account or signed-in surfaces. Not entered past the login wall where a URL loaded as login. |
| CART | `/shoppingcart/` | 403. |
| Every primary-nav category page and every `/shop/` and `/pages/` flyout link | `/shop/…`, `/pages/…`, `/products/…` | 403, including in-page clicks from the homepage. |
| Newsletter email and mobile fields | homepage dialog and footer | Not filled. Not submitted. |
| Store search "Enter a location" | `/stores/` | Field is present. No location typed. |
| Track-order email, password, order number, postal code | `/customer-service/order-shipment-tracking/` | Form present. Not filled. Not submitted. |
| Registry create, find, manage | `/registry/` | Marketing page loaded. Create and manage lead into account flows. Not submitted. |

## Reachable pages

| Page | URL | Status |
|---|---|---|
| Home | `/` | 200 |
| Store locator | `/stores/` | 200 |
| Customer service | `/customer-service/` | 200 |
| Track your order | `/customer-service/order-shipment-tracking/` | 200, contains a sign-in form (not submitted) |
| Privacy policy | `/customer-service/privacy-policy/` | 200 |
| Login | `/account/login.html` | 200, email field only, not submitted |
| Account landing | `/account/` | 200, signed-out account chrome |
| Registry marketing | `/registry/` | 200 |
| Appointments | `/appointments/virtual-choice/` | 200, thin page |
| Mobile home | `/m/` | 200, same winter-edit home |

## Primary nav (hover opens a menu; the label link navigates, and those `/shop/` URLs 403'd)
### NEW

Label link: `/shop/new/`

| Item | Path |
|---|---|
| CHRISTMAS | `/shop/holidays/christmas/` |
| The Lookbook | `/pages/features/holiday-lookbook-2026/` |
| The Products | `/shop/new/winter-collection/` |
| PIERCE & WARD | `/shop/collaborations/pierce-and-ward/` |
| LONE FOX | `/shop/collaborations/lone-fox/` |
| All New | `/shop/new/all-new/` |
| New Furniture | `/shop/new/new-furniture/` |
| New Lighting | `/shop/new/new-lighting/` |
| New Rugs | `/shop/new/new-rugs/` |
| New Bedding | `/shop/new/new-bedding/` |
| New Pillows & Throws | `/shop/new/new-pillows-throws/` |
| New Art & Mirrors | `/shop/new/new-wall-decor-mirrors/` |
| … 16 more links in the same menu | |
### FURNITURE

Label link: `/shop/furniture/`

| Item | Path |
|---|---|
| LIVING ROOM | `/shop/furniture/all-living-room/` |
| Sofa & Sectional Collections | `/shop/furniture/sofa-sectional-collections/` |
| Chairs | `/shop/furniture/living-room-chairs/` |
| Sectionals | `/shop/furniture/sectionals/` |
| Sofas & Loveseats | `/shop/furniture/sofas/` |
| Sleeper Sofas & Sectionals | `/shop/furniture/sleeper-sofas/` |
| Ottomans & Stools | `/shop/furniture/ottomans/` |
| Coffee Tables | `/shop/furniture/coffee-tables/` |
| End & Side Tables | `/shop/furniture/end-side-tables/` |
| TV & Media Consoles | `/shop/furniture/consoles-media-storage-cabinets/` |
| Console & Sofa Tables | `/shop/furniture/console-tables/` |
| Bookcases | `/shop/furniture/living-room-bookcases/` |
| … 36 more links in the same menu | |
### OUTDOOR

Label link: `/shop/outdoor/`

| Item | Path |
|---|---|
| OUTDOOR COLLECTIONS | `/pages/features/outdoor-furniture-collections/` |
| Porto Collection | `/shop/outdoor/porto-outdoor-furniture/` |
| Telluride Collection | `/shop/outdoor/telluride-outdoor-furniture/` |
| Westport Collection | `/shop/outdoor/westport-outdoor-furniture/` |
| Monterey Collection | `/shop/outdoor/monterey-outdoor-furniture/` |
| Ventura Collection | `/shop/outdoor/ventura-outdoor-furniture/` |
| Mara Vista Collection | `/shop/outdoor/mara-vista-outdoor-furniture/` |
| Oceana Collection | `/shop/outdoor/oceana-outdoor-furniture/` |
| Baycrest Collection | `/shop/outdoor/baycrest-outdoor-furniture/` |
| Portside Collection | `/shop/outdoor/portside-outdoor-furniture/` |
| All Outdoor Furniture | `/shop/outdoor/all-outdoor-furniture/` |
| OUTDOOR LOUNGE FURNITURE | `/shop/outdoor/outdoor-lounge-furniture/` |
| … 36 more links in the same menu | |
### OFFICE

Label link: `/shop/west-elm-office/`

| Item | Path |
|---|---|
| EXPLORE WEST ELM OFFICE | `/shop/west-elm-office/` |
| OFFICE COLLECTIONS | `/pages/features/west-elm-office-collections/` |
| Hughes | `/shop/west-elm-office/west-elm-office-hughes/` |
| Marlowe | `/shop/west-elm-office/west-elm-office-marlowe/` |
| Tandem | `/shop/west-elm-office/west-elm-office-tandem/` |
| Wallace & Cutler | `/shop/west-elm-office/west-elm-office-cutler-wallace/` |
| Pierce | `/shop/west-elm-office/west-elm-office-pierce/` |
| Mid-Century | `/shop/west-elm-office/west-elm-office-mid-century/` |
| All Office Collections | `/pages/features/west-elm-office-collections/` |
| Desks | `/shop/west-elm-office/west-elm-office-desks/` |
| Desk Chairs | `/shop/west-elm-office/west-elm-office-desk-chairs/` |
| Bookcases & Shelving | `/shop/west-elm-office/west-elm-office-shelving/` |
| … 14 more links in the same menu | |
### RUGS

Label link: `/shop/rugs/`

| Item | Path |
|---|---|
| ALL RUGS | `/shop/rugs/all-rugs/` |
| Living Room | `/shop/rugs/living-room-rugs/` |
| Bedroom | `/shop/rugs/bedroom-rugs/` |
| Dining Room | `/shop/rugs/dining-room-rugs/` |
| Entryway & Kitchen | `/shop/rugs/entryway-rugs/` |
| Hallway Runners | `/shop/rugs/hallway-runners/` |
| Outdoor Rugs | `/shop/rugs/outdoor-rugs/` |
| Wool Rugs | `/shop/rugs/wool-rugs/` |
| Natural & Jute Rugs | `/shop/rugs/natural-fiber-rugs/` |
| TENCEL™ Lyocell Rugs | `/shop/rugs/tencel-rugs/` |
| Patterned Rugs | `/shop/rugs/pattern-rugs/` |
| Solid Rugs | `/shop/rugs/solid-color-rugs/` |
| … 25 more links in the same menu | |
### BEDDING

Label link: `/shop/bedding/`

| Item | Path |
|---|---|
| ALL BEDDING | `/shop/bedding/bedding-sets/` |
| Duvet Covers & Shams | `/shop/bedding/duvet-covers/` |
| Quilts | `/shop/bedding/quilts-blankets/` |
| Sheet Sets & Pillowcases | `/shop/bedding/sheet-sets/` |
| Comforters | `/shop/bedding/comforters/` |
| Blankets | `/shop/bedding/throws-blankets/` |
| Bedding Bundles | `/shop/bedding/bedding-bundles/` |
| All Bedding | `/shop/bedding/bedding-sets/` |
| TENCEL™: Silky Smooth | `/shop/bedding/tencel-bedding/` |
| Linen: Airy & Breathable | `/shop/bedding/linen-bedding/` |
| Cotton: Relaxed & Soft | `/shop/bedding/cotton-bedding/` |
| Percale: Smooth & Crisp | `/shop/bedding/percale-bedding/` |
| … 28 more links in the same menu | |
### BATH

Label link: `/shop/bath/`

| Item | Path |
|---|---|
| BATH LINENS | `/shop/bath/all-bath-linens/` |
| Towels | `/shop/bath/towels/` |
| Bath Mats | `/shop/bath/bath-mats/` |
| Shower Curtains | `/shop/bath/shower-curtains/` |
| Beach Towels | `/shop/bath/beach-towels/` |
| All Bath Linens | `/shop/bath/all-bath-linens/` |
| BATHROOM FURNITURE | `/shop/furniture/bath-furniture/` |
| Vanities | `/shop/bath/bathroom-vanities/` |
| Medicine Cabinets & Mirrors | `/shop/bath/vanity-mirrors/` |
| Bath Cabinets | `/shop/bath/bath-cabinets/` |
| Bath Furniture Collections | `/shop/bath/bath-furniture-collections/` |
| All Bathroom Furniture | `/shop/furniture/bath-furniture/` |
| … 19 more links in the same menu | |
### LIGHTING

Label link: `/shop/lighting/`

| Item | Path |
|---|---|
| CEILING LIGHTING | `/shop/lighting/all-ceiling-lighting/` |
| Chandeliers | `/shop/lighting/chandeliers/` |
| Pendants | `/shop/lighting/pendants/` |
| Flush Mounts | `/shop/lighting/flush-mounts/` |
| Ceiling Fans | `/shop/lighting/ceiling-fans/` |
| All Ceiling Lighting | `/shop/lighting/all-ceiling-lighting/` |
| LAMPS | `/shop/lighting/table-floor-lamps/` |
| Table & Desk Lamps | `/shop/lighting/table-lamps/` |
| Floor Lamps | `/shop/lighting/floor-lamps/` |
| All Lamps | `/shop/lighting/table-floor-lamps/` |
| SCONCES | `/shop/lighting/sconces/` |
| Bathroom & Vanity | `/shop/lighting/bathroom-lighting/` |
| … 11 more links in the same menu | |
### PILLOWS & DECOR

Label link: `/shop/accessories-pillows/`

| Item | Path |
|---|---|
| PILLOWS, THROWS & POUFS | `/shop/accessories-pillows/all-pillows-throws-poufs/` |
| Pillows | `/shop/accessories-pillows/pillows/` |
| Throws | `/shop/accessories-pillows/throw-blankets/` |
| Pillow Inserts | `/products/p502/` |
| Outdoor Pillows | `/shop/accessories-pillows/outdoor-pillows-cushions/` |
| Poufs & Floor Pillows | `/shop/accessories-pillows/floor-pillows/` |
| All Pillows, Throws & Poufs | `/shop/accessories-pillows/all-pillows-throws-poufs/` |
| ROOM DECOR | `/shop/accessories-pillows/room-decor-accessories/` |
| Vases | `/shop/accessories-pillows/vases-botanicals/` |
| Decorative Objects | `/shop/accessories-pillows/decorative-objects/` |
| Picture Frames | `/shop/wall-decor-mirrors/picture-frames/` |
| Decorative Trays & Bowls | `/shop/accessories-pillows/decorative-trays-bowls/` |
| … 27 more links in the same menu | |
### WINDOW

Label link: `/shop/windows/`

| Item | Path |
|---|---|
| CURTAINS | `/shop/windows/curtains-drapes/` |
| Solid Curtains | `/shop/windows/solid-curtains/` |
| Patterned Curtains | `/shop/windows/patterned-curtains/` |
| Outdoor Curtains | `/shop/windows/outdoor-curtains/` |
| Cafe Curtains & Rods | `/shop/windows/cafe-curtains/` |
| Custom Curtains | `/shop/windows/curtain+custom-window-treatments/producttype-m-product-type-ff000e151dfe20-1/` |
| All Curtains | `/shop/windows/curtains-drapes/` |
| Blackout Curtains | `/shop/windows/blackout-curtains/` |
| Sheer Curtains | `/shop/windows/sheer-curtains/` |
| CURTAIN RODS & HARDWARE | `/shop/windows/curtain-rods-hardware/` |
| WINDOW SHADES | `/shop/windows/shades-blinds/` |
| Linen | `/shop/windows/linen-curtains/` |
| … 12 more links in the same menu | |
### ART & MIRRORS

Label link: `/shop/wall-decor-mirrors/`

| Item | Path |
|---|---|
| MIRRORS | `/shop/wall-decor-mirrors/all-mirrors/` |
| Wall Mirrors | `/shop/wall-decor-mirrors/wall-mirrors/` |
| Floor Mirrors | `/shop/wall-decor-mirrors/floor-mirrors/` |
| Bathroom Mirrors | `/shop/bath/vanity-mirrors/` |
| All Mirrors | `/shop/wall-decor-mirrors/all-mirrors/` |
| ART | `/shop/wall-decor-mirrors/all-art-photography/` |
| Art Pairs & Sets | `/shop/wall-decor-mirrors/wall-art-sets/` |
| Paintings | `/shop/wall-decor-mirrors/paintings/` |
| Dimensional Art | `/shop/wall-decor-mirrors/dimensional-art/` |
| Photography | `/shop/wall-decor-mirrors/photography/` |
| All Art | `/shop/wall-decor-mirrors/all-art-photography/` |
| FRAMES | `/shop/wall-decor-mirrors/picture-frames/` |
| … 14 more links in the same menu | |
### KITCHEN & DINING

Label link: `/shop/dining-kitchen/`

| Item | Path |
|---|---|
| DINNERWARE & FLATWARE | `/shop/dining-kitchen/all-dining/` |
| Dinnerware Collections | `/shop/dining-kitchen/all-dinnerware-collections/` |
| Dinnerware Sets | `/shop/dining-kitchen/dinnerware-sets/` |
| Dinner Plates | `/shop/dining-kitchen/dinner-plates/` |
| Salad & Dessert Plates | `/shop/dining-kitchen/salad-dessert-plates/` |
| Bowls | `/shop/dining-kitchen/soup-cereal-bowls/` |
| Mugs | `/shop/dining-kitchen/mugs/` |
| Flatware | `/shop/dining-kitchen/flatware-sets/` |
| Outdoor Dinnerware | `/shop/dining-kitchen/all-outdoor-entertaining/` |
| All Dinnerware | `/shop/dining-kitchen/all-dining/` |
| DRINKWARE & BARWARE | `/shop/dining-kitchen/all-drinkware-barware/` |
| Glassware Collections | `/shop/dining-kitchen/all-glassware-collections/` |
| … 36 more links in the same menu | |
### STORAGE

Label link: `/shop/storage-organization/`

| Item | Path |
|---|---|
| STORAGE ACCESSORIES | `/shop/storage-organization/home-storage-solutions/` |
| Baskets & Bins | `/shop/storage-organization/storage-baskets-bins/` |
| Wall Hooks | `/shop/storage-organization/wall-hooks/` |
| Laundry Hampers | `/shop/storage-organization/laundry-room-storage/` |
| Jewelry Storage | `/shop/accessories-pillows/jewelry-box-storage/` |
| Trash Cans | `/shop/storage-organization/trash-cans/` |
| Pet Accessories | `/shop/storage-organization/dog-accessories/` |
| All Home Organization | `/shop/storage-organization/home-storage-solutions/` |
| Shelves & Display Ledges | `/shop/storage-organization/wall-shelves/` |
| Bookcases | `/shop/furniture/living-room-bookcases/` |
| Storage Cabinets | `/shop/furniture/cabinets/` |
| Bar & Kitchen Cabinets | `/shop/furniture/dining-room+kitchen+cabinets/shopbyroom-m-shop-by-room-ff00070b16181f27fe202020-2/` |
| … 15 more links in the same menu | |
### GIFTS

Label link: `/shop/gifts/`

| Item | Path |
|---|---|
| ALL GIFTS | `/shop/gifts/gift-ideas/` |
| Gifts $25 & Under | `/shop/gifts/gifts-25-under/` |
| Gifts $50 & Under | `/shop/gifts/gifts-50-under/` |
| Gifts $100 & Under | `/shop/gifts/gifts-100-under/` |
| Our Favorite Gifts | `/shop/gifts/top-gifts/` |
| The Monogram Shop | `/shop/gifts/monogram-gifts/` |
| Gift Sets | `/shop/gifts/gift-sets/` |
| Gifts For Her | `/shop/gifts/gifts-for-her/` |
| Gifts For Him | `/shop/gifts/gifts-for-him/` |
| Gifts For Me | `/shop/gifts/gifts-for-yourself/` |
| Gifts For The Host | `/shop/gifts/hostess-gifts/` |
| Gifts For Babies & Kids | `/shop/kids-gifts/all-baby-kids-gifts/` |
| … 19 more links in the same menu | |
### HOLIDAYS

Label link: `/shop/holidays/`

| Item | Path |
|---|---|
| CHRISTMAS DECORATING | `/shop/holidays/christmas/` |
| Ornaments & Tree Decor | `/shop/holidays/christmas-ornaments/` |
| Stockings & Stocking Holders | `/shop/holidays/christmas-stockings-decor/` |
| Decorative Accents | `/shop/holidays/all-holiday-decor/` |
| Wreaths & Garlands | `/shop/holidays/christmas-wreaths-garland-decor/` |
| Faux Christmas Trees | `/shop/holidays/artificial-christmas-trees/` |
| Candles & Candleholders | `/shop/holidays/holiday-candles-votives/` |
| String Lights & Lit Decor | `/shop/holidays/holiday-lights/` |
| Holiday Storage | `/shop/holidays/holiday-storage/` |
| Outdoor Christmas Decor | `/shop/holidays/outdoor-christmas-decor/` |
| All Christmas | `/shop/holidays/christmas/` |
| Holiday Pillows & Throws | `/shop/holidays/holiday-pillows-throws/` |
| … 16 more links in the same menu | |
### SALE

Label link: `/shop/sale/`

| Item | Path |
|---|---|
| Shop All Deals | `/shop/sale/all-sale/` |
| Furniture Up To 50% Off | `/shop/sale/sale-furniture/` |
| Outdoor Up To 50% Off | `/shop/sale/outdoor-garden-sale/` |
| Rugs Up To 50% Off | `/shop/sale/rugs-sale/` |
| Pillows & Throws Up To 40% Off | `/shop/sale/pillows-throws-sale/` |
| Kitchen & Dining Up To 30% Off | `/shop/sale/dining-kitchen-sale/` |
| Holiday Decor Up To 30% Off | `/shop/sale/holiday-sale/` |
| Up To 60% Off Sale & Clearance | `/shop/sale/clearance/` |
| All Sale | `/shop/sale/all-sale/` |
| Furniture | `/shop/sale/sale-furniture/` |
| Outdoor & Garden | `/shop/sale/outdoor-garden-sale/` |
| Rugs | `/shop/sale/rugs-sale/` |
| … 14 more links in the same menu | |
### BABY & KIDS

Label link: `/shop/west-elm-baby-kids/`

| Item | Path |
|---|---|
| EXPLORE BABY & KIDS | `/pages/baby-kids/` |
| NURSERY FURNITURE | `/shop/kids-furniture/all-baby-furniture/` |
| KIDS FURNITURE | `/shop/kids-furniture/all-kids-furniture/` |
| All New Arrivals | `/shop/kids-new/baby-kids-all-new/` |
| Christmas | `/shop/kids-holiday-gifts/kids-christmas/` |
| Hanukkah | `/shop/kids-holiday-gifts/kids-hanukkah/` |
| SHOP ALL NEW | `https://www.westelm.com/shop/kids-new/baby-kids-all-new/` |
| SHOP PETITE PLUME COLLAB | `https://www.westelm.com/shop/kids-collaborations/petite-plume/` |
## Secondary nav
### Room Inspiration

Label link: `https://www.westelm.com/pages/shop-by-room/living-rooms/`

| Item | Path |
|---|---|
| Living Room | `https://www.westelm.com/pages/shop-by-room/living-rooms/` |
| Bedroom | `https://www.westelm.com/pages/shop-by-room/bedrooms/` |
| Dining Room | `https://www.westelm.com/pages/shop-by-room/dining-rooms/` |
| Home Office | `https://www.westelm.com/pages/shop-by-room/home-offices/` |
| Outdoor | `https://www.westelm.com/pages/shop-by-room/outdoor-rooms/` |
| Bathroom | `https://www.westelm.com/pages/shop-by-room/bathrooms/` |
| Kitchen | `https://www.westelm.com/pages/shop-by-room/kitchen/` |
| Entryway | `https://www.westelm.com/pages/shop-by-room/entry/` |
| Bedding Looks | `https://www.westelm.com/shop/inspiration/bedding-looks/` |
| Pillow Pairings | `https://www.westelm.com/shop/inspiration/pillow-pairings/` |
| Table Inspiration | `https://www.westelm.com/shop/inspiration/table-settings/` |
| Pierce and Ward | `https://www.westelm.com/shop-by-style/pierce-ward/` |
| … 10 more links in the same menu | |
### Sustainability

Label link: `https://www.westelm.com/shop/collaborations/sustainably-sourced/`

| Item | Path |
|---|---|
| Sustainably Sourced | `https://www.westelm.com/shop/collaborations/sustainably-sourced/` |
| GREENGUARD | `https://www.westelm.com/shop/collaborations/greenguard-certified-furniture/` |
| Fair Trade | `https://www.westelm.com/shop/collaborations/fair-trade/` |
| St. Jude | `https://www.westelm.com/shop/collaborations/st-jude/` |
| No Kid Hungry | `https://www.westelm.com/shop/collaborations/no-kid-hungry/` |
| SHOP SUSTAINABLY | `https://www.westelm.com/shop/collaborations/sustainably-sourced/` |
### Free Design Services

Label link: `https://www.westelm.com/pages/style-and-service/`

| Item | Path |
|---|---|
| Appointments | `https://www.westelm.com/appointments/virtual-choice/` |
| Room Planner | `https://www.westelm.com/pages/ideas-and-advice/room-planner/` |
| Shop by Style | `https://www.westelm.com/shop-by-style/` |
| Design Boards | `https://www.westelm.com/my-boards/` |
| Request Swatches | `https://www.westelm.com/products/swatches/` |
| Measure for Delivery | `https://www.westelm.com/pages/ideas-and-advice/measure-for-delivery/` |
| INTRODUCING: DESIGN BOARDS | `https://www.westelm.com/my-boards/` |
### Registry

Label link: `https://www.westelm.com/registry/`

| Item | Path |
|---|---|
| Wedding Registry | `https://www.westelm.com/registry/` |
| Baby Registry | `https://www.westelm.com/registry/` |
| Find a Registry | `https://www.westelm.com/registry/find-registry.html` |
| Manage my Registry | `https://www.westelm.com/registry/manage-registry.html` |
| Dinnerware | `https://www.westelm.com/shop/dining-kitchen/dinnerware-sets/` |
| Drinkware & Barware | `https://www.westelm.com/shop/dining-kitchen/all-drinkware-barware/` |
| Flatware | `https://www.westelm.com/shop/dining-kitchen/flatware-sets/` |
| Bedding | `https://www.westelm.com/shop/bedding/bedding-sets/` |
| Bath | `https://www.westelm.com/shop/bath/all-bath-linens/` |
| Decor | `https://www.westelm.com/shop/accessories-pillows/room-decor-accessories/` |
| REGISTRY ESSENTIALS | `https://www.westelm.com/shop/inspiration/registry-essentials/` |
### Contract Grade

Label link: `https://www.westelm.com/pages/business-sales-programs/hospitality/`

| Item | Path |
|---|---|
| Sofas | `https://www.westelm.com/shop/business-contract-grade/sofa+contract-grade-seating/producttype-m-product-type-ff000b121afe20-1/` |
| Sectionals | `https://www.westelm.com/shop/business-contract-grade/sectional+contract-grade-seating/producttype-m-product-type-ff0010171ffe20-1/` |
| Chairs | `https://www.westelm.com/shop/business-contract-grade/chair+contract-grade-seating/producttype-m-product-type-ff000c131bfe20-1/` |
| Dining | `https://www.westelm.com/shop/business-contract-grade/contract-grade-dining-furniture/` |
| Benches & Banquettes | `https://www.westelm.com/shop/business-contract-grade/bench+banquette+contract-grade-dining-furniture/producttype-m-product-type-ff0005151c24fe20-2/` |
| Outdoor | `https://www.westelm.com/shop/business-contract-grade/commercial-outdoor-furniture/` |
| Bedroom | `https://www.westelm.com/shop/business-contract-grade/contract-grade-bedroom-furniture/` |
| Bedding | `https://www.westelm.com/shop/bedding/all-bedding/` |
| Lighting | `https://www.westelm.com/shop/business-contract-grade/commercial-lighting/` |
| Rugs | `https://www.westelm.com/shop/business-office-spaces/business-all-flooring/` |
| Office | `https://www.westelm.com/shop/business-contract-grade/contract-grade-office-media/` |
| Bath | `https://www.westelm.com/shop/business-contract-grade/contract-bath-furniture/` |
| … 2 more links in the same menu | |
## Account menu

| Item | Path |
|---|---|
| View My RewardsView your Key Rewards certificates | `/account/keyrewards.html` |
| Key RewardsEarn Rewards and enjoy exclusive benefits | `/pages/the-key-rewards/` |
| FavoritesSave your favorite items | `/favorites/` |
| RegistryCreate, find and manage registries | `/registry/` |
| STORE LOCATOR | `/stores/` |
| Design Boards | `/my-boards/` |
| West Elm Credit Card | `/pages/credit-card/` |
| Gift Cards | `/pages/gift-card-services/` |
| My Design Projects | `/my-design-projects/` |
| Customer Service | `/customer-service/` |
| Find A Store | `/stores/` |
| [+] Give Us Feedback | `` |

## Footer

| Item | Path |
|---|---|
| Contact Us | `/customer-service/email-us/` |
| Track Your Order | `/customer-service/order-shipment-tracking/` |
| Returns & Exchanges | `/customer-service/return/` |
| Help Topics | `/customer-service/faq.html` |
| Shipping Information | `/customer-service/shipping-info.html` |
| International Orders | `/customer-service/international-orders.html` |
| Safety Recalls | `/pages/safety-recalls/` |
| Email Preferences | `/customer-service/email-preferences/` |
| The Key Rewards | `/pages/the-key-rewards` |
| Apply For Credit Card | `/ccvalueprop/` |
| Manage Credit Card Account | `https://verified.capitalone.com/auth/signin` |
| Pay Bill Online | `https://verified.capitalone.com/auth/signin` |
| Monthly Payment Plan | `/pages/affirm-monthly-financing/` |
| Gift Cards | `/customer-service/gift-services/gift-card-landing.html` |
| Do Not Sell Or Share My Personal Information | `/customer-service/privacy-policy/#do-not-sell` |
| Sustainability | `/pages/about-west-elm/` |
| Responsible Retail Glossary | `/pages/about-west-elm/responsible-retail-glossary/` |
| Designers & Tastemakers | `/shop/collaborations/` |
| Careers | `/customer-service/employment.html` |
| Find A Store | `/stores/` |
| Meet With Design Crew | `/pages/style-and-service/` |
| Ideas & Advice | `/pages/ideas-and-advice/` |
| Room Planner | `/pages/ideas-and-advice/room-planner/` |
| Overview | `/pages/business/` |
| West Elm TRADE | `/pages/business/` |
| West Elm CONTRACT | `/pages/business-sales-programs/hospitality/` |
| West Elm WORK | `https://www.westelm.com/shop/business-office-spaces/` |
| Corporate Gifting | `/shop/business-office-spaces/corporate-gifts/` |
| Apple Store Download | `https://apps.apple.com/us/app/west-elm/id867468341` |
| Terms and Conditions | `/customer-service/terms.html` |
| Accessibility | `/customer-service/accessibility.html` |
| Privacy Policy | `/customer-service/privacy-policy/` |
| Terms & Conditions | `/about-us/terms.html` |
| Financial Incentive Terms | `/customer-service/privacy-policy/#financial-incentives` |
| Do Not Sell My Personal Information | `/about-us/privacy-policy.html#do-not-sell` |
| ACCESSIBILITY | `/about-us/accessibility.html` |
