# Components

Controls that were on screen on 2026-11-22. Login, signup, plan, and cookie controls were not clicked. Hover and focus were not opened.

## Primary button

Start for free and Get Evernote free on the light homepage. Fill `#141414`, label `#ffffff`, Figtree, label weight 600, radius 5px.

| Instance | Size | Padding | Page |
|---|---|---|---|
| Start for free | 151 by 46 | 10px 28px | Homepage header |
| Get Evernote free | 250 by 59 | 16px 40px | Homepage hero |

On the AI Features page the same Start for free control paints lime `#94e130` with an ink label. That page puts `class="dark"` on the header. [screenshots/public/ai-features-light-desktop.png](screenshots/public/ai-features-light-desktop.png)

## Lime button

Discover more on the homepage. Fill `#94e130`, label `#141414`, 20px, weight 600, radius 5px, 250 by 59. [screenshots/public/home-light-desktop.png](screenshots/public/home-light-desktop.png)

## Outline button

Choose Starter and Choose Advanced on the plans page. Transparent fill, 1px border `#a1a1a1`, ink label, radius 5px, 200 by 46. Not clicked. [screenshots/public/plans-light-desktop.png](screenshots/public/plans-light-desktop.png)

## Chip

Capture on the homepage and Starter on the plans page. Fill `#94e130`, radius 52px, padding 4px 12px, weight 600. Capture's label is `#141414`. Starter's label is `#262626` in Inter.

## Nav link

AI Features in the light header. Figtree, 16px, weight 400, color `rgb(0, 0, 0)`, radius 10px, padding 8px 10px 10px. On the AI Features page the same label computes to `#ffffff`.

## Text link

Log in in the light header. No fill, radius 5px, padding 10px 24px, 92 by 39. Footer Why Evernote is the same family at 16px, padding 8px, radius 5px.

## Heading

Homepage h1, "Your second brain". Figtree, 72px, weight 600, line-height 72px, letter-spacing -3.6px, color `#141414`. Section h2 is 50px, line-height 55px, letter-spacing -2.5px. [screenshots/public/home-light-desktop.png](screenshots/public/home-light-desktop.png)

## Hero card

Sand `#f4eee5`, 1px border `#e7e7e7`, radius 16px. It wraps the homepage hero. [screenshots/public/home-light-desktop.png](screenshots/public/home-light-desktop.png)

## Wordmark

Header image, 179 by 44, from the site's own SVG. The light file is `evernote-logo.86b04f42.svg`. The inverted file is hidden on the homepage (`dark:hidden` shows, `hidden dark:block` does not). On the AI Features page those displays swap.

## Auth field

Empty email field on the login wall. Border 1px `#cccccc`, radius 6px, 454 by 50, Inter 15px, color `#262626`. Placeholder is the product's own "Email address or Username". Nothing was typed. [screenshots/public/login-wall-desktop.png](screenshots/public/login-wall-desktop.png)

## Disabled Continue

Login wall, empty state. Fill `#cccccc`, label `#ffffff`, radius 8px, 454 by 50. Not clicked.

## Gaps

Hover, focus, pressed, and loading were not captured. The green hover rule `.hover:bg-green:hover` is `#00a82d` in the stylesheet and was not hovered. Explore was not opened in this pass. Cookie accept and reject were not clicked. Google and Apple were not clicked. No checkbox, radio, switch, tab, dialog, toast, or table was measured.
