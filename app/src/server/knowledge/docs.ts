import { promises as fs } from "node:fs";
import path from "node:path";
// The anchor rule lives in one place; markdown-heading.ts has no client-only code.
import { headingId } from "@/features/markdown-heading";
import { boundedFile, contained, repoRoot } from "@/server/sources/files";

export interface LibraryDocument {
  slug: string;
  title: string;
  excerpt: string;
  text: string;
}
export const stripFrontmatter = (text: string) =>
  text.replace(/^---\s*\n[\s\S]*?\n---\s*\n/, "");
const plain = (text: string) =>
  text
    .replace(/\[([^\]]+)\]\([^)]*\)/g, "$1")
    .replace(/[*_`]/g, "")
    .trim();
async function documentRoot(): Promise<string | null> {
  try {
    const repo = await fs.realpath(/* turbopackIgnore: true */ repoRoot());
    const docs = await fs.realpath(
      /* turbopackIgnore: true */ path.join(repo, "docs"),
    );
    return contained(repo, docs) ? docs : null;
  } catch {
    return null;
  }
}
export async function readLibraryDocument(
  slug: string,
): Promise<LibraryDocument | null> {
  if (
    !slug.split("/").every((part) => /^[A-Za-z0-9][A-Za-z0-9_-]*$/.test(part))
  )
    return null;
  const root = await documentRoot();
  const file = root ? await boundedFile(root, `${slug}.md`) : null;
  if (
    !file ||
    (await fs.stat(/* turbopackIgnore: true */ file)).size > 2 * 1024 * 1024
  )
    return null;
  const source = await fs.readFile(/* turbopackIgnore: true */ file, "utf8");
  if (
    !source ||
    source.includes("\0") ||
    source.startsWith("version https://git-lfs.github.com/spec/v1")
  )
    return null;
  const text = stripFrontmatter(source);
  const title = plain(text.match(/^#\s+(.+)$/m)?.[1] || slug);
  const excerpt = plain(
    text
      .split(/\n\s*\n/)
      .find(
        (block) => !/^(#|\||[-*]|<|!|\d+\.)/.test(block.trim()) && block.trim(),
      ) || "",
  ).slice(0, 220);
  return { slug, title, excerpt, text };
}
export async function listLibraryDocuments(): Promise<LibraryDocument[]> {
  const root = await documentRoot();
  if (!root) return [];
  const entries = await fs
    .readdir(/* turbopackIgnore: true */ root)
    .catch(() => [] as string[]);
  const names = entries.filter((name) => name.endsWith(".md")).sort();
  const docs = await Promise.all(
    names.map(async (name) =>
      (await boundedFile(root, name))
        ? readLibraryDocument(name.slice(0, -3))
        : null,
    ),
  );
  return docs
    .filter((doc): doc is LibraryDocument => !!doc)
    .sort((a, b) =>
      a.slug === "index"
        ? -1
        : b.slug === "index"
          ? 1
          : a.title.localeCompare(b.title),
    );
}
/** Resolve recorded repository links without allowing a document to link outside its source tree. */
export function documentHref(base: string, href: string): string | null {
  if (/^https?:\/\//i.test(href) || /^mailto:/i.test(href)) return href;
  if (href.startsWith("#")) return href;
  if (/^[a-z][a-z\d+.-]*:/i.test(href) || href.startsWith("//")) return null;
  const hashAt = href.indexOf("#");
  const file = hashAt >= 0 ? href.slice(0, hashAt) : href;
  const hash = hashAt >= 0 ? href.slice(hashAt) : "";
  const resolved = path.posix.normalize(
    file.startsWith("/")
      ? file.slice(1)
      : path.posix.join(path.posix.dirname(base), file),
  );
  if (resolved.startsWith("../") || resolved === "..") return null;
  const doc = /^docs\/(.+)\.md$/i.exec(resolved);
  if (doc) return `/docs/${doc[1]}${hash}`;
  if (/^systems\/[a-z0-9-]+\/.+\.(png|jpe?g|webp|gif|svg)$/i.test(resolved))
    return `/media/${resolved}${hash}`;
  const pkg = /^systems\/([a-z0-9-]+)(?:\/(.*))?$/i.exec(resolved);
  if (pkg)
    return pkg[2]
      ? `/library/${pkg[1]}?tab=files&file=${encodeURIComponent(pkg[2])}${hash}`
      : `/styles/systems/${pkg[1]}${hash}`;
  if (resolved.startsWith("docs/assets/")) return `/media/${resolved}${hash}`;
  if (resolved === "README.md") return `/docs/index${hash}`;
  if (resolved === "scorecard" || resolved.startsWith("scorecard/"))
    return "/scorecard";
  // The private repo has scripts and source links that have no browser reader.
  return null;
}
export { headingId };
