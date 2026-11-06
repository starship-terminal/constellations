import { Children, isValidElement, type ReactNode } from "react";
/** The plain text of rendered markdown children, however deeply they nest. */
export function nodeText(node: ReactNode): string {
  return Children.toArray(node)
    .map((child) =>
      typeof child === "string" || typeof child === "number"
        ? String(child)
        : isValidElement<{ children?: ReactNode }>(child)
          ? nodeText(child.props.children)
          : "",
    )
    .join("");
}
/** GitHub-style anchor for a heading's text, so captured `file.md#heading` links land. */
export function headingId(text: string): string {
  return text
    .toLowerCase()
    .replace(/[^\p{L}\p{N}\s_-]/gu, "")
    .trim()
    .replace(/\s+/g, "-");
}
