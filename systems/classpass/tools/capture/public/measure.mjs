// Measures ClassPass public components. One fresh browser per page.
// Does not fill forms, submit, or click Apple, Google, Facebook, or SSO.
// Cookie banners are hidden, never accepted.
import fs from 'node:fs';
import path from 'node:path';
import { BASE, launch, hideConsent, styleOf, CROPS, RAW } from './lib.mjs';

fs.mkdirSync(CROPS, { recursive: true });
fs.mkdirSync(RAW, { recursive: true });
const OUT = path.join(RAW, 'components-computed.json');
const out = fs.existsSync(OUT) ? JSON.parse(fs.readFileSync(OUT, 'utf8')) : { _meta: {}, components: {} };
out.components ??= {};
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);

async function hide(page) {
  await hideConsent(page);
  await page.addStyleTag({ content: '*{caret-color:transparent!important}' }).catch(() => {});
}

async function shot(loc, name) {
  const file = path.join(CROPS, name + '.png');
  try {
    await loc.scrollIntoViewIfNeeded();
    await loc.screenshot({ path: file });
    return file;
  } catch (e) {
    log('  crop fail', name, e.message.split('\n')[0]);
    return null;
  }
}

async function record(name, state, loc, extra = {}) {
  const reading = await styleOf(loc);
  const crop = await shot(loc, `${name}-${state}`);
  out.components[name] ??= { states: {} };
  out.components[name].states[state] = { ...reading, crop: crop ? path.basename(crop) : null, ...extra };
  log('  ', name, state, reading.text, reading.style.fontSize, reading.style.color, reading.style.backgroundColor);
}

async function withPage(url, fn) {
  const { browser, context } = await launch();
  const page = await context.newPage();
  page.setDefaultTimeout(12000);
  log('open', url);
  await page.goto(BASE + url, { waitUntil: 'domcontentloaded', timeout: 60000 });
  await page.waitForTimeout(2500);
  await hide(page);
  try { await fn(page); } catch (e) { log('  PAGE FAIL', url, e.message.split('\n')[0]); }
  fs.writeFileSync(OUT, JSON.stringify(out, null, 2) + '\n');
  await browser.close();
}

function first(page, sel) { return page.locator(sel).first(); }

await withPage('/', async (page) => {
  out._meta.home = { url: page.url(), title: await page.title(), at: new Date().toISOString() };
  const header = page.locator('header').first();
  if (await header.count()) await record('header', 'default', header);

  const login = page.getByRole('link', { name: 'Log in', exact: true }).first();
  if (await login.count()) {
    await record('nav-link', 'default', login);
    await login.hover();
    await page.waitForTimeout(300);
    await record('nav-link', 'hover', login);
  }

  const cta = page.locator('header a').filter({ hasText: 'Get 14 days free' }).last();
  if (await cta.count()) {
    await record('button-primary', 'default', cta);
    await cta.hover();
    await page.waitForTimeout(300);
    await record('button-primary', 'hover', cta);
  }

  const how = page.getByRole('button', { name: 'How it works' }).first();
  if (await how.count()) {
    await record('menu-button', 'default', how);
    await how.click();
    await page.waitForTimeout(500);
    const item = page.getByRole('link', { name: 'How ClassPass works' }).first();
    if (await item.count()) await record('menu-item', 'default', item);
    const menu = page.locator('[role="menu"], [aria-haspopup] + *, header ul, header [class*="menu"]').first();
    await page.keyboard.press('Escape');
  }

  const heroCta = page.getByRole('link', { name: 'Get 14 days free' }).nth(2);
  if (await heroCta.count()) await record('button-dark', 'default', heroCta);
  const learn = page.getByRole('link', { name: 'Learn more about ClassPass' }).first();
  if (await learn.count()) {
    await record('button-outline', 'default', learn);
    await learn.hover();
    await page.waitForTimeout(250);
    await record('button-outline', 'hover', learn);
  }

  const display = page.locator('[class*="word"], [class*="Display"], [class*="ticker"]').filter({ hasText: /beauty|wellness|fitness|gyms/i }).first();
  if (await display.count()) await record('display', 'default', display);

  const legal = page.locator('p, small, span').filter({ hasText: 'Offer available for new members' }).first();
  if (await legal.count()) await record('caption', 'default', legal);

  const fees = page.getByRole('link', { name: 'fees' }).first();
  if (await fees.count()) await record('link', 'default', fees);

  await page.evaluate(() => scrollTo(0, document.body.scrollHeight));
  await page.waitForTimeout(400);
  await hide(page);
  const footer = page.locator('footer').first();
  if (await footer.count()) await record('footer', 'default', footer);
  const lang = page.getByRole('button', { name: /English|select site language/i }).first();
  if (await lang.count()) {
    await record('language-button', 'default', lang);
    await lang.click();
    await page.waitForTimeout(500);
    await record('language-button', 'open', lang);
    await page.keyboard.press('Escape');
  }
});

await withPage('/plans', async (page) => {
  const find = page.getByRole('link', { name: /Find your plan/i }).first();
  if (!(await find.count())) {
    const b = page.getByRole('button', { name: /Find your plan/i }).first();
    if (await b.count()) await record('button-ink', 'default', b);
  } else await record('button-ink', 'default', find);
  const heading = page.locator('h1, h2').filter({ hasText: /Choose how much/i }).first();
  if (await heading.count()) await record('heading', 'default', heading);
});

await withPage('/login', async (page) => {
  const email = page.getByLabel('Email address').first();
  if (await email.count()) {
    await record('text-field', 'default', email);
    await email.focus();
    await page.waitForTimeout(250);
    await record('text-field', 'focus', email);
  }
  const password = page.getByLabel('Password').first();
  if (await password.count()) await record('text-field-password', 'default', password);
  const submit = page.getByRole('button', { name: 'Log in', exact: true }).first();
  if (await submit.count()) await record('button-submit', 'default', submit);
  const apple = page.getByRole('button', { name: /Sign in with Apple/i }).first();
  if (await apple.count()) await record('button-sso', 'default', apple);
  const card = page.locator('form').first();
  if (await card.count()) await record('login-card', 'default', card);
  const forgot = page.getByRole('link', { name: /Forgot your password/i }).first();
  if (await forgot.count()) await record('link-inline', 'default', forgot);
});

await withPage('/search', async (page) => {
  const search = page.getByRole('textbox').first();
  if (await search.count()) {
    await record('search-field', 'default', search);
    await search.click();
    await page.waitForTimeout(200);
    await record('search-field', 'focus', search);
  }
  const fitness = page.getByRole('button', { name: 'Fitness' }).first();
  if (await fitness.count()) {
    await record('filter-chip', 'default', fitness);
    await fitness.click();
    await page.waitForTimeout(400);
    await record('filter-chip', 'open', fitness);
    const option = page.getByRole('option', { name: /Wellness/i }).first();
    const menuitem = page.getByText('Wellness', { exact: true }).first();
    const target = (await option.count()) ? option : menuitem;
    if (await target.count()) await record('filter-option', 'default', target);
    await page.keyboard.press('Escape');
  }
  const card = page.locator('a[href*="/studios/"]').first();
  if (await card.count()) await record('studio-card', 'default', card);
});

await withPage('/contact', async (page) => {
  const heading = page.locator('h1').first();
  if (await heading.count()) await record('page-title', 'default', heading);
});

await withPage('/gifts', async (page) => {
  const heading = page.locator('h1').first();
  if (await heading.count()) await record('page-title-gifts', 'default', heading);
});

fs.writeFileSync(OUT, JSON.stringify(out, null, 2) + '\n');
console.log('components', Object.keys(out.components).length);
