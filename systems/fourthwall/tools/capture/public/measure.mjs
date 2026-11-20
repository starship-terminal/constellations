// Measures fourthwall.com's public components in every state reachable without
// signing in or submitting anything.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node measure.mjs [page ...]
//
// Pages: home pricing blog compare cmparticle shops signup catalog pdp docs
//        docsart docsdark help helpcat helpdark mobile.
// Writes raw/components-computed.json (merged) and one crop per component and
// state into components/crops/; raw/measurements.md is built by
// build-measurements.mjs.
//
// fourthwall.com is a Webflow marketing site (the --_primitives---*/--gs* var
// layer): one light surface with scoped dark "on-ink" sections and no user
// theme toggle. products.fourthwall.com is the public catalogue on the
// light-dark() DS. /get-started redirects to auth.fourthwall.com (Keycloak)
// behind the same DS — measured at rest, never submitted. docs.fourthwall.com
// is Mintlify with a real theme menu (html.dark); help.fourthwall.com is
// Docusaurus with a real data-theme="dark" toggle. Specs select by role,
// aria-label, class or text. Nothing is sent, bought or signed into: the only
// presses are local UI toggles — the Features mega-menu, the signup modal,
// the billing toggle, FAQ disclosures, the compare/catalog/help search fields,
// a quiz option, the PDP size-guide dialog and print-type option, the docs
// search dialog and the docs/help theme toggles. "Sign in to design", "Start
// now" destinations, checkout and every provider button are measured, never
// activated; every link is measured, never followed. The Osano consent layer
// is hidden, never answered.
import fs from 'node:fs';
import path from 'node:path';
import { BASE, PRODUCTS, DOCS, HELP, SIGNUP_URL, PDP_URL, M, launch, patch, open, closePromo, domFind, styleOf, crop, centre, RAW, UA, UA_MOBILE } from './lib.mjs';

const OUT = process.env.OUT_JSON || path.join(RAW, 'components-computed.json');
const out = fs.existsSync(OUT) ? JSON.parse(fs.readFileSync(OUT, 'utf8')) : {};
out._meta ??= {};
out.components ??= {};
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const save = () => fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');
const URLS = {
  home: '/', pricing: '/pricing', blog: '/blog', compare: '/compare', cmparticle: '/compare/fourthwall-vs-shopify',
  shops: '/shops', inspired: '/get-inspired', contact: '/contact', signup: SIGNUP_URL,
  catalog: PRODUCTS + '/', pdp: PDP_URL, all: PRODUCTS + '/all',
  docs: DOCS + '/', docsart: DOCS + '/quickstart', docsdark: DOCS + '/quickstart',
  help: HELP + '/', helpcat: HELP + '/category/setting-up-your-shop', helpdark: HELP + '/category/setting-up-your-shop',
  mobile: '/',
};
// Hosts a page legitimately sits on besides its own: /get-started 302s to the
// Keycloak host, so the signup page's real surface is auth.fourthwall.com.
const PAGE_HOSTS = { signup: ['auth.fourthwall.com'] };
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

