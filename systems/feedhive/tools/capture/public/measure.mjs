// Measures feedhive.com's public components in every state reachable without
// signing in or submitting anything.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node measure.mjs [page ...]
//
// Pages: home pricing features blog tools-bio login signup mobile.
// Writes raw/components-computed.json (merged) and one crop per component and
// state into components/crops/; raw/measurements.md is built by
// build-measurements.mjs.
//
// www.feedhive.com is a light-only Next.js marketing site signed out: a thin
// Tailwind-v4 theme layer with nearly every value carried in arbitrary-value
// utilities (text-[#23252b], bg-[#4457ff], bg-primary = #4457ff). There is no
// user theme toggle and no dark mode. app.feedhive.com/signin and /signup are
// a separate Chakra-UI app (css-* emotion classes) that does not share this
// layer; its values are measured, never read from the marketing harvest.
// Specs select by role, aria-label, attribute or text. Nothing is sent,
// bought or signed into: the only presses are local UI toggles — the header's
// dropdown nav triggers (anchors with href="#" and aria-haspopup="true"), the
// feature tab pills, the pricing Monthly/Yearly toggle and the mobile menu;
// the bio-generator and signin/signup fields are typed into and cleared,
// never submitted; Sign Up, Login, Get started and every submit button are
// measured, never followed or pressed. The vanilla-cookieconsent layer stays
// empty on every observed load; any consent overlay is hidden, never
// answered.
import fs from 'node:fs';
import path from 'node:path';
import { BASE, LOGIN_URL, SIGNUP_URL, M, launch, patch, open, closePromo, domFind, styleOf, crop, centre, RAW, UA, UA_MOBILE } from './lib.mjs';

const OUT = process.env.OUT_JSON || path.join(RAW, 'components-computed.json');
const out = fs.existsSync(OUT) ? JSON.parse(fs.readFileSync(OUT, 'utf8')) : {};
out._meta ??= {};
out.components ??= {};
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const save = () => fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');
const URLS = { home: '/', pricing: '/pricing', features: '/features/scheduling', blog: '/blog', 'tools-bio': '/tools/bio-generator', login: LOGIN_URL, signup: SIGNUP_URL, mobile: '/' };
let page, cdp, current, context, run, liveCtx;
const touched = new Set();
const listed = new Map();
// Routes an edge block gates this run: components last measured on them keep
// their earlier readings instead of being pruned below (a blocked pass must
// never erase evidence).
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
  const loaded = await open(page, url || (URLS[key].startsWith('http') ? URLS[key] : BASE + URLS[key]), { wait, promo });
  if (!loaded || await blocked()) { log('  BLOCKED', key); failedPages.add(key); await page.close(); await ctx.close(); return false; }
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
  Object.assign(c, { page: current, run, url: URLS[current] && (URLS[current].startsWith('http') ? URLS[current] : BASE + URLS[current]) }, meta);
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
    c.states[state] = { ...s, crop: file, via: opts.via, run };
    if (opts.extra) c.states[state].extra = await opts.extra(loc);
    log('  ', key, state, s.rect.w + 'x' + s.rect.h);
  } catch (e) {
    // A failed re-read must not erase an earlier successful one: keep the
    // saved style and record the failed attempt beside it.
    const prev = c.states[state];
    if (prev && prev.style) prev.rerunError = String(e.message || e).slice(0, 200);
    else c.states[state] = { error: String(e.message).slice(0, 200) };
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
        await f.click({ timeout: 4000 }).catch(() => f.evaluate((el) => el.focus()));
        await page.keyboard.type(opts.fillText || 'name@example.com', { delay: 10 });
        await page.waitForTimeout(500);
        undo = async () => { await f.focus(); await page.keyboard.press('ControlOrMeta+a'); await page.keyboard.press('Backspace'); await page.waitForTimeout(300); };
        via = `typed "${opts.fillText || 'name@example.com'}", then deleted; nothing sent`;
      } else if (st === 'opened') {
        if (opts.noToggle) via = 'held open by an earlier toggle';
        else { await toggle(loc, { allowLink: opts.allowLink }); await page.waitForTimeout(900); via = 'own toggle'; }
      } else if (st === 'selected') {
        if (opts.noToggle) via = 'held selected by an earlier toggle';
        else { await toggle(loc, { allowLink: opts.allowLink }); await page.waitForTimeout(900); via = 'own toggle, then left selected'; }
      } else via = via || 'at rest';
      await measure(key, st, loc, { ...opts, via });
    } catch (e) {
      const prev = out.components[key].states[st];
      if (prev && prev.style) prev.rerunError = String(e.message || e).slice(0, 200);
      else out.components[key].states[st] = { error: String(e.message).slice(0, 200) };
      log('  !', key, st, String(e.message).slice(0, 120));
    }
    if (undo) await undo().catch(() => {});
    if (opts.after?.[st]) await opts.after[st](loc).catch(() => {});
  }
  // A listed state that failed its re-read kept the earlier evidence under
  // rerunError (and its own earlier `run`); the entry then republishes under
  // the earlier run's page/run/url and records the miss, so retained readings
  // never carry the new run's date.
  if (keep && list.some((st) => out.components[key].states[st]?.rerunError)) {
    Object.assign(out.components[key], keep);
    out.components[key].recaptureMissed = run;
  }
  await reset();
}

