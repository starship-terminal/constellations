// Measures calendly.com's public components in every state reachable without
// signing in, booking, buying or submitting anything.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node measure.mjs [page ...]
//
// Pages: home pricing booking event login signup mobile.
// Writes raw/components-computed.json (merged) and one crop per component and
// state into components/crops/; raw/measurements.md is built by
// build-measurements.mjs.
//
// calendly.com is two surfaces: the Astro/Tailwind marketing site (utility
// classes over a declared --color-*/--radius-* token layer, .dark islands) and
// the invitee booking app on /<user> (booking-kit_*, Proxima Nova). Nothing is
// sent, booked, bought or signed into: the only presses are local UI toggles —
// the header Product dropdown, the Billed-yearly radio, the mobile menu and a
// picked calendar day (which reveals the times column; Next is never pressed).
// The OneTrust/Ketch banners and the Intercom launcher are hidden, never
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
const URLS = { home: '/', pricing: '/pricing', booking: '/calendly-demo', event: '/calendly-demo/dog-nail-trim-shampoo-small', login: '/login', signup: '/signup' };
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
  await open(page, url || BASE + URLS[key], { wait, promo });
  if (await blocked()) { log('  BLOCKED', key); failedPages.add(key); await page.close(); await ctx.close(); return false; }
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
    c.states[state] = { error: String(e.message || e).slice(0, 200) };
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
        await fld.click({ timeout: 4000 }).catch(() => fld.evaluate((el) => el.focus()));
        await page.waitForTimeout(400);
        via = 'clicked into the field';
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
      await measure(key, st, loc, { ...opts, via });
    } catch (e) {
      out.components[key].states[st] = { error: String(e.message || e).slice(0, 200) };
      log('  !', key, st, String(e.message).slice(0, 120));
    }
    if (undo) await undo().catch(() => {});
    if (opts.after?.[st]) await opts.after[st](loc).catch(() => {});
  }
  await reset();
}

// Clicks a UI toggle (dropdown, menu, radio, day). Refuses a submit button and
// any control whose text names an action this kit must never take.
const NEVER = /^(send|submit|sign in|log ?in|login|create|add|download|buy|purchase|pay|checkout|join|subscribe|save|apply|accept|reject|start|get started|claim|share|export|continue|claim this offer|try again|next|confirm|schedule event|i understand|decline)$/i;
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
// the same component re-read in a context with reduce on.
async function reducedMotion(key, sel) {
  out._meta.reducedMotion ??= {};
  try {
    const b = context.browser();
    const ctx = await b.newContext({ viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1, userAgent: UA, locale: 'en-US', reducedMotion: 'reduce' });
    await patch(ctx);
    const p = await ctx.newPage();
    await p.goto(BASE + URLS[key], { waitUntil: 'domcontentloaded', timeout: 90000 }).catch(() => {});
    await p.waitForTimeout(7000);
    await closePromo(p);
    const v = await p.evaluate((s) => {
      const el = document.querySelector(s);
      if (!el) return null;
      const cs = getComputedStyle(el);
      return { transition: cs.transition, animation: cs.animation, scrollBehavior: getComputedStyle(document.documentElement).scrollBehavior };
    }, sel).catch(() => null);
    out._meta.reducedMotion[key] = { selector: sel, reduce: v };
    await ctx.close();
  } catch (e) { out._meta.reducedMotion[key] = { selector: sel, error: String(e).slice(0, 120) }; }
}

// Marks the nearest ancestor of the element matching sel that paints a fill
// or a background image (the hero island paints a gradient), or falls back to
// marking a painted descendant: the hero card is a sibling layer, not an
// ancestor, so for it we mark the painted element inside its section instead.
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
  booking: 'Booking (invitee flow)', auth: 'Log in and sign up',
  footer: 'Footer', mobile: 'Mobile (390 wide)',
};

