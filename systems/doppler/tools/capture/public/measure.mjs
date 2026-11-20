// Measures doppler.com's public components in every state reachable without
// signing in, booking, buying or submitting anything.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node measure.mjs [page ...]
//
// Pages: home platform pricing demo integrations customers blog about mobile.
// Writes raw/components-computed.json (merged) and one crop per component and
// state into components/crops/; raw/measurements.md is built by
// build-measurements.mjs.
//
// doppler.com is one surface: a Next.js/Tailwind marketing site painting a
// single dark theme (warm-black #1c1624 field). Nothing is sent, booked,
// bought or signed into: the only presses are local UI toggles — the header
// Platform dropdown, the mobile menu and a pricing FAQ accordion. The demo
// form's fields were focused and sample-filled then deleted, never submitted;
// Start for Free / Sign In point off-site (dashboard.doppler.com) and were
// measured, never followed. The cookie-preferences banner is hidden, never
// answered.
import fs from 'node:fs';
import path from 'node:path';
import { BASE, M, launch, patch, open, closePromo, domFind, styleOf, crop, centre, RAW, UA, UA_MOBILE } from './lib.mjs';

const OUT = process.env.OUT_JSON || path.join(RAW, 'components-computed.json');
const out = fs.existsSync(OUT) ? JSON.parse(fs.readFileSync(OUT, 'utf8')) : {};
out._meta ??= {};
out.components ??= {};
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const save = () => fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');
const URLS = { home: '/', platform: '/platform/secrets-manager', pricing: '/pricing', demo: '/demo', integrations: '/integrations', customers: '/customers', blog: '/blog', agents: '/agents' };
let page, cdp, current, context, run, liveCtx;
const touched = new Set();
const listed = new Map();
// Routes the edge gates this run: components last measured on them keep their
// earlier readings instead of being pruned below (a blocked pass must never
// erase evidence).
const failedPages = new Set();

async function blocked() {
  return page.evaluate(() => {
    const t = (document.body && document.body.innerText) || '';
    return /performing security verification|verifying you are human|just a moment|access denied|unusual activity from your computer network|not a robot|you have been blocked|unable to access/i.test(t) || t.trim().length < 40;
  }).catch(() => true);
}

async function newPage(key, { mobile = false, wait = 8000, promo = 'close', url = null } = {}) {
  current = key;
  // Close the previous page's context before opening the next: leaving them
  // alive keeps every captured page (and its animations) running in the
  // background for the rest of the run.
  if (liveCtx) { await liveCtx.close().catch(() => {}); liveCtx = null; }
  const b = context.browser();
  const ctx = liveCtx = await b.newContext(mobile
    ? { viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, userAgent: UA_MOBILE, isMobile: true, hasTouch: true, locale: 'en-US' }
    : { viewport: { width: 1440, height: 900 }, deviceScaleFactor: 2, userAgent: UA, locale: 'en-US' });
  await patch(ctx);
  page = await ctx.newPage();
  cdp = await ctx.newCDPSession(page);
  await cdp.send('DOM.enable');
  await cdp.send('CSS.enable');
  page.setDefaultTimeout(8000);
  log('open', key, mobile ? '(mobile)' : '');
  const cleared = await open(page, url || BASE + URLS[key], { wait, promo });  // false: the bot check did not clear (lib.mjs)
  if (!cleared || (await blocked())) { log('  BLOCKED', key); failedPages.add(key); await page.close(); await ctx.close(); return false; }
  await page.addStyleTag({ content: '*{caret-color:transparent!important}' });
  return true;
}

// Fixed/sticky chrome with paint order: the z-index map of the page's bars and
// overlays. Recorded per page into _meta.chrome.
async function chrome(key) {
  const z = await page.evaluate(() => {
    const els = [...document.querySelectorAll('body *')];
    const seen = [];
    for (const el of els) {
      const cs = getComputedStyle(el);
      if (cs.position !== 'fixed' && cs.position !== 'sticky') continue;
      const r = el.getBoundingClientRect();
      if (r.width < 40 || r.height < 10) continue;
      seen.push({ node: el.tagName.toLowerCase() + '.' + String(el.className).split(' ')[0].slice(0, 60), z: cs.zIndex, pos: cs.position, rect: `${r.width | 0}x${r.height | 0}@${r.x | 0},${r.y | 0}`, text: (el.innerText || '').slice(0, 40).replace(/\n/g, '|') });
    }
    return seen.sort((a, b) => (parseInt(b.z) || 0) - (parseInt(a.z) || 0)).slice(0, 20);
  }).catch(() => []);
  out._meta.chrome ??= {};
  out._meta.chrome[key] = z;
}

async function reset() {
  await page.evaluate(() => document.activeElement && document.activeElement.blur && document.activeElement.blur()).catch(() => {});
  const vw = page.viewportSize()?.width ?? 1440;
  await page.mouse.move(vw - 2, 2);
  await page.waitForTimeout(250);
}

