// Captures Mapbox public marketing pages into RAW (full-colour PNGs).
//
//   RAW=~/.design-systems/mapbox/raw-shots PLAYWRIGHT=... node public.mjs [id,id,...]
//
// Desktop 1440x900 at 1x, phone 390x844 at 2x. Nothing is submitted. The
// OneTrust banner is hidden, never accepted. Auth URLs are recorded and the
// branch stops.
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { hideConsent, isAuthUrl, chromium, UA, UA_MOBILE, BASE } from './lib.mjs';

const pages = JSON.parse(fs.readFileSync(new URL('./pages.json', import.meta.url), 'utf8'));
const PKG = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..', '..');
const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', 'mapbox', 'raw-shots');
fs.mkdirSync(RAW, { recursive: true });
const want = new Set((process.argv[2] || '').split(',').filter(Boolean));
const onlyMobile = process.env.ONLY === 'mobile';
const onlyDesktop = process.env.ONLY === 'desktop';
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const wait = (p, ms) => p.waitForTimeout(ms);

async function lazyScroll(p) {
  const h = await p.evaluate(() => document.documentElement.scrollHeight);
  const cap = Math.min(h, 4800);
  for (let y = 0; y < cap; y += 700) {
    await p.evaluate((y) => scrollTo(0, y), y);
    await wait(p, 120);
  }
  await p.evaluate(() => scrollTo(0, 0));
  await wait(p, 400);
}

class Shooter {
  constructor(p, prefix, vw, vh, dpr, source) {
    this.p = p; this.prefix = prefix; this.vw = vw; this.dpr = dpr; this.source = source;
    this.requested = { viewport: { width: vw, height: vh }, deviceScaleFactor: dpr, sanitizedSourceUrl: source };
    this.count = 0;
  }
  async view(name) {
    await screenshotWithMetadata(this.p, { path: `${RAW}/${this.prefix}-${name}.png` }, this.requested);
    this.count++;
    log('  shot', this.prefix, name);
  }
  async full(name = 'full') {
    const p = this.p;
    await lazyScroll(p);
    const H = await p.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body.scrollHeight));
    const chunk = Math.floor(8000 / this.dpr);
    const f = `${RAW}/${this.prefix}-${name}`;
    for (const old of fs.readdirSync(RAW).filter((n) => n.startsWith(`${path.basename(f)}.part`))) fs.unlinkSync(`${RAW}/${old}`);
    const MAXH = 4 * chunk;
    const hCap = Math.min(H, MAXH);
    if (H > MAXH) log(`  ! ${this.prefix}: page is ${H}px, capturing first ${hCap}px`);
    if (hCap <= chunk) await screenshotWithMetadata(p, { path: f + '.png', fullPage: true }, this.requested);
    else for (let i = 0, y = 0; y < hCap; i++, y += chunk) {
      await screenshotWithMetadata(p, { path: `${f}.part${i}.png`, fullPage: true, clip: { x: 0, y, width: this.vw, height: Math.min(chunk, hCap - y) } }, this.requested);
    }
    this.count++;
    log('  shot', this.prefix, name, 'H=' + H);
    await p.evaluate(() => scrollTo(0, 0));
  }
}

async function openPage(p, urlPath) {
  const resp = await p.goto(BASE + urlPath, { waitUntil: 'domcontentloaded', timeout: 60000 });
  await wait(p, 2200);
  await hideConsent(p);
  const url = p.url();
  const title = await p.title();
  const status = resp ? resp.status() : 0;
  return { url, title, status, auth: isAuthUrl(url) };
}

const browser = await chromium.launch({ headless: true });
const logRows = [];

async function runWidth(mobile) {
  if (mobile && onlyDesktop) return;
  if (!mobile && onlyMobile) return;
  const vw = mobile ? 390 : 1440;
  const vh = mobile ? 844 : 900;
  const dpr = mobile ? 2 : 1;
  const prefix0 = mobile ? 'mobile-' : '';
  for (const spec of pages) {
    const name = prefix0 + spec.id;
    if (want.size && !want.has(spec.id) && !want.has(name)) continue;
    const ctx = await browser.newContext({
      viewport: { width: vw, height: vh },
      deviceScaleFactor: dpr,
      userAgent: mobile ? UA_MOBILE : UA,
      isMobile: mobile,
      hasTouch: mobile,
      locale: 'en-US',
    });
    await ctx.addInitScript(() => { Object.defineProperty(navigator, 'webdriver', { get: () => undefined }); });
    const p = await ctx.newPage();
    const source = BASE + spec.path;
    const S = new Shooter(p, `${name}-light`, vw, vh, dpr, source);
    log(name);
    try {
      const info = await openPage(p, spec.path);
      logRows.push({ name, ...info, vw, vh, dpr });
      if (info.auth) {
        log('  AUTH WALL', info.url);
        await S.view('auth-wall');
      } else if (info.status >= 400 || /just a moment|verify you are human|unusual activity/i.test(info.title)) {
        log('  BLOCKED', info.status, info.title);
        await S.view('blocked');
      } else {
        await S.view('default');
        if (spec.id === 'home' || spec.id === 'pricing' || spec.id === 'contact' || spec.id === 'maps') await S.full();
      }
    } catch (e) {
      log('  PAGE FAILED', name, String(e.message).split('\n')[0]);
      logRows.push({ name, error: String(e.message).split('\n')[0] });
    }
    await ctx.close();
  }
}

await runWidth(false);
await runWidth(true);
fs.writeFileSync(path.join(RAW, 'page-log.json'), JSON.stringify(logRows, null, 2));
log('done', logRows.length);
await browser.close();
