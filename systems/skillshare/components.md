# Components

Public signed-out chrome on skillshare.com, measured 2026-11-19. Crops are from headless Chromium at deviceScaleFactor 2. The T3 preview browser returned "The browser is not producing screenshot frames", so these crops are not from that tab. Computed styles were read in both.

| Component | States | Crop | Values |
|---|---|---|---|
| Nav Sign Up | default, hover, focus | [nav-signup-default.png](components/crops/nav-signup-default.png) | background `{color.accent}`, label `{color.accent-ink}`, radius 4px, height 40px, padding 0 20px, type 18px/700. Hover background `{color.accent-hover}` from a real mouse hover. Focus crop did not show a distinct ring. |
| Nav Sign In | default | [nav-signin-default.png](components/crops/nav-signin-default.png) | Transparent, `{color.ink}` on the light bar, 15px/700, padding 0 10px. Focus-visible outline `{color.focus}` auto 1px. |
| Search | default | [search-default.png](components/crops/search-default.png) | 500 by 40, radius 4px, border 1px `{color.border}`, padding 0 38px. Focus did not change the border in a forced-pseudo read. Placeholder color on the light bar is `{color.ink}`. |
| Continue with Google | default, hover | [oauth-google-default.png](components/crops/oauth-google-default.png), [oauth-google-hover.png](components/crops/oauth-google-hover.png) | 320 by 40, white face, 1px `{color.border-strong}`, radius 4px, 16px/700. Hover background `{color.oauth-wash}`. |
| Continue with email | default | [oauth-email-default.png](components/crops/oauth-email-default.png) | Transparent, label `{color.link}`, 16px/700, radius 4px. Real hover underlines and fills `{color.link-wash}`. |
| Wordmark | default | [logo.svg](icons/logo.svg) | 104 by 52. Mint dots are `#55da9b`. Wordmark paths are `black`. |

Facebook and Apple buttons match Google: same size, border, radius, and type. They were measured and not cropped separately.

## Gaps

- Checkbox, radio, switch, select, textarea, tabs, menu, tooltip, toast, table, avatar, and badge were not on the public pages that loaded.
- Sign In is an in-page sheet. It was not opened, so its fields, error, and disabled states are unmeasured.
- Pressed and disabled were not observed. `CSS.forcePseudoState` did not apply the hover rules that a real mouse hover did, so pressed is left unmeasured rather than copied from a failed force.
- Browse, class, teacher, and blog pages returned a Cloudflare challenge in headless Chromium.
- No dark theme on the public surface.
