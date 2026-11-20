// Measures Melius public signed-out components. Nothing is submitted, signed
// into, or purchased.
//
//   PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs node measure.mjs
//
// Controls are marked with data-m-mark so a crop is the control, not the page.
import fs from 'node:fs';
import path from 'node:path';
import { BASE, APP, DOCS, launch, open, styleOf, crop, centre, RAW, hideConsent } from './lib.mjs';
import { startRun, touch, readOk, readFailed } from './dates.mjs';

fs.mkdirSync(RAW, { recursive: true });
fs.mkdirSync(path.join(RAW, '..', 'components', 'crops'), { recursive: true });
const OUT = path.join(RAW, 'components-computed.json');
// Start from the committed readings and replace only what this run reads, so a page that fails
// part way keeps the earlier readings of every later component instead of dropping them.
const prev = fs.existsSync(OUT) ? JSON.parse(fs.readFileSync(OUT, 'utf8')) : { components: {} };
// Dates follow dates.mjs: _meta.read and each component's `read` move only when a state is
// actually read, kept readings take the earlier date, and _meta.lastAttempt records this run.
const today = new Date().toLocaleDateString('en-CA');
const done = new Set();
const earlier = new Map();   // key -> the states the committed file held, for a failed reread
const out = startRun(prev, today);
Object.assign(out._meta, {
  product: 'Melius',
  route: 'public-web',
  theme: 'light',
  note: 'Signed out. Consent banner hidden, never clicked. Login and signup fields focused and filled with a sample string, then cleared. Nothing submitted. Billing and OAuth not followed.',
});
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const save = () => fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');

let page, context, browser, cdp, current;

async function newPage(url) {
  if (page) await page.close().catch(() => {});
  page = await context.newPage();
  page.setDefaultTimeout(8000);
  cdp = await context.newCDPSession(page);
  await cdp.send('DOM.enable');
  await cdp.send('CSS.enable');
  current = url;
  log('open', url);
  await open(page, url, { wait: 2200 });
  await page.addStyleTag({ content: '*{caret-color:transparent!important}' });
  await hideConsent(page);
}

async function reset() {
  await page.mouse.move(8, 8).catch(() => {});
  await page.evaluate(() => document.activeElement && document.activeElement.blur && document.activeElement.blur()).catch(() => {});
  await page.waitForTimeout(120);
}

async function kbFocus(loc) {
  await loc.evaluate((el) => el.focus());
  await page.keyboard.press('Shift+Tab');
  await page.keyboard.press('Tab');
  let ok = await loc.evaluate((el) => el === document.activeElement || el.contains(document.activeElement));
  if (!ok) {
    await loc.evaluate((el) => el.focus());
    ok = await loc.evaluate((el) => el === document.activeElement || el.contains(document.activeElement));
  }
  await page.waitForTimeout(200);
  return ok ? 'Shift+Tab, Tab' : 'focus failed';
}

async function forcePseudo(loc, classes) {
  await page.evaluate(() => document.querySelectorAll('[data-m-force]').forEach((n) => n.removeAttribute('data-m-force')));
  await loc.evaluate((el) => el.setAttribute('data-m-force', '1'));
  const { root } = await cdp.send('DOM.getDocument', { depth: 0 });
  const { nodeId } = await cdp.send('DOM.querySelector', { nodeId: root.nodeId, selector: '[data-m-force]' });
  if (!nodeId) return async () => {};
  await cdp.send('CSS.forcePseudoState', { nodeId, forcedPseudoClasses: classes });
  await page.waitForTimeout(220);
  return async () => { await cdp.send('CSS.forcePseudoState', { nodeId, forcedPseudoClasses: [] }).catch(() => {}); };
}

async function record(key, state, loc, meta, via) {
  // A component this run reaches is rewritten from its new readings; one it never reaches keeps its
  // reading and date. Dates move only on a successful read (dates.mjs).
  if (!done.has(key)) { touch(out, earlier, key, { ...meta, url: current }); done.add(key); }
  const c = out.components[key];
  Object.assign(c, meta, { url: current });
  c.states ??= {};
  try {
    await centre(loc);
    await hideConsent(page);
    const s = await styleOf(loc);
    let file;
    try { file = await crop(page, loc, `${key}-${state}`); }
    catch (e) { s.cropError = String(e.message).slice(0, 160); }
    readOk(out, c, state, { ...s, crop: file, via }, today);
    log(' ', key, state, Math.round(s.rect.w) + 'x' + Math.round(s.rect.h), s.cropError || '');
  } catch (e) {
    readFailed(c, earlier.get(key), state, { error: String(e.message).slice(0, 180), via }, today);
    log(' !', key, state, String(e.message).slice(0, 120));
  }
}

