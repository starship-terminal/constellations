// Measures forhims.co.uk public components. Consent is hidden, never clicked.
// Nothing is submitted. The register drawer is opened and closed; Create account is not pressed.
//
//   PLAYWRIGHT=... node measure.mjs
import fs from 'node:fs';
import path from 'node:path';
import { BASE, CROPS, RAW, crop, hideConsent, launchBrowser, newContext, open, styleOf } from './lib.mjs';

const OUT = path.join(RAW, 'components-computed.json');
fs.mkdirSync(RAW, { recursive: true });
fs.mkdirSync(CROPS, { recursive: true });

const out = { product: 'hims', host: 'www.forhims.co.uk', run: new Date().toISOString(), components: {} };
let page, current;

async function shot(loc, key, state) {
  const file = path.join(CROPS, `${key}-${state}.png`);
  await loc.scrollIntoViewIfNeeded().catch(() => {});
  await crop(loc, file, { pad: 8 });
  return `components/crops/${key}-${state}.png`;
}

async function S(key, loc, state, meta = {}) {
  const c = out.components[key] ??= { states: {} };
  Object.assign(c, { page: current, url: page.url().split('?')[0], ...meta });
  const style = await styleOf(loc);
  const file = await shot(loc, key, state);
  c.states[state] = { style, file };
  console.log('  ', key, state);
}

const browser = await launchBrowser();
const ctx = await newContext(browser, { width: 1440, height: 900, dpr: 1 });
page = await ctx.newPage();

current = 'home';
await open(page, BASE + '/', { wait: 1800 });
await hideConsent(page);

await S('logo', page.getByRole('link', { name: 'Link to homepage' }), 'default');
await S('nav-link', page.getByRole('link', { name: 'Weight', exact: true }), 'default');
const hair = page.getByRole('link', { name: 'Hair', exact: true });
await hair.hover();
await page.waitForTimeout(250);
await S('nav-link', hair, 'hover');
await S('login-button', page.getByRole('button', { name: 'Login' }).first(), 'default');
const login = page.getByRole('button', { name: 'Login' }).first();
await login.hover();
await page.waitForTimeout(200);
await S('login-button', login, 'hover');
await S('menu-button', page.locator('[data-testid="global-navigation-open-menu"]'), 'default');
const cta = page.getByRole('button', { name: 'Explore treatments' }).first();
await S('hero-cta', cta, 'default');
await cta.hover();
await page.waitForTimeout(250);
await S('hero-cta', cta, 'hover');
await page.keyboard.press('Tab');
await page.waitForTimeout(150);
await S('category-card', page.getByRole('link', { name: 'Lose weight' }), 'default');
const sexCard = page.getByRole('link', { name: 'Have great sex' });
await sexCard.hover();
await page.waitForTimeout(200);
await S('category-card', sexCard, 'hover');
await S('hero-title', page.getByRole('heading', { level: 2 }).first(), 'default');

await page.getByRole('button', { name: 'Sex', exact: true }).hover();
await page.waitForTimeout(500);
await hideConsent(page);
const sexItem = page.locator('a[href*="erectile"]').filter({ hasText: /Erectile|ED/ }).first();
const box = await sexItem.boundingBox().catch(() => null);
if (box && box.width > 8 && box.height > 8 && box.y < 900) {
  await S('nav-menu-link', sexItem, 'default', { note: 'Sex menu item' });
} else {
  console.log('  skip nav-menu-link', box);
}

current = 'login';
await open(page, BASE + '/customer/login', { wait: 1600 });
await hideConsent(page);
await S('login-title', page.getByRole('heading', { name: 'Welcome back' }), 'default');
const email = page.locator('form input[name="email"]').first();
await S('input', email, 'default');
await email.focus();
await page.waitForTimeout(200);
await S('input', email, 'focus');
await email.fill('name@example.com');
await page.waitForTimeout(150);
await S('input', email, 'filled');
await email.fill('');
await email.blur();
await page.waitForTimeout(250);
const err = page.getByText('Your email is required');
if (await err.count()) await S('input-error', err, 'default');
await S('login-submit', page.getByRole('button', { name: 'Login', exact: true }).last(), 'disabled');
await S('text-button', page.getByRole('button', { name: 'Forgot your password?' }), 'default');
await S('text-button', page.getByRole('button', { name: 'Create an account' }), 'create');

await page.getByRole('button', { name: 'Create an account' }).click();
await page.waitForTimeout(700);
await hideConsent(page);
const drawer = page.locator('[data-cy="global-drawer.component-content-register"]');
await S('drawer', drawer, 'register');
const terms = page.locator('#enrolment-terms');
await S('checkbox', terms, 'default');
await terms.focus();
await page.waitForTimeout(150);
await S('checkbox', terms, 'focus');
const create = drawer.getByRole('button', { name: 'Create account' });
await S('create-account', create, 'disabled');
await page.keyboard.press('Escape');
await page.waitForTimeout(300);

current = 'footer';
await page.evaluate(() => scrollTo(0, document.body.scrollHeight));
await page.waitForTimeout(400);
await hideConsent(page);
const footer = page.locator('footer').first();
if (await footer.count()) await S('footer-link', footer.getByRole('link', { name: 'About Us' }), 'default');

fs.writeFileSync(OUT, JSON.stringify(out, null, 2));
console.log('wrote', OUT, 'components', Object.keys(out.components).length);
await browser.close();
