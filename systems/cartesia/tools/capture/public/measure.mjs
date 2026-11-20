// Measures cartesia.ai's public components in every state reachable without
// signing in, cloning a voice, buying or submitting anything.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node measure.mjs [page ...]
//
// Pages: home sonic voices pricing signin signup docs mobile.
// Writes raw/components-computed.json (merged) and one crop per component and
// state into components/crops/; raw/measurements.md is built by
// build-measurements.mjs.
//
// cartesia.ai is three surfaces: the Astro/Tailwind marketing site (utility
// classes over a declared --cartesia-*/semantic token layer, .dark islands),
// play.cartesia.ai's auth card (Clerk-style, signed-out wall only) and
// docs.cartesia.ai (a Mintlify docs app in Inter). Nothing is sent, recorded,
// bought or signed into: the only presses are local UI toggles — the header
// Products menu (a Radix navigation-menu-trigger), the Cloud/On-premise
// accordion, a use-case chip, a voice chip and the mobile menu. Play buttons
// are measured but never pressed, and the consent island is hidden, never
// answered.
import fs from 'node:fs';
import path from 'node:path';
import { BASE, PLAY, DOCS, M, launch, patch, open, closePromo, domFind, styleOf, crop, centre, RAW, UA, UA_MOBILE } from './lib.mjs';

