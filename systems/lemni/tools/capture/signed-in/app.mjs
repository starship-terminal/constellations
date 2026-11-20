// Live capture of Lemni's free signed-in product.
//
//   PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs node app.mjs [page,page,...]
//
// Auth: ~/.design-systems/lemni/access-token (workspace id, then JWT). Persistent
// Chromium profile: ~/.design-systems/lemni/chrome-profile. Never clicks Upgrade,
// Invite, Google, or a payment control. Desktop 1440x900 at 1x, phone 390x844 at 2x.
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { closePromo, clearChallenge, patch, chromium, UA, UA_MOBILE } from '../public/lib.mjs';

const AUTH = path.join(os.homedir(), '.design-systems', 'lemni', 'access-token');
const PROFILE = process.env.LEMNI_PROFILE || path.join(os.homedir(), '.design-systems', 'lemni', 'chrome-profile');
const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', 'lemni', 'raw-shots');
fs.mkdirSync(RAW, { recursive: true });
fs.mkdirSync(PROFILE, { recursive: true });

const [workspace, token] = fs.readFileSync(AUTH, 'utf8').trim().split('\n');
if (!workspace || !token) throw new Error('access-token file missing workspace or token');
const SPACE = `/s/${workspace}`;
const ORIGIN = 'https://lemni.com';
const pageArg = (process.argv[2] || '').split(',').filter(Boolean);
const log = (...a) => console.log(...a);
const wait = (p, ms) => p.waitForTimeout(ms);
// The recorded form of a page URL: the workspace id masked, and the query and fragment dropped
// (a query can carry a search, an invite or a token).
const sanitize = (url) => url.replace(workspace, 'XXXXX').split('#')[0].split('?')[0];

async function injectAuth(context) {
  await context.addInitScript(({ workspace, token }) => {
    try {
      localStorage.setItem('workspace', workspace);
      localStorage.setItem('lemni.accessToken', token);
    } catch { /* quota / private mode */ }
  }, { workspace, token });
}

async function settled(p) {
  await wait(p, 1200);
  await p.waitForFunction(() => {
    const t = document.body && document.body.innerText || '';
    return t.length > 40 && !/reconnecting/i.test(t);
  }, { timeout: 12000 }).catch(() => {});
  await wait(p, 400);
}

class Shooter {
  constructor(p, prefix, vw, vh, dpr) {
    this.p = p; this.prefix = prefix; this.vw = vw; this.dpr = dpr;
    this.requested = { viewport: { width: vw, height: vh }, deviceScaleFactor: dpr };
    this.count = 0;
  }
  async view(name, url) {
    await closePromo(this.p);
    await screenshotWithMetadata(this.p, { path: `${RAW}/${this.prefix}-${name}.png` }, {
      ...this.requested,
      sanitizedSourceUrl: url ? sanitize(url) : null,
    });
    this.count++;
    log('  shot', name);
  }
  async full(name, url) {
    await closePromo(this.p);
    await this.p.evaluate(() => scrollTo(0, 0));
    await wait(this.p, 200);
    await screenshotWithMetadata(this.p, { path: `${RAW}/${this.prefix}-${name}.png`, fullPage: true }, {
      ...this.requested,
      sanitizedSourceUrl: url ? sanitize(url) : null,
    });
    this.count++;
    log('  shot', name, 'full');
  }
}

