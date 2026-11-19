# Patterns

## Sunset notice

`https://sora.com/` redirected to `https://sora.chatgpt.com/sunset`. The page is one `main` that fills the viewport (`min-h-screen`, flex, centered). Inside it, a column with `max-width: 28rem` (computed 448px) and `gap: 24px` holds the secondary sentence and the Export link. Horizontal page padding is 24px. Text is centered.

There is no header, no footer, no nav, and no logo on the page. The document title is "Sora". The meta description still says "Transform text and images into immersive videos."

The loaded theme is dark: black page, white text, white Export control with black text. Removing the `dark` class inverts that pair.

## Gaps

| Pattern | Status |
|---|---|
| Marketing home | Not present. The start URL redirects to the sunset page. |
| Login and signup | Not present. No email field, so the AgentMail address was not submitted. |
| App shell and navigation | Not present. `--sidebar-width: 196px` is declared and not painted. |
| Form with a validation error | Not present. |
| Empty, loading, error | The sunset copy is the product's unavailable state. No skeleton, spinner or error toast was rendered. |
| Destructive confirmation, search, list, onboarding | Not present. |
| Signed-in composer and video generation | Not entered. |
| Screenshots of this pattern | Not captured. Preview screenshots failed, and headless Playwright hit Cloudflare. |
