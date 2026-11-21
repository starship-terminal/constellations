# Components

Measured signed out on 2026-11-21 from the live DOM. Values are the computed styles in [raw/components-computed.json](raw/components-computed.json). Crops were not cut; the screenshots show the controls in place.

## Button

| State | Where | Reading |
|---|---|---|
| Store, default | header on `https://www.dji.com/sg` | white on `#0070d5`, 14px, 32px tall, padding 8px 16px, capsule radius |
| Store, hover | same | fill `#2490e3` |
| Buy Now, default | where-to-buy | white on `#0070d5`, 16px, 40px tall, radius 100px |
| Buy Now, hover | same | fill `#238fe3` |
| Learn More, homepage | hero | white 1px outline, radius 64px, 32px tall. Text colour resolved to the browser default and is not the brand blue |
| Log In, disabled | login wall | label `rgba(0,0,0,0.25)` on `rgba(0,0,0,0.04)`, 48px tall, radius 4px. Not clicked |

Pressed, loading and error were not held.

## Link

Camera Drones nav link: `rgba(0,0,0,0.85)`, 14px, weight 400, row height 64px, radius 0. Support "Learn More" computed `rgb(24, 144, 255)`, close to the brand blue and not tokenised separately.

## Text field

Support search: 16px, 32px tall, white fill, radius 0. Login password: 16px, 40px tall, radius 4px, 1px border `rgba(0,0,0,0.15)`, padding 7px 11px. Empty. Not typed into.

## Menu

Lifestyle Tech, Specialized and Explore open small white dropdowns on hover. The phone menu button (`a.navbar-control`) opens a full-screen list. See [site-tree.md](site-tree.md).

## Dialog

The login wall is a white card on a photograph at `https://account.dji.com/login`. It asks for email and password, or Apple, Google or Facebook. None of those were used. The country panel opens from Singapore and was photographed, not confirmed.

## Gaps

Text area, select, radio, switch, tabs, tooltip, toast, avatar and badge were not present on the pages measured, or were not used. The login checkbox was seen and not measured. Focus-visible was applied in the measure pass and a distinct ring was not recorded, so focus is Not captured. Icon sizes are Not captured. The product mega menu did not render for Camera Drones or Handheld.
