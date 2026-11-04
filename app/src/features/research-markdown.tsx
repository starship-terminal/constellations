/** Markdown is untrusted prose. Image URLs must never cause browser requests. */
export function MarkdownImageAsText({ alt }: { alt?: string }) {
  return <span>{alt ? `[Image: ${alt}]` : "[Image omitted]"}</span>;
}