async function kbFocus(loc) {
  await loc.evaluate((el) => el.focus());
  await page.keyboard.press('Shift+Tab');
  await page.keyboard.press('Tab');
  let ok = await loc.evaluate((el) => document.activeElement === el || el.contains(document.activeElement));
  let how = 'Shift+Tab, Tab';
  if (!ok) {
    await page.keyboard.press('Shift');
    await loc.evaluate((el) => el.focus());
    ok = await loc.evaluate((el) => document.activeElement === el);
    how = 'keydown then focus()';
  }
  await page.waitForTimeout(350);
  return ok ? how : 'focus failed';
}

async function forcePseudo(loc, classes) {
  await page.evaluate(() => document.querySelectorAll('[data-m-force]').forEach((n) => n.removeAttribute('data-m-force')));
  await loc.evaluate((el) => el.setAttribute('data-m-force', '1'));
  const { root } = await cdp.send('DOM.getDocument', { depth: 0 });
  const { nodeId } = await cdp.send('DOM.querySelector', { nodeId: root.nodeId, selector: '[data-m-force]' });
  await cdp.send('CSS.forcePseudoState', { nodeId, forcedPseudoClasses: classes });
  await page.waitForTimeout(400);
  return async () => { await cdp.send('CSS.forcePseudoState', { nodeId, forcedPseudoClasses: [] }).catch(() => {}); };
}

function comp(key, meta) {
  const c = (out.components[key] ??= { states: {} });
  Object.assign(c, { page: current, run, url: URLS[current] && BASE + URLS[current] }, meta);
  touched.add(key);
  c.states ??= {};
  return c;
}

// A failed recapture must not erase an earlier good reading: keep the saved
// state and record the failed attempt beside it (under this run's date), the
// same way a missing target keeps earlier states under their own provenance.
function recordError(c, state, e, prevRun) {
  const err = String(e.message || e).slice(0, 200);
  const earlier = c.states[state];
  if (earlier && !earlier.error) {
    if (prevRun) earlier.run = prevRun;
    earlier.recaptureFailed = run;
    earlier.recaptureError = err;
  } else {
    c.states[state] = { error: err };
  }
}

async function measure(key, state, target, opts = {}) {
  const loc = target.filter({ visible: true }).first();
  const c = out.components[key];
  try {
    const s = await styleOf(loc);
    let file;
    if (opts.crop !== false) {
      try {
        file = await crop(page, (opts.cropLoc || loc).filter({ visible: true }).first(), `${key}-${state}`, opts.pad ?? 8);
      } catch (e) { s.cropError = String(e.message || e).slice(0, 120); }
    }
    c.states[state] = { ...s, crop: file, via: opts.via };
    if (opts.extra) c.states[state].extra = await opts.extra(loc);
    log('  ', key, state, s.rect.w + 'x' + s.rect.h);
  } catch (e) {
    recordError(c, state, e, opts.prevRun);
    log('  !', key, state, String(e.message).slice(0, 120));
  }
}

