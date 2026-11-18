# forhers patterns

How the measured components combine into the signed-out surfaces of forhers.com, the Hims & Hers women's telehealth product. Every value cited lives in [tokens.json](tokens.json); every pattern links the screenshot or crop that shows it. Captured signed out at 1440 x 900 (mobile notes at 390 x 844). Because www.forhers.com answers this network with a Cloudflare managed challenge, the evidence is recent Wayback SSR snapshots served locally — real archived markup and sheets, scripts stripped, so hydration-owned states are recorded gaps rather than reconstructions.

## The chrome

Every page stacks the same three layers: a promo strip on top (a short offer line on the `#d5ff5d` lime — or a teal variant — with a tiny arrow chevron), the header under it (the ~71px `hers` wordmark left, category links centre, a `Log in` pill right and a menu toggle), then the footer at the bottom — a `#e8eae8` grey slab holding link columns, a row of circular social wells (Facebook, Instagram, TikTok, X icons in `rgba(0,0,0,.06)` hover wells), the `hims` sister-brand links and the legal fineprint. See [home-light-default](screenshots/home-light-default.png) and [footer-default](components/crops/footer-default.png).

The header is the only chrome the pages carry; nothing else sticks on desktop. The `Log in` control is a rounded pill (`~48px` radius) whose hover paints a `rgba(0,0,0,.06)` well — see [login-button](components/crops/login-button-default.png) and its hover row in [components.md](components.md). The slide menu and the login dropdown are hydration-owned: their toggles were measured, the panels never opened, and the gap is recorded in [components.md](components.md).

On a phone the nav collapses to the hamburger toggle and the pages gain a **sticky black action pill** — `border-radius: 9999px`, white text, fixed to the viewport foot — that carries the page's primary conversion action ([mobile-weight-loss-light-default](screenshots/mobile-weight-loss-light-default.png), [cta-primary](components/crops/cta-primary-default.png)).

## The home page (marketing stack)

The home page composes hero → bento → tiles → products → proof: a full-width hero with a fluid `CareSans` headline (~57px at 1440, `letter-spacing: -0.0625em`) over photography; a bento grid of feature cards on the sage washes (`#e4eee6`, `#f2f9f4`); category tiles linking the treatment verticals (weight loss, hair, skin, mental health, birth control); quiz-entry tiles that invite the intake flow; product cards with `CareSans` ~28px titles and price lines; an FDA/legitimacy badge row; testimonial cards; and a closing section CTA. See [home-light-full](screenshots/home-light-full.png) and the Home group in [components.md](components.md).

## The shop pages

The treatment verticals (weight-loss, hair-loss, skin-care, mental-health, birth-control, product, anti-aging, wegovy-pill, labs, benefits) share one composition: a `CareSans` page heading (about 53px at 1440), a `CareSans` section dek (~18.5px/23px), then content and **treatment cards** — each treatment card carries a product image, title, `CareSans` price line and a CTA. Actions come in three weights: the solid primary CTA, the secondary bordered CTA and the tertiary/underlined link; the measured trio is under Shop pages in [components.md](components.md) ([cta-primary](components/crops/cta-primary-default.png), [cta-secondary](components/crops/cta-secondary-default.png), [cta-underlined](components/crops/cta-underlined-default.png)).

Supporting devices repeat down the page: an **accordion** of FAQ toggles (the chevron toggles were measured; expansion is hydration-owned and uncaptured), `Read more` toggles on long copy (faint `rgba(0,0,0,.37)` text), carousel arrows and slide indicators on card rails (the rail cannot scroll without scripts — measured at rest), and a `sofia-pro` 14px/20px disclaimer block before the footer.

## The content pages

The editorial surfaces compose differently. The [blog hub](screenshots/blog-light-default.png) is a grid of article cards with topic links; an [article](screenshots/blog-post-light-default.png) is a `sofia-pro` ~62px/65px title, a 12px/20px byline block, prose at 20px/28px with inline links, and a regional-redirect card offering to switch locale. The [drug-information index](screenshots/drugs-info-light-default.png) is an A–Z of chips over a directory of `sofia-pro` ~29px/37px drug links in `#0077ab` blue.

## Forms and tools

The signed-out forms share one shape: a labelled field with an ~11px radius and a hairline border, a submit below, and a privacy disclosure line. The [BMI calculator](screenshots/bmi-calculator-light-default.png) is the fullest example — number fields for height and weight, a `#b6dd64` lime Calculate submit, a disabled button state (`rgba(0,0,0,.06)` well) and a BMI dial for the result. The [lead-capture block](screenshots/quality-light-default.png) is an email field plus submit plus a privacy note. Fields were clicked into for `focused` readings and typed-and-cleared for `filled` ones; nothing was ever submitted, so success, error and post-submit states are recorded gaps.

## Motion and focus

The motion probe ([raw/motion.json](raw/motion.json)) read transitions clustered on colour/background and transform at short durations; `prefers-reduced-motion` is partially honoured across the pages. Focus treatment varies per control — several draw a visible ring on real keyboard focus, some draw none; each entry's `focus-visible` row in [components.md](components.md) says which. `pressed` readings were forced with DevTools, so no button was ever really pressed.

## What a page does not do

Nothing behind sign-in exists in this package: no member account, no consultation or intake answers, no prescription, order or checkout surface — the quiz/intake entry points were captured at rest and never started. No form was submitted, no purchase begun, no consent banner answered. The live origin was never reached past Cloudflare's challenge, so every value is archived evidence, and the ~79 asset URLs the archive never held are missing imagery, not invention. These are recorded gaps, not design sources.
