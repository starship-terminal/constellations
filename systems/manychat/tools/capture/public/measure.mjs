// Measures manychat.com's public components in every state reachable without
// signing in or submitting anything.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs PYTHON=<venv python3> node measure.mjs [page ...]
//
// Pages: home pricing instagram how-to mobile.
// Writes raw/components-computed.json (merged) and one crop per component and
// state into components/crops/; raw/measurements.md is built by
// build-measurements.mjs.
//
// manychat.com is a Next.js + Tailwind marketing site; the page paints one
// light theme. Specs select by role, aria-label, href or visible text.
// Log in, Get started, Start for free and Try 14 days for free are measured,
// never followed. The Product mega-menu, the billing toggle and FAQ summaries
// are local UI toggles. The Usercentrics privacy layer is hidden, never
// answered. app.manychat.com is never entered. The bot builder and the
// in-app template library sit behind sign-in.
import fs from 'node:fs';
import path from 'node:path';
import { BASE, M, launch, patch, open, closePromo, styleOf, crop, centre, RAW, UA, UA_MOBILE } from './lib.mjs';

const OUT = process.env.OUT_JSON || path.join(RAW, 'components-computed.json');
const out = fs.existsSync(OUT) ? JSON.parse(fs.readFileSync(OUT, 'utf8')) : {};
out._meta ??= {};
out.components ??= {};
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const save = () => { fs.mkdirSync(RAW, { recursive: true }); fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n'); };
const URLS = { home: '/', pricing: '/pricing', instagram: '/product/instagram', 'how-to': '/resources/how-to' };
let page, cdp, current, context, run, liveCtx;
const touched = new Set();
const listed = new Map();
// Routes blocked this run: components last measured on them keep their
// earlier readings instead of being pruned below (a blocked pass must never
// erase evidence).
const failedPages = new Set();

async function blocked() {
  return page.evaluate(() => {
    const t = (document.body && document.body.innerText) || '';
    return /client challenge|performing security verification|verifying you are human|just a moment|access denied|unusual activity from your computer network|not a robot|you have been blocked|unable to access|a required part of this site/i.test(t + ' ' + document.title) || t.trim().length < 40;
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
    : { viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1, userAgent: UA, locale: 'en-US' });
  await patch(ctx);
  page = await ctx.newPage();
  cdp = await ctx.newCDPSession(page);
  await cdp.send('DOM.enable');
  await cdp.send('CSS.enable');
  page.setDefaultTimeout(8000);
  log('open', key, mobile ? '(mobile)' : '');
  // Cloudflare Turnstile can greet a route: wait it out, then one retry on a
  // fresh context before recording the route as blocked this run.
  let ok = false;
  for (let tries = 0; tries < 2 && !ok; tries++) {
    ok = (await open(page, url || (/^https?:/.test(URLS[key]) ? URLS[key] : BASE + URLS[key]), { wait, promo }))
      && !(await blocked());
    if (!ok && tries === 0) { log('  challenge, one reload', key); }
  }
  if (!ok) { log('  BLOCKED', key); failedPages.add(key); await page.close(); await ctx.close(); liveCtx = null; return false; }
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
  Object.assign(c, { page: current, run, url: /^https?:/.test(URLS[current] || '') ? URLS[current] : BASE + (URLS[current] || '') }, meta);
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
  let opened = '';
  if (opts.open) {
    await reset();
    try { opened = await opts.open() || ''; } catch (e) { opened = 'open failed: ' + String(e.message).slice(0, 80); log('  ! open failed', key, String(e.message).slice(0, 80)); }
    if (opts.requireOpen && !/painted|already open/.test(opened)) {
      log('  ! menu did not paint', key, opened);
      out.components[key].states = {};
      out.components[key].missing = true;
      out.components[key].recaptureNote = opened;
      return;
    }
  }
  const loc = target.filter({ visible: true }).first();
  await loc.waitFor({ state: 'visible', timeout: 6000 }).catch(() => {});
  if (!(await loc.count())) {
    const has = Object.keys(out.components[key].states || {}).length > 0;
    log('  ! missing', key, has ? '(earlier states kept)' : '');
    // Keep earlier evidence under its own provenance: the states stay but the
    // entry keeps its original page/run/url and records the miss, so a re-run
    // never republishes old readings under a new date.
    if (!has || opts.replaceOnMiss) {
      out.components[key].states = {};
      out.components[key].missing = true;
    } else { Object.assign(out.components[key], keep); out.components[key].recaptureMissed = run; }
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
      } else if (st === 'opened') {
        if (opts.noToggle) via = 'held open by an earlier toggle';
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

// Clicks a UI toggle (dropdown, menu, sheet trigger). Refuses a submit button
// and any control whose text names an action this kit must never take.
const NEVER = /^(send|submit|sign in|log ?in|login|create|add|download|buy|purchase|pay|checkout|join|subscribe|save|apply|accept|reject|start|get started|claim|share|export|select|continue|start for free|try 14 days for free|register for free|ok)$/i;
async function toggle(loc, { allowLink = false } = {}) {
  const l = loc.filter({ visible: true }).first();
  const t = await l.evaluate((el) => ({ tag: el.tagName, type: el.getAttribute('type'), text: (el.innerText || el.getAttribute('aria-label') || '').trim() }));
  if (t.type === 'submit' || NEVER.test(t.text) || (t.tag === 'A' && !allowLink)) throw new Error(`toggle refused: ${t.tag} "${t.text}"`);
  await l.click({ timeout: 4000 }).catch(() => l.evaluate((el) => el.click()));
}

// Variant of S() for routes whose Playwright locators never resolve.
// curater.org/taste client-side redirected to /taste/soon and the navigation
// never settles: locators count matches, but every resolve dies with the
// execution context. Measuring the default state through the main world
// (same styleOf reader + clip crop) instead of locators.
const q = (sel) => page.locator(sel);
const B4 = ['default', 'hover', 'focus-visible', 'pressed'];

// Scrolls the page down in steps and back to the top: lazy-mounted sections
// only enter the DOM once scrolled into view.
async function lazyLoad() {
  await page.evaluate(async () => {
    const h = document.documentElement.scrollHeight;
    for (let y = 0; y <= h; y += 800) { scrollTo(0, y); await new Promise((r) => setTimeout(r, 120)); }
    scrollTo(0, 0);
  });
  await page.waitForTimeout(1600);
}

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
    await p.goto(URLS[key] ? (/^https?:/.test(URLS[key]) ? URLS[key] : BASE + URLS[key]) : BASE, { waitUntil: 'domcontentloaded', timeout: 90000 }).catch(() => {});
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

const G = {
  shell: 'Shell and navigation', home: 'Home', pricing: 'Pricing',
  instagram: 'Instagram product', howto: 'How-to resources',
  mobile: 'Mobile (390 wide)',
};

// The marketing chrome is not a <header>. Nav labels are divs (PRODUCT,
// SOLUTIONS, AGENCIES, RESOURCES, EN). PRICING, LOG IN and GET STARTED are
// anchors. Billing MONTHLY / ANNUAL are labels. innerText triples because
// the pill paints button__before and button__after spans, so match on the
// element's own text node, not a regex against the whole innerText.
async function markOwnText(tag, re, { band = null, maxW = 280, maxLen = 40 } = {}) {
  return page.evaluate(({ tag, source, band, maxW, maxLen }) => {
    const rx = new RegExp(source, 'i');
    document.querySelectorAll('[data-mc-mark]').forEach((n) => n.removeAttribute('data-mc-mark'));
    const text = (el) => (el.innerText || el.textContent || '').replace(/\s+/g, ' ').trim();
    const hits = [...document.querySelectorAll(tag)].filter((el) => {
      const r = el.getBoundingClientRect();
      if (r.width < 8 || r.height < 8 || r.width > maxW) return false;
      if (band && (r.top < band[0] || r.top > band[1] || r.bottom > band[1] + 40)) return false;
      const cs = getComputedStyle(el);
      if (cs.visibility === 'hidden' || cs.display === 'none' || cs.pointerEvents === 'none') return false;
      const t = text(el);
      if (!rx.test(t) || t.length > maxLen) return false;
      return true;
    });
    hits.sort((a, b) => {
      const ra = a.getBoundingClientRect();
      const rb = b.getBoundingClientRect();
      return (ra.width * ra.height) - (rb.width * rb.height);
    });
    const hit = hits[0];
    if (!hit) return false;
    hit.setAttribute('data-mc-mark', '1');
    return { tag: hit.tagName, text: text(hit).slice(0, 40), w: Math.round(hit.getBoundingClientRect().width), y: Math.round(hit.getBoundingClientRect().y) };
  }, { tag, source: re.source, band, maxW, maxLen });
}

function marked() {
  return page.locator('[data-mc-mark="1"]').first();
}

// Opens the Product mega dropdown and waits until a menu link paints.
// A box with opacity 0 is the closed menu, not an open one. The nav label is a div.
async function openProduct() {
  const painted = () => page.evaluate(() => [...document.querySelectorAll('a')].some((a) => {
    if (!/automate your instagram marketing/i.test(a.textContent || '')) return false;
    const r = a.getBoundingClientRect();
    const cs = getComputedStyle(a);
    if (!(r.height > 8 && r.width > 8 && r.top >= 0 && r.top < 700)) return false;
    if (cs.visibility === 'hidden' || cs.display === 'none' || cs.opacity === '0') return false;
    for (let n = a; n && n !== document.documentElement; n = n.parentElement) {
      const pcs = getComputedStyle(n);
      if (pcs.visibility === 'hidden' || pcs.display === 'none' || pcs.opacity === '0') return false;
    }
    return true;
  }));
  if (await painted()) return 'the Product menu was already open';
  const ok = await markOwnText('div, a, button', /^PRODUCT$/, { band: [40, 200], maxW: 160 });
  if (!ok) return 'no Product trigger';
  const item = marked();
  await item.click({ timeout: 4000 }).catch(() => item.evaluate((el) => el.click()));
  for (let i = 0; i < 8; i++) {
    if (await painted()) return 'clicked Product; a menu link painted';
    await page.waitForTimeout(250);
  }
  return 'clicked Product; no menu link painted';
}

const FIELD = ['default', 'focused', 'filled'];

async function home() {
  if (!(await newPage('home'))) return;
  if (process.env.ONLY === 'nav-cta') {
    const ctaHit = await markOwnText('a', /^GET STARTED/, { band: [60, 180], maxW: 200, maxLen: 50 });
    log('  mark cta', JSON.stringify(ctaHit));
    await S('nav-cta', marked(), B4, { group: G.shell, title: 'Get started pill', desc: 'The nav "Get started" pill. It opens the sign-up flow. Measured, never followed.', sel: 'a (text GET STARTED, nav band y 60-180)' }, { noScroll: true, replaceOnMiss: true, open: async () => { await markOwnText('a', /^GET STARTED/, { band: [60, 180], maxW: 200, maxLen: 50 }); return 'marked Get started'; } });
    return;
  }
  await sheetsFor('home');
  await chrome('home');
  const g = G.shell;
  await S('promo-banner', q('a[href*="creatorworld"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Promo banner', desc: 'The Creator World 27 strip above the nav. A marketing link; measured, never followed.', sel: 'a[href*="creatorworld"]' }, { noScroll: true });
  await S('header-nav', q('nav').filter({ visible: true }).first(), ['default'], { group: g, title: 'Header', desc: 'The sticky nav: logo, Product/Solutions/Agencies/Pricing/Resources, locale, Log in, Get started. The site paints no <header> element.', sel: 'nav' }, { noScroll: true });
  await S('nav-logo', q('nav a[href="/"], a[href="/"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Logo', desc: 'The Manychat wordmark in the nav.', sel: 'nav a[href="/"]' }, { noScroll: true });
  const productHit = await markOwnText('div, a, button', /^PRODUCT$/, { band: [40, 200], maxW: 160 });
  log('  mark product', JSON.stringify(productHit));
  await S('nav-link', marked(), [...B4, 'opened'], { group: g, title: 'Nav item (dropdown)', desc: '"Product" is a div, not a button. It opens the channel mega-menu. A local toggle; its links were never followed.', sel: 'div (text PRODUCT, nav band)' }, { noScroll: true, open: async () => { await markOwnText('div, a, button', /^PRODUCT$/, { band: [40, 200], maxW: 160 }); return 'marked Product'; } });
  await markOwnText('a', /^PRICING$/, { band: [40, 200], maxW: 140 });
  await S('nav-plain-link', marked(), B4, { group: g, title: 'Nav link', desc: '"Pricing" is a plain nav anchor. Measured, never followed from this shot.', sel: 'a (text PRICING, nav band)' }, { noScroll: true, open: async () => { await markOwnText('a', /^PRICING$/, { band: [40, 200], maxW: 140 }); return 'marked Pricing'; } });
  await markOwnText('div, button, a', /^EN$/, { band: [40, 200], maxW: 80 });
  await S('nav-locale', marked(), B4, { group: g, title: 'Locale switch', desc: 'The EN language switch is a div. Measured; the locale was never changed.', sel: 'div (text EN, nav band)' }, { noScroll: true, open: async () => { await markOwnText('div, button, a', /^EN$/, { band: [40, 200], maxW: 80 }); return 'marked EN'; } });
  await S('nav-login', q('a[href*="app.manychat.com/signin"]').filter({ visible: true }).first(), B4, { group: g, title: 'Log in link', desc: '"Log in" points at app.manychat.com/signin. Measured, never followed. Sign-in boundary.', sel: 'a[href*="/signin"]' }, { noScroll: true });
  const ctaHit = await markOwnText('a', /^GET STARTED/, { band: [60, 180], maxW: 200, maxLen: 50 });
  log('  mark cta', JSON.stringify(ctaHit));
  await S('nav-cta', marked(), B4, { group: g, title: 'Get started pill', desc: 'The nav "Get started" pill. It opens the sign-up flow. Measured, never followed.', sel: 'a (text GET STARTED, nav band y 60-180)' }, { noScroll: true, replaceOnMiss: true, open: async () => { await markOwnText('a', /^GET STARTED/, { band: [60, 180], maxW: 200, maxLen: 50 }); return 'marked Get started'; } });
  await S('menu-item', q('a[href="/product/instagram"]').filter({ hasText: /instagram/i }).filter({ visible: true }).first(), ['default', 'focus-visible'], { group: g, title: 'Mega-menu item', desc: '"Instagram — Automate your Instagram Marketing" inside the Product menu. Measured after a menu link painted; never followed from the menu.', sel: 'a[href="/product/instagram"]' }, { open: openProduct, noScroll: true, replaceOnMiss: true, requireOpen: true });
  const h = G.home;
  await S('hero-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: h, title: 'Hero heading', desc: '"Social smarter, not harder." set in ManyChatGravity.', sel: 'h1' }, { noScroll: true });
  await S('hero-cta', q('a[href*="signup"]').filter({ hasText: /get started/i }).filter({ visible: true }).nth(1), B4, { group: h, title: 'Hero Get started', desc: 'The neon-pink hero pill. It opens sign-up. Measured, never followed.', sel: 'main a[href*="signup"]' });
  await S('section-heading', q('h2').filter({ visible: true }).first(), ['default'], { group: h, title: 'Section heading', desc: 'A Rooftop section heading below the hero.', sel: 'h2' });
  await S('channel-card', q('a[href="/product/tiktok"], a[href="/sms-marketing"]').filter({ visible: true }).first(), ['default', 'hover', 'focus-visible'], { group: g, title: 'Channel menu item', desc: 'The TikTok item inside the open Product menu. Measured after a menu link painted; never followed.', sel: 'a[href="/product/tiktok"]' }, { open: openProduct, noScroll: true, replaceOnMiss: true, requireOpen: true });
  await S('quote-card', q('blockquote, figure, [class*="quote" i], [class*="testimonial" i]').filter({ visible: true }).first(), ['default'], { group: h, title: 'Creator quote', desc: 'A published creator quote on the home page. Marketing copy, not an account.', sel: 'blockquote, figure' });
  await S('faq-item', q('button').filter({ hasText: /will using manychat/i }).filter({ visible: true }).first(), ['default', 'opened', 'focus-visible'], { group: h, title: 'FAQ accordion', desc: 'A home FAQ summary. Opened by its own click. Nothing was submitted.', sel: 'button' });
  await S('footer', q('footer').filter({ visible: true }).last(), ['default'], { group: g, title: 'Footer', desc: 'The footer band: product, company and legal columns.', sel: 'footer' });
  await S('footer-link', q('footer a').filter({ hasText: /^about$/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Footer link', desc: '"About" in the footer. Measured, never followed.', sel: 'footer a' });
}

// Walk up from the Free heading until the box is a card (under 480px wide,
// over 280px tall) with a painted radius.
async function markFreeCard() {
    return page.evaluate(() => {
      document.querySelectorAll('[data-mc-mark]').forEach((n) => n.removeAttribute('data-mc-mark'));
      const text = (el) => (el.innerText || '').replace(/\s+/g, ' ').trim();
      const head = [...document.querySelectorAll('h2, h3, h4, p, div, span')].find((el) => {
        const r = el.getBoundingClientRect();
        return text(el) === 'Free' && r.width > 20 && r.width < 400 && r.top > 200 && r.top < 800;
      });
      if (!head) return false;
      let n = head;
      for (let i = 0; i < 10 && n; i++) {
        const r = n.getBoundingClientRect();
        const rad = parseFloat(getComputedStyle(n).borderTopLeftRadius);
        if (r.width > 200 && r.width < 480 && r.height > 280 && rad >= 8) {
          n.setAttribute('data-mc-mark', '1');
          return { w: Math.round(r.width), h: Math.round(r.height), y: Math.round(r.y), rad };
        }
        n = n.parentElement;
      }
      return false;
    });
}

async function pricing() {
  if (!(await newPage('pricing'))) return;
  if (process.env.ONLY === 'price-card') {
    const freeHit = await markFreeCard();
    log('  mark free', JSON.stringify(freeHit));
    await S('price-card', marked(), ['default'], { group: G.pricing, title: 'Price card', desc: 'The Free plan card: $0, 25 active contacts, Start for free.', sel: 'card ancestor of the Free heading' }, { replaceOnMiss: true, open: async () => { await markFreeCard(); return 'marked Free card'; } });
    return;
  }
  await sheetsFor('pricing');
  await chrome('pricing');
  const g = G.pricing;
  await S('price-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Pricing heading', desc: '"Plans that scale when you do".', sel: 'h1' }, { noScroll: true });
  const annualHit = await markOwnText('label, button, div, span', /^ANNUAL$/, { band: [80, 420], maxW: 180 });
  log('  mark annual', JSON.stringify(annualHit));
  await S('billing-toggle', marked(), ['default', 'hover', 'focus-visible', 'pressed'], { group: g, title: 'Billing toggle', desc: 'The Annual side of the Monthly/Annual switch. The control is a label, not a button. A local UI toggle. Checkout was never opened.', sel: 'label (text ANNUAL)' }, { noScroll: true, open: async () => { await markOwnText('label, button, div, span', /^ANNUAL$/, { band: [80, 420], maxW: 180 }); return 'marked Annual'; } });
  const freeHit = await markFreeCard();
  log('  mark free', JSON.stringify(freeHit));
  await S('price-card', marked(), ['default'], { group: g, title: 'Price card', desc: 'The Free plan card: $0, 25 active contacts, Start for free.', sel: 'card ancestor of the Free heading' }, { replaceOnMiss: true, open: async () => { await markFreeCard(); return 'marked Free card'; } });
  await S('price-cta', q('a').filter({ hasText: /start for free/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Price CTA', desc: '"Start for free" on the Free card. It opens sign-up. Measured, never followed. Checkout was not submitted.', sel: 'a[href*="signup"]' });
  // The plan-feature rows are not an FAQ. Leave price-faq missing unless a
  // real accordion summary is on the page. Do not measure a feature row as one.
  await S('price-faq', q('button, summary').filter({ hasText: /which plan is right|frequently asked/i }).filter({ visible: true }).first(), ['default', 'opened'], { group: g, title: 'Pricing FAQ', desc: 'A pricing FAQ summary, opened by its own click. Nothing was submitted.', sel: 'button, summary' }, { replaceOnMiss: true });
}

async function instagram() {
  if (!(await newPage('instagram'))) return;
  await sheetsFor('instagram');
  await chrome('instagram');
  const g = G.instagram;
  await S('product-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Product heading', desc: '"Your Instagram just got smarter".', sel: 'h1' }, { noScroll: true });
  await S('product-cta', q('main a, a').filter({ hasText: /get started/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Product CTA', desc: 'A product-page Get started pill. Measured, never followed.', sel: 'a[href*="signup"]' });
}

async function howto() {
  if (!(await newPage('how-to'))) return;
  await sheetsFor('how-to');
  await chrome('how-to');
  const g = G.howto;
  await S('howto-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'How-to heading', desc: '"How to Use Manychat". A public guide index, not the bot builder.', sel: 'h1' }, { noScroll: true });
  await S('howto-card', q('main a').filter({ hasText: /how to/i }).filter({ visible: true }).first(), ['default', 'hover'], { group: g, title: 'Guide card', desc: 'A public how-to card. Measured, never followed into a form.', sel: 'main a' });
}

async function mobile() {
  if (!(await newPage('home', { mobile: true }))) return;
  const g = G.mobile;
  await S('m-header', q('nav').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile header', desc: 'The nav at phone width. The site paints no <header> element.', sel: 'nav' }, { noScroll: true });
  await S('m-logo', q('nav a[href="/"], a[href="/"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile logo', sel: 'a[href="/"]' }, { noScroll: true });
  // The painted hamburger is not a selectable button in this headless pass
  // (the only top-right button is a hidden Close). Do not invent a crop.
  await S('m-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile hero heading', desc: 'The hero h1 at 390px.', sel: 'h1' });
  await S('m-cta', q('a[href*="signup"]').filter({ visible: true }).first(), B4, { group: g, title: 'Mobile Get started', desc: 'A Get started link at 390px. Measured, never followed.', sel: 'a[href*="signup"]' });
}

run = new Date().toISOString().slice(0, 10);
out._meta.read = run;
out._meta.viewport = '1440 x 900 (mobile group 390 x 844); manychat.com paints a single light theme';
out._meta.tool = 'tools/capture/public/measure.mjs';
const { browser, context: ctx0 } = await launch();
context = ctx0;
const pages = process.argv.slice(2);
const plan = { home, pricing, instagram, 'how-to': howto, mobile };
const order = Object.keys(plan).filter((k) => !pages.length || pages.includes(k));
try {
  for (const k of order) { if (k !== 'mobile') await plan[k](); }
  if (!pages.length || pages.includes('mobile')) await plan.mobile();
  // Reduced-motion check on an element that transitions (a nav link's hover),
  // so the delta is meaningful.
  if (!pages.length || pages.includes('home')) await reducedMotion('home', 'nav a');
} finally {
  for (const [key, c] of Object.entries(out.components)) {
    // An untouched entry is pruned only on a full run: a page-scoped rerun
    // keeps readings from the pages it did not open. An edge-blocked route
    // also keeps its earlier readings.
    if (!touched.has(key) && !pages.length && !failedPages.has(c.page)) { delete out.components[key]; continue; }
    const want = listed.get(key);
    if (want) for (const st of Object.keys(c.states || {})) if (!want.has(st)) delete c.states[st];
  }
  save();
  await browser.close();
}
console.log('components-computed.json:', Object.keys(out.components).length, 'components');