// Clicks a UI toggle (dropdown, menu, sheet trigger). Refuses a submit button
// and any control whose text names an action this kit must never take.
const NEVER = /^(send|send message|submit|sign in|log ?in|login|create|add|download|buy|purchase|pay|checkout|join|subscribe|save|apply|accept|reject|start|get started|claim|share|export|select|continue|continue with.*|claim this offer|try again|generate|generate.*|sign up|connect)$/i;
async function toggle(loc, { allowLink = false } = {}) {
  const l = loc.filter({ visible: true }).first();
  const t = await l.evaluate((el) => ({ tag: el.tagName, type: el.getAttribute('type'), text: (el.innerText || el.getAttribute('aria-label') || '').trim() }));
  if (t.type === 'submit' || NEVER.test(t.text) || (t.tag === 'A' && !allowLink)) throw new Error(`toggle refused: ${t.tag} "${t.text}"`);
  await l.click({ timeout: 4000 }).catch(() => l.evaluate((el) => el.click()));
}

const q = (sel) => page.locator(sel);
const B4 = ['default', 'hover', 'focus-visible', 'pressed'];
const FIELD = ['default', 'focused', 'filled'];

// Tags the closest ancestor of loc that paints a rounded card (an opaque fill
// and radius) and returns a locator for it — how the Chakra sign-in/up card is
// found, since app.feedhive.com uses css-* emotion classes, no <form>, no
// <main> and no "card" class to select by.
async function paintedCard(loc, { minR = 10, maxW = 900 } = {}) {
  const ok = await loc.filter({ visible: true }).first().evaluate((el, { minR, maxW }) => {
    document.querySelectorAll('[data-m-card]').forEach((n) => n.removeAttribute('data-m-card'));
    for (let n = el; n && n !== document.body; n = n.parentElement) {
      const cs = getComputedStyle(n);
      const r = n.getBoundingClientRect();
      if (cs.backgroundColor !== 'rgba(0, 0, 0, 0)' && parseFloat(cs.borderTopLeftRadius) >= minR && r.width > 200 && r.width <= maxW && r.height > 100) {
        n.setAttribute('data-m-card', '1');
        return true;
      }
    }
    return false;
  }, { minR, maxW }).catch(() => false);
  return ok ? page.locator('[data-m-card="1"]') : page.locator('[data-m-card="__none__"]');
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
    await p.goto(URLS[key].startsWith('http') ? URLS[key] : BASE + URLS[key], { waitUntil: 'domcontentloaded', timeout: 90000 }).catch(() => {});
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
  shell: 'Site chrome', promo: 'Promo bar', home: 'Home', tabs: 'Feature tabs',
  pricing: 'Pricing', features: 'Feature pages', blog: 'Blog', tools: 'Tools',
  login: 'App sign-in (Chakra)', signup: 'App sign-up (Chakra)',
  mobile: 'Mobile (390 wide)', footer: 'Footer',
};

