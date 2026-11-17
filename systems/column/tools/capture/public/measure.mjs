// Measures column.com's public components in every state reachable
// without signing in, paying or submitting anything.
//
//   node measure.mjs [page ...]   (headless renders clean; no bot wall)
//
// Pages: home ach cardprograms signin mobile (the footer group also runs
// on home). Writes raw/components-computed.json (merged) and one crop per
// component and state into components/crops/; raw/measurements.md is
// built by build-measurements.mjs.
//
// column.com is a Gatsby marketing site styled with styled-components plus
// a Tailwind layer — ~510 custom properties on :root, hashed sc-* component
// classes, SuisseIntl/Inter faces. A launch-banner promo row mounts inside
// the header — measured as real chrome. The styled-components cookie
// banner is hidden by closePromo, never answered.
// dashboard.column.com/login is the product's sign-in boundary: the form
// is measured, never submitted — the email field gets a focus reading
// only (nothing typed, nothing sent). The only presses are local UI
// toggles — the mobile menu button opens its own overlay.
import fs from 'node:fs';
import path from 'node:path';
import { BASE, launch, patch, open, closePromo, domFind, styleOf, crop, centre, RAW, UA, UA_MOBILE } from './lib.mjs';

const OUT = process.env.OUT_JSON || path.join(RAW, 'components-computed.json');
const out = fs.existsSync(OUT) ? JSON.parse(fs.readFileSync(OUT, 'utf8')) : {};
out._meta ??= {};
out.components ??= {};
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const save = () => fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');
const URLS = { home: '/', ach: '/ach/', cardprograms: '/card-programs/', signin: 'https://dashboard.column.com/login' };
let page, cdp, current, view, context, run;
const touched = new Set();
const listed = new Map();
// Page+viewport visits that actually loaded this run (not blocked): readings
// may only be pruned for components of one of these — a blocked mobile visit
// must not erase evidence the desktop visit of the same route kept.
const opened = new Set();

async function blocked() {
  return page.evaluate(() => {
    const t = (document.body && document.body.innerText) || '';
    return /performing security verification|verifying you are human|just a moment|access denied/i.test(t) || /just a moment/i.test(document.title) || t.trim().length < 40;
  }).catch(() => true);
}

async function newPage(key, { mobile = false, wait = 8000, dsf } = {}) {
  current = key;
  view = mobile ? 'mobile' : 'desktop';
  const b = context.browser();
  const ctx = await b.newContext(mobile
    ? { viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, userAgent: UA_MOBILE, isMobile: true, hasTouch: true, locale: 'en-US' }
    : { viewport: { width: 1440, height: 900 }, deviceScaleFactor: dsf ?? 2, userAgent: UA, locale: 'en-US' });
  await patch(ctx);
  page = await ctx.newPage();
  cdp = await ctx.newCDPSession(page);
  await cdp.send('DOM.enable');
  await cdp.send('CSS.enable');
  page.setDefaultTimeout(8000);
  log('open', key, mobile ? '(mobile)' : '');
  await open(page, /^https?:/.test(URLS[key]) ? URLS[key] : BASE + URLS[key], { wait });
  if (await blocked()) { log('  BLOCKED', key); await page.close(); await ctx.close(); return false; }
  opened.add(key + '|' + view);
  await page.addStyleTag({ content: '*{caret-color:transparent!important}' });
  await closePromo(page);
  return true;
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
  Object.assign(c, { page: current, view, run, url: URLS[current] && (/^https?:/.test(URLS[current]) ? URLS[current] : BASE + URLS[current]) }, meta);
  touched.add(key);
  c.states ??= {};
  return c;
}

