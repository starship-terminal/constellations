// Measures hume.ai's signed-out components on its public surfaces, in every
// state that can be reached without signing in or submitting anything.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node measure.mjs [group ...]
//
// Groups: home decision-model blog blog-post contact-form docs docs-theme
// demo login mobile. Writes raw/components-computed.json (merged, so a
// subset can be re-run) and one crop per component and state into
// components/crops/. raw/measurements.md is then built from the JSON by
// build-measurements.mjs.
//
// States:
//   hover          real mouse hover, 500ms settle for transitions
//   focus-visible  keyboard: focus, Shift+Tab, Tab, so the browser sees a keyboard focus
//   pressed        CDP CSS.forcePseudoState [active, hover]; no mouse button is pressed,
//                  so no link or button can fire
//   dark           the same element after the docs header's own Theme menu
//                  (Light / Dark / System items) repaints html.dark — dev.hume.ai
//                  is the only surface with a real theme control; www, demo
//                  and app are light-only so they have no dark state
//   opened         a resting state reached by the component's own toggle:
//                  the docs Theme menu, the mobile "Open menu" drawer
//   focused        a field clicked into — nothing is typed
//   playing        the home player's own Play press — a scripted sample
//                  call player (a media control, not a submission), Stop ends it
//   selected       a tab's own activation (benchmark categories, blog filters)
// Nothing else is typed, sent, bought or signed into. The contact form,
// newsletter Subscribe and the log-in button are measured and focused,
// never submitted; the docs Search is never queried and "Ask AI" never
// pressed; Send on the docs API playground is never pressed — issuing a
// request is a network side effect.
import fs from 'node:fs';
import path from 'node:path';
import { chromium, BASE, DOCS, DEMO, APP, M, open, closePromo, setTheme, paintedTheme, styleOf, crop, centre, domFind, patch, UA, UA_MOBILE, RAW } from './lib.mjs';
import { toggleBefore, toggleOpen, toggleRestore } from './toggle.mjs';
import { safeUrl } from '../safe-url.mjs';

const OUT = process.env.OUT_JSON || path.join(RAW, 'components-computed.json');
const out = fs.existsSync(OUT) ? JSON.parse(fs.readFileSync(OUT, 'utf8')) : {};
out._meta ??= {};
out.components ??= {};
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const save = () => fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');

const URLS = {
  home: BASE + '/',
  'decision-model': BASE + '/products/decision-model-api',
  'expression-apis': BASE + '/products/expression-apis',
  benchmark: BASE + '/benchmark',
  blog: BASE + '/blog',
  'blog-post': BASE + '/blog/hume-audio-decision-benchmarks',
  'contact-form': BASE + '/contact-form',
  docs: DOCS + '/audio-decisions/docs/overview',
  'docs-reference': DOCS + '/audio-decisions/reference/decisions/create',
  demo: DEMO + '/decision-model/file',
  login: APP + '/log-in',
};
const urlOf = (key) => URLS[key] || BASE + '/';
const pathOf = (key) => new URL(URLS[key] || BASE + '/').pathname;
const hostOf = (key) => new URL(URLS[key] || BASE + '/').host;

let page, cdp, context, current;

// ---------- state drivers ----------

async function reset() {
  // open() leaves the tab on about:blank when a reload was blocked; every
  // state after that fails here, so the saved readings are kept
  if (page.url() === 'about:blank') throw new Error('the page was lost to a blocked reload; saved readings kept');
  await page.keyboard.press('Escape').catch(() => {});
  await page.evaluate(() => document.activeElement && document.activeElement.blur && document.activeElement.blur()).catch(() => {});
  const vw = page.viewportSize()?.width ?? 1440;
  await page.mouse.move(vw - 2, 2);
  await page.waitForTimeout(300);
}

async function hover(loc) {
  await centre(loc);
  const b = await loc.boundingBox();
  if (b) { await page.mouse.move(b.x + b.width / 2, b.y + b.height / 2); await page.waitForTimeout(600); }
}

async function kbFocus(loc) {
  await loc.evaluate((el) => el.focus());
  await page.keyboard.press('Shift+Tab');
  await page.keyboard.press('Tab');
  await page.waitForTimeout(400);
  // The attempt is only evidence when focus really came back to the element
  // and paints the :focus-visible ring — anything else is a resting reading,
  // recorded under the "focus failed" via rather than claimed as a state.
  return await loc.evaluate((el) => {
    const ae = document.activeElement;
    const held = ae === el || el.contains(ae);
    let ring = false;
    try { ring = Boolean((ae && ae.matches(':focus-visible')) || el.matches(':focus-visible')); } catch { /* unpierceable */ }
    return { held, ring };
  }).catch(() => ({ held: false, ring: false }));
}

