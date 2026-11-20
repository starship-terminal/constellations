# Shop patterns

Measured on 2026-11-19 from a signed-out T3 preview tab. Viewport 1169 by 731, devicePixelRatio 2. No screenshots: preview frames failed.

## Home

https://shop.app/ follows redirects to https://shop.com/. The page title is "Shop - Shopping designed around you". `html` has no theme class. `body` is `bg-page` with computed background `oklch(0.98809 0 0)` and text `rgb(0, 0, 0)`.

The shell is a fixed left rail, 96px wide, and a content column whose wrapper padding-left is 76px (`--nav-content-offset` is 4.75rem). Rail items, top to bottom: Home wordmark, Home, Explore, View Cart, Deals, Orders, Sign in to view saved items, Sign in. Each hit target is 56 by 56.

A search shell sits near the top, 32px radius, white at 75 percent, with the placeholder "What are you shopping for today?". Under it, category chips (Holiday Sale, Gifts, Beauty, Women, Men, Baby & toddler, Sporting goods) are 36px pills.

A hero heading, "The Korean Beauty Edit", computed at 64px/58px, weight 800, letter-spacing -1px, white, over a promotional image. Section titles such as "Trending stores" and "Categories" are 20px/22px, weight 600, letter-spacing -1px, black.

Product tiles are 150px squares, 20px radius, with a dark price chip. A black download aside, 380 by 120, 24px radius, sits at the lower right: "Download the Shop app".

The footer is white, padding-left 76px, with Learn more, What is Shop?, Why trust Shop?, Why use Shop Pay?, Help center, and a Get started group (For brands, For creators, For agents, Build your store).

## Signup wall

Sign in leaves https://shop.com/ and opens https://shop.app/accounts/login. The document title is "Log in to your Shop account | Shop". Visible copy: "Sign in to Shop", "Or create an account", an empty email field, Continue, Use a passkey, and "By continuing, you agree to Shop's Terms and Privacy Policy."

The form column is 344px wide inside a 400px centered stack. The page background is `rgb(255, 255, 255)`. A background video element is present (1408 by 1768). Its play control computed as a 32px circle.

This is the signup wall. No email was entered. Continue was not submitted. Passkey was not used. No card, phone or checkout followed.

## Not entered

Cart, orders, saved items, deals and product pages can be linked while signed out. They were not treated as the signed-in app. Checkout and Shop Pay were not opened. No account was created.
