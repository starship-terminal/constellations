// SoundCloud public capture. Desktop 1440x900 at 1x, phone 390x844 at 2x.
// Hides the OneTrust banner in CSS. Never clicks I accept, Reject all, Google,
// Facebook, or Apple. Never types a password or submits a form.
//
//   PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs node shoot.mjs [names]
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { screenshotWithMetadata } from '../screenshot.mjs';

const pw = await import(process.env.PLAYWRIGHT || 'playwright');
const { chromium } = pw.default ?? pw;

const PKG = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..', '..');
const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', 'soundcloud', 'raw-shots');
fs.mkdirSync(RAW, { recursive: true });

const UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36';
const UA_MOBILE = 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 Mobile/15E148 Safari/604.1';

const log = (...a) => console.log(...a);
const wait = (p, ms) => p.waitForTimeout(ms);
const only = (process.argv[2] || '').split(',').filter(Boolean);

async function hideConsent(p) {
  await p.addStyleTag({ content: `
    #onetrust-consent-sdk, #onetrust-banner-sdk, #onetrust-pc-sdk, .onetrust-pc-dark-filter { display: none !important; }
  ` }).catch(() => {});
}

async function settle(p, ms = 2500) {
  await wait(p, ms);
  await hideConsent(p);
  await wait(p, 400);
}

class Shooter {
  constructor(p, prefix, vw, vh, dpr) {
    this.p = p; this.prefix = prefix; this.vw = vw; this.vh = vh; this.dpr = dpr;
    this.requested = { viewport: { width: vw, height: vh }, deviceScaleFactor: dpr };
    this.count = 0;
  }
  async view(name) {
    const file = `${RAW}/${this.prefix}-${name}.png`;
    await screenshotWithMetadata(this.p, { path: file }, this.requested);
    this.count++;
    log('  shot', this.prefix + '-' + name);
  }
  async full(name = 'full') {
    const p = this.p;
    const H = await p.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body ? document.body.scrollHeight : 0));
    const chunk = Math.floor(8000 / this.dpr);
    const maxH = Math.min(H, 4 * chunk);
    if (H > maxH) log(`  ! ${name}: page is ${H}px, capturing first ${maxH}px`);
    const parts = [];
    for (let y = 0, i = 0; y < maxH; y += chunk, i++) {
      const h = Math.min(chunk, maxH - y);
      await p.evaluate((yy) => scrollTo(0, yy), y);
      await wait(p, 350);
      const file = `${RAW}/${this.prefix}-${name}.part${i}.png`;
      await screenshotWithMetadata(p, { path: file }, this.requested);
      parts.push({ file, y, h });
    }
    await p.evaluate(() => scrollTo(0, 0));
    const stitch = `${RAW}/${this.prefix}-${name}.png`;
    const py = `
from PIL import Image
import json, sys
parts = json.loads(sys.argv[1])
imgs = [Image.open(p["file"]).convert("RGB") for p in parts]
w = imgs[0].width
h = sum(im.height for im in imgs)
out = Image.new("RGB", (w, h))
y = 0
for im in imgs:
    out.paste(im, (0, y)); y += im.height
out.save(sys.argv[2], "PNG")
print(w, h)
`;
    const { execFileSync } = await import('node:child_process');
    execFileSync(process.env.PYTHON || 'python3', ['-c', py, JSON.stringify(parts), stitch], { stdio: 'inherit' });
    this.count++;
    log('  shot', this.prefix + '-' + name, 'H=' + H);
  }
}

async function clickRole(p, role, name) {
  const loc = p.getByRole(role, { name });
  if (await loc.count()) {
    await loc.first().click({ timeout: 4000 });
    return true;
  }
  return false;
}

const shots = [];

function add(name, mobile, url, run) {
  shots.push({ name: (mobile ? 'mobile-' : '') + name, mobile, url, run });
}

const desktopPages = [
  ['home', 'https://soundcloud.com/'],
  ['discover', 'https://soundcloud.com/discover'],
  ['search-empty', 'https://soundcloud.com/search'],
  ['search-techno', 'https://soundcloud.com/search?q=techno'],
  ['search-sounds', 'https://soundcloud.com/search/sounds?q=techno'],
  ['search-people', 'https://soundcloud.com/search/people?q=techno'],
  ['search-albums', 'https://soundcloud.com/search/albums?q=techno'],
  ['search-sets', 'https://soundcloud.com/search/sets?q=techno'],
  ['profile', 'https://soundcloud.com/dcthedon'],
  ['track', 'https://soundcloud.com/akamersad/vay'],
  ['upload', 'https://soundcloud.com/upload'],
  ['charts', 'https://soundcloud.com/charts/top'],
  ['download', 'https://soundcloud.com/download'],
  ['terms', 'https://soundcloud.com/terms-of-use'],
  ['privacy', 'https://soundcloud.com/pages/privacy'],
  ['cookies', 'https://soundcloud.com/pages/cookies'],
  ['imprint', 'https://soundcloud.com/imprint'],
  ['copyright', 'https://soundcloud.com/pages/copyright'],
  ['guidelines', 'https://soundcloud.com/community-guidelines'],
  ['transparency', 'https://soundcloud.com/transparency-reports'],
  ['company', 'https://soundcloud.com/company/home/'],
  ['newsroom', 'https://soundcloud.com/company/newsroom/'],
  ['careers', 'https://soundcloud.com/company/careers/'],
  ['plans', 'https://soundcloud.com/company/plans/'],
  ['contact', 'https://soundcloud.com/company/contact-us/'],
  ['topics', 'https://soundcloud.com/topic/'],
  ['getheard', 'https://soundcloud.com/getstarted/getheard/'],
  ['getpaid', 'https://soundcloud.com/getstarted/getpaid/'],
  ['getstarted', 'https://soundcloud.com/getstarted/home/'],
  ['checkout-go', 'https://checkout.soundcloud.com/go'],
  ['checkout-artist', 'https://checkout.soundcloud.com/artist'],
  ['developers', 'https://developers.soundcloud.com/'],
  ['help', 'https://help.soundcloud.com/hc/en-us'],
  ['wall-feed', 'https://soundcloud.com/feed'],
  ['wall-library', 'https://soundcloud.com/you/library'],
];