// Pick one element out of a selector's matches inside the page — marks the
// winner with data-m-mark="<tag>" and returns a locator for it. score(el, r,
// cs) returns a number, lowest wins; return Infinity to skip a match.
async function pick(p, sel, score, tag = 'pk') {
  const ok = await p.evaluate(([s, t, src]) => {
    document.querySelectorAll(`[data-m-mark="${t}"]`).forEach((n) => n.removeAttribute('data-m-mark'));
    const fn = new Function('el', 'r', 'cs', `return (${src})(el, r, cs)`);
    let best = null, bestV = Infinity;
    for (const el of document.querySelectorAll(s)) {
      const r = el.getBoundingClientRect();
      if (!r.width || !r.height) continue;
      const cs = getComputedStyle(el);
      if (cs.visibility === 'hidden' || cs.opacity === '0') continue;
      const v = fn(el, r, cs);
      if (v < bestV) { bestV = v; best = el; }
    }
    if (!best) return false;
    best.setAttribute('data-m-mark', t);
    return true;
  }, [sel, tag, score.toString()]);
  return ok ? p.locator(`[data-m-mark="${tag}"]`) : p.locator('[data-m-mark="__none__"]');
}

// CSS.forcePseudoState through CDP: the press never happens, so no link can
// navigate and no button can fire.
async function pressOn(loc) {
  // Force :active:hover on the component element itself, never the topmost
  // node at its centre (a text span or an svg), so the component's own
  // :active rule applies (2026-11 audit, finding 12-6; not run since).
  await cdp.send('DOM.getDocument').catch(() => {});
  await loc.evaluate((el) => el.setAttribute('data-press-target', '1'));
  try {
    const { result } = await cdp.send('Runtime.evaluate', { expression: `document.querySelector('[data-press-target]')`, returnByValue: false });
    // an unresolved target throws, so the state records an error instead of
    // a resting reading labelled pressed
    if (!result || !result.objectId) throw new Error('press target not resolvable');
    const { nodeId } = await cdp.send('DOM.requestNode', { objectId: result.objectId });
    if (!nodeId) throw new Error('press target has no DOM node');
    await cdp.send('CSS.forcePseudoState', { nodeId, forcedPseudoClasses: ['active', 'hover'] });
    await page.waitForTimeout(400);
    return nodeId;
  } finally {
    await loc.evaluate((el) => el.removeAttribute('data-press-target')).catch(() => {});
  }
}
const pressOff = (id) => id == null ? null : cdp.send('CSS.forcePseudoState', { nodeId: id, forcedPseudoClasses: [] }).catch(() => {});

// ---------- the component specs ----------
// find: page -> Locator. states: name -> 'hover' | 'focus-visible' |
// 'pressed' | 'dark' | 'focused' | (loc, page) => Promise<void>.
const via = {
  'hover': 'mouse hover over the element',
  'focus-visible': 'keyboard focus (Shift+Tab, Tab)',
  'pressed': 'CDP CSS.forcePseudoState(:active:hover) — no real press',
  'dark': 'same element after the docs header Theme menu\'s own Dark item repaints html.dark (the only real theme control on any captured surface)',
};

const CHROME = [
  { key: 'site-nav', group: 'Site chrome', title: 'Site navigation bar',
    desc: 'The top nav on www.hume.ai: the wordmark, Emotion Science, the Products / Solutions / Benchmarks / Resources menu buttons and the "See a Demo" action.',
    sel: 'header nav, nav', find: (p) => p.locator('nav').filter({ visible: true }).first(), states: ['default'] },
  { key: 'nav-menu-button', group: 'Site chrome', title: 'Nav menu button ("Products")',
    desc: 'A top-level nav menu button — the product/solution picker.',
    sel: 'button (text Products)', find: async (p) => await domFind(p, /^products$/i, { sel: 'button', tag: 'nm', minW: 40 }), states: ['default', 'hover', 'focus-visible'] },
  { key: 'nav-cta', group: 'Site chrome', title: '"See a Demo" button',
    desc: 'The solid primary button in the nav — measured, never followed.',
    sel: 'button, a (text See a Demo)', find: async (p) => await domFind(p, /see a demo/i, { sel: 'button, a', tag: 'cta', minW: 60 }), states: ['default', 'hover', 'focus-visible', 'pressed'] },
  { key: 'site-footer', group: 'Site chrome', title: 'Site footer',
    desc: 'The page footer: link columns, the newsletter form, the social links.',
    sel: 'footer', find: (p) => p.locator('footer').filter({ visible: true }).last(), states: ['default'] },
  { key: 'social-link', group: 'Site chrome', title: 'Social link',
    desc: 'A footer social link ("X/Twitter") — measured, never followed.',
    sel: 'footer a (social icon)', find: (p) => p.locator('footer a[href*="x.com"], footer a[href*="twitter"], footer a[href*="linkedin"], footer a[href*="github"]').filter({ visible: true }).first(), states: ['default', 'hover'] },
];

