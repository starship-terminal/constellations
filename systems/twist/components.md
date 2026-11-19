# Components

Measured on the public pages and the signed-out login. Crops are cut from the 2x public screenshots. The login page was not screenshotted: the preview browser returned "The browser is not producing screenshot frames", and headless Playwright was not opened against the login host.

## Button

The pricing page paints one primary button, Log in.

| State | Fill | Text | Radius | Padding |
|---|---|---|---|---|
| Default | `#008AA6` | `#FFFFFF`, Inter 600 17px | 8px | 9px 14px |
| Disabled | `#99D0DB` | `#FFFFFF` | 8px | login Continue with email, before an address is typed |
| Hover | gap | not forced | | |
| Pressed | gap | not forced | | |
| Focus | gap on the button itself | declared keyboard ring is on the login host | | |

Crop: [components/crops/button-primary-default.png](components/crops/button-primary-default.png).

The home page also has a Play control: `rgba(34, 40, 41, 0.8)` fill, white Inter 600 17px, radius 9999px, padding 22px 48px, height 68. It sits on the product demo and was not cropped.

## Link

Nav links, including Log in, are Inter 500 15.5px, `#222829`, padding 7px 11px, radius 6px, no fill.

Banner links are `#006780`, Inter 400 16px, no underline.

Crops: [components/crops/link-nav-default.png](components/crops/link-nav-default.png), [components/crops/link-banner-default.png](components/crops/link-banner-default.png), [components/crops/link-nav-phone.png](components/crops/link-nav-phone.png).

## Text field

The login email box is 360 by 54, radius 8px, border 1px `#C4C7C8`, padding 3px 10px 5px. The label is Graphik Web 500 12px, `rgba(0, 0, 0, 0.88)`. The input itself has no border. Mouse focus did not change the computed outline. The declared `:focus-within` rule sets the border to `--reactist-divider-primary`, which is the same `#C4C7C8`.

The field was filled with the AgentMail address and submitted. The next step asked for a full name and a password. Those were not entered.

## Tabs

Yearly and Monthly on the pricing page. Yearly starts selected: Inter 500 14px, `#222829`, padding 5px 12px, radius 6px. Monthly is `rgba(26, 45, 49, 0.64)`. Clicking Monthly selects it and changes Unlimited from US$6 to US$8. The click was local. No checkout was opened.

Crop: [components/crops/tabs-billing-yearly.png](components/crops/tabs-billing-yearly.png).

## Logo

The wordmark is teal. The fetched icon is [icons/icon.svg](icons/icon.svg), fill `#008AA6`.

Crops: [components/crops/logo-default.png](components/crops/logo-default.png), [components/crops/logo-phone.png](components/crops/logo-phone.png).

## Gaps

- Hover, pressed, loading, and error states were not forced.
- Checkbox, radio, switch, select, textarea, menu, tooltip, dialog, toast, avatar, and badge were not on these pages.
- The login page has no crop. Preview screenshots failed, and Playwright was kept off the login host.
- Google and Apple were not clicked.
- The profile form (name and password) was not submitted.
- Dark theme was declared, not painted.
