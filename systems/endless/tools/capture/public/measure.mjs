// Measures endless.app's public components in every state reachable without
// signing in, sending, generating or paying for anything.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node measure.mjs [page ...]
//
// Pages: home pricing contact toolgen models radar brand blog docs mcp mobile.
// Writes raw/components-computed.json (merged) and one crop per component and
// state into components/crops/; raw/measurements.md is built by
// build-measurements.mjs.
//
// endless.app (what endless.io redirects to) is one Next.js surface: the
// marketing pages, the free-tool pages, the model catalog, the radar trends,
// /docs (a docs shell) and /brand. Its shadcn-style token layer resolves on
// :root and re-binds under .dark. Nothing is sent, signed into or generated:
// the only presses are local UI toggles — the Annual billing toggle, the
// mobile menu — and fields clicked into or typed
// and deleted (nothing sent). Sign-in (clerk.endless.app) and sign-up
// (s.endless.app) are out of scope and never followed; Send message, Generate
// and every plan CTA are measured, never pressed.
import fs from 'node:fs';
import path from 'node:path';
import { BASE, M, launch, patch, open, closePromo, domFind, styleOf, crop, centre, RAW, UA, UA_MOBILE } from './lib.mjs';

const OUT = process.env.OUT_JSON || path.join(RAW, 'components-computed.json');
const out = fs.existsSync(OUT) ? JSON.parse(fs.readFileSync(OUT, 'utf8')) : {};
out._meta ??= {};
out.components ??= {};
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const save = () => fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');
const URLS = { home: '/', pricing: '/pricing', contact: '/contact', toolgen: '/tools/ai-image-generator', models: '/models', radar: '/radar', brand: '/brand', blog: '/blog', docs: '/docs', mcp: '/mcp' };
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

