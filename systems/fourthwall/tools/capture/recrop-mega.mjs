// One-off: re-crop the Features mega-menu card with the menu held open.
// The measure run's crop raced the hover menu closing; this keeps the
// pointer on the trigger for the whole crop.
import { BASE, launch, patch, open, closePromo, crop } from './public/lib.mjs';

const { browser, context } = await launch({});
const page = await context.newPage();
await patch(context);
await open(page, BASE + '/');
await closePromo(page);

const trig = page.locator('.nav-bar a, .nav-bar [role="button"], .nav-bar .nav-link, .nav-bar .w-dropdown-toggle').filter({ hasText: /Features/i }).first();
await trig.hover({ timeout: 8000 });
await page.waitForTimeout(1200);
const openNow = await page.evaluate(() => {
  const c = document.querySelector('.mega-clip, .nav-menu .w-dropdown-list, [class*="mega"]');
  if (!c) return false;
  const r = c.getBoundingClientRect(), cs = getComputedStyle(c);
  return r.height > 60 && cs.display !== 'none' && parseFloat(cs.opacity) > 0.05;
});
console.log('menu open:', openNow);

const card = page.locator('a.mega-card:visible').first();
console.log('card count:', await page.locator('a.mega-card:visible').count());
const bb = await card.boundingBox();
console.log('card box:', bb);

// Keep hovering the trigger so a mouse-leave does not close the menu mid-shot.
const file = await crop(page, card, 'mega-card-default', 8);
console.log('wrote', file);

const stillOpen = await page.evaluate(() => {
  const c = document.querySelector('.mega-clip, [class*="mega"]');
  if (!c) return false;
  const r = c.getBoundingClientRect(), cs = getComputedStyle(c);
  return r.height > 60 && cs.display !== 'none';
});
console.log('menu still open after crop:', stillOpen);
await browser.close();
