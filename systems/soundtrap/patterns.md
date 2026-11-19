# Patterns

How the public pages combine the components. No screenshots were saved. The preview browser did not produce frames.

## Marketing shell

`https://www.soundtrap.com/` redirects to `/musicmakers`. The nav is 90px, dark (`dark.background.page`), with Matter 15px weight 700 links and a light pill. The hero sits on `rgb(26, 26, 35)`, which is not a named token, with an 80px headline. Later sections switch to `st-light-theme`.

Features (`/content/features`) keeps the same dark nav. Its headline is `st-display-1` in `dark.text.link`.

## Login

`/login` is a light page, html background `#ffffff`, form 448px wide, centered. Four OAuth buttons stack at 44px with 8px radius, then an "or" rule, then email and password fields, then a primary "Log in" button. Nothing was submitted. OAuth was not followed.

## Pricing

`/pricing` uses a different shell. The bar is `rgb(62, 17, 101)`, 90px, and at 390 it shows a 24px menu button. Plan cards are 225px wide, 8px radius, in purple-rain, primary, simply-red, and maroon sets. A billing toggle is a 25px-radius track. The FAQ section is the negative set, `#b4074b`. No card was entered.

## Phone

At 390 CSS pixels the features and pricing pages still load. The marketing type scale did not change on the features h1 (still 37px). The pricing nav collapses to a menu button. A 390 capture of `/musicmakers` and `/login` was not taken.
