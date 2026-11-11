// Measures butter.video's public components in every state reachable without
// signing in, subscribing or submitting anything.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node measure.mjs [page ...]
//
// Pages: home pricing explore mobile.
// Writes raw/components-computed.json (merged) and one crop per component and
// state into components/crops/; raw/measurements.md is built by
// build-measurements.mjs.
//
// butter.video is a Next.js marketing app (styled-components, index-style__*
// classes) whose /explore, /blocks and /templates pages hand off to a dark MUI
// app shell (MuiButtonBase/css-* classes) that is public signed-out. Nothing
// is sent, bought or signed into: the only presses are local UI toggles — the
// nav dropdown, the billing period buttons and the mobile menu. The iubenda
// consent banner is hidden, never answered.
import fs from 'node:fs';
import path from 'node:path';
import { BASE, M, launch, patch, open, closePromo, domFind, styleOf, crop, centre, RAW, UA, UA_MOBILE } from './lib.mjs';

const OUT = process.env.OUT_JSON || path.join(RAW, 'components-computed.json');
const out = fs.existsSync(OUT) ? JSON.parse(fs.readFileSync(OUT, 'utf8')) : {};
out._meta ??= {};
out.components ??= {};
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const save = () => fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');
const URLS = { home: '/', pricing: '/pricing', explore: '/explore' };
let page, cdp, current, context, run, liveCtx;
const touched = new Set();
const listed = new Map();
// Routes PerimeterX gates this run: components last measured on them keep their
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
const NEVER = /^(send|submit|sign in|log ?in|login|create|add|download|buy|purchase|pay|checkout|join|subscribe|save|apply|accept|reject|start|get started|claim|share|export|select|continue|claim this offer|try again)$/i;
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

const G = {
  shell: 'Shell and navigation', home: 'Home', pricing: 'Pricing',
  app: 'App shell (dark)', footer: 'Footer', mobile: 'Mobile (390 wide)',
};

