# Components

Measured signed out on ssense.com/en-sg on 2026-11-19, viewport 1169 by 731, device pixel ratio 2. Values are computed styles. No crops: the preview browser did not produce screenshot frames.

## Header

Fixed bar, 55px tall, white, no shadow, no radius. Nav is a flex row with a 20px gap. Links are Favorit SSENSE Inter 11px / 15px, weight 400, black, uppercase, padding 0. The wordmark is an inline SVG, 104 by 21.2px, fill rgb(0, 0, 0), centred in the bar.

## Link

Storefront links share the 11px chrome style and have `text-decoration: none` at rest. Hover uses `.background-underline`: a 2px repeating gradient of `rgba(0, 0, 0, 0.75)` at `1.1em`. That state was read from the rule, not from a painted hover.

## Button

Add to bag is a 35px-tall flex button, black background, white 11px uppercase label, 1px solid black border, radius 0, min-width 140px. On the product page it was 255.1px wide. It was not clicked.

Continue on the login page is the same black fill and white uppercase label, 37px tall and 380px wide, set in Favorit SSENSE Regular with a Helvetica Neue fallback. It was not clicked.

Add to wishlist sits beside Add to bag: transparent, black, 35px tall, padding 10px 18px, min-width 130px, no border. It was not clicked.

The homepage Shop menswear control (`.ed-ButtonCTA`) is different: transparent, 36px tall, padding 0 18px, 1px solid rgb(151, 151, 151), radius 10px. Its label is Favorit SSENSE Inter1 at 12.35px / 16px, letter-spacing -0.05px, color rgb(51, 51, 51), uppercase.

A declared `.s-button--disabled` rule uses rgb(182, 182, 182) for background and border and white text. It was not painted on a control.

## Text field

Login email (`#email`) is 380 by 30px, padding 0 6px, 1px solid black, radius 0, Favorit SSENSE Inter 11px. The label above it is weight 500 with a 5px margin-bottom. Focus showed no outline and no shadow. The field was left empty.

The search dialog field is 37px tall inside a 39px row, 1px solid black, padding-left 9px. Its placeholder "SEARCH MENSWEAR" is rgb(182, 182, 182). Nothing was typed.

The listing "Search Designers" input is 150 by 30px, background rgb(251, 251, 251), padding 0 14px, no border.

## Select

The product size control (`#size-dropdown`) is 385.1 by 36px, 1px solid rgb(119, 119, 119), padding 7px 25px 7px 6px, 11px / 20px, radius 0. The empty "SELECT A SIZE" option is disabled. While focused, outline-color was rgb(229, 151, 0) and outline-style was none, so the ring did not paint. The value was not changed.

## Checkbox

The SALE ONLY checkbox in the search dialog is 12 by 12px, `appearance: none`, margin-right 10px, radius 0. It was not toggled.

## Card

A listing card is a column link. The image box is 237.3 by 356px (aspect 2 / 3) with a 10px bottom margin. Brand is 11px uppercase. The product name is 11px / 15px, sentence case. Price is 11px. A sale price stays black; the previous price is rgb(136, 136, 136) and `line-through`, 5px to the right.

## List row

FAQ questions are a `strong` inside a paragraph: Favorit SSENSE Inter 11px, weight 700, line-height 15px, margin-bottom 10px. The answer paragraph is the same size at weight 400. Sidebar group titles (Help, Shopping) are 13px weight 700, line-height 20px.

## Dialog

The search popover is `role="dialog"`, 450 by 151px, white, 1px solid rgb(182, 182, 182), padding 20px, radius 0. Department buttons inside it are the 11px uppercase chrome style with a 16px left margin after the first. Close is an uppercase text button, 39px tall. The dialog was closed without a search.

## Gaps

- No screenshot crops. `preview_snapshot` failed with "The browser is not producing screenshot frames".
- Hover, pressed, loading, and error were not painted. The underline hover rule and the disabled button rule are declared only.
- Focus on the size select did not paint. Focus on the login field and the search field cleared the outline.
- No textarea, radio (the footer gender radios were in a closed popover, height 0), switch, tabs, menu, tooltip, toast, table, avatar, or badge was measured as a visible control.
- OneTrust cookie controls were in the DOM at height 0. Their 2px radius and 14.4px type were computed but not on screen.
- Dark theme was not present. Phone width was not measured.
- Add to bag, wishlist, login, checkout, and account creation were not entered.
