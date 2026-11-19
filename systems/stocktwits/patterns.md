# Stocktwits patterns

Public signed-out pages, 2026-11-19. Measurements are computed styles. Screenshots of the product were not captured. [screenshots/capture-gap-light.png](screenshots/capture-gap-light.png) is a label for that gap.

## App shell

`https://stocktwits.com/` is the signed-out home. At 1440px the header is 90px, white, fixed. The watchlist column is 300px (`--sidebar`) and starts 81px from the left. The stream sits to its right. For You and Following are the two tabs under the header.

The left column holds Continue with Apple, Create Account, a blue text link to log in, and a default watchlist (AAPL, BTC, MSFT, NVDA, QQQ, SPY, TSLA on this load). A trending strip sits in the header.

At 390px the sidebar computed `display: none`. A 52px mobile header spans the width, with a 1px `#f2f2f7` bottom border and a Use App pill. The For You row is 390px wide.

## Auth

`/signin` splits the viewport. The left panel is 719px, background `#000000`, with a 57.6px weight 900 white welcome line. The right side is the form: two fields, a disabled Log In pill, blue links, and Continue with Apple.

`/signup` uses the same split. The form is one email field, a disabled Sign Up pill, and Continue with Apple. It was not submitted.

## Symbol

`/symbol/AAPL` keeps the shell. The quote block shows the ticker at 20px, the price at 30px, and the day's change in `light.positive` when the price is up. Tabs are Feed, News, Sentiment, Earnings, Futures, Fundamentals, Info. Feed is selected (black). The others are `#8e8e93`.

## Plans

`/subscriptions` sits in the shell. The heading "Unlock the Power of Stocktwits Data" is 36px weight 700, white, so it sits on a dark band that was not isolated as its own box. Three cards follow: Ad Free, Edge, Enterprise. Subscribe and Get In Touch were not clicked. No card number was entered.

## Marketing

`/about` is a black landing page. The hero title is 80px weight 700, line-height 74px, letter-spacing -2.4px, white, 530px wide. The hero container background is black plus a purple wash (`rgba(150, 102, 255, 0.44)` in the gradient). Content cards are 40px radius black panels.

`/widgets` is a white page. The title is 48px weight 700. The sample widget prints a loss in `light.negative`.

`/enterprise` is a white sales form: name, job title, work email, company, website, message. It was not submitted.

`/about/legal/privacy` is a white document. The title is 36px weight 700, line-height 42px.

## OneTrust

A privacy banner covers the lower right of every page that loaded. Its buttons are the vendor's `#1d68d7`, radius 2px. It was not accepted or rejected. It is not part of the Stocktwits component set.

## Not entered

- No account was created. Signup is email plus Apple on the first screen. The next step was not opened.
- No password was typed. No Apple sheet was opened.
- No brokerage, bank, card, phone, or government ID field was filled. Enterprise and subscriptions were read and left.
- Search was not submitted.
- The theme cookie stayed `viewMode=lightMode`. Dark values were read from `[data-theme=dark]` and the attribute was removed.
