// Measures dji.com's public components in every state reachable without an
// account and writes raw/components-computed.json + component crops.
// dji.com is one product signed out: the geo-locale /sg brand site — mega
// nav, home hero, category pages (/camera-drones, /handheld), a product page
// (/mavic-4-pro), /support, /company and /where-to-buy/online-stores —
// sections opt into the product's own .light-theme/.dark-theme classes —
// the dark hero sections are themed, not baked art; no root-level dark
// theme ships.
import fs from 'node:fs';
import path from 'node:path';
import { BASE, M, launch, patch, open, closePromo, domFind, styleOf, crop, centre, RAW, UA, UA_MOBILE } from './lib.mjs';

const OUT = process.env.OUT_JSON || path.join(RAW, 'components-computed.json');
const out = fs.existsSync(OUT) ? JSON.parse(fs.readFileSync(OUT, 'utf8')) : {};
out._meta ??= {};
out.components ??= {};
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const save = () => fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');
const PRODUCT = '/mavic-4-pro';
const URLS = { home: '', drones: '/camera-drones', handheld: '/handheld', product: PRODUCT, support: '/support', company: '/company', stores: '/where-to-buy/online-stores', mobile: '' };
let page, cdp, current, context, run, liveCtx;
const touched = new Set();
const listed = new Map();
// Routes PerimeterX gates this run: components last measured on them keep their
// earlier readings instead of being pruned below (a blocked pass must never
// erase evidence).
const failedPages = new Set();

async function blocked() {
  return page.evaluate(() => {
    const t = (document.body && document.body.innerText) || '';
    return /performing security verification|verifying you are human|just a moment|access denied|unusual activity from your computer network|not a robot|you have been blocked|unable to access/i.test(t) || t.trim().length < 40;
  }).catch(() => true);
}

async function newPage(key, { mobile = false, wait = 8000, promo = 'close', url = null, theme = null } = {}) {
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
  const cleared = await open(page, url || (URLS[key].startsWith('http') ? URLS[key] : BASE + URLS[key]), { wait, promo });  // false: the bot check did not clear (lib.mjs)
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
  Object.assign(c, { page: current, run, url: URLS[current] && (URLS[current].startsWith('http') ? URLS[current] : BASE + URLS[current]) }, meta);
  touched.add(key);
  c.states ??= {};
  return c;
}

// A failed re-read must not erase an earlier successful one: keep the saved
// style and record the failed attempt beside it. comp() has already stamped
// this run's date on the component, so the kept state is pinned to the run
// that actually read it (its own run stamp, else the component's earlier run)
// and an old reading is never republished as a new one.
function keepEarlier(c, state, e, earlierRun) {
  const err = String(e.message || e).slice(0, 200);
  const prev = c.states[state];
  if (prev && prev.style) {
    // A state that already carried a rerunError before read was recorded is
    // from an unknown earlier run: its date stays unknown (null), never the
    // component's date, which a failed re-read had already advanced.
    if (prev.read === undefined) prev.read = prev.rerunError ? null : (prev.run || earlierRun);
    prev.rerunError = err;
    prev.rerunOn = run;
  } else c.states[state] = { error: err };
}

