import { promises as fs, existsSync } from "node:fs";
import path from "node:path";

// Repository and media paths belong to runtime-mounted private data.
// Match Next's own runtime-path convention: prevent Turbopack from tracing these trees.
export function repoRoot(): string {
  if (process.env.DESIGN_SYSTEMS_REPO)
    return path.resolve(
      /* turbopackIgnore: true */ process.env.DESIGN_SYSTEMS_REPO,
    );
  let dir = process.cwd();
  for (let n = 0; n < 4; n++, dir = path.dirname(dir))
    if (existsSync(path.join(/* turbopackIgnore: true */ dir, "catalog.json")))
      return dir;
  return process.cwd();
}
export function mediaRoot(): string {
  return path.resolve(
    /* turbopackIgnore: true */
    process.env.DESIGN_SYSTEMS_MEDIA ||
      path.join(
        /* turbopackIgnore: true */ process.env.HOME || "",
        "services/design-systems/media/refero",
      ),
  );
}
export function contained(root: string, target: string): boolean {
  const rel = path.relative(root, target);
  return (
    rel === "" ||
    (!rel.startsWith(`..${path.sep}`) && rel !== ".." && !path.isAbsolute(rel))
  );
}
// Check both lexical and real paths. A symlink in an allowed tree cannot expose another tree.
export async function boundedFile(
  root: string,
  rel: string,
): Promise<string | null> {
  if (
    !rel ||
    rel.includes("\0") ||
    rel.includes("\\") ||
    rel.split("/").some((x) => x === "..") ||
    path.isAbsolute(rel)
  )
    return null;
  const target = path.resolve(/* turbopackIgnore: true */ root, rel);
  if (!contained(path.resolve(/* turbopackIgnore: true */ root), target))
    return null;
  try {
    const [realRoot, realTarget] = await Promise.all([
      fs.realpath(/* turbopackIgnore: true */ root),
      fs.realpath(/* turbopackIgnore: true */ target),
    ]);
    return contained(realRoot, realTarget) &&
      (await fs.stat(/* turbopackIgnore: true */ realTarget)).isFile()
      ? realTarget
      : null;
  } catch {
    return null;
  }
}
// A package file is bounded by its own package folder, anything else by the
// repository root.
function repoFile(rel: string): Promise<string | null> {
  const root = repoRoot();
  const parts = rel.split("/");
  const packagePath =
    ["systems", "refero"].includes(parts[0]) && parts.length > 2;
  return boundedFile(
    packagePath
      ? path.join(/* turbopackIgnore: true */ root, parts[0], parts[1])
      : root,
    packagePath ? parts.slice(2).join("/") : rel,
  );
}
/** Whether readText could find the file, without reading it. */
export async function hasFile(rel: string): Promise<boolean> {
  return (await repoFile(rel)) !== null;
}
export async function readText(rel: string): Promise<string | null> {
  const file = await repoFile(rel);
  if (!file) return null;
  try {
    const text = await fs.readFile(/* turbopackIgnore: true */ file, "utf8");
    return text.startsWith("version https://git-lfs.github.com/spec/v1")
      ? null
      : text;
  } catch {
    return null;
  }
}
export async function readJson<T>(rel: string): Promise<T | null> {
  const text = await readText(rel);
  if (!text) return null;
  try {
    return JSON.parse(text) as T;
  } catch {
    return null;
  }
}
export function remoteUrl(value: unknown): string | null {
  if (typeof value !== "string") return null;
  try {
    const u = new URL(value);
    return ["https:", "http:"].includes(u.protocol) &&
      !u.username &&
      !u.password
      ? u.href
      : null;
  } catch {
    return null;
  }
}
const MIME: Record<string, string> = {
  ".jpg": "image/jpeg",
  ".jpeg": "image/jpeg",
  ".png": "image/png",
  ".webp": "image/webp",
  ".gif": "image/gif",
  ".avif": "image/avif",
  ".svg": "image/svg+xml",
  ".ico": "image/x-icon",
  ".mp4": "video/mp4",
  ".webm": "video/webm",
  ".mov": "video/quicktime",
};
export function mediaMime(file: string): string | null {
  return MIME[path.extname(file).toLowerCase()] || null;
}
export async function usableMedia(file: string | null): Promise<boolean> {
  if (!file || !mediaMime(file)) return false;
  try {
    const handle = await fs.open(/* turbopackIgnore: true */ file, "r");
    try {
      const header = Buffer.alloc(100);
      const { bytesRead } = await handle.read(header, 0, 100, 0);
      return (
        bytesRead > 0 &&
        !header
          .toString("utf8")
          .startsWith("version https://git-lfs.github.com/spec/v1")
      );
    } finally {
      await handle.close();
    }
  } catch {
    return false;
  }
}
// Raw readings, local fonts and tooling output stay private on every surface.
const PRIVATE_PACKAGE_DIRS = new Set([
  "raw",
  "fonts",
  "node_modules",
  "__pycache__",
]);
export async function resolveMedia(parts: string[]): Promise<string | null> {
  if (
    !parts.length ||
    parts.some(
      (p) =>
        !p ||
        p.startsWith(".") ||
        p.includes("/") ||
        p.includes("\\") ||
        p.includes("\0"),
    ) ||
    (parts[0] === "systems" &&
      parts.slice(2).some((p) => PRIVATE_PACKAGE_DIRS.has(p)))
  )
    return null;
  let root = repoRoot(),
    rel = parts.join("/");
  if (parts[0] === "refero-media") {
    root = mediaRoot();
    rel = parts.slice(1).join("/");
  } else if (parts[0] === "data" && parts[1] === "thumbs") rel = `web/${rel}`;
  else if (
    parts[0] !== "systems" &&
    !(parts[0] === "docs" && parts[1] === "assets")
  )
    return null;
  const file = await boundedFile(root, rel);
  return (await usableMedia(file)) ? file : null;
}
export async function imageUrl(value: unknown): Promise<string | null> {
  if (typeof value !== "string") return null;
  const remote = remoteUrl(value);
  if (remote) return remote;
  const rel = value.replace(/^\/?media\//, "").replace(/^\//, "");
  return (await resolveMedia(rel.split("/")))
    ? `/media/${rel.split("/").map(encodeURIComponent).join("/")}`
    : null;
}
export async function referoMedia(
  local: string | null,
  remote: unknown,
): Promise<string | null> {
  if (local) {
    const available = await imageUrl(local);
    if (available) return available;
    const base = process.env.DESIGN_SYSTEMS_MEDIA_BASE;
    if (base) {
      const url = remoteUrl(
        `${base.replace(/\/$/, "")}/${local.replace(/^\//, "")}`,
      );
      if (url) return url;
    }
  }
  return remoteUrl(remote);
}

/** Vision accepts only bounded, hydrated local raster files, never arbitrary URLs. */
export async function readLocalImage(
  url: string,
): Promise<{ data: Uint8Array; mediaType: string } | null> {
  if (!url.startsWith("/media/")) return null;
  let parts: string[];
  try {
    parts = url.slice("/media/".length).split("/").map(decodeURIComponent);
  } catch {
    return null;
  }
  const file = await resolveMedia(parts);
  if (!file) return null;
  const mediaType = mediaMime(file)!;
  if (
    !["image/jpeg", "image/png", "image/webp", "image/gif"].includes(mediaType)
  )
    return null;
  if ((await fs.stat(/* turbopackIgnore: true */ file)).size > 5 * 1024 * 1024)
    return null;
  return {
    data: await fs.readFile(/* turbopackIgnore: true */ file),
    mediaType,
  };
}

// Package documents are a separate bounded surface from binary media. Never
// allow arbitrary repository reads or ignored/private capture directories.
const DOCUMENT_EXT = new Set([
  ".md",
  ".txt",
  ".json",
  ".css",
  ".html",
  ".js",
  ".mjs",
  ".ts",
  ".tsx",
  ".jsx",
  ".yml",
  ".yaml",
  ".tsv",
  ".csv",
  ".svg",
  ".xml",
  ".py",
  ".toml",
  ".sh",
  ".map",
]);
const MAX_DOCUMENT_BYTES = 4 * 1024 * 1024;
export function packageDocumentUrl(slug: string, relative: string): string {
  return `/api/packages/${encodeURIComponent(slug)}/files?path=${encodeURIComponent(relative)}`;
}
function readablePackagePath(relative: string): boolean {
  const parts = relative.split("/");
  return (
    parts.every(
      (p) =>
        p &&
        !p.startsWith(".") &&
        !p.includes("\\") &&
        !p.includes("\0") &&
        !PRIVATE_PACKAGE_DIRS.has(p),
    ) && DOCUMENT_EXT.has(path.extname(relative).toLowerCase())
  );
}
async function packageDirectory(
  id: string,
): Promise<{ slug: string; dir: string } | null> {
  const match = /^systems:([a-z0-9][a-z0-9-]*)$/i.exec(id);
  if (!match) return null;
  const catalog = await readJson<{ systems?: { slug: string }[] }>(
    "catalog.json",
  );
  if (
    !Array.isArray(catalog?.systems) ||
    !catalog.systems.some((s) => s.slug === match[1])
  )
    return null;
  const dir = path.join(
    /* turbopackIgnore: true */ repoRoot(),
    "systems",
    match[1],
  );
  try {
    const [realRepo, realDir] = await Promise.all([
      fs.realpath(/* turbopackIgnore: true */ repoRoot()),
      fs.realpath(/* turbopackIgnore: true */ dir),
    ]);
    return contained(realRepo, realDir)
      ? { slug: match[1], dir: realDir }
      : null;
  } catch {
    return null;
  }
}
export async function listPackageDocuments(
  id: string,
): Promise<import("@/contracts/library").PackageDocument[]> {
  const pkg = await packageDirectory(id);
  if (!pkg) return [];
  const out: import("@/contracts/library").PackageDocument[] = [];
  async function walk(relative: string, depth: number): Promise<void> {
    if (depth > 12 || out.length > 20_000) return;
    const entries = (
      await fs.readdir(
        path.join(/* turbopackIgnore: true */ pkg!.dir, relative),
        { withFileTypes: true },
      )
    ).sort((a, b) => a.name.localeCompare(b.name));
    for (const entry of entries) {
      if (entry.name.startsWith(".") || PRIVATE_PACKAGE_DIRS.has(entry.name))
        continue;
      const rel = relative ? `${relative}/${entry.name}` : entry.name;
      if (entry.isDirectory()) await walk(rel, depth + 1);
      else if (entry.isFile() && readablePackagePath(rel)) {
        const file = await boundedFile(pkg!.dir, rel);
        if (!file) continue;
        const stat = await fs.stat(/* turbopackIgnore: true */ file);
        if (stat.size > MAX_DOCUMENT_BYTES) continue;
        out.push({
          path: rel,
          name: entry.name,
          group: relative.split("/")[0] || "",
          size: stat.size,
          url: packageDocumentUrl(pkg!.slug, rel),
        });
      }
    }
  }
  await walk("", 0);
  return out;
}
export async function readPackageDocument(
  id: string,
  relative: string,
): Promise<import("@/contracts/library").PackageDocumentContent | null> {
  if (!readablePackagePath(relative)) return null;
  const pkg = await packageDirectory(id);
  if (!pkg) return null;
  const file = await boundedFile(pkg.dir, relative);
  if (!file) return null;
  const stat = await fs.stat(/* turbopackIgnore: true */ file);
  if (stat.size > MAX_DOCUMENT_BYTES) return null;
  const text = await fs.readFile(/* turbopackIgnore: true */ file, "utf8");
  if (
    text.includes("\0") ||
    text.includes("\uFFFD") ||
    text.startsWith("version https://git-lfs.github.com/spec/v1")
  )
    return null;
  const ext = path.extname(relative).toLowerCase();
  return {
    path: relative,
    name: path.basename(relative),
    group: relative.includes("/") ? relative.split("/")[0] : "",
    size: stat.size,
    url: packageDocumentUrl(pkg.slug, relative),
    text,
    format:
      ext === ".md"
        ? "markdown"
        : ext === ".json"
          ? "json"
          : ext === ".html"
            ? "html"
            : "text",
  };
}
// HTML runs only in an opaque sandbox. Resource reads still stay inside the
// named package; raw captures and hidden paths remain inaccessible.
export async function readPackageGuide(
  id: string,
  relative: string,
): Promise<{ body: Uint8Array; mime: string } | null> {
  const parts = relative.split("/");
  if (
    parts.some(
      (p) =>
        !p ||
        p.startsWith(".") ||
        p.includes("\\") ||
        p.includes("\0") ||
        ["raw", "node_modules", "__pycache__"].includes(p),
    )
  )
    return null;
  const ext = path.extname(relative).toLowerCase();
  // A guide may link its README, import instructions, component guidance or
  // tokens. Serve these as text inside the sandbox instead of nesting the app
  // in an opaque frame or opening a broken guide-resource URL.
  if (
    ext !== ".html" &&
    ext !== ".css" &&
    !mediaMime(relative) &&
    readablePackagePath(relative)
  ) {
    const document = await readPackageDocument(id, relative);
    if (document)
      return {
        body: new TextEncoder().encode(document.text),
        mime: "text/plain; charset=utf-8",
      };
  }
  const mime =
    ext === ".html"
      ? "text/html; charset=utf-8"
      : ext === ".css"
        ? "text/css; charset=utf-8"
        : ext === ".woff2"
          ? "font/woff2"
          : ext === ".woff"
            ? "font/woff"
            : mediaMime(relative);
  if (!mime || mime.startsWith("video/")) return null;
  const pkg = await packageDirectory(id);
  if (!pkg) return null;
  const file = await boundedFile(pkg.dir, relative);
  if (
    !file ||
    (await fs.stat(/* turbopackIgnore: true */ file)).size > 16 * 1024 * 1024
  )
    return null;
  const body = await fs.readFile(/* turbopackIgnore: true */ file);
  if (
    body
      .subarray(0, 100)
      .toString()
      .startsWith("version https://git-lfs.github.com/spec/v1")
  )
    return null;
  return { body, mime };
}
