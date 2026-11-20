// Measures byborre.com's public components in every state reachable without
// signing in, ordering or submitting anything.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node measure.mjs [page ...]
//
// Pages: home collection textile login faq contact mobile.
// Writes raw/components-computed.json (merged) and one crop per component and
// state into components/crops/; raw/measurements.md is built by
// build-measurements.mjs.
//
// byborre.com is a Nuxt (Vue) storefront over DatoCMS with a compiled
// Tailwind utility layer (bg-cream, text-black-BRAND, the New badge's
// bg-yellow) over an inline :root that declares the --color-primary-*/
// --color-gray-* ramps. The Design Studio at /dashboard redirects signed-out
// visitors to /?redirectTo=/dashboard and opens a login dialog — that dialog
// is a public surface and is measured as one; it was never filled or
// submitted. Nothing is sent, bought or signed into: the only presses are
// local UI toggles — the About flyout, the cart drawer, a FAQ question, the
// mobile menu and the fields' own focus. The cookie consent bar is hidden,
// never answered.
import fs from 'node:fs';
import path from 'node:path';
import { BASE, M, launch, patch, open, closePromo, domFind, styleOf, crop, centre, RAW, UA, UA_MOBILE } from './lib.mjs';

const OUT = process.env.OUT_JSON || path.join(RAW, 'components-computed.json');
const out = fs.existsSync(OUT) ? JSON.parse(fs.readFileSync(OUT, 'utf8')) : {};
out._meta ??= {};
out.components ??= {};
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const save = () => fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');
const URLS = { home: '/', collection: '/collection', textile: '/collection/blink', login: '/?redirectTo=/dashboard', faq: '/faq', contact: '/contact' };
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
  // meta is the entry's description only; an option placed here (fillText, cropLoc,
  // noToggle...) would be silently ignored, so refuse it
  for (const k of Object.keys(meta)) if (!['group', 'title', 'desc', 'sel'].includes(k)) throw new Error(`S(${key}): '${k}' is an option; pass it in opts`);
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
const NEVER = /^(send|submit|sign in|log ?in|login|create|add|download|buy|purchase|pay|checkout|join|subscribe|save|apply|accept|reject|start|get started|claim|share|export|select|continue|claim this offer|try again|order( free)?( sample)?|add to cart|go to the platform)$/i;
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
    await p.goto(BASE + URLS[key], { waitUntil: 'domcontentloaded', timeout: 90000 }).catch(() => {});
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

// The About header button opens its flyout (hover on desktop). Keeps the
// pointer over the panel so it is still painted when read.
async function openAbout() {
  const t = q('header button').filter({ hasText: /^\s*About\s*$/ }).filter({ visible: true }).first();
  if (!(await t.count())) return false;
  await t.hover({ timeout: 5000 }).catch(() => {});
  await page.waitForTimeout(900);
  const open = await page.evaluate(() => [...document.querySelectorAll('header a')].some((a) => /Knit Innovation|Responsibility|Creative Control/.test(a.innerText || '') && a.getBoundingClientRect().height > 0));
  if (!open) await toggle(t, { allowLink: true }).catch(() => {});
  await page.waitForTimeout(900);
  return true;
}

const G = {
  shell: 'Shell and navigation', home: 'Home', collection: 'Textile Room',
  textile: 'Textile detail', login: 'Login dialog', faq: 'FAQ',
  contact: 'Contact form', footer: 'Footer', mobile: 'Mobile (390 wide)',
};

