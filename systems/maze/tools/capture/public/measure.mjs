// Measures Maze's public signed-out components. Nothing is submitted, signed
// into, or started as a study.
//
//   PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs node measure.mjs
//
// Marketing CTAs are an <a> wrapping a painted <button>. Selectors mark the
// painted button with data-m-mark so a crop is the control, not the page.
import fs from 'node:fs';
import path from 'node:path';
import { BASE, AUTH, requireReport, maskReport, launch, open, styleOf, crop, centre, RAW, hideConsent } from './lib.mjs';
import { startRun, touch, readOk, readFailed } from './dates.mjs';

const REPORT = requireReport();   // the sample report's share link, from the environment (lib.mjs)
fs.mkdirSync(RAW, { recursive: true });
fs.mkdirSync(path.join(RAW, '..', 'components', 'crops'), { recursive: true });
const OUT = path.join(RAW, 'components-computed.json');
// Start from the committed readings and merge into them, so a run that dies on one page leaves every
// other component as it was (the kit's approach) instead of a file missing every later component.
const previous = fs.existsSync(OUT) ? JSON.parse(fs.readFileSync(OUT, 'utf8')) : {};
// Dates follow dates.mjs: _meta.read and each component's `read` move only when a state is
// actually read, kept readings take the earlier date, and _meta.lastAttempt records this run.
// _meta.captured stays the first capture's date (it used to become today on every run).
const today = new Date().toLocaleDateString('en-CA');
const out = startRun(previous, today);
Object.assign(out._meta, {
  product: 'Maze',
  route: 'public-web',
  theme: 'light',
  note: 'Signed out. CookieYes and OneTrust hidden, never clicked. Login fields focused and filled with a sample string, then cleared. Nothing submitted. No study started.',
});
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const save = () => fs.writeFileSync(OUT, maskReport(JSON.stringify(out, null, 1)) + '\n');
const freshThisRun = new Set();
const earlier = new Map();   // key -> the states the committed file held, for a failed reread

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
  const c = (out.components[key] ??= { states: {}, ...meta, url: current });
  Object.assign(c, meta, { url: current });
  delete c.missing;   // found now: a missing flag seeded from the committed readings must not hide this reading
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
    return;
  }
  // Found: start this component afresh on its first call in this run, so neither an old missing flag
  // nor states this run no longer reads survive from the committed file. A later call for the same
  // component (the platform menu reads default, then hover) adds to it.
  // touch() keeps the component's earlier read date and states aside until a state is read again.
  if (!freshThisRun.has(key)) { touch(out, earlier, key, { ...meta, url: current }); freshThisRun.add(key); }
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
  const el = document.querySelector('header a[href="/"]');
  if (!el) return false;
  const r = el.getBoundingClientRect();
  if (r.width < 2) return false;
  el.setAttribute('data-m-mark', t);
  return true;
}), ['default'], { title: 'Wordmark', group: 'Navigation', sel: 'header a[href="/"]' });
await states('nav-link', await mark(page, 'nav-link', (t) => {
  const el = [...document.querySelectorAll('header a')].find((a) => {
    const r = a.getBoundingClientRect();
    return (a.getAttribute('href') || '') === '/pricing/' && r.y < 70 && r.height > 10 && r.height < 80;
  });
  if (!el) return false;
  el.setAttribute('data-m-mark', t);
  return true;
}), B, { title: 'Nav link', group: 'Navigation', sel: 'header a[href="/pricing/"] in the nav row' });
await states('nav-login', await mark(page, 'nav-login', (t) => {
  const el = [...document.querySelectorAll('header a')].find((a) => {
    const r = a.getBoundingClientRect();
    return /auth\.maze\.co\/login/.test(a.href) && r.y < 90 && r.width > 20 && r.width < 80;
  });
  if (!el) return false;
  el.setAttribute('data-m-mark', t);
  return true;
}), B, { title: 'Log in', group: 'Link', sel: 'header a[href*=auth.maze.co/login] in the nav row. The label is text, not a nested button.' });
await states('nav-try', await mark(page, 'nav-try', (t) => {
  const el = [...document.querySelectorAll('header a')].find((a) => /signup/.test(a.href))?.querySelector('button');
  if (!el || el.getBoundingClientRect().width < 2) return false;
  el.setAttribute('data-m-mark', t);
  return true;
}), B, { title: 'Try Maze for free', group: 'Button', sel: 'header signup button (pill, hairline)' });
await states('nav-demo', await mark(page, 'nav-demo', (t) => {
  const el = [...document.querySelectorAll('header a')].find((a) => (a.getAttribute('href') || '') === '/demo/')?.querySelector('button');
  if (!el || el.getBoundingClientRect().width < 2) return false;
  el.setAttribute('data-m-mark', t);
  return true;
}), B, { title: 'Get a demo', group: 'Button', sel: 'header a[href="/demo/"] button (filled)' });
await states('hero-title', page.locator('h1').first(), ['default'], {
  title: 'Hero title', group: 'Type', sel: 'h1',
});