async function newPage(key, { mobile = false, wait = 9000, promo = 'close', url = null } = {}) {
  lazyDone = false;
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
  const loc = target;
  const c = out.components[key];
  try {
    const s = await styleOf(loc);
    let file;
    if (opts.crop !== false) {
      try {
        file = await crop(page, (opts.cropLoc || loc), `${key}-${state}`, opts.pad ?? 8);
      } catch (e) { s.cropError = String(e.message || e).slice(0, 120); }
    }
    c.states[state] = { ...s, crop: file, via: opts.via };
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
  if (opts.open) {
    await reset();
    try { await opts.open(); } catch (e) { log('  ! open failed', key, String(e.message).slice(0, 80)); }
  }
  // An open probe — or a late-firing navigation it started — can send the page
  // away: the nav "Start now" control goes to /get-started, which 302s to
  // auth.fourthwall.com (and once landed on chrome-error:// while page.url()
  // still reported the source at check time). Whatever happened, the page
  // must be back on its own host before the next measurement runs.
  const want = URLS[current];
  if (want) {
    const wantUrl = want.startsWith('http') ? want : BASE + want;
    const allowed = new Set([new URL(wantUrl).hostname, ...(PAGE_HOSTS[current] || [])]);
    let cur = '';
    try { cur = new URL(page.url()).hostname; } catch { /* chrome-error:// */ }
    if (!allowed.has(cur)) {
      log('  ! page drifted to', cur || page.url().slice(0, 60), '— reloading', current);
      if (!(await open(page, wantUrl, { wait: 8000 }))) {
        // a blocked reload measures nothing: earlier states keep their own
        // provenance and the page counts as failed, so cleanup prunes nothing
        failedPages.add(current);
        const has = Object.keys(out.components[key].states || {}).length > 0;
        log('  ! reload blocked, skipped', key, has ? '(earlier states kept)' : '');
        if (!has) out.components[key].missing = true;
        else { Object.assign(out.components[key], keep); out.components[key].recaptureMissed = run; }
        return;
      }
      lazyDone = false;
    }
  }
  let loc = await firstVisible(target);
  const box0 = await loc.boundingBox().catch(() => null);
  if (!(await loc.count()) || !box0 || box0.width < 2 || box0.height < 2) {
    await lazyScrollPage();
    loc = await firstVisible(target);
  }
  const box1 = await loc.boundingBox().catch(() => null);
  if (!(await loc.count()) || !box1 || box1.width < 2 || box1.height < 2) {
    const has = Object.keys(out.components[key].states || {}).length > 0;
    log('  ! missing', key, has ? '(earlier states kept)' : '');
    // Keep earlier evidence under its own provenance: the states stay but the
    // entry keeps its original page/run/url and records the miss, so a re-run
    // never republishes old readings under a new date.
    if (!has) out.components[key].missing = true;
    else { Object.assign(out.components[key], keep); out.components[key].recaptureMissed = run; }
    return;
  }
  // A broad selector re-resolves against the live DOM on every use, so an
  // overlay that mounts mid-run (a search dialog, a modal) can swap the node a
  // state reads. opts.pin marks the resolved element once and every state
  // below measures that same node.
  if (opts.pin) {
    await loc.evaluate((el) => el.setAttribute('data-m-pin', '1')).catch(() => {});
    loc = page.locator('[data-m-pin="1"]').first();
  }
  for (const st of list) {
    let undo, via;
    try {
      if (!opts.noReset) await reset();
      if (!opts.noScroll) await centre(loc);
      if (opts.before?.[st]) via = await opts.before[st](loc);
      if (st === 'hover') {
        await (opts.hoverLoc || loc).hover({ timeout: 5000 }).catch(() => (opts.hoverLoc || loc).hover({ timeout: 5000, force: true }));
        await page.waitForTimeout(450);
        via = 'mouse hover';
      } else if (st === 'focus-visible') {
        via = await kbFocus((opts.focusLoc || loc));
      } else if (st === 'pressed') {
        undo = await forcePseudo((opts.pressLoc || loc), ['active', 'hover']);
        via = 'CDP forcePseudoState :active:hover';
      } else if (st === 'focused') {
        const fld = (opts.fieldLoc || loc);
        await fld.click({ timeout: 4000 }).catch(() => fld.evaluate((el) => el.focus()));
        await page.waitForTimeout(400);
        via = 'clicked into the field';
      } else if (st === 'filled') {
        const f = (opts.fieldLoc || loc);
        await f.click({ timeout: 4000 }).catch(() => f.evaluate((el) => el.focus()));
        await page.keyboard.type(opts.fillText || 'name@example.com', { delay: 10 });
        await page.waitForTimeout(500);
        undo = async () => { await f.focus(); await page.keyboard.press('ControlOrMeta+a'); await page.keyboard.press('Backspace'); await page.waitForTimeout(300); };
        via = `typed "${opts.fillText || 'name@example.com'}", then deleted; nothing sent`;
      } else if (st === 'opened') {
        // A before.opened callback already toggled the control open — a second
        // generic click would close it again before the reading.
        if (opts.noToggle) via = 'held open by an earlier toggle';
        else if (!via) { await toggle(loc, { allowLink: opts.allowLink }); await page.waitForTimeout(900); via = 'own toggle'; }
        const exp = await loc.evaluate((el) => el.getAttribute('aria-expanded')).catch(() => null);
        if (exp !== null) via = (via || 'opened') + (exp === 'true' ? ' (aria-expanded=true at save)' : ' (aria-expanded=false at save — the open did not hold)');
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
  if (opts.pin) await page.evaluate(() => document.querySelectorAll('[data-m-pin]').forEach((n) => n.removeAttribute('data-m-pin'))).catch(() => {});
  await reset();
}

// Clicks a UI toggle (dropdown, menu, sheet trigger). Refuses a submit button
// and any control whose text names an action this kit must never take.
const NEVER = /^(send|send message|submit|sign in|log ?in|login|create|add|download|buy|purchase|pay|checkout|join|subscribe|save|apply|accept|reject|start|start now|get started|claim|share|export|select|continue|continue with.*|claim this offer|try again|start for free|sign in to design|sign up)$/i;
// Every scripted click in this file goes through toggle(), so NEVER applies to
// the hooks and openers too (edited 2026-11 audit; not run since).
async function toggle(loc, { allowLink = false } = {}) {
  const l = loc;
  const t = await l.evaluate((el) => ({ tag: el.tagName, type: el.getAttribute('type'), text: (el.innerText || el.getAttribute('aria-label') || '').trim() }));
  if (t.type === 'submit' || NEVER.test(t.text) || (t.tag === 'A' && !allowLink)) throw new Error(`toggle refused: ${t.tag} "${t.text}"`);
  await l.click({ timeout: 4000 }).catch(() => l.evaluate((el) => el.click()));
}

const q = (sel) => page.locator(sel);
const B4 = ['default', 'hover', 'focus-visible', 'pressed'];

// The first element matching `sel` whose trimmed text is at least `min` chars
// (hasText cannot express a trimmed length — /\S{20,}/ means twenty
// *consecutive* non-space characters, which no normal paragraph matches).
const p20 = async (sel, min = 20) => {
  const all = q(sel).filter({ visible: true });
  const n = Math.min(await all.count(), 15);
  for (let i = 0; i < n; i++) {
    const t = ((await all.nth(i).innerText().catch(() => '')) || '').trim();
    if (t.length >= min) return all.nth(i);
  }
  return all.first();
};

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
  shell: 'Site chrome', home: 'Home', pricing: 'Pricing', blog: 'Blog',
  compare: 'Compare', cmparticle: 'Comparison page', shops: 'Shops',
  inspired: 'Get inspired', contact: 'Contact', signup: 'Signup (auth shell)',
  catalog: 'Product catalogue', pdp: 'Product page', docs: 'Developer docs',
  docsdark: 'Developer docs (dark)', help: 'Help center', helpdark: 'Help center (dark)',
  mobile: 'Mobile (390 wide)', footer: 'Footer', ink: 'On-ink (dark sections)',
};

// Hovers/clicks the "Features" nav item — the Webflow mega-menu opens on
// hover; its links are never followed.
async function openMega() {
  const trig = page.locator('.nav-bar a, .nav-bar [role="button"], .nav-bar .nav-link, .nav-bar .w-dropdown-toggle').filter({ hasText: /Features/i }).first();
  if (!(await trig.count())) return 'no Features nav item';
  const open = async () => page.evaluate(() => { const c = document.querySelector('.mega-clip, .nav-menu .w-dropdown-list, [class*="mega"]'); if (!c) return false; const r = c.getBoundingClientRect(); const cs = getComputedStyle(c); return r.height > 60 && cs.display !== 'none' && parseFloat(cs.opacity) > 0.05; }).catch(() => false);
  if (await open()) return 'the mega-menu was already open';
  await trig.hover({ timeout: 5000 }).catch(() => trig.hover({ timeout: 5000, force: true }));
  await page.waitForTimeout(1200);
  if (await open()) return 'hovered Features to open the mega-menu';
  await toggle(trig, { allowLink: true });
  await page.waitForTimeout(900);
  return (await open()) ? 'clicked Features to open the mega-menu' : 'the mega-menu did not report open';
}

// The nav "Start now" control navigates to /get-started, which 302s to
// auth.fourthwall.com — there is no local signup modal on the marketing
// home. The signed-out auth choices are measured on the 'signup' page
// instead; the control itself is never activated here.

// Opens the PDP size-guide dialog — a local UI toggle mounting a size table.
async function openSizeGuide() {
  const btn = page.locator('button, [role="button"], a').filter({ hasText: /Size guide/i }).first();
  if (!(await btn.count())) return 'no size-guide control';
  await toggle(btn, { allowLink: true });
  await page.waitForTimeout(1200);
  const open = await page.evaluate(() => { const d = document.querySelector('[role="dialog"], [class*="dialog"], [class*="modal"]'); return d && d.getBoundingClientRect().height > 60; }).catch(() => false);
  return open ? 'clicked "Size guide" to open the size dialog' : 'clicked "Size guide"; the dialog did not report open';
}

// Clicks the docs search — opens the Mintlify dialog on the
// button[aria-label="Open search"] trigger; nothing is sent.
async function openDocsSearch() {
  const f = page.locator('button[aria-label="Open search"], button[data-search-item="trigger"], input[placeholder*="earch"], button[aria-label*="earch"], [class*="search"] button, button[class*="search"]').first();
  if (!(await f.count())) return 'no docs search';
  await toggle(f);
  await page.waitForTimeout(1500);
  const open = await page.evaluate(() => [...document.querySelectorAll('[role="dialog"], [cmdk-root], input[placeholder="Search..."]')].some((d) => { const r = d.getBoundingClientRect(); return r.width > 100 && r.height > 40; })).catch(() => false);
  return open ? 'clicked the docs search to open its dialog' : 'clicked the docs search; the dialog did not report open';
}

// Opens the docs "Change theme preference" menu — a local UI toggle.
async function openDocsThemeMenu() {
  const btn = page.locator('button[aria-label="Change theme preference"], button[aria-label*="theme preference" i]').first();
  if (!(await btn.count())) return 'no theme menu button';
  await toggle(btn, { allowLink: true });
  await page.waitForTimeout(900);
  const open = await page.evaluate(() => { const m = document.querySelector('[role="menu"], [data-radix-popper-content-wrapper]'); return m && m.getBoundingClientRect().height > 40; }).catch(() => false);
  return open ? 'clicked "Change theme preference" to open the theme menu' : 'clicked the theme button; the menu did not report open';
}

// The docs site's real dark toggle: theme menu -> Dark, sets html.dark
// (persisted in localStorage inside this context).
async function docsDarkOn() {
  const cur = await page.evaluate(() => document.documentElement.classList.contains('dark')).catch(() => false);
  if (cur) return 'the docs page already painted html.dark';
  const btn = page.locator('button[aria-label="Change theme preference"], button[aria-label*="theme preference" i]').first();
  if (!(await btn.count())) return 'no theme menu button';
  await toggle(btn, { allowLink: true });
  await page.waitForTimeout(900);
  const dk = page.locator('[role="menu"] *, [data-radix-popper-content-wrapper] *, [role="menuitem"], [role="option"]').filter({ hasText: /^Dark$/ }).first();
  if (!(await dk.count())) { await page.keyboard.press('Escape').catch(() => {}); return 'the theme menu listed no Dark item'; }
  await toggle(dk);
  await page.waitForTimeout(1200);
  return 'chose Dark in the docs site\'s own "Change theme preference" menu — the user-facing toggle';
}

// Types into the help navbar search — the Docusaurus local-search filter.
async function openHelpSearch() {
  const f = page.locator('.navbar input[type="search"], input[placeholder*="earch"], input[type="search"]');
  if (!(await f.count())) return 'no help search field';
  await f.click({ timeout: 4000 }).catch(() => f.evaluate((el) => el.focus()));
  await page.keyboard.type('storefront', { delay: 20 });
  await page.waitForTimeout(1500);
  const open = await page.evaluate(() => { const pop = document.querySelector('[class*="search-result"], [class*="dropdown"], [class*="SearchResults"]'); return pop && pop.getBoundingClientRect().height > 40; }).catch(() => false);
  return open ? 'typed "storefront" into the help search; the results dropdown opened' : 'typed "storefront" into the help search';
}

// The help site's real dark toggle: the Docusaurus colour-mode button in the
// navbar sets <html data-theme="dark"> (persisted in this context).
async function helpDarkOn() {
  const cur = await page.evaluate(() => document.documentElement.getAttribute('data-theme')).catch(() => null);
  if (cur === 'dark') return 'the help page already painted data-theme=dark';
  const btn = page.locator('button[aria-label*="Switch between" i], [class*="colorModeToggle"] button, button[class*="colorModeToggle"], button[class*="toggleButton"], .navbar button[class*="toggle"]');
  // The toggle cycles system -> light -> dark -> …, so keep clicking until
  // dark paints (three clicks covers the whole cycle).
  for (let i = 0; i < 3; i++) {
    let b = btn;
    if (!(await b.count())) {
      const fb = page.locator('.navbar__items--right button, .navbar__items button').last();
      if (!(await fb.count())) return 'no dark-mode toggle';
      b = fb;
    }
    await toggle(b);
    await page.waitForTimeout(1100);
    const t = await page.evaluate(() => document.documentElement.getAttribute('data-theme')).catch(() => null);
    if (t === 'dark') return 'clicked the help site\'s own colour-mode toggle until data-theme=dark painted — the user-facing control';
  }
  return 'clicked the colour-mode toggle; data-theme=dark never painted';
}

const FIELD = ['default', 'focused', 'filled'];

// Marketing sections lazy-mount near the viewport, so a below-fold component
// is display:none until the page has been scrolled. The first miss on a page
// triggers one lazy pass, then the locator is re-resolved.
let lazyDone = false;
async function lazyScrollPage() {
  if (lazyDone) return;
  lazyDone = true;
  const H = await page.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body ? document.body.scrollHeight : 0)).catch(() => 0);
  for (let y = 0; y < H; y += 600) { await page.evaluate((y) => scrollTo(0, y), y); await page.waitForTimeout(120); }
  await page.evaluate(() => scrollTo(0, 0));
  await page.waitForTimeout(900);
}

// The page mounts hidden duplicates of real controls (off-canvas drawers,
// collapsed menus, clipped modals) ahead of the visible one in DOM order, and
// Playwright's visible filter still counts some zero-size nodes as visible —
// so walk candidates and return the first with a real painted box.
async function firstVisible(target) {
  const n = Math.min(await target.count(), 30);
  for (let i = 0; i < n; i++) {
    const bb = await target.nth(i).boundingBox().catch(() => null);
    if (bb && bb.width > 2 && bb.height > 2) return target.nth(i);
  }
  return target.first();
}

async function home() {
  if (!(await newPage('home'))) return;
  await sheetsFor('home');
  await chrome('home');
  const g = G.shell;
  await S('mkt-nav', q('nav.nav-bar'), ['default'], { group: g, title: 'Nav bar', desc: 'The fixed top bar: the Fourthwall wordmark, the Features mega-menu and Learn dropdowns, Product catalog / Pricing links, Log in and the "Start now" pill.', sel: 'nav.nav-bar' }, { noScroll: true });
  await S('mkt-logo', q('nav.nav-bar a[href="/"], .nav-bar a'), ['default'], { group: g, title: 'Wordmark', desc: 'The Fourthwall wordmark in the nav, linking home.', sel: 'nav.nav-bar wordmark' }, { noScroll: true });
  await S('nav-features', q('.nav-bar a, .nav-bar [role="button"], .nav-bar .nav-link, .nav-bar .w-dropdown-toggle').filter({ hasText: /^Features$/ }), B4, { group: g, title: 'Mega-menu trigger', desc: 'The "Features" nav item that opens the mega-menu on hover; its links were never followed.', sel: '.nav-bar Features' }, { noScroll: true });
  await S('nav-link', q('.nav-menu a, .nav-bar a').filter({ hasText: /^Pricing$/ }), B4, { group: g, title: 'Nav link', desc: 'A marketing nav link (Pricing); measured, never followed.', sel: '.nav-bar Pricing' }, { noScroll: true });
  await S('nav-login', q('.nav-bar a, .nav-menu a').filter({ hasText: /^Log ?in$/i }), B4, { group: g, title: 'Log in link', desc: 'The "Log in" nav link to the shop admin; measured, never followed.', sel: '.nav-bar Log in' }, { noScroll: true });
  // The real pill is a.btn-primary whose two label spans make its text
  // "Start now|Start now" — an anchored regex misses it and would catch a
  // full-bleed marquee band instead.
  await S('nav-cta', q('.nav-bar a.btn-primary').filter({ hasText: /Start now/i }), B4, { group: g, title: 'Start now button', desc: 'The "Start now" pill in the nav — it links to /get-started; measured, never activated.', sel: '.nav-bar a.btn-primary' }, { noScroll: true });
  await S('mega-clip', q('.mega-clip, .nav-menu .w-dropdown-list, [class*="mega"]'), ['default'], { group: g, title: 'Mega-menu panel', desc: 'The Features mega-menu panel — nav columns plus featured cards; opened by hovering its own trigger.', sel: '.mega-clip' }, { open: openMega, noScroll: true, noReset: true });
  await page.mouse.move(10, 600);
  await page.keyboard.press('Escape').catch(() => {});
  const h = G.home;
  await S('hero-h1', q('h1'), ['default'], { group: h, title: 'Hero headline', desc: '"One platform for premium products and branded shops." — the display masthead.', sel: 'h1' }, { noScroll: true });
  await S('hero-sub', await p20('h1 ~ p, h1 + p, p').then((l) => l), ['default'], { group: h, title: 'Hero lede', desc: 'The hero standfirst under the masthead.', sel: 'hero lede' });
  await S('hero-cta', q('.hero-cta-row a.btn-primary, .hero-foot a.btn-primary, section a.btn-primary').filter({ hasText: /Start now/i }), B4, { group: h, title: 'Hero CTA', desc: 'The primary "Start now" hero action — the only hero action; measured, never followed.', sel: '.hero-cta-row a.btn-primary' });
  // No hero-cta2: the hero carries a single action; the broad "See/Explore"
  // filter previously matched a hidden mega-menu card. The cards themselves:
  await S('mega-card', q('a.mega-card'), ['default'], { group: g, title: 'Mega-menu card', desc: 'A .mega-card tile inside the Features mega-menu (Get inspired / Designers / Help / Blog); measured with the menu open, never followed. The tiles compute visibility:hidden until a Webflow reveal — earlier passes read mid-reveal or before it; the settle wait lets it paint.', sel: 'a.mega-card' }, { open: openMega, noScroll: true, noReset: true });
  await page.mouse.move(10, 600);
  await page.keyboard.press('Escape').catch(() => {});
  // No signup-modal/signup-google entries: "Start now" navigates to the
  // auth host rather than opening a modal (measured as the 'signup' page).
  await S('tile', q('a.ph-tile, .ph-tile'), ['default', 'hover'], { group: h, title: 'Product tile', desc: 'A .ph-tile product/showcase tile in the home scatter grid (product card with hover-swap imagery).', sel: 'a.ph-tile' });
  await S('rating-card', q('.ph-tile-rating'), ['default'], { group: h, title: 'Rating chip', desc: 'The star-rating chip inside a product tile (rating + price).', sel: '.ph-tile-rating' });
  await S('brand-grid', q('.ws--trusted'), ['default'], { group: h, title: 'Logo wall', desc: 'The .ws--trusted "trusted by" section — the creator/company logo wall.', sel: '.ws--trusted' });
  await S('design-preview', q('.design-preview, .design-preview-track, .design-col--preview'), ['default'], { group: h, title: 'Design preview carousel', desc: 'The storefront design-preview carousel in the .on-ink design section.', sel: '.design-preview' });
  const k = G.ink;
  await S('leg-section', q('.page-section.on-ink, .leg-section.gs1000, .leg-section'), ['default'], { group: k, title: 'Dark feature section', desc: 'A .page-section.on-ink dark band — the sheet\'s own on-ink scope class repaints the --_surface---* variables; measured as painted, no theme toggle exists.', sel: '.page-section.on-ink' });
  await S('made-with', q('.made-with'), ['default'], { group: k, title: 'Made-with band', desc: 'The .made-with "Made with Fourthwall" storefront showcase band — on-ink surface values.', sel: '.made-with' });
  await S('wordmark-section', q('.wordmark-section'), ['default'], { group: k, title: 'Wordmark section', desc: 'The dark "Made with Fourthwall" wordmark band — on-ink surface values.', sel: '.wordmark-section' });
  await S('closer', q('.closer-section'), ['default'], { group: k, title: 'Closing CTA section', desc: 'The closing "Make something worth buying / Start now for free" section.', sel: '.closer-section' });
  await S('closer-cta', q('a.closer-link, .closer-section a').filter({ hasText: /Make something|Start now/i }), B4, { group: k, title: 'Closer CTA', desc: 'The giant "Make something worth buying" word-link in the closing section — it carries the start flow; measured, never followed.', sel: '.closer-section a.closer-link' });
  const f = G.footer;
  await S('footer', q('footer.site-footer, .site-footer, footer').last(), ['default'], { group: f, title: 'Footer', desc: 'The .site-footer.is-warm footer — sitemap columns, social and legal links on the ink surface.', sel: 'footer.site-footer' }, { noScroll: true });
  await S('footer-link', q('footer a, .site-footer a').filter({ hasText: /^Pricing$/ }).last(), B4, { group: f, title: 'Footer link', desc: 'A footer sitemap link; measured, never followed.', sel: 'footer Pricing link' }, { noScroll: true });
  save();
}

async function pricing() {
  if (!(await newPage('pricing'))) return;
  await sheetsFor('pricing');
  const g = G.pricing;
  await S('price-h1', q('h1'), ['default'], { group: g, title: 'Pricing headline', desc: 'The /pricing masthead.', sel: 'pricing h1' }, { noScroll: true });
  await S('billing-toggle', q('.billing-toggle'), ['default'], { group: g, title: 'Billing toggle', desc: 'The "Pay yearly / Pay monthly" toggle — the monthly state was painted by clicking it (a local UI toggle; Pro reads $19 vs $15).', sel: '.billing-toggle' });
  await S('billing-btn', q('.billing-toggle-btn').filter({ hasText: /monthly/i }).first(), B4, { group: g, title: 'Billing option', desc: 'The "Pay monthly" toggle button; measured, and clicked once to paint the monthly state.', sel: '.billing-toggle-btn monthly' });
  // .pricing-plans is the two-column grid itself (1120px wide) — the cards are
  // its .plan-card children; .plan-feature rows live inside each card's
  // .plan-features list (.ph-faq-summary is the FAQ disclosure, not a row).
  await S('plan-card', q('.pricing-plans .plan-card'), ['default', 'hover'], { group: g, title: 'Plan card', desc: 'A plan card on /pricing (Free / Pro) — one .plan-card cell inside the .pricing-plans grid.', sel: '.pricing-plans .plan-card' });
  await S('plan-row', q('.plan-card .plan-feature'), ['default'], { group: g, title: 'Plan feature row', desc: 'A .plan-feature row inside a plan card\'s .plan-features list.', sel: '.plan-card .plan-feature' });
  await S('faq-summary', q('.ph-faq-summary'), [...B4, 'opened'], { group: g, title: 'FAQ disclosure', desc: 'A disclosure button in the pricing FAQ; the opened state was measured after clicking it (a local UI toggle).', sel: '.ph-faq-summary' }, { before: { opened: async (loc) => { await toggle(loc); await page.waitForTimeout(700); return 'clicked the FAQ summary to expand its answer'; } } });
  save();
}

async function blog() {
  if (!(await newPage('blog'))) return;
  await sheetsFor('blog');
  const g = G.blog;
  await S('blog-h1', q('h1, h2'), ['default'], { group: g, title: 'Blog headline', desc: 'The /blog masthead.', sel: 'blog h1' }, { noScroll: true });
  await S('blog-card', q('a[href*="/blog/"]'), ['default', 'hover'], { group: g, title: 'Post card', desc: 'A post card on the blog index; measured, never followed.', sel: 'blog post card' });
  await S('blog-news', q('input[type="email"], input[placeholder*="mail" i]'), FIELD, { group: g, title: 'Newsletter field', desc: 'The newsletter email input on /blog; focused and typed into then cleared — never subscribed.', sel: 'blog email input' }, { fillText: 'name@example.com' });
  save();
}

async function compare() {
  if (!(await newPage('compare'))) return;
  await sheetsFor('compare');
  const g = G.compare;
  await S('cmp-h1', q('h1'), ['default'], { group: g, title: 'Compare headline', desc: 'The /compare masthead.', sel: 'compare h1' }, { noScroll: true });
  await S('cmp-search', q('input[type="search"], .cmp-search input, input[placeholder*="earch"]'), FIELD, { group: g, title: 'Platform search', desc: 'The "Compare Fourthwall to…" search field; focused and typed into then cleared — a local filter, nothing sent.', sel: '.cmp-search input' }, { fillText: 'shopify' });
  await S('cmp-card', q('main a[href*="/compare/"], .page-section a[href*="/compare/"], .page-content a[href*="/compare/"]'), ['default', 'hover'], { group: g, title: 'Comparison card', desc: 'A comparison card linking to a vs-page (Shopify, Patreon…); measured, never followed.', sel: 'compare card' });
  save();
}

async function cmparticle() {
  if (!(await newPage('cmparticle'))) return;
  await sheetsFor('cmparticle');
  const g = G.cmparticle;
  await S('cmpart-h1', q('h1'), ['default'], { group: g, title: 'Vs-page headline', desc: 'The "Fourthwall vs Shopify" masthead.', sel: 'cmparticle h1' }, { noScroll: true });
  // The vs-page uses no <table>: the "Choose Fourthwall if / Choose Shopify
  // if" pair lives in .cmp2-pair > .plan-card.
  await S('cmpart-card', q('.cmp2-pair .plan-card, .cmp2-pair > div'), ['default'], { group: g, title: 'Vs comparison card', desc: 'A "Choose X if" card in the .cmp2-pair comparison on a vs-page.', sel: '.cmp2-pair .plan-card' });
  save();
}

async function shops() {
  if (!(await newPage('shops'))) return;
  await sheetsFor('shops');
  const g = G.shops;
  await S('shops-h1', q('h1'), ['default'], { group: g, title: 'Shops headline', desc: 'The /shops masthead.', sel: 'shops h1' }, { noScroll: true });
  await S('shops-tile', q('a.brand-card, a.pg-card'), ['default', 'hover'], { group: g, title: 'Shop tile', desc: 'An example-shop card on /shops (.brand-card showcase / .pg-card grid); measured, never followed.', sel: 'a.brand-card' });
  save();
}

async function inspired() {
  if (!(await newPage('inspired'))) return;
  const g = G.inspired;
  await S('insp-h1', q('h1'), ['default'], { group: g, title: 'Get-inspired headline', desc: 'The /get-inspired masthead.', sel: 'inspired h1' }, { noScroll: true });
  await S('insp-card', q('a.ex-tile'), ['default', 'hover'], { group: g, title: 'Creator card', desc: 'An .ex-tile creator/showcase card on /get-inspired; measured, never followed.', sel: 'a.ex-tile' });
  save();
}

async function contact() {
  if (!(await newPage('contact'))) return;
  const g = G.contact;
  await S('contact-h1', q('h1'), ['default'], { group: g, title: 'Contact headline', desc: 'The /contact masthead.', sel: 'contact h1' }, { noScroll: true });
  await S('contact-card', q('a.contact-card'), ['default', 'hover'], { group: g, title: 'Contact card', desc: 'An a.contact-card on /contact (Contact support / Contact sales); measured, never followed.', sel: 'a.contact-card' });
  save();
}

async function signup() {
  if (!(await newPage('signup', { wait: 10000 }))) return;
  await sheetsFor('signup');
  await chrome('signup');
  const g = G.signup;
  await S('auth-card', q('div').filter({ has: q('button, a, input[type="submit"]').filter({ hasText: /Google/i }) }).last(), ['default'], { group: g, title: 'Auth card', desc: 'The signed-out auth surface at /get-started (auth.fourthwall.com, Keycloak on the catalogue DS) — the panel holding the Google/Apple/email choices; measured at rest, nothing pressed.', sel: 'auth card' }, { noScroll: true });
  await S('auth-google', q('button, a, [role="button"], input[type="submit"]').filter({ hasText: /Google/i }), B4, { group: g, title: 'Google provider', desc: 'The "Continue with Google" provider button; states measured, never pressed — no OAuth flow was started.', sel: 'auth Google' }, { noScroll: true });
  await S('auth-apple', q('button, a, [role="button"], input[type="submit"]').filter({ hasText: /Apple/i }), B4, { group: g, title: 'Apple provider', desc: 'The "Continue with Apple" provider button; measured, never pressed.', sel: 'auth Apple' }, { noScroll: true });
  await S('auth-email', q('button, a, [role="button"], input[type="submit"]').filter({ hasText: /email/i }), B4, { group: g, title: 'Email provider', desc: 'The "Continue with email" action; measured, never pressed.', sel: 'auth email' }, { noScroll: true });
  await S('auth-login', q('a').filter({ hasText: /^Log ?in$|already have/i }), B4, { group: g, title: 'Login link', desc: 'The "Log in" link on the signup surface; measured, never followed.', sel: 'auth login link' }, { noScroll: true });
  save();
}

async function catalog() {
  if (!(await newPage('catalog'))) return;
  await sheetsFor('catalog');
  await chrome('catalog');
  const g = G.catalog;
  await S('cat-nav', q('header, nav, [class*="header"], [class*="navbar"]'), ['default'], { group: g, title: 'Catalogue nav', desc: 'The products.fourthwall.com top bar — logo, category tabs, search, Log in / Sign up.', sel: 'catalog header' }, { noScroll: true });
  // Header controls are measured before the search field: once the search
  // expands (focused/filled paint it 638px wide) the nav buttons re-render
  // and the locators go stale. Each control also exists several times in
  // the DOM (hydration swaps which duplicate is painted), so :visible keeps
  // the locator pinned to the painted copy across re-renders.
  await S('cat-login', q('a:visible, button:visible').filter({ hasText: /^Log ?in$/i }), ['default', 'hover'], { group: g, title: 'Log in action', desc: 'The "Log in" catalogue action; measured, never followed. Hydration swaps the nav copy roughly a minute after load, so focus/pressed states could not be captured reliably.', sel: 'catalog Log in' }, { noScroll: true });
  await S('cat-signup', q('a:visible, button:visible').filter({ hasText: /^Sign ?up$/i }), ['default', 'hover'], { group: g, title: 'Sign up action', desc: 'The "Sign up" catalogue action; measured, never followed. Focus/pressed states were not reliably measurable (hydration nav swap).', sel: 'catalog Sign up' }, { noScroll: true });
  await S('cat-tab', q('a:visible').filter({ hasText: /^All Products$|^Discover$|^Apparel$|^Accessories$|^Home & Living$/ }), ['default', 'hover'], { group: g, title: 'Category tab', desc: 'A category tab in the catalogue nav strip (Discover / All Products / Apparel…); measured, never followed. Focus/pressed states were not reliably measurable (hydration nav swap).', sel: 'catalog category tab' }, { noScroll: true });
  await S('cat-search', q('input[type="search"], input[placeholder*="earch"], input[aria-label*="earch"], input[type="text"]'), FIELD, { group: g, title: 'Catalogue search', desc: 'The catalogue search field — a bare input[type=text] in the nav; focused and typed into then cleared — a local filter, nothing sent.', sel: 'catalog search' }, { noScroll: true, fillText: 'hoodie' });
  await S('quiz-card', q('[class*="quiz"], [class*="Quiz"], section').filter({ hasText: /looking for|quiz|recommend/i }), ['default'], { group: g, title: 'Quiz card', desc: 'The "What are you looking for?" product-finder card on the catalogue home.', sel: 'catalog quiz card' });
  await S('quiz-option', q('button, [role="button"], a, li, label').filter({ hasText: /Premium quality|Budget-friendly|Streetwear|Accessories|Drinkware|Home & living/i }), B4, { group: g, title: 'Quiz option', desc: 'A product-finder answer chip; clicking selects it locally (the quiz needs more steps before recommending) — nothing is submitted.', sel: 'catalog quiz option' });
  await S('prod-card', q('a[href*="-dtg"], a[href*="t-shirt"], a[href*="/product"], a[class*="card"], [class*="ProductCard"]'), ['default', 'hover'], { group: g, title: 'Product card', desc: 'A catalogue product card (thumbnail, name, colour count, "From $" price); measured, never followed.', sel: 'catalog product card' });
  await S('prod-badge', q('span').filter({ hasText: /^(Best seller|Staff pick)$/ }), ['default'], { group: g, title: 'Product badge', desc: 'A "Best seller" / "Staff pick" badge on a product card.', sel: 'catalog badge' });
  // No cat-footer entry: the catalogue page mounts no footer element.
  save();
}

async function pdp() {
  if (!(await newPage('pdp'))) return;
  await sheetsFor('pdp');
  await chrome('pdp');
  const g = G.pdp;
  await S('pdp-h1', q('h1'), ['default'], { group: g, title: 'Product headline', desc: 'The PDP product title ("Comfort Colors Garment-Dyed Heavyweight T-Shirt").', sel: 'pdp h1' }, { noScroll: true });
  await S('pdp-badge', q('[class*="badge"], [class*="Badge"], span').filter({ hasText: /^Best seller$|^Staff pick$/ }), ['default'], { group: g, title: 'PDP badge', desc: 'The "Best seller" badge beside the title.', sel: 'pdp badge' });
  await S('pdp-swatch', q('[role="radio"], input[type="radio"], [class*="swatch"], [class*="Swatch"], [class*="color"] button, button[class=""], button:not([class])'), B4, { group: g, title: 'Colour swatch', desc: 'A colour swatch button on the PDP (classless styled-components swatch buttons); selecting one repaints the photo locally — measured, selection states only.', sel: 'pdp swatch' });
  // This PDP exposes no per-size selector or decoration picker — the sheet
  // shows a static "S–4XL" range label and a Size-guide toggle; sizes are
  // chosen inside the designer (behind sign-in). pdp-size measures the
  // range label; pdp-print is omitted as absent, not fabricated.
  await S('pdp-size', q('span, [class*="size"], [class*="Size"]').filter({ hasText: /^(XS|S|M|L|XL).{0,3}(XL|4XL|5XL)$/ }), ['default'], { group: g, title: 'Size-range label', desc: 'The static "S–4XL" size-range label — no per-size option exists on the public PDP.', sel: 'pdp size range' });
  await S('pdp-sizeguide-btn', q('button, [role="button"], a').filter({ hasText: /^Size guide$/i }), B4, { group: g, title: 'Size-guide button', desc: 'The "Size guide" control — a local dialog toggle.', sel: 'pdp Size guide' });
  await S('pdp-sizeguide', q('[role="dialog"], [class*="dialog"], [class*="modal"]'), ['default'], { group: g, title: 'Size-guide dialog', desc: 'The size-table dialog mounted by the Size-guide control; opened by its own toggle.', sel: 'pdp size dialog' }, { open: openSizeGuide, noScroll: true, noReset: true });
  await page.keyboard.press('Escape').catch(() => {});
  await S('pdp-price', q('[class*="price"], [class*="Price"], span').filter({ hasText: /^From \$|\$\d/ }), ['default'], { group: g, title: 'Price text', desc: 'The "From $15.45" price text.', sel: 'pdp price' });
  await S('pdp-design-cta', q('a, button').filter({ hasText: /Sign in to design|Start designing|Design now/i }), B4, { group: g, title: 'Sign-in-to-design CTA', desc: 'The "Sign in to design" action — it starts an auth flow; measured, never pressed.', sel: 'pdp Sign in to design' });
  await S('pdp-desc', await p20('p, [class*="description"]'), ['default'], { group: g, title: 'Product description', desc: 'The product description paragraph (materials, fit, print specs).', sel: 'pdp description' });
  // No pdp-faq entry: this PDP mounts no shipping/returns accordion.
  save();
}

async function docs() {
  if (!(await newPage('docs', { wait: 9000 }))) return;
  await sheetsFor('docs');
  await chrome('docs');
  const g = G.docs;
  await S('docs-nav', q('header, nav#navbar, .navbar, [class*="navbar"]'), ['default'], { group: g, title: 'Docs navbar', desc: 'The Mintlify top bar — logo, tabs, search and the theme menu.', sel: 'docs navbar' }, { noScroll: true });
  await S('docs-search', q('button[aria-label*="earch"], input[placeholder*="earch"], [class*="search"] button, button[class*="search"]'), B4, { group: g, title: 'Search trigger', desc: 'The docs search control — opens the cmdk dialog; states measured.', sel: 'docs search' }, { noScroll: true });
  await S('docs-search-dialog', q('[role="dialog"]:has(input[placeholder="Search..."]), [cmdk-root]:has(input), div[class]:has(> input[placeholder="Search..."])'), ['default'], { group: g, title: 'Search dialog', desc: 'The Mintlify search dialog; opened by its own search control, nothing sent.', sel: 'docs search dialog' }, { open: openDocsSearch, noScroll: true, noReset: true });
  await page.keyboard.press('Escape').catch(() => {});
  await S('docs-theme-btn', q('button[aria-label="Change theme preference"], button[aria-label*="theme preference" i]'), B4, { group: g, title: 'Theme menu button', desc: 'The "Change theme preference" button — the docs site\'s real Light/Dark/System menu; measured, the Dark choice is made only on the docsdark pass.', sel: 'docs theme button' }, { noScroll: true });
  await S('docs-sidebar', q('[class*="sidebar"], aside, nav[class*="side"]'), ['default'], { group: g, title: 'Docs sidebar', desc: 'The Mintlify sidebar nav tree.', sel: 'docs sidebar' });
  await S('docs-side-item', q('[class*="sidebar"] a, aside a').filter({ hasText: /Quickstart|Authentication|Overview/i }), B4, { group: g, title: 'Sidebar item', desc: 'A sidebar nav link; measured, never followed.', sel: 'docs sidebar link' });
  // The cards are Mintlify's div.card/a.card tiles — not the .columns grid
  // wrapper that holds them (a bare [class*="card"] matched the whole grid).
  await S('docs-card', q('.mdx-content .card, div.card, a.card').filter({ hasText: /API|Guide|Quickstart|Webhook/i }), ['default', 'hover'], { group: g, title: 'Docs card', desc: 'A .card tile on the docs landing page (Platform API / Webhooks / …); measured, never followed.', sel: 'docs .card' });
  save();
}

async function docsart() {
  if (!(await newPage('docsart', { wait: 9000 }))) return;
  const g = G.docs;
  await S('docs-h1', q('h1'), ['default'], { group: g, title: 'Article headline', desc: 'The docs article title (the /quickstart page).', sel: 'docs h1' }, { noScroll: true });
  await S('docs-prose', await p20('main p, article p, #content-area p'), ['default'], { group: g, title: 'Article body', desc: 'A body paragraph in a docs article.', sel: 'docs article p' });
  // The first <pre> in DOM can be an inline icon slot; tag the largest real
  // code block (anything taller than 60px) and measure that.
  await page.evaluate(() => { const ps = [...document.querySelectorAll('pre, [class*="code-block"]')].filter((e) => e.getBoundingClientRect().height > 60).sort((a, b) => b.getBoundingClientRect().height - a.getBoundingClientRect().height); if (ps[0]) ps[0].setAttribute('data-m-code', '1'); });
  await S('docs-code', q('[data-m-code="1"], pre'), ['default'], { group: g, title: 'Code block', desc: 'A fenced code block in a docs article.', sel: 'docs pre' });
  await S('docs-anchor', q('main a, article a, #content-area a').filter({ hasText: /\S/ }), B4, { group: g, title: 'Article link', desc: 'An in-content link inside a docs article; measured, never followed.', sel: 'docs article a' }, { pin: true });
  await S('docs-toc', q('[class*="toc"], [class*="table-of-contents"], nav[aria-label*="contents" i]'), ['default'], { group: g, title: 'On-this-page rail', desc: 'The right-hand table-of-contents rail.', sel: 'docs toc' });
  save();
}

async function docsdark() {
  if (!(await newPage('docsdark', { wait: 9000 }))) return;
  const g = G.docsdark;
  const via = await docsDarkOn();
  log('  docs dark toggle:', via);
  const dark = await page.evaluate(() => document.documentElement.classList.contains('dark')).catch(() => false);
  if (!dark) { log('  ! html.dark never painted; skipping dark measurements'); return; }
  await S('dd-page', q('main, #content-area, article'), ['default'], { group: g, title: 'Docs page (dark)', desc: 'The docs article surface under html.dark — reached through the site\'s own theme menu, not a reconstruction.', sel: 'docs main (dark)' }, { noScroll: true });
  await S('dd-h1', q('h1'), ['default'], { group: g, title: 'Article headline (dark)', desc: 'The article title under html.dark.', sel: 'docs h1 (dark)' }, { noScroll: true });
  await S('dd-nav', q('header, [class*="navbar"]'), ['default'], { group: g, title: 'Docs navbar (dark)', desc: 'The Mintlify navbar under html.dark.', sel: 'docs navbar (dark)' }, { noScroll: true });
  await S('dd-prose', await p20('main p, article p, #content-area p'), ['default'], { group: g, title: 'Article body (dark)', desc: 'A body paragraph under html.dark.', sel: 'docs article p (dark)' });
  await page.evaluate(() => { const ps = [...document.querySelectorAll('pre, [class*="code-block"]')].filter((e) => e.getBoundingClientRect().height > 60).sort((a, b) => b.getBoundingClientRect().height - a.getBoundingClientRect().height); if (ps[0]) ps[0].setAttribute('data-m-code', '1'); });
  await S('dd-code', q('[data-m-code="1"], pre'), ['default'], { group: g, title: 'Code block (dark)', desc: 'A code block under html.dark.', sel: 'docs pre (dark)' });
  await S('dd-card', q('main div.card, main a.card, div.card, a.card'), ['default'], { group: g, title: 'Docs card (dark)', desc: 'A docs card under html.dark.', sel: 'docs card (dark)' });
  save();
}

async function help() {
  if (!(await newPage('help', { wait: 9000 }))) return;
  await sheetsFor('help');
  await chrome('help');
  const g = G.help;
  await S('help-navbar', q('.navbar'), ['default'], { group: g, title: 'Help navbar', desc: 'The Docusaurus navbar — "Help center" wordmark, the ctrl-K search, the Fourthwall link and the colour-mode toggle.', sel: '.navbar' }, { noScroll: true });
  await S('help-search', q('.navbar input[type="search"], input[placeholder*="earch"], input[type="search"]'), FIELD, { group: g, title: 'Search field', desc: 'The help search field (ctrl-K hint); focused and typed into then cleared — a local filter, nothing sent.', sel: 'help search input' }, { noScroll: true, fillText: 'storefront' });
  await S('help-search-pop', q('[class*="dropdownMenu"], [class*="suggestions"], [class*="search-result"], [class*="SearchResult"], [class*="dropdown-menu"]'), ['default'], { group: g, title: 'Search results dropdown', desc: 'The local-search results dropdown the navbar search opens while typing.', sel: 'help search dropdown' }, { open: openHelpSearch, noScroll: true, noReset: true });
  await page.keyboard.press('Escape').catch(() => {});
  await S('help-theme', q('button[aria-label*="Switch between" i], [class*="colorModeToggle"] button, button[class*="toggleButton"], .navbar button[class*="toggle"]'), B4, { group: g, title: 'Colour-mode toggle', desc: 'The navbar colour-mode button — the help site\'s real dark toggle (data-theme); its states were measured but it was only switched on the helpdark pass.', sel: 'help theme toggle' }, { noScroll: true });
  await S('help-fw-link', q('.navbar a').filter({ hasText: /Fourthwall/ }), B4, { group: g, title: 'Fourthwall link', desc: 'The "Fourthwall ↗" navbar link back to the product; measured, never followed.', sel: 'help Fourthwall link' }, { noScroll: true });
  await S('help-card', q('a[class*="sectionLink"], a[href*="/category/"], [class*="card"], .card'), ['default', 'hover'], { group: g, title: 'Category link', desc: 'A category link row on the help landing list ("Setting up your shop", "Design my storefront", …); measured, never followed.', sel: 'help category link' });
  save();
}

async function helpcat() {
  if (!(await newPage('helpcat', { wait: 9000 }))) return;
  const g = G.help;
  await S('help-h1', q('h1, .docItemContainer h1, article h1'), ['default'], { group: g, title: 'Category headline', desc: 'The category page title ("Setting up your shop").', sel: 'help h1' }, { noScroll: true });
  await S('help-side-item', q('.menu__link, aside a, [class*="menu"] a'), B4, { group: g, title: 'Sidebar item', desc: 'A help sidebar menu link on the category page; measured, never followed.', sel: 'help sidebar link' });
  await S('help-doc-link', q('article a, [class*="docCard"] a, .card a, main a'), B4, { group: g, title: 'Article link', desc: 'An article link inside a help category; measured, never followed.', sel: 'help article link' }, { pin: true });
  await S('help-prose', await p20('main p, article p, [class*="docItemContainer"] p'), ['default'], { group: g, title: 'Category body', desc: 'A body paragraph on the help category page.', sel: 'help category p' });
  save();
}

async function helpdark() {
  if (!(await newPage('helpdark', { wait: 9000 }))) return;
  const g = G.helpdark;
  const via = await helpDarkOn();
  log('  help dark toggle:', via);
  const dark = await page.evaluate(() => document.documentElement.getAttribute('data-theme') === 'dark').catch(() => false);
  if (!dark) { log('  ! data-theme=dark never painted; skipping dark measurements'); return; }
  await S('hd-page', q('main, [class*="docPage"], article'), ['default'], { group: g, title: 'Help page (dark)', desc: 'The help category surface under data-theme=dark — reached through the site\'s own colour-mode toggle, not a reconstruction.', sel: 'help main (dark)' }, { noScroll: true });
  await S('hd-h1', q('h1'), ['default'], { group: g, title: 'Category headline (dark)', desc: 'The category title under data-theme=dark.', sel: 'help h1 (dark)' }, { noScroll: true });
  await S('hd-navbar', q('.navbar'), ['default'], { group: g, title: 'Help navbar (dark)', desc: 'The Docusaurus navbar under data-theme=dark.', sel: 'help navbar (dark)' }, { noScroll: true });
  await S('hd-search', q('.navbar input[type="search"], input[placeholder*="earch"], input[type="search"], .navbar input[type="text"]'), ['default'], { group: g, title: 'Search field (dark)', desc: 'The help search field under data-theme=dark.', sel: 'help search (dark)' }, { noScroll: true });
  await S('hd-card', q('a[href*="/category/"], [class*="card"], .card'), ['default'], { group: g, title: 'Category card (dark)', desc: 'A help category card under data-theme=dark.', sel: 'help card (dark)' });
  save();
}

async function mobile() {
  if (!(await newPage('mobile', { mobile: true, url: BASE + '/' }))) return;
  await chrome('mobile');
  const g = G.mobile;
  await S('m-nav', q('nav.nav-bar'), ['default'], { group: g, title: 'Mobile nav bar', desc: 'The phone nav bar: wordmark and menu toggle. The mobile Start-now variant keeps a box but paints nothing (visibility:hidden) — no mobile CTA exists at rest.', sel: 'mobile nav.nav-bar' }, { noScroll: true });
  await S('m-menu-btn', q('.nav-bar button, .nav-bar [class*="hamburger"], .nav-bar .w-nav-button, .nav-bar [role="button"]'), B4, { group: g, title: 'Menu toggle', desc: 'The mobile menu toggle; measured, never used to navigate.', sel: 'mobile menu button' }, { noScroll: true });
  // No m-cta entry: the mobile Start-now anchor is visibility:hidden at rest
  // (nonzero box, nothing painted), so there is no mobile CTA to measure.
  await S('m-hero-h1', q('h1'), ['default'], { group: g, title: 'Mobile hero headline', desc: 'The masthead at 390 wide.', sel: 'mobile h1' });
  save();
}

run = new Date().toISOString().slice(0, 10);
out._meta.read = run;
out._meta.viewport = '1440 x 900 (mobile group 390 x 844); fourthwall.com paints one light surface with scoped on-ink dark sections (no user toggle); products.fourthwall.com + /get-started paint the catalogue DS light; docs.fourthwall.com paints dark via its own theme menu (the docsdark group); help.fourthwall.com paints dark via its own colour-mode toggle (the helpdark group)';
out._meta.tool = 'tools/capture/public/measure.mjs';
const { browser, context: ctx0 } = await launch();
context = ctx0;
const pages = process.argv.slice(2);
const plan = { home, pricing, blog, compare, cmparticle, shops, inspired, contact, signup, catalog, pdp, docs, docsart, docsdark, help, helpcat, helpdark, mobile };
const order = Object.keys(plan).filter((k) => !pages.length || pages.includes(k));
const finishedPages = new Set();
try {
  for (const k of order) { if (k !== 'mobile') { await plan[k](); finishedPages.add(k); } }
  if (!pages.length || pages.includes('mobile')) { await plan.mobile(); finishedPages.add('mobile'); }
  // Reduced-motion check on an element that transitions (the nav CTA's
  // hover), so the delta is meaningful.
  if (!pages.length || pages.includes('home')) await reducedMotion('home', '.nav-bar a, .nav-bar button');
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
