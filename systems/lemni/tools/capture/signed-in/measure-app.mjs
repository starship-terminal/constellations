// Measures Lemni's signed-in free-product controls. Merges into
// systems/lemni/raw/components-computed.json. Never clicks Upgrade, Invite,
// Enable Agent, Add, Create, or a payment control.
//
//   PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs node measure-app.mjs
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { closePromo, clearChallenge, patch, chromium, styleOf, crop, centre, mark, RAW, UA } from '../public/lib.mjs';

const AUTH = path.join(os.homedir(), '.design-systems', 'lemni', 'access-token');
const PROFILE = process.env.LEMNI_PROFILE || path.join(os.homedir(), '.design-systems', 'lemni', 'chrome-profile');
const [workspace, token] = fs.readFileSync(AUTH, 'utf8').trim().split('\n');
const SPACE = `https://lemni.com/s/${workspace}`;
const OUT = path.join(RAW, 'components-computed.json');
const out = fs.existsSync(OUT) ? JSON.parse(fs.readFileSync(OUT, 'utf8')) : { _meta: {}, components: {} };
const TODAY = new Date().toLocaleDateString('en-CA');
// _meta.read keeps the earlier date until this run reads a state, so a rerun that
// fails throughout never redates old readings; _meta.lastAttempt is this run's date.
// Each component and state also carries its own `read` date.
out._meta = { ...out._meta, read: (out._meta && out._meta.read) || TODAY, lastAttempt: TODAY, product: 'Lemni', route: 'public-web+signed-in-free' };
out.components ??= {};
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const save = () => fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');
const B4 = ['default', 'hover', 'focus-visible', 'pressed'];

const context = await chromium.launchPersistentContext(PROFILE, {
  headless: true,
  viewport: { width: 1440, height: 900 },
  deviceScaleFactor: 2,
  userAgent: UA,
  locale: 'en-US',
  // automation is not hidden: the AutomationControlled feature stays as Chromium sets it (bot check: recorded as a boundary, not bypassed)
});
await patch(context);
await context.addInitScript(({ workspace, token }) => {
  try {
    localStorage.setItem('workspace', workspace);
    localStorage.setItem('lemni.accessToken', token);
  } catch { /* */ }
}, { workspace, token });
const page = context.pages()[0] || await context.newPage();
page.setDefaultTimeout(8000);
const cdp = await context.newCDPSession(page);
await cdp.send('DOM.enable');
await cdp.send('CSS.enable');

let current = 'inbox';

async function go(key, url, waitMs = 2500) {
  current = key;
  log('open', key);
  await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 90000 });
  if (!(await clearChallenge(page))) throw new Error('blocked ' + key);
  await page.waitForTimeout(waitMs);
  await closePromo(page);
}

async function reset() {
  await page.evaluate(() => document.activeElement && document.activeElement.blur && document.activeElement.blur()).catch(() => {});
  await page.mouse.move(1430, 2);
  await page.waitForTimeout(150);
}

async function kbFocus(loc) {
  await loc.evaluate((el) => el.focus());
  await page.keyboard.press('Shift+Tab');
  await page.keyboard.press('Tab');
  const ok = await loc.evaluate((el) => document.activeElement === el || el.contains(document.activeElement));
  await page.waitForTimeout(250);
  return ok ? 'keyboard focus' : 'focus failed';
}

async function forcePseudo(loc, classes) {
  await page.evaluate(() => document.querySelectorAll('[data-m-force]').forEach((n) => n.removeAttribute('data-m-force')));
  await loc.evaluate((el) => el.setAttribute('data-m-force', '1'));
  const { root } = await cdp.send('DOM.getDocument', { depth: 0 });
  const { nodeId } = await cdp.send('DOM.querySelector', { nodeId: root.nodeId, selector: '[data-m-force]' });
  if (!nodeId) return async () => {};
  await cdp.send('CSS.forcePseudoState', { nodeId, forcedPseudoClasses: classes });
  await page.waitForTimeout(250);
  return async () => { await cdp.send('CSS.forcePseudoState', { nodeId, forcedPseudoClasses: [] }).catch(() => {}); };
}

function comp(key, meta) {
  // Each component carries the date it was read, so a partial run that leaves
  // other components untouched does not pass their readings off as today's.
  out.components[key] = { page: current, url: meta.url, read: TODAY, states: {}, ...meta };
  return out.components[key];
}

async function measure(key, state, loc, opts = {}) {
  const c = out.components[key];
  try {
    const s = await styleOf(loc);
    let file;
    if (opts.crop !== false) {
      try { file = await crop(page, loc, `${key}-${state}`, opts.pad ?? 10); }
      catch (e) { s.cropError = String(e.message || e).slice(0, 140); }
    }
    c.states[state] = { ...s, crop: file, via: opts.via, read: TODAY };
    out._meta.read = TODAY; // a reading succeeded in this run
    log('  ', key, state, s.rect.w + 'x' + s.rect.h);
  } catch (e) {
    c.states[state] = { error: String(e.message || e).slice(0, 200) };
    log('  !', key, state, String(e.message).slice(0, 140));
  }
}

