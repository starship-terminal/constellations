// Element screenshots of public controls. Headed Chrome. No form submit.
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';
import { chromium } from '/Users/kaichen/.design-systems/pw/node_modules/playwright/index.mjs';

const OUT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '../../../components/crops');
fs.mkdirSync(OUT, { recursive: true });

const browser = await chromium.launch({ channel: 'chrome', headless: false });
const ctx = await browser.newContext({ viewport: { width: 1440, height: 900 }, locale: 'en-US', deviceScaleFactor: 2 });
const page = await ctx.newPage();
await page.goto('https://www.washingtonpost.com/', { waitUntil: 'domcontentloaded', timeout: 50000 });
await page.waitForTimeout(2500);
await page.addStyleTag({ content: '[id^="softwall-"]{display:none!important}' }).catch(() => {});

async function shot(name, locator) {
  const el = locator.first();
  if (!(await el.count())) { console.log('miss', name); return; }
  await el.scrollIntoViewIfNeeded().catch(() => {});
  await el.screenshot({ path: path.join(OUT, name + '.png') }).catch((e) => console.log('fail', name, e.message.split('\n')[0]));
  console.log('crop', name);
}

const subscribe = page.locator('a[data-qa="subs-offer"], a:has-text("Save and subscribe")').first();
const signin = page.locator('a[href*="/subscribe/signin"]').first();
const searchBtn = page.getByRole('button', { name: 'Search and browse sections' });
const alerts = page.getByRole('button', { name: 'News alerts' });
const section = page.locator('a[href="https://www.washingtonpost.com/politics/"]').first();

await shot('button-subscribe-default', subscribe);
await subscribe.hover();
await page.waitForTimeout(200);
await shot('button-subscribe-hover', subscribe);
await subscribe.focus();
await page.waitForTimeout(150);
await shot('button-subscribe-focus-visible', subscribe);

await shot('button-signin-default', signin);
await signin.hover();
await shot('button-signin-hover', signin);
await signin.focus();
await shot('button-signin-focus-visible', signin);

await shot('icon-button-search-default', searchBtn);
await searchBtn.hover();
await shot('icon-button-search-hover', searchBtn);
await searchBtn.focus();
await shot('icon-button-search-focus-visible', searchBtn);

await shot('icon-button-alerts-default', alerts);
await shot('link-section-default', section);
await section.hover();
await shot('link-section-hover', section);

await searchBtn.click();
await page.waitForTimeout(700);
const field = page.locator('#query');
await shot('text-field-default', field);
await field.click();
await field.fill('public');
await page.waitForTimeout(200);
await shot('text-field-filled', field);
const drawer = page.locator('#sc-sections-nav-drawer');
await shot('menu-sections-default', drawer);
await page.keyboard.press('Escape');
await page.waitForTimeout(300);

await alerts.click();
await page.waitForTimeout(700);
const dialog = page.locator('[role=dialog]').filter({ hasText: 'NEWS ALERTS' });
await shot('dialog-alerts-default', dialog);
await page.keyboard.press('Escape');

const headline = page.locator('h2, h1').first();
await shot('headline-default', headline);
const logo = page.locator('a[aria-label*="Washington Post"], a[href*="masthead"]').first();
await shot('logo-default', logo);

await page.evaluate(() => scrollTo(0, document.body.scrollHeight));
await page.waitForTimeout(800);
await shot('footer-link-default', page.locator('footer a').first());
await shot('footer-default', page.locator('footer'));

await browser.close();
console.log('crops done', OUT);
