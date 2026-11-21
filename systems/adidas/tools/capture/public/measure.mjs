// Measures adidas.com.cn's public components in every state reachable
// without signing in or submitting anything.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node measure.mjs [page ...]
//
// Pages: home plp pdp cart mobile.
// Writes raw/components-computed.json (merged, so a subset of pages can be
// re-run) and one crop per component and state into components/crops/.
// raw/measurements.md is then built from the JSON by build-measurements.mjs.
//
// adidas.com.cn is the China flagship storefront: a client-rendered app on a
// `lib-*` component library with Tailwind utilities and iconfont glyphs, in
// zh-CN. Nothing is sent, bought or signed into: the only presses are local
// UI toggles (the Search disclosure, the nav flyout, the burger menu, PDP
// accordions). Submit controls are measured through CDP-forced
// pseudo-classes only. There is no consent SDK on these routes.
import fs from 'node:fs';
import path from 'node:path';
import { BASE, patch, open, killGeo, domFind, styleOf, crop, centre, RAW, UA, UA_MOBILE, chromium } from './lib.mjs';

const OUT = process.env.OUT_JSON || path.join(RAW, 'components-computed.json');
const out = fs.existsSync(OUT) ? JSON.parse(fs.readFileSync(OUT, 'utf8')) : {};
out._meta ??= {};
out.components ??= {};
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const save = () => fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');
const URLS = {
  // The PDP is pinned to one SKU so the screenshot pass (public.mjs) and this
  // pass always describe the same product.
  home: '/', plp: '/plp/sp_run_app_male', pdp: '/pdp?articleId=JP1477', cart: '/cart',
};
let page, cdp, current, context, run;
let activeCtx = null;
const touched = new Set();
const sheetsDone = new Set();

// A bot interstitial or an error page renders a minimal body: detect it so a
// blocked load is skipped, not measured.
async function blocked() {
  return page.evaluate(() => {
    const t = (document.body && document.body.innerText) || '';
    return /something went wrong|performing security verification|verifying you are human|just a moment|page cannot be found/i.test(t) || t.trim().length < 40;
  }).catch(() => true);
}

// ---------- helpers ----------

