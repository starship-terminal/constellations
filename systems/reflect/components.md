# Reflect components

Public site only, measured 2026-11-21. Crops were not cut. The screenshots show the controls.

## Button

Marketing primary (`.button.button-primary`): 14px Inter V at 500, colour `#f4f0ff`, padding 8px 16px, radius 8px, height 36px. The fill is a pseudo-element wash `rgba(113, 47, 255, 0.12)` with an inset glow, not a solid background on the anchor. Hover swaps to the `::after` wash at `rgba(113, 47, 255, 0.24)`. See [home](screenshots/home-light-default.png).

Secondary (`.button-secondary`): 1px border `rgba(243, 238, 255, 0.08)` and a near-clear wash. Used for Subscribe and "Get the iPhone & iPad app".

Blog trial (`Start Free Trial`): solid `#a855f7`, text `#ece5ff`, 14px weight 600, height 40px, radius 8px. See [blog](screenshots/blog-light-default.png).

Auth Continue: solid `#7c3aed`, white text, 18px weight 600, 288×44, radius 8px. See [login](screenshots/login-light-default.png). Not clicked.

## Link

Nav links are 14px Inter V at 400, `rgba(255, 255, 255, 0.9)`, line-height 20px. Product, Pricing, and Company are in-page anchors. Blog, Changelog, and GitHub leave the page.

## Text field

Auth email: placeholder `your@email.com`, empty, height 50px, padding 12px 16px, radius 8px, 1px solid `#1e293b`, fill `rgba(15, 23, 42, 0.5)`. Newsletter fields on the home footer and the blog were not typed into.

## Menu

Desktop nav is a pill of links, not a dropdown. At 390px a `.header-toggle` opens `.header-nav`, position fixed, full viewport, background `rgba(3, 0, 20, 0.9)`. Close is an X. See [mobile menu](screenshots/mobile-home-light-menu.png).

## Dialog

"Play the Reflect launch film" opens a video overlay with a Close video control. The film was not played past the poster. See [video](screenshots/home-light-video-dialog.png).

## Chip

Blog tags are pills. The selected tag is `#1e3a8a` with white text, radius 9999px. See [articles](screenshots/blog-light-articles.png).

## Card

Download page lists platform rows (macOS Apple Silicon, macOS Universal, Windows, Linux, iPhone & iPad). Blog posts are image cards with a tag chip and a date. See [download](screenshots/download-light-default.png).

## Gaps

Checkbox, radio, switch, tabs, tooltip, toast, table, avatar, and badge were not present on the public pages that were opened. Pressed, disabled, and loading were not captured. Identity provider buttons on the auth wall were photographed and not clicked.
