// Measure public Discord controls. Does not submit, type secrets, or click
// identity providers. Writes raw/components-computed.json and crops.
//
//   PLAYWRIGHT=... node measure.mjs
import fs from 'node:fs';
import path from 'node:path';
import { BASE, launch, styleOf, crop, RAW, CROPS } from './lib.mjs';

fs.mkdirSync(RAW, { recursive: true });
fs.mkdirSync(CROPS, { recursive: true });
const OUT = path.join(RAW, 'components-computed.json');
const out = { _meta: { source: 'https://discord.com/', capturedAt: new Date().toISOString(), route: 'public signed-out' }, components: {} };

const { browser, context } = await launch({ width: 1440, height: 900 });
const page = await context.newPage();
page.setDefaultTimeout(12000);

async function open(urlPath) {
  await page.goto(BASE + urlPath, { waitUntil: 'domcontentloaded', timeout: 60000 });
  await page.waitForTimeout(2000);
}

async function record(name, state, locator, note) {
  const n = await locator.count();
  if (!n) {
    out.components[name] = out.components[name] || { states: {} };
    out.components[name].states[state] = { missing: true, note: note || 'selector matched nothing' };
    console.log('  miss', name, state);
    return;
  }
  const loc = locator.first();
  const style = await styleOf(loc);
  let cropFile = null;
  try {
    cropFile = await crop(page, loc, `${name}-${state}`, 6);
  } catch (e) {
    cropFile = 'crop failed: ' + String(e.message).split('\n')[0];
  }
  out.components[name] = out.components[name] || { states: {} };
  out.components[name].states[state] = { style, crop: cropFile, note: note || null };
  console.log('  ok', name, state);
}

await open('/');
// Visible Download link in the desktop nav
await record('nav-link', 'default', page.locator('a.nav_link').filter({ hasText: 'Download' }), 'desktop nav link');
const navLink = page.locator('a.nav_link').filter({ hasText: 'Download' });
await navLink.first().hover();
await page.waitForTimeout(300);
await record('nav-link', 'hover', navLink, 'real hover');

await record('nav-login', 'default', page.locator('a').filter({ hasText: /^Log In$/ }).locator('visible=true'), 'login link, not followed');

const hero = page.locator('a, button').filter({ hasText: 'Download for Mac' }).locator('visible=true');
await record('button-download', 'default', hero, 'hero download link');
if (await hero.count()) {
  await hero.first().hover();
  await page.waitForTimeout(300);
  await record('button-download', 'hover', hero, 'real hover');
}

const openApp = page.getByRole('button', { name: 'Open Discord in your browser' });
await record('button-open-app', 'default', openApp, 'hero button. Not clicked. It leads to the login wall.');

// Discover menu
const toggles = page.locator('.nav_dd_trigger').filter({ hasText: 'Discover' });
const n = await toggles.count();
for (let i = 0; i < n; i++) {
  const box = await toggles.nth(i).boundingBox();
  if (box && box.width > 20 && box.y < 120) {
    await toggles.nth(i).hover();
    await page.waitForTimeout(500);
    break;
  }
}
await record('menu-discover', 'opened', page.locator('.nav_dd_list.w--open').first(), 'hover opened the Discover menu');

await open('/login');
await record('login-heading', 'default', page.locator('h1'), 'login wall heading. Form not filled.');
await record('login-field', 'default', page.locator('input[name="email"]'), 'email or phone field, empty, not typed');
await record('login-password', 'default', page.locator('input[name="password"]'), 'password field, empty, not typed');
const loginBtn = page.getByRole('button', { name: 'Log In' });
await record('login-submit', 'default', loginBtn, 'submit control. Not clicked.');

await open('/servers');
const search = page.locator('input[type="search"], input[name="search"]').first();
await record('search-field', 'default', search, 'server search, not submitted');
if (await search.count()) {
  await search.click();
  await page.waitForTimeout(300);
  await record('search-field', 'focused', search, 'clicked, not submitted');
}

fs.writeFileSync(OUT, JSON.stringify(out, null, 2) + '\n');
console.log('wrote', OUT);
await browser.close();
