// Measures Exa's public components in every state reachable without
// signing in, submitting a form or firing the demo's real request.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node measure.mjs [page ...]
//
// Pages: home pricing product signin docs docsdark mobile.
// Writes raw/components-computed.json (merged) and one crop per component and
// state into components/crops/; raw/measurements.md is built by
// build-measurements.mjs.
//
// Exa's public surface is three sites: the exa.ai marketing pages (light
// only, a Next.js app), the Mintlify docs under exa.ai/docs in their real
// light and dark themes, and the auth.exa.ai login card dashboard.exa.ai
// redirects to (light only). Nothing is sent, bought or signed into: the
// only presses are local UI toggles — the header's hover mega-menu, the home
// demo's latency/category/output pills (they only re-configure the widget's
// preview, never fire it), a pricing use-case pill, the docs' code tabs and
// the mobile hamburger. The demo's "Run preview" arrow, Get-started/Sign-up
// actions and the login buttons are measured at rest and in forced/hover
// states, never pressed; the login e-mail field is focused and filled then
// cleared, never submitted.
import fs from 'node:fs';
import path from 'node:path';
import { BASE, AUTH_BASE, DOCS_BASE, M, launch, patch, open, closePromo, domFind, styleOf, crop, centre, hoverNavMenu, RAW, REF, CROPS, UA, UA_MOBILE } from './lib.mjs';

const OUT = process.env.OUT_JSON || path.join(RAW, 'components-computed.json');
const out = fs.existsSync(OUT) ? JSON.parse(fs.readFileSync(OUT, 'utf8')) : {};
out._meta ??= {};
out.components ??= {};
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const save = () => fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');
const URLS = {
  home: BASE + '/', pricing: BASE + '/pricing', product: BASE + '/products/search',
  signin: AUTH_BASE, docs: DOCS_BASE, docsdark: DOCS_BASE,
  mobile: BASE + '/',
};
let page, cdp, current, context, run, liveCtx;
const touched = new Set();
const listed = new Map();
// Routes a block or error gates this run: components last measured on them
// keep their earlier readings instead of being pruned below (a blocked pass
// must never erase evidence).
const failedPages = new Set();

async function blocked() {
  return page.evaluate(() => {
    const t = (document.body && document.body.innerText) || '';
    return /performing security verification|verifying you are human|just a moment|access denied|unusual activity from your computer network|not a robot|you have been blocked|unable to access|too many requests/i.test(t) || t.trim().length < 40;
  }).catch(() => true);
}

async function newPage(key, { mobile = false, wait = 8000, promo = 'close', url = null, scheme = 'light' } = {}) {
  current = key;
  // Close the previous page's context before opening the next: leaving them
  // alive keeps every captured page (and its animations) running in the
  // background for the rest of the run.
  if (liveCtx) { await liveCtx.close().catch(() => {}); liveCtx = null; }
  const b = context.browser();
  const ctx = liveCtx = await b.newContext(mobile
    ? { viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, userAgent: UA_MOBILE, isMobile: true, hasTouch: true, locale: 'en-US', colorScheme: scheme }
    : { viewport: { width: 1440, height: 900 }, deviceScaleFactor: 2, userAgent: UA, locale: 'en-US', colorScheme: scheme });
  await patch(ctx);
  page = await ctx.newPage();
  cdp = await ctx.newCDPSession(page);
  await cdp.send('DOM.enable');
  await cdp.send('CSS.enable');
  page.setDefaultTimeout(8000);
  log('open', key, mobile ? '(mobile)' : '', scheme === 'dark' ? '(dark)' : '');
  const cleared = await open(page, url || URLS[key], { wait, promo });  // false: the bot check did not clear (lib.mjs)
  if (!cleared || (await blocked())) { log('  BLOCKED', key); failedPages.add(key); await page.close(); await ctx.close(); liveCtx = null; return false; }
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
  Object.assign(c, { page: current, run, url: URLS[current] }, meta);
  touched.add(key);
  c.states ??= {};
  return c;
}