async function home() {
  if (!(await newPage('home'))) return;
  await sheetsFor('home');
  await chrome('home');
  const g = G.shell;
  await S('header', q('header[class*="HeaderContainer"], header').filter({ visible: true }).first(), ['default'], { group: g, title: 'Header', desc: 'The marketing header: wordmark, the Co-Create/Product dropdown, plain links, Login and the Try-for-free pill.', sel: 'header.index-style__HeaderContainer' }, { noScroll: true });
  await S('logo', q('header a[href="/"]:has(svg), header a:has(svg)').filter({ visible: true }).first(), ['default'], { group: g, title: 'Logo', desc: 'The wordmark anchor (an unclassed <a> wrapping the Butter svg).', sel: 'header a:has(svg)' }, { noScroll: true });
  await S('nav-link', q('header nav a, header a').filter({ hasText: /^(Pricing|Blog)/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Nav link', desc: 'A plain header link (Pricing/Blog).', sel: 'header nav a' }, { noScroll: true });
  await S('nav-cta', q('header a').filter({ hasText: /Try for free/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Nav CTA', desc: 'The Try-for-free header action; links to /explore, measured never followed.', sel: 'header a Try for free' }, { noScroll: true });
  await S('nav-trigger', q('button[class*="CoCreateTrigger"], header button').filter({ visible: true }).first(), B4, { group: g, title: 'Nav trigger', desc: 'The Co-Create button that opens the header dropdown; toggled, never followed.', sel: 'button.CoCreateTrigger' }, { noScroll: true });
  // The header dropdown opens on hover of the Product item; keep the mouse put
  // (noReset) so the panel is still painted when it is read and cropped.
  try {
    const t = q('header nav a, header nav button, header a, header button').filter({ hasText: /^\s*Product\s*$/ }).filter({ visible: true }).first();
    if (await t.count()) { await t.hover({ timeout: 5000 }); await page.waitForTimeout(1200); }
  } catch (e) { log('  ! dropdown hover failed', String(e.message).split('\n')[0]); }
  await S('nav-dropdown', q('nav[class*="HeaderDropdownMain"], [class*="HeaderDropdownMain" i]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Nav dropdown', desc: 'The Product dropdown panel, opened by hovering its own trigger.', sel: 'nav.HeaderDropdownMain' }, { noScroll: true, noReset: true });
  await S('menu-link', q('[class*="HeaderDropdownMain" i] a, [class*="HeaderDropDown" i] a').filter({ hasText: /\S/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Menu link', desc: 'A link inside the opened header dropdown.', sel: 'dropdown link' }, { noScroll: true, noReset: true });
  const h = G.home;
  await S('hero-title', q('h1, [class*="Heading1Styled"]').filter({ visible: true }).first(), ['default'], { group: h, title: 'Hero headline', desc: 'The 108px display headline (TextStyles__Heading1Styled).', sel: 'h1' }, { noScroll: true });
  await S('hero-cta', q('main a, section a, main button').filter({ hasText: /^\s*Get Started\s*$|Get started/i }).filter({ visible: true }).first(), B4, { group: h, title: 'Hero CTA', desc: 'The hero Get-Started action; measured never followed.', sel: 'hero CTA' });
  await S('hero-sub', q('[class*="HeroSubcontent" i], main p, section p').filter({ hasText: /video editor|first video|build on/i }).filter({ visible: true }).first(), ['default'], { group: h, title: 'Hero copy', desc: 'The lede under the headline.', sel: 'hero lede' });
  // The badge only paints while the pointer is over the page, and it fades to
  // opacity 0 / scale .6 the moment the pointer stops. Even a sustained
  // synthetic mouse.move loop does not wake it (it tracks real pointer input,
  // not dispatched events), so the sampled entry is its hidden state and the
  // via records that plainly rather than pretending the pill was painted.
  await S('cursor-badge', q('span[class*="CursorButter"], [class*="CursorMain"]').filter({ visible: true }).first(), ['default'], { group: h, title: 'Cursor badge', desc: 'The custom-cursor pill ("Add butter") that follows the pointer. Captured in its hidden state (opacity 0, scale .6): it only paints while a real pointer follows the page, which synthetic movement does not wake — the reported box is the shrunken pill, not its visible size.', sel: 'span.CursorButter' }, { noScroll: true,
    before: { default: async () => 'element at rest: the badge does not paint for synthetic pointer movement, so the sampled state is its hidden one (opacity 0, scale .6)' } });
  await S('section-h2', q('main h2, section h2, [class*="Heading2Styled"]').filter({ visible: true }).first(), ['default'], { group: h, title: 'Section heading', desc: 'A 60px section heading (TextStyles__Heading2Styled).', sel: 'h2' });
  save();
}

async function pricing() {
  if (!(await newPage('pricing', { wait: 12000 }))) return;
  await sheetsFor('pricing');
  await chrome('pricing');
  const g = G.pricing;
  await S('pricing-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Pricing title', desc: 'The "Unlimit your creativity." display heading.', sel: 'h1 on /pricing' }, { noScroll: true });
  await S('billing-toggle', q('button[class*="PricingToggle"]').filter({ hasText: /Annually/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Billing toggle', desc: 'A Monthly/Annually billing-period button; toggled, never checked out.', sel: 'button.PricingToggle' }, { noScroll: true });
  await S('plan-card', q('[class*="PricingCardInner" i]').filter({ hasText: /Pro/ }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Plan card', desc: 'A pricing plan card (the Pro tier); the grey 32px-radius fill is a sibling Background layer, reported under Child layers.', sel: 'div.PricingCardInner' });
  await S('plan-price', q('[class*="PricingAmount" i]').filter({ hasText: /\$/ }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Plan price', desc: 'A plan card\'s price figure ($18 annually / $25 monthly).', sel: 'div.PricingAmount' });
  await S('plan-cta', q('a[class*="PricingCTA" i], [class*="PricingCTA" i] a, [class*="PricingCTA" i]').filter({ hasText: /Choose Pro/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Plan CTA', desc: 'A plan Choose-Pro action; measured never followed.', sel: 'a.PricingCTA' });
  await S('faq-item', q('button[class*="AccordionTrigger" i], [class*="AccordionHeader" i]').filter({ visible: true }).first(), ['default'], { group: g, title: 'FAQ item', desc: 'A Frequently-Asked accordion question (button.AccordionTrigger); toggled open would reveal the answer, never clicked.', sel: 'button.AccordionTrigger' });
  await S('feature-row', q('[class*="PricingAccordionItem" i]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Feature row', desc: 'A feature-comparison accordion row (Free stock photos, Reseller rights, ...).', sel: 'div.PricingAccordionItem' });
  save();
}

async function explore() {
  if (!(await newPage('explore', { url: BASE + '/explore', wait: 11000 }))) return;
  await sheetsFor('explore');
  await chrome('explore');
  const g = G.app;
  await S('d-sidebar', q('aside, [class*="sidebar" i]').filter({ visible: true }).first(), ['default'], { group: g, title: 'App sidebar', desc: 'The dark app-shell rail: wordmark, Home/Explore/Templates/Blocks nav, Log-in/Sign-up at the foot.', sel: 'aside.sidebar' }, { noScroll: true });
  await S('d-nav-link', q('aside a, [class*="sidebar" i] a').filter({ hasText: /^\s*(Explore|Templates|Blocks|Blog|Pricing)\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Sidebar link', desc: 'A nav link inside the dark sidebar.', sel: 'sidebar a' }, { noScroll: true });
  await S('d-login', q('aside a, aside button, [class*="sidebar" i] a').filter({ hasText: /^\s*Log in\s*$/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Sidebar login', desc: 'The sidebar Log-in button (dark fill); measured never followed.', sel: 'sidebar Log in' }, { noScroll: true });
  await S('d-signup', q('aside a, aside button, [class*="sidebar" i] a').filter({ hasText: /^\s*Sign up\s*$/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Sidebar signup', desc: 'The sidebar Sign-up button (white pill); measured never followed.', sel: 'sidebar Sign up' }, { noScroll: true });
  await S('d-create', q('button, a, [class*="Button" i]').filter({ hasText: /^\s*Create\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Create button', desc: 'The top-bar Create action (white pill on the dark shell); measured never followed.', sel: 'top Create button' }, { noScroll: true });
  await S('d-search', q('input[placeholder], input[type="search"], input').filter({ visible: true }).first(), ['default'], { group: g, title: 'Search field', desc: 'The shell search input, if one paints; never typed into.', sel: 'input' }, { noScroll: true });
  await S('d-card', q('[class*="card" i]').filter({ hasText: /Meet Butter|Figma|collection|Whats New/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Feature card', desc: 'A large feature/release card on /explore.', sel: 'explore card' });
  await S('d-block-card', q('[class*="card" i]').filter({ hasText: /Butter Studio|Particles|Glitch|Mockup/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Block card', desc: 'A block-preview card in the Featured Blocks row.', sel: 'block card' });
  await S('d-section', q('h2[class*="sections" i], h2.MuiTypography-root').filter({ visible: true }).first(), ['default'], { group: g, title: 'Section heading', desc: 'An /explore section heading (24px).', sel: 'h2.MuiTypography-sections' });
  save();
}

async function footer() {
  if (!(await newPage('home', { wait: 6000 }))) return;
  const g = G.footer;
  await page.evaluate(() => scrollTo(0, document.documentElement.scrollHeight));
  await page.waitForTimeout(1500);
  await S('footer', q('footer').filter({ visible: true }).last(), ['default'], { group: g, title: 'Footer', desc: 'The light-grey FooterMain: link columns, social, legal.', sel: 'footer.FooterMain' }, { noScroll: true });
  await S('footer-link', q('footer a').filter({ hasText: /\S/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Footer link', sel: 'footer a' }, { noScroll: true });
  await S('social-icon', q('footer a[href*="instagram"], footer a[href*="youtube"], footer a[href*="x.com"], footer a[href*="twitter"], footer a[href*="linkedin"], footer a').filter({ hasText: /Instagram|Youtube|YouTube|LinkedIn/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Social link', desc: 'A social link in the footer (text links, not glyphs).', sel: 'footer social a' }, { noScroll: true });
  save();
}

async function mobile() {
  if (!(await newPage('mobile', { mobile: true, url: BASE + '/' }))) return;
  await chrome('mobile');
  const g = G.mobile;
  await S('m-header', q('header').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile header', sel: 'header at 390' }, { noScroll: true });
  const menu = q('button[class*="MenuToggle"], header button').filter({ visible: true }).first();
  await S('m-menu-button', menu, ['default'], { group: g, title: 'Menu button', desc: 'The menu toggle (button.MenuToggleMain).', sel: 'button.MenuToggleMain' }, { noScroll: true });
  try {
    if (await menu.count()) { await menu.click({ timeout: 5000 }).catch(() => menu.evaluate((el) => el.click())); await page.waitForTimeout(1500); }
  } catch (e) { log('  ! mobile menu toggle failed', String(e.message).split('\n')[0]); }
  // The outer menu panel is div.index-style__HeaderDropdown (wraps the primary
  // nav AND the secondary Co-Create/MCP/social nav); .first() on document order
  // picks that outer container, not a nested nav.
  await S('m-menu-open', q('header div[class*="HeaderDropdown" i], header [class*="MobileMenu" i]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile menu, open', desc: 'The whole header menu panel opened by its own toggle (div.index-style__HeaderDropdown).', sel: 'div.index-style__HeaderDropdown' }, { noScroll: true });
  await S('m-nav-item', q('header nav a, header a').filter({ hasText: /^(Product|Blocks|Templates|Pricing|Blog)/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Mobile nav item', desc: 'A link inside the opened header menu.', sel: 'header menu a' }, { noScroll: true });
  await page.keyboard.press('Escape'); await page.waitForTimeout(500);
  await S('m-hero', q('h1, [class*="Heading1Styled"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile headline', sel: 'h1 at 390' });
  save();
}

run = new Date().toISOString().slice(0, 10);
out._meta.read = run;
out._meta.viewport = '1440 x 900 (mobile group 390 x 844); the marketing pages paint light, the /explore app shell paints dark';
out._meta.tool = 'tools/capture/public/measure.mjs';
const { browser, context: ctx0 } = await launch();
context = ctx0;
const pages = process.argv.slice(2);
const plan = { home, pricing, explore, login: () => {}, mobile };
const order = Object.keys(plan).filter((k) => !pages.length || pages.includes(k));
try {
  for (const k of order) { if (k !== 'mobile' && k !== 'login') await plan[k](); }
  if (!pages.length || pages.includes('home')) await footer();
  if (!pages.length || pages.includes('mobile')) await plan.mobile();
  // Reduced-motion check on an element that actually transitions (the cursor
  // badge's 0.2s opacity/transform), so the delta is meaningful.
  if (!pages.length || pages.includes('home')) await reducedMotion('home', '[class*="CursorButter"]');
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
