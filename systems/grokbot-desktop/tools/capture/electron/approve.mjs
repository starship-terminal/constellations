// Whether an agent's approval card may be accepted during a capture run. Default-deny: a card is approved
// only when it shows one of the exact commands or files the capture's own prompts ask for, inside the
// scratch folder, and nothing else that could be a command. Kept apart from product.mjs (which loads
// Playwright) so `node --test` can check it; test_approve.py runs that from `make test`.
//
// Every line of the card's text must be one of:
//   - an allowed command (`ls -la`, `cat hello.txt`, ...), alone or after an allowed tool label (`Bash ls`);
//   - an allowed path: the scratch folder, or one of the run's files in it, absolute, `~/`-relative or bare;
//   - a label: a capitalised word or phrase with no path, flag, quote or shell character in it, and not a
//     tool name followed by what could be a command (`Run rm build`).
// and at least one line must be an allowed command or path. So `rm -rf ..`, `cd ~`, `ls $HOME`, `ls *`,
// `ls | sh`, a path outside the folder, or a card whose text also holds the transcript (whose prompt names
// the folder) are all denied.

const LS = ['ls', 'ls -l', 'ls -a', 'ls -A', 'ls -1', 'ls -la', 'ls -al', 'ls -lA', 'ls -Al', 'ls -lah', 'ls -alh', 'ls -F'];
const TOOLS = ['Bash', 'Shell', 'Terminal', 'Run', 'Command', 'Read', 'Write', 'Create', 'Edit', 'List', 'View', 'Open'];
// A label: starts with a capital, holds words and plain punctuation only. Flags (` -x`) and anything a shell
// or a path could use (`/ . ~ $ * ? [ ] ` | ; & < > \ = " '`) rule a line out.
const LABEL = /^[A-Z][A-Za-z0-9 ,:()!’-]{0,79}$/;
const FLAG = /(^|\s)-/;
// A tool name followed by anything but a generic noun is a command line, never a label (`Run rm build`).
const TOOLED = new RegExp(`^(${TOOLS.join('|')}) (?!(this |a )?(command|commands|tool|file|files)$)`, 'i');

// The exact lines a run may approve. `root` is the scratch folder's absolute path, `rel` the same folder
// relative to the home folder (for the `~/` form), `files` the bare file names the prompts create or read,
// `commands` any further exact commands a prompt spells out (`sleep 5; ls`). `relative: false` drops the bare
// and `./` forms, for an agent whose working folder is not known to be the scratch folder.
export function allowance({ root, rel, files = [], commands = [], relative = true }) {
  const dirs = [root, `${root}/`, `~/${rel}`, `~/${rel}/`];
  const paths = [...dirs, ...files.flatMap(f => [...(relative ? [f, `./${f}`] : []), `${root}/${f}`, `~/${rel}/${f}`])];
  const targets = [...(relative ? ['', ' .', ' ./'] : []), ...dirs.map(d => ` ${d}`)];
  const cmds = [...LS.flatMap(l => targets.map(t => l + t)), ...files.flatMap(f => paths.filter(p => p.endsWith(`/${f}`) || p === f).map(p => `cat ${p}`)), ...commands];
  return { paths: new Set(paths), commands: new Set(cmds) };
}

export function approvable(text, allow) {
  const lines = String(text || '').split('\n').map(l => l.replace(/\s+/g, ' ').trim()).filter(Boolean);
  let named = false;
  for (const line of lines) {
    const bare = TOOLS.reduce((l, t) => (l.startsWith(`${t} `) ? l.slice(t.length + 1) : l), line);
    if (allow.commands.has(bare) || allow.paths.has(bare)) { named = true; continue; }
    if (LABEL.test(line) && !FLAG.test(line) && !TOOLED.test(line)) continue;
    return false;
  }
  return named;
}