for (const [name, url] of desktopPages) {
  add(name, false, url, async (p, S) => {
    await S.view('default');
    if (['home', 'discover', 'company', 'newsroom', 'plans', 'getheard', 'help', 'charts', 'profile'].includes(name)) {
      await S.full('full');
    }
  });
  add(name, true, url, async (p, S) => { await S.view('default'); });
}

add('home-banner-closed', false, 'https://soundcloud.com/', async (p, S) => {
  const close = p.getByRole('button', { name: /^Close$/ });
  if (await close.count()) { await close.first().click(); await wait(p, 600); }
  await S.view('default');
});

add('discover-menu', false, 'https://soundcloud.com/discover', async (p, S) => {
  const ok = await clickRole(p, 'button', /Settings and more/i);
  if (!ok) throw new Error('no settings button');
  await wait(p, 700);
  await S.view('open');
  await p.keyboard.press('Escape');
});

add('discover-shortcuts', false, 'https://soundcloud.com/discover', async (p, S) => {
  await clickRole(p, 'button', /Settings and more/i);
  await wait(p, 500);
  const kb = p.getByRole('link', { name: /Keyboard shortcuts/i });
  if (!(await kb.count())) throw new Error('no shortcuts link');
  await kb.click();
  await wait(p, 800);
  await S.view('open');
  await p.keyboard.press('Escape');
});

add('discover-signin-wall', false, 'https://soundcloud.com/discover', async (p, S) => {
  const btn = p.locator('button.loginButton, button').filter({ hasText: /^Sign in$/ }).first();
  await btn.click();
  await wait(p, 2500);
  await S.view('open');
  await p.keyboard.press('Escape');
});

add('search-focused', false, 'https://soundcloud.com/discover', async (p, S) => {
  const search = p.getByRole('button', { name: /^Search$/ }).first();
  await search.click();
  await wait(p, 600);
  const input = p.locator('input[type="search"], input[placeholder*="Search" i], input[name="q"]').first();
  if (await input.count()) await input.focus();
  await S.view('focused');
});

add('search-typed', false, 'https://soundcloud.com/search?q=techno', async (p, S) => {
  await S.view('results');
});

add('playbar', false, 'https://soundcloud.com/akamersad/vay', async (p, S) => {
  const play = p.getByRole('button', { name: /^Play$/ }).first();
  if (await play.count()) {
    await play.click();
    await wait(p, 1500);
    await p.evaluate(() => { for (const a of document.querySelectorAll('audio, video')) { try { a.pause(); } catch (e) {} } });
  }
  await S.view('paused');
});

add('share-menu', false, 'https://soundcloud.com/search?q=techno', async (p, S) => {
  const share = p.getByRole('button', { name: /^Share$/ }).first();
  if (!(await share.count())) throw new Error('no share');
  await share.click();
  await wait(p, 800);
  await S.view('open');
  await p.keyboard.press('Escape');
});

add('company-services', false, 'https://soundcloud.com/company/home/', async (p, S) => {
  const ok = await clickRole(p, 'button', /^Services$/);
  if (!ok) throw new Error('no services');
  await wait(p, 600);
  await S.view('open');
});

add('help-search-focused', false, 'https://help.soundcloud.com/hc/en-us', async (p, S) => {
  const input = p.locator('input[type="search"], input[name="query"]').first();
  if (await input.count()) { await input.click(); await wait(p, 400); }
  await S.view('focused');
});

add('mobile-menu', true, 'https://soundcloud.com/discover', async (p, S) => {
  const more = p.getByRole('button', { name: /Settings and more|Menu|More/i });
  if (await more.count()) {
    await more.first().click();
    await wait(p, 700);
  }
  await S.view('open');
});

const browser = await chromium.launch({ headless: true });
let total = 0;
const failures = [];
for (const shot of shots) {
  if (only.length && !only.includes(shot.name)) continue;
  const vw = shot.mobile ? 390 : 1440;
  const vh = shot.mobile ? 844 : 900;
  const dpr = shot.mobile ? 2 : 1;
  const ctx = await browser.newContext({
    viewport: { width: vw, height: vh },
    deviceScaleFactor: dpr,
    userAgent: shot.mobile ? UA_MOBILE : UA,
    isMobile: shot.mobile,
    hasTouch: shot.mobile,
    locale: 'en-US',
  });
  const p = await ctx.newPage();
  log(shot.name, shot.url);
  const S = new Shooter(p, shot.name + '-dark', vw, vh, dpr);
  try {
    const resp = await p.goto(shot.url, { waitUntil: 'domcontentloaded', timeout: 50000 });
    log('  status', resp && resp.status(), 'final', p.url().split('?')[0]);
    await settle(p, 2800);
    await shot.run(p, S);
  } catch (e) {
    const msg = String(e.message || e).split('\n')[0];
    log('  FAILED', msg);
    failures.push(shot.name + ': ' + msg);
  }
  total += S.count;
  await ctx.close();
}
log('done', total, 'shots, failures', failures.length);
for (const f of failures) log('  fail', f);
fs.writeFileSync(path.join(RAW, 'failures.json'), JSON.stringify(failures, null, 2));
await browser.close();
process.exit(failures.length && total === 0 ? 1 : 0);