// The header nav triggers ("Product", "Agents & Automation", "Socials",
// "Learn") are anchors with href="#" and aria-haspopup="true" — local UI
// toggles. Clicking opens the dropdown panel; its links are never followed.
const NAVTRIG = 'header a[href="#"][aria-haspopup], header button[aria-haspopup]';
const navTrigger = (name) => q(NAVTRIG).filter({ hasText: new RegExp(`^${name}$`) }).filter({ visible: true }).first();

async function openNavMenu(name) {
  const btn = navTrigger(name);
  if (!(await btn.count())) return 'no ' + name + ' trigger';
  for (let i = 0; i < 3; i++) {
    const st = await btn.evaluate((el) => {
      const panel = el.parentElement && [...el.parentElement.parentElement.querySelectorAll('[class*="absolute"], [role="menu"]')].find((x) => {
        const r = x.getBoundingClientRect();
        return r.width > 200 && r.height > 80 && getComputedStyle(x).visibility !== 'hidden' && getComputedStyle(x).opacity !== '0';
      });
      return (el.getAttribute('aria-expanded') === 'true') || !!panel;
    }).catch(() => false);
    if (st) return 'clicked the "' + name + '" nav trigger to open its dropdown';
    await toggle(btn, { allowLink: true });
    await page.waitForTimeout(900);
  }
  return 'activated the "' + name + '" trigger; no dropdown reported open';
}

// The mobile nav: the icon-only 44px button in the header.
async function openMobileMenu() {
  const open = () => page.evaluate(() => {
    const el = [...document.querySelectorAll('body > div, body > nav, [role="dialog"], header [class*="fixed"], header [class*="absolute"]')].find((x) => {
      const r = x.getBoundingClientRect();
      const cs = getComputedStyle(x);
      return r.height > 300 && /\S/.test(x.textContent || '') && (cs.position === 'fixed' || cs.position === 'absolute') && cs.visibility !== 'hidden' && cs.opacity !== '0';
    });
    return !!el;
  }).catch(() => false);
  if (await open()) return 'the nav overlay was already open';
  const b = page.locator('header button').filter({ visible: true }).last();
  if (!(await b.count())) return 'no menu toggle';
  for (let i = 0; i < 3; i++) {
    await b.click({ timeout: 4000 }).catch(() => b.evaluate((el) => el.click()));
    if (await open()) return 'clicked the menu button to open the nav overlay';
    await page.waitForTimeout(500);
    await b.focus();
    await page.keyboard.press('Enter');
    await page.waitForTimeout(700);
    if (await open()) return 'focused the menu button and pressed Enter to open the nav overlay';
  }
  return 'activated the menu button; the overlay did not report open';
}

