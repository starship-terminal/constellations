# Meta public site tree

Mapped from https://www.meta.com/ on 2026-11-21, signed out, before the screenshot pass. The request returned 200 and the browser landed on `https://www.meta.com/sg/`. The page title was "Meta: Shop AI Glasses, Meta Glasses & Quest Headsets (en-SG)". This is a live shop for AI glasses and Quest headsets, not a parked domain.

There is no theme switch. `color-scheme` on the root was `normal`. No email was typed. No password was typed. No form was submitted. No identity provider was clicked. Nothing was added to the bag. No purchase was started.

The locale in the path is Singapore (`/sg/`). That is the geo redirect from this machine. It is not an account location, and no region dialog was on the page.

Account sign-in is not in the header. The footer link "Meta account (single login)" points at `/account/`. That page is a stop: it was not opened for a signed-in walk. Order status, returns, and checkout are stops too.

## Promo bar

A banner sits above the header. It is a link, not a dialog.

| Control | Opens |
|---|---|
| Shop our lowest prices of the year until 30 November. Shop now | `/sg/ai-glasses/shop-all/` |

## Header

The wordmark and five nav items sit in the top bar. Four icon buttons sit on the right. They are `role="button"` divs, not links, except the bag, which is a link. Hovering AI glasses, Meta Quest, Explore Meta, and Support revealed a flyout of further links on the same page. Hovering Meta VR Glasses did not reveal a flyout; that item navigates.

| Control | Opens | Stop? |
|---|---|---|
| Meta home (wordmark) | `/sg/` | |
| AI glasses | Flyout on hover. The link itself opens `/sg/ai-glasses/` | |
| Meta Quest | Flyout on hover. The link itself opens `/sg/quest/` | |
| Meta VR Glasses | `/sg/vr-glasses/`. No flyout on this visit | |
| Explore Meta | Flyout on hover. The link itself opens `/about/` | |
| Support | Flyout on hover. The link itself opens `/help/` | |
| Search Meta Store | Search dialog on the same page. Placeholder: "Search for products or articles" | |
| Change delivery country and language – SG | Dialog "Change delivery country/region and language". Country and language selects. Cancel and Confirm | Stop. Confirm was not pressed |
| View bag items | `/bag/`. On this visit the page said "Your bag is empty" | |
| Log in | Dialog "Meta account" / "Log in to your Meta account". One button: "Sign up or log in to Meta account" | Stop. That button was not clicked |
| Skip to main content | In-page skip link. Keyboard only | |

On a 390-wide viewport the nav collapses. "Open Mobile Navigation Menu" opens a drawer with AI glasses, Meta Quest, Meta VR Glasses, Singapore (English), Explore Meta, and Support. Each row has a chevron. Those rows were not followed.

## AI glasses flyout

Hover on AI glasses opens the flyout. Moving the pointer away closes it.

| Item | Opens |
|---|---|
| Meta Glasses | `/sg/ai-glasses/meta-glasses/` |
| Ray-Ban Meta | `/sg/ai-glasses/ray-ban-meta/` |
| Ray-Ban Meta Audio | `/sg/ai-glasses/ray-ban-meta-audio/` |
| Meta Ray-Ban Display | `/sg/ai-glasses/meta-ray-ban-display/` |
| Oakley Meta | `/sg/ai-glasses/oakley-meta/` |
| About AI glasses | `/sg/ai-glasses/` |
| Compare glasses | `/sg/ai-glasses/compare/` |
| Take style quiz | `/sg/ai-glasses/shop-all/?open_style_quiz=1&style_quiz_source=nav` |
| Shop all glasses | `/sg/ai-glasses/shop-all/` |
| Accessories | `/sg/ai-glasses/accessories/` |
| Prescription | `/sg/ai-glasses/prescription/` |
| Gift guide | `/sg/gift-guide/` |
| Meta Glasses (promo tile) | `/sg/ai-glasses/meta-glasses/adventurer-tortoise-brown/` |
| 25% off Ray-Ban Meta (Gen 2) | `/sg/ai-glasses/ray-ban-meta-wayfarer-gen-2/` |
| 25% off Oakley Meta HSTN | `/sg/ai-glasses/oakley-meta-hstn-glasses/` |

## Meta Quest flyout

| Item | Opens |
|---|---|
| Meta Quest 3S | `/sg/quest/quest-3s/` |
| Meta Quest 3 | `/quest/quest-3/` |
| About Meta Quest | `/sg/quest/` |
| Compare devices | `/quest/compare/` |
| Shop all Quest | `/quest/shop-all/` |
| Accessories | `/sg/quest/shop-all/accessories/` |
| Shop all apps and games | `/experiences/` |
| Gaming | `/quest/gaming/` |
| Entertainment | `/quest/entertainment/` |
| Fitness | `/quest/fitness/` |
| Social | `/quest/social/` |
| Family | `/quest/family/` |
| Productivity | `/quest/productivity/` |
| Mixed reality | `/experiences/section/7552117818138723/` |
| Meta Horizon+ | `/meta-horizon-plus/` |

## Explore Meta flyout

These are product-family links. Facebook, Instagram, and Threads are not captured as this package. The flyout is recorded so the control is documented. The pages themselves are out of scope.