const HOME = [
  { key: 'hero-headline', group: 'Home', title: 'Hero headline',
    desc: 'The home hero h1 — the product\'s largest display style.',
    sel: 'h1', find: (p) => p.locator('h1').first(), states: ['default'] },
  { key: 'player-card', group: 'Home', title: 'Customer-call player',
    desc: 'The scripted sample-call player on the home hero ("Live answers from the call"): transport, emotion labels, the audio-pipeline diagram.',
    sel: 'div (player with transport)', find: async (p) => {
      const pl = p.locator('button[aria-label="Play"], button[aria-label="Pause"], button[aria-label="Stop"]').first();
      if (!(await pl.count())) return p.locator('[data-m-mark="__none__"]');
      return await pick(p, 'div,section', (el, r) => r.width > 200 && r.height > 100 && r.height < 800 && /answers|00:|Next|banter|Amusement|Calmness/i.test(el.innerText || '') ? r.height : Infinity, 'pc');
    }, states: ['default',
      { name: 'playing', via: 'the player\'s own Play press (a scripted sample-call player — a media control, not a submission); Stop ended it',
        // playing while the transport offers Stop or Pause
        stateOf: async () => ((await page.locator('button[aria-label="Stop"], button[aria-label="Pause"]').count()) ? 'playing' : 'stopped'),
        fn: async (loc) => {
          const pl = page.locator('button[aria-label="Play"]').first();
          if (!(await pl.count())) throw new Error('no Play button');
          await pl.click({ timeout: 4000 });
          await page.waitForTimeout(2500);
          return loc;
        }, restore: async () => {
          await page.locator('button[aria-label="Stop"], button[aria-label="Pause"]').first().click({ timeout: 4000 });
          await page.waitForTimeout(600);
        } },
    ] },
  { key: 'player-transport', group: 'Home', title: 'Player transport button',
    desc: 'The player\'s Play button — pressed for the playing state, stopped after; a media control, not a submission.',
    sel: 'button[aria-label="Play"]', find: (p) => p.locator('button[aria-label="Play"], button[aria-label="Pause"]').filter({ visible: true }).first(), states: ['default', 'hover'] },
  { key: 'scenario-button', group: 'Home', title: 'Player scenario button',
    desc: 'A "Show …" scenario chip inside the call player — its own press swaps the scripted scene.',
    sel: 'button[aria-label^="Show "]', find: (p) => p.locator('button[aria-label^="Show " i]').filter({ visible: true }).first(), states: ['default', 'hover'] },
  { key: 'benchmark-tab', group: 'Home', title: 'Benchmark category tab',
    desc: 'A benchmark category control ("Voice naturalness") — "selected" is its own activation.',
    sel: 'button (text Voice naturalness)', find: async (p) => await domFind(p, /voice naturalness/i, { sel: 'button, [role="tab"], a', tag: 'bt', minW: 60 }), states: ['default', 'hover',
      { name: 'selected', via: 'the tab\'s own activation — a local UI toggle', fn: async (loc) => {
        await loc.click({ timeout: 4000 }).catch(() => {});
        await page.waitForTimeout(900);
      } },
    ] },
  { key: 'newsletter-input', group: 'Home', title: 'Newsletter email input',
    desc: 'The "Email address" field of the footer newsletter form. "focused" is the field clicked into — nothing is typed, the form is never submitted.',
    sel: 'input[type="email"]', find: (p) => p.locator('input[type="email"], input[placeholder*="email" i]').filter({ visible: true }).first(), states: ['default', 'focused'] },
  { key: 'newsletter-button', group: 'Home', title: 'Newsletter "Subscribe" button',
    desc: 'The newsletter form\'s submit — measured, never pressed.',
    sel: 'button (text Subscribe)', find: async (p) => await domFind(p, /^subscribe$/i, { sel: 'button', tag: 'sb', minW: 60 }), states: ['default', 'hover'] },
  { key: 'section-heading', group: 'Home', title: 'Section heading',
    desc: 'A home section heading (an h2).',
    sel: 'main h2', find: (p) => p.locator('h2').filter({ visible: true }).first(), states: ['default'] },
];