// First match with a non-empty box. Exa's header renders every nav item
// twice — once inside the hidden mobile drawer (display:none ancestors give
// 0x0 rects Playwright's :visible still passes) and once in the desktop nav —
// so .first() must skip the zero-size twins.
async function pick(loc) {
  const n = Math.min(await loc.count().catch(() => 0), 24);
  for (let i = 0; i < n; i++) {
    const has = await loc.nth(i).evaluate((el) => {
      const r = el.getBoundingClientRect();
      return r.width > 0 && r.height > 0;
    }).catch(() => false);
    if (has) return loc.nth(i);
  }
  return loc.first();
}

async function measure(key, state, target, opts = {}) {
  const loc = await pick(target.filter({ visible: true }));
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
    else c.states[state] = { error: String(e.message || e).slice(0, 200) };
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
  if (opts.open) { if (!opts.noReset) await reset(); try { await opts.open(); } catch (e) { log('  ! open failed', key, String(e.message).slice(0, 80)); } }
  const loc = await pick(target.filter({ visible: true }));
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
      } else via = via || 'at rest';
      if (st === 'focus-visible' && via === 'focus failed') {
        // Keyboard focus never reached the element, so a reading now would be the element at rest
        // saved as its focus. Record the miss instead (the builders list it as "focus could not be
        // captured"), and drop the crop an earlier run saved for this state.
        // An earlier run's real focus reading is kept, with the failed retry noted beside it.
        const prevSt = out.components[key].states[st];
        if (prevSt?.style && prevSt.via !== 'focus failed') {
          prevSt.rerunError = 'focus failed: keyboard focus did not reach the element';
          log('  !', key, st, 'focus failed; earlier reading kept');
        } else {
          const old = prevSt?.crop && path.resolve(REF, prevSt.crop);
          if (old && old.startsWith(CROPS + path.sep)) fs.rmSync(old, { force: true });
          out.components[key].states[st] = { skipped: 'focus failed: keyboard focus did not reach the element', via, run };
          log('  -', key, st, 'skipped: focus failed');
        }
      } else await measure(key, st, loc, { ...opts, via });
    } catch (e) {
      const prev = out.components[key].states[st];
      if (prev && prev.style) prev.rerunError = String(e.message || e).slice(0, 200);
      else out.components[key].states[st] = { error: String(e.message || e).slice(0, 200) };
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
const NEVER = /^(send|submit|sign in|log ?in|login|create|add|download|buy|purchase|pay|checkout|join|subscribe|save|apply|accept|reject|start|get started|claim|share|export|select|continue|claim this offer|try again|get a demo|request a demo|start reading|run preview|sign up|contact sales|get api key|try api for free|continue with google|continue with email)$/i;
async function toggle(loc, { allowLink = false } = {}) {
  const l = loc.filter({ visible: true }).first();
  const t = await l.evaluate((el) => ({ tag: el.tagName, type: el.getAttribute('type'), text: (el.innerText || el.getAttribute('aria-label') || '').trim() }));
  if (t.type === 'submit' || NEVER.test(t.text) || (t.tag === 'A' && !allowLink)) throw new Error(`toggle refused: ${t.tag} "${t.text}"`);
  await l.click({ timeout: 4000 }).catch(() => l.evaluate((el) => el.click()));
}

const q = (sel) => page.locator(sel);
const B4 = ['default', 'hover', 'focus-visible', 'pressed'];
const FIELD = ['default', 'focused', 'filled'];

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
async function reducedMotion(key, sel, text = null) {
  // `text` narrows `sel` to the named, visible element the normal pass measured (the header's
  // `a` also matches the logo link, which has no transition).
  const slot = `${key} ${sel}${text ? ` "${text.source}"` : ''}`; // one entry per element
  out._meta.reducedMotion ??= {};
  try {
    const b = context.browser();
    const ctx = await b.newContext({ viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1, userAgent: UA, locale: 'en-US', reducedMotion: 'reduce' });
    await patch(ctx);
    const p = await ctx.newPage();
    await p.goto(URLS[key], { waitUntil: 'domcontentloaded', timeout: 90000 }).catch(() => {});
    await p.waitForTimeout(7000);
    await closePromo(p);
    const v = await p.evaluate(([s, src]) => {
      const re = src && new RegExp(src);
      const el = [...document.querySelectorAll(s)].find((n) => {
        const r = n.getBoundingClientRect();
        return r.width > 0 && r.height > 0 && (!re || re.test((n.innerText || '').trim()));
      });
      if (!el) return null;
      const cs = getComputedStyle(el);
      return { transition: cs.transition, animation: cs.animation, scrollBehavior: getComputedStyle(document.documentElement).scrollBehavior };
    }, [sel, text && text.source]).catch(() => null);
    out._meta.reducedMotion[slot] = { page: key, selector: sel, text: text && text.source, reduce: v };
    await ctx.close();
  } catch (e) { out._meta.reducedMotion[slot] = { page: key, selector: sel, error: String(e).slice(0, 120) }; }
}

const G = {
  shell: 'Marketing chrome', home: 'Home hero and search demo', pricing: 'Pricing',
  product: 'Product pages', signin: 'Sign in (auth.exa.ai)',
  docs: 'Docs (exa.ai/docs)', footer: 'Footer', mobile: 'Mobile (390 wide)',
};

// The Products mega-menu: a div.cursor-pointer trigger that opens
// div.absolute.top-full on a real pointer hover — a local UI toggle whose
// links are never followed.
async function openProducts() {
  const openNow = (ms) => page.waitForFunction(
    () => [...document.querySelectorAll('div')].some((e) => e.className && /absolute/.test(e.className) && e.getBoundingClientRect().height > 100 && e.getBoundingClientRect().top >= 40 && e.getBoundingClientRect().top < 220 && (e.innerText || '').length > 60),
    undefined, { timeout: ms }).then(() => true).catch(() => false);
  if (await openNow(300)) return 'the products menu was already open';
  const ok = await hoverNavMenu(page, 'Products');
  if (ok) return 'hovered "Products" to open the mega-menu';
  return 'hovered "Products"; the menu did not report open';
}

// A pricing use-case pill ("Chatbots" etc.) — a local toggle that switches
// the price calculator's scenario, never a form post.
// The mobile nav: the "Toggle menu" button opens a drawer — a local toggle,
// its links never followed.
async function openMobileNav() {
  const openNow = (ms) => page.waitForFunction(
    () => [...document.querySelectorAll('nav, div, aside')].some((e) => { const r = e.getBoundingClientRect(); return r.height > 200 && /Products/.test(e.innerText || '') && getComputedStyle(e).position === 'fixed'; }),
    undefined, { timeout: ms }).then(() => true).catch(() => false);
  if (await openNow(400)) return 'the mobile nav was already open';
  const t = page.locator('button[aria-label="Toggle menu"]').filter({ visible: true }).first();
  if (!(await t.count())) return 'no hamburger';
  for (let i = 0; i < 3; i++) {
    await t.click({ timeout: 4000 }).catch(() => t.evaluate((el) => el.click()));
    if (await openNow(2500)) return 'clicked the hamburger to open the mobile nav';
    await page.waitForTimeout(500);
  }
  return 'clicked the hamburger; the nav did not report open';
}

// A demo widget pill (latency/category/output) — a local re-configuration of
// the preview panel; it never fires the search request itself.
async function demoPill(text) {
  const b = await page.evaluate((want) => {
    const el = [...document.querySelectorAll('button')].find((x) => (x.innerText || '').trim().replace(/\s+/g, ' ') === want && x.getBoundingClientRect().width > 0);
    if (!el) return false;
    el.click();
    return true;
  }, text);
  await page.waitForTimeout(900);
  return b;
}

async function home() {
  if (!(await newPage('home', { wait: 10000 }))) return;
  await sheetsFor('home');
  await chrome('home');
  const g = G.shell;
  await S('mkt-header', q('div.header'), ['default'], { group: g, title: 'Marketing header', desc: 'The sticky top bar: wordmark, Products/Solutions/Resources hover menus, Docs, Pricing, Sign in, Contact sales and Sign up, under the Exa 3.0 announcement strip.', sel: 'div.header' }, { noScroll: true });
  await S('mkt-announce', await domFind(page, /Introducing Exa 3\.0/, { sel: 'a, div, aside', tag: 'ann', up: 'div' }), ['default'], { group: g, title: 'Announcement strip', desc: 'The "Introducing Exa 3.0" banner over the header, with a Learn-more link and a dismiss button (never pressed).', sel: 'announcement banner' }, { noScroll: true });
  await S('mkt-logo', q('div.header a[href="/"]'), ['default'], { group: g, title: 'Logo', desc: 'The exa wordmark at the left of the header.', sel: 'header logo' }, { noScroll: true });
  await S('mkt-nav-trigger', q('div.header div.cursor-pointer').filter({ hasText: /^Products$/ }), ['default', 'hover'], { group: g, title: 'Products menu trigger', desc: 'The header "Products" item; the mega-menu opens on a real pointer hover, never a click.', sel: 'div.cursor-pointer Products' }, { noScroll: true });
  await S('mkt-menu', q('div.header div.absolute.top-full').filter({ hasText: /Search API/ }), ['default'], { group: g, title: 'Products mega-menu', desc: 'The dropdown the "Products" hover opens: Search/Contents/Agent/Monitors APIs, Exa Snapshot and Library, integrations and use cases — a local toggle, its links never followed.', sel: 'div.absolute.top-full' }, { open: openProducts, noScroll: true, noReset: true });
  await S('mkt-menu-item', q('div.header div.absolute a, div.header div.absolute [role="menuitem"]').filter({ hasText: /Search API/ }), ['default'], { group: g, title: 'Mega-menu link', desc: 'One product link inside the open mega-menu; measured, never followed.', sel: 'mega-menu link' }, { open: openProducts, noScroll: true, noReset: true });
  await page.keyboard.press('Escape').catch(() => {});
  await S('mkt-nav-link', q('div.header a').filter({ hasText: /^\s*(Docs|Pricing)\s*$/ }), B4, { group: g, title: 'Nav link', desc: 'A marketing header link (Docs/Pricing); measured, never followed.', sel: 'header nav link' }, { noScroll: true });
  await S('mkt-signin', q('div.header a').filter({ hasText: /^\s*Sign in\s*$/i }), B4, { group: g, title: 'Sign-in link', desc: 'The header "Sign in" link to dashboard.exa.ai; measured, never followed.', sel: 'header Sign in' }, { noScroll: true });
  await S('mkt-sales', q('div.header a').filter({ hasText: /^\s*Contact sales\s*$/i }), B4, { group: g, title: 'Contact-sales link', desc: 'The bordered "Contact sales" button-link; measured, never followed.', sel: 'header Contact sales' }, { noScroll: true });
  await S('mkt-signup', q('div.header a').filter({ hasText: /Sign up/i }), B4, { group: g, title: 'Sign-up button', desc: 'The black "Sign up" pill — the header\'s one filled action; measured, never followed.', sel: 'header Sign up' }, { noScroll: true });

  const h = G.home;
  await S('hero-h1', q('h1'), ['default'], { group: h, title: 'Hero headline', desc: '"The world\'s data for AI agents" — the ABC Arizona Flare display.', sel: 'h1' }, { noScroll: true });
  await S('hero-sub', q('p').filter({ hasText: /largest index/i }), ['default'], { group: h, title: 'Hero sub', desc: '"Search the largest index of public web and private information."', sel: 'hero sub' }, { noScroll: true });
  await S('hero-cta', await domFind(page, /Try API for free/, { sel: 'button, a', tag: 'herocta' }), B4, { group: h, title: 'Try-API CTA', desc: 'The black "Try API for free" button under the hero copy; measured never pressed (it leads to sign-up).', sel: 'Try API for free' }, { noScroll: true });
  // The public search demo widget: measured at rest and with its local pills
  // toggled; the "Run preview" arrow is never pressed.
  await S('demo-widget', q('div[class*="noprint"]').filter({ hasText: /latency/i }), ['default'], { group: h, title: 'Search demo widget', desc: 'The interactive preview card under the hero: query field, Search/Agent modes, latency and category pills, output tabs and a result panel that asks the visitor to sign in when the request cannot run.', sel: 'demo widget' });
  await S('demo-textarea', q('textarea'), FIELD, { group: h, title: 'Demo query field', desc: 'The "Find anything…" query box, pre-filled with "Latest open source LLMs"; focused and typed into then restored — the preview was never run.', sel: 'demo textarea' }, { fillText: 'latest research on fusion' });
  await S('demo-mode', q('button').filter({ hasText: /^\s*(Search|Agent)\s*$/ }), B4, { group: h, title: 'Demo mode toggle', desc: 'The Search/Agent segmented control at the top of the demo; measured, never pressed.', sel: 'demo Search/Agent' });
  await S('demo-pill', q('button').filter({ hasText: /^\s*(Auto|Lite|Deep)/ }), B4, { group: h, title: 'Latency pill', desc: 'A LATENCY pill (Lite 300ms / Auto 1s / Deep ~10s); switching it only re-configures the preview, never fires a request.', sel: 'demo latency pill' });
  await S('demo-category', q('button').filter({ hasText: /^\s*(Full Web|News|Companies)\s*$/ }), B4, { group: h, title: 'Category pill', desc: 'A CATEGORY pill (Full Web / News / Companies / Research / People / Financials); local toggle only.', sel: 'demo category pill' });
  await S('demo-output-tab', await domFind(page, /^(Results|Answer|Structured)$/, { sel: 'button, [role="tab"], div, span', tag: 'outtab' }), B4, { group: h, title: 'Output tab', desc: 'A Results/Answer/Structured output tab; local toggle only.', sel: 'demo output tab' });
  await S('demo-run', q('button[aria-label="Run preview"]'), ['default', 'hover'], { group: h, title: 'Run-preview button', desc: 'The blue arrow button that would fire the demo request; measured at rest and hovered — never pressed.', sel: 'demo run button' });
  await S('demo-output', await domFind(page, /couldn't verify your browser/, { sel: 'div, p, span', tag: 'demoout' }), ['default'], { group: h, title: 'Demo output panel', desc: 'The output area\'s signed-out state: "We couldn\'t verify your browser … Sign in to continue" — the widget\'s honest resting state in a headless browser.', sel: 'demo output' });
  await S('mkt-footer', q('footer'), ['default'], { group: G.footer, title: 'Footer', desc: 'The marketing footer: link columns, status and social marks.', sel: 'footer' });
  save();
}

async function pricing() {
  if (!(await newPage('pricing'))) return;
  await sheetsFor('pricing');
  await chrome('pricing');
  const g = G.pricing;
  // The plans are three bordered cards (STARTER Free / DEVELOPER Pay as you
  // go / ENTERPRISE Custom); the innermost div still holding both the tier
  // label and its action is the card itself.
  await S('plan-card', await domFind(page, /STARTER[\s\S]*Start building for free/, { sel: 'div, li', tag: 'plancard', minW: 200, minH: 250 }), ['default'], { group: g, title: 'Plan grid', desc: 'The pricing plans table (STARTER Free / DEVELOPER Pay as you go / ENTERPRISE Custom): a row-divided grid rather than three independent card divs — the smallest node still holding a tier label and its action.', sel: 'pricing grid' });
  await S('plan-price', await domFind(page, /^(Free|Pay as you go|Custom)$/, { sel: 'p, h2, h3, div, span', tag: 'planprice', minW: 40, minH: 16 }), ['default'], { group: g, title: 'Plan price', desc: 'A plan card\'s price line ("Free" / "Pay as you go" / "Custom").', sel: 'plan price' });
  await S('plan-cta', await domFind(page, /^(Start building for free|Get an API key|Upgrade now|Talk to sales)$/, { sel: 'button, a', tag: 'plancta' }), B4, { group: g, title: 'Plan CTA', desc: 'A plan card\'s action ("Start building for free" / "Get an API key" / "Talk to sales"); measured never pressed.', sel: 'plan CTA' });
  await S('plan-includes', await domFind(page, /Everything in Starter|MCP server access/, { sel: 'li, div', tag: 'planinc', minW: 100, minH: 16 }), ['default'], { group: g, title: 'Plan feature row', desc: 'A checkmarked "Includes:" feature row inside a plan card.', sel: 'plan includes row' });
  // One pill, read at rest and then selected by its own click: the 2026-11-13 run clicked
  // "Chatbots" before the loop and then measured "Coding agents" in every state.
  await S('pricing-pill', q('button').filter({ hasText: /^\s*Chatbots\s*$/ }), [...B4, 'opened'], { group: g, title: 'Use-case pill', desc: 'A pricing scenario pill ("Chatbots"), at rest and selected by its own click; its toggle switches the estimate — a local control, never a form post.', sel: 'pricing use-case pill (Chatbots)' });
  await S('pricing-h1', q('h1'), ['default'], { group: g, title: 'Pricing headline', desc: '"Start searching for free" — the pricing page heading.', sel: 'pricing h1' }, { noScroll: true });
  save();
}

async function product() {
  if (!(await newPage('product'))) return;
  await sheetsFor('product');
  await chrome('product');
  const g = G.product;
  await S('prod-h1', q('h1'), ['default'], { group: g, title: 'Product headline', desc: 'The /products/search page heading.', sel: 'product h1' }, { noScroll: true });
  // /products/search ships no pre/code blocks — its API samples are framed
  // visual mockups. Measure the alternating feature section instead.
  await S('prod-feature', await domFind(page, /Search the public web|semantic search/i, { sel: 'h2, h3, p', tag: 'prodfeat', up: 'section' }), ['default'], { group: g, title: 'Feature section', desc: 'An alternating feature block ("Search the public web and proprietary data through one API") with its framed visual card.', sel: 'feature section' });
  await S('prod-cta', await domFind(page, /Get started|Try|Start building/, { sel: 'button, a', tag: 'prodcta', minW: 40, minH: 16 }), B4, { group: g, title: 'Product CTA', desc: 'A product-page call to action; measured never followed.', sel: 'product CTA' });
  save();
}

async function signin() {
  if (!(await newPage('signin', { wait: 10000 }))) return;
  await sheetsFor('signin');
  await chrome('signin');
  const g = G.signin;
  // The innermost block holding the heading and both buttons: `form, main, [class*=card]`
  // caught the 360 x 98 e-mail form on 2026-11-13.
  await S('auth-card', await domFind(page, /Start building with Exa[\s\S]*Continue with email/, { sel: 'div, section, main', tag: 'authcard', minW: 300, minH: 200 }), ['default'], { group: g, title: 'Login card', desc: 'The "Start building with Exa" sign-in card on auth.exa.ai: heading, Continue-with-Google and Continue-with-email buttons, the e-mail field, SSO link and a code sample — measured, never submitted.', sel: 'login card' }, { noScroll: true });
  await S('auth-heading', q('h1'), ['default'], { group: g, title: 'Login heading', desc: '"Start building with Exa".', sel: 'login h1' }, { noScroll: true });
  await S('auth-google', await domFind(page, /Continue with Google/, { sel: 'button, a', tag: 'authg' }), B4, { group: g, title: 'Google button', desc: 'The "Continue with Google" OAuth button; measured never pressed.', sel: 'Continue with Google' }, { noScroll: true });
  await S('auth-email-btn', await domFind(page, /Continue with email/, { sel: 'button, a', tag: 'authe' }), B4, { group: g, title: 'Email button', desc: 'The "Continue with email" button; measured never pressed.', sel: 'Continue with email' }, { noScroll: true });
  await S('auth-email', q('input[type="email"], input[placeholder*="mail" i]'), FIELD, { group: g, title: 'Email field', desc: 'The "Email" input; focused and typed into then cleared — never submitted.', sel: 'login email input' }, { noScroll: true, fillText: 'name@example.com' });
  await S('auth-code', q('pre, code'), ['default'], { group: g, title: 'Code sample', desc: 'The exa.search() snippet the login page shows beside the card.', sel: 'login code sample' });
  save();
}

async function docsPage(scheme = 'light') {
  const key = scheme === 'dark' ? 'docsdark' : 'docs';
  if (!(await newPage(key, { wait: 10000, scheme }))) return;
  await sheetsFor(key);
  await chrome(key);
  const g = G.docs + (scheme === 'dark' ? ' (dark)' : ' (light)');
  const p = scheme === 'dark' ? 'd-' : '';
  await S(p + 'docs-sidebar', q('#sidebar, aside, nav[id*="sidebar" i], [class*="sidebar" i]'), ['default'], { group: g, title: 'Docs sidebar', desc: 'The docs left rail: search, the theme control and the nav tree (Overview / Get Started / Search / Agent / Other APIs).', sel: 'docs sidebar' }, { noScroll: true });
  await S(p + 'docs-logo', q('img.nav-logo'), ['default'], { group: g, title: 'Docs logo', desc: 'The exa mark at the top of the docs chrome.', sel: 'img.nav-logo' }, { noScroll: true });
  await S(p + 'docs-search', q('button[class*="docs-sidebar-search"], button#search-bar-entry'), B4, { group: g, title: 'Search button', desc: 'The "Search Ctrl K" field-styled button in the docs rail; measured, never opened.', sel: 'button.docs-sidebar-search' }, { noScroll: true });
  await S(p + 'docs-topbar-cta', q('li#topbar-cta-button a, #topbar-cta-button a').filter({ hasText: /API Dashboard/ }), B4, { group: g, title: 'Topbar CTA', desc: 'The "API Dashboard" button in the docs topbar; measured, never followed.', sel: '#topbar-cta-button a' }, { noScroll: true });
  await S(p + 'docs-theme-btn', q('button[aria-label*="theme" i], button[id*="theme" i]'), B4, { group: g, title: 'Theme button', desc: 'The docs theme preference button; measured, never opened (the dark capture used a prefers-color-scheme context instead).', sel: 'theme button' }, { noScroll: true });
  await S(p + 'docs-nav-item', q('aside a, nav a, [class*="sidebar" i] a').filter({ hasText: /^\s*(Quickstart|MCP|Overview)\s*$/ }), B4, { group: g, title: 'Nav item', desc: 'A docs sidebar link; measured, never followed.', sel: 'sidebar nav link' }, { noScroll: true });
  await S(p + 'docs-h1', q('h1'), ['default'], { group: g, title: 'Page heading', desc: 'The doc page\'s h1 ("Start building with Exa").', sel: 'docs h1' }, { noScroll: true });
  await S(p + 'docs-para', q('main p, article p, #content-area p'), ['default'], { group: g, title: 'Body paragraph', desc: 'A body paragraph in the doc.', sel: 'docs paragraph' });
  await S(p + 'docs-link', q('main a, article a').filter({ hasText: /\S{3,}/ }), B4, { group: g, title: 'Body link', desc: 'A link inside the doc body; measured, never followed.', sel: 'docs body link' });
  await S(p + 'docs-code', q('main pre, article pre, main code, article code'), ['default'], { group: g, title: 'Code block', desc: 'A code block or inline code span in the doc (Paper Mono).', sel: 'docs pre/code' });
  await S(p + 'docs-tab', await domFind(page, /^(Python|JavaScript|cURL)$/, { sel: 'button, [role="tab"], li, span', tag: 'codetab', up: 'button, [role="tab"], li', minW: 10, minH: 10 }), B4, { group: g, title: 'Code-language tab', desc: 'A Python/JavaScript/cURL language tab in the docs; local toggle only.', sel: 'docs language tab' });
  await S(p + 'docs-cta', await domFind(page, /Add Exa to your agent/, { sel: 'div, section, aside, a', tag: 'docscta', minH: 60 }), ['default'], { group: g, title: 'CTA banner', desc: 'The blue "Add Exa to your agent" banner with Get-Started and Get-API-Key actions — the actions measured, never followed.', sel: 'docs CTA banner' });
  await S(p + 'docs-assistant', q('textarea.chat-assistant-input, textarea[placeholder*="Ask" i]'), FIELD, { group: g, title: 'Assistant field', desc: 'The "Ask a question…" assistant input; focused and typed into then cleared — never sent.', sel: 'textarea.chat-assistant-input' }, { fillText: 'what is neural search' });
  save();
}

async function mobile() {
  if (!(await newPage('mobile', { mobile: true, url: BASE + '/' }))) return;
  await chrome('mobile');
  const g = G.mobile;
  await S('m-header', q('div.header'), ['default'], { group: g, title: 'Mobile header', desc: 'The top bar at 390: wordmark, hamburger and the Sign-up action.', sel: 'mobile header' }, { noScroll: true });
  await S('m-hamburger', q('button[aria-label="Toggle menu"]'), [...B4, 'opened'], { group: g, title: 'Hamburger', desc: 'The mobile nav toggle; opened to reveal the drawer — a local toggle, its links never followed.', sel: 'Toggle menu button' }, { noScroll: true });
  await S('m-drawer', q('div.header div.fixed'), ['default'], { group: g, title: 'Mobile nav drawer', desc: 'The full-height nav the hamburger opens (div.fixed inset-x-0 inside the header).', sel: 'mobile nav drawer' }, { open: openMobileNav, noScroll: true, noReset: true });
  await S('m-hero-h1', q('h1'), ['default'], { group: g, title: 'Hero headline (mobile)', desc: '"The world\'s data for AI agents" at 390 wide.', sel: 'h1' }, { noScroll: true });
  await S('m-demo-textarea', q('textarea'), FIELD, { group: g, title: 'Demo query field (mobile)', desc: 'The demo query box at 390; focused and typed into then restored — the preview was never run.', sel: 'demo textarea' }, { fillText: 'latest research on fusion' });
  save();
}

const PAGES = { home, pricing, product, signin, docs: () => docsPage('light'), docsdark: () => docsPage('dark'), mobile };
const want = process.argv.slice(2).filter((a) => !a.startsWith('-'));
const launched = await launch();
const browser = launched.browser;
context = launched.context;
run = new Date().toISOString();
out._meta.read = run.slice(0, 10);
const finishedPages = new Set();
try {
  for (const k of Object.keys(PAGES)) {
    if (want.length && !want.includes(k)) continue;
    await PAGES[k]();
    finishedPages.add(k);
  }
  // Controls that declare a transition (the header links transition colour over 0.15s); a
  // heading with no transition says nothing about reduced motion.
  await reducedMotion('home', 'div.header a', /^(Docs|Pricing)$/);
  await reducedMotion('home', 'button[aria-label="Run preview"]');
} finally {
  for (const k of failedPages) log('blocked:', k);
  // An untouched entry is pruned only when its page finished this run (a page the run never
  // reached, or an edge-blocked one, keeps its earlier readings under their own provenance), and
  // a touched entry keeps only the states this run's spec lists. comp() stamps every touched
  // entry with this run, so the old `c.run === run` guard could never prune anything.
  for (const [k, c] of Object.entries(out.components)) {
    if (!touched.has(k) && finishedPages.has(c.page) && !failedPages.has(c.page)) { delete out.components[k]; continue; }
    const wantSt = listed.get(k);
    if (wantSt) for (const st of Object.keys(c.states || {})) if (!wantSt.has(st)) delete c.states[st];
  }
  save();
  if (liveCtx) await liveCtx.close().catch(() => {});
  await context.close().catch(() => {});
  await browser.close();
}
