# Telescope patterns

Signed-out only. Marketing home at https://telescope.fyi/ and the login form at https://telescope.fyi/login.

## Marketing home

The page is one long scroll on `--color-beige` (`light.color.page`). Type is Beausite at a fluid root size, with DM Mono uppercase labels ("Currently in beta", "Scroll", "Login"). The hero headline uses `.t-h1`. A yellow pill (`Sign up`) and a text `Login` link sit in the footer chrome. Both go to `/login`.

The middle of the page is a public demo of curator collections (product cards, collection titles, entry counts). Those cards are the marketing site's own content, not a signed-in library. Grid is 6 columns below 1024px and 12 columns at 1024px and up. Margin and gutter are `core.space.grid-margin-mobile` and `core.space.grid-margin`.

Footer brand is an SVG that scales with scroll (`--min-scale` 0.4, and 0.15625 at 1024px). That motion is scroll-driven. This capture did not record a scroll timeline.

## Login

`/login` is a different app (Next.js, not the Nuxt marketing site). `body` has class `dark`. The form column is 360px inside a 480px panel. The rest of the row, from x=480, is a curator panel (`hidden` below the `md` breakpoint).

The form is Google, the word "or", an email field, a disabled Continue, and a legal line. Continue stays disabled while the email is empty. Google was not used. No email was submitted. No payment, phone, or company SSO appeared.

## Not captured

Signed-in home, collections, save, subscribe, settings, onboarding, search, empty, loading and error screens. Theme toggle on the marketing site: the marketing CSS has no `prefers-color-scheme` block. The login light tokens exist as declarations only.
