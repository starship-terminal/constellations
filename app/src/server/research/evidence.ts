import { getReference } from "@/server/sources";
import {
  listPackageDocuments,
  readPackageDocument,
} from "@/server/sources/files";
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
// A group may legitimately contain a token named "value". Legacy Tokens
// Studio tokens use an unprefixed value field, so distinguish their payload
// from a nested token tree before treating the enclosing object as a leaf.
function containsToken(node: unknown): boolean {
  if (!node || typeof node !== "object" || Array.isArray(node)) return false;
  const obj = node as Raw;
  if (Object.hasOwn(obj, "$value")) return true;
  if (
    Object.hasOwn(obj, "value") &&
    (typeof obj.type === "string" ||
      !obj.value ||
      typeof obj.value !== "object" ||
      Array.isArray(obj.value))
  )
    return true;
  return Object.values(obj).some(containsToken);
}
function tokenLeaves(node: unknown, prefix = "", out: Raw[] = []) {
  if (!node || typeof node !== "object" || Array.isArray(node)) return out;
  const obj = node as Raw;
  const dtcg = Object.hasOwn(obj, "$value");
  const legacy =
    Object.hasOwn(obj, "value") &&
    (typeof obj.type === "string" || !containsToken(obj.value));
  if (dtcg || legacy)
    out.push({
      name: prefix,
      value: dtcg ? obj.$value : obj.value,
      type: obj.$type ?? obj.type,
      description: obj.$description ?? obj.description,
      evidence: obj.$extensions ?? null,
    });
  else
    for (const [key, value] of Object.entries(obj))
      if (!key.startsWith("$"))
        tokenLeaves(value, prefix ? `${prefix}.${key}` : key, out);
  return out;
}
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
  const tokens = JSON.parse(document.text) as Raw;
  const all = tokenLeaves(tokens),
    byName = new Map(all.map((token) => [token.name, token.value]));
  const aliasPath = (alias: string, context: string): string | null => {
    const group = context.split(".")[0];
    return (
      [alias, `${group}.${alias}`, `core.${alias}`].find((candidate) =>
        byName.has(candidate),
      ) || null
    );
  };
  const resolve = (
    value: unknown,
    seen: Set<string>,
    context: string,
  ): unknown => {
    if (typeof value === "string") {
      const exact = /^\{([^{}]+)\}$/.exec(value);
      const target = exact ? aliasPath(exact[1], context) : null;
      if (target && !seen.has(target))
        return resolve(byName.get(target), new Set([...seen, target]), target);
      return value.replace(/\{([^{}]+)\}/g, (match, alias: string) => {
        const name = aliasPath(alias, context);
        if (!name || seen.has(name)) return match;
        const resolved = resolve(
          byName.get(name),
          new Set([...seen, name]),
          name,
        );
        return typeof resolved === "object"
          ? JSON.stringify(resolved)
          : String(resolved);
      });
    }
    if (Array.isArray(value))
      return value.map((v) => resolve(v, seen, context));
    if (value && typeof value === "object")
      return Object.fromEntries(
        Object.entries(value).map(([key, v]) => [
          key,
          resolve(v, seen, context),
        ]),
      );
    return value;
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
    const resolved = {
      ...token,
      rawValue: token.value,
      value: resolve(token.value, new Set([token.name]), token.name),
    };
    const size = JSON.stringify(resolved).length;
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
  return {
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
    `Use the ${reference.name} reference from my private design-systems library${appDescription ? ` for ${appDescription}` : ""}.\n\n` +
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