async function measure(key, state, target, opts = {}) {
  const loc = target.and(page.locator(':visible')).first();
  const c = out.components[key];
  try {
    const s = await styleOf(loc);
    let file;
    if (opts.crop !== false) {
      try {
        file = await crop(page, (opts.cropLoc || loc).and(page.locator(':visible')).first(), `${key}-${state}`, opts.pad ?? 8);
      } catch (e) { s.cropError = String(e.message || e).slice(0, 120); }
    }
    c.states[state] = { ...s, crop: file, via: opts.via };
    if (opts.extra) c.states[state].extra = await opts.extra(loc);
    log('  ', key, state, s.rect.w + 'x' + s.rect.h);
  } catch (e) {
    keepEarlier(c, state, e, opts.earlierRun);
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
  const loc = target.and(page.locator(':visible')).first();
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
        await (opts.hoverLoc || loc).and(page.locator(':visible')).first().hover({ timeout: 5000 }).catch(() => (opts.hoverLoc || loc).and(page.locator(':visible')).first().hover({ timeout: 5000, force: true }));
        await page.waitForTimeout(450);
        via = 'mouse hover';
      } else if (st === 'focus-visible') {
        via = await kbFocus((opts.focusLoc || loc).and(page.locator(':visible')).first());
      } else if (st === 'pressed') {
        undo = await forcePseudo((opts.pressLoc || loc).and(page.locator(':visible')).first(), ['active', 'hover']);
        via = 'CDP forcePseudoState :active:hover';
      } else if (st === 'focused') {
        const fld = (opts.fieldLoc || loc).and(page.locator(':visible')).first();
        await fld.click({ timeout: 4000 }).catch(() => fld.evaluate((el) => el.focus()));
        await page.waitForTimeout(400);
        via = 'clicked into the field';
      } else if (st === 'filled') {
        const f = (opts.fieldLoc || loc).and(page.locator(':visible')).first();
        await f.click({ timeout: 4000 }).catch(() => f.evaluate((el) => el.focus()));
        await page.keyboard.type(opts.fillText || 'name@example.com', { delay: 10 });
        await page.waitForTimeout(500);
        undo = async () => { await f.focus(); await page.keyboard.press('ControlOrMeta+a'); await page.keyboard.press('Backspace'); await page.waitForTimeout(300); };
        via = `typed "${opts.fillText || 'name@example.com'}", then deleted; nothing sent`;
      } else if (st === 'opened') {
        if (opts.noToggle) via = 'held open by an earlier toggle';
        else {
          await toggle(loc, { allowLink: opts.allowLink }); await page.waitForTimeout(900); via = 'own toggle';
          undo = () => closeOpened(key, loc, opts);
        }
      } else via = via || 'at rest';
      await measure(key, st, loc, { ...opts, via, earlierRun: keep?.run });
    } catch (e) {
      keepEarlier(out.components[key], st, e, keep?.run);
      log('  !', key, st, String(e.message).slice(0, 120));
    }
    if (undo) await undo().catch(() => {});
    if (opts.after?.[st]) await opts.after[st](loc).catch(() => {});
  }
  await reset();
}

// Closes what an `opened` state opened. An open dropdown or menu keeps focus
// and covers the page, so every later focus-visible reading would come back
// 'focus failed'. Escape first, then the trigger again; if the trigger still
// reports aria-expanded="true" the miss is recorded on the opened state so
// the later readings on this page can be checked.
async function closeOpened(key, loc, opts) {
  const expanded = () => loc.evaluate((el) => el.getAttribute('aria-expanded')).catch(() => null);
  await page.keyboard.press('Escape').catch(() => {});
  await page.waitForTimeout(400);
  if ((await expanded()) === 'true') { await toggle(loc, { allowLink: opts.allowLink }).catch(() => {}); await page.waitForTimeout(600); }
  if ((await expanded()) === 'true') {
    const st = out.components[key].states.opened;
    if (st) st.closeFailed = 'aria-expanded still "true" after Escape and a second toggle';
    log('  ! opened state did not close', key);
  }
}

// Clicks a UI toggle (dropdown, menu, sheet trigger). Refuses a submit button
// and any control whose text names an action this kit must never take.
const NEVER = /^(send|submit|sign in|log ?in|login|create|add|download|buy|purchase|pay|checkout|join|subscribe|save|apply|accept|reject|start|get started|claim|share|export|select|continue|claim this offer|try again)$/i;
async function toggle(loc, { allowLink = false } = {}) {
  const l = loc.and(page.locator(':visible')).first();
  const t = await l.evaluate((el) => ({ tag: el.tagName, type: el.getAttribute('type'), text: (el.innerText || el.getAttribute('aria-label') || '').trim() }));
  if (t.type === 'submit' || NEVER.test(t.text) || (t.tag === 'A' && !allowLink)) throw new Error(`toggle refused: ${t.tag} "${t.text}"`);
  await l.click({ timeout: 4000 }).catch(() => l.evaluate((el) => el.click()));
}

const q = (sel) => page.locator(sel);
const B4 = ['default', 'hover', 'focus-visible', 'pressed'];
// Elements inside scroll-driven reveals flicker in and out of :visible while
// the reveal animates; giving the page a beat after centre() lets the locator
// resolve the painted element instead of the pre-reveal one.
const settle = () => page.waitForTimeout(1500);
const SETTLE = { hover: settle, 'focus-visible': settle, pressed: settle, opened: settle, filled: settle, focused: settle };

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
  chrome: 'Site chrome', hero: 'Home hero', cards: 'Product cards',
  listing: 'Category page', detail: 'Product page', support: 'Support / company',
  mobile: 'Mobile (390 wide)',
};

