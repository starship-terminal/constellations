// Measures frame.io's public components in every state reachable without
// signing in or submitting anything.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node measure.mjs [page ...]
//
// Pages: home pricing contact contactform welcome customers casestudy
//        integrations whatsnew mobile.
// Writes raw/components-computed.json (merged) and one crop per component and
// state into components/crops/; raw/measurements.md is built by
// build-measurements.mjs.
//
// frame.io is two public stacks signed out. Every frame.io page is the same
// Next.js + CSS-modules site painted in the one dark theme (ink #fcfcfc on
// near-black); accounts.frame.io/welcome is the sign-in surface, a light
// styled-components page on a different stack. Classes are <File>_<name>__hash,
// so specs select by role, aria-label, the stable class part
// ([class*="navigationMainItem"]) or text. Nothing is sent, bought or signed
// into: the only presses are local UI toggles — the header's mega-menu
// triggers, the pricing accordions, the mobile nav button. Fields stay
// empty: nothing is typed. Schedule a
// Meeting, Talk with Sales, Sign Up Now, Start Free Trial, Let's go and every
// CTA are measured, never followed or clicked. The announcement banner is
// real chrome, never hidden; any consent overlay would be hidden, never
// answered.
import fs from 'node:fs';
import path from 'node:path';
import { BASE, LOGIN_URL, M, launch, patch, open, closePromo, domFind, styleOf, crop, centre, RAW, UA, UA_MOBILE } from './lib.mjs';

