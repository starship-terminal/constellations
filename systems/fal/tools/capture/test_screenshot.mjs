import assert from 'node:assert/strict';
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import test from 'node:test';
import vm from 'node:vm';
import { pngDimensions, screenshotWithMetadata } from './screenshot.mjs';

// Only the IHDR is needed to exercise the dimension reader; no image decoder
// or browser dependency is involved in these contract tests.
function png(width, height) {
  const bytes = Buffer.alloc(33);
  Buffer.from([137, 80, 78, 71, 13, 10, 26, 10]).copy(bytes);
  bytes.writeUInt32BE(13, 8); bytes.write('IHDR', 12);
  bytes.writeUInt32BE(width, 16); bytes.writeUInt32BE(height, 20);
  return bytes;
}
const actual = {
  innerWidth: 884, innerHeight: 1104, devicePixelRatio: 2,
  theme: { classes: ['dark'], attributes: { 'data-mode': 'dark' }, colorScheme: 'dark' },
  visualViewport: { width: 884, height: 1104, scale: 1, offsetLeft: 0, offsetTop: 0, pageLeft: 0, pageTop: 0 },
  documentSize: { width: 884, height: 2400 }, scroll: { x: 0, y: 30 },
};
function fakePage(width, height, viewport = { width: 884, height: 1104 }, metrics = actual) {
  return { viewportSize: () => viewport, evaluate: async () => metrics,
    screenshot: async options => { assert.equal(options.type, 'png'); return png(width, height); } };
}
function temporary(t) {
  const dir = fs.mkdtempSync(path.join(os.tmpdir(), 'capture-test-'));
  t.after(() => fs.rmSync(dir, { recursive: true, force: true }));
  return path.join(dir, 'state.png');
}

test('records requested and actual sizes separately; dimensions cannot accept visual content', async t => {
  const output = temporary(t);
  const result = await screenshotWithMetadata(fakePage(1768, 2208), { path: output },
    { viewport: { width: 1440, height: 900 }, deviceScaleFactor: 2 });
  assert.deepEqual(result.requested.viewport, { width: 1440, height: 900 });
  assert.equal(result.actual.innerWidth, 884);
  assert.deepEqual(result.actual.theme, actual.theme);
  assert.ok(!Number.isNaN(Date.parse(result.capturedAt)));
  assert.equal(result.sanitizedSourceUrl, null);
  assert.deepEqual(result.actual.visualViewport, actual.visualViewport);
  assert.deepEqual(result.png, { width: 1768, height: 2208 });
  assert.equal(result.dimensionCheck.status, 'pass');
  assert.equal(result.visualReview.status, 'pending');
  assert.equal(result.cropCoordinates.status, 'unverified');
  assert.deepEqual(JSON.parse(fs.readFileSync(`${output}.capture.json`)), result);
});

test('mobile layout viewport may differ from configured screenshot viewport', async t => {
  const metrics = { ...actual, innerWidth: 980, innerHeight: 2121,
    visualViewport: { ...actual.visualViewport, width: 980, height: 2121, scale: 390 / 980 } };
  const result = await screenshotWithMetadata(fakePage(780, 1688, { width: 390, height: 844 }, metrics),
    { path: temporary(t) }, { viewport: { width: 390, height: 844 }, deviceScaleFactor: 2 });
  assert.equal(result.dimensionCheck.status, 'pass');
  assert.equal(result.actual.innerWidth, 980);
  assert.equal(result.configuredViewport.width, 390);
});

test('browser probe retains safe theme fields and never reads URL or arbitrary root attributes', async t => {
  const root = { scrollWidth: 884, clientWidth: 884, scrollHeight: 1104, clientHeight: 1104,
    classList: ['hashed-class', 'dark', 'owner-example-test'],
    getAttribute: name => ({ 'data-mode': 'dark', 'data-theme': 'owner-example-test',
      'data-color-mode': 'system' })[name] ?? null };
  const page = fakePage(1768, 2208);
  page.url = () => { throw new Error('must not read a live URL'); };
  page.evaluate = async callback => vm.runInNewContext(`(${callback.toString()})()`, {
    document: { documentElement: root, body: null }, window: { visualViewport: null },
    innerWidth: 884, innerHeight: 1104, devicePixelRatio: 2, scrollX: 0, scrollY: 0,
    getComputedStyle: () => ({ colorScheme: 'dark' }),
  });
  const report = await screenshotWithMetadata(page, { path: temporary(t) });
  assert.deepEqual(JSON.parse(JSON.stringify(report.actual.theme)), {
    classes: ['dark'], attributes: { 'data-mode': 'dark', 'data-color-mode': 'system' }, colorScheme: 'dark',
  });
  assert.equal(JSON.stringify(report).includes('owner-example-test'), false);
});