const FIELD = ['default', 'focused', 'filled'];
const HEADER = '.official-site-header, [class*="siteHeaderShell"], [class*="siteHeader-module__siteHeader"], nav.dui-navbar, nav.dui-navbar-m, [class*="site-header-m"], header';
const VCARDS = '[class*="hero-vertical-card"], [class*="product-card" i]';
const ATOM = 'button[class*="dji-btn"], a[class*="dji-btn"]';

async function home() {
  if (!(await newPage('home'))) return;
  await sheetsFor('home');
  await chrome('home');
  const g = G.chrome;
  await S('nv-bar', q(HEADER).and(page.locator(':visible')).first(), ['default'], { group: g, title: 'Site header', desc: 'The top nav — DJI mark, product menus, ecosystem links, Login/Register, Store (the home page paints the legacy dui-navbar; category and product pages paint the newer siteHeader module).', sel: 'siteHeader/dui-navbar' }, { noScroll: true });
  await S('nv-mark', q('a[href*="dji.com/sg"], header a').and(page.locator(':visible')).first(), B4, { group: g, title: 'DJI mark', desc: 'The DJI logo link in the header; measured, never followed.', sel: 'logo link' }, { noScroll: true });
  await S('nv-item', q('a[href*="/sg/camera-drones"], a[href*="/sg/handheld"]').and(page.locator(':visible')).first(), B4, { group: g, title: 'Nav menu item', desc: 'A product menu link (Camera Drones) that opens the mega-menu; hover measured, menu opened via toggle below.', sel: 'nav product link' }, { noScroll: true });
  await S('nv-store', q('a[class*="store-btn"], a[href*="store.dji.com"]').and(page.locator(':visible')).first(), B4, { group: g, title: 'Store button', desc: 'The "Store" nav button linking to store.dji.com; measured, never followed — the store gates on a DJI account.', sel: 'store-btn' }, { noScroll: true });
  await S('nv-login', q('a[href*="member/login"], a[href*="redirect/member"]').and(page.locator(':visible')).first(), B4, { group: g, title: 'Login link', desc: 'The Login link in the header; measured, never followed — it redirects to the DJI account.', sel: 'login link' }, { noScroll: true });
  const gh = G.hero;
  await S('hm-slide', await domFind(page, /mavic|dji|neo|mini|osmo|ronin/i, { sel: 'section, div[class*="slide"], div[class*="swiper"], div[class*="hero"], div[class*="banner"]', tag: 'hms', minW: 800, minH: 300, leaf: true }), ['default'], { group: gh, title: 'Hero panel', desc: 'A home hero panel — product art over a dark or light backdrop with the CTA row.', sel: 'hero panel' }, { noScroll: true });
  await S('hm-learn', q('a').filter({ hasText: /^learn more$/i }).and(page.locator(':visible')).first(), B4, { group: gh, title: 'Learn More CTA', desc: 'The hero "Learn More" link to the product page; measured, never followed.', sel: 'Learn More' }, { noScroll: true });
  await S('hm-buy', q('a, button').filter({ hasText: /^buy now$/i }).and(page.locator(':visible')).first(), B4, { group: gh, title: 'Buy Now CTA', desc: 'The hero "Buy Now" CTA linking to the store; measured, never followed — checkout gates on a DJI account.', sel: 'Buy Now' }, { noScroll: true });
  await S('ft-bar', q('footer').and(page.locator(':visible')).last(), ['default'], { group: g, title: 'Site footer', desc: 'The DJI sitemap footer — product/support/company columns and locale links.', sel: 'footer' }, { before: SETTLE });
  await S('ft-link', q('a.ga-data, footer a').and(page.locator(':visible')).last(), B4, { group: g, title: 'Footer link', desc: 'A footer column link; hover measured, never followed.', sel: 'footer a' }, { before: SETTLE });
  save();
}

async function drones() {
  if (!(await newPage('drones'))) return;
  await sheetsFor('drones');
  await chrome('drones');
  const g = G.listing;
  await S('ct-h1', q('h1').and(page.locator(':visible')).first(), ['default'], { group: g, title: 'Category heading', desc: 'The "Camera Drones" listing heading.', sel: 'category h1' }, { noScroll: true });
  await S('ct-card', q(VCARDS).filter({ hasText: /dji (mavic|mini|avata|neo|flip|air)/i }).and(page.locator(':visible')).first(), ['default', 'hover'], { group: G.cards, title: 'Product card', desc: 'A 2-up atom-design hero-vertical-card on the category grid — product art, tagline and name (the page\'s H1 banner and full-width series intro share the class, so the filter anchors on a DJI product name); hover measured, never followed.', sel: 'hero-vertical-card' });
  await S('ct-subnav', q('a[class*="sub-nav-btn"], a[class*="store-btn"]').and(page.locator(':visible')).first(), B4, { group: g, title: 'Sub-nav Store button', desc: 'The "Store"/"Buy Now" button pinned in the page sub-nav; measured, never followed.', sel: 'sub-nav/store-btn' }, { noScroll: true });
  save();
}

