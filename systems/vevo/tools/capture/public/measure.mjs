// Measures Vevo's public marketing pages. Nothing is submitted, signed into, or consented.
//
//   PLAYWRIGHT=... node tools/capture/public/measure.mjs
//
// Writes raw/components-computed.json and crops into components/crops/.
import fs from 'node:fs';
import path from 'node:path';
import { BASE, launch, open, styleOf, crop, RAW } from './lib.mjs';

fs.mkdirSync(RAW, { recursive: true });


const out = { _meta: { product: 'vevo', base: BASE, captured: '2026-11-21', route: 'public headless' }, components: {} };
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);

async function record(page, name, state, locator, extra = {}) {
  const n = await locator.count();
  if (!n) { log('  miss', name, state); return null; }
  const loc = locator.first();
  const box = await loc.boundingBox().catch(() => null);
  if (!box || box.width < 2 || box.height < 2) { log('  empty', name, state); return null; }
  const style = await styleOf(loc);
  const entry = { ...style, ...extra, state, page: page.url().replace(/\?.*$/, '') };
  out.components[name] ??= {};
  out.components[name][state] = entry;
  const file = `${name}-${state}`;
  await crop(page, loc, file).catch((e) => log('  crop fail', file, String(e.message).split('\n')[0]));
  log('  ok', name, state, Math.round(box.width), Math.round(box.height));
  return entry;
}

async function hover(page, loc) {
  const box = await loc.boundingBox();
  if (!box) return;
  await page.mouse.move(box.x + box.width / 2, box.y + Math.min(box.height / 2, 20));
  await page.waitForTimeout(350);
}

const { browser, context } = await launch({ width: 1440, height: 900 });
const page = await context.newPage();
page.setDefaultTimeout(12000);

async function go(url) {
  await open(page, url.startsWith('http') ? url : BASE + url, { wait: 2500 });
  await page.addStyleTag({ content: '*{caret-color:transparent!important}' }).catch(() => {});
}

await go('/');
await record(page, 'nav-link', 'default', page.getByRole('link', { name: 'About', exact: true }));
const about = page.getByRole('link', { name: 'About', exact: true }).first();
await hover(page, about);
await record(page, 'nav-link', 'hover', about);
await page.keyboard.press('Tab');
await page.keyboard.press('Tab');
await record(page, 'skip-link', 'focus', page.locator('#SKIP_TO_CONTENT_BTN'), { via: 'Tab' });

await record(page, 'hero-heading', 'default', page.locator('h1').first());
await record(page, 'body', 'default', page.locator('body'));
await record(page, 'footer-link', 'default', page.getByRole('link', { name: 'Privacy Policy' }).first());
await record(page, 'text-link', 'default', page.getByRole('link', { name: 'View All' }).first());
const viewAll = page.getByRole('link', { name: 'View All' }).first();
await hover(page, viewAll);
await record(page, 'text-link', 'hover', viewAll);

await record(page, 'play-button', 'default', page.getByRole('button', { name: /Play video/ }).first());
const play = page.getByRole('button', { name: /Play video/ }).first();
await hover(page, play);
await record(page, 'play-button', 'hover', play);

await record(page, 'news-card', 'default', page.locator('a[href*="/press/"]').first());
await record(page, 'logo', 'default', page.locator('header a, [id*="comp-"] a').first());

await go('/for-advertisers-contact');
const name = page.locator('input[name="name"]');
await record(page, 'text-field', 'default', name);
await name.click();
await page.waitForTimeout(250);
await record(page, 'text-field', 'focus', name, { via: 'click' });
// Do not type into the field. A filled crop would store sample text.
await record(page, 'select', 'default', page.locator('select').first());
await record(page, 'text-area', 'default', page.locator('textarea').first());
const area = page.locator('textarea').first();
await area.click();
await record(page, 'text-area', 'focus', area, { via: 'click' });
await record(page, 'checkbox', 'default', page.locator('input[type="checkbox"]').first());
const submit = page.getByRole('button', { name: 'Submit' }).first();
await record(page, 'button', 'default', submit);
await hover(page, submit);
await record(page, 'button', 'hover', submit);
// Empty invalid: blur a required field. Do not click Submit.
await name.focus();
await name.blur();
await page.waitForTimeout(200);
await record(page, 'text-field', 'blurred-empty', name, { note: 'required field blurred empty; form not submitted' });

await go('/for-artists-feedback');
await record(page, 'radio', 'default', page.locator('input[type="radio"]').first());

await go('/advertising/specs');
const preroll = page.getByRole('button', { name: 'Video Preroll' }).first();
await record(page, 'accordion', 'default', preroll);
await preroll.click().catch(() => {});
await page.waitForTimeout(500);
await record(page, 'accordion', 'expanded', preroll);

await go('/press/vevo-announces-highly-acclaimed-dscvr-artists-to-watch-list-for-2027');
await record(page, 'article-title', 'default', page.locator('h1').first());
await record(page, 'share-button', 'default', page.getByRole('button', { name: /Share via/ }).first());
const more = page.getByRole('button', { name: 'More actions' }).first();
if (await more.count()) {
  await more.click().catch(() => {});
  await page.waitForTimeout(400);
  await record(page, 'menu-button', 'open', more);
}

await go('/about');
await record(page, 'button-secondary', 'default', page.getByRole('button', { name: 'Start Now' }).first());
const start = page.getByRole('button', { name: 'Start Now' }).first();
await hover(page, start);
await record(page, 'button-secondary', 'hover', start);

// phone drawer
await page.close();
const mctx = await browser.newContext({
  viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, isMobile: true, hasTouch: true,
  userAgent: 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 Mobile/15E148 Safari/604.1',
  locale: 'en-US',
});
const mp = await mctx.newPage();
await open(mp, BASE + '/', { wait: 2500 });
await record(mp, 'menu-button', 'default', mp.locator('#comp-lklqhtjc_r_comp-ldc6q7ym'));
await mp.locator('#comp-lklqhtjc_r_comp-ldc6q7ym').click().catch(() => {});
await mp.waitForTimeout(700);
await record(mp, 'drawer-link', 'default', mp.getByRole('link', { name: 'Home', exact: true }));
await record(mp, 'drawer', 'open', mp.getByRole('dialog', { name: /navigation/i }).or(mp.locator('[role="dialog"]')).first());

fs.writeFileSync(path.join(RAW, 'components-computed.json'), JSON.stringify(out, null, 1) + '\n');
log('wrote', Object.keys(out.components).length, 'components');
await browser.close();