// Platform menu: hover opens it. Measure one item, then move away. Do not click the item.
const platHit = await page.evaluate(() => {
  const el = [...document.querySelectorAll('header a[href="/platform/"]')].find((a) => {
    const r = a.getBoundingClientRect();
    return r.y < 70 && r.height > 10 && r.height < 80 && r.width > 40;
  });
  if (!el) return null;
  el.setAttribute('data-m-mark', 'nav-platform');
  const r = el.getBoundingClientRect();
  return { x: r.x + 24, y: r.y + r.height / 2 };
});
if (platHit) {
  const plat = page.locator('[data-m-mark="nav-platform"]');
  await states('nav-platform', plat, ['default'], { title: 'Platform menu trigger', group: 'Menu', sel: 'header a[href="/platform/"] in the nav row' });
  await page.mouse.move(platHit.x, platHit.y);
  await page.waitForTimeout(700);
  await states('nav-platform', plat, ['hover'], { title: 'Platform menu trigger', group: 'Menu', sel: 'header a[href="/platform/"] in the nav row' });
  const item = await mark(page, 'menu-item', (t) => {
    const el = [...document.querySelectorAll('header a')].find((a) => {
      const r = a.getBoundingClientRect();
      return (a.getAttribute('href') || '') === '/features/research-panel/' && r.y > 70 && r.y < 400 && r.height > 12 && r.height < 60;
    });
    if (!el) return false;
    el.setAttribute('data-m-mark', t);
    return true;
  });
  await states('menu-item', item, ['default', 'hover'], { title: 'Platform menu item', group: 'Menu', sel: 'header a[href="/features/research-panel/"] while the menu is open' });
  await page.mouse.move(8, 500);
  await page.waitForTimeout(300);
}
save();

await newPage(BASE + '/pricing/');
await states('plan-title', page.getByRole('heading', { name: 'Starter', exact: true }).first(), ['default'], {
  title: 'Plan title', group: 'Card', sel: 'heading Starter',
});
await states('plan-cta', await mark(page, 'plan-cta', (t) => {
  const a = [...document.querySelectorAll('a')].find((n) => /plan=starter/.test(n.href));
  const el = a?.querySelector('button') || [...document.querySelectorAll('a,button')].find((n) => {
    const r = n.getBoundingClientRect();
    return /sign up now/i.test(n.innerText || '') && r.height > 30 && r.height < 80;
  });
  if (!el || el.getBoundingClientRect().width < 2) return false;
  el.setAttribute('data-m-mark', t);
  return true;
}), B, { title: 'Starter sign up', group: 'Button', sel: 'pricing Starter CTA; not clicked' });
await states('plan-card', await mark(page, 'plan-card', (t) => {
  const h = [...document.querySelectorAll('h2,h3')].find((n) => (n.innerText || '').trim() === 'Starter');
  if (!h) return false;
  let el = h;
  for (let i = 0; i < 8 && el.parentElement; i++) {
    el = el.parentElement;
    const r = el.getBoundingClientRect();
    if (r.width > 280 && r.width < 560 && r.height > 280) break;
  }
  el.setAttribute('data-m-mark', t);
  return true;
}), ['default'], { title: 'Starter plan card', group: 'Card', sel: 'ancestor of the Starter heading, 280-560px wide' });
save();

