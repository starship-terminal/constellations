// Measures The Org's public components. Nothing is submitted. Login, signup,
// Google, and contact forms are never opened.
//
//   PLAYWRIGHT=... node measure.mjs
import fs from 'node:fs';
import path from 'node:path';
import { BASE, launch, open, styleOf, crop, centre, RAW, hasPrivateContact, isAuthWall } from './lib.mjs';

const OUT = path.join(RAW, 'components-computed.json');
fs.mkdirSync(RAW, { recursive: true });
const out = { _meta: { product: 'theorg.com', capturedAt: new Date().toISOString().slice(0, 10), route: 'public-web' }, components: {} };
const log = (...a) => console.log(...a);

const browserBox = await launch();
const context = browserBox.context;
const page = await context.newPage();
const cdp = await context.newCDPSession(page);
await cdp.send('DOM.enable');
await cdp.send('CSS.enable');

async function forcePseudo(loc, classes) {
  await page.evaluate(() => document.querySelectorAll('[data-m-force]').forEach((n) => n.removeAttribute('data-m-force')));
  await loc.evaluate((el) => el.setAttribute('data-m-force', '1'));
  const { root } = await cdp.send('DOM.getDocument', { depth: 0 });
  const { nodeId } = await cdp.send('DOM.querySelector', { nodeId: root.nodeId, selector: '[data-m-force]' });
  await cdp.send('CSS.forcePseudoState', { nodeId, forcedPseudoClasses: classes });
  await page.waitForTimeout(250);
  return async () => { await cdp.send('CSS.forcePseudoState', { nodeId, forcedPseudoClasses: [] }).catch(() => {}); };
}

async function record(key, state, loc, meta) {
  const c = (out.components[key] ??= { states: {}, ...meta });
  Object.assign(c, meta);
  const target = loc.filter({ visible: true }).first();
  if (!(await target.count())) { log('  missing', key); c.missing = true; return; }
  await centre(target);
  const s = await styleOf(target);
  try { s.crop = await crop(page, target, `${key}-${state}`); } catch (e) { s.cropError = String(e.message).slice(0, 120); }
  c.states[state] = s;
  log(' ', key, state, s.rect.w + 'x' + s.rect.h, s.style.backgroundColor, s.style.color);
}

async function states(key, loc, meta) {
  await record(key, 'default', loc, meta);
  const target = loc.filter({ visible: true }).first();
  if (!(await target.count())) return;
  await target.hover();
  await page.waitForTimeout(250);
  await record(key, 'hover', loc, meta);
  await page.mouse.move(2, 2);
  try {
    await target.focus();
    await page.keyboard.press('Shift+Tab');
    await page.keyboard.press('Tab');
    await page.waitForTimeout(200);
    await record(key, 'focus-visible', loc, meta);
  } catch (e) { log('  focus failed', key, String(e.message).slice(0, 80)); }
  const release = await forcePseudo(target, ['hover', 'active']).catch(() => null);
  if (release) {
    await record(key, 'pressed', loc, meta);
    await release();
  }
}

await open(page, BASE + '/');
if (await isAuthWall(page) || await hasPrivateContact(page)) {
  console.log('home blocked'); process.exit(2);
}

await states('nav-signup', page.getByRole('link', { name: 'Sign up', exact: true }), { group: 'button', title: 'Sign up', page: 'home' });
await states('nav-login', page.getByRole('link', { name: 'Log in', exact: true }), { group: 'link', title: 'Log in', page: 'home' });
await states('nav-pricing', page.getByRole('link', { name: 'Pricing', exact: true }), { group: 'link', title: 'Pricing', page: 'home' });
await states('hero-cta', page.getByRole('link', { name: 'Start for free' }), { group: 'button', title: 'Start for free', page: 'home' });
await states('hero-secondary', page.getByRole('link', { name: 'Learn more' }), { group: 'link', title: 'Learn more', page: 'home' });
await states('nav-platform', page.getByRole('button', { name: 'Platform', exact: true }), { group: 'menu', title: 'Platform trigger', page: 'home' });

const h1 = page.locator('h1').first();
await record('hero-title', 'default', h1, { group: 'type', title: 'Hero title', page: 'home' });

await page.getByRole('button', { name: 'Platform', exact: true }).click();
await page.waitForTimeout(400);
await states('menu-link', page.getByRole('link', { name: /For Companies/ }), { group: 'menu', title: 'Platform menu link', page: 'home' });
await page.keyboard.press('Escape');

await open(page, BASE + '/pricing');
await record('plan-card', 'default', page.locator('text=Free forever').locator('xpath=ancestor::*[self::div][3]').first(), { group: 'card', title: 'Free plan', page: 'pricing' }).catch((e) => log('plan card', e.message));
await states('billing-monthly', page.getByText('Monthly', { exact: true }), { group: 'tabs', title: 'Monthly billing', page: 'pricing' });
await states('plan-cta', page.getByRole('link', { name: 'Get started' }).first(), { group: 'button', title: 'Get started', page: 'pricing' });

await open(page, BASE + '/explore/industries');
const search = page.locator('input').first();
await record('search-field', 'default', search, { group: 'text field', title: 'Industry search', page: 'explore' });
await search.focus();
await page.waitForTimeout(200);
await record('search-field', 'focus-visible', search, { group: 'text field', title: 'Industry search', page: 'explore' });

await open(page, BASE + '/org/five-blocks');
if (!(await hasPrivateContact(page))) {
  await record('org-title', 'default', page.locator('h1').first(), { group: 'type', title: 'Org title', page: 'org' });
  await states('org-tab', page.getByRole('button', { name: 'Teams', exact: true }).first(), { group: 'tabs', title: 'Teams tab', page: 'org' });
  await record('avatar', 'default', page.locator('img').nth(2), { group: 'avatar', title: 'Person avatar', page: 'org' });
}

await open(page, BASE + '/companies');
await states('directory-link', page.getByRole('link', { name: /^A$/ }).first(), { group: 'link', title: 'Letter index', page: 'companies' });

await open(page, BASE + '/');
const footer = page.locator('footer a').filter({ hasText: 'About' }).first();
await footer.scrollIntoViewIfNeeded();
await states('footer-link', footer, { group: 'link', title: 'Footer About', page: 'home' });

fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');
console.log('wrote', OUT, Object.keys(out.components).length, 'components');
await browserBox.browser.close();
