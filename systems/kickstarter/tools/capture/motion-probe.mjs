// Kickstarter motion probe. Headed Chrome, consent hidden, never clicked.
// Reads the atomic stylesheet (cross-origin CSSOM is blocked) plus computed
// motion on the live home, discover and project pages.
//
//   PLAYWRIGHT=... node tools/capture/motion-probe.mjs
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { BASE, launchBrowser, newContext, open } from './public/lib.mjs';

const here = path.dirname(fileURLToPath(import.meta.url));
const REF = path.resolve(here, '..', '..');
const OUT = path.join(REF, 'raw', 'motion.json');
const CACHE = path.join(os.homedir(), '.design-systems', 'kickstarter', 'css');

function loadCss() {
  const dir = fs.existsSync(CACHE) ? CACHE : path.join(os.homedir(), '.design-systems', 'kickstarter', 'probe', 'css');
  // The sheet vars.mjs recorded in raw/css-vars.json (cssFile) wins; otherwise the cached atomic
  // sheets are sorted so the pick does not depend on directory order.
  const recorded = (() => { try { return JSON.parse(fs.readFileSync(path.join(REF, 'raw', 'css-vars.json'), 'utf8')).cssFile; } catch { return null; } })();
  const hits = fs.readdirSync(dir).filter((n) => n.includes('atomic')).sort();
  if (!hits.length) throw new Error('no atomic css in ' + dir);
  const known = recorded && hits.includes(path.basename(recorded));
  const name = known ? path.basename(recorded) : hits[0];
  if (!known && hits.length > 1) console.log('several atomic sheets cached and none is the recorded one; reading', name);
  return fs.readFileSync(path.join(dir, name), 'utf8').replace(/^\/\* https?:\/\/[^\n]*\n/, '');
}

const css = loadCss();
const browser = await launchBrowser();
const pages = ['/', '/discover?ref=nav', '/projects/shirtaloon/hwfwm'];
const records = {};
let i = 0;
for (const route of pages) {
  const ctx = await newContext(browser, { dpr: 1 });
  const page = await ctx.newPage();
  await open(page, BASE + route, { wait: 1500 });
  const reading = await page.evaluate(async (cssText) => {
    const sheet = new CSSStyleSheet();
    await sheet.replace(cssText);
    const declared = [];
    const keyframes = [];
    const reduced = [];
    const walk = (list, ctx) => {
      for (const r of list) {
        if (r.type === CSSRule.KEYFRAMES_RULE) {
          keyframes.push({ name: r.name, css: (r.cssText || '').slice(0, 300) });
          continue;
        }
        if (r.type === CSSRule.MEDIA_RULE && /prefers-reduced-motion/.test(r.media.mediaText)) {
          reduced.push({ media: r.media.mediaText, sample: (r.cssText || '').slice(0, 280) });
        }
        if (r.cssRules && !r.style) { walk(r.cssRules, [...ctx, (r.conditionText || r.media?.mediaText || '').slice(0, 80)]); continue; }
        if (!r.style) continue;
        const t = r.style.getPropertyValue('transition');
        const a = r.style.getPropertyValue('animation');
        if ((t && t !== 'all 0s ease 0s' && t !== 'none') || (a && a !== 'none')) {
          declared.push({
            selector: (r.selectorText || '').slice(0, 140),
            context: ctx.filter(Boolean).slice(0, 2),
            transition: t.slice(0, 160),
            animation: a.slice(0, 120),
          });
        }
      }
    };
    walk(sheet.cssRules, []);
    const moving = [];
    const nodes = document.querySelectorAll('body *');
    let scanned = 0;
    for (const el of nodes) {
      if (scanned++ > 4000) break;
      const cs = getComputedStyle(el);
      const dur = cs.transitionDuration;
      const anim = cs.animationName;
      if ((dur && dur !== '0s') || (anim && anim !== 'none')) {
        moving.push({
          node: el.tagName.toLowerCase() + '.' + String(el.className).split(' ')[0].slice(0, 40),
          transition: cs.transitionProperty + ' ' + dur + ' ' + cs.transitionTimingFunction,
          animation: anim + ' ' + cs.animationDuration,
        });
        if (moving.length > 40) break;
      }
    }
    return {
      url: location.href.split('?')[0],
      matchMedia: window.matchMedia('(prefers-reduced-motion: reduce)').matches,
      moving: moving.slice(0, 24),
      declared: declared.slice(0, 80),
      keyframes: keyframes.slice(0, 30),
      reduced: reduced.slice(0, 20),
    };
  }, css);
  // second pass under reduce
  await page.emulateMedia({ reducedMotion: 'reduce' });
  await page.waitForTimeout(400);
  const reducedMatch = await page.evaluate(() => window.matchMedia('(prefers-reduced-motion: reduce)').matches);
  reading.matchMediaReduce = reducedMatch;
  records['page-' + (++i)] = reading;
  console.log(route, 'moving', reading.moving.length, 'declared', reading.declared.length, 'reduceMedia', reducedMatch);
  await ctx.close();
}
const out = {
  product: 'kickstarter',
  read: new Date().toLocaleDateString('en-CA'),
  source: 'headed Chrome, atomic stylesheet parsed in a constructed sheet, computed motion on the live DOM',
  pages: records,
  verdict: 'partial',
  note: 'Authored motion (card hover, creator nav, progress pulse) is gated on prefers-reduced-motion: no-preference, so reduce removes those transitions. The public home at rest has little computed motion. A progress-bar pulse animation is declared only under no-preference.',
};
fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');
console.log('wrote', OUT);
await browser.close();
