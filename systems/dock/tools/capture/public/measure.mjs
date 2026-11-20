// Measures dock.us's public components in every state reachable without
// signing in, buying or submitting anything.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node measure.mjs [page ...]
//
// Pages: home pricing customers templates demo auth mobile.
// Writes raw/components-computed.json (merged) and one crop per component and
// state into components/crops/; raw/measurements.md is built by
// build-measurements.mjs.
//
// dock.us is a Webflow marketing site (a declared --ds-*/--color-*/--_anchor---*
// token layer; the header menus are <details>/<summary> toggles) plus the
// auth app on auth.dock.us (Next.js/Chakra). The product workspace sits
// behind the auth flow; the login/sign-up cards are public surfaces and are
// measured as such, never filled or submitted. Nothing is sent, bought or
// signed into: the only presses are local UI toggles — the Product
// nav dropdown, a pricing FAQ <details>, the customer-category radio
// filters, the mobile menu, and the fields' own focus. Any consent or chat
// overlay is hidden, never answered.
import fs from 'node:fs';
import path from 'node:path';
import { BASE, M, launch, patch, open, closePromo, domFind, styleOf, crop, centre, RAW, UA, UA_MOBILE } from './lib.mjs';

const OUT = process.env.OUT_JSON || path.join(RAW, 'components-computed.json');
const out = fs.existsSync(OUT) ? JSON.parse(fs.readFileSync(OUT, 'utf8')) : {};
out._meta ??= {};
out.components ??= {};
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const save = () => fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');
const URLS = {
  home: 'https://dock.us/', pricing: 'https://dock.us/pricing',
  customers: 'https://dock.us/customers', templates: 'https://dock.us/templates',
  demo: 'https://dock.us/demo', login: 'https://auth.dock.us/login', signup: 'https://auth.dock.us/sign-up',
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
  const cleared = await open(page, url || URLS[key], { wait, promo });  // false: the bot check did not clear (lib.mjs)
  if (!cleared || (await blocked())) { log('  BLOCKED', key); failedPages.add(key); await page.close(); await ctx.close(); return false; }
  await page.addStyleTag({ content: '*{caret-color:transparent!important}' });
  return true;
}