const PRODUCT = [
  { key: 'product-hero', group: 'Product pages', title: 'Product hero headline',
    desc: 'The product page h1 — the display face at its working size.',
    sel: 'h1', find: (p) => p.locator('h1').first(), states: ['default'] },
  { key: 'product-cta', group: 'Product pages', title: 'Product "Contact sales" button',
    desc: 'The product page\'s primary action — measured, never followed.',
    sel: 'button, a (text Contact sales)', find: async (p) => await domFind(p, /contact sales|get started|talk to (us|hume)/i, { sel: 'button, a', tag: 'pc', minW: 80 }), states: ['default', 'hover', 'focus-visible'] },
  { key: 'product-card', group: 'Product pages', title: 'Decision demo tab control',
    desc: 'The Audio Fact / Listener Judgment / Interaction Decisions segmented tablist in the product page\'s decision demo.',
    sel: '[role="tablist"]', find: (p) => p.locator('[role="tablist"]').filter({ visible: true }).first(), states: ['default'] },
];

const BLOG = [
  { key: 'post-card', group: 'Blog', title: 'Post preview card',
    desc: 'A blog index post card: title, excerpt, meta.',
    sel: 'main a (post card)', find: async (p) => await pick(p, 'main a[href*="/blog/"], main article, main li', (el, r) => r.height > 60 && (el.innerText || '').length > 30 ? -r.width : Infinity, 'pc'), states: ['default', 'hover'] },
  { key: 'post-title-link', group: 'Blog', title: 'Post title link',
    desc: 'The post\'s title link inside an index card.',
    sel: 'main a (post title)', find: (p) => p.locator('main a[href*="/blog/"]').filter({ visible: true }).filter({ hasText: /\w{6}/ }).first(), states: ['default', 'hover'] },
  { key: 'blog-filter', group: 'Blog', title: 'Blog category filter',
    desc: 'A blog category chip ("Research"). "selected" is its own activation; the All filter restores.',
    sel: 'button, a (text Research)', find: async (p) => await domFind(p, /^research$/i, { sel: 'button, a', tag: 'bf', minW: 40 }), states: ['default', 'hover',
      { name: 'selected', via: 'the filter\'s own activation — a local UI toggle (All restored after)', fn: async (loc) => {
        // the chip has no state to read: All is restored only once this press landed
        await loc.click({ timeout: 4000 });
        await page.waitForTimeout(1200);
      }, restore: async () => {
        const all = page.locator('button, a').filter({ hasText: /^all$/i }).filter({ visible: true }).first();
        if (await all.count()) await all.click({ timeout: 4000 }).catch(() => {});
        await page.waitForTimeout(800);
      } },
    ] },
];

const PROSE = [
  { key: 'prose-h1', group: 'Prose', title: 'Article title (h1)',
    desc: 'The blog post title.', sel: 'main h1', find: (p) => p.locator('h1').first(), states: ['default'] },
  { key: 'prose-p', group: 'Prose', title: 'Body paragraph',
    desc: 'A paragraph of article prose.', sel: 'main p (sentence)', find: (p) => p.locator('main p, p').filter({ visible: true }).filter({ hasText: /\S+(\s+\S+){7,}/ }).first(), states: ['default'] },
  { key: 'prose-link', group: 'Prose', title: 'Prose link',
    desc: 'A body-text link inside the article.', sel: 'main p a', find: (p) => p.locator('main :is(p,li) a, p a').filter({ visible: true }).first(), states: ['default', 'hover'] },
  { key: 'prose-code', group: 'Prose', title: 'Inline code',
    desc: 'An inline code span in prose.', sel: 'main p code', find: (p) => p.locator('main p code, p code').filter({ visible: true }).first(), states: ['default'] },
  { key: 'prose-pre', group: 'Prose', title: 'Code block',
    desc: 'A fenced code block in the article.', sel: 'main pre', find: (p) => p.locator('main pre, pre').filter({ visible: true }).first(), states: ['default'] },
  { key: 'prose-table', group: 'Prose', title: 'Prose table',
    desc: 'A data table in the article (the benchmark post tabulates results).', sel: 'main table', find: (p) => p.locator('main table, table').filter({ visible: true }).first(), states: ['default'] },
];