async function newPage(key, { mobile = false, promo = 'close', wait = 6000 } = {}) {
  current = key;
  const b = context.browser();
  if (activeCtx) { await activeCtx.close().catch(() => {}); activeCtx = null; }
  const ctx = await b.newContext(mobile
    ? { viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, userAgent: UA_MOBILE, isMobile: true, hasTouch: true, locale: 'zh-CN' }
    : { viewport: { width: 1440, height: 900 }, deviceScaleFactor: 2, userAgent: UA, locale: 'zh-CN' });
  activeCtx = ctx;
  await patch(ctx);
  page = await ctx.newPage();
  cdp = await ctx.newCDPSession(page);
  page.setDefaultTimeout(8000);
  await cdp.send('DOM.enable');
  await cdp.send('CSS.enable');
  log('open', key, mobile ? '(mobile)' : '');
  for (let attempt = 0; attempt < 3; attempt++) {
    await open(page, URLS[key].startsWith('http') ? URLS[key] : BASE + URLS[key], { wait, promo });
    if (!(await blocked())) break;
    log('  blocked pass', attempt + 1, '- reloading');
  }
  if (await blocked()) { log('  BLOCKED', key); return false; }
  if (promo === 'close') await killGeo(page);
  await page.addStyleTag({ content: '*{caret-color:transparent!important}' }).catch(() => {});
  if (!sheetsDone.has(key + (mobile ? '@390' : ''))) { await sheetsFor(key + (mobile ? '@390' : '')); sheetsDone.add(key + (mobile ? '@390' : '')); }
  return true;
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

// Clicks a UI toggle (menu, search, filter). Refuses a submit button and any
// control whose text names an action this kit must never take.
const NEVER = /^(send|submit|sign up|sign in|log in|create|buy|checkout|pay|purchase|subscribe|share|add to bag|add to cart|register|continue|google|accept|reject|customize|sign me up)$/i;
async function toggle(loc) {
  const l = loc.filter({ visible: true }).first();
  const t = await l.evaluate((el) => ({ tag: el.tagName, type: el.getAttribute('type'), text: (el.innerText || el.getAttribute('aria-label') || '').trim() }));
  if (t.type === 'submit' || NEVER.test(t.text)) throw new Error(`toggle refused: ${t.tag} "${t.text}"`);
  await l.click({ timeout: 4000 }).catch(() => l.evaluate((el) => el.click()));
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
    let s;
    try {
      s = await styleOf(loc);
    } catch (e) {
      // A state change can briefly unmount/remount the node; retry once
      // against the re-queried element.
      await page.waitForTimeout(1500);
      s = await styleOf(target.filter({ visible: true }).first());
    }
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

// Records the listed states of one component. meta: title, group, desc, sel.
async function S(key, target, list, meta = {}, opts = {}) {
  const prev = out.components[key];
  const keep = prev && Object.keys(prev.states || {}).length ? { page: prev.page, run: prev.run, url: prev.url } : null;
  comp(key, { title: meta.title, group: meta.group, desc: meta.desc, selector: meta.sel });
  delete out.components[key].missing;
  if (opts.open) { await reset(); await opts.open(); }
  const loc = target.filter({ visible: true }).first();
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
        const f = (opts.fieldLoc || loc).filter({ visible: true }).first();
        await f.click({ timeout: 4000 }).catch(() => f.evaluate((el) => el.focus()));
        await page.waitForTimeout(400);
        via = 'clicked into the field';
      } else if (st === 'filled') {
        const f = (opts.fieldLoc || loc).filter({ visible: true }).first();
        await f.click({ timeout: 4000 }).catch(() => f.evaluate((el) => el.focus()));
        await page.keyboard.type(opts.fillText || FILL, { delay: 10 });
        await page.waitForTimeout(500);
        undo = async () => { await f.focus(); await page.keyboard.press('ControlOrMeta+a'); await page.keyboard.press('Backspace'); await page.waitForTimeout(300); };
        via = `typed "${opts.fillText || FILL}", then deleted; nothing sent`;
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
  save(); // the host runs a fleet of captures: persist each component so a crash loses at most one
}

const q = (sel) => page.locator(sel);
const B4 = ['default', 'hover', 'focus-visible', 'pressed'];
const FILL = 'name@example.com';

// Transitions and animations declared in every readable sheet, by selector.
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

// ---------- page runs ----------
const G = {
  shell: 'Shell and navigation', home: 'Home', plp: 'Catalogue page (PLP)',
  pdp: 'Product page (PDP)', overlay: 'Panels and overlays',
  footer: 'Footer', mobile: 'Mobile (390 wide)',
};

async function shell() {
  const g = G.shell;
  await S('header', q('.navigation-warpper, header').filter({ visible: true }).first(), ['default'], { group: g, title: 'Header', desc: 'The sticky top bar every page shares: a utility strip (在线客服, 请登录), the adidas wordmark, the category nav and the campaign tag strip.', sel: '.navigation-warpper' }, { noScroll: true });
  await S('nav-item', q('.catalog-item-first-page').filter({ visible: true }).first(), B4, { group: g, title: 'Nav item', desc: 'A top-level category item (男装, 男鞋, 女装, 女鞋, 儿童, 配件).', sel: '.catalog-item-first-page' }, { noScroll: true });
  await S('utility-link', q('.online, .loginin').filter({ visible: true }).first(), B4, { group: g, title: 'Utility link', desc: 'A utility-strip entry (在线客服 online service, 请登录 sign in).', sel: '.online' }, { noScroll: true });
  await S('promo-tag', await domFind(page, /折|雪境|毛衣|户外|三条纹/, { sel: '.header *, [class*="tag" i], [class*="item" i]', tag: 'pt', minH: 14 }), B4, { group: g, title: 'Promo tag', desc: 'A campaign tag in the strip under the nav (11.11 不止5折, 雪境漫游, 降温毛衣精选).', sel: 'promo tag' }, { noScroll: true });
  await S('logo', q('[class*="logo" i], a[href="/"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Wordmark', desc: 'The adidas wordmark linking home.', sel: 'logo' }, { noScroll: true });
}

async function footerRun() {
  const g = G.footer;
  await S('footer', q('footer, [class*="footer" i]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Footer', desc: 'The page foot: link columns and the published service line.' });
  await S('footer-link', q('footer a, [class*="footer" i] a').filter({ visible: true }).first(), B4, { group: g, title: 'Footer link', desc: 'A footer link entry.' });
}

async function home() {
  const g = G.home;
  // The campaign container explicitly: `.feed-com-carousel` is the full-bleed
  // band under the 124px header. A broad `swiper`/`banner` first-match catches
  // the 40px tag strip inside the header instead — record a miss over that.
  await S('hero', q('.feed-com-carousel, .banner-container, a.banner-box').filter({ visible: true }).first(), ['default'], { group: g, title: 'Hero', desc: 'The campaign band under the header: photography, a headline and a 立即选购 CTA.', sel: '.feed-com-carousel' });
  await S('hero-cta', q('.lib-button').filter({ hasText: /选购|查看更多|查看|了解/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Primary CTA', desc: 'A lib-button campaign CTA (立即选购 "Shop now").', sel: '.lib-button' });
}

async function plp() {
  const g = G.plp;
  await S('plp-title', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Page title', desc: 'The catalogue page heading.' }, { noScroll: true });
  await S('filter-row', await domFind(page, /性别|分类|排序|筛选|价格/, { sel: '.item, .label-1, .label-4, [class*="filter" i] *, button, [role="button"]', tag: 'fr', minH: 18 }), B4, { group: g, title: 'Filter row', desc: 'A refinement row in the left filter column (性别 gender, category, price).', sel: 'filter row' });
  await S('product-card', q('a[href*="/pdp"]').filter({ visible: true }).first(), ['default', 'hover'], { group: g, title: 'Product tile', desc: 'A product card linking /pdp?articleId=… : image, name, price.', sel: 'a[href*="/pdp"]' });
  await S('product-card-name', q('a[href*="/pdp"] .label-1, a[href*="/pdp"] [class*="name" i], a[href*="/pdp"] [class*="title" i]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Tile name', desc: 'The product name inside a tile.' });
  await S('product-card-price', q('a[href*="/pdp"] [class*="price" i]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Tile price', desc: 'The ¥ price inside a tile.' });
}

async function pdp() {
  const g = G.pdp;
  await S('pdp-title', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Product title', desc: 'The product name heading.' }, { noScroll: true });
  await S('pdp-price', await domFind(page, /¥|￥/, { sel: '[class*="price" i], .label-1, .heading-3, span', tag: 'pp', minH: 14 }), ['default'], { group: g, title: 'Product price', desc: 'The ¥ price beside the title.' }, { noScroll: true });
  await S('add-to-cart', q('.lib-button, button').filter({ hasText: /加入购物|立即购买|加入购物袋|马上抢/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Add-to-cart button', desc: 'The primary purchase bar (加入购物袋). Measured, never pressed.', sel: 'lib-button atc' });
  await S('size-cell', q('[class*="size" i] .item, [class*="size" i] button, [class*="spec" i] .item').filter({ visible: true }).first(), B4, { group: g, title: 'Size cell', desc: 'A size/spec cell on the PDP.' });
  await S('accordion', q('.lib-collapse-item, [class*="collapse" i] > *, [class*="accordion" i] > *').filter({ visible: true }).first(), B4, { group: g, title: 'Accordion row', desc: 'An expandable detail row on the PDP.' });
}

async function mobile() {
  if (!(await newPage('home', { mobile: true }))) return;
  const g = G.mobile;
  // At 390 the top bar is the `.search-bar` pill, not the desktop
  // `.navigation-warpper` nav.
  await S('m-header', q('.search-bar, .navigation-warpper, header').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile header', desc: 'The top bar at 390 wide: a search-field pill, no nav row.', sel: '.search-bar' }, { noScroll: true });
  // Only a real menu control counts — never a bare `.iconfont` glyph (the
  // first one is the search bar's `icon_performance` logo mark). At 390
  // adidas.com.cn mounts no burger; this should record a miss.
  await S('m-burger', q('button[aria-label*="menu" i], [role="button"][aria-label*="menu" i], [class*="hamburger" i], [class*="burger" i]').filter({ visible: true }).first(), B4, { group: g, title: 'Burger button', desc: 'The menu button on mobile. None is mounted at 390 — the top bar is the search field, so this records a miss rather than an icon glyph.', sel: 'menu control' }, { noScroll: true });
}

const ALL = {
  home: async () => { if (!(await newPage('home'))) return; await shell(); await home(); await footerRun(); },
  plp: async () => { if (!(await newPage('plp'))) return; await plp(); await footerRun(); },
  pdp: async () => { if (!(await newPage('pdp'))) return; await pdp(); await footerRun(); },
  cart: async () => { if (!(await newPage('cart'))) return; },
  mobile: mobile,
};
const pageArg = process.argv.slice(2).join(',').split(',').filter(Boolean);
out._meta.read = new Date().toISOString().slice(0, 10);
out._meta.measuredAt = new Date().toISOString();
out._meta.viewport = '1440 x 900 (mobile group 390 x 844), light theme';
out._meta.tool = 'tools/capture/public/measure.mjs';
const browser = await chromium.launch();
try {
  context = browser.contexts()[0] || await browser.newContext();
  for (const [k, fn] of Object.entries(ALL)) {
    if (pageArg.length && !pageArg.includes(k)) continue;
    run = k;
    try { await fn(); } catch (e) { log('PAGE FAILED', k, e.message.split('\n')[0]); }
    if (page) await page.close().catch(() => {});
    page = null;
  }
} finally {
  if (page) await page.close().catch(() => {});
  if (activeCtx) await activeCtx.close().catch(() => {});
  save();
  log('components:', Object.keys(out.components).length);
  await browser.close().catch(() => {});
}
