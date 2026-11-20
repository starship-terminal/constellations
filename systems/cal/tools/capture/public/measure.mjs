// Measures cal.com's public components in every state reachable without
// signing in, booking or submitting anything.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node measure.mjs [page ...]
//
// Pages: home pricing booking bookingdark login signup mobile.
// Writes raw/components-computed.json (merged) and one crop per component and
// state into components/crops/; raw/measurements.md is built by
// build-measurements.mjs.
//
// cal.com is a Next.js marketing app (Tailwind utility classes) over three
// public hosts: the marketing pages on cal.com, the auth cards on app.cal.com
// and the public booking page on i.cal.com (cal.com/peer), whose supported
// ?theme=dark&embed=true mode paints the booker's dark theme. Nothing is sent,
// booked or signed into: the only presses are local UI toggles — the Products
// nav dropdown, the pricing plan tabs and yearly switch, another calendar day
// and a time slot on the booker, which opens the guest details form (measured,
// never filled or confirmed).
import fs from 'node:fs';
import path from 'node:path';
import { BASE, AUTH, BOOKER, BOOKER_DARK, M, launch, patch, open, closePromo, domFind, styleOf, crop, centre, RAW, UA, UA_MOBILE } from './lib.mjs';

const OUT = process.env.OUT_JSON || path.join(RAW, 'components-computed.json');
const out = fs.existsSync(OUT) ? JSON.parse(fs.readFileSync(OUT, 'utf8')) : {};
out._meta ??= {};
out.components ??= {};
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const save = () => fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');
const URLS = { home: BASE + '/', pricing: BASE + '/pricing', booking: BOOKER, bookingdark: BOOKER_DARK, login: AUTH + '/auth/login', signup: AUTH + '/signup' };
let page, cdp, current, context, run, liveCtx;
const touched = new Set();
const listed = new Map();
// Routes the edge gates this run keep their earlier readings (a blocked pass
// must never erase evidence).
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
  await open(page, url || URLS[key], { wait, promo });
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
        file = await crop(page, (opts.cropLoc || loc).filter({ visible: true }).first(), `${key}-${state}`, opts.pad ?? 8, opts.keepSticky);
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
const NEVER = /^(send|submit|sign in|log ?in|login|create|add|download|buy|purchase|pay|checkout|join|subscribe|save|apply|accept|reject|start|get started|claim|share|export|select|continue|claim this offer|try again|confirm|schedule event|book)$/i;
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
    await p.goto(url || URLS[key], { waitUntil: 'domcontentloaded', timeout: 90000 }).catch(() => {});
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
  booker: 'Booking page (public)', bookerDark: 'Booking page, dark', auth: 'Auth cards',
  footer: 'Footer', mobile: 'Mobile (390 wide)',
};