const FORM = [
  { key: 'contact-field', group: 'Contact form', title: 'Contact form field',
    desc: 'A text field of the "Talk to Hume" form — clicked into for the focus look, never typed.',
    sel: 'input', find: (p) => p.locator('input[type="text"], input[type="email"], input').filter({ visible: true }).first(), states: ['default', 'focused'] },
  { key: 'contact-textarea', group: 'Contact form', title: 'Contact form textarea',
    desc: 'The message textarea, if the form carries one.',
    sel: 'textarea', find: (p) => p.locator('textarea').filter({ visible: true }).first(), states: ['default', 'focused'] },
  { key: 'contact-select', group: 'Contact form', title: 'Contact interest select',
    desc: 'The interest/topic select or radio group the form carries — its menu never opened.',
    sel: 'select, [role="combobox"], button (interest)', find: (p) => p.locator('select, [role="combobox"], [role="radiogroup"] *').filter({ visible: true }).first(), states: ['default'] },
  { key: 'contact-submit', group: 'Contact form', title: 'Contact submit button',
    desc: 'The form\'s submit — measured at rest and hover only, never pressed.',
    sel: 'button (submit)', find: async (p) => await domFind(p, /submit|send|talk to hume|contact/i, { sel: 'button', tag: 'cs', minW: 60 }), states: ['default', 'hover'] },
];

const DOCSP = [
  { key: 'docs-nav', group: 'Docs', title: 'Docs sidebar',
    desc: 'The left navigation rail on dev.hume.ai (a Fern docs shell).',
    sel: 'aside, nav', find: (p) => p.locator('aside').filter({ visible: true }).first(), states: ['default', 'dark'] },
  { key: 'docs-side-link', group: 'Docs', title: 'Docs nav section link',
    desc: 'A section link in the docs left nav ("Authentication").',
    sel: 'aside a', find: async (p) => await domFind(p, /authentication|primitives|quickstart/i, { sel: 'a', tag: 'dl', minW: 60 }), states: ['default', 'hover'] },
  { key: 'docs-search-button', group: 'Docs', title: 'Docs "Search /" button',
    desc: 'The header search field button — its dialog was never queried.',
    sel: 'button (text Search)', find: async (p) => await domFind(p, /^search/i, { sel: 'button', tag: 'ds', minW: 60 }), states: ['default', 'hover'] },
  { key: 'docs-theme-button', group: 'Docs', title: 'Docs Theme button',
    desc: 'The header\'s Theme button — the only real theme control on any captured surface. "opened" is its own press painting the Light / Dark / System menu.',
    sel: 'button[aria-label="Theme" i]', find: (p) => p.locator('button[aria-label="Theme" i]').first(), states: ['default', 'hover',
      { name: 'opened', via: 'the Theme button\'s own press (the Light / Dark / System menu open; Escape restores)', fn: async (loc) => {
        await loc.click({ timeout: 5000, force: true }).catch(() => {});
        await page.waitForTimeout(1000);
        const m = page.locator('[role="menu"], [role="listbox"], [role="radiogroup"]').filter({ hasText: /light/i }).filter({ visible: true }).last();
        const found = (await m.count()) ? m : null;
        return found;
      } },
    ] },
  { key: 'docs-cta', group: 'Docs', title: 'Docs "Get access" button',
    desc: 'The header\'s primary action — measured, never followed.',
    sel: 'a, button (text Get access)', find: async (p) => await domFind(p, /get access|start building/i, { sel: 'a, button', tag: 'dc', minW: 60 }), states: ['default', 'hover'] },
  { key: 'docs-code-block', group: 'Docs', title: 'Docs code block',
    desc: 'A fenced code block in the docs article — the surface the docs\' --code-background and syntax palette paint.',
    sel: 'pre', find: (p) => p.locator('pre').filter({ visible: true }).first(), states: ['default', 'dark'] },
  { key: 'docs-inline-code', group: 'Docs', title: 'Docs inline code',
    desc: 'An inline code span inside the docs article.',
    sel: 'code', find: (p) => p.locator('main code, article code, code').filter({ visible: true }).first(), states: ['default'] },
  { key: 'docs-toc', group: 'Docs', title: 'Docs "On this page" rail',
    desc: 'The right-rail table of contents.',
    sel: 'aside, nav (toc)', find: async (p) => await pick(p, 'aside, nav', (el, r) => /on this page/i.test(el.innerText || '') ? r.x : Infinity, 'tc'), states: ['default', 'dark'] },
  { key: 'docs-lang-tab', group: 'Docs', title: 'Docs language tab',
    desc: 'A code-sample language tab ("Python"). "selected" is its own activation.',
    sel: 'button (text Python)', find: async (p) => await domFind(p, /^python$/i, { sel: 'button, [role="tab"]', tag: 'lt', minW: 40 }), states: ['default', 'hover',
      { name: 'selected', via: 'the tab\'s own activation — a local UI toggle', fn: async (loc) => {
        await loc.click({ timeout: 4000 }).catch(() => {});
        await page.waitForTimeout(700);
      } },
    ] },
];

