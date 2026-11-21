// Measures cron.com's public components in every state reachable without
// signing in or submitting anything.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs PYTHON=<venv python3> node measure.mjs [page ...]
//
// Pages: home blog changelog post mobile.
// Writes raw/components-computed.json (merged) and one crop per component and
// state into components/crops/; raw/measurements.md is built by
// build-measurements.mjs.
//
// cron.com is a static landing page (no challenge layer seen this run): an
// inline <style> block and a 3.6KB style.css of literal declarations — the
// only custom properties are the Sign-up pill's --glow/--glow-hover shadows.
// The page paints one dark theme (#161412 over #0f0d0a). Specs select by
// class, role or text. Sign up / Login / Docs and every notion.so link are
// measured, never followed; the only press is the mobile menu toggle.
import fs from 'node:fs';
import path from 'node:path';
import { BASE, M, launch, patch, open, closePromo, domFind, styleOf, crop, centre, RAW, UA, UA_MOBILE } from './lib.mjs';

const OUT = process.env.OUT_JSON || path.join(RAW, 'components-computed.json');
const out = fs.existsSync(OUT) ? JSON.parse(fs.readFileSync(OUT, 'utf8')) : {};
out._meta ??= {};
out.components ??= {};
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const save = () => { fs.mkdirSync(RAW, { recursive: true }); fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n'); };
const URLS = { home: '/', blog: '/blog', changelog: '/changelog', post: '/blog/2024-01-17-cron-is-now-notion-calendar' };
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
    await open(page, url || (/^https?:/.test(URLS[key]) ? URLS[key] : BASE + URLS[key]), { wait, promo });
    ok = !(await blocked());
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

// Marks the opened mobile nav overlay: .nav-menu, shown while body carries
// the showing-menu class the menu button toggles.
async function markMobileMenu() {
  await page.evaluate(() => {
    const m = document.querySelector('.nav-menu');
    if (m && getComputedStyle(m).display !== 'none') m.setAttribute('data-m-mark', 'mmenu');
  });
}

// Marks a blog index entry: the smallest ancestor that holds a date, a title
// and a byline ("By ...").
async function markPostEntry() {
  await page.evaluate(() => {
    const cand = [...document.querySelectorAll('article')].filter((el) => {
      const t = (el.innerText || '').trim();
      const r = el.getBoundingClientRect();
      return /\b(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec) \d{1,2}, \d{4}\b/.test(t) && /By /.test(t) && r.height > 60 && r.width > 300;
    }).sort((a, b) => (a.innerText || '').length - (b.innerText || '').length);
    if (cand[0]) cand[0].setAttribute('data-m-mark', 'postentry');
  });
}

// Marks a changelog entry: the smallest ancestor holding a date and a feature
// title.
async function markChangelogEntry() {
  await page.evaluate(() => {
    const cand = [...document.querySelectorAll('article')].filter((el) => {
      const t = (el.innerText || '').trim();
      const r = el.getBoundingClientRect();
      return /\b(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec) \d{1,2}, \d{4}\b/.test(t) && r.height > 80 && r.width > 400;
    }).sort((a, b) => (a.innerText || '').length - (b.innerText || '').length);
    if (cand[0]) cand[0].setAttribute('data-m-mark', 'clentry');
  });
}

const G = {
  shell: 'Shell and navigation', home: 'Home', blog: 'Blog', changelog: 'Changelog',
  post: 'Post', footer: 'Footer', mobile: 'Mobile (390 wide)',
};

async function home() {
  if (!(await newPage('home'))) return;
  await sheetsFor('home');
  await chrome('home');
  const g = G.shell;
  await S('site-header', q('header').filter({ visible: true }).first(), ['default'], { group: g, title: 'Site header', desc: 'The 120px header: the Cron logotype and the nav (Blog / Changelog / Docs / Login / Sign up).', sel: 'header' }, { noScroll: true });
  await S('logotype', q('#logotype, header img, header svg').filter({ visible: true }).first(), ['default'], { group: g, title: 'Logotype', desc: 'The Cron logotype image (40px tall).', sel: '#logotype' }, { noScroll: true });
  await S('nav-link', q('.nav-menu a').filter({ hasText: /^\s*Blog\s*$/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Nav link', desc: 'A top-nav link (Blog); measured, never followed.', sel: '.nav-menu a' }, { noScroll: true });
  await S('login-link', q('.nav-menu a, header a').filter({ hasText: /^\s*Login\s*$/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Login link', desc: 'The Login link to calendar.notion.so; measured, never followed.', sel: 'Login link' }, { noScroll: true });
  await S('signup-btn', q('a.primary-link-button').filter({ visible: true }).first(), B4, { group: g, title: 'Sign up button', desc: 'The #ff4700 Sign up pill (9999px radius, the --glow shadow var); measured, never followed.', sel: 'a.primary-link-button' }, { noScroll: true });
  const h = G.home;
  await S('banner', q('a.banner, .banner').filter({ visible: true }).first(), B4, { group: h, title: 'Rebrand banner', desc: '"Cron is now Notion Calendar →" — the #161412 pill with the orange inset ring and glow shadow; measured, never followed.', sel: '.banner' });
  await S('hero-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: h, title: 'Hero heading', desc: '"It\'s about time." — 140px/-3px tracking Helvetica at 90% leading.', sel: 'h1' });
  await S('hero-sub', q('main p, .content p').filter({ hasText: /next-generation calendar/i }).filter({ visible: true }).first(), ['default'], { group: h, title: 'Hero subline', desc: '"Cron is the next-generation calendar for professionals and teams."', sel: 'hero p' });
  const ft = q('footer').filter({ visible: true }).first();
  await ft.scrollIntoViewIfNeeded().catch(() => {});
  const fg = G.footer;
  await S('footer', ft, ['default'], { group: fg, title: 'Footer', desc: 'The #0f0d0a footer: Privacy / Terms / Web app / Download links.', sel: 'footer' }, { noScroll: true });
  await S('footer-link', q('footer a').filter({ visible: true }).first(), B4, { group: fg, title: 'Footer link', desc: 'A footer link (Privacy Policy); measured, never followed.', sel: 'footer a' }, { noScroll: true });
}

async function blog() {
  if (!(await newPage('blog'))) return;
  await sheetsFor('blog');
  await chrome('blog');
  const g = G.blog;
  await S('blog-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Blog heading', desc: '"Cron Blog" — the index heading.', sel: 'h1' }, { noScroll: true });
  await lazyLoad();
  await markPostEntry();
  await S('post-entry', q('[data-m-mark="postentry"]').filter({ visible: true }).first(), B4, { group: g, title: 'Post entry', desc: 'A blog index article: date, h1 title, byline, hero image and excerpt; measured, never followed.', sel: 'article' });
}

async function changelog() {
  if (!(await newPage('changelog'))) return;
  await sheetsFor('changelog');
  await chrome('changelog');
  const g = G.changelog;
  await S('changelog-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Changelog heading', desc: '"Cron Changelog" — the index heading.', sel: 'h1' }, { noScroll: true });
  await lazyLoad();
  await markChangelogEntry();
  await S('changelog-entry', q('[data-m-mark="clentry"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Changelog entry', desc: 'A dated release entry (title + notes).', sel: 'changelog entry' });
  await S('demo-link', q('a').filter({ hasText: /^\s*View demo\s*$/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Demo link', desc: 'The "View demo" link inside a release entry; measured, never followed.', sel: 'View demo link' });
  await S('feature-h2', q('h2, h3').filter({ visible: true }).first(), ['default'], { group: g, title: 'Feature heading', desc: 'A feature title inside an entry ("New name").', sel: 'feature heading' });
}

async function post() {
  if (!(await newPage('post'))) return;
  await sheetsFor('post');
  await chrome('post');
  const g = G.post;
  await S('post-h1', q('h1, h2').filter({ visible: true }).first(), ['default'], { group: g, title: 'Post title', desc: '"Cron is now Notion Calendar" — the post heading.', sel: 'post h1' });
  await S('post-meta', q('article time, article .date, article').locator('text=/By /').filter({ visible: true }).first(), ['default'], { group: g, title: 'Post byline', desc: 'The date + "By Raphael Schaad" byline.', sel: 'post byline' });
  await S('post-body', q('article p, main p, .content p').filter({ visible: true }).first(), ['default'], { group: g, title: 'Body paragraph', desc: 'A body paragraph in the post (22px/170%).', sel: 'post p' });
  await S('post-media', q('article video, article img, main video, main img').filter({ visible: true }).first(), ['default'], { group: g, title: 'Post media', desc: 'The post\'s demo media (675x450).', sel: 'post media' });
  await S('post-back', q('a').filter({ hasText: /All blog posts/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Back link', desc: '"← All blog posts" — the article back link; measured, never followed.', sel: 'back link' });
}

async function mobile() {
  if (!(await newPage('home', { mobile: true }))) return;
  const g = G.mobile;
  await S('m-header', q('header').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile header', sel: 'header at 390' }, { noScroll: true });
  const menu = q('.nav-menu-button').filter({ visible: true }).first();
  await S('m-menu-button', menu, B4, { group: g, title: 'Menu button', desc: 'The 24x18 menu icon that toggles body.showing-menu.', sel: '.nav-menu-button' }, { noScroll: true });
  if (await menu.count()) {
    try {
      await menu.click({ timeout: 5000 }).catch(() => menu.evaluate((el) => el.click()));
      await page.waitForTimeout(1200);
      await markMobileMenu();
    } catch (e) { log('  ! menu open failed', String(e.message).slice(0, 80)); }
  }
  await S('m-menu-open', q('[data-m-mark="mmenu"], .nav-menu').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile menu, open', desc: 'The opened nav overlay (.nav-menu over #161412).', sel: 'opened mobile menu' }, { noScroll: true });
  await S('m-nav-item', q('.nav-menu li a').filter({ hasText: /^\s*(Blog|Changelog|Docs|Login)\s*$/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Mobile menu row', desc: 'A 24px row inside the opened nav overlay.', sel: 'mobile menu row' }, { noScroll: true });
  await S('m-signup-btn', q('.nav-menu .primary-link-button').filter({ visible: true }).first(), B4, { group: g, title: 'Mobile sign up', desc: 'The full-width Sign up pill inside the menu.', sel: '.nav-menu .primary-link-button' }, { noScroll: true });
  // close the menu
  await page.evaluate(() => document.body.classList.remove('showing-menu'));
  await page.waitForTimeout(600);
  await page.evaluate(() => { const c = [...document.querySelectorAll('h1,h2')].filter((e) => { const r = e.getBoundingClientRect(); return r.width > 100 && r.height > 10; }); if (c[0]) c[0].setAttribute('data-m-mark', 'mhead'); });
  await S('m-heading', q('[data-m-mark="mhead"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile heading', sel: 'painted heading at 390' });
}

run = new Date().toISOString().slice(0, 10);
out._meta.read = run;
out._meta.viewport = '1440 x 900 (mobile group 390 x 844); cron.com paints a single dark page';
out._meta.tool = 'tools/capture/public/measure.mjs';
const { browser, context: ctx0 } = await launch();
context = ctx0;
const pages = process.argv.slice(2);
const plan = { home, blog, changelog, post, mobile };
const order = Object.keys(plan).filter((k) => !pages.length || pages.includes(k));
try {
  for (const k of order) { if (k !== 'mobile') await plan[k](); }
  if (!pages.length || pages.includes('mobile')) await plan.mobile();
  // Reduced-motion check on an element that actually transitions (the Sign up
  // pill's glow), so the delta is meaningful.
  if (!pages.length || pages.includes('home')) await reducedMotion('home', 'a.primary-link-button');
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
