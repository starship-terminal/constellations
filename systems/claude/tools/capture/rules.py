#!/usr/bin/env python3
"""Read the rules Claude's stylesheets apply under conditions and states, and write raw/css-rules.json.

    SNAPS=<dir of page copies> python3 tools/capture/rules.py

vars.mjs keeps custom properties only, so the values a product sets in ordinary declarations are
missing from it: where its layout changes width, what it does under reduced motion, what a
pressed control does, and which border widths it draws. This reads the same <style> blocks
snapshot.js inlined into every page copy (deduplicated by content, as vars.mjs does), walks every
rule with its enclosing @media / @supports / @layer / @container, and tallies:

  breakpoints     every width condition in an @media or @container query, in px, with the number
                  of rules under it and whether it is one of Tailwind's named screens
  reducedMotion   what changes under `prefers-reduced-motion: reduce`, under Claude's own setting
                  (`[data-reduce-motion="true"]`, written by Settings > Motion > Reduced) and
                  under Tailwind's `motion-reduce:` / `motion-safe:` variants
  pressed         every :active rule and aria-pressed / data-pressed rule, by property and value
  borderWidths    every border width and outline width declared, with counts
  gridColumns     every grid-template-columns value, with counts
  links           the rules that style a link's colour and underline

No network: the copies are read from disk.
"""
import collections, hashlib, json, os, pathlib, re, sys

HERE = pathlib.Path(__file__).resolve().parent
REF = HERE.parent.parent
SNAPS = os.environ.get('SNAPS')
if not SNAPS:
    sys.exit('SNAPS=<dir of page copies> is required')

TAILWIND_SCREENS = {640: 'sm (40rem)', 768: 'md (48rem)', 1024: 'lg (64rem)', 1280: 'xl (80rem)', 1536: '2xl (96rem)'}


def blocks():
    seen, out = set(), []
    for f in sorted(pathlib.Path(SNAPS).glob('*.html')):
        html = f.read_text(encoding='utf-8')
        for m in re.finditer(r'<style([^>]*)>(.*?)</style>', html, re.S):
            css = m.group(2).replace('<\\/style', '</style')
            key = hashlib.sha1((m.group(1) + css).encode()).hexdigest()
            if key not in seen:
                seen.add(key)
                out.append(css)
    return out


def _split_selector(prelude):
    """Split `color: red; .title` into the closed declaration and the selector.

    The semicolon has to sit outside quotes and parentheses, so
    `&[data-label="a;b"]` stays one selector. No semicolon means the
    whole prelude is the selector.
    """
    depth, quote, last = 0, None, -1
    i = 0
    while i < len(prelude):
        c = prelude[i]
        if c == '\\':
            i += 2
            continue
        if quote:
            if c == quote:
                quote = None
        elif c in '"\'':
            quote = c
        elif c == '(':
            depth += 1
        elif c == ')' and depth:
            depth -= 1
        elif c == ';' and depth == 0:
            last = i
        i += 1
    if last == -1:
        return '', prelude.strip()
    return prelude[:last + 1], prelude[last + 1:].strip()


def parse(css):
    """Yield (conditions, selector, body) for every style rule; conditions are the at-rule
    preludes around it, outermost first.

    Nested style rules are their own yields. A declaration that sits beside
    one (`color: red; .title { ... } margin: 4px`) stays on the outer rule.
    The nested selector is not folded into that declaration, and a child
    block is not copied into the outer body.
    """
    i, n = 0, len(css)
    # (head, declarations already closed before a nested child)
    stack, start, quote = [], 0, None
    while i < n:
        c = css[i]
        if c == '\\':  # an escape, in a string or in a selector such as .\[data-cds\=\'Button\'\]
            i += 2
            continue
        if quote:
            if c == quote:
                quote = None
            i += 1
            continue
        if c in '"\'':
            quote = c
        elif c == '{':
            prelude = css[start:i]
            owned = ''
            if stack and not stack[-1][0].startswith('@'):
                owned, prelude = _split_selector(stack[-1][1] + prelude)
                stack[-1][1] = owned
            stack.append([prelude.strip(), ''])
            start = i + 1
        elif c == '}':
            if stack:
                head, owned = stack.pop()
                body = owned + css[start:i]
                # a step inside @keyframes (0%, from, to) is not a style rule.
                if not head.startswith('@') and not any(
                        frame[0].startswith(('@keyframes', '@-webkit-keyframes')) for frame in stack):
                    if ':' in body:
                        yield [frame[0] for frame in stack], head, body
            start = i + 1
        elif c == ';' and not stack:
            start = i + 1
        i += 1


def _split_declarations(body):
    """Split a declaration list on semicolons outside quotes and parentheses."""
    parts, start, depth, quote = [], 0, 0, None
    i = 0
    while i < len(body):
        c = body[i]
        if c == '\\':
            i += 2
            continue
        if quote:
            if c == quote:
                quote = None
        elif c in '"\'':
            quote = c
        elif c == '(':
            depth += 1
        elif c == ')' and depth:
            depth -= 1
        elif c == ';' and depth == 0:
            parts.append(body[start:i])
            start = i + 1
        i += 1
    parts.append(body[start:])
    return parts


def decls(body):
    out = []
    for part in _split_declarations(body):
        if ':' in part:
            k, v = part.split(':', 1)
            out.append((k.strip(), v.strip()))
    return out


