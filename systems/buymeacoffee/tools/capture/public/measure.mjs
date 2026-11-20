// Measures buymeacoffee.com's public components in every state reachable without
// signing in, subscribing or submitting anything.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node measure.mjs [page ...]
//
// Pages: home creator login reviews faq mobile.
// Writes raw/components-computed.json (merged) and one crop per component and
// state into components/crops/; raw/measurements.md is built by
// build-measurements.mjs.
//
// buymeacoffee.com paints two public frontends: the Nuxt marketing site
// (home/faq/reviews/blog/brand/about, Circular faces + Tailwind utilities on a
// #faf8f0 cream field) and the creator pages, login and signup (a Vite app on
// cdn.buymeacoffee.com that themes itself with inline --theme-color* custom
// properties). Nothing is sent, bought or signed into: the only presses are
// local UI toggles — the Apps nav dropdown, the Search-creators overlay, the
// coffee-count radios, the Make-this-monthly checkbox, the more-options menu
// and the mobile menu. The Support submit button is measured, never pressed;
// the login form is measured, never submitted. The CookieYes (cky-*) consent
// banner is hidden, never answered.
import fs from 'node:fs';
import path from 'node:path';
import { BASE, M, launch, patch, open, closePromo, domFind, styleOf, crop, centre, RAW, UA, UA_MOBILE } from './lib.mjs';

const OUT = process.env.OUT_JSON || path.join(RAW, 'components-computed.json');
const out = fs.existsSync(OUT) ? JSON.parse(fs.readFileSync(OUT, 'utf8')) : {};
out._meta ??= {};
out.components ??= {};
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const save = () => fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');
const URLS = { home: '/', creator: '/cara.app', login: '/login', reviews: '/reviews', faq: '/faq' };
let page, cdp, current, context, run, liveCtx;
const touched = new Set();
const listed = new Map();
// Routes a bot-edge gates this run: components last measured on them keep their
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

// The inline --theme-color* custom properties a creator page declares on its
// own wrapper elements (the per-creator accent and its derived tints); the
// stylesheet harvest never sees them, so they are read off the DOM here.
async function inlineVars(key) {
  const v = await page.evaluate(() => {
    const found = {};
    for (const el of document.querySelectorAll('[style*="--"]')) {
      for (const decl of (el.getAttribute('style') || '').split(';')) {
        const m = decl.match(/^\s*(--[\w-]+)\s*:\s*(.+)$/);
        if (m) {
          const probe = el;
          found[m[1]] = { declared: m[2].trim(), computed: getComputedStyle(probe).getPropertyValue(m[1]).trim(), on: el.tagName.toLowerCase() + (el.id ? '#' + el.id : '') + '.' + String(el.className).split(' ').slice(0, 2).join('.') };
        }
      }
    }
    return found;
  }).catch(() => ({}));
  if (Object.keys(v).length) { out._meta.inlineVars ??= {}; out._meta.inlineVars[key] = v; }
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
  // Found this run: the fresh readings replace any earlier miss, so the flag
  // must not outlive it (the token builders refuse a recaptureMissed entry).
  delete out.components[key].recaptureMissed;
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
const NEVER = /^(send|submit|sign in|log ?in|login|create|add|download|buy|purchase|pay|checkout|join|subscribe|save|apply|accept|reject|start|get started|claim|share|export|select|continue|claim this offer|try again|support|follow)$/i;
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
    await p.goto(url || BASE + URLS[key], { waitUntil: 'domcontentloaded', timeout: 90000 }).catch(() => {});
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
  shell: 'Shell and navigation', home: 'Home', creator: 'Creator page',
  login: 'Login', reviews: 'Reviews', faq: 'FAQ', footer: 'Footer',
  mobile: 'Mobile (390 wide)',
};

