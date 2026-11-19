# Trulia components

Measured on the signed-out homepage at https://www.trulia.com/ on 2026-11-19. Viewport 1169 by 731 CSS pixels, device pixel ratio 2. No element crops: the preview browser did not produce screenshot frames, and a later navigation hit PerimeterX.

Values are token names from [tokens.json](tokens.json). The reading is in [raw/homepage-computed.json](raw/homepage-computed.json).

## Header

Fixed header, computed height 64px (`core.size.header`). Background transparent. Wordmark link "Go to Trulia Home" (`data-testid="navbar-trulia-logo"`), color `light.color.accent`, padding 16px 24px 16px 0, an inline SVG at 70 by 24.

Nav links Buy and Rent: `button--type_navigation`, text `light.color.text`, weight 700, padding 8px 16px, radius `core.radius.m`, height 42px, transparent fill and border.

Sign up or Log in: `button--type_default`, white fill, 1px `light.color.border`, text `light.color.text`, weight 700, padding 8px 16px, radius 8px, height 42px, width 157px. Not clicked.

## Hero

h1 "Discover a place you'll love to live": `textStyle_headline`, 28px, weight 900, line-height 31.92px, letter-spacing -0.1px, color white. Sits on a photograph. The photograph is content.

Buy / Rent / Sold tabs. Selected Buy: white fill, text `light.color.accent`, weight 400, padding 8px 24px, radius 8px, height 40px. Resting Rent and Sold: transparent fill, white text, same padding and radius.

Search combobox, placeholder "Search for City, Neighborhood, Zip, County, School": white fill, 1px `light.color.search-border`, radius 8px, height 60px, width 520px, padding 8px 48px 8px 16px, 20px Figtree, weight 400. Not typed into. A second combobox on the page used grey-50 fill. Which instance is the hero field was not isolated.

## City card

Link "Atlanta, GA / View Homes" to `/GA/Atlanta/`. Card title h3 `textStyle_title`, 24px, weight 900, white, text-shadow `0 1px 5px black` from class `tsh_0_1px_5px_black`. The card photo is content. The link was not followed. A later direct navigation to that URL was denied by PerimeterX.

## Section CTA

"Find a home", "Find a rental", "Learn more": `button--type_primary`, background `light.color.accent`, text white, weight 700, padding 8px 16px, radius 8px, height 42px, width 175px, shadow `core.shadow.button-primary`. Not followed.

## Footer link

Caption anchors such as "Houses for Rent Near Me": 12px, weight 400, line-height 15.96px, color `light.color.text`, class includes `hover:td_underline`. "More" is the same size, weight 700, color `light.color.accent`. Hover was not measured.

Legal line: 10px, line-height 16px, letter-spacing -0.1px.

## Icon button

40 by 40, color `light.color.accent`, class `trs_opacity_0.2s_ease hover:op_0.85`. Resting opacity only. Hover not measured.

## Gaps

- Button hover, focus-visible, pressed, disabled, loading, and error were not measured. `--focus-shadow` is declared on `:root` and was not seen applied.
- Text field filled, error, and disabled states were not measured. The search field was left empty.
- Text area, select, checkbox, radio, switch, menu, tooltip, dialog, toast, table, avatar, and badge were not present as measurable controls on the homepage, or were not isolated before the challenge.
- Tabs were observed as the hero Buy / Rent / Sold group at rest. Switching them was not done.
- Saved Homes and Saved Searches were visible in the header and were not opened.
- Sign up or Log in was not opened. No account was created. No phone was entered. No agent was contacted.
- Listing cards, map, filters, neighborhood pages, mortgage calculators, and the help center were not measured. `/GA/Atlanta/` returned a PerimeterX press-and-hold wall. A reload of the homepage and a new preview tab returned the same wall. Headless Chromium got HTTP 403 and was not used for values.
- No screenshots or crops exist. The preview browser reported: "The browser is not producing screenshot frames."