async function S(key, target, list, meta = {}, opts = {}) {
  const prev = out.components[key];
  const keep = prev && Object.keys(prev.states || {}).length ? { page: prev.page, run: prev.run, url: prev.url } : null;
  comp(key, { title: meta.title, group: meta.group, desc: meta.desc, selector: meta.sel });
  if (!listed.has(key)) listed.set(key, new Set());
  for (const st of list) listed.get(key).add(st);
  delete out.components[key].missing;
  if (opts.open) { await reset(); try { await opts.open(); } catch (e) { log('  ! open failed', key, String(e.message).slice(0, 80)); } }
  const loc = target.filter({ visible: true }).first();
  if (!(await loc.count())) {
    const has = Object.keys(out.components[key].states || {}).length > 0;
    log('  ! missing', key, has ? '(earlier states kept)' : '');
    // Keep earlier evidence under its own provenance: the states stay but the
    // entry keeps its original page/run/url and records the miss, so a re-run
    // never republishes old readings under a new date.
    if (!has) out.components[key].missing = true;
    else { Object.assign(out.components[key], keep); out.components[key].recaptureMissed = run; }
    return;
  }
  for (const st of list) {
    let undo, via;
    try {
      if (!opts.noReset) await reset();
      if (!opts.noScroll) await centre(loc);
      if (opts.before?.[st]) via = await opts.before[st](loc);
      if (st === 'hover') {
        await (opts.hoverLoc || loc).filter({ visible: true }).first().hover({ timeout: 5000 }).catch(() => (opts.hoverLoc || loc).filter({ visible: true }).first().hover({ timeout: 5000, force: true }));
        await page.waitForTimeout(450);
        via = 'mouse hover';
      } else if (st === 'focus-visible') {
        via = await kbFocus((opts.focusLoc || loc).filter({ visible: true }).first());
      } else if (st === 'pressed') {
        undo = await forcePseudo((opts.pressLoc || loc).filter({ visible: true }).first(), ['active', 'hover']);
        via = 'CDP forcePseudoState :active:hover';
      } else if (st === 'focused') {
        const fld = (opts.fieldLoc || loc).filter({ visible: true }).first();
        // A range input's whole track is clickable: clicking it to focus also
        // moves the thumb, so the "focused" reading would capture a changed
        // value. Focus sliders by el.focus() and click everything else.
        const isRange = await fld.evaluate((el) => el.tagName === 'INPUT' && (el.getAttribute('type') || '').toLowerCase() === 'range').catch(() => false);
        if (isRange) {
          await fld.evaluate((el) => el.focus());
          via = 'focus() (a click would move the thumb)';
        } else {
          await fld.click({ timeout: 4000 }).catch(() => fld.evaluate((el) => el.focus()));
          via = 'clicked into the field';
        }
        await page.waitForTimeout(400);
      } else if (st === 'filled') {
        const f = (opts.fieldLoc || loc).filter({ visible: true }).first();
        await f.click({ timeout: 4000 });
        await page.keyboard.type(opts.fillText || 'name@example.com', { delay: 10 });
        await page.waitForTimeout(500);
        undo = async () => { await f.focus(); await page.keyboard.press('ControlOrMeta+a'); await page.keyboard.press('Backspace'); await page.waitForTimeout(300); };
        via = `typed "${opts.fillText || 'name@example.com'}", then deleted; nothing sent`;
      } else if (st === 'selected') {
        if (opts.noToggle) via = 'held selected by an earlier toggle';
        else { await toggle(loc, { allowLink: opts.allowLink }); await page.waitForTimeout(900); via = 'own toggle'; }
      } else via = via || 'at rest';
      await measure(key, st, loc, { ...opts, via, prevRun: keep && keep.run });
    } catch (e) {
      recordError(out.components[key], st, e, keep && keep.run);
      log('  !', key, st, String(e.message).slice(0, 120));
    }
    if (undo) await undo().catch(() => {});
    if (opts.after?.[st]) await opts.after[st](loc).catch(() => {});
  }
  await reset();
}

// Clicks a UI toggle (dropdown, menu, accordion, chip). Refuses a submit
// button and any control whose text names an action this kit must never take.
const NEVER = /^(send|submit|sign in|log ?in|login|create|add|download|buy|purchase|pay|checkout|join|subscribe|save|apply|accept|reject|start|get started|claim|share|export|continue|claim this offer|try again|next|confirm|schedule event|i understand|decline|choose a time|opt-?out|start for free|get demo|book|request integration)$/i;
async function toggle(loc, { allowLink = false } = {}) {
  const l = loc.filter({ visible: true }).first();
  const t = await l.evaluate((el) => ({ tag: el.tagName, type: el.getAttribute('type'), text: (el.innerText || el.getAttribute('aria-label') || '').trim() }));
  if (t.type === 'submit' || NEVER.test(t.text) || (t.tag === 'A' && !allowLink)) throw new Error(`toggle refused: ${t.tag} "${t.text}"`);
  await l.click({ timeout: 4000 }).catch(() => l.evaluate((el) => el.click()));
}

const q = (sel) => page.locator(sel);
const B4 = ['default', 'hover', 'focus-visible', 'pressed'];

async function sheetsFor(key) {
  const res = await page.evaluate(() => {
    const transitions = [];
    const walk = (rules) => {
      for (const r of rules) {
        if (r.cssRules && !r.selectorText) { walk(r.cssRules); continue; }
        if (!r.style) continue;
        const t = r.style.getPropertyValue('transition');
        const a = r.style.getPropertyValue('animation');
        if (t || a) transitions.push({ selector: (r.selectorText || '').slice(0, 160), transition: t, animation: a });
      }
    };
    for (const ss of document.styleSheets) { try { walk(ss.cssRules); } catch { /* cross-origin */ } }
    return transitions;
  });
  out._meta.sheets ??= {};
  out._meta.sheets[key] = res;
}

// Whether the page paints a different transition under prefers-reduced-motion:
// the same selector read in both a no-preference and a reduce context, on an
// element that actually transitions, so the delta is a real comparison — not
// a restatement of an element with no motion either way.
async function reducedMotion(key, sel) {
  out._meta.reducedMotion ??= {};
  const probe = async (reduced) => {
    const b = context.browser();
    const ctx = await b.newContext({ viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1, userAgent: UA, locale: 'en-US', reducedMotion: reduced ? 'reduce' : 'no-preference' });
    await patch(ctx);
    const p = await ctx.newPage();
    try {
      await p.goto(BASE + URLS[key], { waitUntil: 'domcontentloaded', timeout: 90000 }).catch(() => {});
      await p.waitForTimeout(7000);
      await closePromo(p);
      return await p.evaluate((s) => {
        const el = document.querySelector(s);
        if (!el) return null;
        const cs = getComputedStyle(el);
        return { transitionProperty: cs.transitionProperty, transitionDuration: cs.transitionDuration,
                 transitionTimingFunction: cs.transitionTimingFunction,
                 animationName: cs.animationName, animationDuration: cs.animationDuration,
                 scrollBehavior: getComputedStyle(document.documentElement).scrollBehavior };
      }, sel).catch(() => null);
    } finally {
      await ctx.close();
    }
  };
  try {
    const noPreference = await probe(false);
    const reduce = await probe(true);
    out._meta.reducedMotion[key] = { selector: sel, noPreference, reduce };
  } catch (e) { out._meta.reducedMotion[key] = { selector: sel, error: String(e).slice(0, 120) }; }
}