const desktop = {
  inbox: { path: `${SPACE}/inbox`, run: async (p, S, url) => {
    await S.view('default', url);
    if ((p.viewportSize()?.width || 1440) <= 400) {
      if (await openMobileNav(p)) await S.view('nav-open', url);
    }
  } },
  assigned: { path: `${SPACE}/assigned`, run: async (p, S, url) => { await S.view('default', url); } },
  agents: { path: `${SPACE}/agents`, run: async (p, S, url) => { await S.view('default', url); await S.full('full', url); } },
  knowledge: { path: `${SPACE}/knowledge`, run: async (p, S, url) => { await S.view('default', url); } },
  behavior: { path: `${SPACE}/behavior`, run: async (p, S, url) => { await S.view('default', url); } },
  actions: { path: `${SPACE}/actions`, run: async (p, S, url) => { await S.view('default', url); await S.full('full', url); } },
  'workspace-settings': { path: `${SPACE}/inbox?workspaceSettings=members`, run: async (p, S, url) => { await S.view('default', url); } },
  profile: { path: `${SPACE}/inbox?settings=profile`, run: async (p, S, url) => { await S.view('default', url); } },
  subscribe: { path: '/welcome/subscribe', run: async (p, S, url) => { await S.view('default', url); } },
  tutorial: { path: '/welcome/tutorial', run: async (p, S, url) => { await S.view('default', url); } },
};

async function openMobileNav(p) {
  const loc = p.locator('button, [role="button"], div').filter({ has: p.locator('svg') });
  const n = await loc.count().catch(() => 0);
  for (let i = n - 1; i >= 0 && i >= n - 8; i--) {
    const box = await loc.nth(i).boundingBox().catch(() => null);
    if (!box) continue;
    if (box.y > 700 && box.width < 80 && box.height < 80) {
      await loc.nth(i).click({ timeout: 3000 }).catch(() => {});
      await wait(p, 700);
      return true;
    }
  }
  // No blind click at fixed coordinates: if no menu control was found, say so and skip the state.
  log('  no mobile menu control found');
  return false;
}

const mobileKeys = ['inbox', 'agents', 'knowledge', 'actions', 'subscribe'];

async function runWidth({ mob }) {
  const vw = mob ? 390 : 1440, vh = mob ? 844 : 900, dpr = mob ? 2 : 1;
  const context = await chromium.launchPersistentContext(PROFILE, {
    headless: true,
    viewport: { width: vw, height: vh },
    deviceScaleFactor: dpr,
    userAgent: mob ? UA_MOBILE : UA,
    isMobile: mob,
    hasTouch: mob,
    locale: 'en-US',
    // automation is not hidden: the AutomationControlled feature stays as Chromium sets it (bot check: recorded as a boundary, not bypassed)
  });
  await patch(context);
  await injectAuth(context);
  const p = context.pages()[0] || await context.newPage();
  p.setDefaultTimeout(15000);
  let total = 0;
  const keys = mob ? mobileKeys : Object.keys(desktop);
  for (const k of keys) {
    const name = (mob ? 'mobile-app-' : 'app-') + k;
    if (pageArg.length && !pageArg.includes(name) && !pageArg.includes(k) && !pageArg.includes('app-' + k)) continue;
    const spec = desktop[k];
    const url = ORIGIN + spec.path;
    log(name, 'light');
    const S = new Shooter(p, `${name}-light`, vw, vh, dpr);
    try {
      await p.goto(url, { waitUntil: 'domcontentloaded', timeout: 90000 });
      if (!(await clearChallenge(p))) { log('  BLOCKED', sanitize(url)); continue; }
      await settled(p);
      const body = await p.evaluate(() => (document.body && document.body.innerText || '').slice(0, 400));
      if (/verify you are human|captcha|phone number|enter your card|payment method/i.test(body)
        && !/upgrade now|upgrade your free trial|pick a plan/i.test(body)) {
        log('  STOP challenge/payment', sanitize(url), JSON.stringify(body.slice(0, 180)));
        await context.close();
        return { total, stop: true };
      }
      await spec.run(p, S, url);
    } catch (e) {
      log('  PAGE FAILED', name, String(e.message).split('\n')[0]);
    }
    total += S.count;
  }
  await context.close();
  return { total, stop: false };
}

let shots = 0;
const desk = await runWidth({ mob: false });
shots += desk.total;
if (!desk.stop) {
  const mob = await runWidth({ mob: true });
  shots += mob.total;
}
log('done', shots, 'screenshots ->', RAW);