const OUT = process.env.OUT_JSON || path.join(RAW, 'components-computed.json');
const out = fs.existsSync(OUT) ? JSON.parse(fs.readFileSync(OUT, 'utf8')) : {};
out._meta ??= {};
out.components ??= {};
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const save = () => fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');
const URLS = { home: '/', sonic: '/sonic', voices: '/voices', pricing: '/pricing', signin: PLAY + '/sign-in', signup: PLAY + '/sign-in/create', docs: DOCS + '/', mobile: '/' };
const abs = (key) => (URLS[key] && URLS[key].startsWith('http') ? URLS[key] : BASE + URLS[key]);
let page, cdp, current, context, run, liveCtx;
const touched = new Set();
const listed = new Map();
// Routes the edge gates this run: components last measured on them keep their
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
  await open(page, url || abs(key), { wait, promo });
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
  Object.assign(c, { page: current, run, url: abs(current) }, meta);
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
      } else if (st === 'selected') {
        if (opts.noToggle) via = 'held selected by an earlier toggle';
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

// Clicks a UI toggle (menu trigger, accordion, chip, locale dot). Refuses a
// submit button and any control whose text names an action this kit must
// never take.
const NEVER = /^(send|submit|sign in|log ?in|login|create|add|download|buy|purchase|pay|checkout|join|subscribe|save|apply|accept|reject|start free|get started|claim|share|export|continue|claim this offer|try again|next|confirm|schedule event|i understand|decline|try cartesia|try sonic|clone your voice|contact sales|contact us|select startup|call the agent.*|record your voice|upload recording)$/i;
async function toggle(loc, { allowLink = false } = {}) {
  const l = loc.filter({ visible: true }).first();
  const t = await l.evaluate((el) => ({ tag: el.tagName, type: el.getAttribute('type'), text: (el.innerText || el.getAttribute('aria-label') || '').trim() }));
  if (t.type === 'submit' || NEVER.test(t.text) || (t.tag === 'A' && !allowLink)) throw new Error(`toggle refused: ${t.tag} "${t.text}"`);
  await l.click({ timeout: 4000 }).catch(() => l.evaluate((el) => el.click()));
}

const q = (sel) => page.locator(sel);
const B4 = ['default', 'hover', 'focus-visible', 'pressed'];
const navTrigger = () => q('header button[data-slot="navigation-menu-trigger"], header button').filter({ hasText: /^\s*Products\s*$/ }).first();
// Click the Products trigger only when the menu is closed: a second click
// would collapse it again, and the measurements below need it open.
const openNav = async () => {
  const t = navTrigger();
  if (!(await t.count())) return;
  const state = () => page.evaluate(() => ({ n: document.querySelectorAll('[data-slot="navigation-menu-content"]').length, open: [...document.querySelectorAll('[data-slot="navigation-menu-content"]')].some((e) => { const r = e.getBoundingClientRect(); return r.width > 100 && r.height > 50; }) }));
  if ((await state()).open) return;
  const ok = await t.click({ timeout: 5000 }).then(() => true).catch(async () => { await t.evaluate((el) => el.click()); return 'js'; });
  await page.waitForTimeout(1100);
  const after = await state();
  log('  · openNav click=' + ok, 'content=' + after.n, 'open=' + after.open);
  // A click on a hover-armed trigger can toggle the menu closed again; click
  // once more when the first press left it shut.
  if (!after.open && ok === true) {
    await t.click({ timeout: 5000 }).catch(() => {});
    await page.waitForTimeout(1100);
    const again = await state();
    log('  · openNav retry', 'content=' + again.n, 'open=' + again.open);
  }
};
// Cartesia mounts its Astro islands on intersection (client:visible), so a
// component below the fold may not exist in the DOM until it has been
// scrolled to. The sweep walks the page once, mounts every island, and comes
// back to the top.
async function lazySweep() {
  await page.evaluate(async () => {
    const h = document.documentElement.scrollHeight;
    for (let y = 0; y < h; y += 700) { scrollTo(0, y); await new Promise((r) => setTimeout(r, 110)); }
    scrollTo(0, 0);
  });
  await page.waitForTimeout(1400);
}
// The biggest visible element matching sel gets data-m-mark="<tag>"; returns
// a locator for it (an empty one when nothing matched).
async function markBiggest(sel, tag, { minW = 100, minH = 40 } = {}) {
  const ok = await page.evaluate(([s, t, w, h]) => {
    document.querySelectorAll(`[data-m-mark="${t}"]`).forEach((n) => n.removeAttribute('data-m-mark'));
    const cands = [...document.querySelectorAll(s)].filter((n) => {
      const r = n.getBoundingClientRect();
      return r.width >= w && r.height >= h && getComputedStyle(n).visibility !== 'hidden';
    }).sort((a, b) => b.getBoundingClientRect().width * b.getBoundingClientRect().height - a.getBoundingClientRect().width * a.getBoundingClientRect().height);
    if (!cands[0]) return false;
    cands[0].setAttribute('data-m-mark', t);
    return true;
  }, [sel, tag, minW, minH]);
  return ok ? page.locator(`[data-m-mark="${tag}"]`) : page.locator('[data-m-mark="__none__"]');
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
    await p.goto(abs(key), { waitUntil: 'domcontentloaded', timeout: 90000 }).catch(() => {});
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

// Marks the nearest ancestor of the element matching sel that paints a fill
// or a background image (the hero island paints a gradient), or falls back to
// marking a painted descendant: the hero card is a sibling layer, not an
// ancestor, so for it we mark the painted element inside its section instead.
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
      // The painted layer sits beside the content, not above it: find the
      // biggest painted element under the element's own section.
      const sec = el.closest('section') || el.parentElement;
      const cands = [...(sec || el).querySelectorAll('*')].filter((n) => {
        const r = n.getBoundingClientRect(); const cs = getComputedStyle(n);
        return r.width >= w && r.height >= h && paints(cs);
      }).sort((a, b) => b.getBoundingClientRect().width * b.getBoundingClientRect().height - a.getBoundingClientRect().width * a.getBoundingClientRect().height);
      if (cands[0]) { cands[0].setAttribute('data-m-mark', t); return true; }
    }
    return false;
  }, [sel, tag, maxUp, minW, minH, descend]);
  return ok ? page.locator(`[data-m-mark="${tag}"]`) : page.locator('[data-m-mark="__none__"]');
}

