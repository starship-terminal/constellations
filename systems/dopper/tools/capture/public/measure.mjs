// Measures dopper.com's public components in every state reachable without
// signing in, checking out or submitting anything.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node measure.mjs [page ...]
//
// Pages: home shop category pdp cart login mobile.
// Writes raw/components-computed.json (merged) and one crop per component and
// state into components/crops/; raw/measurements.md is built by
// build-measurements.mjs.
//
// Two hosts, one brand system: www.dopper.com is a Next.js/Storyblok app
// where every class is a build hash (specs select by role, text and
// structure) and shop.dopper.com is Magento 2 (theme Dopper/dopper_b2c) with
// stable .page-header/.navigation/.tocart class names. Nothing is sent,
// bought or signed into: the only presses are local UI toggles — the Bottle
// mega-menu, the collections tab bar, the PLP filter sheet, the PDP
// configurator accordions, the mobile menu and the login fields' own focus.
// The Cookiebot consent dialog and the chat widget are hidden, never
// answered.
import fs from 'node:fs';
import path from 'node:path';
import { BASE, SHOP, M, launch, patch, open, closePromo, domFind, styleOf, crop, centre, RAW, UA, UA_MOBILE } from './lib.mjs';

const OUT = process.env.OUT_JSON || path.join(RAW, 'components-computed.json');
const out = fs.existsSync(OUT) ? JSON.parse(fs.readFileSync(OUT, 'utf8')) : {};
out._meta ??= {};
out.components ??= {};
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const save = () => fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');
// page key -> url; shop pages live on the storefront host.
const URLS = {
  home: BASE + '/',
  shop: SHOP + '/', category: SHOP + '/bottles', pdp: SHOP + '/dopper-original-pacific-blue',
  cart: SHOP + '/checkout/cart/', login: SHOP + '/customer/account/login/', mobile: BASE + '/', 'mobile-category': SHOP + '/bottles',
};
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

async function newPage(key, { mobile = false, wait = 8000, promo = 'close' } = {}) {
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
  const cleared = await open(page, URLS[key], { wait, promo });  // false: the bot check did not clear (lib.mjs)
  if (!cleared || (await blocked())) { log('  BLOCKED', key); failedPages.add(key); await page.close().catch(() => {}); await ctx.close().catch(() => {}); return false; }
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
  // Blur whatever holds focus wherever it actually lives: for a control inside
  // DOPPER-NAVIGATION's shadow root, document.activeElement is the host, so the
  // focused node is the root's own activeElement.
  await page.evaluate(() => {
    let active = document.activeElement;
    while (active && active.shadowRoot && active.shadowRoot.activeElement) active = active.shadowRoot.activeElement;
    if (active && active.blur) active.blur();
  }).catch(() => {});
  const vw = page.viewportSize()?.width ?? 1440;
  await page.mouse.move(vw - 2, 2);
  await page.waitForTimeout(250);
}

