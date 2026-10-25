#!/usr/bin/env python3
"""Capture an agent run in the scratch workspace: streaming, tool calls, any approval prompt, the result.

    python3 tools/capture/inspector/run.py <theme> <step> "<prompt>"

The owner allowed test prompts on 2026-10-25, in a fresh chat of the scratch workspace only, with
harmless prompts. This sends the prompt from the composer, then every INTERVAL seconds screenshots the
window and records, for the conversation pane, every text-bearing element with its box and computed style,
plus the composer's send/stop button. It never approves anything: when a prompt with approve/deny buttons
appears it records the frame, stops, and prints the buttons, so a person decides (only actions inside the
scratch folder may be approved). Frames go to $RAW/<theme>/run/<step>-NN.png, readings to frames.json.
"""
import json
import os
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from shots import RAW, run_js, shoot  # noqa: E402

INTERVAL = float(os.environ.get("INTERVAL", "2"))
TIMEOUT = float(os.environ.get("TIMEOUT", "240"))

READ = r"""
const pane = (() => { const c = P.composer(); let p = c; while (p && p.getBoundingClientRect().height < 500) p = p.parentElement; return p || document.body; })();
const els = [];
for (const e of pane.querySelectorAll('*')) {
  if (!C.vis(e) || /^(path|svg|g|circle|rect|line|polyline)$/i.test(e.tagName)) continue;
  const own = [...e.childNodes].filter(n => n.nodeType === 3).map(n => n.textContent.trim()).join(' ').trim();
  const cs = getComputedStyle(e);
  const deco = cs.backgroundColor !== 'rgba(0, 0, 0, 0)' || parseFloat(cs.borderTopWidth) > 0 || e.tagName === 'BUTTON' || e.getAttribute('role');
  if (!own && !deco) continue;
  els.push({ tag: e.tagName.toLowerCase(), role: e.getAttribute('role'), aria: e.getAttribute('aria-label'), text: own.slice(0, 60),
    cls: (e.getAttribute('class') || '').slice(0, 200), data: [...e.attributes].filter(a => a.name.startsWith('data-')).map(a => a.name + '=' + a.value.slice(0, 30)).join(' '),
    box: C.box(e), style: C.style(e) });
  if (els.length > 260) break;
}
const send = P.sendButton();
const btns = C.$('button').filter(b => b.getAttribute('role') !== 'tab' && b.getBoundingClientRect().x < 1015).map(b => b.innerText.trim()).filter(t => /^(approve|allow|accept|deny|reject|always|run|yes|no)\b/i.test(t));
return { viewport: C.viewport(), send: send ? { svg: (send.querySelector('svg') || {}).getAttribute && send.querySelector('svg').getAttribute('class'), aria: send.getAttribute('aria-label'), disabled: send.disabled, style: C.style(send), box: C.box(send) } : null,
  approval: btns, els };
"""


def main():
    theme, step, prompt = sys.argv[1:4]
    out_dir = RAW / theme / "run"
    out_dir.mkdir(parents=True, exist_ok=True)
    frames_path = out_dir / "frames.json"
    frames = json.loads(frames_path.read_text()) if frames_path.exists() else {}
    for k in ([] if os.environ.get("WATCH") else [k for k in frames if k.startswith(step + "-")]):
        del frames[k]
    chat = os.environ.get("CHAT", "")
    run_js(f"await P.ready(); await P.workspace({json.dumps(chat) if chat else ''}); return 'ok';")
    send = f"""
C.type('.composer-tiptap-editor', {json.dumps(prompt)});
await C.sleep(500);
const b = P.sendButton(); if (!b || b.disabled) throw new Error('send button not ready');
C.click(b);
return 'sent';
"""
    if os.environ.get("WATCH"):
        i0 = int(os.environ["WATCH"])
    else:
        print(run_js(send)); i0 = 0
    t0, i, idle = time.time(), i0, 0
    while time.time() - t0 < TIMEOUT:
        name = f"{step}-{i:02d}"
        shoot(f"{theme}/run", name)
        data = json.loads(run_js(READ))
        data["t"] = round(time.time() - t0, 1)
        data["file"] = f"{theme}/run/{name}.png"
        frames[name] = data
        frames_path.write_text(json.dumps(frames, indent=1) + "\n")
        svg = (data.get("send") or {}).get("svg") or ""
        print(name, data["t"], svg[:60], data["approval"], len(data["els"]))
        if data["approval"]:
            print("APPROVAL PROMPT: stopping for a person to decide", data["approval"])
            return
        running = "square" in svg or "stop" in svg or "loader" in svg
        idle = 0 if running else idle + 1
        if i >= 6 and idle >= 3:
            print("done")
            return
        i += 1
        time.sleep(INTERVAL)
    print("TIMEOUT")


if __name__ == "__main__":
    main()
