# Components

Public signed-out Yelp, measured 2026-11-19. Crops are from the 1440px about and 404 screenshots. Homepage, search and business values were read from computed styles in the preview tab. Those pages blocked headless Chromium, and the preview pane did not paint screenshot frames, so those surfaces have no crops.

| Component | State | Where | Values |
|---|---|---|---|
| Sign Up | default | about header, homepage hero chips | background `#D71616`, text `#FFFFFF`, height 40px, padding 8px 16px, radius 20px. Crop: [signup-button-default.png](components/crops/signup-button-default.png) |
| Sign Up | focus | about, element focused | outline `rgb(0, 118, 146) solid 2px` |
| Log In | default on light header | search and about | background `#F0F0F0`, text `#2D2E2F`, height 40px, padding 8px 16px, radius 20px. Crop: [login-button-default.png](components/crops/login-button-default.png) |
| Log In | default on photo header | homepage | transparent fill, white text, 2px solid `rgba(255,255,255,0.4)`, radius 20px |
| Search field | default | homepage, about, 404 | height 48px, radius 8px, shadow `rgba(0,0,0,0.16) 0 0 18px`, input Open Sans 16px/20px `#2D2E2F`, padding 13px 15px. Crop: [search-field-default.png](components/crops/search-field-default.png) |
| Search button | default | search header | background `#D71616`, white text, height 48px, radius 8px. Crop: [search-button-default.png](components/crops/search-button-default.png) |
| Filter chip | default | search | white fill, 1px `#C8C9CA`, height 32px, padding 7px 11px, radius 10000px, Open Sans 12px/16px weight 600 |
| Filter chip | hover | not captured | Headless hover was blocked. No hover colour was read |
| Result name | default | search | Poppins 20px weight 700, `#2D2E2F` |
| Rating | default | search, business | 20px svg. Fill is `rgba(var(--sem-color-bg-rating-*), 1)`. A 3.7 rating used rating-three `#FF8742`. Icon on the star is onStrong `#FFFFFF` |
| Hero heading | default | homepage | Poppins 48px/56px weight 700, letter-spacing -0.4px, white on the photo |
| Page title | default | search | Poppins 24px/32px weight 700, `#2D2E2F` |
| Marketing heading | default | about | Poppins 60px/75px weight 700, white. Crop: [hero-heading-default.png](components/crops/hero-heading-default.png) |
| 404 heading | default | missing route | Poppins 28px/36px weight 700, `#2D2E2F`. Crop: [notfound-heading-default.png](components/crops/notfound-heading-default.png) |
| Login field | default, not filled | /login | height 30px, padding 5px 9px, radius 3px, border 1px `#999999`, Helvetica Neue 14px, text `#333333`, width 300px |
| Login submit | default, not pressed | /login | background `#D32323`, white text, height 43px, width 300px, radius 3px, Helvetica Neue 16px weight 700. This red is the older login page, not `--sem-color-bg-brandPrimary-strong-default` |
| Logo | default | about header | The wordmark and burst. Crop: [logo-default.png](components/crops/logo-default.png). Not redrawn as an icon |

## Gaps

- Hover, pressed and disabled were not captured. The preview pane did not paint, so a hover screenshot could not be taken. Headless Chromium was blocked on the pages that hold the chips.
- No checkbox, radio, switch, select, tabs, menu, tooltip, dialog, toast, table or avatar was open on the signed-out pages. The cookie dialog was in the DOM at height 0.
- Signup and login were not submitted. The form asks for a password, a name and a ZIP. See [README.md](README.md).
- Dark theme: not present on these pages.
- Phone width: the 390px headless pass was a block page and was deleted. No phone screenshot remains.
