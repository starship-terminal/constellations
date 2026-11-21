# Nike public site tree

Mapped from https://www.nike.com/ on 2026-11-21, signed out, before the screenshot pass. The request redirected to https://www.nike.com/sg/. The page title was "Nike. Just Do It. Nike SG". This is the live Singapore English storefront, not a parked domain and not a captcha wall.

There is no theme switch on the public storefront. The only region control is the footer button "Singapore" (`aria-label` "Selected location: Singapore"). It opens the dialog "Select your Location". That dialog was closed without choosing another country. No email was typed. No password was typed. No form was submitted. No identity provider was clicked. Nothing was added to the bag.

Sign In and Join Us both point at `/sg/register`. That page is the account wall and was not opened from the homepage mapping. Favourites (`/sg/favorites`) and Bag (`/sg/cart`) are header links. They were not followed during the map.

## Utility bar

Sits above the main nav.

| Control | Opens | Stop? |
|---|---|---|
| Jordan (swoosh, `aria-label` Jordan) | `/sg/jordan` | |
| Find a Store | `/sg/retail` | |
| Help | `/sg/help` | |
| Join Us | `/sg/membership` | |
| Sign In | `/sg/register` | yes, account wall |
| Skip to main content | `#skip-to-content` | |

## Header

The wordmark is a link labelled "Nike Homepage". Category labels are links. Each one except SNKRS has a sibling `details` flyout. SNKRS is a standalone link.

| Control | Opens | Stop? |
|---|---|---|
| Nike Homepage | `/sg/` | |
| New & Featured | Button. Opens a flyout on the same page. Does not navigate. | |
| Men | `/sg/men`. Sibling flyout does not navigate. | |
| Women | `/sg/women`. Sibling flyout does not navigate. | |
| Kids | `/sg/kids`. Sibling flyout does not navigate. | |
| NikeSKIMS | `/sg/nikeskims`. Sibling flyout does not navigate. | |
| Sale | `/sg/w/sale-3yaep`. Sibling flyout does not navigate. | |
| Gifts | `/sg/w/gifting-l2wr`. Sibling flyout does not navigate. | |
| SNKRS | `/sg/launch` | |
| Search (`aria-label` Search) | Search overlay on the same page. Does not navigate. | |
| Favourites (`aria-label` Favourites) | `/sg/favorites` | yes, account wall |
| Bag Items: 0 | `/sg/cart` | not followed |

## New & Featured flyout

The button opens a `details` panel. Column labels are Featured, Trending, Shop Icons, and Shop By Sport.

| Item | Opens |
|---|---|
| Upcoming Drops | `/sg/w/new-upcoming-drops-k0gk` |
| New Arrivals | `/sg/w/new-3n82y` |
| Bestsellers | `/sg/w/best-76m50` |
| SNKRS Launch Calendar | `/sg/launch` |
| Customise with Nike By You | `/sg/nike-by-you` |
| Jordan | `/sg/jordan` |
| Kobe Bryant | `/sg/w/kobe-pgd6` |
| LeBron James | `/sg/basketball/lebron-james` |
| Gift Sport | `/sg/w/gifting-l2wr` |
| Travel Essentials | `/sg/w/travel-collection-951k` |
| Sun-Ready Performance | `/sg/w/sunday-essentials-9w0kj` |
| Just Do the Work | `/sg/w/nike-training-gym-58jtoz7yfb` |
| More Colours, More Running | `/sg/w/running-shoes-1sytgz37v7jz7gee1z8nexhzy7ok` |
| What's Trending | `/sg/w/trending-now-5fpm9` |
| 24.7 Collection | `/sg/w/247-collection-asi8j` |
| Colours of the Season | `/sg/w/fresh-colors-a499l` |
| Retro Running | `/sg/w/retro-running-8kemk` |
| Running Shoe Finder | `/sg/running-shoe-finder` |
| Lifestyle | `/sg/sportswear` |
| Air Force 1 | `/sg/w/air-force-1-shoes-5sj3yzy7ok` |
| Air Jordan 1 | `/sg/w/jordan-1-shoes-aj85gzy7ok` |
| Air Max | `/sg/w/air-max-shoes-a6d8hzy7ok` |
| Dunk | `/sg/w/dunk-shoes-90aohzy7ok` |
| Cortez | `/sg/w/cortez-shoes-byfxzy7ok` |
| Blazer | `/sg/w/blazer-shoes-9gw3azy7ok` |
| Pegasus | `/sg/w/pegasus-shoes-8nexhzy7ok` |
| Vomero | `/sg/w/zoom-vomero-shoes-7gee1zy7ok` |
| Running | `/sg/running` |
| Basketball | `/sg/basketball` |
| Football | `/sg/football` |
| Golf | `/sg/w/golf-23q9w` |
| Tennis & Pickleball | `/sg/tennis` |
| Gym & Training | `/sg/training` |
| Yoga | `/sg/w/yoga-anrlj` |
| Skateboarding | `/sg/skateboarding` |
| Trail Running | `/sg/w/trail-running-75jcn` |
| ACG | `/sg/acg` |

