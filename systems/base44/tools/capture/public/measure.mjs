// Measures base44.com's public components in every state reachable without
// signing in, downloading or submitting anything.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node measure.mjs [page ...]
//
// Pages: home pricing signin mobile.
// Writes raw/components-computed.json (merged) and one crop per component and
// state into components/crops/; raw/measurements.md is built by
// build-measurements.mjs.
//
// base44.com is a Remix/Vite site (Tailwind + named CSS vars) in one light
// theme on the public routes; components are found by role, landmark,
// aria-label or stable text. Nothing is sent, downloaded or signed into: the
// only presses are local UI toggles — the Product nav menu, the pricing
// billing toggle, an FAQ item and the mobile menu. "Start building", the plan
// CTAs, the prompt box's Send, the OAuth buttons and the sign-in email flow
// are measured in all states except followed or pressed for real.
import fs from 'node:fs';
import path from 'node:path';
import { BASE, APP, launch, patch, open, closePromo, domFind, styleOf, crop, centre, RAW, UA, UA_MOBILE } from './lib.mjs';

const OUT = process.env.OUT_JSON || path.join(RAW, 'components-computed.json');
const out = fs.existsSync(OUT) ? JSON.parse(fs.readFileSync(OUT, 'utf8')) : {};
out._meta ??= {};
out.components ??= {};
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const save = () => fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');
const URLS = { home: '/', pricing: '/pricing', signin: APP + '/login' };
let page, cdp, current, context, run;
const touched = new Set();
const listed = new Map();
// Pages that actually loaded this run (not blocked): readings may only be
// pruned for components on one of these — a blocked route must not erase
// evidence captured earlier.
const opened = new Set();

async function blocked() {
  return page.evaluate(() => {
    const t = (document.body && document.body.innerText) || '';
    return /performing security verification|verifying you are human|just a moment|access denied/i.test(t) || t.trim().length < 40;
  }).catch(() => true);
}

