export interface CaptureViewerOrigin {
  id: string;
  element: HTMLElement;
  rect: { left: number; top: number; width: number; height: number };
  url: string;
  width: number;
  height: number;
}

/** Read the clipped thumbnail frame before the dialog locks page scrolling. */
export function captureViewerOrigin(
  trigger: HTMLElement,
  id: string,
): CaptureViewerOrigin | undefined {
  const image = trigger.querySelector("img");
  const element = image?.parentElement;
  if (!image || !element) return;
  const rect = element.getBoundingClientRect();
  if (!rect.width || !rect.height) return;
  return {
    id,
    element,
    rect: {
      left: rect.left,
      top: rect.top,
      width: rect.width,
      height: rect.height,
    },
    url: image.currentSrc || image.src,
    width: image.naturalWidth,
    height: image.naturalHeight,
  };
}

function visibleOrigin(id: string) {
  const frame = [
    ...document.querySelectorAll<HTMLElement>("[data-viewer-source]"),
  ].find((element) => element.dataset.viewerSource === id);
  const origin =
    frame?.parentElement && captureViewerOrigin(frame.parentElement, id);
  if (!origin) return;
  const { left, top, width, height } = origin.rect;
  return left < innerWidth &&
    top < innerHeight &&
    left + width > 0 &&
    top + height > 0
    ? origin
    : undefined;
}

export function reducedViewerMotion() {
  return window.matchMedia("(prefers-reduced-motion: reduce)").matches;
}

/** Retain the previous image independently while React changes capture URLs. */
export function animateViewerDeparture(stage: HTMLElement, direction: number) {
  const image = stage.querySelector<HTMLImageElement>("img");
  if (!image || reducedViewerMotion()) return () => {};
  const bounds = image.getBoundingClientRect();
  const clip = stage.getBoundingClientRect();
  const frame = document.createElement("div");
  Object.assign(frame.style, {
    position: "fixed",
    pointerEvents: "none",
    zIndex: "152",
    overflow: "hidden",
    left: `${bounds.left}px`,
    top: `${Math.max(bounds.top, clip.top)}px`,
    width: `${bounds.width}px`,
    height: `${Math.max(0, Math.min(bounds.bottom, clip.bottom) - Math.max(bounds.top, clip.top))}px`,
  });
  frame.setAttribute("aria-hidden", "true");
  const copy = image.cloneNode() as HTMLImageElement;
  Object.assign(copy.style, {
    display: "block",
    maxWidth: "none",
    maxHeight: "none",
    width: `${bounds.width}px`,
    height: `${bounds.height}px`,
    margin: "0",
    visibility: "visible",
    transform: `translateY(${Math.min(0, bounds.top - clip.top)}px)`,
  });
  frame.append(copy);
  document.body.append(frame);
  const animation = frame.animate(
    [
      { opacity: 1, transform: "translateX(0)" },
      { opacity: 0, transform: `translateX(${-direction * 18}px)` },
    ],
    { duration: 180, easing: "ease-out", fill: "both" },
  );
  const cancel = () => {
    animation.cancel();
    frame.remove();
  };
  void animation.finished.then(cancel, cancel);
  return cancel;
}