| Item | Opens | Stop? |
|---|---|---|
| Facebook | `https://www.meta.com/facebook-app/` | Out of scope for this package |
| Messenger | `https://www.meta.com/messenger/` | Out of scope |
| Instagram | `https://www.meta.com/instagram/` | Out of scope |
| WhatsApp | `https://www.meta.com/whatsapp/` | Out of scope |
| Meta Horizon | `https://horizon.meta.com/` | Leaves the shop |
| Threads | `https://www.threads.com/` | Out of scope |
| Meta AI | `https://ai.meta.com/meta-ai/` | Different product |
| Muse | `https://muse.ai/` | Different product |
| Muse Spark | `https://developer.meta.com/ai/` | Leaves the shop |
| Meta Pay | `https://www.meta.com/meta-pay/` | |
| Meta Verified | `https://www.meta.com/meta-verified/` | |
| Meta Account | `/account/` | Stop. Sign-in wall |
| Meta One | `/meta-one-plans/` | |
| About Meta | `/about/` | |
| Businesses | `https://www.facebook.com/business` | Out of scope |
| Creators | `https://creators.atmeta.com/` | Leaves the shop |
| Designers | `/sg/design-at-meta/` | |
| Developers | `https://developers.meta.com/` | Leaves the shop |
| Researchers | `https://research.facebook.com/` | Out of scope |
| Newsroom | `https://about.fb.com/news/` | Leaves the shop |

## Support flyout

| Item | Opens | Stop? |
|---|---|---|
| Find order | `/order/find/` | Stop if it asks for an order email or identity |
| Meta Quest and Quest Pro | `/help/quest/` | |
| AI glasses | `/help/ai-glasses/` | |
| Meta Portal | `/help/portal/` | |
| Accounts Centre | `/help/accounts-center/` | Stop if it asks to sign in |
| Meta Pay | `/help/meta-pay/` | |
| Policies | `/help/policies/1138173423768570/` | |
| Connected experiences | `/help/connected-experiences/` | |
| Meta Horizon | `/help/quest/1191673084645599/` | |
| Facebook, Messenger, Instagram, WhatsApp, Workplace | Help centres on facebook.com, instagram.com, whatsapp.com | Out of scope |

## Homepage body

The first screen is the shop. Controls below the header, in document order:

| Control | Opens |
|---|---|
| Shop | `/sg/ai-glasses/shop-all/` |
| Browse gift guide | `/sg/gift-guide/` |
| AI glasses (card) | `/sg/ai-glasses/shop-all/` |
| Meta VR Glasses (card) | `/sg/vr-glasses/` |
| Meta Quest (card) | `/sg/quest/` |
| Shop Meta Glasses | `/sg/ai-glasses/shop-all/?filter_tags_match[0]=meta-glasses` |
| Learn more, Meta Glasses | `/sg/ai-glasses/meta-glasses/` |
| Shop Ray-Ban Meta | `/sg/ai-glasses/shop-all/?filter_tags_match[0]=RAYBAN&filter_tags_match[1]=ray-ban-meta-gen-2&filter_tags_match[2]=ray-ban-meta-gen-3` |
| Learn more, Ray-Ban Meta | `/sg/ai-glasses/ray-ban-meta-gen-2/` |
| Shop Oakley Meta | `/sg/ai-glasses/shop-all/?filter_tags_match[0]=oakley-meta` |
| Learn more, Oakley Meta | `/sg/ai-glasses/oakley-meta/` |
| Shop Quest 3S | `/sg/quest/quest-3s/buy-now/` |
| Learn more, Quest 3S | `/sg/quest/quest-3s/` |
| Learn more, Ray-Ban Meta Audio | `/sg/ai-glasses/ray-ban-meta-audio/` |
| Learn more, Meta Ray-Ban Display | `/sg/ai-glasses/meta-ray-ban-display/` |
| Learn more, Meta VR Glasses | `/sg/vr-glasses/` |
| Learn more, Muse Charm | `/sg/muse-charm/` |
| Explore gift guide | `/sg/gift-guide/` |
| Everything we announced at Meta Connect 2026 | `/blog/meta-connect-2026-everything-we-announced/` |

A later blog card links to `about.fb.com`. That host is not photographed for this package.

## Shop filter

`/sg/ai-glasses/shop-all/` has a Filter control. It opens a dialog titled Filter, with Brand, Style, Lens type, and Personalise chips, plus Reset and Apply. Apply was not pressed. Sort by Featured is a separate control on the page and was not opened.

## Bag

`/bag/` is a page, not a drawer. On this visit it said "Your bag is empty". The footer of that page has an Email field and a Sign up button for "Get news and updates from Meta". The field was left empty. Sign up was not pressed.

## Account wall

The header Log in button opens a dialog on the same page. It is titled "Meta account". The only action is "Sign up or log in to Meta account". That button was not clicked. No identity provider was shown in the dialog. No email field was shown.

`/account/` is a marketing page titled "Meet your Meta Account". It is not a signed-in screen. Its sign-in control was not followed.

## Footer

Product columns repeat the shop links above. Account and order links are stops.

| Control | Opens | Stop? |
|---|---|---|
| Meta Help Centre | `/help/` | |
| Order status | `/order/find/` | Stop if it asks for an order email |
| Returns | `/returns/` | Stop if it asks to sign in |
| Find a product demo | `/demo/` | |
| Find a shop | `/sg/retailers/` | |
| Legal | `/sg/legal/` | |
| Terms of sale | `/sg/legal/terms-of-sale/` | |
| Meta Quest safety centre | `/sg/quest/safety-center/` | |
| Accessibility | `/sg/accessibility/` | |
| About Meta | `/about/` | |
| Meta account (single login) | `/account/` | Stop. Sign-in wall |
| Meta Verified | `/meta-verified/` | |
| Facebook, Threads, Instagram, X, YouTube | Off-site social profiles | Out of scope. Not clicked |
| Cookie policy | `facebook.com` cookie policy | Out of scope |

No cookie banner was on the page at map time. No region picker was on the page.
