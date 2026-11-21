# Readings

Live page: https://www.raus.life/ on 2026-11-19, T3 preview, signed out.

`preview_snapshot` returned "The browser is not producing screenshot frames" on 2026-11-19. Measurements already read were kept. A later headless pass on 2026-11-21 wrote screenshots/. Those PNGs are 256-colour. Do not sample tokens from them.

The page background is `html` `background-color: rgb(253, 249, 237)` (`#fdf9ed`). `body` itself computed to transparent. Body text is `rgb(35, 33, 44)` (`#23212c`).

Headings that are green computed to `rgb(0, 100, 52)` (`#006434`). The wordmark `fill` computed to the same green. A small forest fill on three spans computed to `#006334`. Those two greens are both on the page. Tokens use `#006434` for text and the logo, and record `#006334` as a second measured fill.

The promo strip "The wait is over" computed to `rgb(166, 223, 255)` (`#a6dfff`), padding `8px 48px`, no radius. "Book now!" on that strip computed to `rgb(221, 80, 0)` (`#dd5000`), white text, radius `12px`, padding `0px 10px`, height 32, font 18px.

The search pill on the home page computed to `rgb(252, 189, 28)` (`#fcbd1c`), radius `40px`, height 128, padding `0px 48px`. "Book your stay" inside it is a 128px circle (`border-radius: 64px`) in `rgb(178, 24, 164)` (`#b218a4`).

Filled actions (Search, Start quiz, View all articles, Learn more, Find a cabin) computed to `#23212c` with white text, radius `20px`, height 48, padding `0px 20px`, font 22px, letter-spacing `-0.22px`.

The outline action "Cabins near me" computed to a 1px `#23212c` border, transparent fill, radius `20px`, height 48, padding `0px 20px`.

Filter chips on `/search` computed to white fill, `1px solid rgba(35, 33, 44, 0.1)`, radius `12px`, height 34, font 18px. The Filters control computed to `#bdda0e` with ink text, radius `16px`, height from padding `0px 10px`, font 14px.

Listing drive-time chips computed to a 1px `#23212c` border, radius `20px`, padding `4px 7.2px`, font 14px. Trait labels computed to 12px, `text-transform: uppercase`, letter-spacing `-0.06px`.

The newsletter link in the footer computed to a `#a6dfff` fill, `#dd5000` text, radius `20px`, height 48, padding `0px 20px`.

Focus on Search and Start quiz, after `focus()`, computed to `outline: rgb(255, 255, 255) auto 3px` and `box-shadow: none`. That outline matches the button text colour. It is what the page returned.

Adyen checkout CSS is in the Next.js bundle (`#0075ff`, `#00112c`, and the rest). Those controls were not painted. They are not tokens.

`--font-serif` in that bundle is `"fonts", "fonts Fallback"`. Serif headings computed to `fonts, "fonts Fallback", serif` at weight 300. The `@font-face` for `fonts` is weight 300, woff2, served from `/_next/static/media/19b50e30d7f70f04-s.p.woff2`. The family name in the face is the literal word `fonts`.

UI text computed to `neue-haas-unica, sans-serif`. Typekit kit `fco7dci` declares weights 300, 400, 500 and 600. Measured controls used 300 or 400.

No product custom properties were declared on `:root`. Styled-components class names (`sc-…`) carry the paint.

`prefers-reduced-motion: reduce` appears once, on `.adyen-checkout__card__cvc__hint__wrapper { transition: none; }`. Product links computed `transition: 0.2s` (property `all`, easing `ease`). The Book your stay button computed `opacity 0.2s cubic-bezier(0.665, 0.425, 0.44, 1.105), color 0.4s cubic-bezier(0.665, 0.425, 0.44, 1.105)`. The page was not re-read under reduced motion.

Not entered: no booking, no date selection submitted, no guest count changed, no card, no account, no phone, no newsletter address. Gift cards, shop, business, finder quiz, and Personio careers were not opened. Mailchimp `eepurl.com` and Jotform waiting list were not opened.
