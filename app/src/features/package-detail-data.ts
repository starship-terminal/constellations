import type { ReferenceMedia } from "@/contracts/library";
export function filterPackageMedia(
  items: ReferenceMedia[],
  query: string,
  tag: string,
): ReferenceMedia[] {
  const words = query.toLowerCase().trim().split(/\s+/).filter(Boolean);
  return items.filter(
    (item) =>
      (!tag || item.tags.includes(tag)) &&
      words.every((word) =>
        `${item.name} ${item.group || ""} ${item.path || ""} ${item.tags.join(" ")}`
          .toLowerCase()
          .includes(word),
      ),
  );
}
export function packageFileHref(slug: string, relative: string): string {
  return `/library/${encodeURIComponent(slug)}?tab=files&file=${encodeURIComponent(relative)}`;
}
/** decodeURIComponent that keeps a malformed escape ("50%off.md") as written instead of throwing. */
export function safeDecode(value: string): string {
  try {
    return decodeURIComponent(value);
  } catch {
    return value;
  }
}
/** Resolve captured document links without letting package-relative traversal become an arbitrary read. */
export function packageDocumentLink(
  slug: string,
  current: string,
  href: string,
  image = false,
): string | undefined {
  if (/^(https?:|mailto:)/i.test(href)) return image ? undefined : href;
  if (/^[a-z][a-z\d+.-]*:/i.test(href) || href.startsWith("//"))
    return undefined;
  if (href.startsWith("#")) return href;
  const url = new URL(
    href,
    `https://package.invalid/systems/${slug}/${current}`,
  );
  const parts = url.pathname.split("/").filter(Boolean).map(safeDecode);
  if (parts[0] === "systems" && parts[1] && parts.length > 2) {
    if (image) return `/media/${parts.map(encodeURIComponent).join("/")}`;
    return `${packageFileHref(parts[1], parts.slice(2).join("/"))}${url.hash}`;
  }
  if (!image && parts[0] === "docs")
    return `/docs/${parts.slice(1).join("/").replace(/\.md$/i, "")}${url.hash}`;
  return undefined;
}
export function mediaDetailHref(slug: string, item: ReferenceMedia): string {
  const tab =
    item.kind === "crop"
      ? "components"
      : item.kind === "icon"
        ? "icons"
        : item.kind === "board"
          ? "boards"
          : "screenshots";
  return `/library/${encodeURIComponent(slug)}?tab=${tab}&media=${encodeURIComponent(item.id)}`;
}
