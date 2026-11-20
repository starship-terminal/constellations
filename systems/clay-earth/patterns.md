# Mesh patterns

How the measured components compose me.sh's two public surfaces — the black marketing site and the warm-cream pricing route — plus the app.me.sh sign-in boundary. Values are tokens from [tokens.json](tokens.json); every number was measured ([raw/measurements.md](raw/measurements.md)).

## The glass nav pill

A 388 x 48 pill floats centred at the top (`header`), radius 16, padding 24: its `::before` paints a 3% white fill under a vertical white-sheen gradient plus a layered glass shadow (hairline ring + two soft drops). Inside, the tan wordmark (`color.tan.300` #f2b98b), 12px/700 white links (Verlag), three dropdown BUTTONs (Releases/Resources/Company — `nav-dropdown`, 64x27) that open a 556 x 154 link panel (`menu-panel` / `menu-card`, 14px/700 white links) on their own press, a "Sign In" action (34px tall, `text.muted` 64% white, radius 8, hover: 8% white wash + full white text) and the "Get Started" pill (`nav-cta`, 32px, radius 8, painted only by a 24% white inset ring — never filled). All navigations away (app.me.sh, /start) were measured, never followed.

## The hero

Black ground (`color.ink.950`, painted by `documentElement`) under: the animated "RELATIONSHIPS MANAGED:" counter (`stat-counter`, 18px/700 white digits cycling in `IQmOHa_animatedDigit` spans), the 64px/700 VerlagCondensed headline in `#fefef7` (`color.cream.0`) — the last word rotates — and a 20px Verlag lede in `#86868b`. The "Get Mesh Free" CTA (`cta`, 205 x 54, radius 14) is an inverted `#fdfcfa` fill with black 18px/600 text, a 98% white glow (`shadow.ctaGlow`) and a `::before` painting the blue-violet-amber ring gradient (`gradient.ctaRing`, 225deg) 54px proud of the pill; hover shrinks it ~1%. Its twin `cta-bottom` (185 x 52, radius 16, pure `#fff`) closes the page on the `#0f0f10` band with tan text — the gradient ring behind it too.

## Feature filter pills

480 x 48 pills (`filter-button`) on a light band switch the demo panel — a local toggle, never a navigation. The pill itself is transparent; an `::after` paints the ink wash (`gradient.filterWash`, 6% -> 3% of `#1d1d1f`) at radius 16.

## The pricing route

A different skin on the same site: `main` paints `#f9f8f6` (`light.surface.page`), 48px/700 VerlagCondensed h1 in `#1f1f1f` (`light.text.primary`). Above the cards, the 226 x 40 billing toggle (`billing-toggle`, radius 12, 6% ink chip). Four 288 x 196 card tops (`plan-card`, radius 16): 6% grey fill under a white sheen (`gradient.cardSheen`), 1px `#eceae8` hairline (`light.border.subtle`), 24px padding; the popular Team card adds the 24% orange glow ring (`light.accentRing` / `shadow.popularRing`) and a POPULAR tag. Eyebrow labels in `#fb7232` (`plan-name` / `light.text.accent`, 14px/600), Chronicle-serif prices (`plan-price`, 18px measured on the row — the $ amounts set larger), then the action: outline "Get started"/"Try it free" (`plan-cta`, 238 x 44, radius 10, 40% ink border `light.border.control`) or the filled `#fb7232` "Try it free" on the popular card (`plan-cta-filled`, white text `light.text.onAccent`). Hover flips the outline button to the orange fill with white text; pressed holds it.

## The sign-in card (boundary)

app.me.sh/login is a third stack: `#fcfcfc` ground, SF Pro Text, gray `#48494a` text. The 272 x 40 e-mail field (`signin-input`, radius 6, 4% ink fill `light.field.fill`, 10% ink border `light.border.field`) was focused and filled with `name@example.com` then cleared — nothing sent. Above it the 272 x 44 OAuth pair: near-black `#1f1f1e` Apple (`light.oauth.ink`) and `#5383ec` Google (`light.oauth.google`, 87% on hover/pressed). The 272 x 40 "Sign in with email" (`signin-email-btn`, radius 12) wears the app orange `#ff6821` (`light.accentApp`) with 60% white text — never pressed. The "Create account" toggle (`signin-toggle`, 12px gray) was measured never flipped.

## Footer and mobile

The 1440 x 335 `#0f0f10` footer (`color.ink.900`): 12px/700 link columns at 40% white (`dark.text.faint`), tan social icons, the "AN AUTOMATTIC PRODUCTION" badge. At 390 px the nav becomes three fixed pieces — the logo, the 123 x 32 Get-Started pill and the 44 x 32 hamburger (`m-menu-button`, 6% white scrim, radius 8) — and the hero drops to 48px type. The hamburger's own press slides in the 374 x 762 drawer (`m-menu-open`, radius 12): a near-black glass fill over the page (`measured.drawer-fill` + sheen gradient), 14px/700 link rows (`m-menu-link`, hover text `#fb7232`), an expanded RELEASES list with a feature card, and the Get-Started-For-Free button.