// Fixed/sticky chrome with paint order: the z-index map of the page's bars and
// overlays. Recorded per page into _meta.chrome.
async function chrome(key) {
  const z = await page.evaluate(() => {
    // Walk shadow roots too: dock-site-header's fixed header bar is inside
    // its shadow DOM, invisible to a plain querySelectorAll('body *').
    const els = [];
    const walk = (root) => {
      for (const el of root.querySelectorAll('*')) {
        els.push(el);
        if (el.shadowRoot) walk(el.shadowRoot);
      }
    };
    walk(document.body);
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
  // A control inside a shadow root (the dock-site-header/footer web
  // components) never lands on document.activeElement — that reads the
  // shadow host. :focus and :focus-within are evaluated on the element in
  // its own root, so they see focus wherever it actually landed.
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

let markSeq = 0;
async function forcePseudo(loc, classes) {
  // Each call stamps a unique mark: the header lives inside dock-site-header's
  // shadow root, where the light-DOM cleanup pass cannot reach, so a plain
  // shared attribute would leave stale marks behind.
  const mark = `m${++markSeq}`;
  await loc.evaluate((el, m) => el.setAttribute('data-m-force', m), mark);
  // Dock's header is a <dock-site-header> web component with a shadow root;
  // DOM.querySelector on the document does not reach inside it, so the marked
  // node is searched across the pierced document and every shadow root.
  const { root } = await cdp.send('DOM.getDocument', { depth: -1, pierce: true });
  const roots = [root.nodeId];
  const stack = [root];
  while (stack.length) {
    const n = stack.pop();
    if (n.shadowRoots) for (const sr of n.shadowRoots) { roots.push(sr.nodeId); stack.push(sr); }
    if (n.children) stack.push(...n.children);
    // Frame documents are roots of their own (the demo form's fields live
    // inside the cross-origin HubSpot iframe).
    if (n.contentDocument) { roots.push(n.contentDocument.nodeId); stack.push(n.contentDocument); }
  }
  let nodeId;
  for (const id of roots) {
    try {
      const r = await cdp.send('DOM.querySelector', { nodeId: id, selector: `[data-m-force="${mark}"]` });
      if (r.nodeId) { nodeId = r.nodeId; break; }
    } catch (e) { /* root had no match */ }
  }
  if (!nodeId) throw new Error('forcePseudo: [data-m-force] node not found in document or shadow roots');
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
  const keep = prev && Object.keys(prev.states || {}).length ? { page: prev.page, run: prev.run, url: prev.url } : null;
  comp(key, { title: meta.title, group: meta.group, desc: meta.desc, selector: meta.sel });
  if (!listed.has(key)) listed.set(key, new Set());
  for (const st of list) listed.get(key).add(st);
  delete out.components[key].missing;
  if (opts.open) { await reset(); try { await opts.open(); } catch (e) { log('  ! open failed', key, String(e.message).slice(0, 80)); } }
  const loc = target.filter({ visible: true }).first();
  // Webflow hydration can re-mount subtrees when async data resolves: give a
  // briefly unmounted element up to 6s to come back before declaring a miss.
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
const NEVER = /^(send|submit|sign in|log ?in|login|create|add|download|buy|purchase|pay|checkout|join|subscribe|save|apply|accept|reject|start|get started|claim|share|export|select|continue|claim this offer|try again|order( free)?( sample)?|add to cart|go to the platform)$/i;
async function toggle(loc, { allowLink = false } = {}) {
  const l = loc.filter({ visible: true }).first();
  const t = await l.evaluate((el) => ({ tag: el.tagName, type: el.getAttribute('type'), text: (el.innerText || el.getAttribute('aria-label') || '').trim() }));
  if (t.type === 'submit' || NEVER.test(t.text) || (t.tag === 'A' && !allowLink)) throw new Error(`toggle refused: ${t.tag} "${t.text}"`);
  await l.click({ timeout: 4000 }).catch(() => l.evaluate((el) => el.click()));
}

const q = (sel) => page.locator(sel);
const B4 = ['default', 'hover', 'focus-visible', 'pressed'];

// Scrolls the page down in steps and back to the top: pricing's plan cards
// and comparison rows hydrate lazily, so a cold page only has the heading
// region in the DOM when the run reaches it.
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
    await p.goto(URLS[key], { waitUntil: 'domcontentloaded', timeout: 90000 }).catch(() => {});
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

// The header's Product/Resources triggers are <details>/<summary> dropdowns;
// a click toggles them. Local UI only, never a link.
async function openDropdown() {
  const t = q('summary.nav-trigger').filter({ hasText: /^\s*Product\s*$/ }).filter({ visible: true }).first();
  if (!(await t.count())) return false;
  await t.click({ timeout: 5000 }).catch(() => t.evaluate((el) => el.click()));
  await page.waitForTimeout(1200);
  return true;
}

// Marks the smallest visible ancestor of the auth card's primary control that
// holds the card (the field + button + terms text).
async function markAuthCard(anchorRe, tag) {
  await page.evaluate(([src, flags, t]) => {
    const re = new RegExp(src, flags);
    const g = [...document.querySelectorAll('input,button')].find((b) => re.test((b.innerText || b.getAttribute('placeholder') || b.name || '')) && b.getBoundingClientRect().width > 0);
    if (!g) return;
    let n = g;
    for (let i = 0; i < 12 && n.parentElement; i++) {
      n = n.parentElement;
      const tx = n.innerText || '';
      const r = n.getBoundingClientRect();
      if (/Continue|Sign up|Log in/i.test(tx) && tx.length < 3000 && r.height > 200 && r.width < 900) {
        n.setAttribute('data-m-mark', t);
        return;
      }
    }
  }, [anchorRe.source, anchorRe.flags, tag]);
}

// Marks the smallest visible ancestor of a plan CTA that holds a plan name
// and a price — one pricing card, not the comparison grid around it.
async function markPlanCard() {
  await page.evaluate(() => {
    // .pr-sticky is the fixed plan summary bar parked above the viewport; its
    // CTAs are the first text matches but must not stand in for the plan card.
    const cta = [...document.querySelectorAll('button, a')].find((b) => /Get started|Request a demo|Contact sales|Book a demo|Talk to sales/i.test(b.innerText || '') && b.getBoundingClientRect().width > 0 && !b.closest('.pr-sticky'));
    if (!cta) return;
    let n = cta;
    for (let i = 0; i < 12 && n.parentElement; i++) {
      n = n.parentElement;
      const t = n.innerText || '';
      const r = n.getBoundingClientRect();
      if (/Free|Standard|Premium|Enterprise/i.test(t) && /\$\d|per (month|year)|forever/i.test(t) && t.length < 2500 && r.width < 700) {
        n.setAttribute('data-m-mark', 'plancard');
        return;
      }
    }
  });
}

// Marks the smallest visible ancestor of a h1 (or any sel) that paints a fill
// or a background image — kept for pages whose panels live in the light DOM.
async function markPainted(sel, tag, { maxUp = 8, minW = 100, minH = 60, descend = false } = {}) {
  const ok = await page.evaluate(([s, t, up, w, h, desc]) => {
    document.querySelectorAll(`[data-m-mark="${t}"]`).forEach((n) => n.removeAttribute('data-m-mark'));
    const el = [...document.querySelectorAll(s)].find((n) => { const r = n.getBoundingClientRect(); return r.width > 0 && r.height > 0; });
    if (!el) return false;
    const paints = (cs) => cs.backgroundColor !== 'rgba(0, 0, 0, 0)' || cs.backgroundImage !== 'none';
    if (!desc) for (let n = el, i = 0; n && i < up; n = n.parentElement, i++) {
      const cs = getComputedStyle(n);
      const r = n.getBoundingClientRect();
      if (r.width >= w && r.height >= h && paints(cs)) { n.setAttribute('data-m-mark', t); return true; }
    }
    if (desc) {
      const sec = el.closest('section') || el.parentElement;
      const cands = [...(sec || el).querySelectorAll('*')].filter((n) => {
        const r = n.getBoundingClientRect(); const cs = getComputedStyle(n);
        return r.width >= w && r.height >= h && paints(cs);
      }).sort((a, b) => b.getBoundingClientRect().width * b.getBoundingClientRect().height - a.getBoundingClientRect().width * a.getBoundingClientRect().height);
      if (cands[0]) { cands[0].setAttribute('data-m-mark', t); return true; }
    }
    return false;
  }, [sel, tag, maxUp, minW, minH, descend]);
  return ok ? q(`[data-m-mark="${tag}"]`) : q('[data-m-mark="__none__"]');
}

const G = {
  shell: 'Shell and navigation', home: 'Home', pricing: 'Pricing',
  customers: 'Customers', templates: 'Templates', demo: 'Demo request',
  auth: 'Log in and sign up', footer: 'Footer', mobile: 'Mobile (390 wide)',
};

async function home() {
  if (!(await newPage('home'))) return;
  await sheetsFor('home');
  await chrome('home');
  const g = G.shell;
  await S('header', q('header').filter({ visible: true }).first(), ['default'], { group: g, title: 'Header', desc: 'The sticky marketing header: the Dock logo, the Product and Resources <details> dropdowns, Pricing and Customers links, Log in, Request demo and the Start-for-free primary action.', sel: 'header' }, { noScroll: true });
  await S('logo', q('header a[href="/"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Logo', desc: 'The Dock wordmark anchor.', sel: 'header a[href="/"]' }, { noScroll: true });
  await S('nav-trigger', q('summary.nav-trigger').filter({ hasText: /^\s*Product\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Nav trigger', desc: 'The Product <summary> that opens the header mega-menu; toggled, never followed.', sel: 'summary.nav-trigger "Product"' }, { noScroll: true });
  await S('nav-link', q('header a.nav-trigger, header a.nav-direct').filter({ hasText: /^\s*Pricing\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Nav link', desc: 'The plain Pricing header link.', sel: 'header a "Pricing"' }, { noScroll: true });
  await S('nav-login', q('header a').filter({ hasText: /^\s*Log in\s*$/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Log-in link', desc: 'The Log-in header action (to auth.dock.us); measured, never followed.', sel: 'header a "Log in"' }, { noScroll: true });
  await S('nav-demo', q('header a').filter({ hasText: /Request demo/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Demo button', desc: 'The Request-demo header action; measured, never followed.', sel: 'header a "Request demo"' }, { noScroll: true });
  await S('nav-cta', q('header a').filter({ hasText: /Start for free/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Nav CTA', desc: 'The Start-for-free primary header action; measured, never followed.', sel: 'header a "Start for free"' }, { noScroll: true });
  // Open the Product dropdown (its own <summary> toggle) and read the panel,
  // a group toggle and a link inside it while it is open.
  try { await openDropdown(); } catch (e) { log('  ! dropdown open failed', String(e.message).split('\n')[0]); }
  // The header is a <dock-site-header> web component; locators pierce its
  // shadow root, and .menu-viewport is the painted mega-menu panel it opens.
  // The panel can auto-close between states, so re-open it before each read.
  const ensureOpen = async () => {
    if (!(await q('.menu-viewport').filter({ visible: true }).count())) {
      await openDropdown(); await page.waitForTimeout(400);
    }
  };
  await S('nav-dropdown', q('.menu-viewport').filter({ visible: true }).first(), ['default'], { group: g, title: 'Nav dropdown', desc: 'The Product mega-menu panel inside dock-site-header, opened by its own <summary> trigger.', sel: '.menu-viewport' }, { noScroll: true, noReset: true });
  await S('menu-group', q('.menu-group h2.menu-heading, h2.menu-heading').filter({ visible: true }).first(), ['default'], { group: g, title: 'Menu group heading', desc: 'A group heading inside the opened mega-menu (Sales / Customer success / Content / Learning / AI / Integrations).', sel: 'h2.menu-heading' }, { noScroll: true, noReset: true });
  await S('menu-link', q('.menu-viewport a.menu-link, a.menu-link').filter({ visible: true }).first(), B4, { group: g, title: 'Menu link', desc: 'A feature link inside the opened mega-menu.', sel: 'a.menu-link' }, { noScroll: true, noReset: true, open: ensureOpen, before: { default: ensureOpen, hover: ensureOpen, 'focus-visible': ensureOpen, pressed: ensureOpen } });
  await page.keyboard.press('Escape'); await page.waitForTimeout(400);
  const h = G.home;
  await S('hero-title', q('h1').filter({ visible: true }).first(), ['default'], { group: h, title: 'Hero headline', desc: 'The "Build high-performing sales teams" display headline.', sel: 'h1' }, { noScroll: true });
  // The lede is the first real paragraph after the hero h1 — a broad
  // "revenue|seller" text match lands on p.hero-eyebrow (the "AI Revenue
  // Enablement" tag) instead, so mark the intended node by structure: a
  // visible paragraph below the headline that is not an eyebrow/kicker and
  // carries real sentence-length copy.
  await page.evaluate(() => {
    const h1 = [...document.querySelectorAll('main h1, h1')].find((n) => n.getBoundingClientRect().width > 0);
    if (!h1) return;
    const top = h1.getBoundingClientRect().top;
    for (const p of [...document.querySelectorAll('main p, p')]) {
      const r = p.getBoundingClientRect();
      const t = (p.innerText || '').trim();
      if (r.width <= 0 || r.top < top - 40) continue;
      if (/eyebrow|kicker|overline|tagline|tag/i.test(String(p.className))) continue;
      if (t.length < 40) continue;
      p.setAttribute('data-m-mark', 'herolede');
      return;
    }
  });
  await S('hero-lede', q('[data-m-mark="herolede"]').filter({ visible: true }).first(), ['default'], { group: h, title: 'Hero copy', desc: 'The lede under the hero headline — the first sentence-length paragraph after the h1, not the hero-eyebrow tag.', sel: 'first p after h1 (data-m-mark)' });
  await S('hero-cta', q('a.dock-home-button').filter({ hasText: /Start for free/i }).filter({ visible: true }).first(), B4, { group: h, title: 'Hero CTA', desc: 'The primary Start-for-free action in the hero; measured, never followed.', sel: 'a.dock-home-button "Start for free"' });
  await S('hero-demo', q('a.dock-home-button').filter({ hasText: /Request demo/i }).filter({ visible: true }).first(), B4, { group: h, title: 'Hero demo action', desc: 'The secondary Request-demo action in the hero; measured, never followed.', sel: 'a.dock-home-button "Request demo"' });
  await S('hero-card', q('.hero-screen, .sales-room, .hero-intro .page-placeholder').filter({ visible: true }).first(), ['default'], { group: h, title: 'Hero artwork', desc: 'The painted product-scene layer behind the hero copy (the sales-room artwork panel).', sel: '.hero-screen' });
  await S('section-h2', q('h2').filter({ visible: true }).first(), ['default'], { group: h, title: 'Section heading', desc: 'A section heading in the light sections.', sel: 'h2' });
  await S('mcp-prompt', q('.mcp-prompt').filter({ visible: true }).first(), ['default'], { group: h, title: 'MCP prompt', desc: 'The Dock-MCP "install the prompt" widget in the MCP section: a prompt field, an Explore link and the Copy action.', sel: '.mcp-prompt' });
  await S('mcp-copy', q('button.mcp-copy').filter({ visible: true }).first(), B4, { group: h, title: 'Copy prompt', desc: 'The Copy-prompt action in the MCP widget; hover/focus/pressed read, the copy itself never clicked.', sel: 'button.mcp-copy' });
  await S('agent-field', q('input[aria-label*="prompt" i]').filter({ visible: true }).first(), ['default'], { group: h, title: 'Prompt field', desc: 'The read-only Dock-MCP setup prompt input; it paints inside the collapsed label.mcp-prompt-field, so only the hidden state is normally reachable.', sel: 'input[aria-label*="prompt"]' });
  save();
}

async function pricing() {
  if (!(await newPage('pricing', { wait: 10000 }))) return;
  await sheetsFor('pricing');
  await chrome('pricing');
  await lazyLoad();
  const g = G.pricing;
  await S('pricing-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Pricing title', desc: 'The "Dock Pricing" display heading.', sel: 'h1 on /pricing' }, { noScroll: true });
  await S('pr-sticky', q('.pr-sticky').filter({ visible: true }).first(), ['default'], { group: g, title: 'Plan bar', desc: 'The sticky plan summary bar that pins under the header while scrolling the plan comparison.', sel: '.pr-sticky' }, { noScroll: true });
  await markPlanCard();
  await S('plan-card', q('[data-m-mark="plancard"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Plan card', desc: 'A pricing plan card (plan name, price and its action).', sel: 'plan card' });
  await S('plan-name', q('.plan-name').filter({ visible: true }).first(), ['default'], { group: g, title: 'Plan name', desc: "A plan card's name (Free / Standard / Premium / Enterprise).", sel: '.plan-name' });
  await S('plan-price', q('.plan-price, .pr-sticky-price').filter({ hasText: /\$\d|forever/i }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Plan price', desc: "A plan card's price figure.", sel: '.plan-price' });
  await S('plan-cta', q('[data-m-mark="plancard"] a, [data-m-mark="plancard"] button').filter({ hasText: /Get started|Talk to sales|Request/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Plan CTA', desc: "A plan card's Get-started action (not the fixed .pr-sticky summary bar); measured, never followed.", sel: 'plan card CTA' });
  await S('faq-item', q('main details.faq-item summary, main details summary').filter({ visible: true }).first(), [...B4, 'opened'], { group: g, title: 'FAQ item', desc: 'A pricing FAQ <details>/<summary> row; toggled open once for the opened state, a local UI toggle.', sel: 'main details.faq-item summary' });
  save();
}

async function customers() {
  if (!(await newPage('customers', { wait: 10000 }))) return;
  await sheetsFor('customers');
  await chrome('customers');
  const g = G.customers;
  await S('customers-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Customers title', desc: 'The "Why revenue teams love Dock" display heading.', sel: 'h1 on /customers' }, { noScroll: true });
  await S('filter-radio', q('label.filter--item').filter({ visible: true }).first(), B4, { group: g, title: 'Filter radio', desc: 'A category filter pill on the testimonial wall ("💙 All Dock love" / Sales / Enablement …); a local UI filter, one was toggled for the selected state.', sel: 'label.filter--item' });
  await S('customer-card', q('.customers--grid a.link-block, a.link-block').filter({ visible: true }).first(), B4, { group: g, title: 'Customer card', desc: 'A customer-story card in the grid; measured, never followed.', sel: '.customers--grid a.link-block' });
  await S('testimonial', q('.testimonial').filter({ visible: true }).first(), ['default'], { group: g, title: 'Testimonial', desc: 'A testimonial block in the wall of love.', sel: '.testimonial' });
  save();
}

async function templates() {
  if (!(await newPage('templates', { wait: 10000 }))) return;
  await sheetsFor('templates');
  await chrome('templates');
  const g = G.templates;
  await S('templates-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Templates title', desc: 'The "Templates" display heading.', sel: 'h1 on /templates' }, { noScroll: true });
  await S('templates-sidebar', q('.sidebar--sticky, aside').filter({ visible: true }).first(), ['default'], { group: g, title: 'Sidebar', desc: 'The template category sidebar.', sel: '.sidebar--sticky' });
  await S('sidebar-link', q('.sidebar--sticky a, aside a').filter({ hasText: /Sales|Customer|Onboarding/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Sidebar link', desc: 'A category link in the template sidebar; measured, never followed.', sel: 'sidebar a' });
  await S('template-card', q('a[href^="/templates/"]').filter({ visible: true }).first(), B4, { group: g, title: 'Template card', desc: 'A template card in the gallery; measured, never followed.', sel: 'a[href^="/templates/"]' });
  save();
}

async function demo() {
  if (!(await newPage('demo', { wait: 16000 }))) return;
  await sheetsFor('demo');
  await chrome('demo');
  const g = G.demo;
  await S('demo-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Demo title', desc: 'The "Request a Demo" display heading.', sel: 'h1 on /demo' }, { noScroll: true });
  await S('demo-form', q('#dock-demo-form, form.hs-form, .demo-form-mount').filter({ visible: true }).first(), ['default'], { group: g, title: 'Demo form mount', desc: 'The HubSpot scheduler mount on /demo; its fields paint inside the hsforms iframe, which is read through the frame below — nothing was ever submitted.', sel: '#dock-demo-form' });
  const df = page.frameLocator('iframe.hs-form-iframe, #dock-demo-form iframe');
  await S('demo-field', df.locator('input[type="email"], input[type="text"], input').filter({ visible: true }).first(), ['default', 'focused'], { group: g, title: 'Demo field', desc: 'A field inside the HubSpot demo form (read through the iframe); clicked into once for the focused state, never filled or submitted.', sel: 'hsform iframe input' });
  await S('demo-submit', df.locator('input[type="submit"], button').filter({ visible: true }).first(), B4, { group: g, title: 'Demo submit', desc: 'The Schedule-demo submit inside the HubSpot iframe; measured, never pressed.', sel: 'hsform iframe submit' });
  save();
}

async function login() {
  if (!(await newPage('login', { wait: 10000 }))) return;
  await sheetsFor('login');
  const g = G.auth;
  await markAuthCard(/Subdomain|subdomain/i, 'logincard');
  await S('login-card', q('[data-m-mark="logincard"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Login card', desc: 'The sign-in card on auth.dock.us (a workspace-subdomain field + Continue); captured, never used.', sel: 'login card' }, { noScroll: true });
  await S('subdomain-field', q('input[name="subdomain"], input').filter({ visible: true }).first(), ['default', 'focused', 'filled'], { group: g, title: 'Subdomain field', desc: 'The workspace-subdomain input; focused and given sample text that was deleted again — nothing sent.', sel: 'input[name=subdomain]' }, { noScroll: true, fillText: 'acme' });
  await S('continue-btn', q('button').filter({ hasText: /^\s*Continue\s*$/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Continue button', desc: "The login form's Continue submit; measured, never pressed.", sel: 'button "Continue"' }, { noScroll: true });
  save();
}

async function signup() {
  if (!(await newPage('signup', { wait: 10000 }))) return;
  await sheetsFor('signup');
  const g = G.auth;
  await markAuthCard(/email|Enter email/i, 'signupcard');
  await S('signup-card', q('[data-m-mark="signupcard"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Signup card', desc: 'The create-account card on auth.dock.us; captured, never used.', sel: 'signup card' }, { noScroll: true });
  await S('signup-field', q('input[type="email"], input[name="email"], input').filter({ visible: true }).first(), ['default', 'focused', 'filled'], { group: g, title: 'Signup email field', desc: 'The signup email input; focused and given sample text that was deleted again — nothing sent.', sel: 'input[type=email]' }, { noScroll: true });
  await S('signup-check', q('iframe[src*="challenges.cloudflare" i], iframe[src*="turnstile" i], iframe').filter({ visible: true }).first(), ['default'], { group: g, title: 'Human check', desc: 'The Cloudflare Turnstile "Verify you are human" widget on the signup card (an iframe; its inner checkbox cannot be read and was never toggled).', sel: 'turnstile iframe' }, { noScroll: true });
  // The email form's submit, not the OAuth actions above it: prefer the
  // form's type="submit" button and fall back to an exact label match, so a
  // broad text match can never save "Continue with Google" as the submit.
  let submit = q('button[type="submit"]').filter({ hasText: /Sign up|Create|Continue/i }).filter({ visible: true }).first();
  if (!(await submit.count())) {
    submit = q('button').filter({ hasText: /^\s*(Sign up|Create account|Create|Continue)\s*$/i }).filter({ visible: true }).first();
  }
  if (await submit.count()) {
    const picked = await submit.evaluate((el) => (el.innerText || '').trim()).catch(() => '');
    if (/google|microsoft|apple|sso|saml/i.test(picked)) {
      log('  ! signup-submit matched an OAuth action, not the email submit; recorded missing:', JSON.stringify(picked));
      delete out.components['signup-submit'];
      submit = q('[data-m-none="signup-submit"]');
    }
  }
  await S('signup-submit', submit, B4, { group: g, title: 'Signup submit', desc: "The signup card's email-form submit (the OAuth actions above it are different controls); measured, never pressed.", sel: 'button[type=submit] on sign-up' }, { noScroll: true });
  save();
}

async function footer() {
  if (!(await newPage('home', { wait: 6000 }))) return;
  const g = G.footer;
  await page.evaluate(() => scrollTo(0, document.documentElement.scrollHeight));
  await page.waitForTimeout(1500);
  await S('footer', q('footer').filter({ visible: true }).last(), ['default'], { group: g, title: 'Footer', desc: 'The marketing footer: link columns, legal, social and the trust badges.', sel: 'footer' }, { noScroll: true });
  await S('footer-link', q('footer a').filter({ hasText: /\S/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Footer link', sel: 'footer a' }, { noScroll: true });
  await S('trust-badge', q('footer .trust-badge, footer [class*="trust" i]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Trust badge', desc: 'A compliance badge in the footer (GDPR / SOC 2 …).', sel: 'footer .trust-badge' }, { noScroll: true });
  save();
}

async function mobile() {
  if (!(await newPage('mobile', { mobile: true, url: 'https://dock.us/' }))) return;
  await chrome('mobile');
  const g = G.mobile;
  await S('m-header', q('header').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile header', sel: 'header at 390' }, { noScroll: true });
  const menu = q('summary.navigation-toggle, .nav-mobile-toggle, button[aria-label*="menu" i]').filter({ visible: true }).first();
  await S('m-menu-button', menu, ['default'], { group: g, title: 'Menu button', desc: 'The header Menu <summary> toggle inside dock-site-header.', sel: 'summary.navigation-toggle' }, { noScroll: true });
  try {
    if (await menu.count()) { await menu.click({ timeout: 5000 }).catch(() => menu.evaluate((el) => el.click())); await page.waitForTimeout(1600); }
  } catch (e) { log('  ! mobile menu toggle failed', String(e.message).split('\n')[0]); }
  // The opened panel is .navigation-content inside the shadow root's
  // details.navigation; locators pierce the shadow boundary.
  await S('m-menu-open', q('details.navigation[open] .navigation-content, .navigation-content').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile menu, open', desc: 'The opened mobile navigation panel inside dock-site-header (the expanded list of nav groups and actions).', sel: 'details.navigation[open] .navigation-content' }, { noScroll: true, noReset: true });
  await S('m-nav-item', q('details.navigation[open] summary.nav-trigger, details.navigation[open] a.menu-link').filter({ hasText: /^\s*(Product|Resources|Sales|Content|Learning)\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Mobile nav item', desc: 'A nav item inside the opened mobile menu.', sel: 'mobile menu item' }, { noScroll: true, noReset: true });
  await page.keyboard.press('Escape'); await page.waitForTimeout(500);
  // Escape does not close a <details> menu: use its own toggle so m-hero is not read under it
  if (await q('details.navigation[open]').count()) { await menu.click({ timeout: 5000 }).catch(() => menu.evaluate((el) => el.click())); await page.waitForTimeout(800); }
  await S('m-hero', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile headline', sel: 'h1 at 390' });
  save();
}

run = new Date().toISOString().slice(0, 10);
out._meta.read = run;
out._meta.viewport = '1440 x 900 (mobile group 390 x 844); the public surface paints light only — the marketing site has no dark theme (its .dark classes paint individual sections) and the auth app paints light';
out._meta.tool = 'tools/capture/public/measure.mjs';
const { browser, context: ctx0 } = await launch();
context = ctx0;
const pages = process.argv.slice(2);
const plan = { home, pricing, customers, templates, demo, login, signup, mobile };
const order = Object.keys(plan).filter((k) => !pages.length || pages.includes(k));
try {
  for (const k of order) { if (k !== 'mobile') await plan[k](); }
  if (!pages.length || pages.includes('home')) await footer();
  if (!pages.length || pages.includes('mobile')) await plan.mobile();
  // Reduced-motion check on an element that actually transitions (a header
  // dropdown trigger), so the delta is meaningful.
  if (!pages.length || pages.includes('home')) await reducedMotion('home', 'summary.nav-trigger');
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
