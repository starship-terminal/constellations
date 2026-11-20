# Patterns

Sweden English storefront, signed out, 1440×900, 2026-11-19. Screenshots were not saved. The preview browser stopped producing frames, then PerimeterX denied the host.

## Storefront chrome

The header is 118px and not sticky on the home page (`position: relative`).

| Band | Height | Paint |
|---|---|---|
| Rotating banner | 30px | `rgb(239, 253, 164)` fill, black 12px uppercase Helvetica Now Text. Copy on the day: "Are you ready for the ski season ahead? Shop here." |
| Top bar | 44px | White. Logo is an Icon-Peak2024 glyph, 215×29, black. Nav links sit in the same row. Country switcher reads "SE / ENG", 12px, padding 8px |
| Bottom bar | 44px | White, 1px top border `rgba(0, 0, 0, 0.15)`. Search field fills it, placeholder "Search..." |

`--h-header-top-bar` and `--h-header-bottom-bar` are 50px. Those are the mobile bar heights. They were declared, not measured at 390.

## Home

The hero title is white Helvetica Now Display, 96px, line-height 96px, letter-spacing -2.88px, uppercase: "Are you ready for the cold?" The eyebrow above it is 12px white, letter-spacing normal: "Outerwear without compromise". Two pills sit on the photo: "Shop women's jackets" and "Shop men's jackets".

Below that, a "Shop jackets" rail (32px uppercase, letter-spacing -0.32px) of 360px product tiles. Then full-bleed story tiles with a 12px eyebrow, a 48px title and the same pill. The page ends in a link directory (About, Membership, footer columns) and a 317px footer of 12px uppercase links.

## Collection

`/se/en/women/jackets.html`, title "Jackets & Vests - Women". Breadcrumb "Women / Jackets & Vests", 12px uppercase, padding 24px 24px 32px. The h1 is 64px, line-height 70.4px, letter-spacing -0.64px, uppercase, inset 24px from the left.

A 50px toolbar, 1px bottom border `rgba(0, 0, 0, 0.15)`, holds "Filter & sort", "66 items" and "View as: Model / Product". The grid is four 360px tiles with no gap.

"Filter & sort" opens a 450px white sheet from the left, fixed, full viewport height, no shadow. Groups are uppercase 14px rows. Colour options are 12px dots. The footer of the sheet is an outline "Clear filters" pill and a black "Show results 66" pill.

## What was not walked

| Pattern | Why |
|---|---|
| Product page | Direct URL hit PerimeterX. Size grid, gallery and buy column (`--pdp-w-block-right: 540px`) were not measured |
| Bag and minicart | Not opened. The drawer is in the DOM at `display: none`. Checkout was not entered |
| Account, register, newsletter | Not submitted. Footer links only |
| Search results | The field was not typed into |
| Empty, loading, error pages | Not reached |
| Phone layout | Not resized before the block |
| Dark theme | No toggle on the public storefront |