const DEMOG = [
  { key: 'demo-gate-card', group: 'Demo gate', title: 'Invitation gate card',
    desc: 'The demo.hume.ai gate: "Start from your invitation — the Audio Decision Model playground opens from the link in your invitation email". The playground itself is a documented boundary.',
    sel: 'main, div (gate card)', find: async (p) => await pick(p, 'main, main > div, body > div > div', (el, r) => /invitation/i.test(el.innerText || '') && r.height > 80 ? r.height : Infinity, 'gc'), states: ['default'] },
  { key: 'demo-gate-cta', group: 'Demo gate', title: 'Gate "Contact sales" link',
    desc: 'The gate\'s only action — measured, never followed.',
    sel: 'a (text Contact sales)', find: async (p) => await domFind(p, /contact sales/i, { sel: 'a, button', tag: 'gc', minW: 60 }), states: ['default', 'hover'] },
];

const LOGING = [
  { key: 'login-card', group: 'Log-in', title: 'Log-in card',
    desc: 'The app.hume.ai sign-in card — the platform\'s public boundary page; nothing past it was entered.',
    sel: 'main, div (login card)', find: async (p) => await pick(p, 'main, form, [class*="card" i], div', (el, r) => /log in|sign in/i.test(el.innerText || '') && r.width > 200 && r.width < 700 && r.height > 100 ? -r.height : Infinity, 'lc'), states: ['default'] },
  { key: 'login-email-field', group: 'Log-in', title: 'Email field',
    desc: 'The log-in Email field — clicked into for the focus look, never typed.',
    sel: 'input[type="email"], input (Email)', find: (p) => p.locator('input[type="email"], input[placeholder*="mail" i]').filter({ visible: true }).first(), states: ['default', 'focused'] },
  { key: 'login-password-field', group: 'Log-in', title: 'Password field',
    desc: 'The log-in Password field — clicked into, never typed.',
    sel: 'input[type="password"]', find: (p) => p.locator('input[type="password"]').filter({ visible: true }).first(), states: ['default', 'focused'] },
  { key: 'login-submit', group: 'Log-in', title: '"LOG IN" button',
    desc: 'The sign-in submit — measured at rest and hover only, never pressed (no credentials exist to submit).',
    sel: 'button (text LOG IN)', find: async (p) => await domFind(p, /log\s*in/i, { sel: 'button', tag: 'li', minW: 80 }), states: ['default', 'hover'] },
  { key: 'login-oauth', group: 'Log-in', title: '"SIGN IN WITH GOOGLE" button',
    desc: 'An OAuth button — measured, never pressed.',
    sel: 'button (text SIGN IN WITH GOOGLE)', find: async (p) => await domFind(p, /sign in with google/i, { sel: 'button', tag: 'lo', minW: 80 }), states: ['default', 'hover'] },
  { key: 'login-show-password', group: 'Log-in', title: '"Show password" toggle',
    desc: 'The password visibility toggle — measured; its own press would reveal a (never-typed) field.',
    sel: 'button[aria-label="Show password"]', find: (p) => p.locator('button[aria-label*="password" i]').filter({ visible: true }).first(), states: ['default', 'hover'] },
];

