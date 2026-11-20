import assert from 'node:assert/strict';
import test from 'node:test';
import { noQuery, scrubQueries } from './no-query.mjs';

// Hostile inputs first: each is a way a query or a token-bearing fragment has slipped past, or could.
// A URL ends where its context says: the quote around it, the url( ) around it, or, bare, the next
// space or quote (a closing bracket at the very end is given back only when the kept URL opened it).
const CUT = {
  // absolute
  'https://cdn.example.test/a.png?X-Amz-Signature=1': 'https://cdn.example.test/a.png',
  'https://cdn.example.test/a.png#access_token=abc': 'https://cdn.example.test/a.png',
  'https://cdn.example.test/a.png?crop=(0,0)&token=abc 2x': 'https://cdn.example.test/a.png 2x',
  'url(https://cdn.example.test/a.png?sig=1)': 'url(https://cdn.example.test/a.png)',
  // scheme-relative
  '//cdn.example.test/avatar.png?token=secret': '//cdn.example.test/avatar.png',
  '"//cdn.example.test/a.png#access_token=abc"': '"//cdn.example.test/a.png"',
  'image-set("//cdn.example.test/a.png?sig=1" 1x, //cdn.example.test/b.png?sig=2 2x)': 'image-set("//cdn.example.test/a.png" 1x, //cdn.example.test/b.png 2x)',
  // relative, with parentheses in the query or the path
  '/avatar.png?crop=(0,0)&token=secret': '/avatar.png',
  'avatar(1).png?token=secret': 'avatar(1).png',
  '"/img/a(2).png?crop=(1,2)&sig=x" 2x': '"/img/a(2).png" 2x',
  '/a.png?x=1)&token=secret': '/a.png',
  'url(/a.png?sig=1)': 'url(/a.png)',
  'url( "/a(1).png?sig=(x)" )': 'url( "/a(1).png" )',
  'image-set(/a.png?sig=1 1x, /b.png?crop=(0,0)&sig=2 2x)': 'image-set(/a.png 1x, /b.png 2x)',
  'image-set(url(/a.png?sig=1) 1x)': 'image-set(url(/a.png) 1x)',
  '/media/avatar.png?token=secret': '/media/avatar.png',
  '"avatar.png?sig=abc"': '"avatar.png"',
  // nested and mixed quotes: the URL ends at its own closing quote, whatever the other quote does
  [`"/a.png?q='x' token=s"`]: '"/a.png"',
  [`'/a.png?note="hi there"&sig=1'`]: "'/a.png'",
  'img[src="/a/b.png?sig=1"]': 'img[src="/a/b.png"]',
  'img[src=/a/b.png?sig=1]': 'img[src=/a/b.png]',
  'a[href="/x?t=1"], a[href=\'/y?t=2\']': 'a[href="/x"], a[href=\'/y\']',
  // a quoted value with a space or text before the URL (Greptile on the context rewrite)
  '" https://cdn.example.test/avatar.png?token=secret"': '" https://cdn.example.test/avatar.png"',
  '"see /media/a.png?sig=1 for more"': '"see /media/a.png"',
  "'avatar: //cdn.example.test/a(1).png#access_token=x'": "'avatar: //cdn.example.test/a(1).png'",
  '"Ready? then /next?t=1"': '"Ready? then /next"',
  // a space inside the URL itself: only the closing quote ends it
  '"https://cdn.example.test/avatar 1?token=secret"': '"https://cdn.example.test/avatar 1"',
  '"/media/my photo.png?sig=1"': '"/media/my photo.png"',
  '"/a.png /b.png?sig=1"': '"/a.png /b.png"',
  // a srcset in one quoted value: the quotes delimit one URL, so what follows its query goes with it
  '"/a.png?s=1 1x, /b.png?s=2 2x"': '"/a.png"',
  // a relative fragment that carries a parameter
  '/cb#access_token=abc&state=x': '/cb',
  '"./login.html#token=abc"': '"./login.html"',
};

const KEEP = [
  `url("data:image/svg+xml,<svg viewBox='0 0 1 1'/>?x=1")`,
  'data:image/png;base64,iVBOR?w0#AA=', 'image-set(data:image/png;base64,AA?x=1 1x)',
  'url(data:image/svg+xml;utf8,%3Csvg%3E?x=(1)%3C/svg%3E)',
  '"data:image/png;base64,iVBOR?w0#AAA="',
  'icons.svg#close', 'url(#clip)', 'a[href="#top"]', '#5e6ad2', 'calc(100% - 2px)', '0 1px 2px rgba(0, 0, 0, 0.1)',
  '1.5rem', 'url(…)', 'a // b', '', 'var(--x, 4px)', 'what? why?', '"Ready?"', '"Is it ready? Yes."', '"Yes. What?"', '"a data:image/png;base64,AA?x=1"', 'rotate(45deg)',
];

test('every hostile input loses its query and its token-bearing fragment', () => {
  for (const [v, want] of Object.entries(CUT)) assert.equal(noQuery(v), want, v);
});

test('no output of the hostile table still holds a parameter', () => {
  for (const v of Object.keys(CUT)) assert.doesNotMatch(noQuery(v), /token|secret|signature|sig=|crop|state=|note=|[?&]\w+=/i, v);
});

test('data: URLs, plain fragments and plain values are left alone', () => {
  for (const v of KEEP) assert.equal(noQuery(v), v, v);
  assert.equal(noQuery(3), 3);
  assert.equal(noQuery(null), null);
});

test('scrubQueries walks objects, arrays and keys', () => {
  assert.deepEqual(scrubQueries({ '--a': '//x.test/a.png?t=1', list: ['/b.png?t=2', 4], 'img[src="/c.png?sig=3"]': 1 }),
    { '--a': '//x.test/a.png', list: ['/b.png', 4], 'img[src="/c.png"]': 1 });
});

test('keys that clean to the same key are merged, counts summed', () => {
  // vars.mjs counts custom properties per selector; two selectors that differ only in a query are one
  const got = scrubQueries({ bySelector: { 'img[src="/a.png?sig=1"]': 2, 'img[src="/a.png?sig=2"]': 3, ':root': 7 },
    nested: { 'a[href="/x?t=1"]': { n: 1, list: ['p'] }, 'a[href="/x?t=2"]': { n: 4, list: ['q'], only: 'b' } } });
  assert.deepEqual(got, { bySelector: { 'img[src="/a.png"]': 5, ':root': 7 },
    nested: { 'a[href="/x"]': { n: 5, list: ['p', 'q'], only: 'b' } } });
  assert.deepEqual(Object.keys(scrubQueries(JSON.parse('{"__proto__": 1}'))), ['__proto__']);
});