// Marks the nearest ancestor of the element matching sel that paints a fill
// or a background image, or falls back to marking a painted descendant.
// markPainted() returns a locator that matches nothing on a miss (never null), so `x || fallback`
// never fell back; orElse() takes x when it matches and the fallback only when it does not.
async function orElse(preferred, fallback) {
  return preferred && (await preferred.count().catch(() => 0)) ? preferred : fallback;
}

async function markPainted(sel, tag, { maxUp = 8, minW = 100, minH = 60, descend = false } = {}) {
  const ok = await page.evaluate(([s, t, up, w, h, desc]) => {
    document.querySelectorAll(`[data-m-mark="${t}"]`).forEach((n) => n.removeAttribute('data-m-mark'));
    const el = [...document.querySelectorAll(s)].find((n) => { const r = n.getBoundingClientRect(); return r.width > 0 && r.height > 0; });
    if (!el) return false;
    const paints = (cs) => cs.backgroundColor !== 'rgba(0, 0, 0, 0)' || cs.backgroundImage !== 'none';
    if (!desc) for (let n = el, i = 0; n && i < up; n = n.parentElement, i++) {
      const cs = getComputedStyle(n);
      const r = n.getBoundingClientRect();
      if (r.width >= w && r.height >= h && paints(cs)) { n.setAttribute('data-m-mark', t); return true; }
    }
    if (desc) {
      // The painted layer sits beside the content, not above it: find the
      // biggest painted element under the element's own section.
      const sec = el.closest('section') || el.parentElement;
      const cands = [...(sec || el).querySelectorAll('*')].filter((n) => {
        const r = n.getBoundingClientRect(); const cs = getComputedStyle(n);
        return r.width >= w && r.height >= h && paints(cs);
      }).sort((a, b) => b.getBoundingClientRect().width * b.getBoundingClientRect().height - a.getBoundingClientRect().width * a.getBoundingClientRect().height);
      if (cands[0]) { cands[0].setAttribute('data-m-mark', t); return true; }
    }
    return false;
  }, [sel, tag, maxUp, minW, minH, descend]);
  return ok ? page.locator(`[data-m-mark="${tag}"]`) : page.locator('[data-m-mark="__none__"]');
}

const G = {
  shell: 'Shell and navigation', hero: 'Home hero', home: 'Home', pricing: 'Pricing',
  demo: 'Demo request', integrations: 'Integrations', customers: 'Customers',
  blog: 'Blog', agents: 'Agents', footer: 'Footer', mobile: 'Mobile (390 wide)',
};

