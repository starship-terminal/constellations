// Measures jetbrains.com public components without signing in or submitting.
//
//   PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs node measure.mjs
//
// Writes raw/components-computed.json and crops into components/crops/.
// Cookie banner is hidden, never answered. Login is measured at rest: identity
// providers and Continue with email are not clicked, and no email is typed.
import fs from 'node:fs';
import path from 'node:path';
import { BASE, ACCOUNT, launch, closePromo, styleOf, crop, RAW, CROPS } from './lib.mjs';

fs.mkdirSync(RAW, { recursive: true });
fs.mkdirSync(CROPS, { recursive: true });
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);

const out = {
  _meta: {
    product: 'JetBrains',
    readAt: '2026-11-18',
    source: 'live public pages on www.jetbrains.com and account.jetbrains.com/login at rest; Continue with email and identity providers were not clicked',
    viewport: '1440x900 desktop, 390x844 phone',
  },
  components: {},
};

async function settle(page, url) {
  await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 90000 });
  await page.waitForTimeout(3500);
  await closePromo(page);
  await page.addStyleTag({ content: '*{caret-color:transparent!important}' }).catch(() => {});
}

async function record(page, name, locator, states = ['default']) {
  const loc = locator.first();
  if (!(await loc.count())) { log('  miss', name); return; }
  const box = await loc.boundingBox();
  if (!box || box.width < 2 || box.height < 2) { log('  empty', name); return; }
  out.components[name] = { states: {}, page: page.url().split('?')[0] };
  for (const state of states) {
    try {
      if (state === 'hover') await loc.hover({ timeout: 4000 });
      if (state === 'focus') await loc.focus({ timeout: 4000 });
      if (state === 'pressed') {
        await page.mouse.move(box.x + box.width / 2, box.y + box.height / 2);
        await page.mouse.down();
      }
      await page.waitForTimeout(250);
      const style = await styleOf(loc);
      out.components[name].states[state] = style;
      await crop(page, loc, `${name}-${state}`, 10);
      log('  ', name, state, style?.rect);
    } catch (e) {
      log('  fail', name, state, String(e.message).split('\n')[0]);
    } finally {
      if (state === 'pressed') await page.mouse.up().catch(() => {});
    }
  }
  await page.mouse.move(2, 2).catch(() => {});
}

const { browser, context } = await launch({ width: 1440, height: 900 });
const page = await context.newPage();

await settle(page, BASE + '/');
await record(page, 'button-primary', page.getByRole('link', { name: 'Explore Air' }).first(), ['default', 'hover', 'focus']);
await record(page, 'link', page.getByRole('link', { name: 'Read the story' }).first(), ['default', 'hover']);
await record(page, 'nav', page.locator('header').first(), ['default']);
await record(page, 'nav-link', page.getByRole('button', { name: 'Products: Open submenu' }).first(), ['default', 'hover']);
await record(page, 'icon-button', page.getByRole('button', { name: 'Open search' }).first(), ['default', 'hover', 'focus']);
await record(page, 'card', page.locator('[class*="_card_"]').filter({ hasText: 'For teams' }).first(), ['default', 'hover']);
await record(page, 'banner', page.locator('text=Introducing Air').first(), ['default']);

await page.getByRole('button', { name: 'Products: Open submenu' }).first().click();
await page.waitForTimeout(800);
await record(page, 'menu', page.locator('[class*="submenu"], [class*="_menu_"]').filter({ hasText: 'All IDEs' }).first(), ['opened']);
await page.keyboard.press('Escape');

await page.getByRole('button', { name: 'Open search' }).first().click();
await page.waitForTimeout(700);
await record(page, 'search-field', page.locator('input[type="search"], input[placeholder*="Search" i], input').last(), ['opened']);
await page.keyboard.press('Escape');

await settle(page, BASE + '/store/?section=personal&billing=yearly');
await record(page, 'tabs', page.getByRole('button', { name: /For Individual Use/ }).first(), ['default']);
await record(page, 'badge', page.locator('text=Best offer').first(), ['default']);
await record(page, 'price-card', page.locator('text=All Products Pack').locator('xpath=ancestor::*[contains(@class,"card") or self::article or self::div][1]').first(), ['default']);
await record(page, 'button-buy', page.getByRole('link', { name: /Buy|Get/ }).first(), ['default', 'hover']);

await settle(page, ACCOUNT + '/login');
await record(page, 'oauth-button', page.getByRole('button', { name: 'Continue with Google' }), ['default', 'hover', 'focus']);
await record(page, 'oauth-button-gitlab', page.getByRole('button', { name: 'Continue with Gitlab' }), ['default']);
await record(page, 'oauth-button-wechat', page.getByRole('button', { name: 'Continue with WeChat' }), ['default']);
await record(page, 'oauth-button-bitbucket', page.getByRole('button', { name: 'Continue with Bitbucket' }), ['default']);
await record(page, 'oauth-button-email', page.getByRole('button', { name: 'Continue with email' }), ['default']);
await record(page, 'link-signup', page.getByRole('link', { name: 'Create an account' }), ['default']);
await record(page, 'login-card', page.locator('text=Log in to JetBrains').locator('xpath=ancestor::div[1]').first(), ['default']);

await page.close();
await context.close();

const mob = await browser.newContext({
  viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, isMobile: true, hasTouch: true, locale: 'en-US',
});
const mp = await mob.newPage();
await settle(mp, BASE + '/');
await record(mp, 'icon-button-menu', mp.getByRole('button', { name: 'Open main menu' }), ['default']);
await mp.getByRole('button', { name: 'Open main menu' }).click().catch(() => {});
await mp.waitForTimeout(700);
await record(mp, 'menu-mobile', mp.locator('nav, [class*="mobileMenu"], [role="dialog"]').filter({ hasText: 'Products' }).first(), ['opened']);
await mp.close();
await mob.close();
await browser.close();

fs.writeFileSync(path.join(RAW, 'components-computed.json'), JSON.stringify(out, null, 1) + '\n');
log('wrote', Object.keys(out.components).length, 'components');
