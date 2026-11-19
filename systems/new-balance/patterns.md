# Patterns

Signed-out pages on newbalance.co.uk, measured 2026-11-19. No page screenshots: the preview browser did not produce frames, and headless Chromium was blocked with HTTP 403.

## Storefront chrome

Two bars. A black banner (computed `#151415`, 57px) carries the country label, rotating promo lines at 14px weight 500 in white, and a Help menu. Under it, a white navigation bar (82px) holds the red NB wordmark (59 by 28px on desktop), category links at 16px weight 300, and 32px search, account and bag icons. Combined header height was about 139px at innerWidth 1169.

The footer paints `#000000`. Footer link colour computed to `#000000` on the login page, which is the body's colour showing through a link that had not picked up a footer text colour in that read. Treat footer link colour as unread.

## Home

Hero headline "The 983" computed at 60px, weight 300, line-height 68px, black on a transparent box. Shop now is the secondary button. A page heading "New Balance Trainers & Clothing" is 32px weight 500. Product rails repeat tile name and price. The page scroll height was 4584px.

## Listing

`/men/` titles the grid in ITC Garamond at 40px / 40px weight 500. Filters sit in a left column. Hide Filters is a 4px-radius outline button. Tiles are name, then price, with no card chrome.

## Product

The buy column is 328px wide. Title 32px / 40px weight 500 in Proxima Nova. Price 18px weight 700. Colour swatches, then a size grid of 2px-radius cells, then a full-width Add to Bag. Add to Bag was not pressed.

## Help

`/customer-care/` opens with "Contact Us" in ITC Garamond at 56px / 60px weight 500. Side links (Contact Us, FAQ, Size Guide) computed to `rgb(230, 230, 230)` at 16px, which is too light to read on white. That reading is kept as measured and called out under What to distrust. An email field uses the same 4px-radius, 58px box as login. The form was not submitted.

## Login

`/account-login` redirects to the Demandware Login-Show page. Email, password, a 16px Remember me checkbox, Forgot password, and a 328 by 54px Log in button. The form asks for a password. It was not submitted. No card, phone or address field was on that page.

## Not captured

Bag, checkout, search results, an open menu, a validation error, an empty state, a loading state, and any phone-width layout.
