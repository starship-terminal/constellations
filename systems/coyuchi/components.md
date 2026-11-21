# Components

Public homepage, one public product, and the empty sign-in wall, signed out, 2026-11-22. The sign-in URL carried OAuth query state, so that screenshot was discarded. Measurements for the wall are in [raw/readings.json](raw/readings.json).

| Component | States seen | Evidence |
|---|---|---|
| Wordmark | default | [screenshots/home-light-1440.png](screenshots/home-light-1440.png). [icons/mark.svg](icons/mark.svg) |
| Promo bar | default | Same shot. Sage `#637868`, 50px, white type |
| Department link | default | TT Norms Pro 14px, uppercase, `#333333` |
| Icon button | default | Search, Log in, Cart |
| Hero | default | Sale type over a photograph, white square button |
| Primary button | default | Shop 25% Off, 60px, white, square. Add to Cart, 58px, ink. Not clicked |
| Product title | default | [screenshots/product-light-1440.png](screenshots/product-light-1440.png). Tiempos Headline 32px, `#333333` |
| Price | default, sale | Struck `#898989`, sale 20px rust `#832b1a` |
| Color swatch | selected | Doe swatch among a row of fabric chips |
| Size chip | selected, unselected | Queen filled ink. King and Cal King outlined, 36px, stone border |
| Text field | empty | Sign-in email, 49px, `12px` radius. Not photographed |
| Display heading | default | Sign in, Roboto 20px, weight 700. Not photographed |

## Gaps

Hover, focus-visible, pressed, error, and loading were not measured. Search and the cart were not opened. No toast, table, or avatar was captured. A password field does not appear until email is submitted, and that submit was not made. The login screenshot was discarded because the URL carried OAuth state.
