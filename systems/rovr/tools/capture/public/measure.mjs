// Measures ROVR's public components. Nothing is typed into a password field,
// submitted, or sent to Google or Apple.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node measure.mjs
//
// Writes raw/components-computed.json and crops under components/crops/.
import fs from 'node:fs';
import path from 'node:path';
import { BASE, launch, open, styleOf, crop, RAW, CROPS } from './lib.mjs';

fs.mkdirSync(RAW, { recursive: true });
fs.mkdirSync(CROPS, { recursive: true });

const out = {
  product: 'ROVR',
  url: BASE,
  captured: new Date().toISOString().slice(0, 10),
  theme: 'dark',
  widths: [1440, 390],
  components: {},
};
const log = (...a) => console.log(...a);

const { browser, context } = await launch();
const page = await context.newPage();
const cdp = await context.newCDPSession(page);
await cdp.send('DOM.enable');
await cdp.send('CSS.enable');

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

async function record(key, state, loc, meta) {
  const target = loc.filter({ visible: true }).first();
  const entry = (out.components[key] ??= { ...meta, states: {} });
  if (!(await target.count())) {
    entry.states[state] = { missing: true };
    log('  missing', key, state);
    return;
  }
  try {
    const s = await styleOf(target);
    let file;
    try { file = await crop(page, target, `${key}-${state}`); } catch (e) { s.cropError = String(e.message).slice(0, 100); }
    entry.states[state] = { ...s, crop: file };
    log(' ', key, state, s.rect.w + 'x' + s.rect.h, s.backgroundColor, s.color, s.fontSize);
  } catch (e) {
    entry.states[state] = { error: String(e.message).slice(0, 160) };
    log('  !', key, state, String(e.message).slice(0, 80));
  }
}

async function states(key, loc, meta) {
  await record(key, 'default', loc, meta);
  const target = loc.filter({ visible: true }).first();
  if (!(await target.count())) return;
  const releaseH = await forcePseudo(target, ['hover']);
  await record(key, 'hover', target, meta);
  await releaseH();
  const releaseF = await forcePseudo(target, ['focus-visible']);
  await record(key, 'focus-visible', target, meta);
  await releaseF();
  const releaseP = await forcePseudo(target, ['active']);
  await record(key, 'pressed', target, meta);
  await releaseP();
}

async function go(url) {
  await open(page, BASE + url, { wait: 2200 });
  log('open', url, page.url());
}

// Resolve declared HSL channel tokens to painted colours on the live page.
await go('/');
const roles = await page.evaluate(() => {
  const root = getComputedStyle(document.documentElement);
  const names = ['--background', '--foreground', '--primary', '--primary-foreground', '--secondary', '--secondary-foreground', '--muted', '--muted-foreground', '--accent', '--accent-foreground', '--destructive', '--destructive-foreground', '--border', '--input', '--ring', '--card', '--card-foreground', '--popover', '--popover-foreground', '--radius'];
  const el = document.createElement('div');
  document.body.appendChild(el);
  const painted = {};
  for (const n of names) {
    const raw = root.getPropertyValue(n).trim();
    if (!raw) { painted[n] = { raw: null }; continue; }
    if (n === '--radius') { painted[n] = { raw }; continue; }
    el.style.backgroundColor = `hsl(${raw})`;
    painted[n] = { raw, painted: getComputedStyle(el).backgroundColor };
  }
  el.remove();
  const body = getComputedStyle(document.body);
  return {
    painted,
    body: { backgroundColor: body.backgroundColor, color: body.color, fontFamily: body.fontFamily, fontSize: body.fontSize },
    scheme: root.colorScheme,
  };
});
out.roles = roles;
fs.writeFileSync(path.join(RAW, 'components-computed.json'), JSON.stringify(out, null, 1) + '\n');

await states('nav-link', page.getByRole('link', { name: 'MOODS', exact: true }), { group: 'link', title: 'Header nav link' });
await states('menu-button', page.getByRole('button', { name: 'open drawer menu' }), { group: 'button', title: 'MENU pill' });
await states('play-button', page.getByRole('button', { name: 'Listen to music' }).first(), { group: 'icon button', title: 'Play' });
await states('quick-menu', page.getByRole('button', { name: 'Show quick menu' }), { group: 'icon button', title: 'Quick menu' });
await record('display-title', 'default', page.locator('h1').first(), { group: 'type', title: 'Show title' });
await record('curator-name', 'default', page.getByRole('link', { name: /Navarro|BY/ }).first(), { group: 'link', title: 'Curator name' });

await page.getByRole('button', { name: 'open drawer menu' }).click();
await page.waitForTimeout(600);
await record('drawer', 'open', page.getByRole('dialog').first(), { group: 'menu', title: 'Navigation drawer' });
await states('drawer-item', page.getByRole('button', { name: 'MY TRACKS' }), { group: 'menu', title: 'Drawer item' });
await record('search-field', 'default', page.getByPlaceholder('SEARCH'), { group: 'text field', title: 'Drawer search' });
await page.getByRole('button', { name: 'close drawer' }).click();
await page.waitForTimeout(300);

await page.getByRole('button', { name: 'Open Alexa modal' }).click();
await page.waitForTimeout(600);
await record('dialog', 'open', page.getByRole('dialog').last(), { group: 'dialog', title: 'Alexa dialog' });
await page.keyboard.press('Escape');
await page.waitForTimeout(300);

await record('footer-link', 'default', page.getByRole('link', { name: 'Privacy Policy' }).first(), { group: 'link', title: 'Footer link' });

await go('/curators');
await states('search-input', page.getByPlaceholder('Search by name'), { group: 'text field', title: 'Curator search' });
await record('curator-card', 'default', page.getByRole('link', { name: /DOOR KEY|ABUL/ }).first(), { group: 'card', title: 'Curator card' });

await go('/archive');
await record('show-card', 'default', page.getByRole('button', { name: /EP / }).first(), { group: 'card', title: 'Archive show card' });
await states('tab', page.getByRole('button', { name: 'Shows', exact: true }), { group: 'tabs', title: 'Archive Shows tab' });
await record('tab-saved', 'default', page.getByRole('button', { name: 'Saved', exact: true }), { group: 'tabs', title: 'Archive Saved tab' });

await go('/about');
await record('manifesto', 'default', page.locator('h1').first(), { group: 'type', title: 'About headline' });

await go('/sign-in');
// Look only. Do not type or submit.
await record('text-field', 'default', page.getByPlaceholder('Enter your Email'), { group: 'text field', title: 'Sign-in email field' });
await record('sign-in-button', 'default', page.getByRole('button', { name: 'SIGN IN', exact: true }), { group: 'button', title: 'Sign-in submit, disabled until filled' });
await record('auth-wall', 'default', page.locator('h1').first(), { group: 'pattern', title: 'Sign-in wall heading' });

await go('/moods');
await record('mood-card', 'default', page.getByRole('button', { name: /THINK/ }).first(), { group: 'card', title: 'Mood station' });

fs.writeFileSync(path.join(RAW, 'components-computed.json'), JSON.stringify(out, null, 1) + '\n');
log('wrote', Object.keys(out.components).length, 'components');
await browser.close();
