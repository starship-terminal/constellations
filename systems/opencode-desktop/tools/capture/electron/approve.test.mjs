// node --test approve.test.mjs (test_approve.py runs it from `make test`).
import { test } from 'node:test';
import assert from 'node:assert/strict';
import { allowance, approvable, approvableCard, ancestors } from './approve.mjs';

const root = '/Users/someone/.design-systems/harness-scratch/demo';
const allow = allowance({ root, rel: '.design-systems/harness-scratch/demo', files: ['hello.txt'], commands: ['sleep 5; ls'] });
const ok = t => assert.equal(approvable(t, allow), true, t);
const no = t => assert.equal(approvable(t, allow), false, t);

test('approves the commands and files the prompts ask for', () => {
  ok('Bash\nls -la\nAllow\nDeny');
  ok(`Run command\nls ${root}\nAllow once\nDeny`);
  ok('Write\nhello.txt\nApprove');
  ok(`Create ${root}/hello.txt\nAccept`);
  ok('Read\ncat hello.txt\nAllow');
  ok('Bash\nsleep 5; ls\nAllow');
  ok('~/.design-systems/harness-scratch/demo\nls\nAllow');
});

test('denies escapes from the scratch folder', () => {
  no(`Bash\nrm -rf ..\n${root}\nAllow`);
  no(`Bash\nls ..\nAllow`);
  no('Bash\ncd ~\nAllow');
  no('Bash\nls ~\nAllow');
  no('Bash\nls $HOME\nAllow');
  no('Bash\nls *\nAllow');
  no('Bash\nls `pwd`\nAllow');
  no('Bash\nls | sh\nAllow');
  no('Bash\nls; rm hello.txt\nAllow');
  no('Bash\nls && rm hello.txt\nAllow');
  no(`Bash\nls ${root}-backup\nAllow`);
  no(`Write\n${root}/../other.txt\nAllow`);
  no('Write\nnotes.txt\nAllow');
});

test('denies commands dressed as labels and cards with no target', () => {
  no('Run rm build\nls\nAllow');
  no(`Command: printenv\n${root}\nAllow`);
  no(`Run: rm build\n${root}\nAllow`);
  no(`Execute whoami\n${root}\nAllow`);
  no(`Bash, printenv\n${root}\nAllow`);
  no('Bash\nrm hello\nls\nAllow');
  no('Allow\nDeny');
  no('');
  no(null);
});

test('relative: false approves only absolute forms', () => {
  const abs = allowance({ root, rel: '.design-systems/harness-scratch/demo', files: ['hello.txt'], relative: false });
  assert.equal(approvable(`Read\ncat ${root}/hello.txt\nAllow`, abs), true);
  assert.equal(approvable('Read\ncat hello.txt\nAllow', abs), false);
  assert.equal(approvable('Write\nhello.txt\nAllow', abs), false);
  assert.equal(approvable('Bash\nls\nAllow', abs), false);
});

test('denies a container that holds the transcript, whose prompt names the folder', () => {
  no(`List the files in ~/.design-systems/harness-scratch/demo on this Mac.\nBash\nrm -rf /tmp/x\nAllow`);
});

test('the next wider container must pass too, so a path-only section cannot hide the command', () => {
  const buttons = 'Allow once\nDeny';
  const pathOnly = `${root}\n${buttons}`;
  const card = `Bash\nrm -rf build\n${pathOnly}`;
  assert.equal(approvableCard([buttons, pathOnly, card], allow), false);
  assert.equal(approvableCard([buttons, pathOnly, `Bash\nls -la\n${pathOnly}`], allow), true);
  assert.equal(approvableCard([buttons, `Bash\nls\n${buttons}`], allow), true);
  assert.equal(approvableCard([buttons, buttons], allow), false);
  assert.equal(approvableCard([], allow), false);
});

test('ancestors reads each wider container, nearest first', () => {
  const node = (innerText, parentElement = null) => ({ innerText, parentElement });
  const card = node('card', node('pane', node('app')));
  const row = node('row', card);
  assert.deepEqual(ancestors({ parentElement: row }), ['row', 'card', 'pane', 'app']);
  assert.deepEqual(ancestors({ parentElement: row }, 2), ['row', 'card']);
});