async function handheld() {
  if (!(await newPage('handheld'))) return;
  await sheetsFor('handheld');
  await chrome('handheld');
  const g = G.listing;
  await S('hh-h1', q('h1, h2').and(page.locator(':visible')).first(), ['default'], { group: g, title: 'Handheld heading', desc: 'The handheld category heading (Osmo action cameras, gimbals, mics).', sel: 'handheld h1' }, { noScroll: true });
  await S('hh-card', q(VCARDS).filter({ hasText: /osmo (mobile|action)|square up|all angles|own the moment|capture every detail/i }).and(page.locator(':visible')).first(), ['default', 'hover'], { group: G.cards, title: 'Handheld card', desc: 'A 2-up handheld product card (atom hero-vertical-card; the full-width Osmo Pocket hero shares the class, so the filter anchors on a grid product name); hover measured, never followed.', sel: 'hero-vertical-card' });
  save();
}

async function product() {
  if (!(await newPage('product', { wait: 14000 }))) return;
  await sheetsFor('product');
  await chrome('product');
  const g = G.detail;
  await S('pd-subnav', q('nav[class*="sub-nav"], [class*="subnav"], div[class*="sub-nav"]').and(page.locator(':visible')).first(), ['default'], { group: g, title: 'Product sub-nav', desc: 'The product page sticky sub-nav — section links and the Buy Now button.', sel: 'sub-nav bar' }, { noScroll: true });
  await S('pd-buy', q(ATOM).filter({ hasText: /buy now/i }).and(page.locator(':visible')).first(), B4, { group: g, title: 'Atom Buy button', desc: 'The atom-design-v1 primary "Buy Now" button (dji-btn-lg); states measured, never pressed — purchase gates on the store account.', sel: 'atom dji-btn' }, { noScroll: true });
  await S('pd-watch', q(ATOM).filter({ hasText: /watch video/i }).and(page.locator(':visible')).first(), B4, { group: g, title: 'Atom ghost button', desc: 'The secondary "Watch Video" atom button; states measured, never pressed.', sel: 'atom dji-btn ghost' }, { noScroll: true });
  await S('pd-eyebrow', q('[class*="eyebrow"], .text-ms-24, h2[class*="eyebrow"]').and(page.locator(':visible')).first(), ['default'], { group: g, title: 'Eyebrow heading', desc: 'A section eyebrow line (e.g. "Triple-Camera Imaging System") using the text-ms-24 size utility.', sel: 'eyebrow text-ms-24' });
  await S('pd-h', await domFind(page, /mavic|imaging|spin your world|flagship|hasselblad|tele/i, { sel: 'h1, h2, h3', tag: 'pdh', minW: 100, minH: 14 }), ['default'], { group: g, title: 'Product heading', desc: 'A product page display heading.', sel: 'product h1/h2' }, { noScroll: true });
  await S('pd-spec', await domFind(page, /\d+\s*(mp|gb|minutes|km|fps|g\b)/i, { sel: 'li, td, div, p, span', tag: 'pds', minW: 30, minH: 10 }), ['default'], { group: g, title: 'Spec line', desc: 'A spec value line on the product page.', sel: 'spec text' });
  save();
}

async function support() {
  if (!(await newPage('support'))) return;
  await sheetsFor('support');
  await chrome('support');
  const g = G.support;
  await S('sp-h1', q('h1, h2').and(page.locator(':visible')).first(), ['default'], { group: g, title: 'Support heading', desc: 'The support portal heading.', sel: 'support h1' }, { noScroll: true });
  await S('sp-card', q('[class*="card-container"][class*="size-s"]').and(page.locator(':visible')).first(), ['default', 'hover'], { group: g, title: 'Support tile', desc: 'A support category tile (repairs, service, downloads); hover measured, never followed.', sel: 'support tile a' });
  await S('sp-search', q('input[type="search"], input[placeholder*="earch"], [class*="search"] input, a[class*="search"]').and(page.locator(':visible')).first(), FIELD, { group: g, title: 'Support search', desc: 'The support search field; focus/fill measured, never submitted.', sel: 'support search' }, { noScroll: true });
  save();
}

