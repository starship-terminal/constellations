#!/usr/bin/env python3
"""Neutralise every user-written string in a directory of Claude page copies, before they are rendered.

usage: python3 neutralise.py SRC_DIR DST_DIR [--map MAP.json]

snapshot.js removes the account's name and email, but the copies still hold the owner's chat titles
(sidebar, Chats page, search), artifact and project names, file names and the text of the thread that
was open. Screenshots and crops show all of it. This script writes a second copy in DST_DIR in which
every text node and every aria-label, title, alt, placeholder and value that is not interface text has been
replaced, so render-all.sh, measure.mjs and layout.mjs can run on DST_DIR (SNAPS) and nothing private
reaches a pixel or a raw/*.json value.

What counts as interface text is the KEEP list below, month and relative-time labels, and any string
without three letters in a row. Everything else is replaced by a neutral stand-in:

  pinned titles                  Pinned chat N
  other chat and list titles     Conversation N
  titles on the Artifacts page   Artifact N
  file names                     File N.<ext>
  thread text, long text         filler words of the same length, so wrapping stays about the same

The same string always gets the same stand-in, so a title in the sidebar, the header, the search
dialog and a `More options for ...` label stay consistent. --map writes the string-to-stand-in table;
it holds the private strings, so write it outside the repository and never commit it. A page copy
that fails to show an interface string means the string is missing from KEEP: add it. measure.mjs
finds several components by their text (`T('Take a screenshot')` and so on), so every string it
looks up must be in KEEP; measure.mjs reports "element not found" when one is not. A label that only an attribute carries is replaced too unless it
is in ATTR_KEEP. The copy of SRC_DIR-cdn-cache is linked beside DST_DIR as DST_DIR-cdn-cache.
"""
import collections, glob, html, json, os, re, sys

KEEP = {k.strip() for k in '''
Artifacts|Chats and tasks|Code|Home|Learner|Max|New|O|Pinned|Shift|View all|More|Command|Medium|Opus 5.5|Chat|Cowork
Hello, night owl|How can I help you today?|New chat - Claude|Type / for skills|Projects|Memory|Scheduled|Customize|Settings|Search|Share
Ctrl|Anthropic|Claude|Done when|Improved|Original|Reason|Scope|Goal|Deliverables|What to document|How to extract values|No finish line
What changed and why:|markdown|learner@example.com|A project|Design systems|Reflect|Time and focus|Take a screenshot|Research|Design system
Claude is AI and can make mistakes. Please double-check responses.|Use the up and down arrow keys to move between messages.
Beta|Select|All|Claude Design|Connectors|Created|Docs|Design|Edited|Language|Skills|Slides|Usage|Viewed|Yours|Shared with you|Make something new
Visit the standalone homepage|Add to project|Account|Actions|Add files or photos|Add from GitHub|Add plugins|Anthropic Serif|Appearance|Billing|Capabilities|Chat font
Claude Code|Claude in Chrome|Code notifications|Code permission requests|Context|Delete|Dispatch messages|Edit sidebar…|Effort|English|Fable 5.1|Fast|Fastest for quick answers
For complex work and everyday tasks|For your toughest challenges|General|Get API keys|Get apps and extensions|Get help|Haiku 4.5|Instructions|Learn more|Log out|Mellow|Message collapsed|More models
Most efficient for simpler tasks|Motion|Move to group|New project|Notifications|Only you|Open menu|Past month|Past week|Paused|Pin|Plugins|Privacy|Recents|Reduced|Rename|Response completions
Scheduled tasks|Show more|Sonnet 5.5|Speed|Style|System|Theme|Today|Voice|View all plans|View memory|Web search|on Claude Platform|Show message actions|Thought for 6s
Emails from Claude Code cloud sessions|Add PDFs, documents, or other text to reference in this project.|Set up recurring tasks for this project.
Claude can choose to notify you about important updates from a Code session.
Get a push notification on your phone when Claude messages you in Dispatch.
Get a push notification when Claude needs your approval to run a command in a Code session.
Get an email when a cloud session has finished building or needs your response.
Get notified when Claude has finished a response. Useful for long-running tasks.
Get notified when scheduled tasks finish, can’t run, or need your input.
Reduce animation in streaming responses and other interface elements.
View and manage what Claude remembers from your chats.
Example project|How to use Claude|Claude Design lives here now|Migrate team design systems
PBC|support@anthropic.com
'''.replace('\n', '|').split('|') if k.strip()}
# whole strings that cannot sit in the '|' list above
KEEP |= {
    'New Slides and Design projects are created as artifacts. Migrate your design systems here to use them across all your artifacts and Claude sessions.',
    'A card with a "Start with a prompt" link is available — press Tab until focus enters the card, Escape to return.',
    'An example project that also doubles as a how-to guide for using Claude. Chat with it to learn more about how to get the most out of chatting with Claude!',
    'We’ve migrated to a new memory system. You have 2 days left if you’d like to',
    'export this project’s legacy memory',
    'Anthropic PBC | 사업자등록번호 86-1969045 (미국 델라웨어) | 다리오 아모데이',
}
# interface labels that only occur in attributes (aria-label, title, placeholder, value); a prefix such as
# "More options for " is stripped before the rest is looked up
ATTR_KEEP = {k.strip() for k in '''
Add files|Add files, connectors, and more|Add scheduled task|Bad response|Chat messages|Close|Close sidebar|Copy|Copy to clipboard|Dark|Design, Beta|Dismiss|Docs, Beta|Done
Edit|Edit instructions|Filter and group recents|Filter by|Filter by type: All types|Good response|Grid view|Hide sidebar|Idle|Light|Mark as unread|Message actions|Mode
Model: Opus 5.5 Medium|More navigation items|New from a template|Pin project|Press and hold to record|Private|Public|Quick task|Read aloud|Resize file viewer|Resize sidebar|Retry
Scroll to bottom|Search chats and projects|Search mode|Search projects|Search results|Search settings|Search your activity|Search your artifacts|Send message|Shared with your organization
Slides, Beta|Show sidebar|Sidebar|Sort projects|Surface|Turn on microphone|Upload files|Use incognito|Use voice mode|Write a message…|Write your prompt to Claude
auto|chat|cowork|dark|fast|light|mellow|reduce|serif|system|markdown code|Learner, Learner|Search|Claude|New chat - Claude
'''.replace('\n', '|').split('|') if k.strip()}
ATTR_PREFIX = ('More options for ', 'Select ', 'Open standalone version of ', 'Show message actions for ', 'Rename ')
DATE = re.compile(r'^((Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]* \d{1,2}(, \d{4})?|(January|February|March|April|May|June|July|August|September|October|November|December)( \d{4})?|\d+ (runs|hours ago|days ago)|\d+ ?(h|d) ago)$')
FILES = re.compile(r'\.(md|jsx|html|py|js|pdf|png|txt|docx)$')
FILL = ('amet consectetur elit sed tempor labore magna aliqua enim minim veniam quis nostrud ullamco laboris nisi aliquip commodo '
        'consequat duis aute irure dolor reprehenderit voluptate velit esse cillum fugiat nulla pariatur excepteur sint occaecat cupidatat '
        'proident sunt culpa officia deserunt mollit anim').split()
