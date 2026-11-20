# Patterns

Public signed-out pages only. Measured 19 November 2026. [screenshots/home-light-default.png](screenshots/home-light-default.png) is a reconstruction of the measured chrome. The preview browser returned "The browser is not producing screenshot frames", so it is not a photograph of the page.

## Homepage

https://www.pinterest.com/ at 1440 by 900 CSS pixels, device pixel ratio 2.

A white page, an 80px header, a red Log in button, a gray Sign up button, and a gray search shell. The hero "Create the life you love on Pinterest" is 48px / 900 / -0.5px. Below that, idea cards at 8px radius, then a black footer. A signup wall sits further down the page: "Welcome to Pinterest", email, password, birthday, Continue, and Continue with Google. That form was not submitted.

## Explore

https://www.pinterest.com/ideas/ at 1169 by 731 CSS pixels.

The h1 "Explore the best of Pinterest" is 36px / 700. Category tiles sit on the page. A login wall is in the document: "Log in to discover more ideas just for you", email, password, Forgot password?, Log in, Continue with Google, Continue with QR code. It was not submitted.

## Policy

https://policy.pinterest.com/en/privacy-policy at 1169 by 731 CSS pixels.

A separate policy site. Body face is pinSans. The h1 "Privacy Policy" computed 84px / 900 / #111111. This is not the Gestalt homepage scale. It is recorded as a different surface, not as a homepage token.

## Phone width

https://www.pinterest.com/ at 390 by 844 CSS pixels.

The header stayed 80px tall and the desktop links still laid out past 390px. Search input width computed to 0. A dedicated phone shell was not measured.

## Gaps

| Pattern | Status |
|---|---|
| App shell | Not captured. Signed-in home was not entered. |
| Form with a validation error | Not captured. Signup and login forms were not submitted. |
| Empty, loading, error | Not captured. |
| Destructive confirmation | Not present on the public pages. |
| Search results | Not captured. Search was not submitted. |
| Board or pin | Not captured. Following a board needs an account. |
| Dark theme | Not present. The OS preferred dark. The page stayed `lightMode`. |
