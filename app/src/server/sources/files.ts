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
export async function readText(rel: string): Promise<string | null> {
  const root = repoRoot();
  const parts = rel.split("/");
  const packagePath =
    ["systems", "refero"].includes(parts[0]) && parts.length > 2;
  const file = await boundedFile(
    packagePath
      ? path.join(/* turbopackIgnore: true */ root, parts[0], parts[1])
      : root,
    packagePath ? parts.slice(2).join("/") : rel,
  );
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
export async function resolveMedia(parts: string[]): Promise<string | null> {
  if (
    !parts.length ||
    parts.some(
      (p) =>
        !p || p === ".." || p === "." || p.includes("/") || p.includes("\\"),
    )
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