const MOBILE = [
  { key: 'm-nav', group: 'Site chrome (mobile)', title: 'Mobile nav',
    desc: 'The sticky header bar at 390px — the desktop nav links hide behind "Open menu".', sel: 'header',
    find: (p) => p.locator('header').first(), states: ['default'] },
  { key: 'm-menu-button', group: 'Site chrome (mobile)', title: '"Open menu" button',
    desc: 'The mobile menu trigger. "opened" is its own press painting the drawer; Escape closes it.',
    sel: 'button[aria-label="Open menu"]', find: (p) => p.locator('button[aria-label="Open menu"]').first(), states: ['default',
      { name: 'opened', via: 'the Open menu button\'s own press (the drawer open; Escape restores)', fn: async (loc) => {
        await loc.click({ timeout: 4000 }).catch(() => {});
        await page.waitForTimeout(1200);
        const m = page.locator('[role="dialog"], nav, header + div').filter({ hasText: /products|benchmarks/i }).filter({ visible: true }).last();
        return (await m.count()) ? m : null;
      } },
    ] },
];

const GROUPS = {
  home: { page: 'home', specs: [...CHROME, ...HOME] },
  'decision-model': { page: 'decision-model', specs: PRODUCT },
  'expression-apis': { page: 'expression-apis', specs: [] }, // reserved
  blog: { page: 'blog', specs: BLOG },
  'blog-post': { page: 'blog-post', specs: PROSE },
  benchmark: { page: 'benchmark', specs: [] },
  'contact-form': { page: 'contact-form', specs: FORM },
  docs: { page: 'docs', specs: DOCSP },
  'docs-reference': { page: 'docs-reference', specs: [] },
  demo: { page: 'demo', specs: DEMOG },
  login: { page: 'login', specs: LOGING },
  mobile: { page: 'home', mobile: true, specs: MOBILE },
};

// ---------- runner ----------

const b = await chromium.launch();
context = await b.newContext({ viewport: { width: 1440, height: 900 }, deviceScaleFactor: 2, userAgent: UA, locale: 'en-US' });
await patch(context);
const mobCtx = await b.newContext({ viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, userAgent: UA_MOBILE, isMobile: true, hasTouch: true, locale: 'en-US' });
await patch(mobCtx);

const wanted = process.argv.slice(2);
out._meta.read = new Date().toLocaleDateString('en-CA');
out._meta.viewport = '1440 x 900 (mobile group 390 x 844); www.hume.ai, demo.hume.ai and app.hume.ai paint a single light theme with no control; dev.hume.ai is the one surface with a real theme control — the header Theme button\'s own Light / Dark / System menu repaints html.dark, so `dark` states are measured on the painted dark docs surface and Light is restored after';
out._meta.tool = 'tools/capture/public/measure.mjs';
out._meta.sheets ??= {};

