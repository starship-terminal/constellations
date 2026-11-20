# Patterns

Signed-out public pages only. Measured 2026-11-19. No screenshots: the preview browser returned "The browser is not producing screenshot frames".

| Pattern | Page | What was on screen |
|---|---|---|
| Marketing shell | https://workleap.com/officevibe (redirect from https://officevibe.com/) | White nav, 58px, with Product, How it works, Our Story, Pricing, Resources, a text Log in, a secondary Let's chat and a filled Book a demo. Hero heading in ABC Favorit Variable. Footer is boardroom navy `#0c1754`. |
| Pricing | https://workleap.com/pricing | Three tiers: Standard from $4,999 USD, Pro from $11,999 USD (most popular, yellow header), Enterprise custom for 250+ employees. Cards are white, 24px radius, blue-tinted shadow. Compare-tiers table sits below. |
| Demo request | https://workleap.com/demo | Heading "Book a demo with an expert" in `#0c1754`. Form asks for first name, last name, business email, job title, phone number, company, employee count. Not submitted. |
| Signed-out login | https://login.workleap.com/ | Ivory page `#f8f6f3`, white card, radius 16px, blue-tinted shadow. Heading "Let's leap in!" in ABC Favorit, 24px, weight 680, colour `#3c3c3c`. One field labelled "Email or mobile number" and a Next button. Not submitted. |

## Not captured

| Pattern | Reason |
|---|---|
| App shell, survey, employee directory, recognition | Behind a company workspace. The capture rule says not to enter one. |
| Form validation error | Reaching it on the demo form needs a phone number. The login field accepts a mobile number, so it was not submitted. |
| Empty, loading, error, destructive confirmation, toast, search, table of employee data, onboarding | Not on the public pages. |
| Dark theme | `prefers-color-scheme: dark` was true and the pages still painted the light tokens. No dark theme switch was on the public pages. |
| 1440 and 390 widths | The preview viewport was 1169 by 731 CSS pixels and could not be resized. |