async function states(key, loc, list, meta) {
  const target = loc.first();
  if (!(await target.count())) {
    log(' ! missing', key);
    // The absence was seen on this run, so the entry is dated today; no state was read, so
    // _meta.read stays where it was.
    out.components[key] = { missing: true, ...meta, url: current, read: today, states: {} };
    done.add(key);
    return;
  }
  for (const st of list) {
    await reset();
    let undo;
    let via = 'at rest';
    if (st === 'hover') {
      await target.hover({ timeout: 4000 }).catch(() => {});
      via = 'mouse hover';
      await page.waitForTimeout(280);
    } else if (st === 'focus-visible') {
      via = await kbFocus(target);
      if (via === 'focus failed') {
        // Keyboard focus never reached the element, so a reading now would be the element at rest
        // saved as its focus. Record the miss instead, as the kit does.
        if (!done.has(key)) { touch(out, earlier, key, { ...meta, url: current }); done.add(key); }
        readFailed(out.components[key], earlier.get(key), st, { skipped: 'focus failed: keyboard focus did not reach the element', via }, today);
        log('  -', key, st, 'skipped: focus failed');
        continue;
      }
    } else if (st === 'pressed') {
      undo = await forcePseudo(target, ['active', 'hover']);
      via = 'CDP forcePseudoState :active:hover; no click, so the control does not navigate or submit';
    } else if (st === 'focused') {
      await target.click({ timeout: 4000 });
      via = 'clicked into the field; nothing submitted';
      await page.waitForTimeout(180);
    } else if (st === 'filled') {
      await target.click({ timeout: 4000 });
      await target.fill('sample@example.com');
      via = 'sample text typed, then the field is cleared; nothing submitted';
      await page.waitForTimeout(150);
    }
    await record(key, st, target, meta, via);
    if (st === 'filled') await target.fill('').catch(() => {});
    if (undo) await undo();
  }
  await reset();
}

// Mark the painted control. Marketing wraps a <button> in an <a>; measuring
// the anchor reads the browser's unvisited-link colour.
async function mark(page, tag, pick) {
  const ok = await page.evaluate(pick, tag);
  return ok ? page.locator(`[data-m-mark="${tag}"]`) : page.locator('[data-m-mark="__none__"]');
}

const B = ['default', 'hover', 'focus-visible', 'pressed'];

({ browser, context } = await launch({ width: 1440, height: 900, dpr: 2 }));