SPLIT = re.compile(r'(<style\b.*?</style>|<script\b.*?</script>)', re.S)
TEXT = re.compile(r'>([^<>]+)<')
IDS = [(re.compile(r'/(chat|project)/[0-9a-fA-F-]{8,}'), r'/\1/<id>'), (re.compile(r'artifactId=[^&"\s]+'), 'artifactId=<id>'),
       (re.compile(r'versionUuid=[0-9a-fA-F-]+'), 'versionUuid=<id>')]
ATTR = re.compile(r'\b(aria-label|title|alt|placeholder|aria-description|data-label|value)="([^"]*)"')


def is_ui(t):
    if t in KEEP or DATE.match(t):
        return True
    return not re.search(r'[A-Za-zÀ-￿]{3}', t)  # symbols, numbers, single letters


def filler(n, seed):
    out, size, i = [], 0, seed * 7
    while size < n:
        w = FILL[i % len(FILL)]
        i += 3
        out.append(w)
        size += len(w) + 1
    s = ' '.join(out)[:max(n, 4)].rstrip()
    return s[0].upper() + s[1:]


def text_nodes(path):
    out = []
    for seg in SPLIT.split(open(path, encoding='utf-8').read()):
        if seg.startswith(('<style', '<script')):
            continue
        out += [html.unescape(m.group(1)).strip() for m in TEXT.finditer(seg)]
    return [t for t in out if t]


def attr_values(path):
    out = []
    for seg in SPLIT.split(open(path, encoding='utf-8').read()):
        if not seg.startswith(('<style', '<script')):
            out += [html.unescape(m.group(2)).strip() for m in ATTR.finditer(seg)]
    return [v for v in out if v]