async function measure(key, state, target, opts = {}) {
  const loc = target.filter({ visible: true }).first();
  const c = out.components[key];
  try {
    const s = await styleOf(loc);
    const prev = c.states[state];
    let file;
    if (opts.crop !== false) {
      try {
        file = await crop(page, (opts.cropLoc || loc).filter({ visible: true }).first(), `${key}-${state}`, opts.pad ?? 8);
      } catch (e) { s.cropError = String(e.message || e).slice(0, 120); }
    }
    // A failed crop keeps the previous state's image link rather than
    // dropping it; the style reading is fresh, the crop is last good.
    c.states[state] = { ...s, crop: file ?? (prev && prev.crop), via: opts.via, run };
    if (opts.extra) c.states[state].extra = await opts.extra(loc);
    log('  ', key, state, s.rect.w + 'x' + s.rect.h);
  } catch (e) {
    // A failed state capture must not erase a previous reading: keep it under
    // its own provenance and record the error beside it.
    const prev = c.states[state];
    c.states[state] = prev && !prev.error
      ? { ...prev, recaptureError: String(e.message || e).slice(0, 200) }
      : { error: String(e.message || e).slice(0, 200) };
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
        if (opts.noToggle) via = 'menu held open by opts.open';
        else { await toggle(opts.toggleLoc || loc); await page.waitForTimeout(900); via = 'own toggle'; }
      } else via = via || 'at rest';
      await measure(key, st, loc, { ...opts, via });
    } catch (e) {
      const prev = out.components[key].states[st];
      out.components[key].states[st] = prev && !prev.error
        ? { ...prev, recaptureError: String(e.message || e).slice(0, 200) }
        : { error: String(e.message || e).slice(0, 200) };
      log('  !', key, st, String(e.message).slice(0, 120));
    }
    if (undo) await undo().catch(() => {});
    if (opts.after?.[st]) await opts.after[st](loc).catch(() => {});
  }
  await reset();
}

// Clicks a UI toggle (nav menu, mobile menu). Refuses a submit button and any
// control whose text names an action this kit must never take.
const NEVER = /^(send|submit|sign in|log ?in|login|create|add|download|buy|purchase|pay|checkout|join|subscribe|sign up|save|apply|accept|reject|start|get started|claim|share|export|select|continue|book|request)$/i;
async function toggle(loc, { allowLink = false } = {}) {
  const l = loc.filter({ visible: true }).first();
  const t = await l.evaluate((el) => ({ tag: el.tagName, type: el.getAttribute('type'), text: (el.innerText || el.getAttribute('aria-label') || '').trim() }));
  if (t.type === 'submit' || NEVER.test(t.text) || (t.tag === 'A' && !allowLink)) throw new Error(`toggle refused: ${t.tag} "${t.text}"`);
  await l.click({ timeout: 4000 }).catch(() => l.evaluate((el) => el.click()));
}

const q = (sel) => page.locator(sel);
const B4 = ['default', 'hover', 'focus-visible', 'pressed'];

// Marks the shallowest ancestor of a text leaf whose subtree paints a fill of
// colour `want` (Framer draws a button's fill on a sibling layer, so the
// anchor alone reads transparent). `minY` skips same-text copies in the
// header. Falls back to the leaf. Returns whether anything was marked.
const markFillParent = async (textRe, want, attr, { minY = 0 } = {}) => page.evaluate(([src, flags, a, w, miny]) => {
  const re = new RegExp(src, flags);
  const texts = [...document.querySelectorAll('a,button,div,p,span')].filter((n) => {
    const t = (n.innerText || '').trim();
    const r = n.getBoundingClientRect();
    return re.test(t) && t.length < 60 && r.width > 0 && r.y >= miny;
  });
  const leaf = texts.find((n) => !texts.some((o) => o !== n && n.contains(o))) || texts[0];
  if (!leaf) return false;
  const paints = (n) => getComputedStyle(n).backgroundColor === w;
  for (let n = leaf, i = 0; n && i < 8; i++, n = n.parentElement) {
    if (n.getBoundingClientRect().width > 700) break;
    if (paints(n) || [...n.children].some((k) => paints(k) && k.getBoundingClientRect().width >= 80)) {
      n.setAttribute(a, '1');
      return true;
    }
  }
  leaf.setAttribute(a, '1');
  return true;
}, [textRe.source, textRe.flags, attr, want, minY]);

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

const G = {
  shell: 'Shell and navigation', home: 'Home', ach: 'ACH page',
  cardprograms: 'Card programs page', signin: 'App sign-in (boundary)',
  footer: 'Footer', mobile: 'Mobile (390 wide)',
};