async function home() {
  if (!(await newPage('home'))) return;
  await sheetsFor('home');
  await chrome('home');
  const g = G.shell;
  await S('header', q('nav.sticky').filter({ visible: true }).first(), ['default'], { group: g, title: 'Header', desc: 'The floating rounded nav bar: wordmark, the Products/Use-cases/Features/Resources dropdowns, Enterprise and Pricing links, Sign in and the dark Get-started button.', sel: 'nav.sticky' }, { noScroll: true });
  await S('logo', q('nav.sticky a[href="/"], nav.sticky a').filter({ visible: true }).first(), ['default'], { group: g, title: 'Logo', desc: 'The Cal.com wordmark anchor.', sel: 'nav.sticky a[href="/"]' }, { noScroll: true });
  await S('nav-trigger', q('nav button').filter({ hasText: /^Products$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Nav trigger', desc: 'The Products button that opens the header dropdown; toggled, never followed.', sel: 'nav button "Products"' }, { noScroll: true });
  await S('nav-link', q('nav a').filter({ hasText: /^(Pricing|Enterprise)$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Nav link', desc: 'A plain header link (Pricing).', sel: 'nav a "Pricing"' }, { noScroll: true });
  await S('nav-signin', q('nav a').filter({ hasText: /^\s*Sign in\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Sign-in link', desc: 'The Sign-in header action, linking to app.cal.com; measured never followed.', sel: 'nav a "Sign in"' }, { noScroll: true });
  await S('nav-cta', q('nav a').filter({ hasText: /^\s*Get started\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Nav CTA', desc: 'The dark Get-started header button, linking to app.cal.com/signup; measured never followed.', sel: 'nav a "Get started"' }, { noScroll: true });
  // Open the Products dropdown for the panel entries; keep the state
  // (noReset) so the panel is still painted when it is read and cropped.
  const openMenu = async () => {
    const panel = q('div[role="presentation"][class*="z-50"]').filter({ has: page.locator('a') }).filter({ visible: true }).first();
    if (await panel.count()) return;
    const t = q('nav button').filter({ hasText: /^Products$/ }).filter({ visible: true }).first();
    if (await t.count()) { await t.click({ timeout: 5000 }).catch(() => t.evaluate((el) => el.click())); await page.waitForTimeout(1500); }
  };
  try { await openMenu(); } catch (e) { log('  ! dropdown toggle failed', String(e.message).split('\n')[0]); }
  // The Products dropdown is a Base UI mega-panel (role="presentation", z-50)
  // holding product links and a booking-app preview; it stays open after the
  // trigger click (noReset) so the panel is still painted when read. The
  // menu-link entry re-opens it via open() because the panel closes as soon
  // as the mouse leaves, and skips focus-visible (Tab dismisses the menu).
  await S('nav-dropdown', q('div[role="presentation"][class*="z-50"]').filter({ has: page.locator('a') }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Nav dropdown', desc: 'The Products mega-menu panel, opened by its own trigger: product links beside a booking-app preview card.', sel: 'div[role="presentation"].z-50' }, { noScroll: true, noReset: true, keepSticky: true });
  await S('menu-link', q('div[role="presentation"] a').filter({ hasText: /Scheduling Links|Event planning|Cal\.ai/ }).filter({ visible: true }).first(), ['default', 'hover', 'pressed'], { group: g, title: 'Menu link', desc: 'A product card inside the opened Products dropdown (title, blurb, thumbnail).', sel: 'dropdown item' }, { noScroll: true, noReset: true, keepSticky: true, open: openMenu });
  await page.keyboard.press('Escape');
  const h = G.home;
  await S('hero-title', q('h1').filter({ visible: true }).first(), ['default'], { group: h, title: 'Hero headline', desc: 'The "Where people find the time to meet" display headline (it wraps the product mock, so its rect covers the mock too — the text readings are the headline\'s).', sel: 'h1' }, { noScroll: true });
  await S('hero-sub', q('p').filter({ hasText: /Making time for millions/ }).filter({ visible: true }).first(), ['default'], { group: h, title: 'Hero copy', desc: 'The lede under the headline.', sel: 'hero lede' }, { noScroll: true });
  await S('hero-google', q('a').filter({ hasText: /Sign up with Google/ }).filter({ visible: true }).first(), B4, { group: h, title: 'Google signup', desc: 'The hero Sign-up-with-Google action, linking to app.cal.com SSO; measured never followed.', sel: 'a "Sign up with Google"' });
  await S('hero-microsoft', q('a').filter({ hasText: /Sign up with Microsoft/ }).filter({ visible: true }).first(), B4, { group: h, title: 'Microsoft signup', desc: 'The hero Sign-up-with-Microsoft action; measured never followed.', sel: 'a "Sign up with Microsoft"' });
  await S('hero-email', q('a').filter({ hasText: /Sign up with email/ }).filter({ visible: true }).first(), B4, { group: h, title: 'Email signup link', desc: 'The quiet "Sign up with email." link under the SSO buttons.', sel: 'a "Sign up with email."' });
  await S('changelog', q('a').filter({ hasText: /Cal\.com launches/ }).filter({ visible: true }).first(), B4, { group: h, title: 'Changelog badge', desc: 'The NEW "Cal.com launches" release pill under the hero.', sel: 'changelog pill' });
  // The hero embeds a booking-page product mock ("Intro call 30m ... Booked");
  // its pieces are measured as the mock they are, not as the live booker.
  const mock = await domFind(page, /Intro call/, { sel: 'div, section', tag: 'mock', up: null, minW: 200, minH: 60 });
  await S('hero-mock', page.locator('[data-m-mark="mock"]'), ['default'], { group: h, title: 'Product mock', desc: 'The booking-page mock inside the hero (Intro call card with the 12:30 slot chips and the Booked badge).', sel: 'hero booking mock' });
  save();
}

async function pricing() {
  if (!(await newPage('pricing', { wait: 12000 }))) return;
  await sheetsFor('pricing');
  await chrome('pricing');
  const g = G.pricing;
  await S('pricing-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Pricing title', desc: 'The "Choose your Cal.com subscription" display heading.', sel: 'h1 on /pricing' }, { noScroll: true });
  await S('pricing-sub', q('p').filter({ hasText: /Start scheduling for free/ }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Pricing copy', desc: 'The lede under the pricing heading.', sel: 'pricing lede' });
  await S('plan-tab', q('button').filter({ hasText: /^(Individuals|Teams|Organizations|Enterprise)$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Plan tab', desc: 'A plan-group tab (Individuals/Teams/Organizations/Enterprise); toggled, never checked out.', sel: 'plan group tab' });
  await S('billing-toggle', q('[role="switch"], button[aria-checked]').filter({ visible: true }).first(), B4, { group: g, title: 'Billing switch', desc: 'The YEARLY billing switch; toggled locally, never checked out.', sel: 'role=switch' });
  const planCard = await domFind(page, /Everything you could need for scheduling[\s\S]+Use for free/, { sel: 'div, section, article', tag: 'pc', minW: 200, minH: 200 });
  await S('plan-card', page.locator('[data-m-mark="pc"]'), ['default'], { group: g, title: 'Plan card', desc: 'The Free plan card ("Everything you could need for scheduling as an individual").', sel: 'Free plan card' });
  await S('plan-cta', q('a, button').filter({ hasText: /^\s*Use for free\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Plan CTA', desc: 'The Free plan "Use for free" action; measured never followed.', sel: 'Use for free' });
  await S('sales-cta', q('a, button').filter({ hasText: /^\s*Talk to sales\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Sales CTA', desc: 'The Talk-to-sales action beside the heading; measured never followed.', sel: 'Talk to sales' });
  await S('feature-accordion', q('button').filter({ hasText: /^(Advanced features|Set meeting limits|Customization|Integrations|Support & service)$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Feature accordion', desc: 'A feature-breakdown accordion section; measured closed, never expanded.', sel: 'feature accordion button' });
  save();
}

async function booking() {
  if (!(await newPage('booking', { wait: 10000 }))) return;
  await sheetsFor('booking');
  await chrome('booking');
  const g = G.booker;
  // The booker's left column holds the host, event title and meta rows; the
  // month grid and the slot column are the interactive surface.
  await S('bk-page', q('main, body > div').filter({ visible: true }).first(), ['default'], { group: g, title: 'Booker canvas', desc: 'The booking page\'s outer container on the lab-grey canvas.', sel: 'main' }, { noScroll: true });
  await S('bk-title', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Event title', desc: 'The event name ("15 Minute Meeting").', sel: 'h1' }, { noScroll: true });
  await S('bk-host', q('div, span, p').filter({ hasText: /^With Peer Richelsen,/ }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Host line', desc: 'The host line under the title (other people\'s names stay per policy).', sel: 'host line' }, { noScroll: true });
  await S('bk-badge', q('div, span').filter({ hasText: /^Requires confirmation$/ }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Confirmation badge', desc: 'The "Requires confirmation" badge under the title.', sel: 'confirmation badge' }, { noScroll: true });
  await S('bk-meta', q('div, li').filter({ hasText: /^Asia\// }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Timezone row', desc: 'The timezone meta row (Asia/Singapore).', sel: 'timezone row' });
  await S('bk-calendar', q('button[data-testid="day"]').first().locator('xpath=ancestor::div[contains(@class,"grid-cols-7")][1]'), ['default'], { group: g, title: 'Calendar grid', desc: 'The month grid (grid-cols-7) holding the day buttons.', sel: 'button[data-testid=day] grid ancestor' });
  await S('bk-day', q('button[data-testid="day"]:not([disabled])').filter({ hasText: /^\s*1[3-9]\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Day button', desc: 'A bookable day in the month grid; clicking it is a local toggle that shows that day\'s slots.', sel: 'button[data-testid=day]' });
  await S('bk-day-today', q('button[data-testid="day"]').filter({ hasText: /Today/ }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Today cell', desc: 'The today cell in the month grid (its "Today" label is sr-only; the date number paints).', sel: 'button[data-testid=day] Today' });
  await S('bk-slot', q('button, a').filter({ hasText: /^\s*\d{1,2}:\d{2}(am|pm)\s*$/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Time slot', desc: 'An available time slot; measured, never clicked (a selected slot can be held).', sel: 'time slot' });
  // Booking slot: recorded as a boundary, not clicked. Selecting a slot on a real
  // person's booking page can hold it, so the details form below is no longer
  // opened; its specs record missing until an owned demo page is captured.
  await S('bk-form', q('form').filter({ visible: true }).first(), ['default'], { group: g, title: 'Details form', desc: 'The guest details form a slot opens: name/email/notes fields and the confirm action. Measured, never filled or submitted.', sel: 'form' }, { noScroll: true, noReset: true });
  await S('bk-field', q('form input[type="text"], form input[type="email"], form input').filter({ visible: true }).first(), ['default', 'focused'], { group: g, title: 'Form field', desc: 'A text field in the details form; focused by a click, never typed into or submitted.', sel: 'form input' }, { noReset: true });
  await S('bk-confirm', q('button[type="submit"], form button').filter({ hasText: /confirm|schedule|book/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Confirm button', desc: 'The booking confirm action; measured only — a real press would create a booking, so it was never clicked (pressed is a CDP-forced state).', sel: 'form confirm button' }, { noReset: true });
  save();
}

async function bookingDark() {
  if (!(await newPage('bookingdark', { wait: 10000 }))) return;
  const g = G.bookerDark;
  await S('bkd-canvas', q('main, body > div').filter({ visible: true }).first(), ['default'], { group: g, title: 'Dark booker canvas', desc: 'The booking page under its supported ?theme=dark&embed=true mode: the real dark theme, not a forced class.', sel: 'main (dark)' }, { noScroll: true });
  await S('bkd-title', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Dark event title', sel: 'h1 (dark)' }, { noScroll: true });
  await S('bkd-calendar', q('button[data-testid="day"]').first().locator('xpath=ancestor::div[contains(@class,"grid-cols-7")][1]'), ['default'], { group: g, title: 'Dark calendar', sel: 'calendar grid (dark)' });
  await S('bkd-slot', q('button, a').filter({ hasText: /^\s*\d{1,2}:\d{2}(am|pm)\s*$/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Dark time slot', desc: 'A dark-mode slot button; measured, never followed.', sel: 'time slot (dark)' });
  save();
}

async function login() {
  if (!(await newPage('login', { wait: 10000 }))) return;
  const g = G.auth;
  const acard = await domFind(page, /Sign in with Google[\s\S]+Continue/, { sel: 'div, section, main', tag: 'ac', minW: 200, minH: 150 });
  await S('auth-card', page.locator('[data-m-mark="ac"]'), ['default'], { group: g, title: 'Login card', desc: 'The sign-in card on app.cal.com: SSO buttons, the email and password fields, Forgot?, Continue. Captured as a boundary — never filled or submitted.', sel: 'login card' }, { noScroll: true });
  const atitle = await domFind(page, /Welcome back/, { sel: 'h1, h2, h3, p, span, div', tag: 'at' });
  await S('auth-title', page.locator('[data-m-mark="at"]'), ['default'], { group: g, title: 'Login title', desc: 'The "Welcome back! Sign in to continue" heading.', sel: 'welcome back' }, { noScroll: true });
  await S('sso-google', q('button, a').filter({ hasText: /Sign in with Google/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Google SSO', desc: 'The Sign-in-with-Google button; measured never followed.', sel: 'SSO button' });
  await S('email-field', q('input[type="email"]').filter({ visible: true }).first(), ['default', 'focused'], { group: g, title: 'Email field', desc: 'The email input; focused by a click, never typed into or submitted.', sel: 'input[type=email]' });
  await S('pass-field', q('input[type="password"]').filter({ visible: true }).first(), ['default', 'focused'], { group: g, title: 'Password field', desc: 'The password input; focused by a click, never typed into or submitted.', sel: 'input[type=password]' });
  await S('forgot-link', q('a').filter({ hasText: /^Forgot\?/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Forgot link', desc: 'The "Forgot?" password link.', sel: 'a "Forgot?"' });
  await S('continue-btn', q('button').filter({ hasText: /^Continue$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Continue button', desc: 'The sign-in submit; measured only, never clicked (pressed is CDP-forced).', sel: 'button "Continue"' });
  await S('saml-link', q('button, a').filter({ hasText: /SAML/ }).filter({ visible: true }).first(), B4, { group: g, title: 'SAML link', desc: 'The "Sign in with SAML/OIDC" action.', sel: 'SAML/OIDC' });
  save();
}

async function signup() {
  if (!(await newPage('signup', { wait: 10000 }))) return;
  const g = G.auth;
  const scard = await domFind(page, /Continue with Google[\s\S]+Continue with SAML/, { sel: 'div, section, main', tag: 'sc', minW: 200, minH: 150 });
  await S('signup-card', page.locator('[data-m-mark="sc"]'), ['default'], { group: g, title: 'Signup card', desc: 'The signup card on app.cal.com: Continue-with-SSO buttons and the plan pitch. Captured as a boundary — never followed.', sel: 'signup card' }, { noScroll: true });
  const stitle = await domFind(page, /Claim cal\.com\/you/, { sel: 'h1, h2, h3, p, span, div', tag: 'st' });
  await S('signup-title', page.locator('[data-m-mark="st"]'), ['default'], { group: g, title: 'Signup title', desc: 'The "Claim cal.com/you" heading on the signup card.', sel: 'claim cal.com/you' }, { noScroll: true });
  await S('signup-google', q('button, a').filter({ hasText: /Continue with Google/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Google continue', desc: 'The Continue-with-Google button; measured never followed.', sel: 'Continue with Google' });
  await S('signup-email', q('button, a').filter({ hasText: /Continue with Email/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Email continue', desc: 'The Continue-with-Email button; measured never followed.', sel: 'Continue with Email' });
  const trow = await domFind(page, /Trustpilot/, { sel: 'div, p, span', tag: 'tr', minW: 60 });
  await S('trust-row', page.locator('[data-m-mark="tr"]'), ['default'], { group: g, title: 'Trust row', desc: 'The rating row (Trustpilot / Product Hunt / G2) beside the signup card.', sel: 'rating row' });
  save();
}

async function footer() {
  if (!(await newPage('home', { wait: 6000 }))) return;
  const g = G.footer;
  await page.evaluate(() => scrollTo(0, document.documentElement.scrollHeight));
  await page.waitForTimeout(1500);
  await S('footer', q('footer').filter({ visible: true }).last(), ['default'], { group: g, title: 'Footer', desc: 'The near-black footer: link columns, app-store badges, social links.', sel: 'footer' }, { noScroll: true });
  await S('footer-link', q('footer a').filter({ hasText: /\S/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Footer link', sel: 'footer a' }, { noScroll: true });
  save();
}

async function mobile() {
  if (!(await newPage('mobile', { mobile: true, url: BASE + '/' }))) return;
  await chrome('mobile');
  const g = G.mobile;
  await S('m-header', q('nav.sticky, nav').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile header', sel: 'nav at 390' }, { noScroll: true });
  const menu = q('nav button[aria-label], nav button').filter({ visible: true }).first();
  await S('m-menu-button', menu, ['default'], { group: g, title: 'Menu button', desc: 'The nav menu toggle at 390px.', sel: 'mobile menu button' }, { noScroll: true });
  try {
    if (await menu.count()) { await menu.click({ timeout: 5000 }).catch(() => menu.evaluate((el) => el.click())); await page.waitForTimeout(1500); }
  } catch (e) { log('  ! mobile menu toggle failed', String(e.message).split('\n')[0]); }
  await S('m-menu-open', q('div[role="dialog"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile menu, open', desc: 'The full-screen nav drawer opened by its own toggle.', sel: 'div[role=dialog]' }, { noScroll: true });
  await S('m-nav-item', q('div[role="dialog"] a').filter({ hasText: /^(Pricing|Enterprise|Sign in)$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Mobile nav item', desc: 'A link inside the opened nav drawer.', sel: 'mobile menu link' }, { noScroll: true });
  await page.keyboard.press('Escape'); await page.waitForTimeout(500);
  await S('m-hero', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile headline', sel: 'h1 at 390' });
  save();
}

run = new Date().toISOString().slice(0, 10);
out._meta.read = run;
out._meta.viewport = '1440 x 900 (mobile group 390 x 844); the marketing pages and the booker paint light; the booker also paints dark under its supported ?theme=dark&embed=true mode';
out._meta.tool = 'tools/capture/public/measure.mjs';
const { browser, context: ctx0 } = await launch();
context = ctx0;
const pages = process.argv.slice(2);
const plan = { home, pricing, booking, bookingdark: bookingDark, login, signup, mobile };
const order = Object.keys(plan).filter((k) => !pages.length || pages.includes(k));
try {
  for (const k of order) { if (k !== 'mobile') await plan[k](); }
  if (!pages.length || pages.includes('home')) await footer();
  if (!pages.length || pages.includes('mobile')) await plan.mobile();
  // Reduced-motion check on an element that transitions (the nav trigger's
  // hover fade), so the delta is meaningful.
  if (!pages.length || pages.includes('home')) await reducedMotion('home', 'nav button');
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
