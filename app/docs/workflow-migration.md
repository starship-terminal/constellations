# Knowledge and research workflow migration

The new app keeps the durable Studio research and collection model while restoring the old library's knowledge workflows. Canonical package, rubric, audit and library-doc files remain unchanged.

## Restored workflows

| Workflow                                                | New implementation                                                              | Canonical input                                                                    |
| ------------------------------------------------------- | ------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| Docs index and document sidebar                         | `src/app/docs/`, `src/features/knowledge/docs.tsx`                              | Top-level `docs/*.md`                                                              |
| Docs reader, heading anchors, tables and relative links | `src/features/knowledge/markdown.tsx`, `src/server/knowledge/docs.ts`           | Same Markdown sources; links adapt to the new document/package reader              |
| Scorecard overview and criterion heatmap                | `src/app/scorecard/page.tsx`, `src/features/knowledge/scorecard.tsx`            | `scorecard/criteria.json`, dated audit snapshots                                   |
| Individual package audit and evidence                   | `src/app/scorecard/[slug]/page.tsx`                                             | Latest audit, platform wording, capture/review dates and criterion evidence        |
| Rubric and audit history                                | `src/app/scorecard/criteria/`, `src/app/scorecard/changelog/`                   | Every platform's wording and every audit snapshot                                  |
| Complete package guidance in research                   | `readPackageDocument`, `listPackageDocuments` in `src/server/research/agent.ts` | Bounded package document readers shared with the Files UI                          |
| Any token group in research                             | `getPackageTokens`, `src/server/research/evidence.ts`                           | Original `tokens.json`, raw values/evidence plus resolved aliases                  |
| Selected visual evidence                                | `listReferenceMedia`, `viewReferenceMedia`                                      | Normalized reference media; only hydrated local raster images enter model requests |
| Coding-agent handoff                                    | `handoffPrompt` plus research result copy action                                | Chosen reference's canonical paths and evidence/rights guidance                    |

The scorecard reader reuses the old app's typed audit calculations, without its UI or CSS. Repository discovery now uses the new app's runtime `repoRoot()` so a mounted library works from `app/` or another working directory. Docs rendering uses the new Markdown renderer, shared Studio tokens and neutral typography.

Scorecard completion counts applicable grades only. The weakest-evidence links rank up to five criteria by the share of applicable packages that do not fully meet them, show the actual numerator and denominator, and omit criteria with no applicability. Optional not-applicable grades do not lower completion or create false gaps.

## Behavior and limits

Research retains durable messages, streaming, provider selection, pin/exclude controls, retry/regenerate and transcript export. New evidence tools respect excluded references both during execution and when older tool parts enter model history. Documents return at most 24,000 characters per page, tokens at most 100 entries and 24,000 characters, and document/media lists at most 60 entries per page. The existing six-step, 120-second research budget remains in place.

Alias resolution preserves source values and evidence. It supports explicit set-qualified references, same-set aliases, core aliases, arrays and composite values. Cyclic or unknown aliases remain visible instead of becoming invented values. Package-specific interpretation and evidence limits still govern how a value may be used.

Image selection accepts a recorded media ID rather than an arbitrary URL. Remote images, videos, SVG boards and providers without tool-image support stay explicitly text-only for the model. The UI still lets the user open recorded media. Full SVG board source can be read through package documents. A partial document read identifies its character offset and whether more content remains.

Docs reject traversal and symlink escapes, render Markdown without executing HTML/scripts, and map canonical docs/package links to the new app. Repository scripts and other code files without a browser reader appear as plain text links; the migration does not expose arbitrary repository files. Package HTML rendering and file access use the separately implemented package reader's bounds and sandbox.

## Deliberate exclusions and implementation choices

The user explicitly excluded auth/accounts, billing/pricing, and MCP plugin/onboarding. None of those workflows is part of this migration. Model-provider configuration remains part of research and is separate from account onboarding.

The old chat drawer, request names, in-memory chat transcript, raw tool-name log and browser-stored provider credentials are implementation details. The new app keeps its persistent research pages and server-managed credentials. The old home dashboard's exact visual arrangement does not need reproduction; the underlying library and audit information remains available through browsing and scorecard workflows.

Theme/sidebar preferences, provider connection/model discovery, individual saved media and navigation are implemented by the coordinating workstream. Collections supplement saved media: a saved reference and an individual saved screenshot have different granularity. Gallery, measured-package files and Refero details are implemented by their owning workstreams.

## Verification

Focused tests cover mounted library paths, document traversal and symlink escapes, heading/link mapping, platform-specific rubric wording and audit history, full package-document pagination, token aliases and composites, chosen media selection, text-only image behavior, and reference exclusions. Existing research streaming tests continue to check durable raw evidence and provider image transport. The coordinating workstream performs browser review and the production build.

No knowledge/research migration scope remains intentionally unfinished. Canonical files or LFS media absent from a particular checkout still produce an unavailable state; the app does not fabricate evidence or download arbitrary remote media into the model.