await newPage(BASE + '/');
await states('wordmark', await mark(page, 'wordmark', (t) => {
  const el = document.querySelector('header a[href="/"], nav a[href="/"]');
  if (!el) return false;
  const r = el.getBoundingClientRect();
  if (r.width < 2 || r.y > 80) return false;
  el.setAttribute('data-m-mark', t);
  return true;
}), ['default'], { title: 'Wordmark', group: 'Navigation', sel: 'header a[href="/"] in the nav row' });
await states('nav-link', await mark(page, 'nav-link', (t) => {
  const el = [...document.querySelectorAll('header a, nav a')].find((a) => {
    const r = a.getBoundingClientRect();
    return (a.getAttribute('href') || '') === '/pricing' && r.y < 90 && r.height > 10 && r.height < 80;
  });
  if (!el) return false;
  el.setAttribute('data-m-mark', t);
  return true;
}), B, { title: 'Pricing link', group: 'Navigation', sel: 'nav a[href="/pricing"]' });
await states('nav-signin', await mark(page, 'nav-signin', (t) => {
  const el = [...document.querySelectorAll('header a, nav a')].find((a) => {
    const r = a.getBoundingClientRect();
    return /\/login/.test(a.href) && r.y < 90 && r.height > 20;
  });
  if (!el) return false;
  el.setAttribute('data-m-mark', t);
  return true;
}), B, { title: 'Sign In', group: 'Button', sel: 'nav a to /login. Yellow fill. Not clicked.' });
await states('nav-start', await mark(page, 'nav-start', (t) => {
  const el = [...document.querySelectorAll('header a, nav a')].find((a) => {
    const r = a.getBoundingClientRect();
    return /\/signup/.test(a.href) && /start for free/i.test(a.innerText || '') && r.y < 90 && r.height > 20;
  });
  if (!el) return false;
  el.setAttribute('data-m-mark', t);
  return true;
}), B, { title: 'Start for Free', group: 'Button', sel: 'nav a to /signup. Orange fill. Not clicked.' });
await states('hero-title', page.locator('h1').first(), ['default'], {
  title: 'Hero title', group: 'Type', sel: 'h1',
});
await states('hero-cta', await mark(page, 'hero-cta', (t) => {
  const el = [...document.querySelectorAll('a')].find((a) => {
    const r = a.getBoundingClientRect();
    return /get started for free/i.test(a.innerText || '') && r.height > 30 && r.y > 80 && r.y < 700;
  });
  if (!el) return false;
  el.setAttribute('data-m-mark', t);
  return true;
}), B, { title: 'Get started for free', group: 'Button', sel: 'hero a, orange fill. Not clicked.' });

// Product menu: hover the Product control. Measure one item. Do not click it.
const prodHit = await page.evaluate(() => {
  const el = [...document.querySelectorAll('header button, header a, nav button, nav a')].find((n) => {
    const r = n.getBoundingClientRect();
    return (n.innerText || '').trim() === 'Product' && r.y < 90 && r.height > 10 && r.height < 70;
  });
  if (!el) return null;
  el.setAttribute('data-m-mark', 'nav-product');
  const r = el.getBoundingClientRect();
  return { x: r.x + r.width / 2, y: r.y + r.height / 2 };
});
if (prodHit) {
  const prod = page.locator('[data-m-mark="nav-product"]');
  await states('nav-product', prod, ['default', 'hover'], { title: 'Product menu trigger', group: 'Menu', sel: 'nav control labelled Product' });
  await page.mouse.move(prodHit.x, prodHit.y);
  await page.waitForTimeout(700);
  const item = await mark(page, 'menu-item', (t) => {
    const el = [...document.querySelectorAll('a')].find((a) => {
      const r = a.getBoundingClientRect();
      return (a.getAttribute('href') || '') === '/product/ai-image-generator' && r.y > 40 && r.y < 500 && r.height > 12 && r.height < 80;
    });
    if (!el) return false;
    el.setAttribute('data-m-mark', t);
    return true;
  });
  await states('menu-item', item, ['default', 'hover'], { title: 'Product menu item', group: 'Menu', sel: 'a[href="/product/ai-image-generator"] while the menu is open. Not clicked.' });
  await page.mouse.move(8, 500);
  await page.waitForTimeout(200);
}
await states('footer-link', await mark(page, 'footer-link', (t) => {
  const el = [...document.querySelectorAll('footer a')].find((a) => (a.getAttribute('href') || '') === '/about');
  if (!el) return false;
  el.setAttribute('data-m-mark', t);
  return true;
}), ['default', 'hover'], { title: 'Footer link', group: 'Link', sel: 'footer a[href="/about"]' });
save();

await newPage(BASE + '/pricing');
await states('plan-title', page.getByRole('heading', { name: /creator/i }).first(), ['default'], {
  title: 'Creator plan title', group: 'Card', sel: 'heading whose text includes Creator',
});
await states('plan-cta', await mark(page, 'plan-cta', (t) => {
  const el = [...document.querySelectorAll('a')].find((n) => {
    const r = n.getBoundingClientRect();
    return /start with creator/i.test(n.innerText || '') && r.height > 24 && r.height < 80;
  });
  if (!el) return false;
  el.setAttribute('data-m-mark', t);
  return true;
}), B, { title: 'Start with Creator', group: 'Button', sel: 'pricing a to /billing. Not clicked.' });
await states('plan-card', await mark(page, 'plan-card', (t) => {
  const a = [...document.querySelectorAll('a')].find((n) => /start with creator/i.test(n.innerText || ''));
  if (!a) return false;
  let el = a;
  for (let i = 0; i < 8 && el.parentElement; i++) {
    el = el.parentElement;
    const r = el.getBoundingClientRect();
    if (r.width > 220 && r.width < 480 && r.height > 200) break;
  }
  el.setAttribute('data-m-mark', t);
  return true;
}), ['default'], { title: 'Creator plan card', group: 'Card', sel: 'ancestor of Start with Creator, 220-480px wide' });
save();

