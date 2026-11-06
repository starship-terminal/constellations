// Client-safe URL helpers — no node imports, safe to pull into "use client"
// modules. Server-only data access lives in catalog.ts/refero.ts.
export const mediaUrl = (repoRelPath: string) =>
  "/media/" + repoRelPath.split("/").map(encodeURIComponent).join("/");