for (const [key, g] of Object.entries(GROUPS)) {
  if (wanted.length && !wanted.includes(key)) continue;
  if (!g.specs.length) continue;
  const ctx = g.mobile ? mobCtx : context;
  page = await ctx.newPage();
  page.setDefaultTimeout(8000);
  cdp = await ctx.newCDPSession(page);
  await cdp.send('DOM.enable');
  await cdp.send('CSS.enable');
  const url = urlOf(g.page);
  log('open', key, g.mobile ? '(mobile)' : '', url);
  if (!(await open(page, url, { wait: g.page === 'demo' || g.page === 'login' ? 9000 : 7000 }))) { log('  group skipped: the page never loaded'); await page.close().catch(() => {}); continue; }
  await page.addStyleTag({ content: '*{caret-color:transparent!important}' }).catch(() => {});
  // the readable sheets' transition declarations, for measurements.md
  out._meta.sheets[hostOf(g.page) + pathOf(g.page)] = await page.evaluate(() => {
    const found = [];
    for (const ss of document.styleSheets) {
      try {
        for (const r of ss.cssRules) {
          if (r.style && r.style.transition && r.style.transition !== 'all 0s') found.push({ transition: r.style.transition.slice(0, 90) });
        }
      } catch { /* cross-origin sheet */ }
    }
    return found.slice(0, 30);
  }).catch(() => []);

  for (const spec of g.specs) {
    const comp = out.components[spec.key] ??= {};
    comp.group = spec.group;
    comp.title = spec.title;
    comp.desc = spec.desc;
    comp.selector = spec.sel;
    comp.page = hostOf(g.page) + pathOf(g.page);
    comp.url = safeUrl(url);
    comp.run = new Date().toISOString();
    comp.states ??= {};
    let loc;
    // A lookup miss must not erase states a previous run already measured —
    // only a component with no good readings at all counts as missing.
    const hasStates = () => Object.values(comp.states ?? {}).some((s) => s && s.style);
    try { loc = await spec.find(page); } catch (e) {
      log(' ', spec.key, 'find failed:', e.message.split('\n')[0]);
      if (hasStates()) comp.rerunMiss = e.message.split('\n')[0]; else comp.missing = true;
      continue;
    }
    if (!(await loc.count()) || !(await loc.first().isVisible().catch(() => false))) {
      log(' ', spec.key, 'absent');
      if (hasStates()) comp.rerunMiss = 'absent on this run'; else comp.missing = true;
      continue;
    }
    delete comp.missing;
    delete comp.rerunMiss;
    loc = loc.first();
    for (const st of spec.states) {
      const name = typeof st === 'string' ? st : (st.name || 'opened');
      // pressed/dark are cleared in finally so a failed read can never leak
      // the forced state into the next measurement.
      let pressed = null;
      let toggle = null;  // a toggled state's press and its state before, for the restore
      let darkOn = false;
      try {
        await reset();
        let viaText = 'resting state';
        let readLoc = loc;
        if (st === 'hover') { await hover(readLoc); viaText = via.hover; }
        else if (st === 'focus-visible') { const f = await kbFocus(readLoc); viaText = f && (f.held || f.ring) ? via['focus-visible'] : 'focus failed'; }
        else if (st === 'focused') { await readLoc.click({ timeout: 3000 }).catch(() => readLoc.evaluate((el) => el.focus())); await page.waitForTimeout(400); viaText = 'the field clicked into'; }
        else if (st === 'pressed') { pressed = await pressOn(readLoc); viaText = via.pressed; }
        else if (st === 'dark') { if (!(await setTheme(page, 'dark'))) { log(' ', spec.key, name, 'dark never painted — skipped'); continue; } darkOn = true; viaText = via.dark; }
        else if (st && typeof st === 'object' && st.fn) { toggle = await toggleBefore(st, readLoc); const alt = await toggleOpen(st, toggle); if (alt && typeof alt.count === 'function' && await alt.count()) readLoc = alt; viaText = st.via || 'reached by the component\'s own UI toggle'; }
        else if (typeof st === 'function') { await st(readLoc); viaText = 'reached by the component\'s own UI toggle'; }
        await centre(readLoc).catch(() => {});
        const v = await styleOf(readLoc);
        v.via = viaText;
        v.crop = await crop(page, readLoc, `${spec.key}-${name}`).catch((e) => { log('  crop failed', spec.key, name, e.message.split('\n')[0]); return undefined; });
        v.run = new Date().toISOString();
        comp.states[name] = v;
        log(' ', spec.key, name, 'ok');
      } catch (e) {
        // A failed rerun records the error beside the last good reading, not
        // over it — a good saved state outlives a transient failure.
        const prev = comp.states[name];
        comp.states[name] = (prev && prev.style)
          ? { ...prev, rerunError: e.message.split('\n')[0] }
          : { error: e.message.split('\n')[0] };
        log(' ', spec.key, name, 'FAILED', e.message.split('\n')[0]);
      } finally {
        if (pressed != null) await pressOff(pressed).catch(() => {});
        // a toggled state presses its control back, so later components are
        // read in the resting layout (the ifttt pattern; 2026-11 audit, not run)
        // back to the state it had before its press (toggle.mjs): a press
        // that never landed leaves nothing to undo
        if (toggle && st.restore) {
          const refind = async () => { const a = await spec.find(page).catch(() => null); return a && await a.count() ? a.first() : null; };
          await toggleRestore(st, toggle, refind).catch((e) => log(' ', spec.key, name, 'restore failed', e.message.split('\n')[0]));
        }
        if (darkOn) {
          let back = await setTheme(page, 'light').catch(() => false);
          if (!back) back = await setTheme(page, 'light').catch(() => false);
          if (!back) {
            // A failed reset must never leak dark paint into the next
            // default reading: reload, which restores the html.light boot,
            // and re-find the element so later states measure the live page.
            log(' ', spec.key, 'light reset failed — reloading to the light boot');
            await open(page, url, { wait: 7000 }).catch(() => {});
            await page.addStyleTag({ content: '*{caret-color:transparent!important}' }).catch(() => {});
            const refound = await spec.find(page).catch(() => null);
            if (refound && await refound.count()) loc = refound.first();
          }
        }
      }
    }
    save();
  }
  await page.close();
}
await b.close();
log('done ->', OUT);