async function S(key, getLoc, list, meta, opts = {}) {
  comp(key, meta);
  const loc0 = await getLoc();
  if (!loc0) { out.components[key].missing = true; log('  ! missing', key); return; }
  for (const st of list) {
    let undo, via = 'at rest';
    try {
      await reset();
      const loc = (await getLoc()) || loc0;
      if (!opts.noScroll) await centre(loc);
      if (st === 'hover') {
        await loc.hover({ timeout: 4000 }).catch(() => loc.hover({ force: true, timeout: 4000 }));
        await page.waitForTimeout(300);
        via = 'mouse hover';
      } else if (st === 'focus-visible') {
        via = await kbFocus(loc);
      } else if (st === 'pressed') {
        undo = await forcePseudo(loc, ['active', 'hover']);
        via = 'CDP forcePseudoState :active:hover; not clicked through';
      }
      const loc2 = (await getLoc()) || loc;
      await measure(key, st, loc2, { ...opts, via });
    } catch (e) {
      out.components[key].states[st] = { error: String(e.message || e).slice(0, 200) };
      log('  !', key, st, String(e.message).slice(0, 140));
    }
    if (undo) await undo().catch(() => {});
  }
  await reset();
}

const byText = (text, tags) => () => mark(page, { text, tags, exact: true });

await go('inbox', `${SPACE}/inbox`);
const inboxUrl = 'https://lemni.com/s/XXXXX/inbox';
await S('app-nav-inbox', byText('Inbox', 'div,a,button,span'), ['default', 'hover'], {
  group: 'App shell', title: 'Inbox nav row', url: inboxUrl,
  desc: 'Selected row in the workplace sidebar.', selector: 'text Inbox',
}, { noScroll: true });
await S('app-upgrade', byText('Upgrade', 'div,button'), B4, {
  group: 'App shell', title: 'Sidebar Upgrade', url: inboxUrl,
  desc: 'Free-trial upgrade pill in the sidebar. Measured, never followed.', selector: 'Upgrade',
}, { noScroll: true });
await S('app-empty', byText('No threads todo', 'div,p,span'), ['default'], {
  group: 'Inbox', title: 'Empty inbox', url: inboxUrl,
  desc: 'Empty state copy in the thread list.', selector: 'No threads todo',
});
await S('app-toast', async () => mark(page, { text: 'Reconnecting', tags: 'div,span' }), ['default'], {
  group: 'Inbox', title: 'Reconnecting toast', url: inboxUrl,
  desc: 'Black pill toast the headless client shows while the socket retries.', selector: 'Reconnecting',
});

await go('settings', `${SPACE}/inbox?workspaceSettings=members`, 2800);
const setUrl = 'https://lemni.com/s/XXXXX/inbox?workspaceSettings=members';
await S('app-dialog', async () => mark(page, { text: 'My Workspace workplace', tags: 'div,section,h2,h1' }), ['default'], {
  group: 'Workplace', title: 'Workplace settings dialog', url: setUrl,
  desc: 'Members dialog over a dimmed inbox.', selector: 'dialog heading',
});
await S('app-invite-field', async () => page.locator('input[placeholder="name@myworkspace.com"]').first(), ['default', 'focus-visible'], {
  group: 'Workplace', title: 'Invite email field', url: setUrl,
  desc: 'Invite field. Typed nothing; Invite was not pressed.', selector: 'input[placeholder=name@myworkspace.com]',
});
await S('app-member-row', async () => mark(page, { text: 'Owner', tags: 'div,tr,li' }), ['default'], {
  group: 'Workplace', title: 'Member row', url: setUrl,
  desc: 'Owner row in the members list.', selector: 'Owner',
});
await S('app-role-badge', byText('Owner', 'div,span'), ['default'], {
  group: 'Workplace', title: 'Owner badge', url: setUrl,
  desc: 'Role label on the member row.', selector: 'Owner',
});

await go('profile', `${SPACE}/inbox?settings=profile`, 2800);
const profUrl = 'https://lemni.com/s/XXXXX/inbox?settings=profile';
await S('app-profile-dialog', async () => mark(page, { text: 'Account', tags: 'div,h1,h2,section' }), ['default'], {
  group: 'Account', title: 'Account dialog', url: profUrl,
  desc: 'Profile dialog with name and email fields.', selector: 'Account',
});
await S('app-name-field', async () => page.locator('input[value="Kai"]').first(), ['default'], {
  group: 'Account', title: 'First name field', url: profUrl,
  desc: 'First name field at rest. Not edited.', selector: 'input[value=Kai]',
});

await go('agents', `${SPACE}/agents`, 2800);
const agUrl = 'https://lemni.com/s/XXXXX/agents';
await S('app-disabled-badge', byText('Disabled', 'div,span'), ['default'], {
  group: 'Agents', title: 'Disabled badge', url: agUrl,
  desc: 'Status on a stock agent that is off.', selector: 'Disabled',
});
await S('app-enable', byText('Enable Agent', 'div,button'), B4, {
  group: 'Agents', title: 'Enable Agent', url: agUrl,
  desc: 'Primary control in the interact column. Measured, never pressed.', selector: 'Enable Agent',
});

await go('knowledge', `${SPACE}/knowledge`, 2500);
const knUrl = 'https://lemni.com/s/XXXXX/knowledge';
await S('app-add-webpage', byText('Add Webpage', 'div,button'), ['default', 'hover'], {
  group: 'Knowledge', title: 'Add Webpage', url: knUrl,
  desc: 'Empty-dataset control. Not pressed.', selector: 'Add Webpage',
});

await go('subscribe', 'https://lemni.com/welcome/subscribe', 2500);
await S('app-plan-upgrade', byText('Upgrade', 'div,button'), B4, {
  group: 'Plan', title: 'Onboarding Upgrade', url: 'https://lemni.com/welcome/subscribe',
  desc: 'Paid plan CTA. Measured, never pressed.', selector: 'Upgrade',
});

save();
await context.close();
log('wrote', Object.keys(out.components).filter((k) => k.startsWith('app-')).length, 'app components');
