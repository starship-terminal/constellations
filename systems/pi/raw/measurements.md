# Measurements

Read on 21 November 2026 from headed Chrome. Viewport requests landed as recorded.

## Viewports

| Page | innerWidth | innerHeight | devicePixelRatio | visualViewport |
|---|---|---|---|---|
| Chat, desktop | 1440 | 900 | 2 | 1440 × 900, scale 1 |
| Marketing home, desktop | 1440 | 900 | 2 | scale 1 |
| Chat and marketing, phone | 390 | 844 | 2 | scale 1 |
| Help Center | 1440 | 900 | 1 | screenshot is CSS pixels |

PNG pixel sizes are CSS size times devicePixelRatio, except the Help Center frame, which was saved at scale 1.

## Chat controls, light, 1440×900

| Element | Box | Background | Text | Radius | Other |
|---|---|---|---|---|---|
| Sidebar | 280×831 at 0,69 | #F7EFE4 | | 0 | `--sidebar-width: 280px` |
| Sidebar collapsed | | | | | `--sidebar-width: 64px` |
| Header Log in | 128×48 at 1120,85 | #1A4631 | #FCFAF7 | 48px | declared `--color-primary-default` |
| Sign up for free | 160×48 at 1256,85 | #FAF3EA | #655E55 | 48px | border 1px #E1D3C0 |
| Submit name | 40×40 | #038247 | #FCFAF7 | 9999px | |
| Name field | 528×40 at 572,805 | #FCFAF7 | #131212 | 10px | DM Sans 16/22.4, weight 500, tracking -0.16px |
| Greeting paragraph | 576×158 | transparent | #1A4631 | 0 | GRENETTE 18/25.2, tracking -0.36px |
| Greeting column | 576 wide | | | | `max-w-[576px]` |

## Login, light, 1440×900

| Element | Box | Background | Text | Radius | Other |
|---|---|---|---|---|---|
| h3 Sign up or log in | 672×35 at 384,222 | transparent | #131212 | 0 | GRENETTE_CONDENSED 32/35.2, tracking -0.48px |
| Continue with Google | 353×56 at 544,297 | #FCFAF7 | #131212 | 48px | border 1.5px #E1D3C0 |
| Email | 56×56 at 636,578 | transparent | #655E55 | 9999px | border 1px #E1D3C0 |

Dark login uses page `#131212`, OAuth fill `#242322`, border `#504A42`.

## Marketing, hey.pi.ai

Desktop scroll height about 4813 CSS pixels. Phone scroll height about 6096 CSS pixels.

| Element | Value |
|---|---|
| body background | #FAF3EA |
| h1, 1440 | Grenette Pro Regular 64/60.8, tracking -3px, #131212, 379×182 |
| nav Try Pi | 96×40, radius 40px, fill #131212 |
| Get the app | Grenette 15/30, tracking -0.15px, #131212 |
