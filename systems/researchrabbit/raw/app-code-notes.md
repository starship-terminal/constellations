# ResearchRabbit app code notes

Read on 2026-10-17 from the production bundle `app.researchrabbit.ai/assets/index-QYes0gqU.js`
(3.2 MB, minified, identifiers kept). Only the short excerpts below are quoted; no bundle
code is committed. They cover what the page CSS cannot show: breakpoints applied in script,
and the toast's timing. Each heading names the identifier the tokens cite.

## 1. `breakpoints`

```js
breakpoints={xs:0,sm:640,md:768,xmd:896,lg:1024,xl:1280,"2xl":1536}
```

`useBreakpoint()` reads `window.innerWidth` on resize and returns the step it falls in;
components ask `isSmallerThan(key)` or `isLargerThan(key)`. Uses found:

| Call | Where | Effect |
|---|---|---|
| `isSmallerThan("xmd")` | `Dashboard` | Below 896px the home cards stack in one column (`flex flex-col`) instead of a row |
| `isLargerThan("md")` | `Dashboard` | The hero illustration shows only above 768px |
| `isSmallerThan("lg")` | `ExploreStep` | Below 1024px a split view falls back to the list view |
| `isSmallerThan("lg")` | `ExploreActionsInspected` | The article drawer changes layout below 1024px |
| `isSmallerThan("sm")` | `Upgrader` | The upgrade dialog's price line changes below 640px |

The Screen too small notice is CSS, not this hook: `@media (max-width: 640px)` (raw/css-vars.json).

## 2. `Toast`

```js
Toast=({config:i,onComplete:s})=>{const{message:a,info:c,icon:u,...,duration:P=4e3,durationAfterHover:me=2e3,...}=i
```

A toast stays 4000ms (`duration`), stops its timer while hovered, and leaves 2000ms after the
pointer leaves (`durationAfterHover`). It enters with `animation:"up"` and leaves with
`animation:"right"` (`AnimatedContainer`). Toasts render into `#toast-container`
(`ToastManager__Container`: fixed, centred, `bottom:12px`, `width:500px`, `max-width:85%`,
`z-index:2`). `ToastFill` adds `.error &{border:1px solid orange;}` for error toasts.

The capture raised one with `CopyContainer`:

```js
invokeToast({icon:SvgCopied,iconColor:"#fff",message:"Copied to clipboard"})
```

## 3. `WarningContainer` (article drawer)

```js
u&&u.forwardEdgeCount===0&&u.backwardEdgeCount===0?...jsx(WarningContainer,...children:"Cannot search: Citation info missing"
```

Shown in the article panel's drawer when an article has no references and no citations.

## 4. Reduced motion

A search of the whole bundle for `prefers-reduced-motion`, `reducedMotion` and
`useReducedMotion` finds nothing, and no captured stylesheet has the media
query (raw/css-vars.json `media`). The app does not change its motion when the
system asks for less.
