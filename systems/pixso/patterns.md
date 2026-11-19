# Patterns

No screenshots were saved. The preview browser did not produce frames. These notes describe the structure that was in the DOM.

## Marketing home

`https://pixso.net/` is a light page. Body is white, text is black, Figtree 16px / 24px. A 54px frosted nav sits at the top with Product, AI design, Import from Figma, Resources, Enterprise, Pricing, Log in, and Get started. The hero `h1` is 60px / 66px weight 700: "The collaborative UI/UX design tool, powered by AI". The primary action is the black `px-common-btn`. Sections continue with 48px headings. The footer (`#common-footer`) is a flex column with 32px inline padding. Its own text token is `#202124` and its muted token is `#667085`. The footer's computed colour on the element that was read was black, so the footer tokens are declared, not a second computed pass down the column.

## Product page

`https://pixso.net/ui-design-collaboration/` uses the same nav. An eyebrow (`.up-eyebrow`) is 12px weight 650, letter-spacing 0.84px, `rgb(80, 104, 165)`, in capitals as the product wrote it. The `h1` is 43px / 48.59px weight 700, `rgb(25, 28, 41)`. The lead is 18px / 32.4px, `rgb(87, 97, 115)`. Two buttons sit together: a dark primary and a white secondary, both radius 9px and 50px tall.

## Pricing

`https://pixso.net/pricing/` opens with a 46px / 62.1px weight 700 heading. Four plan columns (Free, Team, Enterprise, Private deployment) sit in a row. Amounts that were on screen included `$18`, `$8` and `$4` per seat per month, and yearly figures `$280`, `$120` and `$90`. Those amounts are product copy, not colours. Upgrade buttons were not clicked.

## Signed-out login

`https://pixso.net/user/login/` is a white card, 474px wide, centred in the 1169px viewport (the card started at x 348). The form offers Google, NAVER, then email and password, then a blue submit. "Sign up for free" swaps the same card to a signup form with the same two fields and a "Sign up" submit. SSO is a text button under the form. Nothing was submitted.
