// Whether an agent's approval card may be accepted during a capture run. Default-deny: a card is approved
// only when it shows one of the exact commands or files the capture's own prompts ask for, inside the
// scratch folder, and nothing else that could be a command. Kept apart from product.mjs (which loads
// Playwright) so `node --test` can check it; test_approve.py runs that from `make test`.
//
// Every line of the card's text must be one of:
//   - an allowed command (`ls -la`, `cat hello.txt`, ...), alone or after an allowed tool label (`Bash ls`);
//   - an allowed path: the scratch folder, or one of the run's files in it, absolute, `~/`-relative or bare;
//   - a label: plain words, every one of them from WORDS (button and heading words such as `Allow once`,
//     `Run command`, `Permission required`). Any other word, and any punctuation but an apostrophe or a
//     hyphen, rules the line out, so `Run rm build`, `Command: printenv` or `Execute whoami` deny.
// and at least one line must be an allowed command or path. So `rm -rf ..`, `cd ~`, `ls $HOME`, `ls *`,
// `ls | sh`, a path outside the folder, or a card whose text also holds the transcript (whose prompt names
// the folder) are all denied.

const LS = ['ls', 'ls -l', 'ls -a', 'ls -A', 'ls -1', 'ls -la', 'ls -al', 'ls -lA', 'ls -Al', 'ls -lah', 'ls -alh', 'ls -F'];
const TOOLS = ['Bash', 'Shell', 'Terminal', 'Run', 'Command', 'Read', 'Write', 'Create', 'Edit', 'List', 'View'];
const WORDS = new Set(`allow allowed once always approve accept deny reject skip cancel yes no run running bash shell terminal
  command commands tool tools file files read write create edit list view permission permissions required request requested
  wants want to the a an this that in on of for folder directory session agent ask again don't do not and or proceed
  continue action needed approval`.split(/\s+/).filter(Boolean));
const LABEL = /^[A-Za-z'’-]+( [A-Za-z'’-]+)*$/;
const label = line => LABEL.test(line) && line.split(' ').every(w => WORDS.has(w.toLowerCase().replace(/’/g, "'")));

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
    if (label(line)) continue;
    return false;
  }
  return named;
}

// The card is read from the approval button outwards (`ancestors(button)`: each wider container's text, nearest
// first). The first container that names an allowed command or path must pass, and so must the next wider one
// that holds more text, so a narrow section showing only the path cannot hide the command beside it. A wider
// container that reaches the transcript fails, which denies: a refusal only costs the approval.
export function approvableCard(texts, allow) {
  const seen = (texts || []).map(t => String(t || '').trim()).filter((t, i, a) => t && t !== a[i - 1]);
  const first = seen.findIndex(t => approvable(t, allow));
  if (first < 0) return false;
  return first + 1 >= seen.length || approvable(seen[first + 1], allow);
}

// Runs in the page: the innerText of the button's ancestors, nearest first, up to `depth` levels.
export const ancestors = (button, depth = 8) => {
  const out = [];
  for (let e = button.parentElement; e && out.length < depth; e = e.parentElement) out.push(e.innerText);
  return out;
};