## Men flyout

| Item | Opens |
|---|---|
| New Arrivals | `/sg/w/new-mens-3n82yznik1` |
| Bestsellers | `/sg/w/mens-best-76m50znik1` |
| ACG | `/sg/w/mens-acg-93bsdznik1` |
| Shop All Sale | `/sg/w/mens-sale-3yaepznik1` |
| Shoes / All Shoes | `/sg/w/mens-shoes-nik1zy7ok` |
| Lifestyle | `/sg/w/mens-lifestyle-shoes-13jrmznik1zy7ok` |
| Jordan | `/sg/w/mens-jordan-shoes-37eefznik1zy7ok` |
| Running | `/sg/w/mens-running-shoes-37v7jznik1zy7ok` |
| Football | `/sg/w/mens-football-shoes-1gdj0znik1zy7ok` |
| Basketball | `/sg/w/mens-basketball-shoes-3glsmznik1zy7ok` |
| Gym & Training | `/sg/w/mens-training-gym-shoes-58jtoznik1zy7ok` |
| Tennis | `/sg/w/mens-tennis-shoes-ed1qznik1zy7ok` |
| Skateboarding | `/sg/w/mens-skateboarding-shoes-8mfrfznik1zy7ok` |
| Sandals & Slides | `/sg/w/mens-sandals-slides-fl76znik1` |
| Nike By You | `/sg/w/mens-nike-by-you-shoes-6ealhznik1zy7ok` |
| Trail Running | `/sg/w/mens-acg-trail-running-shoes-75jcnz93bsdznik1zy7ok` |
| Clothing / All Clothing | `/sg/w/mens-clothing-6ymx6znik1` |
| Tops & T-Shirts | `/sg/w/mens-tops-t-shirts-9om13znik1` |
| Shorts | `/sg/w/mens-shorts-38fphznik1` |
| Pants & Leggings | `/sg/w/mens-trousers-tights-2kq19znik1` |
| Hoodies & Sweatshirts | `/sg/w/mens-hoodies-sweatshirts-6riveznik1` |
| Jackets & Gilets | `/sg/w/mens-jackets-gilets-50r7yznik1` |
| Jerseys & Kits | `/sg/w/mens-kits-jerseys-3a41eznik1` |
| Jordan (clothing) | `/sg/w/mens-jordan-clothing-37eefz6ymx6znik1` |
| ACG (clothing) | `/sg/w/mens-acg-clothing-6ymx6z93bsdznik1` |
| Running (sport) | `/sg/w/mens-running-37v7jznik1` |
| Basketball (sport) | `/sg/w/mens-basketball-3glsmznik1` |
| Football (sport) | `/sg/w/mens-football-1gdj0znik1` |
| Golf | `/sg/w/mens-golf-23q9wznik1` |
| Tennis & Pickleball | `/sg/w/mens-tennis-ed1qznik1` |
| Gym & Training (sport) | `/sg/w/mens-training-gym-58jtoznik1` |
| Yoga | `/sg/w/mens-yoga-anrljznik1` |
| Skateboarding (sport) | `/sg/w/mens-skateboarding-8mfrfznik1` |
| Trail Running (sport) | `/sg/w/mens-trail-running-75jcnznik1` |
| All Accessories & Equipment | `/sg/w/mens-accessories-equipment-awwpwznik1` |
| Bags & Backpacks | `/sg/w/mens-bags-backpacks-9xy71znik1` |
| Socks | `/sg/w/mens-socks-nik1zuwr3` |
| Hats & Headwear | `/sg/w/mens-hats-visors-headbands-31btsznik1` |

## Women flyout

Same column shape as Men, plus NikeSKIMS, Performance Essentials, Sports Bras, Skirts & Dresses, and Modest Wear.

