import { getReference } from "@/server/sources";
import {
  listPackageDocuments,
  readPackageDocument,
} from "@/server/sources/files";
import {
  colorsAsHex,
  hasUnresolved,
  tokenLeaves,
  tokenResolver,
  type TokenLeaf,
} from "@/server/sources/tokens";
import { parseJson, pyJsonStringify } from "@/server/sources/pyjson";
import type { LibraryDetail } from "@/contracts/library";

export async function allowedReference(
  referenceId: string,
  excluded: Set<string>,
): Promise<LibraryDetail> {
  if (excluded.has(referenceId))
    throw new Error("This reference was excluded by the user.");
  const reference = await getReference(referenceId);
  if (!reference) throw new Error("Reference not found.");
  return reference;
}
export async function packageDocuments(
  referenceId: string,
  excluded: Set<string>,
  offset = 0,
) {
  const reference = await allowedReference(referenceId, excluded);
  if (reference.source !== "systems")
    throw new Error(
      "Package documents are available for measured systems only.",
    );
  const documents = await listPackageDocuments(referenceId);
  return {
    kind: "package-documents",
    referenceId,
    documents: documents.slice(offset, offset + 60),
    offset,
    total: documents.length,
    truncated: offset + 60 < documents.length,
  };
}
export async function packageDocument(
  referenceId: string,
  relativePath: string,
  offset: number,
  excluded: Set<string>,
) {
  const reference = await allowedReference(referenceId, excluded);
  if (reference.source !== "systems")
    throw new Error(
      "Package documents are available for measured systems only.",
    );
  const document = await readPackageDocument(referenceId, relativePath);
  if (!document)
    throw new Error(
      "This document is unavailable or outside the package's readable files.",
    );
  return {
    kind: "package-document",
    referenceId,
    path: document.path,
    url: document.url,
    text: document.text.slice(offset, offset + 24000),
    offset,
    totalCharacters: document.text.length,
    truncated: offset + 24000 < document.text.length,
  };
}
type Raw = Record<string, any>;
export async function packageTokens(
  referenceId: string,
  group: string | undefined,
  offset: number,
  excluded: Set<string>,
) {
  const reference = await allowedReference(referenceId, excluded);
  if (reference.source !== "systems")
    throw new Error(
      "Use the recorded interpreted values in inspectReference for Refero styles.",
    );
  const document = await readPackageDocument(referenceId, "tokens.json");
  if (!document)
    throw new Error("No readable tokens.json exists for this package.");
  const tokens = parseJson(document.text) as Raw;
  const all = tokenLeaves(tokens),
    resolver = tokenResolver(all);
  // Theme sets the catalog names. A `core` token whose alias only resolves
  // inside a theme (Duolingo's lip shadows) gets a value per theme, as
  // `catalog.py export` gives it.
  const themeSets = reference.themes.filter(
    (theme) => theme !== "core" && Object.hasOwn(tokens, theme),
  );
  const resolveToken = (token: TokenLeaf): Raw => {
    const base = resolver.final(token.name);
    if (!hasUnresolved(base)) return { value: colorsAsHex(base) };
    if (token.name.split(".")[0] === "core" && themeSets.length) {
      const themes = Object.fromEntries(
        themeSets.map((theme) => [
          theme,
          colorsAsHex(resolver.final(token.name, theme)),
        ]),
      );
      if (!Object.values(themes).some(hasUnresolved))
        return { value: token.value, themes };
    }
    return { value: token.value, unresolved: true };
  };
  const groups = Object.keys(tokens).filter((key) => !key.startsWith("$"));
  if (!group)
    return {
      kind: "package-tokens",
      referenceId,
      groups: groups.map((name) => ({
        name,
        count: all.filter(
          (token) => token.name === name || token.name.startsWith(`${name}.`),
        ).length,
      })),
      note: "Choose any group or nested dotted token path. Values preserve their recorded evidence.",
      text: undefined,
      tokens: undefined,
    };
  if (
    !all.some(
      (token) => token.name === group || token.name.startsWith(`${group}.`),
    )
  )
    throw new Error("Token group not found. List the available groups first.");
  const selected = all.filter(
    (token) => token.name === group || token.name.startsWith(`${group}.`),
  );
  const page: Raw[] = [];
  let characters = 0;
  for (const token of selected.slice(offset, offset + 100)) {
    const { extensions, ...leaf } = token;
    const resolved = {
      ...leaf,
      evidence: extensions,
      rawValue: token.value,
      ...resolveToken(token),
    };
    const size = pyJsonStringify(resolved).length;
    if (characters + size > 24000) {
      if (!page.length)
        page.push({
          name: token.name,
          note: "This token exceeds the response limit. Read tokens.json in character pages for its complete value.",
        });
      break;
    }
    page.push(resolved);
    characters += size;
  }
  const result = {
    kind: "package-tokens",
    referenceId,
    group,
    tokens: page,
    offset,
    total: selected.length,
    truncated: offset + page.length < selected.length,
    nextOffset:
      offset + page.length < selected.length ? offset + page.length : null,
  };
  // Saved conversations and the stream are plain JSON, where 1.0 is 1. The
  // page's Python-style text travels with it so a replay still shows the
  // model 1.0.
  return { ...result, text: pyJsonStringify(result) };
}
export async function handoffPrompt(
  referenceId: string,
  appDescription: string,
  excluded: Set<string>,
) {
  const reference = await allowedReference(referenceId, excluded);
  const sourcePath = `${reference.source}/${reference.slug}`;
  const measured = reference.source === "systems";
  const prompt =
    `Use the ${reference.name} reference from my private Constellations library${appDescription ? ` for ${appDescription}` : ""}.\n\n` +
    (measured
      ? `Read ${sourcePath}/README.md in full first, including capture limits and Health. Take values from ${sourcePath}/tokens.json and preserve their per-value evidence labels. Resolve aliases and use the recorded theme groups. Read components.md and patterns.md when available. Use screenshots and component crops for layout and proportion only. ${sourcePath}/style-guide.html renders the recorded tokens.\n\n`
      : `Read ${sourcePath}/DESIGN.md and design-system.json. This Refero reference contains third-party interpreted values, not measurements. Treat it as inspiration and verify every value against a measured package or the target app's own design system.\n\n`) +
    `Borrow structure and proportions. Do not copy the product's logo, icons, illustrations, proprietary fonts or brand colours into shipped work. Follow docs/RIGHTS.md and docs/EVIDENCE.md. Name the reference, token paths, evidence limits and any adaptations in your summary.\n\nLibrary reference: /styles/${reference.source}/${reference.slug}`;
  return {
    kind: "handoff-prompt",
    referenceId,
    title: `Apply ${reference.name}`,
    prompt,
  };
}
