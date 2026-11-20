import assert from 'node:assert/strict';
import test from 'node:test';
import { pruneStale, mergeLayout } from './readings.mjs';

const comps = () => ({
  'a-button': { run: 'home', states: { default: {}, hover: {}, pressed: {} } },
  'a-gone': { run: 'home', states: { default: {} } },
  'b-card': { run: 'academy', states: { default: {} } },          // academy threw before reaching it
  'b-tab': { run: 'academy', states: { default: {}, hover: {} } }, // reached before academy threw
  'c-row': { run: 'news', states: { default: {} } },               // a later page, not rerun
  'd-old': { states: { default: {} } },                            // an entry with no run recorded
});

test('a finished page drops what it no longer produces and the states its spec no longer lists', () => {
  const c = comps();
  const dropped = pruneStale(c, {
    done: new Set(['home']), touched: new Set(['a-button', 'b-tab']),
    listed: new Map([['a-button', new Set(['default', 'hover'])], ['b-tab', new Set(['default'])]]),
  });
  assert.deepEqual(dropped, ['a-button pressed', 'a-gone']);
  assert.deepEqual(Object.keys(c['a-button'].states), ['default', 'hover']);
});

test('a page that threw, a later page and an entry with no run keep every reading', () => {
  const c = comps();
  pruneStale(c, { done: new Set(['home']), touched: new Set(['a-button', 'b-tab']), listed: new Map([['b-tab', new Set(['default'])]]) });
  assert.ok(c['b-card'] && c['c-row'] && c['d-old']);
  assert.deepEqual(Object.keys(c['b-tab'].states), ['default', 'hover']);
});

test('with no finished page nothing is dropped', () => {
  const c = comps();
  assert.deepEqual(pruneStale(c, { done: new Set(), touched: new Set(), listed: new Map() }), []);
  assert.deepEqual(Object.keys(c), Object.keys(comps()));
});

const earlier = {
  'home@1440': { label: 'home', vw: 1440, old: true },
  'mobile-home@390': { label: 'mobile-home', vw: 390, old: true },
  'removed@1440': { label: 'removed', vw: 1440, old: true },
};

test('a copy that fails to open keeps its earlier layout reading', () => {
  const got = mergeLayout(earlier, { 'home@1440': { label: 'home', vw: 1440 } }, { failed: ['mobile-home'], labels: ['home', 'mobile-home'] });
  assert.deepEqual(got['home@1440'], { label: 'home', vw: 1440 });
  assert.equal(got['mobile-home@390'].old, true);
  assert.equal(got['removed@1440'].old, true, 'a partial run drops nothing');
});

test('a complete run replaces every reading and drops copies no longer on disk', () => {
  const fresh = { 'mobile-home@390': { label: 'mobile-home', vw: 390 }, 'home@1440': { label: 'home', vw: 1440 } };
  const got = mergeLayout(earlier, fresh, { failed: [], labels: ['home', 'mobile-home'] });
  assert.deepEqual(Object.keys(got), ['home@1440', 'mobile-home@390']);
  assert.ok(!got['home@1440'].old && !got['mobile-home@390'].old);
});

test('a copy read at a new width replaces the old width, and the file keeps label order', () => {
  const got = mergeLayout({ 'home@1280': { label: 'home' }, 'home-dark@1440': { label: 'home-dark' } },
    { 'home@1440': { label: 'home' }, 'home-dark@1440': { label: 'home-dark' } }, { failed: [], labels: ['home', 'home-dark'] });
  assert.deepEqual(Object.keys(got), ['home@1440', 'home-dark@1440']);
  assert.deepEqual(mergeLayout(undefined, {}, { failed: [], labels: [] }), {});
});