async function home() {
  if (!(await newPage('home'))) return;
  await sheetsFor('home');
  const g = G.shell;
  // Header__SiteHeader (.header-hydrated): a LaunchBanner promo row on top
  // (~40px), then the ~62px bar with the Column logo, Products/Developers/
  // Company nav triggers, a "Sign in" link and the "Get started" pill
  // trigger; the GetStartedMenu's navy "Sign up" choice renders eager but
  // hidden, so nothing beyond the trigger is measured at rest.
  await S('promo-banner', q('a[class*="LaunchBanner"], [class*="LaunchBanner"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Promo banner', desc: 'The launch announcement row at the top of the header (Header__LaunchBanner) — real chrome, kept.', sel: '[class*=LaunchBanner]' }, { noScroll: true });
  await S('header', q('header.Header__SiteHeader, header[class*="SiteHeader"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Nav bar', desc: 'The fixed site header (Header__SiteHeader): Column logo, nav triggers, Sign in, ghost CTAs and the navy Sign up button.', sel: 'header[class*=SiteHeader]' }, { noScroll: true });
  await S('logo', q('header [class*="HeaderLogo"], header a[href="/"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Logo', desc: 'The Column logo home anchor in the nav (Header__HeaderLogo).', sel: 'header [class*=HeaderLogo]' }, { noScroll: true });
  await S('nav-item', q('header [class*="NavItemButton"]').filter({ visible: true }).first(), B4, { group: g, title: 'Nav link', desc: 'A nav trigger ("Products", Header__NavItemButton); its mega-menu renders eager in the DOM.', sel: 'header [class*=NavItemButton] first' }, { noScroll: true });
  await S('nav-ghost', q('header a[class*="NavItem"]').filter({ hasText: /^Sign in$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Nav sign-in link', desc: 'The "Sign in" NavItem anchor (Header__NavItem) linking to dashboard.column.com/login; measured never followed.', sel: 'header a[class*=NavItem]:has-text("Sign in")' }, { noScroll: true });
  await S('nav-cta', q('header button[class*="GetStartedMenu__Trigger"], header [class*="GetStartedMenu__Trigger"]').filter({ visible: true }).first(), B4, { group: g, title: 'Nav CTA', desc: 'The "Get started" pill (Button__StyledButton / GetStartedMenu__Trigger, white-50% fill + border) — the nav\'s painted CTA; it opens the GetStartedMenu dropdown whose navy "Sign up" choice renders eager but hidden, so it is not measured at rest.', sel: 'header [class*=GetStartedMenu__Trigger]' }, { noScroll: true });
  const h = G.home;
  await S('hero-title', q('main h1, h1').filter({ visible: true }).first(), ['default'], { group: h, title: 'Hero title', desc: '"Move, hold, and lend the dollar at scale" — the hero headline (SuisseIntl 52px, deep navy).', sel: 'first visible h1' }, { noScroll: true });
  await S('hero-cta', q('main a[class*="StyledButton"], main a[class*="StyledOutboundLink"], main button[class*="StyledButton"]').filter({ visible: true }).first(), B4, { group: h, title: 'Hero CTA', desc: 'The first button under the hero copy (the "Get started"/contact pair); links onward, never followed.', sel: 'main [class*=StyledButton] first' });
  await S('stat-figure', q('[class*="StatsWrapper"] [class*="Column"], [class*="_scale__StatsWrapper"] [class*="Column"]').filter({ visible: true }).first(), ['default'], { group: h, title: 'Stat tile', desc: 'A stat tile in the home stats row (_scale__StatsWrapper > Column — "$4.5T+ Annual transaction volume").', sel: '[class*=StatsWrapper] [class*=Column] first' });
  await S('dark-band', q('[class*="_infrastructure__Wrapper"]').filter({ visible: true }).first(), ['default'], { group: h, title: 'Dark band', desc: 'The near-black navy infrastructure section ("The only bank built from the ground up for developers", #011821 ground).', sel: '[class*=_infrastructure__Wrapper]' });
  await S('dark-title', q('[class*="_infrastructure"] h3').filter({ visible: true }).first(), ['default'], { group: h, title: 'Dark band title', desc: '"Flexible building blocks built on USD" — the 48px heading inside the dark infrastructure band (white on #011821).', sel: '[class*=_infrastructure] h3 first' });
  await S('section-title', q('main h2').filter({ hasText: /Start building/i }).filter({ visible: true }).first(), ['default'], { group: h, title: 'Section title', desc: '"Start building today" — the display section heading (SuisseIntl 60px).', sel: 'main h2:has-text("Start building")' });
  await S('page-ground', q('body'), ['default'], { group: h, title: 'Page ground', desc: 'The body element painted fill — the page ground.', sel: 'document.body' }, { noScroll: true, crop: false });
  save();
}

async function ach() {
  if (!(await newPage('ach'))) return;
  const g = G.ach;
  await S('ach-title', q('main h1, h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'ACH title', desc: '"Ultimate control and simplicity" — the ACH product page headline.', sel: 'first visible h1' }, { noScroll: true });
  await S('section-box', q('main [class*="SectionBox__Wrapper"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Section box', desc: 'A SectionBox content card on the ACH page.', sel: '[class*=SectionBox__Wrapper] first' });
  await S('product-screen', q('main [class*="ProductScreen__Wrapper"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Product screen', desc: 'The product-UI mock on the ACH page (ProductScreen__Wrapper — a rendered app frame inside the marketing page).', sel: '[class*=ProductScreen__Wrapper] first' });
  save();
}

async function cardprograms() {
  if (!(await newPage('cardprograms'))) return;
  const g = G.cardprograms;
  await S('cards-title', q('main h1, h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Cards title', desc: 'The Card programs product page headline.', sel: 'first visible h1' }, { noScroll: true });
  await S('cards-cta', q('main a[class*="StyledButton"], main a[class*="StyledOutboundLink"]').filter({ visible: true }).first(), B4, { group: g, title: 'Cards CTA', desc: 'The first button CTA on the Card programs page; links onward, never followed.', sel: 'main [class*=Styled*Link|Button] first' }, { noScroll: true });
  save();
}

async function signin() {
  if (!(await newPage('signin', { wait: 18000 }))) return;
  const g = G.signin;
  // dashboard.column.com/login is the product's sign-in surface — a
  // different styled-components build (sc-* hashed classes): an email
  // field, a "Sign in" submit and a passkey row, measured at rest; the
  // field gets a focus reading only — nothing typed, nothing submitted.
  await S('signin-card', q('form').filter({ visible: true }).first(), ['default'], { group: g, title: 'Sign-in card', desc: 'The dashboard.column.com login form — email field plus the Sign-in and passkey rows. Measured at rest, never submitted.', sel: 'form' }, { noScroll: true });
  await S('signin-field', q('input[name="email"], input[type="text"]').filter({ visible: true }).first(), ['default', 'focused'], { group: g, title: 'Email field', desc: 'The sign-in email input — a focus reading only; nothing typed, nothing sent.', sel: 'input[name=email]' }, { noScroll: true });
  await S('signin-submit', q('button').filter({ hasText: /Sign in|Continue/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Sign-in button', desc: 'The "Sign in"/"Continue" submit on the login form; measured never pressed — it would submit the form.', sel: 'form button:has-text("Sign in|Continue")' }, { noScroll: true });
  await S('signin-passkey', q('button').filter({ hasText: /passkey/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Passkey button', desc: 'The "Sign in with a passkey" row on the login form; measured never pressed.', sel: 'button:has-text("passkey")' }, { noScroll: true });
  save();
}

async function footer() {
  if (!(await newPage('home'))) return;
  const g = G.footer;
  await page.evaluate(() => scrollTo(0, document.documentElement.scrollHeight));
  await page.waitForTimeout(1600);
  // The footer is the _closer band — a light-grey (#eeeff2) block holding
  // link columns and the logo; no <footer> element, styled modules only.
  await page.evaluate(() => {
    const f = document.querySelector('[class*="_closer__Wrapper"]');
    if (f) f.setAttribute('data-m-footer', '1');
  });
  await S('footer', q('[data-m-footer="1"]'), ['default'], { group: g, title: 'Footer', desc: 'The closer band at the page bottom (light grey, #eeeff2): link columns, the Column logo and legal copy.', sel: '[class*=_closer__Wrapper]' }, { noScroll: true });
  await S('footer-link', q('[data-m-footer="1"] [class*="_footer__ListLink"], [data-m-footer="1"] a').filter({ visible: true }).first(), B4, { group: g, title: 'Footer card link', desc: 'The closer band\u2019s card link (_closer__CardLink — "Documentation / Get started" tiles, white-25% fill + 1px white ring).', sel: 'footer closer CardLink first' }, { noScroll: true });
  await S('footer-logo', q('[data-m-footer="1"] [class*="_footer__FooterLogoContainer"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Footer logo', desc: 'The Column logo block inside the footer band (_footer__FooterLogoContainer).', sel: '[class*=_footer__FooterLogoContainer]' }, { noScroll: true });
  save();
}

async function mobile() {
  if (!(await newPage('home', { mobile: true }))) return;
  const g = G.mobile;
  // At 390 the nav collapses to Header__SiteHeader (~45px) under the
  // LaunchBanner row: the logo and a Header__MobileNavToggle hamburger
  // (aria-label "Open menu"); the menu opens on the button's own press.
  await S('m-header', q('header[class*="SiteHeader"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile bar', desc: 'The 390 mobile nav bar (Header__SiteHeader): logo and the menu toggle, under the launch banner row.', sel: 'header[class*=SiteHeader]' }, { noScroll: true });
  await S('m-menu-button', q('[class*="MobileNavToggle"], button[aria-label="Open menu"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Menu button', desc: 'The hamburger (Header__MobileNavToggle, aria-label "Open menu"); its own press opens the menu.', sel: '[class*=MobileNavToggle]' }, { noScroll: true });
  const menuBtn = q('[class*="MobileNavToggle"], button[aria-label="Open menu"]').filter({ visible: true }).first();
  if (await menuBtn.count()) {
    try { await menuBtn.click({ timeout: 5000 }); await page.waitForTimeout(1500); } catch (e) { log('  ! mobile menu toggle failed', String(e.message).split('\n')[0]); }
  }
  // The open menu is a fixed overlay holding the link list; tag whatever
  // fills the viewport and contains a nav link.
  await page.evaluate(() => {
    const p = [...document.querySelectorAll('body *')].find((e) => {
      const cs = getComputedStyle(e);
      const r = e.getBoundingClientRect();
      return (cs.position === 'fixed' || cs.position === 'absolute') && r.height > 400 && r.width > 300 && (e.querySelector('a[href*="/ach"], a[href*="dashboard"], [class*="Menu"] a'));
    });
    if (p) p.setAttribute('data-m-panel', '1');
  }).catch(() => {});
  await S('m-menu-open', q('[data-m-panel="1"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile menu, open', desc: 'The menu overlay after the hamburger press.', sel: 'opened mobile menu overlay' }, { noScroll: true });
  await S('m-menu-link', q('[data-m-panel="1"] a, [data-m-panel="1"] button').filter({ visible: true }).first(), B4, { group: g, title: 'Menu link', desc: 'A link/accordion row inside the open mobile menu.', sel: 'first row inside the open menu' }, { noScroll: true });
  await page.keyboard.press('Escape'); await page.waitForTimeout(500);
  await S('m-hero', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile headline', desc: 'The hero headline at 390.', sel: 'h1 at 390' });
  save();
}

run = new Date().toISOString().slice(0, 10);
out._meta.read = run;
out._meta.viewport = '1440 x 900 (mobile group 390 x 844), light theme (dashboard.column.com/login is the sign-in boundary)';
out._meta.tool = 'tools/capture/public/measure.mjs';
const { browser, context: ctx0 } = await launch();
context = ctx0;
const pages = process.argv.slice(2);
const plan = { home, ach, cardprograms, signin, footer, mobile };
const order = Object.keys(plan).filter((k) => !pages.length || pages.includes(k));
try {
  for (const k of order) { if (k !== 'mobile') await plan[k](); }
  if (!pages.length || pages.includes('mobile')) await plan.mobile();
} finally {
  for (const [key, c] of Object.entries(out.components)) {
    // Prune only components whose page+viewport visit actually opened this
    // run: a blocked route (or a blocked mobile pass of a route the desktop
    // pass captured) keeps its earlier readings. Components saved before the
    // view field existed fall back to the m- prefix for their variant.
    if (!touched.has(key) && !pages.length) {
      const cview = c.view || (key.startsWith('m-') ? 'mobile' : 'desktop');
      if (opened.has(c.page + '|' + cview)) delete out.components[key];
      continue;
    }
    if (!touched.has(key)) continue;
    const want = listed.get(key);
    if (want) for (const st of Object.keys(c.states || {})) if (!want.has(st) && pages.length) delete c.states[st];
  }
  save();
  await browser.close().catch(() => {});
}
console.log('done ->', OUT);
