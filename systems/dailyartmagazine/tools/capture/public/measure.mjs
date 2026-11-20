// Measures dailyartmagazine.com's public components in every state reachable
// without signing in or submitting anything.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs PYTHON=<venv python3> node measure.mjs [page ...]
//
// Pages: home latest category article about contact search mobile.
// Writes raw/components-computed.json (merged) and one crop per component and
// state into components/crops/; raw/measurements.md is built by
// build-measurements.mjs.
//
// dailyartmagazine.com is a WordPress magazine; the page paints one light
// theme. Specs select by theme/plugin class names, role, aria-label or text.
// Article cards, menu items and the Shop/Courses outbound links are measured,
// never followed; the hamburger and the Latest/Trending tabs are local UI
// toggles; newsletter and wpcf7 forms are measured but never submitted.
import fs from 'node:fs';
import path from 'node:path';
import { BASE, M, launch, patch, open, closePromo, domFind, styleOf, crop, centre, RAW, UA, UA_MOBILE } from './lib.mjs';

const OUT = process.env.OUT_JSON || path.join(RAW, 'components-computed.json');
const out = fs.existsSync(OUT) ? JSON.parse(fs.readFileSync(OUT, 'utf8')) : {};
out._meta ??= {};
out.components ??= {};
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const save = () => { fs.mkdirSync(RAW, { recursive: true }); fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n'); };
const URLS = { home: '/', latest: '/latest/', category: '/category/art-movements/impressionism/', article: '/10-japanese-woodblock-prints-you-need-to-see/', about: '/about-dailyart-magazine/', contact: '/contact/', search: '/?s=van+gogh' };
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
    : { viewport: { width: 1440, height: 900 }, deviceScaleFactor: 2, userAgent: UA, locale: 'en-US' });
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
    ok = (await open(page, url || (/^https?:/.test(URLS[key]) ? URLS[key] : BASE + URLS[key]), { wait, promo })) && !(await blocked());  // open() is false when the bot check did not clear
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
  if (opts.open) { await reset(); try { await opts.open(); } catch (e) { log('  ! open failed', key, String(e.message).slice(0, 80)); } }
  const loc = target.filter({ visible: true }).first();
  await loc.waitFor({ state: 'visible', timeout: 6000 }).catch(() => {});
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
const NEVER = /^(send|submit|sign in|log ?in|login|create|add|download|buy|purchase|pay|checkout|join|subscribe|save|apply|accept|reject|start|get started|claim|share|export|select|continue|claim this offer|try again|order( free)?( sample)?|add to cart|buy now|buy font|go to the platform|get a demo|get demo|contact sales|send message)$/i;
async function toggle(loc, { allowLink = false } = {}) {
  const l = loc.filter({ visible: true }).first();
  const t = await l.evaluate((el) => ({ tag: el.tagName, type: el.getAttribute('type'), text: (el.innerText || el.getAttribute('aria-label') || '').trim() }));
  if (t.type === 'submit' || NEVER.test(t.text) || (t.tag === 'A' && !allowLink)) throw new Error(`toggle refused: ${t.tag} "${t.text}"`);
  await l.click({ timeout: 4000 }).catch(() => l.evaluate((el) => el.click()));
}

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
  shell: 'Shell and navigation', home: 'Home', latest: 'Latest',
  category: 'Category', article: 'Article', about: 'About',
  contact: 'Contact', search: 'Search', mobile: 'Mobile (390 wide)',
};

// Opens the fixed-nav category menu via the hamburger (a local UI toggle,
// never a link). Idempotent: if the nav is already painted on screen it is
// left open, so a sequence of specs can share one opening.
async function openCatMenu() {
  const onscreen = await page.evaluate(() => {
    const n = document.querySelector('nav.fixed-nav, nav.navigation');
    if (!n) return false;
    const r = n.getBoundingClientRect();
    const cs = getComputedStyle(n);
    return r.right > 0 && r.left < innerWidth && cs.visibility !== 'hidden' && cs.display !== 'none' && cs.opacity !== '0';
  });
  if (!onscreen) {
    const ham = page.locator('#hamburger').filter({ visible: true }).first();
    if (await ham.count()) {
      await ham.click({ timeout: 4000 }).catch(() => ham.evaluate((el) => el.click()));
      await page.waitForTimeout(1400);
    }
  }
  await page.evaluate(() => {
    const n = document.querySelector('nav.fixed-nav, nav.navigation');
    if (n) n.setAttribute('data-m-mark', 'catnav');
  });
}

