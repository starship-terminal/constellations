# Xbox components

Public signed-out surfaces on xbox.com, measured 2026-11-19. Marketing pages use Microsoft Web Framework (square corners, lime and green CTAs). Search and the store use a second module with 4px radius. Crops were not cut: the preview browser stopped producing frames (`The browser is not producing screenshot frames`), and the package keeps full-page screenshots instead.

## Button

The marketing primary is `a.c-call-to-action.f-heavyweight`: fill `light.action.primary` (#9bf00b), label `light.action.primaryText` (#054b16), Segoe Pro Black 15px/900, padding 5px 20px 5px 22px, height 32px, radius `core.radius.none`. Transition `all 0.2s ease-in-out`. Hover on the live hero CTA did not change the computed fill. A stylesheet rule paints group CTAs to #8bd80a on hover and #0d630d on active.

The lightweight CTA is transparent with a 2px transparent border, same type, height 41px. Colour modifiers measured: white, #107c10, #054b16, #9bf00b.

The store primary, GET GAME PASS, is a different green. Sampled fill #008746 on [product-light-desktop.png](screenshots/product-light-desktop.png) and [product-light-phone.png](screenshots/product-light-phone.png). The BUY button beside it samples to #484e58 with a white label. Neither control had painted in the live preview when computed styles were read, so those two fills are sampled, not computed.

Search "Buy now" is a 40px control, 4px radius, 2px white border, label rgb(61, 70, 90).

## Link

Footer links are 11px Segoe UI, #616161 on the light footer and #a7a7a7 on the dark product footer. Nav items are 13px, white on the dark header and #262626 on the light search header.

## Badge

`.c-badge.f-highlight` is #ffd800 on black, 13px/700, letter-spacing 0.975px, padding 0 7px 1px, height 18px, square. The search discount chip uses the same yellow.

## Card

Search result cards are 176px wide at the 1169px preview, fill #f9f9f9, 4px radius, shadow `0 1px 2px rgba(0,0,0,0.11), 0 3px 7px rgba(0,0,0,0.13)`, title 14px/600. Marketing mosaic tiles are square and borderless.

## Tabs

Product page DETAILS / REVIEWS / MORE are 40px, 14px, 4px radius, transparent fill, white text. The selected tab draws an underline. Search category tabs (Games, Add-Ons, Subscriptions, Hardware, Support, General) sit on white.

## Text field

The header search input is #2d2d2d with a 1px #7cc400 border in the closed dark header, and white with a 1px #0067b8 border on the light header. It was `display` with zero size until search opened, so padding (7px 38px 7px 10px) is computed but the open field was not screenshotted as a focused control.

## Avatar

The signed-out ME control is 36px, `border-radius: 50%`, 1px white border, 14px label. It is not a signed-in gamerpic.

## Gaps

Text area, select, checkbox, radio, switch, menu (beyond the closed nav), tooltip, dialog, toast, table, list row, and destructive confirmation were not on the public pages measured. The nav dropdowns exist in the DOM hidden. Sign-in, checkout, and the Microsoft account flow were not entered. Icon SVGs were not extracted.
