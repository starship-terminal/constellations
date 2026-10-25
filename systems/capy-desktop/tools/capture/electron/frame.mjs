// PRODUCT (adapt): the native window frame, which CDP's screenshot leaves out. Capy's window is
// titleBarStyle hiddenInset with the traffic lights at (16, 12) over the web page's tab strip, so the lights
// exist only in the window server's picture. This holds the emulated colour scheme while macOS captures the
// window by its id (screencapture -l), and writes $RAW/<theme>/native/window-frame.png (Display P3; quantize.py
// converts it to sRGB).
//
//   PORT=9407 SCHEME=dark node tools/capture/electron/frame.mjs dark
import { execFileSync } from 'node:child_process';
import { mkdirSync } from 'node:fs';
import { basename, dirname, resolve as pathResolve } from 'node:path';
import { fileURLToPath } from 'node:url';
import { connect, disconnect } from './cdp.mjs';
import * as P from './product.mjs';

const HERE = dirname(fileURLToPath(import.meta.url));
const SLUG = process.env.SLUG || basename(pathResolve(HERE, '../../..'));
const RAW = process.env.RAW || `${process.env.HOME}/.design-systems/${SLUG}/raw-shots`;
const theme = process.argv[2];
if (!theme) { console.error('usage: frame.mjs <theme>'); process.exit(2); }
const h = await connect(P.WINDOWS.app);
try {
  await P.home(h);
  await h.page.evaluate(() => document.activeElement && document.activeElement.blur());
  execFileSync('osascript', ['-e', `tell application "${P.NAME}" to activate`]);
  await h.page.waitForTimeout(1500);
  const repo = pathResolve(HERE, '../../../../..');
  const id = execFileSync('swift', [`${repo}/tools/kit/capture/native/winid.swift`, P.NAME]).toString().trim();
  const out = `${RAW}/${theme}/native/window-frame.png`;
  mkdirSync(dirname(out), { recursive: true });
  execFileSync('screencapture', ['-o', '-x', '-l', id, out]);
  console.log(out, 'window', id);
} finally {
  await disconnect(h.browser);
}