async function closeCatMenu() {
  const ham = page.locator('#hamburger').filter({ visible: true }).first();
  if (await ham.count()) await ham.click({ timeout: 3000 }).catch(() => {});
  await page.waitForTimeout(600);
}

// Opens the category menu and hovers its first top-level item so the painted
// .sub-menu can be measured while it is actually on screen.
async function openCatSub() {
  await openCatMenu();
  const li = page.locator('nav.fixed-nav #primary-menu > li, nav.navigation #primary-menu > li').filter({ visible: true }).first();
  if (await li.count()) {
    await li.hover({ timeout: 4000 }).catch(() => li.hover({ timeout: 4000, force: true }));
    await page.waitForTimeout(800);
  }
}

// Marks the first painted ad slot (the a.pub.network placeholders
// div[id^="dailyartmagazine_*"] or an .ad wrapper) so it can be measured as a
// component; the slot is read only, never clicked.
async function markAd() {
  await page.evaluate(() => {
    const el = [...document.querySelectorAll('[id^="dailyartmagazine_"], .ad, .ad-content')].find((x) => {
      const r = x.getBoundingClientRect();
      return r.width > 100 && r.height > 40;
    });
    if (el) el.setAttribute('data-m-mark', 'adslot');
  });
}

// Opens the newsletter modal with the site's own mechanism: the stylesheet's
// .modal-r--show class on .modal-r[data-modalCtn="newsletter"] (the class its
// JS toggles). closePromo hid the layer for clean page shots; this undoes
// those hides first, then applies the real open class.
async function showModal() {
  await page.evaluate(() => {
    const overlay = document.querySelector('.modal-r[data-modalCtn="newsletter"]') || document.querySelector('.modal-r') || document.querySelector('[data-modalCtn]');
    if (!overlay) return false;
    const unhide = (x) => { x.style.removeProperty('display'); x.style.removeProperty('visibility'); };
    unhide(overlay);
    overlay.classList.add('modal-r--show');
    const box = overlay.querySelector('section.newsletter-modal') || overlay;
    unhide(box);
    box.setAttribute('data-m-mark', 'nlmodal');
    return true;
  });
  await page.waitForTimeout(900);
}

const FIELD = ['default', 'focused', 'filled'];

