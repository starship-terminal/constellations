// Retakes the menu-state shots: the kebab is an empty <a> wrapping
// span.responsive-nav__icon inside .nav-dropdown/.responsive-nav. Clicks it
// (a local UI toggle) and screenshots the opened menu. Same rules as
// public.mjs: hide overlays, never consent, never submit.
//   RAW=<raw-shots> PLAYWRIGHT=<index.mjs> node fixup.mjs
import { screenshotWithMetadata } from '../screenshot.mjs';
import { closePromo, clearChallenge, patch, chromium, UA, UA_MOBILE, BASE } from './lib.mjs';

const RAW = process.env.RAW;
// No default: the shots belong in a scratch dir outside the repo, and an unset RAW
// used to write them to ./undefined/.
if (!RAW) { console.error('set RAW=<raw-shots dir> (a scratch dir outside the repo)'); process.exit(2); }
const wait = (p, ms) => p.waitForTimeout(ms);
const log = (...a) => console.log(...a);
const b = await chromium.launch();

for (const mob of [false, true]) {
  const ctx = await b.newContext(mob
    ? { viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, userAgent: UA_MOBILE, isMobile: true, hasTouch: true, locale: 'en-US' }
    : { viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1, userAgent: UA, locale: 'en-US' });
  await patch(ctx);
  const p = await ctx.newPage();
  await p.goto(BASE + '/', { waitUntil: 'domcontentloaded', timeout: 90000 }).catch(() => {});
  if (await clearChallenge(p)) {
    await wait(p, 9000);
    await closePromo(p);
    const name = mob ? 'mobile-home-light-menu' : 'home-light-menu';
    const req = mob ? { viewport: { width: 390, height: 844 }, deviceScaleFactor: 2 } : { viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1 };
    const kebab = p.locator('span.responsive-nav__icon').filter({ visible: true }).first();
    try {
      if (!(await kebab.count())) { log('  no kebab', name); }
      else {
        await kebab.click({ timeout: 5000 }).catch(() => kebab.evaluate((el) => (el.closest('a') || el).click()));
        await wait(p, 1600);
        log('  url after click:', await p.url());
        await screenshotWithMetadata(p, { path: `${RAW}/${name}.png` }, req);
        log('  shot', name);
      }
    } catch (e) { log('  menu failed', name, String(e.message).split('\n')[0]); }
  }
  await ctx.close();
}
await b.close();
log('done');