| Item | Opens |
|---|---|
| New Arrivals | `/sg/w/new-womens-3n82yz5e1x6` |
| Bestsellers | `/sg/w/womens-best-5e1x6z76m50` |
| ACG | `/sg/w/womens-acg-5e1x6z93bsd` |
| Shop All Sale | `/sg/w/womens-sale-3yaepz5e1x6` |
| NikeSKIMS | `/sg/nikeskims` |
| All Shoes | `/sg/w/womens-shoes-5e1x6zy7ok` |
| All Clothing | `/sg/w/womens-clothing-5e1x6z6ymx6` |
| Performance Essentials | `/sg/w/womens-back-to-basics-5e1x6zkkjj` |
| Sports Bras | `/sg/w/womens-sports-bras-40qgmz5e1x6` |
| Modest Wear | `/sg/w/modest-wear-22fj5` |
| All Accessories & Equipment | `/sg/w/womens-accessories-equipment-5e1x6zawwpw` |

## Kids flyout

| Item | Opens |
|---|---|
| New Arrivals | `/sg/w/new-kids-3n82yzv4dh` |
| Bestsellers | `/sg/w/kids-best-76m50zv4dh` |
| Back to School | `/sg/w/back-to-school-840ik` |
| Lifestyle Looks | `/sg/w/kids-lifestyle-13jrmzv4dh` |
| Nike x LEGO | `/sg/lego` |
| ACG | `/sg/w/kids-acg-93bsdzv4dh` |
| Nike Teens | `/sg/teens` |
| All Shoes | `/sg/w/kids-shoes-v4dhzy7ok` |
| All Clothing | `/sg/w/kids-clothing-6ymx6zv4dh` |
| Older Kids (7 - 14 years) | `/sg/w/older-kids-agibjzv4dh` |
| Younger Kids (4 - 7 years) | `/sg/w/little-kids-6dacezv4dh` |
| Babies & Toddlers (0 - 4 years) | `/sg/w/baby-toddlers-kids-2j488zv4dh` |
| All Accessories & Equipment | `/sg/w/kids-accessories-equipment-awwpwzv4dh` |

## NikeSKIMS flyout

| Item | Opens |
|---|---|
| All | `/sg/w/nikeskims-b2asd` |
| Footwear | `/sg/w/nikeskims-shoes-b2asdzy7ok` |
| Bras | `/sg/w/nikeskims-sports-bras-40qgmzb2asd` |
| Tops and Tanks | `/sg/w/nikeskims-tops-t-shirts-9om13zb2asd` |
| Leggings | `/sg/w/nikeskims-tights-leggings-29sh2zb2asd` |
| Shorts | `/sg/w/nikeskims-shorts-38fphzb2asd` |
| Bottoms | `/sg/w/nikeskims-bottoms-5hnnkzb2asd` |
| Jackets | `/sg/w/nikeskims-jackets-gilets-50r7yzb2asd` |
| Accessories & Equipment | `/sg/w/nikeskims-accessories-equipment-awwpwzb2asd` |
| Sweatshirts | `/sg/w/nikeskims-fleece-tops-4blglzb2asd` |
| Online Exclusive | `/sg/w/online-exclusive-5rplf` |

Colour chips in the same flyout go to University Red, Collegiate Blue, Atmosphere Grey, and Citrine listing pages under `/sg/w/nikeskims-*`.

## Sale flyout

| Item | Opens |
|---|---|
| Shop All Sale | `/sg/w/sale-3yaep` |
| Last Chance | `/sg/w/sale-low-inventory-3yaepz52uxv` |
| Men's Sale | `/sg/w/mens-sale-3yaepznik1` |
| Women's Sale | `/sg/w/womens-sale-3yaepz5e1x6` |
| Kids' Sale | `/sg/w/kids-sale-3yaepzv4dh` |
| Football, Running, Basketball, Gym & Training, Tennis | `/sg/w/sale-<sport>-3yaep` |

Each gender column also lists Shoes, Clothing, and Accessories & Equipment.

## Gifts flyout

| Item | Opens |
|---|---|
| Shop All Gifts | `/sg/w/gifting-l2wr` |
| Gifts For Men | `/sg/w/mens-gifting-l2wrznik1` |
| Gifts For Women | `/sg/w/womens-gifting-5e1x6zl2wr` |
| Gifts For Kids | `/sg/w/kids-gifting-l2wrzv4dh` |
| Jordan Gifts | `/sg/w/gifting-jordan-37eefzl2wr` |
| Gifts By You | `/sg/w/gifting-nike-by-you-6ealhzl2wr` |
| Top Picks Under $50 | `/sg/w/gifting-xa-under-50-3k9h4zl2wr` |
| Top Picks $50 - $100 | `/sg/w/gifting-xa-50-100-bbjlzl2wr` |
| Top Picks $100 - $150 | `/sg/w/gifting-xa-100-150-2kq6ozl2wr` |
| Top Picks Over $150 | `/sg/w/gifting-xa-over-150-1gvmxzl2wr` |
| Clothing | `/sg/w/gifting-clothing-6ymx6zl2wr` |
| Footwear | `/sg/w/gifting-shoes-l2wrzy7ok` |
| Stocking Stuffers | `/sg/w/gifting-accessories-equipment-awwpwzl2wr` |

