import ReactMarkdown from "react-markdown";
import remarkGfm from "remark-gfm";
import { Children, isValidElement, type ReactNode } from "react";
import { documentHref, headingId } from "@/server/knowledge/docs";
function nodeText(node: ReactNode): string {
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
export function DocumentMarkdown({
  text,
  base,
}: {
  text: string;
  base: string;
}) {
  return (
    <ReactMarkdown
      remarkPlugins={[remarkGfm]}
      urlTransform={(url) => documentHref(base, url) || ""}
      components={{
        h1: ({ children }) => (
          <h1 id={headingId(nodeText(children))}>{children}</h1>
        ),
        h2: ({ children }) => (
          <h2 id={headingId(nodeText(children))}>{children}</h2>
        ),
        h3: ({ children }) => (
          <h3 id={headingId(nodeText(children))}>{children}</h3>
        ),
        h4: ({ children }) => (
          <h4 id={headingId(nodeText(children))}>{children}</h4>
        ),
        a: ({ href, children }) =>
          href ? (
            <a
              href={href}
              {...(/^https?:/.test(href)
                ? { target: "_blank", rel: "noreferrer" }
                : {})}
            >
              {children}
            </a>
          ) : (
            <span>{children}</span>
          ),
        img: ({ src, alt }) =>
          typeof src === "string" && src.startsWith("/media/") ? (
            <img src={src} alt={alt || ""} loading="lazy" />
          ) : (
            <span>{alt || "Recorded image"}</span>
          ),
      }}
    >
      {text}
    </ReactMarkdown>
  );
}