test('full-page validation uses measured document size rather than requested height', async t => {
  const result = await screenshotWithMetadata(fakePage(1768, 4800), { path: temporary(t), fullPage: true });
  assert.deepEqual(result.dimensionCheck.expected, { width: 1768, height: 4800 });
  assert.equal(result.capture.mode, 'fullPage');
});

test('tile validation uses the explicit clip and CSS screenshot scale', async t => {
  const clip = { x: 0, y: 2000, width: 884, height: 400 };
  const result = await screenshotWithMetadata(fakePage(884, 400), { path: temporary(t), fullPage: true, clip, scale: 'css' });
  assert.equal(result.capture.mode, 'clip');
  assert.deepEqual(result.capture.clip, clip);
  assert.deepEqual(result.dimensionCheck.expected, { width: 884, height: 400 });
});

test('attached window without configured viewport records no requested resize', async t => {
  const result = await screenshotWithMetadata(fakePage(1768, 2208, null), { path: temporary(t) });
  assert.deepEqual(result.requested, { viewport: null, deviceScaleFactor: null });
  assert.equal(result.dimensionCheck.status, 'pass');
});

test('creates a fresh output directory and accepts only an explicit sanitized source URL', async t => {
  const output = path.join(path.dirname(temporary(t)), 'fresh', 'state.png');
  const result = await screenshotWithMetadata(fakePage(1768, 2208), { path: output },
    { sanitizedSourceUrl: 'https://example.test/settings' });
  assert.equal(result.sanitizedSourceUrl, 'https://example.test/settings');
  assert.ok(fs.existsSync(`${output}.capture.json`));
});

test('dimension mismatch rejects the capture and retains its failing evidence', async t => {
  const output = temporary(t);
  await assert.rejects(screenshotWithMetadata(fakePage(1778, 1234), { path: output }), /dimension mismatch/);
  const report = JSON.parse(fs.readFileSync(`${output}.capture.json`));
  assert.equal(report.dimensionCheck.status, 'fail');
  assert.deepEqual(report.png, { width: 1778, height: 1234 });
  assert.equal(report.visualReview.status, 'pending');
});

test('a failed viewport probe invalidates an old same-path pass before the browser read', async t => {
  const output = temporary(t);
  fs.writeFileSync(output, png(1768, 2208));
  fs.writeFileSync(`${output}.capture.json`, JSON.stringify({ dimensionCheck: { status: 'pass' }, png: { width: 1768, height: 2208 } }));
  const page = fakePage(1768, 2208);
  page.evaluate = async () => {
    assert.equal(JSON.parse(fs.readFileSync(`${output}.capture.json`)).dimensionCheck.status, 'pending');
    throw new Error('Execution context destroyed');
  };
  page.screenshot = async () => { throw new Error('must not take a screenshot after a failed probe'); };
  await assert.rejects(screenshotWithMetadata(page, { path: output }), /Execution context destroyed/);
  const report = JSON.parse(fs.readFileSync(`${output}.capture.json`));
  assert.equal(report.dimensionCheck.status, 'fail');
  assert.equal(report.dimensionCheck.error, 'Execution context destroyed');
  assert.equal(report.png, null);
  assert.equal(report.actual, null);
});

test('a synchronous configured-viewport error also replaces stale pass metadata', async t => {
  const output = temporary(t);
  fs.writeFileSync(`${output}.capture.json`, JSON.stringify({ dimensionCheck: { status: 'pass' } }));
  const page = fakePage(1768, 2208);
  page.viewportSize = () => { throw new Error('Page closed'); };
  await assert.rejects(screenshotWithMetadata(page, { path: output }), /Page closed/);
  assert.equal(JSON.parse(fs.readFileSync(`${output}.capture.json`)).dimensionCheck.status, 'fail');
});

test('browser rounding of one physical pixel is tolerated, larger drift fails', async t => {
  const result = await screenshotWithMetadata(fakePage(1767, 2209), { path: temporary(t) });
  assert.equal(result.dimensionCheck.status, 'pass');
  await assert.rejects(screenshotWithMetadata(fakePage(1766, 2208), { path: temporary(t) }), /dimension mismatch/);
});

test('invalid/empty PNG and non-PNG screenshot requests are rejected', async t => {
  assert.throws(() => pngDimensions(Buffer.from('not a png')), /not a PNG/);
  assert.throws(() => pngDimensions(png(0, 10)), /empty dimension/);
  const invalid = png(10, 10); invalid.writeUInt32BE(12, 8);
  assert.throws(() => pngDimensions(invalid), /not a PNG/);
  await assert.rejects(screenshotWithMetadata(fakePage(10, 10), { path: temporary(t), type: 'jpeg' }), /requires a .png/);
  const page = fakePage(10, 10); page.screenshot = async () => Buffer.from('invalid');
  const output = temporary(t);
  await assert.rejects(screenshotWithMetadata(page, { path: output }), /not a PNG/);
  assert.equal(JSON.parse(fs.readFileSync(`${output}.capture.json`)).dimensionCheck.status, 'fail');
});