def px(value, unit):
    v = float(value)
    return round(v * 16) if unit in ('rem', 'em') else round(v)


def main():
    rules = [r for css in blocks() for r in parse(css)]
    bp = {'@media': collections.defaultdict(lambda: {'rules': 0, 'queries': collections.Counter()}),
          '@container': collections.defaultdict(lambda: {'rules': 0, 'queries': collections.Counter()})}
    squish = []
    reduce_props, reduce_sel = collections.Counter(), collections.Counter()
    app_reduce, tw_reduce, tw_safe = collections.Counter(), collections.Counter(), 0
    pressed, pressed_sel = collections.Counter(), []
    borders, outlines, grid = collections.Counter(), collections.Counter(), collections.Counter()
    links = []
    for conds, sel, body in rules:
        ds = decls(body)
        for cond in conds:
            if cond.startswith(('@media', '@container')):
                for value, unit in re.findall(r'(?:width\s*[<>]=?\s*|min-width:\s*|max-width:\s*)([\d.]+)(px|rem|em)', cond):
                    w = px(value, unit)
                    kind = bp['@media' if cond.startswith('@media') else '@container']
                    kind[w]['rules'] += 1
                    kind[w]['queries'][re.sub(r'\s+', ' ', cond)] += 1
        if any('prefers-reduced-motion: reduce' in c for c in conds):
            for k, v in ds:
                reduce_props[f'{k}: {v}'] += 1
            reduce_sel[sel[:120]] += 1
        if '[data-reduce-motion="true"]' in sel:
            for k, v in ds:
                app_reduce[f'{k}: {v}'] += 1
        if 'motion-reduce\\:' in sel:
            for k, v in ds:
                tw_reduce[f'{k}: {v}'] += 1
        if 'motion-safe\\:' in sel:
            tw_safe += 1
        if 'squish' in sel or '--cds-btn-press' in body or '--cds-card-press' in body:
            squish.append({'selector': sel[:200], 'declarations': dict(ds)})
        if re.search(r':active\b|aria-pressed|\[data-pressed\]', sel):
            for k, v in ds:
                pressed[f'{k}: {v}'] += 1
            if ':active' in sel and ('btn' in sel or 'Button' in sel or 'Card' in sel):
                pressed_sel.append({'selector': sel[:200], 'declarations': dict(ds)})
        for k, v in ds:
            if re.fullmatch(r'border(-(top|right|bottom|left|inline|block)(-(start|end))?)?-width', k):
                borders[v] += 1
            elif re.fullmatch(r'border(-(top|right|bottom|left|inline|block)(-(start|end))?)?', k):
                w = re.match(r'([\d.]+px|thin|medium|thick|0)\b', v)
                if w:
                    borders[w.group(1)] += 1
            elif k in ('outline-width', 'outline'):
                w = re.match(r'([\d.]+px|var\([^)]*\))', v)
                if w:
                    outlines[w.group(1)] += 1
            elif k == 'grid-template-columns':
                grid[v] += 1
        if re.search(r'(^|[\s>,(])a(:[\w-]+)?($|[\s,)\[])', sel) and any(k in ('color', 'text-decoration', 'text-decoration-line', 'text-decoration-color', 'text-underline-offset', 'text-decoration-thickness') or k.startswith('--_text-link') for k, _ in ds):
            links.append({'selector': sel[:200], 'conditions': conds[-1:], 'declarations': dict(ds)})
    top = lambda c, n: [{'value': k, 'count': v} for k, v in c.most_common(n)]
    out = {
        'readAt': '2026-10-17',
        'source': "the <style> blocks snapshot.js inlined into each 2026-10-17 page copy (claude.ai's CSS from assets-proxy.anthropic.com), deduplicated by content",
        'rules': len(rules),
        # @media widths are the page's breakpoints; @container widths belong to one component each
        'breakpoints': [{'px': w, 'rules': b[w]['rules'], 'tailwind': TAILWIND_SCREENS.get(w), 'queries': [q for q, _ in b[w]['queries'].most_common(3)]} for b in [bp['@media']] for w in sorted(b)],
        'containerWidths': [{'px': w, 'rules': b[w]['rules']} for b in [bp['@container']] for w in sorted(b)],
        'reducedMotion': {
            'mediaRules': sum(reduce_sel.values()),
            'mediaDeclarations': top(reduce_props, 40),
            'mediaSelectors': top(reduce_sel, 25),
            'appSetting': {'selector': '[data-reduce-motion="true"]', 'declarations': top(app_reduce, 30)},
            'tailwindMotionReduce': top(tw_reduce, 20),
            'tailwindMotionSafeRules': tw_safe,
        },
        'pressed': {'declarations': top(pressed, 40), 'squish': squish[:20], 'buttonRules': pressed_sel[:20]},
        'borderWidths': top(borders, 20),
        'outlineWidths': top(outlines, 12),
        'gridColumns': top(grid, 30),
        'links': links[:30],
    }
    path = REF / 'raw' / 'css-rules.json'
    path.write_text(json.dumps(out, indent=1, ensure_ascii=False) + '\n')
    print(f"{len(rules)} rules; {len(out['breakpoints'])} @media widths; {out['reducedMotion']['mediaRules']} reduced-motion rules; {sum(pressed.values())} pressed declarations; {len(links)} link rules -> {path.relative_to(REF)}")


if __name__ == '__main__':
    main()