async function home() {
  if (!(await newPage('home'))) return;
  await sheetsFor('home');
  await chrome('home');
  const g = G.shell;
  await S('marquee', q('div[class*="animate-marquee"], div[class*="marquee" i]').locator('xpath=..').filter({ visible: true }).first(), ['default'], { group: g, title: 'Marquee bar', desc: 'The top ticker (ORDER FREE SAMPLES — WORLDWIDE SHIPPING) that scrolls continuously; measured as the outer bar, whose inner strip translates.', sel: 'marquee bar' }, { noScroll: true });
  await S('header', q('header.sticky, header').filter({ visible: true }).first(), ['default'], { group: g, title: 'Header', desc: 'The sticky cream header: wordmark, Textile Room/Design Studio links, the Collaborations and About flyout triggers, Contact, Cart and account icons, the Go-to-the-platform pill.', sel: 'header.sticky' }, { noScroll: true });
  await S('logo', q('header a[href="/"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Logo', desc: 'The BYBORRE wordmark anchor (an img inside the home link).', sel: 'header a[href="/"]' }, { noScroll: true });
  await S('nav-link', q('header nav a, header a').filter({ hasText: /^\s*Textile Room\s*/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Nav link', desc: 'The Textile Room header link (with the New badge inside it).', sel: 'header a Textile Room' }, { noScroll: true });
  await S('nav-badge', q('header').locator('div, span').filter({ hasText: /^\s*New\s*$/ }).filter({ visible: true }).last(), ['default'], { group: g, title: 'Nav badge', desc: 'The yellow "New" chip inside the Textile Room link.', sel: 'header .bg-yellow chip' }, { noScroll: true });
  await S('nav-trigger', q('header button').filter({ hasText: /^\s*About\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Nav trigger', desc: 'The About button that opens the header flyout; toggled, never followed.', sel: 'header button About' }, { noScroll: true });
  await S('cart-button', q('header button[aria-label="Cart"]').filter({ visible: true }).first(), B4, { group: g, title: 'Cart button', desc: 'The icon-only cart action; opens the cart drawer (a local toggle).', sel: 'header button[aria-label=Cart]' }, { noScroll: true });
  await S('account-button', q('header button:has([class*="account" i]), header button[class*="group flex items-center"]').filter({ hasText: /^\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Account button', desc: 'The icon-only account action that opens the login dialog; measured, never followed.', sel: 'header account icon button' }, { noScroll: true });
  // The About flyout opens on hover of its own trigger; keep the mouse put
  // (noReset) so the panel is still painted when it is read and cropped.
  try { await openAbout(); } catch (e) { log('  ! flyout hover failed', String(e.message).split('\n')[0]); }
  await S('nav-dropdown', q('header ul[class*="ml-44"]').locator('xpath=..').filter({ visible: true }).first(), ['default'], { group: g, title: 'Nav flyout', desc: 'The About flyout panel (link column plus the two image cards), opened by hovering its own trigger.', sel: 'header flyout panel' }, { noScroll: true, noReset: true });
  await S('menu-link', q('header ul a').filter({ hasText: /Knit Innovation|Responsibility|Creative Control/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Flyout link', desc: 'A link inside the opened About flyout.', sel: 'flyout link' }, { noScroll: true, noReset: true });
  await S('flyout-card', q('header ul[class*="ml-44"]').locator('xpath=..').locator('a').filter({ hasText: /Go to Textile Room/ }).filter({ visible: true }).first().locator('xpath=../..'), B4, { group: g, title: 'Flyout card', desc: 'An image card inside the About flyout (the card whose caption is "Go to Textile Room"); measured, never followed.', sel: 'flyout image card' }, { noScroll: true, noReset: true });
  await page.keyboard.press('Escape'); await page.waitForTimeout(400);
  const h = G.home;
  await S('hero-title', q('h1, h2, [class*="display-text" i]').filter({ hasText: /brand|stitch|DNA/i }).filter({ visible: true }).first(), ['default'], { group: h, title: 'Hero headline', desc: 'The "Your brand\'s DNA in every stitch" display headline over the dark hero media.', sel: 'display headline' });
  await S('hero-sub', page.locator('main :text("Made to match"), section :text("Made to match"), [class*="normal-text" i]:has-text("Made to match")').filter({ visible: true }).first(), ['default'], { group: h, title: 'Hero copy', desc: 'The lede under the hero headline (white on the dark hero media).', sel: 'hero lede' });
  await S('hero-cta', q('main a, main button, section a, section button, [class*="group"] a').filter({ hasText: /Explore samples/i }).filter({ visible: true }).first(), B4, { group: h, title: 'Hero CTA', desc: 'The "Explore samples →" action on the dark hero; measured, never followed.', sel: 'hero CTA' });
  await S('section-h2', q('main h1, main h2, section h1, section h2, [class*="display-text" i]').filter({ hasText: /reprogram|reimagine|rethink|textile innovation/i }).filter({ visible: true }).first(), ['default'], { group: h, title: 'Section heading', desc: 'A section display heading ("We reprogram tradition" / "BYBORRE is a textile innovation…").', sel: 'section display-text' });
  save();
}

async function collection() {
  if (!(await newPage('collection', { wait: 9000 }))) return;
  await sheetsFor('collection');
  await chrome('collection');
  const g = G.collection;
  await S('page-title', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Page title', desc: 'The "Textile Room" display title.', sel: 'h1' }, { noScroll: true });
  await S('filter-bar', q('div.sticky').filter({ hasText: /Select colors/i }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Filter bar', desc: 'The sticky colour-filter bar (Select colors, max 3) under the header.', sel: 'div.sticky filter bar' }, { noScroll: true });
  await S('colour-chip', q('input[name="color-select-Blue"]').locator('xpath=..').filter({ visible: true }).first(), B4, { group: g, title: 'Colour filter chip', desc: 'A colour-filter circle (the label wrapping a colour-select checkbox); a BLUE selection was toggled for the filtered screenshot state, never submitted.', sel: 'label colour chip' });
  await S('pattern-dropdown', q('button').filter({ hasText: /^\s*Pattern\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Pattern dropdown', desc: 'The Pattern filter trigger on the collection filter bar; measured closed, never opened.', sel: 'button Pattern' });
  await S('filter-toggle', q('button').filter({ hasText: /Show all filters/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Filter toggle', desc: 'The "Show all filters" expander on the filter bar; present in the DOM but rendered 0x0 at desktop width, so it records missing rather than a phantom measurement.', sel: 'button Show all filters' });
  await S('textile-card', q('main a[href*="/collection/"], a[href*="color="]').filter({ visible: true }).first(), B4, { group: g, title: 'Textile card', desc: 'A textile card in the Textile Room grid (name, price, Configure textile / Order actions); measured, never followed.', sel: 'a[href*="/collection/"]' });
  save();
}

async function textile() {
  if (!(await newPage('textile', { wait: 9000 }))) return;
  await sheetsFor('textile');
  await chrome('textile');
  const g = G.textile;
  await S('textile-title', q('h1, h2').filter({ visible: true }).first(), ['default'], { group: g, title: 'Textile name', desc: 'The textile product title.', sel: 'h1/h2' }, { noScroll: true });
  await S('view-tab', q('button').filter({ hasText: /^\s*(Sample|Textile repeat)\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Sample tab', desc: 'The Sample tab in the Configure-textile panel; the PHOTO/RENDER viewer toggle is a separate button captured as the render screenshot state.', sel: 'sample tab button' });
  await S('order-cta', q('button').filter({ hasText: /Order free sample|Order sample/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Order CTA', desc: 'The "Order free sample" action; measured, never pressed — it would mutate the cart.', sel: 'button Order sample' });
  await S('swatch', q('[class*="swatch" i], button.group.relative, label:has(input.sr-only)').filter({ visible: true }).first(), B4, { group: g, title: 'Colourway swatch', desc: 'A colourway selector (sr-only inputs behind swatch labels) on the detail page.', sel: 'colourway swatch' });
  await S('spec-row', q('[class*="detail" i] tr, dl div, [class*="spec" i] div').filter({ visible: true }).first(), ['default'], { group: g, title: 'Spec row', desc: 'A row in the Textile-details block (composition, weight, width).', sel: 'detail row' });
  save();
}

// Marks the login dialog (the smallest ancestor of the email input that holds
// the whole form) so it can be located and cropped without a class-name guess.
async function markDialog() {
  await page.evaluate(() => {
    const inp = document.querySelector('input[name="email"]');
    if (!inp) return;
    const vw = innerWidth, vh = innerHeight;
    const submitRe = /log ?in|sign ?in|continue/i;
    let n = inp.parentElement;
    while (n && n !== document.body) {
      const r = n.getBoundingClientRect();
      // The dialog is the first ancestor that wraps the form in a panel
      // smaller than the page itself (the backdrop/root are also ancestors
      // and carry the same text).
      if (/Log ?in to continue/i.test(n.innerText || '') && r.width > 300 && r.height > 200 && r.width < vw * 0.95 && r.height < vh * 0.98) {
        // Only accept an ancestor that also wraps the submit button, so the
        // crop covers the whole dialog rather than just the form column.
        const hasBtn = [...n.querySelectorAll('button, [role="button"], input[type="submit"], a')].some((x) => submitRe.test(x.innerText || x.value || ''));
        if (hasBtn) { n.setAttribute('data-m-mark', 'dlg'); return; }
        if (!n.getAttribute('data-m-mark')) n.setAttribute('data-m-mark', 'dlg-candidate');
      }
      n = n.parentElement;
    }
    // Fallback: mark the smallest candidate even if no submit was found inside.
    const cand = document.querySelector('[data-m-mark="dlg-candidate"]');
    if (cand) { cand.setAttribute('data-m-mark', 'dlg'); document.querySelectorAll('[data-m-mark="dlg-candidate"]').forEach((x) => x.removeAttribute('data-m-mark')); }
  });
}

async function login() {
  // /dashboard redirects signed-out visitors here and opens the login dialog.
  if (!(await newPage('login', { wait: 10000 }))) return;
  await sheetsFor('login');
  const g = G.login;
  await markDialog();
  await S('login-dialog', q('[data-m-mark="dlg"]'), ['default'], { group: g, title: 'Login dialog', desc: 'The "Log in to continue" dialog that gates the Design Studio; captured open, never filled or submitted.', sel: 'login dialog' }, { noScroll: true });
  await S('login-email', q('input[name="email"]').filter({ visible: true }).first(), ['default', 'focused', 'filled'], { group: g, title: 'Email field', desc: 'The login email input; focused and given sample text that was deleted again — nothing sent.', sel: 'input[name=email]' });
  await S('login-password', q('input[name="password"]').filter({ visible: true }).first(), ['default', 'focused'], { group: g, title: 'Password field', desc: 'The login password input; focused only, never typed into.', sel: 'input[name=password]' });
  await S('login-button', q('button').filter({ hasText: /^\s*(Log ?in|Login)\s*$/i }).filter({ visible: true }).last(), B4, { group: g, title: 'Login button', desc: 'The dialog\'s Login action; measured, never pressed.', sel: 'login submit' });
  await S('signup-link', q('a, button').filter({ hasText: /^\s*Sign up\s*$/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Sign-up link', desc: 'The "Don\'t have an account? Sign up" link; measured, never followed.', sel: 'sign up link' });
  await S('forgot-link', q('a, button').filter({ hasText: /Forgot password/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Forgot-password link', desc: 'The forgot-password link inside the dialog; measured, never followed.', sel: 'forgot password link' });
  save();
}

async function faq() {
  if (!(await newPage('faq', { wait: 8000 }))) return;
  await sheetsFor('faq');
  const g = G.faq;
  await S('faq-title', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'FAQ title', desc: 'The FAQ page title and a section heading (Textile information).', sel: 'h1' }, { noScroll: true });
  await S('faq-question', q('button').filter({ hasText: /\?\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'FAQ question', desc: 'An accordion question row; toggled open for the opened state and the screenshot.', sel: 'button question' });
  save();
}

async function contact() {
  if (!(await newPage('contact', { wait: 9000 }))) return;
  await sheetsFor('contact');
  const g = G.contact;
  await S('contact-title', q('h1').filter({ hasText: /Contact us|create together/i }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Contact title', desc: 'The "Contact us" heading.', sel: 'h1' }, { noScroll: true });
  await S('text-field', q('input[name="firstname"]').filter({ visible: true }).first(), ['default', 'focused', 'filled'], { group: g, title: 'Text field', desc: 'The First-name input; focused and given sample text that was deleted again — nothing sent.', sel: 'input[name=firstname]' }, { fillText: 'Sample' });
  await S('email-field', q('input[name="email"]').filter({ visible: true }).first(), ['default', 'focused'], { group: g, title: 'Email field', desc: 'The Email input on the contact form; focused only.', sel: 'input[name=email]' });
  await S('select-field', q('select[name="inquiry"], select').filter({ visible: true }).first(), ['default', 'focused'], { group: g, title: 'Select', desc: 'The inquiry-type select; focused only, never changed.', sel: 'select[name=inquiry]' });
  await S('text-area', q('textarea[name="project_description"], textarea').filter({ visible: true }).first(), ['default', 'focused'], { group: g, title: 'Text area', desc: 'The project-description textarea; focused only, never typed into.', sel: 'textarea' });
  await S('submit-button', q('button[type="submit"], button').filter({ hasText: /Send|Submit/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Submit button', desc: 'The form\'s Send action; measured, never pressed.', sel: 'form submit' });
  await S('person-card', q('[class*="card" i], div').filter({ hasText: /Jan Maarten|Erik-Jan|Anna Maria/ }).filter({ visible: true }).last(), ['default'], { group: g, title: 'Contact person', desc: 'A named contact block (name, role) on the contact page.', sel: 'contact person block' });
  save();
}

async function footer() {
  if (!(await newPage('home', { wait: 6000 }))) return;
  const g = G.footer;
  await page.evaluate(() => scrollTo(0, document.documentElement.scrollHeight));
  await page.waitForTimeout(1500);
  await S('footer', q('footer').filter({ visible: true }).last(), ['default'], { group: g, title: 'Footer', desc: 'The page footer: link columns, social links, legal and newsletter copy.', sel: 'footer' }, { noScroll: true });
  await S('footer-link', q('footer a').filter({ hasText: /\S/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Footer link', sel: 'footer a' }, { noScroll: true });
  await S('social-icon', q('footer a[href*="instagram"], footer a[href*="linkedin"]').filter({ visible: true }).first(), B4, { group: g, title: 'Social link', desc: 'A social link in the footer.', sel: 'footer social a' }, { noScroll: true });
  save();
}

async function mobile() {
  if (!(await newPage('mobile', { mobile: true, url: BASE + '/' }))) return;
  await chrome('mobile');
  const g = G.mobile;
  await S('m-header', q('header').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile header', sel: 'header at 390' }, { noScroll: true });
  const menu = q('header button[aria-label="Open menu"], header button').filter({ has: q('[class*="menu" i], svg') }).filter({ visible: true }).last();
  const menuBtn = q('header button[aria-label="Open menu"]').first();
  const t = (await menuBtn.count()) ? menuBtn : menu;
  await S('m-menu-button', t, ['default'], { group: g, title: 'Menu button', desc: 'The burger toggle that opens the mobile menu.', sel: 'button[aria-label=Open menu]' }, { noScroll: true });
  try {
    if (await t.count()) { await t.click({ timeout: 5000 }).catch(() => t.evaluate((el) => el.click())); await page.waitForTimeout(1500); }
  } catch (e) { log('  ! mobile menu toggle failed', String(e.message).split('\n')[0]); }
  await S('m-menu-open', q('aside.fixed, aside[class*="inset-x-0"]').filter({ hasText: /Textile Room|Design Studio/ }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile menu, open', desc: 'The opened mobile menu panel (the aside that slides over the page).', sel: 'aside mobile menu' }, { noScroll: true });
  await S('m-nav-item', q('aside a').filter({ hasText: /Textile Room|Design Studio|Contact/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Mobile nav item', desc: 'A link inside the opened mobile menu.', sel: 'mobile menu a' }, { noScroll: true });
  await S('m-login-button', q('aside a, aside button').filter({ hasText: /Login|Sign-up/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Mobile login button', desc: 'The Login/Sign-up row inside the mobile menu; opens the login dialog, measured never followed.', sel: 'mobile menu login row' }, { noScroll: true });
  await page.keyboard.press('Escape'); await page.waitForTimeout(500);
  await S('m-hero', q('h1, h2, [class*="display-text" i]').filter({ hasText: /brand|stitch|DNA/i }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile headline', sel: 'display headline at 390' });
  save();
}

run = new Date().toISOString().slice(0, 10);
out._meta.read = run;
out._meta.viewport = '1440 x 900 (mobile group 390 x 844); the public surface paints light throughout';
out._meta.tool = 'tools/capture/public/measure.mjs';
const { browser, context: ctx0 } = await launch();
context = ctx0;
const pages = process.argv.slice(2);
const plan = { home, collection, textile, login, faq, contact, mobile };
const order = Object.keys(plan).filter((k) => !pages.length || pages.includes(k));
try {
  for (const k of order) { if (k !== 'mobile') await plan[k](); }
  if (!pages.length || pages.includes('home')) await footer();
  if (!pages.length || pages.includes('mobile')) await plan.mobile();
  // Reduced-motion check on an element that actually moves (the marquee's
  // translate animation), so the delta is meaningful.
  if (!pages.length || pages.includes('home')) await reducedMotion('home', 'div[class*="animate-marquee"], div[class*="marquee" i]');
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
