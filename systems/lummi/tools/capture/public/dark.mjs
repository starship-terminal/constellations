// Dark-theme pass. Lummi switches with prefers-color-scheme: dark when html has no
// data-theme="light" (systems/lummi/raw/css-vars.json, :root:not([data-theme="light"])).
// Same pages as the light pass's main templates. No forms, no login entry.
import fs from 'fs';
import os from 'os';
import path from 'path';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { closePromo, chromium, UA, UA_MOBILE, BASE } from './lib.mjs';

const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', 'lummi', 'raw-shots');
fs.mkdirSync(RAW, { recursive: true });
const log = (...a) => console.log(...a);
const wait = (p, ms) => p.waitForTimeout(ms);

const pages = [
  ['home', '/'],
  ['illustration', '/illustration'],
  ['3d', '/3d'],
  ['photo', '/photo/speaker-on-stage-8_rbc'],
  ['pro', '/pro'],
  ['blog', '/blog'],
  ['about', '/about'],
  ['explore', '/explore'],
  ['login', '/login'],
];
const mobile = [['home', '/'], ['photo', '/photo/speaker-on-stage-8_rbc'], ['pro', '/pro'], ['login', '/login']];

const b = await chromium.launch();
let n = 0;
for (const [mob, list] of [[false, pages], [true, mobile]]) {
  for (const [name, urlPath] of list) {
    const vw = mob ? 390 : 1440, vh = mob ? 844 : 900, dpr = mob ? 2 : 1;
    const ctx = await b.newContext({
      viewport: { width: vw, height: vh }, deviceScaleFactor: dpr,
      userAgent: mob ? UA_MOBILE : UA, isMobile: mob, hasTouch: mob,
      locale: 'en-US', colorScheme: 'dark',
    });
    const p = await ctx.newPage();
    const prefix = `${mob ? 'mobile-' : ''}${name}-dark`;
    const requested = { viewport: { width: vw, height: vh }, deviceScaleFactor: dpr };
    log(prefix);
    try {
      await p.goto(BASE + urlPath, { waitUntil: 'domcontentloaded', timeout: 60000 });
      await wait(p, 2200);
      await closePromo(p);
      const theme = await p.evaluate(() => ({ bg: getComputedStyle(document.body).backgroundColor, scheme: matchMedia('(prefers-color-scheme: dark)').matches }));
      log('  theme', JSON.stringify(theme));
      await screenshotWithMetadata(p, { path: `${RAW}/${prefix}-default.png` }, requested);
      n++;
      if (name === 'home' && !mob) {
        await p.getByRole('button', { name: 'footer-dropdown' }).click().catch(() => {});
        await wait(p, 600);
        await screenshotWithMetadata(p, { path: `${RAW}/${prefix}-overflow.png` }, requested);
        n++;
      }
    } catch (e) { log('  FAILED', e.message.split('\n')[0]); }
    await ctx.close();
  }
}
log('done', n);
await b.close();