async function home() {
  if (!(await newPage('home'))) return;
  await sheetsFor('home');
  await chrome('home');
  let g = G.promo;
  await S('promo-bar', q('a, div').filter({ hasText: /Limited launch bonus/i }).filter({ visible: true }).first(), ['default', 'hover'], { group: g, title: 'Launch promo bar', desc: 'The top banner ("Limited launch bonus: Double your AI credits for 3 months when you start today →"); measured, never followed.', sel: 'launch promo banner' }, { noScroll: true });
  g = G.shell;
  await S('mkt-header', q('header').filter({ visible: true }).first(), ['default'], { group: g, title: 'Site header', desc: 'The 80px header below the promo bar: FeedHive mark, Product / Agents & Automation / Socials / Learn dropdowns, Pricing, Login and the indigo Sign Up pill.', sel: 'header' }, { noScroll: true });
  await S('mkt-logo', q('header a[href="/"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Logo', desc: 'The FeedHive mark-and-wordmark in the header, linking home.', sel: 'header a[href=/]' }, { noScroll: true });
  await S('nav-dropdown', navTrigger('Product'), [...B4, 'opened'], { group: g, title: 'Nav dropdown trigger', desc: 'The "Product" header trigger — an anchor with href="#" and aria-haspopup="true" that opens the product dropdown. The opened state was measured after clicking it.', sel: 'header a[href="#"] Product' }, { noScroll: true, allowLink: true });
  await S('nav-panel', q('header [class*="absolute"], header [role="menu"], header + div [class*="absolute"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Nav dropdown panel', desc: 'The dropdown panel opened by the Product trigger; its links were never followed.', sel: 'header dropdown panel' }, { open: () => openNavMenu('Product'), noScroll: true, noReset: true });
  await S('nav-menu-item', q('header [class*="absolute"] a, header [role="menu"] a, header + div [class*="absolute"] a').filter({ visible: true }).first(), ['default', 'hover'], { group: g, title: 'Nav dropdown item', desc: 'A link inside the opened dropdown panel; measured, never followed.', sel: 'dropdown panel a' }, { open: () => openNavMenu('Product'), noScroll: true, noReset: true });
  await page.keyboard.press('Escape').catch(() => {});
  await page.mouse.move(720, 400).catch(() => {});
  await S('nav-link', q('header a[href="/pricing"]').filter({ visible: true }).first(), B4, { group: g, title: 'Nav link', desc: 'The "Pricing" header link; measured, never followed.', sel: 'header a[href=/pricing]' }, { noScroll: true });
  await S('nav-login', q('header a[href*="signin"]').filter({ visible: true }).first(), B4, { group: g, title: 'Login button', desc: 'The light "Login" pill in the header linking to app.feedhive.com; measured, never followed.', sel: 'header a[href*=signin]' }, { noScroll: true });
  // Two Sign Up anchors sit in the header: an off-canvas copy that keeps a 0x0
  // rect on desktop, and the real pill — domFind picks the painted one.
  await S('nav-signup', await domFind(page, /^\s*Sign Up\s*$/, { sel: 'header a[href*="signup"]', minW: 10, minH: 10 }), B4, { group: g, title: 'Sign Up button', desc: 'The indigo "Sign Up" pill in the header linking to app.feedhive.com/signup; measured, never followed.', sel: 'header a[href*=signup] (the painted copy)' }, { noScroll: true });
  g = G.home;
  await S('hero-badge', q('main div.cta-gradient-ring').filter({ visible: true }).first(), ['default', 'hover'], { group: g, title: 'Release badge', desc: 'The "Introducing FeedHive v2.0" pill badge over the hero — the gradient-ring outer div.', sel: 'main div.cta-gradient-ring' }, { noScroll: true });
  await S('hero-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Hero headline', desc: '"Social media using Automation & AI Agents." — the display heading; the second line paints the indigo accent.', sel: 'h1' }, { noScroll: true });
  await S('hero-sub', q('main p').filter({ hasText: /AI social media management/i }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Hero lede', desc: 'The muted lede under the headline.', sel: 'hero lede p' }, { noScroll: true });
  await S('hero-cta', q('main a').filter({ hasText: /^\s*Get started for free\s*$/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Hero CTA', desc: 'The indigo "Get started for free" button in the hero; measured, never followed.', sel: 'hero Get started for free' }, { noScroll: true });
  await S('hero-check', q('main li').filter({ hasText: /Create with AI/i }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Feature check row', desc: 'A checked feature row ("Create with AI. Generate content that fits your tone-of-voice & brand.").', sel: 'hero check list li' }, { noScroll: true });
  // The hero product mock is a static screenshot: an img clipped by a
  // rounded-l-[16px] overflow-hidden div — measure the clip, not the image.
  await S('hero-mock', q('main img[src*="hero"]').filter({ visible: true }).first().locator('xpath=ancestor::div[contains(@class,"overflow-hidden")][1]'), ['default'], { group: g, title: 'Product mock panel', desc: 'The product screenshot beside the hero — a static public image clipped by a rounded container, not the signed-in product.', sel: 'hero product mock (img clip)' });
  g = G.tabs;
  // The showcase pills auto-rotate their selection: which pill paints the
  // #eef2ff tint at any instant is transient (AI Assistant on 2026-11-14,
  // Automation then Post Conditions on 2026-11-15). The active variant is
  // therefore captured deterministically — tab-pill-active selects AI
  // Assistant by clicking before it is read, and it runs before tab-pill
  // selects Composer, so an entry described as selected never holds the
  // inactive values a later read would otherwise see.
  await S('tab-pill-active', q('main button').filter({ hasText: /^AI Assistant$/ }).filter({ visible: true }).first(), ['selected'], { group: g, title: 'Feature tab pill (active)', desc: 'A feature tab pill in its selected state — the #eef2ff indigo tint, #84a1ff border and #5a84ff ink the pills select into; selected by clicking (the at-load selection auto-rotates).', sel: 'main button AI Assistant' });
  await S('tab-pill', q('main button').filter({ hasText: /^Composer$/ }).filter({ visible: true }).first(), ['default', 'hover', 'selected'], { group: g, title: 'Feature tab pill', desc: 'One of the feature tab pills (Composer / AI Assistant / Automation / …) that switch the showcase panel — a local UI toggle; selected by clicking.', sel: 'main button Composer' });
  g = G.home;
  await S('agent-card', q('main a').filter({ hasText: /Hermes Agent|Visual automation|AI Agent/i }).filter({ visible: true }).first(), ['default', 'hover'], { group: g, title: 'Agent card', desc: 'An AI-agent feature card ("Hermes Agent ↗ — Use Herm…") on the home page; measured, never followed.', sel: 'agent feature card' });
  await S('section-h2', q('main h2').filter({ hasText: /\S/ }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Section heading', desc: 'A marketing section heading further down the home page.', sel: 'main h2' });
  g = G.footer;
  await S('footer', q('footer').filter({ visible: true }).first(), ['default'], { group: g, title: 'Footer', desc: 'The page footer: sitemap columns, legal links, social icons, the cookie-preferences button.', sel: 'footer' }, { noScroll: true });
  await S('footer-link', q('footer a').filter({ hasText: /^Pricing$/ }).first(), B4, { group: g, title: 'Footer link', desc: 'A footer sitemap link; measured, never followed.', sel: 'footer a Pricing' }, { noScroll: true });
  save();
}

async function pricing() {
  if (!(await newPage('pricing'))) return;
  await sheetsFor('pricing');
  await chrome('pricing');
  const g = G.pricing;
  await S('price-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Pricing headline', desc: '"The best social solution, for the best price." — the /pricing masthead.', sel: 'h1' }, { noScroll: true });
  // billing-yearly is the half selected on load: measure it before
  // billing-monthly's 'selected' step clicks Monthly, or its readings would
  // be the inactive half described as selected.
  await S('billing-yearly', q('button').filter({ hasText: /^Yearly$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Billing toggle (Yearly)', desc: 'The "Yearly" half of the billing pill, selected on load.', sel: 'pricing Yearly button' });
  await S('billing-monthly', q('button').filter({ hasText: /^Monthly$/ }).filter({ visible: true }).first(), ['default', 'hover', 'selected'], { group: g, title: 'Billing toggle (Monthly)', desc: 'The "Monthly" half of the billing pill — a local UI toggle that re-renders the prices; selected by clicking.', sel: 'pricing Monthly button' });
  // Each plan card is an <article> (~297x680, rounded-16); the Business card
  // paints the indigo #4457ff fill, the others are white.
  await S('plan-card', q('h2').filter({ hasText: /^Business$/ }).first().locator('xpath=ancestor::article[1]'), ['default'], { group: g, title: 'Plan card (Business)', desc: 'The highlighted indigo "Business" plan card ("POPULAR" chip).', sel: 'Business plan article' });
  await S('plan-card-plain', q('h2').filter({ hasText: /^Creator$/ }).first().locator('xpath=ancestor::article[1]'), ['default'], { group: g, title: 'Plan card (Creator)', desc: 'A plain plan card beside the highlighted one.', sel: 'Creator plan article' });
  await S('plan-cta', q('main a, main button').filter({ hasText: /^\s*Get started\s*$/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Plan CTA', desc: 'A plan card\'s "Get started" button; measured, never followed.', sel: 'plan Get started' });
  await S('trial-badge', q('main div.cta-gradient-ring').filter({ hasText: /free trial/i }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Trial badge', desc: 'The "7-day free trial" pill over the plan cards — the gradient-ring outer div.', sel: '7-day free trial badge' });
  save();
}

async function features() {
  if (!(await newPage('features'))) return;
  await sheetsFor('features');
  const g = G.features;
  // The eyebrow's DOM text may be lowercase with text-transform doing the
  // caps — match case-insensitively.
  await S('feat-eyebrow', q('main p').filter({ hasText: /^scheduling$/i }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Page eyebrow', desc: 'The tracked caps eyebrow label ("SCHEDULING", Sometype Mono) over the feature page masthead.', sel: 'feature eyebrow' }, { noScroll: true });
  await S('feat-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Feature headline', desc: '"Plan and schedule your content." — the /features/scheduling masthead.', sel: 'h1' }, { noScroll: true });
  await S('feat-cta', q('main a').filter({ hasText: /^\s*Get started for free\s*$/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Feature CTA', desc: 'The feature page\'s "Get started for free" call-to-action; measured, never followed.', sel: 'feature Get started CTA' }, { noScroll: true });
  // Further down the page the feature grid paints white <article> cards
  // (~247x225, 16px radius, soft shadow) — AI Image Generation, Vibe
  // Marketing, Post Recycling, Link Shortening.
  await S('feat-card', await domFind(page, /Post Recycling|AI Image Generation|Vibe Marketing/i, { sel: 'main article', minW: 150, minH: 150 }), ['default', 'hover'], { group: g, title: 'Feature card', desc: 'A feature card in the scheduling page grid ("AI Image Generation", "Post Recycling", …).', sel: 'feature article card' });
  save();
}

async function blog() {
  if (!(await newPage('blog'))) return;
  await sheetsFor('blog');
  const g = G.blog;
  await S('blog-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Blog headline', desc: '"FeedHive blog" — the /blog masthead.', sel: 'h1' }, { noScroll: true });
  await S('blog-card', q('main a').filter({ hasText: /Best Time to Post|Instagram/i }).filter({ visible: true }).first(), ['default', 'hover'], { group: g, title: 'Featured post card', desc: 'The featured article card on the blog index; measured, never followed.', sel: 'blog featured card' });
  await S('blog-row', q('main a').filter({ hasText: /schedule|post|instagram|linkedin|tiktok/i }).filter({ visible: true }).nth(3), ['default', 'hover'], { group: g, title: 'Article row', desc: 'An article card/row in the archive list; measured, never followed.', sel: 'blog archive row' });
  save();
}

async function toolsBio() {
  if (!(await newPage('tools-bio'))) return;
  await sheetsFor('tools-bio');
  const g = G.tools;
  await S('bio-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Tool headline', desc: '"Free AI bio generator for social media" — the /tools/bio-generator masthead.', sel: 'h1' }, { noScroll: true });
  await S('bio-platform', q('main button, main [role="radio"], main [role="tab"]').filter({ hasText: /^Instagram$/ }).filter({ visible: true }).first(), ['default', 'hover', 'selected'], { group: g, title: 'Platform option', desc: 'A platform option button (TikTok / Instagram / LinkedIn) — a local UI toggle; selected by clicking.', sel: 'bio platform Instagram' });
  await S('bio-tone', q('main button').filter({ hasText: /^Professional$/ }).filter({ visible: true }).first(), ['default', 'hover'], { group: g, title: 'Tone option', desc: 'A tone option button (Professional / Friendly / Funny / Bold / Aesthetic); measured at rest.', sel: 'bio tone Professional' });
  await S('bio-textarea', q('main textarea').filter({ visible: true }).first(), FIELD, { group: g, title: 'Bio input', desc: 'The "describe yourself" textarea; focused and typed into then cleared — never submitted.', sel: 'bio textarea' }, { fillText: 'A ceramics studio posting reels.' });
  await S('bio-submit', q('main button[type="submit"], main button').filter({ hasText: /generate/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Generate button', desc: 'The "Generate bios" submit; its states were measured but the button was never clicked — nothing was submitted.', sel: 'bio Generate bios' }, { noScroll: true });
  save();
}

async function login() {
  if (!(await newPage('login', { wait: 12000 }))) return;
  await sheetsFor('login');
  await chrome('login');
  const g = G.login;
  // The Chakra app paints a white 512x610 card (radius 20px) over the pale
  // field — found by walking up from the email input to the painted
  // container, since it has no form/main/card hook.
  await S('login-panel', await paintedCard(q('input[type="email"], input[name="email"]').filter({ visible: true }).first()), ['default'], { group: g, title: 'Sign-in card', desc: 'The sign-in card over the pale field: "Let\'s get you signed in".', sel: 'signin card (painted ancestor of email input)' }, { noScroll: true });
  await S('login-google', q('button, a').filter({ hasText: /sign in with google/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Google sign-in', desc: 'The "Sign in with Google" outlined pill; measured, never followed.', sel: 'signin Google button' }, { noScroll: true });
  await S('login-field-email', q('input[type="email"], input[name="email"]').filter({ visible: true }).first(), FIELD, { group: g, title: 'Email field (sign-in)', desc: 'The Email input on the app sign-in; focused and typed into then cleared — never submitted.', sel: 'signin input[type=email]' }, { noScroll: true, fillText: 'name@example.com' });
  await S('login-field-pass', q('input[type="password"]').filter({ visible: true }).first(), FIELD, { group: g, title: 'Password field (sign-in)', desc: 'The Password input on the app sign-in; focused and typed into then cleared — never submitted.', sel: 'signin input[type=password]' }, { noScroll: true, fillText: 'not-a-real-password' });
  await S('login-submit', q('button[type="submit"], button').filter({ hasText: /^\s*Sign in\s*$/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Sign in submit', desc: 'The sign-in submit button; its states were measured but the button was never clicked — nothing was submitted.', sel: 'signin Sign in submit' }, { noScroll: true });
  await S('login-forgot', q('a, button').filter({ hasText: /forgot your password/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Forgot password link', desc: 'The "Forgot your password?" link under the submit; measured, never followed.', sel: 'signin Forgot your password' }, { noScroll: true });
  save();
}

async function signup() {
  if (!(await newPage('signup', { wait: 12000 }))) return;
  await sheetsFor('signup');
  const g = G.signup;
  await S('signup-panel', await paintedCard(q('input').filter({ visible: true }).first()), ['default'], { group: g, title: 'Sign-up card', desc: 'The sign-up card on app.feedhive.com/signup.', sel: 'signup card (painted ancestor of first input)' }, { noScroll: true });
  await S('signup-google', q('button, a').filter({ hasText: /google/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Google sign-up', desc: 'The Google sign-up button; measured, never followed.', sel: 'signup Google button' }, { noScroll: true });
  await S('signup-field', q('input[type="email"], input[name="email"], input[type="text"]').filter({ visible: true }).first(), FIELD, { group: g, title: 'Field (sign-up)', desc: 'The first text field on the app sign-up; focused and typed into then cleared — never submitted.', sel: 'signup first input' }, { noScroll: true, fillText: 'name@example.com' });
  await S('signup-submit', q('button').filter({ hasText: /^\s*Sign up\s*$/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Sign-up submit', desc: 'The filled "Sign up" submit (the "Sign up with Google" outline is signup-google); its states were measured but the button was never clicked — nothing was submitted.', sel: 'signup Sign up submit' }, { noScroll: true });
  save();
}

async function mobile() {
  if (!(await newPage('mobile', { mobile: true, url: BASE + '/' }))) return;
  await chrome('mobile');
  const g = G.mobile;
  await S('m-header', q('header').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile header', desc: 'The phone header: FeedHive mark, the icon-only menu button and the Sign Up pill.', sel: 'mobile header' }, { noScroll: true });
  await S('m-menu-btn', q('header button[aria-label*="menu" i]').filter({ visible: true }).first(), [...B4, 'opened'], { group: g, title: 'Mobile menu button', desc: 'The icon-only button (aria-label "Open menu") that opens the phone nav overlay — a local UI toggle; the opened state was measured after clicking it.', sel: 'mobile header button[aria-label*=menu]' }, { noScroll: true, allowLink: true });
  await S('m-drawer', q('body > div, body > nav, [role="dialog"], header [class*="fixed"], header [class*="absolute"]').filter({ hasText: /Product|Pricing|Sign Up/ }).filter({ visible: true }).last(), ['default'], { group: g, title: 'Mobile nav overlay', desc: 'The nav overlay opened by the menu button; its links were never followed.', sel: 'mobile nav overlay' }, { open: openMobileMenu, noScroll: true, noReset: true });
  await page.keyboard.press('Escape').catch(() => {});
  await S('m-hero-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile hero headline', desc: 'The masthead at 390 wide.', sel: 'mobile h1' });
  await S('m-hero-cta', q('main a').filter({ hasText: /^\s*Get started for free\s*$/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Mobile hero CTA', desc: 'The hero "Get started for free" button at 390 wide; measured, never followed.', sel: 'mobile hero CTA' });
  save();
}

run = new Date().toISOString().slice(0, 10);
out._meta.read = run;
out._meta.viewport = '1440 x 900 (mobile group 390 x 844); every www.feedhive.com page paints light — no user theme toggle, no dark mode; app.feedhive.com sign-in/up is a separate light Chakra-UI app';
out._meta.tool = 'tools/capture/public/measure.mjs';
const { browser, context: ctx0 } = await launch();
context = ctx0;
const pages = process.argv.slice(2);
const plan = { home, pricing, features, blog, 'tools-bio': toolsBio, login, signup, mobile };
const order = Object.keys(plan).filter((k) => !pages.length || pages.includes(k));
const finishedPages = new Set();
try {
  for (const k of order) { if (k !== 'mobile') { await plan[k](); finishedPages.add(k); } }
  if (!pages.length || pages.includes('mobile')) { await plan.mobile(); finishedPages.add('mobile'); }
  // Reduced-motion check on an element that transitions (a nav pill's
  // hover), so the delta is meaningful.
  if (!pages.length || pages.includes('home')) await reducedMotion('home', 'header a[href="/pricing"]');
} finally {
  for (const [key, c] of Object.entries(out.components)) {
    // An untouched entry is pruned only when its page finished this run: a
    // page the run never reached, and an edge-blocked route, keeps its earlier
    // readings under their original provenance instead of being erased and
    // republished.
    if (!touched.has(key) && !pages.length && finishedPages.has(c.page) && !failedPages.has(c.page)) { delete out.components[key]; continue; }
    const want = listed.get(key);
    if (want) for (const st of Object.keys(c.states || {})) if (!want.has(st)) delete c.states[st];
  }
  save();
  await browser.close();
}
console.log('components-computed.json:', Object.keys(out.components).length, 'components');
