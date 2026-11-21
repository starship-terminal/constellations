# J.Crew public site tree

Mapped signed out on 2026-11-22 from [https://www.jcrew.com](https://www.jcrew.com). The browser landed on [https://www.jcrew.com/sg/?](https://www.jcrew.com/sg/?). Title "J.Crew: Clothes, Shoes & Accessories For Women, Men & Kids". Incognito preview, 1440 by 900 CSS pixels, `devicePixelRatio` 2. Visual viewport scale 1. Screenshots are 2880 by 1800. Prices read SGD. The page is a live shop, not a parked domain and not a captcha wall. Header background `rgb(255, 255, 255)`. Announcement bar background `rgb(0, 0, 0)`. Body type is soleil, 16px, color `rgb(0, 0, 0)`. Display type is Adobe Caslon Pro.

A Singapore shipping welcome mat covered the first paint. It named the country, said jcrew.com ships worldwide, and offered Start shopping plus a link to the U.S. site. Start shopping was clicked to dismiss it. The U.S. site control was not clicked. The mat also printed a public help email and a public phone number. That first screenshot was discarded because it printed the phone number.

Nothing was typed. No email, password, code, phone, or address was entered. No form was submitted. No identity provider was clicked. No captcha was solved. Add to Bag was not clicked. The bag link points at `/checkout/cart` and was not opened. The mailing list was not filled. Search was not submitted. `login-extracted` stays `not-started`.

`catalog.json` and `webapps-manifest.json` were left alone. origin/main had no `systems/jcrew/`. `systems/madewell` was not touched.

Tracking query strings are not recorded. Sign In is a button. It was not opened.

## Announcement bar

One black strip sits above the departments, 55px, type 14px, weight 500, white. It rotates one line. Previous and Next were not used to change the slide for the site map.

| Line | Copy | Opens |
|---|---|---|
| 1 | Have a question? We can help. Shop now | `/plp/womens/features/new-arrivals` (no `/sg` prefix). Listed, not opened |

## Header

Photographed: [home-light-1440.png](screenshots/home-light-1440.png).

The bar is white. Combined chrome is 116px: 55px announcement plus a 60px department row. The wordmark is an SVG, fill `#231f20`, rendered 114 by 24. Saved as [icons/mark.svg](icons/mark.svg).

| Control | Kind | Destination | This pass |
|---|---|---|---|
| Skip to Main Content | link | `#global__main` | not followed |
| J.Crew | link | [https://www.jcrew.com/sg/](https://www.jcrew.com/sg/) | home |
| Gifts | link | [https://www.jcrew.com/sg/feature/gifts](https://www.jcrew.com/sg/feature/gifts) | menu listed, page not opened. Label is red `rgb(208, 2, 27)` |
| New | link | [https://www.jcrew.com/sg/feature/new-arrivals](https://www.jcrew.com/sg/feature/new-arrivals) | menu listed, page not opened |
| Women | link | [https://www.jcrew.com/sg/womens](https://www.jcrew.com/sg/womens) | landing opened, then the clothing grid was photographed |
| Men | link | [https://www.jcrew.com/sg/mens](https://www.jcrew.com/sg/mens) | menu listed, page not opened |
| Kids | link | [https://www.jcrew.com/sg/kids](https://www.jcrew.com/sg/kids) | menu listed, page not opened |
| Cashmere | link | [https://www.jcrew.com/sg/feature/cashmere](https://www.jcrew.com/sg/feature/cashmere) | menu listed, page not opened |
| Petites | link | [https://www.jcrew.com/sg/plp/womens?fit=Petite](https://www.jcrew.com/sg/plp/womens?fit=Petite) | menu listed, page not opened |
| Sale | link | [https://www.jcrew.com/sg/sale](https://www.jcrew.com/sg/sale) | menu listed, page not opened |
| Search | field | overlay | not submitted. Placeholder "Search J.Crew" |
| Sign In | button | not opened | login wall, stopped |
| Bag | link | `/checkout/cart` | checkout wall, not opened. Aria label "Shopping bag; currently empty" |

Each department has a menu in the header DOM. Those panels were read, not photographed as separate pages. Image tiles inside the menus often have an empty accessible name. The text links are listed below. Query strings that only track a click (`intcmp`, `om_i`) are dropped. Size and filter queries that change the page are kept.

### Gifts

| Control | Destination |
|---|---|
| Gift guide | [https://www.jcrew.com/sg/shop/gift-guide](https://www.jcrew.com/sg/shop/gift-guide) |
| Women's gift guide | [https://www.jcrew.com/sg/shop/gift-guide/womens](https://www.jcrew.com/sg/shop/gift-guide/womens) |
| Men's gift guide | [https://www.jcrew.com/sg/shop/gift-guide/mens](https://www.jcrew.com/sg/shop/gift-guide/mens) |
| Girls' gift guide | [https://www.jcrew.com/sg/shop/gift-guide/girls](https://www.jcrew.com/sg/shop/gift-guide/girls) |
| Boys' gift guide | [https://www.jcrew.com/sg/shop/gift-guide/boys](https://www.jcrew.com/sg/shop/gift-guide/boys) |
| Gifts for her | [https://www.jcrew.com/sg/feature/gifts/gifts-for-her](https://www.jcrew.com/sg/feature/gifts/gifts-for-her) |
| Gifts for him | [https://www.jcrew.com/sg/feature/gifts/gifts-for-him](https://www.jcrew.com/sg/feature/gifts/gifts-for-him) |
| Gifts for kids | [https://www.jcrew.com/sg/feature/gifts/gifts-for-kids](https://www.jcrew.com/sg/feature/gifts/gifts-for-kids) |

### New

| Control | Destination |
|---|---|
| Women's new arrivals | [https://www.jcrew.com/sg/plp/womens/features/new-arrivals](https://www.jcrew.com/sg/plp/womens/features/new-arrivals) |
| Men's new arrivals | [https://www.jcrew.com/sg/plp/mens/features/new-arrivals](https://www.jcrew.com/sg/plp/mens/features/new-arrivals) |
| Girls' new arrivals | [https://www.jcrew.com/sg/plp/girls/features/new-arrivals](https://www.jcrew.com/sg/plp/girls/features/new-arrivals) |
| Boys' new arrivals | [https://www.jcrew.com/sg/plp/boys/features/new-arrivals](https://www.jcrew.com/sg/plp/boys/features/new-arrivals) |
| Party dressing, women | [https://www.jcrew.com/sg/shop/party-dressing/womens](https://www.jcrew.com/sg/shop/party-dressing/womens) |
| Sweater index | [https://www.jcrew.com/sg/feature/sweater-index](https://www.jcrew.com/sg/feature/sweater-index) |
| Family dressing | [https://www.jcrew.com/sg/shop/family-dressing](https://www.jcrew.com/sg/shop/family-dressing) |
| Women's icons | [https://www.jcrew.com/sg/feature/womens/the-jcrew-icons](https://www.jcrew.com/sg/feature/womens/the-jcrew-icons) |
| Women's Rollneck | [https://www.jcrew.com/sg/plp/womens/features/rollneck-collection](https://www.jcrew.com/sg/plp/womens/features/rollneck-collection) |
| Women's cold weather | [https://www.jcrew.com/sg/shop/cold-weather-accessories/womens](https://www.jcrew.com/sg/shop/cold-weather-accessories/womens) |
| Suiting swatchbook | [https://www.jcrew.com/sg/feature/the-suiting-swatchbook](https://www.jcrew.com/sg/feature/the-suiting-swatchbook) |
| Men's icons | [https://www.jcrew.com/sg/feature/mens/the-jcrew-icons](https://www.jcrew.com/sg/feature/mens/the-jcrew-icons) |
| Men's Rollneck | [https://www.jcrew.com/sg/plp/mens/features/rollneck-collection](https://www.jcrew.com/sg/plp/mens/features/rollneck-collection) |
| Men's cold weather | [https://www.jcrew.com/sg/shop/cold-weather-accessories/mens](https://www.jcrew.com/sg/shop/cold-weather-accessories/mens) |
| Family pajamas | [https://www.jcrew.com/sg/shop/family-pajamas](https://www.jcrew.com/sg/shop/family-pajamas) |
| American Girl | [https://www.jcrew.com/sg/feature/american-girl](https://www.jcrew.com/sg/feature/american-girl) |
| Dress-up shop | [https://www.jcrew.com/sg/plp/girls/features/dress-up-shop](https://www.jcrew.com/sg/plp/girls/features/dress-up-shop) |
| Kids icons | [https://www.jcrew.com/sg/feature/kids/the-jcrew-icons](https://www.jcrew.com/sg/feature/kids/the-jcrew-icons) |
| Resale | [https://www.jcrew.com/sg/feature/resale](https://www.jcrew.com/sg/feature/resale) |

### Women

| Control | Destination |
|---|---|
| Women | [https://www.jcrew.com/sg/womens](https://www.jcrew.com/sg/womens) |
| Best sellers | [https://www.jcrew.com/sg/plp/womens](https://www.jcrew.com/sg/plp/womens) |
| Top rated | [https://www.jcrew.com/sg/shop/top-rated/womens](https://www.jcrew.com/sg/shop/top-rated/womens) |
| Sale | [https://www.jcrew.com/sg/sale/women](https://www.jcrew.com/sg/sale/women) |
| All clothing | [https://www.jcrew.com/sg/plp/womens/categories/clothing](https://www.jcrew.com/sg/plp/womens/categories/clothing) |
| Sweaters | [https://www.jcrew.com/sg/plp/womens/categories/clothing/sweaters](https://www.jcrew.com/sg/plp/womens/categories/clothing/sweaters) |
| Pants | [https://www.jcrew.com/sg/plp/womens/categories/clothing/pants](https://www.jcrew.com/sg/plp/womens/categories/clothing/pants) |
| Jeans | [https://www.jcrew.com/sg/plp/womens/categories/clothing/jeans](https://www.jcrew.com/sg/plp/womens/categories/clothing/jeans) |
| Coats and jackets | [https://www.jcrew.com/sg/plp/womens/categories/clothing/coats-and-jackets](https://www.jcrew.com/sg/plp/womens/categories/clothing/coats-and-jackets) |
| Tees and tanks | [https://www.jcrew.com/sg/plp/womens/categories/clothing/tees-and-tanks](https://www.jcrew.com/sg/plp/womens/categories/clothing/tees-and-tanks) |
| Sweatshirts and sweatpants | [https://www.jcrew.com/sg/plp/womens/categories/clothing/sweatshirts-and-sweatpants](https://www.jcrew.com/sg/plp/womens/categories/clothing/sweatshirts-and-sweatpants) |
| Blazers | [https://www.jcrew.com/sg/plp/womens/categories/clothing/blazers](https://www.jcrew.com/sg/plp/womens/categories/clothing/blazers) |
| Skirts | [https://www.jcrew.com/sg/plp/womens/categories/clothing/skirts](https://www.jcrew.com/sg/plp/womens/categories/clothing/skirts) |
| Dresses and jumpsuits | [https://www.jcrew.com/sg/plp/womens/categories/clothing/dresses-and-jumpsuits](https://www.jcrew.com/sg/plp/womens/categories/clothing/dresses-and-jumpsuits) |
| Suiting | [https://www.jcrew.com/sg/plp/womens/categories/clothing/suiting](https://www.jcrew.com/sg/plp/womens/categories/clothing/suiting) |
| Shirts and tops | [https://www.jcrew.com/sg/plp/womens/categories/clothing/shirts-and-tops](https://www.jcrew.com/sg/plp/womens/categories/clothing/shirts-and-tops) |
| Matching sets | [https://www.jcrew.com/sg/plp/womens/categories/clothing/matching-sets](https://www.jcrew.com/sg/plp/womens/categories/clothing/matching-sets) |
| Pajamas and intimates | [https://www.jcrew.com/sg/plp/womens/categories/clothing/pajamas-and-intimates](https://www.jcrew.com/sg/plp/womens/categories/clothing/pajamas-and-intimates) |
| Shorts | [https://www.jcrew.com/sg/plp/womens/categories/clothing/shorts](https://www.jcrew.com/sg/plp/womens/categories/clothing/shorts) |
| Swim | [https://www.jcrew.com/sg/plp/womens/categories/clothing/swim](https://www.jcrew.com/sg/plp/womens/categories/clothing/swim) |
| All shoes | [https://www.jcrew.com/sg/all/womens/categories/shoes](https://www.jcrew.com/sg/all/womens/categories/shoes) |
| Boots | [https://www.jcrew.com/sg/plp/womens/categories/shoes/boots](https://www.jcrew.com/sg/plp/womens/categories/shoes/boots) |
| Slippers | [https://www.jcrew.com/sg/plp/womens/categories/shoes/slippers](https://www.jcrew.com/sg/plp/womens/categories/shoes/slippers) |
| Accessories | [https://www.jcrew.com/sg/plp/womens/categories/accessories](https://www.jcrew.com/sg/plp/womens/categories/accessories) |
| Scarves and gloves | [https://www.jcrew.com/sg/plp/womens/categories/accessories/scarves-and-gloves](https://www.jcrew.com/sg/plp/womens/categories/accessories/scarves-and-gloves) |
| Bags | [https://www.jcrew.com/sg/plp/womens/categories/accessories/bags](https://www.jcrew.com/sg/plp/womens/categories/accessories/bags) |
| Jewelry | [https://www.jcrew.com/sg/plp/womens/categories/accessories/jewelry](https://www.jcrew.com/sg/plp/womens/categories/accessories/jewelry) |
| Belts | [https://www.jcrew.com/sg/plp/womens/categories/accessories/belts](https://www.jcrew.com/sg/plp/womens/categories/accessories/belts) |
| Socks and tights | [https://www.jcrew.com/sg/plp/womens/categories/accessories/socks-and-tights](https://www.jcrew.com/sg/plp/womens/categories/accessories/socks-and-tights) |
| Hair | [https://www.jcrew.com/sg/plp/womens/categories/accessories/hair](https://www.jcrew.com/sg/plp/womens/categories/accessories/hair) |
| Personalization | [https://www.jcrew.com/sg/feature/personalization-shop](https://www.jcrew.com/sg/feature/personalization-shop) |

Shoe tiles also filter the all-shoes page by heels, ballets, loafers, sneakers, New Balance, Made in Italy, and Birkenstock. Those query strings stay on `/sg/all/womens/categories/shoes`.

### Men

| Control | Destination |
|---|---|
| Men | [https://www.jcrew.com/sg/mens](https://www.jcrew.com/sg/mens) |
| Best sellers | [https://www.jcrew.com/sg/plp/mens](https://www.jcrew.com/sg/plp/mens) |
| Top rated | [https://www.jcrew.com/sg/shop/top-rated/mens](https://www.jcrew.com/sg/shop/top-rated/mens) |
| Wallace & Barnes | [https://www.jcrew.com/sg/plp/mens/features/wallace-and-barnes](https://www.jcrew.com/sg/plp/mens/features/wallace-and-barnes) |
| Sale | [https://www.jcrew.com/sg/sale/men](https://www.jcrew.com/sg/sale/men) |
| All clothing | [https://www.jcrew.com/sg/plp/mens/categories/clothing](https://www.jcrew.com/sg/plp/mens/categories/clothing) |
| Sweaters | [https://www.jcrew.com/sg/plp/mens/categories/clothing/sweaters](https://www.jcrew.com/sg/plp/mens/categories/clothing/sweaters) |
| Shirts | [https://www.jcrew.com/sg/plp/mens/categories/clothing/shirts](https://www.jcrew.com/sg/plp/mens/categories/clothing/shirts) |
| Dress shirts | [https://www.jcrew.com/sg/plp/mens/categories/clothing/dress-shirts](https://www.jcrew.com/sg/plp/mens/categories/clothing/dress-shirts) |
| T-shirts and polos | [https://www.jcrew.com/sg/plp/mens/categories/clothing/tshirts-and-polos](https://www.jcrew.com/sg/plp/mens/categories/clothing/tshirts-and-polos) |
| Pants and chinos | [https://www.jcrew.com/sg/plp/mens/categories/clothing/pants-and-chinos](https://www.jcrew.com/sg/plp/mens/categories/clothing/pants-and-chinos) |
| Jeans | [https://www.jcrew.com/sg/plp/mens/categories/clothing/jeans](https://www.jcrew.com/sg/plp/mens/categories/clothing/jeans) |
| Suits and tuxedos | [https://www.jcrew.com/sg/plp/mens/categories/clothing/suits-and-tuxedos](https://www.jcrew.com/sg/plp/mens/categories/clothing/suits-and-tuxedos) |
| Blazers | [https://www.jcrew.com/sg/plp/mens/categories/clothing/blazers](https://www.jcrew.com/sg/plp/mens/categories/clothing/blazers) |
| Coats and jackets | [https://www.jcrew.com/sg/plp/mens/categories/clothing/coats-and-jackets](https://www.jcrew.com/sg/plp/mens/categories/clothing/coats-and-jackets) |
| Sweatshirts and sweatpants | [https://www.jcrew.com/sg/plp/mens/categories/clothing/sweatshirts-and-sweatpants](https://www.jcrew.com/sg/plp/mens/categories/clothing/sweatshirts-and-sweatpants) |
| Pajamas and loungewear | [https://www.jcrew.com/sg/plp/mens/categories/clothing/pajamas-and-loungewear](https://www.jcrew.com/sg/plp/mens/categories/clothing/pajamas-and-loungewear) |
| Underwear and boxers | [https://www.jcrew.com/sg/plp/mens/categories/clothing/underwear-and-boxers](https://www.jcrew.com/sg/plp/mens/categories/clothing/underwear-and-boxers) |
| Shorts | [https://www.jcrew.com/sg/plp/mens/categories/clothing/shorts](https://www.jcrew.com/sg/plp/mens/categories/clothing/shorts) |
| Shoes | [https://www.jcrew.com/sg/plp/mens/categories/shoes](https://www.jcrew.com/sg/plp/mens/categories/shoes) |
| Boots | [https://www.jcrew.com/sg/plp/mens/categories/shoes/boots](https://www.jcrew.com/sg/plp/mens/categories/shoes/boots) |
| Accessories | [https://www.jcrew.com/sg/plp/mens/categories/accessories](https://www.jcrew.com/sg/plp/mens/categories/accessories) |
| Suiting accessories | [https://www.jcrew.com/sg/plp/mens/categories/accessories/suiting-accessories](https://www.jcrew.com/sg/plp/mens/categories/accessories/suiting-accessories) |
| Hats | [https://www.jcrew.com/sg/plp/mens/categories/accessories/hats](https://www.jcrew.com/sg/plp/mens/categories/accessories/hats) |
| Socks | [https://www.jcrew.com/sg/plp/mens/categories/accessories/socks](https://www.jcrew.com/sg/plp/mens/categories/accessories/socks) |
| Belts | [https://www.jcrew.com/sg/plp/mens/categories/accessories/belts](https://www.jcrew.com/sg/plp/mens/categories/accessories/belts) |
| Sunglasses | [https://www.jcrew.com/sg/plp/mens/categories/accessories/sunglasses](https://www.jcrew.com/sg/plp/mens/categories/accessories/sunglasses) |
| Bags and wallets | [https://www.jcrew.com/sg/plp/mens/categories/accessories/bags-and-wallets](https://www.jcrew.com/sg/plp/mens/categories/accessories/bags-and-wallets) |
| Watches and jewelry | [https://www.jcrew.com/sg/plp/mens/categories/accessories/watches-and-jewelry](https://www.jcrew.com/sg/plp/mens/categories/accessories/watches-and-jewelry) |
| Miles Davis x J.Crew | [https://www.jcrew.com/sg/plp/mens/features/brands-we-love](https://www.jcrew.com/sg/plp/mens/features/brands-we-love) |
| Party dressing | [https://www.jcrew.com/sg/shop/party-dressing/mens](https://www.jcrew.com/sg/shop/party-dressing/mens) |

### Kids

| Control | Destination |
|---|---|
| Kids | [https://www.jcrew.com/sg/kids](https://www.jcrew.com/sg/kids) |
| Girls' new arrivals | [https://www.jcrew.com/sg/plp/girls/features/new-arrivals](https://www.jcrew.com/sg/plp/girls/features/new-arrivals) |
| Boys' new arrivals | [https://www.jcrew.com/sg/plp/boys/features/new-arrivals](https://www.jcrew.com/sg/plp/boys/features/new-arrivals) |
| Girls' sale | [https://www.jcrew.com/sg/sale/girls](https://www.jcrew.com/sg/sale/girls) |
| Boys' sale | [https://www.jcrew.com/sg/sale/boys](https://www.jcrew.com/sg/sale/boys) |
| Shop all girls | [https://www.jcrew.com/sg/plp/girls](https://www.jcrew.com/sg/plp/girls) |
| Girls' clothing | [https://www.jcrew.com/sg/plp/girls/categories/clothing](https://www.jcrew.com/sg/plp/girls/categories/clothing) |
| Girls' tops | [https://www.jcrew.com/sg/plp/girls/categories/clothing/tops](https://www.jcrew.com/sg/plp/girls/categories/clothing/tops) |
| Girls' dresses | [https://www.jcrew.com/sg/plp/girls/categories/clothing/dresses](https://www.jcrew.com/sg/plp/girls/categories/clothing/dresses) |
| Girls' bottoms | [https://www.jcrew.com/sg/plp/girls/categories/clothing/bottoms](https://www.jcrew.com/sg/plp/girls/categories/clothing/bottoms) |
| Girls' coats | [https://www.jcrew.com/sg/plp/girls/categories/clothing/coats-and-jackets](https://www.jcrew.com/sg/plp/girls/categories/clothing/coats-and-jackets) |
| Girls' pajamas | [https://www.jcrew.com/sg/plp/girls/categories/clothing/pajamas-and-underwear](https://www.jcrew.com/sg/plp/girls/categories/clothing/pajamas-and-underwear) |
| Girls' active | [https://www.jcrew.com/sg/plp/girls/categories/clothing/active](https://www.jcrew.com/sg/plp/girls/categories/clothing/active) |
| Girls' swim | [https://www.jcrew.com/sg/plp/girls/categories/clothing/swim-and-rash-guards](https://www.jcrew.com/sg/plp/girls/categories/clothing/swim-and-rash-guards) |
| Girls' matching sets | [https://www.jcrew.com/sg/plp/girls/categories/clothing/matching-sets](https://www.jcrew.com/sg/plp/girls/categories/clothing/matching-sets) |
| Girls' baby | [https://www.jcrew.com/sg/plp/girls/categories/clothing/baby](https://www.jcrew.com/sg/plp/girls/categories/clothing/baby) |
| Girls' accessories | [https://www.jcrew.com/sg/plp/girls/categories/accessories](https://www.jcrew.com/sg/plp/girls/categories/accessories) |
| Girls' shoes | [https://www.jcrew.com/sg/plp/girls/categories/shoes](https://www.jcrew.com/sg/plp/girls/categories/shoes) |
| Shop all boys | [https://www.jcrew.com/sg/plp/boys](https://www.jcrew.com/sg/plp/boys) |
| Boys' clothing | [https://www.jcrew.com/sg/plp/boys/categories/clothing](https://www.jcrew.com/sg/plp/boys/categories/clothing) |
| Boys' tops | [https://www.jcrew.com/sg/plp/boys/categories/clothing/tops](https://www.jcrew.com/sg/plp/boys/categories/clothing/tops) |
| Boys' bottoms | [https://www.jcrew.com/sg/plp/boys/categories/clothing/bottoms](https://www.jcrew.com/sg/plp/boys/categories/clothing/bottoms) |
| Boys' suiting | [https://www.jcrew.com/sg/plp/boys/categories/clothing/suiting](https://www.jcrew.com/sg/plp/boys/categories/clothing/suiting) |
| Boys' coats | [https://www.jcrew.com/sg/plp/boys/categories/clothing/coats-and-jackets](https://www.jcrew.com/sg/plp/boys/categories/clothing/coats-and-jackets) |
| Boys' active | [https://www.jcrew.com/sg/plp/boys/categories/clothing/active](https://www.jcrew.com/sg/plp/boys/categories/clothing/active) |
| Boys' swim | [https://www.jcrew.com/sg/plp/boys/categories/clothing/swim-and-rash-guards](https://www.jcrew.com/sg/plp/boys/categories/clothing/swim-and-rash-guards) |
| Boys' matching sets | [https://www.jcrew.com/sg/plp/boys/categories/clothing/matching-sets](https://www.jcrew.com/sg/plp/boys/categories/clothing/matching-sets) |
| Boys' baby | [https://www.jcrew.com/sg/plp/boys/categories/clothing/baby](https://www.jcrew.com/sg/plp/boys/categories/clothing/baby) |
| Boys' accessories | [https://www.jcrew.com/sg/plp/boys/categories/accessories](https://www.jcrew.com/sg/plp/boys/categories/accessories) |
| Boys' shoes | [https://www.jcrew.com/sg/plp/boys/categories/shoes](https://www.jcrew.com/sg/plp/boys/categories/shoes) |
| American Girl x J.Crew | [https://www.jcrew.com/sg/feature/american-girl](https://www.jcrew.com/sg/feature/american-girl) |
| Matching family pajamas | [https://www.jcrew.com/sg/shop/family-pajamas](https://www.jcrew.com/sg/shop/family-pajamas) |
| Cozy shop | [https://www.jcrew.com/sg/plp/girls/features/cozy](https://www.jcrew.com/sg/plp/girls/features/cozy) |
| Dress-up shop | [https://www.jcrew.com/sg/plp/girls/features/dress-up-shop](https://www.jcrew.com/sg/plp/girls/features/dress-up-shop) |
| Kids icons | [https://www.jcrew.com/sg/feature/kids/the-jcrew-icons](https://www.jcrew.com/sg/feature/kids/the-jcrew-icons) |
| Mini-me shop | [https://www.jcrew.com/sg/shop/mommy-and-me](https://www.jcrew.com/sg/shop/mommy-and-me) |
| Tween girls | [https://www.jcrew.com/sg/plp/girls/features/tween](https://www.jcrew.com/sg/plp/girls/features/tween) |
| Tween boys | [https://www.jcrew.com/sg/plp/boys/features/tween](https://www.jcrew.com/sg/plp/boys/features/tween) |

Baby, girls (2-9), boys (2-9), and tween links also carry size filters. Those were read, not opened.

### Cashmere

| Control | Destination |
|---|---|
| Cashmere | [https://www.jcrew.com/sg/feature/cashmere](https://www.jcrew.com/sg/feature/cashmere) |
| Women's cashmere | [https://www.jcrew.com/sg/plp/womens/features/the-cashmere-shop](https://www.jcrew.com/sg/plp/womens/features/the-cashmere-shop) |
| Men's cashmere | [https://www.jcrew.com/sg/plp/mens/features/the-cashmere-shop](https://www.jcrew.com/sg/plp/mens/features/the-cashmere-shop) |
| Girls' cashmere | [https://www.jcrew.com/sg/plp/girls/features/the-cashmere-shop](https://www.jcrew.com/sg/plp/girls/features/the-cashmere-shop) |
| Boys' cashmere | [https://www.jcrew.com/sg/plp/boys/features/the-cashmere-shop](https://www.jcrew.com/sg/plp/boys/features/the-cashmere-shop) |
| Baby cashmere | [https://www.jcrew.com/sg/plp/baby/features/the-cashmere-shop](https://www.jcrew.com/sg/plp/baby/features/the-cashmere-shop) |
| Responsible cashmere | [https://www.jcrew.com/sg/feature/responsible-cashmere](https://www.jcrew.com/sg/feature/responsible-cashmere) |
| Cashmere care | [https://www.jcrew.com/sg/feature/cashmere-care](https://www.jcrew.com/sg/feature/cashmere-care) |

Weight filters (ultra-light, light, medium, heavy, brushed) stay on the women's cashmere shop URL.

### Petites

| Control | Destination |
|---|---|
| All petites | [https://www.jcrew.com/sg/plp/womens?fit=Petite](https://www.jcrew.com/sg/plp/womens?fit=Petite) |
| New arrivals | [https://www.jcrew.com/sg/plp/womens/features/new-arrivals?fit=Petite](https://www.jcrew.com/sg/plp/womens/features/new-arrivals?fit=Petite) |
| Jeans, pants, dresses, coats, shirts, skirts | same shop with `fit=Petite` and a sub-category |

### Sale

| Control | Destination |
|---|---|
| Sale | [https://www.jcrew.com/sg/sale](https://www.jcrew.com/sg/sale) |
| Women's sale | [https://www.jcrew.com/sg/sale/women](https://www.jcrew.com/sg/sale/women) |
| Men's sale | [https://www.jcrew.com/sg/sale/men](https://www.jcrew.com/sg/sale/men) |
| Girls' sale | [https://www.jcrew.com/sg/sale/girls](https://www.jcrew.com/sg/sale/girls) |
| Boys' sale | [https://www.jcrew.com/sg/sale/boys](https://www.jcrew.com/sg/sale/boys) |

## Pages opened

| Page | URL | Shot |
|---|---|---|
| Homepage | [https://www.jcrew.com/sg/](https://www.jcrew.com/sg/) | [home-light-1440.png](screenshots/home-light-1440.png) |
| Women's clothing | [https://www.jcrew.com/sg/plp/womens/categories/clothing](https://www.jcrew.com/sg/plp/womens/categories/clothing) | [collection-light-1440.png](screenshots/collection-light-1440.png) |
| Product | [https://www.jcrew.com/sg/p/womens/categories/clothing/sweaters/pullovers/CZ308](https://www.jcrew.com/sg/p/womens/categories/clothing/sweaters/pullovers/CZ308) | [product-light-1440.png](screenshots/product-light-1440.png) |
| Our Story | [https://www.jcrew.com/sg/s/aboutus](https://www.jcrew.com/sg/s/aboutus) | [about-light-1440.png](screenshots/about-light-1440.png) |

The women's landing at `/sg/womens` reused the homepage hero. The clothing grid is the category page. The product is "Mockneck sweater in argyle vintage wool", SGD 328. Add to Bag was not clicked.

## Footer

Footer background `rgb(240, 241, 242)`. Copyright "© 2026 J.Crew". Country control reads Singapore and points at [https://www.jcrew.com/sg/r/context-chooser](https://www.jcrew.com/sg/r/context-chooser). That chooser was not opened.

| Group | Control | Destination | This pass |
|---|---|---|---|
| Help | Email Us | modal | not opened |
| Help | Customer Service | [https://www.jcrew.com/sg/help/customer-service](https://www.jcrew.com/sg/help/customer-service) | listed |
| Help | Track Order | [https://www.jcrew.com/sg/help/order-status](https://www.jcrew.com/sg/help/order-status) | listed |
| Help | Returns & Exchanges | [https://www.jcrew.com/sg/help/returns-exchanges](https://www.jcrew.com/sg/help/returns-exchanges) | listed |
| Help | Shipping | [https://www.jcrew.com/sg/help/shipping-handling](https://www.jcrew.com/sg/help/shipping-handling) | listed |
| Help | International Orders & Returns | [https://www.jcrew.com/sg/help/international-orders](https://www.jcrew.com/sg/help/international-orders) | listed |
| Help | Contact Us | [https://www.jcrew.com/sg/help/contact-us](https://www.jcrew.com/sg/help/contact-us) | listed. Not opened, so no address was saved |
| Help | Policy on Fraudulent Activity | [https://www.jcrew.com/sg/company/jcrew-policy-on-fraudulent-activity](https://www.jcrew.com/sg/company/jcrew-policy-on-fraudulent-activity) | listed |
| Quick links | Offers & Promotions | [https://www.jcrew.com/sg/promo-codes-discounts-coupons](https://www.jcrew.com/sg/promo-codes-discounts-coupons) | listed |
| Quick links | My Favorites | [https://www.jcrew.com/sg/favorites](https://www.jcrew.com/sg/favorites) | not opened |
| About | Our Story | [https://www.jcrew.com/sg/s/aboutus](https://www.jcrew.com/sg/s/aboutus) | photographed |
| About | Careers | [https://jobs.jcrew.com/](https://jobs.jcrew.com/) | not opened |
| About | Impact at J.Crew Group | [https://www.jcrew.com/sg/s/corporate-responsibility](https://www.jcrew.com/sg/s/corporate-responsibility) | listed |
| About | California Transparency Act | [https://www.jcrew.com/sg/s/CSR-california-transparency-act](https://www.jcrew.com/sg/s/CSR-california-transparency-act) | listed |
| About | Investor Relations | [https://investors.jcrew.com/](https://investors.jcrew.com/) | not opened |
| Legal | Terms of Use | [https://www.jcrew.com/sg/help/terms-of-use](https://www.jcrew.com/sg/help/terms-of-use) | listed |
| Legal | Privacy Policy | [https://www.jcrew.com/sg/help/privacy-policy](https://www.jcrew.com/sg/help/privacy-policy) | listed |
| Legal | Responsible Disclosure Policy | [https://www.jcrew.com/sg/help/responsible-disclosure-policy](https://www.jcrew.com/sg/help/responsible-disclosure-policy) | listed |
| Legal | Belonging & Equity | [https://www.jcrew.com/sg/company/belonging](https://www.jcrew.com/sg/company/belonging) | listed |
| Legal | California Do Not Sell | button | not opened |
| Sister shops | Madewell | [https://www.madewell.com/](https://www.madewell.com/) | not opened |
| Sister shops | J.Crew Factory | [https://factory.jcrew.com/](https://factory.jcrew.com/) | not opened |
| Social | facebook, x, linkedin, pinterest, youtube, instagram | external profiles | not opened |
| Subscribe | SIGN UP | email form | not filled, not submitted |

## Where the walk stopped

Sign In was not opened. The bag was not opened. Add to Bag was not clicked. Search was not submitted. Email Us and SIGN UP were not submitted. The country chooser was not opened. The U.S. site control on the welcome mat was not clicked. Contact Us was not opened.