await newPage(APP + '/login');
await states('login-title', page.getByRole('heading').first(), ['default'], {
  title: 'Login title', group: 'Type', sel: 'first heading on app.melius.com/login',
});
const email = page.locator('input[type="email"], input[name="email"], input[autocomplete="email"]').first();
if (await email.count()) {
  await states('login-email', email, ['default', 'focused', 'filled'], {
    title: 'Email field', group: 'Field', sel: 'first email input on /login. Sample text cleared. Nothing submitted.',
  });
}
const password = page.locator('input[type="password"]').first();
if (await password.count()) {
  await states('login-password', password, ['default', 'focused'], {
    title: 'Password field', group: 'Field', sel: 'input[type=password]; never filled',
  });
}
const submit = page.locator('button[type="submit"]').first();
if (await submit.count()) {
  await states('login-submit', submit, ['default', 'hover', 'focus-visible', 'pressed'], {
    title: 'Log in button', group: 'Button', sel: 'button[type=submit]; pressed via CDP, never clicked',
  });
}
const google = page.getByRole('button', { name: /google/i }).first();
if (await google.count()) {
  await states('login-google', google, B, {
    title: 'Continue with Google', group: 'Button', sel: 'button whose name includes Google; never clicked',
  });
}
save();

await newPage(APP + '/signup');
await states('signup-title', page.getByRole('heading').first(), ['default'], {
  title: 'Signup title', group: 'Type', sel: 'first heading on app.melius.com/signup',
});
const signupEmail = page.locator('input[type="email"], input[name="email"]').first();
if (await signupEmail.count()) {
  await states('signup-email', signupEmail, ['default', 'focused'], {
    title: 'Signup email', group: 'Field', sel: 'first email input on /signup; focused only, nothing typed or submitted',
  });
}
save();

await newPage(DOCS + '/');
await states('docs-title', page.getByRole('heading').first(), ['default'], {
  title: 'Docs title', group: 'Type', sel: 'first heading on docs.melius.com',
});
await states('docs-link', page.locator('a').nth(3), ['default', 'hover'], {
  title: 'Docs link', group: 'Link', sel: 'fourth link on the docs home; not followed',
});
save();

await newPage(BASE + '/contact');
const contactField = page.locator('input, textarea').first();
if (await contactField.count()) {
  await states('contact-field', contactField, ['default', 'focused'], {
    title: 'Contact field', group: 'Field', sel: 'first field on /contact; focused only, nothing typed or submitted',
  });
}
save();

await context.close();
await browser.close();
({ browser, context } = await launch({ width: 390, height: 844, mobile: true }));
await newPage(BASE + '/');
const menuBtn = page.locator('button[aria-label*="menu" i], button[aria-label*="Menu" i], header button').first();
if (await menuBtn.count()) {
  await states('m-menu', menuBtn, ['default', 'pressed'], {
    title: 'Mobile menu button', group: 'Navigation', sel: 'first header button at 390; pressed via CDP',
  });
  await menuBtn.click().catch(() => {});
  await page.waitForTimeout(500);
  await states('m-menu-link', await mark(page, 'm-menu-link', (t) => {
    const el = [...document.querySelectorAll('a')].find((a) => {
      const r = a.getBoundingClientRect();
      return (a.getAttribute('href') || '') === '/pricing' && r.width > 40 && r.height > 16 && r.y > 40;
    });
    if (!el) return false;
    el.setAttribute('data-m-mark', t);
    return true;
  }), ['default'], { title: 'Mobile pricing link', group: 'Menu', sel: 'a[href="/pricing"] after the menu toggle' });
}
save();

await context.close();
await browser.close();
log('wrote', OUT, Object.keys(out.components).length, 'components');