await newPage(AUTH + '/login');
await states('login-title', page.getByRole('heading', { name: /log in to maze/i }), ['default'], {
  title: 'Login title', group: 'Type', sel: 'h1 Log in to Maze',
});
await states('login-email', page.locator('input[name="email"]'), ['default', 'focused', 'filled'], {
  title: 'Email field', group: 'Field', sel: 'input[name=email]',
});
await states('login-password', page.locator('input[name="password"]'), ['default', 'focused'], {
  title: 'Password field', group: 'Field', sel: 'input[name=password]; never filled',
});
await states('login-submit', page.locator('button[type="submit"]'), ['default', 'hover', 'focus-visible', 'pressed'], {
  title: 'Log in button', group: 'Button', sel: 'button[type=submit]; pressed via CDP, never clicked',
});
await states('login-google', page.getByRole('button', { name: /continue with google/i }), B, {
  title: 'Continue with Google', group: 'Button', sel: 'button Continue with Google; never clicked',
});
await states('login-sso', page.getByRole('link', { name: /continue with sso/i }), B, {
  title: 'Continue with SSO', group: 'Link', sel: 'a Continue with SSO; never clicked',
});
await states('login-reset', page.getByRole('link', { name: /reset password/i }), ['default', 'hover'], {
  title: 'Reset password', group: 'Link', sel: 'a Reset password; never clicked',
});
save();

await newPage(REPORT);
await states('report-title', page.getByRole('heading').first(), ['default'], {
  title: 'Report title', group: 'Type', sel: 'first heading on the public sample report',
});
await states('report-signup', await mark(page, 'report-signup', (t) => {
  const el = [...document.querySelectorAll('a,button')].find((n) => {
    const r = n.getBoundingClientRect();
    return /sign up for free/i.test(n.innerText || '') && r.height > 24 && r.height < 60 && getComputedStyle(n).backgroundColor !== 'rgba(0, 0, 0, 0)';
  });
  if (!el) return false;
  el.setAttribute('data-m-mark', t);
  return true;
}), B, { title: 'Report sign up', group: 'Button', sel: 'painted Sign up for free on the public report; never clicked' });
await states('report-login', await mark(page, 'report-login', (t) => {
  const el = [...document.querySelectorAll('a,button')].find((n) => {
    const r = n.getBoundingClientRect();
    return /^login$/i.test((n.innerText || '').trim()) && r.height > 24 && r.height < 60 && r.width < 140;
  });
  if (!el) return false;
  el.setAttribute('data-m-mark', t);
  return true;
}), ['default', 'hover'], { title: 'Report login', group: 'Button', sel: 'Login on the public report; never clicked' });
save();

await newPage(BASE + '/demo/');
await states('demo-title', page.getByRole('heading').first(), ['default'], {
  title: 'Demo page title', group: 'Type', sel: 'first heading on /demo/',
});
const demoField = page.locator('input[type="email"], input[name="email"]').first();
if (await demoField.count()) {
  await states('demo-field', demoField, ['default', 'focused'], {
    title: 'Demo form field', group: 'Field', sel: 'first input on /demo/; focused only, nothing typed or submitted',
  });
}
save();

// Phone width: the menu trigger. Close the desktop browser first. launch()
// starts a new one, and the old process would stay open.
await context.close();
await browser.close();
({ browser, context } = await launch({ width: 390, height: 844, mobile: true }));
await newPage(BASE + '/');
await states('m-menu', page.getByRole('button', { name: /open navigation/i }), ['default', 'pressed'], {
  title: 'Open navigation', group: 'Navigation', sel: 'button Open navigation; pressed via CDP, not opened here',
});
const menuBtn = page.getByRole('button', { name: /open navigation/i });
if (await menuBtn.count()) {
  await menuBtn.click();
  await page.waitForTimeout(600);
  await states('m-menu-open', await mark(page, 'm-menu-open', (t) => {
    const el = [...document.querySelectorAll('nav,div,dialog')].find((n) => {
      const r = n.getBoundingClientRect();
      return (n.innerText || '').includes('PRICING') && r.width > 200 && r.height > 180 && r.y < 220 && r.height < 900;
    });
    if (!el) return false;
    el.setAttribute('data-m-mark', t);
    return true;
  }), ['default'], { title: 'Mobile menu', group: 'Menu', sel: 'opened mobile navigation; local toggle only' });
}
save();

await context.close();
await browser.close();
log('wrote', OUT, Object.keys(out.components).length, 'components');
