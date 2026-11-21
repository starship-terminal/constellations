// Measures vsco.co public components without submitting anything.
// Writes raw/components-computed.json and components/crops/.
import fs from 'node:fs';
import path from 'node:path';
import { BASE, launch, hideBanner, styleOf, crop, forcePseudo, RAW } from './lib.mjs';

fs.mkdirSync(RAW, { recursive: true });
const OUT = path.join(RAW, 'components-computed.json');
const out = { _meta: { product: 'VSCO', captured: '2026-11-21', url: BASE, theme: 'dark', widths: [1440, 390] }, components: {} };
const log = (...a) => console.log(...a);

async function record(page, name, state, locator, { pseudo } = {}) {
  const loc = locator.first();
  if (!(await loc.count())) { log('  miss', name, state); return; }
  if (!(await loc.isVisible().catch(() => false))) { log('  hidden', name, state); return; }
  let release;
  if (pseudo) release = await forcePseudo(page, loc, pseudo);
  await page.waitForTimeout(120);
  const style = await styleOf(loc);
  out.components[name] ??= { states: {} };
  out.components[name].states[state] = { ...style, via: pseudo || 'live' };
  try { await crop(page, loc, `${name}-${state}`); log('  crop', name, state); }
  catch (e) { log('  crop fail', name, state, e.message.split('\n')[0]); }
  if (release) await release();
}

async function homeDesktop(page) {
  await record(page, 'nav-logo', 'default', page.locator('a.nav_logo, a[aria-label="home"], header a').first());
  const products = page.locator('.menu_link.w-dropdown-toggle').filter({ hasText: 'PRODUCTS' });
  await record(page, 'nav-menu', 'default', products);
  await record(page, 'nav-menu', 'hover', products, { pseudo: 'hover' });
  await record(page, 'nav-menu', 'focus-visible', products, { pseudo: 'focus-visible' });
  await products.click();
  await page.waitForTimeout(400);
  await record(page, 'nav-menu', 'pressed', products);
  await record(page, 'menu-link', 'default', page.locator('.w-dropdown-list.w--open a.menu_dropdown-link').first());
  await record(page, 'menu-link', 'hover', page.locator('.w-dropdown-list.w--open a.menu_dropdown-link').first(), { pseudo: 'hover' });
  await page.keyboard.press('Escape');
  await page.mouse.click(700, 700);
  await page.waitForTimeout(200);

  const login = page.locator('a.button').filter({ hasText: /^LOG IN$/ }).last();
  await record(page, 'button-outline', 'default', login);
  await record(page, 'button-outline', 'hover', login, { pseudo: 'hover' });
  await record(page, 'button-outline', 'focus-visible', login, { pseudo: 'focus-visible' });
  const trial = page.locator('a.button').filter({ hasText: /TRY FOR FREE/ }).first();
  await record(page, 'button-primary', 'default', trial);
  await record(page, 'button-primary', 'hover', trial, { pseudo: 'hover' });
  await record(page, 'button-primary', 'focus-visible', trial, { pseudo: 'focus-visible' });
  await record(page, 'button-primary', 'pressed', trial, { pseudo: 'active' });

  const tab = page.locator('.w-tab-link').filter({ hasText: 'CREATE' });
  await record(page, 'tab', 'default', page.locator('.w-tab-link').first());
  await tab.click();
  await page.waitForTimeout(200);
  await record(page, 'tab', 'selected', tab);
  await record(page, 'hero-heading', 'default', page.locator('h1').first());
  await record(page, 'body-text', 'default', page.locator('p').filter({ hasText: /photographer/i }).first());
  await record(page, 'link', 'default', page.locator('footer a').first());
  await record(page, 'link', 'hover', page.locator('footer a').first(), { pseudo: 'hover' });
  await record(page, 'card', 'default', page.locator('.w-tab-pane.w--tab-active a').first());
}

async function plans(page) {
  const select = page.locator('a.button, a').filter({ hasText: /SELECT VSCO ONE|SELECT PRO/i }).first();
  await record(page, 'plan-cta', 'default', select);
  const faq = page.locator('button, [class*="accordion"]').filter({ hasText: /included in each|worth it/i }).first();
  if (await faq.count()) {
    await faq.scrollIntoViewIfNeeded();
    await record(page, 'accordion', 'default', faq);
    await faq.click();
    await page.waitForTimeout(300);
    await record(page, 'accordion', 'selected', faq);
  }
}

async function login(page) {
  const email = page.locator('input[name="identity"]');
  const password = page.locator('input[name="password"]');
  if (!(await email.count())) { log('  login form missing'); return; }
  await record(page, 'text-field', 'default', email);
  await email.focus();
  await page.waitForTimeout(150);
  await record(page, 'text-field', 'focus', email);
  await record(page, 'text-field-password', 'default', password);
  const submit = page.locator('button, input[type="submit"], a.button').filter({ hasText: /^LOG IN$/ }).first();
  await record(page, 'button-submit', 'default', submit);
  // Do not type, do not click Google or Apple, do not submit.
}

async function mobileHome(page) {
  const ham = page.locator('.w-nav-button, [aria-label="menu"]').first();
  await record(page, 'icon-button', 'default', ham);
  await ham.click();
  await page.waitForTimeout(400);
  await record(page, 'icon-button', 'pressed', ham);
  await record(page, 'drawer-link', 'default', page.locator('.w-nav-menu a').filter({ hasText: 'PRICING' }).first());
}

const { browser, context } = await launch({ width: 1440, height: 900 });
const page = await context.newPage();
const jobs = [
  [BASE + '/', homeDesktop],
  [BASE + '/subscribe/plans', plans],
  ['https://vsco.co/user/login', login],
];
for (const [url, fn] of jobs) {
  log('open', url);
  await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 45000 }).catch((e) => log('  goto', e.message.split('\n')[0]));
  await page.waitForTimeout(1600);
  await hideBanner(page);
  const blocked = await page.evaluate(() => /just a moment|security verification/i.test(document.title)).catch(() => true);
  if (blocked) { log('  blocked', url); continue; }
  await fn(page);
  fs.writeFileSync(OUT, JSON.stringify(out, null, 1));
}

const m = await launch({ mobile: true });
const mp = await m.context.newPage();
log('open mobile home');
await mp.goto(BASE + '/', { waitUntil: 'domcontentloaded', timeout: 45000 });
await mp.waitForTimeout(1500);
await hideBanner(mp);
await mobileHome(mp);
fs.writeFileSync(OUT, JSON.stringify(out, null, 1));
await browser.close();
await m.browser.close();
log('components', Object.keys(out.components).length);