async function home() {
  if (!(await newPage('home'))) return;
  await sheetsFor('home');
  await chrome('home');
  const g = G.shell;
  await S('nav-bar', q('#top-header').filter({ visible: true }).first(), ['default'], { group: g, title: 'Top header', desc: 'The full-width top bar over the dark hero: hamburger, Stories/Shop/Courses, wordmark, social icons and the Search button.', sel: '#top-header' }, { noScroll: true });
  await S('nav-cluster', q('nav.primary-navigation').filter({ visible: true }).first(), ['default'], { group: g, title: 'Nav cluster', desc: 'The left cluster inside the header: hamburger + the Stories/Shop/Courses menu.', sel: 'nav.primary-navigation' }, { noScroll: true });
  await S('nav-logo', q('a.logo').filter({ visible: true }).first(), ['default'], { group: g, title: 'Logo', desc: 'The DailyArt Magazine wordmark (inline SVG).', sel: 'a.logo' }, { noScroll: true });
  await S('nav-link', q('#primary-top-menu a').filter({ hasText: /^\s*Stories\s*$/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Nav link', desc: '"Stories" — a primary-nav item; measured, never followed.', sel: '#primary-top-menu a' }, { noScroll: true });
  await S('nav-outbound', q('#primary-top-menu a').filter({ hasText: /^\s*Shop\s*$/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Outbound nav link', desc: '"Shop" — outbound to shop.dailyartmagazine.com; measured, never followed.', sel: '#primary-top-menu a[target="_blank"]' }, { noScroll: true });
  await S('hamburger', q('#hamburger').filter({ visible: true }).first(), ['default', 'hover', 'pressed'], { group: g, title: 'Hamburger', desc: 'The six-bar hamburger that toggles the fixed-nav category menu.', sel: '#hamburger' }, { noScroll: true });
  await S('cat-nav', q('nav.fixed-nav, nav.navigation').filter({ visible: true }).first(), ['opened'], { group: g, title: 'Category nav', desc: 'The fixed-nav category menu (Art Movements tree) opened by the hamburger.', sel: 'nav.fixed-nav' }, { open: openCatMenu, noScroll: true, crop: false, noToggle: true });
  await S('cat-nav-item', q('nav.fixed-nav #primary-menu > li > a, nav.navigation #primary-menu > li > a').filter({ visible: true }).first(), B4, { group: g, title: 'Category nav item', desc: 'A top-level category link ("Art Movements") in the opened nav; measured, never followed.', sel: 'nav.fixed-nav #primary-menu > li > a' }, { open: openCatMenu, after: { pressed: closeCatMenu } });
  await S('cat-nav-sub', q('nav.fixed-nav .sub-menu a, nav.navigation .sub-menu a').filter({ visible: true }).first(), ['opened'], { group: g, title: 'Category sub-menu item', desc: 'A sub-menu link ("Prehistoric Art") painted while its parent is hovered in the opened nav; measured, never followed.', sel: 'nav.fixed-nav .sub-menu a' }, { open: openCatSub, noToggle: true, noReset: true, after: { opened: closeCatMenu } });
  await S('search-btn', q('.social-media form button.primary.btn, form button.primary.btn').filter({ hasText: /search/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Search button', desc: 'The "Search" button in the header (a submit that GETs /?s=); measured, never submitted.', sel: '.social-media form button.primary.btn' }, { noScroll: true });
  const h = G.home;
  await S('hero-block', q('section.intro').filter({ visible: true }).first(), ['default'], { group: h, title: 'Hero block', desc: 'The dark hero section over the white page ("Scandalous Rodin" featured story + side cards).', sel: 'section.intro' }, { noScroll: true });
  await S('hero-tag', q('.intro .category.center, .intro .category').filter({ visible: true }).first(), ['default'], { group: h, title: 'Hero tag', desc: 'The "Featured Story" pink pill above the hero title.', sel: '.intro .category' }, { noScroll: true });
  await S('hero-h1', q('.intro h1.title, .intro h1').filter({ visible: true }).first(), ['default'], { group: h, title: 'Hero heading', desc: '"Scandalous Rodin" — the serif hero title on the dark block.', sel: '.intro h1' }, { noScroll: true });
  await S('hero-card', q('.intro .single-post').filter({ visible: true }).first(), ['default', 'hover'], { group: h, title: 'Hero card', desc: 'A story card inside the dark hero.', sel: '.intro .single-post' });
  await S('section-heading', q('h3.big').filter({ visible: true }).first(), ['default'], { group: h, title: 'Section heading', desc: 'A big serif section heading ("Latest" / "Long reads" / "Featured").', sel: 'h3.big' });
  await S('feed-tab', q('.main-p-tab').filter({ visible: true }).first(), ['default', 'hover'], { group: h, title: 'Feed tab', desc: 'The Latest/Trending tab label in the main feed heading.', sel: '.main-p-tab' });
  await S('feed-tab-active', q('.main-p-tab-active').filter({ visible: true }).first(), ['default'], { group: h, title: 'Feed tab (active)', desc: 'The active feed tab ("Latest").', sel: '.main-p-tab-active' });
  await S('browse-link', q('a.link-browse').filter({ visible: true }).first(), B4, { group: h, title: 'Browse-more link', desc: '"Browse More" beside the feed heading; measured, never followed.', sel: 'a.link-browse' });
  await S('post-card-h', q('.single-post__horizontal').filter({ visible: true }).first(), ['default', 'hover'], { group: h, title: 'Post card (horizontal)', desc: 'A horizontal story card in the Latest feed.', sel: '.single-post__horizontal' });
  await S('post-card-img', q('.single-post__horizontal .post-image').filter({ visible: true }).first(), ['default'], { group: h, title: 'Card image', desc: 'The card\'s 264x177 thumbnail block.', sel: '.post-image' });
  await S('post-card-title', q('.single-post__horizontal .post-content h1, .single-post__horizontal .post-content h2, .single-post__horizontal .post-content h3, .single-post__horizontal .post-content a').filter({ visible: true }).first(), B4, { group: h, title: 'Card title link', desc: 'A story title link inside a feed card; measured, never followed.', sel: '.post-content a' });
  await S('post-card-excerpt', q('.single-post__horizontal .post-excerpt, .single-post .post-excerpt').filter({ visible: true }).first(), ['default'], { group: h, title: 'Card excerpt', desc: 'The story excerpt paragraph under a card title.', sel: '.post-excerpt' });
  await S('post-card-cat', q('.single-post a.category').filter({ visible: true }).first(), B4, { group: h, title: 'Category chip', desc: 'The pink category chip on a card image ("Quiz", "Asian Art"); measured, never followed.', sel: '.single-post a.category' });
  await S('post-card-author', q('.author-link').filter({ visible: true }).first(), B4, { group: h, title: 'Author link', desc: 'A byline author link; measured, never followed.', sel: '.author-link' });
  await S('post-card-date', q('.single-post .date').filter({ visible: true }).first(), ['default'], { group: h, title: 'Card date', desc: 'A card\'s publication date.', sel: '.single-post .date' });
  await S('post-card-v', q('.single-post__vertical, .small-post').filter({ visible: true }).first(), ['default', 'hover'], { group: h, title: 'Post card (vertical)', desc: 'A vertical/small story card.', sel: '.single-post__vertical' });
  await S('load-more', q('.load-more-arts, .more-arts, a.load-more-arts, button.load-more-arts').filter({ visible: true }).first(), B4, { group: h, title: 'Load-more button', desc: 'The feed\'s "load more" control; measured, never clicked.', sel: '.load-more-arts' });
  await S('donation', q('.donation, .donate-row').filter({ visible: true }).first(), ['default'], { group: h, title: 'Donation block', desc: 'The donation call-out block.', sel: '.donation' });
  await S('nl-form', q('#newsletter-footer, form.newsletter-form').filter({ visible: true }).first(), ['default'], { group: g, title: 'Newsletter form', desc: 'The newsletter signup form (email + consent checkbox + send).', sel: 'form.newsletter-form' });
  await S('nl-email', q('input.email-newsletter, form.newsletter-form input[type="text"], form.newsletter-form input[type="email"]').filter({ visible: true }).first(), FIELD, { group: g, title: 'Newsletter email field', desc: 'The newsletter email input; typed into for the filled state, then cleared — never submitted.', sel: 'input.email-newsletter' });
  await S('nl-checkbox', q('form.newsletter-form input[type="checkbox"]').filter({ visible: true }).first(), ['default', 'hover'], { group: g, title: 'Newsletter consent checkbox', desc: 'The required consent checkbox; measured, never toggled.', sel: '.newsletter-form input[type="checkbox"]' });
  await S('nl-send', q('button.newsletter-send, form.newsletter-form button[type="submit"]').filter({ visible: true }).first(), B4, { group: g, title: 'Newsletter send button', desc: 'The newsletter submit; measured, never submitted.', sel: '.newsletter-send' });
  await markAd();
  await S('ad-slot', q('[data-m-mark="adslot"]').first(), ['default'], { group: h, title: 'Ad slot', desc: 'A painted a.pub.network ad placeholder (billboard/leaderboard/right-rail); read, never clicked.', sel: '[id^="dailyartmagazine_"]' }, { crop: false });
  await S('footer', q('footer').filter({ visible: true }).last(), ['default'], { group: g, title: 'Footer', desc: 'The footer band: six link menus, social icons and the newsletter form.', sel: 'footer' });
  await S('footer-link', q('footer a').filter({ hasText: /about us/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Footer link', desc: '"About Us" — a footer menu link; measured, never followed.', sel: 'footer a' });
  await S('social-link', q('.social-media a').filter({ visible: true }).first(), B4, { group: g, title: 'Social icon link', desc: 'A social-media icon link; measured, never followed.', sel: '.social-media a' });
  await S('nl-modal', q('[data-m-mark="nlmodal"]').first(), ['default'], { group: g, title: 'Newsletter modal', desc: 'The newsletter dialog (720px white box on a 90%-black overlay); opened with the site\'s own .modal-r--show class — it never self-mounted during the public pass.', sel: 'section.newsletter-modal' }, { open: showModal, noScroll: true, before: { default: async () => 'opened via the .modal-r--show class the site toggles — the modal never self-mounted on the public surface' } });
}

async function latest() {
  if (!(await newPage('latest'))) return;
  await sheetsFor('latest');
  await chrome('latest');
  const g = G.latest;
  await S('latest-h1', q('h1, h2.big').filter({ visible: true }).first(), ['default'], { group: g, title: 'Index heading', desc: 'The stories index heading.', sel: 'latest h1' }, { noScroll: true });
  await S('latest-row', q('.single-post, .post-row').filter({ visible: true }).first(), ['default', 'hover'], { group: g, title: 'Story row', desc: 'A story row on the Latest index.', sel: '.single-post' });
  await S('latest-link', q('.single-post .post-content a, .post-row a').filter({ visible: true }).first(), B4, { group: g, title: 'Story link', desc: 'A story title link on the index; measured, never followed.', sel: '.post-content a' });
}

async function category() {
  if (!(await newPage('category'))) return;
  await sheetsFor('category');
  await chrome('category');
  const g = G.category;
  await S('cat-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Category heading', desc: '"Impressionism" — the category archive heading.', sel: 'category h1' }, { noScroll: true });
  await S('cat-card', q('.single-post').filter({ visible: true }).first(), ['default', 'hover'], { group: g, title: 'Archive card', desc: 'A story card in the category archive.', sel: '.single-post' });
  await S('cat-card-title', q('.single-post .post-content a, .single-post h2 a, .single-post h3 a').filter({ visible: true }).first(), B4, { group: g, title: 'Archive title link', desc: 'An archive card title link; measured, never followed.', sel: '.single-post a' });
}

async function article() {
  if (!(await newPage('article'))) return;
  await sheetsFor('article');
  await chrome('article');
  const g = G.article;
  await S('art-h1', q('h1.title, h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Article title', desc: '"10 Incredible Japanese Woodblock Prints You Need to See" — the article h1.', sel: 'h1.title' }, { noScroll: true });
  await S('art-meta', q('.info, .post-info, .meta').filter({ visible: true }).first(), ['default'], { group: g, title: 'Article meta', desc: 'The byline/date block under the title.', sel: '.info' }, { noScroll: true });
  await S('art-cat', q('.cat a, .category a').filter({ visible: true }).first(), B4, { group: g, title: 'Article category link', desc: 'A category chip on the article; measured, never followed.', sel: '.cat a' });
  await S('art-para', q('.project-module-text p, .project-module p, article p').filter({ visible: true }).first(), ['default'], { group: g, title: 'Article paragraph', desc: 'A body paragraph in the article flow.', sel: '.project-module p' });
  await S('art-inline-link', q('.project-module p a, article p a').filter({ visible: true }).first(), B4, { group: g, title: 'Inline link', desc: 'An in-copy link inside the article; measured, never followed.', sel: '.project-module p a' });
  await S('art-figure', q('.project-module-single_image, figure').filter({ visible: true }).first(), ['default'], { group: g, title: 'Article figure', desc: 'A figure block (image + caption) in the article flow; the lightgallery viewer is not opened.', sel: '.project-module-single_image' });
  await S('art-caption', q('figcaption').filter({ visible: true }).first(), ['default'], { group: g, title: 'Figure caption', desc: 'A figure caption under an article image.', sel: 'figcaption' });
  await S('share-btn', q('.share-links a').filter({ visible: true }).first(), B4, { group: g, title: 'Share button', desc: 'A share icon button in the article share-links row; measured, never followed.', sel: '.share-links a' });
  await S('art-tag', q('.tags-menu a, a[rel="tag"]').filter({ visible: true }).first(), B4, { group: g, title: 'Tag link', desc: 'An article tag link in the tags-menu; measured, never followed.', sel: '.tags-menu a' });
  await S('author-box', q('section.author-footer').filter({ visible: true }).first(), ['default'], { group: g, title: 'Author box', desc: 'The author bio box at the end of the article (avatar, name, bio).', sel: 'section.author-footer' });
  await S('related-card', q('.related .single-post, .small-post').filter({ visible: true }).first(), ['default', 'hover'], { group: g, title: 'Related card', desc: 'A related-stories card under the article.', sel: '.small-post' });
  await S('nl-form-article', q('#newsletter-footer, form.newsletter-form').filter({ visible: true }).first(), ['default'], { group: g, title: 'Article newsletter form', desc: 'The newsletter form under the article.', sel: '.newsletter-form' });
}

async function about() {
  if (!(await newPage('about'))) return;
  await sheetsFor('about');
  await chrome('about');
  const g = G.about;
  await S('about-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'About heading', desc: 'The About page heading.', sel: 'h1' }, { noScroll: true });
  await S('about-para', q('.page-content p').filter({ visible: true }).first(), ['default'], { group: g, title: 'About paragraph', desc: 'A body paragraph in the About page content.', sel: '.page-content p' });
}

async function contact() {
  if (!(await newPage('contact'))) return;
  await sheetsFor('contact');
  await chrome('contact');
  const g = G.contact;
  await S('contact-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Contact heading', desc: 'The Contact page heading.', sel: 'h1' }, { noScroll: true });
  await S('cf7-form', q('form.wpcf7-form').filter({ visible: true }).first(), ['default'], { group: g, title: 'Contact form', desc: 'The Contact Form 7 form (name, email, message, consent, Send).', sel: 'form.wpcf7-form' });
  await S('cf7-name', q('input.wpcf7-text').filter({ visible: true }).first(), FIELD, { group: g, title: 'Text field', desc: 'The "Your name" required text field; typed into for filled, then cleared — never submitted.', sel: 'input.wpcf7-text' });
  await S('cf7-email', q('input.wpcf7-email').filter({ visible: true }).first(), FIELD, { group: g, title: 'Email field', desc: 'The "Your email" required email field; typed into for filled, then cleared — never submitted.', sel: 'input.wpcf7-email' });
  await S('cf7-message', q('textarea.wpcf7-textarea').filter({ visible: true }).first(), FIELD, { group: g, title: 'Textarea', desc: 'The "Your message" textarea; typed into for filled, then cleared — never submitted.', sel: 'textarea.wpcf7-textarea' });
  await S('cf7-accept', q('.wpcf7-acceptance label, .wpcf7-acceptance .wpcf7-list-item-label').filter({ visible: true }).first(), ['default', 'hover'], { group: g, title: 'Acceptance checkbox', desc: 'The wpcf7 acceptance control: the native input is visibility:hidden, the box is painted by the label span ::before; measured, never toggled.', sel: '.wpcf7-acceptance label' });
  await S('cf7-send', q('input.wpcf7-submit').filter({ visible: true }).first(), B4, { group: g, title: 'Send button', desc: 'The wpcf7 "Send" submit; measured, never submitted.', sel: 'input.wpcf7-submit' });
}

async function search() {
  if (!(await newPage('search'))) return;
  await sheetsFor('search');
  await chrome('search');
  const g = G.search;
  await S('search-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Search heading', desc: 'The results heading for ?s=van+gogh.', sel: 'search h1' }, { noScroll: true });
  await S('search-card', q('.single-post').filter({ visible: true }).first(), ['default', 'hover'], { group: g, title: 'Result card', desc: 'A search-result story card.', sel: '.single-post' });
}

async function mobile() {
  if (!(await newPage('home', { mobile: true }))) return;
  const g = G.mobile;
  await S('m-nav-bar', q('nav.primary-navigation, nav').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile nav', sel: 'nav at 390' }, { noScroll: true });
  await S('m-logo', q('a.logo').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile logo', sel: 'a.logo at 390' }, { noScroll: true });
  await S('m-hamburger', q('#hamburger').filter({ visible: true }).first(), ['default', 'pressed'], { group: g, title: 'Mobile hamburger', desc: 'The hamburger at 390px.', sel: '#hamburger' }, { noScroll: true });
  await S('m-post-card', q('.single-post').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile post card', desc: 'A story card at 390px.', sel: '.single-post' });
  await S('m-nl-email', q('form.newsletter-form input[type="text"], input.email-newsletter').filter({ visible: true }).first(), FIELD, { group: g, title: 'Mobile newsletter field', desc: 'The newsletter input at 390px; typed into for filled, then cleared — never submitted.', sel: '.email-newsletter' });
}

run = new Date().toISOString().slice(0, 10);
out._meta.read = run;
out._meta.viewport = '1440 x 900 (mobile group 390 x 844); dailyartmagazine.com paints a single light theme';
out._meta.tool = 'tools/capture/public/measure.mjs';
const { browser, context: ctx0 } = await launch();
context = ctx0;
const pages = process.argv.slice(2);
const plan = { home, latest, category, article, about, contact, search, mobile };
const order = Object.keys(plan).filter((k) => !pages.length || pages.includes(k));
try {
  for (const k of order) { if (k !== 'mobile') await plan[k](); }
  if (!pages.length || pages.includes('mobile')) await plan.mobile();
  // Reduced-motion check on an element that transitions (a nav link's hover),
  // so the delta is meaningful.
  if (!pages.length || pages.includes('home')) await reducedMotion('home', '#primary-top-menu a');
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
