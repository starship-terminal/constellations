// Script stripping for the archived page copies prepare-pages.mjs writes.
// No dependencies, so tools/test_sanitize.py can run it in Node.

const URL_ATTRS = new Set(['href', 'src', 'action', 'formaction', 'xlink:href', 'data', 'poster', 'background', 'srcdoc']);

function decoded(v) {
  return v
    .replace(/&#x([0-9a-f]+);?/gi, (_, h) => String.fromCodePoint(parseInt(h, 16)))
    .replace(/&#(\d+);?/g, (_, d) => String.fromCodePoint(Number(d)))
    .replace(/&colon;/gi, ':').replace(/&tab;|&newline;/gi, '')
    .replace(/[\u0000-\u0020]/g, '')
    .toLowerCase();
}

// One start tag with its event handlers dropped and any script URL emptied.
export function cleanTag(tag) {
  const m = tag.match(/^<([a-zA-Z][\w:-]*)([\s\S]*?)(\/?)>$/);
  if (!m) return tag;
  const [, name, rest, self] = m;
  const kept = [];
  for (const a of rest.matchAll(/([^\s"'>\/=]+)(?:\s*=\s*("[^"]*"|'[^']*'|[^\s"'=<>`]+))?/g)) {
    const attr = a[1].toLowerCase();
    if (attr.startsWith('on')) continue;
    let val = a[2];
    if (val !== undefined && URL_ATTRS.has(attr)) {
      const raw = /^["']/.test(val) ? val.slice(1, -1) : val;
      if (/^(javascript|vbscript|data:text\/html)/.test(decoded(raw)) || attr === 'srcdoc') val = '"#"';
    }
    kept.push(val === undefined ? a[1] : `${a[1]}=${val}`);
  }
  return `<${name}${kept.length ? ' ' + kept.join(' ') : ''}${self ? ' /' : ''}>`;
}
