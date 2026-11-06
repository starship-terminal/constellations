"use client";
import {
  useCallback,
  useEffect,
  useRef,
  useState,
  type KeyboardEventHandler,
  type ReactNode,
  type RefObject,
  type SetStateAction,
} from "react";
import {
  LoaderCircle,
  X,
  Check,
  ChevronDown,
  Copy,
  Download,
  ArrowUpRight,
} from "lucide-react";
import * as Dialog from "@radix-ui/react-dialog";
export async function api<T = any>(
  url: string,
  options?: RequestInit,
): Promise<T> {
  const r = await fetch(url, {
    ...options,
    headers: { "Content-Type": "application/json", ...options?.headers },
  });
  const data = await r.json().catch(() => ({}));
  if (!r.ok)
    throw new Error(
      data.error || data.message || `Request failed (${r.status})`,
    );
  return data;
}
interface ResourceState<T> {
  url: string;
  data: T | null;
  error: string;
  loading: boolean;
}
/**
 * What a useResource caller sees for `url`. State fetched for another URL is
 * never shown: until the new request settles the caller gets loading and no
 * data, so a page keyed on the new URL cannot mount with the old response.
 */
export function resourceView<T>(
  state: ResourceState<T>,
  url: string,
): Omit<ResourceState<T>, "url"> {
  return state.url === url
    ? { data: state.data, error: state.error, loading: state.loading }
    : { data: null, error: "", loading: true };
}
export function useResource<T>(url: string) {
  const [state, setState] = useState<ResourceState<T>>({
    url,
    data: null,
    error: "",
    loading: true,
  });
  useEffect(() => {
    let alive = true;
    setState({ url, data: null, error: "", loading: true });
    api<T>(url)
      .then((data) => {
        if (alive) setState({ url, data, error: "", loading: false });
      })
      .catch((e) => {
        if (alive)
          setState({ url, data: null, error: e.message, loading: false });
      });
    return () => {
      alive = false;
    };
  }, [url]);
  const setData = useCallback(
    (action: SetStateAction<T | null>) =>
      setState((previous) =>
        previous.url === url
          ? {
              ...previous,
              data:
                typeof action === "function"
                  ? (action as (value: T | null) => T | null)(previous.data)
                  : action,
            }
          : previous,
      ),
    [url],
  );
  return { ...resourceView(state, url), setData };
}
export function Spinner({ label = "Loading…" }: { label?: string }) {
  return (
    <div className="loading-state" role="status">
      <LoaderCircle className="spin" size={19} />
      <span>{label}</span>
    </div>
  );
}
export type SkeletonShape =
  | "card"
  | "web"
  | "ios"
  | "browse"
  | "screen"
  | "screen-ios"
  | "style"
  | "tile"
  | "collection"
  | "list";