async function kbFocus(loc) {
  await loc.evaluate((el) => el.focus());
  await page.keyboard.press('Shift+Tab');
  await page.keyboard.press('Tab');
  // A control inside a shadow root (DOPPER-NAVIGATION's nav links and buttons)
  // never lands on document.activeElement — that reads the shadow host. :focus
  // and :focus-within are evaluated on the element in its own root, so they see
  // focus wherever it actually landed.
  const hasFocus = (el) => el.matches(':focus') || el.matches(':focus-within')
    || el === document.activeElement || el.contains(document.activeElement);
  let ok = await loc.evaluate(hasFocus);
  let how = 'Shift+Tab, Tab';
  if (!ok) {
    await page.keyboard.press('Shift');
    await loc.evaluate((el) => el.focus());
    ok = await loc.evaluate(hasFocus);
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
  Object.assign(c, { page: current, run, url: URLS[current] }, meta);
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
  const keep = prev && !prev.missing && Object.keys(prev.states || {}).length ? { page: prev.page, run: prev.run, url: prev.url } : null;
  comp(key, { title: meta.title, group: meta.group, desc: meta.desc, selector: meta.sel });
  // An entry flagged missing (misidentified) holds no readings: drop any states it still carries so
  // a later miss cannot bring them back as live readings under recaptureMissed.
  if (prev && prev.missing) { out.components[key].states = {}; delete out.components[key].note; }
  if (!listed.has(key)) listed.set(key, new Set());
  for (const st of list) listed.get(key).add(st);
  delete out.components[key].missing;
  if (opts.open) { await reset(); try { await opts.open(); } catch (e) { log('  ! open failed', key, String(e.message).slice(0, 80)); } }
  const loc = target.filter({ visible: true }).first();
  await loc.waitFor({ state: 'visible', timeout: 6000 }).catch(() => {});
  if (!(await loc.count())) {
    const has = Object.keys(out.components[key].states || {}).length > 0;
    log('  ! missing', key, has ? '(earlier states kept)' : '');
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
      } else if (st === 'opened') {
        if (opts.noToggle) via = 'held open by an earlier toggle';
        else {
          await toggle(loc, { allowLink: opts.allowLink }); await page.waitForTimeout(900); via = 'own toggle';
          // close it again with the same control so it cannot hold focus or cover the next reading
          undo = async () => { await page.keyboard.press('Escape'); if ((await loc.getAttribute('aria-expanded').catch(() => null)) === 'true' || (await loc.evaluate((el) => !!el.closest('details[open]')).catch(() => false))) await toggle(loc, { allowLink: opts.allowLink }); await page.waitForTimeout(400); };
        }
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
const NEVER = /^(send|submit|sign in|log ?in|login|create|add|download|buy|purchase|pay|checkout|join|subscribe|save|apply|accept|reject|start|get started|claim|share|export|select|continue|claim this offer|try again|order( free)?( sample)?|add to cart|add to bag|go to checkout|proceed to checkout|back to shop|shop now|shop our collection|watch now|create an account|buy a bottle|shop insulated)$/i;
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
async function reducedMotion(key, sel, url) {
  out._meta.reducedMotion ??= {};
  try {
    const b = context.browser();
    const ctx = await b.newContext({ viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1, userAgent: UA, locale: 'en-US', reducedMotion: 'reduce' });
    await patch(ctx);
    const p = await ctx.newPage();
    await p.goto(url || URLS[key], { waitUntil: 'domcontentloaded', timeout: 90000 }).catch(() => {});
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

// Scrolls the page down in steps and back to the top: home sections hydrate
// lazily, so a cold page only mounts the hero region when the run reaches it.
async function lazyLoad() {
  await page.evaluate(async () => {
    const h = document.documentElement.scrollHeight;
    for (let y = 0; y <= h; y += 800) { scrollTo(0, y); await new Promise((r) => setTimeout(r, 120)); }
    scrollTo(0, 0);
  });
  await page.waitForTimeout(1600);
}

// www.dopper.com paints its top bar as the DOPPER-NAVIGATION custom element
// (.header_nav__*) — there is no <header>/<nav> tag. The shop wraps the same
// component in Magento's .page-header.
const NAV = 'dopper-navigation, .page-header, header';

// The header's Bottle button opens the yellow mega-menu (a hover or click
// toggles it). The triggers sit in DOPPER-NAVIGATION's shadow root, so the
// click uses a Playwright locator (locators pierce shadow DOM).
// The mega-menu's copy ("A range of reusable bottles", "so everyone can just
// refill") is also the static "Explore our solutions" section's copy, so a
// document-wide text match lands on ordinary page content. The flyout only
// counts when the match lives inside DOPPER-NAVIGATION's shadow root or a
// fixed/absolute overlay — the shapes an opened menu actually takes.
const menuScope = `(() => {
  const nav = document.querySelector('dopper-navigation');
  const inOverlay = (e) => {
    for (let n = e; n; n = n.parentElement || (n.getRootNode && n.getRootNode().host)) {
      if (n === document.body) break;
      const cs = getComputedStyle(n);
      if (cs.position === 'fixed' || cs.position === 'absolute') return true;
    }
    return false;
  };
  const roots = [nav && nav.shadowRoot, document].filter(Boolean);
  const heads = [];
  for (const root of roots) {
    for (const e of root.querySelectorAll('h1,h2,h3,h4,p,div,span')) {
      const t = e.innerText || '';
      if (!/range of reusable|everyone can just refill/i.test(t) || !e.getBoundingClientRect().height) continue;
      if ((nav && root === nav.shadowRoot) || inOverlay(e)) heads.push(e);
    }
  }
  return heads;
})()`;

async function openFlyout() {
  const t = q('dopper-navigation button').filter({ hasText: /^\s*Bottle\s*$/ }).filter({ visible: true }).first();
  if (!(await t.count())) { log('  ! flyout trigger not found'); return false; }
  await t.hover().catch(() => {});
  await page.waitForTimeout(900);
  // Class names are build hashes — the open signal is the flyout's own copy
  // ("so everyone can just refill") being painted inside the opened panel.
  const flyoutOpen = () => page.evaluate(`${menuScope}.length > 0`);
  if (!(await flyoutOpen())) await t.click({ timeout: 5000 }).catch(() => t.evaluate((el) => el.click()));
  await page.waitForTimeout(900);
  if (!(await flyoutOpen())) { log('  ! flyout did not open'); return false; }
  await page.waitForTimeout(1400);
  return true;
}

// Marks the opened mega-menu panel: the first visible ancestor of the
// flyout's "A range of reusable bottles" heading wide enough to be the panel —
// scoped to the opened menu, never the static section with the same copy.
async function markFlyout() {
  await page.evaluate(`{
    const heads = ${menuScope};
    const h = heads[0];
    if (!h) return;
    let n = h;
    for (let i = 0; i < 9 && n; i++) {
      n = n.parentElement || (n.getRootNode && n.getRootNode().host);
      if (!n || n === document.body) break;
      const r = n.getBoundingClientRect();
      if (r.width > 500 && r.height > 300) { n.setAttribute('data-m-mark', 'flyout'); return; }
    }
    h.setAttribute('data-m-mark', 'flyout');
  }`);
}

// Marks a home content card: the smallest ancestor of a card heading that
// also holds the card's body copy and a CTA. Takes a Playwright locator so
// lazy-mounted headings are scrolled into view first.
async function markCard(loc, tag) {
  const el = await loc.elementHandle().catch(() => null);
  if (!el) return;
  await loc.scrollIntoViewIfNeeded().catch(() => {});
  await page.waitForTimeout(700);
  await el.evaluate((h, tg) => {
    let n = h;
    for (let i = 0; i < 10 && n.parentElement; i++) {
      n = n.parentElement;
      const r = n.getBoundingClientRect();
      if (r.width > 300 && r.width < 1500 && r.height > 200 && r.height < 1400 && (n.querySelector('a,button,[role="button"],[role="link"]'))) { n.setAttribute('data-m-mark', tg); return; }
    }
    h.parentElement && h.parentElement.setAttribute('data-m-mark', tg);
  }, tag);
}

// Marks the leaf row inside the marked filter sheet holding one option's
// text (under 120px tall). Scoped to the opened sheet: without a panel mark
// nothing is marked (the spec records missing), and product cards/links are
// never filter rows.
const markRow = (re, tag) => page.evaluate(([src, flags, tg]) => {
  const rx = new RegExp(src, flags);
  const panel = document.querySelector('[data-m-mark="fpanel"]');
  if (!panel) return;
  const cand = [...panel.querySelectorAll('li, a, label, div, span')].filter((e) => rx.test(e.innerText || '') && e.getBoundingClientRect().height > 0 && e.getBoundingClientRect().height < 120 && !e.closest('.product-item, .products, [class*="product-item"]'));
  const leaf = cand.filter((e) => !cand.some((o) => o !== e && e.contains(o)))[0] || cand[0];
  leaf && leaf.setAttribute('data-m-mark', tg);
}, [re.source, re.flags, tag]);

// Marks the PLP product card: the smallest ancestor of a product link that
// holds an image, a name and a price.
async function markProductCard() {
  await page.evaluate(() => {
    const li = [...document.querySelectorAll('li.item, .product-item, .products li')].find((n) => n.getBoundingClientRect().width > 150 && n.getBoundingClientRect().height > 250);
    if (li) { li.setAttribute('data-m-mark', 'pcard'); return; }
    const price = [...document.querySelectorAll('.price')].find((n) => /€/.test(n.innerText || '') && n.getBoundingClientRect().width > 0);
    if (!price) return;
    let n = price;
    for (let i = 0; i < 8 && n.parentElement; i++) {
      n = n.parentElement;
      const r = n.getBoundingClientRect();
      if (r.width > 150 && r.height > 250 && n.querySelector('img')) { n.setAttribute('data-m-mark', 'pcard'); return; }
    }
  });
}

// Marks the open filter sheet on the shop PLP: the panel holding the
// Collection/Size/Colour groups.
async function markFilterPanel() {
  await page.evaluate(() => {
    const h = [...document.querySelectorAll('h1,h2,h3,h4,strong,span,div')].find((e) => /^\s*Collection\s*$/.test(e.innerText || '') && e.getBoundingClientRect().height > 0);
    if (!h) return;
    let n = h;
    for (let i = 0; i < 9 && n.parentElement; i++) {
      n = n.parentElement;
      const r = n.getBoundingClientRect();
      const t = n.innerText || '';
      if (/Collection/.test(t) && /Size/.test(t) && r.width > 300 && r.height > 300) { n.setAttribute('data-m-mark', 'fpanel'); return; }
    }
    h.setAttribute('data-m-mark', 'fpanel');
  });
}

// Marks a Magento form card: the smallest ancestor of a heading that holds
// the card's fields/actions.
async function markFormCard(headingRe, tag) {
  await page.evaluate(([src, flags, tg]) => {
    const re = new RegExp(src, flags);
    const h = [...document.querySelectorAll('h1,h2,h3,h4,strong,span')].find((e) => re.test(e.innerText || '') && e.getBoundingClientRect().height > 0);
    if (!h) return;
    let n = h;
    for (let i = 0; i < 10 && n.parentElement; i++) {
      n = n.parentElement;
      const r = n.getBoundingClientRect();
      if (r.width > 300 && r.height > 150 && r.height < 1200) { n.setAttribute('data-m-mark', tg); return; }
    }
    h.setAttribute('data-m-mark', tg);
  }, [headingRe.source, headingRe.flags, tag]);
}

// Marks the opened mobile navigation panel: a fixed overlay holding the nav
// links (Bottle / Travel Mug / Mission).
async function markMobileMenu() {
  await page.evaluate(() => {
    const nav = document.querySelector('dopper-navigation');
    const root = (nav && nav.shadowRoot) || document;
    const cand = [...root.querySelectorAll('div,nav,aside,section')].filter((el) => {
      const r = el.getBoundingClientRect();
      const cs = getComputedStyle(el);
      const t = el.innerText || '';
      return (cs.position === 'fixed' || cs.position === 'absolute') && r.height > innerHeight * 0.55 && r.width > innerWidth * 0.6
        && /Bottle/.test(t) && /Travel Mug/.test(t) && /Mission/.test(t) && t.length < 9000;
    }).sort((a, b) => (a.innerText || '').length - (b.innerText || '').length);
    if (cand[0]) cand[0].setAttribute('data-m-mark', 'mmenu');
  });
}

const G = {
  shell: 'Shell and navigation', home: 'Home (www)', shop: 'Shop', plp: 'Product list (PLP)',
  pdp: 'Product page (PDP)', cart: 'Cart', login: 'Login and signup', footer: 'Footer',
  mobile: 'Mobile (390 wide)',
};

async function home() {
  if (!(await newPage('home', { wait: 9000 }))) return;
  await sheetsFor('home');
  await chrome('home');
  const g = G.shell;
  // The DOPPER-NAVIGATION custom element is position:fixed but 0x0 — its
  // shadow-root children paint the bar. Mark the smallest ancestor of the
  // Bottle trigger that spans the viewport: the bar shell.
  await page.evaluate(() => {
    const nav = document.querySelector('dopper-navigation');
    const root = (nav && nav.shadowRoot) || document;
    const b = [...root.querySelectorAll('button, [role="button"], a')].find((e) => /^\s*Bottle\s*$/i.test(e.innerText || '') && e.getBoundingClientRect().width > 0);
    if (!b) { nav && nav.setAttribute('data-m-mark', 'hbar'); return; }
    let n = b;
    for (let i = 0; i < 10 && n.parentElement; i++) {
      n = n.parentElement;
      const r = n.getBoundingClientRect();
      if (r.width > 1000 && r.height > 30 && r.height < 300) { n.setAttribute('data-m-mark', 'hbar'); return; }
    }
    n = b.parentElement;
    while (n && n !== nav) { const r = n.getBoundingClientRect(); if (r.width > 500) { n.setAttribute('data-m-mark', 'hbar'); return; } n = n.parentElement; }
    nav && nav.setAttribute('data-m-mark', 'hbar');
  });
  await S('header', q('[data-m-mark="hbar"], dopper-navigation').filter({ visible: true }).first(), ['default'], { group: g, title: 'Header', desc: 'The transparent-then-solid top bar (the DOPPER-NAVIGATION custom element): flyout triggers (Bottle / Travel Mug / Tap / Mission / Get Involved), the dopper. wordmark, right links (Impact report / Find a Store / For Businesses / EN) and the bag button.', sel: 'dopper-navigation' }, { noScroll: true });
  await S('logo', q('dopper-navigation a').filter({ has: page.locator('svg') }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Logo', desc: 'The dopper. wordmark anchor (svg, centred in the bar).', sel: 'dopper-navigation a svg' }, { noScroll: true });
  await S('nav-trigger', q('dopper-navigation button').filter({ hasText: /^\s*Bottle\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Nav trigger', desc: 'The Bottle flyout trigger in the header; toggled, never followed.', sel: 'dopper-navigation button Bottle' }, { noScroll: true });
  await S('nav-link', q('dopper-navigation a').filter({ hasText: /^\s*Impact report\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Nav link', desc: 'A right-side header link (Impact report).', sel: 'dopper-navigation a Impact report' }, { noScroll: true });
  await S('bag-button', q('dopper-navigation a[href*="checkout/cart"]').filter({ visible: true }).first(), B4, { group: g, title: 'Bag button', desc: 'The shopping-bag icon button, right end of the header (light-blue circle); links to the cart, never followed.', sel: 'dopper-navigation a[href*=cart]' }, { noScroll: true });
  const g2 = G.home;
  await S('hero-display', q('h1').filter({ visible: true }).first(), ['default'], { group: g2, title: 'Hero display', desc: 'The h1 over the full-bleed video hero ("Whatever the season") — Dopper display type on media.', sel: 'h1' });
  const watch = await domFind(page, /^\s*Watch now\s*$/, { sel: 'a, button', tag: 'btn1' });
  await S('btn-dark', watch, B4, { group: g2, title: 'Button, dark', desc: 'The deep-sea filled pill CTA ("Watch now") on the video hero.', sel: 'hero dark pill' });
  const outline = await domFind(page, /^\s*Shop our collection\s*$/, { sel: 'a, button', tag: 'btn2' });
  await S('btn-outline', outline, B4, { group: g2, title: 'Button, outline', desc: 'The outline pill CTA ("Shop our collection") on the video hero.', sel: 'hero outline pill' });
  // Mega-menu: open the Bottle flyout and measure the panel + its CTA. The
  // header auto-hides on scroll and the menu closes on blur — each spec
  // re-opens it via openFlyout and skips reset() while it is up.
  await page.evaluate(() => scrollTo(0, 0));
  await page.waitForTimeout(800);
  const openAndMark = async () => { if (await openFlyout()) await markFlyout(); };
  await S('flyout', q('[data-m-mark="flyout"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mega-menu', desc: 'The yellow Bottle flyout (tab pills across the top, feature columns, CTAs and a product photo).', sel: 'opened Bottle menu' }, { noScroll: true, noReset: true, open: openAndMark });
  // "Map" and "Community" exist only inside the opened flyout's top pill row;
  // the marked panel also holds the bottom card carousel.
  await S('flyout-tab', q('button, a, [role="tab"], span, h1, h2, h3, h4, p, div').filter({ hasText: /^\s*(Map|Community)\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Flyout tab', desc: 'A pill tab across the top of the opened menu (Bottle active on yellow).', sel: 'flyout tab pill' }, { noScroll: true, noReset: true, open: openAndMark });
  await S('flyout-card', q('[data-m-mark="flyout"] button, [data-m-mark="flyout"] a').filter({ hasText: /range of reusable|mug that keeps/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Flyout card', desc: 'An option card inside the flyout carousel ("Bottle — A range of reusable bottles…").', sel: 'flyout option card' }, { noScroll: true, noReset: true, open: openAndMark });
  // The flyout card's own CTAs ("Buy a bottle", "Customise 60+ bottles") sit
  // inside the card button's inner markup — no standalone leaf exposes them
  // (probably a closed shadow root). The same deep-sea pill is measured as
  // btn-dark and add-to-cart instead.
  await page.keyboard.press('Escape'); await page.waitForTimeout(600);
  await lazyLoad();
  // The collections showcase: a tab bar of product buttons over swappable
  // cards ("The collections").
  const tab = q('button:has(h3), [role="tab"]:has(h3)').filter({ hasText: /Insulated|Steel|Original/ }).filter({ visible: true }).first();
  if (await tab.count()) {
    await tab.click({ timeout: 5000 }).catch(() => {});
    await page.waitForTimeout(900);
  }
  await S('collection-tab', tab, B4, { group: g2, title: 'Collection tab', desc: 'A product tab inside "The collections" showcase; toggled to swap the card below.', sel: 'collections tab' });
  await S('collections-heading', q('h1, h2, h3, h4, p, span, div').filter({ hasText: /^\s*The\s+collections\s*$/i }).filter({ visible: true }).first(), ['default'], { group: g2, title: 'Section heading', desc: 'A section heading ("The collections") — Gilroy bold, deep-sea.', sel: 'collections heading' });
  // A content card mid-page: "Refill what matters" band or similar.
  await markCard(q('h1, h2, h3, h4, p').filter({ hasText: /Refill what matters|Rewriting the system|Make your company part|Calculate your impact/i }).filter({ visible: true }).first(), 'hcard');
  await S('content-card', q('[data-m-mark="hcard"]').filter({ visible: true }).first(), ['default'], { group: g2, title: 'Content card', desc: 'A home split card (copy + CTA beside a photo tile).', sel: 'home content card' });
  // Footer (last block on the page).
  await S('footer', q('footer').filter({ visible: true }).last(), ['default'], { group: G.footer, title: 'Footer', desc: 'The sand footer: newsletter band, "Just refill" columns, social icons, certification and payment logos.', sel: 'footer' });
  const emailIn = q('input[type="email"], input[placeholder*="email" i], input[name*="email" i]').filter({ visible: true }).first();
  await S('newsletter-input', emailIn, ['default', 'focused'], { group: G.footer, title: 'Newsletter input', desc: 'The email field in the footer newsletter band; focused, never submitted.', sel: 'footer email input' });
  save();
}

async function shop() {
  if (!(await newPage('shop', { wait: 9000 }))) return;
  await sheetsFor('shop');
  await chrome('shop');
  const g = G.shop;
  await S('shop-header', q('dopper-navigation, .page-header, header').filter({ visible: true }).first(), ['default'], { group: g, title: 'Shop header', desc: 'The same dopper header on the Magento storefront, plus the catalog nav row below it.', sel: 'dopper-navigation' }, { noScroll: true });
  await S('shop-nav', q('.navigation, nav[role="navigation"], .sections.nav-sections').filter({ visible: true }).first(), ['default'], { group: g, title: 'Shop nav', desc: 'The catalog nav row (All products / Mugs / Bottles / Accessories / Spare parts / E-Gift Card / Last chance).', sel: '.navigation' }, { noScroll: true });
  await S('shop-nav-link', q('.navigation a, nav a').filter({ hasText: /^\s*(All products|Bottles)\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Shop nav link', desc: 'A catalog nav item; "All products" paints the active darkBlue.', sel: '.navigation a' }, { noScroll: true });
  const shopNow = await domFind(page, /^\s*Shop now\s*$/, { sel: 'a, button', tag: 'sbtn' });
  await S('shop-hero-button', shopNow, B4, { group: g, title: 'Shop CTA', desc: 'The darkBlue pill CTA on a shop hero tile ("Shop now").', sel: 'shop hero Shop now' });
  save();
}

async function category() {
  if (!(await newPage('category', { wait: 9000 }))) return;
  await sheetsFor('category');
  await chrome('category');
  const g = G.plp;
  await S('plp-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'PLP title', desc: '"Bottles" — Dopper display type, deep-sea, centred over the sand field.', sel: 'h1' });
  await S('plp-sub', q('.category-payoff, .category-view p, .page-title-wrapper p').filter({ visible: true }).first(), ['default'], { group: g, title: 'PLP subtitle', desc: 'The one-line lede under the title ("End packaged water. Just refill your Dopper bottle.").', sel: '.category-payoff' });
  const fb = await domFind(page, /Filters/i, { sel: 'button, a', tag: 'fbtn' });
  await S('filters-button', fb, B4, { group: g, title: 'Filters button', desc: 'The teal "+ Filters" pill that opens the filter sheet (open by default on desktop).', sel: '+ Filters' });
  // The filter sheet is open on desktop load; mark and measure it.
  await markFilterPanel();
  await S('filter-panel', q('[data-m-mark="fpanel"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Filter panel', desc: 'The light-blue (darkBlue-3) filter sheet: Collection/Size radio groups, Colour swatches, Bundle checkbox.', sel: 'filter sheet' }, { crop: true, pad: 0 });
  // The Collection/Size options are custom rows (a styled circle + name +
  // muted count), not real inputs.
  await markRow(/Original/, 'frow');
  await S('filter-radio', q('[data-m-mark="frow"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Filter radio', desc: 'A Collection/Size option row: ring + name + muted item count.', sel: 'filter option row' });
  await S('filter-swatch', q('[data-m-mark="fpanel"] .swatch-option, [data-m-mark="fpanel"] [class*="swatch" i], .swatch-attribute .swatch-option').filter({ visible: true }).first(), B4, { group: g, title: 'Colour swatch', desc: 'A colour-dot swatch filter option.', sel: 'colour swatch' });
  await markRow(/Bundle/, 'fbox');
  await S('filter-checkbox', q('[data-m-mark="fbox"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Filter checkbox', desc: 'The Bundle option: box checkbox + "Flip Straw Bundle" + count.', sel: 'filter checkbox row' });
  await S('filter-close', q('[data-m-mark="fpanel"] button, .filter-current + button, button[aria-label*="lose" i]').filter({ visible: true }).first(), B4, { group: g, title: 'Filter close', desc: 'The deep-sea circle × button closing the filter sheet.', sel: 'filter X button' });
  await markProductCard();
  await S('product-card', q('[data-m-mark="pcard"]').filter({ visible: true }).first(), ['default', 'hover'], { group: g, title: 'Product card', desc: 'A PLP card: product photo, optional badge chip, name, price in EUR.', sel: '.product-item' });
  await S('product-price', q('[data-m-mark="pcard"] .price, [data-m-mark="pcard"] [class*="price"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Price', desc: 'The EUR price on a product card.', sel: '.price' });
  await S('product-badge', q('[data-m-mark="pcard"] *').filter({ hasText: /^\s*(New|Sale|%\s*off)\s*$/i }).filter({ visible: true }).last(), ['default'], { group: g, title: 'Badge chip', desc: 'The outlined "New" chip on a product card.', sel: 'product badge' });
  save();
}

async function pdp() {
  if (!(await newPage('pdp', { wait: 10000 }))) return;
  await sheetsFor('pdp');
  await chrome('pdp');
  const g = G.pdp;
  // Nudge the gallery: images lazy-load, and the buy box skeleton resolves.
  await lazyLoad();
  await S('breadcrumb', q('.breadcrumbs, nav[aria-label*="rumb" i], .breadcrumb').filter({ visible: true }).first(), ['default'], { group: g, title: 'Breadcrumb', desc: 'Home > Original - Pacific Blue trail above the gallery.', sel: '.breadcrumbs' });
  await S('pdp-title', q('h1, .page-title, [itemprop="name"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'PDP title', desc: 'The product name ("Original - Pacific Blue").', sel: 'PDP h1' });
  await S('pdp-price', q('.price-box .price, .product-info-price .price, [data-price-type] .price').filter({ visible: true }).first(), ['default'], { group: g, title: 'PDP price', desc: '€14.95 under the title.', sel: '.price-box .price' });
  const atc = await domFind(page, /^\s*Add to cart\s*$/, { sel: 'button, a', tag: 'atc' });
  await S('add-to-cart', atc, B4, { group: g, title: 'Add to cart', desc: 'The darkBlue pill buy button; measured, never pressed for real (pressed state is CDP-forced).', sel: '.tocart' });
  // The configurator rows: "Choose collection / Select your pattern / Own
  // text or image / Accessories" — expandable selects.
  const sel = await domFind(page, /^\s*(Choose collection|Select your pattern|Own text or image|Accessories)\s*$/, { sel: 'button, a, [role="button"], summary, div', tag: 'psel', leaf: true });
  await S('pdp-option', sel, ['default', 'opened'], { group: g, title: 'Configurator row', desc: 'A collapsed configurator row in the buy box; the "opened" state presses its own toggle (a local expand).', sel: 'pdp option row' });
  const sw = q('.swatch-option, [class*="swatch" i] [class*="option" i], [data-option-type] > *, [class*="swatch" i] li, [class*="swatch" i] a, [class*="swatch" i]').filter({ visible: true }).first();
  await S('pdp-swatch', sw, ['default'], { group: g, title: 'PDP swatch', desc: 'A colour dot in "Choose your colour" (the selected ring vs the rest).', sel: 'pdp swatch' });
  const feat = await domFind(page, /Lightweight and extremely|Leakproof|Cradle to Cradle/i, { sel: 'li, div, span', tag: 'feat', leaf: true });
  await S('pdp-feature', feat, ['default'], { group: g, title: 'Feature line', desc: 'An icon + claim row in the buy box (Lightweight and extremely tough).', sel: 'pdp feature' });
  save();
}

async function cart() {
  if (!(await newPage('cart', { wait: 9000 }))) return;
  await chrome('cart');
  const g = G.cart;
  await S('cart-title', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Cart title', desc: '"Your cart" — darkBlue Dopper display on sand.', sel: 'cart h1' });
  // The "← Continue shopping / Customer Service" band: smallest ancestor of
  // the link under 120px tall.
  await page.evaluate(() => {
    const a = [...document.querySelectorAll('a')].find((e) => /Continue shopping/i.test(e.innerText || '') && e.getBoundingClientRect().width > 0);
    if (!a) return;
    let n = a;
    for (let i = 0; i < 8 && n.parentElement; i++) { n = n.parentElement; const r = n.getBoundingClientRect(); if (r.width > 800 && r.height > 30 && r.height < 140) { n.setAttribute('data-m-mark', 'cstrip'); return; } }
  });
  await S('cart-strip', q('[data-m-mark="cstrip"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Cart strip', desc: 'The darkBlue-3 band under the header: ← Continue shopping left, Customer Service right.', sel: 'cart strip' });
  await markFormCard(/basket is empty/i, 'cartb');
  await S('cart-empty', q('[data-m-mark="cartb"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Empty cart', desc: 'The empty-basket block: "Be my hero" illustration, copy and a Back to shop CTA. A filled cart was not exercised (nothing is added).', sel: 'empty cart block' });
  const back = await domFind(page, /^\s*Back to shop\s*$/, { sel: 'a, button', tag: 'back' });
  await S('cart-cta', back, B4, { group: g, title: 'Cart CTA', desc: 'The darkBlue pill "Back to shop" in the empty state.', sel: 'Back to shop' });
  save();
}

async function login() {
  if (!(await newPage('login', { wait: 9000 }))) return;
  await sheetsFor('login');
  await chrome('login');
  const g = G.login;
  await markFormCard(/Registered Customers/i, 'logcard');
  await S('login-card', q('[data-m-mark="logcard"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Login card', desc: 'The darkBlue "Registered Customers" card: Email + Password fields, Sign in, Show password, Remember Me, Forgot link.', sel: 'login card' });
  const email = q('input#email, input[name="login[username]"], input[type="email"]').filter({ visible: true }).first();
  await S('login-email', email, ['default', 'focused', 'filled'], { group: g, title: 'Email field', desc: 'The white rounded Email field on the blue card; focused and typed into, then cleared — nothing sent.', sel: '#email' });
  const pass = q('input#pass, input[name="login[password]"], input[type="password"]').filter({ visible: true }).first();
  await S('login-password', pass, ['default', 'focused'], { group: g, title: 'Password field', desc: 'The Password field beside the Sign in button.', sel: '#pass' });
  const signin = await domFind(page, /^\s*Sign in\s*$/, { sel: 'button, input[type="submit"]', tag: 'sin' });
  await S('login-button', signin, B4, { group: g, title: 'Sign in button', desc: 'The deep-sea pill Sign in inside the blue card; never pressed (pressed state is CDP-forced).', sel: '#send2' });
  await S('login-label', q('label').filter({ hasText: /^\s*Email\s*\*?\s*$/ }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Field label', desc: 'The small sand label above a field on the blue card.', sel: 'label' });
  await S('login-checkbox', q('label').filter({ hasText: /Remember Me|Show password/i }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Checkbox row', desc: 'The Remember Me / Show password checkbox rows under the password field.', sel: 'checkbox label' });
  const forgot = await domFind(page, /Forgot Your Password/i, { sel: 'a', tag: 'fgt' });
  await S('login-link', forgot, B4, { group: g, title: 'Form link', desc: '"Forgot Your Password?" — sand text link on the blue card.', sel: 'forgot link' });
  await markFormCard(/New Customers/i, 'newcard');
  await S('new-card', q('[data-m-mark="newcard"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'New customers card', desc: 'The darkBlue-3 "New Customers" card with benefits copy and a Create an Account CTA.', sel: 'new customers card' });
  const create = await domFind(page, /^\s*Create an Account\s*$/, { sel: 'a, button', tag: 'cta2' });
  await S('create-button', create, B4, { group: g, title: 'Create account', desc: 'The darkBlue pill in the New Customers card; a link, never followed.', sel: 'create account' });
  save();
}

async function mobile() {
  if (!(await newPage('mobile', { mobile: true, wait: 9000 }))) return;
  await chrome('mobile');
  const g = G.mobile;
  // Same 0x0 fixed custom element as desktop — mark the bar shell via the
  // burger's ancestor chain.
  await page.evaluate(() => {
    const nav = document.querySelector('dopper-navigation');
    const root = (nav && nav.shadowRoot) || document;
    const b = [...root.querySelectorAll('button, [role="button"], a')].find((e) => /menu|navigation/i.test(e.getAttribute('aria-label') || '') || (e.querySelector('svg') && e.getBoundingClientRect().width > 0));
    if (!b) { nav && nav.setAttribute('data-m-mark', 'mhbar'); return; }
    let n = b;
    for (let i = 0; i < 10 && n.parentElement; i++) { n = n.parentElement; const r = n.getBoundingClientRect(); if (r.width > 300 && r.height > 30 && r.height < 300) { n.setAttribute('data-m-mark', 'mhbar'); return; } }
    nav && nav.setAttribute('data-m-mark', 'mhbar');
  });
  await S('m-header', q('[data-m-mark="mhbar"], dopper-navigation').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile header', desc: 'The 390 bar: dopper. wordmark left-centre and the sand burger circle.', sel: 'dopper-navigation @390' }, { noScroll: true });
  const burger = q('dopper-navigation button, header button').filter({ visible: true }).first();
  await S('m-burger', burger, B4, { group: g, title: 'Burger button', desc: 'The sand-circle hamburger opening the full-screen menu.', sel: 'burger' }, { noScroll: true });
  await S('m-hero', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile display', desc: 'The hero h1 at 390.', sel: 'h1 @390' });
  try {
    const menu = q('dopper-navigation button, header button').filter({ visible: true }).first();
    if (await menu.count()) { await menu.click({ timeout: 5000 }).catch(() => menu.evaluate((el) => el.click())); await page.waitForTimeout(1600); }
  } catch (e) { log('  ! mobile menu toggle failed', String(e.message).split('\n')[0]); }
  await markMobileMenu();
  await S('m-menu-open', q('[data-m-mark="mmenu"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile menu, open', desc: 'The darkBlue full-screen menu: large white rows, outline pills, bag and × controls.', sel: 'opened mobile menu' }, { noScroll: true });
  await S('m-nav-item', q('[data-m-mark="mmenu"] a, [data-m-mark="mmenu"] button, [data-m-mark="mmenu"] [role="button"], [data-m-mark="mmenu"] li, [data-m-mark="mmenu"] div, [data-m-mark="mmenu"] span').filter({ hasText: /^\s*(Bottle|Travel Mug|Mission)\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Mobile nav item', desc: 'A large row inside the opened menu.', sel: 'mobile menu row' }, { noScroll: true });
  await S('m-menu-pill', q('[data-m-mark="mmenu"] a, [data-m-mark="mmenu"] button').filter({ hasText: /^\s*(Impact report|Find a Store)\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Mobile menu pill', desc: 'An outline pill inside the menu (Impact report / Find a Store).', sel: 'menu outline pill' }, { noScroll: true });
  await page.keyboard.press('Escape'); await page.waitForTimeout(500);
  // The PLP filter sheet on mobile is a full-screen overlay (closed by
  // default): open it once with its own toggle. The page key is the same one
  // the saved components carry, so a blocked load is recorded against them
  // and a temporary block can never erase earlier readings.
  if (!(await newPage('mobile-category', { mobile: true, wait: 8000 }))) return;
  const fb = q('button, a, [role="button"]').filter({ hasText: /^\s*Filters\s*$/i }).filter({ visible: true }).first();
  if (await fb.count()) {
    await fb.click({ timeout: 5000 }).catch(() => fb.evaluate((el) => el.click()));
    await page.waitForTimeout(1200);
  }
  await markFilterPanel();
  await S('m-filter-sheet', q('[data-m-mark="fpanel"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Filter sheet (mobile)', desc: 'The opened filter overlay at 390: Collection/Size radios, Colour swatches, × close.', sel: 'mobile filter sheet' }, { noScroll: true });
  await markRow(/Original|Insulated|350\s*ml/, 'mfrow');
  await S('m-filter-radio', q('[data-m-mark="mfrow"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile filter row', desc: 'A radio row in the mobile filter sheet.', sel: 'mobile filter radio' }, { noScroll: true });
  save();
}

run = new Date().toISOString().slice(0, 10);
out._meta.read = run;
out._meta.viewport = '1440 x 900 (mobile group 390 x 844); the public surface is light-only on both hosts — no dark theme mechanism was found';
out._meta.tool = 'tools/capture/public/measure.mjs';
const { browser, context: ctx0 } = await launch();
context = ctx0;
const pages = process.argv.slice(2);
const plan = { home, shop, category, pdp, cart, login, mobile };
const order = Object.keys(plan).filter((k) => !pages.length || pages.includes(k));
try {
  for (const k of order) { if (k !== 'mobile') await plan[k](); }
  if (!pages.length || pages.includes('mobile')) await plan.mobile();
  // Reduced-motion check on an element that actually transitions (a header
  // flyout trigger), so the delta is meaningful.
  if (!pages.length || pages.includes('home')) await reducedMotion('home', 'dopper-navigation button', BASE + '/');
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
