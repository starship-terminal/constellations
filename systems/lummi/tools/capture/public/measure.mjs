// Measures a short list of public Lummi controls and writes crops plus raw/components-computed.json.
// Does not type into login, newsletter, or profile fields. Does not submit.
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { launch, open, closePromo, styleOf, crop, BASE, CROPS, RAW } from './lib.mjs';

fs.mkdirSync(CROPS, { recursive: true });
fs.mkdirSync(RAW, { recursive: true });

const { browser, context } = await launch({ width: 1440, height: 900 });
const page = await context.newPage();
const out = { components: {}, _meta: { source: 'https://www.lummi.ai/ signed out 1440x900', readAt: new Date().toISOString().slice(0, 10) } };

async function shot(key, state, loc) {
  const target = loc.first();
  if (!(await target.count())) { console.log('missing', key, state); return; }
  await target.scrollIntoViewIfNeeded().catch(() => {});
  const style = await styleOf(target);
  const file = `${key}-${state}.png`;
  await crop(page, target, `${key}-${state}`, 8);
  const c = (out.components[key] ??= { states: {} });
  c.states[state] = { file, style };
  console.log('crop', file);
}

await open(page, BASE + '/', { wait: 2500 });
await closePromo(page);
const close = page.getByRole('button', { name: 'Close', exact: true });
if (await close.count()) await close.first().click({ force: true }).catch(() => {});
await page.waitForTimeout(300);

await shot('button-primary', 'default', page.getByRole('button', { name: 'Try Pro for free' }));
await page.getByRole('button', { name: 'Try Pro for free' }).hover();
await page.waitForTimeout(300);
await shot('button-primary', 'hover', page.getByRole('button', { name: 'Try Pro for free' }));

await shot('nav-link', 'default', page.getByRole('link', { name: 'Illustrations', exact: true }));
await page.getByRole('link', { name: 'Illustrations', exact: true }).hover();
await page.waitForTimeout(250);
await shot('nav-link', 'hover', page.getByRole('link', { name: 'Illustrations', exact: true }));

await shot('text-field', 'default', page.getByPlaceholder('Search or create anything!'));
await page.getByPlaceholder('Search or create anything!').focus();
await page.waitForTimeout(250);
await shot('text-field', 'focus', page.getByPlaceholder('Search or create anything!'));
await page.keyboard.press('Escape');

await page.getByRole('button', { name: 'footer-dropdown' }).click();
await page.waitForTimeout(500);
await shot('menu', 'open', page.getByRole('dialog', { name: 'overflow-menu' }));
await page.keyboard.press('Escape');

await page.getByRole('button', { name: 'Tools', exact: true }).click();
await page.waitForTimeout(400);
await shot('menu-tools', 'open', page.getByRole('menu'));
await page.keyboard.press('Escape');

await page.getByRole('button', { name: 'Try Pro for free' }).click();
await page.waitForTimeout(600);
const dialog = page.locator('[role="dialog"]').filter({ hasText: 'Unlock everything' });
await shot('dialog', 'pro', dialog);
await page.keyboard.press('Escape');

fs.writeFileSync(path.join(RAW, 'components-computed.json'), JSON.stringify(out, null, 2) + '\n');
await browser.close();
console.log('components', Object.keys(out.components).length);
