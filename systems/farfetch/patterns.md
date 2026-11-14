# FARFETCH patterns

How the components in [components.md](components.md) combine on each captured surface. Everything below is the public, signed-out surface of farfetch.com painted in its single light theme; read exact values from [tokens.json](tokens.json). The DOM is archived Wayback SSR markup served locally (live farfetch.com answers Akamai 403 to automation), so everything hydration owns — dropdown panels, the size listbox, the filter drawer, accordion animation — stays closed.

## Chrome that wraps every page

- **TopBar (~80px, sticky, 1px `#e6e6e6` hairline):** department links (Womenswear · Menswear · Kidswear, 44px rows, the active one inked and underlined), the ~201px letterspaced FARFETCH wordmark, then the 44px square icon hit areas — language-and-region flag, account, wishlist, bag. On the phone the departments collapse into a dropdown trigger beside the wordmark.
- **NavBar (~44px):** the category links in `#727272` 13px label type — Clothing, Shoes, Bags, Jewelry, Accessories, Beauty — plus the one chromatic item, **Sale** in `#e71d34`, and the 270×44 search field at the right edge.
- **Footer:** uppercase FooterSectionTitle link columns (FARFETCH / Customer service / About FARFETCH …) in muted 13px type, the "Get updates by Email" newsletter field with the square `Sign Up` button, the ghost-dark social IconButtonGhostDark row, and the legal line with the locale summary.

## Home (department chooser)

`[screenshots/home-light-*]`

The country landing is a chooser, not a feed:

1. **"Choose a department"** — a centered page title over three full-bleed tiles (WOMENSWEAR / MENSWEAR / KIDSWEAR), each a campaign photograph with an uppercase Display overlay label; each tile is a department landing link.
2. **Category cards** — under the tiles, one row of four 330 x 484 cards per department (Womenswear: New in, Clothing, Bags, Shoes; Menswear: New in, Clothing, Accessories, Shoes; Kidswear: Boys, Girls, Baby boys, Baby girls), each an image with a Kicker heading and one link around the whole card.
3. **Newsletter and footer** — the archived home ends there: it paints no campaign modules or fashion-feed editorial cards (those appear on the listing pages), so none are described here.

## Product listing (modular PLP)

`[screenshots/plp-women-light-*, plp-men-light-*]`

`/shopping/{women,men}/items.aspx` is a modular storefront rather than a bare grid:

1. **Hero module** — a ~1392px content module: campaign image, DisplayLarge title, the 'Nimbus Roman D' Editorial dek and a `Shop Now` secondary button (white surface, `#222` stroke).
2. **"Brands of the moment"** — a premium-brands tile module (logo/photo tiles in a row).
3. **Product-card grid** — the 4-up grid at 1440 (`--page-max-width` 1440 minus 24px lateral spacers, ~336px cards): 3:4 image, ghost-dark wishlist heart on the photo, uppercase brand kicker, muted description, price; sale cards strike the original and add the `-40%` line in `#e71d34`. Skeleton bars paint where hydration would fill banners and recommendation rails.
4. **Editorial card rail** — mid-page editorial modules break the grid cadence.
5. Breadcrumbs, the filter toolbar and pagination are hydration-owned on these routes — they did not paint; the same components were measured on the classic edit page below.

## New-in edit (classic listing)

`[screenshots/set-women-light-*]` — the full page ran to 16,602 CSS px, split into two captures (part 0: 14,000px, part 1: the remainder; boundaries on the sidecars).

`/sets/women/new-in-this-week-eu-women.aspx` is the traditional listing shape:

- **Breadcrumb** — "Women · New In" BreadcrumbsNavigation in small muted type.
- **Page title block** — PageTitleHeading (the 22px Title) over the collapsible PageTitleDescription SEO copy.
- **Toolbar** — the `All Filters` button (outlined, 44px) and the quick-filter chip scroller; the chips are lazy-rendered, so the SSR paints the skeleton bar.
- **The grid** — the same 4-up product cards as the modular page, plus ProductCardSizes availability hints on hover cards and PriceOriginal/PriceSaleDiscount sale pricing.
- **Showcase carousels** — ProductShowcase rails with CarouselArrowSmall ghost-dark controls.
- **Pagination** — the Pagination row ("1 of 3" + next arrow) closes the grid.

## Product detail

`[screenshots/pdp-light-*]`

The Dolce & Gabbana slides PDP:

1. **Breadcrumbs** — Women · Dolce & Gabbana · Shoes · item.
2. **Gallery column** — the image carousel, ghost-dark arrows on the photography, thumbnail rail.
3. **Buy column** — the underlined uppercase brand link (LinkGhostDark), the 22px product title, the `$345` PriceCallout, the 44px `Select size` combobox (hydration-owned listbox, closed here), then the square `#222` **Add To Bag** (hover lifts the fill to `#727272`) beside the outlined **Wishlist** secondary with the heart.
4. **Information accordion** — "The Details", "Size & Fit", delivery/returns AccordionButton rows; the SSR ships them collapsed.
5. **Related showcases** — skeletonised ProductShowcase rails (the loading states the SSR ships).

## Mobile (390 wide)

`[screenshots/mobile-home-light-*, mobile-plp-women-light-*, mobile-pdp-light-*]`

The same pages at phone width: the TopBar collapses the department links into a dropdown trigger and keeps the icon row; the NavBar links scroll horizontally; the grid goes 2-up on cards; the PDP keeps its two columns side by side in the archived markup: a 199.5px gallery and a 142.5px sticky buy column with a 16px gap (`raw/layout.json`, `pdp@390`), so Add To Bag is an 84.5px-wide button inside that narrow column, not a full-width row. Whether the live site reflows the buy box under the gallery at 390 is not shown by this evidence and would need a live recapture. The hamburger menu itself is hydration-owned — the archived SSR paints the desktop chrome responsively.

## Shared conventions

- **One theme.** Everything paints light — white surfaces, `#222` ink, `#727272` secondary text, `#e6e6e6` hairlines, `#e71d34` only for sale. There is no dark hook.
- **Square controls.** Every button, field and card is a 0-radius square; the 1000px pill radius is reserved for chips/rounded controls.
- **Two voices.** 'Farfetch Basis' carries every UI string; 'Nimbus Roman D' appears only as the editorial serif in deks and campaign copy.
- **Skeletons are the loading idiom.** `#f5f5f5` ui-skeleton bars and cards stand in for anything hydration fills — banners, recommendations, quick filters.
- **Sticky chrome, hairline separation.** The TopBar is `position: sticky`; depth comes from the 1px hairline, not shadows — the page is essentially flat.