export function SkeletonCard({ shape = "card" }: { shape?: SkeletonShape }) {
  return (
    <div className={`card-skeleton card-skeleton-${shape}`} aria-hidden="true">
      <div className="card-skeleton-media" />
      <span className="card-skeleton-line" />
    </div>
  );
}
export function SkeletonGrid({
  shape = "card",
  count = 6,
  className = "",
  label = "Loading…",
}: {
  shape?: SkeletonShape;
  count?: number;
  className?: string;
  label?: string;
}) {
  return (
    <div className={className} role="status" aria-label={label}>
      {Array.from({ length: count }, (_, i) => (
        <SkeletonCard key={i} shape={shape} />
      ))}
    </div>
  );
}
export function Empty({
  title,
  children,
}: {
  title: string;
  children?: ReactNode;
}) {
  return (
    <div className="empty-state">
      <span className="empty-glyph">✳</span>
      <h2>{title}</h2>
      <div>{children}</div>
    </div>
  );
}
export function ErrorState({
  message,
  retry,
}: {
  message: string;
  retry?: () => void;
}) {
  return (
    <div className="notice error" role="alert">
      <p>{message}</p>
      {retry && (
        <button className="pill" onClick={retry}>
          Try again
        </button>
      )}
    </div>
  );
}
export function Modal({
  open,
  onOpenChange,
  title,
  description,
  children,
  className = "",
}: {
  open: boolean;
  onOpenChange: (open: boolean) => void;
  title: string;
  description?: string;
  children: ReactNode;
  className?: string;
}) {
  return (
    <Dialog.Root open={open} onOpenChange={onOpenChange}>
      <Dialog.Portal>
        <Dialog.Overlay className="modal-overlay" />
        <Dialog.Content
          className={`modal ${className}`}
          aria-describedby={description ? "modal-description" : undefined}
        >
          <header className="modal-header">
            <div>
              <Dialog.Title>{title}</Dialog.Title>
              {description && (
                <Dialog.Description id="modal-description">
                  {description}
                </Dialog.Description>
              )}
            </div>
            <Dialog.Close className="icon-button" aria-label="Close">
              <X size={20} />
            </Dialog.Close>
          </header>
          {children}
        </Dialog.Content>
      </Dialog.Portal>
    </Dialog.Root>
  );
}
export function CopyButton({
  value,
  label = "Copy",
}: {
  value: string;
  label?: string;
}) {
  const [copied, setCopied] = useState(false);
  const [error, setError] = useState("");
  return (
    <>
      <button
        className="pill small"
        onClick={async () => {
          try {
            await navigator.clipboard.writeText(value);
            setCopied(true);
            setTimeout(() => setCopied(false), 1800);
          } catch {
            setError("Clipboard unavailable. Select and copy the text below.");
          }
        }}
      >
        {copied ? <Check size={14} /> : <Copy size={14} />}{" "}
        {copied ? "Copied" : label}
      </button>
      {error && (
        <span role="status" className="muted">
          {error}
        </span>
      )}
    </>
  );
}
export function download(value: string, name: string, type = "text/plain") {
  const blob = new Blob([value], { type });
  const u = URL.createObjectURL(blob);
  const a = document.createElement("a");
  a.href = u;
  a.download = name;
  a.click();
  setTimeout(() => URL.revokeObjectURL(u), 1000);
}
export function DownloadButton({
  value,
  name,
  label = "Download",
}: {
  value: string;
  name: string;
  label?: string;
}) {
  return (
    <button className="pill small" onClick={() => download(value, name)}>
      <Download size={14} />
      {label}
    </button>
  );
}
export function External({
  href,
  children,
}: {
  href: string;
  children: ReactNode;
}) {
  return (
    <a href={href} target="_blank" rel="noreferrer" className="pill small">
      {children}
      <ArrowUpRight size={14} />
    </a>
  );
}
function menuKeys(
  root: RefObject<HTMLDivElement | null>,
  open: boolean,
): KeyboardEventHandler<HTMLDivElement> {
  return (event) => {
    if (!open || (event.key !== "ArrowDown" && event.key !== "ArrowUp")) return;
    event.preventDefault();
    const items = Array.from(
      root.current?.querySelectorAll<HTMLElement>(".select-option") || [],
    );
    if (!items.length) return;
    const index = items.indexOf(document.activeElement as HTMLElement);
    const next =
      event.key === "ArrowDown"
        ? (index + 1) % items.length
        : (index - 1 + items.length) % items.length;
    items[next]?.focus();
  };
}
function useMenuDismiss(
  root: RefObject<HTMLDivElement | null>,
  open: boolean,
  setOpen: (open: boolean) => void,
  refocus?: () => void,
) {
  useEffect(() => {
    if (!open) return;
    const close = (event: MouseEvent) => {
      if (!root.current?.contains(event.target as Node)) setOpen(false);
    };
    const escape = (event: KeyboardEvent) => {
      if (event.key === "Escape") {
        setOpen(false);
        refocus?.();
      }
    };
    document.addEventListener("mousedown", close);
    document.addEventListener("keydown", escape);
    return () => {
      document.removeEventListener("mousedown", close);
      document.removeEventListener("keydown", escape);
    };
  }, [open, root, setOpen, refocus]);
}
export function Select({
  value,
  onChange,
  options,
  label,
  disabled = false,
  compact = false,
}: {
  value: string;
  onChange: (value: string) => void;
  options: { value: string; label: string }[];
  label: string;
  disabled?: boolean;
  compact?: boolean;
}) {
  const [open, setOpen] = useState(false);
  const root = useRef<HTMLDivElement>(null);
  const trigger = useRef<HTMLButtonElement>(null);
  useMenuDismiss(root, open, setOpen, () => trigger.current?.focus());
  useEffect(() => {
    if (open)
      root.current
        ?.querySelector<HTMLElement>('.select-option[aria-selected="true"]')
        ?.focus();
  }, [open]);
  const current = options.find((option) => option.value === value);
  return (
    <div
      className={`select${compact ? " compact" : ""}`}
      ref={root}
      onKeyDown={menuKeys(root, open)}
    >
      <button
        type="button"
        className="select-trigger"
        ref={trigger}
        disabled={disabled}
        aria-haspopup="listbox"
        aria-expanded={open}
        aria-label={`${label}: ${current?.label ?? value}`}
        onClick={() => setOpen((v) => !v)}
      >
        <span>{current?.label ?? value}</span>
        <ChevronDown size={14} />
      </button>
      {open && (
        <div className="select-menu" role="listbox" aria-label={label}>
          {options.map((option) => (
            <button
              key={option.value}
              type="button"
              role="option"
              aria-selected={option.value === value}
              className="select-option"
              onClick={() => {
                if (option.value !== value) onChange(option.value);
                setOpen(false);
                trigger.current?.focus();
              }}
            >
              <span>{option.label}</span>
              {option.value === value && <Check size={14} />}
            </button>
          ))}
        </div>
      )}
    </div>
  );
}
export function Combobox({
  value,
  onChange,
  options,
  label,
  placeholder,
  disabled = false,
  required = false,
}: {
  value: string;
  onChange: (value: string) => void;
  options: string[];
  label: string;
  placeholder?: string;
  disabled?: boolean;
  required?: boolean;
}) {
  const [open, setOpen] = useState(false);
  const [matches, setMatches] = useState<string[]>(options);
  const root = useRef<HTMLDivElement>(null);
  const input = useRef<HTMLInputElement>(null);
  const suppressOpen = useRef(false);
  // Refocusing after a dismiss fires onFocus; the flag keeps the menu closed.
  const refocusInput = () => {
    if (document.activeElement === input.current) return;
    suppressOpen.current = true;
    input.current?.focus();
  };
  useMenuDismiss(root, open, setOpen, refocusInput);
  useEffect(() => {
    // The option list arrives once per test; typing only re-filters it here.
    const timer = setTimeout(() => {
      const query = value.trim().toLowerCase();
      setMatches(
        query
          ? options.filter((option) => option.toLowerCase().includes(query))
          : options,
      );
    }, 150);
    return () => clearTimeout(timer);
  }, [value, options]);
  return (
    <div
      className="select combobox"
      ref={root}
      onKeyDown={menuKeys(root, open)}
    >
      <input
        role="combobox"
        aria-expanded={open && options.length > 0}
        aria-label={label}
        aria-autocomplete="list"
        autoComplete="off"
        spellCheck={false}
        disabled={disabled}
        required={required}
        placeholder={placeholder}
        ref={input}
        value={value}
        onChange={(event) => {
          onChange(event.target.value);
          setOpen(true);
        }}
        onFocus={() => {
          if (suppressOpen.current) suppressOpen.current = false;
          else setOpen(true);
        }}
        onBlur={(event) => {
          if (!root.current?.contains(event.relatedTarget as Node))
            setOpen(false);
        }}
      />
      {open && options.length > 0 && (
        <div className="select-menu" role="listbox" aria-label={label}>
          {matches.length ? (
            matches.slice(0, 50).map((option) => (
              <button
                key={option}
                type="button"
                role="option"
                aria-selected={option === value}
                className="select-option"
                onMouseDown={(event) => event.preventDefault()}
                onClick={() => {
                  onChange(option);
                  setOpen(false);
                  refocusInput();
                }}
              >
                <span>{option}</span>
                {option === value && <Check size={14} />}
              </button>
            ))
          ) : (
            <p className="select-hint">
              No matching models. The typed ID is used as-is.
            </p>
          )}
        </div>
      )}
    </div>
  );
}
export function MediaPreview({
  image,
  video,
  name,
  always = false,
}: {
  image: string | null;
  video?: string | null;
  name: string;
  always?: boolean;
}) {
  const ref = useRef<HTMLVideoElement>(null),
    container = useRef<HTMLDivElement>(null);
  const [playing, setPlaying] = useState(false);
  const active = useRef(false);
  useEffect(() => {
    const node = container.current;
    if (!node) return;
    const observer = new IntersectionObserver(
      (entries) => {
        if (!entries[0].isIntersecting) {
          ref.current?.pause();
          setPlaying(false);
        } else if (
          always &&
          !matchMedia("(prefers-reduced-motion: reduce)").matches
        ) {
          ref.current
            ?.play()
            .then(() => setPlaying(true))
            .catch(() => {});
        }
      },
      { threshold: 0.15 },
    );
    observer.observe(node);
    const pause = () => {
      if (document.hidden) {
        ref.current?.pause();
        setPlaying(false);
      }
    };
    document.addEventListener("visibilitychange", pause);
    return () => {
      observer.disconnect();
      document.removeEventListener("visibilitychange", pause);
    };
  }, [always, video]);
  function start() {
    active.current = true;
    if (matchMedia("(prefers-reduced-motion: reduce)").matches) return;
    ref.current
      ?.play()
      .then(() => {
        if (active.current) setPlaying(true);
      })
      .catch(() => {});
  }
  function stop() {
    active.current = false;
    ref.current?.pause();
    setPlaying(false);
  }
  return (
    <div
      className="media-preview"
      ref={container}
      onMouseEnter={start}
      onMouseLeave={stop}
      onFocus={start}
      onBlur={stop}
    >
      {image ? (
        <img
          src={image}
          alt={`${name} design preview`}
          loading="lazy"
          decoding="async"
        />
      ) : (
        <div className="media-missing">
          <span>{name.slice(0, 1)}</span>
          <small>Preview unavailable</small>
        </div>
      )}
      {video && (
        <video
          ref={ref}
          src={video}
          muted
          loop
          playsInline
          preload="none"
          className={playing ? "playing" : ""}
          aria-label={`${name} scrolling preview`}
        />
      )}
    </div>
  );
}