const OUT = process.env.OUT_JSON || path.join(RAW, 'components-computed.json');
const out = fs.existsSync(OUT) ? JSON.parse(fs.readFileSync(OUT, 'utf8')) : {};
out._meta ??= {};
out.components ??= {};
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const save = () => fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');
const URLS = { home: '/', pricing: '/pricing', contact: '/contact', contactform: '/contact/form', welcome: LOGIN_URL, customers: '/customers', casestudy: '/case-studies/ford', integrations: '/integrations', whatsnew: '/whats-new', mobile: '/' };
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
  // A fresh reading clears the marker a previous missed pass left; a new
  // miss re-records it below.
  delete out.components[key].recaptureMissed;
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
        const pl = (opts.pressLoc || loc).filter({ visible: true }).first();
        // The forced pseudo-state still paints through the element's own
        // transition, so listen for the transition itself: getComputedStyle
        // sampling is unreliable here (a fixed delay caught mid-fade values —
        // a Button_white press read as alpha 0.35 / mid-grey text instead of
        // the settled transparent + #fcfcfc — and the headless compositor can
        // hold a mid-flight value level across several polls). Attach the
        // listener before forcing so no transitionrun is missed; a pressed
        // style identical to default starts no transition and resolves at
        // the first timeout.
        const settled = pl.evaluate((el) => new Promise((resolve) => {
          let started = false, finished = false, quiet = 0;
          const fin = (v) => {
            if (finished) return;
            finished = true;
            el.removeEventListener('transitionrun', ping);
            el.removeEventListener('transitionstart', ping);
            el.removeEventListener('transitionend', ping);
            el.removeEventListener('transitioncancel', ping);
            resolve(v);
          };
          // Every transition event re-arms a 300ms quiet window; when the
          // stream stops, the fade is done. Stray ends from animations that
          // were already running only ever stretch the window, never finish
          // early — pending-counting would let one fake a settle.
          const ping = () => {
            started = true;
            clearTimeout(quiet);
            clearTimeout(endCap);
            endCap = setTimeout(() => fin('end-timeout'), 8000);
            quiet = setTimeout(() => fin('settled'), 300);
          };
          el.addEventListener('transitionrun', ping);
          el.addEventListener('transitionstart', ping);
          el.addEventListener('transitionend', ping);
          el.addEventListener('transitioncancel', ping);
          let endCap = 0;
          const noStart = setTimeout(() => { if (!started) fin('no-transition'); }, 2500);
        }));
        undo = await forcePseudo(pl, ['active', 'hover']);
        await settled;
        await page.waitForTimeout(120);
        via = 'CDP forcePseudoState :active:hover';
      } else if (st === 'focused') {
        const fld = (opts.fieldLoc || loc).filter({ visible: true }).first();
        await fld.click({ timeout: 4000 }).catch(() => fld.evaluate((el) => el.focus()));
        await page.waitForTimeout(400);
        via = 'clicked into the field';
      } else if (st === 'filled') {
        // Public capture does not type into email, name, password, or message fields.
        throw new Error('filled is not captured: typing into a form is refused');
      } else if (st === 'opened') {
        if (opts.noToggle) via = 'held open by an earlier toggle';
        else {
          await toggle(loc, { allowLink: opts.allowLink });
          await page.waitForTimeout(900);
          // A collapsible that reports expansion must still be open when its
          // "opened" reading is taken; a control without the attribute is
          // trusted (some toggles expose no state).
          const expanded = await loc.evaluate((el) => el.getAttribute('aria-expanded')).catch(() => null);
          if (expanded === 'false') throw new Error('the opened state measured closed (aria-expanded="false" after the toggle)');
          via = 'own toggle';
        }
      } else if (st === 'closed') {
        await toggle(loc, { allowLink: opts.allowLink }); await page.waitForTimeout(900); via = 'own toggle';
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

// Clicks a UI toggle (dropdown, menu, accordion, sheet trigger). Refuses a
// submit button and any control whose text names an action this kit must
// never take.
const NEVER = /^(send|send message|submit|sign in|log ?in|login|sign up|create|add|download|buy|purchase|pay|checkout|join|subscribe|save|apply|accept|reject|start|get started|get started for free|claim|share|export|select|continue|continue with.*|claim this offer|try again)$/i;
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
async function reducedMotion(key, sel) {
  out._meta.reducedMotion ??= {};
  try {
    const b = context.browser();
    const ctx = await b.newContext({ viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1, userAgent: UA, locale: 'en-US', reducedMotion: 'reduce' });
    await patch(ctx);
    const p = await ctx.newPage();
    await p.goto(URLS[key].startsWith('http') ? URLS[key] : BASE + URLS[key], { waitUntil: 'domcontentloaded', timeout: 90000 }).catch(() => {});
    await p.waitForTimeout(8000);
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
  shell: 'Site chrome (header, announcement, nav, footer)', home: 'Home',
  pricing: 'Pricing', contact: 'Contact', contactForm: 'Contact form',
  auth: 'Sign-in surface (accounts.frame.io — a different stack)',
  gallery: 'Customers, case study, integrations, what\'s new',
  mobile: 'Mobile (390 wide)',
};

// Opens one of the header's mega-menu overlays: a
// button[class*="navigationMainItem"] ("Features"/"Enterprise"/"Resources")
// whose group's NavGroup_open__ class flips on a pointer click (hovering does
// nothing — verified 2026-11; the nav gains Navigation_subNavOpen__). Enter
// is the fallback. Links inside are never followed; Escape closes.
async function openMegaMenu(name) {
  const btn = await domFind(page, new RegExp(`^${name}$`), { sel: 'nav[class*="mainNavigation"] button[class*="navigationMainItem"]', tag: 'navtrg', minW: 40, minH: 20 });
  if (!(await btn.count())) return 'no ' + name + ' trigger';
  const open = async () => page.evaluate(() => !!document.querySelector('[class*="subNavOpen"], [class*="NavGroup_open"]')).catch(() => false);
  if (await open()) return 'the ' + name + ' menu was already open';
  for (let i = 0; i < 3; i++) {
    await btn.click({ timeout: 4000 }).catch(() => {});
    await page.waitForTimeout(900);
    if (await open()) return 'clicked the "' + name + '" trigger to open the mega-menu';
    await btn.focus(); await page.keyboard.press('Enter'); await page.waitForTimeout(900);
    if (await open()) return 'focused the "' + name + '" trigger and pressed Enter to open the mega-menu';
  }
  return 'activated "' + name + '"; the menu did not report open';
}

// Opens the pricing page's collapsed feature-comparison table: the
// "View all Features" control is a local UI toggle (it expands the section in
// place; nothing is submitted and no link is followed).
async function openFeatureTable() {
  const btn = await domFind(page, /view all features/i, { sel: 'button, a', tag: 'featbtn', minW: 60, minH: 15 });
  if (!(await btn.count())) return 'no "View all Features" control';
  const open = () => page.evaluate(() => [...document.querySelectorAll('button[class*="categoryTitle" i]')].some((e) => e.getBoundingClientRect().width > 10)).catch(() => false);
  if (await open()) return 'the comparison table was already expanded';
  for (let i = 0; i < 3; i++) {
    await btn.scrollIntoViewIfNeeded().catch(() => {});
    await btn.click({ timeout: 4000 }).catch(() => btn.evaluate((el) => el.click()));
    await page.waitForTimeout(1200);
    if (await open()) return 'clicked "View all Features" to expand the comparison table';
  }
  return 'activated "View all Features"; the table stayed collapsed';
}

// Opens the phone's nav overlay: the "Toggle mobile navigation" button
// (ToggleButton_navMobileButton) — a local UI toggle.
async function openMobileMenu() {
  const b = page.locator('button[class*="navMobileButton"], button[aria-label*="navigation" i], button[aria-label*="menu" i]').filter({ visible: true }).first();
  if (!(await b.count())) return 'no menu toggle';
  const open = () => page.evaluate(() => !!document.querySelector('[class*="subNavOpen"], [class*="mobileMenuOpen" i], [class*="navOpen" i]')).catch(() => false);
  if (await open()) return 'the nav overlay was already open';
  for (let i = 0; i < 3; i++) {
    await b.click({ timeout: 4000 }).catch(() => b.evaluate((el) => el.click()));
    await page.waitForTimeout(1000);
    if (await open()) return 'clicked "Toggle mobile navigation" to open the nav overlay';
    await b.focus(); await page.keyboard.press('Enter'); await page.waitForTimeout(1000);
    if (await open()) return 'focused the menu button and pressed Enter to open the nav overlay';
  }
  return 'activated the menu button; the overlay did not report open';
}

const FIELD = ['default', 'focused'];

async function home() {
  if (!(await newPage('home'))) return;
  await sheetsFor('home');
  await chrome('home');
  const g = G.shell;
  await S('mkt-header', q('nav[class*="mainNavigation"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Site header', desc: 'The fixed top bar on every public page (header is a 0-height sentinel; the painted bar is nav.mainNavigation, 80px under the 36px announcement strip): the Frame.io mark, the Features/Enterprise/Resources mega-menu triggers, Pricing, Contact Us, Sign In and the "Start Free Trial" pill.', sel: 'nav[class*=mainNavigation]' }, { noScroll: true });
  await S('page-field', q('html'), ['default'], { group: g, title: 'Page field', desc: 'The near-black field the whole public site paints (the html background layer; body is transparent over it).', sel: 'html' }, { noScroll: true, crop: false });
  await S('mkt-logo', q('nav[class*="mainNavigation"] a[href="/"], nav[class*="mainNavigation"] a[href="https://frame.io/"], nav[class*="mainNavigation"] a[href="https://frame.io"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Logo', desc: 'The Frame.io waveform mark in the header, linking home.', sel: 'mainNavigation a[href=/]' }, { noScroll: true });
  await S('announcement', q('[class*="AnnouncementBanner"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Announcement banner', desc: 'The site-wide promo strip above the header ("Put your creative context to work with new AI-powered capabilities →") — real chrome, never hidden.', sel: '[class*=AnnouncementBanner]' }, { noScroll: true });
  await S('nav-trigger', await domFind(page, /^Features$/, { sel: 'nav[class*="mainNavigation"] button[class*="navigationMainItem"]', minW: 40, minH: 20 }), [...B4, 'opened'], { group: g, title: 'Mega-menu trigger', desc: 'The "Features" header button — click opens the mega-menu (the group gains NavGroup_open__ and the nav Navigation_subNavOpen__; hovering does not open it). The opened state was measured after its own toggle click.', sel: 'button[class*=navigationMainItem] Features' }, { noScroll: true, allowLink: true });
  await S('nav-panel', q('[data-m-mark="navpanel"]'), ['default'], { group: g, title: 'Mega-menu panel', desc: 'The Features mega-menu opened by its trigger (Workflow Management, File Management, Share & Present, Review & Approvals, Camera to Cloud, Integrations, Mounted Storage, Frame.io Drive); its links were never followed.', sel: '[class*=navGroupSubnav] open' }, { open: async () => { await openMegaMenu('Features'); await domFind(page, /\S/, { sel: '[class*="NavGroup_open"] [class*="navGroupSubnav"]', tag: 'navpanel', minW: 500, minH: 100, leaf: false }); }, noScroll: true, noReset: true });
  await S('nav-menu-item', q('[data-m-mark="navmi"]'), ['default', 'hover'], { group: g, title: 'Mega-menu item', desc: 'A destination row inside the opened mega-menu; measured, never followed.', sel: 'mega-menu item' }, { open: async () => { await openMegaMenu('Features'); await domFind(page, /Workflow Management/, { sel: '[class*="NavGroup_open"] [class*="navGroupSubnav"] a', tag: 'navmi', minW: 100, minH: 20 }); }, noScroll: true, noReset: true });
  await page.keyboard.press('Escape').catch(() => {});
  await S('nav-pricing', await domFind(page, /^Pricing$/, { sel: 'nav[class*="mainNavigation"] a', minW: 30, minH: 10 }), B4, { group: g, title: 'Nav link', desc: 'The "Pricing" header link; measured, never followed.', sel: 'header a Pricing' }, { noScroll: true });
  await S('nav-contact', await domFind(page, /^Contact Us$/, { sel: 'nav[class*="mainNavigation"] a', minW: 40, minH: 10 }), B4, { group: g, title: 'Contact Us link', desc: 'The "Contact Us" header link; measured, never followed.', sel: 'header a Contact Us' }, { noScroll: true });
  await S('nav-signin', await domFind(page, /^Sign In$/, { sel: 'nav[class*="mainNavigation"] a', minW: 30, minH: 10 }), B4, { group: g, title: 'Sign In link', desc: 'The "Sign In" header link to app.frame.io (which redirects to the accounts.frame.io/welcome sign-in surface); measured, never followed.', sel: 'header a Sign In' }, { noScroll: true });
  await S('nav-cta', await domFind(page, /^Start Free Trial$/, { sel: 'nav[class*="mainNavigation"] a', minW: 80, minH: 20 }), B4, { group: g, title: 'Header CTA', desc: 'The white "Start Free Trial" header pill; links to the trial sign-up, measured never followed.', sel: 'header a Start Free Trial' }, { noScroll: true });
  const h = G.home;
  await S('hero-h1', await domFind(page, /\S/, { sel: 'h1', tag: 'h1', minW: 200, minH: 20 }), ['default'], { group: h, title: 'Hero headline', desc: '"One platform for all your creative work." — the frame.io hero display heading in FrameGothic 80px.', sel: 'h1' }, { noScroll: true });
  await S('hero-cta', q('main a, main button').filter({ hasText: /^Start Free Trial$/ }).filter({ visible: true }).first(), B4, { group: h, title: 'Hero CTA', desc: 'The hero "Start Free Trial" button; measured, never followed.', sel: 'main Start Free Trial' });
  await S('hero-tour', q('main a, main button').filter({ hasText: /Take a Product Tour/i }).filter({ visible: true }).first(), B4, { group: h, title: 'Hero secondary action', desc: 'The hero "Take a Product Tour" ghost button; measured, never followed.', sel: 'main Take a Product Tour' });
  await S('section-h2', await domFind(page, /\S/, { sel: 'main h2', minW: 100, minH: 20 }), ['default'], { group: h, title: 'Section headline', desc: 'A section heading on the home page; first visible h2.', sel: 'h2' });
  const f = G.shell;
  await S('footer', q('footer').filter({ visible: true }).first(), ['default'], { group: f, title: 'Site footer', desc: 'The dark footer on every public page: link columns, legal row, "Cookie preferences" and the language selector.', sel: 'footer' });
  await S('footer-link', q('footer a').filter({ hasText: /Privacy|Terms|Support/i }).filter({ visible: true }).first(), ['default', 'hover'], { group: f, title: 'Footer link', desc: 'A legal/support link in the footer; measured, never followed.', sel: 'footer a' });
  await S('locale-btn', q('button[class*="LanguageSelector"], button').filter({ hasText: /^English/i }).filter({ visible: true }).first(), B4, { group: f, title: 'Language selector', desc: 'The "English (US)" footer trigger (LanguageSelector_trigger); measured at rest, never opened.', sel: 'footer English (US)' });
  await S('cookie-prefs', q('footer button, footer a').filter({ hasText: /^Cookie preferences$/ }).filter({ visible: true }).first(), B4, { group: f, title: 'Cookie preferences', desc: 'The footer "Cookie preferences" button, which mounts the consent manager on demand; measured at rest, never pressed.', sel: 'footer Cookie preferences' });
  save();
}

async function pricing() {
  if (!(await newPage('pricing'))) return;
  await sheetsFor('pricing');
  await chrome('pricing');
  const g = G.pricing;
  await S('price-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Pricing headline', desc: 'The /pricing masthead.', sel: 'h1' }, { noScroll: true });
  await S('price-toggle', q('[role="radio"], button').filter({ hasText: /^Monthly$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Billing toggle', desc: 'The "Monthly" side of the Monthly/Annually billing switch — a pair of round radio controls (a 24px circle ringed grey-60, a 10px turquoise-triumph dot on the selected side), not a segmented pill; a local UI toggle, measured at rest — the alternate price state was not toggled.', sel: 'billing Monthly control' }, { noScroll: true });
  await S('price-toggle-alt', q('[role="radio"], button').filter({ hasText: /Annually/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Billing toggle (annual)', desc: 'The "Annually — SAVE 13%" side of the billing switch — the same round radio control, measured at rest, never toggled.', sel: 'billing Annually control' }, { noScroll: true });
  await S('plan-card', await domFind(page, /\S/, { sel: '[class*="PricingCard_pricingCard__"]', tag: 'plancard', minW: 150, minH: 300, leaf: false }), ['default'], { group: g, title: 'Plan card', desc: 'A pricing plan card (Free / Pro / Team / Enterprise, $0–$25 monthly); the card wrapping a "Sign Up Now" CTA.', sel: '[class*=PricingCard_pricingCard__]' });
  await S('plan-signup', q('main a, main button').filter({ hasText: /^Sign Up Now$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Plan CTA', desc: 'A plan card\'s "Sign Up Now" button; measured, never followed or clicked (it begins account creation).', sel: 'plan Sign Up Now' });
  await S('plan-trial', q('main a, main button').filter({ hasText: /^Start Free Trial$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Plan trial CTA', desc: 'A plan card\'s "Start Free Trial" button; measured, never followed.', sel: 'plan Start Free Trial' });
  await S('plan-meeting', q('main a, main button').filter({ hasText: /Book a Meeting/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Plan meeting CTA', desc: 'The Enterprise card\'s "Book a Meeting" button; measured, never followed.', sel: 'plan Book a Meeting' });
  await S('ptable-acc', q('[data-m-mark="ptacc"]'), ['default', 'closed'], { group: g, title: 'Feature-comparison accordion', desc: 'A category row in the feature-comparison table (Users, Storage, Projects & workspaces, Feedback & collaboration, … — the rows mount expanded); the closed state was measured after clicking the row — a local UI toggle.', sel: 'comparison category accordion' }, { open: async () => { await openFeatureTable(); await domFind(page, /^(Users|Storage)$/, { sel: 'button[class*="categoryTitle" i]', tag: 'ptacc', minW: 200, minH: 15 }); }, noScroll: true, noReset: true });
  await S('faq-acc', q('button[class*="FaqItem"], button').filter({ hasText: /How do monthly and annual pricing differ/i }).filter({ visible: true }).first(), ['default', 'opened'], { group: g, title: 'FAQ accordion', desc: 'A question row in the pricing FAQ; the opened state was measured after clicking it — a local UI toggle.', sel: 'pricing FAQ accordion' });
  save();
}

async function contact() {
  if (!(await newPage('contact'))) return;
  await sheetsFor('contact');
  await chrome('contact');
  const g = G.contact;
  await S('contact-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Contact headline', desc: '"Hello, how can we help you?" — the /contact hub.', sel: 'h1' }, { noScroll: true });
  await S('schedule-btn', q('main a, main button').filter({ hasText: /Schedule a Meeting/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Schedule a Meeting', desc: 'The white "Schedule a Meeting" button on /contact (it mounts a Calendly scheduler — a vendor widget, never opened); measured, never pressed.', sel: 'contact Schedule a Meeting' }, { noScroll: true });
  await S('sales-link', q('a, button, [role="link"]').filter({ hasText: /Talk with Sales/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Talk with Sales', desc: 'The "Talk with Sales" text-link button on /contact (leads to /contact/form); measured, never followed.', sel: 'contact Talk with Sales' }, { noScroll: true });
  save();
}

async function contactform() {
  if (!(await newPage('contactform'))) return;
  await sheetsFor('contactform');
  await chrome('contactform');
  const g = G.contactForm;
  await S('form-panel', q('form, [class*="ContactForm"], main').filter({ visible: true }).first(), ['default'], { group: g, title: 'Contact form card', desc: 'The dark form card on /contact/form — "Enter your info below. We\'ll get back to you shortly." with Name/Email/Message fields and a Submit pill; never submitted.', sel: 'contact form' });
  await S('form-name', q('form input[type="text"], [class*="ContactForm"] input[type="text"], input[type="text"]').filter({ visible: true }).first(), FIELD, { group: g, title: 'Name field', desc: 'The underlined "Name" input, photographed empty. Focus lands in the field. Nothing is typed.', sel: 'contact Name input' });
  await S('form-email', q('form input[type="email"], input[type="email"]').filter({ visible: true }).first(), FIELD, { group: g, title: 'Email field', desc: 'The underlined "Email" input, photographed empty. Focus lands in the field. Nothing is typed.', sel: 'contact Email input' });
  await S('form-message', q('form textarea, form input[type="text"], textarea').filter({ visible: true }).last(), FIELD, { group: g, title: 'Message field', desc: 'The underlined "Message" input, photographed empty. Focus lands in the field. Nothing is typed.', sel: 'contact Message input' });
  await S('form-submit', q('form button[type="submit"], button[type="submit"]').filter({ hasText: /Submit/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Submit', desc: 'The form\'s pill "Submit" button; its states were measured but the button was never clicked — nothing was sent.', sel: 'contact Submit' });
  save();
}

async function welcome() {
  if (!(await newPage('welcome', { wait: 10000 }))) return;
  await sheetsFor('welcome');
  await chrome('welcome');
  const g = G.auth;
  await S('login-panel', q('form').filter({ visible: true }).first(), ['default'], { group: g, title: 'Sign-in panel', desc: 'The accounts.frame.io/welcome sign-in card — the Frame.io mark, "Welcome / Enter your email to get started.", an e-mail field and a "Let\'s go" submit on a light page (styled-components — a different stack from the marketing site); never submitted.', sel: 'welcome form' }, { noScroll: true });
  await S('login-email', q('input[type="email"], input[name="email"]').filter({ visible: true }).first(), FIELD, { group: g, title: 'Email field (sign-in)', desc: 'The "Email" input with placeholder "you@example.com", photographed empty. Focus lands in the field. Nothing is typed.', sel: 'welcome input[type=email]' }, { noScroll: true });
  await S('login-submit', q('button[type="submit"], button').filter({ hasText: /Let.s go/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Let\'s go submit', desc: 'The cobalt "Let\'s go" submit; its states were measured but the button was never clicked — nothing was submitted.', sel: 'welcome Lets go' }, { noScroll: true });
  save();
}

async function customers() {
  if (!(await newPage('customers'))) return;
  await sheetsFor('customers');
  await chrome('customers');
  const g = G.gallery;
  await S('cust-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Customers headline', desc: 'The /customers masthead.', sel: 'h1' }, { noScroll: true });
  await S('cust-card', q('main a[href*="case-studies"], main [class*="card" i]').filter({ visible: true }).first(), ['default', 'hover'], { group: g, title: 'Customer card', desc: 'A customer-story card on /customers; measured, never followed.', sel: 'customer card' });
  save();
}

async function casestudy() {
  if (!(await newPage('casestudy'))) return;
  await sheetsFor('casestudy');
  await chrome('casestudy');
  const g = G.gallery;
  await S('cs-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Case-study headline', desc: 'The masthead of a published case study (Ford); published editorial content, measured at rest.', sel: 'h1' }, { noScroll: true });
  save();
}

async function integrations() {
  if (!(await newPage('integrations'))) return;
  await sheetsFor('integrations');
  await chrome('integrations');
  const g = G.gallery;
  await S('int-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Integrations headline', desc: 'The /integrations masthead.', sel: 'h1' }, { noScroll: true });
  await S('int-card', await domFind(page, /\S/, { sel: '[class*="tileItem" i]', tag: 'intcard', minW: 100, minH: 40 }), ['default', 'hover'], { group: g, title: 'Integration card', desc: 'An integration card on /integrations; measured, never followed.', sel: '[class*=tileItem]' });
  save();
}

async function whatsnew() {
  if (!(await newPage('whatsnew'))) return;
  await sheetsFor('whatsnew');
  await chrome('whatsnew');
  const g = G.gallery;
  await S('wn-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'What\'s New headline', desc: 'The /whats-new release-notes index masthead.', sel: 'h1' }, { noScroll: true });
  await S('wn-card', q('a[class*="CardGridEditorial_card__"]').filter({ visible: true }).first(), ['default', 'hover'], { group: g, title: 'Release card', desc: 'A release-note card on /whats-new; measured, never followed.', sel: 'whats-new card' });
  save();
}

async function mobile() {
  if (!(await newPage('mobile', { mobile: true, url: BASE + '/' }))) return;
  await chrome('mobile');
  const g = G.mobile;
  await S('m-topbar', q('header [class*="navigationWrapper"], nav[class*="mainNavigation"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile top bar', desc: 'The phone header at 390 wide: the Frame.io mark, "Start Free Trial" and the nav button.', sel: 'mobile header' }, { noScroll: true });
  await S('m-cta', q('[class*="NavMobile"] a[href*="accounts.frame.io"], [class*="navMobile"] a[href*="accounts.frame.io"]').filter({ visible: true }).first(), ['default', 'focus-visible', 'pressed'], { group: g, title: 'Drawer CTA', desc: 'The nav overlay\'s white "Start Free Trial" pill at 390 wide — the closed top bar carries none (mark, Sign In and the menu button only); measured with the drawer open, never followed.', sel: 'mobile drawer Start Free Trial' }, { noScroll: true, open: openMobileMenu });
  const ham = q('button[class*="navMobileButton"], button[aria-label*="navigation" i], button[aria-label*="menu" i]').filter({ visible: true }).first();
  await S('m-menu-btn', ham, [...B4, 'opened'], { group: g, title: 'Mobile menu button', desc: 'The "Toggle mobile navigation" button — a local UI toggle; the opened state was measured after activating it.', sel: 'mobile nav toggle' }, { noScroll: true, allowLink: true });
  await S('m-drawer', q('[class*="navMobileMenu"] [class*="navGroupSubnav"], [class*="navMobileMenu"] ul, [class*="NavMobile"] [class*="navGroupSubnav"], [class*="NavMobile"] ul').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile nav overlay', desc: 'The nav list inside the overlay opened by the menu button; its links were never followed.', sel: 'mobile nav overlay' }, { open: openMobileMenu, noScroll: true, noReset: true });
  await page.keyboard.press('Escape').catch(() => {});
  await S('m-hero-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile hero headline', desc: 'The masthead at 390 wide.', sel: 'mobile h1' });
  await S('m-hero-cta', q('main a, main button').filter({ hasText: /^Start Free Trial$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Mobile hero CTA', desc: 'The hero "Start Free Trial" button at 390 wide; measured never followed.', sel: 'mobile hero Start Free Trial' });
  save();
}

run = new Date().toISOString().slice(0, 10);
out._meta.read = run;
out._meta.viewport = '1440 x 900 (mobile group 390 x 844); every public frame.io page paints the one dark theme (ink #fcfcfc on near-black — the site ships no theme switch); accounts.frame.io/welcome is the sign-in surface, a light styled-components page on a different stack';
out._meta.tool = 'tools/capture/public/measure.mjs';
const { browser, context: ctx0 } = await launch();
context = ctx0;
const pages = process.argv.slice(2);
const plan = { home, pricing, contact, contactform, welcome, customers, casestudy, integrations, whatsnew, mobile };
const order = Object.keys(plan).filter((k) => !pages.length || pages.includes(k));
const finishedPages = new Set();
try {
  for (const k of order) { if (k !== 'mobile') { await plan[k](); finishedPages.add(k); } }
  if (!pages.length || pages.includes('mobile')) { await plan.mobile(); finishedPages.add('mobile'); }
  // Reduced-motion check on an element that transitions (the header CTA's
  // hover), so the delta is meaningful.
  if (!pages.length || pages.includes('home')) await reducedMotion('home', 'header a[class*="Button"], [class*="navigationMainItem"]');
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