async function newPage(key, { mobile = false, wait = 8000 } = {}) {
  current = key;
  const b = context.browser();
  const ctx = await b.newContext(mobile
    ? { viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, userAgent: UA_MOBILE, isMobile: true, hasTouch: true, locale: 'en-US' }
    : { viewport: { width: 1440, height: 900 }, deviceScaleFactor: 2, userAgent: UA, locale: 'en-US' });
  await patch(ctx);
  page = await ctx.newPage();
  cdp = await ctx.newCDPSession(page);
  await cdp.send('DOM.enable');
  await cdp.send('CSS.enable');
  page.setDefaultTimeout(8000);
  log('open', key, mobile ? '(mobile)' : '');
  const url = URLS[key].startsWith('http') ? URLS[key] : BASE + URLS[key];
  await open(page, url, { wait });
  if (await blocked()) { log('  BLOCKED', key); await page.close(); await ctx.close(); return false; }
  opened.add(key);
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
    c.states[state] = { ...s, crop: file, via: opts.via };
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
        else { await toggle(loc); await page.waitForTimeout(900); via = 'own toggle'; }
      } else if (st === 'expanded') {
        await toggle(loc); await page.waitForTimeout(900); via = 'own toggle';
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

// Clicks a UI toggle (nav menu, billing toggle, FAQ item, mobile menu). Refuses
// a submit button and any control whose text names an action this kit must
// never take.
const NEVER = /^(send|send message|submit|sign in|log ?in|login|sign up|create|add|download|buy|purchase|pay|checkout|join|subscribe|save|apply|accept|reject|start|start building|get started|claim|share|export|select|continue|continue with email|book|request)$/i;
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

const G = {
  shell: 'Shell and navigation', home: 'Home', pricing: 'Pricing',
  signin: 'Sign in', footer: 'Footer', mobile: 'Mobile (390 wide)',
};

// Clicks the Product nav button and marks the mega panel it opened (the
// full-width white sheet under the header holding "AI App Builder").
const openProductPanel = async () => {
  const b = q('header button').filter({ hasText: /^Product$/ }).filter({ visible: true }).first();
  await b.click({ timeout: 4000 }).catch(() => b.evaluate((el) => el.click()));
  await page.waitForTimeout(1400);
  return page.evaluate(() => {
    // The mega menu is an absolutely positioned full-width sheet that mounts
    // just under the 86px header; mark the outermost one that paints.
    const hit = [...document.querySelectorAll('div,section,nav')].filter((n) => {
      const r = n.getBoundingClientRect();
      const c = getComputedStyle(n);
      return (c.position === 'absolute' || c.position === 'fixed') && r.y >= 70 && r.y < 180 && r.width > 1000 && r.height > 150 && c.visibility !== 'hidden';
    }).pop();
    const el = hit || document.querySelector('header');
    if (!el) return false;
    el.setAttribute('data-m-panel', '1');
    return true;
  });
};

async function home() {
  if (!(await newPage('home'))) return;
  await sheetsFor('home');
  const g = G.shell;
  await S('header', q('header').first(), ['default'], { group: g, title: 'Header', desc: 'The fixed bar: logo, the nav (Product, Use Cases, Solutions, Resources menus; Pricing, Enterprise, Superagents links), the language globe and the dark Start building pill.', sel: 'header' }, { noScroll: true });
  await S('logo', q('header a[aria-label="Base44"]').first(), ['default'], { group: g, title: 'Logo', sel: 'header a[aria-label=Base44]' }, { noScroll: true });
  const navB = (t) => q('header button').filter({ hasText: t }).filter({ visible: true }).first();
  const navA = (t) => q('header a, nav a').filter({ hasText: t }).filter({ visible: true }).first();
  await S('nav-menu-button', navB(/^Product$/), B4, { group: g, title: 'Nav menu button', desc: 'A top-level nav item that opens a mega menu (Product; Use Cases, Solutions and Resources are the same control).', sel: 'header button:has-text("Product")' }, { noScroll: true });
  await S('nav-product-open', navB(/^Product$/), ['opened'], { group: g, title: 'Product menu, open', desc: 'The nav button after its own press opens the full-width product panel; the crop holds the opened panel.', sel: 'header button:has-text("Product")' }, { noScroll: true, noToggle: true, before: { opened: async () => { await openProductPanel(); return 'own press opens the mega menu'; } }, cropLoc: q('[data-m-panel="1"]'), pad: 4, after: { opened: async () => { await page.keyboard.press('Escape'); await page.mouse.move(700, 500); await page.waitForTimeout(500); } } });
  await S('nav-link', navA(/^Pricing$/), B4, { group: g, title: 'Nav link', sel: 'header a:has-text("Pricing")' }, { noScroll: true });
  await S('nav-superagents', navA(/^Superagents$/), B4, { group: g, title: 'Superagents link', desc: 'The highlighted nav item, dotted either side and painted blue.', sel: 'header a:has-text("Superagents")' }, { noScroll: true });
  await S('nav-locale', q('header button[aria-label*="language" i]').first(), B4, { group: g, title: 'Language button', desc: 'The globe icon left of the CTA.', sel: 'header button[aria-label*="language"]' }, { noScroll: true });
  await S('nav-cta', navA(/^Start building$/), B4, { group: g, title: 'Start building button', desc: 'The dark pill on the right of the nav, repeated through the site. Measured, never followed.', sel: 'header a:has-text("Start building")' }, { noScroll: true });

  const h = G.home;
  await S('hero-title', q('h1').first(), ['default'], { group: h, title: 'Hero title', desc: '"Every builder needs a base" in the site\'s display face (Dazzed).', sel: 'h1' }, { noScroll: true });
  await S('hero-sub', q('h1').first().locator('xpath=following::*[self::p or self::div][string-length(normalize-space())>40][1]'), ['default'], { group: h, title: 'Hero subcopy', sel: 'first long paragraph under h1' }, { noScroll: true });
  await S('section-title', q('h2').first(), ['default'], { group: h, title: 'Section title', sel: 'first h2' });
  // The hero prompt box is the site's signature control: a white card with a
  // big textarea and a button row (attach, mode trigger, mic, orange send).
  await S('prompt-box', q('.sa-prompt-box').first(), ['default'], { group: h, title: 'Prompt box', desc: 'The hero\'s "I want to build…" composer: a white rounded card with the textarea and its button row.', sel: '.sa-prompt-box' }, { noScroll: true });
  await S('prompt-field', q('textarea[aria-label]').first(), ['default', 'focused', 'filled'], { group: h, title: 'Prompt field', desc: 'The composer\'s textarea; sample text was typed and deleted, nothing sent.', sel: 'textarea[aria-label="Describe the app you want to build"]' });
  await S('prompt-attach', q('button[aria-label="More options"]').first(), B4, { group: h, title: 'Attach button', desc: 'The "+" button at the composer\'s left. Measured, never pressed.', sel: 'button[aria-label="More options"]' });
  await S('prompt-mode', q('button').filter({ hasText: /^Build$/ }).filter({ visible: true }).first(), B4, { group: h, title: 'Mode trigger', desc: 'The "Build" dropdown inside the composer; its menu was not opened.', sel: 'button:has-text("Build")' });
  await S('prompt-mic', q('button[aria-label="Voice input"]').first(), B4, { group: h, title: 'Voice button', desc: 'The microphone button. Measured, never pressed.', sel: 'button[aria-label="Voice input"]' });
  await S('prompt-submit', q('button[aria-label="Send message"]').first(), B4, { group: h, title: 'Send button', desc: 'The orange send button. Measured in all states except pressed for real — nothing was sent.', sel: 'button[aria-label="Send message"]' });
  await S('build-tile', q('button.br-build-type-tile').first(), B4, { group: h, title: 'Build-type tile', desc: 'One of the five "What will you build?" tiles under the composer (App; Dashboard, Website, Mobile app and Online store are the same control).', sel: 'button.br-build-type-tile' });
  const faq = q('button').filter({ hasText: /^What is Base44\?/ }).filter({ visible: true }).first();
  await S('faq-item', faq, B4, { group: h, title: 'FAQ item', desc: 'A collapsed row of the FAQ accordion.', sel: 'button:has-text("What is Base44?")' });
  await S('faq-open', faq, ['expanded'], { group: h, title: 'FAQ item, expanded', desc: 'The same row after its own press; the crop holds the item and its answer.', sel: 'button:has-text("What is Base44?")' }, { cropLoc: faq.locator('xpath=ancestor::*[self::li or self::div][1]'), pad: 6 });
  save();
}

async function pricing() {
  if (!(await newPage('pricing'))) return;
  await sheetsFor('pricing');
  const g = G.pricing;
  await S('pricing-title', q('h1').first(), ['default'], { group: g, title: 'Pricing title', sel: 'h1' }, { noScroll: true });
  await S('billing-toggle', q('.pricing-toggle-btn').first().locator('xpath=..'), ['default'], { group: g, title: 'Billing toggle', desc: 'The Yearly/Monthly segment control over the plan cards.', sel: 'parent of .pricing-toggle-btn' }, { noScroll: true });
  await S('billing-yearly', q('button').filter({ hasText: /^Yearly/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Yearly segment', desc: 'The selected segment ("Yearly SAVE 20%"), painted orange.', sel: 'button:has-text("Yearly")' }, { noScroll: true });
  await S('billing-monthly', q('button').filter({ hasText: /^Monthly$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Monthly segment', desc: 'The unselected segment; switching it is a local toggle, no purchase.', sel: 'button:has-text("Monthly")' }, { noScroll: true });
  const planBtn = q('a.br-cta-fluid, button').filter({ hasText: /^Start building$/ }).filter({ visible: true }).first();
  await S('plan-cta', planBtn, B4, { group: g, title: 'Plan CTA', desc: 'The full-width "Start building" button inside a plan card. Measured, never followed.', sel: '.br-cta-fluid inside a plan card' });
  // The card is the smallest ancestor that actually paints its own surface —
  // .pricing-card carries the white fill.
  await page.evaluate(() => {
    const a = [...document.querySelectorAll('.pricing-card')][0];
    if (a) a.setAttribute('data-m-plan-card', '1');
  });
  await S('plan-card', q('[data-m-plan-card="1"]'), ['default'], { group: g, title: 'Plan card', sel: '.pricing-card' });
  await S('popular-badge', q('*').filter({ hasText: /^Popular$/ }).filter({ visible: true }).last(), ['default'], { group: g, title: 'Popular badge', desc: 'The blue chip on the Builder plan card.', sel: 'span:has-text("Popular")' });
  await S('price', q('*').filter({ hasText: /^\$\d+$/ }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Price figure', desc: 'A plan\'s price ("$160" on Elite at yearly billing).', sel: 'text "$NNN"' });
  save();
}

async function signin() {
  if (!(await newPage('signin'))) return;
  const g = G.signin;
  await S('signin-title', q('h1, h2').first(), ['default'], { group: g, title: 'Sign-in title', desc: '"Welcome to Base44" on app.base44.com/login.', sel: 'h1/h2' }, { noScroll: true });
  await S('signin-google', q('button').filter({ hasText: /log in with google/i }).first(), B4, { group: g, title: 'Log in with Google', desc: 'The OAuth button. Measured, never pressed — no sign-in was attempted.', sel: 'button:has-text("Log in with Google")' });
  await S('signin-apple', q('button').filter({ hasText: /log in with apple/i }).first(), B4, { group: g, title: 'Log in with Apple', desc: 'The OAuth button. Measured, never pressed.', sel: 'button:has-text("Log in with Apple")' });
  await S('signin-github', q('button').filter({ hasText: /log in with github/i }).first(), B4, { group: g, title: 'Log in with GitHub', desc: 'The OAuth button. Measured, never pressed.', sel: 'button:has-text("Log in with GitHub")' });
  // The email field is a bare input inside a bordered wrapper; measure both.
  await page.evaluate(() => {
    const i = document.querySelector('input[type="email"], input[aria-label="Email"]');
    if (!i) return;
    i.setAttribute('data-m-field', '1');
    let n = i;
    for (let k = 0; n && k < 5; n = n.parentElement, k++) {
      const c = getComputedStyle(n);
      if (parseFloat(c.borderTopWidth) > 0 && c.borderTopStyle !== 'none' || c.backgroundColor !== 'rgba(0, 0, 0, 0)') { n.setAttribute('data-m-fieldwrap', '1'); break; }
    }
  });
  await S('signin-field-wrap', q('[data-m-fieldwrap="1"]'), ['default'], { group: g, title: 'Email field shell', desc: 'The bordered box holding the email input.', sel: 'bordered ancestor of the email input (marked in-page)' });
  await S('signin-field', q('input[type="email"], input[aria-label="Email"]').first(), ['default', 'focused', 'filled'], { group: g, title: 'Email field', desc: 'The sign-in email input; sample text was typed and deleted, nothing sent.', sel: 'input[type=email]' });
  // The submit starts disabled (empty field); that is its default state here.
  await S('signin-submit', q('button').filter({ hasText: /continue with email/i }).first(), ['default'], { group: g, title: 'Continue with email button', desc: 'The email sign-in submit, captured disabled as painted for an empty field (the state was measured, never enabled or pressed).', sel: 'button:has-text("Continue with email")' });
  await S('signin-signup', q('a').filter({ hasText: /^Sign up$/ }).first(), B4, { group: g, title: 'Sign up link', desc: 'The register link under the form. Measured, never followed.', sel: 'a:has-text("Sign up")' });
  await S('signin-legal', q('a').filter({ hasText: /terms of service|privacy policy/i }).first(), B4, { group: g, title: 'Legal link', sel: 'a:has-text("Terms of Service")' });
  save();
}

async function footer() {
  // The footer is measured on the home page, so home must be the document that
  // is actually open — assigning `current` alone would keep another page's
  // readings under the wrong url.
  if (!(await newPage('home'))) return;
  const g = G.footer;
  const fl = q('footer a.br-footer-link, footer a.footer-link').filter({ visible: true }).first();
  if (await fl.count()) {
    await S('footer', q('footer'), ['default'], { group: g, title: 'Footer', sel: 'footer' });
    await S('footer-link', fl, B4, { group: g, title: 'Footer link', sel: 'footer a.br-footer-link' });
    await S('footer-social', q('footer a').filter({ hasText: /\(opens in a new tab\)/ }).first(), B4, { group: g, title: 'Footer social icon', desc: 'One of the social icon links (X; Discord, LinkedIn and Reddit are the same control).', sel: 'footer social a' });
    await S('footer-legal', q('footer a').filter({ hasText: /privacy|terms|security|cookie/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Legal link', sel: 'footer a:has-text("Privacy")' });
  }
  save();
}

async function mobile() {
  if (!(await newPage('home', { mobile: true }))) return;
  const g = G.mobile;
  await S('m-header', q('header').first(), ['default'], { group: g, title: 'Mobile header', sel: 'header' }, { noScroll: true });
  const menuBtn = q('header button[aria-label*="menu" i]').first();
  if (await menuBtn.count()) {
    await S('m-menu-button', menuBtn, ['default', 'pressed'], { group: g, title: 'Mobile menu button', desc: 'The hamburger trigger at the right of the mobile bar; its own press opens the full-sheet menu.', sel: 'header button[aria-label*="menu"]' }, { noScroll: true });
    await S('m-menu-open', menuBtn, ['opened'], { group: g, title: 'Mobile menu, open', desc: 'The trigger after its own toggle; the open sheet shows in the crop.', sel: 'header menu trigger' }, { noScroll: true, cropLoc: q('body') });
    await page.keyboard.press('Escape'); await page.waitForTimeout(500);
  }
  save();
}

run = new Date().toISOString().slice(0, 10);
out._meta.read = run;
out._meta.viewport = '1440 x 900 (mobile group 390 x 844), light theme';
out._meta.tool = 'tools/capture/public/measure.mjs';
const { browser, context: ctx0 } = await launch();
context = ctx0;
const pages = process.argv.slice(2);
const plan = { home, pricing, signin, mobile };
const order = Object.keys(plan).filter((k) => !pages.length || pages.includes(k));
try {
  for (const k of order) { if (k !== 'mobile') await plan[k](); }
  if (!pages.length || pages.includes('home')) await footer();
  if (!pages.length || pages.includes('mobile')) await plan.mobile();
} finally {
  for (const [key, c] of Object.entries(out.components)) {
    // Prune only components on a page that actually opened this run: a blocked
    // or unvisited route keeps its earlier readings (write new captures first,
    // prune old outputs only after a complete run).
    if (!touched.has(key) && !pages.length) { if (opened.has(c.page)) delete out.components[key]; continue; }
    if (!touched.has(key)) continue;
    const want = listed.get(key);
    if (want) for (const st of Object.keys(c.states || {})) if (!want.has(st) && pages.length) delete c.states[st];
  }
  save();
  await browser.close().catch(() => {});
}
console.log('done ->', OUT);