async function home() {
  if (!(await newPage('home'))) return;
  await sheetsFor('home');
  await chrome('home');
  const g = G.shell;
  await S('header', q('header#site-header, header').filter({ visible: true }).first(), ['default'], { group: g, title: 'Header', desc: 'The sticky marketing header: wordmark, the Product/Solutions/Resources dropdowns, Pricing, Talk to sales, Log In and the dark Get-started pill.', sel: 'header#site-header' }, { noScroll: true });
  await S('logo', q('header a[href="/"], header a').filter({ visible: true }).first(), ['default'], { group: g, title: 'Logo', desc: 'The Calendly wordmark anchor.', sel: 'header a:first' }, { noScroll: true });
  await S('nav-trigger', q('header button').filter({ hasText: /^\s*Product\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Nav trigger', desc: 'The Product button that opens the header mega-menu; toggled, never followed.', sel: 'header button "Product"' }, { noScroll: true });
  await S('nav-link', q('header nav a, header a').filter({ hasText: /^\s*Pricing\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Nav link', desc: 'The plain Pricing header link.', sel: 'header nav a "Pricing"' }, { noScroll: true });
  await S('nav-sales', q('header a').filter({ hasText: /Talk to sales/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Sales link', desc: 'The Talk-to-sales header action; measured never followed.', sel: 'header a "Talk to sales"' }, { noScroll: true });
  await S('nav-login', q('header a').filter({ hasText: /^\s*Log In\s*$/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Login link', desc: 'The Log-In header action (outlined pill); measured never followed.', sel: 'header a "Log In"' }, { noScroll: true });
  await S('nav-cta', q('header a').filter({ hasText: /Get started for free/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Nav CTA', desc: 'The Get-started-for-free dark pill; measured never followed.', sel: 'header a "Get started for free"' }, { noScroll: true });
  // The Product trigger opens the mega-menu on hover (a click toggles it too
  // but a hover is how the surface really opens); keep the pointer put while
  // the panel and one of its links are read (noReset), then Escape to close.
  try {
    const t = q('header button').filter({ hasText: /^\s*Product\s*$/ }).filter({ visible: true }).first();
    if (await t.count()) { await t.hover({ timeout: 5000 }); await page.waitForTimeout(1200); }
  } catch (e) { log('  ! dropdown hover failed', String(e.message).split('\n')[0]); }
  const panel = await markPainted('header a[href*="scheduling"], header a[href*="features"], header a[href*="product"], header a[href*="callie"], header a[href*="notetaker"]', 'm-panel', { minW: 300, minH: 150 }).catch(() => null);
  await S('nav-dropdown', panel || q('header [class*="panel" i], header [class*="dropdown" i]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Nav dropdown', desc: 'The Product mega-menu panel, opened by its own trigger.', sel: 'header product panel' }, { noScroll: true, noReset: true });
  await S('menu-link', q('header a').filter({ hasText: /Scheduling|Callie|Notetaker|Routing|Payments/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Menu link', desc: 'A feature link inside the opened mega-menu.', sel: 'header menu a' }, { noScroll: true,
    open: async () => { const t = q('header button').filter({ hasText: /^\s*Product\s*$/ }).filter({ visible: true }).first(); if (await t.count()) { await t.hover({ timeout: 5000 }); await page.waitForTimeout(1000); } } });
  await page.keyboard.press('Escape'); await page.waitForTimeout(400);
  const h = G.hero;
  await S('hero-title', q('h1').filter({ visible: true }).first(), ['default'], { group: h, title: 'Hero headline', desc: 'The 72px Calendly-Sans display headline inside the dark hero island.', sel: 'h1' }, { noScroll: true });
  await S('hero-lede', q('p').filter({ hasText: /scheduling|meeting/i }).filter({ visible: true }).first(), ['default'], { group: h, title: 'Hero copy', desc: 'The 18px lede under the headline, Geist on the dark island.', sel: 'hero lede' });
  await S('signup-google', q('button').filter({ hasText: /Sign up with Google/i }).filter({ visible: true }).first(), B4, { group: h, title: 'Google signup button', desc: 'The light Sign-up-with-Google pill in the dark hero; measured never followed.', sel: 'button "Sign up with Google"' });
  await S('signup-email', q('a, button').filter({ hasText: /Sign up with email/i }).filter({ visible: true }).first(), B4, { group: h, title: 'Email signup link', desc: 'The underlined Sign-up-with-email link under the OAuth buttons; measured never followed.', sel: '"Sign up with email"' });
  const card = await markPainted('h1', 'm-hero-card', { minW: 400, minH: 200, descend: true }).catch(() => null);
  await S('hero-card', card || q('section').filter({ visible: true }).first(), ['default'], { group: h, title: 'Hero card', desc: 'The painted island behind the hero (the .dark section card).', sel: 'first painted ancestor of h1' });
  const s = G.home;
  await S('h2-serif', q('h2[class*="font-wulkan"], h2').filter({ visible: true }).first(), ['default'], { group: s, title: 'Section heading (serif)', desc: 'A 48px Wulkan-Text section heading in the light sections.', sel: 'h2.font-wulkan' });
  await S('badge', q('[class*="badge" i], [class*="chip" i]').filter({ hasText: /Beta|New/i }).filter({ visible: true }).first(), B4, { group: s, title: 'Badge', desc: 'A "Beta"/"New" chip (rounded-ui-xxs).', sel: 'badge chip' });
  save();
}

async function pricing() {
  if (!(await newPage('pricing', { wait: 11000 }))) return;
  await sheetsFor('pricing');
  await chrome('pricing');
  const g = G.pricing;
  await S('pricing-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Pricing title', desc: 'The pricing page display heading.', sel: 'h1 on /pricing' }, { noScroll: true });
  await S('billing-radio', q('label').filter({ hasText: /Billed yearly/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Billing toggle', desc: 'A Billed-monthly/Billed-yearly radio label; the yearly option was toggled for the screenshot state, never checked out.', sel: 'label "Billed yearly"' }, { noScroll: true });
  await S('plan-name', q('h3').filter({ hasText: /^\s*(Free|Standard|Teams|Enterprise)\s*$/ }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Plan name', desc: 'A plan card\'s name (h3, Calendly Sans).', sel: 'h3 plan name' });
  await S('plan-price', q('span, div, p').filter({ hasText: /^\$\d+$/ }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Plan price', desc: 'A plan card\'s price figure.', sel: 'plan price' });
  await S('plan-cta', q('button').filter({ hasText: /^\s*Get started\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Plan CTA', desc: 'A plan card\'s Get-started action; measured never followed.', sel: 'button "Get started"' });
  const planCard = await markPainted('h3', 'm-plan', { minW: 200, minH: 300 }).catch(() => null);
  await S('plan-card', planCard || q('[class*="card" i]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Plan card', desc: 'A pricing plan card (the painted ancestor of the plan name).', sel: 'plan card' });
  await S('icon-button', q('button[class*="iconbutton" i], button[class*="icon-button" i]').filter({ visible: true }).first(), B4, { group: g, title: 'Icon button', desc: 'A round icon-only expander (bg-iconbutton-bg).', sel: 'button.iconbutton' });
  await S('feature-tip', q('[class*="underline" i], span, li').filter({ hasText: /SCIM|Automate and secure/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Feature tooltip link', desc: 'A dotted-underline feature name (opens a tooltip on hover, never clicked).', sel: 'dotted-underline feature' });
  save();
}

async function booking() {
  if (!(await newPage('booking', { wait: 11000 }))) return;
  await sheetsFor('booking');
  await chrome('booking');
  const g = G.booking;
  await S('bk-panel', q('[class*="main-panel" i], [class*="booking-kit" i]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Booking panel', desc: 'The invitee page\'s centred panel (booking-kit), Proxima Nova.', sel: '.booking-kit_main-panel' }, { noScroll: true });
  await S('bk-poweredby', q('a').filter({ hasText: /POWERED BY/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Powered-by badge', desc: 'The "POWERED BY Calendly" badge link; measured never followed.', sel: 'a "POWERED BY"' });
  await S('bk-event', q('a[href*="calendly-demo/"], a').filter({ hasText: /Dog Nail|Meeting|Minute|Trim/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Event link', desc: 'An event-type link in the invitee list; measured, never opened by a press (the event page was navigated to directly).', sel: 'booking event link' });
  save();
}

async function event() {
  if (!(await newPage('event', { wait: 11000 }))) return;
  await sheetsFor('event');
  await chrome('event');
  const g = G.booking;
  await S('bk-calendar', q('table, [role="grid"], [class*="calendar" i], [class*="month" i]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Calendar', desc: 'The month grid on the event page.', sel: 'calendar grid' });
  await S('bk-month-nav', q('button[aria-label*="next month" i], button[aria-label*="previous month" i]').filter({ visible: true }).first(), B4, { group: g, title: 'Month nav button', desc: 'A previous/next-month arrow button; measured, never pressed.', sel: 'button "Go to next month"' });
  await S('bk-day', q('button[aria-label*="Times available"]').filter({ visible: true }).first(), B4, { group: g, title: 'Day cell', desc: 'An enabled day button in the calendar grid; one was selected for the times-panel state, never booked.', sel: 'calendar day button' });
  // Selecting a day reveals the times column (local UI state; Next is never
  // pressed and nothing is booked).
  try {
    const day = q('button[aria-label*="Times available"]').filter({ visible: true }).first();
    if (await day.count()) { await day.click({ timeout: 5000 }).catch(() => day.evaluate((el) => el.click())); await page.waitForTimeout(1500); }
  } catch (e) { log('  ! day select failed', String(e.message).split('\n')[0]); }
  await S('bk-day-today', q('button[aria-current="date"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Day cell, today', desc: 'Today\'s cell (aria-current="date"), an unavailable day here.', sel: 'button[aria-current="date"]' });
  await S('bk-day-selected', q('button[class*="booking-kit_button-selected" i], button[class*="selected" i]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Day cell, selected', desc: 'The picked day in its selected state (solid #006bff, locked disabled once picked).', sel: 'button.booking-kit_button-selected' });
  await S('bk-timeslot', q('button').filter({ hasText: /^\s*\d{1,2}:\d{2}\s*(am|pm)?\s*$/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Time slot', desc: 'An available time button in the revealed column; measured, never pressed (Next is never reached).', sel: 'time slot button' });
  await S('bk-timezone', q('button[class*="dropdown" i], button, select, [role="combobox"]').filter({ hasText: /GMT|UTC|Eastern|Time ?zone|EDT|EST|Pacific|Standard Time/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Timezone control', desc: 'The timezone dropdown under the calendar (its list was never opened).', sel: 'timezone control' });
  save();
}

async function login() {
  if (!(await newPage('login', { wait: 9000 }))) return;
  await sheetsFor('login');
  await chrome('login');
  const g = G.auth;
  const card = await markPainted('input, h1', 'm-login', { minW: 250, minH: 200 }).catch(() => null);
  await S('login-card', card || q('main, [class*="card" i]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Login card', desc: 'The centred login card; never filled or submitted.', sel: 'login card' });
  await S('email-field', q('input[type="email"], input[name*="email" i], input').filter({ visible: true }).first(), ['default', 'focused', 'filled'], { group: g, title: 'Email field', desc: 'The email input; sample text was typed and deleted, nothing sent.', sel: 'input[type=email]' });
  await S('continue-btn', q('button, a').filter({ hasText: /Continue with email|Continue/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Continue button', desc: 'The Continue-with-email submit; measured, never pressed (a press would submit).', sel: 'button "Continue"' });
  await S('sso-btn', q('button, a').filter({ hasText: /Continue with Google|Google/i }).filter({ visible: true }).first(), B4, { group: g, title: 'SSO button', desc: 'A Continue-with-Google/Microsoft button; measured, never followed.', sel: 'button "Continue with Google"' });
  save();
}

async function signup() {
  if (!(await newPage('signup', { wait: 9000 }))) return;
  const g = G.auth;
  const card = await markPainted('input, h1', 'm-signup', { minW: 250, minH: 200 }).catch(() => null);
  await S('signup-card', card || q('main, [class*="card" i]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Signup card', desc: 'The centred create-account card; never filled or submitted.', sel: 'signup card' });
  await S('signup-field', q('input[type="email"], input[name*="email" i], input').filter({ visible: true }).first(), ['default', 'focused'], { group: g, title: 'Signup email field', desc: 'The signup email input; focused only, never filled or submitted.', sel: 'signup input[type=email]' });
  save();
}

async function footer() {
  if (!(await newPage('home', { wait: 6000 }))) return;
  const g = G.footer;
  await page.evaluate(() => scrollTo(0, document.documentElement.scrollHeight));
  await page.waitForTimeout(1500);
  await S('footer', q('footer').filter({ visible: true }).last(), ['default'], { group: g, title: 'Footer', desc: 'The footer card (a .dark island): link columns, legal and social.', sel: 'footer' }, { noScroll: true });
  await S('footer-link', q('footer a').filter({ hasText: /\S/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Footer link', sel: 'footer a' }, { noScroll: true });
  save();
}

async function mobile() {
  if (!(await newPage('mobile', { mobile: true, url: BASE + '/' }))) return;
  await chrome('mobile');
  const g = G.mobile;
  await S('m-header', q('header').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile header', sel: 'header at 390' }, { noScroll: true });
  const menu = q('header button').filter({ visible: true }).last();
  await S('m-menu-button', menu, ['default'], { group: g, title: 'Menu button', desc: 'The header menu toggle.', sel: 'header menu button' }, { noScroll: true });
  try {
    if (await menu.count()) { await menu.click({ timeout: 5000 }).catch(() => menu.evaluate((el) => el.click())); await page.waitForTimeout(1500); }
  } catch (e) { log('  ! mobile menu toggle failed', String(e.message).split('\n')[0]); }
  await S('m-menu-open', q('[class*="fixed"][class*="inset-0"], [role="dialog"], header + div').filter({ hasText: /Product/ }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile menu, open', desc: 'The header menu panel opened by its own toggle.', sel: 'mobile menu panel' }, { noScroll: true });
  await S('m-nav-item', q('nav a, nav button, [role="dialog"] a, [role="dialog"] button, body button, body a').filter({ hasText: /^\s*(Product|Solutions|Resources|Pricing)\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Mobile nav item', desc: 'An item inside the opened header menu.', sel: 'mobile menu item' }, { noScroll: true });
  await page.keyboard.press('Escape'); await page.waitForTimeout(500);
  await S('m-hero', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile headline', sel: 'h1 at 390' });
  save();
}

run = new Date().toISOString().slice(0, 10);
out._meta.read = run;
out._meta.viewport = '1440 x 900 (mobile group 390 x 844); the marketing pages paint light with .dark islands (hero card, footer card); the booking pages paint light';
out._meta.tool = 'tools/capture/public/measure.mjs';
const { browser, context: ctx0 } = await launch();
context = ctx0;
const pages = process.argv.slice(2);
const plan = { home, pricing, booking, event, login, signup, mobile };
const order = Object.keys(plan).filter((k) => !pages.length || pages.includes(k));
try {
  for (const k of order) { if (k !== 'mobile') await plan[k](); }
  if (!pages.length || pages.includes('home')) await footer();
  if (!pages.length || pages.includes('mobile')) await plan.mobile();
  // Reduced-motion check on an element that transitions (the header's
  // transition-shadow), so the delta is meaningful.
  if (!pages.length || pages.includes('home')) await reducedMotion('home', 'header#site-header');
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