async function home() {
  if (!(await newPage('home'))) return;
  await sheetsFor('home');
  await chrome('home');
  const g = G.shell;
  await S('header', q('header').filter({ visible: true }).first(), ['default'], { group: g, title: 'Header', desc: 'The sticky marketing header: a 72px warm-black bar with a 1px glow-stroke border and 16px bottom radii — wordmark, the Platform/Solutions/Resources dropdowns, Doppler for Agents, Customers, Pricing, Get Demo, the green Start-for-Free pill and Sign In.', sel: 'header' }, { noScroll: true });
  await S('logo', q('header a[href="/"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Logo', desc: 'The Doppler wordmark anchor.', sel: 'header a[href="/"]' }, { noScroll: true });
  await S('nav-trigger', q('header nav button, header button').filter({ hasText: /^\s*Platform\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Nav trigger', desc: 'The Platform button that opens the header mega-menu; toggled, never followed.', sel: 'header nav button "Platform"' }, { noScroll: true });
  await S('nav-link', q('header nav a').filter({ hasText: /^\s*Pricing\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Nav link', desc: 'The plain Pricing header link.', sel: 'header nav a "Pricing"' }, { noScroll: true });
  await S('nav-demo', q('header a').filter({ hasText: /^\s*Get Demo\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Demo link', desc: 'The Get-Demo header action; measured never followed.', sel: 'header a "Get Demo"' }, { noScroll: true });
  await S('nav-cta', q('header a').filter({ hasText: /Start for Free/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Nav CTA', desc: 'The fluorescent-green Start-for-Free pill (points off-site to dashboard.doppler.com/register); measured never followed.', sel: 'header a "Start for Free"' }, { noScroll: true });
  await S('nav-signin', q('header a').filter({ hasText: /^\s*Sign In\s*$/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Sign-in link', desc: 'The bordered Sign-In header action (points off-site to dashboard.doppler.com/login); measured never followed.', sel: 'header a "Sign In"' }, { noScroll: true });
  // The Platform trigger opens the mega-menu on hover; keep the pointer put
  // while the panel and one of its links are read (noReset), then Escape.
  try {
    const t = q('header nav button, header button').filter({ hasText: /^\s*Platform\s*$/ }).filter({ visible: true }).first();
    if (await t.count()) { await t.hover({ timeout: 5000 }); await page.waitForTimeout(1200); }
  } catch (e) { log('  ! dropdown hover failed', String(e.message).split('\n')[0]); }
  const panel = await markPainted('header a[href*="platform"], header a[href*="secrets-manager"], header a[href*="govern"]', 'm-panel', { minW: 300, minH: 150 }).catch(() => null);
  await S('nav-dropdown', await orElse(panel, q('header div[class*="absolute"][class*="rounded"], header [class*="dropdown" i]').filter({ visible: true }).first()), ['default'], { group: g, title: 'Nav dropdown', desc: 'The Platform mega-menu panel, opened by its own trigger.', sel: 'header platform panel' }, { noScroll: true, noReset: true });
  const openPanel = async () => {
    const t = q('header nav button, header button').filter({ hasText: /^\s*Platform\s*$/ }).filter({ visible: true }).first();
    if (await t.count()) { await t.hover({ timeout: 5000 }).catch(() => {}); await page.waitForTimeout(900); }
  };
  // noReset: moving the pointer away collapses the hover-opened panel and the
  // menu link vanishes; the panel stays open while the pointer rests on it.
  await S('menu-link', q('header a').filter({ hasText: /Secrets manager|Govern access|Develop locally|CICD/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Menu link', desc: 'A feature link inside the opened mega-menu.', sel: 'header menu a' }, { noScroll: true, noReset: true,
    open: openPanel,
    before: { default: openPanel, 'focus-visible': openPanel, pressed: openPanel } });
  await page.keyboard.press('Escape'); await page.waitForTimeout(400);
  const h = G.hero;
  await S('hero-title', q('h1').filter({ visible: true }).first(), ['default'], { group: h, title: 'Hero headline', desc: 'The display headline ("One platform. Every secret. Human or AI.") with a lilac-to-carmine gradient line.', sel: 'h1' }, { noScroll: true });
  await S('hero-sub', q('p').filter({ hasText: /engineer|agents|secrets/i }).filter({ visible: true }).first(), ['default'], { group: h, title: 'Hero copy', desc: 'The lede paragraph under the headline.', sel: 'hero lede' });
  await S('hero-cta', q('main a, section a, a').filter({ hasText: /Start for Free/i }).filter({ visible: true }).last(), B4, { group: h, title: 'Hero CTA', desc: 'The green Start-for-Free button in the hero; measured never followed.', sel: 'hero "Start for Free"' });
  // No "Take a self-guided tour" button exists in the DOM: the tour affordance
  // is painted inside the dashboard-mock image. Recorded as a gap, not a spec.
  const s = G.home;
  await S('h2-section', q('h2').filter({ visible: true }).first(), ['default'], { group: s, title: 'Section heading', desc: 'A gradient-text section heading ("Built for every identity").', sel: 'first h2' });
  await S('feature-card', q('.interactive-card').filter({ visible: true }).first(), ['default'], { group: s, title: 'Feature card', desc: 'A .interactive-card tile under a section heading (the "Built for every identity" cards).', sel: '.interactive-card on /' });
  save();
}

async function pricing() {
  if (!(await newPage('pricing', { wait: 11000 }))) return;
  await sheetsFor('pricing');
  await chrome('pricing');
  const g = G.pricing;
  await S('pricing-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Pricing title', desc: 'The "One bill. No surprises." display heading.', sel: 'h1 on /pricing' }, { noScroll: true });
  await S('seat-slider', q('input[type="range"]').filter({ visible: true }).first(), ['default', 'focused'], { group: g, title: 'Seat slider', desc: 'The seats range input in the pricing calculator; focused, never dragged past a checkout.', sel: 'input[type=range]' });
  await S('seat-field', q('input[type="text"]').filter({ visible: true }).first(), ['default', 'focused'], { group: g, title: 'Spend field', desc: 'The "$100,000" currency field beside the seats slider; focused only.', sel: 'pricing calculator input[type=text]' });
  await S('plan-name', q('h2, h3, [class*="plan" i]').filter({ hasText: /^\s*(Developer|Team|Enterprise)\s*$/ }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Plan name', desc: 'A plan card\'s name.', sel: 'plan name' });
  await S('plan-price', page.getByText(/^\s*\$\d+\s*\/\s*mo|Custom pricing|Free for \d+ days/i).filter({ visible: true }).first(), ['default'], { group: g, title: 'Plan price', desc: 'A plan card\'s price figure (e.g. "$8/mo per additional user").', sel: 'plan price leaf' });
  await S('plan-cta', q('.interactive-card a, .interactive-card button').filter({ hasText: /Start|Free|Talk|Contact|Get/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Plan CTA', desc: 'A plan card\'s action; measured never followed.', sel: '.interactive-card CTA on /pricing' });
  await S('plan-badge', q('span, div').filter({ hasText: /^\s*MOST POPULAR\s*$/i }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Plan badge', desc: 'The MOST POPULAR chip on the Team card.', sel: '"MOST POPULAR" chip' });
  const planCard = await markPainted('h2, h3', 'm-plan', { minW: 200, minH: 300 }).catch(() => null);
  await S('plan-card', await orElse(planCard, q('[class*="card" i]').filter({ visible: true }).first()), ['default'], { group: g, title: 'Plan card', desc: 'A pricing plan card (the painted ancestor of the plan name).', sel: 'plan card' });
  await S('faq-item', q('button[aria-expanded="false"]').filter({ hasText: /What does Doppler do|How long does it take|Is Doppler secure/i }).filter({ visible: true }).first(), B4, { group: g, title: 'FAQ accordion', desc: 'A closed FAQ row (aria-expanded=false); the open state below is a row expanded by its own toggle.', sel: 'pricing FAQ button, closed' });
  // The first FAQ row is open by default; if nothing is expanded, open a row
  // by its own toggle — a local UI state, nothing sent.
  try {
    const open = q('button[aria-expanded="true"]').filter({ hasText: /What does Doppler do|How long does it take|Is Doppler secure/i }).filter({ visible: true }).first();
    if (!(await open.count())) {
      const f = q('button[aria-expanded="false"]').filter({ hasText: /What does Doppler do|How long does it take|Is Doppler secure/i }).filter({ visible: true }).first();
      if (await f.count()) { await f.click({ timeout: 5000 }).catch(() => f.evaluate((el) => el.click())); await page.waitForTimeout(900); }
    }
  } catch (e) { log('  ! faq open failed', String(e.message).split('\n')[0]); }
  await S('faq-open', q('button[aria-expanded="true"]').filter({ hasText: /What does Doppler do|How long does it take|Is Doppler secure/i }).filter({ visible: true }).first().locator('xpath=..'), ['default'], { group: g, title: 'FAQ accordion, open', desc: 'An expanded FAQ row container (question plus revealed answer).', sel: 'aria-expanded=true FAQ row container' });
  save();
}

async function demo() {
  if (!(await newPage('demo', { wait: 11000 }))) return;
  await sheetsFor('demo');
  await chrome('demo');
  const g = G.demo;
  await S('demo-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Demo title', desc: 'The demo-request display heading.', sel: 'h1 on /demo' }, { noScroll: true });
  const card = await markPainted('form, input, select', 'm-demo', { minW: 300, minH: 300 }).catch(() => null);
  await S('demo-card', await orElse(card, q('form, [class*="card" i]').filter({ visible: true }).first()), ['default'], { group: g, title: 'Demo card', desc: 'The "See Doppler in action" form panel; never submitted.', sel: 'demo form panel' });
  await S('demo-field', q('form input[type="text"], input[type="text"]').filter({ visible: true }).first(), ['default', 'focused', 'filled'], { group: g, title: 'Text field', desc: 'The First-name input; sample text was typed and deleted, nothing sent.', sel: 'demo input[type=text]' });
  await S('demo-email', q('input[type="email"]').filter({ visible: true }).first(), ['default', 'focused'], { group: g, title: 'Email field', desc: 'The company-email input; focused only, never filled or submitted.', sel: 'input[type=email]' });
  await S('demo-select', q('select').filter({ visible: true }).first(), ['default', 'focused'], { group: g, title: 'Select', desc: 'The Company-Size select; focused, never opened (a native list would paint).', sel: 'select' });
  await S('demo-submit', q('button').filter({ hasText: /Choose a Time/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Submit button', desc: 'The Choose-a-Time submit; measured, never pressed (a press would submit).', sel: 'button "Choose a Time"' });
  await S('check-item', q('li, p').filter({ hasText: /Cloud or on-prem|Eliminating secrets sprawl|least-privilege/i }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Checklist row', desc: 'A green-check benefit row beside the form.', sel: 'demo checklist li' });
  save();
}

async function integrations() {
  if (!(await newPage('integrations', { wait: 11000 }))) return;
  await sheetsFor('integrations');
  await chrome('integrations');
  const g = G.integrations;
  await S('integrations-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Integrations title', desc: 'The integrations display heading.', sel: 'h1 on /integrations' }, { noScroll: true });
  await S('search-field', q('input[placeholder*="Search" i], input[type="search"], input').filter({ visible: true }).first(), ['default', 'focused', 'filled'], { group: g, title: 'Search field', desc: 'The integrations search input; sample text was typed and deleted, nothing sent.', sel: 'input "Search"' }, { fillText: 'aws' });
  await S('filter-chip', q('button').filter({ hasText: /^\s*(WEBHOOKS|KUBERNETES|SYNCS|SCIM)\s*$/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Filter chip', desc: 'An integration-category filter button; measured, never toggled (a toggle would filter the grid).', sel: 'category filter button' });
  const icard = await markPainted('a[href*="/integrations/"], [class*="card" i]', 'm-int', { minW: 150, minH: 80 }).catch(() => null);
  await S('integration-card', await orElse(icard, q('a[href*="/integrations/"]').filter({ visible: true }).first()), ['default', 'hover'], { group: g, title: 'Integration card', desc: 'An integration tile (a provider name and glyph) in the grid; never followed.', sel: 'integration tile' });
  await S('request-integration', q('a, button').filter({ hasText: /Request Integration/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Request link', desc: 'The Request-Integration action; measured, never followed.', sel: '"Request Integration"' });
  save();
}

async function blog() {
  if (!(await newPage('blog', { wait: 11000 }))) return;
  await sheetsFor('blog');
  await chrome('blog');
  const g = G.blog;
  await S('blog-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Blog title', desc: 'The blog index heading.', sel: 'h1 on /blog' }, { noScroll: true });
  await S('cat-chip', q('button, a').filter({ hasText: /^\s*(COMPANY|DEVREL|ENGINEERING|PRODUCT|TUTORIALS|SECURITY)\s*$/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Category chip', desc: 'A blog-category filter chip; measured, never toggled. Labels are sentence-case in the DOM, painted uppercase by text-transform.', sel: 'blog category button' });
  await S('cat-chip-active', q('button, a').filter({ hasText: /^\s*ALL\s*$/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Category chip, active', desc: 'The ALL filter chip, selected at rest (no toggle needed for the selected state).', sel: 'blog "ALL" chip' });
  const pcard = await markPainted('a[href*="/blog/"], article, h2, h3', 'm-post', { minW: 200, minH: 120 }).catch(() => null);
  await S('post-card', await orElse(pcard, q('a[href*="/blog/"], article').filter({ visible: true }).first()), ['default', 'hover'], { group: g, title: 'Post card', desc: 'A blog post card in the index grid; never followed.', sel: 'post card' });
  await S('page-number', q('button, a').filter({ hasText: /^\s*[2-9]\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Pagination button', desc: 'A numbered pagination control; measured, never followed.', sel: 'pagination "2"' });
  await S('read-more', q('a').filter({ hasText: /^Read More$/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Read-More link', desc: 'The Read-More card link under each post; measured never followed.', sel: 'a "Read More"' });
  save();
}

async function customers() {
  if (!(await newPage('customers', { wait: 11000 }))) return;
  await sheetsFor('customers');
  await chrome('customers');
  const g = G.customers;
  await S('customers-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Customers title', desc: 'The "Doppler effect" customers heading.', sel: 'h1 on /customers' }, { noScroll: true });
  await S('industry-chip', q('button, a').filter({ hasText: /^\s*(AI|Software development|Marketplace|Health|Insurtech)\s*$/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Industry chip', desc: 'A customer-industry filter chip; measured, never toggled.', sel: 'industry filter button' });
  const ccard = await markPainted('a[href*="case-stud"], [class*="card" i]', 'm-case', { minW: 200, minH: 120 }).catch(() => null);
  await S('case-card', await orElse(ccard, q('a[href*="case-stud"]').filter({ visible: true }).first()), ['default', 'hover'], { group: g, title: 'Case-study card', desc: 'A customer case-study card; never followed.', sel: 'case-study card' });
  save();
}

async function agents() {
  if (!(await newPage('agents', { wait: 11000 }))) return;
  await sheetsFor('agents');
  await chrome('agents');
  const g = G.agents;
  await S('agents-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Agents title', desc: 'The "Run AI coding agents with Doppler" heading.', sel: 'h1 on /agents' }, { noScroll: true });
  await S('agents-cta', q('a, button').filter({ hasText: /Pick Your Tool/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Agents CTA', desc: 'The "Pick Your Tool" hero call-to-action on the agents landing (an in-page scroll link); measured never followed.', sel: 'a "Pick Your Tool"' });
  await S('agents-card', q('.interactive-card').filter({ visible: true }).first(), ['default'], { group: g, title: 'Agents card', desc: 'A "Why Doppler for agents" / "Pick your tool" .interactive-card tile.', sel: '.interactive-card on /agents' });
  await S('code-chip', q('span.text-code, [class*="text-code"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Inline code chip', desc: 'An inline span.text-code ("doppler run") painted as a rounded black4 mono chip; the only real code element on the public pages — CLI samples elsewhere are baked into mock imagery.', sel: 'span.text-code on /agents' });
  save();
}

async function platform() {
  if (!(await newPage('platform', { wait: 11000 }))) return;
  await sheetsFor('platform');
  const g = G.home;
  await S('platform-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Platform title', desc: 'The secrets-manager product-page heading.', sel: 'h1 on /platform/secrets-manager' }, { noScroll: true });
  await S('platform-card', q('.interactive-card').filter({ visible: true }).first(), ['default'], { group: g, title: 'Platform feature card', desc: 'A .interactive-card feature tile on the secrets-manager page.', sel: '.interactive-card on /platform/secrets-manager' });
  save();
}

async function footer() {
  if (!(await newPage('home', { wait: 6000 }))) return;
  const g = G.footer;
  await page.evaluate(() => scrollTo(0, document.documentElement.scrollHeight));
  await page.waitForTimeout(1500);
  await S('footer', q('footer').filter({ visible: true }).last(), ['default'], { group: g, title: 'Footer', desc: 'The marketing footer: link columns, legal, social icons and the Cookie Preferences button.', sel: 'footer' }, { noScroll: true });
  await S('footer-link', q('footer a').filter({ hasText: /\S/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Footer link', sel: 'footer a' }, { noScroll: true });
  await S('cookie-button', q('footer button, footer a, button').filter({ hasText: /Cookie Preferences/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Cookie button', desc: 'The footer Cookie-Preferences button; measured, never pressed (it would open the consent panel).', sel: '"Cookie Preferences" button' }, { noScroll: true });
  save();
}

async function mobile() {
  if (!(await newPage('mobile', { mobile: true, url: BASE + '/' }))) return;
  await chrome('mobile');
  const g = G.mobile;
  await S('m-header', q('header').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile header', sel: 'header at 390' }, { noScroll: true });
  const menu = q('header button[aria-label*="menu" i], header button').filter({ visible: true }).first();
  await S('m-menu-button', menu, ['default'], { group: g, title: 'Menu button', desc: 'The header hamburger toggle.', sel: 'header menu button' }, { noScroll: true });
  try {
    if (await menu.count()) { await menu.click({ timeout: 5000 }).catch(() => menu.evaluate((el) => el.click())); await page.waitForTimeout(1500); }
  } catch (e) { log('  ! mobile menu toggle failed', String(e.message).split('\n')[0]); }
  await S('m-menu-open', q('div[class*="fixed"][class*="top-"]').filter({ hasText: /Platform/ }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile menu, open', desc: 'The header menu panel opened by its own toggle.', sel: 'mobile menu panel' }, { noScroll: true });
  await S('m-nav-item', q('nav a, nav button, [role="dialog"] a, [role="dialog"] button, body button, body a').filter({ hasText: /^\s*(Doppler for Agents|Customers|Pricing)\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Mobile nav item', desc: 'An item inside the opened header menu.', sel: 'mobile menu item' }, { noScroll: true });
  await page.keyboard.press('Escape'); await page.waitForTimeout(500);
  await S('m-hero', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile headline', sel: 'h1 at 390' });
  await S('m-cta', q('main a, section a, a').filter({ hasText: /Start for Free/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Mobile CTA', desc: 'The hero Start-for-Free button at phone width; measured never followed.', sel: 'mobile "Start for Free"' });
  save();
}

run = new Date().toISOString().slice(0, 10);
out._meta.read = run;
out._meta.viewport = '1440 x 900 (mobile group 390 x 844); every surface paints the same dark theme (warm-black #1c1624)';
out._meta.tool = 'tools/capture/public/measure.mjs';
const { browser, context: ctx0 } = await launch();
context = ctx0;
const pages = process.argv.slice(2);
const plan = { home, pricing, demo, integrations, blog, customers, agents, platform, mobile };
const order = Object.keys(plan).filter((k) => !pages.length || pages.includes(k));
try {
  for (const k of order) { if (k !== 'mobile') await plan[k](); }
  if (!pages.length || pages.includes('home')) await footer();
  if (!pages.length || pages.includes('mobile')) await plan.mobile();
  // Reduced-motion check on an element that actually transitions — the header
  // links' measured 0.3s colour transition — read under both settings. The
  // header bar itself has no transition, so probing it shows no change either
  // way.
  if (!pages.length || pages.includes('home')) await reducedMotion('home', 'header a[href*="dashboard.doppler.com"], header nav a');
} finally {
  for (const [key, c] of Object.entries(out.components)) {
    // An untouched entry is pruned only when its page was not blocked this
    // run: an edge-blocked route keeps its earlier readings under their
    // original provenance instead of being erased and republished.
    if (!touched.has(key) && !pages.length && !failedPages.has(c.page)) { delete out.components[key]; continue; }
    const want = listed.get(key);
    if (want) for (const st of Object.keys(c.states || {})) if (!want.has(st)) delete c.states[st];
  }
  save();
  await browser.close();
}
console.log('components-computed.json:', Object.keys(out.components).length, 'components');