Sport rows (Sportswear, Running, Training, Football, Basketball, Golf, Tennis) sit in the same flyout.

## Search overlay

The Search button opens an overlay on `/sg/`. The field is `input[type=search]`, `aria-label` "Search Products", placeholder "Search". The field was left empty. Search was not submitted.

| Control | Opens | Stop? |
|---|---|---|
| Cancel | Closes the overlay | |
| Ask NikeAI | NikeAI panel on the same page | not submitted |
| Close Nike AI | Closes the NikeAI panel | |
| Popular Search Terms | Links such as `/sg/w?q=air%20force%201`. Not followed. | |

Popular terms on this visit: gift sport, pegasus plus 2, air force 1, vomero, acg, jordan, socks, pegasus.

## Home page

https://www.nike.com/sg/

Hero slides on this visit: NEVER MISS A DAY (Nike FIT System), NEW NIKESKIMS, ALPHAFLY 4, Greatness is Never Out of Reach (Jordan). Carousel controls stay on the page: Pause carousel autoplay, Previous, Next, Go to slide 1 of 4 through 4 of 4.

| Control | Opens |
|---|---|
| Shop (FIT System) | `/sg/w/perfect-fit-3rauvz5e1x6zae2h7znik1` |
| Explore (FIT System) | `/sg/fit-system` |
| Shop (NikeSKIMS) | `/sg/w/nikeskims-b2asd` |
| Explore (NikeSKIMS) | `/sg/nikeskims` |
| Shop (Alphafly 4) | `/sg/w/nike-alphafly-1tp17` |
| Shop (Jordan Space Jam) | `/sg/w/jordan-brand-x-space-jam-collection-9b8qk` |
| Preview on SNKRS | `/sg/launch/t/air-jordan-4-bred` |
| Join Now | `/sg/register` | 
| View Details | `/sg/help/a/shipping-delivery-gs` |

Join Now is the account wall. It was not followed during the map.

## Location dialog

The footer button "Singapore" opens `#modal-select-your-location`, heading "Select your Location". Regions are Africa, Americas, Asia Pacific, Europe, and Middle East. Country rows are links such as Singapore English (`/sg/`). No other country was chosen. Close pop-up closes the dialog.

## Footer

Resources, Help, and Company are link columns. Guides are legal links. Off-site company links were not entered.

| Item | Opens | Stop? |
|---|---|---|
| Find A Store | `/sg/retail` | |
| Become A Member | `/sg/register` | yes, account wall |
| Running Shoe Finder | `/sg/running/shoe-finder` | |
| Product Advice | `/sg/product-advice` | |
| Nike Coaching | `/sg/coaching` | |
| Magazine | about.nike.com | not entered |
| Education Discounts | `/sg/help/a/student-discount-gs` | |
| Send Us Feedback | `#site-feedback` | not submitted |
| Get Help | `/sg/help` | |
| Order Status | `/sg/orders` | yes, account wall |
| Delivery | `/sg/help/a/shipping-delivery-gs` | |
| Returns | `/sg/help/a/returns-policy-gs` | |
| Payment Options | `/sg/help/a/payment-options-gs` | |
| Contact Us | `/sg/help/#contact` | |
| About Nike, News, Careers, Investors, Impact, Report a Concern | Off-site Nike properties | not entered |
| Sustainability | `/sg/sustainability` | |
| Singapore | Location dialog, same page | |
| Terms of Sale | eshopworld.com terms page | not entered |
| Terms of Use | agreementservice.svs.nike.com | not entered |
| Nike Privacy Policy | agreementservice.svs.nike.com | not entered |
| Privacy Settings | `/sg/guest/settings/privacy` | not submitted |

## Login wall

`/sg/register` is the destination of Sign In, Join Us, Join Now, and Become A Member. It was not opened during the homepage map. The screenshot pass stops there. No email, password, or code is typed. Google, Apple, and any other identity provider are not clicked.