async function company() {
  if (!(await newPage('company'))) return;
  await sheetsFor('company');
  await chrome('company');
  const g = G.support;
  await S('co-h1', await domFind(page, /^about dji$/i, { sel: 'a, span, div', tag: 'coh', minW: 40, minH: 14 }), ['default'], { group: g, title: 'About DJI nav heading', desc: 'The "About DJI" section heading in the company sidebar nav — the page paints its hero as image, so this named link is its display text.', sel: 'about nav item' }, { noScroll: true });
  // The first visible <p> was the unsupported-browser notice in a modal box
  // (2026-11 run), not the company lede.
  await S('co-lede', q('p:not(.modal-box p)').filter({ hasNotText: /no longer supported/i }).and(page.locator(':visible')).first(), ['default'], { group: g, title: 'Company lede', desc: 'The first body paragraph on the company page.', sel: 'company p' });
  save();
}

async function stores() {
  if (!(await newPage('stores'))) return;
  await sheetsFor('stores');
  await chrome('stores');
  const g = G.support;
  await S('st-h1', q('h1, h2').and(page.locator(':visible')).first(), ['default'], { group: g, title: 'Where to Buy heading', desc: 'The where-to-buy page heading.', sel: 'stores h1' }, { noScroll: true });
  await S('st-link', q('a.ga-data, a').filter({ hasText: /flagship|operated|retail/i }).and(page.locator(':visible')).first(), B4, { group: g, title: 'Store-type link', desc: 'A store-type link (Flagship Stores); measured, never followed.', sel: 'ga-data link' }, { noScroll: true });
  save();
}

async function mobile() {
  if (!(await newPage('mobile', { mobile: true, url: BASE }))) return;
  await chrome('mobile');
  const g = G.mobile;
  await S('m-bar', q(HEADER).and(page.locator(':visible')).first(), ['default'], { group: g, title: 'Mobile header', desc: 'The phone header at 390px — mark and menu affordance.', sel: 'mobile header' }, { noScroll: true });
  await S('m-menu', q('a.navbar-control').and(page.locator(':visible')).first(), B4, { group: g, title: 'Mobile menu button', desc: 'The hamburger control in the /sg/mobile navbar; measured, never toggled open.', sel: 'a.navbar-control' }, { noScroll: true });
  await S('m-tab', q('.dui-navbar-m a:not(.navbar-control):not(.navbar-search):not(.navbar-dji-icon), .site-header-m a, nav a').filter({ hasText: /camera drones|handheld|lifestyle|explore/i }).and(page.locator(':visible')).first(), B4, { group: g, title: 'Mobile nav tab', desc: 'A category tab in the mobile nav row (the phone UA is redirected to the separate /sg/mobile site); measured, never followed.', sel: 'mobile nav tab' }, { noScroll: true });
  await S('m-cta', q('a, button').filter({ hasText: /learn more|buy now|shop/i }).and(page.locator(':visible')).first(), B4, { group: g, title: 'Mobile CTA', desc: 'A hero CTA at 390px; measured, never followed.', sel: 'mobile CTA' });
  save();
}

run = new Date().toISOString().slice(0, 10);
out._meta.read = run;
out._meta.viewport = '1440 x 900 (mobile group 390 x 844); dji.com signs one product into its geo-locale brand site (/sg) — mega-nav, hero, category grids, product pages over the declared --grey-*/--font-* token layer (Open Sans/PingFang UI), light nav/listings and dark hero/product/footer sections over the shared declared layer';
out._meta.tool = 'tools/capture/public/measure.mjs';
const { browser, context: ctx0 } = await launch();
context = ctx0;
const pages = process.argv.slice(2);
const plan = { home, drones, handheld, product, support, company, stores, mobile };
const order = Object.keys(plan).filter((k) => !pages.length || pages.includes(k));
const finishedPages = new Set();
try {
  for (const k of order) { if (k !== 'mobile') { await plan[k](); finishedPages.add(k); } }
  if (!pages.length || pages.includes('mobile')) { await plan.mobile(); finishedPages.add('mobile'); }
  // Reduced-motion check on an element that transitions (a nav link's hover),
  // so the delta is meaningful.
  if (!pages.length || pages.includes('home')) await reducedMotion('home', 'nav a');
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
