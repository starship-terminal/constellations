import assert from 'node:assert/strict';
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import test from 'node:test';
import { updateReadings } from './readings.mjs';

function saved(t, data) {
  const dir = fs.mkdtempSync(path.join(os.tmpdir(), 'readings-test-'));
  t.after(() => fs.rmSync(dir, { recursive: true, force: true }));
  const file = path.join(dir, 'raw', 'layout.json');
  if (data) { fs.mkdirSync(path.dirname(file)); fs.writeFileSync(file, JSON.stringify(data)); }
  return file;
}
const quiet = () => {};

test('a run over one page keeps the other saved page', async t => {
  const file = saved(t, { 'home@1440': { h1: 'old' }, 'search@1440': { h1: 'kept' } });
  await updateReadings(file, [['home@1440', async () => ({ h1: 'new' })]], quiet);
  assert.deepEqual(JSON.parse(fs.readFileSync(file, 'utf8')), { 'home@1440': { h1: 'new' }, 'search@1440': { h1: 'kept' } });
});

test('a page that fails keeps its saved reading', async t => {
  const file = saved(t, { 'home@1440': { h1: 'old' }, 'search@1440': { h1: 'kept' } });
  await updateReadings(file, [['home@1440', async () => { throw new Error('timeout'); }], ['search@1440', async () => ({ h1: 'new' })]], quiet);
  assert.deepEqual(JSON.parse(fs.readFileSync(file, 'utf8')), { 'home@1440': { h1: 'old' }, 'search@1440': { h1: 'new' } });
});

test('a first run creates the file', async t => {
  const file = saved(t, null);
  await updateReadings(file, [['home@390', async () => ({ vw: 390 })]], quiet);
  assert.deepEqual(JSON.parse(fs.readFileSync(file, 'utf8')), { 'home@390': { vw: 390 } });
});