async function home() {
  if (!(await newPage('home'))) return;
  await sheetsFor('home');
  await chrome('home');
  await inlineVars('home');
  // Sweep the page once so scroll-reveal sections mount their content before
  // they are measured; several sections lazy-render only once on screen.
  await page.evaluate(async () => { const H = document.documentElement.scrollHeight; for (let y = 0; y <= H; y += 700) { scrollTo(0, y); await new Promise((r) => setTimeout(r, 120)); } scrollTo(0, 0); });
  await page.waitForTimeout(900);
  const g = G.shell;
  await S('header', q('#bmc-header').filter({ visible: true }).first(), ['default'], { group: g, title: 'Header', desc: 'The white marketing header: FAQ and Wall-of-love links, the Apps and Resources dropdowns, the wordmark, a fake Search-creators field, Log-in and the yellow Sign-up pill.', sel: '#bmc-header' }, { noScroll: true });
  await S('logo', q('#bmc-header a[href="/"]:has(svg)').filter({ visible: true }).first(), ['default'], { group: g, title: 'Logo', desc: 'The coffee-cup + "Buy me a coffee" wordmark anchor in the header centre.', sel: '#bmc-header a[href="/"]:has(svg)' }, { noScroll: true });
  await S('nav-link', q('#bmc-header a').filter({ hasText: /^\s*FAQ\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Nav link', desc: 'A plain header link (FAQ); hover paints a 5%-black pill (::before) that scales in.', sel: '#bmc-header a FAQ' }, { noScroll: true });
  await S('nav-trigger', q('#bmc-header div.btn-hover-bg.cursor-pointer').filter({ hasText: /^\s*Apps\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Nav trigger', desc: 'The Apps label + chevron that opens the header dropdown; toggled by click, never followed.', sel: '#bmc-header div.btn-hover-bg Apps' }, { noScroll: true });
  // The Apps dropdown opens on its trigger's click; keep the state (noReset)
  // so the panel is still painted when it is read and cropped.
  try {
    const t = q('#bmc-header div.btn-hover-bg.cursor-pointer').filter({ hasText: /^\s*Apps\s*$/ }).first();
    if (await t.count()) { await t.click({ timeout: 5000 }).catch(() => t.evaluate((el) => el.click())); await page.waitForTimeout(1200); }
  } catch (e) { log('  ! dropdown click failed', String(e.message).split('\n')[0]); }
  await S('nav-dropdown', q('#bmc-header .drop-up-or-down').filter({ visible: true }).first(), ['default'], { group: g, title: 'Nav dropdown', desc: 'The white drop-up-or-down panel the Apps trigger opens (iOS/Android links).', sel: '#bmc-header .drop-up-or-down' }, { noScroll: true, noReset: true });
  await S('menu-link', q('#bmc-header .drop-up-or-down a').filter({ hasText: /\S/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Menu link', desc: 'A link inside the opened header dropdown.', sel: 'dropdown link' }, { noScroll: true, noReset: true });
  await page.keyboard.press('Escape'); await page.mouse.click(700, 450).catch(() => {}); await page.waitForTimeout(600);
  await S('nav-search', q('#bmc-header div').filter({ hasText: /^\s*Search creators\s*$/ }).last(), B4, { group: g, title: 'Search field', desc: 'The "Search creators" pill in the header — a fake input that opens a Trending search overlay on click.', sel: '#bmc-header Search creators' }, { noScroll: true });
  await S('nav-login', q('#bmc-header a').filter({ hasText: /^\s*Log in\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Nav login', desc: 'The Log-in header link; measured never followed.', sel: '#bmc-header a Log in' }, { noScroll: true });
  await S('nav-cta', q('#bmc-header a.bmc-btn').filter({ hasText: /Sign up/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Nav CTA', desc: 'The yellow Sign-up pill (a.bmc-btn whose ::before paints #fd0, scaling on hover).', sel: '#bmc-header a.bmc-btn Sign up' }, { noScroll: true });
  const h = G.home;
  await S('page-field', q('div.bg-floral-white').filter({ visible: true }).first(), ['default'], { group: h, title: 'Page field', desc: 'The #faf8f0 cream wrapper the marketing pages paint on.', sel: 'div.bg-floral-white' }, { noScroll: true, crop: false });
  await S('rating', q('#bmc-header ~ * .ratings, .ratings').filter({ visible: true }).first(), ['default'], { group: h, title: 'Rating row', desc: 'The five stars + "Loved by 2,000,000+ creators" row over the hero.', sel: 'div.ratings' });
  await S('hero-title', q('h1').filter({ visible: true }).first(), ['default'], { group: h, title: 'Hero headline', desc: 'The 96px "Fund your creative work" display in Circular Bold.', sel: 'h1' });
  await S('hero-sub', q('p').filter({ hasText: /Accept support/i }).filter({ visible: true }).first(), ['default'], { group: h, title: 'Hero copy', desc: 'The 22px tagline under the headline.', sel: 'hero tagline' });
  await S('hero-cta', q('div.btn.header-anim').filter({ hasText: /Start my page/i }).filter({ visible: true }).first(), B4, { group: h, title: 'Hero CTA', desc: 'The hero Start-my-page yellow pill (div.btn.header-anim, 74px tall); measured never followed.', sel: 'div.btn.header-anim' });
  await S('creator-card', q('.creator-tile').filter({ visible: true }).first(), ['default'], { group: h, title: 'Creator card', desc: 'A floating creator card in the hero artwork (white tile, avatar, supporter count).', sel: 'div.creator-tile' });
  // hasText matches DOM text, not the text-transform rendering: the eyebrow's
  // textContent is "Support" (CSS uppercases it to SUPPORT), so match /support/i.
  await S('section-eyebrow', q('h2').filter({ hasText: /support/i }).filter({ visible: true }).first(), ['default'], { group: h, title: 'Eyebrow', desc: 'The 16px section eyebrow (SUPPORT / MEMBERSHIPS / SHOP, CSS-uppercased).', sel: 'h2 eyebrow' });
  await S('section-h2', q('h2').filter({ hasText: /Give your audience/i }).filter({ visible: true }).first(), ['default'], { group: h, title: 'Section heading', desc: 'A 64px section heading in Circular Bold.', sel: 'h2 section' });
  await S('section-lede', q('h3').filter({ hasText: /makes supporting fun/i }).filter({ visible: true }).first(), ['default'], { group: h, title: 'Section lede', desc: 'The 24px Circular Regular lede under a section heading.', sel: 'h3 lede' });
  save();
}

async function creator() {
  if (!(await newPage('creator', { url: BASE + '/cara.app', wait: 11000 }))) return;
  await sheetsFor('creator');
  await chrome('creator');
  await inlineVars('creator');
  const g = G.creator;
  await S('c-page-field', q('div.min-h-screen.bg-white').filter({ visible: true }).first(), ['default'], { group: g, title: 'Page field', desc: 'The white wrapper a creator page paints on (carries the inline --theme-color* vars).', sel: 'div.min-h-screen.bg-white' }, { noScroll: true, crop: false });
  await S('c-header', q('.tw-header-shadow').filter({ visible: true }).first(), ['default'], { group: g, title: 'Profile header', desc: 'The sticky creator-page bar: avatar, name, supporter count, the Home/Membership/Wishlist tabs, more-options and Login.', sel: 'div.tw-header-shadow' }, { noScroll: true });
  await S('c-tab', q('a.tw-tab-each').filter({ hasText: /^\s*Home\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Tab link', desc: 'A profile tab (Home/Membership/Wishlist); the active tab paints the theme-colour underline (::before).', sel: 'a.tw-tab-each' }, { noScroll: true });
  await S('c-login', q('.tw-header-shadow a').filter({ hasText: /^\s*Login\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Header login', desc: 'The Login link at the profile header\'s right edge; measured never followed.', sel: 'header Login' }, { noScroll: true });
  // more-options opens a context menu; keep it open for the menu entry below.
  try {
    const t = q('[role="button"][aria-label="more options"]').first();
    if (await t.count()) { await t.click({ timeout: 5000 }).catch(() => t.evaluate((el) => el.click())); await page.waitForTimeout(1000); }
  } catch (e) { log('  ! more-options click failed', String(e.message).split('\n')[0]); }
  await S('c-more', q('[role="button"][aria-label="more options"]').filter({ visible: true }).first(), B4, { group: g, title: 'More options', desc: 'The ellipsis trigger (aria-haspopup=menu) that opens the profile context menu.', sel: '[aria-label="more options"]' }, { noScroll: true });
  // The context menu opens on the ellipsis's own click and must stay open
  // (noReset) while the panel and its rows are read and cropped. Several
  // more-options buttons exist on the page; filter to the visible profile one.
  // The evaluate click is tried first: the sticky header re-renders on scroll,
  // which can leave the Playwright click retrying until it times out.
  try {
    const t = q('[role="button"][aria-label="more options"]').filter({ visible: true }).first();
    let opened = 0;
    if (await t.count()) {
      for (const how of ['eval', 'click', 'enter']) {
        try {
          if (how === 'eval') await t.evaluate((el) => el.click());
          else if (how === 'click') await t.click({ timeout: 4000 });
          else { await t.evaluate((el) => el.focus()); await page.keyboard.press('Enter'); }
          await page.waitForTimeout(900);
          opened = await q('ul[role=menu]').filter({ visible: true }).count();
        } catch { opened = 0; }
        if (opened) { log('  context menu opened via', how); break; }
      }
    }
    if (!opened) log('  ! context menu never opened');
  } catch (e) { log('  ! more-options click failed', String(e.message).split('\n')[0]); }
  await S('c-context', q('ul[role=menu], ul:has(li.follow-user)').filter({ visible: true }).first(), ['default'], { group: g, title: 'Context menu', desc: 'The small menu the more-options trigger opens: Follow, Share, Report.', sel: 'ul[role=menu]' }, { noScroll: true, noReset: true });
  await S('c-follow', q('ul[role=menu] li.follow-user').filter({ visible: true }).first(), B4, { group: g, title: 'Follow item', desc: 'The Follow row inside the more-options menu (follow-user); measured never toggled — following needs an account.', sel: 'li.follow-user' }, { noScroll: true, noReset: true });
  await S('c-share', q('ul[role=menu] li').filter({ hasText: /Share/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Share item', desc: 'The Share row inside the more-options menu (px-3 py-2, dark/5 hover fill).', sel: 'menu Share li' }, { noScroll: true, noReset: true });
  await page.keyboard.press('Escape'); await page.mouse.click(700, 500).catch(() => {}); await page.waitForTimeout(600);
  await S('c-about', q('[role="region"][aria-label="About Cara"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'About box', desc: 'The "About Cara" sidebar box (aria region): bio copy, links, icon row.', sel: '[role=region][aria-label="About Cara"]' });
  await S('c-widget', q('[role="region"][aria-label="Support Cara"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Support widget', desc: 'The "Buy Cara a coffee" card (aria region): quantity pills, custom amount, name field, message, monthly checkbox, the orange Support button.', sel: '[role=region][aria-label="Support Cara"]' });
  await S('c-qty-on', q('.tw-coffee-counter.bg-pageTheme, .tw-coffee-counter[class*="bg-pageTheme"]').filter({ visible: true }).first(), B4, { group: g, title: 'Quantity pill, selected', desc: 'The checked coffee-count pill: the theme-colour #FF813F fill with white count.', sel: '.tw-coffee-counter.bg-pageTheme' });
  await S('c-qty-off', q('.tw-coffee-counter.bg-white, .tw-coffee-counter[class*="bg-white"]').filter({ visible: true }).first(), B4, { group: g, title: 'Quantity pill', desc: 'An unchecked coffee-count pill (white fill, theme-colour count and hairline border).', sel: '.tw-coffee-counter.bg-white' });
  await S('c-amount', q('input[aria-label="quantity input"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Custom amount', desc: 'The free-amount field inside the last quantity pill (number input, "20").', sel: 'input[aria-label="quantity input"]' });
  await S('c-name', q('input#supporterDisplayName, input[placeholder*="Name or @"]').filter({ visible: true }).first(), ['default', 'focused', 'filled'], { group: g, title: 'Name field', desc: 'The "Name or @yoursocial" text input in the support widget.', sel: '#supporterDisplayName' }, { fillText: 'Ada' });
  await S('c-message', q('textarea[placeholder*="Say something"]').filter({ visible: true }).first(), ['default', 'focused'], { group: g, title: 'Message field', desc: 'The "Say something nice..." textarea (tw-box-common-v2).', sel: 'textarea Say something' });
  await S('c-monthly', q('label[for="doMonthlySupport"]').filter({ visible: true }).first(), B4, { group: g, title: 'Monthly checkbox', desc: 'The "Make this monthly" checkbox label; the visible box is a .tw-checkmark span.', sel: 'label[for=doMonthlySupport]' });
  await S('c-private', q('label[for="makeMsgPrivate"]').filter({ visible: true }).first(), B4, { group: g, title: 'Private checkbox', desc: 'The "Make this message private" checkbox label.', sel: 'label[for=makeMsgPrivate]' });
  await S('c-support', q('button.tw-btn-bg').filter({ hasText: /Support/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Support button', desc: 'The orange "Support $5" submit pill: a type=submit button measured in every state, never pressed.', sel: 'button.tw-btn-bg Support' });
  await S('c-supporter', q('[role="region"][aria-label="Recent supporters"] div').filter({ hasText: /bought/i }).filter({ visible: true }).last(), ['default'], { group: g, title: 'Supporter row', desc: 'A row in the Recent-supporters list ("SolanaNami bought 2 coffees"), avatar + text + more icon.', sel: 'supporter row' });
  await S('c-tier', q('[role="group"][aria-label*="membership level"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Membership tier', desc: 'A membership-level group in "Become a member": tier name, price, benefits list, Join button.', sel: '[role=group][aria-label*="membership level"]' });
  await S('c-join', q('[role="group"][aria-label*="membership level"] button, [role="group"][aria-label*="membership level"] a').filter({ hasText: /Join|month|year|\$/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Join button', desc: 'A membership tier\'s join action; measured never followed.', sel: 'tier Join button' });
  save();
}

async function login() {
  if (!(await newPage('login', { url: BASE + '/login', wait: 9000 }))) return;
  await sheetsFor('login');
  await chrome('login');
  await inlineVars('login');
  const g = G.login;
  await S('l-title', q('div, h1, h2').filter({ hasText: /^\s*Welcome back\s*$/ }).filter({ visible: true }).last(), ['default'], { group: g, title: 'Login title', desc: 'The "Welcome back" heading on the centred login card.', sel: 'Welcome back' });
  await S('l-email', q('input[type="text"], input[type="email"], input[placeholder*="Email" i]').filter({ visible: true }).first(), ['default', 'focused', 'filled'], { group: g, title: 'Email field', desc: 'The Email input on the login card (grey fill, rounded); typed into and cleared, never submitted.', sel: 'input Email' }, { fillText: 'name@example.com' });
  // The password input sits in a display:none second step that appears only
  // after "Continue with email" — a submit — so it is documented, not read.
  await S('l-cta', q('button.tw-btn-bg').filter({ hasText: /Continue with email|Login/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Continue button', desc: 'The yellow "Continue with email" pill (tw-btn-bg, theme-colour paint); a submit button measured, never pressed.', sel: 'button.tw-btn-bg Continue with email' });
  await S('l-social', q('button').filter({ hasText: /Continue with Google/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Social button', desc: 'A white "Continue with Google" button (greyE5 border, rounded-lg); measured never pressed.', sel: 'button Continue with Google' });
  await S('l-divider', q('div').filter({ hasText: /^\s*or login with\s*$/i }).filter({ visible: true }).last(), ['default'], { group: g, title: 'Divider', desc: 'The "or login with" divider between the email pill and the social buttons.', sel: 'or login with' });
  await S('l-signup-link', q('a').filter({ hasText: /^\s*Sign up\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Signup link', desc: 'The "Sign up" link at the card\'s top right ("Don\'t have an account?").', sel: 'Sign up link' });
  save();
}

async function reviews() {
  if (!(await newPage('reviews', { url: BASE + '/reviews', wait: 10000 }))) return;
  await sheetsFor('reviews');
  const g = G.reviews;
  await S('r-title', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Wall title', desc: 'The "Wall of ❤" page title.', sel: 'h1 on /reviews' });
  await S('r-tweet', q('a.tweet-card').filter({ visible: true }).first(), B4, { group: g, title: 'Tweet card', desc: 'A testimonial card on the Wall of Love (white, shadow-sm, slight transform on hover).', sel: 'a.tweet-card' });
  await S('r-slide', q('button[aria-label="slide next"]').filter({ visible: true }).first(), B4, { group: g, title: 'Slide button', desc: 'A carousel "slide next" button: 40px square bordered control, dark fill on hover.', sel: 'button[aria-label="slide next"]' });
  save();
}

async function faq() {
  if (!(await newPage('faq', { url: BASE + '/faq', wait: 9000 }))) return;
  const g = G.faq;
  await S('f-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'FAQ title', desc: 'The "Frequently Asked Questions" heading.', sel: 'h1 on /faq' });
  await S('f-q', q('h2').filter({ visible: true }).first(), ['default'], { group: g, title: 'FAQ question', desc: 'A question heading (static, not an accordion).', sel: 'h2 question' });
  await S('f-a', q('h3').filter({ visible: true }).first(), ['default'], { group: g, title: 'FAQ answer', desc: 'An answer paragraph under a question.', sel: 'h3 answer' });
  await S('f-cta', q('a.bmc-btn').filter({ hasText: /Contact support/i }).filter({ visible: true }).first(), B4, { group: g, title: 'FAQ CTA', desc: 'A bordered "Contact support" pill (btn-with-br-2-dark variant); measured never followed.', sel: 'a.bmc-btn Contact support' });
  save();
}

async function footer() {
  if (!(await newPage('home', { wait: 6000 }))) return;
  const g = G.footer;
  await page.evaluate(() => scrollTo(0, document.documentElement.scrollHeight));
  await page.waitForTimeout(1500);
  const foot = q('[data-v-35e7fb9e]').first();
  await S('footer', foot, ['default'], { group: g, title: 'Footer', desc: 'The marketing footer bar (its own Vue component): the Apps/Resources/Legal drop-up triggers, socials and the legal line; the link lists live in the drop-up panels.', sel: '[data-v-35e7fb9e] root' }, { noScroll: true });
  // Scope to the footer component (data-v-35e7fb9e) and take the deepest
  // match: "Legal" also lives in the trigger's ancestors up to the page root.
  const legal = () => q('[data-v-35e7fb9e] div').filter({ hasText: /Legal/ }).filter({ visible: true }).last();
  await S('footer-trigger', legal(), B4, { group: g, title: 'Footer trigger', desc: 'The "Legal" drop-up trigger in the footer bar; opens the legal link list.', sel: 'footer Legal trigger' }, { noScroll: true });
  // The Legal drop-up opens on its trigger's click; keep it open while the
  // panel and a link inside it are read and cropped.
  try {
    const t = legal();
    if (await t.count()) { await t.evaluate((el) => el.click()).catch(() => t.click({ timeout: 4000 })); await page.waitForTimeout(1200); }
  } catch (e) { log('  ! footer drop-up click failed', String(e.message).split('\n')[0]); }
  await S('footer-menu', q('[data-v-35e7fb9e] .drop-up-or-down, [data-v-35e7fb9e] div.absolute, [data-v-35e7fb9e] ul').filter({ hasText: /Terms of Use/ }).filter({ visible: true }).last(), ['default'], { group: g, title: 'Footer menu', desc: 'The drop-up panel the Legal trigger opens (Terms of Use, Privacy Policy, Cookie Policy...).', sel: 'footer .drop-up-or-down' }, { noScroll: true, noReset: true });
  await S('footer-link', q('[data-v-35e7fb9e] a[href*="/terms"], [data-v-35e7fb9e] a[href*="/privacy-policy"]').filter({ visible: true }).first(), B4, { group: g, title: 'Footer link', desc: 'A legal link inside the opened footer drop-up panel.', sel: 'footer a' }, { noScroll: true, noReset: true });
  await page.keyboard.press('Escape'); await page.waitForTimeout(500);
  await S('footer-social', q('a[href*="twitter.com"], a[href*="youtube.com"], a[href*="instagram.com"]').filter({ visible: true }).first(), B4, { group: g, title: 'Social link', desc: 'A social icon link in the footer.', sel: 'footer social a' }, { noScroll: true });
  save();
}

async function mobile() {
  if (!(await newPage('mobile', { mobile: true, url: BASE + '/' }))) return;
  await chrome('mobile');
  const g = G.mobile;
  await S('m-header', q('#bmc-header').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile header', desc: 'The header at 390: wordmark, Log-in link, Start-my-page pill and the burger.', sel: '#bmc-header at 390' }, { noScroll: true });
  const menu = q('#bmc-header div.cursor-pointer').filter({ visible: true }).first();
  await S('m-menu-button', menu, ['default'], { group: g, title: 'Menu button', desc: 'The burger that slides the full-screen menu in (translate-x-full -> translate-x-0).', sel: '#bmc-header div.cursor-pointer' }, { noScroll: true });
  try {
    if (await menu.count()) { await menu.click({ timeout: 5000 }).catch(() => menu.evaluate((el) => el.click())); await page.waitForTimeout(1500); }
  } catch (e) { log('  ! mobile menu toggle failed', String(e.message).split('\n')[0]); }
  await S('m-menu-open', q('div[class*="translate"]').filter({ hasText: /Wall of/ }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile menu, open', desc: 'The full-screen white panel the burger slides in (FAQ, Wall of, iOS, Android, Start my page).', sel: 'div[class*=translate] menu panel' }, { noScroll: true });
  await S('m-nav-item', q('a.mobile-nav-item').filter({ visible: true }).first(), B4, { group: g, title: 'Mobile nav item', desc: 'A link inside the opened mobile menu.', sel: 'a.mobile-nav-item' }, { noScroll: true });
  await page.keyboard.press('Escape'); await page.waitForTimeout(500);
  await S('m-hero', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile headline', desc: 'The hero display at 390.', sel: 'h1 at 390' });
  save();
}

run = new Date().toISOString().slice(0, 10);
out._meta.read = run;
out._meta.viewport = '1440 x 900 (mobile group 390 x 844); every public surface paints light — marketing on a #faf8f0 cream field, the Vite creator/login app on white with its own --theme-color* accents';
out._meta.tool = 'tools/capture/public/measure.mjs';
const { browser, context: ctx0 } = await launch();
context = ctx0;
const pages = process.argv.slice(2);
const plan = { home, creator, login, reviews, faq, mobile };
const order = Object.keys(plan).filter((k) => !pages.length || pages.includes(k));
try {
  for (const k of order) { if (k !== 'mobile') await plan[k](); }
  if (!pages.length || pages.includes('home')) await footer();
  if (!pages.length || pages.includes('mobile')) await plan.mobile();
  // Reduced-motion check on an element that actually transitions (the
  // bmc-btn's 0.2s ::before scale), so the delta is meaningful.
  if (!pages.length || pages.includes('home')) await reducedMotion('home', '#bmc-header a.bmc-btn');
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