/** Geometry belongs to an independent clipped image, never the whole dialog. */
export function animateCaptureViewer({
  content,
  overlay,
  stage,
  id,
  phase,
  origin,
  direction = 1,
}: {
  content: HTMLElement;
  overlay: HTMLElement | null;
  stage: HTMLElement;
  id: string;
  phase: "open" | "close" | "change";
  origin?: CaptureViewerOrigin;
  direction?: number;
}) {
  const animations: Animation[] = [];
  let clone: HTMLDivElement | undefined;
  const image = stage.querySelector<HTMLImageElement>("img");
  let hiddenImage = false;
  let disposed = false;
  const cleanups: (() => void)[] = [];
  const duration = phase === "change" ? 180 : 340;
  const ease = "cubic-bezier(.22,1,.36,1)";
  function run(
    element: HTMLElement | null,
    frames: Keyframe[],
    ms: number,
    delay = 0,
  ) {
    if (!element) return;
    const animation = element.animate(frames, {
      duration: ms,
      easing: ease,
      delay,
      fill: "both",
    });
    animations.push(animation);
    return animation;
  }
  function cleanup() {
    if (disposed) return;
    disposed = true;
    for (const callback of cleanups) callback();
    for (const animation of animations) animation.cancel();
    clone?.remove();
    if (hiddenImage && image) image.style.visibility = "";
  }
  if (reducedViewerMotion())
    return { finished: Promise.resolve(), cancel: cleanup };
  if (phase !== "change") {
    run(
      overlay,
      [
        { opacity: phase === "open" ? 0 : 1 },
        { opacity: phase === "open" ? 1 : 0 },
      ],
      240,
    );
    run(
      content,
      [
        { opacity: phase === "open" ? 0 : 1 },
        { opacity: phase === "open" ? 1 : 0 },
      ],
      phase === "open" ? 200 : 260,
    );
    for (const chrome of content.querySelectorAll<HTMLElement>(
      "[data-viewer-chrome]",
    ))
      run(
        chrome,
        phase === "open"
          ? [
              { opacity: 0, transform: "translateX(18px)" },
              { opacity: 1, transform: "translateX(0)" },
            ]
          : [
              { opacity: 1, transform: "translateX(0)" },
              { opacity: 0, transform: "translateX(10px)" },
            ],
        phase === "open" ? 300 : 180,
        phase === "open" ? 50 : 0,
      );
  }
  const source =
    phase === "close"
      ? origin
        ? visibleOrigin(id)
        : undefined
      : origin?.id === id
        ? origin
        : undefined;
  if (image && source && phase !== "change") {
    const imageRect = image.getBoundingClientRect();
    const stageRect = stage.getBoundingClientRect();
    const destination = {
      left: Math.max(imageRect.left, stageRect.left),
      top: Math.max(imageRect.top, stageRect.top),
      width: Math.max(
        0,
        Math.min(imageRect.right, stageRect.right) -
          Math.max(imageRect.left, stageRect.left),
      ),
      height: Math.max(
        0,
        Math.min(imageRect.bottom, stageRect.bottom) -
          Math.max(imageRect.top, stageRect.top),
      ),
    };
    if (destination.width && destination.height) {
      const start = phase === "open" ? source.rect : destination;
      const end = phase === "open" ? destination : source.rect;
      clone = document.createElement("div");
      clone.setAttribute("aria-hidden", "true");
      clone.dataset.viewerProjection = phase;
      Object.assign(clone.style, {
        position: "fixed",
        zIndex: "153",
        pointerEvents: "none",
        overflow: "hidden",
        left: "0",
        top: "0",
        transformOrigin: "top left",
        background: "var(--surface)",
      });
      const copy = document.createElement("img");
      copy.src = phase === "open" ? source.url : image.currentSrc || image.src;
      copy.alt = "";
      Object.assign(copy.style, {
        display: "block",
        width: "100%",
        height: "100%",
        objectFit: "cover",
        objectPosition: "top",
      });
      clone.append(copy);
      document.body.append(clone);
      image.style.visibility = "hidden";
      hiddenImage = true;
      run(
        clone,
        [
          {
            transform: `translate(${start.left}px, ${start.top}px)`,
            width: `${start.width}px`,
            height: `${start.height}px`,
            borderRadius: phase === "open" ? "6px" : "0px",
          },
          {
            transform: `translate(${end.left}px, ${end.top}px)`,
            width: `${end.width}px`,
            height: `${end.height}px`,
            borderRadius: phase === "open" ? "0px" : "6px",
          },
        ],
        duration,
      );
    }
  }
  if (!clone && image && phase !== "close")
    run(
      image,
      [
        {
          opacity: 0,
          transform: `translateX(${phase === "change" ? direction * 18 : 0}px)`,
        },
        { opacity: 1, transform: "translateX(0)" },
      ],
      phase === "change" ? duration : 200,
    );
  const finished = Promise.all(
    animations.map((animation) => animation.finished.catch(() => undefined)),
  ).then(() => {
    // A thumbnail is already available on card opens. Keep its final projected
    // frame until the original image is ready, then swap without a blank frame.
    if (phase === "open" && clone && image && !image.complete && !disposed) {
      const reveal = () => cleanup();
      image.addEventListener("load", reveal, { once: true });
      image.addEventListener("error", reveal, { once: true });
      cleanups.push(() => {
        image.removeEventListener("load", reveal);
        image.removeEventListener("error", reveal);
      });
    } else if (phase !== "close") cleanup();
  });
  return { finished, cancel: cleanup };
}