def build_map(files):
    where = collections.OrderedDict()
    for f in files:
        for t in text_nodes(f):
            if not is_ui(t):
                where.setdefault(t, set()).add(os.path.basename(f))
    # a label that only an attribute carries (no text node says the same) is private unless it is a known interface label
    for f in files:
        for v in attr_values(f):
            core = v
            for p in ATTR_PREFIX:
                if core.startswith(p):
                    core = core[len(p):]
            if is_ui(core) or core in ATTR_KEEP or re.match(r'Message \d+ of \d+$', core) or any(k in core for k in where):
                continue
            where.setdefault(core, set()).add(os.path.basename(f))
    # the pinned rows are the titles between the "Pinned" and "Chats and tasks" labels of the first sidebar
    pinned, side = set(), text_nodes(files[0])
    if 'Pinned' in side and 'Chats and tasks' in side:
        pinned = set(side[side.index('Pinned') + 1:side.index('Chats and tasks')])
    kind, mapping = collections.Counter(), {}
    for i, (t, fs) in enumerate(where.items()):
        many = len(fs) >= 15  # in every copy: the sidebar
        short = (len(t) <= 75 and '\n' not in t and (many or not t.endswith(('.', ':', '?', '!')))) or FILES.search(t)
        thread = all(x.startswith(('thread-', 'mobile-thread')) for x in fs)
        if t.startswith("A conversation's "):  # left by the 2026-10-11 text cleanup
            k, ph = 'old', t.replace("A conversation's design system", 'A conversation')
        elif thread and not many and not t.startswith(('Claude responded', 'You said')):
            k, ph = 'fill', filler(len(t), i)
        elif FILES.search(t):
            k, ph = 'file', 'File %d%s' % (kind['file'] + 1, FILES.search(t).group(0))
        elif t.startswith('Claude responded:'):
            k, ph = 'r', 'Claude responded: ' + filler(len(t) - 18, i)
        elif t.startswith('You said:'):
            k, ph = 's', 'You said: ' + filler(len(t) - 10, i)
        elif many and t in pinned:
            k, ph = 'pin', 'Pinned chat %d' % (kind['pin'] + 1)
        elif short and all(x.startswith('artifacts-') for x in fs):
            k, ph = 'art', 'Artifact %d' % (kind['art'] + 1)
        elif short and all(x.startswith('projects-') for x in fs):
            k, ph = 'proj', 'Project %d' % (kind['proj'] + 1)
        elif short:
            k, ph = 'chat', 'Conversation %d' % (kind['chat'] + 1)
        else:
            k, ph = 'fill', filler(len(t), i)
        kind[k] += 1
        mapping[t] = ph
    return mapping


def main():
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    src, dst = args[0], args[1]
    map_out = sys.argv[sys.argv.index('--map') + 1] if '--map' in sys.argv else None
    if map_out and args[-1] == map_out:
        args.pop()
    # the first copy sets the pinned list and the numbering, so it goes first
    files = sorted(glob.glob(src + '/*.html'), key=lambda f: (not f.endswith('/home-dark.html'), f))
    mapping = build_map(files)
    keys = sorted(mapping, key=len, reverse=True)

    def subst(s):
        for k in keys:
            if k in s:
                s = s.replace(k, mapping[k])
        return s

    def node(m):
        t = html.unescape(m.group(1))
        tt = t.strip()
        return '>' + html.escape(t.replace(tt, mapping[tt]), quote=False) + '<' if tt in mapping else m.group(0)

    def attr(m):
        v = html.unescape(m.group(2))
        n = subst(v)
        return m.group(0) if n == v else '%s="%s"' % (m.group(1), html.escape(n, quote=True))

    os.makedirs(dst, exist_ok=True)
    # fonts and images the copies load come from <SNAPS>-cdn-cache (lib.mjs); give the new directory the same cache
    cache, new_cache = src.rstrip('/') + '-cdn-cache', dst.rstrip('/') + '-cdn-cache'
    if os.path.isdir(cache) and not os.path.lexists(new_cache):
        os.symlink(os.path.abspath(cache), new_cache)
    for f in files:
        out = []
        for seg in SPLIT.split(open(f, encoding='utf-8').read()):
            if not seg.startswith(('<style', '<script')):
                seg = ATTR.sub(attr, TEXT.sub(node, seg))
                for pat, rep in IDS:  # links to chats and artifacts
                    seg = pat.sub(rep, seg)
            out.append(seg)
        open(os.path.join(dst, os.path.basename(f)), 'w', encoding='utf-8').write(''.join(out))
    # the page-copy metadata: chat and project ids out of the URL, the title through the same map
    for f in glob.glob(src + '/*.json'):
        meta = json.loads(IDS[0][0].sub(IDS[0][1], open(f, encoding='utf-8').read()))
        if 'title' in meta:
            meta['title'] = subst(meta['title'])
        open(os.path.join(dst, os.path.basename(f)), 'w', encoding='utf-8').write(json.dumps(meta, indent=1, ensure_ascii=False))
    if map_out:
        json.dump(mapping, open(map_out, 'w'), indent=0, ensure_ascii=False)
    print('%d page copies, %d strings neutralised' % (len(files), len(mapping)))


if __name__ == '__main__':
    main()
