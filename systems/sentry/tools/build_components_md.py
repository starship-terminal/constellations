"""Build an evidence inventory from the reviewed screenshot manifest."""
from pathlib import Path
R=Path(__file__).resolve().parents[1]
text='# Sentry components and visible states\n\nApp screenshots are live signed-in evidence. Public images stay in a separate folder. Use tokens.json for values; images establish layout and visible states only.\n\n'
for p in sorted((R/'screenshots/app').glob('*.png')):
 text+=f'## {p.stem}\n\n![{p.stem}](screenshots/app/{p.name})\n\n[Computed readings](raw/app/{p.stem}.json) · [Capture dimensions](screenshots/app/{p.name}.capture.json)\n\n'
text+='## Gaps\n\nNo populated issue list or error stack trace existed in the selected project. No destructive action, feedback submission, trial, upload, invitation or data mutation was performed. Hover and pressed variants, validation errors, action-result toasts, mobile app and full theme parity remain uncaptured. Feedback form shadow DOM has visual evidence only. Trace attributes are a scrollable panel; captures show its top portion.\n'
(R/'components.md').write_text(text)