async function newPage(key, { mobile = false, wait = 8000, promo = 'close', url = null, colorScheme = 'light' } = {}) {
  current = key;
  // Close the previous page's context before opening the next: leaving them
  // alive keeps every captured page (and its animations) running in the
  // background for the rest of the run.
  if (liveCtx) { await liveCtx.close().catch(() => {}); liveCtx = null; }
  const b = context.browser();
  const ctx = liveCtx = await b.newContext(mobile
    ? { viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, userAgent: UA_MOBILE, isMobile: true, hasTouch: true, locale: 'en-US', colorScheme }
    : { viewport: { width: 1440, height: 900 }, deviceScaleFactor: 2, userAgent: UA, locale: 'en-US', colorScheme });
  await patch(ctx);
  page = await ctx.newPage();
  cdp = await ctx.newCDPSession(page);
  await cdp.send('DOM.enable');
  await cdp.send('CSS.enable');
  page.setDefaultTimeout(8000);
  log('open', key, mobile ? '(mobile)' : '', colorScheme === 'dark' ? '(dark)' : '');
  const cleared = await open(page, url || BASE + URLS[key], { wait, promo });  // false: the bot check did not clear (lib.mjs)
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

// Clicks a UI toggle (dropdown, menu, tab, radio). Refuses a submit button and
// any control whose text names an action this kit must never take.
const NEVER = /^(send|send message|submit|sign in|log ?in|login|sign up|create|generate|generate the image|add|download|buy|purchase|pay|checkout|join|subscribe|save|apply|accept|reject|start|start free|get started|claim|share|export|continue|claim this offer|try again|next|confirm|book|book a call|i understand|decline|copy|download svg|download png|download json|copy svg|copy citation)$/i;
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

// Marks the nearest ancestor of the element matching sel that paints a fill
// or a background image, or falls back to marking a painted descendant.
async function markPainted(sel, tag, { maxUp = 8, minW = 100, minH = 60, maxW = 1e5, maxH = 1e5, descend = false } = {}) {
  const ok = await page.evaluate(([s, t, up, w, h, W, H, desc]) => {
    document.querySelectorAll(`[data-m-mark="${t}"]`).forEach((n) => n.removeAttribute('data-m-mark'));
    const el = [...document.querySelectorAll(s)].find((n) => { const r = n.getBoundingClientRect(); return r.width > 0 && r.height > 0; });
    if (!el) return false;
    const paints = (cs) => cs.backgroundColor !== 'rgba(0, 0, 0, 0)' || cs.backgroundImage !== 'none';
    if (!desc) for (let n = el, i = 0; n && i < up; n = n.parentElement, i++) {
      const cs = getComputedStyle(n);
      const r = n.getBoundingClientRect();
      if (r.width >= w && r.height >= h && r.width <= W && r.height <= H && paints(cs)) { n.setAttribute('data-m-mark', t); return true; }
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
  }, [sel, tag, maxUp, minW, minH, maxW, maxH, descend]);
  return ok ? page.locator(`[data-m-mark="${tag}"]`) : page.locator('[data-m-mark="__none__"]');
}

const G = {
  shell: 'Shell and navigation', hero: 'Home hero', home: 'Home', pricing: 'Pricing',
  contact: 'Contact form', toolgen: 'AI image generator (free tool)',
  models: 'Model catalog', radar: 'Radar trends', brand: 'Brand kit',
  docs: 'Docs shell', mcp: 'MCP page', blog: 'Blog',
  footer: 'Footer', mobile: 'Mobile (390 wide)', darkp: 'Dark theme (system dark)',
};

async function home() {
  if (!(await newPage('home'))) return;
  await sheetsFor('home');
  await chrome('home');
  const g = G.shell;
  await S('header', q('header').filter({ visible: true }).first(), ['default'], { group: g, title: 'Header', desc: 'The sticky 56px marketing header: logo mark, flat nav links, Sign in and the Sign-up-for-free pill.', sel: 'header.home-marketing-header' }, { noScroll: true });
  await S('logo', q('header a[href="/"], header a').filter({ visible: true }).first(), B4, { group: g, title: 'Logo', desc: 'The Endless mark anchor.', sel: 'header a:first' }, { noScroll: true });
  // The desktop header is flat links: Product, Models, Industries, Pricing, Blog.
  // There is no dropdown menu at 1440px — nav-dropdown and menu-link record the
  // absence below; the mobile run measures the opened menu at 390px.
  await S('nav-industries', q('header a').filter({ hasText: /^\s*Industries\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Nav link — Industries', desc: 'The Industries header link (a plain link, not a dropdown trigger).', sel: 'header a "Industries"' }, { noScroll: true });
  await S('nav-link', q('header a').filter({ hasText: /^\s*Pricing\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Nav link', desc: 'The plain Pricing header link.', sel: 'header a "Pricing"' }, { noScroll: true });
  await S('nav-signin', q('header button, header a').filter({ hasText: /^\s*Sign in\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Sign-in button', desc: 'The Sign-in control (goes to clerk.endless.app; measured, never followed).', sel: '"Sign in"' }, { noScroll: true });
  await S('nav-cta', q('header a, header button').filter({ hasText: /Sign up for free/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Sign-up CTA', desc: 'The dark Sign-up-for-free pill (goes to s.endless.app; measured, never followed).', sel: '"Sign up for free"' }, { noScroll: true });
  await S('nav-dropdown', q('header [class*="panel" i], header [class*="dropdown" i], [role="menu"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Nav dropdown', desc: 'No dropdown exists on the desktop header — recorded missing.', sel: 'header dropdown panel' }, { noScroll: true, noReset: true });
  await S('menu-link', q('header a, [role="menu"] a, [role="dialog"] a').filter({ hasText: /agencies|brands|education|media|newsroom/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Menu link', desc: 'No dropdown menu on the desktop header — recorded missing.', sel: 'industries menu a' }, { noScroll: true });
  const h = G.hero;
  await S('hero-title', q('h1').filter({ visible: true }).first(), ['default'], { group: h, title: 'Hero headline', desc: 'The home display headline.', sel: 'h1' }, { noScroll: true });
  await S('hero-lede', q('p.home-intro').filter({ visible: true }).first(), ['default'], { group: h, title: 'Hero copy', desc: 'The lede under the headline.', sel: 'p.home-intro' });
  // markPainted returns the __none__ locator on a miss (S records it missing), never null.
  const comp0 = await markPainted('textarea', 'm-composer', { minW: 200, minH: 40 });
  await S('composer', comp0, ['default'], { group: h, title: 'Prompt composer', desc: 'The painted Ask-Endless prompt box (the hero\'s chat composer). Its send control is never pressed.', sel: 'painted ancestor of the hero textarea' });
  await S('composer-input', q('textarea').filter({ visible: true }).first(), ['default', 'focused', 'filled'], { group: h, title: 'Composer input', desc: 'The "Ask Endless…" textarea; sample text was typed and deleted, nothing sent.', sel: 'textarea' }, { fillText: 'A launch post for the winter drop' });
  // Not `form button`: that union caught the composer's "Add to prompt" attach
  // button first. Only a submit or a send-labelled control counts; anything
  // else is recorded missing. (Edited after the last run; not re-run.)
  await S('composer-send', q('button[type="submit"], button[aria-label*="send" i]').filter({ hasNotText: /add to prompt/i }).filter({ visible: true }).first(), B4, { group: h, title: 'Composer send', desc: 'The send/generate control inside the composer; measured, never pressed.', sel: 'composer send button' });
  await S('mode-pill', q('button').filter({ hasText: /Terra|GPT|Claude|Gemini|model/i }).filter({ visible: true }).first(), B4, { group: h, title: 'Model pill', desc: 'The model-picker pill on the composer ("GPT-6.1 Terra" on this pass).', sel: 'model picker button' });
  await S('prompt-chip', q('button, a').filter({ hasText: /Account analysis|Launch post|Product video/i }).filter({ visible: true }).first(), B4, { group: h, title: 'Prompt chip', desc: 'A suggestion chip under the composer; measured, never pressed.', sel: 'prompt suggestion chip' });
  const s = G.home;
  await S('h2-section', q('h2').filter({ visible: true }).first(), ['default'], { group: s, title: 'Section heading', desc: 'A home section heading.', sel: 'h2' });
  save();
}

async function pricing() {
  if (!(await newPage('pricing', { wait: 10000 }))) return;
  await sheetsFor('pricing');
  await chrome('pricing');
  const g = G.pricing;
  await S('pricing-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Pricing title', desc: 'The pricing page heading.', sel: 'h1 on /pricing' }, { noScroll: true });
  await S('billing-toggle', q('button').filter({ hasText: /^\s*(Monthly|Annual)\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Billing toggle', desc: 'The Monthly/Annual billing segment, read on its Monthly button at rest (Annual was pressed only for the pricing-*-annual screenshots, by public.mjs); never checked out.', sel: 'button "Monthly" or "Annual", first' }, { noScroll: true });
  await S('plan-name', q('h2, h3').filter({ hasText: /^\s*(Free|Pro|Team|Business|Enterprise|Creator)\s*$/i }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Plan name', desc: 'A plan card\'s name.', sel: 'plan name heading' });
  await S('plan-price', q('span, div, p').filter({ hasText: /^\s*(US)?\$\d+/ }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Plan price', desc: 'A plan card\'s price figure.', sel: 'plan price' });
  await S('plan-cta', q('button, a').filter({ hasText: /^\s*(Get started|Start free)\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Plan CTA', desc: 'A plan card\'s action; measured never followed (sign-up goes to s.endless.app).', sel: 'plan CTA button' });
  const planCard = await markPainted('h2, h3', 'm-plan', { minW: 220, minH: 200 });
  await S('plan-card', planCard, ['default'], { group: g, title: 'Plan card', desc: 'A pricing plan card (the painted ancestor of the plan name).', sel: 'plan card' });
  await S('credits-slider', q('input[type="range"]').filter({ visible: true }).first(), ['default', 'focused'], { group: g, title: 'Credits slider', desc: 'The shared-credits range input on /pricing; focused only, never dragged.', sel: 'input[type=range]' });
  await S('faq-item', q('button, summary, [role="button"]').filter({ hasText: /\?\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'FAQ row', desc: 'A pricing FAQ accordion row; measured closed, never opened.', sel: 'faq row' });
  save();
}

async function contact() {
  if (!(await newPage('contact', { wait: 9000 }))) return;
  await sheetsFor('contact');
  await chrome('contact');
  const g = G.contact;
  // The form is an unpainted 640px column over the page field; the inputs
  // paint their own translucent fills. The <form> element is the boundary.
  await S('contact-form', q('form').filter({ visible: true }).first(), ['default'], { group: g, title: 'Contact form', desc: 'The contact/sales form (an unpainted 640px column; the fields paint their own fills); never submitted.', sel: 'form' });
  await S('field-name', q('input[type="text"], input').filter({ visible: true }).first(), ['default', 'focused', 'filled'], { group: g, title: 'Name field', desc: 'A text input on the contact form; sample text typed and deleted, nothing sent.', sel: 'input[type=text]' }, { fillText: 'Ada Lovelace' });
  await S('field-email', q('input[type="email"]').filter({ visible: true }).first(), ['default', 'focused', 'filled'], { group: g, title: 'Email field', desc: 'The email input; sample text typed and deleted, nothing sent.', sel: 'input[type=email]' });
  await S('field-company', q('input[placeholder*="acme" i], input[name*="compan" i], input[name*="domain" i]').filter({ visible: true }).first(), ['default', 'focused'], { group: g, title: 'Company field', desc: 'The company/domain input ("acme.com" placeholder); focused only.', sel: 'input[placeholder*=acme]' });
  await S('field-message', q('textarea').filter({ visible: true }).first(), ['default', 'focused'], { group: g, title: 'Message field', desc: 'The message textarea; focused only, nothing typed.', sel: 'contact textarea' });
  await S('send-btn', q('button').filter({ hasText: /Send message|Send/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Send button', desc: 'The Send-message submit; measured, never pressed.', sel: 'button "Send message"' });
  save();
}

async function toolgen() {
  if (!(await newPage('toolgen', { wait: 9000 }))) return;
  await sheetsFor('toolgen');
  await chrome('toolgen');
  const g = G.toolgen;
  await S('tool-title', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Tool title', desc: 'The free-tool page heading (AI image generator).', sel: 'h1' }, { noScroll: true });
  const card = await markPainted('input', 'm-tool', { minW: 250, minH: 60 });
  await S('tool-panel', card, ['default'], { group: g, title: 'Tool panel', desc: 'The prompt panel of the free tool; Generate is never pressed.', sel: 'tool panel' });
  await S('tool-prompt', q('input').filter({ visible: true }).first(), ['default', 'focused', 'filled'], { group: g, title: 'Prompt field', desc: 'The tool\'s prompt input ("e.g. a fox reading a map…" placeholder); sample text typed and deleted, nothing generated.', sel: 'tool prompt input' }, { fillText: 'a fox reading a map in a snowy forest' });
  await S('tool-generate', q('button').filter({ hasText: /Generate the image|Generate/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Generate button', desc: 'The Generate-the-image submit; measured, never pressed.', sel: 'button "Generate the image"' });
  await S('tool-step', q('h2, h3').filter({ hasText: /how|step|describe|generate|download/i }).filter({ visible: true }).first(), ['default'], { group: g, title: 'How-it-works heading', desc: 'A how-it-works heading on the tool page.', sel: 'tool h2' });
  save();
}

async function models() {
  if (!(await newPage('models', { wait: 9000 }))) return;
  await sheetsFor('models');
  await chrome('models');
  const g = G.models;
  await S('models-title', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Models title', desc: 'The model catalog heading.', sel: 'h1' }, { noScroll: true });
  await S('models-search', q('input[type="search"], input[placeholder*="search" i]').filter({ visible: true }).first(), ['default', 'focused', 'filled'], { group: g, title: 'Search field', desc: 'The catalog search input; sample text typed and deleted.', sel: 'input[type=search]' }, { fillText: 'image' });
  await S('mode-tab', q('button, a').filter({ hasText: /·\s*\d+/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Modality tab', desc: 'A modality filter pill ("All · 65", "Chat · 21", …); measured, never toggled.', sel: 'modality filter pill' });
  await S('model-card', q('a[href*="/models/"]').filter({ has: page.locator('h2, h3') }).filter({ visible: true }).first(), B4, { group: g, title: 'Model card', desc: 'A model tile in the catalog grid (the anchor is the card; 354x200, rounded 20px); measured, never followed.', sel: 'a[href*=/models/] with a heading' });
  await S('model-link', q('a[href*="/models/"]').filter({ hasText: /\S/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Model link', desc: 'A model name link in the catalog; measured, never followed.', sel: 'a[href*=/models/]' });
  save();
}

async function radar() {
  if (!(await newPage('radar', { wait: 10000 }))) return;
  await sheetsFor('radar');
  await chrome('radar');
  const g = G.radar;
  await S('radar-title', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Radar title', desc: 'The social radar heading.', sel: 'h1' }, { noScroll: true });
  await S('radar-search', q('input[type="search"], input[placeholder*="Search" i], input').filter({ visible: true }).first(), ['default', 'focused'], { group: g, title: 'Radar search', desc: 'No search input exists on /radar — recorded missing.', sel: 'radar search input' });
  // Scope to links inside <main> that point at a trend detail — the earlier
  // page-wide `ul a` matched the header's own nav list and measured the
  // Industries link as a "trend row".
  await S('radar-row', q('main a[href*="/radar/trends/"], main a[href*="/radar/tiktok/"], main a[href*="/radar/"]').filter({ hasText: /#\w+|[A-Za-zÀ-ÿ]{4,}/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Trend row', desc: 'A trend row in the live radar list (a link to a trend detail page); measured, never followed.', sel: 'main a[href*=/radar/] trend link' });
  await S('radar-copy', q('button').filter({ hasText: /^\s*Copy\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Copy button', desc: 'A trend Copy button; measured, never pressed.', sel: 'button "Copy"' });
  await S('radar-why', q('button, a').filter({ hasText: /Find out why/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Why link', desc: 'A trend\'s Find-out-why action; measured, never followed.', sel: '"Find out why"' });
  save();
}

async function brand() {
  if (!(await newPage('brand', { wait: 9000 }))) return;
  await sheetsFor('brand');
  await chrome('brand');
  const g = G.brand;
  await S('brand-title', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Brand title', desc: 'The brand-kit heading.', sel: 'h1' }, { noScroll: true });
  await S('brand-logo-block', q('main [class*="bg-card"], main [class*="rounded-2xl"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Logo block', desc: 'A logo asset card on the brand page (a rounded-2xl bg-card tile with On-light/On-dark variants and SVG/PNG download links).', sel: 'main .bg-card' });
  await S('brand-swatch', q('main [class*="swatch" i]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Colour swatch', desc: 'A brand colour swatch tile in the Colors section (285x174; the page names #0A0A0A, #FAFAFA, #01BCFF).', sel: 'main .swatch' });
  await S('brand-btn', q('main a, main button').filter({ hasText: /Download SVG|Download PNG|Download all assets/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Asset button', desc: 'An asset Download link; measured, never pressed.', sel: 'brand asset download link' });
  save();
}

async function blog() {
  if (!(await newPage('blog', { wait: 9000 }))) return;
  await sheetsFor('blog');
  await chrome('blog');
  const g = G.blog;
  await S('blog-title', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Blog title', desc: 'The blog index heading.', sel: 'h1' }, { noScroll: true });
  await S('blog-pill', q('button, a').filter({ hasText: /^\s*(All|Guides|Customer stories)\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Category pill', desc: 'A blog category filter pill; measured, never toggled.', sel: 'category pill' });
  const card = await markPainted('article a, a[href*="/blog/"]', 'm-post', { minW: 150, minH: 100 });
  await S('blog-card', card, B4, { group: g, title: 'Post card', desc: 'A post card in the blog index; measured, never followed.', sel: 'post card' });
  save();
}

async function docs() {
  if (!(await newPage('docs', { wait: 9000 }))) return;
  await sheetsFor('docs');
  await chrome('docs');
  const g = G.docs;
  await S('docs-sidebar', q('aside, nav').filter({ hasText: /Get started|Concepts/ }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Docs sidebar', desc: 'The docs navigation sidebar — a separate shell from the marketing pages.', sel: 'docs aside' }, { noScroll: true });
  await S('docs-nav-item', q('aside button, aside a, nav button, nav a').filter({ hasText: /^\s*(Get started|Concepts|Chat|Create)\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Docs nav item', desc: 'A sidebar section button in the docs shell; measured, never toggled.', sel: 'docs nav item' }, { noScroll: true });
  await S('docs-search', q('button').filter({ hasText: /Search/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Search button', desc: 'The docs Search (⌘K) button; measured, never opened.', sel: 'docs search button' }, { noScroll: true });
  await S('docs-h1', q('main h1, h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Docs heading', desc: 'The docs page heading in the docs typeset.', sel: 'docs h1' });
  save();
}

async function mcp() {
  if (!(await newPage('mcp', { wait: 9000 }))) return;
  await sheetsFor('mcp');
  await chrome('mcp');
  const g = G.mcp;
  await S('mcp-title', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'MCP title', desc: 'The MCP page heading.', sel: 'h1' }, { noScroll: true });
  await S('mcp-code', q('pre, code').filter({ visible: true }).first(), ['default'], { group: g, title: 'Code block', desc: 'An install/config code block (monospace surface).', sel: 'pre code' });
  await S('mcp-copy', q('button').filter({ hasText: /^\s*Copy\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Copy button', desc: 'A code Copy button; measured, never pressed.', sel: 'button "Copy"' });
  save();
}

async function footer() {
  if (!(await newPage('home', { wait: 6000 }))) return;
  const g = G.footer;
  await page.evaluate(() => scrollTo(0, document.documentElement.scrollHeight));
  await page.waitForTimeout(1500);
  await S('footer', q('footer').filter({ visible: true }).last(), ['default'], { group: g, title: 'Footer', desc: 'The marketing footer: link columns, legal, the Cookie-settings and Theme controls.', sel: 'footer' }, { noScroll: true });
  await S('footer-link', q('footer a').filter({ hasText: /\S/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Footer link', sel: 'footer a' }, { noScroll: true });
  await S('theme-toggle', q('footer button[aria-label*="Theme"], footer button[title*="Switch to"]').filter({ visible: true }).first(), B4, { group: g, title: 'Theme toggle', desc: 'The footer Theme icon control ("Theme: system. Switch to light"; writes the .dark class the system scheme also drives); measured, never pressed.', sel: 'footer theme icon button' }, { noScroll: true });
  await S('cookie-btn', q('footer button').filter({ hasText: /Cookie settings/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Cookie settings button', desc: 'The footer Cookie-settings button; measured, never pressed (a consent surface).', sel: '"Cookie settings"' }, { noScroll: true });
  save();
}

// A small dark pass: the same components re-read under emulated
// prefers-color-scheme dark, which the site honours with its .dark class —
// evidence that the dark token set genuinely paints, not a reconstruction.
async function darkp() {
  if (!(await newPage('home', { wait: 8000, colorScheme: 'dark' }))) return;
  const g = G.darkp;
  const themed = await page.evaluate(() => ({ cls: document.documentElement.className, scheme: getComputedStyle(document.documentElement).colorScheme, bg: getComputedStyle(document.body).backgroundColor }));
  out._meta.darkProbe = themed;
  await S('d-header', q('header').filter({ visible: true }).first(), ['default'], { group: g, title: 'Header (dark)', desc: 'The sticky header painted by the dark token scope.', sel: 'header under .dark' }, { noScroll: true });
  await S('d-nav-cta', q('header a, header button').filter({ hasText: /Sign up for free/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Sign-up CTA (dark)', desc: 'The sign-up pill under .dark.', sel: '"Sign up for free" under .dark' }, { noScroll: true });
  await S('d-hero-title', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Hero headline (dark)', desc: 'The display headline under .dark.', sel: 'h1 under .dark' }, { noScroll: true });
  await S('d-composer-input', q('textarea').filter({ visible: true }).first(), ['default', 'focused'], { group: g, title: 'Composer input (dark)', desc: 'The Ask-Endless textarea under .dark; focused, nothing typed or sent.', sel: 'textarea under .dark' });
  await S('d-nav-link', q('header a').filter({ hasText: /^\s*Pricing\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Nav link (dark)', desc: 'A header link under .dark.', sel: 'header a "Pricing" under .dark' }, { noScroll: true });
  save();
}

async function mobile() {
  if (!(await newPage('mobile', { mobile: true, url: BASE + '/' }))) return;
  await chrome('mobile');
  const g = G.mobile;
  await S('m-header', q('header').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile header', sel: 'header at 390' }, { noScroll: true });
  const menu = q('header button').filter({ visible: true }).last();
  await S('m-menu-button', menu, ['default'], { group: g, title: 'Menu button', desc: 'The header menu toggle.', sel: 'header menu button' }, { noScroll: true });
  try {
    if (await menu.count()) { await menu.click({ timeout: 5000 }).catch(() => menu.evaluate((el) => el.click())); await page.waitForTimeout(1500); }
  } catch (e) { log('  ! mobile menu toggle failed', String(e.message).split('\n')[0]); }
  await S('m-menu-open', q('[class*="fixed"][class*="inset-0"], [role="dialog"], header + div').filter({ hasText: /Industries|Pricing|Tools/ }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile menu, open', desc: 'The header menu panel opened by its own toggle.', sel: 'mobile menu panel' }, { noScroll: true });
  // Items must come from the opened menu panel itself — the earlier selector
  // included `body a` and measured a footer Pricing link at y≈9940, outside
  // the menu, where hover fails and focus cannot be held.
  await S('m-nav-item', q('[class*="fixed"][class*="inset-0"] a, [class*="fixed"][class*="inset-0"] button, [role="dialog"] a, [role="dialog"] button').filter({ hasText: /^\s*(Industries|Pricing|Tools|Models|Blog|Docs)\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Mobile nav item', desc: 'An item inside the opened header menu.', sel: 'mobile menu item' }, { noScroll: true });
  await page.keyboard.press('Escape'); await page.waitForTimeout(500);
  await S('m-hero', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile headline', sel: 'h1 at 390' });
  await S('m-composer', q('textarea').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile composer', sel: 'textarea at 390' });
  save();
}

// A page argument that matches no page fails loudly before anything is
// rewritten: a misspelt one used to run nothing yet stamp _meta.read with
// today's date, so stale readings looked fresh.
const plan = { home, pricing, contact, toolgen, models, radar, brand, blog, docs, mcp, darkp, mobile };
const pages = process.argv.slice(2);
const unknown = pages.filter((p) => !Object.hasOwn(plan, p));
if (unknown.length) {
  console.error(`unknown page argument(s): ${unknown.join(', ')} — known pages: ${Object.keys(plan).join(', ')}`);
  process.exit(1);
}
run = new Date().toISOString().slice(0, 10);
out._meta.read = run;
out._meta.viewport = '1440 x 900 (mobile group 390 x 844); every page paints light on a light system and dark on a dark system via next-themes .dark (the dark group was measured under emulated prefers-color-scheme dark)';
out._meta.tool = 'tools/capture/public/measure.mjs';
const { browser, context: ctx0 } = await launch();
context = ctx0;
const order = Object.keys(plan).filter((k) => !pages.length || pages.includes(k));
try {
  for (const k of order) { if (k !== 'mobile' && k !== 'darkp') await plan[k](); }
  if (!pages.length || pages.includes('home')) await footer();
  if (!pages.length || pages.includes('darkp')) await plan.darkp();
  if (!pages.length || pages.includes('mobile')) await plan.mobile();
  // Reduced-motion check on an element that transitions (the sticky header),
  // so the delta is meaningful.
  if (!pages.length || pages.includes('home')) await reducedMotion('home', 'header');
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