const G = {
  shell: 'Shell and navigation', hero: 'Home hero', home: 'Home', product: 'Product pages',
  pricing: 'Pricing', auth: 'Playground sign-in boundary', docs: 'Docs (Mintlify surface)',
  footer: 'Footer', mobile: 'Mobile (390 wide)',
};

async function home() {
  if (!(await newPage('home'))) return;
  await sheetsFor('home');
  await chrome('home');
  const g = G.shell;
  await S('header', q('header[data-site-nav-header], header').filter({ visible: true }).first(), ['default'], { group: g, title: 'Header', desc: 'The sticky marketing header: wordmark, the Products/Solutions/Resources menu triggers, Customers, Pricing, Sign in, Contact Sales and the Try-Cartesia pill.', sel: 'header[data-site-nav-header]' }, { noScroll: true });
  await S('logo', q('header a[aria-label="Cartesia"], header a[href="/"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Logo', desc: 'The Cartesia wordmark anchor (verdant mark over the neutral wordmark paths).', sel: 'header a[aria-label=Cartesia]' }, { noScroll: true });
  await S('banner', q('a').filter({ hasText: /Introducing Cartesia|Managed Agents, at/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Announcement banner', desc: 'The full-width announcement strip above the header; measured never followed.', sel: 'a "Introducing Cartesia…"' }, { noScroll: true });
  await S('nav-trigger', navTrigger(), B4, { group: g, title: 'Nav trigger', desc: 'The Products button that opens the header mega-menu; toggled, never followed.', sel: 'header button "Products"' }, { noScroll: true });
  await S('nav-link', q('header nav a, header a').filter({ hasText: /^\s*Pricing\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Nav link', desc: 'The plain Pricing header link.', sel: 'header nav a "Pricing"' }, { noScroll: true });
  await S('nav-signin', q('header a').filter({ hasText: /^\s*Sign in\s*$/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Sign-in link', desc: 'The Sign-in header action (ghost pill); measured never followed.', sel: 'header a "Sign in"' }, { noScroll: true });
  await S('nav-sales', q('header a').filter({ hasText: /Contact Sales/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Sales link', desc: 'The Contact-Sales header action (outlined pill); measured never followed.', sel: 'header a "Contact Sales"' }, { noScroll: true });
  await S('nav-cta', q('header a').filter({ hasText: /^\s*Try Cartesia\s*$/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Nav CTA', desc: 'The Try-Cartesia solid pill; measured never followed.', sel: 'header a "Try Cartesia"' }, { noScroll: true });
  // The Products trigger opens the mega-menu on click (a Radix
  // navigation-menu-trigger — a local UI toggle, never a link). Keep the panel
  // open while it and one of its links are read — moving the pointer off it
  // dismisses the menu, so both reads skip the per-state reset — then Escape
  // to close.
  await S('nav-dropdown', q('[data-slot="navigation-menu-content"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Nav dropdown', desc: 'The Products mega-menu panel (navigation-menu-content), opened by its own trigger.', sel: '[data-slot=navigation-menu-content]' }, { noScroll: true, noReset: true, open: openNav });
  await S('menu-link', q('[data-slot="navigation-menu-content"] a, [data-slot="navigation-menu-content"] [data-slot="navigation-menu-link"]').filter({ hasText: /Sonic|Ink|Managed Agents|Voices|Languages/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Menu link', desc: 'A product link inside the opened mega-menu.', sel: 'menu content a "Sonic"' }, { noScroll: true, noReset: true, open: openNav });
  await page.keyboard.press('Escape'); await page.waitForTimeout(400);
  // Mount the lazy islands below the fold before the hero/home reads, then
  // give the last island a moment to hydrate.
  await lazySweep();
  await q('a').filter({ hasText: /Ink\.|Sonic\.|Managed Agents/ }).first().waitFor({ timeout: 9000 }).catch(() => {});
  const h = G.hero;
  await S('hero-title', q('h1').filter({ visible: true }).first(), ['default'], { group: h, title: 'Hero headline', desc: 'The display headline (PP Kyoto / font-display) under the header.', sel: 'h1' }, { noScroll: true });
  await S('hero-lede', q('main p, section p').filter({ visible: true }).filter({ hasText: /voice|agent|speech/i }).first(), ['default'], { group: h, title: 'Hero copy', desc: 'The lede under the headline, ABC Diatype / font-sans.', sel: 'hero lede' });
  await S('hero-orb', q('button[aria-label*="Talk to" i], button[aria-label*="Skylar" i]').filter({ visible: true }).first(), B4, { group: h, title: 'Talk-to-Skylar orb', desc: 'The large round voice-agent button in the hero (icon-only, aria-labelled); measured, never pressed (a press starts a call).', sel: 'button[aria-label*="Talk to Skylar"]' });
  // The carousel keeps duplicate chooser buttons that stay fully transparent
  // (opacity 0); Playwright's visible filter still matches them, so pick the
  // first chooser that actually paints.
  const choosers = q('button[aria-label^="Choose" i]').filter({ visible: true });
  let chooser = choosers.first();
  for (let i = 0, n = await choosers.count(); i < n; i++) {
    const el = choosers.nth(i);
    if (await el.evaluate((e) => parseFloat(getComputedStyle(e).opacity) > 0.01).catch(() => false)) { chooser = el; break; }
  }
  await S('voice-choose', chooser, B4, { group: h, title: 'Voice chooser', desc: 'A round "Choose <voice>, <role>" button around the orb (icon-only, aria-labelled).', sel: 'button[aria-label^="Choose"]' });
  await S('voice-nav', q('button[aria-label*="Next voice" i], button[aria-label*="Previous voice" i]').filter({ visible: true }).first(), B4, { group: h, title: 'Voice carousel arrow', desc: 'A previous/next-voice arrow button in the hero voice carousel.', sel: 'button[aria-label*="voice"]' });
  await S('media-frame', q('button').filter({ hasText: /Play with sound|Play with/i }).or(q('button[aria-label*="Play with" i]')).filter({ visible: true }).first(), B4, { group: h, title: 'Media frame', desc: 'A customer-story media tile with a play affordance; measured, never pressed.', sel: 'button "Play with sound"' });
  // The story tile is the painted frame around the play button.
  await page.evaluate(() => { const b = [...document.querySelectorAll('button')].find((e) => /Play with sound|Play with/i.test((e.innerText || '') + (e.getAttribute('aria-label') || ''))); b && b.setAttribute('data-m-story-btn', '1'); });
  const story = await markBiggest('button[data-m-story-btn], button[data-m-story-btn] > *', 'm-story', { minW: 200, minH: 150 });
  await S('story-card', (await story.count()) ? story : q('[data-m-story-btn]'), ['default'], { group: h, title: 'Customer story tile', desc: 'The customer-story media tile behind the play affordance.', sel: 'story media frame' });
  const s = G.home;
  await S('h2-display', q('h2[class*="font-display"], h2').filter({ visible: true }).first(), ['default'], { group: s, title: 'Section heading (display)', desc: 'A PP-Kyoto display section heading in the light sections.', sel: 'h2.font-display' });
  await S('product-card', q('a').filter({ hasText: /^Ink\.|^Sonic\./ }).filter({ visible: true }).first(), B4, { group: s, title: 'Product card', desc: 'A product card link (Ink/Sonic) in the full-stack section; measured never followed.', sel: 'a product card "Ink."' });
  await S('product-row', q('a').filter({ hasText: /Managed Agents\./i }).filter({ visible: true }).first(), B4, { group: s, title: 'Product row', desc: 'The wide Managed-Agents product row link; measured never followed.', sel: 'a "Managed Agents."' });
  await S('cta-link', q('a').filter({ hasText: /^\s*Our research\s*$/i }).filter({ visible: true }).first(), B4, { group: s, title: 'Text CTA', desc: 'The "Our research" pill link in the research section; measured never followed.', sel: 'a "Our research"' });
  await S('accordion-trigger', q('button[data-slot*="accordion"], button').filter({ hasText: /^\s*(Cloud|On-premise)\s*$/ }).filter({ visible: true }).first(), B4.concat('selected'), { group: s, title: 'Accordion trigger', desc: 'A Cloud/On-premise deployment accordion header; toggled for its collapsed/expanded state.', sel: 'button accordion "Cloud"' });
  // Open a deployment section, then measure the expanded answer region —
  // [role="region"] matches the trigger stack, not the content.
  const accTrig = q('button[data-slot*="accordion"], button').filter({ hasText: /^\s*(Cloud|On-premise)\s*$/ }).filter({ visible: true }).first();
  // The trigger's own 'selected' state above already opened it; a second click closed it again and the
  // content reading caught the trigger stack. Click only when the section is not open.
  const isOpen = async () => (await accTrig.getAttribute('data-state').catch(() => null)) === 'open' || (await accTrig.getAttribute('aria-expanded').catch(() => null)) === 'true';
  if (await accTrig.count() && !(await isOpen())) { await accTrig.click({ timeout: 6000 }).catch(() => accTrig.evaluate((e) => e.click())); await page.waitForTimeout(900); }
  await S('accordion-content', q('[data-slot="accordion-content"]').filter({ visible: true }).first(), ['default'], { group: s, title: 'Accordion content', desc: 'The expanded accordion region beside the deployment triggers, opened for the read.', sel: '[data-slot=accordion-content]' });
  save();
}

async function sonic() {
  if (!(await newPage('sonic', { wait: 9000 }))) return;
  await sheetsFor('sonic');
  await chrome('sonic');
  await lazySweep();
  const g = G.product;
  await S('pd-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Product headline', desc: 'The Sonic product-page display headline.', sel: 'h1 on /sonic' }, { noScroll: true });
  await S('pd-cta', q('main a, section a').filter({ hasText: /Try Sonic/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Product CTA', desc: 'The "Try Sonic-3.6" hero action; measured never followed.', sel: 'a "Try Sonic-3.6"' }, { noScroll: true });
  await S('pd-secondary', q('main a').filter({ hasText: /Contact Sales/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Secondary CTA', desc: 'The Contact-Sales hero action; measured never followed.', sel: 'a "Contact Sales" hero' }, { noScroll: true });
  await S('usecase-chip', q('button').filter({ hasText: /^\s*(Customer Support|Storytelling|Concierge|Logistics)\s*$/ }).filter({ visible: true }).first(), B4.concat('selected'), { group: g, title: 'Use-case chip', desc: 'A demo use-case chip in the voice demo; toggled for its selected state (switches the demo script, nothing sent).', sel: 'button "Customer Support"' });
  await S('voice-chip', q('button').filter({ hasText: /^\s*(American English|Jacqueline)\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Voice/locale chip', desc: 'A rounded-full locale or voice picker chip in the demo bar.', sel: 'button "American English" / "Jacqueline"' });
  await S('play-btn', q('button').filter({ hasText: /^\s*Play\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Play button', desc: 'The demo Play action; measured, never pressed.', sel: 'button "Play"' });
  await S('word-play', q('button[aria-label^="Play " i], button').filter({ hasText: /^Play (Original|Clone|charcuterie|subpoena|epinephrine)/i }).or(q('button[aria-label^="Play " i]')).filter({ visible: true }).first(), B4, { group: g, title: 'Sample play button', desc: 'A 32px square play button on a pronunciation/clone sample (icon-only, aria-labelled); measured, never pressed.', sel: 'button[aria-label^="Play"]' });
  await S('voice-row', q('button').filter({ hasText: / - (American English|Canadian French|Castilian Spanish)/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Voice row', desc: 'A "voice — locale" row in the voice list (group flex row with a play affordance).', sel: 'button "Emma - American English"' });
  save();
}

async function voices() {
  if (!(await newPage('voices', { wait: 9000 }))) return;
  await sheetsFor('voices');
  const g = G.product;
  await S('voices-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Voices headline', desc: 'The "Find your voice." display headline.', sel: 'h1 on /voices' }, { noScroll: true });
  await S('globe-dot', q('button.voices-globe-dot, button[class*="voices-globe-dot"]').filter({ visible: true }).first(), B4, { group: g, title: 'Globe locale dot', desc: 'A locale dot on the voices globe; toggled, never dragged.', sel: 'button.voices-globe-dot' });
  await S('globe-play', q('button.voices-globe-play, button[class*="voices-globe-play"]').filter({ visible: true }).first(), B4, { group: g, title: 'Globe play', desc: 'The round play button inside the voices globe; measured, never pressed.', sel: 'button.voices-globe-play' });
  await S('globe-arrow', q('button.voices-globe-arrow, button[class*="voices-globe-arrow"]').filter({ visible: true }).first(), B4, { group: g, title: 'Locale arrow', desc: 'A previous/next-locale arrow in the globe panel.', sel: 'button.voices-globe-arrow' });
  await S('globe-voice', q('button.voices-globe-voice, button[class*="voices-globe-voice"]').filter({ visible: true }).first(), B4, { group: g, title: 'Globe voice row', desc: 'A "voice + persona" row in the globe voice list.', sel: 'button.voices-globe-voice' });
  save();
}

async function pricing() {
  if (!(await newPage('pricing', { wait: 10000 }))) return;
  await sheetsFor('pricing');
  await chrome('pricing');
  const g = G.pricing;
  await S('pricing-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Pricing title', desc: 'The pricing page display heading.', sel: 'h1 on /pricing' }, { noScroll: true });
  await lazySweep();
  await S('plan-name', q('h3').filter({ hasText: /^\s*(Text to Speech|Speech to Text|Voice Agents)\s*$/ }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Plan group name', desc: 'A plan group heading (Text to Speech / Speech to Text / Voice Agents).', sel: 'h3 plan group' });
  await S('plan-tab', q('button').filter({ hasText: /^\s*(Pro|Startup|Scale)\s*$/ }).filter({ visible: true }).first(), B4.concat('selected'), { group: g, title: 'Plan tab', desc: 'A plan tab in the compare strip (Free/Pro/Startup/Scale/Enterprise); toggled for its selected state, never checked out.', sel: 'button plan tab "Pro"' });
  await S('plan-slider', q('input[aria-label*="minutes" i], input[aria-label*="audio" i]').filter({ visible: true }).first(), ['default', 'focused'], { group: g, title: 'Usage slider', desc: 'The "Minutes of generated audio per month" range input in the cost calculator; focused only, never dragged.', sel: 'input[aria-label*=minutes]' });
  await S('plan-cta', q('a').filter({ hasText: /^\s*Start free\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Plan CTA', desc: 'A plan card\'s "Start free" action; measured never followed.', sel: 'a "Start free"' });
  await S('plan-cta-alt', q('a').filter({ hasText: /^\s*(Select Startup|Contact us)\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Plan CTA alt', desc: 'A secondary plan action ("Select Startup"/"Contact us"); measured never followed.', sel: 'a "Select Startup"' });
  // The plan card is the painted cell that holds the CTA: tag the CTA first,
  // then walk up to its painted ancestor.
  await page.evaluate(() => { const a = [...document.querySelectorAll('a')].find((e) => /^\s*Start free\s*$/.test(e.innerText || '')); a && a.setAttribute('data-m-plan-cta', '1'); });
  const planCard = await markPainted('[data-m-plan-cta]', 'm-plan', { minW: 200, minH: 300 }).catch(() => null);
  await S('plan-card', (await (planCard || q('[data-m-mark="__none__"]')).count()) ? planCard : q('div[class*="ring-1" i]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Plan card', desc: 'A pricing plan card (the painted cell holding the plan CTA, ring-1 bg-background).', sel: 'plan card' });
  await S('faq-trigger', q('summary.faq-summary, details summary').filter({ visible: true }).first(), B4.concat('selected'), { group: g, title: 'FAQ item', desc: 'An FAQs details/summary row (the summary toggles its own answer).', sel: 'summary.faq-summary' });
  save();
}

async function signin() {
  if (!(await newPage('signin', { wait: 9000 }))) return;
  await sheetsFor('signin');
  await chrome('signin');
  const g = G.auth;
  // The sign-in surface is a centred column, not a painted card: main is the
  // column that holds the h1, the email form and the legal links.
  const card = await markBiggest('main, [class*="card" i]', 'm-login', { minW: 250, minH: 200 });
  await S('login-card', card, ['default'], { group: g, title: 'Sign-in card', desc: 'The centred sign-in column on play.cartesia.ai (the boundary before the gated playground); never filled or submitted.', sel: 'sign-in main column' }, { noScroll: true });
  await S('email-field', q('input[type="email"], input[name*="email" i], input[type="text"], input').filter({ visible: true }).first(), ['default', 'focused', 'filled'], { group: g, title: 'Email field', desc: 'The email-address input; sample text was typed and deleted, nothing sent.', sel: 'input[type=email]' });
  await S('continue-btn', q('button').filter({ hasText: /^\s*Continue\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Continue button', desc: 'The Continue submit; measured, never pressed (a press would submit the form).', sel: 'button "Continue"' });
  // The OAuth buttons render icon-only in some page variants: fall back to the
  // first textless svg button in the form column when the label is not there.
  let sso = q('button').filter({ hasText: /Google|GitHub|Apple/i }).filter({ visible: true }).first();
  if (!(await sso.count())) {
    await page.evaluate(() => {
      const b = [...document.querySelectorAll('main button, form button')].find((e) => {
        const r = e.getBoundingClientRect();
        return e.querySelector('svg, img') && !(e.innerText || '').trim() && r.width > 100 && r.width < 300 && r.height > 30;
      });
      b && b.setAttribute('data-m-mark', 'm-sso');
    });
    sso = q('[data-m-mark="m-sso"]');
  }
  await S('sso-btn', sso, B4, { group: g, title: 'SSO button', desc: 'An OAuth button beside the form (labelled "Continue with Google"/"Continue with GitHub" when the labels render); measured, never followed.', sel: 'sso button' });
  await S('passkey-btn', q('button').filter({ hasText: /passkey/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Passkey button', desc: 'The "Sign in with a passkey" text action; measured, never pressed.', sel: 'button "Sign in with a passkey"' });
  save();
}

async function signup() {
  if (!(await newPage('signup', { wait: 9000 }))) return;
  const g = G.auth;
  const card = await markBiggest('main, [class*="card" i]', 'm-signup', { minW: 250, minH: 200 });
  await S('signup-card', card, ['default'], { group: g, title: 'Signup card', desc: 'The centred create-account column (/sign-in/create); never filled or submitted.', sel: 'signup main column' }, { noScroll: true });
  await S('signup-field', q('input[type="email"], input[name*="email" i], input').filter({ visible: true }).first(), ['default', 'focused'], { group: g, title: 'Signup email field', desc: 'The signup email input; focused only, never filled or submitted.', sel: 'signup input[type=email]' });
  save();
}

async function docs() {
  if (!(await newPage('docs', { wait: 9000 }))) return;
  await sheetsFor('docs');
  await chrome('docs');
  const g = G.docs;
  await S('docs-header', q('header').filter({ visible: true }).first(), ['default'], { group: g, title: 'Docs header', desc: 'The Mintlify docs top bar (wordmark, Search ⌘K, Log In / Playground links).', sel: 'docs header' }, { noScroll: true });
  await S('docs-search', q('button').filter({ hasText: /Search/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Search button', desc: 'The "Search… ⌘K" docs search input; measured, never opened.', sel: 'button "Search…"' }, { noScroll: true });
  await S('docs-nav-item', q('aside a, nav a').filter({ hasText: /^\s*(Text-to-Speech|Speech-to-Text|Generate speech)\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Docs nav item', desc: 'A sidebar navigation link in the docs app.', sel: 'aside a "Text-to-Speech"' });
  await S('docs-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Docs title', desc: 'The docs page title (Inter, docs-platform type — a separate surface from the marketing fonts).', sel: 'docs h1' });
  save();
}

async function footer() {
  if (!(await newPage('home', { wait: 6000 }))) return;
  const g = G.footer;
  await page.evaluate(() => scrollTo(0, document.documentElement.scrollHeight));
  await page.waitForTimeout(1500);
  await S('footer', q('footer').filter({ visible: true }).last(), ['default'], { group: g, title: 'Footer', desc: 'The footer: link columns (Products/Company/Capabilities/Use cases/Industries/Resources), legal and social.', sel: 'footer' }, { noScroll: true });
  await S('footer-link', q('footer a').filter({ hasText: /\S/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Footer link', sel: 'footer a' }, { noScroll: true });
  await S('footer-col-head', q('footer h2').filter({ visible: true }).first(), ['default'], { group: g, title: 'Footer column head', desc: 'A footer column heading (17px font-sans medium).', sel: 'footer h2' }, { noScroll: true });
  save();
}

async function mobile() {
  if (!(await newPage('mobile', { mobile: true, url: BASE + '/' }))) return;
  await chrome('mobile');
  const g = G.mobile;
  await S('m-header', q('header').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile header', sel: 'header at 390' }, { noScroll: true });
  const menu = q('header button[aria-label*="menu" i], header button').filter({ visible: true }).last();
  await S('m-menu-button', menu, ['default'], { group: g, title: 'Menu button', desc: 'The header "Open menu" toggle.', sel: 'header button "Open menu"' }, { noScroll: true });
  try {
    if (await menu.count()) { await menu.click({ timeout: 5000 }).catch(() => menu.evaluate((el) => el.click())); await page.waitForTimeout(1500); }
  } catch (e) { log('  ! mobile menu toggle failed', String(e.message).split('\n')[0]); }
  await S('m-menu-open', q('[role="dialog"], [class*="fixed"][class*="inset-0"], nav').filter({ hasText: /Products|Sonic|Pricing/ }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile menu, open', desc: 'The header menu panel opened by its own toggle.', sel: 'mobile menu panel' }, { noScroll: true });
  await S('m-nav-item', q('[role="dialog"] a, [role="dialog"] button, nav a, nav button, body a, body button').filter({ hasText: /^\s*(Products|Sonic|Pricing|Sign in)\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Mobile nav item', desc: 'An item inside the opened header menu.', sel: 'mobile menu item' }, { noScroll: true });
  await page.keyboard.press('Escape'); await page.waitForTimeout(500);
  await S('m-hero', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile headline', sel: 'h1 at 390' });
  save();
}

run = new Date().toISOString().slice(0, 10);
out._meta.read = run;
out._meta.viewport = '1440 x 900 (mobile group 390 x 844); the marketing pages paint light with .dark islands (cards, panels); the sign-in card paints light on play.cartesia.ai; docs is a Mintlify light surface';
out._meta.tool = 'tools/capture/public/measure.mjs';
const { browser, context: ctx0 } = await launch();
context = ctx0;
const pages = process.argv.slice(2);
const plan = { home, sonic, voices, pricing, signin, signup, docs, mobile };
const order = Object.keys(plan).filter((k) => !pages.length || pages.includes(k));
try {
  for (const k of order) { if (k !== 'mobile') await plan[k](); }
  if (!pages.length || pages.includes('home')) await footer();
  if (!pages.length || pages.includes('mobile')) await plan.mobile();
  // Reduced-motion check on an element that transitions (the sticky header's
  // own transitions), so the delta is meaningful.
  if (!pages.length || pages.includes('home')) await reducedMotion('home', 'header[data-site-nav-header]');
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
